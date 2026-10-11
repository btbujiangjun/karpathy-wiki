---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-11)"
type: synthesis
created: 2026-10-11
updated: 2026-10-11
sources: [arxiv.org, dl.acm.org, link.springer.com]
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent, game-theory, npc, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-11)

> A **spot-check digest across all seven lanes** (Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Industry Game AI, Related Techniques), compiled from targeted arXiv abstraction sweeps + web searches run for this digest. **Method note up front**: this edition is *not* a full export-API window enumeration — the arXiv export API was **unreachable** for this run (`http://export.arxiv.org/api/query` → HTTP 429 rate-limit; direct `curl` to the API returned `301`/`000` — see §0.2). As in the 2026-10-10 edition, the arXiv announcement block remains frozen around the **2026-10-08** cut (`2610.10537+`) and today's siblings report no new in-window game-RL papers, so this digest surfaces the **strongest recent game-RL/game-AI papers across the `2604→2610` ID range** not re-featured in the last two editions, plus **five fully-fresh items (0 hits anywhere in the wiki)**. Every featured ID was grep-verified: **0 hits in `wiki/synthesis/2026-10-11/`**; 5 of 17 are **0 hits repo-wide**; the remaining 12 are already documented in earlier digests and are detailed here for continuity with an explicit note.

---

## §0 Method and Corpus

