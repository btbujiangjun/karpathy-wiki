---
title: "arXiv AI Research Scan — July 2026"
type: synthesis
created: 2026-07-06
updated: 2026-07-06
sources: []
tags: [arxiv, survey, llm, recommendation, ctr, attention, rl, multimodal]
---

# arXiv AI Research Scan — July 2026

> Papers collected from arXiv recent submissions (late May – early July 2026). Organized by domain.

---

## 1. Large Language Models — Training & Alignment

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2506.24119
- **Key Innovation**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen/Llama families.

### T-STAR: Tree-structured Self-Taught Agent Rectification
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2604.07165
- **Key Innovation**: Consolidates RL trajectories into a Cognitive Tree to identify critical divergence steps. Enables variance-reduced advantage estimation and "thought grafting" (contrasting successful/failed branches to synthesize corrective reasoning). Surgical policy optimization targets critical steps via Bradley-Terry loss.

### SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2604.08865
- **Key Innovation**: Reformulates reasoning from token-level MDP to sequence-level contextual bandit, resolving bias-variance dilemma in sparse-reward CoT alignment. Decoupled Critic (1.5B critic for 7B policy) cuts memory 12.8%. Matches GRPO peak with 5.9× training speedup.

### SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
- **Authors**: Tianyi Hu, Qingxu Fu, Yanxi Chen, Zhaoyang Liu, Bolin Ding
- **Link**: https://arxiv.org/abs/2602.06554
- **Key Innovation**: First critic-free multi-turn RL with monotonic improvement guarantees. Models multi-turn as sequentially executed multi-agent bandits, uses backward induction. 43.3–54.6% gains on Qwen3-14B on AppWorld/BFCL.

### Trainee-to-Trainer: LLM-Designed Training Environment for RL
- **Authors**: Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo (HKUST, Cambridge)
- **Link**: https://arxiv.org/abs/2606.17682
- **Key Innovation**: LLM-as-Environment Engineer — the policy model itself analyzes failure trajectories and proposes next-stage training environment configs. Current RL checkpoint serves as better environment engineer than base model.

---

## 2. Attention Mechanisms & Architectures

### Keyless Attention: Value-Space Routing and Value-Only Caching
- **Author**: Xin Gao
- **Link**: https://arxiv.org/abs/2606.21848
- **Key Innovation**: Eliminates key projection entirely — QVV attention. 50% KV cache reduction. Matches or beats standard attention on perplexity (4/5 models tested). Depth-m Attention Factorization generalizes the bilinear form.

### MiniMax Sparse Attention (MSA)
- **Authors**: MiniMax AI
- **Link**: https://arxiv.org/abs/2606.13392
- **Key Innovation**: Blockwise sparse attention with lightweight Index Branch scoring KV blocks per GQA group. 28.4× compute reduction at 1M context on 109B model. 14.2× prefill and 7.6× decoding speedups on H800.

### Affine-Scaled Attention
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2602.23057
- **Key Innovation**: Relaxes softmax sum-to-one constraint via input-dependent scaling + bias. Improves training stability and downstream performance across multiple model sizes.

### Tucker Attention
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2603.30033
- **Key Innovation**: Unifying view treating attention weights as a tensor — MHA, MQA, GQA, MLA are all special cases. Up to 9× parameter reduction. Compatible with Flash Attention and RoPE.

### CAHP: Complementary Attention Head Pruning
- **Authors**: Yaniv Livertovsky, Shahar Somin, Gonen Singer
- **Link**: https://arxiv.org/abs/2606.19150
- **Key Innovation**: Graph-theoretical head pruning using clustering + information-theoretic distance. Automatically determines per-layer head count. Avoids "proximity bias" of gradient-based methods.

### Nonlinear Queries for Attention
- **Authors**: Marko Karbevski et al. (ICLR 2026 Workshop GRaM)
- **Link**: https://arxiv.org/abs/2603.13381
- **Key Innovation**: Replaces linear W_Q with nonlinear residual (bottleneck MLP + identity). Consistent validation loss improvement over linear baseline.

### Exact Attention Sensitivity & Transformer Stability
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2602.18849
- **Key Innovation**: Derives exact operator norm of softmax Jacobian. Proves pre-LN preserves identity gradient paths; explains DeepNorm's N^{-1/4} scaling. Key finding: attention never sharpens during training — stability is architectural, not learned.

### Streaming Attention — Tight Bounds
- **Authors**: Boris Prokhorov et al.
- **Link**: https://arxiv.org/abs/2606.07205
- **Key Innovation**: Nearly tight space complexity bounds for streaming attention approximation. Combines discrepancy theory, polynomial method, and space partitioning.

### Rethinking Efficient Attention in Hybrid Architectures
- **Authors**: Yinuo Xu et al.
- **Link**: https://arxiv.org/abs/2606.15378
- **Key Innovation**: Systematic analysis of hybrid attention (full + SWA/recurrent). Discovers "Large-Window Laziness": larger SWA windows delay retrieval head formation in full-attention layers. NoPE on full-attention layers of small-window hybrids improves long-context performance.

