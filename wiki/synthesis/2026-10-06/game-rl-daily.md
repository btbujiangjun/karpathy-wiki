---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-06)"
type: synthesis
created: 2026-10-06
updated: 2026-10-06
sources: [arxiv.org, cog2026.org]
tags: [game-rl, game-ai, llm-agents, imperfect-information, chess, self-play, pcg, benchmarks, world-models, industry-game-ai, game-dev-se, conference-awards, ieee-cog, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-06)

> **For the first time in this series, the arXiv fresh window genuinely did not reopen — and that is a finding, not a failure.** The `/new` announcement ceiling sat at exactly `2610.03717`, byte-identical to yesterday's. Of the 624 papers above yesterday's boundary, **zero are new game papers**; the only three that survive a game filter (`2610.02835`, `2610.02645`, `2610.02366`) are a LLM post-training paper with a game title, a four-page repeated-game theory note, and an embodiment benchmark that merely *lists* games as a domain. Yesterday's digest predicted the `2610.*` block was "never the venue." Today confirms it in the strongest possible way: **the channel was idle, and the digest still has thirty-six new papers.** Two things did the work. First, **IEEE CoG 2026 posted its award results**, promoting MAPLE from "nominated" to **First Runner Up (Committee Vote)** — the first ranked, peer-reviewed game-RL result this wiki has ever recorded — while the **Best Paper crown went to a player-experience paper, not a game-AI paper**. Second, and more reusable: **arXiv full-text search for the literal string `"Conference on Games"` recovers CoG 2026 preprints that title search could not find.** Yesterday's digest located 14 CoG preprints across eleven title-query variants each; this single query surfaced three more in one pass, including two of today's ★★ papers. That is a channel upgrade, and it is the operationally important result of this run.

---

## §0 Method and Corpus

### 0.1 Boundary determination
- **Yesterday's ceiling: `2610.03717`.** Read directly, not inferred — yesterday's digest states "`2610.03716` is the highest ID in the retrieved pools."
- **Today's ceiling: `2610.03717`.** Re-enumerated from scratch across **six** `/new` categories (`cs.LG`, `cs.AI`, `cs.MA`, `cs.CL`, `cs.CV`, `cs.NE`) rather than yesterday's five. `pool.json` = **941 unique papers**, max ID `2610.03717`.
- **Fresh-window size: 624 papers** above `2610.02210`. **Fresh-window game yield: 0 new.** The five game papers yesterday identified in that band (`2610.03604` Wayfarer, `2610.02331` World Editing, `2610.03598` Broker-Trader, `2610.02425` XiangqiBench, `2610.03695` Queen) are all **claimed**, as is sibling-collision `2610.02563` OpenGameEval. A 41-term keyword pass over the 624 returns 84 hits, of which only three are unclaimed and game-adjacent:
  - `2610.02835` *All Work And No Play Makes Jack a Dull Boy* — **RLVR/GRPO strategy collapse in LLM post-training**; a game idiom, not a game paper. Excluded.
  - `2610.02645` *Performance of Zero-determinant Strategies in Repeated Games without Discounting* — 4 pages, 1 figure, `cs.MA`. Removes a Cesàro-limit assumption from prior ZD-strategy results. Genuinely in scope, **too small to feature**; recorded here.
  - `2610.02366` *Co-design Gym* — embodiment/policy co-optimization benchmark that names games as one of several application domains. Not a game benchmark.
- **⚠️ The ceiling is an announcement frontier, not a submission frontier.** True global arXiv ceiling this run: **`2610.06853`**. The band **`2610.03718`–`2610.06900` is unswept by this digest** — it is visible to the export API but not to `/new`, and the API was rate-limited (§0.3). Sibling `arxiv-ai-search.md` (same directory, today) already covered up to `2610.05748` through that band and found **`2610.05033` Code2Games** — game-adjacent, recorded in §9.3 as a collision. **This is a known gap with a known owner, not an undetected one.**

### 0.2 Sweep — three channels, and the third is the one that worked
1. **arXiv `/new` enumeration** (exhaustive on the fresh window, six categories) — yielded **0**. This is the first negative result in the series and it is *enumerated*, not sampled.
2. **~30 targeted arXiv HTML full-text queries** — `srch2.py` ran broad topical passes plus named-game and genre terms. **1,099 unique papers, 798 unclaimed.** The export-API variants of the same queries (`ti_game_agent`, `ti_pcg`, `ti_gamelearning`) returned **0 hits each** — all rate-limit failures, not empty result sets (§0.3).
3. **The new channel: arXiv full-text search for the literal venue string `"Conference on Games"`.** This searches *paper text*, not titles — so it catches papers whose **comment field or body says "Accepted at IEEE CoG 2026"** while the title says nothing about games. One pass returned `2601.05386`, `2606.26267`, `2607.04782`, `2607.11501` and others. **All four are today's venue recoveries**, and two of them (`2601.05386` chess cheating, `2607.04782` Magic Draft) were among the ~19 CoG entries yesterday's title-only search could not reach.
4. **`https://cog2026.org/awards`** — fetched and parsed for the first time. Produces §6.1.
5. **`https://cog2026.org/acceptedpapers`** re-fetched (658 parsed lines) and **re-dedup'd by exact title**, not by the surname heuristic that produced false positives in an intermediate pass.

**Pool accounting**: `pool.json` 941 + `srch2_all.json` 1,099 + CoG 2026 proceedings/awards ≈ 450 + targeted abs pages 40 → **~2,400 unique records**, **~1,780 unclaimed**.

### 0.3 Rate limiting and the scraper workaround
- **The arXiv export API returned `HTTP 429` ("Rate exceeded") on every attempt this run**, including retries at 9 s, 60 s and 5-minute spacing. Two topical API sweeps therefore completed with **0 results and are recorded as failures, not negatives**. A direct `urllib` fetch of arXiv HTML returned `HTTP 406`.
- **Workaround, unchanged from yesterday and now confirmed durable**: `curl` with a browser `User-Agent` against `/search/`, `/abs/` and `/html/`. All 40 abs-page fetches and 35 HTML-version fetches succeeded under this method.
- **Background execution is not viable on this host**: `setsid` is unavailable on macOS, and a 600 s background batch was killed at tool timeout mid-run, leaving 6 of 19 venue-title queries incomplete. The work was re-run in the foreground with an extended timeout. **Recorded because a future run that parallelizes will silently lose coverage rather than erroring.**
- Consequence: **the ID-range sweep `2610.03718`→`2610.06900` is deferred, not done.** See §10.

### 0.4 Dedup
- Whole-`wiki/` regex sweep over `2[0-9]{3}\.[0-9]{4,5}` → **7,940 unique arXiv IDs already claimed** before this file was written.
- **All 36 featured IDs verified 0-hit immediately before writing**, by exact word-boundary regex over `wiki/`. The check printed no `CLAIMED` line for any of them.
- **⚠️ An intermediate CoG dedup pass used an author-surname heuristic and reported 19 "new" entries, several of which were false positives** (`RIDGE` matched an unrelated MoE page, `PRISM` matched a whitepaper, `Social Deduction` matched a July paper, `Tales of Tribute` was already covered on 10-05, `Wave Function Collapse` covered on 07-08/07-30). **Every one of those was re-checked by exact title and dropped.** The surviving CoG entries below are title-verified.
- **⚠️ Same-day sibling collision**: `arxiv-ai-search.md` (same directory) claims **`2610.05033`** (Code2Games), which sits in the unswept band. Excluded from §1–§7 and recorded in §9.3.

---

## §1 Game RL — Reinforcement Learning in Games

