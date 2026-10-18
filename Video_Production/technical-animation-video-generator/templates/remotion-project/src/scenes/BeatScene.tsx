import React from 'react';
import { Audio, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { ArrowRight, Landmark, Play } from 'lucide-react';
import { THEME } from '../theme/tokens';
import { BeatManifest, ChapterManifest, StageProps } from '../types';
import { SceneFrame } from '../primitives/SceneFrame';

/** Map beat id → stage component. Real/tech beats should be mechanism simulations. */
export type StageRegistry = Record<string, React.FC<StageProps>>;

/* Generic chapter bridge: stage[0] = chapter number, stage[1] = next topic. */
export const BridgeStage: React.FC<StageProps> = ({ f, beat }) => {
  const { fps } = useVideoConfig();
  const enter = spring({
    frame: f,
    fps,
    config: { damping: 18, stiffness: 140 },
  });
  const stepNum = beat.stage[0] ?? '•';
  const nextTopic = beat.stage[1] ?? beat.sceneTitle;

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 34,
        height: '100%',
        padding: '0 24px',
      }}
    >
      <div
        style={{
          width: 136,
          height: 136,
          borderRadius: 999,
          backgroundColor: THEME.colors.violetBg,
          border: `3px solid ${THEME.colors.violet}`,
          boxShadow: `0 0 48px ${THEME.colors.violet}55`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 64,
          fontWeight: 800,
          color: THEME.colors.violet,
          transform: `scale(${interpolate(enter, [0, 1], [0.7, 1])})`,
        }}
      >
        {stepNum}
      </div>

      <div
        style={{
          fontSize: 26,
          fontWeight: 700,
          color: THEME.colors.textSecondary,
          letterSpacing: 1.5,
          textTransform: 'uppercase',
        }}
      >
        PHƯƠNG PHÁP TIẾP THEO
      </div>

      <div
        style={{
          padding: '28px 42px',
          borderRadius: 30,
          backgroundColor: 'rgba(15, 23, 42, 0.92)',
          border: `2.5px solid ${THEME.colors.cyan}`,
          boxShadow: `0 20px 50px rgba(0,0,0,0.45), 0 0 32px ${THEME.colors.cyan}33`,
          fontSize: 48,
          fontWeight: 800,
          color: THEME.colors.textPrimary,
          textAlign: 'center',
        }}
      >
        {nextTopic}
      </div>

      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: 14,
          padding: '12px 24px',
          borderRadius: 999,
          backgroundColor: THEME.colors.amberBg,
          border: `1.5px solid ${THEME.colors.amber}66`,
          fontSize: 25,
          fontWeight: 700,
          color: THEME.colors.amber,
        }}
      >
        <Landmark size={24} color={THEME.colors.amber} />
        <span>Bắt đầu từ ví dụ thực tế</span>
        <ArrowRight size={22} color={THEME.colors.amber} />
      </div>
    </div>
  );
};


/* Generic outro: stage[0] = next episode title, stage[1] = "A · B · C" upcoming topics. */
export const OutroStage: React.FC<StageProps> = ({ f, beat }) => {
  const { fps } = useVideoConfig();
  const title = beat.stage[0] ?? 'Tập tiếp theo';
  const topics = (beat.stage[1] ?? '').split(' · ').filter(Boolean);
  const enter = spring({ frame: f, fps, config: { damping: 18, stiffness: 140 } });
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 34, height: '100%' }}>
      <div
        style={{
          display: 'flex', alignItems: 'center', gap: 16, padding: '18px 34px', borderRadius: 999,
          backgroundColor: THEME.colors.greenBg, border: `3px solid ${THEME.colors.green}`,
          fontSize: 54, fontWeight: 800, color: THEME.colors.green,
          transform: `scale(${interpolate(enter, [0, 1], [0.8, 1])})`,
        }}
      >
        <Play size={44} color={THEME.colors.green} strokeWidth={2.6} />
        {title}
      </div>
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: 18, maxWidth: 860 }}>
        {topics.map((t, i) => {
          const p = spring({ frame: Math.max(0, f - 8 - i * 6), fps, config: { damping: 18 } });
          return (
            <div
              key={t}
              style={{
                padding: '16px 28px', borderRadius: 20, backgroundColor: 'rgba(15,23,42,0.92)',
                border: `2px solid ${THEME.colors.cyan}88`, fontSize: 36, fontWeight: 800,
                color: THEME.colors.textPrimary, opacity: f >= 8 + i * 6 ? p : 0,
              }}
            >
              {t}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export const BeatScene: React.FC<{
  part: number;
  totalParts: number;
  chapters: ChapterManifest[];
  beat: BeatManifest;
  stages: StageRegistry;
}> = ({ part, totalParts, chapters, beat, stages }) => {
  const f = useCurrentFrame();
  const T = (cueIdx: number, frac = 0): number => {
    const c = beat.cues[Math.min(cueIdx, beat.cues.length - 1)];
    return c ? Math.round(c.startFrame + c.durationInFrames * frac) : 0;
  };
  let activeCueIndex = 0;
  beat.cues.forEach((c, i) => {
    if (f >= c.startFrame - 4) activeCueIndex = i;
  });
  const activeCue = beat.cues[activeCueIndex] ?? null;
  const cueFrame = activeCue ? f - activeCue.startFrame : 0;

  const Stage =
    beat.mode === 'bridge' ? BridgeStage : beat.mode === 'outro' ? OutroStage : stages[beat.id] ?? BridgeStage;

  return (
    <SceneFrame
      part={part}
      totalParts={totalParts}
      chapters={chapters}
      beat={beat}
      beatFrame={f}
      activeCue={activeCue}
      activeCueIndex={activeCueIndex}
      cueFrame={cueFrame}
    >
      {beat.cues.map((cue, idx) => (
        <Sequence key={idx} from={cue.startFrame} durationInFrames={cue.durationInFrames} name={`Cue ${idx}`}>
          <Audio src={staticFile(cue.audioFile)} />
        </Sequence>
      ))}
      <Stage f={f} beat={beat} T={T} />
    </SceneFrame>
  );
};
