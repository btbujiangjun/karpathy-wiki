---
title: arXiv Paper Check — AI & CTR (November 10, 2026)
type: synthesis
created: 2026-11-10
updated: 2026-11-10
sources:
  - http://export.arxiv.org/api/query
  - https://arxiv.org/
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - ads
  - generative-recommendation
  - reranking
  - retrieval
  - agents
  - reasoning
  - llm
---

# arXiv Paper Check — AI & CTR (November 10, 2026)

> **Window note:** The user requested papers from the "last 24 hours." As checked on 2026-11-10 10:20 CST, arXiv Export API queries show the most recent announced submissions visible at query time are primarily from **2026-11-05/06/07** (with some late-October/early-November CTR hits). A `submittedDate` filter for strictly the last 24h did not yield a clean fresh batch at query time, consistent with arXiv announcement/indexing timing. This report curates the most interesting **recent** AI and CTR/recommendation/ads papers from the latest available windows (including items surfaced in the repo's 2026-11-10 `arxiv-daily` / `arxiv-ai-search`), with all metrics marked as **author-reported**.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| CTR / Search Ads / Generative Retrieval | **ReuseGR** (2611.04259) | Decouples 7B offline query planning from 0.5B online personalized completion with prefix reuse; reports online CTR +0.93% / RPM +1.05% and 38.9% lower latency. |
| CTR / Numerical Embeddings | **NumEmbBench** (2611.01090) | First open benchmark/taxonomy for numerical embeddings in CTR (18 configs, 6 families) with unified FuxiCTR eval; shows no universal winner and tradeoffs between accuracy/cost. |
| Recommendation / Local Search / Generative Query | **SPADE** (2611.04662) | End-to-end generative query rec for local search with spatiotemporal alignment and diversity; online module CTR +1.88% in A/B. |
| Sequence-level Re-ranking | **Beyond Independent Predictions (ICE/JBM)** (2611.07591) | Models display→impression→click as a browsing journey (vs independent per-item CTR); Taobao A/B clicks +0.70% / revenue +3.67%. |
| Agents / Test-time Compute | **Parallel Agent Teams** (2611.09798) | Teams-of-small-agents in parallel outperform large single teams / independent sampling on long-horizon tasks at equal/competitive cost. |
| LLM Agents / Internals | **Value-Policy Dissociation** (2611.10457) | Shows relative action values are linearly decodable but not always used by policy; proposes Natural Value Transport (NVT) as actuator. |
| Retrieval / CTR infra | **WeSearch** (2611.00530) | Unified model-centric retrieval for WeChat Search; online CTR +0.68% / article clicks/user +2.27%, 41% less retrieval cost, lower latency. |

## 1) CTR, Recommendation, Advertising & Retrieval

### ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix Reuse
- **arXiv:** [2611.04259](https://arxiv.org/abs/2611.04259) (submitted 2026-11-03)
- **Authors:** Xujing Wang, Yufeng Chen, Boxuan Zhang, Chao Wei, Cai Xu, Jie Zhao, Weiru Zhang, Wei Zhao, Ziyu Guan
- **Categories:** cs.IR
- **Key contributions:**
  - **Decoupled planning/completion:** 7B offline planner produces shared SID prefix sets per query; 0.5B online model selects prefixes and completes using request history.
  - **ReuseCut / Path KD / BudgetCut (OPD→GRPO):** balances reuse vs coverage, transfers suffix knowledge, and selects branches under a fixed budget.
  - **Reported (author-reported):** HR@100 +3.83pp, online latency -38.9% vs all-online 0.5B; HR@100 comparable to all-online 7B with 57.7% lower latency. 14-day A/B: CTR +0.93%, revenue/1000 req +1.05%.

### SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local Search
- **arXiv:** [2611.04662](https://arxiv.org/abs/2611.04662) (submitted 2026-11-03)
- **Authors:** Chenxu Wang et al.
- **Categories:** cs.IR
- **Key contributions:**
  - **OA-BPE / STAR / MARS-DPO / SDBS:** aligns tokenization to business value, encodes fine-grained spatiotemporal context, aligns to production impression-clicks, and improves slate diversity.
  - **Reported:** offline HR@5 +5.6%, GeoC@5 -40.3%, Exec@5 +1.9%; 1-week online A/B: module CTR +1.88%, search volume +0.177%, search DAU +0.105%.

### Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking (ICE/JBM)
- **arXiv:** [2611.07591](https://arxiv.org/abs/2611.07591) (submitted 2026-11-05)
- **Authors:** Jiayi Zhang et al.
- **Categories:** cs.IR
- **Key contributions:**
  - Models **display→impression→click** with browsing-depth estimation, suppresses unexposed-item context, and matches click distribution within sequence.
  - **Reported:** 14-day Taobao App A/B +0.70% clicks, +3.67% revenue; full-traffic deployment.

### Numerical Embeddings for CTR Prediction: A Taxonomy, Unified Benchmark, and Open-Source FuxiCTR Extension
- **arXiv:** [2611.01090](https://arxiv.org/abs/2611.01090) (submitted 2026-10-31)
- **Authors:** Heng Yao et al.
- **Categories:** cs.IR
- **Key contributions:**
  - **NumEmbBench:** taxonomy of 18 numerical-embedding configs into 6 families; evaluated across 3 datasets, 9 backbones, 5 seeds with equal-budget tuning in FuxiCTR.
  - **Finding:** no single winner (DEER best mean rank), native-scale changes winners in many settings, and accuracy/cost need not align.

### WeSearch: A Unified Model-Centric Retrieval Framework for WeChat Search
- **arXiv:** [2611.00530](https://arxiv.org/abs/2611.00530) (submitted 2026-10-31)
- **Authors:** Kepu Zhang et al.
- **Categories:** cs.IR, cs.CL
- **Key contributions:**
  - Retrieves query-relevant clusters then ranks atomic docs; relevance-aware training and incremental index updates enable weekly/daily refreshes.
  - **Reported (production):** 1-month full-traffic A/B +0.68% CTR, +2.27% per-user article clicks; 41% retrieval resource reduction, 19ms lower graphic-text latency; 100% production traffic.

## 2) Core AI, LLMs & Agents

### Test-Time Compute Scales Better with Parallel Agent Teams
- **arXiv:** [2611.09798](https://arxiv.org/abs/2611.09798) (submitted 2026-11-06)
- **Authors:** Junlin Wang et al.
- **Categories:** cs.AI
- **Key contributions:**
  - **Parallel agent teams:** sample many small teams in parallel and pick the best team's result (balances collaboration mean with sampling variance).
  - **Reported:** beats one large team on all tested large-team cases and beats independent sampling on 10/12 long-horizon tasks; competitive with a frontier model at equal dollar cost on half the tasks.

### Represented but Not Used: Value-Policy Dissociation in LLM Agents
- **arXiv:** [2611.10457](https://arxiv.org/abs/2611.10457) (submitted 2026-11-07)
- **Authors:** Yuzhang Luo, Mohamed Aghzal, Liangming Pan, Ziyu Yao
- **Categories:** cs.AI
- **Key contributions:**
  - Relative action values are linearly decodable from hidden states even when policy chooses worse actions (**value-policy dissociation**).
  - **Natural Value Transport (NVT)** (learned from hidden-state shifts due to value differences) more consistently influences action preferences than direct readout-direction interventions; closed-loop control improves outcomes in tested settings.

### On Agentic Manipulation Policies (AMP1)
- **arXiv:** [2611.09892](https://arxiv.org/abs/2611.09892) (submitted 2026-11-06)
- **Authors:** Chen Chen et al. (Apple AIML)
- **Categories:** cs.RO, cs.AI, cs.CV, cs.LG
- **Key contributions:**
  - Generalist agentic control across single-arm/bimanual/mobile manipulation without demonstrations/task-specific training; persistent memory improves bimanual performance; strong zero-shot results on benchmarks and real-world tasks.

### CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse
- **arXiv:** [2611.09891](https://arxiv.org/abs/2611.09891) (submitted 2026-11-06)
- **Authors:** Peter Belcak et al. (NVIDIA)
- **Categories:** cs.AI
- **Key contributions:**
  - Compiles LLM reasoning traces into reusable, CPU-executable agentic reasoning caches (ARCs); reports near-frontier performance with 16–291× lower invocation cost and robustness to perturbations.

## Cross-cutting Observations

1. **From independent predictions to journey/slate modeling.** Papers like ICE/JBM, ReuseGR, SPADE, and OneTrans-style slate generation (seen in recent reports) move beyond per-item CTR to sequence/slate-level objectives with online business metrics.
2. **Efficiency through reuse and decomposition.** Prefix reuse (ReuseGR), agentic reasoning caches (CPU-ARC), and parallel agent teams all target compute/latency without sacrificing quality.
3. **Evaluation is maturing.** Open benchmarks (NumEmbBench) and production A/Bs are increasingly paired with offline results; several works report latency/cost alongside CTR/GMV.
4. **Agent internals matter.** Work on value-policy dissociation suggests better mechanisms may come from understanding when internal representations are used, not just whether they exist.

## Caveats

- This is a **curated check** of recent/visible papers, not an exhaustive scan.
- All metrics are **author-reported** unless independently reproduced.
- The "last 24 hours" constraint could not be fully satisfied at query time due to arXiv announcement/indexing timing; the window is labeled explicitly.
- Some affiliations are not exposed in API metadata and are marked/omitted where unknown.
