"""Draws the channel profile mascot by hand (no AI): cartoon storyteller with helmet and scroll."""
from PIL import Image, ImageDraw

S = 4  # supersampling for smooth edges
W = 1024 * S
img = Image.new("RGB", (W, W), (255, 138, 36))
d = ImageDraw.Draw(img)
K = (20, 20, 20)
LW = 14 * S


def s(*v):
    return [x * S for x in v]


# soft background ring
d.ellipse(s(60, 60, 964, 964), fill=(255, 158, 64))

# shoulders / tunic
d.rounded_rectangle(s(250, 760, 774, 1100), radius=160 * S, fill=(236, 226, 205), outline=K, width=LW)
d.line(s(512, 790, 512, 1024), fill=(200, 160, 60), width=18 * S)
d.polygon(s(400, 770, 512, 880, 624, 770), fill=(214, 170, 60), outline=K)

# head
d.ellipse(s(292, 300, 732, 800), fill=(255, 255, 255), outline=K, width=LW)

# helmet dome
d.chord(s(270, 200, 754, 640), 180, 360, fill=(205, 140, 60), outline=K, width=LW)
d.rectangle(s(270, 418, 754, 468), fill=(180, 118, 45), outline=K, width=LW)
d.line(s(512, 210, 512, 418), fill=(150, 95, 35), width=16 * S)
# red crest
for i, x in enumerate(range(360, 680, 22)):
    top = 90 + abs(512 - x) * 0.45
    d.line(s(x, 250, x - 10, top), fill=(200, 40, 40), width=34 * S)
d.arc(s(350, 70, 674, 330), 200, 340, fill=K, width=LW)

# eyes
for cx in (430, 594):
    d.ellipse(s(cx - 34, 540, cx + 34, 626), fill=K)
    d.ellipse(s(cx - 16, 552, cx + 2, 572), fill=(255, 255, 255))
# eyebrows (one raised)
d.line(s(390, 515, 468, 505), fill=K, width=16 * S)
d.line(s(556, 490, 636, 470), fill=K, width=16 * S)
# smile
d.arc(s(430, 600, 600, 720), 20, 160, fill=K, width=14 * S)

# scroll next to the face
d.rounded_rectangle(s(740, 560, 880, 900), radius=30 * S, fill=(245, 225, 180), outline=K, width=LW)
d.ellipse(s(720, 530, 900, 600), fill=(230, 200, 150), outline=K, width=LW)
d.ellipse(s(720, 860, 900, 930), fill=(230, 200, 150), outline=K, width=LW)
for y in (640, 690, 740, 790):
    d.line(s(770, y, 850, y), fill=(170, 130, 80), width=8 * S)
# hand holding the scroll
d.ellipse(s(700, 700, 790, 800), fill=(255, 255, 255), outline=K, width=LW)

img.resize((1024, 1024), Image.LANCZOS).save("/home/user/Ian/canal/perfil_dibujado.png")
print("ok")
