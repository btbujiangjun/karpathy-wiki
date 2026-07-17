---
title: "Top ML/AI Conference & arXiv Paper Digest — Updated 2026-07-17"
type: synthesis
created: 2026-07-17
updated: 2026-07-17
sources: [arxiv, conference-proceedings]
tags: [icml-2026, iclr-2026, neurips-2025, aaai-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, recommendation, ctr, llm, agent, code-generation, games, generative-models, sequential-modeling, benchmark]
---

# Top ML/AI Conference & arXiv Paper Digest — 2026-07-17

> Comprehensive digest covering ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, and recent arXiv papers. Updated July 17, 2026. Total: **180+ papers** across 12+ venues, 20+ labs.

---

## 1. ICML 2026

**Conference Stats**: 23,918 submissions → 6,352 accepted (26.6%), 536 spotlights

### 1.1 Outstanding Paper Awards

#### The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **Authors**: Zanlin Ni et al.
- **Venue**: ICML 2026 (Outstanding Paper Award)
- **Key Innovation**: Reveals that for general reasoning tasks (math, coding), arbitrary order generation in diffusion LLMs may limit reasoning potential. dLLMs tend to bypass high-uncertainty tokens crucial for exploration. Proposes JustGRPO: simply forgoing arbitrary order and applying standard GRPO achieves **89.1% on GSM8K** while retaining parallel decoding.
- **Significance**: Challenges the fundamental assumption of diffusion LMs about unordered generation being beneficial for reasoning. Suggests that the flexibility of arbitrary order is actually a "trap" for tasks requiring structured reasoning.
- **Link**: https://icml.cc/virtual/2026/poster/61998

#### High-accuracy Sampling for Diffusion Models and Log-concave Distributions
- **Venue**: ICML 2026 (Outstanding Paper Award)
- **Key Innovation**: Achieves δ-error in polylog(1/δ) steps with Õ(δ)-accurate score estimates — **exponential improvement** over all prior results. Under minimal data assumptions: Õ(d·polylog(1/δ)) complexity; with intrinsic dimension d*: Õ(d*·polylog(1/δ)).
- **Significance**: Breakthrough in diffusion sampling theory. Makes high-accuracy sampling exponentially cheaper, directly impacting generation quality for image, video, and audio diffusion models.
- **Link**: https://icml.cc/virtual/2026/poster/65132

#### Test of Time Award: A3C (Asynchronous Advantage Actor-Critic)
- **Original Authors**: Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Original Venue**: ICML 2016
- **Significance**: A3C pioneered asynchronous training for deep RL, enabling diverse exploration through multiple parallel agents. Its influence persists in modern distributed RL systems.

### 1.2 Agent & RL Systems

#### MemoPilot: From Player to Master — Enhancing Test-Time Learning via RL over Memory
- **Authors**: [Multiple authors]
- **Venue**: ICML 2026
- **Key Innovation**: Plug-in memory copilot that trains the memory update process using multi-turn GRPO. Introduces turn-wise reward signal and context-independent advantage estimation for long-horizon agent tasks.
- **Results**: Achieves **#1 Elo on Rock-Paper-Scissors (1590)** and **Limit Texas Hold'em (1762)**, outperforming DeepSeek-V3.2.
- **Significance**: Demonstrates that learning how to remember (meta-learning over memory) is more effective than static memory-augmented agents. The memory copilot approach is model-agnostic.
- **arXiv**: https://arxiv.org/abs/2606.08656

#### HiPER: Hierarchical Policy Encoding for Multi-Agent Collaboration
- **Authors**: [Multiple authors]
- **Venue**: ICML 2026
- **Key Innovation**: Hierarchical framework where high-level policy selects sub-policies for long-horizon tasks, low-level executes sub-tasks. Uses curriculum learning for progressive difficulty.
- **Results**: **97.4% success rate on ALFWorld** — state-of-the-art among LLM-based agents.
- **Significance**: Bridges the gap between LLM planning and RL execution. The hierarchical decomposition enables generalization to unseen tasks.

#### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries
- **Venue**: ICML 2026
- **Key Innovation**: Addresses dynamics shifts in RL through a geometry lens. Proves that target-domain regret is controlled by smoothness of trajectory dynamics encoder. Method significantly outperforms baselines under severe dynamics failures.
- **Significance**: When dynamics change (sim-to-real, environment shifts), traditional RL fails. This work provides theoretical grounding and practical method for learning transferable dynamics representations.
- **Link**: https://openreview.net/forum?id=XQLa5PVQ0D

### 1.3 LLM Training & Theory

#### Shannon Scaling Law: LLMs as Noisy Channels
- **Venue**: ICML 2026
- **Key Innovation**: Reformulates LLM pretraining as a noisy channel communication problem. Proposes Shannon Scaling Law that predicts loss as a function of compute, data, and model size — incorporating information-theoretic limits.
- **Significance**: Provides theoretical upper bounds on LLM improvement from scaling alone. Suggests that without better data (higher SNR), scaling alone hits fundamental limits.

#### Self-Supervised Flow Matching (Self-Flow)
- **Venue**: ICML 2026
- **Key Innovation**: Eliminates the need for paired data in flow matching by learning to predict intermediate states between unpaired samples. Self-supervised objective based on optimal transport theory.
- **Significance**: Makes flow matching applicable to domains where paired source-target data is unavailable (e.g., molecular conformations, cross-lingual without parallel data).

#### Complete-muE: MoE Hyperparameter Transfer
- **Venue**: ICML 2026
- **Key Innovation**: Provides theoretical framework for hyperparameter transfer in Mixture-of-Experts models. Shows that optimal hyperparameters for dense models can be transferred to MoE variants via scaling rules.
- **Significance**: Eliminates expensive hyperparameter search for MoE training — critical as MoE becomes the dominant architecture for large-scale models.
- **arXiv**: https://arxiv.org/abs/2605.23893

#### UniAR: Unified Multimodal Autoregressive Modeling
- **Authors**: Alibaba
- **Venue**: ICML 2026
- **Key Innovation**: Unified autoregressive framework handling text, images, video, and audio with a single transformer. Next-token prediction over a unified vocabulary.
- **Significance**: Moves toward truly multimodal foundation models where all modalities share the same autoregressive training paradigm.

### 1.4 Key Trends from ICML 2026
1. **Diffusion LLMs face fundamental questions**: The Flexibility Trap paper questions arbitrary-order generation for reasoning
2. **Memory-augmented RL agents**: Test-time learning and meta-memory are emerging as key paradigms
3. **Theoretical foundations of scaling**: Shannon Scaling Law provides information-theoretic grounding
4. **MoE theory matures**: Hyperparameter transfer, scaling rules for sparse models
5. **Multimodal unification**: Single autoregressive models across all modalities

---

## 2. NeurIPS 2025

**Conference Stats**: 20,000+ submissions → 5,772 accepted (25%), 87 orals, 739 spotlights

### 2.1 Best Paper Awards

#### Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: Alibaba (Qwen Team)
- **Venue**: NeurIPS 2025 (Best Paper Award)
- **Key Innovation**: First systematic examination of how attention gating affects LLM performance. Introduces sigmoid gating after softmax attention, providing: (1) non-linearity for richer expressivity, (2) sparsity induction that automatically suppresses low-value attention connections, (3) elimination of attention sink where models disproportionately attend to initial tokens.
- **Results**: Eliminates attention sink entirely, enables larger learning rates, improves long-context benchmarks.
- **Significance**: Simple architectural modification (minimal added parameters) with profound effects on training stability and long-context capabilities. Alibaba published **146 papers** at NeurIPS 2025.
- **Impact**: Gated attention is being adopted across multiple LLM families post-NeurIPS.

#### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Enables New Goal-Reaching Capabilities
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Venue**: NeurIPS 2025 (Best Paper Award)
- **Key Innovation**: Demonstrates that scaling network depth in self-supervised RL (beyond 1000 layers) enables qualitatively new goal-reaching capabilities that shallow networks cannot achieve, regardless of width.
- **Results**: Deep networks discover hierarchical representations automatically, enabling zero-shot goal generalization.
- **Significance**: Challenges the conventional wisdom that width matters more than depth in RL. Shows depth unlocks emergent hierarchical planning.

#### Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Venue**: NeurIPS 2025 (Best Paper Award)
- **Key Innovation**: Comprehensive study of homogeneity in LLMs — models from different families converge to similar representations and failure modes. Identifies the "hivemind" phenomenon where LLM populations lack diversity.
- **Significance**: Raises critical questions about AI robustness and the value of model diversity. If all models converge to the same biases, ensemble methods offer diminishing returns.

#### Why Diffusion Models Don't Memorize
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard
- **Venue**: NeurIPS 2025 (Best Paper — previously listed under ICML 2026 in some reports, confirmed as NeurIPS)
- **Key Innovation**: Studies implicit dynamical regularization in diffusion model training that prevents memorization. Shows that the diffusion process itself creates a natural regularizer that limits overfitting.
- **Significance**: Theoretically explains why diffusion models generalize well even with massive training sets.

### 2.2 Runner-Up Papers

#### Does RL Really Incentivize Reasoning in LLMs Beyond the Base Model?
- **Authors**: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang
- **Venue**: NeurIPS 2025 (Runner-Up)
- **Key Innovation**: Critical analysis showing RL post-training may not fundamentally improve reasoning — much of the gain comes from format change and calibration rather than genuine reasoning enhancement.
- **Results**: Controlled experiments isolating format effects from reasoning improvements.
- **Significance**: Important cautionary paper for the RL-for-reasoning boom. Suggests that reported gains need careful deconfounding.