### 0.1 Coverage
- **No fresh in-window game papers to claim.** The 2026-10-08 announcement block was harvested by the 10-09/10-10 sibling digests and contains **no unclaimed game-playing-RL paper**; the announcement frontier has not advanced to a new block for 2026-10-11. This digest therefore **re-mines the recent back-catalog** (`2604.*`–`2610.*`) across the seven requested lanes, weighted toward work last surfaced in the 2026-08/09 digests.
- **Boundary**: featured IDs span `2604.03091`–`2610.10164`; latest submission date ~2026-10-07 (`2610.09218`). No re-feature of the 10-10 featured set (verified 0 hits in `wiki/synthesis/2026-10-10/` for all of this edition's additions).

### 0.2 Sweep
1. **Web/targeted searches** across: Game RL (self-play, reward/policy interventions, RL algorithm evolution), Game AI Bot / LLM+RL NPC, Game Foundation Models / generalist agents, PCG (level gen, agentic game creation, world-model map gen), Game Benchmarks (world-model eval, LLM-RL testbeds, social games), Industry Game AI (affective adaptation, RL deployment), Related (skill learning, world models, program evolution).
2. **arXiv abs-page pulls** for every refined candidate to lock authors + submission dates + venue comments.
3. **Network note**: `curl` to the arXiv export API failed this run (`http://` → `http=301`; `https://` → `http=000`; `webfetch` on the API → **HTTP 429 rate-limit**). Metadata was recovered via `webfetch` on individual `arxiv.org/abs/*` pages and web search instead. This is a known limitation carried over from the 10-10 edition.
4. **Dedup** — each candidate ID `rg`-grep'd against the whole `wiki/` (**17 featured: 5 fresh / 12 documented-and-refeatured**) and against `wiki/synthesis/2026-10-11/` (**0 hits for all 17**).

### 0.3 Dedup accounting (featured set)
| arXiv ID / DOI | In wiki total | In today's dir |
|----------------|--------------:|---------------:|
| 2610.04441 (LocusRL) | 0 | 0 |
| 2605.14211 (ASH) | 0 | 0 |
| 2610.10164 (UniSkill) | 0 | 0 |
| 10.1145/3807895.3807929 (Pacing-Aware Level Gen) | 0 | 0 |
| 10.1145/3816781 (Affective Game Adaptation) | 0 | 0 |
| 2610.09218 (RLDiscover) | 2 | 0 |
| 2606.24597 (Qwen-AgentWorld) | 2 | 0 |
| 2604.03091 (CASCADE) | 2 | 0 |
| 2609.09418 (Valerant) | 3 | 0 |
| 2610.00416 (Chess Prompt Optimization) | 4 | 0 |
| 10.1007/s00521-026-12275-w (HeRoN) | 4 | 0 |
| 2610.08621 (Recursive Game Creator) | 4 | 0 |
| 2609.34214 (GlyphBench) | 4 | 0 |
| 2608.09128 (Social Gym / SPaRTan) | 5 | 0 |
| 2608.29910 (Matrix-Game 3.5) | 6 | 0 |
| 2608.13552 (PlayWorld) | 7 | 0 |
| 2606.08656 (MemoPilot) | 17 | 0 |

### 0.4 Affiliations and venues
- **Abs-page pulls frequently do not print affiliations.** Where an institution could not be read from the paper's own author block/thanks, it is marked **"not stated"** and **not inferred** from surnames or email domains (standing wiki discipline). Inferred affiliations appear only as **"⚠️ inference from public author records — tentative"**, never asserted as fact.
- Venues are stated **only where the venue is explicit** in the source (e.g., `NeurIPS 2026`, `ICML 2026`, `PACM HCI 10(4)`, `I3D Companion '26`); otherwise `arXiv preprint`. **No result independently replicated.**

---

## §1 Game RL — Reinforcement Learning in Games

### ★★★ LocusRL: Diagnosing LLM Reward and Policy Interventions in Competitive Games
- **Authors**: Chengyu Luan, Bo Xin, Songyan Guo, Yuxiang Zuo, Ahmed Yazdan, Jiahang Li, Yicheng Liu
- **Affiliation**: ⚠️ not stated on abs page; *not inferred*.
- **Venue**: arXiv:2610.04441 (3 Oct 2026) — `cs.LG`. 47 pages incl. appendices.
- **Link**: https://arxiv.org/abs/2610.04441
- **Abstract and key innovations**: a **diagnostic framework** for what LLM interventions *actually do* when they enter an RL loop, either as **reward designers or action selectors**. Because aggregate returns conceal mechanism, LocusRL connects **controlled reward-policy comparisons** with **audits of reward judgments, signal delivery, optimization objectives, and executed actions**, tracing performance gaps to **testable explanations** and checking corrections via **executable rules + counterfactual replay**. Across **two batches / ten Connect Four seeds** it finds **seed-dependent reversals** in whether an intervention helps, and shows historical Qwen training operates through **reward-weighted teacher-action likelihood**. A matched **reward-direction experiment** isolates *sensitivity to a learning signal* from its *usefulness*: with terminal rewards fixed, a **sign-reversed dense oracle yields 2.8% win rate vs. 57.2% for terminal-only and 46.7% for the positive dense oracle** — "a reward can strongly influence learning without improving performance." Extensions to **Leduc** (imperfect information) and reward-validation in **Goofspiel**.
- **Why it matters here**: the wiki's sharpest **evaluation-methodology** entry for the LLM-in-the-RL-loop paradigm that §2's NPC papers depend on — the natural counterpart to the 10-10 digest's *self-play instability* cluster, but at the **diagnosis** layer rather than the algorithm layer.
- **Caveats**: **fully fresh — 0 hits in wiki**; games are small (Connect Four, Leduc, Goofspiel); diagnostic framework rather than a new winning agent.

### ★★ MemoPilot: From Player to Master — Enhancing Test-Time Learning of LLM Agents via RL over Memory
- **Authors**: Yishuo Cai, Xingyu Guo, Xuancheng Huang, Jinhua Du, Can Huang, Wenxuan Huang, Wenhan Ma, Yuyang Hu, Aohan Zeng, Jie Tang, Xu Sun
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Tsinghua/Alibaba-aligned author block per public records — tentative).
- **Venue**: **ICML 2026** — also arXiv:2606.08656 (7 Jun 2026) — `cs.CL`.
- **Link**: https://arxiv.org/abs/2606.08656
- **Abstract and key innovations**: treats **memory updating as a multi-turn decision problem** and trains it **end-to-end with multi-turn GRPO** for a **frozen** player LLM. The recipe adds **(i) a turn-wise reward signal** and **(ii) context-independent, turn-level advantage estimation across rollouts** for finer credit assignment. Evaluated on **multi-round Rock-Paper-Scissors** and **Limit Texas Hold'em**, MemoPilot ranks **first in Elo on both** (1762 LHE, 1590 RPS) and beats all baseline memory methods and proprietary models including **DeepSeek-V3.2**.
- **Why it matters here**: the clearest recent result that **test-time memory is itself a learnable policy** in zero-sum games — the "learn-in-the-loop" cousin of LocusRL's "diagnose-in-the-loop," and a direct fit for the wiki's poker/long-horizon-NPC line.
- **Caveats**: already in wiki (17 hits) — re-featured for the lane with an explicit continuity note; games are stylized (RPS/LHE); frozen backbone only.

### ★★ Benchmarking Prompt Optimization of Large Language Models With Chess
- **Authors**: Timothée Lesort, Alejandra López de Aberasturi Gómez, Tristan Karch, Tom Veniat, Philippe Modard, Karl Tuyls, Ludovic Denoyer
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (imec-AI Labs + industrial co-authors per the project repo — tentative).
- **Venue**: arXiv:2610.00416 (30 Sep 2026) — `cs.AI`/`cs.LG`.
- **Link**: https://arxiv.org/abs/2610.00416
- **Abstract and key innovations**: a **chess benchmark of 1,118 Lichess puzzles** built specifically to study **automatic prompt optimization (APO)** for **frozen** LLMs. Chess offers **cheap exact-match scoring**, **engine-based evaluation of alternative moves**, and a **renewable, difficulty-adjustable** problem supply. The benchmark links puzzle-solving gains to **short game-play rollouts** in the same domain. It evaluates **six APO algorithms on eight target models**, measuring baseline strength, responsiveness to optimization, and **cross-model/cross-task transfer**. Even the strongest meta-model (Gemini 3.5 Flash) solves only **~55%** of puzzles; the whole study runs for **~\$800**.
- **Why it matters here**: gives the wiki a **renewable, anti-contamination game benchmark** whose design principles transfer to any game-agent eval — explicitly motivated by benchmark saturation/contamination, the same problem flagged by 10-10's GameHorizon/MineExplorer entries.
- **Caveats**: already in wiki (4 hits); chess-only; APO is the object of study, not game-playing ability per se.

