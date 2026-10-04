import sys, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
src, out = sys.argv[1], sys.argv[2]; lines = sys.argv[3:6]
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
im=Image.new('RGB',(1080,1920),(9,8,5))
photo=Image.open(src).convert('RGB');photo.thumbnail((1080,1420),Image.Resampling.LANCZOS)
im.paste(photo,((1080-photo.width)//2,490))
ImageDraw.Draw(im).rectangle((20,20,1060,1900),outline=(162,122,35),width=3)
def gold(text,y,size):
    font=ImageFont.truetype(FONT,size); b=font.getbbox(text); x=(1080-(b[2]-b[0]))//2-b[0]
    mask=Image.new('L',im.size); ImageDraw.Draw(mask).text((x,y),text,font=font,fill=255)
    sh=Image.new('L',im.size); ImageDraw.Draw(sh).text((x+3,y+5),text,font=font,fill=180)
    im.paste((100,65,12),(0,0,1080,1920),sh.filter(ImageFilter.GaussianBlur(3)))
    g=Image.new('RGB',im.size); gd=ImageDraw.Draw(g)
    for yy in range(1920):
        t=((yy-y)%max(1,size))/size
        gd.line((0,yy,1080,yy),fill=(255,230,150) if t<.35 else ((203,154,49) if t<.7 else (247,208,94)))
    im.paste(g,(0,0),mask)
for t,y in zip(lines,[45,185,325]): gold(t,y,88)
d=ImageDraw.Draw(im); d.rectangle((0,1765,1080,1920),fill=(4,4,3)); d.line((35,1770,1045,1770),fill=(202,160,65),width=3)
gold('COACH MINH THƯ',1805,62)
im.save(out)
