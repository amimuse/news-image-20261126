# World News — 26 November 2026, in One Image

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/amimuse/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/amimuse/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

One 1024×1024 image summing up Thursday 26 November 2026, built for the [make.fun news-image-20261126 bounty](https://make.fun/bounty/news-image-20261126). The judge has no news feed, so the image itself carries the news: seven verified stories, each with a readable headline, the key facts and the numbers.

## The seven stories

1. **US proposes new tariffs on 14 trading partners** (Washington) — duties of 18–20% proposed on several Asian exporters, citing excess industrial capacity; China, the EU and Japan among the 14 named.
2. **Drone attack in Kuwait kills two Italians** — two Rheinmetall Italia technicians died at an air-defence site, four others hurt; Kuwait blamed Iran, Tehran denied any role.
3. **Cairo tanker fire kills 31** — a fuel tanker overturned on the Ring Road and burst into flames; 21 injured, the driver detained after police said he was speeding.
4. **New chief picked to lead the ECB** — Spain's Pablo Hernández de Cos, now head of the Bank for International Settlements, will succeed Christine Lagarde; formal appointment expected in December.
5. **Kim vows a bigger nuclear arsenal** (Pyongyang) — Kim Jong Un visited nuclear facilities and called for wider use of tactical nuclear weapons.
6. **Blast at Bangkok oil facility injures nine** — explosion at a Bangchak refinery; three critically hurt, nearby residents urged to leave.
7. **Macy's parade postponed — a first in 100 years** (New York) — a storm forced the Thanksgiving Day Parade to Saturday 28 Nov; about 300,000 lost power, hundreds of flights cancelled.

Sources checked against Reuters, BBC, Al Jazeera, CNBC, The Guardian and NPR, plus the 26 November day summary on oneturn.news.

## How the image was made

`poster.html` is a hand-built newspaper-style infographic (system fonts only, no external resources). It was rendered to `entry.png` (1024×1024, PNG) with a headless Chromium screenshot, and visually checked: every headline and fact is legible at full size, with no overflow.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png`. It uses no network, so two runs write byte-identical output.

## Referral

Made with make.fun — try it with referral code `6aqcqv8v`: https://make.fun/r/6aqcqv8v