---

## §2 Game AI Bot — LLM-Powered Game Agents and NPC Intelligence

### ★★★ ASH: Agents that Self-Hone in Long-Horizon Worlds
- **Authors**: Benjamin Schneider, Xavier Schneider, Victor Zhong, Sun Sun
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Waterloo-aligned authors per public records — tentative).
- **Venue**: **NeurIPS 2026** — also arXiv:2605.14211 (v1 14 May 2026; v5 1 Oct 2026) — `cs.AI`/`cs.LG`.
- **Link**: https://arxiv.org/abs/2605.14211
- **Abstract and key innovations**: an **agentic self-improvement loop** that learns a long-horizon policy from **unlabeled, noisy internet video — no reward shaping, no expert action labels**. When stuck, ASH **learns an Inverse Dynamics Model (IDM) from its own trajectories** and uses it to **extract supervision from relevant internet video**; unsupervised learning identifies **key moments** from large-scale video, retained as **long-term memory**. Evaluated on two multi-hour environments — **Pokemon Emerald** (turn-based RPG) and **The Legend of Zelda: The Minish Cap** (real-time action-adventure) — behavioral cloning, retrieval-augmented and zero-shot FM baselines plateau, while **ASH sustains progression across an 8-hour evaluation**: **11.2/12 vs. 9.3/12 milestones** on Pokemon and **9.9/12 vs. 7.8/12** on Zelda.
- **Why it matters here**: the strongest **self-honing / no-supervision long-horizon game-agent** result in the wiki — the "the agent mines its own supervision from raw video" thesis, directly complementing the 10-10 digest's world-model *detect-and-repair* theme and the long-horizon NPC line.
- **Caveats**: **fully fresh — 0 hits in wiki**; two-game scope; relies on internet video quality; milestone scoring is paper-defined.

### ★★ HeRoN: A Mediated RL-LLM Framework for Adaptive NPC Behavior in Interactive Environments
- **Authors**: not listed on the retrieved index (see venue link for the full author block)
- **Affiliation**: ⚠️ not restated here — *not inferred*.
- **Venue**: **Neural Computing and Applications 38, art. 549 (2026)** — DOI 10.1007/s00521-026-12275-w (published 26 Jun 2026).
- **Link**: https://link.springer.com/article/10.1007/s00521-026-12275-w
- **Abstract and key innovations**: a **mediated RL–LLM architecture** (Helper–Reviewer–NPC) that separates RL action execution from LLM reasoning: the **NPC** is an RL policy, the **Helper** an LLM generating context-aware proposals, and the **Reviewer** a lightweight critique module that **refines proposals against environment constraints**. Functional separation — rather than autonomous LLM control — targets the twin failure modes of RL (inefficiency) and LLMs (hallucination/context drift). On a JRPG-style turn-based battle and **ViZDoom**, **early-phase** mediation gives up to **81% task-success improvement** and reduces constraint-violating actions. The **Reviewer cuts hallucinated actions by up to 98%**, and PPO-refined critique is critical (Qwen 0%→81.2% testing vs. 43.0% supervised-only).
- **Why it matters here**: the cleanest **"LLM proposes, RL disposes, a critic grounds"** decomposition in the wiki — an explicit architectural answer to the hallucination problem that 10-10's Cutscene Agent and this edition's NPC papers all circle.
- **Caveats**: 4 hits in wiki (documented earlier; re-featured); custom small game environments; author block not captured in this sweep.

