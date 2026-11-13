import React from "react";
import { ICONS } from "./iconPaths";
import { T } from "./theme";

export type Mood =
  | "neutral"
  | "happy"
  | "think"
  | "confused"
  | "wow"
  | "monster"
  | "love"
  | "sleep"
  | "blank"
  | "question"
  | "check"
  | "loading"
  | "bars";

export type FaceProps = {
  mood: Mood;
  blink?: number; // 0 open … 1 closed
  lookX?: number;
  lookY?: number;
  progress?: number; // loading 0..1
  up?: number; // bars %
  down?: number;
  glitch?: number; // 0..1 jitter for monster/confused
  frame?: number;
};

const W = 116;
const H = 79;

const Icon: React.FC<{ name: string; x: number; y: number; s: number; color: string }> = ({ name, x, y, s, color }) => (
  <g transform={`translate(${x} ${y}) scale(${s / 256})`}>
    {ICONS[name].map((d, i) => (
      <path key={i} d={d} fill={color} />
    ))}
  </g>
);

export const Face: React.FC<FaceProps> = ({ mood, blink = 0, lookX = 0, lookY = 0, progress = 0, up = 0, down = 0, glitch = 0, frame = 0 }) => {
  const glow = mood === "monster" ? "#D46BFF" : T.tealGlow;
  const eyeH = 25 * (1 - 0.92 * blink);
  const jx = glitch ? Math.sin(frame * 2.7) * glitch * 2.2 : 0;
  const jy = glitch ? Math.cos(frame * 3.3) * glitch * 1.2 : 0;
  const ex = lookX + jx;
  const ey = lookY + jy;
  const pill = (cx: number, cy: number, w = 15, h = eyeH) => (
    <rect x={cx - w / 2} y={cy - h / 2} width={w} height={Math.max(h, 2.6)} rx={Math.min(w, Math.max(h, 2.6)) / 2} fill={glow} />
  );
  let content: React.ReactNode = null;
  switch (mood) {
    case "neutral":
      content = (
        <>
          {pill(38 + ex, 35 + ey)}
          {pill(78 + ex, 35 + ey)}
          <path d={`M51 ${58 + ey * 0.4} Q58 ${63 + ey * 0.4} 65 ${58 + ey * 0.4}`} stroke={glow} strokeWidth={3.2} fill="none" strokeLinecap="round" />
        </>
      );
      break;
    case "happy":
      content = (
        <>
          <path d={`M${29 + ex} ${41 + ey} Q${38 + ex} ${27 + ey} ${47 + ex} ${41 + ey}`} stroke={glow} strokeWidth={6} fill="none" strokeLinecap="round" />
          <path d={`M${69 + ex} ${41 + ey} Q${78 + ex} ${27 + ey} ${87 + ex} ${41 + ey}`} stroke={glow} strokeWidth={6} fill="none" strokeLinecap="round" />
          <path d="M47 54 Q58 67 69 54" stroke={glow} strokeWidth={4} fill="none" strokeLinecap="round" />
        </>
      );
      break;
    case "think":
      content = (
        <>
          {pill(42 + ex + 5, 33 + ey - 4, 14)}
          {pill(80 + ex + 5, 33 + ey - 4, 14)}
          <path d="M52 60 L64 58" stroke={glow} strokeWidth={3.2} strokeLinecap="round" />
          {[0, 1, 2].map((i) => (
            <circle key={i} cx={92 + i * 7} cy={60} r={2.4} fill={glow} opacity={0.35 + 0.65 * Math.max(0, Math.sin((frame - i * 5) / 5))} />
          ))}
        </>
      );
      break;
    case "confused":
      content = (
        <>
          {pill(38 + ex, 36 + ey, 15, eyeH)}
          <circle cx={78 + ex} cy={33 + ey} r={6.5 * (1 - 0.8 * blink) + 0.8} fill={glow} />
          <path d="M47 59 q4 -4 8 0 t8 0 t8 0" stroke={glow} strokeWidth={3.2} fill="none" strokeLinecap="round" />
        </>
      );
      break;
    case "wow":
      content = (
        <>
          <circle cx={38 + ex} cy={35 + ey} r={9.5 * (1 - 0.85 * blink) + 0.6} fill={glow} />
          <circle cx={78 + ex} cy={35 + ey} r={9.5 * (1 - 0.85 * blink) + 0.6} fill={glow} />
          <ellipse cx={58} cy={60} rx={4.5} ry={5.5} fill="none" stroke={glow} strokeWidth={3} />
        </>
      );
      break;
    case "monster":
      content = (
        <>
          <path d={`M${27 + ex} ${28 + ey} L${48 + ex} ${36 + ey} L${44 + ex} ${42 + ey} L${28 + ex} ${38 + ey} Z`} fill={glow} />
          <path d={`M${89 + ex} ${28 + ey} L${68 + ex} ${36 + ey} L${72 + ex} ${42 + ey} L${88 + ex} ${38 + ey} Z`} fill={glow} />
          <path d="M36 56 L44 62 L52 55 L60 62 L68 55 L76 62 L82 56" stroke={glow} strokeWidth={3.4} fill="none" strokeLinejoin="round" strokeLinecap="round" />
        </>
      );
      break;
    case "love":
      content = (
        <>
          <Icon name="star" x={26 + ex} y={22 + ey} s={24} color={T.yellow} />
          <Icon name="star" x={66 + ex} y={22 + ey} s={24} color={T.yellow} />
          <path d="M47 54 Q58 67 69 54" stroke={glow} strokeWidth={4} fill="none" strokeLinecap="round" />
        </>
      );
      break;
    case "sleep":
      content = (
        <>
          <path d="M30 37 L46 37 M70 37 L86 37" stroke={glow} strokeWidth={4} strokeLinecap="round" opacity={0.75} />
          <text x={92} y={22} fill={glow} fontFamily="Fredoka" fontWeight={700} fontSize={12} opacity={0.7}>
            z
          </text>
        </>
      );
      break;
    case "question":
      content = <Icon name="question" x={36} y={18} s={44} color={T.yellow} />;
      break;
    case "check":
      content = <Icon name="check" x={34} y={15} s={48} color="#5BF29A" />;
      break;
    case "loading": {
      const r = 20;
      const c = 2 * Math.PI * r;
      content = (
        <>
          <circle cx={58} cy={39.5} r={r} fill="none" stroke={glow} strokeOpacity={0.18} strokeWidth={6} />
          <circle cx={58} cy={39.5} r={r} fill="none" stroke={glow} strokeWidth={6} strokeDasharray={`${c * progress} ${c}`} strokeLinecap="round" transform="rotate(-90 58 39.5)" />
          <text x={58} y={44} textAnchor="middle" fill={glow} fontFamily="Fredoka" fontWeight={700} fontSize={13}>
            {Math.round(progress * 100)}%
          </text>
        </>
      );
      break;
    }
    case "bars": {
      const row = (y: number, icon: string, v: number, col: string) => (
        <g>
          <Icon name={icon} x={11} y={y - 9} s={18} color={col} />
          <rect x={33} y={y - 5} width={56} height={10} rx={5} fill={col} opacity={0.2} />
          <rect x={33} y={y - 5} width={Math.max(10, 56 * v / 100)} height={10} rx={5} fill={col} />
          <text x={92} y={y + 4} fill={col} fontFamily="Fredoka" fontWeight={700} fontSize={10.5}>
            {Math.round(v)}%
          </text>
        </g>
      );
      content = (
        <>
          {row(27, "thumbsUp", up, "#7FA6FF")}
          {row(53, "thumbsDown", down, "#FF8B78")}
        </>
      );
      break;
    }
    default:
      content = null;
  }
  return (
    <svg viewBox={`0 0 ${W} ${H}`} width="100%" height="100%" style={{ position: "absolute", inset: 0, overflow: "visible", mixBlendMode: "screen" }}>
      <defs>
        <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="1.7" result="b" />
          <feMerge>
            <feMergeNode in="b" />
            <feMergeNode in="b" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      <g filter="url(#glow)">{content}</g>
    </svg>
  );
};
