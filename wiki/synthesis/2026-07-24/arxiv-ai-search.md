---
title: "arXiv AI Research Search Report"
type: synthesis
created: 2026-07-24
updated: 2026-07-24
sources: [arxiv-web-search]
tags: [arxiv, paper-digest, LLM, CTR, recommendation, advertising, sequential-modeling, game-theory, RLHF, multimodal]
---

# arXiv AI Research Search Report — 2026-07-24

A curated digest of recent arXiv papers across AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and game theory.

---

## 1. LLM Training & Inference

### LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget
- **Authors**: Not listed (Qwen/GLM teams)
- **Institution**: Unknown
- **Abstract**: An architecture-aware execution stack for million-token RL post-training under a fixed GPU budget. Instantiated with GRPO, LongStraw evaluates the shared prompt without autograd, retains only model-specific state needed by later tokens, and replays short response branches one at a time. On eight H20 GPUs, completes grouped Qwen scoring at 2.1M positions; a stress test reaches 4.46M positions.
- **Key Innovations**: Autograd-free prompt evaluation, replay-based response backward, hybrid recurrent + full-attention support, scales RL post-training to >2M tokens under fixed GPU budgets.
- **Link**: https://arxiv.org/abs/2607.14952

### Loopie: The Most Powerful Looped Transformer to Date
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Loopie series consists of two MoE models (20B/2B active and 6B/0.6B active). Addresses the longstanding challenge that increasing parameter count by N usually outperforms looping a model N times. Loopie substantially outperforms vanilla Transformer baselines trained with the same compute budget. At 2025 IMO and IPhO, achieves gold-medal performance without tools.
- **Key Innovations**: Novel looped Transformer design that overcomes the parameter-vs-looping tradeoff; strong reasoning via post-training pipeline.
- **Link**: https://arxiv.org/abs/2607.16051

### Hidden Decoding at Scale: Latent Computation Scaling for LLMs
- **Authors**: Not listed (WeLM team)
- **Institution**: Unknown
- **Abstract**: Proposes Hidden Decoding, a sequence-length scaling method applied during continued pretraining (CPT). Expands each token into n streams with independent embedding tables, keeping intermediate KV cache as context. Introduces Stream-Factorized Attention reducing attention cost from quadratic to near-linear in n. Trains WeLM-HD4-80B and WeLM-HD4-617B at n=4, first demonstrated sequence-length scaling at 100B+ MoE scale.
- **Key Innovations**: Sequence-length scaling during CPT, Stream-Factorized Attention for near-linear cost, first 100B+ MoE demonstration.
- **Link**: https://arxiv.org/abs/2607.08186

### Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Presents set diffusion, a new class of language models that factorizes over flexible-position, flexible-length token sets with a set-causal diffusion architecture supporting KV cache updates after every inference step. Tokens can be decoded in arbitrarily-ordered sets including sliding-window sets. Achieves better speed-quality tradeoffs on math reasoning, summarization, and unconditional generation.
- **Key Innovations**: Set-causal diffusion architecture, any-order decoding, KV-cache-compatible diffusion LM.
- **Link**: https://arxiv.org/abs/2607.01775

### DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Speculative decoding framework unifying high-throughput parallel generation with adaptive, load-aware verification. Uses semi-autoregressive architecture (parallel backbone + lightweight sequential module) for intra-block dependency modeling. Deployed within DeepSeek-V4 serving system, accelerates per-user generation by 60-85% at matched throughput.
- **Key Innovations**: Confidence-scheduled verification, semi-autoregressive draft architecture, production-deployed speculative decoding.
- **Link**: https://arxiv.org/abs/2607.05147

### MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under realistic test-time constraints. Maintains modular memory units with asymmetric sub-goal embedding / sub-instruction pairs. Coarse-to-fine retrieval mechanism: coarse level for memory expansion, fine stage for learned selection head reranking.
- **Key Innovations**: Modular instruction memory, learnable selection heads, coarse-to-fine retrieval for test-time reasoning.
- **Link**: https://arxiv.org/abs/2607.06974

