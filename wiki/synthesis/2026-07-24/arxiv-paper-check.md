---
title: "arXiv Paper Check — 2026-07-24"
type: synthesis
created: 2026-07-24
updated: 2026-07-24
sources: []
tags: [arxiv, ai, ctr, recommendation, agents, reasoning, sequential-modeling]
---

# arXiv Paper Check — 2026-07-24

> Automated search across arXiv for recent papers in AI and CTR (Click-Through Rate) categories from the last 24 hours.
> Categories: cs.AI (354 new Jul 24), cs.IR (20 new Jul 24), cs.LG (263 new Jul 24).

---

## 1. CTR Prediction & Ranking

### 1.1 BARGE: Bridging the Structural Gap for Autoregressive Generation in Recommendation
- **Authors**: Junchao Zeng, Junzhang Zhu, Junyang Chen, Yudong Li, Wei Liu, Chengxiang Zhuo, Zang Li (Tencent)
- **Date**: 24 Jul 2026
- **Abstract**: Addresses two structural gaps in generative recommendation with hierarchical Semantic IDs: (1) flattening multi-token IDs destroys item-level structure, and (2) training/inference inconsistency causes semantic drift. Proposes Item Context-Aware Attention (ICA) to restore item structure during encoding, and Hierarchical Path Reranking (HPR) with Dual-Path Decoding (DPD) to suppress drift during decoding. Online A/B test on Tencent platform: +0.60% CTR, +1.34% click-unique-visitors, +1.70% total reading time.
- **Key Innovations**: ICA for item-level structure restoration; HPR+DPD for semantic drift suppression; end-to-end validated in production.
- **Impact**: First production-validated fix for structural gaps in generative recommendation with semantic IDs.

### 1.2 LO-FAR: Cost-Aware Local Filter for Sparse Feature Ranking in Industrial Ad Recommendation
- **Authors**: Egemen Erbayat, Luis Duque, Sohini Roychowdhury, Mohammad Amin, Srihari Reddy (RecSys 2026)
- **Date**: 24 Jul 2026
- **Abstract**: Proposes a CPU-only, model-agnostic workflow for ranking sparse high-cardinality ID-list features in ad recommendation. Uses lightweight local estimators instead of GPU-bound retraining loops. On production dataset with 1M+ interactions and 475 sparse features, completes ranking in ~2 CPU-hours while preserving Normalized Entropy gains on CTR/CVR tasks competitive with shuffle-based importance and Binary Stochastic Neurons across budgets of 100-400 retained features.
- **Key Innovations**: CPU-only feature ranking; local held-out estimators; cost-constrained production workflow.
- **Impact**: Practical production tool for feature engineering when GPU compute budgets are limited.

### 1.3 DLMRec: Diffusion Language Model for Recommendation
- **Authors**: Chengyi Liu, Yongqi Zhou, Junwei Pan, Zhixiang Feng, Chengguo Yin, Haijie Gu, Jie Jiang, Yinghao Liu, Yujuan Ding, Qing Li, Wenqi Fan
- **Date**: 24 Jul 2026
- **Abstract**: Proposes DLMRec, a discrete diffusion language model for recommendation as an alternative to autoregressive generation. Introduces collaborative-aware stochastic tokenizer encoding multi-hop collaborative signals, curriculum-driven training aligning denoising with preference recovery, and stability-aware voting for robust generation. Argues that next-token objectives emphasize sequential order over structural inter-item dependencies.
- **Key Innovations**: Discrete diffusion for generative recommendation; collaborative-aware tokenizer; curriculum denoising.
- **Impact**: Challenges the autoregressive dominance in generative recommendation; first diffusion-based approach for rec.

### 1.4 PRL: Probabilistic Residual Learning for Online Recommendations
- **Authors**: Wenyuan Wang, Yusong Zhao, Zihao Xu, et al. (RecSys 2026)
- **Date**: 24 Jul 2026
- **Abstract**: A causal Bayesian recommendation model that models the residual between ground-truth and base predictions. Probabilistically groups users for localized residual modeling, models domain-level confounders, and aggregates cluster-specific residual predictions using do-calculus. Plug-and-play compatible with various base deep learning recommender systems.
- **Key Innovations**: Causal residual modeling; probabilistic user clustering; do-calculus aggregation; plug-and-play compatibility.
- **Impact**: Principled causal approach to improving existing recommender systems without architectural changes.

