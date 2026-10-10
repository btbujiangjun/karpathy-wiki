---
title: ArXiv Paper Check — AI & CTR (2026-10-10)
type: synthesis
created: 2026-10-10
updated: 2026-10-10
sources: []
tags: [arxiv, arxiv-paper-check, daily-check, ai, ctr, recommendation, ads, ir, retrieval, on-policy-distillation, self-improvement, reasoning-rl, kv-cache, world-action-models, agents, guardrails, evaluation-validity, sibling-collision, daily-digest]
---

# ArXiv Paper Check — AI & CTR (2026-10-10)

**Search**: arXiv export API over HTTPS, category sweeps (`cat:cs.AI`, `cat:cs.LG`, `cat:cs.CL`, `cat:cs.IR`, 2 pages each) restricted to `submittedDate:[202610080000 TO 202610102359]`, `sortBy=submittedDate desc`, plus 23 topical `all:` passes (`"click-through rate"`, `CTR`, `advertising`, `"sponsored search"`, `"ad auction"`, `"recommender system(s)"`, `"sequential recommendation"`, `"generative recommendation"`, `"feature interaction"`, `"multi-interest"`, `"user response prediction"`, `"search ranking"`, `"item recommendation"`, `counterfactual` + recommender, `"ad ranking"`, `"ad relevance"`, `"embedding bag"`, `"short video"` + recommend, `"retrieval-augmented"` + ranking, `LLM` + advertising, `"preference optimization"` + recommend). **478 harvested raw entries → 478 unique papers, all `published = 2026-10-08`.**

⚠️ **Window framing, stated up front**: this is the **2026-10-08 submission/announcement block**, a **single-day window**, not a rolling 24 hours — arXiv's newest available block at run time (`submittedDate:[202610090000 TO 202610102359]` returns nothing). The same finding is recorded by the same-day `arxiv-daily` sibling.

⚠️ **★ Headline: the CTR / advertising lane is completely empty in this block — zero papers.** Full-batch regex sweeps of the 478 abstracts return **0 hits for `click-through` / `click through` / `clickthrough`, and 0 relevant hits for `advertis`** (the two `advertis` matches are a cycling-safety IoT paper and a text-to-image bias paper). This is the first fully-zero CTR yield in this series and the strongest instance yet of the "supply is genuinely thin" note carried since 10-07/10-08. There is **no new CTR-prediction architecture**, and — unlike 10-07/10-08 — not even an ads/recsys methodology-audit paper to fill the lane. The recsys/IR content that does exist is concentrated in retrieval, and most of it was claimed by the same-day sibling (below).

⚠️ **Sibling-collision day (per the standing 10-07/10-08 precedent "withdrawn, not merged")**: the same-day `2026-10-10/arxiv-daily.md` sibling was written *during* this run (10:32) and independently claimed **10 of this run's original selections** — **4 primary** (`2610.12300` learned-sparse-retrieval indexes, `2610.11816` mixed-modality retriever modality preference, `2610.11666` Autoregressive Retriever, `2610.11128` reference-guided vs free rollout generation) and **6 from the "also worth recording" set** (`2610.12360`, `2610.12444`, `2610.11750`, `2610.11063`, `2610.12304`, `2610.11765`). All 10 were **withdrawn and replaced with fresh, 0-hit papers**, and the full featured slate re-verified `rg -l` 0-hit against the live wiki immediately before writing. This is the **fifth same-day sibling collision documented in the last eight daily runs and the third consecutive day** — the shared claimed-ID lock file remains the standing ask.

**Dedup baseline**: 8,535 unique arXiv IDs regex-extracted from `wiki/**/*.md` (including the same-day sibling `2026-10-10/arxiv-daily.md`). **413 / 478 window papers unclaimed.** **15 papers featured** (3 IR/retrieval + 12 core AI); all 15 IDs re-verified 0-hit immediately before writing.

---

## Interesting Papers

### IR / Retrieval lane

Three papers. The citable framing is **retrieval failure-mode diagnosis, not new retrieval methods** — a direct echo of the 10-08 CTR-lane "methodology-audit day." ⚠️ The three strongest *method* papers in the block (learned-sparse index compression `2610.12300`, mixed-modality retriever bias `2610.11816`, item-feedback query refinement `2610.11666`) are **sibling-claimed and therefore withdrawn here** (see header).

---

#### 1. [Beyond Resolution: Object-to-Image Ratio Mismatch in Instance Retrieval](https://arxiv.org/abs/2610.11489)

