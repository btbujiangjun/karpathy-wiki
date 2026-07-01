---
title: "arXiv AI Search — July 2026"
type: synthesis
created: 2026-07-01
updated: 2026-07-01
sources: []
tags: [arxiv, survey, llm, recommendation, ctr, multimodal, rl, games, attention]
---

# arXiv AI Search — July 2026

> Comprehensive search of recent arXiv preprints across AI, LLMs, recommendation systems, advertising/CTR, sequential modeling, multimodal learning, games, and efficient architectures. Papers from January–June 2026.

---

## 1. Recommender Systems & LLMs for Recommendation

### AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors**: Changxin Lao, Fei Pan, Guozhuang Ma, Han Li, et al. (Kuaishou / Kun Gai group)
- **Link**: https://arxiv.org/abs/2606.26859
- **Abstract**: AgentX is a production-deployed multi-agent system that autonomously generates, implements, evaluates, and learns from recommendation experiments. It orchestrates four stages in a closed loop: a Proposal Agent, a Development Agent (repository-grounded code generation), an Evaluation Agent (safe online A/B with guardrails), and a Harness Evolution layer (SGPO) that distills trajectories into semantic-gradient updates.
- **Key Innovations**: Self-evolving development engine for industrial recommenders; SGPO for semantic-gradient policy optimization; autonomous paper reproduction and module ablation. Delivers ¥100M+ annualized revenue uplift.

### Filling the Gaps: Selective Knowledge Augmentation for LLM Recommenders (KnowSA-CKP)
- **Authors**: Nowhyun et al.
- **Link**: https://arxiv.org/abs/2604.07825
- **Abstract**: Identifies the "knowledge gap problem" — LLMs have uneven knowledge of items due to imbalanced pretraining exposure. Proposes CKP (Comparative Knowledge Probing) to estimate per-item knowledge and selectively augment only knowledge-poor items.
- **Key Innovations**: Training-free selective augmentation; CKP scoring via collaborative relationship ranking; more efficient use of limited context budget.
- **Code**: https://github.com/nowhyun/KnowSA_CKP

### User Simulator-Guided Multi-Turn Preference Optimization (SMTPO) for Reasoning LLM-based Conversational Recommendation
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2604.03671
- **Abstract**: SMTPO uses an LLM-based simulator to generate high-quality feedback, a retriever to dynamically filter candidates, and a Reasoning LLM (trained with SFT + RL) to iteratively optimize preferences. Addresses noisy feedback in multi-turn conversational recommendation.
- **Key Innovations**: Reasoning LLM as recommender backbone; simulator-guided multi-turn preference optimization; dual semantic-collaborative view retriever.

### Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2602.07298
- **Abstract**: First demonstration of robust power-law scaling for LLMs continually pre-trained on recommendation-specific synthetic data. Sequential models (SasRec, GRU4Rec) trained on synthetic data outperform real-data counterparts by +130% Recall@100. Scaling law: L(D) = L∞ + A·D^{-α} across 0.6B–8B models on 163B tokens.
- **Key Innovations**: First scaling laws for LLM recommenders; layered synthetic data curriculum (collaborative filtering + UI histories); asymmetric synergy between data modalities.

### From Token to Item: Item-aware Attention Mechanism (IAM) for LLM Recommendation
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2603.19693
- **Abstract**: Reveals that LLM-based recommenders focus on token-level relations, missing item-level collaborative signals. Proposes IAM with two complementary attention layers: intra-item (content semantics) and inter-item (collaborative relations).
- **Key Innovations**: Item-aware attention explicitly modeling items as fundamental units; stacked intra-/inter-item attention design.

### BEAR: Beam-Search-Aware Optimization for LLM Recommendation
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2601.22925
- **Abstract**: Identifies training-inference inconsistency: SFT optimizes overall probability of positive items but beam search can prune them early due to insufficient prefix probability. BEAR enforces that each token ranks within top-B at each decoding step.
- **Key Innovations**: Beam-search-aware regularization; model-agnostic fine-tuning objective; 12.50% average improvement over 9 SFT baselines.

### GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: N/A (JD.com)
- **Link**: https://arxiv.org/abs/2604.14878
- **Abstract**: Addresses three challenges in generative retrieval for recommendation: (i) pagination inconsistency, (ii) long user sequence encoding cost, (iii) alignment with user preferences. Proposes Page-wise NTP, asymmetric linear Token Merger, and GRPO-SR (GRPO + NLL regularization + Hybrid Rewards).
- **Key Innovations**: Page-wise NTP task; Token Merger for 2× input compression; GRPO-SR for preference alignment with reward hacking mitigation. 9.5% click and 8.7% transaction lift on JD.

### Generative Archetype-Grounded Item Representations (GenAIR) for Sequential Recommendation
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.11023
- **Abstract**: GenAIR uses LLMs to infer "Archetype" descriptions of items' ideal target audiences, extracts embeddings, and applies behavioral calibration to ground archetypes in real-world interaction patterns.
- **Key Innovations**: Archetype-grounded item representations bridging semantic and behavioral gaps; behavioral calibration objective; plug-and-play with existing sequential models.

### Gryphon: Unified Architecture for Semantic-ID Generation and Item-Level Scoring
- **Authors**: N/A (Music streaming service)
- **Link**: https://arxiv.org/abs/2606.08604
- **Abstract**: Encoder-decoder generative retrieval architecture that adds item-level scoring alongside SID generation. Resolves the mismatch between beam-search likelihood and item relevance, and handles SID collisions by re-scoring concrete items.
- **Key Innovations**: Joint SID generation + item-level scoring; resolves SID collision problem; replaces 15+ candidate generators in production. +3.7% Recall@1000 over vanilla GR.

### Modular Representation Compression (MARC) for LLM Recommendations
- **Authors**: N/A (SIGIR 2026)
- **Link**: https://arxiv.org/abs/2604.18146
- **Abstract**: Discovers Mid-layer Representation Advantage (MRA) — middle LLM layers outperform final layers for recommendation. Proposes MARC: Modular Adjustment + Modular Task Decoupling to compress LLM representations effectively. 2.82% eCPM lift in search advertising.
- **Key Innovations**: Identification of MRA phenomenon; modular compression with information constraints; deployed in large-scale commercial search advertising.

---

## 2. CTR Prediction & Advertising

### LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation
- **Authors**: Lee Xiong, Zhirong Chen, Rahul Mayuranath, et al. (Meta)
- **Link**: https://arxiv.org/abs/2601.20083
- **Abstract**: Demonstrates power-law scaling for sequence modeling in production ads recommendation. Finds semantic features are a prerequisite for scaling. Introduces two-stage architecture (asynchronous upstream user model + downstream ranking). Deployed as Meta's largest user model.
- **Key Innovations**: First scaling laws for industrial ads recommendation; two-stage architecture decoupling heavy computation; 4.3% conversion uplift on Facebook Feed/Reels.

### CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, et al. (LinkedIn)
- **Link**: https://arxiv.org/abs/2602.11410
- **Abstract**: End-to-end decoder-only transformer for ads CTR. Key innovations: context-conditioned decoding with multi-tower prediction heads (resolving predicted-CTR vs. position chicken-and-egg), self-gated attention, timestamp-based RoPE, session masking. 11.04% CTR lift over LiRank (DCNv2 + sequential).
- **Key Innovations**: Context-conditioned architecture for post-scoring signals; self-gated attention; timestamp RoPE; production engineering (Flash Attention, tensor packing). Serves LinkedIn main traffic.

