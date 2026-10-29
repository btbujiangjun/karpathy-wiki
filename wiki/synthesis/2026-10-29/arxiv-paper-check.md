---
title: "arXiv Paper Check — AI & CTR (October 29, 2026)"
type: synthesis
created: 2026-10-29
updated: 2026-10-29
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, retrieval, ranking, llm, agents, rl, harness, multimodal]
---

# arXiv Paper Check — AI & CTR (October 29, 2026)

*Report generated: 2026-10-29 | Window: 2026-10-28 arXiv announcement batch (latest RSS at query time)*

## Summary

- Swept the `cs.IR`, `cs.AI`, `cs.LG`, and `cs.CL` RSS feeds: 822 unique papers, 491 `new`/`cross` announcements, including 51 `cs.IR` items.
- The strongest CTR/ads cluster is about **representation and supervision granularity**: target-aware positional encoding, token-level multi-objective distillation, latent residual ranking, daily embedding drift, and Thompson-sampled creative pre-ranking.
- The strongest AI cluster is about **what scaling does not fix**: RLVR self-reinforcement collapse, the finite-data "structure gap", harness-induced policy failure, and information loss in agent tool pipelines.
- Industrial deployment evidence appears in PailitaoMMSearch2.0 (Taobao), KL-MOPD (e-commerce ads), Refiner (online A/B), and exploratory creative pre-ranking (Roblox production).
- All papers below were checked against the wiki and the concurrent 2026-10-26 sibling report; no duplicate coverage. Abstract-only screening; reported numbers are author-reported and not independently reproduced.

## CTR / Ranking / Ads

### 1) [Rethinking Positional Encoding and Interaction Granularity for CTR Prediction](https://arxiv.org/abs/2610.37140)
- **Authors:** Xinxun Zhang, Yuxiang Wang, Xiaokai Zhou, Jiayue Li, Yi Li, Yue Liu, Jun Zhang, Xiaoling Zhou, Tieyun Qian, Xiao Yan, Jiawei Jiang
- **Categories:** cs.IR
- **Announced:** 2026-10-28
- **Summary:** Re-examines two default choices in Transformer CTR models: positional encoding and token-level causal interaction. The authors observe that most positional encodings do not beat NoPE, while relaxing causal constraints inside target-relative temporal groups helps. **TRIP** combines factorized rank encoding, target-relative time encoding, and temporal group-causal interaction.
- **Key Contributions:**
  - Shows that absolute/index-based positional encodings are not automatically useful for CTR behavior sequences.
  - Factorizes ordinal rank and represents coarse-to-fine time distance to the target item.
  - Allows bidirectional interaction within temporal groups while preserving causal order across groups.
  - Reports up to **+4.45% relative AUC** over the strongest baseline on four public benchmarks.

### 2) [KL-MOPD: Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation](https://arxiv.org/abs/2610.36973)
- **Authors:** Weiqin Yang, Yandong Wang, Yuan Gao, Hao Deng, Jinxin Hu, Jing Cao, Jiawei Chen
- **Categories:** cs.IR
- **Announced:** 2026-10-28
- **Summary:** Applies multi-objective on-policy distillation to generative recommendation, where click and conversion teachers supervise each decoding token. Vanilla MOPD suffers from **token-level imbalance** and **cross-token inconsistency**: the harder teacher changes across tokens, so some objectives are under-supervised at some steps.
- **Key Contributions:**
  - Weights each teacher at each token by initial student-teacher KL divergence.
  - Proves the KL-weighted objective improves the additive joint recommendation objective under mild conditions.
  - Requires only one-time weight calibration; plug-and-play with negligible overhead.
  - Evaluated on three public benchmarks, a billion-scale industrial dataset, and online e-commerce ads A/B tests.

