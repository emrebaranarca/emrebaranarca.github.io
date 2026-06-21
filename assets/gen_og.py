"""Generate the social-share card (og.png, 1200x630)."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent / "og.png"
PORTRAIT = Path(__file__).parent / "portrait.jpg"

W, H = 1200, 630
BG = (244, 241, 234)
INK = (27, 25, 22)
MUTED = (111, 104, 91)
FAINT = (156, 148, 132)
LINE = (221, 214, 200)
ACCENT = (214, 69, 31)

GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"
GEORGIA_IT = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
HELV = "/System/Library/Fonts/HelveticaNeue.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"

def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# top mono lockup: accent square + name / role
SQ = 22
PAD_X = 72
PAD_TOP = 64

d.rectangle([PAD_X, PAD_TOP, PAD_X + SQ, PAD_TOP + SQ], fill=ACCENT)

f_mono_md = font(MENLO, 22)
d.text((PAD_X + SQ + 16, PAD_TOP - 1), "Emre Baran Arca", fill=INK, font=f_mono_md)
name_w = d.textlength("Emre Baran Arca", font=f_mono_md)
d.text((PAD_X + SQ + 16 + name_w + 12, PAD_TOP - 1), "/ software-engineer", fill=FAINT, font=f_mono_md)

# eyebrow
f_mono_sm = font(MENLO, 19)
d.text((PAD_X, 178), "FULL-STACK SOFTWARE ENGINEER", fill=ACCENT, font=f_mono_sm)

# main serif headline (two lines)
f_serif_xl = font(GEORGIA, 116)
d.text((PAD_X - 6, 218), "Emre Baran", fill=INK, font=f_serif_xl)
d.text((PAD_X - 6, 338), "Arca", fill=INK, font=f_serif_xl)
arca_w = d.textlength("Arca", font=f_serif_xl)
# accent dot
d.text((PAD_X - 6 + arca_w, 338), ".", fill=ACCENT, font=f_serif_xl)

# italic tagline
f_serif_it = font(GEORGIA_IT, 28)
tagline = "I design systems, write the code, and treat software"
tagline2 = "as something worth crafting."
d.text((PAD_X - 2, 480), tagline, fill=MUTED, font=f_serif_it)
d.text((PAD_X - 2, 520), tagline2, fill=MUTED, font=f_serif_it)

# bottom meta line
META_Y = H - 64
d.line([(PAD_X, META_Y - 22), (W - PAD_X, META_Y - 22)], fill=LINE, width=1)
f_meta = font(MENLO, 18)
d.text((PAD_X, META_Y - 8), "emrebaranarca.github.io", fill=FAINT, font=f_meta)
right_text = "Node.js  ·  NestJS  ·  gRPC  ·  AWS"
right_w = d.textlength(right_text, font=f_meta)
d.text((W - PAD_X - right_w, META_Y - 8), right_text, fill=FAINT, font=f_meta)

# portrait on the right — circular mask, slightly inset
if PORTRAIT.exists():
    p = Image.open(PORTRAIT).convert("RGB")
    # square crop
    ps = min(p.size)
    left = (p.width - ps) // 2
    top = max(0, (p.height - ps) // 2 - int(ps * 0.06))
    p = p.crop((left, top, left + ps, top + ps))
    size = 280
    p = p.resize((size, size), Image.LANCZOS)
    # circular mask
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size, size], fill=255)
    px = W - PAD_X - size + 12
    py = 198
    # subtle accent ring offset
    ring = Image.new("RGBA", (size + 24, size + 24), (0, 0, 0, 0))
    rd = ImageDraw.Draw(ring)
    rd.ellipse([12, 12, size + 12, size + 12], outline=ACCENT, width=2)
    img.paste(ring, (px - 12 + 14, py - 12 + 14), ring)
    img.paste(p, (px, py), mask)

img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}, {OUT.stat().st_size // 1024} KB")
