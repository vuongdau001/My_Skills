import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {
  Landmark,
  Cpu,
  ArrowRight,
  Sparkles,
  Play,
  Layers,
} from 'lucide-react';
import {
  THEME,
  SemanticColorKey,
  getAccentBg,
  getAccentHex,
} from '../theme/tokens';
import {
  BeatManifest,
  ChapterManifest,
  CueManifest,
  splitPairs,
} from '../types';

interface SceneFrameProps {
  part: number;
  totalParts: number;
  chapters: ChapterManifest[];
  beat: BeatManifest;
  beatFrame: number;
  activeCue: CueManifest | null;
  activeCueIndex: number;
  cueFrame: number;
  children: React.ReactNode;
}

const MODE_META: Record<
  BeatManifest['mode'],
  { label: string; color: SemanticColorKey; bgTint: string }
> = {
  real: {
    label: 'VÍ DỤ THỰC TẾ',
    color: 'amber',
    bgTint: 'rgba(251, 191, 36, 0.07)',
  },
  tech: {
    label: 'CƠ CHẾ KỸ THUẬT',
    color: 'cyan',
    bgTint: 'rgba(56, 189, 248, 0.08)',
  },
  bridge: {
    label: 'ĐẶT VẤN ĐỀ TIẾP THEO',
    color: 'violet',
    bgTint: 'rgba(167, 139, 250, 0.10)',
  },
  outro: {
    label: 'ĐÓN XEM TIẾP',
    color: 'green',
    bgTint: 'rgba(52, 211, 153, 0.09)',
  },
  summary: {
    label: 'TỔNG KẾT HỆ THỐNG',
    color: 'green',
    bgTint: 'rgba(52, 211, 153, 0.08)',
  },
};

function renderHighlightedCue(
  sub: string,
  highlights: string[],
  accentColor: SemanticColorKey
): React.ReactNode {
  if (!highlights || highlights.length === 0) {
    return sub;
  }

  type Seg = { text: string; highlighted?: boolean };
  let segments: Seg[] = [{ text: sub }];

  for (const term of highlights) {
    if (!term) continue;
    const next: Seg[] = [];
    for (const seg of segments) {
      if (seg.highlighted) {
        next.push(seg);
        continue;
      }
      const idx = seg.text.indexOf(term);
      if (idx === -1) {
        next.push(seg);
      } else {
        if (idx > 0) next.push({ text: seg.text.slice(0, idx) });
        next.push({ text: term, highlighted: true });
        const rest = seg.text.slice(idx + term.length);
        if (rest.length > 0) next.push({ text: rest });
      }
    }
    segments = next;
  }

  const hex = getAccentHex(accentColor);
  const bg = getAccentBg(accentColor);

  return segments.map((s, i) =>
    s.highlighted ? (
      <span
        key={i}
        style={{
          color: hex,
          backgroundColor: bg,
          padding: '2px 10px',
          borderRadius: 10,
          fontWeight: 800,
          border: `1px solid ${hex}55`,
          margin: '0 3px',
          display: 'inline-block',
          whiteSpace: s.text.length <= 24 ? 'nowrap' : 'normal',
        }}
      >
        {s.text}
      </span>
    ) : (
      <span key={i}>{s.text}</span>
    )
  );
}

