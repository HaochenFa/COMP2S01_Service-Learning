import numpy as np, wave, json
from scipy.signal import lfilter
SR=48000; FPS=30; TOTAL=2250; DUR=TOTAL/FPS
rng=np.random.default_rng(5)
def lp(x,c): a=np.exp(-2*np.pi*c/SR); return lfilter([1-a],[1,-a],x)
def hp(x,c): return x-lp(x,c)
def ks(f,dur,bright=0.55,decay=0.9965):
    n=int(dur*SR); N=int(round(SR/f)); buf=lp(rng.uniform(-1,1,N),1200+5000*bright)
    out=np.empty(n); idx=0
    for i in range(n):
        v=buf[idx]; out[i]=v; nx=idx+1 if idx+1<N else 0; buf[idx]=decay*0.5*(v+buf[nx]); idx=nx
    return out*np.minimum(1,np.arange(n)/(0.002*SR))
CH={'C':[392,261.63,329.63,523.25],'G':[392,293.66,392,493.88],'Am':[440,261.63,329.63,440],'F':[440,261.63,349.23,440]}
cache={}
def pluck(f):
    k=round(f,2)
    if k not in cache: cache[k]=ks(f,1.6)
    return cache[k]
mus=np.zeros(int(DUR*SR)+SR*3)
def add(buf,x,t,g):
    s=int(t*SR); e=min(len(buf),s+len(x)); buf[s:e]+=g*x[:e-s]
BPM=100; beat=60/BPM; bar=4*beat; e8=beat/2
def strum(chord,t,down=True,g=0.5):
    notes=CH[chord] if down else CH[chord][::-1]
    for i,f in enumerate(notes): add(mus,pluck(f),t+i*0.012,g*(1.0 if down else 0.6))
def bass(f,t,g=0.5,d=0.5):
    n=int(d*SR); tt=np.arange(n)/SR; x=(np.sin(2*np.pi*f*tt)+0.35*np.sin(4*np.pi*f*tt))*np.exp(-tt*5)*np.minimum(1,tt/0.008); add(mus,x,t,g)
def shaker(t,g=0.08):
    n=int(0.05*SR); x=hp(rng.normal(0,1,n),5500)*np.exp(-np.arange(n)/SR*90); add(mus,x,t,g)
def pad(chord,t,d,g=0.12):
    n=int(d*SR); tt=np.arange(n)/SR; x=np.zeros(n)
    for f in CH[chord]: x+=np.sin(2*np.pi*f/2*tt)+0.3*np.sin(2*np.pi*f*tt)
    x*=np.sin(np.pi*np.clip(tt/d,0,1))**2; add(mus,lp(x,1200),t,g)
BASSF={'C':130.81,'G':98.0,'Am':110.0,'F':87.31}
prog=['C','G','Am','F']
t=0.0; T1=1695/FPS; T2=2070/FPS
pattern=[(0,True),(2,True),(3,False),(5,False),(6,True),(7,False)]
bi=0
while t<T1-0.01:
    c=prog[bi%4]
    for pos,dn in pattern:
        tt=t+pos*e8
        if tt<T1: strum(c,tt,dn,0.42)
    bass(BASSF[c],t,0.55); bass(BASSF[c],t+2*beat,0.45)
    for k in range(8):
        if t+k*e8<T1: shaker(t+k*e8,0.07 if k%2 else 0.04)
    t+=bar; bi+=1
# tension section
t=T1; tp=['Am','F','Am','F','Am','F']; k=0
while t<T2-0.01:
    c=tp[k%len(tp)]; pad(c,t,bar*1.05,0.10)
    for q in range(4):
        if t+q*beat<T2: bass(BASSF[c],t+q*beat,0.32,0.35)
    t+=bar; k+=1
# outro
t=T2; for_chords=['C','G','C']
for i,c in enumerate(for_chords):
    if i<2:
        for pos,dn in pattern: strum(c,t+pos*e8,dn,0.45)
        bass(BASSF[c],t,0.55); bass(BASSF[c],t+2*beat,0.45)
    else:
        strum(c,t,True,0.6); bass(BASSF[c],t,0.6,1.5)
    t+=bar
mus=mus[:int(DUR*SR)]
fade=np.ones_like(mus); fi=int(1.0*SR); fade[:fi]=np.linspace(0,1,fi); fo=int(1.5*SR); fade[-fo:]=np.linspace(1,0,fo)
mus*=fade; mus=lp(mus,7000)
mus=mus/np.max(np.abs(mus))*0.16
# ---- SFX cues ----
S=dict(np.load('sfx.npz'))
G={'pop':0.45,'tick':0.22,'card':0.30,'whoosh':0.32,'chime':0.42,'ding':0.48,'blip':0.30,'question':0.34,'processing':0.26,'sparkle':0.30,'stamp':0.55,'glitch':0.30,'uhoh':0.30,'rise':0.30,'hmm':0.40,'fanfare':0.50}
cues=[(8,'chime'),(18,'pop'),(42,'blip'),(140,'whoosh'),(256,'whoosh'),(290,'question'),(366,'uhoh'),(430,'whoosh')]
cues+=[(446+i*4,'tick') for i in range(12)]
cues+=[(645,'whoosh'),(652,'blip')]
cues+=[(692+i*11,'card') for i in range(18)]
cues+=[(886,'stamp'),(889,'sparkle'),(1050,'blip'),(1104,'processing'),(1148,'processing'),(1192,'processing'),(1244,'ding')]
cues+=[(1246+i*3,'tick') for i in range(18)]
cues+=[(1365,'blip'),(1384,'whoosh'),(1404,'pop'),(1420,'processing'),(1476,'rise'),(1556,'ding'),(1559,'sparkle'),(1696,'whoosh'),(1712,'hmm')]
cues+=[(1722+i*4,'tick') for i in range(18)]
cues+=[(1892,'whoosh'),(1900,'glitch'),(1910,'pop'),(1962,'question'),(2072,'whoosh'),(2086,'fanfare'),(2090,'pop'),(2100,'pop')]
sfx=np.zeros(int(DUR*SR)+SR*3)
for fr,name in cues:
    x=S[name]; add(sfx,x,fr/FPS,G[name])
sfx=sfx[:int(DUR*SR)]
json.dump(cues,open('cues.json','w'))
def write(name,mono_mix):
    st=np.stack([mono_mix,mono_mix],axis=1)
    # small stereo width: delay right channel slightly for music only handled outside
    st=st/max(1e-6,np.max(np.abs(st)))*0.89
    pcm=(st*32767).astype(np.int16)
    with wave.open(name,'wb') as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
write('mix_music_sfx.wav', mus+sfx)
write('mix_sfx_only.wav', sfx*0.9)
# ---- voiceover, with music and SFX ducked under it ----
vo=np.zeros(len(sfx)); duck=np.zeros(len(sfx))
for line in json.load(open('voiceover.json'))['lines']:
    with wave.open(f"vo/{line['id']}.wav") as w: x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16)/32768
    s=int(line['frame']/FPS*SR); e=min(len(vo),s+len(x)); vo[s:e]+=x[:e-s]
    duck[max(0,s-int(0.15*SR)):e+int(0.15*SR)]=1
duck=np.clip(lp(duck,6),0,1); vo=vo/np.max(np.abs(vo))*0.8
write('mix_voice_music_sfx.wav', vo+mus*(1-0.6*duck)+sfx*(1-0.5*duck))
print('ok', len(cues), 'cues', DUR, 's')
