---
title: arXiv Daily - 2026-09-06
type: synthesis
created: 2026-09-06
updated: 2026-09-06
tags: [arxiv, daily, LLM, recommendation, CTR, advertising, sequential-modeling, games, game-theory, multi-agent, AI]
---

# arXiv Daily Report — 2026-09-06

> Curated selection of recent arXiv papers across LLMs, recommendation systems, CTR prediction, advertising, sequential modeling, games, and multi-agent systems.
>
> **Note on methodology**: arXiv does not announce on weekends, so Sunday 6 Sep 2026 has no new mailing; the freshest window is the **Fri 4 Sep 2026** mailing. This run re-scanned the cs.IR / cs.LG / cs.AI / cs.CL / cs.GT / cs.MA "recent" listings and features papers that are **fresh to the wiki** (every featured ID grep-verified absent from the 09-01 → 09-05 sibling digests, including `arxiv-ai-search.md` and `game-rl-daily.md`). A few older submission dates (20/28 Jul, 7/20 Aug) appear because the cs.IR recent listing aggregated re-announced / cross-listed entries; each is noted individually. The arXiv API remains rate-limited, so data was gathered directly from listing + `/abs/` pages.

---

## Large Language Models (LLMs)

### 1. TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Jinwei Gan |
| **Institution** | Single-author — *(opencode-compiled)* |
| **arXiv** | [2609.03383](https://arxiv.org/abs/2609.03383) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: Graph-based policy optimization improves credit assignment for long-horizon LLM agents by organizing rollouts into state-transition graphs, but existing methods rebuild the graph inside each policy update, discarding transitions found by earlier policies and limiting advantages to small, batch-local groups. TIGPO keeps a **persistent transition graph per task**, so valid transitions discovered by different policy versions jointly determine credit for current rollouts.

**Key innovations**:
- **Exploration + Revisit slots** — the rollout budget is split between ordinary task sampling and delayed re-attempts of previously explored tasks; each revisit pairs the current group with its earlier Exploration group as a *cross-temporal reference*.
- Stablized relative advantage under small groups, while same-task comparison directly measures policy improvement across training stages.
- Historical transitions/scores are used only as detached structural reference — never replayed in the policy loss.
- Outperforms prior group- and graph-based methods on ALFWorld and WebShop.

---

### 2. Headroom-Drift Replay: A Primitive for Principled Replay Control in GRPO

| Field | Detail |
|-------|--------|
| **Authors** | Hyun Bin Park, Du-Seong Chang |
| **Institution** | Academic (Korea) — *(opencode-compiled)* |
| **arXiv** | [2609.03941](https://arxiv.org/abs/2609.03941) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: Replaying old rollout groups in GRPO can help (recurring skills, agentic search) or hurt (forgetting, mode collapse), and naive replay controls do not distinguish the two. The paper introduces **Headroom-Drift Replay**, a group-level control primitive: *Headroom* ranks candidate stored groups by remaining learning value (a signal-based estimate), and *Drift* gates replay by the group's compatibility with the current policy.

**Key innovations**:
- Heads/Drift act as a single, principled control primitive with **no auxiliary generation or training machinery**.
- Consistently beats naive replay baselines across math reasoning, multimodal reasoning, and Agentic Search.
- A direct complement to the growing family of GRPO modifications (cf. SIGNBALANCE in the 09-05 digest) aimed at making group-relative advantages more robust.

---

### 3. VestigeKV: The NoPE-MLA KV Cache Carries Its Own Eviction Signal in a Vestigial Branch

| Field | Detail |
|-------|--------|
| **Authors** | WenJie Fan |
| **Institution** | Single-author — *(opencode-compiled)* |
| **arXiv** | [2609.03949](https://arxiv.org/abs/2609.03949) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: A long-lived KV cache must be compressed before the queries that will read it exist, so attention-based eviction (H2O, SnapKV) collapses on NoPE-MLA models (0.00–0.33 needle retrieval). On Kimi Linear, **VestigeKV** evicts by a query-independent signal the cache already carries: the 64-dimensional decoupled branch — a vestige of RoPE that NoPE training repurposes into a *salience channel*. Reading just 11% of each row, it partitions the cache: top-m rows stay in the attended tier; all other rows move — exactly, never deleted — to a GPU-resident archive reachable per step by a certified trigger. No training, quantization, or kernel change.

**Key innovations**:
- **Retrieval 1.00 @ 8×, 0.92 @ 32×** from 8k to 65k context — zero gap to full-row selection; attended tier is only **0.25 KB of Kimi Linear's 8.1 KB per-token cache** at 32×.
- Recall tier (standard config) holds 128× at 1.00; host-offload variant reclaims VRAM.
- **NoPE exclusivity** — the identical operator on a RoPE MLA collapses (0.08; plain eviction 0.42); query-independent salience exists only without rotation (top-1 targets span 2.3–6.7% vs 10.2–46.8% of tokens); query-universal exact merging is provably impossible under RoPE.
- Notes plausible extension to Kimi K3's NoPE Gated-MLA variant (cautiously scoped).

---

### 4. Hardware-Aware FP4 FlashAttention-4

| Field | Detail |
|-------|--------|
| **Authors** | Robert Hu |
| **Institution** | Single-author — *(opencode-compiled)* |
| **arXiv** | [2609.04105](https://arxiv.org/abs/2609.04105) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: Blackwell's FP4 tensor cores do not automatically speed up attention, because softmax conversion and on-chip dependencies dominate once matrix products shrink. The paper introduces **Direct-P** for noncausal inference (scores mapped directly to FP4 probabilities) and a **causal path** that passes forward quantization directly into backward.

**Key innovations**:
- Up to **2.13× BF16 forward throughput** on NVIDIA GB200 for noncausal attention.
- Causal path reconstructs probabilities from saved quantized Q/K with FP8 gradient operands — accelerating a complete single-GPU 8B-parameter update by up to **1.14×**.
- Matched distributed training keeps FP8 probabilities/values; **every tested MXFP4 probability/value training trajectory diverges** — a cautionary datapoint for MXFP4 adoption in training.

---

### 5. Post-Training Language Models for Gold-Medal Performance in Coding Competitions

| Field | Detail |
|-------|--------|
| **Authors** | Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Somshubra Majumdar, Boris Ginsburg |
| **Institution** | NVIDIA |
| **arXiv** | [2609.02849](https://arxiv.org/abs/2609.02849) |
| **Submitted** | 2 Sep 2026 (cs.LG) |

**Abstract**: An end-to-end specialization pipeline combining large-scale problem curation, synthetic reasoning traces, SFT, and RL. Using 22,000 curated problems, the authors train **Nemotron-3-Nano-CC** (30B-A3B, SFT+RL) and **Nemotron-3-Ultra-CC** (550B-A55B, SFT), plus **GenCorrect**, a feedback-driven test-time strategy that iteratively generates, evaluates, and refines diverse solutions.

**Key innovations**:
- **IOI 2025**: Nano-CC 130 → 291 after post-training → **468 with GenCorrect**, exceeding the gold threshold (438.3); Ultra-CC reaches 502.
- **IOI 2026 (prospective, live under contest constraints)** — Ultra-CC scores **535.4/600**, above both the gold threshold (361.12) and the top human score (498.27): the first AI system to outscore the highest-scoring human contestant on an IOI problem set.
- Reinforces the trend that post-training + verifier-driven test-time compute, not pretraining alone, unlocks frontier reasoning.

---

### 6. Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Kevin Du, Alexander Hoyle, Laura Ruis, Acyr Locatelli |
| **Institution** | Academic (Princeton / Toronto / Amsterdam et al.) — *(opencode-compiled)* |
| **arXiv** | [2609.04194](https://arxiv.org/abs/2609.04194) |
| **Submitted** | 3 Sep 2026 (cs.CL) — **COLM 2026** |

**Abstract**: Humans and LLM judges evaluate reasoning by reading chain-of-thought, but judged importance may diverge from the steps that actually matter. The paper operationalizes a reasoning step's importance as its **advantage** — the expected change in outcome when that step is removed — estimated via Monte Carlo rollouts, and compares judged importance against this ground truth.

**Key innovations**:
- LLM judges beat a prevalence baseline but **fall short of the noise ceiling** — judged importance is only weakly predictive of causal importance.
- Draws a hard line between *legibility* (how well people can read the trace) and *interpretability* (whether the trace reflects the mechanism driving the answer).
- Dovetails with "Clean Engineering, Unstable Measurement" (below): both are skeptical audits of how LLMs are used as measurement instruments.

---

### 7. Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints

| Field | Detail |
|-------|--------|
| **Authors** | Haoyaun Zhu, Jie Zhang |
| **Institution** | Academic — *(opencode-compiled)* |
| **arXiv** | [2609.04198](https://arxiv.org/abs/2609.04198) |
| **Submitted** | 3 Sep 2026 (cs.AI) |

**Abstract**: LLM judges gate training data, score generations, and drive leaderboards, resting on one rarely tested assumption: the same request sent to the same model name reads the same tomorrow. Two preregistered audits with every threshold fixed in advance audited that assumption across **52,988 requests**. Neither got past instrument validation: same-window repeat rankings agreed at Spearman **0.400** (required 0.90); byte-identical next-day replays at **0.78** (required 0.99).

**Key innovations / findings**:
- Three mechanisms: a label-to-meaning mapping that biased readouts as strongly as the signal; candidate gaps seven orders of magnitude under the instrument's noise floor; and byte-identical inputs returning different rankings, which exact-permutation readouts compound.
- Follow-ups bound the problem: waiting did not help (0.805 vs 0.800 over five days); **four providers share the floor** (medians 0.74–0.88, not predicted by exposed metadata); self-hosting helped only while the server was quiet; readout separation tracks error *type* not size.
- Distills a three-level snapshot-identity ladder, eight design rules, and a reporting checklist; a 2%-scale pilot would have exposed both unreachable gates in advance.

---

### 8. Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems

| Field | Detail |
|-------|--------|
| **Authors** | Jinxi Yu, Yubei Li, Eric Hanchen Jiang, Zhi Zhang, Dong Liu, Wenxiao Zhao, Levina Li, Kai-Wei Chang, Ying Nian Wu |
| **Institution** | Academic (UCLA et al.) + industry — *(opencode-compiled)* |
| **arXiv** | [2609.02264](https://arxiv.org/abs/2609.02264) |
| **Submitted** | 2 Sep 2026 (cs.AI) |

**Abstract**: Current MAS topology designers treat the problem as conditional graph generation with an autoregressive/diffusion search over an N×N adjacency space, ranked by a graph-network proxy. The authors show this formulation is misaligned with the data: surviving topologies collapse to ~6 distinct graphs even as codebook capacity grows 8→64; edge count is negatively correlated with token consumption (Pearson r ≈ −0.4, so sparsifying makes inference *more* expensive); and message-passing scorers are adjacency-invariant whenever agents share a profile — the default in published benchmarks.

**Key innovations**:
- **Codebook Agent**: a VQ autoencoder compresses successful topologies into a query-independent **16-entry codebook**; a reward-weighted MLP maps the query embedding to a code distribution; an MLP proxy over flattened adjacency reranks top decoded candidates in one batched forward pass.
- No iterative search, no message passing at test time — **most accurate on all six benchmarks** (84.6 avg vs 83.0 for strongest prior), emits a topology in **2.4 ms**, and uses **21.9–33.2% fewer LLM tokens**.

---

## Recommendation Systems

### 9. Recommender System as Slow and Fast Thinkers

| Field | Detail |
|-------|--------|
| **Authors** | Zichen Yuan, Xiaoxuan Dong, Linkun Dai, Jinwei Yang, Jining Luan, Dexu Yu, Chunxiao Li, Joemon M. Jose, Youhua Li, Hanwen Du, Junchen Fu |
| **Institution** | Academic (UK/China) + industry — *(opencode-compiled)* |
| **arXiv** | [2609.02671](https://arxiv.org/abs/2609.02671) |
| **Submitted** | 2 Sep 2026 (cs.IR) |

**Abstract**: Sequential recommenders typically use one monolithic model with a fixed inference cost per user. The authors propose **DS-Frame**, an adaptive fast–slow inference framework: a *Fast System* handles routine requests, a *Slow System* refines latents iteratively (system-2 style) for hard cases, and a learned *selector* routes each request under a controllable computation budget.

**Key innovations**:
- Iterative latent refinement (with open-loop / closed-loop self-refinement) allocates compute where it pays off.
- Evaluated on five real-world datasets; boosts existing sequential recommendation backbones and delivers **larger gains on challenging groups** (long-histories, less-mainstream items).
- A clean framing for the latency–accuracy frontier in industrial recommendation.

---

### 10. SPAR: Enhancing Industrial-Scale Generative POI Recommendation via Real-World Spatial Perception

| Field | Detail |
|-------|--------|
| **Authors** | Fangye Wang, Yunjin Gu, Haowen Lin, Yifang Yuan, Song Yang, Xiaojiang Zhou, Pengjie Wang |
| **Institution** | Industry (LBS / e-commerce) — *(opencode-compiled)* |
| **arXiv** | [2609.02062](https://arxiv.org/abs/2609.02062) |
| **Submitted** | 2 Sep 2026 (cs.IR) |

**Abstract**: Generative POI recommendation autoregressively generates a target POI's semantic ID (SID), but existing methods treat geography only as a textual attribute, so predictions are behaviorally plausible yet far from the user's real location. **SPAR** injects real urban spatial knowledge through three synergistic stages.

**Key innovations**:
- **SI-SID tokenization** — longitude–latitude encoded into a sinusoidal geospatial embedding fused with textual semantics, producing RQ-Kmeans SIDs that are simultaneously semantically and geographically consistent.
- **MG-CPT** — continual pre-training on 25 curated geospatial datasets across three tiers (basic attributes, pairwise relations, city-scale navigation).
- **TV-SFT** — the acquired spatial knowledge is anchored as a frozen parameter-space task vector to prevent catastrophic forgetting during behavioral fine-tuning.
- Validated on two public and four industrial-scale datasets.

---

### 11. GenCAR: Generative Counterfactual Alignment with Risk-Controlled Selection for Out-of-Distribution Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Qianqian Wang, Yunshan Li, Jiawen Zeng, Wenwu Gong, Lili Yang |
| **Institution** | Academic (China) — *(opencode-compiled)* |
| **arXiv** | [2609.02162](https://arxiv.org/abs/2609.02162) |
| **Submitted** | 2 Sep 2026 (cs.IR) |

**Abstract**: OOD recommendation usually improves ranking or builds counterfactual candidates *without* controlling the false discovery rate (FDR) of served items. The paper formalizes **α-VCR** (α-Valid Counterfactual Recommendation), retaining candidate support learned from counterfactual supervision while controlling proxy-label FDR, and proposes **GenCAR**.

**Key innovations**:
- Fixes the stable-preference representation while intervening on the environmental factor; grounds offline LLM proposals through preference anchors and trust-radius filtering.
- **Conformal p-values + Benjamini–Hochberg** selection; a Benjamini–Yekutieli guarantee under arbitrary dependence.
- Provable finite-sample, distribution-free FDR control; experiments audit realized false-discovery proportions across benchmarks.

---

### 12. Beyond Modality Harmony: Orthogonal Purification and Topology-Guided MoE for Conflict-Aware Multimodal Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Jialin Liu, Zhaorui Zhang, Ray C. C. Cheung |
| **Institution** | Academic (City University of Hong Kong et al.) |
| **arXiv** | [2609.02152](https://arxiv.org/abs/2609.02152) |
| **Submitted** | 2 Sep 2026 (cs.IR) — **ACM Multimedia 2026** |

**Abstract**: Multimodal recommenders assume "modality harmony" — that multimodal features are inherently aligned with collaborative signals — but deceptive clickbaits and mismatched semantics make modality–topology conflicts ubiquitous. **OrthoRec** replaces blind integration with conflict-aware handling.

**Key innovations**:
- **CGOP (Collaborative-Guided Orthogonal Purification)** — decouples multimodal features into directions parallel and orthogonal to a pure collaborative anchor, truncating orthogonal noise with an energy-preserving normalization.
- **TAR-MoE** — topology-aware routing with *decoupled sigmoid gating* to break softmax's zero-sum bottleneck and set each purified modality's injection scale.
- **Safe-SSL** objective that dynamically penalizes forced contrastive alignment of contradictory pairs.
- Consistently outperforms recent baselines on three Amazon datasets, with better robustness under modality noise and item sparsity.

---

### 13. Training seeds and model-selection stability in recommender-system evaluation

| Field | Detail |
|-------|--------|
| **Authors** | Juan Manuel Rodriguez, Oleg Lesota, Antonela Tommasel |
| **Institution** | Academic (JKU Linz / UNICEN) |
| **arXiv** | [2609.02499](https://arxiv.org/abs/2609.02499) |
| **Submitted** | 2 Sep 2026 (cs.IR) — **RecSys 2026 (Research & Practice Notes)** |

**Abstract**: RecSys experiments usually run a single random seed, assuming run-to-run stochasticity barely affects conclusions. The paper tests that assumption by fixing the data partition and varying the training seed across hyperparameter configurations, analyzing effects at three levels: user-level metric sensitivity, validation-based model selection, and recommendation-list agreement.

**Key innovations**:
- Seed variation is **often detectable**, and its impact depends on whether configurations are clearly separated, whether validation transfers to test, and whether similar scores yield similar top-k lists.
- Argues single-seed results can overstate stability, and training seeds should be part of the evaluation protocol — **not incidental implementation noise**.
- A methodological companion to this wave's LLM-judge reliability findings (see Clean Engineering, #7): both audit measurement stability in evaluation.

---

### 14. RecEvolve: A Knowledge-Driven Autonomous Agent System for Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Weidi Pan, He Ma, Shuhao Ye, Palaksh Rungta, David McPeek, Junyi Jiao, Arnab Bhadury, Mingyan Gao, Onkar Dalal |
| **Institution** | Industry (production Two-Tower retrieval) — *(opencode-compiled)* |
| **arXiv** | [2609.01622](https://arxiv.org/abs/2609.01622) |
| **Submitted** | 20 Jul 2026 (cs.IR) — target RecSys '26 *(re-announced in the 4 Sep window)* |

**Abstract**: An autonomous agent system that delegates the entire ML research lifecycle — idea generation, code, offline training, metric evaluation — to a closed loop deployed directly on a **production-scale Two-Tower retrieval model**. It executed 40+ autonomous training runs from scratch under production-grade evaluations.

**Key innovations**:
- Autonomously navigated hidden architectural bottlenecks, achieving a **~20% relative NDCG improvement**, translating to **+3.77% user satisfaction** in live traffic.
- The agent **autonomously discovered reward-hacking shortcuts** in the standard evaluation protocol — real evidence that autonomous pipelines stress-test experimental infrastructure, exposing failure modes (reward hacking, redundant exploration of failed hypotheses).
- One of the first published empirical validations of self-iterating agentic research inside a live recommender stack.

---

### 15. The Utility of LLMs in Recommender Systems Explanation Evaluation

| Field | Detail |
|-------|--------|
| **Authors** | Kathrin Wardatzky, Oana Inel, Luca Rossetto, Abraham Bernstein |
| **Institution** | Academic (University of Zurich) |
| **arXiv** | [2609.01627](https://arxiv.org/abs/2609.01627) |
| **Submitted** | 7 Aug 2026 (cs.IR) — **ACM RecSys 2026** *(re-announced in the 4 Sep window)* |

**Abstract**: Choosing an explanation method for recommender systems is hard: user studies are unfeasible at scale, automated metrics either assess abstract outputs or need unavailable ground truth, and LLM judges have been proposed but not rigorously validated. This paper generates 18 explanation prototypes, evaluates them with **14 LLMs across two temperature settings**, and compares against human ratings from a user study.

**Key innovations**:
- LLMs show human-like rating patterns and moderate rank correlation with humans, but **absolute agreement is low** and varies substantially by model size and evaluation construct.
- Four practical recommendations: keep explanation-generation prompts concise, prefer larger models for evaluation, pre-test evaluation constructs, and audit for factual accuracy (neither humans nor LLMs reliably detect non-factual content).

---

### 16. Imagine Before Retrieval: Prospective Skill Retrieval for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Shuo Liu, Yutong Yang, Haohao Xiao, Mouxing Yang, Xi Peng |
| **Institution** | Academic (Sichuan University et al.) |
| **arXiv** | [2609.01642](https://arxiv.org/abs/2609.01642) |
| **Submitted** | 28 Aug 2026 (cs.IR) *(re-announced in the 4 Sep window)* |

**Abstract**: Skill retrieval gives LLM agents procedural knowledge for a task, but task queries and skills are written from different perspectives — *objective-oriented* vs *procedural-oriented* — creating a **Query–Skill Misalignment (QSM)** problem that semantic retrieval cannot bridge. Inspired by human prospective cognition, **SkillDreamer** imagines before retrieving.

**Key innovations**:
- Three steps: infer the *capabilities* needed for task execution; *imagine* how to realize them by generating pseudo skills; use that prospective information to bridge objective queries and execution-oriented skills.
- Improves both skill retrieval and end-to-end execution on SkillRet and SkillUsage, and **generalizes across retrieval models and pipelines** (no retrieval-model retraining required).

---

## CTR Prediction & Advertising

### 17. From Feature Interaction to Feature Transport — A Unified Block for Scalable Recommendation Models

| Field | Detail |
|-------|--------|
| **Authors** | Zichen Luo, Jiachen Guo, Keming Gu, Jie Zhang |
| **Institution** | Industry/academic (TAAC2026 advertising competition) — *(opencode-compiled)* |
| **arXiv** | [2609.01655](https://arxiv.org/abs/2609.01655) |
| **Submitted** | 31 Aug 2026 (cs.IR) — **KDDCUP 2026 Workshop** |

**Abstract**: Unified recommendation models mix non-sequential multi-field features and sequential user behaviors, but interaction-centric designs only mix tokens within a layer. The paper introduces **feature transport** — treating deep unified recommendation as a discrete context-conditioned representation evolution process — and proposes **CRAFT**, a Contextual Residual Adaptive Feature Transport block.

**Key innovations**:
- Summarizes non-sequential features into a **reliability-aware contextual field** that generates residual displacement and memory-preserving signals for intent and sequence representations — context becomes an active *controller* of representation evolution rather than a passive interaction object.
- **TAAC2026 advertising competition**: test AUC **0.838090**, surpassing the previous leaderboard best (0.83798); stacking to six blocks reaches 0.838148; wider hidden dim 0.838106 — scaling on both depth and width.

---

## Sequential Modeling & Time-Series

### 18. TraveL: Transformer-based Multi-view Path Distributional Representation Learning

| Field | Detail |
|-------|--------|
| **Authors** | Fang He, Tao-yang Fu, Wang-chien Lee |
| **Institution** | Academic (Penn State et al.) |
| **arXiv** | [2609.03427](https://arxiv.org/abs/2609.03427) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: Path representation learning for road networks typically encodes co-occurrence between segments and paths into a single vector, ignoring varied traveler behaviors and regional correlations. **TraveL** learns a *distributional* representation of a path **plus its travel starting time**, capturing per-path variability of traveler behavior.

**Key innovations**:
- Distributional encoding decodes possible samples of on-path traveler behavior; a **regional attention** encodes road-segment regional correlations.
- Uses a **Kolmogorov–Smirnov test** to compare sampled traveler behavior against ground truth during training.
- Outperforms SOTA on synthetic and real data: **+14.7% mean K-S distance** for travel-time distribution estimation, **+16.7% MAE** for path similarity, **+3.97% MAE** for destination prediction.

---

## Games, Game Theory & Multi-Agent Systems

### 19. Otter: A Provably MEV-Resilient Automated Market Maker via Surplus Redistribution

| Field | Detail |
|-------|--------|
| **Authors** | Elaine Shi, Mengqian Zhang, Hao Chung, Yuhao Li |
| **Institution** | Academic (Carnegie Mellon University et al.) |
| **arXiv** | [2609.03474](https://arxiv.org/abs/2609.03474) |
| **Submitted** | 3 Sep 2026 (cs.GT) |

**Abstract**: MEV in automated market makers lets block builders profit from ordering and injected trades, costing users and centralizing builders. **Otter** (Optimal Truthful Trading with Excess Redistribution) is a two-asset batch AMM with provable MEV resilience when the consensus layer is censorship-resilient and block space uncongested.

**Key innovations**:
- Makes **truthful behavior a dominant strategy for users and builders** — a builder cannot profit by reordering bids or injecting sybil bids, even when the builder is itself a trader with intrinsic value.
- Introduces the **surplus redistribution** paradigm: residual surplus is redirected to a community-governed smart contract (e.g., subsidizing fees, rewarding LPs) instead of being capturable as MEV.
- An **impossibility result** motivates the censorship-resilience assumption: the guarantees are unattainable if the builder can censor — a formal demonstration that consensus-layer security expands what's achievable at the application layer.

---

### 20. EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments

| Field | Detail |
|-------|--------|
| **Authors** | Zih-Sian Yang, Yi-Hao Chen, Yu-Te Kuan, Cheng-Jui Wu, Chuang-Chieh Lin, Po-An Chen |
| **Institution** | Academic (Taiwan) — *(opencode-compiled)* |
| **arXiv** | [2609.03846](https://arxiv.org/abs/2609.03846) |
| **Submitted** | 3 Sep 2026 (cs.GT) |

**Abstract**: Studies the allocation of indivisible goods among agents with identical additive valuations under **EF1 + Nash Social Welfare**. The threshold problem is strongly NP-complete (inheriting NSW maximization hardness), so the paper analyzes welfare guarantees of arbitrary EF1 allocations and a stronger *prefix-wise* EF1 sequential setting.

**Key innovations**:
- Theory: every EF1 allocation achieves the known e^{−1/e} approximation, but under uniform valuations every EF1 allocation is NSW-optimal; under an ε-small-item condition, all EF1 allocations hit an explicit ratio ρ_n(ε) = 1 − O(ε²).
- **PriorityNet**: deep RL (PPO) with *prospective EF1 action masking* that guarantees prefix-wise EF1 by construction, no post-hoc repair.
- Mean normalized NSW **0.9911** (offline) / **0.9701** (random-order online) over n∈[2,20], m∈[5,100]; beats LPT / least-valued-bundle baselines by +27.10% / +17.87% win-minus-loss.

---

### 21. Classic AI Scaffolding for LLM Social Agents

| Field | Detail |
|-------|--------|
| **Authors** | Anatole Gershman |
| **Institution** | Academic (Carnegie Mellon University) |
| **arXiv** | [2609.01167](https://arxiv.org/abs/2609.01167) |
| **Submitted** | 1 Sep 2026 (cs.MA) |

**Abstract**: LLMs produce locally plausible social turns, but fluent next-turn generation is not enough for social simulation. Encounters like restaurant lunches and hotel check-ins are *bounded social episodes* with roles, scripts, obligations, timing, and closure conditions. **EpisodeSim** is a hybrid LLM-agent architecture that interprets classic-AI structures (scripts, state, obligations) as natural-language control state executed by LLM calls.

**Key innovations**:
- A **World Master** maintains shared reality, builds scenes, adjudicates proposed actions, tracks effects/obligations, and controls closure.
- Small qualitative ablations on two held-out settings support the design claim: LLM fluency supplies local texture, but coherent social simulation needs persistent classic-AI-style scaffolding to organize behavior over time.

---

### 22. Collective creativity in hybrid societies

| Field | Detail |
|-------|--------|
| **Authors** | Mason Youngblood, Katie Mudd, Manuel Anglada-Tort, Cameron Jones, Elena Miu, Diana Omigie, Margaret Schedel |
| **Institution** | Academic (multiple universities) — *(opencode-compiled)* |
| **arXiv** | [2609.02620](https://arxiv.org/abs/2609.02620) |
| **Submitted** | 2 Sep 2026 (cs.AI) |

**Abstract**: Disagreement over whether generative AI enriches or impoverishes culture, the authors argue, conflates two distinct components of creativity: **novelty** (a property of single artifacts) and **diversity** (a property of populations). Creativity under generative AI is best understood as a property of *hybrid collectives* — populations of interacting people and algorithms.

**Key innovations / positions**:
- AI-assisted ideation reliably raises the novelty of individual output while **narrowing aggregate diversity** — but this is not inevitable: because humans and models search in complementary ways, mixed groups can outperform and out-diversify either kind alone, and machine-discovered solutions can persist in human culture.
- The decisive factor is **composition**: which agents are present, in what proportion, and how they are connected. The question shifts from "does AI help or harm creativity" to "which mixtures let individual gains accumulate without eroding collective diversity."

---

## Cross-Cutting Observations

- **Measurement reliability is the theme of this wave.** Three independent papers attack the same problem from different angles: Black-box LLM judges on shared endpoints fail preregistered reliability gates (#7); LLM judges of reasoning miss the noise ceiling because judged ≠ causal importance (#6); RecSys training seeds are detectable and can flip conclusions (#13). Petitioners: validate your instrument before freezing gates.
- **KV cache compression is moving to query-independent signals.** VestigeKV (#3) pairs with 09-05's Random Attention — both argue explicit importance scoring is over-invested; XVestigeKV exploits a *latent*, already-computed signal instead.
- **RL post-training keeps absorbing structure.** GRPO replay control (#2) and temporal graph persistence across policy updates (#1) extend the 09-05 GRPO/modifier family (SIGNBALANCE, just-GRPO), while NVIDIA's gold-medal coding system (#5) shows verifier-driven test-time compute + RL is the recipe for frontier problem-solving.
- **Recommendation is going agentic and risk-aware.** RecEvolve (#14) closes the loop of production rec research itself; GenCAR (#11) introduces formal FDR control for OOD serving; DS-Frame (#9) splits fast/slow inference; orthogonal-purification reframes modality fusion (#12). Evaluators (auditing LLM brand recommendations) also got a standardized protocol from this window (Dice Roll Method, 2609.04047, not featured in full).
- **Advertising/CTR activity this window is still competition-driven** (CRAFT, #17). The broader industry theme — context-centric unified CTR and marginal eCPM — was covered in the 09-05 digest (UniCon / meCPM).
- **DeFi meets mechanism design.** Otter (#19) is a game-theoretic AMM with dominant-strategy truthfulness and surplus redistribution; a concrete application-layer payoff of consensus-level security guarantees.