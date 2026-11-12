import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";
import { ICONS } from "./iconPaths";
import { BODY, HEAD, T, ease, map } from "./theme";

export const Icon: React.FC<{ name: string; size: number; color: string; style?: React.CSSProperties }> = ({ name, size, color, style }) => (
  <svg viewBox="0 0 256 256" width={size} height={size} style={{ display: "inline-block", verticalAlign: "middle", ...style }}>
    {ICONS[name].map((d, i) => (
      <path key={i} d={d} fill={color} />
    ))}
  </svg>
);

/** Warm notebook paper with a dot grid. */
export const Paper: React.FC<{ frame: number; tone?: string }> = ({ frame, tone = T.paper }) => (
  <AbsoluteFill style={{ background: tone }}>
    <AbsoluteFill
      style={{
        backgroundImage: `radial-gradient(${T.paperDot} 2.2px, transparent 2.4px)`,
        backgroundSize: "44px 44px",
        backgroundPosition: `${(frame * 0.15) % 44}px ${(frame * 0.08) % 44}px`,
        opacity: 0.9,
      }}
    />
    <AbsoluteFill style={{ background: "radial-gradient(ellipse at 50% 45%, rgba(255,255,255,0) 55%, rgba(120,90,50,0.10) 100%)" }} />
  </AbsoluteFill>
);

/** Caption text supports **highlight** and [up]/[down] inline hand icons. */
const renderRich = (text: string, hl: string, iconSize: number) => {
  const parts = text.split(/(\*\*[^*]+\*\*|\[up\]|\[down\])/g).filter(Boolean);
  return parts.map((p, i) => {
    if (p === "[up]")
      return (
        <span key={i} style={{ display: "inline-flex", alignItems: "center", justifyContent: "center", background: T.up, borderRadius: 18, width: iconSize * 1.35, height: iconSize * 1.2, margin: "0 6px", verticalAlign: "-0.18em" }}>
          <Icon name="thumbsUp" size={iconSize * 0.82} color="#fff" />
        </span>
      );
    if (p === "[down]")
      return (
        <span key={i} style={{ display: "inline-flex", alignItems: "center", justifyContent: "center", background: T.down, borderRadius: 18, width: iconSize * 1.35, height: iconSize * 1.2, margin: "0 6px", verticalAlign: "-0.18em" }}>
          <Icon name="thumbsDown" size={iconSize * 0.82} color="#fff" />
        </span>
      );
    if (p.startsWith("**"))
      return (
        <span key={i} style={{ color: hl }}>
          {p.slice(2, -2)}
        </span>
      );
    return <span key={i}>{p}</span>;
  });
};

export type Cap = { from: number; to: number; text: string; hl?: string };
export const Captions: React.FC<{ frame: number; caps: Cap[] }> = ({ frame, caps }) => (
  <>
    {caps.map((c, i) => {
      if (frame < c.from - 2 || frame > c.to + 12) return null;
      const a = ease(frame, c.from, c.from + 12) * (1 - ease(frame, c.to, c.to + 10));
      const dy = map(frame, c.from, c.from + 14, 26, 0);
      return (
        <div key={i} style={{ position: "absolute", left: 0, right: 0, bottom: 58, display: "flex", justifyContent: "center", opacity: a, transform: `translateY(${dy}px)` }}>
          <div
            style={{
              background: T.navy,
              color: "#fff",
              fontFamily: HEAD,
              fontWeight: 600,
              fontSize: 64,
              lineHeight: 1.15,
              padding: "22px 52px 26px",
              borderRadius: 999,
              boxShadow: "0 12px 30px rgba(23,33,61,0.25)",
              letterSpacing: 0.3,
              whiteSpace: "nowrap",
            }}
          >
            {renderRich(c.text, c.hl ?? T.yellow, 58)}
          </div>
        </div>
      );
    })}
  </>
);

