---
title: "Conference & arXiv Digest — 2026-10-08 (NeurIPS 2026 / ICML 2026 / ACL 2026 / EMNLP 2026 / ICLR 2026 / AAAI 2026 / KDD 2026 / CVPR 2026 / RecSys 2026 / CIKM 2026 / AAMAS 2026)"
type: synthesis
created: 2026-10-08
updated: 2026-10-08
sources: [arxiv-export-api, arxiv-html, conference-announcements]
tags: [conference-digest, NeurIPS2026, ICML2026, ACL2026, EMNLP2026, ICLR2026, AAAI2026, KDD2026, CVPR2026, RecSys2026, CIKM2026, AAMAS2026, agents, LLM, code-reasoning, world-models, recommendation, advertising, benchmarks, evaluation, quantization, serving, daily-digest]
---

# Conference & arXiv Digest — 2026-10-08

> **Scope.** Papers whose arXiv submission dates fall in the observed span **2026-08-16 → 2026-10-07** and that carry a *verified* venue tag from the requested list — **ICML 2026, AAAI 2026, NeurIPS 2025/2026, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025/2026, SIGIR 2026, WWW 2026, CIKM 2025/2026, RecSys 2025/2026** — plus AAMAS 2026, across the wiki's core categories: agents, LLM training/inference, code & verification, world models & RL, recommendation/advertising, NLP, and evaluation. **47 papers featured**, **organized by venue, then category**. Four further candidates were **withdrawn as same-day / prior-wiki collisions** and are listed in §16.

**Method (for reproducibility).** Harvest via the **arXiv export API** (`export.arxiv.org/api/query`, Atom XML): **47 serialized queries** — 25 `comment:` venue sweeps (incl. `SIGIR/WWW/CIKM/RecSys/KDD/ICLR/AAAI/CVPR` 2025 *and* 2026 tags), one date-bounded category sweep, and 21 topic/lab queries — requests spaced ≥3–4 s. The API's failure mode is a bare **14-byte `Rate exceeded.` body with no HTTP error status**, which a naive parser reads as *zero results*; this run logged **no re-fetches**, and four queries (`Meta AI`, `Microsoft Research`, `Baidu`, `code execution prediction`) returned 0 hits **within their `submittedDate` window and were accepted as-is** — a zero here is therefore *not* independently distinguished from a silent rate-limit. Venue tags were read from each entry's arXiv `comment` / `journal_ref` fields. Affiliations were read **only** from the paper's own arXiv HTML author block (`arxiv.org/html/<id>`), **never inferred from surnames or email domains** — unresolved items are marked *(affiliation not recovered)* rather than guessed; **2 featured entries** are so marked.

**Dedup.** Baseline regex-extract of every `NNNN.NNNNN` id across `wiki/**/*.md` at run start → **8,133 unique claimed arXiv IDs**; pool of 5,730 records → 1,679 unique → **1,371 unclaimed → 492 venue-tagged → 52 selected → 48 kept after collision re-check (47 featured + 1 noted-only)**. All 47 featured IDs were **re-verified 0-hit against the whole live wiki immediately before writing** (baseline has since grown past 8,248 IDs as sibling jobs committed).

---

## 0. Executive Summary

- **Venue spread is unusually even** — 12 conferences / 13 venue tags carry hits, none above 13 papers: NeurIPS 2026 **13** (4 main + 9 workshop), EMNLP 2026 **9**, ICML 2026 **6**, ACL 2026 **3**, KDD 2026 **3**, CIKM 2026 **3**, ICLR 2026 **3**, RecSys 2026 **2**, CVPR 2026 **1**, AAAI 2026 **1**, AAMAS 2026 **1**, plus NeurIPS 2025 **1** and EMNLP 2025 **1** carry-overs — **47 in total**. **Four requested venues are empty this window: SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025** (§14).
- **The strongest cluster is *evaluation is broken* — 7 papers across 6 venues.** Evidence-grounded accuracy for AI scientists drops Claude from 95% to **41%** once evidence is withdrawn/reversed (`2610.04915`, NeurIPS workshop oral); shipped **AppWorld/WorkArena verifiers accept 6/15 and 21/23 wrong-state executions** (`2610.09142`); benchmark labels themselves are wrong on **18.0%** of EquiBench pairs (`2610.04371`, AWS); signer-independent re-evaluation cuts sign-language BLEU-4 from 21.44 to **3.59** (`2609.07965`); the *Verification Trap* shows generator and verifier share false premises (AUROC 0.846 predictor, `2610.05170`); a *serving stack* paper shows tool-use fidelity can be an **Ollama artifact** (±55 pt, `2609.26693`); and a quantization study shows the 8-vs-4-bit conclusion **flips sign with the prompt and the scoring policy** (`2610.07781`).
- **Industrial-lab papers are unusually dense this window: 6 of 47 are company-first-authored, 8 have a company affiliation** — **Meta AI** (category-conditioned agent memory, `2610.07100`), **AWS AI Labs** (code-equivalence auditing, `2610.04371`), **NVIDIA AI Technology Center** (SSM operator conditioning, `2610.09092`), **Alibaba Group + USTC** (demand forecasting on 32M product trajectories, `2608.25871`), **eBay + Ben-Gurion** (aspect affinity, `2609.02468`), **JPMorgan Chase ML Center of Excellence** (hierarchical long-term memory, `2610.02472`); plus **Morgan Stanley** as a co-affiliation (`2610.04791`) and **AIM Intelligence** co-authoring MIOH (`2608.30653`). The seventh targeted company paper — **Dable Inc.**'s RTB filter study `2609.08725` — was **withdrawn as a collision** (§16).
- **Agent systems (13 papers)** split cleanly into *how to build them* — SkillForge's skill lifecycle (**+7.8%** relative, `2610.09832`), STEPGATE's step-level cloud handoff (**69.0%** vs 48.0% local-only at 30% cloud, `2610.07816`), APDMem's 4-layer progressive disclosure (strong LongMemEval at **8%** of conversation reads, `2610.02472`) — and *how to bound them*, where the sharpest result is **"Not Self-Decidable"**: across ~22,000 labels from 4 models/3 labs, models agree on obvious predicates, collapse on regulatory text, and **err together on the deployed agent's own rules in the direction that never escalates** (`2610.04699`).
- **Numbers that anchor the window:** HealthBench **70.1** for the 27B HuatuoGPT-3 with **RL-only** adaptation (no SFT stage, `2610.05966`); **−42.6%** average and **−84.8%** tail latency for memory-aware LLM serving (`2609.15359`); **−62%** jailbreak ASR from inference-time safety-aware token pruning (`2610.09703`); **+14.8%** Recall@300 from hybrid CF+GNN candidate generation at 2M-property scale (`2609.05748`); CodeGraph's **158M nodes / ~1B edges** over 167M Stack-Edu files (`2609.29474`).

---

## 1. NeurIPS 2026 — Main Track (4 papers)

### 1.1 SkillForge — Co-Evolving Skills and Agents via Dynamic Skill Lifecycles
- **中文标题**: SkillForge：通过动态技能生命周期实现技能与智能体的协同演化
- **Authors**: Yuyao Ge, Yiwei Wang, Yuchen He, Baolong Bi, Lingrui Mei, Jiayu Yao, Lizhe Chen, Shenghua Liu
- **Affiliation**: Institute of Computing Technology, Chinese Academy of Sciences; University of California, Merced; Tsinghua University
- **Venue**: **NeurIPS 2026**
- **Problem background**: Memory-augmented RL strengthens LLM agents on long-horizon tasks, but keeping every skill as the policy improves lets **obsolete or harmful entries accumulate** and mislead the agent.
- **Key innovation**: A **fitness-driven skill lifecycle** with four states — *trial, active, stable, retired* — so the skill library and model co-evolve: a **pre-RL phase** uses the base model's own rollouts to pre-retire low-fe fitness skills and seed SFT; during RL, **selective retirement, stabilisation and LLM-guided mutation** continue alongside policy optimisation.
- **Results / comparison**: Highest aggregate success across multiple interactive agent benchmarks, **up to +7.8% relative** over the strongest baseline, with the library kept compact throughout. Releases **SkillFurnace** (5k+ annotated records: retirement-filtered SFT trajectories, evolved libraries with fitness labels, human-annotated failure categories).
- **Link**: https://arxiv.org/abs/2610.09832

### 1.2 Self-Consuming Generative Models with Co-Evolving Human Preferences
- **中文标题**: 与人类偏好共同演化的自消耗生成模型
- **Authors**: Xiukun Wei, Tian Xie, Ding Zhu, Xueru Zhang
- **Affiliation**: The Ohio State University
- **Venue**: **NeurIPS 2026** (conference paper)
- **Problem background**: Self-consuming loops (users curate model output → curation trains the next generation) have been analysed only under **fixed** preferences; in reality exposure to model output **reshapes what users find desirable**.
- **Key innovation**: First treatment of the **coupled dynamics** of model distribution *and* preference. Theory: with curated synthetic data only, iterative curation **amplifies initial bias** and drives the system to one of several **singleton equilibria** (the initially advantaged instance dominates); injecting **reference data above a sufficient rate** changes the dynamics to a **unique globally attracting equilibrium**. Proposes an efficient algorithm jointly choosing the reference distribution and its **mixing weight**.
- **Results / comparison**: Analytic characterisation of the equilibria plus a steering algorithm that preserves desired attributes while **minimising data-collection cost** — a control result rather than a benchmark win.
- **Significance**: Directly relevant to the wiki's model-collapse / synthetic-data thread.
- **Link**: https://arxiv.org/abs/2610.09415

