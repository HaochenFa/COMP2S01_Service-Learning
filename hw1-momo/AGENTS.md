# Momo Learns to Munch

This is the Pair B project for Assignment 1. The [brief](HW1_Digital-Product-Dev.docx) asks for an interactive educational AI game for Grade 5–6 pupils aged 9–12. Another pair tests and extends the game. Keep earlier versions available for the before-and-after class presentation.

## Files and versions

- `momo-learns-to-munch/` contains the game. Keep it playable offline by double-clicking `index.html`. It uses plain HTML, CSS and JavaScript with local assets and has no build step.
- `meet-momo-video/` is the Remotion source for the intro video. Its render and poster go into `momo-learns-to-munch/media/` as `meet-momo.mp4` and `meet-momo.jpg`.
- `hw1-v0` marks the initial implementation and `hw1-v0.1` the picture-book redesign. Use these version names in project materials. The historically named `v1-screenshots/` at the root of the old tree shows v0.
- [README.md](README.md) maps the brief to the implementation. Preserve the start screen, instructions, multiple stages, scoring, feedback and hints for wrong guesses, increasing difficulty across at least three levels, and a final screen with feedback.

## Game commands

Run from `hw1-momo/`. Start the HTTP server only when browser automation needs HTTP.

```sh
open momo-learns-to-munch/index.html
node momo-learns-to-munch/tools/check-levels.js
python3 -m http.server 8765 --bind 127.0.0.1 --directory momo-learns-to-munch
```

- Use `index.html?level=2` or `?level=3` to jump to a level. For scripted play, `window.MomoGame` exposes `state`, `startLevel`, `showFinal`, `put`, `runTest` and `confetti`.
- Play the affected flow and inspect screenshots after behavioural or visual changes. Open `momo-learns-to-munch/tools/art-sheet.html` after editing `art.js`. Regenerate `img/grain.png` with `node momo-learns-to-munch/tools/make-grain.js`.
- Hard-reload or serve with `Cache-Control: no-store` if Chrome caches JavaScript and CSS during local testing.
- Preserve `preload="none"` and the poster on the intro video. A local server without Range support can delay the page's load event if the video preloads metadata. The video error handler closes the player and hides the “Meet Momo” button if the file is missing. In an automated browser without an audio device, set `video.muted = true` to check playback.

## Shared game and video code

- Keep the UMD wrappers in `momo-learns-to-munch/js/` apart from `game.js`. The browser uses classic scripts for `file://` play, and the level checker and Remotion asset preparation use CommonJS. `meet-momo-video/src/momo.ts` imports the same tokens and artwork.
- Preserve script order in `index.html`. The head loads `tokens.js` and copies colours into CSS variables. The remaining scripts load in the order `art.js`, `brain.js`, `levels.js`, `sound.js`, then `game.js`.
- `css/fonts.css` embeds the two font families as base64 WOFF2 data. When replacing a font file, update the matching `@font-face` data URL using `base64 -i fonts/<file>.woff2` from the game directory.
- Keep artwork and tokens in `art.js` and `tokens.js`. Use the existing brush-and-paper style with wobbly shapes, offset ink outlines, tapered strokes and flat lower-right shading. Use seeded `dice` or `snackSeed` for wobble so rerendering the same drawing does not flicker.
- Preserve SVG class hooks for animation in `css/game.css`, including `.momo-body`, `.momo-face`, `.momo-eyes`, `.momo-arm`, `.momo-sprout`, `.momo-shadow`, `.snack-art`, `.floaty`, `.waft` and `.mark`. The video supplies explicit poses through `momo(mood, size, { arms, sway, grow, look })` and `snack(data, mark, phase)`.
- Give `lettering()` and `words()` a unique `id` for each instance on a page because they generate SVG clip paths and masks. `ADVANCE` is measured for Bagel Fat One.
- The 116-unit snack box and 200-unit Momo box are shared by the CSS, `MOUTH` and `MOMO` in `game.js`, and `Snack` and `Momo` in the video’s `src/parts.tsx`.
- `sound.js` supplies Web Audio recipes and `talkPitches(text)` for Momo's chirps. The game plays the samples and the video asset script turns them into WAVs.

## Game behaviour and levels

- The game uses a 1280 × 720 stage scaled through `--scale`. `point()` converts pointer coordinates to stage units. `placeOf()` and `settle()` position snacks by their `where` value, and the tray resizes to `game.capacity`.
- Keep `stage.dataset.phase` in sync with the `intro`, `teach`, `testing` and `tested` phases because CSS uses it to switch between the tray and results. Preserve `game.token` checks in asynchronous sequences so starting another level cancels prior work.
- `guessOne()` shows Momo comparing snacks, picking the nearest example, and explaining the guess through `reason()`. Keep the player's role hands-on. Pupils teach with examples, watch Momo guess and fix the examples. Use short speech in Momo's own bubbles for this machine-learning lesson and keep the same approach in the video.
- `brain.js` uses 1-nearest-neighbour on weighted OKLab colour, size and spikiness. The model cannot consult the snack's true `yum` label during prediction. `helpful()` and `mixedUp()` power the hints.
- `levels.js` holds `tray`, `test`, and optional `later`, `stuck` and `box` data. `later` arrives after the first failed test. `box: 'lunchbox'` changes the first tray's presentation.
- The first level is winnable with an example on each plate. In level 2, the later examples make passing possible. In level 3, teaching with only blue yum and green yuck examples misclassifies green yum snacks until those examples arrive. Preserve the colour weighting that makes this work. After changing the levels, `WEIGHT` or snack colours, run `check-levels.js`. Levels with `later` should fail to meet the threshold with the first tray alone and score full marks with all examples.
- `PASS` is 75%. Stars use each level's best run with three for zero misses, two for one miss and one otherwise. Score is 10 points for each correct guess in the best run of each level. `mood()`, `watch()` and `growth()` control Momo's pose, gaze and sprout.

## Remotion video

Run from `meet-momo-video/`. The render script writes both the video and poster.

```sh
npm install
npm run assets
npm run dev
npm run lint
npm run render
npx remotion render MeetMomo out/frames --frames=30,400,1010 --image-format=png --scale=0.5
```

- Keep the continuous picnic-blanket shot. `src/story.ts` holds positions and frame timings in `BEAT`. Actors derive their state from the global frame. `src/MeetMomo.tsx` owns the camera, draw order and sounds. At zoom 1, `World` in `src/parts.tsx` shows 1280 × 720 stage units scaled to 1920 × 1080.
- Drive motion with `useCurrentFrame()` and `interpolate()`. The game's CSS animations do not render in Remotion.
- Keep dialogue in `src/lines.json`. Re-run `npm run assets` after changing dialogue, sound recipes, fonts or grain. It generates `public/audio`, `public/fonts` and `public/img`, including the `say-<key>.wav` files.
- For a broader preview without a full render, use `npx remotion render MeetMomo out/frames --sequence --every-nth-frame=15 --image-format=jpeg --scale=0.4`.
- Keep the shipped video near 12 MB with `Config.setCrf(24)` in `remotion.config.ts`. The `LOUD` scale keeps the audio peak below 0 dB. Check the mix with `ffmpeg -i <mp4> -af volumedetect -f null -`.
