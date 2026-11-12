import { bundle } from "@remotion/bundler";
import { renderStill, selectComposition } from "@remotion/renderer";
import path from "node:path";
import fs from "node:fs";
const outDir = process.argv[2];
const jobs = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
const browserExecutable = "/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell";
const serveUrl = await bundle({ entryPoint: path.resolve("src/index.ts") });
for (const j of jobs) {
  const composition = await selectComposition({ serveUrl, id: j.id, inputProps: j.props || {}, browserExecutable });
  await renderStill({ composition, serveUrl, frame: 0, output: `${outDir}/${j.name}.png`, inputProps: j.props || {}, browserExecutable, imageFormat: "png", scale: j.scale || 1 });
  console.log("ok", j.name);
}
