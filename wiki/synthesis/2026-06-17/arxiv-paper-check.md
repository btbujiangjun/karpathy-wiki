---
title: "arXiv Paper Check — AI & CTR (June 17, 2026)"
type: synthesis
created: 2026-06-17
updated: 2026-06-17
sources: [arxiv.org]
tags: [arxiv, paper-check, ai, ctr, recommendation]
---

# arXiv Paper Check — AI & CTR (June 17, 2026)

> Surveying cs.AI new submissions (214 entries, Wed 17 Jun) + cs.IR (10 new + 34 Tue 16 Jun). Focus: AI/LLM systems, CTR prediction, recommendation, IR.

## AI / LLM Systems

### 1. Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers
- **Authors**: Sajad Movahedi, Vera Milovanović, Shlomo Libo Feigin, Alexander Theus, Thomas Hofmann, Valentina Boeva, T. Konstantin Rusch, Antonio Orvieto
- **arXiv**: 2606.18206 (16 Jun 2026)
- **Key idea**: FPRM uses fixed-point convergence as an end-to-end halting mechanism in a looped Transformer architecture. Pre-norm + residual scaling fixes signal propagation in deep loops. Adapts compute to task difficulty. Strong on Sudoku, Maze, state-tracking, ARC-AGI.
- **Significance**: Elegant solution for adaptive-depth reasoning without explicit halting predictors.

### 2. Small Initialization Matters for Large Language Models
- **Authors**: Liangkai Hang, Junjie Yao, Zhiyu Li, Feiyu Xiong, Hongkang Yang, Zhi-Qin John Xu
- **arXiv**: 2606.17945 (16 Jun 2026)
- **Key idea**: Parameter initialization is a "gene-like determinant" of LLM training. Small initialization drives a distinct developmental trajectory: parameters condense into low-complexity structures first, then expand. Gains concentrate on non-trivial predictions. Proposes γ-initialization rule.
- **Significance**: Almost cost-free intervention that improves pretraining and reasoning across model scales.

### 3. How Inference Compute Shapes Frontier LLM Evaluation
- **Authors**: Jessica McFadyen, Ole Jorgensen, Harry Coppock, Kevin Wei, Cozmin Ududec
- **arXiv**: 2606.17930 (16 Jun 2026)
- **Key idea**: 12 frontier LLMs evaluated on 7 benchmarks (cybersecurity, FrontierMath, HLE, TerminalBench) under varying inference budgets. Larger token budgets substantially improve scores. Benchmark scores are protocol-dependent — should be reported as a function of inference compute.
- **Significance**: Critical for proper model comparison and safety evaluation. Fixed-budget evals increasingly understate frontier capability.

### 4. PreAct: Computer-Using Agents that Get Faster on Repeated Tasks
- **Authors**: Bojie Li
- **arXiv**: 2606.17929 (16 Jun 2026)
- **Key idea**: On first success, compiles the agent run into a small state-machine program. Later replays directly 8.5-13x faster with no per-step LLM calls. Replay checks screen state at each step; falls back to agent if mismatch detected. Store-time validation catches faulty programs.
- **Significance**: Practical speedup for repeated computer-use tasks with safety checks.

### 5. STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training
- **Authors**: Jinjie Shen, Wei Deng, Xian Hu, Daiguo Zhou, Jian Luan
- **arXiv**: 2606.17979 (16 Jun 2026)
- **Key idea**: Rather than single scalar reward for entire diffusion trajectory, STAR uses text-image attention to spatially allocate rewards per denoising step. Applies stronger policy updates to relevant latent regions. Achieves 0.9759 GenEval, 0.9757 OCR, 23.60 PickScore with SD3.5 Medium.
- **Significance**: Fine-grained RL for text-to-image; demonstrates spatial/temporal structure matters for policy updates.

### 6. E³RL: Shattering the Autoregressive Curse — Dynamic Epistemic Entropy Orchestrated Erasable RL
- **Authors**: Ziliang Wang, Kang An, Faqiang Qian, Jialu Cai, Cijun Ouyang, Yuhang Wang, Qibing Ren, Yichao Wu
- **arXiv**: 2606.17735 (16 Jun 2026)
- **Key idea**: RL for LLMs that can detect and "erase" early mistakes during long reasoning traces by using local autoregressive cross-entropy as epistemic uncertainty signal. Segment-level adaptive thresholds + KV cache reuse. 4B/8B models beat SOTA on AIME by 5.3%/6.5%.
- **Significance**: Self-healing reasoning — addresses the fundamental autoregressive curse of error propagation.

### 7. HyGRAG: A Unified Framework for Context-Aware and Relation-Aware Graph RAG
- **Authors**: Haoyang Zhong, Yifei Sun, Antong Zhang, Chunping Wang, Lei Chen, Yang Yang
- **arXiv**: 2606.18075 (WWW 2026)
- **Key idea**: Hierarchical graph RAG with LLM-generated summaries over hybrid chunk+entity nodes. Iterative clustering + community-based retrieval. Dynamic updates via attachment algorithms. +9.7% multi-hop reasoning accuracy.
- **Significance**: Addresses the fundamental RAG limitation of retrieving before synthesizing — HyGRAG synthesizes first, then retrieves.

