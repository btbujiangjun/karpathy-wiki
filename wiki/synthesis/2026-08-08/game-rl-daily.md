---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-08-08)"
type: synthesis
created: 2026-08-08
updated: 2026-08-08
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, multi-agent-rl, llm-agents]
sources: []
---

# Game RL & Game AI Bot — Daily Synthesis (2026-08-08)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Verified via arXiv abs pages (fresh window Aug 4–8, 2026). Complements the [[2026-08-04/game-rl-daily]] digest with **no overlap** — every paper below was confirmed absent from the wiki before inclusion. Two edge submissions (SyncPlan, OASE) are Aug 3 but were missed by the 08-04 digest; they are included here after confirming they are absent from all prior dailies.

---

## 1. Game RL — Reinforcement Learning in Games

### IFlowNets: Extending Generative Samplers to Learn Strategies in Incomplete Information Games
- **Authors**: Conor M. Artman, Nicholas Di, Scott Perkins
- **Affiliation**: —
- **Venue**: arXiv:2608.05422 (Aug 5, 2026); accepted at NeurIPS 2025 Workshop on Dynamics at the Frontiers of Optimization, Sampling, and Games
- **Key Innovation**: Extends Adversarial Flow Networks (AFlowNets) to incomplete information games via **Information Flow Networks (IFNs)**, proving that the constraints used for generative flow networks in complete information games are inadmissible for producing valid strategy densities and a valid training objective in imperfect information. IFlowNets strictly generalizes AFlowNets and performs comparably or better than Outcome Sampling Monte Carlo CFR (OSMCCFR) and standard RL baselines on three standard game environments. Bridges the generative-sampling and counterfactual-regret literature for imperfect information games.
- **Link**: https://arxiv.org/abs/2608.05422

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction
- **Authors**: Shen You, Xiaoming Zhu, Weining Weng, Hefei Mei, Weixuan Wang, Zhongshen Li
- **Affiliation**: —
- **Venue**: arXiv:2608.01652 (Aug 3, 2026)
- **Key Innovation**: A plan-execute-correct framework for long-horizon LLM multi-agent coordination. A centralized LLM coordinator generates per-agent action chains in a single planning call; explicit wait primitives + deadlock detection enforce inter-agent and agent-environment dependencies during execution, and a lightweight **Plan Staleness Detector** triggers replanning when environmental changes invalidate assumptions. Optimized via SFT + planning-oriented RL with dense task-progress and outcome-level feedback. On Overcooked and **Honor of Kings**, achieves state-of-the-art task success rates while using **<0.05% of wall-clock runtime** versus existing LLM coordinators — directly relevant to real-time MOBA game agents.
- **Link**: https://arxiv.org/abs/2608.01652

### Emotion Dynamics in Social Deception Games (Werewolf)
- **Authors**: Sho Mitarai, Chang Liu, Goshiro Yamamoto, Nagisa Munekata
- **Affiliation**: —
- **Venue**: arXiv:2608.04605 (Aug 5, 2026)
- **Key Innovation**: Physiological study (electrodermal activity, EDA) of how humans manage emotions in social deception games like Werewolf. Professional players maintained persuasion-based communication under high arousal with more stable emotional states (better regulation); non-professional players shifted to information-focused communication. Statistical analysis shows significant differences in expression patterns by expertise level. Informs the design of emotionally intelligent AI agents that adapt communication strategy to recipient characteristics in deception/social-deduction games — complements CaM-Wolf-style social deduction research ([[2026-08-01/game-rl-daily]]).
- **Link**: https://arxiv.org/abs/2608.04605

### Cross-reference: VLM-annotated game data (NVIDIA)
- The pair **VLMs for Videogame Data Annotation** (2608.05949) and **Training a Conditioned Video Game Agent on a VLM-Annotated Dataset** (2608.05954) by Katrin Schmid & Iuri Frosio (NVIDIA) fall in this window but are **already covered** in today's broader [[2026-08-08/arxiv-daily]]. They are not re-listed here to avoid duplication.

---

## 3. Game Foundation Models — Generalist Game Agents & World Models

