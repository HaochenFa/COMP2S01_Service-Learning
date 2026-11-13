import React from "react";
import { HEAD, T, ease, map, pop } from "./theme";
import { ClassChip, Icon, PhotoCard } from "./Bits";

export type AlbumProps = {
  frame: number;
  fps: number;
  up: string[]; // 9 photos for left page
  down: string[]; // 9 photos for right page
  appear: number[]; // frame each card appears (index 0..17, alternating up/down)
  show: number; // 0..1 album visibility
  flips?: number[]; // frames when a page flip starts
  scan?: [number, number]; // [start frame, frames per card]
  arrows?: number; // frame arrows start appearing (pattern)
  total?: number; // photos per class (for the counter)
  sameNote?: boolean;
  dim?: number;
};

export const ALBUM = { w: 1240, h: 660 };
const PAGE_W = 600;
const CARD = 158;
const GAP = 22;

export const Album: React.FC<AlbumProps> = ({ frame, fps, up, down, appear, show, flips = [], scan, arrows, total = 30, sameNote, dim = 0 }) => {
  const page = (side: "up" | "down") => {
    const left = side === "up" ? 0 : ALBUM.w - PAGE_W;
    const photos = side === "up" ? up : down;
    const shown = appear.filter((a, i) => (side === "up" ? i % 2 === 0 : i % 2 === 1) && frame >= a).length;
    const count = Math.min(total, Math.round((shown / 9) * total));
    const gx = (PAGE_W - (3 * CARD + 2 * GAP)) / 2;
    return (
      <div style={{ position: "absolute", left, top: 0, width: PAGE_W, height: ALBUM.h, background: "#FFFDF7", borderRadius: side === "up" ? "28px 8px 8px 28px" : "8px 28px 28px 8px", boxShadow: "0 18px 40px rgba(80,60,30,0.18), inset 0 0 0 2px #EFE5D2", overflow: "visible" }}>
        <div style={{ position: "absolute", inset: 0, borderRadius: "inherit", backgroundImage: "linear-gradient(#F3EADA 2px, transparent 2px)", backgroundSize: "100% 46px", opacity: 0.5 }} />
        <ClassChip kind={side} text={side === "up" ? "Thumbs up" : "Thumbs down"} size={34} style={{ left: 22, top: 20 }} />
        <div style={{ position: "absolute", right: 24, top: 26, display: "flex", alignItems: "center", gap: 8, fontFamily: HEAD, fontWeight: 600, fontSize: 32, color: T.inkSoft }}>
          <Icon name="stack" size={34} color={side === "up" ? T.up : T.down} />
          {count} photos
        </div>
        {photos.slice(0, 9).map((src, i) => {
          const idx = side === "up" ? i * 2 : i * 2 + 1;
          const a = appear[idx] ?? 0;
          const p = pop(frame, fps, a, 13);
          if (frame < a) return null;
          const r = ((i * 37) % 9) - 4;
          const col = i % 3;
          const row = Math.floor(i / 3);
          const x = gx + col * (CARD + GAP);
          const y = 96 + row * (CARD + GAP);
          const fly = 1 - ease(frame, a, a + 14);
          const fx = (side === "up" ? -380 : 380) * fly;
          const arr = arrows !== undefined ? pop(frame, fps, arrows + i * 3 + (side === "down" ? 2 : 0), 12) : 0;
          const order = side === "up" ? i * 2 : i * 2 + 1;
          const sc = scan ? (frame - scan[0]) / scan[1] - order : -99;
          const cur = sc >= 0 && sc < 1.6 ? Math.sin(Math.min(1, sc / 1.6) * Math.PI) : 0;
          return (
            <React.Fragment key={i}>
              {cur > 0.01 ? <div style={{ position: "absolute", left: x - 10, top: y - 10, width: CARD + 20, height: CARD + 20, borderRadius: 20, background: "rgba(70,240,211,0.25)", boxShadow: `0 0 ${30 * cur}px rgba(70,240,211,${0.9 * cur})`, border: `5px solid rgba(25,181,161,${cur})`, transform: `scale(${1 + 0.06 * cur})` }} /> : null}
              <PhotoCard src={src} size={CARD} dim={dim} style={{ left: x + fx, top: y - fly * 60, transform: `rotate(${r * (0.4 + fly) * (1 - cur)}deg) scale(${(0.6 + 0.4 * p) * (1 + 0.06 * cur)})` }} />
              {arrows !== undefined && arr > 0.01 ? (
                <div style={{ position: "absolute", left: x + CARD - 46, top: y - 14, width: 62, height: 62, borderRadius: 99, background: side === "up" ? T.up : T.down, border: "4px solid #fff", display: "flex", alignItems: "center", justifyContent: "center", transform: `scale(${arr})`, boxShadow: "0 6px 14px rgba(0,0,0,0.18)" }}>
                  <Icon name={side === "up" ? "arrowUp" : "arrowDown"} size={38} color="#fff" />
                </div>
              ) : null}
            </React.Fragment>
          );
        })}
      </div>
    );
  };
  return (
    <div style={{ position: "absolute", width: ALBUM.w, height: ALBUM.h, opacity: show }}>
      {page("up")}
      {page("down")}
      {/* spiral spine */}
      {Array.from({ length: 9 }).map((_, i) => (
        <div key={i} style={{ position: "absolute", left: ALBUM.w / 2 - 28, top: 40 + i * 70, width: 56, height: 22, borderRadius: 12, border: "6px solid #B9AE9B", background: "transparent", boxSizing: "border-box" }} />
      ))}
      {/* page flips (training) */}
      {flips.map((f0, i) => {
        const t = map(frame, f0, f0 + 26, 0, 1);
        if (frame < f0 || frame > f0 + 27) return null;
        const ang = -180 * t;
        const shade = Math.abs(Math.sin(t * Math.PI));
        return (
          <div key={i} style={{ position: "absolute", left: ALBUM.w - PAGE_W, top: 0, width: PAGE_W, height: ALBUM.h, perspective: 2200, perspectiveOrigin: "0% 50%" }}>
            <div style={{ position: "absolute", inset: 0, transformOrigin: `${-(ALBUM.w - 2 * PAGE_W) / 2}px 50%`, transform: `rotateY(${ang}deg)`, background: "#FFFDF7", borderRadius: 10, boxShadow: `0 10px 30px rgba(0,0,0,${0.12 + 0.2 * shade})` }}>
              <div style={{ position: "absolute", inset: 0, background: `linear-gradient(90deg, rgba(0,0,0,${0.18 * shade}), rgba(0,0,0,0))`, borderRadius: 10 }} />
              <div style={{ position: "absolute", left: 40, top: 100, right: 40, bottom: 40, display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 20, opacity: 0.55 }}>
                {Array.from({ length: 9 }).map((_, k) => (
                  <div key={k} style={{ background: k % 2 ? T.downSoft : T.upSoft, borderRadius: 10 }} />
                ))}
              </div>
            </div>
          </div>
        );
      })}
      {sameNote ? null : null}
    </div>
  );
};
