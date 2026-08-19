---
title: "arXiv Daily Digest - 2026-08-19"
type: synthesis
created: 2026-08-19
updated: 2026-08-19
tags: [arxiv, daily-digest, ai, llm, recommendation, sequential-modeling, games]
---

# arXiv Daily Digest — 2026-08-19

> Papers from arXiv listings: cs.AI, cs.CL, cs.IR, cs.LG, stat.ML (submitted Aug 18–19, 2026). Curated for relevance to AI, LLMs, recommendation, advertising, sequential modeling, CTR, and games.

---

## 1. Recommendation Systems

### 1.1 UniDot: A Unified Network for Sequence Modeling and Feature Interaction in Large-scale Recommendation
- **Authors**: Rongcheng Lin, Yan Sun, Jamey Zhang, Guanglei Xiong, Ivan Ji, Xianjie Chen, Shujian Bu
- **Affiliation**: KDD Cup 2026 (runner-up, Industrial track)
- **arXiv**: [2608.16797](https://arxiv.org/abs/2608.16797) — cs.IR, cs.AI
- **Key Innovation**: Unifies feature-interaction models (FM) and sequential models into a single architecture. Embedding inner product = attention query-key scoring → single dot-product primitive underlies both feature interaction and sequence modeling. Dual sparse/dense optimizer (Adagrad + Muon), auxiliary conversion-delay head, multi-path mutual learning.
- **Abstract**: Industrial recommenders rely on feature-interaction models and sequential models that have evolved largely independently. UniDot tokenizes non-sequential fields and behavioral sequences into one shared token space. A single macro-block runs a token-mixing bus and a sequence-retrieval bus in parallel, exchanging state through an MLP-Mixer fusion, while an FM Highway carries explicit per-layer dot-product interactions directly to the classifier. Finished runner-up on TAAC KDD Cup 2026 Industrial track.

### 1.2 Once Generated, Ranked: End-to-End Generative Slate Recommendation with Unified Semantic-Collaborative IDs
- **Authors**: Yang Hu, Jiayi Guo, Jingui Ma, Ning Li, Jiangling Qin, Yanming Li, Yang Deng, Xiaoshuang Chen, Kaiqiao Zhan
- **Affiliation**: Kuaishou
- **arXiv**: [2608.17613](https://arxiv.org/abs/2608.17613) — cs.IR, cs.SI
- **Key Innovation**: OGR framework generates ordered slates directly (end-to-end). TUSID adaptively fuses item-specific semantic and local collaborative information into hierarchical SIDs. List-wise preference planning + pipelined position-wise SID decoding. SPA (reward-guided conservative policy optimization) aligns generated slates with user preferences. +1.120% Effective Views in online A/B on Kuaishou.
- **Abstract**: Slate recommendation requires joint optimization of item interactions and slate utility. OGR first introduces TUSID, then uses list-wise preference planning and pipelined position-wise SID decoding. 48.2% and 27.2% relative NDCG@5 gains on industrial and public datasets respectively.

### 1.3 Empowering Compact LLMs with Fusion of Layer-wise Exits for Recommendation (FLEXRec)
- **Authors**: Xurong Liang, Tong Chen, Quoc Viet Hung Nguyen, Jianxin Li, Xiangliang Zhang, Hongzhi Yin
- **Affiliation**: ICDM 2026
- **arXiv**: [2608.17316](https://arxiv.org/abs/2608.17316) — cs.IR
- **Key Innovation**: Discriminative framework enhancing compact LLMs for recommendation. Inserts prediction heads at multiple transformer layers, adaptively fuses score distributions. Adaptive continuous router (AC-Router) dynamically selects number and identity of exits per user sequence. Target-k hinge loss regulates routing sparsity. State-of-the-art on compact-backbone methods with Qwen 3 1.7B and Llama 3.2 3B.
- **Abstract**: LLM-RSs are computationally unsustainable. FLEXRec enables efficient full-corpus ranking through embedding similarity while enhancing compact LLMs with multi-layer exits and adaptive routing.

### 1.4 Decoupled Temporal Encoding for Generative Recommendation (DTE)
- **Authors**: Pengfei Jia, Jingjian Wang, Jingmao Li, Ge Zhang, Feng Shi
- **Affiliation**: CIKM 2026
- **arXiv**: [2608.16274](https://arxiv.org/abs/2608.16274) — cs.IR, cs.AI
- **Key Innovation**: Separates temporal dynamics from order information in generative recommendation. Macro-temporal module injects temporal primitives into embeddings; time-gated micro-sequential module introduces relative-order bias only when interactions are temporally dense. Parameter-efficient and deployment-friendly.
- **Abstract**: Addresses multi-level temporal regularities in recommendation sequences (recency, meal-time peaks, weekday/weekend, promotions). Existing methods inject heterogeneous signals through a unified representation. DTE is a lightweight framework that decouples these signals.

### 1.5 TRACER: Balancing Stability-Plasticity-Cognitivity Trilemma for LLM Enhanced Continual Recommendation
- **Authors**: WooJoo Kim, HyunSik Yoo, JunYoung Kim, JaeHyung Lim, SeongKu Kang, HwanJo Yu
- **Affiliation**: CIKM 2026
- **arXiv**: [2608.16075](https://arxiv.org/abs/2608.16075) — cs.IR
- **Key Innovation**: Identifies the Stability-Plasticity-Cognitivity (SPC) Trilemma in LLM-enhanced continual recommendation. Three specialized modules each target one lemma, preventing any from dominating. Semantic knowledge supports history retention and adaptation without disrupting continual learning. +14.38% over SOTA.
- **Abstract**: Continual recommendation struggles with sparsity. LLM enhancers mitigate this but naive integration creates conflict between generalized LLM semantic priors (Cognitivity), personalized historical preferences (Stability), and adapting to interest shifts (Plasticity).

### 1.6 GOD: Enhancing Generalization via Deep Grafting for Sequential Recommendation
- **Authors**: WooJoo Kim, JunYoung Kim, JaeHyung Lim, HwanJo Yu
- **Affiliation**: CIKM 2026
- **arXiv**: [2608.16073](https://arxiv.org/abs/2608.16073) — cs.IR, cs.LG
- **Key Innovation**: Graft-Oriented Distillation — replaces selected frozen-teacher components with trainable student counterparts to build hybrid source models. Component-level feedback for embeddings and encoders separately. No additional inference cost. +13.92% over SOTA.
- **Abstract**: Sequential recommenders struggle with sparse/noisy histories. GOD uses grafting to evaluate student components in teacher context, providing component-level distillation rather than output/representation matching.

### 1.7 Decomposing Staleness in Recommender Systems (SDF)
- **Authors**: Di Bai, Feng Han, Zhenwei Tang, Jintao Liu, Luoshu Wang, Jialu Liu
- **Affiliation**: Google Discover — CIKM 2026 Applied Research Track
- **arXiv**: [2608.15780](https://arxiv.org/abs/2608.15780) — cs.IR, cs.AI
- **Key Innovation**: Deployed at Google Discover (hundreds of millions DAU). Two complementary filters: relational staleness model (detects supersession between item pairs) and predicted traffic ratio (PTR) model (forecasts relevance decay). User-filed staleness reports declined **54.9%** over two-year production deployment.
- **Abstract**: Items lose relevance through supersession (emerging updates render prior coverage stale) and relevance decay (informational value diminishes). SDF prunes stale candidates upstream of ranking, reducing serving costs while improving engagement.

### 1.8 POI Recommendation with LLM-Augmented Multi-Graph Learning (LLM-MGCL)
- **Authors**: Burak Tamer, Wolfram Höpken, Zehui Wang
- **arXiv**: [2608.16407](https://arxiv.org/abs/2608.16407) — cs.IR, cs.LG
- **Key Innovation**: Multi-graph neural network using LLM-generated semantic graphs + geographic graphs as auxiliary signals on top of LightGCN. Bidirectional InfoNCE contrastive alignment connects behavioral, semantic, and spatial representations. +52.0% Recall@20, +64.8% NDCG@20 over LightGCN.
- **Abstract**: GNN-based POI models struggle with cold-start. LLM-MGCL constructs semantic graphs from LLM-generated photo summaries and geographic graphs from Haversine distances, fusing them additively with the collaborative graph.

### 1.9 SAGA: Structure-Attended Generative Action Embedding Model
- **Authors**: Tsz Fung Pang, Po Jen Chen, Nimish Ronghe, Farhad Farahani, Bo Zhang
- **arXiv**: [2608.15429](https://arxiv.org/abs/2608.15429) — cs.LG, cs.IR
- **Key Innovation**: Encodes multi-surface user interaction sequences (checkout, P2P, in-app, email, account actions) into unified user representations. Per-field tokenization decomposes each action event into field-level tokens enabling field-level attention and per-field training objectives. Deployed across a Financial Service organization's ecosystems.
- **Abstract**: Prior embedding models operate in homogeneous action space. SAGA spans distinct behavioral domains within a single generative model with per-field tokenization.

### 1.10 SAHC-NS: Structure-Aware and Hardness-Calibrated Negative Sampling
- **Authors**: Jiayi Wu, Zhengyu Wu, Xunkai Li, Hongchao Qin, Rong-Hua Li, Guoren Wang
- **arXiv**: [2608.16587](https://arxiv.org/abs/2608.16587) — cs.IR
- **Key Innovation**: Uses mean and std of layer-wise matching scores to capture cross-layer structural discrepancy. Candidate-pool-aware hardness calibration dynamically adjusts negative augmentation strength based on pool conditions.
- **Abstract**: Negative sampling in implicit CF overlooks hardness variation across users. SAHC-NS evaluates candidates through multi-hop neighborhood aggregation rather than final matching scores alone.

### 1.11 Ask to Be Sure: Informative Interactions for Confident Multi-Turn LLM Recommendation
- **Authors**: Cedar Site Bai, Duanshun Li, Zhenyu Liao, Sheikh Sarwar, Huiyuan Chen, Yuan Chen, Changhe Yuan, Haiyang Zhang, Qilin Qi
- **Affiliation**: CIKM 2026
- **arXiv**: [2608.15949](https://arxiv.org/abs/2608.15949) — cs.IR, cs.AI, cs.CL, cs.LG
- **Key Innovation**: Quantifies interaction effectiveness by entropy reduction over recommendations. Entropy reduction reward (no ground-truth needed) fine-tunes LLM for strategic interaction generation. Tested with SFT and DPO on INSPIRED and ReDial datasets.
- **Abstract**: Existing CRS approaches don't measure useful information gain. This work uses uncertainty reduction as reward for multi-turn LLM recommendation.

### 1.12 Unbiased Recommender Systems with Implicit Feedback
- **Authors**: Md Aminul Islam
- **Affiliation**: RecSys 2026
- **arXiv**: [2608.16704](https://arxiv.org/abs/2608.16704) — cs.IR
- **Key Innovation**: Comprehensive framework for mitigating position bias and popularity bias across LTR, CF, and social GNN-based recommender systems. Develops methods overcoming limitations of existing debiasing approaches.
- **Abstract**: Implicit feedback is prone to position bias (higher-ranked items get more interactions regardless of relevance) and popularity bias (popular items over-recommended). Addresses both across multiple recommendation paradigms.

### 1.13 Impression Share Prediction: An Offline Evaluation Task for Ranking Systems
- **Authors**: Mohsen Malmir, Houssam Nassif, Danish Nasir Shaikh, Taher Rahgooy, Murat Ali Bayir
- **arXiv**: [2608.16872](https://arxiv.org/abs/2608.16872) — cs.IR
- **Key Innovation**: Proposes impression share prediction as offline evaluation task — predict distribution of impressions across objective buckets (click, video view) for a candidate ranking model. Structural causal model for counterfactual identification. Random Forest reduces L1 error by 49%.
- **Abstract**: Standard offline metrics are only surrogate for downstream utility. No offline method surfaces impression share shifts before online evaluation. Counterfactual task with causal identification.

---

## 2. LLM Agents & Reinforcement Learning

### 2.1 PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs
- **Authors**: Dayang Liang, Liyuan He, Xuan Feng, Shuxin Li, Bo An, Yunlong Liu
- **arXiv**: [2608.17289](https://arxiv.org/abs/2608.17289) — cs.AI
- **Key Innovation**: Coarse-to-fine advantage signals capturing trajectory-level and turn-level response length differences. Enables agents to learn deliberate planning behaviors from high-quality rollouts without degenerating into length minimization. +27.2% over GRPO on ALFWorld, WebShop, SciWorld.
- **Abstract**: Most GRPO variants assign identical reward to successful trajectories that differ substantially in interaction efficiency, causing advantage collapse.

### 2.2 LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents
- **Authors**: Yiming Du, Yuxin Jiang, Tao Yuan, Jianbo Dai, Shaowei Wang, Jierun Chen, Chaofan Tao, Xianzhi Yu, Lifeng Shang, Kam-Fai Wong, Xiaohui Li, Haoli Bai
- **arXiv**: [2608.17393](https://arxiv.org/abs/2608.17393) — cs.AI
- **Key Innovation**: Bridges native coding-agent harnesses with policy-gradient optimization. In-process LLM proxying for token-level alignment + robust trainer-side log-prob recomputation. Scalable sandbox with image caching and stage-wise defenses. Improves Qwen3.5-35B-A3B from 64.0% → 70.4% on SWE-bench Verified (OpenHands SDK).
- **Abstract**: RL for coding agents relies on long-running harnesses that are misaligned with policy-gradient training. LEGO-RL uses in-process LLM proxying and sandbox orchestration without modifying harness internals.

### 2.3 Agent Lightning v1.0: Towards Harnessed Agentic RL
- **Authors**: Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo
- **arXiv**: [2608.17528](https://arxiv.org/abs/2608.17528) — cs.AI, cs.SE
- **Key Innovation**: ~3,500 lines of code framework for harnessed agentic RL. Addresses retokenization, sample merging, advantage calculation, loss normalization, and backend scheduling. RL improves Qwen3.5-9B on SWE-bench Verified from 41.8% → 56.4% (+14.6 points) with only 6K training examples.
- **Abstract**: Harnessed agentic RL differs from traditional agentic RL — the harness owns environment interaction while trainer observes only LLM request-response pairs. Agent Lightning provides a lightweight practical testbed.

### 2.4 Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements
- **Authors**: Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee
- **arXiv**: [2608.17310](https://arxiv.org/abs/2608.17310) — cs.LG
- **Key Innovation**: Evolution strategies instead of RL for long-horizon LLM agents. Full-parameter optimization with minimal inference-level GPU memory. Trajectory-level parameter attribution without decomposing rewards. Online prompt–parameter co-evolution. +6.69% on WebArena-Lite for Qwen-3.5-27B.
- **Abstract**: RL's heavyweight backpropagation stack makes it impractical for large LLMs. ES offers model scalability (minimal GPU), flexibility (black-box feedback), and long-horizon scalability (no reward decomposition).

### 2.5 Towards Better Agents for Multi-Turn User Interaction (FACA)
- **Authors**: Yiwen Zhao, Zhihao Wen, Yuchen Mao, Mingxuan Jiang, Yihao Hu, Pan Wang, Xin Zhang, Wei Wu
- **arXiv**: [2608.17499](https://arxiv.org/abs/2608.17499) — cs.AI
- **Key Innovation**: Feedback-Aware Credit Assignment — uses next user turn as noisy, temporally local evidence about preceding segment. Locally normalized reaction advantage added to verified terminal outcome advantage. No extra critic or rollout needed. +5.91 pp at 8B, +10.22 pp at 14B on nine-domain τ-family.
- **Abstract**: Interactive RL reduces each rollout to terminal reward, assigning same credit to effective elicitation, errors, and repair. Next user turn provides actionable local credit.

### 2.6 GUPO: Gradient Uncertainty-aware Policy Optimization
- **Authors**: Peizheng Guo, Jianqi Zhang, Xingyu Zhang, Yun Fan, Jiahuan Zhou, Changwen Zheng, Wenwen Qiang
- **arXiv**: [2608.17411](https://arxiv.org/abs/2608.17411) — cs.LG
- **Key Innovation**: Models group gradients as random variables under Bayesian formulation. Dirichlet-based gradient uncertainty calibration of contribution during aggregation. Addresses gradient conflicts in GRPO that cause less effective policy updates.
- **Abstract**: GRPO directly averages group gradients from different queries, but these can point in conflicting directions. GUPO estimates gradient uncertainty to calibrate aggregation.

### 2.7 Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation
- **Authors**: Zhizhao Liu, Zhiliang Tian, Xi Wang, Zhihua Wen, Yihang Xiong, Zhiquan Lai, Dongsheng Li
- **arXiv**: [2608.17941](https://arxiv.org/abs/2608.17941) — cs.LG, cs.AI, cs.CL
- **Key Innovation**: Graph-based difficulty-aware sample graph using semantic/reasoning similarities. Latent difficulty states with Potts prior for neighboring sample sharing. Beta-Binomial model + online mean-field variational algorithm. Plug-and-play framework for sample-selection and rollout-allocation schedulers.
- **Abstract**: RLVR assigns same exploration budget to all samples regardless of difficulty. Easy samples get redundant rollouts while difficult but learnable ones get too little exploration.

---

## 3. LLM Reasoning, Agents & Self-Improvement

### 3.1 On the Fragility of Self-Improving Agents
- **Authors**: Qinyuan Ye, Yu Li, Yada Pruksachatkun, Jiaxin Zhang, Chien-Sheng Wu
- **arXiv**: [2608.18066](https://arxiv.org/abs/2608.18066) — cs.AI, cs.CL, cs.LG
- **Key Innovation**: Comprehensive re-evaluation of memory-based self-improving agents. Two key findings: (1) stacking self-improving loop amplifies noise, (2) improvement is highly dependent on task order — default orderings impose implicit curriculum. Hypothesizes underspecification as root cause; validates with detailed rubrics and environment feedback.
- **Abstract**: Memory-based self-improving agents learn from online task streams. Evaluation across multiple runs and random task shuffling reveals fragility — agents show high variance and task-order dependence.

### 3.2 LLM-Derived Preference Judgments Are Not Self-Consistent
- **Authors**: Matthew T. Ford, Francis Bahk, Jingjing Wang, Adam S. Jovine, Tinghan Ye, David B. Shmoys, Peter I. Frazier
- **arXiv**: [2608.17644](https://arxiv.org/abs/2608.17644) — cs.AI, cs.CL
- **Key Innovation**: Statistical tests measuring self-consistency of cardinal LLM preference judgments. Experiments across 6 LLMs with flight, apartment, and hotel examples reveal large persistent inconsistencies. LLM-derived preference judgments cannot be faithfully summarized by a single utility function.
- **Abstract**: Agents increasingly use LLMs for numerical preference judgments (e.g., willingness-to-pay). The pipeline assumes approximate self-consistency, but experiments show large departures.

### 3.3 Chain-of-Experience for Continual LLM Improvement
- **Authors**: Haoqin Tu, Yunhao Fang, Yizhong Wang, Cihang Xie, Shen Yan
- **arXiv**: [2608.18027](https://arxiv.org/abs/2608.18027) — cs.CL
- **Key Innovation**: Chain-of-Experience (CoE) — models accumulate experiential traces through iterative interactions with self or environmental feedback. 5.6% overall improvement and 19% lower API cost. Combining complementary feedback channels yields additional gains. Models remain robust under weak/spurious feedback. Evaluated with GPT-5, Gemini-2.5 Pro, Claude-4.5 Sonnet.
- **Abstract**: Studies how LLMs learn from iterative experience at test time. Consistently outperforms feedback-free baselines across math, coding, and knowledge domains using 8 LLMs.

### 3.4 Beyond the Trace: Coupling an Interpretable Reasoning-State Readout to Native MoE Routing
- **Authors**: Kang Chen, Sihan Zhao, Yixin Cao, Yugang Jiang
- **arXiv**: [2608.17638](https://arxiv.org/abs/2608.17638) — cs.AI
- **Key Innovation**: J64 — 64-axis semantic frame distilled from model's own reasoning states, revealing process state not shown in emitted trace. R64 — routing-only proxy reconstructed from native expert-routing statistics (0.69–0.86 correlation with J64). Supports test-time decisions: improved single-branch selection, voting, and stop-and-resample policy.
- **Abstract**: What a reasoning model writes is only a partial record. J64 separates inference effort from problem-induced strain, adding 0.096–0.135 held-out AUC over baseline.

### 3.5 When AI Designs AI: Innovation or Imitation?
- **Authors**: Yikang Yang, Zhengxin Yang, Luzhou Peng, Minghao Luo, Yanqi Kan, Wanling Gao, Jianfeng Zhan
- **arXiv**: [2608.17471](https://arxiv.org/abs/2608.17471) — cs.AI, cs.LG
- **Key Innovation**: Derives task-specific algorithmic design spaces from human methods, maps both human- and agent-designed methods. Agents match/surpass human SOTA in 10/72 configurations, but 96.8% of agent-designed methods fall within human design spaces — nearly half exactly match existing human algorithms.
- **Abstract**: LLM agents designing AI methods show occasional performance parity but their designs largely recombine existing human algorithmic choices rather than innovating beyond them.

### 3.6 Policy-Invariant Reward Shaping from LLM Feedback
- **Authors**: Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba
- **arXiv**: [2608.18008](https://arxiv.org/abs/2608.18008) — cs.LG, cs.AI
- **Key Innovation**: Formalizes hybrid LLM-planner + RL-controller architecture as Goal-Augmented MDP. Shows that LLM per-state progress score as bounded potential preserves optimal policy set even when LLM scores are inaccurate. Verified numerically including adversarial configurations scaled 20x base reward.
- **Abstract**: Combining LLMs with RL — theoretical status of LLM-derived reward signals often left implicit. Provides formal policy-invariance guarantee.

---

## 4. LLM Memory & Agent Systems

### 4.1 ArborMem: Navigating Interaction States with Memory Forests
- **Authors**: Zongwei Lv, Yuemeng Xu, Yilun Yao, Siyi Ding, Xinyu Tan, Yaoming Li, Guangxiang Zhao, Weihong Lin, Lin Sun, Xiangzheng Zhang, Tong Yang
- **arXiv**: [2608.17534](https://arxiv.org/abs/2608.17534) — cs.CL
- **Key Innovation**: Represents long-running conversations as navigable forest of interaction states. Each branch preserves locally coherent trajectory; forest maintains multiple resumable trajectories. Localizes relevant state, restores branch-local context, augments with cross-branch evidence. +3.36–10.31 pp over baselines. Introduced BranchMemEval benchmark.
- **Abstract**: Existing memory methods don't determine which prior interaction state the current turn resumes. Important when conversations interleave multiple tasks, people, and plans.

### 4.2 Write, Execute, Refine (WER): From Skill Followers to Skill Optimizers
- **Authors**: Kang Peng, Zhiwei Zhang, Yichen Zhang, Zezhong Wang, Yiming Du, Geng Tu, Baojun Wang, Bin Liang, Ruifeng Xu, Kam-Fai Wong
- **arXiv**: [2608.17587](https://arxiv.org/abs/2608.17587) — cs.CL
- **Key Innovation**: Multi-phase framework training Skill Optimizer outside frozen executor. Optimizer proposes skills, frozen agent executes, programmatic verifier scores. Matched successful/failed trajectories form refinement states. Trained 4B optimizer reaches 76.63% on BFCL v4, outperforming all evaluated general-purpose models.
- **Abstract**: Agent-authored skills perform 8-11 points worse than no skill. WER bridges this gap through iterative optimization from execution feedback.

### 4.3 Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals (InnerExpert)
- **Authors**: Joao Fonseca, Rodrigo Rodrigues, Paolo Romano
- **arXiv**: [2608.17687](https://arxiv.org/abs/2608.17687) — cs.AI, cs.LG
- **Key Innovation**: First method leveraging MoE-specific signals (router entropy, expert disagreement, expert usage patterns) for per-token hallucination detection. Lightweight detector on compact per-token feature vectors. Up to 0.91 answer-level and 0.76 token-level AUROC. Single forward pass.
- **Abstract**: Most hallucination detection operates at answer/sentence level. InnerExpert exploits MoE-internal signals unavailable in dense architectures for fine-grained per-token detection.

---

## 5. LLM Inference & Efficiency

### 5.1 TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration
- **Authors**: Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, Yunhe Feng
- **arXiv**: [2608.17336](https://arxiv.org/abs/2608.17336) — cs.AI
- **Key Innovation**: Precision routing as executable spatial decision over score-tile groups within fused dense attention. Partitions attention matrix into hardware-aligned score tiles, packs routing decisions into compact bitmasks. FP16 or INT8 per tile group with shared online-softmax state. No training required. Controllable accuracy-efficiency frontier.
- **Abstract**: Long-context prefill in LLMs incurs quadratic computation. TileMix routes precision at tile-group level while preserving dense token connectivity.

### 5.2 MoNe: Modular Neural Memory for Efficient Long Context Inference
- **Authors**: Wonguk Cho, Kyubyung Chae, Tribhuvanesh Orekondy, Sunghyun Park, Hyoungwoo Park, Jeongho Kim, Arash Behboodi, Kyuwoong Hwang, Sungrack Yun
- **arXiv**: [2608.17616](https://arxiv.org/abs/2608.17616) — cs.AI, cs.CL, cs.LG
- **Key Innovation**: Lightweight modular neural memory attaching to frozen Transformers. Two-phase: test-time learning (fast-weight neural memory with layer-localized gradients) → inference (generates keys/values from query tokens alone). O(N) preprocessing, O(1) query cost. At 128K tokens: ~80% reduction in compute and GPU memory vs ICL. Only 6.4% parameter overhead.
- **Abstract**: Decouples inference cost from context length. Memory generates K/V from queries alone — no context tokens re-read. Strong performance on RULER benchmarks.

### 5.3 When to Review: Spaced Repetition for Continual Pre-Training of Language Models (SRT)
- **Authors**: Alankar Atreya, Devesh Batra, Yoages Kumar Mantri, Geremy Bantug, Greig A Cowan, Raad Khraishi
- **arXiv**: [2608.17530](https://arxiv.org/abs/2608.17530) — cs.AI, cs.LG
- **Key Innovation**: Spaced Repetition Training — schedules sample-rehearsal using SuperMemo-2 algorithm from cognitive science. Maintains per-example review state, maps perplexity to recall-quality signal. Recovers 5–37 pp of old-knowledge accuracy while preserving new-knowledge acquisition. Extends beyond language to vision and tabular data.
- **Abstract**: Continual pre-training must acquire new information without erasing old knowledge. SRT decides not only how much history to replay, but which examples should return at each step.

---

## 6. Games & Procedural Content Generation

### 6.1 Procedural Content Metageneration via Program Search and Continual Abstraction Discovery (CAD)
- **Authors**: Matthew Siper, Ahmed Khalifa, Julian Togelius
- **Affiliation**: Accepted at IEEE Conference on Games 2026
- **arXiv**: [2608.17947](https://arxiv.org/abs/2608.17947) — cs.AI, cs.LG, cs.NE
- **Key Innovation**: Evolves complete Python generators (not individual levels) through LLM mutation and crossover. Continual Abstraction Discovery (CAD) extracts reusable primitives from high-fitness programs into run-specific helper modules. 2×2 experiment across Sokoban, Zelda, Dangerous Dave, Lode Runner. CAD raises mean fitness in all 8 domain×API comparisons. Learned libraries adopted by most later programs.
- **Abstract**: LLMs can generate executable programs, enabling search over procedural content generators rather than individual levels. CAD discovers reusable primitives that improve evolutionary program search.

### 6.2 The Concentration Game: Bayesian Updating, Regret, and Information
- **Authors**: Akshay Balsubramani
- **arXiv**: [2608.18061](https://arxiv.org/abs/2608.18061) — cs.LG, cs.GT, math.PR, math.ST
- **Key Innovation**: Theoretical analysis of a Bayesian updating / regret / information game. Bridges game theory with machine learning through information-theoretic analysis.
- **Abstract**: Studies a concentration game through the lens of Bayesian updating, regret bounds, and information measures at the intersection of GT, LG, probability, and statistics.

### 6.3 Policy Optimization and Statistical Inference for Online Contextual Matrix Games
- **Authors**: Liner Xiang, Yixin Wang, Hengrui Cai
- **arXiv**: [2608.17173](https://arxiv.org/abs/2608.17173) — stat.ML, cs.LG, math.ST, stat.ME
- **Key Innovation**: Framework for policy optimization and statistical inference in online contextual matrix games. Connects online learning, game theory, and statistical methodology.
- **Abstract**: Addresses online decision-making in adversarial settings where agents interact through matrix-valued payoff structures.

---

## 7. RAG & Retrieval

### 7.1 LineageRAG: Harnessing GraphRAG by Constructing Evidence Lineages with Source Grounding
- **Authors**: Linyao Zheng, Xuhang Shi, Zhifang Mao, Sai Zhou, Shuaixian An, Xiuquan Hou, Jinze Li
- **arXiv**: [2608.16004](https://arxiv.org/abs/2608.16004) — cs.IR
- **Key Innovation**: Constructs evidence lineage per query-derived demand, completes with verbatim source span. Demand-conditioned retrieval over corpus graph + lineage completion using provenance. +3.51 R@5, +5.96 EM, +5.22 F1 over GraphRAG baselines on HotpotQA, 2WikiMultiHopQA, MuSiQue.
- **Abstract**: Existing GraphRAG leaves connection between evidence discovery and source grounding implicit. LineageRAG makes this explicit through demand-conditioned lineage construction.

### 7.2 Ask to Be Sure (see §1.9 above)
- Cross-listed as cs.IR, cs.AI, cs.CL, cs.LG — LLM conversational recommendation with entropy-based interaction effectiveness.

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| Recommendation Systems | 13 |
| LLM Agents & RL | 7 |
| LLM Reasoning & Self-Improvement | 6 |
| LLM Memory & Agent Systems | 3 |
| LLM Inference & Efficiency | 3 |
| Games & PCG | 3 |
| RAG & Retrieval | 2 |
| **Total** | **37** |

## Notable Trends

1. **Generative Recommendation Matures**: End-to-end generative models (OGR, DTE, Decoupled Temporal Encoding) move beyond sequential token prediction to slate-level generation with position-aware decoding and temporal decoupling.

2. **LLM as Recommender Backbone**: FLEXRec, TRACER, LLM-MGCL demonstrate that compact LLMs (1.7B–3B) can compete with larger models through architectural innovations like multi-layer exits and contrastive alignment.

3. **Agentic RL Goes Mainstream**: LEGO-RL, Agent Lightning, PlanPO, and Agentic ESOpt all address practical challenges of RL for LLM agents — harness alignment, credit assignment, GPU efficiency, and training stability.

4. **Production Validation**: SDF (Google Discover, 54.9% staleness reduction), UniDot (KDD Cup 2026 runner-up), OGR (Kuaishou A/B test), SAGA (financial services deployment) — multiple papers report real-world deployment results.

5. **Temporal Awareness**: DTE, SDF, and TRACER all address the critical challenge of temporal dynamics — recency, decay, supersession — in recommendation and continual learning.

6. **MoE Internal Signals**: Both InnerExpert (hallucination detection) and J64/R64 (reasoning state readout) exploit MoE-internal signals that are unavailable in dense architectures, suggesting a fertile research direction.
