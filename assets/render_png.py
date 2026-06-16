#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
from pathlib import Path

html_path = Path("/tmp/perseus-amd-agent/assets/architecture.html")
png_path = Path("/tmp/perseus-amd-agent/assets/thumbnail.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1400, "height": 1050})
    page.goto(f"file://{html_path}", wait_until="networkidle")
    page.screenshot(path=str(png_path), full_page=True)
    browser.close()

size = png_path.stat().st_size
print(f"✅ Thumbnail rendered: {png_path} ({size:,} bytes)")

# Verify
with open(png_path, 'rb') as f:
    header = f.read(8)
    assert header[:4] == b'\x89PNG', "Not valid"
    print(f"   Valid PNG")
