---
title: "arXiv AI Research Roundup — June 30, 2026"
type: synthesis
created: 2026-06-30
updated: 2026-06-30
sources: []
tags: [arxiv, llm, recommendation, ctr, sequential-modeling, rl, agents, survey]
---

# arXiv AI Research Roundup — June 30, 2026

Curated recent papers across LLMs, recommendation systems, CTR prediction, sequential modeling, RL, and AI agents.

---

## LLMs & Reasoning

### 1. TACO: Tool-Augmented Credit Optimization for Agentic Tool Use
- **Link:** [2606.30251](https://arxiv.org/abs/2606.30251)
- **Authors:** Mingkuan Feng, Jinyang Wu, Hao Gu, Fangrui Lv, Ruihan Jin, Chuyuan Zhang, Zhengqi Wen, Jianhua Tao
- **Institution:** N/A
- **Abstract:** Introduces TACO, a GRPO variant for code-tool agents with two coupled advantage channels: Differential Answer-Probe Reward (DAPR) — a self-supervised, judge-free tool-contribution advantage — and Outcome-Gated Advantage Routing (OGAR). Trained via two-stage SFT+RL pipeline.
- **Key Innovation:** DAPR reuses the existing answer checker to credit each tool call by its own effect on correctness, robust to probe-hacking; eliminates need for external judge model.

### 2. When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding
- **Link:** [2606.30265](https://arxiv.org/abs/2606.30265)
- **Authors:** Aaryam Sharma
- **Institution:** N/A
- **Abstract:** Develops a theory for greedy decoding, relaxed acceptance rules, and tree-based candidate sets in speculative decoding. Characterizes rejection regions as lower level sets of the target distribution and derives exact KL-divergence certificates.
- **Key Innovation:** First theoretical framework for deterministic local acceptance events in practical inference systems; evaluated on Qwen3 models.

### 3. MCP Server Architecture Patterns for LLM-Integrated Applications
- **Link:** [2606.30317](https://arxiv.org/abs/2606.30317)
- **Authors:** Carson Rodrigues, Oysturn Vas
- **Institution:** ANSYR voice AI platform
- **Abstract:** Catalogues five recurring MCP server architectural patterns (Resource Gateway, Tool Orchestrator, Stateful Session Server, Proxy Aggregator, Domain-Specific Adapter) observed across 15 independently developed servers.
- **Key Innovation:** First structured taxonomy of MCP server patterns in production; quantitative evaluation with inter-rater reliability (Cohen's kappa = 0.76) and tool-count scalability study.

### 4. Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents
- **Link:** [2606.30306](https://arxiv.org/abs/2606.30306)
- **Authors:** Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang
- **Institution:** N/A
- **Abstract:** Survey of 435 works treating always-on agents as persistent-state systems. Analyzes state through six axes: authority, scope, mutability, provenance, recoverability, actionability. Introduces Always-On Evaluation Protocol (AOEP-v0).
- **Key Innovation:** Finds literature concentrates on accumulating/retrieving state but understudies governance, recovery, and relinquishment.

### 5. Dynamo: Dynamic Skill-Tool Evolution for Vision-Language Agents
- **Link:** [2606.30185](https://arxiv.org/abs/2606.30185)
- **Authors:** Yutao Sun, Yanting Miao, Hao-Xuan Ma, Mengyu Zhou, Mingshuai Chen, Tiancheng Zhao, Dexin Wang, Lei Lv, Li Xu, Xiaoxi Jiang, Guanjun Jiang
- **Institution:** N/A
- **Abstract:** Training-free framework that adapts frozen VLMs by evolving reusable reasoning skills and executable visual tools from the agent's own correct/incorrect attempts. Accumulates in a persistent library.
- **Key Innovation:** Closes 65-99% of the RL gap at a fraction of compute; combines additively with RL when available.

### 6. ManimAgent: Self-Evolving Multimodal Agents for Visual Education
- **Link:** [2606.30296](https://arxiv.org/abs/2606.30296)
- **Authors:** Wenjia Jiang, Zongyuan Cai, Yuanhang Shao, Chenru Wang, Boyan Han, Zhixue Song, Keyu Chen, Shengwei An, Xu Yang, Zhou Yang
- **Institution:** N/A
- **Abstract:** Self-evolving agent that writes Manim Python code to render mathematical animations. Uses dual-channel Episodic Memory Bank (positive successes + negative failure patterns) grown entirely from its own task stream.
- **Key Innovation:** Blind human Pass@1 rises and reflection rounds fall as memory grows; no weight updates or human seeds needed.

### 7. MirrorCode: AI Can Rebuild Entire Programs from Behavior Alone
- **Link:** [2606.30182](https://arxiv.org/abs/2606.30182)
- **Authors:** Tom Adamczewski, David Owen, David Rein, Florian Brand, Giles Edkins, Allen Hart, Daniel O'Connell
- **Institution:** Epoch Research
- **Abstract:** Long-horizon coding benchmark where AI agents reimplement entire software projects (25 targets across Unix utils, bioinformatics, interpreters, cryptography, etc.) without source code access. Strongest model scores 56%.
- **Key Innovation:** AI reimplemented gotree (16,000-line bioinformatics toolkit); largest single attempt cost $2,600 over 19 days.

---

## Recommendation Systems

### 8. From Extraction to Navigation: Progressive Retrieval with Indirectly Infinite Depth (IID-Nav)
- **Link:** [2606.29970](https://arxiv.org/abs/2606.29970)
- **Authors:** Linxiao Che, Shanshan Huang, Haitao Lu, Yijia Sun, Qiang Luo, Ruiming Tang, Han Li, Kun Gai, Guorui Zhou
- **Institution:** Kuaishou
- **Abstract:** Frames retrieval as stateful autonomous graph exploration rather than static similarity matching. Introduces goal-aware navigation policy, recursive state evolution with cross-request state reuse (Indirectly Infinite Depth).
- **Key Innovation:** Alleviates "search drift" in billion-scale industrial systems; logical unlimited-depth graph traversal without linearly rising latency.

### 9. POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation
- **Link:** [2606.29946](https://arxiv.org/abs/2606.29946)
- **Authors:** Linxiao Che, Yijia Sun, Siyuan Lou, Shanshan Huang, Qiang Luo, Ruiming Tang, Han Li, Kun Gai
- **Institution:** Kuaishou
- **Abstract:** Real-time sequential modeling framework using partial-order relations from the recommendation cascade (multi-task ranking scores including predicted CTR and watch duration). Deployed on Kuaishou online traffic.
- **Key Innovation:** Partial-order guided sequence construction + multi-objective score fusion; online gains of 0.249% watch time lift on KS Single Page.

### 10. CMSL: Constructive Multi-Sequence Learning for Recommendation Systems
- **Link:** [2606.28533](https://arxiv.org/abs/2606.28533)
- **Authors:** Zikun Cui, Renzhi Wu, Junjie Yang, Li Sheng, Jijie Wei, Linfeng Liu, Tai Guo, Tao Jia, Xiaodong Wang, Hong Li, Li Yu, Sri Reddy, Hong Yan
- **Institution:** Meta
- **Abstract:** Paradigm shift from passive single-sequence ingestion to active "context engineering" that constructs multiple coherent sequences in latent space. Uses learnable Sequence Construction Module + linear attention.
- **Key Innovation:** Deployed across ranking and retrieval tasks on four major surfaces at Meta.

### 11. DeGRe: Dense-supervised Generative Reranking for Recommendation
- **Link:** [2605.25749](https://arxiv.org/abs/2605.25749)
- **Authors:** Chaotian Song, Jingyao Zhang, Chenghao Chen, Zisen Sang, Dehai Zhao, Guodong Cao, Boxi Wu, Deng Cai, Jia Jia
- **Institution:** Taobao / Alibaba
- **Abstract:** Generative reranking framework with offline-online decoupled design. Uses Lookahead Evaluator with beam search to mine high-value sequences, then distills into lightweight Online Generator.
- **Key Innovation:** Accepted to KDD 2026 (ADS Track); deployed on Taobao Flash Shopping.

### 12. Diagnosing and Mitigating Retrieval Bottlenecks in LLM-Based Cold-Start Recommendation
- **Link:** [2606.29947](https://arxiv.org/abs/2606.29947)
- **Authors:** Zhe Dong (U. Maine at Presque Isle), Fang Qin (Stanford), Manish Shah (Independent), Yicheng Wang (Independent)
- **Institution:** University of Maine at Presque Isle, Stanford University
- **Abstract:** Five-domain benchmark separating reranking quality from retrieval coverage. Finds single retrievers place gold item in 200-item pool only 4.6-22.9% of the time. Introduces LHF learned hybrid fusion layer.
- **Key Innovation:** LLM cold-start advantage exists but is largely unreachable in current retrieve-then-rerank pipelines.

### 13. Monosemanticity in Recommender Systems
- **Link:** [2606.29341](https://arxiv.org/abs/2606.29341)
- **Authors:** Yagel Alfasi, Eden Rzezak, Eadan Schechter
- **Institution:** N/A
- **Abstract:** Applies Matryoshka Sparse Autoencoder (MSAE) to matrix factorization embeddings on Amazon Fashion dataset. Reveals hierarchical interpretable structure with gender-associated latent neurons.
- **Key Innovation:** First application of monosemanticity analysis to collaborative filtering embeddings.

### 14. Fairness Attacks on Recommender Systems
- **Link:** [2606.29064](https://arxiv.org/abs/2606.29064)
- **Authors:** Yanan Wang, Yong Ge
- **Institution:** N/A
- **Abstract:** Structure-aware RL-based fairness attack using graph-based encoder and gender selection policy to exacerbate unfairness of target recommender systems.
- **Key Innovation:** First dedicated study of fairness attacks on recommender systems.

### 15. Fast and Feasible: Permutation-based Constrained Reranking for Revenue Maximization
- **Link:** [2606.28059](https://arxiv.org/abs/2606.28059)
- **Authors:** Svetlana Shirokovskikh, Anastasiia Soboleva, Ekaterina Solodneva, Aleksandr Katrutsa, Roman Loginov, Egor Samosvat
- **Institution:** N/A (large classified platform)
- **Abstract:** Lightweight PermR algorithm for reranking to maximize revenue subject to per-query constraints. Achieves ~63% of ILP revenue improvement within production latency limits.
- **Key Innovation:** 14-day online A/B test over 56M search queries increased revenue by 2%.

---

## CTR Prediction & Advertising

### 16. Selective Test-Time Compute Scaling for CTR Prediction via Uncertainty-Triggered Feature Path Exploration
- **Link:** [2605.24989](https://arxiv.org/abs/2605.24989)
- **Authors:** Moyu Zhang, Yun Chen, Yujun Jin, Jinxin Hu, Yu Zhang, Xiaoyi Zeng
- **Institution:** N/A
- **Abstract:** Training-free model-agnostic framework (UTTSI) that scales inference depth per-instance uncertainty. Combines model logit confidence with data-level frequency prior. 7-day online A/B test confirms 5.3% relative CTR gain.
- **Key Innovation:** First application of test-time compute scaling to industrial CTR prediction.

### 17. Self-Balancing Gradient Allocation for Heterogeneity-Aware Feature Generation in CTR Prediction
- **Link:** [2605.24986](https://arxiv.org/abs/2605.24986)
- **Authors:** Moyu Zhang, Yun Chen, Yujun Jin, Jinxin Hu, Yu Zhang, Xiaoyi Zeng
- **Institution:** N/A
- **Abstract:** HeteGenCTR resolves generative difficulty imbalance via per-field learnable difficulty parameters. Self-balancing loss + difficulty-guided attention. Consistent gains on 5 CTR benchmarks + 7-day online A/B test.
- **Key Innovation:** Disproportionate gains for cold-start and long-tail users.

### 18. AdaGRPO: Adaptive Loss Balancing for Noise-Robust GRPO in Generative Recommendation
- **Link:** [2606.08480](https://arxiv.org/abs/2606.08480)
- **Authors:** Kewei Xu, Junbo Qi, Yanyan Zou, Pengfei Zhang, Xingzhi Yao, Shengjie Li
- **Institution:** N/A
- **Abstract:** GRPO gated by per-sample diagnostics (policy difficulty + reward discriminability). Unsure samples default to supervised NLL. Production A/B tests show statistically significant CTR and dwell time gains.
- **Key Innovation:** First application of GRPO to generative recommendation with per-instance gating.

### 19. Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes?
- **Link:** [2605.31036](https://arxiv.org/abs/2605.31036)
- **Authors:** Ashwinkumar Badanidiyuru
- **Institution:** N/A
- **Abstract:** Studies interaction between pCTR/pCVR model quality, auction format, and autobidder behavior. First-price auctions with uniform bidding guarantee revenue monotonicity for tCPA bidders; second-price and budgets break it.
- **Key Innovation:** Accepted at ICML 2026; formal definition of model improvement via cluster refinement.

### 20. EMA-FS: Accelerating GBDT Training via Gain-Informed Feature Screening
- **Link:** [2606.26337](https://arxiv.org/abs/2606.26337)
- **Authors:** Yan Song
- **Institution:** N/A
- **Abstract:** Algorithm-level optimization maintaining EMA of per-feature split gains across boosting iterations. Restricts histogram construction to top-K features. Up to 2.61x speedup on dense data with AUC improvement.
- **Key Innovation:** Informed feature screening (vs. random subsampling); ~120 lines of C++ across all six LightGBM tree learners.

### 21. Representation Curriculum: Stagewise Training for Robust Ranking and Allocation
- **Link:** [2606.09891](https://arxiv.org/abs/2606.09891)
- **Authors:** Ehsan Ebrahimzadeh, Sina Baharlouei, Abraham Bagherjeiran
- **Institution:** N/A
- **Abstract:** Training-time intervention that stages feature utilization — foregrounds content-based merit signals first, then introduces exposure-dependent belief signals. Closed-form solutions in Gaussian linear ridge setting.
- **Key Innovation:** Measurably shifts reliance from historical belief signals toward content-based merit; validated in large-scale e-commerce search A/B test.

---

## Sequential Modeling

### 22. POEM (see #9 above)
Real-time sequential modeling using partial-order relations from ranking cascade. Kuaishou. [2606.29946](https://arxiv.org/abs/2606.29946)

### 23. CMSL (see #10 above)
Constructive Multi-Sequence Learning disentangling user history into thematic strands. Meta. [2606.28533](https://arxiv.org/abs/2606.28533)

---

## Reinforcement Learning, World Models & Games

### 24. DreamForge-World 0.1 Preview: A Low-Compute Real-Time Controllable World Model
- **Link:** [2606.30292](https://arxiv.org/abs/2606.30292)
- **Authors:** Daniyel Ayupov, Artur Markov-Tsoy
- **Institution:** N/A
- **Abstract:** Preview foundational world model for real-time interactive simulation. Supports live keyboard/mouse control, multimodal initialization, mid-stream reprompting, 14-15 FPS at 480p on single RTX 4090.
- **Key Innovation:** Low-compute route toward consumer-GPU world models; residual action pathway from Matrix-Game family.

### 25. Toward an Energy-Optimized Operation of Data Centers in Wind Farms Using RL
- **Link:** [2606.30316](https://arxiv.org/abs/2606.30316)
- **Authors:** Jan Stenner, Alexander Kilian, Sebastian Peitz, Hermann de Meer
- **Institution:** N/A
- **Abstract:** RL as online controller for curtailment-aware workload shifting in wind-turbine-integrated HPC data centers. PPO and SAC variant with on-policy update achieve strong empirical performance.
- **Key Innovation:** Imitation Learning and Reward Shaping solve credit-assignment problem; reproducible fixed-day simulation framework.

### 26. Exploration and Online Transfer with Behavioral Foundation Models
- **Link:** [2606.29980](https://arxiv.org/abs/2606.29980)
- **Authors:** Louis Bagot (SyCoSMA), Mathieu Lefort (LIRIS, SyCoSMA, IRISA), Laëtitia Matignon (SyCoSMA)
- **Institution:** SyCoSMA, LIRIS, IRISA, UR
- **Abstract:** Extends zero-shot RL transfer to online setting where reward is observed through trial-and-error. Frames as bandit-like exploration-exploitation using BFM-generated exploration policies.
- **Key Innovation:** Derives UCB-inspired formulation; exploration via eigenvalue minimization of uncertainty matrix.

### 27. Behavioral Foundation Models for Zero-Shot RL Transfer
- **Link:** [2606.30191](https://arxiv.org/abs/2606.30191)
- **Authors:** Haoliang Han
- **Institution:** N/A
- **Abstract:** Shows agency-gated slow credit produces durable behavioral residue on spiking neural substrates. Self-preserving behavior survives episodic buffer removal (retained fraction 0.96).
- **Key Innovation:** Formalizes "operational behavioral self"; multiplicative veto prevents forgetting across 8 sequential tasks with no replay buffer.

---

## Graph Learning & Multimodal

### 28. PromptGNN-sim: Deep Fusion and Alignment of GNN and LLMs for Text-Attributed Graph Learning
- **Link:** [2606.30291](https://arxiv.org/abs/2606.30291)
- **Authors:** Zhifei Hu, Alexandra I. Cristea
- **Institution:** N/A
- **Abstract:** Bi-directional structure-semantic fusion framework. GAT for semantically aware neighborhood selection + structure-aware prompts for LLM. Bi-directional cross-modal contrastive learning + cross-attention.
- **Key Innovation:** Outperforms classical GNNs, LLMs, and recent GNN-LLM fusion methods on six public datasets.

### 29. BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language
- **Link:** [2606.30319](https://arxiv.org/abs/2606.30319)
- **Authors:** Haitao Wu, Qirui Zhang, Zhouheng Yao, Shangquan Sun, Qihao Zheng, Mianxin Liu, Chi Zhang, Wanli Ouyang, Chunfeng Song, Changqing Zhang, Jiamin Wu
- **Institution:** N/A
- **Abstract:** First unified brain model integrating brain, vision, and language. Unified Brain Tokenizer + All-in-One autoregressive architecture for any-to-any generation (image/text to brain and vice versa).
- **Key Innovation:** Accepted at ICML 2026; zero-shot generalization with interpretable biological topography.

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| LLMs & Reasoning | 7 |
| Recommendation Systems | 8 |
| CTR Prediction & Advertising | 6 |
| Sequential Modeling | 2 |
| RL / World Models / Games | 4 |
| Graph Learning & Multimodal | 2 |
| **Total** | **29** |

### Notable Trends

1. **LLMs for recommendation** is a hot area — cold-start, reranking, and generative approaches all active.
2. **Test-time compute scaling** entering CTR prediction (UTTSI paper).
3. **GRPO variants** emerging for generative recommendation (AdaGRPO, TACO).
4. **Multi-sequence / partial-order modeling** replacing single-chronological-sequence paradigm (CMSL at Meta, POEM at Kuaishou).
5. **World models** becoming practical on consumer GPUs (DreamForge-World).
6. **MCP server architecture** formalized as a research area.
7. **Fairness attacks** on recommenders gaining attention.