#### Superposition Yields Robust Neural Scaling
- **Authors**: Yizhou Liu, Ziming Liu, Jeff Gore
- **Venue**: NeurIPS 2025 (Runner-Up)
- **Key Innovation**: Shows that superposition (models learning more features than dimensions) yields robust scaling — performance continues to improve with more data even beyond the interference threshold.
- **Significance**: Explains the empirical success of overparameterized models through the lens of superposition.

### 2.3 Key Trends from NeurIPS 2025
1. **Attention innovation wins Best Paper**: Gated attention may become standard in next-gen LLMs
2. **RL scaling debate**: Growing recognition that RL gains need careful evaluation
3. **Diffusion theory matures**: Understanding why diffusion works so well
4. **Model diversity concern**: Homogeneity across model families is a systemic risk
5. **Depth scaling in RL**: New capabilities from very deep networks

---

## 3. ICLR 2026

**Conference Stats**: 19,525 submissions → 5,355 accepted (27.4%)

### 3.1 Outstanding Paper Awards

#### Transformers are Inherently Succinct
- **Venue**: ICLR 2026 (Outstanding Paper)
- **Key Innovation**: Proves that transformers can represent any succinct computation (polynomial-time verifiable) with size proportional to circuit complexity rather than brute-force representation. Establishes theoretical connection between transformer depth and circuit depth.
- **Significance**: Provides theoretical justification for why deep transformers outperform shallow ones on complex reasoning tasks.

#### LLMs Lost Multi-Turn Ability After Alignment
- **Venue**: ICLR 2026 (Outstanding Paper)
- **Key Innovation**: Reveals that alignment (RLHF/DPO) degrades multi-turn conversation ability in LLMs. Shows that single-turn reward optimization creates negative transfer to multi-turn settings.
- **Results**: Alignment improves single-turn metrics but causes up to 15% degradation on multi-turn benchmarks.
- **Significance**: Important finding for conversational AI deployment. Suggests that multi-turn specific alignment is necessary.

### 3.2 Honorable Mentions

#### Polar Express: Fast and Exact Training of Diffusion Transformers
- **Venue**: ICLR 2026 (Honorable Mention)
- **Key Innovation**: Training acceleration for diffusion transformers using polar decomposition of attention matrices. Achieves exact (not approximate) training while reducing computation.
- **Significance**: Makes diffusion transformer training practical at scale.

#### Muon Optimizer
- **Venue**: ICLR 2026 (Honorable Mention)
- **Key Innovation**: Optimizer that uses matrix orthonormalization (Newton-Schulz) for gradient updates. Empirically outperforms AdamW across LLM, vision, and diffusion training.
- **Significance**: Muon is becoming a standard optimizer in the post-Adam era. Used in modded-nanoGPT and adopted by multiple labs. Recent work (Muse, arXiv 2607.14536) provides geometric analysis of why Muon works.

#### Mean Flow Policy
- **Venue**: ICLR 2026 (Outstanding)
- **Key Innovation**: Policy optimization based on mean-field flow matching. Maps policy improvement to continuous flow in parameter space.
- **Significance**: Theoretical unification of policy gradient methods and flow-based generative modeling.

### 3.3 Key Themes from ICLR 2026
- Neural compression of 3D meshes
- Belief control as a key principle for building robust LLM agents
- Extrapolation from self-training for image generation
- Compositional diffusion with guided search
- MEM1: Memory-Reasoning Synergy for Long-Horizon Agents (paper: mem1-agent)
- AlphaAlign: RL-based alignment for multi-modal models
- WaltzRL: Dance of RL algorithms for LLM fine-tuning
- Emergent Dexterity from self-supervised RL

---

## 4. AAAI 2026

**Conference Stats**: ~29,000 submissions → 4,167 accepted (17.6%)

### 4.1 LLM Reasoning & Safety

#### AURA: Affordance-Understanding and Risk-aware Alignment
- **Authors**: Adak, Chatterjee, Banerjee, Hazra, Aditya, Mukherjee
- **Venue**: AAAI 2026 (Special Track on AI Alignment)
- **Key Innovation**: Multi-layered framework using Process Reward Models (PRMs) for step-level evaluations across logical coherence and safety-awareness. Combines introspective self-critique, fine-grained PRM assessments, and adaptive safety-aware decoding.
- **Significance**: One of the first comprehensive alignment frameworks addressing both capability and safety in a unified manner.

#### In-Token Rationality Optimization (InTRO)
- **Authors**: Zhu, Liu, Fu, Wang, Zhang
- **Venue**: AAAI 2026
- **Key Innovation**: Enables token-level exploration and self-feedback for accurate/concise reasoning. Uses correction factors (token-wise importance weights) estimated by information discrepancy.
- **Results**: Up to **20% relative improvement** on math-reasoning benchmarks.
- **Significance**: Token-level granularity for reasoning optimization — finer than trajectory-level RL approaches.

#### DEPO: Dual-Efficiency Preference Optimization for LLM Agents
- **Venue**: AAAI 2026
- **Key Innovation**: Addresses efficiency in LLM agent optimization through dual-efficiency preference optimization — optimizing both sample efficiency and computational efficiency.

#### MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents
- **Venue**: AAAI 2026
- **Key Innovation**: Intent-driven memory selection mechanism for multi-session LLM agents. Selectively retrieves and compresses memories based on agent's current intent.

### 4.2 RAG & Knowledge

#### PathRAG: Pruning Graph-based RAG with Relational Paths
- **Venue**: AAAI 2026
- **Key Innovation**: Prunes graph-based RAG using relational paths for more efficient retrieval. Reduces retrieval cost while maintaining or improving answer quality.

#### DCTR: Dual-Constraint Subgraph Optimization for KG-RAG
- **Venue**: AAAI 2026
- **Key Innovation**: Dual-constraint optimization for knowledge graph-based RAG. Balances relevance and diversity in subgraph selection.

### 4.3 Industry Papers from AAAI 2026

#### MoMoREC: Momentum Multimodal Recommendation
- **Affiliation**: Alibaba/Taobao
- **Results**: **+6.3% GMV** on Taobao
- **Key Innovation**: Momentum-based multimodal representation learning for recommendation with temporal dynamics.

#### TreeBridge: LLM-Guided Recommendation
- **Affiliation**: Shopee
- **Results**: **+1.55% GMV** on Shopee
- **Key Innovation**: Tree-structured LLM reasoning for bridging query and item representations.

#### RecCocktail: Ensemble for Recommendation
- **Key Innovation**: Adaptive ensemble of multiple recommendation models, dynamically weighting based on user context.

---

## 5. CVPR 2026

**Conference Stats**: 16,092 submissions → 4,089 accepted (~25%)

### 5.1 Best Paper Awards

#### SAM 3D: 3Dfy Anything in Images
- **Authors**: Jianing Yang, Georgia Gkioxari, Anushka Sagar, Aohan Lin, Bowen Song, Bowen Zhang, Fu-Jen Chu, Hao Tang et al.
- **Affiliation**: Meta + Multiple Institutions
- **Venue**: CVPR 2026 (Best Paper Award)
- **Key Innovation**: Extends Segment Anything Model (SAM) to 3D understanding from single or few 2D images. Zero-shot 3D segmentation without 3D training data.
- **Significance**: Brings the "foundation model for segmentation" paradigm to 3D, enabling applications in robotics, AR/VR, and autonomous driving.

#### Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco et al.
- **Affiliation**: Google DeepMind + Collaborators
- **Venue**: CVPR 2026 (Best Paper Award)
- **Key Innovation**: Dynamic 4D scene reconstruction method that can reconstruct moving scenes from monocular video efficiently.
- **Significance**: Enables practical 4D reconstruction (3D + time) for real-world dynamic environments.

#### B³-Seg: Camera-Free, Training-Free 3DGS Segmentation
- **Authors**: Hiromichi Kamata, Samuel Arthur Munro, Fuminori Homma
- **Venue**: CVPR 2026 (Best Paper Award)
- **Key Innovation**: 3D Gaussian Splatting segmentation without camera parameters or training. Leverages inherent structure of 3D Gaussians for segmentation.
- **Significance**: Eliminates two major barriers to 3DGS adoption: need for calibrated cameras and per-scene training.

### 5.2 Vision-Language Models

#### Molmo2: Open Weights and Data for VLMs with Video Understanding and Grounding
- **Authors**: Christopher Clark, Jieyu Zhang, Zixian Ma et al.
- **Venue**: CVPR 2026 (Oral)
- **Key Innovation**: Open-source VLM with video understanding capabilities and spatial grounding. Fully open weights, training data, and code.
- **Significance**: Democratizes VLM research by releasing full pipeline (weights + data). Video understanding distinguishes it from image-only open VLMs.

#### TIPSv2: Vision-Language Pretraining with Enhanced Patch-Text Alignment
- **Authors**: Bingyi Cao, Koert Chen et al.
- **Venue**: CVPR 2026
- **Key Innovation**: Enhanced patch-text alignment for vision-language pretraining. Improves fine-grained understanding by explicitly aligning image patches with corresponding text spans.

### 5.3 Gaming Agents

#### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Collaborative team (NVIDIA, Stanford, Caltech, UChicago, UT Austin)
- **Affiliation**: NVIDIA Research + Academia
- **Venue**: CVPR 2026 (Award Candidate)
- **Key Innovation**: Vision-action foundation model trained on **40,000 hours of gameplay** across **1,000+ games**. Strong zero-shot competence across diverse gaming domains (platformers, racing, strategy, sports).
- **Results**: Achieves competitive performance with domain-specific SOTA models without fine-tuning.
- **Significance**: Largest open generalist game agent. Demonstrates scaling laws for game-playing — more games and hours = broader competence.
- **Arrow**: https://arxiv.org/abs/2605.XXXXX

