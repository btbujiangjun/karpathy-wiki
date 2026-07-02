---
title: arXiv AI Research Roundup — July 2, 2026
type: synthesis
created: 2026-07-02
updated: 2026-07-02
sources: []
tags: [arxiv, survey, llm, recommendation, ctr, reinforcement-learning, multi-agent, transformers, optimization]
---

# arXiv AI Research Roundup — July 2, 2026

A curated selection of recent arXiv preprints across AI, LLMs, recommendation systems, CTR prediction, games, and reinforcement learning.

---

## 1. LLM Training & Optimizers

### Spectra: Rethinking Optimizers for LLMs Under Spectral Anisotropy
- **Authors**: — (submitted Feb 2026)
- **Link**: [arXiv:2602.11185](https://arxiv.org/abs/2602.11185)
- **Key Innovation**: Identifies that gradient signals in LLM training are highly anisotropic, with ~1.5% of spectral directions dominating optimizer statistics. Proposes Spectra, a spike-aware optimizer that suppresses dominant low-rank spike subspace without amplifying noise-sensitive tail. On LLaMA3-8B (50B tokens), reaches target loss **30% faster** than AdamW, cuts optimizer-state memory by **49.25%**, and improves avg accuracy by **1.62%**. Compared to Muon, is **5.1× faster** in optimizer processing.

### Muown: Row-Norm Control for Muon Optimization
- **Authors**: — (submitted May 2026)
- **Link**: [arXiv:2605.10797](https://arxiv.org/abs/2605.10797)
- **Key Innovation**: Diagnoses spectral norm drift in Muon as driven by row-magnitude (not row-coherence). Proposes Muown, a drop-in replacement that treats row-magnitude as an explicit optimizer variable under ℓ∞ geometry. Improves perplexity over Muon, SOAP, AdamW, Lion across 124M–2.7B GPT-style models on FineWeb-Edu.

### Accelerating LLM Pre-Training through Flat-Direction Dynamics Enhancement (LITE)
- **Authors**: Shuchen Zhu, Rizhen Hu, Mingze Wang, Mou Sun, Xue Wang, Kun Yuan et al. (Feb 2026)
- **Link**: [arXiv:2602.22681](https://arxiv.org/abs/2602.22681)
- **Key Innovation**: Unifies adaptive optimizers under a Riemannian ODE framework showing preconditioner ≈ Riemannian geometry + momentum ≈ damping. Proposes LITE to apply larger Hessian damping along flat trajectories. Accelerates both Muon and SOAP across Dense/MoE architectures (130M–1.3B), achieving **2× speedup** in long-horizon training.

### Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training
- **Authors**: — (submitted Mar 2026)
- **Link**: [arXiv:2603.17970](https://arxiv.org/abs/2603.17970)
- **Key Innovation**: Replaces Muon's Newton-Schulz polar decomposition with triangular whitening (Gauss-Seidel-like solves), reducing FLOPs ~12× per step. Achieves fixed validation perplexity **10–50% faster** than tuned AdamW/Muon across GPT-2 small/medium/large. Improves tokens/s by **1.3–2.6×** over Muon.

### Spectral Scaling Laws of Muon
- **Authors**: — (submitted Jun 2026)
- **Link**: [arXiv:2606.04058](https://arxiv.org/abs/2606.04058)
- **Key Innovation**: First systematic study of singular value spectra of Muon's momentum buffers across model scales (77M–2.8B). Finds stabilization values follow clean power laws per layer. Some late layers scale aggressively (up to M⁻⁰·⁹⁶), indicating NS iteration count must increase at frontier scale. Provides a principled recipe for minimum NS configuration.

### Rethinking Language Model Scaling under Transferable Hypersphere Optimization (HyperP)
- **Authors**: — (submitted Mar 2026)
- **Link**: [arXiv:2603.28743](https://arxiv.org/abs/2603.28743)
- **Key Innovation**: First framework transferring optimal LR across width/depth/tokens/MoE granularity under Frobenius-sphere constraint with Muon. Proves weight decay is first-order no-op on the sphere. Single base LR transfers across compute budgets, yielding **1.58× compute efficiency** over strong Muon baseline at 6e21 FLOPs.

### HTMuon: Improving Muon via Heavy-Tailed Spectral Correction
- **Authors**: — (submitted Mar 2026)
- **Link**: [arXiv:2603.10067](https://arxiv.org/abs/2603.10067)
- **Key Innovation**: Argues Muon's orthogonalized update suppresses heavy-tailed weight spectra. Proposes HTMuon to produce heavier-tailed updates. On LLaMA pretraining (C4), reduces perplexity by **up to 0.98** over Muon. Theoretically corresponds to steepest descent under Schatten-q norm.

### Fast Catch-Up, Late Switching: Optimal Batch Size Scheduling via Functional Scaling Laws
- **Authors**: Jinbo Wang, Binghui Li, Zhanpeng Zhou, Mingze Wang et al. (Feb 2026)
- **Link**: [arXiv:2602.14208](https://arxiv.org/abs/2602.14208)
- **Key Innovation**: Characterizes optimal batch size scheduling (BSS) via functional scaling laws. For hard tasks, optimal BSS maintains small batches most of training then switches late. Late-switch schedules consistently outperform constant-batch baselines across dense and MoE LLMs up to 1.1B / 1T tokens.

---

## 2. LLM-Based Recommendation

### From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation in Production
- **Authors**: Yucheng Shi, Ying Li, Yu Wang, Yesu Feng, Arjun Rao, Rein Houthooft, Shradha Sehgal, Jin Wang, Hao Zhen, Ninghao Liu, Linas Baltrunas (Feb 2026)
- **Link**: [arXiv:2602.20558](https://arxiv.org/abs/2602.20558)
- **Key Innovation**: Uses RL to train a verbalization agent that transforms raw interaction logs into optimized textual contexts for LLM recommenders. On large-scale industrial streaming data, achieves **up to 93% relative improvement** in discovery item recommendation accuracy over template-based baselines.

### Reasoning to Rank: An End-to-End Solution for Exploiting LLMs for Recommendation
- **Authors**: Kehan Zheng, Deyao Hong, Qian Li, Jun Zhang, Huan Yu, Jie Jiang et al. (Feb 2026)
- **Link**: [arXiv:2602.12530](https://arxiv.org/abs/2602.12530)
- **Key Innovation**: End-to-end training framework that internalizes recommendation utility optimization into step-by-step LLM reasoning. Performs reasoning at user-item level and uses RL for training. Consistent gains on 3 Amazon datasets + large-scale industrial dataset.

### Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation
- **Authors**: — (Feb 2026, v3)
- **Link**: [arXiv:2602.07298](https://arxiv.org/abs/2602.07298)
- **Key Innovation**: First demonstration of robust power-law scaling for LLMs continually pre-trained on recommendation-specific synthetic data. SasRec trained on synthetic data outperforms real-data model by **+130% on Recall@100**. Scaling law L(D)=L∞+A·D^−α observed across 0.6B–8B models on 163B tokens.

### R³-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs over Multi-Granular Interest Signals
- **Authors**: — (submitted Mar 2026)
- **Link**: [arXiv:2603.13730](https://arxiv.org/abs/2603.13730)
- **Key Innovation**: Unifies multi-level user intent reasoning, item semantic extraction, long-short interest polarity mining, and similar user collaborative enhancement. Up to **+10.2% HR@1** and **+6.4% HR@5** on ML-1M, Games, Bundle datasets.

### Internalizing Multi-Agent Reasoning for Accurate and Efficient LLM-based Recommendation (STAR)
- **Authors**: Yang Wu, Hao Wang, Qian Li, Jun Zhang, Huan Yu, Jie Jiang (Feb 2026)
- **Link**: [arXiv:2602.09829](https://arxiv.org/abs/2602.09829)
- **Key Innovation**: Multi-agent teacher (with Collaborative Signal Translation) distills reasoning into a compact single-agent STAR model via trajectory-driven distillation. STAR surpasses its teacher by **8.7–39.5%** while eliminating iterative latency.

### From Token to Item: Enhancing LLMs for Recommendation via Item-aware Attention Mechanism (IAM)
- **Authors**: — (submitted Mar 2026)
- **Link**: [arXiv:2603.19693](https://arxiv.org/abs/2603.19693)
- **Key Innovation**: Categorizes token relations into intra-item (content semantics) and inter-item (collaborative relations). Proposes IAM with dual complementary attention layers, explicitly modeling item-level collaborative relations. Consistent SOTA across multiple public datasets.

### User Simulator-Guided Multi-Turn Preference Optimization (SMTPO) for Reasoning LLM-based Conversational Recommendation
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.03671](https://arxiv.org/abs/2604.03671)
- **Key Innovation**: Uses an LLM-based user simulator to generate high-quality natural language feedback, with Reasoning LLM as recommender backbone. Two-stage SFT+RL training enables multi-turn preference optimization filtering noisy feedback.

---

## 3. Generative Recommendation & Semantic IDs

### GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.14878](https://arxiv.org/abs/2604.14878)
- **Key Innovation**: Deployed on JD.com. Proposes Page-wise NTP (next-token prediction) task, asymmetric Linear Token Merger (~2× prompt compression), and GRPO-SR with hybrid rewards. Month-long A/B test: **+9.5% clicks**, **+8.7% transactions** over existing pipeline.

### Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations
- **Authors**: — (submitted Jun 2026)
- **Link**: [arXiv:2606.08604](https://arxiv.org/abs/2606.08604)
- **Key Innovation**: Adds jointly trained item-level scoring alongside SID generation. Resolves miscalibrated beam search likelihoods and SID collisions. On industrial music service: **+3.7% Recall@1000** over vanilla GR. Replaced 15+ candidate generators in 7-day A/B test.

### CapsID: Soft-Routed Variable-Length Semantic IDs for Generative Recommendation
- **Authors**: — (submitted May 2026)
- **Link**: [arXiv:2605.05096](https://arxiv.org/abs/2605.05096)
- **Key Innovation**: Replaces hard RQ-VAE with capsule routing — items probabilistically route to multiple semantic capsules, SID terminates when confidence is high. +SemanticBPE composes adjacent tokens. **+9.6% Recall@10** over ReSID on Amazon benchmarks; 51% inference latency of COBRA-style systems.

### End-to-End Semantic ID Generation for Generative Advertisement Recommendation (UniSID)
- **Authors**: Jie Jiang, Xinxun Zhang, Enming Zhang et al. (Feb 2026)
- **Link**: [arXiv:2602.10445](https://arxiv.org/abs/2602.10445)
- **Key Innovation**: Jointly optimizes embeddings and SIDs end-to-end, addressing objective misalignment and error accumulation from two-stage RQ. Multi-granularity contrastive learning + summary-based ad reconstruction. **Up to 4.62% improvement** in Hit Rate.

### Deep Interest Mining with Cross-Modal Alignment for Semantic ID Generation (DeepInterestGR)
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.20861](https://arxiv.org/abs/2604.20861)
- **Key Innovation**: Uses VLMs to align non-textual modalities into unified text-based semantic space; deep interest mining via reconstruction; quality-aware RL to encourage semantically rich SIDs.

### SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
- **Authors**: Yang Yu, Lei Kou, Huaikuan Yi, Bin Chen et al. (Feb 2026)
- **Link**: [arXiv:2602.22913](https://arxiv.org/abs/2602.22913)
- **Key Innovation**: Multi-view alignment mapping semantics + item entities into unified latent space. Hybrid item tokenization (SID prefix + unique ID). Large-scale multi-task SFT dataset. Three-step generation with adaptive probabilistic fusion. Validated via online A/B tests on AliExpress.

### Reasoning over Semantic IDs Enhances Generative Recommendation (SIDReasoner)
- **Authors**: Yingzhi He, Yan Sun, Junfei Tan et al. (Mar 2026)
- **Link**: [arXiv:2603.23183](https://arxiv.org/abs/2603.23183)
- **Key Innovation**: Two-stage framework eliciting reasoning over SIDs by strengthening SID-language alignment via multi-task training on teacher-synthesized corpus.

### LASAR: Latent Adaptive Semantic Aligned Reasoning for Generative Recommendation
- **Authors**: — (submitted May 2026)
- **Link**: [arXiv:2605.10207](https://arxiv.org/abs/2605.10207)
- **Key Innovation**: First latent reasoning (continuous hidden-state) framework for generative recommendation. CoT semantic alignment + step-wise bidirectional KL + GRPO-based RL with terminal KL. **~20× faster** than explicit CoT text generation. Nearly halves latent step count.

---

## 4. CTR Prediction

### Length-Adaptive Interest Network (LAIN) for CTR Prediction
- **Authors**: — (submitted Jan 2026)
- **Link**: [arXiv:2601.19142](https://arxiv.org/abs/2601.19142)
- **Key Innovation**: Plug-and-play framework addressing attention polarization from length heterogeneity. Spectral Length Encoder + Length-Conditioned Prompting + Length-Modulated Attention. **Up to 1.15% AUC gain**, 2.25% log loss reduction. Significantly improves short-sequence users without sacrificing long-sequence accuracy.

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer et al. (Feb 2026)
- **Link**: [arXiv:2602.11410](https://arxiv.org/abs/2602.11410)
- **Key Innovation**: Decoder-only Transformer architecture for ads CTR prediction conditioned on page/session context.

### IDProxy: Cold-Start CTR Prediction with Multimodal LLMs at Xiaohongshu
- **Authors**: — (submitted Mar 2026)
- **Link**: [arXiv:2603.01590](https://arxiv.org/abs/2603.01590)
- **Key Innovation**: Leverages multimodal LLMs to proxy ID-based cold-start items, deployed on Xiaohongshu's highly optimized industrial CTR system.

### FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
- **Authors**: — (submitted May 2026)
- **Link**: [arXiv:2605.01726](https://arxiv.org/abs/2605.01726)
- **Key Innovation**: Discovers user attention scores exhibit distinct spectral entropy distributions conditioned on positive vs. negative targets. Proposes dual-branch (time + frequency) architecture with target-aware spectrum filtering. Consistent SOTA across 3 public datasets.

### Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao et al. (Renmin Univ. & ByteDance & Meituan, Jan 2026)
- **Link**: [arXiv:2606.04944](https://arxiv.org/abs/2606.04944)
- **Key Innovation**: Two MLP components — main (explicit interactions via distillation from teachers) + parallel (implicit interactions). Alignment via batch normalization + direct task supervision. Simple, efficient, scalable.

### Generative Recommendation for Large-Scale Advertising
- **Authors**: — (submitted Feb 2026, v2)
- **Link**: [arXiv:2602.22732](https://arxiv.org/abs/2602.22732)
- **Key Innovation**: Generative retrieval paradigm applied to large-scale advertising systems.

### AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors**: Changxin Lao, Fei Pan, Guozhuang Ma et al. (Kuaishou, Jun 2026)
- **Link**: [arXiv:2606.26859](https://arxiv.org/abs/2606.26859)
- **Key Innovation**: Production-deployed multi-agent system that autonomously generates, implements, evaluates, and learns from recommendation experiments. Storm Agent → Design Agent → Evaluation Agent → Harness Evolution (SGPO). Turned 374 ideas into $100M+ annualized revenue. Replaces linear human effort with compounding gains.

---

## 5. Multi-Agent Systems, Games & RL

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: — (submitted May 2026)
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)
- **Key Innovation**: Adapted PPO with lightweight turn-level critic for VLM-based game agents in Super Mario Land (100+ turns). Achieves **3× average game progress** over frontier models. Turn-level critic drastically reduces memory/compute vs. token-level critics.

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: — (submitted Jun 2025, v3)
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)
- **Key Innovation**: Self-play on two-player zero-sum language games. Fully online multi-turn multi-agent RL with distributed actor-learner architecture. Role-conditioned Advantage Estimation (RAE) stabilizes training. Generates unlimited training data through game dynamics.

### Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.17696](https://arxiv.org/abs/2604.17696)
- **Key Innovation**: Selectively reinforces trajectories via Reasoning Transferability Coefficient (abstract/domain-agnostic) and Reasoning Evolution Reward (adaptive reasoning across turns). Strong gains on competition-level mathematics and code generation.

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: — (submitted May 2026)
- **Link**: [arXiv:2605.04906](https://arxiv.org/abs/2605.04906)
- **Key Innovation**: Recursive reasoning paradigm where agent's reasoning integrates opponents' reasoning processes. Centralized CoT comparison module for intermediate reasoning evaluation. **22.1% average improvement** across multi-agent games.

### T-STAR: Tree-structured Self-Taught Agent Rectification for Multi-turn Agent Policy Optimization
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.07165](https://arxiv.org/abs/2604.07165)
- **Key Innovation**: Consolidates trajectories into Cognitive Tree, enabling Introspective Valuation (variance-reduced step-level advantage) and In-Context Thought Grafting (contrasting successful/failed branches). Surgical Policy Optimization using Bradley-Terry loss at critical divergence points.

### From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning
- **Authors**: Chao Chen, Chengzu Li, Zhiwei Li et al. (HKUST GZ & Cambridge, Jun 2026)
- **Link**: [arXiv:2606.17682](https://arxiv.org/abs/2606.17682)
- **Key Innovation**: Current RL policy model analyzes failure trajectories and proposes modifications to next-stage training environment configuration (LLM-as-Environment-Engineer). MAPF-FrozenLake testbed. The RL checkpoint itself serves as best environment engineer.

### LangMARL: Natural Language Multi-Agent Reinforcement Learning
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.00722](https://arxiv.org/abs/2604.00722)
- **Key Innovation**: Brings credit assignment + policy gradient from cooperative MARL into language space. Language Policy Actors + Centralized Language Critic + Language Policy Gradient Estimator + Language Policy Optimizer. Interpretable, sample-efficient.

### Cooperation and Exploitation in LLM Policy Synthesis for Sequential Social Dilemmas
- **Authors**: Víctor Gallego (Mar 2026)
- **Link**: [arXiv:2603.19453](https://arxiv.org/abs/2603.19453)
- **Key Innovation**: Studies LLM generating Python policy functions for multi-agent environments, refined via self-play. Dense feedback (reward + social metrics) consistently outperforms sparse. Characterizes 5 attack classes for reward hacking.

### Competition and Cooperation of LLM Agents in Games
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.00487](https://arxiv.org/abs/2604.00487)
- **Key Innovation**: Studies LLM agents in network resource allocation and Cournot competition games. Finds agents tend to cooperate when given multi-round prompts and non-zero-sum context. Fairness reasoning is central.

### Coalition Formation in LLM Agent Networks: Stability Analysis and Convergence Guarantees
- **Authors**: — (submitted Apr 2026)
- **Link**: [arXiv:2604.14386](https://arxiv.org/abs/2604.14386)
- **Key Innovation**: First framework grounding coalition formation in hedonic game theory. LLM Coalition Formation Game (LCFG) with Nash-stable partition guarantees. Coalition-of-Thought (CoalT) protocol achieves 73.2% Nash stability vs. 41.8% standard prompting.

### Multi-Agent Fictitious Play (MAFP) for Enhancing Decision-Making with LLMs
- **Authors**: — (submitted Jun 2026)
- **Link**: [arXiv:2606.19308](https://arxiv.org/abs/2606.19308)
- **Key Innovation**: Addresses stance entanglement in decision-making via game-theoretic fictitious play. Agents iteratively best-respond to empirical mixture of others' past decisions. Outperforms single-round and multi-round baselines on tournament strength and robustness.

### TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning
- **Authors**: — (submitted May 2026)
- **Link**: [arXiv:2605.28699](https://arxiv.org/abs/2605.28699)
- **Key Innovation**: Separates collaborative decision into controller-regret layer (speak/skip via regret matching) and generation-credit layer (role-specific GSPO rewards). Extends classical game theory to DL with mathematically rigorous convergence.

### MARO: Multi-Agent Reward Optimization for Stronger Reasoning from Social Interaction
- **Authors**: — (submitted Jan 2026, v2)
- **Link**: [arXiv:2601.12323](https://arxiv.org/abs/2601.12323)
- **Key Innovation**: Decomposes sparse terminal outcomes into per-behavior rewards; handles uneven role distribution; evaluates utility of each behavior directly. Social reasoning improvements transfer to mathematical reasoning and instruction following.

### Agentic Transformers Provably Learn to Search via Reinforcement Learning
- **Authors**: Tong Yang, Yu Huang, Yingbin Liang, Yuejie Chi (May 2026)
- **Link**: [arXiv:2606.00183](https://arxiv.org/abs/2606.00183)
- **Key Innovation**: Provable analysis that transformers can learn to perform search via RL. Theoretical guarantees on in-context search capabilities.

---

## Cross-Cutting Themes

| Theme | Papers |
|-------|--------|
| Muon optimizer variants & analysis | Spectra, Muown, MUD, Spectral Scaling Laws, HyperP, HTMuon, LITE |
| RL for LLM reasoning | Odysseus, SPIRAL, Stratagem, Strat-Reasoner, T-STAR, MARO |
| Generative recommendation / Semantic IDs | GenRec, Gryphon, CapsID, UniSID, DeepInterestGR, SIGMA, SIDReasoner, LASAR |
| LLM-based recommenders | Logs-to-Language, Reasoning-to-Rank, STAR, IAM, SMTPO, R³-REC, Scaling Laws |
| CTR prediction | LAIN, CADET, IDProxy, FEDIN, DS-MLP |
| Multi-agent systems | AgentX, LangMARL, Coalition Formation, MAFP, TRACER, Competition&Cooperation |
| Training data & scaling | Synthetic Data Scaling Laws, BSS via FSL, Quality-Aware Data Scheduling |