### 3) [PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search](https://arxiv.org/abs/2610.36958)
- **Authors:** Xiaohan Ye, Zihan Gong, Jingqian Zhao, Lianyu Du, Yunmeng Shu, Xu Chen, Zesheng Zhou, Renchun You, Bocheng Chen, Jinsong Lan, Haihong Tang, Bo Zheng
- **Categories:** cs.AI, cs.IR
- **Announced:** 2026-10-28
- **Summary:** A deployed Taobao Pailitao system that generates product Semantic IDs directly from an image plus free-form instruction. It unifies open-ended image-text queries, heterogeneous shopping intents, and multiple serving budgets in one generative retrieval model.
- **Key Contributions:**
  - **Data scaling:** composable workflows for cold-start synthesis, quality control, real-traffic refinement, and continuous production.
  - **Intent scaling:** continual pre-training, mixed-budget SFT, and RL with intent-balanced optimization plus Sample-Beam rollouts.
  - **Scenario scaling:** exposes quality-cost operating points across model capacity and reasoning budget.
  - Online A/B: **+17.90% item page views, +27.04% transactions, +8.94% GMV**.

### 4) [Latent Residual Reasoning for Ranking in Generative Recommendation](https://arxiv.org/abs/2610.36890)
- **Authors:** Haihan Shi, Ruidong Han, Wenjie Wang, Shangyu Chen, Sunhao Dai, Yongqi Li, Yangyang Li, Fei Jiang, Wei Lin, Fuli Feng, Xiangnan He
- **Categories:** cs.IR
- **Announced:** 2026-10-28
- **Summary:** Asks whether extra inference-time computation can improve generative ranking without moving reasoning into text space. **Refiner** performs latent residual reasoning for ID-based recommendation models: each step adds a cumulative correction to the ranking score.
- **Key Contributions:**
  - Residual reasoning mechanism that progressively refines candidate scores rather than re-predicting from scratch.
  - History queries condense user behavior into candidate-specific context.
  - Parameter-efficient LoRA adaptation for latent reasoning.
  - Improvements on two public benchmarks, an industrial offline dataset, and an online A/B test.

### 5) [Exploratory creative pre-ranking: Hierarchical empirical-Bayes Thompson sampling for real-time creative optimization](https://arxiv.org/abs/2610.36020)
- **Authors:** Jiale Han, Ajith Moparthi, Dan Xie, Xiaowu Dai
- **Categories:** cs.GT, cs.LG
- **Announced:** 2026-10-28
- **Summary:** Dynamic creative optimization picks which ad creative to render per request. With AI-generated creatives, feedback per creative is sparse and latency is tight. The paper adds calibrated uncertainty and exploration to creative pre-ranking, before the per-user ad ranker runs.
- **Key Contributions:**
  - Hierarchical empirical-Bayes model over audience segment, advertised item, campaign, and creative; cold creatives borrow from parent levels.
  - Closed-form borrowing strength from historical logs, one parameter per level, no tuning.
  - Segment-level scoring from per-attribute counters plus one Thompson draw per creative.
  - Roblox replay: **+8.14% predicted play-through rate** vs +2.80% for a random shortlist, **>40% fewer creatives forwarded**, **+0.2% serving time**; now in production.

### 6) [Cross-Day Compatibility of Daily Item Embeddings: An Empirical Study of Alignment, Scale Management, and CTR Adaptation](https://arxiv.org/abs/2610.36408)
- **Authors:** Yicheng Wang
- **Categories:** cs.IR
- **Announced:** 2026-10-28
- **Summary:** Studies a practical failure mode in multi-day CTR training: daily item co-occurrence embeddings are mixed across days even though the same item's direction and norm drift. Compares Word2Vec and an item-graph XSimGCL adaptation across 48 configurations.
- **Key Contributions:**
  - ID initialization and orthogonal alignment raise cross-day cosine by **51.2%** and **93.4%**, and GAUC by **2.2%** and **2.6%**.
  - Warm starts accumulate scale: +102.5% norm after eight days; daily global rescaling limits this to **8.2%** and gives the best observed **+4.0% GAUC**.
  - CTR-trained dimensionality-reducing encoders further adapt to residual drift.
  - Industrial empirical study; raw dataset sizes and exact values withheld, so treat as directional evidence rather than a reproducible benchmark.