### 5.4 Vision & Diffusion

#### ARCache: Caching Acceleration for Video Diffusion
- **Affiliation**: CVPR 2026
- **Key Innovation**: Adaptive caching strategy for video diffusion models that reuses intermediate computations across frames.
- **Significance**: Addresses the high inference cost of video diffusion — critical for practical deployment.

### 5.5 Best Paper Honorable Mentions

#### O-Voxel: Efficient 3D Representation
- **Affiliation**: Microsoft Research
- **Key Innovation**: Octree-based voxel representation for efficient 3D deep learning.

---

## 6. KDD 2026

**Conference**: Jeju Island, Korea, August 9-13, 2026

### 6.1 Recommendation Systems

#### SPiKE: Semantic Profiles into Knowledge Graphs for Enhanced Recommendation
- **Venue**: KDD 2026
- **Key Innovation**: Hybrid knowledge base combining structured user-item interactions with KG relations and textual metadata. Enriches item profiles using LLMs for better recommendation.
- **Significance**: Practical integration of LLM knowledge enrichment with traditional collaborative filtering.

#### RankUp: Towards High-rank Representations for Large Scale Advertising
- **Authors**: Jin Chen et al.
- **Affiliation**: Tencent (Weixin Video Accounts, Official Accounts, Moments)
- **Venue**: KDD 2026
- **Key Innovation**: Mitigates representation collapse in ad ranking through randomized permutation splitting. Prevents embedding dimensions from collapsing into low-rank subspace.
- **Results**: Deployed across Weixin: **GMV +3.41%** (Video), **+4.81%** (Official Accounts), **+2.12%** (Moments).
- **Significance**: Addresses a fundamental problem in large-scale embedding models — representation collapse — with a simple yet effective technique. Multi-scenario deployment validates robustness.

#### RankElastor: Effective-Rank Dynamics for Recommendation
- **Venue**: KDD 2026
- **Affiliation**: [Multiple institutions]
- **Key Innovation**: Analyzes and optimizes effective rank of embeddings during training. Shows that maintaining high effective rank throughout training improves generalization.
- **Significance**: Builds on the representation collapse literature with practical training dynamics optimization.

### 6.2 Few-Shot Learning & Tabular Data

#### TAROT: Task-Adaptive Refinement of LLM-prior Graphs for Few-shot Tabular Learning
- **Venue**: KDD 2026
- **Key Innovation**: Uses GPT-4o-mini for generating graph structures from tabular data metadata. Task-adaptive semantic graph refinement for few-shot tabular learning.
- **Results**: Outperforms traditional tabular methods on few-shot benchmarks by 5-10%.
- **Significance**: Novel application of LLMs to tabular learning — a domain traditionally dominated by gradient-boosted trees.

### 6.3 CTR & Advertising (KDD)

#### GR4AD: Generative Recommendation for Large-Scale Advertising
- **Affiliation**: Kuaishou
- **Venue**: KDD 2026
- **Key Innovation**: Production-oriented generative recommender for real-time advertising. Introduces UA-SID for advertisement tokenization, LazyAR decoder for efficiency, VSL and RSPO for value alignment, and dynamic beam serving.
- **Results**: Up to **4.2% ad revenue improvement** on Kuaishou.
- **Significance**: One of the first large-scale deployments of generative recommendation in the advertising domain. The UA-SID tokenization is tailored for ad-specific requirements.

#### EST: Towards Efficient Scaling Laws in CTR Prediction
- **Authors**: Mingyang Liu et al.
- **Affiliation**: Alibaba (Taobao)
- **Venue**: KDD 2026
- **Key Innovation**: Fully unified modeling without lossy aggregation. Lightweight Cross Attention + Content Sparse Attention. Shows stable power-law scaling relationship for CTR models.
- **Results**: Deployed on Taobao: **+3.27% RPM**, **+1.22% CTR**.
- **Significance**: Demonstrates that CTR models follow power-law scaling similar to LLMs — deeper models with more data yield predictable improvements.

### 6.4 CTR Scaling Papers (Full Track from KDD & Related)

#### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Affiliation**: Major social-media platform
- **Venue**: arXiv (applies across KDD/ICML cycle)
- **Key Innovation**: Dual-path inter-layer connector for CTR Transformers. Identity residual path + Block Attention Residual path with SiLU gate (replacing Softmax in attention residual).
- **Results**: Outperforms 12 baselines including OneTrans, TokenMixer-Large, UniMixer. **+0.32% AUC** on industrial dataset (331M interactions). Fits steeper compute-AUC scaling law (γ=0.118 vs 0.071 for OneTrans).
- **Significance**: The dual-path design decouples training stability (identity path) from adaptivity (attention path), enabling deeper CTR Transformers without degradation.

#### CTR-Sink: Attention Sink for Language Models in CTR
- **Authors**: Zixuan Li, Binzong Geng et al.
- **Affiliation**: Ant Group
- **Venue**: KDD 2026
- **Key Innovation**: Inserts sink tokens fused with recommendation signals (temporal distance) between user behaviors. Two-stage training guides attention to sink tokens; sink-specific attention mechanism amplifies inter-sink dependencies.
- **Results**: **0.2-0.5% AUC improvement** across industrial and public datasets on both RoBERTa and Qwen architectures.
- **Significance**: Architecture-agnostic: works with encoder (RoBERTa) and decoder (Qwen) models. Bridges the gap between LM pretraining and CTR data structure.

#### FAT: Field-Aware Transformer for CTR (Rademacher Scaling Law)
- **Affiliation**: Alibaba / Taobao
- **Venue**: arXiv (KDD cycle)
- **Key Innovation**: Identifies that standard Transformers assume sequential compositionality while CTR data requires combinatorial reasoning over heterogeneous fields. Introduces Field-Decomposed Attention with field-aware parameters and Basis-Composed Hypernetwork.
- **Theoretical Contribution**: First CTR scaling law based on **Rademacher complexity** — showing generalization depends on field interactions, not vocabulary size.
- **Results**: Up to **+4.38% AUC improvement** offline; **+2.33% CTR** and **+0.66% RPM** in live Taobao production.
- **Significance**: The Rademacher-based scaling law provides theoretical grounding for CTR model design.

---

## 7. SIGIR 2026

**Conference**: Melbourne, Australia, July 20-24, 2026 | **Stats**: 656 papers accepted

### 7.1 Agent-Based Search

#### Agentic Search in the Wild: Intents and Trajectory Dynamics from 14M+ Real Search Requests
- **Authors**: Jingjie Ning, João Coelho, Yibo Kong, Yunfan Long, Bruno Martins, João Magalhães, Jamie Callan, Chenyan Xiong
- **Affiliation**: Carnegie Mellon University + Collaborators
- **Venue**: SIGIR 2026
- **Key Innovation**: Large-scale log analysis of agentic search from **14.44M requests**. Introduces CTAR (Context Trace-Aware Retrieval) metric for evidence traceability. Reveals key patterns: 90%+ multi-turn sessions have ≤10 steps, 89% inter-step intervals <1 minute.
- **Significance**: First large-scale empirical characterization of how users interact with agentic search systems. Informs design of future search agents.

#### AgentRank: Trajectory-Aware Document Ranking for Autonomous IR
- **Venue**: SIGIR 2026
- **Key Innovation**: Ranking framework that learns document utility for autonomous agents in multi-step tasks. Not just relevance to query, but usefulness for the agent's next action.
- **Significance**: Re-frames IR ranking for the agent era — documents should be ranked by their actionability, not just topical relevance.

### 7.2 RAG & Retrieval

#### LTRR: Learning to Rank Retrievers for LLMs
- **Venue**: SIGIR 2026
- **Key Innovation**: Query routing approach that dynamically selects from a pool of retrievers based on query type. Uses pairwise XGBoost for best results, outperforming single-retriever approaches.
- **Results**: Significant improvement over best single retriever across diverse query types.
- **Significance**: In the RAG era, having multiple retrievers and routing dynamically beats any single retriever.

#### Revisiting BM25 Feedback Models Using HyDE
- **Authors**: Nour Jedidi, Jimmy Lin
- **Affiliation**: University of Waterloo
- **Venue**: SIGIR 2026
- **Key Innovation**: Shows BM25 feedback models (Rocchio, RM3) improve HyDE effectiveness by up to **1.4 points (4.2%)** on average. Classic IR techniques still useful in the LLM era.
- **Significance**: Important reminder that well-established IR methods complement modern LLM-based approaches.

### 7.3 Conversational Search

#### Improving Ad-hoc Search Effectiveness for Conversational IR via Model Merging
- **Venue**: SIGIR 2026
- **Key Innovation**: Training-free model merging strategy for conversational retrievers. Combines specialized retrievers without additional training.
- **Results**: Up to **15% higher NDCG@3** under zero-shot conditions.
- **Significance**: Model merging (popularized by model soups) applied to IR — zero-cost improvement for conversational search.

#### GEMS: Generative Entity Matching for Search
- **Venue**: SIGIR 2026
- **Key Innovation**: Uses generative LLMs for entity matching in search, combining generative and discriminative approaches.

### 7.4 Beyond Links (SIGIR)

#### Beyond Positive Signals: Mixed-Polarity Sequential Recommendation
- **Venue**: SIGIR 2026
- **Key Innovation**: Incorporates negative and mixed signals (skips, dislikes, dwell time) into sequential recommendation. Learns from both positive and negative user feedback.
- **Results**: **+9.6% AUC** improvement over positive-only methods.
- **Significance**: Most sequential recommenders only use positive feedback. This work shows negative signals contain rich signal for preference learning.

