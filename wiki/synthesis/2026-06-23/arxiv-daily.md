---
title: "arXiv Daily — 2026-06-23"
type: synthesis
created: 2026-06-23
updated: 2026-06-23
tags: [arxiv, daily, llm, recommendation, ctr, games, sequential-modeling, rl]
sources: []
---

# arXiv Daily Report — 2026-06-23

> Recent papers across AI, LLMs, recommendation, CTR, advertising, sequential modeling, games. Compiled 2026-06-23 from arxiv.org recent listings (Jun 15–19, 2026).

---

## 1. Large Language Models & Reasoning

### 1.1 Large Language Models Do Not Always Need Readable Language
- **arXiv**: [2606.19857](https://arxiv.org/abs/2606.19857)
- **Authors**: Jiayi Zhu et al.
- **Date**: 2026-06-18
- **Key Innovation**: Proposes **BabelTele**, a model-centric textual representation that compresses semantic content to 27.9% of original length while preserving 99.5% semantic fidelity for instruction-tuned LLMs. Demonstrates human readability and semantic recoverability can be decoupled.
- **Significance**: Opens path toward model-native representations for reduced context overhead in multi-agent communication and agent memory.

### 1.2 Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models
- **arXiv**: [2606.13603](https://arxiv.org/abs/2606.13603)
- **Authors**: Daniel Scalena, Sara Candussio, Luca Bortolussi, et al.
- **Date**: 2026-06-11
- **Key Innovation**: Identifies a **commitment boundary** in CoT reasoning — a sharp single-step transition where answers stabilize. Shows subsequent steps are often *epiphenomenal* (leave final answer probability unaltered). Early-exit at this boundary reduces CoT length by up to 55% with negligible performance loss.

### 1.3 Operads for Compositional Reasoning in LLMs
- **arXiv**: [2606.13634](https://arxiv.org/abs/2606.13634)
- **Authors**: Nathaniel Bottman et al.
- **Date**: 2026-06-11
- **Key Innovation**: Proposes **operads** as a rigorous mathematical framework for question decomposition. Introduces *operadic consistency* — measuring whether a QA model's answers agree across partial collapses of a decomposition tree. Strongly correlated with accuracy across 12 LLMs and 4 multi-hop QA datasets.

### 1.4 The Shibboleth Effect: Auditing the Cross-Lingual Distributional Skew of Large Language Models
- **arXiv**: [2606.11082](https://arxiv.org/abs/2606.11082)
- **Authors**: Hakan Mehmetcik et al.
- **Date**: 2026-06-09
- **Key Innovation**: Multi-agent wargame experiment (Cerulean Sea Crisis) revealing that cross-lingual behavioral skew is **model-specific** (Llama-4 becomes more coercive in Turkish; DeepSeek-R1 buffers via CoT institutional anchoring). Two buffering mechanisms identified: CoT anchoring and multilingual RLHF alignment.

### 1.5 Native Reasoning Training (NRT)
- **arXiv**: [2602.11549](https://arxiv.org/abs/2602.11549)
- **Date**: Feb 2026
- **Key Innovation**: **Verifier-free reasoning framework** that treats reasoning traces as latent variables. Rewards paths that increase model's confidence in ground-truth answer. Eliminates need for expert-written CoT demonstrations. New SOTA for verifier-free reasoning on Llama/Mistral families.

### 1.6 Hidden-Align: Aligning Verified Hidden States Empowers RL Reasoning
- **arXiv**: [2606.03234](https://arxiv.org/abs/2606.03234)
- **Date**: Jun 2026
- **Key Innovation**: Auxiliary loss that maximizes pairwise cosine similarity of correct rollouts' hidden states at the **anchor token** (position before answer marker). Zero overhead at inference. +3.8–6.2 pp on Qwen3-1.7B/4B/14B on math reasoning.

### 1.7 Cognitive Pairwise Training (CPT)
- **arXiv**: [2606.00869](https://arxiv.org/abs/2606.00869)
- **Date**: Jun 2026
- **Key Innovation**: Mid-training alignment stage using pairwise comparisons over reasoning traces to internalize a **reasoning-quality discrimination boundary**. At 14B, CPT+RL outperforms SFT+RL by +2.2 math points and +5.2 abstention-F1 points.

### 1.8 Calibration-Aware Policy Optimization (CAPO)
- **arXiv**: [2604.12632](https://arxiv.org/abs/2604.12632)
- **Date**: Apr 2026
- **Key Innovation**: Proves GRPO-style algorithms degrade calibration due to uncertainty-agnostic advantage estimation. Proposes logistic AUC surrogate loss for uncertainty-aware advantage estimation. Up to 15% calibration improvement while maintaining accuracy.

### 1.9 Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT)
- **arXiv**: [2606.13680](https://arxiv.org/abs/2606.13680)
- **Date**: Jun 2026
- **Key Innovation**: Teaches LLMs to reason **by analogy** via retrieving structurally analogous problems. Gold-relevance distillation + reasoning-aware retriever + RLVR. Strong gains on AIME and HMMT benchmarks.

### 1.10 SaRO: Safety-Oriented Reasoning Optimization
- **arXiv**: [2504.09420](https://arxiv.org/abs/2504.09420)
- **Date**: 2025/2026
- **Key Innovation**: Integrates safety-policy-driven reasoning into alignment. Two-stage: Reasoning-style Warmup (RW) + Safety-oriented Reasoning Process Optimization (SRPO) with stepwise reflection and self-correction.

### 1.11 Does LLM Alignment Really Need Diversity?
- **arXiv**: [2603.10588](https://arxiv.org/abs/2603.10588)
- **Date**: 2026-03-11
- **Key Innovation**: Counter-intuitive finding that moral reasoning exhibits **more concentrated high-reward distributions** than math reasoning. Standard reward-maximizing RLVR transfers effectively to moral reasoning without explicit diversity mechanisms.

### 1.12 AltTrain: Reasoning Structure Matters for Safety Alignment
- **arXiv**: [2604.18946](https://arxiv.org/abs/2604.18946)
- **Date**: Apr 2026
- **Key Innovation**: Alters reasoning structure to problem understanding → harmfulness assessment → conditional reasoning. SFT with only 1K examples achieves strong safety alignment with robust generalization.

### 1.13 Beyond Representational Alignment with Brain-Guided Language Models
- **arXiv**: [2606.11893](https://arxiv.org/abs/2606.11893)
- **Date**: Jun 2026
- **Key Innovation**: Uses task-evoked fMRI signals to steer LLM representations. Up to 13% absolute accuracy gain on deductive reasoning across 10 LLMs (1.5B–72B). First demonstration of brain-signal-driven LLM improvement.

### 1.14 Learning Dynamics of Chain-of-Thought State Tracking
- **arXiv**: [2606.18164](https://arxiv.org/abs/2606.18164)
- **Date**: 2026-06-16
- **Key Innovation**: Statistical-physics analysis of a simplified 1-block transformer. Reveals **staged learning**: MLP first learns a mixed heuristic, then attention locks onto relevant action. Provides mechanistic account of emergent CoT capabilities.

---

## 2. Efficient Attention & Architecture

### 2.1 MiniMax Sparse Attention (MSA)
- **arXiv**: [2606.13392](https://arxiv.org/abs/2606.13392)
- **Institution**: MiniMax
- **Date**: Jun 2026
- **Key Innovation**: Blockwise sparse attention with lightweight Index Branch for Top-k KV block selection per GQA group. **28.4×** attention compute reduction at 1M context. 14.2× prefill and 7.6× decoding speedups on H800. Deployed in 109B MoE multimodal model.

### 2.2 Depth-Attention: Cross-Layer Value Mixing
- **arXiv**: [2606.05014](https://arxiv.org/abs/2606.05014)
- **Date**: Jun 2026
- **Key Innovation**: Query attends along **depth** (earlier layers' keys at same position) before attending over sequence. No added parameters, same KV cache as vanilla decoder. Up to +2.3 accuracy points at 1.5B/3B scale.

### 2.3 SparDA: Sparse Decoupled Attention
- **arXiv**: [2606.04511](https://arxiv.org/abs/2606.04511)
- **Date**: 2026-06-03
- **Key Innovation**: Decoupled sparse attention with a fourth projection (Forecast) that predicts KV blocks needed by next layer, enabling CPU→GPU prefetch overlap. Up to 1.7× decode and 5.3× throughput speedup.

### 2.4 Do Transformers Need Three Projections? Systematic Study of QKV Variants
- **arXiv**: [2606.04032](https://arxiv.org/abs/2606.04032)
- **Date**: 2026-06-01
- **Key Innovation**: Q-K=V (shared key-value) achieves 50% KV cache reduction with only 3.1% perplexity degradation at 1.2B scale. Combined with MQA yields 96.9% cache reduction. Enables practical on-device inference.

### 2.5 HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization
- **arXiv**: [2606.20097](https://arxiv.org/abs/2606.20097)
- **Date**: 2026-06-19
- **Key Innovation**: Hybridizes full attention (FA) and linear attention (LA) along the **head axis** rather than per-layer. Interpretability-driven selection preserves FA only for retrieval-critical heads. Trained on 15B tokens, achieves 69% improvement at 512K context.

### 2.6 Parallel Causal Associative Fields (PCAF)
- **arXiv**: [2606.10435](https://arxiv.org/abs/2606.10435)
- **Date**: Jun 2026
- **Key Innovation**: Parallel content-addressed memory over causal successor records. Hash-bucket retrieval + sparse cache + learned gate. At 303M params, achieves 36.31 PPL on WikiText-103 (vs 47.49 for dense Transformer) with higher throughput.

### 2.7 Towards Tight Bounds for Streaming Attention
- **arXiv**: [2606.07205](https://arxiv.org/abs/2606.07205)
- **Date**: 2026-06-05
- **Key Innovation**: Nearly tight theoretical bounds on KV cache compression via streaming attention. Unifies discrepancy theory, polynomial method, and space partitioning for kernel density estimation.

---

## 3. Multimodal & Unified Models

### 3.1 UniAR: Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer
- **arXiv**: [2606.18249](https://arxiv.org/abs/2606.18249)
- **Date**: 2026-06-16
- **Key Innovation**: Single discrete visual tokenizer bridges understanding and generation. Multi-level feature fusion + lookup-free bitwise quantization + parallel-bitwise-prediction. SOTA on image generation and editing while competitive on understanding.

### 3.2 PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models
- **Hugging Face Daily Papers** ([2606.19534](https://arxiv.org/abs/2606.19534))
- **Date**: Jun 2026
- **Key Innovation**: Multimodal diffusion language model with parallel region perception capabilities.

---

## 4. CTR Prediction & Advertising

### 4.1 CADET: Context-Conditioned Ads Decoder-Only Transformer (LinkedIn)
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Institution**: LinkedIn
- **Date**: Feb 2026
- **Key Innovation**: End-to-end decoder-only transformer for ads CTR. Self-gated attention, timestamp-based RoPE, session masking, context-conditioned decoding resolving the CTR-vs-ranking chicken-and-egg problem. **11.04% CTR lift** in online A/B test. Deployed on LinkedIn Ads.

### 4.2 GRAB: Generative Ranking for Ads at Baidu
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Institution**: Baidu
- **Date**: Feb 2026
- **Key Innovation**: Causal Action-aware Multi-channel Attention (CamA) for generative CTR. STS (Step-by-Step) training paradigm to mitigate distribution shift. **3.49% CTR increase**, **3.05% revenue increase** in Baidu home feed ads.

### 4.3 EST: Efficient Scaling Laws in CTR Prediction (Taobao)
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Institution**: Alibaba/Taobao
- **Date**: Feb 2026
- **Key Innovation**: Lightweight Cross-Attention (LCA) + Content Sparse Attention (CSA). Power-law scaling with model capacity. Deployed on Taobao display ads: **3.27% RPM increase**, **1.22% CTR lift**.

### 4.4 SparseCTR: Unleashing Sparse Attention on Long-term Behaviors
- **arXiv**: [2601.17836](https://arxiv.org/abs/2601.17836)
- **Date**: Jan 2026
- **Key Innovation**: Three-branch sparse self-attention (global interests, interest transitions, short-term) with personalized chunking. Composite relative temporal encoding. **1.72% CTR lift**, **1.41% CPM lift** in online test.

### 4.5 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR
- **arXiv**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Date**: Jun 2026
- **Key Innovation**: Dual-path residual connector (Identity residual + Block Attention Residual with SiLU gating). 1.66× steeper compute–AUC scaling law than OneTrans. 8-layer DeRes matches 16-layer OneTrans.

### 4.6 LoopCTR: Loop Scaling Paradigm for CTR Prediction
- **arXiv**: [2604.19550](https://arxiv.org/abs/2604.19550)
- **Date**: Apr 2026
- **Key Innovation**: Sandwich architecture (Entry → Loop → Exit) with Hyper-Connected Residuals + MoE. **Train-multi-loop, infer-zero-loop** strategy. Zero-loop inference outperforms all baselines.

### 4.7 RankUp: High-Rank Representations for Advertising (Tencent)
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Institution**: Tencent
- **Date**: Apr 2026
- **Key Innovation**: Mitigates embedding collapse via task-specific token decoupling. Deployed on Weixin Video Accounts, Moments, Official Accounts. **3.41–4.81% GMV lift**.

### 4.8 GR4AD: Generative Recommendation for Large-Scale Advertising (Kuaishou)
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Institution**: Kuaishou
- **Date**: Feb 2026
- **Key Innovation**: UA-SID tokenization, LazyAR decoder, RSPO (list-wise RL algorithm), Dynamic Beam Serving. Up to **4.2% ad revenue improvement**. Deployed on 400M+ user platform.

### 4.9 OneRanker: Unified Generation and Ranking (Tencent)
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Institution**: Tencent
- **Date**: Mar 2026
- **Key Innovation**: Value-aware multi-task decoupling + coarse-to-fine target awareness + dual-side consistency (KV pass-through + DC loss). **GMV +1.34%** on Weixin Channels.

### 4.10 Memento: Personalized RAG-Style Long-Retention Data Scaling (Meta)
- **arXiv**: [2605.24051](https://arxiv.org/abs/2605.24051)
- **Institution**: Meta
- **Date**: May 2026
- **Key Innovation**: Treats user history as document corpus, ad requests as queries. MMR-based retrieval. 5–10× resource efficiency over linear scaling. **1% CTR lift**, **1.2% CVR lift** on Facebook Feed/Reels at 365+ day retention.

### 4.11 SOLARIS: Speculative Offloading of Latent-Based Representation (Meta)
- **arXiv**: [2604.12110](https://arxiv.org/abs/2604.12110)
- **Institution**: Meta
- **Date**: Apr 2026
- **Key Innovation**: Speculative decoding-inspired precomputation of user-item embeddings for CTR/CVR. Decouples foundation model inference from latency-critical path. **0.67% revenue gain** across Meta's ads system.

### 4.12 IDProxy: Cold-Start CTR with Multimodal LLMs (Xiaohongshu)
- **arXiv**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Institution**: Xiaohongshu
- **Date**: Mar 2026
- **Key Innovation**: MLLM-generated proxy embeddings aligned with ID embedding space for cold-start items. Deployed in Content Feed and Display Ads.

### 4.13 LLM-HYPER: Generative CTR for Cold-Start via LLM Hypernetworks
- **arXiv**: [2604.12096](https://arxiv.org/abs/2604.12096)
- **Date**: Apr 2026
- **Key Innovation**: LLMs as hypernetworks generating linear CTR model weights from few-shot CoT over multimodal ad content. 55.9% NDCG@10 improvement. Deployed on top US e-commerce platform.

### 4.14 GenCI: Generative Modeling of User Interest Shift via Cohort-Based Intent Learning
- **arXiv**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Date**: Jan 2026
- **Key Innovation**: Generative model with NTP objective produces candidate interest cohorts. Hierarchical candidate-aware network injects contextual signal into ranking.

### 4.15 Field-Aware Transformer (FAT) for CTR
- **arXiv**: [2511.12081](https://arxiv.org/abs/2511.12081)
- **Date**: 2025/2026
- **Key Innovation**: Field-Decomposed Attention + Basis-Composed Hypernetwork for structured expressivity. Shifts complexity from vocabulary size n to number of fields F (n ≫ F). Up to +4.38% AUC improvement.

### 4.16 Disentangled Interest Network (DiseCTR) for OOD CTR
- **arXiv**: [2602.00002](https://arxiv.org/abs/2602.00002)
- **Date**: 2025-11/2026
- **Key Innovation**: Causal factorization of CTR (interest, exposure, click models) + weakly supervised interest disentangler. +0.02 AUC and 13.7% logloss reduction on OOD settings.

### 4.17 PRECTR-V2: Unified Relevance–CTR Framework
- **arXiv**: [2602.20676](https://arxiv.org/abs/2602.20676)
- **Date**: Feb 2026
- **Key Innovation**: Joint search relevance + CTR prediction. Cross-user preference mining, exposure bias correction, LLM-distilled encoder optimization.

### 4.18 SIGMA: Semantic-Grounded Generative Multi-Task Recommender (AliExpress)
- **arXiv**: [2602.22913](https://arxiv.org/abs/2602.22913)
- **Institution**: Alibaba/AliExpress
- **Date**: Feb 2026
- **Key Innovation**: Instruction-driven generative multi-task recommender. Hybrid item tokenization, adaptive probabilistic fusion. Deployed at AliExpress.

---

## 5. Recommendation Systems

### 5.1 UniRec: Bridging Generative and Discriminative Recommendation with Chain-of-Attribute (Shopee)
- **arXiv**: [2604.12234](https://arxiv.org/abs/2604.12234)
- **Institution**: Shopee
- **Date**: Apr 2026
- **Key Innovation**: Chain-of-Attribute (CoA) prefixes SID sequences with attribute tokens (category, seller, brand). Proves attribute conditioning yields per-step entropy reduction. +22.6% HR@50 overall, +5.37% PVCTR, +5.60% GMV online.

### 5.2 GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation
- **arXiv**: [2606.11023](https://arxiv.org/abs/2606.11023)
- **Date**: Jun 2026
- **Key Innovation**: LLM-generated archetypes (ideal target audience description) for items + behavioral calibration objective. Seamless integration with existing sequential models.

---

## 6. Games & Reinforcement Learning

### 6.1 GrandCode: Grandmaster Level in Competitive Programming via Agentic RL
- **arXiv**: [2604.02721](https://arxiv.org/abs/2604.02721)
- **Date**: Apr 2026
- **Key Innovation**: First AI system to consistently beat all humans in live Codeforces contests (Rounds 1087, 1088, 1089 — March 2026). Multi-agent system (hypothesis, solver, test generator, summarization) + Agentic GRPO for multi-stage rollouts.

### 6.2 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Date**: May 2026
- **Key Innovation**: Adapted PPO with lightweight turn-level critic for long-horizon (100+ turns) VLM game-playing in Super Mario Land. 3× average game progress over frontier models. Pretrained VLMs provide strong action priors.

### 6.3 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Date**: 2025/2026
- **Key Innovation**: Self-play on multi-turn zero-sum games (TicTacToe, Kuhn Poker, Negotiation). Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Up to 10% improvement across 8 reasoning benchmarks.

### 6.4 Augmenting Game AI with Deep Reinforcement Learning
- **arXiv**: [2606.20210](https://arxiv.org/abs/2606.20210)
- **Date**: 2026-06-19
- **Key Innovation**: Framework for training RL models for game AI in AAA production. Addresses usability, stability, controllability, and integration workflows. Demonstrates RL can augment rather than replace traditional game AI.

### 6.5 OpenGame: Open Agentic Coding for Games
- **arXiv**: [2604.18394](https://arxiv.org/abs/2604.18394)
- **Date**: Apr 2026
- **Key Innovation**: First open-source agentic framework for end-to-end web game creation. GameCoder-27B (specialized code LLM) with execution-grounded RL. OpenGame-Bench for evaluating generated games.

### 6.6 GraphPO: Graph-Based Policy Optimization for Reasoning Models
- **arXiv**: [2606.18954](https://arxiv.org/abs/2606.18954)
- **Date**: Jun 2026
- **Key Innovation**: Represents RL rollouts as DAGs (nodes = semantic states, edges = reasoning steps). Merges semantically equivalent paths, reduces redundant exploration, provides emergent process supervision.

### 6.7 Sparrow: Sparse Rollout for Stable and Efficient Long-context RL
- **arXiv**: [2606.08446](https://arxiv.org/abs/2606.08446)
- **Date**: Jun 2026
- **Key Innovation**: Dynamic sparsity scheduling for RLVR rollouts. Keeps tail distribution mismatch below critical threshold. 2.0–2.4× rollout speedup on Qwen3-1.7B/4B/8B.

### 6.8 Agentic Monte Carlo (AMC): Simulating RL for Black-Box Agents
- **arXiv**: [2606.05296](https://arxiv.org/abs/2606.05296)
- **Date**: Jun 2026
- **Key Innovation**: Sequential Monte Carlo to sample from optimal policy of black-box LLM agents. Learns value function to steer without modifying underlying model. Outperforms GRPO at scale on AgentGym benchmark.

### 6.9 From Trainee to Trainer: LLM-Designed Training Environment for RL
- **arXiv**: [2606.17682](https://arxiv.org/abs/2606.17682)
- **Date**: 2026-06-16
- **Key Innovation**: LLM-as-Environment-Engineer framework — current policy analyzes failure trajectories and proposes environment config modifications for next training stage. Qwen3-4B outperforms GPT/Gemini at environment design.

### 6.10 OpenClaw-Skill: Collective Skill Tree Search for Agentic LLMs
- **arXiv**: [2606.16774](https://arxiv.org/abs/2606.16774)
- **Date**: Jun 2026
- **Key Innovation**: Collective Skill Tree Search (CSTS) with multi-model skill generation/assessment + Collective Skill Reinforcement Learning. Constructs reusable skill trees for tool use and multi-step reasoning.

### 6.11 Reward Modeling for Multi-Agent Orchestration (OrchRM)
- **arXiv**: [2606.13598](https://arxiv.org/abs/2606.13598)
- **Date**: 2026-06-11
- **Key Innovation**: Self-supervised reward modeling for MAS orchestration using intermediate artifacts. Up to 10× token efficiency improvement, +8% accuracy in MAS test-time scaling.

### 6.12 PROPEL: Breaking the Solver Bottleneck — Training Task Generators at the Learnable Frontier
- **arXiv**: [2606.18284](https://arxiv.org/abs/2606.18284)
- **Date**: Jun 2026
- **Key Innovation**: Solver-amortized framework using lightweight activation probes to predict pass rates. Increases learnable-frontier task generation from 10.1% → 20.0% (coding) and 9.8% → 19.6% (SWE).

### 6.13 Representation Learning Enables Scalable Multitask Deep RL
- **arXiv**: [2606.05555](https://arxiv.org/abs/2606.05555)
- **Date**: Jun 2026
- **Key Innovation**: MR.Q algorithm: model-free actor-critic with predictive representation learning outperforms world-model-based methods (Newt) on multitask continuous control. Shows representation quality is primary driver of RL scaling.

### 6.14 Visual Verification Enables Inference-Time Steering (VERITAS)
- **arXiv**: [2606.18247](https://arxiv.org/abs/2606.18247)
- **Date**: 2026-06-16
- **Key Innovation**: Generator-verifier framework for robot policies. Gradient-free visual verifier enables inference-time steering + self-improvement from verified rollouts without human intervention.

---

## 7. Sequential & Time Series Modeling

### 7.1 CAPS: Unifying Attention, Recurrence, and Alignment in Transformer-based Time Series Forecasting
- **arXiv**: [2602.02729](https://arxiv.org/abs/2602.02729)
- **Date**: Feb 2026
- **Key Innovation**: Three-part attention mechanism: SO(2) rotations (RoPE) for alignment, diagonal SPD gates for causal decay, Clock (weighted Riemann softmax) for global structure. All three within a unified layer.

### 7.2 StretchTime: Adaptive Time Series Forecasting via Symplectic Attention
- **arXiv**: [2602.08983](https://arxiv.org/abs/2602.08983)
- **Date**: Feb 2026
- **Key Innovation**: Symplectic Positional Embeddings (SyPE) generalizing RoPE from SO(2) to Sp(2,R). Input-dependent adaptive warp module captures non-affine temporal warping. SOTA on benchmarks with non-stationary dynamics.

### 7.3 Revisiting the Generic Transformer for Time Series Foundation Models
- **arXiv**: [2602.06909](https://arxiv.org/abs/2602.06909)
- **Date**: Feb 2026
- **Key Innovation**: Demonstrates standard patch Transformer with straightforward training achieves SOTA zero-shot forecasting. Identifies data composition, contiguous patch masking, and context length as key drivers.

### 7.4 UniTok: Time Series as Language — A Universal Tokenizer for TSFMs
- **arXiv**: [2606.09861](https://arxiv.org/abs/2606.09861)
- **Date**: Jun 2026
- **Key Innovation**: Universal TS tokenizer enabling NTP pretraining. Supports zero-shot forecasting, **prompt-boosted**, few-shot generation, and few-shot classification — all via training-free in-context inference.

### 7.5 Time-TK: Transformer + Kolmogorov-Arnold Networks for Time Series
- **arXiv**: [2602.11190](https://arxiv.org/abs/2602.11190)
- **Date**: Feb 2026
- **Key Innovation**: Multi-offset temporal token embedding + MI-KAN (KAN-based kernel function modeling). Lightweight architecture outperforms more complex models.

### 7.6 Reverso: Efficient Time Series Foundation Models (0.2M–2.6M params)
- **arXiv**: [2602.17634](https://arxiv.org/abs/2602.17634)
- **Date**: Feb 2026
- **Key Innovation**: Small hybrid models (long convolution + DeltaNet linear RNN) match or outperform TSFMs orders of magnitude larger. Pushes performance-efficiency Pareto frontier.

### 7.7 EnTransformer: Deep Generative Transformer for Multivariate Probabilistic Forecasting
- **arXiv**: [2603.11909](https://arxiv.org/abs/2603.11909)
- **Institution**: Sorbonne University
- **Date**: Mar 2026
- **Key Innovation**: Integrates **engression** (stochastic learning for conditional distributions) with Transformer. Learns joint predictive distribution without parametric assumptions.

### 7.8 DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters
- **arXiv**: [2602.06597](https://arxiv.org/abs/2602.06597)
- **Date**: Feb 2026
- **Key Innovation**: Frames endogenous/exogenous variates as distinct modalities. Dual-stream Transformer (Time Attention + Variate Attention). Leverages low-rank property of multivariate dependencies.

### 7.9 MoHETS: Mixture-of-Heterogeneous-Experts for Time Series
- **arXiv**: [2601.21866](https://arxiv.org/abs/2601.21866)
- **Date**: Jan/Feb 2026
- **Key Innovation**: Shared depthwise-convolution expert + routed Fourier-based experts for patch-level periodic structures. 12% average MSE reduction.

### 7.10 UniMamba: Unified Spatial-Temporal Framework with SSM and Attention
- **arXiv**: [2604.16325](https://arxiv.org/abs/2604.16325)
- **Date**: Apr 2026
- **Key Innovation**: Mamba Variate-Channel Encoding (FFT-Laplace + TCN) + Spatial Temporal Attention. State-of-the-art on 8 benchmarks with better efficiency.

---

## Themes & Trends

1. **RL for Reasoning is the dominant paradigm**: GRPO variants, process supervision, and verifier-free methods (NRT, CPT, CAPO, GraphPO) are the hottest area in LLM research.
2. **CTR/Advertising is going generative**: Nearly every major tech company (Meta, LinkedIn, Baidu, Alibaba, Tencent, Kuaishou, Shopee, Xiaohongshu) has published generative/transformer-based CTR models deployed in production.
3. **Sparse attention for long context**: MSA, SparDA, HydraHead, PCAF all tackle the long-context bottleneck with different sparsity strategies.
4. **Self-play / multi-agent RL for reasoning**: SPIRAL and GrandCode show that competitive game-like settings produce transferable reasoning capabilities.
5. **Foundation models for time series**: The field is maturing with small efficient models (Reverso 0.2M params matching models 100× larger) and universal tokenizers (UniTok).
6. **Cross-layer communication**: Depth-Attention and DeRes explore attention over depth rather than just sequence.
