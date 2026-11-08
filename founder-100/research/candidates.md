# Candidate assessment (2026-11-08)

Scores are **heuristic 1-5, not market statistics**. Weights: urgency 20, reachable buyers 20, time to cleared cash 20, contribution economics 15, reliable delivery 15, low legal/security complexity 10. Missing evidence lowers confidence. Evidence is mostly secondary (marketplace listings, vendor blogs); treat as weak.

| # | Candidate | Urg | Reach | Cash | Econ | Deliv | Legal | Weighted | Confidence |
|---|-----------|-----|-------|------|------|-------|-------|----------|-----------|
| 1 | **Product/inventory spreadsheet cleanup -> import-ready CSV for small online sellers** | 3 | 3 | 4 | 3 | 4 | 3 | **3.3** | low-med |
| 2 | Bookkeeping catch-up / reconciliation | 4 | 4 | 3 | 3 | 2 | 1 | 3.0 | low |
| 3 | Local-business FAQ / listing copy | 2 | 3 | 3 | 2 | 4 | 4 | 2.9 | low |
| 4 | Meeting-notes / transcript cleanup | 2 | 2 | 3 | 2 | 4 | 2 | 2.5 | low |
| 5 | Generic Excel cleanup (no niche) | 3 | 3 | 4 | 2 | 4 | 3 | 3.1 | low |

Weighted = sum(score x weight)/100, computed by hand; recompute before relying on it.

## Decision: Candidate 1 (narrowed version of 5)
A named buyer segment (small online sellers and local retailers with messy product/inventory lists) beats a generic "Excel help" gig, which competes on price with $10-$45 listings. Data is low-sensitivity by design: product names, SKUs, prices, quantities. No customer PII, no financial/bank data accepted.

## Rejections
- **#2 Bookkeeping:** financial data, tax-law judgement, "compiling transaction records" is described as taxable data processing in Texas, high-trust role without credentials. Rejected per prompt section 5.
- **#3 Copy:** low urgency, crowded, hard to price above commodity.
- **#4 Transcripts:** confidential meeting content = sensitive data handling.
- **#5 Generic:** no differentiation; subsumed by #1.

## Observed facts (with sources, secondary)
- Marketplace Excel-cleanup listings: basic $10-$45, pivot/formula work $45-$95, higher tiers $95-$200. One listing: from $50 for one file up to 5,000 rows, one revision, excludes macros and sensitive data. Source: https://fiverr.com/resources/guides/costs/excel-expert ; https://contra.com/s/NrWP3LZX-excel-and-csv-data-cleanup-in-24-hours (retrieved 2026-11-08). Fiverr guide is platform marketing.
- Pain-point statistics (e.g. "77% struggle with receipts") are uncited vendor-blog claims. **Not used.** No direct willingness-to-pay data found.

## Assumptions (unverified)
- Small sellers will pay ~$75 for a fixed-scope 48h cleanup. Scenario only.
- They can find and trust a solo operator with no reviews. Likely hard; this is the main risk.

## What could disprove demand
No qualified replies from one batch of 10 matched prospects; objections that price anchors at $10-$45; buyers preferring to use free tools; platform import tools already solving this.

## Pivot trigger
After 14 active selling days with no paid pilot: review objections; consider narrowing to one platform's import format (e.g. a single marketplace) or a different segment. No automatic extra spend.

## Economics scenario (NOT actuals)
Price $75. Payment fee assumption ~3% + fixed per-transaction (unverified; verify chosen processor). Delivery ~1.5 owner/agent hours; AI cost per job assumed < $1 (unmeasured). Contribution roughly $70 before sales tax and owner labor. At one job per week this is not a livable business; the test is whether demand exists at all.
