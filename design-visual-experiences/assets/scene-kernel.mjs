// Original renderer-neutral scene helpers. Seconds and explicit source PTS.
// No provider, DOM, playback clock, brand, or creative acceptance defaults.
import {hermite} from './motion-kernel.mjs';

const fail = message => { throw new Error(message); };
const finite = (n, label) => Number.isFinite(n) || fail(`${label}: expected finite number`);
const keys = (o, allowed, label) => {
  if (!o || typeof o !== 'object' || Array.isArray(o)) fail(`${label}: expected object`);
  for (const k of Object.keys(o)) if (!allowed.includes(k)) fail(`${label}: unknown ${k}`);
};
const id = (s, label) => typeof s === 'string' && /^[A-Za-z][\w-]*$/.test(s) || fail(`${label}: invalid id`);
const copy = x => structuredClone(x);
const curves = {
  linear: u => u,
  smooth: u => u*u*(3-2*u),
  smoother: u => u*u*u*(u*(u*6-15)+10),
  out4: u => 1-(1-u)**4,
};

/** Compile a finite numeric motion plan. Tracks own channels over [at,end).
 * Values hold between tracks. Discontinuities require cut:true; flowing
 * waypoints can use hermite with explicit velocities in units/second. */
export function compileScene(input) {
  const plan = copy(input);
  keys(plan, ['duration','cues','objects','tracks'], 'scene');
  finite(plan.duration, 'duration');
  if (plan.duration <= 0) fail('duration must be positive');
  const cueDefs = plan.cues ?? {}, cues = Object.create(null), visiting = new Set();
  keys(cueDefs, Object.keys(cueDefs), 'cues');
  function resolve(ref) {
    if (typeof ref === 'number') { finite(ref,'time'); return ref; }
    keys(ref, ['cue','offset'], 'time reference');
    return cue(ref.cue) + (ref.offset === undefined ? 0 : (finite(ref.offset,'offset'),ref.offset));
  }
  function cue(name) {
    id(name,'cue');
    if (Object.hasOwn(cues,name)) return cues[name];
    if (!Object.hasOwn(cueDefs,name)) fail(`missing cue ${name}`);
    if (visiting.has(name)) fail(`cyclic cue ${name}`);
    visiting.add(name);
    const value = resolve(cueDefs[name]);
    if (value < 0 || value > plan.duration) fail(`cue ${name} outside scene`);
    visiting.delete(name); cues[name] = value; return value;
  }
  Object.keys(cueDefs).forEach(cue);
  keys(plan.objects, Object.keys(plan.objects ?? {}), 'objects');
  const channels = new Map(), initial = Object.create(null);
  for (const [name, object] of Object.entries(plan.objects)) {
    id(name,'object'); keys(object,['values','stationary'],'object');
    if (object.stationary !== undefined && typeof object.stationary !== 'boolean') fail('stationary must be boolean');
    keys(object.values,Object.keys(object.values ?? {}),'values');
    initial[name] = Object.create(null);
    for (const [property,value] of Object.entries(object.values)) {
      id(property,'property'); finite(value,property); initial[name][property] = value;
      channels.set(`${name}.${property}`,[]);
    }
  }
  if (!Array.isArray(plan.tracks)) fail('tracks must be an array');
  for (const track of plan.tracks) {
    keys(track,['target','property','at','end','from','to','ease','v0','v1','cut'],'track');
    const channel = channels.get(`${track.target}.${track.property}`);
    if (!channel) fail(`unknown target/property ${track.target}.${track.property}`);
    if (plan.objects[track.target].stationary) fail(`stationary object ${track.target} has a track`);
    for (const field of ['from','to']) finite(track[field],field);
    if (track.cut !== undefined && typeof track.cut !== 'boolean') fail('cut must be boolean');
    const at = resolve(track.at), end = resolve(track.end), ease = track.ease ?? 'linear';
    if (at < 0 || end > plan.duration || end <= at) fail('track outside lifetime or empty');
    if (!Object.hasOwn(curves,ease) && ease !== 'hermite') fail(`unknown easing ${ease}`);
    for (const field of ['v0','v1']) {
      if (track[field] !== undefined) {
        finite(track[field],field);
        if (ease !== 'hermite') fail('velocity requires hermite');
      }
    }
    channel.push({...track,at,end,ease});
  }
  for (const [name, tracks] of channels) {
    tracks.sort((a,b)=>a.at-b.at);
    const [object,property] = name.split('.');
    let end = 0, value = initial[object][property];
    for (const track of tracks) {
      if (track.at < end) fail(`conflicting writers on ${name}`);
      if (track.from !== value && !track.cut) fail(`unmarked discontinuity on ${name}`);
      end = track.end; value = track.to;
    }
  }
  function sample(time) {
    finite(time,'sample time');
    if (time < 0 || time > plan.duration) fail('sample outside scene');
    const state = copy(initial);
    for (const [name,tracks] of channels) {
      const [object,property] = name.split('.');
      for (const track of tracks) {
        if (time < track.at) break;
        if (time >= track.end) state[object][property] = track.to;
        else {
          const u = (time-track.at)/(track.end-track.at);
          state[object][property] = track.ease === 'hermite'
            ? hermite(time,track.at,track.end,track.from,track.to,track.v0??0,track.v1??0)
            : track.from+(track.to-track.from)*curves[track.ease](u);
          break;
        }
      }
    }
    return state;
  }
  return Object.freeze({duration:plan.duration,cues:Object.freeze({...cues}),sample});
}