## AI / Agents / Training

### 7) [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666)
- **Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang
- **Categories:** cs.AI, cs.CV, cs.RO
- **Announced:** 2026-10-28
- **Summary:** VLA models are limited by action-labeled robot data. ThinkWorld represents each action thought as a **Chain-of-Dynamics (CoD)**: a sequence of discrete motion tokens connecting the current world to a future state. It initializes CoD on action-labeled demonstrations, then rewards CoDs whose predicted future better matches the observed outcome, letting unlabeled human videos supervise the same reasoning space.
- **Key Contributions:**
  - Embodiment-agnostic action representation based on world dynamics rather than low-level actions.
  - Uses future-state prediction as verifiable reward for CoD reinforcement.
  - Enables human-to-robot transfer without action annotations on human videos.
  - Simulation and real-robot gains on unseen tasks and environments.

### 8) [Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives Policy Collapse in Unsupervised RLVR](https://arxiv.org/abs/2610.37553)
- **Authors:** Peize Ding
- **Categories:** cs.LG
- **Announced:** 2026-10-28
- **Summary:** Explains why label-free RLVR, which rewards a model for agreeing with its own majority vote, improves reasoning and then collapses. Collapse appears only with many training problems. The paper models this as a collective instability: per-problem sharpening slows as **1/N**, while a shared cross-problem perturbation grows independently of **N**.
- **Key Contributions:**
  - Derives a critical problem count **N_c ≈ ln(1/δ)/(λ²G)** and predicts a sharp transition.
  - Identifies a single critical amplification **λ²NG** across couplings, confidence profiles, and training variants.
  - Shows confident initial models can avoid collapse; batch-size dependence is logarithmic.
  - Small-Transformer experiments: removing the shared direction prevents collapse entirely, restoring it causes collapse.
  - Practical implication: label-free self-reinforcement needs diversity or explicit regularization against a shared mode.

### 9) [The Structure Gap: When More Data Cannot Replace Structured Reasoning](https://arxiv.org/abs/2610.37523)
- **Authors:** Kheer Sagar Patel, Mojtaba Soltanalian
- **Categories:** cs.AI, cs.LG
- **Announced:** 2026-10-28
- **Summary:** Formalizes when a structured solver beats a structure-agnostic learner at finite data. For **structure-encoded problems** whose map is determined by a solver, symmetry, graph, physical law, grammar, or optimization objective, the issue is not expressivity but finite-data identification, extrapolation, and certification.
- **Key Contributions:**
  - Defines the **structure gap** between a method given the governing structure and a learner given only examples.
  - Proves for a Gaussian inverse problem that the known-operator Wiener solver attains Bayes risk while a dense empirical learner has persistent excess risk.
  - Proves a cell-coverage lower bound and an unobserved-orbit non-identifiability result.
  - Controlled experiments in known-operator inversion, sparse recovery, and graph reachability with size extrapolation.
  - Careful claim: structure-agnostic learning may approach the solver asymptotically; the gap is finite-resource, not absolute.

### 10) [Bayes-Adaptive MDPs for Rollout Allocation to Enhance GRPO Training](https://arxiv.org/abs/2610.37429)
- **Authors:** Faeze Moradi Kalarde, Armin Toroghi, Nam Ho Koh, Doo Hwan Hwang, Seungjin Kim, Kee-Eung Kim, Scott Sanner
- **Categories:** cs.AI, cs.LG
- **Announced:** 2026-10-28
- **Summary:** GRPO gives every question the same rollout budget, which wastes compute on easy questions and starves hard ones of informative positive rewards. **AdaRoll-GRPO** treats rollout allocation as sequential decision-making and learns a difficulty-aware allocation policy with a Bayes-adaptive MDP.
- **Key Contributions:**
  - Matches standard GRPO's total rollout budget while reallocating it across questions.
  - Learns the allocation policy offline; no extra online optimization during training.
  - Consistent gains across reasoning datasets and model architectures.
  - Simple systems-level lever for GRPO efficiency.

