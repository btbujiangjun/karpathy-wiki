---
title: "arXiv AI/LLM/RecSys/CTR/Game Search — 2026-07-15"
type: synthesis
created: 2026-07-15
updated: 2026-07-15
sources: []
tags: [arxiv, ai, llm, recommendation, ctr, sequential-modeling, games, reinforcement-learning]
---

# arXiv Recent Papers Survey — AI, LLMs, Recommendation, CTR, Sequential Modeling, Games

> Generated on 2026-07-15. Papers span roughly Jan–Jul 2026.

---

## 1. Large Language Models & Foundation Models

### 1.1 MiniMax Sparse Attention (MSA)

- **Title:** MiniMax Sparse Attention
- **Authors:** MiniMax Team
- **Institution:** MiniMax AI
- **Date:** 2026-06
- **Abstract:** Introduces MSA, a blockwise sparse attention mechanism built on GQA. A lightweight Index Branch scores KV blocks and selects a Top-k subset per GQA group; the Main Branch performs exact block-sparse attention on selected blocks. On a 109B MoE model with native multimodal training, MSA matches GQA quality while reducing per-token attention compute by 28.4x at 1M context. Co-designed GPU kernels achieve 14.2x prefill and 7.6x decoding wall-clock speedups on H800.
- **Key Innovation:** Blockwise sparse attention with group-specific Top-k selection; exp-free TopK kernel and KV-outer sparse attention for tensor-core utilization.
- **Link:** https://arxiv.org/abs/2606.13392

### 1.2 KARLA: Knowledge-base Augmented Retrieval for Language Models

- **Title:** KARLA: Knowledge-base Augmented Retrieval for Language Models
- **Authors:** Samy Haffoudhi, Fabian M. Suchanek, Nils Holzenberger
- **Institution:** Télécom Paris / Institut Polytechnique de Paris
- **Date:** 2026-06
- **Abstract:** Proposes training an LLM to emit special tokens that trigger queries to a knowledge base during generation. Facts are updated via KB edits rather than parameter updates. Small models (Qwen 0.6B) enhanced with KARLA beat larger models on factual accuracy. Introduces Counterfactual YAGO benchmark for factual overriding.
- **Key Innovation:** Separating linguistic competence from factual knowledge via KB-triggered query tokens; zero-shot factual updates without retraining.
- **Link:** https://arxiv.org/abs/2606.26807

### 1.3 Evo: Autoregressive-Diffusion LLMs with Evolving Balance

- **Title:** Evo: Autoregressive-Diffusion Large Language Models with Evolving Balance
- **Authors:** Junde Wu, Minhao Hu, Jiayuan Zhu, Yuyuan Liu, Tianyi Zhang, Kang Li, et al.
- **Institution:** Tsinghua University / Various
- **Date:** 2026-02
- **Abstract:** Unifies AR and diffusion generation within a single latent flow model. Each token has a vector-valued embedding that evolves over a progression variable, adaptively balancing AR refinement (low t) and diffusion planning (high t). Evo 8B achieves SOTA on 15 benchmarks including GSM8K, HumanEval, MBPP, at near-AR decoding speed (52 tokens/s).
- **Key Innovation:** Theoretical unification of AR and diffusion as discretizations of a shared probability flow; semantic-maturity-adaptive decoding.
- **Link:** https://arxiv.org/abs/2603.06617

### 1.4 A Family of LLMs Liberated from Static Vocabularies (HAT / T-Free)

- **Title:** A Family of LLMs Liberated from Static Vocabularies
- **Authors:** Aleph Alpha Research Team
- **Institution:** Aleph Alpha
- **Date:** 2026-03
- **Abstract:** Introduces HAT (Hierarchical Autoregressive Transformer) architecture: encoder aggregates bytes into word embeddings, backbone processes at word level, decoder generates bytes. Converts Llama 3.1 8B and 70B into tokenizer-free byte-level models. Demonstrates strong English and German performance, improving on original Llama 3.1 in most benchmarks. Released on Hugging Face.
- **Key Innovation:** Tokenizer-free LLM architecture with hierarchical byte-to-word-to-byte processing; eliminates fixed vocabulary limitations.
- **Link:** https://arxiv.org/abs/2603.15953

### 1.5 Large Language Model Reasoning Failures (Survey)

