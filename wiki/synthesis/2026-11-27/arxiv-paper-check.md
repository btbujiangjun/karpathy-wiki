---
title: "ArXiv Paper Check — AI & CTR (2026-11-27)"
type: synthesis
created: 2026-11-27
updated: 2026-11-27
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=100
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR&sortBy=submittedDate&sortOrder=descending&max_results=100
  - https://export.arxiv.org/api/query?search_query=all:%22click+through+rate%22+OR+all:%22click-through+rate%22+OR+ti:CTR+OR+all:%22CTR+prediction%22+OR+all:%22click-through+rate+prediction%22&sortBy=submittedDate&sortOrder=descending&max_results=100
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

# ArXiv Paper Check — AI & CTR (2026-11-27)

> **Window note:** Queried via the arXiv Export API at ~2026-11-27T02:21Z. Strict last-24h window: **2026-11-26T02:21Z → 2026-11-27T02:21Z**. AI = `cat:cs.AI`; CTR = keyword sweep (`all:"click through rate" OR all:"click-through rate" OR ti:CTR OR all:"CTR prediction" OR all:"click-through rate prediction"`) + CTR-relevant `cat:cs.IR` (**arXiv has no "CTR" category**; click-through-rate prediction lives in `cs.IR`, with CTR models also posted to `cs.LG`/`cs.CL`). **Result: 0 new AI papers and 0 new CTR papers in the strict last-24h window — arXiv is quiet.** There is no in-window pick to summarize. The "most interesting" papers below are the **freshest available submissions just outside the window** (2026-11-25 submissions; CTR keyword matches as old as 2026-11-19), clearly labeled. Abstract/metadata-level screening only — no full-text review; all metrics and claims are author-reported. (See also same-day sibling [[synthesis/2026-11-27/arxiv-ai-search|arXiv AI Search 2026-11-27]], which sweeps a wider 7-day window across more categories.)

## Coverage table

| Lane | Query | Fetched | New in strict last-24h window | Newest available |
|------|-------|---------|-------------------------------|------------------|
| AI | `cat:cs.AI` (sorted by `submittedDate`, top 100) | 100 | **0** | `2611.34942v1` 2026-11-25T18:59:57Z |
| CTR home category | `cat:cs.IR` (sorted by `submittedDate`, top 100) | 100 | **0** | `2611.34576v1` 2026-11-25T15:41:52Z (retrieval/recommendation; freshest *CTR-relevant* `cat:cs.IR` is `2611.25659v1` 2026-11-19) |
| CTR keyword sweep | `all:"click through rate" OR all:"click-through rate" OR ti:CTR OR all:"CTR prediction" OR all:"click-through rate prediction"` | 100 | **0** | `2611.25659v1` 2026-11-19T07:40:54Z (DNA: Unlocking Depth Scaling in CTR Models) |

## Result

**0 new papers in the strict last-24h window (2026-11-26T02:21Z → 2026-11-27T02:21Z) in both lanes.** Consistent with sibling reports ([[synthesis/2026-11-25/arxiv-paper-check|2026-11-25]], [[synthesis/2026-11-24/arxiv-paper-check|2026-11-24]], [[synthesis/2026-11-23/arxiv-paper-check|2026-11-23]]): in this arXiv data stream, new submissions land in bursts ~18:45–19:00Z once daily; the freshest announcement is 2026-11-25T18:59Z, i.e. ~7.4 h before query time, but nothing was submitted inside the last 24 h. arXiv `updated` timestamps on window-crossing entries did not pull any older paper into the window (`published` governs "new").

## Most interesting papers — freshest available (OUTSIDE strict window)

### AI lane (submitted 2026-11-25 unless noted)

