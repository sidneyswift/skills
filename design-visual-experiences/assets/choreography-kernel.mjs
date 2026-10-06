// Original optional choreography constraints. No brand, genre or reference timings.
import {compileScene} from './scene-kernel.mjs';
const fail = message => { throw new Error(message); };
const finite = (x, name) => Number.isFinite(x) || fail(`${name}: expected finite number`);
const fields = (o, names, label) => {
  if (!o || typeof o !== 'object' || Array.isArray(o)) fail(`${label}: expected object`);
  for (const name of Object.keys(o)) if (!names.includes(name)) fail(`${label}: unknown ${name}`);
};
const phase = (t, a, b) => Math.max(0, Math.min(1, (t-a)/(b-a)));
const out = u => 1-(1-u)**3;
const travel = u => u*u*u*(u*(u*6-15)+10);

/** Separate rise, stable hold and fall; no inferred universal timing. */
export function visibilityEnvelope(t, timing) {
  fields(timing, ['enter','ready','exit','gone'], 'visibility');
  const {enter,ready,exit,gone} = timing;
  [t,enter,ready,exit,gone].forEach(x=>finite(x,'visibility time'));
  if (!(enter<ready && ready<=exit && exit<gone)) fail('invalid visibility order');
  return out(phase(t,enter,ready))*(1-travel(phase(t,exit,gone)));
}

/** Transient scale response with exact rest outside its interval. */
export function pressScale(t, options) {
  fields(options, ['at','duration','depth'], 'press');
  const {at,duration,depth} = options;
  [t,at,duration,depth].forEach(x=>finite(x,'press value'));
  if (duration<=0 || depth<0 || depth>=1) fail('invalid press duration/depth');
  if (t<=at || t>=at+duration) return 1;
  return 1-depth*Math.sin(Math.PI*(t-at)/duration);
}

/** Wrap numeric scene sampling with declared temporal and readable-hold bounds.
 * These checks do not inspect pixels, certify taste or grant human approval.
 * Every rendered frame must use sample(); unsampled times are not certified. */
export function compileChoreography(input) {
  fields(input, ['scene','relations','holds'], 'choreography');
  const plan = structuredClone(input), scene = compileScene(plan.scene);
  const initial = scene.sample(0), ids = new Set();
  const unique = name => {
    if (typeof name!=='string' || !/^[A-Za-z][\w-]*$/.test(name) || ids.has(name)) fail('invalid or duplicate constraint id');
    ids.add(name);
  };
  const time = ref => {
    let t;
    if (typeof ref==='number') t=ref;
    else {
      fields(ref,['cue','offset'],'constraint time');
      if (!Object.hasOwn(scene.cues,ref.cue)) fail(`missing cue ${ref.cue}`);
      const offset=ref.offset??0; finite(offset,'offset');
      t=scene.cues[ref.cue]+offset;
    }
    finite(t,'constraint time');
    if (t<0 || t>scene.duration) fail('constraint outside scene');
    return t;
  };
  const relations=plan.relations??[], holds=plan.holds??[];
  if (!Array.isArray(relations)||!Array.isArray(holds)) fail('constraints must be arrays');
  for (const relation of relations) {
    fields(relation,['id','before','after','minGap'],'relation'); unique(relation.id);
    finite(relation.minGap,'minimum gap');
    if (relation.minGap<0) fail('minimum gap must be nonnegative');
    if (time(relation.after)-time(relation.before)+1e-9<relation.minGap) fail(`insufficient gap: ${relation.id}`);
  }
  const compiled=holds.map(hold=>{
    fields(hold,['id','at','end','channels'],'hold'); unique(hold.id);
    const at=time(hold.at),end=time(hold.end);
    if (end<=at || !Array.isArray(hold.channels) || !hold.channels.length) fail('hold needs interval and channels');
    const seen=new Set();
    for (const channel of hold.channels) {
      fields(channel,['target','property','min','max'],'hold channel');
      if (!Object.hasOwn(initial,channel.target)||!Object.hasOwn(initial[channel.target],channel.property)) fail('unknown hold channel');
      const key=`${channel.target}.${channel.property}`;
      if (seen.has(key)) fail('duplicate hold channel'); seen.add(key);
      finite(channel.min,'minimum');finite(channel.max,'maximum');
      if (channel.max<channel.min) fail('invalid hold bounds');
    }
    return {...hold,at,end};
  });
  function sample(t) {
    const state=scene.sample(t);
    for (const hold of compiled) if (t>=hold.at && t<hold.end) {
      for (const channel of hold.channels) {
        const value=state[channel.target][channel.property];
        if (value<channel.min-1e-9 || value>channel.max+1e-9)
          fail(`hold ${hold.id}: ${channel.target}.${channel.property} outside bounds at ${t}`);
      }
    }
    return state;
  }
  return Object.freeze({duration:scene.duration,cues:scene.cues,sample});
}

/** Use actual selected source hashes, never filenames, for explicit rejections. */
export function assertSelectedAssets(selectedHashes, rejectedHashes) {
  for (const list of [selectedHashes,rejectedHashes]) {
    if (!Array.isArray(list) || list.some(s=>typeof s!=='string'||!/^[a-f0-9]{64}$/.test(s))) fail('asset lists require SHA-256 hashes');
  }
  const rejected=new Set(rejectedHashes);
  for (const hash of selectedHashes) if (rejected.has(hash)) fail(`rejected asset selected: ${hash}`);
  return true;
}