### 1.5 SalesLoop: RL from Performance Feedback for Sales Lead Ranking
- **Authors**: Chenyu Zhang
- **Date**: 24 Jul 2026
- **Abstract**: Proposes a reinforcement learning framework for CRM lead ranking with a closed feedback loop between predictions and real-world outcomes. Introduces performance-aware reward weighted by ranking position and conversion velocity, and Discriminative GRPO for listwise optimization. 160-day production A/B test at a New Energy Vehicle manufacturer (16.5M leads, 280 sales specialists): +4.7% (p=0.047) and +8.7% (p=0.002) cumulative lift. Top-10% recall of 44.1% and 2.3x conversion rate vs. specialist baselines.
- **Key Innovations**: Performance-aware reward for RL; Discriminative GRPO; closed-loop production feedback.
- **Impact**: First production-validated RL system for B2B sales lead ranking with statistical significance.

---

## 2. AI Agents & Safety

### 2.1 ATM: Autonomous Topology Mutation for Multi-Agent LLM Systems
- **Authors**: Bronislav Sidik, Chaya Levi, Nizzan Kimhi
- **Date**: 24 Jul 2026
- **Abstract**: Introduces runtime team-mutation for multi-agent LLM frameworks. Combines telemetry-driven overload detection (six-signal Bottleneck Index: queue depth, context thrash, tool-error rate, role entropy, retry-loop rate, cross-agent wait time) with three safety invariants: capability monotonicity, state-routing completeness, and shadow-before-live validation. On 720 DeepSeek-V3-driven tasks, factoriser split lifts code-task success from 3.3% to 61.7%. Runtime rails add <500μs p99 latency.
- **Key Innovations**: Runtime topology mutation; six-signal Bottleneck Index; three safety invariants; privacy-level-aware routing.
- **Impact**: First system to enable dynamic agent restructuring at runtime with provable safety guarantees.

### 2.2 Robust Critics: Defending LLMs Against Multi-Turn Attacks
- **Authors**: Roman Belaire, Arunesh Sinha, Pradeep Varakantham
- **Date**: 24 Jul 2026
- **Abstract**: Proposes Dialogue Critic Guided Sampling (DCGS) for inferring user intent at every turn of adversarial dialogue. Models adversarial dialogue as MDP with value and regret-based critics at token and utterance levels. Proves inference-time reweighting approximates exponential tilting, guaranteeing improvement for any finite candidate pool. Outperforms strong baselines on CARES-18k, WildJailbreak, Redbench, and Harmbench. Transfers to frontier models without fine-tuning.
- **Key Innovations**: Per-turn intent inference; dual-level critics (token + utterance); theoretical improvement guarantee; transferability.
- **Impact**: Moves beyond contextual bandit safety to full trajectory-level adversarial defense.

### 2.3 DCGS: Multi-Turn Safety via Markov Decision Process Formulation
- **Authors**: (overlaps with 2.2)
- **Impact**: Demonstrates that multi-turn attacks require fundamentally different defense mechanisms than single-turn safety.

### 2.4 VeriSimpl: Robust Optimization Modeling from Natural Language
- **Authors**: Sumaya Abdul Rahman et al. (ICML 2026)
- **Date**: 24 Jul 2026
- **Abstract**: A solver-LLM framework for robust natural-language-to-optimization formalization using simplification-based verification. Leverages the optimization solver to generate simplified diagnostic queries, allowing the LLM to tractably reason about formulation correctness.
- **Key Innovations**: Simplification-based verification; solver-LLM feedback loop; high-precision self-verification signal.
- **Impact**: Bridges NL understanding with formal optimization verification.

### 2.5 PhantomFill: When Forms Cause LLM Hallucination
- **Authors**: Rana Muhammad Usman
- **Date**: 24 Jul 2026
- **Abstract**: Shows that required JSON fields cause 100% fabrication in 10 of 13 LLMs tested. GPT-5.5 answers honestly 98% in free text but invents answers 40/40 times given required sentiment field. Explicit "insufficient evidence" option rescues only frontier models; all 9 open-weight models ignore it. Resistance does not correlate with scale. Releases PhantomFill benchmark with Coerced Fabrication Rate and Escape Utilization Rate metrics.
- **Key Innovations**: Form-caused hallucination characterization; deterministic benchmark; two reportable metrics.
- **Impact**: Reveals a widespread but undermeasured failure mode in structured LLM outputs.

---

## 3. Reasoning & Optimization

