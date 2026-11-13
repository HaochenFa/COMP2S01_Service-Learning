import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";
import { Robi } from "./Robi";
import { Mood } from "./Face";
import { Icon } from "./Bits";
import { BODY, HEAD, T } from "./theme";
import A from "./robiAnchors.json";

export type StickerProps = { mood: Mood; armL: number; armR: number; tint?: string; tintAmt?: number; hat?: boolean; antenna?: string; lookX?: number; lookY?: number; up?: number; down?: number; progress?: number };

const ChefHat: React.FC<{ size: number }> = ({ size }) => {
  const k = size / A.size;
  const cx = A.headTop[0] * k;
  const top = (A.headTop[1] - 250) * k;
  return (
    <svg style={{ position: "absolute", left: cx - 230 * k, top, width: 460 * k, height: 330 * k, overflow: "visible", transform: "rotate(-6deg)" }} viewBox="0 0 460 330">
      <defs>
        <radialGradient id="puff" cx="40%" cy="30%" r="75%">
          <stop offset="0%" stopColor="#ffffff" />
          <stop offset="75%" stopColor="#F1EEE8" />
          <stop offset="100%" stopColor="#DCD6CB" />
        </radialGradient>
        <linearGradient id="band" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stopColor="#ffffff" />
          <stop offset="100%" stopColor="#E3DED4" />
        </linearGradient>
        <filter id="hs" x="-20%" y="-20%" width="140%" height="160%">
          <feDropShadow dx="0" dy="10" stdDeviation="9" floodColor="#6b5a3a" floodOpacity="0.28" />
        </filter>
      </defs>
      <g filter="url(#hs)">
        <circle cx={120} cy={150} r={100} fill="url(#puff)" />
        <circle cx={340} cy={150} r={100} fill="url(#puff)" />
        <circle cx={230} cy={110} r={125} fill="url(#puff)" />
        <rect x={95} y={190} width={270} height={115} rx={30} fill="url(#band)" />
        <path d="M170 200 L175 290 M230 200 L230 292 M290 200 L285 290" stroke="#D8D1C4" strokeWidth={6} strokeLinecap="round" />
      </g>
    </svg>
  );
};

export const RobiSticker: React.FC<StickerProps> = ({ mood, armL, armR, tint, tintAmt = 0, hat, antenna = "#FFE89A", lookX = 0, lookY = 0, up = 0, down = 0, progress = 0 }) => {
  const size = 1000;
  return (
    <AbsoluteFill style={{ background: "transparent" }}>
      <Robi x={500} y={A.feet[1] * (size / A.size)} size={size} mood={mood} armL={armL} armR={armR} tint={tint} tintAmt={tintAmt} shadow={0} antenna={antenna} antennaOn={0.7} lookX={lookX} lookY={lookY} up={up} down={down} progress={progress} frame={8} />
      {hat ? <ChefHat size={size} /> : null}
    </AbsoluteFill>
  );
};

