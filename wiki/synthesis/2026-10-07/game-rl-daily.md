---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-07)"
type: synthesis
created: 2026-10-07
updated: 2026-10-07
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, imperfect-information, poker, chess, self-play, marl, world-models, benchmarks, game-dev, game-theory, industry-game-ai, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-07)

> **Yesterday's digest declared the `2610.*` announcement block idle. Today the export API shows it was never idle — it was only invisible to `/new`.** The frontier moved from `2610.03717` (the 10-06 `/new` ceiling) to **`2610.08791`** on the export API, a gap of ~5,000 IDs that yesterday's run explicitly flagged as "unswept, with a known owner." This run swept it. The fresh window yields **17 featured papers across all seven requested lanes** — Game RL theory, LLM game agents, world models, benchmarks, game-dev industry, and game-theoretic RL — plus **5 papers withdrawn as same-day sibling duplicates** and recorded in §9 rather than re-summarized. ⚠️ **The most consequential event of this run is a dedup collision, not a paper**: `arxiv-daily.md` (same directory) was written *during* this harvest and claims four of this run's originally-selected papers — including its two strongest game papers, the ten-hero MOBA world-model result and the video-game speedrunning benchmark. They are excluded from §§1–7 and cross-referenced in §9.3. This is the **fifth time in seven days** that ID-level dedup alone would have produced duplicates, and the second consecutive day in which the collision was with a same-directory sibling.

---

## §0 Method and Corpus

