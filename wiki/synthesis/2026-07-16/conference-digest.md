---
title: "Top ML/AI Conference & arXiv Paper Digest"
type: synthesis
created: 2026-07-16
updated: 2026-07-16
sources: [arxiv, conference proceedings]
tags: [icml-2026, iclr-2026, neurips-2025, aaai-2026, kdd-2026, cvpr-2026, acl-2026, sigir-2026, recsys-2025, recommendation, ctr, llm, agent, code-generation]
---

# Top ML/AI Conference & arXiv Paper Digest (2026-07-16)

This digest covers recent papers from top ML/AI conferences and arXiv, organized by venue and category.

---

## 1. ICML 2026

**Conference Stats**: 23,918 submissions → 6,352 accepted (26.6%), 536 spotlights

### 1.1 Outstanding Paper Awards

#### The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **Authors**: Zanlin Ni et al.
- **Affiliation**: [Not specified in search results]
- **Venue**: ICML 2026 (Outstanding Paper Award)
- **Key Innovation**: Reveals that for general reasoning tasks (math, coding), arbitrary order generation in diffusion LLMs (dLLMs) may limit reasoning potential. dLLMs tend to bypass high-uncertainty tokens crucial for exploration. Proposes JustGRPO: simply forgoing arbitrary order and applying standard GRPO achieves 89.1% on GSM8K while retaining parallel decoding.
- **arXiv**: https://icml.cc/virtual/2026/poster/61998

#### High-accuracy Sampling for Diffusion Models and Log-concave Distributions
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: ICML 2026 (Outstanding Paper Award)
- **Key Innovation**: Achieves δ-error in polylog(1/δ) steps with Õ(δ)-accurate score estimates—exponential improvement over all prior results. Under minimal data assumptions: Õ(d·polylog(1/δ)) complexity; with intrinsic dimension d*: Õ(d*·polylog(1/δ)).
- **arXiv**: https://icml.cc/virtual/2026/poster/65132

### 1.2 Agent & RL Systems

#### From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory (MemoPilot)
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: ICML 2026
- **Key Innovation**: Plug-in memory copilot that trains memory update process using multi-turn GRPO. Introduces turn-wise reward signal and context-independent advantage estimation. Achieves #1 Elo on Rock-Paper-Scissors (1590) and Limit Texas Hold'em (1762), outperforming DeepSeek-V3.2.
- **arXiv**: https://pubdb.com/paper/2606.08656

#### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: ICML 2026
- **Key Innovation**: Addresses dynamics shifts in RL through geometry lens. Proves target-domain regret controlled by smoothness of trajectory dynamics encoder. Method significantly outperforms baselines under severe dynamics failures.
- **Link**: https://openreview.net/forum?id=XQLa5PVQ0D

### 1.3 Diffusion Models

#### Why Diffusion Models Don't Memorize
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard
- **Affiliation**: [Not specified]
- **Venue**: NeurIPS 2025 (Best Paper Award)
- **Key Innovation**: Studies implicit dynamical regularization in diffusion model training that prevents memorization.

---

## 2. NeurIPS 2025

**Conference Stats**: 20,000 submissions → 5,772 accepted (25%), 87 orals, 739 spotlights

### 2.1 Best Paper Awards

#### Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: Alibaba (Qwen Team)
- **Venue**: NeurIPS 2025 (Best Paper Award)
- **Key Innovation**: First to systematically examine how attention gating affects LLM performance and training. Introduces non-linearity, sparsity, and attention-sink-free properties to attention mechanisms.
- **Impact**: 146 Alibaba papers accepted at NeurIPS 2025.

#### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Affiliation**: [Not specified]
- **Venue**: NeurIPS 2025 (Best Paper Award)
- **Key Innovation**: Demonstrates that scaling depth in self-supervised RL enables new goal-reaching capabilities.

#### Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: [Not specified]
- **Venue**: NeurIPS 2025 (Best Paper Award)
- **Key Innovation**: Studies homogeneity in language models and its implications.

#### Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **Authors**: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang
- **Affiliation**: [Not specified]
- **Venue**: NeurIPS 2025 (Runner-Up)
- **Key Innovation**: Critical analysis of whether RL truly enhances LLM reasoning beyond base model capabilities.

#### Superposition Yields Robust Neural Scaling
- **Authors**: Yizhou Liu, Ziming Liu, Jeff Gore
- **Affiliation**: [Not specified]
- **Venue**: NeurIPS 2025 (Runner-Up)
- **Key Innovation**: Shows that superposition in neural networks yields robust scaling properties.

---

## 3. AAAI 2026

**Conference Stats**: ~29,000 submissions → 4,167 accepted (17.6%)

### 3.1 LLM Reasoning & Safety

#### AURA: Affordance-Understanding and Risk-aware Alignment Technique for Large Language Models
- **Authors**: Adak, Chatterjee, Banerjee, Hazra, Aditya, Mukherjee
- **Affiliation**: [Not specified]
- **Venue**: AAAI 2026 (Special Track on AI Alignment)
- **Key Innovation**: Multi-layered framework using Process Reward Models (PRMs) for step-level evaluations across logical coherence and safety-awareness. Combines introspective self-critique, fine-grained PRM assessments, and adaptive safety-aware decoding.

#### In-Token Rationality Optimization (InTRO): Towards Accurate and Concise LLM Reasoning via Self-Feedback
- **Authors**: Zhu, Liu, Fu, Wang, Zhang
- **Affiliation**: [Not specified]
- **Venue**: AAAI 2026
- **Key Innovation**: Enables token-level exploration and self-feedback for accurate/concise reasoning. Uses correction factors (token-wise importance weights) estimated by information discrepancy. Achieves up to 20% relative improvement on math-reasoning benchmarks.

#### DEPO: Dual-Efficiency Preference Optimization for LLM Agents
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: AAAI 2026
- **Key Innovation**: Addresses efficiency in LLM agent optimization through dual-efficiency preference optimization.

#### MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: AAAI 2026
- **Key Innovation**: Intent-driven memory selection mechanism for multi-session LLM agents.

### 3.2 RAG & Knowledge

#### PathRAG: Pruning Graph-based Retrieval Augmented Generation with Relational Paths
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: AAAI 2026
- **Key Innovation**: Prunes graph-based RAG using relational paths for more efficient retrieval.

#### DCTR: Dual-Constraint Subgraph Optimization for Knowledge Graph-based RAG
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: AAAI 2026
- **Key Innovation**: Dual-constraint optimization for knowledge graph-based retrieval augmented generation.

---

## 4. ICLR 2026

**Conference Stats**: 19,525 submissions → 5,355 accepted (27.4%)

### 4.1 Key Themes
- Neural compression of 3D meshes
- Belief control as a key principle for building robust LLM agents
- Extrapolation from self-training for image generation
- Compositional diffusion with guided search

---

## 5. CVPR 2026

**Conference Stats**: 16,092 submissions → 4,089 accepted (~25%)

### 5.1 Best Paper Awards

#### SAM 3D: 3Dfy Anything in Images
- **Authors**: Jianing Yang, Georgia Gkioxari, Anushka Sagar, Aohan Lin, Bowen Song, Bowen Zhang, Fu-Jen Chu, Hao Tang et al.
- **Affiliation**: [Multiple institutions]
- **Venue**: CVPR 2026 (Best Paper Award)
- **Key Innovation**: Extends SAM to 3D understanding from images.

#### Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco et al.
- **Affiliation**: [Multiple institutions]
- **Venue**: CVPR 2026 (Best Paper Award)
- **Key Innovation**: Dynamic scene reconstruction method.