## CTR / Recommendation / IR

### 8. OneRank: Unified Transformer-Native Ranking Architecture for Multi-Task Recommendation
- **Authors**: Jiakai Tang, Sunhao Dai, Kun Wang, Zhiluohan Guo, Yu Zhao, Cong Fu, Kangle Wu, Yabo Ni, Anxiang Zeng, Xu Chen, Jun Xu
- **arXiv**: 2606.16838 (KDD 2026, 15 Jun 2026)
- **Key idea**: Eliminates encoder-predictor separation in multi-task ranking. Task-private channels for forward representation and backward optimization. Dynamic matching-based scoring replaces static MLP scorers. Reduces inter-task interference (seesaw phenomenon).
- **Significance**: A new architectural paradigm for industrial MTL ranking — Transformer-native, not Transformer-as-encoder.

### 9. Temporal Preference Optimization for Unsupervised Retrieval
- **Authors**: HyunJin Kim, Jaejun Shim, Young Jin Kim, JinYeong Bak
- **arXiv**: 2606.17664 (ICML 2026, 16 Jun 2026)
- **Key idea**: TPOUR uses TRPO (Temporal Retrieval Preference Optimization) to guide unsupervised retrievers toward temporally aligned documents. Learns time embeddings for continuous temporal alignment. Despite 72.7x smaller than Qwen-Embedding-8B, improves nDCG@5 by +12-15%.
- **Significance**: Addresses temporal misalignment in retrieval without explicit timestamp supervision.

### 10. Do Generative Recommenders Deepen the Information Cocoon?
- **Authors**: Jiyuan Yang, Gengxin Sun, Mengqi Zhang, Lingjie Wang, Yuanzi Li, Hongxi Cui, Xin Xin, Pengjie Ren
- **arXiv**: 2606.17707 (16 Jun 2026)
- **Key idea**: Closed-loop simulation with LLM-powered user simulators comparing generative recommenders vs traditional sequential baselines. Generative recommenders are less prone to exposure-level cocoons. Cocoon severity depends on tokenization (collaborative > semantic) and model scale (larger = more diverse).
- **Significance**: Timely study as generative recommendation gains adoption in production.

### 11. On the Memorization Behavior of LLMs in Generative Recommendation
- **Authors**: Sunwoo Kim, Sunkyung Lee, Clark Mingxuan Ju, Donald Loveland, Bhuvesh Kumar, Kijung Shin, Neil Shah, Liam Collins
- **arXiv**: 2606.17276 (16 Jun 2026)
- **Key idea**: Systematic study of memorization in generative recommender LLMs — when models memorize user-item interactions vs generalize. Implications for privacy and recommendation quality.
- **Significance**: Important for understanding when generative recommenders generalize vs overfit.

### 12. HoloRec: Holistic Encoding and Interleaved Reasoning for Generative Recommendation
- **Authors**: Shuqi Zhao, Jingsong Su, Xiang Liu, Xingzhi Yao, Yiming Qiu, Huimu Wang, Liang Lin, Pengbo Mo, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu
- **arXiv**: 2606.15331 (16 Jun 2026)
- **Key idea**: Holistic encoding that captures both user preferences and item semantics, interleaved reasoning for step-by-step recommendation generation.
- **Significance**: Advances the generative recommendation paradigm with structured reasoning.

### 13. RSRank: Learning Relevance from Representational Shifts
- **Authors**: Archit Gupta, Sai Sundaresan, Debabrata Mahapatra
- **arXiv**: 2606.17468 (16 Jun 2026)
- **Key idea**: Relevance scoring based on representational shifts rather than static similarity — captures dynamic relevance through model representation changes.
- **Significance**: Novel perspective on relevance modeling for retrieval.

## Summary

| Category | Count | Top Pick |
|----------|-------|----------|
| AI/LLM Architecture | 3 | Fixed-Point Reasoners (looped Transformers) |
| LLM Training & Evaluation | 2 | Small Initialization Matters |
| Agent Systems | 1 | PreAct (8.5-13x faster repeated tasks) |
| Text-to-Image RL | 1 | STAR (spatiotemporal reward allocation) |
| RAG | 1 | HyGRAG (+9.7% multi-hop reasoning) |
| RL for LLM Reasoning | 1 | E³RL (self-healing autoregressive reasoning) |
| CTR/Ranking | 1 | OneRank (Transformer-native MTL, KDD 2026) |
| IR/Retrieval | 3 | TPOUR (temporal-aware unsupervised retrieval, ICML 2026) |
| Recommendation | 2 | Information Cocoon (generative vs traditional) |

**Key themes**: (1) Adaptive compute allocation (Fixed-Point, PreAct, E³RL, STAR) — the test-time compute scaling theme continues across domains; (2) Transformer-native ranking replacing encoder-predictor separation (OneRank); (3) Temporal awareness in retrieval (TPOUR); (4) Generative recommendation maturing with behavioral analysis (cocoons, memorization).