export const SceneFrame: React.FC<SceneFrameProps> = ({
  part,
  totalParts,
  chapters,
  beat,
  beatFrame,
  activeCue,
  activeCueIndex,
  cueFrame,
  children,
}) => {
  const { fps } = useVideoConfig();
  const globalFrame = useCurrentFrame();

  const meta = MODE_META[beat.mode];
  const accentHex = getAccentHex(meta.color);
  const accentBg = getAccentBg(meta.color);

  // Smooth entry & exit envelope for every beat so transitions never feel abrupt
  const enterSpring = spring({
    frame: beatFrame,
    fps,
    config: { damping: 22, stiffness: 150, mass: 0.85 },
  });
  const exitOpacity = interpolate(
    beatFrame,
    [beat.durationInFrames - 10, beat.durationInFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );
  const stageOpacity = Math.min(enterSpring, exitOpacity);
  const stageTranslateY = interpolate(enterSpring, [0, 1], [24, 0]);
  const stageScale = interpolate(enterSpring, [0, 1], [0.975, 1]);

  // Cue transition animation inside the Vietsub box
  const cueEnter = spring({
    frame: Math.max(0, cueFrame),
    fps,
    config: { damping: 24, stiffness: 220 },
  });
  const cueProgress = activeCue
    ? interpolate(cueFrame, [0, activeCue.durationInFrames], [0, 100], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      })
    : 0;

  const activeChapterIdx = Math.max(
    0,
    chapters.findIndex((c) => c.id === beat.sceneId)
  );

  const pairs = splitPairs(beat.mapBar);
  const mapBarEnter = spring({
    frame: Math.max(0, beatFrame - 8),
    fps,
    config: { damping: 20, stiffness: 140 },
  });

  const ModeIcon =
    beat.mode === 'real'
      ? Landmark
      : beat.mode === 'tech'
      ? Cpu
      : beat.mode === 'bridge'
      ? Sparkles
      : beat.mode === 'outro'
      ? Play
      : Layers;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: THEME.colors.bgDeep,
        fontFamily: THEME.fontFamily,
        color: THEME.colors.textPrimary,
        overflow: 'hidden',
      }}
    >
      {/* Ambient Radial Glow that shifts color smoothly between Real (Amber) & Tech (Cyan) */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `
            radial-gradient(circle at 50% 24%, ${meta.bgTint} 0%, transparent 62%),
            radial-gradient(circle at 85% 78%, rgba(56, 189, 248, 0.05) 0%, transparent 55%),
            linear-gradient(180deg, #070B14 0%, #0B1222 55%, #070B14 100%)
          `,
        }}
      />

      {/* Subtle architectural grid */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage: `
            linear-gradient(to right, rgba(148, 163, 184, 0.04) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(148, 163, 184, 0.04) 1px, transparent 1px)
          `,
          backgroundSize: '72px 72px',
          opacity: 0.7,
        }}
      />

      {/* TOP HEADER: Part Pill + Chapter Progress Segments + Mode Badge + Title */}
      <div
        style={{
          position: 'absolute',
          top: 64,
          left: 48,
          right: 48,
          display: 'flex',
          flexDirection: 'column',
          gap: 18,
          zIndex: 10,
        }}
      >
        {/* Chapter progress bar + Episode badge */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 16,
          }}
        >
          <div
            style={{
              padding: '6px 14px',
              borderRadius: 999,
              backgroundColor: 'rgba(15, 23, 42, 0.85)',
              border: `1px solid ${THEME.colors.borderSubtle}`,
              fontSize: 20,
              fontWeight: 700,
              color: THEME.colors.textSecondary,
              letterSpacing: 0.6,
              whiteSpace: 'nowrap',
            }}
          >
            TẬP {part}/{totalParts}
          </div>

          <div
            style={{
              display: 'flex',
              flex: 1,
              gap: 10,
              alignItems: 'center',
            }}
          >
            {chapters.map((ch, idx) => {
              const isDone = idx < activeChapterIdx;
              const isCurrent = idx === activeChapterIdx;
              return (
                <div
                  key={ch.id}
                  style={{
                    flex: 1,
                    height: 8,
                    borderRadius: 999,
                    backgroundColor: isDone
                      ? THEME.colors.cyan
                      : isCurrent
                      ? accentHex
                      : 'rgba(148, 163, 184, 0.18)',
                    boxShadow: isCurrent ? `0 0 14px ${accentHex}88` : 'none',
                  }}
                />
              );
            })}
          </div>
        </div>

        {/* Mode Badge + Scene Title */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            backgroundColor: 'rgba(15, 23, 42, 0.88)',
            border: `1.5px solid ${accentHex}44`,
            borderRadius: 24,
            padding: '18px 26px',
            boxShadow: '0 14px 34px rgba(0, 0, 0, 0.38)',
          }}
        >
          <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
            <div
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: 10,
                alignSelf: 'flex-start',
                padding: '5px 14px',
                borderRadius: 999,
                backgroundColor: accentBg,
                border: `1px solid ${accentHex}66`,
              }}
            >
              <ModeIcon size={20} color={accentHex} strokeWidth={2.4} />
              <span
                style={{
                  fontSize: 20,
                  fontWeight: 800,
                  color: accentHex,
                  letterSpacing: 0.8,
                }}
              >
                {meta.label}
              </span>
            </div>

            <div
              style={{
                fontSize: 40,
                fontWeight: 800,
                color: THEME.colors.textPrimary,
                letterSpacing: -0.5,
                lineHeight: 1.15,
              }}
            >
              {beat.sceneTitle}
            </div>
          </div>

          {/* Right indicator showing Real -> Tech two-step flow within each chapter */}
          {(beat.mode === 'real' || beat.mode === 'tech') && (
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 10,
                padding: '10px 16px',
                borderRadius: 16,
                backgroundColor: 'rgba(7, 11, 20, 0.75)',
                border: `1px solid ${THEME.colors.borderSubtle}`,
              }}
            >
              <span
                style={{
                  fontSize: 20,
                  fontWeight: 800,
                  color:
                    beat.mode === 'real'
                      ? THEME.colors.amber
                      : THEME.colors.textMuted,
                  opacity: beat.mode === 'real' ? 1 : 0.55,
                }}
              >
                1. Thực tế
              </span>
              <ArrowRight size={18} color={THEME.colors.textMuted} />
              <span
                style={{
                  fontSize: 20,
                  fontWeight: 800,
                  color:
                    beat.mode === 'tech'
                      ? THEME.colors.cyan
                      : THEME.colors.textMuted,
                  opacity: beat.mode === 'tech' ? 1 : 0.55,
                }}
              >
                2. Kỹ thuật
              </span>
            </div>
          )}
        </div>
      </div>

      {/* MAIN VISUAL STAGE (Spacious, low-text, smooth enter/exit) */}
      <div
        style={{
          position: 'absolute',
          top: 268,
          left: 48,
          right: 48,
          bottom: 450,
          borderRadius: 34,
          backgroundColor:
            beat.mode === 'real'
              ? 'rgba(15, 25, 42, 0.78)'
              : beat.mode === 'tech'
              ? 'rgba(13, 20, 38, 0.82)'
              : 'rgba(17, 24, 44, 0.72)',
          border: `2px solid ${accentHex}38`,
          boxShadow: `0 24px 60px rgba(0, 0, 0, 0.48), inset 0 0 48px ${accentHex}0D`,
          padding: 36,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          opacity: stageOpacity,
          transform: `translateY(${stageTranslateY}px) scale(${stageScale})`,
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            position: 'relative',
          }}
        >
          {children}
        </div>

        {/* 1-Line Mapping Bar: ONLY rendered in 'tech' mode to bridge Real -> Tech */}
        {beat.mode === 'tech' && pairs.length > 0 && (
          <div
            style={{
              marginTop: 20,
              padding: '18px 24px',
              borderRadius: 22,
              backgroundColor: 'rgba(7, 11, 20, 0.92)',
              border: `1.5px solid ${THEME.colors.violet}55`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 24,
              flexWrap: 'wrap',
              opacity: mapBarEnter,
              transform: `translateY(${interpolate(mapBarEnter, [0, 1], [18, 0])}px)`,
            }}
          >
            {pairs.map(([realTerm, techTerm], idx) => (
              <div
                key={idx}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 12,
                  fontSize: 25,
                  fontWeight: 700,
                }}
              >
                <span
                  style={{
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: 8,
                    color: THEME.colors.amber,
                    backgroundColor: THEME.colors.amberBg,
                    padding: '6px 14px',
                    borderRadius: 12,
                    border: `1px solid ${THEME.colors.amber}44`,
                  }}
                >
                  <Landmark size={20} color={THEME.colors.amber} />
                  {realTerm}
                </span>
                <ArrowRight
                  size={24}
                  color={THEME.colors.violet}
                  strokeWidth={2.6}
                />
                <span
                  style={{
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: 8,
                    color: THEME.colors.cyan,
                    backgroundColor: THEME.colors.cyanBg,
                    padding: '6px 14px',
                    borderRadius: 12,
                    border: `1px solid ${THEME.colors.cyan}44`,
                  }}
                >
                  <Cpu size={20} color={THEME.colors.cyan} />
                  {techTerm}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* BOTTOM VIETSUB CARD: 1-2 lines max, exact cue sync, high contrast */}
      <div
        style={{
          position: 'absolute',
          left: 48,
          right: 48,
          bottom: 180,
          height: 236,
          borderRadius: 28,
          backgroundColor: 'rgba(8, 13, 24, 0.95)',
          border: `2px solid ${accentHex}55`,
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.65)',
          padding: '26px 34px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          overflow: 'hidden',
        }}
      >
        {/* Cue step dots in top-right of subtitle box */}
        {beat.cues.length > 1 && (
          <div
            style={{
              position: 'absolute',
              top: 16,
              right: 24,
              display: 'flex',
              gap: 8,
            }}
          >
            {beat.cues.map((_, idx) => (
              <div
                key={idx}
                style={{
                  width: idx === activeCueIndex ? 26 : 9,
                  height: 9,
                  borderRadius: 999,
                  backgroundColor:
                    idx === activeCueIndex
                      ? accentHex
                      : idx < activeCueIndex
                      ? `${accentHex}66`
                      : 'rgba(148, 163, 184, 0.25)',
                }}
              />
            ))}
          </div>
        )}

        <div
          style={{
            fontSize: 38,
            fontWeight: 600,
            lineHeight: 1.38,
            color: THEME.colors.textPrimary,
            textAlign: 'center',
            opacity: interpolate(cueEnter, [0, 1], [0.25, 1]),
            transform: `translateY(${interpolate(cueEnter, [0, 1], [10, 0])}px)`,
          }}
        >
          {activeCue
            ? renderHighlightedCue(activeCue.sub, activeCue.hl, meta.color)
            : ''}
        </div>

        {/* Bottom progress bar for current cue */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            bottom: 0,
            height: 6,
            backgroundColor: 'rgba(148, 163, 184, 0.12)',
          }}
        >
          <div
            style={{
              width: `${cueProgress}%`,
              height: '100%',
              backgroundColor: accentHex,
              boxShadow: `0 0 12px ${accentHex}`,
            }}
          />
        </div>
      </div>
    </AbsoluteFill>
  );
};
