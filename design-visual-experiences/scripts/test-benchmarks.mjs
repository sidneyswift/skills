import assert from 'node:assert/strict';
import {filmState,filmTargets,stringDisplacement,stringGeometry,tideAt,tideRange} from '../assets/benchmark-lab/models.mjs';
let checks=0;
const near=(a,b,tol=1e-7)=>{assert.ok(Math.abs(a-b)<tol,`${a} != ${b}`);checks++};
// Seek order must not affect timeline state or glyph identity.
const saved=JSON.stringify(filmState(7.3));for(const t of [12,0,9,2])filmState(t);assert.equal(JSON.stringify(filmState(7.3)),saved);checks++;
assert.deepEqual(filmState(-1),filmState(0));assert.deepEqual(filmState(99),filmState(12));checks+=2;
assert.equal(new Set(filmTargets.map(p=>`${p.x},${p.y}`)).size,filmTargets.length);checks++;
for(const v of [-500,0,500]){near(stringDisplacement(0,45,v),45);near((stringDisplacement(1e-7,45,v)-45)/1e-7,v,.002)}
for(let i=0;i<7;i++){const g=stringGeometry(i,500);near(g.pluck,.5);near(stringGeometry(i,g.left+(g.right-g.left)*.3).pluck,.3)}
near(tideRange(0),2.92);near(tideRange(Math.PI/2),1.08);
// Compare analytic range to independent dense extrema across angular profiles.
for(const angle of [0,.3,1.2,Math.PI/2,3,5]){let lo=Infinity,hi=-Infinity;for(let j=0;j<10000;j++){const y=tideAt(j/10000*2*Math.PI,angle);lo=Math.min(lo,y);hi=Math.max(hi,y)}near(hi-lo,tideRange(angle),.00001);near(tideRange(angle,false),2);near(tideAt(.2,angle),tideAt(.2+Math.PI,angle));}
console.log(`PASS: ${checks} benchmark model checks (seek, release continuity, geometry, tide extrema)`);