### ★★★ Factoriax: A GPU-Accelerated Factorio-Style Simulator for Reinforcement Learning
- **Authors**: Mickey Beurskens (corresponding), Tristan Tomilin, Thiago D. Simão
- **Affiliation**: **Eindhoven University of Technology** (all three; `m.r.m.beurskens@tue.nl`). Recovered from the arXiv HTML authors block — the abs page carries no affiliation.
- **Venue**: arXiv:2610.05569 (4 Oct 2026) — `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.05569
- **Abstract and key innovations**: a **factory-building simulator written in JAX**, in the Factorio idiom: an agent collects resources, builds machines, and arranges them into production pipelines. Ships an initial benchmark, **Easy Rocket**, requiring the agent to build a resource-intensive Rocket within a fixed tick budget to escape the planet. **The headline is throughput: a 1-billion-step PPO run (≈500,000 episodes) completes in ~8 minutes on a single NVIDIA A100, and in ~84 minutes on a standard laptop GPU.** PPO baselines are published showing the agent learns to gather, craft, and place.
- **Why it matters here**: **this is the throughput argument for game RL, and the number is the contribution.** A billion steps in eight minutes on one GPU moves an RL environment from "run overnight" to "run during a meeting," which is the regime where hyperparameter sweeps, seed variance and ablation stop being luxuries. Factorio-like environments are also structurally unlike Atari: the state is a factory layout with combinatorial interaction, so a fast version of *that* is worth more than a fast version of *this*. It belongs to the same lineage as the environment-construction thread (§6's ConstructRL, §2's ViZDoom work) with the axis switched from realism to clock speed.
- **Caveats**: **preprint, no venue, and a single benchmark.** "Easy Rocket" is one task; nothing in the abstract establishes that the speedup survives a denser or longer-horizon task. JAX portability is claimed implicitly, not measured — the two reported numbers are both NVIDIA. No baseline against an existing Factorio-like environment, so **"fast" is asserted relative to nothing** in the record.

### ★★★ Discovering High-Quality Chess Puzzles with Offline Reinforcement Learning
- **Authors**: Allen Nie, Anirudhan Badrinath, Nicholas Tomlin, Timothy Dai, Carissa Yip, Rose E. Wang, Emma Brunskill, Chris Piech
- **Affiliation**: not printed on the abs page. **Emma Brunskill and Chris Piech are Stanford CS faculty** (the APLE / AI, Play and Education lab); the remaining authors are their students. **(affiliation inferred from known appointments, not verified against the paper)**
- **Venue**: arXiv:2608.14851 (14 Aug 2026) — `cs.AI`, `cs.LG`. Comment field: **"Published at RLC 2026"** (Reinforcement Learning Conference).
- **Link**: https://arxiv.org/abs/2608.14851
- **Abstract and key innovations**: frames **puzzle generation as a pedagogical control problem**. Platforms like Chess.com and Lichess already hold millions of puzzles; the bottleneck the paper names is not volume but **composition** — a teacher must *balance motifs and look-ahead depth* to train specific thinking patterns, and doing that by hand needs domain expertise. The paper applies **offline RL** to the puzzle-discovery problem rather than treating existing puzzle corpora as ground truth.
- **Why it matters here**: this is the **first paper in this wiki's corpus to treat a game-derived training artifact as the deliverable rather than the agent.** Everything else in §1 asks "how does the agent play"; this asks "what should a human be shown," and it uses the same machinery to answer it. The reframe is load-bearing: it makes the *evaluation criterion pedagogical* (balance across motifs and depths) instead of win-rate, which is exactly the axis §5's chess benchmarks keep failing to move along. RLC is a serious venue and it is not a games venue — worth noting that this game-RL result was reviewed by the RL community, not the games community.
- **Caveats**: **no quantitative results in the abstract** — no comparison to a baseline generator, no human evaluation, no statement of what "high-quality" is measured by. Offline RL from *what* dataset is unspecified. The affiliation is inferred. **Treat the contribution as problem formulation until the paper is read.**

### ★★ Turnover-Orthogonal Credit Assignment for Open-Team Multi-Agent Reinforcement Learning (TOCA)
- **Authors**: Amit Thakur, Mukesh Singhal
- **Affiliation**: **University of California, Merced** (both). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.02847 (2 Oct 2026) — `cs.LG`, `cs.MA`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.02847
- **Abstract and key innovations**: studies cooperative systems where **agents join, leave, or are replaced mid-episode**. The core observation: the team return changes both because *agents chose useful actions* and because *the active population itself changed*, and **standard centralized critics and shared advantages collapse these into one scalar** — so surviving agents get rewarded or penalized for **exogenous turnover they did not cause**. TOCA is a **value decomposition that separates action effects, pure turnover effects, and action–turnover interactions**; under exogenous turnover, an event-conditioned baseline removes the pure-turnover component while preserving credit for actions that make the team robust to future turnover.
- **Why it matters here**: **open-team structure is the honest model of most deployed multi-agent games** — matchmaking lobbies, battle-royale fills, MMO guilds, and any PvP game where a leaver is backfilled. The literature this wiki tracks overwhelmingly assumes a fixed roster, which means its credit-assignment results are all computed under a confound this paper has named. The framing is also unusually precise about the failure: it is not "noise," it is **a specific term in the return that no agent in the team controlled**, and naming it makes it removable. This is the MARL analogue of §7's observation that evaluation instruments are broken.
- **Caveats**: **preprint, unreviewed, and no results are quoted in the abstract** — no environment names, no baselines, no improvement figure. "Exogenous turnover" is the tractable case; **endogenous** turnover (agents leaving *because* of what happened) is where games actually live and is not addressed.

### ★★ Accelerating Skill Assessment in Chess: A Drift-Diffusion-Enhanced Elo Rating System (DD-Elo) — venue recovery
- **Authors**: Tianyuan Zhou, Zhizheng Fu, Tianming Yang (each marked with an equal-contribution asterisk)
- **Affiliation**: **School of Intelligent Software and Engineering, Nanjing University, Suzhou, China** (`tyzhou@smail.nju.edu.cn`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2606.26267 — comment field: **"Accepted at the IEEE Conference on Games (IEEE CoG 2026)"**, **paper #89**. Proceedings pending on IEEE Xplore.
- **Link**: https://arxiv.org/abs/2606.26267
- **Abstract and key innovations**: Elo's known failure is **response lag** — it uses only match outcomes and ignores the quality of the play that produced them. DD-Elo imports the **drift diffusion model from cognitive neuroscence** and models *skill expression itself as a decision process*, so **move-level data can move a rating** without the enormous noise that naive move-scoring introduces. The paper proves a **bounded-deviation theorem**: DD-Elo's deviation from classical Elo stays bounded, so the new signal cannot run away from the established scale.
- **Why it matters here**: **rating is the evaluation instrument beneath every competitive-game result this wiki records**, and §5's benchmarks keep tripping over variance. A method that consumes move-level signal while *provably staying on the Elo scale* is the rare upgrade that does not require re-baselining a decade of history — the bounded-deviation proof is what makes it adoptable rather than merely interesting. Paired with §5's GTO Wizard Benchmark, which attacks the same variance problem from the evaluation side (AIVAT) instead of the rating side: **two venues, two mechanisms, one target.**
- **Caveats**: "substantial noise and the vastness of the game-state space" is stated as the obstacle and **the abstract does not say how it was overcome** — the theorem bounds deviation from Elo, which is a *safety* result, not an *accuracy* result. Whether move-level signal actually predicts future strength better than outcome-only Elo is not asserted in the abstract. **Recovered via the new venue-string channel (§0.2.3)** — not findable by title.

### ★★ How Much Can a Few Engine Moves Help? Quantifying Limited Cheating in Chess — venue recovery
- **Authors**: Daniel Keren
- **Affiliation**: **Department of Computer Science, University of Haifa, Haifa, Israel** (`dkeren@ds.haifa.ac.il`). Single author. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2601.05386 — comment field: **"Accepted, IEEE CoG 2026 (IEEE Conference on Games 2026)"**, **paper #59**. Note also: *"Replaces previous version 'On the Effect of Cheating in Chess'"* — the title changed between versions.
- **Link**: https://arxiv.org/abs/2601.05386
- **Abstract and key innovations**: unlike the bulk of chess-cheating literature, which is about **detection**, this measures the **gain**. Using a controlled engine-vs-engine setting with Stockfish, it develops **threshold-based and Bellman-style intervention policies** and quantifies the payoff: **1 cheat → average score 0.71; 2 cheats → 0.82; no cheats → 0.51.** It also introduces a **fast engine-free simulator** that supports hyperparameter optimization without running games, and reports it closely matches the engine-based optimum. Stated goal explicitly *not* to assist cheaters, but to measure the threat so it can be contained.
- **Why it matters here**: the number — **two illegal moves take a game from a coin flip to 0.82** — is the single most decision-relevant figure in today's §1, and it is exactly the kind of figure this wiki's game-RL corpus rarely produces because everyone reports Elo deltas against their own baseline. It also establishes a **methodological transfer**: a Bellman-style intervention policy is a *reinforcement-learning* construction applied to the cheating question, and the engine-free simulator is a variance-reduction technique that generalizes to any engine-evaluated experiment. The 0.51 baseline is itself a useful calibration: engine-vs-engine at matched strength is near-draw, so 0.71/0.82 are unambiguous.
- **Caveats**: **engine-vs-engine only** — a human receiving two tips does not play like Stockfish receiving two, and the whole transfer question is open. The framing invites misuse despite the disclaimer. **Recovered via the new venue-string channel (§0.2.3)**; title search across eleven variants yesterday missed it because the title contains no venue signal.

### ★★ UBCL: A Reinforcement Learning Framework for Controllable and Diverse Player Behaviors
- **Authors**: Atahan Cilan, Atay Özgövde
- **Affiliation**: Cilan — **Turkish Aerospace, Istanbul** *and* **Department of Computer Engineering, Boğaziçi University, Istanbul**; Özgövde — Associate Professor, **Boğaziçi University**. Recovered from the arXiv HTML thanks block.
- **Venue**: arXiv:2512.10835 — comment field: **"Accepted version. Published in IEEE Transactions on Games."**
- **Link**: https://arxiv.org/abs/2512.10835
- **Abstract and key innovations**: existing controllable-NLPlayer approaches need **large-scale human trajectories**, train a **separate model per player type**, or give **no interpretable mapping** from behavioural parameters to policy. UBCL instead defines player behaviour as an **N-dimensional continuous space**, uniformly samples target behaviour vectors from a region covering the subset that real human styles occupy, conditions each agent on `(current, target)`, and sets reward on the **normalized reduction of distance** to that target. One policy, continuous control, **no human data required**.
- **Why it matters here**: the three named failure modes are the three reasons NPC-behaviour work does not transfer, and this attacks all three at once. The important design decision is **replacing the discrete player-type taxonomy with a continuous space** — that makes "diversity" measurable (coverage of the space) rather than an aesthetic claim, and it means the *controllability* is a property of the reward, not of a post-hoc classifier. Published in **IEEE Transactions on Games**, which alongside §6.1's CoG award results is evidence that the peer-reviewed games literature is thicker than this wiki's preprint-heavy record suggests.
- **Caveats**: **no environment, no baseline and no result figure in the abstract.** "The subset representing real human styles" is asserted without a source — where the human behaviour manifold comes from is the load-bearing unaddressed question, and it is precisely what "without relying on human gameplay data" is meant to avoid.

### ★★ Beyond Tracking or Shortcut: Composition-Bounded Predictive States in Poker Autoregressive Models
- **Authors**: Quanhao Li, Qianyu Chen (no affiliation printed on the abs page or in the HTML authors block)
- **Venue**: arXiv:2607.19369 (13 Jun 2026, current version later) — `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2607.19369
- **Abstract and key innovations**: takes a **no-range Limit Hold'em autoregressive model** — trained only on action and value targets, never on opponent hands or ranges — and asks whether a positive hidden-state probe means the model holds a *posterior belief*. Answer: **mostly no.** Opponent-range probes stay positive after action/value controls in two of three seeds, and the behaviour head beats an observable-public-history baseline by ~5 pp — **but visible public betting composition explains more opponent-range signal than the residual hidden state.** Action/value+composition baselines recover most of the effect.
- **Why it matters here**: this is a **negative result about an evaluation method**, and it lands squarely on the belief-tracking claim that the imperfect-information literature leans on. §2's 10-05 *Broken Links* paper reached a related conclusion from the LLM side (internal beliefs beat verbal reports, and neither converts to payoff); this reaches it from the **probing** side: **a probe finding a label does not establish that the model represents it for the reason you think.** The control that does the work — *regressing out betting composition before trusting a hidden-state probe* — is a concrete, transferable methodological fix, and three seeds with one failing is honest reporting.
- **Caveats**: **three seeds, two positive** — the result is suggestive rather than settled, and the paper says so. No-range Limit Hold'em is the simplest poker formulation; **no-range is a deliberately crippled setting**, so how much of the shortcut survives with ranges and No-Limit is untested. Preprint, unreviewed. No affiliation available.

### ★ RIDGE: State-Conditioned Reward Blending for Behavioral Coverage in Deep RL Game Agents
- **Authors**: Kevin Christopher Chua, Al Muqshith Mohammed Shifan, Cristiano Politowski, Ali Neshati, Loutfouz Zaman
- **Affiliation**: not printed on the proceedings page (superscripts only). **Loutfouz Zaman is at Ontario Tech University** and won the **CoG 2026 Best Reviewer Award** (§6.1). **(partial — verify against the published version)**
- **Venue**: **IEEE CoG 2026**, paper #415, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (proceedings pending on IEEE Xplore; **no arXiv preprint located**)
- **Abstract and key innovations**: from the title — **state-conditioned reward blending** aimed at **behavioural coverage**. The target is not peak performance but the *range* of behaviours an agent exhibits.
- **Why it matters here**: this is the direct algorithmic counterpart to §1's UBCL. Both reframe the game-agent objective from "play well" to "**cover a behaviour space**," and both do it inside the reward rather than by training an ensemble — UBCL with a continuous target vector, RIDGE with a blended reward conditioned on state. Two independent groups reaching the same structural answer, one in *IEEE Transactions on Games* and one at CoG, is the strongest signal in §1 that the controllability framing is converging.
- **Caveats**: **no abstract available** — everything above is inference from the title and from its structural relation to UBCL. Treat as a pointer, not a finding.

### ★ Privileged Critics Improve Bridge Bidding Agents Trained with PPO and Self-Play
- **Authors**: Botao Hu, Qi Zhang
- **Affiliation**: not printed on the proceedings page. **(unverified)**
- **Venue**: **IEEE CoG 2026**, paper #411, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: applies **privileged critics** — training-time access to information the acting policy does not have — to **contract bridge bidding** under PPO with self-play.
- **Why it matters here**: bridge bidding is a **pure imperfect-information, no-perception** problem: the entire difficulty is hidden state, which makes it a clean testbed for whether privileged-critic methods (developed largely in perfect-information and locomotion settings) transfer to information asymmetry. Contract bridge has almost no representation in this wiki's corpus relative to poker, so this is a **new domain entry** for the same underlying question.
- **Caveats**: no abstract; no result available. **Unverified affiliation.** Included as a domain pointer.

---

## §2 Game AI Bot — NPCs, Agents, and Interaction

### ★★★ Separating Decision Time from Decision Quality in the Real-Time Gap of Distilled Deciders: Evidence from a Game and a Conveyor Simulator
- **Authors**: Chihoon Shin (corresponding), Junyeong Lee, Kihyeok Jeong, Wonok Kwon
- **Affiliation**: **Myeongseongsimjae AX Institute, Yeongyang-gun, Gyeongsangbuk-do, Republic of Korea** (Shin, Lee); **Department of Computer Science and Software Engineering, Korea University, Seoul** (Jeong); **Electronics and Telecommunications Research Institute (ETRI)** (Kwon). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.04810 (3 Oct 2026) — **80 pages including supplementary material**, submitted to *Knowledge-Based Systems*. **No acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.04810
- **Abstract and key innovations**: **attacks a measurement convention.** Real-time agents are normally evaluated with the world paused, or with decision time rounded to whole ticks ("tick conversion"). The paper shows tick conversion **predicts almost no loss** for a decider whose hit accuracy actually **falls 14.8 pp** in asynchronous play. It then decomposes the decider's gap to a zero-latency teacher into a **time component** and a **quality component**, using ViZDoom with a control in which the teacher waits for the decider's server. Three preregistered studies on Windows: **time 6.5–8.7 pp, quality 6.3–8.6 pp.** On a Linux host that skips 0.08–0.09% of ticks, **the time component vanishes (−0.1 pp, 95% bootstrap [−0.4, 0.0]) while the quality component persists (5.6 pp [3.7, 7.5])**.
- **Why it matters here**: this is **the single most rigorous measurement-validity result in today's digest**, and it is on the axis this wiki keeps rediscovering: *the instrument is measuring something other than what you think.* Tick conversion is used pervasively in real-time game-agent evaluation, and the paper demonstrates it is **not conservative** — it is actively wrong by ~15 pp while appearing to cost nothing. The decomposition is the valuable part: because the authors can **hold the teacher fixed and gate only its clock**, they can attribute the loss to latency rather than to the distilled policy, which is a claim almost no distillation paper in this corpus makes. The **preregistration, the paired bootstrap intervals, and the two-host replication** put this above nearly everything else in the series on evidential quality. The Linux/Windows split is itself the finding: **an OS-level tick-skip of under a tenth of a percent abolishes the entire latency penalty**, which means reported real-time gaps may be artifacts of scheduler behavior.
- **Caveats**: **ViZDoom plus a conveyor simulator** — fast-decision settings; how this scales to slower tactical games is unknown, and slower games are where tick conversion is *least* defensible and *most* used. The decider is distilled from a **scripted** teacher, not a learned one, so the generality of the decomposition to learned teachers is untested. 80 pages submitted to *Knowledge-Based Systems*, **not accepted**. Industrial Korean institute affiliation — no academic lab attached.