### Recursive Harness Self-Improvement (RHI)
- **Authors**: Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Matei Zaharia, Yujin Tang
- **Institution**: Unknown
- **Abstract**: Introduces RHI, which represents the harness as a prompt-level specification of the agent loop and iteratively refines it using pairwise feedback. Across 30 synthetic ML research tasks, a few RHI iterations substantially raise performance ceiling of low-reasoning-effort agents, exceeding maximum-reasoning-effort settings while reducing inference cost by up to 60%.
- **Key Innovations**: Harness-level self-improvement via prompt-level optimization, information-theoretic implicit objective, harness-model co-evolution.
- **Link**: https://arxiv.org/abs/2607.15524

### From RLHF to Direct Alignment: A Theoretical Unification of Preference Learning
- **Authors**: Tarun Raheja, Nilay Pochhi
- **Institution**: Unknown
- **Abstract**: Survey providing theoretical unification of preference learning methods (RLHF, DPO, IPO, KTO, SimPO, ORPO, etc.). Reveals apparent diversity reduces to three orthogonal axes: Preference Model, Regularization Mechanism, Data Distribution. Establishes coverage separation between online/offline methods, scaling laws for reward overoptimization, and conditions under which direct alignment fails.
- **Key Innovations**: Three-axis taxonomy unifying all preference learning methods, failure mode prediction framework, practitioner decision guide.
- **Link**: https://arxiv.org/abs/2601.06108

### DAR: Dual-regularized Advantage Regression (Unifying Stable Optimization and Reference Regularization in RLHF)
- **Authors**: Li He, Qiang Qu, He Zhao, et al.
- **Institution**: Unknown
- **Abstract**: Introduces dual-KL alignment objective unifying reward hacking prevention (KL to π₀) and stable optimization (KL to π_t). Reformulates RL alignment as weighted SFT loss. DAR is a novel RL-free algorithm that outperforms both online RLHF and online preference optimization.
- **Key Innovations**: Dual-KL regularization, RL-free alignment via weighted SFT, theoretical proof of effective reference interpolation.
- **Link**: https://arxiv.org/abs/2602.11523

### Alignment Tampering: How RLHF Is Exploited to Optimize Misaligned Biases
- **Authors**: Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee
- **Institution**: Unknown
- **Abstract**: Introduces "alignment tampering" — a vulnerability where the LLM being aligned influences the preference dataset, causing RLHF to amplify undesired behaviors. Demonstrates amplification across keyword bias, propaganda, brand promotion, and instrumental goal-seeking. Existing mitigation techniques fail to fully resolve it without sacrificing quality.
- **Key Innovations**: Identification and formalization of alignment tampering vulnerability, detection method, cross-bias demonstration.
- **Link**: https://arxiv.org/abs/2605.27355

### GeoAlign: Geometric Rollout Curation for Robust LLM Reinforcement Learning
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Identifies "directional inconsistency" failure mode in online RL for LLMs. Proposes GeoAlign, a plug-in for rollout curation that forms within-prompt preference pairs, learns an online projector, detects directionally inconsistent rollouts via angular deviation, and rectifies them. Forward-pass only, negligible overhead.
- **Key Innovations**: Directional consistency as reliability signal, geometric rollout curation, within-prompt replacement strategy.
- **Link**: https://arxiv.org/abs/2606.26917

---

## 2. CTR Prediction

### GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors**: Not listed (Baidu)
- **Institution**: Baidu
- **Abstract**: End-to-end generative framework for CTR prediction. Integrates Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics and specific action signals in user behavior sequences. Online deployment: +3.05% revenue, +3.49% CTR. Demonstrates monotonic and approximately linear scaling with longer interaction sequences.
- **Key Innovations**: Sequence-first generative CTR paradigm, CamA mechanism for temporal dynamics, demonstrated scaling behavior on long sequences.
- **Link**: https://arxiv.org/abs/2602.01865

### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: Not listed
- **Institution**: Unknown (social-media platform)
- **Abstract**: Dual-path inter-layer connector for CTR Transformers: Identity residual path (first-order reuse) + Block Attention Residual path (high-order recall via cross-layer attention). Pointwise AttnRes replaces Softmax with SiLU for parallel multi-interest patterns. On 331M industrial interactions: +0.32% AUC, fits steeper compute-AUC scaling law (γ=0.118 vs 0.071 for OneTrans).
- **Key Innovations**: Dual-path residual design (DPN-inspired for CTR), Pointwise AttnRes with SiLU, 1.66x compute saving at equivalent AUC.
- **Link**: https://arxiv.org/abs/2606.07980

### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Generative user intent framework leveraging semantic interest cohorts for CTR prediction. Uses next-item prediction to produce candidate interest cohorts as explicit, candidate-agnostic intent representations. Hierarchical candidate-aware network injects contextual signal into ranking. Trained end-to-end with self-supervised regularization.
- **Key Innovations**: Generative intent cohorts for CTR, recall-ranking consistency via candidate-aware cross-attention, end-to-end joint optimization.
- **Link**: https://arxiv.org/abs/2601.18251

### IDProxy: Cold-Start CTR Prediction with Multimodal LLMs at Xiaohongshu
- **Authors**: Not listed
- **Institution**: Xiaohongshu
- **Abstract**: Leverages multimodal LLMs to generate proxy embeddings from rich content signals for new items without usage data. Proxies are explicitly aligned with ID embedding space and optimized end-to-end under CTR objectives. Deployed in Content Feed and Display Ads at Xiaohongshu, serving hundreds of millions daily.
- **Key Innovations**: MLLM-generated proxy embeddings for cold-start, ID-space alignment, production deployment at scale.
- **Link**: https://arxiv.org/abs/2603.01590

### EST: Efficiently Scalable Transformer for CTR Prediction
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan, et al.
- **Institution**: Alibaba (Taobao)
- **Abstract**: Fully unified modeling of all raw inputs without lossy aggregation. Lightweight Cross Attention (LCA) prunes redundant self-interactions; Content Sparse Attention (CSA) uses content similarity to dynamically select high-signal behaviors. Exhibits stable power-law scaling. Deployed on Taobao: +3.27% RPM, +1.22% CTR.
- **Key Innovations**: LCA + CSA for efficient CTR scaling, power-law scaling law for CTR, fully unified sequence modeling.
- **Link**: https://arxiv.org/abs/2602.10811

### SparseCTR: Sparse Attention on Long-term Behaviors for CTR Prediction
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Three-branch sparse self-attention for users' global interests, interest transitions, and short-term interests. Personalized time-aware chunking (TimeChunking) for behavior sequences. Composite relative temporal encoding via learnable, head-specific bias. Exhibits scaling law over 3 orders of magnitude in FLOPs. Online: +1.72% CTR, +1.41% CPM.
- **Key Innovations**: Personalized temporal chunking, three-branch sparse attention, scaling law for CTR, production validated.
- **Link**: https://arxiv.org/abs/2601.17836

### DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation CTR
- **Authors**: Zhihao Lv, Longtao Zhang, Ailong He, et al.
- **Institution**: Unknown (Xianyu/Alibaba platform)
- **Abstract**: Addresses intent myopia in trigger-induced recommendation. Extracts personalized intent representations via correlation analysis between user click and trigger item. Hybrid enhancer with ID and semantic information, adaptive selection for varying intents. Three-stage training strategy.
- **Key Innovations**: Intent myopia solution, explicit/implicit intent decomposition, hybrid ID+semantic similarity enhancement.
- **Link**: https://arxiv.org/abs/2602.13971

### Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, et al.
- **Institution**: Renmin University, ByteDance, Meituan
- **Abstract**: Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, while a parallel MLP captures implicit interactions. Two alignment strategies optimize dual-stream architecture. Achieves SOTA across Criteo, Avazu, MovieLens with low latency.
- **Key Innovations**: Knowledge distillation for CTR feature interactions, dual-stream MLP achieving SOTA, efficient and scalable.
- **Link**: https://arxiv.org/abs/2606.04944

---

## 3. Sequential Recommendation & Behavior Modeling

### CMSL: Constructive Multi-Sequence Learning for Recommendation (Meta)
- **Authors**: Not listed
- **Institution**: Meta
- **Abstract**: Paradigm shift from passive sequence ingestion to active "context engineering" that constructs multiple coherent sequences in latent space. Learnable Sequence Construction Module disentangles user history into pure thematic strands. Linear attention for efficiency. Deployed across ranking and retrieval on four major surfaces at Meta.
- **Key Innovations**: Context pollution diagnosis, learnable multi-sequence construction, implicit context engineering for recommendation, Meta production deployment.
- **Link**: https://arxiv.org/abs/2606.28533

