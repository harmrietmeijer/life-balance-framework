#!/usr/bin/env python3
"""
Generates docs/og-image.jpg for social media link previews.
Run via GitHub Actions on every push to main.
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys

W, H = 1200, 630
img = Image.new("RGB", (W, H), color=(15, 17, 23))
draw = ImageDraw.Draw(img)

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

f_huge  = load_font(FONT_BOLD, 92)
f_big   = load_font(FONT_BOLD, 58)
f_med   = load_font(FONT_BOLD, 36)
f_sm    = load_font(FONT_REG,  28)

# Top accent stripe
draw.rectangle([0, 0, W, 8], fill=(16, 185, 129))

# Main headline
draw.text((80, 110), "Life Balance Score Calculator", font=f_big,  fill=(255, 255, 255))
draw.text((80, 195), "Happy. Healthy. Wealthy.", font=f_huge, fill=(16, 185, 129))

# Subline
draw.text((80, 325), "Free 2-min quiz  ·  No signup  ·  Open Source (MIT)", font=f_sm, fill=(100, 116, 139))

# Three pillar pills
PILLARS = [
    ("Happy",   (16, 185, 129)),
    ("Healthy", (139, 92, 246)),
    ("Wealthy", (255, 106,   0)),
]
for i, (label, color) in enumerate(PILLARS):
    x = 80 + i * 240
    draw.rounded_rectangle([x, 395, x + 210, 462], radius=28, fill=(26, 29, 39), outline=color, width=2)
    draw.text((x + 24, 412), label, font=f_med, fill=color)

# Score circle (decorative)
cx, cy, r = 1010, 300, 118
draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(42, 45, 58), width=3)
draw.ellipse([cx-r+10, cy-r+10, cx+r-10, cy+r-10], outline=(16, 185, 129), width=4)
draw.text((cx - 48, cy - 58), "7.4", font=f_huge, fill=(16, 185, 129))
draw.text((cx - 60, cy + 44), "your score", font=f_sm, fill=(100, 116, 139))

# Footer branding
draw.text((80, 556), "nuvo.coach  ·  github.com/harmrietmeijer/life-balance-framework", font=f_sm, fill=(71, 85, 105))

# Output
out_path = os.path.join(os.path.dirname(__file__), "..", "docs", "og-image.jpg")
out_path = os.path.normpath(out_path)
img.save(out_path, "JPEG", quality=82, optimize=True)
size = os.path.getsize(out_path)
print(f"Saved {out_path} ({size:,} bytes)")
