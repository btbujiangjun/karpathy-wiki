---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-22)"
type: synthesis
created: 2026-08-22
updated: 2026-08-22
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, reinforcement-learning, world-models, diffusion-lm, auction-theory]
---

# arXiv Recent Papers — AI, LLM, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-22 · Scope: papers not yet covered anywhere in the wiki (dedup verified by grep against every existing page). Fresh wave = Fri Aug 14 – Fri Aug 21 submission window (IDs ~2608.15xxx–2608.20xxx). No new CTR / recommendation / sequential-modeling papers found today — all candidates were already covered by sibling digests (see Coverage Notes). 10 new papers below across 4 categories.

## 1. LLM Reasoning & Post-Training

---

### 1.1 Continual Reasoning Gym: Shared Reasoning in Continual RLVR

| Field | Detail |
|-------|--------|
| **Title** | Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR |
| **Authors** | Lirui Luo, Guoxi Zhang, Hongming Xu, Rongqing Li, Cong Fang, Lifeng Fan |
| **Institution** | Peking University + Beijing Academy of AI (inferred from author roster — not stated in metadata, tentative) |
| **arXiv** | https://arxiv.org/abs/2608.18574 |
| **Date** | 2026-08-19 |

**Abstract:** Multitask RLVR (MTRL) retrains reasoning models jointly as new tasks arrive, which is costly at scale. The paper studies continual RLVR — updating an existing model each time a task arrives — and asks whether sequential updates can match joint training. Continual Reasoning Gym organizes text and visual reasoning tasks into five task sequences to answer this systematically.

**Key Innovations:**
- Diagnosis: sequential RLVR shows only modest forgetting, yet final performance still trails MTRL — decomposing the gap shows forgetting explains only part of it
- Identifies **shared reasoning**: transferable reasoning structure lets training on one task support others on average (the missing ingredient is harnessing it, not preventing forgetting)
- **Continual Prompt Replay (CPR):** replay previous-task prompts but regenerate responses with the current policy — only method that reaches MTRL-level performance on average
- Practical implication: capability expansion can be incremental without full retraining, if transfer structure is actively exploited

---

### 1.2 Nested Sequential Monte Carlo for Discrete Diffusion LM Control

| Field | Detail |
|-------|--------|
| **Title** | Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo |
| **Authors** | Lohithsai Yadala Chanchu, Hany Abdulsamad, Christian A. Naesseth |
| **Institution** | University of Amsterdam + collaborators (inferred — not stated in metadata, tentative) |
| **arXiv** | https://arxiv.org/abs/2608.20123 |
| **Date** | 2026-08-20 |

**Abstract:** Inference-time steering of discrete diffusion language models toward sequence-level rewards without retraining. Prior particle-based methods have complementary failure modes: best-of-n suffers overoptimism, bootstrap SMC suffers weight degeneracy. The paper formulates nested SMC (NSMC) and fully-adapted nested SMC (FA-NSMC) for Feynman–Kac steering.

**Key Innovations:**
- Nested SMC replaces flat particle populations with nested estimators inside the Feynman–Kac framework, attacking both overoptimism and weight degeneracy simultaneously
- Identifies and corrects biased formulations in prior nested-SMC-for-diffusion attempts
- **Results:** consistently outperforms best-of-n and bootstrap SMC on toxicity and fluency steering for discrete diffusion LMs
- Complements objective-level fixes like PCD ([2026-08-21 digest](../2026-08-21/arxiv-ai-search.md)): control at inference vs alignment at pretraining

---

## 2. Latent World Models & Learned Planning

---

### 2.1 Orthogonal JEPA: Factorized Predictive States

| Field | Detail |
|-------|--------|
| **Title** | Orthogonal JEPA: Factorized Predictive States for Latent World Models |
| **Authors** | Taoyong Cui, Pheng Ann Heng, Wanli Ouyang |
| **Institution** | CUHK + Shanghai AI Laboratory |
| **arXiv** | https://arxiv.org/abs/2608.20065 |
| **Date** | 2026-08-20 |

