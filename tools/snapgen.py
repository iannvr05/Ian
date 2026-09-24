"""Small SnapGen AI client used to make history Shorts.

The API key is NOT in this file: the cloud environment injects it as the `x-api-key` header for api.snapgen.ai
(credential configured in the environment settings). Nothing here needs the key.

Usage:
  python3 tools/snapgen.py credits
  python3 tools/snapgen.py image  <out.png> <prompt.txt> [reference.png ...]
  python3 tools/snapgen.py video  <out.mp4> <prompt.txt> <first_frame.png>

Each command submits ONE job, waits for it, downloads the result and prints the credits used.
Failed jobs (rate limit / timeout) are not charged; the command prints the error and exits 1.
"""
import json
import subprocess
import sys
import time

API = "https://api.snapgen.ai/uapi/v1"


def curl(*args):
    return json.loads(subprocess.run(["curl", "-sS", *args], capture_output=True, text=True).stdout)


def credits():
    c = curl(f"{API}/account")["user_credit"]
    print(f"disponibles: {c['available_credit']}  bloqueados: {c['locked_credit']}")


def wait(uuid, every=10):
    t0 = time.time()
    while True:
        time.sleep(every)
        d = curl(f"{API}/history/{uuid}")
        if d["status"] in (2, 3):  # 2 = done, 3 = failed
            return d, (time.time() - t0) / 60


def submit(endpoint, fields, files):
    args = ["-X", "POST"]
    for k, v in fields.items():
        args += ["-F", f"{k}={v}"]
    for f in files:
        args += ["-F", f"files=@{f}"]
    r = curl(*args, f"{API}/{endpoint}")
    if "uuid" not in r:
        sys.exit(f"rechazado: {r}")
    print(f"enviado {r['uuid']} ({r.get('estimated_credit')} créditos estimados)", flush=True)
    return r["uuid"]


def image(out, prompt_file, *refs):
    fields = {"prompt": open(prompt_file).read().strip(), "model": "nano-banana-2",
              "aspect_ratio": "9:16", "resolution": "1K"}
    d, mins = wait(submit("generate_image", fields, refs), every=8)
    finish(d, mins, out, d.get("generated_image"), "image_url")


def video(out, prompt_file, first_frame):
    fields = {"prompt": open(prompt_file).read().strip(), "model": "veo-3.1-fast", "mode_image": "frame",
              "aspect_ratio": "9:16", "resolution": "1080p"}
    d, mins = wait(submit("video-gen/veo", fields, [first_frame]), every=15)
    finish(d, mins, out, d.get("generated_video"), "video_url")


def finish(d, mins, out, items, key):
    if d["status"] != 2:
        sys.exit(f"fallo {d['error_code']} tras {mins:.0f} min (no cobrado)")
    subprocess.run(["curl", "-sS", "-o", out, items[0][key]], check=True)
    print(f"OK {out} ({d['used_credit']} créditos, {mins:.0f} min)")


if __name__ == "__main__":
    cmd, *rest = sys.argv[1:]
    {"credits": credits, "image": image, "video": video}[cmd](*rest)
