---
title: arXiv AI Paper Search Report
type: synthesis
created: 2026-07-27
updated: 2026-07-27
tags: [arxiv, AI, LLM, recommendation, CTR, sequential-modeling, games, RL]
---

# arXiv AI Paper Search Report — 2026-07-27

Search scope: LLMs, recommendation systems, CTR prediction, advertising, sequential modeling, games, reinforcement learning.

---

## 1. LLM Reasoning & Architecture

### 1.1 PoTRE: Test-Time Reasoning inspired by Cognitive Heterogeneity

- **Authors**: (not specified in search result)
- **Institution/Company**: (not specified)
- **Date**: 2026-07-22
- **Abstract**: Introduces PoTRE (Poly-Topological Reasoning Ensembles), a heterogeneous framework that decouples inference into four agents: Adversarial Refinement Agent, Hierarchical Strategic Planning Agent, Spectrum Search Agent, and Direct Chain Agent. A Task-Adaptive Aggregation Layer reconciles these perspectives via candidate selection, semantic synthesis, or neuro-symbolic verification. Achieves 49.92% accuracy on HLE, surpassing previous best official score.
- **Key Innovations**: Heterogeneous multi-agent reasoning ensemble; four decoupled reasoning agents with adaptive aggregation; architectural heterogeneity achieves better reasoning with similar or fewer tokens vs. scaled homogeneous baselines.
- **Link**: https://arxiv.org/abs/2607.20268

### 1.2 MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

- **Authors**: Ruilin Tong et al.
- **Institution/Company**: (not specified)
- **Date**: 2026-07-08
- **Abstract**: Proposes MILES, a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under realistic test-time constraints. Maintains modular memory units with asymmetric pairs of sub-goal embeddings and sub-instructions, each with a learnable selection head. Coarse-to-fine retrieval mechanism enables memory expansion and learned reranking.
- **Key Innovations**: Modular instruction memory with learnable selection; coarse-to-fine retrieval for incremental test-time memory; correctness-optimized memory composition.
- **Link**: https://arxiv.org/abs/2607.06974

### 1.3 LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion LLMs

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2026-07-16
- **Abstract**: Proposes LaCache, a training-free acceleration framework for diffusion-based LLMs (DLLMs). Uses Lossless State Memoization (LSM) caching EmbedCache, RoPECache, and FACache to skip redundant computation on unchanged tokens. Integrates per-group FP8 quantization for FFN layers. Achieves up to 40.2x end-to-end speedup while maintaining comparable task accuracy.
- **Key Innovations**: Lossless state memoization for diffusion LLMs; three-tier caching (embedding, RoPE, FlashAttention); composable with existing acceleration methods for massive speedups.
- **Link**: https://arxiv.org/abs/2607.16339

### 1.4 LatentMT: Machine Translation with Latent Reasoning

- **Authors**: Wei-Rui Chen, Samar M. Magdy, et al.
- **Institution/Company**: (not specified)
- **Date**: 2026-07-21
- **Abstract**: First systematic study of latent-reasoning LoopLMs for machine translation. Adapts a 2.6B-parameter backbone with lightweight training. Across 32 translation directions, achieves performance comparable to models 3-5x larger. Shows recurrent computation improves translation quality in early steps then saturates. Requires lower training and inference compute than larger non-latent-reasoning models.
- **Key Innovations**: Latent recurrent computation for MT; scaling via hidden states rather than parameters or CoT tokens; efficiency advantage over explicit reasoning models.
- **Link**: https://arxiv.org/abs/2607.18618

### 1.5 In-Place Tokenizer Expansion for Pre-trained LLMs

- **Authors**: Jimmy T.H. Smith, Tarek Dakhran, Alberto Cabrera, et al.
- **Institution/Company**: (not specified)
- **Date**: 2026-07-16
- **Abstract**: Presents tokenizer expansion as an in-place recipe for upgrading a pre-trained model's tokenizer. Continues existing BPE merges on multilingual corpus, initializes new token embeddings as mean of source sub-token embeddings. Applied to LFM2-8B-A1B to produce LFM2.5-8B-A1B with 128K tokenizer. Achieves 2.2-3.7x per-character decode speedup for Hindi and Vietnamese.
- **Key Innovations**: In-place tokenizer expansion without retraining from scratch; mean initialization of new embeddings; two-stage adaptation (embedding-only then full-model).
- **Link**: https://arxiv.org/abs/2607.15232