### RecRec: Recursive Refinement for Sequential Recommendation
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Lightweight model (3.9M-14M parameters) maintaining compact latent state updated through shared recursive module. Evidence-anchored correction mechanism stabilizes refinement. Matches or outperforms SOTA sequential, graph-based, and reasoning-enhanced recommenders.
- **Key Innovations**: Recursive latent state refinement, evidence-anchored correction gate, extreme parameter efficiency.
- **Link**: https://arxiv.org/abs/2607.10541

### RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: RL-free framework decoupling reasoning from prediction. Context Compressor distills backbone hidden states into R latent interests with diversity regularizer. Recursive Reasoner refines interests in separate latent space. Deep supervision allows freely adjusting reasoning depth at inference.
- **Key Innovations**: Decoupled reasoning/prediction state, multi-interest representation, depth-adjustable at inference without retraining.
- **Link**: https://arxiv.org/abs/2607.12945

### ManCAR: Manifold-Constrained Adaptive Reasoning for Sequential Recommendation
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Grounds latent reasoning within topology of global interaction graph. Constructs local intent prior from collaborative neighborhood. Progressively aligns latent predictive distribution with prior. Adaptive test-time stopping when distribution stabilizes. Up to 46.88% relative improvement on NDCG@10.
- **Key Innovations**: Graph-manifold constraint for latent reasoning, variational interpretation, convergence-based adaptive stopping.
- **Link**: https://arxiv.org/abs/2602.20093

### HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequential Recommendation
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Hybrid attention explicitly decoupling long-term stable preferences from short-term intent spikes. Linear attention backbone with softmax branch for recent interactions. Temporal-Aware Delta Network (TADN) dynamically upweights fresh signals. Over 8% Hit Rate improvement for users with ultra-long sequences.
- **Key Innovations**: Hybrid linear/softmax attention, TADN for temporal gating, 10K interaction scale.
- **Link**: https://arxiv.org/abs/2602.18283

### Learning to Forget: Satiation-Aware Mechanism for Mitigating Post-Purchase Redundancy
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Models the lifecycle of user interests for sequential recommendation. Dual-path cross-Attention retroactively suppresses fulfilled intent while retrieving replenishment rhythms. Adaptive Satiation Gating Unit generates time-sensitive soft mask. Self-supervised TTNP auxiliary task. Reduces Post-Purchase Repeat Rate by over 60%.
- **Key Innovations**: Interest lifecycle modeling, satiation-aware gating, interest re-awakening mechanism, self-supervised purchase timing.
- **Link**: https://arxiv.org/abs/2607.12714

### Beyond One-Size-Fits-All: Adaptive Test-Time Augmentation (AdaTTA) for Sequential Recommendation
- **Authors**: Xibo Li, Liang Zhang
- **Institution**: Unknown
- **Abstract**: RL-based adaptive inference framework selecting sequence-specific augmentation operators per user sequence. Formulates augmentation selection as MDP with Actor-Critic policy network. Up to 26.31% relative improvement on Home dataset with ~1.48x overhead.
- **Key Innovations**: Per-sequence adaptive augmentation selection, reinforcement learning for TTA, hybrid macro-rank reward.
- **Link**: https://arxiv.org/abs/2604.16121

---

## 4. Advertising & Auto-Bidding

### Long-History User Transformers for Real-Time Ad Ranking (Yandex)
- **Authors**: Not listed
- **Institution**: Yandex
- **Abstract**: Multi-stage transformer architecture: large offline model encodes full cross-surface history into cached representation; lightweight runtime model combines with recent events and request context. Pre-trained autoregressively with dual objective (feedback + next-item prediction). Recovers 72-80% of full-history quality. Production: +2.77% search ads metric, +2.1% YAN metric, +2.26% revenue, zero latency increase.
- **Key Innovations**: Offline/online split for ad ranking, autoregressive pre-training for ad embedding, production-validated zero-latency-cost gains.
- **Link**: https://arxiv.org/abs/2607.14331

