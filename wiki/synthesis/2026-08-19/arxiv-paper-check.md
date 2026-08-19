---
title: "arXiv Paper Check — AI & CTR (August 19, 2026)"
type: synthesis
created: 2026-08-19
updated: 2026-08-19
tags: [arxiv, daily-check, ai, ctr, recommendation, agents, reasoning, rl, quantization, efficiency]
---

# arXiv Paper Check — AI & CTR (August 19, 2026)

> Papers from arXiv listings: cs.AI, cs.LG, cs.CL, cs.IR, stat.ML (submitted Aug 18–19, 2026). Curated for relevance to AI, LLMs, recommendation, advertising, sequential modeling, CTR, and games.

---

## 1. CTR/Rec/Ads/IR

### 1.1 GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors**: Chuyue (Baidu)
- **Affiliation**: Baidu
- **arXiv**: [2602.01865v2](https://arxiv.org/abs/2602.01865v2) — cs.IR, cs.AI
- **Key Innovation**: Generative Ranking for Ads at Baidu (GRAB) — end-to-end generative framework for CTR prediction. Integrates Causal Action-aware Multi-channel Attention (CamA) mechanism to capture temporal dynamics and specific action signals within user behavior sequences. Full-scale online deployment demonstrates +3.05% revenue increase and +3.49% CTR rise. Shows desirable scaling behavior with monotonic improvement as longer interaction sequences are utilized.
- **Abstract**: Traditional Deep Learning Recommendation Models (DLRMs) face increasing bottlenecks in performance and efficiency. GRAB integrates a novel CamA mechanism for temporal dynamics. Online deployment shows significant improvements over established DLRMs.

### 1.2 LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction
- **Authors**: Jiakai Tang, Runfeng Zhang, Weiqiu Wang, Yifei Liu, Chuan Wang, Xu Chen, et al.
- **Affiliation**: Not specified
- **arXiv**: [2604.19550](https://arxiv.org/abs/2604.19550) — cs.IR
- **Key Innovation**: Loop scaling paradigm that increases training-time computation through recursive reuse of shared model layers, decoupling computation from parameter growth. Sandwich architecture enhanced with Hyper-Connected Residuals and Mixture-of-Experts. Train-multi-loop, infer-zero-loop strategy where a single forward pass without any loop already outperforms all baselines. Oracle analysis reveals 0.02–0.04 AUC of untapped headroom.
- **Abstract**: Scaling Transformer-based CTR models by stacking more parameters brings growing computational overhead. LoopCTR introduces loop scaling to address this gap.

### 1.3 PRECTR-V2: Unified Relevance–CTR Framework with Cross-User Preference Mining
- **Authors**: Shuzhi Cao, Rong Chen, Ailong He, Shuguang Han, Jufeng Chen
- **Affiliation**: Xianyu (Alibaba)
- **arXiv**: [2602.20676](https://arxiv.org/abs/2602.20676) — cs.IR
- **Key Innovation**: Unified framework integrating search relevance matching and CTR prediction. Cross-user relevance preference mining for cold-start scenarios. Exposure bias correction via synthetic hard negative sampling. LLM-distilled lightweight encoder (2M params vs BERT's 110M) for joint optimization. Online A/B testing shows +1.39% per capita orders and +3.18% GMV.
- **Abstract**: Effectively coordinating search relevance matching and CTR prediction is crucial for discovering users' interests and enhancing platform revenue.

### 1.4 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng
- **Affiliation**: Not specified
- **arXiv**: [2606.07980](https://arxiv.org/abs/2606.07980) — cs.IR
- **Key Innovation**: Dual-path connector that pairs an identity residual with a block-level attention residual. Pointwise AttnRes with SiLU replaces Softmax for non-competitive multi-interest encoding. Up to +0.32% AUC at under 5% additional FLOPs. 8-layer DeRes matches 16-layer OneTrans performance (~2× compute saving). Fits steeper compute–AUC scaling law (α=0.118 vs 0.071 for OneTrans).
- **Abstract**: Transformer-based CTR models face a growing bottleneck at the residual connection. DeRes addresses Pre-Norm signal dilution, inability to forget, and single-layer view limitations.

---

## 2. AI/Agents

### 2.1 ATLAS: Scaffold-Free Algorithm Synthesis by LLMs via Embedding-Guided Quality-Diversity Search
- **Authors**: Danial Yazdani et al.
- **Affiliation**: Not specified
- **arXiv**: [2608.15546](https://arxiv.org/abs/2608.15546) — cs.AI, cs.NE
- **Key Innovation**: Embedding-guided quality-diversity framework for scaffold-free full-algorithm synthesis in combinatorial optimization. Problem specification supplies objectives and constraints; LLM chooses and restructures components, interactions, and control flow. Three-layer search: best design refinement, cross-region synthesis. Across four NP-hard problems, outperforms state-of-the-art component-synthesis methods.
- **Abstract**: Most LLM-based automated algorithm design methods optimize a designated component within a human-specified scaffold. ATLAS enables full-algorithm synthesis.

### 2.2 Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents
- **Authors**: Tianxin Wei et al.
- **Affiliation**: Not specified
- **arXiv**: [2608.15071](https://arxiv.org/abs/2608.15071) — cs.AI, cs.CL
- **Key Innovation**: Context-to-harness skill compilation distills noisy, single-shot executions into reusable skill harnesses for cross-domain and topic-level adaptation. Evaluates across five realistic benchmarks (TerminalBench2, SWE-bench, CL-Bench, WebArena-Infinity). Demonstrates how LLM agents can learn on the fly.
- **Abstract**: Learning from experience is critical for developing capable, self-improving LLM agents. Evo-Harness addresses online harness learning.

### 2.3 Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents
- **Authors**: Sagar Jose et al.
- **Affiliation**: Not specified
- **arXiv**: [2608.14109](https://arxiv.org/abs/2608.14109) — cs.AI, cs.LG, cs.MA
- **Key Innovation**: Graph-based framework where a single small language model is trained via RL to specialize at each node of a recovery graph. Each node has a precise role: drift classification, operation detection, risk evaluation, or final decision. Training combines rule-based structural rewards with LLM-as-judge semantic-quality signal. Plug-and-play recovery module for main agent.
- **Abstract**: Autonomous LLM agents remain vulnerable to runtime behavioral drift. This work targets a plug-and-play recovery module.

---

## 3. ML/Efficiency

### 3.1 SchurQuant: Groupwise Discrete Optimization for Layer-Wise LLM Quantization
- **Authors**: Gunjun Lee et al.
- **Affiliation**: Not specified
- **arXiv**: [2608.15567](https://arxiv.org/abs/2608.15567) — cs.LG
- **Key Innovation**: SCHUROPT analytically eliminates the suffix's optimal continuous response, yielding an exact groupwise quadratic with Schur-complement curvature. Alternates closed-form row-wise scale/zero-point refitting with coordinate descent over integer codes. Improves mean zero-shot accuracy on 2-bit Qwen3-4B by 11.88 percentage points. SCHURQUANT combines SCHUROPT with quantized-prefix teacher reconstruction.
- **Abstract**: Weight-only post-training quantization enables deployment under tight memory budgets, but accuracy often collapses at 2-3 bits.

### 3.2 Comparative Analysis of Low-Rank Adaptation in Large Language Models versus Dense Embedding Regression for Headline CTR Prediction
- **Authors**: Not specified
- **Affiliation**: Not specified
- **arXiv**: [2608.11912](https://arxiv.org/abs/2608.11912) — cs.IR
- **Key Innovation**: Rigorous comparative evaluation of LOLA-Qwen (0.6B) fine-tuned via LoRA against Dense Embedding Regression for headline CTR prediction. Formulates headline selection as "Winner-Take-All" classification. Embedding Regression achieves 42.79% Top-1 Accuracy vs LLM's 35.70%. Suggests lightweight discriminative models offer superior calibration and efficiency for high-velocity scoring tasks.
- **Abstract**: Optimizing digital content headlines to maximize CTR is a pivotal challenge. This paper compares generative vs discriminative approaches.

---

## Cross-Cutting Trends

1. **CTR Scaling Paradigms Evolve**: LoopCTR introduces loop scaling (parameter reuse), DeRes optimizes residual connections, and GRAB demonstrates LLM-inspired generative CTR. All three push beyond traditional layer stacking.

2. **Unified Relevance-CTR Frameworks**: PRECTR-V2 shows that integrating search relevance and CTR prediction with LLM-distilled encoders can improve both ranking quality and calibration.

3. **Agent Self-Improvement**: Evo-Harness and ATLAS demonstrate different approaches to agent self-improvement — skill compilation vs full-algorithm synthesis.

4. **Quantization Breakthroughs**: SchurQuant's 11.88pp improvement at 2-bit suggests we're approaching practical deployment thresholds for extreme quantization.

5. **Small vs Large LLM Tradeoffs**: The headline CTR comparison (42.79% vs 35.70%) shows that task-specific discriminative models can outperform fine-tuned LLMs for certain applications.

---

*Generated: 2026-08-19*
*Source: arXiv cs.AI, cs.LG, cs.CL, cs.IR, stat.ML*
