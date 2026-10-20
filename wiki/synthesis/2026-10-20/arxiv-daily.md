---
title: arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-20)
type: synthesis
created: 2026-10-20
updated: 2026-10-20
sources: []
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, marl, llm-post-training]
---

# arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-20)

> Auto-generated from recent arXiv publications (submissions ~2026-10-06 to 2026-10-19)

## Summary

Today's selection clusters around: (1) **industrial sequence transduction for recommendation** — Meta's TransX dissects encoder/memory/fusion scaling with disaggregated serving, echoing the LLaTTE/ReST line; (2) **generative retrieval & semantic IDs** — WeGR (WeChat) combines a collaborative SID tokenizer with horizon-expanded RL (online +2.5% orders), while SAHL, HASTE, OneChord, and ReRankID probe supervision, distillation, and reasoning from SIDs alone; (3) **LLM/agent-driven advertising** — MAPS (Kuaishou) generates personalized ad scripts via a multi-agent RL loop, and AdCoEvo co-evolves multi-agent ad-delivery strategies; (4) **LLM post-training RL theory** — an anatomy of off-policy policy gradient unifying GRPO variants with offline-RL pessimism; (5) **games** — Player-1 learns game control from synthetic experience, plus new MARL/imperfect-information benchmarks (MARL-BGs, BluffJAX) and a strategist-executor architecture for MicroRTS.

---

## 1. TransX Technical Report: Scaling Sequence Transduction for Recommendation