### GRAB: Generative Ranking for Ads at Baidu (LLM-Inspired CTR)
- **Authors**: Shaopeng Chen, Chuyue Xie, et al. (Baidu)
- **Link**: https://arxiv.org/abs/2602.01865
- **Abstract**: Generative CTR framework with Causal Action-aware Multi-channel Attention (CamA). Demonstrates monotonic improvement with longer sequences. 3.05% revenue increase, 3.49% CTR lift in full-scale deployment.
- **Key Innovations**: CamA for capturing temporal dynamics and action signals; scaling behavior approximately linear with sequence length.

### HyFormer: Revisiting Sequence Modeling and Feature Interaction in CTR
- **Authors**: Yunwen Huang, Shiyong Hong, et al.
- **Link**: https://arxiv.org/abs/2601.12681
- **Abstract**: Unified hybrid transformer integrating long-sequence modeling and feature interaction. Alternating Query Decoding (expanding non-sequential features into Global Tokens) and Query Boosting (cross-query/sequence interactions via efficient token mixing).
- **Key Innovations**: Unified rather than decoupled pipeline; alternating optimization view of LRM modeling; superior scaling with parameters and FLOPs.

### EST: Efficient Scaling Laws in CTR Prediction via Unified Modeling
- **Authors**: Mingyang Liu, Yong Bai, et al. (Alibaba / Taobao)
- **Link**: https://arxiv.org/abs/2602.10811
- **Abstract**: Achieves fully unified modeling (all raw inputs in single sequence without lossy aggregation). Proposes Lightweight Cross Attention (LCA) and Content Sparse Attention (CSA). Exhibits stable power-law scaling. 3.27% RPM lift, 1.22% CTR lift on Taobao display advertising.
- **Key Innovations**: Fully unified sequence modeling for CTR; LCA for cross-feature dependencies; CSA for content-based behavior selection.

### SparseCTR: Sparse Attention on Long-term Behaviors for CTR
- **Authors**: Weijiang Lai, Beihong Jin, et al.
- **Link**: https://arxiv.org/abs/2601.17836
- **Abstract**: Three-branch sparse self-attention (global interests, interest transitions, short-term interests) with composite relative temporal encoding. Scaling law across three FLOPs orders of magnitude. 1.72% CTR lift, 1.41% CPM lift online.
- **Key Innovations**: Personalized chunk segmentation; three-branch sparse attention for multi-scale interests; scaling law in FLOPs.

### TokenFormer: Unify Multi-Field and Sequential Recommendation Worlds
- **Authors**: N/A (Tencent)
- **Link**: https://arxiv.org/abs/2604.13737
- **Abstract**: Identifies Sequential Collapse Propagation (SCP) when unifying multi-field and sequential features. Proposes Bottom-Full-Top-Sliding (BFTS) attention + Non-Linear Interaction Representation (NLIR). State-of-the-art on Tencent's advertising platform.
- **Key Innovations**: Diagnosis of SCP failure mode; BFTS attention schedule; NLIR gated mechanism for dimensional robustness.

### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.07980
- **Abstract**: Dual-path residual (Identity residual + Block Attention Residual) with SiLU-based Pointwise AttnRes. Steeper scaling law (γ=0.118 vs 0.071 for OneTrans, 1.66×). 8-layer DeRes matches 16-layer OneTrans.
- **Key Innovations**: Dual-path residual design; Pointwise AttnRes with SiLU (enabling negative forgetting weights); 2× compute savings at equivalent AUC.

### LoopCTR: Computation Scaling Through Recursive Loop Latent Reasoning
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2604.19550
- **Abstract**: Reuses the same layers recursively with Hyper-Connected Residuals + MoE. Train-multi-loop, infer-zero-loop strategy. Loop scaling effect: more loops during training consistently improve performance.
- **Key Innovations**: Loop scaling paradigm for CTR; sandwich architecture (Entry/Loop/Exit); process supervision enabling zero-loop inference.

### GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2602.22732
- **Abstract**: Production-oriented generative recommender with Unified Advertisement Semantic ID (UA-SID), Value-Aware Supervised Learning (VSL), Ranking-Guided Softmax Preference Optimization (RSPO), LazyAR decoder, and Dynamic Beam Serving.
- **Key Innovations**: UA-SID with MGMR quantization; RSPO list-wise RL for advertising; LazyAR decoder for throughput; DBS with traffic-adaptive beam search.

---

## 3. LLM Alignment & Reinforcement Learning

### f-GRPO and Beyond: Divergence-Based RL Algorithms for General LLM Alignment
- **Authors**: Rajdeep Haldar, Lantao Mei, Guang Lin, Yue Xing, Qifan Song
- **Link**: https://arxiv.org/abs/2602.05946
- **Abstract**: Extends divergence-based perspective to general alignment (RLVR + PA). Proposes f-GRPO (on-policy) and f-HAL (hybrid on/off-policy) derived from f-divergences. Theoretical guarantees for reward improvement.
- **Key Innovations**: Unified divergence framework for general alignment; f-GRPO generalizes GRPO; theoretical justification of expected improvement over GRPO.

### Unifying Stable Optimization and Reference Regularization in RLHF (DAR)
- **Authors**: Li He, Qiang Qu, et al.
- **Link**: https://arxiv.org/abs/2602.11523
- **Abstract**: Dual-KL alignment objective unifying KL penalty against π₀ (reward hacking prevention) and ratio clipping toward πₜ (stable optimization). Yields weighted SFT loss. ICLR 2026.
- **Key Innovations**: Explicitly addresses trade-off between two KL regularizations; RL-free (weighted SFT); consistent gains over PPO and online preference methods.

### GAC: Stabilizing Asynchronous RL Training for LLMs via Gradient Alignment Control
- **Authors**: Haofeng Xu, Junwei Su, et al.
- **Link**: https://arxiv.org/abs/2603.01501
- **Abstract**: Identifies "stale-aligned gradient effect" in asynchronous RL — persistently high cosine similarity between consecutive policy gradients. Proposes Gradient Alignment Control via gradient projection. Convergence guarantees.
- **Key Innovations**: Diagnosis of stale-aligned gradients as instability cause; dynamics-aware gradient projection; recovers synchronous-like training dynamics at high staleness.

### RLAR: Agentic Reward System for Multi-task RL on LLMs
- **Authors**: Andrew Zhuoer Feng, Cunxiang Wang, et al.
- **Link**: https://arxiv.org/abs/2603.00724
- **Abstract**: Agent-driven framework that dynamically assigns tailored reward functions per query. LLM agents retrieve optimal reward models from the Internet and synthesize programmatic verifiers. 10–60% consistent gains across math, code, translation, dialogue.
- **Key Innovations**: Dynamic reward orchestration via LLM agents; tool synthesis for reward acquisition; self-evolving with shifting data distributions.

### Efficiently Aligning Language Models with Online Natural Language Feedback
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2605.04356
- **Abstract**: Iterative protocol: train against proxy reward → stop at over-optimization → collect expert NL feedback → update proxy. ICL recovers 35% with 50× fewer samples; fine-tuning recovers 100% with 3× fewer samples.
- **Key Innovations**: Online NL feedback for fuzzy domains; iterative over-optimization correction; dramatic data efficiency improvements.

### Bootstrapping Exploration with Group-Level NL Feedback (GOLF)
- **Authors**: Lei Huang, Xiang Cheng, et al.
- **Link**: https://arxiv.org/abs/2603.04597
- **Abstract**: Exploits group-level NL feedback (external critiques + intra-group attempts) for targeted exploration. Adaptive refinement injection as off-policy scaffolds. 2.2× sample efficiency improvement.
- **Key Innovations**: Aggregated group-level feedback for exploration; adaptive scaffold injection; joint optimization of generation and refinement.

