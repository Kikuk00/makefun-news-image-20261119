# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Kikuk00/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Kikuk00/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A newspaper-style front-page infographic summing up the world news of
**Thursday 19 November 2026** in one image, for the make.fun bounty
[news-image-20261119](https://make.fun/bounty/news-image-20261119).

The image is 1024×1024 and was drawn entirely by code (flat vector shapes
and a hand-built bitmap font, standard library only — no image libraries,
no copied artwork). `main.py` copies `entry.png` to the output directory.

## The six stories

1. **First US–China–Russia summit in Shenzhen** — Donald Trump, Xi Jinping
   and Vladimir Putin held the first-ever trilateral summit in Shenzhen on
   the sidelines of APEC (90 minutes), then issued a joint "peace
   declaration" pledging dialogue on reducing nuclear risks and preventing
   the spread of nuclear weapons, plus more oil supply. No breakthrough on
   Ukraine or Iran.
2. **Myanmar guilty of Rohingya genocide** — The UN International Court of
   Justice ruled Myanmar committed state-sponsored genocide against the
   Rohingya, the court's first such ruling. It found about 10,000 Rohingya
   were killed and ordered investigations, compensation for victims and the
   return of displaced people.
3. **Kerch Bridge hit for a third time** — Russia said Ukraine attacked the
   Crimean Bridge for the third time this week; the rail section was hit and
   train traffic halted. Russian strikes killed at least five people in
   Ukraine and knocked out power in Dnipropetrovsk, Zhytomyr, Zaporizhzhia,
   Mykolaiv and Sumy regions.
4. **Israeli tanks push into central Gaza** — Israeli tanks pushed into
   central Gaza beyond the Yellow Line near Nuseirat despite the ceasefire,
   after evacuation orders to residents.
5. **Houthi missile hits Riyadh tower** — A Houthi missile attack damaged
   the Public Investment Fund Tower in Riyadh. Separately, the LPG tanker
   Gas Husky sank off Bulgaria after being struck by projectiles.
6. **Anthropic's record $81bn IPO** — Anthropic raised about $81 billion in
   a record initial public offering at $83 a share; trading began on
   Thursday.

## How it works

One file, `main.py` (Python 3.13, standard library only, no network).
It copies the `entry.png` shipped in this repository to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), byte for byte, so
both runs of the program write identical output.

## Run it

```sh
python3 main.py
```

Writes `entry.png` (1024x1024 PNG, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR`.

## Files

- `main.py` — stdlib-only program; copies `entry.png` to the output dir
- `entry.png` — the 1024×1024 front page
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=wmk9f4s6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