### 1.3 EpicWorldModel — Exploration-driven Planning with Latent World Models
- **中文标题**: EpicWorldModel：基于隐空间世界模型的探索驱动规划
- **Authors**: Bowen Feng, Julian Ost, May Mei, Anirudha Majumdar, Felix Heide
- **Affiliation**: Princeton University; Torc Robotics
- **Venue**: **NeurIPS 2026**
- **Problem background**: JEPA-style latent world models are **deterministic by design**, which breaks down under partial observability — the same history can lead to several plausible futures (occlusion).
- **Key innovation**: Trains a **stochastic JEPA** that predicts *multiple* candidate futures with a **flow-matching objective** on the latent representation, then uses **flow predictive variance** (motivated as a bound on predictive entropy) as an **exploration signal inside CEM-based planning**, balancing goal-reaching against uncertain regions where occluded goals are likely to be.
- **Results / comparison**: Best or on-par across latent-planning tasks; **up to +22% success rate** over LeWorldModel.
- **Link**: https://arxiv.org/abs/2610.05996

### 1.4 MaRK — Markov-adapted Recurrent Kernels for Dynamic Operator Conditioning in State Space Models
- **中文标题**: MaRK：面向状态空间模型动态算子条件化的 Markov 适配递归核
- **Authors**: Syed Ibrahim Omer, Ginny Y. Wong, Xiangyu Zhao
- **Affiliation**: City University of Hong Kong (Department of Data Science); **NVIDIA AI Technology Center** (Santa Clara)
- **Venue**: **NeurIPS 2026** (via `journal_ref`: "NeurIPS 2026"; no acceptance comment posted — *(tentative on main-vs-workshop)*)
- **Problem background**: Conditioning a *pre-trained* SSM for iterative generation normally happens **outside** the recurrence (input injection, activation modulation), leaving the temporal dynamics **fixed**.
- **Key innovation**: Maps context vectors into **bounded modulations of the frozen recurrence parameters** `A, B, C, D, Δ`; viewed as an **LPV-SSM**, each diffusion timestep reshapes a context-indexed family of **Markov parameter sequences**. Three adapter geometries — **Hypernet, Chebyshev, DCT** — on a frozen **111M Hydra** backbone. Because the adapters are low-rank maps over a frozen backbone, **parameter-efficient tuning falls out structurally** (6.3–11M trainable params), and the bounded parameterisation yields an **analytic Affine Quadratic Stability certificate**.
- **Results / comparison**: Chebyshev best (validation loss **2.55**), DCT 2.59, Hypernet 3.77; recovers coordinate-invariant temporal operators in synthetic LPV tests.
- **Link**: https://arxiv.org/abs/2610.09092

## 2. NeurIPS 2026 — Workshops (9 papers)

> All nine are workshop-acceptances (non-archival or archival per the comment); verifiers, SLM routing and evaluation methodology dominate.

### 2.1 Agents: verification & rules

#### 2.1.1 FEAgent — Functionally Equivalent or Not? Graph-Grounded Differential Surrogate Execution for Code Equivalence
- **中文标题**: FEAgent：基于程序图证据与差分替代执行的代码等价性判定
- **Authors**: Amit Kachroo, Like Hui, Haitao Mao, Yuhao Zhang, Nguyen Vo
- **Affiliation**: **AWS AI Labs** (Santa Clara / New York)
- **Venue**: **NeurIPS 2026 Workshop on AI for Verifiable Coding**
- **Problem background**: Equivalence checks rest on incomplete signals — tests cover finite inputs, text similarity confuses implementation with behaviour, raw LLM judgement is unauditable, and direct execution is often impossible (obsolete/licensed/unsafe environments).
- **Key innovation**: A **selective assessor agent** combining typed **program-graph evidence** (call/control/data-flow, types, imports, effects) with **differential surrogate execution**: two *blinded* LLM surrogates independently predict source/target observables, every claim is written to an **evidence ledger**, and a deterministic reconciler returns EQUIVALENT / INEQUIVALENT / **UNCLEAR** instead of forcing a verdict.
- **Results / comparison**: Disagreements with the oracle adjudicated by real execution reveal **benchmark-label errors**: on **EquiBench**, execution confirms FEAgent's disagreement with published labels on **216/1,200 pairs (18.0%)**; on **SWE-bench Verified**, **94/331 (28.4%)** test-passing agent patches **diverge** from the reference patch. Positioned as an **audit layer between testing and formal verification**.
- **Link**: https://arxiv.org/abs/2610.04371

#### 2.1.2 Finding Blind Spots in AppWorld and WorkArena Task Verifiers
- **中文标题**: 审计 AppWorld 与 WorkArena 任务验证器的盲点
- **Authors**: Richard Abrich
- **Affiliation**: OpenAdapt.AI (MLDSAI Inc.)
- **Venue**: **NeurIPS 2026 workshop "Who Verifies the Agents?"** (poster)
- **Problem background**: Execution-based verifiers decide whether an agent succeeded — so a verifier bug is a **silent reward hack**.
- **Key innovation**: **Source-informed mutation testing** that never modifies the shipped checker: duplicate a non-idempotent write (checked fields unchanged, extra record created) and see whether the verifier still passes.
- **Results / comparison**: AppWorld — **6/15** constructed effects pass, from **2 of 5** eligible generators; a cardinality patch makes all six fail while valid controls stay green. WorkArena — of 23 earlier checker-PASS candidates, **21 have independently confirmed non-default persisted values, all 23 still PASS**; 2 are aliases of stored defaults. Intent-swap grid: **0 PASS on 2,689** off-diagonal executions (a rejection census, not a rate estimate).
- **Link**: https://arxiv.org/abs/2610.09142

#### 2.1.3 Not Self-Decidable — LLMs Cannot Draw the Boundary of What an Agent Verifier Can Check
- **中文标题**: 不可自我裁定：LLM 无法划定 Agent 验证器的可判定边界
- **Authors**: Anthony Rhodes
- **Affiliation**: Confidential Core AI
- **Venue**: **NeurIPS 2026 "Who Verifies the Agents?" Workshop** (non-archival)
- **Problem background**: A verifier must split every rule predicate into *fixed-checkable* vs *needs-a-judge*. Teams that write their own rules fix that split up front; where requirements come from outside (finance, healthcare, law), the split must be made **at runtime, for every predicate, at a rate no reviewer can audit**. Escalation schemes assume the model can make that call itself — that it is *self-decidable*.
- **Key innovation**: ~**22,000 labels** from **4 models built by 3 labs** across six corpora (EU AI Act, FINRA guidance, a deployed credit agent), plus **CoVer (corroborate-then-verify)**: unanimity is only a *nomination*; a predicate is admitted only if the synthesised check **survives intervention**, reads fields the agent cannot write, and holds under deterministic rewording.
- **Results / comparison**: Models agree almost perfectly on obvious answers but **collapse on regulatory text**; errors run in **opposite directions** (no model is the conservative choice); on the deployed agent's own rule-set they **err together, over-claiming that a fixed check will do — the direction that never escalates**. The obvious alternative — agreement with a reference judge — certifies nothing: agreement climbs **30% → 77%** across calibration bands while the genuinely decidable share does not move.
- **Link**: https://arxiv.org/abs/2610.04699

### 2.2 Agents: SLM routing & memory

#### 2.2.1 Not Every Call Needs a Frontier Model — Per-Call-Site Evaluation of SLMs in a Deployed Home-Automation System
- **中文标题**: 并非每次调用都需要前沿模型：部署态家庭自动化系统的逐调用点 SLM 评估
- **Authors**: Panagiotis Kasnesis, Christos Chatzigeorgiou, Lazaros Toumanidis, Amalia Contiero Syropoulou
- **Affiliation**: University of West Attica (Athens); Waldiez PC; ThinGenious PC
- **Venue**: **NeurIPS 2026 Workshop on SLMs for Agentic Systems** (Paris)
- **Problem background**: An agentic system issues structurally different call sites (intent routing, action classification, device-registry grounding, multi-agent planning, Python codegen) whose difficulty spans an order of magnitude — yet practice picks **one model, for the hardest site, and uses it everywhere**.
- **Key innovation**: Evaluation on the **unmodified production prompts** of a deployed open-source framework (Wactorz) over two real Home Assistant installations — **9 models (0.8B → frontier hosted), 5 call sites, 280 cases, 2,520 scored calls**, with paired statistical testing per site.
- **Results / comparison**: Capability is **not ordered the same way at every site**; a 4B model is *worse* than its 2B sibling on grounded actuation. Best local model is statistically **indistinguishable from both hosted models at 4/5 sites**; only code generation separates them (p=0.039 vs small hosted, p=0.002 vs frontier). Routing each site to its best local model: **91.8% vs 95.4%** at zero per-call cost; live deployment hosting only the two generative sites matches full hosting (**39/43 vs 39/43**) at **28% of the spend**. ⚠️ Safety finding: **Gemma4 E2B actuates 87.2% of requests for devices the site does not own**, another model refuses everything — aggregate accuracy hides degenerate accuracy/refusal trade-offs.
- **Link**: https://arxiv.org/abs/2610.09021

#### 2.2.2 STEPGATE — Do I Need the Cloud? Uncertainty-Aware Step-Level Handoff for SLM Agents
- **中文标题**: STEPGATE：SLM 智能体的不确定性感知步级云端切换
- **Authors**: Abolfazl Younesi
- **Affiliation**: Sharif University of Technology (Tehran)
- **Venue**: **NeurIPS 2026 Workshop on SLMs for Agentic Systems**
- **Problem background**: Routers pick a model **once per query**, but agents expose **sequential decision points** whose difficulty changes after each intermediate observation.
- **Key innovation**: Scores **each local SLM action** and escalates only hard steps to a stronger model (uncertainty-aware handoff), with risk tiers as research annotations.
- **Results / comparison**: Single-step (52-task BFCL-derived hold-out), Qwen2.5-1.5B/7B pair: **82.7% at 30.8% escalation** vs **67.3%** local-only and **75.4%** random escalation (33.8% escalation). Multi-turn: **69.0% trajectory / 84.0% action success at 30.0% cloud actions** vs 48.0%/70.5% local-only, 60.0%/78.2% random, **57.0%/77.1% query-level routing**; strong-only gets 82.0% at 100% cloud. ⚠️ Stated limits: one model family, one backend, small test sets.
- **Link**: https://arxiv.org/abs/2610.07816

