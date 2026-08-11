---
title: "arXiv Daily Digest — 2026-08-10"
type: synthesis
created: 2026-08-10
updated: 2026-08-10
sources: [arxiv-cs.CL, arxiv-cs.LG, arxiv-cs.AI, arxiv-cs.GT, arxiv-cs.IR]
tags: [arxiv, llm, reasoning, post-training, agents, skills, memory, sequential-modeling, time-series, world-models, recommendation, advertising, auctions, quantization, efficiency, evaluation, games]
---

# arXiv Daily Digest — 2026-08-10

> **Batch note:** arXiv announces new submissions Mon–Fri; Sat Aug 8 and Sun Aug 9 had **no announcements**, so today's **Mon Aug 10, 2026** listing is the **first fresh batch since Fri Aug 7** (papers submitted Aug 7–9; IDs span ~2608.06394–2608.07457). Today's [paper check](../2026-08-10/arxiv-paper-check.md) already curated the cs.AI/cs.IR flagship cluster (36 papers: SYF, HD-Rec, TM20K, MISO, WebGrader, ResidencyRL…), the [game-rl-daily](../2026-08-10/game-rl-daily.md) the games/world-model cluster (13 papers), and the [conference-digest](../2026-08-10/conference-digest.md) the big-company arXiv picks. This digest is therefore a **zero-overlap breadth pass** over the same Monday batch's **cs.CL / cs.LG / cs.GT streams and the uncovered remainder of cs.AI/cs.IR** — 25 papers, all grep-verified absent from the wiki. Signature themes of this remainder: **warm-up/initialization demystified in OPSD**, **KV-cache compression as global resource allocation**, **step-level supervision densification across the long-horizon stack**, **retrieval as a training-free inductive bias for time-series forecasting**, and **auction/attention-allocation mechanisms for social feeds**.

---

## 1. LLM Post-Training, Reasoning & Inference Efficiency

