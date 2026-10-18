export type BeatMode = 'real' | 'tech' | 'bridge' | 'outro' | 'summary';

export interface CueManifest {
  sub: string;
  hl: string[];
  audioFile: string;
  /** relative to beat start */
  startFrame: number;
  durationInFrames: number;
}

export interface MapBar {
  real: string;
  tech: string;
}

export interface BeatManifest {
  id: string;
  sceneId: string;
  sceneTitle: string;
  act: string;
  mode: BeatMode;
  stage: string[];
  mapBar: MapBar | null;
  startFrame: number;
  durationInFrames: number;
  cues: CueManifest[];
}

export interface ChapterManifest {
  id: string;
  title: string;
  act: string;
  startFrame: number;
}

export interface EpisodeManifest {
  title: string;
  part: number;
  totalParts: number;
  voiceProvider: string;
  fps: number;
  width: number;
  height: number;
  totalFrames: number;
  totalDurationSec: number;
  chapters: ChapterManifest[];
  beats: BeatManifest[];
}

/** Props every stage component receives. `f` = frame inside the beat. */
export interface StageProps {
  f: number;
  beat: BeatManifest;
  /** T(cueIndex, fraction 0..1) → frame inside beat */
  T: (cue: number, frac?: number) => number;
}

export function splitPairs(mapBar: MapBar | null): Array<[string, string]> {
  if (!mapBar) return [];
  const r = mapBar.real.split(' · ');
  const t = mapBar.tech.split(' · ');
  return r.map((x, i) => [x, t[i] ?? t[t.length - 1]]);
}
