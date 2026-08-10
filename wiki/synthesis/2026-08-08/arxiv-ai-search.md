---
title: arXiv AI Research Search — August 8, 2026
type: synthesis
created: 2026-08-08
updated: 2026-08-08
sources: [arxiv-listing, arxiv-abstract-pages]
tags: [arxiv, ai, llm, reasoning, rl, agents, skill-reuse, retrieval, mechanism-design, game-theory, ai-governance, conversational-commerce, weather-forecasting, daily-digest]
---

# arXiv AI Research Search — 2026-08-08

> Search window: arXiv new submissions Aug 5–6, 2026 (IDs ~2608.05150–2608.06380). arXiv announces new listings Mon–Fri; there is **no Sat Aug 8, 2026 announcement**, so this scan is a **zero-overlap, uncovered-paper curation of the same Fri Aug 7 batch**. Streams scanned: cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.HC, cs.SE. The arXiv export API was intermittently rate-limited (HTTP 429), so all metadata was verified against individual abstract pages (`citation_date` meta tags) and cross-checked against the [Aug 7 AI scan](../2026-08-07/arxiv-ai-search.md), the [Aug 7 digest](../2026-08-07/arxiv-daily.md), and the [Aug 8 daily digest](arxiv-daily.md).
>
> 10 papers curated, **all NEW** (no prior wiki coverage, verified by grep on arXiv ID across wiki/index.md, wiki/log.md, and wiki/synthesis/**). Zero overlap with the Aug 7 scan (17 papers), Aug 7 digest (26), Aug 8 digest (21), or Aug 6 outputs.

## Overview table

| # | Paper | Domain | Institution / Company | arXiv | Status |
|---|-------|--------|----------------------|-------|--------|
| 1 | OPD²: On-Policy Delta Distillation for Multilingual Math Reasoning | LLM post-training | NAVER AI Lab | 2608.05802 | **new** |
| 2 | KV-Skill: Forging Expertise in the Model's Native Language | LLM skill / parameter-efficiency | (not stated) | 2608.05475 | **new** |
| 3 | CIPO: Contextual Information Policy Optimization for Search Agents | Agents / RL reasoning | (not stated; tentative BUAA) | 2608.06128 | **new** |
| 4 | EcoAgent-Bench: Economic Decision-Making in Budget-Constrained LLM Agents | Agents / evaluation | (not stated) | 2608.05519 | **new** |
| 5 | SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse | Agents / auditability | (not stated) | 2608.05204 | **new** |
| 6 | CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents | Coding agents / retrieval | (not stated) | 2608.05886 | **new** |
| 7 | Resourced Authority: Participatory Governance of Deployed AI Agents | Mechanism design / AI governance | Atria University / IIIT Hyderabad / IIT Hyderabad | 2608.06353 | **new** |
| 8 | Fair and Efficient Balanced Allocations for Additive Valuations | Mechanism design / fair division | University of Toronto | 2608.06325 | **new** |
| 9 | Cleo: Transparent and Controllable Chatbot for Conversational Commerce | Conversational search / IR | (not stated; tentative FIZ Karlsruhe) | 2608.06068 | **new** |
| 10 | GEM-3: Timestep-Conditioned Transformers for Global Weather Forecasting | Applied ML / weather | Salient (salientpredictions.com) | 2608.06241 | **new** |

---

## 1. LLM Reasoning, RL & Post-Training

### 1.1 OPD²: On-Policy Delta Distillation for Multilingual Math Reasoning

- **arXiv**: [2608.05802](https://arxiv.org/abs/2608.05802) (cs.CL / cs.LG; submitted 2026-08-06) — **NEW**
- **Authors**: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- **Institution**: NAVER AI Lab (high confidence — well-known affiliation of all authors)
- **Abstract (faithful summary)**: On-Policy Distillation (OPD) is emerging as a promising alternative to RL for LLM post-training, but its effectiveness in multilingual settings is underexplored. The authors study OPD and its advanced variant **OPD² (On-Policy Delta Distillation)** for mathematical reasoning in **English, Korean, and Japanese**. OPD² improves on OPD by using the **probability gap between a post-trained teacher and its base model** as the learning signal. Experiments with Qwen3 show OPD² consistently outperforms the original OPD, with particularly strong gains in Korean and Japanese, and generally narrows the English–Korean performance gap. A further finding: **English-only OPD** can also improve Korean and Japanese performance, but often **shifts responses toward English**, highlighting the importance of multilingual data for preserving target-language responses.
- **Key innovations**: (1) First systematic study of on-policy self-distillation under multilingual data; (2) the probability-gap (delta) teacher/base signal transfers better cross-lingually; (3) documents a language-shift failure mode of monolingual OPD.

### 1.2 KV-Skill: Forging Expertise in the Model's Native Language

- **arXiv**: [2608.05475](https://arxiv.org/abs/2608.05475) (cs.CL; submitted 2026-08-05) — **NEW**
- **Authors**: Zhaowei Han, Xiang Zhang, Bing Han, Kai Liu, Danqi Hu, Jie Liu
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Task knowledge is usually stored either as text in the prompt (modular but re-interpreted every use) or as weight updates (capable but hard to load, remove, or share). KV-Skill introduces a design space of **external factorized operators** that a **frozen** language model reads through a lightweight interface. Two complementary paths: **Registration** converts an authored text skill into a text-derived operator with a shared per-backbone interface; **reward learning** develops a compact latent operator directly from task outcomes, with or without an authored skill. Neither path adds positions to the prompt. Across ten benchmarks and four backbones from three model families, converting text to a KV-Skill consistently makes the same procedural knowledge more effective — e.g. on Qwen3.5-4B LiveMath, registration reaches 77.2 accuracy vs 23.4 for the source text skill, 52.0 for SkillOpt, and 64.5 for SoftSkill. Under matched reward training and parameter budgets, KV-Skill wins seven of eight matched settings against soft prefixes, prefix tuning, and LoRA. A rank analysis shows text-derived operators retain nearly all benefit with one task-aligned direction per injection layer, while matched random directions fail. One shared interface retains three independently loadable KV-Skills without measurable forgetting.
- **Key innovations**: (1) External, loadable/removable skill operators for frozen backbones — a middle ground between prompting and fine-tuning; (2) text-to-operator registration plus outcome-based latent operator learning; (3) loadable skills without cross-skill forgetting.

---

## 2. Agents, Skills & Tool Use

### 2.1 CIPO: Contextual Information Policy Optimization for Search Agents

- **arXiv**: [2608.06128](https://arxiv.org/abs/2608.06128) (cs.AI; submitted 2026-08-06) — **NEW**
- **Authors**: Xingyu Guo, Wei Chen, Linlin Yang, Baochang Zhang
- **Institution**: Not stated on abstract page. Co-author Baochang Zhang is affiliated with Beihang University (tentative; single-source).
- **Abstract (faithful summary)**: Search agents extend LLMs beyond static parametric memory by acquiring and using external evidence during multi-step reasoning. Reliability depends not just on retrieving relevant evidence but on **using it to guide subsequent reasoning** — yet existing methods reward final-answer correctness or intermediate progress without directly assessing whether post-retrieval actions are grounded in retrieved evidence. This misalignment encourages **prior-driven reasoning**: agents form conclusions from internal knowledge and use retrieval mainly to confirm them, producing confirmation bias and inefficient search. CIPO is an evidence-oriented RL framework that explicitly aligns policy optimization with external evidence use: it assigns **dense, turn-level credit** to reasoning actions influenced by retrieved information, and combines this evidence-use signal with a **global outcome reward**. This discourages evidence-detached guesses and promotes trajectories where retrieved facts guide or revise subsequent reasoning. CIPO requires neither human process annotations nor an additional reward model. Across seven in-domain and out-of-domain benchmarks, CIPO reduces the prevalence of prior-driven reasoning and achieves strong performance on most tasks.
- **Key innovations**: (1) Direct supervision of evidence grounding, not just outcome; (2) dense turn-level evidence-use credit + global outcome reward; (3) no human annotations and no reward model.

### 2.2 EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents

- **arXiv**: [2608.05519](https://arxiv.org/abs/2608.05519) (cs.AI; submitted 2026-08-06) — **NEW**
- **Authors**: Jie Wu, Ming Gong, Feixiang Cheng, Qinqin Zhao
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Agent benchmarks usually measure task completion and treat resource use as an auxiliary statistic. In deployment, the choice among a local lookup, broad search, composite research tool, stronger model, or human escalation **is part of the task itself**. EcoAgent-Bench makes every task specify **priced actions and an explicit budget**. Its 304 real-derived tasks span five families adapted from GAIA, HotpotQA, and MuSiQue, testing four decisions: avoiding unnecessary escalation, escalating when local evidence is insufficient, selecting a model tier, and stopping on unsupported premises. Seven LLM agents are evaluated in tool-API and workspace-CLI settings, alongside four oracle scripted controls. Micro-averaged accuracy rewards one-sided policies: always-escalate controls get high micro success while failing save-oriented tasks, so the paper adds an **economic-consistency score** (the worse of accuracy on upgrade-oriented and save-oriented family groups). Tool-API agents reach only 3.9–24.0% micro strict success (at most 7.3% economic consistency), often either stopping before warranted escalation or overspending on cheap tasks. A threshold-crossing budget sweep changes GPT-5.4's escalation rate from 0% to only 3% — completion under a budget and economical action selection are distinct properties. Task bundle, transformation pipeline, frozen evaluation environments, and integrity-bound result artifacts are released.
- **Key innovations**: (1) A benchmark where *how* the agent spends is the task, not an afterthought; (2) economic-consistency scoring that exposes one-sided escalation policies; (3) demonstrates a large gap between budgeted success and economical action selection.

### 2.3 SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse

- **arXiv**: [2608.05204](https://arxiv.org/abs/2608.05204) (cs.AI; submitted 2026-08-05) — **NEW**
- **Authors**: Jialuo Chen, Minghe Wang, Lingqi Jiang, Jianan Ma, Xinhao Deng, Xiaohu Du, Ruixiao Lin, Yunhao Feng, Linkang Du, Jingyi Wang
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: LLM-agent ecosystems are growing around reusable **skills** — mixed-modality packages of metadata, natural-language instructions, code, tools, references, and operational workflows. As skills become marketplace artifacts, auditing reuse is no longer ordinary code-clone detection: existing detectors target single-modality source code or whole-package similarity, and miss reuse that preserves only one part of a skill. SKILLTRACE is a multi-trace provenance auditing framework that extracts three provenance traces — **Expression, Implementation, and Operational** — representing the Operational Trace as a **Skill Operational Graph (SOG)** capturing activation, procedure, and resource-flow structure. An LLM assists only Operational-trace extraction, once at ingestion; at audit time SKILLTRACE compares cached traces deterministically, calibrates each trace against same-function strict negatives, and reports which trace supports a reuse decision. On SKILLTRACE-BENCH (820 transformed reuse positives over 100 marketplace anchors + 751 negative controls) it reaches **AUROC 0.938 / F1 0.898**. A 36,446-skill wild audit shows trace-attributed evidence surfaces actionable reuse review queues beyond repository-level baselines.
- **Key innovations**: (1) Provenance auditing tailored to mixed-modality skill reuse rather than code clones; (2) deterministic, LLM-free audit-time comparison with per-trace attribution; (3) operational-trace graph representation (SOG) capturing activation/flow structure.

### 2.4 CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents

- **arXiv**: [2608.05886](https://arxiv.org/abs/2608.05886) (cs.AI / cs.SE; submitted 2026-08-06) — **NEW**
- **Authors**: Wuya Chen, Yihao Yang, Yang Cao, Yue Lin
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Modern LLM coding agents such as Claude Code and OpenHands spend much of their token budget **finding the file to patch** rather than patching it: on SWE-Bench Verified, a 30B OpenHands agent averages 23 rounds and 631K tokens per resolved issue, many calls spent on grep, glob, and view_file during repository exploration. CodeGrep is a **14B retrieval agent trained end-to-end with GRPO** to issue multi-turn parallel grep, glob, and read tool calls and return candidate files to a frozen downstream coding agent. On all 500 SWE-Bench Verified instances it preserves resolve rate while improving efficiency — **27.0% vs 25.8%** for the no-retrieval baseline, with **15% fewer rounds and 19% fewer tokens** on resolved instances. Across retrievers, downstream utility follows a precision threshold: BM25 (precision 0.375) degrades the agent, Jina (0.445) is neutral, and CodeGrep (0.677) crosses the threshold at which retrieval begins to reduce rollout cost. Supervision is mined from 67K open-source agent trajectories using CATM, in a Git-worktree environment for multi-turn agent RL. Applying the efficiency signal at the **advantage layer** rather than the reward layer reduces KL drift and translates cleanly into downstream efficiency. Model, training pipeline, RL environment, and evaluation harnesses are released.
- **Key innovations**: (1) A dedicated RL-trained file-retrieval agent that decouples repo exploration from patching; (2) a precision-threshold account of when retrieval helps vs hurts downstream coding agents; (3) advantage-layer (not reward-layer) efficiency signal with lower KL drift.

---

## 3. Mechanism Design, Fair Division & AI Governance

### 3.1 Resourced Authority: A Mechanism-Design Model for Participatory Governance of Deployed AI Agents

- **arXiv**: [2608.06353](https://arxiv.org/abs/2608.06353) (cs.GT / cs.AI; submitted 2026-08-06) — **NEW**
- **Authors**: Praphul Chandra, Sujit Gujar, Ganesh Ghalme
- **Institution**: Atria University (Chandra) / IIIT Hyderabad (Gujar) / IIT Hyderabad (Ghalme) (high confidence — well-known affiliations)
- **Abstract (faithful summary)**: A formal mechanism-design model for the **continuous participatory governance of a deployed AI agent**, built on the principle that governance should control the agent through **resource allocation** so that authorization becomes **self-enforcing via compute budgets** — establishing the Safe AI paradigm that compute is an effective governance lever. The mechanism is situated as a compliance/commons overlay on a deployer. One governance period is an extensive-form game in which verified human stakeholders arrive sequentially and contribute, on a provision or rejection market, in a governance currency deliberately distinct from the agent's compute. A funding aggregator turns raw contributions into breadth-weighted effective supports; a **two-threshold gate with hysteresis** converts net support into a binary authorization that, via a coupling map bounded by an exogenously certified safety ceiling, releases a **metered compute budget** — realized in hardware as a signed compute license so the decision is self-enforcing. The paper characterizes the class of agents the mechanism can govern and isolates **manipulation of the governing electorate by the governed agent** as the central open problem.
- **Key innovations**: (1) Compute budgets as the enforcement lever for participatory AI governance; (2) signed-compute-license hardware realization makes authorization self-enforcing; (3) formally names electorate-manipulation by the governed agent as the central open problem.

### 3.2 Fair and Efficient Balanced Allocations for Additive Valuations

- **arXiv**: [2608.06325](https://arxiv.org/abs/2608.06325) (cs.GT; submitted 2026-08-06) — **NEW**
- **Authors**: Benjamin Cookson, Nisarg Shah, Paritosh Verma
- **Institution**: University of Toronto (high confidence — Nisarg Shah's affiliation)
- **Abstract (faithful summary)**: Studies the existence of fair and efficient allocations of indivisible goods under the **balancedness constraint** — any two agents' bundles must differ in size by at most one. Main result: balanced allocations that are simultaneously **envy-free up to one good (EF1)** and **fractionally Pareto optimal (fPO)** exist for **arbitrary additive valuations**. This generalizes a recent result of Kawase et al. (2026), which established existence only for personalized bivalued valuations or at most two distinct valuation types. The proof applies the **Knaster–Kuratowski–Mazurkiewicz (KKM) lemma** to a weighted-welfare duality framework and develops a novel **price-interlacing lemma** to overcome barriers in prior work. The technique extends to **category constraints (partition-matroid constraints)**, where the paper establishes existence of an fPO allocation satisfying a weaker, category-sensitive relaxation of EF1, under which envy can be eliminated by removing at most one good from each category. All proofs were obtained using GPT-5.6-Sol with author guidance; the authors verified the proofs and expanded/simplified the arguments with assistance from GPT-5.6-Sol and Claude Fable 5.
- **Key innovations**: (1) EF1 + fPO existence under balancedness for all additive valuations (generalizing Kawase et al. 2026); (2) price-interlacing lemma + KKM-based duality framework; (3) extension to partition-matroid (category) constraints with a category-sensitive EF1 relaxation.

---

## 4. Conversational Search & IR

### 4.1 Cleo: A Transparent and Controllable Chatbot for Conversational Commerce

- **arXiv**: [2608.06068](https://arxiv.org/abs/2608.06068) (cs.HC / cs.IR; submitted 2026-08-06) — **NEW**
- **Authors**: Kevin Schott, Jan Lattenkamp, Daniel Hienert, Dagmar Kern
- **Institution**: Not stated on abstract page. Authors are affiliated with FIZ Karlsruhe (tentative; single-source).
- **Abstract (faithful summary)**: A transparent and controllable conversational product advisor addressing opacity, LLM unpredictability, and comparison complexity in conversational commerce. Four contributions. **Transparency**: the LLM is prompted to reflect on interpreted user needs, and an auditable ranking mechanism reveals **loss values per attribute**, explaining ranking decisions. **Controllability**: a hybrid architecture separates deterministic ranking from language generation — a ranker applies categorical filters and numeric loss functions over **3,638 product specifications**, while a constrained LLM generates grounded descriptions limited to catalog evidence, mitigating hallucinated or persuasive content. **Decision support**: natural-language comparisons and a highlights feature contextualize specifications relative to user needs. **Extensibility**: an experimental system for IR and HCI researchers and practitioners of conversational search/recommendation. Unlike traditional faceted search or opaque LLM-only recommenders, Cleo allows fluid conversation while maintaining algorithmic transparency; a live demonstration covers needs elicitation and reflection, conversational refinement with real-time re-ranking, per-attribute loss inspection, and AI-generated multi-item comparisons.
- **Key innovations**: (1) Auditable per-attribute loss-based ranking rather than opaque LLM scores; (2) hybrid deterministic-ranker + constrained-generator architecture; (3) a conversational-commerce testbed for transparent, controllable recommendation.

---

## 5. Applied ML & Forecasting

### 5.1 GEM-3: Timestep-Conditioned Transformers for Global Weather Forecasting

- **arXiv**: [2608.06241](https://arxiv.org/abs/2608.06241) (cs.LG / physics.ao-ph; submitted 2026-08-06) — **NEW**
- **Authors**: Sam Levang, Fran Bartolic, Ty Dickinson, Chase Dwelle, Paulius Rauba, Viktor Cikojevic
- **Institution**: Salient (salientpredictions.com) (high confidence — company site in abstract page)
- **Abstract (faithful summary)**: Existing ML weather models rely on predetermined, fixed autoregressive timesteps. Timestep choice is a fundamental trade-off: short timesteps (1–6h) resolve sub-daily dynamics but accumulate more error at long horizons; long timesteps (24h) reduce error accumulation but hurt short-range usability. GEM-3, a probabilistic global weather model, addresses this via **explicit multi-timestep inference**: with a single set of trained weights, the model timestep is configured at inference time to balance predictability and usability across the forecast horizon. **Mixed-timestep training** consistently improves rollout stability relative to timestep-specialist models. Under the hood, GEM-3 is a lightweight **neighborhood-attention transformer (~134M parameters)** on an equirectangular grid, with architectural advancements beyond its predecessor GEM-2. The result is a practical system coupling near-SOTA medium-range probabilistic skill, stable extended-range rollouts, efficient training/inference, and decision-relevant diagnostics.
- **Key innovations**: (1) Configurable-at-inference model timestep from one weight set — a new axis of the predictability/usability trade-off; (2) mixed-timestep training for rollout stability; (3) ~134M-parameter lightweight backbone.

---

## Cross-cutting trends

- **Skill management moves outside the model and inside the audit trail** — KV-Skill factorizes task knowledge into external operators loadable on frozen backbones; SkillTrace audits skill reuse across expression/implementation/operational traces; both treat capability as separable, loadable, and auditable artifacts rather than opaque weights.
- **Agent evaluation shifts from "did it succeed" to "how economically / how groundedly did it act"** — EcoAgent-Bench prices every action under an explicit budget; CIPO rewards evidence-grounded turns over confirmation-bias reasoning; CodeGrep isolates the precision threshold at which retrieval pays for itself in coding agents. This mirrors the Aug 7/8 reliability-and-auditability theme (SearchAuditor, OrchestraBench, SkillZip).
- **RL supervision keeps shedding labels** — OPD² distills using only the teacher/base probability gap (no reward model), CIPO needs no human annotations or reward model, CodeGrep applies an advantage-layer (not reward-layer) efficiency signal — extending the Aug 8 digest's supervision-free/gradient-free cluster (U-OPSD, Hyper-ES).
- **Mechanism design grows a governance branch** — Resourced Authority makes compute budgets a self-enforcing authorization lever for deployed agents; balanced allocations (EF1+fPO under balancedness) advances the classical fair-division frontier with a novel price-interlacing lemma. Both treat AI/compute as objects of explicit institutional design.
- **Transparency is being engineered into the product surface** — Cleo exposes per-attribute loss explanations in conversational commerce, parallel to the digest's auditability theme and prior scans' VLM-as-judge work.
- **Forecasting efficiency continues as a theme** — GEM-3's multi-timestep inference and ~134M lightweight backbone sit alongside the Aug 8 digest's time-series papers (Align-RAG, TS-RAG) as efficiency-first forecasting contributions.

## Methodology & caveats

- Papers selected from the Aug 5–6, 2026 arXiv window across the requested domains (AI, LLM, agents, retrieval, mechanism design, games, conversational IR, applied ML). Not exhaustive; ranked by novelty, industrial signal, and domain coverage. All 10 are **new** to the wiki (grep-verified, 0 hits).
- arXiv announces new listings Mon–Fri only; there is no Sat Aug 8 announcement, so this scan curates **uncovered papers from the same Fri Aug 7 batch**, with zero overlap against the Aug 7 scan (17), Aug 7 digest (26), Aug 8 digest (21), and Aug 6 outputs (all candidates grep-checked on arXiv ID).
- Institution/company attribution: **high confidence** where stated in the abstract (deployment/venue) or a well-known affiliation; **tentative** marks where only inferred from co-author affiliations (single-source). No affiliation should be treated as authoritative without checking the paper.
- arXiv export API returned HTTP 429 intermittently; metadata cross-checked against individual abstract pages (`citation_date`, `citation_author` meta tags) and cached listing data.
- Note on coverage boundaries: three originally shortlisted papers were excluded — 2608.05152 (submitted 20 May 2026 despite 2608 ID prefix; pre-window) and 2608.05944 (multi-node B300 full-fine-tuning operations field report; off-domain infra).
