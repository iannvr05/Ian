"""Render each scene image into an 8 s vertical clip with camera moves and basic effects.

Usage: python3 render_clips.py [scene numbers...]   (default: all 8)
Output: clips/escenaN.mp4 (1080x1920, 30 fps, no audio) and clips/short_completo.mp4
"""
import math
import random
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).parent
OUT = HERE / "clips"
W, H, FPS, SECONDS = 1080, 1920, 30, 8
FRAMES = FPS * SECONDS
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

# Camera per scene: zoom (1 = full image) and centre (x, y as 0..1 of the image), start -> end.
# fx: particle effect, shake: camera shake strength, flicker: firelight flicker, fade_out: fade to black at the end.
SCENES = {
    1: dict(z=(1.45, 1.0), c=((0.62, 0.72), (0.5, 0.5)), fx="dust"),
    2: dict(z=(1.0, 1.35), c=((0.5, 0.5), (0.32, 0.36)), fx="embers"),
    3: dict(z=(1.0, 1.5), c=((0.5, 0.5), (0.5, 0.72)), fx="motes"),
    4: dict(z=(1.6, 1.0), c=((0.5, 0.64), (0.5, 0.5)), fx="dust"),
    5: dict(z=(1.55, 1.0), c=((0.74, 0.36), (0.5, 0.5)), fx="ash"),
    6: dict(z=(1.15, 1.32), c=((0.5, 0.58), (0.5, 0.62)), fx="dust", shake=6),
    7: dict(z=(1.0, 1.4), c=((0.5, 0.5), (0.5, 0.78)), fx="embers", flicker=True, fade_out=1.0),
    8: dict(z=(1.0, 1.3), c=((0.5, 0.5), (0.5, 0.6)), fx="sparkles", fade_out=0.6),
}

PARTICLES = {
    # count, colour, size range, velocity (px/frame), alpha, blur
    "dust": (70, (235, 215, 180), (2, 6), ((-1.2, 1.2), (-0.4, 0.3)), 110, 1.5),
    "motes": (45, (255, 240, 200), (2, 5), ((-0.4, 0.4), (-0.5, 0.2)), 120, 1.2),
    "embers": (60, (255, 150, 50), (2, 5), ((-0.6, 0.6), (-2.2, -0.8)), 200, 1.0),
    "ash": (70, (90, 85, 80), (2, 6), ((-0.8, 0.8), (0.6, 1.6)), 150, 1.0),
    "sparkles": (40, (255, 225, 140), (2, 5), ((-0.3, 0.3), (-0.6, -0.1)), 200, 0.8),
}


def ease(t):
    return t * t * (3 - 2 * t)


def make_particles(kind, seed):
    n, color, (smin, smax), ((vx0, vx1), (vy0, vy1)), alpha, blur = PARTICLES[kind]
    rng = random.Random(seed)
    return [dict(x=rng.uniform(0, W), y=rng.uniform(0, H), vx=rng.uniform(vx0, vx1), vy=rng.uniform(vy0, vy1),
                 s=rng.uniform(smin, smax), ph=rng.uniform(0, 6.28)) for _ in range(n)], color, alpha, blur


def particle_layer(parts, color, alpha, blur, f):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for p in parts:
        x = (p["x"] + p["vx"] * f + 8 * math.sin(f / 25 + p["ph"])) % W
        y = (p["y"] + p["vy"] * f) % H
        a = int(alpha * (0.55 + 0.45 * math.sin(f / 12 + p["ph"])))
        r = p["s"]
        d.ellipse((x - r, y - r, x + r, y + r), fill=(*color, a))
    return layer.filter(ImageFilter.GaussianBlur(blur))


def vignette():
    y, x = np.ogrid[:H, :W]
    d = np.sqrt(((x - W / 2) / (W / 2)) ** 2 + ((y - H / 2) / (H / 2)) ** 2)
    return np.clip(1.0 - 0.35 * np.clip(d - 0.55, 0, None) ** 1.5, 0, 1)[..., None]


def render(n):
    cfg = SCENES[n]
    src = Image.open(HERE / f"escena{n}.png").convert("RGB")
    # Upscale once so every crop is sampled from plenty of pixels (keeps motion smooth and sharp).
    big = src.resize((src.width * 3, src.height * 3), Image.LANCZOS)
    bw, bh = big.size
    parts, color, alpha, blur = make_particles(cfg["fx"], n)
    vig = vignette()
    shake = cfg.get("shake", 0)
    rng = random.Random(n)
    OUT.mkdir(exist_ok=True)
    proc = subprocess.Popen([FFMPEG, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                             "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                             "-pix_fmt", "yuv420p", str(OUT / f"escena{n}.mp4")], stdin=subprocess.PIPE)
    for f in range(FRAMES):
        t = ease(f / (FRAMES - 1))
        z = cfg["z"][0] + (cfg["z"][1] - cfg["z"][0]) * t
        (cx0, cy0), (cx1, cy1) = cfg["c"]
        cx, cy = (cx0 + (cx1 - cx0) * t) * bw, (cy0 + (cy1 - cy0) * t) * bh
        cw, ch = bw / z, bw / z * H / W
        if ch > bh:
            ch, cw = bh / z, bh / z * W / H
        if shake:
            cx += shake * 3 * math.sin(f * 1.7) + rng.uniform(-shake, shake)
            cy += shake * 3 * math.cos(f * 2.3) + rng.uniform(-shake, shake)
        x0 = min(max(cx - cw / 2, 0), bw - cw)
        y0 = min(max(cy - ch / 2, 0), bh - ch)
        frame = big.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch)).convert("RGBA")
        frame.alpha_composite(particle_layer(parts, color, alpha, blur, f))
        arr = np.asarray(frame.convert("RGB"), dtype=np.float32) * vig
        if cfg.get("flicker"):
            arr *= 0.94 + 0.06 * math.sin(f / 3.1) * math.sin(f / 7.3 + 1)
        fade = min(1.0, f / 9)  # quick fade-in
        if cfg.get("fade_out"):
            fade *= min(1.0, (FRAMES - 1 - f) / (cfg["fade_out"] * FPS))
        proc.stdin.write(np.clip(arr * fade, 0, 255).astype(np.uint8).tobytes())
    proc.stdin.close()
    proc.wait()
    print(f"escena {n}: {OUT / f'escena{n}.mp4'}", flush=True)


def join():
    lst = OUT / "lista.txt"
    lst.write_text("".join(f"file 'escena{n}.mp4'\n" for n in sorted(SCENES)))
    subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    str(OUT / "short_completo.mp4")], check=True)
    lst.unlink()
    print(f"short completo: {OUT / 'short_completo.mp4'}")


if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or sorted(SCENES):
        render(n)
    if all((OUT / f"escena{n}.mp4").exists() for n in SCENES):
        join()
