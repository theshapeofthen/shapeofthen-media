# Update pack: copenhagen-christiansborg, 24h checkpoint (written 2026-11-10 20:40Z)
Header: VIDEO_ID unknown (analytics/videos.csv missing): needs --sync on the PC: `yt_update.py --sync copenhagen-christiansborg "Denmark's parliament sits on a bishop's island"`. Metrics: analytics/metrics_youtube.csv missing, please run `--metrics` on the PC. Buffer's YouTube numbers are stale (125 views @2.4 h, metricsUpdatedAt 2026-11-09 21:29Z), so no YouTube judgment is made from them.

```apply
MATCH_TITLE: Denmark's parliament sits on a bishop's island
VIDEO_ID:
TITLE: Denmark's parliament sits on a bishop's island
TAGS: Copenhagen, Christiansborg, Christiansborg Palace, Copenhagen history, Denmark, Danish parliament, Folketing, Bishop Absalon, Absalon's Castle, city history, history shorts
THUMBNAIL:
DESCRIPTION:
Denmark's parliament meets on a little island where Bishop Absalon built a castle around 1167.

The Hanseatic League had his castle torn down in 1369. Later kings built a new castle on the ruins, and from 1731 Christian VI replaced it with one of northern Europe's biggest palaces. An overheated stove burned it in 1794. Palace two housed Denmark's new parliament from 1850, then burned in October 1884, three days before parliament opened. And then two rival parties couldn't agree how to rebuild, so the ruins sat there for about twenty years. Honestly, that standoff is the bit I can't stop thinking about. Parliament moved into its wing of palace three in 1918, and the king stayed at Amalienborg.

Absalon's ruins are still under the palace, and you can visit them. If you've been down there, what surprised you?

The Shape of Then shows how a city's history built the streets you walk today. A new city every day, subscribe so you don't miss one.

Sources:
https://www.thedanishparliament.dk/en/christiansborg-palace/the-history-of-christiansborg-palace
https://denkongeligesamling.dk/en/christiansborg-palace/interior-and-objects/the-ruins-under-christiansborg-palace/
https://en.wikipedia.org/wiki/Absalon%27s_Castle

#copenhagen #denmark #history
```

## Why this change (one variable: metadata completeness, tags added)
The live description already follows the format (claim, honest reaction, comment question, channel line, plain sources, exactly 3 hashtags, no sound credit), so the text is unchanged. The only gap is search metadata: Buffer has no YouTube tags field, so the video has none. Title and first two lines are kept on purpose: the YouTube data is too thin to judge them (arm E sample 1, hook test), and changing the title would confound hook_pattern. Virality-predictor (TikTok rows as Shorts proxy, judgment): live title 66, first two description lines 70, new text identical, so not lower. Logged as T-COPENHAGEN-TAGS.

## Title options (not applied)
1. Denmark's parliament sits on a bishop's island: KEEP (concrete, plain speech, "Denmark" and "parliament" are searchable).
2. Why Copenhagen's parliament burned down twice: more search-style, but "twice" is a count the title would carry on its own; test only on a later video.
3. Denmark's parliament sits on top of a castle ruin you can visit: more searchable, longer (63 chars), loses the bishop curiosity gap.

## Pinned comment (post only on the owner's say-so)
The ruins of Absalon's castle are in the excavations under Christiansborg, open to visitors (The Royal Danish Collection runs them). Which city's "palace that kept burning" should I do next?

## Cover-frame picks
None to apply: Copenhagen is a pre-PC episode, so no episodes\copenhagen-christiansborg\output\cover_A.jpg or cover_B.jpg exists. THUMBNAIL left empty (first-second rule: a cover without readable title + gold subject is a regression). Package cover idea for reference: night fire still at 23.2 s, "COPENHAGEN / BURNED TWICE".

## Numbers that led to the change
Instagram @ 24.4 h (Buffer, metricsUpdatedAt 2026-11-10 19:29Z): 2,870 views, reach 2,282, avg watch 24.8 s (42.9%), 35 likes, 0 comments, 5 shares, 14 saves. That is 1.40x the 2,050 IG plateau at a younger age (Lisbon/Vienna/Washington) and the most saves of any post (Florence 9). It is below Florence (6,623 @28.7 h) and London/Barcelona on avg view % (London 50.4, Barcelona 54.6). YouTube: unknown (stale 125 @2.4 h). Opening v2, hook E sample 1, predicted 73.
