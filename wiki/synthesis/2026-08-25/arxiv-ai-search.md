---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-25)"
type: synthesis
created: 2026-08-25
updated: 2026-08-25
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, rag, world-models, daily-digest]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-25 · Scope: papers **not yet covered anywhere in the wiki** (every arXiv ID below grep-verified absent from all existing pages — including the same-day sibling digests [arxiv-daily](arxiv-daily.md) and [game-rl-daily (08-24)](../2026-08-24/game-rl-daily.md), which absorbed 13 + 1 candidates respectively; zero overlap). Fresh window = Mon Aug 24 announcement wave (Fri Aug 21 late – Mon Aug 24 submissions, IDs ~2608.214xx–2608.235xx), retrieved via arXiv API across cs.IR / cs.CL / cs.AI / cs.LG / cs.GT with topic-keyword sweeps (recommendation, CTR/click-through/advertising, sequential/user-behavior, games, LLM/agents). **17 new papers below across 5 categories.**
>
> Affiliations marked *(stated)* come from paper comments/front matter; *(inferred)* = deduced from author identities; otherwise "not stated". **Advertising note:** no advertising-specific paper survived dedup this window — closest ads-adjacent entries are the carousel metric reformulation (1.3), the industrial shopping simulator (1.4), and the multivector retrieval separation (2.1).

---

## ① Recommendation & Sequential Modeling (4)

### 1.1 A Dual-Expert Strategy Integrating LLMs to Mitigate Negative Transfer in Cross-Domain Sequential Recommendation (DuELRec)