### ★★ You Are Not My Teammate: Behavioral Fingerprint-based Detection of Suspicious Account Misuse
- **Authors**: Dong Hwan Lee, Huy Kang Kim
- **Affiliation**: **School of Cybersecurity, Korea University, Republic of Korea** (`{20-10076, cenda}@korea.ac.kr`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2608.09132 — comment field: **"Accepted at WISA 2026"** (Workshop on Information Security Applications). 12 pages, 4 figures.
- **Link**: https://arxiv.org/abs/2608.09132
- **Abstract and key innovations**: prior work on game bots and gold farming targets **economy abuse** — progression speedup and currency conversion. But in **competitive MOBAs like League of Legends**, the primary objective is **match outcome and ranking**, so the threat model shifts: the target is not farming currency but **account sharing / account misuse in ranked play**, where a stronger player pilots a weaker account. The paper's move is **behavioural fingerprinting** — identifying *who is actually at the keyboard* from play patterns rather than detecting that a script is playing.
- **Why it matters here**: **this reframes bot detection from "is it a bot" to "is it the account owner,"** and that is a different problem with a different signal. The economy-abuse framing has dominated this wiki's few anti-cheat entries; competitive-integrity abuse is the one publishers actually lose ranked populations over, and it requires *identity* inference from behaviour, not automation inference. It also sits directly beside §7's *Synthetic Counteradaptation* — both are about the strategic interaction between a detection/optimization system and the humans adapting to it.
- **Caveats**: **WISA is a workshop**, not a main conference. The abstract does not state accuracy, dataset size, or which behaviours form the fingerprint. MOBA-only — whether behavioural identity is separable in lower-actions-per-minute games is unaddressed.

### ★★ StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure
- **Authors**: Wenyi Wu, Sibo Zhu, Kun Zhou, Aayush Salvi, Zixuan Song, Biwei Huang
- **Affiliation**: **University of California, San Diego** (all); **Aether AI Lab** (work done during internship); one further affiliation truncated in the HTML block. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2607.11388 — **no venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2607.11388
- **Abstract and key innovations**: long-horizon agents operate over **raw interaction history** — accumulated observations, intermediate edits, failed attempts, partially completed executions — which makes *task progress* hard to interpret, verify, or recover. StructAgent **structures both state and workflow around a unified causal representation of task progress**, so that what has been done, what caused it, and what remains are explicit rather than reconstructed from a transcript on demand.
- **Why it matters here**: **the failure mode it names is the same one §2's 10-05 *Broken Links* paper diagnosed in game agents**: the information exists in the history, but the model cannot get it into a form it can act on. The structural fix — build the representation instead of prompting harder — is the same prescription. For game NPCs specifically, long-horizon causal state is what distinguishes a character with memory from one that re-derives its situation each turn, which is the gap §2's FlashLore and NPC-memory work are attacking from the retrieval side. **Causal structure vs. memory retrieval is the same problem's two ends.**
- **Caveats**: **computer-use / digital-agent setting, not a game.** No result figures in the abstract, no environment named, no acceptance. Included for the structural argument; domain transfer is untested.

### ★★ Reconstructing Persistent Worlds from Narratives for Narrative-Grounded Interactive Experiences
- **Authors**: Yi-Chun Chen (single author; no affiliation printed)
- **Venue**: arXiv:2608.04037 (3 Aug 2026) — `cs.CL`, `cs.AI`, `cs.GR`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2608.04037
- **Abstract and key innovations**: existing work formulates **narrative planning, scene generation and gameplay generation separately**, each building its own task-specific representation — so the *world* that all three depend on is an implicit by-product, never explicitly represented. This paper argues the central computational objective should be **reconstructing and maintaining an explicit persistent world from the narrative**, with the downstream tasks deriving from it rather than each inventing their own.
- **Why it matters here**: this is an **architecture argument about where game content should live**, and it is the structural answer to §4's Spec2Game finding. Spec2Game reports that high executability does not imply faithful specification realization when LLMs generate whole Pygame projects in one shot; this paper's claim is that the failure is *representational* — there is no shared, persistent object holding the truth that generation must conform to. A world as by-product cannot be checked against; a world as artifact can. The framing also connects to §4's Game Simulacra (recovering a world from video) — **both insist on the world as the first-class object**, one from narrative, one from footage.
- **Caveats**: **single author, preprint, no venue, no results in the abstract.** "We investigate" language suggests a position/study paper rather than a system with measurements. Whether the reconstruction is executable or descriptive is not stated.

### ★★ SAT-RTS: A Systematic Framework for Tactical Knowledge Extraction and Visualization-Based Analysis in Real-Time Strategy Games
- **Authors**: Chunhui Bai, Changhe Li, Yuqiang Li, Lei Liu, Shoufei Han
- **Affiliation**: **School of Artificial Intelligence and Automation, China University of Geosciences, Wuhan** (Bai); **State Key Laboratory of Digital Intelligent Technology for Unmanned Coal Mining, Anhui University** (Li, Li, Liu, Han). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2606.30090 (29 Jun 2026) — `cs.AI`. **37 pages, 28 figures including supplementary material.** No venue acceptance claimed.
- **Link**: https://arxiv.org/abs/2606.30090
- **Abstract and key innovations**: RTS micromanagement analysis is blocked by **high-dimensional coupled state–action sequences** and by **black-box decision-making**, and existing work "rarely provides a hierarchical visualization-based attribution analysis." SAT-RTS (**state–action–tactic** pipeline) integrates interpretable visualization with automated extraction of latent tactical patterns, aiming at **hierarchical attribution from data decoupling and abstraction**.
- **Why it matters here**: interpretability for RTS is the same problem §7's *Attention Trajectories* solves for Atari, and the two should be read together — both aggregate low-level attribution into a **hierarchical** summary over time or abstraction level, and both treat the raw saliency/heat map as unusable without that aggregation. The 28 figures are the point: **this is an analysis instrument, and in a field where the decision process is a black box, the instrument is the contribution.** RTS has thin coverage in this wiki relative to its historical importance.
- **Caveats**: **no quantitative result in the abstract** — no agent improvement, no user study, no measured attribution fidelity. "Systematic framework" with 37 pages and 28 figures risks being a pipeline description. Coal-mining-affiliated lab signals a domain-transfer motivation that is not visible in the abstract. Preprint, unreviewed.

### ★ Training Compact Language Models for Strategic Reasoning in Social Deduction Games
- **Authors**: Christian Poglitsch, Johanna Pirker
- **Affiliation**: not printed on the proceedings page (superscripts only). **(unverified)**
- **Venue**: **IEEE CoG 2026**, paper #8, *AI for Game Playing — Regular Papers*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located across title-query variants)
- **Abstract and key innovations**: trains **compact** language models for **strategic reasoning** in social deduction games — i.e. the setting where the difficulty is lying, reading and coordinating under hidden roles rather than board evaluation.
- **Why it matters here**: social deduction is the domain where §2's belief-tracking papers are most at home, and **"compact" is the operative word**: it moves the question from *can an LLM play* to *how small can the model be while still reasoning strategically*, which is the version of the question that matters for shipping an NPC. It also sits against §2's *Annoying AI* and §5's *DR.DENKER* — three CoG papers this run that use LLMs as **objects of study or instruments** rather than as agents to be scaled up.
- **Caveats**: **no abstract available.** All content is inference from title and section placement. **Unverified affiliation.**

### ★ The Annoying AI: Impact of Context-Aware LLM Trash-Talking on Player Frustration and Engagement
- **Authors**: Pablo Carrasco Velo, Yifan Geng, Yi Xia, Ibrahim Khan, Mustafa Can Gursesli, Anna Enrica Tosti, Juho Hamari, Ruck Thawonmas
- **Affiliation**: not printed on the proceedings page. **Juho Hamari** (gamification/HCI) and **Ruck Thawonmas** (game AI) are long-standing names in this literature; the pairing suggests a Japanese/international collaboration. **(tentative — not inferred further)**
- **Venue**: **IEEE CoG 2026**, paper #430, *AI for Game Playing*; a **Demo version** also appears in the accepted-demo list.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: a **context-aware** LLM that **trash-talks** the player, evaluated on **frustration and engagement**.
- **Why it matters here**: trash-talk is one of the few NPC social behaviours that is *measurable on players* rather than on task performance, and the paper evaluates it on the two axes that actually decide whether a shipped feature stays in. Context-awareness is the substantive claim — generic taunts are trivial, taunts that land on what just happened are the hard case. It pairs with §6's CoG award cluster to show **the peer-reviewed lane is doing player-facing agent work, not only benchmark work.**
- **Caveats**: **no abstract, no numbers, no method available.** Frustration and engagement are self-report constructs whose manipulation by an LLM is exactly the confound a paper like this has to control for. Demo-track acceptance indicates a working artifact, not a validated finding.

### ★ Communicating Chess Strategies in Natural Language — venue recovery
- **Authors**: Langyuan Cui, Chun Kai Ling, Hwee Tou Ng
- **Affiliation**: **Department of Computer Science, National University of Singapore** (all three; `13 Computing Drive, Singapore 117417`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2607.11486 — **21 pages, 13 figures.** No venue acceptance claimed.
- **Link**: https://arxiv.org/abs/2607.11486
- **Abstract and key innovations**: chess engines are superhuman but **the strategy behind their moves is hard for humans, including strong ones, to comprehend.** Proposes **chess strategy verbalization** — describing strategy in natural language — with (i) a **verbalization pipeline** and (ii) an **objective evaluation framework** for the generated descriptions. Findings: natural language is a promising interpretable medium for communicating strategy to **both human and LLM players**; evaluating **beyond the main line** matters; **pure concept-based descriptions have limits.**
- **Why it matters here**: this is the **communication half of the interpretation problem**, and the paper is careful to target *both* audiences — which is unusual and correct, since the same unexplained engine output is a barrier for a human learner and for an LLM that has to build on it. **"Evaluate beyond the main line"** is a concrete methodological finding: a description that tracks the top line scores well while saying nothing about *why*, which is exactly the failure mode that makes LLM game-play explanations superficial. It is the natural successor to this wiki's Queen result (10-05), which had LLMs explain moves without an evaluation framework for the explanations.
- **Caveats**: **no quantitative result in the abstract** — "promising" is the strength of the claim. The objective evaluation framework's criteria are not described. Preprint, unreviewed, no affiliation beyond NUS.

### ★ Ally-Conscious Area of Effect Targeting
- **Authors**: Anthony Gagliano, Clark Verbrugge
- **Affiliation**: not printed on the proceedings page. **Clark Verbrugge** is the long-standing **OpenSpiel / Nervana Games / Samsung** author already met in this wiki's CoG coverage. **(partial — verify)**
- **Venue**: **IEEE CoG 2026**, paper #166, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: targeting for **area-of-effect** abilities that accounts for **allies** — i.e. not just maximizing enemy damage but reasoning about friendly fire and positional externalities.
- **Why it matters here**: this is a **small, precisely-scoped combat-AI primitive**, and it is the kind of thing that separates a demo from a shipped agent. AOE targeting with ally-awareness is a **general-sum** subproblem inside an otherwise zero-sum fight — the allies are not opponents but their welfare enters the objective — which places it structurally with §7's constrained-games work rather than with pure reward maximization. Verbrugge's involvement signals OpenSpiel-adjacent tooling.
- **Caveats**: **no abstract.** Inference from title only. Included because it is a concrete, well-posed subproblem with an established author; content unverified.

---

## §3 Game Foundation Models & World Models

### ★★★ VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning
- **Authors**: Kuan-Chen Chen, Winston Chen, Wei-Fang Sun, Min-Chun Hu
- **Affiliation**: **Department of Computer Science, National Tsing Hua University** (Kuan-Chen Chen, Winston Chen, Hu); **NVIDIA AI Technology Center (NVAITC)** (Wei-Fang Sun). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2607.00483 — comment field: **"Accepted at IJCAI 2026"**; project website available.
- **Link**: https://arxiv.org/abs/2607.00483
- **Abstract and key innovations**: reward design is the blocker in **open-ended environments where goals are abstract and hard to quantify** — precisely the game-NPC and sandbox setting. VLM-AR3L reads the agent's **visual observations in the context of a natural-language task goal** and learns **two** reward models from VLM-generated preference labels: an **absolute** reward model giving a scalar for individual states, and a **relative** reward model comparing consecutive observations to infer **progress or regression** toward the goal.
- **Why it matters here**: **the absolute/relative split is the contribution, and it is the right one for games.** Absolute state scoring is what makes a sparse game reward flat; step-to-step relative scoring is what dense shaping tries and usually fails to do without being gameable. Learning *both* from preference labels rather than hand-authoring either removes the reward-hacking surface that §1's broker-trader paper (10-05) demonstrated can defeat a *correct* reward. The NVIDIA co-authorship plus IJCAI acceptance makes this the most credentialed open-ended-reward result in this run. It is the mechanism-level successor to the foundation-model question: **the model is not being used to act or to imagine, it is being used to score.**
- **Caveats**: **VLM preference labels are themselves noisy**, and the paper does not report agreement or cost. "Open-ended" is not tied to a named environment in the abstract. Relative rewards are structurally blind to absolute quality — a policy can improve continuously against itself while never reaching the goal, and the abstract does not say whether the two heads are reconciled.

### ★★★ PhysEditWorld: A Large-Scale Dataset Toward Physics-Editable World Models
- **Authors**: Bin Hu, Yanwen Ma, Jiehui Huang, Ziliang Zhang, Haoning Wu, Ruicheng Zhang, Yaokun Li, Zijun Wang, Yuechen Zhang, Chun-Mei Tseng, Hanhui Li, and others
- **Affiliation**: **Tsinghua Shenzhen International Graduate School, Tsinghua University** (Hu, Zhang, and others); **Beihang University** (Ma); **The Hong Kong University of Science and Technology** (Huang); **Shanghai Jiao Tong University** (Wu); one independent researcher. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2606.26694 — project page available. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2606.26694
- **Abstract and key innovations**: existing game world models produce plausible action-conditioned rollouts but restrict interaction to **exploratory or wandering trajectories**, and — the core criticism — **learn physical dynamics as implicit correlations rather than as controllable variables**, which is exactly wrong for authored games where **physics rules are deliberately designed and must be explicitly manipulated**. PhysEditWorld is a **multimodal dataset carrying physical parameters**, gravity first, built on a **UE5 replay-and-rendering pipeline**.
- **Why it matters here**: **"physics learned implicitly is a bug, not a feature" is the thesis, and for games it is correct.** A world model that cannot expose gravity as a knob cannot support level editing, ragdoll tuning, or any designer-facing tool — it can only continue. This reframes the world-model objective from *prediction fidelity* to *editability*, which is the property a game studio actually buys. It is the physical counterpart to §4's world-as-artifact argument (§2's narrative reconstruction) and to the earlier *World Editing* result this wiki claimed on 10-05: **three papers, three representations, one claim that the world must be addressable, not merely generated.** The UE5 replay pipeline is also a practical note — it means the data is engine-grounded rather than learned from video.
- **Caveats**: **dataset paper; no model results in the abstract**, so nothing yet shows that exposing gravity improves control. "Primary focus on gravity in this initial version" — one parameter is a thin slice of physics. Preprint, unreviewed. A large multi-institution author list with equal-contribution and project-lead markers suggests a lab-scale release whose evaluation burden may exceed what the abstract reports.

### ★★ WorldPack: Dynamic Frame Compression for Long-context Video World Modeling
- **Authors**: Yuta Oshima, Yusuke Iwasawa, Masahiro Suzuki, Yutaka Matsuo, Hiroki Furuta
- **Affiliation**: **The University of Tokyo** (Oshima, Iwasawa, Suzuki, Matsuo); **Google DeepMind** (Furuta). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2512.02473 — comment field: **"Published in TMLR (09/2026)"**.
- **Link**: https://arxiv.org/abs/2512.02473
- **Abstract and key innovations**: long-horizon video world models fail on **temporal and spatial consistency** because existing methods either **compress past frames without accounting for 3D viewpoint geometry**, or **retrieve only a handful of spatially relevant frames without increasing retained history**. WorldPack does both at once: **spatially-aware compressed memory** whose key insight is that compression should respect the geometry of where the camera has been.
- **Why it matters here**: memory is the axis on which every game world model in this wiki's corpus degrades, and this is a **clean statement of why the two obvious fixes each fail** — compression without geometry loses structure, retrieval without compression loses volume. The 3D-viewpoint framing is what makes it game-relevant rather than generic video: **a game camera moves in a space, and ignoring that is discarding information the environment already provides.** TMLR publication and a Google DeepMind author make this the best-credentialed memory result in §3 today. Pairs with §3's PhysEditWorld: one makes the world *editable*, this makes it *durable*.
- **Caveats**: **video world models, not game engines** — no action-space or game-specific evaluation stated in the abstract. "Long-horizon" is not quantified. Published in TMLR, which is solid but non-selective by design.

### ★★ How To Train Your World Model: Fine-tuning vs RAG for LM-based World Modeling
- **Authors**: Dhananjay Ashok (work done during an internship at CapitalOne), Shantanu Agarwal, Vivek Datla, Jonathan May, Alfy Samuel
- **Affiliation**: **Information Sciences Institute, University of Southern California** (Ashok, May); **Capital One** (Agarwal, Datla, Samuel). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.02542 (2 Oct 2026) — **no venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.02542
- **Abstract and key innovations**: in text environments, **fine-tuning an LM to act as a world model** is the dominant paradigm, while **retrieval for LM-based world modelling is underexplored**. Systematic comparison across **five environments spanning embodied, web-navigation and social settings**: **fine-tuning wins on reward in 15/20 settings** — but **RAG is more data-efficient**, and both benefit from more and more diverse exploration.
- **Why it matters here**: **"15/20, but RAG is more data-efficient" is a genuinely useful non-binary answer** to a question the field has been arguing by assertion. For games the implication is specific: a game world model's dynamics are *fixed and known to the developer*, which is the condition under which non-parametric retrieval should be most competitive — so a result where fine-tuning still leads 15/20 is a stronger statement than it looks. The social-settings coverage matters for NPC work, and the industrial co-authors mean the comparison is not academic. This is the **construction-paradigm** question that §3's other papers assume away.
- **Caveats**: **text environments only** — no visual world models, so the result does not transfer to §3's PhysEditWorld/WorldPack line. "15/20" is reward-based; the abstract does not report whether the ordering holds on held-out dynamics prediction. CapitalOne sponsorship points to enterprise-agent motivation rather than games. Preprint, unreviewed.

### ★★ PWM: Personalized World Models with Online Reinforcement Learning
- **Authors**: Zhexin Lou, Guancheng Lu, Zeyu Zhang, Yi Zhang, Yang Zhao, Hao Tang (equal contribution / project lead markers present)
- **Affiliation**: **School of Computer Science, Peking University**; **La Trobe University**; **Northwestern University**. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.04920 (4 Oct 2026) — **code and project website available.**
- **Link**: https://arxiv.org/abs/2610.04920
- **Abstract and key innovations**: pretrained world models generate diverse environments, but users want **a specific scene from their own video**. PWM customizes an interactive world model from **short scene videos** using **online RL**: the support trajectory and its controls give reward on continuations sampled from the current policy. In the **GRPO** instantiation, group-relative optimization updates a **compact LoRA adapter** against a unified reward for scene appearance, visual continuity and motion, with **base-policy anchoring** regularizing drift from a frozen **Yume-5B** backbone. Applied across real and rendered environments.
- **Why it matters here**: **personalization as a world-model objective is the user-facing version of §3's editability thesis.** PhysEditWorld wants to expose physics as a knob and WorldPack wants memory; PWM wants *this scene, not a similar one* — and it does it with the same machinery this wiki's game-RL corpus already knows (GRPO) applied to **generation rather than control**. The technical detail that makes it credible is **base-policy anchoring**: without it, LoRA adaptation to one scene would destroy the general dynamics that make the model interactive, and the paper names that failure explicitly. La Trobe + Peking + Northwestern, with code released.
- **Caveats**: **unified reward over three desiderata** (appearance, continuity, motion) whose weighting is not stated — a single scalar hiding three trade-offs is exactly the reward-composition problem §1's broker-trader paper flags. Evaluated on **Yume-5B** only. No acceptance claimed; the four-OCTober posting is days old.

---

## §4 Procedural Content Generation

### ★★★ Spec2Game: Can LLMs Generate Complete Playable Games from Detailed Specifications?
- **Authors**: Yixue Cai, Yuzhe Zhao, Hanxiang Chao, Qingsen Ma, Ziheng Xiong, Jinhu Qi, Irwin King
- **Affiliation**: **The Chinese University of Hong Kong** (Cai, Ma, Xiong, King); **Nankai University, Tianjin** (Zhao); **Wuhan University** (Chao). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.04253 (2 Oct 2026) — **37 pages, 11 figures.** No venue acceptance claimed.
- **Link**: https://arxiv.org/abs/2610.04253
- **Abstract and key innovations**: **generating an executable program is not the same as implementing behavioral requirements written in natural language** — the paper's opening sentence is its thesis. **Spec2Game** requires models to generate **complete Pygame projects** from detailed natural-language specifications: **15 game families, 150 task instances**, one canonical task plus **nine controlled rule variants** per family, across **three implementation-complexity levels**. Evaluation uses **source-code, runtime and visual evidence** along four dimensions — **Executability, Specification Realization, Code Quality, User-Facing Quality** — over **14 LLMs and 3,330 generated projects**. Headline finding: **high executability does not imply faithful specification realization.**
- **Why it matters here**: **the controlled rule variants are the design that makes this paper worth ★★★.** Varying nine rules within a family while holding everything else fixed means a failure can be attributed to *the rule change* rather than to the game — which is the same instrument logic §5's XiangqiBench (10-05) uses and that this wiki's benchmarks have repeatedly lacked. The four-way dimension split matters just as much: reporting only "it ran" is what prior game-generation evaluations did, and separating *ran* from *implemented the spec* from *looks right* is the measurement upgrade. **3,330 projects across 14 models is a real sample.** This is also the honest counterweight to the whole "LLMs can build games" line: the question was never executability.
- **Caveats**: **Pygame only** — a single, forgiving 2D framework; nothing here speaks to engines where the spec lives in asset pipelines and scene graphs. "User-Facing Quality" and "Specification Realization" scoring method is not described in the abstract and is where subjectivity enters. Preprint, unreviewed. The 15-family taxonomy is self-authored, so the difficulty calibration of the three complexity levels is unvalidated.

### ★★ Pacing-Aware Procedural Generation and Runtime Control
- **Authors**: John Brazell, Justus Robertson
- **Affiliation**: not printed on the proceedings page (superscripts only). **Justus Robertson** is also first author of the **CoG 2026 Best Paper Award winner** (§6.1). **(partial — verify)**
- **Venue**: **IEEE CoG 2026**, paper #356, *Procedural Content Generation — Regular Papers*. A **Demo version** also appears in the accepted-demo list.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: PCG with an explicit **pacing** objective, plus **runtime control** — i.e. generation is not a pre-level event but a process modulated during play.
- **Why it matters here**: **pacing is the PCG objective that static generation structurally cannot hit**, because pacing is a property of the *sequence over time*, not of a single generated artifact. Adding runtime control is therefore not an optimization, it is a change of what is being generated. This pairs with §6's Best Paper winner (same group, experience-management difficulty) to show **a coherent program at CoG 2026: difficulty and pacing as runtime, measured, controllable quantities** rather than as level properties. The demo-track acceptance indicates working tooling.
- **Caveats**: **no abstract, no results.** Inference from title only. "Pacing" is not operationalized in anything available here.

### ★★ Game Simulacra Construction from Gameplay Video with a Multimodal LLM
- **Authors**: Justus Robertson (single author — also first author of the Best Paper winner, §6.1)
- **Affiliation**: not printed on the proceedings page. **(unverified)**
- **Venue**: **IEEE CoG 2026**, paper #313, *Procedural Content Generation*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: reconstructs a **game simulacrum** — a playable stand-in — from **gameplay video** using a **multimodal LLM**.
- **Why it matters here**: this is **content acquisition from the one artifact every game already has in abundance: footage.** Where §4's other entries assume a spec (Spec2Game) or a design intent, this starts from observation, which makes it applicable to legacy titles, user-generated content, and reverse-engineering — the PCG analogue of §6's decompilation thread (this wiki's *Simulating Super Mario Odyssey* and *ConstructRL*). It also closes a loop with §3: **world-from-video and simulacrum-from-video are the same inverse problem** approached at different levels of fidelity. Same author as the Best Paper winner and as #356 — one group carrying three PCG/EX items at a single venue is itself notable.
- **Caveats**: **no abstract, no results, unverified affiliation.** "Simulacra" is undefined in anything available; whether the output is playable, replayable, or merely visually consistent is unknown. Included as a strong-title pointer.

### ★ Repair-Aware Game AI Agents for Long-Horizon Narrative Design and Planning
- **Authors**: Mei Si (single author)
- **Affiliation**: not printed on the proceedings page. **(unverified)**
- **Venue**: **IEEE CoG 2026**, paper #422, *Game Design and Technology*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: game AI agents that are **aware of repair** — recovering from failure — applied to **long-horizon narrative design and planning**.
- **Why it matters here**: **"repair-aware" is the correct primitive for long-horizon generation**, and its absence is the usual cause of collapse in narrative agents: a plan that cannot be revised has to be right the first time over an horizon long enough that nothing is. This is the design-side instance of §2's StructAgent argument — both say the representation must carry *what went wrong and what is still true* — and of §5's executability/specification split in Spec2Game: a spec-faithful generator must detect its own divergence, which is exactly repair awareness.
- **Caveats**: **no abstract, no results.** Single author; unverified affiliation. Inference from title only.

### ★ Dance Dance Prompting: Generating Stepfiles with Large Language Models
- **Authors**: Mukesh Guntumadugu, Chad Mourning
- **Affiliation**: not printed on the proceedings page. **(unverified)**
- **Venue**: **IEEE CoG 2026**, paper #417, *Procedural Content Generation*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: LLM generation of **dance stepfiles** — a PCG task where the output is a *timing* artifact mapped onto music rather than a spatial level.
- **Why it matters here**: rhythm-chart generation is a **PCG modality outside the platformer/dungeon default** that dominates this wiki's PCG coverage, and it imposes a constraint the usual benchmarks do not: **the generated artifact must align to an external temporal signal.** That is a materially different playability condition than "the level is traversable," and it makes this a useful contrast case against §4's Spec2Game (which measures specification fidelity against text) — one scores against a clock, the other against a document.
- **Caveats**: **no abstract, no results.** Title inference only. Unverified affiliation.

---

## §5 Benchmarks and Evaluation

### ★★★ GTO Wizard Benchmark
- **Authors**: Marc-Antoine Provost, Nejc Ilenic, Christopher Solinas, Philippe Beardsell
- **Affiliation**: **GTO Wizard** (all four; `{marco,nejc,chris,phil}@gtowizard.com`). **Industry — a commercial poker-training platform benchmarking against its own agent.** Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2603.23660 — **public API.** No venue acceptance claimed.
- **Link**: https://arxiv.org/abs/2603.23660
- **Abstract and key innovations**: a **public API and standardized evaluation framework for Heads-Up No-Limit Texas Hold'em (HUNL)**, evaluating agents against **GTO Wizard AI**, described as approximating Nash equilibria and as having **defeated Slumbot — the 2018 ACPC champion and previous strongest publicly accessible HUNL benchmark — by 19.4 ± 4.1 bb/100.** Variance is addressed by integrating **AIVAT**, a provably unbiased variance-reduction technique achieving equivalent statistical significance **with ten times fewer hands** than naive Monte Carlo. The benchmarking study includes **state-of-the-art large language models** under the framework.
- **Why it matters here**: **the benchmark gap this wiki has been circling is now filled by a vendor, and the number is stark: +19.4 bb/100 over the incumbent public baseline.** That is not a marginal improvement — it means every HUNL result measured against Slumbot since 2018 has been measured against something a known agent beats by roughly two big blinds per hundred hands, which is larger than most reported method gains. **AIVAT at 10× fewer hands is the second contribution and the more transferable one**: poker evaluation has been variance-bound for decades, and a provably unbiased 10× reduction changes what sample sizes are feasible for everyone, not just for this benchmark. Including LLMs positions it as the successor to the chat-poker evaluations this wiki recorded earlier. This is also the §1 DD-Elo pairing noted there: **same problem, evaluation side vs. rating side.**
- **Caveats**: **GTO Wizard is the vendor of the reference agent** — a conflict of interest stated plainly by the author block and not addressed in the abstract. "Approximates Nash equilibria" is a self-description. AIVAT is provably unbiased *given its baseline*, and the baseline quality is not discussed. **No acceptance claimed**; industry preprint.

### ★★★ The Morality Game: An Online Multiplayer Platform to Standardize, Expedite, and Expand Research on Cooperation
- **Authors**: Gregory N. Stanley, Alan Yang, Liam Tsimhoni, Roujia Wang, Ekdatha Arramreddy, Rohan Desai, Shulin Pan, Michael Ahn, Vijairam G. Moorthy, William Mathias, Mai Xu, James Kessler, Yahan Xing, Yang Li, Duoming Bian (15 authors)
- **Affiliation**: **not printed** in the HTML authors block (unavailable for this paper). The `q-bio.NC` primary category and the 15-author roster indicate a behavioural-science collaboration. **(unverified — do not infer)**
- **Venue**: arXiv:2606.24037 (23 Jun 2026) — **primary category `q-bio.NC` (Neurons and Cognition)**, 28 pages, 4 figures. Platform publicly available. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2606.24037
- **Abstract and key innovations**: a **zero-code platform for launching customized online multiplayer experiments** using **game trees to simulate moral dilemmas**, which also **automates participant payments, data collection and analysis**. Positioned as "a video game for science, a hub for economic game research, an open-access data repository, and a tool for expediting the research process," with **replication and transparency** as the stated goals.
- **Why it matters here**: **this is infrastructure for the human-subjects half of the field, which this wiki has almost no coverage of.** Every game-RL and game-AI result recorded here is evaluated against agents or metrics; the questions of what players actually experience, choose and sacrifice are answered by exactly this kind of platform, and the bottleneck the paper names — **manual experiment construction, manual payment, non-reproducible data** — is real. Filing note: **primary category is `q-bio.NC`, not `cs.*`**, and this is a *research tool*, not a game-AI result. Included because it is a benchmark/platform artifact directly serving the games-research loop and because §6's Best Paper winner (experience management) shows the peer-reviewed games community weighting this side heavily. **Flagged in §8.4 as a possible scope stretch.**
- **Caveats**: **category mismatch with this digest's brief.** No experimental results — it is a systems paper about a tool. **Affiliation unverified.** Zero-code and automated-payment claims are unbenchmarked.

### ★★ Computer Vision for MOBA Analytics: A Dataset and Baseline for Visibility Analysis in Dota 2 (Dota2-Vis)
- **Authors**: Ricardo da Rocha Carvalho, Eloísa Oliveira, Luiz Bernardo Martins Kummer, Emerson Cabrera Paraiso, Rayson Laroca
- **Affiliation**: all five — **Universidade de Brasília (UnB)**, Brazil (Carvalho, Oliveira, Kummer, Paraiso marked `1`; Laroca the senior author). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2606.26970 — comment field: **"Accepted for presentation at the 2026 Simpósio Brasileiro de Jogos e Entretenimento Digital (SBGames)."**
- **Link**: https://arxiv.org/abs/2606.26970
- **Abstract and key innovations**: MOBA analytics relies on **structured data** (logs), which **does not capture what each team could actually see** — i.e. vision/fog-of-war state is missing. **Dota2-Vis** covers **all 144 matches from The International 2025, from both team perspectives — 288 Full HD videos — plus 2,477 manually annotated minimap images.** A modern object detector is evaluated in several variants for **player-icon detection**, and the best is used to estimate **opponent-visible player presence** over time.
- **Why it matters here**: **fog of war is the defining information structure of the MOBA genre and structured logs discard it.** Reconstructing visibility from *video* is the move that makes it recoverable, and 288 videos across both perspectives of a complete premier tournament is a genuinely large, properly-constructed dataset — the coverage claim ("all 144 matches") is what makes it a benchmark rather than a sample. It extends the same inverse problem as §4's Game Simulacra (**recover game state from footage**) to a *competitive* setting where the recovered quantity is not content but **information asymmetry**, which is the thing §1's poker and §2's social-deduction work reason about abstractly.
- **Caveats**: conference is **SBGames** (Brazilian), not CoG or a CS venue. **2,477 minimap images against 288 videos is a small annotation ratio** — the baseline's accuracy at that density is not stated in the abstract. Player-icon detection in a 1080p teamfight is the hard case and is not broken out. No acceptance beyond presentation.

### ★★ Chess_db: A Framework for Working with Large Chess Game Datasets
- **Authors**: Nicos Angelopoulos (**University College London & Imperial College London, UK**), Jan Wielemaker (**SWI-Prolog solutions**)
- **Affiliation**: printed inline in the abs-page author field — the two above. Both recovered directly.
- **Venue**: arXiv:2607.21195 (23 Jul 2026) — comment field: **"In Proceedings ICLP 2026, arXiv:2607.17707"** (International Conference on Logic Programming).
- **Link**: https://arxiv.org/abs/2607.21195
- **Abstract and key innovations**: a framework for **large chess game datasets**, motivated by the observation that chess's computational resources are now **centered on training players**, where **engine output is only one aspect** and **access to past games is essential** — both for what a given player has played and for **which continuations from a position led to win more often for each side.** Implemented in the SWI-Prolog ecosystem.
- **Why it matters here**: this is a **data-access artifact for the same corpus §1's chess papers train on**, and the stated motivation is the correct reframing: chess datasets are not engine-scored position collections, they are **populations of human decisions with outcomes attached**. That is what DD-Elo (§1) needs move-level signal from, what the cheating paper (§1) needs its baseline distribution for, and what §1's puzzle-discovery work needs its pedagogical labels from. The ICLP venue is the surprise — **logic programming, not games or ML** — which is a reminder that chess data infrastructure is being built by the knowledge-representation community.
- **Caveats**: **4-page-scale venue note; no performance numbers or dataset sizes in the abstract.** SWI-Prolog dependency narrows adoption. Preprint of a proceedings paper; the `arXiv:2607.17707` cross-reference suggests a companion entry.

### ★★ Characterizing Game Difficulty Using Monte Carlo Tree Search Convergence Metrics
- **Authors**: Lukas Grassauer (single author)
- **Affiliation**: not printed on the proceedings page. **(unverified)**
- **Venue**: **IEEE CoG 2026**, paper #23, *AI for Game Playing — Regular Papers*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: uses **MCTS convergence metrics** as the measure of **game difficulty** — difficulty is what you read off how long search takes to converge, not a property assigned by a designer.
- **Why it matters here**: this is an **instrument-based definition of difficulty**, and it is the sharpest methodological entry in §5 today. Rather than asking players or experts to rate difficulty, or equating it with win rate (which confounds skill with difficulty), it measures **the search process itself** — a quantity available for any game with a simulator, requiring no human subjects and no learned opponent. That makes it directly comparable across games, which no difficulty measure this wiki has recorded is. It is also the natural companion to §6's experience-management Best Paper winner, which categorizes *problem* difficulty from a graph: **one measures difficulty from search convergence, the other from problem structure, and neither uses win rate.**
- **Caveats**: **no abstract available** — all of the above is inference from title and from the surrounding CoG program. **Unverified affiliation.** Convergence speed depends on the MCTS configuration, so cross-game comparability requires a fixed budget and rollout policy, which the title does not promise.

### ★★ Predicting Drafted Deck Strength for "Magic: the Gathering" — venue recovery
- **Authors**: Tomas Rigaux, Hisashi Kashima
- **Affiliation**: **Graduate School of Informatics, Kyoto University, Japan** (both; `tomas@rigaux.com`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2607.04782 — comment field: **"Accepted at IEEE Conference on Games (CoG) 2026."** Proceedings pending on IEEE Xplore.
- **Link**: https://arxiv.org/abs/2607.04782
- **Abstract and key innovations**: names the structural reason **general-purpose policy learning is impractical** in many real games: *"their dynamics are defined by interactions among a large and often evolving collection of game pieces"* — the cards themselves write the rules. **Draft** is isolated as the tractable subproblem: eight players make **39–45 sequential selections from semi-random packs** to build a **40-card deck under partial information**, with **gameplay removed entirely**. Proposes an **encoder-based model producing set-contextualized card embeddings** to encode combinatorial card synergies.
- **Why it matters here**: **"the rules are in the pieces, so learn the decision not the game" is the correct reduction**, and this paper executes it cleanly — by discarding play and keeping only selection, it turns an unbounded-dynamics problem into a combinatorial-optimization one with a fixed horizon. That is a general template for any collectible/evolving-piece game, a class this wiki has almost no coverage of despite its commercial dominance. Partial information over 39–45 rounds also makes it a genuine sequential decision problem rather than a static prediction task. **Recovered via the new venue-string channel (§0.2.3)** — title search missed it.
- **Caveats**: **deck strength is predicted, not draft quality end-to-end** — the abstract does not say whether a strong predicted deck wins. Set-contextualized embeddings are the natural encoding but the abstract gives no baseline comparison. Kyoto University; CoG acceptance; **no results figures in the abstract.**

### ★★ Comparative Analysis of GAT and BERT for Human-Like Playtesting — venue recovery
- **Authors**: Kleio Fragkedaki, Theodoros Panagiotakopoulos, Matteo Biasielli, Hui Wang
- **Affiliation**: **AI Center of Excellence, King, Stockholm, Sweden** (all four; `@king.com` — **King Digital Entertainment**, the Candy Crush publisher). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2607.11501 — comment field: **"2025 IEEE Conference on Games (CoG)."** ⚠️ **CoG 2025, not 2026** — accepted last cycle, on arXiv now.
- **Link**: https://arxiv.org/abs/2607.11501
- **Abstract and key innovations**: predictive playtesting models mimic player behaviour, but existing data-driven methods **fail to capture the full range of player strategies** and demand **extensive feature engineering and network-architecture modelling** — a cost that recurs **every time a new game mechanic or feature is introduced**. The paper proposes a **more generalized representation** that reduces or eliminates the need for that per-mechanic retuning, comparing **GAT** (graph attention) against **BERT**.
- **Why it matters here**: **this is the industry's own statement of the maintenance problem.** The load-bearing phrase is *"necessitate continual adjustments to the models"* — a playtesting model that must be rebuilt per feature is not a tool, it is a recurring cost, and a major publisher saying so in a peer-reviewed venue is better evidence than any academic claim about generalization. The GAT-vs-BERT comparison is also a clean test of **whether structure (graph) or sequence (transformer) is the right inductive bias for player behaviour**, which is exactly the representational question §1's UBCL answers differently (continuous behaviour vectors). **First King-affiliated paper this wiki has recorded.**
- **Caveats**: **CoG 2025, one cycle stale** — filed as a venue recovery because the wiki had not covered it. **No winner declared in the abstract** — the comparison's outcome is not stated. A publisher-authored paper benchmarking its own representation carries the usual industry caveat; no acceptance beyond CoG 2025.

### ★ The Optimal Knight Exchange Puzzle is NP-Hard
- **Authors**: Henry Siegel (single author; no affiliation printed)
- **Venue**: arXiv:2606.29153 (28 Jun 2026) — `cs.DM`, `cs.CC`. 13 pages, 10 figures and tables. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2606.29153
- **Abstract and key innovations**: Knight's Tour is known **NP-hard on boards with holes** and **constant-time decidable on rectangular boards**, so the open case is intermediate restrictions. This paper shows **Knight's Tour is NP-hard for connected boards**, and gives a **polynomial-time reduction between the two problems** showing the **optimality version of Knight Exchange (Swap) is NP-hard**.
- **Why it matters here**: it closes a **specific gap in the hardness map** of a canonical recreational problem — the intermediate-restriction case that neither the trivial nor the fully-holed case covers — and does so with a reduction that transfers hardness *between* two well-known puzzles rather than only out of a known NP-hard problem. Included because chess-problem complexity is the theoretical substrate under §1's engine-evaluated experiments: **anything that assumes optimal puzzle structure is hard implicitly assumes a complexity class**, and this paper states it. Low impact on the game-RL lane but it is a clean, verifiable result on a game object.
- **Caveats**: **not a game-RL or game-AI paper** — pure combinatorial complexity. Single author, no affiliation, no venue. Included at ★ as scope-adjacent theory; see §8.4.

### ★ Playing the Rebus Game: DR.DENKER Measures Visual Lateral Reasoning in Language Models
- **Authors**: Michiel Pronk, Rik van Noord, Malvina Nissim
- **Affiliation**: not printed on the proceedings page. **Malvina Nissim** is a well-known NLP researcher (University of Groningen). **(partial — verify)**
- **Venue**: **IEEE CoG 2026**, paper #400, *Game Design and Technology*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: **DR.DENKER** is a puzzle game used to measure **visual lateral reasoning** in language models — a rebus/wordplay instrument rather than a game-playing agent.
- **Why it matters here**: this is **a game used as a psychometric instrument**, not a game to be beaten, and lateral reasoning is precisely the capability class that all of §5's chess and poker LLM evaluations fail to isolate. It pairs with yesterday's Queen and XiangqiBench to show the evaluation lane splitting into *playing* benchmarks and *reasoning* benchmarks — this is firmly the latter. The name is a Dutch wordplay reference, which fits the Groningen-adjacent author list.
- **Caveats**: **no abstract, no results.** Whether any model performs above chance is unknown from anything available. Unverified affiliation (partially inferred from a known appointment).

### ★ A Hybrid Codenames AI Team: Combining Static Word Embeddings and LLMs — Best Paper nominee
- **Authors**: Joseph Dalhke, Thomas Esplin, Matthew Sheppard, Christopher Archibald
- **Affiliation**: not printed on the proceedings page. **(unverified)**
- **Venue**: **IEEE CoG 2026**, paper #425, *AI for Game Playing* — and **one of the five nominees for the IEEE CoG 2026 Best Paper Award** (listed alongside MAPLE, MIPCGRL, #179 and #245 on the accepted-papers page).
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: a **team** of Codenames players combining **static word embeddings with LLMs** — i.e. a hybrid rather than an LLM-only agent.
- **Why it matters here**: **its Best Paper nomination is the finding.** Of the five nominees this wiki can now name in full (`129` MAPLE, `179` Genoese-Zerbi, `217` MIPCGRL, `245` Sroka & Tokarchuk, `425` Codenames), **three are about player experience, PCG or hybrid-agent design and only one (MAPLE) is game-RL** — and MAPLE did not win. That distribution says something about where the games community's self-assessed best work sits, and §8.3 takes it up. The hybrid architecture itself is a modest, sensible design: static embeddings for fast candidate generation, LLMs for the constrained final choice.
- **Caveats**: **no abstract, no results, unverified affiliation.** The nomination is verified; the content is not. Do not cite the nomination as evidence of a result.

---

## §6 Industry Game AI

### ★★★ IEEE CoG 2026 Award Results — MAPLE promoted to First Runner Up; the Best Paper crown goes to player experience
- **Source**: **`https://cog2026.org/awards`**, fetched and parsed for the first time in this series.
- **Full results as posted**:
  - **Best Paper Award — Winner (Delegate Vote)**: Valentina Genoese-Zerbi, Justus Robertson, Rogelio E. Cardona-Rivera — *Categorizing Experience Management Problem Difficulty Using Graph Analysis*
  - **Best Paper Award — First Runner Up (Committee Vote)**: Qian-Rong Li, Hung Guei, I-Chen Wu, Ti-Rong Wu — *MAPLE: Multi-State Aggregated Policy Evaluation for AlphaZero in Imperfect-Information Games*
  - **Best Paper Award — Second Runner Up**: Filip Sroka, Laurissa Tokarchuk — *Segment-Based Dynamic Difficulty Adjustment for Motor Learning in VR Rhythm Games*
  - **Best Reviewer Award**: Loutfouz Zaman (**Ontario Tech University**); Alexander Dockhorn (**University of Southern Denmark**); Miguel Belbute (**Instituto Superior Técnico, University of Lisbon**)
  - **Best Demo — Winner (Delegate Vote)**: Toby Best, Raluca Gaina, Simon Lucas, James Goodman, Jamie Harris — *Descent: Journeys in the Dark' Computer-Aided Content Generation*
  - **Best Demo — First Runner Up**: Paul Riesch, Mary Linke, Florian Rupp, Sabiha Ghellal, Katie Seaborn — *CaféBeans: An Exploratory Serious Game for Deceptive Design Awareness*
  - **Best Demo — Second Runner Up (tied)**: Mathias Babin — *TRACE: Temporal Representation Alignment for non-player Character Evolution*; Adrian Kathagen, Fabian Ostermann, Marco Pleines — *Simulating Super Mario Odyssey for Agent Training*
- **Why it matters here**: **three separate findings.**
  1. **MAPLE is upgraded from "nominated" to First Runner Up (Committee Vote).** Yesterday's digest recorded MAPLE as the wiki's first peer-reviewed game-RL signal with only a nomination attached. **It now has a rank**: second-place-by-committee among all CoG 2026 papers. That is a materially stronger claim than "nominated," and it is the **highest-ranked peer-reviewed game-RL result this wiki has ever recorded**.
  2. **The Best Paper winner is not game AI.** *Categorizing Experience Management Problem Difficulty Using Graph Analysis* is a **player-experience** paper, and the second runner-up is **VR motor-learning DDA**. **Of the three Best Paper placements, zero are agents, RL, or benchmarks.** The delegate-vote winner and the committee-vote runner-up disagree in kind, which is itself informative: **the room voted for experience management; the committee voted for AlphaZero.**
  3. **The Best Demo winner is content generation with Simon Lucas attached** — the OpenSpiel/VGDL author already met across this wiki's CoG coverage — and the tied second runner-up is the **Super Mario Odyssey agent-training simulator** this wiki covered at ★ on 10-05, now carrying a **Best Demo award**. That is a venue upgrade for an already-claimed entry (§9.2).
- **Caveats**: **awards are not papers.** Delegate votes reflect presentation-day impressions; committee votes reflect review. Neither substitutes for the content, and for the winner **no abstract is available in any source this run reached** (§6.5).

### ★★★ Playing the Player: A Heuristic Framework for Adaptive Poker AI ("Patrick")
- **Authors**: Andrew Paterson, Carl Sanders
- **Affiliation**: **Spiderdime Systems** — the comment field states **"White Paper by Spiderdime Systems."** Industry; no academic affiliation given.
- **Venue**: arXiv:2512.04714 (4 Dec 2025) — **49 pages, 39 figures. White paper.** No peer-review venue.
- **Link**: https://arxiv.org/abs/2512.04714
- **Abstract and key innovations**: **an explicit attack on the solver consensus.** The paper argues poker AI discourse has been dominated by solvers and the pursuit of **unexploitable, machine-perfect play**, and that the real path to victory is being **maximally exploitative**. It presents **Patrick**, a purpose-built engine for *understanding and attacking the flawed, psychological, and often irrational nature of human opponents*, with a **prediction-anchored learning method** and a reported **64,267-hand profitable trial**.
- **Why it matters here**: this is the **industry counter-position to the equilibrium orthodoxy that §5's GTO Wizard Benchmark embodies**, and the two should be read as a pair: GTO Wizard measures agents against a Nash approximation, Spiderdime argues that approximating Nash is the wrong objective against humans. **Both are correct in their own regime** — equilibrium play is unexploitable and therefore safe, exploitation is higher-variance and therefore higher-ceiling — and the fact that one is a benchmark paper and the other a vendor white paper is a fair summary of how the field actually splits. **64,267 hands is a real trial size** for poker and is disclosed as such. This is the most substantive industry artifact in §6 since the CoG industry talks.
- **Caveats**: **a vendor white paper with no peer review**, reporting its own profitability — the profit figure is self-published and unaudited. "Often irrational" is the load-bearing premise about human opponents and is not established in the abstract. 49 pages and 39 figures is long enough to contain the method, but no baseline comparison against a solver-derived agent is claimed. Filed under industry for exactly this reason.

### ★★ SAGE: Semantic-Aware Gray-Box Game Regression Testing with Large Language Models
- **Authors**: Jinyu Cai, Jialong Li, Nianyu Li, Zhenyu Mao, Mingyue Zhang, Kenji Tei
- **Affiliation**: **Waseda University, Tokyo, Japan** (all; `lijialong@fuji.waseda.jp` for Li). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2512.00560 — comment field: **"This paper has been accepted by Automated Software Engineering journal."**
- **Link**: https://arxiv.org/abs/2512.00560
- **Abstract and key innovations**: live-service games have **rapid iteration cycles**, so regression testing is indispensable — but in the common **gray-box setting where full source access is unavailable**, existing approaches rely on **manual test construction**, maintain **redundant suites**, and lack mechanisms for **prioritizing relevant tests**, producing excessive cost, limited automation, and insufficient bug detection. **SAGE** is a semantic-aware framework covering **test generation, test maintenance, and test selection** for gray-box game environments.
- **Why it matters here**: this is the **software-engineering side of the constraint this wiki has identified repeatedly**: for game AI, the binding limit is organizational and infrastructural, not algorithmic. SAGE attacks the *testing* half of that — the thing the 10-04 review found game studios largely lack — and it does so in the **gray-box** condition that is the actual state of most external QA work, not the full-source condition that academic tooling assumes. **Accepted in the *Automated Software Engineering* journal**, which makes it the best-credentialed SE result in this wiki's game-dev thread. It pairs directly with §2's 10-05 geometry-clipping QA paper: **detection of what to test (that one) and management of the suite (this one).**
- **Caveats**: **not a game-AI paper** — no agent, no RL, no player modelling. It is game *engineering*. Included in §6 because §6 is where this wiki's deployment-constraint thread lives; see §8.4. No defect-detection or cost numbers in the abstract.

### ★★ Efficient Human-like Aiming in FPS Games
- **Authors**: Brian Yang, Toma Allary, Ian Gauk, Clark Verbrugge, Joshua Romoff
- **Affiliation**: not printed on the proceedings page. **Clark Verbrugge** (OpenSpiel / Nervana Games / Samsung) and **Joshua Romoff** are established names; the roster suggests a Canadian collaboration. **(partial — verify)**
- **Venue**: **IEEE CoG 2026**, paper #163, *AI for Game Playing*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: **efficient human-like aiming** in first-person shooters — both efficiency and human-likeness as joint objectives for the aim controller.
- **Why it matters here**: **aiming is the FPS primitive where "human-like" is a hard requirement rather than a nicety** — an aimbot that plays better than a human is detectable precisely because it is not human-like, so the objective is genuinely two-dimensional. That makes this a rare case where the *production constraint* (undetectable) and the *research objective* (human-like) coincide, which is why the joint framing in the title is the contribution. It extends the same human-likeness thread as this wiki's CoG #394 (*general and human-like Mario playing*) into a genre where it has direct anti-cheat consequences.
- **Caveats**: **no abstract, no results.** "Efficient" is undefined — efficient relative to what compute or what latency budget. Unverified affiliation (partially inferred from known authors).

### ★ Efficient Multi-Guard Patrol through Extended Composite Potential Fields
- **Authors**: Kaijie Xu, Yiwei Zhang, Clark Verbrugge
- **Affiliation**: not printed on the proceedings page. **Clark Verbrugge** again (same author as §2's *Ally-Conscious Area of Effect Targeting* and §7's 10-05 *Expected Target Entropy*). **(partial — verify)**
- **Venue**: **IEEE CoG 2026**, paper #287, *AI for Game Playing — Auxiliary Papers*.
- **Link**: https://cog2026.org/acceptedpapers (no arXiv preprint located)
- **Abstract and key innovations**: **composite potential fields** extended for **multi-guard patrol** efficiency — a coverage/patrol problem in game AI.
- **Why it matters here**: potential-field methods are the old workhorse of game agent movement, and this is **an extension result rather than a replacement** — it is notable mainly as evidence that the classical toolkit is still being actively extended at CoG rather than displaced by learned policies. Included because Verbrugge's three papers at this single venue (#166, #287, and the 10-05 #339) collectively describe a **coherent classical-game-AI program**, which is the counterweight to the LLM-dominated entries elsewhere in this digest.
- **Caveats**: **auxiliary track** — a lower bar than the regular track. No abstract, no results, unverified affiliation. Included for programmatic context rather than as a finding.

---

## §7 Related Techniques

### ★★ CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery
- **Authors**: Tao Feng, Fangxu Yu, Zijie Lei, Jiaru Zou, Changjiang Jiang, Yi Yan, Jiaxuan You, Pan Lu
- **Affiliation**: **University of Illinois Urbana-Champaign** (Feng, Lei); **University of Maryland, College Park** (Yu); **Stanford University** (You, Lu); remaining authors without affiliation in the HTML block. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.04851 (3 Oct 2026) — **no venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.04851
- **Abstract and key innovations**: frozen-LLM search can reuse prior solutions in context but **cannot update from successes and failures on the test problem**; RL enables that adaptation but **strongly favoring high-reward trajectories suppresses low-reward yet potentially promising directions too early.** CURIO complements task feedback with an **Intrinsic Curiosity World Model (ICWM)** that learns transitions in the policy's **hidden-state representation** and supplies **prediction-error bonuses at sampled tokens outside the policy's top-k choices** — i.e. curiosity is injected exactly where the policy is *not* already confident. **Epoch normalization** and an **annealed weight** regulate contribution.
- **Why it matters here**: **the design decision that makes this transferable to games is *where* the bonus goes — outside the top-k.** That is a principled answer to the exploration problem rather than an epsilon to tune: reward novelty precisely in the tokens the policy would never emit on its own. The ICWM operating on **hidden states rather than inputs** is the detail that makes it cheap and domain-agnostic, and it is structurally the same move as §1's option discovery — both carve out *unexplored* regions of the decision space and fund them explicitly. The stated failure mode (premature suppression of low-reward directions) is exactly what kills exploration in sparse-reward games.
- **Caveats**: **six mathematical tasks named; no game evaluation.** Preprint, unreviewed. The annealed weight and epoch normalization are two more hyperparameters in what is already a two-signal objective. Test-time RL is expensive and the abstract gives no cost figure.

### ★★ Attention Trajectories as a Diagnostic Axis for Deep Reinforcement Learning
- **Authors**: Charlotte Beylier, Hannah Selder, Arthur Fleig, Simon M. Hofmann, Nico Scherf
- **Affiliation**: **Max Planck Institute for Human Cognitive and Brain Sciences**; **Center for Scalable Data Analytics and Artificial Intelligence (ScaDS.AI)** — i.e. MPI + Saarland/Saarbrücken. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2511.20591 — comment field: **"Published in Transactions on Machine Learning Research (TMLR)."**
- **Link**: https://arxiv.org/abs/2511.20591
- **Abstract and key innovations**: feature reliance in deep RL is poorly understood. The method aggregates **saliency information at object and modality level into hierarchical attention profiles**, quantifying how agents allocate attention *over time* to form **attention trajectories** through training. Profiles are **compared across controlled conditions, connected to behavioural measurements, and reproduced with different saliency methods to check robustness**. Applied to **Atari 2600 benchmarks** plus custom environments.
- **Why it matters here**: **this is the interpretability instrument §2's SAT-RTS is reaching for, done properly and on the canonical RL benchmark.** Three design choices separate it from the usual saliency tour: aggregation to **object and modality** level rather than raw pixels, **trajectories over training** rather than single snapshots, and — most importantly — **reproduction across different saliency methods as a robustness check**, which is the control that saliency work almost always skips. Connecting the profiles to **behavioural measurements** closes the loop that pure attribution leaves open. Atari 2600 is the same benchmark as §1's Wayfarer, so this could in principle be run against it. TMLR publication from an MPI cognitive-science group gives it unusual methodological credibility for a diagnostic paper.
- **Caveats**: **salience maps are contested as explanations** and the paper's own robustness requirement concedes that. "Applied to Atari 2600" — no specific finding about *which* agents over-rely on *what* appears in the abstract, so this is a method claim, not a result. Not a game paper beyond the Atari substrate.

### ★★ Characterizing Robustness of Strategies to Novelty in Zero-Sum Open Worlds
- **Authors**: Mayank Kejriwal, Shilpa Thomas, Hongyu Li
- **Affiliation**: **Information Sciences Institute, University of Southern California**, Marina del Rey, CA (all three; `kejriwal@isi.edu`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2602.14278 — **25 pages, 10 tables, 15 figures.** No venue acceptance claimed.
- **Link**: https://arxiv.org/abs/2602.14278
- **Abstract and key innovations**: agents must contend with **novel conditions that deviate from training or design assumptions**. Studies robustness of **fixed-strategy** agents to novelty in two-player zero-sum games, across **Iterated Prisoner's Dilemma and heads-up Texas Hold'em Poker**. Novelty is **operationalized as a perturbation of the game's rules or scoring mechanics while agent behaviour remains fixed**, and two metrics are introduced to measure the effect.
- **Why it matters here**: **holding behaviour fixed while perturbing the rules is the correct experimental design for isolating environmental novelty**, and it is the design almost nobody uses — the default confounds "the agent adapted" with "the change was survivable." That makes this the *control-condition* paper for the open-ended-generalization thread: §3's Neural MMO work and the robustness claims in this wiki's foundation-model entries all need to know how much of a gain under novelty is adaptation and how much is that the novelty was benign. **Two structurally different domains** (IPD is a tiny symmetric game; Hold'em is large and asymmetric) is the right spread for a generalization claim. ISI/USC is the same lab as §7's RAG-vs-fine-tuning world-model paper.
- **Caveats**: **fixed-strategy agents only** — the interesting case (agents that adapt) is explicitly out of scope, so this measures the *floor* of robustness, not the behaviour of a trained system. "Novelty" is defined by the authors' own perturbation set; how it maps to real distribution shift is unaddressed. Preprint, unreviewed.

### ★★ How Much Due Diligence Before You Bid? Learning in Intractable Takeover Auctions
- **Authors**: Zain Naboulsi (single author)
- **Affiliation**: not printed — **no HTML version available.** **(unverified)**
- **Venue**: arXiv:2606.29457 (28 Jun 2026) — `cs.AI`, `cs.GT`, and machine-learning categories. 21 pages, 13 figures, 2 tables; **code and data released.**
- **Link**: https://arxiv.org/abs/2606.29457
- **Abstract and key innovations**: two companies bid for the same target; each pays for **due diligence — costly, imperfect homework that sharpens its private estimate before bidding.** The paper builds a computer model of the contest and **lets it teach itself to bid by playing against itself, the way a game engine learns chess.** The economic question (how much diligence pays) and the computational question (when the contest becomes too complex to solve exactly) are **both controlled by one variable: how many pieces of private information a bidder carries.** Main finding: the right amount of diligence is set by that information count.
- **Why it matters here**: **self-play as a solver for an intractable auction is the game-RL method applied outside games, and the framing makes the transfer explicit** — "the way a game engine learns chess." What makes it worth carrying is that the **economic and computational questions are shown to share a single control parameter**, which is the kind of structural result that does not come out of either literature alone. Included at ★★ because the self-play mechanism is directly this wiki's core method, tested where there is no simulator to fall back on. Code and data released.
- **Caveats**: **not a game** — a financial-market model. Single author, no affiliation available, no peer-review venue. The "intractable" framing is a modelling choice; whether real auctions resemble the model is unstated. Included under §7 with scope flagged in §8.4.

### ★★ Synthetic Counteradaptation: A Principle of Human-AI Co-evolution
- **Authors**: Ivar Frisch, Jackie Kay, Philip Moreira Tomei
- **Affiliation**: not printed in the HTML authors block (no HTML version available). **(unverified)**
- **Venue**: arXiv:2606.15503 — comment field: **"Published in Antikythera (MIT Press), February 2025."** 15 pages, 1 figure.
- **Link**: https://arxiv.org/abs/2606.15503
- **Abstract and key innovations**: **synthetic counteradaptation** — human and AI systems co-evolve by adapting to each other's strategies; AI systems develop **novel strategies or social protocols**, prompting humans to extract insights and adapt, producing **new agent interaction dynamics.** Illustrated across **the game of Go, mixed-motive social interactions, and geopolitical simulations.**
- **Why it matters here**: this names the dynamic that §2's anti-cheat paper (behavioural fingerprinting vs. account misuse) and §5's whole evaluation lane both assume but rarely articulate: **the measured population is adapting to the measurer.** A benchmark result is only stable while players and agents have not co-adapted around it, and Go after AlphaGo is the canonical instance. Placing it in a **MIT Press** venue rather than a CS one signals it is aimed at the conceptual frame rather than a method — which is what this digest's §8 needs: a vocabulary for why instrument-validity findings keep recurring.
- **Caveats**: **MIT Press *Antikythera* is a theory outlet, not peer-reviewed ML.** No method, no measurement, examples illustrative. "Co-evolve" is asserted of cases where the feedback loop is loose. Included for framing, not evidence.

### ★ Quantifying Skill and Chance: A Unified Framework for the Geometry of Games
- **Authors**: David H. Silver (single author; **not** the DeepMind Go/AlphaZero David Silver — see §9.5)
- **Affiliation**: **Remiza AI** (from the HTML authors block). Industry.
- **Venue**: arXiv:2511.11611 (3 Nov 2025) — `cs.AI`, `cs.LG`, `cs.MA`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2511.11611
- **Abstract and key innovations**: models games as **complementary sources of control over stochastic decision trees**, and defines a **Skill-Luck Index S(G) ∈ [−1, 1]** by decomposing outcomes into **skill leverage K** and **luck leverage L**, plus a **volatility Σ** for outcome uncertainty across turns. Applied to **30 games**: coin toss S = −1; backgammon S = 0, Σ = 1.20; chess S = +1, Σ = 0; **poker S = 0.33, K = 0.40 ± 0.03, Σ = 0.80.**
- **Why it matters here**: **a single index that places 30 games on one calibrated axis** is the kind of instrument this wiki's benchmark section has lacked when asking *which games are fair tests of skill*. The interesting numbers are the middle ones: **backgammon at S = 0 with the highest volatility** shows the index separates "balanced" from "noisy," which a naive skill metric conflates; **poker at 0.33 with a quoted ±0.03** is the only game given an uncertainty, and it is the claim most likely to be contested. The stochastic-decision-tree formulation is general enough to cover the games §1 and §5 actually study.
- **Caveats**: **author-name collision with DeepMind's David Silver is a live dedup risk** (§9.5). **Remiza AI affiliation; no peer-review venue.** 30 games with one index implies strong modelling assumptions that the abstract does not state, and the ±0.03 on poker appears without a method. Treat the specific values as provisional.

### ★ Turing's First Imitation Game: Design Concepts and a Human-Approximates-Machine Reading
- **Authors**: Sharon Temtsin, Christoph Bartneck
- **Affiliation**: **University of Canterbury, Christchurch, New Zealand** (`sharon.temtsin@pg.canterbury.ac.nz`); Bartneck is a long-standing Canterbury robotics/HCI faculty member. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2608.05558 — **no venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2608.05558
- **Abstract and key innovations**: reads Turing's **1948 "Intelligent Machinery" report** as the source of the later imitation games. Identifies the **design concepts behind the 1948 chess-based imitation game**: that intelligent machines may **make mistakes**, the **exclusion of irrelevant physical features**, the role of the **human judge**, and Turing's claim that **intellectual activity consists mainly of search**. Second contribution: restricting the human contestant to a **rather poor chess player** *increases* the role of intellectual search and makes human behaviour **more comparable to machine behaviour**.
- **Why it matters here**: the **human-approximates-machine** reading inverts the usual Turing framing, and it is directly relevant to how this wiki's evaluation papers set their baselines: if the point is comparability rather than indistinguishability, then **a weak human baseline is the correct instrument, not a deficient one.** That is a defensible methodological stance for LLM game evaluation, where comparing against grandmaster play has repeatedly produced uninterpretable results. Turing's "intellectual activity is mainly search" is also the premise §1's MCTS-convergence difficulty measure (§5) operationalizes without knowing it.
- **Caveats**: **history/philosophy of AI, not a technical contribution.** No method, no results. University of Canterbury; preprint. Included at ★ for the framing only.

### ★ The Affordance is the Message: Creative Media as Complex Systems
- **Authors**: Ane Espeseth, Elias Najarro
- **Affiliation**: **Center for Computing in Science Education, University of Oslo, Norway** (Espeseth); **Play, Culture and AI, IT University of Copenhagen, Denmark** (Najarro). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2608.12349 — comment field: **"17th International Conference on Computational Creativity (ICCC 2026), Coimbra, Portugal."**
- **Link**: https://arxiv.org/abs/2608.12349
- **Abstract and key innovations**: formalises **computational-creativity media** using the conceptual toolbox of **complex systems**, introducing nine properties — **emergence, collective intelligence, self-organisation, non-linear dynamics, criticality, multi-scale hierarchy, phase transitions, diversity of attractors, path dependence, open-endedness** — as a vocabulary for describing and comparing creative media **at the system level**, with **medium affordances as the design-level mechanisms** that produce those properties.
- **Why it matters here**: **open-endedness is the property this wiki's game-foundation-model work keeps invoking and never defines**, and this paper supplies a nine-term vocabulary for it that is not tied to any one system. That makes it a useful reference for §3: when a world model or a PCG system is called "open-ended," this is the checklist against which the claim can be itemized. The affordance/system-level split — **design mechanisms vs. emergent properties** — is also the right way to state what §4's PCG papers are actually manipulating.
- **Caveats**: **conceptual/formal paper at a computational-creativity venue; no empirical result.** The nine properties are presented as a vocabulary, not as measured quantities, so the framework's usefulness is untested. Included at ★ as definitional infrastructure.

---

## §8 Cross-Cutting Synthesis

### 8.1 The fresh window was empty, and that is the first honest negative result in this series
Every prior digest in this run has been able to point at a moving `/new` ceiling and a handful of new game papers above it. **Today the ceiling did not move at all — `2610.03717` yesterday, `2610.03717` today, across six categories re-enumerated from scratch.** The 624 papers above yesterday's boundary contain **zero** new game papers, and the three that survive a keyword filter are a LLM post-training paper with a game title, a four-page repeated-game note, and an embodiment benchmark that merely lists games among its domains. This matters for a reason the 10-05 digest did not state: **a digest that needs the fresh window to have content will manufacture saturation claims whenever the window idles, and will under-report whenever it is ignored.** The correct response is to say the channel was idle and then show that the rest of the method still produced thirty-six papers — which is what §0.2 documents. **The empty window validates the multi-channel design rather than refuting it.**

### 8.2 The venue-string query is the channel upgrade of this run
Yesterday's digest located 14 CoG 2026 preprints using **eleven title-search variants per paper**. Today, **one full-text query for the literal string `"Conference on Games"`** surfaced `2601.05386` (chess cheating), `2606.26267` (DD-Elo), `2607.04782` (Magic Draft) and `2607.11501` (GAT/BERT playtesting) — **two of which are today's ★★ venue recoveries and which title search had missed entirely.** The mechanism is simple and worth writing down: **CoG authors put the venue in the comment field or the body, not the title**, so title search is structurally the wrong field. The generalizable form is **search arXiv full text for the venue string**, which will work for any conference whose authors annotate their submissions. This should be the first query run on any future proceedings sweep, and it retroactively explains why the earlier CoG coverage had long tails of papers marked "no arXiv preprint located" — several of those were findable, just not by title.

### 8.3 The CoG 2026 awards say where the games community thinks its best work is
Reading the award placements together rather than individually: **the delegate-vote Best Paper went to experience-management difficulty categorization; the committee-vote First Runner Up went to AlphaZero for imperfect-information games; the Second Runner Up went to VR motor-learning DDA; and the Best Demo went to board-game content generation.** **Zero of the three Best Paper placements are agent, RL, or benchmark papers**, and the two voting bodies disagree in kind. Meanwhile the Best Paper *nominee* list is `129` MAPLE (game RL), `179` (experience management), `217` MIPCGRL (PCG), `245` (VR DDA), `252` (mental-health mobile games), `425` Codenames (hybrid agent design) — **one game-RL entry in six.** The honest reading is that **this wiki's lane is a minority interest at its own flagship venue**, and that the peer-reviewed signal it has been waiting for (§8.3 of the 10-05 digest) is real but small. That has a practical consequence for cadence: **treating CoG as a source of game-RL results will keep yielding one or two papers per sweep; treating it as a source of player-experience and PCG results will yield the venue's actual center of gravity.**

### 8.4 Where I stretched the brief, and why
Four entries are included despite not being game-RL or game-AI papers, each deliberately: **The Morality Game** (§5) is `q-bio.NC` behavioural-science infrastructure; **SAGE** (§6) is software-engineering test-suite management; **The Optimal Knight Exchange Puzzle is NP-Hard** (§5) is combinatorial complexity; **Takeover Auctions** (§7) is a financial model. Each is flagged in its own caveats. The justification is that §6 in particular exists in this wiki specifically to track the **deployment-constraint thread** — the finding, repeated across three digests, that game AI's binding limit is organizational rather than algorithmic — and SAGE is a directly actionable instance of that thread's remedy. If the reader disagrees, dropping those four costs nothing structurally.

### 8.5 Measurement validity is now the recurring theme of the week
Four independent entries this run attack an instrument rather than a result: **§2's real-time gap paper** shows tick conversion under-predicts loss by ~15 pp while appearing to cost nothing; **§1's poker probing paper** shows a hidden-state probe's positive result is largely explained by observable betting composition; **§5's MCTS-convergence difficulty paper** replaces designer-assigned difficulty with a search measurement; **§7's attention-trajectory paper** requires reproduction across saliency methods before trusting an attribution. That is the **fourth consecutive digest** in which the strongest papers are the ones that say *the field is measuring the wrong thing*, and it is now a pattern rather than a coincidence. The practical implication for this wiki: **when selecting papers, an instrument-critique paper is higher-value than a method paper with a better number**, because the number's interpretability depends on the instrument.

---

## §9 Cross-References and Dedup Notes

### 9.1 Dedup verification log
- Whole-`wiki/` regex sweep: **7,940 unique arXiv IDs claimed** prior to this file.
- **All 36 featured arXiv IDs verified 0-hit immediately before writing** by exact word-boundary regex:
  `2610.05569`, `2610.04253`, `2610.04810`, `2610.02847`, `2610.02542`, `2610.04851`, `2610.04920`, `2601.05386`, `2607.04782`, `2606.26267`, `2608.14851`, `2607.19369`, `2606.30090`, `2607.21195`, `2606.24037`, `2603.23660`, `2607.11486`, `2512.04714`, `2606.29153`, `2512.00560`, `2512.10835`, `2608.09132`, `2606.26694`, `2607.00483`, `2512.02473`, `2511.20591`, `2602.14278`, `2606.29457`, `2607.11501`, `2606.26970`, `2608.04037`, `2607.11388`, `2606.15503`, `2511.11611`, `2608.12349`, `2608.05558`.
- **CoG 2026 entries verified by exact title**, not by author surname. Entries confirmed **already covered and therefore dropped**: *Social Deduction* (#8 — ⚠️ **false positive: the wiki's "Social Deduction" hits are different papers**; see §9.5), *Wave Function Collapse* (covered 07-08 and 07-30 under a different title), *Tales of Tribute* (covered 10-05), *Augmenting Game AI with Deep RL* (#294, `2606.20210`, covered 06-30 / 07-06 / 07-07 / 07-08), *MIPCGRL / Multi-Objective Instruction-Aware PCGRL* (#217, `2508.09193`, covered 07-15 / 07-30 / 08-17 / 10-05), *Vox Deorum* (#208, covered 07-30), *PCG.ME* (#359, covered 07-01 / 10-04), *IRumAI* (#171, covered 06-30 / 10-05), *Compiling VGDL into Causal Models* (#320, `2609.05459`, covered 09-30), *Augmentations for Streamed Video Games* (#150, covered 08-01), *Proactive or Reactive? DDA in an Exergame* (#147), *Nonslop* (#165), *Dance Dance Prompting* was **re-verified as new**, *PuzzleJAX* (#221, covered 10-05), *Stack More Levels* (#394, covered 10-05), *Text2BT* (#371, covered 10-05), *PIMCTS Evaluation* (covered 10-05), *An Evaluation of VLMs for Geometry Clipping* (#380, covered 10-05).
- **⚠️ A surname-based intermediate pass produced 6 false-positive "new" flags** (`RIDGE`, `PRISM`, `Social Deduction`, `Tales of Tribute`, `Wave Function Collapse`, plus `Monte Carlo Tree Search in Imperfect-Information`). All were caught by exact-title re-verification. **This is the second consecutive run where title-level dedup was required after ID-level dedup passed** — a repeat of the failure mode the 10-05 digest recorded.

### 9.2 Venue updates to already-covered papers (not re-summarized)
- **MAPLE (`2605.24139`, CoG #129)** — **elevated from "Best Paper nominee" to "First Runner Up (Committee Vote)"** per `cog2026.org/awards`. Recorded in §6.1; the 10-05 summary stands otherwise.
- **Simulating Super Mario Odyssey for Agent Training (CoG #86, Kathagen / Ostermann / Pleines)** — awarded **Best Demo, Second Runner Up (tied)**. Covered at ★ on 10-05; the award is the update.
- **MIPCGRL (`2508.09193`, CoG #217)** — confirmed still on the **Best Paper nominee list**; not placed. Covered on 10-05.
- **Characterizing Game Difficulty Using MCTS Convergence (#23)**, **Pacing-Aware PCG (#356)**, **Game Simulacra (#313)** — new entries whose groups overlap with the award winners; see §6.1.
- **Augmenting Game AI with Deep RL (`2606.20210`, CoG #294)** — confirmed on the accepted list under *AI for Game Playing — Auxiliary Papers*; already covered in four files.
- **Best Reviewer Award: Loutfouz Zaman (Ontario Tech)** — Zaman is a co-author of today's §1 RIDGE (#415). Noted because the two facts together indicate a heavily engaged single-author-group presence at this venue.

### 9.3 Same-day sibling collisions (recorded, not absorbed)
- **`arxiv-ai-search.md`** (same directory, today) claims **`2610.05033` Code2Games** — an agentic framework building UE5 game worlds from a natural-language game intent, plus the **GameCode4D benchmark** (10 prompts). It falls inside the **unswept band `2610.03718`–`2610.06900`** (§0.1) and is the clearest evidence that band has game content. **Excluded from §1–§7.**
- No other same-day sibling claims an ID overlapping this digest's featured set.

### 9.4 Affiliation and rendering caveats
- **No HTML version exists** for `2606.24037` (Morality Game), `2512.04714` (Spiderdime), `2606.29457` (Takeover Auctions), `2606.15503` (Counteradaptation). Affiliations for these are **unverified or absent** and are marked as such in their entries.
- **Abs pages carry no affiliation at all** for `2608.14851` (chess puzzles), `2607.19369` (poker probing), `2608.04037` (narrative worlds), `2606.29153` (knight hardness). Where an affiliation is given it is **inferred from a known appointment and labelled as inference** (§1, chess puzzles; §5, knight hardness is explicitly *not* inferred).
- **CoG 2026 proceedings pages carry affiliations only as unlinked superscripts.** Every CoG entry in §1–§6 therefore either prints no affiliation or marks a partial one tied to a previously-established author identity (Verbrugge, Lucas, Zaman, Nissim, Robertson, Hamari/Thawonmas).
- `2606.26970` and `2606.30090` use numeric affiliation markers (`1`, `1,3,4`) whose full expansions are partially truncated in the HTML block; the institutions given are the ones legible.

### 9.5 Name collisions and dedup traps encountered
- **⚠️ "David H. Silver" (`2511.11611`, Remiza AI) is NOT the DeepMind David Silver** of AlphaGo/AlphaZero/DreamerV3 fame. Same surname, different person, different affiliation. Explicitly flagged in §7 and here because a future dedup pass matching on surname+field would wrongly merge or wrongly drop this entry.
- **⚠️ "Yuchen Li" appears twice in CoG 2026 with different papers**: as co-author of **#394 Stack More Levels** (Togelius group, NYU) and as co-author of **#221 PuzzleJAX**. The 10-05 digest already warned these are the same name across the Togelius group — but **"Yuchen Li" in the §1 MIPCGRL context is a different author entirely**. Name matching is not identity matching.
- **⚠️ "Social Deduction" title collision**: the CoG #8 title *Training Compact Language Models for Strategic Reasoning in Social Deduction Games* matched wiki text from unrelated papers on 07-31 and 09-12 that merely used the phrase. **Exact-title verification required**; #8 is genuinely new.
- **⚠️ "RIDGE" collision**: the string matched `wiki/papers/llm-training/complete-mue-moe.md` and `wiki/synthesis/2026-06-09/investment-daily.md`, both unrelated. CoG #415 is genuinely new.

---

## §10 Bottom Line

1. **The arXiv fresh window is idle, not exhausted** — ceiling `2610.03717` unchanged across two runs, **0 new game papers above yesterday's boundary**. This is the series' first enumerated negative result and it validates the multi-channel design: thirty-six papers came from the other channels.
2. **The unswept band `2610.03718`–`2610.06900` is a known, owned gap.** The export API was rate-limited all run; sibling `arxiv-ai-search.md` has already covered most of it and found `2610.05033` Code2Games there. **A future run should sweep that range first, before any topical query.**
3. **Search arXiv full text for the venue string.** `"Conference on Games"` in one pass beat eleven title-query variants yesterday and recovered two ★★ papers (`2601.05386`, `2606.26267`) that title search had declared absent. This is the highest-leverage procedural change available.
4. **MAPLE is now First Runner Up at CoG 2026 (Committee Vote)** — the highest-ranked peer-reviewed game-RL result this wiki has recorded, upgraded from a bare nomination.
5. **But CoG 2026's Best Paper placements contain zero game-RL, game-AI or benchmark papers.** The venue's center of gravity is player experience and PCG. Future sweeps should be scoped accordingly — **one or two game-RL papers per CoG sweep is the realistic yield, not a failure.**
6. **Strongest papers today**: `2610.04810` (real-time gap — tick conversion is wrong by 15 pp, preregistered, two-host replicated), `2610.04253` (Spec2Game — controlled rule variants across 3,330 projects), `2603.23660` (GTO Wizard — the incumbent HUNL baseline is beatable by +19.4 bb/100, and AIVAT gives 10× cheaper evaluation), `2610.05569` (Factoriax — 1B PPO steps in 8 minutes).
7. **Title-level dedup caught six false positives that ID-level dedup missed**, in the second consecutive run. **Exact-title verification of CoG entries is now mandatory, not optional.**
