import React from "react";
import { Img, staticFile } from "remotion";
import { Face, FaceProps } from "./Face";
import A from "./robiAnchors.json";

export type RobiProps = FaceProps & {
  x: number; // feet x in px
  y: number; // feet y in px (bottom of body)
  size: number; // displayed size of the 1400px render canvas
  armL?: number; // CSS degrees, 0 = hanging down, + = outward
  armR?: number; // CSS degrees, 0 = hanging down, - = outward
  tilt?: number; // degrees
  bob?: number; // px vertical offset (floating)
  antenna?: string; // glow colour
  antennaOn?: number; // 0..1
  shadow?: number; // 0..1 opacity
  tint?: string; // optional colour wash (e.g. monster)
  tintAmt?: number;
  style?: React.CSSProperties;
};

const S = A.size;
const pct = (v: number) => `${(v / S) * 100}%`;

export const Robi: React.FC<RobiProps> = ({
  x,
  y,
  size,
  armL = 16,
  armR = -16,
  tilt = 0,
  bob = 0,
  antenna = "#FFE89A",
  antennaOn = 0.6,
  shadow = 1,
  tint,
  tintAmt = 0,
  style,
  ...face
}) => {
  const k = size / S;
  const left = x - size / 2;
  const top = y - A.feet[1] * k;
  const [sx0, sy0, sx1, sy1] = A.screen;
  const arm = (side: "L" | "R", deg: number) => {
    const p = side === "L" ? A.shoulderL : A.shoulderR;
    return (
      <Img
        src={staticFile(`v2/robi/robi_arm${side}.png`)}
        style={{
          position: "absolute",
          inset: 0,
          width: "100%",
          height: "100%",
          transformOrigin: `${pct(p[0])} ${pct(p[1])}`,
          transform: `rotate(${deg}deg)`,
        }}
      />
    );
  };
  return (
    <div style={{ position: "absolute", left, top: top, width: size, height: size, ...style }}>
      {/* ground shadow (does not bob) */}
      <div
        style={{
          position: "absolute",
          left: pct(A.feet[0] - 300 + bob * 0.4),
          top: pct(A.feet[1] + 70),
          width: pct(600 - bob * 0.8),
          height: pct(90),
          borderRadius: "50%",
          background: "radial-gradient(closest-side, rgba(40,30,20,0.28), rgba(40,30,20,0))",
          opacity: shadow,
        }}
      />
      <div style={{ position: "absolute", inset: 0, transform: `translateY(${-bob}px) rotate(${tilt}deg)`, transformOrigin: `50% ${pct(A.feet[1])}` }}>
        {arm("L", armL)}
        {arm("R", armR)}
        <Img src={staticFile("v2/robi/robi_body.png")} style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }} />
        {tint && tintAmt > 0 ? (
          <div
            style={{
              position: "absolute",
              inset: 0,
              background: tint,
              mixBlendMode: "color",
              opacity: tintAmt,
              WebkitMaskImage: `url(${staticFile("v2/robi/robi_body.png")})`,
              WebkitMaskSize: "100% 100%",
              maskImage: `url(${staticFile("v2/robi/robi_body.png")})`,
              maskSize: "100% 100%",
            }}
          />
        ) : null}
        {/* antenna glow */}
        <div
          style={{
            position: "absolute",
            left: pct(A.ball[0] - 95),
            top: pct(A.ball[1] - 95),
            width: pct(190),
            height: pct(190),
            borderRadius: "50%",
            background: `radial-gradient(closest-side, ${antenna}, rgba(255,255,255,0))`,
            opacity: antennaOn,
            mixBlendMode: "screen",
          }}
        />
        {/* face on the screen */}
        <div style={{ position: "absolute", left: pct(sx0), top: pct(sy0), width: pct(sx1 - sx0), height: pct(sy1 - sy0) }}>
          <Face {...face} />
        </div>
      </div>
      <div style={{ position: "absolute", width: 0, height: 0, left: 0, top: 0, fontSize: k }} />
    </div>
  );
};
