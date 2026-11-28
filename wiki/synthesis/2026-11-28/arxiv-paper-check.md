---
title: "ArXiv Paper Check — AI & CTR (2026-11-28)"
type: synthesis
created: 2026-11-28
updated: 2026-11-28
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.CV+OR+cat:cs.IR+OR+cat:cs.MA+OR+cat:cs.NE+OR+stat.ML&sortBy=submittedDate&sortOrder=descending&max_results=200
  - https://export.arxiv.org/api/query?search_query=all:%22click-through+rate%22+OR+all:%22click+through+rate%22+OR+ti:CTR+OR+abs:CTR+OR+all:%22CTR+prediction%22&sortBy=submittedDate&sortOrder=descending&max_results=200
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - advertising
  - retrieval
  - ir
  - lg
  - daily-digest
---

# ArXiv Paper Check — AI & CTR (2026-11-28)

> **Window note:** Queried via the arXiv Export API at ~2026-11-28T02:22Z. Strict last-24h window: **2026-11-27T02:22Z → 2026-11-28T02:22Z**. **AI** = `cat:cs.AI` + `cat:cs.LG` + `cat:cs.CL` + `cat:cs.CV` + `cat:cs.IR` + `cat:cs.MA` + `cat:cs.NE` + `stat.ML`. **CTR** = keyword sweep (`all:"click-through rate" OR all:"click through rate" OR ti:CTR OR abs:CTR OR all:"CTR prediction"`) + CTR-relevant `cat:cs.IR`. **arXiv has no "CTR" category**; click-through-rate prediction lives in `cs.IR` (and also `cs.LG`/`cs.CL`). **Result: 0 new AI papers and 0 new CTR papers in the strict last-24h window — arXiv is quiet.** There is no in-window paper to summarize. The "most interesting" papers below are the **freshest available submissions just outside the window**, clearly labeled. Abstract/metadata-level screening only — no full-text review; all metrics and claims are author-reported. (See same-day sibling [[synthesis/2026-11-28/arxiv-daily|arXiv Daily 2026-11-28]] and prior [[synthesis/2026-11-27/arxiv-paper-check|2026-11-27 ArXiv Paper Check]].)

## Coverage table

| Lane | Query | Fetched | New in strict last-24h window | Newest available |
|------|-------|---------|-------------------------------|------------------|
| AI | combined `cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.CV OR cat:cs.IR OR cat:cs.MA OR cat:cs.NE OR stat.ML`, `sortBy=submittedDate`, `max_results=200` | 200 | **0** | `2611.34944v1` 2026-11-25T18:59:59Z (cs.CV); cs.AI newest `2611.34942v1` 2026-11-25T18:59:57Z |
| CTR keyword sweep | `all:"click-through rate" OR all:"click through rate" OR ti:CTR OR abs:CTR OR all:"CTR prediction"`, `max_results=200` | 200 | **0** | `2611.25659v1` 2026-11-19T07:40:54Z (DNA: Unlocking Depth Scaling in CTR Models) |
| Cross-check (per-category) | top-5 `sortBy=submittedDate` for `cat:cs.AI`, `cat:cs.IR`, `cat:cs.LG`, `cat:stat.ML`, `cat:cs.CL`, `cat:cs.CV`, `cat:cs.MA`, `cat:cs.NE`, + CTR keyword | — | **0** | `2026-11-25T18:59:59Z` across all scanned AI categories; CTR keyword newest `2026-11-19` |

## Result

**0 new papers in the strict last-24h window (2026-11-27T02:22Z → 2026-11-28T02:22Z) in both lanes.** No `<published>` timestamp falls inside the window in any scanned category or the CTR keyword sweep; the newest submission across all AI categories is `2026-11-25T18:59:59Z`, and the newest CTR-keyword match is `2026-11-19T07:40:54Z`. Consistent with the sibling quiet-window reports ([[synthesis/2026-11-27/arxiv-paper-check|2026-11-27]], [[synthesis/2026-11-25/arxiv-paper-check|2026-11-25]]). arXiv `updated` revisions on older papers do not pull anything new into the window — `published` governs "new."

## Most interesting papers — freshest available (OUTSIDE strict window)

Nothing is in-window; these are the newest available submissions (2026-11-25) not already covered by the sibling reports, curated by interest, **not** a ranking. Picks are single-source; numbers are author-reported from abstracts.

### AI lane (submitted 2026-11-25)

