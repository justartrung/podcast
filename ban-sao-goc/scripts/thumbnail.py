"""Composite existing locked host photo and separate Vietnamese text; no AI regeneration."""
from pathlib import Path
import json, hashlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'06-san-sang-dang/MT-0001';out.mkdir(parents=True,exist_ok=True)
src=ROOT/'02-host/1.png'
im=Image.new('RGB',(1080,1920),(9,8,5))
photo=Image.open(src).convert('RGB');photo.thumbnail((1080,1420),Image.Resampling.LANCZOS)
im.paste(photo,((1080-photo.width)//2,490))
draw=ImageDraw.Draw(im)
draw.rectangle((20,20,1060,1900),outline=(162,122,35),width=3)
fontpath=Path('C:/Windows/Fonts/timesbd.ttf')
def gold_text(text,y,size):
    font=ImageFont.truetype(str(fontpath),size)
    box=font.getbbox(text);x=(1080-(box[2]-box[0]))//2-box[0]
    mask=Image.new('L',im.size);md=ImageDraw.Draw(mask)
    md.text((x,y),text,font=font,fill=255)
    shadow=Image.new('L',im.size);ImageDraw.Draw(shadow).text((x+3,y+5),text,font=font,fill=180)
    im.paste((100,65,12),(0,0,1080,1920),shadow.filter(ImageFilter.GaussianBlur(3)))
    gradient=Image.new('RGB',im.size);gd=ImageDraw.Draw(gradient)
    for yy in range(1920):
        t=((yy-y)%max(1,size))/size
        c=(255,230,150) if t<.35 else ((203,154,49) if t<.7 else (247,208,94))
        gd.line((0,yy,1080,yy),fill=c)
    im.paste(gradient,(0,0),mask)
for text,y in [('MỘT CÂU HỎI',45),('CẢ NHÀ',185),('IM LẶNG',325)]:gold_text(text,y,91)
draw=ImageDraw.Draw(im);draw.rectangle((0,1765,1080,1920),fill=(4,4,3));draw.line((35,1770,1045,1770),fill=(202,160,65),width=3)
gold_text('COACH MINH THƯ',1805,65)
im.save(out/'thumbnail.png')
(out/'caption.txt').write_text('Một câu hỏi vì lo lắng đôi khi lại được nghe thành lời trách. Thử nói rõ điều mình cần, bằng một lời đề nghị nhẹ nhàng. Tối nay, bạn muốn người nhà hiểu điều gì?\n#ChuyenGiaDinh #MinhThu\n',encoding='utf-8')
(out/'thumbnail-provenance.json').write_text(json.dumps({'source':'02-host/1.png','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'size':[1080,1920],'face_regenerated':False,'font':str(fontpath),'episode':'MT-0001','status':'thumbnail_only_not_episode_QA'},ensure_ascii=False,indent=2),encoding='utf-8')
print(out/'thumbnail.png')
