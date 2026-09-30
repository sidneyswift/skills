import assert from 'node:assert/strict';
import {seedFor,randomAt,logZoom,envelopeAt,sharedWind,solveLimb,footAt} from '../assets/experience-kernel.mjs';
const near=(a,b,e=1e-6)=>assert.ok(Math.abs(a-b)<e,`${a} != ${b}`);
const dist=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
const seed=seedFor('garden','plants'),melody=seedFor('garden','melody');
assert.notEqual(seed,melody);
for(let i=0;i<100;i++){const x=randomAt(seed,i);assert.ok(x>=0&&x<1);near(x,randomAt(seed,i));}
// Random access must not depend on evaluation order or another stream's work.
const baseline=[2,9,4].map(i=>randomAt(seed,i));for(let i=0;i<1000;i++)randomAt(melody,i);
assert.deepEqual(baseline,[2,9,4].map(i=>randomAt(seed,i)));
near(logZoom(2,32,.5),8);near(logZoom(2,32,.25)/2,logZoom(2,32,.5)/logZoom(2,32,.25));
assert.throws(()=>logZoom(0,4,.5),RangeError);
const events=[{time:1,strength:2},{time:2,strength:1}];near(envelopeAt(.9,events),0);near(envelopeAt(1.06,events),2);
near(envelopeAt(2.06,events),envelopeAt(2.06,events.slice(0,1))+envelopeAt(2.06,events.slice(1)));
for(const target of [{x:70,y:15},{x:0,y:0},{x:400,y:-40},{x:2,y:1}]){
 const root={x:0,y:0},r=solveLimb(root,target,55,40);
 near(dist(root,r.joint),55);near(dist(r.joint,r.end),40);
 assert.ok(Number.isFinite(r.end.x)&&Number.isFinite(r.joint.y));
}
const a=solveLimb({x:0,y:0},{x:70,y:0},50,50,1),b=solveLimb({x:0,y:0},{x:70,y:0},50,50,-1);
near(a.joint.x,b.joint.x);near(a.joint.y,-b.joint.y);
const gait={period:1.4,stride:110,stance:.62};
near(footAt(.1,gait).x,footAt(.7,gait).x);assert.equal(footAt(.1,gait).stance,true);
for(const t of [1.4,1.4*.62,2.8]){near(footAt(t-1e-7,gait).x,footAt(t+1e-7,gait).x,1e-3);near(footAt(t-1e-7,gait).y,footAt(t+1e-7,gait).y,1e-3);}
for(let t=0;t<5;t+=.01){const f=footAt(t,gait);assert.ok(f.y<=0);}
near(sharedWind(100,4),sharedWind(100,4));near(sharedWind(100,4,0),0);
console.log('PASS: seeded streams, random access, logarithmic zoom, event envelopes, limb lengths and reach clamps, planted contacts, gait continuity, shared wind.');
