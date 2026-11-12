import numpy as np, wave, json, sys
SR=48000
rng=np.random.default_rng(3)
def env(n,a=0.005,d=None,curve=6.0):
    t=np.arange(n)/SR; e=np.minimum(1,t/max(a,1e-4))
    if d: e*=np.exp(-curve*t/d)
    return e
def sine(f,dur,phase=0):
    t=np.arange(int(dur*SR))/SR
    if callable(f): ph=2*np.pi*np.cumsum(f(t))/SR
    else: ph=2*np.pi*f*t
    return np.sin(ph+phase)
def lowpass(x,cut):
    a=np.exp(-2*np.pi*cut/SR); y=np.zeros_like(x); acc=0.0
    for i in range(len(x)): acc=(1-a)*x[i]+a*acc; y[i]=acc
    return y
def lp_fast(x,cut):
    # one-pole via lfilter-like vectorization using scipy if present
    try:
        from scipy.signal import lfilter
        a=np.exp(-2*np.pi*cut/SR); return lfilter([1-a],[1,-a],x)
    except Exception: return lowpass(x,cut)
def hp_fast(x,cut): return x-lp_fast(x,cut)
def bp(x,lo,hi): return hp_fast(lp_fast(x,hi),lo)
def bell(f,dur=1.2,amp=1.0):
    n=int(dur*SR); t=np.arange(n)/SR; y=np.zeros(n)
    for r,a,d in [(1,1,dur),(2.0,0.35,dur*0.6),(3.0,0.18,dur*0.35),(4.2,0.12,dur*0.25),(5.4,0.08,dur*0.18)]:
        y+=a*np.sin(2*np.pi*f*r*t)*np.exp(-t*4.5/d)
    return amp*y*env(n,0.002)
def ks(f,dur,amp=1.0,bright=0.5):
    n=int(dur*SR); N=int(SR/f); buf=rng.uniform(-1,1,N); buf=lp_fast(buf, 1500+6000*bright)
    out=np.zeros(n); idx=0
    for i in range(n):
        out[i]=buf[idx]; nxt=(idx+1)%N; buf[idx]=0.996*0.5*(buf[idx]+buf[nxt]); idx=nxt
    return amp*out
SFX={}
n=int(0.11*SR); t=np.arange(n)/SR
SFX['pop']=0.8*np.sin(2*np.pi*np.cumsum(700-3800*t)/SR)*np.exp(-t*38)+0.25*rng.normal(0,1,n)*np.exp(-t*400)
SFX['tick']=0.35*sine(1500,0.03)*env(int(0.03*SR),0.001,0.03)+0.15*sine(2600,0.03)*env(int(0.03*SR),0.001,0.02)
nn=int(0.07*SR); SFX['card']=0.45*bp(rng.normal(0,1,nn),1800,6000)*env(nn,0.002,0.05)+0.2*np.pad(SFX['tick'],(0,nn-len(SFX['tick'])))
nw=int(0.5*SR); tw=np.arange(nw)/SR; noise=rng.normal(0,1,nw)
sweep=np.concatenate([bp(noise[i:i+2400],300+3000*np.sin(np.pi*i/nw)**2,800+5000*np.sin(np.pi*i/nw)**2) for i in range(0,nw,2400)])[:nw]
SFX['whoosh']=0.55*sweep*np.sin(np.pi*tw/0.5)**1.5
ch=np.zeros(int(1.8*SR))
for i,fq in enumerate([1046.5,1318.5,1568,2093]):
    b=bell(fq,1.3,0.45); s=int(i*0.085*SR); ch[s:s+len(b)]+=b[:len(ch)-s]
SFX['chime']=ch
SFX['ding']=bell(1318.5,1.4,0.7)+np.pad(bell(1975.5,1.0,0.25),(0,int(1.4*SR)-int(1.0*SR)))
def blip(f,d=0.07):
    x=np.sign(sine(f,d))*0.35+sine(f,d)*0.65; return lp_fast(x,3500)*env(len(x),0.004,d*1.5,3)
SFX['blip']=np.concatenate([blip(660),np.zeros(int(0.03*SR)),blip(990)])*0.6
SFX['question']=0.5*lp_fast(np.sign(sine(lambda tt:480+520*(tt/0.28)**1.5,0.28))*0.3+sine(lambda tt:480+520*(tt/0.28)**1.5,0.28),3000)*env(int(0.28*SR),0.01,0.4,2)
pr=np.zeros(int(1.45*SR))
for k in range(11):
    fq=rng.choice([523,659,784,880,1046,1175]); b=blip(fq,0.045)*0.35; s=int(k*0.125*SR); pr[s:s+len(b)]+=b
SFX['processing']=pr
sp=np.zeros(int(0.7*SR))
for k in range(9):
    fq=rng.uniform(2400,4200); b=0.18*sine(fq,0.25)*env(int(0.25*SR),0.001,0.18); s=int(k*0.04*SR); sp[s:s+len(b)]+=b
SFX['sparkle']=sp
ns=int(0.35*SR); ts=np.arange(ns)/SR
SFX['stamp']=0.9*np.sin(2*np.pi*np.cumsum(160-200*ts)/SR)*np.exp(-ts*14)+0.25*lp_fast(rng.normal(0,1,ns),2500)*np.exp(-ts*30)
ng=int(0.4*SR); g=np.sign(rng.normal(0,1,ng))*0.3; g=np.repeat(g[::60],60)[:ng]
gate=(np.floor(np.arange(ng)/(SR*0.03))%2==0)
SFX['glitch']=lp_fast(g*gate,4000)*0.5*env(ng,0.002,0.4,2)
u1=sine(lambda tt:523+12*np.sin(2*np.pi*7*tt),0.18)*env(int(0.18*SR),0.01,0.25,2); u2=sine(lambda tt:392+12*np.sin(2*np.pi*7*tt),0.32)*env(int(0.32*SR),0.01,0.4,3)
SFX['uhoh']=0.35*np.concatenate([u1,np.zeros(int(0.04*SR)),u2])
nr=int(0.7*SR); SFX['rise']=0.22*sine(lambda tt:420+700*(tt/0.7)**1.2,0.7)*np.sin(np.pi*np.arange(nr)/nr)
nh=int(1.6*SR); th=np.arange(nh)/SR
SFX['hmm']=0.28*(sine(196,1.6)+0.5*sine(233.1,1.6)+0.3*sine(293.7,1.6))*np.sin(np.pi*th/1.6)**2
ff=np.zeros(int(2.4*SR))
for i,fq in enumerate([523.25,659.25,783.99,1046.5]):
    p=ks(fq,1.6,0.55,0.7); s=int(i*0.09*SR); ff[s:s+len(p)]+=p
for fq in [523.25,659.25,783.99]:
    p=ks(fq,2.0,0.35,0.6); s=int(0.45*SR); ff[s:s+len(p)]+=p[:len(ff)-s]
_b=np.pad(bell(2093,1.2,0.25),(int(0.42*SR),0)); _b=np.pad(_b,(0,max(0,len(ff)-len(_b))))[:len(ff)]; SFX['fanfare']=ff+_b
for k,v in SFX.items():
    v=v/ max(1e-6,np.max(np.abs(v)))*0.9; SFX[k]=v.astype(np.float32)
np.savez('sfx.npz',**SFX)
print('sfx',list(SFX.keys()))
