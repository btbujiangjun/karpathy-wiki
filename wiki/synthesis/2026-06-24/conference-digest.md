---
title: Conference & arXiv Digest — June 2026
type: synthesis
created: 2026-06-24
updated: 2026-06-24
sources: [arxiv.org, openreview.net, blog.neurips.cc, blog.iclr.cc, aaai.org, sigir2026.org]
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, recsys-2025, llm, agent, recommendation, ctr, generative-model, benchmark]
---

# Conference & arXiv Digest — June 2026

> A comprehensive survey of recent papers from top ML/AI conferences and arXiv, covering LLMs, agents, recommendation systems, CTR prediction, generative models, benchmarks, and related domains. Focus on papers from Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top academic labs.

---

## 目录 Table of Contents

1. [NeurIPS 2025 最佳论文](#1-neurips-2025-best-paper-awards)
2. [ICLR 2026 杰出论文](#2-iclr-2026-outstanding-papers)
3. [AAAI 2026 杰出论文](#3-aaai-2026-outstanding-papers)
4. [ICML 2026 亮点](#4-icml-2026-highlights)
5. [CVPR 2026 亮点](#5-cvpr-2026-highlights)
6. [EMNLP 2025 最佳论文](#6-emnlp-2025-best--outstanding-papers)
7. [RecSys 2025 亮点](#7-recsys-2025-highlights)
8. [WWW 2026 / SIGIR 2026 亮点](#8-www-2026--sigir-2026-highlights)
9. [LLM 架构与推理 (arXiv 2026)](#9-llm-architecture--reasoning-arxiv-2026)
10. [Agent 系统与工具使用](#10-agent-systems--tool-use)
11. [推荐系统与 CTR 预估](#11-recommendation-systems--ctr-prediction)
12. [生成式模型 (扩散/AR/流匹配)](#12-generative-models-diffusion-ar-flow-matching)
13. [评测基准与 Scaling Law](#13-benchmarks--scaling-laws)
14. [中国 AI 实验室最新进展](#14-china-ai-lab-updates)
15. [参考文献汇总](#15-full-reference-list)

---

## 1. NeurIPS 2025 Best Paper Awards

**Conference:** NeurIPS 2025, San Diego, Dec 2025  
**Accepted:** Main + Datasets & Benchmarks  
**Best Papers:** 4 | **Runners-Up:** 3

### 1.1 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

| Field | Value |
|-------|-------|
| **Title (CN)** | 门控注意力：非线性、稀疏性与无注意力汇 |
| **Authors** | Zihan Qiu et al. |
| **Affiliation** | Alibaba Qwen Team |
| **Award** | Best Paper |
| **Links** | [OpenReview](https://openreview.net/forum?id=1b7whO4SfY) |

**Problem:** Standard softmax attention suffers from "attention sink" — certain activations grow excessively large, hindering learning and long-context performance.

**Method:** Adds a simple head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA). The gate introduces an extra nonlinearity and allows each attention head to dynamically decide whether to contribute, naturally suppressing unhelpful signals.

**Experiments:** Evaluated on 30 model variants including 15B MoE and 1.7B dense models trained on up to 3.5T tokens. Gated attention consistently outperforms ungated baselines in stability, scalability, and long-context extrapolation. The design is now used in Qwen3-Next models.

**Key Insight:** The gating mechanism alleviates attention sink by regulating information flow at both representation and interaction levels, enabling higher learning rates and better training stability.

### 1.2 Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)

| Field | Value |
|-------|-------|
| **Title (CN)** | 人工蜂群思维：语言模型的开放式同质性 |
| **Authors** | Liwei Jiang et al. |
| **Affiliation** | University of Washington, CMU, Allen Institute |
| **Award** | Best Paper (Datasets & Benchmarks) |
| **Links** | [OpenReview](https://openreview.net/forum?id=saDOrrnNTz) |

**Problem:** When millions of users ask similar questions to the same LLM, they receive remarkably similar answers. This raises concerns about diversity, creativity, and value pluralism in AI-augmented society.

**Method:** Introduces Infinity-Chat benchmark (26k open-ended queries + dense human annotations) and large-scale analysis of diversity across 70+ LLMs. Measures both intra-model repetition (same model gives similar answers) and inter-model homogeneity (different models converge on similar outputs).

**Key Findings:**
- Even with high temperature settings, LLMs produce homogeneous outputs
- Individual models repeat themselves constantly
- The "Artificial Hivemind effect" — AI is making everything sound the same

### 1.3 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

| Field | Value |
|-------|-------|
| **Title (CN)** | 千层网络自监督强化学习 |
| **Authors** | Kevin Wang et al. |
| **Affiliation** | - |
| **Award** | Best Paper |
| **Links** | [OpenReview](https://openreview.net/forum?id=32) |

**Problem:** Common assumption that RL is incompatible with very deep networks.

**Method:** Demonstrates that very deep (up to 1024-layer) self-supervised RL agents can achieve strong goal-reaching performance without explicit rewards. Uses contrastive, goal-conditioned self-supervision.

**Results:** Depth scaling yields 2–50x improvement in success rates and richer emergent behaviors in simulated tasks compared to current methods.

### 1.4 Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training

| Field | Value |
|-------|-------|
| **Title (CN)** | 扩散模型为何不记忆：隐式动态正则化的作用 |
| **Authors** | - |
| **Affiliation** | - |
| **Award** | Best Paper |
| **Links** | [OpenReview](https://openreview.net/forum?id=43) |

**Key Insight:** Proves that diffusion models' generalization stems from the dynamical regularization inherent in the denoising process, not from dataset properties or explicit regularization. The reverse SDE implicitly penalizes memorization while preserving generalization.

### 1.5 Runner-Up: Transductive Online Learning — A 30-Year-Old Open Problem Solved

| Field | Value |
|-------|-------|
| **Authors** | Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer |
| **Award** | Runner-Up |

**Contribution:** Resolves a 30-year-old open problem by proving the transductive mistake bound is Ω(√d) — an exponential improvement over previous logarithmic lower bounds. Establishes a quadratic gap between transductive and standard online learning.

### 1.6 Runner-Up: Superposition & Neural Scaling Laws

**Key Insight:** First-principles derivation of neural scaling laws from representation superposition. In the strong-superposition regime (more features than dimensions), loss scales as L ∝ 1/m with model width. Validated on OPT, Pythia, Qwen.

### 1.7 Runner-Up: RLVR & LLM Reasoning

**Key Question:** Does reinforcement learning truly expand LLM reasoning capabilities? Critical analysis showing that RLVR improves Pass@1 while degrading high-k Pass@k — raising concerns about diversity collapse in reasoning.

---

## 2. ICLR 2026 Outstanding Papers

**Conference:** ICLR 2026, Rio de Janeiro, April 23–27  
**Submissions:** 19,525 | **Accepted:** 5,357 (27.4%) | **Oral:** 223  
**Outstanding Papers:** 2 | **Honorable Mention:** 1

### 2.1 Transformers are Inherently Succinct

| Field | Value |
|-------|-------|
| **Title (CN)** | Transformer 本质上是简洁的 |
| **Authors** | Bergsträßer, Cotterell, Lin |
| **Award** | Outstanding Paper |
| **Links** | [arXiv:2510.19315](https://arxiv.org/abs/2510.19315) |

**Problem:** What is the fundamental representational advantage of the Transformer architecture over RNNs and other sequence models?

**Method:** Formal language theory analysis proving Transformers are **doubly exponentially** more succinct than finite automata, and **exponentially** more succinct than RNNs and LTL (Linear Temporal Logic).

**Key Results:**
- As a corollary, verifying properties of Transformers is EXPSPACE-complete — formally intractable
- Provides theoretical grounding for why Transformers outperform RNNs on tasks requiring long-range dependencies
- "Succinctness" measures how compactly a model can represent a given concept

### 2.2 LLMs Get Lost In Multi-Turn Conversation

| Field | Value |
|-------|-------|
| **Title (CN)** | 大模型在多轮对话中迷失 |
| **Authors** | Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville |
| **Affiliation** | - |
| **Award** | Outstanding Paper |
| **Links** | [arXiv:2505.06120](https://arxiv.org/abs/2505.06120) |

**Problem:** Most LLM training data is text completion or single-turn, but deployment is inherently multi-turn. There is a dissonant gap.

**Method:** Designed a scalable method to evaluate multi-turn capabilities across all mainstream LLMs. Analyzed 200,000+ simulated conversations.

**Key Findings:**
- Every mainstream LLM tested shows a **39% average drop** from single-turn QA to multi-turn dialogue
- Models tested: GPT-4o-mini, GPT-4o, o3, GPT-4.1, Claude 3 Haiku/3.7 Sonnet, Gemini 2.5 Flash/Pro, Llama 3.1-8B/3.3-70B/4 Scout, OLMo-2-13B, Phi-4, DeepSeek-R1, Cohere Command-A
- Decline is not due to reduced aptitude, but **reduced reliability** — models make early assumptions, emit premature "final answers," and cannot self-correct
- Once a wrong step is taken, the model "gets lost" and cannot recover

### 2.3 Honorable Mention: The Polar Express — Optimal Matrix Sign Methods for the Muon Algorithm

| Field | Value |
|-------|-------|
| **Authors** | Noah Amsel, David Persson, Christopher Musco, Robert M. Gower |
| **Award** | Honorable Mention |

**Contribution:** Optimal matrix sign methods and their application to the Muon optimizer, which has shown 2x computational efficiency over AdamW in LLM training (Moonshot AI).

---

## 3. AAAI 2026 Outstanding Papers

**Conference:** AAAI 2026, Singapore, January 20–27  
**Submissions:** 23,680 | **Accepted:** 4,167 (17.6%)  
**Outstanding Papers:** 5 (Main) + 2 (AI for Social Impact)

### 3.1 Model Change for Description Logic Concepts

**Authors:** Ana Ozaki, Jandson S Ribeiro

**Problem:** Modifying a description logic concept in light of models represented as pointed interpretations. Distinguishes three kinds of changes: eviction (removing models), reception (incorporating models), and revision (combined).

### 3.2 Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis

**Authors:** Nicholas Tagliapietra, Katharina Ensinger, Christoph Zimmer, Osman Mian

Real-world systems evolve in continuous time with complex causal dependencies. Proposes theoretical framework for learning causal structures from dynamical system data with score-based analysis.

### 3.3 ReconVLA: Visual-Linguistic-Action Model for Robotics

**Authors:** Chinese team (Westlake University, Zhejiang University, HKUST Guangzhou)

A visual-language-action (VLA) model for embodied intelligence, bridging visual perception, language understanding, and action planning.

### 3.4 LLM2CLIP: Multi-Temporal Representation Learning

**Authors:** Chinese team

Multi-temporal expression of forward directions using LLM-enhanced CLIP-style contrastive learning.

### 3.5 CADyT: Causal Discovery in Power Systems

Power system causal discovery using advanced AI methods for infrastructure applications.

### Notable: AAAI 2026 AI Review Pilot

AAAI 2026 ran the largest-ever live experiment in AI-assisted peer review. Partnered with OpenAI to generate AI reviews for **22,977 papers** in under 24 hours. AI output did not replace human reviewers — reports carried explicit AI labels, no numeric scores, and no accept/reject recommendations.

---

## 4. ICML 2026 Highlights

**Conference:** ICML 2026, Seoul, July 6–11  
**Accepted:** 6,500+ papers  
**Not yet held** (as of June 24, 2026)

### 4.1 Key Accepted Papers

#### FullStack-Agent: Unified Agent System for Full-Stack Coding
**Problem:** Production-level full-stack web applications are far more challenging than frontend-only generation, requiring careful data flow control, dependency understanding, and bug localization.

**Method:** Three-part system: (1) FullStack-Dev multi-agent framework with planning, code editing, navigation, and bug localization; (2) dynamic dependency resolution; (3) end-to-end testing.

#### TabICooL: Foundation Model for Tabular Data
**Innovations:**
- Novel synthetic data generation engine for high pretraining diversity
- New scalable softmax in attention improving generalization
- Optimized pretraining protocols replacing AdamW with Muon optimizer

#### Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control
**Authors:** Peihao Wang, Shan Yang et al.
**Links:** [arXiv:2603.09221](https://arxiv.org/abs/2603.09221)

Proposes optimal control framework for reasoning, bridging test-time compute scaling with hardware efficiency.

#### How does Chain of Thought decompose complex tasks?
**Authors:** Amrut Nadgir, Vijay Balasubramanian, Pratik Chaudhari
**Links:** [arXiv:2604.08872](https://arxiv.org/abs/2604.08872)

Theoretical analysis of how CoT decomposes tasks, providing insight into why it improves reasoning.

#### Theory-Level Autoformalization (Spotlight)
**Authors:** Marcus J. Min et al.
From isolated statements to unified formal knowledge bases — bridging natural language math to formal proofs.

#### CORAL: Correctness-Optimized Residual Activation Lens
**Authors:** Miranda Muqing Miao et al.
**Links:** [arXiv:2602.06022](https://arxiv.org/abs/2602.06022)

Transferrable and calibration-aware inference-time steering for LLMs.

#### Statistical Early Stopping for Reasoning Models
**Authors:** Yangxinyu Xie et al.
**Links:** [arXiv:2602.13935](https://arxiv.org/abs/2602.13935)

Principled early stopping criterion for reasoning models to balance compute cost and accuracy.

#### When to Trust the Cheap Check (Spotlight)
**Authors:** Shayan Kiyani et al.
**Links:** [arXiv:2602.17633](https://arxiv.org/abs/2602.17633)

Weak and strong verification for reasoning — metrics for incorrect acceptance, incorrect rejection, and strong-verification frequency.

### 4.2 ICML 2026 Tutorial

**"Adaptive Reasoning in LLMs: From Post-Training to Test-Time Learning"**
- Presenters: Akhil Arora, Nouha Dziri
- Covers the full spectrum from post-training alignment to test-time compute scaling

---

## 5. CVPR 2026 Highlights

**Conference:** CVPR 2026 (ongoing/happening June 2026)  
**Papers:** 4,068 accepted

### 5.1 Diffusion Transformers with Representation Autoencoders (RAE)

| Field | Value |
|-------|-------|
| **Authors** | Boyang Zheng, Nanye Ma, Shengbang Tong, Saining Xie |
| **Affiliation** | NYU |
| **Links** | [OpenReview (ICLR 2026)](https://openreview.net/pdf?id=0u1LigJaab) |

**Problem:** Most DiTs continue to rely on the original VAE encoder with outdated backbones, low-dimensional latent spaces, and weak representations from reconstruction-only training.

**Method:** Replaces VAE with pretrained representation encoders (DINO, SigLIP, MAE) paired with trained decoders — Representation Autoencoders (RAEs). Provides both high-quality reconstructions and semantically rich latent spaces.

**Results:** Achieves 1.51 FID at 256×256 (no guidance) and 1.13 FID (with guidance) on ImageNet — state-of-the-art among DiT variants.

### 5.2 SAM 3D: 3Dfy Anything in Images

**Authors:** Xingyu Chen, FU-JEN CHU et al.
Generalizes the SAM approach to 3D reconstruction from single images.

### 5.3 DROID-SLAM in the Wild

**Authors:** Moyang Li, Zihan Zhu, Marc Pollefeys, Daniel Barath
Robust visual SLAM system that works in diverse, unconstrained environments.

### 5.4 Faithful Contouring: Near-Lossless 3D Voxel Representation

**Authors:** Yihao Luo et al.
Sparse voxelized representation supporting 2048+ resolutions with distance errors at 10^-5 level.

---

## 6. EMNLP 2025 Best & Outstanding Papers

**Conference:** EMNLP 2025, Suzhou, China, November 4–9  
**Submissions:** 8,000+ | **Accepted:** 3,000+

### 6.1 Best Paper: Infini-gram mini

| Field | Value |
|-------|-------|
| **Title (CN)** | Infini-gram mini: 互联网规模精确 n-gram 搜索 |
| **Authors** | H. Xu, J. Liu, Choi, N. A. Smith, Hajishirzi |
| **Affiliation** | UW / AI2 |
| **Links** | [arXiv:2506.12229](https://arxiv.org/abs/2506.12229) |

**Problem:** Exact n-gram search at internet scale for contamination audits, membership inference, and grounding.

**Method:** FM-index–based system that makes 83 TB of text (Common Crawl Jan–Jul 2025, DCLM-baseline, Pile) exactly searchable by n-gram, with index size only 44% of the corpus.

### 6.2 Outstanding: PAFT — Prompt-Agnostic Fine-Tuning

**Authors:** Wei, Y. Shu, Ou, Y. He, F. R. Yu
**Links:** [arXiv:2502.12859](https://arxiv.org/abs/2502.12859)

**Key Idea:** Continually samples diverse synthetic prompts during SFT/RLFT so the model learns task-level structure rather than surface phrasing. +7% generalization to unseen prompts, 3.2× faster inference.

### 6.3 Outstanding: Constructions are Revealed in Word Distributions

**Authors:** Rozner, Weissweiler, Mahowald, Shain

Uses RoBERTa as a proxy for language distribution, showing that constructions (construction-grammar sense) are visible as patterns of statistical affinity.

### 6.4 Outstanding: To Mask or to Mirror

**Authors:** C. Qian, Parisi, Bouleau, Tsai, Lebreton, Dixon (Google)

748-participant "Lost at Sea" experiment matched with LLM groups (Gemini 2.5, GPT-4.1, Claude Haiku 3.5, Gemma 3). Some models mirror human demographic biases; others mask and over-correct. Collective alignment is model-specific.

### 6.5 Apple at EMNLP 2025

Apple presented research on:
- **Speculative Streaming:** Efficient and scalable speculative decoding with multi-stream attention
- **Bias after Prompting:** Persistent discrimination in LLMs even after prompt-level interventions

---

## 7. RecSys 2025 Highlights

**Conference:** RecSys 2025, Prague, September 22–26  
**Full proceedings:** 49 papers across research, industry, and late-breaking tracks

### 7.1 Lasso: LLM-Based User Simulator for Cross-Domain Recommendation

**Method:** Uses LLM agents to simulate user behavior across domains for cross-domain recommendation. Generates synthetic interaction data to augment training.

### 7.2 Scaling Laws of CTR Model for Online Performance Improvement

**Links:** [arXiv:2508.15326](https://arxiv.org/abs/2508.15326)

Empirical study of scaling laws in CTR models — how model size, data volume, and training compute affect online CTR metrics in production advertising systems.

### 7.3 Balancing Fine-tuning and RAG: A Hybrid Strategy for Dynamic LLM Recommendation Updates

**Links:** [arXiv:2510.20260](https://arxiv.org/abs/2510.20260)

Explores the trade-off between fine-tuning LLMs for recommendation and augmenting them with retrieval — proposes a hybrid approach that balances freshness, accuracy, and computational cost.

### 7.4 Beyond Immediate Click: Engagement-Aware and MoE-Enhanced Transformers

**Links:** [ACM](https://dl.acm.org/doi/10.1145/3705328.3748076)

Moves beyond click signals to model deeper engagement (watch time, dwell, completion) using mixture-of-experts enhanced transformers.

### 7.5 LEAF: Lightweight Embedding for Large-Scale Recommendation

**Links:** [ACM](https://dl.acm.org/doi/10.1145/3705328.3748078)

Novel embedding framework that achieves 10x compression with minimal accuracy loss, critical for deploying large-scale recommendation models on resource-constrained hardware.

### 7.6 You Say Search, I Say Recs — Spotify's Agentic Query Understanding

**Links:** [ACM](https://dl.acm.org/doi/10.1145/3705328.3748127)

Scalable agentic approach to query understanding and exploratory search at Spotify. Uses LLM agents to bridge the gap between explicit search and implicit recommendation.

---

## 8. WWW 2026 / SIGIR 2026 Highlights

### 8.1 WWW 2026 (The Web Conference)

**Notable papers in recommendation/advertising:**

- **Auto-bidding under Return-on-Spend Constraints with Uncertainty Quantification** — Jiale Han, Chun Gan et al. (Alibaba). ROI-constrained auto-bidding with uncertainty estimation for auction markets.
- **DARA: Few-shot Budget Allocation via RL-Finetuned LLMs** — Mingxuan Song et al. (Alibaba). In-context decision making for budget allocation across channels.
- **Generative Regression Based Watch Time Prediction for Short-Video** — Hongxu Ma et al. (Kuaishou). Watch time prediction using generative regression methods.
- **FeDecider: LLM-Based Federated Cross-Domain Recommendation** — Xinrui He et al. (UIUC). Cross-domain federated recommendation with LLM integration.
- **AgentDR: Dynamic Recommendation with Implicit Item-Item Relations** — Mingdai Yang et al. (Meta/Amazon). LLM-based agents for dynamic recommendation with discovered item relations.
- **ScotRec: Social Chain-of-Thought LLM Reasoning for Recommendation** — Kaibei Li et al. Social reasoning paths for recommendation via CoT.
- **SeaRAG: Reducing Hallucination via Statement-Entity Adaptive Ranking** — Xiaosong Yuan et al. RAG architecture that reduces hallucination through entity-aware ranking.

### 8.2 SIGIR 2026 (Melbourne, July 20–24)

**Accepted:** 234 papers from 1,271 submissions (18.41% acceptance rate)

**Notable recsys/IR papers from recent SIGIR cycles:**

- HeterRec: Heterogeneous Information Transformer for Scalable Sequential Recommendation (Hao Deng et al.)
- Dynamic Margin-based Contrastive Learning for Robust Negative Sampling in IR
- Aligning Web Query Generation with Ranking Objectives via DPO

---

## 9. LLM Architecture & Reasoning (arXiv 2026)

### 9.1 Mamba-3: Improved Sequence Modeling Using State Space Principles

| Field | Value |
|-------|-------|
| **Links** | [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) |
| **Date** | March 2026 |

**Innovation:** Improved SSM architecture building on Mamba-2 principles. Better handling of long-range dependencies with linear-time inference. Forms the basis for hybrid Mamba-Transformer models (e.g., Nemotron-3).

### 9.2 Nemotron 3 Super: Open, Efficient MoE Hybrid Mamba-Transformer

| Field | Value |
|-------|-------|
| **Affiliation** | NVIDIA |
| **Links** | [arXiv:2604.12374](https://arxiv.org/abs/2604.12374) |
| **Date** | April 2026 |

Open-source MoE hybrid combining Mamba state-space layers with Transformer attention. Designed for agentic reasoning tasks. Contains extensive ablations on multi-token prediction, NVFP4 pretraining, synthetic data, and post-training quantization.

### 9.3 Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

| Field | Value |
|-------|-------|
| **Affiliation** | - |
| **Links** | [arXiv:2605.22791](https://arxiv.org/abs/2605.22791) |
| **Date** | May 2026 |

Decouples the erase and write operations in linear attention, improving the expressiveness of recurrent linear attention while maintaining O(n) inference complexity.

### 9.4 MiniMax-M3 Series: Native Multimodal, Million Context

| Field | Value |
|-------|-------|
| **Affiliation** | MiniMax |
| **Links** | [arXiv:2605.26494](https://arxiv.org/abs/2605.26494) |
| **Date** | May 2026 |

Native multimodal (text+image+audio) model supporting million-token context. Achieves 80.5% SWE-bench Verified and strong multimodal reasoning.

### 9.5 DiffusionGemma: 4x Faster Text Generation

| Field | Value |
|-------|-------|
| **Affiliation** | Google DeepMind |
| **Links** | [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/) |
| **Date** | June 2026 |

Diffusion-based text generation model achieving 4x speedup over autoregressive Gemma by generating multiple tokens in parallel per denoising step.

### 9.6 DeepSeek V4 Pro & Flash

| Field | Value |
|-------|-------|
| **Affiliation** | DeepSeek |
| **Links** | [OpenRouter](https://openrouter.ai) |
| **Date** | May 2026 |

**V4 Pro:** 1.6T total / 49B active parameters, MIT-licensed. Top open-weights score on SWE-bench Verified (80.6%), tied with Gemini 3.1 Pro.
**V4 Flash:** 284B total / 13B active. Exceptional cost efficiency at $0.28/M output tokens.

### 9.7 Scaling Embeddings Outperforms Scaling Experts in Language Models

| Field | Value |
|-------|-------|
| **Links** | [arXiv:2601.21204](https://arxiv.org/abs/2601.21204) |
| **Date** | January 2026 |

Key finding: Scaling embedding dimensions provides more benefit per parameter than scaling the number of experts in MoE architectures. Challenges the dominant MoE scaling paradigm.

### 9.8 FLARE: Diffusion for Hybrid Language Model

| Field | Value |
|-------|-------|
| **Links** | [arXiv:2606.01774](https://arxiv.org/abs/2606.01774) |
| **Date** | June 2026 |

Systematic conversion framework for hybrid-attention LLMs to diffusion language models. Identifies transfer data quality as the primary determinant of capability preservation.

### 9.9 Attention Residuals

| Field | Value |
|-------|-------|
| **Affiliation** | Moonshot AI |
| **Links** | [arXiv:2603.15031](https://arxiv.org/abs/2603.15031) |
| **Date** | March 2026 |

Drop-in replacement for residual connections with consistent scaling gains across model sizes. Released with open-source implementation by Moonshot AI.

### 9.10 ERNIE 5.0 Technical Report

| Field | Value |
|-------|-------|
| **Affiliation** | Baidu |
| **Links** | [arXiv:2602.04705](https://arxiv.org/abs/2602.04705) |
| **Date** | February 2026 |

Baidu's latest LLM with enhanced multimodal understanding and generation capabilities.

---

## 10. Agent Systems & Tool Use

### 10.1 Coding Agents are Effective Long-Context Processors

| Field | Value |
|-------|-------|
| **Authors** | Weili Cao, Xunjian Yin, Bhuwan Dhingra, Shuyan Zhou |
| **Links** | [arXiv:2603.20432](https://arxiv.org/abs/2603.20432) |
| **Date** | March 2026 |

**Problem:** LLMs fail to effectively _process_ long context despite scaling to _access_ massive contexts via attention mechanisms. Performance degrades significantly as context length increases.

**Method:** Externalizes long-context processing from latent attention into explicit, executable interactions. Enables coding agents to organize text in file systems and manipulate it using native tools (code, terminal commands).

**Results:** Outperforms published SOTA by **17.3% on average** across 5 benchmarks spanning 188K to 3 trillion tokens. Key factors: native tool proficiency and file system familiarity.

### 10.2 TMAX: Simple Recipe for Terminal Agents

| Field | Value |
|-------|-------|
| **Authors** | Hamish Ivison, Junjie Oscar Yin, Rulin Shao |
| **Affiliation** | Allen Institute for AI, University of Washington |
| **Links** | [arXiv](https://arxiv.org/abs/2606.15231) |
| **Date** | June 2026 |

Dataset and RL recipe for training open-weight LLMs as terminal agents. TMAX-9B achieves 27.2% on Terminal-Bench 2.0, outperforming prior open-weight models under 10B parameters.

### 10.3 Agents' Last Exam (ALE)

| Field | Value |
|-------|-------|
| **Authors** | Xinyang Han et al. |
| **Affiliation** | UC Berkeley (Dawn Song group) |
| **Links** | [arXiv:2606.05405](https://arxiv.org/abs/2606.05405) |
| **Date** | June 2026 |

**Tasks:** 1,490 instances across 55 subfields, 13 industry clusters
**Hardest tier pass rate:** 2.6% average full pass (most configs: 0%)
**Codex with GPT-5.5:** 82% on Terminal-Bench, but 0% on Last-Exam tasks

**Significance:** The most challenging agent benchmark to date, testing real professional workflows (not trivia). Reveals a massive gap between benchmark performance and real-world agent capability.

### 10.4 General Agent Evaluation

| Field | Value |
|-------|-------|
| **Links** | [arXiv:2602.22953](https://arxiv.org/abs/2602.22953) |
| **Date** | February 2026 |

First systematic study comparing tool-calling, MCP, code-generation, and CLI agents on the same benchmarks with the same models. Contributes a unifying protocol, evaluation harness, and the first **Open General Agent Leaderboard**.

### 10.5 CUDA Agent: Large-Scale Agentic RL for CUDA Kernel Generation

| Field | Value |
|-------|-------|
| **Affiliation** | ByteDance Seed |
| **Links** | [ByteDance Seed](https://seed.bytedance.com/en/public_papers) |
| **Date** | February 2026 |

Applies RL at scale to train agents for high-performance CUDA kernel generation. Uses agentic RL to discover optimized CUDA kernels automatically.

### 10.6 FullStack-Agent (ICML 2026)

Unified multi-agent system for full-stack development with planning, code editing, navigation, and bug localization. Addresses the gap between frontend-only and full-stack agentic coding.

### 10.7 MedAgentGym (ICLR 2026 Oral)

**Links:** [OpenReview](https://openreview.net/forum?id=jHDZEUgS4r)

Scalable agentic training environment for code-centric reasoning in biomedical data science.

---

## 11. Recommendation Systems & CTR Prediction

### 11.1 CADET: Context-Conditioned Ads CTR Prediction With Decoder-Only Transformer

| Field | Value |
|-------|-------|
| **Authors** | Ruoyan Wang et al. |
| **Affiliation** | LinkedIn |
| **Links** | [arXiv:2602.11410](https://arxiv.org/abs/2602.11410) |
| **Date** | February 2026 |

**Problem:** Adapting generative transformer architectures to ads CTR prediction faces challenges: post-scoring contextual signals, offline-online consistency, and industrial scaling.

**Innovations:**
1. Context-conditioned decoding with multi-tower prediction heads (resolves chicken-and-egg problem between predicted CTR and ranking)
2. Self-gated attention mechanism adapting information flow
3. Timestamp-based RoPE capturing temporal relationships from seconds to months
4. Session masking preventing train-serve skew
5. Production engineering: tensor packing, sequence chunking, custom Flash Attention

**Results:** **11.04% CTR lift** in online A/B testing vs LiRank (DCNv2 + sequential encoder ensemble). Deployed on LinkedIn's advertising platform.

### 11.2 GenCTR: Generative Click-through Rate Prediction

| Authors | Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao |
|--------|----------------------------------------------------------------------------|
| Affiliation | Alibaba |
| Links | [arXiv:2507.11246](https://arxiv.org/abs/2507.11246) |

**Method:** Two-stage training: (1) generative pre-training for next-item prediction, (2) fine-tuning within a discriminative CTR framework. Deployed on one of the world's largest e-commerce platforms (Alibaba).

### 11.3 Unified Value Alignment for Generative Recommendation in Industrial Advertising

| Affiliation | Tencent |
|------------|---------|
| Links | [arXiv:2605.05803](https://arxiv.org/abs/2605.05803) |
| Date | May 2026 |

Addresses value alignment in generative recommendation for advertising — ensuring that generative recommendation outputs align with business metrics (CTR, CVR, GMV) while maintaining user experience.

### 11.4 RecGPT-Mobile: On-Device LLM for User Intent Understanding — Taobao

| Affiliation | Alibaba Taobao & Tmall Group |
|------------|-----------------------------|
| Links | [arXiv:2605.04726](https://arxiv.org/abs/2605.04726) |
| Date | May 2026 |

Predicts user's next search query from recent interaction behaviors. On-device deployment for low-latency intent understanding in feed recommendation.

### 11.5 FEDIN: Frequency-Enhanced Deep Interest Network

| Affiliation | Tencent |
|------------|---------|
| Links | [arXiv:2605.01726](https://arxiv.org/abs/2605.01726) |
| Date | May 2026 |

Addresses the challenge of capturing latent periodic patterns in user interests using frequency-domain analysis combined with deep interest networks.

### 11.6 Meta: General Framework for Multimodal LLM in Large-Scale Recommendation

| Affiliation | Meta Platforms |
|------------|---------------|
| Links | [arXiv:2605.09338](https://arxiv.org/abs/2605.09338) |
| Date | May 2026 |

Framework for leveraging multimodal LLMs to extract high-dimensional semantic signals from multimedia content in large-scale recommendation systems.

### 11.7 Factorized Latent Reasoning for LLM-based Recommendation

| Affiliation | Meituan |
|------------|--------|
| Links | [arXiv:2604.26760](https://arxiv.org/abs/2604.26760) |
| Date | April 2026 |

Factorizes reasoning into latent steps for LLM-based recommendation, enabling more structured and interpretable recommendation decisions.

### 11.8 RecRM-Bench: Benchmarking Multidimensional Reward Modeling for Agentic Recommender Systems

| Affiliation | Meituan |
|------------|--------|
| Links | [arXiv:2605.11874](https://arxiv.org/abs/2605.11874) |
| Date | May 2026 |

Benchmark for evaluating reward models in agentic recommendation systems across multiple dimensions (accuracy, diversity, freshness, serendipity).

---

## 12. Generative Models (Diffusion / AR / Flow Matching)

### 12.1 NextFlow: Unified Sequential Modeling for Multimodal Generation

**Authors:** Huichao Zhang, Liao Qu et al.
**Links:** [arXiv:2601.02204](https://arxiv.org/abs/2601.02204)

Unified decoder-only autoregressive transformer trained on 6T interleaved text-image tokens. Uses next-token prediction for text, next-scale prediction for images. Generates 1024×1024 images in 5 seconds — orders of magnitude faster than comparable AR models.

### 12.2 ByteDance Seedance 2.0

ByteDance's video generation model maintaining top-tier global position. Native audio-visual joint generation. Training data pool of unprecedented scale with 2,000+ person review team.

### 12.3 ByteDance Seed3D 2.0

**Date:** April 2026
**Links:** [ByteDance Seed](https://seed.bytedance.com/en/public_papers)

State-of-the-art in both geometry and texture & material generation for simulation-ready 3D content.

### 12.4 CausalFusion: Causal Diffusion Transformers

**Authors:** Chaorui Deng et al.
**Links:** [arXiv:2412.12095](https://arxiv.org/abs/2412.12095)

Introduces Causal Diffusion as the autoregressive counterpart of diffusion models. Dual-factorizes data across sequential tokens and diffusion noise levels. SOTA on ImageNet generation.

### 12.5 PhyCo: Controllable Physical Priors for Generative Motion

**Affiliation:** CMU & NEC Labs America
Conditions video diffusion on physical property maps (friction, restitution, deformation, force). SOTA on Physics-IQ benchmark.

### 12.6 AdvDMD: Adversarial Reward Meets DMD for Few-Step Generation

**Affiliation:** Shanghai Jiao Tong University & Alimama Tech (Alibaba)
Unifies Distribution Matching Distillation with RL for high-quality few-step image generation.

---

## 13. Benchmarks & Scaling Laws

### 13.1 SWE-bench Pro (Scale AI)

**Links:** [arXiv:2509.16941](https://arxiv.org/abs/2509.16941)
**Tasks:** 1,865 across 41 repos (Python, Go, TypeScript, JavaScript)
**Top scores (June 2026):**
- MiniMax M3: 80.5% Verified
- DeepSeek V4-Pro-Max: 80.6% Verified
- Qwen3.7 Max: 80.4% Verified
- Claude Opus 4.8: 69.2% Pro

### 13.2 ScaleToT: Structured LLM Reasoning for Billion-Scale Low-Activity User Modeling

| Affiliation | - |
|------------|---|
| Links | [arXiv:2606.24622](https://arxiv.org/abs/2606.24622) |

Applies Tree-of-Thought reasoning at billion-user scale for modeling users with sparse interaction data.

### 13.3 Artificial Analysis Intelligence Index

Neutral composite index of 10 independent evaluations tracking open-weight model quality. Top scores (May 2026):
- Kimi K2.6: 54 (#4 overall)
- MiMo-V2.5-Pro (Xiaomi): 54
- DeepSeek V4 Pro: ~52

### 13.4 MetaSyn: Benchmarking LLM Agents on Meta-Analysis

| Links | [arXiv:2606.17041](https://arxiv.org/abs/2606.17041) |
|-------|------------------------------------------------------|

**Dataset:** 442 expert-curated meta-analyses from Nature Portfolio.
**Finding:** Despite 90.9% retrieval recall at K=200, no system recovers more than 52.7% of ground-truth literature — a critical screening bottleneck for LLM agents.

---

## 14. China AI Lab Updates

### 14.1 ByteDance Seed

**2026 Priorities:**
1. **World Models** — Release at least one world model by year-end, benchmark against Google's Genie 3
2. **Seedance** — Maintain top-tier video generation position
3. **Coding** — Strengthen foundation with CUDA Agent and coding models
4. **Doubao** — Accelerate commercialization (200M+ DAUs after Lunar New Year)

**Notable Papers:**
- CUDA Agent: Large-Scale Agentic RL for Kernel Generation
- UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation
- Mixture-of-Depths Attention
- Beyond Token Eviction: Mixed-Dimension Budget Allocation for KV Cache Compression
- Seed Diffusion: Large-Scale Diffusion Language Model with High-Speed Inference

### 14.2 Moonshot AI (Kimi)

**Recent Releases:**
- **Kimi K2.6**: Top open-weight model on Artificial Analysis Index (54). Modified MIT license.
- **Kimi K2.5**: Most powerful open-source multimodal agentic model
- **Kimi K2 Thinking**: 1T MoE, 32B active, 256K context. Outperforms GPT-5 and Claude Sonnet 4.5 on Humanity's Last Exam (44.9%) and BrowseComp (60.2%)

**Research Highlights:**
- **Attention Residuals**: Drop-in replacement for residual connections
- **Muon is Scalable for LLM Training**: 2x computational efficiency vs AdamW
- **Mooncake**: KV-centric disaggregated LLM serving (FAST 2025 Best Paper)
- **Kimi-VL**: MoE Vision-Language Model for multimodal reasoning

### 14.3 Alibaba (Qwen)

- **Qwen3.6**: Latest open-weight flagship under Apache-2.0
- **Qwen3.7-Max**: Closed-weight flagship, $2.50/$7.50 per 1M tokens
- Top scores on SWE-bench Verified (80.4%)
- Strong multimodal capabilities with Qwen-Image 2.0

### 14.4 DeepSeek

- **DeepSeek V4 Pro (1.6T/49B active)**: MIT-licensed, 80.6% SWE-bench Verified
- **DeepSeek V4 Flash (284B/13B active)**: Exceptional cost efficiency
- Aggressive pricing ($0.14/1M input tokens for Reasoner)
- Hired top researcher from DeepSeek by ByteDance for 100M RMB/year

### 14.5 Xiaomi (MiMo)

- **MiMo-V2.5-Pro**: 1T/42B active MoE, 1M context, Apache-2.0
- Ties Kimi K2.6 at 54 on Artificial Analysis Index
- MiMo-V2.5: 310B/15B active, scores 49

### 14.6 Zhipu AI (GLM)

- **GLM-5.1**: Leads overall rankings on BenchLM (85) and 77.8% SWE-bench Verified
- Cleanest MIT license among Chinese models
- GLM-5: 64 in coding benchmarks, 58.4% SWE-bench Pro (vendor-reported)

---

## 15. Full Reference List

### NeurIPS 2025 Best Papers
| # | Paper | Link |
|---|-------|------|
| 1 | Gated Attention for Large Language Models | [OpenReview](https://openreview.net/forum?id=1b7whO4SfY) |
| 2 | Artificial Hivemind | [OpenReview](https://openreview.net/forum?id=saDOrrnNTz) |
| 3 | 1000 Layer Networks for Self-Supervised RL | [OpenReview](https://openreview.net/forum?id=32) |
| 4 | Why Diffusion Models Don't Memorize | [OpenReview](https://openreview.net/forum?id=43) |
| 5 | Transductive Online Learning (Runner-Up) | [NeurIPS Blog](https://blog.neurips.cc/2025/11/26/) |
| 6 | Superposition & Scaling Laws (Runner-Up) | [NeurIPS Blog](https://blog.neurips.cc/2025/11/26/) |
| 7 | RLVR & LLM Reasoning (Runner-Up) | [NeurIPS Blog](https://blog.neurips.cc/2025/11/26/) |

### ICLR 2026 Outstanding Papers
| # | Paper | Link |
|---|-------|------|
| 1 | Transformers are Inherently Succinct | [arXiv:2510.19315](https://arxiv.org/abs/2510.19315) |
| 2 | LLMs Get Lost In Multi-Turn Conversation | [arXiv:2505.06120](https://arxiv.org/abs/2505.06120) |
| 3 | The Polar Express (Honorable Mention) | [ICLR Blog](https://blog.iclr.cc/2026/04/23/) |

### AAAI 2026 Outstanding Papers
| # | Paper | Link |
|---|-------|------|
| 1 | Model Change for Description Logic Concepts | [AAAI Proceedings](https://ojs.aaai.org) |
| 2 | Causal Structure Learning for Dynamical Systems | [AAAI Proceedings](https://ojs.aaai.org) |
| 3 | ReconVLA | - |
| 4 | LLM2CLIP | - |
| 5 | CADyT | - |

### Key arXiv Papers
| # | Paper | Link |
|---|-------|------|
| 1 | CADET (LinkedIn CTR) | [arXiv:2602.11410](https://arxiv.org/abs/2602.11410) |
| 2 | Coding Agents as Long-Context Processors | [arXiv:2603.20432](https://arxiv.org/abs/2603.20432) |
| 3 | Agents' Last Exam (ALE) | [arXiv:2606.05405](https://arxiv.org/abs/2606.05405) |
| 4 | General Agent Evaluation | [arXiv:2602.22953](https://arxiv.org/abs/2602.22953) |
| 5 | Mamba-3 | [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) |
| 6 | Nemotron 3 Super | [arXiv:2604.12374](https://arxiv.org/abs/2604.12374) |
| 7 | Gated DeltaNet-2 | [arXiv:2605.22791](https://arxiv.org/abs/2605.22791) |
| 8 | FLARE: Diffusion for Hybrid LM | [arXiv:2606.01774](https://arxiv.org/abs/2606.01774) |
| 9 | NextFlow | [arXiv:2601.02204](https://arxiv.org/abs/2601.02204) |
| 10 | DeepSeek V4 (via OpenRouter) | [OpenRouter](https://openrouter.ai) |

---

> **Overall Trends (H1 2026):**
> 1. **Agent systems dominate**: Coding agents, terminal agents, and general-purpose agents becoming the dominant paradigm for AI deployment
> 2. **Multi-turn reliability gap**: ICLR 2026 Outstanding Paper reveals 39% performance drop in multi-turn — a critical unsolved problem
> 3. **Gating mechanisms unify attention**: Gated Attention (NeurIPS 2025 Best Paper) being adopted across model families (Qwen3-Next)
> 4. **Hybrid architectures win**: Mamba-Transformer hybrids (Nemotron-3) outperforming pure Transformer or pure SSM
> 5. **China AI open-weight race**: Kimi, DeepSeek, Qwen, MiMo, GLM all releasing frontier-level open models within 30 days
> 6. **CTR going generative**: LinkedIn CADET, Alibaba GenCTR, and generative approaches showing 5-11% lifts over discriminative baselines
> 7. **RL for reasoning faces diversity collapse**: RLVR improves top-1 accuracy but degrades diversity (k>1 metrics)
> 8. **Diffusion language models advancing**: DiffusionGemma (4x speedup), FLARE framework enabling hybrid-attention dLLMs
> 9. **Agent evaluation maturing**: ALE, General Agent Eval, SWE-bench Pro providing comprehensive agent capability measurement
> 10. **Scaling debate continues**: Embedding scaling > expert scaling; superposition explains scaling laws; anti-scaling in video generation
