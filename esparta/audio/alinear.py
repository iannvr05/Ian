"""Alinea las 57 frases de guion.md con parte1.mp3 + parte2.mp3 buscando las pausas de la voz.
Guarda tiempos.json: [(inicio_s, fin_s) en la línea de tiempo total] por escena."""
import json, os, re, subprocess
import numpy as np, imageio_ffmpeg
D = os.path.dirname(os.path.abspath(__file__)); FF = imageio_ffmpeg.get_ffmpeg_exe(); HOP = 0.01
L = [l.split("|")[2].strip() for l in open(f"{D}/../guion.md") if re.match(r"^\| \d+ \|", l)]
ch = np.array([len(x) for x in L], float)

def pausas(f):
    raw = subprocess.run([FF, "-loglevel", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(float); w = int(16000 * HOP); n = len(a) // w
    db = 20 * np.log10(np.sqrt((a[:n * w].reshape(n, w) ** 2).mean(1)) + 1) - 90.3
    q = db < -50; out = []; i = 0
    while i < n:
        if q[i]:
            j = i
            while j < n and q[j]: j += 1
            if (j - i) * HOP >= 0.08: out.append(((i + j) / 2 * HOP, (j - i) * HOP))
            i = j
        else: i += 1
    voz = np.where(~q)[0]
    return out, voz[0] * HOP, voz[-1] * HOP + HOP

def dp(cands, t0, t1, lines, rate):
    """Elige len(lines)-1 cortes entre las pausas; coste = error de duración frente a lo esperado - premio por pausa larga."""
    m = len(lines); P = [(t0, 0)] + cands + [(t1, 0)]; K = len(P)
    INF = 1e18; best = np.full((m + 1, K), INF); bk = np.zeros((m + 1, K), int); best[0][0] = 0
    for s in range(1, m + 1):
        e = rate * ch[lines[s - 1]]
        for k in range(1, K):
            if s == m and k != K - 1: continue
            for j in range(k):
                if best[s - 1][j] >= INF: continue
                d = P[k][0] - P[j][0]
                c = best[s - 1][j] + ((d - e) / (0.25 * e + 1)) ** 2 - (8 * P[k][1] if k < K - 1 else 0)
                if c < best[s][k]: best[s][k] = c; bk[s][k] = j
    k = K - 1; cuts = []
    for s in range(m, 0, -1): cuts.append(P[k][0]); k = bk[s][k]
    return best[m][K - 1], [t0] + cuts[::-1]

(c1, a1, b1), (c2, a2, b2) = pausas(f"{D}/parte1.mp3"), pausas(f"{D}/parte2.mp3")
dur1 = float(subprocess.run([FF, "-i", f"{D}/parte1.mp3"], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0].split(":")[2]) \
       + 60 * int(subprocess.run([FF, "-i", f"{D}/parte1.mp3"], capture_output=True, text=True).stderr.split("Duration: ")[1].split(":")[1])
K1 = 37  # Ian: la parte 2 empieza en "Antes de la batalla…" (escena 38)
res = []
for k in [K1]:
    r1 = (b1 - a1) / ch[:k].sum(); r2 = (b2 - a2) / ch[k:].sum()
    s1, t1 = dp(c1, a1, b1, list(range(k)), r1); s2, t2 = dp(c2, a2, b2, list(range(k, len(L))), r2)
    res.append((s1 + s2, k, t1, t2))
res.sort(key=lambda r: r[0]); print("mejores cortes parte1/parte2:", [(r[1], round(r[0], 1)) for r in res[:4]])
_, k, t1, t2 = res[0]
T = [(t1[i], t1[i + 1]) for i in range(k)] + [(dur1 + t2[i], dur1 + t2[i + 1]) for i in range(len(L) - k)]
json.dump({"parte1_hasta": k, "dur1": dur1, "tiempos": T}, open(f"{D}/tiempos.json", "w"), indent=1)
for i, (a, b) in enumerate(T, 1): print(f"{i:2d} {a:6.1f}-{b:6.1f} ({b - a:4.1f}s) {L[i - 1][:50]}")
