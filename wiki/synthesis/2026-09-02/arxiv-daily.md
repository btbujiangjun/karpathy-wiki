---
title: "arXiv Daily — 2026-09-02: LLM-Agent Self-Evolving Recommenders (CoVeMem / YouTube Gemini Loop), CADET Decoder-Only Ads CTR, Transition-Aware Graph Sequential Modeling, RLVR Weak-Model Exploration, Game AI with RL"
type: synthesis
created: 2026-09-02
updated: 2026-09-02
tags: [arxiv, daily, llm, agents, recommendation, agentic-recommender, ctr, advertising, sequential-modeling, e-commerce, graph-attention, rlvr, rl, reasoning, games, game-ai, ranking, counterfactual, daily-digest]
---

# arXiv Daily — 2026-09-02

Cross-topic digest of recent arXiv papers spanning LLMs/agents, recommendation, advertising/CTR, sequential user-behavior modeling, efficiency-oriented graph modeling, and game AI. Covers the late-August → early-September 2026 submission wave.

> **Note on method & sources:** Papers compiled via live web search of arXiv abs/list pages. Affiliations marked *(stated)* come from paper front matter or author ties; *(inferred)* = deduced from author identities/company affiliation (e.g. YouTube, LinkedIn, WeChat Pay); otherwise "not stated". All IDs are linked to their arXiv abstract pages.

---

## ① LLM Agents & Self-Evolving / Agentic Recommendation (3)

