---
title: "arXiv Daily — 2026-07-06"
type: synthesis
created: 2026-07-06
updated: 2026-07-06
tags: [arxiv, survey, llm, recommendation, ctr, time-series, games, reasoning, efficiency, moe]
---

# arXiv Daily Report — 2026-07-06

A curated survey of recent papers across AI, LLMs, recommendation, advertising, CTR prediction, time-series modeling, games/RL, architectures, and efficiency.

---

## 1. LLM Reasoning & Test-Time Compute

### TTT-NTP: Test-Time Training with Next-Token Prediction
- **Link**: [2606.21803](https://arxiv.org/abs/2606.21803)
- **Authors**: Xuan Ouyang, Zefan Cai, Junjie Hu
- **Institution**: — 
- **Key Innovation**: Drop-in fast weight adaptation for pretrained LLMs using the model's own next-token prediction signal at test time. Consistently improves RULER Full-13 across Llama-3.1-8B (+3.9), Mistral-7B-v0.3 (+3.0), Qwen3-4B (+4.1), Qwen3-0.6B (+2.9). +5.6 on LongBench-v2 for Llama-3.1-8B. No backbone redesign needed.

### LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents
- **Link**: [2606.18388](https://arxiv.org/abs/2606.18388)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: LLM agents search training trajectories via tree search, diagnosing pathologies at each checkpoint and proposing coordinated multi-parameter transitions. Improves over base model by 9%–140% relative and over grid search by 6%–15% across 4 GRPO tasks. Key finding: capacity parameters accumulate monotonically while regularization parameters oscillate.

### PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.1253.pdf)
- **Authors**: Jingcheng Hu et al.
- **Institution**: —
- **Key Innovation**: Massive parallel exploration via message-passing architecture. An 8B model reaches 94.5% on HMMT 2025, surpassing GPT-5's 93.2%, by scaling effective TTC to ~2M tokens. End-to-end RL training.

### T² Scaling Laws: Test-Time Scaling Makes Overtraining Compute-Optimal
- **Link**: [2604.01411](https://arxiv.org/abs/2604.01411)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Jointly optimizes model size, training tokens, and inference samples under end-to-end budgets. Finding: when accounting for inference cost, optimal pretraining shifts radically into the overtraining regime (beyond Chinchilla-optimal).

### TRACE: Efficient Test-Time Scaling via Temporal Reasoning Aggregation
- **Link**: [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.651/)
- **Authors**: Jiakun Li et al.
- **Institution**: —
- **Key Innovation**: Training-free early exit using temporal aggregation of answer consistency and confidence trajectory. Reduces reasoning tokens by 25–30% while maintaining accuracy within 1–2% of full-length reasoning.

### ThinkBooster: Unified Framework for Seamless Test-Time Scaling
- **Link**: [2606.06915](https://arxiv.org/abs/2606.06915)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Modular library + benchmark + deployable OpenAI-compatible proxy for TTC scaling. Unifies multi-sample generation, verifier reranking, and adaptive reasoning.

### Adaptive Test-Time Compute Allocation via Constrained Policy Optimization
- **Link**: [2604.14853](https://arxiv.org/abs/2604.14853)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Formalizes TTC allocation as constrained optimization (max accuracy s.t. budget). Lagrangian relaxation → per-instance oracle → lightweight classifier. Up to 12.8% relative accuracy improvement on MATH under matched budget.

### Seer Self-Consistency: Advance Budget Estimation for Adaptive Test-Time Scaling
- **Link**: [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.2120.pdf)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: System 1 (fast entropy) → System 2 (dynamic self-consistency). Up to 47% token reduction and 43% latency reduction via parallel generation.

### Parallel Test-Time Scaling for Latent Reasoning Models
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.2069.pdf)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: First work enabling parallel TTS for latent reasoning models (continuous-space). Introduces Monte Carlo Dropout + Additive Gaussian Noise for sampling, and a Latent Reward Model for trajectory selection.

### Agentic Transformers Provably Learn to Search via Reinforcement Learning
- **Link**: [2606.00183](https://arxiv.org/abs/2606.00183)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Theoretical proof that transformers learn DFS via policy gradient under depth-wise curriculum. Two-head attention mechanism: one tracks previous actions, other detects failures and triggers backtracking.

### RKSC: Reasoning-Aware KV Cache Sharing and Confident Early Exit
- **Link**: [2606.09937](https://arxiv.org/abs/2606.09937)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Training-free inference acceleration for multi-branch reasoning. Semantic KV cache sharing (ASKS) + confidence-gated early exit (CGEE). Mean 3.0× speedup, 1.66× over vLLM prefix caching. Error rate only 0.37%.

### T-STAR: Tree-structured Self-Taught Agent Rectification
- **Link**: [2604.07165](https://arxiv.org/abs/2604.07165)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Consolidates RL trajectories into a Cognitive Tree, enabling Introspective Valuation + In-Context Thought Grafting. Surgical Policy Optimization with Bradley-Terry loss at critical divergence points.

---

## 2. LLM Training & Data

### CuratorKIT: Data Curation and Synthetic Data Generation for LLM Post-Training
- **Link**: [2606.21631](https://arxiv.org/abs/2606.21631)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Open-source Python library covering the full lifecycle: ingestion, deduplication, synthetic generation, quality filtering. 8 LLM-powered generation tasks, 3 quality gates, hallucination verification with provenance chains. Compatible with TRL, Unsloth, AlignTune.

### From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning
- **Link**: [2606.17682](https://arxiv.org/abs/2606.17682)
- **Authors**: Chao Chen et al.
- **Institution**: —
- **Key Innovation**: Closed-loop framework where LLM autonomously redesigns RL training environments based on rollout feedback. Uses MAPF-FrozenLake as testbed.

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Link**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Self-play framework where models play multi-turn zero-sum games against improving versions of themselves. Up to 10% improvement across 8 reasoning benchmarks on Qwen3 and Llama families. Role-conditioned advantage estimation (RAE) for multi-agent stability.

---

## 3. LLM Architectures & Efficiency

### HydraHead: Head-Level Functional Heterogeneity to Specialized Attention Hybridization
- **Link**: [2606.20097](https://arxiv.org/abs/2606.20097)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Hybridizes full attention (FA) and linear attention (LA) at the head granularity (vs. layer-wise). Interpretability-driven head selection. Achieves 69% improvement over baseline at 512K context with only 15B training tokens. Approaches Qwen3.5 quality.

### MiniMax Sparse Attention (MSA)
- **Link**: [2606.13392](https://arxiv.org/abs/2606.13392)
- **Authors**: MiniMax
- **Institution**: MiniMax
- **Key Innovation**: Blockwise sparse softmax attention with ultra-lightweight Index Branch. Exp-free TopK kernel + KV-outer order execution for practical GPU speedups. Designed for broad GPU architecture compatibility.

### Hyperloop Transformers
- **Link**: [2604.21254](https://arxiv.org/abs/2604.21254)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Looped transformer with hyper-connections at loop level. Outperforms depth-matched Transformers with ~50% fewer parameters at 240M–2B scale. Gains persist through quantization.

### The Recurrent Transformer: Greater Effective Depth and Efficient Decoding
- **Link**: [2604.21215](https://arxiv.org/abs/2604.21215)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Each layer attends to KV pairs from its own activations (layerwise recurrent memory). Exact tiling algorithm reduces HBM traffic from Θ(N²) to Θ(N log N). Fewer layers needed at fixed parameter count, reducing KV cache.

### Tapered Language Models
- **Link**: [2606.23670](https://arxiv.org/abs/2606.23670)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Monotonically taper parameter-bearing components (heads, KV-dim, MLP width, experts) across depth under fixed budget. Cosine decay schedule consistently improves perplexity across 4 architectures (Transformer, Gated Attention, Hope-attention, Titans) at 440M–1.3B.

### SpanNorm: Reconciling Training Stability and Performance in Deep Transformers
- **Link**: [2601.22580](https://arxiv.org/abs/2601.22580)
- **Authors**: Chao Wang et al.
- **Institution**: —
- **Key Innovation**: Resolves PreNorm vs. PostNorm dilemma with spanning residual + PostNorm-style normalization. Maintains bounded signal variance, prevents gradient issues and representation collapse.

### Manifold-Geometric Transformer (MGT)
- **Link**: [2601.01014](https://arxiv.org/abs/2601.01014)
- **Authors**: Haoran Su, Chenyu You
- **Institution**: —
- **Key Innovation**: Geometric framework: manifold-constrained hyper-connections + deep delta learning (non-monotonic erasure). Prevents rank collapse in ultra-deep networks. Theoretical prediction for >100-layer Transformers.

### Sparse Growing Transformer (SGT)
- **Link**: [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.307.pdf)
- **Authors**: Yao Chen et al. (CAS & Baidu)
- **Institution**: CAS / Baidu
- **Key Innovation**: Training-time sparse depth allocation via progressive attention looping on informative heads. Follows deep-to-shallow maturation trajectory. Reduces additional FLOPs from 16–20% to only 1–3% vs. standard Transformer.

### Complementary Attention Head Pruning (CAHP)
- **Link**: [2606.19150](https://arxiv.org/abs/2606.19150)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Graph-theoretic head pruning using clustering + information-theoretic distance. Automatically determines sparsity via diminishing marginal returns. Avoids "proximity bias" of gradient methods.

---

## 4. Mixture-of-Experts (MoE) Efficiency

### OmniMoE: Orchestrating Atomic Experts at Scale
- **Link**: [2602.05711](https://arxiv.org/abs/2602.05711)
- **Authors**: Jingze Shi et al.
- **Institution**: —
- **Key Innovation**: Vector-level Atomic Experts with Cartesian Product Router (O(√N) routing). Expert-Centric Scheduling converts scattered lookups into dense operations. 10.9× speedup over PEER. 1.7B active params achieve 50.9% zero-shot accuracy.

### FRI-MxMoE: Profiling-Free Mixed-Precision Quantization for MoE
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.982.pdf)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Replaces exhaustive expert-wise profiling with Fuzzy Rule Interpolation from sparse anchor samples. 15.7× faster profiling on DeepSeek-V2 with comparable accuracy.

### CodeQuant: Unified Clustering and Quantization for MoE
- **Link**: [2604.10496](https://arxiv.org/abs/2604.10496)
- **Authors**: —
- **Institution**: NYU
- **Key Innovation**: Jointly optimizes quantization and codebook clustering. Absorbs weight outliers into cluster centroids. Up to 4.15× speedup across Phi-Mini-MoE, Qwen3-30B-A3B, DeepSeek-V2-Lite, Mixtral.

### AlphaQ: Calibration-Free Bit Allocation for MoE Quantization
- **Link**: [2606.04980](https://arxiv.org/abs/2606.04980)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Uses Heavy-Tailed Self-Regularization (HT-SR) theory to allocate bit-widths based on weight spectral properties. No calibration data needed. Near full-precision accuracy at 3.5 bits on Qwen1.5-MoE. 4× memory compression.

### MoBiE: Inference of Mixture of Binary Experts
- **Link**: [2604.06798](https://arxiv.org/abs/2604.06798)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: First binarization framework for MoE. Joint SVD to reduce cross-expert redundancy + Hessian-guided importance + null-space expert-shift mitigation. On Qwen3-30B-A3B: 52.2% PPL reduction, 43.4% zero-shot improvement, 2× speedup.

### ASET: Adaptive Skipping for Faster MoE Inference
- **Link**: [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.2140.pdf)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Adaptive per-token expert activation using router confidence + entropy. Static skipping yields 10–78% throughput gains on fine-grained MoEs, including ≥10% on DeepSeek-V3 without measurable loss.

### Replicate-and-Quantize (R&Q): Load Balancing for SMoE
- **Link**: [2602.19938](https://arxiv.org/abs/2602.19938)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Replicate heavy-hitter experts + quantize less important ones within original memory budget. Up to 1.4× reduction in load imbalance, accuracy within ±0.6%. Training-free.

### KBVQ-MoE: KLT-guided SVD with Bias-Corrected VQ for MoE
- **Link**: [2602.11184](https://arxiv.org/abs/2602.11184)
- **Authors**: Zukang Xu et al.
- **Institution**: —
- **Key Innovation**: KLT-guided SVD extracts dominant weight components shared across experts + bias-corrected output stabilization. 3-bit Qwen1.5-MoE reaches 67.99 accuracy vs. FP16 68.07.

---

## 5. CTR Prediction & Recommendation

### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR
- **Link**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Dual-path residual (Identity + Block Attention Residual) with vector-wise gating. SiLU-based Pointwise AttnRes for multi-interest patterns. Outperforms 12 baselines on 331M-interaction industrial dataset. 1.66× steeper compute–AUC scaling law vs. OneTrans.

### DS-MLP: Dual-Stream MLP is All You Need for CTR
- **Link**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Two-stream MLP architecture for feature interaction in CTR. Alternative to transformer-based approaches.

### EST: Efficiently Scalable Transformer for CTR
- **Link**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Authors**: Mingyang Liu et al. (Taobao)
- **Institution**: Alibaba / Taobao
- **Key Innovation**: Lightweight Cross Attention (LCA) + Content Sparse Attention (CSA) for fully unified sequence modeling without lossy aggregation. Stable power-law scaling. Deployed on Taobao: +3.27% RPM, +1.22% CTR.

### CADET: Context-Conditioned Ads CTR with Decoder-Only Transformer
- **Link**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: David Pardoe et al.
- **Institution**: —
- **Key Innovation**: Decoder-only transformer for ads CTR with context conditioning.

### DAIAN: Deep Adaptive Intent-Aware Network for CTR in Trigger-Induced Recommendation
- **Link**: [2602.13971](https://arxiv.org/abs/2602.13971)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Models user intent as preference distribution relative to trigger item. Hybrid ID + semantic similarity enhancer. Three-stage training strategy for convergence.

### IDProxy: Cold-Start CTR with Multimodal LLMs (Xiaohongshu)
- **Link**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors**: Yubin Zhang et al. (Xiaohongshu)
- **Institution**: Xiaohongshu
- **Key Innovation**: MLLM-generated proxy embeddings aligned with ID embedding space. End-to-end optimized under CTR objectives. Successfully deployed in Content Feed and Display Ads at Xiaohongshu.

### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Link**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Generates user interest shifts via cohort intent learning for CTR prediction.

---

## 6. Generative Recommendation (Industrial)

### OneRanker: Unified Generation and Ranking (Tencent Weixin)
- **Link**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Authors**: — (Tencent)
- **Institution**: Tencent
- **Key Innovation**: Value-aware multi-task decoupling + coarse-to-fine target awareness + K/V pass-through. Deployed on Weixin Channels advertising. GMV-Normal +1.34%.

### UniVA: Unified Value Alignment for Generative Recommendation (Tencent)
- **Link**: [2605.05803](https://arxiv.org/abs/2605.05803)
- **Authors**: — (Tencent)
- **Institution**: Tencent
- **Key Innovation**: Commercial SID tokenizer + Generation-as-Ranking SID Decoder with eCPM-aware RL + value-guided beam search. 37% offline HR@100 improvement, 1.5% GMV lift online.

### UniSID: End-to-End Semantic ID Generation for Generative Ad Recommendation
- **Link**: [2602.10445](https://arxiv.org/abs/2602.10445)
- **Authors**: Jie Jiang et al.
- **Institution**: —
- **Key Innovation**: End-to-end joint optimization of embeddings and SIDs (vs. two-stage RQ). Multi-granularity contrastive learning. Up to 4.62% HR improvement.

### GEM-Rec: One Model, Two Markets — Bid-Aware Generative Recommendation
- **Link**: [2603.22231](https://arxiv.org/abs/2603.22231)
- **Authors**: Yanchen Jiang et al.
- **Institution**: —
- **Key Innovation**: Control tokens decouple ad decision from item selection. Bid-aware decoding with allocation monotonicity guarantee.

### Gryphon: Unified SID Generation and Item-Level Scoring
- **Link**: [2606.08604](https://arxiv.org/abs/2606.08604)
- **Authors**: — (Industrial Music Platform)
- **Institution**: —
- **Key Innovation**: Jointly trained item-level scoring alongside SID generation. Replaces 15+ candidate generators + preranking stage. +3.7% Recall@1000 over vanilla GR.

### GenRec: Preference-Oriented Generative Framework (JD)
- **Link**: [2604.14878](https://arxiv.org/abs/2604.14878)
- **Authors**: — (JD)
- **Institution**: JD
- **Key Innovation**: Page-wise NTP + asymmetric Token Merger (2× input compression) + GRPO-SR with hybrid rewards. Deployed on JD: +9.5% clicks, +8.7% transactions.

### UniRec: Bridging Expressive Gap via Chain-of-Attribute (Shopee)
- **Link**: [2604.12234](https://arxiv.org/abs/2604.12234)
- **Authors**: — (Shopee)
- **Institution**: Shopee
- **Key Innovation**: Chain-of-Attribute prefixes SID with structured attribute tokens. Capacity-constrained SID + conditional decoding context. Deployed on Shopee: +5.37% PVCTR, +4.76% orders, +5.60% GMV.

### GFlowGR: Fine-tuning Generative Recommendation with GFlowNet (Taobao)
- **Link**: [2506.16114](https://arxiv.org/abs/2506.16114)
- **Authors**: — (Alibaba/Taobao)
- **Institution**: Alibaba / Taobao
- **Key Innovation**: GFlowNet-based fine-tuning with trajectory sampler + reward model. Deployed across all Taobao search advertising since May 2025. Driving 1% relative annual revenue increase at billion-dollar scale.

---

## 7. Time Series Foundation Models

### Timer-S1: Billion-Scale Time Series Foundation Model with Serial Scaling
- **Link**: [2603.04791](https://arxiv.org/abs/2603.04791)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: 8.3B MoE model (0.75B active) with Serial-Token Prediction (STP). TimeBench corpus with 1T time points. SOTA on GIFT-Eval leaderboard (best MASE and CRPS).

### Falcon-X: Time Series Foundation Model for Heterogeneous Multivariate Modeling
- **Link**: [2605.27286](https://arxiv.org/abs/2605.27286)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Unified Prototype Diff-Attention (captures synergistic + antagonistic variate relationships) + Latent Entity Attention. 591M encoder-only. Zero-shot structural transfer across domains.

### EIDOS: Latent-Space Predictive Learning for Time Series Foundation Models
- **Link**: [2602.14024](https://arxiv.org/abs/2602.14024)
- **Authors**: Xinxing Zhou et al.
- **Institution**: —
- **Key Innovation**: Shifts pretraining from future value prediction to latent-space predictive learning. Causal Transformer predicts evolution of latent representations. SOTA on GIFT-Eval.

### Chronicle: Multimodal Foundation Model for Joint Language and Time Series
- **Link**: [2605.20268](https://arxiv.org/abs/2605.20268)
- **Authors**: Paul Quinlan et al.
- **Institution**: —
- **Key Innovation**: First model jointly pretrained on text and time series from scratch (324M decoder-only). Matches Gemma 3-270M on 19 NLU tasks. SOTA frozen-embedding time series classification on 24 UCR/UEA datasets.

### Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis
- **Link**: [2607.01918](https://arxiv.org/abs/2607.01918)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Tuning-free TS foundation model.

### Time Series as Language: A Universal Tokenizer for General-Purpose TS Foundation Models
- **Link**: [2606.09861](https://arxiv.org/abs/2606.09861)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Universal tokenizer converting time series into language-like tokens for general-purpose TS foundation models.

### Revisiting the Generic Transformer: Strong Baseline for TS Foundation Models
- **Link**: [2602.06909](https://arxiv.org/abs/2602.06909)
- **Authors**: Yunshi Wen et al.
- **Institution**: —
- **Key Innovation**: Standard patch Transformer achieves SOTA zero-shot forecasting with straightforward training. Comprehensive ablation on scaling, data, and training techniques.

### Instruction-Conditioned In-Context Time Series Foundation Model
- **Link**: [2603.22586](https://arxiv.org/abs/2603.22586)
- **Authors**: Anish Saha, Konstantin Shmakov
- **Institution**: —
- **Key Innovation**: Quantile-regression T5 encoder-decoder with structured tokenization and hierarchical Transformer. Multi-task training (forecasting, imputation, classification, anomaly detection). Outperforms strong baselines on fev-bench and GIFT-Eval.

---

## 8. Games, RL, and Multi-Agent

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Link**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Adapted PPO with turn-level critic for VLM agents in Super Mario Land (100+ turns). 3× average game progress over frontier models. Cross-game generalization.

### Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Link**: [2604.17696](https://arxiv.org/abs/2604.17696)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Reasoning Transferability Coefficient (φ) + Reasoning Evolution Reward (ψ) to reinforce abstract, adaptive patterns in game self-play. Transfers to math reasoning.

### Generative Gamer (GenGamer): Learning Equilibrium Strategy by LLM-driven Dynamic Deduction
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.574/)
- **Authors**: Yadong Zhang et al.
- **Institution**: —
- **Key Innovation**: Trains LLMs to generate compact, pruned reasoning trajectories (Dynamic Deduction) using action/state/branch pruning. Deduction Tree Reward for step-level feedback. Surpasses SOTA LMs on Tic-Tac-Toe and Leduc Poker.

### Augmenting Game AI with Deep Reinforcement Learning
- **Link**: [2606.20210](https://arxiv.org/abs/2606.20210)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Practical deployment of player-facing RL-augmented game AI. Covers real-world considerations.

### Fluid-Agent Reinforcement Learning
- **Link**: [2602.14559](https://arxiv.org/abs/2602.14559)
- **Authors**: Shishir Sharma, Doina Precup, Theodore J. Perkins
- **Institution**: —
- **Key Innovation**: Framework for agents that can create other agents (fluid-agent environments).

---

## 9. LLM Agents & Skills

### OpenClaw-Skill: Collective Skill Tree Search for Agentic LLMs
- **Link**: [2606.16774](https://arxiv.org/abs/2606.16774)
- **Authors**: —
- **Institution**: —
- **Key Innovation**: Tree-search-based skill construction for real-world agent tasks. Addresses skill fragmentation, limited diversity, and weak transferability in long-horizon environments.

### OpenClaw-RL & related (Claw-style persistent runtimes)
- **Link**: —
- **Authors**: Multiple (ByteDance, Nous Research, etc.)
- **Institution**: Multiple
- **Key Innovation**: Persistent runtimes with interfaces, sessions, tools, and structured workspace state for real-world LLM agent deployment.

---

## 10. Notable Trends & Themes

1. **Test-time compute is the new scaling axis**: A flood of work on TTC scaling (PaCoRe, T² laws, ThinkBooster, TRACE, RKSC, SeerSC) — the field is moving beyond pure pretraining scaling.
2. **Generative recommendation goes industrial**: OneRanker (Tencent), GenRec (JD), UniRec (Shopee), GFlowGR (Taobao) — all deployed in production, proving GR as the next paradigm.
3. **MoE efficiency is a hot topic**: 8+ papers on MoE quantization, binarization, load balancing, and pruning (CodeQuant, AlphaQ, MoBiE, FRI-MxMoE, ASET, R&Q, KBVQ-MoE, OmniMoE).
4. **Attention hybridization matures**: HydraHead (head-level), MiniMax Sparse Attention, Hyperloop, Recurrent Transformer — all aiming to break the quadratic bottleneck.
5. **CTR prediction scales like LLMs**: DeRes, EST show scaling laws in CTR with billion-parameter-class transformer backbones deployed in production.
6. **Time Series Foundation Models diversify**: From pure forecasting (Timer-S1, Falcon-X) to multimodal (Chronicle) to latent-space (EIDOS).

---

*Generated 2026-07-06. Papers sourced from arXiv, ACL 2026 proceedings, and related venues. Links to arXiv abstracts; full PDFs accessible via arxiv.org/pdf/{id}.*
