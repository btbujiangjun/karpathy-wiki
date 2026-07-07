---
title: "arXiv AI Research Search — 2026-07-07"
type: synthesis
created: 2026-07-07
updated: 2026-07-07
tags: [arxiv, survey, llm, recommendation, ctr, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Research Search — 2026-07-07

Curated recent papers across AI, LLMs, recommendation, advertising, CTR prediction, sequential modeling, and games.

---

## LLM Architecture & Model Design

### 1. Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: Tri Dao, Albert Gu
- **Institution**: — (ICLR 2026)
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **Abstract**: Introduces three core improvements inspired by SSM discretization: (1) a more expressive recurrence derived from SSM discretization, (2) a complex-valued state update rule for richer state tracking, and (3) a multi-input multi-output (MIMO) formulation for better performance without increasing decode latency. At 1.5B scale, Mamba-3 improves downstream accuracy by 0.6 pp over Gated DeltaNet; MIMO variant adds another 1.2 pp.
- **Key Innovations**: Complex-valued SSM states; MIMO formulation decouples training cost from inference latency; removes short conv from Mamba-1/2; RoPE-based complex rotations replace costly custom kernels.

### 2. MoBA: Mixture of Block Attention for Long-Context LLMs
- **Authors**: Moonshot AI (Kimi team)
- **Institution**: Moonshot AI
- **arXiv**: [2502.13189](https://arxiv.org/abs/2502.13189)
- **Abstract**: Applies Mixture-of-Experts principles to the attention mechanism. The model learns to select which blocks of KV to attend to, enabling seamless transition between full and sparse attention. Deployed in production for Kimi's long-context requests.
- **Key Innovations**: MoE-gated sparse attention with no predefined bias; sparse/full attention toggle without performance degradation.

### 3. Understanding Large Language Models
- **Authors**: Yannik Keller, Thomas Eisenmann
- **Institution**: —
- **arXiv**: [2607.01006](https://arxiv.org/abs/2607.01006)
- **Abstract**: Comprehensive chapter covering Transformer architecture, emergent capabilities (symbolic reasoning, theory of mind, deception), mechanistic interpretability, and the debate on whether LLMs genuinely understand vs. pattern-match. Argues against simplistic reductionist dismissal of AI cognition.
- **Key Innovations**: Survey/synthesis rather than novel method; advocates nuanced position on LLM cognition.

---

## Recommendation Systems

### 4. Deep Research for Recommender Systems (RecPilot)
- **Authors**: Kesha Ou, Chenghao Wu, Xiaolei Wang, Wayne Xin Zhao et al.
- **Institution**: Renmin University
- **arXiv**: [2603.07605](https://arxiv.org/abs/2603.07605)
- **Abstract**: Proposes a paradigm shift from list-based recommendation to deep research reports. RecPilot is a multi-agent framework with a user trajectory simulation agent and a self-evolving report generation agent. Produces comprehensive, user-centric reports instead of item lists.
- **Key Innovations**: Agent-driven recommendation paradigm; proactive exploration + synthesis into natural-language reports.

### 5. Self-Evolving Recommendation System: End-to-End Autonomous Model Optimization with LLM Agents
- **Authors**: Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Institution**: Google (YouTube)
- **arXiv**: [2602.10226](https://arxiv.org/abs/2602.10226)
- **Abstract**: Uses LLMs (Gemini family) to autonomously generate, train, and deploy model changes. Offline Agent (Inner Loop) does high-throughput hypothesis generation with proxy metrics; Online Agent (Outer Loop) validates against live business metrics. Multiple successful production launches at YouTube.
- **Key Innovations**: LLM-driven MLE agents that discover novel optimizers, architectures, and reward functions; dual-loop design with proxy → north star validation.

### 6. Efficient Sequential Recommendation for Long Term User Interest via Personalization (PerSRec)
- **Authors**: Qiang Zhang et al. (Meta/Facebook)
- **Institution**: Meta
- **arXiv**: [2601.03479](https://arxiv.org/abs/2601.03479) (ICDM 2025)
- **Abstract**: Compresses long user interaction histories into learnable tokens combined with recent interactions. Significantly reduces O(n²) cost of Transformer-based sequential recommenders like HSTU and HLLM.
- **Key Innovations**: Learnable compression tokens for long user histories; plug-and-play with existing Transformer recommenders. Code: [github.com/facebookresearch/PerSRec](https://github.com/facebookresearch/PerSRec).

### 7. Planning over Matrix-Factorization MDPs for Candidate Generation
- **Authors**: Mikhail Trapeznikov, Maksim Utushkin
- **Institution**: VK / Lomonosov Moscow State University
- **arXiv**: [2607.02115](https://arxiv.org/abs/2607.02115)
- **Abstract**: Casts top-K retrieval as an MDP over implicit-ALS posterior. Actions are items; transitions are closed-form rank-one fold-ins. Compares static retrieval, one-step planning, and horizon-K MCTS. One-step lookahead captures most of the gain.
- **Key Innovations**: Dynamics-aware retrieval via lightweight planning layer on top of fixed MF embeddings; no retraining required.

### 8. Bi-NAS: Towards Effective and Personalized Explanation for Recommender Systems via Bi-Level Neural Architecture Search
- **Authors**: Longfeng Wu, Yao Zhou, Tong Zeng et al. (Virginia Tech, Google, Amazon)
- **Institution**: Virginia Tech / Google / Amazon
- **arXiv**: [2607.01387](https://arxiv.org/abs/2607.01387)
- **Abstract**: Bi-level NAS framework that jointly optimizes cross-attention and feature interaction functions for explanation generation. Integrates LLM zero-shot prompting for personalized explanations. Aligns user feature preferences with item quality scores.
- **Key Innovations**: NAS for explainability in recommenders; LLM-enhanced personalized explanation generation.

### 9. Diffusion-GR2: Diffusion Generative Reasoning Re-ranker
- **Authors**: Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, Mingfu Liang et al.
- **Institution**: Meta AI / UNC Chapel Hill
- **arXiv**: [2607.01170](https://arxiv.org/abs/2607.01170)
- **Abstract**: Converts autoregressive reasoning re-ranker (GR2) to block-diffusion for parallel decoding. Uses conversion fine-tuning (CFT), on-policy distillation (OPD), and RL stage. Achieves 2.4–3.5× throughput increase with near-AR accuracy on Amazon Beauty.
- **Key Innovations**: Block-diffusion for recommendation re-ranking; CFT closes structural gap; OPD closes distributional gap.

### 10. Real-Time Hard Negative Sampling via LLM-based Clustering for Large-Scale Two-Tower Retrieval
- **Authors**: Ivan Ji, Liuyi Hu, Harrison Zhao et al.
- **Institution**: Meta
- **arXiv**: [2607.00448](https://arxiv.org/abs/2607.00448)
- **Abstract**: Self-supervised hard negative sampling using LLM-generated item clusters. "Cluster GOOBS" framework generates hard negatives on-the-fly during training. +53% CTR lift in production; reduces popularity bias (top-100 item impression contribution drops from 50% to 32%).
- **Key Innovations**: LLM-based clustering for hard negative mining; real-time serving framework at billion-scale; popularity bias mitigation.

### 11. ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping
- **Authors**: Jiacheng Chen, Tao Zhang et al.
- **Institution**: Alibaba (Taobao & Tmall Group)
- **arXiv**: [2606.31693](https://arxiv.org/abs/2606.31693)
- **Abstract**: Foundation model unifying intent understanding, execution planning, and semantic-ID-based item-space operations for agentic shopping. Replaces tool-mediated pipelines with model-native item fulfillment. Evaluated on Taobao production logs.
- **Key Innovations**: Unified intent-to-item model; LLM-operable semantic IDs; model-native action protocol reduces lossy handoffs between LLM and retrieval/ranking interfaces.

---

## CTR Prediction & Advertising

### 12. CADET: Context-Conditioned Ads CTR Prediction with a Decoder-Only Transformer
- **Authors**: LinkedIn Engineering (Kulothungun, Kumar, Boda, Borisyuk, Wang et al.)
- **Institution**: LinkedIn
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Abstract**: End-to-end decoder-only Transformer for ads CTR deployed at LinkedIn. Key innovations: context-conditioned decoding with multi-tower heads (solves CTR-position chicken-and-egg), self-gated attention, timestamp-based RoPE, session masking for train-serve consistency, custom Flash Attention. 11.04% CTR lift vs. LiRank baseline in production.
- **Key Innovations**: First decoder-only Transformer for ads CTR at scale; self-gated attention; timestamp RoPE; resolves CTR-position feedback loop.

### 13. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao et al.
- **Institution**: Renmin University
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944) (Accepted by TKDD)
- **Abstract**: Knowledge distillation consolidates explicit feature interaction learning into a main MLP network; parallel MLP captures implicit interactions. Despite being vanilla MLP, achieves SOTA across three benchmarks. Scalable and efficient.
- **Key Innovations**: Dual-stream MLP with knowledge distillation; alignment strategies for dual-MLP compatibility; SOTA with simple architecture.

### 14. Generative Long-term User Interest Modeling for Click-Through Rate Prediction (GenLI)
- **Authors**: Jiangli Shao, Kaifu Zheng et al.
- **Institution**: —
- **arXiv**: [2605.15905](https://arxiv.org/abs/2605.15905)
- **Abstract**: Generative model with Interest Generation Module (IGM), Behavior Retrieval Module (BRM), and Interest Fusion Module (IFM). IGM generates multiple interest distributions via O(1) lookup; target-independent and captures behavior interactions.
- **Key Innovations**: Generative (not retrieval-based) long-term interest modeling; O(1) behavior retrieval complexity; target-independent interest distributions.

---

## Sequential Modeling

### 15. NextFlow: Unified Sequential Modeling Activates Multimodal Capabilities
- **Authors**: ByteDance (ByteVisionLab)
- **Institution**: ByteDance
- **arXiv**: [2601.02204](https://arxiv.org/abs/2601.02204)
- **Abstract**: Unified decoder-only autoregressive transformer trained on 6T interleaved text-image tokens. Next-token prediction for text; next-scale prediction for images. Generates 1024×1024 images in 5 seconds. SOTA among unified models, rivals specialized diffusion models.
- **Key Innovations**: Next-scale prediction for visual generation (not raster-scan); unified text-image autoregressive modeling at 6T scale; prefix-tuning for RL.

---

## Games & Reinforcement Learning

### 16. Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning
- **Authors**: Jingqi Tong, Jixin Tang et al. (Fudan University)
- **Institution**: Fudan University
- **arXiv**: ICLR 2026 (OpenReview)
- **Abstract**: Proposes Code2Logic to synthesize game reasoning data from code. GameQA dataset covers 30 games, 158 verifiable tasks. RL training on game data generalizes to 7 out-of-domain VLM benchmarks. Scaling game diversity/data volume consistently improves reasoning.
- **Key Innovations**: Code2Logic for synthetic game reasoning data; verifiable rewards from game mechanics; cross-domain generalization from game RL training.

### 17. AI Native Games: A Survey and Roadmap
- **Authors**: Zhiyue Xu, Fandi Meng et al.
- **Institution**: —
- **arXiv**: [2607.00527](https://arxiv.org/abs/2607.00527)
- **Abstract**: Defines AI-native games by counterfactual criterion: if generative AI were removed, the core loop would collapse. Analyzes 53 artifacts; introduces G/N taxonomy (game type × AI mechanic). Corpus concentrated on language-forward designs.
- **Key Innovations**: Counterfactual definition of AI-native games; G/N taxonomy; identifies semantic openness as central design problem.

### 18. Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Player Games
- **Authors**: —
- **Institution**: —
- **arXiv**: (May 2026)
- **Abstract**: Uses RL to teach LLMs strategic game reasoning. Model learns from feedback about move quality rather than generating first-answer heuristics.
- **Key Innovations**: RL-based strategic reasoning for LLMs in game environments.

---

## Inference Efficiency & Sparse Attention

### 19. SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference
- **Authors**: Yaosheng Fu, Guangxuan Xiao, Xin Dong, Song Han, Oreste Villa
- **Institution**: NVIDIA / MIT / ByteDance Seed
- **arXiv**: [2606.04511](https://arxiv.org/abs/2606.04511) (June 2026)
- **Abstract**: Decoupled sparse attention with a fourth "Forecast" projection that predicts KV blocks needed by the next layer, enabling CPU-to-GPU prefetching overlap. <0.5% parameter overhead. Up to 1.7× speedup over state-of-the-art sparse attention methods.
- **Key Innovations**: Forecast projection for lookahead KV selection; decoupled from attention query; compact implementation (1 head per GQA group).

### 20. SPIN: Sparse-Attention-Aware Inference Framework
- **Authors**: Baotong Lu et al.
- **Institution**: —
- **arXiv**: [2604.26837](https://arxiv.org/abs/2604.26837)
- **Abstract**: Co-designs execution pipeline with hierarchical KV storage. Unified partition abstraction maps sparsity granularities to page-based KV substrate; locality-aware KV cache manager with bucketed LRU. 1.66–5.66× higher throughput than vLLM; 7–9× lower TTFT.
- **Key Innovations**: Unified sparse-attention abstraction across granularities; two-level hierarchical metadata layout; bucketed LRU for GPU-CPU boundary efficiency.

---

## Summary of Trends

| Trend | Key Papers |
|-------|-----------|
| **SSMs & Hybrid Architectures** | Mamba-3, Nemotron-3 (hybrid attention + SSM) |
| **LLM x Recommendation** | RecPilot, Self-Evolving RecSys, GenLI, ShopX |
| **CTR with Transformers** | CADET (decoder-only), DS-MLP (MLP renaissance) |
| **Diffusion for RecSys** | Diffusion-GR2 (parallel decoding for re-ranking) |
| **Agentic Shopping** | ShopX (model-native intent-to-item) |
| **Hard Negative Sampling** | Cluster GOOBS (+53% CTR), HNLMRec |
| **Sparse Attention** | MoBA, SparDA, SPIN |
| **Games for VLM Training** | Game-RL (Code2Logic verifiable data) |
| **AI-Native Game Design** | AI Native Games survey, Strat-Reasoner |
| **Autonomous ML Engineering** | Self-Evolving RecSys (LLM-as-MLE) |
