---
title: "arXiv Daily — June 16, 2026"
type: synthesis
created: 2026-06-16
updated: 2026-06-16
tags: [arxiv, ai, llm, recommendation, ctr, sequential-modeling, games, reinforcement-learning, diffusion, state-space-models, attention]
sources: []
---

# arXiv Daily — June 16, 2026

Papers across AI, LLMs, recommendation, advertising, CTR, sequential modeling, state-space models, games, and diffusion language models.

---

## 1. LLM Architectures & Attention

### 1.1 MiniMax Sparse Attention (MSA)
- **arXiv**: [2606.13392](https://arxiv.org/abs/2606.13392)
- **Authors**: MiniMax AI
- **Affiliation**: MiniMax
- **Abstract**: Blockwise sparse attention built on GQA. A lightweight Index Branch scores KV blocks and selects Top-k per GQA group; Main Branch does exact block-sparse attention. On a 109B MoE model, MSA matches GQA while reducing per-token attention compute by 28.4× at 1M context. Co-designed kernel achieves 14.2× prefill and 7.6× decoding speedups on H800.
- **Key Innovations**: Blockwise group-specific sparse retrieval; exp-free Top-k selection; KV-outer sparse attention for tensor-core utilization; production-grade multimodal model released.

### 1.2 Recurrent Transformer
- **arXiv**: [2604.21215](https://arxiv.org/abs/2604.21215)
- **Affiliation**: —
- **Abstract**: Each layer attends to KV pairs computed from its own activations, yielding layerwise recurrent memory while preserving standard autoregressive decoding cost. Can emulate both conventional Transformer and token-to-token recurrent updates. Exact tiling-based algorithm reduces HBM traffic from Θ(N²) to Θ(N log N). At 300M params on C4, 6-layer RT performs comparably to 12-layer Transformer.
- **Key Innovations**: Layerwise recurrent attention without breaking AR decoding; tiling algorithm for efficient training; depth-to-inference efficiency translation.

### 1.3 Sessa: Selective State Space Attention
- **arXiv**: [2604.18580](https://arxiv.org/abs/2604.18580)
- **Affiliation**: —
- **Abstract**: Places attention inside a recurrent feedback path, creating multiple attention-based paths for past tokens to influence future states. Proves power-law memory tails (O(ℓ^{-β})) with slower decay than Transformer/Mamba baselines. Only model class realizing flexible selective retrieval (including non-decaying influence profiles).
- **Key Innovations**: Attention-in-recurrent-feedback decoder design; theoretical power-law memory guarantees; selective retrieval without distance decay.

### 1.4 SparDA: Sparse Decoupled Attention
- **arXiv**: [2606.04511](https://arxiv.org/abs/2606.04511)
- **Authors**: Yaosheng Fu, Guangxuan Xiao, Xin Dong, Song Han, Oreste Villa
- **Affiliation**: NVIDIA, MIT
- **Abstract**: Decouples sparse selection from attention—a Forecast head in layer ℓ selects KV blocks for layer ℓ+1, enabling CPU-to-GPU prefetch overlap. One Forecast head per GQA group. <0.5% added params. Up to 1.25× prefill, 1.7× decode speedup, and 5.3× higher decode throughput vs. non-offload sparse baseline.
- **Key Innovations**: Lookahead sparse selection decoupled from attention query; Forecast head design; trainable via KL divergence without base model retraining.

### 1.5 AB-Sparse: Adaptive Block Size Sparse Attention
- **arXiv**: [2605.12110](https://arxiv.org/abs/2605.12110)
- **Affiliation**: —
- **Abstract**: Training-free framework that allocates different block sizes per attention head (heads vary in sensitivity to block granularity). Uses lossless block centroid quantization. Custom GPU kernels for variable block sizes. Up to 5.43% accuracy improvement over fixed-block baselines.
- **Key Innovations**: Per-head adaptive block size via calibration; lossless centroid quantization; variable-block GPU kernels.

### 1.6 STS: Speculative Token Sparsity
- **arXiv**: [2605.15508](https://arxiv.org/abs/2605.15508)
- **Affiliation**: —
- **Abstract**: Uses a smaller draft model's attention scores to build dynamic token-and-head-wise sparsity masks for a larger target model. Integrates into speculative decoding. 2.67× speedup at ~90% sparsity on NarrativeQA with negligible accuracy loss.
- **Key Innovations**: Cross-model attention correlation for mask generation; dynamic per-token granularity sparsity; no retraining required.

### 1.7 RTPurbo: Full Attention → Sparse in 100 Steps
- **arXiv**: [2605.16928](https://arxiv.org/abs/2605.16928)
- **Affiliation**: —
- **Abstract**: Shows full-attention LLMs are intrinsically sparse. Retains full KV cache only for retrieval heads; uses 16D token indexer for sparse attention; dynamic Top-p selection. Up to 9.36× prefill speedup at 1M context, 2.01× decode speedup. Only hundreds of training steps needed.
- **Key Innovations**: Head-wise retrieval/streaming specialization; low-dimensional indexer; demonstration that full-attention training + lightweight sparsification works.

### 1.8 Sparse Feature Attention (SFA)
- **arXiv**: [2603.22300](https://arxiv.org/abs/2603.22300)
- **Affiliation**: —
- **Abstract**: Explores feature-axis sparsity (not token-axis). Q/K are k-sparse codes; attention cost reduced from Θ(n²d) to Θ(n²k²/d). FlashSFA kernel avoids materializing dense score matrices. Matches dense baselines with 2.5× speedup, ~50% FLOPs/KV-cache reduction.
- **Key Innovations**: Feature-level sparsity as orthogonal axis for attention efficiency; FlashSFA IO-aware kernel for sparse overlaps.

### 1.9 Forget, Then Recall (Gist Sparse Attention)
- **arXiv**: [2604.20920](https://arxiv.org/abs/2604.20920)
- **Affiliation**: —
- **Abstract**: Interleaved gist compression tokens provide learnable summaries for sparse attention routing. Compresses context→gists→selects relevant gists→restores raw chunks for detailed attention. Hierarchical gist-of-gist for multi-resolution with log decoding complexity. Outperforms compression baselines 8×–32×.
- **Key Innovations**: End-to-end learnable bridge between compression and sparse attention; selective unfolding mechanism; recursive gist hierarchy.

### 1.10 Vortex: Programmable Sparse Attention Serving
- **arXiv**: [2606.06453](https://arxiv.org/abs/2606.06453)
- **Authors**: Zhuoming Chen, Xinrui Zhong, Qilong Feng, Ranajoy Sadhukhan, Yang Zhou et al.
- **Affiliation**: —
- **Abstract**: Python-embedded frontend + page-centric tensor abstraction for expressing diverse sparse attention algorithms. Enables rapid prototyping, deployment, evaluation. AI agents using Vortex generate algorithms reaching 3.46× higher throughput than full attention. Up to 4.7× on MLA-based GLM-4.7-Flash.
- **Key Innovations**: Sparse attention DSL; page-centric tensor abstraction; agent-driven algorithm discovery.

### 1.11 Token Sparse Attention
- **arXiv**: [2602.03216](https://arxiv.org/abs/2602.03216)
- **Affiliation**: —
- **Abstract**: Per-head token-level sparsification—compress Q,K,V to reduced token set, attend, then decompress back to original sequence. Interleaved selection across layers prevents irreversible eviction. Up to 3.23× attention speedup at 128K context with <1% degradation.
- **Key Innovations**: Compress-and-decompress design per layer; layer-wise adaptive sparsity budgets; compatible with FlashAttention.

### 1.12 Vashista: Constant-Time Sparse Attention
- **arXiv**: [2602.13804](https://arxiv.org/abs/2602.13804)
- **Affiliation**: —
- **Abstract**: Geometric framework showing attention is intrinsically sparse under mild non-degeneracy. Per-token decode reduces to O(PD + K_c D) with context-independent constants. Near-constant decode latency up to 128K on Llama-3-8B.
- **Key Innovations**: Convex-geometric theory of attention sparsity; Sparse Paged Attention; exponential leakage bound.

---

## 2. State Space Models (SSM / Mamba)

### 2.1 Mamba-3
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **Authors**: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- **Affiliation**: Carnegie Mellon, Princeton, etc.
- **Abstract**: Three innovations: (1) "exponential-trapezoidal" discretization for more expressive dynamics; (2) complex-valued state spaces for state tracking; (3) MIMO (multi-input multi-output) for improved hardware utilization. Combined into updated Mamba block.
- **Key Innovations**: Complex-valued SSM states enable non-commutative state tracking; MIMO SSM improves inference throughput; new discretization scheme.

### 2.2 Swimba: Switch Mamba (MoE-SSM)
- **arXiv**: [2603.06938](https://arxiv.org/abs/2603.06938)
- **Affiliation**: —
- **Abstract**: MoE-parameterized SSM layer preserving single-pass recurrence. Each expert produces candidate SSM streams; token-level router computes mixture weights; mixed in parameter space with single SSM evaluation. Avoids replicating expensive recurrence across experts.
- **Key Innovations**: First MoE-parameterized SSM with single-recurrence mixing; parameter-space expert aggregation.

### 2.3 Zamba2-VL
- **arXiv**: [2606.00390](https://arxiv.org/abs/2606.00390)
- **Authors**: Zyphra
- **Affiliation**: Zyphra
- **Abstract**: Vision-language models on Zamba2 hybrid architecture (Mamba2 backbone + shared transformer blocks). 1.2B, 2.7B, 7B scales. Competitive with Qwen3-VL, InternVL3.5 at respective scales while substantially faster generation and cheaper serving.
- **Key Innovations**: Hybrid Mamba2 + shared attention for VLM; LoRA-specialized shared blocks.

### 2.4 Q-Mamba: Query-based Mamba Multimodal LLM
- **arXiv**: [2606.04719](https://arxiv.org/abs/2606.04719)
- **Affiliation**: —
- **Abstract**: Learnable queries project vision information via interleaved Mamba sequencing + cross-modal attention. Eliminates heuristic 2D visual scan order; dynamically downsamples visual features.
- **Key Innovations**: Q-Former-style cross-modal projection adapted for Mamba backbone; local attention mask in Mamba sequence modeling.

### 2.5 UniMamba: Unified Spatial-Temporal Forecasting
- **arXiv**: [2604.16325](https://arxiv.org/abs/2604.16325)
- **Affiliation**: —
- **Abstract**: Hybrid framework combining Mamba VC encoding (FFT-Laplace + TCN) with Spatial Temporal Attention for multivariate forecasting.
- **Key Innovations**: Bidirectional Mamba for temporal dynamics; FFT-Laplace signal reconstruction; joint spatial-temporal attention.

---

## 3. Sequence Models — Expressivity & Theory

### 3.1 Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
- **arXiv**: [2603.08859](https://arxiv.org/abs/2603.08859)
- **Affiliation**: —
- **Abstract**: Proves pure SSMs need large internal state (linear scaling) and pure sliding-window Transformers need large window (linear scaling) for function-composition tasks. Constructs provably successful shallow hybrids with sublinear memory.
- **Key Innovations**: Rigorous expressivity lower bounds for pure SSMs and Transformers; provable success of shallow hybrids.

### 3.2 Latent Recurrent Transformer (LRT)
- **arXiv**: [2605.26797](https://arxiv.org/abs/2605.26797)
- **Affiliation**: —
- **Abstract**: Lightweight augmentation reusing high-level source-layer hidden state from previous token as recurrent memory. KV Projection + Residual Injection. Interleaved parallel training at ~2× baseline compute. Improves LM loss and ICL under matched compute.
- **Key Innovations**: Cross-token recurrent latent pathway without pausing AR; interleaved parallel training strategy.

### 3.3 Recurrent Transformer (see 1.2)

### 3.4 PCAF: Parallel Causal Associative Fields
- **arXiv**: [2606.10435](https://arxiv.org/abs/2606.10435)
- **Affiliation**: Google
- **Abstract**: Parallel content-addressed memory over causal successor records. Hash-bucket retrieval + sparse cache + learned gate with local language model. At 303M params, outperforms dense Transformer on WikiText-103 (36.31 vs 47.49 PPL) and PG-19, while processing 0.61M tokens/s vs 0.43M.
- **Key Innovations**: Third primitive beyond attention and recurrence; hash-bucket successor cache; learned mixture gate between parametric and retrieved distributions.

### 3.5 Prefix-Scannable Models (PSMs)
- **arXiv**: [2506.10918](https://arxiv.org/abs/2506.10918) (ICLR 2026)
- **Affiliation**: —
- **Abstract**: Formalizes Sequential-Parallel Duality (SPD). Generalizes prefix scan to non-associative aggregation rules. New Transformer-PSM model achieves O(1) amortized inference with O(log N) memory. Unifies Mamba, GLA, Mamba2, mLSTM, linear Transformers.
- **Key Innovations**: SPD framework; non-associative prefix scan; Transformer-PSM instantiation.

### 3.6 Why Depth Matters: A Lie Algebraic View
- **arXiv**: [2603.05573](https://arxiv.org/abs/2603.05573)
- **Affiliation**: —
- **Abstract**: Lie-algebraic framework connecting sequence model depth to tower of Lie algebra extensions. Approximation error diminishes exponentially with depth. Validated on symbolic word and state-tracking problems.
- **Key Innovations**: Lie-algebraic expressivity analysis of SSMs/Transformers; exponential error-depth scaling.

### 3.7 Sliding-Window Transformers without PE are Turing Complete
- **arXiv**: [2606.01532](https://arxiv.org/abs/2606.01532)
- **Affiliation**: —
- **Abstract**: Proves sliding-window Transformer without positional encoding is Turing complete. Window motion itself breaks permutation symmetry. Introduces HIST model (token-count histogram) for analysis.
- **Key Innovations**: Separation of positional encoding from sequential computation; HIST abstract model.

### 3.8 Padded Transformer Expressivity
- **arXiv**: [2605.30523](https://arxiv.org/abs/2605.30523)
- **Affiliation**: —
- **Abstract**: Characterizes padded transformer expressivity: constant-precision = L-uniform AC⁰, growing-precision = L-uniform TC⁰. Looping scales expressivity with circuit depth d. Robust to attention type, width, uniformity.
- **Key Innovations**: Exact circuit-complexity characterizations; looping-depth tradeoff.

### 3.9 Gecko: Long-Context Architecture
- **arXiv**: [2601.06463](https://arxiv.org/abs/2601.06463)
- **Affiliation**: —
- **Abstract**: Builds on Mega/Megalodon with timestep decay normalization, sliding chunk attention, adaptive working memory. At 7B scale, reaches loss 1.68 (vs Llama2-7B 1.75, Megalodon-7B 1.70). Handles up to 4M tokens without context-extension techniques.
- **Key Innovations**: Timestep decay normalization; sliding chunk attention; linear attention for working memory.

---

## 4. CTR Prediction & Recommendation

### 4.1 DeRes: Decoupling Residual Stability and Adaptivity for CTR
- **arXiv**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Affiliation**: —
- **Abstract**: Dual-path inter-layer connector—Identity residual path + Block Attention Residual path with vector-wise gate. Pointwise AttnRes replaces Softmax with SiLU for multi-interest forgetting. On 331M interactions industrial dataset, outperforms 12 baselines with <5% added FLOPs. 1.66× steeper compute-AUC scaling law.
- **Key Innovations**: Dual-path residual design for CTR Transformers; SiLU-based cross-layer attention for parallel interest activation; CTR scaling law analysis.

### 4.2 LoopCTR: Loop Scaling Paradigm
- **arXiv**: [2604.19550](https://arxiv.org/abs/2604.19550)
- **Affiliation**: —
- **Abstract**: Sandwich architecture (Entry→Loop→Prediction) with Hyper-Connected Residuals + MoE. Process supervision at every loop depth. Train-multi-loop, infer-zero-loop strategy matches or surpasses full multi-loop inference. Oracle analysis reveals 0.02–0.04 AUC untapped headroom.
- **Key Innovations**: Loop scaling paradigm for CTR; train-multi-loop/infer-zero-loop strategy; process supervision encoding multi-loop training into shared params.

### 4.3 EST: Efficient Scaling Laws in CTR
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Affiliation**: Alibaba (Taobao)
- **Abstract**: Efficiently Scalable Transformer for CTR unifying heterogeneous inputs. Lightweight Cross Attention (LCA) + Content Similarity Attention (CSA). Power-law scaling with model capacity. Online A/B tests: CTR +1.22%, RPM +3.27% on Taobao display advertising.
- **Key Innovations**: Domain-specific analysis of CTR vs LLM scaling differences; LCA for efficient cross-feature interaction; CSA for sparse long-behavior modeling.

### 4.4 SparseCTR
- **arXiv**: [2601.17836](https://arxiv.org/abs/2601.17836)
- **Affiliation**: —
- **Abstract**: Three-branch sparse self-attention for long-term user behaviors: global interests, interest transitions, short-term interests. Composite relative temporal encoding via learnable head-specific bias coefficients. Online: CTR +1.72%, CPM +1.41%. Scaling law across 3 OOM FLOPs.
- **Key Innovations**: Personalized chunk segmentation; three-branch sparse attention for multi-scale interests; head-specific temporal encoding.

### 4.5 GRAB: Generative Ranking for Ads at Baidu
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: Baidu
- **Affiliation**: Baidu
- **Abstract**: LLM-inspired end-to-end generative CTR framework. Causal Action-aware Multi-channel Attention (CamA). Full-scale deployment: revenue +3.05%, CTR +3.49%. Linear scaling with longer interaction sequences.
- **Key Innovations**: Sequence-first generative paradigm for CTR; CamA for temporal dynamics + action signals; monotonic scaling with sequence length.

### 4.6 IDProxy: Cold-Start CTR with MLLMs
- **arXiv**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors**: Xiaohongshu
- **Affiliation**: Xiaohongshu
- **Abstract**: Multimodal LLM generates proxy embeddings from content signals for cold-start items, aligned with existing ID embedding space. Optimized end-to-end under CTR objectives. Deployed on Content Feed and Display Ads at Xiaohongshu.
- **Key Innovations**: MLLM-based proxy embedding aligned to ID space; end-to-end cold-start CTR optimization.

### 4.7 GenCI: Generative User Intent Framework
- **arXiv**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Affiliation**: —
- **Abstract**: Generative model (NTP objective) produces candidate interest cohorts as explicit intent representations. Hierarchical candidate-aware network refines cohorts via cross-attention. Captures interest shifts beyond discriminative paradigms.
- **Key Innovations**: Generative (NTP-based) interest cohort modeling; bridging recall-stage context to ranking.

### 4.8 RankUp: High-rank Representations for Advertising
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Affiliation**: Tencent (Weixin)
- **Abstract**: Addresses embedding collapse in deep MetaFormer-based rankers. Randomized permutation splitting, multi-embedding paradigm, global token integration. Deployed on Weixin Video Accounts/Moments/Official Accounts: GMV +3.41%/+4.81%/+2.12%.
- **Key Innovations**: Representation collapse analysis for ranking models; permutation splitting for feature diversity; production-scale validation.

### 4.9 DAIAN: Deep Adaptive Intent-Aware Network
- **arXiv**: [2602.13971](https://arxiv.org/abs/2602.13971)
- **Affiliation**: —
- **Abstract**: For Trigger-Induced Recommendation—extracts intent representations from trigger-click correlation; hybrid ID+semantic similarity enhancer with adaptive selection. Addresses "intent myopia."
- **Key Innovations**: Intent-aware adaptation in trigger-induced recommendation; hybrid semantic+ID similarity.

### 4.10 LLaCTR: Lightweight LLM-enhanced CTR
- **arXiv**: [2505.14057](https://arxiv.org/abs/2505.14057) (WWW '26)
- **Affiliation**: —
- **Abstract**: Field-level enhancement paradigm—uses LLMs for self-supervised field-feature fine-tuning, distills semantic knowledge to enhance feature representation and interaction. 10–100× less compute than other LLM-enhanced methods.
- **Key Innovations**: Field-level (not instance-level) LLM enhancement; self-supervised field-feature fine-tuning.

### 4.11 Memento: RAG-Style Long-Retention for Ads
- **arXiv**: [2605.24051](https://arxiv.org/abs/2605.24051)
- **Affiliation**: Meta
- **Abstract**: Treats user history as document corpus, ad requests as queries. MMR retrieval balances similarity + diversity. Representation Memento + Data Memento. 5–10× resource efficiency over linear scaling. Sub-10ms latency. CTR +1%, CVR +1.2% on Facebook Feed/Reels.
- **Key Innovations**: RAG framing for user history scaling; dual representation/data memento; production 365-day retention.

---

## 5. Advertising Ranking & Generative Recommendation

### 5.1 CADET: Context-Conditioned Ads Decoder-Only Transformer
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Affiliation**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR. Context-conditioned decoding with multi-tower heads (resolves position chicken-and-egg); self-gated attention; timestamp RoPE; session masking. LinkedIn deployment: CTR +11.04% vs LiRank.
- **Key Innovations**: Context-conditioned decoding architecture for post-scoring signals; self-gated attention; timestamp-based RoPE.

### 5.2 CaliCausalRank: Calibrated Multi-Objective Ad Ranking
- **arXiv**: [2602.18786](https://arxiv.org/abs/2602.18786)
- **Affiliation**: —
- **Abstract**: Integrates training-time scale calibration, Lagrangian constraint optimization, variance-reduced counterfactual estimation. Score calibration as first-class training objective. AUC +1.1%, calibration error -31.6%, utility +3.2%.
- **Key Innovations**: Training-time calibration (not post-hoc); robust counterfactual utility for offline evaluation.

### 5.3 OneRanker: Unified Generation and Ranking
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Affiliation**: Tencent (WeiXin)
- **Abstract**: Value-aware multi-task decoupling (task token sequences + causal mask); coarse-to-fine target awareness (Fake Item Tokens); KV pass-through + Distribution Consistency loss. Deployed on WeiXin Channels: GMV +1.34%.
- **Key Innovations**: Architectural fusion of generation and ranking; value-aware decoupling; distribution consistency constraint.

### 5.4 GR4AD: Generative Recommendation for Advertising
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Affiliation**: —
- **Abstract**: UA-SID (Unified Advertisement Semantic ID from fine-tuned MLLM); LazyAR decoder (relaxes layer-wise AR); VSL + RSPO (ranking-guided preference optimization); Dynamic Beam Serving. Up to 4.6% improvement over strong baseline.
- **Key Innovations**: MLLM-derived semantic IDs for ads; lazy autoregressive decoder; list-wise ranking-guided RL for online learning.

### 5.5 GPR: Generative Pre-trained Recommender
- **arXiv**: [2511.10138](https://arxiv.org/abs/2511.10138)
- **Affiliation**: Tencent (Weixin)
- **Abstract**: First one-model framework formulating advertising recommendation as end-to-end generative task. RQ-Kmeans+ tokenization; dual-decoder (HHD); Multi-Token Prediction + Value-Aware Fine-Tuning + HELD. Deployed on Weixin Channels with significant GMV/CTCVR improvement.
- **Key Innovations**: Fully generative one-model paradigm for ads; hierarchy-enhanced policy optimization; multi-token prediction.

### 5.6 LLM-HYPER: LLMs as Hypernetworks for Cold-Start CTR
- **arXiv**: [2604.12096](https://arxiv.org/abs/2604.12096)
- **Affiliation**: (Top US e-commerce platform)
- **Abstract**: LLM as hypernetwork generating linear CTR estimator weights via few-shot CoT over multimodal ad content. CLIP retrieval for similar past campaigns. NDCG@10 +55.9% over cold-start baselines. Successfully deployed in production.
- **Key Innovations**: Weight generation (not score prediction) via LLM; training-free parameter generation; production cold-start deployment.

---

## 6. Diffusion Language Models

### 6.1 Quokka: Scaling Laws for Diffusion LMs
- **arXiv**: [2510.03280](https://arxiv.org/abs/2510.03280)
- **Affiliation**: —
- **Abstract**: First large-scale scaling law for DLMs covering compute-constrained and data-constrained regimes. Ablates transition kernels, diffusion schedules, loss formulations, optim hyperparameters. Shows DLMs have different scaling coefficients from AR models.
- **Key Innovations**: Comprehensive scaling law study for DLMs; optimal allocation rules for compute/data/params.

### 6.2 OPDLM: AR-to-Diffusion via On-Policy Distillation
- **arXiv**: [2606.06712](https://arxiv.org/abs/2606.06712)
- **Affiliation**: —
- **Abstract**: Converts ARLMs to DLMs via on-policy distillation—student DLM samples reverse trajectories, trained on token-level targets from frozen ARLM teacher. 15×–7000× fewer tokens than established DLMs.
- **Key Innovations**: Post-training ARLM→DLM conversion; on-policy distillation without DLM teacher pretraining; extreme data efficiency.

### 6.3 FLARE: Diffusion for Hybrid Language Models
- **arXiv**: [2606.01774](https://arxiv.org/abs/2606.01774)
- **Affiliation**: —
- **Abstract**: Studies AR-to-diffusion post-training for hybrid-attention backbones. Token-balanced clean/noisy loss combining AR NTP with block diffusion. First to join dLLM thread with hybrid architecture thread.
- **Key Innovations**: Joint AR + diffusion training for hybrid backbones; mask/objective design for capability preservation.

### 6.4 LoopMDM: Looped Masked Diffusion
- **arXiv**: [2605.26106](https://arxiv.org/abs/2605.26106)
- **Affiliation**: —
- **Abstract**: Selectively looping early-middle transformer layers in MDMs. Matches same-size MDMs with 3.3× fewer training FLOPs; up to +8.5 points on GSM8K. Adaptive loop count at inference for compute scaling.
- **Key Innovations**: Layer looping for depth-scaling in MDMs; training/inference compute flexibility; attention analysis showing masked-position interaction.

### 6.5 Accelerating Masked Diffusion Training
- **arXiv**: [2605.13026](https://arxiv.org/abs/2605.13026)
- **Affiliation**: —
- **Abstract**: Identifies locality bias as main cause of slow MDM training. Proposes bell-shaped time sampling (focus on middle timesteps). Up to 4× faster NLL convergence on LM1B. Scales to billion-param CPT setting.
- **Key Innovations**: Training speed analysis for MDMs; bell-shaped time sampling; generalizes to ARM-initialized CPT.

### 6.6 Continuous Diffusion Scales Competitively
- **arXiv**: [2605.18530](https://arxiv.org/abs/2605.18530)
- **Affiliation**: —
- **Abstract**: RePlaid—continuous diffusion aligned with modern discrete DLM architecture. First unified scaling comparison: continuous gap narrows to ~20× compute vs AR (previous belief was much larger). Competitive with discrete DLM scaling.
- **Key Innovations**: Fair architecture alignment between continuous and discrete DLMs; revised scaling comparison.

### 6.7 Cola DLM: Hierarchical Continuous Latent Diffusion
- **arXiv**: [2605.06548](https://arxiv.org/abs/2605.06548)
- **Affiliation**: —
- **Abstract**: Text VAE → block-causal DiT in latent space → conditional decoding. Separates global semantic organization from local textual realization. Verified at ~2B scale with scaling curves up to ~2000 EFLOPs.
- **Key Innovations**: Hierarchical (latent→token) generation; block-causal DiT for latent prior; Markov-path interpretation.

### 6.8 TextLDM: Language Modeling with Continuous Latent Diffusion
- **arXiv**: [2605.07748](https://arxiv.org/abs/2605.07748)
- **Affiliation**: —
- **Abstract**: Continuous VAE latent space + DiT. REPA alignment with frozen LLM. Scaling from 114M to 768M shows consistent improvements across MAUVE, ROUGE-1. 2–13× faster sampling than competing methods.
- **Key Innovations**: REPA-aligned latent space for text diffusion; scaling analysis for latent DiT; serving efficiency.

### 6.9 Scaling Beyond Masked Diffusion
- **arXiv**: [2602.15014](https://arxiv.org/abs/2602.15014)
- **Affiliation**: —
- **Abstract**: First scaling law study of uniform-state and interpolating discrete diffusion. MDLM can be 12% more FLOPs-efficient with cross-entropy objective. Uniform-state diffusion (Duo) outperforms AR/MDLM on GSM8K at 1.7B despite worse perplexity. Challenges perplexity as cross-algorithm metric.
- **Key Innovations**: Cross-family scaling comparison; low-variance training objective for MDLM; Pareto frontier analysis (speed vs quality).

---

## 7. Games & Reinforcement Learning

### 7.1 Odysseus: Scaling VLMs to 100+ Turn Games
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Affiliation**: —
- **Abstract**: RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Adapted PPO with lightweight turn-level critic. 3× average game progress over frontier models. Cross-game generalization.
- **Key Innovations**: Turn-level critic PPO for long-horizon VLM agents; pretrained VLM action priors; open training framework.

### 7.2 MemoPilot: RL over Memory for Game Agents
- **arXiv**: [2606.08656](https://arxiv.org/abs/2606.08656)
- **Affiliation**: —
- **Abstract**: Plug-in memory copilot training memory update process via multi-turn GRPO. Turn-wise rewards + context-independent advantage estimation. Ranked #1 Elo on LHE (1762) and RPS (1590), outperforming DeepSeek-V3.2.
- **Key Innovations**: Memory update as multi-turn decision problem; multi-turn GRPO training; plug-in design for frozen LLMs.

### 7.3 Resource-Efficient Model-Free RL for Board Games
- **arXiv**: [2602.10894](https://arxiv.org/abs/2602.10894)
- **Authors**: Kazuki Ota, Takayuki Osa, Motoki Omura, Tatsuya Harada
- **Affiliation**: Univ. of Tokyo / RIKEN
- **Abstract**: Model-free RL algorithm for board games (Animal Shogi, Gardner Chess, Go, Hex, Othello). More efficient learning than search-based methods (AlphaZero). Extensive ablation study.
- **Key Innovations**: Efficient model-free approach challenging search-based dominance; comprehensive multi-game validation.

### 7.4 AI Gamestore: Open-Ended Evaluation
- **arXiv**: [2602.17594](https://arxiv.org/abs/2602.17594)
- **Authors**: Lance Ying, Ryan Truong, Prafull Sharma, Kaiya Ivy Zhao, Nathan Cloos, Kelsey R. Allen, Thomas L. Griffiths, Katherine M. Collins, José Hernández-Orallo, Phillip Isola, Samuel J. Gershman, Joshua B. Tenenbaum
- **Affiliation**: MIT, Princeton, Cambridge, etc.
- **Abstract**: Platform using LLMs + human-in-the-loop to synthesize representative human games. Generated 100 games from Apple App Store / Steam top charts. Best VLMs achieved <10% of human average score on most games.
- **Key Innovations**: "Multiverse of Human Games" evaluation paradigm; LLM-based game synthesis; multi-VLM benchmark.

### 7.5 PokéAgent Challenge
- **arXiv**: [2603.15563](https://arxiv.org/abs/2603.15563)
- **Affiliation**: —
- **Abstract**: Large-scale benchmark (20M+ battle trajectories) with Battling Track (strategic reasoning under partial observability) and Speedrunning Track (long-horizon planning). NeurIPS 2025 competition with 100+ teams. Pokémon battling nearly orthogonal to standard LLM benchmarks.
- **Key Innovations**: Multi-agent battle + RPG speedrunning benchmark; large-scale trajectory dataset; orthogonal capability evaluation.

### 7.6 Nemobot: LLM Game Agents for Interactive Learning
- **arXiv**: [2604.21896](https://arxiv.org/abs/2604.21896)
- **Affiliation**: —
- **Abstract**: Interactive agentic engineering environment for LLM-powered game agents across Shannon's four game classes. Compresses state-action mappings, applies mathematical reasoning, integrates minimax + crowdsourced data, utilizes RLHF + self-critique.
- **Key Innovations**: Four-class game agent taxonomy; crowd-sourced + LLM strategy synthesis; tool-augmented generation.

### 7.7 Sensi: Curriculum-Based Test-Time Learning for Game Agents
- **arXiv**: [2603.17683](https://arxiv.org/abs/2603.17683)
- **Affiliation**: —
- **Abstract**: LLM agent for ARC-AGI-3 with two-player perception/action separation, curriculum learning, database-as-control-plane, LLM-as-judge with dynamic rubrics. 50–94× sample efficiency over comparable systems.
- **Key Innovations**: Database-as-control-plane for steerable context window; LLM-as-judge for curriculum progression; precise diagnosis of perception bottleneck.

### 7.8 Open-P2P: Open Recipe for Game-Playing Foundation Model
- **arXiv**: [2601.04575](https://arxiv.org/abs/2601.04575)
- **Affiliation**: —
- **Abstract**: Behavior cloning at scale (8300+ hours human gameplay). Models up to 1.2B params. Competitive with human players across 3D games. Scaling analysis shows depth/data improve causal policy learning.
- **Key Innovations**: Open-source game-playing foundation model; scaling laws for behavior cloning; causal reasoning analysis.

### 7.9 Reward Modeling for Multi-Agent Orchestration (OrchRM)
- **arXiv**: [2606.13598](https://arxiv.org/abs/2606.13598)
- **Affiliation**: —
- **Abstract**: Self-supervised framework for evaluating multi-agent orchestration without human annotations. Win-lose pairs from intermediate artifacts for Bradley-Terry reward model. 10× token efficiency improvement; up to 8% accuracy gain.
- **Key Innovations**: Orchestration-level (not agent-level) reward modeling; training efficiency via direct orchestration supervision.

---

## 8. Agent Memory & Reasoning

### 8.1 Bayesian-Agent: Posterior-Guided Skill Evolution
- **arXiv**: [2606.08348](https://arxiv.org/abs/2606.08348)
- **Affiliation**: DataArcTech
- **Abstract**: Treats reusable skills as hypotheses; maintains feature-conditioned categorical posterior over each skill. Actions: patch, split, compress, retire, explore. With DeepSeek-v4-flash: SOP-Bench 80%→95%, Lifelong AgentBench 90%→100%, RealFin-Bench 45%→65%.
- **Key Innovations**: Bayesian inference for skill evolution; cross-harness framework; posterior-guided action selection.

### 8.2 MemRefine: LLM-Guided Memory Compression
- **arXiv**: [2606.13177](https://arxiv.org/abs/2606.13177)
- **Authors**: Minjae Kim, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang
- **Affiliation**: KAIST
- **Abstract**: Budgeted memory management for long-term LLM agents. Uses similarity for candidate pairing, LLM judge for delete/merge/preserve decisions based on factual content. Consistently meets target budgets while preserving downstream performance.
- **Key Innovations**: Factual-value-based (not similarity-based) memory compression; budgeted storage formulation.

### 8.3 ACTS: Agentic Chain-of-Thought Steering
- **arXiv**: [2606.03965](https://arxiv.org/abs/2606.03965)
- **Affiliation**: —
- **Abstract**: Formulates reasoning steering as MDP—controller agent adaptively steers frozen reasoner via reasoning strategy + steering phrase. RL-optimized with budget-conditioned reward shaping. Matches full-thinking performance with substantial token savings.
- **Key Innovations**: MDP formulation of CoT steering; budget-aware strategy control; synthetic multi-budget trajectory augmentation.

### 8.4 The Shibboleth Effect: Cross-Lingual Skew in LLMs
- **arXiv**: [2606.11082](https://arxiv.org/abs/2606.11082)
- **Affiliation**: —
- **Abstract**: Multi-agent geopolitical wargame (Cerulean Sea Crisis) testing 6 frontier models in English vs Turkish. Llama-4: coercive rhetoric +0.800 under Turkish; DeepSeek-R1: -0.860 (buffering via CoT). GPT-4o: no detectable effect. Identifies CoT institutional anchoring and multilingual RLHF as buffering mechanisms.
- **Key Innovations**: Cross-lingual behavioral skew audit methodology; multi-agent wargame framework; buffering mechanism identification.

---

## 9. Industry Deployment Snapshot

| Paper | Company | Domain | Key Metric |
|-------|---------|--------|-----------|
| GRAB | Baidu | CTR/CVR | Revenue +3.05%, CTR +3.49% |
| CADET | LinkedIn | Ads CTR | CTR +11.04% |
| EST | Alibaba (Taobao) | Display Ads | CTR +1.22%, RPM +3.27% |
| SparseCTR | — | Long-behavior CTR | CTR +1.72%, CPM +1.41% |
| RankUp | Tencent (Weixin) | Ads CVR/GMV | GMV +3.41%/+4.81%/+2.12% |
| Memento | Meta (Facebook) | Ads CTR/CVR | CTR +1%, CVR +1.2% |
| OneRanker | Tencent (Weixin) | Generative Ads | GMV +1.34% |
| GPR | Tencent (Weixin) | Generative Ads | GMV/CTCVR significant |
| IDProxy | Xiaohongshu | Cold-start CTR | Production deployment |
| LLM-HYPER | US e-commerce | Cold-start CTR | NDCG@10 +55.9% |
| MSA (MiniMax) | MiniMax | LLM Inference | 14.2× prefill, 7.6× decode speedup |

---

## Key Cross-Cutting Themes

1. **Sparse attention is the dominant efficiency paradigm** — at least 12 papers propose new sparse attention mechanisms (MSA, SparDA, AB-Sparse, STS, RTPurbo, SFA, GSA, Vashista, Token Sparse, Vortex), each targeting different axes (block, token, feature, head, speculative).

2. **CTR prediction is undergoing a generative/LLM-inspired paradigm shift** — GRAB, EST, GPR, GR4AD, OneRanker, CADET all move from DLRM cascades to end-to-end generative/transformer architectures. Scaling laws are being established for CTR (LoopCTR, DeRes, EST).

3. **Hybrid SSM-Attention architectures mature** — Mamba-3, Zamba2-VL, Swimba, Sessa all demonstrate that combining SSM recurrence with attention (sparse or shared) outperforms pure approaches.

4. **Diffusion LMs reach practical viability** — Multiple works (OPDLM, LoopMDM, Quokka, RePlaid) show DLMs approaching AR quality with parallel generation benefits. Scaling laws and training recipes are being established.

5. **RL for LLM agents gains traction** — Odysseus (VLM games), MemoPilot (memory RL), OrchRM (multi-agent reward modeling) use RL to improve agent behavior beyond SFT.

6. **Attention-free computation challenge** — PCAF, Vashista, and PSMs explore primitives beyond both attention and recurrence (hash-based content-addressable memory, geometric sparsity).
