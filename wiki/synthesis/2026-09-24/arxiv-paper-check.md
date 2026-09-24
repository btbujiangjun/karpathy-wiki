---
title: "arXiv Paper Check — AI & CTR (September 24, 2026)"
type: synthesis
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: [arxiv, daily-check, ai, ctr, evaluation, benchmark-validity, statistics, experimentation, decision-layer, agent-memory, alignment, red-teaming, agent-control, retrieval, temporal-ir, text-autoencoder, tabular, online-linear-programming, auc, quasi-experiments, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 24, 2026)

**Thursday note**: the live arXiv mailing is the **Thu 24 Sep 2026** batch (Wed 23 Sep submissions, IDs **2609.26809–2609.28473**), already claimed by today's [[arxiv-daily]] (39 papers / 8 sections + 10 runner-ups, API sweep 2609.27173–2609.28470) and [[arxiv-ai-search]] (21 papers / 5 sections + 6 runner-ups, `/list/{cat}/new` parse). This issue is therefore a **second-pass sweep of the unclaimed remainder of the Thu-24 window** from the AI & CTR angle — restricted to papers *not* claimed by either sibling or any earlier wiki page. All 23 curated arXiv IDs below (17 featured + 6 runner-ups) were grep-verified absent (0 hits) from the entire `wiki/`.

**CTR status**: still **zero direct end-to-end CTR/advertising-ML papers** in the unclaimed remainder — the ~11th–12th consecutive window with a direct-category drought, consistent with both siblings' reads. The window's rec/ads marquees (DSI distributional watch-time 2609.28383, LLM-vs-aggregate profiling 2609.27183, agentic shopping 2609.28372, XAI-for-seq-rec 2609.27201) were claimed by [[arxiv-daily]]. The CTR-relevant remainder here is the *decision-and-measurement scaffold*: experimentation credibility (quasi-experiment power calibration, agent-based population experiments), the statistics/AUC objective layer CTI scores actually optimize (AUC-bound self-optimization, tree-boosted tabular meta-learning, online-LP allocation), and the evaluation-instrument reliability that governs whether any CTR/rec claim can be believed.

---

## ① Evaluation Instruments & Benchmark Validity (5)

