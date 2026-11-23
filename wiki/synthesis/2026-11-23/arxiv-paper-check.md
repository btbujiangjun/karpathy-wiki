---
title: "arXiv Paper Check — AI & CTR (2026-11-23)"
type: synthesis
created: 2026-11-23
updated: 2026-11-23
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=40
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR+OR+cat:cs.LG+OR+cat:stat.ML&sortBy=submittedDate&sortOrder=descending&max_results=60
  - https://export.arxiv.org/api/query?search_query=abs:%22click+through+rate%22+OR+ti:CTR&sortBy=submittedDate&sortOrder=descending&max_results=50
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - advertising
  - retrieval
  - ir
  - daily-digest
---

# arXiv Paper Check — AI & CTR (2026-11-23)

> **Window note:** Queried via the arXiv Export API at ~2026-11-23 02:23 UTC (strict last-24h window, 2026-11-22 → 2026-11-23). AI = `cat:cs.AI`; CTR = `cat:cs.IR` / `cat:cs.LG` / `cat:stat.ML` (home categories of click-through-rate / recommender / advertising literature) + keyword sweep (`abs:"click through rate" OR ti:CTR`). **Result: 0 new AI/CTR papers — arXiv is quiet in this window; there are no picks to summarize.** The keyword sweep was rate-limited (HTTP 429) during this run; the window queries for `cat:cs.AI`, `cat:cs.IR`, `cat:cs.LG` and `stat.ML` completed normally (0 results each). Newest submissions in the query window: `2611.27206v1` (cs.AI + cs.LG, submitted 2026-11-20T06:45:57Z) and the `2611.272xx` batch around 06:21–06:45 UTC on 2026-11-20 — already covered by the 2026-11-20 window. Abstract/metadata-level screening only, no full-text review; metrics/claims author-reported where present.

## Coverage table

| Lane | New papers in window | Newest paper (submitted) |
|------|---------------------|--------------------------|
| AI — `cat:cs.AI` | 0 | 2611.27206v1 (cs.AI + cs.LG) — 2026-11-20T06:45:57Z |
| CTR — `cat:cs.IR` | 0 | — (newest cs.IR seen: 2611.26609v1, 2026-11-19, per sibling 2026-11-22 report) |
| CTR — `cat:cs.LG` / `stat.ML` | 0 | 2611.27196v1 (cs.AI + cs.SE) — 2026-11-20T06:31:08Z |
| CTR keyword sweep | 0 (rate-limited) | — |

## Interpretation

- No new `cat:cs.AI` papers between 2026-11-22 02:23Z and 2026-11-23 02:23Z; the freshest submissions in the query are dated 2026-11-20 (IDs ~2611.272xx, 06:21–06:45 UTC), already covered by the 2026-11-20 batch.
- No new `cat:cs.IR` submissions in the window either (last seen: `2611.26609v1` Variants of Beam Search for DiskANN, 2026-11-19T18:57:05Z).
- The keyword sweep (`abs:"click through rate" OR ti:CTR`) was unavailable this run (arXiv API HTTP 429/timeouts); the sibling 2026-11-22 and 2026-11-21 reports recorded 0 for the same sweep — no new matches are expected in the empty window.

## Related

- [[synthesis/2026-11-22/arxiv-paper-check|2026-11-22 arXiv Paper Check]]
- [[synthesis/2026-11-21/arxiv-paper-check|2026-11-21 arXiv Paper Check]]
- [[synthesis/2026-11-20/arxiv-paper-check|2026-11-20 arXiv Paper Check]]