### 11) [Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255)
- **Authors:** Jian Mu, Ruibo Shen, Yao Shu
- **Categories:** cs.CL, cs.LG
- **Announced:** 2026-10-28
- **Summary:** A trained agent carries the preferences of its harness: prompts, tools, observation layout, and control logic. Under KL-regularized control, the log odds of the optimal policy recover how strongly the harness favors each action. Deployed return decomposes into the harness **ceiling** minus the policy **mismatch**; training only changes mismatch, while changing the harness moves both.
- **Key Contributions:**
  - Formalizes harness change as a shift in both achievable ceiling and policy compatibility.
  - MiniWoB++: reversing observation-field order, which preserves every optimal decision, drops a trained model from **85.0% to 19.2%** success.
  - Harnesses rejected by fixed-model comparison can outperform the original after retraining; ceiling and mismatch predict the gain.
  - Terminal-Bench Lite coding harnesses: ceiling-minus-mismatch reproduces accuracy ranking; either term alone does not.
  - Strong argument for evaluating harnesses with retraining, not only with a frozen policy.

### 12) [WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training](https://arxiv.org/abs/2610.37161)
- **Authors:** Ziyang Zeng, Tingyang Chen, Jia Deng, Qiyao Wang, Shuo Tang, Yike Yang, Tao Ren, Wayne Xin Zhao, Feng Chang, Jujie He, Chuan Hao, Ran Tao, Bryan Dai
- **Categories:** cs.AI
- **Announced:** 2026-10-28
- **Summary:** Scaling supervised training for working agents needs diverse professional tasks with reliable expert demonstrations. WorkFactory turns professional intents into executable tasks using an **information support graph**, then uses probe executions to find and repair missing or inconsistent task information.
- **Key Contributions:**
  - **112,686 tasks across 612 occupations**, with teacher trajectories.
  - WorkPilot models at 4B, 27B, and 35B-A3B all beat their base models on four professional-work benchmarks.
  - WorkPilot-35B-A3B improves GDPval-AA v2.1 Elo from **879 to 1565**.
  - Planning and repair reduce diagnosed environment defects; execution length shows model-dependent diminishing returns.

### 13) [Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses](https://arxiv.org/abs/2610.36114)
- **Authors:** Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan
- **Categories:** cs.AI, cs.SE
- **Announced:** 2026-10-28
- **Summary:** Measures information loss before tool output reaches the model. In a Linux-kernel-trace debugging agent, the context window was almost empty, yet a third of tool results were silently truncated and turned into broken JSON by fixed-length slicing. Which field held the fault evidence depended on when the faulty process started.
- **Key Contributions:**
  - Models agent context as a five-stage pipeline with a measured failure at each stage.
  - Across 720 runs, the largest prompt used only **5.75%** of the context window, but **3,827 of 11,189** tool results were cut.
  - Controlled replay: truncation first causes extra work, with **43% more tool calls**, **2x computation**, and yield falling from **0.61 to 0.31**.
  - A survey of seven agent frameworks finds two that cut tool output the same unsafe way.
  - Honest caveat: whether truncation directly causes the accuracy drop remains open; the measured cost is extra work and lower yield.

### 14) [h1: A Taste of the Bitter Lesson in Automated Theorem Proving](https://arxiv.org/abs/2610.35962)
- **Authors:** Skander Moalla, Ahmad Rammal, Niket Patel, Remi Munos, Julia Kempe
- **Categories:** cs.LG, cs.LO
- **Announced:** 2026-10-28
- **Summary:** Asks whether a simple agentic loop with scaled test-time compute can match human-designed formal-proving workflows. **h1** gives a model an efficient Lean 4 interface and keeps it working through verifier feedback and self-reflection, without imposed decomposition or search structure.
- **Key Contributions:**
  - State-of-the-art on PutnamBench, FATE-X, and FormalConjectures100-Solved; settles **eight open problems** in FormalConjectures.
  - At matched models, matches or beats specialized workflows such as Goedel-Architect and AlphaProof Nexus.
  - Pass@1 can often scale to solve open problems; simplicity alone is not enough because the Lean interface dominates cost and solve rate.
  - Recommends evaluating frontier models with efficient execution feedback before prescribing workflow structure.

