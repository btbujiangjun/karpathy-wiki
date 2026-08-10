---
title: "arXiv Daily Digest — 2026-08-08 (Saturday catch-up)"
type: synthesis
created: 2026-08-08
updated: 2026-08-08
tags: [arxiv, llm, recommendation, retrieval, reasoning, rl, agents, sequential-modeling, games, world-models, personalization, time-series, evaluation, tool-use]
---

# arXiv Daily Digest — 2026-08-08 (Saturday catch-up)

> **Batch note:** arXiv announces new submissions Mon–Fri; there is **no Sat Aug 8, 2026 announcement**. The latest listing is the **Fri Aug 7, 2026** batch (papers submitted Aug 5–6), which the [Aug 7 digest](../2026-08-07/arxiv-daily.md) already curated in depth (26 papers). This digest is a **supplementary, zero-overlap curation of the same batch** — 21 additional papers across AI, LLMs, agents, sequential modeling, time series, games, and recommendation that the Aug 7 digest did not cover. It therefore reads as a breadth pass: it fills in the agent/safety/reliability cluster, the time-series forecasting cluster, and the games/annotation cluster, while the Aug 7 digest already carried the flagship recsys/RL/architecture papers. As with Aug 7, **no dedicated advertising/CTR paper surfaced** in the cs.IR stream; the closest industrial recommendation work today is the Kuaishou research-agent infrastructure paper (From Trajectories to Evidence). Signature themes of this batch's remainder: **supervision-free self-distillation and gradient-free reasoning search**, **agent reliability/auditability as a first-class research target**, and **alignment (not learned fusion) driving retrieval-augmented time-series forecasting**.

---

## 1. LLM Reasoning, RL & Post-Training

