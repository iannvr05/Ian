"""Draws the YouTube banner by hand (no AI). 2560x1440; text and mascots stay inside the
1546x423 safe area that YouTube shows on every device.

Usage: python3 dibujar_banner.py ["Channel name"] ["tagline"]
"""
import sys
from PIL import Image, ImageDraw, ImageFont

NAME = sys.argv[1] if len(sys.argv) > 1 else "The History Summarizer"
TAG = sys.argv[2] if len(sys.argv) > 2 else "Historias reales en menos de un minuto"
W, H = 2560, 1440
K = (20, 20, 20)
img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# sunset gradient sky
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(255 - 40 * t), int(170 - 90 * t), int(70 - 30 * t)))
d.ellipse([W // 2 - 260, 330, W // 2 + 260, 850], fill=(255, 214, 120))  # sun

# silhouettes along the horizon: pyramids, castle, Alcatraz lighthouse, mountains
SIL = (120, 50, 30)
d.polygon([(0, 1000), (300, 780), (520, 930), (760, 760), (1000, 1000)], fill=(150, 65, 35))
d.polygon([(1560, 1000), (1800, 790), (2040, 1000)], fill=SIL)
d.polygon([(1880, 1000), (2080, 850), (2280, 1000)], fill=SIL)
d.polygon([(2150, 1000), (2400, 720), (2560, 900), (2560, 1000)], fill=(150, 65, 35))
d.rectangle([900, 880, 1060, 1000], fill=SIL)
for x in range(900, 1060, 40):
    d.rectangle([x, 850, x + 22, 880], fill=SIL)
d.rectangle([1420, 800, 1460, 1000], fill=SIL)
d.polygon([(1410, 800), (1440, 760), (1470, 800)], fill=SIL)
d.rectangle([0, 1000, W, H], fill=(95, 40, 25))


def head(cx, cy, r, hat):
    """Round white cartoon head with simple eyes, like the channel characters."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r * 1.1], fill="white", outline=K, width=10)
    for ex in (cx - r * 0.35, cx + r * 0.35):
        d.ellipse([ex - r * 0.13, cy - r * 0.05, ex + r * 0.13, cy + r * 0.3], fill=K)
        d.ellipse([ex - r * 0.07, cy, ex, cy + r * 0.08], fill="white")
    d.arc([cx - r * 0.35, cy + r * 0.2, cx + r * 0.35, cy + r * 0.65], 20, 160, fill=K, width=9)
    if hat == "helmet":
        d.chord([cx - r * 1.05, cy - r * 1.15, cx + r * 1.05, cy + r * 0.35], 180, 360, fill=(205, 140, 60), outline=K, width=10)
        d.polygon([(cx - r * 0.5, cy - r * 0.9), (cx, cy - r * 1.7), (cx + r * 0.5, cy - r * 0.9)], fill=(200, 40, 40), outline=K)
    elif hat == "crown":
        pts = [(cx - r * 0.8, cy - r * 0.55), (cx - r * 0.8, cy - r * 1.2), (cx - r * 0.4, cy - r * 0.85), (cx, cy - r * 1.35),
               (cx + r * 0.4, cy - r * 0.85), (cx + r * 0.8, cy - r * 1.2), (cx + r * 0.8, cy - r * 0.55)]
        d.polygon(pts, fill=(250, 200, 50), outline=K)
        d.line(pts + [pts[0]], fill=K, width=10)
    elif hat == "prisoner":
        d.chord([cx - r * 0.95, cy - r * 1.05, cx + r * 0.95, cy + r * 0.2], 180, 360, fill=(110, 70, 40), outline=K, width=10)
        d.ellipse([cx - r * 0.6, cy + r * 0.55, cx + r * 0.6, cy + r * 1.15], fill=(110, 70, 40))  # beard


def body(cx, top, r, color):
    d.rounded_rectangle([cx - r * 1.2, top, cx + r * 1.2, top + r * 2.2], radius=int(r * 0.8), fill=color, outline=K, width=10)


# three mascots inside the safe area, left and right of the title
for cx, cy, hat, col in ((330, 760, "crown", (245, 235, 210)), (560, 740, "helmet", (180, 60, 50)), (2010, 740, "prisoner", (240, 120, 30))):
    r = 100
    body(cx, cy + r * 0.9, r, col)
    head(cx, cy, r, hat)

# title and tagline, centered in the safe area
def centered(text, y, size, fill, stroke):
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=K)

centered(NAME, 610, 100 if len(NAME) < 22 else 88, "white", 10)
centered(TAG, 740, 48, (255, 240, 200), 6)

img.save("/home/user/Ian/canal/banner.png")
print("ok")
