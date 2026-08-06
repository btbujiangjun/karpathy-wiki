---
title: arXiv Paper Check — AI & CTR (August 6, 2026)
type: synthesis
created: 2026-08-06
updated: 2026-08-06
sources: [arxiv-cs.AI, arxiv-cs.IR]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, agents, reasoning, rl, serving, memory, evaluation]
---

# arXiv Paper Check — AI & CTR (August 6, 2026)

> Curated from the fresh **Thu, Aug 6, 2026** announcement batch via the arXiv listing pages: cs.AI (176 new) + cs.IR (12 new). 27 papers curated. arXiv IDs in parentheses. No overlap with the Aug 4/5 paper checks or daily digests.

## 🔥 Highlights

### CTR, Recommendation & Advertising

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **Multi-Objective Ranking for Live-Streaming** (2608.04455) | Xiaoyi Gu, Julia Tavares, Eder Santana, Carlos Mendoza-Cardenas, Nikita Mishra, Saad Ali | RecSys 2026 Industry Track. Live-streaming ranking under **sparse, delayed, concurrent behaviors** (watching/chatt/following/spending): a delayed-window approach that extends feedback beyond immediate responses, a multi-model architecture combining **fresh + delayed signals**, a segment-aware targeting module that optimizes ranking scores differently by user lifecycle stage, and MMoE integration for correlated multi-task targets. |
| **DEGR** (2608.04809) | Binglei Zhao, Xuanhua Yang, Xiwei Zhao, Sulong Xu | KDD 2026 ADS Track. **Dual Exploration-Driven Generative Re-Ranking** that escapes the "fixed upstream supply" ceiling: when supply quality is low, re-ranking should prioritize exploratory exposure to preserve browsing potential. Hybrid supervised–RL paradigm guided by an **exploratory reward model** that adaptively balances immediate vs exploratory value. |
| **GOAL** (2608.04421) | Gege Chen, Ning Luo, Hao Jiang, Da Li, Wenzheng Shu, et al. | **Generative Optimization for Incentivized Advertising** under strict global constraints: formulates incentive magnitude allocation as **conditional sequence generation**, conditioned on user histories and system-level global pressure, with a hierarchical causal state encoder for local behavior + long-range dependencies (fatigue, delayed feedback). Bypasses the limits of uplift modeling and constrained RL in high-frequency, non-Markovian settings. |
| **Price of Isolation** (2608.04432) | Yuanyuan Shen, Yiren Yan, Wenjie Li, Chunhui Zhu | Two-sided A/B testing with **symmetric two-sided isolation** (matching creator/viewer submarkets) removes cross-arm interference but thins candidate catalogs. Extreme-value theory yields a **sharp tail-class dichotomy**: light/bounded tails → isolation loss vanishes as platform grows; heavy tails → loss converges to a size-independent constant. Practical guidance for when creator/cold-start isolation experiments are affordable. |
| **A/B Agent** (2608.04625) | Zhuohang Jiang, Yuxin Chen, Yongsen Pan, Zheng Hu, Wenqi Fan, Qing Li, Hongyang Wang, Jun Wang, Wenwu Ou | **Self-evolving agent for industrial A/B testing** strategy iteration: builds a hierarchical memory of business scenarios → recommendation stages → optimization objectives → experimental contexts (fixing flat-RAG retrieval mismatches), enabling cross-scenario transfer and continuous strategy refinement without expert-in-the-loop tuning. |
| **Compass** (2608.04274) | Aadit Barua, Leijie Wang, Amy X. Zhang | UIST 2026. **In-situ preference reflection** for social feeds: instead of a one-time config page, Compass surfaces lightweight reflection prompts during everyday browsing so users' feeds continuously re-align with stated (not just behavioral) preferences — attacks the "stated vs behavioral preference divergence" problem without requiring user initiative. |
| **WatchLens** (2608.04807) | Deogyong Kim, Dongha Lee | RecSys 2026. Open-source **configurable platform for online video-recommendation experiments**: modular UI/content/policy components, separate policy assignment for feed vs watch page, and a standardized logging layer that attaches policy + ranking position to every event — links playback behavior to the recommendation conditions that produced it. |