const STEPS = [
  { n: 1, label: "SHOW", color: T.up, icon: "camera" },
  { n: 2, label: "TRAIN", color: "#F29A1F", icon: "brain" },
  { n: 3, label: "TEST", color: T.green, icon: "magnifier" },
];
export const StepTracker: React.FC<{ frame: number; active: number; show: number }> = ({ frame, active, show }) => (
  <div style={{ position: "absolute", top: 44, left: 0, right: 0, display: "flex", justifyContent: "center", gap: 26, opacity: show, transform: `translateY(${(1 - show) * -30}px)` }}>
    {STEPS.map((s) => {
      const on = s.n === active;
      const done = s.n < active;
      return (
        <div
          key={s.n}
          style={{
            display: "flex",
            alignItems: "center",
            gap: 14,
            padding: "12px 30px 12px 14px",
            borderRadius: 999,
            background: on ? s.color : "#fff",
            color: on ? "#fff" : done ? s.color : "#9AA0AE",
            border: `3px solid ${on || done ? s.color : "#E2DACB"}`,
            fontFamily: HEAD,
            fontWeight: 700,
            fontSize: 38,
            transform: `scale(${on ? 1.08 : 0.94})`,
            boxShadow: on ? `0 10px 24px ${s.color}55` : "none",
          }}
        >
          <span style={{ width: 52, height: 52, borderRadius: 99, background: on ? "#fff" : done ? s.color : "#EFE8DA", color: on ? s.color : "#fff", display: "flex", alignItems: "center", justifyContent: "center" }}>
            {done ? <Icon name="check" size={30} color="#fff" /> : <Icon name={s.icon} size={30} color={on ? s.color : "#A89F8E"} />}
          </span>
          {s.n} · {s.label}
        </div>
      );
    })}
  </div>
);

export const PhotoCard: React.FC<{ src: string; size: number; style?: React.CSSProperties; dim?: number }> = ({ src, size, style, dim = 0 }) => (
  <div
    style={{
      position: "absolute",
      width: size,
      height: size,
      padding: size * 0.045,
      background: "#fff",
      borderRadius: size * 0.05,
      boxShadow: `0 ${size * 0.04}px ${size * 0.09}px rgba(60,40,20,0.20)`,
      boxSizing: "border-box",
      ...style,
    }}
  >
    <Img src={staticFile(`v2/photos/${src}`)} style={{ width: "100%", height: "100%", borderRadius: size * 0.03, display: "block", filter: dim ? `grayscale(${dim}) brightness(${1 - dim * 0.15})` : undefined }} />
  </div>
);

export const NewTag: React.FC<{ s: number; style?: React.CSSProperties }> = ({ s, style }) => (
  <div style={{ position: "absolute", transform: `scale(${s}) rotate(-10deg)`, ...style }}>
    <svg width={190} height={190} viewBox="0 0 200 200">
      <polygon
        points={Array.from({ length: 24 })
          .map((_, i) => {
            const r = i % 2 ? 78 : 98;
            const a = (i / 24) * Math.PI * 2;
            return `${100 + r * Math.cos(a)},${100 + r * Math.sin(a)}`;
          })
          .join(" ")}
        fill={T.yellow}
        stroke="#fff"
        strokeWidth={8}
        strokeLinejoin="round"
      />
      <text x={100} y={116} textAnchor="middle" fontFamily={HEAD} fontWeight={700} fontSize={50} fill={T.ink}>
        NEW!
      </text>
    </svg>
  </div>
);

export const Sparkles: React.FC<{ frame: number; start: number; x: number; y: number; r?: number; color?: string; n?: number }> = ({ frame, start, x, y, r = 160, color = T.yellow, n = 10 }) => {
  const t = frame - start;
  if (t < 0 || t > 30) return null;
  const p = t / 30;
  return (
    <>
      {Array.from({ length: n }).map((_, i) => {
        const a = (i / n) * Math.PI * 2 + 0.3;
        const d = r * (0.3 + 0.9 * Math.sqrt(p));
        const s = (1 - p) * (i % 2 ? 34 : 48);
        return <Icon key={i} name="sparkle" size={s} color={i % 3 === 0 ? T.up : color} style={{ position: "absolute", left: x + Math.cos(a) * d - s / 2, top: y + Math.sin(a) * d - s / 2, opacity: 1 - p * 0.6 }} />;
      })}
    </>
  );
};

