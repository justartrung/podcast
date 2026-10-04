"""Hậu kỳ podcast Minh Thư (chạy trong shell Linux của Claude, dữ liệu trên D:).
Lệnh:
  analyze  <tap_dir>                       -> phân tích im lặng + ASR từng clip, ghi cat-dung/phan-tich.json
  cut      <tap_dir>                       -> cắt + ghép theo cat-dung/manifest.json -> cat-dung/noi-dung.mp4 (1080x1920, 30fps)
  asr      <tap_dir>                       -> ASR bản ghép -> phu-de/asr.json
  srt      <tap_dir>                       -> căn lời kịch bản theo timestamp ASR -> phu-de/noi-dung.srt
  render   <tap_dir> <thumbnail.png> <out_dir> -> burn phụ đề, chèn 1s thumbnail, SRT +1s, final.mp4
"""
import sys, os, json, subprocess, re, hashlib, unicodedata

MODEL = os.path.expanduser('~/mnt/PODCAST TU DONG/08-cong-cu/models/models--Systran--faster-whisper-small/snapshots/536b0662742c02347bc0e980a01041f333bce120')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr[-3000:])
    return r


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def dur(p):
    return float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).stdout)


def silences(p, noise='-35dB', d=0.25):
    r = subprocess.run(['ffmpeg', '-i', p, '-af', f'silencedetect=noise={noise}:d={d}', '-f', 'null', '-'], capture_output=True, text=True)
    out, cur = [], None
    for l in r.stderr.splitlines():
        m = re.search(r'silence_start: ([\d.]+)', l)
        if m: cur = float(m.group(1))
        m = re.search(r'silence_end: ([\d.]+)', l)
        if m and cur is not None: out.append([cur, float(m.group(1))]); cur = None
    if cur is not None: out.append([cur, dur(p)])
    return out


def model():
    from faster_whisper import WhisperModel
    return WhisperModel(MODEL, device='cpu', compute_type='int8')


def words_of(m, p):
    segs, _ = m.transcribe(p, language='vi', word_timestamps=True, vad_filter=False, beam_size=5)
    return [dict(w=w.word.strip(), s=round(w.start, 3), e=round(w.end, 3)) for s in segs for w in s.words]


def analyze(tap):
    clips = sorted(f for f in os.listdir(f'{tap}/clip-goc') if f.endswith('.mp4'))
    m = model(); res = []
    for c in clips:
        p = f'{tap}/clip-goc/{c}'
        res.append(dict(file=c, sha256=sha(p), duration=dur(p), silences=silences(p), words=words_of(m, p)))
    json.dump(res, open(f'{tap}/cat-dung/phan-tich.json', 'w'), ensure_ascii=False, indent=1)
    for r in res:
        print(r['file'], r['duration'], 'words:', ' '.join(w['w'] for w in r['words']))
        print('   speech', r['words'][0]['s'] if r['words'] else None, '->', r['words'][-1]['e'] if r['words'] else None, 'silences', r['silences'])


def cut(tap):
    man = json.load(open(f'{tap}/cat-dung/manifest.json'))
    assert man.get('cuts_reviewed_against_audio') is True
    parts = []
    for i, seg in enumerate(man['segments']):
        src = f"{tap}/clip-goc/{seg['file']}"
        assert sha(src) == seg['sha256'], 'hash clip đổi'
        out = f'{tap}/cat-dung/_p{i:02d}.mp4'
        run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{seg['start']:.3f}", '-to', f"{seg['end']:.3f}", '-i', src,
             '-vf', 'scale=1080:1920:flags=lanczos,fps=30,format=yuv420p', '-af', 'aresample=48000,afade=t=in:d=0.02,afade=t=out:st={:.3f}:d=0.03'.format(seg['end'] - seg['start'] - 0.03),
             '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', out])
        parts.append(out)
    lst = f'{tap}/cat-dung/_list.txt'
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    out = f'{tap}/cat-dung/noi-dung.mp4'
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', '-movflags', '+faststart', out])
    print('noi-dung.mp4', dur(out), sha(out))


def asr(tap):
    p = f'{tap}/cat-dung/noi-dung.mp4'
    json.dump(dict(source_sha256=sha(p), words=words_of(model(), p)), open(f'{tap}/phu-de/asr.json', 'w'), ensure_ascii=False, indent=1)
    print(' '.join(w['w'] for w in json.load(open(f'{tap}/phu-de/asr.json'))['words']))


def norm(t):
    t = unicodedata.normalize('NFC', t.lower())
    return re.sub(r'[^\w]', '', t)


def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'


