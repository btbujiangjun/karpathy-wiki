---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-21)"
type: synthesis
created: 2026-10-21
updated: 2026-10-21
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent-rl, industry, real-time, vlm, daily-digest]
sources: [arxiv.org, openreview.net]
---

# Game RL & Game AI Bot — Daily Digest (2026-10-21)

Covers 7 categories: Game RL, Game AI Bot, Game Foundation Models / World Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and Related Techniques (self-play, exploratory & multi-agent RL, game theory, imitation).

> **Run note.** Wednesday fresh sweep. The arXiv **export API was hard-429** the entire session (`/api/query` returned `429 Too Many Requests` on every attempt), so metadata was gathered via the `arxiv.org/search` HTML interface (25 topical queries, all computed on title+abstract) and the `arxiv.org/list/{cat}/recent` browse pages, then a full abstract-page scan of the `cs.LG/cs.AI/cs.CL/cs.CV/cs.MA/cs.GT/cs.NE` recent listings (`2610.10xxx`–`2610.286xx`). **11 papers featured, all grep-verified absent from the entire `wiki/` tree:** 6 **new-to-wiki** featured papers + 1 late-posting cross-confirm + 3 game-theory items + 1 closely related item. Deduped against the four same-day siblings [`arxiv-daily`](../2026-10-21/arxiv-daily.md), [`arxiv-ai-search`](../2026-10-21/arxiv-ai-search.md), [`arxiv-paper-check`](../2026-10-21/arxiv-paper-check.md) and [`conference-digest`](../2026-10-21/conference-digest.md), and against the exhaustive Tuesday digest [`game-rl-daily` 2026-10-20](../2026-10-20/game-rl-daily.md). Affiliations stated only where declared or unambiguously inferable from author list — never invented.

---

## 1. Game RL — Reinforcement Learning in Games

### Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations (ORBiT)
- **Authors**: Cedric Derstroff, Jannis Blüml, Janosch Moos, Michael Girstl, Zihan Ye, Debora Clever, Kristian Kersting
- **Affiliation**: — (TU Darmstadt / Hessian AI lineage per on-paper conventional tiers; not declared on abs page)
- **Venue**: arXiv preprint, 20 Oct 2026 (cs.LG, cs.AI)
- **Link**: https://arxiv.org/abs/2610.28197
- **Abstract**: Object-centric RL agents typically receive each object's position in a **fixed global frame**, even though their decisions depend on where objects are relative to one another. This forces the agent to relearn the same response at every location, and performance collapses under a mere scene shift. The paper proposes **Object-Relative Coordinates fixed to Anchor (ORCA)** — describing entities in a relative frame — operationalized via **Object-Relative inductive-Bias Transformers (ORBiT)**, a transformer for anchor-relative inputs in RL.
- **Key innovations**: (i) Relative representations beat absolute ones for both MLP and transformer agents; (ii) ORBiT beats pixel-based PPO with an aggregate **HNS IQM > 1.0 over 13 Atari games**; (iii) learns **Foosball from scratch, dominating all baselines**; (iv) in a controlled Tag environment ORCA extends to rotations, generalizes to unseen distractors, and the gain **requires a decision-relevant anchor**.
- **Status**: **new-to-wiki**, featured.

### Bandit and RL theory for games — see §7 for the three 2026-10-18/19 game-theory entries
Turn-based deterministic game complexity results (Mean-Payoff Games strategy recovery, poset games) are grouped under §7 Related Techniques to keep §1 focused on learning-based game RL.

## 2. Game AI Bot — LLM/VLM Game Agents, NPCs, Play