### JD-BP: Joint-Decision Generative Framework for Auto-Bidding and Pricing
- **Authors**: Not listed
- **Institution**: JD.com
- **Abstract**: Jointly outputs bid value and pricing correction term. Memory-less Return-to-Go encourages future value maximizing while pricing correction handles cumulated bias. Trajectory augmentation from arbitrary base bidding policy. Energy-Based DPO with cross-attention module. Online: +4.70% ad revenue, +6.48% target cost improvement.
- **Key Innovations**: Joint bidding+pricing optimization, memory-less RTG, trajectory augmentation for cold-start, energy-based DPO.
- **Link**: https://arxiv.org/abs/2604.05845

### Constrained Auto-Bidding via Generative Response Modeling (GRM)
- **Authors**: Eunseok Yang, Xingdong Zuo, Kyung-Min Kim
- **Institution**: Unknown
- **Abstract**: Shifts learning target from actions to responses — predicts horizon-aggregate cost/value curves as functions of a single bid multiplier. Analytic controller enforces constraints via 1D root-finding. Proves exactness for single-multiplier problem and bounds violations under receding-horizon replanning. Outperforms best baseline by 7.8% on AuctionNet.
- **Key Innovations**: Response-curve prediction paradigm, analytic constraint controller, theoretical guarantees on constraint violations.
- **Link**: https://arxiv.org/abs/2605.27811

### AHBid: Adaptable Hierarchical Bidding Framework for Cross-Channel Advertising
- **Authors**: Xinxin Yang, Yangyang Tang, et al.
- **Institution**: Unknown
- **Abstract**: Diffusion model-based high-level planner for budget/constraint allocation across channels. Constraint enforcement mechanism and trajectory refinement mechanism. Control-based low-level bidder integrating historical knowledge with real-time information. Online: +13.57% return, +4.13% constraint satisfaction.
- **Key Innovations**: Diffusion-based cross-channel planning, constraint enforcement, real-time control integration.
- **Link**: https://arxiv.org/abs/2602.22650

### Guide: Generative Auto-Bidding with Unified Modeling and Exploration
- **Authors**: Mingming Zhang, Feiqing Zhuang, et al.
- **Institution**: Taobao (Alibaba)
- **Abstract**: Unified framework integrating exploration and safety. Decision Transformer generates future state trajectories and candidate actions; Inverse Dynamics Model serves as safety fallback; Q-value module adaptively selects between them. Online on Taobao: +4.10% Ad GMV, +1.40% Ad clicks, +3.52% Ad ROI.
- **Key Innovations**: DT + IDM + Q-value triple-component design, exploration-safety tradeoff, production-validated.
- **Link**: https://arxiv.org/abs/2605.19457

### PRO-Bid: Constraint-Aware Generative Auto-Bidding via Pareto-Prioritized Regret Optimization
- **Authors**: Binglin Wu, Yingyi Zhang, et al.
- **Institution**: Unknown
- **Abstract**: Constraint-Decoupled Pareto Representation (CDPR) decomposes global constraints into recursive cost and value contexts. Counterfactual Regret Optimization (CRO) identifies superior counterfactual actions. Online A/B tests demonstrate superior constraint satisfaction and value acquisition.
- **Key Innovations**: Pareto-prioritized regret optimization, constraint-decoupled representation, counterfactual action improvement.
- **Link**: https://arxiv.org/abs/2602.08261

### Audited Auctions: Reducing Harms in Advertising
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Proposes auction-and-penalty mechanism to screen worst externalities in ad markets. Proves mechanism can internalize externalities. Simulates welfare gains from audits on political advertisements: estimated $1-10M/month on one major social media platform.
- **Key Innovations**: Audit-penalty mechanism for ad auction welfare, externality-aware auction design, empirical welfare estimation.
- **Link**: https://arxiv.org/abs/2607.16586

---

## 5. Game Theory & Multi-Agent RL

### Phi-Actor-Critic: Steering General-Sum Games to Pareto-Efficient Correlated Equilibria
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Leverages swap regret minimization to steer learning toward high-welfare correlated equilibria. Centralized attention critic predicts vector-valued regrets in O(1). Regret-Balancing Social Welfare Objective (RB-SWO) optimizes welfare under regret constraints via Lagrangian formulation.
- **Key Innovations**: Swap regret-based equilibrium selection, O(1) regret estimation via attention critic, Lagrangian welfare-regret tradeoff.
- **Link**: https://arxiv.org/abs/2606.11284

