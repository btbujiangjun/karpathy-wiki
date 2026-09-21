---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Sequential Modeling / Games"
type: synthesis
created: 2026-09-21
updated: 2026-09-21
sources: [arxiv.org]
tags: [arxiv-daily, AI, LLM, advertising, auto-bidding, oCPX, recommendation, personalized-search, video-retrieval, sequential-recommendation, SSM, recurrent-transformer, world-models, games, computer-use, long-context, KV-cache, sparse-attention, speculative-decoding, post-training, GRPO, distillation, formal-verification, agents, multi-agent, agent-RL, deferral, routing, LLM-as-judge, memborship-detection, retrieval-confidence, daily-digest]
---

# arXiv Daily Report — 2026-09-21

> **Mailing status**: Fresh **Monday, 21 September 2026** mailing (weekend-processed submissions) — the first new window since the Fri-18 batch. In-window IDs for the parsed categories span **2609.20823–2609.22064**.
> **Methodology**: Parsed `/list/{cat}/new` for **cs.LG / cs.AI / cs.CL / cs.CV / cs.IR / cs.CY / cs.DC / cs.GT / cs.MA / cs.NE / cs.SI** (305 listing entries in window; full abstracts are embedded in the listing pages). Screened every title in-window, deepened ~40 shortlisted abstracts, and featured **35 papers + 12 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/`** at write time. Probe HTML was cached under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and cleaned up after. Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).
> **CTR/ads note**: The direct end-to-end CTR/pCVR-model drought continues (≈8 consecutive windows with ~0 classic CTR-ML papers at the daily layer). But the **auto-bidding / oCPX line returns in force** this window: **OneBid** (a unified oCPX auto-bidding foundation model, deployed at Kuaishou with online A/B) and **ADAPT** (disentangled advertiser profiles with train-free adaptation). Recommendation/search also contributes two production-scale systems papers (trillion-doc hybrid GPU-CPU retrieval; EvoPilot long-horizon online autoresearch for video discovery), which is rare first-party infrastructure depth for a daily window.

---

## 1. Advertising, Auto-Bidding & oCPX

### 1.1 OneBid: A Unified Auto-Bidding Foundation Model for Diverse oCPX Advertising Scenarios

| Field | Detail |
|-------|--------|
| **Authors** | Yewen Li, Peng Jiang, Yitian Li, Pengfei Lv, Xialong Liu, Peng Jiang, Qingpeng Cai |
| **Institution** | Kuaishou (inferred; Peng Jiang / Qingpeng Cai) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Auto-bidding has evolved from rule-based controllers to RL and generative methods (Decision Transformer), but these increasingly mismatch the dominant oCPX paradigm: heterogeneous scenarios (registration, purchase, ROAS…) are each served by a separate model, fragmenting pipelines and under-using cross-scenario data. **OneBid** unifies them into a single foundation model: (1) a reusable backbone pretrained on heterogeneous oCPX logs, adapting per scenario via offline post-training; (2) extends DT's single Return-to-Go conditioning to **two atomic signals — Return-to-Go (conversion value) + Cost-to-Go (cost ratio)** with value-aware regularization; (3) a **sequence-level MoE** where shared experts encode cross-scenario knowledge and sparsely-routed experts capture scenario patterns at low latency (capacity scales with size/data). Post-training uses **CROP** (Critic-guided Relative Offline Policy Optimization): a critic scores candidate actions group-relatively, avoiding unsafe online exploration of GRPO-style fine-tuning while constraining policy shift. |
| **Key Innovations** | (1) First foundation-model-style unification of heterogeneous oCPX scenarios in one backbone (cross-scenario transfer + consistent scaling); (2) dual Return-to-Go/Cost-to-Go conditioning as the two atomic control signals; (3) offline, critic-guided relative policy optimization (CROP) as the safe post-training primitive — validated **fully deployed at Kuaishou: overall +2.2% ADVV on oCPX Ads, peaking +13.1% on the ROAS scenario**. |
| **Link** | [arXiv:2609.21550](https://arxiv.org/abs/2609.21550) |

### 1.2 ADAPT: Auto-Bidding with Disentangled Advertiser Profiles and Train-Free Adaptation

| Field | Detail |
|-------|--------|
| **Authors** | Songyue Cai, Shan Gu, Wei Chen, Ziru Xu, Lianyu Wang, Jian Xu, Xiaofeng Zhu |
| **Institution** | Alibaba-affiliated (inferred; Jian Xu) |
| **Published** | Announced 21 Sep 2026 (cs.IR) |
| **Abstract** | Profile-based personalization works in recommendation but has struggled in auto-bidding because extracting *pure* advertiser profiles is hard, modeling common + private information simultaneously is hard, and profiles need updating/cold-start adaptation. **ADAPT** (Auto-bidding with Disentangled Advertiser Profiles and Training-free adaptation) uses a two-stage paradigm: stage 1 extracts pure **static + dynamic** profiles via contrastive learning over an advertiser memory bank; stage 2 disentangles the dynamic profile into a **common + private** profile and conditions the bidding strategy on all three; once trained, ADAPT constructs profiles for *new* advertisers and updates existing ones **without retraining**. |
| **Key Innovations** | (1) Explicit separation of static/common/private advertiser signals as bidding conditions; (2) contrastive memory-bank extraction of pure profiles (no interaction-feedback contamination); (3) train-free profile update + cold-start handling — deployment-relevant for ads systems where retraining per advertiser is prohibitively costly. |
| **Link** | [arXiv:2609.21308](https://arxiv.org/abs/2609.21308) |

---

## 2. Recommendation, Personalized Search & E-commerce

### 2.1 Hybrid GPU-CPU Retrieval for Personalized Search at Ultra-Large Scale

| Field | Detail |
|-------|--------|
| **Authors** | Hao Fu, Jichao Sun, Baiting Zhu, Qiaoling Liu, Yan Shi, Cheng Lu, Liu Liu, Yubo Wang, Xin Yao, Xiangyu Niu, Xu Dong, Wenhan Lyu, Chiyao Shen, Yinjie Huang, Minglei Chen, Shuai Ding, Li Fan, Xiao Kong |
| **Institution** | (inferred industrial — trillion-doc UGC search) |
| **Published** | Announced 21 Sep 2026 (cs.IR) |
| **Abstract** | Hosting the full serving inventory of a trillion-document UGC search in GPU memory is infeasible, while CPU compute cannot run an interaction-heavy model on the latency-critical path — the **personalization-scale paradox**. The authors resolve it via orchestration, not a new model class: a **high-depth GPU pathway** fuses retrieval + interaction pre-ranking over a curated ~1B-doc online pool, while a **high-breadth CPU pathway** searches an independently selected inventory ~20× larger with lightweight personalized scoring; either/both run per request and candidates are deduplicated before downstream ranking. |
| **Key Innovations** | (1) A clean depth-on-GPU / breadth-on-CPU split of the serving path (independently evolvable, matched-capacity economic analysis); (2) evidence that the two pathways contribute *structurally distinct* candidates rather than overlapping sets; (3) full production deployment with an A/B vs the legacy CPU-only config improving model-scored relevance and substantive engagement. |
| **Link** | [arXiv:2609.21281](https://arxiv.org/abs/2609.21281) |

### 2.2 Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval at Scale

| Field | Detail |
|-------|--------|
| **Authors** | Hao Fu, Baiting Zhu, Minglei Chen, Yinjie Huang, Shuai Ding |
| **Institution** | (inferred industrial; same author cluster as 2.1) |
| **Published** | Announced 21 Sep 2026 (cs.IR) |
| **Abstract** | LLM agents can run "minutes-scale autoresearch" on self-contained programs, but **online autoresearch** — asynchronous systems, hours-long variants, weeks-long campaigns — is fragile: a run can support an invalid conclusion when a code change is a no-op, data windows leak, evaluators drift, or arms traverse different funnels. **EvoPilot** is a human-gated method for long-horizon online autoresearch: role-specific agents execute each round through a versioned domain skill + typed adapter, with durable records and deterministic checks enforcing recorded lessons. A **37-day campaign** on Video Deep Dive (VDD) retrieval (hourly refreshed index of hundreds of millions of videos): EvoPilot's human-gated verification traced a false 22-pp offline hit-rate decline to a pre-existing evaluation defect (output depths 3,000 vs 600), then measured a true +3.20 pp offline improvement; a 7-day randomized online test estimated +0.66% relative Good Search Result Rate for Retention on the VDD slice. |
| **Key Innovations** | (1) Walks the arc from naive autoresearch → false conclusion → human-gated EvoPilot → corrected, verified result (a concrete cautionary tale); (2) durable-state recovery + artifact reuse (≈5 GPU-hours saved) as systems primitives; (3) post-study replay/mutation tests that reject invalid comparisons while admitting valid ones — evaluation-gating as a first-class component of agentic model development. |
| **Link** | [arXiv:2609.21257](https://arxiv.org/abs/2609.21257) |

### 2.3 DSRec: Dual-Interest Sequential Product Recommendation With Multi-Granular SSM

| Field | Detail |
|-------|--------|
| **Authors** | Shuiying Liao, P. Y. Mok |
| **Institution** | Hong Kong Polytechnic University (inferred; P. Y. Mok) |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | Sequential recommenders struggle with *item polysemy* — the same item plays different semantic roles depending on user context — and with cost efficiency. **DSRec** encodes sequence items into two interest branches: **long-term** embeddings capturing stable preferences via historical aggregation, and **short-term** embeddings emphasizing local session intent modulated by **inter-click time intervals**. Each branch gets its own SSM encoder: a full-sequence **Mamba** for long-range modeling and a **time-modulated SSM** that dynamically adjusts state evolution from temporal gaps, joined by a residual cross-fusion that exchanges context while preserving semantic independence. |
| **Key Innovations** | (1) Explicit long/short-term dual-branch decomposition of item roles (polysemy as a modeling target, not a nuisance); (2) time-gap-conditioned SSM state transitions — temporal gating native to the recurrent path; (3) residual cross-fusion for granularity alignment without branch entanglement; outperforms SOTA on public sequential-rec benchmarks. |
| **Link** | [arXiv:2609.21548](https://arxiv.org/abs/2609.21548) |

### 2.4 APCL: Adaptive Preference Modeling via Explicit Indirect Relational Learning for Personalized Fashion Matching

| Field | Detail |
|-------|--------|
| **Authors** | Shuiying Liao, Li Li, P. Y. Mok |
| **Institution** | Hong Kong Polytechnic University (inferred; P. Y. Mok) |
| **Published** | Announced 21 Sep 2026 (cs.IR) |
| **Abstract** | Personalized fashion complementary recommendation must jointly model user preference and item compatibility under sparse, multimodal data. Existing work captures higher-order relational signals mostly *implicitly* (graph propagation) or relies on direct interactions. **APCL** models **direct and indirect** relational signals explicitly: a correlation-guided adaptive aggregation constructs indirect user-item and item-item relationships carried as dedicated personalization vs compatibility views, and a **functional-view contrastive loss** aligns direct/indirect representations of both preference and compatibility. Multimodal (visual + textual) inputs are integrated throughout. |
| **Key Innovations** | (1) Explicit (not implicit) construction of indirect relational views; (2) contrastive alignment across relational contexts — direct↔indirect preference and direct↔indirect compatibility; (3) sparse-interaction robustness via the adaptive aggregation, beating representative baselines on two fashion datasets. |
| **Link** | [arXiv:2609.21475](https://arxiv.org/abs/2609.21475) |

### 2.5 Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction

| Field | Detail |
|-------|--------|
| **Authors** | Qi Chen, Yunfei Chu, Haolin He, Yifan Yang, Zihan Liu, Yuxuan Wang, Ziyang Ma, Ruiyang Xu, Meng Gao, Yinsong Yan, Ling Wang, Hui Wang, Wen Huang, Yiheng Chen, Guanrou Yang, Qiuqiang Kong, Jin Xu, Xie Chen |
| **Institution** | (inferred industrial — MLLM assistant team) |
| **Published** | Announced 21 Sep 2026 (cs.CL) |
| **Abstract** | Assistants now interact through natural audio-visual streams, yet benchmarks judge *response quality*, not the prior step: **can the model infer the user's underlying demand from complex multimodal interaction**? Real demands are underspecified in speech, must be read from multimodal cues + dialogue history, and are complicated by ambiguous/disfluent expression and noise; conversely request-like speech can be a false trigger. Establishes **ODU** as a distinct multimodal contextual-inference problem (demand present? + intent) evaluated along five dimensions, and builds **ODU-Bench** from a challenge-driven taxonomy, taxonomy-guided agentic video generation, and human-recorded interactions with media-grounded annotation and human verification. |
| **Key Innovations** | (1) Frames "demand understanding before responding" as its own benchmarkable capability (a rec/eval-layer blind spot for multimodal assistants); (2) large gated eval: among 14 native MLLMs, even Gemini 3.1 Pro recovers only **44.7%** of the key information that must be inferred from visual/acoustic/conversational context, and **11/14 models show >50% false-trigger rates** on non-demand scenarios; (3) a reproducible construction pipeline (taxonomy → agentic video gen → human verification). |
| **Link** | [arXiv:2609.21392](https://arxiv.org/abs/2609.21392) |

### 2.6 Self-Meta-Evolve: One Prompt Does Not Fit All — Personalized Information Extraction

| Field | Detail |
|-------|--------|
| **Authors** | Hongliang Li, Lu Wang, Yong Xu, Hanyang Chen, Zhitao Hou, Xiaoting Qin, Song Ge, Qingwei Lin, Dongmei Zhang |
| **Institution** | Microsoft Research Asia (inferred; Qingwei Lin / Dongmei Zhang) |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | Enterprise information extraction is *per-user*: the same document must be reorganized differently for each worker. Global single-prompt optimization is misaligned with that heterogeneity. **Self-Meta-Evolve** maintains a dedicated prompt per user refined in a **dual loop**: an inner loop edits structured prompts from persona-conditioned feedback; an outer loop evolves a *meta-prompt* by distilling successful editing patterns. Training/eval is on a new **persona-driven IE benchmark of 292 simulated enterprise users** (O\*NET-grounded persona generation). |
| **Key Innovations** | (1) Formulates IE as per-user prompt adaptation under interaction feedback (rec-like personalization inside the prompt-engineering substrate); (2) hierarchical dual-loop evolution (per-user prompt + meta-prompt that learns how to edit); (3) strong results — **74.58% success, +13.56 pp over the best prompt-optimization baseline, 52.54% within two iterations**, and a double-blind study with 20 real professionals where adapted prompts beat static baselines in **71%** of pairwise comparisons. |
| **Link** | [arXiv:2609.21626](https://arxiv.org/abs/2609.21626) |

---

## 3. Sequential Modeling & Recurrent Architectures

### 3.1 Trading Depth for Time in Recurrent Transformers

| Field | Detail |
|-------|--------|
| **Authors** | Zeyi Huang, Xuehai He, Yong Jae Lee, Yelong Shen |
| **Institution** | Apple / UW-Madison (inferred; Yelong Shen) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Recurrent Transformers add computational depth *temporally* (recurrence), raising the question: is extra compute better spent on more temporal steps or more physical depth? Using **Latent Recurrent Transformers (LRTs)** — one backbone pass per vocabulary token, with an inserted **latent thought token** between vocab tokens — the paper compares an *L*-layer LRT (+thought token) against a *2L*-layer LRT without. Both execute 2L blocks per vocab token at decode, but the thought-token model uses fewer parameters. |
| **Key Innovations** | (1) A controlled apples-to-apples budget analysis (equal FLOPs/token, fewer params) of temporal vs physical depth; (2) on 16/20-layer MoE NanoChat backbones, one thought token recovers **67%/81%** of the double-depth improvement within 0.006/0.004 bpb at **~48% fewer parameters**; (3) empirical support for parametric "thinking time" as a cheaper substitute for stacking layers in recurrent Transformers. |
| **Link** | [arXiv:2609.21605](https://arxiv.org/abs/2609.21605) |

### 3.2 Prediction Dynamics in Depth-Recurrent Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Xinyue Luo, Fei Yu |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.CL) |
| **Abstract** | Depth-recurrent LMs refine predictions through repeated latent updates — but *why do intermediate answers agree with the endpoint while their scores keep changing*? The paper derives a **sharp margin characterization** decomposing a magnitude bound's conservatism into (i) common translation, (ii) update direction relative to the winning answer, and (iii) how each competitor's update pairs with its score gap. Across **Huginn-3.5B and Ouro-1.4B**, accounting for update direction + competitor pairing reduces the mean earliest qualifying depth by a further **22.5–34.4%** of total depth beyond simple translation removal. |
| **Key Innovations** | (1) A de-composition of depth-recurrent prediction dynamics into three interpretable components; (2) the finding that answer *agreement* is a weak early-stopping signal — direction and pairing matter; (3) concrete remaining-depth reduction numbers, useful for depth-recurrent inference/serving decisions. |
| **Link** | [arXiv:2609.21383](https://arxiv.org/abs/2609.21383) |

### 3.3 Recursive Language Models Generalize Out of Domain

| Field | Detail |
|-------|--------|
| **Authors** | Chenxiao Yang, Zhiyuan Li, David McAllester, Nathan Srebro |
| **Institution** | TTIC / University of Chicago (inferred; McAllester / Srebro) |
| **Published** | Announced 21 Sep 2026 (cs.CL) |
| **Abstract** | When does *limiting what the model can see* help? Compares standard CoT (the general learner reading the full trace) against **recursive language models**, which solve each subtask in an isolated context. In-distribution, CoT can simulate the recursive rule so recursion offers little. **Out of domain**, CoT can fit training via context *outside* the current subtask — a shortcut that breaks when tokens change — while recursive context isolation rules that failure mode out. |
| **Key Innovations** | (1) A clean theoretical separation: IID generalization is ~free for both, but OOD generalization differs because **simplicity bias picks the shortcut over the truth** for CoT; (2) reframes the classical-learning-theory contrast ("covering the right rule is not enough beyond distributional accuracy") in LM terms; (3) gives a principled argument for recursive/isolated-context architectures as OOD-hardened alternatives to full-trace CoT. |
| **Link** | [arXiv:2609.20831](https://arxiv.org/abs/2609.20831) |

---

## 4. World Models, Games & Interaction

### 4.1 World Modeling in Transformers (TaxiGPT)

| Field | Detail |
|-------|--------|
| **Authors** | Pierre Beckmann, Matthieu Queloz, Andre Freitas |
| **Institution** | University of Manchester (inferred; Andre Freitas) |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | Behavioral failures can make a transformer look like it lacks a world model even when it has faithful internal representations of its environment. In **TaxiGPT** (a transformer trained on random walks through Manhattan whose failures were read as an incoherent internal map), mechanistic analysis + causal interventions show the model **does** represent intersections and streets, tracks position, and uses a goal compass to navigate. Failures trace to **interference between superposed intersection features** disrupting localization. "Affordance packing" — grouping intersection representations with identical legal moves — limits the damage; mechanistic indicators compare models and show world-modeling capacities emerge at different training stages. |
| **Key Innovations** | (1) Reinterprets an iconic "no world model" failure story as superposition interference, not an absent map; (2) a tangible representation-engineering fix (affordance packing) that undercuts the failure; (3) shifts the field's question from *whether* a model has a world model to *how* its world modeling is structured and where it emerges in training. |
| **Link** | [arXiv:2609.21748](https://arxiv.org/abs/2609.21748) |

### 4.2 Benchmarking World Models for Continual Learning on Compositional Tasks

| Field | Detail |
|-------|--------|
| **Authors** | Haoyu Zhou, Joe Watson, Anson Lei, Ingmar Posner |
| **Institution** | University of Oxford (inferred; Ingmar Posner) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | A desirable world model learns continually — reusing acquired knowledge across new environments, since physical dynamics recur across tasks. But adaptation metrics *entangle* two abilities: speed/capacity to learn unseen tasks and reuse of prior knowledge. To **isolate knowledge reuse**, the paper builds a **compositional continual-learning benchmark for robot-manipulation world models**: each curriculum composes tasks from aspects seen earlier, factored along **action vs perception axes** to find which modality bottlenecks reuse. Evaluates SOTA world models under canonical continual-learning methods plus a **modular world model** with explicitly reusable dynamics components. |
| **Key Innovations** | (1) A benchmark purpose-built to measure reuse-without-forgetting, decoupled from raw adaptation speed; (2) action/perception factorization as a diagnostic for *what* blocks reuse; (3) finding: modularity balances reuse against forgetting better than conventional CL methods, but nobody solves it fully — an open call for continual world models. |
| **Link** | [arXiv:2609.22055](https://arxiv.org/abs/2609.22055) |

### 4.3 GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development

| Field | Detail |
|-------|--------|
| **Authors** | Xiuhui Zhang, Yi Chen, Shusheng Xu, Fan Li, Huan Wang, Tongkai Yang, Binhang Yuan |
| **Institution** | HKUST (inferred; Binhang Yuan) |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | Autonomous software generation (ASG) turning requirements into apps rarely proves the *interacting components satisfy behavioral requirements*. **GameASG-Bench** makes **behavioral testability** part of the generation task for games: an evaluation interface specification is declared before generation (legal start states, player-level actions, stable snapshots, rejection behavior, invariants) while private implementation stays open. Checks are **static L1** (source-level compliance) + **browser-executed L2** (semantic observations with real input + runtime evidence), across **47 game-generation tasks, 12 primary genres, 2D + 3D**. |
| **Key Innovations** | (1) Testability-by-construction protocol (interface spec declared pre-generation) rather than post-hoc unit tests; (2) two-level (static + execution-grounded) verification with an independently verified reference per task; (3) sharp measurement result: across nine agent stacks the best mean **L2 pass rate is 93.2%** yet the best **strict task success is only 55.3% (26/47)** — high average check pass rates obscure per-task compliance gaps. |
| **Link** | [arXiv:2609.21293](https://arxiv.org/abs/2609.21293) |

### 4.4 RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents

| Field | Detail |
|-------|--------|
| **Authors** | Shuai Bai, Jiayong Deng, …, An Yang, Dayiheng Liu, …, Bowen Zhou (34 authors) |
| **Institution** | Alibaba Qwen team (inferred; Bowen Zhou et al.) |
| **Published** | Announced 21 Sep 2026 (cs.CL) |
| **Abstract** | Computer-use agents (CUAs) have split into two lines — GUI interaction vs code/CLI development — but real digital work interleaves both. **RecreationWorld** studies **hybrid CUAs** that autonomously decide when to explore an interface, implement software, and visually verify artifacts. Given a running *reference* app, an agent must reverse-engineer its behavior and build a faithful implementation with no prescribed workflow. Five reproducible platforms (Ubuntu, macOS, Windows, Android, Web), unified harness with GUI control + coding tools, and a **reference-as-oracle** running app that grounds hidden behavioral tests. **RecreationBench**: 250 held-out tasks with programmatic + visual assertions validated on the reference and by humans before freezing. |
| **Key Innovations** | (1) The hybrid GUI+code agent task class ("recreate the running artifact") and a verifiable multi-platform benchmark for it; (2) reference-as-oracle execution-grounded rewards for trajectory scaling; (3) sobering measurement: **GPT-6 Astra leads at 58.1%** but passes all programmatic tests on only **2.8%** of tasks; agents reproduce static structure better than interaction/computed outputs — a concrete critique for agentic coding + computer-use research. |
| **Link** | [arXiv:2609.22000](https://arxiv.org/abs/2609.22000) |

### 4.5 Scaling Discovery through Test-Time Communication

| Field | Detail |
|-------|--------|
| **Authors** | Jongho Park, Vasilis Kontonis, Shivam Garg, Akshay Krishnamurthy, Dimitris Papailiopoulos |
| **Institution** | UW-Madison / MSR (inferred; Papailiopoulos / Krishnamurthy) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Do communicating agents beat parallel attempts? Mixed prior results. On **ARC-AGI-3**, a team of *k* role-free agents communicating through a shared directory matches the success rate of **4k independent agents**, and the advantage *grows* with *k* — a task no single agent can solve, a team solves reliably. Gains transfer to research tasks under sufficient compute: on polyomino packing they beat best@*k* and the prior best-known score; on MNIST classifier compression a team of four produced a **1,957-byte classifier at 99.4% accuracy** — smaller than the best-known human solution and best single agent. Caveat: communication can hurt when compute is limited or progress is hard to measure. |
| **Key Innovations** | (1) The 1:4 "communication → parallelism" scaling ratio with compounding gains at scale; (2) super-additive transfer — group success where *no* individual succeeds (shared-directory, role-free design); (3) explicit failure boundary (limited compute / absent feedback) so the recipe is not oversold. |
| **Link** | [arXiv:2609.21032](https://arxiv.org/abs/2609.21032) |

---

## 5. Long-Context, KV-Cache & Inference Efficiency

### 5.1 RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Chuxu Song, Jiuqi Wei, Zhencan Peng |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | Long-context inference is increasingly prefill-bound; sparse block selection helps but a block *centroid* can hide a highly relevant token among noise — **mean dilution**. **RBS-Attention** is a training-free sparse-prefill method with two complementary branches: a *centroid base* branch (average relevance) plus a *rescue* branch using the **maximum key-block radius** and its prompt/layer/head-dependent distribution to catch blocks risk being underestimated; the two masks are thresholded independently and merged while preserving block-sparse FlashAttention execution. |
| **Key Innovations** | (1) Identifies/named "mean dilution" and attacks it with a max-radius rescue branch (radius-adaptive dual-branch selection); (2) strong numbers on H100: **20.65× standalone prefill-attention, 11.92× vLLM prefill-attention, 5.97× end-to-end TTFT at 128K on Qwen3-30B-A3B-FP8**, with Qwen3-32B RULER at 88.65 vs 89.52 dense; (3) auxiliary measurements (retention, matched-density selectors, memory behavior) keep the comparison honest. |
| **Link** | [arXiv:2609.20971](https://arxiv.org/abs/2609.20971) |

### 5.2 Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding

| Field | Detail |
|-------|--------|
| **Authors** | Themistoklis Haris, Henry Li, Maryam Karimzadehgan |
| **Institution** | Google Research (inferred; M. Karimzadehgan) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Sparse attention loaded selectively to cut KV bandwidth usually pays with rigid heuristics that drop necessary context. **ETA** is an **end-to-end trainable** architecture that predicts *dynamic, contextual* thresholds from query representations: dense-like context for hard retrieval/reasoning steps, pruning for routine tokens. To learn without representation collapse it **multiplicatively suppresses sub-threshold logits toward zero** (a smooth uniform-attention floor) rather than deleting them — which makes localized attention sinks on initial tokens disappear. At inference a Triton kernel screens KV blocks in O(1) via cached geometric-probabilistic bounds. |
| **Key Innovations** | (1) Learned per-query thresholds (trainable sparsity) that preserve dense quality for hard steps; (2) a mechanism-level explanation (attention-sink removal via the multiplicative floor) for why it trains cleanly; (3) 1.45B model rivals dense attention at **~85% training sparsity / ~38% active decode density**, with **up to 2.5× wall-clock decode speedups over FlashAttention-2 at 512K** and a calibration path that cuts attention compute another 27%. |
| **Link** | [arXiv:2609.20888](https://arxiv.org/abs/2609.20888) |

### 5.3 TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching

| Field | Detail |
|-------|--------|
| **Authors** | Zhihao Shu, Md Musfiqur Rahman Sanim, Jie Hu, Kun Yuan, Minghai Qin, Gagan Agrawal, Wei Niu |
| **Institution** | (academic/industrial, inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | On-device LLMs face KV-cache as the dominant memory bottleneck for long contexts. Prior mitigations (low-rank compression, eviction, flash offloading) incur reconstruction overhead, irreversible token loss, or I/O stalls. **TierKV** = **Predictive Multi-Tier Cache Optimization (PMCO)**: *before* decoding, predicts future cache demand from prefill hidden states and jointly assigns tokens to **exact / low-rank / flash-offloaded tiers** under device memory + accuracy budgets — retaining access to full context, removing the circular dependency of reactive eviction, and admitting a **closed-form solver** for tier boundaries and per-layer ranks at runtime. |
| **Key Innovations** | (1) Predictive (prefill-time) tier assignment instead of reactive eviction — a class of solution the on-device literature largely lacks; (2) closed-form runtime solver for boundary + rank choices; (3) across 8 text/vision/audio models on 3 mobile SoCs: **up to 17.6× prefill throughput gain**, **12.5–34% RAM-resident KV reduction** (longer contexts under the same memory budget) with minor accuracy loss. |
| **Link** | [arXiv:2609.21172](https://arxiv.org/abs/2609.21172) |

### 5.4 SpecQuant: Speculative Decoding with Multi-Parent Quantization for Adaptive LLM Inference

| Field | Detail |
|-------|--------|
| **Authors** | Harish KB, Jagadeeswaran M, Pradheep P, Yuvanesh S, Sivakumar T |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Acceleration stacks (quantization, speculative decoding, adaptive inference) usually demand retraining, per-architecture tuning, or separate draft models. **SpecQuant** is training-free: it derives **multiple quantized variants (INT4 / FP8 / FP16) from one shared base model** (multi-parent), dynamically routes queries by predicted complexity (lightweight variants for simple/factual tasks, higher precision for hard reasoning/long-context), and — crucially — the shared weight-parent design keeps speculative-decoding token acceptance high without a separate draft model or compatibility issues. |
| **Key Innovations** | (1) Multi-parent quantization → single-shared-weights speculative decoding (no draft model, no retraining); (2) complexity-routed adaptive precision as the serving policy; (3) on Qwen2.5 family (MMLU/AlpacaEval/GSM8K): **35–43% speedup with <2% accuracy degradation** — practical on-device LLM inference without special infra. |
| **Link** | [arXiv:2609.21704](https://arxiv.org/abs/2609.21704) |

---

## 6. LLM Post-Training, RL & Distillation

### 6.1 GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Kaichen Zhang, Yuzhong Hong, Junwei Bao, Hongfei Jiang, Yang Song, Dingqian Hong, Hui Xiong |
| **Institution** | HKUST-GZ-affiliated (inferred; Hui Xiong) + industry |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | GRPO-family post-training suffers training instability from **importance sampling**. **GVPO** integrates the *analytical solution of KL-constrained reward maximization* into its gradient weighting, giving a clean interpretation: the GVPO gradient is the **mean squared error between the central distance of implicit rewards and that of actual rewards**. This guarantees (1) a unique optimal solution exactly matching the KL-constrained reward-maximization objective, and (2) **flexible sampling distributions without importance sampling**. GVPO extends naturally to on-policy distillation (OPD) and enables a family of extended OPD objectives. |
| **Key Innovations** | (1) Replaces IS-based weighting with closed-form KL-constrained-optimal weights (unique optimum, no importance sampling); (2) unifies post-training and on-policy distillation under one objective family; (3) positions for "reliable and versatile" post-training with theoretical guarantees — contrasts with heuristic stabilizers in 6.2. |
| **Link** | [arXiv:2609.21432](https://arxiv.org/abs/2609.21432) |

### 6.2 λ‑Controlled GRPO: Turning Flow-Matching Ratio Instability into a Budgeted Resource

| Field | Detail |
|-------|--------|
| **Authors** | Yufeng Wang, Parivesh Priye, Meeshawn Marathe, Ramit Pahwa |
| **Institution** | Stony Brook-aligned (inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Flow-GRPO aligns diffusion/image models by treating the denoising sampler as a policy, but multi-step denoising is *unstable in a specific way*: importance ratios drift below one, disperse, clip at different rates, and leave fewer usable samples late in training. Prior work treats these as separate failure modes needing hand-tuned stabilizers; the paper shows they all arise from one per-step quantity, **path variance**, determined exactly by the sampler's **Gaussian transition kernel** and cheap to estimate. **λ-Controlled GRPO** calibrates importance-ratio behavior from this predicted law (not noisy empirical stats) and allocates gradient effort across steps according to predicted cost; the two governing scales are fixed by standard policy choices, not free tuning parameters. |
| **Key Innovations** | (1) Unifies scattered "stabilizers" into one exactly-computable per-step quantity (path variance); (2) instability recast as a *budgeted resource* — predicted-ratio calibration beats empirical-stat calibration; (3) on text-to-image (OCR-scored difficult text + preference-model-scored human preference) it improves both accuracy and preference reward over the strongest empirical stabilizer, holding late-step path variance within budget where baselines overshoot. |
| **Link** | [arXiv:2609.22041](https://arxiv.org/abs/2609.22041) |

### 6.3 On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Anton Baumann, Akmal Ashirmatov, Leo Schmidt-Traub, Frederike Lübeck, Jonas Hübotter, Thomas Kleine Buening, Andreas Krause |
| **Institution** | ETH Zürich (inferred; Andreas Krause) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | On-policy self-distillation gives dense token-level supervision by conditioning the model on privileged information (e.g., the correct/incorrect solution), but privileged information changes both *what* the teacher knows and *how it behaves* — entangling correctness signals with unintended behavioral shifts. Contrasts **attractive** (move toward a correct-solution-conditioned teacher) vs **repulsive** (move away from an incorrect-solution teacher) distillation: attraction suppresses exploratory reasoning and shortens/confidentializes responses; repulsion lengthens responses, can trigger a latent thinking mode, and becomes unstable. **Contrastive self-distillation** (attraction toward correct + repulsion from incorrect teachers) largely cancels the shared behavioral shifts, leaving a token-level signal that more directly reflects correctness. |
| **Key Innovations** | (1) Systematically separates the correctness channel from the behavioral channel of privileged-conditioned teachers; (2) isolates the pure self-distillation objective (vs prior work that merges it with GRPO); (3) contrastive combination improves reasoning across non-thinking, instruct-only, and already-thinking models while keeping response lengths stable — direct evidence for the wiki's distillation/reasoning-quality track. |
| **Link** | [arXiv:2609.21561](https://arxiv.org/abs/2609.21561) |

### 6.4 SWE-Proof: Can Language Models Resolve Real-World Issues with Machine-Checked Proofs?

| Field | Detail |
|-------|--------|
| **Authors** | George Ma, Benjamin Mikek, Haoyu Li, Ferhat Erata, Yuhao Zhang, Zeren Shui, Behrooz Omidvar Tehrani, Jun Huan, Murali Krishna Ramanathan, Somayeh Sojoudi, Hao Zhou, Anoop Deoras |
| **Institution** | Microsoft + academia (inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Agentic coding benchmarks check held-out tests — incomplete and increasingly memorized. Formal verification avoids both, but prior work covers only standalone tasks with given specs. **Benchproofer** turns a coding task with a known correct patch into a formally verified one: write a spec for the new code, summarize called functions with axioms, admit an instance only after mechanical + adversarial gates agree → **SWE-Proof**, 500 real SWE-bench Verified issues with formally verified correctness (extends to SWE-bench Pro). |
| **Key Innovations** | (1) Verification catches what tests miss: **a quarter to a half of test-passing patches admit counterexamples**; a correct formal spec lifts Opus 4.8 resolution from 85%→95%; (2) the hard part is *writing the spec*: models writing their own gain nothing, only **62%** of their specs pass audit — failure is usually **faithfulness** (a spec that constrains part of the behavior and leaves the rest free); (3) spec quality tracks outcome (fails on 89% of unresolved vs 47% of resolved instances), making faithful spec synthesis a concrete open problem. |
| **Link** | [arXiv:2609.21190](https://arxiv.org/abs/2609.21190) |

---

## 7. Agents, Multi-Agent & Agentic RL

### 7.1 MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems

| Field | Detail |
|-------|--------|
| **Authors** | Kairui Yang, Minghao An, Xunkai Li, Ziheng Yi, Zekai Chen, Guangyuan He, Rong-Hua Li |
| **Institution** | Beijing Institute of Technology (inferred; Rong-Hua Li) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Multi-agent collaboration traces record how agents plan, verify, and repair; reusing them requires preserving an action's **prerequisites and downstream outputs**. Empirical studies: grouping dependencies into functional memory units improves retention; connecting units improves retrieval of jointly-required units *and links*; the preferred unit-combination changes between **instructions vs checklists** even with fixed content. **MACE** co-evolves memory organization and agent memory use from execution feedback: a **MemGoG** structure (functional units as subgraphs of conditions/actions/outputs) connected by support/conflict/repair relations, with a selection loop that records chosen units, formats, outputs, and outcomes to update scores/relations. |
| **Key Innovations** | (1) Memory graphs as *executable structure* (prereqs + downstream needs), not just retrieval indices; (2) bandit-style co-adaptation of unit selection *and* presentation format per task form; (3) across 8 benchmarks averages **81.11% vs 78.97% for the strongest baseline (SAGE)**. |
| **Link** | [arXiv:2609.21533](https://arxiv.org/abs/2609.21533) |

### 7.2 OpenMAS-GCom: A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems

| Field | Detail |
|-------|--------|
| **Authors** | Kairui Yang, Xunkai Li, Kaixiang Zhang, Minghao An, Zekai Chen, Yuxuan Ba, Rong-Hua Li |
| **Institution** | Beijing Institute of Technology (inferred; Rong-Hua Li) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Graph-enhanced multi-agent systems (G-MAS) coordinate LLM agents via communication graphs + role assignments, but final-score comparisons entangle models, communication structure, roles, and cost — so performance differences can't be attributed. **OpenMAS-GCom** is a benchmark for *diagnosing* how communication structures, role assignments, and information flows affect G-MAS performance. (Companion-controller design to MACE 7.1.) |
| **Key Innovations** | (1) Attacks the evaluation-attribution problem in multi-agent systems (isolating topology/roles/information-flow as controlled axes); (2) a diagnostic benchmark to stop "bigger harness = better score" confounds; (3) pairs with MACE to give both a method and a measurement harness for graph-structured agent memory/communication. |
| **Link** | [arXiv:2609.21527](https://arxiv.org/abs/2609.21527) |

### 7.3 DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement

| Field | Detail |
|-------|--------|
| **Authors** | Siyuan Liu, Fan Yu, Dongyu Ru, Yizhu Liu, Yifan Yang, Xuezhi Cao, Xunliang Cai, Yixin Cao |
| **Institution** | Fudan University + Meituan Longcat Team |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | Online agent deployments produce abundant trajectories but verification/annotations are costly. **DENSE** distills traces into reusable feedback *without post-hoc outcome labels*, relying on evidence of local progress, recovery, and unfinished requirements: it organizes evidence into **nested shortcut trees** — compressing redundant attempts, reconciling issues across levels with recovery evidence, summarizing completed branches, expanding unresolved ones. Pairing protocol **REFIT** compares feedback from shared initial trajectories under outcome blindness, with environments/model contexts reset for fresh attempts. |
| **Key Innovations** | (1) Outcome-free trajectory reuse (local progress/recovery, not final labels) as a self-refinement primitive; (2) the REFIT protocol for fair, source-paired feedback comparison; (3) on Terminal-Bench 2.1, best strict pass rate among non-privileged feedback methods across 4 recipients: **+7.12–15.64 pp vs initial executions with 19.0–43.6% fewer recipient tokens** in reruns. |
| **Link** | [arXiv:2609.21423](https://arxiv.org/abs/2609.21423) |

### 7.4 CodeMidas: Scaling Agentic Coding RL Environments from Code Itself

| Field | Detail |
|-------|--------|
| **Authors** | Bowen Ye, Lei Li, Shicheng Li, Zihao Yue, Linghao Zhang, Hanglong Lv, Yuanxin Liu, Wenhan Ma, Hao Tian, Rang Li, Jinhao Dong, Yikai Zhao, Xiangwei Deng, Hailin Zhang, Liang Zhao, Qi Liu, Lingpeng Kong, Tong Yang, Fuli Luo |
| **Institution** | (industry + academia, inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | RL for coding agents needs diverse tasks with reliable verifiers, but prior extraction relies on dev artifacts (issues/commits). **CodeMidas** turns *implemented functionality* in existing codebases into executable RL environments using **source code as the only task-specific input**: agents explore functionality to write behavioral specs, construct tests grounded in real execution, and validate/filter via execution checks + repeated solution rollouts → **5,545 training tasks from 3,185 codebases across 23 languages and 15 domains**. |
| **Key Innovations** | (1) Source-code-only environment construction (no issues/commits needed) — an important scaling unlock for coding RL; (2) execution-grounded specs/tests as reliable GRPO verifiers; (3) training MiMo-V2.5 with GRPO improves all five benchmarks — DeepSWE +11.7%, ProgramBench +17%, Terminal-Bench v2.1 +8.5% — with trajectory analysis showing better exploration/self-verification. |
| **Link** | [arXiv:2609.22068](https://arxiv.org/abs/2609.22068) |

### 7.5 ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL

| Field | Detail |
|-------|--------|
| **Authors** | Qiang Zhang, Ruixue Ding, Fanrui Zhang, Xi Chen, Boli Chen, Shihang Wang, Yinfeng Huang, Yi Zheng, Pengjun Xie, Kaipeng Zhang, Jiawei Liu, Zheng-Jun Zha |
| **Institution** | USTC / industrial (inferred; Zheng-Jun Zha / Kaipeng Zhang) |
| **Published** | Announced 21 Sep 2026 (cs.CL) |
| **Abstract** | Pairwise/preference RL fixes reward-discrimination collapse but still compresses rich comparative feedback into one trajectory-level reward, obscuring decisive intermediate steps and preventing skill consolidation. **ArenaFlow** does hierarchical credit propagation for open-ended agent RL: **tournament-based relative ranking** gives trajectory-level rewards; each comparison carries **structured reflective evaluation** exposing (i) pivotal success steps, (ii) reusable strategy skills, (iii) usage attribution of retrieved skills. Step-level: trajectory advantages propagate to high-confidence pivotal steps by tournament survival depth. Skill-level: global skill memory updated/pruned/retrieved by utility, and high-utility skills become policy priors for future exploration. |
| **Key Innovations** | (1) Three supervision types extracted from each pairwise comparison (pivotal steps, reusable skills, usage attribution) — richer credit than scalar preference; (2) tournament-survival-depth-weighted step credit; (3) a utility-managed global skill memory that feeds back as exploration policy priors — a concrete loop from evaluation to reusable skill. |
| **Link** | [arXiv:2609.21378](https://arxiv.org/abs/2609.21378) |

### 7.6 RACER: Role-Aligned Competence Estimation for Human-AI Routing

| Field | Detail |
|-------|--------|
| **Authors** | Joshua Strong, Emma Sun, Alexander Capstick, Pramit Saha, Cheng Ouyang, J. Alison Noble |
| **Institution** | University of Oxford (inferred; J. Alison Noble) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | **Learning to defer** decides when a system should act and when to hand off to a human expert; **population-adaptive deferral** handles *unseen* experts from a small context set. L2D-Pop can learn routing shortcuts tied to absolute class coordinates; Identity-Free Deferral removes shortcuts but keeps competence constant within a class. **RACER** estimates the **posterior-predictive probability that an unseen expert is correct on a specific query under each candidate class role**, combining these with the model posterior into a Bayes-relevant expert-correctness probability; estimators use candidate-role relations, shared aggregation, symmetric summaries — excluding absolute class-identity channels. Proves class-relabelling invariance, derives a Bayes-aligned deferral surrogate and a plug-in regret bound. |
| **Key Innovations** | (1) Instance-level (query-specific) competence estimation for unseen experts, not class-constant profiles; (2) theoretical grounding (invariance, surrogate, regret bound) atypical for this area; (3) competitive-or-best budget-swept deferral on VinDr-CXR and CheXpert radiologist benchmarks, with strength under hidden subtype dependence on synthetic data. |
| **Link** | [arXiv:2609.21953](https://arxiv.org/abs/2609.21953) |

---

## 8. Evaluation, Retrieval & Evidence Discipline

### 8.1 When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation

| Field | Detail |
|-------|--------|
| **Authors** | Sy-Tuyen Ho, Minghui Liu, Furong Huang |
| **Institution** | University of Maryland (inferred; Furong Huang) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | As AI reviews enter public corpora, AI peer review becomes **recursive** — later reviewers learn from earlier models' judgments. Controlled one-step study: fine-tune a reviewer on official ICLR 2018–2023 reviews, then train four successors on ICLR 2024 with varied mixtures of official + model-generated reviews. **Synthetic reviews compress rating distributions and reduce semantic diversity** — **scientific-judgment collapse**. Mitigation: **TrustReviewer**, an open-source reviewer system with (i) training-time prevention (single-stage training on a curated, de-degenerate corpus) and (ii) test-time correction (paired activation steering). |
| **Key Innovations** | (1) Names and causally demonstrates "scientific-judgment collapse" from recursive reviewer training (direct evidence for the LLM-as-judge poisoning concern); (2) treats training-time data hygiene and test-time steering as complementary; (3) open-source TrustReviewer for the evaluation community — empirics relevant to how model-generated ground truth can degrade future alignment/eval data. |
| **Link** | [arXiv:2609.20942](https://arxiv.org/abs/2609.20942) |

### 8.2 How Many Humans Is a Judge Panel Worth?

| Field | Detail |
|-------|--------|
| **Authors** | Chao Li, Yingying Yu, Yunfeng Li |
| **Institution** | (academic, inferred; tentative) |
| **Published** | Announced 21 Sep 2026 (cs.CL) |
| **Abstract** | "Panel of LMs ≈ N humans" claims depend on what's matched. Audits categorical judge panels against empirical human label distributions, retaining disagreement (not binary errors to one gold label). **Spectral residual diversity** νH (matching participation ratio of a normalized residual Gram matrix to conditionally independent human-reference draws) vs **distributional squared error** νMSE: the same 32-judge panels on three ChaosNLI tasks have **νH=4.24–6.50 but νMSE=2.30–3.75**. A spectral identity separates the error-contributing eigenvalues, member energies, and averaging-direction weights; the consensus-direction share of centered residual variance is 43.8% (MNLI-m) / 33.7% (SNLI). |
| **Key Innovations** | (1) Two distinct "effective size" measures (spectral-diversity vs distribution-recovery) that disagree for the same panels — they are *not* interchangeable quality metrics; (2) an identity decomposing what drives error (eigenvalues/energies/averaging weights); (3) both measures are well below "32 humans", i.e., LM panels enrich diversity slower than independent humans retain it. |
| **Link** | [arXiv:2609.21277](https://arxiv.org/abs/2609.21277) |

### 8.3 A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal

| Field | Detail |
|-------|--------|
| **Authors** | Hiskias Dingeto |
| **Institution** | (single author, inferred) |
| **Published** | Announced 21 Sep 2026 (cs.AI) |
| **Abstract** | Models can hold knowledge they don't report — sandbagging, concealment, or answering against what it knows; outputs alone can't distinguish hiding from not-knowing. Borrowing forensics' **Concealed Information Test**, **PIR (Probe of Internal Recognition)** presents a question with candidate answers and reads from model internal states which candidate the model *recognizes* as correct — reference-free (no honest model, no labeled truth). |
| **Key Innovations** | (1) A principled probe separating "won't answer" from "cannot answer" (recognition vs knowledge); (2) robustness across concealment forms (prompted deception, trained sandbagging, even password-locked/circuit-broken checkpoints: recognition 0.85–0.93); (3) direct uses: sandbagging audits and **unlearning verification** (recognition drops when knowledge is actually removed) — actionable for the wiki's safety/unlearning track. |
| **Link** | [arXiv:2609.21996](https://arxiv.org/abs/2609.21996) |

### 8.4 Energy Transfer Detection: Pretraining-Data Detection from a Free-Energy Perspective

| Field | Detail |
|-------|--------|
| **Authors** | Chenye Ke, Zirui Liu, Qi Liu, Yan Zhuang, Jintao Zhang, Zhenya Huang, Shijin Wang |
| **Institution** | USTC / iFLYTEK-aligned (inferred; Shijin Wang) |
| **Published** | Announced 21 Sep 2026 (cs.LG) |
| **Abstract** | Membership detection is hard because high likelihood can reflect exposure *or* generalization. In the joint space of prediction loss × predictive entropy, a likelihood-only detector draws a *horizontal* boundary and mistakes predictable non-members for members. **ETD** uses an **inclined boundary** (loss relative to predictive entropy): entropy correction preserves the expected membership signal while reducing its variance, and the adjusted score admits a **Helmholtz free-energy interpretation** (macroscopic residual free-energy transfer). |
| **Key Innovations** | (1) An entropy-corrected, mean-variance-justified membership score with a clean information-theoretic/thermodynamic frame; (2) simple and training-free (loss + entropy only); (3) best average detection with **AUROC up to +3.5% and TPR@5%FPR up to +5.1%** over SOTA baselines, robust across settings — relevant to copyright/training-data audit debates. |
| **Link** | [arXiv:2609.21888](https://arxiv.org/abs/2609.21888) |

### 8.5 Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring and Abstention

| Field | Detail |
|-------|--------|
| **Authors** | Andre Bacellar |
| **Institution** | (single author, inferred) |
| **Published** | Announced 21 Sep 2026 (cs.IR) |
| **Abstract** | Multi-hop retrieval failures cluster in structurally predictable subpopulations. Two theorems: **(CWAR Reducibility)** confident-failure reduction is possible iff retrieval features carry mutual information about success (satisfied by LLM-judge pipelines, weaker in dense-only settings — explaining the AUC-AC gap); **(Feature Regime Complementarity)** no single ANN score feature dominates all regimes (query length on MuSiQue, hop-1 concentration on HoVer). Instantiates **RegimeAbstain** with **RCS**, a logistic function of up to nine query-ANN structural features (no extra LLM calls) driving a calibrated abstention policy, plus the **CWAR** (Confident-Wrong-Answer Rate) metric. |
| **Key Innovations** | (1) A framework where failure prediction is *provably* regime-dependent — retrieval confidence as an explicit research primitive; (2) cheap (feature-only) calibrated abstention: **on MuSiQue LLM-judge, CWAR drops 39.5%→20.6% at 50% coverage (−47.8%), ECE=0.035**, best/co-best AUC-AC in all five conditions vs eight baselines; (3) cross-dataset transfer (MuSiQue→2WikiMultiHopQA, −0.5 pp AUC) supporting domain-agnostic regime features. |
| **Link** | [arXiv:2609.22056](https://arxiv.org/abs/2609.22056) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **Auto-bidding/oCPX comes back to the daily layer, foundation-model style** | OneBid (unified oCPX MoE foundation model, CROP offline post-training, +2.2% ADVV deployed at Kuaishou, +13.1% ROAS), ADAPT (disentangled advertiser profiles, train-free update/cold-start) — classic end-to-end CTR-ML still absent (~8 windows) but the bidding layer is clearly fertile |
| **Production search/retrieval systems content deepens: depth/breadth split + online autoresearch** | Hybrid GPU-CPU co-serving at trillion-doc scale (relevance+engagement A/B wins), EvoPilot 37-day video-discovery autoresearch campaign (false 22-pp decline traced to an eval defect; true +3.20 pp, +0.66% GSRR online) — first-party infrastructure evidence rare at the daily layer |
| **Private research matures into evaluation-first skeletons: attribution, diagnosis, post-training safety** | Recursive-LLMs-OOD (simplicity bias picks shortcuts), TaxiGPT mechanistic world-model reinterpretation, GameASG-Bench (93.2% avg L2 pass but 55.3% strict success), RecreationWorld (GPT-6 Astra 58.1% overall, 2.8% full-programmatic), ArenaFlow (credit hierarchy), CodeMidas, OpenMAS-GCom (attribution), SWE-Proof (test-passing patches admit counterexamples) |
| **Recurrent & SSM architectures keep compounding: depth↔time trade-offs + polysemy** | Trading Depth for Time (1 thought token ≈ 67–81% of 2L depth at ~48% fewer params), Depth-Recurrent prediction dynamics (direction+pairing as early-stop signals), DSRec (time-modulated dual-interest SSM for sequential rec), Recursive LMs OOD |
| **Long-context serving: learned/prefetch sparsity + predictive tiering** | RBS-Attention (mean-dilution rescue branch, 5.97× TTFT @128K), Elastic Threshold Attention (trainable thresholds, sink removal, 2.5× decode @512K), TierKV (closed-form predictive tier assignment, 17.6× prefill), SpecQuant (multi-parent quantization + speculation) |
| **Post-training theory chases stability without hand-tuning** | GVPO++ (closed-form KL-optimal weights, no importance sampling), λ-Controlled GRPO (path-variance budgeted Flow-GRPO), Repulsive/Attractive Teachers (contrastive self-distillation isolates correctness), Cal-OPD (teacher-deviation calibration, runner-up) |
| **Evaluation/verification becomes the honest-measurement agenda** | TrustReviewer (scientific-judgment collapse, UMD), How Many Humans Is a Judge Panel Worth (νH 4.24–6.50 vs νMSE 2.30–3.75), PIR lie-detector probe (unlearning verification), ETD (free-energy membership detection), RegimeAbstain (calibrated retrieval abstention) |

(Runner-ups worth a look, grep-verified unclaimed: **2609.21425** Tracing the evidence behind zero-shot TSF (evidence-access audit framework); **2609.21044** Lightweight pre-encoder gate for TS forecasters; **2609.21899** ExpBoN (exponential-noise soft BoN + ExpGSI, −14–45% compute); **2609.21619** Cal-OPD (calibrated teacher–student discrepancy, keeps only 52–65% of signal and wins); **2609.21325** LEGIT credentialing protocol for AI agent marketplaces; **2609.20974** Attention-Aware Routing in MoEs (+3.37 pp GSM8K on OLMoE); **2609.21672** L0-MoE (2.5× dense-LLM speedup); **2609.20886** BI-Agent / BI-Bench end-to-end business intelligence; **2609.20845** ZENDAYA closed-form bandwidth dial for streaming multimodal decoders; **2609.21894** LLMs as feature engineers for text-and-tabular; **2609.21496** Two Fault Lines (latent polarity geometry of X Community Notes); **2609.20824** Do small language models know what they don't know.)

(End of file — total 35 papers / 8 sections)