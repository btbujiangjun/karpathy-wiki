---
title: "Conference Digest 2025–2026: Major ML/AI Proceedings Overview"
type: synthesis
created: 2026-07-08
updated: 2026-07-08
sources: []
tags: [conference-digest, icml2026, aaai2026, neurips2025, iclr2026, kdd2026, cvpr2026, acl2026, emnlp2025, sigir2026, www2026, recsys2025]
---

# Conference Digest 2025–2026: Major ML/AI Proceedings Overview

> Comprehensive survey of notable papers from top ML/AI conferences (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, RecSys 2025). Coverage spans LLMs, recommendation systems, advertising/CTR, agents, multimodal, generative models, and more.

---

## Table of Contents

1. [NeurIPS 2025 — December 2025, San Diego](#1-neurips-2025)
2. [EMNLP 2025 — November 2025, Suzhou](#2-emnlp-2025)
3. [AAAI 2026 — January 2026, Singapore](#3-aaai-2026)
4. [ICLR 2026 — April 2026, Brazil](#4-iclr-2026)
5. [WWW 2026 — April 2026](#5-www-2026)
6. [CVPR 2026 — June 2026, Denver](#6-cvpr-2026)
7. [KDD 2026 — August 2026, Jeju Island](#7-kdd-2026)
8. [ICML 2026 — July 2026](#8-icml-2026)
9. [ACL 2026 — July 2026](#9-acl-2026)
10. [SIGIR 2026 — July 2026, Melbourne](#10-sigir-2026)
11. [RecSys 2025 — September 2025, Prague](#11-recsys-2025)
12. [Cross-Conference Themes & Trends](#12-cross-conference-themes--trends)

---

## 1. NeurIPS 2025

**Date**: December 2–7, 2025 | **Location**: San Diego, CA + Mexico City | **Papers**: ~5,200 accepted (24.5% of ~21,575 submissions)

### 1.1 Best Paper: Gated Attention for Large Language Models

**Title**: Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
**Authors**: Qwen Team (Alibaba)
**Affiliation**: Alibaba / Qwen Team
**Links**: [arXiv:2505.06708](https://arxiv.org/abs/2505.06708) | [GitHub](https://github.com/qiuzh20/gated_attention)

**Abstract**: The first systematic study examining how attention gating affects LLM performance. The authors compared 30+ variants of 15B MoE models and 1.7B dense models trained on 3.5T tokens. The winning configuration — a head-specific, elementwise sigmoid gate inserted after Scaled Dot-Product Attention (SDPA) — consistently improves performance, training stability, allows larger learning rates, and improves scaling properties.

**Key Innovations**:
- **Attention Sink Mitigation**: Reduces BOS token attention from 46.7% to 4.8% (globally); in Layer 21 from 83% to 4%, Layer 23 from 41% to 1%
- **PPL Reduction**: 0.05–0.27 improvement depending on model and setting
- **Training Stability**: Substantially suppresses loss spikes during training
- **Long-Context Extrapolation**: Significantly improved

**Comparison with Prior Methods**: Previous gating work (Switch Heads, DeepSeek NSA) attributed gains to routing or sparse-attention designs without separately quantifying the gate's contribution. This paper isolated gating from confounding designs.

---

### 1.2 Best Paper Runner-Up: Reinforcement Learning with Verifiable Rewards

**Title**: Scaling Reinforcement Learning with Verifiable Rewards for LLM Reasoning
**Authors**: Kevin Wang et al.
**Affiliation**: Multiple institutions

**Abstract** (from summary): Examined large LLMs trained using RLVR (Reinforcement Learning with Verifiable Rewards). Found that while RLVR enhances sampling efficiency, it does not necessarily improve reasoning capabilities. Explored scaling RL policies dramatically from traditional 2-5 layers to over 1,000 layers using Contrastive RL.

---

### 1.3 Best Paper Runner-Up: Neural Scaling Laws via Superposition

**Title**: Neural Scaling Laws via Superposition
**Authors**: Yizhou Liu et al.
**Links**: [NeurIPS Blog](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)

**Abstract**: Investigated neural scaling laws linking them to representation superposition. Revealed that model performance scales inversely with width in a strong superposition regime.

---

### 1.4 Best Paper (Datasets & Benchmarks): Artificial Hivemind

**Title**: Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
**Authors**: Jiang et al.

**Abstract**: Introduced **Infinity-Chat**, a large-scale dataset of 26K diverse, real-world, open-ended user queries that admit a wide range of plausible answers. Presented the first comprehensive taxonomy for characterizing open-ended prompts posed to LMs (6 top-level categories, 17 subcategories). Revealed the "Artificial Hivemind" phenomenon — different models produce similar outputs, challenging the belief that temperature settings or ensemble models enhance output diversity.

---

### 1.5 SWE-RL: Advancing LLM Reasoning via RL on Software Evolution

**Title**: SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution
**Authors**: Yuxiang Wei et al.
**Affiliation**: Multiple institutions
**Links**: [arXiv:2502.18449](https://arxiv.org/abs/2502.18449)

**Abstract**: Enables LLMs to autonomously recover developer reasoning processes by learning from open-source software evolution data (code snapshots, code changes, issues, PRs). Llama3-SWE-RL-70B achieves **41.0% solve rate on SWE-bench Verified** — best reported for <100B LLMs, comparable to GPT-4o. Also shows generalized reasoning improvements on 5 out-of-domain tasks (coding, math, language understanding).

---

### 1.6 DAPO: Open-Source LLM RL System at Scale

**Title**: DAPO: An Open-Source LLM Reinforcement Learning System at Scale
**Links**: [OpenReview](https://openreview.net/forum?id=2a36EMSSTp)

**Abstract**: Open-source RL system for LLM training at scale, advancing the RLVR paradigm.

---

### 1.7 Additional Notable Papers (LLM Agents)

Selected from 47 LLM Agent papers:
- **AgentAuditor**: Human-level safety evaluation for LLM agents
- **Agentic Plan Caching**: Test-time memory for fast, cost-efficient LLM agents
- **Group-in-Group Policy Optimization**: Novel training paradigm for LLM agents
- **T1**: Tool-oriented conversational dataset for multi-turn agentic planning
- **SuffixDecoding**: Extreme speculative decoding for emerging AI applications

---

## 2. EMNLP 2025

**Date**: November 4–9, 2025 | **Location**: Suzhou, China | **Papers**: ~3,000+ accepted (from 8,000+ submissions)

### 2.1 s1: Simple Test-Time Scaling

**Title**: s1: Simple Test-time Scaling
**Authors**: Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, Tatsunori Hashimoto
**Affiliation**: Stanford University, University of Washington, Allen Institute for AI, Contextual AI
**Links**: [arXiv:2501.19393](https://arxiv.org/abs/2501.19393) | [GitHub](https://github.com/simplescaling/s1)

**Abstract**: The simplest approach to achieve test-time scaling and strong reasoning performance. Curated **s1K** — 1,000 questions with reasoning traces based on difficulty, diversity, and quality. Developed **budget forcing** to control test-time compute by forcefully terminating the model's thinking or extending it by appending "Wait." SFT on Qwen2.5-32B-Instruct with only 26 minutes of training on 16 H100 GPUs. **s1-32B exceeds o1-preview** on competition math by up to 27% (MATH and AIME24). Scaling from 50% → 57% on AIME24 with budget forcing.

**Key Innovation**: "Wait" token forcing leads models to double-check and fix incorrect reasoning steps — a remarkably simple but effective technique.

**Comparison**: Prior replication attempts used MCTS, multi-agent approaches, or large-scale RL (DeepSeek R1 used millions of samples). s1 achieves comparable o1-level performance with only 1,000 SFT samples.

---

### 2.2 S1 Extended Findings

**Full Paper**: [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1025/)
**Pages**: 20275–20321 (46 pages)

The paper demonstrates that sequential scaling (budget forcing) is substantially more effective than parallel scaling (majority voting). With budget forcing, the model operates in a different scaling paradigm — scaling test-time compute via parallel methods on the base model does not catch up.

---

## 3. AAAI 2026

**Date**: January 20–27, 2026 | **Location**: Singapore | **Submissions**: ~29,000 (record), ~23,000 after filtering | **Acceptance**: 4,167 papers

**Key Stats**: ~20,000 submissions from China; 75,000+ unique authors; largest areas: CV, ML, NLP.

### 3.1 Outstanding Papers (Selected)

#### LLM2CLIP
- **Type**: Outstanding Paper (Main Track)
- **Focus**: Multimodal learning, connecting LLMs with CLIP

#### ReconVLA
- **Type**: Outstanding Paper (Main Track)
- **Focus**: Vision-language-action models for robotics

#### CADYT: Causal Structure Learning
- **Type**: Outstanding Paper (Main Track)

### 3.2 LLM Reasoning (37 Papers)

Selected highlights:
- **Beyond ReAct**: Planner-centric framework for complex tool-augmented LLM reasoning
- **Graph of Verification**: Structured LLM reasoning verification with DAGs
- **MathSmith**: Forging synthetic problems with reinforced policy for extremely hard math reasoning
- **In-Token Rationality Optimization**: Accurate and concise LLM reasoning via self-feedback
- **SAPO**: Self-adaptive process optimization making small reasoners stronger
- **RPM-MCTS**: Knowledge retrieval as process reward model with MCTS for code generation

**Chinese Summary**: AAAI 2026 的 LLM 推理方向共有 37 篇论文，核心趋势包括：(1) 从 ReAct 范式向 Planner-Centric 架构演进；(2) 验证器（Process Reward Model）与 MCTS 的结合成为代码生成主流方案；(3) 小模型通过自适应过程优化（SAPO）获得推理能力提升。

### 3.3 LLM Agents (AAA14 2026)

- **EvoClaw**: Evaluating AI agents on continuous software evolution
- **MacArena**: Benchmarking computer use agents on macOS environment
- **Agent Omit**: Adaptive context omission for efficient LLM agents
- **NaviAgent**: Graph-driven bilevel planning for scalable tool orchestration

### 3.4 Recommender Systems (27 Papers)

- **Can Recommender Systems Teach Themselves?** Recursive self-improving framework with fidelity control
- **GCIB**: Graph contrastive information bottleneck for multi-behavior recommendation
- **Rethinking Contrastive Learning for Graph Collaborative Filtering**: Limitations and a simple remedy

### 3.5 Safety & Alignment (45 Papers)

- **BLM-Guard**: Explainable multimodal ad moderation with CoT and policy-aligned rewards
- **Dropouts in Confidence**: Moral uncertainty in human-LLM alignment

---

## 4. ICLR 2026

**Date**: April 2026 | **Location**: Brazil | **Submissions**: 19,809 | **Acceptance**: 5,343 (26.97%)

### 4.1 Notable Papers

#### ECF8: Exponent-Concentrated FP8
**Affiliation**: Lambda, Stanford, CMU, Google, NVIDIA, Microsoft
**Links**: [lambda.ai blog](https://lambda.ai/blog/iclr-2026-12-papers)

**Abstract**: Reveals that exponent values in trained model weights concentrate into just 2–3 bits of entropy out of FP8's 4 bits. **ECF8** exploits this via Huffman coding, achieving up to 26.9% memory savings on diffusion models and 177.1% throughput gains, losslessly scaling to 671B LLM parameters.

#### Principled RL for Diffusion LLMs (ESPO)
**Links**: [arXiv:2512.03759](https://arxiv.org/abs/2512.03759)

**Abstract**: Emerges from a sequence-level perspective for RL training of diffusion language models. Opens new paradigm for training diffusion-based text generation models.

#### In-The-Flow Agentic System Optimization
**Links**: [arXiv:2510.05592](https://arxiv.org/abs/2510.05592)

**Abstract**: Stanford and Google collaboration on effective planning and tool use for agent systems.

#### Latent Particle World Models
**Links**: [arXiv:2603.04553](https://arxiv.org/abs/2603.04553)

**Abstract**: Self-supervised object-centric stochastic dynamics modeling.

### 4.2 A*STAR CFAR Papers (16 Accepted)

Selected:
- **FZOO**: Fine-tuning speed within same order as Adam while using inference-level GPU memory
- **TS²**: Training with Sparsemax+, Testing with Softmax for accurate and diverse LLM fine-tuning
- **WaterDrum**: Watermark-based data-centric unlearning metric for LLMs

### 4.3 MMLab@NTU Papers (11 Accepted)

- **NEO**: From Pixels to Words — native vision-language primitives at scale
- **Visual Jigsaw Post-Training**: Improves MLLMs
- **SeedVR2**: One-step video restoration via diffusion adversarial post-training

---

## 5. WWW 2026

**Date**: April 2026

### 5.1 OneTrans: Unified Feature Interaction and Sequence Modeling

**Title**: OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender
**Authors**: Zhaoqi Zhang, Haolei Pei, Jun Guo, Tianyu Wang, Yufei Feng, Hui Sun, Shaowei Liu, Aixin Sun
**Affiliation**: ByteDance, Nanyang Technological University
**Links**: [arXiv:2510.26104](https://arxiv.org/abs/2510.26104) | [WWW 2026](https://www2026.org/)

**Abstract**: Unifies user-behavior sequence modeling and feature interaction into a single Transformer backbone. Uses unified tokenizer to convert both sequential and non-sequential attributes into a single token sequence. Mixed parameterization: shared params for sequential tokens, token-specific for non-sequential. Causal attention + cross-request KV caching. **5.68% lift in per-user GMV** in online A/B tests.

**Key Innovation**: First industrial system to fully unify the historically separate sequence modeling and feature interaction pipelines, enabling LLM-style optimizations (KV caching) for recommendation.

**Comparison with Prior Methods**: Previous approaches (Wukong, RankMixer for feature interaction; LONGER for sequences) operated on separate tracks, limiting bidirectional information exchange. OneTrans achieves unified optimization.

### 5.2 HAP: Heterogeneity-Aware Pre-ranking

**Title**: Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking in Recommender Systems
**Author**: ByteDance
**Links**: [arXiv:2603.03770](https://arxiv.org/abs/2603.03770)

**Abstract**: Novel pre-ranking approach accounting for candidate heterogeneity in large-scale recommender systems.

---

## 6. CVPR 2026

**Date**: June 3–7, 2026 | **Location**: Denver, CO | **Submissions**: 16,092 | **Acceptance**: ~4,090 (25.42%)

### 6.1 Best Paper: D4RT

**Title**: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
**Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
**Affiliation**: Google DeepMind, UCL, University of Oxford
**Links**: [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html)

**Abstract**: D4RT reconstructs geometry and motion of dynamic 4D scenes from video using a unified transformer architecture. Estimates depth, spatio-temporal correspondence, and full camera parameters, enabling independent and efficient probing of any 3D point in space and time. A lightweight, highly scalable method for efficient training and inference.

### 6.2 Best Student Paper: Native and Compact Structured Latents for 3D Generation

**Title**: Native and Compact Structured Latents for 3D Generation
**Links**: [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

**Abstract**: Novel approach for compact 3D representation enabling efficient 3D generation.

### 6.3 Key Trends

- **Multimodal LLMs doubled** as a share of accepted papers
- **Video generation papers grew 2.3x** year-over-year
- **Classic detection papers declined**
- **Major themes**: Dynamic scene reconstruction, 3D generative modeling, multimodal understanding, embodied AI, video generation

---

## 7. KDD 2026

**Date**: August 9–13, 2026 | **Location**: Jeju Island, South Korea | **Two review cycles**

### 7.1 Meta Lattice: Model Space Redesign

**Title**: Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations
**Authors**: Liang Luo, Yuxin Chen, Zhengyu Zhang, et al. (40+ authors)
**Affiliation**: Meta AI
**Links**: [arXiv:2512.09200](https://arxiv.org/abs/2512.09200)

**Abstract**: A recommendation framework centered around model space redesign that extends Multi-Domain, Multi-Objective (MDMO) learning. Combines cross-domain knowledge sharing, data consolidation, model unification, distillation, and system optimizations.

**Online Results**:
- 10% revenue-driving top-line metrics gain
- 11.5% user satisfaction improvement
- 6% boost in conversion rate
- 20% capacity saving

**Key Innovation**: Portfolios consolidation (36% of gain), data integration (11%), model unification (13%), efficiency optimization (23%), knowledge transfer (17%). Paradigm shift from siloed models to unified cross-domain representation.

### 7.2 CTR-Sink: Attention Sink for CTR Prediction

**Title**: CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction
**Authors**: UGaussian Lab et al.
**Links**: [arXiv:2508.03668](https://arxiv.org/abs/2508.03668) | [GitHub](https://github.com/UGUESS-lzx/CTR-SINK)

**Abstract**: Addresses "semantic fragmentation" — the mismatch between discrete user behavior sequences and coherent natural language in LM pre-training. Proposes behavior-level attention sinks tailored for recommendation, inserting sink tokens between consecutive behaviors with temporal distance signals. Two-stage training strategy + attention sink mechanism. Validated on industrial dataset, MovieLens, Kuairec.

### 7.3 Chinese Industry Papers at KDD 2026

From the Awesome-CTR-Scaling collection:

| Company | Paper | Direction | ArXiv |
|---------|-------|-----------|-------|
| **Alibaba** | FAT: Field-Aware Transformer for CTR | Scaling Law for CTR | 2511.12081 |
| **Alibaba** | LoopCTR: Loop Scaling Power for CTR | Training/Inference Decoupling | 2604.19550 |
| **Tencent** | Expand More, Shrink Less: Effective-Rank Dynamics | Dense Scaling | 2605.23191 |
| **ByteDance** | OneTrans (also WWW 2026) | Unified Sequence + Feature | 2510.26104 |
| **Kuaishou** | UniMixer: Unified Architecture for Scaling Laws | Unified Attention/Mixer/FM | 2604.00590 |

### 7.4 Tencent Uni-Rec Challenge @ KDD Cup 2026

Tencent hosted the **Uni-Rec Challenge**: "Towards Unifying Sequence Modeling and Feature Interaction for Large-scale Recommendation" with $885,000 total prize. Innovation awards for Unified Block Innovation ($45K) and Scaling Law Innovation ($45K).

---

## 8. ICML 2026

**Date**: July 2026 | **Papers**: ~1,846 noted in papernotes collection

### 8.1 LLM Agents (59 Papers)

Selected highlights:
- **AdaMEM**: Test-time adaptive memory for language agents
- **Agent Omit**: Adaptive context omission for efficient LLM agents
- **ACON**: Optimizing context compression for long-horizon LLM agents
- **AgentXRay**: White-boxing agentic systems via workflow reconstruction
- **CoDA-Bench**: Can code agents handle data-intensive tasks?
- **Memory is Reconstructed, Not Retrieved**: Graph memory for LLM agents
- **NaviAgent**: Graph-driven bilevel planning for scalable tool orchestration
- **MCP-Persona**: Evaluating LLM agent capabilities via environment simulation

### 8.2 Recommender Systems (11 Papers)

- **T-POP**: Test-time personalization with online preference feedback
- **RGMem**: Renormalization group-inspired memory evolution for language agents
- **Can Recommender Systems Teach Themselves?** Recursive self-improving framework
- **A Paired Testing Protocol**: Batch-conditioned refusal robustness in LLM serving

### 8.3 AI Safety (114 Papers)

- **LLM-Safety Evaluations Lack Robustness** (Position Paper): Systematically analyzes the LLM safety evaluation pipeline, identifies key issues and practical impact, proposes guidelines.
- **Position: AI Researchers Must Help Lead Arms Control**: Urges proactive technical research into military AI arms control.
- **Position: Neglecting the Sustainability of AI**: Warns about the global AI arms race.

### 8.4 Other Notable Papers

- **Byte Pair Encoding for Efficient Time Series Forecasting**: Pattern-centric tokenizer for time series, adapatively merges samples according to patterns. Delivers large gains in forecasting accuracy.
- **Excited Pfaffians**: Generalized neural wave functions across structure and state (Spotlight).
- **Inverse Entropic Optimal Transport**: Semi-supervised learning via data likelihood maximization.
- **One-Step Gradient Delay for Async Pipeline Parallelism**: Shows async PP can match synchronous baselines with Muon optimizer + Error Feedback.

---

## 9. ACL 2026

**Date**: June/July 2026 | **Papers**: ~2,400+ accepted

### 9.1 Coverage (from Paper Digest)

ACL 2026 continues trends in:
- **Scaling test-time compute for NLP tasks**
- **LLM evaluation and benchmarking**
- **Multilingual and cross-lingual methods**
- **Efficient fine-tuning and adaptation**
- **Retrieval-augmented generation (RAG)**

Notable papers (from listings):
- **EC-FUNSD**: Entity-centric benchmark for information extraction from visually-rich documents
- **Cultural alignment evaluation** in LLMs
- **Automated error discovery** in conversational AI

---

## 10. SIGIR 2026

**Date**: July 20–24, 2026 | **Location**: Melbourne, Australia

### 10.1 Agentic Spatio-Temporal Grounding

**Title**: Agentic Spatio-Temporal Grounding via Collaborative Reasoning
**Authors**: Joey Zhou, Zhao Heng et al.
**Affiliation**: A*STAR CFAR, Singapore
**Links**: [arXiv:2602.13313](https://arxiv.org/abs/2602.13313)

**Abstract**: Proposes the Agentic Spatio-Temporal Grounder (ASTG) framework for Spatio-Temporal Video Grounding (STVG) in open-world, zero-shot scenarios. Eliminates per-frame spatial annotation requirements in training and per-frame reasoning in inference.

### 10.2 Key Chinese Industry Papers at SIGIR 2026

| Company | Paper | Direction |
|---------|-------|-----------|
| **Alibaba** | SSR: Beyond Dense Connectivity — Explicit Sparsity for Scalable Recommendation | Scalable models |
| **Alibaba** | KARMA: Knowledge-Action Regularized Multimodal Architecture | Multimodal search |
| **ByteDance** | HeterRec: Heterogeneous Information Transformer for Sequential Recommendation | Sequential Rec |

---

## 11. RecSys 2025

**Date**: September 22–26, 2025 | **Location**: Prague, Czech Republic

**Key Papers**:
- **Language Model-Based Playlist Generation**: Using semantic clustering + transformer fine-tuning for playlist generation
- **Multi-Factor Collaborative Prediction**: Mining complex relationships between click and rating behaviors
- **Long-term Interest Modeling**: Papers on lifelong user behavior modeling at scale

### 11.1 LONGER (RecSys 2025 / ByteDance)

**Title**: LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders
**Affiliation**: ByteDance
**Links**: [arXiv:2505.04421](https://arxiv.org/abs/2505.04421)

**Abstract**: Scales ultra-long user behavior sequences beyond two-stage retrieval approaches for industrial recommendation.

---

## 12. Cross-Conference Themes & Trends

### 12.1 LLM Reasoning & Test-Time Compute

Across NeurIPS 2025, EMNLP 2025, AAAI 2026, and ICML 2026, the dominant trend is **test-time scaling** as a new axis of LLM capability. Key contributions:
- **s1** (EMNLP 2025): Budget forcing with "Wait" token — simplest scaling approach
- **RLVR** (NeurIPS 2025 Runner-up): RL with verifiable rewards for reasoning
- **MathSmith** (AAAI 2026): Synthetic problem forging for hard math
- **SWE-RL** (NeurIPS 2025): RL on software evolution data

### 12.2 Industrial Recommendation Scaling

A major wave of papers from Chinese tech companies (ByteDance, Alibaba, Tencent, Kuaishou) + Meta focused on **scaling ranking models**:

| Theme | Papers | Companies |
|-------|--------|-----------|
| Unified Sequence + Feature Interaction | OneTrans, MixFormer, HyFormer, TokenFormer | ByteDance, Tencent |
| Generative Recommendation | MTGR, MBGR, SIGMA, NSGR, R³-VAE | Alibaba, Meituan, ByteDance |
| Attention-Aware CTR | CTR-Sink (KDD), FAT (KDD) | Alibaba |
| Model Space Redesign | Meta Lattice (KDD) | Meta |
| Long Sequence Modeling | LONGER, IAT, ENCODE, VQL | ByteDance, Alibaba, Kuaishou |
| Loop Scaling | LoopCTR | Alibaba |

### 12.3 Gated Attention & Architecture Innovation

NeurIPS 2025 Best Paper (Gated Attention) has already been integrated into **Qwen3-Next** (deployed September 2025). This architectural innovation — simple sigmoid gating after SDPA — is expected to be adopted broadly across frontier LLMs.

### 12.4 LLM Agents Maturation

The agent ecosystem matured significantly across conferences:
- **ICML 2026**: 59 agent papers covering memory, orchestration, evaluation
- **NeurIPS 2025**: 39 agent papers on safety, planning, benchmarks
- **AAAI 2026**: Agent evolution (EvoClaw), computer use (MacArena), persuasion (TRAP)

### 12.5 4D/3D & Generative Vision

CVPR 2026 best paper (D4RT) and student best paper signal a shift toward **dynamic scene understanding** and **compact 3D representations**. Video generation papers grew 2.3× at CVPR 2026.

### 12.6 Efficiency as a First-Class Concern

Multiple papers tackle efficiency:
- **ECF8** (ICLR 2026): 26.9% memory savings via Huffman coding of FP8 exponents
- **Async Pipeline Parallelism** (ICML 2026): Matching synchronous baselines
- **Meta Lattice** (KDD 2026): 20% capacity saving at Meta scale
- **OneTrans** (WWW 2026): KV caching for recommendation

---

*Generated by comprehensive web search of conference proceedings, paper repositories, and analysis blogs. Individual paper details may be incomplete — verify against official proceedings for full accuracy.*
