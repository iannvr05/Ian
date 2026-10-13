"""Monta escobar/video/escobar.mp4: cada escenaN.png con zoom lento (Ken Burns), duración según las palabras
de su frase en guion.md (~2,4 palabras/s, ritmo de ZVoice). Sin audio. Uso: python3 montar.py [N...] (solo esos clips)."""
import json, os, re, subprocess, sys
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); V = f"{P}/video"; C = f"{V}/clips"
os.makedirs(C, exist_ok=True)
WPS, FPS = 2.4, 30
rows = [l.split("|") for l in open(f"{P}/guion.md") if re.match(r"^\| \d+ \|", l)]
dur = {int(r[1]): max(5.0, round(len(r[2].split()) / WPS, 1)) for r in rows}
AUD = f"{P}/audio"; TJ = f"{AUD}/tiempos.json"
if os.path.exists(TJ):  # con voz: cada imagen dura desde que empieza su frase hasta que empieza la siguiente
    T = json.load(open(TJ))["tiempos"]; st = [0.0] + [a for a, _ in T[1:]] + [T[-1][1] + 1.0]
    dur = {i + 1: round(st[i + 1] - st[i], 3) for i in range(len(T))}

def clip(n):
    out = f"{C}/c{n:02d}.mp4"; frames = int(dur[n] * FPS)
    z = "1+0.10*on/{f}" if n % 2 else "1.10-0.10*on/{f}"          # alterna acercar / alejar
    pan = ["iw/2-(iw/zoom/2)", "(iw-iw/zoom)*on/{f}", "(iw-iw/zoom)*(1-on/{f})"][n % 3]  # centro, paneo dcha, paneo izda
    vf = (f"scale=3840:2160,zoompan=z='{z}':x='{pan}':y='ih/2-(ih/zoom/2)':d={frames}:s=1920x1080:fps={FPS}"
          .replace("{f}", str(frames)) + ",format=yuv420p")
    subprocess.run([FF, "-y", "-loglevel", "error", "-loop", "1", "-i", f"{P}/escena{n}.png", "-vf", vf,
                    "-frames:v", str(frames), "-c:v", "libx264", "-preset", "medium", "-crf", "20", out], check=True)
    return out

ns = [int(a) for a in sys.argv[1:]] or sorted(dur)
for n in ns: clip(n); print(f"clip {n}: {dur[n]} s", flush=True)
if not sys.argv[1:]:
    open(f"{C}/lista.txt", "w").write("".join(f"file 'c{n:02d}.mp4'\n" for n in sorted(dur)))
    voz = os.path.exists(TJ)
    aud = (["-i", f"{AUD}/parte1.mp3", "-i", f"{AUD}/parte2.mp3", "-filter_complex", "[1:a][2:a]concat=n=2:v=0:a=1[a]",
            "-map", "0:v", "-map", "[a]", "-c:a", "aac", "-b:a", "128k"] if voz else [])
    subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{C}/lista.txt", *aud,
                    "-c:v", "libx264", "-preset", "slow", "-crf", "26", "-movflags", "+faststart",
                    f"{V}/esparta{'_voz' if voz else ''}.mp4"], check=True)
    print(f"FIN: {sum(dur.values()):.0f} s en total", flush=True)
