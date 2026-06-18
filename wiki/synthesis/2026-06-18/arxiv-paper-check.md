---
title: "arXiv Paper Check — AI & CTR (June 18, 2026)"
type: synthesis
created: 2026-06-18
updated: 2026-06-18
sources: []
tags: [arxiv, ai, ctr, recommendation, llm, survey]
---

# arXiv Paper Check — AI & CTR (June 18, 2026)

> Papers submitted June 17, 2026. Coverage: cs.AI, cs.LG, stat.ML, CTR/IR/RecSys. ~15 selected highlights from ~90 new submissions.

## 🧠 LLM Architectures & Training

### 1. Looped World Models (LoopWM)
- **arXiv**: 2606.18208
- **Authors**: Hongyuan Adam Lu et al.
- **Key idea**: First looped architectures for world modelling — iteratively refines latent states through a parameter-shared transformer block. Achieves up to 100x parameter efficiency over conventional approaches. Establishes iterative latent depth as a new scaling axis.

### 2. Fixed-Point Reasoners (FPRM)
- **arXiv**: 2606.18206
- **Authors**: Sajad Movahedi et al. (ETH Zurich)
- **Key idea**: Transformer-based fixed-point reasoning model using fixed-point convergence as end-to-end halting mechanism. Adaptive compute scales depth to task difficulty. Effective on Sudoku, Maze, state-tracking, ARC-AGI.

### 3. FoMoE: Federation of MoEs
- **arXiv**: 2606.19025
- **Authors**: Lorenzo Sani et al.
- **Key idea**: Breaks full-replica paradigm by partitioning expert layers across workers for geographically distributed LLM training. Reduces communication costs up to 45.44x vs DDP. Novel skip-token mechanism achieves 1.4x throughput speedup.

### 4. Diffusion-Proof: Formal Theorem Proving with Diffusion LLMs
- **arXiv**: 2606.19315
- **Authors**: Ruida Wang et al.
- **Key idea**: First framework applying diffusion LLMs to formal theorem proving. *dLLM-Prover-7B* for whole-proof writing + *dLLM-Corrector-7B* for local proof correction. Solves one IMO problem that DeepSeek-Prover-V2-7B could not.

### 5. Complementary Attention Head Pruning (CAHP)
- **arXiv**: 2606.19150
- **Authors**: Yaniv Livertovsky et al.
- **Key idea**: Post-hoc graph-theoretical framework for attention head pruning. Uses graph-based clustering + information-theoretic distance to preserve topologically diverse heads. Automatically determines sparsity level. Accepted at IJCNN 2026.

### 6. Essential Subspace Merging (ESM)
- **arXiv**: 2606.19164
- **Authors**: Longhua Li et al.
- **Key idea**: Training-free multi-task model merging via essential subspace decomposition. Orthogonalizes task updates and fuses essential components. ESM++ extends to dynamic routing with low-rank experts.

### 7. Explaining Attention with Program Synthesis
- **arXiv**: 2606.19317
- **Authors**: Amiri Hayes, Belinda Li, Jacob Andreas (MIT)
- **Key idea**: Generates Python programs that reproduce attention patterns. <1,000 programs reproduce GPT-2/TinyLlama/Llama-3B attention with >75% IoU. Replacing 25% of heads with programmatic surrogates incurs only 16% perplexity increase.

### 8. Smoothness-Based Derandomization of PAC-Bayes Bounds
- **arXiv**: 2606.19105
- **Authors**: Alexandre Lemire Paquin et al.
- **Key idea**: Generalization bounds for deterministic predictors exploiting smoothness. Bounds involve Jacobian/Hessian flatness quantities. Practical regularizer derived for BatchNorm networks.

### 9. Safety Reflection Pretraining
- **arXiv**: 2606.19168
- **Authors**: Jinhan Li et al.
- **Key idea**: Inserts short safety reflections into pretraining corpora. Improves safety classification + reduces attack success rates vs data filtering/rewriting. Synthetic MedSafetyWorld environment for controlled experiments.