#### 2.2.3 When to Remember, When to Abstain — Category-Conditioned Retention for Reliable Agent Memory
- **中文标题**: 何时记忆、何时弃权：面向可靠 Agent 记忆的类别条件化保留策略
- **Authors**: Olukunle Owolabi, Pulkit Gupta, Fei Wang
- **Affiliation**: **Meta AI**
- **Venue**: **NeurIPS 2026 Social Agent Workshop**
- **Problem background**: A memory write decision can only be as reliable as its source — a weakly-supported assertion gets stored and later reused as fact. A **single global confidence threshold** cannot handle this: values/beliefs are inherently less supported than other assertion types.
- **Key innovation**: Make the confidence bar **conditional on the semantic category** of the assertion — retain well-evidenced categories liberally, abstain aggressively where inference is unreliable — evaluated in a **deployed cold-start memory pipeline** over 100 synthetic personas.
- **Results / comparison**: Across **4,715 candidate assertions**, only **77.9%** of value/belief assertions are supported vs **96.2%** for everything else. A stricter bar on values alone cuts unsupported retentions **6.2% → 4.0% (≈36% relative)** and preserves an estimated **13 pp more coverage** (95% CI 9.8–16.0) than a global threshold at comparable retention.
- **Link**: https://arxiv.org/abs/2610.07100

### 2.3 Evaluation & measurement

#### 2.3.1 Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists
- **中文标题**: 我们在测量科学智能吗？重新思考 AI Scientist 的评估方式
- **Authors**: Kate Zhang, Yuante Li
- **Affiliation**: Carnegie Mellon University
- **Venue**: **NeurIPS 2026 Agentic AI for Biological Discovery Workshop (Oral)**
- **Problem background**: Scientific-agent benchmarks give a question + dataset and score the final answer against a fixed key — assuming the answer was derived from the data (**evidence grounding**). An agent can instead reach the key from **prior knowledge** or by elimination; a single run cannot distinguish these.
- **Key innovation**: Build controlled variants of each question's data files where the evidence is **intact / withdrawn / reversed**, verify each edit with a pre-registered reference statistic, run the same agent on every version, and compute **evidence-grounded accuracy** (credit only if the agent still answers when evidence is withdrawn *and* follows it when reversed).
- **Results / comparison**: 3 scaffolds × 5 models on 18 BAISBench single-cell questions + 4 GeneBench-Pro synthetics. Claude agents are **95% accurate** but answer **83% correctly with no data at all**; evidence-grounded accuracy is only **41%**. Hiding gene names raises the share of runs that follow reversed evidence **58% → 93%**. Benchmark scores and LLM judges can both reward answers that **ignore** changed evidence.
- **Link**: https://arxiv.org/abs/2610.04915

#### 2.3.2 Memory Depth and Reconstructed Context Width — A Controlled Evaluation of Hierarchical Retrieval
- **中文标题**: 记忆深度与重建上下文宽度：层次化检索的受控评估
- **Authors**: Michael Andreev
- **Affiliation**: Independent Researcher
- **Venue**: **PALM Workshop @ NeurIPS 2026**
- **Problem background**: Long-term conversational memory architectures keep proposing deeper structures (topics → events → graphs with causal/temporal links) without isolating whether **depth** or **context width** is what actually helps.
- **Key innovation**: Controlled sweep on **EverMemBench**: depths D1–D4 × core budgets 1,024/2,048/4,096 tokens + Production and Oracle conditions.
- **Results / comparison**: Width 1K→4K improves accuracy **+10.11 to +17.98 pp**; **depth shows no monotonic gain**. Beyond 8–16K, Production plateaus while **tokens per correct answer keep rising**; Oracle holds quality on full 68–71K archives. Argues for large coherent context blocks over progressively deeper memory.
- **Link**: https://arxiv.org/abs/2610.08300

#### 2.3.3 Quantization Effects on Tool-Failure Recovery Vary Across Prompts and Evaluation Designs
- **中文标题**: 量化对工具故障恢复的影响随提示词与评估设计而变
- **Authors**: Yuhe Hu
- **Affiliation**: Duke University
- **Venue**: **NeurIPS 2026 Workshop on SLMs for Agentic Systems (SLM-Agents)**
- **Problem background**: PTQ makes agents cheap to deploy, but claims about quantised-agent robustness are usually stated from **one prompt, one screened task set, one scoring policy**.
- **Key innovation**: Factorial re-evaluation of 8-bit vs 4-bit **Llama-3.1-8B-Instruct** and **Qwen2.5-7B-Instruct** on 20 deterministic tool-use tasks × 5 prompts, varying **evaluation target** and **executor leniency**.
- **Results / comparison**: On mutually clean-passing tasks the 8-vs-4-bit gap ranges **0 to +20.2 pp (Llama)** and **−50.0 to +35.0 pp (Qwen)**. The evaluation target alone can reverse the verdict: under one prompt, scoring each variant on its own clean tasks favours 4-bit by **+17.5**, scoring shared tasks gives 0, full-pipeline favours 8-bit by **+28.3**; re-scoring the same logs with strict output parsing turns **+28.3 into −15.0**. Methodological takeaway: matched tasks, full-pipeline success for deployment, stated scoring policy, uncertainty across tasks.
- **Link**: https://arxiv.org/abs/2610.07781

## 3. NeurIPS 2025 — carry-over (1 paper)

### 3.1 LLM Layers Immediately Correct Each Other
- **中文标题**: LLM 层与层之间在即时相互纠正
- **Authors**: Arjun Patrawala, Jiahai Feng, Erik Jones, Jacob Steinhardt
- **Affiliation**: University of California, Berkeley
- **Venue**: **NeurIPS 2025** (published)
- **Problem background**: Sparse-autoencoder interpretability is usually read as finding features that **persist** in the residual stream and that later layers build on.
- **Key innovation**: Identifies the **Transformer Layer Correction Mechanism (TLCM)** — adjacent layers systematically **counteract portions of each other's contributions** — present in **5 of 7** major open-source families, active on nearly all tokens, emerging during pretraining, strongest on contextually dependent tokens, with correction strength calibrated to the preceding layer's output. Layer-Jacobian analysis shows selective subspace correction → a **"propose-and-reject"** reading: layers propose candidate features, successors remove inappropriate ones.
- **Why it matters for the wiki**: explains three empirical oddities at once — **low-specificity SAE feature descriptions**, the need for **extreme amplification in steering**, and the **theoretical advantage of transcoders over SAEs**. Residual stream contains *transient proposals* alongside persistent features.
- **Link**: https://arxiv.org/abs/2609.07876

## 4. ICML 2026 (6 papers)

### 4.1 Training & adaptation

#### 4.1.1 HuatuoGPT-3 — RL-Only Domain Adaptation from Base Models (OnePO)
- **中文标题**: HuatuoGPT-3：从基座模型出发的纯 RL 领域适配（OnePO）
- **Authors**: Junying Chen, Xinyuan Xie, Ziniu Li, Wenyuan Gu, Jianquan Li, Xiang Wan, Guangjun Yu, Ruoyu Sun, Haizhou Li, Benyou Wang
- **Affiliation**: The Chinese University of Hong Kong, Shenzhen; Shenzhen Research Institute of Big Data; Shenzhen Loop Area Institute; National Health Data Institute
- **Venue**: **ICML 2026** (extended version of *OnePO*, with scaling to HuatuoGPT-3)
- **Problem background**: The dominant SFT+RL domain-adaptation pipeline gives a convenient cold start but **reduces exploration diversity** and adds multi-stage complexity; pure on-policy RL has a cold-start problem, and mixed-policy RL learns informative teacher tokens **too slowly early** and is **anchored by stale teacher output later**.
- **Key innovation**: Names those two failure modes **Gradient Starvation** and **Teacher-Distribution Anchoring**, then proposes **OnePO (One-stage Policy Optimization)**: teacher output is *transient guidance*, with **Adaptive Objective Evolution** (strengthen learning on informative low-probability teacher tokens) and **Teacher Retirement** (discard the teacher once policy surpasses it).
- **Results / comparison**: HealthBench (Total) **67.2** with only **20K samples**, beating SFT+RL by **+2.7** and pure RL by **+7.4**. Scaled to **HuatuoGPT-3**: 27B reaches **70.1** HealthBench Total and **71.4** Professional — stated to surpass **GPT-6 Astra**. Open weights + code.
- **Link**: https://arxiv.org/abs/2610.05966

#### 4.1.2 U-LoRA — Adaptive Utilization of Low-Rank Adaptation via Conditioned Gating
- **中文标题**: U-LoRA：通过条件门控自适应利用低秩适配子空间
- **Authors**: Guang Yang, Changhao Guan, Chao Huang, Yufeng Chen, Kaiyu Huang
- **Affiliation**: Key Laboratory of Big Data & Artificial Intelligence in Transportation (Beijing Jiaotong University), Ministry of Education; Beijing Jiaotong University
- **Venue**: **ICML 2026**
- **Problem background**: LoRA applies a **shared low-rank update across tokens**, under-using the adaptation subspace for tokens from different sequences.
- **Key innovation**: **Conditioned gating** produces per-token **utilisation coefficients along the low-rank directions**, coordinated by sequence-level context so patterns stay consistent within a sentence; a **bias-corrected EMA historical prior** suppresses batch-to-batch noise. Gains come from *better use of the existing subspace*, not from enlarging it.
- **Results / comparison**: Competitive with strong LoRA baselines and recent variants at **comparable parameter budgets** on mathematical-reasoning and NLU benchmarks (abstract reports parity rather than headline jumps).
- **Link**: https://arxiv.org/abs/2610.05800

