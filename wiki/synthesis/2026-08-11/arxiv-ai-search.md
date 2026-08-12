---
title: arXiv AI Research Search — August 11, 2026
type: synthesis
created: 2026-08-11
updated: 2026-08-11
sources: [arxiv-listing, arxiv-abstract-pages]
tags: [arxiv, ai, llm, coding-agents, multi-agent, agent-security, distillation, rlvr, kv-cache, graph-neural-network, game-theory, mechanism-design, cad, daily-digest]
---

# arXiv AI Research Search — 2026-08-11

> Search window: fresh **Aug 9–10, 2026** arXiv submissions (IDs ~2608.08131–2608.09930), retrieved via the arXiv API **ahead of the Tue Aug 11 announcement** (~20:00 ET), plus recall fill-in of absent Aug 6–8 submissions (IDs ~2608.05791–2608.08130). Streams scanned: cs.SE (60), cs.MA (50), cs.GT (50), cs.CR (excess from cs.LG/cs.CL), and the cs.LG/cs.CL/cs.GT remainder not claimed by the same-day [arXiv Daily Digest](./arxiv-daily.md). Metadata verified against individual abstract pages.
>
> **21 papers curated, all NEW** (grep-verified 0 hits on arXiv ID across wiki/index.md, wiki/log.md, and wiki/synthesis/**). **Zero overlap** with the same-day [arXiv Paper Check](../2026-08-11/arxiv-paper-check.md) (18 papers, cs.AI+cs.IR deep scan), [arXiv Daily Digest](../2026-08-11/arxiv-daily.md) (31 papers, cs.LG/cs.CL/cs.GT/econ.TH breadth), [Game RL Daily](../2026-08-11/game-rl-daily.md) (19 papers), or [Conference Digest](../2026-08-11/conference-digest.md). Papers already covered elsewhere (Ouroboros 2608.08311 — 08-12 paper-check; MARP 2608.07280 — 08-10 game-rl-daily; extensive-form switching regret 2608.09501 — 08-12 game-rl-daily) are excluded and cross-referenced below.

## Overview table

| # | Paper | Domain | Institution / Company | arXiv | Status |
|---|-------|--------|----------------------|-------|--------|
| 1 | SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring | Coding agents / benchmark | HKUST / Shanghai Jiao Tong University | 2608.09802 | **new** |
| 2 | SpecPath: Testing Coding Agents Across Contract-Equivalent Specification Histories | Coding agents / eval | USTC / HKUST (high confidence) | 2608.09799 | **new** |
| 3 | OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review | Code review agents | (not stated; Nanjing University, tentative) | 2608.09290 | **new** |
| 4 | AgentChaos: Chaos Engineering for Agent Systems via Programmatic Fault Injection | Agent robustness | Singapore Management University / NUS (high confidence for David Lo) | 2608.06790 | **new** |
| 5 | GALA+: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response | Agents / reliability | University of Toronto (high confidence for Jacobsen) | 2608.08968 | **new** |
| 6 | PMCoder: Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution | Coding agents | (not stated) | 2608.06811 | **new** |
| 7 | Pseudo2CodeQA: A Benchmark for LLM-Based Structured Algorithmic Reasoning in Code Generation | Code generation / benchmark | (not stated) | 2608.09068 | **new** |
| 8 | Certifying Collective Reasoning in Multi-Agent Systems via Koopman Spectral Analysis | Multi-agent theory | Colorado State University (tentative) | 2608.05956 | **new** |
| 9 | TIPEX: A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems | Multi-agent systems | (not stated) | 2608.05791 | **new** |
| 10 | Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning | Agent security | Illinois Institute of Technology (high confidence for Kai Shu) | 2608.08303 | **new** |
| 11 | Compositional Threat Analysis of Latent Compromise in LLM Agent Systems: The Order 66 Scenario | Agent security | RIKEN / Institute of Science Tokyo (high confidence for Matsuoka) | 2608.08131 | **new** |
| 12 | Matryoshka Language Model Suites | LLM training / architecture | Cornell Tech / Cornell University (high confidence for Artzi) | 2608.09703 | **new** |
| 13 | Mismatch Matters: On-Policy Distillation Beyond Token Agreement (TIDE) | LLM post-training / distillation | (not stated; HKU for Zou, tentative) | 2608.09836 | **new** |
| 14 | Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training (TrajVal) | RL post-training | Alibaba Group (high confidence for Li/Chen) | 2608.09217 | **new** |
| 15 | Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation (OP²SD) | LLM post-training / distillation | (not stated) | 2608.09228 | **new** |
| 16 | Parameter Exploration for RLVR via Variational Learning (3PO) | RLVR / exploration | TU Darmstadt (high confidence for Gurevych) | 2608.09805 | **new** |
| 17 | SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization | LLM inference / parallelism | (not stated) | 2608.09160 | **new** |
| 18 | Repeated-Game Security for Restaking-Based Verifiable Inference | Game theory / crypto-economics | HKUST (high confidence) | 2608.09055 | **new** |
| 19 | Detecting Collusion in Peer Review: Drawing Inspiration from VCG Principle | Mechanism design | (not stated; Israel, tentative) | 2608.08486 | **new** |
| 20 | CADEngBench: It Looks Like CAD, but Does It Work? | Engineering benchmark | (not stated) | 2608.09296 | **new** |
| 21 | Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection | CAD generation / test-time scaling | (not stated) | 2608.09706 | **new** |

---

## 1. Software Engineering & Coding Agents

### 1.1 SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring

- **arXiv**: [2608.09802](https://arxiv.org/abs/2608.09802) (cs.CL / cs.SE; submitted 2026-08-10) — **NEW**
- **Authors**: Yuling Shi, Jinghan Xu, Kelin Fu, Wenhao Zeng, Shilin He, Lei Zhang, Yue Liu, Zelin Zhao, Terry Yue Zhuo, Jialun Cao, Siyu Ye, Tianyu Liu, Kai Cai, Shing-Chi Cheung, Xiaodong Gu
- **Institution**: HKUST (Cheung — high confidence) / Shanghai Jiao Tong University (Gu — high confidence, verified via web).
- **Abstract (faithful summary)**: Existing coding-agent benchmarks are rapidly saturating and their evaluation quality is under scrutiny — a recent audit found nearly **60% of unsolved SWE-bench Verified instances contain flawed tests** (overly narrow tests rejecting correct solutions, or overly broad tests checking unstated requirements), and frontier models can verbatim reproduce gold patches from training data. The paper argues **code refactoring** — coordinated, behavior-preserving changes across many files — is a substantially harder and more realistic test, yet underserved. **SWE-Bench ProMax** is an expert-curated, multilingual refactoring benchmark of **170 instances from real commits across seven languages (Python, Java, TypeScript, Go, C, C++, Rust)**. Every instance undergoes rigorous multi-stage curation: issue descriptions are rewritten from scratch for precise, unambiguous specifications; test suites are manually reviewed to remove too-narrow and too-broad tests; low-complexity or low-cross-file-scope tasks are filtered out. Instances average **11.4 modified files and 261.6 lines of code per instance**, far exceeding existing benchmarks. Frontier models under two agent scaffolds are evaluated (best-model results in the full abstract).
- **Key innovations**: (1) A refactoring benchmark that sidesteps test-quality flaws and gold-patch memorization identified in SWE-bench; (2) multi-stage human curation with rewritten specs and manually-audited tests; (3) substantially larger cross-file scale (avg 11.4 files / 261.6 LOC) than existing coding benchmarks.

### 1.2 SpecPath: Testing Coding Agents Across Contract-Equivalent Specification Histories

- **arXiv**: [2608.09799](https://arxiv.org/abs/2608.09799) (cs.SE; submitted 2026-08-10) — **NEW**
- **Authors**: Yangfan Wu, Haozhe Wang, Huanyu Yang, Jianmin Ji, Fangzhen Lin
- **Institution**: USTC (Ji — high confidence) / HKUST (Lin — high confidence, verified via web).
- **Abstract (faithful summary)**: Coding agents increasingly follow complex requirements, but their success leaves an ambiguity: do they resolve the **active specification**, or merely follow the **most salient path by which it was stated**? The paper identifies **specification-path sensitivity** — requirement histories equivalent in final meaning lead the same agent system to produce behaviorally different programs. It reframes evolving-requirement evaluation as **active-contract resolution**: before writing code, an agent must determine which requirements still count. **SpecPath** holds the repository, final contract, verifier, agent system, and execution budget fixed while varying only the revision path to the contract, and uses paired executable outcomes to reveal whether an agent realizes the same tested behavior across contract-equivalent histories. Across five calibrated tasks and fourteen agent configurations, aggregate direct and revision-history accuracy is nearly unchanged, yet **35 of 100 complete blocks that succeed on the direct specification fail on at least one equivalent history**. Implementation success on a consolidated request does not guarantee specification-path invariance.
- **Key innovations**: (1) Isolates specification-path sensitivity as a distinct coding-agent failure mode; (2) a paired-outcome diagnostic that holds everything fixed except the revision path; (3) evidence that direct-spec success ≠ robustness across equivalent histories (35/100 blocks flip).

### 1.3 OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review

- **arXiv**: [2608.09290](https://arxiv.org/abs/2608.09290) (cs.SE; v2, submitted 2026-08-10) — **NEW**
- **Authors**: Zhengfeng Li, Lei Zhang, Xianwei Wu, Zhengqi Zhuang, Yingjie Xu, Boge Wang, Shaofei Zhu, Chuan Wang, Peng Zhao, Xinyu Zheng, Guoping Rong
- **Institution**: Not stated on abstract page. Co-author Guoping Rong is affiliated with Nanjing University (tentative; single-source).
- **Abstract (faithful summary)**: LLM-based code review agents promise scalable always-on review but suffer two intertwined weaknesses: **non-determinism** (unbounded tool use makes outcomes unstable) and **context locality** (reviewer access is bounded to the diff, capping discoverable issue depth), giving rise to misaligned context retrieval, a coherence–efficiency trade-off in multi-file PRs, and hallucinated comments. **OpenCodeReview** inverts the design: rather than granting maximal freedom, it injects determinism at three deliberate pipeline points. **Rule-Guided Dispatch** uses a multi-layer rule system to deterministically select files and review criteria; **Grounded File Review** replaces free-form exploration with a curated tool set exposed through a ReAct loop while file-level parallel SubAgents balance coherence vs efficiency; **Independent Reflection** adds a falsification-first filter under an asymmetric information boundary — the reflector sees only the diff, not the agent's tool-augmented exploration — removing hallucinated comments without self-reinforcing bias. On **AACR-Bench** (200 real PRs, 10 languages, 1,505 expert-verified comments), OpenCodeReview outperforms mainstream coding agents (e.g., Claude Code, Codex) across six LLM backends, up to **2.17× higher SEM-F1** (25.10% vs 11.6%).
- **Key innovations**: (1) Deterministic engineering (rule dispatch, grounded tool set, asymmetric reflection) to stabilize agentic review; (2) a falsification-first independent reflector that sees only the diff; (3) state-of-the-art results on a multi-language expert-verified review benchmark.

### 1.4 AgentChaos: Chaos Engineering for Agent Systems via Programmatic Fault Injection

- **arXiv**: [2608.06790](https://arxiv.org/abs/2608.06790) (cs.SE; submitted 2026-08-07) — **NEW**
- **Authors**: Gou Tan, Zhensu Sun, Jieke Shi, Ting Zhang, Zilong He, Qingfu Wu, Shuai Liang, Weifeng Sun, Junda He, Pengfei Chen, Chuanfu Zhang, Lwin Khin Shar, David Lo
- **Institution**: Singapore Management University (Lo — high confidence) and NUS (Shar; verified via web).
- **Abstract (faithful summary)**: Agent systems depend on LLM APIs for every response, but those APIs can return server errors, truncated responses, or corrupted content that propagates through downstream agents and causes task failure. Existing fault-injection methods are offline, require source-code modification, or cannot modify specific response fields. **AgentChaos** is a chaos-engineering framework for controlled, runtime, **non-intrusive** LLM API fault injection: since all agent systems access LLMs through the same HTTP interface, faults are injected at this shared layer without source-code changes. It defines **crash, omission, and value faults** on content and tool-call fields, intercepts and modifies responses at runtime, and verifies each fault triggers (filtering untriggered tasks to avoid underestimating impact). Across agent systems, benchmarks, and backbone LLMs under **65 fault configurations**, all systems degrade, with pass@1 dropping by up to **50 percentage points**. Ranking is consistent across models — robustness depends on system implementation, not model capability. Existing fault-diagnosis methods achieve below 53% accuracy on fault type and below 56% on fault step.
- **Key innovations**: (1) A shared-HTTP-layer fault injection that is runtime, non-intrusive, and field-specific; (2) a systematic crash/omission/value fault taxonomy with per-fault trigger verification; (3) finding that robustness tracks system implementation, not model capability.

### 1.5 GALA+: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices

- **arXiv**: [2608.08968](https://arxiv.org/abs/2608.08968) (cs.SE / cs.AI; submitted 2026-08-10) — **NEW**
- **Authors**: Yifang Tian, Yaming Liu, Zichun Chong, Zihang Huang, Yiran Li, Hans-Arno Jacobsen
- **Institution**: University of Toronto (Jacobsen — high confidence, verified via web).
- **Abstract (faithful summary)**: Microservice root cause analysis (RCA) requires correlating failures across heterogeneous telemetry within complex service dependency graphs. Existing methods often rely on a single telemetry modality, LLM-based approaches can suffer unconstrained exploration and hallucination, and most systems stop at fault ranking without producing actionable incident response. **GALA+** is a graph-augmented LLM agentic framework centered on **graph-guided investigation**, using service dependencies to bound exploration and refine diagnosis through localized multi-modal evidence. For initial hypothesis generation it combines complementary telemetry signals with **STRIX**, a novel trace- and graph-structure-aware scoring module, then produces ranked diagnoses, incident summaries, and stratified action recommendations. **SURE-Score**, a human-guided evaluation framework co-developed with industry SRE experts, assesses RCA output quality beyond text-similarity metrics. On two microservice benchmarks, GALA+ surpasses the best LLM-based baseline by **more than 25 percentage points in AC@1**, and receives the highest ratings from both SURE-Score and independent human SRE evaluation.
- **Key innovations**: (1) Graph-guided exploration bounding to curb hallucination in RCA; (2) STRIX, a trace- and graph-structure-aware scoring module; (3) SURE-Score, an SRE-co-developed evaluation beyond text similarity; (4) end-to-end outputs from ranked diagnoses to action recommendations.

### 1.6 PMCoder: Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution

- **arXiv**: [2608.06811](https://arxiv.org/abs/2608.06811) (cs.SE / cs.AI; submitted 2026-08-07) — **NEW**
- **Authors**: Jiahao Zhang, Yifan Zhang, Yu Huang
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Resolving a real software issue with an LLM agent is a long repair episode — tens to hundreds of steps spanning exploration, hypothesis, implementation, and verification. Success depends on both the base model's local reasoning and the agent's ability to maintain an evolving plan and remember observations across phases. Existing repository-level agents typically strengthen planning or memory in isolation, leaving long trajectories vulnerable to stale evidence, repeated failed edits, and verification inferred from the agent's own claims rather than execution evidence. **PMCoder** couples a hierarchical phase planner with episodic memory, **bidirectionally**: the current plan phase conditions memory retrieval, while memory-derived trajectory statistics inform stuck detection and replanning. When available, issue-reproduction verdicts ground verification progress in execution evidence rather than self-reported completion. On **SWE-bench Verified**, PMCoder resolves an average of **25 more cases (+5.0pp)** than a harness-matched baseline, with gains persisting even where the reproduction gate never fires; further Verified-500 evaluations show the same direction across Claude Haiku 4.5, DeepSeek-V4-Flash, and an OpenHands port (at least +14 cases, +2.8pp). Evaluation on TerminalWorld's official sample suggests the plan-memory substrate transfers beyond issue resolution.
- **Key innovations**: (1) Bidirectional coupling of hierarchical planning with episodic memory (phase-conditioned retrieval + memory-derived replanning); (2) grounding verification in execution evidence via issue-reproduction verdicts; (3) consistent gains across SWE-bench Verified and multiple model harnesses.

### 1.7 Pseudo2CodeQA: A Benchmark for LLM-Based Structured Algorithmic Reasoning in Code Generation

- **arXiv**: [2608.09068](https://arxiv.org/abs/2608.09068) (cs.SE; submitted 2026-08-10) — **NEW**
- **Authors**: Shadikur Rahman, Umme Ayman Koana, Syed Muhammad Danish
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: LLMs are impressive at natural-language-to-code generation, but their ability to follow **structured algorithmic reasoning** is insufficiently understood. **Pseudo2Code** is a benchmark systematically evaluating the impact of structured pseudocode on code-generation quality and algorithmic faithfulness: **300 manually validated real-world programming tasks** spanning multiple domains and three difficulty levels (Easy/Medium/Hard), each with a problem description, structured pseudocode, reference implementation, and executable test suite, validated with a dual-stage human protocol. The companion **Pseudo2Code Agentic Framework** is a multi-stage pipeline using pseudocode as an explicit intermediate reasoning representation. Evaluated with a rubric-based framework (correctness, completeness, relevance, clarity, reasoning quality, pseudocode adherence) plus execution-based testing, the pipeline outperforms strong commercial and open-source baselines, scoring **4.78 vs 4.31 for the strongest baseline**; a human evaluation study is described (truncated in abstract).
- **Key innovations**: (1) A 300-task, dual-human-validated benchmark with executable test suites for pseudocode-grounded code generation; (2) pseudocode as an explicit intermediate reasoning representation in an agentic pipeline; (3) multi-rubric + execution-based evaluation including pseudocode adherence.

---

## 2. Multi-Agent Systems & Agent Security

### 2.1 Certifying Collective Reasoning in Multi-Agent Systems via Koopman Spectral Analysis

- **arXiv**: [2608.05956](https://arxiv.org/abs/2608.05956) (cs.MA / eess.SY; submitted 2026-08-06) — **NEW**
- **Authors**: Nuzhat Khan, Indrakshi Dey
- **Institution**: Colorado State University (Dey — tentative; inferred from author affiliation, single-source).
- **Abstract (faithful summary)**: Orchestrated collectives of LLM agents that debate and vote are an emerging form of computational intelligence — intelligent behavior resides in the **interaction**, not in any single agent. They improve task accuracy yet remain black boxes at the system level: no principled test of convergence, no bound on rounds needed, no faithful account of what drove a decision. This paper applies **Koopman operator theory** to the collective as one nonlinear dynamical system on a communication graph, reading its essential behavior off the spectrum of the Koopman transfer operator (an exact linear representation of the nonlinear dynamics, estimated from interaction traces). The spectrum yields **three machine-checkable certificates**: the sub-dominant eigenvalue λ₂ fixes the intrinsic timescale of reasoning and yields a convergence deadline computable *before* the debate runs; its eigenvector names the coherent factions the collective reasons in, and |λ₂| certifies when that explanation is valid; the leading spectral coordinates form a compressed, auditable message basis. On an attention-consensus model, the deadline tracks observed convergence with **log–log correlation 0.93** and bounds it in 96% of 24 configurations; attribution is exact when the spectrum certifies metastability; eight of 32 coordinates preserve the decision at **99.7% fidelity**; a certificate learned from 15 debates held on 60/60 held-out debates.
- **Key innovations**: (1) A system-level (non-agent-internal) theory of multi-agent consensus via Koopman spectra; (2) pre-run convergence deadlines and faction attribution certificates; (3) compressed auditable message bases with strong fidelity.

### 2.2 TIPEX: A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems

- **arXiv**: [2608.05791](https://arxiv.org/abs/2608.05791) (cs.MA / cs.AI; submitted 2026-08-06) — **NEW**
- **Authors**: Zihan Xu, Haolin Tian, Hai Jiang
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: LLM-driven multi-agent systems require multiple model invocations and complex coordination during inference; execution strategies directly affect accuracy, latency, and cost. Parallel execution improves inference-time efficiency, and the paper models it as two decision levels: **Replica Parallelism** (multiple complete solution paths at the task level) and **Structural Parallelism** (concurrent execution within a single solution path via task decomposition). **TIPEX** is a controllable execution framework that unifies the two levels under a unified execution semantics, supporting systematic combinations and analysis of parallel strategies and parameters. On **GAIA**, inference-time parallelism significantly improves accuracy and reduces end-to-end latency at the cost of increased token consumption. Replica and Structural Parallelism are **complementary across task complexities** — intermediate-difficulty tasks benefit most from coordination, and overly aggressive parallel strategies do not necessarily yield better performance.
- **Key innovations**: (1) A two-tier (replica × structural) formalization of inference-time parallelism; (2) a controllable framework for combining both levels under unified semantics; (3) evidence that coordination helps most at intermediate difficulty and over-parallelism saturates.

### 2.3 Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning

- **arXiv**: [2608.08303](https://arxiv.org/abs/2608.08303) (cs.AI / cs.MA; submitted 2026-08-08) — **NEW**
- **Authors**: Yuyang Luo, Haoran Wang, Kai Shu
- **Institution**: Illinois Institute of Technology (Shu — high confidence, verified via web).
- **Abstract (faithful summary)**: Agentic skills improve LLM agents by encoding reusable procedures, but manually authored skills adapt poorly to long-horizon tasks. **Self-evolving skill systems** automatically construct and update skills from execution trajectories, shifting acquisition from external marketplaces to a "trusted" internal pipeline — reducing exposure to direct skill-injection attacks. However, this introduces a new attack surface: an attacker can **indirectly steer skill evolution** by inducing compromised trajectories through agent interactions. **TBA (Trajectory Backdoor Attack)** is a **query-only** attack — the attacker only submits queries — that steers the pipeline toward producing a backdoored skill: crafted queries lead the agent to perform the target action and explicitly state the activation condition in the trajectory; repeating the condition-action pattern across diverse triggered tasks (clean queries unchanged) encourages the evolver to consolidate the pattern into the evolved skill. On three benchmarks across two skill-evolution systems and four open/closed-source backbone models, TBA reliably implants conditional backdoors while preserving clean-task utility, **matching or surpassing direct skill injection**.
- **Key innovations**: (1) First query-only, trajectory-poisoning attack against self-evolving skill pipelines; (2) no direct skill manipulation — only interaction-induced trajectory conditioning; (3) demonstrates a critical vulnerability in the "trusted evolution" shift.

### 2.4 Compositional Threat Analysis of Latent Compromise in LLM Agent Systems: The Order 66 Scenario

- **arXiv**: [2608.08131](https://arxiv.org/abs/2608.08131) (cs.CR / cs.AI / cs.MA; submitted 2026-08-08) — **NEW**
- **Authors**: Satoshi Matsuoka
- **Institution**: RIKEN (R-CCS) / Institute of Science Tokyo (Matsuoka — high confidence, verified via web).
- **Abstract (faithful summary)**: Named for the *Star Wars* scenario, the paper translates the "Order 66" mechanism — a preconditioned trusted population, a short activating directive, and protective authority turning against the system — into an **origin-neutral security analysis of tool-using LLM agents**. A representative scenario combines a deployed artifact or shared memory bearing a dormant destructive rule, a later email/document/update/peer message that activates it, and an agent harness granting operational and recovery authority. The paper introduces a **compositional model** explaining why no component is catastrophic alone yet their conjunction produces correlated destructive action, separating three population-reach routes (release-time pre-positioning, post-release durable seeding, peer replication) from a common core of dormancy, activation, authority, reachable targets, and failed recovery. This yields **defensive cut sets** and shows why checkpoint scanning or prompt filtering cannot close every route. A two-class example shows cross-class feedback can sustain spread even when both within-class reproduction terms are below one; isolation and persistence controls suppress the loop. Published work instantiates constituent mechanisms, while incidents demonstrate autonomous boundary crossing, malicious agent extensions, agent-assisted reconnaissance, and public-package propagation — but not yet the full dormant-instruction lifecycle.
- **Key innovations**: (1) A compositional, origin-neutral security model for latent compromise in agent systems; (2) defensible cut sets showing why prompt filtering/checkpoint scanning alone are insufficient; (3) formal analysis (two-class reproduction) of how cross-class feedback sustains spread.

---

## 3. LLM Post-Training, Distillation & RLVR

### 3.1 Matryoshka Language Model Suites

- **arXiv**: [2608.09703](https://arxiv.org/abs/2608.09703) (cs.AI / cs.CL; submitted 2026-08-10) — **NEW**
- **Authors**: Nathan Godey, Yoav Artzi
- **Institution**: Cornell Tech / Cornell University (Artzi — high confidence, verified via web).
- **Abstract (faithful summary)**: Training a language-model suite classically requires training each model separately and serving them independently. **Matryoshka training** stacks sub-models of increasing size into a single nested architecture trained end-to-end, reducing total parameter count and enabling **low-cost distillation from the largest to all smaller sub-models at every training step**, plus a natural fit for **speculative decoding** (the draft model is contained within the verifier). Validated with a suite of **500M / 1.5B / 3B sub-models**: on par with independently trained baselines on benchmarks and validation/OOD perplexities, while using **36% less training compute** and improving speculative-decoding throughput by **14–26%**. Architectural choices are ablated, offering guidance for building strong Matryoshka LM suites.
- **Key innovations**: (1) A single nested architecture jointly training a whole model suite; (2) per-step free distillation from largest to smallest sub-models; (3) draft-inside-verifier speculative decoding with 14–26% throughput gains at 36% less compute.

### 3.2 Mismatch Matters: On-Policy Distillation Beyond Token Agreement (TIDE)

- **arXiv**: [2608.09836](https://arxiv.org/abs/2608.09836) (cs.AI / cs.CL; submitted 2026-08-10) — **NEW**
- **Authors**: Zichao Yu, Chengzhi Yu, Shengze Xu, Yujin Han, Bingqing Jiang, Xu Wang, Difan Zou
- **Institution**: Not stated on abstract page. Co-author Difan Zou is affiliated with HKU (tentative; single-source).
- **Abstract (faithful summary)**: On-policy distillation (OPD) is core to modern LLM post-training, but the paper reveals a failure mode: **degenerate agreement**, where students exploit repetitive loops to achieve near-perfect token agreement with the teacher despite globally flawed responses. Shifting focus from agreement to **teacher–student mismatch**, mismatch tokens split into **student-excess tokens** (student-generated but near-zero teacher probability; their log-ratio corrections grow unbounded and destabilize the update) and **student-deficit tokens** (teacher-preferred but rarely sampled by the student; their absence blocks transfer of the teacher's reasoning patterns). **TIDE** (Token-level Independent Deficit-Excess correction) applies **bounded Hellinger shaping** to suppress the most severe sampled excesses and an **analytic teacher top-K injection** to restore deficient probability mass without requiring deficit tokens to be sampled. Across mathematical-reasoning benchmarks with multiple Qwen3 teacher–student pairs, TIDE outperforms standard OPD and recent token-selection/reward-shaping baselines; gains are more pronounced under strong mismatch, improving **Avg@8 from 6.9% to 20.3%**, reducing average response length by **3.6×**, and substantially reducing formatting failures.
- **Key innovations**: (1) Identifies degenerate agreement as an OPD failure mode; (2) a two-direction mismatch taxonomy (excess vs deficit) with distinct treatments; (3) bounded Hellinger shaping + analytic teacher top-K injection, with large gains under strong mismatch.

### 3.3 Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training (TrajVal)

- **arXiv**: [2608.09217](https://arxiv.org/abs/2608.09217) (cs.LG / cs.AI; submitted 2026-08-10) — **NEW**
- **Authors**: Ting Zhou, Zhenqing Ling, Daoyuan Chen, Qianli Shen, Yilun Huang, Ying Shen, Yaliang Li
- **Institution**: Alibaba Group (Li, Chen — high confidence, verified via web).
- **Abstract (faithful summary)**: RL has become central to LLM post-training, yet uniform task sampling allocates compute without regard to how tasks respond to optimization. Existing task-valuation methods use snapshot signals (current pass rate or reward), estimating how **solvable** a task is under the current policy — but tasks with similar solvability can differ substantially in how positively they respond to further training. The paper studies **task learnability**: a regime-conditional measure of expected positive response to continued training under a fixed RL regime. Analyzing per-task reward trajectories, learnability is **reproducible across independently sampled training contexts** and predictive of downstream utility. **TrajVal** is a lightweight probe-based estimator approximating per-task learnability from a short probe run and two endpoint evaluations, usable as a standalone static prior for task sampling or a multiplicative prior for online schedulers. On math and logical-reasoning benchmarks across multiple model scales, TrajVal improves data efficiency over uniform sampling and provides complementary gains with online scheduling.
- **Key innovations**: (1) Separates learnability from solvability as a regime-conditional, reproducible signal; (2) a lightweight probe-based estimator (TrajVal) for per-task learnability before training; (3) measurable data-efficiency gains as a standalone or multiplicative sampling prior.

### 3.4 Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation (OP²SD)

- **arXiv**: [2608.09228](https://arxiv.org/abs/2608.09228) (cs.LG / cs.AI; submitted 2026-08-10) — **NEW**
- **Authors**: Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, Junpei Komiyama
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: On-policy self-distillation (OPSD) is commonly interpreted as **transfer of privileged information**: a teacher observes the verified solution to the target problem and supervises the student's trajectory. But this conflates two effects — the reference solution reveals the answer *and* changes the context under which the teacher provides token-level supervision. **OP²SD** (On-Policy Self-Distillation from Other Problems) replaces the paired reference with a problem and solution from a **different** example, preserving the student rollout, teacher, and distillation objective. Across three models and three math benchmarks, OP²SD improves over the base model and stays competitive with OPSD. Success of OP²SD implies OPSD gains do **not** necessarily come from access to the reference solution — the teacher's **context-induced behavior** is an important factor.
- **Key innovations**: (1) An ablation (other-problem reference) separating privileged information from context-induced teacher behavior; (2) challenges the standard privileged-information interpretation of OPSD; (3) competitive results with mismatched references across three models and three math benchmarks.

### 3.5 Parameter Exploration for RLVR via Variational Learning (3PO)

- **arXiv**: [2608.09805](https://arxiv.org/abs/2608.09805) (cs.LG / cs.AI / cs.CL; submitted 2026-08-10) — **NEW**
- **Authors**: Vatsal Venkatkrishna, Nico Daheim, Iryna Gurevych
- **Institution**: TU Darmstadt (Gurevych — high confidence, verified via web).
- **Abstract (faithful summary)**: Exploration is an important ingredient in LLM RL recipes. Most existing methods control exploration in **action space** (e.g., temperature scaling), which cannot reorder tokens — it only influences output-distribution variance, limiting exploration and risking divergence or stalled training. This paper investigates **parameter-space exploration**: rollouts are generated by sampling different policies from a posterior, each potentially exploring different rollouts; sampling more or less diverse policies is a complementary control lever. **3PO** (Perturbed Parameter Policy Optimization) is a family of methods using different sampling strategies and rollout groupings for reward estimation. On **OLMo-3-1025-7B and Qwen2.5-Math-7B** across math reasoning and code generation, 3PO consistently improves average downstream performance over standard **GRPO** at near-identical FLOPs cost, and multiple parameter samples produce **fewer zero-advantage groups and malformed/incorrect rollouts** during training than GRPO and action-space baselines.
- **Key innovations**: (1) Parameter-space (posterior-sampled policy) exploration as a complementary lever to action-space methods; (2) a family of perturbed-parameter policy optimization variants; (3) consistent GRPO improvements at matched FLOPs with fewer degenerate rollouts.

---

## 4. LLM Inference & Systems

### 4.1 SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization

- **arXiv**: [2608.09160](https://arxiv.org/abs/2608.09160) (cs.LG / cs.DC; submitted 2026-08-10) — **NEW**
- **Authors**: Gyudong Kim, Wonjun Han, Young Geun Kim
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Query-Key Normalization (QK-Norm) improves training stability and quality of modern LLMs, but under **Tensor Parallelism (TP)** layerwise QK-Norm adds cross-GPU communication because the normalization factor depends on the full hidden vector. **SwiftQK** is a multi-GPU RMSNorm kernel that exchanges **only scalar normalization statistics** and overlaps the remaining Peer-to-Peer reduction with independent element-wise computation in a deadlock-safe persistent kernel. Evaluations on recent LLMs show SwiftQK reduces **QK-Norm latency by 81.4–93.9%** relative to standard TP QK-Norm using full-vector All-Gather; in end-to-end serving it reduces **TPOT by 29.5% on average** over the All-Gather baseline and by **14.3%** over an optimized scalar-aggregation implementation.
- **Key innovations**: (1) Scalar-only statistics exchange for QK-Norm under TP; (2) deadlock-safe persistent kernel overlapping P2P reduction with computation; (3) 81–94% QK-Norm latency reduction and ~30% end-to-end TPOT savings.

---

## 5. Game Theory & Mechanism Design

### 5.1 Repeated-Game Security for Restaking-Based Verifiable Inference

- **arXiv**: [2608.09055](https://arxiv.org/abs/2608.09055) (cs.GT / cs.CR; submitted 2026-08-10) — **NEW**
- **Authors**: Zhenhang Shang, Yingzhe Yu, Kani Chen
- **Institution**: HKUST (Chen — high confidence, verified via web).
- **Abstract (faithful summary)**: Restaking-based protocols enable verifiable LLM inference without zkML's proving cost or TEEs' hardware trust assumptions. Their security is commonly justified by a **one-round slashing condition**: a rational provider should not cheat when the expected penalty exceeds the cost saving from dishonest inference. This paper shows the condition can **overstate security when inference is supplied repeatedly under the same stake**, modeling verifiable inference as a discounted repeated game and identifying a **repeated-game gap** caused by proportional slashing: detected deviations reduce future penalty exposure while cost savings are earned again across queries. The gap is derived in closed form, shown to persist under minimum-stake ejection, and extended to memoryless bounded-slashing protocols covering deployed designs. The proposed deployable mechanism combines **history-dependent challenges, reputation-weighted slashing, and stake vesting**, restoring infinite-horizon subgame-perfect incentive compatibility against stationary mixed-strategy deviations above an explicit discount-factor threshold without per-query cryptographic verification. Evaluation across nine open-weight model pairs (0.5B–14B) shows the audit signal has the required concave detectability response; a Stackelberg audit-budget analysis shows improved signal responsiveness reduces the baseline audit rate by **2.6× at discount factor 0.95**. Calibrated to deployed parameters, surveyed protocols pass one-round incentive compatibility but admit repeated-game deviations.
- **Key innovations**: (1) Formal repeated-game gap in one-round slashing security arguments; (2) closed-form gap derivation incl. minimum-stake ejection and memoryless bounded-slashing protocols; (3) a deployable history-dependent + reputation-weighted + vesting mechanism restoring long-horizon subgame-perfect incentive compatibility.

### 5.2 Detecting Collusion in Peer Review: Drawing Inspiration from VCG Principle

- **arXiv**: [2608.08486](https://arxiv.org/abs/2608.08486) (cs.GT; submitted 2026-08-09) — **NEW**
- **Authors**: Itay Rabinovitz, Rica Gonen, Omer Lev, Asaf Samuel
- **Institution**: Not stated on abstract page (Israeli institutions — tentative; single-source inference).
- **Abstract (faithful summary)**: Peer review is increasingly undermined by sophisticated **collusion rings** that manipulate review outcomes to favor in-group members. Existing detection methods struggle to untangle obfuscated social ties in explicit co-authorship graphs. The paper introduces **Exclusion-Based Anomaly Detection**: analogous to VCG auctions, it formally measures the **marginal influence of suspected reviewer groups**, exposing their signature even when explicit social graphs are hidden. For scale without prior knowledge of colluding groups, the **Embedding-Based Discovery Framework** leverages continuous semantic embeddings to isolate latent collusive communities directly from their semantic profile, bypassing the adversarial limitations of explicit network analysis. It functions as an **automated auditor** requiring no prior group membership knowledge, executing a decoupled search across independent diagnostic algorithms and combining findings into consensus formations, letting organizers balance precision and recall. On large-scale datasets (based on **ICLR 2021**), the method identifies overt and subtle adversarial tactics with high sensitivity and strict **Family-Wise Error Rate (FWER)** control.
- **Key innovations**: (1) VCG-style marginal-influence measurement of suspect reviewer groups; (2) embedding-based discovery of latent collusive communities without explicit graphs; (3) an automated, no-prior-knowledge auditor with decoupled diagnostics and FWER-controlled detection.

---

## 6. CAD & Engineering

### 6.1 CADEngBench: It Looks Like CAD, but Does It Work?

- **arXiv**: [2608.09296](https://arxiv.org/abs/2608.09296) (cs.AI / cs.CV / cs.LG / cs.RO; submitted 2026-08-10) — **NEW**
- **Authors**: Harmanjot Singh, Abhra Dubey, Jorge Alejandro Amador Herrera
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: A CAD model is not engineering-grade merely because it looks correct: it must satisfy design requirements, respond predictably to parameter changes, support controlled edits, match a reference structural response under a declared analysis, and connect to other parts through valid joints. **CADEngBench** is a two-track benchmark for these capabilities. **CADEngBench-P** evaluates **300 parametric parts** (each used for one zero-to-CAD task and one functional-editing task — 600 tasks total) through B-Rep validity, engineering/DFM checks, parameter-family perturbations, functional editing, and matched linear-static FEA in **CalculiX**. **CADEngBench-A** evaluates **150 body pairs** through ranked joint retrieval, exact face-and-edge grounding, joint-frame prediction, and kinematic verification. Across eight multimodal, code-capable models, editing supplied CAD is substantially easier than generating it, while complex edits and matched FEA remain difficult; assembly predictions often locate the relevant region but fail to recover the recorded joint or mating entities.
- **Key innovations**: (1) A two-track (parametric + assembly) benchmark testing engineering behavior, not appearance; (2) matched FEA and joint/kinematic verification; (3) findings that editing ≫ generation and assembly grounding fails at the joint level.

### 6.2 Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection

- **arXiv**: [2608.09706](https://arxiv.org/abs/2608.09706) (cs.CE / cs.LG; submitted 2026-08-10) — **NEW**
- **Authors**: Aaron Haag, Altay Kaçan, Bertram Fuchs, Oliver Lohse
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: LLMs can write parametric CAD programs from natural-language descriptions, but a single sample is often wrong. Increasing test-time compute by sampling multiple candidates only helps if a good candidate can be identified — yet no ground-truth model is available at generation time, and existing systems require a separate verifier (e.g., a vision-language judge) for selection. The paper asks whether the **candidate pool itself** provides enough signal: **consensus selection** samples N parametric CAD programs, compiles them to 3D models, and returns the candidate agreeing most with the rest of the pool. It is **training-free** and compatible with existing CAD agents. Geometric and topological notions of agreement each improve their corresponding evaluation metric: on the exact candidate pools of a state-of-the-art CAD generation method, **geometric consensus improves all three geometric metrics over the method's verifier**, while topological consensus matches it on topology. Across every tested LLM and prompt variant, geometric consensus also improves geometric accuracy over random selection from the same pool, reducing **Chamfer distance by 1–10%**.
- **Key innovations**: (1) Verifier-free, training-free consensus selection among CAD candidates; (2) geometric vs topological agreement notions with matched metric improvements; (3) beats a separate VLM verifier on geometric metrics without any extra model.

---

## Cross-cutting trends

- **Coding-agent evaluation is leaving the "solved" SWE-bench era.** Two benchmark papers (SWE-Bench ProMax, Pseudo2CodeQA) plus a diagnostic (SpecPath) independently attack eval quality: SWE-bench's ~60% flawed-test rate and gold-patch memorization, specification-path sensitivity (35/100 direct-success blocks flip across equivalent histories), and the gap between appearance and real engineering behavior. The theme: benchmark what agents must actually do (large multilingual refactors, active-contract resolution, algorithmic faithfulness), not what they can memorize.
- **Agent robustness is being engineered at the infrastructure layer.** AgentChaos injects faults at the shared HTTP layer (robustness tracks system implementation, not model capability); GALA+ uses dependency graphs to bound exploration; PMCoder grounds verification in execution evidence. Agent security shifts to **indirect channels**: TBA's query-only trajectory poisoning targets trusted self-evolving skill pipelines, while the Order 66 analysis formalizes dormant-condition compromise where no single component is catastrophic.
- **On-policy distillation's "privileged information" story is under active revision.** TIDE splits teacher–student mismatch into excess vs deficit tokens (bounded Hellinger shaping + analytic top-K injection, Avg@8 6.9%→20.3% under strong mismatch); OP²SD shows gains survive swapping in a *different* problem's reference (context-induced teacher behavior, not privilege); both join the week's OPSD/OPD cluster (U-OPSD, Simple-OPD, PAST, SR-OPSD in the same-day arxiv-daily).
- **Post-training compute allocation is becoming a first-class research target.** TrajVal separates learnability from solvability as a reproducible static prior for task sampling; 3PO moves exploration from action space to parameter space (posterior-sampled policies), improving GRPO at matched FLOPs with fewer degenerate rollouts.
- **Efficiency work targets communication, not just FLOPs.** SwiftQK cuts QK-Norm TP latency 81–94% by exchanging only scalar statistics; Matryoshka LM Suites get 36% training-compute savings and 14–26% speculative-decoding gains by nesting a model suite in one architecture — both attack the coordination/serving layer rather than adding new kernels.
- **Crypto-economic and mechanism-design rigor reaches LLM infrastructure and science.** Repeated-Game Security shows one-round slashing conditions overstate restaking-protocol security (a closed-form repeated-game gap, fixed by history-dependent challenges + reputation-weighted slashing + vesting); Detecting Collusion applies VCG-style marginal-influence auditing to peer review with FWER control — economic-incentive analysis migrating into AI-native contexts.

## Methodology & caveats

- Papers selected from the fresh **Aug 9–10, 2026** arXiv submissions (retrieved via the API ahead of the Tue Aug 11 announcement, which lands ~20:00 ET), spanning cs.SE, cs.MA, cs.GT, cs.CR, and the cs.LG/cs.CL remainder, plus recall fill-in of absent Aug 6–8 submissions. Not exhaustive — the same-day [arXiv Daily Digest](./arxiv-daily.md) already claims the cs.LG/cs.CL/cs.GT/econ.TH breadth pass (31 papers) and [arXiv Paper Check](./arxiv-paper-check.md) the cs.AI+cs.IR deep scan (18 papers); this report covers the coding-agent, multi-agent/agent-security, and engineering-benchmark streams plus excess post-training/inference papers. cs.IR submissions (e.g., PushDualGen 2608.07989, Structure-Preserving Projection 2608.08583, PreGress 2608.09016) are left to the paper-check's domain and are not re-covered here. Ranked by novelty, industrial signal, and domain coverage. All 21 are **new** to the wiki (grep-verified, 0 hits).
- **Zero-overlap verification**: every candidate arXiv ID grep-checked across wiki/index.md, wiki/log.md, and wiki/synthesis/** before inclusion. Papers already covered elsewhere were excluded and are cross-referenced: Ouroboros 2608.08311 (2026-08-12 arxiv-paper-check), MARP 2608.07280 (2026-08-10 game-rl-daily), extensive-form switching regret 2608.09501 (2026-08-12 game-rl-daily). Same-day outputs (18 paper-check + 31 daily + 19 game-rl + conference-digest) are not duplicated.
- Institution/company attribution: **high confidence** where stated or a well-known affiliation (Artzi/Cornell, Matsuoka/RIKEN, Lo/SMU, Jacobsen/U Toronto, Cheung+Gu/SWE-ProMax, Kani Chen/HKUST, Gurevych/TU Darmstadt, Shu/IIT, Alibaba Li/Chen); **tentative** marks where inferred from a single co-author's known affiliation (CSU for Dey, Nanjing for Rong, HKU for Zou, Israel for the peer-review paper). No affiliation should be treated as authoritative without checking the paper.
- arXiv export/listing APIs were used for discovery; all selected-paper metadata (authors, submit dates, abstracts) verified against individual abstract pages. Submission-date caveat: 2608.05956 (Koopman) and 2608.05791 (TIPEX) are listed as submitted Aug 6 and 2608.06790 (AgentChaos)/2608.06811 (PMCoder) as Aug 7 — they sit in the recent cs.MA/cs.SE listings (arXiv IDs are not strictly ordered by submission time) and are new to the wiki.

## Related pages
- [arXiv Daily Digest (August 11, 2026)](./arxiv-daily.md) — same-day cs.LG/cs.CL/cs.GT/econ.TH breadth pass (31 papers)
- [arXiv Paper Check — AI & CTR (August 11, 2026)](./arxiv-paper-check.md) — same-day cs.AI + cs.IR deep scan (18 papers)
- [Game RL & Game AI Bot — Daily Synthesis (August 11, 2026)](./game-rl-daily.md) — same-day game RL/world-model curation (19 papers)
- [Conference Digest (August 11, 2026)](./conference-digest.md) — same-day conference roundup
- [arXiv AI Research Search (August 10, 2026)](../2026-08-10/arxiv-ai-search.md) — prior AI scan (Mon Aug 10 batch)
