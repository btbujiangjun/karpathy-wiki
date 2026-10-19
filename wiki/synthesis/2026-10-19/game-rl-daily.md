---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-19)"
type: synthesis
created: 2026-10-19
updated: 2026-10-19
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, multi-agent, game-theory, foundation-models, world-models, pcg, benchmarks, npc, imitation-rl, bandits, proceedings, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-19)

> A **seven-lane sweep** (Game RL, Game AI Bot, Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, Related Techniques) run on **Monday 2026-10-19 (from ~11:00 CST)**, plus a **backward-window pass over submissions 28 Sep – 8 Oct**. **Method note up front**: the **Monday 10-19 arXiv block is live** this run — the sibling [`arxiv-ai-search` 2026-10-19](../2026-10-19/arxiv-ai-search.md) reported that "the Monday block had not appeared at search time" because it ran earlier; the sibling [`tech-report-digest` 2026-10-19](../2026-10-19/tech-report-digest.md) independently scraped the same block (**cs.CL 226 / cs.AI 344 / cs.LG 391 / cs.CV 201 = 1,162 titles**). This run parsed **all ten game-relevant `/list/*/new` categories** (cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.GT, cs.HC, cs.SD, cs.NE) → **1,034 unique entries with abstracts** = **631 new-band IDs (2610.22373–2610.23856, v1 submitted 15–16 Oct)** + **403 cross-listed/re-announced older entries** (oldest 1906.07073). The arXiv **export API returned HTTP 429** for this run's batch attempts (the same wall as the 10-15…10-18 runs), so metadata came from `/list` HTML, `/abs/{id}` and LaTeXML `/html/{id}vN` pages. A parallel date-ranged search sweep (**28 Sep – 8 Oct**, 40 game-lane queries, `search/advanced`) yielded **228 unique candidates**, of which **18** survive title/abstract triage and are used here (**3 promoted to featured: Gambit `2605.09027`, HARL-A `2510.01264`, humanoid table tennis `2610.14067`; 15 as residue bullets**, including 2 further items surfaced after that sweep: `2610.08129`, `2604.06189`). **33 papers featured in full, all 62 fresh IDs grep-verified 0-hit** against the live `wiki/**/*.md` tree before writing; **29 more logged as "also fresh"** in per-lane bullet lists. **13 on-file in-lane papers are cross-referenced, not repeated** (§0.3).
>
> **Three threads run through this pass.**
>
> **① A two-paper *allocations/equilibrium* correction-and-convergence pair anchors the game-theory lane.** [`2610.23686`](https://arxiv.org/abs/2610.23686) (AUEB/Athena RC + UNSW + Liverpool + Sapienza + Amsterdam) **corrects a published claim**: it shows that *not* every pure Nash equilibrium of the **Round-Robin** picking sequence is **EF1**, giving a counterexample and identifying the step where the original WINE-2021 / *Math. Oper. Res.* proof fails — then proves the positive result that every pure NE of any fixed **recursively balanced** picking sequence is **1/2-EF1 and PROP1**, with a family showing no guarantee better than **2/3-EF1** is possible. The same week, [`2610.23040`](https://arxiv.org/abs/2610.23040) (LIP6/CNRS/Sorbonne + U Paris 1) studies **iterated Round Robin** under best-response preference revision, showing cycles can occur even under strong manipulation restrictions, but that **item-preserving swaps** converge to a pure NE for any number of agents/items, and that a cautious partial-information rule makes iterated RR **strategyproof**. Around them sit fresh equilibrium-learning results: Bayesian recovery of **parametric mean-field games with common noise** (`2610.23387`), **observation-safe counterfactual coupling** for imperfect-information policy gradients (`2609.33543`), and a complete learnability characterization for **adversarial noisy bandits** (`2605.09200`).
>
> **② Language-game agents get a measurement trio — and one of them is a new ALE reimplementation.** [`2610.22953`](https://arxiv.org/abs/2610.22953) (U Washington) builds a **controlled Go evaluation set for *atari* and *sente*** and shows a fine-tuned Go language model struggles to recognize *atari* changes and their strategic implications; [`2610.23166`](https://arxiv.org/abs/2610.23166) introduces an automatic metric for **chess explanations** grounded in engine evaluations, finds LLMs perform "surprisingly poorly", and offers **BinProp**, a training-free method that nearly triples explainability scores and transfers to Go, draughts and shogi; and [`2610.23650`](https://arxiv.org/abs/2610.23650) (TU Darmstadt + Google Intrinsic AI Research + Hessian.AI + DFKI) releases **JAXtari**, a GPU-parallel reimplementation of the **Arcade Learning Environment** that trains PPO for **100M steps on a single A100 in under an hour** and adds **object-centric observations** and a modification system for causal-model research.
>
> **③ Video world-model *memory* is the sharpest foundation-model subplot — and the PCG and studio lanes are empty again.** [`2610.23542`](https://arxiv.org/abs/2610.23542) (HKU + U Michigan + PKU) **MIST** separates *executing a change* from *remembering it*, diagnoses that video world models often **set the scene but never carry out the instructed change**, and its **M3-Agent** more than triples the reveal score; [`2610.23423`](https://arxiv.org/abs/2610.23423) (INSAIT + Harvard + Ulm + TUM) **Momentum** uses synchronized **camera-rig graphs** to keep dynamic content alive outside the view (+126.2% consistency); and [`2610.23795`](https://arxiv.org/abs/2610.23795) (Tsinghua + Ant Group + HKUST, **NeurIPS 2026**) **PPMem** uses **oriented planes** as a compact persistent 3D memory. Their evaluation counterpart, [`2610.22708`](https://arxiv.org/abs/2610.22708) **GlobeBench**, finds **631 of 1,632 tasks remain unsolved by any of 20 LLMs/world models** (GPT-6 Astra tops out at **49.57%**). §4 (PCG) and §6 (studio) carry **no fresh in-lane paper** — targeted queries for `pcg / nethack / npc` and for studio terms returned **zero in-window hits** (§0.2), so §4 is a lane note and §6 leans on the featured LoongSage RL framework plus competition/proceedings news.

---

## §0 Method and Corpus

### 0.1 Coverage
- **Window**: the **Monday 2026-10-19 arXiv block is live** this run (v1 submissions **15–16 Oct**, new-band IDs `2610.22373–2610.23856`), with `./list/*/new` for ten categories parsed into `monday.json`; a complementary **backward sweep over submissions 28 Sep – 8 Oct** (the early-week residue the daily series had not drained).
- **Sources**:
  1. **`/list/{cat}/new` HTML** for cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.GT, cs.HC, cs.SD, cs.NE → **1,034 unique entries with abstracts** = **631 new-band (2610.22373–2610.23856)** + **403 cross-listed/re-announced older** (oldest `1906.07073`). Raw per-category entries: cs.LG 391 / cs.AI 344 / cs.CL 226 / cs.CV 201 / cs.RO 121 / cs.HC 35 / cs.SD 31 / cs.MA 29 / cs.GT 20 / cs.NE 9.
  2. **Date-ranged `search/advanced` sweep (28 Sep – 8 Oct)**: **40 game-lane queries** (`self-play`, `marl_rl`, `pcg`, `levelgen`, `atari`, `nethack`, `starcraft`, `minecraft`, `poker`, `hanabi`, `npc`, `gameagent`, `gameplaying`, `gamebot`, `openended`, `oppmodel`, `wm_game`, `chess`, `dota`, `fdn_game`, `invrl`, `imit_game`, `offrl_game`, `rewardshape`, `curiosity`, `pbt`, `qualitydiv`, `markovgame`, `nasheq`, `efg`, `cfr`, `alphazero`, `gamefdn`, `llmgameagent`, `muzero`, `openaifive`, `grids`, `crafting`, `nmmo`, …) → **228 unique candidates**, **61** pass a title gate, **18** used.
  3. **Proceedings/competition web pass**: IEEE CoG 2026 and AIIDE 2026 (deferred — no public papers this run).
- **Filter**: game-lane keyword sweep with a noise filter (finance/medicine/sports senses of "game"); broad gate flagged **707** (658 fresh / 49 on-file); strict triage `t1` = **33** fresh (22 used, 11 off-lane), `t2` = **8** on-file; complementary title-slices added 22; **manual abstract triage**, then **freshness gate** (0-hit `grep` against `wiki/**/*.md`), then feature-ranking. **33 featured in full; 29 additional fresh items** carried as bullets (14 Monday + 15 backward residue).

### 0.2 Sweep and negative results
1. `/list` HTML via `curl` + browser UA; `/abs/{id}` pulls at ≥1.5 s delay; LaTeXML `/html/{id}vN` pulls for printed affiliations (`aff/`, `babs/`).
2. **Targeted empty-lane queries (in-window)**: `pcg`, `nethack`, `npc`, `gamebot`, `oppmodel`, `cfr`, `gamefdn`, `openaifive`, `nmmo`, `offrl_game` → **0 results each**. `levelgen`/`crafting`/`grids`/`openended`/`qualitydiv` returned fresh hits, but **all audited off-lane** (PXtal crystal diffraction, CRAFTER IoT, Hessian null space, etc.) — so **no classic-PCG item exists anywhere in the window**.
3. **Dedup**: every candidate ID `grep`-tested against the whole `wiki/` tree before featuring (§0.3). All **62 fresh IDs verified 0-hit**.

### 0.2.1 Rate limiting and tooling
- **Export API**: `https://export.arxiv.org/api/query` → **HTTP 429** throughout (same wall as 10-15…10-18). A **single 429** also hit the `search/advanced` sweep mid-way (after `qualitydiv`) and was auto-retried.
- **Search/abs/html pages**: HTTP 200 via `curl` + browser UA.
- **Bash caveat (zsh)**: unquoted `$var` loops do **not** word-split in zsh; a freshness-check loop over the featured IDs was rewritten as a Python subprocess loop after a zsh `for id in $ids` silently checked only the first ID.

### 0.3 Dedup accounting (featured + notable fresh items)
| arXiv ID | Lane | Cat | Status |
|----------|------|-----|--------|
| 2610.23686 (Round-Robin NE fairness, corrected) | Game RL / GT | cs.GT | **fresh, featured** |
| 2610.23040 (iterated Round Robin convergence) | Game RL / GT | cs.GT | **fresh, featured** |
| 2610.23565 (distributional MCTS, CVaR) | Game RL | cs.LG | **fresh, featured** (NeurIPS 2026) |
| 2610.23650 (JAXtari ALE) | Game RL | cs.LG | **fresh, featured** |
| 2609.33543 (OSCC, imperfect-info coupling) | Game RL | cs.GT/cs.LG/cs.AI | **fresh, featured** |
| 2604.01151 (multi-agent collusion detection) | Game RL / MAS | cs.LG/cs.MA/cs.AI | **fresh, featured** |
| 2605.06557 (process-aware cooperative MARL eval) | Game RL | cs.LG/cs.MA/cs.AI | **fresh, featured** |
| 2610.23387 (Bayesian MFG common noise) | Game RL / GT | cs.GT | **fresh, featured** |
| 2605.09200 (adversarial noisy bandits learnability) | Game RL / bandits | cs.LG | **fresh, featured** |
| 2610.22683 (closed-credit auction, ATM slots) | Game RL | cs.GT/cs.MA | **fresh** (bullet) |
| 2610.23157 (Cross-Centaur, individual decision-making) | Game RL / HAI | cs.CL | **fresh** (bullet); EMNLP 2026 Oral |
| 2209.14128 (liquid-democracy delegation equilibria) | Game RL / GT | cs.MA | **fresh** (bullet) |
| 2605.09027 (Gambit, imposter-detecting collectives) | Game AI Bot | cs.MA | **fresh, featured** (promoted) |
| 2610.19863 (extremists in LLM societies, EXAM) | Game AI Bot | cs.MA | **fresh, featured** |
| 2607.11250 (MACE, multi-agent exploration) | Game AI Bot | cs.MA/cs.AI | **fresh, featured** (NeurIPS 2026 IAEval Oral) |
| 2610.22701 (emergent discrimination/polarization) | Game AI Bot | cs.MA | **fresh, featured** |
| 2610.23056 (Thought Blocks, latent communication) | Game AI Bot | cs.MA | **fresh, featured** |
| 2610.22674 (Gossip Agents, reputation diffusion) | Game AI Bot | cs.MA | **fresh, featured** |
| 2508.17366 (CMASE generative-agent society experiments) | Game AI Bot | cs.MA/cs.AI | **fresh, featured** (ACM TSC) |
| 2610.22915 (Reward Engine, self-evolution agents) | Game AI Bot | cs.AI | **fresh, featured** |
| 2610.22953 (Go atari/sente evaluation) | Game AI Bot / language | cs.CL | **fresh, featured** |
| 2610.23166 (chess/Go explanation metric + BinProp) | Game AI Bot / language | cs.CL/cs.LG/cs.AI | **fresh, featured** |
| 2610.22740 (R²Orch self-play orchestration) | Game AI Bot | cs.AI | **fresh** (bullet) |
| 2604.24698 (persona collapse/homogenization) | Game AI Bot / MAS | cs.CL | **fresh** (bullet) |
| 2610.23542 (MIST video-WM memory diagnosis) | Game Fdn | cs.CL/cs.CV | **fresh, featured** |
| 2610.23423 (Momentum, persistent dynamics) | Game Fdn | cs.CV | **fresh, featured** |
| 2610.23795 (PPMem, persistent planar memory) | Game Fdn | cs.CV | **fresh, featured** (NeurIPS 2026) |
| 2605.16395 (OrbiSim, differentiable physics engine) | Game Fdn | cs.LG/cs.RO | **fresh, featured** |
| 2510.08713 (UniWM unified navigation world model) | Game Fdn | cs.CV | **fresh** (bullet) |
| 2610.22619 (FCTS terrain curriculum tree search) | PCG / related | cs.RO | **fresh** (bullet) |
| 2610.22708 (GlobeBench text world-model benchmark) | Benchmarks | cs.CL/cs.AI | **fresh, featured** |
| 2510.01264 (HARL-A heterogeneous adversarial MARL) | Benchmarks | cs.RO | **fresh, featured** (promoted) |
| 2610.16352 (LoongSage agentic RL framework) | Industry | cs.CL/cs.LG | **fresh, featured** |
| 2610.14067 (humanoid table tennis, strategy) | Industry | cs.RO | **fresh, featured** (promoted) |
| 2610.23148 (grounded credit assignment, search agents) | Related | cs.LG | **fresh, featured** |
| 2610.23181 (TreeOPSD posterior distillation) | Related | cs.CL/cs.LG/cs.AI | **fresh, featured** |
| 2610.23445 (RecReg recovery-based shielding) | Related / safe RL | cs.LG/cs.AI | **fresh, featured** |
| 2610.23550 (reason-guided human reward modeling) | Related | cs.RO/cs.AI | **fresh, featured** |
| 2610.22852 (AnchorQ flow-reversed action anchors) | Related | cs.RO/cs.AI | **fresh, featured** |
| 2508.03904 (information-ordered policies) | Related / RL theory | cs.LG | **fresh, featured** |
| 2610.23048 (Distill Until Divergence) | Related | cs.AI | **fresh** (bullet) |
| 2610.22665 (EquivAug symbolic equivalence) | Related | cs.AI | **fresh** (bullet); AACL 2026 |
| 2610.23470 (QD-Rec quality-diversity) | Related / QD | cs.LG/cs.NE/cs.AI | **fresh** (bullet) |
| 2610.22973 (DiffusionRVGE value-gradient) | Related | cs.AI | **fresh** (bullet) |
| 2610.22781 (anytime contracts for AI services) | Related / contract theory | cs.GT/cs.LG | **fresh** (bullet) |
| 2610.23402 (contracting under model mismatch) | Related / contract theory | cs.GT/cs.LG | **fresh** (bullet) |
| 2610.22448 (Lean4AgenticRL multi-level process rewards) | Related | cs.LG | **fresh** (bullet) |
| 2610.08129 (Hanabi partner conventions, LLM actions) | residue | cs.LG | **fresh** (bullet) |
| 2604.06189 (Shogi state-space complexity, MC) | residue | cs.AI | **fresh** (bullet) |
| 2002.12119 (path polymatrix games PPAD-hard) | residue | cs.GT | **fresh** (bullet) |
| 2210.03852 (Stackelberg POMDP) | residue | cs.LG/cs.GT/cs.MA | **fresh** (bullet) |
| 2601.12310 (survival-only self-training) | residue | cs.AI | **fresh** (bullet) |
| 2605.09278 (EquiMem, multi-agent debate) | residue | cs.MA | **fresh** (bullet) |
| 2606.01382 (ENPO Nash preference optimization) | residue | cs.LG | **fresh** (bullet) |
| 2607.18255 (semantic cooperative games attribution) | residue | cs.GT/cs.AI | **fresh** (bullet) |
| 2609.34695 (zeroth-order reward shaping) | residue | cs.LG/cs.RO | **fresh** (bullet) |
| 2609.35052 (OPIS multi-object video-WM memory) | residue | cs.CV | **fresh** (bullet) |
| 2609.35928 (prompted identity degrades cooperation) | residue | cs.MA | **fresh** (bullet) |
| 2610.01882 (OMAF one-step flow policies) | residue | cs.LG/cs.MA | **fresh** (bullet) |
| 2610.04614 (feedback Nash via MPC) | residue | cs.GT/eess.SY | **fresh** (bullet) |
| 2610.06885 (dynamical low-rank equilibrium, MTD) | residue | cs.GT | **fresh** (bullet) |
| 2610.09337 (LLM-guided RL cyber defense) | residue | cs.AI | **fresh** (bullet); IEEE GLOBECOM 2026 |
| 2610.22882 / 2610.20200 / 2610.19422 / 2610.17895 / 2610.22626 / 2610.22779 | various | — | **on-file** (cross-ref, §Cross-references) |
| 2609.32544 / 2610.00416 / 2610.08621 / 2610.11723 / 2610.13947 / 2610.20473 / 2610.21711 | various | — | **on-file** (cross-ref) |

**Sibling editions on file for this week** (cross-referenced, not re-featured): [`arxiv-ai-search` 2026-10-19](../2026-10-19/arxiv-ai-search.md), [`tech-report-digest` 2026-10-19](../2026-10-19/tech-report-digest.md) (independently corroborates the Monday block counts), [`conference-digest` 2026-10-19](../2026-10-19/conference-digest.md) (defers the games lane), [`arxiv-daily` 2026-10-19](../2026-10-19/arxiv-daily.md) (carries **none** of this edition's 62 IDs), and the 10-16/10-17/10-18 `game-rl-daily` editions.

### 0.4 Affiliations and venues
- Affiliations are reported only from the paper's own rendered LaTeXML `Affiliation:` author block or the rendered author footnote; otherwise **"not stated"** — *never inferred* from surnames or email domains.
- **29 of 33 featured affiliations recovered; 4 not stated**: `2610.23166` (empty author block), `2610.22708` (LaTeXML page returned 404), `2610.16352` (only "Team" printed), `2610.23181` (numeric affiliation markers with no unit list). Three affiliations came from the rendered **body footnote** (`2508.03904`, `2610.22852`, `2610.23387`).
- Venues are stated **only where explicit** (NeurIPS 2026, NeurIPS 2026 IAEval Workshop, EMNLP 2026, AACL 2026, ACM TSC, IEEE GLOBECOM 2026, "Under review"); otherwise `arXiv preprint`. **No result independently replicated.**

### 0.5 Temp artifacts
- Scratch dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/gamerl1019/` (`monday.json`, `known_ids.txt`, `triage*.json`, `featured_abstracts.txt`, `backward_abs.txt`, `babs/`, `aff/`, `dates.json`, parsed scripts) — deleted after this write-up.
---

## §1 Game RL — Reinforcement Learning, Self-Play, Multi-Agent & Game Theory

### ★★★ Revisiting the Fairness of Pure Nash Equilibria of Round-Robin
- **Authors**: Georgios Amanatidis, Haris Aziz, Georgios Birmpas, Federico Fusco, Stefano Leonardi, Rebecca Reiffenhäuser
- **Affiliation**: Department of Informatics, Athens University of Economics and Business; Archimedes / Athena RC; UNSW Sydney; University of Liverpool; Sapienza University of Rome; Institute for Logic, Language and Computation, University of Amsterdam.
- **Venue**: arXiv:2610.23686 (16 Oct 2026) — `cs.GT`. Comment: **corrects the claim in arXiv:2109.08644 (WINE 2021; Math. Oper. Res. 49(4), 2024)**.
- **Link**: https://arxiv.org/abs/2610.23686
- **Abstract and key innovations**: For additive valuations, the paper shows that **not every pure Nash equilibrium of the Round-Robin mechanism induces an EF1 allocation** with respect to agents' true valuations — explicitly correcting the earlier Amanatidis et al. claim. It gives a counterexample and identifies **the step of the original proof that fails**. On the positive side, **every pure NE of every fixed recursively balanced picking sequence** induces an allocation that is **1/2-EF1 and PROP1**; the approximate-EF1 guarantee is proved via a **potential function comparing two executions**, the proportionality via a **deviation that preserves the agent's most valuable goods**. It also exhibits a family of Round-Robin equilibria showing **no guarantee strictly better than 2/3-EF1 is possible for all equilibria**.
- **Why it matters here**: it is a rare **self-correction of a published game-theory result** that directly affects fair-division-of-indivisible-goods mechanisms — the "asked for something stronger than is true" pattern is worth tracking, and the potential-function method is a reusable proof template for picking-sequence fairness.
- **Caveats**: **fully fresh — 0 hits in wiki**; additive valuations only; correction concerns the *strength* of the equilibrium guarantee, not the existence of EF1 allocations.

### ★★★ On the Convergence of Iterated Round Robin
- **Authors**: Maxime Lucet, Henri Surugue, Nawal Benabbou, Aurélie Beynier, Nicolas Maudet, Arianna Novaro
- **Affiliation**: LIP6, CNRS, Sorbonne Université; Université Paris 1 Panthéon-Sorbonne, CNRS, CES.
- **Venue**: arXiv:2610.23040 (16 Oct 2026) — `cs.GT`.
- **Link**: https://arxiv.org/abs/2610.23040
- **Abstract and key innovations**: **Round Robin (RR)** guarantees EF1 under additive preferences and, though manipulable, always admits a pure Nash equilibrium. This paper studies an **iterated variant** in which agents observe outcomes each iteration and revise reported preferences by **best responses**. In a **full-information** setting, **cycles can occur even under strong manipulation restrictions**, but a natural restriction — **item-preserving swaps** — guarantees convergence to a pure NE **for any number of agents and items**; restricting to **adjacent swaps** guarantees convergence for two agents and a bounded number of items (open for unbounded items). In a **partial-information** setting (agents see only the allocation and infer others' preferences consistent with the RR sequence), two natural manipulation behaviours may cycle while a **more cautious rule makes iterated RR strategyproof**.
- **Why it matters here**: mechanism dynamics under strategic preference revision is exactly the **repeated-allocation game** behind drafting/matching systems; the item-preserving-swap result is the useful, implementable convergence condition, and it pairs directly with the correction above as a same-week Round-Robin duo.
- **Caveats**: **fully fresh — 0 hits in wiki**; theoretical (no empirical tournament); adjacent-swap convergence limited to two agents.

### ★★ Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search
- **Authors**: Quynh Trinh, Trung Nguyen, Nam Nguyen, Tuan Dam
- **Affiliation**: Hanoi University of Science and Technology; Center for AI Research, VinUniversity.
- **Venue**: **Proceedings of the 40th Annual Conference on Neural Information Processing Systems (NeurIPS 2026)** — also arXiv:2610.23565 (16 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.23565
- **Abstract and key innovations**: Standard MCTS stores only scalar mean estimates and is poorly suited to **tail-risk objectives** such as **CVaR**. The paper introduces **CATSO** (Categorical Thompson Sampling with Optimism) and **PATSO** (Particle Thompson Sampling with Optimism), distributional MCTS algorithms that maintain **finite-support empirical backup laws at Q-edges** — categorical atoms with Dirichlet sampling, or adaptive particles — selecting actions by the **CVaR of a Thompson-sampled Q-edge law plus a polynomial optimism bonus**. For the finite-depth nested-CVaR planning target it proves an **O(n⁻¹/²) bound on root value error** after n rollouts (bounding risk-sensitive simple regret), with a fixed-grid discretization bias (CATSO) or a tunable Wasserstein compression bias (capped PATSO).
- **Why it matters here**: **risk-sensitive planning** is what game AI needs when catastrophic outcomes (lost games, unsafe states) matter more than expected return; distributional Q-edges are a clean way to make tree search CVaR-aware with a regret bound.
- **Caveats**: **fully fresh — 0 hits in wiki**; stochastic-planning benchmarks rather than game engines; nested-CVaR objective.

### ★★★ JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment
- **Authors**: Quentin Delfosse, Raban Emunds, Paul Seitz, Sebastian Wette, Jannis Blüml, Daniel Kirn, Dominik Mandok, Kristian Kersting
- **Affiliation**: Department of Computer Science, Technical University Darmstadt; Google Intrinsic AI Research; Hessian Center for Artificial Intelligence (hessian.AI); Centre for Cognitive Science, Darmstadt; German Research Center for Artificial Intelligence (DFKI).
- **Venue**: arXiv:2610.23650 (16 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.23650
- **Abstract and key innovations**: The **Arcade Learning Environment (ALE)** is the canonical general-agent benchmark, but lacks native **object extraction** and **environment modification** and depends on **CPU emulation**, bottlenecking GPU-accelerated pipelines. **JAXtari** is an open-source, high-performance reimplementation of Atari 2600 environments using **massive GPU parallelization**, allowing PPO agents to finish **100M environment steps on a single A100 in under an hour**. It provides **object-centric observations** and a flexible **modification system** so researchers can build neuro-symbolic methods or discover novel shortcuts and retrain in minutes.
- **Why it matters here**: a **step-change in game-RL benchmarking infrastructure** — the throughput removes the CPU bottleneck for Atari studies, and the object-centric + modification API directly enables the **causal-model-vs-visual-heuristic** question the ALE has historically made hard.
- **Caveats**: **fully fresh — 0 hits in wiki**; Atari 2600 only; throughput claims are hardware-specific (A100).

### ★★ OSCC: Certified Observation-Safe Coupling Optimization for Gradient-Noise Control in Imperfect-Information Learning
- **Authors**: Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Rui Chen, Daren Zha
- **Affiliation**: School of Artificial Intelligence, University of Chinese Academy of Sciences; Institute of Information Engineering, Chinese Academy of Sciences.
- **Venue**: arXiv:2609.33543 (27 Sep 2026, v2 16 Oct 2026) — `cs.GT`; `cs.LG`, `cs.AI`. 34 pages, 10 figures.
- **Link**: https://arxiv.org/abs/2609.33543
- **Abstract and key innovations**: Coupled rollouts can cut the noise of **counterfactual action comparisons**, but standard common-random-number constructions can **expose hidden state, synchronize policy randomness, or misalign chance events** after counterfactual histories diverge. **Observation-safe counterfactual coupling (OSCC)** defines an admissible class through **marginal preservation, information-state safety, branch-local policy randomness, semantic event alignment, and trace-before-oracle replay**, with a **gradient-aware coupling criterion** (policy-gradient noise change is governed by policy-Jacobian-weighted off-diagonal return covariance) and **OSCC-Select**, a calibration-only selector choosing among independent/root-only/continuation-only/fully coupled rollouts using separate safety and gain certificates (falling back to independent sampling when improvement is not certified). On 100,000 fixed-root **Leduc** comparisons, the fully coupled CP-GRPO instantiates a **55.87% return-contrast variance reduction** (41.12→18.14) while preserving declared marginals.
- **Why it matters here**: **imperfect-information training efficiency with certificates** — variance reduction in CFR/policy-gradient solvers is a recurring practical bottleneck, and this is the first treatment that makes coupling *safe* for hidden information rather than merely lower-variance.
- **Caveats**: **fully fresh — 0 hits in wiki**; Leduc-scale empirics; safety/gain certification depends on calibration budget.

### ★★ Detecting Multi-Agent Collusion Through Multi-Agent Interpretability
- **Authors**: Aaron Rose, Carissa Cullen, Sahar Abdelnabi, Philip Torr, Brandon Gary Kaplowitz, Christian Schroeder de Witt
- **Affiliation**: University of Oxford; New York University.
- **Venue**: arXiv:2604.01151 (1 Apr 2026, v5 15 Oct 2026) — `cs.LG`; `cs.MA`, `cs.AI`.
- **Link**: https://arxiv.org/abs/2604.01151
- **Abstract and key innovations**: Secret/non-verbalised **collusion** may cap transcript-level monitoring, and detecting collusion within an **unknown subgroup** is a joint inference task over multiple agents. The paper derives detection statistics from the **composite hypothesis testing** literature and introduces **HELIOS**, a multi-agent detector using per-agent activation probes as sensors, evaluated on **NARCBench** (collusion detection under environment distribution shift). Across four open-weight models, group-level statistics and heuristics transfer **zero-shot to NARCBench's holdout environments**; the best method per model reaches **0.99–1.00 AUROC** transferring from committee deliberations to a **steganographic collusion task** that unprimed transcript monitors cannot separate. No single statistic dominates (consistent with "no known universally most powerful test"), and transfer to **emergent** (vs instructed) collusion is only partial — in one environment **only 2 of 229 collusive episodes verbalise coordination**.
- **Why it matters here**: **hidden-coalition detection is the anti-collusion game** — the same structure as detecting teaming/implicit cooperation among NPCs or players, and the stress-test distinction between **instructed vs emergent** collusion is a benchmark-design lesson.
- **Caveats**: **fully fresh — 0 hits in wiki**; probes fitted on instructed collusion may under-detect emergent collusion; activation access required.

### ★★ Coordination Matters: Process-Aware Evaluation of Cooperative Multi-Agent Reinforcement Learning
- **Authors**: Maria Ana Cardei, Matthew Landers, Afsaneh Doryab
- **Affiliation**: University of Virginia.
- **Venue**: arXiv:2605.06557 (7 May 2026, v2 16 Oct 2026) — `cs.LG`; `cs.MA`, `cs.AI`. Comment: "Under review".
- **Link**: https://arxiv.org/abs/2605.06557
- **Abstract and key innovations**: Cooperative MARL benchmarks emphasize aggregate outcomes (return, success rate, completion time), which can **obscure how** agents coordinate. The paper proposes a **process-aware evaluation framework** adding diagnostics of **interference, coordinated task completion, participation, and coordination efficiency**, validated in **STAT** (a controlled spatial task-allocation testbed) and two established cooperative MARL benchmarks. Across value-based and actor-critic methods, policies with **nearly identical return exhibit substantially different coordination behavior**; controlled scaling reveals distinct process signatures, and a reward-shaping ablation shows **penalizing assignment conflicts can alter coordination with little change in task return**.
- **Why it matters here**: the eval-methodology complement to the wiki's reward-vs-behavior thread — "same score, different play" is precisely the trap in evaluating **game AI whose quality is coordination, not return**.
- **Caveats**: **fully fresh — 0 hits in wiki**; diagnostics are environment-specific and framed as a structure for choosing them; STAT is a testbed.

### ★★ Bayesian Learning of Parametric Mean Field Games with Common Noise
- **Authors**: Grégoire Lambrecht, Mathieu Laurière
- **Affiliation**: NYU Center for Data Science; NYU Shanghai (from the paper's rendered author footnote).
- **Venue**: arXiv:2610.23387 (16 Oct 2026) — `cs.GT`.
- **Link**: https://arxiv.org/abs/2610.23387
- **Abstract and key innovations**: Studies the **inverse problem** of recovering unknown parameters governing the dynamics and rewards of **Mean Field Games (MFGs)** from partial observations of population trajectories made stochastic by **common noise**. Because evaluating the likelihood requires solving a new **Nash equilibrium for each candidate θ**, the paper introduces the **Bayesian-Extended Mean Field Game (BE-MFG)**, whose **single NE simultaneously encodes equilibrium policies for all parameters**, enabling efficient learning of the conditional density of mean-field trajectories. It formalizes **parameter consistency and identifiability**, recovering ground-truth parameters accurately on three synthetic environments (beating an IRL-for-MFG adaptation), with a fourth experiment on **public electricity-market data**.
- **Why it matters here**: **inverse game learning** — recovering the game's parameters from observed population behavior is the theory analogue of inferring reward structure from player telemetry, and common noise is the realistic (shared-shock) regime.
- **Caveats**: **fully fresh — 0 hits in wiki**; synthetic + one real application; identifiability conditions required.

### ★★ A Complete Characterization of Learnability for Adversarial Noisy Bandits
- **Authors**: Steve Hanneke, Kun Wang
- **Affiliation**: Department of Computer Science, Purdue University.
- **Venue**: arXiv:2605.09200 (9 May 2026, v3 16 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2605.09200
- **Abstract and key innovations**: Studies **adversarial noisy bandits** given a known function class $\mathcal{F}$: each round the adversary picks $f\in\mathcal{F}$, the learner picks an arm, and observes a **noisy reward** from a fixed distribution. The main result is a **complete characterization of learnability** (existence of a sublinear-regret algorithm) via a **convexified generalized maximin volume** evaluated on the convex hull $\operatorname{co}(\mathcal{F})$: $\mathcal{F}$ is learnable **iff** this quantity is positive at every scale. The condition characterizes learnability against both **oblivious and adaptive** adversaries (showing the two notions coincide in the noisy setting), and connects to new combinatorial notions (**hitting set** and **distribution covering number**). Claimed as the **first complete characterization** for adversarial noisy bandits.
- **Why it matters here**: the bandit-theory lane's cleanest fresh dichotomy result — the equivalence of oblivious/adaptive learnability in the noisy regime is a strong structural fact adjacent to the wiki's bandit-evaluation threads.
- **Caveats**: **fully fresh — 0 hits in wiki**; known-function-class setting; theory only.

### Also fresh in this lane (not independently featured)
- [`2610.22683`](https://arxiv.org/abs/2610.22683) **Dynamic Auction Mechanisms in a Closed-Credit Economy: Sequential Slot Reallocation in Air Traffic Management** — a sequential resource-reallocation scheme using **reusable artificial credits** where agents hold pre-existing rights and have heterogeneous marginal valuations; capacity reductions create **fractional endowments** resolved into indivisible final allocations by an **ascending auction** using the minimum subgroup market-clearing price as a common transaction price, preserving non-myopic individual rationality and weak nontrader neutrality, with Pareto efficiency under optimal-demand clearing and a bound on misreporting gain (12 pages; Jihun Kim, Pan-Yang Su, Maria G. Mendoza, Victoria Marie Tuck, Chinmay Maheshwari, S. Shankar Sastry; `cs.GT`/`cs.MA`; affiliation not stated).
- [`2610.23157`](https://arxiv.org/abs/2610.23157) **Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models** — introduces **Cross-Psych-101** (591 participants, 261,551 valid decisions across 12 Bandit/Tradeoff/Structure/Social tasks) and trains **Cross-Centaur** to predict a participant's target-task actions from the target + source task descriptions paired with the same participant's source-task behavior, beating off-the-shelf LLMs and Centaur **on held-out participants both within and across tasks**; probing suggests hidden states encode **participant-level tendencies that transfer across tasks** (**EMNLP 2026 Main, Oral**; Hikaru Asano, Hidezo Suganuma, Ryutaro Mori, Yukino Baba; `cs.CL`; affiliation not stated).
- [`2209.14128`](https://arxiv.org/abs/2209.14128) **Generalizing Liquid Democracy to multi-agent delegation: A Voting Weight Measure and Equilibrium Analysis** — generalizes liquid democracy to allow **fractional delegation to multiple representatives** while retaining a fraction of one's own voting power, adds a **penalty for delegation-chain length**, and shows that a delegation game with this measure has **pure Nash equilibria contingent on the length penalty** (Francisco M. Bersetche; `cs.MA`; affiliation not stated).

---

## §2 Game AI Bot — LLM-Powered Game Agents, NPC Intelligence & Multi-Agent Systems

### ★★★ Agent Collectives Should Not Detect Their Own Imposters: A Chess Case Study
- **Authors**: Alexandre Le Mercier, Chris Develder, Thomas Demeester
- **Affiliation**: IDLab–T2K, Ghent University–imec.
- **Venue**: arXiv:2605.09027 (9 May 2026, v3 28 Sep 2026) — `cs.MA`. 60 pages, 16 figures. Benchmark released.
- **Link**: https://arxiv.org/abs/2605.09027
- **Abstract and key innovations**: Studies a **collective of AI agents** collaborating on a task and its robustness against **imposters** that deliberately mislead peers, on **Gambit** — a testbed where **4 reasoning agents deliberate on chess moves** (objectively scored by a strong engine). Comparing (i) **in-collective** imposter detection vs (ii) a **dedicated external detector**, it finds that merely **warning agents of potential imposters is harmful**: it degrades decisions when no imposter is present, provokes **self-accusation to scapegoating**, inflates token use, and **reveals to the imposter how it was uncovered**. It therefore recommends a detector that **reads but never joins** the deliberation and returns only a verdict, and that **recalibrates to new attacks after few examples** — a 3B model with a meta-trained classification head **adapts in a single gradient step on 20 labeled examples**, giving **8× the adaptation gain of standard finetuning at 14× lower cost**. Releases **37,352 labeled deliberations across 240 evolved imposter strategies**.
- **Why it matters here**: a **competitive game structure (hidden adversary inside a cooperative team)** with a counterintuitive, actionable finding — "don't tell the team" is the kind of design lesson game-AI multi-agent panels need, and the adaptation benchmark is directly reusable.
- **Caveats**: **fully fresh — 0 hits in wiki**; chess-only, 4-agent collective; the detector is engineered by the same authors as the benchmark.

### ★★★ Do Multi-Agent LLMs Explore Each Other?
- **Authors**: Hyeong Kyu Choi, Jiatong Li, Wendi Li, Xin Eric Wang, Sharon Li
- **Affiliation**: University of Wisconsin–Madison; University of California, Santa Barbara.
- **Venue**: **NeurIPS 2026 IAEval Workshop (Oral Presentation)** — also arXiv:2607.11250 (13 Jul 2026, v2 16 Oct 2026) — `cs.MA`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2607.11250
- **Abstract and key innovations**: **Exploration between LLM agents** is understudied, and the paper shows modern agents often **fail to explore peers**, exhibiting **myopic and polarized interaction patterns** that cause suboptimal coordination and increased regret. It formalizes the **Multi-Agent Exploration problem** as a **partially observable stochastic game (POSG)** in which agents must probe peers to infer capabilities and identify effective interaction strategies. **MACE (Multi-Agent Contextual Exploration)** explicitly promotes exploration through **structured peer selection**; across contextual and parametric diversity settings, both exploration behavior and downstream performance improve substantially, with a theoretical **sublinear expected-regret bound**.
- **Why it matters here**: it frames the **who-should-I-talk-to** decision of an LLM game/NPC team as a POSG with an exploration problem — a game-theoretic lens on agent communication that connects §2 to §1's equilibrium-learning lane.
- **Caveats**: **fully fresh — 0 hits in wiki**; workshop paper; regret bound is expected-regret (structural, not tight-constant).

### ★★ When Extremists Enter LLM Societies: Investigating Extreme Behavior in Multi-Agent Systems
- **Authors**: Guo Chen, Huaijin Xie, Ziwen Li, Reed Li, Yu Lu, Haibo Shi, Bingbing Xu, Junjie Huang
- **Affiliation**: College of Computer and Information Science, Southwest University; Yuanbao Team, Tencent; Communication University of China; State Key Laboratory of AI Safety, Institute of Computing Technology, CAS.
- **Venue**: arXiv:2610.19863 (14 Oct 2026, v2 16 Oct 2026) — `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.19863
- **Abstract and key innovations**: Social science shows **persistent tail actors** can disproportionately shape collective dynamics; the paper studies this in controlled **LLM-based multi-agent systems**, where such actors cannot be reduced to fixed scalar states. It models the LLM extremist from an LLM-native perspective and introduces **EXAM**, an **EXtremist Agent Modeling** framework that configures extremist agents for specific tasks and precisely controls their **population proportion, spatial distribution, interaction protocols, and measurement interfaces**. Across **congressional election, financial crisis, epidemic public opinion, and iterated prisoner's dilemma**, small persistent tail groups produce **measurable, backbone- and scenario-dependent collective shifts**.
- **Why it matters here**: the **iterated prisoner's dilemma** scenario and the population-fraction control make this a simulation-grade tool for studying how a few adversarial/griefing agents shift a game society — directly relevant to multiplayer community safety and NPC-society design.
- **Caveats**: **fully fresh — 0 hits in wiki**; social-simulation scenarios; findings backbone-dependent.

### ★★ Emergent Discrimination and Polarization in Multi-Agent Systems
- **Authors**: Nestor Caticha, João Henrique Sant'Ana, Felippe Alves, Davi Bastos Costa, Mariana Mercucci, Juan P. Neirotti, Otavio Citton, Renato Vicente
- **Affiliation**: Instituto de Física, Universidade de São Paulo; IEA-USP; TELUS Digital Research Hub CIAAM-USP; IMEC-USP; Data Science Institute, University of Chicago; Bernoulli Institute, University of Groningen.
- **Venue**: arXiv:2610.22701 (15 Oct 2026) — `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.22701
- **Abstract and key innovations**: Studies theoretically how **discrimination and polarization emerge** in a population of learning agents. Each agent uses an **adaptive linear decision layer** mapping a language-model embedding of an issue to a binary opinion and maintains an **evolving trust estimate** for every other agent; through pairwise interactions agents update weights and trust via an **online Bayesian rule from teacher-student learning over a noisy channel**, with in-context-learning experiments qualitatively reproducing the predicted updates. Assigning two group labels A/B and allowing a fraction $f_b$ of agents to shift perceived agreement by strength $b$, order parameters from statistical mechanics reveal a **rich phase diagram** with four states: **spin-glass frustrated out-group favoritism, nondiscriminatory polarization, discrimination with opinion alignment, and discrimination without opinion alignment**.
- **Why it matters here**: a **statistical-mechanics phase diagram for in-group bias in multi-agent societies** — measurable order parameters for emergent factionalism, complementing §2's prompted-identity result and the collusion thread.
- **Caveats**: **fully fresh — 0 hits in wiki**; theoretical + qualitative LLM checks (not a large-scale agent run); large author/affiliation list with per-author mapping unresolved.

### ★★ Thought Blocks: Non-Autoregressive Latent Communication for Multi-Agent Systems via Trajectory-to-State Compilation
- **Authors**: Zhenhan Guan, Xiaolong Liu, Hengwei Ye, Zheng Tian
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.23056 (16 Oct 2026) — `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.23056
- **Abstract and key innovations**: Text-based multi-agent communication incurs repeated generation/re-encoding costs, and latent communication still often needs **autoregressive latent trajectories**. The paper **separates message representation from message construction** and asks whether agents can **directly construct useful continuation states** without executing the producing trajectories — formulated as **trajectory-to-state compilation**. **Thought Blocks** are fixed-size blocks of latent **key–value (KV) continuation memory constructed in one shot**, achieving a **2.5× speedup over autoregressive latent communication**, and (vs text communication) **45.7% fewer text tokens, 84.8% fewer autoregressive steps, 8.6× lower latency**.
- **Why it matters here**: the **infrastructure efficiency result** for LLM agent teams — one-shot latent state exchange is exactly what real-time multi-agent game/NPC systems need to cut per-turn latency.
- **Caveats**: **fully fresh — 0 hits in wiki**; efficiency-focused (coordination quality not the headline); no affiliation printed.

### ★★ Gossip Agents: Reputation through Opinion Dynamics over Evolving Networks
- **Authors**: Yutong Wu, Arlei Silva
- **Affiliation**: Rice University.
- **Venue**: arXiv:2610.22674 (15 Oct 2026) — `cs.MA`. 10 pages, 8 figures.
- **Link**: https://arxiv.org/abs/2610.22674
- **Abstract and key innovations**: Sustained cooperation among self-interested agents needs **reputation**, but existing MARL reputation work assumes reputation is globally available or derived only from an agent's own observations, leaving **how reputational information propagates** largely unexplored. The paper studies **gossip** — exchange of information about third parties — over **dynamic communication networks**: agents form private opinions from limited observations and exchange them with neighbors via **DeGroot opinion dynamics** while the network changes as agents interact and move, with a **tunable broadcast radius** spanning private/local/global reputation. In two n-player social dilemmas — a **Prisoner's Dilemma** with resampled groups and **Harvest**, where communication neighborhoods emerge from movement — the **reach of reputational information shapes cooperation**, and in Harvest reputation diffusion raises environmental rewards and yields **more peaceful, sustainable behavior**.
- **Why it matters here**: the **reputation-propagation mechanism** is the social fabric of persistent multiplayer worlds (trading, guilds, karma), and the movement-coupled network is a realistic model for shared-world games.
- **Caveats**: **fully fresh — 0 hits in wiki**; two abstract social dilemmas; DeGroot dynamics is a simplification of real belief updating.

### ★★ Computational Multi-Agents Society Experiments: Social Modeling Framework Based on Generative Agents
- **Authors**: Hanzhong Zhang, Muhua Huang, Jindong Wang
- **Affiliation**: Data Science, William & Mary; Graduate School of Business, Stanford University.
- **Venue**: **Accepted for publication in ACM Transactions on Social Computing (TSC)** — also arXiv:2508.17366 (24 Aug 2025, v3 15 Oct 2026) — `cs.MA`; `cs.AI`. 36 pages, 6 figures.
- **Link**: https://arxiv.org/abs/2508.17366
- **Abstract and key innovations**: Computational social science lacks models combining **in-world human intervention with outcome forecasting**. **CMASE** is a generative agent-based framework for **in-world researcher participation and traceable interventions at runtime**, treating simulation as a **simulated ethnographic field**: it supports real-time human-computer interaction, controlled experiments with ethnography-inspired observation/interviewing/interpretation, and forward exploration of intervention trajectories. It combines **LLM-driven perception/memory/emotion**, a composable environment from texture and area maps, and researcher roles (observation, interviewing, participation, intervention), so **interventions enter as social events rather than exogenous parameters**. It replicates two published field studies (**urban greenery**, **social fragmentation**) and **cooperation in a public goods game** across two different language models.
- **Why it matters here**: the **public-goods-game** replication plus the "interventions as social events" design makes CMASE a method for studying how to *intervene* in agent societies — the experimenter's toolkit for game-society research.
- **Caveats**: **fully fresh — 0 hits in wiki**; small/medium-scale settings; replication targets selected field studies.

### ★★ Reward Engine: Reward-Centric Self-Evolution for Open-Ended Tool Agents
- **Authors**: Litong Feng, Ji Qi, Yiran Cheng, Shaowu Pan, Xinyu Zhang, Qijun Li
- **Affiliation**: Huawei openJiuwen Team.
- **Venue**: arXiv:2610.22915 (16 Oct 2026) — `cs.AI`. 29 pages.
- **Link**: https://arxiv.org/abs/2610.22915
- **Abstract and key innovations**: Open-ended tool agents can reach the same objective via different tool paths, and quality depends jointly on the interaction trace, environment state, and final artifacts, so such tasks **rarely admit an executable ground-truth reward**. The central challenge is to **construct a stationary reward from existing experience** that exposes the current policy's failures without drifting during optimization. **Reward Engine** builds a **RewardPack** of **testcases** for required correctness and **rubrics** for graded quality, each executed as a check returning a judgment with evidence; the **frozen** RewardPack then guides revision/selection and can serve as an RL reward. On WorkBuddy Bench Office and Claw-Eval it **largely agrees with benchmark graders** (not reversing their ordering on **82.3% / 80.5%** of candidate pairs) and raises three-run consistency **Pass³ 45.0→54.0%** and **78.4→83.7%**.
- **Why it matters here**: **reward construction for open-ended agent tasks** is the bottleneck for training game/NPC agents without a crisp win signal; the frozen RewardPack is a concrete recipe.
- **Caveats**: **fully fresh — 0 hits in wiki**; two office/tool benchmarks; agreement measured against existing graders.

### ★★ Recognizing Atari and Assessing Sente: Controlled Evaluation Tasks for Language-Based Go Agents
- **Authors**: Taiyi Chen, Iskar Deng, Amandalynne Paullada
- **Affiliation**: University of Washington.
- **Venue**: arXiv:2610.22953 (16 Oct 2026) — `cs.CL`. 7 pages, 2 figures, 5 tables.
- **Link**: https://arxiv.org/abs/2610.22953
- **Abstract and key innovations**: Domain terminology (e.g. **atari**) concisely describes game states, but whether game-playing language models can **recognize these concepts and relate them to move evaluation** is unclear. The paper builds a **controlled evaluation set** centered on *atari* and its relationship to *sente* in Go, testing **terminology recognition under local board changes** and **move evaluation under different strategic conditions**, on **LoGos** (a Go language model) after fine-tuning with terminology and commentary supervision. The model **struggles to recognize changes in the atari relationship and assess their strategic implications**, and its terminology predictions are **associated with move preferences even when those preferences contradict the reference evaluation**.
- **Why it matters here**: a **calibrated probe of whether language-game agents connect terminology to board truth** — it separates "knows the word" from "understands the position", the exact failure mode of commentary-trained game LLMs.
- **Caveats**: **fully fresh — 0 hits in wiki**; Go + one model; controlled set rather than full-strength play.

### ★★ Explaining Chess and Go in Natural Language
- **Authors**: Ori Press, Alexander Golubev
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.23166 (16 Oct 2026) — `cs.CL`; `cs.LG`, `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.23166
- **Abstract and key innovations**: Modern chess engines play beyond human ability, often choosing moves whose ideas are hard to explain. The paper proposes an **automatic metric for evaluating chess explanations grounded in engine evaluations**, finds state-of-the-art language models perform **surprisingly poorly** (relying on surface-level board observations rather than robust transferable concepts), then introduces **BinProp**, a **training-free** method that lets the same models **discover reusable chess concepts and explain moves in natural language**, nearly **tripling** the average score vs direct prompting and transferring to **Go, draughts, and shogi** without additional tuning.
- **Why it matters here**: **interpretability + concept discovery in board-game play** — BinProp is a cheap, general bolt-on for concept-based explanations, the direct counterpart to the atari/sente recognition study above.
- **Caveats**: **fully fresh — 0 hits in wiki**; explanation quality measured by an engine-grounded automatic metric; no affiliation printed.

### Also fresh in this lane (not independently featured)
- [`2610.22740`](https://arxiv.org/abs/2610.22740) **R²Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop** — a **recursive self-play orchestration** paradigm with an inner loop (self-play improves the orchestrator on self-chosen tasks) and an outer loop (improves how the inner loop improves), keyed by **Recursive Learnability** (reward a Proposer for tasks whose rollouts keep diverging as skills are withdrawn) and **Skill Withdrawal**; across twelve datasets it beats baselines on QA, math, code and interactive tasks (Mingda Zhang et al.; `cs.AI`; affiliation not stated).
- [`2604.24698`](https://arxiv.org/abs/2604.24698) **The Chameleon's Limit: Investigating Persona Collapse and Homogenization in Large Language Models** — formalizes **Persona Collapse** and quantifies its population-level structure with three diagnostic metrics (**Coverage, Uniformity, Complexity**); across eight LLMs on BFI-44 personality, moral reasoning and self-introduction it finds collapse is **universal but task-dependent**, sampling more personas cannot mitigate it, there is a **fidelity–diversity tradeoff**, and persona-targeted fine-tuning **narrows** populations further (Yunze Xiao, Vivienne J. Zhang, Chenghao Yang, Weihao Xuan, Jen-tse Huang; `cs.CL`; affiliation not stated).
---

## §3 Game Foundation Models & World Models

### ★★★ Execution Before Memory: Diagnosing Memory Failures in Video World Models
- **Authors**: Weiyang Jin, Jiwen Yu, Sihan Xu, Yuwei Niu, Xihui Liu
- **Affiliation**: University of Hong Kong; University of Michigan – Ann Arbor; Peking University.
- **Venue**: arXiv:2610.23542 (16 Oct 2026) — `cs.CL`; `cs.CV`. 27 pages, 7 figures. Project page + code linked.
- **Link**: https://arxiv.org/abs/2610.23542
- **Abstract and key innovations**: A **memory test for a video world model** should say whether the scene was set, whether the **asked change was carried out**, and whether the last frame shows the result — current tests fold these into one number, so a low score reads as "forgetting" even when the change was never executed (and thus no hidden state transition could appear). **MIST** **separates the change from the memory it should leave behind**: the model first sets the scene with the change hidden, and only later is asked to show it, with leakage controlled. This locates the bottleneck: **models set the scene but do not carry out the instructed change**, and the same gap appears in general memory evaluations. The proposed **M3-Agent (Make the Missing Move)** recursively revises the input instruction so the model carries it out, **more than tripling** the MIST reveal score; on benchmarks **WRBench score T rises 26.1%** and **MBench-T score U rises 52.7%**.
- **Why it matters here**: it **re-diagnoses a whole category of "memory" claims as execution failures** — the sharpest foundation-model methodology result this window, directly bearing on long-horizon game-generation consistency, and it proposes a stricter baseline rather than a bigger model.
- **Caveats**: **fully fresh — 0 hits in wiki**; evaluation-centric; M3-Agent is an instruction-revision wrapper, not a retrained model.

### ★★★ Momentum: Persistent Dynamics for Video World Models
- **Authors**: Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel, Yilun Du, Xi Wang, Luc Van Gool
- **Affiliation**: INSAIT Sofia; Harvard University; University of Ulm; TUM Munich (MCML).
- **Venue**: arXiv:2610.23423 (16 Oct 2026) — `cs.CV`.
- **Link**: https://arxiv.org/abs/2610.23423
- **Abstract and key innovations**: Video world models must capture how a scene evolves **beyond the current camera view**; observation history, static point clouds, and image caches are expensive and **cannot update dynamic content outside the field of view** (generated vehicles/pedestrians may be forgotten or reappear in physically inaccurate states). **Momentum** represents an evolving scene through **synchronized videos from reference-camera rigs** (eight cameras jointly covering the surroundings), connects rigs in a **graph**, and propagates generation between neighbors. Its two-stage pipeline — **WorldUpdate** (jointly generate reference-camera videos as a **shared memory of scene dynamics**) and **WorldInteract** (ground camera-controlled generation in this memory) — keeps moving content represented outside the target view. A **CARLA pipeline** provides synchronized-rig training/evaluation data; on generated street scenes **Momentum improves dynamic-scene consistency by 126.2% in unseen scenes** over static image conditioning, with better visual fidelity.
- **Why it matters here**: the **persistent-dynamics** problem behind open-world game rendering — "what happened off-camera" — with a concrete multi-rig memory design and a large reported consistency gain.
- **Caveats**: **fully fresh — 0 hits in wiki**; CARLA street scenes; 8-camera rigs are a heavier capture setup than gameplay video.

### ★★★ Persistent Planar Memory for Video World Models
- **Authors**: Yuze He, Bin Tan, Zelin Gao, Yujun Shen, Yong-Jin Liu, Nan Xue, Yinghao Xu
- **Affiliation**: Tsinghua University; Ant Group; HKUST.
- **Venue**: **Accepted by NeurIPS 2026** — also arXiv:2610.23795 (16 Oct 2026) — `cs.CV`. 20 pages, 9 figures.
- **Link**: https://arxiv.org/abs/2610.23795
- **Abstract and key innovations**: World models that generate and explore environments need a **persistent 3D memory**; **plane primitives** offer a compact candidate — a set of **oriented planes** captures the dominant structure (walls, floors, facades) with only **7 parameters per primitive**. **PPMem** adopts plane primitives as persistent memory: a video diffusion transformer is augmented with a **planar prediction head** and a **Depth Token Fusion (DTF)** module, each **autoregressive chunk jointly producing RGB video and planar geometry** that merges into a persistent plane memory conditioning subsequent chunks via rendered depth. The memory is **three orders of magnitude more compact** than per-pixel point clouds (~100K primitives, **5 MB** for a full scene), **geometrically explicit** (metric depth, normals, exportable surfaces), **cross-view consistent**, and **adaptive** (refined as generation proceeds). On DL3DV and RealEstate10K it beats prior 3D-grounded world models in video quality while jointly producing metric depth, normals, and exportable planar geometry, staying coherent across **hundreds of frames** under large viewpoint changes.
- **Why it matters here**: a **compact, explicit 3D memory** for generated worlds — planes are a strong game/runtime primitive (level geometry *is* mostly planes), so this is the most "engine-native" of the three memory papers.
- **Caveats**: **fully fresh — 0 hits in wiki**; indoor/outdoor real-estate-style scenes; plane primitives suit man-made structure more than organic terrain.

### ★★ OrbiSim: World Models as Differentiable Physics Engines for Embodied Intelligence
- **Authors**: Jiajian Li, Jingyuan Huang, Junru Gong, Qi Wang, Xiaokang Yang, Yunbo Wang
- **Affiliation**: MoE Key Lab of Artificial Intelligence, AI Institute, School of Computer Science, Shanghai Jiao Tong University.
- **Venue**: arXiv:2605.16395 (12 May 2026, v2 16 Oct 2026) — `cs.LG`; `cs.RO`. Project page linked.
- **Link**: https://arxiv.org/abs/2605.16395
- **Abstract and key innovations**: Prior world models do **unconstrained imagination** in latent/visual space; **OrbiSim** redefines a world model as a **fully differentiable physics engine** bridging structured scene assets, neural dynamics, and downstream RL. By enabling **end-to-end differentiability throughout the simulation loop** (explicit state transitions → visual observation generation), it supports tasks classically intractable for simulators: **differentiable contact modeling, gradient-based policy optimization under sparse rewards, and intuitive physical inference**. It outperforms state-of-the-art world models in **predictive fidelity and control performance** and responds consistently to asset configurations and physical parameters.
- **Why it matters here**: a **differentiable game/physics engine as a trainable world model** — the bridge from §3 to game RL (gradient-through-sim is a long-standing game-AI ambition).
- **Caveats**: **fully fresh — 0 hits in wiki**; embodied-robotics framing; "physics engine" claims scoped to asset/contact settings.

### Also fresh in this lane (not independently featured)
- [`2510.08713`](https://arxiv.org/abs/2510.08713) **Towards Unified World Models for Visual Navigation via Memory-Augmented Planning and Foresight (UniWM)** — a **unified, memory-augmented world model** integrating egocentric **visual foresight and planning** in one multimodal autoregressive backbone, grounding action selection in imagined outcomes, with a **hierarchical memory** fusing short-term perceptual cues and longer-term trajectory context; it improves navigation success by up to **30%** on four benchmarks (Go Stanford, ReCon, SCAND, HuRoN) plus the 1X Humanoid Dataset and generalizes zero-shot to TartanDrive (Yifei Dong et al.; `cs.CV`; affiliation not stated).

---

## §4 Procedural Content Generation

> **Lane note.** Classic PCG (`procedural content generation` / `level generation`) returns **no fresh in-window item** — the **fourth consecutive edition** with an empty PCG lane (10-16, 10-17, 10-18 had none either). Targeted queries (`pcg`, `levelgen`, `nethack`, `crafting`, `grids`, `openended`) produced fresh hits that were **all audited off-lane** (§0.2). Anchors for continuity remain **Multiverse** `2603.26782` (19 hits), **HDPCG** `2602.18943` (17), **Playtrace Reconstructive Partitioning** `2607.12097` (7), **PCG Benchmark** `2503.21474` (6). The closest fresh **content-generation-adjacent** item is the terrain-curriculum paper below (it *generates content to train against*, rather than *for play*), and §6's proceedings news carries the CoG content-generation recognition from the 10-18 edition.

### Also fresh in this lane (content-generation-adjacent, not classic PCG)
- [`2610.22619`](https://arxiv.org/abs/2610.22619) **FCTS: Failure-Guided Curriculum Tree Search Over Generated Terrain for Legged Parkour** — a **failure-conditioned terrain curriculum** that uses localized traversal failures (location, termination mode, robot state, surrounding geometry) to **automatically generate the terrains a policy should train on next**, with **Monte Carlo Tree Search** exploring curriculum trajectories under a fixed budget; on terrains from **scanned real-world construction sites** it raises success from **28.4%→85.8%** (medium) and **14.9%→44.7%** (hard) over the strongest parkour/LLM-curriculum baselines, with hardware transfer on a quadruped (Narayanan Palghat Parameswaran et al.; `cs.RO`; affiliation not stated).

---

## §5 Game Benchmarks & Evaluation Suites

### ★★★ GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations
- **Authors**: Nicholas Saban, Charvi Bannur, Mariya Vasileva, Darshan Deshpande
- **Affiliation**: not stated (LaTeXML page returned 404 this run); *not inferred*.
- **Venue**: arXiv:2610.22708 (15 Oct 2026) — `cs.CL`; `cs.AI`. Code + data linked.
- **Link**: https://arxiv.org/abs/2610.22708
- **Abstract and key innovations**: Text-based world models can simulate complex RL environment state transitions, but **no standardized benchmark exists** to compare them. **GlobeBench** contributes **1,632 tasks across five domains and nineteen simulation skills**, checking whether a model can **predict the environment's response to an action given the full agent trajectory** — understanding earlier state changes, following environment rules, and predicting effects on **related and unrelated objects**. Predictions are compared with an **execution-derived reference** via a hybrid of **deterministic gates and a semantic judge**. Among **20 general-purpose LLMs and specialized text world models**, **GPT-6 Astra** tops task success at **49.57%**; accuracy falls as actions affect larger portions of the environment, and when changes must **propagate to dependent objects** task success drops to an average of **5.1%** — and **631 tasks remain unsolved by any model**.
- **Why it matters here**: the **environment-simulation benchmark** the text-world-model lane lacked, with a headline "631-unsolved" gap that quantifies how far LLMs are from being reliable game-world simulators.
- **Caveats**: **fully fresh — 0 hits in wiki**; text-based environments; hybrid judge introduces its own evaluation surface.

### ★★ HARL-A: An Extensible Benchmark Framework for Heterogeneous Multi-Agent Adversarial Reinforcement Learning in IsaacLab
- **Authors**: Isaac Peterson, Christopher Allred, Jacob Morrey, Mario Harper
- **Affiliation**: Utah State University; US DEVCOM Army Research Laboratory.
- **Venue**: arXiv:2510.01264 (26 Sep 2025, v2 5 Oct 2026) — `cs.RO`. 8 pages, 9 figures. Code linked.
- **Link**: https://arxiv.org/abs/2510.01264
- **Abstract and key innovations**: Adversarial MARL for robotics lacks **shared, extensible infrastructure** supporting **heterogeneous agent morphologies** in high-fidelity simulation; existing frameworks are cooperative, simplified-physics, or non-extensible. **HARL-A** is an open-source, actively-maintained framework on **IsaacLab** enabling scalable training/benchmarking of adversarial policies across morphologically diverse robot teams (**any number of teams, any mix of morphologies per team**). It contributes: (1) a **modular architecture** lowering the overhead of defining new heterogeneous adversarial environments; (2) **three benchmark environments** — **Sumo** (contact-rich pushing), **Soccer** (ball-skill competition), **3D Galaga** (pursuit/evasion); (3) **ten-plus pretrained policies** spanning homogeneous and heterogeneous teams, released on **Hugging Face**. It reliably produces learned adversarial policies and **emergent role specialization**.
- **Why it matters here**: the **benchmark substrate for heterogeneous competitive robot teams** — making adversarial MARL reproducible is the biggest blocker to comparing self-play methods, and the pretrained-policy release lowers entry cost.
- **Caveats**: **fully fresh — 0 hits in wiki**; robot-morphology domain; IsaacLab/GPU dependency.

---

## §6 Industry Game AI & Deployment, Competitions and Proceedings

### ★★★ From Hitter to Player: Separating Motor Execution and Strategy in Competitive Humanoid Table Tennis
- **Authors**: Fanrong Dong, Ziyi Sun, Ziqi Han, Junhan Sun, Lei Ye, Zetong Jing, Hao Zhao, Shaoxun Liu, Rongrong Wang
- **Affiliation**: Zhejiang University; Ocean University of China; Tongji University; Shanghai Innovation Institute; Tsinghua University; RoboParty Lab.
- **Venue**: arXiv:2610.14067 (7 Oct 2026) — `cs.RO`. 8 pages, 7 figures. Project page linked.
- **Link**: https://arxiv.org/abs/2610.14067
- **Abstract and key innovations**: Competitive humanoid table tennis requires **executing a desired return** and **deciding where to return** — two distinct abilities. The paper separates them with the **ball landing target as the motor-control/strategy interface**: (1) train a **whole-body motor policy conditioned on the desired landing target** (model-based strike planner + learned controller); (2) improve it via **self-play in closed-loop rallies** against incoming balls generated by another player (targets still sampled without an opponent, so execution improves but no strategy is learned); (3) **freeze the entire motor stack** and train a **stroke-level strategic policy** to choose landing targets via competitive self-play. With the motor stack fixed, changing only target selection **wins 89% / 82% / 73%** of points against **center / random / away-from-opponent** baselines, and the strategy **adapts to opponent position and previous target**. On hardware the same frozen stack supports complete **11-point games** against a recreational human, with forehand and backhand rallies.
- **Why it matters here**: a **clean separation of execution vs strategy** in a real competitive sport robot — the interface design is the key idea, and the "frozen motor stack, learned strategy" ablation is a template for **layering decision-making over a fixed skill policy** in game AI.
- **Caveats**: **fully fresh — 0 hits in wiki**; table-tennis-specific; strategy evaluated against scripted baselines and one recreational human.

### ★★ LoongSage: A Production-Grade, High-Efficiency Agentic RL Framework for Frontier LLMs with Validated Recipes
- **Authors**: LoongSage Team, Bowei Song, Caiwei Zhao, Chuwen Liu, Dechuang Gu, Dong Fang, Feiyu Xie, et al.
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block (only "Team" printed); *not inferred*.
- **Venue**: arXiv:2610.16352 (12 Oct 2026, v2 16 Oct 2026) — `cs.CL`; `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.16352
- **Abstract and key innovations**: As LLM training shifts from static reasoning to **agentic tasks** (tool invocation, multi-turn interaction, long-horizon decisions), mainstream RL frameworks have grown unwieldy. **LoongSage** is an **agent-native, fully asynchronous** RL framework with a lightweight core of **~14K lines**, built on **Megatron** (distributed training) and **SGLang** (high-throughput inference), centralizing orchestration in **one controller process** with GPU-resident components as **Ray actors**. It introduces **AgentFlow** (unified execution for white-box and black-box agents), **sliding-window strategies** bounding trajectory staleness, **TransferMesh** (topology-aware weight synchronization over the fastest transport per receiver), and a memory-efficient **Teacher Manager** natively supporting **Multi-Teacher On-Policy Distillation**. Four complete training runs show steadily improving task rewards with the train-inference gap under continuous control, and the fully asynchronous pipeline removes synchronous idle bubbles.
- **Why it matters here**: the **deployment-infrastructure** entry for agentic RL — an efficiency-first framework for training long-horizon **game/NPC agents**, notable for its small code core and async design (the practical counterpart to §7's credit-assignment methods).
- **Caveats**: **fully fresh — 0 hits in wiki**; systems paper (no novel algorithm); affiliation not printed.

### Proceedings & competition news (web pass — not arXiv)
- **IEEE Conference on Games (CoG) 2026** — Madrid, Spain, **1–4 September 2026**; the 10-18 edition reported the award results (**Best Paper**: *Categorizing Experience Management Problem Difficulty Using Graph Analysis*; **Best Demo**: *Descent: Journeys in the Dark* computer-aided content generation) and the relevant accepted highlights. **No new CoG material surfaced this run** beyond the fixed results already on file.
- **AIIDE 2026** — 22nd AIIDE, **Belo Horizonte, Brazil, 9–13 November 2026** (AAAI Press), special theme "New Grounds"; topic areas include **RL for Games, NPC AI, PCG, and game agents**. **Papers not yet public** as of this run — flagged for a later harvest.
- **Industry/studio lane**: targeted searches for studio terms are **in-window empty** again — no studio paper this week; industrial involvement remains embedded in the featured set (Huawei openJiuwen §2, Tencent Yuanbao §2, Tencent FiT / Ant Group / Huawei §7, Google Intrinsic AI Research §1, DFKI/hessian.AI/TU Darmstadt §1).
---

## §7 Related Techniques — Self-Play, Model-Based RL, Reward Shaping, Imitation & World Models

### ★★★ Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents
- **Authors**: Qirui Liu, Hao Chen, Yi Wen, Weijie Shi, Yao Zhao, Xianhe Chen, Hao Zhao, Xing Tang, Weihong Luo, Yuyu Luo
- **Affiliation**: South China University of Technology; Tencent FiT; City University of Hong Kong; HKUST; Nanjing University; Imperial College London; Shenzhen Technology University.
- **Venue**: arXiv:2610.23148 (16 Oct 2026) — `cs.LG`. 27 pages.
- **Link**: https://arxiv.org/abs/2610.23148
- **Abstract and key innovations**: Outcome-reward RL such as **GRPO** gives every token of a rollout the same advantage even though the rollout exercises two capabilities — **finding evidence** and **using it**. The paper shows **accuracy improves without grounding**: Search-R1 raises accuracy on seven QA benchmarks, yet on **Bamboogle** the evidence-supported share of correct answers **falls from 84.0% to 42.9%**. It attributes this to GRPO's credit assignment, where evidence-bearing rollouts are favoured only in proportion to their accuracy gain. **Grounded Credit Assignment (GCA)** uses **verifiable sub-outcomes** (evidence retrieval + answer correctness) to correct search and answer credit separately — **blaming a wrong answer more than the search that found the evidence**, and crediting less a correct answer that bypasses retrievable evidence. Never negative on evidence-finding search, capped at **10% of each token's advantage**, it improves average EM over Search-R1 by **+5.7 (Qwen2.5-3B)** and **+6.3 (Qwen3-30B-A3B)** and raises the grounded share **76.9%→93.4%** without extra models, rollouts, or stages.
- **Why it matters here**: **decoupled credit for process vs outcome** — the same "right answer for the wrong reason" problem plagues game agents that win via lucky/shortcut play, and GCA is a drop-in, verifier-driven fix.
- **Caveats**: **fully fresh — 0 hits in wiki**; search-QA domain; correction magnitude is a capped hyperparameter.

### ★★★ Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning (TreeOPSD)
- **Authors**: Heming Zou, Qi Wang, Yixiu Mao, Yun Qu, Yuyi Guo, Zeyuan Liu, Chenglin Li, Weijie Liu, Saiyong Yang, Xiangyang Ji
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block (numeric markers with no unit list); *not inferred*.
- **Venue**: arXiv:2610.23181 (16 Oct 2026) — `cs.CL`; `cs.LG`, `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.23181
- **Abstract and key innovations**: RL with verifiable rewards over **long-horizon** interactions suffers (i) **sparse, high-variance turn-level credit** from terminal-only rewards and (ii) **policy staleness** from sequential mini-batch updates on a fixed rollout batch; existing fixes need a value network, step-level annotations, or a stronger external teacher. **TreeOPSD** is a **critic-free, tree-aware posterior self-distillation** framework: it treats each interaction turn as a **tree node**, branches alternative continuations from shared prefixes, and **recursively backs up terminal rewards into implicit turn-level credit**, then maps each credit to a **closed-form bounded teacher distribution** parameterized by the likelihood ratio to the frozen behavior policy. Minimizing the divergence to this teacher recovers the policy-gradient direction at the behavior policy while **bounding updates toward a finite target** across mini-batches. It improves agentic capability across benchmarks/scales, e.g. **+4.97 points** over GRPO for Qwen3-30B-A3B-Thinking-2507 in the Deep Research setting.
- **Why it matters here**: **tree-structured credit without a critic or teacher model** — turn-level credit is the central obstacle for long-horizon game/agent RL, and the bounded target addresses staleness explicitly.
- **Caveats**: **fully fresh — 0 hits in wiki**; needs a frozen behavior policy and branchable environment; affiliation not printed.

### ★★ RecReg: Recovery-based Shielding for Regular Safety Properties in Reinforcement Learning
- **Authors**: Alexander W. Goodall, Francesco Belardinelli
- **Affiliation**: Department of Computer Science, Imperial College London.
- **Venue**: arXiv:2610.23445 (16 Oct 2026) — `cs.LG`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.23445
- **Abstract and key innovations**: Deploying RL agents often requires formal **safety and constraint compliance**. **RecReg** is a **safe RL framework** enforcing **non-Markovian regular safety properties via recovery-based shielding**, a unified approach supporting different levels of a priori knowledge and safety guarantees. The paper focuses on **theoretical foundations in the tabular setting**, giving rigorous **safety and convergence guarantees** not present in related work, with extensive empirical results using the **MASA-Safe-RL** library, plus an outlined extension to **deep RL** using SOTA model-based RL. Empirics show efficient learning that **matches the theory**.
- **Why it matters here**: **non-Markovian safety** (e.g. "never repeat an unsafe sequence") with recovery is the realistic constraint in game AI deploy, and the tabular guarantees give a principled baseline for shield design.
- **Caveats**: **fully fresh — 0 hits in wiki**; core is tabular; deep-RL extension is outlined, not fully evaluated.

### ★★ Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning
- **Authors**: Anshul Nayak, Shahil Shaik, Jonathan Smereka, Yue Wang
- **Affiliation**: Clemson University; US Army DEVCOM GVSC.
- **Venue**: arXiv:2610.23550 (16 Oct 2026) — `cs.RO`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.23550
- **Abstract and key innovations**: RL policies optimized for task rewards can be **efficient but misaligned** with human expectations, safety preferences, or intent. This paper presents a **reason-guided preference-based RL (PbRL)** framework that learns a human reward model from **trajectory-level feedback**: in addition to preference labels, it incorporates **reason tags** explaining *why* a behavior is preferred, enabling the learned reward to capture both choices and their rationale. Compared with preference-only reward learning, the reason-guided formulation provides **extra supervision for human-aligned rewards** and improves policy interpretability; the learned human reward is combined with the environment reward during optimization, improving task performance while producing more interpretable, human-aligned, preference-sensitive behavior.
- **Why it matters here**: **rationale tags as extra reward supervision** — a lightweight way to inject human intent into game-NPC reward models beyond pairwise preferences.
- **Caveats**: **fully fresh — 0 hits in wiki**; abstract does not report quantitative results; reason tags assume annotator effort.

### ★★ Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors (AnchorQ)
- **Authors**: Carl Qi, Weijun Dong, Xiaojie Wang, Peiyi Chen, Rahul Sajnani, Mingyuan Zhang, Amy Zhang, Jose Barreiros, Manikatan Nambi, Lillian J. Ratliff, Dylan Randle
- **Affiliation**: Amazon; UT Austin; UC San Diego; Brown University; University of Washington (from the paper's rendered author footnote).
- **Venue**: arXiv:2610.22852 (16 Oct 2026) — `cs.RO`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.22852
- **Abstract and key innovations**: Generalist robot policies offer strong behavioral priors, but RL improvement is limited by **online-interaction cost**; existing methods adapt frozen **flow-matching** policies by treating **noise space as a continuous action space**, which is **behaviorally unstructured** and makes exploration inefficient. **AnchorQ** enables **coarse-to-fine policy improvement** through a structured, refinable **latent action representation**: at each step it uses **flow reversal** to map reference behaviors to **state-conditioned latent anchors**, samples **local particles** around them, and applies **value-guided sampling**. The analysis shows anchors **reduce identification complexity at the cost of support bias**, particle refinement trades bias against action-class complexity, and critic accuracy governs reliability of KL-regularized value-guided selection. Across simulated and real-world manipulation, **AnchorQ** delivers **+37% real-world success** and **97% higher simulated throughput** under the same interaction budget.
- **Why it matters here**: **structured latent action spaces for sample-efficient improvement** — the "anchor + local particle" mechanism is portable to game policy refinement over physics-based controllers where online interaction is expensive.
- **Caveats**: **fully fresh — 0 hits in wiki**; manipulation tasks (not games); support-bias/complexity tradeoff is analysis-driven.

### ★★ Reinforcement Learning in MDPs with Information-Ordered Policies
- **Authors**: Zhongjun Zhang, Shipra Agrawal, Ilan Lobel, Sean R. Sinclair, Christina Lee Yu
- **Affiliation**: Northwestern University (IE/MS); Columbia University (IEOR); NYU Stern (Technology and Operations); Cornell University (ORIE) (from the paper's rendered body footnote).
- **Venue**: arXiv:2508.03904 (5 Aug 2025, v2 16 Oct 2026) — `cs.LG`. 94 pages, 3 figures.
- **Link**: https://arxiv.org/abs/2508.03904
- **Abstract and key innovations**: Many operational MDPs provide **structured information** where a trajectory under one policy also reveals how **other policies would have performed**. The paper formalizes this as an **information order** over a parameterized policy class ($\pi_{\theta'}\preceq\pi_\theta$ when data under $\pi_\theta$ can estimate the long-run average cost of $\pi_{\theta'}$) and develops an **epoch-based RL algorithm** for infinite-horizon average-cost MDPs with continuous state/action spaces that exploits the order via **counterfactual inference**. For a $d$-dimensional policy class whose information order has **width $w$**, it achieves **$\widetilde O(H\sqrt{wdT/\alpha})$ regret**, so $w$ captures effective exploration complexity, interpolating between full counterfactual feedback and unstructured learning. Instantiations: **lost-sales inventory with lead times, dual-sourcing dual-index policies, and state-dependent-service queues** — new regret guarantees without global convexity.
- **Why it matters here**: **counterfactual feedback as an exploitable structure** — the theory of "one policy's data reveals others' performance" is exactly why offline logged game data can be so powerful, and the width parameter is a clean complexity measure.
- **Caveats**: **fully fresh — 0 hits in wiki**; average-cost continuous MDP theory; operations-research instantiations rather than games.

### Also fresh in this lane (not independently featured)
- [`2610.23048`](https://arxiv.org/abs/2610.23048) **Distill Until Divergence: Error-Truncated Hindsight Distillation for Agentic RL** — routes two complementary hindsight skills by trajectory outcome and error boundary: **Positive skills** reinforce successful workflows and pre-error decisions, **Negative skills** target decisive errors, with the **post-error suffix optimized only by GRPO** to avoid mismatched hindsight supervision (Yibin Huang, Conghui Zhu; `cs.AI`; affiliation not stated).
- [`2610.22665`](https://arxiv.org/abs/2610.22665) **Diverse Reasoning Paths Matter: Symbolic Equivalence Augmentation for Enhancing RL Exploration (EquivAug)** — converts CoT solutions into formal symbolic representations, applies **equivalence transformations**, and reconstructs natural-language explanations to produce **provably correct, reasoning-level-diverse** SFT data; across GSM8K and FOLIO it yields the highest path diversity after SFT and strongest accuracy after GRPO (**AACL 2026**; Xiaoou Liu, Tiejin Chen, Hanyang Chen, Yuan Ling, Hua Wei; `cs.AI`; affiliation not stated).
- [`2610.23470`](https://arxiv.org/abs/2610.23470) **QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity** — formalizes open-ended recommendation as building a **diverse, high-quality set** of (item, natural-language hypothesis) pairs; **QD-Rec** selects items with a **contextual bandit** and generates hypotheses with a foundation model from earlier archive entries, admitting a recommendation if it is **novel or better than its nearest neighbor** (Takashi Ishida, Taro Makino, Issa Sugiura; `cs.LG`/`cs.NE`/`cs.AI`; affiliation not stated).
- [`2610.22973`](https://arxiv.org/abs/2610.22973) **DiffusionRVGE: Reinforcement Learning via Regression-Based Value Gradient Estimation** — constructs update directions by **regressing centered rewards on centered final denoised images** (no reward derivatives or adjoint backprop through the sampling trajectory); one SD3.5-Medium model matches/exceeds DiffusionNFT on 7/8 metrics at ~1/5 compute, reaching **GenEval 0.94, OCR 0.92, PickScore 23.82** (Jiayuan Wang, Tongyao Pang; `cs.AI`; affiliation not stated).
- [`2610.22781`](https://arxiv.org/abs/2610.22781) **Anytime Contracts for AI Services** — AI services suffer **moral hazard** (silently routing to cheaper models) and users can terminate subscriptions at any time; the paper extends **contract theory to unknown exit rules**, formalizes it as a **Principal-Agent game**, and shows budget-optimal contracts are proportional to **anytime-valid likelihood-ratio e-value tests**, with betting e-processes approximating them when models are unknown (19 pages; Boris Velasevic, Eden Saig, Eric Mazumdar; `cs.GT`/`cs.LG`; affiliation not stated).
- [`2610.23402`](https://arxiv.org/abs/2610.23402) **Contracting with an Agent under Model Mismatch** — studies a **principal-agent MDP** (PAMDP) where the agent acts under **misspecified beliefs** about environment dynamics while the principal knows the true model; characterizes contract design under model mismatch and induces desirable long-term benefits despite the agent's inaccurate understanding (Elif Yılmaz, Jakub Tłuczek, Victor Villin, Christos Dimitrakakis; `cs.GT`/`cs.LG`; affiliation not stated).
- [`2610.22448`](https://arxiv.org/abs/2610.22448) **Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards** — grounds **multi-level process rewards** (tool-call, workflow-stage, outcome) in a unified **Lean4 formalization schema**, with a problem-specific workflow system and workflow-stage-normalized GRPO; **LAR-27B** reaches **77.3% on TerminalBench-2.1**, and the family beats the base model by **+9.89%** on average (Ruida Wang, Gerald Friedland, Tong Zhang, Chris Kong; `cs.LG`; affiliation not stated).

### Backward-window residue (submissions 28 Sep – 8 Oct; all grep-verified 0-hit)
- [`2610.08129`](https://arxiv.org/abs/2610.08129) **Do LLMs Act on What They Know? From Partner Representations to Cooperative Actions** — in a controlled **Hanabi-derived** environment with scripted hints and frozen weights, **linear probes recover *intent* conventions far better than *target* conventions**, yet receiving choices do not consistently follow the sender's convention; **rule statements** yield modest model-dependent changes while **action translation** produces larger gains, and activation transfers from oracle-action donors improve intent accuracy but do not reliably reproduce benefits (6 Oct 2026; Yuhwan Jeong, Jinnyeong Yang, Kuk-Jin Yoon; `cs.LG`; affiliation not fetched).
- [`2604.06189`](https://arxiv.org/abs/2604.06189) **High-Precision Estimation of the State-Space Complexity of Shogi via the Monte Carlo Method** — closes a **five-orders-of-magnitude gap** ($10^{64}$–$10^{69}$) in Shogi state-space estimates by combining **Monte Carlo sampling** with a **reachability test** that reverse-searches toward **"King–King only" positions** (mutually reachable with the initial position) rather than the single initial position; over **five billion sampled positions** it estimates **$6.55\times10^{68}$** reachable positions (v1 24 Feb / v2 3 Oct 2026; Sotaro Ishii, Tetsuro Tanaka; `cs.AI`; IPSJ JIP preprint; affiliation not stated).
- [`2002.12119`](https://arxiv.org/abs/2002.12119) **Path Polymatrix Games are PPAD-hard** — proves computing a Nash equilibrium is **PPAD-hard** for **tree polymatrix games with ≤20 actions/player** and **path polymatrix games with ≤400 actions/player** — the first PPAD hardness for a **constant-actions-per-player, acyclic-interaction-graph** game; also shows PPAD-hardness for an ε-fixed point of a 2D LinearFIXP instance for any constant ε<0.5 (tight, since 0.5 is trivial) (v2 2 Oct 2026; Argyrios Deligkas, John Fearnley, Rahul Savani; `cs.GT`).
- [`2210.03852`](https://arxiv.org/abs/2210.03852) **Stackelberg POMDP: Learning to Lead via Reinforcement Learning** — embeds follower adaptation into the leader's environment to form a single-agent **Stackelberg POMDP**; proves that for policy-interactive response algorithms an optimal policy based only on the leader's game history yields an optimal commitment, then uses PPO with a centralized critic and meta-learned contextual followers. Applications: indirect mechanism design (buyer-message mechanisms beat standard sequential price mechanisms), platform design (**+8.4% mean consumer surplus** over an optimized fixed price cap), and **Atari bilateral trade** (leadership assignment shifts prices/payoffs) (v5 **8 Oct 2026**; Gerstgrasser, Brero, Eden, Chakrabarti, Lepore, Li, Mibuari, Greenwald, Parkes; `cs.LG`/`cs.GT`/`cs.MA`).
- [`2601.12310`](https://arxiv.org/abs/2601.12310) **Survival is the Only Reward: Sustainable Self-Training Through Environment-Mediated Selection** — a proof-of-concept architecture in which learning is mediated **exclusively by environmental viability** (no reward/objective/fitness): candidate behaviours execute under **real resource constraints** and only those whose effects **persist and preserve future interaction** propagate, making proxy optimisation and reward hacking impossible; reports **"negative-space learning"** and emergent meta-strategies such as deliberate experimental failure (v2 30 Sep 2026; Dodgson, Alhajir, Joedhitya, Pattirane, Kumar, Lim, Peh, Ramdas, Zhexu; `cs.AI`; affiliation not stated).
- [`2605.09278`](https://arxiv.org/abs/2605.09278) **EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium** — formulates memory updating in multi-agent debate as a **zero-trust memory game** whose equilibrium motivates a principled objective for calibrating memory influence; **EquiMem** evaluates each update against shared memory state and other agents' used memory via their retrieval queries/traversal paths, for embedding- and graph-based memory, robust under adversarial agents at negligible overhead (v2 29 Sep 2026; Meng, Tang, Narvekar, Vaje, Zhang, Ye, Xi; `cs.MA`; affiliation not stated).
- [`2606.01382`](https://arxiv.org/abs/2606.01382) **Efficient Exploration for Iterative Nash Preference Optimization** — shows standard iterative **NLHF** can incur **exponential dependence on the inverse KL parameter** (implicit exploration is insufficient), then proposes **ENPO** (SFT-type regularization + adversarial policy exploration) eliminating it without minimax oracles, **BENPO** achieving **O(log T)** regret, and **DENPO** as a practical fine-tuning variant; consistent gains for Llama-3-8B-Instruct (v2 2 Oct 2026; Nan, Li, Kroer, Lin; `cs.LG`; affiliation not stated).
- [`2607.18255`](https://arxiv.org/abs/2607.18255) **Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems** — represents a realized language flow as a **semantic generation hypergraph**, induces an agent-level **semantic value function**, defines the **Semantic Shapley Value (SSV)**, and gives **SLIC** (single-trajectory, counterfactual-free) which reduces computation **93.3%** while tracking Monte Carlo Shapley on a medical benchmark and exposing where semantic contribution and failure impact diverge (v2 1 Oct 2026; Pengyi Jiang, Xiaoguang Zhu, Quanyan Zhu; `cs.GT`/`cs.AI`; affiliation not stated).
- [`2609.34695`](https://arxiv.org/abs/2609.34695) **Sufficiency of Zeroth-Order Reward Shaping for Policy Gradient in Stabilization Control** — shows policy-gradient methods can solve stabilization **without first-order (velocity) reward terms**, and that adding them can introduce severe sensitivity as their scale grows, while reward functions must be **zeroth-order complete over goal-relevant coordinates** (first-order state still needed in the observation under low-dissipation assumptions) (28 Sep 2026; Yisheng Zhang, Tao Wang, Sicun Gao; `cs.LG`/`cs.RO`; affiliation not stated).
- [`2609.35052`](https://arxiv.org/abs/2609.35052) **OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models** — anchors evaluation to a fixed set of object instances from the initial observation; **500 cases** across real-world, embodied-robotic, and **game-world** domains with dense annotations for **12,672** rigid/articulated/deformable instances; a hierarchical **Object-Presence-Identity-Structure** evaluator shows average **Identity falls 40.22→23.11** as the reference inventory grows from <20 to >40 objects (28 Sep 2026; Hao Wang et al.; `cs.CV`; affiliation not stated).
- [`2609.35928`](https://arxiv.org/abs/2609.35928) **Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems** — exposing each agent's **model family** to peers causes **factionalism** (agents prefer same-label peers) even with no task reward for it; labeled groups spend **+30% rounds** and **+55% tokens**, with success dropping **96%→81%**; shuffling/arbitrary labels still drive factions, while **hiding labels removes the effect** (28 Sep 2026; Del Giudice, Palma, Migliarini, Galasso, Spinelli; `cs.MA`; affiliation not stated).
- [`2610.01882`](https://arxiv.org/abs/2610.01882) **Flowing Faster to Coordinate: One-Step Online Multi-Agent Flow Policies (OMAF)** — combines expressive generative policies with **efficient one-step action generation** via a Transformer-based flow policy and an approximate path-score surrogate, plus a joint optimization coupling softmax Q-estimation with a joint flow objective; on 10 MPE/MAMuJoCo tasks it reaches up to **3.4× higher returns** and **10.5× sample efficiency** (1 Oct 2026; Zhuoran Li, Yunzhan Li, Xun Wang, Yihan Du, Longbo Huang; `cs.LG`/`cs.MA`; affiliation not stated).
- [`2610.04614`](https://arxiv.org/abs/2610.04614) **Approximate Feedback Nash Equilibria in Constrained Differential Games via Model Predictive Control with Upper Bound Guarantees** — approximates infinite-horizon **feedback Nash equilibrium** trajectories by repeatedly solving finite-horizon open-loop games, with an auxiliary-game formulation selecting horizons/terminal costs and an extension to **hard constraints**; for the unconstrained case it derives an **analytic upper bound** on the MPC-vs-FNE state-trajectory deviation (3 Oct 2026; Balint Varga, Karl Handwerker, Imre Rudas, Peter Galambos; `cs.GT`/`eess.SY`; affiliation not stated).
- [`2610.06885`](https://arxiv.org/abs/2610.06885) **Dynamical low-rank equilibrium computation for stochastic games between advanced persistent threats and moving target defense** — exploits the **intrinsic low-rank** attack/defense influence matrices in ICS dynamics; proposes **DLR-NE**, which augments the rank-r search space, regularizes the core spectrum, and retracts via truncated SVD, converging **geometrically** with explicit error decomposition and per-step cost O(nr²) (a Θ(n/r²) speedup over full-rank value iteration) plus a **certified sensitivity bound**; six power-system experiments show **94% parameter compression at 2.3% utility loss** (v2 7 Oct 2026; under review at *Automatica*; Tian Zijian et al.; `cs.GT`).
- [`2610.09337`](https://arxiv.org/abs/2610.09337) **Ask the Expert: LLM-Guided Reinforcement Learning for Autonomous Cyber Defense** — a **training-time guidance** framework that summarizes hard cyber-defense states, intermittently queries an LLM for host-level recommendations through a constrained action interface, and turns them into **tiered reward shaping** for PPO; the LLM is discarded at deployment, improving sample efficiency over PPO and PBRS baselines on TTCP CAGE CC1/CC2 (**IEEE GLOBECOM 2026**; Fernando Martinez et al.; `cs.AI`; affiliation not stated).
---

## Cross-references (already on file — not re-featured)
- **10-19 siblings (same day)** — [`arxiv-ai-search` 2026-10-19](../2026-10-19/arxiv-ai-search.md) (games lane: `2610.22277` posetal games, etc.), [`tech-report-digest` 2026-10-19](../2026-10-19/tech-report-digest.md) (independently confirms the Monday block counts), [`conference-digest` 2026-10-19](../2026-10-19/conference-digest.md) (defers the games lane; mentions `2610.23266` JointCore), [`arxiv-daily` 2026-10-19](../2026-10-19/arxiv-daily.md) (contains **none** of this edition's 62 fresh IDs).
- **On-file in-lane papers (cross-ref, by wiki hit count)** — `2610.20473` SafeAdapt-Poker (23 hits), `2610.08621` (16), `2610.00416` (15), `2610.22882` (11), `2610.17895` (11), `2610.11723` (10), `2610.20200` (9), `2610.19422` (9), `2610.21711` (9), `2610.22779` (8), `2610.22626` (6), `2609.32544` (5), `2610.13947` (2).
- **10-18 `game-rl-daily` anchors** — **Multiverse** `2603.26782` (19 hits), **HDPCG** `2602.18943` (17), **Playtrace Reconstructive Partitioning** `2607.12097` (7), **PCG Benchmark** `2503.21474` (6), **MuScriptor** `2610.14955`, **PRO-LONG** `2607.20064`, **BehaviorFormer** `2610.16322`, **B-Human '26** `2610.14733`, **Honda convention quantification** `2610.20205`, **SpecWM** `2610.15429`, **PAWA** `2610.20240`, smoothed games `2610.14150`/`2610.22149`, **alternating CFR** `2610.21970` (9) — featured in [`game-rl-daily` 2026-10-18](../2026-10-18/game-rl-daily.md).
- **10-17 / 10-16 `game-rl-daily`** — `2610.22319` Gemini 4 Minecraft team (11), `2610.20665` RealtimeBench + TORSI (23), `2610.20786` EvolvingBrain (9), `2610.21283` Mallea, `2610.22341` 3DCodeVerse, `2610.22355` OmniVerifier-C1, `2610.22149` smoothed PI/VI (9) — featured in [`game-rl-daily` 2026-10-17](../2026-10-17/game-rl-daily.md) and [`game-rl-daily` 2026-10-16](../2026-10-16/game-rl-daily.md).

---

## Contradictions / open questions
- **⚠️ CORRECTION — the Round-Robin EF1-at-equilibrium claim was false.** [`2610.23686`](https://arxiv.org/abs/2610.23686) shows **not every pure NE of Round-Robin is EF1**, explicitly correcting **arXiv:2109.08644 (WINE 2021; Math. Oper. Res. 49(4), 2024)**; the true guarantee is **1/2-EF1 + PROP1** for recursively balanced picking sequences, with a **2/3-EF1 upper bound on how strong a guarantee is achievable for all equilibria**. **No page in the wiki asserts the old claim** (grep-verified), so this note is *prospective*: any future ingest of the 2109.08644 result must carry the correction. Together with [`2610.23040`](https://arxiv.org/abs/2610.23040), the wiki should track **"fair picking sequences under strategic revision"** as a live thread.
- **Memory vs execution in video world models — not a contradiction but a re-diagnosis.** [`2610.23542`](https://arxiv.org/abs/2610.23542) (MIST) argues that low "memory" scores often reflect **failure to execute the instructed change**, and proposes an instruction-revision agent rather than a memory module; [`2610.23423`](https://arxiv.org/abs/2610.23423) (Momentum) and [`2610.23795`](https://arxiv.org/abs/2610.23795) (PPMem) instead build **persistent 3D memory**. The three are complementary, but the wiki should be careful not to read "persistent memory" papers as fixes for what MIST identifies as an **execution** failure.
- **Text world-model capability is far from reliable.** [`2610.22708`](https://arxiv.org/abs/2610.22708) (GlobeBench) finds **631 of 1,632 tasks unsolved by any of 20 models** and **dependent-object propagation success averaging 5.1%** — the quantified ceiling for LLM-as-environment-simulator, consistent with the 10-18 edition's world-model caveats.
- **PCG lane empty for a fourth consecutive day** (10-16/10-17/10-18/10-19). Targeted `pcg`/`levelgen`/`nethack` queries produce only off-lane false positives. Whether classic PCG research is *seasonally quiet* or has *migrated into broader world-model/agent work* (FCTS terrain generation §4, executable-world benchmarks) is now a recurring open question.
- **Industry/studio lane empty again** — no studio paper this run; industrial involvement is embedded in featured affiliations (Huawei, Tencent, Ant Group, Google Intrinsic, DFKI/Hessian.AI).
- **No contradicting claim** against existing wiki sources was identified for the 62 fresh items; all are new-to-wiki and **single-source**.

---

*Generated 2026-10-19 (Monday) — newer arXiv announcement block is live this run (v1 15–16 Oct, `2610.22373–2610.23856`). Scope = ten-category `/list/*/new` parse (1,034 entries) + backward search sweep over 28 Sep – 8 Oct (228 candidates → 18 curated) + proceedings pass. All 62 fresh IDs grep-verified 0-hit against `wiki/**/*.md` before writing; the 10-16/10-17/10-18 sibling editions' picks are cross-referenced, not repeated. Affiliation recovery: 29/33 featured from the paper's own LaTeXML `Affiliation:` block or rendered author footnote; 4 marked "not stated" (never inferred). Venues stated only where explicit.*