---

## 8. ACL 2026

**Conference**: San Diego, California, July 2-7, 2026

### 8.1 Agent Systems

#### SOAR: Supervision from Observation for Agentic RL
- **Authors**: Meng Li, Lei Li, Xiting Wang, Yi Yuan, Zheng Wei, Brucebian, Zang Li
- **Venue**: ACL 2026
- **Key Innovation**: Assigns positive advantages to observation tokens proportional to the negative entropy of preceding actions. Incentivizes agents to process observations that lead to decisive actions.
- **Results**: Improves performance up to **7.0% on reasoning tasks** and **16.9% on deep research tasks**.
- **Significance**: Novel RL signal — instead of rewarding good actions, rewards good observation processing. The agent learns which observations matter.

#### KARL: RL for LLM Agents on Multi-Turn Knowledge-Intensive Tasks
- **Authors**: Xueqiao Sun, Xiao Liu, Bowen Lv et al.
- **Affiliation**: Tsinghua University (THUDM)
- **Venue**: ACL 2026
- **Key Innovation**: Online RL with curiosity-driven reward shaping for knowledge exploration. Agent is rewarded for discovering novel, task-relevant information.
- **Results**: **Qwen2.5-14B agent outperforms GPT-4o, Claude-4, and o4-mini** on knowledge graph and database tasks.
- **Significance**: Demonstrates that smaller models + good RL can surpass frontier models on specific domains. Curiosity-driven exploration is key for knowledge-intensive tasks.

#### HSCodeComp: A Realistic and Expert-level Benchmark for Deep Search Agents
- **Affiliation**: Alibaba
- **Venue**: ACL 2026 (**Best Resource Paper Award**)
- **Key Innovation**: First expert-level benchmark for deep search agents on hierarchical rule application (customs HS code classification). Requires deep reasoning over structured rules.
- **Results**: Best agent achieves **49.4%** vs human **95.0%**. Alibaba's Qwen-based agent ranks #1 at **65.0%**.
- **Significance**: Reveals large gap between agents and human experts on structured reasoning tasks. Becomes standard benchmark for deep search capabilities.

### 8.2 LLM Robustness & Architecture

#### Robertha: Eigenspectrum Regularized Attention for Robust NLU
- **Authors**: Andreia Podasca, Anup Das
- **Venue**: ACL 2026
- **Key Innovation**: Attention mechanism based on Modern Hopfield Networks with Eigenspectrum Regularization. Controls the spectral properties of attention matrices for improved robustness.
- **Results**: Significantly outperforms existing robustness methods across **13 GLUE/SuperGLUE tasks**.
- **Significance**: Brings modern Hopfield network theory to NLP — attention as associative memory with spectral control.

### 8.3 Code & Structured Inference

#### MetaJuLS: Adaptive Constraint Propagation via Meta-Reinforcement Learning
- **Venue**: ACL 2026
- **Key Innovation**: Meta-learned constraint propagation schedules for LLM constrained decoding. Learns which constraints to apply when.
- **Results**: **1.5-2.0× speedups** over GPU-optimized baselines while maintaining accuracy.
- **Significance**: Makes constrained decoding practical for production use. Critical for applications requiring structured outputs (JSON, code, etc.).

#### CoRE: Fine-Grained Code Reasoning Benchmark
- **Authors**: Jun Gao et al.
- **Affiliation**: Zhejiang University, CUHK, CSIRO, Fudan, Yale
- **Venue**: ACL 2026 (Findings)
- **Key Innovation**: Evaluates implementation invariance and process transparency in code LLMs. Reveals "superficial execution" where models produce correct outputs without correct intermediate reasoning.
- **Significance**: Exposes a critical failure mode: code LLMs may look correct on outputs but are wrong in process.

#### DUET: Dual Execution for Test Output Prediction
- **Venue**: ACL 2026 (Findings)
- **Key Innovation**: Combines direct code execution and LLM-based pseudocode execution via functional majority voting.
- **Results**: **+13.6 pp improvement** on LiveCodeBench.
- **Significance**: Dual execution (real + simulated) provides robustness — when real execution fails, simulated execution backstops.

---

## 9. WWW 2026

**Conference**: Dubai, UAE

### 9.1 Test of Time Award

#### LINE: Large-scale Information Network Embedding
- **Authors**: Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, Qiaozhu Mei
- **Affiliation**: BioGeometry (Tang), University of Michigan
- **Original Venue**: WWW 2015
- **Key Innovation**: Graph embedding method that preserves first-order and second-order proximity. One of the most widely adopted graph embedding methods in industry.
- **Significance**: Foundational work that enabled large-scale network analysis — used across recommendation, advertising, social network analysis.

### 9.2 Recommendation & CTR Papers

#### ThinkRec: Thinking-based LLM Recommendation
- **Venue**: WWW 2026
- **Key Innovation**: Applies chain-of-thought reasoning to recommendation tasks. LLM "thinks" about user preferences before making recommendations, with structured reasoning traces.
- **Significance**: Extends the "thinking" paradigm (popularized by o1, DeepSeek-R1) to recommendation.

#### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Venue**: WWW 2026
- **Key Innovation**: Generates semantic interest cohorts as explicit intent representations. Models user interest shift as a generative process over cohorts.
- **Results**: Hierarchical candidate-aware network injects contextual signal into ranking stage.

#### SparseCTR: Sparse Attention for Long-Term Behaviors
- **Authors**: Weijiang Lai, Beihong Jin et al.
- **Affiliation**: Meituan
- **Venue**: WWW 2026
- **Key Innovation**: Three-branch sparse self-attention mechanism that segments behavior sequences in a personalized manner. Proposes composite relative temporal encoding.
- **Results**: Shows **scaling law phenomenon** across three orders of magnitude in FLOPs. **+1.72% CTR** improvement.
- **Significance**: First paper to demonstrate scaling laws for CTR models at WWW. The three-branch design efficiently handles long sequences.

---

## 10. EMNLP 2025

**Conference**: Suzhou, China, November 4-9, 2025

### 10.1 Industry Papers

- **Bloomberg AI**: Published 7 papers covering NLP, LLMs, retrieval-augmented language models, QA, and information extraction for financial domains.
- **Key Theme**: Financial NLP heavily leverages domain-specific pretraining and structured knowledge integration.

---

## 11. CIKM 2025

**Conference**: Seoul, Korea, November 10-14, 2025 | **Stats**: 800+ papers accepted

### 11.1 Key Papers

#### RankMixer: Scaling Up Ranking Models
- **Affiliation**: ByteDance
- **Venue**: CIKM 2025
- **Key Innovation**: TokenMixer-based architecture for scalable ranking. Demonstrates consistent improvement with model size.
- **Significance**: Influential in the CTR scaling movement — inspired follow-up work at ByteDance (TokenMixer-Large, OneTrans).

#### MediKS: Traceable Drug Recommendation over Medical Knowledge Graphs
- **Venue**: CIKM 2025
- **Key Innovation**: Medical knowledge graph-based drug recommendation with traceable reasoning paths. Enables clinicians to verify recommendation rationales.

---

## 12. RecSys 2025

**Conference**: Prague, Czech Republic, September 22-26, 2025

### 12.1 Generative Recommendation

#### Semantic IDs for Joint Generative Search and Recommendation
- **Venue**: RecSys 2025
- **Key Innovation**: Investigates Semantic ID construction for unified search+recommendation. Shows bi-encoder fine-tuned on both tasks provides effective trade-off. Challenges conventional wisdom that per-task IDs are optimal.
- **Significance**: Suggests that unified SIDs for search and recommendation are feasible — important for platforms with both functionalities.

### 12.2 LLM-Enhanced Recommendation

#### LSVCR: Enhancing Sequential Recommender with LLMs for Joint Video and Comment Recommendation
- **Affiliation**: Kuaishou
- **Venue**: RecSys 2025
- **Key Innovation**: Two-stage training paradigm combining SR model with supplemental LLM. Jointly recommends videos and their comments.
- **Results**: Online A/B testing on Kuaishou: **4.13% cumulative gain** in comment watch time.
- **Significance**: Novel dual-recommendation task (video + comment). Demonstrates LLM can improve content recommendation beyond traditional collaborative filtering.

#### LLM-RecG: Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation
- **Venue**: RecSys 2025
- **Key Innovation**: Addresses domain semantic bias in LLMs for cross-domain recommendations using generalization losses. LLMs encode domain-specific biases that hurt zero-shot transfer.
- **Significance**: Identifies and mitigates a specific failure mode of LLM-based recommenders — semantic bias from pretraining corpus.

#### LONGER: Ultra-Long User Behavior Sequences
- **Affiliation**: ByteDance
- **Venue**: RecSys 2025
- **Key Innovation**: Efficient handling of ultra-long user behavior sequences using attention compression and multi-scale aggregation.
- **Significance**: Paved the way for ByteDance's subsequent work on 10K-length sequence modeling.

#### SUAN: Online CTR Scaling Methodology
- **Affiliation**: Meituan
- **Venue**: RecSys 2025
- **Key Innovation**: Systematic methodology for scaling CTR models in online production. Addresses training-serving skew, data distribution shifts, and cost constraints.

---

## 13. arXiv — Recent Papers (Focus: July 2026)

### 13.1 LLM Reasoning & Training

#### MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
- **Authors**: Ruilin Tong et al.
- **arXiv**: 2607.06974
- **Key Innovation**: Dynamic step-wise memory expansion with correctness-optimized memory composition. Maintains modular memory units (asymmetric pairs of sub-goal embeddings and sub-instructions), each with a learnable selection head. Coarse-to-fine retrieval mechanism for test-time self-improvement.
- **Significance**: Memory-augmented reasoning that improves at test time without weight updates. Practical for deployment when fine-tuning is infeasible.

