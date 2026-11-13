import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { Album, ALBUM } from "./Album";
import { Cap, Captions, ClassChip, GuessPanel, NewTag, Paper, PhotoCard, Sparkles, StepTracker, Title } from "./Bits";
import { Mood } from "./Face";
import { Robi } from "./Robi";
import { HEAD, T, ease, glide, inOut, map, pop, vis } from "./theme";

export const TEACH_ROBI_FRAMES = 2250;

type K = [number, number];
const kf = (f: number, keys: K[], e = inOut) => {
  if (f <= keys[0][0]) return keys[0][1];
  for (let i = 0; i < keys.length - 1; i++) {
    const [f0, v0] = keys[i];
    const [f1, v1] = keys[i + 1];
    if (f <= f1) return interpolate(f, [f0, f1], [v0, v1], { easing: e, extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  }
  return keys[keys.length - 1][1];
};
const pick = <V,>(f: number, steps: [number, V][]): V => {
  let v = steps[0][1];
  for (const [s, val] of steps) if (f >= s) v = val;
  return v;
};

const UP = ["up_04.jpg", "up_05.jpg", "up_07.jpg", "up_14.jpg", "up_01.jpg", "up_11.jpg", "up_13.jpg", "up_06.jpg", "up_15.jpg"];
const DOWN = ["down_02.jpg", "down_08.jpg", "down_12.jpg", "down_00.jpg", "down_10.jpg", "down_14.jpg", "down_03.jpg", "down_13.jpg", "down_09.jpg"];
const GRID = ["up_13.jpg", "down_02.jpg", "up_03.jpg", "down_09.jpg", "up_08.jpg", "down_14.jpg", "down_05.jpg", "up_05.jpg", "down_12.jpg", "up_15.jpg", "down_07.jpg", "up_06.jpg"];
const SAME_UP = Array(9).fill("same_up.jpg");
const SAME_DOWN = Array(9).fill("same_down.jpg");

const CAPS: Cap[] = [
  { from: 150, to: 260, text: "This is **Robi**, a brand-new AI." },
  { from: 272, to: 438, text: "Is it [up] or [down]? Robi can't tell!" },
  { from: 455, to: 545, text: "How do **YOU** know?" },
  { from: 552, to: 656, text: "You have seen **LOTS** of examples!" },
  { from: 690, to: 872, text: "**1 · SHOW** Robi lots of examples" },
  { from: 880, to: 1046, text: "Examples are **DATA**" },
  { from: 1086, to: 1244, text: "**2 · TRAIN:** Robi studies every photo" },
  { from: 1258, to: 1360, text: "Robi finds the **pattern!**" },
  { from: 1395, to: 1540, text: "**3 · TEST** with a NEW hand" },
  { from: 1556, to: 1690, text: "Robi got it **right!**" },
  { from: 1726, to: 1888, text: "But what if **ALL** the examples look the **SAME**?" },
  { from: 1902, to: 2066, text: "Will Robi still get it right?" },
  { from: 2145, to: 2245, text: "**YOU** are Robi's teachers today!" },
];

export const TeachRobi: React.FC = () => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();

  // ---------------- Robi path ----------------
  const rx = kf(f, [[0, 1440], [135, 1440], [172, 560], [435, 560], [472, 1745], [1050, 1745], [1092, 1660], [1365, 1660], [1402, 560], [1698, 560], [1740, 1640], [2070, 1640], [2104, 960]]);
  const ry = kf(f, [[0, 935], [135, 935], [172, 850], [435, 850], [472, 1018], [1050, 1018], [1092, 880], [1365, 880], [1402, 850], [1698, 850], [1740, 868], [2070, 868], [2104, 845]]);
  const rs = kf(f, [[0, 800], [135, 800], [172, 760], [435, 760], [472, 400], [1050, 400], [1092, 620], [1365, 620], [1402, 740], [1698, 740], [1740, 600], [2070, 600], [2104, 640]]);
  const enter = pop(f, fps, 16, 12);
  const mood = pick<Mood>(f, [
    [0, "happy"],
    [70, "neutral"],
    [180, "happy"],
    [230, "neutral"],
    [288, "question"],
    [362, "confused"],
    [440, "wow"],
    [560, "happy"],
    [640, "wow"],
    [760, "happy"],
    [1050, "neutral"],
    [1096, "loading"],
    [1244, "happy"],
    [1365, "neutral"],
    [1420, "think"],
    [1556, "check"],
    [1602, "happy"],
    [1700, "neutral"],
    [1790, "think"],
    [1900, "question"],
    [1962, "confused"],
    [2072, "happy"],
  ]);
  const bt = (f + 25) % 86;
  const blink = mood === "loading" || mood === "bars" || mood === "check" || mood === "question" ? 0 : bt < 3 ? bt / 3 : bt < 6 ? (6 - bt) / 3 : 0;
  const lookX = kf(f, [[255, 0], [275, 7], [430, 7], [440, 0], [1395, 0], [1410, 6], [1540, 6], [1555, 0]]);
  const wave = (s: number, e: number) => (f >= s && f <= e ? Math.sin((f - s) / 4.2) * 22 * ease(f, s, s + 8) * (1 - ease(f, e - 8, e)) : 0);
  const armRUp = kf(f, [[24, -16], [36, -140], [116, -140], [130, -16], [1556, -16], [1568, -150], [1640, -150], [1652, -16], [2072, -16], [2086, -155]]);
  const armLUp = kf(f, [[1556, 16], [1568, 150], [1640, 150], [1652, 16], [2072, 16], [2086, 155]]);
  const armR = armRUp + wave(36, 116) + (f > 2086 ? Math.sin(f / 5) * 10 : 0);
  const armL = armLUp + (f > 2086 ? -Math.sin(f / 5) * 10 : 0);
  const bob = Math.sin(f / 17) * 9;
  const antenna = pick<string>(f, [
    [0, "#FFE89A"],
    [1096, "#FFC83A"],
    [1244, "#7DF7C9"],
    [1420, "#FFC83A"],
    [1556, "#7DF7C9"],
    [1900, "#C792FF"],
    [2072, "#7DF7C9"],
  ]);
  const antennaOn = mood === "loading" || mood === "think" ? 0.55 + 0.4 * Math.sin(f / 3) : 0.65;
  const glitch = f >= 1900 && f < 1962 ? 0.7 : f >= 1962 && f < 2070 ? 0.25 : 0;
  const loadP = map(f, 1100, 1238, 0, 1, (x) => x);

  // ---------------- scene visibility ----------------
  const titleA = vis(f, 6, 124, 14);
  const card1 = glide(f, fps, 256);
  const card1Out = ease(f, 428, 450);
  const trackerA = ease(f, 645, 668) * (1 - ease(f, 1695, 1712));
  const active = f < 1050 ? 1 : f < 1365 ? 2 : 3;
  const albumA = ease(f, 655, 685) * (1 - ease(f, 1366, 1392));
  const albumX = kf(f, [[655, 960], [1050, 960], [1092, 760]]);
  const albumS = kf(f, [[655, 0.94], [690, 1], [1050, 1], [1092, 0.84]]);
  const appear = Array.from({ length: 18 }).map((_, i) => 692 + i * 11);
  const stamp = pop(f, fps, 886, 9) * (1 - ease(f, 1046, 1060));
  const testCard = glide(f, fps, 1384) * (1 - ease(f, 1695, 1716));
  const sameA = ease(f, 1712, 1740) * (1 - ease(f, 2070, 2092));
  const sameAppear = Array.from({ length: 18 }).map((_, i) => 1722 + i * 4);
  const twistCard = glide(f, fps, 1892) * (1 - ease(f, 2070, 2090));
  const outroA = ease(f, 2080, 2100);

  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      <Paper frame={f} />

      {/* -------- S1 title -------- */}
      {titleA > 0 ? (
        <>
          <div style={{ position: "absolute", left: 150, top: 250, opacity: titleA, transform: `translateY(${(1 - ease(f, 6, 24)) * 30}px)`, display: "flex", alignItems: "center", gap: 14, background: T.navy, color: T.yellow, fontFamily: HEAD, fontWeight: 600, fontSize: 34, padding: "12px 28px", borderRadius: 999, letterSpacing: 1.5 }}>
            TAMING AI · DAY 1
          </div>
          <Title text="How does a" size={122} style={{ left: 150, top: 330, opacity: titleA, transform: `translateY(${(1 - ease(f, 10, 30)) * 40}px)` }} />
          <Title text="computer learn?" size={122} color={T.up} style={{ left: 150, top: 460, opacity: titleA, transform: `translateY(${(1 - ease(f, 16, 36)) * 40}px)` }} />
          <div style={{ position: "absolute", left: 156, top: 640, opacity: titleA * ease(f, 40, 56), display: "flex", gap: 18 }}>
            <ClassChip kind="up" text="Thumbs up" size={38} style={{ position: "relative" }} />
            <ClassChip kind="down" text="Thumbs down" size={38} style={{ position: "relative" }} />
          </div>
        </>
      ) : null}

      {/* -------- S2 the problem -------- */}
      {f >= 250 && f < 455 ? (
        <PhotoCard src="up_04.jpg" size={520} style={{ left: 1080 + (1 - card1) * 700 + card1Out * 900, top: 170, transform: `rotate(${-4 + (1 - card1) * 10}deg)` }} />
      ) : null}

      {/* -------- S3 lots of examples -------- */}
      {f >= 440 && f < 662
        ? GRID.map((src, i) => {
            const p = pop(f, fps, 446 + i * 4, 12) * (1 - ease(f, 636 + (i % 6) * 2, 652 + (i % 6) * 2));
            const col = i % 6;
            const row = Math.floor(i / 6);
            return <PhotoCard key={i} src={src} size={236} style={{ left: 170 + col * 262, top: 168 + row * 280, transform: `scale(${p}) rotate(${((i * 53) % 11) - 5}deg)`, opacity: Math.min(1, p * 1.5) }} />;
          })
        : null}

      {/* -------- S4/S5 album -------- */}
      {albumA > 0 ? (
        <div style={{ position: "absolute", left: albumX - ALBUM.w / 2, top: 215, width: ALBUM.w, height: ALBUM.h, transform: `scale(${albumS})`, transformOrigin: "50% 40%" }}>
          <Album frame={f} fps={fps} up={UP} down={DOWN} appear={appear} show={albumA} scan={[1104, 7]} arrows={f >= 1246 ? 1246 : undefined} />
          {stamp > 0.01 ? (
            <div style={{ position: "absolute", left: ALBUM.w / 2 - 170, top: ALBUM.h / 2 - 85, width: 340, height: 170, transform: `scale(${stamp}) rotate(-8deg)`, background: T.yellow, borderRadius: 34, border: "8px solid #fff", boxShadow: "0 16px 36px rgba(0,0,0,0.22)", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: HEAD, fontWeight: 700, fontSize: 110, color: T.ink, letterSpacing: 4 }}>
              DATA
            </div>
          ) : null}
        </div>
      ) : null}
      <Sparkles frame={f} start={888} x={960} y={540} r={260} />

      {/* -------- S6 test -------- */}
      {testCard > 0.001 ? (
        <div style={{ position: "absolute", left: 1150 + (1 - testCard) * 760, top: 150, transform: `rotate(${3 - (1 - testCard) * 8}deg)` }}>
          <PhotoCard src="new_up.jpg" size={500} style={{ position: "relative" }} />
          <NewTag s={pop(f, fps, 1404, 9)} style={{ left: 380, top: -48 }} />
        </div>
      ) : null}
      {testCard > 0.001 ? <GuessPanel frame={f} start={1476} up={96} down={4} show={ease(f, 1462, 1480) * (1 - ease(f, 1695, 1712))} x={1150} y={672} /> : null}
      <Sparkles frame={f} start={1558} x={620} y={560} r={300} />

      {/* -------- S7 twist -------- */}
      {sameA > 0 ? (
        <div style={{ position: "absolute", left: 150, top: 230, width: ALBUM.w, height: ALBUM.h, transform: "scale(0.86)", transformOrigin: "0% 0%" }}>
          <Album frame={f} fps={fps} up={SAME_UP} down={SAME_DOWN} appear={sameAppear} show={sameA} />
        </div>
      ) : null}
      {twistCard > 0.001 ? (
        <div style={{ position: "absolute", left: 1010 + (1 - twistCard) * 900, top: 120, transform: `rotate(${6 - (1 - twistCard) * 8}deg)` }}>
          <PhotoCard src="up_05.jpg" size={400} style={{ position: "relative" }} />
          <NewTag s={pop(f, fps, 1910, 9) * 0.8} style={{ left: 270, top: -70 }} />
        </div>
      ) : null}

      {/* -------- S8 outro -------- */}
      {outroA > 0 ? (
        <>
          <Title text="Let's find out!" size={112} style={{ left: 0, right: 0, textAlign: "center", top: 70, opacity: outroA, transform: `translateY(${(1 - outroA) * -30}px)` }} />
          <PhotoCard src="hero_up.jpg" size={420} style={{ left: 150, top: 300 + Math.sin(f / 9) * 10, transform: `scale(${pop(f, fps, 2090, 10)}) rotate(-7deg)` }} />
          <PhotoCard src="hero_down.jpg" size={420} style={{ right: 150, top: 290 + Math.sin(f / 9 + 1.5) * 10, transform: `scale(${pop(f, fps, 2100, 10)}) rotate(7deg)` }} />
        </>
      ) : null}

      {/* -------- Robi (always) -------- */}
      <Robi
        x={rx}
        y={ry}
        size={rs * (0.4 + 0.6 * enter)}
        mood={mood}
        blink={blink}
        lookX={lookX}
        frame={f}
        progress={loadP}
        glitch={glitch}
        armL={armL}
        armR={armR}
        bob={bob}
        tilt={mood === "confused" ? -6 : mood === "question" ? -3 : 0}
        antenna={antenna}
        antennaOn={antennaOn}
        style={{ opacity: Math.min(1, enter * 1.4) }}
      />

      <StepTracker frame={f} active={active} show={trackerA} />
      <Captions frame={f} caps={CAPS} />
    </AbsoluteFill>
  );
};