#### B³-Seg: Camera-Free, Training-Free 3DGS Segmentation
- **Authors**: Hiromichi Kamata, Samuel Arthur Munro, Fuminori Homma
- **Affiliation**: [Not specified]
- **Venue**: CVPR 2026 (Best Paper Award)
- **Key Innovation**: 3D Gaussian Splatting segmentation without cameras or training.

### 5.2 Vision-Language Models

#### Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding
- **Authors**: Christopher Clark, Jieyu Zhang, Zixian Ma et al.
- **Affiliation**: [Multiple institutions]
- **Venue**: CVPR 2026 (Oral)
- **Key Innovation**: Open-source VLM with video understanding and grounding capabilities.

#### TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment
- **Authors**: Bingyi Cao, Koert Chen et al.
- **Affiliation**: [Not specified]
- **Venue**: CVPR 2026
- **Key Innovation**: Enhanced patch-text alignment for VLP.

### 5.3 Gaming & Agents

#### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Collaborative team (NVIDIA, Stanford, Caltech, UChicago, UT Austin)
- **Affiliation**: NVIDIA, Stanford University, California Institute of Technology, University of Chicago, University of Texas at Austin
- **Venue**: CVPR 2026 (Award Candidate)
- **Key Innovation**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Strong competence across diverse gaming domains.

---

## 6. KDD 2026

**Conference**: Jeju Island, Korea, August 9-13, 2026

### 6.1 Recommendation Systems

#### SPiKE: Semantic Profiles into Knowledge Graphs for Enhanced Recommendation
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: KDD 2026
- **Key Innovation**: Hybrid knowledge base combining structured user-item interactions with KG relations and textual metadata. Enriches item profiles using LLMs for better recommendation.

#### Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: KDD 2026
- **Key Innovation**: Uses LLMs to enrich semantic profiles in knowledge graphs for recommender systems.

### 6.2 Few-Shot Learning

#### TAROT: Task-Adaptive Refinement of LLM-prior Graphs for Few-shot Tabular Learning
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: KDD 2026
- **Key Innovation**: Uses GPT-4o-mini for generating graph structures, task-adaptive semantic graph refinement for few-shot tabular learning.

---

## 7. SIGIR 2026

**Conference**: Melbourne, Australia, July 20-24, 2026
**Stats**: 656 papers accepted

### 7.1 Agent-Based Search

#### Agentic Search in the Wild: Intents and Trajectory Dynamics from 14M+ Real Search Requests
- **Authors**: Jingjie Ning, João Coelho, Yibo Kong, Yunfan Long, Bruno Martins, João Magalhães, Jamie Callan, Chenyan Xiong
- **Affiliation**: Carnegie Mellon University et al.
- **Venue**: SIGIR 2026
- **Key Innovation**: Large-scale log analysis of agentic search from 14.44M requests. Introduces CTAR metric for evidence traceability. Reveals 90%+ multi-turn sessions have ≤10 steps, 89% inter-step intervals <1 minute.

#### AgentRank: Trajectory-Aware Document Ranking for Autonomous Information Retrieval
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: SIGIR 2026
- **Key Innovation**: Ranking framework that learns document utility for autonomous agents in multi-step tasks.

### 7.2 RAG & Retrieval

#### LTRR: Learning To Rank Retrievers for LLMs
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: SIGIR 2026
- **Key Innovation**: Query routing approach that dynamically selects from a pool of retrievers based on query type. Uses pairwise XGBoost for best results.

#### Revisiting BM25 Feedback Models using HyDE
- **Authors**: Nour Jedidi, Jimmy Lin
- **Affiliation**: University of Waterloo
- **Venue**: SIGIR 2026
- **Key Innovation**: Shows BM25 feedback models (Rocchio, RM3) improve HyDE effectiveness by up to 1.4 points (4.2%) on average.

### 7.3 Conversational Search

#### Improving Ad-hoc Search Effectiveness for Conversational Information Retrieval via Model Merging
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: SIGIR 2026
- **Key Innovation**: Training-free model merging strategy for conversational retrievers. Achieves up to 15% higher NDCG@3 under zero-shot conditions.

