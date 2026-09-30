import {clamp,smooth,hash,release} from '../motion-kernel.mjs';
export {clamp,smooth,hash};
export function filmState(time){const t=clamp(time,0,12);return {t,gather:smooth((t-1)/2.4),stack:smooth((t-4)/2),reveal:smooth((t-7)/1.4),close:smooth((t-9.4)/1),chapter:t<4?0:t<7?1:2};}
export function stringDisplacement(age,amount,velocity=0){return release(Math.max(0,age),amount,velocity,0,22,.065);}
// Illustrative angular cross-section, not a tide forecast or a full equilibrium solver.
export function tideAt(theta,moonAngle,solar=true){return Math.cos(2*(theta-moonAngle))+(solar?.46*Math.cos(2*theta):0);}
export function tideRange(moonAngle,solar=true){return 2*Math.hypot(Math.cos(2*moonAngle)+(solar?.46:0),Math.sin(2*moonAngle));}
export function nearestString(y){return Math.round(clamp((y-157)/51,0,6));}

export function stringGeometry(index,x){const left=100+index*7,right=900-index*7;return {left,right,pluck:clamp((x-left)/(right-left),.1,.9)};}
// Original compact glyphs; each mark retains its identity through the film.
const glyphs={M:['10001','11011','10101','10101','10001','10001','10001'],A:['01110','10001','10001','11111','10001','10001','10001'],K:['10001','10010','10100','11000','10100','10010','10001'],E:['11111','10000','10000','11110','10000','10000','11111'],R:['11110','10001','10001','11110','10100','10010','10001'],O:['01110','10001','10001','10001','10001','10001','01110']};
export const filmTargets=['MAKE','ROOM'].flatMap((word,row)=>[...word].flatMap((letter,col)=>glyphs[letter].flatMap((line,y)=>[...line].flatMap((cell,x)=>cell==='1'?[{x:247+(col*6+x)*22,y:155+row*195+y*22}]:[]))));
