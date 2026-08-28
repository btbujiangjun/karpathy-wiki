---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-28)"
type: synthesis
created: 2026-08-28
updated: 2026-08-28
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, world-models, marketplace, rl, retrieval, daily-digest]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-28 · Scope: papers **not yet covered anywhere in the wiki** (every arXiv ID below grep-verified absent from `wiki/` — including same-day sibling [arxiv-daily](arxiv-daily.md) which claimed IDs ~2608.26480–2608.27454 across cs.IR/cs.AI/cs.LG; zero overlap). Coverage window: Thu Aug 20 – Thu Aug 27 submission waves (IDs ~2608.20xxx–2608.27xxx), retrieved via arXiv API across cs.IR / cs.CL / cs.AI / cs.LG / cs.GT / cs.MA / cs.CR / cs.HC with topic-keyword sweeps (recommendation, advertising/CTR, sequential/user-behavior, games, world models, agents, RL). **21 new papers below across 6 categories.**
>
> Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities / GitHub / release notes; otherwise "not stated". **Advertising note:** pure CTR/advertising papers were mostly absorbed by the sibling daily (LAMA token-level auction, MaskRec, Stageboost); the two closest survivors here are market-mechanism papers (2.1 AgentLance, 2.2 tacit collusion) plus the industrial e-commerce entries in §①.

---

## ① Recommendation & E-commerce (4)

### 1.1 Beyond Observed Auxiliary Relations: Environment-Conditioned Modeling for Multi-Behavior Recommendation (BOAR)