### LLM Reasoning & RL Post-Training

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **Argus** (2608.05144) | Boxiu Li, Zimo Wen, Yijia Fan, et al. | **General-purpose persistent agentic runtime** for long-horizon reasoning: Manager/Planner/Engineer/Reviewer roles execute bounded missions over durable project state; separates stable user intent from operational objectives/constraints/verification criteria; admits memories, skills, procedures and routing decisions only after **role-owned review + task-native verification**. Self-evolution via runtime state & control policy with fixed weights. Strong results across seven GPT-5.5 benchmark arenas. |
| **ABSeeker** (2608.05102) | Yijun Lu, Rui Ye, Jiajun Wang, Yuwen Du, Tian Jin, Songhua Liu, Siheng Chen | **Answer-Backtracked Credit Assignment (ABC)** for training long-horizon search agents: backtracks from the ground-truth answer to convert sparse trajectory outcomes into dense step-level supervision — rewards useful actions even in *failed* trajectories while suppressing erroneous/redundant ones (addresses the "all steps treated uniformly" flaw of SFT/RL on search trajectories). |
| **WorldCycle** (2608.04964) | Bohai Gu, Yueyang Yuan, Taiyi Wu, Dazhao Du, et al. | **Self-verifiable RL for long-horizon video world models**: the key insight is that *reversible action cycles* (a sequence composed with its inverse must analytically return to the initial state) give **annotation-free supervision on long-horizon correctness**. Optimizes a spatial-closure reward (symmetry of forward/inverse) plus a long-horizon consistency reward — attacks the "no ground-truth future state to verify drift" bottleneck in video world-model post-training. |
| **Fewer Tokens, Smaller Cache** (2608.04771) | Qiyuan Zhu, Dezhi Li, Pengyu Cheng, et al. | Reward-coordinated reasoning compression: shows KV-compression tolerance **varies along a reasoning trajectory and process reward tracks it** (deleting tokens at high-reward steps preserves accuracy far better), and that a smaller cache makes the model *generate more* tokens (partly canceling savings). Coordinates both sides under a single process-reward-driven policy to cut both tokens and cache. |
| **SPOT** (2608.04419) | Zikun Qu, Min Zhang, Mingze Kong, et al. | On-Policy Distillation improvement: standard reverse-KL ignores whether teacher uncertainty is concentrated in a few plausible tokens or spread over a long tail, and local teacher probabilities don't predict downstream success. **Sparse Probing + Outcome-calibrated targets**: an acquisition–exploration–exploitation procedure decides *where to probe* (position-level entropy/top-k capture/student–teacher agreement score) and *what to distill* (outcome-calibrated targets). |
| **Agentic RL w/ Observation-Calibrated Self-Distillation** (2608.04788) | Yi Yang, Cong Qin, Xiaodan Liu, et al. | Diagnoses a confound in On-Policy Self-Distillation (OPSD): token-level "support" reflects both the privileged replay information AND score shifts induced by the replay scaffold itself. When future observations are the privileged info, replaying them needs an extended scaffold that perturbs scores. Calibrates the distillation to attribute support to the actual privileged information. |

