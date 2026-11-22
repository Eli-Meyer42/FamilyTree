"""Regenerate the app icons: python3 make-icons.py"""
import math
from PIL import Image, ImageDraw, ImageFilter
BG=(11,8,7,255); GOLD=(216,183,106,255); GOLD2=(243,220,156,255); BRONZE=(138,109,59,255)
HUES=[(224,170,70),(70,140,214),(200,90,110),(90,180,120),(170,110,220)]
def icon(size, maskable=False):
    S=size*4; img=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(img)
    if maskable: d.rectangle([0,0,S,S],fill=BG); k=0.62
    else: d.rounded_rectangle([0,0,S,S],radius=S*0.22,fill=BG); k=0.80
    c=S/2; R=S*0.40*k
    glow=Image.new('RGBA',(S,S),(0,0,0,0)); g=ImageDraw.Draw(glow)
    g.ellipse([c-R*1.15,c-R*1.15,c+R*1.15,c+R*1.15],fill=(216,183,106,40)); glow=glow.filter(ImageFilter.GaussianBlur(S*0.05)); img.alpha_composite(glow)
    d=ImageDraw.Draw(img); w=max(2,int(S*0.012))
    for rr,a in ((R,255),(R*0.55,180)):
        d.ellipse([c-rr,c-rr,c+rr,c+rr],outline=GOLD[:3]+(a,),width=w)
    pts=[(c+R*math.cos(-math.pi/2+i*2*math.pi/5),c+R*math.sin(-math.pi/2+i*2*math.pi/5)) for i in range(5)]
    for x,y in pts: d.line([(c,c),(x,y)],fill=BRONZE,width=w)
    def node(x,y,r,col):
        d.ellipse([x-r*1.3,y-r*1.3,x+r*1.3,y+r*1.3],fill=GOLD2); d.ellipse([x-r,y-r,x+r,y+r],fill=col+(255,))
    for (x,y),h in zip(pts,HUES): node(x,y,S*0.055*k,h)
    node(c,c,S*0.085*k,(40,30,18))
    d.ellipse([c-S*0.03*k,c-S*0.03*k,c+S*0.03*k,c+S*0.03*k],fill=GOLD2)
    return img.resize((size,size),Image.LANCZOS)
for s in (192,512): icon(s).save(f'icon-{s}.png')
icon(512,True).save('icon-maskable-512.png'); icon(180).save('apple-touch-icon.png')
print('icons written')