| Field | Detail |
|-------|--------|
| **Authors** | Seunghan Lee, Hyunsik Yoo, Jian Kang, Susik Yoon, SeongKu Kang |
| **Institution** | KAIST / RPI / NAVER (inferred: Yoon & Kang are KAIST, Kang RPI) |
| **Abstract** | Multi-behavior recommendation (MBR) uses auxiliary signals (clicks, add-to-cart) to improve target-behavior prediction (purchases). GNN-based MBR baselines suffer two fundamental problems inherent to auxiliary behaviors: *(missing)* items without auxiliary observations get no signal, and *(unreliable)*, auxiliary noise amplifies misalignment with the target. BOAR conditions on auxiliary *observability*: separate modules handle cases where auxiliary info exists vs. is absent, moving beyond "observed auxiliary relations" as the only substrate for preference inference. |
| **Key innovations** | First treatment of auxiliary observability as first-class conditioning rather than imputation; up to **7.82% HR@10** overall and up to **44.2%** on target items *without* auxiliary observations; code released (github.com/LSH0411/BOAR). |
| **arXiv** | [2608.22920](https://arxiv.org/abs/2608.22920) · cs.AI/cs.LG |
| **Why it matters** | Multi-behavior ranking is a core CTR/CVR workhorse in commerce ads — but the industry-standard assumption that auxiliary signals are dense hurts long-tail/cold categories. This is a cheap, orthogonal fix. |

### 1.2 Retrieve, Match, Escalate: Accurate and Scalable Product Linking with VLM-Distilled Cross-Encoders and Agentic VLMs

| Field | Detail |
|-------|--------|
| **Authors** | Jian Wang, Steven Xu, Sanjyot Thete, Maryam Barouti, Tom Tang, Elaine Wu, Charu Sareen, Kyle MacDonald |
| **Institution** | DoorDash (inferred: overlapping author team with TRACE, 1.3) |
| **Abstract** | Product linking (mapping merchant records → canonical catalog entries) is the entity-resolution backbone of marketplace search/ads. The production "retrieve-then-match" cascade spends computation proportional to difficulty: retrieval proposes matches; a lightweight text cross-encoder auto-resolves the high-confidence majority at a **98% precision** bar; an agentic multimodal VLM settles the ambiguous tail by inspecting images and issuing web searches for evidence in neither record. The cross-encoder is distilled from millions of dual-VLM-consensus labels (human annotation retired); the self-hosted open-weight agent matches frontier-VLM precision (88% vs 92% recall) at ~⅟₇ per-pair cost. Per-pair cost spans ~5 orders of magnitude across the stages; escalating only the hard tail lifts end-to-end link coverage 68% → 77%. |
| **Key innovations** | Difficulty-proportional cascade formalized as cost ladder; teacher-free distillation from dual-VLM consensus; cost-calibrated escalation criteria. |
| **arXiv** | [2608.25037](https://arxiv.org/abs/2608.25037) · cs.AI/cs.IR/cs.DB |
| **Why it matters** | The retrieve→cheap-rank→agentic-resolve pattern is the same "spend-compute-where-it-counts" economics as [SOLARIS](../../papers/ctr/solaris.md) & [UG-Sep](../../papers/ctr/ug-sep.md), now applied to the master data layer that feeds search, recommendation, and advertising. |

### 1.3 TRACE: Agentic Catalog Enrichment with Multi-source Evidence Grounding

| Field | Detail |
|-------|--------|
| **Authors** | Rohan Kumar, Steven Xu, Kyle MacDonald, Matthew Long, Bernice Chow, Mac VanRenterghem, Sudeep Das |
| **Institution** | DoorDash *(stated on PDF: "DoorDash, Inc.")* |
| **Abstract** | E-commerce catalogs are attribute-sparse, so shoppers and downstream systems re-derive attributes from titles/images on every query. TRACE runs a two-agent produce-then-verify pipeline: a **ScoutAgent** triangulates evidence across seller catalogs, syndicated feeds, and *identity-matched* web search (relevance alone is insufficient — evidence must be about the exact SKU); a **JudgeAgent** verifies each candidate against its evidence and routes it to WRITE / BLOCK / human REVIEW. On Gemini 2.5 Flash: 98.2% accuracy at 74.7% attribute coverage offline; production deployment +90.4% impression-weighted enrichment coverage across 4 verticals; A/B test of surfacing enriched attributes on the product detail page → **+0.48% checkout conversion** and −1.08% missing/incorrect-item rate. |
| **Key innovations** | Verify-before-write gate decouples publication quality from catalog mix; identity-grounded (not just topical) agentic retrieval; production-scale evidence-provenance for attributes. |
| **arXiv** | [2608.20844](https://arxiv.org/abs/2608.20844) · cs.AI |
| **Why it matters** | Catalog quality is the invisible upstream of every rec/ads metric. Two independent DoorDash systems (1.2, 1.3) this week formalize agentic, evidence-grounded data plumbing — consistent with the wiki's "build-for-agents / data scaffolding" theme. |

### 1.4 GUIDE: Generative Unsupervised Chinese Query Correction via Phonetic and Visual Shared-ID Encoding

| Field | Detail |
|-------|--------|
| **Authors** | Lei Yang, Binbin Huang, Jiwei Tan, Xuhui Sui, Chang Tu, Yi Wang, Han Li |
| **Institution** | Kuaishou (inferred: KwaiSearch dataset + Jiwei Tan) |
| **Abstract** | Chinese query correction (CQC) matters for search and query recommendation on content platforms, but supervised pairs go stale as query vocabularies evolve. GUIDE is a *confuse-then-clarify* unsupervised framework: phonetically/visually confusable characters share IDs, and an encoder–decoder must reconstruct the original query — constraining corrections to plausible confusion neighborhoods and preventing intent drift (over-correction toward high-frequency phrases) while learning from unlabeled query streams. A time-decayed, query-frequency-weighted objective adapts to evolving vocabularies. Outperforms strong baselines on QSpell 250K and production KwaiSearch data; online A/B confirms correction-quality and downstream-engagement gains. |
| **Key innovations** | Shared-ID confusion modeling = built-in error grammar without annotations; frequency-aware unsupervised objective tied to vocabulary drift. |
| **arXiv** | [2608.25343](https://arxiv.org/abs/2608.25343) · cs.CL |
| **Why it matters** | Adds a generative-recirculation corner (query correction during generation) to the wiki's retrieval-correction coverage — complementary to supervised [query-correction](../../sources/karpathy-x-2025-llm-reading.md) work in the LLM-search space. |

---

## ② Advertising & Market Mechanisms (2)

### 2.1 Markets, Not Planners: Decentralized Orchestration of LLM Agents with Private Information (AgentLance)

| Field | Detail |
|-------|--------|
| **Authors** | Xiao Liu, Haoyang Li, Songwei Li, Hongbo Fang, Fengli Xu, Feng Shi, James Evans |
| **Institution** | University of Chicago + Peking University / USTC (inferred: Evans & Shi UChicago; Fengli Xu Peking-U affiliated) |
| **Abstract** | Orchestrating many independent LLM agents is "assembling labor across an economy," not calling subroutines — yet current orchestration is centralized: a single planner assigns every task, requiring agents' private costs, bottlenecking as pools grow, and being trivially manipulable (a single inserted preference nearly doubles a favored agent's task share in a centralized LLM allocator). AgentLance is a repeated labor market: agents bid on tasks with **private costs + self-maintained strategy notes**; an allocator selects winners from bids and public reputation; a **VCG-style payment rule** rewards cost-aware bidding; hierarchical delegation lets winners subcontract through the same mechanism. Beats single-model, centralized-orchestration, and market baselines on math reasoning, code gen, knowledge QA, and agentic tasks; diagnosing market failures (cost self-estimation, bidding) and correcting them yields further gains. |
| **Key innovations** | Mechanism-design (auction) answer to agent orchestration; explicit manipulation-resistance and private-information argument; self-maintained strategy notes as agentic "skills ledger." |
| **arXiv** | [2608.23867](https://arxiv.org/abs/2608.23867) · cs.MA/cs.CL |
| **Why it matters** | The economics angle on [decade-of-agents](../../concepts/decade-of-agents.md): if agent economies really arrive, allocation will be auction-based. Ties directly to token-level ad auctions (LAMA, claimed by sibling daily) — both move "who pays for work" into the mechanism. |

### 2.2 AI Agents in Algorithmic Electricity Markets: On the Emergence of Tacit Collusion

| Field | Detail |
|-------|--------|
| **Authors** | Jakub Seredyński, Georgios Tsaousoglou |
| **Institution** | Technical University of Denmark (inferred: Tsaousoglou is DTU) |
| **Abstract** | As power markets become algorithmic bidders, tacit collusion — sustained supra-competitive outcomes reached without communication via independent learning — is a documented failure mode in other markets, and electricity is structurally susceptible (oligopoly, repeated interaction). Models strategic bidding as a repeated game with imperfect public monitoring and multi-agent RL agents. Proposes a multi-dimensional criteria set *beyond* profit-vs-Nash comparison to classify whether emergent behavior constitutes tacit collusion; shows cases where RL agents do learn to sustain supra-competitive outcomes supportive of collusion indicators, without ever being instructed to collude. |
| **Key innovations** | Multi-dimensional tacit-collusion detection criteria for algorithmic markets; MARL evidence in a real-world repeated-bid setting. |
| **arXiv** | [2608.26896](https://arxiv.org/abs/2608.26896) · cs.AI/cs.GT/cs.MA |
| **Why it matters** | Autobidding wholesale adoption in ads/rec ([auto-bidding](../../synthesis/2026-08-26/arxiv-daily.md)) raises the same question: what do independently learned bidding populations converge to? Same "learning dynamics hazard" lens as the wiki's [equal-regret/self-play theory](../../synthesis/2026-08-28/arxiv-daily.md). |

---

## ③ IR / Retrieval (2)

### 3.1 Query Expansion Is More Than Generation: Improving Dense Retrieval through Better Integration (AnchorQE)

| Field | Detail |
|-------|--------|
| **Authors** | Siyuan Sun, Mihai Surdeanu |
| **Institution** | University of Arizona (inferred: Surdeanu) |
| **Abstract** | LLM-generated query expansions often *hurt* a frozen dense retriever. Prior work blamed expansion quality; this paper holds the generated text fixed and shows degradation is frequently the *integration method's* fault. **AnchorQE** separately encodes the original query and the expansion, then interpolates the two vectors. The interpolation factor is estimated at inference time with an unsupervised online strategy over a small part of the unlabeled test stream: high expansion-trust is assigned only when expansions are both retrieval-strong and consistent with the original query's retrieved evidence. Up to **12.89%** retrieval gains over expansion-only / text-concatenation baselines (TREC-DL, LoTTE, BEIR); the online factor beats a dev-tuned fixed weight by up to 3.81%. |
| **Key innovations** | Attribution of expansion failure to integration, not generation; training-free adaptive interpolation trust estimated online. |
| **arXiv** | [2608.25521](https://arxiv.org/abs/2608.25521) · cs.IR |
| **Why it matters** | Cheap, zero-training gain for any frozen-embedding search/ads stack — echoing the wiki line that "how you spend budget matters more than how big it is" (context-allocation laws, [08-25 arxiv-ai-search](../2026-08-25/arxiv-ai-search.md)). |

### 3.2 Risk-Aware Reranking for Agentic Tool Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Qinfei Li, Xiaoxuan Dong, Jin Zhang, Dexu Yu, Wenhao Deng, Junchen Fu, Youhua Li, Hanwen Du, Chunxiao Li |
| **Institution** | Not stated |
| **Abstract** | Tool retrieval is a *pre-execution safety boundary*: unlike documents, tools are executable. Existing methods optimize semantic relevance only and safety audits focus on post-execution failures. This work reframes retrieval-stage reranking as a safety/utility tradeoff: a lightweight reranker over a frozen first-stage retriever models query-conditioned relevance and tool-level exposure risk separately, combines them with an explicit tradeoff parameter, smooths scores over a **ToolGraph**, and optionally applies rule-based safety constraints. To evaluate retrieval-time safety they annotate **6,108 tools** (UltraTool, Seal-Tools) with 5 ordinal risk levels and define top-k risky-tool exposure metrics. Improves relevance–safety tradeoff over relevance-only and reranking baselines; a rule-filtered conservative variant targets safety-critical deployments. |
| **Key innovations** | First retrieval-stage risk-aware formulation for tool exposure; ToolGraph smoothing; released risk-annotated tool corpus + metrics. |
| **arXiv** | [2608.22751](https://arxiv.org/abs/2608.22751) · cs.IR |
| **Why it matters** | Agent tool-use safety is normally discussed at execution; moving the filter earlier is cheaper and defense-in-depth — directly relevant to the wiki's [supply-chain / prompt-injection](../../concepts/prompt-injection.md) and agent-security tracking. |

---

## ④ Games & World Models (5)

### 4.1 GameWAM: A World Action Model for Video Games

| Field | Detail |
|-------|--------|
| **Authors** | Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Weijia Li |
| **Institution** | Fudan University (inferred: first author's GitHub affiliation) |
| **Abstract** | Video-game agents lack world dynamics; game world models can't act. World-Action Models (WAMs) unify both but were unexplored under fast FPS imagery + persistent state + heterogeneous native controls. GameWAM — "first WAM for native closed-loop gameplay and GUI control" — jointly generates future frames and executable keyboard-mouse trajectories via **parallel visual and action generative processes with block-causal conditioning and flow matching**. It predicts a gameplay/GUI mode per step (mode-specific prediction distributions + continuous-action normalization), and for long-horizon play uses block-cycle control: predict beyond the committed horizon, execute a short prefix, replan. Competitive task success with *fewer* executed native actions; also reports **LASI (Low-Frequency Action Source Imprinting)** — low-frequency components of the sampled action source systematically steer coarse camera motion under fixed conditioning, a source-sensitivity failure mode in generative control. |
| **Key innovations** | First game-native WAM (joint video + keyboard/mouse); mode-conditional heterogeneous action output; de novo control-failure-mode finding (LASI). |
| **arXiv** | [2608.26200](https://arxiv.org/abs/2608.26200) · cs.AI/cs.CV/cs.LG · [project](https://yunncheng.github.io/GameWAM/) |
| **Why it matters** | Direct continuation of the WAM line already tracked in this wiki (DreamZero, WAM-RL, CLAP cross-embodiment world models in today's [arxiv-daily](arxiv-daily.md)) — now with games as first-class target, plus a testable control-theory caveat for anyone building action-conditioned gen models. |

### 4.2 Code World Model: Coding Agent as World Brain

| Field | Detail |
|-------|--------|
| **Authors** | Yiwen Chen, Guosheng Lin, Chi Zhang |
| **Institution** | Beihang University (BUAA) + Nanyang Technological University (inferred: project page buaacyw.github.io; Lin NTU) |
| **Abstract** | Video world models learn dynamics from visuals — which reveal outcomes, not the rules governing world evolution. Code World Model separates **world evolution** from **visual realization**: a coding agent is the "world brain" that reasons about events, writes/executes/revisits code, and maintains persistent world state with rule-consistent evolution (code is inspectable, testable, revocable). A **proxy representation** encodes frame-wise spatiotemporal constraints compiled into a proxy video that conditions a video model to render high-fidelity observations. Data pipelines construct aligned proxy–observation pairs from gameplay and real footage; after fine-tuning on paired gameplay data, MiniMax-H3 follows proxy-based specifications while preserving visual detail — "code for persistent world evolution + video for flexible realization." |
| **Key innovations** | Externalized world rules as executable (not learned-from-pixels) state; proxy-video conditioning bridge between code state and latent video priors. |
| **arXiv** | [2608.25927](https://arxiv.org/abs/2608.25927) · cs.CV/cs.AI/cs.CL · [project](https://buaacyw.github.io/cwm/) |
| **Why it matters** | Strongly aligns with the wiki's "externalized, verifiable state" theme ([[../../concepts/verifiability|Verifiability]], ReWorld's landmark memory): world-state as auditable code sidesteps the persistent-consequence failure all video world models share. |

### 4.3 ShuttleArena: Interpretable Self-Play in Physics-Based Badminton

| Field | Detail |
|-------|--------|
| **Authors** | Peize Ding |
| **Institution** | Not stated (single author) |
| **Abstract** | Racket sports force a hard coupling: shot choice and defensive recovery are inseparable (best recovery depends on the shot's induced reply; shot value depends on whether you can cover the answer). ShuttleArena is a physics-based singles badminton self-play environment coupling continuous shuttle flight, interception, structured shot generation, and post-shot recovery. Policy outputs are **role-conditioned** (masked interception on receiver turns; factorized hitter action over azimuth/elevation/speed/recovery), enabling interpretable tactical probes. Training = PPO self-play vs a staged checkpoint pool, sparse rally-outcome rewards, factor-specific recovery updates. Evaluation shows competitive improvement, opponent-conditioned shot-geometry shifts, and that learned recovery is competitively important. |
| **Key innovations** | Shot–recovery coupling made explicit and interpretable; checkpoint-pool PPO self-play in a continuous physics domain. |
| **arXiv** | [2608.25246](https://arxiv.org/abs/2608.25246) · cs.LG |
| **Why it matters** | A clean intermediate scale between Atari and StarCraft for studying two-body strategy — self-play with *position-dependent action values*, complements wiki-tracked sports/games RL. |

### 4.4 Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for VIPs in JEPA World Models (SCG)

| Field | Detail |
|-------|--------|
| **Authors** | Frederik Berenz |
| **Institution** | Not stated (single author) |
| **Abstract** | JEPA world-model encoders are usually fixed-size: over-provisioned for simple tasks, under-provisioned for hard ones, with redundant attention heads. SCG starts from a minimal ViT encoder (1 head, 2 layers, 283K params) and grows **width** (heads for low-level semantics) or **depth** (blocks for higher-order abstraction) under a test-and-verify scheme using function-preserving expansion — trial a change, roll back if prediction loss doesn't improve. A **SIGReg** regularizer keeps learned semantic dimensions independent while growing. On a 60-dim multi-object dynamics task SCG triggers depth expansion: **+20.3% prediction-loss improvement** over the fixed-small baseline at 56× parameter efficiency vs the fixed-large model; on 2D navigation a single width expansion beats the fixed large model by 23%; zero false-positive expansions, bit-exact function preservation. |
| **Key innovations** | Capacity-growth (not pre-allocation) for world-model encoders; architecture-rollback verification; collapse-resistant expansion. |
| **arXiv** | [2608.27367](https://arxiv.org/abs/2608.27367) · cs.CV/cs.AI |
| **Why it matters** | Directly relevant to the wiki's JEPA/world-model efficiency track (CLAP, Alaya-EVOKE): encoder capacity as a *grown* resource, and the 56×-efficiency number is a strong claim worth reproducing. |

### 4.5 Optimal Alternating Regret for Online Learning and Games

| Field | Detail |
|-------|--------|
| **Authors** | Yixin Tao, Weiqiang Zheng |
| **Institution** | Not stated |
| **Abstract** | Settles minimax-optimal *alternating regret* (a notion motivated by alternating learning dynamics in games) for OLO and OCO. For OLO on the simplex: an algorithm with **O(log d) alternating regret constant in T** and matching lower bound — the first uncoupled learning dynamics with **O(1/T)** convergence to CCE in two-player general-sum games (prior works carry extra log-T factors); O(log d /T) convergence to Nash in zero-sum games. For general OCO on a d-dim compact convex set: O(d log(1+T/d)) with matching Ω(d log(1+T/d)) lower bound, showing the Ω(log T) factor is unavoidable. |
| **Key innovations** | Tight (constant) alternating-regret for simplex OLO; first O(1/T) uncoupled CCE convergence in general-sum games; matching lower bounds. |
| **arXiv** | [2608.24731](https://arxiv.org/abs/2608.24731) · cs.LG/cs.GT |
| **Why it matters** | Theory anchor for self-play/multi-agent training dynamics: which regret notion matches what learners actually generate — connects to MBCCE-style equilibrium work ([08-25 arxiv-ai-search](../2026-08-25/arxiv-ai-search.md)) and the wiki's MARL theory line. |

---

## ⑤ Agents & Agentic RL (5)

### 5.1 Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification (HarnessLens)

| Field | Detail |
|-------|--------|
| **Authors** | Jinghan Xu, Yikai Zhang, Aili Chen, Weiyuan Li, Jiaqing Liang, Deqing Yang |
| **Institution** | Fudan University (inferred: Deqing Yang) |
| **Abstract** | Automated harness evolution (propose-and-verify) scores every candidate on a fixed task set — wasteful and prone to aggregate scores masking specific regressions. HarnessLens jointly explores the *task space* and user-configurable components, derives candidate modifications from execution trajectories, and **selectively verifies each candidate on behavior-relevant tasks using an attributable-evidence gate** (only verify where the change should matter). Across 3 harnesses × 4 benchmarks: +7.6–13.6% average held-out performance with substantially less evaluation budget than competing baselines. |
| **Key innovations** | Attribution-gated verification couples *which* candidate changes to *which* tasks — a targeted fix for the sample-efficiency problem in harness evolution. |
| **arXiv** | [2608.27311](https://arxiv.org/abs/2608.27311) · cs.AI |
| **Why it matters** | Same wave as AutoSaddler / StarHarness / Prime Agent: the scaffold optimizes itself. HarnessLens's contribution is *verification budgeting* — precisely the economics gap the wiki noted when harnesses became learnable artifacts ([08-25 arxiv-ai-search](../2026-08-25/arxiv-ai-search.md)). |

### 5.2 SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL

| Field | Detail |
|-------|--------|
| **Authors** | Kai Ruan, Jinghao Lin, Qianshan Wei, Ziqi Zhou, Zihe Huang |
| **Institution** | Not stated |
| **Abstract** | Group-relative RL (GRPO-style) waits for sibling rollouts — costly for long, variable tool-use trajectories. Single-Stream Policy Optimization (SPO) eliminates that with a persistent prompt-level value estimate, but SPO whitens *one advantage per trajectory* while the actor optimizes a **token-mean loss**; this paper shows trajectory centering generally doesn't center the token-weighted quantity actually consumed, and fixes the mismatch by standardizing terminal-outcome advantages under the **action-token measure**. Also reorganizes prompt evidence by the *policy event* that generated it, not learner-receipt order. On ALFWorld (two model scales) and Math-TIR, SPO++ improves online efficiency over SPO; a paired ablation isolates action-token-measure normalization as the strongest component. |
| **Key innovations** | Identifies and fixes a measure mismatch in stream-based advantage whitening; event-ordered (not receipt-ordered) prompt evidence. |
| **arXiv** | [2608.24870](https://arxiv.org/abs/2608.24870) · cs.AI |
| **Why it matters** | Efficiency of online agentic RL is now the bottleneck; this is a precise correction to the SPO recipe rather than another algorithm — relevant to the wiki's [rl-is-terrible / RLVR](../../concepts/rlvr.md) threads. |

### 5.3 MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG

| Field | Detail |
|-------|--------|
| **Authors** | Qiuyi Qi, Tian Liang, Jiamu Wang, Jinjian Zhang, Wei Zhou, Pengcheng Zhu, Linjian Mo, Ming Kong, Jie Liu, Qiang Zhu |
| **Institution** | Not stated (industry team; Tian Liang / Qiang Zhu affiliations unreported) |
| **Abstract** | Agentic RAG requires deciding *when to keep searching vs. when to answer*. Prior RL methods judge only the external result and ignore the agent's internal belief about evidence sufficiency. MetaRAG reformulates search-decision quality as **belief–action alignment**: Verify-first Action Generation elicits an explicit verification step before each action; Internal Belief Probing estimates the policy's own answerability belief from the same question–history context (training-only, zero inference overhead); a **consistency reward gated by answer correctness** avoids reinforcing internally-consistent-but-wrong trajectories. On 7 public QA benchmarks MetaRAG improves the accuracy–efficiency tradeoff over strong RL agentic-RAG baselines, transferring across deep-research settings, optimizers, and backbones. |
| **Key innovations** | Belief signal as reward — an *internal* supervision channel on top of external correctness; gating prevents spurious internal consistency. |
| **arXiv** | [2608.24214](https://arxiv.org/abs/2608.24214) · cs.AI |
| **Why it matters** | "Search-until-confident" is core to [RL from inference-time compute](../../roles/researchers.md); belief-action consistency is a transferable reward recipe beyond RAG. |

### 5.4 SMITH: Joint Optimization of Tool Creation and Use for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee |
| **Institution** | National Taiwan University (inferred: Lin/Chen/Sun/Lee all NTU) |
| **Abstract** | Tool-augmented models are bounded by "the APIs humans bothered to write." Prior tool-creation systems prompt a frozen LLM at inference, decoupling the writer from the user. **SMITH** trains tool creation *and* use inside a single policy: each rollout is a build task (write a tool from examples) or a use task (invoke the pooled tool on a held-out question), with **three separate reward axes** catching schema / code / outcome failures independently. A 4B Qwen3 trained on 13 procedurally reasoned tasks with exact verifiers: **79.8 macro-avg accuracy** on held-out tasks (best of all evaluated methods, ahead of an untrained 30B-A3B tool-writer); 40.4 on TabMWP-Hard and 42.6 on OOD GQA (+7.6 over same-backbone inference-time baselines) with no visual/tabular training data; SMITH-written tools also lift LFM-2.5-350M and Qwen3-30B-A3B. |
| **Key innovations** | End-to-end tool-creation gradient for the *writer* (fixes schemas it can actually invoke); decomposed reward axes per failure mode; strong small-model + OOD results. |
| **arXiv** | [2608.24571](https://arxiv.org/abs/2608.24571) · cs.AI/cs.SE |
| **Why it matters** | A concrete "agents build their own tools" capability — the same direction as the wiki's [software-3-0 / build-for-agents](../../concepts/build-for-agents.md) thesis, with numbers a 4B model can reach. |

### 5.5 The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams

| Field | Detail |
|-------|--------|
| **Authors** | Summer Eunhyung Ann, Haokun Liu, Chenhao Tan |
| **Institution** | University of Chicago (inferred: Tan) |
| **Abstract** | Pro-vs-con debate on multi-agent LLM interaction (gains from debate/critique vs. "cost without quality under equal budgets") is partly a missing distinction: **not all communication is equal**. Different model families find structurally different solutions, but when agents read each other's complete outputs, their proposals **converge within one round**, erasing the diversity that motivated multi-model teams — the "interaction tax." On 11 verifier-scored optimization tasks under matched budgets: full-solution interaction is a weak default; independent proposal generation avoids collapse; full-solution interaction mainly pins agents to the *first* solution they see; critique helps only when the violated rule is easy to find and fix. |
| **Key innovations** | Characterizes when inter-agent information exchange destroys rather than creates value; direct mechanism (first-solution anchoring/convergence). |
| **arXiv** | [2608.23541](https://arxiv.org/abs/2608.23541) · cs.MA/cs.AI |
| **Why it matters** | Quantifies the cost of naive "more agents = better" — the wiki's [peak-capability / population](../../concepts/peaky-capability.md) skepticism, with an actionable design rule: control *what* agents see, not just how many agents there are. |

---

## ⑥ LLM Training, Efficiency & Evaluation (3)

### 6.1 SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in RL

| Field | Detail |
|-------|--------|
| **Authors** | Zhuochun Li, Yuelyu Ji, Yiming Zeng, Daqing He |
| **Institution** | University of Pittsburgh (inferred: Daqing He) |
| **Abstract** | RL-based distillation faces a reward dilemma: sparse outcome rewards give weak logical guidance; neural PRMs are expensive. SPEAR is a **training-free, plug-and-play process reward** for sequence-level on-policy distillation: project natural-language reasoning traces into **domain-adaptive symbolic milestones**, then align student explorations with teacher milestones via **longest common subsequence (LCS)** — a dense, order-aware reward enforcing logical consistency without an external verifier. Effective across math, science, and commonsense reasoning tasks. |
| **Key innovations** | Symbolic milestone projection turns soft traces into alignable structure; LCS = cheap dense reward respecting step order. |
| **arXiv** | [2608.26550](https://arxiv.org/abs/2608.26550) · cs.CL |
| **Why it matters** | The collision between [RL-from-verifiable-rewards](../../concepts/verifiable-rewards.md) and distillation: if process signals can be made symbolic for free, PRM-era costs shrink. Compare ADAPT-family on-policy distillation in the sibling daily (08-25). |

### 6.2 The Reasoning Tax: Token Economics of LLM Reasoning Across Task Types and Deployment Contexts

| Field | Detail |
|-------|--------|
| **Authors** | Sachin Gopal Wani, Ajay Dholakia, David Ellison |
| **Institution** | Not stated |
| **Abstract** | Accuracy-only benchmarks miss the core deployment question: when do extended thinking tokens *earn their cost*? Introduces the **Token Economy Score (TES)** — accuracy gain of a reasoning model over a non-reasoning baseline normalized by generated-token multiplier — with paired and approximated variants for families with and without reasoning toggles. Empirics: 151 model-benchmark runs, 7 benchmarks (math, code, science, instruction-following, expert knowledge, knowledge recall, research physics). Task structure predicts reasoning efficiency better than nominal difficulty: sequential inference-chain tasks (AIME 2025, LiveCodeBench) → high TES; knowledge recall (MMLU-Pro) → low TES despite difficulty. Also: systematic diminishing returns at high effort (extra thinking can *reduce* accuracy); **Reasoning Cost Share** (inference spend dominated by internal thinking) and **Deployment Cost Multiplier** (on-prem changes economics). |
| **Key innovations** | Marginal cost-normalized reasoning metric (TES); task-type × effort × deployment as the axes of reasoning-economics; evidence for "reasoning hurts some modes." |
| **arXiv** | [2608.26235](https://arxiv.org/abs/2608.26235) · cs.AI/cs.PF |
| **Why it matters** | Gives a quantification framework for the wiki's efficiency/deployability thread ([peer-budget, token economics](../../synthesis/2026-08-26/arxiv-paper-check.md)) — "selective reasoning by task type, not universal mode." |

### 6.3 BALIGN: Preference Data Selection for Mitigating the Alignment Tax

| Field | Detail |
|-------|--------|
| **Authors** | Minsu Kim, Jianxun Lian, Xing Xie, Steven Euijong Whang |
| **Institution** | Microsoft Research Asia + KAIST (inferred: Lian & Xie are MSRA; Whang KAIST) |
| **Abstract** | Alignment fine-tuning routinely catastrophic-forgets pre-trained capabilities — the "alignment tax." Prior work frames it as optimization/architecture; BALIGN targets the *data*. From preference-optimization gradient analysis, three data-centric features predict parameter drift: (1) reference model's log-probability margin, (2) token-length difference between chosen and rejected responses, (3) TF-IDF similarity to general-capability corpora. Aggregated into a composite risk score, BALIGN filters high-risk samples (those disrupting intrinsic params or giving minimal alignment utility). Preserves foundational capabilities without sacrificing alignment gains — optimal Pareto frontier on standard human-preference datasets at minimal compute overhead. |
| **Key innovations** | First data-selection (not method-level) attack on alignment tax; orthogonal risk features derived from the gradient itself. |
| **arXiv** | [2608.24192](https://arxiv.org/abs/2608.24192) · cs.AI/cs.CL |
| **Why it matters** | Data triage is the cheapest lever on the alignment-tax problem the wiki tracks ([[../../concepts/verification-gap|RLHF vs plain SFT]] tradeoffs); directly useful for post-training pipelines. |

---

## Cross-cutting observations

1. **E-commerce data is becoming agentic plumbing** (Box 1.2/1.3/1.4 + market mechanism 2.1): catalog enrichment, product linking, and orchestration all now ship produce-and-verify agent loops with explicit evidence provenance, and the A/B numbers (+0.48% conversion, 68→77% coverage) are production-scale. The "grounded, verifiable data layer" is where agent value is being monetized first.
2. **World models split "world" from "visuals," twice** — GameWAM (parallel video+action generation), Code World Model (code as persistent state, video as renderer), and SCG (growable encoder) all separate causal/state machinery from pixel simulation. Consistent with the wiki's Alaya-EVOKE/Marionette tracking: the memory/state substrate, not pixel fidelity, is the current frontier.
3. **Reward engineering is consolidating on internal signals**: belief-action alignment (MetaRAG), symbolic milestones (SPEAR), action-token measure (SPO++), and preference-data selection (BALIGN) all move supervision away from external scalar outcomes toward process/geometry signals.
4. **Multi-agent benefits are conditional, not automatic**: Interaction Tax shows information exchange can erase diversity; AgentLance shows mechanisms (auctions) beat planners; tacit-collusion work warns learning populations may game the mechanism. Orchestration and mechanism design are converging on the same object: *what information flows between agents*.

## Methodology

- 9 arXiv API queries (`export.arxiv.org`) sorted by submission date: cs.IR(400), cs.CL(400), cs.AI(500), cs.LG(500), cs.GT(250), cs.MA(250), cs.CR(200), cs.HC(200), `all:recommendation`(400) → 2,469 unique papers (ID range 2607.18115–2608.27455).
- Domain-tuned keyword scoring (rec / ctr-advertising / sequential / generative-rec / retrieval / LLM-agent / games / efficiency / eval), freshness filter ≥ 2026-08-20 → 417 weighted candidates → manual abstract review → 21 verified-new papers reported.
- Every reported ID grep-verified absent from `wiki/` (known-ID set of 3,896 IDs) and from same-day sibling [arxiv-daily](arxiv-daily.md) (which separately claimed 28 papers in the 2608.26480–27454 window).
- Temp fetch files cached under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv0828/` and deleted after use (per temp-file constraint).
- For TRACE, DoorDash affiliation confirmed from the PDF front matter via web search; GameWAM and Code World Model affiliations inferred from author GitHub/project pages.

*All affiliations above are stated only when the paper says so; "(inferred)" entries are deduced from author identities and remain tentative.*