/** Simplified Teachable Machine workflow diagram in our palette. */
export const TMDiagram: React.FC = () => {
  const card = (style: React.CSSProperties, children: React.ReactNode) => (
    <div style={{ position: "absolute", background: "#fff", borderRadius: 28, boxShadow: "0 14px 34px rgba(60,40,20,0.14)", border: "3px solid #EFE6D6", padding: 24, boxSizing: "border-box", ...style }}>{children}</div>
  );
  const badge = (n: number, label: string, color: string, style: React.CSSProperties) => (
    <div style={{ position: "absolute", display: "flex", alignItems: "center", gap: 12, background: color, color: "#fff", borderRadius: 999, padding: "8px 24px 8px 8px", fontFamily: HEAD, fontWeight: 700, fontSize: 40, boxShadow: `0 8px 18px ${color}55`, ...style }}>
      <span style={{ width: 48, height: 48, borderRadius: 99, background: "#fff", color, display: "flex", alignItems: "center", justifyContent: "center" }}>{n}</span>
      {label}
    </div>
  );
  const classCard = (kind: "up" | "down", top: number, photos: string[]) =>
    card({ left: 40, top, width: 640, height: 335 }, (
      <>
        <div style={{ display: "flex", alignItems: "center", gap: 14, fontFamily: HEAD, fontWeight: 600, fontSize: 40, color: T.ink }}>
          <span style={{ width: 54, height: 54, borderRadius: 14, background: kind === "up" ? T.up : T.down, display: "flex", alignItems: "center", justifyContent: "center" }}>
            <Icon name={kind === "up" ? "thumbsUp" : "thumbsDown"} size={34} color="#fff" />
          </span>
          {kind === "up" ? "Thumbs up" : "Thumbs down"}
          <span style={{ marginLeft: "auto", fontFamily: BODY, fontSize: 28, color: T.inkSoft }}>50 samples</span>
        </div>
        <div style={{ display: "flex", gap: 14, marginTop: 20 }}>
          <div style={{ width: 150, height: 150, borderRadius: 18, border: `4px dashed ${kind === "up" ? T.up : T.down}`, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 6, fontFamily: BODY, fontWeight: 600, fontSize: 22, color: kind === "up" ? T.up : T.down }}>
            <Icon name="camera" size={52} color={kind === "up" ? T.up : T.down} />
            Webcam
          </div>
          {photos.map((p, i) => (
            <Img key={i} src={staticFile(`v2/photos/${p}`)} style={{ width: 100, height: 100, borderRadius: 12, marginTop: i % 2 ? 50 : 0 }} />
          ))}
        </div>
        <div style={{ position: "absolute", left: 24, bottom: 18, fontFamily: BODY, fontWeight: 600, fontSize: 22, color: T.inkSoft, display: "flex", alignItems: "center", gap: 8 }}>
          <span style={{ background: T.navy, color: "#fff", borderRadius: 12, padding: "6px 16px", fontFamily: HEAD, fontWeight: 600, fontSize: 28 }}>Hold to Record</span>
        </div>
      </>
    ));
  return (
    <AbsoluteFill style={{ background: "transparent" }}>
      {classCard("up", 64, ["up_04.jpg", "up_13.jpg", "up_07.jpg", "up_06.jpg"])}
      {classCard("down", 470, ["down_02.jpg", "down_08.jpg", "down_12.jpg", "down_10.jpg"])}
      {card({ left: 760, top: 300, width: 330, height: 200 }, (
        <>
          <div style={{ fontFamily: HEAD, fontWeight: 600, fontSize: 40, color: T.ink }}>Training</div>
          <div style={{ marginTop: 22, background: T.up, color: "#fff", borderRadius: 16, padding: "18px 0", textAlign: "center", fontFamily: HEAD, fontWeight: 700, fontSize: 32 }}>Train Model</div>
        </>
      ))}
      {card({ left: 1170, top: 120, width: 400, height: 620 }, (
        <>
          <div style={{ fontFamily: HEAD, fontWeight: 600, fontSize: 40, color: T.ink }}>Preview</div>
          <Img src={staticFile("v2/photos/new_up.jpg")} style={{ width: 352, height: 300, objectFit: "cover", borderRadius: 18, marginTop: 14 }} />
          {[
            ["up", 97],
            ["down", 3],
          ].map(([k, v]) => (
            <div key={k as string} style={{ display: "flex", alignItems: "center", gap: 12, marginTop: 22 }}>
              <span style={{ width: 50, height: 50, borderRadius: 14, background: k === "up" ? T.up : T.down, display: "flex", alignItems: "center", justifyContent: "center" }}>
                <Icon name={k === "up" ? "thumbsUp" : "thumbsDown"} size={32} color="#fff" />
              </span>
              <div style={{ flex: 1, height: 30, borderRadius: 99, background: k === "up" ? T.upSoft : T.downSoft, overflow: "hidden" }}>
                <div style={{ width: `${Math.max(5, v as number)}%`, height: "100%", background: k === "up" ? T.up : T.down, borderRadius: 99 }} />
              </div>
              <span style={{ fontFamily: HEAD, fontWeight: 700, fontSize: 34, color: k === "up" ? T.up : T.down, width: 80, textAlign: "right" }}>{v}%</span>
            </div>
          ))}
        </>
      ))}
      {/* connectors */}
      <svg style={{ position: "absolute", inset: 0 }} width={1600} height={900}>
        {[
          "M680 232 C 720 232, 720 360, 760 380",
          "M680 638 C 720 638, 720 440, 760 420",
          "M1090 400 C 1130 400, 1130 400, 1170 400",
        ].map((d, i) => (
          <path key={i} d={d} stroke="#C9BBA2" strokeWidth={6} fill="none" strokeDasharray="4 14" strokeLinecap="round" />
        ))}
      </svg>
      {badge(1, "RECORD", T.up, { left: 60, top: 10 })}
      {badge(2, "TRAIN", "#C9530A", { left: 790, top: 232 })}
      {badge(3, "TEST", "#178A50", { left: 1210, top: 58 })}
    </AbsoluteFill>
  );
};
