---
title: "arXiv Daily — June 6, 2026"
type: synthesis
created: 2026-06-06
updated: 2026-06-06
sources: []
tags: [arxiv, daily, llm, ctr, recommendation, games, rl]
---

# arXiv Daily — June 6, 2026

Recent papers across AI, LLMs, recommendation, advertising, CTR, sequential modeling, and games.

---

## LLM Architectures & Inference

### 1. FLARE: Diffusion for Hybrid Language Model
- **Authors:** Yuchen Zhu, Jing Shi, Chongjian Ge, Hao Tan, Yiran Xu, Wanrong Zhu, Jason Kuen, Koustava Goswami, Rajiv Jain, Yongxin Chen, Molei Tao, Jiuxiang Gu
- **Institution:** Adobe Research, Georgia Institute of Technology
- **Abstract:** Presents FLARE, a systematic recipe for converting hybrid-attention AR LLMs into capable and serving-efficient diffusion LLMs (dLLMs) under a practical training budget. Examines the full conversion pipeline from transfer-data construction and loss-mask design to hybrid-backbone training and serving-time inference.
- **Key Innovations:**
  - Transfer diagnosis identifying data quality as dominant factor for preserving AR capability
  - Hardware-aware algorithms for linear attention under diffusion-specific visibility patterns
  - Unified inference system supporting both AR-style verified decoding and diffusion-style parallel denoising
  - FLARE-2B/4B/9B achieves competitive dLLM quality from Qwen3.5 checkpoints
- **Link:** https://arxiv.org/abs/2606.01774

### 2. Entropy Gate: Entropy Quenching for Near-Lossless Token Compression in LLM Pipelines
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Introduces Entropy Gate, a token compression framework applying entropy quenching — a thermodynamic process that progressively freezes out low-energy tokens while preserving semantic fidelity. Achieves 40–60% compression across five prompt categories with fidelity >0.80. Stateless, model-agnostic, deployable as an OpenAI-compatible HTTP proxy.
- **Key Innovations:**
  - Multi-factor information energy combining statistical, structural, and positional components
  - Provable fidelity guarantees via energy-weighted similarity threshold
  - Combined with external memory, achieves 88–96% total token reduction for agentic workloads
- **Link:** https://arxiv.org/abs/2606.03739

### 3. TreeFlash: Parallel AR-Approximation for Faster Speculative Decoding
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Proposes TreeFlash, a single-pass drafter incorporating a lightweight MLP-based AR-approximation mechanism to overcome the non-autoregressive conditioning problem of one-shot block drafters. Preserves O(1) decoding time complexity while improving block efficiency by 12% and speedup by 9% over marginal tree drafting.
- **Key Innovations:**
  - Two-stage approximation mechanism combining one-shot diffusion-style draft generation with lightweight AR correction
  - O(1) decoding time complexity maintained despite autoregressive approximation
  - State-of-the-art results on Qwen3 models across multiple datasets
- **Link:** https://arxiv.org/abs/2606.03819

### 4. Enhancing LLM Metacognition via Cognitive Pairwise Training
- **Authors:** Weitao Li, Hao Zhou, Xuanyu Lei, Fandong Meng, Yuanhang Liu, Jingyi Ren, Ante Wang, Xiaolong Wang, Yuanchi Zhang, Fuwen Luo, Guangwen Yang, Lin Gan, Weizhi Ma, Yang Liu
- **Institution:** Tsinghua University
- **Abstract:** Proposes Cognitive Pairwise Training (CPT), a metacognitive mid-training stage that turns pairwise comparisons over reasoning traces into a reusable alignment signal. At 14B, CPT+RL outperforms SFT+RL by +2.2 math-average points and +5.2 abstention-F1 points across five model scales and three model families.
- **Key Innovations:**
  - Pairwise reasoning-trace comparison as training signal (not surface-level refusal patterns)
  - Internalized reasoning-quality discrimination boundary
  - Transfers zero-shot to conflicting-source RAG scenarios
- **Link:** https://arxiv.org/abs/2606.00869