### Simple-OPD: Demystifying Warm-up for On-policy Distillation
- **Authors**: Tao Liu, Taiqiang Wu, Mao Zheng, Xuan Luo, Runming Yang, Xuewei Yang, Junjie Wang, Yujiu Yang
- **Institution**: Tsinghua Shenzhen SIGS (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06802](https://arxiv.org/abs/2608.06802)
- **Abstract**: OPD effectiveness depends strongly on the warm-up stage before distillation. This paper demystifies warm-up from data and training perspectives. Data-wise, effective warm-up relies on **teacher-compatible chain-of-thought supervision** — and even *incorrect* teacher rollouts provide comparable benefits to correct ones, implying warm-up transfers a teacher-compatible thinking *pattern*, not merely correct answers. Training-wise, **LoRA with near-saturation training duration** balances in-domain adaptation and OOD generalization better than full-parameter SFT. Simple-OPD is a plug-and-play initialization that warms the student on teacher-generated CoT with LoRA before OPD.
- **Key Innovation**: The first systematic account of *why* OPD warm-up works (thinking-pattern transfer, not answer transfer) and a plug-and-play LoRA-based recipe that removes the tuning burden — extending the wiki's OPSD cluster (Aug 7 DASH/AgentOPSD, Aug 8 U-OPSD/Hyper-ES) to the initialization axis.

### FutureBridge: Token Selection Beyond Local Preference in Collaborative Decoding
- **Authors**: Quanquan Li, Hongbo Zhang, Yihe Chi, Jingyu Li, Xidong Xi, Liuyang Song, Hongzhen Zhang, Yuxiang Huang, Jing Ke, Siyuan Ma, Junyi Lin, Guitao Cao
- **Institution**: East China Normal University (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06819](https://arxiv.org/abs/2608.06819)
- **Abstract**: Token-level collaboration lets an LLM assist a small LM (SLM) when predictions diverge, but existing methods rank candidates by the LLM's *local preference* — even though an LLM-selected token may be hard for the SLM to build on. FutureBridge ranks joint LLM–SLM candidates by **how well they support the SLM's subsequent reasoning**: during training an answer-verified LLM trajectory fixes a shared future and a frozen SLM evaluates each candidate under that common context, producing counterfactual scores that supervise a lightweight token reranker. At inference the LLM only expands the candidate pool; the SLM selects and continues. On five math benchmarks FutureBridge improves Qwen3-1.7B's Math Avg by **35.1% relative to greedy SLM decoding**.
- **Key Innovation**: Reframes speculative/collaborative decoding as *counterfactual usefulness to the receiver* rather than *fluency of the proposer* — a measurable answer-verified criterion for when an LLM should overrule an SLM.

### Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration
- **Authors**: Ruochen Jin, Zhanliang Wang, Zongyu Dai, Jiancong Xiao, Bojian Hou
- **Institution**: University of Pennsylvania (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07419](https://arxiv.org/abs/2608.07419)
- **Abstract**: Preference alignment makes LLMs overconfident and poorly calibrated, and post-hoc temperature scaling is domain-dependent: a temperature fitted on one domain does not generalize. The paper instead modifies model parameters during training, maximizing **predictive-distribution entropy** as the calibration objective to directly target overconfidence. It is realized as a **bilevel optimization** — the lower level trains under a parametric loss, the upper level selects loss hyperparameters to maximize entropy — with an efficient first-order approximation avoiding second-order computation at LLM scale. Across multiple-choice and open-ended QA, the method yields well-calibrated LLMs with particular gains in out-of-domain generalization.
- **Key Innovation**: Moves calibration from post-hoc scaling into training as a parameter-level objective (bilevel entropy maximization), fixing the domain-dependence of temperature scaling.

### Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating with MemGLU
- **Authors**: Yuting Ge, Pengju Yang, Mingkai Nie
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.07323](https://arxiv.org/abs/2608.07323)
- **Abstract**: Decoder-only LM FFNs have converged on SwiGLU, whose gating activation has an open positive tail. MemGLU, a closed-tail comparator derived from a memristive branch geometry, stays within ~0.1% of SwiGLU validation NLL across paired 9M/30M pretraining runs (three seeds). Trained SwiGLU checkpoints are sensitive to positive-tail suppression, yet mechanism diagnostics show the two models **use their gates differently despite similar losses** — models adapt to the gate geometry available during pretraining. Conclusion: at tested scales, SwiGLU's open positive tail is not necessary.
- **Key Innovation**: A controlled negative result on a settled architectural assumption — closed-tail gating matches SwiGLU within 0.1% NLL, suggesting gate *geometry* is an adaptable design dimension rather than a fixed requirement.

### CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights
- **Authors**: Xuetian Gao
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.06763](https://arxiv.org/abs/2608.06763)
- **Abstract**: Weight quantization must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution. CubicQuant is a parametric non-uniform scalar format that keeps a dense integer code stream while adapting reconstruction levels per weight group: a monotonic **cubic curve** (two shape parameters + one scale) maps uniform magnitude codes to non-uniform levels. It spans 1–8-bit payloads, contains symmetric uniform integer quantization as an exact special case, and has effective width B + 64/G bits per weight. At G=128, W4 CubicQuant cuts reconstruction RMSE vs optimally-clipped 4-bit uniform quantization by 3.90% (Uniform) / 13.49% (Gaussian) / 28.14% (Laplace), and beats the best enumerated 4-bit floating-point format by up to 9.44%. H200 kernels show a workload-dependent crossover between model-dtype and Dynamic A8 execution.
- **Key Innovation**: A quantization format family that is *both* non-uniform *and* directly GPU-executable — dense integer codes plus a closed-form monotonic mapping, avoiding the irregular decoding and metadata overhead of learned codebooks.

### Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression (GraceKV)
- **Authors**: Haolin Tian, Yuzhe Liu, Tonghan Wang
- **Institution**: KAIST (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07001](https://arxiv.org/abs/2608.07001)
- **Abstract**: Existing KV cache compression relies on fixed per-layer/head rules for either eviction or merging, so cache resources can neither flow across layers/heads/context slots nor be jointly allocated between local resolution and information coverage. GraceKV frames compression as a **global resource-allocation problem under a fixed cache budget**: each layer-head-slot is an atomic unit built as a prototype tree; adding a tree root expands coverage while splitting a node improves resolution, and all candidate actions compete globally for shared budget. Training-free and GPU-resident, GraceKV ranks first in 24 of 32 long-context settings and stays robust up to **128× compression**.
- **Key Innovation**: The first treatment of KV cache compression as *global* budget allocation across resolution and coverage (trading off eviction vs merging), rather than a per-head heuristic — a systems-level companion to the wiki's cache line (QEvict, ResKV, NOVA-KV).

### Modular TTT: Rethinking Test-Time Training as Composable Modules
- **Authors**: Bohao Tang, Zhen Qin, Yuqi Pan, Zheng Li, Pengfei Liu, Ya Zhang
- **Institution**: Shanghai Jiao Tong University (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07110](https://arxiv.org/abs/2608.07110)
- **Abstract**: Test-time training (TTT) variants are each hard-coded, making design and ablation hard. Modular TTT represents the inner learner as a **directed acyclic graph** and exposes fast-weight network, loss, learning rate, weight decay, and normalization as explicit dimensions, automatically composing primitive train-view forward/backward and causal query-view rules into the full TTT computation. Systematic ablations find: small LR initialization, weight decay, and single-layer nonlinearity help; MSE and inner-product losses perform similarly; deeper fast-weight nets and normalization hurt (excessively large activations); residual connections/gating add little. The best variant trains 410M/1.45B models on 100B tokens with loss/benchmarks comparable to Gated DeltaNet.
- **Key Innovation**: Turns TTT from a zoo of bespoke variants into a composable framework with honest component-level ablations — clarifying *which* TTT design choices actually matter.

### Faster Query-Key Learning Sharpens Attention in Self-Attention Models
- **Authors**: Rahul Vashisht, Harish G. Ramaswamy
- **Institution**: IIT Madras (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06776](https://arxiv.org/abs/2608.06776)
- **Abstract**: A self-attention layer couples two circuits: query-key (attention allocation) and output-value (prediction). Collapsed vs factorized parameterizations yield qualitatively different attention patterns — some give sharper attention to task-relevant tokens at similar loss. Through gradient-flow analysis the paper shows factorization induces **implicit rescaling of the two circuits' learning rates**, and derives closed-form dynamics: parameters move along a line with relative speed set by the learning rates. Faster query-key learning relative to output-value learning produces sharper attention (the model compensates for slower output-value learning by concentrating attention mass). Experiments confirm relative learning-rate differences govern attention concentration, improving interpretability proxies at comparable predictive performance.
- **Key Innovation**: A mechanistic explanation for attention sharpening — factorized QK parametrization implicitly rescales learning rates, so attention allocation is controllable via the two circuits' relative learning speeds.

---

## 2. Mechanistic Understanding, Generalization & Evaluation

### Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization in Language Models
- **Authors**: Zili Zhang, Yilin Wang, Heng Wang, Herun Wan, Minnan Luo
- **Institution**: Xi'an Jiaotong University (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07261](https://arxiv.org/abs/2608.07261)
- **Abstract**: LLMs solve complex multi-hop problems yet fail on simple two-hop queries despite storing each hop. Training transformers from scratch in a controlled symbolic environment, the authors find a sharp pattern: models generalize reliably when the **second hop follows the training distribution and always fail when it deviates**. Mechanistic analysis: success is driven by *consistent intermediate representations* for the same entity across contexts; OOD-second-hop failure arises from a **layer mismatch** — lower layers construct the intermediate representations correctly, but upper layers, trained on corresponding atomic facts, learn to map them to outputs rather than reason over them. A **recurrent-style training strategy** that reuses reasoning circuitry across input forms substantially improves OOD two-hop generalization.
- **Key Innovation**: Localizes two-hop failure to the lower/upper-layer boundary (representation construction vs reasoning) and offers a training fix (circuit reuse) — a precise mechanistic account of compositional failure.

### Post-Grokking Collapse at the Representation-Readout Interface in Muon-Trained Transformers
- **Authors**: Ali Janati, Kaoutar El Maghraoui, Andrei Kanavalau, Anass Belfatmi
- **Institution**: IBM Research (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07436](https://arxiv.org/abs/2608.07436)
- **Abstract**: Under the standard split, Muon gets hidden matrices while AdamW handles embeddings/output head. Muon groks modular addition *faster*, but **its solutions do not hold**: all nine configurations on (a+b) mod 113 grok then lose generalization (the AdamW reference falls below threshold in four of five seeds). The failure localizes to the representation–readout interface, identified only jointly up to an invertible map the loss does not select. Post-solving the training set, gradient drops to ~1e-6 and the optimizers diverge: step-size elasticity −0.03 (Muon) vs +1.5 (AdamW), Muon group moving 8× faster per parameter. **Freezing either group prevents failure**; removing Muon's normalization/orthogonalization collapses the representation (326 effective conjugate pairs → 4) and fails terminally. Fourier filtering separates "circuit failure" (task-aligned family no longer solves) from "masking" (family stays perfect at 100% while the full model drops to 45.85%, outvoted by a near-equal adversarial remainder); rescaling restores 99.9%.
- **Key Innovation**: A reproducibility-critical finding that Muon's fast grokking on modular arithmetic is not stable — post-grokking collapse arises at the representation-readout interface, with freezing the embeddings/readout as the minimal fix.

### Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination
- **Authors**: Ruijie Hou, Yueyang Jiao, Zhao Wang, Yingming Li
- **Institution**: Zhejiang University (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07341](https://arxiv.org/abs/2608.07341)
- **Abstract**: Contamination mitigation evaluation's dominant metric, **G-AP** (Gap of Aggregate Performance), is flawed: discrete correct/incorrect readouts cannot characterize per-question performance, averaging-before-differencing lets over/under-suppression cancel, and uniform per-question weighting invites gaming. The paper proposes **SA-PPG** (Stratified Aggregate of Per-question Probability Gaps): estimate each question's solve probability by sampling, difference per-question against the clean model, and aggregate within groups stratified by clean-model probability. It also introduces **RailCap**, which judges contamination *during generation*: whenever a sample falls back onto the greedy trajectory, the next trajectory token is capped to the runner-up, accumulating suppression until the response distribution disperses. SA-PPG reveals prior strategies' restoration is substantially overestimated; RailCap attains the lowest SA-PPG.
- **Key Innovation**: A corrected metric (per-question, stratified probability gaps) showing contamination-mitigation restoration claims are inflated, plus a decoding-time-only mitigation that needs no contamination-location estimate.

### SABRE: Scalable and Automated Benchmarking of VLMs under Stress
- **Authors**: Zixuan Lan, Luzhe Sun, Matthew R. Walter, Jiawei Zhou
- **Institution**: Northwestern University (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07435](https://arxiv.org/abs/2608.07435)
- **Abstract**: VLM stress-test construction is costly — samples must satisfy controlled conditions, remain answerable, and challenge current models. SABRE is a scalable automated pipeline converting a Test Primer (Markdown task design + data schema) into structured specs, generated/edited images, and QA pairs, with automated VLM filtering plus human review. SABRE-Prior tests whether VLMs follow visual evidence instead of world priors: 600 images / 1,000 questions span Context (unexpected entities), Texture (counterfactual materials), Attribute (noncanonical counts), and Language Elicitation. Across six VLMs, macro-average accuracy is only **17.8%–31.3% (22.6% mean)**. SABRE-Counting/Spatial pilots show workflow generality.
- **Key Innovation**: Positions stress-testing as a *reusable pipeline*, not a fixed benchmark — the priors-vs-evidence failure mode (VLMs at ~23% on prior-violating images) is the headline result.

### From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL
- **Authors**: Jiaqian Wang, Yutao Qi, Wenjin Hou, Yuanxi Che, Muning Wen
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.07213](https://arxiv.org/abs/2608.07213)
- **Abstract**: Test-time scaling corrects difficult text-to-SQL queries but the extra computation is normally discarded. Systems increasingly retain verified repair episodes, yet evaluation reports one end-to-end score that cannot distinguish replay-on-recurring-questions from help-on-unseen-questions. The authors call measuring this future value the **crystallization problem** and run a controlled evaluation holding the single-shot solver fixed while varying one memory choice at a time. On BIRD, storing verified corrected queries improves held-out first-attempt accuracy by **4.34 pp**, capturing 44.4% of the headroom provided by on-demand repair. Interventions identify **database-specific content** as the main operating ingredient; reliable verification and broader retrieval coverage yield supported gains, while richer formats and elaborate retrievers do not.
- **Key Innovation**: Names and measures "crystallization" (test-time compute → reusable memory) with a controlled protocol, and shows *what* is worth storing: database-specific content under reliable verification, not fancier memory formats.

---

## 3. Agents, Skills, Memory & Safety

### The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents
- **Authors**: Mingguang Chen, Licheng Wang, Bo Qu
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.06663](https://arxiv.org/abs/2608.06663)
- **Abstract**: A 1,547-paper survey (2024–2026) on why frontier models fail at multi-hour tasks — losing track of decisions, declaring half-finished work done, drifting from goals. It disambiguates three routinely conflated properties: **long-horizon** (task property: required steps), **long-context** (model property: token capacity), **long-term memory** (system property: persistence). The corpus is organized into six lifecycle categories (planning, memory, execution, training, evaluation, foundations/safety) crossed with where horizons are carried (within-context / within-task-beyond-context / cross-task-persistent). The recurring finding: **outcome-only signals grow uninformative as horizons lengthen**, and the field's response — process reward models, credit assignment, trajectory-level diagnostics — manufactures denser step-level signals.
- **Key Innovation**: A lifecycle-organizing synthesis that separates the three "long-*" properties and argues the field-wide response to long-horizon unreliability is step-level signal densification — a useful map for the wiki's agent-reliability cluster.

### HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses
- **Authors**: Xiao Zhang, Yusheng Wang, Yuhao Fei, Dongyuan Li, Zian Liang, Liuyu Xiang, Hongxun Gu, Zhaofeng He
- **Institution**: Beijing University of Posts and Telecommunications (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06984](https://arxiv.org/abs/2608.06984)
- **Abstract**: Agent harnesses persist state through **persistent carriers** (memory, skills, tools, shared artifacts), creating delayed safety risks: attacker-influenced content can cross system boundaries and affect later benign requests. HarnessSafe is a benchmark of 328 executable cases across seven persistent-carrier families evaluated on most mainstream harnesses. Each case is a **Persistent-Risk Lifecycle** tracing attacker influence from initial entry, through persistence across carriers and boundaries, to a later benign trigger and observable violation. A multi-stage, trace-based evaluation uses observable execution evidence to determine how far each attack chain progresses. Findings: containment is carrier-specific and strongly depends on the harness–model configuration — attack-success rates alone cannot reflect distinct lifecycle progression patterns.
- **Key Innovation**: Shifts agent safety evaluation from end-to-end attack success to *lifecycle progression and containment per carrier* — the delayed-risk counterpart to today's NiyamAI/guardrail line.

### Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework
- **Authors**: Jing Chen, Yang Sun, Li Zhang, Lin Xu, Jie Shi
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.06909](https://arxiv.org/abs/2608.06909)
- **Abstract**: Long-horizon agent benchmarks evaluate outcomes but not fine-grained attribution — *which* component (instruction, tool call, observation, memory) caused an outcome. This work defines trajectory attribution and builds a benchmark + annotation framework: heterogeneous trajectories under a unified component schema with annotations of the primary attribution component plus attack/execution chains. Instantiated with AgentDojo and Agent3Sigma trajectories, it yields 1,300+ annotated trajectories covering task-aligned actions, unsafe actions, and safety refusals, with two tasks (attribution localization and attribution-chain recovery) and reference baselines (incremental contribution, component-level leave-one-out). Baseline results show substantial difficulty variation across local/long-range and chain settings.
- **Key Innovation**: A reusable annotation skill + benchmark making "why did the agent do that" a measurable task — a debugging companion to the wiki's audit/attribution thread (SearchAuditor, SkillTrace).

### Online Monitoring and Corrective Steering of Programming Agents (LivePlan)
- **Authors**: Shuyang Liu, Saman Dehghan, Ji Young Kim, Jatin Ganhotra, Martin Hirzel, Reyhaneh Jabbarvand
- **Institution**: IBM Research / UIUC (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06701](https://arxiv.org/abs/2608.06701)
- **Abstract**: Long-horizon GitHub-issue-fixing agents drift from plans, repeat failed actions, or terminate without a patch. LivePlan **decouples judging from advising**: a deterministic, rule-based monitor checks general trajectory signals without invoking an LLM, and only when an issue is detected does an advisor LLM supply a high-level next-step correction — avoiding the misleading re-planning and costly interventions of prior approaches. Built on SWE-agent and evaluated with three executors + two advisors across SWE-bench Verified/Pro, it raises resolution rates by up to **15.2% (avg 9.9%)** at only $0.08/instance extra cost, with gains concentrated on medium/hard instances and minimal regression on already-successful runs.
- **Key Innovation**: A cheap, deterministic monitor that decides *when* to advise — an explicit separation of detection (rules, no LLM) from correction (LLM), the inverse of the "reason every turn" pattern.

### SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time
- **Authors**: Qinfeng Li, Dalin He, Yuntai Bao, Ying Yang, Ruoxi Chen, Xinyan Yu, Lizhou Liang, Ge Su, Wenqi Zhang, Xuhong Zhang
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.06880](https://arxiv.org/abs/2608.06880)
- **Abstract**: Semantic relevance of a retrieved skill does not guarantee execution utility — a skill may encode assumptions conflicting with the current task, environment, or other retrieved skills (the **skill–execution misfit**). SkillAligner is a training-free, execution-time adaptation framework treating skills as **adaptable drafts**: before execution, a one-time joint adaptation specializes useful skill fragments to task requirements, aligns procedural assumptions with the execution interface, and composes guidance by resolving dependencies/conflicts/redundancy, consolidating into a compact execution guide reused across the trajectory. It improves task performance over skill-use baselines, reduces skill-induced regressions, and lowers total inference cost.
- **Key Innovation**: Moves skills from "fixed instructions" to "drafts requiring runtime alignment" — a pre-execution composition step that complements the wiki's skill-admission/gating line (VaG, SkillProx, BONSAI).

### Explicit, Not Longer: What Makes Epistemic Stance Survive Memory Compression
- **Authors**: Alex Kwon
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.06953](https://arxiv.org/abs/2608.06953)
- **Abstract**: Agent memory compression is built to drop qualifiers, so a claim's epistemic standing (belief vs doubt vs hearsay) tends not to survive being written to memory. In matched notes holding the identical claim and stance and differing only in *where* the stance sits, writing the stance as a **labelled field rather than a bracketed aside** raises retention by ~15 points across two models (permutation p=0.00005); a pre-registered replication on Haiku gives +15.6 points. Ablations show the mechanisms differ per model (labels help both; a full-sentence stance is the largest component on one model and worthless on the other) — so the paper claims only the intersection: make the stance explicit, not merely longer, and expect the best way of being explicit to be model-dependent. A deterministic readout reproduces the direction but not length/labels.
- **Key Innovation**: A tightly controlled, pre-registered result on memory engineering — *formatting* the epistemic stance (not length) determines whether it survives compression, with honest per-model mechanism reporting.

---

## 4. Sequential Modeling, Time Series & World Models

### KReF: Training-Free Retrieval for Long-Term Time-Series Forecasting and Predictive Uncertainty
- **Authors**: Yang Zhang, Rui Su
- **Institution**: —
- **Date**: 2026-08-07
- **Link**: [2608.06748](https://arxiv.org/abs/2608.06748)
- **Abstract**: Probabilistic LTSF relies on trained models; training-free conformal methods wrap a point forecaster and don't natively represent a full predictive distribution, and sequential variants suffer increasingly delayed feedback at long horizons. KReF treats **retrieved historical futures as a query-local empirical predictive distribution**: after robust preprocessing, each lookback is embedded with handcrafted statistics or frozen random Fourier features, similar lookback–future pairs are retrieved, and their similarity weights define predictive masses, quantiles, CRPS, and a weighted-mean point forecast; a probability-integral-transform map plus validation-selected expansion/shrinkage adapts interval boundaries. Across six LTSF benchmarks and four horizons, KReF gets the lowest CRPS in all 12 dataset-embedding settings (IS90 lowest in 9), and matches/surpasses trained baselines on two of six datasets for point forecasts. An archive-oracle analysis shows substantial headroom under finer routing.
- **Key Innovation**: The wiki's "alignment/retrieval beats learned fusion for time series" thread (Aug 8 Align-RAG/TS-RAG) now extends to *training-free full-distribution* forecasting — retrieval as a first-class inductive bias, not a helper.

### When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series (GLIDE)
- **Authors**: Chen Shao, Yue Wang, Zhenyi Zhu, Zhanbo Huang, Tobias Käfer, Zonghan Wu, Danai Koutra
- **Institution**: University of Michigan (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07333](https://arxiv.org/abs/2608.07333)
- **Abstract**: Graph-based multivariate forecasting assumes a static topology of pairwise temporal correlations, but correlations can evolve drastically. The paper proposes **Temporal Correlation Volatility (TCV)**, a model-agnostic metric quantifying the distributional evolution of these latent structures, and shows a clear TCV–degradation link: many models (including Transformers) generalize poorly in high-TCV settings and are often beaten by structure-agnostic baselines. GLIDE (Graph Layer for Inference in Dynamic Environments) adds two theoretically grounded mechanisms — **path-based message passing** (path-based neighborhoods) and **static/dynamic propagation separation** (local static approximation to identify optimal dynamics). GLIDE improves average performance by up to 45.6% across static and dynamic settings (largest gain 85.7%).
- **Key Innovation**: A metric (TCV) that turns "graph structure is stale" into a measurable quantity, plus a GNN layer that handles dynamic topology — a diagnostic-and-fix pair for the time-series cluster.

### Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction (DPWM)
- **Authors**: Xinyi Li, Zaishuo Xia, Chenjie Hao, Yubei Chen
- **Institution**: UC Davis (likely)
- **Date**: 2026-08-07
- **Link**: [2608.07420](https://arxiv.org/abs/2608.07420)
- **Abstract**: World models are trained with few-step local prediction objectives but deployed by recursive rollout — a mismatch: few-step losses optimize local transition fidelity while long-horizon accuracy depends on error/gradient propagation through the whole trajectory, so small local errors amplify. The Direct Prediction World Model (DPWM) compresses an action sequence of arbitrary length into a single embedding and predicts the endpoint observation in a single forward pass, avoiding recurrent rollout in both prediction and gradient propagation. DPWM substantially improves long-horizon endpoint prediction over recursive baselines on continuous-control and pixel benchmarks, with larger gains as the horizon grows — and crucially, **recurrent baselines improve equally when retrained with the same endpoint objective**, showing the training objective, not the backbone, is the main driver.
- **Key Innovation**: A clean claim for the world-model cluster: long-horizon accuracy is set by the *training objective* (endpoint, end-to-end), not the architecture — echoing the wiki's GAUGE/physical-fidelity thread with an honest objective-first ablation.

---

## 5. Recommendation, Advertising, Auctions & Games

### Auctioning Attention on Social Networks
- **Authors**: Andy Lee, Hari Sundaram
- **Institution**: UIUC (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06665](https://arxiv.org/abs/2608.06665)
- **Abstract**: Social media feed construction pits producers, consumers, platform operators, and social pressures against each other; recommendation-based feed design resolves this conflict implicitly. The paper instead proposes an **auction where users bid for the attention of other users**, systematically accounting for producers, consumers, platform, and social welfare, and proves the auction is **weakly incentive compatible under budget constraints**. A tax policy raises the cost of content with negative externalities (polarization, misinformation). Simulations over common topologies and an empirically observed network show the auction yields 36.3% higher producer welfare than comparison algorithms on the observed network (31.4% on synthetic) and more equitable attention distributions across all evaluated network types.
- **Key Innovation**: Feed construction as a *mechanism-design* problem rather than a ranking problem — with an IC-under-budget auction plus externality taxation — directly extending the wiki's advertising/auctions thread (LLM-OSDA, auto-bidding) to the social-feed setting.

### Progressive Content Refinement with Decaying Reward Joint LinUCB
- **Authors**: Shion Ishikawa, Pablo Loyola, Young-joo Chung, Yun Ching Liu
- **Institution**: IBM Research (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06750](https://arxiv.org/abs/2608.06750)
- **Abstract**: Iterative LLM refinement (e.g., Self-Refine) and bandit approaches often ignore the **saturation effect** — repeated use of identical prompts/arms yields diminishing rewards, causing over-exploitation. The paper proposes a contextual bandit with explicit **reward-decay modeling**: an EM algorithm jointly estimates arm-specific and decay parameters, and embedding prompts as arms enables joint learning of arm values (vs disjoint LinUCB). On Sentiment Reversal and GSM8K, the method significantly beats strong baselines, and ablations confirm reward-decay modeling is crucial for mitigating over-exploitation.
- **Key Innovation**: Brings reward decay into LLM-as-bandit refinement — over-exploitation (reusing the same prompt) is treated as a first-class failure mode, not a tuning detail.

### Fast LapSum: Exact Differentiable Top-k at Million Scale
- **Authors**: Łukasz Struski, Joanna Wojciechowicz, Jakub Antczak, Marcin Mazur, Kamil Książek, Jacek Tabor
- **Institution**: Jagiellonian University (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06912](https://arxiv.org/abs/2608.06912)
- **Abstract**: The top-k operation is fundamental to sparse computation (token routing, expert activation, memory selection, attention pruning) but hard top-k blocks gradients and existing soft relaxations are too costly. Fast LapSum is an **exact-budget soft top-k** primitive whose GPU solver runs in linear time after sorting — the first method preserving an exact selection mass of k while fully differentiable end-to-end (prior linear-time methods like DFTopK relax the normalization constraint). It combines a linear-time threshold computation with an analytical VJP; extreme scales use probabilistic bracketing to sort only the uncertain middle band. Overhead is negligible: 10^6/10^7/10^8 scores in 0.41/1.15/5.23 ms. Demonstrated on megapixel sparse adversarial examples (order-of-magnitude speedup) and a fully differentiable sparse image coder.
- **Key Innovation**: Makes *exact* soft top-k cheap enough for in-training-loop use at million-plus scale — an infrastructure primitive for routing/retrieval/attention workloads across the stack.

### Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference (DKG-MTI)
- **Authors**: Tzu-Cheng Peng, Chien Chin Chen, Chih-Hao Ku, Yung-Chun Chang
- **Institution**: National Taiwan University (likely)
- **Date**: 2026-08-07
- **Link**: [2608.06752](https://arxiv.org/abs/2608.06752)
- **Abstract**: Online travel-review intent inference typically uses hierarchical pipelines that suffer error propagation or retrieval methods ignoring structural domain knowledge. DKG-MTI is an inference-only knowledge augmentation framework that builds a **User-Specific Intent Knowledge Graph** per review and aligns it with a **Global Hotel Knowledge Graph** via structure-aware semantic smoothing; the aligned knowledge joins the review in an LLM that simultaneously predicts aspect ratings and generates reverse user-intent statements. On TripAdvisor reviews it consistently outperforms strong LLM and retrieval baselines on both classification and intent generation.
- **Key Innovation**: Structure-aware KG alignment (not just retrieval) as an inference-time augmentation for unified multi-task intent — relevant to the rec/personalization thread.

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Initialization/warm-up becomes the open frontier in OPD** | After Aug 7–8 established supervision-free and gradient-free OPSD, Simple-OPD shows warm-up transfers a teacher *thinking pattern* (even incorrect rollouts help) via teacher-CoT + LoRA — the "when/how to start" axis of self-distillation | Simple-OPD, FutureBridge (as warm-up-adjacent) |
| **KV cache compression turns into global budget allocation** | GraceKV frames compression as a global resource-allocation problem across resolution vs coverage (no fixed per-head rules, 128× robust); CubicQuant and MemGLU attack adjacent efficiency/architecture assumptions (non-uniform-but-executable quantization; closed-tail gating) | GraceKV, CubicQuant, MemGLU |
| **Step-level supervision densification is the field's response to long horizons** | The Horizon Gap survey finds outcome-only signals grow uninformative as horizons lengthen; crystallization (text-to-SQL) measures what reusable step-level memory is worth; FutureBridge and calibration-by-bilevel densify token/candidate-level signals | Horizon Gap, Crystallization, FutureBridge, Bilevel Calibration |
| **Mechanistic results keep landing with reproducibility caveats** | Post-Grokking Collapse shows Muon's faster grokking is unstable at the representation-readout interface (freeze embeddings to fix); Two-Hop Generalization localizes compositional failure to the lower/upper-layer boundary; Faster QK Learning explains attention sharpening via implicit LR rescaling | Post-Grokking Collapse, Two-Hop, Faster QK Learning |
| **Retrieval and alignment keep beating learned components in forecasting** | KReF achieves state-of-the-art probabilistic LTSF fully training-free via retrieved historical futures — extending Aug 8's Align-RAG "alignment-not-fusion" result; GLIDE adds a metric (TCV) for when graph structure fails; DPWM argues the world-model training objective matters more than backbone | KReF, GLIDE, DPWM |
| **Agent safety/eval moves to lifecycle and attribution** | HarnessSafe tracks persistent-carrier risk lifecycles (containment is carrier-specific); Long-Horizon Trajectory Attribution makes "why did the agent do that" measurable; LivePlan decouples cheap rule-based detection from LLM correction; SkillAligner treats skills as runtime-alignable drafts | HarnessSafe, Trajectory Attribution, LivePlan, SkillAligner |
| **Mechanism design returns for attention allocation** | Auctioning Attention on Social Networks reframes feed construction as an IC-under-budget auction with externality taxation (36.3% higher producer welfare); Joint-LinUCB adds reward decay to LLM bandit refinement — attention/refinement treated as market/optimization problems | Auctioning Attention, Joint-LinUCB |

---

## Key Takeaways

1. **The OPSD frontier moved to initialization.** Simple-OPD closes the loop on Aug 7/8's OPSD cluster by showing warm-up is a *thinking-pattern* transfer — teacher-compatible CoT (even incorrect rollouts) plus LoRA is the plug-and-play init — so the remaining open question is no longer supervision or gradients but *where the student starts*.
2. **Compression and efficiency are converging on "global budget, exact semantics".** GraceKV's global resolution-vs-coverage allocation, CubicQuant's non-uniform-but-GPU-native codebooks, and MemGLU's closed-tail-gating negative result all push the same thesis: fixed heuristics are being replaced by globally-optimized, exactly-specified trade-offs. MemGLU in particular is a healthy reminder that settled architecture choices (SwiGLU's tail) may be adaptable rather than necessary.
3. **Long-horizon reliability is being attacked with denser step-level signals — and now measured as reusable value.** The Horizon Gap survey names step-level signal densification as the field-wide response; Crystallization quantifies exactly how much *reusable* value verified repair episodes have (4.34 pp held-out, database-specific content is what matters, not fancier formats). The two papers together are a strong pair on the wiki's agent-reliability thread.
4. **Forecasting keeps learning the same lesson: retrieval and objectives, not fancy modules.** KReF (training-free retrieval beats trained forecasting), GLIDE (when graphs are stale, structure-agnostic baselines win — until you add path-based + separated-propagation layers), and DPWM (endpoint objective > backbone for world models) — three independent confirmations of the wiki's "simple/alignment-driven baselines" thread from Aug 8.
5. **Advertising/auction research shows up this time as mechanism design for attention.** Auctioning Attention on Social Networks is the batch's closest match to the advertising theme (user-bid auctions, externality taxation, IC under budgets) — a cleaner theoretical counterpart to today's paper-check industrial CTR papers (TM20K, HD-Rec). No pure CTR paper surfaced in the cs.CL/cs.LG remainder.
6. **Games were fully claimed by today's game-rl-daily** (13 papers: MDT solver-guided equilibria, Aftab, MemWM, WorldTrace, TRIAL, MARP, PHASE-Tree…); this digest's only GT addition is the auction/fair-division work and the Ex-Post Equilibria theory paper [2608.07025] (noted, not deep-curated).

> ⚠️ Note on sourcing: today's digest curates the **Mon Aug 10, 2026 arXiv batch** (papers submitted Aug 7–9, IDs ~2608.06394–2608.07457), verified via the arXiv API (`submittedDate` window) and individual abs pages. All 25 papers are **grep-verified absent from the entire wiki** — zero overlap with today's [paper check](../2026-08-10/arxiv-paper-check.md) (cs.AI/cs.IR flagship cluster), [game-rl-daily](../2026-08-10/game-rl-daily.md), [conference-digest](../2026-08-10/conference-digest.md), or the Aug 7/8 digests. Institution attributions marked "(likely)" are inferred from author affiliations, not the arXiv record; "—" means not identified.
