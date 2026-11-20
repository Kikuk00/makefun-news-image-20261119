#!/usr/bin/env python3
"""Generate entry.png for make.fun news-image-20261119.

Stdlib only. Draws a 1024x1024 newspaper front page with a 5x7 bitmap
font, flat vector illustrations, and writes PNG bytes via zlib/struct.
"""
import struct
import zlib

W, H = 1024, 1024

# ---------------------------------------------------------------- font ----
# 5x7 bitmap font: each glyph is 7 rows of 5 bits, top to bottom.
F = {}


def _g(ch, rows):
    F[ch] = [int(r, 2) for r in rows]


_g("A", ["01110", "10001", "10001", "11111", "10001", "10001", "10001"])
_g("B", ["11110", "10001", "10001", "11110", "10001", "10001", "11110"])
_g("C", ["01110", "10001", "10000", "10000", "10000", "10001", "01110"])
_g("D", ["11110", "10001", "10001", "10001", "10001", "10001", "11110"])
_g("E", ["11111", "10000", "10000", "11110", "10000", "10000", "11111"])
_g("F", ["11111", "10000", "10000", "11110", "10000", "10000", "10000"])
_g("G", ["01110", "10001", "10000", "10111", "10001", "10001", "01111"])
_g("H", ["10001", "10001", "10001", "11111", "10001", "10001", "10001"])
_g("I", ["01110", "00100", "00100", "00100", "00100", "00100", "01110"])
_g("J", ["00111", "00010", "00010", "00010", "00010", "10010", "01100"])
_g("K", ["10001", "10010", "10100", "11000", "10100", "10010", "10001"])
_g("L", ["10000", "10000", "10000", "10000", "10000", "10000", "11111"])
_g("M", ["10001", "11011", "10101", "10101", "10001", "10001", "10001"])
_g("N", ["10001", "11001", "10101", "10011", "10001", "10001", "10001"])
_g("O", ["01110", "10001", "10001", "10001", "10001", "10001", "01110"])
_g("P", ["11110", "10001", "10001", "11110", "10000", "10000", "10000"])
_g("Q", ["01110", "10001", "10001", "10001", "10101", "10010", "01101"])
_g("R", ["11110", "10001", "10001", "11110", "10100", "10010", "10001"])
_g("S", ["01111", "10000", "10000", "01110", "00001", "00001", "11110"])
_g("T", ["11111", "00100", "00100", "00100", "00100", "00100", "00100"])
_g("U", ["10001", "10001", "10001", "10001", "10001", "10001", "01110"])
_g("V", ["10001", "10001", "10001", "10001", "10001", "01010", "00100"])
_g("W", ["10001", "10001", "10001", "10101", "10101", "10101", "01010"])
_g("X", ["10001", "10001", "01010", "00100", "01010", "10001", "10001"])
_g("Y", ["10001", "10001", "01010", "00100", "00100", "00100", "00100"])
_g("Z", ["11111", "00001", "00010", "00100", "01000", "10000", "11111"])
_g("0", ["01110", "10001", "10011", "10101", "11001", "10001", "01110"])
_g("1", ["00100", "01100", "00100", "00100", "00100", "00100", "01110"])
_g("2", ["01110", "10001", "00001", "00110", "01000", "10000", "11111"])
_g("3", ["11111", "00010", "00100", "00010", "00001", "10001", "01110"])
_g("4", ["00010", "00110", "01010", "10010", "11111", "00010", "00010"])
_g("5", ["11111", "10000", "11110", "00001", "00001", "10001", "01110"])
_g("6", ["00110", "01000", "10000", "11110", "10001", "10001", "01110"])
_g("7", ["11111", "00001", "00010", "00100", "01000", "01000", "01000"])
_g("8", ["01110", "10001", "10001", "01110", "10001", "10001", "01110"])
_g("9", ["01110", "10001", "10001", "01111", "00001", "00010", "01100"])
_g("a", ["00000", "00000", "01110", "00001", "01111", "10001", "01111"])
_g("b", ["10000", "10000", "10110", "11001", "10001", "10001", "11110"])
_g("c", ["00000", "00000", "01110", "10000", "10000", "10001", "01110"])
_g("d", ["00001", "00001", "01101", "10011", "10001", "10001", "01111"])
_g("e", ["00000", "00000", "01110", "10001", "11111", "10000", "01110"])
_g("f", ["00110", "01001", "01000", "11110", "01000", "01000", "01000"])
_g("g", ["00000", "00000", "01111", "10001", "10001", "01111", "00001", "01110"][:7])
_g("h", ["10000", "10000", "10110", "11001", "10001", "10001", "10001"])
_g("i", ["00100", "00000", "01100", "00100", "00100", "00100", "01110"])
_g("j", ["00010", "00000", "00110", "00010", "00010", "10010", "01100"])
_g("k", ["10000", "10000", "10010", "10100", "11000", "10100", "10010"])
_g("l", ["01100", "00100", "00100", "00100", "00100", "00100", "01110"])
_g("m", ["00000", "00000", "11010", "10101", "10101", "10101", "10101"])
_g("n", ["00000", "00000", "10110", "11001", "10001", "10001", "10001"])
_g("o", ["00000", "00000", "01110", "10001", "10001", "10001", "01110"])
_g("p", ["00000", "00000", "11110", "10001", "11110", "10000", "10000"])
_g("q", ["00000", "00000", "01101", "10011", "10001", "01111", "00001"])
_g("r", ["00000", "00000", "10110", "11001", "10000", "10000", "10000"])
_g("s", ["00000", "00000", "01111", "10000", "01110", "00001", "11110"])
_g("t", ["01000", "01000", "11110", "01000", "01000", "01001", "00110"])
_g("u", ["00000", "00000", "10001", "10001", "10001", "10011", "01101"])
_g("v", ["00000", "00000", "10001", "10001", "10001", "01010", "00100"])
_g("w", ["00000", "00000", "10001", "10101", "10101", "10101", "01010"])
_g("x", ["00000", "00000", "10001", "01010", "00100", "01010", "10001"])
_g("y", ["00000", "00000", "10001", "10001", "01111", "00001", "01110"])
_g("z", ["00000", "00000", "11111", "00010", "00100", "01000", "11111"])
_g(" ", ["00000", "00000", "00000", "00000", "00000", "00000", "00000"])
_g(".", ["00000", "00000", "00000", "00000", "00000", "01100", "01100"])
_g(",", ["00000", "00000", "00000", "00000", "01100", "00100", "01000"])
_g("-", ["00000", "00000", "00000", "01110", "00000", "00000", "00000"])
_g("–", ["00000", "00000", "00000", "01110", "00000", "00000", "00000"])
_g("—", ["00000", "00000", "00000", "11111", "00000", "00000", "00000"])
_g(":", ["00000", "01100", "01100", "00000", "01100", "01100", "00000"])
_g(";", ["00000", "01100", "01100", "00000", "01100", "00100", "01000"])
_g("'", ["00100", "00100", "01000", "00000", "00000", "00000", "00000"])
_g("’", ["00100", "00100", "01000", "00000", "00000", "00000", "00000"])
_g('"', ["01010", "01010", "01010", "00000", "00000", "00000", "00000"])
_g("“", ["01010", "01010", "01010", "00000", "00000", "00000", "00000"])
_g("”", ["01010", "01010", "01010", "00000", "00000", "00000", "00000"])
_g("!", ["00100", "00100", "00100", "00100", "00100", "00000", "00100"])
_g("?", ["01110", "10001", "00001", "00110", "00100", "00000", "00100"])
_g("(", ["00010", "00100", "01000", "01000", "01000", "00100", "00010"])
_g(")", ["01000", "00100", "00010", "00010", "00010", "00100", "01000"])
_g("/", ["00001", "00010", "00010", "00100", "01000", "01000", "10000"])
_g("%", ["11001", "11010", "00010", "00100", "01000", "01011", "10011"])
_g("&", ["01100", "10010", "10100", "01000", "10101", "10010", "01101"])
_g("$", ["00100", "01111", "10100", "01110", "00101", "11110", "00100"])
_g("+", ["00000", "00100", "00100", "11111", "00100", "00100", "00000"])
_g("=", ["00000", "00000", "11111", "00000", "11111", "00000", "00000"])
_g("*", ["00000", "10101", "01110", "10101", "00000", "00000", "00000"])
_g("#", ["01010", "01010", "11111", "01010", "11111", "01010", "01010"])
_g("•", ["00000", "00000", "00100", "01110", "01110", "00100", "00000"])
_g("@", ["01110", "10001", "10111", "10101", "10110", "10000", "01110"])
_g("_", ["00000", "00000", "00000", "00000", "00000", "00000", "11111"])