- **Title:** Large Language Model Reasoning Failures
- **Authors:** Peiyang Song, Pengrui Han, Noah D. Goodman
- **Institution:** Stanford University
- **Date:** 2026-02 (Cited by 42)
- **Abstract:** First comprehensive survey dedicated to reasoning failures in LLMs. Catalogs and taxonomizes the types of reasoning errors LLMs exhibit.
- **Key Innovation:** Systematic taxonomy of LLM reasoning failure modes.
- **Link:** https://arxiv.org/abs/2602.06176

---

## 2. Recommendation Systems

### 2.1 UniRec: Bridging Generative and Discriminative Recommendation via Chain-of-Attribute

- **Title:** UniRec: Bridging the Expressive Gap between Generative and Discriminative Recommendation via Chain-of-Attribute
- **Authors:** Shopee Research Team
- **Institution:** Shopee (Sea Group)
- **Date:** 2026-04
- **Abstract:** Proves via Bayes' theorem that generative models with full feature access match discriminative models. Introduces Chain-of-Attribute (CoA) — prefixing SID sequences with structured attribute tokens (category, seller, brand) to recover item-side feature crossing. Deployed on Shopee: +5.37% PVCTR, +4.76% orders, +5.60% GMV in online A/B tests. Capacity-constrained SID suppresses token collapse; CDC enables multi-scenario decoding.
- **Key Innovation:** CoA speculate-then-refine paradigm; theoretical proof that generative-discriminative gap comes from feature coverage, not modeling asymmetry.
- **Link:** https://arxiv.org/abs/2604.12234

### 2.2 Gryphon: Unified Architecture for Semantic-ID Generation and Item-Level Scoring

- **Title:** Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations
- **Authors:** Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov, Mariia Ulianova, Ilya Murzin
- **Institution:** Yandex Music
- **Date:** 2026-06
- **Abstract:** Encoder-decoder generative recommendation that adds jointly trained item-level scoring alongside SID generation. Resolves SIDs to concrete items and re-scores them, sidestepping miscalibrated sequence scores. +3.7% Recall@1000 over vanilla GR on Yandex Music. Deployed as sole candidate source, replacing 15+ candidate generators.
- **Key Innovation:** Item-level re-scoring of generated SIDs; collision resolution for multi-item collapse on single identifiers.
- **Link:** https://arxiv.org/abs/2606.08604

### 2.3 GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation

- **Title:** GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors:** Yanyan Zou, Junbo Qi, Lunsong Huang, et al.
- **Institution:** JD.com
- **Date:** 2026-04
- **Abstract:** Addresses three challenges in scaling GR to production: inconsistent outputs from pagination, prohibitive cost of long behavior sequences with multi-token SIDs, and alignment with user preference. Page-wise NTP, asymmetric Token Merger (2x compression), GRPO-SR (RL + NLL regularization + hybrid rewards). Deployed on JD App: +9.5% click count, +8.7% transaction count.
- **Key Innovation:** Page-wise NTP training; Token Merger for 2x input compression; GRPO-SR RL alignment.
- **Link:** https://arxiv.org/abs/2604.14878

### 2.4 GenAIR: Generative Archetype-Grounded Item Representations

- **Title:** Generative Archetype-Grounded Item Representations for Sequential Recommendation
- **Authors:** Yifan Li, Jiahong Liu, Xinni Zhang, et al.
- **Institution:** Various (KDD 2026)
- **Date:** 2026-04
- **Abstract:** Leverages LLMs to infer "archetype" textual descriptions of items' ideal target audiences. Behavioral calibration objective grounds these in real interaction data. Plug-and-play: improves performance of various sequential recommendation models.
- **Key Innovation:** Archetype-grounded item representations; behavioral calibration to bridge semantic and behavioral spaces.
- **Link:** https://arxiv.org/abs/2606.11023

### 2.5 R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs

- **Title:** R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs over Multi-Granular Interest Signals
- **Authors:** Various
- **Institution:** Various
- **Date:** 2026-03
- **Abstract:** Prompt-centric, retrieval-augmented framework unifying Multi-level User Intent Reasoning, Item Semantic Extraction, Long-Short Interest Polarity Mining, Similar User Collaborative Enhancement, and Reasoning-based Interest Matching. Up to +10.2% HR@1 improvement on Games and Bundle datasets.
- **Key Innovation:** Multi-granular intent reasoning with RAG-style similar user retrieval; training-light modular pipeline.
- **Link:** https://arxiv.org/abs/2603.13730

