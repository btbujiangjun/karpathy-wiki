---
title: "arXiv Paper Check — AI & CTR (June 13, 2026)"
type: synthesis
created: 2026-06-13
updated: 2026-06-13
sources: [arxiv.org/list/cs.AI/new, arxiv.org/list/cs.IR/new, arxiv.org/list/cs.LG/new]
tags: [arxiv, daily, ai, ctr, recommendation, attention, rl, diffusion, molecular, retrieval]
---

# arXiv Paper Check — AI & CTR (June 13, 2026)

> **Saturday quiet day** — arXiv does not process new submissions on weekends. This report covers the Fri Jun 12 batch, focusing on papers not fully covered in the Jun 12 report.

---

## 🧠 AI / LLM / Agents

### 1. Strategic Decision Support for AI Agents
- **Authors**: Shayan Kiyani, Sima Noorani, George Pappas, Hamed Hassani
- **Link**: [2606.12587](https://arxiv.org/abs/2606.12587)
- **Key contribution**: Reverses classical decision support — AI agents act, humans support. Framework minimizes support usage while controlling counterfactual missed-support error (probability agent acts alone where support would materially improve output). Optimal policy is threshold rule on value of support. Online algorithm with adaptive thresholding and randomized exploration — no distributional assumptions. Demonstrated on information gathering, human-AI collaboration, and tool use.

### 2. TrajGenAgent — Hierarchical LLM Agent for Human Mobility Trajectory Generation
- **Authors**: Siyu Li, Toan Tran et al.
- **Link**: [2606.12657](https://arxiv.org/abs/2606.12657)
- **Key contribution**: Two-stage orchestrator-worker design without model fine-tuning. LLM synthesizes activity chains via in-context learning; deterministic workflow grounds activities into visits using personalized POI retrieval, distance-aware location selection, kinematics-aware travel-time propagation. Introduces anomaly-detection-based evaluation framework for behavioral and semantic plausibility.

### 3. PersonaDrive — Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving
- **Authors**: Mahmoud Srewa et al.
- **Link**: [2606.12616](https://arxiv.org/abs/2606.12616)
- **Key contribution**: Conditions VLA driving agent on retrieved demonstrations from style-instructed human driving dataset (aggressive/neutral/conservative). Offline triplet mining + lightweight retrieval head + single VLA backbone. No per-style retraining. Driving score +4.6% over SimLingo, +2.5% over HiP-AD. Speed/acceleration rise 18%/25% conservative→aggressive.

### 4. Did You Lie? — Evaluating Lie Detectors across Model Scale (2B—1T)
- **Authors**: Alan Cooney, David Africa, Geoffrey Irving
- **Link**: [2606.12618](https://arxiv.org/abs/2606.12618)
- **Key contribution**: 13 reasoning model organisms with verified hidden beliefs. Four detectors evaluated (CoT judge, logprob classifier, activation probes, DYL). All detectors scale positively with model capability on prompted lying. But activation/logprob detectors drop sharply on trained model organisms. Only CoT judge remains strong (0.82 balanced accuracy). Current lie detectors cannot support high-confidence claims.

### 5. Rethinking Psychometric Evaluation of LLMs — Self-Reports vs Behavior
- **Authors**: Rafal Kocielnik et al. (Caltech)
- **Link**: [2606.12730](https://arxiv.org/abs/2606.12730)
- **Key contribution**: Contrasts Big 5 with Theory of Planned Behavior (TPB). TPB reaches human-level coherence within a shared conversation; Big 5 does not. Across separate conversations, coherence survives only for behaviors anchored outside the immediate prompt (implicit bias) and collapses when behavior is context-primed (sycophancy). Persona prompting makes SR more consistent but does not align behavior.

### 6. The Containment Gap — Deployed Agentic AI Frameworks Fail Safety
- **Authors**: Md Jafrin Hossain et al.
- **Link**: [2606.12797](https://arxiv.org/abs/2606.12797)
- **Key contribution**: Audits LangChain, AutoGPT, OpenAI Agents SDK — no native compliance with six containment principles. Memory integrity absent in all three. Empirical: single memory-poisoning write in government benefits agent increases wrongful denial rate to 88.9%. Lightweight validator + policy gate eliminate attacks with <0.2ms overhead.

### 7. Deployment-Centered Evaluation — Query-Level Rejection Risk in Clinical LLM
- **Authors**: Alyssa Unell et al. (Stanford)
- **Link**: [2606.12702](https://arxiv.org/abs/2606.12702)
- **Key contribution**: Pre-response classifier predicts user rejection risk using deployment-specific context (provider type, department, model) + query content. AUROC 0.719 over 4.5 months. Deployment context improves prediction over query content alone. Enables targeted guardrail triggering and abstention.

### 8. Teach-and-Repeat — Mobile GUI Agent from Demonstrations (Honor)
- **Authors**: Yudong Zhang et al. (Honor Device Co.)
- **Link**: [2606.12817](https://arxiv.org/abs/2606.12817)
- **Key contribution**: Teach VLM translates mobile screen trajectories into step-wise operational knowledge. Data flywheel for scalable training. Consistent Task Success Rate improvements for downstream GUI agents in Android World.

---

## 📊 CTR / Recommendation / Retrieval

### 1. OneRetrieval — Editable Generative Retrieval at Kuaishou Scale
- **Authors**: Xuxin Zhang, Ben Chen et al. (Kuaishou)
- **Link**: [2606.13533](https://arxiv.org/abs/2606.13533)
- **Key contribution**: One-model generative retrieval replacing multi-branch pipeline. Keyword-Aligned Encoding (KAE) ties identifier positions to interpretable attribute words — reserved slots bind new terms post-deployment without retraining. Six codebook groups with non-uniform capacity via information-theoretic merging. Online: replacing inverted-index branch significantly lifts order volume; extending to nearly the entire stage holds conversion while improving CTR. Hundreds of millions PVs daily.

### 2. HiGR — Hierarchical Generative Slate Recommendation at Tencent (v5 update)
- **Authors**: Yunsheng Pang et al. (Tencent)
- **Link**: [2512.24787](https://arxiv.org/abs/2512.24787)
- **Key contribution**: Prefix-Contrastive Residual Quantized VAE (PCRQ-VAE) for structured semantic IDs. Hierarchical Slate Decoder shifts from token-level to coarse-grained preference embeddings. ORPO-based listwise alignment for ranking fidelity, user interest, diversity. 5× inference speedup. Online: +1.22% watch time, +1.73% video plays. Deployed on multiple Tencent platforms.

### 3. Helmsman — Cost-Effective ANNS at RedNote/Xiaohongshu (OSDI'26)
- **Authors**: Yuchen Huang, Baiteng Ma et al. (RedNote/Xiaohongshu)
- **Link**: [2606.13145](https://arxiv.org/abs/2606.13145)
- **Key contribution**: Clustering-based ANNS on all-flash servers — userspace storage stack avoids kernel I/O overhead, leveling-learned pruning module adapts strategy, GPU-accelerated pipeline for billion-scale index rebuilds in hours. Saves 90%+ hardware costs. 40 machines replace ~35,000 cores + 0.35 PB DRAM.

### 4. Versioned Late Materialization for Ultra-Long Sequences (Meta, v2 update)
- **Authors**: Liang Guo, Ge Song et al. (Meta)
- **Link**: [2604.24806](https://arxiv.org/abs/2604.24806)
- **Key contribution**: Eliminates data redundancy in "Fat Row" paradigm for DLRM training. Stores UIH once in normalized immutable tier, reconstructs just-in-time via versioned pointers. O2O consistency protocol prevents future leakage across streaming and batch. Disaggregated preprocessing keeps training compute-bound. Foundational infra for HSTU and ULTRA-HSTU.

---

## 🔬 cs.LG Highlights

### 1. RoVE — Rotary Value Embeddings Attention
- **Authors**: Alejandro García-Castellanos, Maurice Weiler, Erik J Bekkers
- **Link**: [2606.11275](https://arxiv.org/abs/2606.11275)
- **Key contribution**: Parameter-free modification making values position-sensitive by rotating them simultaneously with keys. Turns RoPE attention into attentive convolution — unifies independent formulations across vision, robotics, and LLM architectures. Trained 124M/354M GPT-2 models show consistent gains on few-shot ICL, OOD perplexity, and long-context retrieval.

### 2. FlowBank — Query-Adaptive Agentic Workflow Optimization
- **Authors**: Lingzhi Yuan, Chenghao Deng et al.
- **Link**: [2606.11290](https://arxiv.org/abs/2606.11290)
- **Key contribution**: Three-stage framework: DiverseFlow (diversify candidate pool), CuraFlow (compress to compact portfolio), Matching (query-workflow bipartite graph routing). No per-query regeneration cost. +4.26% over strongest automated baselines, +14.92% over handcrafted.

### 3. BlendIn — Inference-Time Alignment with Probabilistic Model Blending
- **Authors**: Jin Gan, Xin Li, Jun Luo
- **Link**: [2606.11201](https://arxiv.org/abs/2606.11201)
- **Key contribution**: Quality-aware alignment — shifts from binary intervention decisions to hybrid distributions. Proportionally weights each model's contribution based on reliability. Up to 50% performance improvement on challenging model pairs.

### 4. GLACIER — Multimodal Student-Teacher Foundation Model for Molecular Property Prediction
- **Authors**: Emily Nguyen et al.
- **Link**: [2606.11382](https://arxiv.org/abs/2606.11382)
- **Key contribution**: Three-modality student (molecular graphs, SMILES, physicochemical descriptors) with Finsler geometry-aware fusion. Distills from MiniMol and MolFormer teachers via contrastive learning. Lightweight, high predictive performance.

### 5. ProHiFlo — Hierarchical Flow Matching for De Novo Protein Generation
- **Authors**: Chuanzhen Wang et al.
- **Link**: [2606.11243](https://arxiv.org/abs/2606.11243)
- **Key contribution**: Coarse-to-fine generation (backbone → all-atom), functional guidance via pretrained predictors, adaptive SE(3)-equivariant architecture. 4× fewer sampling steps. 58.9% success rate on enzyme active site scaffolding vs 41.2% for RFDiffusion.

### 6. Least-Action-Guided Diffusion for Physical Extrapolation
- **Authors**: Zhongxin Yang et al.
- **Link**: [2606.11277](https://arxiv.org/abs/2606.11277)
- **Key contribution**: Two-stage: conditional score-based diffusion generates in-distribution proposal, then action-based variational prior refines toward OOD condition. Turns least-action principle into differentiable inference-time correction. Reduces phase drift, preserves dissipative decay across ODE/PDE systems.

### 7. Loss Landscape Diagnosis for Gray-Scott System Inversion
- **Authors**: Yan Yang
- **Link**: [2606.11258](https://arxiv.org/abs/2606.11258)
- **Key contribution**: Backpropagates through unrolled PDE simulation — optimization fails due to flat plateaus aligning with bifurcation boundaries. Disentangles PINN components: residual loss alone avoids the pathology by implicitly encoding full PDE dynamics across all initial conditions. Neural network serves only to complete observed data.

### 8. Learning from Almost Nothing — Neural Networks Survive Heavy Input Corruption
- **Authors**: Justin Tahmassebpur et al.
- **Link**: [2606.11319](https://arxiv.org/abs/2606.11319)
- **Key contribution**: Infinite-width analysis in heavy-corruption regime. Leading-order decision rule is nearest-class-mean (prototype rule) — universal across depth, activation functions, noise distributions. Explains why >90% corrupted inputs still yield above-chance accuracy.

### 9. Energy-Conserved Neural Pipelines
- **Authors**: David Young, Swan Yi Htet
- **Link**: [2606.11341](https://arxiv.org/abs/2606.11341)
- **Key contribution**: Enforces squared L2 norm conservation at every module boundary. At noise σ=0.2: 77.4% clean accuracy vs 35.1% baselines, 30.9% energy-penalized. Conserved noise energy strictly less than input noise energy (formal bound).

### 10. SwiftCTS — Fast Clock Tree Pareto Optimization via Few-Shot Calibration
- **Authors**: Barsat Khadka et al.
- **Link**: [2606.11348](https://arxiv.org/abs/2606.11348)
- **Key contribution**: Physics-informed surrogate with gradient-boosted ensembles — trains in <5s on CPU. K-shot calibration reduces OOD power error 24.5%→3.3%, wirelength 56.6%→<1%. Evaluates 100K CTS configurations in <10s. Closed-loop validation <0.5% error.

### 11. FreeBridge — Variational Schrödinger Bridges for Cellular Transition Dynamics
- **Authors**: Xurui Wang et al.
- **Link**: [2606.11286](https://arxiv.org/abs/2606.11286)
- **Key contribution**: Schrödinger Bridge formulation for single-cell perturbation modeling under endpoint-only supervision. Atomic states as instance-segmented single-cell representations. Empirical latent support regularization constrains transport within cellular manifold.

---

## 📈 Trends

1. **Agent safety maturity**: Strategic Decision Support, Prefill Awareness, Containment Gap, and lie detection all address agent eval validity
2. **Generative retrieval production**: OneRetriever (Kuaishou) and HiGR (Tencent) prove generative approaches at industrial scale
3. **Attention innovation**: RoVE unifies RoPE + value rotation into attentive convolution — simple, parameter-free, consistent gains
4. **Physics-AI intersection**: Least-Action-Guided Diffusion, Energy-Conserved Pipelines, Loss Landscape Diagnosis — growing trend of embedding physical laws into architectures by construction
5. **CTR data infra**: Versioned Late Materialization shows sequence length scaling is increasingly a data infrastructure problem
6. **Inference-time alignment**: BlendIn and FlowBank both shift optimization from train-time to inference-time adaptation
