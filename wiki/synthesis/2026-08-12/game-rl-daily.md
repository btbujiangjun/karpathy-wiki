---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-12)"
type: synthesis
created: 2026-08-12
updated: 2026-08-12
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, game-theory, multi-agent-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-08-12)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.
>
> **Coverage note**: This is a **deep-scan follow-up** over the Wed Aug 12 arXiv window. The Tue Aug 11 digest ([[2026-08-11/game-rl-daily]]) covered submitted Aug 8–10 papers up to ID ~2608.09926 but missed several strong Aug 10 submissions; today's batch is the Aug 11 submission wave (IDs ~2608.10325–2608.11208) plus the late-Aug-10 tail (IDs ~2608.10008–2608.10324) plus recall fill-in of Aug 10 papers (IDs ~2608.09000–2608.09926) still absent from the wiki. **13 papers total**, every one **grep-verified absent** from the entire wiki (0 hits in index/log/synthesis/**). Cross-checked for zero overlap with same-day [[2026-08-12/arxiv-daily]], [[2026-08-12/arxiv-paper-check]], [[2026-08-12/arxiv-ai-search]], [[2026-08-12/conference-digest]] and all prior digests.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Regret, equilibrium, and learning in games: A guided tour
- **Authors**: Panayotis Mertikopoulos
- **Affiliation**: CNRS / Univ. Grenoble Alpes (inferred)
- **Venue**: Book chapter — "Equilibria in Games: Existence, Selection, and Dynamics" (eds. Sylvain Sorin, Bernhard von Stengel); arXiv:2608.09389 (Aug 10, 2026)
- **Abstract**: An entry-point survey of learning in games, structured around two viewpoints: a single learner in an unknown non-stationary (possibly adversarial) environment, and several interacting agents seeking individual rewards. Examines regularized learning policies based on best-responding to past play plus a regularization penalty for exploration. Presents basic regret bounds for regularized learning in adversarial multi-armed bandits (single-agent), an ergodic equilibrium convergence result for zero-sum games in the spirit of fictitious play, and a "folk theorem" linking Nash equilibria to attracting points of regularized learning (multi-agent). Covers both oracle- and payoff-based (bandit) methods through a unified analysis framework.
- **Key Innovation**: A coherent, comprehensible unification of regularized learning (FTRL-style) across single-agent regret and multi-agent equilibrium dynamics — useful as a map of the game-RL theory underlying self-play agents.
- **Link**: https://arxiv.org/abs/2608.09389

### 1.2 Tracking the Best Strategy in an Extensive-Form Game
- **Authors**: Stephen Pasteris; Rahul Savani; Theodore Turocy
- **Affiliation**: UCL / University of Liverpool / University of East Anglia (inferred)
- **Venue**: arXiv:2608.09501 (Aug 10, 2026)
- **Abstract**: Considers the extensive-form bandit problem: on each trial the learner plays an extensive-form game against an oblivious adversary, tracking **switching regret** (expected performance versus any switching sequence of mixed strategies in retrospect). The algorithm takes a parameter ρ>0 and achieves switching regret Õ((1/ρ + ρK)√(HAT)) where K = comparator switches, H = max information sets traversed per play, A = learner's action count. Per-trial time is only O(HB), where B is max actions per information set.
- **Key Innovation**: An extremely efficient (O(HB)/trial) switching-regret algorithm for extensive-form games — a direct algorithmic handle on non-stationary opponents, relevant to game RL agents that must adapt to changing strategies.
- **Link**: https://arxiv.org/abs/2608.09501

### 1.3 Distributed Team Orchestration via Supervisor Networks (DTOA)
- **Authors**: Juntian Zhu; Guanpu Chen; Tongtian Zhu; Miguel de Carvalho; Zhouwang Yang; Fengxiang He
- **Affiliation**: USTC / Univ. of Edinburgh (de Carvalho, inferred)
- **Venue**: arXiv:2608.09256 (Aug 10, 2026)
- **Abstract**: Studies **zero-sum potential team games with a supervisor network**, where agents rely on supervisor-provided belief information rather than accurate common beliefs, which can be corrupted by belief-estimation errors and misreporting by Byzantine teams. Proposes the Distributed Team-Orchestrating Algorithm (DTOA), combining team fictitious play with supervisor-based distributed belief learning. Proves convergence of supervisors' belief estimates and that the induced dynamics converge to a near team-Nash equilibrium (TNE) in terms of team-Nash gap (TNG). Under misreporting attacks, develops a Byzantine-resilient DTOA with probabilistic guarantees for Byzantine-team identification and an asymptotic bound on honest TNG.
- **Key Innovation**: First distributed team-game algorithm robust to supervisor belief errors *and* Byzantine teams, with near-TNE convergence guarantees — a theory contribution to adversarial MARL/team games.
- **Link**: https://arxiv.org/abs/2608.09256

