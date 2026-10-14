"""Genera guion.md y guion_zvoice.txt desde escenas.py (+ datos.md)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
from escenas import S, CAP
caps = dict(CAP)
md = ["# Tu vida como pirata (≈8 min · horizontal 16:9 · imágenes estáticas)", "",
      f"{len(S)} imágenes, una por frase. Sin sangre ni cadáveres.", "", "| # | Narración | Imagen |", "|---|---|---|"]
zv = []
for i, (n, im, _) in enumerate(S, 1):
    if i in caps: md.append(f"| **{caps[i]}** | | |"); zv.append(f"\n[{caps[i]}]")
    md.append(f"| {i} | {n} | {im} |"); zv.append(n)
md += ["", "## Datos y matices", open(f"{D}/datos.md").read()]
open(f"{D}/guion.md", "w").write("\n".join(md))
open(f"{D}/guion_zvoice.txt", "w").write("\n".join(zv).strip() + "\n")
print(len(S), "escenas,", sum(len(n.split()) for n, _, _ in S), "palabras,", sum(len(n) for n, _, _ in S), "caracteres")
