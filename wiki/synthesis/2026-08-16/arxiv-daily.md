---
title: "arXiv Daily Digest — 2026-08-16 (Sunday catch-up)"
type: synthesis
created: 2026-08-16
updated: 2026-08-16
sources: [arxiv-cs.AI, arxiv-cs.LG, arxiv-cs.CL, arxiv-cs.IR, arxiv-cs.GT, econ.TH, stat.ML]
tags: [arxiv, daily-digest, llm, architecture, pretraining, reasoning, rl, agents, skills, memory, retrieval, embeddings, ir, time-series, finance, market-data, games, game-theory, mechanism-design, evaluation, benchmarks, theory, diffusion, moe, constrained-decoding]
---

# arXiv Daily Digest — 2026-08-16 (Sunday catch-up)

> **Batch note:** arXiv announces new submissions Mon–Fri; there is **no Sat–Sun Aug 15–16, 2026 announcement**. The latest listing is the **Fri Aug 14, 2026** batch (submissions Aug 12–13, IDs ~2608.12308–2608.13560), which the 08-14 digests ([arxiv-daily](../2026-08-14/arxiv-daily.md) 29 papers, [arxiv-ai-search](../2026-08-14/arxiv-ai-search.md) 20 papers, [arxiv-paper-check](../2026-08-14/arxiv-paper-check.md) 19 papers, [game-rl-daily](../2026-08-14/game-rl-daily.md) 16 papers) and today's earlier [arxiv-ai-search](../2026-08-16/arxiv-ai-search.md) (20 papers) have been curating. This digest is a **supplementary, zero-overlap curation of the same batch** — 26 additional papers across LLM architecture/pretraining, reasoning/RL/post-training, agents/skills/memory, retrieval/embeddings/IR, time series/finance/market data, and games/mechanism design. It reads as a **breadth pass**: the flagship recsys/ads/CTR and world-model papers were already claimed by the 08-14 and 08-16 sibling digests; what remains here is the systems/theory/retrieval/finance/agent-economy tail of the batch. As with prior weekends, **no new dedicated advertising/CTR paper surfaced** in the cs.IR stream beyond what 08-14 already covered; the closest platform-economics work this digest claims is the algorithm-transparency paper (econ.TH). Signature themes of this remainder: **contrast between cheap memory access (@skills) and structured, evolvable retrieval (ERSkill, SMA, Reconcile Once)**, **the cost dimension of embeddings (Embedder's Dilemma, Vector DB eval)**, **derivative-finance generative modeling maturing (DYSANOS, LOB-ID)**, and **theoretical economics/game theory claiming the cs.GT/econ.TH tail** (Incidence Bimatrix, liquid-democracy pair).

---

## Overview table

| # | Paper | Domain | Institution / Company | arXiv | Status |
|---|-------|--------|----------------------|-------|--------|
| 1 | Algorithm Transparency and Search Manipulation: Steering vs. Persuasion | Search / platform economics | (not stated; econ theory) | 2608.12558 | **new** |
| 2 | LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient LLM Pretraining | LLM architecture / pretraining | SCUT (tentative) | 2608.12419 | **new** |
| 3 | Trie Automata for Constrained Decoding over Large Finite Sets | LLM serving / constrained decoding | INRIA (tentative) | 2608.12574 | **new** |
| 4 | CABS+: Efficient and Scalable Model Merging via Conflict-Aware Sparsification and Adaptive Weight Allocation | Model merging / post-training | Beihang University (tentative) | 2608.12842 | **new** |
| 5 | RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning | MoE RL / systems | (not stated) | 2608.12146 | **new** |
| 6 | The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity | Diffusion theory | UC Berkeley / MIT (tentative) | 2608.13520 | **new** |
| 7 | Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies | LLM post-training / ES | Cognizant AI Labs / UT Austin (tentative) | 2608.12679 | **new** |
| 8 | Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction | LLM evaluation | (not stated) | 2608.12426 | **new** |
| 9 | ε-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution | LLM program evolution | (not stated) | 2608.12522 | **new** |
| 10 | Numeracy in Large Language Models: Fundamental Limitations and Paths to Improvement | LLM capability / survey | (not stated) | 2608.13129 | **new** |
| 11 | @skills: Attention is all you have | Agent skills / protocol | SylphAI Inc (tentative) | 2608.12610 | **new** |
| 12 | ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval | Agent memory / retrieval | (not stated) | 2608.12720 | **new** |
| 13 | Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence | VLM agents / memory | (not stated) | 2608.12743 | **new** |
| 14 | Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research | Research agents / provenance | (not stated) | 2608.12984 | **new** |
| 15 | Intern-S2-Preview: Scientific Agentic Foundation Model | Scientific agentic foundation model | Shanghai AI Lab (tentative) | 2608.13505 | **new** |
| 16 | The Embedder's Dilemma: LLMs Are Better, but at What Cost? | Embeddings / retrieval | KAUST / Allen AI (tentative) | 2608.12875 | **new** |
| 17 | A Comprehensive Empirical Evaluation of Vector Database Systems for ANN Search | Vector DB / IR infra | University of Colombo (tentative) | 2608.12812 | **new** |
| 18 | Query Translation vs. Cross-Lingual Embeddings for Sinhala-Tamil E-Government IR | Cross-lingual IR | University of Colombo (tentative) | 2608.12820 | **new** |
| 19 | ReCoGen: Represent, Then Generate — Multimodal-Conditioned Time-Series Generation under Irregular Missingness | Time series / generation | UNC Chapel Hill (tentative) | 2608.12592 | **new** |
| 20 | DYSANOS: Generative Dynamic Smooth Arbitrage-free Non-parametric Option Surfaces | Finance / generative modeling | JPMorgan (tentative) | 2608.12587 | **new** |
| 21 | LOB-ID: Evaluating Synthetic Market Data by Inception Distances | Finance / market data eval | UCL (tentative) | 2608.13082 | **new** |
| 22 | Incidence Bimatrix Games | Game theory | ISI Delhi / Toronto Metropolitan (tentative) | 2608.13001 | **new** |
| 23 | Power in Liquid Democracy: A Network Centrality Approach | Social choice / networks | Univ. of Groningen / Univ. of Warsaw (tentative) | 2608.13188 | **new** |
| 24 | Representation in Peer Selection: A Liquid Democracy Perspective | Social choice / peer selection | Univ. of Amsterdam (tentative) | 2608.13085 | **new** |
| 25 | LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation | Benchmarks / AI research | SJTU (tentative) | 2608.13136 | **new** |
| 26 | Sampling Luck Masquerades as Allocation Gain: Auditing Test-Time Budget Allocation for NCO | NCO / evaluation auditing | (not stated) | 2608.13087 | **new** |

---

## 1. Search, Ads & Platform Economics

### 1.1 Algorithm Transparency and Search Manipulation: Steering vs. Persuasion