---

## 2. Game AI Bot — LLM Agents in Games

### 2.1 The Politician, the Liar, and the Obedient Worker: Emerging Behavior of LLM Agents in Hierarchical Games
- **Authors**: Fatemeh Seyedin; Adrian Weller; Jinhyuk Yun; Mahmoudreza Babaei
- **Affiliation**: Univ. of Cambridge (Weller, inferred)
- **Venue**: arXiv:2608.09574 (Aug 10, 2026)
- **Abstract**: Introduces the **Hierarchical Game (HG)**, a public-goods game extended with managerial authority, democratic elections, and private communication, testing six frontier LLMs across twelve experiments adding institutions one at a time (speech, peers, government, wages, oversight, elections). Finds distinct behavioral profiles: Qwen promises and lies (13.3% broken promises); Grok refuses to cooperate alone but becomes fully cooperative under a manager who can punish (16%→100%); Claude and GPT-4o cooperate reliably at baseline. Honesty is fragile: paid manager roles drive all models except GPT-4o to cut private deals; anonymous punishment induces cheating in honest models; single-family groups lock the first elected manager in power indefinitely — leadership change only happens in mixed-family groups.
- **Key Innovation**: An incremental-institutions design isolating *which* governance mechanism changes LLM-agent behavior — evidence on free-riding, corruption, and entrenched leadership emerging in multi-agent LLM organizations.
- **Link**: https://arxiv.org/abs/2608.09574

### 2.2 Not a Monolith: Lab-Level Divergence in the Cooperative Equilibria of Chinese Frontier LLM Agents
- **Authors**: Francisco León Zúñiga Bolívar
- **Affiliation**: not stated
- **Venue**: arXiv:2608.10262 (Aug 10, 2026); companion to arXiv:2605.29874 under a fixed-converter design
- **Abstract**: Asks whether the cooperative bias documented for Western frontier LLM agents extends to a different alignment lineage, and whether Chinese models should be treated as a bloc or distinct labs. Studies DeepSeek V4 Pro, Qwen3-Max, Kimi K2.5, GLM-5.1 in an **evolutionary Iterated Prisoner's Dilemma** with a fixed converter (GPT-5.4 Mini) to decouple strategic disposition from coding ability. **H6 (not monolithic) is supported**: aggressive-equilibrium proportion P_A runs 1% (Qwen3-Max) to 9% (DeepSeek V4 Pro), with 4/6 pairwise comparisons surviving Holm-Bonferroni; within-ecosystem spread (8pp) exceeds the East-West mean gap (5.0% vs 5.0%). **H5 (cooperative-bias generality) is consistent but qualified**: cooperative plurality in 6/12 lab-prompt combos vs 9/12 for Western models.
- **Key Innovation**: The lab — not the ecosystem — is the unit at which cooperative disposition is set; directly relevant to comparing LLM game agents across alignment lineages.
- **Link**: https://arxiv.org/abs/2608.10262

### 2.3 CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems
- **Authors**: Aimilios Hadjiliasi; Louis Nisiotis
- **Affiliation**: Cyprus University of Technology (inferred)
- **Venue**: arXiv:2608.09848 (Aug 10, 2026)
- **Abstract**: Proposes a modular cognitive architecture for deploying embodied **Intelligent Virtual Agents (IVAs)/NPCs** in real-time interactive 3D virtual environments. Builds on the Sense-Think-Act paradigm and the Belief-Desire-Intention (BDI) cognitive model to bridge low-level reactive control (constrained by game engines) and high-level reasoning models (hard to deploy in virtual worlds). Aims to be a reusable, implementation-oriented template for deploying IVA "brains."
- **Key Innovation**: A reusable BDI + Sense-Think-Act hybrid architecture specifically targeting the game-engine deployment gap for cognitive NPCs — scalable, adaptive, explainable agents in complex interactive environments.
- **Link**: https://arxiv.org/abs/2608.09848