### 2.6 AgentX: Agent-Driven Self-Iteration of Industrial Recommender Systems

- **Title:** AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors:** AgentX Team (Kuaishou)
- **Institution:** Kuaishou
- **Date:** 2026-06
- **Abstract:** Multi-agent system that autonomously generates, implements, evaluates, and learns from recommendation experiments. Brainstorm Agent → Developing Agent → Evaluation Agent → Harness Evolution (SGPO). 3 workers turned 374 ideas into 10 launchable rollouts in 3 weeks; 8x concurrency, 3.7x business value over manual engineers, >100M RMB annualized revenue.
- **Key Innovation:** Self-evolving agent system for recommendation iteration; SGPO (Semantic-Gradient-based Prompt Optimization) for harness evolution.
- **Link:** https://arxiv.org/abs/2606.26859

### 2.7 Deep Research for Recommender Systems

- **Title:** Deep Research for Recommender Systems
- **Authors:** Kesha Ou, Chenghao Wu, Xiaolei Wang, et al.
- **Institution:** Renmin University / Various
- **Date:** 2026-03 (Cited by 2)
- **Abstract:** Argues that traditional "tool-based" paradigm limits user experience, as the system acts as a passive filter. Proposes deep research paradigm for recommender systems.
- **Key Innovation:** Paradigm shift from passive filtering to active research-driven recommendation.
- **Link:** https://arxiv.org/abs/2603.07605

---

## 3. CTR Prediction & Advertising

### 3.1 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer

- **Title:** CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors:** David Pardoe, Neil Daftary, Miro Furtado, et al. (23 authors)
- **Institution:** LinkedIn
- **Date:** 2026-02 (Cited by 2)
- **Abstract:** End-to-end decoder-only transformer for ads CTR prediction. Innovations: context-conditioned decoding with multi-tower heads for post-scoring signals; self-gated attention; timestamp-based RoPE; session masking for train-serve skew; tensor packing + custom Flash Attention kernels. +11.04% CTR lift over LiRank baseline in online A/B tests. Deployed on LinkedIn's homefeed sponsored updates.
- **Key Innovation:** Context-conditioned decoding resolving chicken-and-egg problem between predicted CTR and ranking; timestamp-based RoPE.
- **Link:** https://arxiv.org/abs/2602.11410

### 3.2 GRAB: Generative Ranking for Ads at Baidu

- **Title:** GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors:** Shaopeng Chen, Chuyue Xie, Huimin Ren, et al.
- **Institution:** Baidu
- **Date:** 2026-02
- **Abstract:** End-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA) mechanism. Captures temporal dynamics and action signals in user behavior sequences. +3.05% revenue, +3.49% CTR in full-scale online deployment. Monotonic approximately linear improvement with longer interaction sequences.
- **Key Innovation:** CamA mechanism for action-aware attention; sequence-first generative CTR paradigm scaling with longer histories.
- **Link:** https://arxiv.org/abs/2602.01865

### 3.3 EST: Efficient Scaling Laws in CTR Prediction

- **Title:** EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Authors:** Mingyang Liu, Yong Bai, Zhangming Chan, et al.
- **Institution:** Alibaba / Various
- **Date:** 2026-02 (Cited by 2)
- **Abstract:** Explores efficient scaling laws for CTR prediction via unified modeling of compute and model size.
- **Key Innovation:** Scaling law analysis for CTR prediction models.
- **Link:** https://arxiv.org/abs/2602.10811

### 3.4 IDProxy: Cold-Start CTR with Multimodal LLMs at Xiaohongshu

- **Title:** IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors:** Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, et al.
- **Institution:** Xiaohongshu
- **Date:** 2026-03 (Cited by 1)
- **Abstract:** Uses MLLMs to generate proxy embeddings from rich content signals for new items without usage data. Proxies are aligned with existing ID embedding space and optimized end-to-end under CTR objectives. Deployed in Content Feed and Display Ads at Xiaohongshu serving hundreds of millions daily.
- **Key Innovation:** MLLM-generated proxy embeddings for cold-start; end-to-end alignment with ID embedding space.
- **Link:** https://arxiv.org/abs/2603.01590

### 3.5 LLM-HYPER: Generative CTR via LLM-Based Hypernetworks

