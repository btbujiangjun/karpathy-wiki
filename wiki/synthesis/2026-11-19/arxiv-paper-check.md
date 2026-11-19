---
title: "arXiv Paper Check — AI & CTR (2026-11-19)"
type: synthesis
created: 2026-11-19
updated: 2026-11-19
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=100
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR&sortBy=submittedDate&sortOrder=descending&max_results=100
  - https://export.arxiv.org/api/query?search_query=(all:"CTR" OR all:"ctr" OR all:"click-through rate" OR all:"click through rate" OR all:"CTR prediction" OR all:"CTR algorithm")&sortBy=submittedDate&sortOrder=descending&max_results=25
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - advertising
  - retrieval
  - agents
  - agent-memory
  - personalization
  - llm
  - daily-digest
---

# arXiv Paper Check — AI & CTR (2026-11-19)

> **Window note:** Query time ~2026-11-19 02:43 UTC; strict last-24h window **2026-11-18T02:43:24Z → now**. AI = `cs.AI`: **14** new papers in the window; the picks below are the 8 most interesting new ones (all deduped against the existing 2026-11-19 `arxiv-daily.md`/`arxiv-ai-search.md` and earlier sibling reports). CTR = `cs.IR` (the category covering click-through-rate / recommender / advertising literature): **0** new papers in the window; the CTR/click-through-rate keyword sweep across all categories in the same window also returned 0 — the fresh CTR-relevant items of this window (CG2R 2611.22163, CONCORD-Rec 2611.23710, IntentFlow 2611.20448) are already covered by today's sibling reports. All numbers are author-reported; abstract/metadata-level screening only, no full-text review.

## 1) AI — 8 picks from the 14-paper window

### RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop
- **arXiv:** [2611.23855](https://arxiv.org/abs/2611.23855) (cs.AI, cs.CV, cs.RO; submitted 2026-11-18)
- **Authors:** Ghadi Nehme, Dahyun Nam, Akshay Govind Srinivasan, Faez Ahmed
- **Key contributions:**
  - Benchmark where coding agents co-design a robot's hardware and program from standard parts, motors and a custom 3D-printed part; every design that passes in simulation is built and tested on a physical course (135 physical robots).
  - Under public part data, none of 15 initial passing sim designs crossed the real course, so the agent learns the simulator from requested measurements and videos of real runs (real-world feedback closing the loop).
  - 16,427 sims of 12,774 distinct robots (~240 h estimated); four frontier coding agents solve nearly all easy obstacles and invent mechanisms the search baselines don't reach; they falter at harder levels, when one robot must cross every obstacle, and in the real world (66% of sim passes hold across levels).
  - Closing the loop: shown a video of its real failure, an agent redesigns, sometimes correcting its simulator, removing 72% of level-1/2 failures.

### RePlan-VLA: Progress-Aware Replanning for Long-Horizon Vision-Language-Action Models
- **arXiv:** [2611.23843](https://arxiv.org/abs/2611.23843) (cs.RO, cs.AI, cs.LG; submitted 2026-11-18)
- **Authors:** Apoorva Vashisth, Manav Kulshrestha, Damon Conover, Zachary Kingston, Aniket Bera
- **Key contributions:**
  - VLA-agnostic framework that monitors the robot's motion for progress and adaptively revises plans — the underlying VLA policy is preserved with no fine-tuning.
  - RoboCasa365 +21.9% and CALVIN +10.4% success rate over the next-strongest baseline; validated on a real Franka Research 3.

### A System 1 Decision Model for Medical Multiple-Choice Questions Built on Frozen Language Models
- **arXiv:** [2611.23832](https://arxiv.org/abs/2611.23832) (cs.AI; submitted 2026-11-18)
- **Authors:** Pavan Kumar Mantha
- **Key contributions:**
  - Frozen LM encodes question+options to vectors; two small trained heads place them in a shared space; the closest option wins.
  - On MedMCQA (3,842 held-out; chance 25%): plain last-token vectors → 33.1%/33.0% (Qwen3.5-0.8B / Granite-4.2-3B); one-word-summary prompts + lower LR → 41.7%/42.5%; Qwen3-8B → 46.0% ± 0.2 (3 seeds).
  - Shuffling the questions against the options returns accuracy to chance → the heads use the question; Flan-PaLM / Med-PaLM 2 report 57.6%/72.3% on MedMCQA under a different protocol.

### TOGBench: Benchmarking and Improving Tiny-Object Generation Fidelity in Aerial Imagery
- **arXiv:** [2611.23840](https://arxiv.org/abs/2611.23840) (cs.CV, cs.AI; submitted 2026-11-18)
- **Authors:** Chanhwi Jeong, Dongmin You, Seungwook Kim
- **Key contributions:**
  - Quantitative, object-level benchmark for evaluating tiny-object fidelity (vehicles, ships, aircraft occupying few pixels) in aerial imagery.
  - Two simple train/inference-time techniques to improve layout-to-image generators' small-object rendering.

### Evidence-Based Credit Assignment for Search-Augmented Language Models
- **arXiv:** [2611.23824](https://arxiv.org/abs/2611.23824) (cs.AI; submitted 2026-11-18)
- **Authors:** Wen Wang, Jindong Wang, Jiahua Bao, Tu Yongsiqi, Yihao Liu, Junwei He, Wenkui Fan
- **Key contributions:**
  - ECA augments terminal outcome rewards in GRPO with a training-only auxiliary signal measuring how retrieved documents improve the likelihood of a reference answer (evidence-only prompt: question + deduplicated observed documents).
  - ECA-Horizon telescopes the telescoping potential gain; ECA-Step clips per-step increments; cross-fold group normalization, novelty gating, search-local token assignment.
  - Strict macro exact match over the outcome-only baseline: +1.03 pp (Qwen2.5-3B) and +4.80 pp (Qwen2.5-7B-Instruct); outperforms RLOO and GiGPO.

### Metrics-in-the-Loop: Complexity Feedback Reshapes Agent-Written Code
- **arXiv:** [2611.23817](https://arxiv.org/abs/2611.23817) (cs.AI; submitted 2026-11-18)
- **Authors:** Nicolas Chapados, Jean-François Gagné, Nouha Dziri
- **Key contributions:**
  - Inference-time intervention: after each code-changing agent turn, feedback messages name changed functions whose cyclomatic complexity exceeds a limit (complexity feedback) or changed lines skipped by tests (coverage feedback).
  - Complexity feedback reduces erosion (complexity concentration of agent-written code) without affecting held-out correctness; 3 long-horizon coding benchmarks × 4 models.

### Beyond Replacement: Levenshtein Editing for Diffusion Language Models
- **arXiv:** [2611.23750](https://arxiv.org/abs/2611.23750) (cs.CL, cs.AI; submitted 2026-11-18)
- **Authors:** Shuaidi Wang, Zhuocheng Gong, Xuejie Liu, Jianguo Li, Yu Zhang
- **Key contributions:**
  - LED extends replacement-only editing of DLMs with insertion and deletion; two training designs (on-the-fly LCS-aligned edit supervision during SFT; multi-stage training exposing earlier errors).
  - On LLaDA2.1-Mini Base, average score over 12 benchmarks: 54.86 → 57.10 (confidence-guided), 27.52 → 47.19 (confidence-free); tokens per forward 6.14 → 7.05.

### Interpreting Timestamp Permutations in Dynamic Link Prediction
- **arXiv:** [2611.23753](https://arxiv.org/abs/2611.23753) (cs.LG, cs.AI, cs.LO, cs.SI; submitted 2026-11-18)
- **Authors:** Ilia Karpov, Kirill Koloskov, Valeriy Kuleshov, Dmitry Ilvovsky
- **Key contributions:**
  - Crossed diagnostic on MOOC: TCL trained chronologically gains ~8 pairwise-accuracy points vs. permuted training under original evaluation history (changing history at fixed weights: 0.03 pts); 68.37% of queries have unchanged inputs under history changes.
  - Suppressing explicit time encoding reduces the training contrast from 8.03 to 3.64 points; DyGFormer shows a 22.34 vs 0.38 contrast pair across seeds.
  - Turns the permutation gap into interpretable statements about training conditions and model responses.

## 2) CTR — nothing new in the window

- `cs.IR` (the category covering click-through-rate / recommender / advertising literature): **0** new papers in the strict last-24h window.
- The CTR/click-through-rate keyword sweep (`all:"CTR" OR all:"ctr" OR all:"click-through rate" OR all:"click through rate" OR all:"CTR prediction" OR all:"CTR algorithm"`) across all categories in the same window: **0** results.
- Fresh CTR-relevant papers of this window (CG2R 2611.22163, CONCORD-Rec 2611.23710, IntentFlow 2611.20448) were already ingested into today's `arxiv-paper-check.md` (2026-11-18), `arxiv-daily.md` and `arxiv-ai-search.md` (2026-11-19); noted here for completeness.