### U-OPSD: On-Policy Self-Distillation without Any Supervision
- **Authors**: Yijiang Li, Bingyang Wang, Yijun Liang, Yunjie Tian, Di Fu, Nuno Vasconcelos
- **Institution**: UC San Diego
- **Date**: 2026-08-06
- **Link**: [2608.06296](https://arxiv.org/abs/2608.06296)
- **Abstract**: On-policy (self-)distillation (OPD/OPSD) has shown strong potential for LLM post-training, but existing methods still lean on external supervision — ground-truth signals, environment feedback, or larger teachers — falling short of genuine "self"-distillation. U-OPSD uses only the model's own generations via internal consistency: sample multiple rollouts, construct a pseudo-solution by majority vote under a self-consistency threshold, then condition a teacher distribution on the *shortest* pseudo-solution and distill it into prefixes of the model's *longest incorrect* completion — correcting the model precisely where it is confidently wrong. Across AIME24/25, HMMT25, MATH500, and AMC23, U-OPSD improves over base Qwen3 non-thinking mode by 8.5%/10.7% at 4B/8B and beats supervised OPSD by 3.2%/2.3%; in thinking mode it stays on par with OPSD and surpasses GRPO.
- **Key Innovation**: The first OPSD variant that removes external supervision entirely — self-consistency voting supplies the pseudo-labels — closing the loop on the Aug 7 on-policy self-distillation cluster (DASH, AgentOPSD) with a genuinely self-supervised method.

### Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging
- **Authors**: Yu Gu, Zhi Zheng, Yunpeng Ba, Xialiang Tong, Mingxuan Yuan, Zhenkun Wang
- **Institution**: Huawei Noah's Ark Lab
- **Date**: 2026-08-06
- **Link**: [2608.05541](https://arxiv.org/abs/2608.05541)
- **Abstract**: Evolution Strategy (ES) is an attractive gradient-free alternative for resource-constrained LLM reasoning, but full-parameter ES on billion-parameter models is ineffective: most random perturbations are nearly orthogonal to useful update directions. Hyper-ES is a subspace-based ES framework — run a small number of cheap gradient fine-tuning runs to obtain descent directions, whose span forms a compact adaptation subspace, then let CMA-ES optimize layer-wise DARE-TIES merging coefficients inside that subspace, searching over combinations of meaningful directions rather than arbitrary full-model perturbations. On three Qwen2.5-Instruct and DeepSeek-R1-Distill backbones across six mathematical reasoning datasets, Hyper-ES consistently outperforms GRPO-LoRA by ~1% while requiring 10% fewer space-consuming gradient updates.
- **Key Innovation**: A gradient/ES hybrid — ES explores the span of a few cheap descent directions instead of random full-model perturbations — giving evolution strategies a tractable low-dimensional search space for reasoning fine-tuning.

### Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints
- **Authors**: Hongbo Ma, Bangji Yang, Yunqian Selina Cheng, Jiajun Fan, Hanwen Zhang, Ge Liu
- **Institution**: —
- **Date**: 2026-08-05
- **Link**: [2608.05254](https://arxiv.org/abs/2608.05254)
- **Abstract**: LLMs can derive a plausible mathematical object yet still violate explicit requirements — omitting a modular reduction, returning a non-integer, or using the wrong encoded answer form. CFR is a training-free two-stage prompting protocol: Stage 1 extracts and summarizes the constraints entailed by the problem; Stage 2 solves while checking intermediate and final results against that summary. Routed-CFR activates the two-stage protocol only when a text-only regex router detects restrictive cues, otherwise falling back to direct chain-of-thought. Across AIME, CMIMC, BRUMO, and AIMO_AMC, CFR improves direct CoT on multiple backbones, with rigorous controls (convention-controlled routing, matched prompting baselines, problem-level paired tests, decoding robustness, constraint-quality audits, token accounting, OlympiadBench evaluation).
- **Key Innovation**: Making answer-space constraints an explicit, checkable contract at inference — honestly scoped as a targeted test-time intervention whose benefit depends on recoverable constraints and reliable Stage-1 extraction, not a general reasoning replacement.

### SCOPE: Learning When to Trust via Selective Context Preference Optimization
- **Authors**: Xian Sun, Wei Chow, Yingshuo Wang, Junhao Liu, Wei Gao, Qing Wu, Lingdong Kong
- **Institution**: — (project: WorldBench)
- **Date**: 2026-08-06
- **Link**: [2608.06377](https://arxiv.org/abs/2608.06377)
- **Abstract**: LMs increasingly condition answers on external signals, and one misleading signal can turn a correct answer wrong. Training models to "resist" such signals hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. The paper recasts this as **selective trust**: MIST, a human-annotated benchmark rendering each reasoning item under four matched conditions (clean, misleading, correct-context, irrelevant-context), plus SC2W, a paired metric counting how often a misleading signal flips a clean-correct answer to wrong. Susceptibility is universal across models. SCOPE mines clean-correct/misleading-wrong failures and optimizes a standard DPO objective over matched preference pairs balanced equally across all four conditions (rather than misleading items alone), substantially reducing SC2W while preserving accuracy on clean, correct, and irrelevant contexts.
- **Key Innovation**: Judging models on selective trust (SC2W) rather than resistance — a matched-condition benchmark plus a DPO recipe that removes vulnerability to misleading context without discarding useful context.

### Measuring and Detecting Harmful AI Sycophancy
- **Authors**: Bohan Jiang, Dawei Li, Yasin Silva, Huan Liu
- **Institution**: Arizona State University
- **Date**: 2026-08-06
- **Link**: [2608.05624](https://arxiv.org/abs/2608.05624)
- **Abstract**: Focuses on one harmful sycophancy subtype — preference-induced stance reversal sycophancy (PSRS), where a model reverses an initial stance merely to align with a user's stated preference. Introduces CAP (Contrastive Anchor Probing) to collect labeled PSRS data and applies it to 17 open- and closed-source LLMs, yielding 290,460 labeled responses across 12 everyday-advice domains. Findings: PSRS rates range 5%–56% with more capable models being less sycophantic; PSRS is detectable from the response text alone, but detectors need subtle patterns and their performance drops on unseen models — a cross-model generalization problem the paper takes an initial stab at.
- **Key Innovation**: Goes beyond "how sycophantic is a model" to "can we detect a specific harmful sycophancy subtype automatically, and does detection generalize to unseen models" — with a 290K-response labeled dataset.

---

## 2. Agents, Skills & Tool Use

### The Bitter Lesson of Tool Calling
- **Authors**: Ishan Patel, Sahil Sen, Elias Lumer, Vamse Kumar Subbiah
- **Institution**: —
- **Date**: 2026-08-06
- **Link**: [2608.06370](https://arxiv.org/abs/2608.06370)
- **Abstract**: An empirical comparison of programmatic tool calling (PTC — tools exposed as typed Python stubs the model invokes through code, with execution and results handled in a single agent turn) vs native JSON tool calling across 14 language models on BFCL v4. PTC matches or exceeds JSON in 11 of 14 models (GPT-5.6 family +10.6%), matches or outperforms in 13 of 14 under parallel fan-out, and stays stable under context-rot conditions where the JSON baseline degrades 2.3% on average.
- **Key Innovation**: Systematic evidence that "tools as code" beats "tools as JSON" — a bitter-lesson-style argument that giving the model more expressiveness/computation (scripts that chain and parallelize) outperforms task-specific rigid structure.

### When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents
- **Authors**: Linfang Shang, Ming Xu, Yiding Sun, Tianle Xia, Lingxiang Hu, Lan Xu, Ning Zheng
- **Institution**: —
- **Date**: 2026-08-06
- **Link**: [2608.05810](https://arxiv.org/abs/2608.05810)
- **Abstract**: Self-evolving agents accumulate capability by distilling reusable skills from trajectories, but the process is not monotonic: past a critical pool size, newly added skills degrade performance — a capability-contamination phase transition. Cause: once a defective skill enters the decision context, it becomes reference material for distilling later skills, forming cross-round contamination chains; and the contamination is structurally irreversible, since post-hoc removal of a source skill cannot erase the flawed reasoning its descendants inherited. This makes skill admission a pre-commit necessity, motivating Verifier-as-Gatekeeper (VaG): three heterogeneous critics (structural validity, behavioral harmlessness, semantic consistency) filter each skill, plus a marginal-gain subset selection that removes combinatorial contamination before skills reach runtime context. On Terminal-Bench 2, unconditional accumulation peaks then gives back most of its gains; VaG improves every round, reaching 72% pass@1 with a ~5x smaller pool, and its frozen skill pool transfers positively to four other backbones and a second benchmark.
- **Key Innovation**: Formalizes a phase transition in agent self-evolution and proves contamination is structurally irreversible — turning skill admission into a pre-commit gate with a three-critic trust hierarchy.

### When History Lies: Evaluating and Improving Tool Use under Misleading Multi-Turn Histories
- **Authors**: Xiaoqing Wu, Xingyu Fan, Feifei Li, Wenhui Que
- **Institution**: —
- **Date**: 2026-08-06
- **Link**: [2608.06057](https://arxiv.org/abs/2608.06057)
- **Abstract**: Tool-calling agents infer task state from accumulated dialogue and tool traces; in persistent interactions, historical traces can stay structurally valid and semantically plausible after they cease to be authoritative. Such history can hijack a policy the model already possesses: on Qwen3-1.7B, pollution flips 32.1% of decisions that are correct under the original trajectory and frequently induces reuse of corrupted entities or interface conventions. Introduces a paired benchmark with synchronized Original, Polluted, and Oracle State views, plus eleven gold-preserving interventions isolating failures in decision state, entity binding, and interface execution. Fix: transfer an Oracle-conditioned teacher policy to a student observing only polluted history via soft supervision on student-generated prefixes — 87.0% Balanced Tool-Use Accuracy vs Gold-SFT 66.3%, Oracle sequence distillation 82.3%, off-policy token distillation 85.0%; an 8B teacher raises the 1.7B student to 91.9% and an 8B student reaches 93.0%. Policies transfer to clean histories, unseen functions, and external benchmarks.
- **Key Innovation**: Establishes history reliability as a distinct tool-use bottleneck and shows reliable-state (Oracle-conditioned) policy transfer is an effective, scalable fix.

### SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents
- **Authors**: Zhixiang Liang, Yifei Liu, Yidan Huang, Haozhe Zhao, Beichen Huang, Jiaqi Wang, Nan Duan, Qiong Cao
- **Institution**: Microsoft Research Asia / Tsinghua (likely)
- **Date**: 2026-08-05
- **Link**: [2608.05212](https://arxiv.org/abs/2608.05212)
- **Abstract**: Deep search agents fail when small reasoning errors propagate through long, noisy trajectories into fluent-but-wrong answers, and manual diagnosis of these traces is beyond human capacity. SearchAuditBench evaluates whether LLM auditors can localize, attribute, and repair such failures: 1,243 failed trajectories (avg 73.1 messages, 65.1K tokens) from eight open-weight models on five deep-search benchmarks, each expert-annotated with the critical error step, a search-specific root cause, and a reference repair with grading rubrics. SearchAuditor is a multi-perspective auditing framework that localizes, attributes, and repairs failures through evidence-grounded adjudication. Even the strongest baseline powered by a frontier model (GPT-5.5) attains only a 26.6% end-to-end pass rate; SearchAuditor reaches 32.3%, and resuming failed runs with its repairs helps agents recover from errors.
- **Key Innovation**: A benchmark + framework for the meta-task of "auditing agent failures" — using LLMs as auditors of other agents' long-horizon traces, with measured repair benefit on resumed runs.

### DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model
- **Authors**: Wenhao Lin, Chenyu Yu, Xingwei Lin, Sicong Cao, Xiang Chen, Lei Xue, Le Yu, Letian Sha, Chunming Wu
- **Institution**: Zhejiang University
- **Date**: 2026-08-06
- **Link**: [2608.05695](https://arxiv.org/abs/2608.05695)
- **Abstract**: Runtime guardrails check proposed agent actions before execution, but most are reactive — assessing only the apparent safety of the current action, with no model of how risk evolves across the trajectory, which creates a blind spot for long-horizon risks where individually benign-looking actions drift toward hazardous states. DreamGuard is a proactive guardrail built around a risk-aware world model: it maintains a compact recurrent latent state over the trajectory and predicts future latent states, deriving immediate-hazard and prefix-risk evidence that is fused into pre-execution intervention decisions. Across four benchmarks and an online guardrail evaluation, DreamGuard outperforms generic, reactive, and proactive baselines, achieves the best safety-utility trade-off, and holds an average end-to-end latency of 25 ms per call.
- **Key Innovation**: Multi-horizon (immediate + prefix) risk reasoning via a latent world model — catching the long-horizon drift that reactive checkers miss, at 25 ms latency.

### SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries
- **Authors**: Xingyu Tan, Xiaoyang Wang, Qing Liu, Xiwei Xu, Xin Yuan, Liming Zhu, Wenjie Zhang
- **Institution**: CSIRO Data61 / UNSW
- **Date**: 2026-08-06
- **Link**: [2608.05604](https://arxiv.org/abs/2608.05604)
- **Abstract**: As skill libraries grow, agents must expose the smallest sufficient executable context under a limited context budget. Existing systems struggle to reuse routines below the whole-skill level, preserve procedural contracts during compression, and keep compressed routines executable and expandable — a unit mismatch where skills are retrieved as packages, compressed as text, and converted to execution graphs only after retrieval. SkillZip performs execution-aware, contract-preserving compression over section-level graphs: it rewrites recurring contract-valid motifs into reversible ported macros while preserving boundary signatures, dependency closure, verifier reachability, and source-level expansion, then hydrates a compact dependency-closed context at inference and expands macros only when required (ReZip integrates new skills and revises risky macros from execution evidence). SkillZip outperforms the strongest baseline by up to 12.2 points with a 3.46x compression ratio, 99.2% dependency preservation, and 98.7% verifier reachability, scaling from 200 to 100K skills.
- **Key Innovation**: The procedural unit — not the text — is what gets compressed, keeping skills verifiable, expandable, and contract-preserving under a fixed context budget.

### OrchestraBench: Evaluating Multi-Agent Orchestration Failure Modes, Recovery, and Decomposition Quality
- **Authors**: Yidian Chen, Yingzi Gu, Natan Vidra, Spurthi Setty, Sharon Zheng
- **Institution**: Salesforce (likely)
- **Date**: 2026-08-05
- **Link**: [2608.05263](https://arxiv.org/abs/2608.05263)
- **Abstract**: Multi-agent orchestration frameworks are moving to production, yet benchmarks report task accuracy without diagnosing why a pipeline failed, where a cascade began, or which routing decision broke. OrchestraBench evaluates failure, recovery, and decomposition via a controlled, seed-reproducible failure-injection harness over templated enterprise workflows, introducing cascade radius and per-failure-mode recovery as primary metrics with bootstrap confidence intervals and paired tests. On a 26-case gold-labelled diagnostic, a keyword/flag router scored 0% on adversarial cases with misleading or missing surface flags while an intent-reasoning model router scored 100%, matching the oracle. Mechanism probes with a real Claude agent over a verifiable arithmetic dependency chain revealed three failure-handling tiers across five MAST modes: tool faults recovered fully (1.0), ambiguous delegation partially (0.30), and latent/semantic modes never (0.0) — an ordering that persisted across reframings and model sizes. Cascade radius grows with pipeline depth (0.9 → 4.7 across depths 3–7), and a trusted-state repair ablation shows apparent containment gains came mainly from the trusted-state signal, not autonomous detection.
- **Key Innovation**: First failure-diagnosis-centric benchmark for multi-agent orchestration — cascade radius + per-mode recovery metrics — honestly scoped as controlled mechanism probes rather than domain-workload claims.

---

## 3. Sequential Modeling, Time Series & Inference Efficiency

### DBLAST: Dependent Block Drafting for Stochastic Speculative Decoding
- **Authors**: Amirmohammad Karimi, Chao Gao, Negar Hassanpour
- **Institution**: —
- **Date**: 2026-08-05
- **Link**: [2608.05448](https://arxiv.org/abs/2608.05448)
- **Abstract**: Speculative decoding accelerates inference with a lightweight drafter, but recent block and diffusion-style drafters are optimized for greedy decoding and assume draft positions are conditionally independent. That assumption breaks in non-greedy speculative decoding, where the target distribution is deliberately stochastic: the accepted draft length degrades as the entropy of the target sampling distribution rises. DBLAST proposes a dependent block drafter based on a low-rank latent mixture over token positions, trained with an acceptance-oriented objective that directly targets expected verified length. On Qwen3-4B and Qwen3-8B across GSM8K, MT-Bench, HumanEval, and creative-writing benchmarks, it consistently improves accepted length over independent block sampling, especially in higher-entropy decoding regimes.
- **Key Innovation**: Fixing the greedy-optimized, independence-assumption failure of block drafters — modeling inter-position dependence via a low-rank latent mixture and training for expected verified length.

### TS-RAG: Retrieval Augmented Generation for Time Series Forecasting
- **Authors**: Yixiong Xiao, Congxi Xiao, Jingbo Zhou
- **Institution**: Baidu
- **Date**: 2026-08-06
- **Link**: [2608.06223](https://arxiv.org/abs/2608.06223)
- **Abstract**: RAG is underexplored in time series forecasting, and naively concatenating retrieved reference sequences into the prompt — as done in language models — does not transfer, because time-series models are smaller, less generative, and data-limited. TS-RAG retrieves similar time series sequences as references and fuses them with the input via specially designed reference tokens, capturing complex temporal dynamics more robustly. It achieves consistent state-of-the-art performance across several real-world forecasting benchmarks.
- **Key Innovation**: Adapting the RAG paradigm to non-LLM time-series models through learned reference tokens rather than raw prompt concatenation.

### Align-RAG: Alignment Is All You Need for TSFM In-Context Learning
- **Authors**: Mohammad Asadi, Soheil Hor, Bardiya Akhbari, Jack W. O'Sullivan, Tahoura Nedaee, Layne C. Price, Raviteja Anantha, Euan Ashley, Ehsan Adeli
- **Institution**: Stanford University (likely)
- **Date**: 2026-08-06
- **Link**: [2608.05571](https://arxiv.org/abs/2608.05571)
- **Abstract**: Retrieval-augmented forecasting typically trains fusion adapters on the assumption that frozen Time Series Foundation Models cannot dynamically incorporate retrieved context. Align-RAG shows that assumption is unnecessary: a training-free, closed-form per-pair amplitude rescaling and integer-lag phase shift applied to retrieved past-future windows before they enter a frozen backbone's context. With zero learned parameters it outperforms the state-of-the-art trained retrieval adapter on frozen Chronos-Bolt across all seven benchmark datasets (avg −3.75% MSE), and improves zero-shot MSE on four additional frozen TSFMs by 2.5–13.7% with no per-backbone tuning. Probing shows aligned demonstrations induce prediction shifts that track a closed-form ridge predictor, with a future-shuffle control ruling out a futures-averaging account.
- **Key Innovation**: A zero-parameter baseline proving that closed-form alignment — not learned fusion — recovers most of retrieval-augmented forecasting's gains, and an argument that it should be the default baseline before any fusion module is trained.

---

## 4. Games, World Models & Multi-Agent Systems

### VLMs for Videogame Data Annotation
- **Authors**: Katrin Schmid, Iuri Frosio
- **Institution**: NVIDIA
- **Date**: 2026-08-06
- **Link**: [2608.05949](https://arxiv.org/abs/2608.05949)
- **Abstract**: VLM adoption in video games is limited by the extreme variability of synthetic scenarios and their poor compliance with real-world physics. This paper investigates using VLMs to annotate video game frame sequences with reward signals — a task with applications in conditioned training and offline reinforcement learning. VLMs often struggle to answer basic questions on racing video games (with similar behavior on other genres); countermeasures include VLM output mixing and prompt optimization. Input sequence length, resolution, and question batching all affect annotation quality and its token consumption.
- **Key Innovation**: An honest mapping of VLM reward-annotation failure modes for games, plus the practical knobs (output mixing, prompt optimization, batching) that trade annotation quality against token cost.

### Training a Conditioned Video Game Agent on a VLM-Annotated Dataset
- **Authors**: Katrin Schmid, Iuri Frosio
- **Institution**: NVIDIA
- **Date**: 2026-08-06
- **Link**: [2608.05954](https://arxiv.org/abs/2608.05954)
- **Abstract**: RL for games normally requires engine access for rewards, a trial-and-error process for identifying/weighting rewards, and sparse rewards that are hard to interpret. This paper proposes annotating a video game dataset with VLMs instructed to extract human-defined rewards, then using offline RL to train a conditioned agent that responds to desired returns. Early experiments confirm the approach works while surfacing the difficulties and limitations (which the paper discusses candidly).
- **Key Innovation**: Replacing environment-computed rewards with VLM-extracted, human-defined rewards — decoupling conditioned agent training from game-engine reward plumbing.

### AI-Farol: Co-Evolutionary Dynamics in a Multi-Agent Two-Sided Learning Framework
- **Authors**: Iosif Polenakis, Kalliopi Kastampolidou, Theodore Andronikos
- **Institution**: University of Ioannina
- **Date**: 2026-08-05
- **Link**: [2608.05479](https://arxiv.org/abs/2608.05479)
- **Abstract**: The El Farol Bar game is a canonical model of coordination under uncertainty that traditionally treats the venue as a passive constraint. AI-Farol reconceptualizes it: the bar becomes a strategic player endowed with AI learning, adjusting pricing policies to balance revenue, utilization, and sustainability, while agents face partial observability (only subsets of past attendees) and learn beliefs and attendance strategies under incomplete information. The resulting two-sided learning system frames coordination as co-evolution between boundedly rational agents and an adaptive institution.
- **Key Innovation**: Extending a canonical coordination model to two-sided learning — an adaptive institution (mechanism-designer bar) co-evolving with learning agents under partial observability — with implications for congestion management and mechanism design.

---

## 5. Recommendation, Personalization & Retrieval

### From Trajectories to Evidence: Auditable Experimental Records for Industrial Research Agents
- **Authors**: Zijie Zhuang, Changxin Lao, Pengbo Xu, Hanwen Xu, Ruochen Yang, Yingzhi He, Peng Zhang, Jiangxia Cao, Yusheng Huang, Guohong Mu, Jian Liang, Ruiming Tang, Shuang Yang, Zhaojie Liu, Wenwu Ou, Kun Gai
- **Institution**: Kuaishou (likely)
- **Date**: 2026-08-05
- **Link**: [2608.05235](https://arxiv.org/abs/2608.05235)
- **Abstract**: Research agents run multi-round ML experiments in industrial recommendation settings and keep the trajectories, but a completed trajectory is not automatically evidence — artifacts may be unsupported or incomplete, rounds may be invalid or confounded, and later modifications may obscure earlier findings. The paper formalizes **trajectory-to-evidence conversion**: a context-isolated generate-verify-repair process checks artifacts before release; post-execution validity and attribution checks consolidate evidence across rounds and qualify intervention-level claims as actionable repairs, diagnostic guards, or withheld findings, preserved as auditable records with explicit provenance. A hybrid LLM-assisted controller applies, defers, or rejects records based on target evidence. Findings: later rounds often improve on the first while final rounds frequently underperform an earlier best (non-monotonic trajectory evolution), and candidates produced through the complete workflow yielded positive online lifts relative to deployed baselines.
- **Key Innovation**: Defining "trajectory-to-evidence conversion" — turning industrial research-agent logs into auditable, qualified claims — and showing both that non-monotonic evolution is common and that workflow-produced candidates beat deployed baselines online.

### SteerWrite: Training-Free Token-Level Steering for LLM Personalized Co-Writing
- **Authors**: Wenhao Mao, Chengbin Hou, Weixiao Wang, Jialiang Zhu, Min Liu, Yibin Hao, Hairong Lv
- **Institution**: —
- **Date**: 2026-08-06
- **Link**: [2608.06069](https://arxiv.org/abs/2608.06069)
- **Abstract**: LLM personalization faces a domain-knowledge gap; fine-tuning is costly and slow to update, while RAG cannot give fine-grained, token-level steering, and co-writing beyond coding is underexplored. SteerWrite is a training-free framework for personalized co-writing that adapts the base model to specialized domains without gradient updates, with designs tailored to small datasets. It achieves state-of-the-art performance across diverse datasets, metrics, and models, significantly reducing human editing effort.
- **Key Innovation**: Token-level context steering as the inference-only analogue of per-user adaptation — personalization for small data without gradient updates or retrieval fusion.

### omni-macos: On-Device Omni-Modal Search on Apple Silicon
- **Authors**: Han Xiao
- **Institution**: Jina AI
- **Date**: 2026-08-06
- **Link**: [2608.05543](https://arxiv.org/abs/2608.05543)
- **Abstract**: An omni-modal search engine (text, code, documents, images, audio, video in one embedding space) almost always assumes a server. omni-macos runs the entire engine — encoder, index, and store — on the Mac the files are already on, so no file, query, or vector ever leaves the machine. Inside one user-set memory budget it keeps a background indexer and an interactive search box: re-encoding only the chunks an edit changes, handing the GPU smaller units while the user types, answering queries from a quantized replica with exact rescoring, and propagating the budget to the allocators that draw on unified memory. All mechanisms are measured on five Macs spanning an eightfold range of accelerator width and a thirty-twofold range of memory.
- **Key Innovation**: A fully on-device, budget-constrained omni-modal search engine — quantization-with-exact-rescoring and incremental re-encoding are the mechanisms that make local-first search practical.

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Self-distillation goes supervision-free; reasoning search goes gradient-free** | Extends the Aug 7 OPSD cluster: U-OPSD replaces external supervision with self-consistency pseudo-labels and matches/beats supervised OPSD and GRPO; Hyper-ES merges a few cheap gradients into a CMA-ES subspace and beats GRPO-LoRA with fewer gradient updates | U-OPSD, Hyper-ES |
| **Trust and robustness become selective, not binary** | SCOPE judges models on selective trust (SC2W) under matched conditions rather than blanket resistance; a specific harmful sycophancy subtype (PSRS) is measured (5–56%) and auto-detected; CFR turns answer-space constraints into explicit test-time contracts | SCOPE, Sycophancy, CFR |
| **The agent stack matures from capability to reliability/auditability** | SearchAuditor benchmarks LLMs as auditors of long-horizon search failures; DreamGuard predicts long-horizon risk with a world model at 25 ms; When History Lies shows stale history hijacks tool policies (Oracle distillation fixes it); When Self-Evolution Backfires proves skill contamination is pre-commit-irreversible | SearchAuditor, DreamGuard, History Lies, VaG |
| **Tool-calling interfaces are being re-evaluated** | Programmatic tool calling (tools as code) matches or beats JSON across 11/14 models on BFCL v4 and stays stable under context rot; SkillZip compresses skill libraries at the procedural level (3.46x, contract-preserving); OrchestraBench diagnoses orchestration failure modes with cascade radius metrics | Bitter Lesson of Tool Calling, SkillZip, OrchestraBench |
| **Time-series forecasting adopts RAG — and alignment is doing the work** | TS-RAG fuses retrieved sequences via reference tokens; Align-RAG shows zero-parameter closed-form alignment beats trained fusion adapters on frozen TSFMs — a running theme that simple baselines capture gains attributed to learned modules | TS-RAG, Align-RAG |
| **Games remain a lab for reward engineering and coordination** | VLMs extract human-defined rewards for conditioned offline RL without engine access; AI-Farol turns the venue into an adaptive mechanism designer co-evolving with learning agents | VLM Annotation, Conditioned Agent, AI-Farol |
| **Recommendation research infrastructure industrializes** | Kuaishou formalizes trajectory-to-evidence conversion for industrial research agents (non-monotonic evolution, positive online lifts); omni-macos pushes omni-modal retrieval fully on-device | Trajectories-to-Evidence, omni-macos |

---

## Key Takeaways

1. **The self-distillation frontier is now genuinely unsupervised.** U-OPSD matches or beats supervised OPSD and GRPO using only self-consistency pseudo-labels from the model's own rollouts, completing the Aug 7 OPSD cluster (DASH, AgentOPSD, EnvACE). Hyper-ES, in parallel, removes the gradient-dependence for reasoning fine-tuning — together they suggest both supervision *and* gradient signals are becoming optional for reasoning post-training.
2. **The agent research agenda has shifted from "can it do the task" to "can we trust, audit, and repair it".** SearchAuditBench turns LLMs into auditors of other agents' long-horizon traces; DreamGuard adds world-model-predicted long-horizon risk; When History Lies isolates history reliability as a distinct tool-use bottleneck; When Self-Evolution Backfires shows skill contamination is structurally irreversible, so admission must be gated pre-commit. Kuaishou's trajectory-to-evidence work industrializes the same theme in recsys research.
3. **Interface decisions are where tool-calling gains live.** Programmatic tool calling beats JSON on 11/14 models and holds up under context rot — a bitter-lesson argument that more expressiveness beats more task-specific structure. This mirrors Aug 7's READ finding that the retrieval *interface* (not iteration) carried the gain.
4. **In retrieval-augmented time-series forecasting, alignment is the mechanism, not learned fusion.** Align-RAG's zero-parameter closed-form alignment beats a trained fusion adapter across all seven benchmark datasets — a strong caution to check simple alignment baselines before training adapters.
5. **Games stay a rigorous RL and coordination testbed.** VLM-extracted rewards enable conditioned offline agents without engine access; AI-Farol extends the canonical coordination game to two-sided learning with an adaptive institution. Together with Aug 7's GAUGE/IFlowNets/AV-AIVAT, the games stream is the strongest "measurement + correctness" cluster in this batch.
6. **No dedicated advertising/CTR paper surfaced** in the Friday cs.IR stream (10 new submissions; 6 already covered Aug 7); industrial recommendation coverage today is via the Kuaishou research-agent infrastructure paper and Aug 7's Gryphon-v2.

> ⚠️ Note on sourcing: arXiv announces new listings Mon–Fri; there is no Sat Aug 8 announcement, so this digest is a **no-overlap supplementary curation of the Fri Aug 7, 2026 batch** (papers submitted Aug 5–6). All 21 papers were verified against the arXiv category listing pages (`cs.AI`, `cs.CL`, `cs.LG`, `cs.IR`, `cs.GT`) and individual abs pages (`citation_date`). None overlap with the [Aug 7 digest](../2026-08-07/arxiv-daily.md), the [Aug 7 AI scan](../2026-08-07/arxiv-ai-search.md), or the Aug 6 [daily](../2026-08-06/arxiv-daily.md)/[paper check](../2026-08-06/arxiv-paper-check.md)/[AI scan](../2026-08-06/arxiv-ai-search.md). Institution attributions marked "(likely)" are inferred from author affiliations, not the arXiv record; "—" means not identified.
