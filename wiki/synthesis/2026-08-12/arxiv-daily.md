---
title: "arXiv Daily Digest — 2026-08-12"
type: synthesis
created: 2026-08-12
updated: 2026-08-12
sources: [arxiv-cs.AI, arxiv-cs.LG, arxiv-cs.CL, arxiv-cs.IR, arxiv-cs.GT, arxiv-cs.MA, econ.TH, stat.ML]
tags: [arxiv, llm, on-policy-distillation, reasoning, test-time-scaling, agents, skills, memory, kv-cache, efficiency, moe, sequential-modeling, time-series, recommendation, generative-ranking, multimodal-recommendation, hallucination-detection, interpretability, safety, games, game-theory, efx, daily-digest]
---

# arXiv Daily Digest — 2026-08-12

> **Batch note:** Today's digest covers the **Wed Aug 12, 2026 announced window — the Aug 11 submission wave (IDs ~2608.10325–2608.11208)**, plus a small late-Aug-10 tail (IDs 2608.10008–2608.10324) that the Tue Aug 11 digest stopped short of. The arXiv export API was rate-limited all session, so entries were harvested from the `/list/{cat}/recent` pages for cs.AI (211), cs.LG (164), cs.CL (95), cs.IR (22), cs.GT (9), cs.MA (14), econ.TH (5), stat.ML (19) — **399 unique IDs** — and curated into **32 papers, all grep-verified absent from the entire wiki** (zero overlap with yesterday's [arxiv-daily](../2026-08-11/arxiv-daily.md), [arxiv-paper-check](../2026-08-11/arxiv-paper-check.md), [game-rl-daily](../2026-08-11/game-rl-daily.md), or any prior digest). **Overlap handling:** 15 further papers of this window are already curated by the same-day [arXiv AI Research Search](./arxiv-ai-search.md) (GenRec, MARCO, ReOrder-OPD, UniF-MoE, CLAUDE.md-catastrophic-remembering, TORF, VERDICT, ContractSim) and [arXiv Paper Check](./arxiv-paper-check.md) (MESA, TimeRoute, LinkedIn causal, LLM-rec hallucination audit, group-rec tie-breaking, sequential-modality dropout, model merging) — those are not re-listed here. Signature themes of this window: **OPD crosses into GUI/visual agents** (Reflection-Guided OPSD, SkillLens/CardDistill), **agent memory gets a repair-after-failure paradigm and self-evolution infrastructure** (Rollback Repair, MEGA, Co-Evolution taxonomy), **structural/multimodal recommendation matures** (NTCF curvature-aware depth, VisGate, FedCGR), and **fair division sharpens its existence boundaries with machine-checked proofs** (EFX∨MMS, EFX chores in Lean 4).

---

## 1. LLM Post-Training & On-Policy Distillation

### MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training
- **Authors**: Yikai Wang, Chuansai Zhou, Yuhang Zhou, Weiqiang Wu, Cong Wu, Yue Deng, Ben Feng, Mingming Zhu, Beirong Zhou, Zhibin Wang, Sheng Zhong, Chen Tian
- **Institution**: Huawei (Ascend platform work, likely)
- **Date**: 2026-08-11
- **Link**: [2608.10823](https://arxiv.org/abs/2608.10823)
- **Abstract**: LLM RL post-training is expensive and failures (gradient overflow, loss divergence from framework adaptation / numerical precision / operator implementation) are costly to reproduce at full scale. The authors systematically analyze failures from large-scale RL training on the **Huawei Ascend platform**, summarize failure types, and identify three model-side factors relevant to fault reproduction. They build **proxy models** via structure-preserving, clustering-based expert pruning that keeps backbone architecture, routing, and task capability. Proxy models cut accelerator requirements by **50–87.5%** and per-step NPU-hours by up to **33.3×** while preserving training dynamics and reproducing the original fault signatures.
- **Key Innovation**: Low-cost surrogates for RL post-training *debugging* — a cost-multiplication concern for the wiki's LLM-post-training infrastructure thread (MISA-T, rollout scheduling).

### Scheduling Mixed RL Rollouts Beyond Prefix Locality (MISA-T)
- **Authors**: Zetao Hong, Song Yuan, Yuanhao Ding, Yibo Zhu, Daxin Jiang, Zhibin Wang, Chen Tian
- **Institution**: Nanjing University + Microsoft Research Asia + Huawei (likely)
- **Date**: 2026-08-11
- **Link**: [2608.11152](https://arxiv.org/abs/2608.11152)
- **Abstract**: Modern RL post-training mixes RLVR, RLHF, and agentic rollouts in one asynchronous inference service, but prefix-aware routing only optimizes cache reuse — it doesn't control how heterogeneous sessions (different sequence structure, interaction patterns, KV-residency times) compete for KV capacity without distorting the trainer's intended workload mixture. MISA-T is a **routing-layer admission policy** combining adaptive session admission, workload-aware KV-capacity allocation, and residency-time-aware KV accounting. Rollout-only ablations on Step3.7 and Qwen3.6-35B-A3B improve rollout throughput over a sweep-tuned vLLM Router by **53.3% and 43.6%**; in a matched 50-iteration Step3.7 run it improves throughput +35.6% and cuts mean iteration time 22.8% while keeping the consumed mixture close to target.
- **Key Innovation**: KV-capacity contention as a first-class RL-serving scheduling problem (not just cache hits) — complements the wiki's rollout-serving and KV-efficiency lines (RippleKV, vLLM Router, RL-as-a-service).

### Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation
- **Authors**: Shiyu Xuan, Zechao Li
- **Institution**: Nanjing University of Science and Technology (likely)
- **Date**: 2026-08-11
- **Link**: [2608.11191](https://arxiv.org/abs/2608.11191)
- **Abstract**: GUI agents freeze after deployment and can't adapt to unseen interfaces; test-time RL adaptation attempts exist but can't reflect on failed exploration. This paper proposes a **closed-loop Exploration→Evaluation→Reflection→Internalization** framework: the agent predicts grounding coordinates, an **MLLM-based Reflector** assesses them and emits reasoning reflections, and **Reflection-Guided On-Policy Self-Distillation** translates the high-level reflection into dense token-level supervision via a conditioned self-teacher. A **Contrastive Calibration** step stops incorrect autoregressive prefixes from corrupting supervision during failed exploration. Across six benchmarks it improves the base model by **7.4% avg** — reported as the first OPSD application to test-time GUI grounding adaptation.
- **Key Innovation**: The wiki's OPSD cluster (Aug 7–11) extends to *visual/GUI* test-time adaptation, with reflection-as-teacher-context and a prefix-corruption guard.

### SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation
- **Authors**: Zhou Liu, Ligang Huang, Zeli Su, Zewei Pan, Zhaoyang Han, Xing Chen, Yuanfeng Song, Wentao Zhang
- **Institution**: HKUST (Guangzhou) + Peking University (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10775](https://arxiv.org/abs/2608.10775)
- **Abstract**: GUI agents lack *visual* procedural memory — they recognize controls but not which workflow is active or what evidence confirms progress. **Visual Skill Cards (VSCs)** bind reusable procedures with applicability cues, visual evidence, and verification signals. SkillLens builds VSCs from heterogeneous interaction traces (Trace-to-Visual-Skill-Card), retrieves relevant cards at inference, and selectively expands only needed evidence for a frozen VLM executor. The same representation powers **CardDistill**, using VSC evidence as privileged teacher context to train a student acting without runtime retrieval. On Multimodal-Mind2Web and WebLINX-BrowserGym, SkillLens improves frozen GPT-5.4-mini by **+11.6 Step SR / +2.9 Overall**; CardDistill improves student-only Qwen3-VL-2B by **+12.0 / +3.2**.
- **Key Innovation**: A *visual* skill representation (state-conditioned, evidence-linked) feeding both retrieval-augmented execution and OPD — extends the wiki's skills cluster (SkillLens is a visual analog of SKALD's skill-conditioned teacher).

---

## 2. Agents, Skills & Memory

### SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure
- **Authors**: Xiaofan Bai, Hongqiang Lin, Chao Liu, Yantao Zhang, Xuan Jin, Xipeng Cao, Yuhong Li
- **Institution**: Duke University
- **Date**: 2026-08-11
- **Link**: [2608.11079](https://arxiv.org/abs/2608.11079)
- **Abstract**: Self-evolving agents accumulate skills by appending procedures and fixes; over time the same requirement gets restated across branches/examples/warnings and common action sequences get copied rather than reused, so skills balloon in injection cost and maintenance. Generic prompt compression fails because a skill is a structured artifact (name/description define applicability, workflow controls execution, tool/output contracts constrain validity, rare exceptions stay essential). SkillZip compresses **without evaluation**: it finds the skill's shortest faithful structural explanation — "explain once, reference many" — formalized as a **typed minimum-description-length objective** over a skill contract + residual with a hard coverage constraint on every trigger, workflow edge, tool requirement, obligation, and output field. It has a one-shot mode (one structured extraction call + deterministic optimization) and a **Zip-on-Write** continual mode that integrates each self-evolution patch without replaying tasks.
- **Key Innovation**: Structure-aware, evaluation-free skill compression with a coverage guarantee — a direct complement to the wiki's skill-accumulation and prompt-compression threads (SkillOpt, self-evolving agents).

### MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale
- **Authors**: Yuhang Yao, Zeyu Wang, Wanyi Chen, Tongyun Yang, Yuhang Han, Jie Xiao, Chengke Bao, Tianyi Zhao, Lynn Ai, Eric Yang, Tianyu Shi
- **Institution**: University of California, Los Angeles + industry (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10333](https://arxiv.org/abs/2608.10333)
- **Abstract**: LLM agents mix calls that need careful reasoning with structured steps (formatting, tool-argument construction); routers assign easy calls to a small model and hard ones to a large model, but leave the small model's capability unchanged — savings bounded by what the student can already solve. MERA **improves the student itself**: each cycle replays failed student invocations for execution-verified teacher demonstrations, distills recurring procedures into an iteratively updated **SkillBook**, and fine-tunes a student LoRA via SFT + optional GRPO. Routing becomes deployment machinery: improved student served behind a **cost-calibrated router with verifier-backed fallback**; a candidate SkillBook/adapter/router is admitted only when joint replay preserves task quality. Four-cycle adaptation raises Qwen2.5-Coder-1.5B from 28.7%→49.7% pass on held-out HumanEval+MBPP; deployed policy retains 88.3% pass at **60.8% of always-Luna cost**.
- **Key Innovation**: "Evolve the student, not just route around it" — capability growth + verifier-backed cost routing, converging with the wiki's LoRA/GRPO agent lines (MERA joins the skill-adaptation cluster).

### From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents
- **Authors**: Caili Yu, Yiqi Wang, Jiaqi Zhang, Yiqun Duan, Mingkai Zheng, Zhangkai Wu, Kaize Shi, Taotao Cai
- **Institution**: HUST + others (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10502](https://arxiv.org/abs/2608.10502)
- **Abstract**: Persistent memory makes agent errors durable — a poisoned/stale/misattributed record alters reasoning, tool use, answers, and future writes. Existing defenses detect/delete suspicious memories or revise the current response, but deletion leaves propagated claims active and full reset destroys benign state. This paper formulates **post-failure memory recovery** (given a failed execution and diagnosed faulty memories, recover both answer and persistent state while retaining unaffected work) and builds **dependency-guided rollback repair**: a typed memory-to-action graph from runtime provenance, explicit downstream-dependency tracing, preservation of candidates with independent trusted support, deactivation of unsupported memory state, and selective replay of only answer-relevant affected computation. On a 150-case controlled benchmark it achieves **85.3% recovery vs 77.3%** for the best competitor, removes all diagnosed faulty memories, preserves all benign memories; on a 50-case LongMemEval-V2-derived stress test, 68.0% vs 54.0% with highest claim-invalidation F1 (0.669 vs 0.603).
- **Key Innovation**: Repair-after-failure as a first-class memory operation — rollback + selective replay instead of detection-only, complementing the wiki's agent-memory correctness line (DocMemo, memory poisoning defenses).

### MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph
- **Authors**: Jung Hwan Lee, Kyu Ho Lee, Gwang Hoon Yoo
- **Institution**: Incheon National University (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10504](https://arxiv.org/abs/2608.10504)
- **Abstract**: As coding agents handle implementation, the bottleneck shifts from building agents to building infrastructure that improves them. MEGA is a **Meta Evaluation-Grounded Adaptation** infrastructure: Layer 1 distills reusable wisdom from agent sessions (behavioral-pattern clustering + empirical A/B validation) into durable assets; Layer 2 decomposes assets into atomic **PCR (Primary-Context-Resultant) units** in a typed **Wisdom Graph** and performs deductive/abductive/inductive reasoning over them, assembling context-specific execution plans via compositional retrieval that surfaces bridging knowledge embedding-similarity misses; Layer 3 runs multi-agent collaborative optimization over heterogeneous workflows (code nodes, LLM calls, tool agents) with controlled evaluation attributing improvement to specific changes. Layer-3 evidence drives self-evolution of both curation strategies and optimization trajectories.
- **Key Innovation**: "Optimizing an agent system and evolving the knowledge that guides optimization are one process" — an infrastructure-level synthesis for the wiki's self-evolving-agent line (distinct from skill-graph approaches by its typed wisdom graph + attribution loop).

### GitSkills: A Dataset of Agent Skills on GitHub
- **Authors**: Giuseppe Destefanis, Daniel Graziotin, Matteo Vaccargiu, Marco Ortu
- **Institution**: University of Cagliari + University of Stuttgart (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10906](https://arxiv.org/abs/2608.10906)
- **Abstract**: Agent skills (a folder with a SKILL.md plus optional scripts/references) spread by copying between repos — no central registry, no compiler, no type checker validates them. Nine months after Anthropic's October 2025 open spec, skill files number in the millions on public GitHub. **GitSkills** collects **3,797,117 SKILL.md files from 282,200 public repositories (July 2026)**, groups identical files into 1,877,981 distinct contents, and enriches one representative per group with full text, parsed front matter, folder contents, repository metadata, and (subset) commit history — one self-contained SQLite file for research on adoption, reuse, structure, authorship, maintenance, and security of agent skills.
- **Key Innovation**: The first large-scale empirical corpus of agent skills — the wiki's skills cluster (SkillZip, SkillLens, SkillSentry) gains a population-level measurement substrate.

### Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design
- **Authors**: Qing Zong, Jiayu Liu, Junhao Shen, Zecong Tang, Linsi Wu, Yuxuan Liu, Rui Wang, Zhaowei Wang, Weiqi Wang, Cheng Qian, Xiusi Chen, Yangqiu Song
- **Institution**: USTC + HKU + UIUC (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10299](https://arxiv.org/abs/2608.10299)
- **Abstract**: Single-entity self-evolution is bounded by a static learning context (fixed tasks, fixed feedback). This survey organizes **co-evolution** — multi-component self-evolution where agents and environment impose adaptive pressure on each other — into a three-stage taxonomy tracking how systems shed human-engineered constraints: **Agent–Agent Co-Evolution** (adversarial, collaborative, organizational adaptation), **Agent–Environment Co-Evolution** (adaptive tasks/feedback/interaction spaces), and **Meta Co-Evolution** (making the evolution mechanism itself evolvable). Open challenges: evaluation, scaling across components, and keeping increasingly autonomous evolution safe and controllable.
- **Key Innovation**: A unifying taxonomy for the "self-evolution beyond a single agent" cluster — a reference frame for the wiki's agent-evolution threads (MEGA, MERA, self-evolving harnesses).

---

## 3. Reasoning & Test-Time Scaling

### ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling
- **Authors**: Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat, Soumyabrata Pal, Ramasuri Narayanam, Dinesh Manocha
- **Institution**: University of Maryland, College Park
- **Date**: 2026-08-11
- **Link**: [2608.10928](https://arxiv.org/abs/2608.10928)
- **Abstract**: LRMs scale test-time compute by generating longer chain-of-thought, but sequential scaling shows diminishing/negative returns — longer traces compound errors and drift from the problem. ThinkRetrieve **augments the reasoning trace itself with dynamically retrieved solved examples at each reasoning step**: given an external corpus of problems with step-by-step solutions, it retrieves relevant exemplars per intermediate step and injects them into the thinking trace — guidance on *how to reason*, not merely what facts are relevant. Across five reasoning models (1.5B–8B) on GSM-8K, MATH-500, AIME 2025, and SciQ, it consistently beats standard test-time scaling with relative gains up to **60% on AIME 2025**.
- **Key Innovation**: Retrieval-augmented *reasoning traces* (retrieve-into-thinking) as a corrective to diminishing-returns sequential scaling — connects the wiki's test-time-scaling and RAG-agent threads.

### From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in LLMs (MPAR-Bench)
- **Authors**: Si'an Xie, Jiaxun Liu, Biao Yang, Wei Yuan, Fan Yang, Tingting Gao, Ming Wu
- **Institution**: Beijing University of Posts and Telecommunications (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10444](https://arxiv.org/abs/2608.10444)
- **Abstract**: LLM reasoning progress is mostly *depth* (longer inferential chains); *breadth* — exploring multiple semantic directions in parallel and integrating clues — is unexamined. MPAR-Bench isolates reasoning breadth via **multi-point associative reasoning**, inspired by the cooperative game *Just One*: recover a hidden target from several independently generated, semantically diverse clues. 1,000 bilingual (en-zh) items built by a multi-agent clue-generation pipeline with embedding-diversity filtering and human verification. Perturbations (clue masking, order shuffling, distractor injection, multi-step clues) reduce accuracy by 9–18pp (en) and 5–12pp (zh); thinking mode improves standard accuracy but not perturbation robustness, and extended reasoning can overturn an initially correct hypothesis — depth does not confer breadth.
- **Key Innovation**: First dedicated benchmark for multi-point associative (breadth) reasoning, with a robustness suite showing thinking-mode fragility — a measurement complement to the wiki's reasoning-evaluation line.

### Optimal Stopping of Self-Refining Foundation Models
- **Authors**: Kim Hammar, Tansu Alpcan, Emil C. Lupu
- **Institution**: University of Melbourne
- **Date**: 2026-08-11
- **Link**: [2608.10729](https://arxiv.org/abs/2608.10729)
- **Abstract**: Self-refinement loops (generate → verifier feedback → in-context refine) improve output but consume compute per iteration. This paper formalizes the loop as an **optimal stopping problem** — decide the number of refinement iterations from expected improvement vs cost — and derives stopping policies computable via stochastic approximation. On a coding benchmark, the derived policies are **significantly more cost-efficient than prior stopping policies**, giving a principled answer to "when to stop self-refining."
- **Key Innovation**: A formal optimal-stopping lens on test-time refinement budgets — pairs with the wiki's budget-aware reasoning lines (s1, budgeted agent evals, test-time compute allocation).

---

## 4. Recommendation & Ranking

### Neural Tree Collaborative Filtering: Rethinking Graph CF as Tree CF with Curvature-Aware Propagation Depth (NTCF)
- **Authors**: Jinfeng Xu, Zheyu Chen, Ziyue Peng, Shuo Yang, Jinze Li, Wenhao Yuan, Jian Chen, Edith C. H. Ngai
- **Institution**: University of Hong Kong + Beijing Institute of Technology + HKUST
- **Date**: 2026-08-11
- **Link**: [2608.10297](https://arxiv.org/abs/2608.10297)
- **Abstract**: Graph CF propagates embeddings through a fixed number of layers, ignoring that nodes differ in local connectivity — peripheral nodes over-smooth while hubs stay under-explored. NTCF re-interprets each node's local neighborhood as a **rooted tree** and assigns node-specific propagation depth from a closed-form **local-degree-imbalance score serving as a discrete Ricci-curvature proxy**. Theory: NTCF strictly generalizes NGCF (degenerating when curvature adjustments vanish), and the curvature-aware schedule retains strictly more discriminative info at deep layers on positively-curved peripheral nodes than uniform depth. NTCF outperforms most widely-used GCF backbones and upgrades self-supervised models when swapped in as backbone.
- **Key Innovation**: Discrete-Ricci-curvature-aware per-node propagation depth — a principled fix for the fixed-depth over-smoothing problem, relevant to the wiki's graph-CF/self-supervised-rec line.

### Deciding When to Rely on Visual Information: Gated Multimodal Fusion in Sequential Recommendation (VisGate)
- **Authors**: Natalija Glisovic, Danica Kragic, Martin Tegner
- **Institution**: KTH Royal Institute of Technology + IKEA Retail (Ingka Group)
- **Date**: 2026-08-11
- **Link**: [2608.10700](https://arxiv.org/abs/2608.10700)
- **Abstract**: Multimodal sequential recommenders fuse visual and collaborative signals uniformly, treating visual utility as fixed. VisGate argues visual utility is a **latent contextual variable** depending on item and the user's sequence context, and makes adaptive item-level fusion decisions conditioned on item embeddings + current sequence. Visual representations are learned via **contrastive objective over sequential co-occurrence patterns** (preserving complementarity rather than aligning spaces). Beyond competitive performance, the learned gate serves as a **measurement tool**: visual utility varies across items, increases under interaction sparsity, and correlates with visual distinctiveness.
- **Key Innovation**: Gating-as-measurement for *when* visual signals help — interpretable adaptive fusion, complementing the wiki's multimodal-rec cluster.

### FedCGR: Federated Cross-Domain Generative Recommendation
- **Authors**: Zhuodong Liu, Hugen Lv, Xiangyu Li, Bohan Guo, Peiyu Hu
- **Institution**: Beijing Jiaotong University + Shanghai Jiao Tong University + University of Malaya + Xi'an Jiaotong-Liverpool University
- **Date**: 2026-08-11
- **Link**: [2608.10929](https://arxiv.org/abs/2608.10929)
- **Abstract**: Cross-domain recommendation (CDR) needs behavioral anchors to align item spaces, but federated deployment makes them sparse/unavailable/privacy-sensitive. FedCGR revisits federated CDR as **generation over a stable semantic item language**: items as discrete **semantic ID (SID) sequences** from public item-side metadata align domains via a shared vocabulary without exchanging private interactions. The tokenizer must stay fixed (semantic-only bottleneck), and standard federated averaging causes negative transfer under domain heterogeneity, so FedCGR keeps the item language stable and makes adaptation explicit: **local CF evidence injected via a reliability-aware semantic interface**, and a **prototype-personalized generator** that selectively aggregates shared parameters by domain relatedness. Wins on six Amazon cross-domain scenarios vs federated generative baselines.
- **Key Innovation**: SID-vocabulary-based cross-domain alignment + prototype personalization for federated generative CDR — relevant to the wiki's generative-rec and federated-rec threads (CIKM 2026).

---

## 5. Sequential Modeling & Time Series

### Do Time-Series Forecasters Use the Right History? Recoverability, Recovery, and Functional Use of Temporal Delays
- **Authors**: Qipeng Qian, Yuntao Qian
- **Institution**: Zhejiang University
- **Date**: 2026-08-11
- **Link**: [2608.10433](https://arxiv.org/abs/2608.10433)
- **Abstract**: Accuracy doesn't tell you which past inputs produced a prediction. The paper separates three questions for models with known delay structure: can the true delay be recovered from data, does the model report it, and does the forecast actually use that history? It derives input-conditioned recoverability measures separating intrinsic ambiguity from model error, and proves a **delay report can be arbitrarily reliable while forecast risk approaches the oracle yet the predictor still uses the wrong lag**. In finite samples, among correct-report, near-oracle forecasts, the reported history is *functionally unused* in **55.4% (N-HiTS) and 92.7% (TCN)** of cases; routing through the reported history removes off-report bypass paths.
- **Key Innovation**: An evaluation-decomposition result showing "good forecast + correct delay report" doesn't imply correct history use — measurement hygiene for the wiki's time-series cluster.

### REATS: LLM Reasoning-Based Ensemble Learning for Adaptive Time Series Forecasting
- **Authors**: Xu Zhang, Chang Xu, Hui Sun, Nan Ma, Zijian Zhang, Peng Wang, Wei Wang, Li Zhao
- **Institution**: Alibaba (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10149](https://arxiv.org/abs/2608.10149)
- **Abstract**: No single forecaster dominates all samples; ensembles exist but rely on fixed rules or black-box numeric models. REATS uses an **LLM as an intelligent ensemble router**: it jointly processes textual temporal-pattern descriptions and numeric features to produce interpretable, sample-adaptive ensemble weights via chain-of-thought. Contributions: (i) structured hybrid textual-numeric input pipeline with fixed token cost and rule-based CoT construction (no API dependency) plus retrieved similar-sample priors; (ii) a token-efficient percentage-table supervision format reducing numeric complexity and mitigating hallucination; (iii) a **two-stage SFT+GRPO** framework with a reciprocal reward mapping that turns unbounded MSE gaps into bounded signals with amplified near-oracle sensitivity. Wins on eight benchmarks with natural-language explanations and out-of-domain generalization.
- **Key Innovation**: LLM-reasoning ensemble routing with a regression-specific GRPO reward fix — a hybrid for the wiki's LLM-time-series line (SCALER, retrieval-augmented TS).

### ChronoSSM: Training for Temporally Aware Representations in Autoregressive State Space Models
- **Authors**: Adrien Schoen, Nachiketa Ratnakar Patil, Arjun Bhagoji, Francesco Bronzino
- **Institution**: ENS de Lyon + IIT Bombay
- **Date**: 2026-08-11
- **Link**: [2608.10120](https://arxiv.org/abs/2608.10120)
- **Abstract**: Sequence models predict *what* happens and treat *when* as secondary; the common strategy trains a separate timing model on event-only representations — assuming those representations already contain temporal structure. ChronoSSM is an **autoregressive SSM jointly modeling events and timestamps** with a shared backbone trained under combined token and temporal generation objectives. It compares the *joint* regime (temporal supervision updates the backbone) against the *two-stage* regime (frozen event representations) across four domains. Joint training consistently makes inter-arrival information more recoverable from frozen representations **without systematic degradation in content-generation quality**.
- **Key Innovation**: Joint temporal supervision as a representation-quality lever — evidence that timing should be first-class in sequence models, relevant to the wiki's SSM/linear-transformer and temporal-modeling lines (MixFormer, TALA).

---

## 6. KV Cache, Efficiency & Model Interfaces

### ImpactHO: Importance-Aware KV Cache Transfer for Multi-User Edge LLM Handover
- **Authors**: Minwoo Kim, Soochang Song, Namyoon Lee, Bang Chul Jung, Yongjune Kim
- **Institution**: Ajou University + POSTECH (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10545](https://arxiv.org/abs/2608.10545)
- **Abstract**: Edge LLMs need KV-cache transfer when a user hands over between edge nodes, but simultaneous handovers saturate backhaul within mobility-limited windows. ImpactHO orders each user's cache by **importance** and transmits only its most informative fraction, turning token-level sparsity into communication savings. Cast as a multi-user backhaul allocation problem maximizing average accuracy: per-user partial-cache accuracy is a utility sigmoid (R²>0.99 on RULER across models/contexts); importance ordering front-loads high-value entries so the concave region spans nearly the whole cache, making each slot allocation convex with a **closed-form weighted water-filling solution** generalizing information-theoretic water-filling. Achieves >93.7% average accuracy in a 500ms window (within 0.5pp of the full-cache ceiling), 98.2–99.5% of a clairvoyant upper bound.
- **Key Innovation**: KV *transfer* (not just compression) under a mobility-communication budget — a systems-level extension of the wiki's KV-cache line into edge handover.

### MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices
- **Authors**: Eunjeong Kim, Yeong Jun Jeon, Myeonggyun Han
- **Institution**: Kyungpook National University
- **Date**: 2026-08-11
- **Link**: [2608.10362](https://arxiv.org/abs/2608.10362)
- **Abstract**: Adaptive speculative decoding exploits input/stage variation in draft-model choice, but on memory-constrained edge devices the **draft-switching overhead kills throughput** — a mismatch between draft selection and draft availability under tight memory budgets. MemSpec **decouples draft selection from execution** via proactive resident working-set management: a lightweight predictor estimates draft effectiveness from prompt/generation context while a memory-aware scheduler reduces reactive model-loading overhead. On a Jetson Orin Nano, MemSpec improves steady-state generation throughput **40.7% on average** over SOTA bandit-based adaptive methods, closely approaching the oracle upper bound.
- **Key Innovation**: Memory-aware draft scheduling as a runtime concern — speculative decoding for edge with resident working sets, complementing the wiki's speculative-decoding and edge-inference lines (LCTES 2026).

### Cracks in the Foundation: Seemingly Minor Architectural Choices Impact Long Context Extension (OlmPool)
- **Authors**: Amanda Bertsch, Luca Soldaini, Matthew R. Gormley, Graham Neubig, Hannaneh Hajishirzi, Kyle Lo, Dirk Groeneveld
- **Institution**: University of Washington + Allen Institute for AI
- **Date**: 2026-08-11
- **Link**: [2608.10296](https://arxiv.org/abs/2608.10296)
- **Abstract**: Minor architectural choices (normalization, GQA, pretraining context length, sliding-window attention — each used by at least one of Olmo/Llama/Qwen families) have a **compounding negative effect on long-context extensibility**: any one alone is minor, but combining three or more drops downstream performance by up to **47%** — and these differences are invisible to short-context loss. Controlled ablations (data/tokenizer/extension recipe fixed) show much of cross-family long-context variation is architectural; they release **OlmPool, 26 comparable 7B models** with pre/post long-context checkpoints (~170,000 GPU hours), including architectures beating Llama-3-style on extensibility, plus analysis of attention-sink behavior per architecture (COLM 2026).
- **Key Innovation**: A controlled multi-architecture ablation *pool* showing long-context extensibility is architecture-sensitive in ways short-context evals miss — infrastructure for the wiki's long-context and architecture-ablation line.

---

## 7. Interpretability & Safety

### Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders
- **Authors**: Nikolai Bolik, Lennart Stöpler, Artur Andrzejak
- **Institution**: Heidelberg University (likely)
- **Date**: 2026-08-11
- **Link**: [2608.11197](https://arxiv.org/abs/2608.11197)
- **Abstract**: Prior work uses cosine similarity over dense representations to test whether LLMs recover human category boundaries. This paper revisits with **overlap over active SAE latent sets** as an interpretable similarity measure. SAE sets recover union-like structure in controlled toy models and induce coherent neighborhoods in natural text, but for human-concept analysis they **do not recover category boundaries or typicality more faithfully than dense embeddings or residual states** — they track model-internal similarity instead. Under controlled semantic modifications there's a substantial mismatch between human judgements of conceptual change and active-set change — evidence that SAE features don't compose via bag-of-features semantics outside idealized settings.
- **Key Innovation**: A cautionary set-level analysis of SAE compositionality — directly qualifies the wiki's SAE feature-composition and interpretability line (MMDiff, model diffing).

### Off-Axis, On Purpose: Where a Transformer Computes Concepts and Why It Does So
- **Authors**: Mark Oskin
- **Institution**: University of Washington
- **Date**: 2026-08-11
- **Link**: [2608.10251](https://arxiv.org/abs/2608.10251)
- **Abstract**: A transformer's answer lives on the unembedding read-out axis, but intermediate states are largely **off-axis** — usually treated as an obstacle to interpretation. This paper shows it's *functional*: a 12-layer model computes in two phases. Early, every sublayer writes into a subspace held near-orthogonal to the read-out (attention 75–96° off at every depth); moving attention values onto the read-out is 64–84× more damaging than a matched random rotation, entirely in cross-token mixing (the subspace insulates composition from the vocabulary). The answer arrives on-axis late, by addition. Pressing every layer onto the read-out (as early-exit training does) matches baselines on perplexity/LAMBADA/BLiMP while shrinking the concept workspace from ~25 to ~14 effective dimensions — a change none of those benchmarks register. The geometry can be imposed (via a fixed rotation at the phase boundary or a sparse absorbable rotation), and which rotation is immaterial across 25 runs/13 distinct rotations.
- **Key Innovation**: Off-axis computational geometry as a *feature*, not an artifact — with an imposed-geometry recipe and a demonstration that standard benchmarks are blind to the concept-phase workspace. A strong mechanistic-interpretability contribution (orthogonal to SAE lines).

### ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions
- **Authors**: Xinzhe Huang, Biwu Yao, Kedong Xiu, Mengnan Zhao, Di Wang, Puning Zhao, Tianhang Zheng
- **Institution**: HKUST (Guangzhou) + KAUST (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10621](https://arxiv.org/abs/2608.10621)
- **Abstract**: Guardrails typically treat safety as deterministic classification over discrete token sequences, discarding probabilistic structure and ignoring early-generation uncertainty. **ProbGuard** is the first completely probabilistic, architecture-agnostic guardrail: it uses the LLM's **early output distributional signals** to estimate/calibrate the safety probability of continued generation, enabling early stopping of unsafe outputs. Safety risk is formalized as the unsafe probability of continued generation dynamics, estimated via Monte-Carlo sampling and post-trained on distributional signals + calibrated risk. It achieves the best calibration across all nine model-dataset settings (avg Brier −79.6%, ECE −71.9% vs best baseline) and limits attack success rate to ≤1% across six jailbreak attacks from **only the first ten decoding steps**.
- **Key Innovation**: Distribution-based, calibration-first guardrails with early-stop — a probabilistic safety layer that complements the wiki's deterministic guardrail/jailbreak-defense line (KVGov timing side-channels, jailbreak attacks).

### Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique (Latent Critic)
- **Authors**: Sanidhya Vijayvargiya, Rahul Lokesh
- **Institution**: —
- **Date**: 2026-08-11
- **Link**: [2608.10430](https://arxiv.org/abs/2608.10430)
- **Abstract**: LLM agents execute hallucinated, undesired actions rather than express uncertainty; existing detectors either fail to localize or add prohibitive latency. The **Latent Critic** is a lightweight LoRA running concurrently with a frozen base LLM that restructures the residual stream — amplifying latent grounding signals and translating them into **localized natural-language feedback within a single sequence**, without secondary inference loops. Mechanistic analysis (activation patching, layer-wise probing) shows it re-arranges pre-existing uncertainty geometry into a linearly separable representation. On tool-calling it achieves **0.966 AUROC and >80% localization accuracy** (e.g., ungrounded: date), beating equivalent-scale external detectors, semantic entropy, and passive probes; in a closed-loop ReAct environment it intercepts hallucinations pre-execution with negligible latency.
- **Key Innovation**: In-line, training-light hallucination *localization* via residual-stream restructuring — actionable critique without a second model, complementing the wiki's hallucination-detection and uncertainty threads (UniProbe, semantic entropy).

### TAF-MED: Multi-Turn Safety Refusal Collapse in LLMs Under Declared Self-Treatment Intent
- **Authors**: Waleed Jamil, Raphael Schmitt
- **Institution**: Technical University of Munich + University of Freiburg
- **Date**: 2026-08-11
- **Link**: [2608.10258](https://arxiv.org/abs/2608.10258)
- **Abstract**: Medical-safety benchmarks don't isolate whether medication-safety boundaries persist across follow-ups after declared self-treatment intent. TAF-MED is a **physician-reviewed benchmark of 500 fixed three-turn scenarios**; eight LLMs evaluated over 4,000 conversations, with a rubric-based judge (94.3% agreement with adjudicated physician labels, κ=0.895). **71.6% of conversations contained an UNSAFE response, and 61.4% of those beginning with a strictly SAFE response later collapsed to UNSAFE** (model-level collapse 24.4%–96.2%); four of 28 model pairs reversed order between initial unsafe and collapse rates.
- **Key Innovation**: First-turn safety as an incomplete proxy — multi-turn refusal-collapse measurement for medical LLM safety, relevant to the wiki's safety-persistence and refusal-robustness threads (echoes the subjective-verification "reasoning collapse" finding).

### Data Attribution of Emergent Misalignment with Persona Features
- **Authors**: Clemens Vetter, David Kaczér, Lucie Flek, Florian Mai
- **Institution**: University of Bonn
- **Date**: 2026-08-11
- **Link**: [2608.11025](https://arxiv.org/abs/2608.11025)
- **Abstract**: Emergent misalignment (EM) — fine-tuning on a narrow task causing unrelated harmful behavior — is attributed to persona features: latent directions pre-training acquired that misaligned fine-tuning amplifies. Using **SAE-based model diffing** across four open-weight models, this paper finds jailbreak-persona, sarcasm, deception, and manipulation features are amplified by misalignment fine-tuning while safety/assistant-identity features are suppressed. Steering single features induces misalignment in aligned models up to **62%** (exceeding the 35% from fine-tuning) and re-aligns misaligned models to near baseline. Attribution to a corpus of 1M pre-training documents retrieves villainous/domination/harmful-agency narratives — but **fine-tuning on these human documents does not reliably induce EM**, while synthetic instruction-response pairs from the same content do (and transfer across model families). Semantic relevance alone is insufficient; response structure/model phrasing matters.
- **Key Innovation**: Causal person-feature attribution for EM with a negative result on purely semantic induction — the wiki's EM/persona line gains data-level attribution and a structure-vs-content separation.

### UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs Using Multi-Structural Internal Representations
- **Authors**: Dvir Samuel, Guy Bar-Shalom, Fabrizio Frasca, Ethan Fetaya, Yftah Ziser, Gal Chechik, Haggai Maron
- **Institution**: Bar-Ilan University + NVIDIA Research (likely)
- **Date**: 2026-08-11
- **Link**: [2608.10835](https://arxiv.org/abs/2608.10835)
- **Abstract**: LVLMs hallucinate content unsupported by the visual input; mitigation needs token-level localization without discarding whole responses. UniProbe models a **frozen LVLM's heterogeneous computational trace from a single forward pass**: a directed graph over image patches, query tokens, and generated tokens with attention weights as relations, processed by interleaved structure-aware modules — **GNN** (relational), **ViT** (2-D visual geometry), **GRU** (response order). A streaming variant enables hallucination-aware decoding (detect and resample during generation) and a self-adaptation strategy aligns the detector with the LVLM's own generations. SOTA token-level and object-hallucination detection across backbones; during decoding it reduces object hallucinations up to **55% at 1.06×** generation latency.
- **Key Innovation**: Graph-structured internal-trace modeling for *token-level* LVLM hallucination detection with streaming resampling — extends the wiki's hallucination-detection line to VLMs at decoding time.

---

## 8. Games & Game Theory

### The Game of Marginal Utilities
- **Authors**: —
- **Institution**: —
- **Date**: 2026-08-11
- **Link**: [2608.10373](https://arxiv.org/abs/2608.10373)
- **Abstract**: A noncooperative resource-allocation game where m players split fixed resources among n projects and player j's payoff is Σ_i a_i·x_i^j/(b_i+Σ_ℓ x_i^ℓ) — diminishing returns plus congestion. The paper proves a **unique Nash equilibrium** characterized by an equimarginal principle: after ordering projects by a_i/b_i, each player invests in an initial segment, segments are **nested across players**, and the equilibrium decomposes into consecutive activity zones; players with more resources invest weakly more everywhere. In the fully-active regime the equilibrium reduces to a single scalar nonlinear equation for the aggregate marginal-utility rate.
- **Key Innovation**: A clean uniqueness + structure theorem (nested initial segments, zone decomposition) for a congestion-with-diminishing-returns game — a theoretical entry for the wiki's market-design/allocation-games thread.

### To EFX OR to MMS, That Is the Question
- **Authors**: —
- **Institution**: —
- **Date**: 2026-08-11
- **Link**: [2608.10397](https://arxiv.org/abs/2608.10397)
- **Abstract**: The agent-wise disjunction of EFX (envy-free up to any item) and MMS (maximin share) for indivisible items — every agent must satisfy one or the other — surprisingly does **not** restore existence: counterexamples with three agents and eight submodular goods, and three agents and seven submodular chores, strengthen recent EFX impossibility results. Positively, existence holds for additive mixed items with at most three valuation types when one type is a singleton, with an extension beyond additivity for goods and approximation schemes; a clean separation is shown (for additive chores with two valuation types, EFX and MMS both fail but EFX∨MMS always exists); identical additive valuations even admit the conjunction.
- **Key Innovation**: Maps the existence frontier of the EFX∨MMS disjunction — a precise boundary result for the wiki's fair-division line (EFX/MMS thread).

### Non-Existence of EFX Chore Allocations for Monotone Cost Functions with Binary Marginals
- **Authors**: —
- **Institution**: —
- **Date**: 2026-08-11
- **Link**: [2608.10572](https://arxiv.org/abs/2608.10572)
- **Abstract**: For indivisible goods, EFX existence is known for monotone functions with binary marginals; for chores the general binary-marginal case was open. This paper answers it negatively: **two counterexamples** built on the same 18-agent, 53-chore word gadget, one for binary XOS costs and one for binary supermodular costs, where a complete EFX allocation need not exist — with the main results **formally verified in Lean 4**.
- **Key Innovation**: Resolves the chores-side existence question for monotone binary-marginal costs, with machine-checked proofs — a theory result for the wiki's fair-division cluster (complements the EFX/MMS disjunction paper).

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **OPD crosses into visual agents, while RL-serve infrastructure gets cheaper** | The Aug 7–11 OPD cluster (PAST, SKALD, SR-OPSD, U-OPSD) extends to test-time GUI grounding (Reflection-Guided OPSD) and visual skill cards as privileged teacher context (SkillLens/CardDistill); the surrounding RL loop is made cheaper via MoE proxy models for failure reproduction and MISA-T's mixed-rollout KV-aware scheduling | Reflection-Guided OPSD, SkillLens, MoE Proxy, MISA-T |
| **Self-evolving agents get structural skill memory and evolution infrastructure** | SkillZip compresses accumulated skills with a coverage-guaranteed, evaluation-free objective; MERA evolves the student model behind a cost-calibrated router; MEGA distills sessions into a typed Wisdom Graph with attribution; the Co-Evolution survey taxonomizes multi-component self-evolution; GitSkills supplies a 3.8M-file population substrate | SkillZip, MERA, MEGA, Co-Evolution, GitSkills |
| **Agent memory gains a repair-after-failure paradigm** | Rollback Repair uses a typed memory-to-action graph for dependency-guided rollback and selective replay — recovery instead of just detection/deletion — complementing the wiki's memory-poisoning and memory-consistency lines | Rollback Repair |
| **Recommendation matures structurally and multi-modally** | NTCF re-interprets graph CF as curvature-aware tree CF (strictly generalizing NGCF); VisGate gates visual fusion as a measurement of when vision helps; FedCGR aligns federated cross-domain spaces over a stable semantic-ID item language | NTCF, VisGate, FedCGR |
| **TS forecasters get principled about *what* and *when*** | Right-History separates delay recovery, reporting, and functional use (correct report ≠ correct history use); REATS routes ensembles through an LLM with a reciprocal GRPO reward; ChronoSSM makes "when" first-class via joint event+timestamp autoregression | Right-History, REATS, ChronoSSM |
| **KV and efficiency meet real-world deployment constraints** | ImpactHO water-fills cache transfers across edge handover backhaul (>93.7% accuracy in 500ms); MemSpec decouples draft selection from execution on memory-constrained edge devices; OlmPool's controlled 26-model pool shows minor architecture choices compound into long-context extensibility | ImpactHO, MemSpec, OlmPool |
| **Hallucination detection goes structural, streaming, and probabilistic** | UniProbe models the full LVLM trace as a graph (GNN+ViT+GRU) for token-level detection with streaming resampling (−55% object hallucinations); Latent Critic restructures the residual stream into in-line localized critique (0.966 AUROC); ProbGuard is the first fully probabilistic guardrail, calibrated from the first ten decoding steps | UniProbe, Latent Critic, ProbGuard |
| **Fair division and game theory sharpen existence boundaries with verified proofs** | The EFX∨MMS disjunction fails to restore existence yet separates cleanly from its constituents; chores with monotone binary-marginal costs get a non-existence proof machine-checked in Lean 4; the Game of Marginal Utilities proves unique Nash equilibrium with nested segments | EFX∨MMS, EFX Chores, Game of Marginal Utilities |

---

## Key Takeaways

1. **The OPD post-training axis has fully generalized.** Aug 7–11 established OPD as the dominant post-training recipe with theory and measurement debate; this window shows it works outside text reasoning — GUI visual grounding (Reflection-Guided OPSD) and visual skill cards as privileged teacher context (SkillLens/CardDistill). Watch for OPD to become a general adaptation primitive rather than a math-specific trick.
2. **Self-evolving agents are becoming a systems discipline.** SkillZip (coverage-guaranteed skill compression), MERA (evolving the student behind a cost-calibrated router), MEGA (Wisdom Graph with attribution), and the Co-Evolution taxonomy together shift the field from "evolve one agent on one task" to maintaining durable skill memory, evolution infrastructure, and multi-component pressure — with GitSkills (3.8M SKILL.md files) as the population-level measurement substrate.
3. **Agent memory now has a repair operation, not just write/read.** Rollback Repair's dependency-guided rollback with selective replay is a first-class post-failure memory operation — a complement to the detection-only defenses the wiki already tracks (memory poisoning).
4. **Recommendation is getting structurally principled again.** NTCF's curvature-aware per-node depth (strictly generalizing NGCF), VisGate's gating-as-measurement, and FedCGR's stable semantic-ID item language for federated cross-domain rec show the field broadening beyond LLM-rankers (which this window's same-day ai-search/paper-check reports cover).
5. **Time series is turning "when" into a first-class modeling question.** ChronoSSM jointly models events and timestamps; REATS routes ensembles through an LLM; and Right-History is a warning shot: a forecaster can report the correct delay while functionally using the wrong history (92.7% of TCN cases) — accuracy alone and delay reports alone are both insufficient evaluation.
6. **Efficiency and interpretability papers keep converging on deployment realism.** ImpactHO (KV transfer under edge handover backhaul), MemSpec (edge speculative decoding), OlmPool (long-context extensibility is architecture-sensitive in ways short-context evals miss), ProbGuard (calibration-first guardrails from the first ten steps), UniProbe/Latent Critic (structural token-level hallucination detection) — all aim at constraints that standard benchmarks ignore.
7. **Fair division sharpens its boundaries, now with machine-checked proofs.** The EFX∨MMS disjunction fails to restore existence yet separates cleanly from its constituents; the chores-side binary-marginal non-existence result is verified in Lean 4. A clean theory result for the wiki's GT cluster — with zero overlap against prior digests.

> ⚠️ Note on sourcing: this digest curates the **Wed Aug 12, 2026 announced window — Aug 11 submissions (IDs ~2608.10325–2608.11208)** plus a late-Aug-10 tail (IDs 2608.10008–2608.10324), harvested from the `/list/{cat}/recent` pages (the export API was rate-limited all session). All 32 papers are **grep-verified absent from the entire wiki**, and the 15 further papers of this window that are already curated in the same-day [arXiv AI Research Search](./arxiv-ai-search.md) and [arXiv Paper Check](./arxiv-paper-check.md) are excluded. Institutions marked "(likely)" are inferred from author affiliations on the arXiv HTML pages or prior knowledge, not always the arXiv record; "—" means not identified.