---

## 3. LLM Inference & Compression

### Joint Structural Pruning & Mixed-Precision Quantization
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.07819
- **Key Innovation**: End-to-end framework jointly learning pruning decisions + mixed-precision quantization. Global error propagation minimization (not per-layer). Up to 21% perplexity reduction at 1-3 bits. 2× prefill speedup, 6.5× peak memory reduction.

### Efficient Post-Training Pruning with Statistical Correction
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2602.07375
- **Key Innovation**: First-order statistical calibration of magnitude-based importance scores. Analytic energy compensation after pruning. No gradients, retraining, or second-order info required.

### GRINQH: Graded Input-based Quantization Hierarchy
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.23419
- **Key Innovation**: Treats decoding as primary optimization target for LLM quantization. Input-graded quantization hierarchy.

### POP: Prefill-Only Pruning
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2602.03295
- **Key Innovation**: Prunes deep layers exclusively during prefill, retains full model for decoding. Stage-aware importance scoring.

---

## 4. Recommendation Systems & CTR

### GenRec: Preference-Oriented Generative Framework (JD)
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2604.14878
- **Key Innovation**: Page-wise NTP task supervising over entire interaction pages. Asymmetric linear Token Merger compresses multi-token Semantic IDs 2×. GRPO-SR with Hybrid Rewards (dense RM + relevance gate). 9.5% click, 8.7% transaction improvement on JD.

### UniRec: Bridging Generative & Discriminative Recommendation (Shopee)
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2604.12234
- **Key Innovation**: Chain-of-Attribute (CoA) recovering item-side feature crossing in generative trajectories. Capacity-constrained SID with exposure-weighted residual quantization. +5.37% PVCTR, +4.76% orders, +5.60% GMV on Shopee.

### OneRanker: Unified Generation & Ranking (Tencent Weixin)
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2603.02999
- **Key Innovation**: Value-aware multi-task decoupling with causal masks. Coarse-to-fine target awareness with Fake Item Tokens. KV pass-through + Distribution Consistency Loss. GMV-Normal +1.34% on Weixin Channels.

### RankUp: High-rank Representations for Advertising (Tencent)
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2604.17878
- **Key Innovation**: Addresses representation collapse via randomized permutation splitting, multi-embedding paradigm, global token integration. GMV improvements: +3.41% (Video Accounts), +4.81% (Moments), +2.12% (Official Accounts).

### GRAB: LLM-Inspired Sequence-First CTR (Baidu)
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren et al.
- **Link**: https://arxiv.org/abs/2602.01865
- **Key Innovation**: Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics. Monotonic/linear scaling with longer sequences. 3.05% revenue increase, 3.49% CTR lift at Baidu.

### IDProxy: Cold-Start CTR with Multimodal LLMs (Xiaohongshu)
- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan et al.
- **Link**: https://arxiv.org/abs/2603.01590
- **Key Innovation**: MLLM-generated proxy embeddings aligned with ID embedding space for cold-start items. Deployed on Explore Feed and Display Ads at Xiaohongshu.

### Dual-Stream MLP for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao et al. (Renmin Univ., ByteDance, Meituan)
- **Link**: https://arxiv.org/abs/2606.04944
- **Key Innovation**: Knowledge distillation from parallel MLP to main MLP with gated high-order interaction filtering. SOTA on three CTR benchmarks with near-zero non-embedding params.

### GenCI: Generative User Interest Shift via Cohort-based Intent Learning
- **Authors**: et al. (WWW 2026)
- **Link**: https://arxiv.org/abs/2601.18251
- **Key Innovation**: Generative next-item-prediction for semantic interest cohorts as explicit intent representations. Hierarchical candidate-aware cross-attention for ranking.

### DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation
- **Authors**: Zhihao Lv, Longtao Zhang et al.
- **Link**: https://arxiv.org/abs/2602.13971
- **Key Innovation**: Hybrid enhancer combining ID and semantic information for trigger-induced recommendation. Addresses "intent myopia" in e-commerce.

### Generative Recommendation for Large-Scale Advertising
- **Authors**: Ben Xue, Dan Liu et al.
- **Link**: https://arxiv.org/abs/2602.22732
- **Key Innovation**: Generative paradigm for large-scale advertising recommendation with multi-objective optimization.

---

## 5. RL for LLM Agents & Games

### MemoPilot: RL over Memory for LLM Agents
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.08656
- **Key Innovation**: Plug-in memory copilot trained with multi-turn GRPO. Turn-wise reward + context-independent turn-level advantage estimation. Ranked #1 Elo on Limit Texas Hold'em (1762) and RPS (1590), beating DeepSeek-V3.2.

### MEMO: Memory-augmented Model Context Optimization via Self-Play
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2603.09022
- **Key Innovation**: Weight-free self-play optimizing inference-time context. Tournament-style context evolution + CRUD memory bank. Uses 19× fewer games than RL baselines. Raises GPT-4o-mini win rate from 25.1% to 49.5%.

