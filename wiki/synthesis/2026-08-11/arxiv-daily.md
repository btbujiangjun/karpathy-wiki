---
title: "arXiv Daily Digest — 2026-08-11"
type: synthesis
created: 2026-08-11
updated: 2026-08-11
sources: [arxiv-cs.AI, arxiv-cs.LG, arxiv-cs.CL, arxiv-cs.IR, arxiv-cs.GT, arxiv-cs.MA, econ.TH, stat.ML]
tags: [arxiv, llm, on-policy-distillation, reasoning, test-time-scaling, agents, skills, memory, kv-cache, efficiency, sequential-modeling, time-series, recommendation, generative-ranking, advertising, games, game-theory, theory-of-mind, interpretability, safety, daily-digest]
---

# arXiv Daily Digest — 2026-08-11

> **Batch note:** arXiv's latest *announced* listing is still Mon Aug 10, 2026 (covered by yesterday's [arxiv-daily](../2026-08-10/arxiv-daily.md), [arxiv-paper-check](../2026-08-10/arxiv-paper-check.md), [arxiv-ai-search](../2026-08-10/arxiv-ai-search.md), [game-rl-daily](../2026-08-10/game-rl-daily.md) and [conference-digest](../2026-08-10/conference-digest.md)). The **Tue Aug 11 announcement lands ~20:00 ET (= 08:00 +08 Aug 12)**, so this digest is a **zero-overlap breadth pass over the fresh Aug 9–10 submission window retrieved ahead-of-announcement via the arXiv API** (submittedDate 2026-08-09→10, IDs ~2608.08382–2608.09930). Today's [paper-check](../2026-08-11/arxiv-paper-check.md) (18 papers) and [game-rl-daily](../2026-08-11/game-rl-daily.md) (19 papers) already curated the CTR/Rec/Ads and games clusters from the overlapping window; this digest covers the **cs.LG/cs.CL/cs.GT/econ.TH remainder** — **31 papers, all grep-verified absent from the entire wiki**. Signature themes of this window: **on-policy self-distillation turns into the dominant post-training axis with a heavy theoretical corrective** (PAST, SR-OPSD, SKALD, "Privileged Likelihood"), **KV-cache security becomes a first-class multi-tenant concern** (KVGov), **verifier-free test-time scaling gets a confidence-trajectory theory** (Consilience), **reasoning-trace styles become a measurable failure mode for subjective verification** (RLVR collapse), and **generative ranking matures into executable-strategy control planes in production** (MetaStrategy at Taobao).

---

## 1. LLM Post-Training & On-Policy Self-Distillation

### PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation
- **Authors**: Yangyang Feng, Zhuoyan Feng, Junlan Chen
- **Institution**: HKUST (Guangzhou) + Sun Yat-sen University
- **Date**: 2026-08-09
- **Link**: [2608.08726](https://arxiv.org/abs/2608.08726)
- **Abstract**: On-policy self-distillation (OPSD) uses a privileged teacher to supervise a reasoning model on prefixes sampled from its own rollouts, but standard OPSD ignores *how* the student's response unfolded and whether it succeeded. PAST treats each **completed student trajectory as additional privileged information** for the OPSD teacher (adapting the teacher toward verified success with student-proximity regularization) while leaving the student's distillation prefixes unchanged. A distributional analysis shows forward-KL distillation projects teacher distributions to their **conditional arithmetic mean given the prefix** — separating trajectory-specific variation (stays privileged) from the mean policy shift (available to the student); for correct trajectories, the unclipped population objective has the frozen student as an ideal fixed point. PAST improves Avg@12 over Vanilla OPSD by **5.6 percentage points** across three math benchmarks; a 2×2 factorial plus trajectory removal/shuffling confirms both complete-trajectory access and teacher adaptation matter.
- **Key Innovation**: The first use of the *outcome* of the student's own full rollout (success/failure hindsight) as teacher signal in OPSD — with a clean characterization of exactly what a trajectory-conditioned teacher can transfer to a prefix-only student.

### SR-OPSD: Self-Referenced On-Policy Self-Distillation
- **Authors**: Zhuo Sun, Entong Li, Yanlong Zhao, Xiaoyuan Cheng, Wenxuan Yuan, Kaiyu Li, Che Liu, Huihang Liu, Harrison Bo Hua Zhu, Li Zeng
- **Institution**: Shanghai University of Finance and Economics + Imperial College London
- **Date**: 2026-08-10
- **Link**: [2608.09745](https://arxiv.org/abs/2608.09745)
- **Abstract**: The OPSD self-teacher (stop-gradient or EMA copy of the student conditioned on extra context) **co-evolves with the student and its on-policy context distribution**, so matching a moving target with a fixed projection can be unstable or over-concentrate. SR-OPSD derives a token-level variational characterization showing the effective distillation target is a **geometric interpolation between the self-teacher and a reference policy**, and generalizes the projection geometry via the **Rényi divergence family** — cleanly separating *where* the adaptive target sits (interpolation coefficient) from *how* the student is projected toward it (Rényi order, sensitivity to token-level density ratios). It achieves SOTA or competitive performance across scientific evaluation, math, and code generation with multiple LLMs.
- **Key Innovation**: Formalizes the "moving target" pathology of OPSD and gives a two-knob formulation (target placement + projection geometry) that decouples stabilization from distributional control — the wiki's OPSD cluster (Aug 7–11) gains a principled stabilization recipe.

### Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation (SKALD)
- **Authors**: Yubo Jiang, Fengying Xie, Zhiguo Jiang, Haopeng Zhang
- **Institution**: Beihang University (likely)
- **Date**: 2026-08-10
- **Link**: [2608.09826](https://arxiv.org/abs/2608.09826)
- **Abstract**: RL with verifiable rewards produces **no group-relative signal when rollout groups are uniformly correct or uniformly wrong — 63.0–68.0% of groups** in the paper's experiments. SKALD (Skill-Anchored Latent Distillation) is an OPSD framework with two context views of the same Qwen3-Base model: a question-only student and a teacher conditioned on an **abstract, explicit-answer-filtered skill card**; the student learns on its own prefixes, transferring the skill-induced advantage into shared parameters with no privileged input at test time. An **annealed exponentially tilted objective** downweights teacher-preferred tokens with very low student likelihood (converging to teacher cross-entropy and recovering the forward-KL gradient as the tilt vanishes), and an empirical gate activates distillation only when verified rollouts estimate positive teacher advantage. SKALD beats GRPO by +2.46/+4.85/+12.01 avg@8 at 0.6B/1.7B/4B on five math benchmarks; at 1.7B it exceeds FLOP-matched GRPO by +4.06 and contextual skill exposure by +3.77.
- **Key Innovation**: Directly answers the OPSD cluster's open question about *what* to condition the teacher on — abstract skill cards as dense supervision exactly where group-relative rewards are uninformative (uniformly-correct/wrong groups), compressed into weights rather than prompts.

### Privileged Likelihood Is Not Automatically Value: Three Checks for Token Credit in On-Policy Self-Distillation
- **Authors**: Xuan-Phi Nguyen, Shrey Pandit, Yiran Zhao, Anurag Koul, Zeyu Liu, Shafiq Joty
- **Institution**: Salesforce AI Research
- **Date**: 2026-08-10
- **Link**: [2608.09263](https://arxiv.org/abs/2608.09263)
- **Abstract**: Outcome verifiers score completed traces but not intermediate tokens; privileged self-distillation rescales a model's own rollout with training-only info. This paper shows a **token likelihood change is not automatically outcome credit**, separating three questions: (1) does the score track better actions, (2) does feedback construction change what is compared, (3) what behavior does the training loss reinforce. When a rollout is scored with hindsight feedback written about that *same* rollout, content determines both tokens and scoring context (**direct self-dependence**); using feedback from another rollout removes it but doesn't guarantee usefulness. In matched 20B-model experiments on AIME 2025, the implemented additive score is near chance (AUC=0.505) and slightly favors incorrect traces after length adjustment; an outcome-only control records 64.2% vs 24.2–33.9% for five token-score variants.
- **Key Innovation**: A rigorous negative-result audit of token-level "credit" signals in OPSD — validating score meaning, feedback construction, and training behavior *separately* before calling a likelihood signal credit. Directly qualifies the enthusiasm around this window's OPSD cluster.

### SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation
- **Authors**: Jefferson Hernandez, Jaywon Koo, Zilin Xiao, Chen Wei, Vicente Ordonez
- **Institution**: Rice University
- **Date**: 2026-08-10
- **Link**: [2608.09271](https://arxiv.org/abs/2608.09271)
- **Abstract**: Group-based RL objectives like GRPO allocate learning signal poorly across prompt difficulty: under binary rewards, z-score group normalization induces **divergent weighting on easy prompts**. SoftmaxGRPO replaces z-score-normalized group advantages with **temperature-scaled softmax advantages**, keeping weights bounded regardless of difficulty. For binary rewards the exact finite-group population objective is derived, with **MaxRL identified as its low-temperature limit**; for bounded scalar rewards the large-group update exactly optimizes a log-moment-generating-function objective, and a universal finite-group scalar objective provably cannot exist without extra reward assumptions. SoftmaxGRPO reallocates gradient budget away from near-solved prompts and consistently beats GRPO under identical rewards: **51.8% on DeepMath** with verifiable rewards, and **35.0%→68.0%** on Poetry for a 1.5B instruction-tuned model using only lightweight text-similarity rewards.
- **Key Innovation**: A drop-in group-advantage fix for the "easy-prompt gradient starvation" of GRPO, with exact finite/large-group theory — a cleaner reward-normalization axis for the wiki's RLVR/GRPO line (DASH, GRPO-LoRA, OPD²).

---

## 2. Reasoning & Test-Time Scaling

### Consilience for Verifier-Free Test-Time Scaling
- **Authors**: Lecheng Kong, Like Hui, Haitao Mao, Jun Huan
- **Institution**: AWS AI Labs
- **Date**: 2026-08-10
- **Link**: [2608.09898](https://arxiv.org/abs/2608.09898)
- **Abstract**: Confidence-based verifier-free test-time scaling (VF-TTS) ranks rollouts purely by confidence — but this paper shows such methods **catastrophically break down on complex tasks**: uniformly high confidence often signals failure to explore, favoring *confidently wrong* answers. The core insight: robust cognitive search needs a specific **confidence trajectory** — low initial confidence (exploratory branching) converging to high final certainty. Consilience operationalizes this via a combinatorial metric that **penalizes high initial confidence while demanding final certainty**. Across graduate-level math and free-form code generation, it outperforms existing confidence-based VF-TTS baselines.
- **Key Innovation**: Reframes VF-TTS selection from *final* confidence to the *temporal asymmetry* of confidence — a cheap, state-agnostic selection criterion that directly extends the wiki's test-time-scaling line (s1, TTRL, verifier debates) without needing a verifier.

### Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute
- **Authors**: Nikita Kozodoi, Zainab Afolabi, Jack Butler
- **Institution**: Amazon Web Services
- **Date**: 2026-08-10
- **Link**: [2608.09351](https://arxiv.org/abs/2608.09351)
- **Abstract**: Self-consistency spends all its test-time compute budget on output-side diversity (repeated reasoning paths). This paper studies Test-Time Augmentation (TTA) — perturbing the *input* and aggregating across transformed versions — under **matched compute**, comparing three input-side strategies (semantic rephrasing, lexical perturbations, visual transformations) across six datasets against CoT prompting and self-consistency. Semantic rephrasing Pareto-dominates self-consistency on cost-effectiveness: **~1.8× more accuracy per dollar**, better on five of six tasks. TTA is most cost-effective for mid-tier models where a stronger model is unavailable or too expensive.
- **Key Innovation**: A deployment-facing result for the test-time-scaling economy — at matched compute, input-side diversity beats output-side diversity for mid-tier LLMs, complementing the wiki's compute-efficiency threads (Self-Refine, budgeted agent evals).

### LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing
- **Authors**: Juncheng Dong, Ding Tong, Ishan Gupta, Yuyan Wang
- **Institution**: Duke University + Netflix
- **Date**: 2026-08-09
- **Link**: [2608.08889](https://arxiv.org/abs/2608.08889)
- **Abstract**: RLVR gains are indexed mostly on objective math tasks; this large-scale study (proprietary + open-source models, four real-world verification tasks from a production recommender platform) asks whether explicit reasoning generalizes to subjective, human-centric industry rubrics. Findings: (1) rigid, math-centric reasoning traces **actively degrade subjective verification**; (2) standard RLVR triggers **reasoning collapse** — the policy abandons deliberation for rapid heuristic guessing; (3) a **conditional length-penalized post-training** objective intertwines verification accuracy with bounded reasoning length, halting collapse; (4) a reasoning trace's efficacy is tightly coupled to its **socio-linguistic framing** — across 1,500 synthesized personas, verification accuracy swings by ~0.38 macro-F1 purely with the adopted reasoning persona. This motivates a mid-training architecture that **routes reasoning through contextually aligned personas**.
- **Key Innovation**: Documents "reasoning collapse" as a distinct RLVR failure for subjective tasks and introduces persona-conditioned reasoning routing — directly relevant to the wiki's LLM-as-judge/verifier and personalization threads (LLM-OSDA, recommendation-quality auditing).

### CoRE: Consensus Rewards via Equilibrium for Test-Time Reinforcement Learning
- **Authors**: Ambuj Mehrish, Sebastiano Vascon
- **Institution**: CVML Lab, Ca' Foscari University of Venice
- **Date**: 2026-08-10
- **Link**: [2608.09324](https://arxiv.org/abs/2608.09324)
- **Abstract**: Test-time RL derives rewards from the model's own rollouts, typically rewarding those matching a **majority vote** over N samples — which discards a correct minority answer and scores all majority-matching rollouts identically. CoRE (Consensus Rewards via Equilibrium) treats the N rollouts as a **graph** whose edges combine answer agreement, reasoning similarity, and generation confidence; **replicator dynamics** extract its dominant set, yielding a refined pseudo-label, graded per-rollout reward, and per-question cohesiveness gate. Majority voting is recovered as a special case; a block-value analysis gives a sharp threshold for when consensus recovers a correct minority against a larger wrong plurality, and confidence calibration provably lowers that threshold multiplicatively. Across 42 model–benchmark cells, CoRE improves the untrained base by +21.7 points avg (vs +20.4 for majority-vote TTRL), wins wherever agreement is contestable (margins up to +7.5), and reaches the vote baseline's plateau accuracy in 54–70% fewer steps.
- **Key Innovation**: Upgrades majority-vote self-reward from counting to graph equilibrium — "consensus, not counting" — improving the TTRL family (already in the wiki's RL-verification cluster) with graded, calibrated self-supervised rewards at zero extra rollout cost.

---

## 3. Agents, Skills & Memory

### Agentic Router: An Execution-Grounded Continual Learning Approach With Memory
- **Authors**: Yuxuan Chen, Rongpeng Li, Zhifeng Zhao, Yuntao Liu, Xing Xu, Honggang Zhang
- **Institution**: Zhejiang University + Zhejiang Lab
- **Date**: 2026-08-10
- **Link**: [2608.09184](https://arxiv.org/abs/2608.09184)
- **Abstract**: LLM agents for CLI-based network operations (SONiC) can generate plausible-but-failing commands; existing work focuses on generation or final-config correctness and ignores **execution-grounded experience**. The Agentic Router is a dual-path consequence-aware agent: it generates multiple complete actions, **predicts execution consequences**, and selects the final action by utility-and-risk-aware reranking. The proposal-side path abstracts reusable operational lessons into retrievable guidance (improving feasible-action coverage without modifying the proposal LLM); the selection-side path adapts the consequence predictor via **session-level LoRA updates on real SSH feedback**. Experiments across multi-turn SONiC sessions with different Qwen3 proposal models show improved feasible-action coverage and top-1 execution success, with the two paths complementarily improving over interaction.
- **Key Innovation**: Explicitly splits the "what could be done" (proposal coverage) and "what should be done" (consequence-aware selection) loops, each adapted with execution feedback — a networked-systems instantiation of the wiki's execution-grounded agent reliability line (LivePlan, READ, SkillTrace).

### Branch2Skill: Efficient Skill Evolution Through Reasoning Trees
- **Authors**: Yanwei Ren, Haotian Zhang, Likang Xiao, Jiaxing Huang, Jiayan Qiu, Baosheng Yu, Quan Chen, Liu Liu
- **Institution**: —
- **Date**: 2026-08-09
- **Link**: [2608.08677](https://arxiv.org/abs/2608.08677)
- **Abstract**: Skill evolution usually refines skills from *single* trajectories, where early reasoning errors propagate and force repeated rollout–diagnose–update cycles at high token cost. Branch2Skill transforms **one reasoning tree into dense supervision**: under a fixed budget it runs MCTS to get diverse trajectories, compares an elite path against sibling alternatives sharing the same prefixes to extract step-wise evidence about which reasoning patterns to retain/revise/avoid, then distills multi-step evidence into reusable skill updates. Across six reasoning + agentic benchmarks it improves performance while cutting cost — e.g. **73.2% fewer tokens than SkillOpt** with GPT-5.5 as target while achieving superior performance.
- **Key Innovation**: Reuses the *contrast structure* of a reasoning tree (elite vs siblings) as step-local supervision for skill updates — a token-efficient complement to the wiki's skill-evolution and reasoning-tree threads (STaR-style, SkillOpt, self-evolving agent harnesses).

### SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance
- **Authors**: You Lu, Xinyu Huang, Bihuan Chen, Xin Peng
- **Institution**: Fudan University (likely)
- **Date**: 2026-08-10
- **Link**: [2608.09253](https://arxiv.org/abs/2608.09253)
- **Abstract**: Even when an agent can complete a task under a skill, it fails inconsistently across similar tasks or repeated runs (deviations from the skill procedure, incorrect steps). SkillSentry is a skill-oriented runtime-assurance framework built on a new **DSL for runtime guidance**: it initializes guidance from a skill specification (extracted from the skill document) + execution experience mined from historical success/failure traces, wraps the agent loop to monitor and guide execution, and iteratively refines guidance from new traces. On 15 skills across Claude Code (Claude-Haiku-4.5/Opus-4.6) and Codex (GPT-5.2/5.4), SkillSentry improves task success rate by **24.1% on average** with lower run-to-run variability.
- **Key Innovation**: Treats skill reliability as a runtime *assurance* problem (spec + experience → live guidance), not a prompt-authoring problem — the wiki's skill-admission/execution thread (VaG, SkillAligner, SkillProx) gains a runtime-enforcement layer.

### Muscle Memory for Agents: Compile not Merely Retrieve
- **Authors**: Pouya Ghiasnezhad Omran, Soujanya Lanka, Qin Zhang, Tanya Dixit
- **Institution**: Google Cloud
- **Date**: 2026-08-10
- **Link**: [2608.08995](https://arxiv.org/abs/2608.08995)
- **Abstract**: Agent memory has converged on one pattern — store experience as text/embeddings/reflections, retrieve at inference, let a general-purpose orchestrator interpret. This paper argues that pattern is the **wrong default for personalization** and positions "Muscle Memory" — **compiling recurring user intent into purpose-built specialist agents** — as a distinct paradigm from retrieval. A four-phase pipeline (Harvest→Analyze→Augment→Evaluate) mines conversational history, separates behavioral from task patterns, and emits quality-gated executable compiled specialists with two-stage trigger matching. On 90 held-out scenarios across five user personas, the augmented assistant wins 32 of 36 fired cases (88.9% win rate) with +2.05 personalization gain and only −0.28 accuracy cost (1–4 scale).
- **Key Innovation**: Argues and demonstrates that *compilation beats retrieval* for recurring personalization workloads (eliminating the "multi-turn tax"), a deliberate contrarian position against the wiki's dominant retrieval-first agent memory line (DocMemo, TRACE-Memory).

---

## 4. KV Cache, Efficiency & Model Interfaces

### RippleKV: Cross-Layer KV Cache Allocation via Perturbation Propagation
- **Authors**: Dongjie Xu, Kai Qian, Julius, Weijie Shi, Yuxuan Sun, Minghua Tang, Fenglei Jin, Hanchi Dong
- **Institution**: —
- **Date**: 2026-08-09
- **Link**: [2608.08684](https://arxiv.org/abs/2608.08684)
- **Abstract**: Distributing a limited KV-cache budget across layers is hard; existing methods use proxies (layer depth, attention statistics, representation change) that don't measure how perturbations at each layer propagate to the output, so sensitive layers get underallocated. RippleKV estimates **output-level sensitivity per layer**: it injects norm-adaptive perturbations into each layer's value cache and measures induced KL divergence at the model output on a small calibration set; the sensitivity profile need not vary monotonically with depth. The profile is converted to layer budget multipliers via normalization + exponential mapping, with a ratio controlling allocation disparity and a final normalization preserving total budget. On LongBench, RippleKV achieves the highest average performance among evaluated KV-compression methods under matched cache budgets.
- **Key Innovation**: First cross-layer KV allocation metric based on *output-propagation of perturbations* (a "ripple" response) rather than local proxies — a principled alternative to the wiki's KV line (GraceKV, QEvict, ResKV, DistillCache).

### DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference
- **Authors**: Asaad Althoubi
- **Institution**: Oklahoma State University
- **Date**: 2026-08-09
- **Link**: [2608.08878](https://arxiv.org/abs/2608.08878)
- **Abstract**: Heuristic KV eviction (H₂O, SnapKV) relies on static attention/positional signals that miss a token's future predictive influence. DistillCache formulates eviction as a **sequential decision problem** learned with RL: a lightweight policy network consumes rich internal signals (attention stats, value norms, entropy, position) and is trained with **REINFORCE under a per-step KL-divergence reward** that preserves the full-cache output distribution. On Mistral-7B-Instruct-v0.3, DistillCache retains **94.2% of full-cache accuracy on LongBench at 25% cache budget**, beating H₂O/SnapKV by up to 2.7 points and concurrent RL methods (ForesightKV, RLKV) by up to 1.4, with up to 2.1× full-cache throughput.
- **Key Innovation**: Brings RL + distribution-preservation reward to KV eviction — learned, distribution-aware policies as a drop-in alternative to heuristics, consistent with the wiki's "learned vs heuristic cache" comparison line.

### KVDiagnosis: A Diagnostic Benchmark for KV-Cache Compression in Long-Context Language Models
- **Authors**: Chen Qiu, Ziwu Liu, Chao Fei, Guozhong Li, Panos Kalnis
- **Institution**: KAUST
- **Date**: 2026-08-10
- **Link**: [2608.09412](https://arxiv.org/abs/2608.09412)
- **Abstract**: Aggregate task scores can't say *which* correct executions fail under KV compression or why. KVDiagnosis is a diagnostic benchmark with three contributions: (1) a **25-method taxonomy** into five mechanism families linked to eight verified implementations; (2) per-method-setting C-to-W rows (FullCache-correct, compressed-wrong) so no compressor defines another's test set; (3) a common record format tying outputs to cache/likelihood/attention/decoding measurements. On Qwen3-8B, four evidence-aware workloads yield 59,800 supported compressed runs over 2,600 sources and 12,520 C-to-W rows: **63.2% have low or partial measured/projected coverage**; only 19 rows (0.2%) combine high coverage with strong likelihood drift. All ten diagnostics separate failed from successful compression (stratified AUROC 0.684–0.871); a controlled 4× evidence-attention boost repairs 29.2% of reproducible low-EAR failures vs 6.3% for a sham intervention.
- **Key Innovation**: The first *diagnostic* (failure-localizing) benchmark for KV compression, showing most compressed-wrong failures are coverage failures fixable by attention to the evidence — a measurement infrastructure counterpart to the wiki's KV methods cluster.

### Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference (KVGov)
- **Authors**: Tejasvi C. Addagada
- **Institution**: —
- **Date**: 2026-08-10
- **Link**: [2608.09225](https://arxiv.org/abs/2608.09225)
- **Abstract**: Shared KV caches in multi-tenant inference create a **timing side channel**: an adversarial tenant can reconstruct another tenant's private prompt by probing cache-hit latency (three published attacks — PROMPTPEEK, EarlyBird, InputSnatch — up to 100% success against unprotected vLLM/SGLang). KVGov is a governance layer: a **per-principal salt** σ_p = HMAC_K(secret, principal_id) seeds the block-hash chain, making cache keys cryptographically disjoint across principals (an ablation isolates this as necessary and sufficient); plus ORIGAMI, a Stackelberg water-filling audit scheduler reducing adversary expected utility by 12.6% at realistic tenant heterogeneity, and an evolutionary-stability analysis giving a 31.6% adversary-prevalence tipping point. Measured gate-verified cold/cached TTFT ratio 0.22 on Qwen2.5-7B + vLLM on A100 confirms the channel is exploitable at production scale. Injecting the salt at the *divergence* boundary (not the chain root) retains ~93% of prefix-cache benefit with no cross-principal signal.
- **Key Innovation**: The wiki's first dedicated KV-cache *security* result — proving prefix-cache isolation and cache efficiency need not conflict — a serious operational gap in the multi-tenant inference line (LLMVisor-style serving, COIN-RAG-style reuse).

### One Adapter Pair per Model: A Universal Activation Interface for Language Models
- **Authors**: Su-Hyeon Kim, Jiwan Mun, Yo-Sub Han
- **Institution**: Yonsei University (likely)
- **Date**: 2026-08-10
- **Link**: [2608.09521](https://arxiv.org/abs/2608.09521)
- **Abstract**: Activation-based tools (probes, SAEs, natural-language interpreters) are tied to one model's native hidden space and must be rebuilt for every new model. The **Universal Activation Bus** learns a shared dense space from a small set of source models plus **one lightweight linear encoder–decoder adapter pair per model**; after source training the interface is frozen and a new model joins by fitting only its adapter pair on unlabeled matched text. Across five models, semantically related texts form consistent neighborhoods, onboarded models reuse existing probes/SAE features/NLAs without retraining, and an intermediate activation from one model can be consumed by another model's frozen upper layers to produce predictions.
- **Key Innovation**: A model-wise "activation contract" making interpretability/control tools portable across LLMs — infrastructure for the wiki's mechanistic-interpretability and activation-steering threads (LoRA-based adaptation, steering-vector work).

---

## 5. Sequential Modeling & Time Series

### End-to-End Neural Decomposition with Koopman Operators for Time-Series Forecasting (NDKoop)
- **Authors**: De-Yan Lu, Xugang Lu, Yu Tsao, Jian-Jiun Ding
- **Institution**: National Taiwan University + Academia Sinica (likely)
- **Date**: 2026-08-09
- **Link**: [2608.08788](https://arxiv.org/abs/2608.08788)
- **Abstract**: Koopman theory linearizes nonlinear dynamics by lifting into a space with a linear time-invariant operator, but real signals are non-stationary and frequency-dependent. NDKoop is an **end-to-end architecture integrating a learnable signal-decomposition module with both frequency-independent and frequency-dependent Koopman networks**: the signal is split into a frequency-independent *trend* component and a frequency-dependent *periodic* component, each governed by its own learned Koopman operator. The paper claims the first unified neural framework jointly realizing end-to-end Koopman modeling and signal decomposition, with improved accuracy when perfect linearization is unattainable across several forecasting benchmarks.
- **Key Innovation**: Marries interpretable signal decomposition (trend/periodic) with learned Koopman linearization inside a single end-to-end model — a hybrid-theory entry for the wiki's time-series cluster that complements the retrieval/alignment-driven baselines (KReF, GLIDE, DPWM).

### Efficient Test-Time Scaling for LLM-based Time Series Forecasting (SCALER)
- **Authors**: Xuan-May Le, Minh-Tuan Tran, Ling Luo, Uwe Aickelin, Dinh Phung, Trung Le
- **Institution**: University of Melbourne + Monash University
- **Date**: 2026-08-09
- **Link**: [2608.08675](https://arxiv.org/abs/2608.08675)
- **Abstract**: LLM forecasters gain accuracy from test-time scaling (iterative refinement) but it's computationally expensive and prone to **global-shape mismatch** as the horizon extends. SCALER is a coarse-to-fine framework: a lightweight Transformer models long-term *shape* and predicts a coarse representation of future dynamics; that predicted shape guides an LLM through iterative coarse-to-fine **residual token refinement** using far fewer tokens per step, avoiding long description prompts and reward-model-based selection. SCALER outperforms strong baselines on long-term, short-term, and zero-shot forecasting while significantly cutting the inference cost of scaled-LLM forecasting.
- **Key Innovation**: Brings the "predict the shape, then refine residuals" divide-and-conquer to LLM time-series test-time scaling — an efficiency result for the wiki's TS cluster that reduces reliance on long prompts and reward models.

### Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: A Comprehensive Ablation Study on High-Frequency Stock Prediction
- **Authors**: Kasun Dewage, Suranadi De Silva, Shankhadeep Mondal
- **Institution**: —
- **Date**: 2026-08-09
- **Link**: [2608.08825](https://arxiv.org/abs/2608.08825)
- **Abstract**: Time-series foundation models (TimesFM, 200M) underperform on specialized domains like high-frequency finance. This study adapts frozen TimesFM to stock-return prediction in the volatile opening hour with hybrid neural-classical correction, comparing AttnCorrect (multi-head self-attention, ~471K params) vs GatedLinear (low-rank bilinear + gating, ~49K params), each augmented with **Random Forest residual learning**, across 10 tech stocks (NVDA/MSFT/AAPL/…, 2M points). Key findings: (1) hybrid correction reaches 0.597 pooled correlation, 6.4× mean per-day correlation improvement over frozen TimesFM; (2) **classical residual learning (RF) provides the largest single-component contribution**, matching or exceeding the neural component; (3) simpler neural architectures beat complex ones when classical residual learning is removed; (4) self-attention is the largest neural-only contributor. GatedLinear+RF is best overall with 9× fewer neural parameters than AttnCorrect+RF.
- **Key Innovation**: An honest ablation showing that for financial forecasting, **classical residual correction often matters more than the neural module** — strong support for the wiki's "simple/classical baselines beat fancy modules" thesis in time series (Align-RAG, KReF line).

### MixFormer: Linear Transformer with Mixture of Memory Experts
- **Authors**: Yu Guo, Lei Duan
- **Institution**: Sichuan University
- **Date**: 2026-08-10
- **Link**: [2608.09468](https://arxiv.org/abs/2608.09468)
- **Abstract**: SSMs/linear transformers suffer from limited input adaptivity and constrained memory capacity for ultra-long sequences. MixFormer integrates a **Mixture-of-Memory-Experts (MoE)** mechanism into a linear transformer: differentiated memory states across collaborating memory experts, plus a **Time-Aware Linear Attention (TALA)** using learnable exponential-decay functions and positional biases to dynamically update memory, selectively reinforcing important history while mitigating memory dilution. It reports significant gains on long-sequence text and image generation tasks.
- **Key Innovation**: Treats *memory states* (not feedforward experts) as the MoE axis for linear attention — a novel hybrid for the wiki's attention/SSM/linear-transformer line (Gated DeltaNet, MixFormer-style sequence models).

---

## 6. Recommendation, Advertising & Ranking

### TSPORec: Token Selection via Preference Optimization for LLM-Based Sequential Recommendation
- **Authors**: Wenqiao Zhu, Chao Xu, Haipang Wu, Ji Liu
- **Institution**: —
- **Date**: 2026-08-10
- **Link**: [2608.09605](https://arxiv.org/abs/2608.09605)
- **Abstract**: LLM-based sequential recommenders incur high inference cost; to cut it, many methods use only the first few tokens of item descriptions, discarding valuable full-text information. TSPORec **pinpoints informative tokens across the entire textual content** via a three-stage selection pipeline plus a novel **proxy reward**, then trains with preference optimization. Across two models and datasets it reports up to **31.25% performance gain and up to 63.4% efficiency gain** over six baselines.
- **Key Innovation**: Token-level selection for LLM sequential recommendation — preserving full-text signal at low inference cost, directly relevant to the wiki's LLM-recommendation and generative-rec cost/quality threads (TM20K sequence distillation, TSPORec-adjacent).

### MetaStrategy: Generative Ranking with Executable LLM Strategies
- **Authors**: Chengyu Lai, Jiuning Lin, Zhibo Xiao, Xiaodong Zhu, Ruiquan Lan, Bin Zhang, Zihong Huang, Wendong Zhang, Chuxin Chen, Yinjiang Cai, Shuai Zhong, Lingqing Zhang
- **Institution**: Taobao & Tmall Group (Alibaba) + Wuhan University + University of Hong Kong + University of Cambridge
- **Date**: 2026-08-10
- **Link**: [2608.09440](https://arxiv.org/abs/2608.09440)
- **Abstract**: Industrial recommenders rank heterogeneous content under coupled user/business/commercial/experience objectives; generative-ranking methods that emit item sequences are hard to integrate with mature predictive models and field-level guardrails. MetaStrategy instead generates a **structured, executable ranking strategy**: an LLM policy emits a typed JSON bundle (objective weights, content/category preferences, experience constraints, position policies), validated and compiled into an isolated Generator that competes atomically with incumbents under a list-level Evaluator (Generator–Evaluator architecture). The policy trains in a **production-path replay environment** (re-executes logged requests offline) with selection, relative-rank, and baseline-lift rewards, a self-competitive curriculum, and Evaluator-routed on-policy distillation (4B Teachers → 0.8B Student). Deployed in **Taobao Homepage "Guess You Like"** with diff-triggered nearline generation and no RT increase: a seven-day user-randomized A/B test wins 27.93% of treatment-side GE calls and improves click PV +2.11%, IPV +3.12%, transaction amount +2.83%.
- **Key Innovation**: Positions generative ranking as a **strategy-control plane** (JSON policy → executable constraints) rather than sequence generation — a production-verified integration story for the wiki's generative-ranking and industrial-rec lines (Gryphon-v2, OneRanker, IntHQ), with transparent online A/B numbers.

### UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models
- **Authors**: Lei Xin, Bin Gu, Peize Li, Zitong Wang, Jianbo Zhao, Changjiang Jiang, Yanyue Xie, Chao Huang, Xuyang Zhao, Zunhai Su, Fanhu Zeng, Zhenglun Kong
- **Institution**: Kuaishou Technology + ByteDance + Alibaba Ant Group + Wuhan University + University of Hong Kong + Hohai University
- **Date**: 2026-08-09
- **Link**: [2608.08627](https://arxiv.org/abs/2608.08627)
- **Abstract**: Sparse MoE layers expand recommendation capacity but a trained checkpoint still stores/routes over its full expert bank. UniMoMo is a **post-training compression framework framed as constrained graph coarsening**: experts are grouped by *functional* similarity measured on an unlabeled calibration set (how similarly they respond to shared recommendation states), with a **layer-adaptive protection mechanism** restricting merging of high-traffic experts based on routing exposure. On Amazon Beauty, KuaiRec, and TenRec with 2/4/6 MoE blocks, four-expert checkpoints retain 99.92–102.30% of source NDCG@10 (5-run mean) with 1.28–1.63× A100 speedups; an aggressive 2-expert/top-1 point reaches 98.36–104.24% with 1.47–2.21× speedups.
- **Key Innovation**: Converts trained recommendation MoEs into smaller serving-time MoEs without an online compression module — functional-similarity merging (not parameter distance) as the grouping criterion, with routing-exposure-aware protection. Relevant to the wiki's MoE-efficiency and industrial-rec threads (HD-Rec quantization, expert merging).

### From Product Search to Preference Articulation: The Economics of Agentic Commerce
- **Authors**: Lingxiu Dong, Kaiwen Luo, Fasheng Xu
- **Institution**: US business schools (WashU Olin et al., likely)
- **Date**: 2026-08-09
- **Link**: [2608.08395](https://arxiv.org/abs/2608.08395)
- **Abstract**: A model where manual search accurately evaluates a limited product set while **agentic search screens a broad catalog through noisy preference representations**, with finite consumer attention split between inspection and agent-refinement depth. Findings: (1) **manual search collapses beyond a finite preference-complexity threshold** (inspection ceases, platform revenue → 0), while agentic search avoids the collapse and stays revenue-positive; (2) when manual inspection is cheap, agentic search becomes **revenue-superior before consumers voluntarily adopt it** — an adoption lag; (3) platforms may assign **lower fidelity to high-attention consumers** because they can offset noise through more refinement — an inverted fidelity allocation. Conclusion: agentic commerce shifts scarcity from product inspection to **preference articulation**, making consumers' willingness/ability to interact central to platform design.
- **Key Innovation**: The wiki's advertising/auction/market-design thread gains its first *agentic-commerce economics* model — formalizing when delegation to AI shoppers wins, why adoption lags, and how platform fidelity should be allocated. Complements LLM-OSDA (ad surfaces) and Economics-of-Attention work.

---

## 7. Games & Game Theory

### ICM Out! Better Tournament Strategy from Computed Continuations, vs. Solvers and LLMs
- **Authors**: Boning Li, Longbo Huang
- **Institution**: IIIS, Tsinghua University
- **Date**: 2026-08-10
- **Link**: [2608.09586](https://arxiv.org/abs/2608.09586)
- **Abstract**: The Independent Chip Model (ICM) converts tournament chips into prize equity using only stack sizes — omitting action order, blind obligations, seat rotation, and big-stack elimination pressure. Strategic-Continuation Optimization (SCO) enumerates current-hand outcomes, maps them to successor states, **prices those states with continuation values computed from the finite tournament model**, and freezes the resulting current-hand policy. In a three-player jam/fold tournament with a $1M prize pool, analytic ICM shows $9,036 mean absolute value error across 2,838 state–seat entries and moves jam frequency by an average of **14.08%** vs the fixed-ICM comparison; SCO earns **$214.33 more prize equity per hand** on average and is favored in 2,433 of 2,838 matched units. The ordering survives replacing the solver-built opponent with two LLMs and a family of non-modeling threshold players.
- **Key Innovation**: Directly measures *when ICM becomes an inadequate objective* for tournament strategy and replaces its successor-state pricing with exact computed continuations — a clean value-to-policy-to-cost chain for the wiki's game-strategy/GT cluster (solver-guided equilibrium line, Aug 7 MDT).

### Algorithmic Asymmetry in Zero-Sum Games: Unilateral Recovery of Fast Convergence Against a Slow Opponent
- **Authors**: James P. Bailey, Soham Das
- **Institution**: Rensselaer Polytechnic Institute + University of Tennessee
- **Date**: 2026-08-10
- **Link**: [2608.09780](https://arxiv.org/abs/2608.09780)
- **Abstract**: Learning dynamics in zero-sum games are usually analyzed under algorithmic symmetry (both agents use the same update family), at odds with reality — competitors need not coordinate on algorithm selection. When one agent is fixed to vanilla gradient descent (whose standard analysis certifies at best O(1/√T) ergodic convergence), the paper shows the **slow rate is not intrinsic**: the opposing agent can use **Alternating Optimistic Gradient Descent (AOGD)** so the joint dynamics simulate alternating GD on the even iterates, driving the time-average to Nash equilibrium at **O(1/T)**. Fast convergence thus needs no coordinated algorithm selection — one agent compensates for a slower opponent.
- **Key Innovation**: Establishes algorithmic asymmetry as a design lens for multiagent optimization — unilateral recovery of fast convergence — a theory entry for the wiki's learning-in-games thread (mean-payoff bidding games, EFX/fair-division line, regret-based agent eval).

### Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics
- **Authors**: Yen-Shan Chen, Yu Chian Duan, Chih-En Kuo, Jian-Bin Wu, Yun-Nung Chen
- **Institution**: National Taiwan University + CyCraft AI Lab
- **Date**: 2026-08-10
- **Link**: [2608.09638](https://arxiv.org/abs/2608.09638)
- **Abstract**: ToM evaluations are either static (oversimplify mental-state reasoning) or interactive (limited diagnostic insight). Avalon-ToM-Bench operationalizes ToM through the **asymmetric-information mechanics of The Resistance: Avalon**, decomposing it into a 2×2 taxonomy (epistemic vs motivational × inference vs action) with human-crafted, perspective-constrained queries — no end-to-end gameplay needed. Benchmarking 28 LLMs yields three insights: (1) **Reasoning, not knowledge** — models understand game rules but have markedly weaker ToM; (2) **Expression, not representation** — linear probes recover 77–82% of correct mental-state inferences from hidden states while models' own CoT only reaches 62–70%, showing models represent ToM but fail to express it; (3) **Policy, not deliberation** — dedicated reasoning training improves ToM substantially (+11.0) while test-time CoT barely helps (+1.1), suggesting robust ToM depends on a learned reasoning policy.
- **Key Innovation**: A fine-grained, mechanics-grounded ToM benchmark isolating *which* ToM component fails — and mechanistic evidence that failures are expression/policy problems, not representation gaps. Directly relevant to the wiki's game-rl/multi-agent alignment and LLM-persona threads (Deal Me Maybe negotiation, PHASE-Tree).

---

## 8. Interpretability & Safety

### Multimodal Model Diffing for Feature Discovery and Control (MMDiff)
- **Authors**: Hunar Batra, Lachin Naghashyar, Ashkan Khakzar, Philip Torr, Christian Schroeder de Witt, Constantin Venhoff, Ronald Clark
- **Institution**: University of Oxford + Microsoft
- **Date**: 2026-08-10
- **Link**: [2608.09928](https://arxiv.org/abs/2608.09928)
- **Abstract**: Hidden states decomposed into SAE feature directions don't isolate *which* features multimodal training changed, and aren't directly useful for control. MMDiff trains **multimodal SAEs** and turns them into feature-level interfaces: (i) feature isolation by diffing a base-LM SAE against its multimodal-adapted counterpart; (ii) task-specific detection via per-token contrastive firing analysis; (iii) **feature-level control** by causally removing or steering discovered directions. On LLaVA-MORE, PaliGemma 2, and InternVL3.5, removal selectively degrades target behaviors by ~12% on spatial tasks and ~17% on OCR, cuts multimodal safety attack success by 24%, with no VQA impact; steering improves spatial/OCR accuracy by +3.6%/+1.8% over single-layer steering.
- **Key Innovation**: The first *diffing* methodology for multimodal SAEs — model-difference-as-discovery — giving causal feature-level control of multimodal behavior, a strong addition to the wiki's mechanistic-interpretability and safety-threading work.

### Measuring the Wrong Thing: Internal Harmfulness Scores Anti-Rank Successful Jailbreaks
- **Authors**: Mingyu Luo, Ming Deng, Zilang Qiu, Yiming Cheng, Ci Tao, Xue Tan, Sijin Sun, Yangfu Li, Ping Chen, Jun Dai, Xiaoyan Sun
- **Institution**: Fudan University + Shanghai University + Tsinghua University + A*STAR
- **Date**: 2026-08-10
- **Link**: [2608.09624](https://arxiv.org/abs/2608.09624)
- **Abstract**: Internal safety scores judge a prompt before generation and are validated by harmful-vs-benign separation — but **harmful intent is a property of the prompt, while jailbreak success is an outcome produced later by a target model, decoding policy, and judge**. The paper introduces **Active Attention Probing** (fixed, content-independent measurement coordinates, since wrapper-based attention measurements change both the content and the readout location) and pairs each base goal with plain/wrapped versions, generating real completions. On Llama, wrapping raises harmful generation from 0.05 to 0.27 while harmful-intent AUROC falls 0.936→0.803 — attacks grow more dangerous while prompts look *safer* to the score. Among wrapped harmful prompts, outcome AUROC is **0.220** — successful attacks rank *below* failed ones. The reversal persists across three target models, seven attack families, two judges, and rare-token/passive/detector-derived channels; distribution shift degrades calibration before ranking.
- **Key Innovation**: A falsifying audit showing internal harmfulness scores can **anti-rank** successful jailbreaks — the score measures the wrong quantity (prompt intent, not outcome). Directly relevant to the wiki's safety-evaluation line (StepJack indirect injection, jailbreak defenses, SABRE priors).

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **On-policy self-distillation becomes the dominant post-training axis — and immediately gets a theoretical corrective** | Five papers in one window push OPSD (complete-trajectory hindsight in PAST, moving-target stabilization in SR-OPSD, skill-conditioned teachers in SKALD) while "Privileged Likelihood" delivers a rigorous negative result (token likelihood ≠ outcome credit, AUC≈0.505). The cluster is now large enough to demand its own measurement standards | PAST, SR-OPSD, SKALD, Privileged Likelihood, SoftmaxGRPO |
| **KV-cache research expands from compression to security and diagnosis** | KVGov shows prefix-cache sharing creates a timing side channel exploitable at production scale (salt-based isolation retains ~93% of reuse benefit); KVDiagnosis shows 63% of compressed-wrong failures are coverage failures fixable by attention; RippleKV and DistillCache push allocation/eviction toward output-propagation and learned policies | KVGov, KVDiagnosis, RippleKV, DistillCache |
| **Verifier-free test-time scaling gets a theory of confidence trajectories** | Consilience shows uniformly high confidence = failed exploration (confidently wrong answers) and selects on low→high confidence *asymmetry*; CoRE upgrades majority-vote self-rewards to graph-equilibrium consensus with graded rewards; TTA shows input-side diversity converts compute into accuracy ~1.8× more efficiently than output-side at matched budget | Consilience, CoRE, TTA |
| **Reasoning-style mismatch is a measurable failure mode** | Subjective-task RLVR triggers "reasoning collapse" (policy abandons deliberation); verification accuracy swings ~0.38 macro-F1 with the adopted reasoning persona, motivating persona-conditioned routing — an architectural blueprint for recommender verification | Subjective RLVR (Duke/Netflix), Avalon-ToM-Bench (expression-not-representation, policy-not-deliberation) |
| **Generative ranking converges on "executable strategy" rather than item sequences** | MetaStrategy generates a typed JSON strategy bundle compiled into a Generator within a GE architecture, A/B-winning +2.11% click PV / +2.83% GMV at Taobao with no RT increase; UniMoMo compresses recommendation MoEs via functional-similarity expert merging (up to 2.21× speedup at ≤2% NDCG loss) | MetaStrategy, UniMoMo, TSPORec |
| **Classical methods keep beating/matching fancy modules in specialized forecasting** | Hybrid neural-classical correction of frozen TimesFM finds Random Forest residual learning is the largest single contributor and GatedLinear+RF beats a 9× larger attention module; SCALER cuts scaled-LLM forecasting cost with coarse-shape guidance; NDKoop adds interpretable Koopman decomposition — reinforcing the wiki's "simple baselines" thesis in TS | Hybrid Neural-Classical, SCALER, NDKoop, MixFormer |
| **Agent memory gets a compile-not-retrieve contrarian** | Muscle Memory argues compiling recurring intent into specialist agents beats retrieval for personalization (88.9% win rate when fired) — a direct challenge to the retrieval-first memory consensus; Branch2Skill and SkillSentry attack skill evolution cost and runtime reliability respectively | Muscle Memory, Branch2Skill, SkillSentry, Agentic Router |
| **Game-theory and mechanism-design work continues at the theory/economics edge** | ICM Out quantifies when ICM value-pricing breaks ($9K value error → 14% jam-frequency shifts) and SCO recovers exact continuation pricing; Algorithmic Asymmetry shows unilateral recovery of O(1/T) convergence in zero-sum games; Avalon-ToM-Bench isolates ToM failure modes in asymmetric games | ICM Out, Algorithmic Asymmetry, Avalon-ToM-Bench |

---

## Key Takeaways

1. **The OPSD cluster has matured into a full research subfield — with an internal critic.** Aug 7–11 delivered supervision-free (U-OPSD), gradient-free (Hyper-ES), warm-up (Simple-OPD), trajectory-hindsight (PAST), skill-conditioned (SKALD), and stabilizing (SR-OPSD) variants — but "Privileged Likelihood" (Salesforce) shows token-level credit signals can be near-chance (AUC 0.505) without careful validation of score meaning, feedback construction, and loss behavior. Watch for the cluster to consolidate behind measurement standards rather than new recipes.
2. **KV-cache management has entered its "systems-security + diagnostics" era.** Compression methods keep improving (RippleKV's output-propagation allocation, DistillCache's RL eviction), but the two most consequential papers this window are KVDiagnosis (which failures are cache-caused, and how to fix them with evidence attention) and KVGov (multi-tenant timing side-channels at 100% attack success — with a salt-boundary fix that keeps ~93% of reuse). Multi-tenant inference security should be on every serving stack's risk list.
3. **Verifier-free reasoning is being re-theorized around confidence *dynamics*.** Consilience's low→high confidence-asymmetry criterion and CoRE's equilibrium consensus both argue that *how* confidence/reward unfolds over the rollout group matters more than final values — converging with the wiki's evidence that simple vote/confidence heuristics are leaving performance on the table.
4. **Subjective-verification RLVR has a named failure: reasoning collapse.** Duke/Netflix's production study and NTU's Avalon-ToM-Bench independently converge on the same pattern: models can represent the right answer but fail to express it under the wrong reasoning policy/persona — motivating length- and persona-conditioned training and routing. A key caveat for any "RLVR everywhere" strategy.
5. **Generative ranking is being productionized as a control plane, and agentic commerce is becoming a formal economics topic.** MetaStrategy's executable-JSON-strategy ranking (deployed, +2.83% GMV) is the strongest industrial evidence this window that generative ranking can integrate with guardrails and legacy stacks; "Economics of Agentic Commerce" gives the field its first formal model of when delegation to AI shoppers wins and why platforms may under-invest in fidelity.
6. **Games were mostly claimed by today's game-rl-daily** (19 papers); this digest adds the GT/econ edge (ICM Out, Algorithmic Asymmetry, Avalon-ToM-Bench) with zero overlap. No pure CTR paper surfaced in the cs.LG/cs.CL/cs.GT remainder of this window.

> ⚠️ Note on sourcing: this digest curates the **fresh Aug 9–10, 2026 arXiv submission window** (IDs ~2608.08382–2608.09930), retrieved via the arXiv API (`submittedDate` window) ahead of the Tue Aug 11 announcement (~20:00 ET). All 31 papers are **grep-verified absent from the entire wiki** — zero overlap with today's [paper-check](../2026-08-11/arxiv-paper-check.md), [game-rl-daily](../2026-08-11/game-rl-daily.md), [conference-digest](../2026-08-11/conference-digest.md), or any prior digest. Institutions marked "(likely)" are inferred from author affiliations on the arXiv HTML pages, not always the arXiv record; "—" means not identified.