## Also Notable

- **[Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](https://arxiv.org/abs/2610.37657)** — per-head attention gates separate trusted instructions from untrusted data; RL-Hammer attack ASR drops to **10%** on GPT-OSS-20B vs 97% undefended, while preserving utility.
- **[When Retrieval Is Not Enough: Obsolete Facts in Agent Memory](https://arxiv.org/abs/2610.36308)** — retrieving the newest fact is insufficient: adding an obsolete competing statement drops Qwen2.5-7B accuracy from **100% to 44.6%**; more retrieved tokens can hurt (45% to 32%).
- **[PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix](https://arxiv.org/abs/2610.35987)** — 2,457 real bug fixes across 20 repos; frontier agents stay below **21% recall** and **9% precision**, yet 85% of their findings are judged valid, and their bug distribution differs from maintainers'.
- **[Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors](https://arxiv.org/abs/2610.36544)** — a fixed 90%-accurate monitor can swing from a 5-point loss to a 35-point gain depending on the replacement attempt; 0 of 103 live comparisons cleared the certification bar.
- **[AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems](https://arxiv.org/abs/2610.37228)** — agents improve 5 of 6 recommendation tasks by **16.1%** on average, but mostly via tuning, training strategy, and ensembling; genuine algorithmic innovation is rare.
- **[RELAY: One Query, Two Roles for Sequential Recommendation](https://arxiv.org/abs/2610.36000)** — one learned query serves semantic readout and behavioral-memory routing; **+14.22% Recall@5** and **+17.88% NDCG@5** average, 65.12% smaller predictor, 1.75-1.79x faster inference.
- **[LESSRec: Level-Specific History Modeling for Semantic ID-Based Recommendation](https://arxiv.org/abs/2610.37286)** — restricts historical attention to the target token's semantic level, plus an item-level semantic sequence; reduces cross-level interference.
- **[REGER: Modeling inter-item Relations with Semantic IDs for Generative Recommendation](https://arxiv.org/abs/2610.37584)** — injects inter-item relations through semantic-neighbor pretraining, local SID-boundary attention, and prefix-conditional preference distillation.

## Emerging Trends

- **CTR is rethinking its defaults.** NoPE matching learned positional encodings, target-relative time, group-causal interaction, and daily embedding drift all point to representation hygiene over bigger backbones.
- **Generative recommendation is moving from retrieval to supervision.** KL-MOPD and Refiner both add fine-grained, token- or score-level supervision at inference or distillation time.
- **Industrial evidence is unusually strong this batch.** Taobao, Roblox, and e-commerce ads deployments report online A/B results, not just offline gains.
- **RLVR stability is becoming a theory problem.** The self-reinforcement collapse result gives a concrete **N_c** and a shared-mode mechanism, not just an empirical warning.
- **Agent failures are often pipeline failures.** Harness layout, tool-output truncation, obsolete memory, and monitor decision value all matter more than nominal context-window size.
- **Scaling data still needs structure.** WorkFactory scales professional task data, while The Structure Gap explains why finite data cannot always replace a known solver.

## Notes

- Data source: arXiv RSS for `cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`; the export API was rate-limited (`HTTP 429`) during this run.
- Counts: 822 unique items, 491 `new`/`cross`, 51 `cs.IR`; `replace`/`replace-cross` items were not treated as new.
- Abstract-only screening. Numbers are author-reported and were not independently reproduced.
- No overlap with the concurrent `wiki/synthesis/2026-10-26/arxiv-ai-search.md` report; all featured IDs were checked as absent from the wiki before writing.
- "Announced" is the RSS announcement date, not necessarily the original submission date.
