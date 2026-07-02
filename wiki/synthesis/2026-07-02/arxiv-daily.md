---
title: "arXiv Daily — 2026-07-02"
type: synthesis
created: 2026-07-02
updated: 2026-07-02
tags: [arxiv, survey, llm, recommendation, ctr, rl, advertising, multimodal, alignment]
---

# arXiv Daily Report — 2026-07-02

Curated recent papers across AI, LLMs, recommendation systems, advertising, CTR prediction, reinforcement learning, multimodal modeling, and sequence modeling.

---

## LLM Training & Alignment

### 1. f-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment
- **Authors**: Rajdeep Haldar, Lantao Mei, Guang Lin, Yue Xing, Qifan Song
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2602.05946
- **Key Innovation**: Extends divergence-based perspective (from DPO) to RLVR regime. Proposes **f-GRPO** (on-policy) and **f-HAL** (hybrid on/off-policy) using variational f-divergences, with theoretical guarantees of average reward improvement.
- **Abstract**: Recent work shows PA objectives act as divergence estimators. This paper extends to RLVR settings, proposing a family of objectives based on f-divergences that unify preference alignment and verifiable reward RL.

### 2. Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients
- **Authors**: Anonymous (OpenReview)
- **Affiliation**: Academic
- **Link**: https://openreview.net/forum?id=mnU8odBWYE
- **Key Innovation**: Models reward corruption as Bernoulli noise and applies noise correction after estimating flip probabilities to yield unbiased gradients. Up to +6.7 pp accuracy on math.
- **Abstract**: RLHF/RLVR is highly sensitive to noisy rewards. Bridges label-noise correction from supervised learning with modern group-based RLHF.

### 3. A Unified Pair-GRPO Family: From Implicit to Explicit Preference Constraints
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2605.06375
- **Key Innovation**: Proves gradient equivalence theorem for Soft-Pair-GRPO (binary preference rewards preserve GRPO gradient structure). Hard-Pair-GRPO adds explicit probability constraints + constrained KL-fitting.
- **Abstract**: Unified theoretical framework for preference-based RL with monotonic improvement guarantees, validated on HH-RLHF, UltraFeedback, and MuJoCo.

### 4. AMIR-GRPO: Inducing Implicit Preference Signals into GRPO
- **Authors**: Amir Hossein Yari, Fajri Koto
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2601.03661
- **Key Innovation**: Augments GRPO with DPO-style contrastive regularizer from intra-group reward rankings, no extra annotations. Mitigates length bias and amplifies low-reward suppression.
- **Abstract**: Transforms each rollout group into denser supervision constraints, outperforming GRPO on math reasoning.

### 5. GeoAlign: Geometric Rollout Curation for Robust LLM Reinforcement Learning
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.26917
- **Key Innovation**: Identifies "directional inconsistency" failure mode. Learns a projection of hidden states to detect and rectify rollouts whose update direction disagrees with batch consensus.
- **Abstract**: Forward-pass-only plug-in for iterative policy optimization. Improves both dialogue alignment and math reasoning stability.

### 6. Representation-Aware Advantage Estimation (GraphAE)
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.10528
- **Key Innovation**: Constructs similarity graph from RM hidden states; advantages propagate through the graph for more robust estimation.
- **Abstract**: Plug-in for GRPO, GSPO, RLOO. Up to +6.3 on Arena-Hard, +8.27 on AlpacaEval 2.0.

### 7. GRPO-VPS: Verifiable Process Supervision for Effective Reasoning
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2604.20659
- **Key Innovation**: Model-free process supervision by probing belief in correct answer at each step segment, no auxiliary model needed. Up to 2.6 pp accuracy gain + 13.7% length reduction.
- **Abstract**: Refines GRPO's trajectory-level feedback with interpretable segment-wise progress measurements.