---

## 3. Game Foundation Models / World Models

### 3.1 FACT: Failure-Aware Causal Training for World-Action Models
- **Authors**: Quanquan Peng; Yutong Liang; Rui Yan; Nicklas Hansen; Xiaolong Wang
- **Affiliation**: not stated (Hansen, Wang = UC San Diego, inferred)
- **Venue**: arXiv:2608.10232 (Aug 10, 2026), cs.RO
- **Abstract**: World-action models (WAMs) co-train policies with future prediction, but are typically trained mostly on *successful* demonstrations, giving them little reason to predict consequences of bad actions. **FACT** is a causal WAM predicting future video and task progress conditioned on the executed action, so **failure rollouts supervise action consequences** — bad actions become valid future targets instead of being discarded. Failure-aware training makes the progress predictor aware of both successful and failed outcomes and can score sampled action candidates at inference. Outperforms many baselines on simulation and real-world bimanual manipulation, improves as failure data is added, and reduces success-biased future hallucination under bad actions.
- **Key Innovation**: Action-conditioned causal interface that turns failed rollouts into supervision — a failure-aware training recipe transferable to game/foundation world-model agents.
- **Link**: https://arxiv.org/abs/2608.10232

### 3.2 The Evaluation Protocol Determines the Result: An Independent Reproduction of LeWorldModel on TwoRoom
- **Authors**: Joyjeet Singh
- **Affiliation**: not stated
- **Venue**: arXiv:2608.10145 (Aug 10, 2026); independent reproduction of arXiv:2603.19312
- **Abstract**: Reproduces LeWorldModel (latent world model with a prediction loss + single anti-collapse regularizer) on TwoRoom for ~$25 of rented compute, reaching 94.0% goals at the repo's evaluation goal offset vs 84.0% for the authors' own checkpoint under identical episodes. Four conventions not in any released config determine the outcome (dense action gathering across a frameskip block, programmatically-set action-encoder width, ImageNet pixel normalization, action z-scoring). On the authors' own weights, the paper's appendix and repository config specify different goal offsets/step budgets yielding 14.0% vs 84.0%; changing only goal construction moves a checkpoint from 84.0% to 8.0%. **Two general findings**: (1) one-step prediction accuracy does not predict long-horizon planning success; (2) a batch-normalization layer inflated reported validation loss up to 300×, concealing a flat training loss.
- **Key Innovation**: A reproducibility post-mortem showing world-model evaluation protocol (goal offset, normalization, frameskip) can swing results by ~76 points — an evaluation-fidelity warning for game world models.
- **Link**: https://arxiv.org/abs/2608.10145

---

## 4. PCG — Procedural Content Generation

> **No new studio-authored or arXiv PCG papers in this window.** Ongoing threads unchanged: WorldClaw agentic 3D open-world generation ([[2026-08-08/game-rl-daily]]), Play2Code/PlaytestArena GUI-agent playtesting ([[2026-08-11/game-rl-daily]]), AutoBG board-game design assistant ([[2026-08-02/game-rl-daily]]).

---

## 5. Game Benchmarks

### 5.1 DSLE: A Learning Environment for Dark Souls Boss Encounters
- **Authors**: Derin Gezgin; Jim O'Connor; Tanner Goodwin; Gary B. Parker
- **Affiliation**: Connecticut College (Parker, inferred)
- **Venue**: AAAI Conference on AI and Interactive Digital Entertainment (AIIDE) 2026; arXiv:2608.09902 (Aug 10, 2026)
- **Abstract**: Introduces the **Dark Souls Learning Environment (DSLE)**, a containerized platform exposing all 22 boss encounters of Dark Souls: Remastered through a Gymnasium-style interface — real-time combat, high-dimensional visual input, sparse terminal rewards, each step a real action against the running game. Defines **DSLE-5**, a representative five-boss subset. Evaluates random, expert-system, evolutionary, PPO, and DQN agents from visual input: expert and evolutionary baselines defeat the tutorial boss Asylum Demon (63% / 43% peak win rates) but nothing beats the other four; PPO/DQN show no measurable learning (≤0.33% on the tutorial boss) within tens of wall-clock hours per run. Reports failures via survival time and damage dealt rather than win rate alone.
- **Key Innovation**: A hard, real-time, visual-sparse-reward commercial-game benchmark showing current deep RL fails entirely on modern action RPGs — a stress-test dataset for game-RL progress.
- **Link**: https://arxiv.org/abs/2608.09902