### GeoAlign: Geometric Rollout Curation for Robust LLM RL
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.26917
- **Abstract**: Identifies "directional inconsistency" — small set of high-reward rollouts with conflicting preference directions. GeoAlign detects and rectifies directionally inconsistent rollouts via angular deviation from batch consensus.
- **Key Innovations**: Directional consensus as reliability signal; forward-only plug-in for rollout curation; outperforms PF-PPO, PAR, PODS, Seed-GRPO.

### EvoTrainer: Co-Evolving LLM Policies and Training Harnesses
- **Authors**: Guhong Chen, Yingcheng Shi, et al.
- **Link**: https://arxiv.org/abs/2606.03108
- **Abstract**: Autonomous training framework that co-evolves policies and training-side harnesses. Diagnoses rollout evidence, revises diagnostics, backtests interventions, accumulates reusable skills. Matches/exceeds human-engineered RL references.
- **Key Innovations**: Autonomous joint evolution of policy + harness; diagnostic reasoning loop; reusable skill accumulation across domains.

### Curriculum-RLAIF
- **Authors**: Jiaye Lin, Mengdi Li, et al.
- **Link**: https://aclanthology.org/2026.findings-acl.1685
- **Abstract**: Constructs preference pairs with varying difficulty levels and produces curriculum for reward model training. Improves reward model generalizability and policy alignment without extra inference cost.
- **Key Innovations**: Data-centric curriculum for RLAIF; difficulty-graded preference data.

### ARF-RLHF: Adaptive Reward-Following through Emotion-Driven Self-Supervision
- **Authors**: N/A
- **Link**: https://aclanthology.org/2026.acl-long.1637
- **Abstract**: Converts natural feedback into continuous preference trajectories optimized via TraceBias algorithm. Outperforms PPO (+3.3%) and DPO (+7.6%) by learning from free-form linguistic feedback.
- **Key Innovations**: Continuous reward modeling from NL feedback; TraceBias algorithm with Double Average Method; personalized RLHF.

---

## 4. AI Agents & Games

### MemoPilot: Test-Time Learning of LLM Agents via RL over Memory
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.08656
- **Abstract**: Treats memory updating as a multi-turn decision problem optimized with multi-turn GRPO. Turn-wise rewards + turn-level advantage estimation. #1 Elo on Limit Texas Hold'em (1762) and Rock-Paper-Scissors (1590), outperforming DeepSeek-V3.2.
- **Key Innovations**: Trainable memory update process; multi-turn GRPO with fine-grained credit assignment; frozen LLM + learned memory pilot.

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2605.04906
- **Abstract**: Recursive reasoning paradigm where agent's reasoning integrates others' reasoning processes. Centralized CoT comparison for reward signals + hybrid advantage estimation. 22.1% average improvement across multi-agent games.
- **Key Innovations**: Recursive reasoning with opponent modeling; centralized CoT comparison module; hybrid advantage estimation.

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2605.00347
- **Abstract**: Trains VLMs for long-horizon gameplay (Super Mario Land, 100+ turns) using PPO with lightweight turn-level critic. Pretrained VLMs provide strong action priors. 3× game progress over frontier models.
- **Key Innovations**: Turn-level critic for long-horizon VLM RL; pretrained VLMs as action priors; open training framework for VLM agents.

### AgentOdyssey: Open-Ended Long-Horizon Text Game Generation
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.24893
- **Abstract**: Procedurally generates open-ended text games with rich entities, dynamics, and long-horizon tasks. Multifaceted evaluation: world knowledge, episodic memory, exploration diversity. Even top agents far below human performance.
- **Key Innovations**: LLM-driven game generation engine with verification; diagnostic test suite beyond game progress; test-time continual learning evaluation.

### LangMARL: Natural Language Multi-Agent RL
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2604.00722
- **Abstract**: Brings credit assignment and policy gradient evolution from cooperative MARL into language space. Agent-level language credit assignment + gradient evolution in language space. Improves sample efficiency and interpretability.
- **Key Innovations**: Language-space policy gradient; centralized critic for LLM agents; scalable to N=20 agents.