1. **Attack Policy Selection can Mislead Monitor Evaluators** — [arXiv:2611.34934v1](https://arxiv.org/abs/2611.34934v1) (cs.LG; cross-listed cs.AI; submitted 2026-11-25T18:59:28Z)
   **Authors:** Charlie Griffin, Oliver Makins, Asa Cooper Stickland, Alessandro Abate, Yarin Gal, Abby D'Cruz, Xander Davies
   **Key contribution:** AI-safety evaluation study. Measured false-negative rate of an ex-production OpenAI monitor is highly sensitive to attack-policy generation method and optimization level: **0.5% → 20.8% across optimization levels of a single RL method; 6.4% → 23.0% across methods at best optimization (optimized prompting vs. transcript editing)**. All attack policies were built against proxy monitors only, yet **transfer to a held-out GPT-5.4 target monitor**; artifacts like side-task reasoning absent from monitor-visible instructions affect judgments. Conclusion: monitor-evasion evals using only basic attacks can give false confidence; any particular number needs a separate legitimacy argument that proxies are informative. (single-source; author-reported numbers; case-study monitor.)

2. **Diverse Alternative Reasoning Traces for Hard Math Problems** (DART) — [arXiv:2611.34928v1](https://arxiv.org/abs/2611.34928v1) (cs.CL; cs.AI, cs.LG; NeurIPS 2026 Workshops per arXiv comment; submitted 2026-11-25T18:59:11Z)
   **Authors:** Lukas Aichberger, Adam Golinski, Arno Blaas, Arwen Bradley, Jacob Springer, Mehrdad Farajtabar, Michael Kirchhof, Sinead Williamson
   **Key contribution:** Trace-mining for post-training math LLMs. Starts from a **rejected** trace, decomposes it into steps, ranks steps by position-weighted uncertainty, then generates **deliberately distinct alternatives** for highly-ranked steps using reference-answer guidance + a meta-thought. On greedy-unsolved DeepMath-103K, **recovers 37% more problems than independent Monte-Carlo sampling at matched trace count**; generation cost per recovered problem ~identical; **cost per accepted trace 30% lower**; post-trained Llama-3.1-8B-Instruct **best point estimate in 5 of 6 MATH-500/AIME evals**. (single-source; author-reported.)

3. **μ-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents** — [arXiv:2611.34920v1](https://arxiv.org/abs/2611.34920v1) (cs.CL; cs.AI; 28 pages; submitted 2026-11-25T18:58:42Z)
   **Authors:** Qihao Lin, Guanxu Chen, Shuhang Zheng, Xiaoya Lu, Jingyi Yang, Terumi Chiba, Wenyi Yu, Chao Zhang, Zhuan Shi, Jing Shao
   **Key contribution:** New benchmark for joint task completion in **closed-loop full-duplex multi-user voice interaction**. Simulated participants act from isolated profiles (goals/knowledge/permissions) and adapt to agent speech + tool outcomes. 20 domains × 100 scenarios (varying group size, acoustics, follow-ups) = **800 cases (408 tool-augmented, 392 tool-free)**. Metrics: **Joint Task Success** (all goals + privacy + terminal states hold jointly), **Pure JTS** (no unauthorized tool calls), and **Attribution/Threading/Coordination** diagnostics. Across **13 voice agents: proprietary peak 62.24% tool-free / 65.44% tool-augmented; open-weight < 20%**; open-weight lag in multi-turn attribution + threading; larger groups degrade JTS across capable systems. (single-source; author-reported.)

4. **How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches** — [arXiv:2611.34875v1](https://arxiv.org/abs/2611.34875v1) (cs.SE; cs.AI; submitted 2026-11-25T18:37:06Z)
   **Authors:** Aakash Goel, Benjamin Steenhoek, Yu Hu
   **Key contribution:** New **Delta Residue Attribution (DRA)** method: replays agent trajectories, traces each patch unit to its writing step, reverts it, reruns tests to decide necessity. Applied to **7,660 resolved GitHub Copilot CLI trajectories from 18 frontier models (SWE-bench Verified 6,728 + DeepSWE 932)**. Larger patches ≠ over-editing: on SWE-bench Verified extra edits are mostly **tests 61% + docs 13%**; on DeepSWE mostly **code 58%**. Agent *code* necessity ≥ developers' (**NP_code 0.887 vs 0.864 SWE-bench Verified; 0.797 vs 0.785 DeepSWE**; 11/18 models leave less unneeded code); **~11% of agent code units unneeded (89% change behavior)**; debug steps write ~no unneeded code; necessity uncorrelated with resolve rate on SWE-bench Verified, **negatively correlated on DeepSWE (Spearman −0.59, p=0.01)**; DRA pruning removes majority of unneeded code, 89% of pruned patches still resolve. Recommend reporting code necessity + harness-level pruning. (single-source; author-reported; benchmark self-graded.)

5. **ConTra: A Training Framework for Effective Contextual Retrieval via Prefix Generation** — [arXiv:2611.34366v1](https://arxiv.org/abs/2611.34366v1) (cs.IR; cs.AI; 15 pages; submitted 2026-11-25T13:30:46Z) *(retrieval; not CTR)*
   **Authors:** Jiajun Hou, Jingbang Chen
   **Key contribution:** **RL-trained lightweight prefix generator** ("Context That Travels") producing one context prefix per chunk at index time; reward = frozen embedding + reranker feedback + factual verification + length control; augmented text + embedding stored for reuse. New **RealContextBench** (5 collections × 3 controlled interference conditions) + ConTEB eval. **ConTra-2B beats prompted 9B (Anthropic method) and PPLX-4B contextual encoder by up to 3.15 pts; indexing 7.74× faster (short docs) / 2.15× faster; leads standalone methods on RealContextBench after reranking; less distractor-sensitive.** Code/data/models at github.com/SStan1/ConTra. (single-source; author-reported; trained only on ConTEB.)

6. **Spectrum Adaptation of AI-Native Autoencoder Communications with Transfer Learning** — [arXiv:2611.34942v1](https://arxiv.org/abs/2611.34942v1) (cs.NI; cs.AI, eess.SP; submitted 2026-11-25T18:59:57Z) *(AI-native comms; not CTR)*
   **Authors:** Yalin E. Sagduyu, Tugba Erpek
   **Key contribution:** End-to-end physical-layer autoencoder trained on AWGN then **low-latency transfer to fading + front-end impairments via fine-tuning only a budget-constrained informative subset of transmitter/receiver layers** (layer selection = budget-constrained optimization); preserves signal geometry/decision structure; **removes mismatch-induced error floor, approaches full-retrain BER; cuts training time, MACs, energy, fraction of updated parameters.** (single-source; author-reported.)

### CTR lane (no paper inside strict window; freshest available CTR papers)

7. **DNA: Unlocking Depth Scaling in CTR Models** — [arXiv:2611.25659v1](https://arxiv.org/abs/2611.25659v1) (cs.IR; 10 pages; submitted 2026-11-19T07:40:54Z) *(already covered in [[synthesis/2026-11-25/arxiv-paper-check|2026-11-25 sibling]])*
   **Authors:** Caiyuan Li, Wenjie Wu, Yuheng Huang, Xiao Zhou, Silu Zhou, Ke Chen, Zinan Zhao, Xinrui Zeng, Hanmo Xu, Chaoqun Song, Hua Zong, Zongyuan Wu, Hongbin Zhou, Huimin Yi, Zhixuan Zhang, Dan Ou, Haihong Tang
   **Key contribution:** **Dual-stream Nexus Attention (DNA)** for long-behavior-sequence CTR: key/value side is the depth bottleneck; each layer lets the request read the sequence, then each behavior token reads the updated request and **updates itself**, so next layer reads a request-shaped sequence; update once per request, **shared across candidates, linear complexity**. +0.08→+0.26 pt AUC vs cross-attention stacks at equal FLOPs; keeps scaling where 16→28-layer stacks plateau (+0.02 pt); **DNA-4 deployed in Taobao search; online A/B CTR +0.8%, GMV +0.5%.** (single-source; author-reported; industry-deployed.)

8. **X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction** — [arXiv:2611.24283v1](https://arxiv.org/abs/2611.24283v1) (cs.IR; submitted 2026-11-18T11:58:37Z; first three authors contributed equally)
   **Authors:** Alexander Ploshkin, Nikita Stepanov, Alexey Pismenny, Viacheslav Ovchinnikov, Nikolay Savushkin
   **Key contribution:** Ad-ranking CTR framework; **end-to-end trained history compressor + online ranker**; compact history tokens computed **offline, reused across candidates**; ranker uses cross-attention over tokens + recent events; **autoregressive click loss + distillation of candidate-specific click logits from a larger teacher on uncompressed history**; token count + recent-history length tunable to serving budget. Offline NE **−0.81%** vs production baseline; online A/B in large-scale real-time bidding **+4.65% conversion-value +2.96% clicks**, **+15% online inference cost**. (single-source; author-reported.)

9. **Serving-Aligned Entire-Space Conversion Modeling via Click-Through Rate Knowledge Distillation** — [arXiv:2611.15137v1](https://arxiv.org/abs/2611.15137v1) (cs.LG; submitted 2026-11-11T07:25:25Z; window falls just outside last 24 h)
   **Authors:** Pavel Dolin, Xun Zou, Jiatian Wu, Deguang Kong
   **Key contribution:** **Knowledge distillation from logged serving pCTR into ESMM's auxiliary pCTR tower** to fix training–serving mismatch in pCTCVR when serving pCTR differs from the aux tower (ESMM deploys only pCVR). Variants KD-α; best on serving pCTCVR = **KD-0.3**. Ali-CCP: **ROC-AUC +2.1% serving pCTCVR / +1.6% pCVR; PR-AUC +9.9% / +8.8%**; with 5% non-click negative downsampling: mean AUC +1.2% / +0.9%, PR-AUC +8.5% / +4.5%. (single-source; author-reported.)

## Honest framing

- **0 in-window ≠ no activity ever;** it means nothing was `published` inside the measured 24 h. arXiv announces ~once/day; run at ~02:2Z, the freshest possible submissions are ~7.4 h old (2026-11-25T18:59Z).
- **No arXiv "CTR" category exists.** CTR-lane coverage = `cat:cs.IR` + exact keyword sweep (`click through rate` / `click-through rate` / `CTR` / `CTR prediction` / `click-through rate prediction`); CTR models also appear under `cs.LG`. Primary-category mis-tagging can hide CTR papers; keyword sweep mitigates.
- Picks **1–9 are outside the strict last-24h window**, labeled as such; picks are my curated selection of "most interesting," not exhaustive; ordering not a ranking.
- **Metrics are author-reported** from abstracts; no full-text verification; no reproduction. Confidence marks `(single-source)`.
- Method note: arXiv Export API `sortBy=submittedDate&sortOrder=descending`, max_results=100 per query, `published ≥ now−24h` filter applied client-side. See [[synthesis/2026-11-27/arxiv-ai-search|2026-11-27 arXiv AI Search]] for the wider-window sweep by the sibling job.

## Related

- [[synthesis/2026-11-25/arxiv-paper-check|2026-11-25 ArXiv Paper Check]]
- [[synthesis/2026-11-24/arxiv-paper-check|2026-11-24 ArXiv Paper Check]]
- [[synthesis/2026-11-27/arxiv-ai-search|2026-11-27 arXiv AI Search]]