### 4.2 Serving & systems

#### 4.2.1 MAPS — Memory-Aware Predictive Scheduling Framework for LLM Serving
- **中文标题**: MAPS：面向 LLM 服务的记忆感知预测式调度框架
- **Authors**: Tiancheng Zhang, Yulin Chen, Yunfeng Zhao, Shaoyuan Huang, Cheng Zhang, Xiaofei Wang
- **Affiliation**: Tianjin University (College of Intelligence and Computing; International Joint Institute); Tianjin University of Finance and Economics
- **Venue**: **ICML 2026**
- **Problem background**: With **prefill-decode disaggregation**, memory-bound decode instances sit in persistent load imbalance because **output lengths are unknown at arrival**.
- **Key innovation**: Device-assisted **speculative output-length prediction overlapped with cloud-side prefilling** (negligible latency), **uncertainty-aware calibration** producing output-length *upper bounds with target coverage*, and a **hierarchical global-local scheduler** that fixes inter-decoder queue build-up and intra-decoder head-of-line blocking.
- **Results / comparison**: On two real workloads × two LLMs, beats three SOTA systems: **−42.6% average end-to-end latency**, **up to −84.8% tail latency**.
- **Link**: https://arxiv.org/abs/2609.15359

#### 4.2.2 Compound AI System Reliability — A Failure Taxonomy and Resilience Pattern Catalog from 150 Production Incidents
- **中文标题**: 复合 AI 系统可靠性：来自 150 起生产事故的故障分类与弹性模式目录
- **Authors**: Rudrendu Kumar Paul, Sourav Nandy
- **Affiliation**: Boston University; University of Texas at Austin
- **Venue**: **AIWILD Workshop, ICML 2026** (camera-ready)
- **Problem background**: Compound-system failures emerge **at component boundaries**, not inside models: cascading errors, silent quality degradation that evades monitoring, and coordination failures producing wrong collective behaviour from correct parts.
- **Key innovation**: Taxonomy of **23 failure modes in 5 categories** (retrieval, generation, tool, orchestration, integration) built from **150 production incident reports** (open-source projects + anonymised enterprise deployments), each paired with a resilience pattern whose effect is **measured by controlled fault injection**.
- **Results / comparison**: Circuit breakers cut cascade propagation **−89%**; output quality gates catch **73%** of silent degradation before user impact; component isolation shrinks blast radius **−64%**; systems implementing ≥3 patterns reduce **MTTR −71%** vs unstructured monitoring. Taxonomy + catalogue released.
- **Link**: https://arxiv.org/abs/2610.02503

### 4.3 Multimodal safety & inference theory

#### 4.3.1 Understanding and Mitigating Token-Pruning-Induced Vulnerabilities in VLMs (SAP)
- **中文标题**: 理解并缓解视觉语言模型中 token 剪枝引发的安全漏洞（SAP）
- **Authors**: Shuailong Wang, Xinyu Lyu, Shengming Yuan, Jingkuan Song, Heng Tao Shen, Lianli Gao
- **Affiliation**: University of Electronic Science and Technology of China; Southwestern University of Finance and Economics; Tongji University; Shanghai Innovation Institute
- **Venue**: **ICML 2026**
- **Problem background**: Token pruning accelerates VLMs but its **safety** implications were unexamined.
- **Key innovation**: First comprehensive safety evaluation — most pruning strategies **degrade safety as the ratio rises**, while **Query-based Compression** behaves oppositely (extreme pruning to 99.8% *improves* safety). Identifies **Pruning-Induced Malicious Amplification**: removing background tokens forces attention to collapse onto a few retained **malicious anchors**, amplifying their toxic semantics under jailbreak. **SAP** (inference-time, plug-and-play): identify malicious anchors → restore pruned benign tokens → reallocate excess attention.
- **Results / comparison**: Across 3 safety + 4 utility benchmarks, **ASR reduced by up to 62%** with no efficiency or utility cost.
- **Link**: https://arxiv.org/abs/2610.09703

#### 4.3.2 Not All Answers Are Contextually Persuadable — Inference Dynamics under Contextual Influence
- **中文标题**: 并非所有答案都能被上下文说服：上下文影响下的推理动力学
- **Authors**: Zongye Hu, Weiqing Luo, Yanjie Fu, Yu Gan, Haofeng Zhang, Ziyi Huang
- **Affiliation**: Arizona State University; University of Maryland, College Park; **Morgan Stanley** (New York)
- **Venue**: **ICML 2026**
- **Problem background**: Prompting depends on contextual sensitivity, but inference behaviour under **strong contextual influence** is poorly understood below the output level.
- **Key innovation**: A theoretical framework analysing contextual influence through **inference dynamics** rather than output changes. Result: dynamics do **not** drift unboundedly — predictive representations converge to **stable, query-dependent regimes** that fundamentally constrain whether context can flip a prediction.
- **Results / comparison**: The headline implication: **repeated contextual assertions are not accumulating evidence** — repetition may *never* change a prediction, while in other cases a flip is inevitable. Theoretical predictions validated empirically.
- **Link**: https://arxiv.org/abs/2610.04791

## 5. ACL 2026 (3 papers)

### 5.1 SelFusion — Self-distillation for Diffusion Language Models
- **中文标题**: SelFusion：面向扩散语言模型的自蒸馏
- **Authors**: Hyeong Soo Lim, Jinyoung Kim, Eunseo Seo, Minho Jang, Jiwon Yoon
- **Affiliation**: Chung-Ang University (Department of Artificial Intelligence)
- **Venue**: **ACL 2026** (main conference paper)
- **Problem background**: DLMs cut AR latency but generate worse; naive **knowledge distillation yields marginal gains or degrades quality**.
- **Key innovation**: **Self-distillation without an external teacher**: two forward passes at different masking levels define an **easy mode** (low mask rate) and **hard mode** (high mask rate); because the easy mode can be *overconfident on wrong tokens*, **bidirectional KD** picks the distillation direction **per token by correctness**.
- **Results / comparison**: On instruction-following, beats KD with external LLM *and* DLM teachers; in many configurations the student **surpasses the LLM teacher**.
- **Link**: https://arxiv.org/abs/2608.22898 · code: https://github.com/scai-research/SelFusion_official

### 5.2 SCS — Focusing Condition: Inference-Time Self-Contrastive Steering for Conditional Text Embeddings
- **中文标题**: SCS：推理时自对比引导生成更聚焦的条件文本嵌入
- **Authors**: Zifeng Cheng, Lingyun Qian, Zhiwei Jiang, Cong Wang, Yafeng Yin, Fei Shen, Ao Zhou, Qing Gu
- **Affiliation**: State Key Laboratory for Novel Software Technology, Nanjing University; National University of Singapore
- **Venue**: **ACL 2026 (Oral)**
- **Problem background**: Prompt-based conditional embedding methods leave the conditional embedding **entangled with the general text embedding**, degrading quality.
- **Key innovation**: **Training-free, plug-and-play Self-Contrastive Steering** — modify attention mask and positional encodings to obtain an **unconditional** embedding, then subtract/refine the conditional one at inference; costs **one extra multi-head self-attention computation**.
- **Results / comparison**: Improves existing prompt-based methods across clustering, STS and triplet-alignment datasets, across different LLMs.
- **Link**: https://arxiv.org/abs/2609.32684

### 5.3 CaRL-EM — Cost-Aware Reinforcement Learning for Entity Matching with LLMs
- **中文标题**: CaRL-EM：基于 LLM 的实体匹配成本感知强化学习
- **Authors**: Chaohui Guo, Michel Klein, Zhisheng Huang
- **Affiliation**: Vrije Universiteit Amsterdam
- **Venue**: **ACL 2026 Main Conference**
- **Problem background**: LLM entity matching is either independent pairwise decisions or hand-built pipelines, and it **ignores inference cost at scale**.
- **Key innovation**: Formulates multi-candidate EM as a **cost-aware sequential decision problem**: an RL controller chooses among abstract operators — **Match / Compare / Select / Decide** — and model capacities to maximise a quality-cost objective. Because the policy interacts with **abstract operators**, the same controller can be **reused with different LLM backends without retraining**.
- **Results / comparison**: 7 benchmarks: learns to spend expensive operators only on complex items, **zero-shot transfers** across datasets/domains, and beats both strong LLM baselines and manual pipelines on the quality-cost frontier.
- **Link**: https://arxiv.org/abs/2609.01195

## 6. EMNLP 2026 & EMNLP 2025 (10 papers)

### 6.1 EMNLP 2026 — main / industry / findings (7)

#### 6.1.1 Verification Trap — Test-Time Selection Failures under False Premises in Code Generation
- **中文标题**: 验证陷阱：代码生成中错误前提下的测试时选择失败
- **Authors**: Feng He, Hejia Wang, Linghao Meng, Ming Gao, Qiankun Li
- **Affiliation**: University of Science and Technology of China; Beijing University of Posts and Telecommunications; National University of Singapore; Nanyang Technological University
- **Venue**: **EMNLP 2026**
- **Problem background**: Test-time compute (sample 64 candidates, let a verifier pick) **assumes the verifier's signal is independent of the generator**. Under a shared false premise that assumption fails.
- **Key innovation**: Names the failure mode **Verification Trap**: generator produces premise-consistent shortcuts, verifier writes tests that inherit the same blind spot, so the selector **picks a hidden-test-wrong candidate even when a hidden-test-correct program is in the pool**. Proposes a **gold-free predictor** from verifier-visible features, and evaluates two mitigation axes.
- **Results / comparison**: 3 benchmarks × 5 code models: false premises degrade first-sample correctness, reduce post-selection correctness at 64 samples, and amplify **recoverable mis-selection**. Predictor reaches **0.846 AUROC** before any hidden execution. **Coupled scaling gives limited recovery; premise-agnostic robustness auditors recover substantial oracle headroom.**
- **Link**: https://arxiv.org/abs/2610.05170

