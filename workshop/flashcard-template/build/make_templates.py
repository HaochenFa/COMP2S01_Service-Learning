from pathlib import Path
import json
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
OUT = ROOT / 'output'
OUT.mkdir(exist_ok=True)
FONT_DIR = Path(os.environ.get('WORKSHOP_FONT_DIR', str(Path.home() / 'Library/Fonts')))
pdfmetrics.registerFont(TTFont('Fredoka', str(FONT_DIR / 'Fredoka[wdth,wght].ttf')))
pdfmetrics.registerFont(TTFont('Lexend', str(FONT_DIR / 'Lexend[wght].ttf')))
W, H = 1024, 1536
CARD_W, CARD_H = 90*mm, 135*mm
INK = '#17213D'
MUTED = '#7F8998'
CATEGORIES = {
 'knowledge': ('ABOUT AI', '#6442A6'),
 'applications': ('AI CAN HELP', '#116FA6'),
 'ethics': ('WISE AI CHOICES', '#087B60'),
}
cards = []
for category, count in [('knowledge',3),('applications',3),('ethics',4)]:
 for _ in range(count): cards.append({'category':category, 'number':len(cards)+1})
cards += [
 {'category':'ethics','number':'A','sample':True,'title':['Keep it','private'],'sentence':['Keep your address','and passwords','private.'],'picture':'privacy_card.png'},
 {'category':'applications','number':'B','sample':True,'title':['AI can','explain'],'sentence':['Ask AI to explain','a word you do','not know.'],'picture':'robi_explains.png'},
]

def line(c, text, x, top, size, color=INK, font='Lexend', center=False):
 c.setFillColor(color)
 c.setFont(font, size)
 if center: c.drawCentredString(x, H-top-size*0.82, text)
 else: c.drawString(x, H-top-size*0.82, text)

def lines(c, contents, x, top, size, color=INK, font='Lexend', leading=None, center=False):
 leading=leading or size*1.18
 for n,t in enumerate(contents): line(c,t,x,top+n*leading,size,color,font,center)

def picture(c, name, x, top, width, height):
 path=ASSETS/name
 with Image.open(path) as im: iw,ih=im.size
 scale=min(width/iw,height/ih)
 dw,dh=iw*scale,ih*scale
 px=x+(width-dw)/2
 py=H-top-height+(height-dh)/2
 c.drawImage(ImageReader(str(path)),px,py,dw,dh,mask='auto')

def card(c, item, x, y, width=CARD_W, height=CARD_H):
 c.saveState()
 c.translate(x,y)
 c.scale(width/W,height/H)
 category=item['category']
 label,accent=CATEGORIES[category]
 c.drawImage(str(ASSETS/f'{category}-background.png'),0,0,W,H)
 line(c,label,94,92,47,accent,'Lexend')
 # Number identifies a slot; category wording also works without relying on colour.
 if item.get('sample'): line(c,'EXAMPLE',760,102,33,accent)
 else: line(c,f"{item['number']:02d}",865,95,45,accent)
 if item.get('sample'):
  lines(c,item['title'],96,205,108,INK,'Fredoka',leading=112)
  picture(c,item['picture'],135,475,750,540)
  lines(c,item['sentence'],96,1108,70,INK,'Lexend',leading=84)
 else:
  line(c,'Short title',96,214,91,INK,'Fredoka')
  line(c,'Maikling pamagat',99,333,43,MUTED)
  line(c,'Your picture',512,685,72,MUTED,'Fredoka',center=True)
  line(c,'Iyong larawan',512,778,45,MUTED,center=True)
  line(c,'One short sentence',96,1117,57,INK,'Fredoka')
  lines(c,['Isang maikling','pangungusap'],99,1197,43,MUTED,leading=54)
 line(c,'TAMING AI',205,1432,36,accent,'Lexend')
 c.restoreState()

single=OUT/'Taming_AI_Flashcard_Templates.pdf'
c=canvas.Canvas(str(single),pagesize=(CARD_W,CARD_H),pageCompression=1)
c.setTitle('Taming AI - editable flashcard templates and examples')
c.setAuthor('Taming AI workshop')
for item in cards:
 card(c,item,0,0)
 c.showPage()
c.save()

printed=OUT/'Taming_AI_Flashcards_A4_Print.pdf'
c=canvas.Canvas(str(printed),pagesize=A4,pageCompression=1)
c.setTitle('Taming AI - A4 flashcard print sheets')
c.setAuthor('Taming AI workshop')
page_w,page_h=A4
x_positions=[10*mm,110*mm]
y_positions=[page_h-8.5*mm-CARD_H,page_h-153.5*mm-CARD_H]
for page_start in range(0,len(cards),4):
 for local,item in enumerate(cards[page_start:page_start+4]):
  xx=x_positions[local%2]; yy=y_positions[local//2]
  card(c,item,xx,yy)
  # Trim guides stay outside the card, suitable for a normal office printer.
  c.setStrokeColorRGB(.68,.7,.73);c.setLineWidth(.35)
  for px,py,sx,sy in [(xx,yy,-1,-1),(xx+CARD_W,yy,1,-1),(xx,yy+CARD_H,-1,1),(xx+CARD_W,yy+CARD_H,1,1)]:
   c.line(px+sx*1.2*mm,py,px+sx*3.2*mm,py)
   c.line(px,py+sy*1.2*mm,px,py+sy*3.2*mm)
 c.setFont('Lexend',7);c.setFillColorRGB(.35,.39,.45)
 c.drawCentredString(page_w/2,2.6*mm,f'Taming AI  |  Print at 100% / Actual size  |  {page_start//4+1}/3')
 c.showPage()
c.save()

manifest={'card_size_mm':[90,135],'templates':10,'examples':2,'balance':{'knowledge':3,'applications':3,'ethics':4},'card_pdf':str(single),'a4_print_pdf':str(printed),'cards':cards}
(OUT/'template-manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({k:v for k,v in manifest.items() if k!='cards'},indent=2))
