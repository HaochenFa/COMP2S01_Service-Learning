import json, random, math
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
random.seed(11); np.random.seed(11)
N=720
def hexrgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def grad(c1,c2):
    a=np.linspace(0,1,N)[:,None,None]; c1=np.array(hexrgb(c1))[None,None,:]; c2=np.array(hexrgb(c2))[None,None,:]
    return np.repeat(c1*(1-a)+c2*a,N,axis=1)
def to_img(arr): return Image.fromarray(np.clip(arr,0,255).astype('uint8'),'RGB')
def blobs(img, shapes, blur):
    d=ImageDraw.Draw(img,'RGBA')
    for kind,box,col in shapes:
        if kind=='rect': d.rounded_rectangle(box,radius=12,fill=col)
        else: d.ellipse(box,fill=col)
    return img.filter(ImageFilter.GaussianBlur(blur))
def finish(img, grain=3.5, vig=0.22):
    a=np.asarray(img).astype(float)
    yy,xx=np.mgrid[0:N,0:N]; r=np.sqrt(((xx-N/2)/(N/2))**2+((yy-N/2)/(N/2))**2)
    a*= (1-vig*np.clip(r-0.35,0,1)**1.6)[:,:,None]
    a+=np.random.normal(0,grain,a.shape)
    return to_img(a)
def bg(kind):
    if kind=='window':
        img=to_img(grad('#dfe7ee','#c9d3dc'))
        img=blobs(img,[('rect',(40,30,330,300),(255,255,250,235)),('rect',(380,40,700,290),(250,252,255,200)),('rect',(-20,560,760,760),(150,120,95,255))],26)
    elif kind=='board':
        img=to_img(grad('#e9e2cf','#d8cfb8'))
        img=blobs(img,[('rect',(-30,40,760,380),(52,92,72,255)),('rect',(-30,380,760,400),(120,90,60,255))],22)
    elif kind=='paper':
        img=to_img(grad('#f7f6f2','#ecebe6'))
        img=img.filter(ImageFilter.GaussianBlur(2))
    elif kind=='shelf':
        img=to_img(grad('#efe2cc','#e2d1b6'))
        sh=[('rect',(-20,250,760,272),(110,80,55,255)),('rect',(-20,520,760,542),(110,80,55,255))]
        x=20
        while x<700:
            w=random.randint(24,60); h=random.randint(120,200); c=random.choice([(214,90,70),(70,120,190),(240,190,70),(90,160,110),(160,110,190),(230,230,220)])
            sh.append(('rect',(x,250-h,x+w,250),c+(255,))); x+=w+random.randint(4,14)
        img=blobs(img,sh,20)
    elif kind=='outdoor':
        img=to_img(grad('#bfe0f5','#e8f3f0'))
        sh=[('ellipse',(random.randint(-100,700),random.randint(250,650),0,0),None)]
        sh=[]
        for i in range(26):
            x=random.randint(-120,720); y=random.randint(260,700); r=random.randint(70,170)
            sh.append(('ellipse',(x,y,x+r,y+r),(random.randint(60,110),random.randint(130,175),random.randint(60,100),235)))
        img=blobs(img,sh,24)
    elif kind=='curtain':
        a=grad('#f5d9c8','#efcbb5'); xx=np.arange(N)[None,:,None]; a=a*(0.9+0.1*np.sin(xx/40.0))
        img=to_img(a).filter(ImageFilter.GaussianBlur(10))
    elif kind=='poster':
        img=to_img(grad('#dedfe3','#cdd0d6'))
        img=blobs(img,[('rect',(60,70,280,330),(250,120,90,255)),('rect',(420,120,640,300),(90,170,220,255)),('rect',(300,420,520,560),(250,205,90,255))],24)
    elif kind=='warm':
        img=to_img(grad('#f6c99a','#e9a978'))
        img=blobs(img,[('ellipse',(380,-80,820,360),(255,240,200,220)),('rect',(-20,600,760,760),(120,80,60,255))],30)
    elif kind=='teal':
        img=to_img(grad('#bfe3df','#a9d6d0'))
        img=blobs(img,[('rect',(500,80,690,520),(245,245,240,230))],24)
    return img
KINDS=['window','board','shelf','outdoor','curtain','poster','warm','teal']
box=json.load(open('out/set/handbox.json'))
def compose(src, kind, out, frac=0.64, dx=0, dy=0, grain=3.5, shadow=0.28):
    im=Image.open(src).convert('RGBA'); x0,y0,x1,y1=box[src]
    hh=max(y1-y0,(x1-x0)*0.95); s=frac*N/hh
    im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
    cx=(x0+x1)/2*s; cy=(y0+y1)/2*s
    ox=int(N/2+dx*N-cx); oy=int(N/2+dy*N-cy)
    b=bg(kind).convert('RGBA')
    # drop shadow
    sh=Image.new('RGBA',b.size,(0,0,0,0)); a=im.split()[3]
    shadowimg=Image.new('RGBA',im.size,(30,20,15,0)); shadowimg.putalpha(a.point(lambda v:int(v*shadow)))
    sh.alpha_composite(shadowimg,(ox+16,oy+22)); sh=sh.filter(ImageFilter.GaussianBlur(18))
    b.alpha_composite(sh)
    layer=Image.new('RGBA',b.size,(0,0,0,0)); layer.alpha_composite(im,(max(ox,0) if ox>=0 else 0, max(oy,0) if oy>=0 else 0), (0 if ox>=0 else -ox, 0 if oy>=0 else -oy))
    b.alpha_composite(layer)
    finish(b.convert('RGB'),grain=grain).save(out, quality=92)
good_up=['01','03','04','05','06','07','08','11','13','14','15']
good_down=['00','01','02','03','05','07','08','09','10','12','13','14','15']
manifest={'up':[],'down':[]}
for i,k in enumerate(good_up):
    kind=KINDS[i%len(KINDS)]; out=f'out/photos/up_{k}.jpg'
    compose(f'out/set/up_{k}.png',kind,out,frac=random.uniform(0.56,0.70),dx=random.uniform(-0.05,0.05),dy=random.uniform(-0.04,0.04)); manifest['up'].append(out)
for i,k in enumerate(good_down):
    kind=KINDS[(i+3)%len(KINDS)]; out=f'out/photos/down_{k}.jpg'
    compose(f'out/set/down_{k}.png',kind,out,frac=random.uniform(0.56,0.70),dx=random.uniform(-0.05,0.05),dy=random.uniform(-0.04,0.04)); manifest['down'].append(out)
compose('out/set/same_up.png','paper','out/photos/same_up.jpg',frac=0.66)
compose('out/set/same_down.png','paper','out/photos/same_down.jpg',frac=0.66)
compose('out/set/new_up.png','outdoor','out/photos/new_up.jpg',frac=0.64)
compose('out/set/new_down.png','window','out/photos/new_down.jpg',frac=0.64)
compose('out/set/side.png','poster','out/photos/side.jpg',frac=0.62)
compose('out/set/hero_up.png','teal','out/photos/hero_up.jpg',frac=0.66)
compose('out/set/hero_down.png','warm','out/photos/hero_down.jpg',frac=0.66)
json.dump(manifest,open('out/photos/manifest.json','w'),indent=1)
print('done')
