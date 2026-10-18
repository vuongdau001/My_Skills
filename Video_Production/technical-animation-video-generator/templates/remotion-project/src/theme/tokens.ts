export const THEME = {
  fontFamily:
    '-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", sans-serif',
  monoFont: '"SF Mono", "JetBrains Mono", Menlo, monospace',
  colors: {
    bgDeep: '#070B14',
    bgNavy: '#0B1120',
    bgCard: 'rgba(17, 25, 42, 0.92)',
    bgBankStage: 'rgba(13, 27, 48, 0.88)',
    bgTechStage: 'rgba(23, 18, 48, 0.90)',
    borderSubtle: 'rgba(148, 163, 184, 0.18)',
    textPrimary: '#F8FAFC',
    textSecondary: '#CBD5E1',
    textMuted: '#94A3B8',
    cyan: '#38BDF8',
    cyanBg: 'rgba(56, 189, 248, 0.14)',
    green: '#34D399',
    greenBg: 'rgba(52, 211, 153, 0.14)',
    coral: '#FF5A65',
    coralBg: 'rgba(255, 90, 101, 0.15)',
    violet: '#A78BFA',
    violetBg: 'rgba(167, 139, 250, 0.15)',
    amber: '#FBBF24',
    amberBg: 'rgba(251, 191, 36, 0.15)',
  },
  layout: {
    width: 1080,
    height: 1920,
    paddingX: 48,
    topSafeY: 72,
    bottomSafeMargin: 240, // Keeps Vietsub above TikTok/Reels/Shorts bottom UI overlay
  },
} as const;

export type SemanticColorKey = 'cyan' | 'green' | 'coral' | 'violet' | 'amber';

export function getAccentHex(key: SemanticColorKey): string {
  return THEME.colors[key];
}

export function getAccentBg(key: SemanticColorKey): string {
  switch (key) {
    case 'cyan':
      return THEME.colors.cyanBg;
    case 'green':
      return THEME.colors.greenBg;
    case 'coral':
      return THEME.colors.coralBg;
    case 'violet':
      return THEME.colors.violetBg;
    case 'amber':
      return THEME.colors.amberBg;
  }
}
