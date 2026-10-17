---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-17)"
type: synthesis
created: 2026-10-17
updated: 2026-10-17
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, multi-agent, game-theory, foundation-models, world-models, pcg, benchmarks, npc, inverse-rl, bandits, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-17)

> A **seven-lane sweep** (Game RL, Game AI Bot, Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, Related Techniques) over the **fresh Fri 2026-10-16 arXiv announcement block**, harvested again from the `arxiv.org/list/cs.*/new` listing pages (cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.GT, cs.MA, cs.HC, cs.SE). **Method note up front**: the arXiv **export API remained unavailable** this run — `https://export.arxiv.org/api/query` → HTTP 000/429 — so metadata was harvested from the listing HTML pages plus per-paper `arxiv.org/abs/{id}` (abstracts, authors, comments) and LaTeXML `arxiv.org/html/{id}v1` (printed affiliations) pages. Every featured ID was **grep-verified 0-hit against the live `wiki/**/*.md` tree before writing** (§0.3). Featured IDs span `2610.20665`–`2610.22372`; submissions 10–15 Oct 2026.
>
> **Saturday second pass.** arXiv posts **no weekend announcements**, so the newest fully-populated block on 2026-10-17 is still **Friday, 2026-10-16** — the same block already reported by the [10-16 `game-rl-daily`](../2026-10-16/game-rl-daily.md) (22 papers) and the [10-17 `arxiv-ai-search`](./arxiv-ai-search.md). This edition is therefore a **complement, not a re-run**: it deliberately features the game-lane papers that the 10-16 edition did **not** claim — 24 fresh items, all 0-hit — and cross-references the 10-16 set rather than repeating it (§0.3).
>
> **Three threads run through this pass.**
>
> **① The block's game-theory/RL-theory layer is unusually deep.** Two SODA/Journal-tier theory papers land here: [`2610.21487`](https://arxiv.org/abs/2610.21487) proves the **Value Approximation Problem for time-bounded weighted timed games is decidable in 4-ExpTime** (the general Approximation problem is undecidable), and [`2610.22149`](https://arxiv.org/abs/2610.22149) (SODA 2027) **drops the ergodicity assumption** from smoothed analysis of policy/value iteration, giving smoothed-polynomial time for *any* deterministic discounted and mean-payoff game graph. Around them sit the RL-theory layer: constrained-RL-under-partial-observability finite-time guarantees ([`2610.21548`](https://arxiv.org/abs/2610.21548)), transfer learning in bandits from *unknown adaptive policies* ([`2610.21582`](https://arxiv.org/abs/2610.21582)), and simultaneous multi-policy evaluation ([`2610.22252`](https://arxiv.org/abs/2610.22252)).
>
> **② "Code world models" are consolidating into a game/foundation-model lane.** Three independent papers now build **executable, rule-governed worlds**: [`2610.21283`](https://arxiv.org/abs/2610.21283) (**Mallea**, PKU) builds *text→code world models* with an object-centric coding agent that steers and re-renders a persistent world; [`2610.22341`](https://arxiv.org/abs/2610.22341) (**3DCodeVerse**) scales a 2M executable-3D-code corpus with a multi-agent DAG harness (**90% pairwise win vs Claude Design**); and [`2610.22355`](https://arxiv.org/abs/2610.22355) (**OmniVerifier-C1**, NeurIPS 2026) argues the transition to *structured world-modeling agents* "critically hinges" on **pairwise graded visual verifiers**, validated on **Maze and Sudoku**. Alongside them, [`2610.21783`](https://arxiv.org/abs/2610.21783) (**ACT3D**, UCSD × Georgia Tech) treats a 3D scene as an *interactive environment* and learns an exploration policy by **outcome-only RL** — the strongest fresh "VLM agents that act in worlds" result here.
>
> **③ Real-time, wall-clock game evaluation doubles down — and a naming collision appears.** [`2610.22155`](https://arxiv.org/abs/2610.22155) (**Realtime-Bench**) is a *second, independent* real-time interactive benchmark (UT Austin × OSU × UIUC × NVIDIA × Northwestern) that is **distinct from** the 10-16 edition's [`2610.20665`](https://arxiv.org/abs/2610.20665) (**RealtimeBench + TORSI**) — same idea, different group, both in the same block (§5, and flagged as an open question). [`2610.22312`](https://arxiv.org/abs/2610.22312) (**Grid-Bench**) makes discrete-world state prediction executable and checkable across 2D–4D grids. See §5.

---

## §0 Method and Corpus

### 0.1 Coverage
- **Source**: `arxiv.org/list/{cs.AI,cs.LG,cs.CL,cs.CV,cs.RO,cs.GT,cs.MA,cs.HC,cs.SE}/new` for the **Fri 16 Oct 2026** announcement block — **1,209 unique merged entries** parsed (deduplicated across categories: cs.LG 467, cs.AI 453, cs.CL 267, cs.CV 253, cs.RO 149, cs.MA 34, cs.GT 16, cs.HC 33, cs.SE 49; merging leaves 1,209 unique), of which **866 carry `2610.*` IDs**.
- **Filter**: title keyword sweep across the game lanes (game/gaming/gameplay/Atari/self-play/open-ended/world model/level/embodied/exploration/environment/player/NPC/…), then manual triage of the printed abstracts; the game-lane candidates were then narrowed to **fresh (0-hit)** items and feature-ranked. 24 featured.
- **Window vs. siblings**: the same-day siblings already claim the fresh `>2610.20610` block — [`arxiv-daily`](../2026-10-16/arxiv-daily.md), [`conference-digest`](../2026-10-16/conference-digest.md) & [`2026-10-17/conference-digest`](./conference-digest.md), [`arxiv-ai-search`](../2026-10-16/arxiv-ai-search.md) & [`2026-10-17/arxiv-ai-search`](./arxiv-ai-search.md), and [`game-rl-daily` 2026-10-16](../2026-10-16/game-rl-daily.md). Overlap is managed explicitly in §0.3; in particular the **five games-lane picks** of today's `arxiv-ai-search` (`2610.22277` posetal-games, `2610.22322` agent swarms, `2610.22138` hidden-belief collapse, `2610.20908` replicable dueling bandits, `2610.22152` spec-gaming gridworld) and the **22 picks** of the 10-16 `game-rl-daily` are **cross-referenced, not re-featured**.

### 0.2 Sweep
1. Listing-page harvest (`/new`) for nine categories (`curl` + browser UA — the plain `webfetch` path returned HTTP 400/000; `curl` returned HTTP 200 throughout).
2. Per-paper `abs` pulls for submission dates, subjects, venue comments **and abstracts** (the listing pages carry no abstracts this run).
- **3. HTML pulls (`/html/{id}v1`)** to recover author affiliations where printed.
4. **Dedup** — each candidate ID `grep`-tested against the whole `wiki/` tree (§0.3).

### 0.2.1 Rate limiting
- **Export API**: `https://export.arxiv.org/api/query?id_list=…` returned **HTTP 000** (connection refused/blackholed) throughout, consistent with the 10-15/10-16/10-17 runs' HTTP 429 wall.
- **Listing pages**: all nine returned **HTTP 200** via `curl` + browser UA (54 KB–1.47 MB). Plain `webfetch` on the same URLs returned HTTP 400.
- **Abs pages**: HTTP 200 with a **≥2 s inter-request delay**; a burst of 30 concurrent requests initially returned HTTP 000 (connection resets), so fetches were throttled. **HTML pages** are large (0.1–1.7 MB) and were fetched 4-at-a-time with a 2 s pause.
- **A shell caveat worth recording**: under **zsh**, `for id in $IDS` does **not** word-split an unquoted scalar, so the loop silently issued a single malformed request (`HTTP 000`) until switched to a zsh array — the "rate limit" first suspected was in fact this shell bug.

### 0.3 Dedup accounting (featured + notable cross-references)
| arXiv ID | Lane | Venue/subject | In-wiki hits | Status |
|----------|------|---------------|-------------:|--------|
| 2610.21487 (time-bounded weighted timed games) | Game GT | cs.GT | 0 | **fresh** |
| 2610.22149 (smoothed analysis PI/VI) | Game GT | cs.GT; SODA 2027 | 0 | **fresh** |
| 2610.21764 (Q(γ_H) multi-discount) | RL | cs.LG; ICONIP 2026 | 0 | **fresh** |
| 2610.21548 (constrained RL under partial observability) | RL | cs.LG | 0 | **fresh** |
| 2610.21582 (transfer bandits, unknown policy) | RL / bandits | cs.LG | 0 | **fresh** |
| 2610.22252 (multi-policy evaluation, linear bandits) | RL / bandits | cs.LG | 0 | **fresh** |
| 2610.22198 (robust multi-agent pursuit) | Game RL | cs.RO/cs.MA; IEEE CDC 2026 | 0 | **fresh** |
| 2610.21746 (delegation dilemma) | Game GT / MAS | cs.AI/cs.LG/cs.MA | 0 | **fresh** |
| 2610.22316 (steering LLM agents) | Game AI Bot | cs.AI/cs.LG/cs.MA | 0 | **fresh** |
| 2610.21887 (MetaShare) | Game AI Bot | cs.MA; NeurIPS 2026 WS | 0 | **fresh** |
| 2610.21243 (responsibility-centered coordination) | Game AI Bot | cs.AI/cs.MA | 0 | **fresh** |
| 2610.21492 (MetaExp) | Game AI Bot | cs.AI | 0 | **fresh** |
| 2610.22056 (PRM4RL) | Related / reward | cs.AI; NeurIPS 2025 | 0 | **fresh** |
| 2610.21783 (Learning to Think and Explore in 3D World) | Game Fdn | cs.CV | 0 | **fresh** |
| 2610.21283 (Mallea code world models) | Game Fdn / PCG | cs.AI/cs.CV | 0 | **fresh** |
| 2610.22341 (3DCodeVerse) | Game Fdn / PCG | cs.AI/cs.CV | 0 | **fresh** |
| 2610.22355 (OmniVerifier-C1) | Game Fdn / world model | cs.CL; NeurIPS 2026 | 0 | **fresh** |
| 2610.22343 (GeoState) | Game Fdn / world model | cs.RO/cs.AI/cs.CV/cs.LG | 0 | **fresh** |
| 2610.22155 (Realtime-Bench) | Benchmarks | cs.AI | 0 | **fresh** |
| 2610.22312 (Grid-Bench) | Benchmarks | cs.CL | 0 | **fresh** |
| 2610.21233 (children's verification in game HAI) | Benchmarks / HCI | cs.HC; HCI Intl 2026 | 0 | **fresh** |
| 2610.22290 (EliteReplay, QD) | Related | cs.AI | 0 | **fresh** |
| 2610.22340 (DSP: Dexterity from Supervised Play) | Related | cs.RO/cs.AI | 0 | **fresh** |
| 2610.22285 (targeted active preference learning) | Related | cs.RO/cs.HC/cs.AI/cs.LG; CoRL 2026 | 0 | **fresh** |
| 2610.20665 (RealtimeBench + TORSI) | Benchmarks | cs.AI | 1 | cross-ref (10-16 `game-rl-daily`) |
| 2610.22319 (Gemini 4 Minecraft) | Game AI Bot | cs.AI | 1 | cross-ref (10-16 `game-rl-daily`) |
| 2610.20786 (EvolvingBrain) | Game AI Bot | cs.AI | 1 | cross-ref (10-16) |
| 2610.21525 (CriticaLLM) | Game AI Bot | cs.AI | 1 | cross-ref (10-16) |
| 2610.21040 (RRI) | Game AI Bot | cs.AI/cs.MA | 1 | cross-ref (10-16) |
| 2610.21156 (MASP) | Game AI Bot | cs.CL | 1 | cross-ref (10-16) |
| 2610.20811 (RIGen) | Game Fdn | cs.CV | 1 | cross-ref (10-16) |
| 2610.21910 (CoWorld Reasoner) | Game Fdn | cs.AI | 1 | cross-ref (10-16) |
| 2610.22311 (Velox) | Game Fdn | cs.CV | 1 | cross-ref (10-16) |
| 2610.21095 (OneWM) | Game Fdn | cs.CV | 1 | cross-ref (10-16) |
| 2610.21612 (Intrinsic Dynamics WM) | Game Fdn | cs.AI | 1 | cross-ref (10-16) |
| 2610.20693 (Orbia) | Benchmarks | cs.CV | 1 | cross-ref (10-16) |
| 2610.21244 (System1-Arena) | Benchmarks | cs.CL/cs.AI | 1 | cross-ref (10-16) |
| 2610.22289 (env-agnostic coding agents) | Benchmarks | cs.AI | 1 | cross-ref (10-16) |
| 2610.21319 (CA-MAMBA) | Related | cs.AI | 1 | cross-ref (10-16) |
| 2610.20866 (SHRED) | Related | cs.LG/cs.RO | 1 | cross-ref (10-16) |
| 2610.19714 (uncertainty self-play driving) | Related | cs.RO | 1 | cross-ref (10-16) |
| 2610.21029 (SCARCE) | Related | cs.MA | 1 | cross-ref (10-16) |
| 2610.21711 (LLM price competition) | Game GT | cs.GT | 1 | cross-ref (10-16) |
| 2610.21912 (Learning Rewards in Strategic Games) | Game GT | cs.GT | 1 | cross-ref (10-16) |
| 2610.22287 (Temporal-objective MARL) | Game RL | cs.LG/cs.MA | 1 | cross-ref (10-16) |
| 2610.15054 (Iterated games) | Game RL | physics.soc-ph | 1 | cross-ref (10-16) |
| 2610.22277 (posetal games) | Game GT | cs.RO/cs.GT/cs.MA | 2 | cross-ref (10-17 `arxiv-ai-search`) |
| 2610.22322 (agent swarms) | Game AI Bot | cs.CL/cs.AI/cs.MA | 2 | cross-ref (10-17 `arxiv-ai-search`) |
| 2610.22138 (hidden belief collapse) | Game AI Bot | cs.CL/cs.AI/cs.MA | 2 | cross-ref (10-17 `arxiv-ai-search`) |
| 2610.20908 (replicable dueling bandits) | Related / bandits | cs.LG/cs.AI | 2 | cross-ref (10-17 `arxiv-ai-search`) |
| 2610.22152 (spec gaming gridworld) | Game RL | cs.AI/cs.LG | 2 | cross-ref (10-17 `arxiv-ai-search`) |
| 2610.21970 (CFR alternation) | Game GT | cs.GT | 1 | cross-ref (10-16 `conference-digest`) |
| 2610.20473 (SafeAdapt-Poker) | Game RL | cs.AI/cs.GT | 4 | cross-ref (10-15 siblings) |
| 2608.15146 (PureTD backgammon) | Game RL | cs.LG | 4 | cross-ref (featured 08-23) |
| 2610.14883 (MARL-BattleGrounds) | Benchmarks | cs.LG | 3 | cross-ref (featured 10-15) |
| 2610.16776 (Game-Creation-Agents, Tencent) | Industry | cs.AI | 4 | cross-ref (featured 10-15) |

**Already-on-file sibling edits** the block also produced, not game-lane but adjacent and *not* re-featured here: `arxiv-ai-search` 2026-10-17 games-lane (`2610.22277`, `2610.22322`, `2610.22138`, `2610.20908`, `2610.22152`), and `2610.20473`/`2610.21970`/`2608.15146` cross-refs.

### 0.4 Affiliations and venues
- **Abs/listing pages frequently do not print affiliations.** Where an institution could not be read from the paper's own LaTeXML `Affiliation:` author block, it is marked **"not stated"** and **not inferred** from surnames or email domains (standing wiki discipline; tentative inferences flagged as such).
- Venues are stated **only where explicit** (e.g. `SODA 2027`, `ICONIP 2026`, `NeurIPS 2025/2026`, `CoRL 2026`, `IEEE CDC 2026`, `HCI International 2026`); otherwise `arXiv preprint`. **No result independently replicated.**

### 0.5 Temp artifacts
- Scratch dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` (listing HTML, `abs/`, `html/`, parsed JSON) — deleted after this write-up.

---

## §1 Game RL — Reinforcement Learning, Self-Play, Multi-Agent & Game Theory

### ★★★ Approximating the Value of Time-Bounded Weighted Timed Games
- **Authors**: Isa Vialard, Joël Ouaknine
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.21487 (15 Oct 2026) — `cs.GT`.
- **Link**: https://arxiv.org/abs/2610.21487
- **Abstract and key innovations**: The **Value Problem** for **weighted timed games** (timed automata extended with weights and adversarial control) asks whether the value of a game with a **reachability objective** exceeds a rational threshold. It is **undecidable** to compute the value exactly, and the natural fallback — the **Approximation Problem** — is *also* undecidable in general. This paper proves that the **Approximation Problem is decidable in 4-ExpTime** for weighted timed games **whose executions are time-bounded**.
- **Why it matters here**: a clean new **decidability boundary** for real-time adversarial games — the "you cannot solve it exactly, but you can bound it when the clock is bounded" result. It sits at the junction of the wiki's **timed/verification-games** and **real-time game AI** threads (§5's wall-clock benchmarks).
- **Caveats**: **fully fresh — 0 hits in wiki**; 4-ExpTime is a complexity upper bound, not a practical algorithm; affiliation not printed.

### ★★★ Smoothed analysis of policy iteration and value iteration for deterministic discounted and mean-payoff games played on any graph
- **Authors**: Bruno Loff, Mateusz Skomra
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: **SODA 2027** — also arXiv:2610.22149 (15 Oct 2026) — `cs.GT`. 56 pages.
- **Link**: https://arxiv.org/abs/2610.22149
- **Abstract and key innovations**: Turn-based games have "the state of linear programming in the 1970s": **policy iteration (PI)** and **value iteration (VI)** work well in practice but are **exponential-time** on some inputs, and no polynomial algorithm is known. A prior result (Loff & Skomra) gave **smoothed-polynomial** PI for deterministic discounted and mean-payoff games on an **ergodic** graph. This paper **drops the ergodicity assumption**: their PI algorithms run in **smoothed-polynomial time for any game graph**, via a generalized criterion under which a game is "well-conditioned" and a new proof. It additionally gives **three smoothed-polynomial VI algorithms** (two fixed-point-iteration variants plus a faster simultaneous-elimination variant) with improved bounds. The framing is explicitly the **Spielman–Teng smoothed-analysis** explanation for why PI performs well in practice.
- **Why it matters here**: the strongest fresh **theory-of-game-solving** result in the wiki — it explains *why* the value/policy iterators used across game AI work well, in the Spielman–Teng smoothed-analysis sense, now without the ergodicity crutch.
- **Caveats**: **fully fresh — 0 hits in wiki**; deterministic (not stochastic) games; smoothed (not worst-case) guarantees.

### ★★ Q(γ_H): Entropy-Guided Horizon Mixing in Multi-Discount Q-Learning
- **Authors**: Arwa Albelaihi, Abdulrahman Altahhan
- **Affiliation**: School of Computer Science, University of Leeds, UK.
- **Venue**: **ICONIP 2026** — also arXiv:2610.21764 (15 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.21764
- **Abstract and key innovations**: A fixed discount factor imposes a **single planning horizon** throughout training, ignoring that early exploration and long-term credit assignment have different demands. **Q(γ_H)** maintains **multiple discount-specific heads** and combines them at *control time* with an **entropy-derived confidence signal**; the mixing weights shift from shorter- to longer-horizon heads as policy confidence rises. Crucially it does **not modify the individual Bellman updates** — horizon adaptation is decoupled from learning.
- **Why it matters here**: a lightweight, drop-in **adaptive-horizon** mechanism relevant to any game RL agent that must trade fast reaction for long-horizon planning; complements the wiki's real-time/game-clock thread (§5).
- **Caveats**: **fully fresh — 0 hits in wiki**; "strongest improvements on delayed-credit tasks"; not game-specific (classical control + deep-RL benchmarks).

### ★★ Finite-Time Guarantees for Constrained Reinforcement Learning under Partial Observability
- **Authors**: Valentina Zaccaria, Philip Jordan, Tingting Ni, Gian Antonio Susto, Maryam Kamgarpour
- **Affiliation**: University of Padova; SYCAMORE, EPFL.
- **Venue**: arXiv:2610.21548 (15 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.21548
- **Abstract and key innovations**: Studies RL in **constrained POMDPs (CPOMDPs)** where optimal policies may need **arbitrarily long observation-action histories**. It converts **finite history windows** into states of a constrained MDP and gives a **primal–dual algorithm** with the **first non-asymptotic** guarantee under incomplete state information, with a **finite-sample bound certifying constraint satisfaction** and convergence. It bounds the approximation error of the finite-memory representation and shows how to choose the window to hit a target accuracy.
- **Why it matters here**: the fresh **safe/constrained RL under partial observability** theory result — the "safety under hidden state" counterpart to the wiki's constrained-MARL thread (CA-MAMBA `2610.21319`).
- **Caveats**: **fully fresh — 0 hits in wiki**; tabular/finite-memory scope; bound depends on an ergodicity-like mixing assumption.

### ★★ Transfer Learning in Bandits from Unknown Adaptive Policies: Problem-Dependent Lower and Upper Bounds
- **Authors**: Adrien Prevost, Timothee Mathieu, Waris Radji, Odalric-Ambrym Maillard
- **Affiliation**: Équipe Scool, Univ. Lille / Inria / CNRS / Centrale Lille, France.
- **Venue**: arXiv:2610.21582 (15 Oct 2026) — `cs.LG`. 50 pages.
- **Link**: https://arxiv.org/abs/2610.21582
- **Abstract and key innovations**: Prior-data transfer in stochastic bandits usually assumes a **fixed offline dataset** or a **known** source. Here the historical observations come from a **previous adaptive decision process whose policy is unknown** (sample sizes may be random and data-dependent), with bounded rewards. The paper derives the **first asymptotic minimax (problem-dependent) lower bounds** for this setting and designs/gives an algorithm beating naive pooling; it characterizes the *impossibility* (a lower bound) matching the impossibility of the offline case, plus an **adaptive** algorithm that achieves both bounds.
- **Why it matters here**: a purely-theory bandit result, but directly relevant to **self-play/curriculum data reuse** and to the wiki's reproducibility/bandit threads (§ Related `2610.20908`).
- **Caveats**: **fully fresh — 0 hits in wiki**; abstract cut off in listing — mechanism details beyond the abstract not verified.

### ★★ Explore Once, Evaluate Many: Multiple Policy Evaluation for Stochastic Linear Bandits
- **Authors**: Spyros Dragazis, Yilei Chen, Aldo Pacchiano
- **Affiliation**: Boston University; Broad Institute of MIT and Harvard.
- **Venue**: arXiv:2610.22252 (15 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.22252
- **Abstract and key innovations**: **Multi-policy / offline evaluation** is central to training and comparing RL agents without fresh environment interaction. The paper studies **simultaneous off-policy evaluation of K policies** in **stochastic contextual linear bandits**, with general function approximation and **no known behavior policy**, and gives an algorithm with a sample-complexity bound scaling as `poly(d, β, L, log K, 1/ε²)` — i.e., **logarithmic in the number of policies to evaluate**.
- **Why it matters here**: the fresh **efficient-evaluation** primitive — "evaluate many candidate policies from one exploratory dataset," the offline-RL/game-benchmark analogue of the wiki's evaluation threads.
- **Caveats**: **fully fresh — 0 hits in wiki**; linear-bandit (not deep) scope; theoretical.

### ★★ Robust Multi-Agent Pursuit with Preemptive Communication via Reachability-Based Control Barrier Functions
- **Authors**: Madison Book, Justin Bradley
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: **IEEE CDC 2026** — also arXiv:2610.22198 (15 Oct 2026) — `cs.RO`; `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.22198
- **Abstract and key innovations**: Safe multi-agent coordination usually assumes **continuous, perfect state sharing** that resource-constrained robots cannot provide. This work proposes a **unified control/communication strategy** that guarantees **inter-agent safety under intermittent communication** and demonstrates it in a **pursuit-evasion scenario**: each agent computes the **reachable set** of neighbors from the **last received state**, then solves a **control-barrier-function (CBF)**-based safe control input that keeps the pursuer maintaining **reachability** to the evader.
- **Why it matters here**: a concrete **pursuit-evasion (game-theoretic) multi-agent** result with a *safety certificate* — the control-theoretic cousin of the wiki's pursuit/MARL entries, and a rare "communication is part of the strategy" formulation.
- **Caveats**: **fully fresh — 0 hits in wiki**; robotics simulation/control (not a game environment); 6-page CDC paper; affiliation not printed.

### ★ The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance
- **Authors**: Arin Mukhopadhyay, Aris Filos-Ratsikas, Panayiotis Danassis
- **Affiliation**: University of Edinburgh; Imperial College London; University of Southampton.
- **Venue**: arXiv:2610.21746 (15 Oct 2026) — `cs.AI`; `cs.LG`, `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.21746
- **Abstract and key innovations**: Models **endogenous delegation** in a **repeated game** where agents form institutions that share costs and delegate to **self-interested representatives**. A reduced-form model yields a **scale–accountability tradeoff**: larger constituencies share costs better but a center's marginal value of retaining any one member falls with size, so **individual exit sustains non-exploitative delegation only up to an endogenous accountable size**; it identifies regions where **polycentric governance is necessary**. They test predictions with **LLM-agent simulations** (30 agents; Sol vs. Luna), observing **emergent cycles of concentration, exploitation, exit, and re-formation**, and that stronger models assume leadership no more often but exercise authority differently.
- **Why it matters here**: the fresh **emergent-institutions / governance-as-a-game** study — pairs with the wiki's SCARCE (`2610.21029`) emergent-institutions entry, and is one of the block's few **LLM-agent repeated-game** experiments.
- **Caveats**: **fully fresh — 0 hits in wiki**; reduced-form analytical model + stylized LLM simulations; model capacity is a paper-defined variable.

---

## §2 Game AI Bot — LLM-Powered Game Agents, NPC Intelligence & Multi-Agent Systems

### ★★★ Learning to Steer LLM Agents and Multi-Agent Systems
- **Authors**: Leyang Shen, Yaxin Gong, Yang Zhang, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Fuli Feng, Chun Kai Ling, Tat-Seng Chua
- **Affiliation**: National University of Singapore; University of Science and Technology of China; Qwen Business Unit of Alibaba.
- **Venue**: arXiv:2610.22316 (15 Oct 2026) — `cs.AI`; `cs.LG`, `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.22316
- **Abstract and key innovations**: Long-horizon LLM agents and multi-agent systems suffer **goal drift** — execution deviates from the overall objective. The paper learns a **steering agent** that supervises execution on the fly, with a **low-cost fast path** (single scoring pass producing a **verifiable drift judgment**) and a **high-cost slow path** that generates a corrective **intervention**, triggered only when needed. Trained with a **pairwise likelihood objective** cast as a GRPO-optimizable reward.
- **Why it matters here**: the fresh **run-time supervisor for game/agent loops** — a learned "referee" that intervenes only on drift, directly applicable to NPC orchestration and to the wiki's long-horizon-agent thread.
- **Caveats**: **fully fresh — 0 hits in wiki**; evaluated on search/execution tasks (abstract cut off before the full result set in listing); GRPO-trained, so sensitive to reward design.

### ★★ MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents
- **Authors**: Vishal Bhutani, Prasang Gupta, Sumanth Chundru, Kevin Paul
- **Affiliation**: PricewaterhouseCoopers (PwC).
- **Venue**: **NeurIPS 2026 Meta-Agents Workshop** — also arXiv:2610.21887 (15 Oct 2026) — `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.21887
- **Abstract and key innovations**: Open-ended self-improving agents (à la **GEA** / **DGM-Hyperagents**) rarely retain **failed** improvement attempts as reusable cross-branch knowledge, and search collapses onto redundant strategies. **MetaShare** records **successful and unsuccessful agent modifications with signed performance deltas**, retrieves diverse high-performing strategies *and* high-confidence failures from **other lineages**, injects absent mechanism categories via a **task-blind auditor**, and de-ranks redundancy; multiple meta-agents propose modifications in parallel, gated by a deterministic selector.
- **Why it matters here**: the fresh **failure-aware open-ended self-improvement** mechanism — "remember which failures not to repeat" as an explicit, transferable artifact; the wiki's open-ended-learning lane gains a concrete memory design.
- **Caveats**: **fully fresh — 0 hits in wiki**; evaluated on text/agent tasks (paper review, coding, math grading, robotics reward design, audit-risk), not games per se; industrial (PwC) authorship.

### ★★ A Responsibility-Centered Coordination Mechanism for Decentralized Multi-Agent Systems (RCM)
- **Authors**: Thi-Nhung Nguyen, Viet-Thanh Pham, Linhao Luo, Thuy-Trang Vu, Dinh Phung
- **Affiliation**: Department of Data Science & AI, Monash University.
- **Venue**: arXiv:2610.21243 (15 Oct 2026) — `cs.AI`; `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.21243
- **Abstract and key innovations**: Centralized orchestration bottlenecks scalability; decentralized schemes leave **responsibility for delegated dependencies and failure recovery** unclear. **RCM** uses **commitments** to couple task delegation with **explicit responsibilities**, and **recursive delegation** so agents retain upstream responsibility while locally orchestrating downstream commitments — preserving accountability across delegation chains and letting **global coordination emerge** without centralized control. Operationalized via responsibility-constrained decision-making + a **Responsibility-oriented Communication Protocol (RCP)**.
- **Why it matters here**: the fresh **accountable multi-agent coordination** design — a natural complement to the wiki's delegation/commitment and MAS-orchestration entries, with an explicit "responsibility" axis rarely modeled in game-agent systems.
- **Caveats**: **fully fresh — 0 hits in wiki**; reasoning/coding/executable-agent environments (not games); evaluation baselines are paper-defined.

### ★★ MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling
- **Authors**: Renhao Li, Xinjie Shen, Yang Su, Jianhong Tu, Derek F. Wong, Dayiheng Liu, Min Yang
- **Affiliation**: University of Macau; Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences; Georgia Institute of Technology; Alibaba Token Hub, Alibaba Group.
- **Venue**: arXiv:2610.21492 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.21492
- **Abstract and key innovations**: Whether **experience learning itself** can become a *transferable* model capability (rather than a per-task scaffold) is open. **MetaExp** trains it through **verifiable task families with controlled cross-task structure**: **Shared-Tool** families fix black-box tools to elicit *operational* experience; **Shared-Workflow** families preserve latent procedures to elicit *procedural* experience. It scales environments, collects and filters **sequential interaction trajectories**, and fine-tunes **Qwen3.5-122B-A10B** on 4,956 trajectories from 1,000 task families; with parameters frozen downstream it improves by **+8.5 pts on SpreadsheetBench**, **+2.3 on APEX-Agents**, **+14.8 on AutomationBench**, persisting under domain-excluded training.
- **Why it matters here**: the fresh **in-context RL / experience-as-capability** result — the "learn to learn from interaction" thread the wiki tracks for agents (cf. MetaExp's kin), with a large scale bake-off.
- **Caveats**: **fully fresh — 0 hits in wiki**; enterprise/agent benchmarks (spreadsheets/automation), not game environments; model name as reported.

---

## §3 Game Foundation Models & World Models

### ★★★ Learning to Think and Explore in 3D World (ACT3D)
- **Authors**: Yijiang Li, Bingyang Wang, Nuno Vasconcelos
- **Affiliation**: University of California, San Diego; Georgia Institute of Technology.
- **Venue**: arXiv:2610.21783 (15 Oct 2026) — `cs.CV`.
- **Link**: https://arxiv.org/abs/2610.21783
- **Abstract and key innovations**: Trains VLMs to **think and actively explore 3D space** while preserving the model's **native single-image visual encoding** — the 3D scene is treated purely as an **environment** interacted with through actions (e.g. *move left*) and observations (rendered images). Each rollout starts from a first-person view + a visual question; the model iteratively **reasons, navigates, and reorients** before answering. After trajectory-supervised finetuning it applies **RL with rewards driven primarily by final-answer correctness**, giving **no direct supervision over which viewpoints/actions to take**. Across six 3D benchmarks, **ACT3D reaches 53.2%** (+22.0% over base Qwen, surpassing **Gemini 3.6 Flash**), using **50–70% fewer input frames**, and generalizes +5.9% to unseen domains; gains rise from **+0.6%** (answerable from first view) to **+16.3%** (requiring extensive exploration).
- **Why it matters here**: the freshest evidence that **outcome-only RL teaches an exploration policy** for a VLM in a 3D world — "learn when and how to acquire visual evidence," the interface between game agents and world models.
- **Caveats**: **fully fresh — 0 hits in wiki**; 3D benchmark suite (not a game engine); "surpasses Gemini 3.6 Flash" is paper-asserted.

### ★★★ Mallea: Building, Steering, and Memorizing Worlds with Coding Agent
- **Authors**: Xuanyi Liu, Ruiqi Li, Siwei Ma
- **Affiliation**: Peking University.
- **Venue**: arXiv:2610.21283 (15 Oct 2026) — `cs.AI`; `cs.CV`.
- **Link**: https://arxiv.org/abs/2610.21283
- **Abstract and key innovations**: Argues for **code world models** — representing world dynamics through **explicit state and executable rules**. **Mallea** builds, steers, and memorizes worlds from text: a **coding agent** infers object interaction requirements and jointly plans **object structure, properties, and rules** (favoring compact representations); the world evolves under the planned rules, **optional user actions steer it**, and **text requests edit properties/extend capabilities with unaffected state preserved**. **Object texture memory** retains reusable appearance only for *whitebox-defined* objects and adapts as they change; a **program advances world state** while a **generative renderer** combines current structure with remembered appearance.
- **Why it matters here**: the fresh anchor for the **executable/steerable world-model** lane — worlds as *code + editable rules + persistent memory*, the closest thing in this block to a **PCG-by-coding-agent** system.
- **Caveats**: **fully fresh — 0 hits in wiki**; a system paper (not benchmarked on classic game RL); "world" scope is paper-defined.

### ★★ 3DCodeVerse: Exploring 3D Worlds as Code
- **Authors**: Yipeng Gao, Ziyao Zeng, Jinfa Huang, Yijiang Li, Haolin Xiong, Wang Qin, Xinlei Yu, Youheng Yao, Jie Zhang, Kun-Yu Lin, Rong Liu, Yinyuan Zhao, Yajie Zhao, Meiqi Guo, Jiebo Luo, Lei Shu, Yunhao Ge, …
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred* (large multi-institution author list; project page linked).
- **Venue**: arXiv:2610.22341 (15 Oct 2026) — `cs.AI`; `cs.CV`.
- **Link**: https://arxiv.org/abs/2610.22341
- **Abstract and key innovations**: A research ecosystem to let **coding agents create editable, verifiable 3D content at scale**: (1) **3DCodeVerse-2M**, a large curated dataset of **standalone executable 3D code** (each program packaged with source, environment, descriptions, verification records); (2) the **3DCodeVerse Harness**, a **multi-agent DAG** framework that generates/refines 3D content using **execution checks, spatial measurements, and visual feedback** with **no human feedback during generation**; (3) systematic empirical studies establishing baselines. The harness reports a **90% win rate against Claude Design (3D Object)** in pairwise human evaluations (both used by Claude Opus 5.5).
- **Why it matters here**: the **dataset + harness** counterpart to Mallea — executable-world generation as a scalable, verifiable task; another data point that the "worlds as code" lane is industrializing.
- **Caveats**: **fully fresh — 0 hits in wiki**; affiliation not printed; "90% win rate" is from pairwise human eval, single reported comparison.

### ★★ OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling
- **Authors**: Bowei Liu, Xinchen Zhang, Xuhuan Li, Tianlin Zhang, Kaian Jiang, Jingwei Liu, Congyang Zhao, Yifei Qian, Junhong Liu, Zhiheng Li, Yujiu Yang, Yang Cai, Ling Yang
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: **NeurIPS 2026** — also arXiv:2610.22355 (15 Oct 2026) — `cs.CL`.
- **Link**: https://arxiv.org/abs/2610.22355
- **Abstract and key innovations**: Moves beyond **binary (True/False) verifiers** to a verifier that **decomposes complex prompts/environmental rules into fine-grained components** and assigns **pointwise graded scores**, giving a **continuous, more informative critique signal**. Trained with a **decoupled RL** objective (pointwise graded verifier + pairwise paradigm). Highlights that **pairwise verification yields more accurate critiques than pointwise** when ground-truth images exist, and validates on **rule-governed generative world modeling** tasks (**Maze**, **Sudoku**) as well as text-to-image.
- **Why it matters here**: the fresh **verifier-for-world-models** result — "graded, pairwise, rule-aware reward signals" for generative game/world environments, a direct bridge to the wiki's reward-model and self-play lines.
- **Caveats**: **fully fresh — 0 hits in wiki**; Maze/Sudoku (not commercial games); affiliation not printed.

### ★★ GeoState: Learning View-Decoupled Geometry States for 3D World Modeling
- **Authors**: Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
- **Affiliation**: Tongji University; Hong Kong Polytechnic University; Tencent; Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ).
- **Venue**: arXiv:2610.22343 (15 Oct 2026) — `cs.RO`; `cs.AI`, `cs.CV`, `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.22343
- **Abstract and key innovations**: 3D world models that use **geometry-foundation-model (GFM) features** as predictive states suffer because those features are **view-dependent**, entangling dynamics with camera variation. **GeoState** decomposes the state into a **view-independent scene state + camera observation**: a **scene tokenizer** aggregates multi-view GFM features; a **geometry decoder** replays them into images from arbitrary viewpoints; an **autoregressive world model** predicts future **scene states** while **camera motion is modeled separately**. Because the representation is view-decoupled, predicted states can be **decoded under specified cameras** with a consistent, single derived scale (**no per-frame scale alignment**).
- **Why it matters here**: a mechanistic fix for the **view-dependence** problem that limits world-model rollouts — relevant to any generative game world that must render the same scene from a moving camera.
- **Caveats**: **fully fresh — 0 hits in wiki**; robotics (action-conditioned video prediction, visiting embodied datasets), not a game engine.

---

## §4 Procedural Content Generation

> **Lane note — this block has no dedicated PCG paper, but the "generative world" lane has moved into PCG territory.** A targeted title/abstract sweep for *procedural content generation / level generation* over the 866-entry `2610.*` pool returned **no** classic PCG paper for the Fri 10-16 block. The freshest PCG-adjacent work is instead the **executable/rule-governed world** cluster featured in §3 — [`2610.21283`](https://arxiv.org/abs/2610.21283) (**Mallea**), [`2610.22341`](https://arxiv.org/abs/2610.22341) (**3DCodeVerse**), and [`2610.22355`](https://arxiv.org/abs/2610.22355) (**OmniVerifier-C1**) — which generate *playable/editable world content* rather than levels per se. For continuity, the nearest already-documented PCG anchors remain:
> - **Multiverse: Language-Conditioned Multi-Game Level Blending via Shared Representation** — `2603.26782` (19 wiki hits).
> - **High-Dimensional PCG (HDPCG)** — `2602.18943` (17 hits): elevates non-geometric gameplay dimensions (layer, time) to first-class coordinates for controllable level generation.
> - **Playtrace Reconstructive Partitioning** — `2607.12097` (7 hits): domain-independent "cake" level representation over time; Sokoban.
> - **The Procedural Content Generation Benchmark** — `2503.21474` (6 hits): 12 game-content problems with quality/diversity/controllability metrics.

---

## §5 Game Benchmarks & Evaluation Suites

### ★★★ Realtime-Bench: Can Frontier Models Solve Real-time Interactive Problems?
- **Authors**: Jingyu Tang, Xu Yang, Zhehao Zhang, Zheng Wang, Qi Cheng, Haozhe Zhao, Manling Li, Wenxuan Li, Xide Xia, Jiaxin Pei
- **Affiliation**: University of Texas at Austin; The Ohio State University; University of Illinois at Urbana-Champaign; NVIDIA; Northwestern University.
- **Affiliation note**: the LaTeXML author block lists the five institutions above plus "Steadyworks" with an equal-contribution footnote; treat the per-author mapping as *not fully resolved*.
- **Venue**: arXiv:2610.22155 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.22155
- **Abstract and key innovations**: Real-time interaction requires perceiving evolving environments and acting under **temporal constraints**, but existing real-time evaluations focus on conversational quality/streaming perception, leaving **action under strict time pressure** untested. **Realtime-Bench** is a curated suite of **dynamic tasks where delayed actions directly affect success**. Under **Wall Clock** (time advances with actual inference latency) the best success rate is only **44%** and best **Pass^3 only 36%**. It introduces **Paused Clock** (an idealized reference removing serving latency) and **Token Clock** (advances simulated time with generated token count) to **separate serving latency from streaming capability**; findings show higher reasoning effort has **mixed effects under time pressure**.
- **Why it matters here**: an **independent, second** real-time game-agent benchmark in the same block as the 10-16 edition's **RealtimeBench `2610.20665`** (see the open question below). The wall-clock-vs-paused-clock-vs-token-clock decomposition is a cleaner latency taxonomy than the wiki previously had.
- **Caveats**: **fully fresh — 0 hits in wiki** and **distinct from `2610.20665`** (different authors/group); model names as reported.

### ★★★ Grid-Bench: Can LLMs Predict How Discrete Worlds Change?
- **Authors**: Zixiang Xu, Zirui Song, Wanrong Zheng, Chiyu Zhang, Yue Huang, Yuyang Peng, Kexin Zhang, Jinkun Chen, Xiuying Chen, Xiangliang Zhang, Yan Liu, Laurent Itti, Frank Shyu, Xiaoqiang Luo, Sandeep Pandey, et al.
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred* (large multi-institution author list; project site + code + data linked).
- **Venue**: arXiv:2610.22312 (15 Oct 2026) — `cs.CL`. 39 pages.
- **Link**: https://arxiv.org/abs/2610.22312
- **Abstract and key innovations**: **Grid-Bench** is an **executable benchmark** in which **eight families of operations** transform **discrete worlds** represented as **2D, 3D, and 4D grids**. Given an initial grid, explicit rules, and an **event history** as text, the model must predict the **complete final grid**; **reference execution** makes every predicted cell **checkable**, enabling comparison across operations, history lengths, and workloads. Evaluating six LLMs: complete-state accuracy **falls sharply as histories grow**, and models that match on single events **diverge substantially** over sequences; some recover many correct changes "beyond copying the initial state."
- **Why it matters here**: a **checkable world-state-prediction benchmark** for LLMs — the "does the model track a changing discrete world?" probe that complements the wiki's spatial-reasoning and world-model threads, and is closer to *game state tracking* than most agent benchmarks.
- **Caveats**: **fully fresh — 0 hits in wiki**; grid worlds (not game engines); affiliation not printed.

### ★★ "Do You Trust It… or Check It?": Exploring Children's Verification Behaviors in Game-Based Human-AI Collaboration
- **Authors**: Shuning Liu, Yuxin Song, Hanbing Li, Ziyue Wang, Mingying Lan, Fei Lv
- **Affiliation**: Beijing University of Posts and Telecommunications, China; Communication University of China.
- **Venue**: **HCI International 2026 (Late Breaking Work)** — also arXiv:2610.21233 (15 Oct 2026) — `cs.HC`.
- **Link**: https://arxiv.org/abs/2610.21233
- **Abstract and key innovations**: A **game-based human-AI collaboration probe** examining how **children (aged 8–10)** verify AI suggestions inside a **biological knowledge reasoning game**. Compares three **Agent interaction styles** — *partner-like*, *tool-like*, and *dual-state* — and studies **situated verification behaviors** (acceptance, evidence checking, questioning, revision, continued use) rather than treating trust as a static attitude. Preliminary findings: Agent style shapes engagement — partner-like tended to support **direct questioning**, tool-like was associated with **evidence seeking**; children viewed AI as **useful but fallible**.
- **Why it matters here**: a rare **human-subjects, game-mediated** evaluation of AI trust — the "NPC/agent persona shapes the player's behavior" angle, and a design-side complement to the wiki's NPC-intelligence entries.
- **Caveats**: **fully fresh — 0 hits in wiki**; small preliminary study (n small, ages 8–10); "game" is a reasoning task, not a commercial title.

### Also fresh in this block (games-adjacent, not independently featured)
- [`2610.21656`](https://arxiv.org/abs/2610.21656) **Data World: Scaling Data Environments from Scratch** — a multi-agent engine that **synthesizes environments, tasks, and rubrics from explicit mechanisms**, with independent audits checking target recoverability and rubrics that feed **RL rewards** (data-agent "world scaling"; the environment-generation cousin of §3).
- [`2610.22066`](https://arxiv.org/abs/2610.22066) **Prism-1: Position- and Rival-Independent Scoring for System One Models** — scoring that is invariant to option position and to rival presence, for single-forward-pass decision models; relevant to **fair multi-option/competitive decision scoring**.
- [`2610.21439`](https://arxiv.org/abs/2610.21439) **Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment for Multi-Reward RL** — token-level credit assignment across multiple rewards (the reward-shaping/credit-assignment lane).

---

## §6 Industry Game AI & Deployment

> **Lane note.** This block has **no dedicated studio paper** (no Tencent/NetEase/miHoYo/EA/Ubisoft *game* title in-window). Industrial involvement is embedded in the featured set: **NVIDIA** (Realtime-Bench `2610.22155` — §5), **Alibaba (Qwen Business Unit)** (`2610.22316` — §2; Alibaba Token Hub `2610.21492` — §2), **Tencent + Guangdong Lab of AI & Digital Economy** (GeoState `2610.22343` — §3), **PricewaterhouseCoopers** (MetaShare `2610.21887` — §2), and **Amazon Frontier AI & Robotics (FAR)** (`2610.22340` — §7). The strongest *deployment-economics* signal remains **real-time inference pressure** (Realtime-Bench `2610.22155`; the 10-16 edition's RealtimeBench `2610.20665`) plus the 10-16 efficiency mechanism **Velox `2610.22311`** and 10-15 **Game-Creation-Agents `2610.16776`** (Tencent).

---

## §7 Related Techniques — Self-Play, Model-Based RL, Reward Shaping, Imitation & World Models

### ★★ EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity Search
- **Authors**: Hanane Nour Moussa, Doeun Lee, Sachin Kumar
- **Affiliation**: The Ohio State University.
- **Venue**: arXiv:2610.22290 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.22290
- **Abstract and key innovations**: RL post-training (e.g. GRPO) improves accuracy on verifiable tasks but **narrows the set of solutions** the model can produce ("behavior sharpening"). Prior fixes optimize proxies that don't reflect **diversity of correct solutions**. **EliteReplay** pairs **GRPO with an "elite" archive** built by **quality-diversity (QD) search**: before training, the frozen base model collects solutions spanning **distinct approaches**; during training, GRPO is combined with a **replay loss** on this archive, improving accuracy while **preserving more of the base model's solution diversity**.
- **Why it matters here**: **quality-diversity search** is a core open-ended/game-AI technique; here it is transplanted into LLM post-training — the "keep many good playstyles, not just the winning one" idea, directly relevant to the wiki's open-ended-learning and diversity threads.
- **Caveats**: **fully fresh — 0 hits in wiki**; text-to-SQL/verifiable tasks (not games); abstract truncated in listing.

### ★★ Dexterity from Supervised Play (DSP)
- **Authors**: Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma, Ruoshi Liu
- **Affiliation**: Amazon Frontier AI & Robotics (FAR); University of Maryland, College Park.
- **Venue**: arXiv:2610.22340 (15 Oct 2026) — `cs.RO`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.22340
- **Abstract and key innovations**: Learns **dexterous manipulation** by *playing*: a robot learns a **play policy** from **minutes of human play** via behavior cloning, then **deploys it autonomously** to collect **hours of interaction data** to train a **world model**; the play policy then guides **MPC** by proposing candidate action sequences evaluated under the world model, and a **closed-loop goal-conditioned policy is distilled via self-play within the world model**. On real hardware it beats **hindsight behavior cloning by 69.6%** in success rate and matches RL with **490× less interaction data**.
- **Why it matters here**: the fresh **"learn-by-play + world-model planning + imagination self-play"** recipe — the robotics analogue of game-agent play/curriculum learning, and a striking interaction-efficiency claim.
- **Caveats**: **fully fresh — 0 hits in wiki**; robotics (multifingered hand) not games; sim + limited real-robot experiments.

### ★★ Asking Smarter Questions: Targeted Active Preference Learning for Underspecified Rewards
- **Authors**: Helena Merker, Nick Walker, Andreea Bobu
- **Affiliation**: Massachusetts Institute of Technology.
- **Venue**: **CoRL 2026** — also arXiv:2610.22285 (15 Oct 2026) — `cs.RO`; `cs.HC`, `cs.AI`, `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.22285
- **Abstract and key innovations**: Reward learning assumes the human's teaching covers everything that matters; in practice it **over/under-supervises features unevenly**. Instead of asking the human to try again, shift the burden to the robot: the **same information revealing what the robot doesn't know** is used to **direct active preference queries** at the under-specified features, **accompanied by explanations** focusing the human's attention. Simulation: the **informed prior beats standard active preference learning by up to 30.8%** in the low-query regime; a user study shows the prior and explanations **each significantly improve reward recovery and amplify each other**.
- **Why it matters here**: the fresh **reward-elicitation / inverse-RL** result — how much and *where* human feedback is needed; directly relevant to the wiki's inverse-RL and reward-design lanes (§1 `2610.21912` and `2610.20473`).
- **Caveats**: **fully fresh — 0 hits in wiki**; robotics/user-study domain; the IRD/active-learning baselines and query budget are paper-defined.

### ★ Progress Reward Model for Reinforcement Learning via Large Language Models (PRM4RL)
- **Authors**: Xiuhui Zhang, Ning Gao, Xingyu Jiang, Yihui Chen, Yuheng Pan, Mohan Zhang, Yue Deng
- **Affiliation**: Beihang University.
- **Venue**: **NeurIPS 2025** — also arXiv:2610.22056 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.22056
- **Abstract and key innovations**: Traditional RL struggles with long-term, **sparse-reward** tasks. **PRM4RL** integrates **task planning and dense reward**: for high-level planning, a complex task is **decomposed into a series of simple, manageable subtasks** with a **subtask-oriented, fine-grained progress function** to monitor execution; for low-level reward generation, it uses the progress function to construct a **Progress Reward Model (PRM)** providing **theoretically grounded optimality and convergence guarantees**, enabling effective policy optimization without hand-designed dense rewards (in the spirit of potential-based reward shaping).
- **Why it matters here**: the fresh **dense-progress-reward** entry for long-horizon agent tasks — the reward-shaping lane the wiki tracks closely (cf. §1 IRL `2610.21912` and `2610.20473`), with an explicit **LLM-planner + RL-trainer** integration.
- **Caveats**: **fully fresh — 0 hits in wiki**; a **NeurIPS 2025** re-announcement; reported experiments are on **robotics control tasks**, not game environments; exact benchmark suite and numbers summarized from the abstract only.

### Also related and fresh
- [`2610.22084`](https://arxiv.org/abs/2610.22084) **Learning Changes the World and Then What Was Learned has Changed: Training and Deploying Neural Networks in the Control Loop** — a **closed-loop** framing of "train-then-deploy" failure: an agent's own actions change the data distribution it was trained on, so deployment shifts the world and invalidates the learned function; gives a **distribution-shift / non-stationarity** taxonomy for learned controllers.
- [`2610.22336`](https://arxiv.org/abs/2610.22336) **Robust Reinforcement Learning for Dynamic Treatment Regimes under Model and Measurement Uncertainty** — robust contextual-MDP RL under distribution shift and measurement error (healthcare domain; the methodology is game/agent-RL-adjacent).

---

## Cross-references (already on file — not re-featured)
- **10-16 `game-rl-daily` (same block, 22 papers)** — [`2610.22319` Minecraft Gemini-4 team](https://arxiv.org/abs/2610.22319), [`2610.20786` EvolvingBrain](https://arxiv.org/abs/2610.20786), [`2610.21525` CriticaLLM](https://arxiv.org/abs/2610.21525), [`2610.21040` RRI](https://arxiv.org/abs/2610.21040), [`2610.21156` MASP](https://arxiv.org/abs/2610.21156), [`2610.20811` RIGen](https://arxiv.org/abs/2610.20811), [`2610.21910` CoWorld Reasoner](https://arxiv.org/abs/2610.21910), [`2610.22311` Velox](https://arxiv.org/abs/2610.22311), [`2610.21095` OneWM](https://arxiv.org/abs/2610.21095), [`2610.21612` Intrinsic Dynamics WM](https://arxiv.org/abs/2610.21612), [`2610.20665` RealtimeBench + TORSI](https://arxiv.org/abs/2610.20665), [`2610.20693` Orbia](https://arxiv.org/abs/2610.20693), [`2610.21244` System1-Arena](https://arxiv.org/abs/2610.21244), [`2610.22289` env-agnostic coding agents](https://arxiv.org/abs/2610.22289), [`2610.21319` CA-MAMBA](https://arxiv.org/abs/2610.21319), [`2610.20866` SHRED](https://arxiv.org/abs/2610.20866), [`2610.19714` uncertainty self-play](https://arxiv.org/abs/2610.19714), [`2610.21029` SCARCE](https://arxiv.org/abs/2610.21029), [`2610.21711` LLM price competition](https://arxiv.org/abs/2610.21711), [`2610.21912` Learning Rewards in Strategic Games](https://arxiv.org/abs/2610.21912), [`2610.22287` temporal-objective MARL](https://arxiv.org/abs/2610.22287), [`2610.15054` iterated games](https://arxiv.org/abs/2610.15054) — all **1 hit**; featured in [`game-rl-daily` 2026-10-16](../2026-10-16/game-rl-daily.md).
- **10-17 `arxiv-ai-search` games lane** — [`2610.22277` posetal games](https://arxiv.org/abs/2610.22277), [`2610.22322` agent swarms](https://arxiv.org/abs/2610.22322), [`2610.22138` hidden-belief collapse](https://arxiv.org/abs/2610.22138), [`2610.20908` replicable dueling bandits](https://arxiv.org/abs/2610.20908), [`2610.22152` spec gaming gridworld](https://arxiv.org/abs/2610.22152) — 2 hits; featured in [`arxiv-ai-search` 2026-10-17](./arxiv-ai-search.md).
- **SafeAdapt-Poker: Counterfactual Risk Calibration for Budgeted Adaptation under Opponent Shift** `2610.20473` — 4 hits; featured in the 10-15 `arxiv-daily`/`arxiv-ai-search` (game/mechanism slice), **not yet in a `game-rl-daily`**.
- **Why Alternation Speeds Up Counterfactual Regret Minimization?** `2610.21970` — 1 hit; featured in the **2026-10-16 `conference-digest`**.
- **PureTD backgammon** `2608.15146` — 4 hits; **featured in `game-rl-daily` 08-23**.
- **MARL-BattleGrounds** `2610.14883` (3 hits) and **Game-Creation-Agents `2610.16776`** (Tencent, 4 hits) — scheduled 10-15 `game-rl-daily`.
- **SpireBench** `2610.12596` (Slay the Spire long-horizon strategic play) — 2 hits — and **SpeedrunBench** `2610.08076` (video-game speedrunning) — 6 hits — game-benchmark lane, documented in prior digests.

---

## Contradictions / open questions
- **⚠️ NAMING COLLISION — two "Realtime" real-time-agent benchmarks in one block.** [`2610.22155`](https://arxiv.org/abs/2610.22155) **Realtime-Bench** (UT Austin × OSU × UIUC × NVIDIA × Northwestern) and [`2610.20665`](https://arxiv.org/abs/2610.20665) **RealtimeBench + TORSI** (PKU × Samsung, featured in the 10-16 `game-rl-daily`) are **independent, same-block benchmarks** addressing the same failure mode (reasoning latency decides success). Not a contradiction in *findings* — both agree that wall-clock time is a first-class failure mode — but a naming/claim-collision the wiki should track; neither cites the other in its abstract.
- **Real-time (Wall Clock 44% / Pass³ 36%) vs. paused-clock capability.** Realtime-Bench's Wall/Paused/Token clock decomposition sharpens the earlier latency-vs-capability open question (10-16 §contradictions): the same model can be strong when paused and weak when the world advances. This edition adds the *token-clock* axis (temporal awareness independent of serving speed) — the open question of **when reasoning beats reflex in games** remains unresolved.
- **Generalist VLM agents map spatial worlds better than they reason about change.** ACT3D (`2610.21783`) learns to *acquire* visual evidence via outcome-only RL, while Grid-Bench (`2610.22312`) finds LLMs' **complete-state accuracy collapses as event histories grow** — i.e., strong evidence acquisition coexists with weak long-horizon state tracking. Flagged as a tension, not resolved.
- **No contradicting claim** within this edition was identified against existing wiki sources; all 24 featured items are new-to-wiki and single-source.

---

*Generated 2026-10-17 (Saturday) over the fresh Fri 2026-10-16 announcement block. All 24 featured IDs grep-verified 0-hit against `wiki/**/*.md` before writing; the 10-16 and 10-17 sibling editions' game-lane picks are cross-referenced, not repeated. Affiliation recovery: 18/24 from the paper's own LaTeXML `Affiliation:` block; 6 marked "not stated" (never inferred).*