- **arXiv**: [2610.20913](https://arxiv.org/abs/2610.20913)
- **Date**: 2026-10-14
- **Authors**: Da Xu, Liyan Fang, Divya Venugopalan, Sunny Hsu, Xukai Wang, Rishav Roy Chowdhury, Cindy Liang, Nishant Satya Lakshmikanth
- **Institution/Company**: Meta (inferred from authors and HSTU-style production baseline; not stated in abstract)

### Abstract

TransX is a sequence-transduction framework with co-designed infrastructure for scaling industrial recommendation under explicit control of model-compute allocation and execution amortization. It separates sequence encoding, behavior memory, and candidate-conditioned fusion into independently scalable components. Training amortizes causal trajectory computation across behavioral prefixes and fans memory states out to candidates; serving disaggregates bulk prefill, nearline refresh, and online prediction via compact behavior-memory KV. The authors observe anisotropic scaling returns: encoder scaling saturates beyond moderate depth at fixed memory resolution/fusion capacity; more supervision shifts the allocation frontier toward candidate-conditioned fusion; memory resolution needed for quality stays roughly stable as capacity grows. Production A/B: core TransX improves CTR +6.02% and conversion +4.45%; post-trained retrieval and preference-ranking variants add +2.96% CTR / +1.33% conversion. Training infrastructure boosts supervised-target throughput +84%; disaggregated serving cuts total serving cost ~80% vs colocated, enabling ~5× per-request FLOPs of an HSTU-style baseline at equal cost and ~4× request throughput per H200 at matched FLOPs.

### Key Innovations

- **Componentized transduction**: independently scalable encoder / behavior-memory / candidate-conditioned fusion, with prefix-amortized training and KV-based memory fan-out.
- **Anisotropic scaling analysis**: depth saturates at fixed memory resolution; supervision shifts compute toward fusion; memory resolution is capacity-invariant.
- **Disaggregated serving**: prefill / nearline refresh / online prediction split → ~80% serving-cost reduction; online serving cost need not scale with model capacity.
- **Shared behavioral interface**: same backbone post-trained for retrieval and preference ranking; generative recommendation explored offline.

---

## 2. WeGR: Unified Generative Retrieval for Industrial Search Systems in WeChat

- **arXiv**: [2610.16979](https://arxiv.org/abs/2610.16979)
- **Date**: 2026-10-12
- **Authors**: Jiajun Han, Guoxin Ma, Felix, Liangsheng Xu, Ruiqi Yu, Yingdi Guo, Zongbing Wang, Xinhua Ye, Chenyan Hua, Xin Xie, Pengcheng Yang, Haijun Wu
- **Institution/Company**: Tencent (WeChat E-commerce Search)

### Abstract

Generative retrieval (GR) unifies candidate generation autoregressively but is limited by two challenges: Semantic ID (SID) tokenizers struggle to incorporate collaborative signals while keeping codebook utilization effective, and RL methods suffer severe reward sparsity under exact SID matching. WeGR addresses both with (1) CoCo-VAE, a Collaborative and Collapse-free Tokenizer injecting query-to-item and item-to-item collaborative signals while mitigating codebook collapse via codebook refresh and complementary regularization, and (2) Dynamic Horizon Policy Optimization (DHPO), which progressively expands reward-evaluation and policy-optimization horizons, leveraging behavioral rewards at different SID-hierarchy levels without auxiliary reward models. A two-month online A/B test in WeChat E-commerce Search yields +2.539% orders, +1.508% CTR, +1.381% conversion rate, with −25.5% CPU and −26.1% GPU usage; deployed across multiple WeChat search scenarios serving billions of users.

### Key Innovations

- **CoCo-VAE tokenizer**: collaborative signals + anti-collapse codebook refresh for more informative, balanced SIDs.
- **DHPO**: expanding-horizon RL over the SID hierarchy mitigates exact-match reward sparsity without reward models.
- **Production proof point**: generative retrieval improves business metrics while *reducing* compute in WeChat search.

---

## 3. MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning

- **arXiv**: [2610.25748](https://arxiv.org/abs/2610.25748)
- **Date**: 2026-10-19
- **Authors**: Zhongyu Wang, Chen Zuo, Qingxuan Sun, Jiayang Qiao, Qiuhao Qian, Songyan Cui, Guocheng Chen
- **Institution/Company**: Kuaishou (inferred from online A/B in the Kuaishou advertising system)

### Abstract

Retrieval-based personalized video advertising matches pre-produced creatives to users in feature space, limiting personalization granularity and causing performance disparities across user groups. MAPS proposes a multi-agent personalized *script-driven* system: four collaborative agents form a closed loop of user-profile modeling, script generation, video synthesis, and feedback-driven iterative refinement. The Scripter Agent is trained with an RL framework using a multi-dimensional reward that steers scripts to align with both user content preferences and target product information. Online A/B experiments in a Kuaishou advertising scenario show +2.87% CTR, +2.74% CVR, and +9.85% ARPU over a generative baseline.

### Key Innovations

- **Generative creative paradigm**: personalization moves from selecting pre-produced ads to synthesizing scripts per user.
- **Closed-loop multi-agent pipeline**: profile → script → video → feedback refinement.
- **Multi-dimensional RL reward** for the scripter aligning user preference and product messaging; strong ARPU gains online.

---

## 4. AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System

- **arXiv**: [2610.19454](https://arxiv.org/abs/2610.19454)
- **Date**: 2026-10-14
- **Authors**: Tianzhu Hu, Hang Yu, Zeyuan Zhao, Zeyu Pan, Huan Luo, Chun Gan, Mingzhe Cao, Liubin Wang, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu
- **Institution/Company**: Chinese Academy of Sciences, Institute of Software (inferred from author group; not stated in abstract)

### Abstract

Existing advertising automation covers individual tasks (bidding, budget allocation) but relies on human operators for overall coordination, cannot convert individual experience into reusable operational capabilities, and struggles to update strategies as markets change. AdCoEvo is a co-evolving multi-agent advertising delivery system that connects delivery decisions across timescales and operational granularities via role specialization: diagnostic results guide account planning and strategy adjustment in the next period, and the system updates model parameters from actual delivery outcomes, improving through mutual feedback among planning, adjustment, and diagnosis. Experiments: vs a rule-based baseline, +14.02% advertiser value and −7.07% CPA; vs a fixed-parameter multi-agent system, +3.96% advertiser value and −1.24% CPA.

### Key Innovations

- **Co-evolution loop**: planning ↔ adjustment ↔ diagnosis agents update each other from delivery outcomes.
- **Cross-timescale role specialization** spanning operational granularities.
- **End-to-end ops automation** with measurable advertiser-value/CPA gains over rules and non-evolving multi-agent systems.

---

## 5. DuoLM: Fast and Effective Personalized Recommendation with Language Models

- **arXiv**: [2610.24481](https://arxiv.org/abs/2610.24481)
- **Date**: 2026-10-17
- **Authors**: Jiang Wu, Yutong Song, Hongbo Wang, Guanghe Cao, Jeff Liang
- **Institution/Company**: unspecified in abstract

### Abstract

LMs can personalize recommendations from item content, user history, and feedback, but scoring many candidates with full-text inputs is prohibitively expensive online. DuoLM splits the work: an encoder LLM learns compact item representations for offline reuse, while a personalized ranker LLM combines them with user history and feedback. Both are trained end-to-end with recommendation supervision and teacher distillation. The serving runtime uses virtual token IDs for embedding access, shared history computation, and CUDA Graph replay. Quality matches the expert teacher; on a single H100 the system serves ~26,400 candidate scores/second, ~60× the teacher served with vLLM and automatic prefix caching.

### Key Innovations

- **Two-LLM split**: offline encoder embeddings + online ranker LLM; end-to-end distillation from a heavy teacher.
- **Serving runtime engineering**: virtual token IDs, shared-prefix history compute, CUDA Graph replay → 60× teacher throughput.
- **Quality-at-speed parity**: teacher-level recommendation quality at production-viable latency.

---

## 6. Structure-Aligned History Learning with Subspace-Structured Semantic IDs for Generative Recommendation (SAHL)

- **arXiv**: [2610.25093](https://arxiv.org/abs/2610.25093)
- **Date**: 2026-10-18
- **Authors**: Kaiwen Wei, Kejun He, Jie Zhang, Xiaomian Kang, Yuming Yang, Aijia Zhou, Xie Zhou, Yining Wang, Nayu Liu, Li Jin, Zhenyang Li, Jiang Zhong, He Bai, Jingxuan Wei, Junnan Zhu
- **Institution/Company**: Chongqing University (inferred from code repo CQU-MM-Intelligent-Lab)

### Abstract

Generative recommendation builds SIDs and predicts the next ID, but conventional quantizers produce imbalanced code assignments and lack coherent intermediate units, limiting history reconstruction; meanwhile next-item prediction gives weak supervision for recovering persistent preferences spread over distant interactions. SAHL reconnects quantization and history modeling: Semantic Residual Balanced Quantization (SRBQ) forms a balanced token–subspace–item hierarchy, and the model reconstructs history at those same granularities. Predictive entropy prioritizes uncertain transitions; curriculum optimization shifts toward inference-aligned next-item prediction. On four Amazon categories, SAHL improves NDCG@10 by 18.6–30.0% over RPG and 2.7–6.0% over MHL.

### Key Innovations

- **SRBQ**: balanced token-subspace-item SID hierarchy as shared structure for quantization *and* history learning.
- **Multi-granularity history reconstruction** aligned with quantizer groups.
- **Entropy-prioritized, curriculum-trained** transition modeling; large NDCG@10 gains on Amazon.

---

## 7. HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation

- **arXiv**: [2610.17368](https://arxiv.org/abs/2610.17368)
- **Date**: 2026-10-12
- **Authors**: Tripti Shukla, Shwetha Somasundaram, Akshat Gupta, Rohit Garg, Paul Duff, Ian Anderson
- **Institution/Company**: unspecified in abstract

### Abstract

Standard causal cross-entropy on semantic IDs ignores SID hierarchy and needs substantial training, while tail items suffer poor representations from sparse supervision. HASTE adds hierarchical loss (supervision at each SID level) and attribute-specific losses that leverage the LM's semantic knowledge to preserve fine-grained item attributes. Hierarchical Loss converges ~2× faster than standard CE, and attribute losses improve long-tail recommendation. Evaluated on a fashion benchmark and multiple Amazon domains across frequency regimes.

### Key Innovations

- **Hierarchical SID loss**: level-wise supervision exploiting the SID tree → ~2× faster convergence.
- **Attribute-specific losses**: fine-grained attribute preservation for tail-item representations.
- **Dual benefit**: training efficiency plus long-tail quality.

---

## 8. OneChord: Distill What You Rank, Recommend in One Pass

- **arXiv**: [2610.25805](https://arxiv.org/abs/2610.25805)
- **Date**: 2026-10-19
- **Authors**: Zesheng Li, Chengchang Pan, Honggang Qi
- **Institution/Company**: unspecified in abstract

### Abstract

In SID recommendation, deployed systems fuse code probabilities with item similarities, so the served ranking depends on normalization and relative weights of the fusion. OneChord adopts a direct training principle — "distill what you rank" — using one learned catalog-normalized fusion for next-item supervision, refinement distillation, and inference. A shared parallel decoder produces joint SID evidence and item-matching scores; a frozen denoiser supplies legal partial SIDs during training, and the student matches direct and refined predictions on shared hard candidates to transfer refinement into one-pass inference. The paper characterizes fusion weights under candidate conditioning and gives sufficient conditions for preserving the refined predictor's full-catalog Top-K selection. Across six Amazon datasets: best Recall@5/NDCG@5 everywhere (+6.30%/+7.12% avg relative over the strongest baseline) with 1.04–1.18× generation speedup.

### Key Innovations

- **Single fusion object** shared across training, distillation, and serving (aligning training with the deployed ranking distribution).
- **Refinement distillation via partial SID states** from a frozen denoiser.
- **Theory**: conditions under which one-pass fusion preserves refined full-catalog Top-K.

---

## 9. Reasoning Reranking with Semantic IDs as the Sole Item Representation (ReRankID)

- **arXiv**: [2610.22797](https://arxiv.org/abs/2610.22797)
- **Date**: 2026-10-16
- **Authors**: Zhenwei Tang, Jintao Liu, Di Bai, Xidong Wu, Xinwu Cheng
- **Institution/Company**: unspecified in abstract

### Abstract

Reasoning rerankers typically read item metadata; ReRankID asks whether a model can rerank a slate given *only* SIDs (much shorter prompts; tokens carry interaction-learned behavioral signal). Controlled experiments show base models often copy the input order; readable metadata does not fix this. Comparing SFT, rejection-sampled self-training, on-policy distillation, and verifier-based RL, the strongest post-trained 8B model (graded ranking reward) matches text-reading LLMs with ~20× shorter prompts, ranks above random with no history, and keeps gains at long histories where text prompts exceed 50k tokens. A rationale audit finds better trade-off arguments but less faithful item descriptions — post-training elicits ranking ability without faithful item knowledge.

### Key Innovations

- **SID-only reasoning reranking testbed** isolating rendering, history length, and slate size.
- **Post-training comparison**: graded-reward RL best; SID-only ranking competitive with 20× longer text prompts.
- **Honest negative**: ranking improves without faithful item descriptions — calls for reasoning-focused post-training.

---

## 10. When Semantics Fall Short: Persona-Guided Cross-Domain Sequential Recommendation with LLMs (PerCDR)

- **arXiv**: [2610.25221](https://arxiv.org/abs/2610.25221)
- **Date**: 2026-10-18
- **Authors**: Jundong Chen, Honglei Zhang, Shuai An, Enneng Yang, Han Yu
- **Institution/Company**: unspecified in abstract

### Abstract

Cross-domain sequential recommendation (CDSR) uses LLMs to bridge domains via global item semantics, but suffers (I) semantic domain isolation and (II) semantic-behavior inconsistency — local semantic relations track behavioral transitions better than global ones. PerCDR shifts from global semantic bridging to persona-guided behavioral modeling: LLM-inferred personas globally guide transferable cross-domain behavioral patterns; local semantic relations enhance intra-domain modeling; domain preference adaptation refines recommendations. Experiments show superiority over prior CDSR methods.

### Key Innovations

- **Persona as the cross-domain transfer object** instead of raw global item semantics.
- **Local-vs-global semantic asymmetry** diagnosed and exploited.
- **Three-stage pipeline**: persona-guided transfer → local semantic enhancement → preference adaptation.

---

## 11. RecSoup: Efficient Model Merging Approach for Controllable Multi-Objective Recommendation

- **arXiv**: [2610.21220](https://arxiv.org/abs/2610.21220) (accepted at CIKM 2026)
- **Date**: 2026-10-15
- **Authors**: Zidong Jia, Guofu Xie, Xiao Zhang
- **Institution/Company**: unspecified in abstract

### Abstract

Controllable multi-objective recommendation (CMOR) adjusts trade-offs at inference without retraining. Existing output-level reranking or parameter-generation approaches limit feasible trade-offs or cost too much. RecSoup uses specialized model merging in two stages: pruning that jointly considers objective-specific importance and cross-objective relevance mitigates parameter interference; then adaptive merging via a learnable preference-to-coefficient mapping enables dynamic control without joint retraining or generative modules. Theoretically shown to navigate the full Pareto front without smoothness constraints, outperforming the parameter-generation paradigm; 165–228× faster inference-time control than parameter-generation approaches.

### Key Innovations

- **Prune-then-merge** pipeline for interference-free specialization reuse.
- **Preference-to-coefficient mapping** for inference-time controllability.
- **Pareto-complete control** with 165–228× latency advantage.

---

## 12. Player-1: Learning to Play from Synthetic Experience

- **arXiv**: [2610.20584](https://arxiv.org/abs/2610.20584)
- **Date**: 2026-10-14
- **Authors**: Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, Guangzhi Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan, Mike Zheng Shou, Hwee Tou Ng
- **Institution/Company**: National University of Singapore, Tencent Youtu Lab / Sea (inferred from author affiliations; not stated in abstract)

### Abstract

Game agents need scalable interactive training beyond demonstrations. Player-1 is a post-training framework learning game control from *synthetic experience*. The computer-use action space is extended with relative pointer motion, sustained inputs, and composite actions. SFT initializes from 6,044 curated gameplay trajectories with task instructions and visual reasoning; Player-1-Gym provides sixteen synthetic 2D/3D environments with programmatically verifiable rewards and randomized observations/dynamics for multi-environment PPO. Player-1-9B and Player-1-35B-A3B improve MineDojo-300 success over their SFT policies by +27.8 and +17.7 points; Player-1-9B reaches 38.33% vs 12.63% for the strongest evaluated baseline, with gains on ViZDoom-10 and GameWorld. Broader synthetic environment coverage improves transfer; composite-action use increases during RL.

### Key Innovations

- **Synthetic-experience RL** for game control beyond demonstration coverage.
- **Extended computer-use action space** (relative pointer, sustained/composite inputs).
- **Player-1-Gym**: 16 verifiable synthetic environments; large MineDojo gains that generalize beyond the RL suite.

---

## 13. Anatomy of Off-Policy Policy Gradient: Importance Sampling, KL Regularization, and Baselines

- **arXiv**: [2610.25725](https://arxiv.org/abs/2610.25725)
- **Date**: 2026-10-19
- **Authors**: Haoqun Cao, Yurun Yuan, Tengyang Xie
- **Institution/Company**: University of Illinois Urbana-Champaign (inferred from author Tengyang Xie; not stated in abstract)

### Abstract

Policy gradient is routinely deployed off-policy in LLM post-training despite assuming on-policy sampling. This work characterizes when off-policy deployment is justified. For a general class of off-policy policy-gradient updates, consistency (optimal policy remains a stationary point) requires either trajectory-level importance weighting (cursed by horizon) or KL regularization with a baseline equal to the optimal soft value, instantiated by the grouped mean. The KL route is identified with group-relative policy gradient (GRPG), equivalent to a trajectory-level Bellman-residual objective, with finite-sample regret bounds under all-policy coverage — a theoretical account of a GRPO variant. Baselines in the off-policy setting implement pessimism (asymmetric REINFORCE), connecting to game-theoretic offline RL with single-policy-coverage regret bounds.

### Key Innovations

- **Two-path consistency theory** for off-policy policy gradient (importance weighting vs KL+soft-value baseline).
- **GRPG ↔ Bellman-residual equivalence** giving theory for GRPO-style objectives.
- **Baselines as pessimism**: link between LLM post-training tricks and offline-RL coverage theory.

---

## 14. MARL-BattleGrounds: A JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL

- **arXiv**: [2610.14883](https://arxiv.org/abs/2610.14883)
- **Date**: 2026-10-10
- **Authors**: Ulixes Tariq Hawili, Subramanian Ramamoorthy, Yoann Altmann, Ignacio Carlucho
- **Institution/Company**: University of Edinburgh (inferred from author group; not stated in abstract)

### Abstract

MARL benchmarks are either simple/efficient (SMAX) or rich/costly (Dota 2); MARL-BGs fills the middle. Team Deathmatch mode: simultaneous turn-based 5v5 with five heterogeneous classes (distinct basic/passive/ultimate abilities). 52 hand-designed maps including a 12-map curriculum and held-out test maps. Evaluation via eight hard endgame generalization scenarios and a monthly round-robin tournament (equal-compute retraining, Elo leaderboard, public downloadable opponents). 11,192 metrics per game; LLM-agent API (Qwen3.5-9B evaluated); human play client; six deep MARL baselines. On one RTX 5090 with 1,024 parallel games: 50,000 5v5 steps/second.

### Key Innovations

- **Missing-middle MARL benchmark**: heterogeneous abilities, competitive 5v5, JAX-native speed (50k steps/s).
- **Tournament + endgame-scenario evaluation** with public opponent releases.
- **LLM-agent and human-in-the-loop interfaces** for mixed autonomy evaluation.

---

## 15. BluffJAX: Adversarial Imperfect Information Games in JAX

- **arXiv**: [2610.07686](https://arxiv.org/abs/2610.07686)
- **Date**: 2026-10-06
- **Authors**: Aryaman Reddi, Jan Peters, Carlo D'Eramo
- **Institution/Company**: TU Darmstadt (inferred from authors; not stated in abstract)

### Abstract

BluffJAX is an open-source suite of adversarial imperfect-information games in JAX, designed for high simulation throughput and GPU parallelization. Canonical benchmarks (Texas Hold'Em, Kuhn Poker) plus games underexplored in RL (Bluff, Stud Poker, Kemps). Throughput/memory benchmarks in single- and multi-GPU settings show scaling to hundreds of millions of samples per second. RL, tree-search, and game-solving baselines in JAX are provided for comparison.

### Key Innovations

- **GPU-native imperfect-information game suite** with novel-to-RL games.
- **Hundreds of millions of samples/second** scaling on GPU.
- **Ready baselines** for RL, tree search, and game solving in JAX.

---

## 16. Constrained Command-Conditioned RL with Bandit Strategy Selection in Real-Time Strategy Games

- **arXiv**: [2610.11663](https://arxiv.org/abs/2610.11663)
- **Date**: 2026-10-08
- **Authors**: Nick Leenders, Roy Lindelauf, Joost van Oijen, Boris Cule
- **Institution/Company**: VU Amsterdam (inferred from authors; not stated in abstract)

### Abstract

Deep RL RTS agents are brittle outside their training distribution. This work separates strategic command selection from unit control: a constrained command-conditioned PPO executor for MicroRTS follows discrete commands specifying economy, army composition, military posture, and worker policy over multiple steps; a Thompson-sampling bandit strategist selects command tuples from an estimated opponent strategy built from in-game observations (not opponent identity). Against the flat PPO baseline (same architecture, budget, curriculum, self-play league), the strategist-executor system wins significantly more often against three of four strongest opponents, including two strongest held-out ones (win rates 0.55→0.97 and 0.01→0.34).

### Key Innovations

- **Strategist–executor separation**: reusable command-conditioned executor + bandit meta-strategy.
- **Observation-based opponent-strategy estimation** instead of opponent identity.
- **Large held-out-opponent gains** in MicroRTS under matched training budgets.

---

## Also Notable

- **Learning to Play: Reinforcement Learning and Games** ([2610.17391](https://arxiv.org/abs/2610.17391), Aske Plaat, 2026-10-12) — comprehensive open book on RL for games (Backgammon → Chess/Go/Poker/StarCraft), Python/Gym/TensorFlow examples.
- **Tool Recommendation for Multi-Step Agents** ([2610.23707](https://arxiv.org/abs/2610.23707), 2026-10-16) — deployed gateway system giving agents access to ~8,200 tools (beyond any context window) via a fixed three-tool interface with per-service consent checks.
- **Candidate-dependent residual routing in sequential recommendation** ([2610.24200](https://arxiv.org/abs/2610.24200), 2026-10-16) — small residual routing module; candidate-conditioned weights trade NDCG@10 for recall on REES46.
- **LSNR: Learned Sparse News Recommendations** ([2610.23510](https://arxiv.org/abs/2610.23510), SIGIR-AP 2026) — per-article encoding + attentive user modeling to avoid concatenation bottlenecks in learned-sparse news rec.

---

## Cross-Paper Observations

1. **The LLM-style scaling program for rec has matured into infrastructure economics**: TransX shows serving cost need not track model capacity (disaggregation + memory KV); DuoLM shows 60× teacher throughput via runtime co-design; WeGR shows generative retrieval *reducing* CPU/GPU use while improving metrics. Latency/serving is now a first-class research object, not an afterthought.
2. **Semantic IDs are becoming the battleground for generative recommendation**: CoCo-VAE (collaborative SIDs), SRBQ (balanced subspace hierarchies), HASTE (hierarchical/attribute losses), OneChord (train-the-served-fusion), ReRankID (reason from SIDs alone) — the field is attacking tokenization, supervision, distillation, and post-training in parallel.
3. **Advertising is going agentic and generative**: from delivery-ops co-evolution (AdCoEvo) to creative synthesis (MAPS), multi-agent systems now cover both ends of the ad pipeline, with consistent online lifts (CTR/CVR/ARPU/CPA).
4. **RL-for-games research is investing in infrastructure and controllability**: JAX-native benchmarks (MARL-BGs, BluffJAX), synthetic-environment game agents (Player-1), and modular strategist-executor designs for out-of-distribution robustness.
5. **LLM post-training RL theory is converging on offline-RL concepts**: off-policy consistency, pessimism-via-baseline, and coverage-based regret bounds now explain GRPO-family practice.