#### 6.1.2 APDMem — Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory
- **中文标题**: APDMem：查询自适应长期记忆的智能体控制渐进式披露
- **Authors**: Chin-Lun Fu, Anagha Kulkarni, Hong Ni, Behrouz Madahian
- **Affiliation**: **Machine Learning Center of Excellence, JPMorgan Chase & Co.**
- **Venue**: **EMNLP 2026 (Industry Track)**
- **Problem background**: Personalised assistants must recover **sparse evidence from long histories** across queries of very different complexity; flat stores and fixed retrieval granularity pay the same for easy and hard queries.
- **Key innovation**: Four progressively detailed layers — **thematic summaries → personalised key facts → turn-level evidence notes → raw messages** — read by a controller that **drills down only when needed**, plus a note synthesiser that consolidates facts, orders events and **flags contradictions**.
- **Results / comparison**: Strong LongMemEval performance while accessing only **8% of total conversations** — an explicit cost-fidelity dial (simple queries terminate early; temporal/multi-hop/exact-evidence queries go deep).
- **Link**: https://arxiv.org/abs/2610.02472

#### 6.1.3 NTRL-Code — Noisy Test-Time Reinforcement Learning for Code LLMs
- **中文标题**: NTRL-Code：面向代码 LLM 的含噪测试时强化学习
- **Authors**: Xikai Yang, Hieu Trung Nguyen, Dunyuan Xu, Yuzhi Zhao, Jinpeng Li, Wenao Ma, Pheng-Ann Heng
- **Affiliation**: The Chinese University of Hong Kong; Huazhong University of Science and Technology
- **Venue**: **EMNLP 2026**
- **Problem background**: Real user instructions are **vague and error-prone**, yet robustness fine-tuning needs costly **paired clean–noisy samples** and good noise simulation.
- **Key innovation**: Robust self-evolution from **unlabelled noisy data only**, at test time: **conservative self-denoising** for a cleaner semantic anchor, **AST-based structural aggregation** to build a proxy target from multiple candidate programs, and a hybrid reward (format validity + code similarity + anti-repetition) over the original noisy prompts.
- **Results / comparison**: Consistent gains on 3 benchmarks with character-, word- and paragraph-level perturbations, stabilising several base models.
- **Link**: https://arxiv.org/abs/2609.32172

#### 6.1.4 ReMCTS — Reflection-Enhanced Monte Carlo Tree Search for Code Generation
- **中文标题**: ReMCTS：面向代码生成的反思增强蒙特卡洛树搜索
- **Authors**: Huifei Wang, Xinying Huang, Yiheng Sun, Yifan Yuan
- **Affiliation**: Shenzhen University (College of Computer Science and Software Engineering)
- **Venue**: **EMNLP 2026**
- **Problem background**: Open-weight LLMs produce plausible candidates that still **fail hidden semantics** and **repeat the same mistakes across repair attempts**.
- **Key innovation**: Execution-grounded, **memory-augmented** MCTS: candidates as tree states, **branch-local debugging context**, **cross-branch failure-experience retrieval**, and an explicit distinction between *failed checks* and *unavailable evidence*.
- **Results / comparison**: On HumanEval + MBPP-Sanitized under held-out evaluation, improves over direct generation in **8 of 10 model-dataset pairs**; proxy-only search is less stable. A 30-task HumanEval-X C++ pilot shows compiler-backed compatibility (⚠️ explicitly *not* a broad multilingual claim). Ablations isolate tree-search / sampling / repair / memory contributions.
- **Link**: https://arxiv.org/abs/2609.34717

#### 6.1.5 SLBF — Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression
- **中文标题**: SLBF：数据无关的 MoE 压缩之共享低秩基分解
- **Authors**: Tianxiao Cao, Jiahe Shao, Yuning Qiu, Kyohei Atarashi, Hisashi Kashima, Qibin Zhao
- **Affiliation**: Kyoto University; The University of Tokyo; RIKEN AIP
- **Venue**: **Findings of EMNLP 2026**
- **Problem background**: MoE LLMs decouple capacity from compute but are expensive to store and serve; the three compression families — **expert pruning, expert merging, weight reconstruction** — had no principled comparison.
- **Key innovation**: Derives **structural error bounds** showing pruning and merging incur **non-vanishing errors tied to routing and expert heterogeneity**, while reconstruction avoids them. Proposes **SLBF**: data-free reconstruction with **rank-k bases shared across experts** (richer cross-expert sharing, faster convergence, lower error) plus a post-hoc **gauge fixing** that removes redundant parameters at no representational cost.
- **Results / comparison**: Across **five MoE architectures from 16B to 122B**, consistently beats methods from all three families.
- **Link**: https://arxiv.org/abs/2610.09342

#### 6.1.6 EpiWorld — Grounding LLM Policy Agents in Epidemiological World Models
- **中文标题**: EpiWorld：将 LLM 政策智能体锚定于流行病学世界模型
- **Authors**: Zeeshan Memon, Yiqi Su, Kai Shu, Naren Ramakrishnan, Liang Zhao
- **Affiliation**: Emory University; Virginia Tech
- **Venue**: **Findings of EMNLP 2026**
- **Problem background**: Epidemic intervention policies are **textual artefacts** humans interpret and revise — a natural LLM task — but a naive LLM lacks epidemic dynamics, quantitative surveillance signals, and institutional constraints.
- **Key innovation**: A **closed-loop framework**: an LLM policy actor grounded in a **learned action-conditioned epidemiological world model** (fast counterfactual rollouts of a candidate intervention) plus a **tiered skill library** of protocols, surveillance tools and **lessons distilled from after-action analysis** (protocols stay fixed, lessons accumulate → interpretable, controllable improvement).
- **Results / comparison**: World model attains the **best out-of-distribution Peak-MAE** among forecasting baselines on retrospective COVID-19 + influenza data; the closed loop cuts **cumulative hospitalisation up to −59%**, average **≈−16% across six LLM backbones**, beating RL and optimal-control policy baselines.
- **Link**: https://arxiv.org/abs/2610.02744

#### 6.1.7 Agentic AutoRAG — RAG Pipeline Optimization through Reasoning-Driven Agents
- **中文标题**: Agentic AutoRAG：由推理驱动智能体优化 RAG 流水线
- **Authors**: Lasse B. Strand, Robert Jakob, Kevin O'Sullivan, Markus Kreft
- **Affiliation**: ETH Zurich
- **Venue**: **REALM Workshop @ EMNLP 2026** + **ML for Systems Workshop @ NeurIPS 2026** (dual acceptance)
- **Problem background**: Configuring RAG is an expensive multi-objective HPO problem over chunking/embedding/reranking/generation; existing optimisers reduce each trial to **one aggregate score** and never model *why* it scored that way — even though retrieved chunks already show whether failure was retrieval or generation.
- **Key innovation**: An LLM-agent optimiser with **retrieval-vs-generation failure attribution**: a **Diagnoser** labels each failed question, a **Proposer** grounded in a knowledge base of model rankings and pricing selects the next configuration, tracing an **accuracy–cost Pareto frontier**.
- **Results / comparison**: On 3 multi-hop QA benchmarks, higher LLM-judge accuracy than every baseline, matching the statistical baselines' **full 30-trial accuracy within its first 10 trials**. On a real healthcare corpus: median exam accuracy **77% vs 71.5%** best baseline at **~58% of its cost/query**, and matches 71.5% at **~22% of the cost**.
- **Link**: https://arxiv.org/abs/2610.08452

### 6.2 EMNLP 2026 — workshops (2)

#### 6.2.1 Measuring the Serving Stack Instead of the Model — Hidden Confounds in Local Tool-Use Evaluation
- **中文标题**: 测量的是服务栈而非模型：本地工具使用评估中的隐藏混淆
- **Authors**: Lijuan Tang, Yuemeng Zheng
- **Affiliation**: Northeastern University (Seattle)
- **Venue**: **REALM Workshop @ EMNLP 2026**
- **Problem background**: A coding agent must emit a **parseable tool call** before the harness can act; if the *serving layer* silently blocks or rewrites that step, the measured "tool-use fidelity" is a **stack artifact**.
- **Key innovation**: Cross-stack probes (**Ollama, llama.cpp, vLLM, SGLang**) + harness tracing. In Ollama, a static per-model template flag gates `tools=`: some models return text, some native `tool_calls`, **Phi-3 and Gemma-3 are rejected before inference** — and rejection/retry-exhaustion are **not preserved as structured failure metadata**, so naive analysis reports **0% fidelity**.
- **Results / comparison**: Adding a text tool list recovers much of the measured fidelity for accepted models, while a uniform text protocol **hurts** Llama-3.2 (which has native support). Constrained decoding removes parse failures but can **non-terminate**; turn-pooled vs per-instance estimates differ by **up to ~55 points**. Ends with an evaluation checklist treating serving behaviour as part of the protocol.
- **Link**: https://arxiv.org/abs/2609.26693