**Abstract:** Standard JEPAs squeeze all predictable content through one target embedding and one prediction pathway; in complex systems this monolithic state wastes capacity on dominant signals while giving weak/conflicting gradients to less dominant structure. Orthogonal JEPA factorizes the predictive state: learned basis matrices decompose each target state into components, each predicted by its own branch from a shared context representation, then synthesized back into a complete latent state usable by planners or decoders.

**Key Innovations:**
- Orthogonal predictive factorization: one target → multiple non-redundant components, each with a dedicated prediction branch
- Regularization quartet: magnitude-preserving predictive regression, orthogonality loss against repeated directions, factor-activity regularization, online variance regularization against encoder collapse
- One mechanism covers temporally future, spatially hidden, or partially observed targets
- **Results:** evaluated across vision, single-cell transcriptomics, longitudinal health records, continuous control, and molecular dynamics — improved representation quality, forecasting, planning, long-horizon stability

---

### 2.2 DA-LeWM: Making Latent Distances Decision-Safe for MPC

| Field | Detail |
|-------|--------|
| **Title** | Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning |
| **Authors** | Jiawei Wang, Ke Rui, Yushen Zuo, Yichun Feng, Minglei Li |
| **Institution** | Not stated in metadata |
| **arXiv** | https://arxiv.org/abs/2608.18746 |
| **Date** | 2026-08-19 |

**Abstract:** JEPA-style world models typically use Euclidean distance to a goal latent as MPC cost — but strong decoding of task variables does not guarantee that this cost ranks candidate action sequences by real task progress. The paper names this property *decision-metric alignment*, introduces two diagnostics (Plan-Real Spearman on random plans; CEM-stage Spearman as search concentrates), and analyzes when latent distance preserves real-cost rankings.

**Key Innovations:**
- Two cheap diagnostics that measure latent↔real rank agreement before deployment — encoder distortion, terminal rollout error, and candidate margins identified as controlling quantities
- DA-LeWM adds inverse-dynamics and demonstration-conditioned goal-action heads to LeWM, aligning the metric with decisions rather than reconstruction
- **Results:** faster convergence and higher online success than LeWM across experiments — while probe scores stay similar (decoding quality was never the bottleneck)

---

### 2.3 RP1: Learning to Improve Plans Instead of Hand-Designing Search

| Field | Detail |
|-------|--------|
| **Title** | Reinforced Planning with Latent World Models |
| **Authors** | Armin Sommer, Jannik Schilling |
| **Institution** | Not stated in metadata |
| **arXiv** | https://arxiv.org/abs/2608.18669 |
| **Date** | 2026-08-19 |

**Abstract:** Current planners over learned world models are hand-designed, distilled from hand-designed optimizers, or trained only to inform amortized policies — none actually learn to revise multi-step plans. RP1 learns both outcome evaluation (critic) and plan improvement (optimizer trained fully offline from imagined rollouts): search itself becomes a reinforcement learning problem.

**Key Innovations:**
- First method claimed to fully learn how to improve multi-step plans (vs executing fixed CCEM/MPC loops)
- Model-agnostic: trains independently of any pretrained latent world model and attaches to it
- **Results:** visual navigation, arm reaching, robotic manipulation × two world-model backbones — near-perfect success in several settings using **1000× fewer world-model rollouts**, up to **67× faster** than the strongest alternative under concurrent planner inference

---

## 3. Advertising & Auction Theory

---

### 3.1 One-Shot Pricing: No Auctions Needed in Hands-Off-the-Wheel Ad Markets

| Field | Detail |
|-------|--------|
| **Title** | One-Shot Pricing for Hands-Off-the-Wheel Advertising Markets |
| **Authors** | Emerson Melo, Matt Shum, Rakesh Vohra |
| **Institution** | Economics academia (Shum: Caltech; Vohra: U. Penn; Melo: UIUC/Tulane — inferred, tentative) |
| **arXiv** | https://arxiv.org/abs/2608.01591 |
| **Date** | 2026-08-03 |

**Abstract:** In hands-off-the-wheel (HOTW) markets, advertisers declare budgets and ROI targets while the exchange's ML models predict click values — so all information needed for optimal pricing already sits with the exchange, which faces a downward-sloping demand curve like a monopolist. Auctions become unnecessary: a HOTW market is a Fisher market whose competitive equilibrium comes from the Eisenberg–Gale convex program.

