---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-24)"
type: synthesis
created: 2026-09-24
updated: 2026-09-24
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, industry-game-ai, self-play, marl, game-theory, model-based-rl, world-action-models, sim-to-real, test-generation, reward-design, agent-skills, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-24)

> **Methodology note**: **Thu 24 Sep 2026** mailing (processes Wed 23 Sep submissions). Fresh window = **IDs 2609.26809–2609.28473** (per today's sibling `/list/{cat}/new` parses: 388 unique IDs in cs.AI/LG/IR/CL/GT/MA/NE/CV). My pipeline used an **arXiv API tail sweep** (sorted by submittedDate descending) over **cs.AI / cs.LG / cs.CV / cs.CL / cs.GT / cs.MA / cs.NE / cs.RO / cs.HC** (9 cats × 2×100, cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/game-rl-daily-0924/`) → **1,526 unique entries parsed** → in-window filter [2609.26809–2609.28473] → **489 unique in-window IDs** → subtracted the whole-wiki known set (**5,839 IDs**, which already subsumes today's five sibling digests — arxiv-daily 52 / arxiv-ai-search 27 / arxiv-paper-check 23 / conference-digest 2 in-window / tech-report-digest) → **384 unclaimed** → title + abstract keyword sweep → **~24 targets** deepened at full-abstract depth → **20 curated + 4 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/`** at write time and sits inside the Thu-24 window (≥ 2609.26809).
>
> **Continuity / already-covered by the 09-24 siblings (cross-referenced, not re-featured):** the fresh window's *pure-game and world-model marquees* were taken hours ago by the same-day digests — **JEV-Star** 2609.27331 (fast JEV + GPT-6 planning defeats StarCraft II Lv7 at ~US$3.71/game) → [arxiv-daily 09-24 §7.5](../2026-09-24/arxiv-daily.md); **InternW0** 2609.27656 (foundational physical world model, Shanghai AI Lab) → §7.1; **Latent Evolving World Action Model (LeWAM)** 2609.27455 (JEPA-latent WAM, 92.28% RoboTwin 2.0) → §7.2; **Frozen Flows Forget** 2609.28414 (latent-flow world-model motion loss) → §7.3; **Agent-Editing World Model (AEWM)** 2609.28416 (edit the task state, don't simulate tools) → §6.1; **Verifiable Hidden Dynamics Play** 2609.27321 (LLM-generated agentic RL environments from solved mechanisms) → §2.5; **CAVEAT** 2609.28470 (incentive-misaligned computer-use agent benchmark) → §6.5. On the game-theory axis, [arxiv-ai-search 09-24](../2026-09-24/arxiv-ai-search.md) §6 owns **credible auctions via MPC** 2609.27402, **online fair division vs oblivious adversary** 2609.28333, **two-trader trade reduction** 2609.27304, **pacing equilibria** 2609.27285 and **evolutionary stability ≠ learning accessibility in MARL** 2609.27664. This edition therefore mines the **unclaimed game-adjacent remainder** — a window whose unclaimed shape is **sports-embodied RL (humanoid soccer ×2), NPC/social-simulation, world-action models at the robotics frontier, game-test-generation tooling, and reward-design RL engineering**.
>
> **Window character**: game-light at the *title* level (the StarCraft and world-model marquees all went to the siblings); the unclaimed remainder generalizes the game-AI levers — sim-to-real contact skills, agent skill internalization, fairness/robustness testing of MARL, scenario-driven game testing, hindsight reward editing, and the continuing **world-action-model** unification thread.

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 Banana Kick: Response-Informed Skill Evolution for Humanoid Soccer
- **Authors**: Hao E. Zhang, Ruize Geng, Raihan Haque, Khalil Zbiss, Guanyang Luo, Hui-ping Wang, H. Eric Tseng, Ding Zhao
- **Affiliation**: not stated (inferred — Ding Zhao is at CMU, humanoid/safety-RL cluster; H. Eric Tseng historically Ford Research) (tentative)
- **Venue**: arXiv preprint (2609.27269, cs.RO), announced in the Thu 24 Sep window
- **Key Innovations**: A **banana kick** demands contact mechanics that generate ball spin and aerodynamic curvature — a qualitatively different contact-rich skill from an ordinary-kick imitation prior, and one that **RL cannot adapt even with a dense reward when the task objective is locally flat over the current policy's responses** (a condition the paper names **first-order learning starvation**). Proposes **RISE (Response-Informed Skill Evolution)**, a closed-loop objective-continuation method: it ranks bounded objective changes by **response sensitivity estimated from cached rollouts** and accepts an update only when it produces *verified response progress* while preserving kicking reliability. Analysis shows rescaling a saturated spin reward cannot recover first-order sensitivity at zero spin, whereas adapting coupled contact responses opens a learnable path to spin.
- **Results**: RISE evolves the ordinary kick into a high-spin curved kick at **11.55 rad/s mean ball spin**, +19.8% mean evaluation score over a learning-progress curriculum, and raises joint target attainment from 15.2% to 50.9%; **30 motion-capture-recorded physical trials** confirm consistent hardware transfer under calibrated contact and Magnus-force aerodynamics.
- **Significance**: A formal diagnosis of *why* dense rewards stop composing skills (sports-game AI, physics-driven game controllers) — and a response-driven curriculum recipe that works on real hardware, directly transferable to game-character skill evolution and skill-gating in sports simulations.
- **Link**: https://arxiv.org/abs/2609.27269

### 1.2 DAVIS: A Depth-Only End-to-End Active-Vision Framework for Humanoid Soccer Skills
- **Authors**: Jiakang Jin, Yixiao Huo, Pengyuan Wang, Yinan Han, Tingxuan Zhang, Zhuobing Zhao, Xuanxin Zhou, Zhangchen Ye, Enxuan Ruan, Yifei Bao, Jiankun Yang, Chenghao Sun
- **Affiliation**: not stated (inferred — humanoid-soccer / RoboCup-adjacent academic cluster; Noetix E1 hardware partner) (tentative)
- **Venue**: arXiv preprint (2609.28175, cs.RO), announced in the Thu 24 Sep window
- **Key Innovations**: Asks a deliberately compact question — can a humanoid learn **contact soccer skills with only a head-mounted depth image + proprioceptive history + an optional low-dimensional task command**, outputting 25-DoF joint PD targets directly with **no extra runtime perception or planning modules**? **DAVIS** learns **visibility-aware auxiliary geometry during training** and combines **GT-to-prediction annealing, task curricula, and AMP-style motion priors** to bridge privileged supervision and real deployment, closing the loop over perception → approach → alignment → impact → recovery while its own motion hides the ball.
- **Results**: Instantiates goal-directed shooting and directional dribbling via task-specific objects/commands/rewards/curricula; validated in simulation, on the **Noetix E1 real humanoid**, and via ablations.
- **Significance**: The "one compact sensor, end-to-end" contention for on-robot game-styled skills — the sensing floor that real soccer-playing robots (and game-AI perception-light controllers) actually have.
- **Link**: https://arxiv.org/abs/2609.28175

### 1.3 Spiking Neural Network Predicting Sequence of the External Worlds States in Model-Based Reinforcement Learning
- **Authors**: Mikhail Kiselev
- **Affiliation**: not stated (single author; bio-inspired computing / SNN group) (tentative)
- **Venue**: arXiv preprint (2609.27459, cs.NE), announced in the Thu 24 Sep window
- **Key Innovations**: A **fully spiking world-state predictor**: rather than learning one world-dynamics model, the paper wraps an SNN predicting the *next* world state with **entirely spiking mechanisms** (spiking-neuron ensembles) to chain predictions into an arbitrary-length **sequence of future external world states**. This targets the sub-symbolic component of model-based RL in games — autoregressive rollouts of the environment without a continuous network forward per step.
- **Results**: The spiking sequential predictor is tested on a classic RL benchmark — **ATARI Pong**.
- **Significance**: A neuromorphic take on the "roll out the future" primitive that game world models and Atari-style planning agents depend on; complements the sibling-claimed generative world-action models with a spike-domain, energy-deployable variant.
- **Link**: https://arxiv.org/abs/2609.27459

### 1.4 FairTest: Search-Based Fairness Testing for Multi-Agent Reinforcement Learning Systems
- **Authors**: Xiaotong Wang, Xuan Xie
- **Affiliation**: not stated (inferred — SE/testing+RL group; fairness-of-Deep-RL audit line) (tentative)
- **Venue**: arXiv preprint (2609.27309, cs.SE), announced in the Thu 24 Sep window
- **Key Innovations**: MARL trains a team to maximize **team return**, but high team return does not imply agents share rewards fairly per episode. **FairTest** is a **search-based testing approach** that actively seeks *unfair executions* of a trained MARL policy: three fitness functions — **measured fairness of runs performed, predicted fairness from abstract states + fairness features, and policy decision uncertainty** — guide crossover/mutation, while prioritization ranks candidates by predicted fairness and uncertainty so test runs land where failures are expected.
- **Results**: On three environments × two MARL algorithms, FairTest detects the most fairness failures at fixed budget vs four baselines (statistically significant, large effect): **+221% failures on average over the strongest baseline, +23% average coverage**.
- **Significance**: The audit counterpart to cooperative reward design — studios shipping MARL bots/NPC squads get a testing discipline that checks "did the team win *fairly*?", not just whether it won.
- **Link**: https://arxiv.org/abs/2609.27309

### 1.5 Anchor and Perturb: Lazy Agent Remediation by Exploration Injection
- **Authors**: Chengxi Zhong, Yongzhe Chang
- **Affiliation**: not stated (inferred — change is also on RACER 2609.27667; multi-agent robustness cluster) (tentative)
- **Venue**: arXiv preprint (2609.27365, cs.MA), announced in the Thu 24 Sep window
- **Key Innovations**: Existing remediation for multi-agent coordination failures either rewires mixing networks or enforces simultaneous exploration across the whole collective — both inflict TD penalties in non-monotonic reward spaces. **Anchor and Perturb (AnP)** instead **isolates underperforming "lazy" agents** and injects an **asymmetric exploratory pulse into targeted coordinates**, while **anchoring converged teammates to nominal greedy exploitation** — decoupling exploration variance from recurrent-manifold stability, with no structural network changes.
- **Results**: Rescues collapsed joint policies (**5% → 85% evaluation win rate**) and escapes suboptimal coordination plateaus to sustain **~90% win rates** (empirical telemetry benchmarks).
- **Significance**: A surgical, no-arch-churn repair tool for cooperative game teams where "free-riding" agents collapse strategies — cheaper than population/architecture overhauls.
- **Link**: https://arxiv.org/abs/2609.27365

---

## 2. Game AI Bots, LLM Agents & Human-Behavior / NPC Simulation

### 2.1 Building Socio-Affective Artificial Intelligence for Interactive Multi-Agent Simulations (AGIMUD)
- **Authors**: David Berga
- **Affiliation**: independent researcher / academic (author-stated context) (tentative)
- **Venue**: arXiv preprint (2609.26927, cs.AI), announced in the Thu 24 Sep window
- **Key Innovations**: Design principles + a software architecture (**AGIMUD**, open-sourced) for **interactive MUD-style worlds where humans and multiple socially- and affectively-aware agents co-exist in real time**. Integrates (a) socially-aware reasoning and emotion in agent behavior/interaction, (b) a multimodal interaction scheme for human users ↔ artificial agents ↔ simulated worlds, and (c) **distributing the AI processing across the network** so many autonomous agents can run concurrently — a direct bridge between the transformer/conversational-agent era and multi-agent *theory of mind*.
- **Results**: A working architecture for dynamic world recreation as **multi-user dungeons** where agents and humans interact simultaneously in real time (https://github.com/dberga/AGIMUD).
- **Significance**: The socio-affective glue for live NPC populations — a concrete plumbing proposal for emotionally/socially aware LLM NPCs in shared online worlds, complementing the sibling-claimed LLM-world-model thread this window.
- **Link**: https://arxiv.org/abs/2609.26927

### 2.2 SkillGym: Internalizing Human Skills into LLMs for Real-World Problem Solving
- **Authors**: Zhilong Ge, Yuting Shao, Yutao Yang, Yuxuan Cai, Jie Zhou, Kai Chen, Bo Zhang, Qin Chen, Liang He
- **Affiliation**: not stated (inferred — LLM-agent / skill-acquisition cluster; Jie Zhou historical at Tencent/Baidu lines) (tentative)
- **Venue**: arXiv preprint (2609.27717, cs.CL), announced in the Thu 24 Sep window
- **Key Innovations**: Human-written agent skills are usually **external inference-time instructions**, not *internalized* capabilities. **SkillGym** converts skills into **executable, verifiable training environments**: a skill-to-task pipeline instantiates concrete tasks, verifies outcomes with code-based checkers, and measures empirical skill dependence via **contrastive executions**. Releases **2,756 environments across 12 categories** and **8,364 successful trajectories** (~49 tool calls, 60k+ logged tokens each) for SFT on verified workflows and RL with outcome rewards.
- **Results**: Under Claude Code, SFT lifts **Qwen3.5-35B-A3B by +199 Elo** on GDPval-AA v2, +19.10 pp on Terminal-Bench 2.1, and +28.13/+12.38 points on SkillsBench v1.1 (with/without skills); the 35B **SkillGym-Agent** reaches 51.47% skill-assisted SkillsBench, exceeding reported Claude Sonnet 4.6 / GPT-5.4 Mini / DeepSeek V4 Pro — and beats skill-assisted bases while *skills are withheld*.
- **Significance**: The "train the skill in, don't prompt it in" recipe for game-agent and NPC competence — reusable procedural skills as first-class training data rather than runtime crutches.
- **Link**: https://arxiv.org/abs/2609.27717

### 2.3 Teach-to-Crash: A Closed-Loop Student-Teacher LLM Framework for Collision-Inducing Test Scenario Generation
- **Authors**: Zaid Ghazal, Khouloud Gaaloul, Bruce Maxim
- **Affiliation**: not stated (inferred — SE/testing group; CARLA-based AV validation) (tentative)
- **Venue**: arXiv preprint (2609.27296, cs.SE), announced in the Thu 24 Sep window
- **Key Innovations**: Adversarial scenario search for validating simulators (driving, but structurally identical to game QA): a high-reasoning **Teacher LLM acts as an adaptive search controller**, while a low-reasoning **Student LLM emits simulator-executable scenarios** in a strict JSON schema; the Teacher intervenes only when rolling collision-rate / time-to-collision metrics **stagnate**, redirecting the search — with a constrained ego-centric scenario representation and stagnation-aware control.
- **Results**: In CARLA (two ego-speed setups): highest **Collision Hit Rate 90.79%**, shortest mean TTC 18.31s, competitive Collision Discovery Rate 136.21 (with substantially lower variance than the 179.44 peak baseline PAFOT), highest **diversity 0.547** and best avoidability-based usefulness proxy (60.04%).
- **Significance**: "Closed-loop failure farming" — a student-teacher LLM harness for generating frequent, diverse, analyzable failure scenarios; the same pattern serves game-bot red-teaming and playtesting bots.
- **Link**: https://arxiv.org/abs/2609.27296

### 2.4 Agent-Based Modeling: Equilibrium, Echo Chambers, and Efficiency in Hybrid Coevolutionary Opinion Games (H-COG)
- **Authors**: Ming-Zhi Jiang, An-Tzi Teng, Jun-En Liu, Po-An Chen, Yung-Ming Li
- **Affiliation**: not stated (inferred — Po-An Chen is at National Yang Ming Chiao Tung University, algorithmic game theory) (tentative)
- **Venue**: arXiv preprint (2609.27639, cs.GT), announced in the Thu 24 Sep window
- **Key Innovations**: Hybrid agent societies where **analytical agents (Friedkin–Johnsen cost-minimizing, Type-C) and LLM-language agents (Phi-4, Type-L) coevolve** beliefs and social ties over a dynamically rewired K-NN network — the **Hybrid Coevolutionary Opinion Game (H-COG)**. Opinions seeded from 5,199 real Reddit comments scored by a fine-tuned RoBERTa regressor; nine population compositions × three topologies × two topics = **540 runs, all converging**.
- **Results**: Language-driven populations reach an attractor as reliably as the analytical rule, enabling equilibrium-based comparison: pooled **Price of Anarchy 5.558 ± 0.309 (pure Type-L) vs 1.139 ± 0.005 (pure Type-C)** — and decomposition shows the gap comes from language agents **moving away from their intrinsic opinions**, not from disagreeing with neighbors. Consistent across topologies.
- **Significance**: A cost-of-efficiency measurement for **LLM NPC societies**: fluent, opinion-updating NPCs replicate convergence but pay a large social-efficiency price — a formal anchor for how much "LLM-ness" a designed agent population can afford.
- **Link**: https://arxiv.org/abs/2609.27639

---

## 3. Game Foundation Models, World Models & Game Agents

### 3.1 CoRe-WAM: Correspondence-Aligned Temporal Residuals for World Action Models
- **Authors**: Bin Zhou, Jialong Liu, Jianan Wang, Changhao Chen, Kani Chen
- **Affiliation**: not stated (inferred — world-action-model / VLA group; Motus-baseline lineage) (tentative)
- **Venue**: arXiv preprint (2609.27314, cs.RO), announced in the Thu 24 Sep window
- **Key Innovations**: Comparing "now vs before" naively at the same image location **mixes different scene content when objects or the camera move**. **CoRe-WAM**'s **TraceDelta** module uses **correspondences from a frozen tracking model to transport historical visual features to current locations** before computing signed differences in a shared pretrained feature space — so correspondence decides *what gets compared*, not the policy's trajectory representation. A lightweight adapter converts differences into validity-gated residuals that supplement current visual conditioning; the backbone stays **frozen**.
- **Results**: Built on Motus, optimizing only **1.59M parameters**: **92.22% clean success on 50 RoboTwin 2.0 tasks** (+3.56pp over Motus), **89.60% randomized** (+2.58pp) under a 5,000-update budget; integrating TraceDelta into StarVLA raises clean success **58.10% → 67.62%**, showing the temporal interface transfers beyond Motus.
- **Significance**: "Change, but change *the right object*" — the correspondence-aware temporal interface is exactly what action-driven world models (game-physics predictors, motion-aware agents) need when scenes move.
- **Link**: https://arxiv.org/abs/2609.27314

### 3.2 PointCast: One World Model for Rigid, Articulated, and Deformable Object Manipulation
- **Authors**: Hantao Ye, Ross Worobel, Zhuoli Xie, Mingen Li, Houjian Yu, Youngjin Hong, Changhyun Choi
- **Affiliation**: not stated (inferred — Changhyun Choi is at University of Minnesota, robotics/ML) (tentative)
- **Venue**: arXiv preprint (2609.28393, cs.RO), announced in the Thu 24 Sep window
- **Key Innovations**: A **point-set world model**: the state is a set of 3D points on the object + end-effector — mesh-free, topology-agnostic — where **each point keeps its identity and is supervised on its own trajectory** (teaches *where every point goes*, not just the shape). A 19.8M-param **diffusion transformer** denoises a short window of future point positions conditioned on history + commanded end-effector motion, with alternating local/global attention and cross-attention to the end-effector carrying the coupling.
- **Results**: One architecture + one recipe covers **four regimes — rigid, cloth, rope, multi-joint cabinets** — scoring best on 3 of 4 vs four baselines (second on rigid); on a real teleoperation dataset it is lowest-error in 4 of 6 categories and beats the dataset's own model in all six; frozen inside sampling-based MPC (one network eval per window) it dominates every baseline on four simulated tasks over 64 episodes.
- **Significance**: A unified, identity-aware, **physics-agnostic world model** for the object kinds games actually simulate (rigid props, cloth, ropes, articulated furniture) — one architecture instead of per-physics engines.
- **Link**: https://arxiv.org/abs/2609.28393

### 3.3 Generalizable Robotic Insertion with World Models
- **Authors**: Nicklas Hansen, Iretiayo Akinola, Yijie Guo, Jie Xu, Bingjie Tang, Hao Su, Xiaolong Wang, Abhishek Gupta, Dieter Fox, Yashraj Narang
- **Affiliation**: not stated (inferred — NVIDIA-adjacent (Fox, Narang, Akinola, Guo, Xu) + UC San Diego (Wang, Su) + UW (Gupta)) (tentative)
- **Venue**: arXiv preprint (2609.28258, cs.RO), announced in the Thu 24 Sep window
- **Key Innovations**: Assembly in high-mixture settings needs adaptability, but current policies are specialized per task. This framework trains a **single model-based world model** combining robot proprioception with wrist-camera raw visuals across **up to 90 insertion tasks with geometrically diverse parts** — and performance *improves with more training objects* (strong scaling).
- **Results**: **56% zero-shot success on unseen objects with unknown geometry** vs just **7%** for a model-free baseline; fine-tuning the generalist on held-out objects is markedly more data-efficient than from-scratch training and sometimes reaches better asymptotic performance. Claimed as the first fully data-driven system to assemble unseen objects.
- **Significance**: The "one model, every prop" evidence that generalist world-model-based policies beat task-specialized controllers — the same bet game-foundation-model companies are making for in-game interaction.
- **Link**: https://arxiv.org/abs/2609.28258

---

## 4. Procedural Content Generation, 3D-World Generation & Automated Game Design

### 4.1 Scenario-Driven Neuroevolution: Using Models to Guide Test Generation for Games (Neatest × Model-Based Testing)
- **Authors**: Gijs van Cuyck, Patric Feldmeier, Jan Tretmans, Gordon Fraser
- **Affiliation**: not stated (inferred — Gordon Fraser is at University of Passau, software testing/neuroevolution; Tretmans is at Radboud University / TNO, model-based testing) (tentative)
- **Venue**: arXiv preprint (2609.28130, cs.SE), announced in the Thu 24 Sep window
- **Key Innovations**: **Neatest** is a white-box neuroevolutionary test generator that evolves neural-network agents to reach uncovered statements/branches of a game's code — but that target scales poorly to large programs and rarely equals *playing the game as intended*. This paper combines Neatest with a **model-based testing** approach: the tester defines **test scenarios via abstract game models**, and Neatest now evolves networks that replicate the *concrete desired gameplay behavior* instead of chasing every branch.
- **Results**: On **13 Scratch games across genres**, model-guided Neatest reproduces the gameplay defined in the game models while **increasing branch coverage by 7%** over purely code-guided Neatest — mastering the game *as a player would* while still covering more code.
- **Significance**: The clearest bridge this window between **automated game-design QA and gameplay interpretation** — "test toward playable scenarios, not line coverage" — and a template for LLM/neuroevolution-augmented automated playtesting and level validation.
- **Link**: https://arxiv.org/abs/2609.28130

---

## 5. Game Benchmarks & Evaluation Suites

### 5.1 X2Real: an eXtensive Simulation Benchmark for Real-World Generalist Policies
- **Authors**: Lian Ruan, Jade Yang, Sherphylan Gao, Felix Gao, Kyson Liang, Galen Liu, Ligo Wu, Lane Jin, Guu Gu, Bevan Xie, Cloud Yan, Zongzi Yuan (+ 26 total)
- **Affiliation**: not stated (inferred — simulation/benchmarking group; NVIDIA Isaac Lab-Arena stack) (tentative)
- **Venue**: arXiv preprint (2609.27449, cs.RO), announced in the Thu 24 Sep window
- **Key Innovations**: Simulation benchmarks for generalist manipulation policies suffer **sim-to-real gaps, narrow task coverage, and unfair train/test pipelines**. **X2Real** is an **evolvable** Isaac Lab-Arena-based benchmark built on three principles — **faithfulness (0.84 linear correlation between simulated and real-robot results after calibrating visual+physical properties), diversity (10 capability dimensions, 44 hierarchical long-horizon tasks incl. visual grounding, language understanding, bimanual control), fairness (multi-axis domain randomization + strictly disjoint train/eval)** — powered by a custom physical domain-specific language and shipping a ~300-hour annotated trajectory dataset.
- **Results**: A benchmark that measurably tracks real-robot outcomes (0.84 corr), resists exploitation via disjoint pipelines, and supports iterative performance analysis over time.
- **Significance**: "Does my agent's sim score mean anything on the real game field?" — the fidelity/disjointness discipline game-bot and game-AI benchmarks need before leaderboard claims transfer to deployment.
- **Link**: https://arxiv.org/abs/2609.27449

### 5.2 PotARCin: Multi-Dimensional Evaluation of Skill Acquisition in Abstract Reasoning Tasks
- **Authors**: Claas Beger, Ryan Yi, Melanie Mitchell
- **Affiliation**: not stated (inferred — Melanie Mitchell is at Santa Fe Institute; ARC abstraction research line) (tentative)
- **Venue**: arXiv preprint (2609.27288, cs.AI), announced in the Thu 24 Sep window
- **Key Innovations**: Standard **ARC** evaluation scores one ability — produce the correct output grid. **PotARCin** extends ARC to measure acquisition of the underlying rule across **five dimensions: Definition, Classification, Constrained Generation, Editing, and Inversion**, using programmatic generation of new instances and input transformations beyond fixed input–output pairs, plus a held-out hand-crafted **P-ARC** test set.
- **Results**: Across five SOTA models on ARC-AGI-1 training: a **25–52 pp gap** between standard ARC scoring and PotARCin scoring; multi-dimensional evaluation **reorders models** that standard accuracy ties; models frequently **contradict their own formalized rule**; on P-ARC all models sit at **1–8%** across the five dimensions.
- **Significance**: An eval-validity upgrade for abstract skill acquisition — game agents trained only on "output the answer" benchmarks may not have learned the *rule*, which is what adaptive difficulty, level synthesis, and transfer need.
- **Link**: https://arxiv.org/abs/2609.27288

---

## 6. Industry Game AI, Real-Time Inference & Deployment Economics

**This window's unclaimed remainder contains 0 standalone industry-deployment/game-AI papers** (11th consecutive window without a dedicated direct paper in this slot's unclaimed pool). The industry-relevant story of the Thu-24 window lives in the sibling-claimed marquees, cross-referenced rather than re-featured:
- **JEV-Star** 2609.27331 — *deployment economics for competitive play*: StarCraft II Lv7 defeated with sub-second (0.422s median) classic JEV control + persistent GPT-6 planning at **~US$3.71/game**, 37.69% mean enemy-elimination lift over JEV-only — [arxiv-daily 09-24 §7.5](../2026-09-24/arxiv-daily.md).
- **InternW0** 2609.27656 — *inference-efficient world models for interactive use*: asymmetric video/action experts with **KV reuse instead of future regeneration** (observation-conditioned context routing) — [arxiv-daily 09-24 §7.1](../2026-09-24/arxiv-daily.md).

---

## 7. Related RL Techniques (Offline RL, Curiosity, Credit Assignment, Model-Based)

### 7.1 DCRL: Decoupling and Coupling Reinforcement Learning via Policy-Reward Manifold Alignment
- **Authors**: Henan Sun, Zehua Li, Haitao Hu, Qifan Zhang, Jianfeng Zhang, Nuo Chen, Jia Li
- **Affiliation**: not stated (inferred — LLM-post-training RL cluster) (tentative)
- **Venue**: arXiv preprint (2609.27572, cs.LG), announced in the Thu 24 Sep window
- **Key Innovations**: Re-reads LLM RL geometrically: reasoning as a **coupled manifold of three sub-manifolds — logical deduction, evaluation, representation**; generation is a decoupling from the evaluation manifold and reward estimation a decoupling from the deduction manifold, so rule-based/reward-model RL failures are **policy-reward manifold mismatch**. **DCRL**: (1) a **syllogistic logic-based prompt-evolution mechanism** that dynamically refines reward rubrics, and (2) a **policy-reward re-coupling mechanism** that jointly updates reward and policy models.
- **Results**: Consistently beats rule-based and reward-model baselines across reasoning domains; notably a **Qwen3-4B under DCRL surpasses Qwen3-32B and approaches Qwen3-235B**.
- **Significance**: Whack-a-mole reward-hacking countermeasure with a geometric rationale — relevant to any token-level RL loop, including self-play and reward-design for character reasoners.
- **Link**: https://arxiv.org/abs/2609.27572

### 7.2 RLDS: Reinforcement Learning with Decomposed Subtasks
- **Authors**: Mattie Terzolo, Mikolaj Sacha, Ayan Sinha, Andrew Rabinovich
- **Affiliation**: not stated (inferred — agentic-RL research group; Ayan Sinha historically at Vima Research) (tentative)
- **Venue**: arXiv preprint (2609.27035, cs.AI), announced in the Thu 24 Sep window (published 09-22)
- **Key Innovations**: GRPO-style policy-gradient agents collapse a multi-turn rollout into **one scalar trajectory reward** — lossy when tasks compose distinct skills under sparse/delayed feedback. **RLDS** replaces the scalar GRPO advantage with **Subtask-Decomposed Advantage Estimation (SDAE)**: split trajectory reward into per-subtask shares on a fixed taxonomy, compute a group-relative advantage per subtask, and distribute per-token credit weighted by subtask importance, concentrated at the step where a reflection marks the subtask as consequential. Also emits **heterogeneity diagnostics** predicting where decomposition pays.
- **Results**: Gains scale with subtask heterogeneity: **ScienceWorld +11.5 points** (95% CI [+9.8, +13.3]) and **FrozenLake +9.8** (+7.0, +12.8), within-noise on HotpotQA/DeepResearch as predicted; ScienceWorld is also **-10.9% wall-clock per step** as long rollouts amortize reflect-and-grade overhead.
- **Significance**: Reward decomposition as discrimination between competencies — the credit-assignment fix for long-horizon game agents whose wins/losses conflate many skills.
- **Link**: https://arxiv.org/abs/2609.27035

### 7.3 WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps
- **Authors**: Abbas Mammadov, Jerry Y. Huang, Justin Lin, Partha Kaushik, Sheel Shah, Kartik Nair, Yee Whye Teh, Nicholas M. Boffi
- **Affiliation**: not stated (inferred — Nicholas M. Boffi and Yee Whye Teh are at Oxford/DeepMind-adjacent flow-model lines) (tentative)
- **Venue**: arXiv preprint (2609.27033, cs.LG), announced in the Thu 24 Sep window (published 09-22)
- **Key Innovations**: Reward fine-tuning of pre-trained **flow-based generative models** is usually formulated as KL-regularized reward-maximization (reward-tilted sampling). **WTF (Wasserstein-Tilted Flow Maps)** uses an **optimal-transport regularizer built directly from the pre-trained drift** — an objective that *transports individual samples* toward higher reward instead of reweighting the base distribution — provably equivalent to a deterministic optimal-control problem on the flow, yielding the first **simulation-free RL recipe native to flow maps**, with no post-hoc distillation at few-step inference budgets.
- **Results**: On ImageNet-256 and text-to-image: higher reward with comparable or higher diversity than baselines, at up to **280× less training compute**.
- **Significance**: RL-as-flow-finetuning — cost-efficient reward shaping for generative game assets, world-model rollouts, and character-motion generators without sampling simulations.
- **Link**: https://arxiv.org/abs/2609.27033

### 7.4 HiRE: Hindsight Reward Editing for Policy Finetuning
- **Authors**: Haoyi Niu, Zhengtao Han, Yufeng Ji, Zhongyu Li, Koushil Sreenath
- **Affiliation**: not stated (inferred — Zhongyu Li & Koushil Sreenath are at UC Berkeley, hybrid systems/legged robotics) (tentative)
- **Venue**: arXiv preprint (2609.27068, cs.RO), announced in the Thu 24 Sep window (published 09-22)
- **Key Innovations**: RL finetuning's bottleneck is reward quality (sparse, biased, or non-control-centric semantics). **HiRE (Hindsight Reward Editing)** — training-free — **contrasts successful vs failed trajectories in hindsight** to calibrate foundation-representation reward models: it identifies **"trap states"** (predicted high-reward yet eventually failing) and explicitly **penalizes them while boosting critical successful states** — usable with any foundation representation and RL algorithm.
- **Results**: Consistently outperforms other reward recipes with dense, control-aware feedback that prevents value collapse and reward hacking — **≥3× performance of base policies**, better sample efficiency and stability.
- **Significance**: Hindsight as a reward-engineering primitive — an immediately transferable reward-shaping tool for game-policy finetuning where curated rewards are costly and "looks good but loses" states (traps) abound.
- **Link**: https://arxiv.org/abs/2609.27068

### 7.5 RACER: Robust Adversarial Reinforcement Learning with Risk Sensitivity and Critic Consistency Regularization
- **Authors**: Jiaxi Wu, Tiantian Zhang, Yuxing Wang, Yongzhe Chang, Xueqian Wang
- **Affiliation**: not stated (inferred — Xueqian Wang is at Tsinghua Shenzhen / SAT-lab cluster) (tentative)
- **Venue**: arXiv preprint (2609.27667, cs.LG), announced in the Thu 24 Sep window
- **Key Innovations**: Robust Adversarial RL (RARL) improves robustness via worst-case perturbations but suffers unstable optimization (over-aggressive adversaries drive agents to uninformative failure states) and **adversarially amplified double-critic disagreement**. **RACER** re-frames it risk-sensitively: a **state-dependent adversarial objective** adapting perturbation strength (suppress harmful disturbances, keep informative exploration) plus **critic consistency regularization** to stabilize Q-estimators.
- **Results**: On challenging continuous-control benchmarks, consistently improves performance, robustness, and training stability over strong robust-RL baselines.
- **Significance**: Adversary-tuning as a calibrated dial rather than max-perturbation — relevant to game-bot hardening and opponent-robust self-play where overly strong opponents can teach uninformative losses.
- **Link**: https://arxiv.org/abs/2609.27667

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.26918** On Preference Coverage Collapse from Hindsight Relabeling in Multi-Objective RL — hindsight relabeling in preference-conditioned MORL frequently harms (19 of 36 settings degraded up to 4 sd); the failure is *coverage collapse* over the preference simplex (quantified by a new **APM** statistic, ρ=-0.73); a single-parameter **her_mix** fix restores 16/19 settings and cuts abandoned preference mass 69%→6%. https://arxiv.org/abs/2609.26918
- **2609.27246** Listening and Mirroring: Verbal Attunement and Behavioral Mimicry for Embodied AI Agents in VR — real-time conversational AI + facial/posture mimicry: verbal attunement is the reliable driver of perceived empathy; mimicry effects are marginal and non-additive — calibration data for designing empathetic NPC/avatar behavior. https://arxiv.org/abs/2609.27246
- **2609.28085** Curriculum Learning with GNN-based RL for Job Shop Scheduling — curriculum beats single-size training on GNN-RL scheduling: at 30×30, ~8.1–8.6 pp lower optimality gap across all eval sizes and ~50 h saved training time — curriculum-scheduling evidence for combinatorial game-planning RL. https://arxiv.org/abs/2609.28085
- **2609.27741** Limiting-Kernel Q(λ): Bridging Short and Long Horizons — off-policy value estimator combining n-step truncation with a limiting-kernel long-horizon approximation, same complexity as n-step estimators, a.s. convergence to optimal values in finite MDPs, better on MuJoCo long-horizon tasks — value-estimation plumbing for evaluation horizons in game RL. https://arxiv.org/abs/2609.27741

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 5 |
| Game AI Bots, LLM Agents & Human-Behavior / NPC Simulation | 4 |
| Game Foundation Models, World Models & Game Agents | 3 |
| PCG, 3D-World Generation & Automated Game Design | 1 |
| Game Benchmarks & Evaluation Suites | 2 |
| Industry Game AI, Real-Time Inference & Deployment Economics | 0 (vacancy — industry story cross-referenced to siblings) |
| Related RL Techniques | 5 |
| **Total featured papers** | **20** |

## Cross-references (covered by sibling digests 09-24, not re-featured)

- 2609.27331 — JEV-Star: fast JEV + GPT-6 planning beats StarCraft II Lv7 at ~US$3.71/game — [arxiv-daily 09-24 §7.5](../2026-09-24/arxiv-daily.md)
- 2609.27656 — InternW0: foundational physical world model (asymmetric video/action experts, KV reuse) — [arxiv-daily 09-24 §7.1](../2026-09-24/arxiv-daily.md)
- 2609.27455 — LeWAM: latent evolving world action model (JEPA latents, DemoDPO, 92.28% RoboTwin 2.0) — [arxiv-daily 09-24 §7.2](../2026-09-24/arxiv-daily.md)
- 2609.28414 — Frozen Flows Forget: lost motion in latent-flow world models, decode-augmented restore — [arxiv-daily 09-24 §7.3](../2026-09-24/arxiv-daily.md)
- 2609.28416 — Agent-Editing World Model: edit task state instead of simulating tools — [arxiv-daily 09-24 §6.1](../2026-09-24/arxiv-daily.md)
- 2609.27321 — Verifiable Hidden Dynamics Play: LLM-generated agentic RL environments from solved mechanisms — [arxiv-daily 09-24 §2.5](../2026-09-24/arxiv-daily.md)
- 2609.28470 — CAVEAT: incentive-misaligned computer-use agent benchmark (marketplace steering) — [arxiv-daily 09-24 §6.5](../2026-09-24/arxiv-daily.md)
- 2609.27402 / 2609.28333 / 2609.27304 / 2609.27285 / 2609.27664 — credible auctions via MPC, online fair division, trade reduction, pacing equilibria, evolutionary-stability≠MARL-learning — [arxiv-ai-search 09-24 §6](../2026-09-24/arxiv-ai-search.md)

## Key Themes

1. **Sports-embodied RL gets its science.** Banana Kick (2609.27269) formalizes **first-order learning starvation** — dense rewards that are locally flat over a policy's responses block skill composition, and response-driven objective continuation (RISE) is the fix — while DAVIS (2609.28175) shows end-to-end soccer contact skills from a single depth sensor. Together: game-sports AI is maturing from "does it play" to "can it *skill-up* on hardware".

2. **NPC / agent-society economics returns with measurements.** AGIMUD (2609.26927) supplies the socio-affective plumbing for human+agent MUD worlds; H-COG (2609.27639) measures the price of fluent LLM agents in opinion games (PoA 5.56 vs 1.14 for analytical agents); SkillGym (2609.27717) internalizes human skills as trainable capability. The through-line: NPC populations are now being *engineered and priced*, not just prompted.

3. **World-action models keep converging on "change, but change the right content."** CoRe-WAM (2609.27314) transports historical features along correspondences before computing residuals (frozen backbone, 1.59M params); PointCast (2609.28393) supervises per-point identity trajectories across rigid/cloth/rope/articulated regimes; the generalist insertion world model (2609.28258) adds mono-model scaling evidence (56% zero-shot vs 7% model-free). This extends the sibling-claimed LeWAM/InternW0/AEWM line — the whole window is one vote for unification.

4. **Testing becomes a first-class game-AI activity.** Scenario-driven neuroevolution (2609.28130) targets playable scenarios instead of branch coverage; Teach-to-Crash (2609.27296) farms diverse collisions with a student-teacher LLM loop; FairTest (2609.27309) searches MARL policies for *unfair* team executions. QA is emerging as a research front: what to test, how to guide the search, and what "fair" means in cooperative play.

5. **Reward engineering is the shared denominator.** DCRL (2609.27572) aligns policy-reward manifolds against hacking, RLDS (2609.27035) decomposes trajectory reward by subtask, HiRE (2609.27068) edits rewards in hindsight (penalize trap states), RACER (2609.27667) calibrates adversaries risk-sensitively, and WTF (2609.27033) makes RL simulation-free for generative flows. Every submission this window is, at bottom, a better reward/credit **interface**.

6. **Dedup discipline note:** every featured ID (2609.27269–2609.27667) was grep-verified 0 hits in `wiki/` and sits inside the Thu-24 window (≥ 2609.26809); today's game marquees (JEV-Star, InternW0, LeWAM, Frozen Flows Forget, AEWM, Verifiable Hidden Dynamics Play, CAVEAT, and the ai-search GT batch) are cross-referenced, not duplicated.