### ROAR: Benchmarking LMM Agents under Real-Time Constraints in Multiplayer Action-Shooter Games
- **Authors**: Dawei Wang, Di Zhao, Jianran Yu, Chengming Zhou, Marci Chi Ma, Xiaoyang Liu, Beining Zhang, Shuliang Chu, Yun Sing Koh, Gary Ushaw, Richard Davison
- **Affiliation**: — (Newcastle University / Auckland lineage per author list — not declared cumulatively on abs page)
- **Venue**: **NeurIPS 2026** (stated in comments); arXiv 20 Oct 2026 (cs.MA)
- **Link**: https://arxiv.org/abs/2610.24282
- **Abstract**: Most LMM-agent benchmarks in multi-agent settings are **turn-based**: the environment and other agents pause while an agent performs inference, hiding the fundamental **real-time** challenge where the world keeps evolving and delayed decisions arrive stale. ROAR is a **multiplayer action-shooter game environment** for evaluating LMM agents under real-time constraints, spanning **cooperative, competitive, mixed cooperative-competitive, and single-agent** scenarios.
- **Key innovations**: (i) A **Multi-Agent Asynchronous Gym interface** that decouples environment evolution from agent reasoning by running environment and each agent in **separate threads**, so the world advances on a fixed clock and agents reason without blocking one another; (ii) easy deployment, **multimodal observations**, and customizable levels; (iii) a practical testbed moving LMM-agent evaluation **beyond static turn-based protocols toward real-time multi-agent decision-making**.
- **Status**: **new-to-wiki**, featured.

### KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses
- **Authors**: Zhikang Chen, Yueqing Sun, Sen Cui, Ziang Ye, Yu Wang, Yan Feng, Xierui Song, Yu Zhang, Tingting Zhu
- **Affiliation**: —
- **Venue**: arXiv preprint, 19 Oct 2026 (cs.AI, cs.CV)
- **Link**: https://arxiv.org/abs/2610.27417
- **Abstract**: A failed gaming trajectory shows that an agent *needs* intervention but not *how its harness should change*. Effective harness adaptation needs **diagnostic evidence**, not just alternative recovery rules. **KPHarness** adapts the external execution harness of a **frozen vision-language-action model** through **knowledge-probing co-evolution**: recovery knowledge supplies context-specific intervention hypotheses that guide **active probing**; probe outcomes reveal when hypotheses apply and refine both the recovery knowledge and later probe selection.
- **Key innovations**: (i) Reciprocal loop improving *which* interventions to apply **and how the harness investigates failures**; (ii) separates fast policy execution from a **slow research loop** producing bounded, sandbox-matched harness revisions accepted only on paired-improvement evidence; (iii) validated recoveries are retained for **cross-task reuse**; (iv) experiments on **Minecraft** (mining, combat, crafting) show improved task coverage over bare policy, a fixed harness, and knowledge-only evolution, with gains holding on **unseen tasks** with the bank/probing policies frozen.
- **Status**: **new-to-wiki**, featured.

### ECHO: Learning Epistemically Adaptive Language Agents with Turn-Level Credit
- **Authors**: Abhijnan Nath, Sifatul Anindho, Nikhil Krishnaswamy
- **Affiliation**: —
- **Venue**: arXiv preprint, announced 20 Oct 2026 (older arXiv number `2606.29745`; late-posting / cross-list) — **new-to-wiki this run**
- **Link**: https://arxiv.org/abs/2606.29745
- **Abstract**: Effective multi-turn agents must decide **what information to seek, how to use new evidence, and when they are certain enough to act**. Introduces **Epistemic Decision Processes (EDPs)**, a belief-state formulation of multi-turn information seeking where actions produce observations that update a posterior over a latent task variable, making **epistemic adaptivity** explicit (good policies pick actions useful under the *current belief*, not merely those correlating with success). **ECHO** (Epistemic Credit for History-Conditioned Optimization) is a clipped policy-gradient objective assigning **turn-level credit via posterior-sensitive rewards**.
- **Key innovations**: (i) EDP belief-state framing of multi-turn seeking; (ii) turn-level epistemic credit beating trajectory-level GRPO on resolution, information gain, and efficiency; (iii) two testbeds — the **Clue Selector Game** (controlled evidence-seeking benchmark) and **CRAFT** (multi-agent coordination game) — with matching or exceeding frontier baselines on grounding, recovery, and calibration.
- **Status**: **new-to-wiki**, featured (announced this window).