### 8. Low-probability Tokens Sustain Exploration in RLVR
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://aclanthology.org/2026.findings-acl.1209
- **Key Innovation**: Identifies "reasoning sparks" — valuable low-probability tokens eliminated by RLVR over-penalization. Lp-Reg filters noise while preserving exploratory tokens.
- **Abstract**: Enables stable on-policy training for 3000+ steps, 3.06–7.98% relative accuracy gains across math, science, code.

### 9. DAR: Unifying Stable Optimization and Reference Regularization in RLHF
- **Authors**: Li He, Qiang Qu, He Zhao, Stephen Wan, Dadong Wang, Lina Yao, et al.
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2602.11523
- **Key Innovation**: Proposes dual-KL alignment objective balancing π₀ (reward hacking prevention) and πₜ (stable updates). DAR simplifies to weighted SFT loss.
- **Abstract**: Consistently outperforms PPO-based RLHF and online preference methods.

### 10. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2506.24119
- **Key Innovation**: Multi-agent multi-turn RL on zero-sum games (TicTacToe, Kuhn Poker, Negotiation). Automatic curriculum via self-play. Up to 10% gain across 8 reasoning benchmarks.
- **Abstract**: Models learn transferable reasoning without human-curated data. Even DeepSeek-R1-Distill-Qwen-7B benefits further.

### 11. CuratorKIT: Data Curation and Synthetic Data Generation for LLM Post-Training
- **Authors**: Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu, Pratinav Seth
- **Affiliation**: Industry
- **Link**: https://arxiv.org/abs/2606.21631
- **Key Innovation**: Open-source pipeline covering ingestion, dedup, synthetic generation, quality filtering. Append-only provenance chain per sample. Supports 100+ LLM providers.
- **Abstract**: Six source readers, 8 generation tasks, 3 quality gates with hallucination verification, 5 export formats.

### 12. LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.18388
- **Key Innovation**: LLM agents search training trajectories via tree search, diagnosing pathologies and proposing multi-parameter transitions. 9–140% relative improvement over base.
- **Abstract**: Discovers that capacity params accumulate monotonically while regularization params oscillate — a transferable structural principle.

### 13. TARPO: Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization
- **Authors**: Liting Zhang, Shiwan Zhao, Xuyang Zhao, Zichen Xu, Jianye Wang, Qicheng Li
- **Affiliation**: Academic (NKU)
- **Link**: https://arxiv.org/abs/2606.05859
- **Key Innovation**: Lightweight action-head router switches between discrete token generation and continuous latent reasoning per step, optimized with shared advantage.
- **Abstract**: Outperforms both explicit and latent reasoning RL baselines on Qwen2.5 and Llama-3.1-8B.

---

## CTR Prediction & Advertising Recommendation

### 14. GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Ben Xue, Dan Liu, Lixiang Wang, Lei Meng, Peng Wang, Pengfei Zhang, et al.
- **Affiliation**: Kuaishou
- **Link**: https://arxiv.org/abs/2602.22732
- **Key Innovation**: UA-SID tokenization for complex business info; LazyAR (lazy autoregressive decoder) for efficient short-sequence generation; RSPO ranking-aware RL. **4.2% ad revenue improvement**, 400M+ users.
- **Abstract**: Full-scale generative recommender deployed at Kuaishou with dynamic beam serving.

### 15. OneRanker: Unified Generation and Ranking with One Model
- **Authors**: Anonymous
- **Affiliation**: Tencent (Weixin Channels)
- **Link**: https://arxiv.org/abs/2603.02999
- **Key Innovation**: Value-aware multi-task decoupling with causal mask separation; Fake Item Tokens for implicit target awareness. KV pass-through + DC constraint loss. **GMV +1.34%**.
- **Abstract**: Architectural-level deep integration of generation and ranking, deployed on Weixin Channels.

### 16. GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: Anonymous
- **Affiliation**: JD.com
- **Link**: https://arxiv.org/abs/2604.14878
- **Key Innovation**: Page-wise NTP task; asymmetric linear Token Merger (~2× compression); GRPO-SR with hybrid rewards. **+9.5% clicks, +8.7% transactions**.
- **Abstract**: Single decoder-only architecture deployed on JD App addressing pagination ambiguity, long sequences, and preference alignment.

