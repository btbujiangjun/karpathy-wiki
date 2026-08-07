---
title: "arXiv Daily Digest — 2026-08-07"
type: synthesis
created: 2026-08-07
updated: 2026-08-07
tags: [arxiv, llm, recommendation, retrieval, reasoning, rl, agents, sequential-modeling, games, world-models, kv-cache, personalization, evaluation]
---

# arXiv Daily Digest — 2026-08-07

> Curated from the **Fri Aug 7, 2026** arXiv batch (new submissions announced on the Fri listing; submitted Aug 5–6, 2026). Stream sizes: cs.AI 201 new, cs.CL 94 new, cs.LG 162 new, cs.IR 15 new, stat.ML 22 new (per listing-page headers). **26 papers curated.** No overlap with the [Aug 6 digest](../2026-08-06/arxiv-daily.md), [Aug 6 paper check](../2026-08-06/arxiv-paper-check.md), or [Aug 5 digest](../2026-08-05/arxiv-daily.md). The signature theme of this batch is **verifiable/agentic RL supervision** (three independent on-policy self-distillation papers: DASH, AgentOPSD, plus the EnvACE world-rehearsal frame) — with strong secondary clusters on recommender audit methodology (modality-weighting audit, popularity-calibration user study), test-time compute for reasoning, dense-retrieval interpretability, KV-cache recoverable eviction, and game/world-model evaluation. Note: **no dedicated advertising/CTR paper** surfaced in the cs.IR stream today; the closest industrial work is the Yandex Music generate-and-rank cascade replacement (Gryphon-v2).

---

## 1. Recommendation, Ranking & Retrieval

