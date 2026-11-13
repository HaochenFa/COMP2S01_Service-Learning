import React from "react";
import { useCurrentFrame } from "remotion";
import { C } from "../theme";

type Mood = "happy" | "think" | "confused";

/** "Robi", a friendly original robot. */
export const Robot: React.FC<{ mood?: Mood; size?: number; style?: React.CSSProperties; wave?: boolean }> = ({
  mood = "happy",
  size = 320,
  style,
  wave = false,
}) => {
  const frame = useCurrentFrame();
  const blink = frame % 90 > 84 ? 0.15 : 1;
  const look = mood === "think" ? Math.sin(frame / 8) * 10 : 0;
  const armRot = wave ? Math.sin(frame / 5) * 25 - 20 : 10;
  const eyeY = mood === "think" ? 100 : 112;
  return (
    <svg viewBox="0 0 260 300" width={size} height={size * (300 / 260)} style={style}>
      {/* antenna */}
      <line x1={130} y1={44} x2={130} y2={16} stroke={C.dark} strokeWidth={8} strokeLinecap="round" />
      <circle cx={130} cy={14} r={12} fill={C.gold} stroke={C.dark} strokeWidth={6} />
      {/* arms */}
      <g transform={`rotate(${-armRot} 40 220)`}>
        <rect x={6} y={200} width={40} height={22} rx={11} fill={C.blue} stroke={C.dark} strokeWidth={6} />
      </g>
      <rect x={214} y={200} width={40} height={22} rx={11} fill={C.blue} stroke={C.dark} strokeWidth={6} />
      {/* body */}
      <rect x={70} y={198} width={120} height={80} rx={22} fill={C.blue} stroke={C.dark} strokeWidth={6} />
      <circle cx={130} cy={238} r={13} fill={C.gold} stroke={C.dark} strokeWidth={5} />
      {/* head */}
      <rect x={30} y={44} width={200} height={156} rx={44} fill={C.blue} stroke={C.dark} strokeWidth={6} />
      <rect x={54} y={66} width={152} height={112} rx={28} fill={C.dark} />
      {/* eyes */}
      {mood === "confused" ? (
        <>
          <circle cx={100} cy={112} r={15} fill={C.gold} />
          <circle cx={160} cy={108} r={9} fill={C.gold} />
        </>
      ) : (
        <>
          <ellipse cx={100 + look} cy={eyeY} rx={14} ry={14 * blink} fill={C.gold} />
          <ellipse cx={160 + look} cy={eyeY} rx={14} ry={14 * blink} fill={C.gold} />
        </>
      )}
      {/* mouth */}
      {mood === "happy" && (
        <path d="M100 145 Q130 168 160 145" stroke={C.gold} strokeWidth={8} fill="none" strokeLinecap="round" />
      )}
      {mood === "think" && <rect x={115} y={146} width={30} height={8} rx={4} fill={C.gold} />}
      {mood === "confused" && (
        <path d="M102 152 Q116 142 130 152 T158 150" stroke={C.gold} strokeWidth={7} fill="none" strokeLinecap="round" />
      )}
    </svg>
  );
};
