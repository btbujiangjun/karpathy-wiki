---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-18)"
type: synthesis
created: 2026-10-18
updated: 2026-10-18
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, multi-agent, game-theory, foundation-models, world-models, pcg, benchmarks, npc, imitation-rl, bandits, proceedings, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-18)

> A **seven-lane sweep** (Game RL, Game AI Bot, Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, Related Techniques) run on **Sunday 2026-10-18**, plus a **proceedings pass** (IEEE CoG 2026 results, AIIDE 2026 forthcoming). **Method note up front**: arXiv posts **no weekend announcements** — the newest fully-populated `/new` block is still **Friday, 2026-10-16**, already reported by the [10-16 `game-rl-daily`](../2026-10-16/game-rl-daily.md) (22 papers) and the [10-17 `game-rl-daily`](../2026-10-17/game-rl-daily.md) (24 papers). This edition is therefore a **weekend verification & complement pass, not a re-run**: it extends the date-ranged search **backwards to submissions 09–13 Oct** (the Mon 13 / Tue 14 announcement blocks the sibling editions did not fully drain), re-triages that residue for game-lane relevance, and cross-references the sibling sets instead of repeating them (§0.3). The arXiv **export API stayed unavailable** this run (`https://export.arxiv.org/api/query` → HTTP 429), so metadata came from `/search/advanced` results HTML, `/abs/{id}` and LaTeXML `/html/{id}v1` pages. **26 papers featured in full, all grep-verified 0-hit** against the live `wiki/**/*.md` tree before writing; **19 more logged as "also fresh"** in per-lane bullet lists.
>
> **Three threads run through this pass.**
>
> **① The week's strongest *pure game-theory / equilibrium-learning* papers are the leftovers of the early-week blocks, not the Friday block.** [`2610.19016`](https://arxiv.org/abs/2610.19016) (U Illinois Chicago) extends regret matching to **constant regret + O(T⁻¹) average duality gap with *alternating* updates** — closing the gap between the practical alternating/optimistic CFR variants and the extra-gradient theory; [`2610.14333`](https://arxiv.org/abs/2610.14333) gives **decentralized bandit learning that converges a.s. to the unique Markov perfect equilibrium** in continuous-action general-sum Markov games at O(n⁻¹/²); [`2509.24226`](https://arxiv.org/abs/2509.24226) stabilizes non-cooperative dynamic-game policy gradients with **model-based priors (MA-GPS)**; and [`2610.14150`](https://arxiv.org/abs/2610.14150) is the **second independent smoothed-complexity result this week** for discounted/mean-payoff games (see the ⚠️ note in §Contradictions — the wiki now tracks two groups claiming smoothed-polynomial game solving, complementary results).
>
> **② Hanabi/collaboration is the week's quiet subplot — and one of its papers was retracted.** [`2610.20205`](https://arxiv.org/abs/2610.20205) (Honda Research Institute) finally *measures* what a convention is (the **"convention gap"** in Hanabi) rather than inferring it from score drops, finding humans beat every off-belief-learning level in raw gap but do **no better than level 2** on the conventions both populations share. Meanwhile [`2503.14555`](https://arxiv.org/abs/2503.14555) **A Generalist Hanabi Agent (R3D2)** — the obvious "generalist cooperative-game agent" citation — was **withdrawn this week** because of an implementation bug that "invalidates some of the key claims" (§Contradictions). Treat generalist Hanabi claims as open again.
>
> **③ The PCG and studio lanes are *still* empty — the lane's one fresh classic-PCG paper this whole week is a rhythm-game chart generator.** [`2610.14955`](https://arxiv.org/abs/2610.14955) freezes a **music-transcription model** as the note-onset prior for rhythm-game chart generation (§4). Targeted queries for `atari / nethack / starcraft / chess / npc` and for studio terms (`NetEase / miHoYo / Ubisoft / game studio`) returned **zero in-window hits** (§0.2), so §6 leans on **competition/proceedings news** instead: IEEE CoG 2026 award results (Best Paper on experience-management difficulty, Best Demo on *Descent* computer-aided content generation) and AIIDE 2026 (Belo Horizonte, Nov 9–13) whose papers are not yet public.

---

## §0 Method and Corpus

### 0.1 Coverage
- **Window**: arXiv announcement blocks **Mon 2026-10-13 → Fri 2026-10-16** (no weekend blocks). The Fri 10-16 block is owned by the sibling editions; this run's *incremental* claim is **submissions 09–13 Oct** (announced Mon 13 / Tue 14), i.e. the front half of the week that the daily-edition series had not drained at title/abstract level.
- **Sources**:
  1. Six date-ranged `arxiv.org/search/advanced` queries, `date-date_type=submitted_date`, **from 2026-10-09 to 2026-10-13**, terms: `game`, `self-play`, `multi-agent`, `reinforcement learning`, `world model`, `player` (cross-lists included, `size=200`, ordered by announced date) → **688 unique papers**; **122** pass a game-lane title/abstract sweep; **92** are new-to-wiki before triage (`early_fresh.json`), of which **19** are used here (rest are off-lane: mean-field finance, scheduling games, sports vision, etc.).
  2. The earlier-in-run inventory still standing behind this edition: **21** date-ranged queries over 13–17 Oct → **927 unique** week-window papers (87 game-lane, 61 fresh) and the **1,209-entry Fri 10-16 block** (316 with abstracts, 211 fresh) — see the 10-17 edition for that half.
  3. **Proceedings web pass**: IEEE CoG 2026 accepted-papers/highlights pages, AIIDE 2026 conference site.
- **Filter**: game-lane keyword sweep (`game / self-play / NPC / atari / minecraft / nethack / starcraft / game level / player / open-ended / world model / …`) with a noise filter (finance/medicine/sports/scheduling senses of "game"), then manual triage of printed abstracts, then **freshness gate**, then feature-ranking. **26 featured in full**; **19 additional fresh items** carried as bullets in their lanes.

### 0.2 Sweep and negative results
1. `search/advanced` HTML via `curl` + browser UA (the plain `webfetch` path and the export API are unusable here); `/abs/{id}` pulls at ≥1.5 s delay; LaTeXML `/html/{id}v1` pulls for printed affiliations (10 fresh IDs fetched this run specifically to recover affiliations — `html2/`).
2. **Targeted empty-lane queries (in-window 09–17 Oct)**: `atari`, `nethack`, `starcraft`, `chess`, `npc` → **0 results each**; industry terms `NetEase`, `miHoYo`, `Ubisoft`, `game studio` → **0 results each** (`Electronic Arts` returned physics false positives only). PCG (`procedural content generation` / `level generation`) → **0 fresh in-lane items all week**, consistent with the 10-16 and 10-17 editions' PCG lane notes.
3. **Dedup**: every candidate ID `grep`-tested against the whole `wiki/` tree before featuring (§0.3).

### 0.2.1 Rate limiting and tooling
- **Export API**: `https://export.arxiv.org/api/query?id_list=…` → **HTTP 429 / connection failure** throughout, the same wall as the 10-15/10-16/10-17 runs.
- **Search/abs/html pages**: HTTP 200 via `curl` + browser UA; a 6-query `search/advanced` batch hit the 300 s shell timeout after three queries (large result pages, ~1 MB each) and was resumed in a second batch — a scheduling artifact, not a rate limit.
- **Abstract caveat**: `search/advanced` abstracts are stored with the highlighted term markup, so titles/abstracts containing `game` split oddly (e.g. `The Token  Games`); full `abs/{id}` pages were pulled to correct this for every featured item.