### MASS: Multiplayer World Models with Authoritative Shared State
- **Authors**: Ziqi Cai, Siqi Yang, Yimu Wang, Zixian Gao, Yunheng Liu, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi
- **Affiliation**: — (incl. Peking University / Key Laboratory of Machine Perception)
- **Venue**: arXiv:2608.06257 (Aug 6, 2026)
- **Key Innovation**: Brings the authoritative-server architecture of online multiplayer games to learned world models. MASS disentangles world dynamics from view rendering: a learned **Logic Engine** advances a global, authoritative typed state from joint actions (no hand-written transition function, sole recurrent memory + synchronization reference), and a learned **Rendering Engine** generates independent, consistent views for any camera on demand. Reaches 0.76 state recovery on a matched multiplayer Snake benchmark vs 0.128 for the strongest video-based baseline, advances **1,024 concurrent players for 10,000 recurrent steps**, and supports cross-game schemas, versioned snapshots, and client-side prediction during update stalls. Addresses the redundant-compute/view-inconsistency failure of visual-latent multiplayer world models (MultiWorld, MultiGen, WanToFight) and extends the multiplayer world-model line (cf. Rocket League model in [[2026-08-02/game-rl-daily]]).
- **Link**: https://arxiv.org/abs/2608.06257

---

## 4. Procedural Content Generation (PCG)

### WorldClaw: Agentic 3D Open-World Generation at Scale
- **Authors**: Chunchao Guo, Jinpeng Li, Yang Li, Zilong Huang
- **Affiliation**: Tencent Hunyuan
- **Venue**: arXiv:2608.05248 (Aug 5, 2026)
- **Key Innovation**: A fully agentic, coarse-to-fine framework for large-scale, freely explorable 3D open worlds from open-ended text. Planning agents translate prompts into structured specifications (regions, terrain, assets, materials, spatial relations); WorldClaw builds a globally coherent terrain foundation from semantic layouts, reusable assets, generative/procedural materials, and a region-aware height field; detail-demanding regions get terrain-conditioned compositions, editable textured meshes, and recovered placement; render-based agents refine terrain/objects/appearance/contacts. Produces large-scale scenes with coherent spatial organization, compelling local content, and editable instance-level assets while preserving global terrain consistency — an explicit-assets approach that contrasts with pure video world generators and suits downstream game-engine reuse.
- **Link**: https://arxiv.org/abs/2608.05248

---

## 5. Game Benchmarks

### ACT-Eval: Hallucinations on the Board — Tool-Augmented Evaluation of LLM Chess Commentary
- **Authors**: S. Ashwin Hebbar, Peiyao Sheng, Sewoong Oh, Pramod Viswanath
- **Affiliation**: University of Illinois Urbana-Champaign (likely)
- **Venue**: arXiv:2608.04240 (Aug 4, 2026)
- **Key Innovation**: ACT-Eval decomposes LLM chess commentary into atomic claims and routes them to engine-supported tools + expert-annotated gold references to assess factual correctness, conceptual coverage, and move-quality judgment. Releases a benchmark of **325 position–move pairs** (125 with expert-verified gold atoms) and a five-class error taxonomy. Finds factual hallucinations remain pervasive: GPT-5.4 without tools produces incorrect sub-claims 22.0% of the time; smaller open-weight models exceed 40%. Tool augmentation substantially improves factual correctness and move-quality, but coverage of expert strategic/tactical ideas stays limited across all models. Human calibration shows factual judgments fall within inter-human agreement while coverage correlates strongly with human strategic-completeness ratings. Model-agnostic (usable with any engine-supported game).
- **Link**: https://arxiv.org/abs/2608.04240

