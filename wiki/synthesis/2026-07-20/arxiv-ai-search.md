---
title: Recent arXiv Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games
type: synthesis
created: 2026-07-20
updated: 2026-07-20
sources: []
tags: [arxiv, llm, recommendation, ctr, advertising, sequential-modeling, games, reinforcement-learning]
---

# Recent arXiv Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Generated: 2026-07-20. Papers sourced from arXiv across cs.CL, cs.AI, cs.LG, cs.IR topics.

---

## 1. LLM Reasoning & Architecture

### Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models

- **Authors**: Patrik Wolf, Thomas Kleine Buening, Andreas Krause, Celestine Mendler-Dünner
- **Institution**: ETH Zurich
- **Date**: 2026-07-16
- **Abstract**: Investigates whether LLM in-context learning estimates satisfy basic probabilistic identities, specifically the law of total probability. Uses binary trees as evaluation scaffold to recursively partition populations and aggregate LLM estimates. Finds widespread violations of self-consistency properties. Discovers the "macro fallacy": fine-grained subpopulation responses are often better aligned with human data than direct population-level estimates. Establishes statistical self-consistency as a new, reference-free LLM evaluation criterion.
- **Key Innovation**: Reveals that LLMs possess relevant subpopulation knowledge but fail to propagate it into aggregate estimates; proposes self-consistency as an unsaturated evaluation criterion.
- **arXiv**: https://arxiv.org/abs/2607.15277

### In-Place Tokenizer Expansion for Pre-trained LLMs

- **Authors**: Jimmy Smith et al.
- **Institution**: Liquid AI
- **Date**: 2026-07-16
- **Abstract**: Presents a recipe for upgrading a pre-trained model's tokenizer in-place by continuing BPE merges on a multilingual corpus. New tokens have exact decomposition into source tokens; carried-over embedding rows are unchanged; new rows initialized as mean of sub-token embeddings. Two-stage adaptation (embedding-only then full-model continued pre-training) recovers source quality. Applied to LFM2-8B-A1B to produce LFM2.5-8B-A1B with 128K tokenizer, achieving ~2.2–3.7× per-character decode speedup for Hindi/Vietnamese/Thai.
- **Key Innovation**: Practical tokenizer expansion recipe that preserves source model quality while dramatically improving multilingual efficiency on compact models.
- **arXiv**: https://arxiv.org/abs/2607.15232

### MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

- **Authors**: Ruilin Tong et al.
- **Date**: 2026-07-08
- **Abstract**: Proposes a framework that dynamically expands step-wise memory with correctness-optimized memory composition for test-time LLM reasoning. Maintains modular memory units with asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head. Enables coarse-to-fine retrieval for reasoning.
- **Key Innovation**: Modular instruction memory with learnable selection that adapts incrementally at test time without requiring fixed action spaces or large-scale training data.
- **arXiv**: https://arxiv.org/abs/2607.06974

### Belief-Reality Separation in Language Models

- **Authors**: Oliver Steele et al.
- **Date**: 2026-07-11
- **Abstract**: Shows that LLMs separate a character's beliefs from reality through two mechanisms: a generic value slot that binds the attributed value, and a router at the query position that selects which frame (belief or reality) a query reads out. Two routes fill the slot: asserted beliefs bind directly; derived beliefs arrive via visibility-gated lookback. Holds across three architectures; behavior emerges between 3B–7B across five model families.
- **Key Innovation**: Identifies the precise computational mechanism (slot + router) for belief-reality separation in LLMs; shows same format is shared across counterfactual, fictional, and temporal contexts.
- **arXiv**: https://arxiv.org/abs/2607.11945

### Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion

- **Authors**: Marianne Arriola et al.
- **Date**: 2026-07-02 | **Venue**: ICML 2026
- **Abstract**: Introduces a new class of language models — set diffusion — with a likelihood parameterization factorizing over flexible-position, flexible-length token sets and a set-causal diffusion architecture supporting KV cache updates after every inference step. Tokens decoded in arbitrarily-ordered sets (including sliding-window) enable faster inference. Achieves better speed-quality tradeoffs on mathematical reasoning, summarization, and unconditional generation compared to prior diffusion LM approaches.
- **Key Innovation**: First diffusion language model supporting arbitrary-order decoding with KV caching, bridging autoregression and diffusion in a unified framework.
- **arXiv**: https://arxiv.org/abs/2607.01775