- **Title:** LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks
- **Authors:** Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, et al.
- **Institution:** E-commerce platform (US)
- **Date:** 2026-04
- **Abstract:** Treats LLMs as hypernetworks to directly generate CTR estimator parameters in a training-free manner. Uses few-shot Chain-of-Thought prompting over multimodal ad content. Retrieves semantically similar past campaigns via CLIP embeddings for demonstrations. +55.9% NDCG@10 over cold-start baselines. Successfully deployed in production.
- **Key Innovation:** LLM-as-hypernetwork for zero-shot CTR parameter generation; CLIP-based demonstration retrieval.
- **Link:** https://arxiv.org/abs/2604.12096

### 3.6 LoopCTR: Loop Scaling for CTR Prediction

- **Title:** Unlocking the Loop Scaling Power for Click-Through Rate Prediction
- **Authors:** Jiakai Tang, Runfeng Zhang, et al.
- **Institution:** Various
- **Date:** 2026-04 (Cited by 1)
- **Abstract:** Introduces LoopCTR, a loop scaling paradigm that increases training-time computation through recursive reuse of shared model components.
- **Key Innovation:** Loop scaling paradigm; recursive computation reuse for training efficiency.
- **Link:** https://arxiv.org/abs/2604.19550

### 3.7 PRECTR-V2: Unified Relevance-CTR Framework

- **Title:** PRECTR-V2: Unified Relevance-CTR Framework with Cross-User Preference Mining, Exposure Bias Correction, and LLM-Distilled Encoder Optimization
- **Authors:** Shuzhi Cao, Rong Chen, Ailong He, et al.
- **Institution:** Various
- **Date:** 2026-02
- **Abstract:** Three contributions: cross-user relevance preference mining for cold-start; exposure bias correction via fake hard negatives with embedding noise injection; lightweight transformer encoder (2M params) distilled from LLM replacing frozen BERT for joint optimization.
- **Key Innovation:** LLM-distilled lightweight encoder for CTR; exposure bias correction via controlled noise.
- **Link:** https://arxiv.org/abs/2602.20676

### 3.8 DAIAN: Deep Adaptive Intent-Aware Network for TIR CTR

- **Title:** DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction in Trigger-Induced Recommendation
- **Authors:** Various
- **Institution:** Xianyu (Alibaba)
- **Date:** 2026-02
- **Abstract:** Addresses intent myopia in Trigger-Induced Recommendation. Extracts user intent as probability distribution over items at varying similarity to trigger. Hybrid enhancer with ID + semantic information. +1.59% CTR, +2.37% bills in online A/B on Xianyu.
- **Key Innovation:** Intent distribution modeling for TIR; addressing intent myopia via multi-similarity-level retrieval.
- **Link:** https://arxiv.org/abs/2602.13971

### 3.9 DS-MLP: Dual-Stream MLP for CTR Prediction

- **Title:** Dual-Stream MLP is All You Need for CTR Prediction
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, et al.
- **Institution:** Renmin University / ByteDance / Meituan
- **Date:** 2026-06
- **Abstract:** Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, with a parallel MLP capturing implicit interactions. Final model is just vanilla MLP achieving SOTA across three benchmarks. Low latency suitable for large-scale deployment.
- **Key Innovation:** KD-based dual-stream MLP achieving SOTA with minimal architecture complexity.
- **Link:** https://arxiv.org/abs/2606.04944

---

## 4. Sequential Modeling & Behavior Modeling

### 4.1 HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequences

- **Title:** HyTRec: A Hybrid Temporal-Aware Attention Architecture for Long Behavior Sequential Recommendation
- **Authors:** Various
- **Institution:** Various
- **Date:** 2026-02
- **Abstract:** Hybrid attention architecture decoupling long-term stable preferences (linear attention) from short-term intent spikes (softmax attention). Temporal-Aware Delta Network (TADN) upweights fresh signals and suppresses historical noise. 7:1 linear-to-standard ratio maintains expressiveness. 8%+ Hit Rate improvement for ultra-long sequences.
- **Key Innovation:** Hybrid linear + softmax attention for long sequences; TADN with exponential gating for temporal dynamics.
- **Link:** https://arxiv.org/abs/2602.18283

### 4.2 Beyond Positive Signals: Implicit Negative Behaviors for CTR