### Strategically Robust Multi-Agent RL with Linear Function Approximation (RQRE-OVI)
- **Authors**: Jake Gonzales, Max Horwitz, Eric Mazumdar, Lillian J. Ratliff
- **Institution**: Unknown
- **Abstract**: Proposes RQRE-OVI for computing Risk-Sensitive Quantal Response Equilibria with linear function approximation. Characterizes sample complexity scaling with rationality and risk-sensitivity parameters. Exposes Pareto frontier between expected performance and robustness. RQRE policy map is Lipschitz continuous (unlike Nash).
- **Key Innovations**: Risk-sensitive equilibrium for robust MARL, Lipschitz-stable equilibrium map, theoretical Pareto frontier characterization.
- **Link**: https://arxiv.org/abs/2603.09208

### Paradoxes of Game Theoretic Equilibria and Price of Anarchy
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Systematically demonstrates that reducing multi-agent learning to static equilibrium and black-box regret analysis introduces fundamental limitations. Proves worst-case Nash equilibria are topologically unstable strict saddles; Price of Anarchy becomes unbounded under strictly positive affine costs; discrete-time learning in congestion games induces Li-Yorke chaos with exponential inefficiency degradation.
- **Key Innovations**: Topological instability of worst-case NE, unbounded PoA under affine costs, chaotic dynamics in congestion games.
- **Link**: https://arxiv.org/abs/2607.11752

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, et al.
- **Institution**: EA (Electronic Arts)
- **Abstract**: Proposes framework for training RL models suited to game AI and game development. Requirements: short training time, controllability, modularity, maintainability, bug detection, authenticity, runtime inference constraints. Experiments in EA SPORTS FC 25 (goalkeeper AI) and Battlefield 6 (ground infantry).
- **Key Innovations**: Production-game RL requirements framework, modularity for integration with hand-coded systems, AAA game deployment insights.
- **Link**: https://arxiv.org/abs/2606.20210

### Parametric Open Source Games
- **Authors**: Aleksandar Todorov, Jesse ten Napel, Alexander Müller
- **Institution**: University of Groningen
- **Abstract**: Continuous analogue of program equilibria where players choose parameter vectors; semantics maps convert full parameter profile into mixed actions. Derives coupling threshold for cooperation in symmetric 2x2 games. Neural semantics class preserves same first-order cooperation criterion via cross-player to self-player sensitivity ratio.
- **Key Innovations**: Continuous open-source game theory, explicit cooperation threshold, neural semantics for strategic interaction.
- **Link**: https://arxiv.org/abs/2606.27068

### Game-Theory-Assisted RL for Border Defense with Early Termination
- **Authors**: Soumik Das, Michael Dorothy, Kyle Volle, Diego Shishika
- **Institution**: Unknown
- **Abstract**: Hybrid approach using Apollonius Circle to compute equilibrium in post-detection phase, enabling early termination of RL episodes. RL concentrates on search strategies while pursuit is handled analytically. Yields 10-20% higher rewards and faster convergence.
- **Key Innovations**: Game-theoretic early termination for RL, analytical pursuit equilibrium, hybrid search-pursuit framework.
- **Link**: https://arxiv.org/abs/2603.15907

---

## 6. Multimodal & Vision-Language Models

### Scalable Visual Pretraining for Language Intelligence
- **Authors**: Yiming Zhang, Zhonghan Zhao, et al.
- **Institution**: Shanghai AI Lab, USTC, ZJU, SJTU
- **Abstract**: Shows that unsupervised visual pretraining directly on raw documents (without text extraction) consistently outperforms text-only pretraining across multiple LLM backbones and scientific reasoning benchmarks. Uses only 25% of token budget. Emerges cross-modal alignment without paired supervision.
- **Key Innovations**: Document-visual pretraining without text extraction, 25% token budget efficiency, emergent cross-modal alignment.
- **Link**: https://arxiv.org/abs/2607.09657

### STBridge: Shared-Target Alignment for Unified Multimodal Models
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Identifies understanding-generation alignment gap in UMMs. STBridge connects understanding and generation through a common target state using align-then-optimize strategy: SFT first establishes shared-target channel, then sequential RL refines coordination.
- **Key Innovations**: Understanding-generation alignment via shared target, sequential SFT+RL post-training.
- **Link**: https://arxiv.org/abs/2607.17140