---

## 8. ACL 2026

**Conference**: San Diego, California, July 2-7, 2026

### 8.1 Agent Systems

#### SOAR: Supervision from Observation for Agentic Reinforcement Learning
- **Authors**: Meng Li, Lei Li, Xiting Wang, Yi Yuan, Zheng Wei, Brucebian, Zang Li
- **Affiliation**: [Not specified]
- **Venue**: ACL 2026
- **Key Innovation**: Assigns positive advantages to observation tokens proportional to negative entropy of preceding actions. Improves performance up to 7.0% on reasoning tasks and 16.9% on deep research tasks.

#### KARL: Reinforcement Learning for LLM Agents on Multi-Turn Knowledge-Intensive Agentic Tasks
- **Authors**: Xueqiao Sun, Xiao Liu, Bowen Lv et al.
- **Affiliation**: Tsinghua University (THUDM)
- **Venue**: ACL 2026
- **Key Innovation**: Online RL with curiosity-driven reward shaping for knowledge exploration. Qwen2.5-14B agent outperforms GPT-4o, Claude-4, and o4-mini on knowledge graph and database tasks.

#### HSCodeComp: A Realistic and Expert-level Benchmark for Deep Search Agents (Best Resource Paper)
- **Authors**: Alibaba team
- **Affiliation**: Alibaba
- **Venue**: ACL 2026 (Best Resource Paper Award)
- **Key Innovation**: First expert-level benchmark for deep search agents on hierarchical rule application. Best agent achieves 49.4% vs human 95.0%. Alibaba's Qwen agent ranks #1 at 65.0%.

### 8.2 LLM Robustness

#### Robertha: Eigenspectrum Regularized Attention for Robust Natural Language Understanding
- **Authors**: Andreia Podasca, Anup Das
- **Affiliation**: [Not specified]
- **Venue**: ACL 2026
- **Key Innovation**: Attention mechanism based on Modern Hopfield Networks with Eigenspectrum Regularization. Significantly outperforms existing robustness methods across 13 GLUE/SuperGLUE tasks.

### 8.3 Structured Inference

#### Adaptive Constraint Propagation via Meta-Reinforcement Learning (MetaJuLS)
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: ACL 2026
- **Key Innovation**: Meta-learned constraint propagation schedules for LLM constrained decoding. Achieves 1.5-2.0× speedups over GPU-optimized baselines while maintaining accuracy.

---

## 9. EMNLP 2025

**Conference**: Suzhou, China, November 4-9, 2025

### 9.1 Industry Applications
- Bloomberg AI published 7 papers covering NLP, LLMs, retrieval-augmented language models, QA, and information extraction.

---

## 10. RecSys 2025

**Conference**: Prague, Czech Republic, September 22-26, 2025

### 10.1 Generative Recommendation

#### Semantic IDs for Joint Generative Search and Recommendation
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: RecSys 2025
- **Key Innovation**: Investigates Semantic ID construction for unified search+recommendation. Shows bi-encoder fine-tuned on both tasks provides effective trade-off. Challenges conventional wisdom that per-task IDs are optimal.

### 10.2 LLM-Enhanced Recommendation

#### LSVCR: Enhancing Sequential Recommender with LLMs for Joint Video and Comment Recommendation
- **Authors**: [Not specified]
- **Affiliation**: Kuaishou
- **Venue**: RecSys 2025
- **Key Innovation**: Two-stage training paradigm combining SR model with supplemental LLM. Online A/B testing on Kuaishou shows 4.13% cumulative gain in comment watch time.

#### LLM-RecG: Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: RecSys 2025
- **Key Innovation**: Addresses domain semantic bias in LLMs for cross-domain recommendations using generalization losses.

---

## 11. CIKM 2025

**Conference**: Seoul, Korea, November 10-14, 2025

