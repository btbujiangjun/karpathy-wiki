---
title: "arXiv Daily Digest — 2026-07-31"
type: synthesis
created: 2026-07-31
updated: 2026-07-31
tags: [arxiv, survey, llm, recommendation, ctr, advertising, games, rl, sequential-modeling, agents]
---

# arXiv Daily Digest — 2026-07-31

> Curated from arXiv submissions across AI, LLMs, recommendation systems, CTR prediction, advertising/bidding, sequential modeling, games, and multi-agent systems. Sources from Jul 29–31, 2026 (cs.AI, cs.CL, cs.LG, cs.IR).

---

## 1. LLM Reasoning & RL Post-Training

### β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation
- **Authors**: Jiawei Xu, Minghui Liu, Juzheng Zhang, Tom Goldstein, Furong Huang et al. (University of Maryland)
- **Date**: 2026-07-31
- **Link**: [2607.28582](https://arxiv.org/abs/2607.28582)
- **Abstract**: Shows vanilla on-policy self-distillation (OPSD) is the β=1 member of a policy-optimization family where β weights the KL anchor to a reference policy. The optimal policy is a geometric interpolation between reference and privileged teacher; rather than optimizing the costly RL objective, it converts the closed-form solution into a distillation target by mixing token-level logits, with return-to-go credit assignment.
- **Key Innovation**: Unifies OPSD and RL by making β a tunable KL knob whose optimal policy is realized via logit mixing instead of RL.

### CSCR: Counterfactual Sensitivity Credit Reallocation
- **Authors**: Qiangqiang He, Zhongheng Wu, ZiJian Wang et al.
- **Date**: 2026-07-30
- **Link**: [2607.27888](https://arxiv.org/abs/2607.27888)
- **Abstract**: Critic-free RL like GRPO broadcasts response-level rewards uniformly across tokens. Counterfactual re-scoring shows most tokens shift the same way under opposing outcome conditions, so privileged shifts mostly reflect counterfactual sensitivity rather than token learning value. CSCR downweights sensitive tokens and renormalizes advantages, beating GRPO on long-CoT math benchmarks.
- **Key Innovation**: Token-level credit reallocation that preserves the credit budget and verifier-determined direction.

### LSPO: LoRA Scaffolded Policy Optimization
- **Authors**: Ken Ding
- **Date**: 2026-07-30
- **Link**: [2607.27787](https://arxiv.org/abs/2607.27787)
- **Abstract**: On "cliff" prompts where every sampled rollout fails, group-normalized advantage is zero so GRPO produces no gradient. LSPO detects cliffs, fits a LoRA adapter on their solutions, re-rolls with base+adapter, splices successes back with an importance-sampling correction, then GRPO-steps the base alone. Beats DAPO on all 16 cells on DeepMath-103K (avg +3.8 pts).
- **Key Innovation**: Sampling-time LoRA scaffold that recovers lost gradient on zero-reward cliffs, then is discarded for a base-only model.

### CoRT: Counterfactual Replay for Token-Level Rubric-Guided RL
- **Authors**: Bo-Wen Zhang, Junwei He, Wen Wang, Song-Lin Lv et al.
- **Date**: 2026-07-29
- **Link**: [2607.25659](https://arxiv.org/abs/2607.25659)
- **Abstract**: Rubric-based RL collapses structured judgments into a scalar reward broadcast uniformly across tokens. CoRT rescoring the same response under rubric-conditioned vs criteria-free prompts yields tokenwise weights that redistribute the GRPO advantage with no auxiliary scorer. Beats response-level GRPO in most comparisons (avg +4.4 pts).
- **Key Innovation**: Policy-internal counterfactual likelihood contrasts as a within-response credit signal for GRPO.

### HARGO: Heterogeneity-Aware Reward-Guided Optimization for RL Post-Training of LLMs on HPC Tasks
- **Authors**: Tiangang Li, Xiangbo Tian
- **Date**: 2026-07-31
- **Link**: [2607.28301](https://arxiv.org/abs/2607.28301)
- **Abstract**: HPC tasks are highly heterogeneous (up to 58x answer-length variation, three reward distributions), making uniform-weight RL like GRPO suboptimal. HARGO adds per-response importance weighting via confidence-modulated advantage, combining a group-level reward-contrast discrimination signal with a reference-model log-probability confidence signal, without task-type labels. Best WinRate (54.62%), Data Race F1 (91.30%), PLP Similarity (0.8558) across four HPC tasks and nine methods.
- **Key Innovation**: Confidence-modulated importance weighting for RL post-training on heterogeneous multi-reward domains.

### Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for Compute-Efficient RLVR (SARA)
- **Authors**: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes et al.
- **Date**: 2026-07-30
- **Link**: [2607.26253](https://arxiv.org/abs/2607.26253)
- **Abstract**: Frames per-step rollout collection as a budget-constrained optimal stopping problem: SARA keeps a Beta posterior over each prompt's success rate and applies a two-threshold SPRT-style rule to commit/abandon groups early, reallocating freed budget to fresh prompts. Matches DPS at 22% fewer rollouts on math reasoning/planning (1.5B/3B); composing with DPS gives best accuracy at 67% fewer rollouts.
- **Key Innovation**: Adaptive early-stopping of rollout allocation per prompt to cut RLVR compute.

### HiFloat4: FP4 End-to-End RL Post-Training
- **Authors**: Hei Yi Mak, Shadan Golestan, Hoang Le, Mehran Taghian Jazi et al.
- **Date**: 2026-07-29
- **Link**: [2607.26515](https://arxiv.org/abs/2607.26515)
- **Abstract**: First end-to-end FP4 RL post-training (rollout + training at 4-bit). The dominant failure is rollout activation quantization: outliers stretch the dynamic range so many activations underflow to zero. Rollout-ResQ (sparse residual on FP4 rollout matmul) plus the HiFloat4 hierarchical-scaling format closes the BF16 gap from 4.9% to 1.1% on Qwen2.5-3B/Math-7B.
- **Key Innovation**: Rollout-side residual correction + hierarchical-scaling 4-bit format enabling FP4 RL within 1.1% of full precision.

---

## 2. LLM Agents & Multi-Agent Systems

### TAPO: Transition-Aware Policy Optimization for LLM Agents
- **Authors**: Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu et al.
- **Date**: 2026-07-31
- **Link**: [2607.27973](https://arxiv.org/abs/2607.27973)
- **Abstract**: RL post-training for LLM agents relies mostly on sparse task rewards, ignoring dense environmental feedback available after actions. TAPO alternates policy optimization with transition supervision, adding action-conditioned next-observation prediction on a shared backbone, motivated by theory linking generalization to predictive environmental knowledge. Lightweight and plug-and-play (no expert data, no extra sampling); improves over pure policy-optimization baselines on WebShop and ALFWorld across scales and algorithms.
- **Key Innovation**: Joint transition-model supervision as a plug-in for agent policy optimization.

### ClawTrack: Towards Trace-Level Evaluation of Real-World Autonomous Agents
- **Authors**: Xingjian Wu, Xuhang Zhu, Xingchen Liu, Junlin Liu et al.
- **Date**: 2026-07-31
- **Link**: [2607.28037](https://arxiv.org/abs/2607.28037)
- **Abstract**: Most agent benchmarks judge only final outcomes. ClawTrack is a dual-assessment benchmark scoring both Task Score (what) and Process Score (how), covering 320 tasks in 8 domains with 25+ deterministic mock services and 12,541 rubric items. Across 16,000+ trials with 21 models, process scores attribute outcomes to reasoning dimensions, filter lucky passes, and reveal result verification as the systematic bottleneck. Trajectory filtering consistently improves post-training across model scales.
- **Key Innovation**: Process-level (trace) evaluation with rubric attribution for agent post-training.

### Why Are GUI Agents Correct but Late? (AAPT)
- **Authors**: Zihan Dong, Rui Qian, Qishi Zhan, Dongshen Peng et al.
- **Date**: 2026-07-31
- **Link**: [2607.28399](https://arxiv.org/abs/2607.28399)
- **Abstract**: Computer-use agents often produce correct actions only after transient GUI events have closed, due to expensive autoregressive decoding on the decision-time critical path. AAPT eliminates this delay without modifying the model: during idle periods it builds a bounded conditional policy tree (guards, pre-authorized actions, deadlines) sized to the model's latency, and a lightweight observer executes prepared branches on event. Success improves 0.50→0.79 with no incorrect actions; open-loop/predict-and-replan baselines get zero.
- **Key Innovation**: Latency-matched pre-compiled policy trees that move decoding off the decision-time critical path.

### Flux-OPD: On-Policy Distillation with Evolving Contexts
- **Authors**: Yuran Wang, Zekun Wang, Bohan Zeng, Ruixu Zhang et al.
- **Date**: 2026-07-31
- **Link**: [2607.28022](https://arxiv.org/abs/2607.28022)
- **Abstract**: Open-ended LLM training lacks verifiable rewards; contexts can encode preferences but give little supervision once distilled. Decomposing the reverse-KL objective shows the student is distilled toward the geometric mean of context-conditioned teachers plus a conflict term measuring disagreement. Flux-OPD treats context-conditioned-vs-free teacher differences as correction signals injected into the context-free anchor, weighted by the conflict indicator.
- **Key Innovation**: Conflict-weighted correction signals stabilize distillation with evolving contexts.

### CaM-Wolf: Causal-Aware Multimodal Agents for Social Deduction Games
- **Authors**: Zheng Zhang, Nanjie Yao, Jiarui He, Deheng Ye et al. (Tencent AI Lab, inferred)
- **Date**: 2026-07-29
- **Link**: [2607.26393](https://arxiv.org/abs/2607.26393)
- **Abstract**: First multimodal social-deduction game (Werewolf) agent: processes other players' video, uses a causal-aware Reasoner trained via RL to link observed behavior to hidden roles, and presents itself via an animated avatar. User study shows superior gameplay and improved human-AI interaction quality (ACMMM 2026).
- **Key Innovation**: Causal-aware, RL-trained multimodal agent with video perception and avatar embodiment.

### ParliamentBench: Can Agents Deceive?
- **Authors**: Niklas Bauer, Lars Benedikt Kaesberg, Akiko Aizawa, Jan Philip Wahle et al. (Göttingen/NII)
- **Date**: 2026-07-30
- **Link**: [2607.28146](https://arxiv.org/abs/2607.28146)
- **Abstract**: Open-source Secret-Hitler-based benchmark evaluating 16 LLMs over 1,600 matches with three metrics isolating social deduction, reasoning, and deceptive consistency. A top-four cluster (GPT-5.4, Kimi K2.5, Grok 4.1 Fast, DeepSeek 3.1 Terminus) emerges while the weakest models fall below random (33%) / algorithmic (45%) baselines; most LLMs fail to keep a deceptive persona consistent, dropping below 50% retention.
- **Key Innovation**: Benchmark + metrics isolating deception retention under information asymmetry.

---

## 3. CTR Prediction & Advertising

### CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent
- **Authors**: Yunlong Wang, Huizhe Zhang, Haonan Hu, Yudong Li et al. (Tencent)
- **Date**: 2026-07-31
- **Link**: [2607.28070](https://arxiv.org/abs/2607.28070)
- **Abstract**: Unifies cross-field feature interaction (field-separated cross attention) with long-sequence subspace token mixing and a hierarchical sequence compression with progressively expanded receptive fields. Online A/B: +3.57% CTR and +1.71% ad revenue with 2.21x faster training vs. HSTU; fully deployed in Tencent production.
- **Key Innovation**: Field-separated cross attention + hierarchical sequence compression to unlock scaling under latency/resource constraints.

### ROCS: Request-Oriented Compute Sharing for Efficient Large-Scale Recommendation (Meta)
- **Authors**: Yuxin Chen, Liang Luo, Buyun Zhang, Jian Jiao et al. (Meta, 47 authors)
- **Date**: 2026-07-31
- **Link**: [2607.27744](https://arxiv.org/abs/2607.27744)
- **Abstract**: Exploits that one user request is scored against many candidates while request-side features are shared. ROCS defers request-candidate interactions, isolates candidate-dependent representations, and evaluates most of the model once per request via Generalized Layer Masking (feature interaction) and Deep Cross Attention (sequence), co-designed with in-kernel broadcast optimization. Up to 3x QPS on retrieval and 50% QPS gain with 0.5% LogLoss improvement on ranking; deployed across Meta ads and organic surfaces.
- **Key Innovation**: Restructures recommendation inference from per-candidate to per-request compute with candidate-isolation masking.

### ReAlloc: Multi-Channel Uplift Policy Learning (Alibaba Taobao)
- **Authors**: Changjian Liu, Tianyu Wang, Xiaoxuan Deng, WenTao Zhu et al. (Alibaba)
- **Date**: 2026-07-31
- **Link**: [2607.28182](https://arxiv.org/abs/2607.28182)
- **Abstract**: Formulates cross-channel marketing budget allocation as a simplex-constrained uplift decision problem. An Orthogonal Teacher extracts unbiased local gradients from short-term logs while an Explanation-Guided Student distills them into a long-horizon marginal field, yielding support-aware, conservative allocations that capture cross-channel substitution. Online A/B on Taobao lifts both pay order and income.
- **Key Innovation**: Fast-slow (short-term teacher / long-term student) causal uplift framework for budget allocation.

### SWAG-Bid: Sliding-Window Aware Generative Auto-Bidding
- **Authors**: Binglin Wu, Chuan Yue, Yingyi Zhang, Xianneng Li et al. (Alibaba AliExpress)
- **Date**: 2026-07-29
- **Link**: [2607.25233](https://arxiv.org/abs/2607.25233)
- **Abstract**: Handles cross-episode coupling where daily bids affect up to W=7 overlapping evaluation windows. A Masked Trajectory Model plans and Multi-Window Model Predictive Control Sampling scores candidate plans across all windows; a Per-Step Gated AdaLN controller adapts reliance on the guidance. Validated on AuctionNet-Sparse and AliExpress online A/B.
- **Key Innovation**: Treats auto-bidding as a sliding-window (multi-episode) optimization problem instead of independent per-day episodes.

### PlatformBid + BidFlow: An Auto-Bidding Benchmark from a Unified Advertising Platform's Perspective (Kuaishou)
- **Authors**: Shengtian Yang, Yewen Li, Peng Jiang, Zhiyi Lyu, Bo An, Qingpeng Cai, Lei Feng (Kuaishou)
- **Date**: 2026-07-31
- **Link**: [2607.27265](https://arxiv.org/abs/2607.27265)
- **Abstract**: First auto-bidding benchmark built from a unified SSP+DSP+Ad-Exchange platform's perspective (optimizing both advertiser conversions and platform revenue), with homogeneous, heterogeneous, and promotional competition settings. Evaluates control, RL, and generative methods; introduces BidFlow, a flow-matching-based bidder. Online: +0.68% target cost on Kuaishou.
- **Key Innovation**: Platform-centric (not advertiser-centric) benchmark design plus a flow-matching generative bidder.

### HOBA: Hierarchical On-Policy Bidding Agents (Kuaishou, KDD 2026)
- **Authors**: Ji Wu, Yunshan Peng, Wentao Bai, Yunke Bai et al. (Kuaishou)
- **Date**: 2026-07-29
- **Link**: [2607.24779](https://arxiv.org/abs/2607.24779)
- **Abstract**: Hierarchical RL bidding across three time scales: an LLM high level infers hyperparameters via a Think-Act-Observe-Reflect loop, a SARSA mid level selects among expert models with causal bias correction, and a low-level expert pool (PID, MPC, IQL, Decision Transformer) executes bids. Restricting online learning to discrete expert selection cuts exploration risk; +3.6% target cost in large-scale deployment.
- **Key Innovation**: LLM + SARSA hierarchical model selection confines online learning to discrete choice, avoiding continuous-bid online RL instability.

---

## 4. Recommendation Systems

### Building a User Foundation Model for the Open Web
- **Authors**: Solal Vernier, Ivan Can Arisoy, Merwan Barlier, Blaž Škrlj (RecSys'26)
- **Date**: 2026-07-31
- **Link**: [2607.28019](https://arxiv.org/abs/2607.28019)
- **Abstract**: Open-web RTB has fragmented identity and mostly aggregated counters, breaking assumptions of stable persistent identity. Pre-trains a Transformer encoder with MLM plus a sequence-level contrastive objective, then fine-tunes on click prediction, optimizing the pipeline via LLM-in-the-loop search over code-level "lifter" edits. +1.197% RIG on production bid-win-rate model, +1.354% RIG on CTR ranker; 7-day live A/B: +2.13% CTR and −1.13% eCPC.
- **Key Innovation**: User foundation model pre-training designed for fragmented-identity open-web RTB, with LLM-driven pipeline search.

### Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study (Google Discover)
- **Authors**: Di Bai, Jintao Liu, Zhenwei Tang, Peifan Wu et al. (Google, RecSys 2026 Industry)
- **Date**: 2026-07-31
- **Link**: [2607.27577](https://arxiv.org/abs/2607.27577)
- **Abstract**: Google Discover's unified feed spans heterogeneous open-web content with distinct feature densities and interaction patterns, making a single unified ranker hard without negative transfer or majority bias. Introduces HA-MoE, a heterogeneity-adaptive multi-gated mixture-of-experts injecting explicit heterogeneity context into gating and expert representations, plus LENS, a lightweight observability framework tracking expert specialization, evaluated with Dual-Level AUC. Online A/B confirms gains in feed activity and exploration metrics.
- **Key Innovation**: Heterogeneity-context-injected MoE for unified ranking over mixed-content feeds.

### OneShot: Index-in-Ranking with Neural Scoring for Large-Scale Retrieval (Meta)
- **Authors**: Ziwei Li, Shuyao Li, Xufeng Cai, Xue Zou et al. (Meta Instagram, fully deployed)
- **Date**: 2026-07-31
- **Link**: [2607.27475](https://arxiv.org/abs/2607.27475)
- **Abstract**: Aligns indexing with ranking objectives via an end-to-end in-model index-learning framework, then scales interaction modeling with neural scoring beyond the dot-product bottleneck. Fully deployed in Instagram's short-video recommender: wins in daily sessions/engagement/time-spent, 20% recall gain at operational ranking volume and 10x efficiency at equivalent recall.
- **Key Innovation**: In-model learned index co-trained with ranking objectives + neural scoring beyond dot-product.

### Memory Layer: Train the In-Model Cache for Recommendation Models (Meta)
- **Authors**: Liangyuan Na, Gufan Yin, Yixin Bao, Xianjie Chen et al. (Meta Instagram)
- **Date**: 2026-07-29
- **Link**: [2607.25110](https://arxiv.org/abs/2607.25110)
- **Abstract**: Early ranking stages cache precomputed item embeddings outside the training loop, so training and serving use different representations. The memory layer is an in-model key-value embedding cache co-trained with the model — the item tower writes embeddings at training, the model reads them at serving. On Instagram Reels: coverage 96%→100%, embedding freshness ~5 min→~20 s, train-serve NE gap narrowed up to 86%, >2x recall on freshest content, 5–6% cold-start engagement lift, 30% compute cut.
- **Key Innovation**: End-to-end trainable in-model KV cache giving one source of truth for item embeddings.

### Tokens are All You Need: Dual-Purpose Semantic IDs (Google / major video platform)
- **Authors**: Baolei Li, Yiping Yuan, Yilin Zheng, Likang Yin et al. (RecSys 2026)
- **Date**: 2026-07-29
- **Link**: [2607.24865](https://arxiv.org/abs/2607.24865)
- **Abstract**: Targets the "Memory Wall" from massive dense embedding tables. Dual-purpose Semantic IDs use hierarchical quantization to condense embeddings into discrete tokens serving as both Collaborative Identity (learnable interaction table) and Content Reconstruction (a lightweight Semantic Decoder reconstructs embeddings on demand), replacing massive vector storage with on-the-fly reconstruction. Validated offline and in production-scale ranking/retrieval at a major video platform.
- **Key Innovation**: Single discrete token serving as both collaborative identity and content source via on-demand reconstruction.

### Guess Where You Go: Generative Next Point-of-Interest Recommendation in Amap (Alibaba)
- **Authors**: Penglong Zhai, Bowen Zheng, Jie Li, Yifang Yuan et al. (Amap/Alibaba)
- **Date**: 2026-07-30
- **Link**: [2607.26073](https://arxiv.org/abs/2607.26073)
- **Abstract**: End-to-end framework combining SID generation with LLM-based generative next-POI recommendation: a contrastive residual-quantization tokenizer aligns textual, visual, spatial, and collaborative signals into discriminative SIDs, then LLMs are adapted via continued pretraining, SFT, and Exposure-Aware Kahneman-Tversky Optimization (EAKTO) for behavioral preference alignment. Long-term online A/B on Amap homepage: +5.83% P-CTR and +6.20% U-CTR over production.
- **Key Innovation**: LLM generative retrieval for next-POI with exposure-aware behavioral alignment.

---

## 5. Generative Recommendation

### LoopMemGR: From Behavior Logs to Evolving Memory for Generative Recommendation (Taobao)
- **Authors**: Hui Qian, Changfa Wu, Chang Liu, Binbin Cao et al. (Alibaba Taobao)
- **Date**: 2026-07-31
- **Link**: [2607.27647](https://arxiv.org/abs/2607.27647)
- **Abstract**: Generative recommenders treat history-as-context and discard the system's own past recommendation decisions, creating asymmetric memory that cannot reuse preference-validation, negative, or exploration signals. LoopMemGR adds a closed-loop recommendation experience log alongside behavior logs, extracting request-relevant evidence from recency, frequency, and global views, compressed into fixed experience tokens under a bounded input budget. Validated on an industrial Taobao dataset.
- **Key Innovation**: Closed-loop experience memory (system's own decisions) as first-class context for generative recommendation.

### HiLaR: Hierarchical Latent Reasoning for LLM-Based Recommendation
- **Authors**: Peiyu Hu, Siying Gu, Weihai Lu, Zhuodong Liu et al.
- **Date**: 2026-07-31
- **Link**: [2607.27760](https://arxiv.org/abs/2607.27760)
- **Abstract**: Explicit natural-language reasoning is costly and existing latent reasoning poorly characterizes layer-wise preference roles. HiLaR builds temporal-guided hierarchical user preference representations, aligns them with multiple LLM latent reasoning states (broad preferences → fine-grained intents), and combines final feedback with layer-aware process rewards from marginal target-likelihood gain. Outperforms sequential, generative, and LLM-based baselines on four Amazon benchmarks.
- **Key Innovation**: Layer-aware process rewards over hierarchical latent reasoning states for LLM recommendation.

### From Understanding to Action: Feedback-Grounded Policy Discovery for Generative Recommendation
- **Authors**: Zhi Chen, Minmao Wang, Xingchen Liu, Haoqiang Liang et al.
- **Date**: 2026-07-31
- **Link**: [2607.27789](https://arxiv.org/abs/2607.27789)
- **Abstract**: Semantic-ID generative recommenders capture co-occurrence but LLMs' linguistically plausible reasoning isn't trained on recommendation outcome feedback — an "Understanding-Action Gap". Separates intent knowledge (current demand) from policy knowledge (direction + rejection boundary) and proposes a feedback-driven agent framework that induces intent and discovers policies by incremental utility over an intent-only baseline, evaluated by outcome feedback rather than plausibility. Distilled into two latent tokens of a lightweight Semantic-ID generator for LLM-free inference; online A/B: +4.506% Revenue, +4.621% ADVV.
- **Key Innovation**: Outcome-feedback-driven policy discovery separated from intent, distilled into latent tokens for LLM-free serving.

### Restoring Collaborative Signals in Semantic-ID Generative Recommendation via Personalized Natural Language
- **Authors**: Changjiang Han, Qingyang Li, Yaqiang Zang, Jikun Kang et al.
- **Date**: 2026-07-31
- **Link**: [2607.27682](https://arxiv.org/abs/2607.27682)
- **Abstract**: Semantic-ID (SID) recommenders struggle to convert explicit reasoning into correct IDs because a compact SID cannot simultaneously hold content and collaborative signal — collaboration loses, capping accuracy. Rather than mapping language onto SIDs or retraining, this framework uses personalized natural language to attach hierarchical collaborative cues during generation. Consistent gains in recommendation accuracy at inference time.
- **Key Innovation**: Inference-time injection of hierarchical collaborative cues via personalized language to fix SID signal loss.

### LGRID: Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation
- **Authors**: Long Zhang, Hao Jiang, Sheng Yu, Fei Pan, Peng Jiang, Kun Gai et al. (Kuaishou, inferred)
- **Date**: 2026-07-31
- **Link**: [2607.27944](https://arxiv.org/abs/2607.27944)
- **Abstract**: Single-representation-then-quantization SID generation entangles attributes (geography, brand, category), causing quantization loss, low-quality SIDs, and collisions. LGRID introduces generative disentanglement via an Encode → Disentangle → Align → Quantize pipeline with a Structured Disentangled Block routing states into attribute-aligned slots and dual-stream residual quantization. Beats strong SID baselines (up to +5.44% relative AUC), >99% coarse-geography attribute decoding, cuts full-SID collisions to 39.9% vs 97.0% for LGSID.
- **Key Innovation**: Interpretable, attribute-disentangled Semantic IDs via LLM-driven generative disentanglement.

### SPARC: Sequence-Aware Progressive Attribute Routing and Compression (Taobao)
- **Authors**: Chang Liu, Changfa Wu, Hui Qian, Binbin Cao et al. (Alibaba Taobao)
- **Date**: 2026-07-29
- **Link**: [2607.25339](https://arxiv.org/abs/2607.25339)
- **Abstract**: Industrial generative recommenders carry heterogeneous attributes (category, brand, price, type, timestamp); expanding them blows up input length while naive compression discards context. SPARC models per-field sequential dependencies for context-aware representations, routes original/contextual/identity representations into multiple slots under fixed capacity, then compresses each historical item to a single token via lightweight cross-item interaction. Outperforms conventional and generative baselines on industrial Taobao and public Amazon data.
- **Key Innovation**: Context-conditioned attribute routing and single-token item compression under fixed capacity.

---

## 6. Sequential Modeling & Architectures

### Raven: High-Recall Sequence Modeling with Sparse Memory Routing (CMU/EPFL)
- **Authors**: Arshia Afzal, Aviv Bick, Eric P. Xing, Volkan Cevher, Albert Gu et al. (CMU/EPFL)
- **Date**: 2026-07-29
- **Link**: [2607.25357](https://arxiv.org/abs/2607.25357)
- **Abstract**: Positions long-context recall as a tradeoff between dense memory writes (SSMs/linear transformers — interference, hard to recover specific tokens) and sparse sliding-window attention (hard eviction at window edge). Raven maintains a fixed set of memory slots updated via learned input-dependent routing of a selected subset each step, mitigating both failure modes. Competitive/stronger than prior linear-time baselines on recall-heavy benchmarks and works when extrapolating to 16x training length.
- **Key Innovation**: Learned sparse routing over fixed memory slots interpolating SSM state density and SWA exact-token storage.

### ClockRoPE: Random Fourier Rotations for Temporal Routine Modeling (Google)
- **Authors**: Yiwen Chen, Joshua Ainslie, Krzysztof Choromanski, Xiang Gao, Su-Lin Wu, Yiping Yuan, Qian Sun et al. (Google)
- **Date**: 2026-07-30
- **Link**: [2607.26369](https://arxiv.org/abs/2607.26369)
- **Abstract**: Shows RoPE's log-linear frequency schedule limits domains needing complex distance-correlation patterns (e.g., temporal periodicity in sequential recommendation), and proves any normalized continuous positive-definite attention modulation can be approximated by random rotations from its own Fourier transform. ClockRoPE derives rotation frequencies from periodic attention modulation functions; consistent online gains and deployed in a production generative retrieval system at a major video platform.
- **Key Innovation**: Generalizes RoPE to arbitrary periodic attention modulations via Random Fourier Rotations.

---

## 7. Efficient LLM Serving & KV Cache

### Back from the Future: KV Cache Management by Counter-Causal Surprise
- **Authors**: Stephen Gould, Anton van den Hengel (ANU / University of Adelaide)
- **Date**: 2026-07-31
- **Link**: [2607.27600](https://arxiv.org/abs/2607.27600)
- **Abstract**: KV eviction rule based on a simple insight: tokens well-predicted from their future context are redundant. The model is run with a counter-causal attention mask (each position attends only to later tokens), reusing stored KV, so eviction scores are in-distribution and require no training. A fast single-layer approximation restricts the counter-causal pass to the last layer. Competitive or better than SOTA eviction across open LLMs and benchmarks.
- **Key Innovation**: Training-free counter-causal (future-attending) scoring of KV entries for eviction.

### Beyond KV Reconstruction: Functional Reconstruction for MLA Draft Models in Speculative Decoding (PKU)
- **Authors**: Weiye Shi, Fanxu Meng, Muhan Zhang (Peking University)
- **Date**: 2026-07-31
- **Link**: [2607.27269](https://arxiv.org/abs/2607.27269)
- **Abstract**: Direct MHA/GQA→MLA conversion harms speculative-decoding draft acceptance because low-rank factorization and RoPE handling introduce attention-function errors. Treats MLA draft construction as functional reconstruction: optimizes each converted MLA module to reproduce the original module's post-output-projection response on calibration hidden states, without verifier logits. Across 192 configs (TransMLA, MHA2MLA, HF/vLLM), materially improves acceptance in 37/64 matched task cells.
- **Key Innovation**: Post-conversion functional (response-level) reconstruction of MLA modules to preserve draft-target agreement.

### InferScale: GPU-Native KV Injection for Personalized LLM Serving
- **Authors**: Peter Li, Prashant Pandey
- **Date**: 2026-07-30
- **Link**: [2607.27090](https://arxiv.org/abs/2607.27090)
- **Abstract**: Replaces repeated prefill of shared personalized memory (Mem0/MemGPT/Zep-style) with reusable KV state: precomputes each memory fact's KV, stores it with a semantic embedding on GPU, retrieves at serving time, and injects directly into vLLM's paged cache. Introduces Chunked RoPE (keys stored unrotated, rotated at serving positions) and Context-Window Encoding. At k=50 cuts TTFT 72–79% (3.6–4.8x) with 3.7–4.5x throughput under load.
- **Key Innovation**: GPU-resident precomputed memory KV with chunked-RoPE position injection, decoupling TTFT from retrieved-context size.

---

## 8. Games & Reinforcement Learning

### Inverse RL Helps Align AI by Imitating Humans (PARED)
- **Authors**: Michał Wiliński, Liu Leqi, Chirag Nagpal
- **Date**: 2026-07-29
- **Link**: [2607.24900](https://arxiv.org/abs/2607.24900)
- **Abstract**: PARED recovers the reward underlying expert demonstrations as an explicit function over a small set of response-level features, learned by a lightweight discriminator separating demonstrations from the policy's own samples — no preference annotations required. The recovered reward improves a base policy via reranking and adversarial on-policy RL, extends SFT-tuned policies, and enables contextual alignment to different audience preferences.
- **Key Innovation**: Demonstrations alone yield an implicit, inspectable reward via discriminator-based inverse RL.

### CaM-Wolf: Causal-Aware Multimodal Agents for Social Deduction Games
- **Authors**: Zheng Zhang, Nanjie Yao, Jiarui He, Deheng Ye et al. (Tencent AI Lab, inferred)
- **Date**: 2026-07-29
- **Link**: [2607.26393](https://arxiv.org/abs/2607.26393)
- **Abstract**: (see §2) First multimodal social-deduction agent that perceives other players' video, learns causal links from behavior to hidden roles via RL, and embodies itself with an animated avatar.
- **Key Innovation**: RL-trained causal-aware reasoner bridging video perception and strategic deception.

### ParliamentBench: Can Agents Deceive?
- **Authors**: Niklas Bauer, Lars Benedikt Kaesberg, Akiko Aizawa, Jan Philip Wahle et al. (Göttingen/NII)
- **Date**: 2026-07-30
- **Link**: [2607.28146](https://arxiv.org/abs/2607.28146)
- **Abstract**: (see §2) Secret-Hitler-based deception/reasoning benchmark over 16 LLMs and 1,600 matches, with metrics isolating social deduction, reasoning, and deceptive consistency.
- **Key Innovation**: Quantitative decomposition of deception retention under information asymmetry.

---

## 9. Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Token-level credit for critic-free RL** | GRPO's uniform broadcast is being replaced by counterfactual/tokenwise credit signals | CSCR, CoRT, LSPO, β-OPSD |
| **RL post-training efficiency** | Budget-aware rollout allocation, 4-bit RL, heterogeneity-aware weighting | SARA, HiFloat4, HARGO |
| **Process/transition supervision for agents** | Moving beyond sparse task rewards to trace- and transition-level learning | TAPO, ClawTrack, Flux-OPD |
| **Generative recommendation deepens** | Outcome-feedback policy learning, closed-loop memory, disentangled/interpretable SIDs | LoopMemGR, HiLaR, Understanding→Action, LGRID, SPARC |
| **Industrial CTR: efficiency + unified modeling** | Compute-sharing inference, cross-field + sequence compression, in-model caches | ROCS, CCFormer, Memory Layer, OneShot |
| **Auto-bidding sophistication** | Multi-window coupling, hierarchical LLM bidding, platform-centric benchmarks | SWAG-Bid, HOBA, PlatformBid/BidFlow |
| **Delayed-feedback & uplift for ads** | Two-clock CVR, multi-channel uplift allocation | TWICE, ReAlloc |
| **Linear-time long-context recall** | Sparse memory routing vs. exact-token storage tradeoffs | Raven, ClockRoPE |
| **Deception & games as AI safety probes** | Social deduction games as evaluation for deceptive capability | ParliamentBench, CaM-Wolf |

---

## Key Takeaways

1. **GRPO is being decomposed token-wise**: A wave of papers (CSCR, CoRT, LSPO, β-OPSD) argues uniform response-level reward broadcast is the core pathology of critic-free RL, and each proposes counterfactual or tokenwise credit without auxiliary critics.
2. **RL post-training is becoming efficiency-critical**: SARA (67% fewer rollouts), HiFloat4 (FP4 RL within 1.1% of BF16), and HARGO (heterogeneity-aware weighting) attack compute cost, quantization, and multi-distribution reward settings.
3. **Agent research moves to process-level signals**: ClawTrack (trace rubrics), TAPO (transition prediction), and AAPT (decode-time critical path) all address what happens *during* execution, not just final outcomes.
4. **Industrial CTR/rec converged on unified efficiency**: ROCS (Meta) computes most of a ranking model once per request; CCFormer (Tencent) beats HSTU at 2.21x faster training; Memory Layer and OneShot (Meta) make the cache and index trainable in-model.
5. **Auto-bidding treats time as coupled**: SWAG-Bid (sliding windows), HOBA (LLM+SARSA hierarchy), and PlatformBid (platform-centric view) move beyond single-episode, advertiser-only optimization.
6. **Generative recommendation matures on memory and interpretability**: LoopMemGR (system's own decisions as memory), LGRID (disentangled SIDs), and Understanding→Action (outcome-feedback policy learning, +4.5% revenue) all shipped or A/B-tested gains.
7. **Deception emerges as a measurable safety property**: ParliamentBench and CaM-Wolf operationalize deceptive consistency in social deduction games, with frontier models (GPT-5.4, Kimi K2.5, Grok 4.1 Fast, DeepSeek 3.1 Terminus) clearly separating from weak models.
