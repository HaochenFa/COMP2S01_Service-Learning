import { bundle } from "@remotion/bundler";
import { renderStill, selectComposition } from "@remotion/renderer";
import path from "node:path";
const out = process.argv[2];
const id = process.argv[3];
const frames = JSON.parse(process.argv[4]);
const scale = +(process.argv[5]||0.5);
const browserExecutable = "/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell";
const serveUrl = await bundle({ entryPoint: path.resolve("src/index.ts") });
const composition = await selectComposition({ serveUrl, id, browserExecutable });
for (const frame of frames) {
  await renderStill({ composition, serveUrl, frame, output: `${out}/${id}-${String(frame).padStart(4,'0')}.png`, browserExecutable, scale, imageFormat: "png" });
  console.log("ok", frame);
}