### 3.1 TRSP: Topologically Regularized Side-Path for LLM Representation Collapse
- **Authors**: Yiheng Tao, Kaiwen Cheng, Yao Lu, Chang Liu, Jie Chen (ICML 2026)
- **Date**: 24 Jul 2026
- **Abstract**: Identifies that LLMs face two pathological extremes: homogenization collapse (attention sinks) and isolation collapse (local attention). Proposes TRSP with a parameter-free Triangular Box mechanism for spectral balance between mixing efficiency and information capacity. On NoLiMa at 8x training length, retains 83% accuracy, surpassing Differential Transformer by ~30pp and Gated Attention by ~50pp.
- **Key Innovations**: Spectral analysis of attention dynamics; Triangular Box mechanism; length-aware gate; proximal coupling + distal propagation.
- **Impact**: First principled fix for representation collapse that scales to 8x training length.

### 3.2 SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales
- **Authors**: Mikail Khona et al. (NVIDIA)
- **Date**: 24 Jul 2026
- **Abstract**: Adapts SOAP and Muon optimizers to large-scale LLM pretraining. Identifies instabilities in SOAP at large batch sizes and proposes per-step QR orthogonalization. Unified empirical study with update-RMS matching for fair comparison. At batch sizes up to 100M tokens, SOAP and Muon maintain training stability while AdamW degrades. Introduces layer-wise distributed optimizer compatible with Megatron-LM.
- **Key Innovations**: Large-scale SOAP/Muon adaptation; per-step QR orthogonalization; layer-wise distributed optimizer.
- **Impact**: Makes higher-order optimizers practical for billion-parameter LLM pretraining.

### 3.3 JAXBench: Benchmarking Autonomous TPU Kernel Optimization
- **Authors**: Arya Tschand et al. (Google)
- **Date**: 24 Jul 2026
- **Abstract**: TPU-native benchmark suite with 50 JAX workloads extracted from production architectures (Llama-3.1, DeepSeek-V3, Mixtral, Mamba-2, AlphaFold2). Gemini 3 Flash achieves 37.3% per-sample correctness with curated TPU docs (vs 5.8% without). Autocomp beam-search reaches 1.36x geomean speedup over XLA, and 1.60x on hand-tuned kernels.
- **Key Innovations**: TPU-native kernel optimization benchmark; documentation-conditioned generation; Autocomp beam search.
- **Impact**: Establishes TPU kernel optimization as a measurable AI engineering task.

### 3.4 SonicSampler: Unified Tile-Aware Kernels for LLM Sampling
- **Authors**: Pragaash Ponnusamy, Shivam Sahni, Jue Wang, Tri Dao
- **Date**: 24 Jul 2026
- **Abstract**: Unified suite of tile-aware Triton kernels fusing the complete sampling pipeline (logit processing, token selection, verification) into a single batched kernel. Supports dynamic per-request sampling behaviors within CUDA Graph execution. Hierarchical two-stage top-k achieves up to 10x speedup. Across heterogeneous speculative decoding workloads, achieves up to 16x speedup over SOTA baselines.
- **Key Innovations**: Complete sampling pipeline fusion; dynamic per-request behavior; CUDA Graph compatible; hierarchical top-k.
- **Impact**: Significant inference speedup for serving systems with diverse sampling requirements.

---

## 4. Recommendation Systems

### 4.1 CCBR: Controllable and Content-Based Recommendations
- **Authors**: Fırat Öncel, Jihoon Jeong, Emiliano Penaloza, Mirco Ravanelli, Laurent Charlin, Cem Subakan
- **Date**: 24 Jul 2026
- **Abstract**: Builds recommendations from textual user profile representations with controllability via text bottlenecks. Infers text summaries directly from item contents (images, audio, video). Achieves competitive performance with latent-representation models while providing text-based multimodal interventions. Outperforms TEARS on controllable recommendation.
- **Key Innovations**: Text bottleneck for controllability; content-derived profiles; multimodal intervention mechanism.
- **Impact**: Enables user steering of recommendations through interpretable text interfaces.

### 4.2 SHIFT: Self-reconstruction Harnesses Implicit Fine-grained Thinking for Retrieval
- **Authors**: Yuxiao Luo, Da Li, Mingjie Zhang, Zhentao He, Shikun Zhang, Wei Ye
- **Date**: 24 Jul 2026
- **Abstract**: Transfers LLMs into reasoning-efficient retrievers with residual projection and bidirectional attention aggregation in latent space. Alleviates contrastive learning / implicit reasoning mismatch using fine-grained next-token-prediction-based reconstruction. Consistently outperforms widely used retrievers on reasoning-intensive retrieval benchmarks.
- **Key Innovations**: Residual projection for LLM-to-retriever transfer; fine-grained reconstruction loss; bidirectional attention aggregation.
- **Impact**: Improves reasoning-intensive retrieval without explicit chain-of-thought tokens.

