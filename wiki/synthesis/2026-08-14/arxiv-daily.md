---
title: "arXiv Daily Digest — 2026-08-14"
type: synthesis
created: 2026-08-14
updated: 2026-08-14
sources: [arxiv-cs.AI, arxiv-cs.LG, arxiv-cs.CL, arxiv-cs.IR, arxiv-cs.GT, arxiv-cs.MA, econ.TH, stat.ML]
tags: [arxiv, llm, self-distillation, grpo, alignment, safety, interpretability, agent-memory, skills, skill-evolution, agents, retrieval, recommendation, time-series, finance, forecasting, pruning, speculative-decoding, diffusion, world-models, multi-agent, mechanism-design, verified-software, ai-scientists, open-models, daily-digest]
---

# arXiv Daily Digest — 2026-08-14

> **Batch note:** Today's digest covers the **Fri Aug 14, 2026 announced window — the Thu Aug 13 submission wave (IDs ~2608.124xx–2608.135xx)**, harvested from the `/list/{cat}/recent` pages for cs.AI (204), cs.LG (157), cs.CL (101), cs.IR (19), cs.GT (6), cs.MA (14), econ.TH (6), stat.ML (29) — **536 entries** — and curated into **29 papers, all 32 shortlisted arXiv IDs grep-verified absent from the entire wiki** (0 hits; zero overlap with [yesterday's digest](../2026-08-13/arxiv-daily.md), which stopped at ~2608.12307). **Same-day dedup:** the [arxiv-ai-search](./arxiv-ai-search.md) page (written earlier today by the scheduled scan) already claims 20 papers of this window — including the OPD trio (CROP, LOPD, CrEST), SPP, vToken, RoPE-Q/K rotations, Post-Norm depth growing, Vero, TsuGO, STAR, Doubly-Robust-CVR, FSGR, DrEM, DrIG, ORBIT, Do-LLMs-Beat-Nash, EA-RAM, Keep-Customize-Exit, DTAMLP, and Neural Quadratic Forms. Those **18 overlapping IDs were removed from this digest, not duplicated** — cross-references below point to the sibling page. **Model dedup:** [AlayaWorld v1.1](https://arxiv.org/abs/2608.13492) is already covered in the wiki ([game-rl-daily](../2026-08-02/game-rl-daily.md), [conference-digest](../2026-08-01/conference-digest.md)) — treated as an update, not re-listed. Signature themes of this digest's complementary slice: **agent memory and skills dominate** (RippleMem associative recollection, LycheeMemory V2 segment-level consolidation, MindMemOS self-evolving memory OS, ReFind's anti-structure raw-log search, SkillEvo multi-turn evolution gradients, DIVE diversity-population skills, QCR target-bound trajectory reuse), **skill evolution gets a safety formalization** (Practice Makes Unsafe / SkillMisevo), **world-model planning diagnostics go negative-on-objective** (Objective-Is-The-Bottleneck, ACPC), and **efficiency pushes pruning/decoding/caching orthogonal to the KV work in the sibling page** (SNIPER, RMM, DARTree, GCache).

---

## 1. LLM Post-Training: Self-Distillation & Credit Assignment

### I-SDPO: Instance-Level Adaptive Self-Distillation Policy Optimization
- **Authors**: Yubo Zhang, Xinhong Ma, Zezhong Tan, Ziqiang Dong
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12957](https://arxiv.org/abs/2608.12957)
- **Abstract**: GRPO gets no useful relative signal when every sampled response in a group is wrong; privileged self-distillation fills that gap but is a biased, low-variance surrogate — persistent imitation can oppose reward-improving updates once the policy can succeed. **I-SDPO** treats teacher reliance as capability-dependent: one routing decision per input instance (shared across its rollout group) — all-incorrect groups use a privileged self-distillation objective, any-success groups stay on GRPO. A local analysis characterizes when teacher and reward directions align and shows a non-vanishing biased distillation weight induces an optimization bias floor; the routing rule automatically withdraws teacher influence as success probability rises, with no hand-designed schedule. On SciKnowEval I-SDPO wins all four scientific domains, improving average mean@16 from 56.67% (GRPO) to 70.31%.
- **Key Innovation**: Instance-level GRPO/SDPO routing keyed to group success — a principled answer to the wiki's "when does the self-teacher help" question, sitting alongside this window's CROP/LOPD/CrEST (see [arxiv-ai-search](./arxiv-ai-search.md)) in the OPD-maturation thread.

---

## 2. Alignment, Safety & Interpretability

### Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents
- **Authors**: Xutao Mao, Liangjie Zhao, Xiang Zheng, Cong Wang
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12851](https://arxiv.org/abs/2608.12851)
- **Abstract**: Self-improving agents convert successful trajectories into persistent cross-task state — an *unsafe* success can become reusable policy after its triggering input disappears. Since skill evolution optimizes task outcomes rather than procedure safety, compromised experience causes **skill misevolution**. The paper introduces **SkillMisevo-Gym** (lifecycle-aware harness that versions skill state across agent frameworks), **SkillMisevo-Bench** (frozen design from malicious exposure to carryover tasks with benign control tasks and nine lifecycle metrics), and **SafeEvolve** (a wrapper that repairs unsafe content and governs reuse). Across 25 agent-method configurations (525 tasks × 25 episodes), all 21 evolved configurations author unsafe artifacts, only 15 cause fresh-session harm; three malicious tasks raise carryover ASR from 16.0% to 35.3%. SafeEvolve cuts unsafe retrieval and fresh-session harm by 26.7 and 17.3 percentage points at ~0.4-point benign utility cost.
- **Key Innovation**: The wiki's skills thread (yesterday's "Agent Skills Can Be Harmful") gains a *lifecycle* safety account and a repair mechanism — persistent-adaptation safety must govern both what updates write and what executors reuse.

### SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization
- **Authors**: Weihan Meng, Hongzhu Guo, Yi Jing, Dewen Liu, Zijun Yao, Xiaozhi Wang, Lei Hou, Juanzi Li
- **Institution**: Tsinghua (likely)
- **Date**: 2026-08-13
- **Link**: [2608.13538](https://arxiv.org/abs/2608.13538)
- **Abstract**: Explaining SAE features still relies on external behavioral observation — superficial and computationally costly at scale. **SAEVerbalizer** injects SAE decoder directions into an LLM's representations and fine-tunes downstream layers to generate natural-language explanations *directly from decoder directions*. The verbalization generalizes to unseen features, transfers across separately trained SAE dictionaries, and (with a lightweight adapter) extends to SAE features from different LLMs. Intervention experiments show injecting multiple directions yields an explanation combining their meanings, and reversing individual directions shifts meaning correspondingly.
- **Key Innovation**: An explainer that reads feature directions instead of collecting behavioral evidence — a practical speedup for the wiki's SAE/interpretability line (feature explanation, dictionary transfer).

### Training AI For When Humans Will Use It
- **Authors**: Kevin A. Bryan, Joshua S. Gans
- **Institution**: University of Toronto (likely)
- **Date**: 2026-08-13
- **Link**: [2608.12538](https://arxiv.org/abs/2608.12538)
- **Abstract**: AI predictions are combined with human verification, queries to other models, and so on — the economic value of an AI depends on how it interacts with its surrounding decision environment, which the paper models as a "composite experiment." Via a geometric argument they show what optimal training looks like when the AI makes a coarse state prediction inside this environment, why optimal training can be discontinuous in economic variables, and how heterogeneous users or monopoly trainers shift results. In particular, **maximizing unconditional prediction accuracy is generally suboptimal**.
- **Key Innovation**: An economics-of-training result (train for decision-environment value, not accuracy) — connects the wiki's value-alignment and decision-focused training threads with decision theory (econ.TH cross-list).

---

## 3. Agents: Memory, Skills & Trajectory Reuse

### RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory
- **Authors**: Jingbo Ji, Lingyi Li, Xilong Cheng, Yuhao Zhou, Wenji Zhang, Yuting Tan, Yunxiao Qin
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.13334](https://arxiv.org/abs/2608.13334)
- **Abstract**: The bottleneck in long-term agent memory is not storing past experience but *recovering the right evidence* when relevant information is distributed across interactions. **RippleMem** replaces one-shot retrieval with adaptive associative recollection: history is stored as cue-rich episodic memory units in an event-centric memory graph; a query first recalls memory anchors via hybrid cues, then expands along semantic/structural associations to recover missing supporting evidence — recalled memories serve as cues for completing the evidence needed. On LoCoMo and LongMemEval-S, RippleMem improves LLM-as-a-Judge accuracy by 3.95% and up to 11.87% while cutting graph construction cost ~30×.
- **Key Innovation**: Cue-driven associative expansion over event graphs — a memory-access design that pairs with the wiki's graph-memory cluster (EvoGraph-Mem, HippoRAG-adjacent lines).

### LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation
- **Authors**: Dongfang Li, Zixuan Liu, Junmai Wang, Jiahe Huang, Fuhao Li, Bonian Jia, Baotian Hu, Min Zhang
- **Institution**: HIT (likely)
- **Date**: 2026-08-13
- **Link**: [2608.12990](https://arxiv.org/abs/2608.12990)
- **Abstract**: Eager per-interaction consolidation makes memory construction increasingly costly as conversations grow. **LycheeMemory V2** replaces turn-level consolidation with **semantic segment-level consolidation**: exchanges are batched into segments and each finalized segment is encoded into context-independent typed memory records; lightweight structured indexes enable query-planned retrieval. With GPT-4.1-Mini it reaches 89.22% on LoCoMo and 92.20% on LongMemEval-S, and cuts construction tokens 86.0% / 75.9% vs A-Mem without increasing query-time usage. The accuracy–cost trade-off depends on *what* is retained and *at what granularity* it is consolidated.
- **Key Innovation**: Granularity-of-consolidation as the memory-efficiency design axis — relevant to the wiki's memory-cost thread (MindMemOS this window; A-Mem and related baselines in prior digests).

### MindMemOS: A Portable and Self-Evolving Memory Operating Layer for AI Agents
- **Authors**: Kaichao Liang, Yuqi Cui, Hao Kong, Xinyuan Huang, Guohaotian Hou, Qingcan Kang, Liang Chen, Yiyang Yin, Ke Ye, Jiaquan Guo, Da Chen, Lingan Zeng, Yixing Peng, Rong Yao, Shixiong Kai, Mingxuan Yuan
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12428](https://arxiv.org/abs/2608.12428)
- **Abstract**: Existing agent memory systems stay fixed after development. **MindMemOS** organizes open-world information with a unified entity-property-timestructure and supports scenario-adaptive memory modeling, higher-order pattern discovery, autonomous refinement, and continuous skill evolution. Its **MindMemEvolve** uses validation-driven evolutionary search over memory schemas plus "dreaming" (merging redundant records, resolving conflicts); implicit corrective feedback serves as a human-in-the-loop revision signal; **MindSkillEvolve** transforms execution trajectories into reusable, progressively refined skills. MindMemOS reaches 94.03% on LOCOMO and 70.63% on PersonaMem; MindSkillEvolve improves SpreadsheetBench success by 9.2 points over an initial-skill baseline.
- **Key Innovation**: Self-evolving memory *schema* (not just content) — the wiki's self-evolving-agent cluster gains a memory-OS instantiation.

### ReFind: When Your Agent Opens the Chat App — Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory
- **Authors**: Ruizhe Li, Licheng Zhang, Benfeng Xu, Mingxuan Du, Zheren Fu, Weidong Chen
- **Institution**: — (likely Alibaba)
- **Date**: 2026-08-13
- **Link**: [2608.12888](https://arxiv.org/abs/2608.12888)
- **Abstract**: Agent-memory systems buy retrieval quality with structure (summaries, embeddings, trees, knowledge graphs). **ReFind** asks how much of that benefit is the structure itself vs competent retrieval: it builds **no semantic structure** — archives stay unmodified, indexed lexically at turn granularity, with a generic iterative keyword-search loop plus four chat-native controls (session-aware rank fusion, local context expansion, temporal narrowing, skip-inspected-sessions), then a reasoning stage answers from collected evidence. Across ~2,800 questions (single/multi-hop QA, event ordering, fact consolidation) under MemoryAgentBench's incremental multi-turn setting, ReFind reaches the highest mean accuracy (58.2), above HippoRAG 2 (53.2), all under a GPT-4o-mini backbone. On LongMemEval-S/M it reaches 93.2±3.3 / 89.3±6.0 with GPT-5-mini.
- **Key Innovation**: An explicit anti-structure result — agent-controlled search over unmodified raw logs recovers much of the benefit credited to elaborate memory structure, with zero LLM-based index construction. A strong counterpoint to the wiki's graph/tree memory enthusiasm.

### SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback
- **Authors**: Qianxi Yan, Chunrong Chen, Jiuzhou Zhao, Min Zhang, Yongzhou Xu, Xiaochuan Xu
- **Institution**: — (likely HIT + industry)
- **Date**: 2026-08-13
- **Link**: [2608.13120](https://arxiv.org/abs/2608.13120)
- **Abstract**: Agent Skills are hand-authored or single-pass generated, with no closed loop for improvement; recent work closes the loop but only via single-turn QA evaluation — the evolution gradient decays after the first round patches single-exchange gaps, multi-turn defects stay invisible, and end-to-end scalar verification gates can't localize/repair structural causes. **SkillEvo** makes trustworthy feedback generate the gradient and controllable governance constrain its direction: multi-turn user simulation becomes a feedback generator (follow-up questions expose defects layer by layer), and an independent governance layer actively repairs factual degradation and structural bloat. Across six cloud-service categories, 9 production Skills, and 98 skill-reference files, SkillEvo beats self-reflection-based evolution by 23.0 points and single-turn-QA-driven evolution by 15.4.
- **Key Innovation**: Multi-turn interaction as a renewable evolution gradient with active governance — directly engages the wiki's skill-evolution line (Branch2Skill, DIVE, SkillEvo-style systems) and yesterday's Skill-induced-Failures critique.

### DIVE: Unlocking Self-Improvement in Frozen Language Models Through Diversity-Driven Skill Evolution
- **Authors**: Siheng Xiong, Ali Payani, Oguzhan Gungordu, Faramarz Fekri
- **Institution**: Georgia Tech (likely)
- **Date**: 2026-08-13
- **Link**: [2608.12486](https://arxiv.org/abs/2608.12486)
- **Abstract**: Frozen LLMs cannot retain post-deployment experience without parameter updates. **DIVE** evolves persistent natural-language skills from task experience and verifier feedback (reusable reasoning procedures, verification strategies, failure modes, output constraints), executed and revised by the same underlying model with no teacher. Because natural-language skill evolution is stochastic and non-convex, DIVE independently evolves multiple skill populations, refines them via diverse transformations, and jointly selects a complementary set. Across six math/logical reasoning tasks and multiple model families, DIVE beats reasoning methods, prompt optimization, skill frameworks, and memory baselines, with larger gains per rollout than SFT/GRPO and GEPA; skills transfer across scales (GPT-5-nano matches/beats GPT-5 under conventional prompting).
- **Key Innovation**: Diversity-population skill evolution as a parameter-free, transferable self-improvement route — a strong complement to the wiki's skill-evolution and GRPO-vs-prompt-optimization threads.

### Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories (QCR)
- **Authors**: Yifei Li, Heng Wang, Lingling Zhang, Muye Huang, Xinyu Zhang, Jiashuai Liu, Hang Yan, Rongman Xu
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12847](https://arxiv.org/abs/2608.12847)
- **Abstract**: Retrieval finds a past trajectory that *may* matter but doesn't say how to use it once users/entities/constraints/environment changed. The paper identifies post-retrieval reuse as a distinct bottleneck and builds an evaluation framework holding candidate retrieval, target state, model, decoding, and tool budget fixed. **QCR** is a deliberately simple target-bound note recording a reusable procedure, bindings to recover, applicability conditions, and verification requirements. Across 2,391 target instances (WebArena, WorkArena, AppWorld) QCR reaches 62.3% average Success — 10.7 points above Full Trajectory injection — using 48.9% fewer online tokens; summary reranking selects a reusable memory for 94.8% of targets within 1.8 points of an oracle selector. Direct trajectory injection loses utility as traces grow or source-specific values change.
- **Key Innovation**: Separates retrieval quality from the reuse problem, with evidence that target-bound notes beat raw trajectory injection — relevant to the wiki's trajectory-memory/reuse thread.

---

## 4. AI Scientists & Verified Reasoning

### Replica & Faraday: Training AI Scientists to Replicate Research
- **Authors**: Damon Falck, Samer Sabri, Anja Surina, Thom Foster, Anya Sims, Sam Devlin, Dylan Rogers, Tantum Collins, Kaloyan Aleksiev, Louis Kirsch, Edward Hughes
- **Institution**: — (likely Google DeepMind)
- **Date**: 2026-08-13
- **Link**: [2608.13331](https://arxiv.org/abs/2608.13331)
- **Abstract**: Replication illuminates underspecified details and requires hypothesis-driven exploration similar to open-ended research. The paper builds **Replica**, a scalable task space for paper replication with an auto-generated rubric-based judge (low noise, agrees with humans), and post-trains **Faraday**, a 27B "AI Scientist" agent that uses coding agents as tools, surpassing Claude Opus 4.8 and GPT-5.5 on held-out replication tasks. Qualitative analysis shows Faraday adopts a more scientifically-principled approach.
- **Key Innovation**: A scalable replication task space + a frontier-beating 27B replication agent — extends the wiki's AI-scientist line toward long-horizon scientific verification. (Repository-level verified code and search-efficiency benchmarks from this window are in [arxiv-ai-search](./arxiv-ai-search.md): Vero, TsuGO.)

---

## 5. World Models & Planning Diagnostics

### Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency (ACPC)
- **Authors**: Guo An, Zijing Wu, Honghua Dong, Yuhao Yan, Zixuan Gui, Haochong Chen, Shanzhao Ruan, Xiang Wang, Yurong Ling, Qi Tian
- **Institution**: — (likely UTSA/HKU-related group)
- **Date**: 2026-08-13
- **Link**: [2608.12939](https://arxiv.org/abs/2608.12939)
- **Abstract**: JEPAs predict in latent space rather than pixels, yet visual perturbations can still alter encoded representations and subsequent action-conditioned predictions. Guided by bisimulation (two observations are the same state iff their action-conditioned consequences agree), the paper introduces **Action-Conditioned Predictive Consistency (ACPC)** — how far a clean history and a visually perturbed view diverge after rolling forward under the same actions — and proves the divergence bounds perturbation-induced changes in multi-step prediction error and planner cost. Two measures follow: **Invariance Radius** (clean–perturbed rollout spread) and **Separation Rate** (distinguishability after rollout). On four visual control tasks, ACPC predicts perturbation-induced cost changes; the IR–SR screen transfers across tasks on LeWM and remains informative under blur/resize.
- **Key Innovation**: A theory-grounded diagnostic (with bounds) for latent world-model robustness to input perturbation — feeds the wiki's JEPA/world-model evaluation thread (LeWorldModel reproduction line).

### The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use
- **Authors**: Joyjeet Singh
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12959](https://arxiv.org/abs/2608.12959)
- **Abstract**: Latent world models are judged by prediction quality, so when long-horizon planning fails the natural reading is predictor degradation. On a reproduction of LeWorldModel on TwoRoom, the paper shows the binding constraint is the **planner's objective**: the predictor's imagined state at +75 steps is only 0.189 as wrong as assuming the world froze, while the planner never imagines beyond +25; squared-latent-distance CEM planning tracks true distance at r=0.426, saturates ~80 arena units, and *decreases* past 120 — so moving away from the goal can lower cost. A ridge probe recovers position from the frozen embedding (R² 0.9922). Replacing only the objective lifts goals reached at offset 100 from 26.0% to 98.0% and reaches 92.0% under a third of the budget; a frame-separation head that predicts spatial distance worse (r=0.819 vs 0.9897) plans better — it has learned *reachability*, not proximity. The pathology holds on the authors' released weights and across four checkpoints.
- **Key Innovation**: A decisive planner-objective negative result that directly engages and qualifies the wiki's LeWorldModel reproduction ([08-12 game-rl-daily](../2026-08-12/game-rl-daily.md)) — predictor quality is not the bottleneck; cost-function geometry is. (⚠️ different conclusion from the prior reproduction's "predictor degrades" framing — worth flagging in both pages.)

---

## 6. Recommendation, Retrieval & Advertising

### Structure then Query: Enabling Precise Analytical Queries over Unstructured Documents (AnnoIndex)
- **Authors**: Teng Lin, Yuyu Luo, Nan Tang
- **Institution**: — (likely CUHK-Shenzhen)
- **Date**: 2026-08-13
- **Link**: [2608.13384](https://arxiv.org/abs/2608.13384)
- **Abstract**: Vector-similarity fuzzy matching can't support precise structured analysis over unstructured text. **AnnoIndex** adds two components: an **Annotation Index** (SchemaLoop auto-creates hierarchical annotation schemas from the corpus; a lightweight LM extracts values, materializing a structured index that amortizes extraction cost into a one-time build) and a **Structured Query Engine** (compiles questions into SQL-extension execution plans, filtering precisely via the index first, then applying extraction in ascending cost order, using LLMs only on the minimal remaining fraction; extracted attributes feed back into the index). On three real-world datasets AnnoIndex achieves the highest average F1 (0.87) with robust performance on multi-hop joins and progressive reasoning queries.
- **Key Innovation**: Materialized-annotation indexing for precise analytical queries over documents — a complementary "structure-first" alternative to the wiki's vector-RAG and document-analytics threads (cf. agentic-BM25 results like ReFind).

### When Can You Trust Offline Evaluation of Equal-Cost Top-k Allocation? A Controlled, Reproducible Benchmark and Practitioner's Guide
- **Authors**: Binshuang Li
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12489](https://arxiv.org/abs/2608.12489)
- **Abstract**: Off-policy evaluation promises to estimate what a targeting rule would have earned, but a deployable deterministic top-k policy removes all averaging over actions, so weak overlap hits the estimate directly. Benchmarked across six estimators, five datasets, and two known-effect sweeps against a non-simulated paired reference: (1) weak overlap is governed by logger–target *action alignment*, not logging sharpness; effective sample size ranks risk across logging environments but is weak within a single log; (2) the optimizer's curse is not fixed by cross-fitting the outcome nuisance — honest policy-level splitting avoids reuse bias by changing the estimand; (3) propensity-estimation error is the largest degradation measured (out-of-fold estimates hurt IPS more than any other stress, leave DR almost unchanged, and can invert the overlap diagnostic). All failures occur with bounded weights (propensities floored at 0.02); benchmark released with public data only.
- **Key Innovation**: A controlled, reproducible map of when top-k OPE fails — measurement hygiene for the wiki's off-policy evaluation / uplift-allocation line. (The window's rec/CTR/CVR cluster — STAR, FSGR, Doubly-Robust-CVR, DrEM, DrIG, DTAMLP — is in [arxiv-ai-search](./arxiv-ai-search.md).)

---

## 7. Time Series, Forecasting & Finance

### SsPCA-MIDAS: Supervised Mixed-Frequency Learning for Macro-Financial Forecasting When Factors are Weak
- **Authors**: Ulrich Hounyo, Zhendong Li
- **Institution**: U Albany (likely)
- **Date**: 2026-08-13
- **Link**: [2608.12589](https://arxiv.org/abs/2608.12589)
- **Abstract**: Factor-MIDAS regressions extract common factors from high-frequency predictors via PCA, which relies on factor pervasiveness often violated in macro-financial forecasting. **SsPCA-MIDAS** integrates supervised scaled PCA into mixed-data sampling, with consistency and asymptotic normality under weak factors (enabling inference on the prediction target). Simulations show it outperforms PCA-based and supervised competitors especially when weak factors prevail, and boosting the cleaner extracted factors yields further gains. In U.S. macro-financial applications it selects economically meaningful predictors and improves forecasts of GDP, inflation, unemployment, asset prices, and volatility.
- **Key Innovation**: Weak-factor-robust supervised factor extraction for mixed-frequency forecasting — statistical rigor for the wiki's macro-financial forecasting thread.

### FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching
- **Authors**: Zhuohan Wang, Andreea Bacalum, Ollie Olby, Carmine Ventre, Namid Stillman
- **Institution**: KCL (likely)
- **Date**: 2026-08-13
- **Link**: [2608.13096](https://arxiv.org/abs/2608.13096)
- **Abstract**: LOB simulators need realistic dynamics, efficient sampling, controllable scenarios, and generalization to unseen instruments — which agent-based and deep generative simulators provide only partially. **FlowLOB** is a conditional flow-matching generator of LOB trajectories trained on multiple HKEX symbols at 0.1s/1s/10s in tick-relative representation, transferring zero-shot to unseen instruments. Because flow and diffusion share a formulation, both are trained with identical data/architecture/budget and sampled via the same fixed-step ODE solvers: flow matching attains its best quality at only 10 solver steps while diffusion needs many more; at that operating point FlowLOB improves realism over two learned and two agent-based baselines on most distributional metrics at the finer frequencies, satisfies a counterfactual controllability criterion in most settings, and both realism and control transfer zero-shot to a held-out symbol.
- **Key Innovation**: A controlled flow-vs-diffusion comparison plus an efficient, controllable LOB generator — relevant to the wiki's market-simulation/generative-finance line.

### The Time Value of Evolution: Lineage-Value Policy Gradients for Trading Policy Discovery
- **Authors**: Matthew Siper, Ahmed Khalifa, Julian Togelius
- **Institution**: NYU (likely)
- **Date**: 2026-08-13
- **Link**: [2608.13297](https://arxiv.org/abs/2608.13297)
- **Abstract**: In evolutionary search, a weak child can be a valuable ancestor that opens high-fitness regions; immediate-return control is blind to this delayed utility. The paper formalizes this as the **time value of evolution** within a finite-horizon MDP and introduces **Lineage-Value Policy Gradients (LVPG)**, a long-horizon actor-critic for automated trading policy discovery: a bootstrapped critic head estimates finite-horizon lineage potential from multi-step mutation trees, while an actor head modulates mutation intensity over the remaining search budget. Across 90 paired runs (matched operators, lineage supervision, folds, seeds, budgets), path-based credit assignment increases validation best-so-far AUC by 0.394 Sharpe units, produces fewer temporary regressions, and recovers from them more often.
- **Key Innovation**: Long-horizon credit assignment for evolutionary search with a clean paired experiment — connects the wiki's evolutionary-search and trading-policy threads.

### Defensive Boosting for Online Probabilistic Forecasting
- **Authors**: Georgy Noarov, Aaron Roth
- **Institution**: UPenn (likely)
- **Date**: 2026-08-13
- **Link**: [2608.13554](https://arxiv.org/abs/2608.13554)
- **Abstract**: Online gradient boosting competes in Brier score with the span-of-H predictor on every sequence but promises nothing when the span lacks an accurate predictor; online weak-to-strong boosting drives error to zero under a weak-learning condition but promises little when it fails. The **Defensive Booster** obtains both guarantees simultaneously: on every adaptive sequence it is Brier-competitive at the online gradient boosting rate, and whenever the realized transcript satisfies the smooth weak-learning condition it matches online classification boosting's Brier/error rate. This is achieved by operationalizing boosting's "dual view" — persistent high randomized classification error yields a smooth reweighting where every weak hypothesis has low edge (an ex-post hard-core certificate that weak learning fails). It accesses only one weak-class learner (vs large ensembles in prior methods) and matches/beats baselines at orders-of-magnitude faster runtime; a strongly adaptive variant satisfies both guarantees on every interval.
- **Key Innovation**: A single efficient algorithm unifying two incomparable online-forecasting guarantees — a clean theory contribution for the wiki's online-learning/probabilistic-forecasting thread (stat.ML).

---

## 8. Inference Efficiency: Pruning, Decoding & Diffusion Caching

### SNIPER: Unifying Depth and Width Pruning for LLMs via Binary Knapsack Optimization
- **Authors**: Palaash Goel, Ayan Sengupta, Akshay Nambi, Tanmoy Chakraborty
- **Institution**: IIIT Delhi (likely)
- **Date**: 2026-08-13
- **Link**: [2608.12953](https://arxiv.org/abs/2608.12953)
- **Abstract**: Structured pruning relies on greedy heuristics that make myopic decisions and miss target compression budgets. **SNIPER** solves a knapsack optimization over coarse-granularity components (conditionally optimal parameter allocation under fixed importance estimates) followed by fine-grained pruning to meet strict budgets. They introduce the **Compression Ratio Adherence Factor (CRAFT)** to quantify budget fidelity: existing pruners deviate up to 33% from target ratios while SNIPER achieves near-exact adherence (CRAFT 0.98). Across four architectures and 18 tasks over five domains, SNIPER beats six SOTA pruners on average performance retention and task-level stability, with a mean rank of 1.25.
- **Key Innovation**: Optimal (knapsack) rather than greedy budget allocation plus a budget-fidelity metric — upgrades the wiki's structured-pruning line with optimization-based allocation.

### Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference (RMM)
- **Authors**: Zixuan Lan, Yanhong Li, Jiawei Zhou
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.13426](https://arxiv.org/abs/2608.13426)
- **Abstract**: **RMM** is a training-free, input-adaptive method that reduces Transformer matrix products by selecting informative slices along their contraction dimensions (no weight changes), under a simple retention-ratio control giving a smooth accuracy–efficiency trade-off. Across 1B–70B models, reduction tolerance depends on family, task, component, and retention ratio but often improves with scale; moderate reduction stays robust across discriminative, generative, and long-context settings and extends to multimodal inference. Mechanistic ablations reveal a structural asymmetry — attention-side computations are substantially more reducible than MLPs. Wall-clock benchmarks on an A100 confirm runtime gains, especially at longer sequences.
- **Key Innovation**: Input-adaptive contraction-dimension pruning as a training-free inference optimization, with an MLP-vs-attention reducibility asymmetry — complements the wiki's inference-time-optimization line.

### DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees
- **Authors**: Tianyi Li, Yaxin Luo, Xinyi Shang, Zhiqiang Shen
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.13524](https://arxiv.org/abs/2608.13524)
- **Abstract**: Diffusion-based drafters predict an entire token block in parallel but their position-wise distributions are marginal, not conditioned on tokens along each draft path. **DARTree** is a training-free method extending a pretrained AR correction head from chains to trees: it builds a fixed-width candidate tree by expanding and scoring all nodes per depth in a single batch, then applies best-first pruning to select the verification tree, decoupling AR-head inference from sequential heap operations. Across seven math/code/chat benchmarks it achieves the highest average acceptance length and speedup in all four model–temperature configs, accepting up to 12.97 tokens per round (98.6% more than DFlash, 27.9% more than Domino) and reaching up to 9.73× lossless speedup.
- **Key Innovation**: Tree-structured speculative diffusion decoding with a training-free AR correction head — extends the wiki's speculative-decoding cluster (diffusion drafters, DFlash/Domino lineage) to candidate trees.

### GCache: From Local Mismatch to Global Impact — Optimizing Cache Reuse Policy for Efficient Diffusion
- **Authors**: Xichen Ye, Yifan Wu, Zhikang Xie, Xiangyu Yue, Cheng Jin, Weizhong Zhang
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.13043](https://arxiv.org/abs/2608.13043)
- **Abstract**: Cache-based diffusion acceleration uses local similarity heuristics misaligned with final generation quality because error propagates and accumulates non-uniformly along the denoising trajectory. **GCache** establishes a theoretical error-propagation upper bound, reparameterizes the exponent in Bernstein form (since the bound is conservative for non-convex models), and reformulates cache-policy search as bilevel optimization — optimal reuse policy in the inner objective, error-weighting aligned with generation-quality loss in the outer. GCache outperforms prior caching on both image and video generation; on Wan2.1 it maintains a 2.17× speedup while improving quality (LPIPS 0.1095 → 0.0316).
- **Key Innovation**: Quality-aligned global cache policy for diffusion — connects the wiki's diffusion-acceleration line (OnlineCache, cache-based methods) with principled error-propagation accounting. (KV-cache virtualization and quantization from this window are in [arxiv-ai-search](./arxiv-ai-search.md): vToken, RoPE-Q/K rotations.)

---

## 9. Games, Multi-Agent & Mechanism Design

### E2-Explainer: Discovering Efficient and Explainable Communication Topologies for LLM-based MAS via Causal Inference
- **Authors**: Junzhi Li, Peng He, Qirui Ji, Wei Wang, Lixiang Liu, Chuxiong Sun
- **Institution**: BUPT (likely)
- **Date**: 2026-08-13
- **Link**: [2608.12921](https://arxiv.org/abs/2608.12921)
- **Abstract**: LLM multi-agent systems depend on communication topologies, but existing generators learn them via black-box reward-driven optimization with no insight into why specific edges matter. **E2-Explainer** frames topology explanation as causal attribution: it identifies compact communication subgraphs supported by edge-level evidence of task preservation, using a Granger-style objective measuring how masking each channel changes the task outcome and response stability; budgeted subgraphs are distilled into an amortized explainer for efficient post-hoc explanation. On reasoning and coding benchmarks it identifies critical subgraphs that preserve collaboration, and the subgraphs can be executed directly to prune redundant edges, cutting communication costs while keeping task performance.
- **Key Innovation**: Causal, explainable MAS topology pruning — complements the wiki's MAS-communication and explainability threads with a Granger-style attribution method.

### Entropy-Augmented Multi-Objective Policy Optimization in Multiagent Systems
- **Authors**: Jamie Santos, Ayhan Alp Aydeniz, Raghav Thakar, Kagan Tumer
- **Institution**: OSU (likely)
- **Date**: 2026-08-13
- **Link**: [2608.12534](https://arxiv.org/abs/2608.12534)
- **Abstract**: Multi-objective evolutionary algorithms like NSGA-II optimize diversity in objective space but neglect behavior-space diversity, risking premature convergence and behavioral collapse. The paper adds an **entropy bonus to agent fitness** to discourage behavioral homogeneity across the population while preserving the Pareto framework. In rover-domain experiments with qualitatively distinct reward structures, hypervolume improves by up to 48% vs NSGA-II — behavioral diversity is a promising, underexplored direction for multi-objective multiagent evolution.
- **Key Innovation**: Behavior-space entropy as a cheap Pareto-preserving diversity signal — relevant to the wiki's multi-objective evolutionary / multiagent threads (cf. LVPG's lineage-value angle this window).

### A Repeated-Game Framework for Incentives in Decentralized Infrastructure Protocols (DePIN)
- **Authors**: Mustafa Qazi
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12576](https://arxiv.org/abs/2608.12576)
- **Abstract**: The paper models quality control in Decentralized Physical Infrastructure Networks as a repeated moral-hazard problem between protocol and provider, with compliance enforced by slashing posted collateral and the discounted threat of demotion on a reputation ladder. The main contribution is the **deterrence ratio Γ** — the worst-case ratio of a deviation's private gain to its marginal probability of detection. Key result: if any profitable deviation does not increase fail probability relative to compliance, binary public-outcome protocols cannot deter it; when all profitable deviations have positive detection gaps and no weakly-costlier action is less likely to fail, compliance is sequentially incentive compatible iff immediate slashing plus discounted reputation loss ≥ Γ at every tier. This yields a design problem mapping service primitives to stake requirements, reward schedules, probation rules, and audit frequency.
- **Key Innovation**: A sequential-incentive framework with a computable deterrence condition for DePIN — extends the wiki's mechanism-design/economics line into decentralized infrastructure. (The window's Nash-coordination and LLM-economics/mechanism papers — Do LLMs Beat Nash?, EA-RAM, Keep/Customize/Exit — are in [arxiv-ai-search](./arxiv-ai-search.md).)

---

## 10. Models, Open Weights & AI Culture

### DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data
- **Authors**: Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina, Kenneth Enevoldsen, Lukas Galke Poech
- **Institution**: SDU / Danish Foundation Models (likely)
- **Date**: 2026-08-13
- **Link**: [2608.13517](https://arxiv.org/abs/2608.13517)
- **Abstract**: Frontier LLM development relies on massive, often non-permissible datasets, excluding researchers committed to ethically sourced data. **Mimir v1** is a 1B-parameter Hierarchical Reasoning Model (HRM) trained from scratch on a mixture of 161 datasets using **only permissible post-training data**: it outperforms the original HRM-Text 1B, competes with larger models (Qwen 3.5 4B, Gemma 4 E2B) across 20 English/Math/Code benchmarks, and sets a new SOTA for Danish. Released on the Hugging Face Hub.
- **Key Innovation**: Frontier-competitive performance at 1B under a permissible-data constraint, with a Danish SOTA — a data-sovereignty datapoint for the wiki's open-models line (DFM/European AI thread).

### Novels generated by language models show compressed formal variation
- **Authors**: Mehdy Sedaghat Payam, Justin Quinn
- **Institution**: —
- **Date**: 2026-08-13
- **Link**: [2608.12630](https://arxiv.org/abs/2608.12630)
- **Abstract**: Rather than asking whether individual passages are AI-generated, the study asks whether repeated AI generation can reproduce the range of diversity found across human corpora. Six corpora (twenty novels each by GPT-5.5 Thinking and Qwen3-14B in a 19th-century British realist style and a contemporary zero style; 205 19th-century human novels; 65 contemporary human zero-style novels) are measured at document level (MATTR-500, Shannon entropy, avg sentence length, readability, punctuation rate). The most robust finding is **compression of sentence structure**: repeated generations vary far less in sentence structure than human novels, with similar compression in readability, punctuation, and within-novel sentence-length variability; lexical measures are mostly compressed too. Individual AI novels may resemble human fiction stylistically while a collection occupies a much narrower formal range — distinguishing *variance overclosure* from *correlational overclosure*.
- **Key Innovation**: A corpus-level "diversity compression" result for generative fiction — an evaluation angle for the wiki's creative-generation and LLM-diversity threads.

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Agent memory splits into "no-structure + control" and "cheap-structure + association" camps** | ReFind shows agent-controlled search over unmodified raw chat logs beats graph/tree memory (58.2 vs HippoRAG 2's 53.2, zero index construction); RippleMem adds associative expansion over event graphs at ~30× lower construction cost; LycheeMemory V2 sets granularity-of-consolidation as the efficiency axis; QCR shows target-bound notes beat raw trajectory injection (62.3% vs 51.6%, −48.9% tokens) | ReFind, RippleMem, LycheeMemory V2, QCR |
| **Skill evolution is scrutinized for safety, gradients, and diversity** | Practice Makes Unsafe formalizes skill misevolution and ships SafeEvolve (carryover ASR 16→35.3% without, cut with repair); SkillEvo renews the evolution gradient from multi-turn feedback (+23.0 vs self-reflection); DIVE shows diversity-population evolution as a parameter-free self-improvement route; MindMemOS evolves memory schemas and skills jointly | SkillMisevo, SkillEvo, DIVE, MindMemOS |
| **Self-distillation converges on "when to trust the teacher"** | I-SDPO routes GRPO-vs-SDPO per instance keyed to group success, with an optimization-bias-floor analysis (SciKnowEval mean@16 56.67→70.31); the sibling [arxiv-ai-search](./arxiv-ai-search.md) contributes CROP (task-relevance selection), LOPD (learnable privileged context), CrEST (magnitude-not-direction teacher) — together this window maps the full OPD supervision design space | I-SDPO (+ CROP/LOPD/CrEST in ai-search) |
| **World-model evaluation turns on planner/objective geometry** | Objective-Is-The-Bottleneck shows TwoRoom planning failures stem from the CEM cost function (squared latent distance saturates and inverts), not the predictor — qualifying the wiki's LeWorldModel reproduction; ACPC bounds perturbation-induced cost changes for JEPA world models and ships an IR–SR diagnostic screen | Objective-Is-The-Bottleneck, ACPC |
| **Inference efficiency hits pruning, decoding, and caching from orthogonal angles** | SNIPER replaces greedy pruning with knapsack-optimal allocation (CRAFT budget fidelity 0.98); RMM input-adaptively prunes contraction dimensions (attention more reducible than MLP); DARTree extends speculative decoding to AR draft trees (up to 9.73×); GCache aligns diffusion caching with generation quality (Wan2.1 LPIPS 0.1095→0.0316 at 2.17×) | SNIPER, RMM, DARTree, GCache |
| **AI-scientist replication crosses the frontier threshold** | Faraday, a 27B replication agent trained on the rubric-judged Replica space, beats Claude Opus 4.8 and GPT-5.5 on held-out replication tasks; Vero (sibling page) shows repository-level verified synthesis caps at 27/43 for the strongest agent — verification and replication are now first-class, measurable agent tasks | Faraday/Replica (+ Vero in ai-search) |
| **Forecasting and market generation add rigor at the modeling layer** | SsPCA-MIDAS gives weak-factor-robust supervised factor extraction for macro-financial forecasting; FlowLOB provides a controlled flow-vs-diffusion comparison with a counterfactual-controllability criterion for LOB generation; Defensive Boosting unifies two incomparable online-forecasting guarantees in one efficient algorithm | SsPCA-MIDAS, FlowLOB, Defensive Boosting |
| **Multi-agent and mechanism design diversify beyond game theory** | E2-Explainer prunes MAS communication topologies causally (Granger-style edge evidence); Entropy-Augmented MO adds behavior-space entropy to Pareto evolution (+48% hypervolume); the DePIN repeated-game framework gives a deterrence-ratio incentive condition for decentralized infrastructure | E2-Explainer, Entropy-Augmented MO, DePIN |

---

## Key Takeaways

1. **This window's digest is a memory-and-skills day — and the "structure-first" premise of agent memory is under direct attack.** ReFind's anti-structure result (raw-log lexical search + agent control beating HippoRAG 2) is the sharpest challenge yet to the graph/tree memory consensus; RippleMem and LycheeMemory V2 counter that structure can be made cheap (30× construction savings, 86% token cuts) if consolidation granularity is right; QCR moves the argument from *finding* trajectories to *reusing* them safely. Read together with SkillMisevo's lifecycle-safety framing, the message is: memory and skills need controlled retrieval *and* controlled writes.
2. **Skill evolution now carries measured risk and measured gradients.** Practice Makes Unsafe is the first lifecycle-safety formalization (all 21 evolved configs author unsafe artifacts; malicious exposure raises carryover ASR from 16% to 35.3%), while SkillEvo and DIVE attack the complementary problem of a decaying evolution gradient. Combined with yesterday's "Agent Skills Can Be Harmful," skill-autonomy claims can no longer be evaluated on task accuracy alone.
3. **The OPD/supervision debate bifurcates into "what to supervise" and "who supplies it."** This digest holds I-SDPO (capability-dependent GRPO/SDPO routing); the sibling page holds CROP (task-relevance selection), LOPD (fully-learnable privileged context), and CrEST (verifier-bounded magnitude modulation). Across both pages, four papers in one window converge on dense, verifier-anchored, artifact-minimal credit assignment — the wiki's OPD thread should read them as one cluster.
4. **World-model diagnostics are saying "check the planner, not the predictor."** Objective-Is-The-Bottleneck (cost geometry saturating/inverting) directly qualifies the 08-12 LeWorldModel reproduction's "predictor degrades" reading, and ACPC gives JEPA-style models a provable robustness bound for the same question. These two belong flagged as a cross-page contradiction for the world-model thread.
5. **Efficiency keeps finding orthogonal wins to the KV-cache work.** vToken and RoPE-quantization (sibling page) fix granularity/scale-statistic mismatches; here, SNIPER optimizes pruning budgets, RMM prunes contraction dimensions input-adaptively, DARTree goes from chains to trees in speculative decoding, and GCache aligns diffusion caching with final quality — each a different axis of "decide where to spend compute."
6. **Measurement is the recurring theme across domains.** Replica/Faraday makes replication a scalable, rubric-judged task; the top-k OPE paper maps exactly when offline evaluation of targeting rules can be trusted; TsuGO (sibling) adds search organization as a measurable reasoning dimension; the Novels study measures *corpus-level* diversity compression rather than single-passage AI detection. The field is shipping benchmarks faster than results.

> ⚠️ Note on sourcing: this digest curates the **Fri Aug 14, 2026 announced window — Thu Aug 13 submissions (IDs ~2608.124xx–2608.135xx)**, harvested from the `/list/{cat}/recent` pages for cs.AI (204), cs.LG (157), cs.CL (101), cs.IR (19), cs.GT (6), cs.MA (14), econ.TH (6), stat.ML (29) — 536 entries. All 32 shortlisted arXiv IDs are **grep-verified absent from the entire wiki** (0 hits; the 08-13 digest's window ended at ~2608.12307). **18 IDs overlapping the same-day [arxiv-ai-search](./arxiv-ai-search.md) were removed rather than duplicated** (CROP, LOPD, CrEST, Post-Norm depth growing, SPP, Vero, TsuGO, STAR, Doubly-Robust-CVR, FSGR, DrEM, DrIG, ORBIT, vToken, RoPE-Q/K rotations, Do-LLMs-Beat-Nash, EA-RAM, Keep/Customize-Exit), as was [AlayaWorld v1.1](https://arxiv.org/abs/2608.13492) (already covered). Institutions marked "(likely)" are inferred from author affiliations or prior knowledge, not always the arXiv record; "—" means not identified. Cross-reference: the **Objective-Is-The-Bottleneck** paper engages the LeWorldModel/TwoRoom reproduction in [08-12 game-rl-daily](../2026-08-12/game-rl-daily.md) with a *different* conclusion (planner objective vs predictor), flagged above for reconciliation.