**Key Innovations:**
- Structural reframing: HOTW advertising = Fisher market → market-clearing prices/allocations satisfying budget + ROI constraints simultaneously
- Revenue optimality: the competitive-equilibrium uniform price is revenue-optimal among all uniform-price mechanisms — sidesteps demand reduction that plagues uniform-price multi-unit auctions
- Equivalence result: outcome-equivalent to sequential first-price auctions with pacing, but pacing multipliers computable **ex-ante** instead of learned dynamically
- Operational punchline: millions of per-impression auctions replaced by one convex program solve

---

### 3.2 Approximation Doesn't Save You: Hardness of Pacing & Throttling Equilibria

| Field | Detail |
|-------|--------|
| **Title** | Tight Inapproximability of Pacing and Throttling Equilibria in Second-Price Auctions |
| **Authors** | Zhengyang Liu |
| **Institution** | Not stated in metadata (single author) |
| **arXiv** | https://arxiv.org/abs/2608.16682 |
| **Date** | 2026-08-17 |

**Abstract:** Budget-constrained advertisers use two control mechanisms: pacing (scale bids) and throttling (randomize participation). The paper proves both share the same sharp hardness threshold in second-price auctions: computing a γ-approximate pacing equilibrium is PPAD-hard for every constant γ ∈ [0,1); same for δ-approximate throttling equilibria for every constant δ ∈ (0,1).

**Key Innovations:**
- First tight inapproximability for **throttling** equilibria, matching known pacing results — two practically distinct budget-management mechanisms sit at the identical fixed-point barrier
- Impossibility of escaping via approximation: at any nontrivial parameter value the complementarity problem remains intractable; only the degenerate all-zero solution at parameter 1 is easy
- Practical read: industrial auto-bidding systems relying on local dynamics (e.g., gradient-based pacing updates) have no polynomial-time guarantee to lean on — equilibrium-finding is intrinsically hard, not just under-studied

---

## 4. Games & Multi-Agent Systems

---

### 4.1 Solvable Sokoban Without a Solver via Diffusion

| Field | Detail |
|-------|--------|
| **Title** | Solvable Sokoban Without a Solver via Diffusion |
| **Authors** | Sina Baghal |
| **Institution** | Independent researcher (single author) |
| **arXiv** | https://arxiv.org/abs/2608.15958 |
| **Date** | 2026-08-16 |

**Abstract:** Sokoban solvability is PSPACE-complete and fragile — one misplaced wall silently kills a puzzle. Yet a transformer-based discrete diffusion model trained purely on tile completion (no solvers, rewards, or solvability labels, MD4 recipe, DeepMind Boxoban data) generates puzzles with 77.4% solvability, and 94.5% of remaining failures become solvable by removing a single wall.

**Key Innovations:**
- Emergent global constraint satisfaction: a search-heavy, globally-coupled property follows from a purely local masked-completion objective — the model inherits solvability it was never trained on
- Structural argument for masked diffusion over AR generation: revealing cells in any order, each conditioned on everything placed so far, matches Sokoban's non-local interaction structure better than fixed-order prefix conditioning
- Relevant to PCG pipelines in this wiki: diffusion generators may implicitly enforce hard combinatorial constraints without symbolic verification

---

### 4.2 UC-PSRO: Game-Theoretic COAs for Adversarial Swarms (with Honest Negative Results)

| Field | Detail |
|-------|--------|
| **Title** | UC-PSRO: Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum for Game-Theoretic Course-of-Action Generation in Adversarial Swarms |
| **Authors** | Phillip Jiang |
| **Institution** | Not stated in metadata (motivated by a public U.S. Air Force SBIR solicitation) |
| **arXiv** | https://arxiv.org/abs/2608.15372 |
| **Date** | 2026-08-15 |

**Abstract:** Generates game-theoretically optimized courses of action for a Blue UAS swarm against an adaptive Red adversary under communication degradation. Three combined mechanisms: PSRO self-play (both sides train as approximate best responses), FiLM conditioning of the Blue policy on a Commander's-Intent Dirichlet-sampled weight vector (one policy re-steerable at execution time), and a curriculum annealing communication-edge dropout for decentralized fallback.