### Agents & Agent Evaluation

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **HiGram** (2608.05095) | Xiawei Yue, Boran Wang, Xiaoqing Zhang, Shuxin Zheng, Ziwei Zhang | **Evolving hierarchical graph memory** for LLM agents: coarse-to-fine memory architecture (replacing flat graphs that accumulate irrelevant context) with **path-level localization and rewrite** — updates propagate along the affected path instead of repeated unit-wise rewrites. |
| **EviGraph** (2608.04738) | Zhenjiang Ren, Ruiji Li, Xujing Zhang, et al. | Autonomous research agents with a **typed evidence graph** (Problem/Gap/Hypothesis/Experiment/Finding/Claim) as the *operational state* of the agent, not a post-hoc record — inspections, additions and consistency checks run on the graph, fixing the "unsupported claims and research-question↔conclusion inconsistency" failure that sequential pipelines inherit. |
| **Canary Tools** (2608.04719) | Atul Anand, Sourav Chattaraj | Diagnostic **canary tools** planted in an agent's MCP tool set, each probing one tool-selection weakness: a six-type taxonomy (semantic decoys, parameter traps, capability mirages, prerequisite blindness, temporal decoys, granularity traps). 8,640 runs × 8 models × 120 tasks; converts a single "wrong tool" outcome into a multi-dimensional reasoning profile. |
| **SkillSV** (2608.04562) | Tao Li, Junfeng Liu, Qinghua Zhao, et al. | **Structure-aware Shapley valuation of agent skills**: assigns credit to internal skill units (rules, examples, scripts, heuristics) under a fixed agent — compiles skills into units/dependencies/hierarchy so only *valid counterfactual* skills are evaluated, uses paired deletion + length-neutral padding to separate content value from context cost. |
| **Breadcrumbing Search Agents** (2608.04565) | Xuebin Li, Hanqing Zhao, Siyuan Liang, et al. | Security: the **search/page observation channel is a fragile boundary** — beyond single-page injection, a mediated search interface can repeatedly steer how the agent gathers evidence and forms its final answer. Appending just **one controlled result per query** can substantially redirect long-horizon search agents (beyond static injection attacks). |
| **ContextWeave** (2608.04830) | Bo Wang, Yuqian Yao, Enxi Wang, et al. | Longitudinal **real-world workflow benchmark** for agent memory: reconstructs privacy-preserved multi-month workflows of 14 participants into 1,005 executable tasks (568 core) with containerized environments + rubrics; measures whether *recalled experience improves downstream performance*, with diagnostics for relevance/continuity/solvability/misleading-recall robustness. |
| **OneDayAgent** (2608.05013) | Jingsheng Zheng, Xinyuan Fang, Jintian Zhang, et al. | Long-horizon harness that jointly manages **goal drift, state loss, and context overflow** for open-ended cross-environment requests: decomposes into bounded subtasks, maintains execution memory under context pressure, verifies/repairs the final deliverable; evaluated on AgentIF-OneDay (104 tasks). |
| **MatrAIx** (2608.04205) | Xiaomin Li, Yuexing Hao, Jianheng Hou, et al. | **Population-scale simulated-user evaluation**: Persona 8B holds 8.3B persona records (1,290 categorical dimensions; ~1M released coreset: 599,847 human-grounded + 400K synthetic); four Playground environments simulate diverse users evaluating AI systems/products — scalable human-diversity for offline eval. |

