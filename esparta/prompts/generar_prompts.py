"""Genera img1.txt…img60.txt para 'Tu vida como espartano' (16:9, imágenes estáticas) desde ../escenas.py."""
import os, sys
d = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(d))
from escenas import S
PRE = ("IMPORTANT: Do not copy ANY element or character from the reference image. Use the uploaded image ONLY as an "
       "art style reference (round white cartoon faces with simple expressive eyes, thick black outlines, flat colors). ")
POST = (" Time period: ancient Greece, 5th century BC, in and around Sparta in the Eurotas valley under Mount Taygetus, "
        "unless the scene says otherwise; nothing modern unless the scene says so. Style: 2D cartoon like a history explainer "
        "animation, thick black outlines, flat colors with soft shading, highly detailed painted background with rich "
        "atmospheric lighting, epic landscapes. All people have round white cartoon faces with simple eyes. No glow outline. "
        "ABSOLUTELY NO TEXT anywhere: no words, no letters, no numbers, no Greek letters or symbols on shields, no logos, "
        "no inscriptions. No blood, no gore, no wounds, no dead bodies, no nudity: everyone fully clothed. No watermark. "
        "Horizontal 16:9 widescreen.")
for n, (_, _, s) in enumerate(S, 1):
    open(f"{d}/img{n}.txt", "w").write("MAIN SUBJECT, must be clearly visible, large and in the foreground, this is the "
                                         "most important part of the image: " + s + " " + PRE + POST)
print(len(S), "prompts")
