#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news poster (1024x1024 PNG).

One image that sums up Thursday 19 November 2026: six verified stories,
each in its own panel with a short headline, plain factual text and a
simple drawn pictogram. Deterministic: fixed layout, no randomness, no
timestamps, no network, no external images.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

# ---- palette ------------------------------------------------------------
PAPER = (247, 245, 239)      # warm off-white
INK = (20, 24, 34)           # near-black
NAVY = (20, 33, 61)          # header
NAVY_LT = (38, 55, 96)
GOLD = (201, 162, 39)
RED = (178, 34, 34)
CARD = (255, 255, 255)
MUTED = (90, 96, 110)
LINE = (214, 210, 198)

ACCENTS = [
    (178, 34, 34),    # summit  - red
    (20, 33, 61),     # ICJ     - navy
    (46, 111, 143),   # bridge  - steel blue
    (34, 139, 92),    # IPO     - green
    (196, 110, 16),   # unrest  - orange
    (64, 90, 160),    # cyclone - indigo
]

# ---- fonts --------------------------------------------------------------
def font(path, size):
    return ImageFont.truetype(path, size)

F_TITLE = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
F_DATE = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
F_KICK = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 19)
F_HEAD = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25)
F_BODY = font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 19)
F_FOOT = font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

# ---- text helpers -------------------------------------------------------
def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

# ---- pictograms (simple drawn shapes, top-right of each panel) ---------
def pic_summit(d, x, y, c):
    # three leaders: three circles joined by lines
    pts = [(x + 12, y + 42), (x + 35, y + 14), (x + 58, y + 42)]
    d.line([pts[0], pts[1], pts[2], pts[0]], fill=c, width=4)
    for px, py in pts:
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=c)

def pic_scales(d, x, y, c):
    # scales of justice
    d.line([x + 35, y + 6, x + 35, y + 58], fill=c, width=4)
    d.line([x + 8, y + 16, x + 62, y + 16], fill=c, width=4)
    d.line([x + 8, y + 16, x + 4, y + 38], fill=c, width=3)
    d.line([x + 8, y + 16, x + 12, y + 38], fill=c, width=3)
    d.line([x + 62, y + 16, x + 58, y + 38], fill=c, width=3)
    d.line([x + 62, y + 16, x + 66, y + 38], fill=c, width=3)
    d.arc([x - 2, y + 34, x + 18, y + 52], 0, 180, fill=c, width=3)
    d.arc([x + 52, y + 34, x + 72, y + 52], 0, 180, fill=c, width=3)
    d.line([x + 20, y + 58, x + 50, y + 58], fill=c, width=4)

def pic_bridge(d, x, y, c):
    # arched bridge with a crack in the middle
    d.arc([x + 2, y + 14, x + 68, y + 66], 180, 360, fill=c, width=5)
    d.line([x + 2, y + 44, x + 68, y + 44], fill=c, width=4)
    d.line([x + 12, y + 44, x + 12, y + 30], fill=c, width=3)
    d.line([x + 58, y + 44, x + 58, y + 30], fill=c, width=3)
    d.line([x + 35, y + 12, x + 30, y + 22, x + 38, y + 30, x + 32, y + 40],
           fill=RED, width=3)
    d.line([x, y + 58, x + 70, y + 58], fill=c, width=3)

def pic_chart(d, x, y, c):
    # rising bars + arrow
    bars = [(x + 4, 46, 12), (x + 22, 34, 12), (x + 40, 20, 12)]
    for bx, bh, bw in bars:
        d.rectangle([bx, y + 58 - bh, bx + bw, y + 58], fill=c)
    d.line([x + 2, y + 12, x + 34, y + 2, x + 66, y + 6], fill=c, width=4)
    d.polygon([(x + 66, y + 6), (x + 54, y + 2), (x + 58, y + 14)], fill=c)

def pic_flame(d, x, y, c):
    # flame
    d.polygon([(x + 35, y + 2), (x + 52, y + 26), (x + 62, y + 42),
               (x + 52, y + 58), (x + 18, y + 58), (x + 8, y + 42),
               (x + 18, y + 26)], fill=c)
    d.polygon([(x + 35, y + 28), (x + 44, y + 40), (x + 40, y + 54),
               (x + 30, y + 54), (x + 26, y + 40)], fill=(255, 214, 120))

def pic_cyclone(d, x, y, c):
    # spiral
    for r, a0, a1 in [(30, 200, 380), (22, 140, 320), (14, 80, 260),
                      (7, 20, 200)]:
        d.arc([x + 35 - r, y + 32 - r, x + 35 + r, y + 32 + r],
              a0, a1, fill=c, width=4)
    d.ellipse([x + 31, y + 28, x + 39, y + 36], fill=c)

PICS = [pic_summit, pic_scales, pic_bridge, pic_chart, pic_flame, pic_cyclone]

