import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { PhotoCard } from "../components/Card";
import { Hand } from "../components/Hand";
import { Robot } from "../components/Robot";
import { Chip, Headline, Sub } from "../components/Text";
import { C, FONT, SKIN, SLEEVE, ease, fadeInOut, pop } from "../theme";

const abs = (x: number, y: number, extra: React.CSSProperties = {}): React.CSSProperties => ({
  position: "absolute",
  left: x,
  top: y,
  ...extra,
});

const slideUp = (frame: number, start: number) => ({
  opacity: ease(frame, start, start + 14),
  translate: `0px ${interpolate(ease(frame, start, start + 18), [0, 1], [40, 0])}px`,
});

/* 1. Title ------------------------------------------------------------ */
export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: C.dark }}>
      <div
        style={abs(140, 190, {
          ...slideUp(frame, 0),
          background: C.gold,
          color: C.dark,
          fontFamily: FONT,
          fontWeight: 900,
          fontSize: 40,
          padding: "12px 30px",
          borderRadius: 999,
          letterSpacing: 2,
        })}
      >
        TAMING AI · DAY 1
      </div>
      <div style={abs(140, 290, slideUp(frame, 8))}>
        <Headline size={116} color={C.white} style={{ whiteSpace: "nowrap" }}>
          How does a
          <br />
          computer learn?
        </Headline>
      </div>
      <div style={abs(140, 620, slideUp(frame, 40))}>
        <Sub size={68} color={C.gold}>
          Let's find out!
        </Sub>
      </div>
      <div
        style={abs(1230, 230, {
          scale: pop(frame, fps, 6),
          translate: `0px ${Math.sin(frame / 10) * 12}px`,
        })}
      >
        <Robot size={500} wave />
      </div>
    </AbsoluteFill>
  );
};

/* 2. Rules ------------------------------------------------------------ */
const Calculator: React.FC = () => (
  <div style={{ width: 440, height: 540, background: C.dark, borderRadius: 40, padding: 34, boxSizing: "border-box" }}>
    <div
      style={{
        height: 130,
        background: "#2B3447",
        borderRadius: 20,
        color: C.gold,
        fontFamily: FONT,
        fontWeight: 900,
        fontSize: 60,
        whiteSpace: "nowrap",
        display: "flex",
        alignItems: "center",
        justifyContent: "flex-end",
        paddingRight: 26,
      }}
    >
      2 + 2 = 4
    </div>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 18, marginTop: 30 }}>
      {Array.from({ length: 12 }).map((_, i) => (
        <div key={i} style={{ height: 82, borderRadius: 20, background: i % 4 === 3 ? C.orange : "#3A4560" }} />
      ))}
    </div>
  </div>
);