### Agentic Transformers Provably Learn to Search via RL
- **Authors**: Yuejie Chi et al.
- **Link**: https://arxiv.org/abs/2606.00183
- **Key Innovation**: Theoretical proof that transformers learn DFS via policy gradient under depth-wise curriculum. Two-head attention mechanism for history tracking + failure backtracking.

### AgentOdyssey: Open-Ended Text Game Generation
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.24893
- **Key Innovation**: Procedurally generated open-ended text games for evaluating test-time continual learning agents. Multifaceted eval: world knowledge acquisition, episodic memory, exploration diversity.

---

## 6. Multimodal Models

### UniAR: Unified Multimodal Autoregressive with Shared Tokenizer
- **Authors**: Wujian Peng et al.
- **Link**: https://arxiv.org/abs/2606.18249
- **Key Innovation**: Single discrete visual tokenizer for both understanding and generation. Lookup-free bitwise quantization. Parallel-bitwise-prediction for spatial multi-level codes. SOTA on image generation + editing while competitive on understanding.

### ARM: AutoRegressive Multimodal with Unified Discrete Representations
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.11188
- **Key Innovation**: Discrete semantic visual tokenizer with multi-objective supervision (semantic discriminability + language alignment + reconstruction). RL alignment for generation/editing induces cross-task synergy. WISE 0.50→0.56, GEdit G_O 5.75→6.68.

### TVI-CoT: Text-Visual Interleaved CoT Reasoning
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.08464
- **Key Innovation**: Learnable control tokens enabling dynamic visual grounding during reasoning chain. Beats vision-blind CoT: +6.1% MMMU, +3.8% MathVerse.

### LaME: Latent Reasoning for Multimodal Embedding
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.13061
- **Key Innovation**: Replaces expensive autoregressive CoT with latent-space reasoning via learnable thought tokens. Eliminates CoT annotation dependency.

### ROSE: Benchmarking Perception-to-Action Gap in MLLMs
- **Authors**: Yihao Wang, Zijian He, Jie Ren, Keze Wang
- **Link**: https://arxiv.org/abs/2606.19965
- **Key Innovation**: Controlled benchmark revealing counting-to-action gap (up to 44.5 percentage points drop). GPT-5.5: 92.2%, Gemini-3.1-Pro: 79.4%, others 14.3–50.3%.

### CogniRoute: Routing Social Evidence in Omni-Modal Models
- **Authors**: Yifan Shen et al.
- **Link**: https://arxiv.org/abs/2606.20970
- **Key Innovation**: Schema-guided MoE with route-aware RL for social video QA. OmniSocialBench dataset (118K). 59.38% accuracy — 15.33 pp above best proprietary baseline.

### UniDrive: Unified VLM for Autonomous Driving
- **Authors**: Yun Ye et al.
- **Link**: https://arxiv.org/abs/2606.24759
- **Key Innovation**: Temporal reasoning branch (multi-frame) + high-res perception branch (latest frame) with gated cross-attention fusion. Jointly generates risk descriptions + bounding boxes.

---

## 7. LLM Development & Evaluation

### CuratorKIT: Data Curation & Synthetic Data Generation for LLM Post-Training
- **Authors**: Soham Bhattacharjee, Karun Sharma et al.
- **Link**: https://arxiv.org/abs/2606.21631
- **Key Innovation**: Open-source library covering full lifecycle: ingestion, dedup, PII filtering, 8 LLM-powered generation tasks, 3 quality gates, hallucination verification. Append-only provenance chain. Supports 100+ LLM providers.

### KARLA: Knowledge-base Augmented Retrieval for Language Models
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2606.26807
- **Key Innovation**: KB-augmented retrieval for grounding LLM outputs with structured knowledge.

### Causal Methods for LLM Development and Evaluation
- **Authors**: et al. (KDD 2026)
- **Link**: https://arxiv.org/abs/2605.25998
- **Key Innovation**: Systematic mapping of causal inference to pretraining data selection, alignment, routing, agentic workflows, and evaluation. Argues causal methods are underutilized in LLM development.

### LLM Reasoning as Trajectories: Step-Specific Geometry
- **Authors**: L. Sun et al.
- **Link**: https://arxiv.org/abs/2604.05655
- **Key Innovation**: Characterizes CoT as structured trajectories through representation space. Mid-reasoning correctness prediction with ROC-AUC 0.87. Trajectory-based steering for inference-time correction and length control.

---

## 8. Sequential Decision Making

### Deep Learning for Sequential Decision Making under Uncertainty
- **Authors**: et al.
- **Link**: https://arxiv.org/abs/2604.11507
- **Key Innovation**: Comprehensive survey covering foundations, frameworks, and frontiers in sequential decision making under uncertainty.

---

**Legend**: Papers with deployed industrial results are marked with company names. arXiv IDs are linked (append to https://arxiv.org/abs/).