#### LLM-as-a-Verifier: A General-Purpose Verification Framework
- **arXiv**: 2607.05391
- **Key Innovation**: Computes expectation over distribution of scoring token logits to generate continuous scores. Enables verification scaling across score granularity, repeated evaluation, and criteria decomposition, all without additional training.
- **Significance**: Training-free verification is critical for agentic systems where verification needs change dynamically.

#### KARLA: Knowledge-base Augmented Retrieval for Language Models
- **arXiv**: 2606.26807
- **Key Innovation**: LLM automatically pulls factual knowledge from a KB during generation via special tokens that trigger KB queries. Enables fact updates without retraining and tracing facts to sources for transparency.
- **Results**: Smaller models with KARLA achieve same factual accuracy as larger models.
- **Significance**: Separates linguistic competence from factual knowledge — addresses the "frozen knowledge" problem in LLMs.

#### Belief-Reality Separation in Language Models
- **arXiv**: 2607.11945
- **Key Innovation**: Shows capable language models hold what a character believes apart from what is true through two mechanisms: a generic value slot that binds attributed value, and a router at query position selecting which frame (belief or reality) is read.
- **Significance**: Mechanistic understanding of how LLMs model beliefs — relevant to theory of mind and narrative understanding.

#### Scalpel vs. Hammer: GRPO Amplifies, SFT Replaces
- **arXiv**: 2507.10616
- **Key Innovation**: Comparative analysis of GRPO (RL) and SFT for reasoning training at the parameter level. RL yields minor in-domain maths gains with slight MMLU degradation; SFT shows more pronounced in-domain gains but greater out-of-domain degradation. SFT additionally affects mid-layer MLPs, potentially causing knowledge degradation — whereas RL primarily modifies query/key attention weights.
- **Significance**: Important mechanistic understanding: RL "amplifies" existing capabilities while SFT "replaces" them. Explains why RL generalizes better OOD.

#### LoRA is All You Need for Safety Alignment of Reasoning LLMs
- **arXiv**: 2507.17075
- **Key Innovation**: Using LoRA for SFT on refusal datasets effectively aligns safety without harming reasoning. Low-rank updates are orthogonal to reasoning weights.
- **Results**: Experiments on DeepSeek-R1-Distill-Qwen-7B and 14B show safety comparable to full fine-tuning while preserving reasoning on AIME, GPQA, HumanEval, and MBPP.
- **Significance**: Practical solution to the "Safety Tax" — the well-known degradation of reasoning after safety alignment.

#### RLSF: Post-Training LLMs via RL from Self-Feedback
- **arXiv**: 2507.21931
- **Key Innovation**: Uses model's own confidence as intrinsic reward. After frozen LLM generates CoT solutions, confidence of each answer span is computed to rank traces. These synthetic preferences fine-tune policy via standard preference optimization.
- **Results**: RLSF + PPO outperforms DPO, improving both calibration and reasoning accuracy.
- **Significance**: No human labels, gold answers, or externally curated rewards needed. Fully self-supervised post-training.

#### The Wall Confronting Large Language Models
- **arXiv**: 2507.19703
- **Key Innovation**: Argues scaling laws severely limit LLM ability to improve prediction uncertainty, making scientific-grade reliability intractable. Non-Gaussian outputs from Gaussian inputs may be the root of error pileup. Proposes avoiding "Degenerative AI" through structural understanding.
- **Significance**: Important counterpoint to the scaling orthodoxy. Provides theoretical argument for diminishing returns.

#### SMACS: Open-Source LLMs Collaboration Beats Closed-Source
- **arXiv**: 2507.14200
- **Key Innovation**: Integrates 15 open-source LLMs using Retrieval-based Prior Selection (RPS) for Top-k selection per instance, plus Exploration-Exploitation-Driven Posterior Enhancement (EPE) for diverse response generation.
- **Results**: Surpasses Claude-3.7-Sonnet (+12.73%), GPT-4.1 (+5.36%), GPT-o3-mini (+5.28%).
- **Significance**: Demonstrates open-source collectives can exceed closed-source performance ceilings. Performance improves monotonically as more LLMs are added.

#### Sparse Delta Memory: Scaling Linear RNNs Through Sparsity
- **Authors**: Loïc Cabannes, Pierre-Emmanuel Mazaré et al.
- **Affiliation**: Meta FAIR, Inria Paris
- **arXiv**: 2607.07386
- **Key Innovation**: Replaces dense key-value outer product with sparse reads/writes to large explicit memory. Scales hidden state to orders of magnitude higher capacity with same compute budget.
- **Results**: Lower training loss than full attention at **8B scale**.
- **Significance**: Linear RNNs + sparse memory may finally match or exceed attention at scale. The sparse addressing mechanism is key.

### 13.2 CTR Prediction & Advertising

#### Long-History User Transformers for Real-Time Ad Ranking
- **Authors**: Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin
- **Affiliation**: Yandex
- **arXiv**: 2607.14331
- **Key Innovation**: Decouples history encoding from real-time inference — high-capacity offline transformer asynchronously encodes full cross-surface interaction history into cached representation; lightweight runtime model combines with request context at serving time. Pre-trained with dual objective (feedback prediction + next-item prediction).
- **Results**: Recovers **72-80% of full-history quality**. Production A/B: **+2.77% search ad ranking, +2.1% Yandex Ad Network, +2.26% revenue** — without latency increase.
- **Significance**: Practical resolution of the "long history vs. low latency" tension. The offline-online decoupling pattern is generalizable to any large-scale ad system.

#### TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search
- **Authors**: Zhentao Song, Yufeng Gao, Xing Fang et al.
- **Affiliation**: Alibaba (Tmall)
- **arXiv**: 2607.13398
- **Key Innovation**: Five components for unified Transformer search ranking: Hierarchical Distribution-Calibrated Tokenization (FSR+DCP), Field-Adaptive Gated Transformer (per-field QKV + noise-adaptive gating), Decoupled FiLM Late Fusion, Context-Aware Bias Net, Error-Aware Progressive Training.
- **Results**: Substantial gains in UCTCVR and GMV on Tmall Search.
- **Significance**: Continues DLRM-to-Transformer transition with careful handling of feature heterogeneity. The all-in-tokenization approach is refined with distribution-calibrated projections.

#### MARS: Modality-Aligned Retrieval for Sequence Augmented CTR
- **Affiliation**: Kuaishou
- **arXiv**: 2509.01184
- **Key Innovation**: Stein kernel-based method to align text and image features into unified semantic space for multimodal user embeddings. Retrieves, filters, and concentrates similar behavior sequences from high-active users for low-active users.
- **Results**: Deployed at Kuaishou serving hundreds of millions of users, with significant growth on core business metrics.
- **Significance**: Addresses the cold-start/interaction sparsity problem for low-active users through cross-user multimodal augmentation.

#### CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado et al.
- **Affiliation**: LinkedIn
- **arXiv**: 2602.11410
- **Key Innovation**: End-to-end decoder-only transformer for ads CTR. Introduces context-conditioned decoding with multi-tower prediction heads, self-gated attention, timestamp-based RoPE, and session masking.
- **Results**: **11.04% CTR lift** in online A/B testing on LinkedIn.
- **Significance**: Largest reported CTR improvement from a decoder-only architecture. Demonstrates that LLM-style architectures can significantly outperform traditional DLRMs in CTR.

#### GRAB: LLM-Inspired Sequence-First CTR Prediction
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren et al.
- **Affiliation**: Baidu
- **arXiv**: 2602.01865
- **Key Innovation**: End-to-end generative framework for CTR with Causal Action-aware Multi-channel Attention (CamA). Demonstrates scaling behavior with monotonic improvement as longer interaction sequences are used.
- **Results**: Deployed at Baidu: **3.05% revenue increase** and **3.49% CTR rise**.
- **Significance**: Confirms the sequence-first paradigm (treat user behavior sequences as primary, features as secondary) at Baidu scale.

#### DiffuMIN: Diffusion-driven Multi-interest Network for CTR
- **Authors**: Weijiang Lai et al.
- **arXiv**: 2508.15311
- **Key Innovation**: Two-stage model: (1) target-oriented multi-interest extraction via orthogonal decomposition of target embeddings into interest channels; (2) diffusion module guided by contextual interests generates augmented interests. Contrastive learning ensures alignment.
- **Results**: Online A/B: **+1.52% CTR** and **+1.10% CPM**.
- **Significance**: First application of diffusion modeling to user interest generation in CTR. The diffusion module creates realistic "what-if" interests.

#### DMGIN: Multimodal LLMs for Lifelong User Post-click Behaviors
- **Affiliation**: Alibaba
- **arXiv**: 2508.21801
- **Key Innovation**: Uses Multimodal LLMs to group repeated shops via multimodal embeddings (name + images). Reorganizes lifelong behavior sequences from tens of thousands to hundreds. Intra-group + inter-group transformers capture group traits and temporal evolution.
- **Results**: Deployed in LBS advertising: **+4.7% CTR** and **+2.3% RPM**.
- **Significance**: Near-zero additional computational overhead through offline shop embedding. Demonstrates MLLM-based sequence compression at scale.

#### OneRanker: Unified Generation and Ranking in Industrial Advertising
- **Affiliation**: Tencent (Weixin/WeChat Channels)
- **arXiv**: 2603.02999
- **Key Innovation**: Architectural-level deep integration of generation and ranking. Value-aware multi-task decoupling, coarse-to-fine collaborative target awareness with Fake Item Tokens, input-output dual-side consistency guarantees.
- **Results**: Deployed on Tencent Weixin: **+1.34% GMV** improvement, Costs +0.72%.
- **Significance**: End-to-end generative advertising framework that unifies two traditionally separate stages (generation + ranking).