### 5. Siri: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Three-phase framework enabling agents to discover, validate, and internalize skills without external skill generators or inference-time skill banks. On ALFWorld and WebShop with Qwen2.5-7B-Instruct, Siri improves GiGPO from 0.908 to 0.930 and from 0.728 to 0.813 respectively.
- **Key Innovations:**
  - Self-Skill Mining from the policy's own successful rollouts
  - Advantage-Weighted Skill Internalization using trajectory-level and action-level credit
  - Skill-free inference — no skill bank, retrieval service, or external memory at deployment
- **Link:** https://arxiv.org/abs/2606.02355

### 6. Model-Native Computing Architecture
- **Authors:** Hai Lin
- **Institution:** Tsinghua University (Shenzhen International Graduate School)
- **Abstract:** Visionary survey establishing a systematic mapping between computer architecture concepts and model-native systems. Proposes the Intelligent Computing Architecture Model (ICAM) with six functional layers, a dual-plane architecture (probabilistic execution + deterministic control), and three quantitative design laws (Semantic Locality, Context Budget, Agent Speedup).
- **Key Innovations:**
  - Dual-plane architecture resolving "LLM as CPU vs. OS" debate
  - Three quantitative laws validated against published system-level data
  - Comprehensive survey connecting LLM-as-OS, memory management, agent frameworks, and safety governance
- **Link:** https://arxiv.org/abs/2606.00288

