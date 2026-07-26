---
title: arXiv AI/LLM/Recommendation/CTR/Sequential Modeling/Search/Ads/Games Weekly Search
type: synthesis
created: 2026-07-26
updated: 2026-07-26
tags: [arxiv, ai, llm, recommendation, ctr, sequential-modeling, advertising, game-theory, weekly-search]
---

# arXiv AI/LLM/Recommendation/CTR/Sequential Modeling/Search/Ads/Games — Weekly Search (2026-07-26)

## 1. LLM & AI Foundation

### 1.1 KVpop — Key-Value Cache Compression with Predictive Online Pruning
- **Authors:** Not specified in listing
- **Institution/Affiliation:** Not specified
- **Abstract:** KV cache growth is a major bottleneck in autoregressive decoding. KVpop learns a fixed-budget KV eviction policy by directly supervising the keep-or-drop decision, replacing static heuristics that poorly track future token utility.
- **Key Innovation:** Online-learned KV eviction policy that dynamically tracks token utility instead of relying on static heuristic scores.
- **arXiv Link:** [arxiv.org/abs/2607.21519](https://arxiv.org/abs/2607.21519) (see DeepPaper weekly listing)

### 1.2 LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Authors:** Not specified in listing
- **Institution/Affiliation:** Not specified
- **Abstract:** Identifies verification as a new scaling axis for LLMs. Introduces a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training, computing explicit verification beyond standard discrete scoring.
- **Key Innovation:** Treats verification as a new scaling axis alongside pre-training, post-training, and test-time compute; provides continuous feedback rather than discrete scores.
- **arXiv Link:** See DeepPaper weekly listing, Jul 8 2026

### 1.3 Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination
- **Authors:** Runzhe Liu, Biquan Bie, Zihao Wang, Yuchao Ma, Yexin Liu, Xinghai Li, Harry Yang, Wenbo Yang, Jinzhe Cao, Shengyang Tao
- **Institution/Affiliation:** Not specified (likely chemical/scientific computing group)
- **Abstract:** Presents G-Frame, an adaptive multi-agent framework integrating Bayesian and team game principles for automated high-quality data synthesis and model training. The resulting 7B model OmniChem achieves performance parity with GPT-4o mini on custom benchmarks while reducing hallucinations by 79.46%. Validated on molecular design and synthesis planning.
- **Key Innovation:** Game-theoretic multi-agent loop (Bayesian + team games) for structured CoT data synthesis and training; 79% hallucination reduction in a 7B model.
- **arXiv Link:** [arxiv.org/abs/2607.08403](https://arxiv.org/abs/2607.08403)

### 1.4 LLM Detection as an Intervention: Downstream Impact under Strategic User Behavior
- **Authors:** Meena Jagadeesan, Tatsunori Hashimoto, Jon Kleinberg
- **Institution/Affiliation:** Cornell University (Kleinberg), Stanford/Hashimoto group
- **Abstract:** Shows how imperfect LLM detection tools create counterintuitive strategic effects: users may increase LLM usage to evade detection, and introducing a detector can lead to lower output quality despite reducing the detected attribute. Develops a stylized game-theoretic model of user strategic behavior, with empirical validation on arXiv abstracts.
- **Key Innovation:** Game-theoretic analysis of LLM detection as an intervention; reveals "rise-then-fall" pattern for detected attributes and perverse incentives on usage and quality.
- **arXiv Link:** [arxiv.org/abs/2607.19300](https://arxiv.org/abs/2607.19300)

---

## 2. Recommendation Systems

### 2.1 Diffusion Language Model for Recommendation (DLMRec)
- **Authors:** Chengyi Liu, Yongqi Zhou, Junwei Pan, Zhixiang Feng, Chengguo Yin, Haijie Gu, Jie Jiang, Yinghao Liu, Yujuan Ding, Qing Li, Wenqi Fan
- **Institution/Affiliation:** Alibaba (likely, based on Jie Jiang/Yinghao Liu affiliation); university collaborators
- **Abstract:** Proposes DLMRec, a discrete diffusion language model tailored for recommendation, replacing autoregressive generation. Introduces a collaborative-aware stochastic tokenizer, curriculum-driven training strategy, and stability-aware voting mechanism to bridge diffusion modeling with collaborative filtering.
- **Key Innovation:** Discrete diffusion instead of autoregressive decoding for generative recommendation; collaborative-aware tokenizer encodes multi-hop CF signals; curriculum training aligns denoising with preference recovery.
- **arXiv Link:** [arxiv.org/abs/2607.21519](https://arxiv.org/abs/2607.21519)

### 2.2 UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction
- **Authors:** Honghao Li, Xianquan Wang, Zibin Zhang, Yi Zhang, Kangyi Lin, Yiwen Zhang
- **Institution/Affiliation:** Not specified
- **Abstract:** Open benchmark for ranking models unifying sequential modeling and feature interaction. Uses chronological pointwise autoregressive supervision. Benchmarks 15 models on 5 large-scale public datasets (up to 700M instances, sequences >10^5 interactions). Provides PyTorch toolkit with DDP, mixed precision, and attention optimization.
- **Key Innovation:** First open-source benchmark unifying sequential modeling + feature interaction evaluation at industrial scale; reproducible toolkit with efficiency optimizations.
- **arXiv Link:** [arxiv.org/abs/2607.19987](https://arxiv.org/abs/2607.19987)

### 2.3 Topology-Aware Tokenization for Generative Recommendation (TopoTok)
- **Authors:** Yaokun Liu, Yifan Liu, Zhenrui Yue, Gyuseok Lee, Zelin Li, Ruichen Yao, Dong Wang
- **Institution/Affiliation:** University of Notre Dame (Dong Wang group)
- **Abstract:** Addresses topology distortion in item tokenization for generative recommendation. Proposes TopoTok with multi-level distillation (inter-group, intra-group, inter-item) to preserve item relational structure through quantization. Achieves up to 9.42% gain in Recall@5.
- **Key Innovation:** Multi-level distillation scheme that preserves item adjacency relationships through quantization hierarchy; resolves topology distortion bottleneck in generative recommenders.
- **arXiv Link:** [arxiv.org/abs/2607.18600](https://arxiv.org/abs/2607.18600) — Accepted at RecSys 2026

### 2.4 Personalized Recommendation Tool Learning via Autonomous Language Agents (PRTA)
- **Authors:** Mingdai Yang, Zhiwei Liu, Weizhi Zhang, Yibo Wang, Hao Peng, Philip Yu
- **Institution/Affiliation:** University of Illinois Chicago (Philip Yu group)
- **Abstract:** Proposes PRTA, an agent-based recommendation framework where an LLM acts as central planner interacting with multiple recommendation models as tools. LLM handles high-level reasoning and personalized tool selection; traditional models do full-ranking scoring. Uses reflection mechanisms for per-user tool evaluation.
- **Key Innovation:** LLM-as-planner + traditional models as tools architecture; reflection mechanism for personalized tool selection avoids LLM hallucination and context-length issues in full-ranking.
- **arXiv Link:** [arxiv.org/abs/2607.19739](https://arxiv.org/abs/2607.19739) — Accepted at RecSys 2026

### 2.5 Mitigating Matthew Effect: Multi-Hypergraph Boosted Multi-Interest Self-Supervised Learning for Conversational Recommendation (HiCore)
- **Authors:** Yongsen Zheng, Ruilin Xu, Guohua Wang, Liang Lin, Kwok-Yan Lam
- **Institution/Affiliation:** NTU (Kwok-Yan Lam), Sun Yat-sen University (Liang Lin)
- **Abstract:** Addresses the Matthew effect in conversational recommender systems where popular items receive disproportionate attention. Builds item-, entity-, and word-oriented multi-channel hypergraphs to learn multi-level user interests. Achieves state-of-the-art on four CRS datasets.
- **Key Innovation:** Multi-hypergraph architecture capturing item/entity/word-level user interests; self-supervised learning for conversational recommendation; specifically targets popularity bias (Matthew effect) in dynamic CRS feedback loops.
- **arXiv Link:** [arxiv.org/abs/2607.18609](https://arxiv.org/abs/2607.18609)

### 2.6 Cardinality-Decomposed Loss (CDL): Matching Training Objectives to Relation Structure in Heterogeneous Recommendation Graphs
- **Authors:** Parul Maheshwari, Amulya Paruchuri, Yiqing Zou, Alireza Sahami Shirazi, Farhad Farahani, Prakhar Mehrotra
- **Institution/Affiliation:** PayPal (based on author affiliations)
- **Abstract:** Identifies that applying BPR loss uniformly across all relation types in heterogeneous GNN-based recommenders causes attribute embeddings to collapse to near-random geometry — a silent failure invisible to standard ranking metrics. Proposes CDL combining CE and BPR losses according to relation cardinality. Introduces lambda-sweep analysis governed by semantic alignment and topology leakage.
- **Key Innovation:** Cardinality-aware loss design recognizing that one-to-one vs one-to-many relations need different objectives; reveals silent attribute embedding collapse with standard BPR.
- **arXiv Link:** [arxiv.org/abs/2607.20737](https://arxiv.org/abs/2607.20737)

### 2.7 CoSimRec: Measuring Coordinated-Content Penetration in Recommender Feedback Loops
- **Authors:** Nan Li, Jiahong Shao, Jiuyang Lyu
- **Institution/Affiliation:** Texas A&M University
- **Abstract:** Offline agent-based evaluation framework modeling coordinated accounts, dynamic ranking, non-bot responses, and ranking interventions in a closed-loop process. Introduces Algorithmic Penetration Rate (APR) metric family to measure target content's share of non-bot exposure. Shows popularity-based ranking produces significant APR-Lift while random controls show no penetration.
- **Key Innovation:** Closed-loop simulation framework for measuring coordinated content amplification; APR metric for quantifying algorithmic penetration in recommendation feedback loops.
- **arXiv Link:** [arxiv.org/abs/2607.15114](https://arxiv.org/abs/2607.15114)

### 2.8 OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender
- **Authors:** Zhaoqi Zhang, Haolei Pei, Jun Guo, Tianyu Wang, Yufei Feng, Hui Sun, Shaowei Liu, Aixin Sun
- **Institution/Affiliation:** ByteDance (Singapore/Hangzhou), Nanyang Technological University
- **Abstract:** Proposes OneTrans, a unified Transformer backbone performing both user-behavior sequence modeling and feature interaction. Uses a unified tokenizer for sequential and non-sequential attributes, with cross-request KV caching for efficient inference. Achieves 5.68% lift in per-user GMV in online A/B tests at ByteDance.
- **Key Innovation:** Single Transformer backbone unifying sequence modeling and feature interaction (breaking the two-track paradigm); cross-request KV caching for industrial-scale efficiency; 5.68% GMV lift.
- **arXiv Link:** [arxiv.org/abs/2510.26104](https://arxiv.org/abs/2510.26104) — Accepted at WWW 2026

---

## 3. CTR Prediction & Advertising

### 3.1 Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution/Affiliation:** Renmin University of China (JI-Rong Wen / RUCAIBox)
- **Abstract:** Proposes DS-MLP, a dual-stream MLP framework for CTR prediction. Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, while a parallel MLP captures implicit interactions. Designed two alignment strategies for optimizing the dual-stream architecture.
- **Key Innovation:** Demonstrates that a vanilla dual-stream MLP (after distillation) achieves SOTA on CTR benchmarks; eliminates complex feature interaction modules while maintaining performance; addresses imbalance between explicit/implicit modules.
- **arXiv Link:** [arxiv.org/abs/2606.04944](https://arxiv.org/abs/2606.04944) — Accepted at TKDD

### 3.2 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors:** Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu
- **Institution/Affiliation:** Xiaohongshu (Little Red Book)
- **Abstract:** Uses multimodal LLMs to generate proxy embeddings from rich content signals for cold-start CTR prediction. Proxies are explicitly aligned with existing ID embedding space and optimized end-to-end under CTR objectives. Deployed at Xiaohongshu serving hundreds of millions of users daily in Content Feed and Display Ads.
- **Key Innovation:** MLLM-generated proxy embeddings for cold-start CTR; end-to-end alignment with existing ID embedding space; seamless integration into production ranking pipelines; live deployment at massive scale.
- **arXiv Link:** [arxiv.org/abs/2603.01590](https://arxiv.org/abs/2603.01590)

---

## 4. Sequential Modeling

### 4.1 POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation
- **Authors:** Linxiao Che, Yijia Sun, Siyuan Lou, Shanshan Huang, Qiang Luo, Ruiming Tang, Han Li, Kun Gai
- **Institution/Affiliation:** Kuaishou (快手)
- **Abstract:** Real-time sequential modeling framework using partial-order relations from the recommendation cascade. Takes real-time multi-task ranking scores (CTR, watch duration) as supervision to construct dynamic partial-order sequences. Uses hierarchical sample learning with hard negatives and margin-based pairwise loss. Fully deployed on Kuaishou traffic.
- **Key Innovation:** Partial-order sequence construction from upstream ranking scores (not just chronological); multi-objective score fusion into normalized quintuple representation; 0.249% per-user watch time lift on KS Single Page.
- **arXiv Link:** [arxiv.org/abs/2606.29946](https://arxiv.org/abs/2606.29946)

---

## 5. Game Theory & AI

### 5.1 Multi-Agent Strategic Games with LLMs
- **Authors:** Maxim Chupilkin
- **Institution/Affiliation:** Not specified
- **Abstract:** Uses LLMs as experimental subjects in repeated security dilemma games. Extends along multipolarity, finite time horizons, and communication dimensions. Finds systematic patterns: multipolarity increases conflict, finite horizons cause backward-induction unraveling, and communication reduces conflict via signaling. Provides access to agents' private reasoning.
- **Key Innovation:** Methodological framework for using LLMs as game-theoretic experimental subjects; scalable, transparent approach to probing strategic mechanisms; links observable behavior to internal strategic reasoning.
- **arXiv Link:** [arxiv.org/abs/2605.03604](https://arxiv.org/abs/2605.03604)

### 5.2 Stability in Combinatorial Markets with Side Payments
- **Authors:** Alexander Grosz, Chiara Vanoli
- **Institution/Affiliation:** Not specified
- **Abstract:** Extends combinatorial market models with explicit side payments among subsets of agents, capturing financial collusion. Establishes systematic classification of expressive power across market orders. Shows higher-order markets with side payments between buyers collapse to equivalence; identifies structural separation between second- and third-order settings.
- **Key Innovation:** Extension of combinatorial market models with side payments; systematic collapse results for market expressiveness; generalized T-core stability notion for restricted transferability.
- **arXiv Link:** [arxiv.org/abs/2607.19098](https://arxiv.org/abs/2607.19098) — Accepted at SAGT 2026

### 5.3 Deep Reinforcement Learning to Master the Asymmetric Strategy of Baghchal
- **Authors:** Ranjit Raut, Aarav Subedi, Sagun Rai, Aaryan Shakya, Manoj Shakya
- **Institution/Affiliation:** Not specified (Nepal-based likely)
- **Abstract:** Applies deep RL to learn asymmetric strategies in Baghchal, a traditional Nepali board game with inherently asymmetric roles (tigers vs goats).
- **Key Innovation:** Application of deep RL to a culturally-specific asymmetric board game; demonstrates transfer of modern game-playing techniques to non-standard game structures.
- **arXiv Link:** [arxiv.org/abs/2607.18296](https://arxiv.org/abs/2607.18296)

### 5.4 LLM Detection as an Intervention (see Section 1.4 above)
- Cross-listed as cs.GT — game-theoretic analysis of LLM detection tools.
- **arXiv Link:** [arxiv.org/abs/2607.19300](https://arxiv.org/abs/2607.19300)

---

## 6. Cross-Cutting Observations

### Key Trends This Week

1. **Generative Recommendation Maturity:** Diffusion models (DLMRec) and tokenization advances (TopoTok) are pushing generative recommendation beyond simple autoregressive paradigms, addressing topology distortion and sequential bias.

2. **Unified Architectures Win:** OneTrans (ByteDance, WWW 2026) and UniRank both advocate for unifying sequence modeling and feature interaction rather than optimizing them separately — with concrete industrial gains (5.68% GMV lift).

3. **LLM-as-Tool, Not LLM-as-Ranker:** PRTA (RecSys 2026) and IDProxy (Xiaohongshu) both use LLMs for reasoning/tool selection/proxy generation while relying on traditional models for full-ranking — a pragmatic pattern for industrial deployment.

4. **Game Theory × AI Convergence:** Multiple papers apply game-theoretic frameworks to AI problems (G-Frame for hallucination reduction, LLM detection strategic behavior, combinatorial market stability, LLM strategic games) — suggesting growing formalization of AI interactions.

5. **Production Validation:** Several papers report online A/B testing results from major platforms (Kuaishou, Xiaohongshu, ByteDance), indicating these methods are moving beyond academic benchmarks into real deployment.

---

*Report generated: 2026-07-26*
