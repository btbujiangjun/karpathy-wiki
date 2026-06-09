---
title: 顶会论文专题报告 — 2026年6月全面版
type: synthesis
created: 2026-06-09
updated: 2026-06-09
sources: 
  - NeurIPS 2025 Best Papers
  - ICLR 2026 Outstanding Papers
  - ICML 2026 accepted papers
  - AAAI 2026 proceedings
  - CVPR 2026 accepted papers
  - EMNLP 2025 awards
  - KDD 2026 papers
  - RecSys 2025 proceedings
  - SIGIR 2026 accepted papers
  - WWW 2026 papers
  - CIKM 2025 papers
  - ACL 2026 papers
tags: [conference-digest, neurips-2025, iclr-2026, icml-2026, aaai-2026, cvpr-2026, emnlp-2025, kdd-2026, recsys-2025, sigir-2026, www-2026, cikm-2025, acl-2026]
---

# 顶会论文专题报告 — 2026年6月全面版

> Comprehensive digest of award-winning and notable papers from top ML/AI conferences. Covers NeurIPS 2025, ICLR 2026, ICML 2026, AAAI 2026, CVPR 2026, EMNLP 2025, KDD 2026, RecSys 2025, SIGIR 2026, WWW 2026, CIKM 2025, ACL 2026.
> Generated: 2026-06-09

---

## Table of Contents