### 10. Compute Efficiency and Serial Runtime Tradeoffs for Stochastic Momentum Methods
- **arXiv**: 2606.19179
- **Authors**: Depen Morwani et al.
- **Key idea**: Theoretical analysis of HB/ASGD batch-size tradeoffs. HB preserves SGD-level compute efficiency over larger batch window (factor √κ larger). ASGD shows spectrum-dependent behavior with power-law spectra.

### 11. Wasserstein Policy Learning for Distributional Outcomes
- **arXiv**: 2606.19117
- **Authors**: Yiyan Huang et al.
- **Key idea**: Offline policy learning with distribution-valued outcomes. Wasserstein barycenter rewards. Finite-sample regret bounds. Accepted at COLT 2026.

## 📊 Recommendation Systems & CTR

### 12. JourneyFormer: Encoding Airbnb Guest Journey with Sequence Modeling
- **arXiv**: 2606.19108
- **Authors**: Daochen Zha et al. (Airbnb)
- **Key idea**: Production sequence model for Airbnb search ranking. Covers guest event selection, ID embeddings, label attribution, training/inference acceleration. Deployed in production with A/B gains across 2 surfaces. **Accepted at KDD 2026.**

### 13. Querit-Reranker: Compact Multilingual Rerankers
- **arXiv**: 2606.19037
- **Authors**: Yunfei Zhong et al.
- **Key idea**: Label-free distribution adaptation for multilingual cross-encoder rerankers. Uses synthetic-query mining with soft labels + spherical linear interpolation merging. MoE backbone (0.4B activated) improves nDCG@10 from 54.11→59.28 on BEIR. 4B variant achieves SOTA on MTEB Multilingual v2.

### 14. Strategic Feature Selection
- **arXiv**: 2606.18867
- **Authors**: Jivat Neet Kaur et al. (UC Berkeley/MIT)
- **Key idea**: Formal study of strategic classification through feature selection + ridge regularization. Shows excluding features by manipulability alone is suboptimal. Practical algorithm for joint feature set + regularization level selection. Healthcare payments benchmark case study.

### 15. Stochastic MoE Discontinuities (SMoE Geometry)
- **arXiv**: 2606.19036
- **Authors**: Tho Tran Huu et al.
- **Key idea**: Rigorous geometric/stochastic analysis of discontinuities in sparse MoEs. Classifies by order, establishes volume estimates. Proposes smoothing mechanism with minimal overhead. **ICML 2026 Spotlight.**

## 🔬 Other Notable

### Giskard: Byzantine Robust and Confidential Aggregation
- **arXiv**: 2606.19129
- **Authors**: Ousmane Touat et al.
- **Key idea**: Tree of committees protocol for decentralized learning — secure MPC-based approximate median. Reduces per-party communication asymptotically. Handles up to n/4 Byzantine parties. Scales to 1M participants.

### ViGOS: Visually Grounded OPSD for MLLMs
- **arXiv**: 2606.19120
- **Authors**: Sihan Wang et al.
- **Key idea**: Decouples perception and reasoning in multimodal self-distillation. Student writes visual description before reasoning. Image-only teacher supervises description; privileged teacher supervises reasoning. Improves image-grounded behavior in shortcut-prone settings.

### Quantifying and Auditing LLM Evaluation via PU Learning
- **arXiv**: 2606.19057
- **Authors**: Zilong Zhang et al.
- **Key idea**: Formulates LLM-as-judge evaluation under selective human supervision as positive-unlabeled learning. Geometric auditing framework using partial optimal transport corrects biased judges without retraining.

---

## Key Themes

1. **Looped/depth-adaptive architectures** — LoopWM, FPRM, and FoMoE all explore iterative refinement as a new scaling axis
2. **Post-hoc efficiency** — CAHP (pruning), ESM (merging), Querit-Reranker (compression) all aim to compress/optimize already-trained models
3. **Production RecSys at scale** — JourneyFormer (Airbnb) shows practical sequence modeling for ranking with real A/B impact
4. **Safety alignment during pretraining** — Safety Reflection Pretraining challenges the "filter/rewrite" paradigm
5. **Diffusion beyond generation** — Diffusion-Proof applies dLLMs to formal theorem proving with non-trivial results
