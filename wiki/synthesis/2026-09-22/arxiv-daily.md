---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Sequential Modeling / Games"
type: synthesis
created: 2026-09-22
updated: 2026-09-22
sources: [arxiv.org]
tags: [arxiv-daily, AI, LLM, advertising, AI-search, recommendation, feed-recommendation, long-sequence, multimodal-retrieval, generative-recommendation, semantic-ID, product-search, sequential-recommendation, time-series-forecasting, state-space-models, recurrent-state, world-models, games, embodied-world-models, long-context, KV-cache, sparse-attention, looped-language-models, speculative-decoding, sequence-parallelism, post-training, GRPO, RLVR, on-policy-distillation, continued-pretraining, FP8, reward-model, agents, multi-agent, agent-routing, agent-memory, LLM-as-judge, retrieval-audit, search-audit, daily-digest]
---

# arXiv Daily Report — 2026-09-22

> **Mailing status**: **Tuesday, 22 September 2026** mailing (processes Mon-21 submissions). Because the `/list/{cat}/new` pages still announce the Mon-21 window (which the 09-21 sibling reports claimed, IDs ≤ 2609.22086), the fresh window was established via an **arXiv API tail sweep**: in-window IDs span **2609.22087–2609.24554** for the parsed categories (486 unique entries after filtering `num > 22086`). Published-date distribution of the window: 09-18 → 72, 09-19 → 207, 09-20 → 145, 09-21 → 58 (plus a handful of earlier strays).
> **Methodology**: Parsed `/list/{cat}/new` for **cs.LG / cs.AI / cs.CL / cs.CV / cs.IR / cs.CY / cs.DC / cs.GT / cs.MA / cs.NE / cs.SI** (all still showing the Mon-21 batch, hence not usable as the fresh window) and switched to `export.arxiv.org` API pagination per category plus **cs.HC**; built a `window_full.json` of 486 unique in-window entries (full authors/abstracts/categories/published) in an approved temp dir under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`. All 486 window IDs were **grep-verified 0 hits in `wiki/`**. Screened every title, deepened ~54 shortlisted abstracts (incl. two non-topical physics-domain entries **explicitly excluded**: 2609.23387 thermodynamics, 2609.23385 particle-physics foundation model), and featured **38 papers + 12 runner-ups**. Every featured/runner-up ID was re-verified **0 hits in `wiki/`** at write time. Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).
> **CTR/ads note**: The direct end-to-end CTR/pCVR-model drought continues (≈9 consecutive windows with ~0 classic CTR-ML papers at the daily layer), and the auto-bidding/oCPX line from 09-21 (OneBid/ADAPT) is silent this window. Ads-adjacent content instead concentrates in **AI-search visibility & audit**: a fitted stage model of brand visibility in GPT/Gemini AI search (Brand-Vis, runner-up) and a cross-lingual Baidu/Google AI-overview source-exposure audit (7.6). Recommendation delivers the window's flagship industrial cluster — two first-party Baidu papers (UNIQUE, MuSeR) plus Walmart GradCIR and YouTube Music LLM rationales — the deepest first-party rec depth observed at the daily layer in recent weeks.

---

## 1. Recommendation, Personalized Search & E-commerce

### 1.1 UNIQUE: A Unified Retrieval and Ranking System for Large-Scale Feed Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Zhuang Liu, Yongkang Fu, Zuodong Yang, Guangxing Chen, Zonggang Wu, Yuqi Lu, Shouke Qin, Shantao Li, Maolin Wang |
| **Institution** | Baidu, Mobile Baidu feed (inferred) |
| **Published** | Announced 22 Sep 2026 (cs.IR) |
| **Abstract** | Industrial mobile feeds serve large-scale, heterogeneous, fast-changing content with a retrieval-ranking pipeline that still suffers two structural defects: (1) **hierarchical quantization instability** in candidate retrieval (hurts long-tail/cold-start) and (2) **information loss** caused by the hard separation between retrieval and ranking stages. **UNIQUE** fuses generative code-based retrieval and target-aware ranking into a **single early-fusion architecture**: end-to-end training under a shared representation while preserving efficient candidate expansion; a **balanced single-layer flat quantization** mechanism (replacing hierarchical quantization) mitigates codebook imbalance and improves long-tail representation. Deployed across **homepage feed, discovery page, and short-video rec of Mobile Baidu** serving large-scale real traffic. |
| **Key Innovations** | (1) One architecture replaces hierarchical quantization + separated retrieval/ranking with flat-quantized, early-fusion generative retrieval⇄ranking; (2) explicit "shared representation for retrieval & ranking" end-to-end training; (3) production results — online A/B **+0.96% total watch duration, +1.08% total distribution volume** with notable gains for new and highly active users; serving at **89 ms P99 latency, 44.23% inference MFU**. |
| **Link** | [arXiv:2609.23718](https://arxiv.org/abs/2609.23718) |

### 1.2 MuSeR: Scalable Long-sequence Recommendation with Multi-interest Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Yongkang Fu, Beining Bao, Yu Jiang, Xiangyu Zhao, Hongyang Wei, Guangxing Chen, Zuodong Yang, Shantao Li, Zonggang Wu, Yuqi Lu, Shouke Qin, Hanmeng Liu, Maolin Wang |
| **Institution** | Baidu + CityU HK (inferred; Xiangyu Zhao) |
| **Published** | Announced 22 Sep 2026 (cs.IR) |
| **Abstract** | Ultra-long user histories (10⁴–10⁵ actions) — even millions of tokens of interpreted text features — carry stable preference signals, but industrial systems truncate to a few hundred actions under latency/memory budgets. **MuSeR** (built on the deployed **MGS** system) integrates: (i) **hierarchical temporal compression** — recent actions at full resolution, older segments progressively pooled → long histories fit a fixed serving budget; (ii) **disentangled multi-query interest extraction** with orthogonality regularization; (iii) **multimodal semantic alignment** augmenting sparse item IDs with LLM-distilled text summaries. Deployment machinery: asynchronous user-representation refresh + adaptive caching + hierarchical beam-search retrieval across heterogeneous hardware. |
| **Key Innovations** | (1) System-level integration, not a new primitive: long-context + multi-interest + multimodal jointly deployable in a real-time production pipeline; (2) hierarchical temporal compression as the budget-safe way to use 10⁵ action histories; (3) online A/B on Baidu APP homepage/discovery/short-video — **+0.26% DAU and +0.89% total session duration (both p<0.05)** with reduced serving latency/cost. |
| **Link** | [arXiv:2609.23677](https://arxiv.org/abs/2609.23677) |

### 1.3 GradCIR: Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search

| Field | Detail |
|-------|--------|
| **Authors** | Anubhav Gupta, Hrushikesh Mohapatra, Prijith Chandra, Asish Mohapatra, Anuj Garg, Arvind Maan, Sudip Datta, Venkat Bulusu, Sitesh Kumar Jalan |
| **Institution** | Walmart Global Tech (inferred) |
| **Published** | Announced 22 Sep 2026 (cs.IR) |
| **Abstract** | Composed image retrieval (CIR — image + modifier text like "color change / style swap") in real e-commerce catalogs is a **graded-relevance** problem: many candidates partially satisfy the query and ranking across that partial-match spectrum drives UX, yet existing CIR trains on binary triplets with a single positive. **GradCIR** provides the supervised recipe: (i) a **VLM curates training data** (object detection + modifier synthesis) producing 4-level relevance labels with no manual annotation; (ii) an **iterative relevance-feedback loop** mining hard negatives from the in-training retriever; (iii) a **hierarchy-aware angular objective** trained directly on graded labels. Instantiated as a PaliGemma2 bi-encoder on 3.5M graded pairs from raw Walmart catalog data. |
| **Key Innovations** | (1) Replaces triplet-binary CIR supervision with graded 4-level relevance (kills the "binary collapse" failure mode); (2) controlled graded-vs-binary ablation: **+4.9–5.9% NDCG@10**, up to **+8.5%** when the recipe is applied to other encoders; (3) deployed live at Walmart serving real visual-search traffic; FashionIQ 0.6703 avg recall ≈ best supervised baseline. |
| **Link** | [arXiv:2609.24152](https://arxiv.org/abs/2609.24152) |

### 1.4 Explainable Recommendations at Scale: LLM Rationales for YouTube Music Artist Discovery

| Field | Detail |
|-------|--------|
| **Authors** | Xiao Liu, Yanwei Song, Srivaths Ranganathan, Yuan Chen, Zheyun Feng, Parker Steenburgh, Jochen Klingenhoefer, Nathan Lasche, Gergo Varady, Tim Steele |
| **Institution** | YouTube Music / Google (inferred) |
| **Published** | Announced 22 Sep 2026 (cs.AI, cs.IR) |
| **Abstract** | Streaming platforms face the exploration-exploitation tradeoff: users want discovery but hesitate to pick unknown artists. Transparent **natural-language rationales** explaining *why* an unexplored item is recommended lower that trust barrier — but LLM real-time inference cost blocks deployment. The paper documents a **decoupled architecture**: LLM inference is isolated **asynchronously offline**, pre-computing personalized candidate pools of undiscovered artists alongside tailored rationales; online serving then only re-ranks/inserts with cheap components. |
| **Key Innovations** | (1) An industry case study where explainability for exploration is decoupled from the latency-critical path (offline LLM pool + rationale pre-computation); (2) a strong claim with production A/B backing: LLM rationales **significantly reduce the trust barrier for novel content** → statistically significant gains in exploration and overall engagement on discovery surfaces. |
| **Link** | [arXiv:2609.23877](https://arxiv.org/abs/2609.23877) |

### 1.5 What Makes a Good Semantic ID for Generative Recommendation? A Reproducibility Study

| Field | Detail |
|-------|--------|
| **Authors** | Yufei Chen, Junchen Fu, Jujia Zhao, Yukun Zhao, Zhaochun Ren |
| **Institution** | Shandong University (inferred; Zhaochun Ren) |
| **Published** | Announced 22 Sep 2026 (cs.IR) |
| **Abstract** | Generative recommendation increasingly represents items by **semantic IDs (SIDs)** — discrete item codes generated token by token — but SID designs vary wildly (construction strategy, codebook organization, code length) with unclear true impact. This large-scale reproducibility study (unified experimental framework) examines: relative effectiveness of competing SID designs; codebook utilization vs recommendation quality; semantic code length; and influence of SID design on local item-semantic preservation. |
| **Key Innovations** | (1) A sobering null-result set: SID-design effects are **largely non-monotonic — no single design is universally best** and RQ-VAE/OPQ behave inconsistently across datasets; (2) codebook utilization is *diagnostic but insufficient* (the most balanced first-level codebook is not the best recommender); (3) scaling the generative backbone or SID length is **not always beneficial**, with complementary strengths across semantic-neighborhood notions — direct caution for the generative-rec line the wiki tracks. |
| **Link** | [arXiv:2609.24430](https://arxiv.org/abs/2609.24430) |

### 1.6 Beyond Raw Engagement: A Counterfactual Observability Framework at Netflix

| Field | Detail |
|-------|--------|
| **Authors** | Chaoran Guo, Ding Tong, Ting-Po Lee, Scarlet Chen |
| **Institution** | Netflix (inferred) |
| **Published** | Announced 22 Sep 2026 (cs.IR, cs.AI) |
| **Abstract** | Raw engagement (views, clicks) conflates content quality, model behavior, presentation bias, and audience reach, making attribution impossible for content creators and model developers. The paper casts recommender observability as a **counterfactual measurement problem**: estimating what the recommender would have done — and what engagement would have followed — in the absence of a specific content item or model decision. Three stakeholder-centered observability principles (bias reduction, relativity, incrementality) plus measurement methodologies for both single-stage and cascading recommenders, all from one measurement foundation, with production deployments at Netflix. |
| **Key Innovations** | (1) Observability as counterfactuals (not raw-signal dashboards) — a general, reusable evaluation frame; (2) explicitly serves two audiences (creators + model developers) from one measurement layer; (3) production-validated across multiple Netflix recommender systems. |
| **Link** | [arXiv:2609.22747](https://arxiv.org/abs/2609.22747) |

---

## 2. Sequential Modeling & Time-Series Forecasting

### 2.1 What Can a Recurrent State Safely Forget?

| Field | Detail |
|-------|--------|
| **Authors** | Linzhe Zhang, Changming Xu |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.LG) |
| **Abstract** | Recurrent models must preserve "future-distinguishing" information while suppressing hidden-state error — two objectives that conflict: **contraction** improves stability but contraction along a future-distinguishing direction destroys memory. The paper formalizes the boundary via the **predictive quotient**: hidden states equivalent when they induce the same conditional future form **predictive fibers**; every semantics-preserving corrector is the identity on the quotient (at regular point with dim d / predictive dim k it can eliminate at most **d−k** directions). Discrete-vs-continuous boundary: finite predictive states admit positive-radius exact correction basins; an uncountable continuum of future-distinguishable states cannot be decoded after arbitrary positive-radius perturbation. An **auditable finite-future framework** (deployment bank W ⊆ audit bank A) plus a certification mechanism with probe complexity O(M·Ω^(−(k+2))), matching minimax lower bound. |
| **Key Innovations** | (1) A clean information-geometric statement of the "remember vs contract" tradeoff in recurrent state space (d−k bound); (2) a deployment/audit certificate constructing a safety-first margin Ω for recurrent compression/recurrent-state editing; (3) matching minimax lower bound on the probe complexity — unusually rigorous for the memory-editing line. |
| **Link** | [arXiv:2609.23366](https://arxiv.org/abs/2609.23366) |

### 2.2 One Patch, Three Roles: What Is Actually Coupled in Autoregressive Time-Series Forecasting?

| Field | Detail |
|-------|--------|
| **Authors** | Ziang Li, Yue Huang, Guoxu Zhou, Na Han, Jie Wen, Lunke Fei, Xiaozhao Fang |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.LG) |
| **Abstract** | Patch-based autoregressive TSF ties **input representation, learned transitions, and recursive execution** to one patch length; the paper asks which roles can be decoupled. Main finding: a frozen parent's **recursive trajectory is easier to fit than the observed future**. **Autoregressive Trajectory Distillation (ATD)** yields selectable ATD-1/2/4/8 execution (ATD-1 exactly recovers the parent), reaching **5.54× end-to-end speedup** with stable quality across widths. Fewer calls do *not* remove the parent's forecast error: ATD improves trajectory fidelity in 21/21 seed runs but forecast accuracy in only 15. A correctable residual projection along a train-selected **periodic-history direction** (Spectrum Tangent, no extra params/Transformer calls) cuts MSE/MAE by ~2.5% at horizon 720 while staying 3.24× faster than recursive inference. |
| **Key Innovations** | (1) Decouples representation / transition / execution as three independent AR design axes (rare in patch-TSF literature); (2) ATD as a distillation-y execution schedule with exact-parent recovery and 5.54× speedup; (3) the trajectory-fidelity-vs-forecast-accuracy mismatch + periodic residual correction — a new, cheap accuracy lever for AR forecasters. |
| **Link** | [arXiv:2609.23686](https://arxiv.org/abs/2609.23686) |

### 2.3 CTRL: Control-Based Time Series Forecasting with LLM-Guided Residual Learning

| Field | Detail |
|-------|--------|
| **Authors** | Minkyoung Kim, Daeun Ji, Yohan Lee, Beomsoo Kim, Beakcheol Jang |
| **Institution** | Sangji University (inferred; Beakcheol Jang) |
| **Published** | Announced 22 Sep 2026 (cs.LG, cs.CL) |
| **Abstract** | LLM-based TSF is torn between reducing LLMs to numerical predictors (bypasses their strengths) and letting them generate forecasts directly (unstable on non-stationary data). **CTRL** decouples semantic reasoning from quantitative prediction: a frozen backbone produces base forecasts; **specialized LLM agents act as controllers** that analyze backbone residual error decomposed into trend / seasonal / irregular components, then emit compact control signals a lightweight residual decoder turns into corrections. Includes **label-free test-time adaptation** that detects distribution shift from input statistics and readapts control signals with only 3–24 LLM calls (cached). |
| **Key Innovations** | (1) Control-theoretic framing: LLM as *controller* of a statistical forecaster rather than forecaster or feature extractor; (2) interpretable decomposition (trend/seasonal/irregular) as the reasoning substrate; (3) cheap label-free drift adaptation — purpose-built for non-stationary deployment, while remaining competitive on stationary data. |
| **Link** | [arXiv:2609.23257](https://arxiv.org/abs/2609.23257) |

### 2.4 TAC-Time: Texts as Channels For Multimodal Time Series Forecasting

| Field | Detail |
|-------|--------|
| **Authors** | Jiayi Liang, Xiaotian Gu, Xinyu Xie, Yuanbin Wu, Xiaoling Wang |
| **Institution** | East China Normal University (inferred; Yuanbin Wu / Xiaoling Wang) |
| **Published** | Announced 22 Sep 2026 (cs.CL, cs.AI, cs.LG, cs.MM) |
| **Abstract** | Most TSF uses numeric observations only, discarding contextual text. Prior multimodal attempts treat text as static features or use LLMs as forecasting backbones (loses temporal dynamics, high compute). **TAC-Time** converts **text into additional temporal channels** — text features are jointly modeled with numeric sequences in a shared temporal backbone, preserving temporal continuity/periodicity while staying efficient. Systematic interpretability via attention + frequency-domain analyses shows strong cross-modal dependencies; correlation-aware alignment of predictive textual signals yields partial forecasting gains. |
| **Key Innovations** | (1) Text-as-channels (not features, not backbone) — orthogonal to the LLM-forecaster trend; (2) first cross-modal interpretability analysis (attention/frequency) for text-conditioned TSF; (3) the partial-gains honesty: alignment helps cerain signals only, reported with ablations. |
| **Link** | [arXiv:2609.24156](https://arxiv.org/abs/2609.24156) |

### 2.5 TWIG: A Time-Causal Wavelet Operator for Autoregressive Forecasting on Irregular Graphs

| Field | Detail |
|-------|--------|
| **Authors** | Subashree Venkatasubramanian, David A. Barajas-Solano, Chuyang Liu, Daniel M. Tartakovsky, Dipankar Dwivedi |
| **Institution** | PNNL + Univ. Alabama (inferred; Tartakovsky / Dwivedi) |
| **Published** | Announced 22 Sep 2026 (cs.LG) |
| **Abstract** | **TWIG** is a graph-native neural operator for autoregressive surrogate modeling on static irregular graphs: each node history is transformed into **causal multiscale temporal features** (recent variation vs progressively slower memory components), propagated through graph-wavelet operator blocks with gated pointwise channel mixing. Causal by construction and designed for **closed-loop forecasting** (predictions recursively reused). Evaluated on three irregular-domain forecasting problems — regional diffusion, 3D subsurface hydrology, aerodynamic flow — with 400–5,233-node graphs and ~70k–10M parameter models. |
| **Key Innovations** | (1) Causal-by-construction multiscale temporal encoding combined with graph-wavelet operators (stable autoregressive closed-loop); (2) lowest rollout errors on subsurface-hydrology + regional-diffusion and second on 10M-param aerodynamic flow (behind GPS Transformer); (3) consistently beats the non-time-causal Graph WNO baseline — a solid operator-style advance for spatiotemporal physical surrogates. |
| **Link** | [arXiv:2609.22585](https://arxiv.org/abs/2609.22585) |

---

## 3. Post-Training, RL & Distillation

### 3.1 1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Huanxin Sheng, Zhiling Ye, Haonan Wang, Jian Wang, Jinjie Gu, Jian Kang |
| **Institution** | (academic/industrial, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.LG, cs.CL) |
| **Abstract** | Sparse on-policy distillation (OPD) supervises only a small token subset of student trajectories — but even useful teacher guidance yields **noisy gradient estimates** from a sampled next token. The paper studies this estimation problem on the teacher's fixed prefix via **information geometry** and derives an **information-efficiency ratio (IER)** from a signal-to-noise decomposition; IER characterizes relative gradient-estimation error under an optimal scalar baseline. A candidate-set approximation enables token selection from IER (+ combination with usefulness scores), keeping the sampled reverse-KL objective. |
| **Key Innovations** | (1) Formalizes *gradient-estimation reliability* (not just usefulness) as the missed axis of sparse-distillation token selection; (2) IER improves existing selectors on math + medical reasoning, with sparse configs matching/beating full OPD at **0.1–1% token budgets**; (3) pairs cleanly with the window's TrustMOPD (3.2) — both amortize token-level teacher reliability. |
| **Link** | [arXiv:2609.24432](https://arxiv.org/abs/2609.24432) |

### 3.2 Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Jie Sun, Mao Zheng, Mingyang Song, Zeyuan Liu, Gengsheng Li, Houcheng Jiang, Yilin Cheng, Bichuan Feng, Yuchen Cai, Junfeng Fang, Xiang Wang |
| **Institution** | USTC + industrial (inferred; Xiang Wang) |
| **Published** | Announced 22 Sep 2026 (cs.CL, cs.LG) |
| **Abstract** | Multi-teacher on-policy distillation should let a student learn from complementary specialists on its own trajectories, but domain-routing selects one teacher per *example* and fixes it for the whole response — depending on labels mixed corpora lack and failing when expertise changes *within* a trajectory. **TrustMOPD** replaces example-level selection with **label-free, token-level supervision allocation**: at each student-generated prefix, it uses each specialist's RL-induced displacement from a shared pre-RL reference as a **local reliability proxy**, calibrates across teachers, and constructs a weighted distillation target. |
| **Key Innovations** | (1) Token-level, label-free, prefix-conditioned teacher allocation — kills the fixed-domain-routing pathology; (2) strong recovery numbers when label-free: recovery ratio **54.4%→91.5% (SingleCap)** and **54.5%→98.0% (MultiCap)**, approaching label-based MOPD; (3) an elegant negative result: *prefix-independent* random token weights ≈ uniform — supervision must be conditioned on the evolving generation context. |
| **Link** | [arXiv:2609.23697](https://arxiv.org/abs/2609.23697) |

### 3.3 RLVR²: Reinforcement Learning with Verifiable Rubric-based Ranking

| Field | Detail |
|-------|--------|
| **Authors** | Hao Li, Zhengkun Zhang, Gangqiang Hu, Zhen Zhang, Yude Gao, Dai Dai, Jing Liu |
| **Institution** | Institute of Computing Technology, CAS (inferred; Dai Dai / Jing Liu) |
| **Published** | Announced 22 Sep 2026 (cs.LG, cs.AI) |
| **Abstract** | RLVR is expanding from provable signals (math, code) to **multi-dimensional rubric** quality requirements, but policy optimization consumes one scalar per rollout — so rubric scores must be aggregated. Prescaling + linear combination assumes cardinal score differences are comparable across heterogeneous criteria and that gains compensate failures, both unreliable. **RLVR²** converts rubric scores into **criterion-specific within-group ordinal outcomes**, recovers a latent utility from the comparison matrix, and merges utilities into one training signal — discarding raw magnitudes and avoiding heterogeneous scale calibration. Supports **objective-preserving attribute adjustment** for auxiliary attributes correlated with rankings but not objectives. |
| **Key Innovations** | (1) A verifiable *ranking* paradigm (ordinal, within-group) instead of score-scaled rewards — removes cross-criterion calibration assumptions; (2) latent-utility recovery from comparison matrices as the rubric→scalar bridge; (3) attribute adjustment without expanding the objective — useful when rubric correlates with (but should not reward) a confound. |
| **Link** | [arXiv:2609.23457](https://arxiv.org/abs/2609.23457) |

### 3.4 Fathom-Vaidya: Advancing Medical Reasoning with Rubric-Based Rewards

| Field | Detail |
|-------|--------|
| **Authors** | Kalash Shah, Kunal Singh, Snehan J, Shreyas Singh |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.AI, cs.CL, cs.LG) |
| **Abstract** | Deploying LLMs in healthcare needs two complementary reasoning dimensions: **diagnostic reasoning** (convergent; infer condition from data) and **clinical healthcare reasoning** (navigational; multi-turn interaction with no single correct answer). HealthBench / MedXpertQA show weaknesses in both. **Fathom-Vaidya** is a sequential training framework on synthetic data + rubric-based RL: (1) MedBullets-derived diagnostic questions with rule- and rubric-guided RL; (2) 5.3k synthetic multi-turn clinical scenarios with multi-dimensional rubrics. |
| **Key Innovations** | (1) Explicit dual-target training (diagnostic + interactive clinical) under one rubric-based RL roof; (2) **>10% improvement on MedXpertQA**; a 30B model hits **50.1% on HealthBench-Hard**, surpassing proprietary baselines including GPT-5 (thinking); (3) evidence that targeted synthetic datasets + rubric-based training can systematically close both medical-reasoning gaps. |
| **Link** | [arXiv:2609.24480](https://arxiv.org/abs/2609.24480) |

### 3.5 Time-Incremental Continued Pretraining of LLMs: Knowledge Updates Without Catastrophic Forgetting

| Field | Detail |
|-------|--------|
| **Authors** | Fırat Öncel, Salman Hussain Ali, Mirco Ravanelli, Cem Subakan, Çağatay Yıldız |
| **Institution** | Meta + Concordia + Laval (inferred; Ravanelli / Subakan) |
| **Published** | Announced 22 Sep 2026 (cs.CL) |
| **Abstract** | LLMs become stale the moment pretraining ends; CPT is the remedy but prior evaluation uses a continual-learning lens assuming disjoint streams — a poor fit for **time-incremental updates on web-scale crawls with overlapping snapshots**. This study runs CPT on FineWeb-Edu dumps strictly *after* each model's knowledge cutoff across 6 open-weight models × 3 families × 1–8B scales. Four practical findings: (i) knowledge is acquired heterogeneously but **without catastrophic forgetting** (5/6 also improve pre-cutoff recall; gains track pretraining saturation = token budget per parameter); (ii) ~zero cost — macro-average stays within 0.01 of base; (iii) recipe: **data quality dominates quantity** (6B curated ≈ 40B broad), LR optima for acquisition vs capability differ by ~1 order of magnitude, LoRA at sufficient rank matches full CPT; (iv) CPT gains survive deployment (transfer §). |
| **Key Innovations** | (1) The right evaluation regime for web-scale CPT (overlapping snapshot streams, strictly post-cutoff data, 6-models/4-scales grid); (2) a concrete recipe (curated 6B > broad 40B, separate LRs, LoRA parity) directly actionable for wiki's continual-learning track; (3) reassuring cost/forgetting numbers — CPT as a cheap, safe knowledge-refresh operation. |
| **Link** | [arXiv:2609.23916](https://arxiv.org/abs/2609.23916) |

### 3.6 Towards Full Pipeline FP8 Reinforcement Learning for LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Fanchao Chen, Ziheng Jiang, Ziyun Wei, Zheng Zhong, Du Li, Chi Zhang, Haibin Lin, Shivaram Venkataraman |
| **Institution** | (industrial + UW-Madison; inferred; Venkataraman) |
| **Published** | Announced 22 Sep 2026 (cs.LG, cs.AI) |
| **Abstract** | FP8 quantization accelerates RL for reasoning/agentic LLMs but prior work fixates on train-inference mismatch (e.g., TIS) while **full-pipeline FP8 RL** still shows severe instability: mid-training entropy surges and garbled outputs. The paper traces it to a previously overlooked cause — **compounded FP8 noise distorts the importance ratio**, disproportionately pushing negative-advantage tokens outside the trust region and zeroing their gradients, so pathological outputs are never penalized. Fix: **Calibrated Clipping**, aligning FP8 clipping bounds with BF16 distributions by matching the lower-bound clipping quantile and rebalancing the upper bound. |
| **Key Innovations** | (1) New instability mechanism (importance-ratio distortion → negative-advantage token gradient zeroing) distinct from the TIS line; (2) a simple, dynamic clipping calibration, eval across **GRPO and DAPO, 8B–32B scales, multiple FP8 granularities**; (3) eliminates entropy surges and restores BF16-comparable performance — key for cost-reducing RL training pipelines. |
| **Link** | [arXiv:2609.22870](https://arxiv.org/abs/2609.22870) |

### 3.7 FLARE: A Full-Lifecycle Dense Supervision Paradigm for Long-Horizon Coding Agents via Generative Reward Model

| Field | Detail |
|-------|--------|
| **Authors** | Jingxuan Xu, Gang Wu, Yanan Wu, Yutao Mou, Songwei Yu, Tianzhuang He, Zhengshuo Gong, Zhao Liu, Zihang Xu, Wenqiang Zhu, Xinping Lei, Weihao Li, Yuhui Bai, Zhongqiu Wang, Yan Wu, Ariel Deng |
| **Institution** | (industrial, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.CL, cs.AI) |
| **Abstract** | Test-time scaling helps LLM coding agents, but **sparse Pass/Fail rewards** create a credit-assignment crisis and waste failed exploration. **FLARE** = a dense-supervision paradigm driven by a lightweight **Generative Reward Model (GRM)**. First, **RADAR** (offline, causal-aware diagnostic) extracts hindsight-free step-level supervision via causal-chain backtracking to distill the GRM. Then the GRM runs the full lifecycle: at inference as an **Active Scaffold** intercepting high-risk generation steps for localized breakpoint re-execution; at post-training, its signals serve as process-supervised reranking for SFT and step-level dense rewards for RL (mitigating policy collapse in sparse environments). |
| **Key Innovations** | (1) Generative reward model → step-level dense rewards across inference + SFT + RL (a unified dense-supervision stack for coding agents); (2) hindsight-free causal-chain supervision (RADAR) addresses the "pass/fail obscures" problem structurally; (3) **new Pareto frontier: FLARE (N=1) beats Global Rollout (N=5) at 5× lower token consumption**. |
| **Link** | [arXiv:2609.23808](https://arxiv.org/abs/2609.23808) |

---

## 4. Long-Context, KV-Cache & Inference Efficiency

### 4.1 ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Junyoung Park, Jungwook Choi, Mingu Lee |
| **Institution** | Hanyang University (inferred; Jungwook Choi) |
| **Published** | Announced 22 Sep 2026 (cs.LG, cs.AI) |
| **Abstract** | Modern LLMs — QK-normalization, gated attention, learned attention sinks, logit softcapping — exhibit **weaker persistent attention sinks**, the very anchor most KV eviction relies on. The paper observes weaker sinks co-occur with **greater value-vector dispersion relative to key dispersion**, motivating **ValueDiff**, a value-geometric eviction that ranks tokens by the L2 deviation of their value vectors from the cache mean (also arises as minimal-disturbance eviction under a max-entropy assumption on future attention). |
| **Key Innovations** | (1) Shifts the eviction signal from key/attention geometry to **value geometry** — right for the sink-suppressed generation of models; (2) at a tight 2k budget on RULER: **88–99% of dense across 7 sink-suppressed models** (best on 6/7); LongBench 4k: 92% vs 83% prior best; MATH-500: strongest non-dense method at 25% cache on every sink-suppressed model (up to ~20 pts on gated attention); (3) a query-invariant, training-free signal — deployable anywhere eviction happens. |
| **Link** | [arXiv:2609.23314](https://arxiv.org/abs/2609.23314) |

### 4.2 Block-Sparse Attention with Semantic-Geometric Decoupled Routing

| Field | Detail |
|-------|--------|
| **Authors** | Xinwei Long, Weigao Sun, Weibo Gao, Pengkun Jiao, Biqing Qi, Feida Zhu, Yiran Zhong, Steven Hoi, Bowen Zhou |
| **Institution** | Shanghai AI Lab-aligned (inferred; Bowen Zhou / Yiran Zhong) |
| **Published** | Announced 22 Sep 2026 (cs.CL, cs.AI) |
| **Abstract** | Block-sparse attention routes each query block to a few key blocks, but accurate **training-free** block routing is hard: existing routers pool post-RoPE token representations, entangling semantic aggregation with RoPE-induced geometry and attenuating local positional cues via high-frequency phase cancellation. **Semantic-Geometric Decoupled Routing** fixes this: semantic aggregation is moved to the **pre-RoPE space**, and geometric bias is reconstructed from an offline structural prior + relative block distances — yielding an explicit closed-form routing score without token-level search or post-hoc calibration. |
| **Key Innovations** | (1) A clean diagnosis (RoPE phase cancellation corrupts semantic pooling) plus a principled pre-RoPE/structural-prior fix; (2) closed-form scores → near-full-attention accuracy across **4K–128K contexts** on text + video tasks; (3) **5.03× speedup over FlashAttn at 128K** with routing overhead <3.4 ms. |
| **Link** | [arXiv:2609.22884](https://arxiv.org/abs/2609.22884) |

### 4.3 WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Hyeongju Ha, Jae-Joon Kim |
| **Institution** | POSTECH (inferred; Jae-Joon Kim) |
| **Published** | Announced 22 Sep 2026 (cs.LG) |
| **Abstract** | **Looped LMs** reuse one weight-shared block for effective depth without more parameters, but T sequential recurrent-block calls per token spike decode latency. **Wavefront Decoding (WFD)** is a training-free self-speculative method exploiting two looped-LM properties: intermediate recurrence outputs are effective draft predictions, and weight-sharing lets mixed-depth token states be processed in one batched block call. WFD organizes them into a **diagonal wavefront** — continuously drafting new positions at shallow depth while advancing earlier positions toward full-depth verification — co-batching draft and verify (vs phase-separated draft-then-verify). |
| **Key Innovations** | (1) Replaces draft-then-verify with a diagonal wavefront schedule that inherently overlaps drafting and verification; (2) **2.42× (Ouro-2.6B) and 3.54× (Huginn-3.5B)** over autoregressive decoding, consistently beating draft-then-verify on Spec-Bench; (3) cross-recurrence KV sharing raises Huginn to **4.81×**. |
| **Link** | [arXiv:2609.23033](https://arxiv.org/abs/2609.23033) |

### 4.4 LoopCD: Loop-wise Contrastive Decoding for Improving Reasoning in Looped Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Byeongho Yu, Junhyuk So, Eunhyeok Park |
| **Institution** | POSTECH (inferred; Eunhyeok Park) |
| **Published** | Announced 22 Sep 2026 (cs.CL) |
| **Abstract** | LoopLMs perform "latent reasoning" by recursively refining internal latents with shared weights — but suffer **loop instability**: unstable refinement across iterations produces localized uncertain "hard" tokens associated with reasoning errors. **LoopCD** intervenes at inference: it contrasts **earlier-iteration logits against last-refined-iteration logits** to build the final sampling distribution, refining reasoning-critical hard tokens without training. |
| **Key Innovations** | (1) Exploits the loop itself (inter-iteration logit contrast) as the reasoning-fix signal — no training, negligible overhead; (2) effective across recent representative LoopLMs on reasoning tasks; (3) complements 4.3's decode-speed work: this improves *accuracy*, WaveFront improves *speed*, both looped-LM-native. |
| **Link** | [arXiv:2609.24196](https://arxiv.org/abs/2609.24196) |

### 4.5 NSP: Accelerating Variable-Length LLM Training via Nested Sequence Parallelism

| Field | Detail |
|-------|--------|
| **Authors** | Yi'ou Wang, Xiaoyang Li, Yijie Zheng, Shouda Liu, Yuxuan Wang |
| **Institution** | (academic/industrial, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.DC) |
| **Abstract** | Long-context training on **long-tailed corpora** faces a communication–balance tradeoff: a fixed sequence-parallelism (SP) degree fits neither few long sequences (imbalanced) nor the many short sequences that dominate (excess communication). Dynamic-SP systems partition GPUs into disjoint groups, reintroducing cross-group imbalance. **NSP** resolves the tradeoff by **nesting differently sized SP groups on shared GPUs within one training iteration** — long sequences use larger SP groups, short sequences smaller ones; communication only where needed and load balanced per GPU. Realized with a tree-structured routing planner (memory-constrained assignment) and an executor exploiting the hierarchy via inter-level phase streaming + tree-level recomputation. |
| **Key Innovations** | (1) Nested (non-disjoint) SP groups solve the long-tail balance/communication coupling that disjoint-group dynamic SP cannot; (2) tree-scheduler + executor without model changes, supports common SP backends; (3) on Qwen3-MoE up to **384K-token contexts** over multiple long-tail datasets on a production cluster — consistent end-to-end throughput gains. |
| **Link** | [arXiv:2609.22755](https://arxiv.org/abs/2609.22755) |

---

## 5. Agents, Multi-Agent & Agentic Systems

### 5.1 Self-Organizing Agent Teams Learn to Reason Together

| Field | Detail |
|-------|--------|
| **Authors** | Aneesh Pappu, Mirac Suzgun, Yongchan Kwon, Federico Bianchi, Batu El, Mykel J. Kochenderfer, Hancheng Cao, James Zou |
| **Institution** | Stanford (inferred; Suzgun / Zou / Kochenderfer) + HKUST-GZ |
| **Published** | Announced 22 Sep 2026 (cs.AI, cs.MA) |
| **Abstract** | When a solution's structure is unknown, useful roles/division-of-labor cannot be specified in advance — teams must learn how to organize reasoning as it unfolds. **Self-Organizing Agent Teams (SAT)** are fixed teams of agents that **learn reusable teamwork strategies from prior collaborations**: roles, conversational phases, participation, information flow — enabling "collaborative computation" where agents exchange, challenge, repair, and synthesize partial reasoning holding in both independent settings, transferring unchanged to unseen benchmarks from only **15 math + 25 grad-level problems** of training collaboration. |
| **Key Innovations** | (1) Learning the *organization of reasoning* (not just the answer) from a tiny amount of shared experience; (2) strong transfer results: **66.7% avg accuracy vs 48.8% strongest member, 58.7% compute-matched inference, and 59.0% for a *perfect router***; +13.4 pts over the router on AIME 2026; (3) explains *when* collaboration helps via **demonstrability** (organization-psychology construct) across 8 benchmarks — a principled boundary on multi-agent benefit. |
| **Link** | [arXiv:2609.22682](https://arxiv.org/abs/2609.22682) |

### 5.2 AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows

| Field | Detail |
|-------|--------|
| **Authors** | Rudrendu Kumar Paul, Sourav Nandy |
| **Institution** | (industrial, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.AI, cs.CL, cs.LG, cs.MA) |
| **Abstract** | Enterprise agentic systems routing every step to a frontier model waste **60–80% of inference budget** on subtasks small models handle equally well — and existing routers optimize single-turn assignment, ignoring that complexity varies *within* a trajectory. **AgentRouter** formalizes **step-level model routing as a sequential assignment problem** over trajectories: a lightweight classifier (12M params, <5ms/step on A100) maps each step to one of four model tiers using five routing-time features, trained on 50k annotated steps across planning/coding/research/data analysis. |
| **Key Innovations** | (1) Step-level, trajectory-aware routing (vs RouteLLM/FrugalGPT single-turn signals, which only reach 31%/44% cost reduction); (2) **72% cost reduction at 97.3% frontier-only quality** (<3% end-task degradation); (3) per-step tier accuracy 76–91% — a directly deployable recipe for cost-optimal agent serving. |
| **Link** | [arXiv:2609.22951](https://arxiv.org/abs/2609.22951) |

### 5.3 Data Agents: Agentic Data Systems

| Field | Detail |
|-------|--------|
| **Authors** | Guoliang Li, Peiyao Zhou, Xuanhe Zhou, Ji Sun, Yuyu Luo, Ju Fan |
| **Institution** | Tsinghua University + academia (inferred; Guoliang Li) |
| **Published** | Announced 22 Sep 2026 (cs.DB, cs.AI, cs.CL, cs.LG) |
| **Abstract** | Traditional data systems need human-crafted pipelines, lack semantic understanding of heterogeneous data, and react rigidly. **Data Agent** is an umbrella paradigm: systems that manage/process/analyze data with minimal human intervention — shifting from manual design → autonomous orchestration, literal manipulation → semantic interpretation, reactive → proactive processing. Six components: semantic data organization, semantic operators, agentic pipeline orchestration & optimization, feedback-driven refinement, memory management, proactive adaptation; instantiated as **data analytics agent** and **data science agent**. |
| **Key Innovations** | (1) A systematic paradigm + architecture for agent-ified data (semantic-first, feedback-loop, memory) rather than a single tool; (2) two concrete specializations (analytics, data science); (3) significant benchmark gains over SOTA — plus an explicit open-challenge list for fully autonomous data systems. |
| **Link** | [arXiv:2609.24137](https://arxiv.org/abs/2609.24137) |

### 5.4 LazyAgent: Demand-Driven Materialization and Physical Optimization of Agentic Programs

| Field | Detail |
|-------|--------|
| **Authors** | Xin Heng |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.AI) |
| **Abstract** | Agent runtimes that plan-then-act generally execute each step once ready. **LazyAgent** reframes agent programs as **goal-derived demanded sets**: it refreshes a backward closure from requested outputs as execution state changes and materializes a ready node only when the active goal requires it — one linear-time graph analysis + constant-time membership tests replacing repeated local judgments, so programs stay broad while execution stays request-specific. |
| **Key Innovations** | (1) Goal-relative *demand materialization* (permission before execution) as a runtime primitive; (2) concrete economics: one unrelated product raises the eager bill 22.5% and LazyAgent's **0.0%**; **42.0% CPU saved on production scientific workflows, 51.7% container time on a live release gate (4 repos)**; goal-relative output projection saves ~90% of a shared step on 3rd-party suites; (3) proves exact equivalence when the request reaches the whole graph — no downside at full coverage. |
| **Link** | [arXiv:2609.23058](https://arxiv.org/abs/2609.23058) |

### 5.5 Total Cost of Agency: Exact Attribution of Memory Injection Cost in Multi-Agent LLM Workflows

| Field | Detail |
|-------|--------|
| **Authors** | Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.AI, cs.MA, cs.PF) |
| **Abstract** | Every node in a multi-agent LLM workflow injects retrieved context into its prompt, billed as input tokens — but observability tools report total token cost only, hiding this component. **Total Cost of Agency (TCA)** decomposes workflow cost into base prompt / inference / **memory injection** / miss penalty / context accumulation, with an exact two-pass, non-billable attribution that measures injected tokens directly (not word-count proxies). On a 200-task enterprise benchmark against real model APIs: memory injection is **13.6% of the variable cost** and ~12% of full billed cost, rising to **27.6% at workflow depth six**; injected tokens grow linearly (R²=0.9974, no convex growth). |
| **Key Innovations** | (1) The first exact attribution of the hidden "memory injection" bill in multi-agent workflows; (2) direct measurements (retrieval-window 32→2 entries cuts injected tokens 28.7% at almost no accuracy cost); (3) a controllable, model-tier-fixed cost lever — an "agent COGS observability" primitive for production workflows. |
| **Link** | [arXiv:2609.23790](https://arxiv.org/abs/2609.23790) |

---

## 6. World Models, Games & Embodied AI

### 6.1 CausalWM: Causal Chain-of-Thought Reasoning for Embodied World Model

| Field | Detail |
|-------|--------|
| **Authors** | Ziming Xu, Shuang Liang, Ruobing Han, Ziqiao Xi, Mingxing Rao, Kun Zhou, Zijun Zhang, Yuchen Yan, Yufan Wei, Junbo Huang, Yifei Shao, Fang Nan, Biwei Huang |
| **Institution** | (academic, inferred; Biwei Huang line) |
| **Published** | Announced 22 Sep 2026 (cs.CV) |
| **Abstract** | Embodied world models predict future dynamics from visual observations + control signals, with physical knowledge implicitly entangled in latents. **CausalWM** is a **16B embodied world model** performing **explicit causal chain-of-thought before future video prediction**: useful variables are organized into a reasoning trajectory progressively capturing causal dependencies. Trained on **31K hours of embodied data** in three stages (large-scale video pretraining → causal-CoT mid-training → multi-objective RL post-training). Despite limited supervised CoT variables, it shows **emergent in-context learning** — contextual visual feature guidance and efficient few-step generation. |
| **Key Innovations** | (1) Explicit causal-CoT in a world model (reason-before-predict), a distinctive departure from implicit latent-physics WMs; (2) the 3-stage recipe (video PT → causal CoT → RL) as a scalable pipeline; (3) SOTA across language/action/single-view/multi-view benchmarks including **Top-1 on the TriWorldBench leaderboard**. |
| **Link** | [arXiv:2609.23184](https://arxiv.org/abs/2609.23184) |

### 6.2 The Right Future for Action: Learning Action-Relevant Predictive States in World Action Models

| Field | Detail |
|-------|--------|
| **Authors** | Qiwen Gu, Jifan Li, Bingjie Gao, Rui Chen, Jing Tang, Xiangxiang Chu, Junqiao Zhao |
| **Institution** | Tongji Univ + industrial (inferred; Xiangxiang Chu) |
| **Published** | Announced 22 Sep 2026 (cs.CV) |
| **Abstract** | Generation-free **world action models (WAMs)** retain future-video prediction only during training and act from internal video features at inference — but what those features should preserve for control is unclear. Diagnostic finding: representations with more predictable future changes do **not** make linear action decoding easier, and linearly readable action information is spatially concentrated. This motivates **Action-Relevant Predictive States (ARPS)**: a horizon-conditioned state predictor aggregates intermediate video features into a compact state supplying all visual context to the action expert; future-representation supervision trains different state parts to predict different future times + their present-relative changes, and is removed at inference. |
| **Key Innovations** | (1) Answers *why* future supervision helps control (action-relevant, spatially concentrated, beyond present) instead of assuming it; (2) a compact predictive interface replacing the video→action coupling in WAMs; (3) **99.2% success on LIBERO with transfer to LIBERO-Plus (87.3%, +39.2 pts over Fast-WAM) without adaptation** — future-supervision → generalization under distribution shift. |
| **Link** | [arXiv:2609.23369](https://arxiv.org/abs/2609.23369) |

### 6.3 FireWorldBench: Benchmarking Complex Physical World Intelligence through Coupled-Field Fire Dynamics

| Field | Detail |
|-------|--------|
| **Authors** | Qiang Chen, Hao Guo, Huatai Zhu, Tairan Huang, Yichao Cao, Hongyan Xu, Keke Huang, Haifeng Li, Yi Chen, Xiu Su |
| **Institution** | (industrial/academic, inferred; tentative) |
| **Published** | Announced 22 Sep 2026 (cs.AI) |
| **Abstract** | Physical-world intelligence is more than recognition/description/short-term prediction: real systems have multiple continuous fields, latent causal mechanisms, partial observations, and intervention-sensitive dynamics. **FireWorldBench** uses **coupled-field fire dynamics** as a canonical stress test (multiple interacting physical fields jointly shape observable states). Two axes (physical capability × fire scenario) cover state understanding, temporal dynamics, causal mechanisms, intervention reasoning — **520 fire-world entries (494 simulated + 26 real-aligned event groups), 47 scene archetypes, 7 environment families, 9,074 text-image interleaved QA pairs** in choice + open-ended report formats. |
| **Key Innovations** | (1) A purpose-built physical-intelligence benchmark centered on coupled-field dynamics (fires = controllable, fast, multimodal); (2) evaluates causal/intervention inference, not just prediction; (3) text-image interleaving at scale — a measurement tool for the WM/embodied line that pairs with CausalWM/ARPS above. |
| **Link** | [arXiv:2609.23064](https://arxiv.org/abs/2609.23064) |

### 6.4 Enforcing Narrative Reliability and Epistemic Pacing in LLM-Driven Detective Games via Structured Knowledge Trees

| Field | Detail |
|-------|--------|
| **Authors** | Parsa Rahmati, Richard Zhao |
| **Institution** | University of Calgary (inferred; Richard Zhao) |
| **Published** | Announced 22 Sep 2026 (cs.AI, cs.CL) |
| **Abstract** | LLMs enable open-ended game dialogue but break authorial control, factual consistency, and the intended information-disclosure sequence. For detective games this is fatal: premature reveals or fabrication break player progression. A **Structured Knowledge Tree** architecture + **tri-agent LLM pipeline** (knowledge retrieval / dialogue generation / response verification) ensures the virtual suspect only reveals information permitted by the current narrative state; evaluated in *The Interrogation of Adrian Gale* playable testbed with a formal user study. |
| **Key Innovations** | (1) Separation of retrieval/generation/verification as the mechanism for narrative-constrained dialogue; (2) **−64.78% critical hallucinations and 0% premature narrative disclosure**; (3) honest about the tradeoff — mechanical constraints introduce forced-reveal usability friction, but epistemic pacing and subjective progression improve. |
| **Link** | [arXiv:2609.23043](https://arxiv.org/abs/2609.23043) |

---

## 7. Evaluation, Auditing & Evidence Discipline

### 7.1 LLJ Cards: Best practices for the Use of LLMs as Judges

| Field | Detail |
|-------|--------|
| **Authors** | Khaoula Chehbouni, Melina Medjdoub, Florian Carichon, Golnoosh Farnadi, Jackie Chi Kit Cheung |
| **Institution** | McGill / Mila (inferred; Cheung / Farnadi) |
| **Published** | Announced 22 Sep 2026 (cs.CL) |
| **Abstract** | LLMs-as-judges (LLJs) are widely adopted but raise validity/reliability concerns; existing fixes (bias mitigation, prompting) are mostly technical and leave a deeper problem: **no standardized, transparent, reproducible evaluation practice**. **LLJ Cards** synthesizes measurement theory + NLG + ML best practices into practical guidance for LLJ-based evaluation — a structured framework for applying validity/reliability/reproducibility principles in the design and reporting of automated evaluations. |
| **Key Innovations** | (1) A framework (cards) rather than another bias patch — standardizes *how LLJ evals are constructed and reported*; (2) grounds LLJ practice in rigorous measurement theory; (3) pairs with this window's empirical judge papers (7.2–7.3): the empirical failures motivate exactly this kind of reporting discipline. |
| **Link** | [arXiv:2609.24516](https://arxiv.org/abs/2609.24516) |

### 7.2 Judging a Review by its Cover: A Reliability Analysis of LLM-based Peer Review Evaluation Metrics

| Field | Detail |
|-------|--------|
| **Authors** | Shakiba Amirshahi, Sajad Ebrahimi, Hai Son Le, Negar Arabzadeh, Ebrahim Bagheri |
| **Institution** | Toronto Metropolitan Univ (inferred; Ebrahim Bagheri) |
| **Published** | Announced 22 Sep 2026 (cs.CL) |
| **Abstract** | If a review scores high for being fluent rather than substantive, LLM-as-judge review metrics may measure form, not content — especially as AI-assisted reviewers polish wording. Uses **meaning-preserving LLM rewrites** (4,044 from 674 human ICLR/NeurIPS reviews) to test whether 29 content-oriented peer-review metrics capture substance beyond surface form, via surface-sensitivity + robustness tests. |
| **Key Innovations** | (1) A statistical framework isolating substantive quality from linguistic form for review metrics; (2) damning result: **23/29 metrics assign significantly different scores to content-preserving rewrites; only 6 meet the robustness criterion**, consistent across two judge models; (3) concrete warning that LLM review metrics are confounded by surface fluency — directly relevant to automated peer review workflows. |
| **Link** | [arXiv:2609.23264](https://arxiv.org/abs/2609.23264) |

### 7.3 Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus

| Field | Detail |
|-------|--------|
| **Authors** | Elias Hossain, Niloofar Yousefi, Ser-Nam Lim |
| **Institution** | UCF (inferred; Ser-Nam Lim) |
| **Published** | Announced 22 Sep 2026 (cs.AI) |
| **Abstract** | Consensus among LLM judges is taken as strong evidence of correctness, but that assumes independent errors. In practice judges are trained/evaluated similarly and share mistakes. The study measures this error dependency: in a bank of ten judges, average pairwise error correlation is **0.21**, so ten judges carry ~**3.5 independent judges'** worth of information; dependency is stronger among high-accuracy frontier judges, even across providers; and in **up to 28% of comparisons**, ignoring shared errors flips a "significantly better" conclusion. |
| **Key Innovations** | (1) Quantifies the "fake independence" of judge panels (effective N = 3.5 of 10); (2) shows *how* errors cluster matters — shared-by-most vs concentrated errors favor different voting methods; (3) actionable fix: use a small trusted-example set to estimate judge accuracy + shared failures, and choose voting on trusted examples before deployment. |
| **Link** | [arXiv:2609.22512](https://arxiv.org/abs/2609.22512) |

### 7.4 From Concept Alignment to Causal Grounding: An Intervention Test of Chain-of-Thought Faithfulness

| Field | Detail |
|-------|--------|
| **Authors** | Qianli Wang, Yilong Wang, Dennis Wei, Jingyi Sun, Simon Ostermann, Pepa Atanasova, Nils Feldhus |
| **Institution** | IBM Research + DFKI (inferred; Dennis Wei / Nils Feldhus) |
| **Published** | Announced 22 Sep 2026 (cs.CL, cs.AI, cs.LG) |
| **Abstract** | CoT can be plausible yet unfaithful; prior probes rely on input/output behavior or attributions. This work casts faithfulness as **internal concept grounding**: encode a prediction pass and a CoT pass with one shared **sparse autoencoder (SAE)** so their internal concepts are directly comparable; three correlational alignment metrics + a causal metric **Δp** (ablate shared concepts, measure answer-probability drop). |
| **Key Innovations** | (1) First SAE-based *causal* intervention test for CoT faithfulness (Δp), complementing correlational alignment; (2) key dissociation: high concept alignment does not imply causal contribution — causal faithfulness peaks at **mid-to-late layers**, and causally important shared concepts are **often not verbalized** in the CoT; (3) a strong argument that faithfulness must be assessed causally, not from surface/representational correspondence. |
| **Link** | [arXiv:2609.23065](https://arxiv.org/abs/2609.23065) |

### 7.5 On the Efficiency-Safety Dilemma in Large Reasoning Models

| Field | Detail |
|-------|--------|
| **Authors** | Yifei Yang, Zouying Cao, Xingrui Wang, Xiao Zhou, Yuexian Li, Dongjie Yang, Hai Zhao |
| **Institution** | Shanghai Jiao Tong University (inferred; Hai Zhao) |
| **Published** | Announced 22 Sep 2026 (cs.CL, cs.AI) |
| **Abstract** | Efficiency techniques (quantization, pruning) reduce LRM inference cost, but their effect on adversarial robustness is unexplored. First comprehensive analysis of the **efficiency–jailbreak–reasoning** interplay: efficiency methods *appear* to lower jailbreak success, but the improvement is often **superficial** — caused by degraded reasoning ("attempted but failed" malicious responses), not genuine alignment. Mechanistic analysis ties reasoning-capability loss to the inability to maintain malicious semantic trajectories. Quantization+pruning is identified as the best efficiency-robustness balance. |
| **Key Innovations** | (1) Distinguishes **true alignment from capability-induced failure** — the key confound in LRM safety eval under efficiency constraints; (2) mechanistic representational-drift evidence for the coupling; (3) actionable deployment guidance (quantize+prune combos) for balancing cost and safety. |
| **Link** | [arXiv:2609.23587](https://arxiv.org/abs/2609.23587) |

### 7.6 Auditing Source Exposure in Baidu and Google AI Search

| Field | Detail |
|-------|--------|
| **Authors** | Yibo Li, Enci Guan, Yuedan Cai, Geng Liu, Francesco Pierri |
| **Institution** | Baidu + Politecnico di Milano (inferred; Francesco Pierri) |
| **Published** | Announced 22 Sep 2026 (cs.IR) |
| **Abstract** | AI-generated overviews are increasingly prominent but **Chinese-language** behavior is underexplored. Cross-lingual audit of Baidu and Google AI overviews on MS MARCO English queries + translated Chinese counterparts: when overviews trigger per platform-language setting, which host domains get visible exposure in Chinese, how concentrated it is, and how source overlap varies. Answer-level semantic similarity for matched intents yields median cosine similarities **0.701–0.813**, while aggregate level shows **low overlap in visible host-domain inventories** across settings. |
| **Key Innovations** | (1) First cross-lingual audit of AI-overview source exposure (CN + EN), unlike prior EN-only audits; (2) separates answer-level semantic similarity from source-visibility distribution — two distinct dimensions of AI-mediated search; (3) policy-relevant: eval of AI search should cover *where source visibility lands*, not just answer quality, across platforms/languages/environments. |
| **Link** | [arXiv:2609.24407](https://arxiv.org/abs/2609.24407) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **First-party industrial rec cluster is the window's flagship — Baidu depth returns** | UNIQUE (unified flat-quantized retrieval+ranking, +0.96% watch duration/+1.08% distribution online at Mobile Baidu), MuSeR (long-seq multi-interest on deployed MGS, +0.26% DAU/+0.89% session, p<0.05) — same author cluster, both system-level and deploying to three Baidu feed surfaces |
| **E-commerce/search retrieval goes graded + explainable + supervised** | GradCIR (4-level graded CIR at Walmart, +4.9–5.9% NDCG@10, live), YouTube Music (offline-deferred LLM rationales cut the trust barrier, significant exploration+engagement A/B), Netflix counterfactual observability framework — explainability/observability as first-class, production-audited |
| **Generative rec touches its measurement limits** | Semantic-ID reproducibility study (2609.24430): no universally best SID, codebook utilization diagnostic-but-insufficient, scaling not always beneficial — the strongest caution yet for the generative-rec line the wiki tracks |
| **Sparse/distilled supervision matures: token-level, reliability-aware** | IER-OPD (gradient-estimation reliability, 0.1–1% token budgets), TrustMOPD (token-level label-free multi-teacher allocation, 54→91–98% recovery), RLVR² (ordinal rubric ranking replacing score scaling), FLARE (generative RM dense supervision; N=1 beats N=5 rollout at 5× fewer tokens) |
| **Practical knowledge maintenance: cheap and safe** | Time-Incremental CPT (post-cutoff FineWeb-Edu: curated 6B ≈ 40B, no forgetting, macro-avg within 0.01, LoRA parity), Full-Pipeline FP8 RL (Calibrated Clipping fixes importance-ratio distortion, BF16-comparable) |
| **Looped LMs become a two-front research target** | WaveFront Decoding (3.54–4.81× decode, draft/verify co-batched) + LoopCD (inter-iteration logit contrast improves reasoning) — both training-free, loop-native |
| **Agent economics climb the agenda: routing, laziness, injection-cost attribution** | AgentRouter (72% cost cut at 97.3% quality, step-level tiers), LazyAgent (demand-driven materialization; 0.0% vs 22.5% on unrelated work, 42% CPU saved), Total Cost of Agency (exact memory-injection attribution, 13.6–27.6% of variable cost by depth) |
| **Multi-agent value gets falsifiable boundaries** | Self-Organizing Agent Teams (66.7% vs 59.0% perfect router; beat router by 13.4 pts on AIME 2026; success tied to demonstrability) |
| **LLM-judge / review-eval reliability is now an empirical subfield** | LLJ Cards (practice framework), Judging a Review by its Cover (23/29 review metrics fail content-preservation robustness), Agreement Overstates Evidence (10 judges ≈ 3.5 independent; 28% flips), CoT faithfulness via SAE causal intervention (Δp) |
| **AI-search accountability pivots to source visibility** | Auditing Source Exposure in Baidu/Google AI Search (CN+EN; low host-domain overlap, cos-sim 0.70–0.81), Brand-Vis (runner-up; own-domain exposure drives 2.8→91.4% GPT mention rates) — ad-adjacent accountability ahead of the classic CTR line |

(Runner-ups worth a look, grep-verified unclaimed: **2609.23111** Inherit4Rec (Dense-to-Dense growth & Dense-to-Sparse SMoE conversion with co-activation-aware partitioning, KuaiRand + industrial); **2609.23646** Beyond Relevance (structured semantic supervision w/ LLM-augmented annotations for product search, nDCG@10 0.9258 human-free); **2609.23849** BT-SR (Barlow-Twins decorrelation as a popularity-concentration control knob in sequential rec); **2609.23162** Brand-Vis (fitted stage model of brand visibility in GPT/Gemini AI search: own-domain exposure lifts mention rates 2.8%→91.4% GPT / 3.8%→100% Gemini); **2609.23449** PSD (pseudo self-distillation of agent memory; SLMs match GPT-4.1-mini on LoCoMo at fraction of cost); **2609.23466** RPMem (recurrent parametric cross-session agent memory mapped to LoRA, 85.52% PERMA w/ Qwen3-8B); **2609.23130** From Inference Engine to Inference Control Plane (vLLM + llm-d synthesis: state/placement/network move up the scarce-resource ladder); **2609.23085** Measured Joules, Learned Routes (learned accuracy-energy routing across LLM pools, sharp phase transition); **2609.22818** The Price of Safety (benign-case cost of agent memory-poisoning defenses: reranker -4.4 pts accuracy, 33.6% false quarantines); **2609.24122** Re:CAP (reference-free RAG retrieval-coverage audit probe loop, recovers 9–29% of gold labels beyond BM25 top-500); **2609.23201** Do Not Trust the Benchmark (perspective on general LLM ranking limits + task-specific evaluation argument); **2609.23585** Global Ranks Survive, Selected Heads Shift (BOS-sink topology under 4-bit weight-only PTQ — global ranks ρ≥0.980 but top-k Jaccard only 0.62–0.79).)

(End of file — total 38 featured / 7 sections / 12 runner-ups)