**Key Innovations:**
- Communication-dropout curriculum is the star: mission completion improves counter-intuitively as denial increases (35% → 62% success as dropout rises 0 → 0.75) — strongest and most robust of any learned method
- Honest negative results, rare in this literature: utility-conditioning + PSRO self-play substantially slow convergence within fixed budget, and show **no reliable exploitability advantage over fixed-opponent training** (statistically indistinguishable from near-zero gap)
- Open fully-vectorized environment: N=200 agents training in single-digit ms/step on one consumer GPU

---

### 4.3 RoboStriker: Humanoid Boxing as a Latent-Space Zero-Sum Game

| Field | Detail |
|-------|--------|
| **Title** | RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing |
| **Authors** | Kangning Yin, Kaige Liu, Zhe Cao, Wentao Dong, Weishuai Zeng, Tianyi Zhang, Qiang Zhang, Jingbo Wang, Jiangmiao Pang, Yang Li, Ming Zhou, Weinan Zhang |
| **Institution** | Shanghai Jiao Tong University + Shanghai AI Laboratory + BAAI (inferred from author roster — not stated in metadata, tentative) |
| **arXiv** | https://arxiv.org/abs/2608.16195 |
| **Date** | 2026-08-17 |

**Abstract:** MARL applied directly to raw motor spaces in contact-rich humanoid boxing collapses at the joint level before tactics emerge. RoboStriker resolves the conflict between strategic exploration and physical feasibility by formulating combat as a two-player zero-sum Markov game **in latent space**: predefined boxing motions are distilled into a topologically bounded latent manifold, then multi-agent co-evolution runs as Neural Fictitious Self-Play over that manifold.

**Key Innovations:**
- Latent-space game formulation with theory: under regularity + approximate best-response assumptions, the latent game induces an equivalent game over the decoder-reachable action manifold → approximate-Nash interpretation of self-play dynamics
- Hierarchical decoupling: motion-tracked low-level controller provides physical plausibility; NFSP self-play operates above it
- **Results:** substantially outperforms raw action-space exploration; drastically reduces catastrophic balance failures; superior win rate and striking efficiency; policies deployed on real humanoid hardware

---

## Coverage Notes

- **CTR prediction / recommendation / sequential modeling:** no new papers this round. Every candidate surfaced (SCoRD 2608.19998, seq-rec benchmark higher-order question 2608.19833, Training-Free Post-LLM refinement 2608.19665, RecPFN 2608.19735, ERASE 2608.18469, rEDMRec 2608.18952, SIDScope 2608.18779, OneModel 2608.18606, Netflix multimodal personalization 2608.18322, slate GenRec 2608.17613, GOD 2608.16073, TRACER 2608.16075, Ask-to-Be-Sure 2608.15949, SAHC-NS 2608.16587, SAGA 2608.15429) is already covered in sibling digests of 08-19 / 08-20 / 08-21 (`arxiv-daily`, `arxiv-paper-check`).
- **Excluded as already covered elsewhere:** SPADE (2608.19197 — arxiv-daily 08-20 + game-rl-daily 08-21), MoE hyperparameter transfer (2608.20061 — arxiv-paper-check 08-21), MARCO (2608.10562 — multiple), MISO (2608.07035), PPAD auto-bidding (2608.01889), Co-RL (2608.17253), Debate-training reward hacking (2608.17776).
- **Strongest cross-cutting theme today: shape the space before you search it.** Four papers independently argue that structuring the action/state geometry beats brute-force search — RoboStriker (motion-manifold latent game), Orthogonal JEPA (orthogonal factorized predictive states), DA-LeWM (decision-aligned latent metric diagnostics), RP1 (learned plan improvement over latent rollouts, 1000× fewer rollouts). Secondary threads: auction-theory impossibility results closing in on practical auto-bidding (One-Shot Pricing's monopolist reframe + tight PPAD inapproximability), and diffusion models exhibiting emergent global properties from local objectives (Sokoban solvability; NSMC control).