### 17. SIGMA: Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
- **Authors**: Anonymous
- **Affiliation**: Alibaba (AliExpress)
- **Link**: https://arxiv.org/abs/2602.22913
- **Key Innovation**: Multi-view alignment framework unifying NL, world knowledge, and item entities; hybrid SID + item-specific ID tokenization; three-step generation with adaptive probabilistic fusion.
- **Abstract**: Instruction-following generative recommender deployed at AliExpress covering diverse recommendation tasks.

### 18. OneMall: End-to-End Generative Recommender Family at Kuaishou E-Commerce
- **Authors**: Kun Zhang, Jingming Zhang, Wei Cheng, Yansong Cheng, Jiaqi Zhang, Hao Lu, et al.
- **Affiliation**: Kuaishou
- **Link**: https://arxiv.org/abs/2601.21770
- **Key Innovation**: Unified framework for product-card, short-video, live-streaming. Query-Former for long sequence compression, Sparse MoE, RL pipeline distilling ranking model. **+13.01% GMV** on product-card.
- **Abstract**: Serves 400M+ DAU across all Kuaishou e-commerce scenarios.

### 19. IDProxy: Cold-Start CTR Prediction with Multimodal LLMs
- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, et al.
- **Affiliation**: Xiaohongshu
- **Link**: https://arxiv.org/abs/2603.01590
- **Key Innovation**: MLLM-generated proxy embeddings aligned with ID embedding space, optimized end-to-end under CTR objectives. Handles cold-start items without usage data.
- **Abstract**: Deployed in Content Feed and Display Ads at Xiaohongshu.

### 20. DS-MLP: Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Affiliation**: Renmin University / ByteDance / Meituan
- **Link**: https://arxiv.org/abs/2606.04944
- **Key Innovation**: Vanilla MLP achieving SOTA via knowledge distillation — main MLP captures implicit interactions, parallel MLP distills explicit high-order interactions from a teacher.
- **Abstract**: Scalable, efficient solution outperforming complex architectures across three benchmarks.

### 21. Dual-Stream MLP for CTR (above) / GRAB: Generative Ranking for Ads at Baidu
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, et al.
- **Affiliation**: Baidu
- **Link**: https://arxiv.org/abs/2602.01865
- **Key Innovation**: Causal Action-aware Multi-channel Attention (CamA) captures temporal dynamics. Linear scaling behavior with longer sequences. **+3.05% revenue, +3.49% CTR**.
- **Abstract**: LLM-inspired sequence-first generative paradigm replacing DLRMs at Baidu.

### 22. RankUp: Towards High-rank Representations for Large Scale Advertising
- **Authors**: Anonymous
- **Affiliation**: Tencent
- **Link**: https://arxiv.org/abs/2604.17878
- **Key Innovation**: MetaFormer-based architecture with mechanisms to mitigate embedding collapse. GMV **+3.41%** (Video Accounts), **+4.81%** (Moments), **+2.12%** (Official Accounts).
- **Abstract**: Full deployment across Weixin advertising scenarios on 32 online optimization objectives.

### 23. GEM-Rec: Bid-Aware Generative Recommendation (One Model, Two Markets)
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2603.22231
- **Key Innovation**: Control tokens decouple ad-placement decision from item selection. Bid-Aware Decoding injects real-time bids at inference with monotonicity guarantee.
- **Abstract**: Unified framework for organic + sponsored recommendation without retraining for bid changes.

### 24. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Authors**: Anonymous
- **Affiliation**: Academic / Industry
- **Link**: https://arxiv.org/abs/2601.18251
- **Key Innovation**: Generative next-item-prediction produces candidate interest cohorts as explicit intent representations. Hierarchical candidate-aware network aligns cohorts with ranking.
- **Abstract**: Addresses overfitting to historical features and point-wise ranking misalignment. Published at WWW 2026.