### AI World Cup 2026: Benchmarking LLMs for End-to-End Football Tournament Prediction
- **Authors**: Jonaid Shianifar, Iias Faiud
- **Affiliation**: AI World Cup Project (independent; Shianifar research intern at Huawei Ireland / Univ. of Galway)
- **Venue**: arXiv:2608.03416 (Aug 4, 2026); completed 2026 FIFA World Cup benchmark
- **Key Innovation**: A completed, reproducible tournament-forecast benchmark: ten LLM-based assistants each made a single pre-tournament forecast of the entire 2026 FIFA World Cup under identical snapshot/prompt/JSON schema/scoring. After all 104 matches, **GPT-5.5 Thinking won (744 pts)** and was the only model to pick Spain (which beat Argentina 1–0 in the final); GPT-5.5 717, Gemini 699, Qwen 3.7 687. Ranking was driven by knockout points (r=0.986 with total) with almost no relationship to group-stage performance (r≈0.05); match-level accuracy produced a different ordering (Claude Sonnet 4.6 best at 63.89% group-stage accuracy but sixth overall). Self-reported confidence was uncorrelated with accuracy or score. Benchmark materials/raw responses/scoring code released. Relevant to LLM game/competition forecasting and sports game AI.
- **Link**: https://arxiv.org/abs/2608.03416

---

## 6. Industry Game AI

> **No new industry papers this cycle.** Ongoing industry threads tracked elsewhere: KRAFTON PUBG ALLIE on-device agents ([[2026-07-17/game-rl-daily]]), NVIDIA ACE/NVIGI SDK ([[2026-07-13/game-rl-daily]]), PCSP UE5 deployment at 64 agents (2605.23652), EA SPORTS NHL 26 production RL (2607.07498, [[2026-08-01/game-rl-daily]]), TerraZero procedural driving sim (2607.13028, [[2026-08-02/game-rl-daily]]), Tencent Hunyuan's WorldClaw (Section 4) is the notable games-adjacent industry contribution this window.

---

## 7. Related Techniques — Self-Play, World Models, Multi-Agent RL

### OASE: Opponent-Aware Selective Evolution via History-Informed Opponent Awareness
- **Authors**: Zhaofeng Zhang, Linhan Xia, Rui Liu, Yihao Wang, Binrui Shen, Shengxin Zhu
- **Affiliation**: —
- **Venue**: arXiv:2608.02005 (Aug 3, 2026)
- **Key Innovation**: Addresses skill-revision self-evolution when opponents simultaneously update their strategies (the environment itself evolves, making naive skill updates target an obsolete reference). **OASE** performs paired comparisons between a candidate skill and the incumbent under identical conditions anchored by historical snapshots of opponent strategies, adopting the candidate only when estimated payoff gain exceeds an acceptance threshold. In first-price auctions and private-cost Cournot competition, OASE achieves lower final equilibrium distance than a Reflexion-style baseline while accepting substantially fewer revisions — evidence-anchored strategy evolution for competitive multi-agent environments (relevant to adversarial/competitive game agents).
- **Link**: https://arxiv.org/abs/2608.02005

### Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks
- **Authors**: Christophe D. Hounwanou, John Emeka Eze, Yaé Ulrich Gaba
- **Affiliation**: —
- **Venue**: arXiv:2608.03502 (Aug 4, 2026)
- **Key Innovation**: Integrates LLM-driven planning with RL action optimization in a hybrid architecture: the LLM generates subgoals, structured plans, and contextual guidance while the RL agent refines low-level actions through environment interaction. On sequential decision tasks, the hybrid shows improved sample efficiency, higher success rates, and more coherent action trajectories than RL-only and LLM-only baselines — a template for LLM/RL hybrid game agents in long-horizon tasks (echoes the LLM+RL NPC line: HeRoN, PA-MAGRPO in [[2026-08-04/game-rl-daily]]).
- **Link**: https://arxiv.org/abs/2608.03502

### ADRS: Agentic RL with Self-Distilled Reward Shaping
- **Authors**: Ranxu Zhang, Guinan Chen, Jinghao Lin, Xiaozhou Xu, et al.
- **Affiliation**: —
- **Venue**: arXiv:2608.03223 (Aug 4, 2026)
- **Key Innovation**: Constructs return-associated token-level credit for multi-turn language agents. A frozen policy snapshot rescored on skill-free trajectories (training-only privileged skills) provides dense supervision; ADRS centers/normalizes privileged token scores per step, modulates them with a return-associated **Teacher Value Advantage (TVA) gate** based on within-group confidence–return association, and integrates the gated signal into native reward-to-advantage construction — while keeping rollouts and inference skill-free. Improves long-horizon performance across three interactive benchmarks with gains persisting across RL backbones, reduced-data settings, unseen tasks, and extended training. Addresses sparse-reward credit assignment for agentic/game-like interactive tasks.
- **Link**: https://arxiv.org/abs/2608.03223

