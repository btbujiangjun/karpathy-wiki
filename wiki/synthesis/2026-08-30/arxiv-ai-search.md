---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-30)"
type: synthesis
created: 2026-08-30
updated: 2026-08-30
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, ml-systems, inference, kv-cache, retrieval, marl, markets, agentic-engineering, daily-digest]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-30 (Sunday) · Scope: papers **not yet covered anywhere in the wiki** (every arXiv ID below grep-verified absent from `wiki/` against the known-ID set of 3,935 `2608.*` IDs). **No weekend arXiv mailing exists** — the latest live listing is **Fri 2026-08-28** (top ID ~2608.27455), so this report follows the Sunday deep-scan precedent of [2026-08-16](../2026-08-16/arxiv-ai-search.md): a **deeper second pass over the Fri Aug 28 submission wave** that the [08-28 siblings (`arxiv-daily`, `arxiv-ai-search`)](../2026-08-28/) already mined (they claimed ~2608.26480–2608.27454, and the 08-29 report took the 2704x–2745x tail). Today we re-screen the same wave for under-covered papers across cs.AI / cs.LG / cs.CL / cs.IR / cs.GT / cs.MA / cs.CV: **72 unique listed papers parsed, 49 NEW vs. the wiki**; 10 featured below + 7 honorable mentions.
>
> Direct arXiv API/web is blocked in this environment (curl exit 35 "Connection reset by peer"; webfetch "Transport error"). Listings were scraped via `papers.cool` (curl) and metadata recovered via targeted `websearch` against live arXiv abstract/HTML pages. Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities / project pages (author websites, GitHub, prior papers); otherwise "not stated".
>
> Sibling jobs `arxiv-daily` (10:00) and `arxiv-paper-check` (10:20) produced no reports for 2026-08-30 — this is the only 08-30 digest.

---

## ① LLM Inference & Reliability (3)

### 1.1 TwinKV: A Composable Repair Pass for KV Cache Eviction via Pairwise Key Redundancy

