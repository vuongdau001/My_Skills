/**
 * Mechanism primitives — "Mô phỏng, không trình chiếu".
 * Everything is positioned on a fixed design canvas (MechStage) so packets can travel
 * between nodes in the real processing order. All timing is in frames inside the beat.
 */
import React from 'react';
import { Easing, interpolate, spring, useVideoConfig } from 'remotion';
import { CircleCheck, CircleX, LucideIcon } from 'lucide-react';
import { THEME, SemanticColorKey, getAccentBg, getAccentHex } from '../theme/tokens';

export type XY = [number, number];

export const CANVAS_W = 912;
export const CANVAS_H = 880;

/** 0→1 spring that starts at `at`. Returns 0 before `at`. */
export function usePop(f: number, at: number): number {
  const { fps } = useVideoConfig();
  if (f < at) return 0;
  return spring({ frame: f - at, fps, config: { damping: 18, stiffness: 170 } });
}

/** Eased 0→1 between frames a and b (clamped). */
export function ease(f: number, a: number, b: number): number {
  return interpolate(f, [a, Math.max(b, a + 1)], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.inOut(Easing.cubic),
  });
}

/** Visible window helper: fades in at `from`, fades out at `until` (if given). */
export function windowOpacity(f: number, from: number, until?: number): number {
  const inO = interpolate(f, [from, from + 6], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  if (until === undefined) return inO;
  const outO = interpolate(f, [until, until + 6], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return Math.min(inO, outO);
}

export const MechStage: React.FC<{ children: React.ReactNode; height?: number }> = ({
  children,
  height = CANVAS_H,
}) => (
  <div style={{ position: 'relative', width: CANVAS_W, height, margin: '0 auto' }}>{children}</div>
);

/** Actor / system component: icon tile + label, centered on (x, y). */
export const MNode: React.FC<{
  f: number;
  at: number;
  x: number;
  y: number;
  icon: LucideIcon;
  label: string;
  color: SemanticColorKey;
  active?: boolean;
  size?: number;
}> = ({ f, at, x, y, icon: Icon, label, color, active = false, size = 132 }) => {
  const p = usePop(f, at);
  const hex = getAccentHex(color);
  return (
    <div
      style={{
        position: 'absolute',
        left: x - 150,
        top: y - size / 2,
        width: 300,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 12,
        opacity: p,
        transform: `scale(${interpolate(p, [0, 1], [0.8, 1])})`,
      }}
    >
      <div
        style={{
          width: size,
          height: size,
          borderRadius: 32,
          backgroundColor: active ? getAccentBg(color) : 'rgba(10,16,30,0.92)',
          border: `${active ? 4 : 2.5}px solid ${active ? hex : `${hex}88`}`,
          boxShadow: active ? `0 0 40px ${hex}66` : '0 14px 30px rgba(0,0,0,0.45)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Icon size={size * 0.48} color={hex} strokeWidth={2.1} />
      </div>
      <div style={{ fontSize: 32, fontWeight: 800, color: THEME.colors.textPrimary, textAlign: 'center' }}>
        {label}
      </div>
    </div>
  );
};

/** Connection line that draws itself from `from` to `to`. */
export const MLink: React.FC<{
  f: number;
  at: number;
  from: XY;
  to: XY;
  color: SemanticColorKey;
  dashed?: boolean;
  glowFrom?: number;
  glowUntil?: number;
  width?: number;
}> = ({ f, at, from, to, color, dashed = true, glowFrom, glowUntil, width = 4 }) => {
  const draw = ease(f, at, at + 14);
  const glowing = glowFrom !== undefined && f >= glowFrom && (glowUntil === undefined || f < glowUntil);
  const hex = getAccentHex(color);
  const x2 = from[0] + (to[0] - from[0]) * draw;
  const y2 = from[1] + (to[1] - from[1]) * draw;
  return (
    <svg style={{ position: 'absolute', inset: 0, overflow: 'visible' }} width={CANVAS_W} height={CANVAS_H}>
      <line
        x1={from[0]}
        y1={from[1]}
        x2={x2}
        y2={y2}
        stroke={hex}
        strokeOpacity={glowing ? 1 : 0.45}
        strokeWidth={glowing ? width + 3 : width}
        strokeDasharray={dashed ? '14 12' : undefined}
        strokeDashoffset={dashed ? -f * 1.5 : undefined}
        strokeLinecap="round"
        style={{ filter: glowing ? `drop-shadow(0 0 10px ${hex})` : undefined }}
      />
    </svg>
  );
};

/** A request/response/data chip that travels from `from` to `to` between frames start→end, then fades. */
export const MPacket: React.FC<{
  f: number;
  start: number;
  end: number;
  from: XY;
  to: XY;
  label: string;
  color: SemanticColorKey;
  hold?: number;
  mono?: boolean;
  icon?: LucideIcon;
}> = ({ f, start, end, from, to, label, color, hold = 8, mono = true, icon: Icon }) => {
  if (f < start - 2 || f > end + hold + 6) return null;
  const t = ease(f, start, end);
  const x = from[0] + (to[0] - from[0]) * t;
  const y = from[1] + (to[1] - from[1]) * t;
  const opacity = Math.min(
    interpolate(f, [start - 2, start + 4], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }),
    interpolate(f, [end + hold, end + hold + 6], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })
  );
  const hex = getAccentHex(color);
  return (
    <div
      style={{
        position: 'absolute',
        left: x,
        top: y,
        transform: 'translate(-50%, -50%)',
        opacity,
        display: 'flex',
        alignItems: 'center',
        gap: 10,
        padding: '10px 18px',
        borderRadius: 14,
        backgroundColor: 'rgba(7,11,20,0.96)',
        border: `2.5px solid ${hex}`,
        boxShadow: `0 0 26px ${hex}77`,
        fontSize: 26,
        fontWeight: 800,
        color: hex,
        whiteSpace: 'nowrap',
        fontFamily: mono ? THEME.monoFont : THEME.fontFamily,
        zIndex: 5,
      }}
    >
      {Icon && <Icon size={26} color={hex} strokeWidth={2.4} />}
      {label}
    </div>
  );
};

/** Persistent chip pinned to a position (e.g. a cookie stored in the browser). */
export const MChip: React.FC<{
  f: number;
  at: number;
  until?: number;
  x: number;
  y: number;
  label: string;
  color: SemanticColorKey;
  icon?: LucideIcon;
  mono?: boolean;
  struck?: boolean;
}> = ({ f, at, until, x, y, label, color, icon: Icon, mono = false, struck = false }) => {
  const p = usePop(f, at);
  const o = Math.min(p, windowOpacity(f, at, until));
  if (o <= 0) return null;
  const hex = getAccentHex(color);
  return (
    <div
      style={{
        position: 'absolute',
        left: x,
        top: y,
        transform: `translate(-50%, -50%) scale(${interpolate(p, [0, 1], [0.85, 1])})`,
        opacity: o,
        display: 'flex',
        alignItems: 'center',
        gap: 10,
        padding: '10px 18px',
        borderRadius: 14,
        backgroundColor: getAccentBg(color),
        border: `2px solid ${hex}aa`,
        fontSize: 27,
        fontWeight: 800,
        color: hex,
        whiteSpace: 'nowrap',
        textDecoration: struck ? 'line-through' : 'none',
        fontFamily: mono ? THEME.monoFont : THEME.fontFamily,
      }}
    >
      {Icon && <Icon size={26} color={hex} strokeWidth={2.4} />}
      {label}
    </div>
  );
};

export interface StoreRow {
  text: string;
  at: number;
  strikeAt?: number;
}

/** Ledger / database card whose rows get written and struck through over time. */
export const MStore: React.FC<{
  f: number;
  at: number;
  x: number;
  y: number;
  icon: LucideIcon;
  title: string;
  color: SemanticColorKey;
  rows: StoreRow[];
  width?: number;
  active?: boolean;
}> = ({ f, at, x, y, icon: Icon, title, color, rows, width = 380, active = false }) => {
  const p = usePop(f, at);
  const hex = getAccentHex(color);
  return (
    <div
      style={{
        position: 'absolute',
        left: x - width / 2,
        top: y,
        width,
        opacity: p,
        transform: `translateY(${interpolate(p, [0, 1], [20, 0])}px)`,
        borderRadius: 26,
        backgroundColor: 'rgba(10,16,30,0.94)',
        border: `${active ? 4 : 2.5}px solid ${active ? hex : `${hex}88`}`,
        boxShadow: active ? `0 0 40px ${hex}55` : '0 14px 30px rgba(0,0,0,0.45)',
        padding: '20px 22px',
        display: 'flex',
        flexDirection: 'column',
        gap: 14,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
        <Icon size={34} color={hex} strokeWidth={2.2} />
        <span style={{ fontSize: 30, fontWeight: 800, color: THEME.colors.textPrimary }}>{title}</span>
      </div>
      {rows.map((r, i) => {
        const rp = fadeIn(f, r.at);
        const struck = r.strikeAt !== undefined && f >= r.strikeAt;
        const strikeW = r.strikeAt !== undefined ? ease(f, r.strikeAt, r.strikeAt + 10) * 100 : 0;
        return (
          <div
            key={i}
            style={{
              position: 'relative',
              opacity: rp * (struck ? 0.55 : 1),
              padding: '10px 14px',
              borderRadius: 12,
              backgroundColor: struck ? THEME.colors.coralBg : 'rgba(148,163,184,0.08)',
              fontFamily: THEME.monoFont,
              fontSize: 26,
              fontWeight: 700,
              color: struck ? THEME.colors.coral : THEME.colors.textSecondary,
            }}
          >
            {r.text}
            <div
              style={{
                position: 'absolute',
                left: 10,
                top: '50%',
                height: 4,
                width: `calc(${strikeW}% - 20px)`,
                backgroundColor: THEME.colors.coral,
                borderRadius: 2,
              }}
            />
          </div>
        );
      })}
    </div>
  );
};

// Plain (non-hook) fade so it is safe to call inside rows.map.
function fadeIn(f: number, at: number): number {
  if (f < at) return 0;
  return interpolate(f, [at, at + 8], [0, 1], { extrapolateRight: 'clamp' });
}

/** ✔ / ✖ verdict with short label, visible in [at, until). */
export const MVerdict: React.FC<{
  f: number;
  at: number;
  until?: number;
  x: number;
  y: number;
  ok: boolean;
  label: string;
}> = ({ f, at, until, x, y, ok, label }) => {
  const p = usePop(f, at);
  const o = Math.min(p, windowOpacity(f, at, until));
  if (o <= 0) return null;
  const hex = ok ? THEME.colors.green : THEME.colors.coral;
  const Icon = ok ? CircleCheck : CircleX;
  return (
    <div
      style={{
        position: 'absolute',
        left: x,
        top: y,
        transform: `translate(-50%, -50%) scale(${interpolate(p, [0, 1], [0.6, 1])})`,
        opacity: o,
        display: 'flex',
        alignItems: 'center',
        gap: 12,
        padding: '12px 22px',
        borderRadius: 999,
        backgroundColor: ok ? THEME.colors.greenBg : THEME.colors.coralBg,
        border: `3px solid ${hex}`,
        boxShadow: `0 0 30px ${hex}66`,
        fontSize: 30,
        fontWeight: 800,
        color: hex,
        whiteSpace: 'nowrap',
        zIndex: 6,
      }}
    >
      <Icon size={34} color={hex} strokeWidth={2.6} />
      {label}
    </div>
  );
};
