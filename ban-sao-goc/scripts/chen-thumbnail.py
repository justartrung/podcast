"""Prepend exactly 30 frames at 30 fps and shift external SRT by one second."""
import argparse,json,re
from pathlib import Path
import importlib.util
spec=importlib.util.spec_from_file_location('post',Path(__file__).with_name('hau-ky.py'))
post=importlib.util.module_from_spec(spec);spec.loader.exec_module(post)
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--thumbnail',required=True);p.add_argument('--srt',required=True);p.add_argument('--output',required=True)
a=p.parse_args();post.guard()
src=post.local(a.input);thumb=post.local(a.thumbnail);srt=post.local(a.srt);out=post.local(a.output,False)
if out.exists():raise ValueError('Output exists: choose new version')
dest=out.parent/'subtitles.srt'
if dest.resolve()==srt.resolve() or dest.exists():raise ValueError('Use fresh delivery folder; preserve source SRT')
meta=post.probe(src);duration=float(meta['format']['duration'])
if duration+1>90:raise ValueError('Including intro exceeds 90 seconds')
from struct import unpack
header=thumb.read_bytes()[:24]
if header[:8]!=b'\x89PNG\r\n\x1a\n' or unpack('>II',header[16:24])!=(1080,1920):raise ValueError('Require 1080x1920 PNG thumbnail')
f='[0:v]fps=30,trim=end_frame=30,setpts=PTS-STARTPTS,setsar=1,format=yuv420p[intro];[1:v]fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,setpts=PTS-STARTPTS[v];[2:a]atrim=duration=1,asetpts=PTS-STARTPTS[s];[1:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS[a];[intro][s][v][a]concat=n=2:v=1:a=1[vo][ao]'
post.call([post.tools()[0],'-hide_banner','-loglevel','error','-n','-loop','1','-framerate','30','-i',str(thumb),'-i',str(src),'-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-filter_complex',f,'-map','[vo]','-map','[ao]','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',str(out)])
def shift(m):
    h,minute,sec,ms=map(int,m.groups())
    return post.stamp(h*3600+minute*60+sec+ms/1000+1)
shifted=re.sub(r'(\d{2}):(\d{2}):(\d{2}),(\d{3})',shift,srt.read_text(encoding='utf-8-sig'))
dest.write_text(shifted,encoding='utf-8-sig')
post.check(a.output)
post.write_json(out.with_suffix('.intro.json'),dict(source_sha256=post.sha(src),thumbnail_sha256=post.sha(thumb),master_sha256=post.sha(out),intro_frames=30,fps=30,intro_seconds=1,external_srt_offset_seconds=1,real_watch_listen_pending=True))
print(out)
