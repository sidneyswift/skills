// Original reusable mechanics. Seconds, pixels, and radians throughout.
export const clamp = (x, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, x));
export const mix = (a, b, u) => a + (b - a) * u;
export const phase = (t, start, duration) => clamp((t - start) / duration);
export const smooth = x => { const u = clamp(x); return u * u * (3 - 2 * u); };

// Exact homogeneous damped oscillator, including velocity at handoff.
// x is displacement from equilibrium; omega is natural angular frequency.
export function springState(t, x = 1, v = 0, omega = 12, damping = 0.8) {
  if (t <= 0) return {x, v};
  if (!(omega > 0 && damping >= 0)) throw new RangeError('Invalid spring parameters');
  const a = damping * omega;
  if (Math.abs(damping - 1) < 1e-7) {
    const b = v + omega * x, e = Math.exp(-omega * t);
    return {x: e * (x + b * t), v: e * (b - omega * (x + b * t))};
  }
  if (damping < 1) {
    const w = omega * Math.sqrt(1 - damping * damping);
    const b = (v + a * x) / w, c = Math.cos(w * t), s = Math.sin(w * t), e = Math.exp(-a * t);
    return {x: e * (x * c + b * s), v: e * ((b * w - a * x) * c + (-x * w - a * b) * s)};
  }
  const q = omega * Math.sqrt(damping * damping - 1), r1 = -a + q, r2 = -a - q;
  const A = (v - r2 * x) / (r1 - r2), B = x - A;
  return {x: A * Math.exp(r1 * t) + B * Math.exp(r2 * t), v: A * r1 * Math.exp(r1 * t) + B * r2 * Math.exp(r2 * t)};
}

export function springStep(t, omega = 12, damping = 0.8) {
  return t < 0 ? 0 : 1 - springState(t, 1, 0, omega, damping).x;
}

// Superposition of target changes: no frame-to-frame accumulated state.
// Events must be time-ordered. All use the same spring to preserve velocity.
export function targetTrack(t, initial, events, omega = 12, damping = 0.8) {
  let value = initial, previousTarget = initial;
  for (const event of events) {
    if (event.time > t) break;
    value += (event.value - previousTarget) * springStep(t - event.time, omega, damping);
    previousTarget = event.value;
  }
  return value;
}

export function release(t, from, velocity, target = 0, omega = 12, damping = 0.8) {
  return target + springState(Math.max(0,t), from - target, velocity, omega, damping).x;
}

// Smooth change of motion regime with specified endpoint velocities.
export function hermite(t, t0, t1, p0, p1, v0 = 0, v1 = 0) {
  const d = t1 - t0;
  if (!(d > 0)) throw new RangeError('Hermite interval must be positive');
  const u = phase(t, t0, d), u2 = u*u, u3 = u2*u;
  return (2*u3-3*u2+1)*p0 + (u3-2*u2+u)*d*v0 + (-2*u3+3*u2)*p1 + (u3-u2)*d*v1;
}

// Stable identity noise: never seed this with the render frame.
export function hash(seed) {
  let x = (seed | 0) ^ 0x9e3779b9;
  x = Math.imul(x ^ (x >>> 16), 0x21f0aaad);
  x = Math.imul(x ^ (x >>> 15), 0x735a2d97);
  return ((x ^ (x >>> 15)) >>> 0) / 4294967296;
}

export function loopWave(t, period, seed = 1) {
  const angle = 2 * Math.PI * t / period;
  return Math.sin(angle + hash(seed)*2*Math.PI)*0.72 + Math.sin(angle*2 + hash(seed+1)*2*Math.PI)*0.28;
}

// Paint refresh may be stepped while the subject/camera clock remains smooth.
export const paintTick = (t, rate = 12) => Math.floor(t * rate);

// Orthographic camera mapping: screen = anchor + zoom * (world - focus).
export const cameraPoint = (point, focus, zoom, anchor) => ({x:anchor.x+zoom*(point.x-focus.x), y:anchor.y+zoom*(point.y-focus.y)});

// Exact first-order response to a target held constant over dt (seconds).
// Retargets preserve position, not velocity. Use a spring for momentum.
export function followHalfLife(value, target, dt, halfLife) {
  if (![value,target,dt,halfLife].every(Number.isFinite) || dt < 0 || halfLife <= 0) {
    throw new RangeError('Expected finite values, nonnegative dt and positive halfLife');
  }
  return value + (target-value) * -Math.expm1(-Math.LN2 * dt / halfLife);
}