/** Hard-cut inner edit, independent of outer camera/parent transforms.
 * PTS are normalized to the source's first displayed frame. Sampling explicitly
 * holds the latest source frame; it does not interpolate or claim native cadence
 * when delivery cadence differs. End is exclusive; a replay must pass a new time. */
export function compileSequence(input) {
  const plan = copy(input);
  keys(plan,['sources','clips'],'sequence');
  keys(plan.sources,Object.keys(plan.sources??{}),'sources');
  for (const [name,source] of Object.entries(plan.sources)) {
    id(name,'source'); keys(source,['duration','pts'],'source');
    finite(source.duration,'source duration');
    if (!(source.duration > 0) || !Array.isArray(source.pts) || !source.pts.length || source.pts[0]!==0) fail('source requires positive duration and normalized PTS');
    source.pts.forEach((t,i)=>{
      finite(t,'PTS');
      if (t<0 || t>=source.duration || (i && t<=source.pts[i-1])) fail('PTS must increase within source');
    });
  }
  if (!Array.isArray(plan.clips) || !plan.clips.length) fail('sequence needs clips');
  let duration = 0;
  const clips = plan.clips.map(clip=>{
    keys(clip,['source','in','out','rate'],'clip');
    const source = plan.sources[clip.source];
    if (!Object.hasOwn(plan.sources,clip.source)) fail(`missing source ${clip.source}`);
    for (const f of ['in','out']) finite(clip[f],f);
    const rate=clip.rate??1; finite(rate,'rate');
    if (rate<=0 || clip.in<0 || clip.out>source.duration || clip.out<=clip.in) fail('invalid source trim/rate');
    const start=duration; duration+=(clip.out-clip.in)/rate;
    return {...clip,rate,start,end:duration};
  });
  function sample(time) {
    finite(time,'sequence time');
    if (time<0 || time>=duration) return null;
    const clipIndex=clips.findIndex(c=>time<c.end),clip=clips[clipIndex];
    const sourceTime=clip.in+(time-clip.start)*clip.rate,pts=plan.sources[clip.source].pts;
    let lo=0,hi=pts.length;
    while(lo<hi){const mid=(lo+hi)>>>1;if(pts[mid]<=sourceTime)lo=mid+1;else hi=mid;}
    const frameIndex=lo-1;
    return {clipIndex,source:clip.source,sourceTime,frameIndex,pts:pts[frameIndex]};
  }
  return Object.freeze({duration,sample});
}

/** Center an object on a screen-space attention point under a uniform camera. */
export function focalPlacement({viewport,camera,focus,size}) {
  for (const pair of [viewport,focus,size]) if (!Array.isArray(pair)||pair.length!==2||pair.some(n=>!Number.isFinite(n))) fail('expected finite pair');
  keys(camera,['x','y','scale'],'camera');
  for (const value of Object.values(camera)) finite(value,'camera');
  if (![camera.x,camera.y,camera.scale].every(Number.isFinite) || camera.scale<=0 || [...viewport,...size].some(n=>n<=0)) fail('invalid dimensions/camera');
  const w=size[0]/camera.scale,h=size[1]/camera.scale;
  return {x:camera.x+(focus[0]-viewport[0]/2)/camera.scale-w/2,
    y:camera.y+(focus[1]-viewport[1]/2)/camera.scale-h/2,w,h};
}

/** Receipt freshness only, never an automatic assessment of taste.
 * Caller supplies actual current hashes for code, recipe, assets, brand and export. */
export function reviewState(receipt,current,{playback=true,audio=false}={}) {
  const issues=[];
  if (!receipt || !receipt.hashes || Object.keys(current).length===0) return {status:'pending',issues:['missing evidence']};
  for (const key of ['export','assets','code','recipe','brand']) {
    if (typeof current[key]!=='string' || !/^[a-f0-9]{64}$/.test(current[key])) issues.push(`missing SHA-256 ${key}`);
  }
  for (const key of new Set([...Object.keys(current),...Object.keys(receipt.hashes)])) {
    if (!current[key] || current[key]!==receipt.hashes[key]) issues.push(`stale ${key}`);
  }
  if (receipt.technical!=='passed') issues.push('technical review pending');
  if (receipt.visual!=='reviewed') issues.push('visual review pending');
  if (playback && receipt.playback!=='observed') issues.push('playback not observed');
  if (audio && receipt.audio!=='heard') issues.push('audio not heard');
  if (receipt.human!=='approved') issues.push('human approval pending');
  return {status:issues.length?'pending':'approved',issues};
}