#### 6.2.2 Predicting the Next State Is Not Enough — JEPA Representations for Lean Theorem Proving
- **中文标题**: 只预测下一状态还不够：用于 Lean 定理证明的 JEPA 表征
- **Authors**: Aarnav Choudhary
- **Affiliation**: University of California, Los Angeles
- **Venue**: **MathNLP Workshop @ EMNLP 2026**
- **Problem background**: Neural theorem provers must both **propose tactics** and **rank successor states**; is one-step Lean transition prediction a usable self-supervised signal for branch ordering?
- **Key innovation**: A JEPA-style model predicts latent successors and scores only **kernel-validated, non-terminal** successors from a fixed ByT5 proposer — a controlled design that **separates representation quality from proposal quality**, with kernel-checked proof completion as the primary endpoint.
- **Results / comparison**: JEPA wins the ranking diagnostic decisively (**Top-1 50.18% vs 31.55%** for matched InfoNCE) yet solves **282.3 / 987** theorems across seeds vs **308** for simple proposer ordering, while needing **more tactic checks**. Conclusion (a negative result worth keeping): **accurate one-step transition ranking is insufficient as a long-horizon search value.**
- **Link**: https://arxiv.org/abs/2609.32908

### 6.3 EMNLP 2025 — carry-over (1)

#### 6.3.1 Rethinking Sign Language Translation — The Impact of Signer Dependence on Model Evaluation
- **中文标题**: 重新思考手语翻译：签名者依赖性对模型评估的影响
- **Authors**: Keren Artiaga, Sabyasachi Kamila, Haithem Afli, Conor Lynch, Mohammed Hasanuzzaman
- **Affiliation**: ADAPT Centre, Munster Technological University; Manipal Institute of Technology Bengaluru (MAHE); Nimbus Research Centre, MTU; Queen's University Belfast
- **Venue**: **Findings of ACL: EMNLP 2025**
- **Problem background**: SLT evaluations typically let **signers overlap across train/dev/test**, so models may exploit signer-specific regularity instead of generalising.
- **Key innovation**: **Signer-fold cross-validation** on three leading gloss-free models (GFSLT-VLP, GASLT, SignCL) over CSL-Daily and PHOENIX14T, plus a sentence-overlap census.
- **Results / comparison**: Under signer-independent evaluation, PHOENIX14T collapses — GFSLT-VLP **BLEU-4 21.44 → 3.59**, ROUGE-L **42.49 → 11.89**; GASLT 15.74 → 8.26; SignCL 22.74 → 3.66. On CSL-Daily, identical sentences appear in **both** train and test for many items, so scores partly reward **sentence recall**. Recommends signer-independent, sentence-disjoint splits and reporting both protocols with overlap statistics.
- **Link**: https://arxiv.org/abs/2609.07965

## 7. ICLR 2026 (3 papers + 1 noted)

### 7.1 SSDi8 — Accurate and Efficient 8-bit Quantization for State Space Duality
- **中文标题**: SSDi8：面向状态空间对偶的准确高效 8-bit 量化
- **Authors**: Hyunwoo Kim, Byoungchan Ko, Minseok Kang, Minwoo Kim, Dongjin Lee, Jaehoon Lee, Sungroh Yoon, Dahuin Jung
- **Affiliation**: Chung-Ang University; Soongsil University; Seoul National University
- **Venue**: **ICLR 2026**
- **Problem background**: Mamba-2's **SSD** (recurrent + attention duality) expands memory and latency; compression had been designed for Transformers, not SSD's structure.
- **Key innovation**: The **first post-training quantisation framework for SSD** maintaining a **persistent INT8 path**: reformulation that **decouples element-wise from matrix multiplications** (so quantised activations are reused across modules), adaptive quantisation of channel-varying activations at cost-effective points, exploitation of SSD's **intrinsic dimensional decomposition** (different outlier distributions per axis) and a **per-channel error-correction term**.
- **Results / comparison**: Accuracy comparable to **FP16** with **up to 1.4× speedup** in W4A8 and W8A8; validated on an **Orin NX** edge device.
- **Link**: https://arxiv.org/abs/2608.21952

### 7.2 Conditioned Initialization for Attention
- **中文标题**: 注意力的条件化初始化
- **Authors**: Hemanth Saratchandran, Simon Lucey
- **Affiliation**: Australian Institute for Machine Learning, Adelaide University
- **Venue**: **ICLR 2026**
- **Problem background**: Q/K/V weights are initialised randomly or by mimicking/transfer heuristics; little work asks whether **initialisation biases the optimisation** of the attention layer itself.
- **Key innovation**: A principled scheme initialising attention weights to improve their **spectral properties** — theory shows it can reduce the **condition number of the attention Jacobian**, giving more stable optimisation.
- **Results / comparison**: Accelerated convergence and improved generalisation across vision and language applications; simple to plug into existing architectures (no architectural change).
- **Link**: https://arxiv.org/abs/2609.07086

### 7.3 Very Credible Auction
- **中文标题**: 极高可信度拍卖
- **Authors**: Thanawat Sornwanee
- **Affiliation**: Graduate School of Business, Stanford University
- **Venue**: **ICLR 2026 Workshop on AI for Mechanism Design and Strategic Decision Making**
- **Content**: Strengthens the *credible auctions* commitment notion into "**very credible**" auctions, argued to suit modern digital applications. ⚠️ **Single-source, one-sentence abstract** — contribution detail not recoverable from the record; treat as *(tentative)*.
- **Link**: https://arxiv.org/abs/2609.14263

> **Also noted (not featured):** *Temporal Geometry of Deep Networks* `2610.03000` (**ICLR 2026 main**, Jheronimus Academy of Data Science / TU Eindhoven) — hyperbolic (Poincaré) embeddings of **temporal parameter graphs** for intrinsic MLP explainability; retained here as a venue-index entry because it sits outside the wiki's core categories.

## 8. AAAI 2026 (1 paper)

### 8.1 WorldAgen — Unified State-Action Prediction with Test-Time World Model Training
- **中文标题**: WorldAgen：统一的状态-动作预测与测试时世界模型训练
- **Authors**: Chi Wan, Kangrui Wang, Yuan Si, Pingyue Zhang, Manling Li
- **Affiliation**: *(affiliation not recovered — the arXiv HTML author block carries no affiliation markup)*
- **Venue**: **AAAI 2026**
- **Problem background**: VLA models that combine world modelling with action prediction are trained on **static datasets** with **no deployment-time adaptation**, so they fail under novel object configurations or shifted dynamics.
- **Key innovation**: One shared Transformer backbone with two heads — a **world-model head** (future states from state-action history) and an **agent-model head** (actions from instructions) — separated by a **Mixed Unidirectional Attention Mask**; at test time the model **samples exploratory actions, observes real transitions, and runs lightweight Test-Time Training** updates on the world-model head.
- **Results / comparison**: Baseline is comparable to or better than SOTA on **CALVIN and LIBERO**; with TTT on a small number of samples it **surpasses existing SOTA**.
- **Link**: https://arxiv.org/abs/2609.08162

## 9. KDD 2026 (3 papers)

### 9.1 CEDAR — Controlled and Event-Driven Demand Forecasting via Residual Decomposition
- **中文标题**: CEDAR：通过残差分解实现受控的事件驱动需求预测
- **Authors**: Junjie Meng, Ranxu Zhang, Zi-an Zhang, Shujun Liu, Xiaoning Qi, Xiaozhou Xu, Yanyong Zhang, Hui Xiong, Chao Wang
- **Affiliation**: University of Science and Technology of China; **Alibaba Group** (Hangzhou); The Hong Kong University of Science and Technology (Guangzhou) / HKUST
- **Venue**: **KDD 2026**
- **Problem background**: E-commerce merchants need forecasting to support **planning over future action sequences** (budget schedules), but existing TSF is **passive**: covariates are fitted by correlation under *historical* policy, giving **autoregressive inertia** and **policy-insensitive rollouts** unusable for counterfactuals.
- **Key innovation**: Two-stage **decision-conditioned simulation** — Stage I **Action-Interleaved Transformer** learns controllable action-conditioned state transitions for intervention rollouts; Stage II **Residual Correction** uses external event signals with **LLM-assisted text representations** to align noisy event descriptions to product context and correct event-driven deviation.
- **Results / comparison**: Enabled by a new **Alibaba 1688** dataset of **~32 million product trajectories** (state-action pairs + aligned event signals). Improves over strong TSF baselines offline **and in online controlled production experiments**, delivering budget-planning gains.
- **Link**: https://arxiv.org/abs/2608.25871

### 9.2 ProtoCP — Temporal Graph Prototype-conditioned Conformal Prediction for Fraud Detection
- **中文标题**: ProtoCP：面向欺诈检测的时序图原型条件化共形预测
- **Authors**: Xudong Chen, Shengbo Gong, Lu Cheng, Wei Jin
- **Affiliation**: Emory University; University of Illinois at Chicago
- **Venue**: **KDD 2026**
- **Problem background**: Edge-level fraud detection wants distribution-free coverage guarantees, but vanilla graph conformal predictors give **inefficient (too-large) prediction sets**: fraud sits in benign-dominated neighbourhoods that dilute calibration, and extreme class imbalance makes class-conditional thresholds over-conservative.
- **Key innovation**: **Learned prototypes** suppress benign-dominated noise in the calibration context; a **neighbourhood-relative score with temporal score diffusion** yields stable class-conditional calibration under imbalance and drift.
- **Results / comparison**: Hits target coverage with **consistently smaller prediction sets** than SOTA on YelpChi, S-FFSD, FTFD, BankSim.
- **Link**: https://arxiv.org/abs/2608.15768

### 9.3 REFINE — Trajectory Representation Learning via Closed-Loop Transcription (extended version)
- **中文标题**: REFINE：基于闭环转写的轨迹表征学习（扩展版）
- **Authors**: Sean Bin Yang, Ying Sun, Jilin Hu, Zongyi Xu, Kristian Torp, Hua Lu, Bin Yang, Christian S. Jensen
- **Affiliation**: Aalborg University; Chongqing University of Posts and Telecommunications; East China Normal University
- **Venue**: **KDD 2026** (extended version of the KDD 2026 paper)
- **Problem background**: Self-supervised trajectory representation learning is **open-loop**: fixed augmentations or random masking with **no feedback**, limiting generalisation and scale.
- **Key innovation**: Draws on **feedback control theory** — couples road-network-aware **generative reconstruction** with **feedback-driven contrastive learning** (no hand-designed augmentation views), with a control-theoretic **convergence guarantee** for the closed-loop optimisation.
- **Results / comparison**: Outperforms SOTA across multiple downstream tasks on **four real-world datasets** while remaining efficient and scalable.
- **Link**: https://arxiv.org/abs/2609.07206

