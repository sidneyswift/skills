import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {compileScene,compileSequence,focalPlacement,reviewState} from '../assets/scene-kernel.mjs';

const make=()=>({duration:4,cues:{send:1,result:{cue:'send',offset:.5}},
  objects:{card:{values:{x:0,opacity:0}},label:{stationary:true,values:{x:30}}},
  tracks:[{target:'card',property:'x',at:{cue:'result'},end:3,from:0,to:100,ease:'smoother'},
    {target:'card',property:'opacity',at:1,end:1.5,from:0,to:1}]});
const p=make(),scene=compileScene(p);
assert.equal(scene.sample(0).card.opacity,0);
assert.equal(scene.sample(1.5).card.x,0);
assert.equal(scene.sample(2.25).card.x,50);
assert.equal(scene.sample(3).card.x,100);
assert.equal(scene.sample(4).label.x,30);
assert.deepEqual(scene.sample(2.25),scene.sample(2.25));
scene.sample(4);scene.sample(0);assert.equal(scene.sample(2.25).card.x,50);
p.tracks[0].to=999;assert.equal(scene.sample(3).card.x,100,'compiled state isolated from later edits');
const shifted=make();shifted.cues.send=1.25;
assert.equal(compileScene(shifted).cues.result,1.75,'dependent event follows edit');
for (const [mutate,message] of [
  [p=>p.tracks.push({...p.tracks[0],at:2}),/conflicting/],
  [p=>p.tracks[0].at={cue:'missing'},/missing cue/],
  [p=>p.cues.send={cue:'result'},/cyclic/],
  [p=>p.tracks[0].target='missing',/unknown target/],
  [p=>p.tracks[0].end=5,/outside/],
  [p=>p.tracks[0].end=1,/outside/],
  [p=>p.tracks[0].to=NaN,/finite/],
  [p=>p.tracks[0].from=20,/unmarked/],
  [p=>p.tracks[0].ease='generic-bounce',/unknown easing/],
  [p=>p.tracks[0].v0=1,/velocity/],
  [p=>p.objects.card.stationary=true,/stationary/],
  [p=>p.tracks[0].typo=1,/unknown/],
]) {const p=make();mutate(p);assert.throws(()=>compileScene(p),message);}
const cut=make();cut.tracks[0].from=20;cut.tracks[0].cut=true;
assert.equal(compileScene(cut).sample(1.5).card.x,20);
const flowing=compileScene({duration:2,objects:{dot:{values:{x:0}}},tracks:[
  {target:'dot',property:'x',at:0,end:1,from:0,to:10,ease:'hermite',v0:10,v1:10},
  {target:'dot',property:'x',at:1,end:2,from:10,to:20,ease:'hermite',v0:10,v1:10}]});
const eps=.00001;
assert.ok(Math.abs((flowing.sample(1).dot.x-flowing.sample(1-eps).dot.x)/eps-10)<1e-6);
assert.ok(Math.abs((flowing.sample(1+eps).dot.x-flowing.sample(1).dot.x)/eps-10)<1e-6);
assert.throws(()=>scene.sample(-1),/outside/);

// Explicit held-PTS sampling across unlike source cadences and nonzero trims.
const sequencePlan={sources:{a:{duration:1,pts:[0,.1,.21,.3,.5,.8]},b:{duration:1,pts:[0,.25,.5,.75]}},
  clips:[{source:'a',in:.21,out:.5},{source:'b',in:.25,out:1}]};
const edit=compileSequence(sequencePlan),boundary=.5-.21;
assert.equal(edit.sample(0).frameIndex,2);
assert.equal(edit.sample(boundary-1e-8).source,'a');
assert.equal(edit.sample(boundary).source,'b');
assert.equal(edit.sample(boundary).frameIndex,1);
assert.equal(edit.sample(edit.duration),null);
assert.equal(edit.sample(-1),null);
assert.deepEqual(edit.sample(.2),edit.sample(.2));
const mapping=edit.sample(.45);
for(const scale of [1,2,7]) {
  const camera={x:430,y:200,scale};
  const g=focalPlacement({viewport:[1920,1080],camera,focus:[650,430],size:[720,405]});
  assert.ok(Math.abs(960+(g.x+g.w/2-camera.x)*scale-650)<1e-9);
  assert.ok(Math.abs(540+(g.y+g.h/2-camera.y)*scale-430)<1e-9);
  assert.deepEqual(edit.sample(.45),mapping,'outer camera cannot reset inner edit');
}
for(const [mutate,message] of [
  [p=>p.sources.a.pts=[0,.2,.1],/increase/],
  [p=>p.sources.a.pts=[.1,.2],/normalized/],
  [p=>p.clips[0].source='absent',/missing source/],
  [p=>p.clips[0].out=2,/trim/],
  [p=>p.clips[0].rate=0,/trim/],
]) {const p=structuredClone(sequencePlan);mutate(p);assert.throws(()=>compileSequence(p),message);}
assert.throws(()=>focalPlacement({viewport:[10,10],camera:{x:0,y:0,scale:0},focus:[5,5],size:[4,4]}),/invalid/);

const hashes=Object.fromEntries(['export','assets','code','recipe','brand'].map(key=>[key,createHash('sha256').update(key).digest('hex')]));
const receipt={hashes,technical:'passed',visual:'reviewed',playback:'observed',audio:'heard',human:'approved'};
assert.equal(reviewState(receipt,hashes,{audio:true}).status,'approved');
for(const key of Object.keys(hashes)) assert.equal(reviewState(receipt,{...hashes,[key]:'changed'}).status,'pending');
for(const [key,value] of [['audio','unavailable'],['playback','unavailable'],['human','pending'],['visual','sampled'],['technical','failed']])
  assert.equal(reviewState({...receipt,[key]:value},hashes,{audio:true}).status,'pending');
assert.equal(reviewState(receipt,{}).status,'pending');
const partial={export:hashes.export};
assert.equal(reviewState({...receipt,hashes:partial},partial).status,'pending');
assert.equal(reviewState(null,hashes).status,'pending');
console.log('PASS: cue dependencies, ownership failures, deterministic seek, velocity continuity, PTS cuts, focal placement and stale-review rejection');