# ---- stories ------------------------------------------------------------
STORIES = [
    ("DIPLOMACY", "Trump, Xi and Putin meet in Shenzhen",
     "The first-ever three-way summit, on the APEC sidelines. "
     "Bilaterals first (Trump\u2013Putin ~40 min, Trump\u2013Xi ~1 hr), "
     "then a joint session of ~80\u201390 min. Joint statement: reform "
     "the UN, boost refined-oil supply, \u201ca nuclear war cannot be "
     "won and must never be fought\u201d."),
    ("THE HAGUE", "ICJ: Myanmar guilty of genocide",
     "The court ruled Myanmar acted with genocidal intent against the "
     "Rohingya in the 2017 crackdown: ~10,000 killed, 730,000+ fled to "
     "Bangladesh. 9 votes to 6 \u2014 the first time in the ICJ\u2019s "
     "80-year history it has held a state accountable for genocide."),
    ("UKRAINE", "Crimean Bridge hit a third time",
     "Overnight 18\u201319 Nov, Ukraine struck the Crimean Bridge again "
     "\u2014 the third strike in a week. Russian-installed head Sergei "
     "Aksyonov confirmed it; traffic, including rail, was halted. "
     "Follows the 17 Nov strike that collapsed a road arch."),
    ("MARKETS", "Anthropic debuts in record IPO",
     "Anthropic shares (ANT) began trading on Nasdaq, priced at $83 "
     "on 18 Nov \u2014 above the $70\u201378 range. 980 million shares, "
     "about $81.3bn: the largest IPO on record."),
    ("BANGLADESH", "Lockdown call as unrest spreads",
     "The banned Awami League called a lockdown. Muhammad Yunus\u2019s "
     "ancestral home in Chattogram was set ablaze; police said two "
     "ruling-party members were killed; violence in 28 of 64 "
     "districts; 97 Border Guard platoons deployed."),
    ("WEATHER", "Cyclone Akvan nears India\u2019s coast",
     "Severe Cyclone Akvan bore down on India\u2019s east coast. Odisha "
     "evacuated over 72,000 people to shelters; schools shut in six "
     "districts. Landfall expected Fri 20 Nov near Gopalpur, winds "
     "90\u2013100 km/h, gusting to 110."),
]

FOOTER_LINES = [
    "Sources: USA Today \u00b7 NPR \u00b7 The Times \u00b7 NY Post \u00b7 CNN \u00b7 Reuters \u00b7 BBC \u00b7 Meduza",
    "Deutsche Welle \u00b7 Anthropic \u00b7 CNBC/AP \u00b7 Nasdaq \u00b7 IMD \u00b7 ANI/PTI",
]

# ---- draw ---------------------------------------------------------------
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # header band
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 124], fill=GOLD)
    d.text((24, 14), "THE WORLD IN ONE DAY", font=F_TITLE, fill=(255, 255, 255))
    d.text((24, 68), "Thursday 19 November 2026", font=F_DATE, fill=GOLD)
    d.text((W - 24 - d.textlength("6 STORIES  \u00b7  1 DAY", font=F_KICK),
            76), "6 STORIES  \u00b7  1 DAY", font=F_KICK, fill=(200, 208, 224))

    # story panels: 2 columns x 3 rows
    px0, py0 = 24, 140
    pw, ph, gap = 476, 268, 16
    for i, (tag, head, body) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = px0 + col * (pw + gap)
        y = py0 + row * (ph + gap)
        accent = ACCENTS[i]

        d.rectangle([x, y, x + pw, y + ph], fill=CARD, outline=LINE, width=2)
        d.rectangle([x, y, x + 8, y + ph], fill=accent)

        # tag chip + pictogram (pictogram drawn on a tile, scaled to 46px
        # so it never collides with the headline below it)
        tag_w = d.textlength(tag, font=F_KICK) + 18
        d.rounded_rectangle([x + 20, y + 16, x + 20 + tag_w, y + 44],
                            radius=6, fill=accent)
        d.text((x + 29, y + 20), tag, font=F_KICK, fill=(255, 255, 255))
        tile = Image.new("RGBA", (72, 72), (0, 0, 0, 0))
        td = ImageDraw.Draw(tile)
        PICS[i](td, 0, 0, accent)
        tile = tile.resize((46, 46), Image.LANCZOS)
        img.paste(tile, (x + pw - 64, y + 8), tile)

        # headline (wraps within width minus pictogram zone on line 1)
        head_lines = wrap(d, head, F_HEAD, pw - 40)
        hy = y + 52
        for line in head_lines:
            d.text((x + 20, hy), line, font=F_HEAD, fill=INK)
            hy += 28

        # body
        body_lines = wrap(d, body, F_BODY, pw - 40)
        by = hy + 6
        for line in body_lines:
            d.text((x + 20, by), line, font=F_BODY, fill=(52, 58, 72))
            by += 24

    # footer (two short lines, centred)
    fy = H - 42
    for line in FOOTER_LINES:
        d.text(((W - d.textlength(line, font=F_FOOT)) / 2, fy),
               line, font=F_FOOT, fill=MUTED)
        fy += 19

    img.save(OUT, format="PNG", optimize=True)

if __name__ == "__main__":
    main()
    print("wrote", OUT)