- **arXiv**: [2608.12558](https://arxiv.org/abs/2608.12558) (econ.TH; submitted 2026-08-12) — **NEW**
- **Authors**: Raphael Boleslavsky, Thomas Jungbauer, Mehdi Shadmehr
- **Institution**: Not stated; standard economic-theory group (Boleslavsky – U. Miami, Shadmehr – U. Chicago Harris, tentative).
- **Abstract (faithful summary)**: A platform prefers to sell the more profitable of two products and designs an algorithm that determines which product the consumer encounters first, conditional on her best match. The algorithm simultaneously manipulates consumer attention (steers) and communicates information about match quality (informs). When the algorithm is opaque, the consumer cannot understand how product order is generated or what it reveals; in the platform's preferred equilibrium it places the profitable product first. When the algorithm is transparent, the consumer understands it — so the algorithm can **persuade as well as steer**. In some cases the equilibrium algorithm deters search; in others it encourages it. In the former case transparency helps consumers; in the latter it harms some or all of them. Extending or shifting transparency requirements uncouples steering from information provision, reverting the consumer's welfare to opacity.
- **Key innovations**: (1) A model where a platform's ranking algorithm is simultaneously a steering instrument and an information channel; (2) the central result that transparency changes whether the algorithm *deters or encourages search*, so transparency is not uniformly consumer-welfare-improving; (3) a mechanism-design reading of search-algorithm regulation with direct relevance to ranking/search-manipulation policy in the ads/rec context.

---

## 2. LLM Architecture, Pretraining & Serving

### 2.1 LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining

- **arXiv**: [2608.12419](https://arxiv.org/abs/2608.12419) (cs.LG; submitted 2026-08-12) — **NEW**
- **Authors**: Qiuwu Chen, Zimo Liu, Yuchen Li, Ying Sun, Yifan Zhang, Zhijie Qiu, Zeng You, Ryan Dong, Simeng Ma, Yaofo Chen, Mingkui Tan
- **Institution**: Not stated; Mingkui Tan's group is at South China University of Technology (tentative).
- **Abstract (faithful summary)**: LLM architectures remain inefficient in pretraining for two reasons: self-attention lacks an explicit inductive bias for locality (redundantly modeling sequence-internal local information), and mixture-of-experts couples knowledge storage with computational pathways, hindering flexible access to sequence-external global knowledge. LoKiFormer augments the standard decoder with two modules: **Local Fusion Attention (LFA)**, a convolutional fusion into attention that explicitly captures local patterns so attention operates on more informative representations; and a **Knowledge Memory Module (KMM)**, a parametric key-value memory storing global knowledge in addressable slots, decoupling storage from computation and enabling direct retrieval. LoKiFormer converges **1.33× faster in pretraining** than baseline models.
- **Key innovations**: (1) Convolution-fused attention as an explicit locality bias for pretraining efficiency; (2) a parametric external key-value memory (KMM) that decouples global knowledge storage from MoE computation pathways — the decoupling-of-storage-and-compute direction the wiki tracks across recurrent/associative-memory architectures.

### 2.2 Trie Automata for Constrained Decoding over Large Finite Sets

- **arXiv**: [2608.12574](https://arxiv.org/abs/2608.12574) (cs.AI; submitted 2026-08-12) — **NEW**
- **Authors**: Xingzi Xu, Karim Bouyarmane
- **Institution**: Not stated; Bouyarmane is affiliated with INRIA (tentative).
- **Abstract (faithful summary)**: LLMs increasingly need to generate outputs conforming to predefined schemas, one common constraint being selection from a finite set of valid strings. General-purpose grammar compilation becomes prohibitively slow as the valid-value count grows into the thousands — a "cardinality wall". The paper introduces the **trie automaton**, exploiting finite-set structure (shared prefixes, bounded depth, known cardinality) via Aho–Corasick multi-pattern matching to precompute per-node token masks. The trie achieves **7× faster per-step valid-token computation (0.65 µs vs 5.8 µs)** than XGrammar (a primary backend in vLLM and SGLang) and 2–6.5× faster compilation at K ≥ 300. Precomputed masks enable a **stateless serving path** that bypasses the guided-decoding pipeline, compounding into **219 req/s vs 7.5 req/s at batch 256 (29× end-to-end vLLM throughput)**. Across seven tokenizer families (32K–262K vocab) the trie maintains sub-100 ms compilation up to K = 10,000 and flat per-step cost regardless of set size, with 100% output validity.
- **Key innovations**: (1) A finite-set-specialized automaton replacing general grammar backends for set-constrained decoding; (2) Aho–Corasick-precomputed masks unlocking a stateless serving path — the 29× batch gain comes from the integration savings, not just the algorithmic 7×; (3) guarantees of validity and flat cost at large cardinality, directly relevant to structured-output serving for rec/ads entity-ID or schema-constrained generation.

### 2.3 RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning

- **arXiv**: [2608.12146](https://arxiv.org/abs/2608.12146) (cs.LG; submitted 2026-08-12) — **NEW**
- **Authors**: Yibo Shen, Xudong Han, Xiaowei Zhu, Gen Li, Zhenxuan Pan
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Training MoE models for RL couples two load-balancing problems: sequence composition determines dense attention work in each data-parallel microbatch, while token routing determines sparse expert work on expert-parallel ranks — optimizing either alone can shift the bottleneck to the other. In MoE RL, rollout-time routing replay exposes every sample's sequence length and layer-wise expert demand before its training step. **RoutePack** is a hierarchical planner that coordinates state-consistent, layer-wise expert rerouting with joint attention- and expert-aware data packing over an optimizer-step window: place experts at each MoE layer from aggregate routing demand, then pack samples into the smallest certified/best-known-feasible number of token-capped execution rows with a projected EDP-shard-aware objective (window-normalized linear-quadratic attention proxy + per-layer physical EP-rank peaks, minimizing the accumulated cost of the slowest EDP shard). Parallel population annealing searches feasible layouts preserving sample coverage, capacity, non-empty cells, equal microbatch counts, and communicator topology; state-consistent materialization preserves logical top-k routing and existing MoE kernels. On Ling-3.0-Tiny/Flash, expert rerouting improves token throughput 3.80%/10.50%, routing-aware packing adds 4.86%/3.98%, for **8.85%/14.89% total**.
- **Key innovations**: (1) Treating attention-packing and expert-placement as one coupled optimization in MoE RL training; (2) a certified/best-known-feasible packing bound with a slowest-shard cost objective; (3) state-consistent rerouting that keeps logical routing and kernels untouched — an efficiency contribution to the MoE-RL training stack the wiki tracks (cf. TEMPO for the serving side).

---

## 3. Reasoning, RL & Post-training

### 3.1 Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies

- **arXiv**: [2608.12679](https://arxiv.org/abs/2608.12679) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Conor F. Hayes, Elliot Meyerson, Kajetan Schweighofer, Roberto Dailey, Babak Hodjat, Risto Miikkulainen, Xin Qiu
- **Institution**: Not stated; author group is affiliated with Cognizant AI Labs / UT Austin (tentative).
- **Abstract (faithful summary)**: In discovery domains (math, science) the usual approach is to present a problem and use the model's answer as the solution. Discovery can be enhanced by test-time compute: pass@k lets the model explore solution space and generate diverse candidates. But standard RL post-training may limit pass@k — the output distribution narrows around high-reward outputs and solution coverage collapses. The alternative is **Evolution Strategies (ES)**, a population-based, gradient-free post-training method optimizing directly in weight space through random perturbations. The paper shows ES achieves **consistently higher pass@k than RL** and produces a broader output distribution with greater solution coverage, which in turn yields better results on standard math benchmarks. ES thus provides a better foundation for post-training in discovery problems where diverse coverage is critical.
- **Key innovations**: (1) Direct evidence that RL's coverage collapse harms pass@k in discovery; (2) ES in weight space as a post-training alternative preserving diversity; (3) a "coverage-first" framing for discovery-oriented post-training that complements (and at times contradicts) the RLVR/GRPO line the wiki tracks.

### 3.2 Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction

- **arXiv**: [2608.12426](https://arxiv.org/abs/2608.12426) (cs.AI / cs.CL; submitted 2026-08-12) — **NEW**
- **Authors**: Mariya I. Vasileva
- **Institution**: Not stated.
- **Abstract (faithful summary)**: LLMs are deployed where many explicit constraints must hold jointly (reasoning structure, safety boundaries, output schemas). Individual constraints are handled proficiently, but the compositional regime is poorly characterized. **Constraint Saturation Evaluation (CSE)** is a procedurally generated benchmark varying the number of simultaneous constraints k, with deterministic rule-based verification and zero LLM-judge involvement: 15 models, 36 constraint types, 369,753 checks at k = 1–12. Three findings. First, per-constraint pass rate decays gradually and predictably while the chance of satisfying *all* constraints collapses — a model passing individual constraints at ~41% at k=8 succeeds on all eight just 5.7% of the time. Second, constraints degrade unequally: structural constraints lose ~2× more baseline capability per added constraint than lexical ones, ordered by a comprehension-maintenance gap separating sustained-tracking from binary constraints. Third, failures are nearly independent (so accumulation is multiplicative); residual coupling tracks shared output features rather than pairwise interference — a wrong sentence count fails every constraint that reads it. Reliable instruction following breaks down beyond **5–6 simultaneous constraints**: probe-level success falls below 50% at 7 constraints for the strongest model, and at 3 or fewer for 12 of 15 models.
- **Key innovations**: (1) A deterministic, LLM-judge-free compositional constraint benchmark (k = 1–12); (2) a sharp characterization of the phase-transition behavior of multi-constraint compliance, with the multiplication-of-near-independent-failures mechanism; (3) a constraint-taxonomy (structural vs lexical) predicting degradation rate — directly relevant to evaluating instruction-following in production agent/rec prompts with many simultaneous requirements.

### 3.3 CABS+: Efficient and Scalable Model Merging via Conflict-Aware Sparsification and Adaptive Weight Allocation

- **arXiv**: [2608.12842](https://arxiv.org/abs/2608.12842) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Yuchen Liu, Zongzhen Yang, Binhang Qi, Hailong Sun, Xiang Gao
- **Institution**: Not stated; Hailong Sun / Xiang Gao are affiliated with Beihang University (tentative).
- **Abstract (faithful summary)**: Model merging builds unified multi-task models without retraining, but parameter conflicts and knowledge interference across tasks degrade merged performance. Prior CABS reduces interference via structured pruning and sequential masking but relies on grid search for scaling coefficients (exponential time) and can be dominated by high-performance tasks. **CABS+** adds **Adaptive Weight Allocation (AWA)**, a gradient-free search scheme for merging coefficients that reduces time complexity, and an **asymmetric fitness function** promoting more comprehensive gains across tasks. It also contributes a systematic empirical study of factors influencing merging and a **Relative Synergy Score (RSS)** quantifying model mergeability to guide model selection. Across 27 datasets and 5 models (large/small language + vision), CABS+ improves overall performance by **16.97% vs AdaMerging and 12.93% vs WUDIMerging**, uses <25% of AdaMerging's GPU memory, and achieves nearly 4× speedup in merging time over WUDIMerging.
- **Key innovations**: (1) Gradient-free adaptive coefficient search replacing exponential grid search; (2) an asymmetric fitness function to avoid high-performance-task dominance; (3) RSS as a mergeability predictor — practical for cheaply composing domain-tuned models in rec/ads pipelines.

### 3.4 ε-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution

- **arXiv**: [2608.12522](https://arxiv.org/abs/2608.12522) (cs.AI; submitted 2026-08-12) — **NEW**
- **Authors**: Aofan Liu, Shiyuan Song, Yiyan Qi
- **Institution**: Not stated.
- **Abstract (faithful summary)**: LLM program-evolution systems (FunSearch, AlphaEvolve) discover novel algorithms but typically optimize each task in isolation, discarding search experience. **ε-MemEvo** stores prior experience as **task-agnostic tactic memories** — compact natural-language summaries of successful algorithmic strategies rather than raw code — enabling transfer across tasks with different APIs and evaluators. An **adaptive injection gate** decides whether retrieved memories should be injected and at what intensity, avoiding negative transfer from semantically mismatched memories. On 8 optimization benchmarks (mathematical optimization + systems engineering), evaluated with a content-level Leave-One-Out protocol, ε-MemEvo improves AUCC over AdaEvolve on all 8 tasks (mean +8.7%) and early-stage convergence +9.4% on average, at <1% computational overhead. Ablations show naive memory injection can fail catastrophically while adaptive gating stays safe; the data-updated posterior favors *skip* during improving search and shifts from *skip* to *hint* across early and late plateaus.
- **Key innovations**: (1) Transfer across program-evolution tasks via tactic-memory summaries (not raw code); (2) an interpretable adaptive gate with posterior dynamics across search phases; (3) explicit negative-transfer analysis — a rigorous look at when cross-task memory helps vs hurts, continuing the wiki's memory-transfer thread.

---

## 4. Agents, Skills & Memory

### 4.1 @skills: Attention is all you have

- **arXiv**: [2608.12610](https://arxiv.org/abs/2608.12610) (cs.AI; submitted 2026-08-12) — **NEW**
- **Authors**: Li Yin, Zhi Li, Zhan Shi, Haoran Zhang, Haebin Seong, Zhangyang Wang
- **Institution**: Not stated; project org is SylphAI Inc (atskills repo, AdaL CLI), with Zhangyang Wang at UT Austin (tentative).
- **Abstract (faithful summary)**: There are 56,804 public agent skills today; the dominant delivery model is installation — once installed, a skill's description stays in the system prompt, competing for fewer than 100 reliable trigger slots, leaving the long tail with no practical path to use. Installation bundles three separable functions: **content, persistence, and automatic triggering** — only the last requires prompt residency. **@skills** is an open protocol that separates them: a path addresses any skill/subtree/collection and reading a skill is sufficient to use it (nothing installed or resident); the `@` operation vendors a copy at the same path into a project's Git-tracked tree; one `.gitignore`-style line is the only element costing prompt residency; a directory is a menu, making bundles ordinary directories. The protocol requires no manifest, lockfile, or registration, and SKILL.md is unchanged. It ships as an installable package and turns any file-reading, command-running agent into a client via a single instruction file. An optional hub (atskills.one) provides corpus-wide search/ranking without repo-specific hooks. "Install less, use more."
- **Key innovations**: (1) Decomposing skill delivery into content/persistence/triggering and showing only triggering needs prompt residency; (2) a path-addressed, read-to-use protocol eliminating the "install footprint" bottleneck; (3) a practical answer to the skill-discovery/retrieval problem that complements the wiki's skill-evolution thread — this is the *access/interface* side, matching how the wiki distinguishes interface gains from mechanism gains.

### 4.2 ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval

- **arXiv**: [2608.12720](https://arxiv.org/abs/2608.12720) (cs.AI / cs.CL; submitted 2026-08-13) — **NEW**
- **Authors**: Haolong Chen, Liang Zhang, Zhuo Li, Lei Xue, Guanrxu Zhu
- **Institution**: Not stated.
- **Abstract (faithful summary)**: LLM agents increasingly rely on long-term memory, but the retrieval mechanisms governing it are rarely treated as evolvable components — a static approach that limits performance on heterogeneous queries demanding diverse evidence-construction strategies. **ERSkill** compiles interaction histories into a structured memory store and represents retrieval behaviors as **executable skills composed of fundamental primitives**. A trained router dynamically matches each query to the optimal skill at inference; the skill set and router **co-evolve** during training, with an experience trie recording explored retrieval paths and a **double-frontier mechanism** that safely decouples expansion of new skill capabilities from stable, router-facing deployment. Across multiple agent-memory benchmarks ERSkill substantially outperforms non-evolving and self-evolving baselines — improving the average across F1, BLEU-1, and LLM-judge by **31.3% (Qwen3-Next-80B-A3B-Instruct)** and **28.1% (GPT-5.4-nano)**.
- **Key innovations**: (1) Retrieval-as-evolvable-skills rather than static retrieval; (2) the double-frontier safety mechanism for capability expansion without destabilizing deployed behavior; (3) strong gains across heterogeneous-memory benchmarks — a direct entry into the wiki's "skill-guided memory" cluster (cf. MindMemOS/SkillEvo on the 08-14 digest).

### 4.3 Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence

- **arXiv**: [2608.12743](https://arxiv.org/abs/2608.12743) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Haokai Zhang, Yuhang Ding, Yunshu Zhou, Xinze Du, Shengtao Zhang, Zhiyue Zhao, Yuling Xi, Hao Chen
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Spatial reasoning in VLM agents is usually improved via post-training (SFT/RL) or by agentic calls to external spatial tools (depth estimation, 3D reconstruction). The paper studies a third route: can a **frozen VLM improve its spatial reasoning through parameter-update-free self-evolution**, without external expert tools at inference? **Spatial Memory Agent (SMA)** is an experience-grounded runtime framework: in a verifiable spatial environment it queries the frozen VLM, obtains a predicted answer and reward, and uses **verifier-guided reflection** to distill compact transferable lessons. Each lesson gets a **Transfer Reliability Score (TRS)**, initialized uniformly and calibrated from later retrieval outcomes. During read-only deployment, SMA retrieves lessons by semantic filter plus similarity–TRS combined ranking to guide the frozen model. Across five spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and best accuracy in most of the 20 evaluations.
- **Key innovations**: (1) Parameter-update-free, tool-free spatial self-evolution via verifier-guided lessons; (2) TRS as a dynamically calibrated reliability signal for lesson retrieval; (3) consistent wins across 5 benchmarks × 4 frozen VLMs — a memory-only mechanism (no weights, no tools) for spatial capability, reinforcing the wiki's theme that runtime memory can substitute for weight/tool changes.

### 4.4 Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research

- **arXiv**: [2608.12984](https://arxiv.org/abs/2608.12984) (cs.CL / cs.MA; submitted 2026-08-13) — **NEW**
- **Authors**: Xing Zhang, Yanwei Cui, Guanghui Wang, Peiyang He
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Long-form LLM research reports drift, contradict themselves, and lose provenance. The paper presents a two-tier agentic system separating a maintained, point-in-time knowledge library from report writing. A deterministic **librarian** ingests timestamped sources into a trust-tiered ontology (evidence cards, an authoritative metric ledger, a claim graph) as an always-current source of truth — not per-query RAG over raw chunks. A portable multi-agent **writer** composes contradiction-free, evidence-grounded reports at any knowledge cutoff T, reading only evidence with as_of ≤ T (no look-ahead); red-team verdicts flow back into the librarian. Evaluation on a self-collected corpus of 6,130 sources → 555,926 evidence cards (SEC EDGAR filings, 295 issuers, 11 sectors; BLS releases; Wikipedia): a shared metric ledger removes **6,845 cross-section contradictions to zero**; tier-first selection is correct on **22/22 gold cases** vs 9/22 popularity-first; trust tiering leaks zero media-sourced numbers and no government statistic displaces a company's filing; a red-team refutation self-corrects a later run with zero manual edits; replay shows zero look-ahead violations across seven cutoffs as the library grows 235K → 555K cards; difficulty-tiered model routing exceeds the all-Opus quality ceiling while running **3.7× faster** than serial.
- **Key innovations**: (1) A maintain-once/write-anytime separation with a point-in-time (as_of ≤ T) contract and deterministic provenance (trust tiers, metric ledger, claim graph); (2) measured elimination of cross-section contradictions and look-ahead leakage; (3) difficulty-tiered routing that beats the all-frontier ceiling at 3.7× speed — an industrial-grade instantiation of the drift-free, provenance-aware research-agent theme.

### 4.5 Intern-S2-Preview: Scientific Agentic Foundation Model

- **arXiv**: [2608.13505](https://arxiv.org/abs/2608.13505) (cs.LG / cs.CL; submitted 2026-08-13) — **NEW**
- **Authors**: Lei Bai, et al. (large Shanghai AI Lab / InternLM-team author list)
- **Institution**: Shanghai AI Laboratory (tentative; InternLM team).
- **Abstract (faithful summary)**: Scientific discovery increasingly needs AI systems that reason over heterogeneous evidence, interact with tools/environments, and sustain long-horizon tasks. **Intern-S2-Preview** is a series of scientific agentic foundation models for multimodal understanding, reasoning, generation, and long-horizon work. Training begins with scientific multimodal pretraining over rendered scientific documents, interleaved image–text data, and scientific corpora; a unified post-training pipeline applies SFT, scalable multi-task RL, black- and white-box agentic RL, and on-policy distillation, stabilized by partial rollout with off-policy correction, adaptive length regularization, online speculative decoding, robust multi-task optimization, and trace-aware experience assembly. The **-397B** member extends time-series modeling from efficient long-sequence understanding to numerical forecasting; a separate **Memory Decoder** path enables rapid scientific specialization without modifying the frozen 397B backbone (Intern-MemDec-4B improves Biology-Instructions from 56.92 to 60.32 on the frozen backbone). Evaluations across scientific, multimodal, agentic, and general-purpose benchmarks show competitive or leading results, with time-series gains on SciTS.
- **Key innovations**: (1) A foundation-model-scale scientific agentic series (up to 397B) with a full SFT/RL/agentic-RL/distillation pipeline; (2) time-series-as-science extension (long-sequence + numerical forecasting); (3) the Memory Decoder as a frozen-backbone specialization path — an architecture/experience of memory-based adaptation consistent with the wiki's memory-vs-weights theme at frontier scale.

---

## 5. Retrieval, Embeddings & IR

### 5.1 The Embedder's Dilemma: LLMs Are Better, but at What Cost?

- **arXiv**: [2608.12875](https://arxiv.org/abs/2608.12875) (cs.CL; submitted 2026-08-13) — **NEW**
- **Authors**: Adnan El Assadi, Niklas Muennighoff, Jinhyuk Lee
- **Institution**: Not stated; author affiliations point to KAUST / Allen AI / Google (tentative).
- **Abstract (faithful summary)**: Should you replace your text-embedding pipeline with an LLM? The paper answers with a controlled, cost-aware comparison of **10 LLMs across 6 families and 26 embedding models (118M–14B params) on 37 tasks** (classification, STS, clustering, pair classification, retrieval). In aggregate the two paradigms are effectively tied: best LLM (Gemini 3.1 Pro, 77.6) vs best embedding model (77.2) — 0.4 points apart. Strengths differ by task: LLMs lead on reasoning-heavy retrieval, embedding models lead on classification, and they match on clustering/STS/pair classification. Parity is expensive: an LLM costs up to **1,431× more than a comparable-quality embedding model (USD 154 vs USD 0.11 per benchmark pass)**, and open LLMs process tokens 2.5–736× more slowly on the same GPU. Reasoning tokens account for 28–81% of LLM inference cost; lower reasoning budgets preserve or improve retrieval quality for most models. The Pareto frontier contains the leading embedding models and one LLM (Gemini 3.1 Pro). Recommendation: a **division of labour** — embedding models for similarity/classification/clustering, LLMs for reasoning-intensive retrieval.
- **Key innovations**: (1) The first controlled, cost-aware head-to-head of LLM-as-embedder vs dedicated embedding models on a 37-task suite; (2) a quantified 1,431× cost gap and reasoning-token cost decomposition; (3) a practical division-of-labour policy — highly relevant to the wiki's retrieval/rec pipelines, and a caution to cost-unaware "just use an LLM" embedding adoption.

### 5.2 A Comprehensive Empirical Evaluation of Vector Database Systems for Approximate Nearest Neighbor Search

- **arXiv**: [2608.12812](https://arxiv.org/abs/2608.12812) (cs.IR; submitted 2026-08-13) — **NEW**
- **Authors**: Ashen Rashmiks, Tiroshan Madushanka
- **Institution**: Not stated; author group overlaps the CLIR paper (University of Colombo, tentative).
- **Abstract (faithful summary)**: Vector databases are critical infrastructure for RAG, semantic search, and recommendation, but comprehensive reproducible benchmarks jointly evaluating retrieval quality, latency, throughput, and resource use are lacking. This paper evaluates **seven systems — FAISS, Qdrant, Milvus, Weaviate, Chroma, pgvector, LanceDB** — across six datasets (SIFT, GIST, MS MARCO, GloVe; >4M vectors; dims 96–960), measuring 15 metrics (Recall@K, Precision@K, MRR, NDCG@K, Hit Rate@K; latency percentiles, QPS, cold-start; index build time, memory, storage). Highlights: on SIFT1M **FAISS** achieves the highest single-node throughput (866 QPS) but lacks database operational features; **Weaviate** provides best out-of-the-box recall (>99%); **Qdrant** offers best latency among full databases (4.55 ms median); **LanceDB** trades retrieval quality for substantially faster index construction. The paper derives system-selection guidelines and releases the benchmark framework open-source.
- **Key innovations**: (1) A broad, reproducible multi-metric benchmark of seven vector-DB systems (quality × performance × resources); (2) task-typed selection guidelines (throughput vs recall vs latency vs build-time); (3) an open benchmarking framework — practical decision support for RAG/rec infrastructure choices the wiki tracks.

### 5.3 Query Translation vs. Cross-Lingual Embeddings for Sinhala-Tamil E-Government Information Retrieval

- **arXiv**: [2608.12820](https://arxiv.org/abs/2608.12820) (cs.IR; submitted 2026-08-13) — **NEW**
- **Authors**: Dharshi Balasubramaniyam, Tiroshan Madushanka
- **Institution**: Not stated; University of Colombo (tentative).
- **Abstract (faithful summary)**: A comparative evaluation of cross-lingual IR (CLIR) for retrieving English government information from Sinhala and Tamil queries. Two paradigms: **Query Translation (QT)** — Google Translate, NLLB, mBART50 — and **Cross-Lingual Embeddings (CLE)** — LaBSE, multilingual E5, BGE-M3 — with monolingual English retrieval as baseline. Experiments use a human-verified benchmark of 500 Sinhala/Tamil/English QA pairs from 1,699 segmented contexts of Sri Lanka's Government Information Center, evaluated by Recall@k (k=1,3,5,10,15). Monolingual retrieval performs poorly (Recall@15 <10%), while all CLIR approaches substantially improve accuracy. **BGE-M3** achieves the highest Recall@15: **96.2% (Sinhala–English) and 95.6% (Tamil–English)**, outperforming the best QT approach (Google Translate: 92.4%/93.0%) while avoiding translation overhead — evidence that multilingual embedding models are more effective and scalable for cross-lingual RAG in low-resource government domains.
- **Key innovations**: (1) A human-verified Sinhala/Tamil↔English government-domain CLIR benchmark; (2) a clean QT-vs-CLE comparison showing BGE-M3-style embeddings beat translation pipelines (and skip translation cost); (3) practical guidance for low-resource cross-lingual RAG deployment.

---

## 6. Time Series, Finance & Market Data

### 6.1 ReCoGen: Represent, Then Generate — Multimodal-Conditioned Time-Series Generation under Irregular Missingness

- **arXiv**: [2608.12592](https://arxiv.org/abs/2608.12592) (cs.LG; submitted 2026-08-12) — **NEW**
- **Authors**: Haochen Zhang, Jiaheng Guo, Yu-Chao Huang, Nicholas Knoz, Tianlong Chen
- **Institution**: Not stated; Tianlong Chen is at UNC Chapel Hill (tentative).
- **Abstract (faithful summary)**: Continuous physiological time series underpin clinical monitoring, yet many informative signals are invasive, expensive, or unavailable. Conditional generation can synthesize an absent signal from co-recorded signals and clinical variables, but existing generators are built around a single conditioning modality and degrade on heterogeneous, irregularly missing mixes of time-variant signals and static covariates. **ReCoGen** is a two-stage framework decoupling multimodal condition representation from target generation: Stage I trains one masked autoencoder per modality, distilling each time-variant condition into a compact, missingness-tolerant token sequence; Stage II trains a **flow-matching generator** fusing these tokens with static conditions to synthesize the target. Across three physiological benchmarks (continuous glucose monitoring on AI-READI; arterial blood pressure on MIMIC-III/IV), ReCoGen attains the best downstream utility on **all sixteen (dataset, task, metric) settings**, surpassing six representative generators; on thirteen it reaches/exceeds the real-signal utility (an approximate anchor, not ceiling). Ablations trace gains to the conditioning path (learnable cross-attention over frozen per-modality encoders, dual token+AdaLN static-condition route).
- **Key innovations**: (1) Two-stage represent-then-generate decoupling for multimodal-conditioned generation; (2) missingness-tolerant per-modality encoders + flow-matching generator; (3) best downstream utility on all 16 physiological settings — a strong representative of the multimodal time-series generation cluster.

### 6.2 DYSANOS: Generative Dynamic Smooth Arbitrage-free Non-parametric Option Surfaces

- **arXiv**: [2608.12587](https://arxiv.org/abs/2608.12587) (cs.LG; submitted 2026-08-12) — **NEW**
- **Authors**: Hans Buehler, Blanka Horvath, Anastasis Kratsios
- **Institution**: Not stated; Buehler is at JPMorgan (tentative).
- **Abstract (faithful summary)**: DYSANOS is presented as the **first generative market model for smooth SANOS option surfaces for all strikes and expiries that are free of static arbitrage**, designed to generate entire paths of daily spot and option prices for years ahead. The paper sets out a robust (if somewhat simplistic) baseline hidden-state generative model in the form of an **AR(1)** model, discusses model setup, data pipeline, and training, and investigates the numerical presence of dynamic arbitrage. Performance is illustrated on OptionMetrics' IvyDB S&P Index data (2020–2025) and compared against a pure implied-vol PCA model.
- **Key innovations**: (1) First static-arbitrage-free generative model of full smooth option surfaces (all strikes/expiries); (2) explicit dynamic-arbitrage investigation on real S&P index data; (3) an AR(1) hidden-state baseline for market simulation — a finance-domain generative-modeling contribution the wiki tracks alongside LOB-generation work (FlowLOB on the 08-14 digest).

### 6.3 LOB-ID: Evaluating Synthetic Market Data by Inception Distances

- **arXiv**: [2608.13082](https://arxiv.org/abs/2608.13082) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Andreea Bacalum, Zhuohan Wang, Ollie Olby, Martin Garaj, Namid Stillman
- **Institution**: Not stated; Zhuohan Wang / Namid Stillman are at UCL (tentative).
- **Abstract (faithful summary)**: Generative models of limit-order-book (LOB) data advance rapidly, but evaluation focuses on stylized facts and selected statistics that may miss the joint temporal and cross-level structure of order-book trajectories. **LOB-ID** adapts the Fréchet Inception Distance (FID) and Monge Inception Distance (MIND) to LOB data, training **DeepLOB** embeddings on four months of Level-2 order-book data for five equities. LOB-ID is stable across time, instruments, and embedding checkpoints, and rises monotonically under controlled distortions. The paper constructs a **moment-matching attack against FID** and a deep-book perturbation that evades statistic-based evaluation; **MIND remains substantially more sensitive to both**. Scoring five generative LOB models (stochastic baselines + deep learning), LOB-ID ranks them in line with the joint temporal/cross-level structure each captures.
- **Key innovations**: (1) FID/MIND adapted to LOB via domain-specific DeepLOB embeddings; (2) adversarial evaluation of the evaluator (moment-matching attack vs FID, deep-book perturbation vs statistics) with MIND winning on robustness; (3) a principled ranking tool for synthetic market-data models — an evaluation-rigor contribution to the finance/LOB generative cluster (cf. FlowLOB).

---

## 7. Games, Game Theory & Mechanism Design

### 7.1 Incidence Bimatrix Games

- **arXiv**: [2608.13001](https://arxiv.org/abs/2608.13001) (econ.TH; submitted 2026-08-13) — **NEW**
- **Authors**: R. B. Bapat, Debapriya Sen
- **Institution**: Not stated; Bapat is at ISI Delhi, Sen at Toronto Metropolitan University (tentative).
- **Abstract (faithful summary)**: The paper solves a natural bimatrix game related to graphs: for a finite directed graph G=(V,E), Player I's strategy set is vertices V and Player II's is edges E, with positive weights {α_e} and {β_e}. If I picks vertex v and II picks edge e, payoffs are zero when non-incident; if e originates at v, I gets α_e and II gets −β_e; if e terminates at v, I gets −α_e and II gets β_e — so the payoff matrices are weighted incidence matrices. When the graph is **acyclic**, Player I has a **unique strategy in any equilibrium** where every vertex is chosen with probability proportional to the maximum directed-path length from that vertex. Defining the path matrix, the set of all equilibrium strategies of Player II is the **convex hull of the column vectors of the path matrix**. This extends Bapat & Tijs (1997) for zero-sum games.
- **Key innovations**: (1) A complete equilibrium characterization for incidence bimatrix games; (2) explicit equilibrium formulas via path lengths / path matrices on acyclic graphs; (3) extension of the classical zero-sum result to bimatrix (non-zero-sum) incidence games — a clean game-theory contribution closing out the econ.TH stream of the batch.

### 7.2 Power in Liquid Democracy: A Network Centrality Approach

- **arXiv**: [2608.13188](https://arxiv.org/abs/2608.13188) (cs.GT; submitted 2026-08-13) — **NEW**
- **Authors**: Davide Grossi, Andreas Nitsche, Georgios Papasotiropoulos, Oskar Skibski, Piotr Skowron, Tomasz Wąs
- **Institution**: Not stated; Groningen / Amsterdam / Warsaw (tentative).
- **Abstract (faithful summary)**: A computationally tractable framework for measuring voters' power in liquid-democracy platforms (transitive and suspendable delegations). The paper employs **Random Walk Decay centrality** to capture how influence propagates through delegation networks, argues for its intuitive appeal and advantages over alternatives such as PageRank, and derives a natural **axiomatic characterization** within the class of power metrics. It also conceptualizes how the framework extends into a practical analysis tool for power distributions and proposes/studies — axiomatically and algorithmically — methods for **selecting representative slates of influential participants**.
- **Key innovations**: (1) Random-Walk-Decay-based power measurement with axiomatic characterization; (2) explicit comparison against PageRank-style alternatives; (3) representative-slate selection methods — a mechanism-design-relevant contribution at the interface of networks and social choice.

### 7.3 Representation in Peer Selection: A Liquid Democracy Perspective

- **arXiv**: [2608.13085](https://arxiv.org/abs/2608.13085) (cs.GT; submitted 2026-08-13) — **NEW**
- **Authors**: Davide Grossi, Grzegorz Lisowski, Georgios Papasotiropoulos
- **Institution**: Not stated; University of Amsterdam / Groningen (tentative).
- **Abstract (faithful summary)**: In the peer-selection problem a group selects a fixed-size committee from among itself. The paper introduces a class of approval-based preference profiles inspired by delegation graphs in liquid democracy — **liquid profiles** — where each voter designates a single trusted agent and approves all those trusted by that individual. After establishing relationships to standard restricted profiles and examining computational properties, the paper studies how novel and established **proportionality axioms** behave in this domain and how they relate, then evaluates their satisfaction under various voting rules (including new ones inspired by the liquid-profile structure). Findings show **particularly strong proportionality guarantees are attainable** in this domain, promising for real-world peer selection via transitive delegations.
- **Key innovations**: (1) A new domain restriction (liquid profiles) linking peer selection to liquid-democracy delegation structure; (2) a proportionality-axiom map within the domain; (3) new voting rules with strong proportionality guarantees — pairs with the Power-in-Liquid-Democracy paper as the batch's social-choice cluster.

---

## 8. Benchmarks, Evaluation & Theory

### 8.1 LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation

- **arXiv**: [2608.13136](https://arxiv.org/abs/2608.13136) (cs.AI / cs.CL / cs.MA; submitted 2026-08-13) — **NEW**
- **Authors**: Chenrun Wang, Mingxuan Zhu, Tiancheng Huang, Wenjie Li, Yujie Zhang, Zichen Zhu, Zhiying Zou, Kai Yu, Lu Chen
- **Institution**: Not stated; Kai Yu / Lu Chen are at Shanghai Jiao Tong University (tentative).
- **Abstract (faithful summary)**: LLM-based research idea generation is attracting attention, but evaluation remains fragmented and lacks objective standards — often direct LLM scoring, which limits unified/reliable assessment across coherent distributions of generated ideas. **LigBench** is an automated evaluation benchmark enabling fine-grained, reliable evaluation of AI research ideas, consistently applicable across different generation distributions. It also introduces **PAIR-IQ**, a dataset for training pairwise idea-judgment models serving as an auxiliary reference for more objective comparison. Experiments show LigBench achieves stable, interpretable evaluations with significantly improved alignment with expert judgments; models trained on PAIR-IQ exhibit enhanced ranking accuracy and robustness.
- **Key innovations**: (1) A unified, distribution-agnostic benchmark for research-idea generation evaluation; (2) a pairwise-judgment training dataset (PAIR-IQ) reducing reliance on raw LLM scoring; (3) demonstrated expert-alignment improvement — relevant to the wiki's AutoResearch/AI-scientist thread (OmniScientist, Replica/Faraday, ARAC).

### 8.2 Sampling Luck Masquerades as Allocation Gain: Auditing Test-Time Budget Allocation for Neural Combinatorial Optimization

- **arXiv**: [2608.13087](https://arxiv.org/abs/2608.13087) (cs.AI / cs.LG; submitted 2026-08-13) — **NEW**
- **Authors**: Jinhyung Bae
- **Institution**: Not stated.
- **Abstract (faithful summary)**: NCO solvers report the best of many sampled solutions per instance, with the sample count conventionally identical per instance; whether non-uniform allocation of a fixed budget buys anything has not been measured. The paper measures it — and audits the measurement. On in-distribution workloads the allocation headroom is not detectable: across POMO, AM, and SymNCO on uniform TSP-100, an oracle allocation computed and evaluated on the same stored samples reports a 2.2–2.6% gain with intervals excluding zero, but measured out-of-sample the same gain is indistinguishable from zero (0.457, 0.015, −0.512 percent) — the customary in-sample procedure would have supported a published 2%-level gain that does not exist. The bias does not shrink with more samples or instances. Under distribution shift, a pre-registered confirmatory experiment finds allocation guided by held-out statistics improves best-of-k by **11.5% (AM; 95% CI [7.4, 19.7]) and 12.0% (SymNCO)** at equal budget, while a pre-registered negative control (POMO, order-of-magnitude more shift-robust) shows −0.3%. The paper gives a correction procedure and a reporting checklist, and releases data, code, and the pre-registration record.
- **Key innovations**: (1) A rigorous audit showing in-sample "allocation gain" in NCO is sampling luck that vanishes out-of-sample; (2) a correction procedure + reporting checklist for test-time budget allocation claims; (3) a pre-registered confirmatory design distinguishing real shift-driven gains (AM/SymNCO) from phantom ones (POMO) — an evaluation-integrity contribution in the spirit of the wiki's methodology/auditing thread (cf. A/B testing rigor papers).

### 8.3 The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity

- **arXiv**: [2608.13520](https://arxiv.org/abs/2608.13520) (cs.AI / cs.LG / stat.ML; submitted 2026-08-13) — **NEW**
- **Authors**: Martin J. Wainwright
- **Institution**: UC Berkeley / MIT (tentative).
- **Abstract (faithful summary)**: A study of masking diffusion for discrete sampling introducing a path-resolved measure of data geometry, the **unmasking growth complexity (UGC)**. Its local increments directly control **KL discretization error**, yielding a unified analysis of Bernoulli-subset and fixed-cardinality unmasking schemes. In log-reveal-odds coordinates, this yields optimized single-block and multi-block schedules and quantifies the gains from adapting computational effort to data geometry. Crucially, UGC increments can be estimated from samples via KL increments along coupled reveal trajectories, giving **certified-optimal samplers** that achieve a prescribed KL error with high probability and iteration complexity within a constant factor of the oracle. Collapsing the UGC path yields the aggregate UGC mass, connecting to classical multivariate dependence measures and prior complexity analyses of discrete diffusion; in the fine-partition limit, the squared integral of the square-root UGC density determines the sharp leading-order optimal Euler discretization error. Examples exhibit substantial dimension-dependent gains over coarse schedules, including **Ω̃(√d) improvements with a constant number of adaptively placed blocks**.
- **Key innovations**: (1) UGC as a path-resolved, sample-estimable measure of discrete-data geometry directly bounding KL error; (2) certified-optimal masking schedules with oracle-constant iteration complexity; (3) a fine-partition sharp limit tying UGC density to optimal Euler error — a strong theoretical contribution to discrete diffusion (connecting to the wiki's diffusion-modeling coverage).

### 8.4 Numeracy in Large Language Models: Fundamental Limitations and Paths to Improvement

- **arXiv**: [2608.13129](https://arxiv.org/abs/2608.13129) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Aoxin Ni
- **Institution**: Not stated.
- **Abstract (faithful summary)**: LLMs achieve strong results on math-reasoning benchmarks yet remain unreliable on elementary numerical tasks (magnitude comparison, large-integer arithmetic, fractions, scientific notation). This survey examines basic numerical understanding as a capability distinct from high-level reasoning, proposing the **Numerical Grounding Framework (NGF)**, which decomposes numeracy into **Representational Grounding (RG)** — mapping numeral forms to value, magnitude, and equivalents — and **Procedural Grounding (PG)** — executing arithmetic operations per their definitions. Using NGF, the survey organizes diagnostic benchmarks, failure modes, structural explanations (tokenization, positional encoding, embedding geometry, pretraining-data distribution), and mitigations, and applies NGF in a coordinated evaluation of three frontier model families across Number Cookbook, NumericBench, and GSM-Symbolic (atomic/contextual/reasoning-assisted numeracy). Architectural interventions (digit-aware tokenization, Abacus Embeddings) help from-scratch training but are unavailable to users of pretrained systems, for whom SFT, reasoning scaffolds, and external tools are more practical. Concludes with deployment recommendations and research directions.
- **Key innovations**: (1) A unified framework (NGF: RG + PG) separating numeracy from high-level math reasoning; (2) an organized evidence map of failure modes and structural causes; (3) a practical distinction between from-scratch architectural fixes and post-hoc interventions for pretrained models — a useful capability-taxonomy complementing the wiki's math-reasoning coverage.

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **The cost of embeddings gets measured** | Embedder's Dilemma shows LLM-as-embedder ties dedicated models in aggregate (77.6 vs 77.2) but costs up to 1,431× more; Vector DB eval compares seven ANN systems across 15 metrics; Sinhala-Tamil CLIR shows embedding-based cross-lingual retrieval beats translation and skips its cost | Embedder's Dilemma, Vector DB eval, CLIR |
| **Agent memory splits: access protocols vs evolvable retrieval** | @skills separates content/persistence/triggering so skills need no prompt residency; ERSkill makes retrieval itself an evolvable skill set (double-frontier safety); SMA does tool-free, parameter-free spatial self-evolution via TRS-calibrated lessons; Reconcile Once builds a deterministic trust-tiered librarian with as_of-point-in-time reporting | @skills, ERSkill, SMA, Reconcile Once |
| **The economics of search and decision-making tighten** | Algorithm transparency changes whether ranking manipulates search (steering vs persuasion, welfare non-monotonic); the NCO budget-allocation audit shows in-sample "allocation gain" is sampling luck that vanishes out-of-sample (pre-registered confirmatory design) | Algorithm Transparency, Sampling Luck |
| **Post-training: coverage vs exploitation** | ES achieves higher pass@k and broader output coverage than RL, which collapses the output distribution; CABS+ makes model merging gradient-free and mergeability-quantifiable (RSS); ε-MemEvo gates cross-task memory transfer with an interpretable skip→hint posterior; CSE maps phase transitions in multi-constraint compliance | Beyond the Best Guess, CABS+, ε-MemEvo, CSE |
| **Generative market/finance modeling matures with evaluation rigor** | DYSANOS generates full static-arbitrage-free option surfaces (with dynamic-arbitrage checks); LOB-ID adapts FID/MIND to order-book data and adversarially audits its own evaluator (MIND more robust than FID); ReCoGen wins all 16 physiological time-series settings with a represent-then-generate design | DYSANOS, LOB-ID, ReCoGen |
| **Social choice takes the cs.GT/econ.TH tail** | Incidence bimatrix games solved for acyclic graphs (unique vertex strategy, convex-hull path-matrix equilibria); liquid-democracy pair — Random Walk Decay power + liquid-profile peer-selection proportionality | Incidence Bimatrix, Power in Liquid Democracy, Peer Selection |
| **Efficient LLM training/serving still finds structure** | LoKiFormer's conv-fused attention + decoupled knowledge memory gives 1.33× pretraining speedup; trie automata give 29× batch constrained-decoding throughput; RoutePack jointly packs attention and expert work in MoE RL (8.85–14.89%) | LoKiFormer, Trie Automata, RoutePack |

---

## Key Takeaways

1. **The embedder-vs-LLM question now has a cost-accounting.** At 0.4 points aggregate apart, the choice is task-driven: embedding models for similarity/classification/clustering, LLMs for reasoning-heavy retrieval — at up to 1,431× cost difference. This is the retrieval-pipeline cost calculus the wiki's rec/ads coverage needs when evaluating "LLM-everything" adoption.
2. **Agent memory is splitting along an access/evolution axis.** @skills removes the prompt-residency tax from skill delivery (content/persistence/triggering separated), while ERSkill, SMA, and Reconcile Once make retrieval/lesson provenance evolvable and calibrated. The recurring pattern: runtime memory/access structure is where capability gains now concentrate — consistent with the wiki's memory-vs-weights thread.
3. **Evaluation audits are tightening across domains.** The NCO budget-allocation audit shows in-sample gains that are pure sampling luck (pre-registered, corrected); LOB-ID adversarially attacks its own evaluator (MIND beats FID under moment-matching attacks); LigBench replaces raw LLM scoring with pairwise human-aligned judgment; CSE gives a deterministic map of multi-constraint collapse (below 50% at ≤3 constraints for 12/15 models). "Audit the measurement" is a batch-wide signature.
4. **ES challenges RL for discovery-oriented post-training.** Beyond-the-Best-Guess shows RL narrows the output distribution and hurts pass@k, while weight-space ES preserves coverage and improves math-benchmark outcomes — a direct counterpoint to the RLVR-heavy post-training line, worth flagging as a coverage-vs-exploitation trade-off.
5. **Finance generative modeling pairs construction with evaluation.** DYSANOS (arbitrage-free option surfaces with dynamic-arbitrage checks) and LOB-ID (adversarially-audited LOB data evaluation) together show the market-data domain moving from "can we generate" to "is it valid and how do we know" — mirroring the wiki's generative-modeling rigor theme (FlowLOB).
6. **No new dedicated advertising/CTR paper beyond the 08-14 picks.** The cs.IR stream (19 new) was already claimed by 08-14's paper-check (7 CTR/Rec/Ads/IR papers); this digest's closest platform-economics item is the econ.TH algorithm-transparency paper.

> ⚠️ Note on sourcing: arXiv announces new listings Mon–Fri; there is no Sat–Sun Aug 15–16 announcement, so this digest is a **no-overlap supplementary curation of the Fri Aug 14, 2026 batch** (submissions Aug 12–13). All 26 arXiv IDs were verified against the arXiv category listing pages (`cs.AI` 205, `cs.LG` 158, `cs.CL` 101, `cs.IR` 19, `cs.GT` 6, `cs.MA` 13, `econ.TH` 6, `stat.ML` 29) and the arXiv API, and grep-checked 0 hits across wiki/index.md, wiki/log.md, and wiki/synthesis/** (zero overlap with the 08-14 digests and today's 08-16 arxiv-ai-search). All 26 carry published dates 2026-08-12/13 within the window (no earlier-v1-date caveats needed). Institution attributions marked "(tentative)" are inferred from author affiliations, not the arXiv record; "not stated" means not identified.
