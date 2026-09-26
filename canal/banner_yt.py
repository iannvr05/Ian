"""Rebuilds the user's banner in YouTube format (2560x1440): keeps every character from banner_original.jpg,
removes the white 'SUMMARIZER' and redraws it bigger in brown behind the characters."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

src = Image.open("banner_original.jpg").convert("RGB")
im = np.asarray(src).astype(int)
H, W, _ = im.shape
BG = (239, 160, 72)

# letters = big white blobs in the central band, plus their black outline (dilation)
white = im.min(axis=2) > 225
lab, n = ndimage.label(white)
sizes = ndimage.sum(white, lab, range(1, n + 1))
letters = np.zeros_like(white)
for i, s in enumerate(sizes, 1):
    ys, xs = np.where(lab == i)
    if s > 1500 and 520 < xs.mean() < 1560:
        letters |= lab == i
letters = ndimage.binary_dilation(letters, iterations=7)
# everything that is not background and not letter = characters
diff = np.abs(im - np.array(BG)).sum(axis=2)
chars = (diff > 60) & ~letters
alpha = Image.fromarray((ndimage.binary_opening(chars, iterations=1) * 255).astype("uint8"))
layer = src.copy(); layer.putalpha(alpha)

CW, CH = 2560, 1440
scale = CW / W
layer = layer.resize((CW, int(H * scale)), Image.LANCZOS)
canvas = Image.new("RGB", (CW, CH), BG)
d = ImageDraw.Draw(canvas)
top = (CH - layer.height) // 2

# big brown title, centered, inside the 1546 px safe width
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 260)
text = "SUMMARIZER"
w = d.textlength(text, font=font)
while w > 1500:
    font = ImageFont.truetype(font.path, font.size - 5); w = d.textlength(text, font=font)
bbox = d.textbbox((0, 0), text, font=font, stroke_width=14)
th = bbox[3] - bbox[1]
canvas.paste(layer, (0, top), layer)
d = ImageDraw.Draw(canvas)
pos = ((CW - w) / 2, CH / 2 - th / 2 - bbox[1] - 10)
d.text(pos, text, font=font, fill=None, stroke_width=26, stroke_fill=(255, 236, 200))  # light halo
d.text(pos, text, font=font, fill=(110, 58, 30), stroke_width=14, stroke_fill=(20, 20, 20))
canvas.save("banner_youtube.png")
print("ok", font.size, w, layer.size)