### Gryphon-v2: One Model in Place of a Cascade — Generate-and-Rank Recommender with Rollout Distillation
- **Authors**: Anna Lipkina, Daria Tikhonovich, Viktor Yanush, Mariia Ulianova, Oleg Sorokin, Vladislav Dodonov, Ilya Murzin, Denis Burshtein, Nikolay Savushkin
- **Institution**: Yandex Music
- **Date**: 2026-08-05
- **Link**: [2608.06213](https://arxiv.org/abs/2608.06213)
- **Abstract**: Industrial recommender systems are typically deployed as multi-stage cascades with separate candidate generators, pre-rankers, and final rankers — effective, but requiring repeated user-history processing, complex feature pipelines, and multiple serving stages. Semantic-ID-based generative retrieval promises simpler end-to-end systems, yet next-item prediction alone does not capture the fine-grained preferences encoded by production ranking objectives. Gryphon-v2 is a unified generate-and-rank architecture: it encodes the user history once, generates Semantic-ID candidates with an autoregressive decoder, resolves them to catalogue items, and ranks them with an item-level Ranking Module that reuses the shared encoder states. To transfer fine-grained production ranking preferences without adding a second serving model, a high-capacity training-only Teacher Ranker is distilled into the Ranking Module. Training uses Rollout Distillation: teacher scores are the only ranking supervision, collected over two complementary candidate distributions — decoder rollouts (exposing the module to the same generation mechanism used at serving) and logged impressions (items users were actually shown). In an online A/B at Yandex Music, a single Gryphon-v2 model replaced a production cascade of **more than 15 candidate generators plus pre-ranking and final ranking**, increasing active users by **+1.41%** at serving latency comparable to the cascade.
- **Key Innovation**: A single generate-and-rank model replacing an entire production cascade, with ranking preferences distilled from a training-only teacher via rollout + impression supervision — evidence that generative retrieval can carry production-grade ranking quality end-to-end.

### Is Personalized Modality Weighting Actually Personalized? A Controlled Audit of Per-User Weighting Claims in Multimodal Recommenders
- **Authors**: Jingyuan Zheng, Xin Zhang, Yang Gu, Dongjing Wang, Yuxiang Wang, Xudong Shen, Haiping Zhang, Youhuizi Li, Dongjin Yu
- **Institution**: Hangzhou Dianzi University / Alibaba (Hema)
- **Date**: 2026-08-05
- **Link**: [2608.05655](https://arxiv.org/abs/2608.05655)
- **Abstract**: Per-user modality weighting is deployed at billion-user scale in multimodal recommenders via user modality-strength vectors, attention gates, meta-weight hypernetworks, and low-rank guided weights — each claiming ranking gains from user-specific modality preference. Prior evaluations, the authors argue, never isolate a genuinely user-specific signal from a global modality weight plus model capacity. The paper audits this family with a two-contrast principle, reducing six implementations onto one shared collaborative backbone and measuring a utility gap (real-GM) against a single global modality weight and an identifiability gap (real-shuf) against an eval-time permutation of the user-weight binding. Across three short-video corpora, a single global weight already delivers nearly all of the content gain (+1.9/+3.6/+3.5pp over a no-modality baseline); making the weight per-user adds no consistent utility — no implementation wins on all corpora/metrics and the few positive gaps are small (≤0.9pp) and flip. The shuffle control is necessary but not sufficient (real-shuf reaches +128% of the content gain for heads that lose to the global weight); tracing this to gates reading the shared collaborative embedding, decoupling the gate input collapses the inflated real-shuf while the utility conclusion stands. A monotone signal-implant dose-response (capture AUROC 0.57→0.89, 0.64→1.00) verifies the harness would detect user-specific structure if present; findings replicate on a fourth e-commerce corpus.
- **Key Innovation**: A standardized audit (real-GM + real-shuf) for the "personalization claim" — the dominant result being that per-user modality weighting adds no consistent utility over a single global weight, and that eval-time permutation controls can be gamed by capacity.

### Robustness and User-Perceived Value of Popularity Calibration in Music Recommendation: A User Study
- **Authors**: Oleg Lesota, Gustavo Escobedo, Bruce Ferwerda, Simone Kopeinik, Dominik Kowald, Elisabeth Lex, Markus Schedl
- **Institution**: JKU Linz / University of Innsbruck / Jönköping University / Know-Center / TU Graz
- **Date**: 2026-08-06
- **Link**: [2608.05402](https://arxiv.org/abs/2608.05402)
- **Abstract**: Popularity calibration is studied both as user-centered personalization and as an indicator of popularity bias, but most work evaluates it offline, often assuming users prefer lists whose popularity distribution matches their historical profile. This user study constructs personalized track lists from real listening histories and uses a controlled naive recommender to build lists with different popularity compositions (highpop-heavy, lowpop-heavy, calibrated). Results: users perceive differences in popularity composition, but do **not** clearly prefer calibrated lists; the relation between JSD-based calibration and perceived popularity depends on item familiarity, list composition, and available user history; computational and user-judged popularity labels only weakly align.
- **Key Innovation**: A rare user study on calibration that challenges the offline assumption that calibration → preference, and shows the metric's reliability is conditional on familiarity and history availability.

### Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations (READ)
- **Authors**: Sagar Tamang, Ayush Vyas, Tabarakul Hazarika
- **Institution**: —
- **Date**: 2026-08-05
- **Link**: [2608.06305](https://arxiv.org/abs/2608.06305)
- **Abstract**: For an important class of documents — financial statements, audit reports, regulatory returns — chunk-embed-topk retrieval is structurally unsound: on a 780-page government financial report, 86.8% of content lines are table rows, thousands of near-identical figures compete in one embedding space, and a figure inherits its unit from a header a median of 13 lines above it, so a chunk boundary routinely separates a number from its lakh/crore unit (a two-order-of-magnitude error). READ (Reliable Embedding-free Agentic Document-search) replaces embeddings with three deterministic operations — normalized lexical search, structural navigation, and bounded span reads — exposed over MCP so a trajectory is a replayable audit trail. On 51 verified questions READ answers 58.8% vs dense retrieval's 15.7% (or 35.3% tuned, READ still ahead by 23.5 points). An agent with the same loop but a top-k tool reaches only 27.5%, locating the gain in the interface rather than iteration. Caveat: BM25 is statistically indistinguishable from READ — the result separates embedding-based from embedding-free retrieval, not agentic from lexical.
- **Key Innovation**: A causal demonstration that for numeric/table-heavy documents the retrieval *interface* (deterministic agentic operations over MCP) outperforms embedding distance, with the honesty that lexical search alone accounts for the gain.

### EXCISE: Query-Side Exclusion for Late-Interaction Retrieval
- **Authors**: Mohammed Ali, Abdelrahman Abdallah, Adam Jatowt
- **Institution**: University of Innsbruck
- **Date**: 2026-08-05
- **Link**: [2608.05497](https://arxiv.org/abs/2608.05497)
- **Abstract**: Late-interaction retrievers handle exclusion queries ("X but not Z") poorly: the additive MaxSim score actively promotes documents covering Z — "exclusion inversion". EXCISE operates purely at query time and leaves the index frozen: two query-side modules (1.5M params total) identify the excluded topic and re-embed a 100-document shortlist, and a parameter-free rule demotes candidates matching that topic. Across six collections and three backbones EXCISE wins all eighteen backbone-collection cells against frozen and fine-tuned baselines: exclusion success@10 on ExcluIR rises 0.058→0.691, Boolean NOT accuracy 0.25–0.29→0.90–0.92, while matching the frozen baseline on no-harm nDCG@10. Releases X-BENCH (explicit/implicit/compound exclusions).
- **Key Innovation**: A query-side-only fix for exclusion inversion in late-interaction models — correcting a structural scoring failure without touching the index or its vectors.

### A Mechanistic Analysis of Gender Sensitivity in Dense Retrieval Models
- **Authors**: Catherine Chen, Maarten de Rijke, Carsten Eickhoff
- **Institution**: Brown University / University of Amsterdam
- **Date**: 2026-08-05
- **Link**: [2608.05467](https://arxiv.org/abs/2608.05467)
- **Abstract**: Gender bias in dense retrieval is well documented, but its internal mechanism is not. This paper mechanistically analyzes bi-encoders and localizes the bias: the signal originates in the input embeddings and propagates through a small set of late-layer attention heads that carry both gender and term-matching signals. Steering interventions at the two identified points have distinct effects — embedding-level steering non-specifically neutralizes score differences, while attention-level steering produces directional shifts — highlighting the difficulty of disentangling gender from relevance in shared components.
- **Key Innovation**: First mechanistic localization of retrieval gender bias to embedding + a small head set, with a roadmap for targeted (directional) debiasing.

---

## 2. LLM Reasoning, RL & Post-Training

### DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models
- **Authors**: ZhiYan Hou, Xinyu Tang, Hongyan An, Jianjin Zhang, Weizhen Wang, Yunyun Han, Gengsheng Li, Xiangzhao Hao, Haiyun Guo, Wenbin Hu, Jinqiao Wang, Yafeng Deng
- **Institution**: Chinese Academy of Sciences (AIR-CAS)
- **Date**: 2026-08-06
- **Link**: [2608.06243](https://arxiv.org/abs/2608.06243)
- **Abstract**: RLVR gives sparse, sequence-level rewards; on-policy self-distillation (OPSD) mitigates sparsity by querying a privileged teacher at student-visited prefixes for dense token-level supervision. But standard OPSD assigns every local divergence the same coefficient regardless of its position or the divergence sequence in which it occurs — the same divergence magnitude can follow different discrepancy histories, and the local scalar cannot distinguish them. DASH maps the gap between each local distillation signal and the sequence-level mean to an adaptive propagation gate, and uses these gates to control backward multi-step aggregation, so token-level weights adapt to how local divergences evolve during generation. On three math benchmarks across three model scales, DASH improves over matched vanilla OPSD reruns everywhere; it reuses the teacher/student distributions OPSD already computes, so gains cost no extra forward pass.
- **Key Innovation**: Making OPSD's token-level weights sensitive to the temporal *history* of divergence, not just its instantaneous magnitude — a no-extra-cost refinement of privileged-distillation credit assignment.

### AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning
- **Authors**: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang
- **Institution**: Tsinghua Shenzhen International Graduate School / VIVO
- **Date**: 2026-08-06
- **Link**: [2608.05987](https://arxiv.org/abs/2608.05987)
- **Abstract**: Trajectory-level advantage estimates in verifiable-reward RL fail to credit the few pivotal decisions in long-horizon, multi-turn agentic tasks. AgentOPSD is a critic-free, recursive turn-level credit assignment method: it aggregates token-level teacher–student log-probability gaps into turn-level evidence and recursively updates a Bayesian belief state in log-odds space, producing a principled reweighting that converts sparse outcome supervision into turn-level credit and identifies pivotal turns via marginal belief revision. No critic, no extra rollouts. On ALFWorld, WebShop, and Search-QA with Qwen2.5-3B/7B, AgentOPSD beats GRPO and strong self-distillation baselines (89.1% success on ALFWorld at 7B); ablations attribute gains to turn-level aggregation and history-dependent recursive updates.
- **Key Innovation**: Bayesian-belief recursion (log-odds space) as the aggregation mechanism for turn-level credit — connecting privileged self-distillation to a principled inference procedure rather than heuristic reweighting.

### RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction
- **Authors**: Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, Xiaoyang Hao, Yuxin Gao, Tianhua Zhou, Xiaojia Chang, Tongran Liu, Jingbo Zhu
- **Institution**: Northeastern University (China)
- **Date**: 2026-08-06
- **Link**: [2608.06310](https://arxiv.org/abs/2608.06310)
- **Abstract**: Generative reward models (GRMs) show a paradigm shift from discriminative reward models, but have not realized their potential in RL. The paper identifies the cause: a mismatch between the *comparative* nature of GRM scoring and the *scalar* scoring paradigm of existing RL algorithms. RRC (Ranking-based Reward Construction) derives RL rewards from relative preference rankings via two complementary strategies — self-competitive ranking (comparisons among sampled responses) and anchor-guided ranking (scalable ranking construction against a small reference set). Experiments on open-ended chat and reasoning benchmarks show consistent gains over existing reward-construction approaches.
- **Key Innovation**: Reframing GRM supervision for RL from scalar scores to ranking-based rewards — bridging a representational mismatch that was blocking GRMs from being useful RL signals.

### Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning
- **Authors**: Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Lena Trigg, Ali Subhan, Muhammad Ali, Dean F. Hougen
- **Institution**: University of Oklahoma
- **Date**: 2026-08-06
- **Link**: [2608.05643](https://arxiv.org/abs/2608.05643)
- **Abstract**: Test-time scaling helps reasoning, but wider sampling suffers diminishing returns — new rollouts repeat existing answer patterns. Verifier-based selection depends on the calibration of an external reward model. The paper proposes a verifier-free breadth–depth refinement framework: sample multiple independent rollouts, refine each via iterative self-critique and self-correction, and aggregate by majority voting. Breadth preserves diverse attempts, depth repairs local errors before aggregation. Across AIME24/25, AMC, OlympiadBench, and MATH500, the method consistently beats greedy decoding, majority voting, verifier-based best-of-N, beam search, and lookahead across multiple open-weight models (e.g., Qwen2.5-1.5B: 58.0% on MATH500, 25.0%→32.5% on AMC vs the strongest verifier baseline).
- **Key Innovation**: An explicit argument that test-time compute is better spent refining sampled trajectories than sampling more candidates or relying on external verifiers.

### Position: It's Time to Optimize LLMs for Self-Consistency
- **Authors**: Itamar Pres, Belinda Z. Li, Laura Ruis, Zifan Carl Guo, Keya Hu, Mehul Damani, Isha Puri, Ekdeep Singh Lubana, Jacob Andreas
- **Institution**: MIT
- **Date**: 2026-08-06
- **Link**: [2608.05188](https://arxiv.org/abs/2608.05188)
- **Abstract**: ICML 2026 Position Paper. Many persistent LM failures — sycophancy, incomplete logical generalization, confident-but-wrong answers — arise from a modeling assumption permeating the pipeline: that behavior can be specified and evaluated independently on single-output pairs. The paper proposes self-consistency as a unifying framework: a wide variety of techniques targeting diverse properties (adversarial robustness, factual coherence, and more) can be understood as special cases of a common "consistency optimization" procedure and addressed with standard optimization tools. It outlines new properties achievable by optimizing for consistency and discusses what generally consistent LMs would enable.
- **Key Innovation**: A position-paper reframing of LM failures as single-output-pair evaluation artifacts, unifying many scattered techniques under one "consistency optimization" umbrella.

### EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning
- **Authors**: Zishan Xu, Zhiyuan Yao, Yuxin Chen, Yifu Guo, Zhengxi Lu, Yuquan Lu, Jinyang Huang, Yan Xu, Yasheng Wang, Weinan Zhang, Xingshan Zeng, Weiwen Liu
- **Institution**: Shanghai Jiao Tong University / Huawei Noah's Ark Lab
- **Date**: 2026-08-06
- **Link**: [2608.06197](https://arxiv.org/abs/2608.06197)
- **Abstract**: Training long-horizon tool-use LLM agents typically needs real or synthesized executable environments (costly to build/verify) or external simulators (hard to ground). EnvACE replaces external environment interaction during training with **world rehearsal**: the policy alternates between acting and rehearsing — generate a tool call, then play the role of the environment to produce the response that action induces, and condition subsequent decisions on the rehearsed response. Both roles are jointly optimized end-to-end with task-success rewards, internalizing action→response dynamics in the parameters (an agent world model). Across BFCL-v4, tau²-Bench, VitaBench, and FinMCP-Bench, EnvACE outperforms environment-scaling baselines overall, improves policy learning across model scales, and at test time enables private rehearsal before committed execution for further gains under a moderate budget.
- **Key Innovation**: Training agent RL entirely via self-rehearsed environment responses — eliminating the external-environment bottleneck and producing an internalized world model usable for pre-commit rehearsal.

---

## 3. Sequential Modeling, LLM Architecture & Inference Efficiency

### Answer First, Reason Later: Commitment Order in Diffusion LLMs
- **Authors**: Jewon Yeom, Jaewon Sok, Seonghyeon Park, Jeongjae Park, Hwiyeong Lee, Taesup Kim
- **Institution**: Seoul National University
- **Date**: 2026-08-06
- **Link**: [2608.05687](https://arxiv.org/abs/2608.05687)
- **Abstract**: Masked diffusion LLMs (dLLMs) can commit tokens in any order — marketed as a core advantage — but on reasoning tasks this freedom is the axis of failure. Logging every commitment during LLaDA-8B decoding on GSM8K, the authors find unconstrained decoding commits the final answer at 15–24% of the trajectory while half the reasoning region is still masked, collapsing to answer-only outputs on up to 90% of problems as the canvas grows. The cause is not termination beliefs (EOS pressure is nearly identical across decoders) but reachability — whether the sampler can act on those beliefs at distant positions. A 2×2 prompt×decoder design shows chain-of-thought helps only under ordered commitment (+34.8pp interaction). A single-knob intervention — **frontier-gated commitment** — causally recovers the full gap (0.528→0.852) while preserving up to 4× parallel decoding, with the optimal gating window flipping from w=1 at full refinement to unconstrained at 8 tokens/step.
- **Key Innovation**: Diagnosing the failure of reasoning dLLMs as a commitment-order pathology (answer committed before reasoning) rather than a model-belief problem, and fixing it with a single frontier-gating knob — reframing window-style samplers (previously efficiency-motivated) as the minimal fix for a reasoning defect.

### Hierarchical Latent Prediction for Language Models (HiLP)
- **Authors**: Chang Shi, Tim Pearce, Manan Tomar, Siddhartha Sen, John Langford
- **Institution**: Microsoft Research
- **Date**: 2026-08-06
- **Link**: [2608.05806](https://arxiv.org/abs/2608.05806)
- **Abstract**: Next-token prediction's teacher-forced paradigm may be suboptimal for long-horizon reasoning and planning. Multi-Token Prediction and Next-Latent prediction mitigate this but suffer limited horizon or compounding error from multi-step latent rollout. HiLP adds a **higher-level abstract latent** to reduce error accumulation in latent-space rollouts. Experiments show longer-horizon coherent belief-state representations and effectiveness on coding and multi-step reasoning benchmarks, plus better speculative decoding efficiency.
- **Key Innovation**: A hierarchy of latent prediction targets to control compounding rollout error — an architectural answer to "predict at what horizon do we supervise".

### Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers (SiPE)
- **Authors**: Haris Riaz, Hyungji Kim, Mihai Surdeanu
- **Institution**: University of Arizona
- **Date**: 2026-08-06
- **Link**: [2608.06111](https://arxiv.org/abs/2608.06111)
- **Abstract**: Positional embeddings encode token distance and order but are largely agnostic to syntactic structure. SiPE learns a lightweight syntactic prior from dependency parses during pretraining and injects it across all three dominant PE families (absolute, relative, rotary), for both encoders and decoders, without touching attention. The best injection point depends on architecture: for autoregressive decoders with relative PE, coupling multiplicatively with the relative-position term of the attention score is strongest; for encoders, adding to the input embeddings. Models pre-trained with SiPE improve SyntaxGym by up to +10.3% while *reducing* perplexity by 9.0% (a metric nearly every existing syntax-injection method degrades), and gains extend to GLUE (+8.2%). SiPE conditions on a single parse, establishing a new Pareto frontier between syntactic supervision and inference cost.
- **Key Innovation**: Syntax supervision that simultaneously improves a syntax benchmark *and* perplexity and GLUE — unlike prior syntax-aware methods that trade language modeling for syntax — via architecture-dependent injection.

### MACRO: Markov Chain Routing of Transformer Layers
- **Authors**: Paweł Batorski, Abtin Pourhadi, Akylgali Aitaza, Przemysław Spurek, Paul Swoboda
- **Institution**: University of Warsaw / Jagiellonian University / University of Mannheim
- **Date**: 2026-08-06
- **Link**: [2608.05872](https://arxiv.org/abs/2608.05872)
- **Abstract**: Dynamic layer routing — skips, repeats, and other moves through an LLM's layers — can improve performance, but existing methods need weight updates, per-instance search loops, or ground-truth labels at inference. MACRO learns task-specific routes without modifying parameters: it models routing as a context-dependent Markov policy conditioned on layer indices, compute-budget phases, directional displacements, and operator context (skip/repeat/residual-add), updates the route distribution via feedback on training data, and decodes with a top-k Viterbi algorithm. Across reasoning/knowledge benchmarks on multiple open-weight LLMs, MACRO gains +5.0% average accuracy over unrouted baselines (largest on small models), beats the best prior routing approach Dr. LLM by +7.2%, and cuts route-search time 9.4× (14.8→1.6 hours).
- **Key Innovation**: Markov-chain layer routing as a learned, parameter-free, train-only-search policy with Viterbi decoding — making per-task routing practical without per-instance cost or weight changes.

### QEvict: Recoverable Quantized KV Eviction for Attention-Drift-Robust Long-Context Decoding
- **Authors**: Ayushman Garg, Akshita Gupta, Shaswata Bhattacharya, Abhishek Gupta, Sandeep Kumar, Manoj Kumar
- **Institution**: (IIT Kanpur / Meta)
- **Date**: 2026-08-06
- **Link**: [2608.05326](https://arxiv.org/abs/2608.05326)
- **Abstract**: KV-cache eviction policies make an implicit irreversible decision: once a token is evicted it can never become useful again. The paper shows this assumption is brittle: token and window importance drift as generated queries evolve, so standard policies permanently discard states that later receive substantial attention under the full-cache model. Introducing two diagnostics (Future Missed Mass, Global LIR), the authors propose QEvict, a three-tier cache management scheme that replaces binary retain-or-delete with **recoverable eviction**: high-confidence windows stay full-precision, intermediate windows go into a quantized recoverable tier, and only the lowest-confidence windows are deleted; when a quantized window regains importance, cumulative attention promotes (dequantizes) it. Under a fixed memory budget this preserves broader context while keeping exact precision on the most important regions, consistently improving over eviction and quantization baselines on long-context understanding, retrieval, and reasoning benchmarks.
- **Key Innovation**: Turning KV eviction from irreversible to recoverable — a three-tier full/quantized/deleted hierarchy with attention-driven promotion that directly targets the attention-drift failure mode of standard eviction.

---

## 4. Agents, Skills & Personalization

### TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories
- **Authors**: Yunjia Qi, Zehua Yin, Xintong Shi, Hao Peng, Songyuanyi Lu, Yixian Liu, Richeng Xuan, Yuhong Liu, Zhichao Hu, Xiaozhi Wang, Lei Hou, Bin Xu, Juanzi Li
- **Institution**: Tsinghua University
- **Date**: 2026-08-06
- **Link**: [2608.06346](https://arxiv.org/abs/2608.06346)
- **Abstract**: Critical error detection aims to locate the earliest error step responsible for a failed agent trajectory, but long trajectories scatter evidence across distant instructions/observations and failed trajectories contain multiple local errors with different downstream effects. TrajDebug is an error-lifecycle tracing framework: multi-granularity history compression + evidence-based error identification, with critical attribution by tracing each error's resolution status and terminal impact. Ships TrajErrBench, 486 manually annotated failed trajectories from Tau2Bench and SWE-Bench Pro. Best overall performance over baselines across agent benchmarks; diagnoses transfer into actionable downstream fixes.
- **Key Innovation**: Treating error *lifecycle* (resolution status + terminal impact) as the attribution signal — not just "where does the trajectory go wrong" but "which error is actually still responsible at the end".

### LUNAR: Benchmarking Personalized LLMs on Universal User Behavior Logs
- **Authors**: Jiahao Zhang, Yongzhi Tong, Zelin Fu, Pengde Zhao, Yanmei Jiang, Jiang Feng, Min Yang
- **Institution**: Shenzhen University
- **Date**: 2026-08-06
- **Link**: [2608.05246](https://arxiv.org/abs/2608.05246)
- **Abstract**: Personalized LLM benchmarks rely mostly on textual personas or isolated behavioral signals. LUNAR is the first benchmark for **cross-domain behavioral personalization** from longitudinal app-interaction histories across clothing, food, housing, and mobility, built with a multi-stage coarse-to-fine synthesis pipeline grounded in real behavioral patterns. Findings across 19 mainstream LLMs: behavioral-log access is necessary but not sufficient — neither more context nor larger models guarantee better performance; direct retrieval of fine-grained behavioral records consistently beats compressed memory; stronger personalization can come at the cost of privacy protection.
- **Key Innovation**: A behavioral-log-based (not persona-based) personalization benchmark that surfaces evidence selection, cross-domain integration, and privacy control as the actual bottlenecks.

### Cautious Context Steering for Language Model Personalization (CCS)
- **Authors**: Gihoon Kim, Jeyoung Lee, Suhan Woo, Sekwon Oh, Minsu Jeon, Hyounsoo Han, Euntai Kim
- **Institution**: Yonsei University
- **Date**: 2026-08-06
- **Link**: [2608.05813](https://arxiv.org/abs/2608.05813)
- **Abstract**: Per-user adapter training and user-dependent reward models suffer data sparsity and poor generalization to unseen users/domains. In-context learning and Context Steering (CoS) condition the base LM directly on user context without per-user training, but neither adapts the influence of that context across decoding steps — ICL leaves it uncontrolled, CoS applies a fixed coefficient and doubles forward passes. CCS adds a lightweight adapter to a frozen backbone that decides at each token whether and how strongly user context should affect generation, learned from an oracle context-conditioned LM, preserving the base LM when context is unhelpful. A single adapter trained on one dataset improves generation in-domain and across four OOD personalization benchmarks, avoiding per-user fine-tuning and the extra forward pass.
- **Key Innovation**: Token-level, learned control of user-context influence with an "abstain when unhelpful" behavior — per-token steering without per-user training or doubled inference cost.

### Search2Skill: Skill Distillation Beyond Knowledge Boundaries via Rubric-Based Reinforcement Learning
- **Authors**: Muyang Ye, Tian Lan, Feihu Jiang, Yongshi Ye, Wuyunsiqin, Bin Zhu, Qianghuai Jia, Zhao Xu, Weihua Luo, Ye Wang, Jinyang Zhang, Longyue Wang, Lingfeng Bao
- **Institution**: Alibaba Group / Beijing Institute of Technology
- **Date**: 2026-08-06
- **Link**: [2608.05245](https://arxiv.org/abs/2608.05245)
- **Abstract**: Self-evolving skill methods build skills from the model's parametric knowledge or trajectories — bounded by what the model already knows. Search2Skill automatically identifies capability gaps, searches external sources to address them, and distills retrieved evidence into structured, reusable skills, optimized by a **rubric-based RL** scheme that jointly improves when to search, how to search, and how to generate skills. On eight expert-level domains from three benchmarks it outperforms search-augmented and trajectory-based skill-learning baselines under streaming and held-out evaluation; gains arise from skill abstraction rather than raw retrieved evidence, and skills transfer across model scales.
- **Key Innovation**: Moving skill distillation beyond the model's parametric knowledge boundary via retrieval + rubric-RL, with ablation evidence that abstraction (not retrieval volume) drives the gain.

---

## 5. Games, World Models & Simulation

### GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models
- **Authors**: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang
- **Institution**: Shanghai Jiao Tong University / Shanghai AI Laboratory / Zhejiang University / University of Adelaide
- **Date**: 2026-08-06
- **Link**: [2608.05948](https://arxiv.org/abs/2608.05948)
- **Abstract**: Physics engines and generative video world models are increasingly used as simulators for embodied intelligence, but physical-fidelity evaluation is conducted in isolation and relies on perceptual similarity or human judgment. GAUGE is a real-world-grounded diagnostic benchmark of 22 controlled task families (rigid bodies, flexible cables, textiles, volumetric deformables) spanning collision, friction, momentum transfer, oscillation, self-contact, and deformation. It benchmarks Isaac Sim, Genesis, and Newton on 14 task families with generalized trajectory errors, and six image-to-video models on 5 rigid-body tasks via physical-law consistency and temporal parameter stability. Findings: no uniformly faithful physics engine (worst on impulsive contact, rapid textile motion, volumetric deformation); video world models can produce equation-consistent trajectories while recovering *incorrect* accelerations, momentum transfer, and oscillation timing.
- **Key Innovation**: A measurement-grounded (trajectory + physical metadata) joint benchmark for engines *and* world models that separates "trajectory looks right" from "underlying physics parameters are right" — exposing equation-form-but-wrong-dynamics failures in generative world models.

### Otter: A Time-Aware, History-Conditioned Human Chess AI
- **Authors**: Tarun Kumar S
- **Institution**: —
- **Date**: 2026-08-06
- **Link**: [2608.05206](https://arxiv.org/abs/2608.05206)
- **Abstract**: Otter is a 15.3M-parameter human chess AI that predicts human move selection by modeling play as a time-aware, sequential process rather than each position in isolation. It conditions on the last 20 moves (history encoder) and on clock pressure (time control module), trained on 6.1 billion positions from 117M Lichess rapid games over 30 days on a single T4 GPU. It reaches 55.23% top-1 and 90.95% top-5 move-prediction accuracy, surpassing prior SOTA human-chess model Maia 2 with far fewer parameters and less data; across 11 Elo brackets accuracy peaks at 57.38% in the 1900–1999 bracket.
- **Key Innovation**: A sequence-conditioned (history + clock) human-move predictor that beats position-only models at a fraction of the size — supporting chess-as-sequential-process over chess-as-position.

### AV-AIVAT: 74× Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games
- **Authors**: Boning Li, Yu Chen, Longbo Huang
- **Institution**: Tsinghua University
- **Date**: 2026-08-06
- **Link**: [2608.06362](https://arxiv.org/abs/2608.06362)
- **Abstract**: Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money/inference/expert time. Fixed budgets either keep paying after the result is settled or stop too early; naive optional stopping invalidates the confidence level. AV-AIVAT combines the Action-Informed Value Assessment Tool (AIVAT, median 54× variance reduction across 15 LLM agent configs / 71,439 HUNL hands) with continuously monitored Confidence Sequences into an anytime-valid stopping rule: at the nominal 95% level and ±1 BB precision, raw outcomes need a median 74× as many hands as AIVAT-corrected outcomes to stop under the asymptotic CS. Exact finite-sample certification uses an Empirical-Bernstein CS with a structurally derived bound on corrected payoffs (Leduc hold'em), separating asymptotic screening from exact certification and enabling auditable stopping.
- **Key Innovation**: Variance reduction + anytime-valid statistics as a *certified* early-stopping procedure for agent evaluation — stopping the moment evidence suffices, with a recheckable verdict at that exact stopping time.

### IFlowNets: Extending Generative Samplers to Learn Strategies in Incomplete Information Games
- **Authors**: Conor M. Artman, Nicholas Di, Scott Perkins
- **Institution**: Georgia Institute of Technology
- **Date**: 2026-08-06
- **Link**: [2608.05422](https://arxiv.org/abs/2608.05422)
- **Abstract**: Generative flow networks are underexplored in game-theoretic settings with incomplete information. The paper extends Adversarial Flow Networks (AFlowNets) to incomplete-information games as Information Flow Networks (IFNs), and proves that the previously established generative-flow constraints for complete-information games are **inadmissible** for obtaining valid densities (player strategies) and a valid training objective there. IFlowNets generalizes AFlowNets and, in three standard game environments, performs comparably to or better than Outcome Sampling Monte Carlo CFR and standard RL methods in performance and speed.
- **Key Innovation**: A correctness result — showing existing GFlowNet flow constraints break under incomplete information — plus a generalized framework that recovers valid strategy densities in imperfect-information games.

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Verifiable/agentic RL supervision is the day's signature theme** | Three independent takes on dense, distributional credit: divergence-history-adaptive OPSD (DASH), Bayesian recursive turn-level credit (AgentOPSD), and environment-free world-rehearsal training (EnvACE) — plus ranking-based GRM rewards (RRC) | DASH, AgentOPSD, EnvACE, RRC |
| **Recommender claims get audited** | Per-user modality weighting adds no consistent utility over one global weight (with a standardized audit protocol); popularity calibration isn't clearly preferred by users and its metric is conditional on familiarity/history; and a single generate-and-rank model can replace a 15+ generator cascade at Yandex | Modality Weighting Audit, Popularity Calibration User Study, Gryphon-v2 |
| **Retrieval gets mechanism-aware and interface-aware** | Late-interaction exclusion inversion fixed at query time (EXCISE); deterministic agentic ops beat embeddings on table-heavy documents, traceable to the interface not iteration (READ); first mechanistic localization of gender bias in bi-encoders | EXCISE, READ, Gender Sensitivity DR |
| **Reasoning fidelity at the decoding frontier** | Diffusion LLMs fail by committing answers before reasoning (frontier-gated commitment fixes it, Answer First); test-time compute is better spent refining than resampling (Refining); higher-level latent targets reduce compounding rollout error (HiLP); syntax-aware PEs improve perplexity AND syntax benchmarks (SiPE) | Answer First, Refining, HiLP, SiPE |
| **Efficiency with recoverability** | KV eviction becomes recoverable via a quantized intermediate tier with attention-driven promotion (QEvict); Markov-chain layer routing is train-free and search-fast (MACRO) | QEvict, MACRO |
| **World models and simulators get physical-fidelity diagnostics** | GAUGE shows no physics engine is uniformly faithful and that video world models produce equation-shaped but dynamically wrong trajectories; IFlowNets gives correctness guarantees for GFlowNet strategies under incomplete information; AV-AIVAT certifies when agent-evaluation games can stop | GAUGE, IFlowNets, AV-AIVAT |

---

## Key Takeaways

1. **Agentic/verifiable RL supervision is converging on dense, distribution-shaped credit.** DASH (divergence-adaptive OPSD), AgentOPSD (Bayesian recursive turn credit), and EnvACE (world rehearsal instead of external environments) all attack the same soft spot — sparse trajectory rewards in long-horizon settings — from different mechanisms. EnvACE in particular suggests a path to scaling agent training without environment infrastructure. RRC shows generative reward models need ranking-based (not scalar) rewards to work in RL.
2. **Recommender "personalization claims" are under empirical attack, and one cascade just died.** The modality-weighting audit argues per-user weighting adds no consistent utility over a single global weight (and that shuffle controls are gamed by capacity); the music-calibration user study finds users don't prefer calibrated lists. Meanwhile Gryphon-v2 replaces a 15+ generator cascade with one generate-and-rank model at Yandex Music (+1.41% active users) — the most concrete industrial proof yet that generative retrieval can absorb ranking quality.
3. **Diffusion LLM reasoning is a commitment-order problem, not a belief problem.** Answer First shows the answer gets committed mid-trajectory because the sampler can act on EOS beliefs at distant positions, and a frontier-gating knob recovers the full gap while preserving parallelism — reframing window-style samplers as reasoning fixes, not just efficiency tricks.
4. **Retrieval is becoming mechanism- and interface-first.** EXCISE fixes exclusion inversion without touching the index; READ shows deterministic agentic ops (MCP-exposed) outperform embeddings on numeric/table-heavy documents, honestly attributing the gain to lexical search over the interface; the mechanistic gender-bias analysis localizes retrieval bias to embeddings + a small attention-head set. The theme: "what does the retriever actually compute" is now a first-class research question.
5. **Efficiency is adding recoverability and adaptability.** QEvict replaces irreversible KV eviction with a recoverable quantized tier that can promote evicted-window regions back; MACRO learns per-task Markov layer routes with no weight changes and 9.4× less search. Both move serving-efficiency from "static choice" toward "state that can be revised".
6. **Physical fidelity of simulators and world models is now measured, not assumed.** GAUGE's 22 task families show no engine is uniformly faithful and that video world models can match equation form while getting acceleration/momentum/timing wrong — a needed corrective as world models are proposed as implicit simulators.
7. **Games remain a rigorous evaluation and algorithm testbed.** AV-AIVAT certifies anytime-valid early stopping for agent evaluation (74× cheaper HUNL evals); IFlowNets proves GFlowNet constraints must change under incomplete information; Otter shows a 15M-parameter history+clock chess model beats Maia 2.

> ⚠️ Note on sourcing: All papers verified against the arXiv **Fri Aug 7, 2026** announcement listing (stream sizes cs.AI 201 / cs.CL 94 / cs.LG 162 / cs.IR 15 / stat.ML 22 new, per listing-page headers; ID range ~2608.05150–2608.06380). The arXiv API was intermittently rate-limited (HTTP 503/429) during curation, so metadata was verified via arXiv listing and abs pages. No dedicated advertising/CTR paper was found in today's cs.IR stream; industrial coverage is via the Yandex Music recommendation paper. Papers in the same-day [arXiv Paper Check](../2026-08-06/arxiv-paper-check.md) and [AI scan](../2026-08-06/arxiv-ai-search.md) are from the Aug 6 window and do not overlap this digest.
