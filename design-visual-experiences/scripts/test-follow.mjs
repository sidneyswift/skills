import assert from 'node:assert/strict';
import {followHalfLife} from '../assets/motion-kernel.mjs';
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);
const at=(parts)=>parts.reduce((x,dt)=>followHalfLife(x,100,dt,.08),0);
const expected=100*(1-2**(-.5/.08));
for(const hz of [30,60,120])near(at(Array(hz/2).fill(1/hz)),expected);
near(at([.017,.063,.11,.21,.1]),expected);
near(followHalfLife(0,100,.08,.08),50);
near(followHalfLife(45,-20,0,.08),45);
near(followHalfLife(0,100,100,.08),100);
for(const a of [.12,.19]){const half=-Math.LN2/(60*Math.log1p(-a));near(followHalfLife(0,100,1/60,half),100*a);}
for(const args of [[0,1,-1,.08],[0,1,1,0],[NaN,1,1,.08],[0,1,Infinity,.08]])assert.throws(()=>followHalfLife(...args),RangeError);
console.log('PASS: refresh-rate equivalence, irregular intervals, half-life, retarget position, conversion and invalid inputs');