### 25. DAIAN: Deep Adaptive Intent-Aware Network for CTR in Trigger-Induced Recommendation
- **Authors**: Anonymous
- **Affiliation**: Xianyu (Alibaba)
- **Link**: https://arxiv.org/abs/2602.13971
- **Key Innovation**: Models user intent as preference distribution relative to trigger item; hybrid enhancer combining ID and semantic information. **+1.59% CTR** on Xianyu.
- **Abstract**: Deployed in Trigger-Induced Recommendation (TIR) scenario at Alibaba.

### 26. S-GRec: Personalized Semantic-Aware Generative Recommendation with Asymmetric Advantage
- **Authors**: Anonymous
- **Affiliation**: Tencent (WeChat Channels)
- **Link**: https://arxiv.org/abs/2602.10606
- **Key Innovation**: A2PO fuses business and semantic objectives in advantage space. LLM-as-Judge for offline evaluation. **+1.19% GMV, +1.16% CTR** in online A/B test.
- **Abstract**: Deployed on 5% WeChat Channels advertising traffic.

### 27. LASAR: Latent Adaptive Semantic Aligned Reasoning for Generative Recommendation
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2605.10207
- **Key Innovation**: First latent reasoning framework for generative recommendation. Two-stage SFT + CoT semantic alignment + REINFORCE-based adaptive step control. ~20× faster than explicit CoT.
- **Abstract**: Nearly halves latent steps while improving recommendation quality.

---

## Games & Multi-Agent RL

### 28. T-STAR: Tree-structured Self-Taught Agent Rectification
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2604.07165
- **Key Innovation**: Consolidates trajectories into a Cognitive Tree; Introspective Valuation back-propagates rewards through tree; In-Context Thought Grafting synthesizes corrective reasoning at divergence points.
- **Abstract**: Outperforms GRPO on embodied, interactive, reasoning, and planning tasks.

### 29. Group-Graph Policy Optimization (G2PO) for Long-Horizon Agentic RL
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.22995
- **Key Innovation**: Transforms linear trajectories into state-transition graph. Group-aggregation state-value estimation reduces sampling variance.
- **Abstract**: Explicitly models graph structure of state transitions for finer-grained credit assignment.

### 30. Agentic Transformers Provably Learn to Search via Reinforcement Learning
- **Authors**: Yuejie Chi et al.
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.00183
- **Key Innovation**: Constructs two-head transformer implementing randomized DFS. RL training dynamics (depth-wise curriculum) provably recovers this mechanism with depth generalization.
- **Abstract**: Theoretical analysis of how attention heads specialize for search in RL-trained transformers.

### 31. SPIRAL (listed above / Section on Games)
- **Note**: Also listed under LLM Training. Self-play on zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) produces transferable reasoning capabilities across 8 benchmarks.

### 32. From Trainee to Trainer: LLM-Designed Training Environment for RL
- **Authors**: Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo
- **Affiliation**: HKUST (GZ) / University of Cambridge
- **Link**: https://arxiv.org/abs/2606.17682
- **Key Innovation**: LLM-as-Environment Engineer — current policy model analyzes failure trajectories and proposes next-stage environment config changes. The RL checkpoint is a better environment engineer than the base model.
- **Abstract**: MAPF-FrozenLake testbed; outperforms GPT, Gemini as environment designers with Qwen3-4B backbone.

---

## Sequence Modeling & Architecture

### 33. MiniMax Sparse Attention (MSA)
- **Authors**: Anonymous
- **Affiliation**: Industry
- **Link**: https://arxiv.org/abs/2606.13392
- **Key Innovation**: Blockwise token selection with small top-k. Ultra-lightweight Index Branch (2 proj matrices). Exp-free TopK kernel for small-k regime. KV-outer order execution.
- **Abstract**: GQA-based sparse attention designed for practical GPU speedups with minimal overhead.

