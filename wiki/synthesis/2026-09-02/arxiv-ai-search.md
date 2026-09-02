---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-09-02)"
type: synthesis
created: 2026-09-02
updated: 2026-09-02
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, rl, world-models, generative-retrieval, industrial-recsys, marketplaces, mechanism-design, eval, daily-digest]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-09-02 (Wednesday) · Scope: curated across the requested domains (AI, LLMs, recommendation, advertising, sequential modeling, CTR, games). Companion to the same-day [arxiv-daily](arxiv-daily.md) (which covers the Wed 2 Sep wave `2609.00002–2609.00xxx` highlights incl. CoVeMem, CADET, TGA, RLVR weak-model exploration, Game-AI). This report is a **cross-domain deep pass** over the **fresh 1–2 Sep 2026 submission wave (`2609.xxxxx`)**, complementary to the daily digest. **17 featured + 2 honorable mentions.** Every arXiv ID below is grep-verified absent from `wiki/`.
>
> Method: titles/abstracts/author-affiliations recovered via arXiv `abs` pages (direct fetch) + the cs.AI new-listing scan. Affiliations marked *(stated)* come from paper/project front matter or documented production deployments, *(inferred)* = deduced from author identities; otherwise "not stated". Temp files under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`, cleaned up after this report lands.

---

## ① Industrial Recommendation, Ranking & Advertising (4)

### 1.1 ReST: From Language to Behavior — Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs

| Field | Detail |
|-------|--------|
| **Authors** | Jie Chen, Xiangqian Yu, Yanchao Lian, Tan Lu, Run Yang, Zhengchun Shang, Xing Wang, Cheng Chen, Ke Hu, Qiang Li, Tianjiu Yin, Xiaobing Liu |
| **Institution** | Not stated (production advertising platform) |
| **Submitted** | 2026-09-01 · [2609.01240](https://arxiv.org/abs/2609.01240) · cs.IR |
| **Abstract** | Scaling Transformers drove gains in language modeling, but transplanting to **behavior-sequence modeling in production ranking** is hard: rec signals are noisy, temporally irregular, sparsely supervised; and each request scores many candidates against one shared user history under tight latency. **ReST** introduces a recommendation-native scaling framework: (1) *signal quality* — sequence encoder with dual-gated attention, rotary positional+temporal embedding, stabilized residual normalization, training-only auxiliary objectives; (2) *computation asymmetry* — factorization into a heavy reusable encoder + lightweight cross decoder with projection-free KV attention and token-specific parameterization, coupling shared-prefix training with shared-prefix serving (compute-once, decode-many-times). Beats LLM-style transformer blocks which saturate. **One-week online A/B on a production advertising platform: +1.31% online AUC and +11.93% core revenue metric within a 50 ms P99 budget; fully deployed.** |
| **Key innovations** | Rec-native (dual-gated attention, rotary temporal PE) rather than LLM-native scaling; encoder/decoder factorization for the many-candidates-one-history setting; GPU-friendly shared-prefix serving; published production lift numbers. |
| **arXiv** | [2609.01240](https://arxiv.org/abs/2609.01240) |
| **Why it matters** | Extremely strong industrial anchor for the wiki's "behavior-sequence scaling" / production-LLM-ranker thread (cf. GenRec, CADET in prior reports): scaling the *sequence* axis, not just model width, pays off in live ads ranking. |

### 1.2 TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking toward Unified Generation and Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | TGR Team: Lei Cheng, Haonan Hu, Beibei Kong, Yudong Li, Zang Li, Yunsheng Pang, Hongyang Su, Jianchao Tu, Yunlong Wang, Bing Wen, Junzhang Zhu, Shaojie Zhu, Chengxiang Zhuo |
| **Institution** | Tencent *(stated: "Tencent Generative Recommendation", deployed across Tencent production surfaces)* |
| **Submitted** | 2026-09-01 · [2609.00986](https://arxiv.org/abs/2609.00986) · cs.IR |
| **Abstract** | Industrial recommenders rely on cascaded retrieval/pre-rank/rank/rerank whose separately optimized models limit scaling and lack semantic knowledge/reasoning. **TGR** advances the generative paradigm along three coupled directions: **TGR-GenRank** (CCFormer: unified feature tokenization, scalable Transformer backbone, feature-field-separated cross-attention, subspace token mixing, hierarchical sequence compression, per-item multi-task outputs); **TGR-GenRec** end-to-end generation under two paradigms — **BARGE** (item-boundary-loss + semantic-drift mitigation via item context-aware attention, hierarchical path reranking, orthogonal dual-path decoding) and **HiGR** (whole-slate generation with prefix-structured semantic IDs, coarse-to-fine decoding, listwise multi-objective alignment); **TGR-Reason** injects offline-generated semantic-ID reason tokens into online decoding (reasoning without request-time rollout). **Deployed at Tencent scale (hundreds of millions of users): CCFormer +3.57% CTR, +1.71% ad revenue (5 A/B scenarios, 2 fully launched); BARGE Hit@5 +10.2–16.9%, +0.60% CTR, +1.70% reading time; HiGR slate quality +15.9–21.3% with 5× inference speedup; TGR-Reason cold-start new-user Hit@1 +477.8%, +13.09% new-user exposure-to-conversion.** |
| **Key innovations** | Unified generation + reasoning across the whole ranking stack; whole-slate (not just per-item) generation; offline-injected reason tokens for zero-request-time-cost reasoning; massive production numbers incl. ads revenue. |
| **arXiv** | [2609.00986](https://arxiv.org/abs/2609.00986) |
| **Why it matters** | A flagship datapoint for the wiki's generative-recommendation thread: Tencent ships GenRank→GenRec→Reason as one framework — the strongest evidence yet that the generative paradigm is production-ready, with direct ad/CTR numbers. |

### 1.3 SwapRec: Warming Up Cold Items Through Training-Time Swaps

| Field | Detail |
|-------|--------|
| **Authors** | Marta Moscati, Jan Malte Lichtenberg, Davide Abbattista, Antonio De Candia, Laura Boggia, Matteo Ruffini |
| **Institution** | Not stated |
| **Submitted** | 2026-09-01 · [2609.00913](https://arxiv.org/abs/2609.00913) · cs.IR · **DaQuaMRec @ RecSys 2026** |
| **Abstract** | Interactions with **cold items** hurt real-time personalization of ID-based recommenders: using them degrades preference estimates, excluding them blocks real-time updates. A common industrial heuristic swaps cold-start items for their most similar "warm" neighbor (similarity from side info) at inference. The authors show sequential models are **not robust to such swaps**, and propose **SwapRec**: apply the *same swap heuristic at training time* so the model learns to expect it. Across three recommendation domains (online shopping, movie, music) and multiple SOTA sequential models, SwapRec yields substantially more accurate recommendations in the presence of cold-item interactions while also lifting cold-item share of recommendation lists. |
| **Key innovations** | Data-quality-aware training-as-deployment realism: matching the inference-time swap heuristic in training; cheap, model-agnostic recipe with consistent gains. |
| **arXiv** | [2609.00913](https://arxiv.org/abs/2609.00913) |
| **Why it matters** | Directly relevant to the wiki's cold-start / data-quality thread: it reframes a common inference hack as a training regularization — the same "simulate serving distribution at train time" logic the wiki tracks in CTR/ads systems. |

### 1.4 CoGR: It Takes Two to Match — Co-Evolving Generative Retriever with Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Runpeng Dai, Kaili Huang, Changsung Kang, Ciya Liao |
| **Institution** | *(inferred: Google — internal APP Marketplace dataset used)* |
| **Submitted** | 2026-09-01 · [2609.00638](https://arxiv.org/abs/2609.00638) · cs.IR / cs.CL |
| **Abstract** | Retrieval is the first stage of modern **search and advertising** systems. Prior work uses LLMs for query expansion/data synthesis/retrieval-feedback, but the generative component stays query-side while matching is still delegated to a downstream retriever. **CoGR** instead trains LLMs to *directly construct retrieval representations on both query and item sides*: each generator emits a compact keyword set matched via an inverted index (keeping compatibility with existing keyword infrastructure). Two-stage pipeline: SFT establishes an aligned keyword space; then **co-evolving RL** alternately optimizes query- and item-side generators with GRPO against the opposite side's frozen index, both optimizing the same query-to-item retrieval F1 (item side gets a counterfactual marginal reward measuring its keywords' contribution to query-side F1). Across 10 sparse/dense/generative baselines, best on internal APP Marketplace and public **WANDS**: **+10.9% and +36.1% F1 over the strongest baseline**; query–item keyword spaces converge over training. |
| **Key innovations** | Fully generative retrieval on *both* sides of the match; alternating GRPO co-evolution with counterfactual marginal reward; deployable on existing inverted-index infra. |
| **arXiv** | [2609.00638](https://arxiv.org/abs/2609.00638) |
| **Why it matters** | Advances the wiki's generative-retrieval thread beyond query-side tricks to true two-sided matching, with explicit advertising-marketplace context (WANDS = Wanxiang Ads search). |

---

## ② Sequential & Conversational Recommendation (4)

### 2.1 TS-SSM: Two-Sided State-Space Models for Sequential Recommendation with Non-Random Multimodal Review Feedback

| Field | Detail |
|-------|--------|
| **Authors** | Ziwen Pan, Zihan Liang, Ruoxuan Xiong |
| **Institution** | *(inferred: Stanford GSB — Ruoxuan Xiong's home institution)* |
| **Submitted** | 2026-08-31 · [2609.00165](https://arxiv.org/abs/2609.00165) · cs.IR · **Findings of EMNLP 2026** |
| **Abstract** | Two-sided platforms are dynamic: user preferences shift, item popularity evolves, reviews both reflect and drive change. Yet existing sequential recommenders treat reviews as passive user-state signals, ignoring (1) that **review generation is non-random** (depends on latent user+item states) and (2) that **reviews reshape item states and spill over to related items**. **TS-SSM** is a two-sided state-space model with: modality-missing-not-at-random review fusion encoding observation patterns; user-state evolution with temporal variation + local graph message passing over related items; item-state evolution with **asymmetric carryover of positive vs. negative feedback**. On six Amazon categories: **Recall@20 +14.8–18.8% over BSARec, +11.7% avg over HM4SR**; Goodreads Fantasy Recall@20 .5191→.5847. |
| **Key innovations** | Explicit *two-sided* (user + item) latent-state dynamics for rec; MNAR-aware observation modeling; asymmetric item-side feedback carryover. |
| **arXiv** | [2609.00165](https://arxiv.org/abs/2609.00165) |
| **Why it matters** | The state-space-model route for sequential rec the wiki tracks (cf. Mamba-family rec models), now with a principled non-ignorable-feedback and item-dynamics treatment — directly relevant to the sequential-modeling thread. |

### 2.2 WMG-RL: World Model-Guided Reinforcement Learning via Counterfactual User Engagement Simulation

| Field | Detail |
|-------|--------|
| **Authors** | Ang Li, Xin Xu, Bin Liang, Yue Ma, Fubang Zhao, Yangyang Kang, Kam-Fai Wong |
| **Institution** | Not stated (academic–industrial mix; Kam-Fai Wong, CUHK) |
| **Submitted** | 2026-09-01 · [2609.01067](https://arxiv.org/abs/2609.01067) · cs.IR · **EMNLP'26** |
| **Abstract** | RL for user-centric agents is limited by cost/latency/risk of online feedback and the lack of counterfactual comparisons under the same user state. **WMG-RL** gives a frozen **User Engagement World Model (UEWM)** — action = recommended item, observation = heterogeneous user feedback — that infers *user-specific* dynamics from engagement history and applies them to candidate items, providing reward supervision *before* real exposure. Downstream policies propose multiple candidate items; UEWM predicts engagement in parallel; predictions become dense rewards. UEWM rewards transfer across domains, and **a compact 1.7B student policy matches or surpasses much larger LLMs** on downstream recommendation tasks. |
| **Key innovations** | User-engagement world model as a pre-exposure reward simulator (language-world-model ideas applied to rec); parallel counterfactual feedback for multiple candidates under one user state. |
| **arXiv** | [2609.01067](https://arxiv.org/abs/2609.01067) |
| **Why it matters** | Strong methodological bridge between the wiki's world-model and recommendation-RL threads — RL for personalization without risky online data collection. |

### 2.3 DREAMS: Structured Context Modeling for Conversational Recommender Systems via Dual-node Monte Carlo Tree Search

| Field | Detail |
|-------|--------|
| **Authors** | Jincheng Zhang, Chen Huang, Wenqiang Lei, See-Kiong Ng, Yang Deng |
| **Institution** | Not stated (multi-institution; Wenqiang Lei — Sichuan University, See-Kiong Ng — NUS) |
| **Submitted** | 2026-09-01 · [2609.00618](https://arxiv.org/abs/2609.00618) · cs.IR / cs.AI |
| **Abstract** | Conversational recommender systems (CRSs) must both *elicit* and *exploit* user preferences. **DREAMS** models conversational context as a **tree structure that explicitly tracks preference evolution** over multi-turn interaction, with two specialized node types: **elicitation nodes** use MCTS to strategically explore conversational actions and infer latent preferences; **exploitation nodes** use LLM-based refinement to turn the tracked preference state into structured retrieval queries. Benchmark experiments validate the design. |
| **Key innovations** | Dual-objective (elicit vs. exploit) tree-structured context; MCTS for preference elicitation combined with LLM query synthesis for exploitation. |
| **arXiv** | [2609.00618](https://arxiv.org/abs/2609.00618) |
| **Why it matters** | Extends the wiki's conversational-recommendation / MCTS-agent threads with an explicit preference-tracking structure — a clean decomposition of the CRS objective. |

### 2.4 HypReflect: Hypotheses-Guided Self Distillation for Continual Personalization

| Field | Detail |
|-------|--------|
| **Authors** | EunJeong Hwang, Kushan Mitra, Dan Zhang, Hannah Kim, Estevam Hruschka |
| **Institution** | *(inferred: Amazon — Hruschka, Kim, Zhang at AWS AI Labs)* |
| **Submitted** | 2026-08-31 · [2609.00251](https://arxiv.org/abs/2609.00251) · cs.AI |
| **Abstract** | User preferences are rarely stated fully and emerge through heterogeneous, latent, noisy signals; existing methods lean on raw interaction histories or costly reward-based optimization. **HypReflect** is a reliable, scalable continual-personalization framework that infers **explicit, uncertainty-aware preference hypotheses** from diverse user signals, reflectively refines them as evidence accumulates, and injects the user model back via **hypotheses-guided self-distillation**. Across online personalization, multi-session interactions, and implicit behavioral signals, it outperforms raw-history and incremental-update baselines, with strong generalization to unseen users and cross-domain settings, stability across context budgets, and reusable hypotheses. |
| **Key innovations** | Explicit/refineable preference models (not opaque embedding memory); uncertainty-aware hypotheses; self-distillation instead of reward optimization for personalization. |
| **arXiv** | [2609.00251](https://arxiv.org/abs/2609.00251) |
| **Why it matters** | A production-plausible recipe for the wiki's personalization thread: interpretable, revisable user models + cheap self-distillation — contrast with reward-based personalization approaches. |

---

## ③ LLM-Driven Recommendation Evaluation & Experimentation (3)

### 3.1 RPCBench: A Benchmark for Proactive Premise Critique in LLM-based Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Zhongru Chen, Yuan Wu, Yi Chang |
| **Institution** | Not stated |
| **Submitted** | 2026-09-01 · [2609.00918](https://arxiv.org/abs/2609.00918) · cs.AI / cs.CL |
| **Abstract** | LLMs act as interactive recommender assistants, but evaluation focuses on plausible item ranking while ignoring whether they can **recognize flawed recommendation requests**. **RPCBench** evaluates *Recommender-Premise Critique*: detect, diagnose, and properly handle faulty premises in natural-language rec requests. Evidence-grounded instances across five domains, ten premise-failure types; fine-grained eval of proactive detection, error localization, post-detection handling, evidence faithfulness. Across 11 LLMs: **proactive detection is the main bottleneck**; worst on underspecified-premise errors; target-critical info density matters more than redundant evidence; **longer reasoning does not monotonically help (peaks at intermediate length, "overthinking penalty")**. |
| **Key innovations** | First benchmark for proactive critique of faulty premises (vs. item quality) in LLM-based rec; evidence-grounded failure taxonomy; finds the overthinking penalty. |
| **arXiv** | [2609.00918](https://arxiv.org/abs/2609.00918) |
| **Why it matters** | Adds an evaluation-quality angle to the wiki's LLM-rec thread: conversational recommenders should push back on bad queries, and current models' main weakness is *detection*, not handling. |

### 3.2 Authority Bias in Conversational Search Engines for Academic Paper Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Uthman Jinadu, Parsa Ghazvinian, Anjila Budathoki, Benjamin M. Ampel, Rajshekhar Sunderraman, Yi Ding |
| **Institution** | Not stated |
| **Submitted** | 2026-08-31 · [2609.00248](https://arxiv.org/abs/2609.00248) · cs.AI · **EMNLP 2026 Main** |
| **Abstract** | Causal test of whether LLM conversational search engines judge papers on content or **authority signals** (author prestige, venue, citations). Holding title+abstract constant and varying authority metadata (original / flipped / boosted) across eight LLMs (5 open + 3 frontier closed) in a top-1 recommendation setting: authority bias is **substantial and directional**, varies markedly across models, only partially fixable via prompt debiasing. Documents a **say–do gap**: debiasing instructions suppress authority mentions far faster than authority-driven flips — so surface auditing systematically underestimates behavioral bias. |
| **Key innovations** | Counterfactual/causal authority-bias protocol (flipped/boosted metadata) rather than correlation; the say-do gap between verbalized and behavioral bias. |
| **arXiv** | [2609.00248](https://arxiv.org/abs/2609.00248) |
| **Why it matters** | A rigor-relevant caveat for the wiki's LLM-recommendation thread — evaluating rankers on listed quality metrics may miss authority-driven systematic distortion. |

### 3.3 Data-Driven Persona-Conditioned Agents for A/B Test Simulation

| Field | Detail |
|-------|--------|
| **Authors** | Ziyad Benomar, Weronika Łajewska, Leonardo Perelli, Saab Mansour |
| **Institution** | *(inferred: Amazon — Mansour, Benomar at Amazon)* |
| **Submitted** | 2026-09-01 · [2609.01038](https://arxiv.org/abs/2609.01038) · cs.AI · **EMNLP 2026 Industry Track** |
| **Abstract** | A/B testing requires real traffic, engineering effort, and weeks of measurement. This work proposes an **LLM-agent simulator of A/B test outcomes** conditioned on **data-driven personas** grounded in anonymized behavioral data (activity patterns, engagement signals, inferred demographics) rather than synthetic/rule-based personas. Frames A/B simulation as a structured question task and studies question design formats, persona data source/domain alignment, persona depth vs. population diversity trade-offs, and subsampling. On 40 A/B tests covering two metric types: **0.75–0.90 directional accuracy** depending on metric — evidence data-driven personas are viable for fast, low-cost experiment pre-screening. |
| **Key innovations** | Behaviorally-grounded (not synthetic) personas for population simulation; an experimental pre-screening layer before expensive real traffic. |
| **arXiv** | [2609.01038](https://arxiv.org/abs/2609.01038) |
| **Why it matters** | Connects the wiki's A/B-experimentation and agent-simulation threads: if pre-screening with faithful personas works, whole experimentation loops could shift to simulation first. |

---

## ④ LLM Agents, RL & Self-Evolution (3)

### 4.1 ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Fanrui Zhang, Ruixue Ding, Qiang Zhang, Xi Chen, Boli Chen, Shihang Wang, Qiuchen Wang, Hongmin Zhan, Jinxin Bian, Xingchao Li, Peijin Zheng, Hao Cheng, Pengjun Xie, Kaipeng Zhang, Jiawei Liu, Zheng-Jun Zha |
| **Institution** | Not stated (multi-institution incl. likely SH/USTC teams — Zheng-Jun Zha on author list) |
| **Submitted** | 2026-09-01 · [2609.01058](https://arxiv.org/abs/2609.01058) · cs.AI |
| **Abstract** | RL of long-horizon open-ended agents lacks verifiable answers and scalable rubrics; near the capability boundary, rewards are brittle, giving weak/noisy rollout contrast for group-based policy learning. **ARISE-RL** is a full-cycle self-evolution framework coupling a **Generator** (task/rubric creator, grounded in real tool observations, rewarded for producing valid intermediate-difficulty tasks near the Solver's boundary) with a reasoning **Solver** (learns from fine-grained rubric-satisfaction signals via multi-step reasoning + tool use). Adds **Reward-Gated Self-Evolution Distillation (RG-SED)**: distill a memory-augmented variant of the same policy back into itself *only when* it yields empirical reward improvement (avoiding blind imitation of noisy guidance). Introduces **ECR-Bench**, an expert-calibrated rubric benchmark (single-tool deep research, multi-tool travel planning). SOTA across all evaluated benchmarks. |
| **Key innovations** | Generator/Solver co-evolution mediated by rubrics (scales task+rubric creation as agents improve); reward-gated selective self-distillation; expert-calibrated rubric benchmark. |
| **arXiv** | [2609.01058](https://arxiv.org/abs/2609.01058) |
| **Why it matters** | A complete answer to the wiki's "RL needs verifiable rewards / scalable rubrics" problem — agentic rubric generation + gated distillation is a strong new entry in the self-evolving-anthropic-loop literature. |

### 4.2 AgentFactory: Towards Automated Agentic System Design and Optimization

| Field | Detail |
|-------|--------|
| **Authors** | Enci Zhang, Haofeng Wang, Yuesheng Zhu, Xiaole Cui, Guibo Luo |
| **Institution** | Not stated |
| **Submitted** | 2026-09-01 · [2609.01045](https://arxiv.org/abs/2609.01045) · cs.AI |
| **Abstract** | Manually designing/optimizing agentic systems doesn't scale; prior auto-optimization of workflows ignores model capabilities and single-objective metrics. **AgentFactory** jointly optimizes **foundation models and workflow structures** under multiple objectives (performance, cost, efficiency), using LLMs-as-optimizers in a three-stage pipeline to search configurations of fine-tuned models + optimized workflows. Across eight benchmarks in five domains (reasoning, coding, math, medicine, finance): **+9.1% avg over manual and automated baselines**, up to **19.6% (MedQA) / 18.7% (FinEval)** on domain tasks. |
| **Key innovations** | Joint model+workflow search with multi-objective constraints — treats agentic systems as a co-design (fine-tune + orchestrate) rather than workflow-only. |
| **arXiv** | [2609.01045](https://arxiv.org/abs/2609.01045) |
| **Why it matters** | Feeds the wiki's agent-engineering thread: automated, cost-aware agentic system synthesis is quickly becoming a standard design tool. |

### 4.3 One Policy Is Enough: Single-Agent Reinforcement Learning Outperforms Tree Search for Chemistry Tool Learning

| Field | Detail |
|-------|--------|
| **Authors** | Armin Dariani, Sifan Wu, Bang Liu, Entao Yang |
| **Institution** | *(inferred: Mila / Université de Montréal — Bang Liu)* |
| **Submitted** | 2026-08-31 · [2608.30952](https://arxiv.org/abs/2608.30952) · cs.LG / cs.CL |
| **Abstract** | Chemistry answers need exact computation and database lookups, so the model must select the right tool, fill typed arguments, and chain calls. Prior **CheMatAgent** uses hierarchical evolutionary MCTS (policy + execution models, two learned critics, one regressed partly onto GPT-assigned scores). This work shows a **single policy suffices**: interleave reasoning, tool calls, and returns in one left-to-right generation; SFT warm-up, then **outcome-level RL against a programmatic reward read directly off the gold call chain** (no critic, no judge). On ChemToolBench multiple-tool chemistry: **+5.5% Tool F1 / +9.6% Return F1 (Qwen-2.5-7B) and +3.7% / +3.9% (Llama-3.1-8B)** vs. strongest search config, at *one* model invocation per question vs. search cost that grows with the tree; also leads answer Pass Rate on Qwen-2.5-7B. |
| **Key innovations** | Removes learned critics/verifiers from the training loop entirely; shows search-time scaling isn't necessary when reward is programmatic and read off gold chains. |
| **arXiv** | [2608.30952](https://arxiv.org/abs/2608.30952) |
| **Why it matters** | A clean, testable counterexample to tree-search-over-policy in tool-use agents — relevant to the wiki's agentic-RL and search-vs-single-policy threads (cf. CAST in prior report which said solver advantage distillation helps). |

---

## ⑤ Games, World Models & Autonomous Software Development (3)

### 5.1 CM-PTM: User Representation via Cross Multi-source Behavior Pre-training for Mobile Games

| Field | Detail |
|-------|--------|
| **Authors** | Chengqi Yang, Yiran Qiao, Feng Liu, Xingyu Lou, Zijun Zhou, Xiaoyun Mo, Changwang Zhang, Jiayuan Xu, Jun Wang, Xiang Ao |
| **Institution** | Not stated (incl. Xiang Ao — ICT, CAS; ICDM 2026 regular paper) |
| **Submitted** | 2026-09-01 · [2609.01057](https://arxiv.org/abs/2609.01057) · cs.AI · **IEEE ICDM 2026** |
| **Abstract** | User-representation pre-training typically covers single-app or app-level behaviors, ignoring that device-level user intent emerges from **cross-source, multi-granular interactions** (heterogeneous behavior sources + hierarchical action structure). **CM-PTM** is a Cross Multi-source Behavior Pre-Training Model for mobile-game user representation on device-level logs, using **hierarchical cascaded mask-then-predict** proxy tasks: first infer the *source* of the next behavior, then progressively refine at app-action level — unifying cross-source dependencies and fine-grained behavioral dynamics in one pre-training paradigm. On large-scale real mobile datasets it captures endogenous interests and consistently improves downstream mobile-game recommendation. |
| **Key innovations** | Device-level (not app-level) cross-source behavior pretraining; cascaded source→app→action prediction; applied to mobile-game rec. |
| **arXiv** | [2609.01057](https://arxiv.org/abs/2609.01057) |
| **Why it matters** | Represents the wiki's games and user-representation threads at once — behavioral pretraining for game-oriented personalization is a growing production use-case. |

### 5.2 HyperWorld: Hypergraph-Structured State Serialization Improves Learned Textual World Models

| Field | Detail |
|-------|--------|
| **Authors** | Yun-Jian Zhang, Chen-Wei Liang, Tian-Yi Zhang, Jian Ding, Yi-Lun Wu, Ao-Bo Li, Wei-Cong Su, Saifullah, Hong-Yu An, Mu-Jiang-Shan Wang |
| **Institution** | Not stated |
| **Submitted** | 2026-06-12 (v1; appears in the 2609.xxxxx new-listing scan) · [2609.00002](https://arxiv.org/abs/2609.00002) · cs.AI |
| **Abstract** | Text-world agents must learn symbolic action effects from serialized state descriptions; the role of **serialization structure** is underexplored. **HyperWorld** is a controlled study comparing raw observations and three symbolic serializations of the same ground-truth state (independent sentences, pairwise triples, entity-centered hyperedge units). Same training objective (predict symbolic effects / judge infeasible action). Across scales, data budgets, ID and OOD test worlds: **hyperedge serialization gives the clearest gains for 0.5B–1.5B models and under distribution shift**; larger models shrink the gap; pairwise triples can match/beat hyperedges in-distribution (exact match), but **hyperedges win OOD fact F1 and small-to-medium-scale trade-offs; highest downstream greedy-planning success**. |
| **Key innovations** | Higher-order (hypergraph) state organization as an inductive bias for learned symbolic world models; shows structured serialization matters most when capacity is limited or test≠train. |
| **arXiv** | [2609.00002](https://arxiv.org/abs/2609.00002) |
| **Why it matters** | A clean, controlled result on *how to feed state to* world-model agents — directly extends the wiki's world-model thread (cf. Twin's write-executable-world-model harness). |

### 5.3 Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement

| Field | Detail |
|-------|--------|
| **Authors** | Haoyang Yan, Min-le Su, Hangfan Zhang, Zhanhao Li, Chen Zhang, Shao Zhang, Yang Chen, Lei Bai, Shuyue Hu |
| **Institution** | Not stated |
| **Submitted** | 2026-09-01 · [2609.01481](https://arxiv.org/abs/2609.01481) · cs.AI |
| **Abstract** | Studies **autonomous software development** (LLM coding agents turn high-level requirements into complete, usable software without human intervention). **Harness-of-Harness (HoH)** organizes existing coding-agent harness executions into iterative planning-coding-testing loops that sustain improvement: balances repair with capability growth, scopes work into small verifiable increments, separates implementation tests from independent evaluation, constrains outputs rather than prescribing agent workflows, exposes deliverables/tools/skills progressively, reuses rather than recreates, and maintains versioned histories. On GameCraft-Bench, FrontierSWE, ProgramBench across three harness-model pairs: **avg +52.25% relative gain over standalone harnesses (max +82.86%) after 3 iterations**. In a 70+-iteration multi-day deployment it autonomously develops a **first-person-shooter game** (coherent storyline, fully implemented core mechanics, human-playable, polished visuals, integrated audio). |
| **Key innovations** | Harness-agnostic accumulation of verifiable increments + progressive skill exposure (builds capability over days, not single shots); reproducible multi-agent compute loop. |
| **arXiv** | [2609.01481](https://arxiv.org/abs/2609.01481) |
| **Why it matters** | Bridges the wiki's games and autonomous-coding threads — and a strong real-world demonstration that long-horizon agent loops with continual improvement outrun single-pass harnesses on game-quality tasks. |

---

## ⑥ Economic Theory & Mechanism Design for AI (1)

### 6.1 Mechanism Design for Alignment and Control

| Field | Detail |
|-------|--------|
| **Authors** | Dirk Bergemann, Andrew Koh, Stephen Morris |
| **Institution** | *(inferred: Yale (Bergemann), MIT (Koh/Morris))* |
| **Submitted** | 2026-09-01 · [2609.01595](https://arxiv.org/abs/2609.01595) · econ.TH / cs.AI / cs.GT |
| **Abstract** | A framework for **mechanism design with AI agents whose alignment (preferences) and capabilities (actions/information) are unknown**; mechanisms must incentivize both honesty and obedience. A **one-sided imitation structure** (capabilities can be concealed but not counterfeited) yields a revelation principle, a characterization of implementable policies via **nested cyclical monotonicity**, and conditions under which eliciting higher-order beliefs disciplines multiple agents. Applied to stylized cases: (i) **sandbagging** (more capable agent pretends to be less); (ii) an **alignment–interpretability trade-off** (substitutes as instruments, complements in value); (iii) **discipline via peer scoring**; (iv) coupling rewards to induce competition among agents; (v) **scalable oversight and reward shaping**. |
| **Key innovations** | Revelation-principle-grade theory for unknown-preference-and-capability AI agents; sandbagging as concealable capability; incentive-compatible scalable oversight. |
| **arXiv** | [2609.01595](https://arxiv.org/abs/2609.01595) |
| **Why it matters** | Grounds the wiki's alignment/oversight thread in formal mechanism design — sandbagging and peer-scoring are exactly the failure modes the wiki's training/evals track (cf. RMC-style reward hacking, "Humanity's Last Exam" concerns). |

---

## ⑦ Honorable mentions

- **Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement** — Yi Ding, Ruqi Zhang · [2608.31046](https://arxiv.org/abs/2608.31046) · cs.LG/cs.CL · 2026-08-31. Analyzes OPD supervision and finds it **noisy (worse with teacher scale) yet the student is insensitive to it**; gains come from suppressing **low log-probability tokens**, achievable with a fixed negative advantage — no teacher needed. Introduces **On-Policy Self-Adaptation (OPSA)**, supervisor-free entropy-adaptive negative advantages: Qwen3-1.7B **+35.41 points Avg@32 on AIME24 (263% relative), doubles Pass@32** across three benchmarks, and beats OPD by 16.77 Avg@32 points. Directly relevant to the wiki's distillation/RLVR thread — a provocative "does distillation even distill?" result.
- **WorldBench: Culturally Grounded Benchmark for Multilingual Agents** — Leonardo Ranaldi, Sherrie Shen, Jushi Kai, Alexandra Birch · [2609.01056](https://arxiv.org/abs/2609.01056) · cs.AI · 2026-09-01 (from new-listing scan). Persona-grounded everyday workflows across 7 languages and 8 cultures; frontier models reach only ~49.2% Constrained Task Success, with large gaps between correctness and environment preservation. Adds an agent-evaluation-quality dimension to the wiki's eval thread.

---

## Synthesis notes & links

- **Cross-cutting theme (generative recommendation, production-grade):** This wave is the strongest yet for the generative-paradigm bet: Tencent's TGR ships GenRank→GenRec→Reason at hundreds-of-millions scale with ad-revenue numbers (#1.2); ReST scales *behavior sequences* rec-natively in production ads ranking (#1.1); CoGR goes fully generative on both sides of retrieval (#1.4). The prior report's question "how do we get to end-to-end generation in production?" now has three different answered deployments.
- **Cross-cutting theme (simulators before real feedback):** Three papers use learned simulation to avoid online/real-world cost: WMG-RL's user-engagement world model for RL rewards (#2.2), persona-conditioned A/B pre-screening (#3.3), and the mechanism-design framing of oversight as incentives (#6.1). Together they push the wiki's "test/reward before real exposure" idea from robotics/agents into recommender and experimentation systems.
- **Cross-cutting theme (scaling isn't free / listen to the evidence):** ReST shows LLM-style transformer blocks *saturate* on rec sequences and need rec-native designs (#1.1); One-Policy-Is-Enough removes tree search AND learned critics entirely (#4.3); OPD's teacher is noisy yet disposable (HM #7); RPCBench finds an overthinking penalty for critique (#3.1). Consistent caution against blindly stacking compute.
- **Cross-cutting theme (economically-grounded AI control):** Bergemann/Koh/Morris (#6.1) gives formal teeth to the alignment/sandbagging/peer-scoring problems the wiki's training+evals pages describe empirically.
- Related wiki pages this extends: the ongoing [arxiv-daily](arxiv-daily.md) digest line, [[ctr-scaling-landscape]], [[technical-roadmap]], and prior-day [arxiv-ai-search (2026-09-01)](../2026-09-01/arxiv-ai-search.md).

---

## Appendix — full arXiv listing

| # | arXiv ID | Title | Category |
|---|----------|-------|----------|
| 1.1 | [2609.01240](https://arxiv.org/abs/2609.01240) | ReST (sequence-transformers ranking) | cs.IR |
| 1.2 | [2609.00986](https://arxiv.org/abs/2609.00986) | TGR (Tencent Generative Recommendation) | cs.IR |
| 1.3 | [2609.00913](https://arxiv.org/abs/2609.00913) | SwapRec | cs.IR |
| 1.4 | [2609.00638](https://arxiv.org/abs/2609.00638) | CoGR (co-evolving generative retriever) | cs.IR/CL |
| 2.1 | [2609.00165](https://arxiv.org/abs/2609.00165) | TS-SSM (two-sided SSM) | cs.IR |
| 2.2 | [2609.01067](https://arxiv.org/abs/2609.01067) | WMG-RL (world-model-guided rec RL) | cs.IR |
| 2.3 | [2609.00618](https://arxiv.org/abs/2609.00618) | DREAMS (MCTS conversational rec) | cs.IR/AI |
| 2.4 | [2609.00251](https://arxiv.org/abs/2609.00251) | HypReflect (continual personalization) | cs.AI |
| 3.1 | [2609.00918](https://arxiv.org/abs/2609.00918) | RPCBench (premise critique) | cs.AI/CL |
| 3.2 | [2609.00248](https://arxiv.org/abs/2609.00248) | Authority bias in conversational search | cs.AI |
| 3.3 | [2609.01038](https://arxiv.org/abs/2609.01038) | Persona A/B test simulation | cs.AI |
| 4.1 | [2609.01058](https://arxiv.org/abs/2609.01058) | ARISE-RL | cs.AI |
| 4.2 | [2609.01045](https://arxiv.org/abs/2609.01045) | AgentFactory | cs.AI |
| 4.3 | [2608.30952](https://arxiv.org/abs/2608.30952) | One Policy Is Enough | cs.LG/CL |
| 5.1 | [2609.01057](https://arxiv.org/abs/2609.01057) | CM-PTM (mobile games behavior pretraining) | cs.AI |
| 5.2 | [2609.00002](https://arxiv.org/abs/2609.00002) | HyperWorld (hypergraph world models) | cs.AI |
| 5.3 | [2609.01481](https://arxiv.org/abs/2609.01481) | Harness-of-Harness | cs.AI |
| 6.1 | [2609.01595](https://arxiv.org/abs/2609.01595) | Mechanism Design for Alignment and Control | econ.TH |
| HM | [2608.31046](https://arxiv.org/abs/2608.31046) | Does OPD Really Distill / OPSA | cs.LG/CL |
| HM | [2609.01056](https://arxiv.org/abs/2609.01056) | WorldBench | cs.AI |