### Serving, Memory & Efficiency

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **Spend Bits Where Queries Look** (2608.04074) | Samuel Fernández-Menduiña, Amir Ziashahabi, Eduardo Pavez, Antonio Ortega, Salman Avestimehr | **KV-cache vector quantization that preserves attention products**: derives the orthogonal transform from a distortion criterion (vs data-oblivious/Hadamard baselines that equalize variance rather than compact energy) and replaces fixed-width scalar quantizers with rate-optimal low-bit schemes. Targets the bandwidth-bound long-context decode regime at fixed per-token bit counts. |
| **AFD-Ledger** (2608.04502) | Chengyu Qiu, Xiao Fu, Fengcun Li, et al. | Offline **analytical provisioning for Attention–FFN Disaggregation (AFD)** vs collocated MoE serving: jointly optimizes hardware assignment + deployment organization under a TPOT SLO and hardware budget, answering "does AFD actually beat the best collocated deployment?" without exhaustive provisioning search. |
| **MESH** (2608.04407) | Masato Fujitake | Memory-efficient MoE training: shows memory-light Sinkhorn/matrix optimizers that work for dense matrices **fail on routed MoE expert matrices** (gradients are conditional, temporally varying — Sinkhorn's stateless normalization degrades loss 3.58→3.83 at 110M scale). MESH adds a **hidden momentum** term through the gradient-buffer lifecycle, restoring temporal first-moment signal while keeping optimizer state low. |

### Evaluation, Safety & Interpretability

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **Item Response Theory for AI Safety** (2608.05086) | Joshua Fonseca Rivera, Neil Shah, David Demitri Africa, Konstantinos Voudouris (UK AI Security Institute) | Fits IRT models to **8 safety benchmarks × 192 LLMs** (largest psychometric analysis of LLM safety to date): three interpretable latent factors (refusal strictness, truthfulness, contextual harm) explain most cross-model variance; psychometrically selected items recover full benchmark signal — an answer to "benchmarks duplicate/correlate and models sandbag." |
| **CoT Monitoring Unreliable in Implicit-Influence Settings** (2608.04735) | Agatha Duzan, Asa Cooper Stickland | First benchmark comparing **CoT monitorability under explicit-influence** (prompt instructs hiding) vs **implicit-influence** (no instruction; behavior shaped by task context, e.g., a biasing aside in a hiring rating). When the nudge is a casual aside, monitoring is unreliable — a gap in frontier-model CoT-safety evaluations. |
| **SciCode-Verified** (2608.04975) | Sihan Hu, Lyuhan Huang, Youjin Deng, Kun Chen | Re-audit of the SciCode scientific-coding benchmark: all 65 problems audited → **263 defects, 192 of which (in 91% of problems) wrongly reject correct solutions** (non-reproducible golds, over-tight tolerances, self-contradictory specs). Argues SciCode's 2026 plateau (~60%) reflects benchmark defects, not model ceiling — a corrective to benchmark-vs-model confounds. |
| **Inference Backend as Behavioral Confound** (2608.04714) | Shahed Masoudian, Passant Shafaei, Monorama Swain, Markus Schedl | Fully-crossed study (3 instruction-tuned models × 5 inference frameworks × 6 benchmarks × 4 generation modes): the **inference backend (HF/vLLM/Ollama) is a non-negligible factor** — even under greedy decoding, backend choice significantly changes scores, structurally and model-dependently. Benchmarks should disclose framework + version. |

## 📊 Summary Statistics

- **Total curated**: 27 papers (Thu, Aug 6, 2026 announcement batch; cs.AI 176 new / cs.IR 12 new; no overlap with Aug 4/5 paper checks or daily digests)
- **CTR, Recommendation & Advertising**: 7 papers
- **LLM Reasoning & RL Post-Training**: 6 papers
- **Agents & Agent Evaluation**: 8 papers
- **Serving, Memory & Efficiency**: 3 papers
- **Evaluation, Safety & Interpretability**: 4 papers

## 🔑 Key Trends

1. **Ads/rec experimentation infrastructure becomes a research topic.** Price of Isolation gives sharp extreme-value asymptotics for when two-sided isolation A/B tests are affordable; A/B Agent and WatchLens turn the experiment lifecycle itself into an agentic/pluggable artifact. The question is shifting from "build a better ranker" to "know when and how to test it."
2. **Generative ranking matures on the serving/constraint side.** GOAL generates incentive magnitudes under global constraints; DEGR uses exploratory reward models to escape fixed-supply ceilings in re-ranking; the live-streaming paper jointly models fresh + delayed signals with segment-aware targeting. Generative rec is moving from architecture novelty to constraint-aware optimization.
3. **A hot cluster on On-Policy Distillation credit assignment.** SPOT, Agentic-RL observation-calibrated self-distillation, and (from yesterday) SFT-vs-RL coexistence all attack the same problem: dense token-level supervision from privileged replay views is confounded and needs calibration/probing. Post-training theory continues to converge across recommenders and LLMs.
4. **Long-horizon agent memory is now benchmarked by workflow outcomes, not retrieval.** ContextWeave (1,005 executable tasks from real multi-month workflows), HiGram (path-level hierarchical graph memory), OneDayAgent, and MemoryCPT evaluate whether recalled experience improves *downstream task performance* — memory is increasingly judged by its effect on the agent, not by recall metrics.
5. **Verification-first thinking is spreading.** WorldCycle gets annotation-free long-horizon supervision from reversible action cycles; Argus admits memory/skills only after role-owned review + task-native verification; EviGraph makes evidence-consistency the agent's operational state; SciCode-Verified and the inference-backend study push benchmark-level verification rigor.
6. **Safety evaluation gets psychometric and influence-aware.** IRT factors (refusal strictness, truthfulness, contextual harm) decompose 192-model safety variance; CoT monitoring is shown unreliable under implicit influence; Breadcrumbing shows search-agent poisoning works through the observation channel itself.

## Related Pages
- [arXiv Paper Check — AI & CTR (August 4, 2026)](../2026-08-04/arxiv-paper-check.md) — prior digest (GRACE, HRPO, Exp-RSFT, Tevatron 3.0, AOSpec, etc.)
- [arXiv AI Research Scan (August 5, 2026)](../2026-08-05/arxiv-ai-search.md) — prior scan
- [arXiv Daily Digest (August 5, 2026)](../2026-08-05/arxiv-daily.md) — prior daily digest
