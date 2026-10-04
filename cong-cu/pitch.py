import sys,subprocess,numpy as np
def f0(path):
    raw=subprocess.run(['ffmpeg','-v','error','-i',path,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    x=np.frombuffer(raw,np.float32); sr=16000; fl=640; hop=320; out=[]
    for i in range(0,len(x)-fl,hop):
        f=x[i:i+fl]; 
        if np.sqrt((f**2).mean())<0.02: continue
        f=f-f.mean(); ac=np.correlate(f,f,'full')[fl-1:]
        lo,hi=int(sr/400),int(sr/70); k=lo+np.argmax(ac[lo:hi])
        if ac[k]/ac[0]>0.5: out.append(sr/k)
    out=np.array(out); return np.median(out), np.percentile(out,10), np.percentile(out,90), len(out)
for p in sys.argv[1:]:
    m,a,b,n=f0(p); print(f'{p.split("/")[-1]}: F0 median {m:.0f} Hz (p10 {a:.0f}, p90 {b:.0f}, voiced frames {n})')