### Teaching an AI Agent to Play Poker Strategically Through Preference Optimization (SPOKE)
- **Authors**: Phurinat Polasa, Thanapon Thanadunpremdet, Phatthanasak Kraiduang, Saksorn Ruangtanusak
- **Affiliation**: —
- **Venue**: **IEEE iSAI-NLP SRW 2026** (stated in comments); arXiv 19 Oct 2026 (cs.AI)
- **Link**: https://arxiv.org/abs/2610.27028
- **Abstract**: A poker agent can make a **legal** move and still a **strategically poor** one. Asks whether compact agents can exhibit strategic behavior under hidden information and whether **preference optimization** improves beyond static/zero-shot policies. Static baseline and three frozen LMs (SmallThinker, Qwen3, Gemma-3) vary substantially between exact-game and six-player evaluation. Proposes **Strategic Preference Optimization with KL-anchored Equilibrium (SPOKE)**: teacher-relative value penalties, policy anchoring, risk constraints, and structured rationale supervision; compared against SFT, DPO, GRPO, and GSPO.
- **Key innovations**: (i) SPOKE achieves lowest mean **exploitability** in Kuhn (0.213) and Leduc (1.081) and highest six-max top-1 agreement (0.775) over 3 runs of a SmallThinker-4B-A0.6B policy; (ii) **preserves teacher KL comparable to SFT** (0.522 vs 0.523) — strategic quality without drifting off the teacher's behavior.
- **Status**: **new-to-wiki**, featured.

## 3. Game Foundation Models & World Models

### Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds
- **Authors**: Jihai Zhang, Runjia Qian, Kaiqin Kong, Biao Jiang, Puyi Wang, Siru Chen, Tianle Li, Guanjie Chen, Junyi Wu, Chubin Chen, Yuanhang Li, Kaichen Huang, Haobo Zhang, Yangguang Li (and others; Skywork/Matrix-Game team)
- **Affiliation**: — (Matrix-Game project — Skywork AI lineage from earlier releases; not declared on abs page)
- **Venue**: arXiv preprint, 20 Oct 2026 (cs.CV); Project page + code + models released
- **Link**: https://arxiv.org/abs/2610.27999
- **Abstract**: Moving from controllable videos to **genuinely playable worlds** needs **persistent world state, executable game rules, and low-latency interaction**. Outlines a roadmap for next-gen Matrix-Game that **separates game execution from visual generation** via an **executable game harness**, and presents **Matrix-Game 4.0** as the first system on this design: a lightweight **game engine** maintains world state and executes interaction rules; a **multimodal coding agent** translates player ideas into game code and dynamic scene captions; an **autoregressive video renderer** turns engine-rendered low-poly proxies into detailed visuals, conditioned on dynamic captions and memory references.
- **Key innovations**: (i) Engine/renderer separation gives **continuous guidance** for visual generation and enables **natural-language creation and modification** of scenes and gameplay; (ii) renderer trained on aligned low-poly/high-fidelity pairs and distilled into a **causal generator producing 4-frame chunks in 1–2 denoising steps**; (iii) **480p @ 60 FPS on a single RTX 5090** with **key-press-to-display latency 112 ms**; single-step generation hits **83 FPS steady-state** at 18.2 GiB peak GPU memory, and 67/58 FPS on RTX 5080/5070 Ti; (iv) demonstrates customizable shooter and driving games with engine-enforced mechanics.
- **Status**: **new-to-wiki**, featured.

### ActionRoPE: Action as Coordinates for Spatially Consistent Control in Planar-Camera Game World Models
- **Authors**: Zhiyang Deng, Yuzhe Wu, Zijun Lin, Yeying Jin
- **Affiliation**: —
- **Venue**: arXiv preprint, 20 Oct 2026 (cs.CV); Project page released
- **Link**: https://arxiv.org/abs/2610.25861
- **Abstract**: Action control in game world models is still mostly **feature conditioning**, leaving the model to *learn* how each action moves the visual world — a poor match for **planar-camera worlds** (top-down, isometric) where player motion induces a **geometrically well-defined planar camera displacement**. Proposes **ActionRoPE**, a **parameter-free action interface** converting action-driven camera displacement into **world-coordinate rotary positions**, so tokens for the same world location keep the same positional address over time.
- **Key innovations**: (i) This exposes a **spatial asymmetry** — regions seen in the initial observation are geometrically known while revealed regions must be synthesized — motivating **Coordinate-Conditioned Noise Scheduling (CNS)** with token-wise denoising schedules; (ii) observed regions stabilize earlier, new content is generated in reference to them; (iii) **reduces revisit drift by 66%** over the strongest of four action-conditioning baselines and follows commanded motion more faithfully; (iv) the **same interface transfers across video backbones from 1.3B to 33B parameters** and to out-of-distribution scenes.
- **Status**: **new-to-wiki**, featured.