### 0.1 Boundary determination
- **Yesterday's announced ceiling: `2610.03717`** (the `/new` announcement frontier; the 10-06 digest stated this directly).
- **Today's true frontier: `2610.08791`.** Enumerated from the arXiv export API (`export.arxiv.org/api/query`), sorted `submittedDate desc`, across **six** categories (`cs.AI`, `cs.LG`, `cs.MA`, `cs.CL`, `cs.CV`, `cs.GT`), `max_results=200` each. Newest indexed timestamp at run time: **`2026-10-06T17:59:02Z`** — i.e. the newest *announced* block is still 2026-10-06, and no 2026-10-07 submission exists yet. The window is therefore a **single-day announcement block, explicitly not a rolling 24 h**, which is arXiv's normal behaviour (announcement lags submission and there is no weekend block).
- **Fresh, unclaimed band: `2610.06901`–`2610.08791`.** The whole-wiki claimed-ID baseline at the start of this run was **8,047 unique arXiv IDs**, with the highest claimed `2610` IDs at `2610.06900` (the 10-06 digest's stated global ceiling). Papers in the `2610.05xxx`–`2610.06xxx` range are **catch-up** from the band yesterday's run deferred; papers at `2610.00608`/`2610.01181` are older still and surfaced because the category sweeps are `max_results`-bounded rather than date-bounded.

### 0.2 Sweep — two channels
1. **arXiv export API, six category feeds** (Atom XML, serialized, `sleep 5` between calls). 857 unique records in the parsed pool, min `2609.20450`, max `2610.08791`.
2. **Targeted keyword sweeps** across `abs:self-play`, `abs:Atari`, `abs:StarCraft`, `abs:NPC`, `abs:level generation`, `abs:game agent`, `abs:game benchmark`, `abs:Minecraft` — used as a **recall net**, since game papers frequently avoid the word "game" in the title. The high-value finds (`CompusPlay` `2609.32228`, `SC2Tools` `2509.18454`, `Physical Atari` `2606.19357`) were older than the featured window and are noted, not featured.

**Pool accounting**: 857 pool records + ~320 targeted-search records → **~1,180 unique records**, of which **~7,940 were already claimed** by the wiki; the game-keyword filter returned **128 game-adjacent candidates (90 unclaimed)**, manually triaged to the 17 below.

### 0.3 Dedup — and the sibling collision that changed the yield
- Whole-`wiki/` regex sweep `2[0-9]{3}\.[0-9]{4,5}` → **8,047 unique claimed IDs** at baseline (rebuilt to **8,099** after the sibling writes, §0.4).
- **All 22 initially-selected IDs re-verified immediately before writing.** **Five were claimed mid-run**:
  - `2610.08033` (ten-hero MOBA Dyna loop), `2610.08076` (SpeedrunBench), `2610.08621` (Recursive Game Creator), `2610.07640` (chess tactics) → `wiki/synthesis/2026-10-07/arxiv-daily.md`, written at **11:19** *after* this run's baseline at 11:01.
  - `2610.08720` (WorldSolver) → `wiki/synthesis/2026-10-07/arxiv-paper-check.md`.
- Per protocol these are **withdrawn from the featured sections and recorded in §9.3** with what the sibling reports and why each belonged here — **not re-summarized**. The lost set is severe: it contains this run's two strongest game papers (the MOBA result and SpeedrunBench). **Standing recommendation: sibling jobs on one announcement window must take their claimed-ID baseline at the same instant or serialize.**
- **Title-level check retained**: the game-keyword filter is a *title+abstract* heuristic and produced obvious false positives (e.g. `2610.08539` matched on unrelated text; `2610.08750` "Neural Petri flows" matched on an internal keyword). Every featured entry was opened and its abstract read before inclusion.

### 0.4 Affiliations
- Institutions were read **only** from each paper's own arXiv HTML `ltx_authors` / `ltx_contact` block, an explicit front-matter address block, or the PDF title block — **never inferred from surnames or email domains**.
- **16 of 17 featured affiliations recovered**; **1 paper has no affiliation printed** (`2610.07814`, Junsoo Ha — independent researcher, single author, only a gmail address). `2610.08033` (independent) was a sibling-claimed paper and is recorded as unaffiliated.
- No LaTeXML author-block stripping occurred this run. Two affiliations are reported *as printed*: `2610.06028` is affiliated with **GTO Wizard** (an industrial poker-solver vendor) per the author's own `wataru@gtowizard.com`; `2610.07638` spans a four-institution collaboration recorded in §7.

---

## §1 Game RL — Reinforcement Learning in Games

### ★★ Orchestrating Level-$K$ Policies Against Unknown Opponents in Partially-Observable Dynamic Games
- **Authors**: Addison Kalanther, Sanika Bharvirkar, Daniel Bostwick, Chinmay Maheshwari, Shankar Sastry
- **Affiliation**: **University of California, Berkeley** (EECS; `{addikala, sbharvirkar, daniel.k.bostwick}@berkeley.edu`, `sastry@coe.berkeley.edu`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.04937 (4 Oct 2026) — `cs.MA`, `cs.RO`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.04937
- **Abstract and key innovations**: Level-$K$ reasoning builds a hierarchy of policies specialized to opponents of different reasoning depths; when the opponent's level is unknown, the standard deployment rule estimates the level and plays the corresponding best response. The paper's observation is that **in a dynamic, partially-observed game this selection is itself a control problem** — the highest-likelihood opponent level need not maximize expected return from the current history, because each choice shapes future states and observations. It formalizes deployment as **dynamic orchestration of a fixed, pretrained policy library in a partially observable Markov game**, and compares classification-based orchestrators (offline and on-policy data aggregation) against a **reinforcement-learning-based orchestrator (RLBO)** trained to maximize discounted return. In pursuit-evasion experiments, RLBO beats both, and given a pretrained library reaches performance comparable to a policy trained directly over the pursuers' action space **with fewer training timesteps**.
- **Why it matters here**: this is the cleanest statement in the corpus of a **separation between policy learning and policy selection** that games actually require — real opponents are heterogeneous and unknown, and the standard response (online opponent modelling + best response) conflates estimation with control. Treating the library as a *resource for orchestration* rather than a *prescription for deployment* is a reusable reframe, and the result that an RL orchestrator beats classifier selection from the same library is a concrete negative result for the ubiquitous "classify then act" pipeline.
- **Caveats**: **preprint, no venue, and the evaluation is a single pursuit-evasion domain.** "Fewer training timesteps" is relative to a direct-action-space policy, not to a wall-clock or sample budget normalized for the library's own training cost. No absolute win-rate or return figures appear in the abstract.

### ★★ Fast Last-Iterate Convergence in Zero-Sum Markov Games with Bandit Feedback
- **Authors**: Yuheng Zhang
- **Affiliation**: **University of Illinois Urbana-Champaign** (`yuhengz2@illinois.edu`). Single author. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.05968 (5 Oct 2026) — `cs.LG`, `cs.GT`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.05968
- **Abstract and key innovations**: studies **last-iterate** convergence in unknown two-player zero-sum discounted Markov games with **bandit feedback** — the players learn independently along a single trajectory without observing each other's actions. The proposed **Adaptive Regularized TD Learning (ARTD)** achieves a $\widetilde{\mathcal{O}}(t^{-1/4})$ duality-gap bound for the *current* policies under a uniform hitting-time assumption, with high probability simultaneously over all rounds and starting states. This **improves the previous best $\widetilde{\mathcal{O}}(t^{-1/(9+\nu)})$ rate** (Cai et al., 2023) under the same feedback model. Two mechanisms do the work: **separating fast TD averaging from bounded value updates** to stabilize policy learning as values change, and **adapting log-barrier regularization to the progress of value estimation**. The algorithm requires no knowledge of the hitting-time bound, the horizon, or the confidence level.
- **Why it matters here**: bandit-feedback Markov games are the honest abstraction for **adaptive opponents in imperfect-information games with sparse payoff observation**, and last-iterate convergence is the version practitioners can actually deploy (average-iterate bounds certify the mean of all policies played, not the one you ship). Improving `1/(9+ν)` to `1/4` is a step change, not a constant, and the algorithm's parameter-free property is what makes it usable without an oracle.
- **Caveats**: the guarantee is **last-iterate under a uniform hitting-time assumption** — i.e. it holds only when every state is visited with bounded delay, which is a strong ergodicity requirement and is exactly what fails in sparse-reward games. The abstract states no experiments; this is a theory paper and **no game environment was run.**

### ★★ $Q$ Can Play That Game: Online Fitted $Q$-Iteration for Continuous-Action Zero-Sum Markov Games with Convex-Concave Function Approximation
- **Authors**: Kushagra Gupta, Jingqi Li, Cade Armstrong, Lasse Peters, Ross E. Allen, Ufuk Topcu, David Fridovich-Keil
- **Affiliation**: The University of Texas at Austin (Gupta, Li, Armstrong, Topcu), University of California, Berkeley (Peters), Massachusetts Institute of Technology (Allen). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.04010 (2 Oct 2026) — `cs.GT`, `cs.MA`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.04010
- **Abstract and key innovations**: finite-sample guarantees for zero-sum Markov-game $Q$-learning had been restricted to finite actions or to linear-quadratic (LQ) games, because the Bellman operator's inner **minimax problem need not admit a tractable saddle point**. The paper introduces a **class of neural-network $Q$-function approximators that is convex-concave in the players' actions**, guaranteeing that the inner minimax has a **pure-strategy saddle point**, then studies an **online fitted $Q$-iteration** in this class and proves — to the authors' knowledge — the **first finite-sample guarantees for non-LQ zero-sum Markov games with continuous states and actions.** Code is released.
- **Why it matters here**: continuous-action adversarial settings are under-served in this wiki's game-RL corpus relative to discrete board/Atari games, and this closes the gap that has kept theory out of continuous control games. The architectural device — *impose convex-concave structure on the function class so the inner game is solvable* — is more transferable than the specific bound.
- **Caveats**: **preprint, no experiments quoted in the abstract, no environment names.** "Convex-concave in the players' actions" is a real restriction on the representable $Q$-functions and its cost is not quantified. Code is at `github.com/CLeARoboticsLab/QCanPlayThatGame`.

### ★★ Who Bears the Burden? Learning Responsibility for Shared Constraints in Multi-Agent Reinforcement Learning (LiRA)
- **Authors**: Xiaoyang Cao, Jingqi Li, Zhe Fu, Alexandre M. Bayen
- **Affiliation**: Massachusetts Institute of Technology (Cao), The University of Texas at Austin (Li), Stanford University (Fu), University of California, Berkeley (Bayen). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.07491 (5 Oct 2026) — `cs.LG`, `cs.AI`. Comment: *"20 pages, 2 figures, 4 tables. Project page with code: https://lira-marl.github.io"*. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.07491
- **Abstract and key innovations**: when agents share a cost budget, a **single Lagrange multiplier** enforces the aggregate constraint but does not decide **how the penalty is allocated** — uniform penalties ignore reward heterogeneity, and agent-specific multipliers may still rely only on the shared aggregate signal. **LiRA learns each agent's share of a common multiplier by optimizing social welfare over a finite horizon**, enforcing the budget while redistributing its influence without modifying the original rewards or constraints. For convex games, varying the shares induces a **smooth family of normalized generalized Nash equilibria**; the paper derives a welfare gradient that **accounts for the induced change in the data distribution** (the changes to be optimized are non-stationary). Across **CityLearn, MABIM, Harvest, and MetaDrive** — 3 to 400 agents — LiRA improves average social welfare by **up to 29%** over uniform and agent-specific baselines, with costs kept within budget.
- **Why it matters here**: shared-constraint MARL is the cooperative-game analogue of team credit assignment, and the paper's sharp framing is that **the multiplier is a resource whose allocation is itself a decision**. `Harvest` is a genuine open-ended social-dilemma game, and the 3→400-agent span with a 29% welfare gain on a held budget is the strongest quantitative result in §1.
- **Caveats**: the equilibrium family and the welfare gradient are **guarantees for convex games**; the experiments include non-convex settings (driving, harvesting) where the theory does not apply and the paper does not claim it does. Preprint, unreviewed, single-run social-welfare improvements without seed variance in the abstract.

### ★ Fully Online Decentralized Learning in Stochastic Games with Unknown Independent Chains
- **Authors**: S. Rasoul Etesami
- **Affiliation**: **Department of Industrial and Systems Engineering, Coordinated Science Laboratory, University of Illinois Urbana-Champaign** (`etesami1@illinois.edu`). Single author. Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.01181 (1 Oct 2026) — `cs.LG`, `cs.GT`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.01181
- **Abstract and key innovations**: considers stochastic games with **independent controlled chains and unknown transition kernels**, where players observe only local states and realized payoffs. A **fully online, decentralized, uncoordinated mirror-descent algorithm in the dual space of occupancy measures** approximates stationary Nash-equilibrium policies using **a single transition/reward sample per primitive time step, local information only, no coverage of the joint state space, and no synchronized episodes.** Under uniform-ergodicity and finite-coverage assumptions, time-averaged fixed-comparator regret decays at **$O(T^{-1/2})$** (log factors and polynomial parameter dependence), with **complexity depending on individual cover times rather than the product state space** — avoiding exponential dependence on player count and state/action sizes. A coarse-correlated-equilibrium guarantee follows; under an additional global variational-stability condition the last iterate converges to a stationary $\epsilon$-NE.
- **Why it matters here**: the complexity bound is the contribution — **the exponent that normally kills multi-agent RL at scale is replaced by a per-player cover time**, which is the theoretical version of the scaling that deployed multi-agent games (large lobbies, many-agent environments) actually need. The paper is also honest that computing a stationary $\epsilon$-NE is **PPAD-hard**, so the achievable target is a coarse-correlated equilibrium unless extra structure is assumed.
- **Caveats**: **theory only, no experiments**; uniform ergodicity is a strong assumption; "independent chains" excludes exactly the interaction that makes games games (each player's transitions depend only on their own chain plus reward coupling). Single-author-paper; no venue.

### ★ Feedback Dominance Analysis for Pursuit-Evasion Games on Graphs
- **Authors**: Yue Guan, Daigo Shishika, Dipankar Maity, Michael Dorothy, Panagiotis Tsiotras
- **Affiliation**: Georgia Institute of Technology (Guan, Tsiotras — School of Aerospace Engineering); George Mason University (Shishika); University of North Carolina at Charlotte (Maity); US Army DEVCOM (Dorothy). Recovered from the arXiv HTML thanks block.
- **Venue**: arXiv:2610.06186 (5 Oct 2026) — `cs.GT`, `cs.MA`. Comment: **"7 pages, accepted at CDC 2026"** (IEEE Conference on Decision and Control).
- **Link**: https://arxiv.org/abs/2610.06186
- **Abstract and key innovations**: existing geometric characterizations of winning regions in pursuit-evasion games on graphs give only **sufficient** conditions and depend on **open-loop** strategies. The paper develops a **set-based dynamic programming** characterization of the pursuer's **winning and losing regions with necessary and sufficient conditions under worst-case (feedback) behaviour**, admits a **set-chasing** interpretation, and translates dominance sets into **real-time feedback strategies**. For states where neither player can guarantee victory it introduces an **instantaneous matrix-game formulation** with upper and lower bounds on the pursuer's winning probability. Simulations validate the dominance regions and the bounds.
- **Why it matters here**: pursuit-evasion on graphs is the canonical abstract game behind stealth/AI-for-strategy reasoning, and this is one of only **two featured papers this run with a peer-reviewed venue** (CDC 2026). Replacing sufficient open-loop conditions with necessary-and-sufficient feedback conditions is the structural upgrade; the matrix-game treatment of undecided states is a clean way to produce a *probability of winning* rather than a binary label.
- **Caveats**: 7 pages, `cs.GT`/`cs.MA`, discrete simultaneous-move games on graphs — **this is control-theoretic, not learning-based**; no agent is trained and no benchmark suite is used. The abstract reports validation but no quantitative comparison to prior geometric methods.

---

## §2 Game AI Bot — LLM-Powered Game Agents and NPC Intelligence

### ★★ Communication Shapes Collective Inference in Self-Adapting LLM Societies: Evidence from Mafia
- **Authors**: Haonan Huang, Joey Xiao
- **Affiliation**: **Princeton University** (Huang) and **New York University** (Xiao). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.05041 (4 Oct 2026) — `cs.MA`, `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.05041
- **Abstract and key innovations**: uses **Mafia** — an informed minority hiding in an uninformed majority whose only evidence is open play — as a testbed for when communication helps a group identify hidden adversaries. The **zero-information game** (each day's vote eliminates a random player) is **exactly solved** and scores every society, and **matched-casting comparisons** between protocols isolate the effect of communication. Societies of **8–100 `claude-haiku-4-5` agents** play **7,416 analyzed games (1.9M model calls)**, adapting by rewriting and inheriting private strategy notes. **Simultaneous broadcast beats silence in all nine compositions tested (8–46 players); turn-taking removes most of the advantage.** At 70 players, agents reading eight statements per day identify adversaries *worse than silent ones*; limited talk is worth less than at 46. Adaptation is fast but need not help: in first broadcast games citizens announce their role far more than mafia (**91% vs 30%**) and first-day votes find mafia at **3× chance**, but within two generations this cue fades — a change the inherited notes carry. In controlled 16-player redeployments, societies carrying **sixty generations of their own notes score below societies with none**.
- **Why it matters here**: this is a **negative-ish, mechanism-grounded result about multi-agent LLM communication** delivered at a scale (7,416 games, an exactly-solved baseline) that the earlier "LLM societies" papers in this wiki generally lack. The killer findings — that **turn-taking destroys the communication advantage**, that reading more statements can *hurt* at scale, and that **self-inherited strategy notes can actively degrade performance** — are direct evidence against the assumption that more communication and more memory are monotonically good for game agents. It belongs next to the wiki's growing thread that agent *memory accumulation* is not automatically beneficial.
- **Caveats**: **single model family** (`claude-haiku-4-5`) and a single social-deduction game; "identified adversaries" is a game-specific proxy for collective inference. Preprint, unreviewed, no venue. The 91%/30% role-announcement figures are one behavioural trace, not a general law — the paper itself frames the cue as transient.

### ★★ Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?
- **Authors**: Yibo Li, Jinhang Qiu, Zhi Zheng, Qianyun Guo, Jiaying Wu, Shuo Ji, Bryan Hooi
- **Affiliation**: **National University of Singapore** (`liyibo@u.nus.edu`, `bhooi@comp.nus.edu.sg`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.08215 (6 Oct 2026) — `cs.AI`. Project website: `liushiliushi.github.io/learn2play-bench-website/`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.08215
- **Abstract and key innovations**: existing agent benchmarks evaluate tasks whose rules are **given in the instructions or already familiar to pretrained models**, which makes it hard to separate *learning from interaction* from *reasoning with existing knowledge*. Learn2Play Bench is a suite of **newly designed text-based games with novel or counterintuitive rules**, so rules must be acquired through play; it provides reproducible feedback, automatic scoring, repeated attempts, and **instance variation** to test transfer. Three findings: (1) **Experience retention** — keeping **complete records of actions and feedback** beats summarizing them into rules or strategies; (2) **human-agent gap** — top human players reach higher peak scores, explore more varied strategies, and repeat actions less; (3) **harness matters** — holding the backbone fixed, changing the harness improves performance *while reducing estimated inference cost*.
- **Why it matters here**: this is a **benchmark about learning itself**, which is the right object for game agents — the paper correctly identifies that most "agent learns" claims are confounded by pretrained knowledge. Finding (3) is the most reusable: **harness changes move the score and cut inference cost simultaneously**, so architecture-of-the-loop is a first-class variable, not an implementation detail. Finding (1) directly contradicts the "summarize your experience into a rule" reflex common in memory-augmented agent designs.
- **Caveats**: **text-based games only** — the transfer to visual/action games is open, and the human comparison has an unspecified sample. Preprint, unreviewed. The abstract reports directions of effects, not effect sizes, datasets per game count, or model list.

### §2 coverage note
Real-time NPC behaviour and bot-detection work did not surface a featureable new arXiv paper in this window; the two Game-AI papers above are the lane's yield. The sibling `arxiv-daily.md` claims two additional game-agent papers this run would otherwise have featured — the **ten-hero MOBA Dyna loop** (`2610.08033`, §9.3) and **SpeedrunBench** (`2610.08076`, §9.3) — both noted there rather than duplicated here.

---

## §3 Game Foundation Models & World Models for Games

### ★★ CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching
- **Authors**: Shangye Song, Dong Gong, Hong Jia, Yun Sing Koh, Xinyu Zhang
- **Affiliation**: University of Auckland (Song, Jia, Koh, Zhang) and UNSW Sydney (Gong). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.08777 (6 Oct 2026) — `cs.CV`. Comment: *"18 pages. Project page: https://wrecklong.github.io/CtrlCache/"*. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.08777
- **Abstract and key innovations**: interactive video world models generate each chunk efficiently while responding to user controls, using **chunk-wise autoregressive generation with few-step denoising**; each chunk still needs several denoising iterations, and existing training-free caching policies decide reuse from **model-internal denoising dynamics, ignoring control transitions**. The paper observes that **controls for a chunk arrive before it is denoised**, so a schedule derived from them costs **no forward pass**. It finds that structural similarity drops around action changes while **low-frequency structure persists longer than high-frequency detail**, then proposes **control-aware caching** that labels each chunk **initial / transition / turning / steady** and reuses the transformer residual at one interior denoising step for turning/steady chunks, plus a **frequency-mixed history prior** reusing the preceding clean latent. On **Matrix-Game 2.0** and **LingBot-World v1/v2** it achieves **1.21×–1.41× DiT-backbone speedups without retraining** while *improving* WBench Overall over original inference on all three models.
- **Why it matters here**: interactive game world models are the infrastructure under AI-native games, and **latency is the deployment blocker**. This is a compute-reduction result that is (a) training-free, (b) uses the **control signal as a free scheduling oracle** rather than inspecting the denoiser, and (c) improves the quality metric rather than trading it away. The scarce-resource framing (spend denoising where controls change, cache where they do not) is the same move this wiki recorded for LLM serving, applied to game world models.
- **Caveats**: **preprint, and the speedups are on a DiT backbone, not end-to-end system latency** (the abstract does not fix the chunk size or the interaction loop overhead). WBench is a world-model benchmark and the improvement is relative to the model's *own* original inference, not to competing caching policies across models. No player-facing evaluation.

### §3 coverage note
Two additional game/world-model papers exist up-window and are recorded only as **pointers**: `2610.08033` (structured multi-agent MOBA world model trained with a continuous Dyna loop, sibling-claimed — §9.3) and `2610.08720` (WorldSolver, LLM agents generating physics solvers, sibling-claimed — §9.3). A generalist *game-playing foundation model* paper — the object this wiki's earlier digests tracked under "Game Foundation Models" — did **not** appear in this window; the nearest are world-model infrastructure rather than a unified game policy. Recorded as a **vacancy, not a claim of absence**.

---

## §4 Procedural Content Generation

### §4 coverage note — PCG is a recorded vacancy this window
No new directly-featureable PCG paper appeared in the swept window. The one strong candidate, **Recursive Game Creator** (`2610.08621`, an agentic four-role Designer/Builder/Player/Reviewer harness reporting **77.89 on GameCraft-Bench** and a **53.2% strict task success on GameASG-Bench, +34.1% over the same-model baseline**), is **sibling-claimed by `arxiv-daily.md`** and is therefore recorded in §9.3 rather than featured here. Two PCG-adjacent items surfaced in earlier digests and are not re-summarized: `2610.04253` Spec2Game (10-06 digest) and `2610.05033` Code2Games (10-06 sibling). **The PCG lane is genuinely thin this window**; recording it explicitly so a gap is not read as disinterest.

---

## §5 Game Benchmarks

### ★★★ PlaySuite: A Large-Scale Benchmark for Interactive Visual Intelligence
- **Authors**: Dheeraj Varghese, Anna Vettoruzzo, Walter Simoncini, Michelle Lorena Acevedo Callejas, Mohammad Mahdi Derakhshani, Kristof Meding, Joaquin Vanschoren, Cees G. M. Snoek
- **Affiliation**: University of Amsterdam (Snoek et al.), Eindhoven University of Technology (Vanschoren), Eberhard Karls Universität Tübingen (Meding). Recovered from the arXiv HTML author block.
- **Venue**: arXiv:2610.07127 (5 Oct 2026) — `cs.CV`, `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.07127
- **Abstract and key innovations**: a large-scale benchmark for **interactive visual intelligence** across **more than 5,000 open-source video games curated from PyWeek and itch.io**, spanning **Pygame, HTML5, Godot, and Unity**. The games are independent, largely **out-of-distribution** for current models, "reducing the likelihood that success can be achieved by retrieving memorized walkthroughs." To evaluate across heterogeneous titles it builds a **unified closed-loop interaction framework optimized for HPC clusters** and a **Video-LLM-as-a-judge protocol** that maps observable gameplay milestones to standardized progress levels. It evaluates **fourteen recent open models** (vision-language models, computer-use agents, vision-language-action models) and reports **strong evidence of a perception-action gap**: despite strong reasoning, models struggle to sustain progress and fail repeatedly on **spatial grounding, action execution, and self-correction**.
- **Why it matters here**: this is the largest interactive-game evaluation surface this wiki has recorded (**5K games**, four engines), and its design choices answer the two objections that have undercut every prior game-agent benchmark in the corpus: **contamination** (curated indie games, not commercial titles in pretraining data) and **heterogeneity** (one interaction framework across engines). The finding — a **perception-action gap** across all fourteen models — is the single most important negative result in today's digest, and the **Video-LLM-as-a-judge milestone protocol** is a reusable evaluation primitive.
- **Caveats**: **preprint, no peer review**, and the benchmark's validity rests on the judge protocol, which is itself a model (an unvalidated instrument at 5K-game scale). "Progress levels" are game-specific and the abstract does not report inter-judge agreement or human calibration. Fourteen models are all recent and open; no frontier closed models.

### §5 coverage note
Two further benchmarks are recorded elsewhere: **SpeedrunBench** (`2610.08076`, 9 games, strategy formation via speedrunning) and **Learn2Play Bench** (`2610.08215`, §2, text games about learning-to-learn) — both are sibling-claimed or cross-listed. `2609.32228` **CompusPlay** (rewarding a *proposer* for moving a solver) surfaced in the keyword sweep but predates the window and is not featured.

---

## §6 Industry Game AI — Game Development, Deployment, and Real-Time Inference

### ★★ Multi-Label Perceptual Bug Detection in Video Games using Deep Learning on Gameplay Footage
- **Authors**: Nahian Rifaat, Felix Morosov, Loutfouz Zaman
- **Affiliation**: Ontario Tech University, Oshawa, Canada (Rifaat, Zaman) and Universität Osnabrück, Germany (Morosov). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.08593 (6 Oct 2026) — `cs.LG`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.08593
- **Abstract and key innovations**: automated game QA via **multi-label perceptual bug detection from gameplay video**. The paper notes that few tools detect **multiple perceptual bugs in the same frame**, which is the real-world constraint. It proposes **ResNet-BiLSTM** for multi-label detection, compares against **I3D** and **3D ResNet**, reports **85.78% F1** on the benchmark dataset, and argues that **temporal-dependency modelling** is what makes video-based bug detection work. It also releases a **new dataset of 77,969 video clips (~1.2M frames)** spanning genres, with combinations of **5 bug classes in the same frame**.
- **Why it matters here**: this is the **game-dev / studio-tooling lane**, which is chronically under-represented relative to research environments despite being where game AI meets revenue. The dataset (77,969 clips, ~1.2M frames, multi-label) is itself the contribution, and the finding that **temporal modelling beats frame-level classification** is a concrete, checkable claim. It sits with the wiki's game-QA thread (the 10-06 CoG sweep's testing/regression papers).
- **Caveats**: **no venue**; F1 is on the authors' own new dataset, so it is not comparable across papers. "Perceptual bugs" is not formally defined in the abstract and the five classes are unspecified there. No deployment or cost-savings measurement.

### ★ Emoception: Selective Affective Layer Fine-Tuning of Video Vision Transformers for Player Arousal Change Recognition From Gameplay Footage
- **Authors**: Yi Xia, Ibrahim Khan, Mury Fajar Dewantoro, Wenwen Ouyang, Ruck Thawonmas
- **Affiliation**: **Ritsumeikan University, Osaka, Japan** (Graduate/College of Information Science and Engineering; `yi.xia@ice.ci.ritsumei.ac.jp`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.07603 (6 Oct 2026) — `cs.HC`, `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.07603
- **Abstract and key innovations**: proposes **Selective Affective Layer Fine-Tuning (SALFT)** for Video Vision Transformers on **player arousal change recognition from gameplay**. Instead of full fine-tuning, it selects which layers to adapt using the **L2-norm change in layer parameters after brief adaptation** — a representational-shift criterion rather than a gradient-based one. On the **Arousal Video Game AnnotatIoN dataset** with five-fold cross-validation, SALFT matches full fine-tuning with **no statistically significant degradation** ($p>0.05$) while updating **≈8% of parameters (>92% reduction)**; in one game it outperforms both full fine-tuning and the best baseline across all metrics and folds (exact two-sided Wilcoxon $p=0.0625$). It also traces attention for interpretability.
- **Why it matters here**: affect-aware game AI is the player-modelling side of the lane, and the **efficiency result (≈8% of parameters, no quality loss)** is the deployable claim — on-device player-state inference is a real console/edge constraint. The selection criterion (parameter-change norms) is a small, transferable parameter-efficient-tuning heuristic.
- **Caveats**: **single dataset**, and p-values from a 5-fold test are weak evidence; the one "outperforms" case is at the theoretical minimum p-value, i.e. the strongest possible result on the smallest possible test. Preprint, unreviewed. The abstract does not state how arousal labels were obtained or their reliability.

### ★ Near-Exact Computation of Independent Chip Model Placement Probabilities for Thousands of Players (DE-ICM)
- **Authors**: Wataru Inariba
- **Affiliation**: **GTO Wizard** (industry poker-solver vendor; `wataru@gtowizard.com`). Single author. Recovered from the arXiv HTML authors/thanks block.
- **Venue**: arXiv:2610.06028 (5 Oct 2026) — `cs.DS`, `cs.GT`. **No venue acceptance claimed.** (Dated "October 2026".)
- **Link**: https://arxiv.org/abs/2610.06028
- **Abstract and key innovations**: the **Independent Chip Model (ICM)** converts poker-tournament chip stacks into finishing-place probabilities and prize equities, and **exact computation has been regarded as intractable for large fields**. The paper presents **DE-ICM**, a deterministic algorithm computing all $n$ players' placement probabilities for all paid places in **$O(M n^2)$ time** ($M$ a fixed quadrature-node count) at accuracy near **double-precision**. It uses a classical integral representation in which, conditional on a player's exponential clock, the number of players ahead is **Poisson-binomial**; a **double-exponential quadrature on a single grid** with closed-form truncation-error bounds; and a stable **leave-one-out deconvolution in $O(n)$** from one shared product. On exactly solvable instances up to **4,000 players**, worst relative equity error is **$4.0\times10^{-14}$** and worst placement-probability error **$1.1\times10^{-14}$**; the full placement matrix for **1,000 players takes 0.2 s on one CPU core**. It notes the ICM is a **Plackett-Luce ranking model**, connecting it to other fields.
- **Why it matters here**: poker is the wiki's canonical imperfect-information game, and **real-time ICM equity is the number that tournament solvers and live-assistance tools need** — so a 1,000-player matrix in 0.2 s on one core is an industry-relevant systems result, not a numerical curiosity. The **Plackett-Luce identification** is the conceptual bridge that makes the method reusable beyond poker (ranking models generally).
- **Caveats**: **self-published by a solver vendor** (GTO Wizard) with **no peer review**, so the two-sided incentive is the same one this wiki flagged for the 10-06 `Patrick` whitepaper. Accuracy is verified on *exactly solvable* instances, not on real tournament fields. Single author.

---

## §7 Related Techniques — Self-Play, Game-Theoretic RL, and Interpretability

### ★★★ BluffJAX: Adversarial Imperfect Information Games in JAX
- **Authors**: Aryaman Reddi, Jan Peters, Carlo D'Eramo
- **Affiliation**: Department of Computer Science, TU Darmstadt, and Hessian Center for Artificial Intelligence (Hessian.ai), Germany; Peters additionally at the German Research Center for Artificial Intelligence (DFKI). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.07686 (6 Oct 2026) — `cs.AI`. Correspondence: `aryaman.reddi@tu-darmstadt.de`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.07686
- **Abstract and key innovations**: an **open-source suite of adversarial imperfect-information games in JAX** with **canonical implementations designed for high simulation throughput and parallelization on GPU accelerators**. It covers well-studied benchmarks (**Texas Hold'Em Poker, Kuhn Poker**) plus **games not previously studied in RL research** — **Bluff, Stud Poker, and Kemps**. It benchmarks **throughput and memory in single- and multi-GPU settings, demonstrating scaling of up to hundreds of millions of samples per second**, and provides baseline results for **reinforcement learning, tree search, and game-solving algorithms in JAX**.
- **Why it matters here**: this is the **infrastructure paper of the run** and it is the game-RL analogue of the 2026-10-06 digest's `Factoriax`: a throughput argument whose number (hundreds of millions of samples/s) moves imperfect-information RL from "run overnight" to "sweep hyperparameters." Its second contribution is more interesting than the first: by including **Bluff, Stud, and Kemps**, it admits the field has been benchmarking on a tiny canonical set (Kuhn, Leduc, HULHE) and offers **new mechanics** for game-theoretic RL — the same "saturation-resistant benchmark" logic that makes SpeedrunBench valuable.
- **Caveats**: **preprint, no venue, and throughput is hardware-specific** (the abstract does not name the GPU). "Hundreds of millions of samples per second" is a peak, not an end-to-end training number. The paper is a benchmark/tooling release, so it does not itself advance a method.

### ★★ Learning Explainable Representations of Complex Game-playing Strategies
- **Authors**: Abhijeet Krishnan, Colin M. Potts, Arnav Jhala, Harshad Khadilkar, Shirish Karande, Chris Martens
- **Affiliation**: North Carolina State University (Krishnan, Potts, Jhala, Martens); Indian Institute of Technology Bombay (Khadilkar); Tata Research Development and Design Centre, Pune (Karande); Northeastern University, Khoury College of Computer Sciences (Martens). Recovered from the arXiv HTML author block.
- **Venue**: arXiv:2610.07638 (6 Oct 2026) — `cs.AI`, `cs.LG`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.07638
- **Abstract and key innovations**: motivated by how human players form **abstractions for concepts and strategies** to explain others' actions and inform their own. The paper trains RL agents to **synthesize learned strategies and policies as executable procedures** from sequences of gameplay actions, and presents methods to **automatically learn such programs for chess and for a grid-based environment**. The learned strategies produce effective actions and can be learned from gameplay data.
- **Why it matters here**: this is the same group and the same research programme as `2610.07640` (sibling-claimed, §9.3) — turning game agents into **executable symbolic procedures** rather than opaque policies — and it is the strongest interpretability thread in today's §7. The reframe is that explanation is an **artefact you compile**, learned from gameplay, not a post-hoc saliency map. That is a materially different and more testable claim than the probing literature the wiki has been recording.
- **Caveats**: **preprint, and the abstract reports no quantitative results** — no win-rate or fidelity figure, no comparison baseline, no human study. "Effective actions" is unquantified. Chess + one grid environment are both small.

### ★ The Complexity of Computing Nash Equilibria in Colonel Blotto Games
- **Authors**: Vasilis Pollatos, Andreas Kontogiannis
- **Affiliation**: National and Kapodistrian University of Athens and Archimedes, Athena Research Center, Greece (Pollatos); Archimedes, Athena Research Center, Greece and National Technical University of Athens (Kontogiannis). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.05956 (5 Oct 2026) — `cs.GT`, `cs.CC`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.05956
- **Abstract and key innovations**: studies Nash-equilibrium computation in **discrete Colonel Blotto games**. For two-player general-sum Blotto with monotonic piecewise-constant battlefield payoffs, it shows that **computing an inverse-polynomial approximate Nash equilibrium is PPAD-hard even with only two battlefields and a constant number of pieces per battlefield**, resolving an open question; the hardness persists with more battlefields; a multiplayer PPAD-membership theorem yields **PPAD-completeness**. It then identifies a **tractable frontier**: if the social payoff has **rank-$r$ structure**, an $\epsilon$-NE can be computed in time polynomial in budgets, battlefields, and $1/\epsilon$ **for every fixed $r$**. For multiplayer winner-takes-all Blotto it uncovers a **sharp tie-breaking frontier** — with full value to every highest bidder a pure NE is polynomial, while under equal splitting among highest bidders approximate NE is **PPAD-hard even with five players**, resolving an open question of Bichler and Ghosh.
- **Why it matters here**: Colonel Blotto is a canonical resource-allocation game, and the **rank-$r$ tractability frontier** is the useful part — it tells you *which* Blotto instances are learnable-at-scale versus which are computationally out of reach, which is exactly the map game-RL practitioners need when choosing an environment. The five-player hardness is a sharp, memorable impossibility.
- **Caveats**: **theory only, no experiments, no venue**. PPAD-hardness is about exact/inverse-polynomial approximation and does not preclude heuristic RL from finding good strategies on instances of interest.

### ★ Forming Alliances in the Fog of War: A General Lotto Perspective
- **Authors**: Edik Hakobyan, Vade Shah, Jason R. Marden
- **Affiliation**: **Department of Electrical and Computer Engineering, University of California, Santa Barbara** (all three; `edikh7606@gmail.com`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.00608 (30 Sep 2026) — `cs.GT`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.00608
- **Abstract and key innovations**: studies **alliance formation under uncertainty** in the **coalitional General Lotto game**, where two players compete against a shared adversary by allocating budgets over separate sets of valued contests. When budgets are known, a **budget transfer from one ally to the other can benefit both**. The paper asks whether this survives when players know budgets only **up to a multiplicative factor**, under two uncertainty models (about the adversary's budget, and about each other's). It characterizes **exactly which games admit a transfer that benefits both players in every game consistent with what they conjecture**, and shows that **such robust transfers exist in a positive-measure set of games for every level of uncertainty** — alliances remain worthwhile even when allies are "largely in the dark."
- **Why it matters here**: robustness of cooperative commitments under partial information is the strategic-game version of the partial-observability that every game agent faces, and "**positive measure for every uncertainty level**" is the right kind of guarantee — not "works when information is good" but "there is always a non-trivial set where it works." It pairs with §1's LiRA, which also studies how to allocate a shared resource across cooperating agents.
- **Caveats**: **theory only, no experiments, no venue**. The "alliance" is a budget transfer in a stylized game; the mapping to actual coalition behaviour in deployed multiplayer games is asserted, not shown.

### ★ Arbitrarily Slow Polynomial Convergence of Fictitious Play
- **Authors**: Jacob Abernethy, John Lazarsfeld, Andre Wibisono
- **Affiliation**: Georgia Institute of Technology (Abernethy, Lazarsfeld) and Yale University (Wibisono); Abernethy also Google Research. Recovered from the arXiv HTML front matter.
- **Venue**: arXiv:2610.08768 (6 Oct 2026) — `cs.GT`. **No venue acceptance claimed.** (Dated "October 6, 2026".)
- **Link**: https://arxiv.org/abs/2610.08768
- **Abstract and key innovations**: proves that **fictitious play can converge at arbitrarily slow polynomial rates in two-player zero-sum games**. For every integer $k\ge2$ it constructs a payoff matrix with $(k+1)^2-5$ actions per player for which the duality gap decays as $\Theta(t^{-1/k})$. The family starts from **rock-paper-scissors** and builds higher-order games recursively, with every best response unique after a prescribed initial action. For $k\ge3$ these are **counterexamples to Karlin's conjectured $O(t^{-1/2})$ convergence rate**, extending the recent $\Theta(t^{-1/3})$ construction of Wang (2025) to arbitrary polynomial rates.
- **Why it matters here**: fictitious play is the ancestor of every regret-matching / CFR-style solver used on poker and imperfect-information games, so a **lower-bound construction that reaches any polynomial rate** is a foundational limit result for that whole family. The recursive rock-paper-scissors construction is elegant and reusable as a stress test: **do not expect a universal convergence rate from FP-style methods.**
- **Caveats**: **theory only, no experiments, no venue**; the constructions have $(k+1)^2-5$ actions, so for large $k$ the counterexamples are large games — the result says the *worst case* is arbitrarily slow, not that typical games are.

### ★ Stochastic Gradient Descent Ascent is Suboptimal for Nonconvex-PL Min-Max Games
- **Authors**: Junsoo Ha
- **Affiliation**: **not printed** — single author, contact `junsoo.ha.contact@gmail.com`, no institutional address in the paper. **(no affiliation available)**
- **Venue**: arXiv:2610.07814 (6 Oct 2026) — `stat.ML`, `cs.GT`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.07814
- **Abstract and key innovations**: asks how far **stochastic gradient descent ascent (SGDA)** can go in **nonconvex min-max games** by tuning timescale ratio and step sizes. For $\ell$-smooth nonconvex-PL games with inner $\mu$-PL inequality, it proves a complexity **lower bound $\Omega(\kappa^2\ell\epsilon^{-2}+\kappa^4\ell\sigma^2\epsilon^{-4})$** (condition number $\kappa=\ell/\mu$, variance $\sigma^2$), **matching existing SGDA upper bounds** and establishing a **complexity separation from Smoothed-AGDA** (Yang et al., 2022). It also shows SGDA **can fail to find a stationary point when its timescale ratio is as small as $o(\kappa^2)$**.
- **Why it matters here**: min-max optimization is the training algorithm under adversarial/self-play game RL, and this is a **tight lower bound** — the standard optimizer is provably not optimal, and the paper identifies the timescale ratio below which it actually breaks. As with the fictitious-play result, this is a limit result that constrains what to expect from the default tool.
- **Caveats**: **theory only, no experiments; single author with no affiliation; no venue.** The separation is from one specific competitor (Smoothed-AGDA), not a claim that no method does better.

---

## §8 Cross-Cutting Observations

1. **The frontier was real, and the previous saturation verdict is fully reversed (again).** The 10-06 digest declared the `2610.*` `/new` block idle and deferred `2610.03718`–`2610.06900`. Today's API sweep shows that band and the band above it are full of unreviewed game work — **17 featureable papers**, of which **6 are squarely in the core Game-RL lane** and **2 carry peer-reviewed venues** (CDC 2026). The lesson repeats the 10-05→10-06 lesson: **the `/new` announcement ceiling under-reports supply; query the export API by category and date.**
2. **★ Sibling collisions are now the dominant dedup risk, not stale baselines.** Five papers were claimed *during* this run by a same-directory sibling written at 11:19. This is the **fifth collision in seven days** and the **second consecutive same-directory one**. The operational fix is unambiguous: **sibling jobs sharing an announcement window must serialize, or snapshot the claimed-ID set at a shared instant.** ID-level dedup alone passed all five.
3. **Game-theoretic RL theory had a strong day.** Three of the seven §7 entries are limit results — **fictitious play's arbitrarily slow convergence**, **SGDA's suboptimality in nonconvex-PL games**, and **Colonel Blotto's PPAD-completeness** — plus two convergence/equilibrium papers in §1. The through-line is that the **default tools of adversarial game learning (FP, SGDA, uniform multipliers) all have now-proven ceilings**, and the constructive papers in §1 (RLBO, LiRA, convex-concave $Q$) are responses to exactly those ceilings.
4. **The best game-agent result is a negative one.** PlaySuite's **perception-action gap** across fourteen models — strong reasoning, weak sustained interaction, recurring failures in spatial grounding, action execution, and self-correction — is the single most consequential finding of the run, and it is a *benchmark* finding, not a method finding. This matches the wiki's 10-06 conclusion that **an instrument-critique paper outranks a method paper with a better number.**
5. **Communication and memory are not free.** The Mafia study is the day's second negative cluster: **turn-taking destroys the broadcast advantage, more statements can hurt at scale, and inherited strategy notes can actively degrade a society.** Together with Learn2Play's finding that **full experience records beat summarized rules**, this cuts against the reflexive "add memory, add communication" design pattern in multi-agent LLM agents.
6. **Infrastructure and efficiency is where the reusable wins are.** **BluffJAX** (hundreds of millions of game samples/s, new imperfect-information mechanics) and **CtrlCache** (control-aware caching, 1.21×–1.41× with *improved* quality) are both throughput/latency arguments whose value survives outside their own results. Same pattern the wiki recorded for `Factoriax` and the LLM-serving literature: **make the iteration loop cheap, then sweep.**
7. **Game-dev / industry is a real lane but a self-published one.** The three §6 entries are respectively **academic tooling** (Ontario Tech + Osnabrück bug detection, with a 77,969-clip dataset), **player modelling** (Ritsumeikan arousal recognition at ≈8% of parameters), and **vendor research** (**GTO Wizard** DE-ICM). Only the first is obviously neutral; the third carries the two-sided-incentive caveat this wiki flagged for the 10-06 `Patrick` whitepaper. **Industry game-AI results in this corpus are systematically unreviewed and should be read as claims, not findings.**
8. **No result in this digest was independently replicated, and none replicated by a second group.** Only `2610.06186` (CDC 2026) carries a peer-reviewed venue among the 17; the remaining 16 are unreviewed preprints.

---

## §9 Contradictions, Venue Updates, and Sibling Collisions

### 9.1 Contradictions
- **No direct contradiction of a 10-06 claim was found.** The 10-06 digest's statement that the `/new` block was idle is *not* contradicted — it was true of `/new` and scoped there; this run's own §8.1 confirms the export API frontier was the real one. The correct reading is the one the 10-06 report itself gave: **the saturation verdict was scoped to the `/new` channel, and the export API reverses it.**
- **Within this report**: **LiRA** (§1) claims a smooth family of *normalized generalized Nash equilibria* as responsibility shares vary, while **Colonel Blotto** (§7) proves **PPAD-hardness** for equilibrium computation in a related resource-allocation game. These do not conflict — Blotto hardness is about *exact/inverse-polynomial* computation on specific piecewise-constant payoffs, LiRA's family is for *convex* games with standard regularity — but the juxtaposition is worth recording, because it delimits where each applies.

### 9.2 Venue updates
- `2610.06186` — **accepted at IEEE CDC 2026** (peer-reviewed; the only such venue among the 17 featured).
- No CoG 2026/2027 proceedings were re-fetched this run (the 10-06 digest covered `cog2026.org` thoroughly; IEEE Xplore proceedings are still pending, expected ~2026-10-16).

### 9.3 Sibling-claimed papers (withdrawn from §§1–7, not re-summarized)
Five IDs were selected and then found claimed mid-run. All are recorded here with a cross-reference; **this report does not restate the sibling's findings as its own.**

| arXiv ID | Title | Claimed by | Why it belonged here |
|---|---|---|---|
| `2610.08033` | Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA | `synthesis/2026-10-07/arxiv-daily.md` (+ `arxiv-paper-check.md`) | Multi-agent MOBA structured world model + continuous Dyna loop; **70.2% real win rate** (421/600) up from 0% dream-only — this run's strongest Game-RL candidate. |
| `2610.08076` | SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning | `synthesis/2026-10-07/arxiv-daily.md` (+ `arxiv-paper-check.md`) | Game-agent benchmark over **9 games**; strategy formation via speedrunning. |
| `2610.08621` | Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness | `synthesis/2026-10-07/arxiv-daily.md` | This run's PCG candidate; **77.89 GameCraft-Bench**, **53.2% GameASG-Bench** (+34.1% over same-model baseline). Branches to §4. |
| `2610.08720` | WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation? | `synthesis/2026-10-07/arxiv-paper-check.md` | World-model / LLM-agent benchmark (168 tasks, 7 physics domains); nearest §3 filler. |
| `2610.07640` | Towards the Automatic Synthesis of Interpretable Chess Tactics | `synthesis/2026-10-07/arxiv-daily.md` | Chess interpretability via ILP-derived symbolic sub-policies; companion to `2610.07638`. |

### 9.4 Coverage gaps declared
- **The export API's `submittedDate` frontier is `2026-10-06`**, so this is a single-day announcement block; papers submitted 2026-10-07 are not yet indexed and are not covered.
- The category sweeps are `max_results=200` per category and thus **not exhaustive for older windows**; band `2609.20xxx`-relative backfill is limited to what the six feeds returned and what the targeted keyword sweeps surfaced.

### 9.5 Name-collision and attribution notes
- `2610.07640` (chess tactics) and `2610.07638` (explainable strategies) share authors **Abhijeet Krishnan and Chris Martens** — the sibling records them as separate papers, and they are: the first is a symbolic chess sub-policy model derived from Inductive Logic Programming (PAL), the second a program-synthesis method for gameplay strategies across chess and a grid world. They are not duplicate IDs.
- `2610.06028` is authored by **Wataru Inariba** with an explicit **GTO Wizard** address; the wiki's 10-06 digest featured `2603.23660` (GTO Wizard Benchmark) by a different GTO Wizard team. **Same org, different paper, different authors** — record carefully.