### 11.1 Knowledge Management
- Over 800 papers accepted
- Topics: LLMs, efficient knowledge graphs, medical knowledge graphs
- Traceable Drug Recommendation over Medical Knowledge Graphs (MediKS)

---

## 12. WWW 2026

**Conference**: Dubai, UAE

### 12.1 Time-of-Award

#### Test of Time Award: LINE: Large-scale Information Network Embedding
- **Authors**: Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, Qiaozhu Mei
- **Affiliation**: BioGeometry (Tang), University of Michigan
- **Key Innovation**: Graph embedding method that preserves first-order and second-order proximity. Widely adopted in industry for large-scale network analysis.

---

## 13. arXiv Recent Papers

### 13.1 CTR Prediction & Advertising

#### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: [Not specified]
- **Affiliation**: Major social-media platform (industrial dataset)
- **Venue**: arXiv 2026
- **Key Innovation**: Dual-path inter-layer connector for CTR Transformers. Identity residual path + Block Attention Residual path with SiLU gate. Outperforms 12 baselines including OneTrans, TokenMixer-Large, UniMixer. +0.32% AUC on industrial dataset (331M interactions). Fits steeper compute-AUC scaling law (γ=0.118 vs 0.071 for OneTrans).

#### EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling
- **Authors**: Mingyang Liu et al.
- **Affiliation**: Alibaba (Taobao)
- **Venue**: arXiv 2026
- **Key Innovation**: Fully unified modeling without lossy aggregation. Lightweight Cross Attention + Content Sparse Attention. Deployed on Taobao: +3.27% RPM, +1.22% CTR. Shows stable power-law scaling relationship.

#### OneRanker: Unified Generation and Ranking in Industrial Advertising
- **Authors**: [Not specified]
- **Affiliation**: Tencent (Weixin Channels)
- **Venue**: arXiv 2026
- **Key Innovation**: End-to-end generative advertising framework. Value-aware multi-task decoupling architecture. Deployed on Tencent Weixin: GMV-Normal +1.34%, Costs +0.72%.

#### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Generates semantic interest cohorts as explicit intent representations. Hierarchical candidate-aware network injects contextual signal into ranking stage.

#### RankUp: Towards High-rank Representations for Large Scale Advertising
- **Authors**: Jin Chen et al.
- **Affiliation**: Tencent (Weixin Video Accounts, Official Accounts, Moments)
- **Venue**: arXiv 2026
- **Key Innovation**: Mitigates representation collapse through randomized permutation splitting. Deployed across Weixin: GMV +3.41% (Video), +4.81% (Official), +2.12% (Moments).

#### UniSID: End-to-End Semantic ID Generation for Generative Advertisement Recommendation
- **Authors**: Jie Jiang et al.
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Jointly optimizes embeddings and SIDs end-to-end. Multi-granularity contrastive learning. Up to 4.62% improvement in Hit Rate.

#### CADET: Context-Conditioned Ads CTR Prediction with a Decoder
- **Authors**: David Pardoe et al.
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Context-conditioned CTR prediction using decoder architecture.

#### IDProxy: Cold-Start CTR Prediction for Ads and Recommendation
- **Authors**: Yubin Zhang et al.
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Addresses cold-start CTR prediction when item ID embeddings are unavailable.

### 13.2 LLM Agent Systems

#### STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Proposes normalized entropy to decouple state complexity from agent confidence. Hierarchical group-based RL framework with trajectory-aware reward and trajectory-independent penalty. State-of-the-art on ALFWorld, WebShop, Search-Augmented QA.

#### Next-Generation Agentic RL Systems Enable Self-Evolving Agents (AReaL2.0)
- **Authors**: Ran Yan et al.
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Argues self-evolving agents need standardized agent trajectory data protocol, enterprise-grade data proxy, and unified agent evolution control plane. Proposes AReaL2.0 architecture.

#### Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Formalizes harness operation as Harness MDP. Lightweight controller selects structural execution actions while LLM executor remains frozen. Improves verification behavior across six domains.

