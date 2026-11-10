# Update pack: london-great-fire, 24h checkpoint (written 2026-11-10 20:40Z)
Header: VIDEO_ID known (wU1uXInMWOg, Buffer asset URL), but analytics/videos.csv is missing, so the live TITLE is unknown (Buffer does not return YouTube titles). MATCH_TITLE is left empty and TITLE is left empty on purpose: the script should keep the live title. Please run `yt_update.py --sync london-great-fire "<live title>"` and `--metrics wU1uXInMWOg --age 24h` on the PC. Buffer's YouTube numbers are stale (1,579 views @19.7 h, metricsUpdatedAt 2026-11-09 21:29Z).

```apply
MATCH_TITLE:
VIDEO_ID: wU1uXInMWOg
TITLE:
TAGS: London, Great Fire of London, 1666, Christopher Wren, Wren's plan for London, London history, Pudding Lane, John Evelyn, city planning, city history, history shorts
THUMBNAIL:
DESCRIPTION:
After the Great Fire of 1666, London could have been rebuilt as a grid. Within days, Christopher Wren handed King Charles II a plan with straight streets and open squares, and John Evelyn drew one too.

What gets me is who beat them: mostly the property owners, who wanted their plots back. Buying them out would have cost a lot and London had to rebuild fast, so the old street pattern largely came back, rebuilt in brick or stone by law.

Would you have taken Wren's grid, or kept the crooked old lanes?

The Shape of Then shows how a city's history built the streets you walk today. A new city every day, subscribe so you don't miss one.

Sources:
https://blogs.loc.gov/maps/2025/12/phoenix-rising-urban-planning-after-the-great-fire-of-london/
https://scalar3.coas.missouri.edu/vm/vol2plates1-2-plans-london-after-1666
https://www.ianvisits.co.uk/articles/the-myth-of-wrens-masterplan-for-london-2353/

#London #History #GreatFireOfLondon
```

## Why this change (one variable: metadata completeness, tags + channel line)
Same gap as Vienna/Lisbon/Copenhagen: no tags (Buffer has no tags field) and the channel line is missing before the sources. Wording of the claim, reaction and question is unchanged, so no new facts. Title untouched (unknown, and the hook-C sample 2 should stay unconfounded). Virality-predictor (judgment, TikTok proxy): first two lines identical to live, ~70; not lower. Logged as T-LONDON-TAGS.

## Title options (not applied; only if the live title turns out to be weak)
1. London could have been a grid after the 1666 fire: the package title; plain speech, "London" and "1666" first.
2. Why London has crooked streets (Wren's grid plan): search-style; the "crooked streets" claim is covered by the script (old pattern largely came back); test on a later video.
3. Wren drew a grid for London. Why didn't it happen?: question form (hook B) so it would change the test variable; do not use now.

## Pinned comment (post only on the owner's say-so)
Wren's plan vs the crooked lanes: which London would you rather walk? Sources: https://blogs.loc.gov/maps/2025/12/phoenix-rising-urban-planning-after-the-great-fire-of-london/ | https://scalar3.coas.missouri.edu/vm/vol2plates1-2-plans-london-after-1666 | https://www.ianvisits.co.uk/articles/the-myth-of-wrens-masterplan-for-london-2353/

## Cover-frame picks
None to apply: London is a pre-PC episode, no cover_A.jpg or cover_B.jpg exists. THUMBNAIL left empty (first-second rule).

## Numbers that led to the change
Instagram @ 41.7 h: 2,263 views, reach 1,628, avg watch 29.1 s (50.4%), 16 likes, 0 comments/shares/saves; 1.10x the 2,050 plateau, flat vs 2,254 @18.7 h (done growing). YouTube: 1,579 views @19.7 h (stale), level with Barcelona at equal age, above Florence. Opening v2, hook C sample 2, predicted 74.
