# Math Meteor Defense

Assignment 1, Pair B, is an interactive educational game for Grade 5–6 pupils aged 9–12. The [assignment brief](../hw1-momo/HW1_Digital-Product-Dev.docx) sets the requirements. The live demo shows the original and improved versions side by side.

## Files and versions

- `math-meteor-defense.html` is V1.1. Keep HTML, CSS and JavaScript in the same file so it can run when double-clicked. Fredoka loads from Google Fonts and falls back to a system rounded font offline. Keep this as the sole external dependency.
- Leave `math-meteor-defense-mvp.html` intact for the before-and-after demo. Its best score uses the `mmd-best` key. The current game stores its settings and progress under `mmd2-`.
- [README.md](README.md) maps the brief to the implementation and records the changes from MVP to V1 to V1.1. Update that mapping and history when a change affects them. Check `presentation-script.docx` for stale steps or screenshots if the menu, hints or final screen change.
- V1 and V1.1 are preserved at `hw1-meteor-v1` and `hw1-meteor-v1.1`. Both tags use the former directory name `inclass1-math-meteor-defense/`. The `hw1-v*` tags belong to Momo.

## Requirements

- Preserve a clear start screen, instructions, multiple stages, scoring, wrong-answer hints, increasing difficulty across at least three stages, and a final screen with feedback.
- Teach one skill per wave with a worked example. Keep difficulty tied to the wave sequence and omit grade labels, developer dashboards and prompt tooling from the learner experience.
- Keep answers to whole numbers from 0 to 144. Use simple fractions, decimals (0.5, 0.1, 0.25) and percentages (10, 20, 25, 50, 75, 100).
- Point each hint at a specific meteor and help the pupil solve the problem. `countIn()` stops before the answer. Aim for roughly 50 characters per hint so the bubble fits its 270 px wrap width.
- Keep pupil-facing copy brief and friendly. Preserve the cartoon style with thick ink outlines, hard offset shadows, Fredoka and the existing palette.

## Implementation

- `WAVES` defines seven waves with weighted topics, a difficulty tier, count, speed, spawn timing and a pre-wave skill card. `waveInfo(i)` generates increasingly fast Meteor Storm waves after wave 7.
- `GEN[topic](tier)` covers `mult`, `div`, `frac`, `dec`, `pct` and `ops`. `P(q, a, hints, why, traps)` returns the question, answer, two hints, miss explanation and a map of common wrong answers. Times tables leave `why` empty. `P()` filters trap answers that are negative, fractional or equal to the correct answer.
- `game` holds the run. `showCard()` displays HTML cards in `#overlay` as the game goes from menu to skill intro, play, wave clear and game over. Play can pause through Esc or a hidden tab. The 700 ms delay on Enter handling prevents a play input from skipping the next card. Typing goes into the answer field with a four-digit limit. Touch screens use the on-screen keypad.
- `spawnMeteor()` tries up to 30 generated problems to avoid duplicate answers on screen and places the meteor where it has the most room. `m.p` is vertical progress and `m.fx` is horizontal position relative to `W`. At most five meteors are visible, or four below 500 px.
- `submit()` zaps the lowest meteor with the entered answer. For a wrong answer, `hintTarget()` prefers a matching trap, then an answer within 30%, then the lowest meteor. `giveHint()` shows a trap explanation or the next hint. Trap explanations preserve the hint sequence, and one meteor shows a hint at a time. `HINT_TIME` and `HINT_SLOW` control the slowdown.
- Each zap scores 10 points times a streak multiplier from ×1 to ×4, increasing after every five consecutive correct answers. A cleared wave awards 20 times the wave number, 50 more for a perfect wave, and one heart up to `MAX_HEARTS` (5). Gold meteors freeze time for four seconds after wave 1 unless they are the last meteor in a wave. A wave clears once its full count has spawned and all meteors are gone.
- `buildScene()` caches the sky and city in offscreen layers on resize. `render(t)` draws meteors between those layers, then the cannon, hints, effects and overlays. `update(dt)` advances the simulation. `tone()` synthesises sound through Web Audio.

## Verification

Run these commands from `hw1-math-meteor-defense/`:

```sh
open math-meteor-defense.html
python3 -m http.server 8766 --bind 127.0.0.1
```

Use the HTTP server for browser automation. Reload with a new query string if the browser is showing a cached copy. Play the affected flow and review screenshots. For changes to the layout or canvas, check both desktop and a phone viewport around 375 px wide.

- Wait for the `ResizeObserver` to set a nonzero `W` and `H` before spawning meteors in a script.
- For a background page with a paused animation loop, call `update(0.05)` and `updateFx(0.05)` repeatedly, then `render(performance.now() / 1000)`.
- To exercise feedback, set `answer.value`, call `submit()` and read `feedback.textContent`. Use an isolated browser profile or origin for scripted runs that change scores and unlocks. Clear the `mmd2-` keys on the test origin after use.

After changing `GEN`, run this in the game page's console. An empty array means the sampled problems passed.

```js
const invalidProblems = [];
for (const generate of Object.values(GEN)) {
  for (const tier of [0, 1, 2]) {
    for (let sample = 0; sample < 3000; sample++) {
      const problem = generate(tier);
      const strings = [problem.q, ...problem.hints, problem.why, ...Object.values(problem.traps)];
      if (
        !Number.isInteger(problem.a) || problem.a < 0 || problem.a > 144 ||
        problem.hints.length !== 2 || Object.hasOwn(problem.traps, problem.a) ||
        strings.some(value => typeof value !== 'string' || /undefined|NaN/.test(value))
      ) {
        invalidProblems.push(problem);
      }
    }
  }
}
console.log(invalidProblems);
```
