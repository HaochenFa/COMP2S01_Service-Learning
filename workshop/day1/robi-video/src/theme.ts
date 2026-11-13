import { loadFont } from "@remotion/fonts";
import { Easing, interpolate, spring, staticFile } from "remotion";

export const C = {
  bg: "#F6F8FB",
  dark: "#1D2433",
  ink: "#1D2433",
  muted: "#5B6475",
  white: "#FFFFFF",
  blue: "#2563EB",
  blueT: "#E2EBFD",
  orange: "#C2410C",
  orangeT: "#FFE9DA",
  green: "#15803D",
  greenT: "#DCF3E3",
  purple: "#6D28D9",
  purpleT: "#EDE5FC",
  gold: "#FFD166",
  soft: "#C9D2E3",
};

export const FONT = "Nunito";

for (const w of ["400", "700", "800", "900"]) {
  loadFont({
    family: FONT,
    url: staticFile(`fonts/nunito-latin-${w}-normal.woff2`),
    weight: w,
  });
}

// Diverse skin tones and sleeve colours used across the video.
export const SKIN = ["#F7D3B0", "#E8B98A", "#C68642", "#8D5524", "#F1C27D", "#A86B3C", "#6B4226", "#FFE0C2"];
export const SLEEVE = [C.blue, C.orange, C.green, C.purple, "#0EA5E9", "#DB2777", "#CA8A04", "#475569"];

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const smooth = Easing.bezier(0.16, 1, 0.3, 1);

/** 0 -> 1 between two frames, eased. */
export const ease = (frame: number, start: number, end: number) =>
  interpolate(frame, [start, end], [0, 1], { ...clamp, easing: smooth });

/** Springy pop-in scale starting at `start`. */
export const pop = (frame: number, fps: number, start: number) =>
  spring({ frame: frame - start, fps, config: { damping: 12, stiffness: 140, mass: 0.6 } });

/** Fade in then (optionally) out. */
export const fadeInOut = (frame: number, inStart: number, outStart?: number) => {
  const a = ease(frame, inStart, inStart + 12);
  if (outStart === undefined) return a;
  return a * (1 - ease(frame, outStart, outStart + 12));
};