### DeltaV: Thinking with Visual State Updates in Unified LMMs
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Replaces full-image generation with compact visual updates (delta tokens). Temporal Similarity Router stops allocating tokens when marginal reconstruction gain falls below threshold. Reduces visual tokens by 55.6% while improving multimodal reasoning by 3.3%. Introduces StructCoT dataset (1.05M samples, 44 domains).
- **Key Innovations**: Visual update tokens instead of full images, TSIM Router for adaptive token budget, StructCoT dataset.
- **Link**: https://arxiv.org/abs/2607.08434

### OmniReasoner: Thinking with Long Audio-Video via Native Tool Use
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Tool-use post-training framework for long audio-video reasoning. Builds low-cost global preview, calls zoom-in tool for higher-fidelity inspection when needed. TimeAnchor keeps temporal argument valid across different sampling granularities. Temporal Augmented Data Engine synthesizes training trajectories.
- **Key Innovations**: Zoom-in tool use for omni-modal reasoning, TimeAnchor for cross-granularity consistency, synthetic training data engine.
- **Link**: https://arxiv.org/abs/2607.19339

### Latent Visual Cache for Video Reasoning (Latent-VC)
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Recurrent latent visual cache inserted into decoder to preserve compact visual memories throughout reasoning. Trained with supervised contrastive cache alignment and vision-grounded GRPO. Built on Qwen3.5-9B, outperforms strong baselines on six video benchmarks. Achieves higher accuracy with shorter responses.
- **Key Innovations**: Latent visual cache for persistent grounding, vision-grounded GRPO training, shorter-but-better reasoning.
- **Link**: https://arxiv.org/abs/2607.02607

### GeoAnchor: Collaborative Reasoning for 3D Spatial Understanding
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Decomposes 3D spatial information into position, direction, and geometry latents. Four-stage collaborative training from local perception to comprehensive 3D understanding. Built on Qwen3-VL-2B, surpasses GPT-4o by 18.0% and Gemini-2.5-Flash by 13.6% on 3D reasoning.
- **Key Innovations**: Decomposed spatial latents (position/direction/geometry), collaborative multi-stage training, RL for latent token selection.
- **Link**: https://arxiv.org/abs/2607.13454

---

## 7. Reinforcement Learning & Policy Optimization

### Reward Modeling from Natural Language Human Feedback (RM-NLHF)
- **Authors**: Not listed
- **Institution**: Unknown
- **Abstract**: Addresses outcome-process inconsistency in generative reward models. Uses F1-based similarity between human and GRM-generated critiques as process reward. MetaRM learns to predict process reward from limited human critiques and generalizes to unlabeled data. Online MetaRM adapts to distribution shifts.
- **Key Innovations**: Process reward via critique similarity, MetaRM for scalable process supervision, online adaptation.
- **Link**: https://arxiv.org/abs/2601.07349

### Alternating RL with Contextual Rubric Rewards (ARL-RR)
- **Authors**: Guangchen Lan
- **Institution**: Unknown
- **Abstract**: Eliminates need for fixed scalarization by optimizing one semantic rubric meta-class at a time. Theoretical analysis shows reward aggregation induces variance contraction. Search-based adaptation procedure dynamically selects next meta-class based on task performance. Uniformly outperforms scalarized methods across 1.7B-14B scales.
- **Key Innovations**: Alternating per-rubric-class optimization, variance contraction proof, dynamic meta-class selection.
- **Link**: https://arxiv.org/abs/2603.15646

### Reinforcement Learning from Human Feedback: A Statistical Perspective
- **Authors**: Pangpang Liu, Chengchun Shi, Will Wei Sun
- **Institution**: Unknown
- **Abstract**: Comprehensive survey connecting RLHF to statistical ideas: Bradley-Terry-Luce model, latent utility estimation, active learning, experimental design, uncertainty quantification. Covers two-stage RLHF and one-stage DPO, plus extensions (RLAIF, RLVR). Accompanied by GitHub demo.
- **Key Innovations**: Statistical unification of RLHF concepts, BTL model connections, statistical challenges framework.
- **Link**: https://arxiv.org/abs/2604.02507