### 1.6 L1 Augmented Attention as an Improved Vector Similarity Metric

- **Authors**: Kurt Godden
- **Institution/Company**: (not specified)
- **Date**: 2026-07-20
- **Abstract**: Introduces L1 augmented attention, subtracting a learned head-specific L1 distance between queries and keys from the dot product score. Combines directional alignment (dot product) with coordinate deviation penalties (L1). Achieves up to 14.5% perplexity reduction on WikiText 2.
- **Key Innovations**: Hybrid L1+dot-product similarity metric for attention; low-dimensional L1 projections for efficient computation; demonstrates head-level geometric specialization.
- **Link**: https://arxiv.org/abs/2607.18027

---

## 2. Recommendation Systems

### 2.1 Probabilistic Residual Learning for Online Recommendations (PRL)

- **Authors**: (not specified)
- **Institution/Company**: (RecSys '26 paper)
- **Date**: 2026
- **Abstract**: Causal Bayesian recommendation model that models the residual between ground-truth and base predictions. Probabilistically groups users for localized residual modeling, models domain-level confounders, and aggregates cluster-specific residual predictions using do-calculus. Plug-and-play framework compatible with DLRM, CDL, NCF, LightGCN.
- **Key Innovations**: Causal Bayesian residual learning; plug-and-play cross-domain enhancement; automatic user cluster discovery with causal debiasing.
- **Link**: https://arxiv.org/abs/2607.20863

### 2.2 Gryphon: Unified Architecture for Semantic-ID Generation and Item-Level Scoring

- **Authors**: Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov, Mariia Ulianova, Ilya Murzin
- **Institution/Company**: (Industrial music service)
- **Date**: 2026-06-07
- **Abstract**: Adds jointly trained item-level scoring alongside SID generation in encoder-decoder generative recommendation. Resolves generated SIDs to concrete items and re-scores directly, sidestepping miscalibrated sequence scores and SID collisions. In 7-day A/B test, replaced pipeline of 15+ candidate generators with no significant change in listening time while passing 66.7% fewer candidates.
- **Key Innovations**: Joint SID generation + item-level scoring in single forward pass; resolves SID collisions; eliminates preranking stage in production.
- **Link**: https://arxiv.org/abs/2606.08604

### 2.3 GLASS: Generative Recommender for Long-sequence Modeling via SID-Tier and Semantic Search

- **Authors**: Shiteng Cao et al.
- **Institution/Company**: (not specified)
- **Date**: 2026-02-05
- **Abstract**: Integrates long-term user interests into generative recommendation via SID-Tier (maps long interactions into unified interest vector for initial SID token prediction) and semantic hard search (uses generated coarse-grained SID as dynamic keys for relevant historical behaviors). Includes semantic neighbor augmentation and codebook resizing for data sparsity.
- **Key Innovations**: SID-Tier for long-sequence interest integration; semantic hard search for history retrieval; adaptive gated fusion for fine-grained token trajectory.
- **Link**: https://arxiv.org/abs/2602.05663

### 2.4 SIDReasoner: Reasoning over Semantic IDs for Generative Recommendation

- **Authors**: Yingzhi He, Yan Sun, Junfei Tan, Yuxin Chen, et al.
- **Institution/Company**: (not specified)
- **Date**: 2026-03-24
- **Abstract**: Two-stage framework that elicits reasoning over SIDs by strengthening SID-language alignment. First stage enhances SID-language alignment via multi-task training on enriched SID-centered corpus synthesized by teacher model. Second stage uses GRPO for outcome-based feedback to steer effective reasoning trajectories. Demonstrates strong cross-domain generalization.
- **Key Innovations**: SID-language alignment via multi-task training; teacher-assisted semantic expansion; GRPO-based RL for SID reasoning; cross-domain generalization.
- **Link**: https://arxiv.org/abs/2603.23183

### 2.5 R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2026
- **Abstract**: Prompt-centric, retrieval-augmented framework unifying Multi-level User Intent Reasoning, Item Semantic Extraction, Long-Short Interest Polarity Mining, Similar User Collaborative Enhancement, and Reasoning-based Interest Matching. Improvements up to +10.2% HR@1 and +6.4% HR@5 on ML-1M, Games, and Bundle datasets.
- **Key Innovations**: Multi-granular interest signal extraction; RAG-style similar-user retrieval; reasoning-based scoring with faithful rationales.
- **Link**: https://arxiv.org/abs/2603.13730

### 2.6 RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation

- **Authors**: (not specified)
- **Institution/Company**: (RecSys '26 paper)
- **Date**: 2026
- **Abstract**: RL-free framework that decouples reasoning from prediction in sequential recommendation. Context Compressor distills backbone hidden states into latent interests with diversity regularization. Recursive Reasoner refines interests in separate intermediate latent space. Deep supervision allows free adjustment of reasoning depth at inference.
- **Key Innovations**: Dual-state recursive reasoning (reasoning state separate from prediction); Interest Diversity Regularizer; inference-time depth adjustment without retraining.
- **Link**: https://arxiv.org/abs/2607.12945

### 2.7 UniRec: Bridging Expressive Gap between Generative and Discriminative Recommendation

- **Authors**: (not specified)
- **Institution/Company**: Shopee
- **Date**: 2026
- **Abstract**: Chain-of-Attribute (CoA) prefixes each SID sequence with structured attribute tokens (category, seller, brand) before SID decoding, recovering item-side feature crossing. Capacity-constrained SID suppresses token collapse. Conditional Decoding Context (CDC) injects scenario signals. Joint RFT and DPO framework aligns with business objectives. Deployed on Shopee with +5.37% PVCTR, +4.76% orders, +5.60% GMV.
- **Key Innovations**: Chain-of-Attribute for generative recommendation; capacity-constrained SID quantization; conditional decoding context; RFT+DPO alignment.
- **Link**: https://arxiv.org/abs/2604.12234

### 2.8 GenAIR: Generative Archetype-Grounded Item Representations

- **Authors**: Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, et al.
- **Institution/Company**: (WWW '26 paper)
- **Date**: 2026-04-09
- **Abstract**: Uses LLM to analyze item metadata and infer archetype (conceptual profile of item's ideal target audience). Behavioral calibration objective grounds generative representations in real interaction patterns. Model-agnostic framework that integrates with most sequential recommendation models.
- **Key Innovations**: Archetype-grounded item representations via LLM; behavioral calibration for grounding in real interactions; seamless integration with existing models.
- **Link**: https://arxiv.org/abs/2606.11023

### 2.9 HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequential Recommendation

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2026-02-20
- **Abstract**: Hybrid attention architecture that decouples long-term stable preferences (linear attention) from short-term intent spikes (softmax attention). Temporal-Aware Delta Network (TADN) dynamically upweights fresh behavioral signals. Maintains linear inference speed while delivering over 8% Hit Rate improvement for users with ultra-long sequences.
- **Key Innovations**: Hybrid linear+softmax attention for long sequences; Temporal-Aware Delta Networks with exponential gating; linear complexity with restored precision.
- **Link**: https://arxiv.org/abs/2602.18283

### 2.10 CMSL: Constructive Multi-Sequence Learning for Recommendation Systems

- **Authors**: Zikun Cui, Renzhi Wu, et al.
- **Institution/Company**: Meta
- **Date**: 2026-07-15
- **Abstract**: Replaces monolithic history modeling with learned context construction. Learnable Sequence Construction Module disentangles user history into multiple coherent latent sequences (addressing "context pollution"). Linear attention mechanism for scalable multi-sequence modeling. Deployed across ranking and retrieval at Meta on four major surfaces.
- **Key Innovations**: Constructive multi-sequence paradigm (context engineering for recs); implicit context engineering via latent space disentanglement; scalable linear attention for multi-streams.
- **Link**: https://arxiv.org/abs/2606.28533

### 2.11 Beyond Item IDs: Semantic-Native Long Sequence Modeling for Short-Form Video

- **Authors**: Ruixiao Sun, Diego Uribe Mora, et al.
- **Institution/Company**: (billion-user platform)
- **Date**: 2026-07-15
- **Abstract**: Adopts content-native Semantic IDs via RQ-VAE with depth-truncated coarse-grained SIDs. Global-Aware Compression Transformer with non-parametric temporal folding condenses sequences. Order-of-magnitude reduction in peak memory. Online gains in satisfied watch time (+1.42%), satisfied views (+1.08%), actively engaged users (+0.52%).
- **Key Innovations**: Semantic-native representation at scale; depth-truncated bi-gram strategy for vocabulary compression; temporal folding for sequence compression with expanded feature expressivity.
- **Link**: https://arxiv.org/abs/2606.07546

### 2.12 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention (TGA)

- **Authors**: Hanqi Jin, Gaoming Yang, Zhangming Chan, et al.
- **Institution/Company**: (deployed in large-scale industrial production)
- **Date**: 2026-01-21
- **Abstract**: Linear-complexity approach for modeling multi-behavior transitions via structured sparse graph with item-level, category-level, and neighbor-level transitions. 5.8x faster than standard Transformer. Deployed in production with measurable business metric improvements.
- **Key Innovations**: Three-perspective transition graph (item, category, neighbor); linear-complexity graph attention; transition-type-aware joint modeling.
- **Link**: https://arxiv.org/abs/2601.14955

---

## 3. CTR Prediction & Advertising

### 3.1 Long-History User Transformers for Real-Time Ad Ranking

- **Authors**: (not specified)
- **Institution/Company**: Yandex
- **Date**: 2026
- **Abstract**: Multi-stage architecture where large offline transformer asynchronously encodes full user history into cached representation, lightweight runtime model combines cached representation with recent events. Pre-trained autoregressively with feedback prediction and next-item prediction. Recovers 72-80% of full-history quality. Production A/B: +2.77% primary metric on search ads, +2.1% on YAN, +2.26% revenue on search.
- **Key Innovations**: Decoupled offline/online architecture; autoregressive pre-training for ad CTR; cached representation robust to staleness; production-validated gains.
- **Link**: https://arxiv.org/abs/2607.14331

### 3.2 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer

- **Authors**: David Pardoe, Neil Daftary, et al.
- **Institution/Company**: LinkedIn
- **Date**: 2026-02-11
- **Abstract**: End-to-end decoder-only transformer for ads CTR. Multi-tower prediction heads model post-scoring signals (ad position). Self-gated attention stabilizes training. Timestamp-based RoPE captures temporal relationships across timescales. Session masking prevents train-serve skew. Achieved +11.04% CTR lift over LiRank baseline. Deployed on LinkedIn's homefeed sponsored updates.
- **Key Innovations**: Context-conditioned decoding for chicken-and-egg ranking problem; self-gated attention; timestamp-based RoPE; session masking for offline-online consistency.
- **Link**: https://arxiv.org/abs/2602.11410

### 3.3 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2026
- **Abstract**: Dual-path inter-layer connector routing each layer through Identity residual path (preserving first-order reuse) and Block Attention Residual path (high-order recall from all earlier blocks). Pointwise AttnRes uses SiLU instead of Softmax for CTR's parallel multi-interest patterns. 8-layer DeRes matches 16-layer OneTrans (2x compute saving). Up to +0.32% AUC on industrial dataset.
- **Key Innovations**: Dual-path (identity + attention residual) inter-layer design; Pointwise AttnRes with SiLU for multi-interest patterns; steeper compute-AUC scaling law.
- **Link**: https://arxiv.org/abs/2606.07980

### 3.4 GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu

- **Authors**: (not specified)
- **Institution/Company**: Baidu
- **Date**: 2026-02-02
- **Abstract**: End-to-end generative framework for CTR prediction with Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics and action signals. Full-scale deployment: +3.05% revenue, +3.49% CTR. Shows monotonic, approximately linear scaling with longer interaction sequences.
- **Key Innovations**: Causal Action-aware Multi-channel Attention; sequence-first generative paradigm for CTR; demonstrated scaling behavior with sequence length.
- **Link**: https://arxiv.org/abs/2602.01865

### 3.5 EST: Efficiently Scalable Transformer for CTR Prediction

- **Authors**: Mingyang Liu, Yong Bai, et al.
- **Institution/Company**: Alibaba (Taobao)
- **Date**: 2026-02-11
- **Abstract**: Fully unified modeling processing all raw inputs in a single sequence without lossy aggregation. Lightweight Cross Attention (LCA) prunes redundant self-interactions. Content Sparse Attention (CSA) uses content similarity for dynamic behavior selection. Exhibits stable power-law scaling. Deployed on Taobao: +3.27% RPM, +1.22% CTR.
- **Key Innovations**: Fully unified token sequence for CTR; LCA for cross-feature dependencies; CSA for content-guided sparse attention; validated power-law scaling.
- **Link**: https://arxiv.org/abs/2602.10811

### 3.6 GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning

- **Authors**: (not specified)
- **Institution/Company**: (WWW '26 paper)
- **Date**: 2026
- **Abstract**: Generative user intent framework leveraging semantic interest cohorts for CTR. Next-item prediction produces candidate interest cohorts (candidate-agnostic intent representations). Hierarchical candidate-aware network refines cohorts with cross-attention aligned to user history and target item. Addresses point-wise ranking paradigm's context blindness.
- **Key Innovations**: Generative interest cohort construction; candidate-agnostic intent representation; hierarchical candidate-aware refinement; end-to-end joint optimization.
- **Link**: https://arxiv.org/abs/2601.18251

### 3.7 LLM-HYPER: LLM-Based Hypernetworks for Cold-Start Ad CTR

- **Authors**: Luyi Ma, Wanjia Sherry Zhang, et al.
- **Institution/Company**: (top U.S. e-commerce platform)
- **Date**: 2026-04-13
- **Abstract**: Treats LLMs as hypernetworks to generate CTR estimator parameters in a training-free manner. Few-shot Chain-of-Thought prompting over multimodal ad content (text + images) infers feature-wise model weights. NDCG@10 +55.9% over cold-start baselines. 30-day A/B test competitive with warm-start model. Successfully deployed in production.
- **Key Innovations**: LLM as hypernetwork for weight generation; training-free cold-start CTR; multimodal CoT prompting; label-independent normalization/calibration.
- **Link**: https://arxiv.org/abs/2604.12096

### 3.8 IDProxy: Cold-Start CTR Prediction at Xiaohongshu with Multimodal LLMs

- **Authors**: (not specified)
- **Institution/Company**: Xiaohongshu
- **Date**: 2026-03-02
- **Abstract**: Uses multimodal LLMs for cold-start CTR prediction in ads and recommendation at Xiaohongshu (not fully detailed in search results).
- **Key Innovations**: Multimodal LLM approach to cold-start CTR; industrial deployment at social commerce platform.
- **Link**: https://arxiv.org/abs/2603.01590

---

## 4. Sequential Modeling

### 4.1 Beyond Positive Signals: Mixed-Polarity Behavior Sequences for CTR

- **Authors**: Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Institution/Company**: (not specified)
- **Date**: 2026-06-13
- **Abstract**: Demonstrates that mixed-polarity behavior sequences (chronologically interleaving positive and negative tokens) consistently outperform positive-only sequences across diverse architectures. Target-Aware Polarity Fusion (TAPF) differentiates behavioral evidence. +1.9% to +9.6% relative AUC across five architectures. Significant gains for cold-start items.
- **Key Innovations**: Mixed-polarity behavior sequences paradigm; Target-Aware Polarity Fusion mechanism; demonstrates negative behavior value across architectures; cold-start improvement.
- **Link**: https://arxiv.org/abs/2606.15252

### 4.2 One Sequential Recommendation Model Pretrained from Synthetic Priors (SRPFN)

- **Authors**: Woosung Kang, Jiwon Jeong, et al.
- **Institution/Company**: KAIST
- **Date**: 2026
- **Abstract**: Prior-data Fitted Network for sequential recommendation. Pretrained offline on 25.6M sequences from synthetic prior spanning diverse transition patterns. Generates recommendations via support set conditioning without gradient updates. Best or second-best across five benchmarks with substantially lower compute.
- **Key Innovations**: Prior-data fitted network for recs; synthetic pretraining on diverse transitions; zero-shot domain adaptation via support set conditioning.
- **Link**: https://arxiv.org/abs/2606.15752

### 4.3 RecRec: Recursive Refinement for Sequential Recommendation

- **Authors**: (not specified)
- **Institution/Company**: (RecSys '26 paper)
- **Date**: 2026
- **Abstract**: Lightweight model (3.9M-14M parameters) maintaining compact latent state updated through shared recursive module. Evidence-anchored correction mechanism stabilizes refinement. Matches or outperforms SOTA sequential, graph-based, and reasoning-enhanced recommenders. Surpasses LLM-based models with 99% smaller footprint.
- **Key Innovations**: Recursive latent refinement with evidence-anchored correction; extreme parameter efficiency; correction-gated stabilization preventing semantic drift.
- **Link**: https://arxiv.org/abs/2607.10541

---

## 5. Games & Reinforcement Learning

### 5.1 Augmenting Game AI with Deep Reinforcement Learning

- **Authors**: Alessandro Sestini, Joakim Bergdahl, amir baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Institution/Company**: EA (Electronic Arts)
- **Date**: 2026-06-18
- **Abstract**: Vision paper proposing framework for training RL models suited towards game AI. Identifies four requirements: short training time, bug detection/fixing, authenticity (not superhuman), and runtime inference constraints. Tested on EA SPORTS FC 25 (goalkeeper AI) and Battlefield 6 (ground infantry). Addresses gap between academic RL and production game deployment.
- **Key Innovations**: Production-oriented RL framework for game AI; authenticity-over-superhumanity principle; practical deployment constraints (latency, hardware, debugging); tested in AAA commercial games.
- **Link**: https://arxiv.org/abs/2606.20210

### 5.2 Think in Games (TiG): Learning to Reason in Games via RL with LLMs

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2025-08-29
- **Abstract**: Empowers LLMs to develop procedural understanding through direct interaction with game environments. Reformulates RL decision-making as language modeling: LLM generates language-guided policies refined via online RL (GRPO). Qwen-3-14B achieves 90.91% accuracy on Honor of Kings, outperforming Deepseek-R1 (86.67%) with 10x fewer parameters.
- **Key Innovations**: Bridging declarative and procedural knowledge in LLMs; RL as language modeling task; competitive performance with dramatically lower data/compute; interpretable step-by-step explanations.
- **Link**: https://arxiv.org/abs/2508.21365

### 5.3 From Black Box to Executable Logic: Explainable RL through Prolog Expert Systems

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2026-07-16
- **Abstract**: Three-stage post-hoc transformation extracting frozen PPO teacher, inducing ordered rule list, emitting as Prolog program. Expansion stage edits rule base with policy evaluation certification. Return-loss bound provides machine-checkable certificate. Expanded Prolog program attains exact optimal return on key-and-door task.
- **Key Innovations**: RL-to-logic distillation (Prolog); machine-checkable return-loss bound; monotonic expansion with certification; demonstrates exact optimal return recovery.
- **Link**: https://arxiv.org/abs/2607.15459

### 5.4 When Actions Disappear: Adversarial Action Removal in Self-Play RL

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2026-05-04
- **Abstract**: Studies adversarial action masking in self-play RL where attacker selectively removes legal actions. Learned masking causes more damage than random masking and perturbation baselines. Persists across Q-learning, PPO, NFSP, DQN victims. Identifies action availability as distinct robustness surface via CAC metrics.
- **Key Innovations**: Action availability as robustness surface; learned adversarial action masking; persistence across algorithms and transfer across agents; CAC metrics for targeted high-value decision points.
- **Link**: https://arxiv.org/abs/2605.16312

### 5.5 ExToken: Structured Exploration for Efficient VLA-RL Fine-tuning

- **Authors**: (not specified)
- **Institution/Company**: (not specified)
- **Date**: 2026-07-14
- **Abstract**: Addresses exploration stagnation in Vision-Language-Action RL. Conditions VLA policies on discrete behavioral priors from offline demonstrations for structured exploration. State-conditioned token selector bridges training exploration with deterministic inference. 98.2% success rate on LIBERO benchmark, outperforming SFT baselines.
- **Key Innovations**: Exploration tokens from demonstration clustering; state-conditioned token selector; trajectory diversity > rollout quantity; compatible with different VLA architectures.
- **Link**: https://arxiv.org/abs/2607.12931

---

## Summary of Trends

1. **Generative Recommendation** is rapidly maturing: Semantic IDs + item-level scoring (Gryphon, UniRec, SIDReasoner) and long-sequence modeling (CMSL, HyTRec, GLASS) are converging toward production-ready systems.

2. **CTR Prediction** is undergoing a transformer revolution: decoder-only architectures (CADET at LinkedIn, GRAB at Baidu, EST at Taobao) are replacing DLRM ensembles with significant online gains (+3-11%).

3. **LLM Reasoning** is diversifying: heterogeneous ensembles (PoTRE), latent computation (LatentMT), modular memory (MILES), and heterogeneous caching (LaCache) explore alternative scaling paths.

4. **Cold-start via LLMs** is emerging: LLM-HYPER and IDProxy use LLMs as hypernetworks or feature extractors for cold-start ad CTR, achieving production-grade results.

5. **Game AI + RL** is bridging academia-industry gap: EA's framework and TiG demonstrate practical RL deployment in AAA games with authenticity and efficiency constraints.

6. **Mixed-polarity and multi-behavior sequences** are unlocking new value: incorporating negative signals and transition patterns consistently improves CTR across architectures.
