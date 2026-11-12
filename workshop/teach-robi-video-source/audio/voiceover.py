import asyncio, json, os, subprocess, wave
import edge_tts
FPS=30
cfg=json.load(open('voiceover.json'))
os.makedirs('vo',exist_ok=True)
async def say(line):
    mp3=f"vo/{line['id']}.mp3"; wav=f"vo/{line['id']}.wav"
    await edge_tts.Communicate(line['text'],cfg['voice'],rate=cfg['rate']).save(mp3)
    subprocess.run(['ffmpeg','-v','error','-y','-i',mp3,'-ar','48000','-ac','1',wav],check=True)
    os.remove(mp3)
async def main():
    for line in cfg['lines']: await say(line)
asyncio.run(main())
lines=cfg['lines']
for i,line in enumerate(lines):
    with wave.open(f"vo/{line['id']}.wav") as w: frames=w.getnframes()/w.getframerate()*FPS
    next_frame=lines[i+1]['frame'] if i+1<len(lines) else 2250
    print(f"{line['id']:9} start {line['frame']:5} ends {line['frame']+frames:7.0f}  room {next_frame-line['frame']-frames:6.0f}")