### 1.1 Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt |
| **Institution** | Google / YouTube *(inferred: production launches at YouTube named in abstract)* |
| **Submitted** | 2026-02-10 (rev. 2026-08-02) · [2602.10226](https://arxiv.org/abs/2602.10226) · cs.LG (RecSys 2026) |
| **Abstract** | Optimizing large-scale ML systems such as recommendations for global video platforms requires navigating a massive hyperparameter space and, more critically, designing sophisticated optimizers, architectures, and reward functions to capture nuanced user behavior. The authors propose a **self-evolving system** using LLMs (Google Gemini family) as specialized Machine Learning Engineers (MLEs) to autonomously generate, train, and deploy complex model changes in an end-to-end automated workflow. It consists of an **Offline Agent (Fast Loop)** for high-throughput hypothesis generation optimized against proxy metrics, and an **Online Agent (Slow Loop)** that validates candidates against delayed north-star business metrics in live production. |
| **Key innovations** | LLM agents acting as MLEs (not just hyperparameter tuners) — discovering novel optimizer improvements, architecture changes, and reward functions targeting long-term engagement; two-loop Offline/Online validation against proxy vs. delayed business metrics; demonstrated via several successful production launches at YouTube. |
| **Why it matters** | A landmark industrial validation that autonomous LLM-driven model evolution can beat traditional engineering workflows in both development velocity and performance — directly extends the wiki's agentic/LLM-in-recommendation thread. |

### 1.2 When Memory Takes Gradients: Collaborative Vector Memory for Agentic Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Hanchong Chen, Xing Tang, Lingjie Li, Xiongfeng Shan, Xiuqiang He |
| **Institution** | Not stated (industrial agentic-recommender group) |
| **Submitted** | 2026-08-27 · [2608.26895](https://arxiv.org/abs/2608.26895) · cs.IR |
| **Abstract** | Agentic recommender systems ground each LLM decision in persistent user memory, which in existing agents is *text* — a narrative maintained by further LLM calls. Text limits memory: it is rewritten one piece at a time (exploiting full interaction history is expensive), and collaborative evidence (graded catalog-wide similarity) does not survive translation into sentences. **CoVeMem** vectorizes the collaborative core of agent memory: frozen LightGCN user/item states form a memory bank; at each decision the candidate set retrieves relevant historical states which enter the LLM context as *soft tokens* alongside a light textual profile. Contrastive alignment to item-semantic anchors plus listwise co-training with masked candidates teaches the model to read and rank through these states. |
| **Key innovations** | Replaces text memory with a gradient-friendly collaborative vector memory; requires **zero extra LLM calls** for memory maintenance (vs. per-interaction calls for text memory); matches/exceeds the strongest collaborative text-memory agent on 19/20 metric cells across four benchmarks. |
| **Why it matters** | Directly challenges the text-memory assumption in agentic recommenders — key for the wiki's agentic-recommender & memory-design tracking. |

### 1.3 Stageboost: Recommending Signals Based on Counterfactual Estimation

| Field | Detail |
|-------|--------|
| **Authors** | Darpan Singhal, Matan Mandelbrod, Tal Franji, Manasa Kolla, Vipul Gaba, Yuri Brovman |
| **Institution** | eBay *(inferred)* |
| **Submitted** | 2026-08-27 · [2608.27366](https://arxiv.org/abs/2608.27366) · cs.IR (Consequences 2026) |
| **Abstract** | Signals are short textual/visual snippets displayed on the eBay View-Item (VI) page giving contextual info about a viewed item, aiming to facilitate purchase and incentivize engagement. The authors present a **2-stage XGBoost-based model** that optimally populates the VI page with signals, selecting/ranking based on counterfactual estimation of their effect. |
| **Key innovations** | Counterfactual-based signal selection/ranking; two-stage XGBoost; sparse/e-commerce surface optimization. Online: +0.08% overall GMB and +0.58% Parts & Accessories GMB, driven largely by conversion lift on high-average-price items. |
| **Why it matters** | A practical example of counterfactual estimation applied to page-layout/signal ranking in e-commerce — adjacent to the wiki's causal-inference-in-ranking line. |

---

## ② Advertising / CTR — Industrial Deployment (2)

### 2.1 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, ... Fedor Borisyuk, Ruoyan Wang, et al. |
| **Institution** | LinkedIn *(stated: deployed on LinkedIn's advertising platform)* |
| **Submitted** | 2026-02-11 (rev. 2026-08-10) · [2602.11410](https://arxiv.org/abs/2602.11410) · cs.LG (AdKDD 2026) |
| **Abstract** | CTR prediction is foundational to online advertising. DLRMs with explicit feature interactions have long dominated, but recent generative recommenders show promise in content recommendation. Adapting transformer architectures to *ads* CTR carries unique challenges: handling post-scoring contextual signals, maintaining offline-online consistency, and scaling to industrial workloads. **CADET** is an end-to-end decoder-only transformer for ads CTR deployed at LinkedIn, combining self-gated attention, timestamp-based RoPE, and session-aware masking to stabilize training and ensure offline-online consistency; production techniques (packing, chunking, custom Flash Attention kernel) enable scalable training and low-latency serving. Optimized with a RankNet-style pairwise loss and context-conditioned prediction heads with auxiliary tasks. |
| **Key innovations** | First unified generative-decoder ads CTR model replacing a DLRM ensemble; context-conditioned heads + auxiliary tasks + pairwise loss; self-gated attention + timestamp RoPE for post-scoring context handling. Online: **+11.04% CTR lift** over the production LiRank baseline (hybrid DCNv2 + sequential encoders), serving main traffic for homefeed sponsored updates. |
| **Why it matters** | A strong industrial counterpart to the wiki's generative-recommender/CTR line — evidence that a single decoder can outperform a multi-component DLRM ensemble at scale. |

### 2.2 Quantizing Intent: Cross-Domain Semantic IDs from Organic Activity for Industrial Ranking

| Field | Detail |
|-------|--------|
| **Authors** | (see arXiv page) |
| **Institution** | Not stated (industrial ranking, cross-domain) |
| **Submitted** | 2026-05-31 (rev. 2026-06) · [2606.01396](https://arxiv.org/abs/2606.01396) · cs.IR |
| **Abstract** | Proposes deriving **cross-domain semantic IDs** by quantizing user intent from organic activity, used as item/user representations for industrial ranking — connecting Id-less/generative recommendations with semantic-ID quantization for cross-domain transfer. |
| **Key innovations** | Semantic-ID quantization from organic signals for ranking; cross-domain representation reuse. |
| **Why it matters** | Fits the wiki's semantic-ID / generative-recommender thread (cross-domain intent quantization for industrial ranking). |

---

## ③ Sequential User-Behavior Modeling & Efficiency (2)

### 3.1 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network for E-Commerce Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Hanqi Jin, Gaoming Yang, et al. |
| **Institution** | Not stated (deployed in large-scale industrial production) |
| **Submitted** | 2026-01-21 · [2601.14955](https://arxiv.org/abs/2601.14955) · cs.AI (WWW 2026 short) |
| **Abstract** | Transitions between user behaviors carry key signals about evolving preferences, motivating multi-behavior sequential modeling. Prior transformer-based approaches have polynomial complexity, limiting use in large-scale industrial systems with long user sequences. **TGA** is a linear-complexity approach that constructs a structured sparse graph of informative transitions from three perspectives — item-level, category-level, and neighbor-level transitions — then applies a transition-aware graph attention mechanism that jointly models user-item interactions and behavior-transition types. |
| **Key innovations** | Linear-complexity multi-behavior modeling (vs. polynomial transformers); sparse structured transition graph (item/category/neighbor levels); transition-aware attention jointly modeling interactions + transition types; industrial deployment with strong business-metric gains. |
| **Why it matters** | Direct contribution to the wiki's sequential-modeling/feature-interaction corpus — an efficiency-first answer to "how to handle long multi-behavior sequences." |

### 3.2 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang |
| **Institution** | Not stated |
| **Submitted** | 2026-06-13 · [2606.15252](https://arxiv.org/abs/2606.15252) · cs.IR |
| **Abstract** | User behavior sequence modeling is central to modern CTR prediction. Most work exploits *positive* signals (clicks/purchases) while ignoring the rich information in *implicit negative* behaviors (impressions without clicks, skips, dwell-time signals). This work unlocks implicit negative behaviors to enrich sequence modeling. |
| **Key innovations** | Uses implicit negatives (not just positives) as learning signal for sequential user modeling; relevant to CTR prediction pipelines. |
| **Why it matters** | Complements the wiki's sequential-modeling/CTR line by challenging the positive-only assumption in behavior sequences. |

---

## ④ LLM Training & Reasoning — RLVR (1)

### 4.1 Boosting LLM Exploration via Weak-Model Guidance in RLVR

| Field | Detail |
|-------|--------|
| **Authors** | Xingyu Shen, Huishuai Zhang, Peng Li, Yinchun Wang, Dongyan Zhao |
| **Institution** | Not stated (academic; Dongyan Zhao — Peking University group) |
| **Submitted** | 2026-08-27 · [2608.27420](https://arxiv.org/abs/2608.27420) · cs.CL |
| **Abstract** | RLVR (Reinforcement Learning with Verifiable Rewards) markedly improves LLM reasoning but often collapses policy entropy, narrowing reasoning coverage and degrading pass@k for large k. Existing fixes use algorithmic regularization; the authors instead exploit **cross-model non-parametric perturbation**: force the target model to generate answers from *partial reasoning trajectories produced by a smaller, weaker model*. These unfamiliar prefixes disrupt over-confidence and encourage exploration of distinct reasoning paths. |
| **Key innovations** | Weak-model guided exploration (outer prefixes) to fight entropy collapse in RLVR; no extra SFT, reward design, or prompting; gains grow with k (expanded reasoning coverage); explains impact of distributional discrepancy on exploration dynamics. |
| **Why it matters** | A lightweight alternative to regularization-based diversity preservation — relevant to the wiki's RLVR/post-training tracking. |

---

## ⑤ Game AI & Reinforcement Learning (1)

### 5.1 Augmenting Game AI with Deep Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén |
| **Institution** | Electronic Arts (EA), Stockholm, Sweden *(stated)* |
| **Submitted** | 2026-06-18 · [2606.20210](https://arxiv.org/abs/2606.20210) · cs.AI (Conference on Games 2026, vision paper) |
| **Abstract** | Immersion in video games depends heavily on believable in-game characters (NPCs), which hand-coded systems struggle to produce. RL can create more authentic, adaptive, immersive NPCs by learning from interaction with the game or from player data. However, current research limitations block broad deployment across game genres. The authors propose a framework for training RL models with game-development-specific requirements in mind, present game examples with RL-augmented game AI, describe the practicalities of deploying player-facing ML agents in modern games, and identify bottlenecks and hard problems. Key requirements include **short training time** (games in active development change daily). |
| **Key innovations** | Vision/framework paper for production game AI (not just superhuman play); requirement set tailorable to game production; candid survey of deployment bottlenecks (training time, drift, plasticity loss); grounded in recent RLRL examples (AlphaStar, GT Sophy, game testing). |
| **Why it matters** | Shifts the wiki's game-AI thread from "RL that beats humans" toward "RL-augmented NPCs in commercial production" — a distinct, deployment-focused perspective. |

---

## Honorable Mentions

- **Understanding Large Language Models** — Yannik Keller, Thomas Eisenmann · [2607.01006](https://arxiv.org/abs/2607.01006) · cs.CL. Survey chapter on emergent LLM capabilities and their mechanistic implementation in processing layers (symbolic reasoning, theory of mind, deception).
- **How Language Models Organize and Structure Moral Knowledge** — Orion Reblitz-Richardson · [2608.27402](https://arxiv.org/abs/2608.27402) · cs.CL. Linear-probe study showing LLM moral-foundation directions span near-maximal independent dimensions with a shared positive component; geometry emerges early in pre-training; moral-dilemma directions partially compose from component foundations.
- **PANTHER: Generative Pretraining Beyond Language for Sequential User Behavior Modeling** — Guilin Li, et al. · [2510.10102](https://arxiv.org/abs/2510.10102) · cs.LG. Extends generative pretraining to user behavior; deployed at WeChat Pay with +25.6% next-transaction HitRate@1 and +38.6% fraud-recall improvement; structured tokenization + sequence pattern recognition.
- **D3ER: Multi-Modal Recommendation via Disentangle and Distillation-based Dynamic Ensemble** — Bingnan Wang, et al. · [2608.25737](https://arxiv.org/abs/2608.25737) · cs.IR (ACMMM 2026).
- **Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings and Temporal Neighbor Sampling** — Maksim Utushkin, et al. · [2608.27413](https://arxiv.org/abs/2608.27413) · cs.IR (CIKM 2026).

---

## Cross-Topic Observations

1. **Agents are now optimizing the recommender itself.** [1.1] (YouTube) and [1.2] (CoVeMem) both push LLM involvement past classic ranking — one as self-evolving MLEs, the other replacing text memory with gradient-bearing vector memory. This is a coherent maturation of the "LLM × recommendation" thread: from content generation → to ranking → to meta-optimization.
2. **Decoder-only generative CTR is production-real.** [2.1] CADET (+11.04% CTR lift at LinkedIn) is a direct industrial rebuttal to "DLRM ensembles are required for ads"; pairs thematically with [3.1]'s efficiency-driven graph alternative and the semantic-ID work [2.2].
3. **Diversity/entropy is the new RLVR bottleneck.** [4.1] attacks pass@k collapse via weak-model perturbations — a non-regularization route to exploration that complements regularization-based fixes.
4. **Sequential modeling keeps moving toward efficiency + richer signals.** [3.1] linear-complexity graph attention and [3.2] implicit-negative exploitation both target the same scalability/signal-coverage gap.
5. **Game AI discourse is shifting to production NPCs.** [5.1] reframes RL in games from superhuman play to deployment of player-facing NPCs — with training-time, drift, and plasticity as the operative constraints.