- **Title:** Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Sequential CTR Prediction
- **Authors:** Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Institution:** Various
- **Date:** 2026-06
- **Abstract:** Addresses the underexplored role of implicit negative behaviors in user behavior sequence modeling for CTR prediction.
- **Key Innovation:** Modeling implicit negative signals alongside positive behavior sequences.
- **Link:** https://arxiv.org/abs/2606.15252

### 4.3 FatsMB: Latent Preference Diffusion for Multi-Behavior Sequential Recommendation

- **Title:** From Agnostic to Specific: Latent Preference Diffusion for Multi-Behavior Sequential Recommendation
- **Authors:** Various
- **Institution:** Various (KDD 2026)
- **Date:** 2026-02
- **Abstract:** Uses latent diffusion model to transfer preferences from behavior-agnostic to behavior-specific in latent space. Multi-Behavior AutoEncoder with Behavior-aware RoPE (BaRoPE) constructs unified latent preference space. Multi-Condition Guided Layer Normalization (MCGLN) for denoising.
- **Key Innovation:** First application of latent diffusion in multi-behavior sequential recommendation; BaRoPE for multi-behavior fusion.
- **Link:** https://arxiv.org/abs/2602.23132

### 4.4 HyFormer: Sequence Modeling and Feature Interaction in CTR

- **Title:** HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction
- **Authors:** Yunwen Huang, Shiyong Hong, et al.
- **Institution:** Various
- **Date:** 2026-01 (Cited by 16)
- **Abstract:** Revisits the roles of sequence modeling versus feature interaction in CTR prediction with a hybrid architecture.
- **Key Innovation:** Systematic re-examination of sequence vs. interaction modeling trade-offs.
- **Link:** https://arxiv.org/abs/2601.12681

### 4.5 SRPFN: One Sequential Model Pretrained from Synthetic Priors

- **Title:** One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets
- **Authors:** Woosung Kang, Jiwon Jeong, et al.
- **Institution:** KAIST (KDD 2026)
- **Date:** 2026-06
- **Abstract:** Prior-data Fitted Network for sequential recommendation — predicts next item in a single forward pass without gradient updates on target domain. Pretrained on 25.6M sequences from synthetic prior (hierarchical degree-corrected stochastic block model). Average +7.53% improvement over second-best method across 5 benchmarks.
- **Key Innovation:** Training-free sequential recommendation via synthetic prior pretraining; single forward pass inference.
- **Link:** https://arxiv.org/abs/2606.15752

### 4.6 ManCAR: Manifold-Constrained Adaptive Reasoning for Sequential Rec

- **Title:** ManCAR: Manifold-Constrained Latent Reasoning with Adaptive Test-Time Computation for Sequential Recommendation
- **Authors:** Various
- **Institution:** Various
- **Date:** 2026-02
- **Abstract:** Grounds latent multi-step reasoning within the topology of a global interaction graph. Constructs local intent prior from collaborative neighborhood; progressive alignment forces reasoning trajectory within valid manifold. Adaptive test-time stopping when distribution stabilizes. Up to 46.88% relative improvement in NDCG@10.
- **Key Innovation:** Manifold constraint on latent reasoning via collaborative graph; convergence-based adaptive stopping.
- **Link:** https://arxiv.org/abs/2602.20093

### 4.7 HORIZON: Benchmark for In-the-wild User Behaviour Modeling

- **Title:** HORIZON: A Benchmark for In-the-wild User Behaviour Modeling
- **Authors:** Arnav Goel, Pranjal A. Chitale, et al.
- **Institution:** Microsoft Research India
- **Date:** 2026-04 (Cited by 1)
- **Abstract:** Benchmark covering 54M users and 35M items for pretraining and realistic evaluation of behavior models in heterogeneous environments.
- **Key Innovation:** Large-scale benchmark for real-world heterogeneous user behavior modeling.
- **Link:** https://arxiv.org/abs/2604.17259

---

## 5. Games & Reinforcement Learning

### 5.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games

- **Title:** Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors:** Various
- **Institution:** Various
- **Date:** 2026-05
- **Abstract:** Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Adapted PPO with lightweight turn-level critic substantially improves training stability. Pretrained VLMs provide strong action priors improving sample efficiency. Odysseus achieves 3x+ average game progress vs frontier models. Agents exhibit in-game and cross-game generalization.
- **Key Innovation:** Turn-level critic for VLM RL training; SFT + multi-task RL pipeline for 100+ turn decision-making; open training framework.
- **Link:** https://arxiv.org/abs/2605.00347

