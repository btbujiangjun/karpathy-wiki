---
title: "arXiv Daily Report - 2026-07-27"
type: synthesis
created: 2026-07-27
updated: 2026-07-27
tags: [arxiv-daily, llm, recommendation, ctr, sequential-modeling, ads, games, rl]
---

# arXiv Daily Report — 2026-07-27

Curated selection of recent arXiv papers across AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and games. Papers are from July 21–27, 2026.

---

## 1. LLMs & Inference

### 1.1 Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context

| Field | Detail |
|-------|--------|
| **Authors** | Alagappan Valliappan |
| **Affiliation** | Independent |
| **Date** | Jul 23, 2026 |
| **Link** | [arXiv:2607.21535](https://arxiv.org/abs/2607.21535) |

**Abstract:** Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. At million-token context, the MTP draft head's full-attention KV cache read grows linearly and dominates draft cost. Windowed-MTP applies a StreamingLLM-style sliding window plus attention sink to the draft's attention only, leaving full-attention verification intact. It is training-free, drop-in, and lossless by construction.

**Key Innovations:**
- Sliding window + attention sink applied only to the draft's attention, preserving lossless verification
- Bounds draft KV working set to constant, dropping ~99% of KV entries at 1M context
- +28% to +44% per-decode-step cost reduction across Qwen and Mamba2-hybrid architectures
- Compact ring buffer reclaims unused draft KV at no quality cost

---

### 1.2 MIRROR: Learning from the Other View for Multi-Modal Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma |
| **Affiliation** | — |
| **Date** | Jul 23, 2026 |
| **Link** | [arXiv:2607.21552](https://arxiv.org/abs/2607.21552) |

**Abstract:** VLMs struggle with visual reasoning, exhibiting inconsistent behavior across text, diagram, and combined views of the same problem. MIRROR constructs a paired multimodal geometry dataset (ODA-Data) and develops a reinforcement learning approach where the model evaluates itself under all views, selects the best-performing view as teacher, and trains other views with reverse-KL.

**Key Innovations:**
- Paired multimodal dataset with text-dominant, image-dominant, and combined views
- Self-supervised RL approach: cross-view distillation via reverse-KL without external supervision
- Improves accuracy and consistency across modalities on geometry reasoning benchmarks

---

### 1.3 ISO: An RLVR-Native Optimization Stack

| Field | Detail |
|-------|--------|
| **Authors** | Hanqing Zhu, Wenyan Cong, Zhizhou Sha, Sagnik Mukherjee, Xinyuan Song, David González-Martínez, Xiaoxia Wu, Yuandong Tian, Shiwei Liu, David Z. Pan, Zhangyang "Atlas" Wang |
| **Affiliation** | UT Austin, Meta FAIR |
| **Date** | Jul 21, 2026 |
| **Link** | [arXiv:2607.19331](https://arxiv.org/abs/2607.19331) |

**Abstract:** RLVR advances LLM reasoning capabilities but the optimization layer converting reward feedback into weight updates remains poorly understood. ISO identifies spectral inheritance: RLVR can reuse the base model's weight spectra while acquiring new behavior through changes in singular frames. Offers offline (ISO-Merger) and online (ISO-Optimizer) instantiations.

**Key Innovations:**
- Spectral inheritance principle: inherit spectrum, optimize frames for post-training
- ISO-Merger combines specialist capabilities without post-merge data/rollouts/gradients
- ISO-Optimizer reaches matched accuracy in ~37% fewer training steps on Qwen3-8B
- Applicable from 1.5B to 8B parameters across reasoning and coding tasks

---

### 1.4 Fast and Efficient Approximate Nearest Neighbor Search for High-Dimensional LLM Embeddings

| Field | Detail |
|-------|--------|
| **Authors** | Nico Hezel, Kai Uwe Barthel, Bruno Schilling, Konstantin Schall, Andre Moelle, Klaus Jung |
| **Affiliation** | — |
| **Date** | Jul 23, 2026 |
| **Link** | [arXiv:2607.20957](https://arxiv.org/abs/2607.20957) |

**Abstract:** Submissions for the 2026 SISAP Indexing Challenge addressing kNNG construction on 1024-dim BGE-M3 embeddings and MIPS on Llama-3.2-8B features. Uses Equi-Voronoi Polytopes for quantization and Fast Linear Assignment Sorting for 1D presorting before graph construction.

**Key Innovations:**
- Equi-Voronoi Polytope quantization for fast kNNG construction
- Fast Linear Assignment Sorting (FLAS) for spatial locality optimization
- Dimensionality augmentation to transform MIPS into Euclidean search

---

## 2. Recommendation Systems

### 2.1 DLMRec: Diffusion Language Model for Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Chengyi Liu, Yongqi Zhou, Junwei Pan, Zhixiang Feng, Chengguo Yin, Haijie Gu, Jie Jiang, Yinghao Liu, Yujuan Ding, Qing Li, Wenqi Fan |
| **Affiliation** | — |
| **Date** | Jul 23, 2026 |
| **Link** | [arXiv:2607.21519](https://arxiv.org/abs/2607.21519) |

**Abstract:** LLM-empowered recommender systems mostly rely on autoregressive paradigms that are suboptimal for recommendation. DLMRec introduces a discrete diffusion language model tailored for recommendation with three key components: collaborative-aware stochastic tokenizer, curriculum-driven training strategy, and stability-aware voting mechanism.

**Key Innovations:**
- First discrete diffusion language model specifically designed for recommendation
- Collaborative-aware stochastic tokenizer encoding multi-hop collaborative signals
- Curriculum-driven training aligning denoising with progressive preference recovery
- Stability-aware voting mechanism for robust generation consistency

---

### 2.2 UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction

| Field | Detail |
|-------|--------|
| **Authors** | Honghao Li, Xianquan Wang, Zibin Zhang, Yi Zhang, Kangyi Lin, Yiwen Zhang |
| **Affiliation** | — |
| **Date** | Jul 22–23, 2026 |
| **Link** | [arXiv:2607.19987](https://arxiv.org/abs/2607.19987) |

**Abstract:** An open benchmark for ranking models that unify sequential modeling and feature interaction. Benchmarks 15 representative unified ranking models on five large-scale public datasets from short-video, advertising, and e-commerce, with the largest dataset containing over 700M instances.

**Key Innovations:**
- Open benchmark with 15 unified ranking models and 5 large-scale public datasets
- Chronological pointwise autoregressive supervision for standardized evaluation
- PyTorch toolkit with DDP training, mixed-precision, and attention optimization
- Reproducible basis for studying scaling laws under limited compute

---

### 2.3 DeltaGate: Zero-Observation User Reactivation with Gap-Driven Dimensional Gating

| Field | Detail |
|-------|--------|
| **Authors** | Jiandong Ding, Tianying Liu, Fuyuan Liu, Huijie Qin, Tiandeng Wu |
| **Affiliation** | — |
| **Date** | Jul 22, 2026 |
| **Venue** | RecSys 2026 |
| **Link** | [arXiv:2607.19802](https://arxiv.org/abs/2607.19802) |

**Abstract:** Addresses Zero-Observation Reactivation: returning users with no interactions for months/years. DeltaGate is a lightweight output-layer plugin that routes each representation dimension between personalized history and a learned global prior, conditioned jointly on gap duration and representation. Achieves 0.047 Hit@10 vs 0.031 for SASRec in >365d gap scenarios with only 66K trainable parameters.

**Key Innovations:**
- Novel problem definition: Zero-Observation User Reactivation
- Lightweight plug-and-play gating module (2–4% parameter overhead)
- Frozen backbone preserves zero drift; 40x fewer parameters than end-to-end retraining
- Dimension-wise routing with interpretability into gap-dependent behavior

---

### 2.4 PRTA: Personalized Recommendation Tool Learning via Autonomous Language Agents

| Field | Detail |
|-------|--------|
| **Authors** | Mingdai Yang, Zhiwei Liu, Weizhi Zhang, Yibo Wang, Hao Peng, Philip Yu |
| **Affiliation** | — |
| **Date** | Jul 22, 2026 |
| **Venue** | RecSys 2026 |
| **Link** | [arXiv:2607.19739](https://arxiv.org/abs/2607.19739) |

**Abstract:** Proposes an agent-based recommendation framework where an LLM acts as central planner interacting with multiple recommendation models as tools. The LLM handles high-level reasoning and personalized tool selection, while traditional models perform full-ranking. Reflection mechanisms enable the agent to evaluate and compare tools per user.

**Key Innovations:**
- LLM-as-planner architecture with traditional RecSys models as tools
- Reflection mechanisms for personalized tool selection per user
- Avoids LLM hallucination and context-length limits in full-ranking by delegating scoring to traditional models

---

### 2.5 PRL: Probabilistic Residual Learning for Online Recommendations

| Field | Detail |
|-------|--------|
| **Authors** | Wenyuan Wang, Yusong Zhao, Zihao Xu, Hengyi Wang, Qi Xu, Zhigang Hua, Yan Xie, Yi Wang, Zihao Zhao, Bo Long, Chengzhi Mao, Shuang Yang, Hengguan Huang, Hao Wang |
| **Affiliation** | — |
| **Date** | Jul 23, 2026 |
| **Venue** | RecSys 2026 |
| **Link** | [arXiv:2607.20863](https://arxiv.org/abs/2607.20863) |

**Abstract:** PRL is a causal Bayesian recommendation model that models the residual between ground-truth and base predictions. It probabilistically groups users for localized residual modeling, models domain-level confounders, and aggregates cluster-specific residuals using do-calculus. Plug-and-play compatible with various base recommender systems.

**Key Innovations:**
- Causal Bayesian framework for residual modeling on top of existing systems
- Do-calculus based aggregation over confounders for debiased refinement
- Plug-and-play compatibility with any base deep learning recommender
- Automatic user cluster discovery for localized modeling

---

### 2.6 CDL: Cardinality-Decomposed Loss for Heterogeneous Recommendation Graphs

| Field | Detail |
|-------|--------|
| **Authors** | Parul Maheshwari, Amulya Paruchuri, Yiqing Zou, Alireza Sahami Shirazi, Farhad Farahani, Prakhar Mehrotra |
| **Affiliation** | — |
| **Date** | Jul 22, 2026 |
| **Link** | [arXiv:2607.20737](https://arxiv.org/abs/2607.20737) |

**Abstract:** BPR loss causes attribute embeddings to collapse to near-random geometry in heterogeneous recommendation graphs — a silent failure invisible to standard ranking metrics. CDL combines Cross Entropy and BPR to enable collective optimization across cardinalities, guided by two graph properties: semantic alignment and topology leakage.

**Key Innovations:**
- Identifies silent attribute embedding collapse under standard BPR training
- Cardinality-Decomposed Loss combining CE and BPR for mixed-cardinality graphs
- Lambda-sweep reveals governing graph properties: semantic alignment and topology leakage
- Consistent improvements on 5 datasets spanning multiple structural configurations

---

## 3. Advertising & CTR

### 3.1 LO-FAR: A Cost-Aware Local Filter for Sparse Feature Ranking in Industrial Ad Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Egemen Erbayat, Luis Duque, Sohini Roychowdhury, Mohammad Amin, Srihari Reddy |
| **Affiliation** | — |
| **Date** | Jul 23, 2026 |
| **Venue** | RecSys 2026 |
| **Link** | [arXiv:2607.20873](https://arxiv.org/abs/2607.20873) |

**Abstract:** Industrial ad recommendation models rely on sparse, high-cardinality ID-list features that dominate storage, training, and serving cost. LO-FAR is a CPU-only, model-agnostic workflow that ranks candidate features using lightweight local estimators. Completes ranking in ~2 CPU-hours on a production dataset of 1M+ interactions and 475 sparse features.

**Key Innovations:**
- CPU-only, model-agnostic feature ranking workflow (no GPU retraining loops)
- Lightweight local estimators instead of permutation/stochastic-gate methods
- Practical production choice: completes in ~2 CPU-hours on real production data
- Maintains competitive Normalized Entropy gains at 100–400 retained features

---

## 4. Generative Retrieval & Search

### 4.1 Prompt Generation Technical Report

| Field | Detail |
|-------|--------|
| **Authors** | Dan Ou, Gui Ling, Hao Wan, Hongbin Zhou, Jialiang Cheng, Jiangnan Pang, Silu Zhou, Wei Shi, Weichen Ye, Wenming Zhang, Yang Wang, Yu Li, Yuliang Yan, Zhan Fa, Zhihong Chen, Zongyuan Wu, Bo Zheng, Changfa Wu, Dunxian Huang, Haihong Tang, Jinlong Guo, Kaixuan Zhang, Kun Ma, Lin Qu, Longbo Zhong, Tao Lan, Tong Xiong, Zhibo Wu |
| **Affiliation** | Alibaba (Taobao) |
| **Date** | Jul 13, 2026 |
| **Link** | [arXiv:2607.11326](https://arxiv.org/abs/2607.11326) |

**Abstract:** Generative retrieval is increasingly adopted for industrial search, recommendation, and advertising. Prompt Generation (PG) is a tokenizer and configuration-driven framework that decouples feature-processing logic from model architecture through two declarative JSON files serving as the single source of truth for offline training and online serving.

**Key Innovations:**
- Configuration-driven framework decoupling features from model architecture via JSON configs
- Three acceleration levels: fast training iteration, fast deployment, fast online inference
- Built-in token compression for ultra-long sequences
- Deployed on Taobao Search: +0.47% transaction count, +0.51% GMV in A/B test

---

## 5. Game AI & Reinforcement Learning

### 5.1 Augmenting Game AI with Deep Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Alessandro Sestini et al. |
| **Affiliation** | — |
| **Date** | Jun 18, 2026 |
| **Venue** | Conference on Games 2026 |
| **Link** | [arXiv:2606.20210](https://arxiv.org/abs/2606.20210) |

**Abstract:** Envisions broader applications of RL for game AI, proposing a framework for training RL models with requirements suited towards game AI and game development. Presents examples of games with RL-augmented AI, describes practicalities of deploying player-facing ML agents, and identifies bottlenecks and hard problems.

**Key Innovations:**
- Practical framework for deploying player-facing RL agents in modern games
- Addresses research limitations inhibiting broad deployment across game genres
- Identifies bottleneck problems as promising research directions
- Covers real-world examples from football simulation to goalkeeping

---

## Summary of Key Trends

| Trend | Representative Papers |
|-------|----------------------|
| **Diffusion models for RecSys** | DLMRec — discrete diffusion as alternative to autoregressive recommendation |
| **Unified ranking architectures** | UniRank — benchmark for merging sequential modeling + feature interaction |
| **LLM agents as RecSys orchestrators** | PRTA — LLM plans, traditional models score |
| **Causal/probabilistic refinement** | PRL — Bayesian residual modeling with do-calculus |
| **Efficient LLM inference at scale** | Windowed-MTP — constant-cost draft at million-token context |
| **RLVR optimization** | ISO — spectral inheritance for efficient post-training |
| **Industrial feature engineering** | LO-FAR, Prompt Generation — cost-aware and config-driven pipelines |
| **User reactivation** | DeltaGate — handling zero-observation returning users |
| **Game AI + RL** | Augmenting Game AI — practical deployment framework |