### Uncheatable Eval: Dynamic Compression-Based Evaluation of Language Models
- **Authors**: Kaifeng Tan, Yudong Li, Linlin Shen
- **arXiv**: [2609.27510](https://arxiv.org/abs/2609.27510) — cs.CL, cs.AI
- **Key contribution**: A **contamination-resistant eval** for *base* LLMs (whose poor instruction-following complicates task-based scoring): periodically sample newly published text and score models by **lossless compression rate** (predictive ability ⇔ compressibility). Evaluates **80 models across 14 text categories**, and reports: (1) compression follows a consistent scaling trend with model size; (2) attention vs hybrid vs recurrent models differ in *how* compression changes with context length; (3) **lower compression strongly correlates with higher zero-shot MMLU accuracy** — an external validation of MMLU as a capability proxy, plus a headless scoring path for pre-release/un-instructed models.
- **Why it matters**: A concrete answer to benchmark contamination that the wiki's eval line keeps hitting: dynamic, fresh-text compression scoring makes model evaluation *not gameable by pretraining on the benchmark*. Pairs with the sibling-claimed leaderboard-sensitivity work ([[arxiv-daily]] 2609.28398) as the two poles of eval-hygiene: fresh data (here) and hidden-selection audit (daily).

### Same Scores, Different Decisions: Evaluating JEV and Language Models for Legal Document Understanding
- **Authors**: Fan Zhang, Yankai Chen, Zhuohan Xie, Yixi Zhou, Sijia Peng, Lei Fan, Xinhua Ji, Cunyuan Zheng, Huangyong Shan, Philip S. Yu, Xue Liu, Yu Chen, Preslav Nakov, Songwei He
- **arXiv**: [2609.27678](https://arxiv.org/abs/2609.27678) — cs.CL
- **Key contribution**: On **ContractNLI**, JEV is compared with nine language models under controlled variations of hypothesis visibility, requested outputs, and output order (contract and target judgment fixed). **Aggregate accuracy conceals decision-level change**: rankings by baseline accuracy differ from rankings by correctness across *every* request condition — and repeated agreement is not evidence of correctness (a model can consistently return the wrong answer). Development diagnostics uncover **compensating corrections and regressions** (errors cancelling in the aggregate). JEV wins on cost and median response time; hosted models win raw accuracy — but the two leaderboards do not line up.
- **Why it matters**: The cleanest "aggregate-vs-decision" audit in this window — directly extends the 09-23 finding that constrained heads follow option *names* ([[arxiv-paper-check]] 2609.26758): evaluation must track *which individual judgments change*, not just average scores. A contract for judge/legal-type bet-against-metric checklists in production rec/ads.

### The Path Matters: Evaluating Small Language Models Beyond Answer Accuracy in KGQA
- **Authors**: Eduin E. Hernandez, Sergio A. Diaz, Luis F. Garcia, Nurassyl Askar, Stefano Rini
- **arXiv**: [2609.27669](https://arxiv.org/abs/2609.27669) — cs.CL, cs.AI
- **Key contribution**: Isolates **navigation capability** from end-to-end KGQA by using the **THESEUS** framework: frozen off-the-shelf SLMs act as local action policies — at each hop they pick one executable legal graph action or stop, with no parameter updates, no beam search, no free-form generation. Evaluation uses **Hits@1 (terminal answer)** and **Path Edit Distance (PED, trajectory fidelity)**. On Kinship and MQuAKE-ST, similarly sized local models differ substantially in both metrics — and the two metrics *frequently favor different models*. A single demonstrated trajectory improves or degrades navigation depending on the model.
- **Why it matters**: Decomposing "right answer" from "right path" is the KGQA analog of the construct-validity theme: pipeline credit assignment (search vs reasoning vs generation) is unobservable from endpoints alone. Adds a path-fidelity measurement to the wiki's KG/retrieval-reasoning thread ([[Knowledge-as-Skill]]-adjacent).

### Exact Feedback Is Not Control: Evaluating Text-Based Closed-Loop Revision in LLMs
- **Authors**: Haitong Jiang, Chunlin Liu, Yile Wang, Yuhong Feng
- **arXiv**: [2609.28150](https://arxiv.org/abs/2609.28150) — cs.CL
- **Key contribution**: A **fixed-budget revision protocol with deterministic verifiers** that enumerate ALL remaining violations (exact-length, lexical, compositional constraints) — fixing feedback correctness/completeness so that only *model-side revision* is measured. Across **19 open- and closed-source models**, final joint success ranges **17.4% → 99.8%**; post-training and scale reshape responses without bringing them consistently closer to exact correction; failed trajectories frequently **repeat earlier outputs**, and prior recurrence predicts lower recoverability. Removing earlier dialogue (holding current draft + feedback fixed) changes recurrence-escape *without* reliably improving final success.
- **Why it matters**: "Give the model the exact, complete target and it will converge" is falsified at the controller level — a sharp, reproducible bound on how much closed-loop self-correction you can bank on. Directly useful to any LLM-instrumented editing/verification pipeline in rec/ads (creative copy, landing pages) and to the eval-thread's rule that feedback quality and model response must be separated.

### When Visual Quality Misleads: Intent Recognition under Rendered Avatar Distortions
- **Authors**: Ning-Hsuan Chang, Kai-Siang Ma, Yu-Chih Chen
- **arXiv**: [2609.27560](https://arxiv.org/abs/2609.27560) — cs.MM, cs.CV, cs.HC
- **Key contribution**: Tests the industry assumption that IQA/VQA fidelity proxies communicative success. **59 participants → 2,688 judgments** over a pristine condition and 14 distortion families. **31/126 content–condition cells (24.6%) exhibit "Misleading Quality"** — above-average perceived quality, below-average action-recognition accuracy (temporal 50.0%, geometric 31.1% rates). A behavioral target **Intent Quality Score (IQS)** (recognition correctness × confidence) is matched against 24 IQA/VQA metrics + 3 supervised baselines; best alignment only **PLCC 0.4435**. Visual fidelity alone does not predict communicative success.
- **Why it matters**: A controlled demonstration that "quality" is task-decomposable, not monolithic — the measurement target must be chosen to match the *downstream decision* (intent/engagement), a lesson that transfers directly from avatar-streaming to content-quality scoring in rec/ads where perceptual-quality surrogates stand in for business goals.

---

## ② Statistics, Experimentation & Decision Layer (5)

### Beyond the Illusion of Power: Calibrating Quasi-Experiments in Observational IS
- **Authors**: Spandan Ghose Chowdhury
- **arXiv**: [2609.27299](https://arxiv.org/abs/2609.27299) — stat.ME, cs.AI, cs.LG
- **Key contribution**: Monte Carlo study over **9,837 parameter conditions (≈9.8M datasets)** decomposing the **planned-vs-achieved power gap** for DiD and IV designs. The serial-correlation component is recoverable by an AR(1)-aware calculator; **attrition, staggered-adoption bias, and parallel-trends pretesting are captured by no closed-form formula** — exogenous attrition alone costs **~8–11 pp** at the few-hundred-to-thousand sample sizes IS studies use, and treatment-correlated / outcome-dependent attrition induces *bias*, not just power loss. For IV: holding first-stage **F** fixed, **larger N neither raises power nor curbs exclusion bias**; identification rests on instrument strength, not sample size.
- **Why it matters**: The statistical honesty contract behind every quasi-experiment — the wiki's [[online-controlled-experiments]] line gets a quantitative "your power calculator is lying in these specific ways" result. For economic/GT experiments and observational CTR-type evaluations, this is the calibration yardstick (bounds first, then N).

### Anomaly-Free Self-Optimization via AUC Bounds
- **Authors**: Kevin Wilkinghoff, Zheng-Hua Tan
- **arXiv**: [2609.27362](https://arxiv.org/abs/2609.27362) — cs.LG, eess.AS
- **Key contribution**: Prior work used *upper-bound AUC* (achievable area under ROC given pseudo-anomalies) to **select** a config from a finite candidate set; this paper turns the bound into a **differentiable, anomaly-free objective** to **directly optimize continuous parameters** — demonstrated on ensemble weights plus a learnable score-rescaling mechanism that adapts pseudo-anomaly scores beyond any predefined set. Achieves significant gains over configuration selection and prior development-set-based parameter selection, and is **less sensitive to pseudo-anomaly construction**.
- **Why it matters**: **AUC is the canonical CTR/ranking metric**; making a *bound* on it differentiable gives a principled way to optimize ranking systems when the positive class is scarce or the "anomaly" definition is under-specified. The CTR-adjacent flagship of this window's remainder — a statistics-first answer to optimizing rankings without clean labels.

### KITE: Scaling Jev Population Experiments with Sparse Flagship Calibration
- **Authors**: Hengyu Li
- **arXiv**: [2609.27535](https://arxiv.org/abs/2609.27535) — cs.MA, cs.CY
- **Key contribution**: **KITE** executes agent **population experiments** from a typed behavioral-kernel table (queried once per unique state) with event-keyed randomness and common random numbers; an expensive flagship model is reserved for **sparse paired anchors** estimating intervention effects, and measured human-model discrepancy is propagated as shared error. On Epstein experiments (9,070 participants), **1.7% anchor coverage cuts effect error 41%**; on 37 held-out SocSci210 experiments, 0.5–1.5% anchor coverage raises captured decision gain 0.27 → 0.39; shared-discrepancy coverage reaches 93%/96% at nominal 80%/90% (vs 29%/36% from sampling alone); a million agents ran 20 tabulated steps in 0.9 s on a laptop.
- **Why it matters**: Cheap, uncertainty-aware **pre-experiment screening**: decide whether an intervention is worth a real trial before running it, with calibrated error bars carried through every conclusion (property-specific evidence records). The experimentation-layer complement to 2609.27299 — one calibrates the human study, the other scales the simulated probe.

### NPBoost: Neural Processes with Gradient-Boosted Fixed Effects
- **Authors**: Andrea Nava, Ken Rölli, Armin Begic, Fabio Sigrist
- **arXiv**: [2609.28122](https://arxiv.org/abs/2609.28122) — stat.ML, cs.LG
- **Key contribution**: Extends the **Neural Process** line using the shared hierarchical view of meta-learning and mixed-effects models: **NPBoost decomposes response variability into tree-boosted fixed effects (shared across tasks) + NP random effects (stochastic task-to-task variation)**, trained jointly by a boosting algorithm where the NP learns residual task structure and the tree ensemble estimates common patterns. Beats a standard NP when the shared structure has **discontinuities or irregular patterns** that boosted trees represent well.
- **Why it matters**: The tree+NPs tabular hybrid is exactly the CTR/rec modeling shape the industry already runs (GBDT features + learned heads); a principled joint formulation instead of ensembling. Balances the wiki's [[tabular-classical-vs-llm]] thread with a strict statistical footing.

### Resource-Adaptive Stochastic Gradient Descent for Online Linear Programming
- **Authors**: Jiameng Lyu
- **arXiv**: [2609.28263](https://arxiv.org/abs/2609.28263) — cs.LG, math.OC
- **Key contribution**: **RASGD** for stochastic online LP (the allocation-workhorse of ads budget/pacing and cloud capacity): each arrival updates resource prices with **O(m) ops and memory per arrival** — no LP re-solving, no sample-average optimization; the stepsize shrinks early (stable learning) then grows to match inventory-adjustment speed. Feasible on **every sample path**, **O(log T) expected regret** vs the realized fractional hindsight optimum — matching the lower bound even for distribution-knowing, computationally-unbounded policies — and curvature conversion turns the fixed reference price into inventory stability.
- **Why it matters**: The math that ad-auction/pacing systems sit on: O(log T) optimal regret at first-order cost makes high-allocation-quality online pricing plausible at LLM-serving scale (the paper's stated motivation). Links the wiki's auction/mechanism-design layer to the serving-availability layer.

---

## ③ Agents: Memory, Control, Alignment & Safety (4)

### Alignment Inertia: Auditing the Durability of Training Data Influence Through Policy Override Resistance
- **Authors**: Renata Barreto, Markelle Roesti, Mohammad Tahaei
- **arXiv**: [2609.27333](https://arxiv.org/abs/2609.27333) — cs.AI
- **Key contribution**: Introduces **Override Success Rate (OSR)** and **alignment inertia** — how reliably system prompts / LoRA fine-tuning override behavior inherited from pretraining, evaluated on Llama and Mistral across medical misinformation and hate speech. Inertia persists across both models but varies by model, domain, and policy direction; strikingly, **in Mistral's restrictive hate-speech condition LoRA increased inertia by 46.5 pp** — fine-tuning *reinforced* rather than overrode prior behavior. **TRAK** (attribution) predicts which samples resist override with **AUC ≥ 0.85 in 7/8 conditions**, beating model confidence, TF-IDF, and embedding similarity.
- **Why it matters**: An operator-facing audit of where prior training constrains downstream governance — the durability question the wiki's alignment/data-influence thread keeps hitting. Also a direct warning: constrained-decoding/fine-tuning "alignment levers" can entrench the very behavior they are meant to remove.

### DRSR: Learning Set-Level Deletion Risk for Efficient Long-Horizon Agents
- **Authors**: Mingxuan Wang, Bo Wang, Fei Luo, Guorun Yao, Chao Ning, Yinglong Guo, Hongyue Chen, Yanbiao Ma, Jungong Han
- **arXiv**: [2609.27276](https://arxiv.org/abs/2609.27276) — cs.AI
- **Key contribution**: Frames agent-history compression as **risk-constrained selection over deletion sets**, not per-unit scores: redundant evidence and post-deletion remaining information matter jointly. Offline, DRSR builds exact counterfactual supervision (delete protocol-valid history blocks → measure change in teacher-forced next-output likelihood); a lightweight scorer predicts set-level harm from online-visible relations, and deployment removes the largest feasible set under recency/protocol/budget/risk constraints, **abstaining when no set is safe**. On **WorkBuddyBench Full260**: mean reward **0.699 → 0.802** while cutting tokens **20.82%**; 35.85% fewer tokens than uncompressed at fixed eval reward 0.794.
- **Why it matters**: Joint-deletion risk (not marginal) is the correct unit for agent memory — and explicit **abstention** (keep everything when unsure) is the safety valve commercial agents need. Strong counterpoint to the many "compress more, always" methods.

### Memory Control Signals Emerge Before Action in Long-Horizon Agents (PaMER)
- **Authors**: Mingxuan Wang, Guorun Yao, Fei Luo, Yinglong Guo, Chao Ning, Bo Wang, Hongyue Chen, Yanbiao Ma, Jungong Han
- **arXiv**: [2609.27286](https://arxiv.org/abs/2609.27286) — cs.AI
- **Key contribution**: Shows the **(de)compression and recall "intentions" are already encoded in the hidden state immediately before each agent action** — and are not explained by context length or interaction progress, with distinct formation patterns across model depth. Most memory-decision information is preserved in a compact recent context; selectively restored historical evidence fills the long-range gaps. **PaMER** (pre-action state-guided compression + external evidence retrieval) and **PaMER+** (step-level evidence selection) cut context consumption substantially on WorkBuddyBench across multiple baselines and backbones while holding task performance.
- **Why it matters**: Memory operations as *read from the model's own state* rather than imposed externally — the "ask the agent, don't guess the policy" result for context management, and a mechanistic sibling to DRSR (same group, same benchmark, complementary layers).

### CART: Closed-Loop Adaptive Red Teaming for Large Language Models
- **Authors**: Dongdong Zhang, Tengchao Lv, Yilin Jia, Yuzhong Zhao, Yupan Huang, Wenshan Wu, Xiangyang Zhou, Shaohan Huang, Nan Yang, Li Dong, Lei Cui, Furu Wei
- **arXiv**: [2609.27336](https://arxiv.org/abs/2609.27336) — cs.AI
- **Key contribution**: Red teaming as a **closed loop**: each result guides the next probe (broad coverage → follow emerging weaknesses → keep probes diverse → record evidence provenance), with a strict **Challenger / Target / Judge role split** (the Target may be text-only or a bounded tool-using agent). Across three evaluation families (Frontier, JAH, Agentic) CART discovers **more failures and higher average risk than static seed replay** for every Target with a baseline, including tool-mediated agents; Challenger–Judge choices demonstrably affect which evidence surfaces.
- **Why it matters**: Turns red teaming from a one-time checklist into a continuous, adaptive, *auditable* search — the reliable-finding generator that the eval-instrument section above consumes. Complements the [[arxiv-paper-check|day-23 paper-check]] red-team/robustness thread (adaptive-attack-red-teaming, conference-digest 09-23).

---

## ④ Retrieval, Temporal & Representation (3)

### MORSE: Multi-Context Ordering via Reverse Scoring for Evidence-Preserving Compression
- **Authors**: Ke Wan, Yifan Wang, Liheng Lai, Chen Chen
- **arXiv**: [2609.27380](https://arxiv.org/abs/2609.27380) — cs.CL
- **Key contribution**: Shows likelihood-based context compression is **order-sensitive to a named mechanism — information preemption**: earlier partially relevant contexts absorb credit for shared information, suppressing the incremental score of later stronger evidence carriers and raising their deletion risk (pair-swap interventions confirm evidence-first ordering substantially improves supporting-evidence survival). **MORSE** applies a common reverse query-evidence principle to both individual contexts and compressed candidates: an evidence-first anchor plus compression-aware permutation selection. Consistently improves evidence preservation over static reverse ordering and compute-matched random search across multi-hop QA benchmarks, compressors, budgets, and scorers.
- **Why it matters**: Ordering as a first-class design variable in context compression — fixes a failure mode the wiki's long-context/compression thread keeps rediscovering (evidence dropped not because it was weak, but because it read *late*). Cheap, mechanism-driven, and directly relevant to rerankers and RAG staging.

### TEMPS: Temporal Sentence Embeddings for Temporal Information Retrieval
- **Authors**: Mourad Hassani, Julien Romero, Amel Bouzeghoub, Christian Jacquelinet
- **arXiv**: [2609.28048](https://arxiv.org/abs/2609.28048) — cs.CL, cs.AI
- **Key contribution**: Defines **Temporal Textual Similarity (TTS)** — do two anchored texts align in *time*, independent of topic — and trains **TEMPS**, a modular temporal branch on a **frozen semantic retriever**, supervised without any hand-labeled temporal data: anchored temporal expressions resolve to intervals, moment-matched to Gaussians, with an ordering that supervises an anchor-date-conditioned encoder (score = Gaussian-KL inclusion measure, fused with the semantic score). On three temporal benchmarks, TEMPS improves **MRR for every semantic backbone tested**; on TS-Retriever it lifts R@1 **19.92 → 25.39** past the prior temporal SOTA.
- **Why it matters**: "On topic but temporally wrong" is a classic failure of dense retrieval and RAG (news, legal, clinical, and rec-side freshness). A label-free modular bolt-on for time-awareness fits directly into the wiki's retrieval/RAG line.

### LLMAE: Repurposing Pre-trained LLMs as High Fidelity Continuous Text Autoencoders
- **Authors**: Arkanath Pathak, Unnat Jain, Alexander C. Berg
- **arXiv**: [2609.27248](https://arxiv.org/abs/2609.27248) — cs.LG
- **Key contribution**: Text lacks the high-fidelity continuous latent space that image autoencoders gave generative modeling. **LLMAE** repurposes a pretrained decoder-only LLM by exposing an **intermediate fixed-length latent bottleneck** inside its activations — implemented on a 270M Gemma 3 with structured attention masks, LoRA, and KL regularization — reaching **near-perfect reconstruction of sequences up to 1024 tokens**, then demonstrates downstream utility by training a **latent text-diffusion model for detailed image captioning** on those latents.
- **Why it matters**: The missing continuous-text primitive: a fixed-length, lossless-ish latent that opens latent-space operations (diffusion, interpolation, retrieval-reasoning) over text — a plausible substrate for compressed text representations in IR/rec and for latent reasoning. Cross-links to the window's [[arxiv-ai-search]] Memory Attention / token-indexed memory line.

---

## Cross-Cutting Themes

1. **Instrument validity keeps winning the window**: the sharpest findings are not about model power but about *whether the measuring device measures what we think* — uncheatable fresh-text compression scoring, aggregate-vs-decision audits, path-vs-answer decomposition, exact-feedback-still-not-control, and perceived-quality-vs-intent dissociation. Benchmark-level accuracy is no longer the frontier; what the score changes when the *protocol* changes is.
2. **The decision layer as the CTR-adjacent story**: with a direct CTR drought, the actionable content clusters around *how decisions are made and validated* — AUC-bound optimization (the CTR metric itself), power-calibrated quasi-experiments, no-resolve online LP pricing (O(log T) regret), tree-boosted tabular meta-learning, and agent-population pre-experiments. Statistics and mechanism-design are where advertising/CTR value surfaces this window.
3. **Agent memory matures into risk management**: DRSR reads memory compression as set-level deletion *risk* with abstention; PaMER reads (de)compression intentions from hidden state *before* action; Alignment Inertia shows fine-tuning can *entrench* prior behavior (+46.5 pp inertia). Together: memory and alignment controllers now publish risk-aware, auditable behavior rather than raw compression wins.
4. **Retrieval/representation engineering is modular**: TEMPS bolts time-awareness onto frozen retrievers without labels; MORSE fixes compression *ordering*; LLMAE supplies a continuous-text latent. Each is a drop-in mechanism rather than a new architecture — the bricklaying the industry can actually adopt.
5. **CTR**: the **~11th–12th consecutive window** without a direct end-to-end CTR-model paper in the unclaimed remainder (siblings agree). The window's closest value-layer flagships ([[arxiv-daily]] DSI watch-time 2609.28383, [[arxiv-ai-search]] credible auctions 2609.27402) remain sibling-claimed; this report's CTR-adjacent contribution is the measurement/decision scaffold in ①② above.

---

## Method Note

Thursday fresh mailing (Wed Sep 23 submissions, Thu 24 Sep 2026; IDs **2609.26809–2609.28473**). Pool: arXiv API tail sweep (8 categories cs.AI / cs.LG / cs.IR / cs.CL / cs.CV / cs.GT / cs.MA / cs.NE, 2 pages × 100, cached in `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-paper-check-0924/`) → **1,385 unique entries → 332 fresh in-window** (published 2026-09-23). Sibling dedup: today's [[arxiv-daily]] (52 claimed IDs) and [[arxiv-ai-search]] (27 claimed IDs) removed → **260 unclaimed** after intersecting the full wiki-context known set (incl. log/index references, which caught two more sibling-claimed IDs — FWBench 2609.27385 and SCFF 2609.28208 — that a page-only diff would have missed). Keyword/abstract screen on the AI & CTR angle (evaluation validity, statistics/decision/experimentation, agent memory/alignment, retrieval/temporal/representation) → **17 featured + 6 runner-ups**. Every curated ID grep-verified **0 hits in `wiki/`** at write time (23/23). Affiliations author-inferred/tentative only where arXiv prints none. **Window's rec/ads marquees and mechanism-design value layer were claimed by today's siblings — this issue mines the remainder.**

**Runner-ups** (0-hit verified, not featured): 2609.27279 **EnSIMem** — entity-structured `[entity][type][property:value]` long-term agent memory with episode-level provenance, high accuracy at compact contexts (Xing Fan / Chenlei Guo / Jiawei Han group); 2609.27297 **Large Knowledge Model** — papers-as-reasoning-graphs → Question/Workflow/Evidence Landscape, retrieval lifts +9.30% ChemBench / +4.20% PubMedQA / +14.69% SciBench; 2609.28041 **Self-Conditioning** — unsupervised information-theoretic estimator separates fully-delegated from machine-polished peer reviews (AUC up to 1.0, monotone in external info, high-temperature evades at quality cost); 2609.27517 **NAFBench** — can LLMs follow a *specified* negation semantics (SLDNF/WFS/credulous/skeptical), open-source 31–74%, two frontier models 100%, order-sensitivity on >half of logically-identical shufflings; 2609.27311 **Multi-View Fusion for Encrypted C2 Detection** — leakage-controlled eval pitfalls study: fold-leaking preprocessing inflates F1 by 0.28 (10× the real effect), endpoint-level positive rate 55.1%→4.2%, 20/62 captures label-gapped — "the evaluation design is the main result"; 2609.27452 **Issuer-Sovereign Agentic Payments** — agentic payments where the issuer's own auth records the approved spending rule and validates each merchant at execution time, keeping control on-card-holder rails.

**Next fresh window**: Fri Sep 25 2026 (Thu 24 Sep submissions).