### 5.2 Discovering Multiagent Learning Algorithms with LLMs

- **Title:** Discovering Multiagent Learning Algorithms with Large Language Models
- **Authors:** Zun Li, John Schultz, Daniel Hennes, Marc Lanctot
- **Institution:** DeepMind
- **Date:** 2026-02
- **Abstract:** Uses AlphaEvolve (LLM-powered evolutionary coding agent) to automatically discover MARL algorithms. Evolves VAD-CFR (Volatility-Adaptive Discounted CFR) with non-intuitive mechanisms outperforming SOTA. Evolves SHOR-PSRO (Smoothed Hybrid Optimistic Regret PSRO) with hybrid meta-solver for population-based training.
- **Key Innovation:** LLM-powered automated discovery of MARL algorithms; non-intuitive algorithmic mechanisms evolved via LLMs.
- **Link:** https://arxiv.org/abs/2602.16928

### 5.3 From Trainee to Trainer: LLM-Designed Training Environments for RL

- **Title:** From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning
- **Authors:** Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo
- **Institution:** HKUST (GZ) / University of Cambridge
- **Date:** 2026-06
- **Abstract:** LLM-as-Environment Engineer framework where the policy model analyzes failure trajectories and proposes environment configuration modifications. Introduces MAPF-FrozenLake controllable testbed. Qwen3-4B under this framework outperforms larger proprietary LLMs (GPT-5.4, Gemini-3.1-Pro) as environment designers.
- **Key Innovation:** LLM-designed training environments for self-improving RL; environment redesign driven by failure evidence.
- **Link:** https://arxiv.org/abs/2606.17682

### 5.4 Augmenting Game AI with Deep Reinforcement Learning (Survey)

- **Title:** Augmenting Game AI with Deep Reinforcement Learning
- **Authors:** Alessandro Sestini, Joakim Bergdahl, et al.
- **Institution:** Various
- **Date:** 2026-06
- **Abstract:** Survey envisioning applications of RL for game AI with examples of games with different mechanics.
- **Key Innovation:** Comprehensive survey of deep RL applications to game AI.
- **Link:** https://arxiv.org/abs/2606.20210

### 5.5 GIFT: Games as Informal Training for Generalizable LLMs

- **Title:** GIFT: Games as Informal Training for Generalizable LLMs
- **Authors:** Various
- **Institution:** Various
- **Date:** 2026-01
- **Abstract:** Proposes treating games as a primary environment for LLM informal learning, leveraging intrinsic reward signals and structured environments.
- **Key Innovation:** Games as structured training environments for LLM generalization.
- **Link:** https://arxiv.org/abs/2601.05633

### 5.6 AGI Maze: Benchmark for World-Modeling Agents

- **Title:** AGI Maze as a Benchmark Framework for World-Modeling Agents
- **Authors:** Alexey Potapov et al.
- **Institution:** Various
- **Date:** 2026-07
- **Abstract:** Lightweight grid-based maze framework for building environments requiring persistent world state representations. Shows vanilla LLMs fail to represent mazes internally; even working memory improvements are insufficient.
- **Key Innovation:** Minimal benchmark for testing world-modeling capability of LLM agents.
- **Link:** https://arxiv.org/abs/2607.00627

---

## Summary of Key Trends (July 2026)

1. **Generative Recommendation is production-deployed:** UniRec (Shopee), GRAB (Baidu), AgentX (Kuaishou), JD GenRec — all reporting significant online gains.
2. **LLMs as hypernetworks/proxies:** LLM-HYPER and IDProxy show LLMs can generate model parameters or embeddings for cold-start CTR.
3. **Hybrid attention dominates long sequences:** HyTRec, MSA, and HyFormer all explore hybrid sparse/linear/dense attention for efficiency.
4. **RL + LLMs in games is scaling:** Odysseus demonstrates VLM RL training at 100+ turns; LLMs are now designing RL training environments (Trainee-to-Trainer).
5. **Multi-agent + LLMs for algorithm discovery:** AlphaEvolve discovers novel MARL algorithms with non-intuitive mechanisms.
6. **Training-free / zero-shot is emerging:** SRPFN (sequential rec) and LLM-HYPER (CTR) both achieve strong results without target-domain training.
7. **Latent diffusion enters recsys:** FatsMB applies latent diffusion for multi-behavior preference transfer.