#### Continual Learning in LLM Agents Without Gradient Updates (JitRL)
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Training-free framework enabling test-time policy optimization without gradient updates.

### 13.3 Code Generation & Execution

#### Self-Execution Simulation Improves Coding Models
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Combines SFT on natural language execution traces with RL using verifiable rewards. Introduces self-verification and self-fixing through simulated test execution. Up to 43% improvement on CruxEval, 39% on competitive programming.

#### DUET: Dual Execution for Test Output Prediction
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: ACL 2026 (Findings)
- **Key Innovation**: Combines direct code execution and LLM-based pseudocode execution via functional majority voting. +13.6 pp improvement on LiveCodeBench.

#### Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Black-box uncertainty quantification using Von Neumann entropy of semantic interaction graphs. Spearman's correlation up to -0.98 with functional correctness.

#### EAGER: Executing as You Generate
- **Authors**: Zhensu Sun et al.
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Parallel execution paradigm that starts executing code while later tokens are being generated. Reduces non-overlapped execution time by up to 99.8%, end-to-end latency by up to 37.3%.

#### CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation
- **Authors**: Zaoyu Chen et al.
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Benchmark for executable behavioral specifications. Best model achieves only 20.2% pass rate on repository-level tasks.

#### IndustryCode: A Benchmark for Industry Code Generation
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: First comprehensive benchmark spanning multiple industrial domains (finance, automation, aerospace) and languages (MATLAB, Python, C++, Stata). Claude 4.5 Opus achieves 68.1% on sub-problems.

#### EvoCodeBench: A Human-Performance Benchmark for Self-Evolving LLM-Driven Coding Systems
- **Authors**: [Not specified]
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2026
- **Key Innovation**: Evaluates inference-time self-evolution with multi-language support. Tracks performance dynamics, efficiency metrics, and human-referenced comparison.

#### CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction
- **Authors**: Jun Gao et al.
- **Affiliation**: Zhejiang University, CUHK, CSIRO, Fudan, Yale
- **Venue**: ACL 2026 (Findings)
- **Key Innovation**: Evaluates implementation invariance and process transparency. Reveals "superficial execution" where models produce correct outputs without correct intermediate reasoning.

### 13.4 Recommendation Systems

#### End-to-End Personalization: Unifying Recommender Systems with LLMs
- **Authors**: Danial Ebrat et al.
- **Affiliation**: [Not specified]
- **Venue**: arXiv 2025
- **Key Innovation**: Combines GATs with LLMs. LLM enriches user/item representations, GAT processes bipartite graph, LLM reranks and generates justifications. Outperforms baselines on MovieLens.

---

## 14. Key Trends & Insights

### 14.1 Scaling Laws
- CTR prediction models now follow power-law scaling (EST, DeRes)
- Diffusion models achieve exponential sampling improvements
- Self-supervised RL benefits from scaling depth

### 14.2 Agent Systems
- Shift from static to self-evolving agents (AReaL2.0)
- Trajectory-aware RL for long-horizon tasks (STAPO)
- Memory-based learning for test-time improvement (MemoPilot)
- Knowledge-augmented RL for proactive exploration (KARL)

### 14.3 Code Generation
- Self-execution simulation enables verification without external tools
- Dual execution strategies (code + pseudocode) improve reliability
- Repository-level code generation remains challenging (20% pass rate)
- Industry-specific benchmarks emerging

### 14.4 CTR & Advertising
- Unified generation+ranking architectures (OneRanker)
- End-to-end semantic ID generation (UniSID)
- High-rank representations for better expressiveness (RankUp)
- Industrial deployment shows consistent gains (+1-4% GMV)

### 14.5 Attention Mechanisms
- Gated attention wins NeurIPS 2025 Best Paper
- Attention sinking addressed in new architectures
- Sparse attention patterns for efficiency

---

*Generated: 2026-07-16*