#### GRAD: Generative Foundation Model for Auto-Bidding
- **Affiliation**: Meituan
- **arXiv**: 2508.02002
- **Key Innovation**: Scalable foundation model with Action-Mixture-of-Experts for diverse bidding exploration and Causal Transformer value estimator for constraint-aware optimization. Addresses distribution shift, limited exploration, and CPM/ROI constraints.
- **Results**: Deployed across Meituan: **+2.18% GMV** and **+10.68% ROI**.
- **Significance**: First bidding foundation model showing scaling-law-inspired architecture design for auto-bidding.

#### Bid2X: Bidding Foundation Model for Online Advertising
- **Authors**: Jiahao Ji et al.
- **Affiliation**: Alibaba / Taobao
- **arXiv**: 2510.23410
- **Key Innovation**: First bidding foundation model generalizing across scenarios. Uniform series embeddings encode heterogeneous bidding data. Zero-inflated projection module handles unique distribution of bidding data.
- **Results**: Evaluated on **8 large-scale datasets** from Taobao. Outperforms MBRL across PV, Cost, GMV, and ROI.
- **Significance**: Generalization across bidding scenarios without per-scenario tuning. Theoretical convergence guarantee to zero-inflated distribution.

#### CBD: Generative Auto-Bidding via Diffusion Completer-Aligner
- **Affiliation**: Kuaishou
- **arXiv**: 2509.03348
- **Key Innovation**: Completer augments diffusion training with t-length historical sequence completion task. Aligner uses trajectory-level return model to refine generated trajectories.
- **Results**: **29.9% improvement** in conversion value on sparse-reward benchmarks. Deployed on Kuaishou with significant improvements.
- **Significance**: Addresses generation uncertainty in diffusion-based auto-bidding — a key barrier to production deployment.

#### LLM-Auction: Generative Auction for LLM-Native Advertising
- **arXiv**: 2512.10551
- **Key Innovation**: First learning-based generative auction mechanism integrating auction and LLM generation. LLM post-trained to model allocation externalities without extra inference cost. First-price payment rule achieves favorable incentive properties.
- **Results**: **59.1% revenue improvement** over state-of-the-art.
- **Significance**: LLM itself implements the allocation rule — the first "LLM-native" auction mechanism.

#### EGA-V1: End-to-End Generative Architecture for Unified Online Advertising
- **Affiliation**: Meituan
- **arXiv**: 2505.19755
- **Key Innovation**: Single generative model replacing multi-stage cascading architecture. RecFormer with cluster-attention models user interests and externalities. Non-autoregressive processing for real-time serving.
- **Results**: **+5.2% CTR, +13.6% RPM, +3.1% ROI** on Meituan.
- **Significance**: Radical simplification of ad ranking pipeline — one model replaces the entire cascade.

### 13.3 Sequential Modeling

#### Make It Long, Keep It Fast: 10K Sequence Modeling on Douyin
- **Authors**: Lin Guan et al.
- **Affiliation**: ByteDance (Douyin/TikTok)
- **arXiv**: 2511.06077
- **Key Innovation**: End-to-end system scaling long-sequence modeling to **10K-length histories** in production. STCA (Stacked Target-to-History Cross Attention) reduces complexity from O(n²) to O(n). RLB (Request Level Batching) aggregates multiple targets for same user, reducing bandwidth by up to **84%**.
- **Results**: Length-extrapolative training: trains on ~2k average, serves on 10k. Deployed on Douyin with monotonic gains.
- **Significance**: First production deployment of 10K-length user behavior sequences. The STCA architecture and RLB batching are reference designs for long-sequence modeling.

#### ReaSeq: Reasoning-Enhanced Sequential Modeling on Taobao
- **Authors**: Chuan Wang, Gaoming Yang et al.
- **Affiliation**: Alibaba / Taobao
- **arXiv**: 2512.21257
- **Key Innovation**: Two components: (1) Reasoning-Enhanced Representation — multi-agent collaboration distills product knowledge into enriched item representations via CoT; (2) Generative Behavior Reasoning — Diffusion LLM reconstructs plausible unobserved user behaviors.
- **Results**: **>6.0% IPV, >6.0% CTR, >2.9% Orders, >2.5% GMV** on Taobao.
- **Significance**: World-knowledge-enhanced sequential modeling via LLM reasoning. The generative behavior reasoning component fills in gaps in observed behavior.

#### ULIM: User Long-Term Multi-Interest Retrieval Model
- **Affiliation**: Alibaba / Taobao
- **arXiv**: 2507.10097
- **Key Innovation**: Enables thousand-scale behavior modeling in retrieval stages (traditionally limited to ranking). Category-Aware Hierarchical Dual-Interest Learning partitions sequences into category-aware subsequences. Pointer-Generator Interest Network (PGIN) for cascaded category-to-item retrieval.
- **Results**: **+5.54% clicks, +11.01% orders, +4.03% GMV** on Taobao.
- **Significance**: Bridges the retrieval-ranking gap — retrieval traditionally uses simple statistics while ranking uses deep models. ULIM brings deep sequential modeling to retrieval.

#### GAMER: Generative Sequential Recommendation via Hierarchical Behavior Modeling
- **Authors**: Zhefan Wang, Siyu Gu et al.
- **arXiv**: 2511.03155
- **Key Innovation**: Multi-behavior generative recommendation with decoder-only backbone. Cross-level interaction layer captures hierarchical dependencies among behaviors (clicks, likes, shares → conversions). Releases ShortVideoAD dataset.
- **Results**: Outperforms both discriminative and generative baselines with **>20% gains** on most metrics.
- **Significance**: First short-video advertising multi-behavior dataset (ShortVideoAD). Decoder-only architecture for generative sequential recommendation.

### 13.4 Game AI & Reinforcement Learning

#### Think-In Games (TiG): LLMs Learn to Reason via Game RL
- **arXiv**: 2508.21365
- **Key Innovation**: Reformulates RL as language modeling — LLMs generate language-guided policies refined through online GRPO based on environmental feedback.
- **Results**: Qwen-3-14B achieves **90.91% accuracy** in Honor of Kings, outperforming DeepSeek-R1 (86.67%) which is **10× larger**.
- **Significance**: Smaller models can rival much larger ones when trained with game-based RL. Provides interpretable step-by-step natural language explanations for decisions.

#### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors**: Bo Liu, Leon Guertler et al.
- **arXiv**: 2506.24119
- **Key Innovation**: LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Negotiation) against improving versions of themselves. Proposes Role-conditioned Advantage Estimation (RAE) for stable multi-agent training.
- **Results**: Multi-game training achieves up to **+10.5% on 8 reasoning benchmarks** across Qwen and Llama families. Even DeepSeek-R1-Distill-Qwen-7B benefits further.
- **Significance**: Zero-sum games provide unlimited curriculum for reasoning development. Cognitive patterns (spatial, probabilistic, strategic) learned from games transfer to general reasoning.

#### Foundation Model Self-Play (FMSP)
- **Authors**: Aaron Dharna, Cong Lu, Jeff Clune
- **arXiv**: 2507.06466
- **Key Innovation**: Three variants: (1) vFMSP refines policies via competitive self-play, (2) NSSP builds diverse strategy populations, (3) QDSP combines diversity and refinement. In Gandalf (LLM jailbreaking), FMSPs automatically break through **6 defense levels** and patch vulnerabilities.
- **Significance**: Foundation model code generation enables policy search across diverse domains. Automatic red-teaming and vulnerability patching.

#### Learning Game-Playing Agents with Generative Code Optimization
- **Authors**: Zhiyi Kuang, Ryan Rong et al.
- **arXiv**: 2508.19506
- **Key Innovation**: Policies represented as Python programs refined via LLMs using the Trace framework. Self-evolving code with execution traces and natural language feedback.
- **Results**: Atari games (Pong, Breakout, Space Invaders) achieve competitive performance with deep RL baselines using **52-98% less training time** and far fewer environment interactions.
- **Significance**: Programmatic policies (code) are interpretable by design. Dramatically reduces training cost.

#### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games
- **arXiv**: 2605.00347
- **Key Innovation**: Open training framework for VLM agents using adapted PPO with lightweight turn-level critic. Trains on Super Mario Land requiring 100+ turns of interaction.
- **Results**: Outperforms frontier models by **at least 3× average game progress**.
- **Significance**: Turn-level critic for stability in long-horizon tasks. Open framework enables reproducible VLM agent research.

#### Multiplayer Interactive World Models
- **arXiv**: 2607.05352
- **Key Innovation**: First multiplayer world model for highly dynamic environments. **5-billion-parameter** latent diffusion model generates four-player matches in real time at **20 FPS** on single Nvidia B200.
- **Results**: Rollouts stay stable far beyond training horizon, continuing for hours.
- **Significance**: Opens the door to world models for multiplayer games — much harder than single-player due to interactive dynamics.

#### GIFT: Games as Informal Training for Generalizable LLMs
- **arXiv**: 2601.05633
- **Key Innovation**: Proposes using games as environment for LLM informal learning. Nested Training Framework transforms implicit OR objective into explicit AND objective.
- **Significance**: Game-based informal learning improves generalization across ability-oriented benchmarks.

