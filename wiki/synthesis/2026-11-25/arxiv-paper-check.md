---
title: "ArXiv Paper Check — AI & CTR (2026-11-25)"
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=50
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR&sortBy=submittedDate&sortOrder=descending&max_results=50
  - https://export.arxiv.org/api/query?search_query=all:%22click+through+rate%22+OR+ti:CTR&sortBy=submittedDate&sortOrder=descending&max_results=50
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

# ArXiv Paper Check — AI & CTR (2026-11-25)

> **Window note:** Queried via the arXiv Export API at ~2026-11-25 (strict last-24h window, 2026-11-24 → 2026-11-25, current ~2026-11-25T02:20Z). AI = `cat:cs.AI`; CTR = `cat:cs.IR` (home category of click-through-rate / recommender / advertising literature) + keyword sweep (`all:"click through rate" OR ti:CTR`). **Result: 0 new AI/CTR papers in the window — arXiv is quiet.** There are no picks to summarize. Abstract/metadata-level screening only, no full-text review; metrics/claims author-reported where present.

## Coverage table

| Lane | New papers in window | Newest paper (submitted) |
|------|----------------------|--------------------------|
| AI — `cat:cs.AI` | 0 | — (freshest available: `2611.31228v1` 2026-11-23T18:58:52Z) |
| CTR — `cat:cs.IR` | 0 | — (freshest available: `2611.31185v1` 2026-11-23T18:38:53Z) |
| CTR keyword sweep | 0 | — (freshest available: `2611.25659v1` 2026-11-19T07:40:54Z) |

## Freshest available (outside the window)

- **Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ** (2611.31228v1; cs.AI; Daniel Theron). Key contribution: evaluates Qwen2.5-7B, Llama-3.1-8B, Mistral-7B and Phi-4 (14.7B) across 15,200 math benchmark attempts (2,017 isolated reasoning errors); shows verbalized confidence does not distinguish error steps from sound reasoning (AUROC 0.500–0.561, near chance), and on first errors confidence stays saturated (95.1–99.9%). Injected low-confidence tags (+3.7 to +22.5 points) do steer repair, while doubt on correct steps costs up to 22.8 points of solve rate.

- **Seeking in Space: Benchmarking Purposeful Active Exploration of Vision-Language Models for Spatial Reasoning** (2611.31215v1; cs.AI; Xiwei Liu, Yulong Li, Xuhui Li, Xinlin Zhuang, Zhixiang Lu). Key contribution: ActSpace-Bench — 994 questions over 234 exploration episodes in 72 real-scanned indoor scenes; strong models seek evidence with purpose but lose it to limited memory, while weaker models explore no better than a random walk.

- **ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents** (2611.31198v1; cs.AI/cs.CL/cs.CV; Rui Sun, Junhua Huang, Luca Zancato, Md Mofijul Islam, Kai-Wei Chang). Key contribution: framework that grows and reuses search/vision tool modules on top of a lean base tool library, evaluated on 3 in-domain and 10 out-of-domain multimodal search benchmarks (VLM-as-a-Judge).

- **DNA: Unlocking Depth Scaling in CTR Models** (2611.25659v1; cs.IR; Caiyuan Li, Wenjie Wu, Yuheng Huang, Xiao Zhou, Silu Zhou, Ke Chen, Zinan Zhao, Xinrui Zeng, Hanmo Xu). Key contribution: Dual-stream Nexus Attention (DNA) lets the long behavior sequence evolve with depth (dual-stream reads + updates), recovering depth-scaling gains lost by plain cross-attention stacks (AUC +0.08 to +0.26 vs. stacks at equal FLOPs); deployed at Taobao search with online A/B: CTR +0.8%, GMV +0.5%.

## Interpretation

- 0 new `cat:cs.AI` submissions in the strict last-24h window (2026-11-24 → 2026-11-25); the freshest cs.AI papers are 2611.31228v1 (2026-11-23T18:58Z) and earlier.
- 0 new `cat:cs.IR` submissions either (freshest 2611.31185v1, 2026-11-23T18:38Z); the keyword sweep's newest is 2611.25659v1 (2026-11-19).
- Consistent with the 0-result windows of the sibling reports (2026-11-21/22/23): arXiv activity in AI/CTR categories has been idle for several days.

## Related

- [[synthesis/2026-11-24/arxiv-paper-check|2026-11-24 ArXiv Paper Check]]
- [[synthesis/2026-11-24/arxiv-daily|2026-11-24 ArXiv Daily]]
- [[synthesis/2026-11-24/arxiv-ai-search|2026-11-24 ArXiv AI Search Report]]