def text_width(s, scale):
    adv = 5 * scale + max(1, scale // 2)
    return len(s) * adv - max(1, scale // 2)


def wrap_text(s, scale, max_w):
    """Greedy word wrap; returns list of lines."""
    adv = 5 * scale + max(1, scale // 2)
    lines = []
    for para in s.split("\n"):
        words = para.split(" ")
        cur = ""
        for w in words:
            trial = w if not cur else cur + " " + w
            if len(trial) * adv - max(1, scale // 2) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


# -------------------------------------------------------------- canvas ----
class Canvas:
    def __init__(self, w, h, bg):
        self.w, self.h = w, h
        self.px = bytearray(bg) * (w * h)

    def set(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            self.px[i:i + 3] = c

    def rect(self, x, y, w, h, c):
        x0, y0 = max(0, x), max(0, y)
        x1, y1 = min(self.w, x + w), min(self.h, y + h)
        for yy in range(y0, y1):
            i = (yy * self.w + x0) * 3
            self.px[i:i + (x1 - x0) * 3] = bytes(c) * (x1 - x0)

    def border(self, x, y, w, h, c, t=2):
        self.rect(x, y, w, t, c)
        self.rect(x, y + h - t, w, t, c)
        self.rect(x, y, t, h, c)
        self.rect(x + w - t, y, t, h, c)

    def line(self, x0, y0, x1, y1, c, t=1):
        dx, dy = abs(x1 - x0), abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while True:
            for a in range(t):
                for b in range(t):
                    self.set(x0 + a, y0 + b, c)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def circle(self, cx, cy, r, c, fill=True):
        for yy in range(cy - r, cy + r + 1):
            for xx in range(cx - r, cx + r + 1):
                d = (xx - cx) ** 2 + (yy - cy) ** 2
                if fill:
                    if d <= r * r:
                        self.set(xx, yy, c)
                else:
                    if abs(d - r * r) <= r:
                        self.set(xx, yy, c)

    def ellipse(self, cx, cy, rx, ry, c):
        for yy in range(cy - ry, cy + ry + 1):
            for xx in range(cx - rx, cx + rx + 1):
                if ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1:
                    self.set(xx, yy, c)

    def triangle(self, pts, c):
        (x0, y0), (x1, y1), (x2, y2) = pts
        ymin, ymax = min(y0, y1, y2), max(y0, y1, y2)
        for yy in range(ymin, ymax + 1):
            xs = []
            for (xa, ya), (xb, yb) in (((x0, y0), (x1, y1)),
                                       ((x1, y1), (x2, y2)),
                                       ((x2, y2), (x0, y0))):
                if ya == yb:
                    continue
                if min(ya, yb) <= yy < max(ya, yb):
                    xs.append(xa + (yy - ya) * (xb - xa) / (yb - ya))
            if len(xs) >= 2:
                for xx in range(int(min(xs)), int(max(xs)) + 1):
                    self.set(xx, yy, c)

    def text(self, x, y, s, scale, c):
        sp = max(1, scale // 2)
        cx = x
        for ch in s:
            g = F.get(ch)
            if g is None:
                cx += 5 * scale + sp
                continue
            for r in range(7):
                bits = g[r]
                for col in range(5):
                    if bits >> (4 - col) & 1:
                        self.rect(cx + col * scale, y + r * scale,
                                  scale, scale, c)
            cx += 5 * scale + sp
        return cx

    def text_center(self, y, s, scale, c):
        x = (self.w - text_width(s, scale)) // 2
        return self.text(x, y, s, scale, c)


# ----------------------------------------------------------------- PNG ----
def write_png(cv, path):
    raw = b"".join(b"\x00" + bytes(cv.px[y * cv.w * 3:(y + 1) * cv.w * 3])
                   for y in range(cv.h))
    comp = zlib.compress(raw, 9)

    def chunk(typ, data):
        c = struct.pack(">I", len(data)) + typ + data
        return c + struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", cv.w, cv.h, 8, 2, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", comp) + chunk(b"IEND", b""))
    with open(path, "wb") as f:
        f.write(png)
    return len(png)


# -------------------------------------------------------------- palette ---
PAPER = bytes([247, 243, 234])
INK = bytes([20, 20, 20])
BLACK = bytes([0, 0, 0])
WHITE = bytes([255, 255, 255])
RED = bytes([164, 20, 20])
NAVY = bytes([18, 38, 68])
GREY = bytes([90, 90, 90])
PANEL_BG = bytes([255, 255, 255])
RULE = bytes([60, 60, 60])

SKIN1 = bytes([232, 190, 150])
SKIN2 = bytes([205, 160, 120])
SKIN3 = bytes([240, 205, 170])
HAIR_D = bytes([60, 45, 35])
HAIR_G = bytes([180, 180, 180])
HAIR_B = bytes([40, 40, 40])
SUIT_N = bytes([30, 50, 90])
SUIT_R = bytes([120, 30, 30])
SUIT_G = bytes([50, 70, 60])
TABLE = bytes([140, 95, 50])
WOOD = bytes([120, 80, 40])

# --------------------------------------------------------- illustrations --
def ill_summit(cv, x, y, w, h):
    cv.rect(x, y, w, h, bytes([216, 232, 244]))          # sky
    cv.rect(x, y + h - 26, w, 26, bytes([190, 205, 190]))  # floor
    # three leaders behind a table
    xs = [x + w // 4, x + w // 2, x + 3 * w // 4]
    skins = [SKIN1, SKIN2, SKIN3]
    hairs = [HAIR_B, HAIR_G, HAIR_D]
    suits = [SUIT_N, SUIT_R, SUIT_G]
    for cx, sk, hr, st in zip(xs, skins, hairs, suits):
        cv.rect(cx - 6, y + 38, 12, 16, sk)             # neck
        cv.rect(cx - 26, y + 52, 52, 30, st)             # shoulders
        cv.circle(cx, y + 34, 17, sk)                    # head
        cv.circle(cx, y + 22, 17, hr)                    # hair cap
        cv.rect(cx - 17, y + 26, 34, 14, sk)             # face lower
        cv.rect(cx - 3, y + 52, 6, 26, WHITE)            # shirt
        cv.triangle([(cx - 5, y + 54), (cx + 5, y + 54),
                     (cx, y + 66)], RED)                 # tie
    cv.rect(x + 40, y + 78, w - 80, 10, TABLE)           # table top
    cv.rect(x + 40, y + 88, w - 80, 18, WOOD)            # table front
    # three small flags on the table
    for i, (fx, col) in enumerate([(x + 90, bytes([180, 30, 30])),
                                   (x + w // 2 - 6, bytes([200, 40, 40])),
                                   (x + w - 110, bytes([220, 220, 220]))]):
        cv.rect(fx, y + 56, 3, 22, BLACK)
        cv.rect(fx + 3, y + 56, 20, 12, col)


def ill_court(cv, x, y, w, h):
    cv.rect(x, y, w, h, bytes([238, 228, 205]))
    # steps
    cv.rect(x + 60, y + 88, w - 120, 6, bytes([150, 140, 120]))
    cv.rect(x + 70, y + 82, w - 140, 6, bytes([165, 155, 135]))
    # columns
    for cx in (x + 100, x + 190, x + w - 210, x + w - 120):
        cv.rect(cx, y + 34, 16, 50, WHITE)
        cv.rect(cx - 3, y + 30, 22, 5, bytes([200, 190, 170]))
        cv.rect(cx - 3, y + 83, 22, 5, bytes([200, 190, 170]))
    # pediment
    cv.triangle([(x + 70, y + 30), (x + w - 70, y + 30),
                 (x + w // 2, y + 6)], bytes([190, 175, 150]))
    cv.circle(x + w // 2, y + 20, 6, NAVY)
    # scales of justice in the pediment centre
    cv.line(x + w // 2, y + 14, x + w // 2, y + 28, NAVY, 2)


def ill_bridge(cv, x, y, w, h):
    cv.rect(x, y, w, h, bytes([210, 224, 232]))          # sky
    cv.rect(x, y + 82, w, h - 82, bytes([70, 120, 160]))  # water
    # deck, broken in the middle
    cv.rect(x + 20, y + 62, 170, 10, bytes([120, 120, 125]))
    cv.rect(x + w - 190, y + 62, 170, 10, bytes([120, 120, 125]))
    # tilted broken ends
    cv.line(x + 190, y + 62, x + 215, y + 80, bytes([120, 120, 125]), 8)
    cv.line(x + w - 190, y + 62, x + w - 215, y + 80,
            bytes([120, 120, 125]), 8)
    # pillars
    cv.rect(x + 60, y + 72, 12, 22, bytes([100, 100, 105]))
    cv.rect(x + w - 72, y + 72, 12, 22, bytes([100, 100, 105]))
    # arch
    cv.line(x + 40, y + 62, x + w // 2 - 30, y + 30, bytes([90, 90, 95]), 4)
    cv.line(x + w - 40, y + 62, x + w // 2 + 30, y + 30,
            bytes([90, 90, 95]), 4)
    # smoke over the gap
    for cx, cy, r in ((x + w // 2 - 14, y + 26, 12),
                      (x + w // 2 + 8, y + 16, 14),
                      (x + w // 2 + 22, y + 30, 10)):
        cv.circle(cx, cy, r, bytes([120, 120, 120]))
    # blast star
    cv.circle(x + w // 2, y + 62, 8, bytes([255, 170, 40]))


def ill_tank(cv, x, y, w, h):
    cv.rect(x, y, w, h, bytes([236, 227, 207]))          # sand
    cv.rect(x, y + 88, w, 18, bytes([190, 175, 140]))     # ground
    # barrel
    cv.line(x + w // 2 + 30, y + 40, x + w - 30, y + 26,
            bytes([70, 80, 60]), 7)
    # turret
    cv.rect(x + w // 2 - 30, y + 30, 70, 26, bytes([85, 95, 70]))
    cv.rect(x + w // 2 - 20, y + 22, 40, 10, bytes([85, 95, 70]))
    # hull
    cv.rect(x + 90, y + 56, w - 190, 30, bytes([100, 110, 80]))
    cv.rect(x + 90, y + 56, w - 190, 6, bytes([120, 130, 95]))
    # wheels
    for cx in range(x + 120, x + w - 100, 42):
        cv.circle(cx, y + 80, 11, bytes([50, 50, 45]))
        cv.circle(cx, y + 80, 5, bytes([160, 160, 150]))
    # dust
    for cx, cy, r in ((x + 70, y + 84, 8), (x + 92, y + 78, 6),
                      (x + w - 70, y + 82, 7)):
        cv.circle(cx, cy, r, bytes([210, 195, 160]))


def ill_tower(cv, x, y, w, h):
    cv.rect(x, y, w, h, bytes([242, 227, 216]))          # dusk
    # PIF tower: stepped skyscraper
    tx = x + w // 2 - 120
    cv.rect(tx, y + 30, 90, 76, bytes([70, 90, 120]))
    cv.rect(tx + 90, y + 48, 60, 58, bytes([90, 110, 140]))
    cv.rect(tx + 150, y + 66, 44, 40, bytes([110, 130, 155]))
    cv.triangle([(tx, y + 30), (tx + 90, y + 30), (tx + 45, y + 8)],
                bytes([70, 90, 120]))
    # windows
    for wy in range(y + 40, y + 100, 12):
        for wx in range(tx + 10, tx + 80, 16):
            cv.rect(wx, wy, 7, 6, bytes([255, 220, 120]))
    # impact flash on the tower
    cv.circle(tx + 45, y + 52, 12, bytes([255, 150, 40]))
    cv.circle(tx + 45, y + 52, 6, bytes([255, 230, 120]))
    # missile streaking in from top right
    cv.line(x + w - 40, y + 8, x + w - 130, y + 40, bytes([200, 60, 30]), 6)
    cv.triangle([(x + w - 132, y + 34), (x + w - 118, y + 28),
                 (x + w - 122, y + 48)], bytes([200, 60, 30]))
    cv.line(x + w - 36, y + 6, x + w - 8, y - 2, bytes([255, 180, 80]), 4)
    # ground
    cv.rect(x, y + h - 6, w, 6, bytes([180, 160, 140]))


def ill_chart(cv, x, y, w, h):
    cv.rect(x, y, w, h, bytes([223, 240, 221]))          # light green
    # bars rising
    bw, gap = 34, 18
    heights = [18, 30, 26, 44, 38, 56, 66]
    bx = x + 60
    for ht in heights:
        cv.rect(bx, y + h - 22 - ht, bw, ht, bytes([60, 140, 90]))
        bx += bw + gap
    # trend line with arrow
    pts = [(x + 66, y + h - 30), (x + 130, y + 66), (x + 195, y + 72),
           (x + 258, y + 46), (x + 322, y + 52), (x + 386, y + 26),
           (x + 430, y + 18)]
    for a, b in zip(pts, pts[1:]):
        cv.line(a[0], a[1], b[0], b[1], NAVY, 4)
    cv.triangle([(x + 430, y + 18), (x + 408, y + 14), (x + 420, y + 34)],
                NAVY)
    # axis
    cv.line(x + 40, y + 12, x + 40, y + h - 22, INK, 3)
    cv.line(x + 40, y + h - 22, x + w - 20, y + h - 22, INK, 3)
    # dollar sign
    cv.text(x + w - 52, y + 12, "$", 3, bytes([30, 110, 60]))


# ---------------------------------------------------------------- stories --
STORIES = [
    ("FIRST US\u2013CHINA\u2013RUSSIA SUMMIT IN SHENZHEN",
     "Trump, Xi and Putin meet for 90 minutes at APEC and issue a joint "
     "peace declaration on nuclear risks.",
     ill_summit),
    ("MYANMAR GUILTY OF ROHINGYA GENOCIDE",
     "The UN's top court rules Myanmar committed state-sponsored genocide; "
     "about 10,000 Rohingya were killed.",
     ill_court),
    ("KERCH BRIDGE HIT FOR A THIRD TIME",
     "Ukraine strikes the Crimean Bridge again; rail traffic halts as "
     "Russian strikes kill at least five.",
     ill_bridge),
    ("ISRAELI TANKS PUSH INTO CENTRAL GAZA",
     "Tanks advance beyond the Yellow Line near Nuseirat despite the "
     "ceasefire, after evacuation orders.",
     ill_tower),
    ("HOUTHI MISSILE HITS RIYADH TOWER",
     "A missile damages the Public Investment Fund Tower; the LPG tanker "
     "Gas Husky sinks off Bulgaria.",
     ill_tank),
    ("ANTHROPIC'S RECORD $81BN IPO",
     "Anthropic raises about $81 billion at $83 a share in a record "
     "listing; trading begins Thursday.",
     ill_chart),
]
# NOTE: story 4 illustration is the tank, story 5 the tower; fix order below.
STORIES[3] = (STORIES[3][0], STORIES[3][1], ill_tank)
STORIES[4] = (STORIES[4][0], STORIES[4][1], ill_tower)


def draw_panel(cv, px, py, pw, ph, headline, body, ill):
    cv.rect(px, py, pw, ph, PANEL_BG)
    cv.border(px, py, pw, ph, INK, 2)
    # illustration strip
    ill(cv, px + 2, py + 2, pw - 4, 106)
    cv.rect(px + 2, py + 108, pw - 4, 2, INK)
    tx = px + 14
    tw = pw - 28
    y = py + 120
    for line in wrap_text(headline, 3, tw):
        cv.text(tx, y, line, 3, INK)
        y += 25
    y += 4
    for line in wrap_text(body, 2, tw):
        cv.text(tx, y, line, 2, bytes([40, 40, 40]))
        y += 17
    return y


def main():
    cv = Canvas(W, H, PAPER)
    # masthead
    cv.rect(0, 0, W, 96, BLACK)
    cv.text_center(20, "THE WORLD TODAY", 8, WHITE)
    cv.rect(0, 96, W, 5, RED)
    # date line
    cv.text_center(118, "Thursday 19 November 2026", 4, RED)
    cv.rect(24, 158, W - 48, 2, RULE)
    # panels: 2 cols x 3 rows
    pw, ph = 494, 272
    xs = [12, 518]
    ys = [168, 448, 728]
    for i, (headline, body, ill) in enumerate(STORIES):
        draw_panel(cv, xs[i % 2], ys[i // 2], pw, ph, headline, body, ill)
    # footer
    cv.text_center(1000,
                   "All six stories happened or were first reported on "
                   "Thursday 19 November 2026.", 2, GREY)
    n = write_png(cv, "entry.png")
    print("wrote entry.png", n, "bytes")


if __name__ == "__main__":
    main()