- **ID**: `2610.11489v1` | **Cat**: cs.CV | **Submitted**: 2026-10-08 | **Comment**: 24 pages. Preprint, under review
- **Authors**: Boaz Meivar, Ofir Kedem, Amit Edenzon, Gal Chechik, Shai Avidan
- **Affiliations**: **Tel Aviv University**; **Bar-Ilan University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.11489)

**Key contributions:**
- Isolates why visual instance retrieval fails when the same object appears at different apparent sizes: the dominant cause is usually **object-to-image (O2I) ratio mismatch** (the object occupies different image fractions), **not resolution loss**
- Controlled benchmark of **3,021 Objaverse objects rendered at five camera distances**: for **9 of 12** pretrained backbones, **>80%** of cross-distance degradation is attributable to O2I mismatch; multi-scale architectures cut the resolution-only effect to single digits yet **remain equally susceptible** to O2I
- The failure is **asymmetric**: tight queries retrieve more reliably against wide gallery images than the reverse
- Guided by the analysis, **query-side scale augmentation** + an OWLv2-based component improve robustness

**Notes:** A clean, controlled "the metric you blame is not the cause" result. The asymmetry (tight→wide beats wide→tight) is the reusable diagnostic, and it transfers to any embedding-based retrieval/matching stack that pools regions at fixed resolution.

---

#### 2. [RAG-Stress: Probing the Limits of Evidence Reliance in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.11183)