def srt(tap):
    """Căn từng từ của kịch bản (đúng chính tả) vào timestamp từ ASR theo thứ tự (difflib)."""
    import difflib
    a = json.load(open(f'{tap}/phu-de/asr.json')); W = a['words']
    script = json.load(open(f'{tap}/phu-de/kich-ban-cue.json'))  # list of cue strings (theo câu / cụm)
    sw = [(ci, w) for ci, cue in enumerate(script) for w in cue.split()]
    A = [norm(w['w']) for w in W]; B = [norm(w) for _, w in sw]
    sm = difflib.SequenceMatcher(a=A, b=B, autojunk=False)
    times = [None] * len(sw)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('equal', 'replace'):
            n = min(i2 - i1, j2 - j1)
            for k in range(n): times[j1 + k] = (W[i1 + k]['s'], W[i1 + k]['e'])
            if tag == 'replace' and (j2 - j1) > n and n:  # dư từ kịch bản: gán vào từ ASR cuối
                for k in range(n, j2 - j1): times[j1 + k] = (W[i2 - 1]['s'], W[i2 - 1]['e'])
    # nội suy chỗ thiếu
    for k in range(len(times)):
        if times[k] is None:
            prv = next((times[j] for j in range(k - 1, -1, -1) if times[j]), (0, 0))
            nxt = next((times[j] for j in range(k + 1, len(times)) if times[j]), (prv[1], prv[1]))
            times[k] = (prv[1], nxt[0])
    cues = []
    for ci, cue in enumerate(script):
        idx = [k for k, (c, _) in enumerate(sw) if c == ci]
        cues.append(dict(text=cue, start=times[idx[0]][0], end=times[idx[-1]][1]))
    for i in range(len(cues) - 1):  # không chồng nhau
        cues[i]['end'] = min(cues[i]['end'] + 0.15, cues[i + 1]['start'] - 0.02)
    cues[-1]['end'] += 0.3
    match = sum(1 for t, *_ in sm.get_opcodes() if t == 'equal')
    ratio = sm.ratio()
    with open(f'{tap}/phu-de/noi-dung.srt', 'w') as f:
        for i, c in enumerate(cues, 1):
            f.write(f"{i}\n{ts(c['start'])} --> {ts(c['end'])}\n{c['text']}\n\n")
    json.dump(dict(asr_vs_script_ratio=round(ratio, 3), cues=cues), open(f'{tap}/phu-de/can-chinh.json', 'w'), ensure_ascii=False, indent=1)
    print('khớp ASR/kịch bản:', round(ratio, 3))
    for c in cues: print(f"{c['start']:6.2f}-{c['end']:6.2f} {c['text']}")


def render(tap, thumb, outdir):
    """Burn phụ đề + chèn đúng 30 khung (1,000 s @30fps) thumbnail đầu; audio nội dung dời đúng +1000 ms; SRT +1 s."""
    os.makedirs(outdir, exist_ok=True)
    src = f'{tap}/cat-dung/noi-dung.mp4'; s = f'{tap}/phu-de/noi-dung.srt'
    style = ("FontName=DejaVu Sans,Bold=1,FontSize=10,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
             "BorderStyle=1,Outline=1.4,Shadow=0.5,Alignment=2,MarginV=70,MarginL=20,MarginR=20,WrapStyle=0")
    sub_path = s.replace(':', r'\:').replace("'", r"\'")
    final = f'{outdir}/final.mp4'
    fc = (f"[1:v]fps=30,scale=1080:1920,setsar=1,format=yuv420p,subtitles='{sub_path}':force_style='{style}'[c];"
          "[0:v]scale=1080:1920,setsar=1,fps=30,format=yuv420p,trim=end_frame=30,setpts=PTS-STARTPTS[t];"
          "[t][c]concat=n=2:v=1:a=0[v];"
          "[1:a]aresample=48000,adelay=1000|1000[a]")
    run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', '30', '-t', '1.2', '-i', thumb, '-i', src,
         '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-r', '30',
         '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', final])
    txt = open(s).read()
    def sh(m):
        h, mi, se, ms = map(int, m.groups()); t = h * 3600 + mi * 60 + se + ms / 1000 + 1
        return ts(t)
    open(f'{outdir}/subtitles.srt', 'w').write(re.sub(r'(\d\d):(\d\d):(\d\d),(\d\d\d)', sh, txt))
    print('final', dur(final), sha(final))


if __name__ == '__main__':
    cmd, tap = sys.argv[1], sys.argv[2]
    dict(analyze=analyze, cut=cut, asr=asr, srt=srt)[cmd](tap) if cmd != 'render' else render(tap, sys.argv[3], sys.argv[4])