export const RulesScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const partA = 1 - ease(frame, 88, 102);
  const partB = ease(frame, 96, 112);
  return (
    <AbsoluteFill style={{ background: C.bg }}>
      <div style={{ opacity: partA }}>
        <div style={abs(140, 100, slideUp(frame, 0))}>
          <Headline>Some machines just follow rules.</Headline>
        </div>
        <div style={abs(180, 330, { scale: pop(frame, fps, 10) })}>
          <Calculator />
        </div>
        {["Same rule.", "Same answer.", "Every time."].map((t, i) => (
          <div key={t} style={abs(700, 400 + i * 120, slideUp(frame, 30 + i * 12))}>
            <Sub size={80} color={C.ink}>
              {t}
            </Sub>
          </div>
        ))}
      </div>
      <div style={{ opacity: partB }}>
        <div style={abs(140, 100)}>
          <Headline>But can you write a rule for this?</Headline>
        </div>
        <div style={abs(780, 330, { scale: pop(frame, fps, 104) })}>
          <Hand skin={SKIN[1]} sleeve={SLEEVE[0]} size={360} />
        </div>
        {[
          [560, 420],
          [1260, 360],
          [1320, 700],
        ].map(([x, y], i) => (
          <div
            key={i}
            style={abs(x, y, {
              scale: pop(frame, fps, 125 + i * 8),
              fontFamily: FONT,
              fontWeight: 900,
              fontSize: 150,
              color: C.orange,
            })}
          >
            ?
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/* 3. Different hands, how do YOU know ------------------------------------ */
const GRID = Array.from({ length: 12 }).map((_, i) => ({
  x: 160 + (i % 6) * 280,
  y: i < 6 ? 285 : 615,
  size: [170, 140, 190, 155, 180, 135][i % 6] + (i < 6 ? 0 : 10),
  rot: [-10, 8, -4, 12, -8, 5, 9, -12, 4, -6, 10, -3][i],
  left: i % 3 === 1,
  skin: SKIN[i % SKIN.length],
  sleeve: SLEEVE[(i * 3) % SLEEVE.length],
}));

export const HandsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const dim = interpolate(ease(frame, 228, 244), [0, 1], [1, 0.18]);
  return (
    <AbsoluteFill style={{ background: C.bg }}>
      <div style={abs(140, 90, { opacity: fadeInOut(frame, 0, 86) })}>
        <Headline size={84}>Hands are all different!</Headline>
      </div>
      <div style={abs(140, 90, { opacity: ease(frame, 94, 108) })}>
        <Headline size={84}>How do YOU know it's a thumbs up?</Headline>
      </div>
      {GRID.map((h, i) => (
        <div
          key={i}
          style={abs(h.x + (240 - h.size) / 2, h.y + (300 - h.size * 1.3) / 2, {
            scale: pop(frame, fps, 8 + i * 5),
            rotate: `${h.rot}deg`,
            opacity: dim,
          })}
        >
          <Hand skin={h.skin} sleeve={h.sleeve} left={h.left} size={h.size} />
        </div>
      ))}
      <div style={abs(140, 935, { opacity: fadeInOut(frame, 165, 226) })}>
        <Sub color={C.blue}>Because you have seen LOTS of examples!</Sub>
      </div>
      <div style={abs(810, 300, { scale: pop(frame, fps, 236) })}>
        <Hand skin={SKIN[5]} sleeve={SLEEVE[6]} left size={300} />
        <div
          style={abs(250, 20, {
            width: 120,
            height: 120,
            borderRadius: 999,
            background: C.green,
            color: C.white,
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 84,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            scale: pop(frame, fps, 250),
          })}
        >
          ✓
        </div>
      </div>
      <div style={abs(140, 935, { opacity: ease(frame, 246, 260) })}>
        <Sub color={C.green}>So you know a NEW one right away!</Sub>
      </div>
    </AbsoluteFill>
  );
};

/* 4. SHOW ---------------------------------------------------------------- */
const ROBOT_CENTER = { x: 1540, y: 600 };

export const ShowScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const cards = [0, 1, 2, 3, 4, 5].map((i) => ({
    down: i >= 3,
    x: 190 + (i % 3) * 200,
    y: i < 3 ? 400 : 690,
    skin: SKIN[(i * 2 + 1) % SKIN.length],
    sleeve: SLEEVE[(i + 2) % SLEEVE.length],
    left: i === 1 || i === 5,
  }));
  return (
    <AbsoluteFill style={{ background: C.bg }}>
      <div style={abs(140, 80, slideUp(frame, 0))}>
        <Chip n={1} label="SHOW" color={C.blue} />
      </div>
      <div style={abs(140, 200, slideUp(frame, 6))}>
        <Headline size={96}>
          Computers learn from <span style={{ color: C.blue }}>EXAMPLES</span>
        </Headline>
      </div>
      {[
        ["Thumbs up", C.blue, 345],
        ["Thumbs down", C.orange, 635],
      ].map(([label, color, y], i) => (
        <div
          key={label as string}
          style={abs(190, y as number, {
            opacity: ease(frame, 20 + i * 30, 34 + i * 30) * (1 - ease(frame, 150, 170)),
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 40,
            color: color as string,
          })}
        >
          {label}
        </div>
      ))}
      {cards.map((c, i) => {
        const fly = ease(frame, 150 + i * 6, 190 + i * 6);
        const x = interpolate(fly, [0, 1], [c.x, ROBOT_CENTER.x - 85]);
        const y = interpolate(fly, [0, 1], [c.y, ROBOT_CENTER.y - 100]);
        return (
          <PhotoCard
            key={i}
            skin={c.skin}
            sleeve={c.sleeve}
            down={c.down}
            left={c.left}
            style={{
              left: x,
              top: y,
              scale: pop(frame, fps, 26 + i * 8) * interpolate(fly, [0, 1], [1, 0.25]),
              opacity: 1 - ease(frame, 182 + i * 6, 194 + i * 6),
              rotate: `${[-4, 3, -2, 4, -3, 2][i]}deg`,
            }}
          />
        );
      })}
      <div style={abs(1340, 360, { scale: pop(frame, fps, 10) })}>
        <Robot size={400} mood={frame > 200 ? "happy" : "think"} />
      </div>
      <div style={abs(140, 945, { opacity: ease(frame, 205, 220) })}>
        <Sub color={C.ink}>We SHOW the computer lots of pictures.</Sub>
      </div>
    </AbsoluteFill>
  );
};

/* 5. TRAIN --------------------------------------------------------------- */
export const TrainScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const p = interpolate(frame, [20, 140], [0, 100], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const done = frame >= 142;
  return (
    <AbsoluteFill style={{ background: C.bg }}>
      <div style={abs(140, 80, slideUp(frame, 0))}>
        <Chip n={2} label="TRAIN" color={C.orange} />
      </div>
      <div style={abs(140, 200, slideUp(frame, 6))}>
        <Headline size={96}>It looks for patterns.</Headline>
      </div>
      <div style={abs(770, 330, { scale: pop(frame, fps, 4) })}>
        <Robot size={380} mood={done ? "happy" : "think"} />
      </div>
      {[0, 1, 2].map((i) => (
        <div
          key={i}
          style={abs(1230 + i * 60, 470, {
            width: 34,
            height: 34,
            borderRadius: 99,
            background: C.orange,
            opacity: done ? 0 : 0.35 + 0.65 * Math.max(0, Math.sin((frame - i * 6) / 6)),
          })}
        />
      ))}
      <div style={abs(410, 860, { width: 1100, height: 64, borderRadius: 99, background: C.orangeT, overflow: "hidden" })}>
        <div style={{ width: `${p}%`, height: "100%", background: done ? C.green : C.orange, borderRadius: 99 }} />
      </div>
      <div style={abs(410, 940, { width: 1100, textAlign: "center" })}>
        <Sub size={56} color={done ? C.green : C.orange}>
          {done ? "Done!" : `Training… ${Math.round(p)}%`}
        </Sub>
      </div>
    </AbsoluteFill>
  );
};

/* 6. TEST ---------------------------------------------------------------- */
const Bars: React.FC<{ up: number; down: number }> = ({ up, down }) => (
  <div style={{ width: 700, display: "flex", flexDirection: "column", gap: 44 }}>
    {[
      ["Thumbs up", up, C.blue, C.blueT],
      ["Thumbs down", down, C.orange, C.orangeT],
    ].map(([label, v, col, bg]) => (
      <div key={label as string}>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 52,
            color: col as string,
          }}
        >
          <span>{label}</span>
          <span>{Math.round(v as number)}%</span>
        </div>
        <div style={{ height: 56, borderRadius: 99, background: bg as string, marginTop: 12, overflow: "hidden" }}>
          <div style={{ width: `${v}%`, height: "100%", background: col as string, borderRadius: 99 }} />
        </div>
      </div>
    ))}
  </div>
);