#### NitroGen (CVPR 2026) — Game AI Foundation Model
- **Affiliation**: NVIDIA + Academia
- **Venue**: CVPR 2026 (also listed under CVPR)
- **Key Innovation**: Vision-action foundation model trained on 40,000 hours of gameplay across 1000+ games. Zero-shot generalization to unseen games.
- **Significance**: Largest open generalist gaming agent to date.

### 13.5 Code Generation & Execution

#### Self-Execution Simulation Improves Coding Models
- **arXiv**: 2026
- **Key Innovation**: Combines SFT on natural language execution traces with RL using verifiable rewards. Self-verification and self-fixing through simulated test execution.
- **Results**: Up to **43% improvement on CruxEval**, **39% on competitive programming**.
- **Significance**: Models learn to simulate code execution internally, enabling verification without external tools.

#### EAGER: Executing as You Generate
- **Authors**: Zhensu Sun et al.
- **arXiv**: 2026
- **Key Innovation**: Parallel execution paradigm that starts executing code while later tokens are being generated. Pipeline parallelism of generation and execution.
- **Results**: Reduces non-overlapped execution time by up to **99.8%**, end-to-end latency by up to **37.3%**.
- **Significance**: Novel approach to code execution latency — don't wait for full generation, execute incrementally.

#### EvoCodeBench: A Human-Performance Benchmark for Self-Evolving LLM-Driven Coding Systems
- **arXiv**: 2026
- **Key Innovation**: Evaluates inference-time self-evolution with multi-language support. Tracks performance dynamics, efficiency metrics, and human-referenced comparison.
- **Significance**: First benchmark specifically for self-evolving code systems.

#### Are LLM-Generated GPU Kernels Production-Ready? (Atrex-Bench)
- **Authors**: Lingyun Yang, Yuxiao Wang et al.
- **Affiliation**: Alibaba
- **arXiv**: 2607.14541
- **Key Innovation**: Trace-driven benchmark (Atrex-Bench) + optimization agent (Atrex-Kernel-Agent) for LLM-generated CUDA kernels.
- **Significance**: Directly relevant to efficient LLM inference and systems programming.

### 13.6 Generative Models & Sequential Modeling

#### NextFlow: Unified Sequential Modeling for Multimodal Understanding
- **Authors**: Huichao Zhang, Liao Qu, Yiheng Liu et al.
- **arXiv**: 2601.02204
- **Key Innovation**: Unified decoder-only autoregressive transformer trained on **6 trillion** interleaved text-image discrete tokens. Next-scale prediction for images (instead of raster-scan), enabling **1024×1024 image generation in 5 seconds**.
- **Results**: State-of-the-art among unified text-image models.
- **Significance**: Next-scale prediction is more efficient than raster-scan for image generation in unified models.

#### Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: Aakash Lahoti, Kevin Y. Li, Berlin Chen et al.
- **arXiv**: 2603.15569
- **Key Innovation**: Three improvements: more expressive recurrence from SSM discretization, complex-valued state update rule, MIMO formulation.
- **Results**: Comparable perplexity to Mamba-2 using **half the state size**. Gains across retrieval, state-tracking, and language modeling.
- **Significance**: State space models continue to improve — complex-valued states add expressivity without parameter cost.

#### Oryx: Hybrid Model with Flexible Sequence Modeling
- **Authors**: Kevin Y. Li, Asher Trockman, Ananda Theertha Suresh et al.
- **arXiv**: 2605.28769
- **Key Innovation**: Hybrid model that flexibly switches between different mixers (attention, recurrence) throughout a sequence. Ties **≥90% of parameters** across mixers, enabling shared internal representations.
- **Results**: Outperforms baselines by **≥0.7 percentage points** on averaged language modeling tasks.
- **Significance**: Sequence-axis hybridization — different tokens get different mixing strategies.

#### Sparse Delta Memory: Scaling Linear RNNs Through Sparsity
- **Affiliation**: Meta FAIR, Inria Paris
- **arXiv**: 2607.07386
- **Key Innovation**: Sparse reads/writes to large explicit memory instead of dense key-value outer product. Scales hidden state to orders of magnitude higher capacity.
- **Results**: Lower training loss than full attention at **8B scale** — constant compute with larger state.
- **Significance**: Linear RNNs with sparse memory may finally match/exceed attention at scale.

### 13.7 Sequential Recommendation — Production Systems

#### STAR-Rec: Length Variance and Pattern Diversity in Sequential Recommendation
- **Authors**: Maolin Wang et al.
- **arXiv**: 2505.03484
- **Key Innovation**: Addresses two underexplored challenges: length variance (users have vastly different behavior sequence lengths) and pattern diversity (heterogeneous interaction patterns). Specialized modules for both.

#### HiT-LBM: Hierarchical Tree Search for Lifelong Behavior Modeling
- **arXiv**: 2505.19505
- **Key Innovation**: Uses LLMs for lifelong behavior modeling via Chunked User Behavior Extraction (CUBE) and Hierarchical Tree Search for Interests (HTS). Compatible with any ID-based recommendation backbone.
- **Significance**: Model-agnostic LLM enhancement for lifelong behavior modeling — embeddable into existing systems.

#### GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li et al.
- **Affiliation**: JD.com
- **arXiv**: 2604.14878
- **Key Innovation**: Addresses scaling challenges in generative retrieval to industrial systems. Page-wise NTP task, asymmetric linear Token Merger, and GRPO-SR for preference alignment.
- **Results**: **9.5% improvement in click count** and **8.7% in transaction count** on JD App.
- **Significance**: One of the largest-scale deployments of generative recommendation at a major e-commerce platform.

#### AgentX: Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Affiliation**: Kuaishou
- **arXiv**: 2606.26859
- **Key Innovation**: Multi-agent system autonomously generating, implementing, evaluating, and learning from recommendation experiments. Brainstorm Agent, Developing Agent, Evaluation Agent, and Harness Evolution layer (SGPO).
- **Results**: 3 workers turning **374 ideas into 10 launchable rollouts**.
- **Significance**: Fully automated recommendation research — the system iterates itself. SGPO provides semantic-gradient updates for evolution.

### 13.8 AI Agent Systems

#### STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training
- **arXiv**: 2026
- **Key Innovation**: Proposes normalized entropy to decouple state complexity from agent confidence. Hierarchical group-based RL framework with trajectory-aware reward and trajectory-independent penalty.
- **Results**: State-of-the-art on ALFWorld, WebShop, Search-Augmented QA.
- **Significance**: Addresses the challenge of training agents on trajectories of varying quality — selective utilization of good trajectories.

#### Next-Generation Agentic RL Systems Enable Self-Evolving Agents (AReaL2.0)
- **Authors**: Ran Yan et al.
- **arXiv**: 2026
- **Key Innovation**: Architecture with standardized agent trajectory data protocol, enterprise-grade data proxy, and unified agent evolution control plane.
- **Significance**: Blueprint for self-evolving agents in production — standardization of data formats enables cross-agent learning.

#### Proof-or-Stop: Loop Engineering for Verifiable Evidence-Gated Lifecycle Control
- **Authors**: Jek Huang, Jeffery Hsia, Jiayi Sun et al.
- **arXiv**: 2607.14890
- **Key Innovation**: Evidence-gated lifecycle control — "don't trust the agent, trust the evidence." Comprehensive 48-page framework for verifiable agent behavior.
- **Significance**: Addresses the verification gap in AI agents. Aligns with Karpathy's "Verifiability" and "Software 3.0" principles.

#### AutoSynthesis: An Agentic System for Automated Meta-Analysis
- **Authors**: Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano, Francesco Pierri, Stefan Feuerriegel
- **arXiv**: 2607.15247
- **Key Innovation**: End-to-end agentic system that automates meta-analysis — from literature search to statistical synthesis.
- **Significance**: "Autoresearch" pattern applied to scientific methodology.

#### SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration
- **Authors**: Yuyao Zhang, Junjie Gao, Zhengxian Wu et al.
- **Affiliation**: Renmin University
- **arXiv**: 2607.15257
- **Key Innovation**: Multi-agent collaboration framework for open-domain information seeking. Open source at github.com/antins-labs/SearchOS.

### 13.9 Advertising & Auction Theory

#### Adaptive Ad Load Design for Sponsored Search Markets
- **Authors**: Mohammad Rashid, Hema Yoganarasimhan
- **arXiv**: 2607.14418
- **Key Innovation**: Evidence, theory, and deployment of adaptive ad load design — how many ads to show per page based on context.
- **Significance**: Ad load optimization is often overlooked but has massive revenue impact. Bridges economic theory with ML systems.

#### ToolRec: Calibrated Preference Alignment for Query Recommendation in On-Device Assistants
- **Authors**: Zihan Luo, Lingkui Chen et al.
- **Affiliation**: OPPO
- **arXiv**: 2607.08466
- **Key Innovation**: Calibrated preference alignment for on-device query recommendation, integrating 708 system tools (SysToolKit). Dual-level calibration to mitigate user behavioral noise.
- **Results**: Online A/B on **OPPO Xiaobu (150M+ MAU)**: significant CTR and click volume improvements.
- **Significance**: On-device LLM recommendation with tool integration. Relevant to "Build for Agents" and LLM GUI themes.

#### Position Auctions with a Capacity Constraint
- **Authors**: Eleni Batziou, Georgios Birmpas et al.
- **arXiv**: 2607.12040
- **Key Innovation**: First truthful constant-approximation mechanism for capacity-constrained position auctions with heterogeneous ad sizes.
- **Significance**: Novel auction theory result for modern ad formats where ad sizes vary.

### 13.10 Generative Recommendation — Architectures

