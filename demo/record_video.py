#!/usr/bin/env python3
"""Record Perseus AMD Agent demo video via Playwright + FFmpeg."""

import os, sys, time, subprocess, threading
import http.server, socketserver
from pathlib import Path
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
VIDEO_DIR = SCRIPT_DIR / "video_output"
OUTPUT_VIDEO = SCRIPT_DIR / "demo_video.mp4"
TOTAL_DURATION = 165  # 2:45

VIDEO_DIR.mkdir(parents=True, exist_ok=True)
for f in VIDEO_DIR.glob("*"):
    f.unlink()

os.chdir(str(SCRIPT_DIR))

# Start HTTP server
httpd = socketserver.TCPServer(("", 9878), http.server.SimpleHTTPRequestHandler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()
print("HTTP server on :9878")

print(f"Recording {TOTAL_DURATION}s...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 1280, "height": 720},
    )
    page = context.new_page()
    page.goto("http://localhost:9878/demo_terminal.html", wait_until="domcontentloaded", timeout=15000)

    # Verify JS is running
    time.sleep(4)
    screen_text = page.inner_text("#screen")
    print(f"Screen content: {len(screen_text)} chars — {'OK' if len(screen_text) > 50 else 'EMPTY! Check JS'}")

    time.sleep(TOTAL_DURATION)
    context.close()
    browser.close()
    httpd.shutdown()

# Convert to MP4
webm_files = list(VIDEO_DIR.glob("*.webm"))
if not webm_files:
    print("ERROR: No WebM")
    sys.exit(1)

webm_path = webm_files[0]
print(f"WebM: {webm_path.stat().st_size / 1024:.0f} KB")

subprocess.run([
    "ffmpeg", "-y", "-i", str(webm_path),
    "-c:v", "libx264", "-preset", "fast", "-crf", "23",
    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
    str(OUTPUT_VIDEO),
], capture_output=True, timeout=120, check=True)

size_kb = OUTPUT_VIDEO.stat().st_size / 1024
print(f"MP4: {OUTPUT_VIDEO} ({size_kb:.0f} KB)")

# Verify duration
result = subprocess.run([
    "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
    "-of", "csv=p=0", str(OUTPUT_VIDEO),
], capture_output=True, text=True)
duration = float(result.stdout.strip())
print(f"Duration: {duration:.1f}s ({duration/60:.1f} min)")

# Extract check frames
for ss, name in [(30, "f1_problem"), (70, "f2_context"), (105, "f3_memory"), (140, "f4_benchmarks")]:
    subprocess.run([
        "ffmpeg", "-y", "-i", str(OUTPUT_VIDEO),
        "-ss", str(ss), "-vframes", "1",
        str(SCRIPT_DIR / f"{name}.png"),
    ], capture_output=True, timeout=10)

print("Done — check f1_problem.png through f4_benchmarks.png")