### ★★ CASCADE: A Cascading Architecture for Social Coordination with Controllable Emergence at Low Cost
- **Authors**: not fully listed on the retrieved source
- **Affiliation**: ⚠️ not restated — *not inferred*.
- **Venue**: arXiv:2604.03091 (Apr 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2604.03091
- **Abstract and key innovations**: a **three-layer, coordination-centric** architecture for cheap, steerable game societies: a **Macro State Director** maintains discrete-time world-state variables and macro causal updates; a modular **Coordination Hub** decomposes state changes into domain modules and routes **JSON directives** by **tag-defined groups**; **Tag-Driven NPCs** execute via **behavior trees + local utility**, invoking LLMs **only for on-demand player-facing interaction**. Compared with a "Full-Generative" per-agent-prompting baseline, CASCADE **slashes token cost** and introduces **Action-Dialogue Decoupling** — a neuro-symbolic isolation that blocks prompt-injection from overwriting physical behavior.
- **Why it matters here**: the wiki's strongest **deployment-economics** counterpoint to "LLM every NPC" — it reframes the design unit from *the agent* to *social coordination*, and adds a security argument relevant to any open-world LLM-NPC shipping decision.
- **Caveats**: 2 hits in wiki (documented earlier; re-featured); micro-scenario/trace-based evaluation, not a shipped title.

### Cross-references (established, not re-summarized)
- **LLM-Guided Reinforcement Learning for Adaptive NPC Behavior** `2609.02931` *(local Mistral-7B emits four runtime tactical tags steering a trained PPO policy; balanced-opponent win rate 11%→24%; but "Surround" chosen 83.8% regardless of opponent)* — 12 hits, last featured **10-10**/10-04.
- **One Policy, Infinite NPCs (pcsp)** `2605.23652` *(persona-conditioned shared RL policy; InfoNCE trajectory-consistency loss is load-bearing; 64-agent UE5 deployment)* — 20 hits, documented in prior digests.

---

## §3 Game Foundation Models

### ★★ Qwen-AgentWorld: Language World Models for General Agents
- **Authors**: Yuxin Zuo, Zikai Xiao, Li Sheng, Fei Huang, Jianhong Tu, Yuxuan Liu, Tianyi Tang, Xiaomeng Hu, Yang Su, … (Qwen team; truncated author list)
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Alibaba Qwen team — tentative).
- **Venue**: arXiv:2606.24597 (23 Jun 2026) — `cs.CL`/`cs.AI`.
- **Link**: https://arxiv.org/abs/2606.24597
- **Abstract and key innovations**: **language world models** that simulate **agentic environments across 7 domains** via long chain-of-thought. Two sizes (`-35B-A3B`, `-397B-A17B`) trained on **>10M real environment-interaction trajectories** through a **three-stage pipeline (CPT → SFT next-state-prediction → RL with hybrid rubric-and-rule rewards)**. Two uses: (i) a **decoupled environment simulator** enabling scalable agentic RL beyond real-environment training, and (ii) a **unified agent foundation model** where world-model training acts as an **effective warm-up**. Ships **AgentWorldBench** (built from 5 frontier models × 9 benchmarks).
- **Why it matters here**: the GFM lane's **first language-based world model** in this wiki (vs. the pixel/video world models of §7.2) — it reframes "world model" from *renderer* to *text-simulator for agent training*, the cleanest bridge between the game-world-model lane and generalist-agent training.
- **Caveats**: 2 hits in wiki (documented earlier; re-featured); 7-domain scope not game-specific; author list truncated on the abs page.

### Cross-references (established, not re-summarized)
- **NitroGen** `2601.02427` — open generalist game agent (40k h / 1,000+ games), **CVPR 2026 (Honorable Mention)**; 53 hits in wiki.
- **Game-TARS** `2510.23691` — ByteDance Seed generalist multimodal game agent, native keyboard-mouse action space; documented in prior digests.
- **Towards Generalist Game Players** `2605.09965` — the field-survey "four pillars / five trade-offs / five-level roadmap" lens (dataset–model–harness–benchmark); 44 hits.

### Lane status
**No fresh unclaimed generalist game foundation model** surfaced for this window; the increment remains **world-model and data/eval infrastructure** (Qwen-AgentWorld here; GameHorizon/MineExplorer/MirrorCraft in the 10-10 edition; PlayWorld/GlyphBench in §5 below).

---

## §4 Procedural Content Generation (PCG)