| Field | Detail |
|-------|--------|
| **Authors** | Hong Chen, Yudong Zeng, Yongwei Huang, Zuhao Ouyang, Junyan Zhang, Xuming Hu |
| **Institution** | (inferred: HKUST(GZ) — Xuming Hu is Assistant Professor of the AI Thrust at HKUST(GZ), also affiliated with HKUST CSE; several prior KV-cache papers of his group carry xuminghu@hkust-gz.edu.cn as contact) |
| **Abstract** | Long-context inference is bottlenecked by the memory footprint of the key-value (KV) cache, especially for small models under tight resource budgets. Existing KV cache eviction methods score tokens using the model's attention distribution or, in attention-free variants, each key's distance from a global reference point. Using a controlled leave-one-out probe, the authors find that **attention magnitude is unrelated to a token's causal contribution to the answer (Spearman ρ = −0.004)**, challenging the premise behind dominant eviction methods. They introduce **TwinKV**, a training-free, attention-free redundancy signal that detects whether a token's key has a near-duplicate elsewhere in context. Rather than replacing existing policies, TwinKV acts as a **composable repair pass**: given a policy's fixed retained set, it identifies evicted tokens with no surviving duplicate (*orphans*) and retained tokens whose information is duplicated elsewhere (*redundant donors*), then swaps them while preserving the original budget and scoring rule. Composed with four recent eviction policies across LongBench, LooGLE, RULER, and a short-context MMLU-Pro no-harm control at ratios {0.3, 0.5, 0.7}: on Qwen3-4B it improves a majority of configurations for two policies and is near-even for a third; on RULER with Llama-3.2-1B the adaptive fourth policy improves in **every** evaluated cell. Few-shot classification exemplars are a task structure where TwinKV does not help. |
| **Key innovations** | Leave-one-out causal probe showing attention ≠ importance (ρ≈0); pairwise key-redundancy / duplication signal (twin detection); repair-pass framing that composes with any eviction policy instead of competing as a new one; no-harm short-context control. |
| **arXiv** | [2608.27128](https://arxiv.org/abs/2608.27128) · cs.CL (submitted 27 Aug 2026) |
| **Why it matters** | Joins the wiki's inference-engineering thread as a measured attack on the core premise of attention-based cache eviction (H₂O/SnapKV-style scoring), plus a composable fix rather than yet another policy — consistent with the "context is a scarce resource, triage it" thesis in [context-engineering](../../concepts/context-engineering.md). |

### 1.2 Prediction of Prediction (PoP): Inter-Layer Activation Fusion for Single-Pass Hallucination Detection in LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Himal Badu (single author) |
| **Institution** | Not stated |
| **Abstract** | Autoregressive LLMs routinely generate factually incorrect outputs with high decoding confidence, limiting their deployment in high-stakes workflows. Existing output-stage uncertainty metrics can fail when models are overconfident on false assertions, while multi-sample verification pipelines introduce substantial memory and latency overhead. This work evaluates whether internal hidden-state **transition dynamics between layers** during generation can signal factual errors without auxiliary decoding calls. **PoP** captures layer-transition uncertainty by fusing intermediate hidden representations across depth in a single forward pass. On TruthfulQA with autoregressive transformer backbones it reaches **AUROC 75.5%** for factual-correctness classification, adding **<1.2% runtime latency and zero additional generation passes**. Results are reported from the author-verified implementation and bounded by the evaluation scope (single benchmark). |
| **Key innovations** | Hallucination signal from *between-layer transitions* (not output logits or multi-sample consistency); single-pass, near-zero-cost detection; fuses per-layer hidden representations across depth. |
| **arXiv** | [2608.27165](https://arxiv.org/abs/2608.27165) · cs.CL (submitted 27 Aug 2026) |
| **Why it matters** | Hallucination detection at ~free latency is an inference-reliability enabler (vetting agents, RAG grounding, high-stakes tool use). Contrast with multi-sample verification (e.g. self-consistency) the wiki tracks — PoP trades benchmark breadth for zero added decoding, the same "single-pass efficiency" bet as MoRe (2.3) and SKILL.state (2.2). |

### 1.3 SCIT: Testing Causal Cache Carriers in Latent Chain-of-Thought Models

| Field | Detail |
|-------|--------|
| **Authors** | Yi Ding, Lijun Huang, Menglin Yang |
| **Institution** | Not stated (Menglin Yang is affiliated with graph/LLM-mechanism groups — see prior HKG/retrieval-object pages; not confirmed for this paper) |
| **Abstract** | Latent chain-of-thought models move intermediate reasoning from emitted text into continuous states, improving compactness but hiding the causal object. **SCIT (Suffix Cache Interchange Test)** is a causal protocol that constructs exact source-recipient counterfactuals, patches declared cache segments, and identifies which transformer object carries the counterfactual computation. It combines sufficiency tests with K/V component splits, hidden-state controls, semantic source controls, decoded validation, and matched corruption. On CODI-GPT2 and a Sim-CoT-style GPT-2 reproduction, counterfactual arithmetic transfers primarily through **value-cache suffix trajectories** rather than hidden states, keys, reusable answer slots, or single-token triggers. Complete sufficiency-and-necessity evidence for the late-value-suffix mechanism holds for the main CODI-GPT2 checkpoint; the Sim-CoT-style checkpoint shows the same sufficiency and decoded-control pattern but insufficient matched-corruption evidence for a necessity call. Beyond these local arithmetic cells, SCIT reveals **carrier-regime shifts**: arithmetic-like 1B cells preserve latent-tail value/KV transfer, competent 8B and repaired non-arithmetic cells route through prompt-prefix or full-cache K/V, and boundary cells get no mechanism call. |
| **Key innovations** | Mechanistic-interpretability protocol for *latent* CoT models with a concrete causal target (what carries the computation — value-cache suffix vs. keys/hidden states); competence-gated carrier map; explicit sufficiency/necessity evidence discipline. |
| **arXiv** | [2608.27265](https://arxiv.org/abs/2608.27265) · cs.CL (submitted 27 Aug 2026) |
| **Why it matters** | Latent-CoT-style models are the frontier of [galaxy-brain-reasoning](../../concepts/galaxy-brain-reasoning.md), but "thinking in hidden state" is unexplained. SCIT's KV-cache carrier result also intersects TwinKV (1.1): *which* cache objects carry computation dictates both eviction and interpretability. |

---

## ② Agent Engineering — Reliability & Efficiency (3)

### 2.1 Agent Mesh: Reliability Primitives for Non-Idempotent Agent Delegation

| Field | Detail |
|-------|--------|
| **Authors** | Mazhar Shaikh, Anurag Rajkumar Bombarde (primary), Harshal Pathak (contributing) |
| **Institution** | Not stated (the authors describe operating a production agentic software-delivery platform; company not surfaced) |
| **Abstract** | Autonomous agents increasingly perform bounded software tasks under an orchestrator that retries, resumes, and budgets them. The machinery such orchestrators reach for is the service mesh's: retry, timeout, and error-rate circuit breaking. This is a **failure study of a production agentic software-delivery platform over 147 numbered incidents spanning 81 runs**, each with a measured cost and, in most cases, a mutation proof reproducing the failure. All three assumptions those primitives rest on are violated in practice: a loop of 54 consecutive successful tool calls no error-rate breaker could see; a progress signal constant by construction, guaranteeing a false trip on the third repair round and driving one run from six-of-six components to three; 21 events accumulated across six invocations of one delegation making a correct, idempotent component unwinnable; a misrouted failure that woke five components for a two-component fault; and twelve incidents where the enforcement layer blocked correct work (the most expensive costing 107 agent turns and zero accepted writes). The cross-cutting cause is dual: **identity adequacy** (in five subsystems, an identity that failed to discriminate produced a confident wrong answer) and **evidence adequacy** (a reliability decision may only be taken on evidence capable of moving, attributable to what it measures, and deterministic). From this they derive **seven reliability primitives whose enforcement unit is the delegation rather than the message**. |
| **Key innovations** | Field-grounded (142/147 incidents with mutation proofs) taxonomy of why mesh primitives fail on agents; delegation-level (not message-level) enforcement unit; identity-adequacy / evidence-adequacy framing of agent reliability. |
| **arXiv** | [2608.26225](https://arxiv.org/abs/2608.26225) · cs.SE/cs.AI (submitted 26 Aug 2026) |
| **Why it matters** | Concrete evidence for the [agentic-engineering](../../concepts/agentic-engineering.md) reliability thread: the retry/timeout/circuit-breaker stack inherited from service meshes changes meaning under non-idempotent, stateful agent execution — the wiki's "agents need their own reliability substrate" thesis. |

### 2.2 SKILL.state: Scalable Long-Horizon Agent Skills

| Field | Detail |
|-------|--------|
| **Authors** | Sanket Badhe, Jonghyun Chung (Google LLC); Priyanka Tiwari (Purdue University) |
| **Institution** | Google LLC + Purdue University *(stated)*; accepted at **EMNLP** |
| **Abstract** | LLMs increasingly act as autonomous agents executing complex, long-running procedural skills. Existing agent runtimes maintain execution by continually appending observations, actions, and intermediate reasoning traces to an ever-growing conversation history, causing latency degradation and **context-poisoning failures over long horizons**. **SKILL.state** is a runtime architecture that replaces append-only conversational history with an explicit, **mutable execution state**. At each execution step, the model receives only the immutable skill specification, the current structured execution state, and the latest observation. Intermediate reasoning is **discarded immediately after producing a validated state update**, preventing prompt growth with execution history. Across diverse datasets, models, and execution environments, SKILL.state improves task accuracy while substantially reducing cumulative token consumption. Explicit execution state is shown to be an effective, architecture-agnostic abstraction for scalable long-horizon agent skills. |
| **Key innovations** | Mutable external state replaces the append-only context (state checkpoints, not transcripts); reasoning consumed-and-discarded after each validated update; fixes latency growth and context poisoning; architecture-agnostic across models/environments. |
| **arXiv** | [2608.26263](https://arxiv.org/abs/2608.26263) · cs.CL/cs.AI (submitted 26 Aug 2026, EMNLP) |
| **Why it matters** | The strongest recent articulation of the wiki's "agent context must be curated, not appended" thesis ([context-engineering](../../concepts/context-engineering.md), [agentic-engineering](../../concepts/agentic-engineering.md)) — mirrors ReWorld-style landmark memory and the delegation-level state of Agent Mesh (2.1). |

### 2.3 One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles (MoRe)

| Field | Detail |
|-------|--------|
| **Authors** | Zhichen Zeng, Xiyuan Yang, Hanghang Tong (UIUC); Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu, Ying Chen, Chaosheng Dong, Haiyang Zhang (Amazon) |
| **Institution** | University of Illinois Urbana-Champaign + Amazon *(stated in front matter)* |
| **Abstract** | Specializing LLMs toward distinct abilities underpins everything from personalized assistants to multi-agent systems (MAS). Single-agent paradigms rely on pre-defined personas or steering vectors, imposing a single fixed specialization that fails to adapt to diverse queries; MAS achieves dynamic multi-perspective solving but inflates context length and inference cost with multi-turn interactions. **MoRe** adaptively composes multiple specializations into a **single steering vector for single-turn inference**: it learns a diversified codebook of steering vectors, each encoding a latent role, and a query-aware router fuses the codebook into a composed steering vector applied to the frozen backbone. Trained via a three-stage SFT curriculum + GRPO post-training (backbone frozen). Across reasoning and personality benchmarks, MoRe **outperforms single-agent baselines by 2.2% on average and matches MAS while reducing token cost ~20×**. Role effects are strongest on long reasoning chains; short-form recall benefits less. |
| **Key innovations** | Mixture-of-roles steering: query-conditioned composition of latent role vectors in one forward pass; single-turn multi-perspective inference (no agent chatter — ~1/20 the tokens of MAS); frozen-backbone training recipe (SFT curriculum + GRPO). |
| **arXiv** | [2608.27338](https://arxiv.org/abs/2608.27338) · cs.MA (submitted 27 Aug 2026) |
| **Why it matters** | Attacks the token-cost side of multi-agent reasoning research (decade-of-agents critique of "more agents = more calls"); sits alongside PoP (1.2) and SKILL.state (2.2) in the "single-pass / minimal-context efficiency" cluster this wave. Composable steering fits the wiki's agentic-models/steering thread. |

---

## ③ Retrieval & Search Infra (2)

### 3.1 misi: a Metric Inverted Sample Index

| Field | Detail |
|-------|--------|
| **Authors** | Edgar Chávez |
| **Institution** | CICESE, Mexico *(stated)* · [code](https://github.com/zevahcle/MISIFU) |
| **Abstract** | **misi** is an inverted index for approximate nearest-neighbor (ANN) search over general metric spaces whose vocabulary is a random sample of the database, of size proportional to n. Each object is represented by its k_b nearest sample points (found via a pluggable inner index over the sample); queries are answered by an idf-weighted shared-neighbor vote plus exact verification of C candidates. Construction generalizes the NAPP index from a constant number of pivots to a **linear-size vocabulary**, keeping posting lists at constant expected length ρ = k_b/α as n grows and making the index a **combinator**: any high-recall index on αn points yields an index on n points, for any metric. A probabilistic model gives a recall guarantee (k_b logarithmic in n over the overlap gap suffices, with a verification budget the index estimates) and a matching limit (the vote cannot resolve overlap differences below order 1/√k_b). Structural strengths: construction is n independent searches — embarrassingly parallel, deterministic, **5,250 s for 10⁸ vectors on 64 cores (3.7× faster than a matched-recall graph build)**, streams under an enforced 3 GiB cap, and serves 10⁸ vectors from NVMe within an 8 GB budget. Cost: saturated graph baselines answer 6–16× faster in RAM; verification budget for 0.99 recall grows as n^0.30. Intended for construction-cost/determinism/memory-constrained/black-box-metric workloads (frequently rebuilt corpora, batch similarity, constrained-memory serving). |
| **Key innovations** | Linear-size random-sample vocabulary (NAPP generalization) with constant-expected-length postings; principled recall guarantee + matching lower bound; index-as-combinator construction (composition of indices); reproducible measured negative results (throughput vs. graphs). |
| **arXiv** | [2608.27422](https://arxiv.org/abs/2608.27422) · cs.IR/cs.DS (submitted 27 Aug 2026) |
| **Why it matters** | Buildable ANN infrastructure for the wiki's retrieval/search thread: determinism, rebuild cost, and memory ceilings are the practical axes alongside recall — relevant to RAG index maintenance and to advertising/rec serving stacks that rebuild infrequently-indexed corpora. |

### 3.2 RATIO: A Benchmark for Retrieval Across Typed Ideation Operations in Scientific Literature

| Field | Detail |
|-------|--------|
| **Authors** | Maayan Sharon, Tom Hope |
| **Institution** | Hebrew University of Jerusalem + Allen Institute for AI (AI2) *(stated via arXivDaily / project affiliation)* |
| **Abstract** | Retrieved scientific literature can serve as inspiration for human and AI scientists, and inspiration takes different forms: prior work may directly suggest how to address a problem, or surface directions at different levels of abstraction — zooming out to a more general view or zooming in to a concrete realization. **RATIO (Retrieval Across Typed Ideation Operations)** is a large-scale benchmark where relevance is defined by three operations called **ideation moves**: *Address* (retrieves potential approaches for stated problems), *Broaden* (retrieves more general formulations), and *Specify* (retrieves concrete instantiations). It is built from millions of full-text scientific papers across CS via a recipe that extends **discourse-marker distant supervision — previously used only for classification — to corpus-scale retrieval**, combined with extensive LLM and human vetting. Experiments show operation-specific fine-tuning substantially boosts retrievers but leaves much room for improvement. |
| **Key innovations** | Ideation-move-typed retrieval as a benchmark task (Address/Broaden/Specify); distant-supervision → corpus-scale retrieval recipe; scalable train/eval framework for scientific inspiration retrieval. |
| **arXiv** | [2608.27394](https://arxiv.org/abs/2608.27394) · cs.CL (submitted 27 Aug 2026) |
| **Why it matters** | Shifts retrieval relevance from "topical match" to "what the query is trying to do" — a reframing with direct echoes in the wiki's RAG/evidence-retrieval thread (cf. 2608.26379 honorable mention) and recommendation-style matching beyond topicality. |

---

## ④ Markets, Games & Multi-Agent RL (2)

### 4.1 Trusting AI in Competitive Markets

| Field | Detail |
|-------|--------|
| **Authors** | Jussi Keppo, Yuze Li, Gerry Tsoukalas, Nuo Yuan |
| **Institution** | (inferred per byline emails: Keppo — National University of Singapore (ISEM); Li — The Chinese University of Hong Kong (yuzeli@cuhk.edu.hk) in this version, earlier BU in SSRN draft; Tsoukalas — Boston University; Yuan — City University of Hong Kong (Dongguan)) |
| **Abstract** | People's trust in AI advice diverges as they use it — deepening for some, eroding for others. This is studied in **oligopoly pricing**, where advice cannot prove itself because rivals' responses decide whether it pays off. In a laboratory experiment, **273 sellers compete across 91 three-seller markets over 30 rounds**, varying the presence of AI pricing recommendations and the gender composition of the market (female-only, male-only, or mixed). The gender composition shapes how sellers learn from the advice and where prices settle: in **female-only markets, recommendations raise prices by 29% and profits by 39%**; in male-only and mixed markets they have no significant effect. A **Non-Homogeneous Hidden Markov Model** reveals a composition-specific dynamic association: profitable rounds predict *rising* adherence in female-only markets and *declining* adherence otherwise — consistent with learned trust and self-serving attribution. This pattern *reverses* what recent evidence on gender and AI would predict. Managerial implication: platform governance and regulatory oversight should focus not only on the algorithm but on the human side that shapes its effects. |
| **Key innovations** | Field-style lab design for AI-advice trust dynamics in strategic (oligopoly) settings where advice payoff is endogenous; compositional (gender) heterogeneity in trust learning; NHMM-based dynamic adherence modeling; falsifies naivety about algorithmic determinism of price outcomes. |
| **arXiv** | [2608.26539](https://arxiv.org/abs/2608.26539) · cs.GT/cs.AI (submitted 27 Aug 2026) |
| **Why it matters** | Real markets with AI pricing recommendations are a live policy question (collusion-by-algorithm concern) the wiki tracks in market design; here the *human-side* trust dynamics decide whether AI advice moves prices at all — and the result is composition-dependent, not algorithm-dependent. |

### 4.2 SIGMA: Structured Noise-Effect-Aware Grouped Multi-Agent Aggregation

| Field | Detail |
|-------|--------|
| **Authors** | Mingqian Li |
| **Institution** | School of Computer Science and Technology, Tongji University, Shanghai *(stated)* · [code](https://github.com/Lmq0/SIGMA-Structured-Noise-effect-Aware-Grouped-Multi-agent-Aggregation) |
| **Abstract** | Cooperative multi-agent RL (MARL) faces significant challenges in maintaining robust coordination under noisy observations. Although observation disturbances are often introduced independently across agents, their downstream effects on cooperative decision-making become **structured** through underlying cooperation structures — a phenomenon dubbed *structured noise effects*: noise-induced decision effects exhibit local correlation among agents with stronger task-related dependencies while remaining globally heterogeneous across agents and local structures. **SIGMA** is a hierarchical collaboration framework that exploits cooperation structures to learn robust representations: it organizes agents into adaptive local structures via **density-based grouping**, performs **intra-group consensus aggregation** to preserve shared task-relevant information while smoothing agent-specific deviations, and uses **inter-group attention** to integrate across groups while accommodating heterogeneous contributions. On noisy-observation tasks in **StarCraft II (SMAC)**, SIGMA empirically validates structured noise effects and consistently improves robustness under observation noise while staying competitive in noise-free environments — where structure-aware baseline HYGMA and QMIX degrade substantially under strong disturbances. |
| **Key innovations** | Characterizes *structured noise effects* (locally correlated, globally heterogeneous) as a distinct failure mode; density-based adaptive grouping + consensus aggregation + inter-group attention; robust-MARL recipe validated on SMAC wrapping MARL value-decomposition baselines. |
| **arXiv** | [2608.26683](https://arxiv.org/abs/2608.26683) · cs.AI/cs.LG/cs.MA (submitted 27 Aug 2026) |
| **Why it matters** | Robustness to observation noise is the deployment gap between clean-benchmark MARL and real multi-agent fleet/robot coordination; the structure-aware (vs. factorized-only) fix is a clean conceptual addition to the wiki's MARL/games thread. |

---

## ⑤ Honorable mentions (scanned, not featured)

| arXiv ID | Title | Category | One-line takeaway |
|----------|-------|----------|-------------------|
| [2608.27380](https://arxiv.org/abs/2608.27380) | D2C-Routing: Dimension-to-Composition Evidence Routing for Mixed-Origin AI-Generated Text Detection | cs.CL (EMNLP 2026) | Binary "machine vs. human" detection breaks on mixed-origin text; routes content/expression evidence to dimension heads + gated composition (Xin Chen, Wei Guo, Fuzhen Zhuang et al.). |
| [2608.26130](https://arxiv.org/abs/2608.26130) | Agents Don't Paginate: First-Chunk Selection for LLM Tool Responses | cs.CL | Coding agents read only the first chunk of oversized tool responses; keyword-first scoring lifts precision-at-1 (24.2% → 35.8%) but — negative result — downstream accuracy does not move. |
| [2608.27161](https://arxiv.org/abs/2608.27161) | STAR/StarPO: Sentence Translation Alignment Rate for Doc2Doc MT | cs.CL | Structural-fidelity metric for document translation + masked-preference optimization; compact models surpass GPT-4o on structural integrity at far lower token cost. |
| [2608.26788](https://arxiv.org/abs/2608.26788) | Decoupling Planning and Control for Instructable Agents (Instruct-to-Act) | cs.AI | VLM planner (slow, language) + world-model controller (fast, high-frequency); instruction-relabeled behavior cloning; beats controller-only and direct VLM action generation in 7 embodied envs. A concrete synthesis of the wiki's planner/actuator split. |
| [2608.26379](https://arxiv.org/abs/2608.26379) | Assessing the Downstream Utility of Evidence-Aware Retrieval in RAG | cs.IR | Evidence-aware retrieval changes rankings but does not reliably improve retriever training, system selection, or answer prediction — RAG evaluation must be justified per downstream use. |
| [2608.27115](https://arxiv.org/abs/2608.27115) | Cross-Lingual Alignment Without Joint Training | cs.CL | Procrustes alignment transfers functionally between *monolingual* models (no joint training needed) — model stitching for modular multilingual systems. |
| [2608.27300](https://arxiv.org/abs/2608.27300) | Nash Loci | cs.GT (math) | Algebraic-geometry characterization (dimensions, multidegrees, Plücker/coordinate equations) of the equilibrium schemes of constrained games; not applied work. |

---

## ⑥ Cross-cutting observations

1. **"Attention ≠ importance" is now a measured, reusable claim.** TwinKV's leave-one-out probe (Spearman ρ ≈ −0.004 between attention magnitude and causal contribution) is the strongest quantified attack yet on attention-scored cache eviction — and its answer is not a new scorner but a *repair pass* over existing policies. Expect this to propagate into the wiki's KV-cache/eviction tracking as the premise-checking story of the wave (cf. SCIT: which cache objects actually carry computation).
2. **Agent reliability & efficiency is converging on "delete the transcript" / "shrink the delegation unit."** SKILL.state discards reasoning after a validated state update; Agent Mesh faults retry/timeout/circuit-breaker at message granularity and proposes delegation-level primitives; MoRe gets multi-perspective synergy in one forward pass. Three papers, same direction: **context curation + coarse-grained reliability units** — the [context-engineering](../../concepts/context-engineering.md) thesis extending from long-context serving into agent runtime design.
3. **Single-call reasoning is catching up to multi-call reasoning.** MoRe ≈ MAS at ~1/20 tokens; PoP detects hallucinations with zero extra passes. The efficiency frontier of the "decade of agents" is compressing specialist-team behavior into a single steering/attention object rather than adding orchestrator round-trips.
4. **Market papers turn on trust dynamics, not algorithms.** Trusting AI's gender-composition result (advice only raises prices/profits in female-only markets; NHMM shows adherence diverging by market composition) is a caution against "algorithm determines collusion" models — governance must model the human side. Pairs naturally with the MARL-robustness paper (SIGMA) as the two "real-world friction" corners of the games/markets category.

## Methodology

- **Listing source**: direct arXiv API (`export.arxiv.org`) and `arxiv.org` are blocked in this environment (curl exit 35; webfetch "Transport error"). The Fri 2026-08-28 wave was scraped from `papers.cool` via curl (`paperscool_cl_lg_ai_cv.html` = cs.CL/LG/AI/CV, `pc_ir.html` = cs.IR, `pc_gt_ma.html` = cs.GT/MA) and parsed to 72 unique papers; 49 were NEW vs. the wiki known-ID set.
- **Verification**: every reported arXiv ID was grep-verified **absent** from the wiki known-ID set (`/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/known_ids_2608.txt`, 3,935 unique `2608.*` IDs extracted from `wiki/`). Known-and-dropped during screening included 2608.264xx–274xx IDs already claimed by the 08-28/08-29 siblings.
- **Metadata recovery**: titles/authors/abstracts/affiliations recovered from live arXiv abstract/HTML pages and aggregators via targeted `websearch` (arXiv → "Transport error" for direct fetch, but search results return full abs-page text). Submissions are all v1 Thu/Fri 27–28 Aug 2026 of the Fri Aug 28 mailing.
- **Coverage disclaimer**: the wiki's known IDs are derived from `wiki/` text only; papers whose IDs appear nowhere in the wiki but were covered through other identifiers (DOI, conference page) could theoretically overlap — flagged candidates were manually cross-checked against the 08-28/08-29 sibling reports.
- **Temp files**: scraped HTML and the candidates/known-ID JSON/text live under the pre-authorized temp path `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and are deleted after this report lands.

*All affiliations above are stated only when the paper front matter says so; "(inferred)" entries are deduced from author identities / projects / prior papers and remain tentative. "(single-source)" claims rest on one abstract pass and were not read in full text.*