---

## 6. Industry Game AI

> **No new studio-authored submissions in this window.** Cross-referenced industry threads remain tracked: EA SPORTS NHL 26 automated testing ([[2026-08-01/game-rl-daily]]), KRAFTON PUBG ALLIE / inZOI Smart Zoi ([[2026-07-17/game-rl-daily]], [[2026-07-29/game-rl-daily]]), NVIDIA ACE/NVIGI/NitroGen + γ-World ([[2026-07-13/game-rl-daily]], [[2026-07-27/game-rl-daily]], [[2026-08-10/conference-digest]]), Tencent WorldClaw ([[2026-08-08/game-rl-daily]]).

---

## 7. Related Techniques — Game Theory, Inverse RL, Curiosity-Driven Exploration

### 7.1 Decision-Focused Learning in Network Interdiction Games (A-DFL)
- **Authors**: Luca M. Hartmann; Parinaz Naghizadeh
- **Affiliation**: Ohio State University (Naghizadeh, inferred)
- **Venue**: GameSec 2026 (Conference on Game Theory and AI for Security); arXiv:2608.09036 (Aug 10, 2026)
- **Abstract**: Studies decision-focused learning (DFL) in **shortest-path network interdiction (SPNI) games**, a Stackelberg game where an interdictor (leader) strengthens network arcs while an evader (follower) with cost uncertainty uses an ML predictor to pick a shortest path. Shows DFL faces a structural failure in this game setting: its objective admits a broad **decision-equivalence class of cost estimators** achieving zero nominal loss yet failing under interdiction, reversing DFL's usual advantage over prediction-focused learning (PFL). Proposes **Adversarial DFL (A-DFL)**, replacing nominal training samples with interdicted scenarios to collapse the harmful equivalence class. Experiments on synthetic and real networks confirm A-DFL restores DFL's advantage.
- **Key Innovation**: Identifies and fixes a game-theoretic failure mode of end-to-end decision-focused learning (Stackelberg interdiction), with an adversarial training fix.
- **Link**: https://arxiv.org/abs/2608.09036

### 7.2 Competitive mediator games and urban CAV routing markets
- **Authors**: Grzegorz Jamróz
- **Affiliation**: University of Warsaw (inferred)
- **Venue**: arXiv:2608.09894 (Aug 10, 2026)
- **Abstract**: Introduces **competitive mediator games** and their equilibria, generalizing (coarse) correlated equilibria — motivated by future autonomous routing and driving (ARAD) markets. Proves that in the generic setting of anonymous congestion (routing) games with market-share-maximizing mediators, **all competitive mediator equilibria are monopolies** whenever one mediator is weakly preferred by all users. Applies results to markets of competing ARAD service providers and discusses mechanism design.
- **Key Innovation**: A new equilibrium concept (competitive mediator equilibrium) between market design and algorithmic game theory, with a monopoly structural result for routing markets — relevant to AI-agent marketplaces and game-theoretic routing.
- **Link**: https://arxiv.org/abs/2608.09894

### 7.3 Efficient Hypergradient Descent for Inverse Reinforcement Learning
- **Authors**: Nikita Sevriukov; Anna Barabanova; Uliana Gagarina; Karina Ivanova; Sofiia Kasaeva; Ilya Levin; Marina Sheshukova
- **Affiliation**: not stated
- **Venue**: arXiv:2608.11052 (Aug 11, 2026)
- **Abstract**: Treats IRL as a bilevel optimization problem (inner = policy optimization under learned reward, outer = discrepancy vs expert data). Shows that at the inner optimum, the Hessian of the inner objective is proportional to the policy's Fisher information matrix, yielding a structured Fisher-based hypergradient closely related to Natural Hypergradient Descent. Approximates the inverse-Fisher-vector product with a **streaming spectral sketch** to avoid building large Fisher matrices. Competitive policy performance and strong reward-ranking quality on discrete- and continuous-control environments, with reduced curvature-storage complexity.
- **Key Innovation**: A scalable Fisher-sketching hypergradient for bilevel IRL — practical for learning reward functions from expert game/task demonstrations.
- **Link**: https://arxiv.org/abs/2608.11052