### 7. Inference Cost Attacks for Retrieval-Augmented Large Language Models
- **Authors:** N/A
- **Institution:** N/A (WWW '26)
- **Abstract:** Introduces RA-ICA, a novel attacking paradigm targeting computational cost of RAG-enhanced LLMs by injecting malicious documents into external knowledge corpus. Proposes CREEP framework using LLM agents with MA-GRPO (Memory-Augmented Group Relative Policy Optimization) to craft malicious documents. Increases token consumption by up to 13.12× with >90% success rate.
- **Key Innovations:**
  - First systematic attack on inference cost of RAG systems via knowledge base poisoning
  - MA-GRPO for fine-tuning attack agents
  - High success rate without degrading answer integrity
- **Link:** https://arxiv.org/abs/2606.02643

---

## Recommendation, CTR & Advertising

### 8. GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors:** N/A
- **Institution:** Kuaishou
- **Abstract:** Production-oriented generative recommender co-designed across architecture, learning, and serving for advertising. Proposes UA-SID tokenization, LazyAR decoder, VSL, and RSPO (Ranking-Guided Softmax Preference Optimization). Achieves up to 4.2% ad revenue improvement over DLRM-based stack. Deployed on Kuaishou with 400M+ users, <100ms latency, 500+ QPS per L20.
- **Key Innovations:**
  - UA-SID (Unified Advertisement Semantic ID) from fine-tuned MLLM embedding
  - LazyAR: lazy autoregressive decoder relaxing layer-wise dependencies
  - RSPO: ranking-aware, list-wise RL algorithm
  - Dynamic Beam Serving with traffic-adaptive beam search
  - Full production deployment at scale
- **Link:** https://arxiv.org/abs/2602.22732

### 9. EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling
- **Authors:** N/A
- **Institution:** Taobao/Alibaba
- **Abstract:** Proposes Efficiently Scalable Transformer (EST) unifying heterogeneous inputs within a single token sequence. Introduces Lightweight Cross-Attention (LCA) and Content Sparse Attention (CSA). Deployed on Taobao's display advertising, delivering 3.27% RPM increase and 1.22% CTR lift with clear power-law scaling.
- **Key Innovations:**
  - Fully unified sequence without lossy prior aggregation for CTR inputs
  - LCA focusing on most informative non-behavioral/behavioral interactions
  - CSA leveraging content similarity for sparse long-behavior modeling
  - Industrial deployment with verified scaling law
- **Link:** https://arxiv.org/abs/2602.10811

### 10. GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm
- **Authors:** N/A
- **Institution:** Baidu
- **Abstract:** End-to-end generative ranking framework for CTR prediction integrating Causal Action-aware Multi-channel Attention (CamA) mechanism. Proposes Sequence-Then-Sparse (STS) training. Full deployment on Baidu home feed delivers 3.05% revenue increase and 3.49% CTR lift with approximately linear scaling with sequence length.
- **Key Innovations:**
  - CamA: multi-channel, action-aware attention for temporal dynamics and user action signals
  - STS training decoupling dense parameters and sparse embeddings to address distribution shift
  - Monotonic AUC improvement with model capacity and behavior sequence length
- **Link:** https://arxiv.org/abs/2602.01865

### 11. RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems
- **Authors:** Yuchen Jiang et al.
- **Institution:** Tencent (Weixin)
- **Abstract:** Addresses representation collapse in deep recommender architectures. Proposes randomized permutation splitting over sparse features, multi-embedding paradigm, global token integration, and crossed pretrained embedding tokens. Full deployment across Weixin Video Accounts, Official Accounts, and Moments yields GMV improvements of 3.41%, 4.81%, and 2.12% respectively.
- **Key Innovations:**
  - Mitigates damped oscillatory effective-rank trajectory observed in deeper layers
  - Multi-embedding paradigm with randomized permutation splitting
  - Global token integration for richer cross-feature representations
  - Cold-start GMV improvement of 9.67% for new advertisements
- **Link:** https://arxiv.org/abs/2604.17878

### 12. HeMix: Query-Mixed Interest Extraction and Heterogeneous Interaction for Scalable CTR
- **Authors:** N/A
- **Institution:** AMAP (AutoNavi/Alibaba)
- **Abstract:** Scalable ranking model unifying adaptive sequence tokenization and heterogeneous interaction structure. Introduces Query-Mixed Interest Extraction and HeteroMixer block replacing self-attention. Deployed on AMAP platform with +3.61% GMV, +2.78% PV_CTR, and +2.12% UV_CVR over DLRM.
- **Key Innovations:**
  - Query-Mixed Interest Extraction with dynamic + fixed queries over global and real-time sequences
  - HeteroMixer block: multi-token fusion → heterogeneous interaction → group-aligned reconstruction
  - Favorable scaling behavior driven by HeteroMixer
- **Link:** https://arxiv.org/abs/2602.09387

### 13. Memento: Personalized RAG-Style Long-Retention Data Scaling for Online Ads Recommendation
- **Authors:** N/A
- **Institution:** Meta (Facebook)
- **Abstract:** Treats user engagement history as a document corpus and ad requests as queries, retrieving relevant interactions via MMR. Two applications: Representation Memento (inference-time feature augmentation) and Data Memento (training-time rehearsal). Sub-10ms latency, 1% CTR lift and 1.2% CVR lift, scaling personalization to 365+ days.
- **Key Innovations:**
  - RAG-style framing of long-retention data scaling in recommendation
  - MMR-based retrieval balancing similarity and diversity
  - Infrastructure co-design: temporal chunking, INT8 quantization, asynchronous serving
  - 5–10× resource efficiency over linear scaling
- **Link:** https://arxiv.org/abs/2605.24051

### 14. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors:** N/A
- **Institution:** LinkedIn
- **Abstract:** End-to-end decoder-only transformer for ads CTR prediction with context-conditioned decoding architecture, self-gated attention, timestamp-based RoPE, and session masking. Achieves 11.04% CTR lift over production LiRank baseline. Deployed on LinkedIn's homefeed sponsored updates.
- **Key Innovations:**
  - Multi-tower prediction heads explicitly modeling post-scoring contextual signals (ad position)
  - Self-gated attention for adaptive information flow regulation
  - Timestamp-based variant of Rotary Position Embedding
  - Session masking for train-serve skew prevention
  - Production engineering: tensor packing, sequence chunking, custom Flash Attention
- **Link:** https://arxiv.org/abs/2602.11410

---

## Games, RL & Sequential Decision Making

### 15. Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Addresses domain specificity and contextual stasis in game-based self-play for reasoning. Selectively reinforces trajectories exhibiting abstract reasoning via a Reasoning Transferability Coefficient (φ) and a Reasoning Evolution Reward (ψ). Training on three text-based games with Qwen3-4B-Base yields consistent improvements on math, general reasoning, and code benchmarks.
- **Key Innovations:**
  - Reasoning Transferability Coefficient measuring abstraction level of reasoning patterns
  - Reasoning Evolution Reward incentivizing adaptive reasoning across turns
  - Multiplicative advantage modulation: Amod = Agame · φ + β · ψ
  - Strong gains on competition-level mathematics
- **Link:** https://arxiv.org/abs/2604.17696

### 16. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO with lightweight turn-level critic, substantially improving stability over critic-free methods (GRPO, Reinforce++). Achieves at least 3× average game progress over frontier models with cross-game generalization.
- **Key Innovations:**
  - Lightweight turn-level critic (not large-model token-level) with positive-advantage filtering
  - Systematic investigation of algorithmic components for long-horizon VLM RL
  - Auto-curriculum via inverse trajectory weighting for multi-level training
  - Open training framework for practical VLM agents
- **Link:** https://arxiv.org/abs/2605.00347

### 17. Vintix II: Decision Pre-Trained Transformer is a Scalable In-Context Reinforcement Learner
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Extends Decision Pre-Trained Transformer (DPT) to diverse multi-domain continuous control environments with Flow Matching for capturing multi-modal action distributions. Trained across hundreds of tasks, achieves clear generalization gains on held-out test sets, outperforming prior Algorithm Distillation scaling.
- **Key Innovations:**
  - Flow Matching as training objective preserving DPT's Bayesian posterior sampling interpretation
  - First Large Action Model operating successfully in both zero-shot and few-demonstration regimes
  - 3.2× dataset expansion over prior cross-domain ICRL work
  - Fully parametric deployment (no retrieval modules needed)
- **Link:** https://arxiv.org/abs/2604.05112

### 18. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving selves. Proposes Role-Conditioned Advantage Estimation (RAE) for stability. Improves performance by up to 10% across 8 reasoning benchmarks on Qwen and Llama families, including benefits for DeepSeek-R1-Distill-Qwen-7B.
- **Key Innovations:**
  - Fully online, multi-turn, multi-agent RL system for LLMs with distributed actor-learner architecture
  - RAE normalizing rewards relative to each player's expected performance
  - Automatic curriculum through self-play (no human-curated problem-answer pairs)
  - Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields complementary cognitive patterns
- **Link:** https://arxiv.org/abs/2506.24119

### 19. MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** A single GPT-based model trained via offline RL on expert trajectories (400M SMACv2, 100M GRF, 1B POGEMA) with a transformer-based observation encoder requiring no task-specific tuning. Achieves competitive performance vs. specialized baselines across all environments.
- **Key Innovations:**
  - First single foundation model spanning multiple significantly different MARL environments
  - Flexible tokenization encoding feature type, agent identity, team affiliation, and temporal step
  - Shared encoder + actor-critic heads trained via behavior cloning and offline RL
- **Link:** https://arxiv.org/abs/2604.05943

### 20. Chessformer: A Unified Architecture for Chess Modeling
- **Authors:** N/A
- **Institution:** N/A
- **Abstract:** Encoder-only transformer representing board squares as tokens with Geometric Attention Bias (GAB). Advances state-of-the-art on three goals simultaneously: (1) Maia-3 achieves 57.1% human move-matching accuracy; (2) Integration into Leela Chess Zero adds 100+ Elo, leading to tournament victories over Stockfish; (3) Square-token design enables granular interpretability.
- **Key Innovations:**
  - Geometric Attention Bias: dynamic positional encoding adapting to chess-specific geometry
  - Attention-based source-destination policy head
  - Domain-aligned tokenization, positional encoding, and output design
  - Single architecture serving playing strength, human prediction, and interpretability
- **Link:** https://arxiv.org/abs/2605.19091

---

## Summary Statistics

| Area | Papers Highlighted |
|------|-------------------|
| LLM Architectures & Inference | 7 |
| Recommendation, CTR & Advertising | 7 |
| Games, RL & Sequential Decision Making | 6 |
| **Total** | **20** |
