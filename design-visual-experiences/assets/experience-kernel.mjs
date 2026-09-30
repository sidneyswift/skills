// Original, dependency-free reference helpers. Coordinates and time units are caller-owned.
export const clamp01 = x => Math.max(0, Math.min(1, x));
export function seedFor(text, stream = '') {
  let h = 2166136261;
  for (const c of `${text.length}:${text}|${stream}`) { h ^= c.codePointAt(0); h = Math.imul(h, 16777619); }
  return h >>> 0;
}
export function randomAt(seed, index) {
  let n = (seed ^ Math.imul(index + 1, 0x9e3779b9)) >>> 0;
  n ^= n >>> 16; n = Math.imul(n, 0x7feb352d); n ^= n >>> 15;
  n = Math.imul(n, 0x846ca68b); n ^= n >>> 16;
  return (n >>> 0) / 4294967296;
}
export function logZoom(start, end, u) {
  if (!(start > 0 && end > 0)) throw new RangeError('Zoom scales must be positive');
  return Math.exp(Math.log(start) + (Math.log(end)-Math.log(start))*clamp01(u));
}
export function envelopeAt(t, events, attack=.06, decay=.5) {
  if (!(attack > 0 && decay > 0)) throw new RangeError('Envelope times must be positive');
  let sum=0;
  for (const e of events) {
    const age=t-e.time;
    if (age<0) continue;
    sum+=(e.strength ?? 1)*(age<attack ? age/attack : Math.exp(-(age-attack)/decay));
  }
  return sum;
}
export function sharedWind(x,t,strength=1) {
  return strength*(.55*Math.sin(t*.8-x*.003)+.28*Math.sin(t*1.71-x*.005)+.17*Math.sin(t*.23));
}
export function solveLimb(root,target,upper,lower,bend=1) {
  if (!(upper>0 && lower>0)) throw new RangeError('Limb lengths must be positive');
  const dx=target.x-root.x,dy=target.y-root.y,raw=Math.hypot(dx,dy);
  const ux=raw>1e-10 ? dx/raw : 0, uy=raw>1e-10 ? dy/raw : 1;
  const d=Math.max(Math.abs(upper-lower)+1e-8,Math.min(upper+lower-1e-8,raw));
  const along=(upper*upper+d*d-lower*lower)/(2*d);
  const height=Math.sqrt(Math.max(0,upper*upper-along*along));
  const s=bend<0 ? -1 : 1;
  return {joint:{x:root.x+ux*along-uy*height*s,y:root.y+uy*along+ux*height*s},end:{x:root.x+ux*d,y:root.y+uy*d},clamped:Math.abs(d-raw)>1e-7};
}
// Absolute-time foot placement for straight travel. Stance contact is fixed in world space.
export function footAt(t,{period=1.4,stride=110,stance=.62,lift=32,offset=0}={}) {
  if (!(period>0 && stride>=0 && stance>0 && stance<1)) throw new RangeError('Invalid gait parameters');
  const q=t/period+offset, cycle=Math.floor(q),phase=q-cycle;
  if (phase<stance) return {x:(cycle+stance/2-offset)*stride,y:0,stance:true};
  const u=(phase-stance)/(1-stance),smooth=u*u*(3-2*u);
  return {x:(cycle+stance/2-offset+smooth)*stride,y:-lift*Math.sin(Math.PI*u)**2,stance:false};
}