| Field | Detail |
|-------|--------|
| **Authors** | Hyeongjun Yun, Kihyuk Song, Jaegul Choo, Chung Park |
| **Institution** | KAIST (inferred: Choo / Park groups) · CIKM 2026 (stated) |
| **Abstract** | Cross-domain sequential recommendation (CDSR) predicts next interactions from sequences spanning multiple domains. LLMRec-style approaches fine-tune LLMs on textual renderings of cross-domain histories but model token-level autoregressive patterns while missing item-level collaborative signals — a semantic misalignment causing *negative transfer* across domains. DuELRec adds an item-aware attention transformation that aggregates textual subtokens into item-level representations under block-level attention masking, then runs two experts: a single-domain expert restricting attention within-domain and a cross-domain expert allowing it everywhere, fused adaptively by a gating mechanism per input. |
| **Key innovations** | Names and targets the negative-transfer failure mode of LLM-based CDSR; dual-expert design makes cross-domain transfer opt-in via gating rather than always-on; block masking aligns aggregation granularity with collaborative signals. |
| **arXiv** | [2608.23131](https://arxiv.org/abs/2608.23131) · cs.IR |
| **Why it matters** | Another instance of the wiki-tracked pattern "LLM rec needs collaborative-signal scaffolding"; here the fix is architectural (gated experts), complementing profiling-based fixes like CAIRO ([2608.20801](../2026-08-23/arxiv-ai-search.md)). |

### 1.2 Enhancing Group Recommendation with Memory-Augmented Reasoning in LLM Agent (AGR)

| Field | Detail |
|-------|--------|
| **Authors** | Qimeng Niu, Bowen Hao, Zixuan Zhang, Shuyu Qu, Hongzhi Yin |
| **Institution** | Heilongjiang University + University of Queensland (inferred: Yin is UQ) |
| **Abstract** | Group recommendation requires modeling dynamic preference evolution and explaining consensus formation. Existing LLM methods treat interaction history as fixed text, ignoring preference drift and lacking explicit group decision dynamics. AGR pairs a Memory Module — a token-based hash table managing group/user records with insertion, update, retrieval, forgetting, and profile summarization — with a Reasoning Module performing multi-step inference: Group Interests Collection → Group Consensus Refinement → Multi-dimensional Evaluation → Explainable Recommendation Generation. |
| **Key innovations** | Token-hash-table memory with explicit forgetting and rolling profile summarization for evolving group state; consensus formation decomposed into inspectable reasoning steps instead of black-box inference. |
| **arXiv** | [2608.21939](https://arxiv.org/abs/2608.21939) · cs.IR |
| **Why it matters** | Extends memory-augmented-agent rec from single-user to multi-party preference aggregation; the consensus-refinement step matters because group choice ≠ averaged individual choice. |

### 1.3 Revisiting N2DCG: An Empirically Grounded Reformulation of Carousel Recommendation Evaluation

| Field | Detail |
|-------|--------|
| **Authors** | Jingwei Kang, Santiago de Leon-Martinez, Maarten de Rijke, Harrie Oosterhuis |
| **Institution** | Uber + University of Amsterdam (inferred: de Rijke / Oosterhuis UvA; industrial carousel data) |
| **Abstract** | Carousels dominate video/music streaming UIs, but N2DCG — the NDCG adaptation for two-dimensional layouts — borrows unverified assumptions from single-list web search. Two flaws identified: its ideal ranking violates carousel placement constraints, and its discount function does not match observed browsing behavior. The reformulation normalizes by constraint-respecting ideal layouts and uses a discount calibrated on empirical examination data, validated on real eye-tracking data and simulated layout comparisons. |
| **Key innovations** | First empirically grounded discount model for carousel layouts; constraint-valid normalization; validated against eye-tracking rather than synthetic assumptions. |
| **arXiv** | [2608.21877](https://arxiv.org/abs/2608.21877) · cs.IR, cs.HC |
| **Why it matters** | Metrics shape what recommenders optimize; listwise metrics silently mis-rank policies on carousel surfaces. Companion theory paper on offline/off-policy evaluation for carousels [2608.22022] was claimed by sibling arxiv-daily. |

### 1.4 Towards Faithful Simulation of Human Shopping Behavior (RecVerse)

| Field | Detail |
|-------|--------|
| **Authors** | Jiakai Tang, Yan Mi, Jing Yu, Yang Zhang, See-Kiong Ng, Qi Cao, Fei Sun, Xu Chen, Wen Chen, Jian Wu, Han Zhu, Bo Zheng |
| **Institution** | Alibaba + National University of Singapore + Renmin University (inferred: Sun/Cao/Chen RUC; Zhu/Zheng/Wu Alibaba ads stack) |
| **Abstract** | Realistic user simulators underpin offline evaluation and RL for e-commerce, but current LLM/VLM simulators fail on two axes: (i) *Memory* — sessions span dozens of pages; agents drop long-range observation history or concatenate everything into the context window; (ii) *Optimization* — step-level imitation yields unrealistic sessions (over-exploration or passivity) that per-step rewards cannot detect or correct. RecVerse is a GUI-grounded agent perceiving screenshots with cognitive-inspired hierarchical memory — Working Memory (short-term focus), Episodic Memory (in-session traces), Preference Memory (long-term) — plus session-level objectives supervising whole-trajectory realism. |
| **Key innovations** | Hierarchical memory mapped onto cognitive stages for long GUI sessions; trajectory-level (not step-level) supervision targeting session-realism failure modes; built against an industrial-scale e-commerce environment. |
| **arXiv** | [2608.20707](https://arxiv.org/abs/2608.20707) · cs.IR |
| **Why it matters** | Faithful user simulators are becoming the standard substrate for rec/ads policy evaluation without live traffic — same trajectory-vs-step supervision debate as agentic RL, now applied to shopping. |

---

## ② Retrieval / IR Infrastructure (3)

### 2.1 Retrieval Needs Multivectors: An Exponential Separation

| Field | Detail |
|-------|--------|
| **Authors** | Mihir Agarwal, Viraj Agrawal, Sabyasachi Basu, Ankit Garg, Kirankumar Shiragur |
| **Institution** | Google Research + Stanford (inferred: Garg/Basu/Agrawal Google; Shiragur Stanford) |
| **Abstract** | Following LIMIT-style benchmarks and Jayaram's score-approximation analysis, this work gives the first *explicit* family of query/document sets where any single-vector embedding that ranks all relevant above irrelevant documents requires exponential size, while polynomial-size multi-vector embeddings suffice. The separation is for the ranking task itself, not numerical score approximation. The authors release ANDOR, a benchmark instantiating AND/OR-compositional relevance; SOTA single-vector embedders fail zero-shot and improve only marginally after fine-tuning. |
| **Key innovations** | First exponential expressiveness separation (single- vs multi-vector) for ranking as such; constructive hard family + matching practical benchmark (ANDOR). |
| **arXiv** | [2608.21494](https://arxiv.org/abs/2608.21494) · cs.IR, cs.DB, cs.LG |
| **Why it matters** | Theory-level bedrock for the industry drift toward multi-vector/late-interaction retrieval — relevant to ads matching and search alike: some relevance structures are provably not encodable in one vector per doc. |

### 2.2 The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search

| Field | Detail |
|-------|--------|
| **Authors** | Peiyang Liu, Xi Wang, Di Liang, Wei Ye |
| **Institution** | Peking University + industry collaborators (inferred: Wei Ye PKU) |
| **Abstract** | RAG shifting toward portfolio generation is blocked by flawed measurement of evidence utilization and suboptimal context budget allocation. The paper exposes a "diagnostic illusion": standard relevance proxies fail catastrophically on hard negatives, replaced by an efficient causal leave-one-out probe isolating generative reliance. In a deconfounded factorial grid it proves monolithic context widening is an architectural trap penalized by relevance decay; instead, iterative allocation across multiple sequential generations drives portfolio recall gains of 16.7–20.5 absolute points, scaling to 32B models. Unified into a closed-loop submodular scheduler with an attribution-steered contrastive decoder overriding LLM attention inertia. |
| **Key innovations** | Causal (leave-one-out) evidence-usage probe replacing correlational relevance proxies; proof that wider-context-at-once is dominated by sequential multi-generation allocation; deployable closed-loop scheduler. |
| **arXiv** | [2608.23252](https://arxiv.org/abs/2608.23252) · cs.LG, cs.CL, cs.IR |
| **Why it matters** | Directly actionable for generative-search/rec products: how you spend a fixed context budget matters more than how big it is. |

### 2.3 RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation (position paper)

| Field | Detail |
|-------|--------|
| **Authors** | Kyle Wild, Yusuke Takahashi, Asako Uraki |
| **Institution** | Not stated (independent/startup authors) |
| **Abstract** | Production RAG re-derives the meaning of raw corpus text on every query and throws the work away — the modern equivalent of a full-table scan, with inference spend rising because context volume grows faster than token prices fall. Proposes ingest-time semantic compilation (ISC): compile corpus meaning at write time into a queryable substrate with incrementally maintained embeddings plus atomic claims whose provenance is validated at compile time, treated as a first-class database object with DDL, maintenance/migration contracts, and cost model. Evidence: substrate upkeep scales with change rather than corpus size (incremental updates ~33.7× cheaper). |
| **Key innovations** | Reframes RAG infrastructure as a database problem ("index your corpus semantics"); atomic-claims layer with compile-time provenance validation; explicit cost model showing change-proportional upkeep. |
| **arXiv** | [2608.20845](https://arxiv.org/abs/2608.20845) · cs.AI, cs.DB, cs.IR · position paper (single-source, ideas not benchmarked head-to-head) |
| **Why it matters** | Converges with wiki-tracked "knowledge base as first-class artifact" themes ([[../../concepts/llm-knowledge-bases|LLM Knowledge Bases]]): the corpus itself becomes engineered, versioned infrastructure rather than raw text. |

---

## ③ Agents & Agentic RL (4)

### 3.1 AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces

| Field | Detail |
|-------|--------|
| **Authors** | Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang |
| **Institution** | Microsoft Research + KAIST + Kyungpook NU (inferred: aka.ms project link; Lin/Rajmohan/Zhang MSR) |
| **Abstract** | LLM agents fail on long-horizon tasks when small local failures compound, and harness design (prompts, tool configs, control logic) remains manual. AutoSaddler formulates harness improvement as offline learning: failure-trace diagnosis → structured patch generation treating the harness as code → validation-based update selection over mini-batches of execution traces. On GAIA2, SWE-Bench Pro, and Terminal-Bench 2.0 it gains +9.0 / +9.6 / +10.0 points over base harnesses. Ablations: deep debugging beats shallow reflection; targeted modification beats unconstrained editing; generalization-aware selection is essential. |
| **Key innovations** | Treats the harness itself as the learnable artifact ("harness-as-code" patches with durable updates); fully automatic loop from production-style failure traces to validated harness upgrades. |
| **arXiv** | [2608.23041](https://arxiv.org/abs/2608.23041) · cs.AI/CL/LG/MA/SE |
| **Why it matters** | Extends the wiki-tracked agentic-engineering thesis ([[../../concepts/agentic-engineering|Agentic Engineering]], [[../../concepts/claws|Claws]]): harness engineering is becoming automated — the scaffold now optimizes itself from traces. Compare HSI self-evolution ([2608.08466](../2026-08-23/game-rl-daily.md)). |

### 3.2 Prime Agent: A Self-Improving RLM Harness

| Field | Detail |
|-------|--------|
| **Authors** | Seth Karten, Alex L. Zhang, Kevin Thomas, Sebastian Müller, Elie Bakouch, Daniel Auras, Mika Senghaas, Fares Obeid, Konstantin Dunas, Johannes Hagemann, Sami Jaghouar et al. |
| **Institution** | Prime Intellect (stated: github.com/PrimeIntellect-ai) |
| **Abstract** | Open-source harness for long-horizon evaluation and coding-agent workflows built on the Recursive Language Model abstraction: a persistent IPython REPL does programmatic context processing and test-time compute; Continual Harness preserves histories, memories, skills, prompts, and subagent specs across trajectories; recursive subagents coordinate via direct agent-to-agent communication; an Agents View lets humans inspect daemon-backed sessions. Standardizes execution, recovery, verification, resource accounting while leaving strategy to the model. Raises ARC-AGI-3 RHAE Best@1 from 30% to 95.5%; matches or exceeds native/popular harnesses on long-context coding, GPU-kernel generation, emulator construction, autonomous nanoGPT speedruns. |
| **Key innovations** | RLM pattern (model writes code to manage its own context) + persistent cross-trajectory memory/skills; explicit design goal that harness failures not masquerade as model failures — measurement moves toward true model capability. |
| **arXiv** | [2608.23552](https://arxiv.org/abs/2608.23552) · cs.AI/CL/SE |
| **Why it matters** | The 30%→95.5% swing from harness alone quantifies how much "model capability" numbers are actually harness artifacts — directly relevant to [[../../concepts/verification-gap|evaluation validity]] debates tracked in this wiki. |

### 3.3 Agent-G²: Gaussian Guidance for Agentic Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Zixuan Wang, Yanrui Miao, Zhengxi Lu, Teng Pan, Yiwen Qiu, Hongxing Li, Peng Qiu, Ruiqing Zhang, Yongliang Shen |
| **Institution** | Zhejiang University (stated-ish: ZJU-REAL GitHub org) |
| **Abstract** | Hint-based RL for sparse-reward agentic tasks keeps a prefix of an expert trajectory before each rollout; effectiveness hinges on guidance depth. Existing methods treat depth as deterministic — shared schedules ignore per-task heterogeneity; per-sample probing costs extra rollouts. Finding: useful guidance occupies a *band* of depths with approximately Gaussian informativeness around its center. Agent-G² draws depth per task from a Gaussian whose center (global baseline + per-cluster difficulty) and spread (within-cluster variance) are estimated online from rollouts already collected — no probe rollouts or learned predictor. Outperforms strongest hint-based baselines on ALFWorld and WebShop with Qwen2.5-1.5B/7B-Instruct. |
| **Key innovations** | Reframes expert-hint injection from point estimate to distribution; zero-extra-rollout online estimation reusing policy-optimization samples; cluster-conditioned center/spread. |
| **arXiv** | [2608.23318](https://arxiv.org/abs/2608.23318) · cs.AI/CL |
| **Why it matters** | Cheap, principled fix for reward sparsity in web-agent RL — the guidance-band insight likely transfers to any curriculum/hint scheme ([[../../methods/reinforcement-learning|RL]]). |

### 3.4 The Compaction Cliff in Long-Running AI Agent Memory

| Field | Detail |
|-------|--------|
| **Authors** | Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer |
| **Institution** | University of Passau (inferred: Granitzer/Mitrovic group) |
| **Abstract** | When an agent's context budget overflows, safety rules and episodic logs get summarized at the same rate — but only rules need exact wording to stay enforceable. Measured on 20 production agent configurations: Claude Code's /compact on Sonnet 4.6 preserves 53% of safety rules after one compaction round, 10% after five — the "Compaction Cliff". Fix: Knowledge Triage classifies each knowledge-base line by type and routes it through per-type retention policies via three deterministic operators — TypeCompact (per-type-fidelity rewriting), TypeDecompose (partition oversized topics, replicating in-scope rules), TypeRetrieve (external storage fetch with rules pinned ahead of relevance). TypeCompact preserves 2–4× more safety rules than the strongest single-shot compactor at every ratio, 96% recall over five rounds. |
| **Key innovations** | First quantitative characterization of rule-decay under context compaction; type-aware retention as a deterministic, auditable operator set rather than another LLM summarizer. |
| **arXiv** | [2608.22752](https://arxiv.org/abs/2608.22752) · cs.AI/IR |
| **Why it matters** | Safety-critical and practical: anyone running long-lived coding agents inherits this cliff. Connects to memory-framework skepticism already logged in [MemTrapBench](../2026-08-23/arxiv-paper-check.md) — uniform summarization is a liability, not a feature. |

---

## ④ LLM Training, Safety & Efficiency (4)

### 4.1 Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM Policy Optimization (ERPO)

| Field | Detail |
|-------|--------|
| **Authors** | Xianlei Zhou, Xiangdi Meng, Yu He, Tianyu Qi, Shuyan Guan, Xianli Zhang, Jian Zhang, Xin Li, Qika Lin, Jun Liu |
| **Institution** | Not stated (inferred, tentative: Jun Liu / Xin Li groups — Northwestern Polytechnical University) · EMNLP 2026 main (stated) |
| **Abstract** | LLM policy optimization faces a stability–exploration trade-off mediated by action-side Policy-KL: keep it and you constrain response behavior while consuming exploration budget; drop it and drift goes uncontrolled. ERPO moves regularization to the *input* side — a Query-KL term bounds the shift of the training-query distribution from its pre-RL reference, plus a reference-derived per-query weight biasing updates toward typical queries. The QKL gradient flows strictly through query likelihood, exerting no direct pressure on the response distribution, so exploration is preserved. Plugs into GRPO/PPO/REINFORCE pipelines. |
| **Key innovations** | Regularizes the environment (query distribution) instead of the policy; gradient-isolation argument showing why input-side KL does not suppress exploration; drop-in for existing PO algorithms. |
| **arXiv** | [2608.23311](https://arxiv.org/abs/2608.23311) · cs.CL |

### 4.2 Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty (SDP)

| Field | Detail |
|-------|--------|
| **Authors** | Yipeng Zhao, Qishun Yang, Shenzhe Zhu, Shu Yang, Di Wang |
| **Institution** | KAUST (inferred: Di Wang / Shu Yang group) |
| **Abstract** | Fine-tuning on purely benign reasoning data (math, code, CoT traces) can induce harmful behaviors — Reasoning-Induced Misalignment (RIM). Prior work blamed neuron-level entanglement without characterizing representation geometry or offering a training-time fix. This paper extracts two activation-space directions — one encoding reasoning ability, one safety behavior — and shows they are coupled: fine-tuning that improves reasoning shifts safety representations, with larger prompt-level shifts predicting larger degradation; CKA ratios and probes localize the safety-decision layers. SDP penalizes movement along the learned safety direction during reasoning fine-tuning. Cross-architecture/scale/dataset checks show RIM does not always emerge. |
| **Key innovations** | Geometric account of RIM (coupled reasoning/safety directions); training-time penalty rather than post-hoc filtering; honest boundary conditions on when RIM appears. |
| **arXiv** | [2608.23497](https://arxiv.org/abs/2608.23497) · cs.AI/CL |

### 4.3 Accelerating Diffusion Language Models via Structured Suffix Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Zifeng Cheng, Keda Li, Zhiwei Jiang, Cong Wang, Fei Shen, Qing Gu |
| **Institution** | Nanjing University of Science and Technology + collaborators (inferred: Jiang/Gu NJUST) |
| **Abstract** | Diffusion LMs denoise many tokens per step, but each step must interact with all suffix tokens. Prior accelerations keep only a local suffix window and re-initialize suffix tokens identically at each timestep. This work splits the suffix into local/middle/tail regions retaining different token counts by structural role, and injects previous-step decoding results into current suffix representations so tokens carry evolving denoising state across steps. Training-free and orthogonal to parallel-decoding and other acceleration techniques. |
| **Key innovations** | Region-aware suffix pruning (heterogeneous roles acknowledged); cross-step suffix memory without retraining; compositional with existing DLM speedups. |
| **arXiv** | [2608.23167](https://arxiv.org/abs/2608.23167) · cs.CL |
| **Why it matters** | Keeps diffusion-LM inference competitive as an alternative to autoregressive decoding — relevant to wiki pages on diffusion-LM reasoning ([LaDiR](../../papers/llm-training/ladir-diffusion-reasoning.md), [DiLaDiff](../../papers/llm-training/diladiff-diffusion-lm.md)). |

### 4.4 Apodex 1.1: Scaling Agentic Intelligence for Complex Work

| Field | Detail |
|-------|--------|
| **Authors** | Apodex Team (~70 authors, anonymized first names) |
| **Institution** | Apodex (company tech report; affiliation opaque, single-source) |
| **Abstract** | Introduces "working capability": sustained, verifiable progress toward real-world objectives via files, information sources, executable code, state maintenance, failure recovery. Scales along two axes — Environment Scaling (diversity + verifiability of executable file/search/code environments) and Agentic Coordination Scaling (task decomposition, parallel delegation, asynchronous result integration, replanning) — with a shared execution harness and AgentOS maintaining task state/provenance across tools and agents. Reaches leading performance band across professional work, finance, science, math, coding, search with a substantially smaller model than frontier systems; a 35B Mini variant retains strong capability for local deployment. |
| **Key innovations** | Names two scaling dimensions beyond parameter count for agency; coordination-as-training-signal (delegation/integration/replanning traces turned into reliable behavior); small-model competitiveness claim. |
| **arXiv** | [2608.23283](https://arxiv.org/abs/2608.23283) · cs.AI/CL/LG · treat benchmarks skeptically until independently reproduced (single-source industry report) |
| **Why it matters** | If "environment scaling + coordination scaling" holds up, it extends [[../../concepts/agentic-models|capability scaling]] past weights+data — same direction as Prime Agent's harness findings (3.2). |

---

## ⑤ Games & World Models (2)

### 5.1 ReWorld: An Interactive World Model with Long-Horizon Memory

| Field | Detail |
|-------|--------|
| **Authors** | Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang, Tianshuo Xu, Yihua Du, Wei Wang, Tianyi Gui, Lianghua Huang, Yingcong Chen |
| **Institution** | HKUST(GZ) + Alibaba (inferred: Yingcong Chen HKUST(GZ); Lianghua Huang Alibaba video-gen) |
| **Abstract** | An interactive world model must follow user actions, remember shown places, and stream in real time — but control wants a short horizon while memory wants an unbounded one. ReWorld separates the two in training and bounds them at inference: mixed per-head attention windows keep most heads on the recent past while a few global heads attend over full history; random head routing prevents capability-head lock-in; random chunk dropping makes sparse histories in-distribution. At inference, the whole past lives under a fixed budget — bounded KV cache backed by a pose-indexed landmark bank retrieving landmarks nearest the current pose. A metric-scale-aligned data engine unifies eight sources (Unreal fly-throughs, game roaming, real footage) on one physical action scale; palindrome trajectories supply revisit evidence for memory training. Distribution-matching distillation into a LoRA compresses sampling to four steps. |
| **Key innovations** | Structural decoupling of control horizon vs memory horizon via head-level attention roles; pose-indexed landmark memory as a bounded KV substitute; metric-scale-aligned multi-source data engine solving cross-source action consistency. |
| **arXiv** | [2608.23565](https://arxiv.org/abs/2608.23565) · cs.AI · [project page](https://zhifeichen097.github.io/ReWorld/) |
| **Why it matters** | Adds a memory mechanism distinct from the world-model line already tracked ([ForgeWM](../2026-08-21/game-rl-daily.md), [Marionette](../2026-08-23/game-rl-daily.md), [Alaya-EVOKE](../2026-08-14/game-rl-daily.md)): retrieval over spatial landmarks rather than externalized state stores. |

### 5.2 Equilibrium in Multi-Agent Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Maurizio D'Andrea, Bar Light |
| **Institution** | University of Liverpool (inferred: Bar Light) |
| **Abstract** | Standard stochastic-game solution concepts (Markov perfect equilibrium, Markov CCE) are computationally hard, so decentralized RL should not be expected to converge to them. Introduces Markov Bayes coarse correlated equilibrium (MBCCE): a distribution over states and stationary policy profiles where, after observing the state but before seeing her recommended action, no player gains by deviating on the current action while the sampled profile governs subsequent play. MBCCE retains key CCE properties from normal-form games. Defines adaptive Markov coarse regret (AMCR) and proves vanishing AMCR implies every accumulation point of the empirical play distribution is an MBCCE; achieving AMCR reduces to two standard no-regret subroutines. |
| **Key innovations** | New solution concept matching what decentralized no-regret learners actually generate; regret notion with convergence guarantee; constructive reduction to known subroutine classes. |
| **arXiv** | [2608.22840](https://arxiv.org/abs/2608.22840) · cs.GT |
| **Why it matters** | Theory anchor for what self-play/multi-agent training populations actually converge to — complements empirically tracked MARL instability results ([unified DQL instability](../2026-08-21/game-rl-daily.md)). |

---

## Cross-cutting observations

1. **Harnesses are becoming first-class learnable artifacts** (AutoSaddler, Prime Agent, Apodex's AgentOS). The scaffold around a frozen model — prompts, tools, memory, recovery logic — is now itself optimized from execution traces. Three independent groups quantify harness-vs-model gaps of tens of points.
2. **Memory under pressure is this week's recurring failure mode**: Compaction Cliff shows uniform summarization silently destroys enforceable rules; RecVerse and AGR both answer with typed/hierarchical memory instead of flat context stuffing; ReWorld bounds memory with pose-indexed retrieval.
3. **Retrieval theory catches up with practice**: the multivector exponential separation + ANDOR benchmark gives formal backing to late-interaction adoption; the context-allocation laws show budget *allocation across generations* beats widening a single context.
4. **Evaluation validity keeps eroding**: N2DCG's borrowed web-search assumptions mis-measure carousels; Prime Agent shows harness artifacts dominate reported capability; RIM analysis warns reasoning fine-tuning shifts safety geometry even on benign data.

## Methodology

- 8 arXiv API queries (`export.arxiv.org`), sorted by submission date: cs.IR sweep (60), "click-through rate" (30), "CTR prediction" (20), advertising∩cs.IR (30), "sequential recommendation" (20), cs.CL sweep (60), cs.GT (20), game∩cs.AI (30) → 247 unique papers, 131 in fresh window (published ≥ 2026-08-21).
- Shortlist of 32 topic-relevant candidates grep-verified against all of `wiki/`: 13 claimed by same-day sibling [arxiv-daily](arxiv-daily.md), 1 by [game-rl-daily 08-24](../2026-08-24/game-rl-daily.md), plus ~1 more absorbed there → 17 verified-new papers reported.
- Temp fetch files cached under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv0825/` and deleted after use (per temp-file constraint).

*All affiliations above are stated only when the paper says so; "(inferred)" entries are deduced from author identities and remain tentative.*
