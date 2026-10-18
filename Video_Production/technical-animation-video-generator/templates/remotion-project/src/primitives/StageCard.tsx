import React from 'react';
import { interpolate, spring, useVideoConfig } from 'remotion';
import { ArrowDown, ArrowRight, LucideIcon } from 'lucide-react';
import { THEME, SemanticColorKey, getAccentBg, getAccentHex } from '../theme/tokens';

/**
 * Static info cards. Use ONLY for bridge / outro / summary beats.
 * Real & tech beats must use Mechanism primitives (packets moving in processing order).
 */

export interface BeatBoxProps {
  icon: LucideIcon;
  label: string;
  sub?: string;
  color: SemanticColorKey;
  enterFrame?: number;
  f: number;
  fps: number;
  highlight?: boolean;
  strike?: boolean;
  wide?: boolean;
}

export const StageCard: React.FC<BeatBoxProps> = ({
  icon: Icon,
  label,
  sub,
  color,
  enterFrame = 0,
  f,
  fps,
  highlight = false,
  strike = false,
  wide = false,
}) => {
  const prog = spring({
    frame: Math.max(0, f - enterFrame),
    fps,
    config: { damping: 20, stiffness: 150 },
  });
  const visible = f >= enterFrame - 2 ? prog : 0;
  const hex = getAccentHex(color);
  const bg = getAccentBg(color);

  return (
    <div
      style={{
        flex: wide ? '1 1 100%' : 1,
        minWidth: wide ? '100%' : 240,
        padding: '28px 26px',
        borderRadius: 28,
        backgroundColor: highlight ? bg : 'rgba(10, 16, 30, 0.90)',
        border: `${highlight ? 3 : 2}px solid ${
          highlight ? hex : `${hex}66`
        }`,
        boxShadow: highlight
          ? `0 18px 42px ${hex}33, inset 0 0 24px ${hex}22`
          : '0 14px 32px rgba(0, 0, 0, 0.4)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 14,
        opacity: visible,
        transform: `translateY(${interpolate(visible, [0, 1], [24, 0])}px) scale(${interpolate(
          visible,
          [0, 1],
          [0.92, 1]
        )})`,
        position: 'relative',
      }}
    >
      <div
        style={{
          width: 84,
          height: 84,
          borderRadius: 24,
          backgroundColor: bg,
          border: `2px solid ${hex}88`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Icon size={44} color={hex} strokeWidth={2.2} />
      </div>

      <div
        style={{
          fontSize: 31,
          fontWeight: 800,
          color: THEME.colors.textPrimary,
          textAlign: 'center',
          lineHeight: 1.22,
          textDecoration: strike ? 'line-through' : 'none',
        }}
      >
        {label}
      </div>

      {sub && (
        <div
          style={{
            fontSize: 23,
            fontWeight: 700,
            color: hex,
            backgroundColor: 'rgba(7, 11, 20, 0.85)',
            padding: '6px 16px',
            borderRadius: 12,
            border: `1px solid ${hex}44`,
            textAlign: 'center',
            fontFamily: sub.includes('$') || sub.includes(':') || sub.includes('=')
              ? THEME.monoFont
              : THEME.fontFamily,
          }}
        >
          {sub}
        </div>
      )}
    </div>
  );
};

export const FlowArrow: React.FC<{
  label?: string;
  color?: SemanticColorKey;
  vertical?: boolean;
  f: number;
  enterFrame?: number;
}> = ({ label, color = 'cyan', vertical = false, f, enterFrame = 0 }) => {
  const { fps } = useVideoConfig();
  const prog = spring({
    frame: Math.max(0, f - enterFrame),
    fps,
    config: { damping: 20, stiffness: 160 },
  });
  const hex = getAccentHex(color);
  const Icon = vertical ? ArrowDown : ArrowRight;

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: vertical ? 'column' : 'row',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 8,
        opacity: f >= enterFrame ? prog : 0,
        margin: vertical ? '6px 0' : '0 6px',
      }}
    >
      {label && (
        <span
          style={{
            fontSize: 21,
            fontWeight: 700,
            color: hex,
            backgroundColor: 'rgba(7, 11, 20, 0.9)',
            padding: '4px 12px',
            borderRadius: 999,
            border: `1px solid ${hex}55`,
            whiteSpace: 'nowrap',
          }}
        >
          {label}
        </span>
      )}
      <Icon size={34} color={hex} strokeWidth={2.8} />
    </div>
  );
};