### MARL-GPT: Foundation Model for Multi-Agent RL
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2604.05943
- **Abstract**: Single GPT-based model trained via offline RL on expert trajectories (400M SMACv2, 100M GRF, 1B POGEMA). Single transformer observation encoder, no task-specific tuning. Competitive with specialized baselines.
- **Key Innovations**: Generalist MARL foundation model; single architecture across diverse environments (combat, sports, navigation); large-scale offline imitation + RL training.

### MEMO: Memory-Augmented Model Context Optimization
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2603.09022
- **Abstract**: Self-play framework optimizing inference-time context without weight updates. Tournament-style prompt evolution with uncertainty-aware selection (TRUESKILL) + prioritized replay. 20.9%→44.3% win rate for Qwen2.5-7B using 19× fewer games than RL.
- **Key Innovations**: Weight-free self-play; CRUD-style persistent memory bank; tournament-style context evolution; 19× sample efficiency over RL.

---

## 5. Efficient Architectures & Attention

### Superlinear Multi-Step Attention
- **Authors**: Yufeng Huang
- **Link**: https://arxiv.org/abs/2601.18401
- **Abstract**: Reformulates causal self-attention as N-step search. N=2 instantiation scales as O(L^{3/2}). 109 tok/s at 1M context, 76 tok/s at 10M on modified 30B MoE model on single B200 GPU.
- **Key Innovations**: Multi-step attention with subquadratic complexity; preserves random context access (structural non-exclusion); span-search + span-attention decomposition.

### Sparse Feature Attention (SFA / FlashSFA)
- **Authors**: Yan Xie, Tiansheng Wen, et al.
- **Link**: https://arxiv.org/abs/2603.22300
- **Abstract**: Explores feature-level sparsity (orthogonal to sequence-level). Q/K as k-sparse codes: cost O(n²k²/d). FlashSFA kernel extends FlashAttention for sparse overlaps. 2.5× speedup, ~50% FLOPs/KV-cache reduction. Matches dense baselines.
- **Key Innovations**: Feature sparsity as complementary axis; FlashSFA IO-aware kernel; matches dense accuracy at 50% compute.

### Gecko: Neural Architecture for Arbitrary-Length Sequences
- **Authors**: Xuezhe Ma, S. P. Wen, et al.
- **Link**: https://arxiv.org/abs/2601.06463
- **Abstract**: Mega/Megalodon descendant with timestep decay normalization, sliding chunk attention, adaptive working memory. Loss 1.68 (vs Llama2-7B 1.75, Megalodon-7B 1.70). Handles 4M tokens natively without context extension.
- **Key Innovations**: Inherently handles arbitrary-length sequences; 4M token context without extension tricks; outperforms Llama2-7B and Megalodon-7B at same scale.

### Nexusformer: Nonlinear Attention Expansion for Transformer Scaling
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2604.19147
- **Abstract**: Replaces linear Q/K/V with Nexus-Rank (three-stage nonlinear mapping via dual activations). Enables lossless structured growth: zero-initialized blocks preserve pretrained knowledge during expansion. 41.5% less compute than Tokenformer for progressive scaling.
- **Key Innovations**: Nonlinear Q/K/V projections enabling incremental growth; geometric scaling law; zero-initialization for stable knowledge inheritance.

### MiniMax Sparse Attention (MSA)
- **Authors**: MiniMax
- **Link**: https://arxiv.org/abs/2606.13392
- **Abstract**: Blockwise sparse attention built on GQA. Lightweight Index Branch selects Top-k KV blocks per GQA group; Main Branch does exact block-sparse attention. 28.4× compute reduction at 1M context; 14.2× prefill and 7.6× decoding speedups on H800. 109B multimodal model.
- **Key Innovations**: Group-specific sparse retrieval; exp-free Top-k + KV-outer execution; production-grade 109B multimodal model; open-source kernel.

