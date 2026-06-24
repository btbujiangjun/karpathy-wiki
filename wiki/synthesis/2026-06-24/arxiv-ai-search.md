---
title: "arXiv AI Research Search — June 2026"
type: synthesis
created: 2026-06-24
updated: 2026-06-24
sources: []
tags: [arxiv, ai, llm, recommendation, ctr, games, sequential-modeling, reinforcement-learning]
---

# arXiv AI Research Search — June 2026

> A curated survey of recent papers from arXiv spanning LLMs, training efficiency, CTR prediction, generative recommendation, reasoning, games, and multi-agent RL. Compiled 2026-06-24.

---

## Table of Contents

1. [Foundation Models & LLM Training](#1-foundation-models--llm-training)
2. [Reasoning & Test-Time Scaling](#2-reasoning--test-time-scaling)
3. [CTR Prediction & Advertising](#3-ctr-prediction--advertising)
4. [Generative Recommendation](#4-generative-recommendation)
5. [Sequential Modeling](#5-sequential-modeling)
6. [Games & RL](#6-games--rl)
7. [Multi-Agent & Agentic Systems](#7-multi-agent--agentic-systems)

---

## 1. Foundation Models & LLM Training

### Memory-Efficient LLM Training with Dynamic Sparsity (SMET)

| Field | Detail |
|-------|--------|
| **Authors** | Qiao Xiao, Boqian Wu, Patrik Okanovic, Tomasz Sternal, Maurice van Keulen, Elena Mocanu, Mykola Pechenizkiy, Decebal Constantin Mocanu, Torsten Hoefler |
| **Institution** | ETH Zurich, University of Twente |
| **arXiv** | [2606.00888](https://arxiv.org/abs/2606.00888) |
| **Venue** | ICML 2026 |

**Abstract:** Dynamic Sparse Training (DST) suffers from optimization instability (loss spikes after topology updates) in LLM training due to a cold-start issue for regrown parameters. SMET stabilizes DST with optimizer warm-up and density-aware LR scaling, storing gradients/optimizer states only for active parameters.

**Key Innovations:**
- Identifies root cause of DST instability in LLM training (cold-start optimizer states)
- SMET: optimizer warm-up + density-aware LR scaling
- Reduces memory by storing gradients/states only for active parameters
- Enables stable, scalable sparse pre-training of LLMs

---

### OpenThoughts-Agent: Data Recipes for Agentic Models

| Field | Detail |
|-------|--------|
| **Authors** | Negin Raoof, Richard Zhuang, Marianna Nezhurina, Etash Guha, et al. (50 authors) |
| **Institution** | Multiple (academic consortium) |
| **arXiv** | [2606.24855](https://arxiv.org/abs/2606.24855) |

**Abstract:** OpenThoughts-Agent addresses the lack of open data curation pipelines for broadly capable agentic models. Conducts 100+ controlled ablations on data curation stages. Fine-tunes Qwen3-32B on a 100K training set, achieving 44.8% avg accuracy across 7 agentic benchmarks (+3.9pp over prior SOTA).

**Key Innovations:**
- Fully open data curation pipeline for agentic models
- 100+ ablation experiments investigating data source diversity
- Qwen3-32B fine-tuned on 100K examples outperforms Nemotron-Terminal-32B
- Strong scaling properties — outperforms alternative open datasets at every training set size

---

### Quantized Reasoning Models Think They Need to Think Longer, but They Do Not

| Field | Detail |
|-------|--------|
| **Authors** | Sanae Lotfi, Polina Kirichenko, Steven Li, Zechun Liu |
| **Institution** | — |
| **arXiv** | [2606.00206](https://arxiv.org/abs/2606.00206) |

**Abstract:** Post-training quantization (PTQ) reduces accuracy in reasoning models while increasing chain-of-thought (CoT) length. In up to 52% of failures, models reach the right answer in intermediate steps but don't output it. A training-free logit penalty on overthinking markers reduces CoT length 12–23% while preserving accuracy.

**Key Innovations:**
- Discovers "overthinking" phenomenon in quantized reasoning models
- Traces root cause to KL divergence peaks at high-entropy token positions
- Simple training-free fix: penalize overthinking markers ("wait", "but", "alternatively")
- Reduces CoT length 12–23% with accuracy preservation across 5 models, 3 quantization methods

---

## 2. Reasoning & Test-Time Scaling

### ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Vladislav Smirnov et al. |
| **Institution** | — |
| **arXiv** | [2606.06915](https://arxiv.org/abs/2606.06915) |

**Abstract:** ThinkBooster is a unified framework for test-time compute (TTC) scaling: modular Python library, benchmark for performance–compute trade-offs, and deployable OpenAI-compatible proxy for drop-in adaptive reasoning.

**Key Innovations:**
- Modular library implementing SOTA TTC strategies and scorers
- Joint evaluation of performance and computational efficiency
- Deployable proxy service for real-world drop-in integration
- Visual debugger for reasoning trajectory inspection

---

### GRACE: Granularity-Regulated Adaptive Computational Efficiency for Optimal Verification in TTS

| Field | Detail |
|-------|--------|
| **Authors** | Ardit Krasniqi, Luan Vejsiu, Elira Dervishi |
| **Institution** | — |
| **arXiv** | [2606.19354](https://arxiv.org/abs/2606.19354) |

**Abstract:** Unified theoretical framework characterizing optimal verification granularity as explicit function of problem difficulty, verifier accuracy, and compute budget. Proves phase transition: fine-grained verification dominates when compute budget is large or problem is hard; coarse-grained when budget is low.

**Key Innovations:**
- Unifies ORM (outcome reward) and PRM (process reward) models under single Pareto-optimality framework
- Proves phase transition in verification granularity
- Adaptive granularity strategy achieving compute-performance Pareto frontier
- Up to 3.1% accuracy improvement at matched compute on MATH-500, GSM8K, AIME

---

### Agentic Chain-of-Thought Steering (ACTS)

| Field | Detail |
|-------|--------|
| **Authors** | Yu Xia, Zhouhang Xie, Xin Xu, Byungkyu Kang, Prarit Lamba, Xiang Gao, Julian McAuley |
| **Institution** | UC San Diego |
| **arXiv** | [2606.03965](https://arxiv.org/abs/2606.03965) |

**Abstract:** ACTS formulates reasoning steering as an MDP where a controller agent adaptively steers a frozen reasoner. At each step, the controller issues a reasoning strategy + steering phrase. Initialized from synthetic trajectories, optimized via RL with budget-conditioned reward shaping.

**Key Innovations:**
- Two-level agent+reasoner architecture for controllable inference
- Budget-aware strategy control via MDP formulation
- RL optimization with budget-conditioned reward shaping
- Matching full-thinking performance with substantial token savings

---

## 3. CTR Prediction & Advertising

### Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)

| Field | Detail |
|-------|--------|
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen |
| **Institution** | Renmin University of China |
| **arXiv** | [2606.04944](https://arxiv.org/abs/2606.04944) |
| **Venue** | ACM TKDD |

**Abstract:** DS-MLP uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP network while a parallel MLP captures implicit interactions. Despite being a vanilla MLP, achieves SOTA across 3 benchmarks.

**Key Innovations:**
- Distills explicit feature interactions into a single MLP stream
- Parallel MLP captures implicit interactions as complement
- Two alignment strategies for dual-stream compatibility
- SOTA performance with vanilla MLP structure — scalable and efficient

---

### Unified Value Alignment for Generative Recommendation in Industrial Advertising (UniVA)

| Field | Detail |
|-------|--------|
| **Authors** | Xinxun Zhang, Yuling Xiong, Jiale Zhou, Zhengkai Guo, et al. (16 authors) |
| **Institution** | Tencent |
| **arXiv** | [2605.05803](https://arxiv.org/abs/2605.05803) |

**Abstract:** UniVA extends generative recommendation to industrial advertising by optimizing both user interest and commercial value. Introduces Commercial SID tokenizer, Generation-as-Ranking SID Decoder with eCPM-aware RL, and value-guided personalized beam search.

**Key Innovations:**
- Commercial SID tokenizer injecting value attributes into SID construction
- Generation-as-Ranking decoder with eCPM-aware reinforcement learning
- Value-guided personalized beam search with request-valid trie constraint
- 37% offline HitRate@100 improvement, 1.5% GMV lift in Tencent WeChat Channels A/B test

---

### IDProxy: Cold-Start CTR Prediction for Ads and Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2603.01590](https://arxiv.org/abs/2603.01590) |

**Abstract:** IDProxy leverages multimodal LLMs to generate proxy embeddings from rich content signals, enabling effective CTR prediction for new items without usage data.

**Key Innovations:**
- MLLM-generated proxy embeddings for cold-start items
- Bridges content signals to CTR prediction without historical data
- Plug-and-play with existing CTR models

---

### FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | Tencent |
| **arXiv** | [2605.01726](https://arxiv.org/abs/2605.01726) |

**Abstract:** Sequential recommendation models struggle with periodic patterns in user interests. FEDIN enhances deep interest networks with frequency-domain analysis to capture latent periodic patterns.

**Key Innovations:**
- Frequency-domain analysis for periodic user interest patterns
- Noise reduction in time-domain behavioral data
- Practical deployment at Tencent

---

## 4. Generative Recommendation

### MTGR: Industrial-Scale Generative Recommendation Framework in Meituan

| Field | Detail |
|-------|--------|
| **Authors** | Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, et al. (15 authors) |
| **Institution** | Meituan |
| **arXiv** | [2505.18654](https://arxiv.org/abs/2505.18654) |

**Abstract:** MTGR is an HSTU-based generative recommendation framework that retains DLRM cross features. Uses Group-Layer Normalization (GLN) and dynamic masking. Achieves 65x FLOPs vs DLRM with 1.22% conversion lift and 1.31% CTR lift in Meituan's food delivery platform.

**Key Innovations:**
- Retains cross features in generative recommendation (unlike prior GR approaches)
- Group-Layer Normalization for multi-semantic-space encoding
- Dynamic masking strategy preventing information leakage
- User-level compression for efficient scaling
- Deployed serving hundreds of millions of users

---

### MBGR: Multi-Business Prediction for Generative Recommendation at Meituan

| Field | Detail |
|-------|--------|
| **Authors** | Changhao Li, Junwei Yin, Zhilin Zeng, Senjie Kou, et al. (9 authors) |
| **Institution** | Meituan |
| **arXiv** | [2604.02684](https://arxiv.org/abs/2604.02684) |

**Abstract:** MBGR addresses the "seesaw phenomenon" in multi-business generative recommendation. Introduces Business-aware semantic ID (BID), Multi-Business Prediction (MBP) structure, and Label Dynamic Routing (LDR) for multi-business capability.

**Key Innovations:**
- First GR framework tailored for multi-business scenarios
- Business-aware SID (BID) with domain-aware tokenization
- Multi-Business Prediction structure for business-specific predictions
- Label Dynamic Routing transforms sparse multi-business labels into dense labels

---

### Unified Value Alignment for Generative Recommendation (UniVA)

*(Already detailed in Section 3)*

---

## 5. Sequential Modeling

### NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation

| Field | Detail |
|-------|--------|
| **Authors** | Liao Qu et al. |
| **Institution** | ByteDance (ByteVisionLab) |
| **arXiv** | [2601.02204](https://arxiv.org/abs/2601.02204) |

**Abstract:** NextFlow is a unified decoder-only autoregressive transformer trained on 6T interleaved text-image tokens. Uses next-token prediction for text, next-scale prediction for images. Generates 1024x1024 images in 5 seconds — orders of magnitude faster than comparable AR models.

**Key Innovations:**
- Unified vision representation in a single autoregressive architecture
- Next-scale prediction for visual generation (vs. raster-scan)
- 6T interleaved text-image token training
- Prefix-tuning strategy for RL
- SOTA among unified models, rivaling diffusion baselines

---

### Beyond Autoregressive RTG: SlimDT for Decision Transformer

| Field | Detail |
|-------|--------|
| **Authors** | Yongyi Wang, Hanyu Liu, Lingfeng Li, Bozhou Chen, Ang Li, et al. |
| **Institution** | — |
| **arXiv** | [2605.06104](https://arxiv.org/abs/2605.06104) |

**Abstract:** SlimDT removes Return-to-Go (RTG) from the autoregressive sequence in Decision Transformer, injecting RTG into state representations before sequential modeling. Reduces sequence length by 1/3 while surpassing standard DT on D4RL.

**Key Innovations:**
- Decouples conditioning signal from information-rich sequence
- RTG injection before (not during) sequential modeling
- 33% sequence length reduction → direct inference speedup
- Surpasses standard DT across D4RL tasks

---

## 6. Games & RL

### Superhuman AI for Generals.io Using Self-Play RL

| Field | Detail |
|-------|--------|
| **Authors** | Matej Straka, Viliam Lisý, Martin Schmid |
| **Institution** | Czech Technical University (CTU) |
| **arXiv** | [2606.23348](https://arxiv.org/abs/2606.23348) |

**Abstract:** Superhuman AI for the real-time strategy game Generals.io. Trained 4 days on 4x H200 GPUs. Reaches #1 on public 1v1 leaderboard (5000+ players). Beats top humans 199-70. Key enabler: JAX-native simulator with ~10,000x speedup over prior simulator.

**Key Innovations:**
- JAX-native game simulator reaching tens of millions FPS on single GPU
- Vision Transformer policy trained end-to-end via self-play
- Top-advantage sample filtering
- EMA policy parameters for stabilization
- Demonstrates that fast simulator removes data bottleneck

---

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2506.24119](https://arxiv.org/abs/2506.24119) (updated Mar 2026) |

**Abstract:** SPIRAL is a self-play framework where LLMs learn by playing multi-turn zero-sum games against themselves. Implements fully online multi-agent RL with role-conditioned advantage estimation (RAE). Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama model families.

**Key Innovations:**
- Automatic curriculum of stronger opponents via self-play
- Role-conditioned advantage estimation (RAE) for multi-agent stability
- Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest transfer
- Outperforms SFT on 25K expert trajectories
- Different games develop complementary reasoning patterns

---

### GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation

| Field | Detail |
|-------|--------|
| **Authors** | Yuxiao Ye, Yiwen Zhang, Huiyuan Xie, Yuqin Huang, Zhiyuan Liu |
| **Institution** | — |
| **arXiv** | [2606.05002](https://arxiv.org/abs/2606.05002) |

**Abstract:** GARL formalizes strategic prioritisation as a two-stage game where competing agents allocate resources and an arbiter produces final ranking. Game-theoretic utilities become RL signals. Small open-source LLMs become competitive with strong closed-source models.

**Key Innovations:**
- Two-stage game formulation for strategic resource allocation
- Role-specific RL signals derived from game utilities
- Enables small open LLMs to compete with closed-source models
- Tested on legal issues-in-dispute ranking

---

### Age of LLM: A Strategic 1v1 Benchmark for Reasoning, Diplomacy and Reliability under Fog of War

| Field | Detail |
|-------|--------|
| **Authors** | Arnaud Ricci |
| **Institution** | — |
| **arXiv** | [2606.24391](https://arxiv.org/abs/2606.24391) |

**Abstract:** A strategic 1v1 benchmark evaluating LLMs under fog of war conditions, testing reasoning, diplomacy, and reliability. Includes verbatim system prompts and engine resolution pseudocode.

**Key Innovations:**
- Multi-dimensional evaluation (reasoning + diplomacy + reliability)
- Fog of war (imperfect information) setting
- Statistical rigor with bootstrap CIs, p-values, Bradley-Terry fit

---

## 7. Multi-Agent & Agentic Systems

### OpenThoughts-Agent (OT-Agent)

*(Already detailed in Section 1)*

### AVIS: Adaptive Test-Time Scaling for Vision-Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Hakki Karaimer et al. |
| **Institution** | — |
| **arXiv** | [2606.11576](https://arxiv.org/abs/2606.11576) |

**Abstract:** AVIS adapts both Visual Context Scaling (VCS) and Visual Reasoning Scaling (VRS) per query. VCS via Key Diversity Visual (KDV) pruning, VRS via adaptive self-consistency. Improves accuracy–compute trade-off across image/video reasoning benchmarks.

**Key Innovations:**
- Joint optimization of visual context + reasoning compute
- Training-free KDV pruning for redundant visual tokens
- Learned difficulty predictor for reasoning rollout count
- Compatible with shared-prefill inference
- Effective on RL post-trained VLMs

---

## Summary

| Category | Key Papers | Trend |
|----------|-----------|-------|
| **LLM Training** | SMET, OT-Agent | Sparse training goes practical; open-source agentic data pipelines |
| **Reasoning / TTS** | ThinkBooster, GRACE, ACTS | Verification granularity theory; controllable CoT; steering frameworks |
| **CTR / Ads** | DS-MLP, UniVA, IDProxy, FEDIN | MLP simplicity returns; generative + value alignment for ads; cold-start MLLM proxy |
| **Gen Recommendation** | MTGR, MBGR, UniVA | HSTU-based GR with cross-features; multi-business scaling; value-aware SID |
| **Sequential Modeling** | NextFlow, SlimDT | Unified text-image AR; efficient Decision Transformer |
| **Games / RL** | Generals.io AI, SPIRAL, GARL, Age of LLM | JAX-native simulators; self-play for reasoning transfer; game-theoretic multi-agent |
| **Multi-Agent** | OT-Agent, AVIS, GARL | Data-centric agent training; adaptive VLM inference; game-theoretic RL |

### Emerging Themes

1. **Efficiency everywhere** — sparse training, quantization overthinking fixes, test-time scaling compute budgets
2. **Generative recommendation matures** — Tencent, Meituan, and Kuaishou all deploying GR at scale with cross-feature retention and value alignment
3. **Self-play for reasoning** — SPIRAL shows games teach transferable reasoning patterns
4. **Agentic data pipelines** — OT-Agent demonstrates open data curation can beat proprietary efforts
5. **Simulators unlock game AI** — 10,000x speedup from JAX-native simulators makes self-play practical for complex games
