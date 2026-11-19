# News Image — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ItsSuperMeow/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ItsSuperMeow/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world news of **Thursday 19 November 2026**.

Built for the [make.fun news-image-20261119 bounty](https://make.fun/bounty/news-image-20261119)
($250, 50 paid places). The entry is `main.ts` at the root: it copies
`entry.png` to `/output/entry.png`. The image is drawn in code
(`draw_poster.py`, Python + Pillow) so every label is crisp and legible.

## The six stories

All six were verified against primary news reporting on 19 November 2026:

1. **Shenzhen summit** — Trump, Xi and Putin held the first-ever
   three-way summit in Shenzhen, on the APEC sidelines. Bilaterals first
   (Trump–Putin ~40 min, Trump–Xi ~1 hr), then a joint session of
   ~80–90 min. Joint statement: reform the UN, boost refined-oil supply,
   "a nuclear war cannot be won and must never be fought".
   Sources: USA Today, NPR, The Times, NY Post.
2. **ICJ: Myanmar genocide** — The International Court of Justice in The
   Hague ruled Myanmar acted with genocidal intent against the Rohingya
   in the 2017 crackdown: ~10,000 killed, 730,000+ fled to Bangladesh.
   9 votes to 6; the first time in the ICJ's 80-year history it has held
   a state accountable for genocide. Case brought by The Gambia in 2019.
   Sources: CNN, Reuters.
3. **Crimean Bridge hit again** — Overnight 18–19 Nov, Ukraine struck the
   Crimean Bridge a third time in a week; Russian-installed head Sergei
   Aksyonov confirmed it and traffic was halted, including rail. Follows
   the 17 Nov strike that collapsed a road arch into the Kerch Strait.
   Sources: BBC, Meduza, Deutsche Welle.
4. **Anthropic IPO debut** — Anthropic's shares (ANT) began trading on
   Nasdaq, priced at $83 on 18 Nov (above the $70–78 range); 980 million
   shares, about $81.3bn — the largest IPO on record.
   Sources: Anthropic announcement, CNBC/AP, Nasdaq notice.
5. **Bangladesh unrest** — The banned Awami League called a nationwide
   lockdown on Thu 19 Nov; former interim leader Muhammad Yunus's
   ancestral home in Chattogram was set ablaze late Wed night; police
   said two ruling-party members were killed; violence reported in 28 of
   64 districts; 97 Border Guard platoons deployed; ahead of ex-PM
   Sheikh Hasina's planned return in December. Source: Reuters.
6. **Cyclone Akvan** — Severe Cyclone Akvan bore down on India's east
   coast; Odisha evacuated tens of thousands (over 72,000, officials
   said) to shelters, schools shut in six districts; landfall expected
   Fri 20 Nov near Gopalpur, winds 90–100 km/h gusting to 110.
   Sources: IMD, ANI/PTI.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (1024x1024 PNG)
```

## Regenerate the poster

```sh
python3 draw_poster.py   # writes entry.png
```