- **ID**: `2610.11183v1` | **Cat**: cs.CL | **Submitted**: 2026-10-08
- **Authors**: Shunyuan Zhou, Hao Chen, Tianyu Wang, Goose Lin, Zaiyuan Wang, Haiying Zhao
- **Affiliation**: **Beijing University of Posts and Telecommunications** (Beijing Key Lab of AI+ Domain Applications; co-listed North China University of Technology / Humanlaya Data)
- **PDF**: [Link](https://arxiv.org/pdf/2610.11183)

**Key contributions:**
- Names a failure standard accuracy hides: following retrieved evidence does **not** guarantee correctness — misleading evidence can make a model **replace an answer it previously gave correctly**
- **RAG-Stress** controlled diagnostic: hold question + reference answer fixed, edit **one assertion** to support a designated incorrect answer, and cross **two source-priority policies** with **three answer-span positions**
- Reports a **misleading rate (MR)** computed only on each model's subset of questions answered correctly without retrieval, alongside clean accuracy on the full set — separating **answer replacement** from pre-existing errors

**Notes:** The measurement contribution is the MR statistic: it turns "RAG made it worse" into a per-model quantity with a clean denominator. Directly relevant to this wiki's recurring "reported ≠ verified" arc and to any RAG evaluation stack that reports accuracy alone.

---

#### 3. [Overview of the NTCIR-19 Automatic Evaluation of LLMs 2 (AEOLLM-2) Task](https://arxiv.org/abs/2610.11598)

- **ID**: `2610.11598v1` | **Cat**: cs.IR | **Submitted**: 2026-10-08 | **Comment**: NTCIR-19
- **Authors**: Junjie Chen, Yuxi Dong, Haitao Li, Yiqun Liu, Qingyao Ai
- **Affiliations**: **Tsinghua University** (DCST + Quan Cheng Laboratory); **University of Science and Technology Beijing**
- **PDF**: [Link](https://arxiv.org/pdf/2610.11598)

**Key contributions:**
- IR-evaluation task overview for NTCIR-19, continuing AEOLLM with a **new "Deep Research Evaluation" subtask**: automatic evaluation of **long-form deep-research reports** generated by LLMs
- Participants' evaluation methods are scored by agreement with **human-annotated ground-truth labels**
- **91 runs from 10 teams**; documents the task design, data, and pooled results

**Notes:** The IR-lane anchor in an otherwise method-free lane. It sits squarely on the wiki's **LLM-as-judge / automated-evaluation** thread (cf. 10-07 LLM-judge integrity, 10-08 backbone evolution, judge-error UQ): the community is now formalizing automatic evaluation of *long-form research output*, where the ground truth is human annotation.

---

### Core AI lane

Twelve papers in four clusters: **(a) on-policy distillation — a third consecutive window, now splitting into efficiency / auditing / recovery axes** (papers 4–6); **(b) reasoning-RL and self-improvement training loops** (papers 7–9); **(c) KV-cache / serving for multi-model and world-action systems** (papers 10–11); **(d) agent/evaluation validity** (papers 12–15).

---

#### 4. [DIAL-OPD: Learning More from Fewer Tokens in On-Policy Distillation](https://arxiv.org/abs/2610.11659)

- **ID**: `2610.11659v1` | **Cat**: cs.CL | **Submitted**: 2026-10-08
- **Authors**: Anhao Zhao, Haoran Xin, Junlong Tong, Yingqi Fan, Xuan Lu, Ping Nie, Wenjie Li, Xiaoyu Shen
- **Affiliations**: **Eastern Institute of Technology, Ningbo (EIT-NLP)**; **The Hong Kong Polytechnic University**; **HKUST (Guangzhou)**; **Shanghai Jiao Tong University**; **University of Hong Kong**; **University of Waterloo**
- **PDF**: [Link](https://arxiv.org/pdf/2610.11659)

**Key contributions:**
- Contrarian observation: **training on fewer tokens can outperform full-token OPD** — more supervision does not monotonically help
- Diagnoses that existing disagreement-based token-selection criteria ignore **probability scale**: tokens assigned negligible probability by *both* models ("low-low" tokens) can receive **large log-ratio rewards** and hinder learning
- **DIAL-OPD** selects tokens by learning value, weighting reward magnitude by the **logarithmic mean of teacher and student probabilities** (parameter β controls the weighting); retains the highest-scoring tokens
- Evaluated across **4 teacher–student pairs and 7 mathematical reasoning benchmarks**

**Notes:** The OPD cluster's newest axis is **which tokens carry signal** — consistent with the wiki's OPD thread (10-06 drift, 10-07 security/stability/signal/reliability, 10-08 skills-not-knowledge / delta-teacher / student-visited states). "Low-low tokens can dominate the update" is a mechanism-level claim worth carrying forward.

---

#### 5. [Policy Alignment: New Signals for Membership Auditing in On-Policy Distillation](https://arxiv.org/abs/2610.11423)

- **ID**: `2610.11423v1` | **Cat**: cs.LG | **Submitted**: 2026-10-08 | **Comment**: 10 pages, 8 figures
- **Authors**: Yilong Yang, Wenzhuo Shang, Yule Liu, Jiale Teng, Zhuo Ma
- **Affiliation**: ⚠️ **not printed on the arXiv author block** (author names + corresponding marker only)
- **PDF**: [Link](https://arxiv.org/pdf/2610.11423)

**Key contributions:**
- OPD places the student policy **on the teacher's direction on private distillation prompts**, creating a need for **prompt-level membership auditing**
- Existing auditing signals are likelihood confidence or checkpoint-to-checkpoint student drift; neither captures the **teacher-induced direction** of the update
- **PAMA (Policy Alignment Membership Auditing)**: a member prompt **directly contributes** to the teacher-guided policy update, whereas a non-member prompt is affected only **indirectly via cross-prompt generalization**; the directional trace separates them

**Notes:** The OPD cluster's **privacy/auditing** axis. Companion to the 10-07 "backdoored-but-aligned teacher poisons the student" result — both treat the distillation prompt/corpus as a sensitive asset that can leak or be poisoned. Reusable idea: **the teacher's update direction, not just likelihood, is the membership signal.**

---

#### 6. [ReCal: Calibrating Structured Pruning for On-Policy Distillation Recovery](https://arxiv.org/abs/2610.11332)

- **ID**: `2610.11332v1` | **Cat**: cs.CL | **Submitted**: 2026-10-08
- **Authors**: Houcheng Jiang, Mao Zheng, Mingyang Song, Qiyong Zhong, Jie Sun, Tianyu Zhang, Junfeng Fang
- **Affiliations**: **Zhongguancun Academy**; **Foundation Model Department, Tencent**; **University of Science and Technology of China**; **National University of Singapore**
- **PDF**: [Link](https://arxiv.org/pdf/2610.11332)

**Key contributions:**
- Problem: **structured pruning** of reasoning models degrades capability, and the damage that persists after offline distillation **limits subsequent OPD recovery** (because OPD relies on student-generated trajectories)
- **ReCal (Recovery-Aware Calibration)**: a plug-and-play change to the *calibration* before pruning — uses **forward KL between the unpruned teacher and a pruned probe** to identify teacher-supported predictions disrupted by pruning, then **reweights calibration statistics** to steer existing pruning criteria toward preserving them
- Across multiple models and pruning methods, improves post-OPD mathematical reasoning by **up to +16.7 percentage points on AIME**

**Notes:** The OPD cluster's **pruning/recovery** axis: the interesting move is optimizing the *pre-OPD* stage for OPD's eventual success rather than the other way around. Industrial provenance (Tencent).

---

#### 7. [Learning to Plan by Looking Back: Hindsight Hierarchies for Training Reasoning Models](https://arxiv.org/abs/2610.12168)

- **ID**: `2610.12168v1` | **Cat**: cs.AI | **Submitted**: 2026-10-08 | **Comment**: 21 pages, 4 figures
- **Authors**: Lars Simon, Holger Eble, Manuel Radons
- **Affiliation**: **Bundesdruckerei GmbH** (Berlin, Germany)
- **PDF**: [Link](https://arxiv.org/pdf/2610.12168)

**Key contributions:**
- Observation: even when a problem exceeds the model's current ability, an **additionally supplied solution can let it extract useful "solution ideas" in hindsight**
- Jointly trains the **same model** on three capabilities: **(i)** predict solution ideas from a problem alone, **(ii)** reverse-engineer ideas from problem + known solution, **(iii)** solve problems using provided ideas
- **Self-improvement loop** alternates reverse-engineering ideas from supplied solutions with using those ideas as **additional supervision** for joint training of all three capabilities
- Formal specification + a concrete instantiation

**Notes:** A "hindsight / solution-prefix as supervision" mechanism in the reasoning-RL training lane — adjacent to the 10-08 ExpDis and the withdrawn `2610.11128` (reference-prefix guidance) but reframed as a **three-headed idea-extraction loop** rather than rollout filtering. Industrial author (a German security-printing firm).

---

#### 8. [PRAXIS: Learning Dynamics of Self-Improving Models with Symbolic Archives](https://arxiv.org/abs/2610.11803)

- **ID**: `2610.11803v1` | **Cat**: cs.LG | **Submitted**: 2026-10-08
- **Authors**: Venkat Margapuri, Mustafa Teber
- **Affiliation**: ⚠️ **not printed** (arXiv HTML author block contains only unfilled LaTeX template placeholders — "Cranberry-Lemon University" example text)
- **PDF**: [Link](https://arxiv.org/pdf/2610.11803)

**Key contributions:**
- Self-improving systems adapt data selection, optimization, and symbolic components, inducing **nonstationary objectives outside standard learning assumptions**
- **PRAXIS** models **generators, learners, and symbolic archives as interacting dynamical processes**
- Theory: KL-constrained generator updates + controlled archive-weight movement **bound one-step objective drift**; archive updates suppress a program relative to any fixed comparator with **persistent cumulative utility advantage under sub-Gaussian noise**; SGD achieves an **average-stationarity guarantee** whose degradation is governed by cumulative objective drift
- Experiments on visual robustness, relational graph reasoning, and algorithmic graph reasoning show generator stabilization, decreasing learner loss, and archive growth

**Notes:** A rare *theory* paper for the co-evolutionary / self-improving-loop thread — it gives drift and stationarity bounds for a system that changes its own objective. Pairs with the 10-08 Winner's Curse (selection noise in self-improvement) as the theory side of the same arc.

---

#### 9. [Recursive Self-Improvement through Multi-Agent Self-Supervision (MASS)](https://arxiv.org/abs/2610.12176)

- **ID**: `2610.12176v1` | **Cat**: cs.AI | **Submitted**: 2026-10-08 | **Comment**: 39 pages
- **Authors**: Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Somayeh Sojoudi, Matei Zaharia, Yujin Tang
- **Affiliations**: **UC Berkeley**; **Sakana AI** (work done during a Sakana AI internship)
- **PDF**: [Link](https://arxiv.org/pdf/2610.12176)

**Key contributions:**
- Recursive self-improvement (RSI) on **non-verifiable tasks** hits a **supervision bottleneck** when outputs exceed what humans can assess, leaving the model as best optimizer/evaluator — but a **single instance** struggles to critique and improve its own complex reasoning
- **MASS (Multi-Agent Self-Supervision)**: alternates **evolutionary workflow optimization** and **supervised fine-tuning on self-generated trajectories**
- Prompts a single base model to iteratively **propose, execute, and self-evaluate multi-agent workflows**, with an evolutionary search **constrained by structural guardrails**

**Notes:** The RSI thread's structural bet: **heterogeneity comes from multi-agent topologies, not from new data.** Notable authorship (Matei Zaharia, Somayeh Sojoudi; Sakana AI) makes it a high-signal entry for the wiki's recursive-self-improvement lineage.

---

#### 10. [RaReCache: Bridging the Gap in Cross-Model KV Cache Reuse via Rank-Disagreement-Based Selective Recomputation](https://arxiv.org/abs/2610.11358)

- **ID**: `2610.11358v1` | **Cat**: cs.AI | **Submitted**: 2026-10-08
- **Authors**: Sreetama Sarkar, Saptarshi Mitra, Sitao Huang, Souvik Kundu, Peter A. Beerel
- **Affiliations**: **University of Southern California**; **University of California, Irvine**; **Intel Labs**
- **PDF**: [Link](https://arxiv.org/pdf/2610.11358)

**Key contributions:**
- Serving pain point: coding agents and multi-model systems **route a shared context across models** (mid-session model switch, cascade escalation), and because KV caches are model-specific, each switch forces a **full reprefill**
- Closed-form linear maps can translate KV between same-family models, but accuracy **degrades as the model-size gap widens**; this paper shows the failures are **concentrated in a small subset of information-dense tokens**
- **RaReCache** lets a large target model decode from a cache prefilled by a much smaller source via **selective recomputation**, scoring each token by the energy of its mapped KV in output directions **weakly supported by the calibration data** (rank disagreement)
- On a **23×** parameter gap (Qwen3-0.6B → 14B), recomputing just **30%** of positions retains **95–99%** of target accuracy

**Notes:** A deployable serving win for the multi-model routing pattern the agents lane keeps producing. The "transfer errors are token-sparse, so recompute only those" framing is the reusable insight.

---

#### 11. [WAM-Cache: Staleness-Bounded KV Reuse for Efficient World Action Models](https://arxiv.org/abs/2610.11401)

- **ID**: `2610.11401v1` | **Cat**: cs.RO | **Submitted**: 2026-10-08 | **Comment**: 19 pages, 5 figures, 7 tables
- **Authors**: Kai Ding, Yang He, Ruijie Quan, Yi Yang
- **Affiliations**: **Zhejiang University**; **IAIC, Agency for Science, Technology and Research (A\*STAR), Singapore**
- **PDF**: [Link](https://arxiv.org/pdf/2610.11401)

**Key contributions:**
- World Action Models (WAMs) condition an action expert on a pretrained **video Diffusion Transformer (DiT)**; in closed-loop control the DiT **re-encodes the observation into layerwise KV pairs at every chunk**, and this prefill dominates per-chunk cost
- Training-free **WAM-Cache** retains layerwise KV across chunks and recomputes only a **sparse refresh set**
- Key negative finding: the intuitive heuristic of refreshing **visually drifted** tokens plateaus far below the dense baseline **even with an oracle predicting ground-truth KV drift** — downstream action accuracy is governed by **where the action expert attends, not by what moved**
- WAM-Cache selects refresh tokens by action-expert attention instead

**Notes:** A mechanism-level correction for world-model/serving caching: **attention-relevance beats visual-change as the freshness criterion.** The oracle-controlled negative result (visual drift is the wrong signal) is the reusable part, and it connects to the wiki's world-model and KV-serving threads.

---

#### 12. [AgentHorizon: Evaluating Agentic Judges for Long-Horizon Computer-Use Tasks](https://arxiv.org/abs/2610.11050)

- **ID**: `2610.11050v1` | **Cat**: cs.AI | **Submitted**: 2026-10-08
- **Authors**: Xing Han Lù, Dheeraj Vattikonda, Sina Hajimiri, Fatemeh Pesaran Zadeh, Parishad BehnamGhader, Ghazwa Darwiche, Amirhossein Kazemnejad, Christopher Pal, Alexandre Drouin, Siva Reddy
- **Affiliations**: **ServiceNow Research**; **McGill University**; **Mila – Quebec AI Institute**; **Seoul National University**; **Université Laval**; **Polytechnique Montréal**; **Canada CIFAR AI Chair**
- **PDF**: [Link](https://arxiv.org/pdf/2610.11050)

**Key contributions:**
- Computer-use agents make **automatic judges** central to training/evaluation, but their reliability on **long, multi-application tasks** is unclear — a trajectory may look complete while **violating instruction constraints** or introducing side effects
- **AgentHorizon**: **1,373** computer-use tasks (instruction–trajectory pairs) drawn from **166 hours** of human-recorded trajectories across **three operating systems**
- By recording trajectories for **closely related instructions**, constructs **negative tasks** (instruction-swapped) that a competent judge must reject

**Notes:** The evaluation-validity thread's newest instrument for computer-use agents. The **negative-task construction by instruction-swap** is the reusable design — it targets the exact failure mode (trajectory looks right, instruction violated) that flat success-judging misses.

---

#### 13. [One Word Opens the Gate: The Option-Channel Attack on Typed Decision Models as Agent Guardrails](https://arxiv.org/abs/2610.12292)

- **ID**: `2610.12292v1` | **Cat**: cs.AI | **Submitted**: 2026-10-08
- **Authors**: Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram
- **Affiliation**: **University of Southern California (USC)**
- **PDF**: [Link](https://arxiv.org/pdf/2610.12292)

**Key contributions:**
- Studies **typed decision models** (read text → probability over caller-defined options, generate no text) deployed as **agent guardrails** that gate tool calls / incoming messages
- Evaluates **seven open-weight models** and separates **fail-open** (allows a prohibited action → vulnerability) from **fail-closed** (blocks a permitted one → cost)
- On prompt-injection, jailbreak, and toxic-content screening, allow/block accuracy ranges **36–72%** (chance 50%); a low error rate in one direction often just reflects a model's **default answer** (one allows nearly everything, another blocks nearly everything)
- On a synthetic agent-tool-call suite, **six** listed models show exploitable behavior via a single crafted option word

**Notes:** A sharp negative result for the increasingly popular "typed decision model as guardrail" pattern (cf. 10-07 SanSi, 10-08 typed-decision thread). **Fail-open/fail-closed decomposition** is the reusable audit lens; the "one word opens the gate" framing is the quotable finding.

---

#### 14. [On the Estimation and Validity of AI Time Horizons — A Statistical Look at the METR Plot](https://arxiv.org/abs/2610.12466)

- **ID**: `2610.12466v1` | **Cat**: cs.AI | **Submitted**: 2026-10-08
- **Authors**: Drew T. Nguyen, William Fithian
- **Affiliation**: **Department of Statistics, UC Berkeley**
- **PDF**: [Link](https://arxiv.org/pdf/2610.12466)

**Key contributions:**
- Recomputes METR's **50% time horizon** (the human completion time of software tasks an AI solves with 50% probability) on **228 tasks × 26 AIs** using **splines and item-response theory**, relaxing the assumption that task AI-difficulty is **linear in log human time**
- The fitted spline **converts** human time to AI difficulty: nearly flat in the **2–30 min** region, close to linear elsewhere — so a **3→30 min** jump is much easier than a **30 min→5 h** jump despite the same 10× multiplier
- Contributes time-horizon point estimates that score better under a **cross-validated suite of proper scoring rules**, plus **diagnostic plots for construct validity**

**Notes:** The measurement-audit thread's most load-bearing target: **the METR time-horizon curve is now a headline AI-capability metric**, and this paper shows the standard linear-in-log-time fit is not the best-supported model and that horizon numbers are **multiplier-dependent**. A caution every "AI time horizons are doubling every N months" claim should absorb.

---

#### 15. [Do LLMs Learn from Rewards in Context? Rethinking the Role of Reward in In-Context Reinforcement Learning](https://arxiv.org/abs/2610.11152)

- **ID**: `2610.11152v1` | **Cat**: cs.LG | **Submitted**: 2026-10-08 | **Comment**: **NeurIPS 2026 Spotlight (Negative Results Track)**
- **Authors**: Minchan Kwon, Seunghee Koh, Sunghyun Baek, Minsung Bae, Junmo Kim
- **Affiliation**: **KAIST** (Korea Advanced Institute of Science and Technology)
- **PDF**: [Link](https://arxiv.org/pdf/2610.11152)

**Key contributions:**
- Tests whether in-context learning can actually play the role of RL ("in-context RL"): simplest form, **direct ICRL**, where the model conditions on raw trajectory–reward pairs
- Controlled experiments on **four benchmarks across six models**: the reward **is read but its effect is small** — flipping, randomizing, or removing the reward leaves the improvement curve **almost unchanged**, even under meta-prompts that instruct explore/exploit/reason over rewards
- Trajectories drive improvement, but **not through semantic content** (shuffled trajectories still help) — isolating the reward's contribution as near-null

**Notes:** A peer-reviewed **negative result** at the center of the "agents improve from experience in context" story. Directly relevant to the wiki's [[verifiable-rewards]] / in-context-improvement arc: **most of the apparent in-context-RL gain is not reward learning.**

---

## Also worth recording (not detailed above)

- **`2610.12338`** — *VFold: Symmetry-Aware Cross-Layer Value Cache Compression* (Neha Verma, Sungwon Kim, Kenton Murray, Kevin Duh). Merges **value** caches across layers by exploiting inter-layer similarity to cut long-context memory **without architectural changes or decode overhead**; composes with existing KV-compression methods. Serving-thread companion to RaReCache/WAM-Cache.
- **`2610.11605`** — *NanoProof: Open and Efficient Automated Theorem Proving in Lean 4* (Matěj Kripner, Milan Straka; **Charles University**). Factorized execution-guided prover with **training data, extraction tooling, pipeline, and weights all released**; **50.8% pass@16 on MiniF2F-Test**, compute-efficient and end-to-end reproducible. Relevant to the wiki's formal-verification/RLVR arc.
- **`2610.11593`** — *Runnable Commit Untangling for Coding Agents* (Jinfeng Jiang, Dongsun Kim, Dayi Lin, Zhou Yang). Argues existing commit-untangling studies miss that untangled commits are **ordered and must leave the code runnable**; reframes untangling for coding-agent output. Opens the "can the patch run at each step" constraint as the evaluation criterion.
- **`2610.12410`** — *Predicting Alignment Generalization with Value Representations* (Andy Liu, Mehar Bhatia, Karolina Stanczak, Mona Diab, Vered Shwartz, Daniel Fried). Establishes **alignment-generalization prediction**: predicting how fine-tuning on one value changes behavior **across held-out values**; uses value representations as the signal. Directly relevant to the alignment/behavior-drift thread.
- **`2610.12005`** — *Test-Time Compute for Tabular Foundation Models: Mechanisms, Gains, and Limits* (Kanghui Ning, Marin Biloš, James T. Wilson, Yilang Zhang, Kashif Rasul, Dongjin Song). Systematic study of test-time compute for TFMs along **adaptation / aggregation / context construction**; **DiagScale** trains only **0.003–0.03%** of parameters yet matches full fine-tuning across three backbones (TabArena).
- **`2610.12242`** — *TokenRouter: Efficient Serving System for Token-Level LLM Routing* (**NeurIPS 2026**). Systems answer to token-level routing: existing single-LLM serving stacks suffer **step desynchronization and batch-admission stalls**; TokenRouter makes fine-grained token-level routing servable.
- **`2610.11599`** — *Large Language Model Turnover Undermines Screening for Artificial Intelligence-Assisted Scientific Writing* (Kazuki Nakajima, Takayuki Mizuno). Pairs **4,000 pre-ChatGPT PNAS abstracts** with rewrites by **23 LLM versions** (June 2023 → Aug 2026): detectors trained against a fixed version set degrade as the in-use versions turn over. Same "pinned-instrument" theme as the 10-08 backbone-evolution finding.
- **`2610.12361`** — *Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought Faithfulness* (Saisab Sadhu, Shreeyans Arora, Pratinav Seth). Across **seven open-weight models (8B–70B)**, when required to justify a verdict by naming the governing authority, models name the correct authority in **66.7–100%** of generations while the verdict barely depends on it — named citations are not evidence of faithfulness.
- **`2610.11185`** — *Predictive Multiplicity in Cell-Fate Assignment: Label-Free Rashomon Sets and the Limits of Per-Cell Certification*. Label-free Rashomon sets for single-cell trajectory inference; **multiplicity is large** and depends more on model-space diversity than size (twelve configurations of a second algorithm expose ~20% conflicting fates). Per-cell certification is shown to be limited.

---

## Cross-cutting observations

1. **Zero CTR papers — a first.** The 2026-10-08 block contains **no** click-through / ad-serving / generative-rec paper at all: full-batch regex yields 0 `click-through` hits. The 10-07/10-08 reports recorded a "supply-thin" CTR lane with methodology-audit papers; this window has **nothing**. The [[ctr-scaling-landscape]] thread gains no entrant for the **third consecutive window**, and the CTR/ads lane is now empty rather than merely method-free.
2. **Same-day sibling collision is now the dominant dedup failure mode (5th in 8 runs, 3rd consecutive).** 10 of this run's picks were claimed by `2026-10-10/arxiv-daily.md` mid-run, including 3 of 3 original IR method papers. All withdrawn, not merged, per precedent; replacements verified 0-hit. The **shared claimed-ID lock file** requested since 10-07 remains unfixed — ID-only dedup against a snapshot cannot survive a concurrent writer.
3. **The OPD cluster keeps splitting into new axes.** Three papers again: **which tokens** carry the learning signal (DIAL-OPD, paper 4), **membership auditing** via teacher-update direction (PAMA, paper 5), and **pre-OPD pruning calibration** for later recovery (ReCal, paper 6). Unifying correction, unchanged: OPD's design space is *not* "distill harder."
4. **Self-improvement / reasoning-RL training loops converge on "where does the supervision come from."** Hindsight Hierarchies (paper 7) extracts ideas from supplied solutions; PRAXIS (paper 8) bounds drift in a co-evolving generator/archive system; MASS (paper 9) manufactures heterogeneity from multi-agent topologies. Three answers to the same non-verifiable-supervision bottleneck, plus the peer-reviewed **negative** that in-context rewards barely drive learning (paper 15).
5. **Serving-layer wins are concentrated on KV reuse across heterogeneous models/loops.** RaReCache (paper 10) recomputes only rank-disagreement tokens for cross-model reuse; WAM-Cache (paper 11) refreshes by action-expert attention, not visual drift; VFold (`2610.12338`) merges value caches. The through-line: **which cached entries matter is decided by the consumer (attention/rank), not by a proxy for change.**
6. **Measurement/negative results dominate the AI lane for the fifth/sixth consecutive window.** AgentHorizon (12), Option-Channel guardrails (13), the METR-plot critique (14), the in-context-RL null (15), RAG-Stress (2), O2I-ratio mismatch (1), the WAM-Cache oracle null (11), and "Cited but Not Consulted" all end in "the apparent effect/metric/guarantee was smaller, confounded, or the wrong target." The series' standing finding — **reported capability and verified capability diverge** — held again, and this window put the **metric itself** (time horizons, reward-in-context, named citations, guardrail accuracy) under audit.

---

## Method disclosure, dedup, and cautions

**Harvest**: arXiv export API over HTTPS. Four category sweeps (`cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, 2 pages each) plus 23 `all:` topical passes, all bounded `submittedDate:[202610080000 TO 202610102359]`, `sortBy=submittedDate desc` → **478 raw entries → 478 unique, all `published = 2026-10-08`**. Requests spaced ~4 s; no HTTP 429 this run.

⚠️ **Window semantics**: "last 24 hours" is not what arXiv exposes. `submittedDate:[202610090000 TO 202610102359]` returns **0 entries**; the newest available block is **2026-10-08 (a single day, not a rolling 24 h)**, matching the same-day `arxiv-daily` sibling's own finding.

⚠️ **CTR-lane emptiness**: full-batch abstract regex over the 478 unique papers gives **0** hits for `click-through`/`click through`/`clickthrough` and **0** relevant `advertis` hits. The lane is empty, not merely thin — recorded explicitly so it is not read as omission.

⚠️ **Dedup / sibling collision**: baseline = **8,535** unique arXiv IDs regex-extracted from `wiki/**/*.md`, taken *after* the same-day sibling `2026-10-10/arxiv-daily.md` (written 10:32). **413 / 478 window entries unclaimed.** ⚠️ The sibling claimed **10** of this run's original selections mid-draft (**4** primary + **6** secondary); all 10 were **withdrawn, not merged**, and **10 replacements** (`2610.11598`, `2610.11489`, `2610.11183`, `2610.12168`, `2610.11358`… plus the retained non-collided set) were verified 0-hit against the live wiki immediately before writing. ID-level dedup only; no title-level pass.

⚠️ **Affiliation discipline**: institutions read **only** from each paper's own arXiv HTML `ltx_authors` author block, **never inferred**. Recovered for **13 / 15** featured papers; the two exceptions are `2610.11423` (author block prints names + corresponding marker only, **no affiliation**) and `2610.11803` (author block contains only unfilled LaTeX template placeholders — "Cranberry-Lemon University" example text). Notable recoveries: paper 4 spans **six institutions** (EIT-Ningbo / HK PolyU / HKUST-GZ / SJTU / HKU / Waterloo); paper 6 has **Tencent**; paper 9 is **UC Berkeley + Sakana AI**; paper 10 is **USC + UC Irvine + Intel Labs**; paper 14 is **UC Berkeley Statistics**.

⚠️ **Venue discipline**: **1 of 15** featured carries a venue — `2610.11152` (**NeurIPS 2026 Spotlight, Negative Results Track**, self-reported). Recorded among the secondaries: `2610.12242` (**NeurIPS 2026**), `2610.11598` (NTCIR-19 task). **No result in this report was independently replicated, and none was replicated by a second group.** Venue tags are self-reported via arXiv `comment`/`journal_ref`.
