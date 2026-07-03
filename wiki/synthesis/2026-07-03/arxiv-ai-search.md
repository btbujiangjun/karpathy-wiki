---
title: "arXiv AI Research Roundup — July 2026"
type: synthesis
created: 2026-07-03
updated: 2026-07-03
sources: []
tags: [arxiv, survey, llm, ctr, recommendation, games, reinforcement-learning, transformers]
---

# arXiv AI Research Roundup — July 2026

A curated survey of recent arXiv preprints (2025–2026) across AI, LLMs, recommendation, advertising, CTR prediction, games, and reinforcement learning.

---

## 1. LLM Architecture & Reasoning

### 1.1 From Memorization to Creativity: LLM as a Designer of Novel Neural Architectures
- **Link:** [2601.02997](https://arxiv.org/abs/2601.02997)
- **Authors:** Waleed Khalid, Dmitry Ignatov, Radu Timofte
- **Institution:** Computer Vision Lab (implied)
- **Date:** Jan 2026
- **Abstract:** Closed-loop architecture synthesis pipeline within the NNGPT framework. A code-oriented LLM evolves over 22 supervised fine-tuning cycles, synthesizing PyTorch convolutional networks validated via low-fidelity performance signals and filtered via MinHash–Jaccard to prevent structural redundancy. On CIFAR-10, valid generation rate stabilizes at 50.6%, mean first-epoch accuracy rises from 28.1% to 51.0%.
- **Key Innovations:** LLM-driven neural architecture search; iterative self-supervised fine-tuning as a task-specialized architectural prior; novelty filtering with MinHash–Jaccard.

### 1.2 Large Language Model Reasoning Failures
- **Link:** [2602.06176](https://arxiv.org/abs/2602.06176)
- **Authors:** Peiyang Song, Pengrui Han, Noah Goodman
- **Institution:** Stanford University
- **Date:** Feb 2026 (TMLR 2026)
- **Abstract:** First comprehensive survey dedicated to reasoning failures in LLMs. Novel categorization framework distinguishing embodied vs. non-embodied reasoning, with further subdivision into informal (intuitive) and formal (logical) reasoning. Covers fundamental failures intrinsic to LLM architectures, application-specific limitations, and robustness issues.
- **Key Innovations:** Taxonomy of reasoning failures; comprehensive survey with structured categorization.

### 1.3 Challenges and Research Directions for Large Language Model Inference Hardware
- **Link:** [2601.05047](https://arxiv.org/abs/2601.05047)
- **Authors:** Xiaoyu Ma, David Patterson
- **Institution:** UC Berkeley
- **Date:** Jan 2026 (IEEE Computer 2026)
- **Abstract:** LLM inference faces memory/interconnect bottlenecks rather than compute. Highlights four architecture research opportunities: High Bandwidth Flash, Processing-Near-Memory, 3D memory-logic stacking, and low-latency interconnect.
- **Key Innovations:** Hardware-level analysis of LLM inference bottlenecks; datacenter and mobile perspectives.

### 1.4 LT2: Linear-Time Looped Transformers
- **Link:** [2605.20670](https://arxiv.org/abs/2605.20670)
- **Authors:** (Multiple, see paper)
- **Date:** May 2026
- **Abstract:** Replaces quadratic softmax attention with subquadratic token-mixing primitives (linear attention and sparse attention) in looped transformer architectures. LT2-linear and LT2-sparse variants match or outperform similarly sized industry-level models.
- **Key Innovations:** Linear-time looped transformers; subquadratic attention for weight-shared recurrence; parameter-efficient reasoning.

### 1.5 Loop as a Bridge: Can Looped Transformers Truly Link Representation Space and Natural Language Outputs?
- **Link:** [2601.10242](https://arxiv.org/abs/2601.10242)
- **Authors:** Guanxu Chen, Dongrui Liu, Jing Shao
- **Date:** Jan 2026
- **Abstract:** Investigates whether looped transformers (LTs) can bridge the gap between internal knowledge and explicit linguistic outputs. Increasing loop iterations narrows the gap but partly due to degradation of internal knowledge.
- **Key Innovations:** Empirical analysis of looped transformer introspection limitations.

### 1.6 Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers
- **Link:** [2603.07670](https://arxiv.org/abs/2603.07670)
- **Authors:** Pengfei Du
- **Institution:** Hong Kong Research Institute of Technology
- **Date:** Mar 2026
- **Abstract:** Comprehensive survey on memory design in LLM-based agents. Formalizes agent memory as a write–manage–read loop. Covers context-resident compression, retrieval-augmented stores, reflective self-improvement, hierarchical virtual context, and policy-learned management.
- **Key Innovations:** Three-dimensional taxonomy for agent memory (temporal scope, representational substrate, control policy); five mechanism families examined in depth.

---

## 2. CTR Prediction & Recommendation Systems

### 2.1 CADET: Context-Conditioned Ads Decoder-Only Transformer for CTR Prediction
- **Link:** [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors:** Ruoyan Wang et al. (LinkedIn team)
- **Institution:** LinkedIn
- **Date:** Feb 2026
- **Abstract:** End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Treats CTR prediction as a generation problem rather than classification. Achieves +2.04% CTR lift vs. production LiRank (hybrid DCNv2 + sequential encoders). Serves main traffic for LinkedIn homefeed sponsored updates.
- **Key Innovations:** First decoder-only transformer for ads CTR at scale; handles post-scoring contextual signals; maintains offline-online consistency at industrial scale.

### 2.2 GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm
- **Link:** [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors:** Shaopeng Chen et al.
- **Institution:** Baidu Inc.
- **Date:** Feb 2026
- **Abstract:** Generative Ranking for Ads at Baidu (GRAB) — an end-to-end generative framework for CTR prediction. Integrates Causal Action-aware Multi-channel Attention (CamA). Full-scale online deployment delivers +3.05% revenue and +3.49% CTR lift. Demonstrates monotonic linear improvement with longer interaction sequences.
- **Key Innovations:** LLM-inspired sequence-first paradigm for CTR; CamA attention mechanism; scaling law behavior in recommendation.

### 2.3 LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction
- **Link:** [2604.19550](https://arxiv.org/abs/2604.19550)
- **Authors:** Jiakai Tang, Runfeng Zhang et al.
- **Institution:** Renmin University of China & Alibaba Group
- **Date:** Apr 2026
- **Abstract:** Introduces loop scaling — increases training-time computation through recursive reuse of shared model layers, decoupling computation from parameter growth. Sandwich architecture with Hyper-Connected Residuals and Mixture-of-Experts. "Train-multi-loop, infer-zero-loop" strategy where a single forward pass outperforms all baselines.
- **Key Innovations:** Loop scaling paradigm for CTR; recursive layer reuse; 0.02–0.04 AUC headroom for adaptive inference.

### 2.4 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Link:** [2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors:** Guillaume Salha-Galvan et al.
- **Institution:** Xiaohongshu (小红书)
- **Date:** Mar 2026
- **Abstract:** Leverages multimodal LLMs to generate proxy embeddings from rich content signals for cold-start CTR prediction. Proxies are aligned with existing ID embedding space and optimized end-to-end. Deployed in Content Feed and Display Ads, serving hundreds of millions of users daily.
- **Key Innovations:** MLLM-based proxy embeddings for cold-start CTR; seamless integration with existing large-scale ranking pipelines.

### 2.5 GenLI: Generative Long-term User Interest Modeling for CTR Prediction
- **Link:** [2605.15905](https://arxiv.org/abs/2605.15905)
- **Authors:** Jiangli Shao et al.
- **Date:** May 2026
- **Abstract:** Generative long-term user interest model for CTR. Interest generation module (IGM) produces multiple interest distributions — target-independent, incorporating interaction information among behaviors. Behavior retrieval via O(1) lookup instead of pairwise matching.
- **Key Innovations:** Generative interest modeling; target-independent interest distributions; O(1) behavior retrieval.

### 2.6 FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
- **Link:** [2605.01726](https://arxiv.org/abs/2605.01726)
- **Authors:** Zenan Dai, Jinpeng Wang, Junwei Pan et al.
- **Date:** May 2026
- **Abstract:** Key observation: user attention scores exhibit distinct spectral entropy distributions when conditioned on positive vs. negative target items. True interests manifest as low-entropy concentrated spectral patterns. Proposes target-aware spectrum filtering.
- **Key Innovations:** Frequency-domain analysis for user interest; spectral entropy as interest signal; target-aware spectrum filtering.

### 2.7 Dual-Stream MLP (DS-MLP) for CTR Prediction
- **Link:** To appear (see aimodels.fyi summary)
- **Date:** Jun 2026
- **Abstract:** Dual-stream architecture for explicit and implicit feature interactions. Teacher-agnostic design — any SOTA CTR model can serve as teacher without rewriting the student architecture.
- **Key Innovations:** Teacher-agnostic distillation for CTR; dual-stream MLP.

### 2.8 Generative CTR Prediction with Applications to Search Advertising (GenCTR)
- **Link:** [2507.11246](https://arxiv.org/abs/2507.11246)
- **Authors:** Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao
- **Institution:** (Major e-commerce platform)
- **Date:** Jul 2025
- **Abstract:** Two-stage training: generative pre-training for next-item prediction → fine-tuning within discriminative CTR framework. Conditional self-condition decoder and conditional negative sampling. Deployed at one of the world's largest e-commerce platforms.
- **Key Innovations:** Generative pre-training + discriminative fine-tuning for CTR; deployed at massive scale.

---

## 3. Reinforcement Learning, Games & Self-Play

### 3.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Link:** [2506.24119](https://arxiv.org/abs/2506.24119)
- **Authors:** Bo Liu, Leon Guertler et al.
- **Date:** Jun 2025 (v3 Mar 2026)
- **Abstract:** Self-play framework where models learn by playing multi-turn zero-sum games against continuously improving versions of themselves. Fully online multi-turn multi-agent RL system. Role-conditioned advantage estimation (RAE) stabilizes training. Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama models. Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results.
- **Key Innovations:** Self-play for reasoning without human supervision; role-conditioned advantage estimation; cognitive pattern transfer from games to reasoning.

### 3.2 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Link:** [2605.04906](https://arxiv.org/abs/2605.04906)
- **Authors:** Yidong He, Yutao Lai, Pengxu Yang et al.
- **Institution:** (Multiple Chinese universities)
- **Date:** May 2026
- **Abstract:** RL-based framework improving LLMs' strategic reasoning in multi-agent games. Recursive reasoning paradigm integrating other agents' reasoning processes. Centralized CoT comparison module for reward signal generation. Group-relative RL for policy optimization. 22.1% average improvement across diverse games.
- **Key Innovations:** Recursive multi-agent reasoning; centralized CoT comparison for rewards; hybrid advantage estimation.

### 3.3 MARS: Reinforcing Multi-Agent Reasoning of LLMs through Self-Play in Strategic Games
- **Link:** [2510.15414](https://arxiv.org/abs/2510.15414)
- **Authors:** Huining Yuan et al.
- **Date:** Oct 2025
- **Abstract:** End-to-end RL framework for multi-agent reasoning of LLMs through self-play. Turn-level advantage estimator and agent-specific advantage normalization. Up to 28.7% performance improvements on held-out games. Transfers to reasoning benchmarks: +10.0% on AIME, +12.5% on GPQA-Diamond.
- **Key Innovations:** Turn-level credit assignment; self-play for multi-agent generalization; transfer from games to reasoning.

### 3.4 TriPlay-RL: Tri-Role Self-Play Reinforcement Learning for LLM Safety Alignment
- **Link:** [2601.18292](https://arxiv.org/abs/2601.18292)
- **Date:** Jan 2026
- **Abstract:** Closed-loop RL framework with three roles: attacker (adversarial prompts), defender (safety defense), evaluator (response assessment). Attacker achieves 20-50% improvement in adversarial effectiveness; defender attains 10-30% safety gains without degrading general reasoning.
- **Key Innovations:** Tri-role self-play for safety alignment; continuous co-evolution in unified learning loop.

### 3.5 Augmenting Game AI with Deep Reinforcement Learning
- **Link:** [2606.20210](https://arxiv.org/abs/2606.20210)
- **Authors:** Alessandro Sestini et al.
- **Date:** Jun 2026 (Conference on Games 2026)
- **Abstract:** Vision paper on RL for game AI. Proposes framework with requirements for game AI deployment. Identifies key bottlenecks: sample efficiency, believability vs. optimality tension, generalization.
- **Key Innovations:** Framework for RL-augmented game AI; genre-level readiness analysis.

### 3.6 SeRL: Self-Play Reinforcement Learning for Large Language Models with Limited Data
- **Link:** [2505.20347](https://arxiv.org/abs/2505.20347)
- **Authors:** Wenkai Fang et al.
- **Date:** May 2025 (v2 Jan 2026)
- **Abstract:** Self-play RL bootstrapping LLM training with limited initial data. Self-instruction generates additional instructions with online filtering; self-rewarding uses majority-voting for reward estimation. Matches performance of high-quality data with verifiable rewards.
- **Key Innovations:** Self-instruction + self-rewarding for data-scarce domains; majority-voting reward estimation.

### 3.7 SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models
- **Link:** [2509.23863](https://arxiv.org/abs/2509.23863)
- **Authors:** Ziyi Yang et al.
- **Date:** Sep 2025 (ICLR 2026)
- **Abstract:** Multi-role self-play (questioner, responder, verifier) for long-context reasoning. Automated curriculum increasing document length. Average 7.6-point gain in pass@8 on Qwen3-30B-A3B-Thinking.
- **Key Innovations:** Label-free long-context optimization; multi-role self-play; adaptive difficulty curriculum.

---

## 4. Generative Models, Diffusion & Transformers

### 4.1 Variable-Length Tokenization via Learnable Global Merging for Diffusion Transformers
- **Link:** [2606.20076](https://arxiv.org/abs/2606.20076)
- **Authors:** Dong Hoon Lee, Seunghoon Hong
- **Date:** Jun 2026
- **Abstract:** Variable-length tokenizer that modulates length by merging tokens rather than truncation. Learnable global merging ensures compatibility with diffusion transformers. Addresses cross-length latent distribution shift.
- **Key Innovations:** Learnable global merging for variable-length tokens; cross-length representation alignment.

### 4.2 d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning
- **Link:** [2504.12216](https://arxiv.org/abs/2504.12216)
- **Authors:** Siyan Zhao et al. (UCLA + Meta AI)
- **Date:** Apr 2025
- **Abstract:** First framework applying RL to diffusion LLMs (dLLMs) for reasoning. diffu-GRPO extends GRPO to diffusion models. Demonstrates that dLLMs can benefit from RL-based reasoning improvement.
- **Key Innovations:** RL for diffusion LLMs; diffu-GRPO algorithm.

---

## 5. Summary & Trends

| Area | Key Trend | Representative Works |
|------|-----------|---------------------|
| LLM Architecture | Looped/shared-weight transformers for parameter-efficient compute scaling | LT2, LoopCTR, Loop as a Bridge |
| CTR Prediction | Generative/LLM-inspired paradigms replacing DLRMs | CADET, GRAB, LoopCTR, GenCTR |
| Cold-Start CTR | Multimodal LLM embeddings for cold-start | IDProxy |
| User Interest Modeling | Generative, frequency-domain, target-independent | GenLI, FEDIN |
| Games & RL | Self-play on games transfers to general reasoning | SPIRAL, MARS, Strat-Reasoner |
| Safety Alignment | Multi-role self-play for automated alignment | TriPlay-RL |
| LLM Memory | Structured memory for autonomous agents | Memory for Autonomous LLM Agents |
| Hardware | Memory-bandwidth bottleneck for inference | LLM Inference Hardware (Patterson) |
| Diffusion Models | Variable-length tokenization, RL for dLLMs | VLT, d1 |
