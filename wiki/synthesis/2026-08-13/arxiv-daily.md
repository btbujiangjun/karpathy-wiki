---
title: "arXiv Daily Digest — 2026-08-13"
type: synthesis
created: 2026-08-13
updated: 2026-08-13
sources: [arxiv-cs.AI, arxiv-cs.LG, arxiv-cs.CL, arxiv-cs.IR, arxiv-cs.GT, arxiv-cs.MA, econ.TH, stat.ML]
tags: [arxiv, llm, on-policy-distillation, grpo, rollout-rl, reward-hacking, reasoning, test-time-scaling, model-merging, personalization, agents, skills, agent-memory, recommendation, generative-recommendation, sequential-recommendation, ctr, uplift, generative-retrieval, time-series, finance, kv-cache, position-independent-caching, hybrid-attention, massive-activations, games, game-theory, mechanism-design, fair-division, world-models, safety, alignment, unlearning, interpretability, daily-digest]
---

# arXiv Daily Digest — 2026-08-13

> **Batch note:** Today's digest covers the **Thu Aug 13, 2026 announced window — the Wed Aug 12 submission wave (IDs ~2608.11207–2608.12307)**, harvested from the `/list/{cat}/recent` pages for cs.AI (211), cs.LG (182), cs.CL (92), cs.IR (16), cs.GT (5), cs.MA (18), econ.TH (5), stat.ML (11) — **540 entries / 380 unique IDs** — and curated into **37 papers, all grep-verified absent from the entire wiki** (zero overlap with yesterday's [arxiv-daily](../2026-08-12/arxiv-daily.md), [game-rl-daily](../2026-08-12/game-rl-daily.md), or any prior digest). This is the first 08-13 page; the same-day arXiv stream is otherwise only partially claimed (the 08-12 digests stopped at ~2608.11208, so this window's entire ~2608.112xx–2608.123xx span is fresh). Signature themes of this window: **OPD/RL post-training gets a wave of diagnosis-and-constrain results** (GCPO subspace geometry, PAIR U-statistic rollout allocation, REOPD reliability-adaptive extrapolation, "illusory distillation" critique, Rubric Dropout), **agent memory and skills come under formalization and stress-testing** (formal memory basis/span/optimality, failure-aware editable memory, skill-induced failures), **CIKM 2026 recommendation is heavy on semantic-ID generative rec and relation recovery** (HCGRec, PRISM, GALLM), and **efficiency work pushes position-independent caching into hybrid LLMs and visual RAG** (LinearKV, QV-PIC).

---

## 1. LLM Post-Training, Rollout RL & On-Policy Distillation

### GCPO: Diagnosing and Constraining Subspace Geometry in Rollout RL for LLMs
- **Authors**: Kai Yang, Jingwei Xu, Wanyu Wang, Kai-Yuan Guo, Zhenbo Yu, Yi Wang, Yu Qiao
- **Institution**: SIAT/CAS + SJTU + Shanghai AI Lab (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11674](https://arxiv.org/abs/2608.11674)
- **Abstract**: On-policy rollout methods such as GRPO central to LLM post-training frequently suffer training instabilities, cross-task capability degradation, and response-length inflation. The paper introduces **Principal-Subspace Overlap**, a dimension-corrected measure of individual rollout updates relative to the dominant singular subspaces of pretrained weights — transient spikes in overlap often precede performance degradation despite low average overlap. **GCPO** applies hard bilateral orthogonal projections constraining updates to the complementary subspaces, preventing excursions by construction. On math reasoning, code generation, and tool use with Qwen3-8B and GLM4-9B, GCPO outperforms GRPO and recent variants (incl. DAPO, GSPO) by up to 27.69 pts over base and 2.37 over the strongest baseline, while preserving general capability, eliminating response-length inflation, and stabilizing entropy.
- **Key Innovation**: A diagnostic (subspace-overlap spikes as early-warning) plus a construction (orthogonal-projection constraint) for stable rollout RL — extends the wiki's GRPO-stability line (SoftmaxGRPO, DAPO variants).

### REOPD: Reliability-Adaptive Reward Extrapolation for On-Policy Distillation
- **Authors**: Yang Sun, Lichao Ma, Houyuan Qin, Yuxin Liu, Hanyang Lu, Yao Zhu, Pinlong Cai, Guohang Yan
- **Institution**: Industry (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11698](https://arxiv.org/abs/2608.11698)
- **Abstract**: Reward-extrapolation OPD methods (e.g. ExOPD) amplify the teacher-reference log-likelihood ratio to move beyond direct imitation, but apply a single global coefficient λ to every token — driving reward hacking on extreme peaks and requiring domain-dependent λ sweeps. **REOPD** combines a token-level compatibility weight with a batch-level adaptive budget into a token-wise coefficient λ_b,t = 1 + γ_b·q_t that preserves teacher alignment while selectively extrapolating along reliable teacher-reference directions. No verifier, reward model, value model, or extra rollout beyond standard OPD. REOPD beats G-OPD on single-teacher math and on both domains in multi-teacher settings, matching G-OPD on single-teacher code.
- **Key Innovation**: Per-token reliability-gated reward extrapolation — a token-level answer to the global-λ instability of the wiki's ExOPD/OPD-reward line.

### PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR
- **Authors**: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
- **Institution**: — (likely industry)
- **Date**: 2026-08-12
- **Link**: [2608.11368](https://arxiv.org/abs/2608.11368)
- **Abstract**: RLVR allocators assign compute budgets by *pointwise* difficulty/utility, but the paper identifies a statistical mismatch: the unclipped leave-one-out group-relative score gradient is a **second-order U-statistic over pairs of rollouts**, not a sum of independent point contributions — completing one rollout reveals contrast with every other, and adaptive endpoint selection changes which pair terms are observable. **PAIR** treats rollout prefixes as vertices and pair-gradient terms as edges of a *contrast graph*: a prefix-only predictor estimates correctness and remaining token cost, a convex design chooses positive continuation probabilities under a suffix-token budget, and each edge is inverse-weighted by its logged joint inclusion probability. The estimator is design-unbiased for the complete candidate-pair gradient. On compute-matched Qwen3-1.7B/4B RLVR, PAIR gains +1.2/+1.4 accuracy over the strongest pointwise allocator while using 51–52% fewer generated tokens than full-group GRPO; a frozen-population audit confirms unweighted adaptive selection is biased.
- **Key Innovation**: Reformulates rollout allocation as a pair-contrast (U-statistic) estimation problem with an unbiased design-weighted estimator — a statistics-first contribution to the wiki's rollout-allocation cluster (SARA, TAPO).

### Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling
- **Authors**: Xinmu Ge, Zizhuo Zhang, Yu Huang, Jianing Zhu, Lin Yuan, Wanli Gu, Weichang Wu, Weiran Huang, Xiaolu Zhang, Bo Han, Jun Zhou, Jiangchao Yao
- **Institution**: SJTU + Ant Group + Huawei (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11829](https://arxiv.org/abs/2608.11829)
- **Abstract**: OPD is commonly believed to distill knowledge from a stronger teacher, expanding the student's reasoning capability. Varying the sampling budget K and evaluating with pass@K and avg@K across several OPD variants, the paper finds OPD-trained models **maintain superior avg@K across budgets while pass@K advantage shifts back to the pre-OPD base as K grows** — i.e. OPD primarily improves *sampling efficiency* rather than expanding the capability boundary. pass@K dynamics across training show a progressive shift toward strong small-K performance at the expense of the large-K boundary; a problem-level pass@1024 solvability analysis shows OPD makes more previously-solvable problems unsolvable than vice versa.
- **Key Innovation**: A test-time-scaling perspective reframing OPD gains as "illusory distillation" (efficiency, not new capability) — directly qualifies the wiki's OPD-capability narrative and pairs with the wiki's pass@K/avg@K evaluation line.

### Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL
- **Authors**: Minglai Yang, Xinyu Guo, Utkarsh Tyagi, Mian Zhang, Razvan Dumitru, Sunjie Hou, Yunzhong He, Daniel Yue Zhang, Ying Liu
- **Institution**: — (industry)
- **Date**: 2026-08-12
- **Link**: [2608.11669](https://arxiv.org/abs/2608.11669)
- **Abstract**: RL against LLM-judge-graded rubrics trains to a fixed proxy of quality; a policy trained long enough exploits the proxy gap. Training Qwen3-8B with GRPO on medical and science rubrics, the paper measures the training judge's score rising while a stronger *gold* judge's OOD score peaks and then falls (by 3 pts on HealthBench-Hard, 22 pts on ResearchQA) — reward hacking, not judge noise (a fixed-bias judge would shift, not bend, the curve). **Rubric Dropout** randomly drops a subset of rubric criteria per step before computing the reward (dropped subset shared within a rollout group so group-relative advantages stay comparable; evaluation always uses the full rubric). Dropout at 30–50% raises OOD gold score at every matched checkpoint (+1–2 pts HealthBench-Hard, +6–7 pts ResearchQA), lowers hacking measures, costs nothing in domain — while reweighting criteria by training usefulness performs *worse than no intervention*.
- **Key Innovation**: A one-line dropout fix for judge-proxy reward hacking, with explicit measurement of the training-gold score divergence — relevant to the wiki's reward-hacking and rubric-judge threads (CalibratedRubric).

---

## 2. Reasoning, Self-Correction & Test-Time Scaling

### Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs (SFS-DPO)
- **Authors**: Vu Duc Anh, Nhat M. Hoang, Do Xuan Long, Cong-Duy Nguyen, Ponhvoan Srey, Luu Anh Tuan
- **Institution**: Nanyang Technological University, Singapore (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11573](https://arxiv.org/abs/2608.11573)
- **Abstract**: Self-correction (verify + fix one's own mistakes) remains hard for LLMs. **SFS-DPO** is a two-stage RL framework for step-level self-verification and correction: stage one strengthens step-level reasoning via step-level preference optimization; stage two explicitly trains models to self-verify and self-correct. A teacher-assisted variant **SFS-DPO-R** adds explanatory rationales for error verification as stronger corrective signals. In-domain and OOD evaluations across multiple LLMs show consistent wins over prior step-level training baselines, with improved self-correction frequency and effectiveness.
- **Key Innovation**: Step-level verifier/corrector training as two explicit stages with rationale augmentation — a complement to the wiki's self-correction and process-supervision lines.

### AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses
- **Authors**: Cheng Qian, Wenting Zhao, Liangwei Yang, Heng Wang, Jielin Qiu, Heng Ji, Silvio Savarese, Huan Wang, Shelby Heinecke
- **Institution**: UIUC + Salesforce AI Research (likely)
- **Date**: 2026-08-12
- **Link**: [2608.12307](https://arxiv.org/abs/2608.12307)
- **Abstract**: Distillation usually transfers capabilities by updating parameters (teacher forcing, on-policy distillation). This paper asks whether transfer can happen **at test time**: a stronger *builder* model constructs inference-time harnesses that let a weaker target solve tasks more reliably with zero parameter updates. On four Theory-of-Mind benchmarks, builders use 5% of data to iteratively refine a harness; results nearly double average target performance (0.49 → 0.91). Gains come primarily from **offloading unstable reasoning into deterministic code, benchmark-specific routing, and strict answer-format enforcement** — not from more extensive reasoning or sampling. Builder reasoning effort monotonically improves harness quality; platform effects are modest; weaker targets gain most.
- **Key Innovation**: Strong-to-weak capability transfer as inference-time harness engineering rather than weight transfer — a test-time complement to the wiki's distillation/OPD and scaffolding lines.

### Small-Scale Experiments: Are We There Yet?
- **Authors**: Nicholas Lourie, Kyunghyun Cho, Karen Ullrich, Sanae Lotfi
- **Institution**: NYU + MIT + Meta (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11859](https://arxiv.org/abs/2608.11859)
- **Abstract**: Scaling laws promised cost-effective experiments but have proven unreliable at small scales (4M+ params), leading many to conclude large models are unavoidable. This paper shows the confounding factor is **hyperparameters**: small models are highly sensitive, but hyperparameter sensitivity fades with scale; scaling laws only emerge on the fully-tuned frontier. As scale increases the hyperparameter loss surface becomes *lower dimensional*, explaining why tuning gets easier. Synthesizing these insights, the authors develop a model-centric research methodology and recover the large-scale "pre-normalization works better as models grow" result from small-scale experiments alone.
- **Key Innovation**: Rehabilitates small-scale experimentation with a hyperparameter-focused methodology — measurement hygiene for the wiki's scaling-law and model-selection threads.

---

## 3. Model Editing, Merging & Personalization

### Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport
- **Authors**: Bohan Zhang, Anqi Ni, Yixin Wang, Paramveer S. Dhillon
- **Institution**: University of Michigan + UMass Amherst (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11342](https://arxiv.org/abs/2608.11342)
- **Abstract**: SFT for personalization is costly when every author needs separate weight access, optimization, storage, and retraining. **WFT** is a training-free decoding-time method approximating the distributional effect of SFT without weight updates: it computes supervised residuals on an author's training sequence and transports them to the current prompt via a **cross-prefix transport operator** estimated from dropout-induced cross-covariance — replacing gradient updates with logit-space corrections. On three LaMP personalization benchmarks WFT achieves the best average performance, matches/exceeds SFT on individual tasks, and approaches SFT within <7% of its effective compute. Logit analysis shows 0.875 cosine similarity between WFT and SFT logit shifts over 95% of next-token probability mass.
- **Key Innovation**: Training-free personalization via distributional logit transport — a lightweight alternative to per-user SFT, relevant to the wiki's personalization and efficient-adaptation lines.

### Orientation, not magnitude: the causal structure of task-vector interference in merged language models
- **Authors**: Chencheng Zhu
- **Institution**: —
- **Date**: 2026-08-12
- **Link**: [2608.11797](https://arxiv.org/abs/2608.11797)
- **Abstract**: Model merging by task arithmetic is diagnosed mostly by *magnitudes* (representation bias, cross-task linearity deviation, parameter overlap). Tracking the exact layerwise cross-term of merged LLMs and intervening on it directly, the paper finds magnitude insufficient and inconsistent across model families. The layerwise flux is dominated by **amplifying transport of the existing cross-term** (~65–70% in both families); erasing it is undone by propagation (rebuilt to 99% of norm at cosine 0.99) unless applied near the output. The carried direction is causally load-bearing: erasure along it removes interference dose-dependently, while norm-matched wrong-direction controls fail or backfire. Instruction wrappers gate the effect (13× less relative interference under a wrapper that internally amplifies the cross-term). The ±15% "universality" of naive bfloat16 generation is shown to be quantization roughness. All 46 predictions were preregistered.
- **Key Innovation**: A preregistered causal-structure account of task-vector interference — direction, not magnitude, with a mechanism account of when erasure survives — a rigorous entry for the wiki's model-merging line (MeRLa, TIES).

### HyperFix: Combinatorial Nonlinear Correction for Task Vector Merging
- **Authors**: Hyo Seo Kim, Ren Wang
- **Institution**: Illinois Institute of Technology (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11499](https://arxiv.org/abs/2608.11499)
- **Abstract**: Task vectors merge models without joint retraining, but most methods use scalar tuning restricted to linear rescaling and require repeated tuning per subset. **HyperFix** formulates merging across varying task subsets as a combinatorial correction problem: a lightweight hypernetwork predicts **subset-conditioned nonlinear corrections in weight space**, trained once on singleton/pair/triple subsets and generalizing to larger subsets without per-subset optimization. Local perturbation analysis bounds the residual beyond linear merging and motivates learning it from small task updates. Outperforms existing task-vector merging methods while reducing tuning cost.
- **Key Innovation**: Hypernetwork-predicted nonlinear, subset-conditioned corrections — pairs with the Orientation paper as a practical counterpoint in the wiki's model-merging thread.

---

## 4. Agents, Skills & Memory

### EvoGraph-Mem: Failure-Aware Editable Graph Memory for Long-Term Language Agents
- **Authors**: Yuxi Qian, Yuxiang Ren
- **Institution**: —
- **Date**: 2026-08-12
- **Link**: [2608.11248](https://arxiv.org/abs/2608.11248)
- **Abstract**: Long-term agent memory degrades: previously distilled insights become outdated, over-generalized, or harmful under new contexts, causing memory pollution on reuse. **EvoGraph-Mem** studies insight-level memory maintenance via an **editable insight graph** where each node tracks positive evidence, negative evidence, and activation state, letting the agent distinguish reusable from conflicting/invalid insights. A utility-aware retrieval mechanism and a graph controller update the graph after task execution (keep reliable, archive invalid, revise outdated, add newly discovered reusable insights). Consistently outperforms memory-agent baselines across backbones; ablations show append-only memory is insufficient for long-horizon tasks, while evidence-aware retrieval and graph-level editing improve reliability.
- **Key Innovation**: Failure-aware, editable memory graphs — a maintenance/repair operation for agent memory that complements the wiki's memory-correctness line (Rollback Repair, memory poisoning).

### Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem
- **Authors**: Hongyao Tang
- **Institution**: SJTU / Shanghai AI Lab (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11654](https://arxiv.org/abs/2608.11654)
- **Abstract**: There is no unified formal account of what agent memory *is* or when it is *optimal*. The paper proposes: **memory is a basis, knowledge is its span, answerability is a coverage problem** — events are stored from a material, a generation operator turns any event set into entailed knowledge, and a query is answerable iff some single item in the span covers it. Optimal memory is the capacity-constrained maximizer of expected coverage, tracing a **utility–capacity frontier** as a common yardstick. Under noise, the write policy must infer truth (coverage vs precision); the continual agent-memory problem is formalized as a sequential MDP where memory is state, writing is action, and query-time utility is delayed reward. The framework is instantiated on Homer's *Odyssey* (frontier, compression zone, coverage-precision divergence as concrete numbers) and used to position existing systems.
- **Key Innovation**: A formal basis/span/coverage theory of agent memory with a measurable optimality frontier — a unifying frame for the wiki's scattered agent-memory threads (DocMemo, Scrubs, memory poisoning).

### Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents
- **Authors**: Gen Dong, Yanjie Gao, Liqun Li, Tianyin Xu, Yu Hua, Fan Yang
- **Institution**: UIUC + Huawei + Microsoft (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11888](https://arxiv.org/abs/2608.11888)
- **Abstract**: Skills are the de facto mechanism for extending agents, yet prior work reports mixed results — some skills hurt. This paper provides a **differential analysis framework** attributing failures/cost regressions to specific loaded skills by comparing a target skill-guided run against a no-skill or semantically-matched reference run. Instantiated on SkillsBench and SWE-Skills-Bench, it yields **307 skill-induced failures (125 functional, 182 efficiency regressions)**. Key findings: (1) functional failures rarely come from obviously irrelevant skills — seemingly relevant skills make agents incorrectly implement or omit required elements; (2) efficiency regressions are not explained by prompt length alone; (3) the largest Excessive-Procedure sources are excessive verification (67 cases) and heavy implementation pipelines (30) — skills turn validation checklists and construction recipes into mandatory work. They release **SkillTriage**, a taxonomy-guided attribution tool.
- **Key Innovation**: First large-scale causal attribution of failures to skills — the wiki's skills cluster (SkillZip, SkillLens, SkillSentry) gains a failure-mode and cost-audit substrate.

### SHAPER: Self-Evolving Embodied Agents via Skill-Harness Evolution
- **Authors**: Peidong Wang, Zhiming Ma, Ying Chang, Xufang Luo, Xiaocui Yang, Shi Feng, Yuqing Yang, Dongsheng Li
- **Institution**: Microsoft Research Asia + Northeastern University (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11350](https://arxiv.org/abs/2608.11350)
- **Abstract**: Embodied agents are increasingly *systems* around foundation models — performance depends on skills, context, action interfaces, and the execution harness, not just weights. SFT/RL need extra data, rewards, and runs; train-free code-centric approaches rely on programmable robot APIs unavailable in fixed-interface settings. **SHAPER** is a train-free self-evolving framework that keeps model parameters frozen and improves the non-parametric agent system by evolving **reusable skills and a context-code harness through target-environment rollouts** — the same frozen model acts as planner and optimizer. On VLABench and ESI-Bench across different low-level action interfaces, it compares favorably with pure execution, SFT, and test-time-scaling baselines (verifier-free selection, voting).
- **Key Innovation**: Skill-and-harness evolution as a train-free route to self-evolving embodied agents — the wiki's self-evolving-agent cluster (MERA, MEGA, Co-Evolution) gains an embodied, non-parametric entry.

---

## 5. Recommendation, CTR & Advertising

### HCGRec: Hint-Conditioned Generative Recommendation with Semantic IDs
- **Authors**: Kangning Zhang, Haotian Fang, Xukun Luo, Hao Yin, Yang Gao, Peng Yan, Weiwen Liu, Weinan Zhang, Yong Yu
- **Institution**: SJTU + Huawei Noah's Ark (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11980](https://arxiv.org/abs/2608.11980)
- **Abstract**: Semantic-ID generative recommenders predict the next item by autoregressively generating discrete semantic tokens, but reward-based post-training hits a structural bottleneck: when an early semantic token enters the wrong branch, finite rollout groups rarely reach ground truth, so group-relative optimization gets identical zero rewards. **HCGRec** diagnoses each instance with checkpoint rollouts and supplies a **minimal target-prefix hint** only when the current generator cannot reach the correct item, then generates the unhinted suffix under the hinted branch — turning zero-reward groups into informative comparisons. Hint-aware credit decomposition uses SFT to preserve item-semantic/prefix alignment on hinted tokens and GRPO on the sampled suffix. Substantially improves over SFT and vanilla reward post-training, cutting zero-advantage training samples from >70% to <20% (CIKM 2026).
- **Key Innovation**: Conditional hinting + credit decomposition to unstick semantic-ID GRPO — a fix for the zero-reward training-signal problem central to the wiki's generative-rec/GRPO line (Semantic IDs, GenRec).

### PRISM: From Overlooked to Explored — Recovering Item Relations via Mixture of Perspectives for Sequential Recommendation
- **Authors**: Junyoung Kim, Wonbin Kweon, Woojoo Kim, Jaehyung Lim, Dongha Kim, Hwanjo Yu
- **Institution**: POSTECH (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11846](https://arxiv.org/abs/2608.11846)
- **Abstract**: Sequential recommenders rely on self-attention's pairwise item interactions, yet empirical analysis shows a persistent **similarity bias**: dot-product attention scores disproportionately favor similar items, systematically overlooking heterogeneous relations that carry real preference signal. **PRISM** re-examines item relations from multiple perspectives using K **Perspective Lenses** — an Affinity View refining homogeneous relations and a Contrast View exposing heterogeneous ones suppressed by similarity bias — calibrating attention to capture the full preference spectrum. Consistent SOTA on seven real-world benchmarks (CIKM 2026 full research track).
- **Key Innovation**: A diagnosable attention bias (similarity bias) plus a multi-view fix — a principled contribution to the wiki's sequential-rec attention line.

### GALLM: Making Collaborative Signals Count — Graph-Aware LLMs for Sequential Recommendation
- **Authors**: Fenglin Yan, Bohao Wang, Jian Zhang, Yu Cui, Tongya Zheng, Ye Feng, Can Wang, Jiawei Chen
- **Institution**: Zhejiang University (likely)
- **Date**: 2026-08-12
- **Link**: [2608.12184](https://arxiv.org/abs/2608.12184)
- **Abstract**: LLM recommenders struggle to capture collaborative signals from language-centric pretraining. **GALLM** builds a collaborative graph over text and item tokens modeling three relation types — Text–Text (semantic dependencies), Item–Text (alignment with descriptions), and Item–Item (global co-occurrence) — and converts them into **lightweight learnable attention biases** injected into the LLM attention, enabling collaborative-aware token interaction without a separate graph encoder. On four benchmarks it beats the strongest baseline by 9.76% on average in HR@5.
- **Key Innovation**: Graph-structure-as-attention-bias for LLM recommenders — a parameter-light injection path for the wiki's LLM-based recommendation cluster.

### From Prompting to Behavioral Alignment: Personalized LLM Judges for Recommendation Evaluation
- **Authors**: Alireza S. Ziabari, Kat Ellis, Colleen Chan, Ding Tong
- **Institution**: — (industry/academia)
- **Date**: 2026-08-12
- **Link**: [2608.11493](https://arxiv.org/abs/2608.11493)
- **Abstract**: LLMs as offline rec-evaluation judges can predict user engagement from raw text logs, but the paper identifies a failure mode it calls **bidirectional rationalization**: zero-shot LLMs convincingly argue for both positive and negative engagement on the *same* item with identical evidence. They develop a sequential behavioral alignment framework — fine-tuning plus preference optimization over paired correct/counterfactual rationales — evaluated on real-world homepage interaction logs, achieving +32.19% Macro-F1 over zero-shot and matching a production feature-engineered baseline, while emitting human-interpretable reasoning traces.
- **Key Innovation**: A documented zero-shot judge failure mode plus an alignment fix — evaluation hygiene for the wiki's LLM-judge and rec-evaluation threads.

### FunnelCausalNet: Funnel-aware Joint Conversion-Revenue Uplift for Multi-tier Coupon Allocation
- **Authors**: Yu Zhang, Zhihan Wang, Guanlin Chen, Min Jiang, Shuai Li
- **Institution**: SJTU (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11675](https://arxiv.org/abs/2608.11675)
- **Abstract**: GMV follows a deterministic funnel (conversion × conditional order value) and is zero-inflated and heavy-tailed, so coupon uplift on GMV is awkward to model. **FunnelCausalNet** couples a binary conversion head with a nonnegative conditional-value head via μ_gmv = μ_conv·μ_val, under explicit RCT/support/rate-gap/covariance-control assumptions, with an idealized MSE analysis identifying regimes where funnel composition reduces pointwise variance. Paired with marginal split-conformal CATE summaries (Bonferroni union as audit bands) and a Lagrangian budgeted allocator with RCT-anchored subsidy accounting. On semi-synthetic Criteo-MT7 the mean AUUC_GMV is within one seed std of the leading feature-interaction baseline among eleven; an ablation reduces GMV effect error vs direct GMV regression by 18–48% across zero-inflation regimes; on de-identified industrial Hotel-Coupon RCT logs (~4.9M hold-out exposures/seed) it has the best seed-averaged DeltaROI at all seven 10–60% anchors (CIKM 2026).
- **Key Innovation**: Funnel-composed uplift with rigorous assumption accounting for coupon allocation — a methodological entry for the wiki's uplift/CTR causal line (ReAlloc, uplift calibration).

### Token-Level Credit Assignment Optimization for Generative Document Retrieval
- **Authors**: Xinpeng Zhao, Yang Liu, Ran Chen, Xinyu Ma, Daiting Shi, Pengjie Ren, Zhumin Chen, Zhaochun Ren, Xin Xin
- **Institution**: Shandong University (likely)
- **Date**: 2026-08-12
- **Link**: [2608.12049](https://arxiv.org/abs/2608.12049)
- **Abstract**: Generative retrieval (GenIR) decodes DocID tokens, but evaluation happens only after the full DocID — sequence-level rewards propagate the same document-level feedback to every decoding step, so the policy can't tell which token decisions caused success/failure. The paper proposes **token-level relevance rewards**: each step's reward estimates how that token decision changes expected retrieval quality of the generation trajectory, enabling precise credit assignment. Practical reward estimation strategies tailored to DocID generation are incorporated into a policy optimization framework; consistently outperforms sequence-level reward baselines on retrieval benchmarks.
- **Key Innovation**: Step-level credit assignment for autoregressive DocID generation — a GenIR analogue of the wiki's token-level RL credit threads (CSCR, CoRT), and a cousin of HCGRec's hinting idea.

---

## 6. Sequential Modeling, Time Series & Finance

### FM-LLM: A Frequency-Enhanced Mixture-of-Experts Framework for Adapting LLMs to Time Series Forecasting
- **Authors**: Rentao Gu, Yihang Ding, Junjie Li, Yi Ding, Weijing Sang, Xiaoli Huo, Xin Qin, Yuefeng Ji
- **Institution**: BUPT (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11623](https://arxiv.org/abs/2608.11623)
- **Abstract**: LLM-based time-series forecasting relies heavily on textual prompts for modality alignment — high compute overhead that fails to exploit spectral dynamics. **FM-LLM** is a prompt-free, frequency-aware frozen-LLM adaptation grounded in constrained asymmetric coupling: a Fourier Analysis Network (FAN)-based spectral token aligner injects structured harmonic representations with numerical compatibility; an asymmetric MoE decoder enforces role separation — shared experts with lightweight FAN layers reconstruct the global periodic backbone, routed experts (restricted to standard FFNs) specialize in non-periodic residual dynamics; a time-frequency hybrid loss mitigates autoregressive error accumulation. SOTA on 59/78 metrics across eleven benchmarks, +5.3% MSE / +5.6% MAE over the strongest autoregressive LLM baseline (max +8.0%/+8.4%), with robust 10% few-shot and zero-shot transfer (Knowledge-Based Systems 2026).
- **Key Innovation**: Prompt-free frequency-aware MoE adaptation of frozen LLMs for forecasting — a spectral-design entry for the wiki's LLM-time-series line (SCALER, REATS).

### RG-ResMoE: Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting
- **Authors**: Junyi Ye, Gargi Vijay Borde
- **Institution**: USC (likely)
- **Date**: 2026-08-12
- **Link**: [2608.12251](https://arxiv.org/abs/2608.12251)
- **Abstract**: Financial volatility is regime-dependent, but feeding regime information into neural nets can destabilize training. This paper asks *where* regime info should enter: **RG-ResMoE** restricts regime state variables to a gating network that routes residual corrections, never letting them into the direct forecast. Five-day realized-volatility forecasts for 1,027 U.S. equities under a matched rolling walk-forward design: RG-ResMoE beats a capacity-matched MLP in accuracy and training stability (replicated on a Japanese panel); **appending regime variables directly to the input degrades both**, hard routing underperforms soft routing. Concludes that in compact volatility models MoE's value is controlling how nonstationary regime information influences prediction, not adding capacity.
- **Key Innovation**: A clean "where does regime info enter" ablation with a routing-only design — methodological guidance for the wiki's regime-aware/MoE time-series line.

### Forma: Long-Horizon Forecasting of Complete Financial Statements
- **Authors**: Travis L. Johnson, Jiannan Jiang, Soumyabrata Chaudhuri, Yihao Chen, Lauren Falvey, Donal O'Cofaigh
- **Institution**: UT Austin McCombs School of Business (from repo affiliation)
- **Date**: 2026-08-12
- **Link**: [2608.11327](https://arxiv.org/abs/2608.11327)
- **Abstract**: No prior work jointly forecasts complete financial statements beyond one year, yet most firm value in DCF valuation sits past that window. They release **ProForma-20Q** — a reproducible benchmark forecasting 78 statement line items 1–20 quarters ahead, scored by change-space R² — and **Forma**, a transformer that reads statements as sets of (account, quarter, value) tuples and maximizes a masked-tuple Gaussian likelihood. Forma beats classical ML, chained gradient boosting, a zero-shot time-series foundation model, and frontier LLMs; its lead widens with horizon; Gaussian intervals never under-cover; forecasts nearly satisfy accounting identities (exact coherence recoverable at no significant accuracy cost); the tuple interface supports scenario analysis (pinning future revenue sharpens the rest of the statement).
- **Key Innovation**: Specialist statement-level forecasting (tuples + Gaussian likelihood) that beats generalist scale at long horizons — evidence for the wiki's specialist-vs-generalist forecasting debate.

### Disentangling the Expressivity of RoPE
- **Authors**: Selim Jerad, Anej Svete, Jiaoda Li, Ryan Cotterell
- **Institution**: ETH Zurich (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11909](https://arxiv.org/abs/2608.11909)
- **Abstract**: Two recurring accounts explain RoPE's success: expressivity studies tie periodic position info to modular predicates; mechanistic/long-context studies emphasize positional anchors and local offsets. For fully uniform, finite-precision soft-attention transformers, the paper formalizes both: if every rotary component is periodic, RoPE transformers recognize exactly languages definable in **past temporal logic with modular predicates**; conventional RoPE is different because its rotations never repeat — yielding a precision-dependent bounded simulation of fixed-offset look-back rather than an all-length modular characterization. Controlled experiments match the separation: constructed periodic schedules length-generalize on modular languages while conventional RoPE behaves like a bounded locality bias and can impair position-invariant access to distant context.
- **Key Innovation**: A formal expressivity characterization separating periodic vs conventional RoPE — theory for the wiki's position-encoding and long-context lines (RoPE theory, length generalization).

---

## 7. Efficiency, KV Cache & Serving

### LinearKV: One Cached State Suffices for Position-Independent Caching in Hybrid LLMs
- **Authors**: Yirui Liu, Ruoling Qi, Longwen Wang, Xuaner Wu, Jian Chen, Yuxin Jin, Jiawei Shao, Xuelong Li
- **Institution**: SJTU + Shanghai AI Lab (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11231](https://arxiv.org/abs/2608.11231)
- **Abstract**: Position-independent caching (PIC) accelerates LLM serving but is built for full-attention models (token-indexed KV to match, concatenate, and locally repair). Hybrid LLMs expose only fixed-size linear states, breaking those primitives. **LinearKV** is a training-free hybrid-PIC framework built on a *decoupled initialization*: each linear layer maps its K matched local states to a **single initial state** while attention layers concatenate KV as before, so existing PIC selectors/recomputation are reused as-is. A single cached state suffices: the algebraically-principled alternative of composing all K states into the exact full-prefix state (concurrent work HYPIC) is unnecessary and sometimes harmful — on the Mamba-2 model exact composition collapses under every selector (46.6% of full quality vs 86.8% for a single cached block under EPIC); a single state also cuts TTFT to 0.46× full prefill. Results hold across LongBench QA and RULER at 8K–32K.
- **Key Innovation**: A negative result with practical payoff — exact state composition is worse than a single-state initializer for hybrid PIC — a direct datapoint for the wiki's KV/PIC thread (Counter-Causal eviction, RippleKV).

### QV-PIC: Query-Aware Visual Position-Independent Caching for Efficient RAG Serving
- **Authors**: Yilin Liu, Rui Meng, Wangze Ni, Jianxin Yan, Heng Cao, Libin Zheng, Peng Cheng, Jinfei Liu
- **Institution**: Hunan University + industry (likely)
- **Date**: 2026-08-12
- **Link**: [2608.12121](https://arxiv.org/abs/2608.12121)
- **Abstract**: RAG prefills identical chunks across queries; PIC reuses KV across positions but is bounded by text-token volume. Rendering chunks as images compresses text into fewer visual tokens but rendered-image PIC degrades more than text PIC due to contextual mismatch across independent caches and loss of fine-grained textual evidence. **QV-PIC** is a query-aware dual-resolution visual PIC reuse framework: offline it compiles visual caches under the model's native chat-template prefix (better PIC quality without online recomputation); online it keeps global context low-res and restores fine-grained textual evidence in a high-resolution budget scored by cumulative query relevance. Across six tasks QV-PIC improves average F1 by +21.6 pts over vanilla rendered-image PIC, surpasses optimized text PIC by 2.58 F1 while cutting TTFT 17.2% (and 83.8% vs full prefill).
- **Key Innovation**: Visual-token PIC with query-aware dual-resolution repair — extends the wiki's KV-cache/PIC line into image-rendered RAG serving.

### Massive Activations in Hybrid Linear Attention LLMs: Pre-Attention Spikes and Inter-Spike Plateaus
- **Authors**: Zunhai Su, Bohan Sun, Xialie Zhuang, Shuibai Zhang, He Xiao, Jing Xiong, Hengyuan Zhang, Zhongzhu Zhou, Tiantian Zhang, Ngai Wong, Chuan-Wei Kuo
- **Institution**: HKU + StartluxLabs (likely)
- **Date**: 2026-08-12
- **Link**: [2608.12149](https://arxiv.org/abs/2608.12149)
- **Abstract**: First systematic study of **Massive activations (MAs)** in layer-interleaved hybrid linear-attention (HLA) LLMs, uncovering two architecture-aligned morphologies: MAs spike immediately before full attention layers (**pre-attention spikes, PAS**) and can persist through intervening linear attention layers (**inter-spike plateaus, ISP**); as attention densifies, PAS connect through ISP, recovering full-attention morphology. Recurrence confirmed across five linear architectures, six hybridization configs, five domains, and open models from 1.2B to 397B. Controlled pretraining (GDN hybrids to 1.3B) shows both morphologies emerge early and respond asymmetrically to output gating. A systematic-outlier analysis supports a shared lifecycle account governed by MA-cancellation timing (localized write-sink-cancel for PAS, delayed cancellation for ISP).
- **Key Innovation**: The first cross-architecture map of massive-activation geometry in hybrid LLMs — the wiki's HLA/massive-activation thread (pre-attention spikes, quantile cuts) gains a morphology taxonomy and pretraining story.

---

## 8. Games, Game Theory & Mechanism Design

### Welfare Approximation in Multilateral Trade
- **Authors**: Tomer Ezra, Aadityan Ganesh, Aviad Rubinstein
- **Institution**: Bar-Ilan University + Stanford (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11351](https://arxiv.org/abs/2608.11351)
- **Abstract**: Introduces **multilateral trade**: a mechanism-design problem where a single trade involves k agents and executes only if *all* agree (bilateral trade is the k=2 case). Under IC, IR, and budget balance, they give a DSIC mechanism with approximation ratio O(k²) and a BIC mechanism with Õ(k^(3/2)), with matching lower bounds up to polylog factors. Extends to an ℓ-out-of-k partial-agreement setting where welfare guarantees improve smoothly as k−ℓ grows, again with matching bounds.
- **Key Innovation**: First welfare-approximation study of joint-participation multilateral trade with tight bounds — a clean mechanism-design contribution for the wiki's GT/mechanism-design cluster.

### A Solution to the Roommate Problem
- **Authors**: Meina Takahashi
- **Institution**: —
- **Date**: 2026-08-12
- **Link**: [2608.11682](https://arxiv.org/abs/2608.11682)
- **Abstract**: Extends **priority-neutral matching** (Reny 2022, school choice) to the roommate problem. Results: a blocking-neutral matching always exists in constrained roommate problems under arbitrary feasibility constraints (Thm 1); stable ⊆ blocking-neutral ⊆ Pareto-optimal matchings (Thm 2); whenever stable matchings exist, blocking-neutral coincides with stable (Thm 3). Existence fails under weak preferences; the concept also extends to two-sided school choice.
- **Key Innovation**: A solution concept for the roommate problem (stable matchings need not exist) that always exists — theory for the wiki's matching-market and fair-division threads.

### Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes
- **Authors**: Chen Xu, Zitian Guo, Chenyan Xiong
- **Institution**: CMU (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11390](https://arxiv.org/abs/2608.11390)
- **Abstract**: Generative engines allocate attention/attribution through citations, creating a strategic tension: content providers optimize for citation while platforms must preserve answer quality. The paper shows this can escalate into **citation wars** — GEO attacks adapt to conventional defenses with citation-seeking rewrites that degrade quality and add unsupported claims. They model supplier–platform interaction as a repeated Stackelberg game with partial monitoring, identify when citation competition reaches an inert stationary outcome, and propose **VCR (verifiable-content rewards)**: rather than only penalizing suspicious rewrites, the platform also credits rewrites surfacing checkable factual substance. On three benchmarks VCR achieves the largest Net defense-utility score (+12.1 pts over the strongest baseline) and produces win–win outcomes.
- **Key Innovation**: Mechanism design for the GEO/citation ecosystem — connects the wiki's generative-engine/search (GEO, SAGEO) and mechanism-design threads.

### When Do Institutions Beat Intelligence?
- **Authors**: Zhengye Han
- **Institution**: —
- **Date**: 2026-08-12
- **Link**: [2608.11357](https://arxiv.org/abs/2608.11357)
- **Abstract**: More capable agents do not necessarily form more capable collectives — MAS can hold sufficient information yet fail from poor evidence routing, unreliable reports entering public belief, correlated claims masquerading as independent support, stale/strategically distorted shared state, or ineffective action interfaces. The paper builds controlled artificial ecologies around four loci of collective failure (access & routing; admission & dependence; state maintenance & incentives; representation & action), varying model capability vs institutional structure. A consistent boundary emerges: **institutions help when they repair failures in constructing usable public state, but lose their advantage when their signals are uninformative/uncheckable, when stronger intelligence can do the same transformation directly, or when resulting state can't support reliable action**.
- **Key Innovation**: A diagnosis-driven framing of intelligence-vs-institutions for collective reasoning — relevant to the wiki's multi-agent and deliberation-debate lines (Koopman certificates, majority-vote pitfalls).

---

## 9. Safety, Alignment & Unlearning

### Locating and Controlling Implicit Personalization in Large Language Models
- **Authors**: Yueru Yan, Siqi Wu, Thai Le
- **Institution**: University of Mississippi (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11735](https://arxiv.org/abs/2608.11735)
- **Abstract**: LLMs shift outputs in response to implicit demographic cues even when no demographic identity is stated; prior work documents the behavior but not the internal locus. Using matched cued/neutral conversations across five LLMs, the paper establishes a **localized internal activation signal tracking recommendation changes (r up to 0.87)**. Multiple cues' internal signals largely combine, but output changes don't add up. Removing the internal signal for one cue suppresses its influence — often better than prompting the model to ignore demographics — while preserving general benchmark performance; however selective removal with co-present dimensions intact remains highly model- and attribute-specific.
- **Key Innovation**: Localization + causal control of implicit personalization in activation space — connects the wiki's personalization-over-inference (MirageBench) and interpretability threads.

### Localizing Safety Alignment: MLP Layers and Mid-Network Blocks Encode Refusal Behavior in LLMs
- **Authors**: Mingyu Zong, Sampad Mohanty, Bhaskar Krishnamachari
- **Institution**: USC (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11583](https://arxiv.org/abs/2608.11583)
- **Abstract**: Refusal behavior may be concentrated in a subset of parameters rather than distributed across the network. Transplanting weights from aligned models into matched unaligned bases at multiple granularities (attention vs MLP, contiguous regions, MLP blocks), on two open-weight pairs and four safety benchmarks: **refusal transfer is dominated by MLP weights (≥2.7× gains over attention)**; within the MLP stack, safety-relevant parameters concentrate mid-network — the layers 8–11 block is selected first in all six greedy searches. Composition is non-additive: in 5/6 greedy trajectories adding more aligned blocks *reduces* refusal, and selective subsets can beat full MLP transplantation on malicious refusal, benign over-refusal, or both. Greedy orders transferred to OR-Bench vary with source benchmark (benchmark-dependent precision-coverage trade-off).
- **Key Innovation**: Localization + interaction-sensitivity of safety alignment with practical targeted-intervention implications — the wiki's safety-alignment-mechanics line gains a transplant-based map (echoes the "alignment is localizable" vs distributed debate).

### Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning
- **Authors**: Zirui Song, Huaxing Liu, Xiang Wang, Shuai Li, Xinye Li, Lang Gao, Jinghui Zhang, Zheng Lu, Fengxian Ji, Xiaojun Chang, Xiuying Chen
- **Institution**: University of Ottawa + UTS + industry (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11408](https://arxiv.org/abs/2608.11408)
- **Abstract**: White-box audits show unlearned LLMs retain latent traces of target knowledge even when outputs no longer express it, but prior audits are one-off diagnostics — unclear if residual signals predict future recovery under continued training or are safe optimization targets. **J-Access** is an inference-time audit using the Jacobian lens to map intermediate representations into vocabulary space, measuring how often target concepts stay accessible along the output pathway. Auditing 398 public unlearned models across 8 methods: (1) most retain access above the retain-only gold level; (2) pre-attack accessibility predicts recovery speed/extent at model level but not which specific facts recover; (3) **minimizing J-Access does not promote genuine deletion** — the model learns to hide from the audit (lower audit scores, greater post-attack recovery). Positioned as a model-level diagnostic, not an optimization target.
- **Key Innovation**: A Jacobian-lens audit plus a negative result against audit-as-optimization — measurement hygiene for the wiki's unlearning line (unlearning evaluation, latent-trace audits).

---

## 10. World Models & Benchmarks

### AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research
- **Authors**: Marjan Moodi, Xuankang Zhu, Fernando De Mesentier Silva, Harold Chaput, Mohammad Reza Taesiri
- **Institution**: Electronic Arts + University of Alberta (from project page)
- **Date**: 2026-08-12
- **Link**: [2608.11216](https://arxiv.org/abs/2608.11216)
- **Abstract**: World modeling is unsettled — architectures, objectives, and state representations interact with no dominating recipe — making it an ideal testbed for *open-ended* AI research rather than engineering-to-spec. **AutoWorldModel-Bench** is a closed-loop benchmark where frontier coding agents autonomously improve a provided world-model starter under a fixed compute budget, spanning eight game environments under a unified structured-state representation (ground-truth entity state via shared tensor format, isolating dynamics from perception, minutes-per-run iteration). Across 64 sessions, Codex-5.4 and Claude Opus 4.6 improve the starter on 63; in 91% of sessions the winning edit is a non-trivial research-style modification (new objective, representation, rollout procedure, or architecture) rather than hyperparameter tweak.
- **Key Innovation**: A state-centric, research-style agentic benchmark for world models — a measurement substrate for the wiki's world-model cluster (FACT, LeWorldModel).

### RIFT: Keep the Future, Drop the Rollout — Rollout-Free Imagination via Future Tokens for World Action Models
- **Authors**: Chushan Zhang, Jinguang Tong, Xuesong Li, Yikai Wang, Hongdong Li
- **Institution**: Australian National University (likely)
- **Date**: 2026-08-12
- **Link**: [2608.11521](https://arxiv.org/abs/2608.11521)
- **Abstract**: World action models (WAMs) condition robot actions on predicted futures, but iterative video rollout adds deployment latency. Across four WAMs on all 40 LIBERO tasks, paired closed-loop interventions show masking/reassigning future-cache values changes execution, yet for Joint and Cosmos-2 **replaying one fixed final-clean K/V cache nearly preserves execution** (1.7–1.9 cm end-effector error, 97.9–98.2% success) — separating cache *consumption* from *production*. **RIFT** uses learned anticipation tokens to construct a complete future K/V cache in one backbone pass while keeping the future-read interface. On LIBERO: 98.8% success (close to rollout-based Joint/IDM/LingBot-VA at 98.4–98.6%) with 68.2–89.1% lower action-chunk latency; on RoboTwin 2.0 it reaches 92.9/92.6% on clean/randomized scenes, highest among evaluated methods.
- **Key Innovation**: Demonstrates future-cache value is separable from rollout, enabling rollout-free future conditioning — relevant to the wiki's world-action-models and latent-futures lines (Foresight Without Seeing, LeWorldModel).

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **OPD/rollout RL shifts from recipes to diagnosis-and-constrain** | GCPO reads subspace-overlap spikes as early warnings and constrains updates by orthogonal projection; PAIR shows rollout-allocation gradients are pair-contrast U-statistics requiring design-unbiased reweighting; REOPD gates reward extrapolation per-token by reliability; the TTS-lens paper argues OPD gains are "illusory" sampling-efficiency, not new capability; Rubric Dropout is a one-line fix for judge-proxy reward hacking | GCPO, PAIR, REOPD, OPD×TTS, Rubric Dropout |
| **Agent memory is being formalized and made maintainable** | A basis/span/coverage theory defines optimal memory via a utility–capacity frontier; EvoGraph-Mem edits an insight graph with evidence tracking to cure memory pollution; on the skills side, a differential framework attributes 307 failures to loaded skills | Formal Agent Memory, EvoGraph-Mem, Skills Can Be Harmful |
| **CIKM 2026 rec papers attack structural training signals** | HCGRec fixes the zero-reward dead zone of semantic-ID GRPO with conditional hints + credit decomposition; PRISM diagnoses similarity bias in sequential-rec attention and fixes it with Perspective Lenses; GALLM injects collaborative graph relations as attention biases into LLMs | HCGRec, PRISM, GALLM |
| **PIC and KV efficiency meet hybrid attention and visual RAG** | LinearKV shows a single cached linear state suffices for hybrid PIC (exact state composition is unnecessary, even harmful on Mamba-2); QV-PIC brings query-aware dual-resolution repair to image-rendered PIC for RAG; Massive Activations maps pre-attention spikes / inter-spike plateaus across five hybrid architectures | LinearKV, QV-PIC, Massive Activations |
| **Test-time transfer and no-weights adaptation mature** | AI4AI transfers strong→weak capability via inference-time harnesses (0.49→0.91 without parameter updates); Weightless Fine-Tuning transports logit-space residuals for personalization at <7% of SFT compute; SHAPER evolves embodied skills and harnesses train-free | AI4AI, Weightless Fine-Tuning, SHAPER |
| **Model merging gets a causal-structure account** | Orientation-not-magnitude shows task-vector interference is carried by an amplifying transport direction (erasable dose-dependently near the output), with 46 preregistered predictions; HyperFix learns subset-conditioned nonlinear corrections via a hypernetwork | Orientation, HyperFix |
| **Mechanism design meets generative engines** | Citation allocation under GEO pressure modeled as a repeated Stackelberg game, with verifiable-content rewards (VCR) restoring win–win; multilateral trade gets tight welfare bounds; the roommate problem gains a always-existent solution concept | VCR, Multilateral Trade, Roommate Problem |
| **Forecasting doubles down on specialist structure** | Forma reads statements as account/quarter/value tuples and beats generalist foundation models and LLMs at 1–20-quarter horizons; RG-ResMoE shows regime info belongs in the routing gate, not the forecast; FM-LLM injects spectral structure prompt-free into frozen LLMs | Forma, RG-ResMoE, FM-LLM |

---

## Key Takeaways

1. **OPD research has entered its "trust but verify" phase.** Yesterday's window generalized OPD across modalities; today's window interrogates *what OPD actually does* — the TTS-lens paper (OPD≈"illusory distillation", sampling efficiency not new capability) is a direct challenge to the field's premise, while GCPO, PAIR, and REOPD respectively diagnose update geometry, fix allocation statistics, and gate extrapolation reliability. Combined with Rubric Dropout's explicit measurement of judge-proxy divergence, the message is: measure the reward curve and the capability boundary, don't trust the recipe.
2. **Agent memory and skills are being stress-tested, not just accumulated.** A formal basis/span/optimality theory (instantiated on the *Odyssey*) gives the wiki's scattered memory threads a common yardstick; EvoGraph-Mem adds failure-aware editing to prevent memory pollution; "Agent Skills Can Be Harmful" attributes 307 failures to loaded skills, showing skills convert validation checklists into mandatory work. The skill-accumulation enthusiasm of Aug 7–11 now has a measured failure cost.
3. **Recommendation keeps finding structural, non-scaling-law wins.** HCGRec (CIKM 2026) un-sticks semantic-ID GRPO with minimal hints — zero-advantage samples drop from >70% to <20%; PRISM fixes a diagnosed similarity bias in sequential attention; GALLM folds collaborative graph structure into LLM attention as bias. None of these add model scale; all attack training-signal structure.
4. **The specialist-vs-generalist forecasting debate gets strong new evidence.** Forma (specialist statement forecaster, wins widening with horizon) and FM-LLM (frozen-LLM spectral adaptation, 59/78 SOTA metrics) stake out opposite sides; RG-ResMoE contributes a decisive placement ablation (regime info in routing, not forecast). For the wiki's forecasting thread, "where information enters" is becoming the key design axis.
5. **Efficiency keeps exporting ideas to harder targets.** LinearKV's negative result (exact state composition is *worse* than a single cached state for hybrid PIC) is a useful caution: algebraic elegance ≠ serving wins. QV-PIC extends PIC to visual tokens with query-aware repair, and the Massive Activations taxonomy gives hybrid-LLM quantization a morphological map — all three feed the wiki's KV/efficiency infrastructure thread.
6. **Games/mechanism-design is producing clean, applicable results.** Multilateral trade with tight bounds, an always-existent roommate solution concept, and a citation-economics mechanism (VCR) that converts GEO conflict into win–win — the last one is directly actionable for the generative-search ecosystem the wiki tracks (SAGEO/GEO thread).

> ⚠️ Note on sourcing: this digest curates the **Thu Aug 13, 2026 announced window — Wed Aug 12 submissions (IDs ~2608.11207–2608.12307)**, harvested from the `/list/{cat}/recent` pages for cs.AI (211), cs.LG (182), cs.CL (92), cs.IR (16), cs.GT (5), cs.MA (18), econ.TH (5), stat.ML (11) — 540 entries / 380 unique IDs. All 37 papers are **grep-verified absent from the entire wiki** (zero overlap with the 08-12 digest's window end ~2608.11208). Institutions marked "(likely)" are inferred from author affiliations on the arXiv HTML pages or prior knowledge, not always the arXiv record; "—" means not identified. Accepted-venue notes (CIKM 2026, Knowl.-Based Syst. 2026) come from each paper's arXiv comments/journal-ref fields.
