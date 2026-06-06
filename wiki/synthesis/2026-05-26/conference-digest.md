---
title: 顶会论文专题报告 — 2026年5月深度版
type: synthesis
created: 2026-05-26
updated: 2026-05-26
sources: [ICML-2025, AAAI-2026, ICLR-2026, CVPR-2026, EMNLP-2025, ACL-2026, KDD-2026, RecSys-2025, WWW-2026, SIGIR-2026, CIKM-2025]
tags: [conference-digest, llm, recsys, ctr, agents, rl, code-generation, diffusion, recommendation-advertising, scaling-laws, reasoning]
---

# 顶会论文专题报告 — 2026年5月深度版

> 覆盖 11 个顶会的最新接收论文，重点聚焦 LLM 推理/后训练、推荐系统缩放定律与生成式推荐、广告 CTR 预估、AI Agent、扩散模型、多模态大模型等方向。包含来自 Google DeepMind、OpenAI、Meta、NVIDIA、Anthropic、ByteDance、Alibaba、Kuaishou 等顶级实验室的论文。

---

## 目录

1. [ICML 2025](#1-icml-2025)
2. [AAAI 2026](#2-aaai-2026)
3. [ICLR 2026](#3-iclr-2026)
4. [CVPR 2026](#4-cvpr-2026)
5. [EMNLP 2025](#5-emnlp-2025)
6. [ACL 2026 / EACL 2026](#6-acl-2026--eacl-2026)
7. [KDD 2026](#7-kdd-2026)
8. [RecSys 2025](#8-recsys-2025)
9. [WWW 2026](#9-www-2026)
10. [SIGIR 2026](#10-sigir-2026)
11. [CIKM 2025](#11-cikm-2025)
12. [顶级实验室专题](#12-顶级实验室专题)

---

## 1. ICML 2025

> Vancouver, July 2025. 3,260 accepted (26.93% from 12,107 submissions).

### 1.1 SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training

- **Authors**: Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans, Quoc V Le, Sergey Levine, Yi Ma
- **Affiliation**: UC Berkeley, Google DeepMind
- **Key Innovation**: Proposed GeneralPoints (arithmetic reasoning card game) and V-IRL (visual navigation) to compare SFT vs RL generalization. Found SFT memorizes while RL generalizes to unseen variants.
- **Significance**: Foundational insight for post-training strategy selection.

### 1.2 MONA: Myopic Optimization with Non-myopic Approval

- **Authors**: Sebastian Farquhar, Vikrant Varma, David Lindner, David Elson, Caleb Biddulph, Ian Goodfellow, Rohin Shah
- **Affiliation**: Google DeepMind
- **Key Innovation**: Prevents multi-step reward hacking by separating myopic optimization from non-myopic approval. Avoids agents learning undesired multi-step plans that receive high reward.
- **Results**: Effective at mitigating reward hacking even when humans cannot detect undesired behavior.

### 1.3 Ladder-Residual: Parallelism-Aware Architecture for Accelerating LLM Inference

- **Authors**: Muru Zhang, Mayank Mishra, William Brandon, Tri Dao et al.
- **Affiliation**: Stanford, Together AI, Princeton
- **Key Innovation**: Redesigns model architecture to decouple communication from computation in tensor parallelism. Enables communication-computation overlapping.
- **Significance**: Practical architecture optimization for large-scale LLM inference.

### 1.4 Improving the Scaling Laws of Synthetic Data with Deliberate Practice

- **Highlight**: Explores how deliberate practice (targeted, iterative refinement) improves synthetic data scaling beyond naive generation.
- **Affiliation**: Multiple top labs

### 1.5 rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking

- **Key Innovation**: Self-evolution framework for small LLMs to achieve math reasoning mastery without teacher distillation.

### 1.6 Star Attention: Efficient LLM Inference over Long Sequences

- **Key Innovation**: Novel attention mechanism for efficient long-sequence LLM inference.

### 1.7 PaperBench: Evaluating AI's Ability to Replicate AI Research

- **Authors**: Multiple (OpenAI)
- **Key Innovation**: Benchmark for evaluating AI agents' ability to replicate state-of-the-art AI research papers.

---

## 2. AAAI 2026

> Singapore, Jan 20-27, 2026. ~29K submissions (23K after policy filtering), ~48 proceedings volumes.

### 2.1 FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards

- **Venue**: AAAI-26 Technical Track on Machine Learning I
- **Key Innovation**: Federated version of GRPO for privacy-preserving foundation model post-training. Enables distributed RL fine-tuning without sharing raw data.
- **Significance**: Bridges federated learning with reasoning-oriented RL post-training.

### 2.2 EfficientFlow: Efficient Equivariant Flow Policy Learning for Embodied AI

- **Key Innovation**: Equivariant flow matching for robotic policy learning with improved sample efficiency.

### 2.3 RaCoT: Plug-and-Play Contrastive Example Generation for Enhanced LLM Reasoning Reliability

- **Key Innovation**: Contrastive example generation mechanism that plugs into existing LLMs to improve reasoning reliability without retraining.

### 2.4 Inference Scaling Law for Retrieval Augmented Generation

- **Key Innovation**: First formal scaling law analysis for RAG systems, characterizing how retrieval quality and number of retrieved documents affect downstream performance.

### 2.5 Entropy Alignment: Reinforcing Structured Uncertainty in LLM Reasoning

- **Key Innovation**: Aligns LLM reasoning with entropy-based uncertainty estimates for more calibrated outputs.

### 2.6 The Avengers: A Routing Recipe for Collective Intelligence in LLMs

- **Key Innovation**: Routing strategy that combines multiple LLMs for collective intelligence, outperforming individual models.

### 2.7 Mosaic Pruning: Hierarchical Pruning of Mixture-of-Experts Models

- **Key Innovation**: Hierarchical framework for generalizable pruning of MoE models.

### 2.8 AdaptCLIP: Adapting CLIP for Universal Visual Anomaly Detection

- **Authors**: Bin-Bin Gao et al.
- **Affiliation**: Tencent (Youtu Lab)
- **Key Innovation**: Adapts CLIP for anomaly detection across diverse visual domains without task-specific training.

### 2.9 MedLA: Logic-Driven Multi-Agent Framework for Complex Medical Reasoning

- **Key Innovation**: Multi-agent LLM framework combining logical reasoning for complex medical diagnosis.

### 2.10 GraphRAG-Induced Dual Knowledge Structure Graphs for Personalized Learning

- **Key Innovation**: Combines GraphRAG with dual knowledge graphs for educational recommendation.

---

## 3. ICLR 2026

> 5,343 accepted (26.97% from 19,809 submissions). 223 orals. Singapore, Apr 2026.

### 3.1 Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling

- **Type**: Oral
- **Key Innovation**: Decouples reasoning length rewards from answer correctness, with curriculum scheduling to reduce overthinking in LLMs.

### 3.2 Mastering Sparse CUDA Generation through Pretrained Models and Deep RL

- **Type**: Oral
- **Key Innovation**: Uses Deep RL to train models for Sparse CUDA kernel generation. Bridges code generation with systems optimization.

### 3.3 Half-order Fine-Tuning for Diffusion Model: A Recursive Likelihood Ratio Optimizer

- **Type**: Oral
- **Key Innovation**: Novel half-order optimization method for diffusion model fine-tuning using recursive likelihood ratio estimation.

### 3.4 Reducing Belief Deviation in RL for Active Reasoning of LLM Agents

- **Type**: Oral
- **Key Innovation**: Reduces belief deviation in LLM agent reasoning through RL-based active information gathering.

### 3.5 LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning

- **Type**: Oral
- **Key Innovation**: Produces coherent ultra-long texts (100K+ tokens) using RL without supervised long-form data.

### 3.6 MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent

- **Type**: Oral
- **Key Innovation**: Multi-conv RL memory agent for effective long-context management in LLMs.

### 3.7 Actions Speak Louder than Prompts: LLMs for Graph Inference

- **Type**: Oral
- **Key Innovation**: Large-scale study showing LLMs perform better at graph inference through actions rather than prompts.

### 3.8 Let Features Decide Their Own Solvers: Hybrid Feature Caching for Diffusion Transformers

- **Type**: Oral
- **Key Innovation**: Hybrid feature caching strategy where different features automatically select optimal solvers in Diffusion Transformers.

### 3.9 TileLang: Bridge Programmability and Performance in Modern Neural Kernels

- **Type**: Oral
- **Key Innovation**: DSL and compiler for neural network kernels that balances programmability with high performance.

### 3.10 LLM Fingerprinting via Semantically Conditioned Watermarks

- **Type**: Oral
- **Key Innovation**: Watermarking technique for LLMs based on semantic conditioning, enabling model fingerprinting.

### 3.11 Verifying Chain-of-Thought Reasoning via Its Computational Graph

- **Type**: Oral
- **Key Innovation**: Formal verification of CoT reasoning by constructing and analyzing computational graphs.

### 3.12 RAIN-Merging: Enhancing Instruction Following in Large Reasoning Models

- **Type**: Oral
- **Key Innovation**: Gradient-free model merging method that enhances instruction following while preserving thinking format.

### 3.13 GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models

- **Type**: Oral
- **Key Innovation**: Efficient inference-time alignment for flow and diffusion models using reward-guided sampling.

### 3.14 Huxley-Gödel Machine: Human-Level Coding Agent via Optimal Self-Improvement

- **Type**: Oral
- **Key Innovation**: Self-improving coding agent architecture inspired by Gödel machine, achieving human-level coding performance.

### 3.15 ∇-Reasoner: LLM Reasoning via Test-Time Differentiation (∇-REASONER)

- **Key Innovation**: Applies differentiable test-time gradient descent in token space for LLM reasoning. 20%+ accuracy improvement on math benchmarks with 10-40% fewer model calls.
- **Theory**: Shows inference-time gradient descent in sample space is dual to KL-regularized RL.

### 3.16 TEMPO: Scaling Test-time Training for Large Reasoning Models

- **Key Innovation**: EM-based actor-critic test-time training. Improves Qwen3-14B from 42.3% to 65.8% on AIME 2024.

### 3.17 ACTIVATIONREASONING: Reasoning in Latent Activation Spaces

- **Key Innovation**: Embeds logical reasoning in SAE-derived latent activation spaces. Outperforms GPT-4o and DeepSeek-R1-8B on multi-hop reasoning.

### 3.18 NeoBERT: A Next Generation BERT

- **Venue**: ICLR 2026 Journal Track
- **Key Innovation**: Modernized BERT architecture incorporating contemporary design choices.

### 3.19 Chimera: State Space Models Beyond Sequences

- **Venue**: Journal Track
- **Key Innovation**: Extends SSMs beyond sequential data to general graph-structured data.

### 3.20 Tabby: A Language Model Architecture for Tabular and Structured Data Synthesis

- **Venue**: Journal Track
- **Key Innovation**: Specialized LLM architecture for tabular data generation and structured data synthesis.

---

## 4. CVPR 2026

> Denver, June 3-7, 2026. 4,090 accepted (25.42% from 16,092 submissions). 42% growth over CVPR 2025.

### 4.1 Key Trends

- **Multimodal LLMs & VLMs** (+5.7pp share, now largest sub-field at 10.6%)
- **Video Generation & World Models** (+5.0pp)
- **Embodied AI / Robotics** (+3.3pp)
- Detection, segmentation, depth all shrank in share

### 4.2 Highlighted Papers

#### 4.2.1 Pixo: In Pursuit of Pixel Supervision for Visual Pre-training

- **Authors**: Lihe Yang, Shang-Wen Li, Yang Li, Kaiming He, Hu Xu et al.
- **Affiliation**: Meta AI, MIT
- **Key Innovation**: Self-supervised visual model trained purely by predicting pixels. Competitive with contrastive and masked-image modeling approaches.

#### 4.2.2 ARCache: Caching-based Acceleration for Autoregressive Video Diffusion Models

- **Key Innovation**: First training-free caching framework for autoregressive video diffusion. Mitigates error accumulation in long video generation.

#### 4.2.3 HiSpatial: Taming Hierarchical 3D Spatial Understanding in VLMs

- **Key Innovation**: Improves 3D spatial reasoning in vision-language models through hierarchical spatial representations.

#### 4.2.4 Improving Vision-language Models with Perception-centric Process Reward Models

- **Key Innovation**: Process reward models that focus on perceptual quality of intermediate VLM reasoning steps.

#### 4.2.5 LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning

- **Key Innovation**: Extends diffusion language models to visual instruction following, bridging diffusion LMs with multimodal tasks.

#### 4.2.6 SynMotion: Semantic-Visual Adaptation for Motion Customized Video Generation

- **Key Innovation**: Semantic-visual adaptation for motion-controllable video generation.

#### 4.2.7 GenieDrive: Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation

- **Key Innovation**: Driving world model that uses 4D occupancy to guide physics-aware video generation.

#### 4.2.8 SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model

- **Key Innovation**: Pixel-anchored latent diffusion for efficient and scalable image generation.

#### 4.2.9 GDRO: Group-level Reward Post-training for Diffusion Models

- **Key Innovation**: Group-level reward optimization for post-training diffusion models, analogous to RLHF for LLMs.

#### 4.2.10 StructXLIP: Enhancing Vision-language Models with Multimodal Structural Cues

- **Key Innovation**: Injects structural cues (edges, depth, segmentation) into vision-language pretraining.

#### 4.2.11 Circuit Tracing in Vision-Language Models: Understanding Multimodal Thinking

- **Authors**: UIUC
- **arXiv**: 2602.20330
- **Key Innovation**: Traces internal circuit mechanisms of VLM multimodal reasoning, revealing how vision and language integrate.

#### 4.2.12 Cupid: Generative 3D Reconstruction via Joint Object and Pose Modeling

- **Key Innovation**: Jointly models object shape and camera pose for generative 3D reconstruction.

#### 4.2.13 Iris: Bringing Real-World Priors into Diffusion

- **Key Innovation**: Incorporates real-world physical priors into diffusion models for more physically plausible generation.

#### 4.2.14 Reconstructing 3D Scenes from Egocentric Interaction Videos

- **Key Innovation**: 4D reconstruction of 3D scenes from egocentric video with human-object interactions.

---

## 5. EMNLP 2025

> Suzhou, China, November 2025. 1,811 Main (22.16%) + 1,417 Findings (17.34%) from ~8,174 commitments.

### 5.1 DeepResearcher: Scaling Deep Research via RL in Real-world Environments

- **Key Innovation**: Applies RL to train LLM agents for deep research tasks, learning to search, read, and synthesize information.

### 5.2 OpenRLHF: A Ray-based Scalable RLHF Framework

- **Key Innovation**: Open-source distributed RLHF framework built on Ray. Supports large-scale RL training for LLM alignment.

### 5.3 A Systematic Analysis of Base Model Choice for Reward Modeling

- **Authors**: Kian Ahrabian et al.
- **Key Innovation**: Comprehensive analysis of how base model selection affects reward model quality in RLHF.

### 5.4 Preemptive Detection and Correction of Misaligned Actions in LLM Agents

- **Key Innovation**: Preemptive approach to detect and correct misalignment in LLM agent actions before execution.

### 5.5 MixLoRA-DSI: Dynamically Expandable Mixture-of-LoRA Experts for Generative Retrieval

- **Key Innovation**: Dynamic LoRA expert routing for generative retrieval over evolving document corpora.

### 5.6 From Problem-Solving to Teaching Problem-Solving: Aligning LLMs with Pedagogy via RL

- **Key Innovation**: Uses RL to train LLMs as pedagogical tutors that teach problem-solving rather than just solving.

### 5.7 Fingerprinting LLMs through Survey Item Factor Correlation

- **Key Innovation**: Survey-based method for fingerprinting LLMs using factor correlation patterns.

### 5.8 RAVEN++: Fine-Grained Violations in Advertisement Videos with Active Reinforcement Reasoning

- **Key Innovation**: Active RL reasoning for detecting policy violations in advertising video content.

---

## 6. ACL 2026 / EACL 2026

### 6.1 ACL 2026 — Accepted Papers (Selected)

#### 6.1.1 Teams of LLM Agents can Exploit Zero-Day Vulnerabilities

- **Key Innovation**: Demonstrates LLM agent teams successfully exploiting zero-day security vulnerabilities, raising important safety considerations.

#### 6.1.2 Online Difficulty Filtering for Reasoning Oriented Reinforcement Learning

- **Key Innovation**: Dynamic difficulty filtering for RL training data selection to improve reasoning capabilities.

#### 6.1.3 Adaptive LLM: Early-Exit and Instant Confidence

- **Key Innovation**: Early-exit strategies with confidence estimation for efficient LLM inference.

#### 6.1.4 CrossThink: Scaling Self-Learning beyond Math Reasoning

- **Key Innovation**: Extends self-learning/self-play reasoning beyond mathematics to broader NLP tasks.

#### 6.1.5 Safety of Large Language Models Beyond English

- **Key Innovation**: Systematic literature review of LLM safety risks, biases, and safeguards in non-English contexts.

#### 6.1.6 DeepTrans: Deep Reasoning Translation via Reinforcement Learning

- **Authors**: Jiaan Wang, Fandong Meng, Jie Zhou
- **Venue**: TACL 2026
- **Key Innovation**: Uses RL (reasoning-oriented) to improve machine translation quality by deep reasoning over source text.

#### 6.1.7 H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents

- **Key Innovation**: Hierarchical memory architecture enabling efficient long-term reasoning for LLM agents.

### 6.2 EACL 2026 — Findings (Selected)

#### 6.2.1 WorkForceAgent-R1: Incentivizing Reasoning Capability in LLM-based Web Agents via RL

- **Key Innovation**: RL fine-tuning to incentivize reasoning in web agents performing workforce tasks.

#### 6.2.2 Being Kind Isn't Always Being Safe: Diagnosing Affective Hallucination in LLMs

- **Key Innovation**: Identifies "affective hallucination" where LLMs produce emotionally pleasing but factually incorrect content.

#### 6.2.3 Joint Multimodal Preference Optimization for Fine-Grained Visual-Textual Alignment

- **Key Innovation**: Preference optimization jointly over visual and textual modalities for fine-grained multimodal alignment.

---

## 7. KDD 2026

> Jeju, Korea, Aug 9-13, 2026. Keynote: Jeff Dean (Google), Jingren Zhou (Alibaba), Regina Barzilay (MIT).

### 7.1 Accepted Papers (from OpenReview)

#### 7.1.1 Self-Evolving Recommendation System: End-to-End Autonomous Model Optimization with LLM Agents

- **Authors**: Google DeepMind / YouTube Team
- **arXiv**: 2602.10226
- **Abstract**: Framework where LLM agents (Gemini 2.5 Pro) autonomously generate, train, and deploy improvements to YouTube's recommendation models. Offline agent generates hypotheses, online agent validates in production.
- **Key Results**: Multiple successful production launches at YouTube. Outperforms human MLEs in development velocity.
- **Innovation**: First end-to-end autonomous LLM-driven evolution of production recommendation systems.

#### 7.1.2 ULTRA-HSTU: Scaling Sequential Recommendation at Meta

- **Authors**: Meta Recommendation Systems
- **arXiv**: 2602.16986
- **Abstract**: Next-generation HSTU model with end-to-end model-system co-design. Incorporates sparse attention, mixed precision, and dynamic topology.
- **Key Results**: 5× faster training scaling, 21× faster inference scaling. Deployed at Meta serving billions of users. 4-8% consumption/engagement improvements.
- **Innovation**: Applies DeepSeek-V2 style system co-design to recommendation transformers.

#### 7.1.3 Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation

- **Authors**: Meta Ads
- **arXiv**: 2602.10016
- **Abstract**: Unified architecture establishing first predictable scaling laws for joint sequence-nonsequence modeling. GDPA, HSP, Sliding Window Attention, CompSkip.
- **Key Results**: MFU 17% → 37% on B200, 2× scaling efficiency over SOTA. 1.2% topline metric improvement. Deployed at major Meta Ads models.
- **Innovation**: First predictable power-law scaling for joint sequence-context recommendation.

#### 7.1.4 SOLARIS: Speculative Offloading for Foundation Model Inference at Meta Ads

- **Authors**: Meta
- **arXiv**: 2604.12110
- **Abstract**: Speculative decoding-inspired framework precomputing user-item embeddings for ads serving. Hierarchical feature enrichment.
- **Key Results**: 0.09% BCE loss reduction, 0.67% revenue gain (~$100M). Transfer ratio 42-44%.
- **Innovation**: Applies speculative decoding principles to recommendation inference scaling.

#### 7.1.5 HILL: Hierarchical Index Learning for Foundation Retrieval Models at Meta

- **Authors**: Meta Ads Platform
- **arXiv**: 2604.12965
- **Abstract**: Learns hierarchical index over retrieval model memory using cross-attention and residual quantization. Supports test-time training for inference upgrade.
- **Deployment**: Serves billions of Facebook/Instagram users.

#### 7.1.6 LLaTTE: Scaling Laws for Sequence Models in Production Recommendation

- **Authors**: Meta
- **arXiv**: 2505.04421, 2601.20083
- **Abstract**: Multi-stage architecture with upstream (45× FLOPs) and online lightweight ranking. Systematic scaling laws study.
- **Key Results**: 0.25% NE improvement on revenue models. Transfer ratio ≈ 50%. Scaling laws follow log-linear trends.

#### 7.1.7 LLM Retrieval for Stable and Predictable Ad Recommendations

- **Authors**: Multiple
- **arXiv**: 2605.21969
- **Abstract**: Semantic candidate generation framework using fine-tuned LLMs for ads retrieval. Graph-based expansion for creative variants.
- **Innovation**: New stability/predictability metrics for ads recommendation evaluation.

#### 7.1.8 AgenticTagger: Generating Structured Item Representation for Recommendation with LLM Agents

- **Authors**: Google DeepMind et al.
- **arXiv**: 2602.05945
- **Abstract**: Multi-agent framework for generating hierarchical descriptor vocabularies for items. Architect LLM + annotator LLMs in a reflection loop.
- **Results**: Consistent improvements in generative retrieval, ranking, and critique-based recommendation.

#### 7.1.9 User Feedback Alignment for LLM-powered Exploration in Large-scale RecSys

- **Authors**: Google DeepMind / YouTube
- **arXiv**: 2504.05522
- **Abstract**: Decouples novelty and user-alignment with separate LLMs. Inference-time scaling with best-of-n selection.
- **Results**: Significant gains in watch activity and exploration diversity.

#### 7.1.10 Discovering Multiagent Learning Algorithms via AlphaEvolve

- **Authors**: Google DeepMind
- **arXiv**: 2602.16928
- **Abstract**: Uses LLM-driven evolutionary search (AlphaEvolve) to automatically discover new multi-agent learning algorithms (VAD-CFR, SHOR-PSRO).

#### 7.1.11 VRec: Verifiable Reasoning for LLM-based Recommendation

- **Authors**: Meta MRS / NUS
- **arXiv**: 2603.07725
- **Abstract**: Reason-verify-recommend paradigm with mixture of verifiers for multi-dimensional user preference verification.

#### 7.1.12 FlexRec: Adapting LLM-based Recommenders for Flexible Needs via RL

- **arXiv**: 2603.11901
- **Abstract**: RL post-training framework with swap-based item-level rewards for adapting LLM recommenders to diverse recommendation needs.

#### 7.1.13 Reasoning to Rank (R2Rank): End-to-End RL for LLM Ranking

- **arXiv**: 2602.12530
- **Abstract**: Unifies CoT reasoning with listwise ranking optimization via Plackett-Luce differentiable surrogate and RL.

#### 7.1.14 From Logs to Language: Learning Optimal Verbalization for LLM Recommendation

- **arXiv**: 2602.20558
- **Abstract**: RL-based verbalization agent that transforms raw interaction logs into optimized textual context. 93% relative improvement in discovery item recommendation.

#### 7.1.15 GR4AD: Generative Recommendation for Large-Scale Advertising (Kuaishou)

- **Authors**: Kuaishou
- **arXiv**: 2602.22732
- **Abstract**: Production-oriented generative recommender with UA-SID tokenization, LazyAR decoder, VSL, and RSPO (ranking-guided RL).
- **Key Results**: 4.2% ad revenue improvement. <100ms latency, 500+ QPS per L20. Deployed at Kuaishou serving 400M+ users.

#### 7.1.16 HyFormer: Unified CTR Prediction at ByteDance

- **Authors**: ByteDance (Douyin Search)
- **arXiv**: 2601.12681
- **Abstract**: Unified hybrid transformer integrating long-sequence modeling and feature interaction. Query Decoding + Query Boosting.
- **Key Results**: Tested on 3B-sample Douyin dataset. Outperforms LONGER + RankMixer baselines.

#### 7.1.17 LONGER: Ultra-Long User Behavior Sequence Modeling at ByteDance

- **Authors**: ByteDance
- **arXiv**: 2505.04421
- **Abstract**: Transformer framework for modeling ultra-long behavior sequences with hybrid causal attention, mixed-precision, KV cache serving.
- **Key Results**: Douyin Ads: +1.06~2.1% ADSS. Douyin E-Commerce: +4.6~7.9% Order/U, +5.3~6.5% GMV/U. Deployed across dozens of scenarios at ByteDance.

#### 7.1.18 TokenMixer-Large: Scaling Up Ranking Models at ByteDance

- **Authors**: ByteDance
- **arXiv**: 2602.06563
- **Abstract**: Evolved architecture with mixing-and-reverting, inter-layer residuals, Sparse Per-token MoE. Scaled to 7B (online) / 15B (offline).
- **Key Results**: +2.0% ADSS (advertising), +2.98% GMV (e-commerce), +1.4% revenue (live streaming).

#### 7.1.19 OneMall: Generative Recommender Family at Kuaishou E-commerce

- **Authors**: Kuaishou
- **arXiv**: 2601.21770
- **Abstract**: Unified generative recommendation for product-card, short-video, and live-streaming. Semantic tokenizer + Pure Transformer + RL distillation.
- **Key Results**: +14.7% GMV (Product-Card), +10.3% GMV (Short-Video), +4.9% GMV (Live-Streaming). Serves 400M+ DAU.

#### 7.1.20 UniMixer: Unified Architecture for Scaling Laws in Recommendation (Kuaishou)

- **Authors**: Kuaishou
- **arXiv**: 2604.00590
- **Abstract**: Unified theoretical framework bridging attention, TokenMixer, and FM-based methods. Best scaling efficiency on Kuaishou ads.
- **Key Results**: CAD D1-D30 increased by 15%+ across multiple scenarios.

#### 7.1.21 GenRec: Preference-Oriented Generative Framework (JD.com)

- **Authors**: JD.com (Alimama)
- **arXiv**: 2604.14878 (SIGIR '26)
- **Abstract**: Generative retrieval with SID-based representation, asymmetric Token Merger, GRPO-SR for preference alignment.
- **Key Results**: 9.5% click and 8.7% transaction improvements. Deployed on JD App.

#### 7.1.22 GFlowGR: Generative Flow Networks for Taobao Recommendation (Alibaba)

- **Authors**: CityU / Alibaba
- **arXiv**: 2506.16114
- **Abstract**: GFlowNet-based fine-tuning framework for generative recommendation. Trajectory sampler + reward model + GFlowNet loss.
- **Key Results**: Deployed across all Taobao search advertising since May 2025. 0.43% total revenue increase ($100M+ annually).

#### 7.1.23 DAIAN: Deep Adaptive Intent-Aware Network for CTR at Alibaba (Xianyu)

- **Authors**: Alibaba (Xianyu / Alimama)
- **arXiv**: 2602.13971
- **Abstract**: Adaptive intent-aware CTR prediction in trigger-induced recommendation scenarios.
- **Key Results**: 1.59% CTR increase, 1.73% recommendation diversity, 2.37% bills increase in online A/B test.

---

## 8. RecSys 2025

> Prague, Sep 2025. Full papers + Industry + Short papers.

### 8.1 Selected Full Papers

#### 8.1.1 Heterogeneous User Modeling for LLM-based Recommendation

- **Authors**: Honghui Bao, Wenjie Wang, Fuli Feng, Tat-Seng Chua et al. (NUS / USTC)
- **Key Innovation**: Compression enhancer + masking mechanism for modeling heterogeneous user behaviors in LLM-based recommendation.

#### 8.1.2 MoRE: Mixture of Reflectors for LLM-based Sequential Recommendation

- **Authors**: Weicong Qin et al.
- **Key Innovation**: Three perspective-aware reflectors (intra-user explicit, intra-user implicit, cross-user CF) with meta-reflector and contextual bandit selection.

#### 8.1.3 GenSAR: Unifying Balanced Search and Recommendation with Generative Retrieval

- **Authors**: Teng Shi, Jun Xu et al. (Renmin University / Kuaishou)
- **Key Innovation**: Single generative model unifying search and recommendation tasks.

#### 8.1.4 Enhancing Sequential Recommender with LLMs for Joint Video and Comment Recommendation (Kuaishou)

- **Authors**: Bowen Zheng, Zihan Lin et al. (Renmin University / Kuaishou)

#### 8.1.5 RESA: Language Model-Based Playlist Generation (EURECOM)

#### 8.1.6 Scalable Agentic Approach to Query Understanding at Spotify

- **Authors**: Enrico Palumbo et al. (Spotify)
- **Key Innovation**: Agentic architecture combining search and recommendation at Spotify scale.

### 8.2 Industry Track Highlights

#### 8.2.1 LLM-RecG: Semantic Bias-Aware Zero-Shot Sequential Recommendation (UIUC)

#### 8.2.2 Balancing Fine-tuning and RAG for Dynamic LLM Recommendation Updates (Meta)

#### 8.2.3 Semantic Embedding Stability in Recommendation Systems (Meta, Pinterest)

#### 8.2.4 Scaling Retrieval: Inverted Indexes to Embedding Search (Meta)

- **Authors**: Yuchin Juan et al. (Meta)
- **Key Innovation**: Practical lessons from scaling retrieval infrastructure at web scale.

---

## 9. WWW 2026

> Dubai, Jun 29 - Jul 3, 2026 (rescheduled from April). 676 accepted (20.06% from 3,370 submissions).

### 9.1 ThinkRec: Thinking-based Recommendation via LLM

- **arXiv**: Published at WWW 2026
- **Key Innovation**: Shifts LLM4Rec from System 1 (intuitive) to System 2 (rational). Thinking activation + instance-wise expert fusion.

### 9.2 Industry Track Papers

#### 9.2.1 PI2I: Personalized Item-Based Collaborative Filtering (Alibaba)

- **Authors**: Shaoqing Wang et al. (Alibaba Group)

#### 9.2.2 GPU-accelerated Multi-relational Parallel Graph Retrieval (Baidu)

- **Authors**: Zhuoning Guo et al. (HKUST Guangzhou / Baidu)

---

## 10. SIGIR 2026

> Melbourne, Jul 20-24, 2026. 234 accepted (18.41% from 1,271 submissions).

### 10.1 Selected Papers

#### 10.1.1 KnowSA: Knowledge-aware Selective Augmentation for LLM Recommenders

- **Venue**: SIGIR 2026
- **arXiv**: 2604.07825
- **Key Innovation**: Comparative Knowledge Probing (CKP) to estimate LLM item knowledge and selectively augment only knowledge-poor items.

#### 10.1.2 NumColBERT: Non-Intrusive Numeracy Injection for Late-Interaction Retrieval

- **Authors**: Haruki Fujimaki, Makoto P. Kato
- **Key Innovation**: Injects numerical reasoning into ColBERT-style late interaction retrieval models.

#### 10.1.3 Total Recall QA: Verifiable Evaluation Suite for Deep Research Agents

- **Authors**: Mahta Rafiee, Hamed Zamani et al. (UMass CIIR)
- **Key Innovation**: Benchmark for evaluating comprehensive information retrieval in deep research agent scenarios.

#### 10.1.4 AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning

- **Authors**: Hongru Song et al. (UvA IRLab / CAS)
- **Key Innovation**: Shows how a single poisoned document can corrupt LLM reasoning via retrieval augmentation.

#### 10.1.5 Learning to Reason for Multi-Step Retrieval of Personal Context

- **Authors**: Maryam Amirizaniani et al. (UMass CIIR)
- **Key Innovation**: RL-based reasoning for multi-step personal context retrieval in QA.

---

## 11. CIKM 2025

> Seoul, Nov 10-14, 2025.

### 11.1 Award Winners

- **Best Full Paper**: Reconsidering the Performance of GAE in Link Prediction
- **Best Applied Paper**: Climber: Toward Efficient Scaling Laws for Large Recommendation Models
- **Best Resource Paper**: Semantic IDs in Generative Recommendation: A Practitioner's Handbook
- **Best Student Full Paper**: A Cost-Effective Framework to Evaluate LLM-Generated Relevance Judgements

### 11.2 Selected Papers

#### 11.2.1 STARec: Efficient Agent Framework for RecSys via Autonomous Deliberate Reasoning

- **Authors**: Chenghao Wu et al. (Renmin University / Huawei)

#### 11.2.2 M-LLM3REC: Motivation-based LLM Interaction Framework for Recommendation

#### 11.2.3 Maximum In-Support Return Modeling for Dynamic Recommendation with LM Prior

#### 11.2.4 CCAgent: Coordinating Collaborative Data Scaling for OS Agents via Web3

#### 11.2.5 LLM-Enhanced Generalized Category Discovery via Dynamic Graph Diffusion

---

## 12. 顶级实验室专题

### 12.1 Google DeepMind

| Paper | Venue | Area |
|-------|-------|------|
| Self-Evolving RecSys (Gemini 2.5 Pro at YouTube) | KDD 2026 | RecSys / Agents |
| Discovering Multiagent Learning Algorithms | KDD 2026 | Game Theory / RL |
| AgenticTagger (Structured Item Representation) | KDD 2026 | RecSys |
| User Feedback Alignment for LLM Exploration | KDD 2026 | RecSys |
| AutoHarness (Code Harness Synthesis for Agents) | - | Agents / Code |
| Subgoal-driven Framework for Long-Horizon Agents (MiRA) | - | Agents / RL |
| DeepSearchQA (Agent Evaluation Benchmark) | - | Evaluation |
| ProEval (Generative AI Evaluation) | - | Evaluation |
| TRecViT (Recurrent Video Transformer) | - | Video / Vision |

### 12.2 OpenAI

| Paper | Venue | Area |
|-------|-------|------|
| Unit Distance Problem Solved by AI (open math problem) | - | Math / Reasoning |
| GeneBench (Genomics Agent Benchmark) | - | Benchmark / Biology |
| Accidental CoT Grading Analysis | - | RL / Safety |
| Investigating CoT Monitorability During RL | - | Alignment |
| TEMPO (with external collaboration) | ICLR 2026 | Test-time Training |
| ORCA (Online Reasoning Calibration) | ICLR 2026 | Reasoning |

### 12.3 Meta AI / Meta Ads / Meta RecSys

| Paper | Venue | Area |
|-------|-------|------|
| ULTRA-HSTU (Next-gen sequential recommendation) | KDD 2026 | RecSys |
| Kunlun (Scaling laws for RecSys) | KDD 2026 | RecSys / CTR |
| SOLARIS (Speculative inference for ads) | KDD 2026 | Ads / Inference |
| HILL (Hierarchical Index Learning) | KDD 2026 | Retrieval |
| LLaTTE (Multi-stage sequence scaling) | KDD 2026 | RecSys / Scaling |
| VRec (Verifiable reasoning for LLM RecSys) | KDD 2026 | RecSys |
| Pixo (Pixel-supervised visual pretraining) | CVPR 2026 | Vision |
| LMRL Gym (multi-turn RL with LMs) | ICML 2025 | RL / LLM |

### 12.4 NVIDIA

| Paper | Venue | Area |
|-------|-------|------|
| Nemotron 3 Super (120B MoE Hybrid Mamba-Transformer) | - | LLM |
| Introspective Training (IXT: 2.8× FLOP efficiency) | - | LLM Training |
| DiLaDiff (Distilled Latent-Augmented Diffusion LM) | - | Diffusion |

### 12.5 Anthropic

| Paper | Venue | Area |
|-------|-------|------|
| Emotion Concepts in Claude Sonnet 4.5 | - | Interpretability |
| Natural Language Autoencoders (NLAs) | - | Interpretability |
| Teaching Claude Why (Agentic Misalignment Reduction) | - | Alignment / Safety |

### 12.6 ByteDance (Douyin)

| Paper | Venue | Area |
|-------|-------|------|
| HyFormer (Unified CTR Transformer) | KDD 2026 | CTR |
| LONGER (Ultra-long sequence modeling) | KDD 2026 | RecSys / Sequence |
| TokenMixer-Large (7B-15B scaling) | KDD 2026 | CTR / Scaling |

### 12.7 Kuaishou

| Paper | Venue | Area |
|-------|-------|------|
| GR4AD (Generative Recommendation for Ads) | KDD 2026 | Ads / Generative |
| OneMall (E-commerce Generative RecSys) | KDD 2026 | E-commerce |
| UniMixer (Unified Scaling Architecture) | KDD 2026 | CTR / Scaling |

### 12.8 Alibaba (Taobao, Xianyu, Alimama)

| Paper | Venue | Area |
|-------|-------|------|
| GFlowGR (GFlowNet for Taobao Ads) | KDD 2026 | Generative RecSys |
| GenRec (Generative Retrieval at JD.com) | SIGIR 2026 | Generative RecSys |
| DAIAN (Intent-aware CTR at Xianyu) | CIKM 2025 | CTR |
| PI2I (Personalized CF at Taobao) | WWW 2026 | RecSys |

### 12.9 Microsoft Research

| Paper | Venue | Area |
|-------|-------|------|
| From Hidden Profiles to Governable Personalization | - | RecSys / Policy |

### 12.10 Apple

| Paper | Venue | Area |
|-------|-------|------|
| Lookahead Training (Latent lookahead for LLM reasoning) | ICLR 2026 | LLM Training |

---

## 13. 核心主题趋势分析

### 13.1 LLM 推理与后训练

- **RL post-training 全面主流化**: GRPO 及其变体成为推荐系统、广告排序、Agent 训练的标准范式
- **Test-time training/scale 爆发**: TEMPO, ∇-Reasoner, ORCA 等工作将推理时计算作为核心扩展维度
- **Chain-of-Thought 安全与监控**: OpenAI 和 Anthropic 均发布了对 CoT 安全性的重要研究

### 13.2 推荐系统的 LLM 化

- **生成式推荐全面落地**: Kuaishou (GR4AD, OneMall)、JD (GenRec)、Alibaba (GFlowGR) 均在大规模生产环境部署
- **缩放定律正式建立**: Meta (Kunlun, LLaTTE)、Kuaishou (UniMixer)、ByteDance (TokenMixer-Large) 独立建立了推荐系统的缩放定律
- **LLM Agent × RecSys**: Google (Self-Evolving RecSys, AgenticTagger)、Meta (ULTRA-HSTU) 使用 LLM Agent 自主优化推荐模型

### 13.3 AI Agent

- **多智能体学习自动化**: Google DeepMind 使用 AlphaEvolve 自动发现多智能体算法
- **长程推理 Agent**: Subgoal/MiRA 框架显著提升 Web Agent 在长程任务上的表现
- **Agent 安全**: Anthropic 对 Agentic Misalignment 的缓解工作取得显著进展

### 13.4 多模态与视觉

- **CVPR 2026 最大趋势**: MLLM/VLM (+5.7pp) 和视频生成/世界模型 (+5.0pp)
- **扩散模型后训练**: GDRO 等工作将 RLHF 范式引入扩散模型
- **3D/CAD 生成**: 创新工作在 3D 场景重建和生成方面取得进展

### 13.5 模型效率与缩放

- **MoE 架构升级**: Nemotron 3 Super、TokenMixer-Large 展示了 MoE 在 LLM 和 RecSys 中的大规模应用
- **低精度训练**: NVFP4 低精度预训练的可行性得到 Nemotron 3 Super 验证
- **推理效率**: $1/\mathcal{W}$ 定律揭示了上下文窗口路由在 LLM 推理能效中的关键作用

---

*Report generated 2026-05-26 based on arXiv, conference proceedings, OpenReview, and official conference websites.*