## 10. CVPR 2026 (1 paper)

### 10.1 MIOH — Fine-Grained Multi Image Object Hallucination Benchmark
- **中文标题**: MIOH：细粒度多图像物体幻觉基准
- **Authors**: Joonki Min, Chaeyun Kim, Hyungwook Choi, Yejin Kim, Kihyun Kim, Yohan Jo, Joonseok Lee
- **Affiliation**: Seoul National University; AIM Intelligence
- **Venue**: **CVPR 2026**
- **Problem background**: MLLMs in multi-image settings still hallucinate objects; existing benchmarks are single-image or only give high-level multi-image scores, so they cannot show **which visual complexity or reasoning demand triggers** the hallucination.
- **Key innovation**: A controlled benchmark crossing **4 foundational tasks** (existence, counting, attribute, position) × **3 multi-image reasoning patterns** (comprehensive, comparative, selective) × **3 adversarial pressures** (visual context scale, perceptual difficulty, contextual bias).
- **Results / comparison**: **29 models** evaluated; even **GPT-5 and Gemini-2.5-Pro** show distinct failure patterns per pattern/task. Diagnosis: hallucination stems less from perception than from **integration-stage limits when maintaining object representations across images**.
- **Link**: https://arxiv.org/abs/2608.30653

## 11. RecSys 2026 (2 featured; 1 withdrawn as collision)

### 11.1 DeepAffinity — Long-Term Aspect Preference Prediction in eCommerce using Small Language Models
- **中文标题**: DeepAffinity：用小型语言模型预测电商长期品类属性偏好
- **Authors**: Yotam Eshel, Guy Hadad, Guy Feigenblat, Yuri M. Brovman, Matt Gearhart, Bracha Shapira
- **Affiliation**: **eBay Inc.**; Ben-Gurion University; DREAM group
- **Venue**: **RecTemp @ ACM RecSys 2026** (workshop)
- **Problem background**: Predicting preference for product **aspects** (brand, size, colour) — defined here as **Aspect Affinity** — needs *long-term* preference from ordered history, beyond the current session.
- **Key innovation**: Frames aspect affinity as a **temporal prediction task** solved with **SLMs + structured prompts + specialised prediction heads** fine-tuned for the task (rather than generative fine-tuning).
- **Results / comparison**: Outperforms standard generative fine-tuning; general-purpose open-source LLMs **perform poorly without task-specific tuning**; improves recommendation quality on a **large-scale multinational eCommerce platform**.
- **Link**: https://arxiv.org/abs/2609.02468

### 11.2 Multi-Source Ensemble for Candidate Generation of Alternative Vacation Rental Recommendations
- **中文标题**: 度假租赁替代房源推荐的多源集成候选生成
- **Authors**: Syed Mohammed Arshad Zaidi, Eric Rincon, Shayan Hassantabar
- **Affiliation**: *(affiliation not recovered — no affiliation markup in the arXiv HTML author block)*
- **Venue**: **RecTour 2026** (Workshop on Recommenders in Tourism, co-located with ACM RecSys 2026)
- **Problem background**: Alternative-listing recommendation faces heterogeneous inventory, geographic constraints, fast-changing availability and a **long tail** — and the choice of candidate generator is usually judged only at the CG stage.
- **Key innovation**: Systematic comparison of collaborative filtering, shallow embeddings and GNNs on a platform with **2M+ active properties**, then a **hybrid architecture**: item-based CF for properties with rich interaction history + **GNN retrieval** for diversity and cold start. Explicitly tracks **how CG gains propagate to ranking**.
- **Results / comparison**: Hybrid improves **Recall@300 by +14.8%** over the strongest baseline; GNN embeddings alone beat shallow Hotel2Vec by **48–68% relative recall** across K. Documents the **recall-conversion gap** — stronger candidate pools yield better downstream ranking, but attribution is confounded by ranker retraining.
- **Link**: https://arxiv.org/abs/2609.05748

> **Withdrawn:** **BAFF** `2609.08725` (Dable Inc., OARS @ RecSys 2026) was already covered by `wiki/synthesis/2026-10-04/arxiv-paper-check.md` — see §16.

## 12. CIKM 2026 (3 papers)

### 12.1 CodeGraph — Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding
- **中文标题**: CodeGraph：带 Wikidata 锚定的源代码开放分类知识图谱
- **Authors**: Federico Pennino, Andrea Gurioli, Stefano Zacchiroli, Maurizio Gabbrielli, Paolo Ferragina
- **Affiliation**: Università di Bologna (DISI); LTCI, Télécom Paris, Institut Polytechnique de Paris; Sant'Anna School of Advanced Studies, Pisa
- **Venue**: **CIKM 2026**
- **Problem background**: Billions of public source files encode engineering knowledge (algorithms, paradigms, patterns, domains) that existing tools can only mine at **syntactic/token level**.
- **Key innovation**: A pipeline using a **code-specialised LLM** to extract entities, grounded in Wikidata by a **three-stage linker** — deterministic SPARQL for unambiguous entities → a **Deep Research Agent** for the long tail → **hierarchy roll-up** importing parent-of closures — plus a **calibrated QA protocol** (small human gold set × LLM-as-judge filter).
- **Results / comparison**: Applied to **167M files** of the Stack-Edu corpus: **~158M nodes** (145M files, ~63,000 concept entities, ~19,800 grounded Wikidata entities), **~1B typed edges**, **14 programming languages** — the first known large-scale open-taxonomy code KG.
- **Link**: https://arxiv.org/abs/2609.29474

### 12.2 MWMixer — Recovering Lost Details: Multi-Scale Frequency Compensation for Long-Term Time Series Forecasting
- **中文标题**: MWMixer：长期时间序列预测中的多尺度频率补偿与细节恢复
- **Authors**: Runmin Zou, Siyi Xie, Yaohui Huang, Yun Wang
- **Affiliation**: Central South University
- **Venue**: **CIKM 2026**
- **Problem background**: Multi-scale forecasting **downsamples**, smoothing away fine temporal fluctuations, and then further biases representation toward dominant trends.
- **Key innovation**: **Bidirectional Frequency-Bands Mixing** (wavelet-based) to recover lost detail across scales, a **Dynamic Scale-Adaptive Fusion** module with time-varying weights, plus a **cross-scale consistency loss** (coarse prediction ≈ interval-averaged fine outputs) and multi-scale supervision.
- **Results / comparison**: Competitive long-term forecasting performance on **seven real-world datasets**.
- **Link**: https://arxiv.org/abs/2609.24229

### 12.3 EVOL — Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation
- **中文标题**: EVOL：模拟器引导的进化式专家合成实现免部署学习路径推荐
- **Authors**: Geonwoo Bang, Dongho Kim, Moohong Min
- **Affiliation**: Sungkyunkwan University (Immersive Media Engineering / Computer Education)
- **Venue**: **CIKM 2026**
- **Problem background**: RL for learning-path recommendation commits to a sequence of L concepts with **reward only at the end** (super-exponential search growth), and the natural cure — expert demonstrations — **does not exist** in educational data (logs record what learners *did*, not what they *should* do).
- **Key innovation**: Imports **simulator-based demonstration learning** from robotics: the **knowledge-tracing simulator** is used (a) to synthesise per-learner expert paths by **evolutionary search** and (b) to train a **deployment-free policy** distilling them. Instantiated with an **asymmetric actor-critic** — the actor plans blind (deployment-realistic), the critic exploits privileged simulator state in training.
- **Results / comparison**: Beats **8 baselines** (heuristic, sequential, RL, graph-enhanced RL, LLM-enhanced) on ASSIST15, Junyi, EdNet (39–189 concepts) at L = 5/10/20; comparing BC/AWR/DAPG shows final performance is governed by **evolutionary expert quality**, not the imitation objective.
- **Link**: https://arxiv.org/abs/2610.03273

## 13. AAMAS 2026 (1 paper)

### 13.1 Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination
- **中文标题**: 分布式多智能体协调中对 LLM 智能体的符号化引导
- **Authors**: Ben Rachmut, Ning Zhang, Yevgeniy Vorobeychik, William Yeoh
- **Affiliation**: Washington University in St. Louis
- **Venue**: Preliminary version in **AAMAS 2026** (extended abstract)
- **Problem background**: Granting LLM agents full reasoning autonomy in distributed coordination protocols leads to **inconsistent or degraded performance** in complex domains (AgentsNet benchmark).
- **Key innovation**: A **Symbolic Guidance Taxonomy (SGT)** spanning a autonomy spectrum — open-ended NL reasoning → partial pseudocode → fully prescribed algorithmic execution — to test how much autonomy regulation helps.
- **Results / comparison**: **Intermediate autonomy levels consistently beat both unguided agents and fully prescriptive specifications** — autonomy regulation, not maximal freedom or maximal control, is the design principle.
- **Link**: https://arxiv.org/abs/2609.31963

---

## 14. Declared Vacancies & Thin Venues

| Venue | Result in window | Note |
|---|---|---|
| **SIGIR 2026** | **0 hits** | No in-window paper carries a SIGIR 2026 tag; the venue was swept (keyword + category + affiliation queries). Vacancy recorded, not silently omitted. |
| **WWW 2026** | **0 hits** | Candidate strings surfaced only **false positives** (title/abstract matches, not `comment`/`journal_ref` tags). |
| **CIKM 2025** | **0 hits** | CIKM hits in-window are all **2026**. |
| **RecSys 2025** | **0 hits** | RecSys hits in-window are all **2026** (2 featured + 1 withdrawn). |
| **NeurIPS 2025** | thin — 8 unclaimed in pool, **1 featured** | Most NeurIPS 2025 volume is already wikied from earlier runs. |
| **EMNLP 2025** | thin — **1 featured** | `2609.07965` (Findings). |
| **ICLR 2025 / KDD 2025** | 2 unclaimed each, **0 featured** | Below the selection bar this window (older, less in-scope). |