### 4.3 UniRank: Benchmarking Ranking Models
- **Authors**: Honghao Li et al.
- **Date**: 24 Jul 2026 (replacement)
- **Abstract**: Open benchmark for ranking models unifying sequential modeling and feature interaction. Benchmarks 15 representative models on 5 large-scale public datasets, with the largest containing 700M+ instances and sequences exceeding 10^5 interactions. Provides PyTorch toolkit with DDP training, operator optimization, and mixed-precision support.
- **Key Innovations**: Unified benchmark; industrial-scale datasets; reproducible evaluation framework.
- **Impact**: Enables systematic comparison of next-generation ranking architectures.

---

## 5. LLM Efficiency & Inference

### 5.1 Codec-Gauge: Learning Compression-Friendly Gauges for Transformer KV Caches
- **Authors**: Yitao Jiang, Yaoqing Yang, Luyang Zhao, Muhao Chen, Devin Balkcom
- **Date**: 24 Jul 2026
- **Abstract**: Post-training cache-coordinate layer learning orthogonal channel transforms around existing compression/quantization backends. Frequency-distribution objective combines token-channel DCT spectral-centroid loss with smooth rate proxy. Reduces zfp KL divergence by 44.0% on average across six models at 3/4/6 bits/value.
- **Key Innovations**: Cache-coordinate geometry as post-training variable; DCT spectral-centroid loss; compatible with existing compression backends.
- **Impact**: Improves KV cache compression fidelity without changing model weights or attention semantics.

### 5.2 DecodeShare: Tracing the Shared Subspace of LLM Decode-Time Decisions
- **Authors**: Zishan Shao et al.
- **Date**: 24 Jul 2026
- **Abstract**: Identifies a low-dimensional subspace consistently shared across tasks in decode-time hidden states. Disturbing this shared subspace degrades performance far more than disturbing prefill-derived or random subspaces. Shared subspace serves as high-leverage causal channel at decode time for activation steering.
- **Key Innovations**: Task-general decode-time shared subspace identification; causal role validation; practical steering implications.
- **Impact**: Reveals structural organization in LLM decode-time representations with deployment implications.

### 5.3 CARGO: Training-Free LLM Offloading via Reliability Gating
- **Authors**: Evan Chen, Shiqiang Wang, Kevin S Chan, Su Wang, Christopher Brinton
- **Date**: 24 Jul 2026
- **Abstract**: Training-free routing framework for local-cloud LLM collaboration. Estimates local model agreement through prompt-varied sampling, applies Bayesian early stopping, and supports arbitrary collaboration ratios through lightweight calibration. Consistently outperforms training-free baselines and surpasses supervised learned routers in several settings.
- **Key Innovations**: Intrinsic response behavior as routing signal; Bayesian early stopping; no additional trained router.
- **Impact**: Reduces deployment overhead for local-cloud LLM collaboration.

---

## Summary

### Key Themes

1. **Generative Recommendation Gains Production Validation**: BARGE demonstrates production-validated fixes for structural gaps in generative rec with semantic IDs (+0.60% CTR on Tencent), while DLMRec challenges autoregressive dominance with diffusion-based alternatives.

2. **RL for Real-World Optimization**: SalesLoop achieves +8.7% lift in B2B sales through RL with performance-aware rewards, and DCGS applies MDP formulation to multi-turn adversarial defense.

3. **Dynamic Agent Architecture**: ATM enables runtime topology mutation with <500μs overhead, lifting agent success from 3.3% to 61.7%, suggesting that static agent architectures are a key bottleneck.

4. **Representation Collapse Fix**: TRSP achieves 83% accuracy at 8x training length via spectral regularization, addressing a fundamental limitation of current attention mechanisms.

5. **KV Cache Compression Advances**: Codec-Gauge reduces compression artifacts by 44% through learned channel transforms, while SonicSampler fuses the complete sampling pipeline for 16x speedup.

6. **Form-Induced Hallucination**: PhantomFill reveals that required JSON fields cause 100% fabrication in most LLMs, exposing a critical gap between free-text and structured output safety.

### Statistics
- **Total Papers Reviewed**: 25+
- **CTR/Recommendation**: 8 papers (3 with production A/B validation)
- **AI Agents & Safety**: 5 papers
- **Reasoning & Optimization**: 4 papers
- **Recommendation Systems**: 3 papers
- **LLM Efficiency & Inference**: 3 papers

---

*Generated on 2026-07-24*
