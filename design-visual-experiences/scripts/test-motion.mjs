import assert from 'node:assert/strict';
import {springState,springStep,targetTrack,release,hermite,loopWave,paintTick} from '../assets/motion-kernel.mjs';
const near=(a,b,tol=1e-5)=>assert.ok(Math.abs(a-b)<tol,`${a} differs from ${b}`);
for(const damping of [.45,.83,1,1.4]){
  const initial=springState(0,2,-3,12,damping);near(initial.x,2);near(initial.v,-3);
  const h=1e-5,t=.12,mid=springState(t,2,-3,12,damping);
  near((springState(t+h,2,-3,12,damping).x-springState(t-h,2,-3,12,damping).x)/(2*h),mid.v,1e-4);
  near(springState(10,2,-3,12,damping).x,0);
  near(springStep(0,12,damping),0);near(springStep(10,12,damping),1);
}
const events=[{time:1,value:100},{time:1.12,value:-40},{time:2,value:60}];
// Rapid retargeting must preserve both position and velocity at the handoff.
const h=1e-5,t=1.12;
near(targetTrack(t,0,events),targetTrack(t,0,events.slice(0,1)));
const before=(targetTrack(t,0,events)-targetTrack(t-h,0,events))/h;
const after=(targetTrack(t+h,0,events)-targetTrack(t,0,events))/h;
near(before,after,.3);
const times=[3,.1,1.12,2.6,1,3],actual=times.map(t=>targetTrack(t,0,events));
near(actual[0],actual[5]);
near(release(0,70,400),70);near((release(h,70,400)-release(0,70,400))/h,400,.2);
near(hermite(0,0,2,10,90,20,-5),10);near(hermite(2,0,2,10,90,20,-5),90);
near((hermite(h,0,2,10,90,20,-5)-10)/h,20,.01);
near((90-hermite(2-h,0,2,10,90,20,-5))/h,-5,.01);
near(loopWave(0,4),loopWave(4,4));
near((loopWave(h,4)-loopWave(-h,4))/(2*h),(loopWave(4+h,4)-loopWave(4-h,4))/(2*h));
assert.equal(paintTick(.01),paintTick(.07));assert.notEqual(paintTick(.07),paintTick(.09));
console.log('Passed: spring regimes, derivative agreement, retarget continuity, seek order, release velocity, Hermite handoff, loop value/velocity, paint clock.');
