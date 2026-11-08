# Update pack: vienna-ringstrasse, 72h checkpoint (written 2026-11-08 20:30Z; 24h pack skipped as superseded, the first optimizer pass to see this video is already past 96 h)
Header: VIDEO_ID unknown (analytics/videos.csv missing): needs --sync on the PC: `yt_update.py --sync vienna-ringstrasse "This Vienna street used to be a fortress"`. Metrics: analytics/metrics_youtube.csv missing, so YouTube numbers are Buffer Data API numbers (stale, metricsUpdatedAt 2026-11-07 22:54Z). Please run `--metrics` on the PC.

```apply
MATCH_TITLE: This Vienna street used to be a fortress
VIDEO_ID:
TITLE: This Vienna street used to be a fortress
TAGS: Vienna, Ringstrasse, Vienna history, city history, fortress, Franz Joseph, Ottoman siege 1529, city walls, Austria, history shorts
DESCRIPTION:
Walk the Ringstrasse today and you're strolling where Vienna's fortress walls used to stand. For centuries the city sat behind walls, bastions and a wide open strip of ground called the glacis, and in 1857 Franz Joseph ordered the walls torn down.

What I love about this one is that the Ring is basically a fossil. It roughly follows the line of the old fortifications, and the grand buildings along it went up on land that had been kept empty for defence.

Have you walked the Ring? Did you notice how it wraps around the old centre?

The Shape of Then shows how a city's history built the streets you walk today. A new city every day, subscribe so you don't miss one.

Sources:
https://www.habsburger.net/en/events/ringstrasse-era-1857-1914
https://www.geschichtewiki.wien.gv.at/Stadtmauer
https://en.wikipedia.org/wiki/Ringstrasse

#Vienna #History #Ringstrasse
```

## Why this change (one variable: metadata completeness)
Title and first two description lines are KEPT: Vienna is the best older YouTube Short (1,793 views @76.7 h, 42 likes, vs Lisbon 1,406 and Florence 1,296), so rewriting the opening lines would only add risk. Live text already follows the format (claim, honest reaction, comment question, 3 hashtags, plain sources, no sound credit). Two gaps fixed: (1) the channel line before the sources is missing; (2) the 10 tags in the package were never applied (Buffer has no YouTube tags field), so the video has no tags for search. Variable logged in experiments.csv as T-VIENNA-TAGS.
Virality-predictor (TikTok rows as Shorts proxy, judgment not a measurement): live first two lines ~72/100 and new first two lines identical, so score is not lower; the added channel line is below the fold.

## Title options (not applied; title is unchanged on purpose)
1. This Vienna street used to be a fortress: KEEP (plain speech, concrete, "Vienna" first four words; working).
2. Vienna's Ringstrasse sits where the fortress walls stood: more searchable (Ringstrasse), less curiosity; test only on the next Vienna-type video.
3. Why is Vienna's Ring road so wide?: question form (hook B), but "so wide" adds a claim the fact-check did not cover; do not use.

## Pinned comment (post only on the owner's say-so)
Sources: habsburger.net (1857 decree), Wien Geschichte Wiki (city walls), Wikipedia (Ringstrasse). The Richard the Lionheart ransom link is the traditional account. Which city should we rewind next?

## Cover-frame picks
None to apply: Vienna is a pre-PC episode, so no episodes\vienna-ringstrasse\output\cover_A.jpg or cover_B.jpg exists. Thumbnail line left empty on purpose (first-second rule: a cover without readable title + gold subject is a regression). Leave the current frame.

## Numbers that led to the change
YT: 1,793 views, 42 likes, 0 comments @76.7 h (flat, near plateau; opening v1). IG: 2,058 plays, avg watch 26.7 s (45%), skip 32.7%, 6 shares + 2 saves, reach 1,635 @ ~102 h (Buffer, 2026-11-08 01:28Z). Opening v1 (no v2 hook). Packaging gap is metadata, not wording.