/** label chip with a hand icon */
export const ClassChip: React.FC<{ kind: "up" | "down"; text: string; size?: number; style?: React.CSSProperties }> = ({ kind, text, size = 40, style }) => (
  <div
    style={{
      position: "absolute",
      display: "inline-flex",
      alignItems: "center",
      gap: size * 0.35,
      padding: `${size * 0.22}px ${size * 0.7}px ${size * 0.22}px ${size * 0.25}px`,
      borderRadius: 999,
      background: kind === "up" ? T.up : T.down,
      color: "#fff",
      fontFamily: HEAD,
      fontWeight: 600,
      fontSize: size,
      whiteSpace: "nowrap",
      boxShadow: `0 8px 18px ${kind === "up" ? T.up : T.down}44`,
      ...style,
    }}
  >
    <span style={{ width: size * 1.35, height: size * 1.35, borderRadius: 99, background: "#fff", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <Icon name={kind === "up" ? "thumbsUp" : "thumbsDown"} size={size * 0.85} color={kind === "up" ? T.up : T.down} />
    </span>
    {text}
  </div>
);

export const Title: React.FC<{ text: string; size?: number; color?: string; style?: React.CSSProperties }> = ({ text, size = 108, color = T.ink, style }) => (
  <div style={{ position: "absolute", fontFamily: HEAD, fontWeight: 700, fontSize: size, lineHeight: 1.05, color, letterSpacing: -0.5, ...style }}>{text}</div>
);

export const Body: React.FC<{ text: string; size?: number; color?: string; style?: React.CSSProperties }> = ({ text, size = 40, color = T.inkSoft, style }) => (
  <div style={{ position: "absolute", fontFamily: BODY, fontWeight: 500, fontSize: size, color, ...style }}>{text}</div>
);

/** Teachable-Machine-style output bars: how sure Robi is. */
export const GuessPanel: React.FC<{ frame: number; start: number; up: number; down: number; show: number; x: number; y: number }> = ({ frame, start, up, down, show, x, y }) => {
  const p = ease(frame, start, start + 40);
  const row = (kind: "up" | "down", v: number) => (
    <div style={{ display: "flex", alignItems: "center", gap: 18, marginTop: 14 }}>
      <span style={{ width: 64, height: 64, borderRadius: 18, background: kind === "up" ? T.up : T.down, display: "flex", alignItems: "center", justifyContent: "center" }}>
        <Icon name={kind === "up" ? "thumbsUp" : "thumbsDown"} size={40} color="#fff" />
      </span>
      <div style={{ flex: 1, height: 34, borderRadius: 99, background: kind === "up" ? T.upSoft : T.downSoft, overflow: "hidden" }}>
        <div style={{ width: `${Math.max(4, v * p)}%`, height: "100%", borderRadius: 99, background: kind === "up" ? T.up : T.down }} />
      </div>
      <span style={{ width: 120, textAlign: "right", fontFamily: HEAD, fontWeight: 700, fontSize: 48, color: kind === "up" ? T.up : T.down }}>{Math.round(v * p)}%</span>
    </div>
  );
  return (
    <div style={{ position: "absolute", left: x, top: y, width: 520, padding: "18px 26px 24px", background: "#fff", borderRadius: 30, boxShadow: "0 16px 36px rgba(60,40,20,0.16)", opacity: show, transform: `translateY(${(1 - show) * 30}px)` }}>
      <div style={{ fontFamily: HEAD, fontWeight: 600, fontSize: 34, color: T.inkSoft }}>Robi's guess</div>
      {row("up", up)}
      {row("down", down)}
    </div>
  );
};