### Nemotron-Labs-Diffusion: A Tri-Mode Language Model

- **Institution**: NVIDIA
- **Date**: 2026-07-07
- **Abstract**: A tri-mode LM unifying AR, diffusion, and self-speculation decoding in a single architecture. Trained with joint AR-diffusion objective. In self-speculation mode, diffusion drafts while AR verifies, outperforming MTP methods. Scales to 3B, 8B, 14B parameters. Nemotron-Labs-Diffusion-8B decodes 6× more tokens per forward than Qwen3-8B with comparable accuracy.
- **Key Innovation**: Tri-mode architecture; diffusion improves lookahead planning while AR provides linguistic priors; 4× higher throughput on SPEED-Bench.
- **arXiv**: https://arxiv.org/abs/2607.05722

### Scalable Visual Pretraining for Language Intelligence

- **Authors**: Yiming Zhang, Zhonghan Zhao, Wenwei Zhang et al.
- **Institution**: Shanghai AI Laboratory, USTC, Zhejiang University, SJTU
- **Date**: 2026-07-13
- **Abstract**: Challenges the default assumption that LMs must be trained on text-only representations. Introduces Visual Pretraining (VP) framework that trains a foundation model to predict document patches in latent space directly from raw documents. VP outperforms text pretraining under matched corpora while consuming only 25% of the token budget. Improves scientific reasoning up to 2.0× on certain benchmarks.
- **Key Innovation**: Visual pretraining on native scientific documents (equations, figures, layouts) as a scalable, efficient alternative to text-only pretraining.
- **arXiv**: https://arxiv.org/abs/2607.09657

---

## 2. CTR Prediction

### Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)

- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University, ByteDance, Meituan
- **Date**: 2026 (ACM TKDD)
- **Abstract**: Proposes DS-MLP, a dual-stream MLP framework using knowledge distillation to consolidate explicit feature interactions into a main MLP while a parallel MLP captures implicit interactions. Two alignment strategies optimize compatibility. Achieves SOTA on Criteo, Avazu, MovieLens with low inference latency comparable to vanilla MLP.
- **Key Innovation**: Proves that a simple vanilla MLP (final model) can match/exceed complex CTR models via distillation-based dual-stream training; highly scalable for production.
- **arXiv**: https://arxiv.org/abs/2606.04944

### SparseCTR: Efficient Scaling Laws in CTR Prediction