1. **Tokenisation is not in APX** — [arXiv:2611.34938v1](https://arxiv.org/abs/2611.34938v1) (cs.CL, cs.LG; submitted 2026-11-25T18:59:38Z)
   **Authors:** Violeta Kastreva, Philip Whittington, Dennis Komm, Tiago Pimentel
   **Key contribution:** Complexity-theoretic hardness for tokenisation. Proves that, **unless P=NP, no polynomial-time algorithm can find a tokeniser whose objective is within any constant factor of the optimum — tokenisation is not in the APX complexity class.** Holds for **direct and bottom-up** tokenisation, under both **compression** and **unigram log-likelihood** objectives, and for **binary or larger alphabets**; further, even on **unary** alphabets direct tokenisation is **APX-hard** (admits no polynomial-time approximation scheme). A foundational negative result relevant to anyone claiming optimal vocabularies are cheaply attainable. (single-source; proofs, no empirical metrics.)

2. **AnyCam: Anything Can Represent Camera for Video Generation** — [arXiv:2611.34944v1](https://arxiv.org/abs/2611.34944v1) (cs.CV; submitted 2026-11-25T18:59:59Z; newest available across scanned categories)
   **Authors:** Weijie Lyu, Zhixin Shu, Yuntian Ke, Ming-Hsuan Yang
   **Key contribution:** Camera-controlled video generation without fragile camera-parameter or explicit-geometry conditioning. Represents the camera with an **anchor object**: reconstructs it in 3D and renders it along the target trajectory, giving a **scale-aware, view-complete, object-relative** camera signal; a video diffusion model transfers source content + dynamics to the new viewpoint. **H-Concat** time-aligned layout lets distillation into **AnyCam-AR**, a **streaming few-step** on-the-fly camera controller. Trained on paired multi-camera + static-scene captures; favorable vs. camera-controlled generation and 3D reconstruction on camera control + visual quality. (single-source; author-reported.)

### CTR lane (no paper inside strict window; freshest available CTR paper)

3. **DNA: Unlocking Depth Scaling in CTR Models** — [arXiv:2611.25659v1](https://arxiv.org/abs/2611.25659v1) (cs.IR; submitted 2026-11-19T07:40:54Z) *(already covered in [[synthesis/2026-11-27/arxiv-paper-check|2026-11-27]] / [[synthesis/2026-11-25/arxiv-paper-check|2026-11-25]] / same-day [[synthesis/2026-11-28/arxiv-daily|arXiv Daily]])*
   **Authors:** Caiyuan Li, Wenjie Wu, Yuheng Huang, Xiao Zhou, Silu Zhou, Ke Chen, Zinan Zhao, Xinrui Zeng, Hanmo Xu, Chaoqun Song, Hua Zong, Zongyuan Wu, Hongbin Zhou, Huimin Yi, Zhixuan Zhang, Dan Ou, Haihong Tang
   **Key contribution:** **Dual-stream Nexus Attention (DNA)** for long-behavior-sequence CTR; key/value side is the depth bottleneck; each layer lets the request read the sequence then each behavior token updates itself from the updated request; update once per request, shared across candidates, linear complexity. AUC +0.08→+0.26 pt vs equal-FLOP cross-attention stacks; DNA-4 deployed in Taobao search, online A/B **CTR +0.8%, GMV +0.5%**. (single-source; author-reported; industry-deployed.)

## Honest framing

- **0 in-window ≠ no activity ever;** it means nothing was `published` inside the measured 24 h. Run at ~02:22Z on a Saturday, the freshest available submissions are ~8.4 h old (`2026-11-25T18:59Z`); arXiv does not announce on weekends, and no `2026-11-26`/`2026-11-27`/`2026-11-28` submissions exist in scope.
- **No arXiv "CTR" category exists.** CTR-lane coverage = `cat:cs.IR` + keyword sweep (`click-through rate` / `click through rate` / `CTR` / `CTR prediction`); CTR models also appear under `cat:cs.LG`. Primary-category mis-tagging can hide CTR papers; the keyword sweep mitigates.
- Picks **1–3 are outside the strict last-24h window**, labeled as such; **"most interesting" is my curation, not exhaustive**, and ordering is not a ranking. Picks already covered by the 2026-11-27 sibling are cross-referenced rather than re-listed.
- **Metrics are author-reported** from abstracts; no full-text verification; no reproduction. `(single-source)`.
- Method: arXiv Export API `sortBy=submittedDate&sortOrder=descending`, `max_results=200` per query, `published ≥ now−24h` filter applied client-side; retries + per-category top-5 cross-check against arXiv HTTP 429 rate-limiting; no `websearch` in this environment.
- This run scanned a **broader AI category set** than the sibling's `cat:cs.AI`-only; both agree on 0 in-window.

## Related

- [[synthesis/2026-11-27/arxiv-paper-check|2026-11-27 ArXiv Paper Check]]
- [[synthesis/2026-11-28/arxiv-daily|2026-11-28 ArXiv Daily]]
- [[synthesis/2026-11-27/arxiv-ai-search|2026-11-27 arXiv AI Search]]
- [[synthesis/2026-11-25/arxiv-paper-check|2026-11-25 ArXiv Paper Check]]