export const TestScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const phase2 = frame >= 135;
  const a = ease(frame, 40, 90);
  const b = ease(frame, 150, 200);
  const up = phase2 ? interpolate(b, [0, 1], [96, 6]) : interpolate(a, [0, 1], [0, 96]);
  const down = phase2 ? interpolate(b, [0, 1], [4, 94]) : interpolate(a, [0, 1], [0, 4]);
  return (
    <AbsoluteFill style={{ background: C.bg }}>
      <div style={abs(140, 80, slideUp(frame, 0))}>
        <Chip n={3} label="TEST" color={C.green} />
      </div>
      <div style={abs(140, 200, slideUp(frame, 6))}>
        <Headline size={96}>Test with a NEW hand.</Headline>
      </div>
      <div style={abs(200, 360, { scale: phase2 ? pop(frame, fps, 138) : pop(frame, fps, 14) })}>
        {phase2 ? (
          <Hand skin={SKIN[0]} sleeve={SLEEVE[5]} down size={250} />
        ) : (
          <Hand skin={SKIN[3]} sleeve={SLEEVE[2]} left size={250} />
        )}
      </div>
      <div
        style={abs(150, 720, {
          width: 350,
          textAlign: "center",
          fontFamily: FONT,
          fontWeight: 900,
          fontSize: 44,
          color: C.white,
          background: C.purple,
          borderRadius: 99,
          padding: "10px 0",
          opacity: ease(frame, 24, 36),
        })}
      >
        NEW hand!
      </div>
      <div style={abs(590, 420, { scale: pop(frame, fps, 10) })}>
        <Robot size={280} mood={a < 1 && !phase2 ? "think" : b > 0 && b < 1 ? "think" : "happy"} />
      </div>
      <div style={abs(1040, 400, { opacity: ease(frame, 30, 44) })}>
        <Bars up={up} down={down} />
      </div>
      <div style={abs(140, 935, { opacity: fadeInOut(frame, 96, 132) })}>
        <Sub color={C.green}>It guessed right!</Sub>
      </div>
      <div style={abs(140, 935, { opacity: ease(frame, 206, 220) })}>
        <Sub color={C.green}>Right again!</Sub>
      </div>
    </AbsoluteFill>
  );
};

