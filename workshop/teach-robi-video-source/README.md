# Taming AI · Day 1 intro video: "How does a computer learn?" (Teach Robi)

75-second video (1920×1080, 30 fps) for Stop 3 of Day 1. Made with Remotion (React).

## Edit and render
1. Install Node.js 18+ and run `npm install` in this folder.
2. Preview and edit in the browser: `npx remotion studio` (composition **TeachRobi**).
3. Render the silent video: `npx remotion render TeachRobi out/v2-silent.mp4 --muted`
4. Add sound: `ffmpeg -i out/v2-silent.mp4 -i audio/mix_voice_music_sfx.wav -map 0:v -map 1:a -c:v copy -c:a aac -shortest out/teach-robi.mp4`

## Where things are
- `src/v2/TeachRobi.tsx` – the whole timeline: captions (`CAPS`), Robi's path, moods and every scene. Change a caption by editing its text in `CAPS`.
- `src/v2/Robi.tsx`, `src/v2/Face.tsx` – Robi (3D-rendered body + animated screen face).
- `src/v2/Album.tsx`, `src/v2/Bits.tsx` – photo album, captions, step tracker, guess panel, stickers.
- `src/v2/Stills.tsx` – Robi sticker poses and the Teachable Machine diagram used in the slides.
- `public/v2/` – rendered hands (photos), Robi layers, fonts.
- `audio/` – `voiceover.json` (narration lines, voice and start frames), `voiceover.py` (records them with free Microsoft neural voices, needs `pip install edge-tts`), `synth.py` (sound effects) and `music_mix.py` (ukulele bed + cue list + voiceover → mixes). Run `python3 voiceover.py && python3 synth.py && python3 music_mix.py`. Keep the captions in `CAPS` in step with `voiceover.json`.
- `3d-pipeline/` – the Three.js pages that pose and render the 3D hands and Robi (`hand2.html`, `robi.html`) and the photo-card composer (`make_photos.py`).

## Credits
3D hand model: WebXR Input Profiles "generic-hand" (MIT, © Amazon). Icons: Phosphor Icons (MIT). Fonts: Fredoka, Lexend (SIL OFL). Robi, music and sound effects: original.