### ★★★ Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness
- **Authors**: Jiajun Chen, Haoyu Wu, Mingda Jia, Xihui Liu
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (HKU-aligned authors per public records — tentative).
- **Venue**: arXiv:2610.08621 (7 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.08621
- **Abstract and key innovations**: closes the gap between "a game that **runs**" and "a game people **want to keep playing**." A recursive loop of four roles — **Designer, Builder, Player, Reviewer** — where the **coding-native Player** creates reusable **policies (programs)** that read game state and act, collecting trajectories **without per-frame LLM screenshot parsing**, and the **Reviewer** induces player preferences from **trajectory metrics + visuals + explicit textual preferences**. On **GameCraft-Bench** (Godot engine) overall score rises **72.70 → 77.89** over three rounds; on **GameASG-Bench** strict task success rises **9/47 → 25/47 (+34.1%)** with **93.4%** runtime-check pass rate. The model itself is never retrained.
- **Why it matters here**: the wiki's most complete **"game = code, verified by executable play"** loop — the experience-oriented successor to the 10-10 edition's AutoUE, and a direct PCG analogue of §7's RLDiscover program-search.
- **Caveats**: 4 hits in wiki (documented earlier; re-featured); **no component ablation** and no compute accounting; code "coming soon," so it is a system design + eval rather than a released tool.

### ★★ Pacing-Aware Level Generation with Dynamic Event Control
- **Authors**: not listed on the retrieved ACM index page
- **Affiliation**: ⚠️ not restated — *not inferred*.
- **Venue**: **I3D Companion '26** (Symposium on Interactive 3D Graphics and Games) — DOI 10.1145/3807895.3807929 (published 29 Jun 2026).
- **Link**: https://dl.acm.org/doi/10.1145/3807895.3807929
- **Abstract and key innovations**: a **pacing-aware AI director** that lets designers specify a **target experience curve**, which drives both **(1) procedural terrain generation** and **(2) runtime gameplay control**. Implemented in the co-op traversal-survival game **Pull It Together** (1–4 players haul a wagon through a storm): trail **segments are generated to match an offline difficulty curve**, and during play a **stress proxy** (health, wagon damage, resources, storm proximity, terrain) is continuously pushed toward the target via **event injection + storm-speed control** in a closed feedback loop.
- **Why it matters here**: a rare **PCG × experience-management** join — it makes *pacing*, not just playability, the generation objective, filling a gap between the wiki's structural PCG (levels) and its NPC/world-model lines (behavior).
- **Caveats**: **fully fresh — 0 hits in wiki**; author block not captured; evaluation is qualitative/telemetry-based; companion-track paper.

### ★★ Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration
- **Authors**: Yiran Qiao, Feng Wang, Jing Ma
- **Affiliation**: ⚠️ not stated on abs page; *not inferred*.
- **Venue**: arXiv:2609.09418 (8 Sep 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2609.09418
- **Abstract and key innovations**: a **training-free** framework that turns a **pretrained action-conditioned world model into a World-Action Model (WAM)** for **exploring and constructing persistent 3D game maps**. Because games — unlike driving/robotics — have **no external physical substrate**, the virtual world must be instantiated: Valerant couples **predictive visual rollouts** with **SLAM-based spatial reconstruction** and **exploration-driven action selection** to progressively turn **a single image into a navigable 3D game map**.
- **Why it matters here**: the PCG lane's **world-model-as-generator** entry — it connects procedural map creation to the §7.2 game-world-model thread and to the 10-10 theme "world models are built to be *used*," not just rendered.
- **Caveats**: 3 hits in wiki (documented earlier; re-featured); single-image→3D-map scope; no downstream gameplay evaluation on the generated maps.

### Cross-references (established, not re-summarized)
- **AutoUE** `2603.07106` (multi-agent LLM → Unreal Engine games, RAG + play-test loop; featured **10-10**), **Multiverse** `2603.26782` (language-conditioned multi-game level blending; 17 hits), **Programmatic Content Metageneration + CAD** `2608.17947` (LLM evolutionary generator search; 12 hits), **High-Dimensional PCG** `2602.18943` (space/time-augmented level generation; 16 hits), **Playtrace Reconstructive Partitioning** `2607.12097` ("cake" temporal level representation; 6 hits).

---

## §5 Game Benchmarks & Datasets

### ★★★ PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives
- **Authors**: not fully listed on the retrieved source (project page: `kxding.github.io/project/PlayWorld/`; work done at the **Kling Team, Kuaishou**)
- **Affiliation**: ⚠️ not restated — *not inferred* beyond the explicit "Kling Team, Kuaishou Technology" thanks.
- **Venue**: arXiv:2608.13552 (14 Aug 2026) — `cs.CV`/`cs.AI`.
- **Link**: https://arxiv.org/abs/2608.13552
- **Abstract and key innovations**: benchmarks **video world models** the way a *human player* would — by pursuing **long-horizon objectives through interaction** rather than fixed action-conditioned clips. A multimodal **Agent Player** adaptively adjusts execution (**Keep/Stop/Extend/Correct/End**) to each model's action granularity; **171 human-annotated scenarios / 50 action patterns / 10–60 s rollouts** are scored by a **VQA rubric verifier** across **geometry consistency, interaction fidelity, out-of-sight evolution, and insight evolution**, plus basic quality/controllability metrics. Nine state-of-the-art models are evaluated (>1,400 videos, >820 questions): all remain **unreliable on long-horizon interactive objectives**, especially **spatial consistency and persistent state evolution**.
- **Why it matters here**: the wiki's **first world-model evaluation protocol built on agentic play** — the empirical instrument that makes the §7.2 "persistent state" claims testable, and a direct sibling of the 10-10 edition's MirrorCraft (hidden-rule generalization).
- **Caveats**: 7 hits in wiki (documented earlier; re-featured); author list not fully captured; world-model-only scope.

### ★★★ GlyphBench: A Playground for Language-Model Reinforcement Learning
- **Authors**: not listed on the retrieved source
- **Affiliation**: ⚠️ not restated — *not inferred* (Prime Intellect "Prime-RL" integration referenced — tentative).
- **Venue**: arXiv:2609.34214 (28 Sep 2026) — `cs.AI`/`cs.LG`.
- **Link**: https://arxiv.org/html/2609.34214v1
- **Abstract and key innovations**: an **environment suite for RL post-training of language-model agents** with **360+ tasks across nine game families**, rendering spatial observations as **2D Unicode "glyph" grids** with a unified train/eval/replay interface. Findings: **glyph observations outperform native text and pixels** in Craftax, with further gains on several **BALROG** environments; RL on **100 tasks improves Qwen3.5-4B on held-out Reasoning Gym to 63.48%**, beating base (56.04%), math-trained (62.29%) and code-trained (58.98%) baselines — evidence that **reasoning gains from gameplay transfer better than math/code RL**.
- **Why it matters here**: the wiki's clearest **"games as RL post-training substrate"** result with a **transfer** claim — connects the benchmark lane to the LLM-training lane and gives concrete numbers for the standing "is gameplay a good training signal?" question.
- **Caveats**: 4 hits in wiki (documented earlier; re-featured); author list not captured; transfer gains are modest (+1.19 pp over Math RL).

### ★★ Social Gym and SPaRTan: Benchmarking and Improving LLM Social Reasoning via Multi-Agent Game Tournaments
- **Authors**: not listed on the retrieved source
- **Affiliation**: ⚠️ not restated — *not inferred*.
- **Venue**: arXiv:2608.09128 (Aug 2026) — `cs.AI`.
- **Link**: https://arxiv.org/html/2608.09128v1
- **Abstract and key innovations**: **Social Gym**, an environment of **21 multi-agent social games** (Werewolves, Resistance, Spyfall, Prisoner's Dilemma, …) whose **rule-decided outcomes** make performance verifiable, with an **Elo tournament / cross-game leaderboard**. No model dominates across all games or roles (GPT-5-mini tops the board but has role-specific weaknesses). **SPaRTan** is a **training-free** play→reflect→transfer loop: the model writes a **transferable natural-language playbook** from its own trajectories and prepends it to future prompts; playbooks **lift the structurally weaker side** of asymmetric games but **largely fail to improve Qwen3-32B**.
- **Why it matters here**: gives the wiki a **verifiable (no-LLM-judge) social-reasoning benchmark** and the concrete finding that **social ability is not a single scalar** — directly relevant to multiplayer/negotiation NPCs and to the RLVR direction.
- **Caveats**: 5 hits in wiki (documented earlier; re-featured); author list not captured; SPaRTan benefits are model-dependent.

### Cross-references (established, not re-summarized)
- **GameHorizon Suite** `2609.25001` (AAA multi-horizon dataset; featured **10-10**), **MirrorCraft** `2607.29218` (paired hidden-rule benchmark; featured **10-10**), **MineExplorer** `2605.30931` (leak-free Minecraft exploration; featured **10-10**), **GameWorld** `2604.07429` (34 browser games, state-verifiable eval; 40+ hits), **Orak** `2506.03610` (KRAFTON, 12-genre; documented prior), **lmgame-Bench** `2505.15146`, **BALROG** `2411.13543`.

---

## §6 Industry Game AI

### ★★ LLM-Assisted Reinforcement Learning for Affective Game Adaptation
- **Authors**: Mahyar Tourchi Moghaddam, Tiziano Santilli, Mina Alipour
- **Affiliation**: ⚠️ not stated in the retrieved index; *not inferred* (SDU/European-aligned authors per public records — tentative).
- **Venue**: **PACM Human-Computer Interaction 10(4), art. EICS029** (2026) — DOI 10.1145/3816781 (published 29 Jun 2026).
- **Link**: https://dl.acm.org/doi/full/10.1145/3816781
- **Abstract and key innovations**: an **affect-aware game-adaptation architecture** combining a warm-started **tabular Q-learning** controller with **bounded LLM-assisted action suggestion inside a MAPE-K loop**. Crucially, the LLM **cannot act freely** — it may only recommend one action from a **fixed, predefined adaptation menu**, while RL retains all value updates and policy improvement. Implemented in **CubeWars** (top-down shooter with browser facial-expression sensing) across four levers (difficulty, color, audio, prompts). **46 participants / three conditions**: both adaptive conditions beat the static baseline on **absolute progression**; RL-only vs. LLM-assisted RL **do not differ on normalized objective throughput**, but the hybrid yields **higher engagement, absorption, and perceived adaptivity**.
- **Why it matters here**: the wiki's first **human-subject, affect-aware** game-AI study — a rare *safe hybrid LLM+RL integration pattern* (constrained action space, RL-owned credit) with an explicit, honest "the value is experiential, not objective" finding.
- **Caveats**: **fully fresh — 0 hits in wiki**; small-N within-subject study; affective comparison did not survive Bonferroni correction.

### Cross-references (established, not re-summarized)
- **Augmenting Game AI with Deep RL** `2606.20210` (EA; vision paper + FC 25 / Battlefield 6 experiments; **65 hits** — the lane's backbone), **AI for Games in the Foundation Model Era** `2609.16679` (featured **09-16**), **Reinforcement Learning with Human-Engine Verification** `2608.25518` (RLHEV; documented prior), **AI Level of Detail** `2606.06565` (distance-aware ML precision LOD; featured **10-10**).

---

## §7 Related Techniques

### 7.1 Skill / Program Learning

#### ★★ UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy
- **Authors**: Yifei Lu, Cheng Liu, Dianzhi Yu, Hui Xiang, Ji Zhang
- **Affiliation**: ⚠️ not stated on abs page; *not inferred*.
- **Venue**: arXiv:2610.10164 (7 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.10164
- **Abstract and key innovations**: a **shared policy** that both acts in the environment and proposes **skillbank edits (Add / Update / No Edit)** from its own trajectories. The key idea is **contrastive action feedback**: instead of testing each proposed skill with costly new rollouts, it measures **how swapping the retrieved skill for the proposed one changes the actor's action log-likelihood gap between previously collected successful and failed trajectories** — an **actor-alignment signal** without extra rollouts. A **skill-edit support regularizer** preserves exploration. Reaches **98.4%** on ALFWorld and **84.7%** on WebShop with stable joint training, including on a smaller backbone.
- **Why it matters here**: **fully fresh — 0 hits in wiki** — the wiki's first **rollout-free skill-critique** method for co-evolving skill libraries, the direct analogue of the Retriever/skillbank thread and applicable to lifelong game-agent skill accumulation.
- **Caveats**: no game in the eval (household/web tasks); single paper, small backbones.

#### ★★★ RLDiscover: LLM-Driven Co-Evolution of Reinforcement Learning Algorithms
- **Authors**: Haoran Li, Zengle Ge, Xiaomin Yuan, Yui Lo, Songlin Zhou, Jiahua Ying, Haoxin Li, Qianhui Liu, Yuanhang Liu, Jiaqun Liu, Guokai Chen, Mingju Chen, Ruinan Wang, Annan Li, Jianmin Wu, Dawei Yin, Dou Shen
- **Affiliation**: ⚠️ stated only via paper affiliations banner — University of the Chinese Academy of Sciences, Baidu, Tsinghua University, Institute of Automation CAS, Peking University, Shanghai University, University of Bristol.
- **Venue**: arXiv:2610.09218 (6 Oct 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2610.09218
- **Abstract and key innovations**: **self-evolution of model-free deep-RL algorithms** via LLM-guided program search. **Progressive Co-Evolution (PCE)** moves from targeted component edits (UCB-allocated over five interfaces: observation processing, target/advantage estimation, value losses, policy objectives, reward/exploration) to **joint** revisions; **Progressive Probabilistic Evaluation (PPE)** uses staged fidelity (L0 50K/1 seed → L1 200K/2 → L2 1M/3) to concentrate compute. Across **SAC, PPO, DQN on four benchmark suites** it improves **all 26 task–algorithm pairs** (median gains **+39.8% / +83.6% / +32.1%**, peak ratio **~363×**) and repeatedly discovers the **same interpretable mechanisms** (robust critic losses, progress-dependent value targets, running statistics) that **transfer to unseen tasks**, at **~1/15 the compute** of full-fidelity evaluation.
- **Why it matters here**: the wiki's strongest **"RL algorithms that write themselves"** result — it generalizes the program-search theme (AutoUE, Recursive Game Creator, CAD) from *content* to *the learning rule itself*, and its compute-efficiency schedule is a reusable template.
- **Caveats**: 2 hits in wiki (documented earlier; re-featured); benchmark suites are standard control/Atari-style, not named games; code "released upon acceptance."

### 7.2 World Models for Games

#### ★★ Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory
- **Authors**: not listed on the retrieved abs page (technical report; Matrix-Game series)
- **Affiliation**: ⚠️ not restated — *not inferred*.
- **Venue**: arXiv:2608.29910 (30 Aug 2026) — `cs.CV`.
- **Link**: https://arxiv.org/abs/2608.29910
- **Abstract and key innovations**: advances real-time interactive world generation via three pieces: (1) a **unified geometry-aware memory framework** — **patch-memory** lifts historical image patches into a persistent 3D memory and retrieves only target-view-visible regions, while **tiled PRoPE** supplies projective camera conditioning (no extra learnable parameters); (2) a **static–dynamic disentangled world representation** separating persistent scene geometry from movable entities; (3) **two-stage progressive real-time distillation** (Perceptual Flow Matching + curriculum Self-Rollout DMD) converting a bidirectional diffusion model into a **few-step causal generator** — **up to 20 FPS on a single GPU**. Trained on Unreal simulations, open-world games, and internet video.
- **Why it matters here**: the world-model lane's **real-time + long-horizon-memory** frontier, the concrete system behind the "persistent state" requirement that §5 PlayWorld now *measures*.
- **Caveats**: 6 hits in wiki (documented earlier; re-featured); technical report, no peer review; author list not captured.

#### Cross-references
- **GameDirector** `2609.25652` (decoupled rule-based logic vs. rendering; featured **10-01/10-04**), **WorldMind** `2608.21439` (decoupled state-aware NPC world model; 15 hits), **Programmable World Model** `2609.10540`, **GameWAM** `2608.26200`, **ReactiveGWM** `2605.15256` (flexible control + NPC reactivity), **Zing-0.5** `2609.17909` (real-time joint action+text control), **ReWorld** `2608.23565` (long-horizon memory), **Rethinking Interactive World Models as Game Engines** `2607.14076` (position paper + Black Myth: Wukong data engine) — all documented in prior digests.

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL | 3 |
| Game AI Bot | 3 (+2 cross-ref) |
| Game Foundation Models | 1 (+3 cross-ref) |
| PCG | 3 |
| Benchmarks & Datasets | 3 (+6 cross-ref) |
| Industry Game AI | 1 (+4 cross-ref) |
| Related Techniques | 3 (+7 cross-ref) |
| **Featured total** | **17** (5 fully fresh, 12 documented-and-refeatured) |

## Key Themes

1. **The intervention loop itself is now the object of study.** LocusRL (diagnose LLM reward/policy interventions), MemoPilot (learn the memory-update policy), and RLDiscover (evolve the RL algorithm) all shift attention from *the policy* to *the machinery that changes the policy* — and LocusRL's "a reward can strongly influence learning without improving performance" is the sharpest caution yet for the wiki's LLM-in-the-loop NPC line.

2. **Games-as-code, verified by execution, is now the default PCG idiom.** Recursive Game Creator (policies as programs, trajectory-metric review), Valerant (world model + SLAM → navigable map), and the standing CAD/AutoUE thread converge: **content should be executable and checkable**, not merely rendered.

3. **World models are being *measured on persistence*, not fidelity.** PlayWorld (agent-player long-horizon objectives) and Matrix-Game 3.5 (patch-memory + static/dynamic disentangling) define the two ends — a test protocol and a system — of the same requirement, with Programmable World Model and ReWorld in between.

4. **LLM+RL integration converges on *bounded* mediation.** HeRoN (Helper–Reviewer–NPC), CASCADE (Action-Dialogue Decoupling), and Affective Game Adaptation (fixed action menu, RL owns credit) independently re-derive the same safe pattern: **let the LLM propose, keep RL (or symbolic rules) in charge of acting.**

5. **The GFM lane's real storyline stays infrastructure, now in *language*.** Qwen-AgentWorld's text-simulator reframes the foundation-model lane, while GlyphBench supplies the "games beat math/code as RL post-training data" transfer evidence and Chess Prompt Optimization provides a renewable, anti-contamination game benchmark.

> **Dedup/venue disclosures**: all 17 featured IDs `rg`-verified **0 hits in `wiki/synthesis/2026-10-11/`**; 5 are **0 hits repo-wide** (LocusRL, ASH, UniSkill, Pacing-Aware Level Generation, Affective Game Adaptation). Selected venues stated only where explicit (**NeurIPS 2026**, **ICML 2026**, **PACM HCI 10(4)**, **I3D Companion '26**, **Neural Computing and Applications 38:549**). Affiliations printed as **not stated** or **tentative inference**; none asserted as fact. **The arXiv export API was rate-limited/unreachable this run** (see §0.2), so metadata came from individual abs-page pulls + web search. No result independently replicated.

## §9 Contradictions, Venue Updates, and Sibling Collisions

### 9.1 Contradictions / tensions
- **"Reward-signal sensitivity ≠ usefulness."** LocusRL's sign-reversed dense oracle (2.8% win rate, worse than terminal-only 57.2%) directly tensions with the implicit assumption in reward-shaping NPC work (e.g., §2 HeRoN's proposal rewards) that a stronger/learnable reward signal is inherently better. Flagged as a **methodological caution**, not a formal contradiction with a single other page.
- **"Memory helps" vs. "retaining raw records helps."** MemoPilot *learns* memory updates for strong gains (RPS/LHE); SPaRTan (§5) finds natural-language playbooks help the *weaker* side but **largely fail on Qwen3-32B**. Both are single-source; note as **model-dependent** rather than contradictory.

### 9.2 Venue updates
- **ASH** `2605.14211` — now confirmed **NeurIPS 2026** (was a preprint in the ID range); v5 revised 1 Oct 2026.
- **MemoPilot** `2606.08656` — confirmed **ICML 2026**.
- **HeRoN** — published in **Neural Computing and Applications** (journal), not an arXiv preprint.
- **Affective Game Adaptation** / **Pacing-Aware Level Generation** — published in **PACM HCI** and **I3D Companion '26** respectively (non-arXiv venues surfaced via ACM).

### 9.3 Sibling-collision notes
- **AAArena** `2610.12341` and **Learn2Play Bench** `2610.08215` remain **claimed by same-day / recent siblings** (`arxiv-ai-search.md`, `conference-digest.md`) and are **not re-featured** here.
- **Cutscene Agent** `2604.25318`, **AutoUE** `2603.07106`, **GameHorizon** `2609.25001`, **MirrorCraft** `2607.29218`, **MineExplorer** `2605.30931`, **AI LOD** `2606.06565`, and the 10-10 Game RL set are **intentionally not re-featured** (featured in the immediately preceding edition).
- **arXiv announcement frontier** has not advanced past the 2026-10-08 block; consistent with today's siblings, **no fresh in-window game-RL paper** is claimed.