/* 7. DATA ---------------------------------------------------------------- */
export const DataScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: C.bg, alignItems: "center" }}>
      <div style={{ position: "absolute", top: 170, width: "100%", textAlign: "center", ...slideUp(frame, 0) }}>
        <Sub size={84} color={C.ink}>
          The examples are called
        </Sub>
      </div>
      <div
        style={{
          position: "absolute",
          top: 280,
          width: "100%",
          textAlign: "center",
          fontFamily: FONT,
          fontWeight: 900,
          fontSize: 300,
          color: C.blue,
          scale: pop(frame, fps, 22),
        }}
      >
        DATA
      </div>
      {Array.from({ length: 7 }).map((_, i) => (
        <PhotoCard
          key={i}
          skin={SKIN[(i + 2) % SKIN.length]}
          sleeve={SLEEVE[(i * 5) % SLEEVE.length]}
          down={i % 2 === 1}
          left={i % 3 === 0}
          w={150}
          style={{ left: 300 + i * 190, top: 760, scale: pop(frame, fps, 50 + i * 5), rotate: `${(i % 2 ? 1 : -1) * 4}deg` }}
        />
      ))}
    </AbsoluteFill>
  );
};

/* 8. Tease --------------------------------------------------------------- */
export const TeaseScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const slide = ease(frame, 118, 150);
  return (
    <AbsoluteFill style={{ background: C.bg }}>
      <div style={abs(140, 90, slideUp(frame, 0))}>
        <Headline size={96}>
          What if the DATA has only
          <br />
          <span style={{ color: C.purple }}>ONE kind of hand?</span>
        </Headline>
      </div>
      {Array.from({ length: 6 }).map((_, i) => (
        <PhotoCard
          key={i}
          skin={SKIN[1]}
          sleeve={SLEEVE[0]}
          down={i % 2 === 1}
          w={160}
          style={{ left: 150 + i * 195, top: 400, scale: pop(frame, fps, 24 + i * 6) }}
        />
      ))}
      <div
        style={abs(interpolate(slide, [0, 1], [-260, 860]), 640, {
          rotate: "-14deg",
          opacity: slide,
        })}
      >
        <Hand skin={SKIN[6]} sleeve={SLEEVE[5]} left size={165} />
      </div>
      <div style={abs(1430, 610, { scale: pop(frame, fps, 6) })}>
        <Robot size={290} mood={frame > 140 ? "confused" : "happy"} />
      </div>
      <div
        style={abs(1360, 470, {
          scale: pop(frame, fps, 150),
          fontFamily: FONT,
          fontWeight: 900,
          fontSize: 170,
          color: C.orange,
        })}
      >
        ?
      </div>
      <div style={abs(140, 900, { opacity: fadeInOut(frame, 158, 198) })}>
        <Sub size={72} color={C.ink}>
          Will it still guess right?
        </Sub>
      </div>
      <div style={abs(140, 900, { opacity: ease(frame, 204, 218) })}>
        <Sub size={72} color={C.purple}>
          Let's find out!
        </Sub>
      </div>
    </AbsoluteFill>
  );
};

/* 9. Outro --------------------------------------------------------------- */
export const OutroScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const bob = (o: number) => `0px ${Math.sin((frame + o) / 9) * 12}px`;
  return (
    <AbsoluteFill style={{ background: C.dark }}>
      <div style={{ position: "absolute", top: 150, width: "100%", textAlign: "center", ...slideUp(frame, 0) }}>
        <Headline size={124} color={C.white}>
          Now YOU are the teacher!
        </Headline>
      </div>
      <div style={{ position: "absolute", top: 330, width: "100%", textAlign: "center", ...slideUp(frame, 16) }}>
        <Sub size={68} color={C.gold}>
          Let's teach a computer:
          <br />
          thumbs up or thumbs down?
        </Sub>
      </div>
      <div style={abs(430, 560, { scale: pop(frame, fps, 34), translate: bob(0) })}>
        <Hand skin={SKIN[2]} sleeve={SLEEVE[0]} size={230} />
      </div>
      <div style={abs(810, 540, { scale: pop(frame, fps, 26) })}>
        <Robot size={300} wave />
      </div>
      <div style={abs(1250, 560, { scale: pop(frame, fps, 42), translate: bob(20) })}>
        <Hand skin={SKIN[4]} sleeve={SLEEVE[1]} down left size={230} />
      </div>
    </AbsoluteFill>
  );
};