### AI Agent Economics: Can Autonomous Economic Behavior Emerge among AI Agents under Minimal External Conditions?
- **Authors**: Lingyun Zhang, Shang Shang
- **Affiliation**: —
- **Venue**: arXiv:2608.03076 (Aug 4, 2026)
- **Key Innovation**: Distinguishes endogenous economic organization from scenario-inherited behavior by giving six-agent worlds executable mechanisms for work, transfer, elections, and allocation with no prescribed social/economic strategy. Without productive tasks, agents communicate and govern resource provision but show no substantive inter-agent transfer; with verified work and scarce task access, transfers, loans, access promises, vote-for-access exchanges, and allocation strategies emerge. Holding the election interface fixed, executable allocation authority increases differentiation while reducing failed allocation and prolonged exclusion. Conclusion: organization follows **executable rights and resource consequences rather than role labels or prompt language** — a governance-audit perspective relevant to economic-game agent design and multi-agent world models.
- **Link**: https://arxiv.org/abs/2608.03076

### Computationally Efficient Collaborative Communication via Regularity-Based Coarsening
- **Authors**: Mark Bedaywi, Scott Emmons, Nika Haghtalab, Stuart Russell
- **Affiliation**: UC Berkeley
- **Venue**: arXiv:2608.05327 (Aug 5, 2026)
- **Key Innovation**: Theoretical result: existence of a short high-utility communication protocol suffices for efficient communication in games. For n observations and m actions, a poly(n,m,1/ε) algorithm designs a protocol achieving utility α−ε using only 2^{O(CC_α(G))}/ε² bits, where CC_α(G) is the minimal protocol bit-count; exponential dependence is tight unless P=NP. Proves prior structural assumptions (informational substitutes, weak learnability) are strictly stronger than needed. Introduces a strengthening of the Frieze–Kannan weak regularity lemma that coarsens observation spaces into constant-size partitions indistinguishable to every short protocol. Grounds efficient inter-agent communication design in cooperative multi-agent games (foundational MARL/communication theory).
- **Link**: https://arxiv.org/abs/2608.05327

---

## Summary Statistics

- **Total new papers**: 8 fully listed + 1 cross-referenced pair (NVIDIA VLM annotation papers, covered in today's arxiv-daily)
- **Categories with new papers**: 5 of 7 (Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Related Techniques); Industry Game AI had no new papers this window
- **Key venues**: arXiv (Aug 2026); one NeurIPS 2025 workshop-accepted paper
- **Notable trends**:
  - **Multiplayer world models adopt authoritative-server design**: MASS brings typed, versioned, server-authoritative state to learned world models, scaling to 1,024 concurrent players — a structural fix for view inconsistency in visual-latent world models
  - **Agentic 3D world generation arrives in industry**: Tencent Hunyuan's WorldClaw produces editable, explicit-asset open worlds for game-engine reuse, contrasting with pure video-generative world proxies
  - **LLM coordination for games moves to plan-execute-correct**: SyncPlan's centralized single-shot plan + staleness-triggered replanning cuts coordination runtime by >99.95% in Honor of Kings
  - **Incomplete-information game RL advances on the sampling side**: IFlowNets proves a correct generative-flow training objective for imperfect information games, competing with OSMCCFR
  - **LLM evaluation extends to games commentary**: ACT-Eval (chess) tool-verified atomic claims show pervasive hallucination (>22%) that tools partially fix; AI World Cup shows tournament-forecast leaderboards are dominated by knockout-point scoring design
  - **Evolving opponents demand evidence-anchored adaptation**: OASE replaces blind skill updating with payoff-anchored selection as opponents co-evolve