1. [NeurIPS 2025 — Best Papers & Runners-Up](#1-neurips-2025--best-papers--runners-up)
2. [ICLR 2026 — Outstanding Papers & Notable Acceptances](#2-iclr-2026--outstanding-papers--notable-acceptances)
3. [ICML 2026 — Outstanding Papers & Accepted Highlights](#3-icml-2026--outstanding-papers--accepted-highlights)
4. [AAAI 2026 — Notable Papers](#4-aaai-2026--notable-papers)
5. [CVPR 2026 — Best Papers & Notable Acceptances](#5-cvpr-2026--best-papers--notable-acceptances)
6. [EMNLP 2025 — Best Paper & Outstanding Papers](#6-emnlp-2025--best-paper--outstanding-papers)
7. [KDD 2026 — Notable Papers (CTR, Ads, RecSys)](#7-kdd-2026--notable-papers-ctr-ads-recsys)
8. [RecSys 2025 — Notable Papers](#8-recsys-2025--notable-papers)
9. [SIGIR 2026 — Notable Papers](#9-sigir-2026--notable-papers)
10. [WWW 2026 — Notable Papers](#10-www-2026--notable-papers)
11. [CIKM 2025 — Notable Papers](#11-cikm-2025--notable-papers)
12. [ACL 2026 — Notable Papers](#12-acl-2026--notable-papers)
13. [Industry Lab Highlights (arXiv 2026)](#13-industry-lab-highlights-arxiv-2026)

---

## 1. NeurIPS 2025 — Best Papers & Runners-Up

NeurIPS 2025 received **21,575 submissions**, accepting **5,290 papers** (~24.5% acceptance rate). Held as a dual-city conference in San Diego and Mexico City, Dec 2025.

### 1.1 Best Papers (4)

#### Paper 1: Gated Attention for Large Language Models
- **Title**: Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **English**: Gated Attention for LLMs: Non-linearity, Sparsity, and Attention-Sink-Free
- **Chinese**: 门控注意力机制：非线性、稀疏性与无注意力汇聚点
- **Authors**: Qiu et al. (Alibaba Qwen Team)
- **Affiliation**: Alibaba (Tongyi Qianwen)
- **Venue**: NeurIPS 2025 **Best Paper**
- **arXiv**: [2505.06708](https://arxiv.org/abs/2505.06708)
- **Abstract**: Proposes adding a learnable, head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA). The gate acts as an "intelligent noise-canceling headphone" — blocking irrelevant information before it reaches the FFN layer, improving both computational efficiency and robustness.
- **Key Innovations**:
  - Eliminates the attention-sink artifact (heads can now output zero)
  - Stabilizes training, tolerates higher learning rates
  - Improves scaling properties
- **Experimental Results**: 
  - 1.7B dense model and 15B MoE model trained on 3.5T tokens
  - Only 1% parameter increase, 0.2 perplexity decrease, +2 points MMLU
  - Consistent improvements across all subdomains of the Pile
- **Impact**: Integrated into Qwen3-Next. Code and models open-sourced on GitHub/HuggingFace.

#### Paper 2: Artificial Hivemind
- **Title**: Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Chinese**: 人工蜂群思维：语言模型的无尽同质化
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: University of Washington, CMU, Allen Institute for AI, Lila Sciences, Stanford University
- **Venue**: NeurIPS 2025 **Best Paper**
- **OpenReview**: [saDOrrnNTz](https://openreview.net/forum?id=saDOrrnNTz)
- **Abstract**: Documents both intra-model repetition and pronounced inter-model homogeneity across 70+ models. Releases Infinity-Chat dataset (26K real open-ended queries, 31K human annotations across ratings + pairwise preferences, 25 annotators per example) and a 6-category / 17-subcategory taxonomy.
- **Key Finding**: Even when using different temperature settings or different models (ChatGPT, Claude, Gemini), outputs converge to eerily similar responses. Models exhibit a systematic homogenization effect.

#### Paper 3: 1000 Layer Networks for Self-Supervised RL
- **Title**: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- **Chinese**: 1000层自监督强化学习网络
- **Authors**: K. Wang et al.
- **Venue**: NeurIPS 2025 **Best Paper**
- **arXiv**: [2503.14858](https://arxiv.org/abs/2503.14858)
- **Abstract**: Most RL networks are 2-5 layers. Pushing contrastive RL to 1024 layers (with the right SSL classification objective rather than TD-regression) gives 2×–50× gains on locomotion and manipulation, in a goal-conditioned setting with no demonstrations or rewards.
- **Key Innovation**: Identifies that the right objective (SSL classification) is what enables depth scaling in RL, not TD-regression which saturates at shallow depths.

#### Paper 4: Why Diffusion Models Don't Memorize
- **Title**: Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training
- **Chinese**: 扩散模型为何不记忆：隐式动力学正则化的作用
- **Authors**: Bonnaire, Urfin, Biroli, Mézard
- **Venue**: NeurIPS 2025 **Best Paper**
- **arXiv**: [2505.17638](https://arxiv.org/abs/2505.17638)
- **Abstract**: Identifies two distinct training timescales: τ_gen (when good samples appear) and τ_mem (when memorization sets in). τ_mem grows linearly with dataset size n while τ_gen stays constant, yielding a widening generalization window. Reframes early stopping as a structural necessity, not a heuristic.

### 1.2 Runners-Up

#### Paper 5: Optimal Mistake Bounds for Transductive Online Learning
- **Authors**: Z. Chase, Hanneke, Moran, Shafer
- **arXiv**: [2512.12567](https://arxiv.org/abs/2512.12567)
- **Summary**: Closes a 30-year-old open problem: the optimal transductive mistake bound is Θ(√d), exponentially tighter than prior bounds.

#### Paper 6: Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **Authors**: Y. Yue et al. (Tsinghua LeapLab)
- **arXiv**: [2504.13837](https://arxiv.org/abs/2504.13837)
- **Summary**: RLVR-trained LLMs beat their base models at small k in pass@k, but the *base* models win at large k. The reasoning paths RLVR produces are already in the base model's sampling distribution — the trained capability boundary actually *narrows*. Distillation genuinely expands it.

#### Paper 7: Superposition Yields Robust Neural Scaling
- **Authors**: Y. Liu, Z. Liu, Gore
- **arXiv**: [2505.10465](https://arxiv.org/abs/2505.10465)
- **Summary**: First-principles derivation of neural scaling laws from representation superposition. In the strong-superposition regime (more features than dimensions), loss scales as L ∝ 1/m with model width. Validated on OPT, Pythia, Qwen.

### 1.3 Test of Time Award
- **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks** — Ren, He, Girshick, Sun (2015). Cited 56,700+ times.

### 1.4 Other Notable NeurIPS 2025 Papers

#### Large Language Diffusion Models (LLaDA) — NeurIPS 2025 Oral
- **Authors**: Shen Nie, Fengqi Zhu, Zebin You, Xiaolu Zhang, Jingyang Ou, Jun Hu, Jun Zhou, Yankai Lin, Ji-Rong Wen, Chongxuan Li
- **Affiliation**: Renmin University of China / GSAI
- **arXiv**: Available on OpenReview
- **Summary**: First diffusion language model (masked diffusion) trained from scratch at 8B scale. Competitive with LLaMA3 8B on in-context learning and instruction following, and addresses the reversal curse (surpassing GPT-4o on reversal poem completion).

---

## 2. ICLR 2026 — Outstanding Papers & Notable Acceptances

ICLR 2026 (Singapore, Apr 2026) received **19,525 submissions**, **5,355 accepted** (27.4% acceptance rate), **223 oral papers**.

### 2.1 Outstanding Papers

#### Paper 1: Transformers are Inherently Succinct
- **Title**: Transformers are Inherently Succinct
- **Chinese**: Transformer 天然具备简洁性
- **Authors**: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation**: ETH Zurich
- **Venue**: ICLR 2026 **Outstanding Paper**
- **arXiv**: [2510.19315](https://arxiv.org/abs/2510.19315)
- **Abstract**: Proves Transformers are *doubly exponentially* more succinct than finite automata, and exponentially more succinct than RNNs and LTL, when representing formal languages. As a corollary, verifying properties of Transformers is EXPSPACE-complete — formally intractable.
- **Impact**: Provides theoretical justification for why Transformers dominate — they can represent certain functions with exponentially fewer parameters than alternative architectures.

#### Paper 2: LLMs Get Lost in Multi-Turn Conversation
- **Title**: LLMs Get Lost in Multi-Turn Conversation
- **Chinese**: 大语言模型在多轮对话中迷失
- **Authors**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Affiliation**: Salesforce Research
- **Venue**: ICLR 2026 **Outstanding Paper**
- **OpenReview**: [VKGTGGcwl6](https://openreview.net/forum?id=VKGTGGcwl6)
- **Abstract**: Across 200,000+ simulated conversations on six generation tasks, every top open- and closed-weight LLM tested shows an average **39% drop** going from single-turn to multi-turn underspecified instructions. Decomposes the drop into a small aptitude loss and a large *unreliability* increase.

#### Honorable Mention: The Polar Express
- **Title**: The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm
- **Authors**: Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **Summary**: Optimal polynomial approximations for polar decomposition used in the Muon optimizer, designed for GPU low-precision settings.

### 2.2 Notable Oral Papers — Mamba-3

#### Mamba-3: Improved Sequence Modeling using State Space Principles — ICLR 2026 Oral
- **Title**: Mamba-3: Improved Sequence Modeling using State Space Principles
- **Chinese**: Mamba-3：基于状态空间原理改进的序列建模
- **Authors**: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- **Affiliation**: CMU, Princeton, Cartesia AI, Together AI
- **Venue**: ICLR 2026 **Oral**
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **Abstract**: Three core methodological improvements from an SSM perspective: (1) exponential-trapezoidal discretization for more expressive recurrence, (2) complex-valued state update for richer state tracking (solves parity tasks Mamba-2 cannot), (3) multi-input multi-output (MIMO) formulation improving performance without increasing decode latency.
- **Experimental Results**:
  - At 1.5B scale: +2.2 over Transformer, +1.9 over Mamba-2, +1.8 over Gated DeltaNet
  - MIMO variant: additional +1.2 points
  - Mamba-3 (state size 64) matches Mamba-2 (state size 128) perplexity — half the state size
  - 100% accuracy on parity tasks vs Mamba-2's near-random

### 2.3 Other Notable ICLR 2026 Acceptances

#### A State-Transition Framework for Efficient LLM Reasoning — ICLR 2026
- **Authors**: Liang Zhang et al.
- **arXiv**: [2602.01198](https://arxiv.org/abs/2602.01198)
- **Summary**: Models LLM reasoning as a state-transition process using linear attention. Reduces attention complexity from quadratic to linear. Mitigates over-thinking via state-based reasoning strategy.

#### MEM1: Memory-Reasoning Synergy for Long-Horizon Agents — ICLR 2026
- **Won**: Best Paper at NeurIPS 2025 Workshop on Multi-Turn Interactions
- **Authors**: Zhou Zijian et al. (NUS / MIT / SMART)
- **Summary**: RL approach training agents to maintain compact, dynamic internal state instead of storing all past interactions. Significantly lower memory usage and faster performance.

#### AgentFlow: In-The-Flow Agentic System Optimization — ICLR 2026
- **Authors**: Lambda Labs + collaborators
- **Summary**: A 7B AgentFlow model beats GPT-4o on search, math, and science reasoning using Flow-GRPO (group refined policy optimization) for training modular agents.

---

## 3. ICML 2026 — Outstanding Papers & Accepted Highlights

ICML 2026 (Seoul, Jul 2026) received ~12,000 submissions, ~3,200 accepted.

### 3.1 Outstanding Papers from ICML 2025 (Most Recent Awarded)

#### CollabLLM: From Passive Responders to Active Collaborators — ICML 2025 Outstanding
- **Authors**: S. Wu, Galley, Peng, Cheng, G. Li, Dou, Cai, Zou, Leskovec, Gao
- **arXiv**: [2502.00640](https://arxiv.org/abs/2502.00640)
- **Summary**: Trains LLMs against multiturn-aware rewards estimated by collaborative simulation. +18.5% task performance, +46.3% interactivity, +17.6% user satisfaction (201-judge study).

#### Train for the Worst, Plan for the Best: Token Ordering in Masked Diffusions — ICML 2025 Outstanding
- **Authors**: J. Kim, Shah, Kontonis, Kakade, S. Chen
- **arXiv**: [2502.06768](https://arxiv.org/abs/2502.06768)
- **Summary**: Shows masked diffusion models can pick next token to decode at inference. "Decode where most confident" heuristic alone takes Sudoku from 7% → ~90%.

#### Roll the Dice: Beyond Creative Limits of Next-Token Prediction — ICML 2025 Outstanding
- **Authors**: Nagarajan, C. H. Wu, Ding, Raghunathan
- **arXiv**: [2504.15266](https://arxiv.org/abs/2504.15266)
- **Summary**: Constructs minimal algorithmic creativity tasks; shows next-token learning is myopic, teacherless and diffusion approaches are more creative.

### 3.2 Notable ICML 2026 Acceptances

#### Shannon Scaling Law — ICML 2026
- **Authors**: —
- **Affiliation**: —
- **arXiv**: [2605.23901](https://arxiv.org/abs/2605.23901)
- **Summary**: Models LLMs as noisy channels, deriving scaling laws from information-theoretic principles.

#### Self-Supervised Flow Matching (Self-Flow) — ICML 2026
- **Summary**: Self-supervised approach to flow matching for generative modeling, eliminating need for paired data.

#### UniAR: Unified Multimodal Autoregressive Modeling — ICML 2026
- **Affiliation**: Alibaba
- **Summary**: Unifies image, video, and text generation under a single autoregressive framework.

#### Provable Benefit of Curriculum in Transformer Tree-Reasoning Post-Training — ICML 2026
- **Authors**: Dake Bu et al.
- **Affiliation**: A*STAR CFAR
- **arXiv**: [2511.07372](https://arxiv.org/abs/2511.07372)
- **Summary**: Shows RL finetuning with curriculum strategies achieves polynomial sample complexity, while non-curriculum encounters exponential bottleneck.

#### Complete-muE: MoE Hyperparameter Transfer — ICML 2026
- **arXiv**: [2605.23893](https://arxiv.org/abs/2605.23893)
- **Summary**: Complete framework for transferring hyperparameters across MoE model scales.

#### DiLaDiff: Distilled Latent-Augmented Diffusion LM — ICML 2026
- **Affiliation**: NVIDIA
- **arXiv**: [2605.23605](https://arxiv.org/abs/2605.23605)
- **Summary**: Distilled diffusion language model with latent augmentation for efficient text generation.

---

## 4. AAAI 2026 — Notable Papers

AAAI 2026 (Singapore, Jan 2026) received **~29,000 submissions** (~23,000 after filtering), the largest in AAAI history.

### Notable Acceptances

#### ProbLog4Fairness: Neurosymbolic Bias Mitigation — AAAI 2026
- **Summary**: Formalizes bias assumptions as ProbLog programs; uses neurosymbolic extensions for bias mitigation in tabular and image data.

#### RefiDiff: Progressive Refinement Diffusion for Missing Data Imputation — AAAI 2026
- **Summary**: Combines Mamba-based denoising with local ML predictions for MNAR imputation. Outperforms SOTA on 9 real-world datasets.

#### Stabilizing Policy Gradient Methods via Reward Profiling — AAAI 2026
- **Summary**: Profiles rewards over trajectories to stabilize policy gradient training.

#### Beyond Content: Speech Toxicity Dataset with Paralinguistic Cues — AAAI 2026
- **Summary**: ToxiAlert-Bench with 30K+ audio clips annotated for 7 toxic categories, distinguishing textual vs paralinguistic toxicity sources.

---

## 5. CVPR 2026 — Best Papers & Notable Acceptances

CVPR 2026 (Denver, Jun 2026) — Apple presenting multiple papers including streaming vision-language models.

### 5.1 CVPR 2025 Best Papers (Most Recent Awarded)

#### VGGT: Visual Geometry Grounded Transformer — CVPR 2025 Best Paper
- **Authors**: Wang, M. Chen, Karaev, Vedaldi, Rupprecht, Novotny
- **Affiliation**: Oxford VGG / Meta AI
- **arXiv**: [2503.11651](https://arxiv.org/abs/2503.11651)
- **Summary**: Single feed-forward Transformer that jointly predicts camera parameters, depth maps, point maps, and 3D point tracks in one second from 1-100 input views. Beats optimization-based pipelines on most 3D benchmarks.

#### Neural Inverse Rendering from Propagating Light — CVPR 2025 Best Student Paper
- **Authors**: Malik, Attal, Xie, O'Toole, Lindell
- **Affiliation**: Toronto / Vector / CMU
- **arXiv**: [2506.05347](https://arxiv.org/abs/2506.05347)
- **Summary**: First physically-based neural inverse rendering from multi-view time-resolved measurements.

### 5.2 Notable CVPR 2026 Acceptances

#### Apple CVPR 2026 Papers
- **VSAS-Bench**: Real-Time Evaluation of Visual Streaming Assistant Models — streaming vision-language models evaluation benchmark
- Multiple papers on computer vision, streaming VLMs, and on-device AI

#### ARCache: Caching Acceleration for Video Diffusion — CVPR 2026
- **Summary**: Caching-based acceleration for video diffusion model inference.

---

## 6. EMNLP 2025 — Best Paper & Outstanding Papers

EMNLP 2025 (Suzhou, China, Nov 2025) received **8,174 submissions**, **1,811 accepted** to main (22.16%), **1,417 to Findings** (17.34%).

### Best Paper

#### Infini-gram mini: Exact n-gram Search at Internet Scale with FM-Index — EMNLP 2025 Best Paper
- **Authors**: H. Xu, J. Liu, Choi, N. A. Smith, Hajishirzi
- **Affiliation**: UW / AI2
- **arXiv**: [2506.12229](https://arxiv.org/abs/2506.12229)
- **Summary**: FM-index–based system that makes 83 TB of text (Common Crawl Jan–Jul 2025, DCLM-baseline, Pile) exactly searchable by n-gram, with index size only 44% of corpus. Practical for contamination audits, membership inference, and grounding.

### Outstanding Papers

#### PAFT: Prompt-Agnostic Fine-Tuning — EMNLP 2025 Outstanding
- **Authors**: Wei, Y. Shu, Ou, Y. He, F. R. Yu
- **arXiv**: [2502.12859](https://arxiv.org/abs/2502.12859)
- **Summary**: Continually samples diverse synthetic prompts during SFT/RLFT. +7% generalization to unseen prompts, 3.2× faster inference.

#### Constructions are Revealed in Word Distributions — EMNLP 2025 Outstanding
- **Authors**: Rozner, Weissweiler, Mahowald, Shain
- **Summary**: Uses RoBERTa to show constructions (construction-grammar sense) are visible as patterns of statistical affinity.

#### To Mask or to Mirror: Human-AI Alignment in Collective Reasoning — EMNLP 2025 Outstanding
- **Authors**: C. Qian, Parisi, Bouleau, Tsai, Lebreton, Dixon
- **Affiliation**: Google
- **Summary**: 748-participant experiment matching LLM groups (Gemini 2.5, GPT-4.1, Claude Haiku 3.5, Gemma 3). Some models mirror human biases; others mask and over-correct.

### Other Notable EMNLP 2025 Papers

#### Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?
- **Summary**: When LLMs are asked about their values, self-declared answers don't align with their actions. Builds benchmark quantifying the "value-action gap."

#### Conflict-Aware Soft Prompting for RAG
- **Authors**: Eunseong Choi et al.
- **Summary**: Addresses conflicts between retrieved documents and model knowledge in RAG.

---

## 7. KDD 2026 — Notable Papers (CTR, Ads, RecSys)

KDD 2026 includes Cycle 1 (Aug deadline) and Cycle 2 (Feb deadline) research tracks.

### Notable Acceptances

#### FAT: Rademacher CTR Scaling Law — KDD 2026
- **Affiliation**: Alibaba
- **arXiv**: [2511.12081](https://arxiv.org/abs/2511.12081)
- **Summary**: Proposes Rademacher complexity-based scaling law for CTR models. Provides theoretical guarantees for model scaling behavior.

#### RankUp: High-rank Representations for Ad Ranking — KDD 2026
- **Affiliation**: Tencent (WeChat)
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Summary**: Novel approach to learning high-rank representations for advertising ranking in WeChat ecosystem.

#### MGOE: Multi-Grained Optimization for CTR — KDD 2026
- **Affiliation**: Alibaba
- **Summary**: Multi-grained optimization framework for CTR prediction with improved fine-grained modeling.

#### GPSD: Generative Pretraining for Discriminative CTR — KDD 2025
- **Affiliation**: Alibaba
- **arXiv**: [2506.03699](https://arxiv.org/abs/2506.03699)
- **Summary**: Uses generative pretraining to improve discriminative CTR model performance.

---

## 8. RecSys 2025 — Notable Papers

RecSys 2025 (Prague, Czech Republic, Sep 2025).

### Notable Papers

#### Exploring Scaling Laws of CTR Model for Online Performance Improvement — RecSys 2025
- **Affiliation**: Meituan
- **arXiv**: [2508.15326](https://arxiv.org/abs/2508.15326)
- **Summary**: SUAN — Systematic study of CTR model scaling at Meituan. Links offline scaling to online performance.

#### LONGER: Ultra-Long User Behavior Sequences — RecSys 2025
- **Affiliation**: ByteDance
- **arXiv**: [2505.04421](https://arxiv.org/abs/2505.04421)
- **Summary**: Efficient modeling of ultra-long user behavior sequences for recommendation.

#### LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding — RecSys 2025
- **Summary**: Novel embedding framework for large-scale recommendation models balancing efficiency and flexibility.

#### You Say Search, I Say Recs: Agentic Query Understanding at Spotify — RecSys 2025
- **Affiliation**: Spotify
- **Summary**: Scalable agentic approach to query understanding and exploratory search.

#### Zero-shot Cross-domain Knowledge Distillation: YouTube Music — RecSys 2025
- **Affiliation**: YouTube/Google
- **Summary**: Cross-domain knowledge distillation for music recommendation without target domain labels.

---

## 9. SIGIR 2026 — Notable Papers

SIGIR 2026 (Melbourne, Australia, Jul 2026).

### Notable Acceptances

#### GenRec: Generative Retrieval Paradigm — SIGIR 2026
- **Summary**: End-to-end generative retrieval replacing cascaded retrieval + ranking pipeline.

#### OneRanker: Unified Ranking Framework — SIGIR 2026
- **Affiliation**: Tencent
- **Summary**: Unified ranking framework for multiple recommendation scenarios.

#### ACE: Adaptive Contrastive Estimation for Retrieval — SIGIR 2026
- **Summary**: Novel contrastive learning approach for information retrieval.

#### GBLA: Linear Attention for Generative Retrieval — SIGIR 2026
- **Affiliation**: Yandex
- **Summary**: Linear attention mechanism enabling efficient generative retrieval at scale.

#### FEDIN: Frequency-Domain CTR — SIGIR 2026
- **Summary**: Frequency-domain feature interaction learning for CTR prediction.

---

## 10. WWW 2026 — Notable Papers

### Notable Acceptances

#### ThinkRec: Thinking-based LLM Recommendation — WWW 2026
- **Summary**: Leverages LLM reasoning (chain-of-thought) for recommendation, interpreting user intent through explicit reasoning steps before generating recommendations.

#### GenCI: Generative CTR via Cohort Intent Learning — WWW 2026
- **Affiliation**: —
- **arXiv**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Summary**: Generative CTR paradigm using cohort-level intent learning.

#### SparseCTR: Sparse Attention Long-Term CTR — WWW 2026
- **Affiliation**: Meituan
- **arXiv**: [2601.17836](https://arxiv.org/abs/2601.17836)
- **Summary**: Sparse attention mechanism enabling efficient long-term user behavior modeling for CTR.

#### OneTrans: Unified Feature Interaction and Sequence Modeling — WWW 2025
- **Affiliation**: ByteDance
- **arXiv**: [2510.26104](https://arxiv.org/abs/2510.26104)
- **Summary**: Unifies sequence (behavior) and non-sequence (profile/context) features into single token sequence via pyramid Transformer blocks. Online A/B: single-user GMV +5.68%.

---

## 11. CIKM 2025 — Notable Papers

### Notable Acceptances

#### RankMixer: Scaling Up Ranking Models in Industrial Recommenders — CIKM 2025
- **Affiliation**: ByteDance
- **arXiv**: [2507.15551](https://arxiv.org/abs/2507.15551)
- **Summary**: Hardware-aware token mixing design. Replaces attention with per-token parameterized FFN + HeadMixing. Foundational work of ByteDance token-based recommendation series.

#### MuChator: Multi-turn Conversation Understanding
- **Affiliation**: JD.com
- **Summary**: Multi-turn dialogue understanding for e-commerce conversational recommendation.

---

## 12. ACL 2026 — Notable Papers

### Notable Acceptances (Prior Year)

#### CodeTree: Agent-guided Tree Search Code Generation — ACL 2025
- **Affiliation**: Salesforce
- **Summary**: Agent-guided tree search for code generation, improving accuracy through structured exploration.

#### Tree-of-Evolution: Tree-Structured Code Instruction Evolution — ACL 2025
- **Affiliation**: NUS
- **Summary**: Evolves code instructions through tree-structured generation for improved code LLM training.

---

## 13. Industry Lab Highlights (arXiv 2026)

### ByteDance

#### Lance: Unified Multimodal Modeling (May 2026)
- **arXiv**: [2605.18678](https://arxiv.org/abs/2605.18678)
- **Summary**: A 3B-active-parameter native unified multimodal model supporting image/video understanding, generation, and editing. Trained from scratch with dual-stream MoE architecture. Matches/fixes SOTA on DPG-Bench (84.67), VBench (85.11), GEdit-Bench (7.30). Outperforms HunyuanVideo (83.43) on video generation. Open-sourced Apache 2.0.

#### TokenMixer-Large (arXiv 2026)
- **Summary**: Scaled RankMixer to 7B online / 15B offline params. Fixes residual misalignment, adds Sparse Per-token MoE. Ads MFU 60%. E-commerce GMV +2.98%, advertising ADSS +2.0%.

#### HyFormer (arXiv 2026)
- **Summary**: Revisits OneTrans [SEP] token design. Proposes query-decoding (global token cross-attends to each sequence) + query-augmentation. Outperforms OneTrans.

#### Precise: SDE-Consistent Sampling for Flow-Matching RL (arXiv 2026)
- **arXiv**: [2605.23522](https://arxiv.org/abs/2605.23522)
- **Summary**: SDE-consistent sampling for flow-matching reinforcement learning.

### Google DeepMind

- **Gemini 3.5**: Latest family of models combining frontier intelligence with action.
- **Lyria 3**: Music composition with vocals.
- **Nano Banana 2**: Pro-level image generation and editing at Flash-level speed.

### Meta AI

- **VGGT** (CVPR 2025 Best Paper): Feed-forward Transformer for 3D reconstruction.
- **Kunlun**: Unified architecture scaling laws for recommendation.
- **ULTRA-HSTU**: Bending scaling law curve for generative recommendation.
- **Foundation-Expert Paradigm**: Foundation model + expert routing for recommendation.

### Microsoft Research

- **SkillOpt**: Self-Evolving Agent Skills (Microsoft Research Asia).
- **Agentic Proving**: Formal verification using agent-based reasoning.

### Alibaba (Qwen Team)
- **Gated Attention** (NeurIPS 2025 Best Paper) — integrated into Qwen3-Next.
- **UniAR** (ICML 2026) — unified multimodal autoregressive modeling.
- **FAT / EST / GPSD**: Multiple CTR scaling and generative CTR papers.

### NVIDIA
- **DiLaDiff** (ICML 2026): Distilled latent-augmented diffusion LM.
- **Nemotron 3**: Mamba-Transformer Hybrid MoE architecture.

### Apple
- **VSAS-Bench** (CVPR 2026): Streaming VLM evaluation benchmark.
- **SGE**: Tree search for on-device generation.

### OpenAI
- **GPT-5.4 Mini and Nano**: Faster reasoning models.
- **o3 Reasoning Model**: 10× training compute vs o1.

### Anthropic
- **Claude Opus 4.8** (May 2026): Latest frontier model.

---

## Meta Trends & Key Takeaways

1. **Diffusion LLMs are rising**: LLaDA (NeurIPS 2025 Oral) and Inception Mercury 2 demonstrate that non-autoregressive language models are competitive with ARMs. LLaDA 8B matches LLaMA3 8B.

2. **RL for reasoning is the dominant post-training paradigm**: DeepSeek-R1 proved RLVR works at scale. GRPO/PPO for reasoning is now standard, but NeurIPS 2025 Runner-Up paper questions whether RL truly expands capability beyond the base model.

3. **SSM architectures are maturing**: Mamba-3 (ICLR 2026 Oral) solves state-tracking tasks Mamba-2 cannot, proving sub-quadratic architectures can match/exceed Transformers on the Pareto frontier.

4. **Gated Attention is a new architectural primitive**: Alibaba's NeurIPS Best Paper shows a simple sigmoid gate after attention eliminates attention sinks, stabilizes training, and improves scaling.

5. **Generative recommendation paradigm**: HSTU, GenCI, ThinkRec — the shift from discriminative matching to generative next-item prediction is accelerating.

6. **CTR scaling laws are the new frontier**: FAT (Alibaba KDD), EST (Alibaba), TokenMixer-Large (ByteDance) — industrial labs are actively developing scaling theories for ranking models.

7. **Agent systems are moving from demos to infrastructure**: KAIROS, AgentFlow, MEM1, and multi-agent memory systems signal maturation beyond proof-of-concept.

8. **Multi-modal unification**: ByteDance Lance shows one 3B model can handle image/video understanding, generation, and editing simultaneously.

9. **Deflationary findings are being rewarded**: "RLVR doesn't expand reasoning," "LLMs lose 39% across multi-turn," "alignment is shallow," "model outputs are homogeneous" — the field rewards critical evaluation.

10. **Mechanistic explanations are back**: Theory papers grounded in clean experiments (diffusion memorization, scaling laws from superposition, attention sinks) are being recognized at the highest level.

---

*Report generated 2026-06-09. Sources include conference proceedings, arXiv, official award announcements, and institutional publications.*