### STEM: Scaling Transformers with Embedding Modules
- **Authors**: Ranajoy Sadhukhan, Sheng Cao, et al. (Meta)
- **Link**: https://arxiv.org/abs/2601.10639
- **Abstract**: Replaces FFN up-projection with static token-indexed embedding lookup. Decouples capacity from per-token FLOPs and communication. Enables CPU offload, knowledge editing, test-time capacity scaling with sequence length. 3–4% accuracy gains on reasoning benchmarks.
- **Key Innovations**: Static sparsity without routing overhead; interpretable knowledge editing; test-time capacity scaling (longer sequences → more parameters activated).

### CAHP: Complementary Attention Head Pruning
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.19150
- **Abstract**: Graph-theoretical head selection via clustering + information-theoretic distance. Automatically determines pruning ratio via diminishing marginal performance curve. Avoids "proximity bias" of gradient-based methods.
- **Key Innovations**: Post-hoc pruning without predefined sparsity; graph-based complementary head selection; preserves intermediate-layer heads.

### Vashista Sparse Attention: Constant-Time Attention
- **Authors**: Vashista Nobaub
- **Link**: https://arxiv.org/abs/2602.13804
- **Abstract**: Face-stability theorem: under support gap condition, entropic attention concentrates on constant-size active face (exponential decay of inactive mass). Practical paging-style context selection. Theoretical guarantee for sparse decoding.
- **Key Innovations**: Theoretical characterization of attention sparsity; exponential decay guarantee; drop-in sparse decoding mechanism.

### Rethinking Efficient Attention in Hybrid Architectures
- **Authors**: Zhou et al.
- **Link**: https://arxiv.org/abs/2606.15378
- **Abstract**: Systematic analysis of hybrid architectures (full attention + SWA/recurrent). Finds efficient-attention design affects speed of long-context emergence, not final convergence. Discovers "Large-Window Laziness" — larger SWA windows delay retrieval head formation. NoPE on full-attention layers improves long-context.
- **Key Innovations**: Large-Window Laziness phenomenon; NoPE-only on full-attention layers; scaling analysis across hybrids.

### InfSA / Linear-InfSA: Infinite Self-Attention
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2603.00175
- **Abstract**: Spectral reformulation treating attention as diffusion on content-adaptive token graph. Neumann series over attention matrices. Linear-time variant maintains O(d_h) auxiliary state. 84.7% ImageNet top-1 (ViT, +3.2 over softmax). 9216×9216 inference capable.
- **Key Innovations**: Graph centrality view of attention (Katz, PageRank); linear-time variant via eigenvector approximation; 13× better throughput/energy.

---

## 6. Multimodal Learning

### Beyond Language Modeling: Multimodal Pretraining Exploration
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2603.03276
- **Abstract**: Controlled from-scratch pretraining with Transfusion (next-token for language + diffusion for vision). Key findings: RAE is optimal visual representation; vision and text are synergistic; MoE harmonizes scaling asymmetry (vision more data-hungry than language).
- **Key Innovations**: IsoFLOP analysis revealing vision-language scaling asymmetry; RAE for unified visual representation; MoE for multimodal scaling.

### Penguin-VL: LLM-based Vision Encoders for Efficient VLM
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2603.06569
- **Abstract**: Builds vision encoder from LLM (Qwen3-0.6B) rather than standard ViT. Two-stage coarse-to-fine training + Temporal Redundancy-Aware (TRA) token compression. Best-in-class at 2B and 8B scales.
- **Key Innovations**: LLM-as-vision-encoder; TRA token compression for video; progressive harmonization of perception and reasoning.

### GenLIP: Generative Language-Image Pre-training
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2605.00809
- **Abstract**: Trains ViT to predict language tokens directly from visual tokens using standard LM objective. No contrastive batches or text decoder. Uses 1/5 the samples of SigLIP2 (8B vs 40B). Strong on OCR and chart understanding.
- **Key Innovations**: Simplest possible generative vision-language pretraining; single transformer for both modalities; native-aspect-ratio adaptation.

