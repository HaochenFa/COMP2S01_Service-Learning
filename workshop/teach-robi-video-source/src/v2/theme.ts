import { loadFont } from "@remotion/fonts";
import { Easing, interpolate, spring, staticFile } from "remotion";

// "Robi's Lab" palette — shared with the slide deck.
export const T = {
  paper: "#FFF7EA",
  paperDot: "#EADFC9",
  ink: "#1C2440",
  inkSoft: "#4B5470",
  navy: "#17213D",
  up: "#2F6BFF",
  upSoft: "#E4ECFF",
  down: "#F2543D",
  downSoft: "#FFE5DF",
  yellow: "#FFC83A",
  yellowSoft: "#FFF1C7",
  teal: "#19B5A1",
  tealGlow: "#46F0D3",
  purple: "#7B4DFF",
  purpleSoft: "#EEE6FF",
  white: "#FFFFFF",
  green: "#1FA463",
};

export const HEAD = "Fredoka";
export const BODY = "Lexend";

const fonts: [string, string, string][] = [
  [HEAD, "500", "fredoka-latin-500-normal.woff2"],
  [HEAD, "600", "fredoka-latin-600-normal.woff2"],
  [HEAD, "700", "fredoka-latin-700-normal.woff2"],
  [BODY, "400", "lexend-latin-400-normal.woff2"],
  [BODY, "500", "lexend-latin-500-normal.woff2"],
  [BODY, "600", "lexend-latin-600-normal.woff2"],
];
for (const [family, weight, file] of fonts) {
  loadFont({ family, weight, url: staticFile(`v2/fonts/${file}`) });
}

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
export const smooth = Easing.bezier(0.22, 1, 0.36, 1);
export const inOut = Easing.bezier(0.65, 0, 0.35, 1);

/** 0→1 between two frames, eased. */
export const ease = (f: number, a: number, b: number, e = smooth) => interpolate(f, [a, b], [0, 1], { ...clamp, easing: e });
/** value mapping with clamp */
export const map = (f: number, a: number, b: number, from: number, to: number, e = smooth) =>
  interpolate(f, [a, b], [from, to], { ...clamp, easing: e });
/** bouncy pop 0→1 */
export const pop = (f: number, fps: number, start: number, damping = 11) =>
  spring({ frame: f - start, fps, config: { damping, stiffness: 160, mass: 0.7 } });
/** soft spring without overshoot */
export const glide = (f: number, fps: number, start: number) =>
  spring({ frame: f - start, fps, config: { damping: 22, stiffness: 120, mass: 0.9 } });
/** fade in at a, out at b (optional) */
export const vis = (f: number, a: number, b?: number, len = 10) => {
  const i = ease(f, a, a + len);
  return b === undefined ? i : i * (1 - ease(f, b, b + len));
};