#### GLASS: Generative Recommender for Long-sequence Modeling
- **Authors**: Shiteng Cao, Junda She, Ji Liu, Bin Zeng, Chengcheng Guo et al.
- **arXiv**: 2602.05663
- **Key Innovation**: Integrates long-term user interests into generative recommendation via SID-Tier and Semantic Search. Maps long-term interactions into unified interest vector for initial SID token prediction.

#### SIDReasoner: Reasoning over Semantic IDs for Generative Recommendation
- **Authors**: Yingzhi He, Yan Sun, Junfei Tan, Yuxin Chen et al.
- **arXiv**: 2603.23183
- **Key Innovation**: Two-stage framework eliciting reasoning over SIDs by strengthening SID-language alignment. Multi-task training on enriched SID-centered corpus + GRPO for outcome-based feedback.

#### Gryphon: Unified Architecture for SID Generation and Item-Level Scoring
- **Authors**: Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov et al.
- **Affiliation**: Industrial music service
- **arXiv**: 2606.08604
- **Key Innovation**: Encoder-decoder generative recommendation adding jointly trained item-level scoring alongside SID generation. Resolves generated SIDs to concrete items and re-scores them.
- **Significance**: Addresses a key limitation of generative recommenders: miscalibrated sequence scores.

---

## 14. arXiv — Live Papers (July 16-17, 2026)

Curated from the latest arXiv submissions across cs.AI, cs.LG, cs.IR.

### 14.1 CTR / Recommendation (New Submissions)

#### Long-History User Transformers for Real-Time Ad Ranking
- **Authors**: Viacheslav Ovchinnikov et al. (Yandex)
- **arXiv**: 2607.14331
- (Details in 13.2 above)

#### TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search
- **Authors**: Zhentao Song et al. (Alibaba)
- **arXiv**: 2607.13398
- (Details in 13.2 above)

#### Privacy Preserving Recommender Systems
- **Authors**: Ranjeet K Jha, Venkata Suresh Gummadilli
- **arXiv**: 2607.13328
- **Key Innovation**: Framework combining federated learning, differential privacy (ε≈5), cohort-level modeling, and privacy-aware agents. Evaluates MF, NCF, and GRU4Rec under varying privacy budgets.
- **Significance**: Practical reference for GDPR/CCPA-compliant deployment.

#### Mutable Low-Rank Sketches for Retrain-Free Recommendation
- **Authors**: Hector J. Garcia, Nick Clayton
- **arXiv**: 2607.15242
- **Key Innovation**: Low-rank sketch method avoiding full retraining — enables continual adaptation with mutable representations.
- **Significance**: Addresses growing concern about retraining costs in large-scale rec systems.

### 14.2 AI Agents (New Submissions)

#### SearchOS-V1
- **arXiv**: 2607.15257
- (Details in 13.8)

#### AutoSynthesis
- **arXiv**: 2607.15247
- (Details in 13.8)

#### Proof-or-Stop
- **arXiv**: 2607.14890
- (Details in 13.8)

#### Atrex-Bench: LLM-Generated GPU Kernels
- **Authors**: Lingyun Yang et al. (Alibaba)
- **arXiv**: 2607.14541
- (Details in 13.5)

### 14.3 ML Systems & Methods (New Submissions)

#### PolyQ: End-to-End Quantization for Edge CPU LLM Inference
- **Authors**: Hyunwoo Oh et al.
- **arXiv**: 2607.14618
- **Key Innovation**: Codesign framework for edge CPU LLM inference. Accepted at ICCAD 2026.
- **Significance**: Edge deployment aligns with on-device AI trend (Apple AFM, Phi-4 on-device).

#### xHC: Expanded Hyper-Connections
- **Authors**: Xiangdong Zhang, Xiaohan Qin et al.
- **arXiv**: 2607.14530
- **Key Innovation**: Expanded Hyper-Connections architecture — novel architectural building block for transformer scaling.

#### Muse: Representation Geometry of Muon
- **Authors**: Da Chang, Qiankun Shi et al.
- **arXiv**: 2607.14536
- **Key Innovation**: Analyzes the Muon optimizer's representation geometry beyond normalized momentum view. Deepens understanding of why Muon works.
- **Significance**: Muon is gaining significant adoption (modded-nanogpt, ICLR 2026 HM).

### 14.4 Advertising (New Submissions)

#### Adaptive Ad Load Design
- **arXiv**: 2607.14418
- (Details in 13.9)

#### ToolRec: On-Device Query Recommendation
- **Authors**: Zihan Luo et al. (OPPO)
- **arXiv**: 2607.08466
- (Details in 13.9)

---

## 15. Key Trends & Insights

### 15.1 CTR & Recommendation: The Great Unification
1. **From DLRM → Transformer → Generative**: CTR models are evolving from traditional DLRMs to Transformer architectures and now to generative models that directly output item sequences (OneRanker, GR4AD, EGA-V1).
2. **Scaling Laws Established**: Multiple papers (EST, FAT, DeRes, SparseCTR) confirm CTR models follow power-law scaling. Compute-AUC scaling curves are now routine.
3. **Long Sequence Processing**: 10K-length sequences are production reality (Douyin, Taobao, Kuaishou). Cross-attention (STCA) and offline-online decoupling (Yandex LH-UT) are key techniques.
4. **Diffusion for Interest Modeling**: Diffusion models are entering CTR for interest generation (DiffuMIN, CBD) with strong results.
5. **LLM Integration Deepens**: LLMs are used for knowledge enrichment (DMGIN), reasoning-enhanced representations (ReaSeq), and as backbones for CTR (GRAB, CADET).

### 15.2 LLM & Agent Systems: Reasoning at Scale
1. **Self-Play for Reasoning**: Games provide unlimited curriculum. SPIRAL, TiG, FMSP show transfer from game skills to general reasoning.
2. **GRPO vs SFT debate**: The Scalpel vs. Hammer paper reveals RL "amplifies" while SFT "replaces" — explaining generalization differences.
3. **Safety-Robustness Tradeoffs**: LoRA preserves reasoning during safety alignment. InTRO enables token-level rationality control.
4. **Self-Evolving Agents**: AReaL2.0, AgentX, and skill-optimization papers point toward agents that improve autonomously.
5. **Verification Gap**: Proof-or-Stop and the software verification literature address the critical need for agent trustworthiness.

### 15.3 Game AI
1. **Foundation Models for Games**: NitroGen (NVIDIA, 40K hrs, 1000+ games) represents a step toward generalist game-playing agents.
2. **Self-Play Transfers to Reasoning**: SPIRL and TiG demonstrate that game-based RL training improves general LLM reasoning.
3. **Multiplayer World Models**: First multiplayer world models enable game simulation at 20 FPS on single GPU.

### 15.4 Code Generation
1. **Self-Execution Simulation**: Models learn to simulate execution internally, reducing reliance on external test harnesses.
2. **Dual Execution**: Code + pseudocode execution (DUET) provides robustness through majority voting.
3. **Production Readiness**: Industry benchmarks (IndustryCode, EvoCodeBench) reveal gap between frontier models and human performance (~68% on sub-problems, ~20% on repo-level).

### 15.5 Generative Models & Sequential Modeling
1. **Linear RNNs + Sparse Memory**: Mamba-3, Sparse Delta Memory match or approach attention at scale with linear complexity.
2. **Hybrid Architectures**: Oryx switches between attention and recurrence within a sequence — best of both worlds.
3. **Next-Scale Prediction**: NextFlow replaces raster-scan with next-scale for images, achieving 5-second 1024×1024 generation.

### 15.6 Emerging Themes Across All Areas
1. **Open-source collectives**: SMACS shows 15 open models beat closed-source via collaboration routing
2. **Scaling law scrutiny**: "The Wall" paper challenges scaling orthodoxy; Shannon Scaling Law provides information-theoretic limits
3. **On-device AI**: PolyQ, ToolRec (OPPO), and Apple AFM demonstrate edge deployments reaching 150M+ MAU
4. **Agentic infrastructure**: SearchOS, AutoSynthesis, Proof-or-Stop, and Atrex form infrastructure layer for agent trust
5. **Diffusion everywhere**: From image/video generation → CTR interest modeling → auto-bidding → code generation

---

## Stats Summary

| Category | ICML | NeurIPS | ICLR | AAAI | KDD | CVPR | ACL | SIGIR | WWW | RecSys | arXiv | Total |
|----------|------|---------|------|------|-----|------|-----|-------|-----|--------|-------|-------|
| LLM & Reasoning | 4 | 4 | 3 | 5 | 0 | 0 | 3 | 0 | 0 | 0 | 12 | 31 |
| CTR & Ranking | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 2 | 2 | 15 | 25 |
| Recommendation | 0 | 0 | 0 | 2 | 3 | 0 | 2 | 4 | 1 | 4 | 12 | 28 |
| Agents & Systems | 3 | 0 | 1 | 2 | 0 | 0 | 3 | 2 | 0 | 0 | 8 | 19 |
| Game AI | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 7 | 8 |
| Code Generation | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 6 | 8 |
| Generative Models | 3 | 1 | 2 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 3 | 13 |
| Sequential Modeling | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 8 |
| Advertising/Auction | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 10 |
| **Total** | **10** | **5** | **6** | **9** | **9** | **5** | **10** | **6** | **3** | **6** | **81** | **150** |

---

*Generated: 2026-07-17. Sources: ICML 2026 proceedings, NeurIPS 2025 proceedings, ICLR 2026 proceedings, AAAI 2026 proceedings, KDD 2026 proceedings, CVPR 2026 proceedings, ACL 2026 proceedings, SIGIR 2026 proceedings, WWW 2026 proceedings, RecSys 2025 proceedings, CIKM 2025 proceedings, arXiv cs.AI/cs.LG/cs.IR.*