### SolarRenderer: Few-Step Generative Reference Rendering (structure-conditioned video renderer for game-engine output)
- **Authors**: Guian Fang, Shengju Qian, Dongyue Lu, Junchao Huang, Lutao Jiang, Xin Wang, Yiren Song, Li Jiang, Mike Zheng Shou
- **Affiliation**: — (incl. Mike Zheng Shou — Show Lab, NUS, per established identity; not declared on abs page)
- **Venue**: arXiv Technical Report, 20 Oct 2026 (cs.CV)
- **Link**: https://arxiv.org/abs/2610.28630
- **Abstract**: Game engines and coding agents can specify a scene's layout, motion, and camera, but turning that coarse structure into realistic video needs a renderer that **follows the structure and completes the appearance it leaves open**. Existing renderers are tied to one engine's representation, need tens of denoising steps, and learn from conditions unaligned with target videos. **SolarRenderer** adapts a **frozen MiniMax-H3 33B backbone with two lightweight LoRAs**: structural videos enter the backbone's **native reference pathway** at the frames they describe, with **no type identifier**, described only in plain text, so **one control LoRA follows arbitrary structural representations**.
- **Key innovations**: (i) Structure-guided distribution matching renders in **4 steps, 12.3× faster than 50-step sampling**, preserving learned control; (ii) a **block-causal variant extends to streaming** and renders **768p video in real time**; (iii) trained on a **frame-aligned corpus of 136K clips** from game engines, simulators, and YouTube; (iv) SOTA on both in-distribution and a **16-representation generalization benchmark**, generalizing to **11 unseen representations** (pose skeletons, drawings, point clouds).
- **Status**: **new-to-wiki**, featured (industry-adjacent rendering line — placed here, not §6).

## 4. Procedural Content Generation

### InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation
- **Authors**: Yi-Chuan Huang, Hao-Jen Chien, Zheng-Hui Huang, Yu-Lun Liu, Kaipeng Zhang, Zhixiang Wang
- **Affiliation**: —
- **Venue**: arXiv preprint, 20 Oct 2026 (cs.CV); Project page released
- **Link**: https://arxiv.org/abs/2610.26853
- **Abstract**: Procedural generation is key to synthetic-data creation and game development (controllability, editability, diversity), but **VLM-based code generation produces simple 3D assets** while sophisticated photorealistic procedural systems need heavy manual development, and existing VLM-guided methods stay bounded by **predefined factories and APIs**. InfiniDream is a **VLM-driven framework for open-ended procedural 3D world generation**.
- **Key innovations**: (i) **Symbolically Constrained Asset Generation** leverages existing procedural algorithms to create **novel photorealistic assets** while preserving editability and **seed-based diversity**; (ii) an end-to-end **text-to-world pipeline** combining semantic scene planning with **Deterministic Frustum-Guided Grid Placement** for large-scale worlds with precise placement, procedural population, and animation; (iii) gains across four perceptual metrics on 100 object + 20 scene tasks, plus diversity analysis, ablations, and human preference evaluation.
- **Status**: **new-to-wiki**, featured.