- **Authors**: Wei Lai et al.
- **Date**: 2026-04 (WWW '26)
- **Abstract**: Proposes SparseCTR for modeling long-term user behaviors with three-branch sparse self-attention (global interests, interest transitions, short-term interests). Introduces TimeChunking for personalized behavior sequence segmentation and composite relative temporal encoding. Exhibits clear scaling law across three orders of magnitude in FLOPs. Online A/B test: +1.72% CTR, +1.41% CPM.
- **Key Innovation**: First CTR model demonstrating clear scaling law behavior; efficient sparse attention for user behaviors with temporal structure.
- **arXiv**: https://arxiv.org/abs/2601.17836

### EST: Efficiently Scalable Transformer for CTR Prediction

- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan et al.
- **Institution**: Alibaba (Taobao)
- **Date**: 2026-02
- **Abstract**: Addresses LLM-inspired scaling laws for industrial CTR under latency constraints. Identifies asymmetry in information density between behavioral/non-behavioral features and content signals as relational priors. Proposes Lightweight Cross Attention (LCA) and Content Sparse Attention (CSA) for fully unified modeling. Exhibits stable power-law scaling. Deployed on Taobao display ads: +3.27% RPM, +1.22% CTR.
- **Key Innovation**: Fully unified CTR modeling without lossy aggregation; domain-specific transformer design leveraging information density asymmetry.
- **arXiv**: https://arxiv.org/abs/2602.10811

### GenCI: Generative Modeling of User Interest Shift for CTR Prediction

- **Authors**: (multiple)
- **Date**: 2026 (WWW '26)
- **Abstract**: Proposes a generative user intent framework using semantic interest cohorts. A generative model produces candidate interest cohorts via next-item prediction; a hierarchical candidate-aware network injects contextual signal into ranking via cross-attention. End-to-end joint optimization with self-supervised regularization. Evaluated on MovieLens, Amazon Fashion, Musical Instruments.
- **Key Innovation**: Bridges recall-ranking gap by generating semantic interest cohorts as dynamic contextual signals for ranking; generative paradigm for user intent modeling.
- **arXiv**: https://arxiv.org/abs/2601.18251

### GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu

- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren et al.
- **Institution**: Baidu
- **Date**: 2026-02
- **Abstract**: End-to-end generative framework for CTR with Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics and action signals. Full-scale deployment at Baidu: +3.05% revenue, +3.49% CTR. Model shows monotonic, approximately-linear AUC improvement with longer interaction sequences (scaling behavior).
- **Key Innovation**: Sequence-first paradigm for industrial CTR; demonstrates scaling laws in production advertising; CamA mechanism for action-aware temporal modeling.
- **arXiv**: https://arxiv.org/abs/2602.01865

### IDProxy: Cold-Start CTR at Xiaohongshu with Multimodal LLMs

- **Institution**: Xiaohongshu (Little Red Book)
- **Date**: 2026-03
- **Abstract**: Uses multimodal LLMs to generate proxy embeddings from rich content signals for cold-start CTR prediction. Proxies aligned with existing ID embedding space and optimized end-to-end. Deployed in Content Feed and Display Ads serving hundreds of millions daily.
- **Key Innovation**: MLLM-generated proxy embeddings that seamlessly integrate into existing large-scale ranking pipelines for cold-start items.
- **arXiv**: https://arxiv.org/abs/2603.01590

---

## 3. Recommendation Systems — Sequential & Generative

### CMSL: Constructive Multi-Sequence Learning (Meta)

- **Authors**: Meta AI
- **Date**: 2026-07-10
- **Abstract**: Addresses context pollution in long heterogeneous user histories by actively constructing multiple coherent latent sequences from raw interactions. Learnable Sequence Construction Module disentangles history into thematic strands; linear attention models each strand efficiently. Deployed across ranking/retrieval on four major surfaces at Meta.
- **Key Innovation**: Active "context engineering" in latent space — disentangling noisy user history into multiple coherent sequences to reduce cross-intent interference.
- **arXiv**: https://arxiv.org/abs/2606.28533

### UniRec: Bridging Generative and Discriminative Recommendation (Shopee)

- **Date**: 2026
- **Abstract**: Proves via Bayes' theorem that the generative-discriminative performance gap arises from feature coverage, not fundamental asymmetry. Proposes Chain-of-Attribute (CoA) for a speculate-then-refine paradigm; Capacity-constrained SID for exposure-weighted residual quantization; Task-Conditioned BOS for multi-scenario decoding. Deployed on Shopee: +5.37% PVCTR, +4.76% orders, +5.60% GMV.
- **Key Innovation**: Theoretical grounding that reframes generative vs. discriminative debate; end-to-end framework achieving significant e-commerce gains.
- **arXiv**: https://arxiv.org/abs/2604.12234

### GenRec: Preference-Oriented Generative Framework at JD App

- **Institution**: JD.com
- **Date**: 2026-04
- **Abstract**: Addresses scaling generative retrieval to industrial systems. Proposes Page-wise NTP for denser gradient signal; asymmetric linear Token Merger compresses multi-token Semantic IDs (~2× input length reduction); GRPO-SR (RL with NLL regularization) with hybrid rewards. Month-long A/B tests: +9.5% clicks, +8.7% transactions.
- **Key Innovation**: Practical solutions for scaling GR in production — page-wise training, token merging, and RL alignment for generative recommendation.
- **arXiv**: https://arxiv.org/abs/2604.14878

### RecRec: Recursive Recommendation

- **Date**: 2026-07
- **Abstract**: Models user preferences as recursively refined latent states. Two variants: (1) Lightweight model with evidence-anchored correction mechanism (3.9M–14M parameters, matches/outperforms 7B LLM-based recommenders); (2) Dual-state framework decoupling reasoning from prediction, predicting from R latent interests. Deep supervision allows free adjustment of reasoning depth at inference.
- **Key Innovation**: Recursive latent inference as scalable alternative to deeper/LM-based architectures; evidence-anchored correction prevents semantic drift.
- **arXiv**: https://arxiv.org/abs/2607.10541 / https://arxiv.org/abs/2607.12945

### ManCAR: Manifold-Constrained Adaptive Reasoning for Sequential Rec

- **Date**: 2026-02
- **Abstract**: Grounds latent reasoning within the topology of a global interaction graph. Constructs local intent prior from collaborative neighborhood as distribution over item simplex. Progressive alignment forces reasoning trajectory to remain within valid manifold. Adaptive test-time stopping when distribution stabilizes. Up to 46.88% relative improvement in NDCG@10.
- **Key Innovation**: Graph-topology constraints on latent reasoning to prevent drift; variational interpretation; convergence-based adaptive stopping.
- **arXiv**: https://arxiv.org/abs/2602.20093

### TokenFormer: Unifying Multi-Field and Sequential Recommendation (Tencent)

- **Institution**: Tencent
- **Date**: 2026-04
- **Abstract**: Discovers Sequential Collapse Propagation (SCP) when naively unifying feature-interaction and sequential models. Proposes Bottom-Full-Top-Sliding (BFTS) attention and Non-Linear Interaction Representation (NLIR). Deployed on Tencent's advertising platform with SOTA performance.
- **Key Innovation**: Identifies and solves a fundamental failure mode (SCP) in unified recommendation architectures.
- **arXiv**: https://arxiv.org/abs/2604.13737

### GenAIR: Generative Archetype-Grounded Item Representations

- **Date**: 2026-04
- **Abstract**: Uses LLM to infer Archetype descriptions representing ideal target audiences of items, then calibrates embeddings with behavioral signals. Bridges semantic-behavioral gap in item representations. Compatible with most existing sequential models.
- **Key Innovation**: LLM-inferred archetypes + behavioral calibration for item representations that bridge semantic and collaborative spaces.
- **arXiv**: https://arxiv.org/abs/2606.11023

---

## 4. Advertising & Bidding

### DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation

- **Authors**: Zhihao Lv, Longtao Zhang et al.
- **Date**: 2026-02
- **Abstract**: Addresses intent myopia in trigger-induced recommendation (TIR) — where systems overemphasize trigger items at the expense of diversity. Extracts personalized intent representations, retrieves related historical behaviors, and uses hybrid enhancer with ID + semantic information. Deployed on Xianyu (Alibaba): +1.59% CTR, +1.73% diversity, +2.37% bills in online A/B.
- **Key Innovation**: Solves intent myopia in TIR through adaptive intent distribution modeling and hybrid ID-semantic similarity enhancement.
- **arXiv**: https://arxiv.org/abs/2602.13971

### Constrained Auto-Bidding via Generative Response Modeling

- **Authors**: Eunseok Yang, Xingdong Zuo, Kyung-Min Kim
- **Date**: 2026-05
- **Abstract**: Proposes Generative Response Model (GRM) that predicts future traffic volume and horizon-aggregate cost/value curves as functions of a bid multiplier. Lightweight analytic controller enforces constraints via 1D root-finding. Proven optimality bounds relative to full per-tick control.
- **Key Innovation**: Shifts learning target from actions to responses; analytic controller for constraint enforcement with theoretical guarantees.
- **arXiv**: https://arxiv.org/abs/2605.27811

### Knowledge-informed Bidding with Dual-process Control (KBD)

- **Authors**: Huixiang Luo et al.
- **Date**: 2026-03
- **Abstract**: Embeds human expertise as inductive biases via informed machine learning. Uses Decision Transformer for global multi-step bidding optimization. Dual-process control combines fast rule-based PID (System 1) with DT (System 2).
- **Key Innovation**: Dual-process cognitive framework for bid optimization combining human expertise, Transformer-based sequence optimization, and PID control.
- **arXiv**: https://arxiv.org/abs/2603.04920

---

## 5. Games & Reinforcement Learning

### Augmenting Game AI with Deep Reinforcement Learning

- **Authors**: Alessandro Sestini, Joakim Bergdahl et al. (EA)
- **Date**: 2026-06
- **Abstract**: Vision paper presenting RL-augmented game AI in AAA games (EA SPORTS FC 25, Battlefield 6). Proposes framework for training RL models with game-development requirements. Demonstrates RL goalkeeper AI positioning and infantry movement. Identifies bottlenecks: low data collection rate in game engines, controllability, integration workflows.
- **Key Innovation**: Practical framework for deploying RL in production AAA game environments; identifies and addresses real-world engineering constraints.
- **arXiv**: https://arxiv.org/abs/2606.20210

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents

- **Date**: 2026-03
- **Abstract**: LLM agent for ARC-AGI-3 game-playing with two-player architecture (perception/action separation), curriculum-based learning via state machine, and database-as-control-plane. v2 achieves 50–94× greater sample efficiency than comparable systems (32 interactions vs. 1,600–3,000). Diagnoses failure as self-consistent hallucination cascade in perception layer.
- **Key Innovation**: Structured test-time learning paradigm with curriculum, state machine, and programmable context for LLM agents.
- **arXiv**: https://arxiv.org/abs/2603.17683

### G1: Bootstrapping Perception and Reasoning via RL

- **Institution**: (multiple, including Tsinghua)
- **Date**: 2025-05
- **Abstract**: Introduces VLM-Gym for scalable multi-game parallel training of VLMs. G0 (pure RL) shows emergent perception and reasoning; G1 (perception-enhanced cold start + KD from teacher) surpasses Claude-3.7-Sonnet-Thinking across all games. Discovers perception and reasoning mutually bootstrap each other during RL.
- **Key Innovation**: Demonstrates RL-driven emergence of perception+reasoning in VLMs; perception-reasoning co-evolution finding.
- **arXiv**: https://arxiv.org/abs/2505.13426

### SPyCE: Skill-Policy Co-evolution for Multimodal Agents

- **Date**: 2026-07
- **Abstract**: Distills reasoning trajectories into hierarchical skill library (execution + workflow skills) that co-evolves with the policy during RL. Policy conditions on retrieved skills for rollouts; high-quality rollouts refresh skills via merge-or-add rule. Outperforms RL-based and memory-based baselines across eight benchmarks.
- **Key Innovation**: Closed-loop skill-policy co-evolution; hierarchical skill abstraction (local operations + global workflow priors).
- **arXiv**: https://arxiv.org/abs/2607.13854

### Seed: Self-Evolving On-Policy Distillation for Agentic RL

- **Date**: 2026-07
- **Abstract**: Converts completed on-policy trajectories into hindsight skills (natural-language reusable workflows) and distills behavioral effects back into the policy via token-level on-policy distillation signal. Jointly optimized with outcome-based RL. Superior performance on embodied interaction, web navigation, search-based QA.
- **Key Innovation**: Self-evolving loop where the same policy model serves as both trajectory collector and skill analyst; dense hindsight supervision for sparse-reward agentic RL.
- **arXiv**: https://arxiv.org/abs/2607.14777

### Reward-Free Evolving Agents via Pairwise Validator

- **Date**: 2026-07-15
- **Abstract**: Replaces scalar reward in self-evolving agentic loops with a pairwise validator (frozen LLM comparing parent vs. child candidates). Integrates into three self-evolving engines (GEPA, ADRS, ShinkaEvolve). Matches/exceeds full-reward baselines without labeling cost.
- **Key Innovation**: Drop-in pairwise judgment replacement for per-step reward design; eliminates domain-specific reward engineering.
- **arXiv**: https://arxiv.org/abs/2607.14408

---

## Summary of Trends

| Theme | Key Trend | Representative Papers |
|-------|-----------|----------------------|
| **LLM Decoding** | AR + Diffusion unification; set-based token generation | Set Diffusion, Nemotron-Diffusion |
| **LLM Reasoning** | Self-consistency, modular memory, belief tracking | PPA, MILES, Belief-Reality |
| **LLM Multilingual** | In-place tokenizer expansion for edge models | Tokenizer Expansion |
| **CTR Scaling** | Power-law scaling laws in CTR models | EST, SparseCTR, GRAB |
| **CTR Architecture** | Simpler is better (MLP-based, dual-stream) | DS-MLP |
| **CTR Cold-Start** | MLLM-generated proxy embeddings | IDProxy |
| **Generative Rec** | GR scaling to production; page-wise NTP; RL alignment | GenRec, UniRec |
| **Sequential Rec** | Multi-sequence disentanglement; recursive reasoning | CMSL, RecRec, ManCAR |
| **Unified Rec** | Bridging feature-interaction and sequential paradigms | TokenFormer |
| **Advertising** | Intent modeling in TIR; generative bidding control | DAIAN, GRM, KBD |
| **Game AI** | RL in AAA production; curriculum test-time learning | EA Game AI, Sensi |
| **VLM Agents** | RL-driven perception-reasoning emergence; skill co-evolution | G1, SPyCE, Seed |