### 0.3 Dedup accounting (featured + notable cross-references)
| arXiv ID | Lane | Venue/subject | In-wiki hits | Status |
|----------|------|---------------|-------------:|--------|
| 2610.19016 (IR-PRM+ alternating regret matching) | Game GT | cs.LG/cs.GT | 0 | **fresh** |
| 2610.14333 (decentralized bandit Markov perfect equilibria) | Game RL | cs.LG/math.OC | 0 | **fresh** |
| 2509.24226 (MA-GPS non-cooperative dynamic games) | Game RL | eess.SY | 0 | **fresh** |
| 2610.18514 (heterogeneous asynchronous multiplayer bandits) | Game RL / bandits | cs.LG | 0 | **fresh** |
| 2509.23026 (multi-objective Markov games, Pareto-Nash) | Game GT / MAS | cs.MA/cs.GT | 0 | **fresh** |
| 2610.15008 (Stackelberg games for preference alignment) | Game GT / alignment | cs.AI/cs.GT | 0 | **fresh** |
| 2610.14150 (smoothed poly-time discounted/mean-payoff games) | Game GT | cs.GT/cs.DS | 0 | **fresh** |
| 2610.15654 (Hive EXPTIME-complete) | Game GT / complexity | cs.CC | 0 | **fresh** |
| 2509.18673 (introspectively envy-free mixed manna) | Game GT | cs.GT | 0 | **fresh** (bullet) |
| 2602.10524 (sequence-form proper equilibria) | Game GT | cs.GT | 0 | **fresh** (bullet) |
| 2504.09006 (structured Stackelberg games) | Game GT / learning | cs.GT/cs.LG | 0 | **fresh** (bullet) |
| 2506.14544 (infinite lexicographic products of positional objectives) | Game GT | cs.GT | 0 | **fresh** (bullet) |
| 2601.08530 (tournament fixing FPT) | Game GT | cs.GT/cs.DS | 0 | **fresh, but merged into 2602.13422** (bullet, ⚠️) |
| 2610.15495 (Rabin games revisited) | Game GT | cs.FL | 0 | **fresh** (bullet) |
| 2606.13093 (EFGs with stochastic action sets) | Game GT | cs.GT | 0 | **fresh** (bullet) |
| 2608.27654 (two-player HJR value decomposition) | Game GT / control | eess.SY | 0 | **fresh** (bullet) |
| 2610.21412 (JevAgentHarness + AgentDecisionBench) | Game AI Bot | cs.AI | 0 | **fresh** |
| 2610.19342 (A2A agent-team failure taxonomy) | Game AI Bot / MAS | cs.MA/cs.AI | 0 | **fresh** |
| 2610.20780 (ARIA runtime repair of MAS) | Game AI Bot | cs.AI/cs.CL | 0 | **fresh** |
| 2610.20205 (quantifying conventions in Hanabi) | Game AI Bot / HAI | cs.HC/cs.AI/cs.MA | 0 | **fresh** |
| 2610.16322 (BehaviorFormer Minecraft behavior clusters) | Game AI Bot | cs.LG/cs.AI/cs.HC | 0 | **fresh**; **IEEE CoG 2026** |
| 2610.21290 (bias control/injection in agent aggregation) | Game AI Bot | cs.AI/cs.CL/cs.MA | 0 | **fresh** |
| 2610.21538 (Agent Status Protocol) | Game AI Bot / infra | cs.AI/cs.MA | 0 | **fresh** (bullet) |
| 2610.22195 (HTN-Orchestrate) | Game AI Bot | cs.AI/cs.CL | 0 | **fresh** (bullet) |
| 2605.17193 (multi-LLM semantic collapse) | Game AI Bot / MAS | cs.MA | 0 | **fresh** (bullet) |
| 2610.20240 (PAWA panoramic multiplayer world model) | Game Fdn | cs.CV/cs.AI | 0 | **fresh** |
| 2610.15429 (SpecWM spectral alignment) | Game Fdn | cs.LG/cs.AI | 0 | **fresh** |
| 2610.15166 (ExeWorldBench) | Game Fdn / benchmarks | cs.CV | 0 | **fresh** |
| 2610.14186 (world model inside a value function) | Game Fdn / interpretability | cs.AI/cs.LG | 0 | **fresh** |
| 2610.19257 (SMART slot memory, long-horizon video) | Game Fdn | cs.CV | 0 | **fresh** (bullet) |
| 2610.14955 (rhythm-game chart generation transfer) | **PCG** | cs.SD | 0 | **fresh** |
| 2607.20064 (PRO-LONG programmatic memory) | Benchmarks / agents | cs.AI | 0 | **fresh**; NetHack + ARC-AGI-3 |
| 2602.17831 (Token Games puzzle duels) | Benchmarks / eval | cs.AI | 0 | **fresh** (bullet) |
| 2610.14158 (Video-Arena) | Benchmarks / world state | cs.CV | 0 | **fresh** (bullet) |
| 2610.14733 (B-Human '26, 11v11 humanoid soccer) | Industry / competition | cs.RO | 0 | **fresh**; RoboCup 2026 LNCS |
| 2610.21448 (V-SHARE advantage-based value learning) | Related / RL theory | cs.LG/cs.AI | 0 | **fresh** |
| 2610.21870 (risk-sensitive offline RL via OCE) | Related / RL theory | cs.LG/cs.AI/math.OC/stat.ML | 0 | **fresh** |
| 2607.13938 (CBF constrained adversarial imitation) | Related / imitation | cs.RO | 0 | **fresh** |
| 2610.22263 (baselines and score centering in PG) | Related / RLVR | cs.LG | 0 | **fresh** |
| 2610.07226 (Minimal Witness RL) | Related / credit assignment | cs.LG/cs.AI/cs.CL/cs.LO | 0 | **fresh** |
| 2610.21336 (attention-head ranking/partitioning for RL fine-tuning) | Related | cs.LG/cs.CL | 0 | **fresh** (bullet) |
| 2608.27906 (environments for open-ended RL) | Related / open-ended | cs.AI | 0 | **fresh** (bullet) |
| 2610.21666 (diffeomorphic hidden-state steering) | Related / imitation | cs.RO | 0 | **fresh** (bullet) |
| 2610.15256 (MARL in the EIP-4844 blob fee market) | Related / applied MARL | cs.MA/cs.GT/q-fin.TR | 0 | **fresh** (bullet) |
| 2605.10064 (MAGE co-evolutionary knowledge graphs) | Related / self-evolution | cs.AI | 0 | **fresh** (bullet) |
| 2503.14555 (Generalist Hanabi Agent, R3D2) | Game RL | cs.MA/cs.AI | 0 | **⚠️ WITHDRAWN 09 Oct 2026** — see §Contradictions |
| 2610.18229 (opponent modeling under partial observability) | Game RL | cs.GT/cs.LG | **7** | cross-ref — featured in `game-rl-daily` 2026-10-15 + siblings |
| 2610.21487 / 2610.22149 (weighted timed games 4-ExpTime / smoothed PI-VI) | Game GT | cs.GT | **9 / 9** | cross-ref — featured 10-17 `game-rl-daily` |
| 2610.20473 (SafeAdapt-Poker) | Game RL | cs.AI/cs.GT | **18** | cross-ref — 10-15 siblings |
| 2610.22319 / 2610.20786 / 2610.20665 (Gemini Minecraft / EvolvingBrain / RealtimeBench) | Bot / Fdn / Benchmarks | — | **11 / 9 / 23** | cross-ref — featured 10-16 `game-rl-daily` |
| 2610.14883 / 2610.16776 (MARL-BattleGrounds / Game-Creation-Agents) | Benchmarks / Industry | cs.LG / cs.AI | **10 / 15** | cross-ref — featured 10-15 |

**Sibling editions on file for this week** (cross-referenced, not re-featured): [`game-rl-daily` 2026-10-16](../2026-10-16/game-rl-daily.md) (22), [2026-10-17](../2026-10-17/game-rl-daily.md) (24), [`arxiv-ai-search` 2026-10-17](../2026-10-17/arxiv-ai-search.md) games lane, [`conference-digest` 2026-10-17](../2026-10-17/conference-digest.md), and the 10-13/10-15 `game-rl-daily` editions.

### 0.4 Affiliations and venues
- **Abs/search pages frequently do not print affiliations.** Institutions are reported only from the paper's own rendered `Affiliation:` author block (LaTeXML) or the rendered author footnote; otherwise **"not stated"** — *never inferred* from surnames or email domains (standing wiki discipline).
- Two affiliations were recovered from the rendered **body footnote** rather than the author block (PAWA's author block failed to compile: raw `\pawaabstract`/`[` placeholders, so the `1]…3]` footnote was used).
- Venues are stated **only where explicit** (IEEE CoG 2026, RoboCup 2026 proceedings, ICML 2026 spotlight, DAI 2026, AAMAS 2027 *submitted*, AIBThings 2026); otherwise `arXiv preprint`. **No result independently replicated.**

### 0.5 Temp artifacts
- Scratch dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/gamerl1018/` (search HTML `e_*.html`, `s_*.html`, `a_*.html`, `abs/`, `html/`, `html2/`, parsed JSON) — deleted after this write-up.

---

## §1 Game RL — Reinforcement Learning, Self-Play, Multi-Agent & Game Theory

### ★★★ IR-PRM+ with Previous-Utility Prediction: Constant Regret and Best-Iterate Convergence
- **Authors**: Michael Sullins, Ian A. Kash
- **Affiliation**: University of Illinois Chicago.
- **Venue**: arXiv:2610.19016 (13 Oct 2026) — `cs.LG`; `cs.GT`.
- **Link**: https://arxiv.org/abs/2610.19016
- **Abstract and key innovations**: Regret matching and **counterfactual regret minimization** are the workhorses of normal-form and extensive-form game solving, but historically lacked the strong convergence guarantees of optimistic/extra-gradient methods. **IREG-PRM+** recently supplied such guarantees — but only for a **simultaneous extra-gradient update**, which is not what practitioners use (optimistic and **alternating** updates usually perform better). This paper introduces **previous-utility prediction**, an analysis that covers both update schemes: for simultaneous *and* alternating IR-PRM+ in finite two-player zero-sum matrix games it recovers **external regret bounded independently of T**, an **O(T⁻¹) average duality gap**, and **O(T⁻¹/²) best-current-iterate convergence**.
- **Why it matters here**: the theory finally catches up with **what CFR implementations actually do** — it is the natural successor question to the wiki's covered *Why Alternation Speeds Up CFR* (`2610.21970`, 9 hits) and to the covered regret-matching line. Alternating-update theory is the missing piece for practical solver guarantees.
- **Caveats**: **fully fresh — 0 hits in wiki**; matrix games (extensive-form extension not claimed in the abstract); affiliation from the LaTeXML author block.

### ★★★ Decentralized Bandit Learning of Markov Perfect Equilibria
- **Authors**: Felix Höfer, H. Mete Soner
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.14333 (9 Oct 2026) — `cs.LG`; `math.OC`. 23 pages, 1 figure.
- **Link**: https://arxiv.org/abs/2610.14333
- **Abstract and key innovations**: Studies **decentralized bandit learning in discounted infinite-horizon, general-sum Markov games with continuous actions**: agents observe the public state but only their **own realized rewards**, and update with **simultaneous perturbation stochastic approximation (SPSA)**. Under **strong monotonicity** of the negative running-reward gradients and a sufficiently small step size, the fully decentralized procedure converges **almost surely to the unique stationary Markov perfect equilibrium**, with an **O(n⁻¹/²) rate**, plus an episodic finite-horizon extension.
- **Why it matters here**: the fresh **equilibrium-learning** result that combines everything real multi-agent training has at once — bandit (reward-only) feedback, decentralization, continuous actions, general-sum — i.e. the theory-side counterpart to independent-learner MARL in games.
- **Caveats**: **fully fresh — 0 hits in wiki**; uniqueness + strong monotonicity assumptions; not deep-RL (stochastic-approximation theory).

### ★★★ Multi-Agent Guided Policy Search for Non-Cooperative Dynamic Games
- **Authors**: Jingqi Li, Gechen Qu, Jason J. Choi, Somayeh Sojoudi, Claire Tomlin
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2509.24226 (29 Sep 2025, v5 last revised 10 Oct 2026) — `eess.SY`. Comment: published by the American Automatic Control Council.
- **Link**: https://arxiv.org/abs/2509.24226
- **Abstract and key innovations**: Multi-agent policy gradients on non-cooperative dynamic games are **unstable and prone to limit cycles**; the usual stabilizers (entropy-based exploration) slow learning and raise variance. This work instead injects **approximate model priors into the reward as regularization**: in LQ games they prove the priors stabilize policy gradients and guarantee **local exponential convergence to an approximate Nash equilibrium**, then extend the idea to infinite-horizon nonlinear games as **MA-GPS**, which builds **short-horizon local LQ approximations from on-policy trajectories** to guide training. Experiments: nonlinear vehicle platooning and a **six-player strategic basketball formation**.
- **Why it matters here**: a *game-physics* MARL result with a convergence proof — the "guide the gradient with a local model of the game" mechanism is directly portable to multi-agent game training where instability, not sample efficiency, is the bottleneck; the basketball-formation demo is one of the few real *sports-tactics* MARL evaluations in this window.
- **Caveats**: **fully fresh — 0 hits in wiki**; local convergence to an *approximate* Nash; v5 with a corrected notation erratum (results unchanged).

### ★★ Approximating Optimal Policies in Heterogeneous Asynchronous Multi-player Bandits
- **Authors**: Sacha Arroues-Paykin, Etienne Boursier, Vianney Perchet
- **Affiliation**: École Polytechnique; INRIA LMO, Université Paris-Saclay; CREST, ENSAE.
- **Venue**: arXiv:2610.18514 (13 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.18514
- **Abstract and key innovations**: Multi-player multi-armed bandits model **decentralized contending agents**; the **asynchronous** variant (players active only a fraction of timesteps) is the realistic one but understudied beyond homogeneous players. This paper first proves the **optimal centralized allocation is NP-hard to compute** for heterogeneous activation probabilities, then shows the natural **greedy algorithm is a polynomial-time 1/e-approximation**, improved when players are processed in decreasing order of activation probability.
- **Why it matters here**: the fresh **competitive multi-agent resource-allocation** theory result — contention, partial availability and heterogeneous players is the abstract structure behind **shared-world multiplayer games and server-side matchmaking/anti-collusion** problems, and it sits next to the wiki's bandit-evaluation threads.
- **Caveats**: **fully fresh — 0 hits in wiki**; bandit (not deep RL) scope; cognitive-radio motivation rather than a game environment.

### ★★ Game-Theoretic Understandings of Multi-Agent Systems with Multiple Objectives
- **Authors**: Zixin Lin, Qianyi Tan, Sihong He, Yue Wang
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2509.23026 (27 Sep 2025, v2 last revised 11 Oct 2026) — `cs.MA`; `cs.GT`.
- **Link**: https://arxiv.org/abs/2509.23026
- **Abstract and key innovations**: Introduces the **Multi-Objective Markov Game (MOMG)** (vector rewards per agent) and adopts the **Pareto-Nash Equilibrium (PNE)** as solution concept: PNEs **always exist** and **coincide with Nash equilibria of the linearly scalarized games with strictly positive weights** — so **standard single-objective Markov-game solvers suffice**. They further define the **Weak Pareto-Nash Equilibrium** (only deviations that strictly improve *all* objectives are excluded) with a gap (WPNG) that is zero exactly at WPNEs and **never exceeds the Nash gap of any linearly scalarized game**, so an approximate scalarized equilibrium is automatically an approximate WPNE.
- **Why it matters here**: the clean reduction the multi-objective MARL lane lacked — "any scalarized solver is already an approximate Pareto-Nash solver" is exactly the kind of result that removes an entire axis of bespoke algorithm design for **agents balancing competing game objectives** (fun vs. difficulty vs. fairness in NPC/policy tuning).
- **Caveats**: **fully fresh — 0 hits in wiki**; preference profile known in the learning setting discussed; not game-environment empirical.

### ★★ Can You Trust Your Preference Models? Stackelberg Games for Alignment
- **Authors**: Riccardo Formenti, Aditya Agrawal, Vikas Garg
- **Affiliation**: ETH Zürich (Department of Computer Science / Department of Mathematics); Aalto University; YaiYai Ltd (author-block affiliation units; per-author mapping not fully resolved).
- **Venue**: arXiv:2610.15008 (10 Oct 2026) — `cs.AI`; `cs.GT`.
- **Link**: https://arxiv.org/abs/2610.15008
- **Abstract and key innovations**: RLHF optimizes against **imperfect evaluators whose errors can be gamed**. The paper trains two policies as a **zero-sum Stackelberg game**: a **Leader** that minimizes and a **Follower** that maximizes **disagreement among an ensemble of preference models** (a proxy for evaluator error, since human labels are unavailable during training), searching for comparisons where the evaluator may **reverse** the true preference — those become candidates for extra supervision. Theory: equilibrium existence for a general class of finite contextual Stackelberg games, uniqueness + closed form under regularization; algorithm **SMIDA** (Stackelberg Mirror Descent-Ascent) with **linear last-iterate convergence** in the tabular case plus a neural policy-gradient analogue.
- **Why it matters here**: a **game-theoretic red-team loop inside alignment training** — the Leader/Follower structure is the same adversarial-curriculum pattern used in game AI (find where the opponent/judge breaks), now formalized with equilibria and convergence rates for preference-model auditing.
- **Caveats**: **fully fresh — 0 hits in wiki**; disagreement is a *proxy* for evaluator error; synthetic-oracle + held-out experiments only, per the abstract.

### ★★ Algorithms with Smoothed Polynomial-Time Complexity for Deterministic Discounted-sum and Mean-payoff Games
- **Authors**: Ali Asadi, Krishnendu Chatterjee, Ruichen Luo
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.14150 (9 Oct 2026) — `cs.GT`; `cs.DS`.
- **Link**: https://arxiv.org/abs/2610.14150
- **Abstract and key innovations**: Deterministic turn-based **discounted-sum and mean-payoff games** are in NP ∩ coNP yet no polynomial algorithm is known, while strategy iteration is remarkably fast in practice — the classic setup for **smoothed complexity**. Prior smoothed-polynomial bounds existed only for **ergodic** games with high-probability guarantees. This paper presents a **new analysis technique** for a variant setting (abstract truncated on the listing; full mechanism not verified beyond the abstract) yielding smoothed-polynomial bounds for these games.
- **Why it matters here**: it is the **second independent smoothed-complexity result for game solving in one week**, alongside Loff & Skomra's SODA 2027 paper `2610.22149` (9 hits, featured 10-17). Two groups converging on "policy/value iteration is polynomial under perturbation" is a genuine signal — tracked as an open question in §Contradictions.
- **Caveats**: **fully fresh — 0 hits in wiki**; deterministic games; smoothed (not worst-case) guarantees; details beyond the printed abstract not verified.

### ★★ Saving the Queen is hard: Hive is EXPTIME-complete
- **Authors**: Francesco Carboni, Daniele Muscillo
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.15654 (11 Oct 2026) — `cs.CC`.
- **Link**: https://arxiv.org/abs/2610.15654
- **Abstract and key innovations**: **Hive** is a boardless two-player game whose pieces *are* the playing surface. The paper proves deciding whether White can force a win in single-Queen **n-Hive** is **EXPTIME-complete**, even with all pieces already placed: hardness by reduction from **unbounded two-player Constraint Logic** (Grasshoppers encode edge orientations, the One Hive rule enforces vertex constraints), upper bound by considering positions **up to translation**. It answers the single-Queen question of Andel and Rin and extends to multi-Queen variants — claimed as the **first use of unbounded two-player Constraint Logic** for an EXPTIME-completeness proof of a natural problem.
- **Why it matters here**: a fresh **complexity classification of a real commercial board game** — the wiki's combinatorial-game-complexity thread gains a natural, previously open case, and the "state is up to translation" trick is reusable for other unbounded-board games.
- **Caveats**: **fully fresh — 0 hits in wiki**; win-decision complexity only (no algorithms); placement-pre-placed variant.

### Also fresh in this lane (not independently featured)
- [`2509.18673`](https://arxiv.org/abs/2509.18673) **Introspectively Envy-Free and Efficient Allocation of Indivisible Mixed Manna** — Barman & Verma show EF1+fPO are incompatible for additive mixed manna, then restore compatibility via a relaxation: allocations that are **fPO and introspectively envy-free up to one item (IEF1)**, where each agent can eliminate envy by reassigning one of its own items (v4, 14 Oct 2026; `cs.GT`; affiliation not stated).
- [`2602.10524`](https://arxiv.org/abs/2602.10524) **Normal-Form Proper Equilibria via the Sequence-Form Representation** — defines *sequence-form proper equilibrium* (strategically equivalent to Myerson's normal-form proper equilibrium) with two differentiable path-following methods, attacking the exponential blow-up of proper-equilibrium computation in extensive-form games (USTC, City University of Hong Kong, Xi'an Jiaotong; v2 15 Oct 2026).
- [`2504.09006`](https://arxiv.org/abs/2504.09006) **Learning in Structured Stackelberg Games** — **ICML 2026 spotlight**: introduces the **Stackelberg-Littlestone dimension**, which tightly characterizes the leader's instance-optimal online regret in Stackelberg games where context predicts the follower's type (security games, AI safety), with matching distributional sample-complexity dimensions (Carnegie Mellon; v6 15 Oct 2026).
- [`2506.14544`](https://arxiv.org/abs/2506.14544) **Infinite lexicographic products of positional objectives** — extends Ohlmann's finite-lexicographic-product positionality preservation to **arbitrary ordinals**, with new descriptive-complexity completeness results (Max-Parity over countable ordinals complete for the difference hierarchy over Σ⁰₂); v4, 15 Oct 2026; affiliation not stated.
- [`2601.08530`](https://arxiv.org/abs/2601.08530) ⚠️ **Tournament Fixing parameterized by favorite in/out-degree** — FPT when parameterized by how few players can beat/are beaten by the designated winner. **Comment on the abs page: "This work has been merged with arXiv:2602.13422. All updates will appear there."** → **cite 2602.13422 instead**; recorded here so the ID is not re-harvested as a fresh finding (USTC / CityU HK / Xi'an Jiaotong per the v2 author block).
- [`2610.15495`](https://arxiv.org/abs/2610.15495) **Rabin Games Revisited** (Di Stasio & Vardi, `cs.FL`) — "excavates" **Rabin's 1972 implicit recursive solver** as an explicit arena-based algorithm built from reachability/Büchi solving, aiming at direct Rabin-game solutions instead of the usual parity-game detour (factorial-in-index dependence is why practice detours).
- [`2606.13093`](https://arxiv.org/abs/2606.13093) **Equilibrium Computation in Extensive-Form Games with Stochastic Action Sets** — actions unavailable due to exogenous stochasticity (EFGSAS): an expansion procedure to an equivalent EFG (exponentially large), but **polynomial-size approximate strategy representations exist under an independence assumption** (affiliation not stated).
- [`2608.27654`](https://arxiv.org/abs/2608.27654) **Exact Decomposition of Value Functions for Two-Player Games in Hamilton-Jacobi Reachability** — a technical note carrying the one-player value-decomposition algebra of HJR **into the two-player setting** under a monotonicity assumption (the safe-control/game-theory bridge; `eess.SY`; affiliation not stated).

---

## §2 Game AI Bot — LLM-Powered Game Agents, NPC Intelligence & Multi-Agent Systems

### ★★★ JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs
- **Authors**: Kunlun Zhu, Tao Feng, Xu Han, Heng Wang, Ling Yang, Xiangru Tang, Jiaxuan You, Heng Ji
- **Affiliation**: Google; Princeton University; University of Illinois Urbana-Champaign (author-block units; per-author mapping not fully resolved).
- **Venue**: arXiv:2610.21412 (15 Oct 2026) — `cs.AI`. Code linked.
- **Link**: https://arxiv.org/abs/2610.21412
- **Abstract and key innovations**: Agent harnesses call a frontier LLM at every step, but most calls are **multiple-choice decisions** (which tool next). **Decision models** (e.g. *Jev*) answer them at a fraction of the cost. The paper asks **how much control can be delegated without losing success**: it builds **AgentDecisionBench** (from isolated questions up to *controlling a running agent*) plus a **DecisionGym** environment, and finds the decision model that is **most accurate on isolated questions solved only 69.5% of agent tasks**, and that delegating without a fitted confidence threshold **lowered success by 19.0 points**. Their fix, **JevAgentHarness**, fits a per-choice confidence threshold on the agent's own trajectories and hands choices back to the LLM below it.
- **Why it matters here**: the sharpest fresh result on **LLM-vs-small-model division of labor inside a game/agent loop** — the "isolated accuracy does not predict in-environment success" finding is exactly the game-agent evaluation trap (a strong static benchmark ≠ a strong player), and the confidence-gated delegation rule is directly reusable for **latency-sensitive real-time game agents** (ties into the wiki's wall-clock/latency thread from the 10-16/10-17 editions).
- **Caveats**: **fully fresh — 0 hits in wiki**; benchmark construction by the same authors as the harness; decision tasks are tool-choice-shaped, not game-playing.

### ★★★ Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States
- **Authors**: Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke, Vaidehi Patil, Jiayu Wang, Srijan Bansal, Trong Huy Nguyen, Dingfeng Jiang, Dongqi Liu, Ruochen Zhao, Wei Lu, Giuseppe Carenini, Mohit Bansal, Silvio Savarese, Shafiq Joty
- **Affiliation**: Salesforce; University of North Carolina; Nanyang Technological University; Singapore University of Technology and Design; University of British Columbia (author-block units; per-author mapping not fully resolved).
- **Venue**: arXiv:2610.19342 (14 Oct 2026, v2 15 Oct 2026) — `cs.MA`; `cs.AI`. Run logs released.
- **Link**: https://arxiv.org/abs/2610.19342
- **Abstract and key innovations**: Studies **agent-to-agent (A2A)** systems where each agent acts for a *different principal* and holds **private state/authority** the other cannot see — cooperative, mixed-motive, or opposed — explicitly breaking the single-orchestrator/shared-workspace assumption of prior failure studies. From **2,500+ recorded runs** across **488 scenarios in eight families** (legal, CRM, security, commerce, …) built from multiple harnesses and models, it derives **A²-Failures: 20 failure modes in four categories** — discovery & delegation, grounding & record consistency, verification, conduct & fidelity — with three findings that hold across harnesses/models.
- **Why it matters here**: **competitive/mixed-motive multi-agent failures are game structure** — opposing principals, hidden information, and exploitation of authority are the abstract form of an adversarial game, making this the most game-theoretic *agent-reliability* taxonomy in the window; it is also a ready-made **NPC/dialogue-adversary evaluation checklist**.
- **Caveats**: **fully fresh — 0 hits in wiki**; scenarios are business-domain, not game titles; taxonomy is observational (no intervention study).

### ★★★ ARIA: Runtime Inspection and Amendment for Multi-Agent Systems
- **Authors**: Bolin Shen, Yushun Dong
- **Affiliation**: Florida State University.
- **Venue**: arXiv:2610.20780 (14 Oct 2026) — `cs.AI`; `cs.CL`.
- **Link**: https://arxiv.org/abs/2610.20780
- **Abstract and key innovations**: In LLM multi-agent systems a **local mistake compounds** as other agents build on it. Diagnosing finished runs, or replaying them to search for fixes, yields **no learned policy for intervening mid-execution**. ARIA turns **execution-verified repairs into supervision**: from **24,000+ successful and failed trajectories** across **4 frameworks, 6 benchmarks, 8 host models** it builds a dataset of **3,953 verified repair pairs** (what went wrong, where to intervene, the fix) and trains a model to **repair live executions** without repeated trial-and-error.
- **Why it matters here**: runtime *intervention policy* is what a game's **director/systems-AI** does — detect a degenerating play state and patch it while the session continues — so this is the agent-harness version of live game balancing; also the largest repair-supervision dataset in the MAS lane this week.
- **Caveats**: **fully fresh — 0 hits in wiki**; repairs verified by execution, not by human judgment of game quality; four frameworks only.

### ★★ What and Where in Identifying and Quantifying Conventions in Humans and AI Agents
- **Authors**: Makoto Fukushima, Tim Puphal
- **Affiliation**: Honda Research Institute Europe; Honda Research Institute Japan.
- **Venue**: arXiv:2610.20205 (14 Oct 2026) — `cs.HC`; `cs.AI`; `cs.MA`. 32 pages.
- **Link**: https://arxiv.org/abs/2610.20205
- **Abstract and key innovations**: Implicit coordination in cooperative games shows up only **indirectly** (swap partners, score drops). In **Hanabi** the failure probability is computable from hints and visible cards, so players who use conventions outperform the no-convention prediction — the margin is the **"convention gap."** Using **off-belief learning's level 1–5 agent hierarchy** (level 1 = convention-free by construction) on a single scale with two independent human corpora: **humans show a larger gap than every agent level**, yet on the conventions *both* populations use, **humans do no better than level 2** — the human advantage concentrates in a specific situation type (the abstract's "concentrated in a situation t…" is cut off; full characterization not verified).
- **Why it matters here**: the first *decomposition* of "humans coordinate better" into **how much convention** and **where it is used** — a direct challenge to blanket human-superiority claims in cooperative-game AI, and a measurement tool for NPC teammates that must **match or exploit a player's conventions**.
- **Caveats**: **fully fresh — 0 hits in wiki**; Hanabi only; abstract truncated in the listing — the "where" half not fully verified.

### ★★ BehaviorFormer: Discovering Behavioral Patterns via Clusterable Next-Token Prediction
- **Authors**: Tobias Schneider, Danial Fahrner, Soren Antebi, Daniel Uedelhoven, Lennard Bodden, Sandra Halscheidt, Rafet Sifa
- **Affiliation**: Fraunhofer IAIS.
- **Venue**: **IEEE Conference on Games 2026** — also arXiv:2610.16322 (12 Oct 2026) — `cs.LG`; `cs.AI`, `cs.HC`.
- **Link**: https://arxiv.org/abs/2610.16322
- **Abstract and key innovations**: Discovering behavioral patterns in **open-ended games** is hard (no objectives, no labels). BehaviorFormer extends a next-token-prediction Transformer with the **DCSS deep-clustering algorithm** so representations become cluster-separated; in a controlled **Minecraft session with 26 players** it discovers **23 distinct behavioral patterns** that generalize across players, grouped into seven interpretable categories: **stationary, roaming, travel, mining, base work, logging, farming**.
- **Why it matters here**: **unsupervised player-behavior segmentation** — the exact primitive needed for adaptive NPC response, dynamic difficulty, and telemetry analytics, and one of the few *validated-on-real-play* behavior-discovery results in the wiki (a CoG-accepted result, so it also anchors §6).
- **Caveats**: **fully fresh — 0 hits in wiki**; 26 players / one game; clusters are descriptive, not causal.

### ★★ Bias Control and Injection for Multi-Agent Aggregation
- **Authors**: Sungjae Lee, Soheil Abbasloo, Jabin Koo, Jungseul Ok
- **Affiliation**: Microsoft Research; POSTECH.
- **Venue**: arXiv:2610.21290 (15 Oct 2026) — `cs.AI`; `cs.CL`, `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.21290
- **Abstract and key innovations**: When LLM agents disagree, aggregation is corrupted by **non-semantic biases** (majority pressure, response-style preferences). The paper shows bias can be **both mitigated and exploited**: *bias control* (presenting one style-normalized reasoning trace per distinct answer) improves initial answer selection, while *bias injection* (placing an agent's initially selected answer in the **minority**) elicits **decision instability usable as a reliability signal**. The resulting test-time aggregation framework needs **no validation data and no prior knowledge of model strengths**, with higher average accuracy and better token efficiency than competing non-oracle aggregation.
- **Why it matters here**: **majority/style bias is the voting-equilibrium problem of multi-agent game AI** — a judge that can be steered by formatting is a weak referee; using induced instability as a *confidence* signal is a neat trick transferable to game-AI panels and NPC-consensus systems.
- **Caveats**: **fully fresh — 0 hits in wiki**; reasoning-QA aggregation domains; injection is used diagnostically, not adversarially.

### Also fresh in this lane (not independently featured)
- [`2610.21538`](https://arxiv.org/abs/2610.21538) **Agent Status Protocol (ASP)** — a lightweight spec for heterogeneous agents to push JSON state events (lifecycle, health, task, floor, governance) over HTTP POST, with SSE fan-out to dashboards and **server-side liveness inference** (missed heartbeats, no-progress detection) because a crashed/compromised agent cannot self-report; reuses A2A task states and floor-control vocabularies (Open Voice Interoperability Initiative; Linux Foundation AI & Data; `cs.AI`/`cs.MA`).
- [`2610.22195`](https://arxiv.org/abs/2610.22195) **HTN-Orchestrate** — two-layer multi-agent orchestration: a Planner holds **subtask hierarchies/dependencies and defers decomposition until prerequisites exist**, local Orchestrators schedule workers over leaves with AND-semantics result propagation, and the network is **rebuilt when it cannot resolve the task**; beats ReAct / Agent Team / DeepSeek Harness on five benchmarks with the same base model (**89.73% on BrowseComp**) (Nanyang Technological University + Apodex; `cs.AI`/`cs.CL`).
- [`2605.17193`](https://arxiv.org/abs/2605.17193) **Multi-LLM Systems Exhibit Robust Semantic Collapse** — interacting multi-LLM systems converge semantically (**semantic collapse**) across model families over **200–1,000 rounds** despite lexical variation; **13 interventions** (decoding, prompts, agent composition, activation engineering, RL) **fail to restore diversity**, with mechanistic evidence pointing at intrinsic autoregressive properties rather than alignment/conformity bias alone (94 pages; v3 14 Oct 2026; affiliation not stated; `cs.MA`).

---

## §3 Game Foundation Models & World Models

### ★★★ PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents
- **Authors**: Siqi Yang, Yimu Wang, Ziqi Cai, Chengxuan Zhu, Shuchen Weng, Erwin Wu, Zhaofei Yu, Kaipeng Zhang, Boxin Shi
- **Affiliation**: Alaya Lab; Peking University; Institute of Science Tokyo (from the paper's rendered author footnote — the LaTeXML author-block affiliation macros failed to compile; equal-contribution and correspondence footnotes printed).
- **Venue**: arXiv:2610.20240 (14 Oct 2026) — `cs.CV`; `cs.AI`. Project page linked. 24 pages.
- **Link**: https://arxiv.org/abs/2610.20240
- **Abstract and key innovations**: A **multiplayer world model** must predict how *other players'* independent actions change a shared world, **including outside the current POV** — POV video only reveals changes after they enter view, while panoramic video records all directions. **No existing Minecraft dataset pairs synchronized POV + panoramic video + actions of interacting players.** PAWA contributes both: a **dataset** pairing each player's POV with **world-stabilized panoramic video** and aligned actions, plus a framework whose **distributed pipeline decouples CPU gameplay capture from GPU rendering**, scales past **64 simultaneous players**, and **re-renders recorded sessions under new observations**; the model jointly forecasts every player's POV and panoramic video.
- **Why it matters here**: the missing **training substrate for multi-agent world models** — "what did my teammates see/do while I wasn't looking" is the core state-prediction problem of shared-world multiplayer games, and the re-rendering trick gives controllable evaluation data. Directly continues the wiki's Minecraft/world-model line (Gemini Minecraft team `2610.22319`, 11 hits).
- **Caveats**: **fully fresh — 0 hits in wiki**; Minecraft only; authors' institution mapping taken from the footnote (author-block affs failed to compile).

### ★★★ World Modeling through Spectral Alignment (SpecWM)
- **Authors**: Holger Molin, William Peng, Marco Bagatella, Randall Balestriero
- **Affiliation**: Brown University; ETH Zürich; Stanford University.
- **Venue**: arXiv:2610.15429 (11 Oct 2026, v2 14 Oct 2026) — `cs.LG`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.15429
- **Abstract and key innovations**: Asks how to tell a world model **what information to preserve**, and answers it in the **spectral representation-learning** register: a **JEPA** framework whose **target similarity kernel** explicitly specifies desired relationships between observations, with the encoder trained to reproduce those relations in embedding geometry. Kernels range from physical-state supervision to a fully **self-supervised temporal kernel** using only within-trajectory ordering. Theory: global optima characterization, conditions for **linear recoverability and nuisance invariance**, and a connection from temporal-kernel similarity to the **behavioral successor measure**. Empirically the kernel choice controls which physical quantities are recoverable, and **temporal spectral alignment lifts CEM planning success**: LeWorldModel → SpecWM on OGBench **Cube 52%→68%**, **Scene 49%→77%**, and a third task **29%→51%**.
- **Why it matters here**: the **"which invariants should a game world model keep?"** design question, with a clean ablation (kernel choice = recoverable physics) and large planning gains — the strongest fresh *world-model training-objective* result in this window.
- **Caveats**: **fully fresh — 0 hits in wiki**; planning gains are CEM-planner-specific; OGBench rather than a game engine.

### ★★ ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling
- **Authors**: Xinge Peng, Zhen Fang, Ruibing Wang, Yongxuan Lv, Haodong Li, Guohui Zhang, Xiaoxiao Ma, Yiting Lu, Lin Chen, Zehui Che, Feng Zhao
- **Affiliation**: University of Science and Technology of China; The Chinese University of Hong Kong (author-block units; per-author mapping not fully resolved).
- **Venue**: arXiv:2610.15166 (10 Oct 2026) — `cs.CV`.
- **Link**: https://arxiv.org/abs/2610.15166
- **Abstract and key innovations**: Coding agents are moving from reproducing **what a world looks like** to constructing **executable worlds that capture how it works** — *executable world modeling* = world understanding (structural/mechanical/causal principles) + executable realization (code whose behavior emerges from physical interaction). Existing benchmarks test physical reasoning, visual fidelity, or behavioral correctness **separately**. ExeWorldBench is claimed as the **first benchmark evaluating both together** through code-based 3D world construction, with three progressively harder tasks beginning at **Mechanism Executability** (realize a single mechanism from visual observation) and **Compositional Executability** (the abstract is cut after this; the third task's name not verified).
- **Why it matters here**: it formalizes the **"game engine as agent output"** evaluation — the direct successor question to the 10-16/10-17 edition's executable-world cluster (Mallea `2610.21283`, 3DCodeVerse `2610.22341`, OmniVerifier-C1 `2610.22355`), now with a benchmark rather than a system.
- **Caveats**: **fully fresh — 0 hits in wiki**; abstract truncated in the listing — third task and headline numbers not verified.

### ★★ Visualizing the World Model in an Agent's Value Function
- **Authors**: Shawheen Naderi, Fatemeh Akherati, Yubei Chen
- **Affiliation**: University of California, Davis.
- **Venue**: arXiv:2610.14186 (9 Oct 2026) — `cs.AI`; `cs.LG`. 20 pages, 15 figures.
- **Link**: https://arxiv.org/abs/2610.14186
- **Abstract and key innovations**: Asks whether **model-free RL actually learns a model anyway**, and probes a **PPO value function in Crafter** with **counterfactual interventions** that hold everything about a state fixed except one targeted change. The value function encodes genuine world knowledge: **rules governing when a diamond is collectible**, effects of **water and food on health**, and **inventory heuristics** — none of which were trained for, only reward was. The paper also discusses safety implications and shortcomings that block "truly advanced machine intelligence."
- **Why it matters here**: an **interpretability result inside a game environment** (Crafter is a wiki-recurring testbed) — "the value function *is* a world model" is the empirical bridge between the model-free and world-model lanes, and Crafter's rule structure makes the decoded knowledge checkable.
- **Caveats**: **fully fresh — 0 hits in wiki**; single environment/model pair (PPO/Crafter); qualitative decoding, no quantitative probe metric in the abstract.

### Also fresh in this lane (not independently featured)
- [`2610.19257`](https://arxiv.org/abs/2610.19257) **Long-horizon Video Generation with Slot Memory Addressed By Region Tokens (SMART)** — bounded **constant-size slot recurrence** whose writes are addressed by the observing camera and reads by the rendering camera, so recall depends on **inter-view geometry rather than recency** (no explicit 3D, no growing cache), with per-read **confidence estimates** conditioning generation (ETH Zurich; Google; `cs.CV`; 23 pages).

---

## §4 Procedural Content Generation

### ★★★ Transfer Learning for Rhythm Game Chart Generation from Music Transcription and Across Games
- **Authors**: Sojeong An, Nathan Pruyne, Chris Donahue, Dasaem Jeong
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.14955 (10 Oct 2026) — `cs.SD`. 5 pages, 2 figures, 3 tables.
- **Link**: https://arxiv.org/abs/2610.14955
- **Abstract and key innovations**: Rhythm-game **charts** (timed action sequences per recording and difficulty) are hand-written; prior auto-generation uses audio encoders but **never targets automatic music transcription (AMT)**, even though most chart times are **note onsets** — exactly what AMT models predict. The paper **freezes a pre-trained AMT encoder** and trains only a linear projection + Transformer decoder on charts. With their **MuScriptor** system this fits human charts **more closely than encoders trained from scratch** and produces **more accurate note types than MERT** (music-pretrained, transcription-untrained). **Joint training across three osu! modes** raises event F1 on the rarest mode **0.492 → 0.506**, while transferring to **Clone Hero** (similar layout) *lowers* it to 0.482 — i.e. cross-game transfer both helps and hurts depending on layout match.
- **Why it matters here**: the **only fresh classic-PCG paper in the entire week** across all seven lanes (see lane note), and it carries the lane's live questions: *which pre-trained priors transfer into content generation*, and *when does cross-game content transfer backfire* (osu! ↑ vs Clone Hero ↓ is a clean, quantified PCG-transfer result).
- **Caveats**: **fully fresh — 0 hits in wiki**; 5-page paper; affiliation not printed; F1 deltas are small in absolute terms.

> **Lane note.** Classic PCG (`procedural content generation` / `level generation`) returns **no other fresh in-window item** — the third consecutive edition with an empty PCG lane apart from this one paper (10-16 and 10-17 had none at all). Anchors for continuity remain the ones the 10-17 edition listed: **Multiverse** `2603.26782` (19 hits), **HDPCG** `2602.18943` (17), **Playtrace Reconstructive Partitioning** `2607.12097` (7), **PCG Benchmark** `2503.21474` (6). The closest fresh neighbors are in §3: PAWA (world content capture), ExeWorldBench (executable world construction), plus §6's CoG Best Demo for computer-aided content generation.

---

## §5 Game Benchmarks & Evaluation Suites

### ★★★ PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning
- **Authors**: Alexis Fox, Junlin Wang, Paul Rosu, Bhuwan Dhingra
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2607.20064 (22 Jul 2026, v3 last revised 12 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2607.20064
- **Abstract and key innovations**: Long-horizon exploration is where LLM agents fail hardest — named concretely on **ARC-AGI-3 and NetHack**, "especially when evaluated without specialized harnesses." Existing context management trades off **retaining more vs. retrieving better**; PRO-LONG breaks the tradeoff using **programmatic memory**: keep a **complete structured interaction log** and write **programs over that log** to load just what is needed, exploiting the same recent progress in coding agents that made programmatic memory viable. Evaluated in long-horizon, exploratory settings.
- **Why it matters here**: **NetHack/ARC-AGI-3 are the wiki's game-agent benchmark anchors**, and the claim that *harness memory design — not model quality —* decides those scores reframes the game-benchmark lane: comparability across harnesses is the confound (echoing the 10-17 edition's "specialized harnesses" caveat, now made into a method).
- **Caveats**: **fully fresh — 0 hits in wiki**; abstract cut before results numbers (headline deltas not verified); no affiliation printed.

### Also fresh in this lane (not independently featured)
- [`2602.17831`](https://arxiv.org/abs/2602.17831) **The Token Games (TTG): Evaluating Language Model Reasoning with Puzzle Duels** — models **challenge each other by creating their own puzzles** (Programming-Puzzles format: find an input making a boolean function return True), 16th-century mathematical-duel style; pairwise duel results → **Elo ratings**, sidestepping both expensive human curation and contamination concerns (Henniger & Poesia; `cs.AI`; affiliation not stated).
- [`2610.14158`](https://arxiv.org/abs/2610.14158) **Video-Arena: A Scalable Agentic Video Benchmark for Spatiotemporal Capability** — turns **competitive game records** into verifiable tests of evolving-world-state understanding: three task categories — **perceiving critical events, interpreting state updates, tracking the resulting states** — with videos and aligned reference labels generated from game records (partially observable real-world state makes annotation otherwise hard; `cs.CV`; affiliation not stated).

---

## §6 Industry Game AI & Deployment, Competitions and Proceedings

### ★★ B-Human '26 — Scalable Team Play up to 11 vs. 11
- **Authors**: Arne Hasselbring, Tim Laue, Thomas Röfer, Philip Reichenberg
- **Affiliation**: Universität Bremen, Fachbereich 3 – Mathematik und Informatik; Deutsches Forschungszentrum für Künstliche Intelligenz (DFKI), Cyber-Physical Systems, Bremen.
- **Venue**: submitted to **"RoboCup 2026: Robot World Cup XXIX"** proceedings (Springer LNCS) — also arXiv:2610.14733 (10 Oct 2026) — `cs.RO`.
- **Link**: https://arxiv.org/abs/2610.14733
- **Abstract and key innovations**: B-Human **won multiple competitions in the Middle Division of the new Humanoid Soccer League in 2026** and, beyond 3v3/5v5, played **demo matches with eleven humanoid robots** — a stress test of tactical flexibility and system robustness. The paper details the transition from the Standard Platform League (robots half the size, under a third the weight) and the **behavior architecture** for 11-player team play, drawing on RoboCup leagues that have run 11 players much longer.
- **Why it matters here**: the window's only **competition-winning embodied game-AI system** paper, and a rare explicit treatment of **scaling team size** — role assignment and tactical structure at 11v11 is the robotics-native version of the multi-agent coordination problems in §2.
- **Caveats**: **fully fresh — 0 hits in wiki**; competition/league paper (architecture description, no new learning method).

### Proceedings & competition news (web pass — not arXiv)
- **IEEE Conference on Games (CoG) 2026** — Madrid, Spain, **1–4 September 2026** (proceedings via IEEE Xplore; accepted-papers/highlights pages harvested this run):
  - **Best Paper Award**: *Categorizing Experience Management Problem Difficulty Using Graph Analysis* — Valentina Genoese-Zerbi, Justus Robertson, Rogelio E. Cardona-Rivera.
  - **Best Paper nominee**: *MAPLE: Multi-State Aggregated Policy Evaluation for AlphaZero in Imperfect-Information Games* — Qian-Rong Li, Hung Guei, I-Chen Wu, Ti-Rong Wu.
  - **Best Demo Award**: ***Descent: Journeys in the Dark* Computer-Aided Content Generation** — Toby Best, Raluca Gaina, Simon Lucas, James Goodman, Jamie Harris — **the PCG recognition point of the week** (§4 lane note).
  - Accepted highlights relevant to this wiki: *Bridging the Generalization Gap in Open-Ended Game Worlds: Multi-Agent LLM Reasoning in Neural MMO 2* (Olca Orakci, Elif Surer); *A Game-Integrated On-Device Gaming Assistant* (Dominik Jeurissen et al.); *Game-Agnostic Value Functions through Automatic JSON Feature Extraction* (Dien Nguyen, Diego Perez Liebana); *PRISM: Promoted Robust Instance-based Spatial Memory for Real-Time Player Behavioral Encoding* (Jerrin Moore); *LURK Werewolf: Evaluating Linguistic Bias in Large Language Models*. Competitions: **Planet Wars RTS AI, GDMC Minecraft Settlement Generation, StarCraft AI, DareFightingICE LLM AI**; special session on *Spatial Intelligence through Games*. CoG 2026 is also the venue for **BehaviorFormer** (featured §2, `2610.16322`).
- **AIIDE 2026** — 22nd AIIDE, **Belo Horizonte, Brazil, 9–13 November 2026**, AAAI Press proceedings (camera-ready deadline 28 Aug 2026), special theme **"New Grounds"**; topic areas explicitly include **RL for Games, NPC AI, PCG, and game agents**. **Papers not yet public** as of this run — flagged for the next harvest.
- **Industry/studio lane**: targeted searches for `NetEase`, `miHoYo`, `Ubisoft`, `game studio` (and `Electronic Arts`, which returned physics false positives) are **in-window empty** — no studio paper this week; industrial involvement remains embedded in the featured set (Honda Research Institute §2, Fraunhofer IAIS §2, Microsoft Research §2, DFKI/Universität Bremen §6, Fraunhofer/ETH/Google/Brown/Stanford in §3).

---

## §7 Related Techniques — Self-Play, Model-Based RL, Reward Shaping, Imitation & World Models

### ★★★ V-SHARE: Provable Convergence Guarantees for Advantage-based Algorithms
- **Authors**: Kintan Saha, Hamed Masoudi, Xinyi Sheng, Dominik Baumann, Joni Pajarinen, Arsenii Mustafin
- **Affiliation**: Aalto University; Indian Institute of Science (author-block units; per-author mapping not fully resolved).
- **Venue**: arXiv:2610.21448 (15 Oct 2026) — `cs.LG`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.21448
- **Abstract and key innovations**: Advantage-based value learning (Q decomposed into state value + action advantages) **shares information across actions** and works in tabular and deep RL, but lacked theory. **V-SHARE** combines cross-action value sharing with an **importance-weighted Bellman-residual correction**, and the paper claims the **first complete theoretical characterization of an advantage-based algorithm**: asymptotic convergence **and** non-asymptotic finite-sample guarantees. It identifies a regime where V-SHARE **mitigates the rare-action bottleneck of asynchronous Q-learning**, and uncovers a **contraction–variance tradeoff** (stronger deterministic contraction ↔ more importance-weighting noise), addressed with **decreasing residual-preconditioning schedules**.
- **Why it matters here**: rare-action bottlenecks are precisely what games with **large action spaces / uncommon skills** suffer, and "share credit across similar actions" is the value-learning analogue of the credit-assignment threads the wiki tracks; the contraction–variance tradeoff gives a principled schedule rather than a tuned constant.
- **Caveats**: **fully fresh — 0 hits in wiki**; guarantees are tabular/regime-scoped per the abstract; deep-RL empirics not verified beyond the abstract.

### ★★★ Provably Efficient Risk-Sensitive Offline Reinforcement Learning via Optimized Certainty Equivalents
- **Authors**: Hanzhen Wang, Boxiang Lyu, Zhongxiang Dai, Siyang Gao, Dake Zhang, Shuang Qiu
- **Affiliation**: institution blocks present in the author footnote — City University of Hong Kong; The Chinese University of Hong Kong, Shenzhen; University of Chicago; Shanghai Jiao Tong University (addresses printed alongside; **per-author mapping not fully resolved**, so listed as present-not-attributed).
- **Venue**: arXiv:2610.21870 (15 Oct 2026) — `cs.LG`; `cs.AI`, `math.OC`, `stat.ML`.
- **Link**: https://arxiv.org/abs/2610.21870
- **Abstract and key innovations**: Risk-sensitive RL matters when **downside outcomes are unacceptable**, yet its **offline theory is underdeveloped**. The paper studies offline risk-sensitive RL under the **optimized certainty equivalent (OCE)** — a general risk-measure class — in two formulations: **dynamic-OCE** (recursive per-step) and **static-OCE** (single applied to cumulative rewards). For tabular settings it gives **pessimistic value-iteration algorithms with tight sublinear suboptimality bounds** that expose how the utility function (risk sensitivity) affects difficulty, plus **minimax lower bounds**, and extensions toward larger state spaces (abstract cut after this).
- **Why it matters here**: **risk-sensitive + offline** is exactly the regime of **game AI trained on logged player/agent data where catastrophic outcomes matter** (fail states, economy breakage, safety), and the OCE generality means the wiki's single risk-sensitivity examples no longer have to stand alone.
- **Caveats**: **fully fresh — 0 hits in wiki**; tabular core; large-state extension details beyond the printed abstract not verified.

### ★★ Discriminative Barrier Functions for Safe Adversarial Imitation Learning from Observation
- **Authors**: Anubhav Vishwakarma, Bhaumik Mehta, Caleb Hsu, Byron Boots, Tyler Han, Karen Leung
- **Affiliation**: University of Washington (author-block unit; other units not printed).
- **Venue**: arXiv:2607.13938 (15 Jul 2026, v2 last revised 14 Oct 2026) — `cs.RO`. 20 pages, 5 figures.
- **Link**: https://arxiv.org/abs/2607.13938
- **Abstract and key innovations**: IRL learns rewards from demonstrations but **relies on unconstrained exploration**, which is unsafe; analytic **control barrier functions (CBFs)** give safety but are hard to design. The paper **restricts reward-function candidacy to the space of CBFs**, yielding safe online control with continuous improvement, and — crucially — enables **data-driven recovery of barrier functions directly from unlabeled expert observations**, robust to unsafe states **absent from the expert data**. Benchmarked against standard IRL in simulated navigation (improved safety), with a study of **planning-based vs policy-based IRL** trade-offs.
- **Why it matters here**: "imitate the expert but **never leave the safe set**" is the requirement for **game characters that copy human play under hard constraints**, and recovering a safety certificate *from the same demonstrations* removes the usual two-demonstration-sources split.
- **Caveats**: **fully fresh — 0 hits in wiki**; simulation navigation domain; safety is CBF-certified, task success follows IRL quality.

### ★★ Baselines and Score Centering in Policy Gradient Estimation
- **Authors**: Shuo Han, Ziqing Hu
- **Affiliation**: University of Illinois Chicago; Perplexity AI.
- **Venue**: arXiv:2610.22263 (15 Oct 2026) — `cs.LG`. 17 pages.
- **Link**: https://arxiv.org/abs/2610.22263
- **Abstract and key innovations**: In RLHF-style training the data-generating policy ≠ trained policy (staleness, train/inference mismatch), so **importance sampling** is used and **regularized** (truncation, masking, clipping). Under regularization the importance-weighted policy gradient **loses invariance to constant reward shifts**. This note shows invariance is recovered by using the **covariance between reward and the importance-weighted score** as the estimand (equal to the policy gradient when the ratio is unregularized), developing the **covariance perspective** for sequence-level and token-level importance sampling — and using it to explain exactly what the **group-mean baseline** and **score centering** each do (both center, but differ).
- **Why it matters here**: the wiki's RLVR/GRPO lane (10-15/10-16 editions) debates baselines and clipping constantly; this is a compact **correctness result**: regularized IS + uncentered rewards = biased objective, fix = covariance formulation. Directly applicable to **any game RL post-training pipeline** using clipped IS.
- **Caveats**: **fully fresh — 0 hits in wiki**; a "note" (17 pp) — proofs scoped to the estimators discussed; no game experiments.

### ★★ Minimal Witness Reinforcement Learning
- **Authors**: T. Y. Tsui, Zihao Ye, Pengxiang Cai, Yanchao Li, Yuqiang Li, Zhehong Ai
- **Affiliation**: not stated on arXiv metadata / LaTeXML author block; *not inferred*.
- **Venue**: arXiv:2610.07226 (5 Oct 2026, v2 last revised 15 Oct 2026) — `cs.LG`; `cs.AI`, `cs.CL`, `cs.LO`.
- **Link**: https://arxiv.org/abs/2610.07226
- **Abstract and key innovations**: Many problems ask for **multiple minimal witnesses** (explanations, mechanisms), yet standard RL returns **one solution or redundant ones**. MWRL formalizes **minimal-witness identification**: take the **union of the sets certified by successful proposals** and **credit each proposal for the coverage the union would lose without it** — a credit-assignment rule derived from the problem definition that unifies minimality and recovery of alternatives from a **single black-box verifier bit**. They derive a **value-iteration planner** recovering the whole witness family and a **policy-gradient method scalable to LLMs**, evaluated across settings (abstract cut before results).
- **Why it matters here**: **many-solutions credit assignment** is the open-ended/game-AI desideratum ("find many distinct ways to win") formalized with a clean estimator — the direct credit-assignment cousin of the wiki's quality-diversity thread (EliteReplay `2610.22290`, 10-17).
- **Caveats**: **fully fresh — 0 hits in wiki**; results beyond the printed abstract not verified; black-box-verifier setting (binary success only).

### Also related and fresh
- [`2610.21336`](https://arxiv.org/abs/2610.21336) **Ranking and Partitioning of Attention Heads for Sparse and Continual RL Fine-tuning** — rank heads by **gradient norm** for sparse RL tuning, and **partition heads across tasks** for continual RL to cut interference; theory links gradient norm to training effectiveness, empirics on math/instruction/coding show high-ranked heads match denser baselines while partitioning improves retention (Tsinghua; University of Hong Kong; University of Washington; Amazon; `cs.LG`/`cs.CL`).
- [`2608.27906`](https://arxiv.org/abs/2608.27906) **Design the Feedback, Not Just the Reward: Environments for Open-Ended Reinforcement Learning** — an RL framework whose **training environment integrates human domain knowledge (rubrics) with model reasoning**: hierarchical rewards distinguish partially-successful open-ended outputs and **diagnosed failures drive token-level weights in GRPO**; instantiated in interactive web-app generation (v3 15 Oct 2026; `cs.AI`; affiliation not stated).
- [`2610.21666`](https://arxiv.org/abs/2610.21666) **Diffeomorphic Hidden-State Steering (DHS)** — test-time robustness for imitation policies **without retraining or extra demos**: learn an **invertible nonlinear map** from expert hidden states (replayed through the frozen policy), attenuate low-expert-variance coordinates more strongly, map back — steering directions then vary by state while every coordinate is retained; improves success under observation noise on four manipulation tasks (single author; affiliation not stated; `cs.RO`).
- [`2610.15256`](https://arxiv.org/abs/2610.15256) **Do Rollups Self-Organize? MARL in the EIP-4844 Blob Fee Market** — a **calibrated multi-agent RL environment** for Ethereum's blob fee market with an endogenous fee rule; independent learners with **no convergence guarantee still settle near the 3-blob target** (3.32 ± 0.01 over five seeds) across a 50× demand range (AIBThings 2026; single author; affiliation not stated; `cs.MA`/`cs.GT`/`q-fin.TR`).
- [`2605.10064`](https://arxiv.org/abs/2605.10064) **MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs** — externalizes self-knowledge into a **four-subgraph co-evolving knowledge graph** (experience subgraph = teacher corrections + learner's own correct traces), updated alongside a task-level search bandit and skill-level routing bandit from one reward stream, for a **frozen weak backbone** at inference (9 Oct 2026; `cs.AI`; affiliation not stated).

---

## Cross-references (already on file — not re-featured)
- **10-17 `game-rl-daily` (same-week sibling, 24 papers)** — `2610.21487` time-bounded weighted timed games (9 hits), `2610.22149` smoothed PI/VI SODA 2027 (9), `2610.21764` Q(γ_H), `2610.21548` constrained-RL-under-POMDP, `2610.21582` bandit transfer, `2610.22252` multi-policy evaluation, `2610.22198` pursuit-evasion CBF, `2610.21746` delegation dilemma, `2610.22316` steering LLM agents, `2610.21887` MetaShare, `2610.21243` RCM, `2610.21492` MetaExp, `2610.21783` ACT3D, `2610.21283` Mallea, `2610.22341` 3DCodeVerse, `2610.22355` OmniVerifier-C1, `2610.22343` GeoState, `2610.22155` Realtime-Bench, `2610.22312` Grid-Bench, `2610.21233` children's verification, `2610.22290` EliteReplay, `2610.22340` DSP, `2610.22285` preference learning, `2610.22056` PRM4RL — featured in [`game-rl-daily` 2026-10-17](../2026-10-17/game-rl-daily.md).
- **10-16 `game-rl-daily` (22 papers)** — `2610.22319` Gemini 4 Minecraft team (11 hits), `2610.20786` EvolvingBrain (9), `2610.20665` RealtimeBench + TORSI (23), `2610.21525` CriticaLLM, `2610.21040` RRI, `2610.21156` MASP, `2610.20811` RIGen, `2610.21910` CoWorld Reasoner, `2610.22311` Velox, `2610.21095` OneWM, `2610.21612` Intrinsic Dynamics WM, `2610.20693` Orbia, `2610.21244` System1-Arena, `2610.21319` CA-MAMBA, `2610.20866` SHRED, `2610.19714`, `2610.21029`, `2610.21711`, `2610.21912`, `2610.22287`, `2610.15054` — featured in [`game-rl-daily` 2026-10-16](../2026-10-16/game-rl-daily.md).
- **10-15 edition & siblings** — **When Does Opponent Modeling Pay Off?** `2610.18229` (7 hits; spatial opponent model fused into dueling DQN, stabilizes training under partial observability, *submitted to AAMAS 2027*) — the opponent-modeling thread this week's §1 sits next to; **SafeAdapt-Poker** `2610.20473` (18 hits); **MARL-BattleGrounds** `2610.14883` (10); **Game-Creation-Agents** `2610.16776` (Tencent, 15); **SpeedrunBench** `2610.08076` (16); **SpireBench** `2610.12596` (5); **PureTD backgammon** `2608.15146`.
- **10-17 `arxiv-ai-search` games lane** — `2610.22277` posetal games, `2610.22322` agent swarms, `2610.22138` hidden-belief collapse, `2610.20908` replicable dueling bandits, `2610.22152` spec-gaming gridworld.
- **Provenance of this edition's early-week sweep**: many early-window papers were already claimed by the 10-13/10-15 `game-rl-daily` editions (e.g. `2610.14883`, `2610.16776`, `2610.17201` Multics, `2610.16450` CivWorldBench) — excluded here by the 0-hit gate rather than by re-reading.

---

## Contradictions / open questions
- **⚠️ RETRACTION — A Generalist Hanabi Agent (R3D2) `2503.14555` is WITHDRAWN.** The abs page (v2, revised 09 Oct 2026 — inside this window) states the paper "**has been withdrawn because we found a bug in R3D2 implementation that invalidates some of the key claims**." Affiliations printed before withdrawal: Mila, Université de Montréal, Polytechnique Montréal, Dalhousie, Chandar Research Lab, IBM Research, Canada CIFAR AI Chair. **Do not cite its generalist/zero-shot Hanabi claims as evidence**; the generalist-cooperative-agent question stays open, which makes the Honda convention-quantification paper (`2610.20205`) the current *measurement* anchor rather than a competitor's benchmark. Recorded here despite 0 wiki hits so the ID is not later ingested as live work.
- **⚠️ MERGED — Tournament Fixing `2601.08530` → `2602.13422`.** All updates will appear in `2602.13422`; cite that ID. (Both 0 hits; harvested as one item to avoid double-counting.)
- **Two independent groups now claim smoothed-polynomial game solving this week.** Loff & Skomra `2610.22149` (SODA 2027; 9 hits; ergodicity assumption dropped, PI *and* VI, any graph) vs. Asadi, Chatterjee & Luo `2610.14150` (fresh; discounted-sum and mean-payoff; new analysis technique). Not a contradiction — the abstracts claim different techniques/scopes — but the wiki should treat **"smoothed complexity of turn-based games" as an emerging two-paper thread**, and verify whether they cover the same algorithm classes once `2610.14150`'s full text is read (beyond-abstract details unverified here).
- **Hanabi: larger convention gap ≠ better conventions.** `2610.20205` finds humans' raw convention gap **exceeds every OBL level 1–5**, yet on the conventions both populations use humans do **no better than level 2** — a partial *reversal* of "humans are conventionally smarter" framing, and in tension with the (now withdrawn) generalist-agent claim that language-reformulated MARL closes the human gap. Flagged as an open measurement question, not resolved.
- **Benchmark-lane asymmetry: game-specific benchmarks are dormant while general agent benchmarks multiply.** In-window searches for `atari/nethack/starcraft/chess/npc` game benchmarks returned **0**, yet NetHack/ARC-AGI-3 reappear as *evaluation contexts* for general methods (PRO-LONG `2607.20064`) and competitive-game records are being repurposed as general world-state benchmarks (Video-Arena `2610.14158`). Whether game-specific benchmarks are being **absorbed into general-purpose suites** is now a recurring pattern worth tracking.
- **No contradicting claim** within this edition was identified against existing wiki sources; all 26 featured items are new-to-wiki and single-source.

---

*Generated 2026-10-18 (Sunday) — no new arXiv announcement block; scope = early-week submissions (09–13 Oct) residue + re-triage + proceedings pass. All 26 featured IDs grep-verified 0-hit against `wiki/**/*.md` before writing; the 10-16/10-17 sibling editions' picks are cross-referenced, not repeated. Affiliation recovery: 16/26 from the paper's own LaTeXML `Affiliation:` block or rendered author footnote; 10 marked "not stated" (never inferred). Venues stated only where explicit.*
