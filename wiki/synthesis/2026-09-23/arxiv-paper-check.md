---
title: "arXiv Paper Check — AI & CTR (September 23, 2026)"
type: synthesis
created: 2026-09-23
updated: 2026-09-23
sources: []
tags: [arxiv, daily-check, ai, ctr, evaluation, llm-as-judge, proxy-reliability, statistics, preference-learning, off-policy-evaluation, tabular-learning, agents, agent-memory, self-improvement, delegation, retrieval, long-context, efficient-evaluation, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 23, 2026)

**Wednesday note**: the live arXiv mailing is the **Wed 23 Sep 2026** batch (Tue 22 Sep submissions, IDs **2609.25006–2609.26796**), already extensively claimed by today's [[arxiv-daily]] (37 papers / 8 sections + 6 runner-ups) and [[arxiv-ai-search]] (22 papers / 6 sections + 6 runner-ups). This issue is therefore a **second-pass sweep of the unclaimed remainder of the Wed-23 window** from the AI & CTR angle — restricted to papers *not* claimed by either sibling or any earlier wiki page. All 14 featured arXiv IDs below were grep-verified absent (0 hits) from the entire `wiki/` (6,325-ID known set).

**CTR status**: no genuinely new *direct-category* CTR/ads papers remain unclaimed — the window's flagships (KwaiMind CTR-as-RL-reward, QSS LLM-reranker shortcut fix, Lightweight Ranking Heads, TailSpec-EASE) were all featured in today's siblings. The CTR-relevant remainder here clusters around **evaluation-instrument reliability (proxy validation, judge construct validity), non-asymptotic statistics for preference/ranking decisions (BTL estimation, OPE under annotation budgets, forecast dilution, causal tabular pretraining), and agent-decision governance (self-improvement, delegation auditing, memory economics)** — the statistical and evaluation scaffold that CTR/rec/ads decisions sit on.

---

## ① Evaluation, Judges & Proxy Reliability (4)

