import React from 'react';
import { AbsoluteFill, Composition, Sequence } from 'remotion';
import part1Data from './manifest-part1.json';
import { EpisodeManifest } from './types';
import { BeatScene } from './scenes/BeatScene';
import { STAGES } from './scenes/stages';

/**
 * One composition per part. manifest-partN.json is produced by tools/generate_audio.py --part N.
 * To add part 2: generate src/manifest-part2.json, import it and push it into EPISODES.
 * Composition id = "Part<N>"  →  remotion render src/index.ts Part1 out/<slug>-part1.mp4
 * (Stage components are imported directly, not passed as props: Remotion props must be JSON-serializable.)
 */
const EPISODES: EpisodeManifest[] = [part1Data as unknown as EpisodeManifest];

type EpisodeProps = { m: EpisodeManifest };

const Episode: React.FC<EpisodeProps> = ({ m }) => (
  <AbsoluteFill>
    {m.beats.map((beat, idx) => (
      <Sequence
        key={beat.id}
        from={beat.startFrame}
        durationInFrames={beat.durationInFrames}
        name={`${idx + 1}. ${beat.id} (${beat.mode})`}
      >
        <BeatScene part={m.part} totalParts={m.totalParts} chapters={m.chapters} beat={beat} stages={STAGES} />
      </Sequence>
    ))}
  </AbsoluteFill>
);

export const RemotionRoot: React.FC = () => (
  <>
    {EPISODES.map((m) => (
      <Composition
        key={m.part}
        id={`Part${m.part}`}
        component={Episode}
        defaultProps={{ m }}
        durationInFrames={m.totalFrames}
        fps={m.fps}
        width={m.width}
        height={m.height}
      />
    ))}
  </>
);