### CEGame-Bench: From Code to Playable Systems — Long-Horizon Game Creation Agents
- **Authors**: Zixuan Dong, Yanghai Wang, Hanyan Bian, Jiaxi Tao, Junze Li, Jiadong Wang, Xinyu Che, Lin Liu, Baoyun Peng, Xiaodong Wang, Jiaheng Liu
- **Affiliation**: —
- **Venue**: arXiv preprint, 19 Oct 2026 (cs.AI, cs.SE); 27 pages
- **Link**: https://arxiv.org/abs/2610.26098
- **Abstract**: A game ships when a player can **launch it, finish it, and return to a saved world** — none of which a successful build guarantees — yet game-creation agents are mostly tested on **one engine or one-prompt browser games**. **CEGame-Bench** is the first long-horizon benchmark for **complete-game creation across five production engines** (Defold, Godot, Roblox Studio, Unity, Unreal). Agents build each game from an empty project + a design document that doubles as a **contract**, in runs averaging up to **295 steps and 65M tokens**, with a **hidden evaluator that accepts a game only by real-input play**.
- **Key innovations**: (i) Quantifies the **artifact-to-play gap** — under four scaffolds agents earn most integration points but usually **under half the gameplay points** and reach the ending in only **16%** of runs, while engineer-built references score near maximum (gap is in the agents); (ii) **no two engines rank configurations alike** (Kendall's τ 0.14–0.62) and the same game scores higher on Unity/Unreal (which check more before play); (iii) releases **Game Completion Boost**, an agent skill for requirement-driven playtesting and repair, raising execution-based scores of three models by **14.1–24.3 points**.
- **Status**: **new-to-wiki**, featured.

## 5. Game Benchmarks

### ROAR (NeurIPS 2026) — real-time multiplayer action-shooter benchmark
Listed in full under **§2** (Game AI Bot) as the run's flagship benchmark paper.

### CEGame-Bench — cross-engine complete-game creation benchmark
Listed in full under **§4** (PCG / game creation).

### AAArena — long-running game-agent competition (re-run cross-reference)
On file since 2026-10-09/11; see [`game-rl-daily` 2026-10-20 §5](../2026-10-20/game-rl-daily.md) for the full entry (Adversarial Heuristic Learning, 12 adversarial games, 1,920 archived human programs, Opus 5.5 + Claude Code earning 6 gold medals). Re-noted here because this run's date-range sweeps surfaced no newer competition-style benchmark.

## 6. Industry Game AI

### Matrix-Game 4.0 — real-time playable world (Skywork-lineage production target)
Listed in full under **§3**. Its **RTX 5090 / 60 FPS / 112 ms key-to-display** profile and **engine-renderer separation** make it the clearest industrial deployment datapoint in this run.

### SolarRenderer — engine-aligned renderer for game assets (production rendering)
Listed in full under **§3** (few-step, streaming 768p, 136K game-engine training clips).

> **Gap flag.** No paper from a named commercial studio (Embark / Ubisoft / EA / Riot / etc.) was surfaced in this window by the sweep queries; the industry lane is represented this run by the two world-model/rendering systems above rather than by a studio-authored position paper.

## 7. Related Techniques — Self-Play, Game Theory, Exploration, Multi-Agent

### ROAR-style asynchrony note
Not a separate paper; see §2 for the asynchronous multi-agent interface, which is the most reusable *technique* contribution this run for game-agent systems.

### How Far Can an Agent Push? Trust-Safety Margins in Live Language-Based Economic Games
- **Authors**: Dima Galat, Marian-Andrei Rizoiu
- **Affiliation**: — (UTS / Sydney lineage per author identity; not declared on abs page)
- **Venue**: arXiv preprint, 19 Oct 2026 (cs.AI, cs.GT) — live competition report
- **Link**: https://arxiv.org/abs/2610.25508
- **Abstract**: Game theory says when a strategic action *should* be accepted; it does not say **how long a live, language-based counterpart will keep accepting it**. The authors entered the **GLEE competition** with one protected agent **Milton** and four instrument agents running deterministic, per-game randomized policy trials, changes entering Milton only through **pre-specified gates or rollback-guarded production rules**.
- **Key innovations**: (i) Negotiation learned pricing improves adjusted percentile by **0.071 (n=21,168)**; a continuation model for bargaining **did not beat** a recency-weighted incumbent and was retired; (ii) a **preregistered five-dose persuasion experiment** (7,391 blinded games) shows recommending every unit raises sales by **0.194 of max** where obedience is rational (52% of the Bayesian benchmark) but **lowers** them (−0.067) where it is not, with a larger early-to-late decline than honest advice (−0.123); (iii) a rule fixed before unblinding routes Milton's dose per cell; Milton stood **11th of 460 agents**; three dispatch defects found by **checking delivered behavior against design**.
- **Status**: **new-to-wiki**, featured (live-deployment trust/safety evidence for language games).

### Strategy recovery for Mean-Payoff Games is as hard as solving them from scratch
- **Authors**: Dani Dorfman, Uri Zwick
- **Affiliation**: — (Tel Aviv University lineage per author identity; not declared on abs page)
- **Venue**: **SOSA 2027** (stated in comments); arXiv 18 Oct 2026 (cs.GT, cs.DS)
- **Link**: https://arxiv.org/abs/2610.25188
- **Abstract**: Mean-Payoff Games (MPGs) are deterministic infinite-duration zero-sum turn-based games on finite weighted digraphs; the players minimize/maximize the **limiting average** edge cost of an infinite path. MPG decision is in NP∩co-NP and even UP∩co-UP but **not known to be in P**. A full solution gives each vertex's value plus **positional optimal strategies**; **strategy recovery** = finding optimal strategies **given the values**.
- **Key innovations**: (i) A simple reduction from **solving MPGs to strategy recovery**, showing recovery is essentially **as hard as solving from scratch** — answering a question of Andersson & Miltersen; (ii) uses **game transformations, self-reducibility, and peeling**; (iii) goes further: finding an optimal strategy for *one* player stays hard **even when the other player's optimal strategy (hence all values) is known**, unlike Mamino's stochastic-game technique which does not extend to deterministic games.
- **Status**: **new-to-wiki**, featured.

### The Two-Level Poset Game is PSPACE-Complete
- **Authors**: Kengo Hashimoto
- **Affiliation**: —
- **Venue**: arXiv preprint, 15 Oct 2026 (cs.DM)
- **Link**: https://arxiv.org/abs/2610.19558
- **Abstract**: Poset games (Nim, Chomp, …) are fundamental combinatorial games; deciding the outcome is PSPACE-complete even for posets of **height ≤ 3**, but the exact complexity of the **Two-Level Poset Game** (height ≤ 2) had been open for over a decade.
- **Key innovations**: Proves **Two-Level Poset Game is PSPACE-complete** via a polynomial-time reduction from **Avoid True on positive CNF formulas** — closing a long-standing gap in combinatorial-game complexity.
- **Status**: **new-to-wiki**, featured.

### HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs
- **Authors**: Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, Honglin Lin, Junru Lu, Zhongxia Chen, Shuo Yang, H. Vicky Zhao, Jie Tang
- **Affiliation**: — (Tsinghua / Zhipu lineage per author identity; not declared on abs page)
- **Venue**: arXiv preprint, 20 Oct 2026 (cs.LG, cs.CL); 41 pages, under review
- **Link**: https://arxiv.org/abs/2610.26770
- **Abstract**: Recent **recursive self-improvement (RSI)** harness methods gain performance at **higher execution cost**. **HarnessPro** is a **label-free** method evolving harnesses to improve task performance *while reducing cost*, evaluating candidates with **LLM-generated tests** (no ground-truth solutions or official tests). Specialized agents **diagnose trajectories, plan updates under different performance-cost priorities, and implement candidate harnesses**; via **normalized weighted squared-distance selection** it emits cost-focused (*lite*), balanced (*medium*), and performance-focused (*heavy*) harnesses for different deployment budgets.
- **Key innovations**: (i) Harness selection under a **performance-cost Pareto front** rather than returning one harness; (ii) selected harnesses feed the next iteration with execution feedback; (iii) on **Terminal-Bench 2, SWE-Bench Pro, ProgramBench** with GPT-5.5+Codex, heavy mode gains **+2.0 pp average pass-rate** and **−26.1% average per-task cost** vs RHO, holding with GLM-5.2+Claude Code; (iv) relevant to game-agent harness lines (cf. KPHarness §2, gaming harnesses).
- **Status**: **new-to-wiki**, featured (game-agent adjacent; included for harness methodology).

### Information-Theoretic Guardrails for MARL: Non-Stationarity Breaks Permutation Surrogates
- **Authors**: Nikolaos Al. Papadopoulos, Konstantinos E. Psannis
- **Affiliation**: —
- **Venue**: arXiv preprint (substantially revised), 19 Oct 2026 (cs.AI, cs.IT, cs.LG, cs.MA); 33 pages; code+data on Zenodo
- **Link**: https://arxiv.org/abs/2604.23716
- **Abstract**: Reporting guidance for **information-theoretic influence measures** in MARL is rarely tested against ground truth. The authors test one guardrail in two MARL games — a **social dilemma** and a **coordination race** — where **directed influence between selected agent pairs is zero by construction**, over **100 seeds**.
- **Key innovations**: (i) Omitting one precondition — **exclusion of the non-stationary training transient** — yields false-positive rates of **100.00% and 99.95%**: independently annealing agents in runs that never met are flagged as influencing each other; (ii) excluding the transient still reaches 3.05% (social dilemma) but **11.8%** (coordination), so exclusion is neither the only way nor sufficient; (iii) recommending instead a **null-model change** (restricted permutation within training-time blocks) reaches **5.25%/5.50%** — the only null control at or below test size in both games; (iv) a third control (four learners) defeats all three, and conditioning costs 3× more (15.20 vs 4.55 points); titration separates it from conditioning on identical pairs (82.5% vs 58.0%).
- **Status**: **new-to-wiki**, featured (methodological guardrail for MARL representational analyses; listed here rather than §1).

---

## §0 Dedup and Cross-References

| arXiv ID | Item | Status in this run |
|----------|------|--------------------|
| 2610.28197 | ORBiT / ORCA (object-relative Atari RL) | **new-to-wiki, featured** (§1) |
| 2610.24282 | ROAR (NeurIPS 2026, real-time LMM agents) | **new-to-wiki, featured** (§2, §5) |
| 2610.27417 | KPHarness (Minecraft VLA harness) | **new-to-wiki, featured** (§2) |
| 2606.29745 | ECHO (epistemic multi-turn agents) | **new-to-wiki, featured** (§2, announced 10-20) |
| 2610.27028 | SPOKE (poker, IEEE iSAI-NLP SRW 2026) | **new-to-wiki, featured** (§2) |
| 2610.27999 | Matrix-Game 4.0 (real-time playable world) | **new-to-wiki, featured** (§3, §6) |
| 2610.25861 | ActionRoPE (planar-camera game world model) | **new-to-wiki, featured** (§3) |
| 2610.28630 | SolarRenderer (engine-aligned renderer) | **new-to-wiki, featured** (§3, §6) |
| 2610.26853 | InfiniDream (VLM procedural 3D worlds) | **new-to-wiki, featured** (§4) |
| 2610.26098 | CEGame-Bench (5-engine game creation) | **new-to-wiki, featured** (§4, §5) |
| 2610.25508 | Trust-safety margins (GLEE live games) | **new-to-wiki, featured** (§7) |
| 2610.25188 | MPG strategy recovery (SOSA 2027) | **new-to-wiki, featured** (§7) |
| 2610.19558 | Two-Level Poset Game PSPACE-complete | **new-to-wiki, featured** (§7) |
| 2610.26770 | HarnessPro (Pareto harness RSI) | **new-to-wiki, featured** (§7) |
| 2604.23716 | MARL permutation-surrogate guardrails | **new-to-wiki, featured** (§7) |
| 2610.12341 | AAArena | on file (10-09/10-11) — re-noted §5 |
| 2610.20584 | Player-1 | sibling [`arxiv-daily` 10-20/10-21](../2026-10-21/arxiv-daily.md) — not re-claimed |
| 2610.17391 | Learning to Play (book) | sibling [`arxiv-daily` 10-21](../2026-10-21/arxiv-daily.md) carries it — not re-claimed |

**Flags**: ⚠️ All claims **abstract-only** (no full-text/code verification this run). ⚠️ **arXiv export API was 429-blocked all session** — metadata sourced from search HTML + abstract pages; announcements/dates as shown by `arxiv.org` at fetch time (20–21 Oct 2026). Affiliations "—" where not declared on the abs page (notable inferences marked inline: TU Darmstadt, NUS Show Lab, Tsinghua/Zhipu, Tel Aviv, Newcastle, UTS). ⚠️ No named-studio (Embark/Ubisoft/EA/Riot) paper surfaced this window — §6 filled by world-model/rendering systems. ⚠️ `2606.29745` (ECHO) carries an older arXiv number but was **announced 2026-10-20**; treated as fresh for this window. No contradictions against existing wiki pages.