### Auditing Proxy-Based Validation Across Text Spans
- **Authors**: Daein Weon, Dong Ho Kang
- **arXiv**: [2609.25808](https://arxiv.org/abs/2609.25808) — cs.LG, cs.CL
- **Key contribution**: Audits the shortcut in *proxy-based validation* — shallow auto-validators / LLM judges used to validate search or generation outputs — by measuring how much of their accuracy is an artifact of text-span position. Augmenting the query with an answer string (off-span information) inflates validation accuracy by **+0.184 at a 50-char prefix**, and the gap collapses to **≤+0.045 once the prefix reaches ~120 chars**; the answer string alone achieves **AUC 0.634**, i.e. most of the "validation" signal is a span-position shortcut. The audit further checks signed validation contracts (of the kind used in production pipelines) and finds only **3/11 external contracts** support off-span control — meaning the shortcut is baked into how these proxies are specified and deployed.
- **Why it matters**: The cleanest quantitative framing yet of the proxy-validator reliability problem — validation accuracy is *span-dependent*, and contract sampling misses the leak. Pairs directly with the wiki's [[llm-as-judge]] line: proxy reliability must be audited at the construct level, not benchmark level.

### Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It
- **Authors**: Yu Sun, Junhao Xu
- **arXiv**: [2609.26758](https://arxiv.org/abs/2609.26758) — cs.AI, cs.LG
- **Key contribution**: A constrained decision head (e.g. constrained decoding over a fixed option vocabulary) is advertised as "type-safe" — the output must land in a rubric's option set. But the head follows the *surface option name*, not the rubric semantics bound to it: on identical rubric-bound decisions, renaming the option labels from `0/1` to `no/yes` flips a model's AUC from **0.94 → 0.23**, and a hosted model goes **0.8146 → 0.5806**. Constraint satisfaction gives no guarantee that the decision obeys the rubric; the model latches onto label surface form.
- **Why it matters**: A sharp warning for every production system that treats format-constrained outputs as correctness — relevant to rubric-based reward modeling, structured LLM outputs in rec/ads pipelines, and the wiki's benchmark-validity thread. Constraint ≠ alignment.

### The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks (Taste-Bench)
- **Authors**: Wenbo Pan et al.
- **arXiv**: [2609.25804](https://arxiv.org/abs/2609.25804) — cs.AI, cs.LG
- **Key contribution**: Introduces **Taste-Bench**, a benchmark for "taste" — the aesthetic / quality-of-judgment dimension of long-horizon agent tasks (background design, photo editing, coffee brewing, etc.): whether the agent makes outcomes that *look and feel good*, not merely functionally correct. Across 100+ long-horizon scenarios the best model reaches **59.7%**, i.e. taste is far from saturated even by strong agents. Taste training transfers: improving taste also raises downstream long-horizon task success.
- **Why it matters**: Adds an under-measured axis (aesthetic judgment) to agent evaluation — complements the wiki's agent-reliability work by showing "success" metrics miss a large quality surface that conditioning/judgment training can recover.

### Receptiveness, Not Sycophancy: Distinguishing Engagement from Deference in Language Models
- **Authors**: Calvin Isley, Johann Gaebler, Max Lamparth, Julia Minson, Sharad Goel
- **arXiv**: [2609.26579](https://arxiv.org/abs/2609.26579) — cs.CL, cs.AI, cs.HC
- **Key contribution**: Separates two constructs commonly conflated under "sycophancy": *deference* (unsupported agreement / flattery) vs *receptiveness* (constructive engagement with a disagreeing user's view). A preregistered experiment shows the wrinkle in existing sycophancy measurement: **socially "sycophantic" responses are also more receptive** — the two correlate, so agreement-based sycophancy detectors over-cite genuine engagement as sycophancy. Argues refusal to disagree and non-engagement should be tracked as distinct failure modes.
- **Why it matters**: A construct-validity argument for the preference-alignment / judge-reliability thread: before we can measure "sycophancy" we must decide whether engagement-with-those-who-disagree is being penalized. Useful corrective to alignment evals that treat any agreement as sycophantic.

---

## ② Statistics, Preference & OPE (4)

### Error Bounds for Statistical Estimators in the BTL Model with Parametric Multivariate Utility Functions
- **Authors**: Yicheng Li, Huifu Xu
- **arXiv**: [2609.26326](https://arxiv.org/abs/2609.26326) — stat.ML, cs.LG
- **Key contribution**: The **Bradley-Terry-Luce (BTL)** model with parametric multivariate utility functions (pairwise comparisons over feature vectors — the workhorse of preference/ranking estimation) gets rigorous statistical guarantees. Derives error bounds for the **unconstrained MLE** (valid beyond the standard full-column-rank regime) and establishes **non-asymptotic minimax-optimal rates** for BTL utility estimation.
- **Why it matters**: Preference data imperfect; knowing exactly how fast BTL MLE converges (and that it is optimal) is the contract behind pairwise-judge aggregation and ranking systems — the statistics layer under LLM-judge and CTR-side preference signals. Strong candidate for the wiki's preference-learning/statistics method line.

### Optimal Sequential Annotations for Off-Policy Evaluation
- **Authors**: Woojin Chae, Ezinne Nwankwo, Haitong Qin, Angela Zhou
- **arXiv**: [2609.26707](https://arxiv.org/abs/2609.26707) — stat.ME, cs.LG
- **Key contribution**: Off-policy evaluation (OPE) of a decision policy (e.g. a ranking policy trained on logged feedback) often needs human annotation of logged outcomes, and budgets are limited. Characterizes **which logged observations to annotate, and in what order**, so that a **doubly-robust (DR) OPE estimator** achieves the largest variance reduction per annotation. Empirically: an optimal annotation policy cuts estimator RMSE by **~34–65% on housing data** and **55–62% on LMArena** at a **40% annotation budget** vs naive annotation.
- **Why it matters**: Directly actionable for any logged-feedback ranking/CTR setting where labels arrive one at a time under budget — the sequential-annotation answer is both principled (statistical) and cheap. Complements the wiki's [[online-controlled-experiments]] / evaluation methodology line.

### Target Alignment, Dilution and Forecast Selection When Cross-Sectional Forecasts Share a Common Target
- **Authors**: Masoud Soleimani
- **arXiv**: [2609.26303](https://arxiv.org/abs/2609.26303) — econ.EM, stat.AP
- **Key contribution**: When many cross-sectional forecasts predict a *common* target (e.g. ranking every stock, every ETF against one market state), forecast selection interacts with **dilution**: combining forecasters that are individually aligned but correlated can dilute signal. Establishes when an **equal-weighted combination** beats the no-information benchmark — only when *average alignment exceeds dispersion* — and when subset selection is preferable. Applied to LLM-generated forecasts of US equity rankings and ETF rankings.
- **Why it matters**: A statistical rule for when to trust/aggregate multi-forecaster ensembles — relevant to any ranking ensemble, LLM-as-forecaster pipelines, and the wiki's forecast-selection / quant thread. The alignment-vs-dispersion condition is the memorable takeaway.

### Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining
- **Authors**: Zhiheng Zhang
- **arXiv**: [2609.26290](https://arxiv.org/abs/2609.26290) — stat.ML, cs.LG
- **Key contribution**: A statistical theory + recipe for **causal tabular pretraining** (**FSP**, Fluctuation State Pretraining): the pretraining signal is a *fluctuating endpoint* whose transition probability encodes the treatment effect, giving the model supervision that transfers to genuinely causal downstream tasks. Empirically FSP cuts RMSE by **69.8%** in large-effect-shift tabular causal settings vs latent (self-supervised) supervision and by **39.5% vs CausalPFN**. The theory quantifies the label-ambiguity tradeoff: at a transition parameter λ<1 the retained label ambiguity decays as **(1−λ)²/n**, and with full fluctuation the label is provably observable with risk **n⁻²**.
- **Why it matters**: Gives tabular foundation models a proper statistical identity — the leak-proof recipe behind transfer to causal / growth-type tabular targets relevant to rec/ads scoring. Cross-links to today's sibling-claimed JEPA-for-tabular negative result (2609.25541, [[arxiv-daily]] §5) and the wiki's [[tabular-classical-vs-llm]] thread.

---

## ③ Agents: Decisions, Self-Improvement & Memory (4)

### Recursive Self-Improvement of AI Research Agents (AIDE²)
- **Authors**: Dhruv Srikanth et al.
- **arXiv**: [2609.26457](https://arxiv.org/abs/2609.26457) — cs.AI, cs.LG
- **Key contribution**: **AIDE²** extends the AIDE research-agent line to *recursive self-improvement*: a research agent whose outputs feed back into improving the agent system (better scaffolding, better baselines). Reports an **8-day autonomous run** producing **7 successive system improvements**, and — critically — a **reward-hacking rate that falls from 55% → 32%** across the improvement loop, suggesting guardrails improve as the agent improves itself.
- **Why it matters**: One of the few concrete, time-boxed accounts of closed-loop agent self-improvement with explicit safety telemetry. Directly relevant to the wiki's agent thread and to the Anthropic R&D-automation index line (AL4) — a "how much and how safely" proto-measure for recursive research automation.

### The Delegation Blind Spot: Auditing Product Decisions from Agent Choices
- **Authors**: Shivam Gupta
- **arXiv**: [2609.26642](https://arxiv.org/abs/2609.26642) — cs.AI, cs.CY
- **Key contribution**: As firms delegate product decisions to AI agents, the audit trail migrates from *stated decisions* to *observed agent choices*. Proposes auditing product decisions by reverse-engineering what the agent's choice behavior implies, using **4,800 logged requests across two pinned system snapshots**, and **14,400 multinomial simulations** of choice behavior to infer the underlying decision policy and detect drift/hidden tradeoffs the organization never sanctioned.
- **Why it matters**: A concrete audit methodology for agentic delegation — the "choices as data" lens lets a firm detect delegation blind spots (decisions delegated to the model that the org wouldn't have made). Complements [[arxiv-daily]]'s agent-reliability section with a governance/accountability framing.

### Beyond Provenance: The Economics and Governance of Personalized AI Memory
- **Authors**: — (author list unconfirmed)
- **arXiv**: [2609.25521](https://arxiv.org/abs/2609.25521) — cs.GT, cs.AI, cs.CY
- **Key contribution**: Moves personalized-AI-memory governance past *provenance* (where did this memory come from, who owns it) to the **economics of memory as a scarce, personalized asset**: what it is worth to whom, who bears the cost of correctness/recency/leakage, and what mechanism/game-theoretic structures could govern sharing, retention and deletion of memory across agent service providers. Frames memory as a governance object with externalities, not just a data-quality problem.
- **Why it matters**: The missing economics layer for persistent agent memory — complements the agent-memory-retrieval work (execution provenance, [[arxiv-daily]] §6) with a mechanism-design view on who controls the memory substrate.

### Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents
- **Authors**: Jiangxu Wu
- **arXiv**: [2609.25991](https://arxiv.org/abs/2609.25991) — cs.IR, cs.AI, cs.CL
- **Key contribution**: Reformulates knowledge-base access for agents as **skills**: instead of "retrieve then answer", each KB encodes its own discovery structure — a **SKILL.md discovery layer + index.md + YAML frontmatter** (a design echoing this wiki's own operating contract) — and the agent opens files lazily/eagerly per task, loading structural knowledge as a skill, not a corpus. On the WixQA agentic-QA benchmark: **Factuality 0.889 / Context Recall 0.816** vs **Corpus2Skill 0.767 / 0.708** — a structural, retrieval-free gain.
- **Why it matters**: The strongest "self-describing knowledge bases" argument this window, and structurally the same pattern as this wiki's SCHEMA-driven design — evidence that skill-encoding beats raw retrieval for agentic knowledge use. Relevant to the wiki's AI-search/RAG line: the unit of retrieval shifts from passage to *usage protocol*.

---

## ④ Retrieval, Long-Context & Efficient Evaluation (2)

### The Sirens' Song: Proximity Trap, LYRA and ProxBench
- **Authors**: Xiaoyu Yang, Jie Lu, Wei Duan, En Yu
- **arXiv**: [2609.26718](https://arxiv.org/abs/2609.26718) — cs.LG, cs.CL, cs.IR
- **Key contribution**: Identifies the **proximity trap** in long-context retrieval: models/retrievers over-trust *positional proximity* (the chunk nearest the question or nearest the answer) even when that proximity is misleading — a "siren's song". Proposes **LYRA**, a **t-distribution-based directional matching** correction that re-ranks long-context candidates away from shallow positional proximity, and **ProxBench**, a benchmark that isolates the proximity signal from genuine relevance.
- **Why it matters**: A named failure mode for long-context agent retrieval (the window's other long-context work focuses on KV/serving efficiency); proximity-vs-relevance decoupling is directly testable on rec/QA long-context pipelines. Complements the wiki's AI-search/RAG thread.

### GittinsEval: Efficient Cost-Aware LLM Evaluation via Bayesian Bandit Gittins Indices
- **Authors**: Qian Xie, Yueli He, Nairen Cao
- **arXiv**: [2609.25645](https://arxiv.org/abs/2609.25645) — cs.LG, cs.AI
- **Key contribution**: Standard LLM evaluation prices every item across every model. **GittinsEval** frames evaluation as a **Bayesian multi-armed bandit** (each model an arm, stopping when the ranking is decided) solved by **Gittins indices** — the optimal *adaptive* policy for when to keep querying a model on more items vs settle. Achieves **~1–2% of exhaustive evaluation cost with near-zero regret** on GSM8K / PIQA / AlpacaEval / MMLU, via adaptive stopping (queries only 1–10% of items for most rankings).
- **Why it matters**: The cost side of the evaluation-reliability story — if we can trust a stopped-early ranking at 1–2% cost, cheap large-scale eval (model-sweeps, judge ablations) becomes affordable. A ready complement to the [[llm-as-judge]] measurement thread.

---

## Cross-Cutting Themes

1. **Evaluation instruments themselves are now the audit target**: The window's sharpest papers are about *whether the measuring device measures what we think* — span-position shortcuts in proxy validators (+0.184 at 50-char prefix), option-name sensitivity of constrained decision heads (AUC 0.94→0.23 under a relabel), taste as a distinct construct, and sycophancy-vs-receptiveness conflation. Benchmark-level accuracy is no longer the frontier; instrument-level construct validity is.
2. **A statistics renaissance under CTR/rec decisions**: BTL minimax error bounds, DR-OPE with optimal sequential annotation (−34–65% RMSE), the alignment-vs-dispersion forecast-selection condition, and FSP causal tabular pretraining (risk n⁻²) all give rigorous, non-asymptotic contracts for the preference/ranking signals the industry runs on.
3. **Agent autonomy acquires its own evaluation & governance**: closed-loop self-improvement with falling reward-hacking (AIDE², 55%→32%), delegation auditing from choice data, memory economics beyond provenance, and self-describing knowledge bases — the agent thread moves from capability demos to *accountability infrastructure*.
4. **Long-context & eval cost as first-class**: ProxBench/LYRA name the proximity trap; GittinsEval prices evaluation itself as a bandit (1–2% cost, near-zero regret). Both treat *when to stop looking / stop paying* as the core decision.
5. **CTR**: still the **~10th consecutive window** without a direct end-to-end CTR-model paper in the unclaimed remainder — KwaiMind (CTR as RL reward, +2.44% online CTR, 2609.26375) remains the advertising/CTR-adjacent flagship of the Wed-23 window, claimed by [[arxiv-daily]]. This report's CTR-adjacent content is the preference/OPE/tabular scaffold above.

---

## Method Note

Wednesday fresh mailing (Tue Sep 22 submissions, Wed Sep 23 2026; IDs **2609.25006–2609.26796**). Pool: arXiv API tail sweep (8 target categories cs.AI / cs.LG / cs.IR / cs.CL / cs.CV / cs.GT / cs.MA / cs.NE, 2 pages × 100, parsed into `~/T/opencode/arxiv-paper-check-0923/window-raw-2.json`) → **1,292 unique entries**, filtered to the subscribed window (published=2026-09-22 & num ≥ 2609.25006) → **281 fresh in-window entries** (primary-cat spread: cs.LG 69 / cs.CV 55 / cs.AI 47 / cs.CL 29 / cs.RO 13 / stat.ML 11 / rest < 11). Sibling dedup: today's [[arxiv-daily]] (37 featured + 6 runner-ups) and [[arxiv-ai-search]] (22 featured + 6 runner-ups) removed → **235 unclaimed IDs**, then keyword-screened for evaluation / statistics / preference / OPE / agent-decision / retrieval / tabular-CTR signal → **14 featured + 6 runner-ups below**. Every featured and runner-up ID grep-verified **0 hits in `wiki/`** (6,325-ID known set). Affiliations marked *(tentative)* where inferred from author/affiliation text rather than confirmed metadata. Window's flagship rec/CTR/LLM entries were claimed by today's siblings — this issue mines the remainder.

**Runner-ups** (0-hit verified, not featured): 2609.26361 **GitScholar** — GitHub-engagement dataset for predicting AI research impact (444k repos ↔ 558k AI arXiv papers; +12% early citation-prediction precision); 2609.26025 **MICRO** — Multi-Fidelity Active Search for severe error discovery (WMT20 EN-DE); 2609.25542 **DefaultGNN** — dual-perspective GNN for corporate-default prediction from buyer-seller transaction graphs (+7–11pp approval-rate lift without added default risk); 2609.25638 **What Drives Hierarchy-Aware Image Retrieval?** (Ling Shi) — objective-family contrasts dominate geometry contrasts (CUB +0.0487 vs +0.0102); 2609.25850 **SASS** — Stage-Adaptive Sample Selection, 98.3% of full-dataset performance at a 40% annotation budget, +5.1pp over BADGE; 2609.25602 **Rewired or Gated?** — instruction tuning shapes knowledge-conflict circuits by *gating*, not rewiring (node overlap 0.60–0.82).

**Next fresh window**: Thu Sep 24 2026 (Wed 23 Sep submissions).