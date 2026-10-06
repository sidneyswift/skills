import assert from 'node:assert/strict';
import {compileChoreography,pressScale,visibilityEnvelope,assertSelectedAssets} from '../assets/choreography-kernel.mjs';
const make=()=>({scene:{duration:4,cues:{ready:1,complete:1.5,act:2,exit:2.5,gone:2.75},
  objects:{panel:{values:{opacity:0,x:0}},camera:{values:{zoom:1}}},tracks:[
    {target:'panel',property:'opacity',at:0,end:{cue:'ready'},from:0,to:1},
    {target:'panel',property:'x',at:{cue:'exit'},end:{cue:'gone'},from:0,to:100,ease:'smoother'},
    {target:'panel',property:'opacity',at:{cue:'exit'},end:{cue:'gone'},from:1,to:0}]},
  relations:[{id:'read-before-act',before:{cue:'complete'},after:{cue:'act'},minGap:.4}],
  holds:[{id:'read',at:{cue:'complete'},end:{cue:'act'},channels:[
    {target:'panel',property:'x',min:0,max:0},{target:'panel',property:'opacity',min:1,max:1},
    {target:'camera',property:'zoom',min:1,max:1}]}]});
const plan=make(),compiled=compileChoreography(plan);
for (let f=0;f<=120;f++) compiled.sample(f/30);
const frame=compiled.sample(2.6);compiled.sample(4);compiled.sample(0);
assert.deepEqual(compiled.sample(2.6),frame);
plan.holds[0].channels[0].max=-1;assert.equal(compiled.sample(1.75).panel.x,0);
assert.equal(compiled.sample(2.75).panel.opacity,0);
const longer=make();longer.scene.cues.complete=1.8;
assert.throws(()=>compileChoreography(longer),/insufficient gap/,'long copy cannot silently eliminate reading interval');
longer.scene.cues.act={cue:'complete',offset:.5};
assert.equal(compileChoreography(longer).cues.act,2.3);
const drifting=make();drifting.scene.tracks.push({target:'camera',property:'zoom',at:1,end:2,from:1,to:2});
assert.throws(()=>compileChoreography(drifting).sample(1.6),/hold read/,'parent motion can violate read even with static panel');
const boundary=make();boundary.scene.tracks.push({target:'camera',property:'zoom',at:2,end:2.3,from:1,to:2});
assert.doesNotThrow(()=>compileChoreography(boundary).sample(2.1),'half-open hold permits later departure');
for(const mutate of [
  p=>p.relations[0].after={cue:'typo'},p=>p.relations[0].minGap=-1,
  p=>p.holds[0].channels[0].target='absent',p=>p.holds[0].channels[0].max=NaN,
  p=>p.holds[0].at=5,p=>p.holds[0].end=1,p=>p.holds[0].channels=[],
  p=>p.holds[0].channels[0].typo=1,p=>p.holds.push(p.holds[0]),
  p=>p.relations[0].before={cue:'ready',offset:Infinity},
]){const p=make();mutate(p);assert.throws(()=>compileChoreography(p));}
const timing={enter:0,ready:.6,exit:2,gone:2.15};
assert.equal(visibilityEnvelope(-1,timing),0);assert.equal(visibilityEnvelope(1,timing),1);
assert.equal(visibilityEnvelope(2.15,timing),0);
for(let f=0;f<300;f++){const v=visibilityEnvelope(f/100,timing);assert.ok(v>=0&&v<=1);}
assert.throws(()=>visibilityEnvelope(0,{...timing,gone:2}),/order/);
const press={at:1,duration:.2,depth:.06};
assert.equal(pressScale(0,press),1);assert.equal(pressScale(1.2,press),1);
assert.ok(Math.abs(pressScale(1.1,press)-.94)<1e-10);
assert.throws(()=>pressScale(0,{...press,depth:1}),/invalid/);
const a='a'.repeat(64),b='b'.repeat(64);
assert.equal(assertSelectedAssets([a],[b]),true);
assert.throws(()=>assertSelectedAssets([b],[b]),/rejected asset/);
assert.throws(()=>assertSelectedAssets(['filename.mp4'],[]),/SHA-256/);
console.log('PASS: readable cue gaps, camera-aware holds, independent exits, deterministic seek, press endpoints, rejected hashes and malformed plans');