## 15. Venue Index

| Venue | Papers featured |
|---|---|
| **NeurIPS 2026** (main) | SkillForge `2610.09832`; Self-Consuming w/ Co-Evolving Preferences `2610.09415`; EpicWorldModel `2610.05996`; MaRK `2610.09092` (journal-ref; main-vs-workshop *(tentative)*) |
| **NeurIPS 2026** (workshops) | FEAgent `2610.04371` (Verifiable Coding, AWS); AppWorld/WorkArena blind spots `2610.09142`; Not Self-Decidable `2610.04699`; per-call-site SLM eval `2610.09021`; STEPGATE `2610.07816`; category-conditioned retention `2610.07100` (Social Agent, Meta AI); scientific-intelligence eval `2610.04915` (Agentic AI for Bio Discovery, **Oral**); memory depth `2610.08300` (PALM); quantization × tool recovery `2610.07781` (SLM-Agents) |
| **NeurIPS 2025** | TLCM `2609.07876` |
| **ICML 2026** | HuatuoGPT-3/OnePO `2610.05966`; U-LoRA `2610.05800`; MAPS `2609.15359`; Compound AI Reliability `2610.02503` (AIWILD); SAP token-pruning safety `2610.09703`; contextual persuadability `2610.04791` |
| **ACL 2026** | SelFusion `2608.22898`; SCS `2609.32684` (**Oral**); CaRL-EM `2609.01195` |
| **EMNLP 2026** (main/industry/findings) | Verification Trap `2610.05170`; APDMem `2610.02472` (Industry, JPMorgan); NTRL-Code `2609.32172`; ReMCTS `2609.34717`; SLBF `2610.09342` (Findings); EpiWorld `2610.02744` (Findings) |
| **EMNLP 2026** (workshops) | Agentic AutoRAG `2610.08452` (REALM + NeurIPS ML4Sys); serving-stack confounds `2609.26693` (REALM); JEPA Lean `2609.32908` (MathNLP) |
| **EMNLP 2025** | Sign-language signer dependence `2609.07965` (Findings) |
| **ICLR 2026** | SSDi8 `2608.21952`; Conditioned Initialization `2609.07086`; Very Credible Auction `2609.14263` (workshop) · *noted:* Temporal Geometry `2610.03000` |
| **AAAI 2026** | WorldAgen `2609.08162` |
| **KDD 2026** | CEDAR `2608.25871` (Alibaba/USTC); ProtoCP `2608.15768`; REFINE `2609.07206` |
| **CVPR 2026** | MIOH `2608.30653` |
| **RecSys 2026** | DeepAffinity `2609.02468` (RecTemp, eBay); vacation-rental CG `2609.05748` (RecTour) |
| **CIKM 2026** | CodeGraph `2609.29474`; MWMixer `2609.24229`; EVOL `2610.03273` |
| **AAMAS 2026** | Symbolic Guidance `2609.31963` |
| **SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025** | *(no in-window hit — §14)* |

## 16. Dedup Collisions & Withdrawn Candidates

> Four of the 52 selected candidates were **withdrawn, not merged** (same precedent as the 10-07 and 10-08 sibling runs).

| ID | Paper | Venue | Claimed by |
|---|---|---|---|
| `2610.09624` | Tool-call vector shaped by suppression | NeurIPS 2026 main poster | `wiki/synthesis/2026-10-08/arxiv-ai-search.md` (same-day) |
| `2610.10087` | MoSDOT — support-preserving distillation for offline MARL | NeurIPS 2026 main poster | `arxiv-ai-search.md` + `game-rl-daily.md` (same-day) |
| `2610.10274` | COSTGRAD — sparse planning in visual world models | NeurIPS 2026 | `game-rl-daily.md` (same-day, §3) |
| `2609.08725` | BAFF — bid-aware filter family for RTB A/B tests | OARS @ RecSys 2026 | `wiki/synthesis/2026-10-04/arxiv-paper-check.md` (prior-wiki, missed by the run-start baseline → **baseline-construction defect recorded in §17**) |

## 17. Cross-Cutting Observations

1. **"The measurement is the bug" is this window's dominant thesis.** Seven papers across six venues independently find that a trusted instrument measures something adjacent to its claim *and ship a substitute*: evidence-grounded accuracy (41% vs 95%), verifier mutation audits (6/15, 21/23), label adjudication (18.0% EquiBench, 28.4% SWE-bench patches), signer-independent SLT (BLEU 21.44→3.59), the Verification Trap (0.846 AUROC pre-detection), serving-stack fidelity (±55 pt), and quantization verdicts that flip with the scoring policy. **Fifth consecutive day** the wiki has logged metric-adjacent failures — see the `arxiv-ai-search` §5.4 thread; this batch is strong enough to justify a dedicated synthesis page.
2. **Company-authored work is concentrated in exactly the layers academia under-serves**: memory write-gates (Meta), code-equivalence audit trails (AWS), SSM conditioning certificates (NVIDIA), demand simulation with online A/B (Alibaba), hierarchical memory at query time (JPMorgan), temporal preference heads (eBay).
3. **Negative and null results are being published deliberately**: JEPA ranking wins Top-1 yet *loses* solved theorems; intermediate symbolic guidance beats both extremes of autonomy; depth in memory hierarchies gives no monotonic gain; repetition of context is not accumulating evidence. Four of these are "X is insufficient" claims, the most reusable kind of wiki claim.
4. **Agent orchestration has converged on *step-level* decisions** — when to escalate (STEPGATE), which call site deserves which model (per-call-site eval), which memory layer to disclose (APDMem), which skills to retire (SkillForge) — while the *verification* half of the field is still arguing about who is allowed to decide what is checkable (`Not Self-Decidable`).
5. **Venue hygiene**: **16 of 47** papers are **workshop** acceptances (NeurIPS×9, EMNLP×3 — REALM×2 + MathNLP×1, RecSys×2, ICML AIWILD×1, ICLR×1; one of them, Agentic AutoRAG, is dual-accepted at a NeurIPS workshop too); **31** are main/industry/Findings-track. Exactly **2 carry-overs** are from 2025 venues (NeurIPS 2025, EMNLP 2025 Findings). Self-reported venue tags were **not** verified against proceedings.

## 18. Method Notes & Caveats

- **Coverage is venue-tag-complete within the query set, not arXiv-exhaustive.** 47 queries: **25 venue `comment`-sweeps are unbounded** (arXiv returns the newest ~200 matching that tag — the mid-August KDD/CVPR/ACL hits came from these) and the **category/topic/lab sweeps are bounded** to `submittedDate:[202609250000 TO 202610082359]`, all with `max_results` caps. Papers carrying a venue tag but **older than what the unbounded sweeps returned, or landing outside the date-bounded queries, would be missed**. The published-date census of the featured set (§1–§13) spans **2026-08-16 → 2026-10-07**.
- **Venue tags are self-reported** in `comment`/`journal_ref` and were **not** verified against proceedings. Where the comment distinguishes main vs workshop vs oral, the distinction is stated; `2610.09092` (MaRK) has **no comment at all** — its NeurIPS tag comes from `journal_ref` and main-vs-workshop is marked *(tentative)*.
- **Affiliation discipline.** All affiliations read from the paper's own arXiv HTML author block; **no inference** from surnames or email domains. **Two featured entries are marked *(affiliation not recovered)*** — WorldAgen `2609.08162` and the vacation-rental CG study `2609.05748` (both have author blocks with no affiliation markup). Separately, the HTML endpoint returned **404 for `2608.24040` (PinSieve, KDD 2026 workshop)**, which was therefore **dropped from the candidate set entirely** rather than guessed at.
- **Baseline defect (recorded, not hidden).** The run-start claimed-ID baseline (8,133) **missed `2609.08725`**, which has been in `wiki/synthesis/2026-10-04/arxiv-paper-check.md` since 10-04 — the extraction evidently ran before that file was indexed or on a narrower glob. It was caught by the pre-write live re-sweep. Follow-up: rebuild baselines from `git ls-files wiki` rather than a cached regex pass.
- **Same-day race.** Between harvest (10:31) and writing (11:45), three sibling jobs committed (`arxiv-ai-search` 10:56, `game-rl-daily` 11:38, `investment-daily`); the live re-sweep withdrew 3 further IDs. Fourth consecutive day with this failure mode → the standing follow-up (**shared claimed-ID lock file before drafting**) is hereby re-affirmed.
- **Temp files** (Atom XML `pool.jsonl`, `rows.json`, `claimed.txt`, `details.txt`, `full.json`, parser scripts) written to `/var/folders/…/T/opencode/conf1008/` (pre-authorized scratch), deleted after writing. No writes outside that directory and the wiki.

## References

- arXiv export API: https://export.arxiv.org/api/query
- NeurIPS 2026: https://neurips.cc/virtual/2026/
- ICML 2026: https://icml.cc/virtual/2026/
- ACL 2026 / EMNLP 2026: https://2026.emnlp.org/
- ICLR 2026: https://iclr.cc/
- AAAI 2026: https://aaai.org/conference/aaai/aaai-26/
- KDD 2026: https://kdd2026.kdd.org/
- CVPR 2026: https://cvpr.thecvf.com/
- ACM RecSys 2026: https://recsys.acm.org/recsys26/
- CIKM 2026: https://cikm2026.org/
- AAMAS 2026: https://aamas2026.org/
