---
title: "arXiv Paper Check — AI & CTR (July 12, 2026)"
type: synthesis
created: 2026-07-12
updated: 2026-07-12
sources: []
tags: [arxiv, daily, ai, ctr, recommendation, llm, agents]
---

# arXiv Paper Check — AI & CTR (July 12, 2026)

> Automated daily scan of cs.AI, cs.LG, cs.IR for new papers. ~188K cs.AI, ~276K cs.LG, ~925 CTR/click-through papers indexed. This report curates the most interesting recent submissions.

## Summary

**20 curated papers** across 6 categories from July 9, 2026 submissions. Key themes: LLM behavioral analysis (quantization effects, super weights), agentic memory & planning, video reasoning, ad CTR optimization, and speculative decoding.

---

## 🧠 LLM Behavior & Training

### 1. The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs
- **Authors**: Baha Rababah, Cuneyt Gurcan Akcora, Carson K. Leung
- **arXiv**: [2607.08734](https://arxiv.org/abs/2607.08734)
- **Key Contribution**: Introduces *correctness agreement* — a decision-level metric revealing that quantized models diverge behaviorally from base models even when perplexity appears preserved. Analyzes quantization as a structural operator on attention weights, showing query/key projections are consistently more sensitive than value/output. Non-linear breakpoints emerge at low bit-widths (2-bit).
- **Relevance**: Challenges the assumption that perplexity tracks model equivalence post-quantization; important for deployment of quantized models in production recommendation/ranking systems.

### 2. Super Weights in LLMs and the Failure of Selective Training
- **Authors**: Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag
- **arXiv**: [2607.08733](https://arxiv.org/abs/2607.08733) (COLM 2026)
- **Key Contribution**: Shows that "Super Weights" (individually critical parameters) cannot be trained in isolation — targeting 100–8,192 Super Weight coordinates drops accuracy to random guessing. Training equal numbers of random positions succeeds. Demonstrates parameter importance ≠ parameter trainability; LoRA's structured decomposition succeeds where point-wise training fails.
- **Relevance**: Important for understanding fine-tuning and compression of LLMs in production settings.

### 3. SLORR: Simple and Efficient In-Training Low-Rank Regularization
- **Authors**: David González-Martínez, Shiwei Liu
- **arXiv**: [2607.08754](https://arxiv.org/abs/2607.08754)
- **Key Contribution**: Stateless, architecture-preserving framework for inducing low-rank structure during training. GPU-friendly approximations for Hoyer sparsity and nuclear norm regularizers. At 135M/560M LLM scale, compressed models preserve performance with <1% training overhead.
- **Relevance**: Practical approach for making models amenable to post-training compression without architecture changes.

### 4. Resample or Reroute? Budget-Aware Test-Time Model Selection for LLMs
- **Authors**: Teng-Ruei Chen
- **arXiv**: [2607.08665](https://arxiv.org/abs/2607.08665)
- **Key Contribution**: Formulates budget-aware test-time model selection where resampling the current model and rerouting to an alternative compete for a per-query cost budget. Proposes RoR (Resample-or-Reroute) allocation policy. Largest gains on most heterogeneous model pools.
- **Relevance**: Directly applicable to multi-model serving systems in production (e.g., routing between small/large models for recommendation queries).

### 5. A Practical Investigation of Training-free Relaxed Speculative Decoding
- **Authors**: Guoxuan Xia, Luka Ribar, Paul Balanca
- **arXiv**: [2607.08690](https://arxiv.org/abs/2607.08690)
- **Key Contribution**: Unifies existing relaxed speculative decoding approaches. Key finding: relaxation requires considerable capability evaluation (unlike lossless SD), and many approaches depend on drafters that are themselves good language models, making them unsuitable for lightweight dedicated drafters.
- **Relevance**: Practical guide for practitioners considering relaxed SD for inference acceleration.

---

## 🤖 Agents & Multi-Agent Systems

### 6. Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
- **Authors**: Yifan Wu, Lizhu Zhang, Yuhang Zhou et al.
- **arXiv**: [2607.08716](https://arxiv.org/abs/2607.08716)
- **Key Contribution**: Addresses "behavioral state decay" in long-horizon tasks. A separate memory agent proactively injects reminders rather than passively retrieving. Plug-and-play with frontier agents. +8.3pp on Terminal-Bench 2.0, +6.8pp on τ²-Bench. Ablations show selective intervention > passive retrieval > always-on injection.
- **Relevance**: Important for agentic AI systems where context windows overflow during multi-step tasks. Trains Qwen3.5-27B memory policy via SFT + GRPO.

### 7. WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search
- **Authors**: Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao et al.
- **arXiv**: [2607.08662](https://arxiv.org/abs/2607.08662)
- **Key Contribution**: Progressive recursive delegation framework for web search. Each agent node couples a local objective with a search mode; nodes can self-solve or delegate children. Probes information organization on the web before expanding. Outperforms single-agent and multi-agent baselines on BrowseComp-Plus, WideSearch, DeepWideSearch.
- **Relevance**: Advances multi-agent search beyond parallel-aggregate patterns; applicable to research and information retrieval tasks.

### 8. ProjAgent: Procedural Similarity Retrieval for Repository-Level Code Generation
- **Authors**: QiHong Chen, Aaron Imani, Iftekhar Ahmed
- **arXiv**: [2607.08691](https://arxiv.org/abs/2607.08691)
- **Key Contribution**: Introduces *procedural similarity* as a new retrieval signal for code generation — retrieving repo functions with similar procedural logic (not just lexical/semantic similarity). Decomposes target into reasoning steps, retrieves matching procedures at each step. 41.14% Pass@1 on REPOCOD, outperforming existing retrieval-based baselines.
- **Relevance**: Novel dimension for code retrieval; relevant for agentic coding tools that search codebases.

### 9. Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference
- **Authors**: Chuning Zhu, Eva Xu, Jose Barreiros et al.
- **arXiv**: [2607.08724](https://arxiv.org/abs/2607.08724)
- **Key Contribution**: Formulates reasoning for control policies as variational inference in an autoregressive latent space ("memory palace"). Retrieval is iterative and adaptive. LMP-π achieves strong performance in simulation and real-world while exhibiting interpretable, adaptive test-time compute allocation. Also yields a variable-length action tokenizer.
- **Relevance**: Bridges LLM-style reasoning with continuous control policies; potentially important for robotics and autonomous systems.

---

## 🎬 Video & Multimodal

### 10. OpenCoF: Learning to Reason Through Video Generation
- **Authors**: Xinyan Chen, Ziyu Guo, Renrui Zhang, Dongzhi Jiang, Hongsheng Li
- **arXiv**: [2607.08763](https://arxiv.org/abs/2607.08763)
- **Key Contribution**: Chain-of-Frame (CoF) reasoning — reasoning unfolds through temporally connected video frames. OpenCoF-17K dataset spans 11 task families. Introduces visual and textual reasoning tokens for spatial/temporal reasoning. Wan-CoF achieves considerable gains over Wan2.2 baseline on 4 video reasoning benchmarks.
- **Relevance**: Novel reasoning paradigm distinct from Chain-of-Thought; opens new research direction for video generation as reasoning medium.

### 11. AUTOPILOT-VQA: Benchmarking VLMs for Dashcam Understanding
- **Authors**: Siddharth Damodharan, Radhika Gupta, Ali Alshami et al.
- **arXiv**: [2607.08745](https://arxiv.org/abs/2607.08745)
- **Key Contribution**: Incident-centric VQA benchmark for dashcam video. Evaluates structured questions around safety-critical incidents covering weather, traffic, road conditions, avoidability reasoning. Part of CVPR 2026 competition.
- **Relevance**: Directly relevant to Tesla FSD and autonomous driving evaluation.

### 12. ARDY: Autoregressive Diffusion for Interactive Human Motion Generation (SIGGRAPH 2026)
- **Authors**: Kaifeng Zhao, Mathis Petrovich et al. (NVIDIA)
- **arXiv**: [2607.08741](https://arxiv.org/abs/2607.08741)
- **Key Contribution**: Streaming motion generation framework with hybrid representation (explicit root + latent body). Two-stage autoregressive transformer denoiser supporting online text prompts and flexible kinematic constraints. SIGGRAPH 2026 publication.
- **Relevance**: Real-time controllable motion generation for animation and humanoid robotics.

---

## 📊 CTR Prediction & Recommendation

### 13. COBART: Controlled, Optimized, Bidirectional and Auto-Regressive Transformer for Ad Headline Generation (KDD 2022)
- **Authors**: Yashal Shakti Kanungo, Gyanendra Das et al.
- **arXiv**: [2607.08071](https://arxiv.org/abs/2607.08071)
- **Key Contribution**: Prefix control tokens + BART fine-tuning for CTR-optimized ad headline generation. +25.82% Rouge-L, +5.82% estimated CTR over prior baseline. Flexible across ad formats and architectures.
- **Relevance**: Classic technique for bid-aware creative generation in advertising.

### 14. POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation (Kuaishou)
- **Authors**: Linxiao Che, Yijia Sun et al.
- **arXiv**: [2606.29946](https://arxiv.org/abs/2606.29946)
- **Key Contribution**: Uses upstream multi-task ranking scores (CTR + watch duration) to construct partial-order sequences for real-time interest modeling. Online deployed at Kuaishou: +0.249% per-user watch time on KS Single Page, +0.213% on KS Lite Page.
- **Relevance**: Directly relevant to CTR scaling and real-time sequential modeling.

### 15. RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning (Meta)
- **Authors**: Renzhi Wu, Zikun Cui et al.
- **arXiv**: [2606.18379](https://arxiv.org/abs/2606.18379)
- **Key Contribution**: Co-designs graph construction, representation learning, and serving. Subsampling with popularity bias correction, pre-computed PPR neighborhoods, co-learned cluster index reducing serving cost by 83%. +0.96% CTR, +2.75% CVR online. Powered 20+ retrieval launches.
- **Relevance**: Production-grade billion-scale graph retrieval system with significant CTR gains.

### 16. Beyond Positive Signals: Implicit Negative Behaviors for Sequential User Modeling
- **Authors**: Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **arXiv**: [2606.15252](https://arxiv.org/abs/2606.15252)
- **Key Contribution**: Mixed-polarity behavior sequences (interleaving positive + negative tokens) consistently outperform positive-only sequences across 5 architectures. +1.9% to +9.6% relative AUC on 3 benchmarks. Introduces Target-Aware Polarity Fusion (TAPF) gating.
- **Relevance**: Simple yet impactful data paradigm shift for CTR prediction — use negative signals (skips, scroll-past) alongside positive ones.

### 17. PIANO: Personalized Reranking for Music Search (NetEase Cloud Music)
- **Authors**: Weisheng Li, Chuqiao Huang et al.
- **arXiv**: [2606.16641](https://arxiv.org/abs/2606.16641) (ECML PKDD 2026)
- **Key Contribution**: Listwise re-ranking with Query-Driven Interest Refiner (historical query cross-attention) and Information Aggregation Node for list-level CTR/CVR prediction. Online: +0.62% CTR, +4.45% CVR on NetEase Cloud Music.
- **Relevance**: Demonstrates list-level optimization for multi-objective CTR/CVR in music search.

### 18. FeLiX: Robust Federated Learning for Real-World Feed Ranking
- **Authors**: Dhruv Garg, Neha Lakhani et al.
- **arXiv**: [2607.06979](https://arxiv.org/abs/2607.06979)
- **Key Contribution**: FL orchestration for model freshness in feed ranking. Streaming-aware availability tiers, fresh-utility selection, delay-robust aggregation. Up to 2.37× faster wall-clock convergence vs. state-of-the-art FL baselines with 1.30× bandwidth reduction.
- **Relevance**: Addresses the staleness problem in federated learning for CTR/recommendation models on mobile.

### 19. EMA-FS: Accelerating GBDT Training via Gain-Informed Feature Screening
- **Authors**: Yan Song
- **arXiv**: [2606.26337](https://arxiv.org/abs/2606.26337)
- **Key Contribution**: EMA of per-feature split gains to screen low-gain features before histogram construction. 2.61× speedup on 500-feature synthetic data, 1.45× on IEEE-CIS Fraud dataset. At 70% retention: +0.11 AUC + 1.34× speedup. Implemented in ~120 lines of C++ across all LightGBM tree learners.
- **Relevance**: Practical optimization for LightGBM-based CTR models used widely in industry.

### 20. Dimensionality Reduction Meets Network Science: Sensemaking on UMAP's kNN Graph
- **Authors**: Duen Horng Chau, Donghao Ren, Fred Hohman, Dominik Moritz (Apple)
- **arXiv**: [2607.08746](https://arxiv.org/abs/2607.08746)
- **Key Contribution**: Leverages UMAP's internal kNN graph (before 2D projection) for data sensemaking. PageRank for exemplar selection, k-core decomposition for density analysis, clustering coefficient for neighborhood detection. Competitive with purpose-built methods.
- **Relevance**: Useful visualization/exploration technique for embedding-based systems (item/user embeddings in recommendation).

---

## 📐 Key Trends

| Trend | Papers |
|-------|--------|
| **LLM Behavioral Analysis** | Illusion of Equivalency, Super Weights, SLORR |
| **Agentic Memory & Planning** | Memory Agent, WebSwarm, Latent Memory Palace |
| **CTR Sequential Modeling** | POEM (partial-order), Beyond Positive Signals (mixed-polarity), PIANO (listwise) |
| **Production Graph Retrieval** | RankGraph-2 (Meta, 0.96% CTR) |
| **Inference Optimization** | Speculative Decoding, RoR (Resample-or-Reroute) |
| **Video Reasoning** | OpenCoF (Chain-of-Frame), AUTOPILOT-VQA |
| **Practical ML Training** | EMA-FS (LightGBM speedup), FeLiX (federated freshness) |

---

## Connection to [[wiki/overview|Karpathy Wiki Themes]]

- **Video Reasoning (OpenCoF)**: Connects to Karpathy's interest in video generation as reasoning medium (Chain-of-Frame vs Chain-of-Thought).
- **Agentic Memory (Memory Agent)**: Directly relevant to Karpathy's agentic engineering framework — behavioral state decay is a practical challenge in agentic systems.
- **LLM Behavioral Analysis**: Super Weights and quantization effects connect to Karpathy's emphasis on understanding model internals deeply.
- **CTR Sequential Modeling**: POEM's real-time partial-order modeling represents the frontier of production ranking systems.
- **Autonomous Driving (AUTOPILOT-VQA)**: Safety-critical reasoning for dashcam understanding aligns with Karpathy's Tesla FSD work.