### Lance: Unified Multimodal Modeling by Multi-Task Synergy
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2605.18678
- **Abstract**: Lightweight native unified model (understanding + generation + editing for images and video). Dual-stream MoE on shared interleaved sequences. Modality-aware RoPE. Staged training (PT→CT→SFT→RL).
- **Key Innovations**: Compact unified model (not scale-dependent); decoupled capability pathways; modality-aware RoPE.

### UniAR: Unified Multimodal Autoregressive with Shared Context-Visual Tokenizer
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.18249
- **Abstract**: Single discrete visual tokenizer shared across understanding and generation. Multi-level feature fusion + lookup-free bitwise quantization. Parallel-bitwise-prediction for short visual sequences. Diffusion decoder for high-fidelity images.
- **Key Innovations**: One tokenizer for both understanding and generation; bitwise quantization scaling visual vocabulary; parallel visual code prediction.

### Hydra-X: Native Unified Multimodal with Holistic Visual Tokenizers
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2606.13289
- **Abstract**: First UMM unifying image and video tokenization in single ViT. Frame-level causal temporal attention (full spatiotemporal degrades reconstruction). Unifies 5 tasks: image/video understanding, generation, and editing.
- **Key Innovations**: Single ViT for image+video tokenization; principled temporal attention design; holistic visual tokenizer for 5 tasks.

### MixAtlas: Uncertainty-aware Data Mixture for Multimodal Midtraining
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2604.14198
- **Abstract**: Decomposes training corpus along two axes (image concepts + task supervision). GP-UCB search with proxy models. Up to 17.6% gains on Qwen2-7B; recipes transfer across model families.
- **Key Innovations**: Two-axis decomposition of multimodal data; proxy-based mixture optimization; transferable recipes.

### Where Does Vision Meet Language? Contrastive Attention for MLLMs
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2601.08151
- **Abstract**: Layer-wise analysis reveals fusion primarily occurs in shallow layers + "review" behavior at deep layer. Proposes training-free contrastive attention (pre-integration vs post-integration attention difference) to mask irrelevant regions. SOTA on LLaVA series.
- **Key Innovations**: Mechanism analysis of visual integration in MLLMs; training-free contrastive attention masking.

### Visual Enhanced Depth Scaling for Multimodal Latent Reasoning
- **Authors**: N/A
- **Link**: https://arxiv.org/abs/2604.10500
- **Abstract**: Reveals vision-text optimization disparity and fixed-depth dilemma in latent reasoning. Visual replay module + routing depth scaling + curriculum latent training (gradual replacement of CoT steps with latent tokens).
- **Key Innovations**: Curriculum latent training bridging CoT and latent reasoning; adaptive depth scaling per token; visual replay for perception grounding.

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **Scaling Laws for Recommendation/CTR** | LLaTTE (Meta), Principled Synthetic Data, EST (Taobao), SparseCTR, DeRes |
| **Generative / LLM-based Recommendation** | AgentX (Kuaishou), GenRec (JD), GR4AD, Gryphon, BEAR, IAM |
| **Multi-agent LLM for Games** | Strat-Reasoner, MemoPilot, LangMARL, MARL-GPT, Odysseus (VLM games) |
| **RL for LLM Alignment** | f-GRPO, DAR, GAC, RLAR, GeoAlign, EvoTrainer, GOLF |
| **Efficient Attention** | Superlinear, SFA/FlashSFA, MSA (MiniMax), Vashista, InfSA |
| **Incremental / Expandable Architectures** | Nexusformer, STEM |
| **Unified Multimodal Models** | Lance, UniAR, Hydra-X, GenLIP, Penguin-VL |
| **Agentic / Autonomous Training** | AgentX, EvoTrainer, RLAR |