### 7.4 EDPFRL-IM: Exploration-Driven Personalized Federated RL via Intrinsic Motivation
- **Authors**: Md Rafid Islam; Rafsan Jany; Zahid Hasan; Ratun Rahman
- **Affiliation**: not stated
- **Venue**: arXiv:2608.10499 (Aug 11, 2026)
- **Abstract**: Adds **curiosity-driven exploration** to personalized federated RL: each client adds an intrinsic Random Network Distillation (RND) signal to its extrinsic reward to explore previously unseen state spaces; the server sends global exploration priors and collects minimal novelty summaries, never raw experiences or gradients. Outperforms average PFRL benchmarks in policy personalization and sample efficiency, mainly in delayed and sparse reward systems.
- **Key Innovation**: Privacy-preserving, coordinated curiosity exploration for federated RL — relevant to distributed game-agent/exploration pipelines.
- **Link**: https://arxiv.org/abs/2608.10499

---

## Summary Statistics

- **Total new papers**: 13 fully listed (verified NEW via grep against the entire wiki), across 6 of 7 categories
- **Fresh window (submitted Aug 10–11, 2026)**: 13 papers — guided tour of learning in games, extensive-form switching regret, DTOA team games, Hierarchical Games, Not a Monolith, CEAA, FACT, LeWorldModel reproduction, DSLE, A-DFL, competitive mediator games, IRL hypergradient, EDPFRL-IM
- **PCG / Industry**: no new submissions this window (cross-referenced threads noted)
- **Key venues**: AAAI AIIDE 2026 (DSLE), GameSec 2026 (A-DFL), book chapter (guided tour), arXiv preprints
- **Notable trends**:
  - **LLM agents in games become an institutional-design laboratory**: Hierarchical Games (incremental governance institutions) and Not a Monolith (lab-level divergence in cooperative equilibria) both treat multi-agent LLM behavior as an empirical phenomenon with measurable equilibria — the "governance failure modes" thread now has replicable protocols
  - **World models under audit**: FACT turns failure rollouts into training signal (opposite of success-biased data), while the LeWorldModel reproduction shows evaluation protocol alone swings results ~76 points — fidelity now includes *what failed and how we measured*, not just generated pixels
  - **Game RL theory returns to non-stationarity and teams**: extensive-form switching regret and DTOA (Byzantine-robust team fictitious play) push game RL from fixed-adversary to dynamic-opponent/team settings
  - **Modern action RPGs remain unlearnable for current deep RL**: DSLE's negative result (PPO/DQN ~0% on non-tutorial bosses) is a sobering stress-test for game-RL claims
  - **Security games and market games import ML tooling**: A-DFL shows decision-focused learning fails structurally in Stackelberg settings; competitive mediator games generalize correlated equilibria for AI-mediated routing markets

## Cross-References

- [[2026-08-11/game-rl-daily]] — prior digest (Sekai2, LDR, Khora, Twin Rollouts, WorldSimProbe, VERDI, Social Gym; covered up to ~2608.09926)
- [[2026-08-10/game-rl-daily]] — prior digest (MDT solver-guided poker, Aftab, MemWM, Dueling World Models, WorldTrace)
- [[2026-08-12/arxiv-daily]] — same-day breadth digest (fresh window 2608.10325–2608.11208; Game of Marginal Utilities in its Games/GT section — zero overlap with this digest)
- [[2026-08-12/arxiv-ai-search]] — same-day search digest (Safe Observation Capacity for poker exploitation 2608.09954; ContractSim 2608.10475 in its Games/Mechanism section — zero overlap)
- [[2026-08-12/conference-digest]] — GPT-Red self-play red-teaming, CoCo world-model debiasing (2608.04653)
- [[2026-08-10/conference-digest]] — γ-World (NVIDIA), Google embedded Bayesian game theory
- [[2026-07-27/game-rl-daily]] — SPIRAL/STRATAGEM self-play reasoning, NitroGen, OmniGameArena benchmarks
