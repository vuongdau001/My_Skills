/**
 * Project stages. One component per real/tech beat id, registered in STAGES.
 * RULE: real/tech beats are mechanism SIMULATIONS (MNode + MLink + MPacket + MStore + MVerdict),
 * not card grids. Bridge/outro beats are handled generically by BeatScene.
 *
 * The two stages below are a worked example (Session & Cookie) — replace them per topic.
 * Timing: T(cueIndex, fraction) returns the frame inside the beat where that part of the cue plays.
 */
import React from 'react';
import { BookOpen, Cookie, Database, Globe, Landmark, Server, Ticket, UserRound } from 'lucide-react';
import { StageProps } from '../types';
import { MChip, MLink, MNode, MPacket, MStore, MVerdict, MechStage, XY } from '../primitives/Mechanism';
import { StageRegistry } from './BeatScene';

/** REAL world (no tech words): reception checks ID once → writes ledger → gives visitor card → counter checks ledger. */
const DemoRealStage: React.FC<StageProps> = ({ f, T }) => {
  const C: XY = [150, 200];
  const R: XY = [456, 200];
  const K: XY = [762, 200];
  return (
    <MechStage>
      <MLink f={f} at={4} from={[C[0] + 80, C[1]]} to={[R[0] - 80, R[1]]} color="amber" />
      <MLink f={f} at={8} from={[R[0] + 80, R[1]]} to={[K[0] - 80, K[1]]} color="amber" />
      <MNode f={f} at={0} x={C[0]} y={C[1]} icon={UserRound} label="Khách hàng" color="amber" />
      <MNode f={f} at={4} x={R[0]} y={R[1]} icon={Landmark} label="Lễ tân" color="amber" />
      <MNode f={f} at={8} x={K[0]} y={K[1]} icon={Landmark} label="Quầy 2" color="amber" />
      <MStore
        f={f}
        at={10}
        x={R[0]}
        y={480}
        icon={BookOpen}
        title="Sổ khách"
        color="amber"
        rows={[{ text: 'K7X9 = An', at: T(0, 0.4), strikeAt: T(1, 0.6) }]}
      />
      <MPacket f={f} start={T(0, 0)} end={T(0, 0.3)} from={[C[0], C[1] - 40]} to={[R[0], R[1] - 40]} label="Căn cước" color="amber" mono={false} />
      <MPacket f={f} start={T(0, 0.55)} end={T(0, 0.85)} from={[R[0], R[1] + 40]} to={[C[0], C[1] + 40]} label="Thẻ K7X9" color="green" icon={Ticket} mono={false} />
      <MChip f={f} at={T(0, 0.85)} x={C[0]} y={C[1] + 250} label="Thẻ K7X9" icon={Ticket} color="green" struck={f >= T(1, 0.6)} />
      <MPacket f={f} start={T(1, 0)} end={T(1, 0.3)} from={[C[0], C[1] - 40]} to={[K[0], K[1] - 40]} label="Thẻ K7X9" color="green" mono={false} />
      <MVerdict f={f} at={T(1, 0.35)} until={T(1, 0.6)} x={K[0]} y={380} ok label="Tra sổ: An" />
      <MVerdict f={f} at={T(1, 0.7)} x={K[0]} y={380} ok={false} label="Thẻ vô hiệu" />
    </MechStage>
  );
};

/** TECH: login → session row → Set-Cookie → cookie request → lookup ✔ → row deleted → ✖ 401. */
const DemoTechStage: React.FC<StageProps> = ({ f, T }) => {
  const B: XY = [170, 200];
  const S: XY = [742, 200];
  const ST: XY = [742, 500];
  return (
    <MechStage>
      <MLink f={f} at={4} from={[B[0] + 80, B[1]]} to={[S[0] - 80, S[1]]} color="cyan" />
      <MLink f={f} at={10} from={[S[0], S[1] + 110]} to={ST} color="violet" glowFrom={T(1, 0.7)} />
      <MNode f={f} at={0} x={B[0]} y={B[1]} icon={Globe} label="Browser" color="cyan" />
      <MNode f={f} at={4} x={S[0]} y={S[1]} icon={Server} label="Server" color="cyan" />
      <MStore
        f={f}
        at={8}
        x={ST[0]}
        y={ST[1]}
        icon={Database}
        title="Session Store"
        color="violet"
        width={340}
        rows={[{ text: '9f3a7c… → an', at: T(0, 0.3), strikeAt: T(1, 0.5) }]}
      />
      <MPacket f={f} start={T(0, 0)} end={T(0, 0.22)} from={[B[0], B[1] - 34]} to={[S[0], S[1] - 34]} label="Đăng nhập" color="cyan" mono={false} />
      <MPacket f={f} start={T(0, 0.45)} end={T(0, 0.75)} from={[S[0], S[1] + 34]} to={[B[0], B[1] + 34]} label="Set-Cookie: sid=9f3a7c…" color="green" />
      <MChip f={f} at={T(0, 0.75)} x={B[0]} y={B[1] + 260} label="sid=9f3a7c…" icon={Cookie} color="green" mono struck={f >= T(1, 0.8)} />
      <MPacket f={f} start={T(1, 0)} end={T(1, 0.25)} from={[B[0], B[1] - 34]} to={[S[0], S[1] - 34]} label="Cookie: sid=9f3a7c…" color="green" />
      <MVerdict f={f} at={T(1, 0.28)} until={T(1, 0.5)} x={456} y={370} ok label="Xin chào, An" />
      <MVerdict f={f} at={T(1, 0.8)} x={456} y={370} ok={false} label="401 · Đã đăng xuất" />
    </MechStage>
  );
};

export const STAGES: StageRegistry = {
  demo_real: DemoRealStage,
  demo_tech: DemoTechStage,
};
