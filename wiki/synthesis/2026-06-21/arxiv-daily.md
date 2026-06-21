---
title: "arXiv Daily — AI, LLMs, CTR, Recommendation, Advertising, Sequential Modeling, Games, Agents (June 21, 2026)"
type: synthesis
created: 2026-06-21
updated: 2026-06-21
sources: [arxiv]
tags: [arxiv-daily, llm, recommendation, ctr, games, rl, advertising, sequential-modeling, agents]
---

# arXiv Daily — AI, LLMs, CTR, Recommendation, Advertising, Sequential Modeling, Games, Agents

> **Date**: 2026-06-21 (covering recent submissions from Jun 15–Jun 21, 2026)
> **Scope**: 20 papers across 7 categories

---

## 1. LLM Architecture & Training

### 1.1 Variable-Width Transformers
- **Title**: Variable-Width Transformers
- **Authors**: Zhaofeng Wu, Oliver Sieberling, Shawn Tan, Rameswar Panda, Yury Polyanskiy, Yoon Kim
- **Institution**: MIT, NVIDIA
- **arXiv**: [2606.18246](https://arxiv.org/abs/2606.18246)
- **Date**: Jun 16, 2026
- **Abstract**: Proposes a `>-<former` architecture with nonuniform width allocation across layers — wider early and late layers, narrower middle layers. Uses a parameter-free residual resizing mechanism. Across 200M–2B dense and 3B MoE models, outperforms uniform baselines on language modeling loss while reducing FLOPs by 22% and KV cache memory by 15%.
- **Key Innovation**: Bottleneck-style variable-width transformer that allocates capacity non-uniformly for resource-optimal scaling.

### 1.2 FLARE: Diffusion for Hybrid Language Model
- **Title**: FLARE: Diffusion for Hybrid Language Model
- **Authors**: Yuchen Zhu et al.
- **Institution**: — (multiple)
- **arXiv**: [2606.01774](https://arxiv.org/abs/2606.01774)
- **Date**: Jun 1, 2026
- **Abstract**: A systematic conversion framework for hybrid-attention LLMs that enables one checkpoint to support both AR-style verified decoding and diffusion-style parallel denoising. Identifies transfer data quality as primary determinant of capability preservation. Competitive with open-source dLLMs and delivers throughput gains in concurrent serving.
- **Key Innovation**: Unifies autoregressive and diffusion decoding in a single hybrid-attention checkpoint; token-equal AR-and-diffusion objective.

### 1.3 Connect the Dots: Training LLMs for Long-Lifecycle Agents via RL
- **Title**: Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning
- **Authors**: Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, Jingren Zhou
- **Institution**: Alibaba Group
- **arXiv**: [2606.20002](https://arxiv.org/abs/2606.20002)
- **Date**: Jun 18, 2026
- **Abstract**: Presents a framework for training LLMs for "Connect the Dots" meta-capability — agents that solve long sequences of tasks while continuously exploring and self-updating their context. Uses GRPO-style RL with fine-grained credit assignment. Demonstrates cross-domain OOD generalization.
- **Key Innovation**: End-to-end RL with long rollout sequences interleaving solve-task and update-context episodes; first systematic training of long-lifecycle agent meta-capability.

---

## 2. CTR Prediction & Advertising

### 2.1 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Title**: CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: Ruoyan Wang et al.
- **Institution**: LinkedIn
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Date**: Feb 11, 2026 (deployed in production)
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Key innovations: (1) context-conditioned decoding with multi-tower prediction heads for post-scoring signals; (2) self-gated attention; (3) timestamp-based RoPE variant; (4) session masking for train-serve skew. Achieves 11.04% CTR lift vs LiRank baseline.
- **Key Innovation**: First decoder-only transformer for ads CTR at scale; resolves chicken-and-egg between predicted CTR and ad position ranking.

### 2.2 Dual-Stream MLP for CTR Prediction
- **Title**: Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: — (multiple)
- **Institution**: — (multiple)
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Date**: Jun 3, 2026
- **Abstract**: Proposes a dual-stream MLP architecture for CTR prediction that outperforms 17 baseline methods including WuKong and SFG. Demonstrates that a well-designed MLP can rival complex DLRM architectures.
- **Key Innovation**: Simple dual-stream design challenges the dominance of complex feature-interaction architectures for CTR.

### 2.3 IDProxy: Cold-Start CTR for Ads and Recommendation
- **Title**: IDProxy: Cold-Start CTR Prediction for Ads and Recommendation
- **Authors**: — (multiple)
- **Institution**: Xiaohongshu (小红书)
- **arXiv**: 2603 (mentioned in search)
- **Date**: Mar 2026
- **Abstract**: Addresses cold-start CTR prediction for ads and recommendation at Xiaohongshu scale. Deployed on production traffic serving millions of users daily.
- **Key Innovation**: Cold-start solution at social-commerce platform scale.

### 2.4 LLM-HYPER: Generative CTR for Cold-Start Ad Personalization
- **Title**: LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks
- **Authors**: Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, Kehui Yao et al.
- **Institution**: Amazon (top US e-commerce platform)
- **arXiv**: [2604.12096](https://arxiv.org/abs/2604.12096)
- **Date**: Apr 2026
- **Abstract**: Treats LLMs as hypernetworks to directly generate parameters of CTR estimator in training-free manner. Uses few-shot CoT prompting over multimodal ad content. Outperforms cold-start baselines by 55.9% NDCG@10. Deployed in production.
- **Key Innovation**: First use of LLMs as hypernetworks for zero-shot CTR parameter generation; eliminates need for cold-start training data.

---

## 3. Recommendation Systems

### 3.1 G2Rec: Structuring and Tokenizing Distributed User Interest for Generative Recommendation
- **Title**: Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
- **Authors**: Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng, Ren Chen, Xiangjun Fan, Hong Li, Hong Yan, Hanghang Tong
- **Institution**: Meta (Facebook), University of Illinois Urbana-Champaign
- **arXiv**: [2606.20554](https://arxiv.org/abs/2606.20554)
- **Date**: Jun 18, 2026
- **Abstract**: Proposes G2Rec, a scalable framework unifying holistic graph-based user co-engagement modeling with semantic tokenization for industrial-scale generative recommendation. Online deployment across Meta product surfaces.
- **Key Innovation**: First framework to combine graph-based user co-engagement with supervised semantic tokenization for generative recommendation at Meta scale.

### 3.2 Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Title**: Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Authors**: Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong, Raghu Keshavan, Aniruddh Nath, Li Wei, Xinyang Xi
- **Institution**: Meta (Facebook)
- **arXiv**: [2606.19635](https://arxiv.org/abs/2606.19635)
- **Date**: Jun 17, 2026
- **Abstract**: Transforms traditional recommendation signals into "soft tokens" that LRMs can process directly. Prevents prompt length explosion while compressing heterogeneous input features. Validated in production-scale environment.
- **Key Innovation**: Soft tokenization framework for compressing diverse recommendation signals into LRM-compatible format without textualization overhead.

### 3.3 Generative Recommendation for Large-Scale Advertising
- **Title**: Generative Recommendation for Large-Scale Advertising
- **Authors**: — (multiple)
- **Institution**: — (multiple)
- **arXiv**: 2602 (mentioned in search)
- **Date**: Feb 2026
- **Abstract**: Explores generative recommendation paradigm for advertising, reformulating recommendation as next-token prediction. Demonstrates that recommendation systems should borrow more from the generative AI toolkit.
- **Key Innovation**: Cross-pollination of generative AI with advertising recommendation.

---

## 4. Reinforcement Learning & Games

### 4.1 SPIRAL: Self-Play on Zero-Sum Games for Reasoning
- **Title**: SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Institution**: NUS, CFAR A*STAR, Northeastern Univ., Sea AI Lab, Plastic Labs, Univ. of Washington
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Date**: Jun 2025 (updated Mar 2026)
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against themselves. Proposes role-conditioned advantage estimation (RAE) for stable multi-agent training. Training Qwen3-4B on Kuhn Poker alone achieves 8.6% improvement on math and 8.4% on general reasoning.
- **Key Innovation**: Self-play on games as a fully autonomous substitute for human-curated RL training data; identifies three transferable cognitive patterns (systematic decomposition, expected value calculation, case-by-case analysis).

### 4.2 Game-RL: Synthesizing Multimodal Verifiable Game Data for VLM Reasoning
- **Title**: Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning
- **Authors**: Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou et al. (24 authors)
- **Institution**: Fudan University, Shanghai Innovation Institute, Shanghai AI Lab, SUSTech
- **arXiv**: [2505.13886](https://arxiv.org/abs/2505.13886) (ICLR 2026)
- **Date**: May 2025 (ICLR 2026 accepted)
- **Abstract**: Proposes Code2Logic to synthesize game reasoning data and the GameQA dataset (30 games, 158 verifiable tasks). RL training solely on GameQA enables VLMs to generalize across 7 diverse out-of-domain vision-language benchmarks. Scaling game diversity or data volume consistently improves generalization.
- **Key Innovation**: First systematic use of video games as verifiable multimodal RL training data for VLM general reasoning; Code2Logic pipeline for unlimited synthesis.

### 4.3 VIMPO: Value-Implicit Policy Optimization for LLMs
- **Title**: VIMPO: Value-Implicit Policy Optimization for LLMs
- **Authors**: Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song, Xuandong Zhao
- **Institution**: UC Berkeley
- **arXiv**: [2606.20008](https://arxiv.org/abs/2606.20008)
- **Date**: Jun 18, 2026
- **Abstract**: New policy optimization method that implicitly captures value information without a separate value network. Improves stability and performance in LLM RL training.
- **Key Innovation**: Implicit value estimation eliminates need for separate critic network in policy gradient methods.

### 4.4 MindGames Arena: Delayed Per-Step Reward Attribution
- **Title**: MindGames Arena Generalization Track: In2AI Solution with Delayed Per-Step Reward Attribution
- **Authors**: Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov
- **Institution**: — (multiple)
- **arXiv**: [2606.00017](https://arxiv.org/abs/2606.00017)
- **Date**: Jun 1, 2026
- **Abstract**: Technical report on first-place solution in both Open and Efficient tracks of MindGames Arena at NeurIPS 2025. Addresses delayed reward attribution in game-playing agents.
- **Key Innovation**: Per-step credit assignment in environments with sparse/delayed rewards.

---

## 5. Sequential Modeling

### 5.1 Diffusion Models for Adaptive Sequential Data Generation
- **Title**: Diffusion Models for Adaptive Sequential Data Generation
- **Authors**: Haoyang Cao, Minshuo Chen, Yinbin Han, Renyuan Xu
- **Institution**: — (multiple)
- **arXiv**: [2606.06007](https://arxiv.org/abs/2606.06007)
- **Date**: Jun 4, 2026 (revised Jun 14)
- **Abstract**: Proposes a sequential forward-backward diffusion framework for adapted time series generation that captures temporal dependence without anticipation of future information. Novel score-matching objective for parallel training with statistical guarantees. Validated on ARMA, Gaussian processes, and portfolio optimization.
- **Key Innovation**: First diffusion framework for adapted (non-anticipating) sequential data generation with rigorous statistical guarantees.

### 5.2 NextFlow: Unified Sequential Modeling for Multimodal Understanding and Generation
- **Title**: NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors**: Huichao Zhang, Liao Qu, Yiheng Liu et al. (36 authors)
- **Institution**: ByteDance (ByteVisionLab)
- **arXiv**: [2601.02204](https://arxiv.org/abs/2601.02204)
- **Date**: Jan 5, 2026
- **Abstract**: Unified decoder-only autoregressive transformer trained on 6T interleaved text-image tokens. Uses next-token prediction for text and next-scale prediction for images. Generates 1024×1024 images in 5 seconds, orders of magnitude faster than comparable AR models. SOTA among unified models.
- **Key Innovation**: Next-scale prediction for visual generation within a unified autoregressive framework; hierarchical prediction for different modalities.

---

## 6. Agents & Multi-Agent Systems

### 6.1 Agentic Reasoning for Large Language Models (Survey)
- **Title**: Agentic Reasoning for Large Language Models
- **Authors**: — (multiple)
- **Institution**: University of Illinois Urbana-Champaign
- **arXiv**: [2601.12538](https://arxiv.org/abs/2601.12538)
- **Date**: Jan 18, 2026
- **Abstract**: Comprehensive survey organizing agentic reasoning along three dimensions: foundational (planning, tool use, search), self-evolving (feedback, memory, adaptation), and collective multi-agent (coordination, knowledge sharing). Distinguishes in-context vs post-training reasoning.
- **Key Innovation**: Unified roadmap bridging thought and action for LLM agents; three-layer taxonomy of agentic reasoning.

### 6.2 Decoupling Search from Reasoning for LLM Agents
- **Title**: Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents
- **Authors**: Emmanuel Aboah Boateng, Kyle MacDonald, Amardeep Kumar, Siddharth Kodwani, Sudeep Das
- **Institution**: — (multiple)
- **arXiv**: [2606.18947](https://arxiv.org/abs/2606.18947)
- **Date**: Jun 17, 2026
- **Abstract**: Proposes a vendor-agnostic grounding architecture that separates search from reasoning in LLM agents. Enables modular, interchangeable search backends while maintaining reasoning quality.
- **Key Innovation**: Decoupled architecture for search and reasoning in agent systems.

### 6.3 LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents
- **Title**: LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents
- **Authors**: Md Nayem Uddin, Amir Saeidi, Eduardo Blanco, Chitta Baral
- **Institution**: Arizona State University
- **arXiv**: [2606.20529](https://arxiv.org/abs/2606.20529)
- **Date**: Jun 18, 2026
- **Abstract**: Introduces an inference-time method that maintains observed task states in a separate ledger, rendering states into the prompt and checking policy constraints before tool calls. Improves pass@k across four customer-service domains.
- **Key Innovation**: Explicit state management ledger for policy-adherent tool-calling; blocks policy violations before execution.

---

## 7. AI Safety & Evaluation

### 7.1 What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?
- **Title**: What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?
- **Authors**: Sihui Dai, Mann Patel
- **Institution**: — (multiple)
- **arXiv**: [2606.20508](https://arxiv.org/abs/2606.20508)
- **Date**: Jun 18, 2026
- **Abstract**: Studies how in-context demonstrations drive jailbreaking. Shows benign and harmful demonstrations are not interchangeable; preference optimization is critical training stage that prevents benign demonstrations from increasing harmful compliance. Reveals recency bias and model-specific refusal behaviors.
- **Key Innovation**: Systematic characterization (not just demonstration) of how demonstration composition, ordering, and training methodology affect safety compliance.

### 7.2 How Transparent is DiffusionGemma?
- **Title**: How Transparent is DiffusionGemma?
- **Authors**: Cindy Wu, Arthur Conmy, Neel Nanda
- **Institution**: — (multiple)
- **arXiv**: [2606.20560](https://arxiv.org/abs/2606.20560)
- **Date**: Jun 19, 2026
- **Abstract**: First interpretability study of DiffusionGemma, uncovering novel diffusion-specific phenomena: non-chronological reasoning, token/sequence smearing, and intermediate-context reasoning. Finds DiffusionGemma is similarly monitorable to Gemma 4.
- **Key Innovation**: First mechanistic interpretability analysis of a diffusion language model; identifies non-chronological reasoning as unique to diffusion.

---

## Summary Table

| # | Category | Paper | Venue/Lab | Date |
|---|----------|-------|-----------|------|
| 1 | LLM Architecture | Variable-Width Transformers | MIT, NVIDIA | Jun 16 |
| 2 | LLM Architecture | FLARE: Diffusion for Hybrid LM | — | Jun 1 |
| 3 | LLM + RL | Connect the Dots (CoD) | Alibaba | Jun 18 |
| 4 | CTR/Ads | CADET (Decoder-Only Transformer) | LinkedIn | Feb (prod) |
| 5 | CTR | Dual-Stream MLP for CTR | — | Jun 3 |
| 6 | CTR | IDProxy Cold-Start CTR | Xiaohongshu | Mar |
| 7 | CTR/Ads | LLM-HYPER (LLM as Hypernetwork) | Amazon | Apr |
| 8 | Recommendation | G2Rec (Generative Rec) | Meta, UIUC | Jun 18 |
| 9 | Recommendation | Token Factory (Soft Tokens) | Meta | Jun 17 |
| 10 | Recommendation | Generative Rec for Advertising | — | Feb |
| 11 | RL/Games | SPIRAL (Self-Play Games) | NUS, UW, Sea AI | Mar 2026 |
| 12 | RL/Games | Game-RL (Game Data for VLM) | Fudan, ByteDance | ICLR 2026 |
| 13 | RL | VIMPO (Value-Implicit Policy Opt) | UC Berkeley | Jun 18 |
| 14 | RL/Games | MindGames Arena | NeurIPS 2025 | Jun 1 |
| 15 | Sequential | Diffusion for Adaptive Sequential Data | — | Jun 4 |
| 16 | Sequential | NextFlow (Unified Seq Model) | ByteDance | Jan |
| 17 | Agents | Agentic Reasoning Survey | UIUC | Jan |
| 18 | Agents | Decoupling Search from Reasoning | — | Jun 17 |
| 19 | Agents | LedgerAgent (Structured State) | ASU | Jun 18 |
| 20 | Safety | Mixed Compliance Demonstrations | — | Jun 18 |
| 21 | Safety | DiffusionGemma Transparency | — | Jun 19 |
