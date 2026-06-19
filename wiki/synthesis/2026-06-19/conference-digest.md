---
title: 2025-2026 Conference Digest — Major AI/ML Venues Paper Survey
type: synthesis
created: 2026-06-19
updated: 2026-06-19
tags: [conference-digest, survey, icml, neurips, iclr, aaai, kdd, cvpr, acl, emnlp, sigir, www, recsys, cikm]
sources: []
---

# 2025-2026 Conference Digest — Major AI/ML Venues Paper Survey

> Comprehensive survey of accepted/notable papers from ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, and recent arXiv preprints. Coverage: LLMs, Reasoning, RL, CTR Prediction, Recommendation, Agents, Generative Models, Benchmarks.

---

## Table of Contents

1. [LLM Architecture & Sequence Modeling](#1-llm-architecture--sequence-modeling)
2. [Reasoning & Test-Time Compute](#2-reasoning--test-time-compute)
3. [Reinforcement Learning for LLMs](#3-reinforcement-learning-for-llms)
4. [Agent Systems & Tool Use](#4-agent-systems--tool-use)
5. [CTR Prediction & Recommendation Scaling](#5-ctr-prediction--recommendation-scaling)
6. [Generative Models & Diffusion](#6-generative-models--diffusion)
7. [Computer Vision (CVPR 2026)](#7-computer-vision-cvpr-2026)
8. [NLP & Evaluation (ACL 2026 / EMNLP 2025)](#8-nlp--evaluation-acl-2026--emnlp-2025)
9. [Information Retrieval & Web (WWW 2026 / SIGIR 2026 / CIKM 2025)](#9-information-retrieval--web)
10. [Recommender Systems (RecSys 2025)](#10-recommender-systems-recsys-2025)
11. [Frontier Model Releases (May–June 2026)](#11-frontier-model-releases-mayjune-2026)
12. [Key Trends Summary](#12-key-trends-summary)

---

## 1. LLM Architecture & Sequence Modeling

### 1.1 Mamba-3: Improved Sequence Modeling using State Space Principles
- **Conference:** ICLR 2026 **Oral**
- **Authors:** Aakash Lahoti, Kevin Li, Berlin Chen, Caitlin Wang, Aviv Bick, Zico Kolter, Tri Dao, Albert Gu
- **Affiliation:** CMU, Princeton, etc.
- **Links:** [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) | [OpenReview](https://openreview.net/forum?id=HwCvaJOiCj)
- **Background:** Mamba-1/2 established SSMs as sub-quadratic alternatives to Transformers. However, they still lag behind on state-tracking tasks and suffer from hardware-inefficient decoding (only ~2.5 ops/byte arithmetic intensity).
- **Key Innovations:**
  1. **Exponential-Trapezoidal Discretization** — formalizes the heuristic Mamba-1/2 discretization as first-order "exponential-Euler" method; new second-order scheme yields O(Δt³) error vs. O(Δt²)
  2. **Complex-Valued State Spaces** — state update uses complex-valued dynamics, enabling richer state tracking (solves parity task that Mamba-2 failed)
  3. **MIMO (Multi-Input Multi-Output) Formulation** — improves model performance without increasing decode latency
- **Results:** At 1.5B scale: +0.6 accuracy pts vs Gated DeltaNet; MIMO variant adds another +1.2 pts. Comparable perplexity to Mamba-2 with half the state size.
- **Significance:** Sets the Pareto frontier for inference efficiency vs. quality among sub-quadratic architectures.

### 1.2 Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer
- **Conference:** arXiv preprint (also discussed at ICLR 2026)
- **Authors:** NVIDIA Research (large team)
- **Affiliation:** NVIDIA
- **Links:** [arXiv:2512.20856](https://arxiv.org/abs/2512.20856) | [Nemotron 3 Super PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)
- **Background:** Hybrid architectures combining attention layers with sub-quadratic alternatives are the dominant 2026 trend.
- **Key Innovations:**
  - Alternating Mamba-2 + Attention layers in Llama-style architecture
  - **LatentMoE** — efficient MoE routing
  - **Multi-Token Prediction (MTP)** layers for speculative decoding acceleration
  - Pretrained on 25T tokens with NVFP4 low-precision training
  - Post-training via diverse RL environments
- **Results:** Up to 2.2× higher throughput than GPT-OSS-120B while maintaining higher accuracy. Released in BF16/FP8/NVFP4 formats.
- **Nemotron 3 Ultra** (550B-A55B, released June 2026) — scales embedding/projection dimensions, most capable US open model (Intelligence Index 49 vs. Kimi K2.6 at 54).

### 1.3 Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention
- **Conference:** arXiv preprint (NVIDIA, May 2026)
- **Authors:** Ali Hatamizadeh, Yejin Choi, Jan Kautz
- **Affiliation:** NVIDIA
- **Links:** [NVIDIA Research](https://research.nvidia.com/publication/2026-05_gated-deltanet-2-decoupling-erase-and-write-linear-attention)
- **Key Innovation:** Decouples the erase and write operations in linear attention, resolving a key limitation of Gated DeltaNet where the same gating mechanism controlled both forgetting and updating.
- **Significance:** Used in Qwen3.6 as the non-attention hybrid component.

### 1.4 Variable-Width Transformers
- **Conference:** arXiv, Jun 2026
- **Links:** [arXiv (Jun 2026)](https://arxiv.deeppaper.ai/papers/weekly)
- **Key Innovation:** Challenges fixed-width-per-layer convention; allocates different widths per layer to match distinct computational roles. Reduces parameters while maintaining quality.

### 1.5 ParaRNN: Unlocking Parallel Training of Nonlinear RNNs for LLMs
- **Conference:** ICLR 2026
- **Affiliation:** Samsung/independent
- **Links:** [OpenReview](https://openreview.net/forum?id=MiV3WXDYJb) (partial)
- **Key Innovation:** Casts the sequence of nonlinear recurrence relationships as a single system of equations; solves in parallel using Newton's iterations. Achieves up to 665× speedup over naive sequential. Trains 7B LSTM/GRU models with perplexity comparable to Transformers and Mamba-2.

### 1.6 Nemotron-Labs-Diffusion: Tri-Mode Language Model
- **Conference:** arXiv, NVIDIA, May 2026
- **Links:** [NVIDIA Research](https://research.nvidia.com/publication/2026-05_nemotron-labs-diffusion-tri-mode-language-model-unifying-autoregressive)
- **Key Innovation:** Unifies autoregressive, diffusion, and self-speculation decoding in a single model. Enables flexible trade-off between speed and quality at inference time.

---

## 2. Reasoning & Test-Time Compute

### 2.1 Re²: Unlocking LLM Reasoning via RL with Re-solving
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Innovation:** Trains LLMs via pure RL to actively abandon invalid CoT chains and restart. Increases redo behavior from 0.5% to 30%+ of trajectories. Significantly outperforms standard RLVR with same compute budget.

### 2.2 Slow-Fast Policy Optimization (SFPO)
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Innovation:** Decomposes each training step into "fast trajectory → reposition → slow correction" three-stage structure. Plug-and-play enhancement for GRPO stability. Up to +2.80 points on math benchmarks, up to 4.93× rollout reduction.

### 2.3 CAPO: Curvature-Aware Policy Optimization
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Innovation:** Models second-order optimization geometry at the LM head's last layer; predicts and filters token updates that would cause policy collapse. Maintains stability at 5× learning rate and 1/12 batch size. 30× sample efficiency vs. standard GRPO on MATH.

### 2.4 The First Impression Problem: Internal Bias Triggers Overthinking
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Finding:** Reasoning models form a "first impression" (internal bias) on seeing the question. When this intuition conflicts with systematic reasoning, the model repeatedly self-doubts and re-checks, inflating reasoning length by 21–43%. All existing mitigation methods fail to fundamentally eliminate this effect.

### 2.5 The Illusion of Diminishing Returns: Measuring Long Horizon Execution
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Finding:** Short-task benchmarks give a false "diminishing returns" signal — small single-step accuracy gains amplify exponentially in long tasks. Discovers "self-conditioning effect" (own errors increase subsequent error probability). Thinking models can repair this; GPT-5 thinking executes 2100+ step tasks.

### 2.6 PoLR: Path of Least Resistance for LLM Reasoning
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Innovation:** First inference-time method leveraging reasoning prefix consistency. Clusters short prefixes and expands only the dominant cluster as an efficient alternative to Self-Consistency. Reduces token usage by 40–60% and latency by up to 50% while maintaining or improving accuracy.

### 2.7 Statistical Early Stopping for Reasoning Models
- **Conference:** ICML 2026
- **Authors:** Yangxinyu Xie, Tao Wang, Soham Mallick, et al.
- **Links:** [arXiv:2602.13935](https://arxiv.org/abs/2602.13935)
- **Key Innovation:** Applies statistical sequential analysis to determine when a reasoning model has generated enough thought tokens; early stopping without sacrificing accuracy.

### 2.8 A State-Transition Framework for Efficient LLM Reasoning
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Innovation:** Models reasoning as a state-transition process; uses Linear Attention to compress historical reasoning steps into a state matrix. Attention complexity O(C²)→O(C), KV cache O(C)→O(1). Momentum strategy mitigates overthinking from noisy reasoning steps.

---

## 3. Reinforcement Learning for LLMs

### 3.1 AREAL: Large-Scale Asynchronous RL for Language Reasoning
- **Conference:** NeurIPS 2025
- **Links:** [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/117538)
- **Key Innovation:** Asynchronous training where samplers and trainers operate on different GPU pools, eliminating synchronization overhead from heterogeneous response lengths. Near-linear scaling to large GPU clusters.

### 3.2 Long-RL: Scaling RL to Long Sequences (LongVILA-R1)
- **Conference:** NeurIPS 2025
- **Authors:** Yukang Chen, Wei Huang, Baifeng Shi, Qinghao Hu, et al.
- **Affiliation:** NVIDIA, UC Berkeley, HKU
- **Links:** [GitHub: NVlabs/Long-RL](https://github.com/NVlabs/Long-RL)
- **Key Innovation:** Multi-modal Reinforcement Sequence Parallelism (MR-SP) enabling hour-level video RL training (3,600 frames = 256k tokens) on a single node. Integrates sequence parallelism + vLLM engine with cached video embeddings.

### 3.3 RLVR Does Not Elicit Novel Reasoning Patterns
- **Conference:** NeurIPS 2025 (notable paper)
- **Affiliation:** Multiple institutions
- **Links:** [NeurIPS 2025 Best Paper Awards](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- **Key Finding:** Critical negative result: Current RLVR methods improve sampling efficiency toward correct paths but do NOT elicit fundamentally new reasoning patterns. Six popular RLVR algorithms perform similarly and remain far from optimal. Distillation can introduce new reasoning patterns from teachers; RLVR cannot.

### 3.4 TAMPO: Temperature Adaptive Meta Policy Optimization
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_reasoning)
- **Key Innovation:** Redefines sampling temperature as a learnable meta-policy. Two-loop structure: inner loop optimizes LLM policy, outer loop updates temperature distribution based on trajectory advantage. No extra rollout needed. Consistently outperforms fixed-temperature baselines.

### 3.5 1000 Layer Networks for Self-Supervised RL
- **Conference:** NeurIPS 2025 **🏆 Best Paper**
- **Links:** [OpenReview](https://openreview.net/forum?id=s0JVsx3bx1) | [arXiv:2503.14858](https://arxiv.org/abs/2503.14858)
- **Key Innovation:** Demonstrates that scaling depth (to 1000 layers) in self-supervised RL unlocks new goal-reaching capabilities not present in shallower networks.

### 3.6 AttnRL: Efficient Exploration for PSRL in Reasoning Models
- **Conference:** ICLR 2026
- **Links:** [OpenReview](https://openreview.net/forum?id=NCN8oUsiNf)
- **Key Innovation:** Uses attention scores to identify high-value branching positions; adaptive sampling accounting for problem difficulty and batch history. One-step off-policy training pipeline. Consistently outperforms prior PSRL approaches.

---

## 4. Agent Systems & Tool Use

### 4.1 A-MEM: Agentic Memory for LLM Agents
- **Conference:** NeurIPS 2025
- **Links:** [Paper Notes](https://en.papernotes.org/NeurIPS2025/llm_agent)
- **Key Innovation:** Zettelkasten-inspired agentic memory system. Each memory entry auto-generates structured notes (keywords/tags/contextual description); dynamic inter-memory links; evolutionary updates on new insertion. Significantly outperforms MemGPT on LoCoMo benchmark.

### 4.2 AgentAuditor: Human-Level Safety Evaluation for LLM Agents
- **Conference:** NeurIPS 2025
- **Links:** [Paper Notes](https://en.papernotes.org/NeurIPS2025/llm_agent)
- **Key Innovation:** Training-free, memory-augmented reasoning framework. Multi-stage context-aware RAG for safety/security evaluation. Introduces ASSEBench (2,293 records, 15 risk types, 29 scenarios). Achieves human expert-level evaluation accuracy.

### 4.3 Agentic Context Engineering (ACE)
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_agent)
- **Key Innovation:** Treats context as an evolving "playbook" via Generator-Reflector-Curator tri-role分工. Incremental delta updates. Solves brevity bias and context collapse in prompt optimization. Average +10.6% on agent tasks, +8.6% on finance tasks, 86.9% adaptive latency reduction.

### 4.4 WebOperator: Action-Aware Tree Search for Web Agents
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_agent)
- **Key Innovation:** Action-aware tree search with speculative backtracking, destructive action detection, action verification and merging. Enables safe exploration in partially-observable, irreversible real web environments. 54.6% SOTA success rate on WebArena with GPT-4o.

### 4.5 DeepSynth Benchmark for Information Synthesis
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_agent)
- **Key Innovation:** 120 real-world information synthesis tasks across 7 domains and 67 countries (avg 5.5 hours human annotation). Strongest agent (o3-deep-research) only achieves 8.97 F1 / 17.5% LLM-Judge.

### 4.6 Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents
- **Conference:** ICLR 2026
- **Links:** [Paper Notes](https://papernotes.org/ICLR2026/llm_agent)
- **Key Finding:** First systematic study of "Misevolution" — self-evolving agents can deviate from intended direction along four pathways (model, memory, tool, workflow). Even Gemini-2.5-Pro cannot avoid alignment degradation and vulnerability introduction.

### 4.7 Provably Reliable Tool-Using LLM Agents (MCP)
- **Conference:** AAAI 2026 Workshop (Trustworthy Agentic AI)
- **Authors:** Flint Xiaofeng Fan, Cheston Tan, Roger Wattenhofer, Yew-Soon Ong
- **Links:** [AAAI Workshop](https://trustagenticai.github.io/AAAI2026/paper.html)
- **Key Innovation:** Formal guarantees on error accumulation in the Model Context Protocol.

---

## 5. CTR Prediction & Recommendation Scaling

### 5.1 EST: Efficient Scaling Laws in CTR via Unified Modeling
- **Conference:** arXiv, Alibaba (Taobao & Tmall Group), 2026
- **Authors:** Mingyang Liu, Yong Bai, Zhangming Chan, et al.
- **Affiliation:** Alibaba
- **Links:** [arXiv:2602.10811](https://arxiv.org/abs/2602.10811)
- **Background:** Industrial CTR models traditionally use early aggregation of user behaviors to maintain efficiency, creating an information bottleneck that discards fine-grained token-level signals.
- **Key Innovations:**
  - **Fully Unified Modeling** — processes all raw inputs in a single sequence without lossy aggregation
  - **Lightweight Cross-Attention (LCA)** — prunes redundant self-interactions
  - **Content Sparse Attention (CSA)** — uses content similarity for dynamic behavior selection
- **Results:** Stable power-law scaling relationship. Deployed on Taobao display advertising: +3.27% RPM, +1.22% CTR lift.

### 5.2 LoopCTR: Unlocking Loop Scaling Power for CTR Prediction
- **Conference:** arXiv, Alibaba, 2026
- **Links:** [arXiv:2604.19550](https://arxiv.org/abs/2604.19550)
- **Key Innovation:** "Loop scaling" via recursive reuse of shared layers. Decouples training-time compute from parameter count. Train-multi-loop, infer-zero-loop strategy.

### 5.3 UniMixer: Unified Architecture for Scaling Laws in Recommendation
- **Conference:** arXiv, Kuaishou, 2026
- **Links:** [arXiv:2604.00590](https://arxiv.org/abs/2604.00590)
- **Key Innovation:** Unifies attention/TokenMixer/FM into a single scaling framework. Proposes UniMixing-Lite for improved scaling ROI.

### 5.4 RankUp: High-Rank Representations for Large-Scale Advertising
- **Conference:** arXiv, Tencent (Weixin), 2026
- **Links:** [arXiv:2604.17878](https://arxiv.org/abs/2604.17878)
- **Key Innovation:** Addresses representation collapse when scaling MetaFormer-based ranking models.

### 5.5 TokenFormer: Unify Multi-Field and Sequential Recommendation
- **Conference:** arXiv, Tencent, 2026
- **Links:** [arXiv:2604.13737](https://arxiv.org/abs/2604.13737)
- **Key Innovation:** Unified architecture bridging the two historically separate paradigms: feature interaction models (multi-field) and sequential models. Bottom-Full-Top-Sliding attention mechanism. Solves Sequential Collapse Propagation.

### 5.6 Tencent All-Modality Generative Recommendation Challenge 2025
- **Conference:** Tencent Advertising Algorithm Challenge 2025 (arXiv report 2026)
- **Authors:** Junwei Pan, Wei Xue, Chao Zhou, et al.
- **Affiliation:** Tencent
- **Links:** [arXiv:2604.04976](https://arxiv.org/abs/2604.04976)
- **Key Innovation:** Two all-modality datasets TencentGR-1M (1M users) and TencentGR-10M (10M users). Rich collaborative IDs + multi-modal representations. Weighted evaluation for high-value conversion events.

### 5.7 Beyond Dense Connectivity: Explicit Sparsity for Scalable Recommendation
- **Conference:** arXiv, Alibaba International, 2026
- **Links:** [arXiv:2604.08011](https://arxiv.org/abs/2604.08011)
- **Key Innovation:** Introduces explicit sparsity patterns in deep recommendation architectures to improve scaling efficiency.

### 5.8 BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization
- **Conference:** arXiv, Jun 2026
- **Links:** [arXiv:2606.00079](https://arxiv.org/abs/2606.00079)
- **Key Innovation:** Spectral energy-guided bit allocation for MoE model quantization. Code/models released.

### 5.9 Exploring Scaling Laws of CTR Model for Online Performance Improvement
- **Conference:** RecSys 2025
- **Links:** [arXiv:2508.15326](https://arxiv.org/abs/2508.15326)
- **Background:** Systematic study of how scaling laws apply to industrial CTR models, with online A/B test validation.

---

## 6. Generative Models & Diffusion

### 6.1 DiffusionGemma: 4x Faster Text Generation
- **Conference:** Google DeepMind, June 2026
- **Affiliation:** Google DeepMind
- **Links:** [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)
- **Key Innovation:** Applies diffusion models to text generation in the Gemma family, achieving 4× speedup over autoregressive decoding.

### 6.2 MMAudio: Audio-Visual Generation
- **Conference:** CVPR 2026 Tutorial / Sony AI
- **Affiliation:** Sony AI
- **Links:** [Sony AI @ CVPR 2026](https://ai.sony/blog/cvpr-2026-sony-ais-latest-in-computer-vision-research)
- **Key Innovation:** Joint audio-visual generation framework; part of Sony AI's CVPR 2026 tutorial on diffusion models.

### 6.3 BAgger: Backwards Aggregation for Autoregressive Video Diffusion
- **Conference:** CVPR 2026
- **Authors:** Ryan Po, Eric Ryan Chan, Changan Chen, Gordon Wetzstein
- **Affiliation:** Stanford University
- **Links:** [arXiv:2512.12080](https://arxiv.org/abs/2512.12080)
- **Key Innovation:** Backwards aggregation to mitigate exposure bias in autoregressive video diffusion models.

### 6.4 Dual Ascent Diffusion for Inverse Problems
- **Conference:** CVPR 2026
- **Authors:** Minseo Kim, Axel Levy, Gordon Wetzstein
- **Affiliation:** Stanford University
- **Links:** [arXiv:2505.17353](https://arxiv.org/abs/2505.17353)
- **Key Innovation:** Integrates diffusion priors with constrained optimization through a dual ascent formulation for image restoration.

---

## 7. Computer Vision (CVPR 2026)

### 7.1 CVPR 2026 Overview
- **Submissions:** 16,092 | **Accepted:** 4,090 (25.42% acceptance rate) | **Findings:** 1,717
- **Location:** Denver, Colorado, June 3-7, 2026
- **Top Areas:** 3D Reconstruction/Gaussian Splatting (45 oral), Generative Models/Diffusion (20 oral), VLM/MLLM/Multimodal Reasoning (12 oral), Robotics/Embodied AI (8 oral), Medical Imaging (15 oral), Segmentation/Detection (30 oral)

### 7.2 Notable CVPR 2026 Papers

#### MAMMA: Markerless Accurate Multi-person Motion Acquisition
- **Status:** Oral
- **Affiliation:** Max Planck Institute
- **Innovation:** Markerless motion capture pipeline recovering SMPL-X parameters from multi-view video. Synthetic multi-view dataset with diverse motions, extreme poses, hand motions, close interactions.

#### OmniVGGT: Omni-Modality Visual Geometry Grounded Transformer
- **Status:** Highlight
- **Innovation:** Multi-modal (text/image/video/3D) visual geometry transformer. Unified geometry understanding.

#### PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image
- **Innovation:** Generates physically simulatable 3D assets from a single image. Bridges single-view 3D reconstruction with physics simulation.

#### WorldLens: Full-Spectrum Evaluations of Driving World Models
- **Status:** Oral
- **Innovation:** Comprehensive benchmark for driving world models. Real-world evaluation across diverse conditions.

#### Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers (LLSA)
- **Status:** Highlight
- **Innovation:** Log-linear sparse attention pattern for diffusion transformers. Improves efficiency while maintaining generation quality.

### 7.3 CVPR 2026 Best Paper Awards
- Multiple awards in generative modeling, 3D scene understanding, and video-to-audio synthesis. Detailed winners announced at CVPR 2026 (June 5).

---

## 8. NLP & Evaluation (ACL 2026 / EMNLP 2025)

### 8.1 ACL 2026 Overview
- **Location:** (TBD, 2026)
- **Program Chairs:** Philipp Koehn (General), Maria Liakata, Viviane P. Moreira, Jiajun Zhang, David Jurgens
- **New Tracks:** Safety and Alignment in LLMs, Mathematical/Symbolic/Neurosymbolic Reasoning, Retrieval-Augmented Language Models, AI/LLM Agents

### 8.2 Notable ACL 2026 Topics (from accepted paper notes)

#### MCP-Bench: Benchmarking Tool-Using LLM Agents via MCP Servers
- **Innovation:** Standardized benchmark for evaluating LLM agents using the Model Context Protocol for tool use.

#### VideoMind: Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning
- **Innovation:** Four-role collaboration (Planner-Grounder-Verifier-Answerer) via LoRA adapter switching on unified base model. 2B model surpasses GPT-4o and Gemini-1.5-Pro.

### 8.3 EMNLP 2025 Overview
- **Location:** Suzhou, China, November 4-9, 2025
- **Submissions:** 8,174 | **Accepted:** 1,811 (22.2% acceptance rate)
- **Main conference papers:** ~1,811 accepted; Findings: ~1,405 papers

### 8.4 Notable EMNLP 2025 Papers

#### Preference Learning with Response Time
- **Authors:** Ayush Sawarni, Sahasrajit Sarmasarkar, Vasilis Syrgkanis
- **Affiliation:** Stanford
- **Innovation:** Incorporates response time into preference learning for RLHF, using orthogonal statistical methods.

#### Agentic NL2SQL — Datalake Agent
- **Innovation:** Interactive reasoning loop with hierarchical information retrieval (GetDBDescription → GetTables → GetColumns → DBQueryFinalSQL). Enables on-demand schema access.

#### Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding
- **Authors:** Melanie Subbiah, et al.
- **Innovation:** Proposes Ambiguity Rewrite Metric (ARM) for nuanced evaluation of claim faithfulness, moving beyond binary judgments.

---

## 9. Information Retrieval & Web

### 9.1 WWW 2026 Overview
- **Location:** (The Web Conference 2026)
- **Accepted Papers:** Research Tracks covering Economics/Online Markets, Social Media, Search, Recommendation, Privacy, and Web4Good special track.

#### Notable WWW 2026 Papers:
- **Auto-bidding under Return-on-Spend Constraints with Uncertainty Quantification** — Jiale Han, et al.
- **DARA: Few-shot Budget Allocation in Online Advertising via RL-Finetuned LLMs** — Mingxuan Song, et al. (RL-finetuned LLM for ad budget allocation)
- **LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting** — Yewen Li, et al.
- **AHBid: Adaptable Hierarchical Bidding Framework for Cross-Channel Advertising** — Xinxin Yang, et al.
- **Strategic Content Creation with GenAI: To Share or Not to Share?** — Gur Keinan, Omer Ben-Porat
- **Robust LLM-Based Website Fingerprinting** — Xiyuan Zhao, et al. (Tsinghua)

### 9.2 SIGIR 2026 Overview
- **Location:** Melbourne, Australia, July 20-24, 2026
- **Submissions:** 1,271 | **Accepted:** 234 (18.41% acceptance rate)
- **New in 2026:** Switched to OpenReview; extra camera-ready page; responsible reviewing policy.

#### Research Areas: Search & Ranking, Recommender Systems, ML for IR (incl. Generative IR, Deep Learning for IR, RL for IR), Fairness/Accountability/Transparency.

### 9.3 CIKM 2025 Overview
- **Location:** Seoul, Korea, November 10-14, 2025
- **Submissions:** 2,761 (+11%) | **Accepted:** 810 (29% acceptance rate)
- **Tutorial highlight:** "Towards Large Generative Recommendation: A Tokenization Perspective" by Hou et al. (UCSD, USTC, NUS) — comprehensive survey of action tokenization (item IDs, textual descriptions, semantic IDs) for generative recommendation.

#### Notable CIKM 2025 Papers:
- **LangPTune: Optimizing Language-based User Profiles for Recommendation** — Zhaolin Gao, et al. (Cornell)
- **AGENTiGraph: Multi-Agent KG Interaction Framework** — Fan Gao, et al. (U. Tokyo) — 95.12% accuracy on KG interactions
- **Continual Recommender Systems** (Tutorial) — Hyunsik Yoo, et al. (UIUC, Korea U.)

---

## 10. Recommender Systems (RecSys 2025)

### 10.1 RecSys 2025 Overview
- **Location:** Prague, Czech Republic, September 22-26, 2025
- **Full papers:** ~35 accepted

### 10.2 Notable RecSys 2025 Papers

#### Beyond Immediate Click: Engagement-Aware MoE Transformers (Prime Video/Amazon)
- **Key Innovation:** Temporal Mixture-of-Experts on Transformer backbone; Personalized Hard-Negative Sampling (PHNS); engagement-aware multi-task learning (CTR + ranking + completion-rate); next-K training with soft labels. On Prime Video data (~1M users): +3.5% NDCG@1.

#### Explicit Negatives at Scale (TikTok/ByteDance)
- **Key Innovation:** Captures lightweight, context-aware micro-signals (in-feed prompts); denoises accidental taps and cold-start artefacts; propagates through training (contrastive shaping) and serving (down-ranking). Buckets negatives by reason ("not relevant", "seen too often").

#### Peak-End Retention (Meta Reels)
- **Key Innovation:** Psychology-informed long-term optimization using peak-end rule from behavioral economics. Optimizes for retention-defining moments, not just immediate engagement.

#### You Say Search, I Say Recs: Scalable Agentic Query Understanding (Spotify)
- **Key Innovation:** Agentic approach bridging search and recommendation; LLM-powered query understanding for exploratory search at Spotify scale.

#### Lasso: LLM-based User Simulator for Cross-Domain Recommendation
- **Key Innovation:** Uses LLM simulation to build RL environment for recommendation training. Could be a game-changer for rec training paradigms.

#### Exploring Scaling Laws of CTR Model (Meta)
- **Key Innovation:** Systematic study of CTR scaling laws with online validation.

#### Balancing Fine-tuning and RAG: Hybrid Strategy for Dynamic LLM Recommendation Updates
- **Key Innovation:** Hybrid strategy combining fine-tuning efficiency with RAG flexibility for keeping LLM-based recommenders up to date.

### 10.3 RecSys Challenge 2026
- **Theme:** Music Conversational Recommendation (Music-CRS)
- **Dataset:** TalkPlayData-Challenge — LLM-generated multi-turn dialogues + music metadata
- **Task:** Conversational Music Recommendation with ranked retrieval + response generation

---

## 11. Frontier Model Releases (May–June 2026)

| Model | Company | Date | Key Specs |
|-------|---------|------|-----------|
| **Claude Opus 4.8** | Anthropic | May 28, 2026 | SWE-Bench Pro 69.2%, OSWorld 83.4%, Dynamic Workflows (parallel subagents) |
| **Gemini 3.5** | Google DeepMind | May 2026 | Frontier intelligence with action; improved reasoning + tool use |
| **Gemini Omni** | Google DeepMind | May 2026 | Create anything from anything, starting with video |
| **Gemma 4 12B** | Google DeepMind | June 2026 | Unified, encoder-free multimodal model, 12B params |
| **DiffusionGemma** | Google DeepMind | June 2026 | 4× faster text generation via diffusion |
| **Nemotron 3 Ultra** | NVIDIA | June 1, 2026 | 550B-A55B MoE, most capable US open model |
| **Kimi K2.7 Code** | Moonshot AI | June 12, 2026 | Latest Chinese open-source frontier, code-specialized |
| **GPT-5.6** | OpenAI | Expected June 2026 | Prediction markets: 80-89% probability |

---

## 12. Key Trends Summary

### Architecture
- **Hybrid SSM-Attention** is the dominant 2026 architecture trend: Mamba-2/3 + Attention layers in Nemotron 3, Qwen3.6 (Gated DeltaNet), etc.
- **Variable-Width** and **Explicit Sparsity** challenge fixed uniform-depth architectures.
- **ParaRNN** resurrects nonlinear RNNs for LLM-scale training through parallelization.

### Reasoning
- **Process Supervision + RL (RLVR)** is the primary paradigm for improving reasoning, but may not elicit *novel* patterns (key negative result at NeurIPS 2025).
- **Test-time compute scaling** is a first-class design axis, driving efficient architecture adoption.
- **Overthinking** is newly recognized as a fundamental unsolved problem.

### Recommendation & Advertising
- **CTR Scaling Laws** are now an established research area: Alibaba (EST, LoopCTR), ByteDance (RankMixer, OneTrans), Kuaishou (UniMixer), Tencent (TokenFormer, RankUp), Meta (scaling laws paper).
- **All-Modality Generative Recommendation** with semantic IDs, text tokenization, and multi-modal embeddings is the emerging paradigm (TencentGR, CIKM 2025 tutorial).
- **Explicit Negatives** and **Engagement-Aware** objectives move beyond naive CTR optimization.

### Agents
- **MCP (Model Context Protocol)** is gaining traction as a standard interface for tool-using agents.
- **Agent Memory** (A-MEM, ACE) is recognized as a critical gap — context engineering and structured memory are active frontiers.
- **Misevolution** risk (self-evolving agents diverging from alignment) is a newly identified safety concern.

### Evaluation & Benchmarks
- **DeepSynth**, **ASSEBench**, **ZeroDayBench**, **MCP-Bench** — new benchmarks exposing agent limitations.
- **Long-horizon task evaluation** reveals that short benchmarks give misleading "diminishing returns" signals.

### Industry Model Releases (H1 2026)
- **Claude Opus 4.8** leads coding/agentic benchmarks
- **NVIDIA Nemotron 3 Ultra** is the strongest US open model
- **Chinese labs** (Moonshot/Kimi, Alibaba/Qwen, DeepSeek, ByteDance) continue to push open-source frontier
- **Google DeepMind** shipped Gemini 3.5, Gemini Omni, DiffusionGemma, and Gemma 4 in a single quarter

---

*Generated 2026-06-19. Sources include conference websites, OpenReview, arXiv, PaperNotes, Paper Copilot, Sebastian Raschka's LLM Research Papers list, and other public repositories.*