### 34. Recurrent Transformer: Greater Effective Depth and Efficient Decoding
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2604.21215
- **Key Innovation**: Each layer uses its own key-value memory (vs shared in Feedback Transformer). Layerwise recurrence enables deeper-in-time representation. I/O-aware exact evaluation algorithm.
- **Abstract**: Demonstrates increased effective depth via layerwise temporal recurrence.

### 35. Cubit: Token Mixer with Kernel Ridge Regression
- **Authors**: Chuanyang Zheng, Jiankai Sun, Yihang Gao, Yuehao Wang, Liangchen Tan, Mac Schwager, et al.
- **Affiliation**: Academic / Industry
- **Link**: https://arxiv.org/abs/2605.06501
- **Key Innovation**: Replaces Nadaraya-Watson regression (standard attention) with closed-form KRR solution. Limited-Range Rescale for training stability.
- **Abstract**: Performance gains over Transformer increase with sequence length. Potential next-gen architecture.

### 36. Superlinear Multi-Step Attention
- **Authors**: Yufeng Huang
- **Affiliation**: Industry
- **Link**: https://arxiv.org/abs/2601.18401
- **Key Innovation**: O(L^{1+1/N}) complexity with N-step search. N=2 instantiation yields O(L^{3/2}). 109 tok/s at 1M context, 76 tok/s at 10M on single B200. No positional exclusion.
- **Abstract**: Subquadratic attention with full random-context access via multi-step span search.

### 37. Towards Tight Bounds for Streaming Attention (KV Cache Compression)
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.07205
- **Key Innovation**: Nearly tight upper/lower bounds on space complexity for streaming attention approximation. Combines discrepancy-based coresets, polynomial method, and space partitioning.
- **Abstract**: New lower bound technique using INDEX problem with side information.

---

## Multimodal LLMs

### 38. UniAR: Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer
- **Authors**: Wujian Peng et al.
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.18249
- **Key Innovation**: Single discrete visual tokenizer serving understanding and generation. Lookup-free bitwise quantization; parallel-bitwise-prediction for shorter visual sequences.
- **Abstract**: Achieves SOTA image generation and editing while competitive on understanding benchmarks.

### 39. Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation
- **Authors**: Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar, et al.
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2606.27376
- **Key Innovation**: Self-evolving framework with Proposer/Solver/Generator roles using only unlabeled images. Solver Token Entropy (STE) for stability. Multi-scale evaluation for generation.
- **Abstract**: +3.5% MMMU, GenEval 82%→85% without human annotations or external reward models.

### 40. LVRPO: Language-Visual Alignment with GRPO for Multimodal Understanding and Generation
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2603.27693
- **Key Innovation**: Treats multimodal consistency as preference signal for GRPO optimization rather than static representation alignment.
- **Abstract**: Behavior-driven reinforcement for cross-modal alignment without auxiliary encoders.

### 41. MegaScale-Omni: Hyper-Scale MLLM Training System
- **Authors**: Anonymous
- **Affiliation**: Industry
- **Link**: https://arxiv.org/abs/2605.08962
- **Key Innovation**: Decoupled parallelism strategies for encoders (long-short seq parallelism) + 5D parallelism for LLM backbone. Workload-resilient encoder-LLM joint pipeline. 1.27×–7.57× throughput improvement.
- **Abstract**: Deployed on thousands of GPUs with production dynamic workloads.

### 42. iGVLM: Dynamic Instruction-Guided Vision Encoding for Question-Aware Multimodal Understanding
- **Authors**: Anonymous
- **Affiliation**: Academic
- **Link**: https://arxiv.org/abs/2603.02748
- **Key Innovation**: Dual-branch architecture separating static and dynamic perception pathways. Frozen vision encoder + lightweight instruction-conditioned adapters.
- **Abstract**: Instruction-aware visual encoding without retraining backbone. MM4 diagnostic benchmark contributed.

---
