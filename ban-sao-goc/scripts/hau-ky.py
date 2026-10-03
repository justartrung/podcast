"""Cut reviewed intervals, transcribe real edited audio, and burn Vietnamese SRT."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parents[1]
try:
    TZ = ZoneInfo('Asia/Bangkok')
except ZoneInfoNotFoundError:
    TZ = timezone(timedelta(hours=7), name='Asia/Bangkok')


def local(rel, exists=True):
    p = (ROOT / rel).resolve()
    if not p.is_relative_to(ROOT.resolve()):
        raise ValueError('Path must stay inside project')
    if exists and not p.is_file():
        raise ValueError(f'File missing: {rel}')
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def guard():
    stop = json.loads((ROOT/'03-he-thong/STOP.json').read_text(encoding='utf-8-sig'))
    if stop['enabled'] or (ROOT/'STOP.now').exists():
        raise ValueError('STOP active')


def tools():
    d = json.loads((ROOT/'03-he-thong/kiem-ke.json').read_text(encoding='utf-8-sig'))
    if not d.get('ffmpeg') or not d.get('ffprobe'):
        raise ValueError('FFmpeg/FFprobe not verified')
    return d['ffmpeg'], d['ffprobe']


def call(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, encoding='utf-8', errors='replace')
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:])
    return p.stdout


def probe(path):
    return json.loads(call([tools()[1],'-v','error','-show_streams','-show_format','-of','json',str(path)]))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def stamp(seconds):
    ms=round(seconds*1000)
    h,ms=divmod(ms,3600000); minute,ms=divmod(ms,60000); sec,ms=divmod(ms,1000)
    return f'{h:02}:{minute:02}:{sec:02},{ms:03}'


def wrap(text, limit=34):
    lines=[]; line=''
    for word in text.split():
        if line and len(line)+1+len(word)>limit:
            lines.append(line); line=word
        else: line=(line+' '+word).strip()
    if line: lines.append(line)
    return '\n'.join(lines)


def make_cues(words):
    cues=[]; group=[]
    for w in words:
        text=' '.join(x['word'].strip() for x in group+[w])
        if group and (w['end']-group[0]['start']>4.5 or len(text)>64 or w['start']-group[-1]['end']>0.6):
            cues.append(group);group=[]
        group.append(w)
        if w['word'].strip().endswith(('.', '?', '!')):
            cues.append(group);group=[]
    if group:cues.append(group)
    return [dict(start=g[0]['start'],end=g[-1]['end'],text=wrap(' '.join(x['word'].strip() for x in g))) for g in cues]


def assemble(manifest_rel):
    manifest_path=local(manifest_rel)
    d=json.loads(manifest_path.read_text(encoding='utf-8-sig'))
    if not d.get('cuts_reviewed_against_audio') or not d.get('reviewer'):
        raise ValueError('Review retained intervals against actual audio first')
    out=local(d['output'],False)
    if out.exists():raise ValueError('Output exists; choose a new version')
    tmp=out.parent/'segments';tmp.mkdir(exist_ok=True)
    parts=[];total=0
    for i,c in enumerate(d['clips'],1):
        guard();src=local(c['file']);meta=probe(src)
        if sha(src)!=c['sha256']:raise ValueError('Input clip changed')
        if not any(s['codec_type']=='audio' for s in meta['streams']):raise ValueError('Clip has no audio')
        start,end=c['keep_start'],c['keep_end']
        if not 0<=start<end<=float(meta['format']['duration'])+0.02:raise ValueError('Invalid cut interval')
        part=tmp/f'{i:03d}.mp4';duration=end-start;total+=duration
        if total>90:raise ValueError('Episode exceeds 90 seconds')
        call([tools()[0],'-hide_banner','-loglevel','error','-n','-i',str(src),'-ss',str(start),'-t',str(duration),
              '-map','0:v:0','-map','0:a:0','-vf','scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1',
              '-r','30','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2',str(part)])
        parts.append(part)
    if not parts:raise ValueError('No clips')
    concat=tmp/'concat.txt';concat.write_text('\n'.join(f"file '{p.name}'" for p in parts),encoding='utf-8')
    guard()
    call([tools()[0],'-hide_banner','-loglevel','error','-n','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(out)])
    write_json(out.with_suffix('.assembly.json'),dict(manifest=manifest_rel,manifest_sha256=sha(manifest_path),output_sha256=sha(out),duration=total))
    print(out)


def transcribe(input_rel, model_path, output_rel):
    from faster_whisper import WhisperModel
    guard();src=local(input_rel);out=local(output_rel,False)
    if out.exists():raise ValueError('Transcript exists; choose a new version')
    model_dir=(ROOT/model_path).resolve()
    if not model_dir.is_relative_to(ROOT.resolve()) or not (model_dir/'model.bin').exists():
        raise ValueError('Approved local model directory required')
    model=WhisperModel(str(model_dir),device='cpu',compute_type='int8',local_files_only=True)
    segments,info=model.transcribe(str(src),language='vi',word_timestamps=True,vad_filter=True,beam_size=5)
    words=[]
    for segment in segments:
        for w in segment.words or []:
            words.append(dict(start=w.start,end=w.end,word=w.word,probability=w.probability))
    if not words:raise ValueError('No speech detected; inspect audio')
    cues=make_cues(words)
    write_json(out,dict(source=input_rel,source_sha256=sha(src),language=info.language,words=words,cues=cues,
                        audio_reviewed=False,note='ASR draft: listen, correct Vietnamese text and timestamps before burn'))
    print(out)


def render(input_rel, transcript_rel, output_rel):
    guard();src=local(input_rel);tpath=local(transcript_rel)
    d=json.loads(tpath.read_text(encoding='utf-8-sig'))
    if d.get('source_sha256')!=sha(src) or not d.get('audio_reviewed') or not d.get('reviewer'):
        raise ValueError('Transcript must identify current edited master and be audio-reviewed')
    duration=float(probe(src)['format']['duration']);last=0;srt=[]
    for i,c in enumerate(d['cues'],1):
        if not last<=c['start']<c['end']<=duration+0.01:raise ValueError('Bad/overlapping subtitle timestamp')
        if not c['text'].strip():raise ValueError('Empty subtitle')
        if len(c['text'].splitlines())>2:raise ValueError('At most two subtitle lines')
        srt.append(f"{i}\n{stamp(c['start'])} --> {stamp(c['end'])}\n{c['text']}\n")
        last=c['end']
    if not srt:raise ValueError('No subtitles')
    out=local(output_rel,False)
    if out.exists():raise ValueError('Master exists; choose a new version')
    # ASCII basename in cwd avoids Windows drive/filter escaping issues.
    subtitle=out.parent/'subtitles.srt';subtitle.write_text('\n'.join(srt),encoding='utf-8-sig')
    style='FontName=Arial,FontSize=10,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=0.7,Shadow=0,Alignment=2,MarginV=55,MarginL=18,MarginR=18'
    call([tools()[0],'-hide_banner','-loglevel','error','-n','-i',str(src),'-vf',f"subtitles=subtitles.srt:force_style='{style}'",
          '-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',str(out)],cwd=out.parent)
    check(output_rel)
    write_json(out.with_suffix('.subtitle-provenance.json'),dict(source_sha256=sha(src),transcript_sha256=sha(tpath),master_sha256=sha(out),srt_sha256=sha(subtitle)))
    print(out)


def check(input_rel):
    guard();src=local(input_rel);p=probe(src)
    video=next(s for s in p['streams'] if s['codec_type']=='video')
    audio=next(s for s in p['streams'] if s['codec_type']=='audio')
    if video['codec_name']!='h264' or audio['codec_name']!='aac':raise ValueError('Require H.264/AAC')
    if abs(video['width']/video['height']-9/16)>0.002:raise ValueError('Require 9:16')
    if float(p['format']['duration'])>90.1:raise ValueError('Over 90 seconds')
    call([tools()[0],'-hide_banner','-v','error','-xerror','-i',str(src),'-f','null','-'])
    write_json(src.with_suffix('.technical.json'),dict(technical_pass=True,master_sha256=sha(src),ffprobe=p,
               checked_at=datetime.now(TZ).isoformat(),full_watch_listen=False))
    print('TECHNICAL PASS only; full watch/listen and subtitle sync still required')


def main():
    p=argparse.ArgumentParser();subs=p.add_subparsers(dest='command',required=True)
    s=subs.add_parser('assemble');s.add_argument('--manifest',required=True)
    s=subs.add_parser('transcribe');s.add_argument('--input',required=True);s.add_argument('--model',required=True);s.add_argument('--output',required=True)
    s=subs.add_parser('render');s.add_argument('--input',required=True);s.add_argument('--transcript',required=True);s.add_argument('--output',required=True)
    s=subs.add_parser('check');s.add_argument('--input',required=True)
    a=p.parse_args()
    if a.command=='assemble':assemble(a.manifest)
    elif a.command=='transcribe':transcribe(a.input,a.model,a.output)
    elif a.command=='render':render(a.input,a.transcript,a.output)
    else:check(a.input)


if __name__=='__main__':main()
