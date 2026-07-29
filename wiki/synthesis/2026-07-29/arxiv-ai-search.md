---
title: "arXiv AI Research Search — 2026-07-29"
type: synthesis
created: 2026-07-29
updated: 2026-07-29
tags: [arxiv, survey, llm, recommendation, ctr, advertising, sequential-modeling, games]
---

# arXiv AI Research Search — 2026-07-29

Coverage spanning LLMs, recommendation systems, CTR prediction, advertising, sequential modeling, and games. Drawn from cs.AI, cs.LG, cs.IR, and cs.CL recent submissions (Jul 23–29, 2026).

---

## 1. LLM Reasoning & Test-Time Compute

### When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling
- **Authors**: — (ACL 2026 Findings)
- **Institution**: —
- **Link**: [aclanthology.org](https://aclanthology.org/2026.findings-acl.1199/)
- **Abstract**: Challenges the assumption that longer reasoning chains always yield better results. Systematically investigates the marginal utility of additional reasoning tokens, showing diminishing and even negative returns beyond a threshold ("overthinking").
- **Key Innovation**: Formalizes the overthinking phenomenon in test-time compute scaling; provides diagnostic metrics to identify when extended thinking degrades accuracy.

### Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL
- **Authors**: Jiabao Ji, Yujian Liu, Li An, Rohit Jain, Gungor Polatkan, Siyu Zhu, Shiyu Chang
- **Institution**: —
- **Link**: [arXiv:2607.25816](https://arxiv.org/abs/2607.25816)
- **Abstract**: Trains an LLM agent to speculate about its next tool call while reasoning. Joint RL over agent + speculator yields faster tool invocation without sacrificing accuracy.
- **Key Innovation**: Speculative tool-call prediction as a parallel decoding task; joint RL training for agent-speculator coordination.

### LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Authors**: — (Jul 2026)
- **Institution**: —
- **Link**: [arXiv (via deeppaper.ai)](https://arxiv.deeppaper.ai/papers/weekly)
- **Abstract**: Identifies verification (determining correctness of a solution) as a new scaling axis. Proposes a training-free framework that computes fine-grained, expressive feedback for agentic tasks.
- **Key Innovation**: Verification as a third scaling axis (beyond pre-training and post-training); fine-grained feedback without additional model training.

### Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks
- **Authors**: Bart Custers, Koorosh Aslansefat
- **Institution**: —
- **Link**: [arXiv:2607.25877](https://arxiv.org/abs/2607.25877)
- **Abstract**: Uses Bayesian Networks to monitor uncertainty in LLM-based multi-agent systems at runtime. Accepted at WAISE 2026.
- **Key Innovation**: Probabilistic safety monitoring for LLM agent swarms; real-time uncertainty estimation without degrading agent performance.

### Bridging Compute- and Data-Optimal Pretraining
- **Authors**: Tian Qin, Kimia Hamidieh, David Alvarez-Melis
- **Institution**: —
- **Link**: [arXiv:2607.25271](https://arxiv.org/abs/2607.25271)
- **Abstract**: Unifies compute-optimal and data-optimal pretraining regimes. Proposes a framework to jointly optimize over compute budget and data quality/quantity.
- **Key Innovation**: Joint optimization of data and compute scaling laws; practical recipes for allocating budget under constrained resources.

---

## 2. Recommendation Systems (Generative, Sequential, LLM4Rec)

### Tokens are All You Need: Dual-purpose Semantic IDs for Achieving LLM-Level I/O Efficiency
- **Authors**: Baolei Li, Yiping Yuan, Yilin Zheng, Likang Yin, Ling Liu, Fabio Soldo, Romer Rosales, Xinyang Yi, Lichan Hong
- **Institution**: — (RecSys 2026)
- **Link**: [arXiv:2607.24865](https://arxiv.org/abs/2607.24865)
- **Abstract**: Proposes dual-purpose semantic IDs that serve both as item identifiers and as feature representations, eliminating the need for separate embeddings in LLM-based recommenders.
- **Key Innovation**: Unified semantic ID tokenization; bridges the I/O gap between LLM training and recommendation serving.

### Memory Layer: Train the In-Model Cache for Recommendation Models
- **Authors**: Liangyuan Na, Gufan Yin, Yixin Bao, Xianjie Chen, Justin Lin, Ziheng Huang et al.
- **Institution**: —
- **Link**: [arXiv:2607.25110](https://arxiv.org/abs/2607.25110)
- **Abstract**: Introduces a trainable in-model memory cache that stores and retrieves user-item interaction patterns, reducing latency and improving personalization.
- **Key Innovation**: Differentiable memory cache integrated into the recommendation model graph; end-to-end training with cache updates.

### Sharpness-aware Model Merging with Salience Recovery for LLM-based Cross-Domain Sequential Recommendation
- **Authors**: Huwei Ji, Jiajie Su, Yuyuan Li, Xiaohua Feng, Chaochao Chen
- **Institution**: — (KDD '26)
- **Link**: [arXiv:2607.25366](https://arxiv.org/abs/2607.25366)
- **Abstract**: Merges domain-specific LLM adapters for cross-domain sequential recommendation using sharpness-aware optimization and salience recovery.
- **Key Innovation**: Sharpness-aware merging prevents knowledge interference across domains; salience recovery preserves domain-specific signals.

### Reward Guided Decoding for Generative Recommendation
- **Authors**: Ruochen Yang, Yusheng Huang, Youfeng Zheng, Shuang Wen et al.
- **Institution**: —
- **Link**: [arXiv:2607.25344](https://arxiv.org/abs/2607.25344)
- **Abstract**: Applies reward-guided decoding (analogous to RL-based text generation) to generative recommendation, steering the autoregressive item generation toward higher-quality results.
- **Key Innovation**: Inference-time reward optimization for generative recommenders; no additional training required for the reward model.

### VaLiDRec: Variable-Length LLM-Aligned Semantic IDs for Generative Recommendation
- **Authors**: Shutong Qiao, Wei Yuan, Tong Chen, Hao Wang, Quoc Viet Hung Nguyen, Hongzhi Yin
- **Institution**: —
- **Link**: [arXiv:2607.25209](https://arxiv.org/abs/2607.25209)
- **Abstract**: Proposes variable-length semantic IDs that adapt code length based on item popularity, improving both recommendation accuracy and efficiency.
- **Key Innovation**: Variable-length code assignment; better utilization of the semantic ID space for long-tail items.

### TopoGR: Revealing and Preserving Latent Structure of Semantic ID in Generative Recommendation
- **Authors**: Ziyu Zheng, Zhengshun Du, Yaming Yang, Bin Tong et al.
- **Institution**: —
- **Link**: [arXiv:2607.25216](https://arxiv.org/abs/2607.25216)
- **Abstract**: Reveals that semantic IDs in generative recommenders encode latent topological structure; proposes methods to preserve this structure during training.
- **Key Innovation**: Topological analysis of semantic ID spaces; structure-preserving regularization for generative recommendation.

### Bumblebee: Interleaved Mixed-Layer Building Blocks for Large-Scale Recommendation Systems
- **Authors**: David Bauer, Cancan Zhang, Wenshun Liu, Xiaoyi Zhang et al.
- **Institution**: —
- **Link**: [arXiv:2607.24804](https://arxiv.org/abs/2607.24804)
- **Abstract**: Proposes interleaved mixed-layer architectures (attention + MLP + cross-attention) as modular building blocks for large-scale recommendation.
- **Key Innovation**: Modular, interleaved architecture design; scales to trillion-parameter recommendation models.

### Hypothesis-Driven Shelf Generation for Personalised Recommendation
- **Authors**: Aleksandr V. Petrov, Tarun Chillara, Matthew D. Moellman et al.
- **Institution**: — (RecSys '26 Industry Track)
- **Link**: [arXiv:2607.25823](https://arxiv.org/abs/2607.25823)
- **Abstract**: Generates personalized "shelves" (themed recommendation groups) by hypothesizing user intents and validating them against behavior.
- **Key Innovation**: Hypothesis-driven shelf generation; explicit intent modeling in recommender presentation.

### A Position Paper on Recommender Systems in the Era of Autonomous Agents
- **Authors**: Aixin Sun
- **Institution**: — (RecSys 2026)
- **Link**: [arXiv:2607.24822](https://arxiv.org/abs/2607.24822)
- **Abstract**: Argues that recommender systems must evolve from reactive item-feeders to proactive agents that negotiate with autonomous user agents.
- **Key Innovation**: New research agenda for agent-agent recommendation protocols.

### Grevo: A Unified Generative Recommendation Framework with Evolutionary Item Indexing
- **Authors**: Huanjie Wang, Liwei Guan, Zekai Sun, Hongwei Zhang, Honghui Bao
- **Institution**: —
- **Link**: [arXiv:2607.25329](https://arxiv.org/abs/2607.25329)
- **Abstract**: Combines generative recommendation with evolutionary item indexing that adapts to shifting item distributions over time.
- **Key Innovation**: Evolutionary index updates for non-stationary item catalogs.

### SPARC: Sequence-aware Progressive Attribute Routing and Compression Framework for Generative Recommendation
- **Authors**: Chang Liu, Changfa Wu, Hui Qian, Binbin Cao et al.
- **Institution**: —
- **Link**: [arXiv:2607.25339](https://arxiv.org/abs/2607.25339)
- **Abstract**: Routes and compresses attribute information progressively through the generative recommendation decoder, attending to sequence context.
- **Key Innovation**: Sequence-aware attribute routing; progressive compression reduces generation cost.

---

## 3. CTR Prediction & Advertising

### TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction in Online Advertising
- **Authors**: Kaiyuan Li, Kun Wang, Zhongbo Wang, Teng Sha, Ming Yan, Yanhua Cheng, Xialong Liu
- **Institution**: —
- **Link**: [arXiv:2607.25404](https://arxiv.org/abs/2607.25404)
- **Abstract**: Proposes a dual-timescale learning framework with two clocks (short-term click window, long-term conversion window) for delayed conversion prediction.
- **Key Innovation**: Explicit two-clock modeling; decouples click and conversion timing dynamics; practical for industrial ad systems with delayed feedback.

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: A. Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang
- **Institution**: LinkedIn
- **Link**: [arXiv:2602.11410](https://arxiv.org/abs/2602.11410)
- **Abstract**: Adapts decoder-only transformer architecture for ads CTR prediction, handling post-scoring contextual signals and maintaining offline-online consistency. +1.04% CTR lift over DCNv2 + sequential encoder hybrid (LiRank).
- **Key Innovation**: Decoder-only architecture for CTR; deployed on LinkedIn's main sponsored feed traffic.

### Fine-Tuned LLM as a Complementary Predictor Improving Ads System
- **Authors**: A. Wu, Leo Lu, Han Sun, Zhifang Liu
- **Institution**: —
- **Link**: [arXiv:2605.27856](https://arxiv.org/abs/2605.27856)
- **Abstract**: Uses a fine-tuned LLM as an auxiliary predictor alongside a traditional DLRM-based ads system, contributing complementary signals for hard cases.
- **Key Innovation**: Auxiliary LLM predictor in production ads; complementary signal integration.

### Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, W. Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: —
- **Link**: [arXiv:2606.04944](https://arxiv.org/abs/2606.04944)
- **Abstract**: Proposes DS-MLP, a dual-stream MLP architecture that captures explicit and implicit feature interactions simultaneously, competing with transformer-based CTR models.
- **Key Innovation**: Dual-stream MLP design; knowledge distillation from explicit interaction branch to main MLP.

### Generative Recommendation for Large-Scale Advertising (GR4AD)
- **Authors**: Ben Xue, Dan Liu, Lixiang Wang, Mingjie Sun et al.
- **Institution**: Kuaishou
- **Link**: [arXiv:2602.22732](https://arxiv.org/abs/2602.22732)
- **Abstract**: Production-grade generative recommender for ads. Proposes UA-SID tokenization, LazyAR decoder, and VSL+RSPO optimization. Up to 4.2% ad revenue improvement. Deployed at Kuaishou (400M+ users).
- **Key Innovation**: End-to-end generative recommendation for advertising at scale; lazy autoregressive decoding; ranking-guided preference optimization.

### Nudging Sustainable Choices through LLM-Generated Recommendation Explanations
- **Authors**: Haya Halimeh, Dietmar Jannach, Oliver Müller
- **Institution**: —
- **Link**: [arXiv:2607.25726](https://arxiv.org/abs/2607.25726)
- **Abstract**: Uses LLMs to generate recommendation explanations that nudge users toward sustainable choices, studying the interplay between explanation framing and user behavior.
- **Key Innovation**: LLM-generated persuasive explanations for sustainability goals in recommenders.

---

## 4. Sequential Modeling

### Raven: High-Recall Sequence Modeling with Sparse Memory Routing
- **Authors**: Arshia Afzal, Aviv Bick, Eric P. Xing, Volkan Cevher, Albert Gu
- **Institution**: —
- **Link**: [arXiv:2607.25357](https://arxiv.org/abs/2607.25357)
- **Abstract**: A state-space model variant that uses sparse memory routing to achieve high recall on long sequences while maintaining linear complexity.
- **Key Innovation**: Sparse memory routing in SSMs; recall-optimized architecture for ultra-long sequence modeling; extends the Mamba line of work.

### The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers
- **Authors**: Zhe Xu, Prachi Agrawal, Kavosh Asadi et al.
- **Institution**: —
- **Link**: [arXiv:2607.25346](https://arxiv.org/abs/2607.25346)
- **Abstract**: Challenges the prevailing generative retrieval paradigm, showing that discriminative LMs fine-tuned for retrieval match or exceed generative approaches at lower cost.
- **Key Innovation**: Systematic comparison of generative vs discriminative retrieval; practical guidelines for retrieval architecture choice.

### Structure-aware Relative Policy Optimization for Ranking
- **Authors**: Yiteng Tu, Weihang Su, Zitao Su, Yiqun Liu, Min Zhang, Qingyao Ai
- **Institution**: —
- **Link**: [arXiv:2607.25268](https://arxiv.org/abs/2607.25268)
- **Abstract**: Proposes a structure-aware RL method for ranking that accounts for inter-item dependencies via relative policy optimization.
- **Key Innovation**: Structure-aware RL for ranking; relative policy optimization that respects list-level item relationships.

---

## 5. Games & Game Theory

### Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment
- **Authors**: Elias Fernández Domingos, The Anh Han
- **Institution**: —
- **Link**: [arXiv:2607.26034](https://arxiv.org/abs/2607.26034)
- **Abstract**: Uses game-theoretic experiments to show that the perception of falling behind in AI development drives unsafe deployment choices, even when cooperation would yield better collective outcomes.
- **Key Innovation**: Formal game-theoretic model of AI race dynamics; experimental evidence for safety degradation under competitive pressure.

### Engine-Equal, Human-Unequal: A Reproducible Outcome Skew in Engine-Assessed Equal Chess Positions
- **Authors**: Jesung Park
- **Institution**: —
- **Link**: [arXiv:2607.25655](https://arxiv.org/abs/2607.25655)
- **Abstract**: Demonstrates systematic bias in chess engine evaluations of objectively equal positions, where evaluation scores skew depending on piece configurations.
- **Key Innovation**: Reproducible skew analysis; implications for fair AI evaluation in competitive domains.

### The Disruptive Impact of Large Language Models on Capture the Flag Competitions and the Path Toward Fair Play
- **Authors**: Michael Macaulay, Harmony Bouabid, Guo Gen Ang, Sasha Shaw
- **Institution**: —
- **Link**: [arXiv:2607.25425](https://arxiv.org/abs/2607.25425)
- **Abstract**: Analyzes how LLMs disrupt cybersecurity CTF competitions, enabling automated flag capture. Proposes competition rule changes for fair play.
- **Key Innovation**: Empirical study of LLM performance on CTF challenges; framework for human-AI competitive integrity.

---

## 6. Multi-Agent, Agents & Evaluation

### HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs
- **Authors**: Yu Hao, Jinxuan Cai, Qi Zhang, Yawen Li et al.
- **Institution**: —
- **Link**: [arXiv:2607.25853](https://arxiv.org/abs/2607.25853)
- **Abstract**: Builds hierarchical skill graphs for LLM agents, enabling compositional generalization and efficient skill reuse.
- **Key Innovation**: Hierarchical skill decomposition; graph-based skill planning for LLM agents.

### Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation
- **Authors**: Stefan Krsteski, Charlotte Meyer, Guillaume Allegre, Tony O'Halloran, Alexandre Sallinen
- **Institution**: —
- **Link**: [arXiv:2607.25891](https://arxiv.org/abs/2607.25891)
- **Abstract**: A high-resolution corpus spanning multiple agent benchmarks, designed to evaluate agent generalization across tasks.
- **Key Innovation**: Standardized cross-benchmark evaluation suite for LLM agents.

### Distributed Constraint Optimization via Online Learning and Iterative Pricing with Application to Large-Scale Satellite Scheduling
- **Authors**: Itai Zilberstein, Pranav Rajbhandari, Steve Chien, Tuomas Sandholm
- **Institution**: —
- **Link**: [arXiv:2607.25835](https://arxiv.org/abs/2607.25835)
- **Abstract**: Combines online learning with iterative pricing for distributed constraint optimization; scales to satellite scheduling with thousands of constraints.
- **Key Innovation**: Novel integration of online learning with pricing mechanisms for combinatorial optimization.

---

## 7. Recommendation Evaluation & Data

### Ranked by Position: Order Sensitivity as an Exploitable Attack Surface in LLM Listwise Recommenders
- **Authors**: Ge Zhang, Jingru Cheng, Huiyuan Chen
- **Institution**: —
- **Link**: [arXiv:2607.24869](https://arxiv.org/abs/2607.24869)
- **Abstract**: Demonstrates that LLM-based listwise recommenders are highly sensitive to input item order, and this sensitivity can be exploited for adversarial manipulation.
- **Key Innovation**: Identifies position-based attack surface in LLM recommenders; provides defense recommendations.

### On the Convergent Validity of Offline Evaluation Designs for Recommender Systems
- **Authors**: Sushobhan Parajuli, Samira Vaez Barenji, Michael D. Ekstrand
- **Institution**: — (RecSys 2026)
- **Link**: [arXiv:2607.25097](https://arxiv.org/abs/2607.25097)
- **Abstract**: Systematic study of whether different offline evaluation designs converge on the same conclusions, highlighting methodological pitfalls.
- **Key Innovation**: Multi-design evaluation comparison; actionable guidelines for robust offline evaluation.

### KuaiLive-M3: A Multi-Modal, Multi-Domain, and Multi-Feedback Dataset for Live Streaming Recommendation
- **Authors**: Ke Guo, Changle Qu, Jiayaqi Cheng, Xiao Zhang et al.
- **Institution**: Kuaishou
- **Link**: [arXiv:2607.24862](https://arxiv.org/abs/2607.24862)
- **Abstract**: A large-scale public dataset for live streaming recommendation with multi-modal content (video, audio, text) and multi-feedback signals.
- **Key Innovation**: First public multi-modal live streaming recommendation dataset; multiple feedback types (like, share, comment, watch time).

---

## Cross-Cutting Themes

| Theme | Papers |
|-------|--------|
| **Generative Recommendation** | GR4AD, VaLiDRec, TopoGR, Grevo, SPARC, Reward Guided Decoding |
| **Test-Time Compute for Reasoning** | Overthinking, Speculate While You Reason, LLM-as-a-Verifier |
| **LLM Agents & Safety** | HiSkill, Runtime Uncertainty Monitoring, Speculate+Rationale RL |
| **CTR / Advertising** | TWICE, CADET, Fine-Tuned LLM for Ads, DS-MLP, GR4AD |
| **Sequential Modeling** | Raven (SSM), Cross-Domain Seq Rec (Sharpness-aware Merging) |
| **Evaluation & Data** | Messier, Convergent Validity, KuaiLive-M3, Ranked by Position |
| **Game Theory & AI Safety** | AI Race Experiment, Engine-Equal Human-Unequal, CTF Disruption |
