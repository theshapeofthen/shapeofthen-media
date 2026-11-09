# Strategy and task change log (append newest at the bottom; never rewrite history)

## 2026-11-04 v1 (setup session, owner request)
- Goal set: make the channel pay for itself (STRATEGY.md section 1).
- Added weekly long-form (Sat 10:00 CT), humanized style guide, A/B protocol, GitHub analytics, vidIQ credit budget.
- Tasks: nightly Shorts updated; daily ledger rewritten (free data sources, writes here); post-publish polish disabled (spent 10 vidIQ credits/day); weekly review rewritten to edit STRATEGY and tasks; long-form worker and long-form optimizer created.

## 2026-11-04 (setup session, v1 -> v1.1)
- vidIQ balance is 45 (not 120); old caps summed to ~80 before the 4 Dec renewal. New caps: optimizer <=10/long-form, weekly review <=3, worker/nightly/ledger 0. Reason: avoid running dry mid-month.
- Old Shorts polish task (1:25/3:25 PM) merged into one daily optimizer at 2:25 PM (Shorts polish + long-form 7-day checkpoints). Reason: the task had been renamed to long-form optimizer but still ran the Shorts prompt.
- Nightly, ledger and weekly-review prompts rewritten to read STRATEGY/HUMAN_STYLE/LEARNING and write analytics/ (posts, metrics, experiments, credits, strategy_changes).

## 2026-11-06 (owner session)
- Owner removed the sound credit line everywhere (OWNER_OVERRIDES.md). Ledger, optimizer, nightly, weekly and long-form prompts updated. Risk noted: Oculus pack is CC BY 4.0.
- Owner schedules YouTube in Studio (not Buffer). Known: Washington P_1_OZj4nkQ Fri 7:00 AM CT; Barcelona yBEuBqwPF8Q Sat 10:00 PM CT.
- Titles/descriptions/tags rewritten by hand: Washington ("Why DC has no skyscrapers (it's not the Capitol)"), Barcelona ("Barcelona picked one plan. Madrid built another."), Florence (description/tags only). Title-test comparisons use the original live titles (posts.csv).
- vidIQ credits: 25 -> about 5 after 3 paid video updates. Renews 4 Dec.
- Scheduled tasks nightly, optimizer and long-form hit USAGE_LIMIT_REACHED on recent runs.

## 2026-11-09 v2.0 (weekly review, week 1)
Evidence: week-1 Buffer data (YouTube 7,525 views over 5 Shorts, Instagram 15,756 plays over 5 reels; plateau YT 1,300-1,800, IG 2,050-2,560, one IG breakout Florence 6,723). No winner under the EXPERIMENTS rule (n=1 per hook arm). YouTube analytics (metrics_youtube.csv, changes.csv, videos.csv) do not exist: yt_update.py never ran or never pushed.
STRATEGY.md sections 4-5 rewritten (before = v1.2 of 4 Nov):
- Hook: before = "concrete contrast inside 2 s, slate-driven"; after = same plus three frame-0 rules from stills of Vienna v1 / Florence v2 / Copenhagen v2 / Amsterdam v3 (max two text layers in the first 2.5 s; character or landmark in the foreground; visible camera move by 0.4 s and gold shape about a third of frame). Reason: Florence stacked three text layers, Copenhagen's first 2.5 s are near-static, Vienna v1 had no title and no subject on frame 0.
- Length: before = 50-58 s, 130-138 words; after = V5 35-42 s, 95-115 words (OWNER_OVERRIDES_ADDENDUM 2026-11-08; Barcelona 41 s fastest start supports it, confounded).
- Titles: before = statement default and "statement beat question 12x" in LEARNING; after = claim withdrawn (Lisbon 111 views at 33 h became 1,406 at 79 h). New tell rule: no two titles in a row start "<Place>'s".
- Descriptions/comments: new rules. Every description used a "the part/bit that gets me" reaction line (7 of 8 episodes); five of eight comment questions were "Have you walked X? Did you notice Y?"; comments are ~0 everywhere. Reaction line must vary and appear in at most one description in three; rotate comment-question shapes. Reason: YouTube's 16 Jul 2026 guidance on generic/template content.
- Ending: before = open question; after = W2-ENDING is a read of existing posts on Mon 16 Nov (question: Barcelona, London, Amsterdam; loop: 5); new episodes hold ending=loop; next variable W3-HOOK-D (Berlin, first D sample).
- vidIQ credit bullet deleted (vidIQ removed by the owner 2026-11-07).
- Money: added the 1 Feb 2027 YPP bar (8,000 h or 20M Shorts views; Shorts revenue sharing 10M/90 d), history Shorts RPM about $0.04-0.10 per 1,000 views, so Shorts ads cannot cover the subscription; Ko-fi and Amazon links are the only revenue steps that can pay before 2027.
- Section 5: milestone re-baseline; topic queue of 7 Shorts and 3 long-form scored (demand/competition are judgement, no search-volume tool).
Task edits (1 of 2 allowed): weekly strategy review prompt (trig_014DfVJ3sRtHCte5uEuUZrHi). Diff: removed "FREE read-only vidIQ calls" and the vidIQ insights call in step 1 (override says no vidIQ tool at all); READ FIRST now includes OWNER_OVERRIDES_ADDENDUM.md and the newest AUDIT (this run almost missed the owner's 2026-11-08 pause); step 1 notes Buffer YouTube metrics can be ~20 h stale and any hand-posted Short without a posts.csv row gets one; step 2 says the latest experiments.csv row per test_id wins; step 2c says extract stills with ffmpeg; step 7 says a gap caused by the owner's pause is reported as "paused", not a failure; step 8 says write project docs from a temporary file inside the working directory and do not rewrite the large STATE.md unless it can be resent complete. Schedule, model, enabled state, IDs and hard rules unchanged. Reason: the prompt contradicted OWNER_OVERRIDES and predated the addendum.
Not changed: ledger and optimizer prompts still mention free vidIQ reads (the override wins in read order; flagged for next week's edit, 1 edit left this week unused); planner/executor stay disabled (owner's switch). STATE.md not rewritten: it is very large, last refreshed 6 Nov, and rewriting it risked losing content; the run note is in LEARNING.
