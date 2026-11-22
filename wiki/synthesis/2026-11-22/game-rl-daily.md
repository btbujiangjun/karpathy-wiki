# Game RL & Game AI Bot — Daily Paper Digest (2026-11-22)

- **Date**: 2026-11-22
- **Window**: papers new to the wiki, submitted 2026-10-23 → 2026-11-22 (today); arXiv Export API rate-limited (HTTP 429/400), discovery via arXiv website search ordered by `-announced_date_first`; deduped vs whole-wiki baseline (grep of `wiki/synthesis`, 10,838 arXiv IDs); affiliations/abstracts from arXiv website search + PDF first pages (pypdf); metrics/claims author-reported.
- **Scope**: Game RL (Atari, StarCraft, Dota, Go, chess, poker, Minecraft, NetHack, etc.), multi-agent RL, self-play/PB/open-ended learning in games; LLM/VLM-powered game agents, NPC intelligence, game bot frameworks, autonomous gameplay; game foundation models & game-playing world models; PCG (level generation, automated game design); game benchmarks (incl. meta-evaluation of user simulators, decision-model leaders); industry game AI (RIVF 2027); related techniques (reward shaping, world models, model-based/offline RL, curiosity/hierarchical/imitation/IRL in games where present).

## Executive Summary

14 papers in this window, led by two themes: **AI in network games** — CoSlice (O-RAN RAN slicing as a coordinated multi-agent RL problem) — and **robustness/efficiency of training RL for games** — Audit Where Hacks Pay (budgeted audits against reward hacking in GRPO), Discrete Flow Matching (offline→online RL on MinAtar), PIVOT (progressive teacher correction on logic games), Regularized Score Centering (stabilizing async RL). Also new: **LLM agents cooperating** — Learning Robust Social Strategies with LLMs (TMRL) and Safe MARL with GNE convergence. **Game AI bot frameworks** — CoToan (executable rules + OpenSpiel contract, accepted at RIVF 2027); **game foundation models** — GameRealm (120M-frame game data asset, SAIL/SJTU/ZJU); **game benchmarks** — On Evaluating User Simulators (meta-eval, 351 real sessions) and Piccolo (Decision Index Vision leaders); **world models** — Algebraic World Model (Lean 4 formalization, ARC-AGI-3 games). PCG had no new papers this window.

---

## 1) Game RL — Atari, Strategic Learning, Multi-Step

### CoSlice: Coordinated Multi-Agent Reinforcement Learning for 5G Network Slicing Allocation (2611.23909)
- **Title (EN)**: CoSlice: Coordinated Multi-Agent Reinforcement Learning for 5G Network Slicing Allocation
- **Authors**: Pengxin Wang; Nakjung Choi; Jingdi Chen
- **Affiliation**: Department of Electrical and Computer Engineering, University of Arizona (Wang, Chen); Nokia & Bell Labs (Choi) — PDF first page
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-18
- **Abstract**: Radio Access Network (RAN) slicing is a shared resource allocation problem: each slice seeks to satisfy its Service Level Agreement (SLA) with minimal radio-resource consumption, while all slices compete for a limited resource budget. This creates both an intra-slice trade-off between SLA assurance and resource efficiency and an inter-slice conflict over shared resources, calling for specialized yet coordinated control. In this work, we present CoSlice, a coordinated multi-agent reinforcement learning framework for inter-slice physical resource block allocation in Open Radio Access Network (O-RAN). CoSlice uses preference-conditioned slice agents for fast resource allocation and an LLM-based coordinator to adapt their objectives using global network observations at a slower timescale. We formulate the problem as a multi-objective partially observable stochastic game (mo-POSG), establish the existence of a Preference Correlated Equilibrium, and derive a sublinear regret bound for the learning procedure. We implement the algorithm by using a two-stage training procedure that consists of multi-objective pretraining and joint optimization. We build a network slicing evaluation environment using ORANSlice and its radio-frequency simulator (RFsim), supporting realistic protocol-stack execution and application traffic across multiple slices. Experimental results show that CoSlice reduces both average and tail SLA violations compared with other centralized and multi-agent baselines under diverse slice workloads.
- **Key innovations**:
  - Mo-POSG formulation of O-RAN inter-slice resource allocation; Preference Correlated Equilibrium existence + sublinear regret bound.
  - Preference-conditioned slice agents + LLM coordinator (slow timescale) with two-stage (multi-objective pretraining + joint optimization) training; ORANSlice/RFsim evaluation env.
  - Reduces average AND tail SLA violations vs centralized and multi-agent baselines.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23909) | [PDF](https://arxiv.org/pdf/2611.23909)

### Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO (2610.35716)
- **Title (EN)**: Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO
- **Authors**: Shurun Li; Michael Hua Wang; Haibo Zeng; Long Wang
- **Affiliation**: REASONS Lab, Institute for Network Sciences and Cyberspace, Tsinghua University (Li, Wang, Wang); Virginia Tech (Zeng) — PDF first page
- **Venue/conference**: arXiv preprint (27 pages, 5 figures, 8 tables)
- **Date**: 2026-10-26
- **Abstract**: Reinforcement learning with verifiable rewards trains on cheap checks, such as unit tests, that a policy can learn to game, while a stronger check is too expensive to run on every rollout. We study how to spend a limited strong-verifier budget in GRPO, separating which weakly passing rollouts to audit from what reward a caught hack receives. At a fixed policy state with centered advantages, the expected update depends on a design only through each rollout's marginal audit probability and correction; reflecting a caught hack's reward about the failure reward negates the advantages of an all-hack group; and auditing whole groups with the fewest weak passes first (low-pass budgeted audits, LB) minimizes the advantage mass left on hacks among pass-count designs with a fixed correction when a label's value falls with the pass count. We tested this analysis in actual LLM training: from each run's starting state, the sign of this mass on a frozen panel predicted whether hacking would be suppressed in 33 of 39 runs, including 13 of 16 preregistered ones. In LeetCode (Wong et al., 2026) and Countdown-Code (Khalifa et al., 2026), LB drives hacking to near zero, while random audits with the same penalty and budget do not and use more labels. We also find that the randomness of the update affects training: in Countdown-Code, two unbiased corrections, per-item reward-level IPW and a group-level advantage correction, bring hacking down too but end 6.1–11.8 and 8.0–11.5 points lower in held-out accuracy than LB at the same budget. A full audit, which the group-level correction reproduces in expectation, stays within about two points of LB in three seeds, while LB uses 28% of its labels, and allocating the same correction by pass count recovers most of the loss (one seed). Training outcomes thus depend not only on the expected update but also on the randomness of its estimate.
- **Key innovations**:
  - "Low-pass budgeted audits" (LB): audit whole groups with fewest weak passes first; minimizes remaining advantage mass on hacks.
  - Analysis: caught-hack rewards should reflect about the failure reward (negating all-hack group advantages); audit-sign on a frozen panel predicted hacking suppression in 33/39 runs (13/16 preregistered).
  - Empirical: LB → hacking near zero in LeetCode/Countdown-Code at same penalty/budget; uniform/random audits ineffective; per-item IPW + group-level correction underperforms LB by 6.1–11.8 / 8.0–11.5 points held-out accuracy.
- **Links**: [arXiv](https://arxiv.org/abs/2610.35716) | [PDF](https://arxiv.org/pdf/2610.35716)

### Discrete Flow Matching for Offline-to-Online Reinforcement Learning (2605.12379)
- **Title (EN)**: Discrete Flow Matching for Offline-to-Online Reinforcement Learning
- **Authors**: Fairoz Nower Khan; Nabuat Zaman Nahim; Peizhong Ju
- **Affiliation**: Department of Computer Science, University of Kentucky, Lexington, KY — PDF first page
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-15
- **Abstract**: Many reinforcement learning (RL) tasks have discrete action spaces, but most generative policy methods based on diffusion and flow matching are designed for continuous control. Meanwhile, generative policies usually rely heavily on offline datasets and offline-to-online RL is itself challenging, as the policy must improve from new interaction without losing useful behavior learned from static data. To address those challenges, we introduce DRIFT, an online fine-tuning method that updates an offline pretrained continuous time Markov chain (CTMC) policy with an advantage-weighted discrete flow matching loss. To preserve useful pretrained knowledge, we add a path-space penalty that regularizes the full CTMC trajectory distribution, rather than only the final action distribution. For large discrete action spaces, we introduce a candidate-set approximation that updates the actor over a small subset of actions sampled from reference-policy rollouts and uniform exploration. Our theoretical analysis shows that focusing on a small set of high probability actions can reduce computation while keeping the approximation error small, making our method practical for large action spaces. We evaluate on macro-action MinAtar games where offline-pretrained DRIFT outperforms its online-only counterpart across all five games and achieves the highest mean return on three and on oracle free Jericho, DRIFT achieves a mean normalized score of 7.3% with a lightweight GRU encoder, outperforming the evaluated pretrained language-model baselines. Ablations demonstrate the importance of appropriately weighted path-space regularization and reference-guided candidate construction.
- **Key innovations**:
  - DRIFT: advantage-weighted discrete flow matching fine-tunes offline CTMC policies online; path-space KL penalty regularizes the full trajectory distribution.
  - Candidate-set approximation for large discrete action spaces (reference-policy rollouts + uniform exploration).
  - Evaluated on macro-action MinAtar games: beats online-only baseline on all 5, best mean on 3; on oracle-free Jericho, mean normalized score 7.3%.
- **Links**: [arXiv](https://arxiv.org/abs/2605.12379) | [PDF](https://arxiv.org/pdf/2605.12379)

### PIVOT: Progressive Intervention via Online Teacher Correction (2610.40576)
- **Title (EN)**: PIVOT: Progressive Intervention via Online Teacher Correction
- **Authors**: Zhihao Yang; Boyuan Zheng; Puhui Tan; Yukun Chen; Kuan Zhang; Longze Chen; Jiaming Li; Renke Shan; Lu Wang; Xianpei Han
- **Affiliation**: 1 University of Chinese Academy of Sciences (Yang, Chen; School of Advanced Interdisciplinary Sciences, UCAS), 2 Tsinghua University (Zheng, Tan), 3 Chinese Information Processing Laboratory, Institute of Software, Chinese Academy of Sciences (Han), 4 School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences (Chen; Zhihao Yang; Renke Shan; Jiaming Li) — PDF first page
- **Venue/conference**: arXiv preprint (19 pages, 9 figures, 6 tables; project page: https://zhihaoyang30.github.io/PIVOT/)
- **Date**: 2026-10-29
- **Abstract**: Reinforcement learning from verifiable rewards (RLVR) is limited by sparse outcome-level feedback on hard reasoning tasks: when all rollouts in a group fail, rewards provide no learning signal. Stronger teachers can provide additional guidance, but this raises a central question: how can such signals be incorporated into RLVR to support successful rollouts while remaining learnable for the student? We distinguish two complementary mechanisms: trajectory-level intervention, which improves access to reward-bearing trajectories, and token-level supervision, which provides dense targets to guide student learning. Our controlled experiments show that either mechanism alone can remain insufficient, motivating their combination. We therefore introduce PIVOT, which inserts teacher-generated corrections into student rollouts and applies token-level KL supervision to these segments alongside the RLVR objective. Beyond their combination, we systematically analyze where to intervene and how to supervise, yielding a recipe for effective guidance. Across hard logic games and mathematical reasoning benchmarks, PIVOT consistently outperforms existing methods, nearly doubling mean avg@8 on logic games from 19.5% for the best-performing baseline to 35.6%.
- **Key innovations**:
  - PIVOT: teacher-generated corrections inserted into student rollouts + token-level KL supervision alongside RLVR; analysis of where to intervene and how to supervise.
  - Doubles mean avg@8 on hard logic games: 19.5% (best baseline) → 35.6%.
- **Links**: [arXiv](https://arxiv.org/abs/2610.40576) | [PDF](https://arxiv.org/pdf/2610.40576)

### Regularized Score Centering (2611.21791)
- **Title (EN)**: Regularized Score Centering
- **Authors**: Hao Bai; Chenlu Ye; Xuanchang Zhang; Aviral Kumar; Tong Zhang
- **Affiliation**: 1 UIUC (Bai, Ye, Zhang; Bai = Hao Bai, haob2@illinois.edu), 2 CMU (Kumar) — PDF first page; project page: https://biechi.github.io/blog/rsc/
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-16
- **Abstract**: Asynchronous reinforcement learning increases training throughput, but data from stale policies and numerical mismatch between training and inference can destabilize learning. To stabilize off-policy learning, score centering (SC) removes the effect of reward baselines on the expected update. Our gradient diagnostics show less extreme gradients with SC than with importance sampling (IS), but SC can still fail when the learner moves far from the behavior policy that generated the data. To limit this policy mismatch, we introduce Regularized Score Centering (RSC), which adds a reverse Kullback–Leibler (KL) penalty to encourage the learner's next-token distribution to stay close to the behavior policy's next-token distribution. RSC works with or without truncated importance sampling (TIS), which caps token importance weights. Our theoretical analysis supports this approach, showing that KL regularization improves convergence guarantees. We evaluate dense and mixture-of-experts models on mathematical reasoning and agentic tasks, including online shopping, tool use, games, and fully asynchronous software engineering. RSC with TIS substantially improves sample efficiency across all agentic benchmarks, attaining higher training rewards with the same number of sampled responses. In final evaluations, it achieves top performance across all six agentic tasks, improving by 14.3% on AppWorld and reaching 9.9× the strongest baseline's score on BabyAI.
- **Key innovations**:
  - RSC: adds reverse-KL penalty keeping the learner's next-token distribution near the behavior policy's (with/without TIS); stabilizes async RL.
  - Sample-efficiency gains on agentic benchmarks incl. games; top-6 agentic tasks; +14.3% AppWorld, 9.9× BabyAI.
- **Links**: [arXiv](https://arxiv.org/abs/2611.21791) | [PDF](https://arxiv.org/pdf/2611.21791)

---

## 2) Multi-agent RL in games (MARL, self-play-style training)

### Learning Robust Social Strategies with Large Language Models (2511.19405)
- **Title (EN)**: Learning Robust Social Strategies with Large Language Models
- **Authors**: Dereck Piche; Mohammed Muqeeth; Milad Aghajohari; Juan Duque; Michael Noukhovitch; Aaron Courville
- **Affiliation**: Mila & University of Montreal, Montreal, Quebec, Canada — PDF first page (Aaron Courville at MILA/UdeM; affiliation of some co-authors on PDF not stated)
- **Venue/conference**: Published in Transactions on Machine Learning Research (10/2026); reviewed on OpenReview
- **Date**: 2026-10-30
- **Abstract**: As agentic AI becomes more widespread, agents with distinct and possibly conflicting goals will interact in complex ways. These multi-agent interactions pose a fundamental challenge, particularly in social dilemmas, where agents' individual incentives can undermine collective welfare. While reinforcement learning (RL) has been effective for aligning large language models (LLMs) in the single-agent regime, prior small-network results suggest that standard RL in multi-agent settings often converges to defecting, self-interested policies. We show the same effect in LLMs: despite cooperative priors, RL-trained LLM agents develop opportunistic behavior that can exploit even advanced closed-source models. To address this tendency of RL to converge to poor equilibria, we adapt a recent opponent-learning awareness algorithm, Advantage Alignment, to fine-tune LLMs toward multi-agent cooperation and non-exploitability. We then introduce a group-relative baseline that simplifies advantage computation in iterated games, enabling multi-agent training at LLM scale. We also contribute a novel social dilemma environment, Trust-and-Split, which requires natural language communication to achieve high collective welfare. Across a wide range of social dilemmas, policies learned with Advantage Alignment achieve higher collective payoffs while remaining robust against exploitation by greedy agents. We release all of our code to support future work on multi-agent RL training for LLMs.
- **Key innovations**:
  - Adapts opponent-learning-awareness (Advantage Alignment) to fine-tune LLMs for cooperation/robustness in multi-agent settings; group-relative baseline for LLM-scale training.
  - New social-dilemma environment Trust-and-Split requiring natural-language communication; policies achieve higher collective welfare while resisting exploitation by greedy agents.
  - Published in TMRL (10/2026), reviewed on OpenReview.
- **Links**: [arXiv](https://arxiv.org/abs/2511.19405) | [PDF](https://arxiv.org/pdf/2511.19405)

### Safe Multi-Agent Reinforcement Learning with Convergence to Generalized Nash Equilibrium (2411.15036)
- **Title (EN)**: Safe Multi-Agent Reinforcement Learning with Convergence to Generalized Nash Equilibrium
- **Authors**: Zeyang Li; Navid Azizan
- **Affiliation**: Not stated on PDF first page (authors: Zeyang Li, Navid Azizan) — verify from full text
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-16
- **Abstract**: Multi-agent reinforcement learning (MARL) has achieved notable success in cooperative tasks, demonstrating impressive performance and scalability. However, deploying MARL agents in real-world applications presents critical safety challenges. Current safe MARL algorithms are largely based on the constrained Markov decision process (CMDP) framework, which enforces constraints only on discounted cumulative costs and lacks an all-time safety assurance. Moreover, these methods often overlook the feasibility issue (the system will inevitably violate state constraints within certain regions of the constraint set), resulting in either suboptimal performance or increased constraint violations. To address these challenges, we propose a novel theoretical framework for safe MARL with state-wise constraints, where safety requirements are enforced at every state the agents visit. To resolve the feasibility issue, we leverage a control-theoretic notion of the feasible region, the controlled invariant set (CIS), characterized by the safety value function. We develop a multi-agent method for identifying CISs, ensuring convergence to a Nash equilibrium on the safety value function. By incorporating CIS identification into the learning process, we introduce a multi-agent dual policy iteration algorithm that guarantees convergence to a generalized Nash equilibrium in state-wise-constrained cooperative Markov games, achieving an optimal balance between feasibility and performance. Furthermore, for practical deployment in complex high-dimensional systems, we propose Multi-Agent Dual Actor-Critic (MADAC), a safe MARL algorithm that approximates the proposed iteration scheme within the deep RL paradigm. Empirical evaluations on safe MARL benchmarks demonstrate that MADAC consistently outperforms existing methods, delivering much higher rewards while reducing constraint violations.
- **Key innovations**:
  - State-wise-constrained safe MARL: feasibility via Controlled Invariant Sets (CIS) + safety value function; multi-agent dual policy iteration → convergence to Generalized Nash Equilibrium.
  - MADAC (Multi-Agent Dual Actor-Critic) approximation within deep RL; higher rewards with fewer constraint violations.
- **Links**: [arXiv](https://arxiv.org/abs/2411.15036) | [PDF](https://arxiv.org/pdf/2411.15036)

### Zero-Shot Coordination for Sparse Reward Tasks with Diverse Reward Shapings (2604.25076)
- **Title (EN)**: Zero-Shot Coordination for Sparse Reward Tasks with Diverse Reward Shapings
- **Authors**: Keenan Powell; Peihong Yu; Pratap Tokekar
- **Affiliation**: Department of Computer Science, University of Maryland, College Park — PDF first page
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-03
- **Abstract**: Many Multi-Agent Reinforcement Learning (MARL) agents fail to adapt properly to cooperating with agents trained with the same objectives but different seeds, algorithms, or other training differences. This is the problem of Zero-Shot Coordination (ZSC), which focuses on training agents to cooperate well with unknown agents. ZSC has been studied for a variety of tabular cases and simple games such as Hanabi, achieving excellent results. However, existing solutions to ZSC only consider identical rewards for your trained agents and all future partners. This is not realistic for the trained agents, as they do not consider the problem of cooperating with agents that have identical sparse objectives but shape the rewards for those objectives in different manner. To address this issue, we show how to train an ensemble of methods using randomized reward shapings chosen using 4 selection algorithms. Experiments done on the Overcooked environment demonstrate consistent improvements of 62.2%-119.2% in sparse reward over baseline ZSC algorithms when playing with agents that have identical sparse rewards but different reward shapings.
- **Key innovations**:
  - ZSC under reward-shaping heterogeneity: ensemble of methods with randomized reward shapings (4 selection algorithms) — a core Related technique (reward shaping).
  - 62.2%–119.2% sparse-reward improvements vs ZSC baselines in Overcooked when cooperating with identically-sparse but differently-shaped partners.
- **Links**: [arXiv](https://arxiv.org/abs/2604.25076) | [PDF](https://arxiv.org/pdf/2604.25076)

---

## 3) Game AI Bot — LLM/VLM agents, NPC intelligence, game bot frameworks, autonomous gameplay

### CoToan: Executable Rules and a Representation Contract for Reproducible Game AI Evaluation (2610.39353)
- **Title (EN)**: CoToan: Executable Rules and a Representation Contract for Reproducible Game AI Evaluation
- **Authors**: Ha-Thanh Nguyen
- **Affiliation**: College of Engineering and Computer Science, Vin University, Hanoi, Vietnam — PDF first page
- **Venue/conference**: Accepted at RIVF 2027
- **Date**: 2026-10-29
- **Abstract**: Game AI results are comparable only when different implementations expose the same decision problem. Yet seemingly minor representation choices can silently change that problem by altering action probabilities or collapsing states with different outcomes. We study this issue through CoToan, an executable specification and representation contract for Vietnamese Mathematical Chess connecting the Game Description Language (GDL) with OpenSpiel. The game provides a useful case because a single capture may have multiple arithmetic justifications, while outcomes can depend on scoring rules and a finite playing horizon. CoToan therefore represents actions by their state transitions rather than by arithmetic witnesses, and treats time and victory configuration as part of task identity. Cross-representation tests show agreement in legal actions, successor states, and terminal outcomes across hundreds of sampled and constructed positions, complemented by exhaustive checks of all 32 operator masks and 512 opposing-material subsets. Controlled diagnostics further show that uniform witness-level sampling alters endpoint-action probabilities, while omitting remaining time or victory settings can merge states with different terminal behavior. These results show that action semantics, time, and victory configuration are not merely implementation details. They are part of the experimental task itself and must be represented explicitly for reproducible game AI.
- **Key innovations**:
  - CoToan: executable specification + representation contract bridging GDL and OpenSpiel; actions as state transitions (not arithmetic witnesses); time/victory config as task identity.
  - Repro-driven diagnostics: cross-representation agreement on legal actions/successors/terminal outcomes; exhaustive checks of 32 operator masks + 512 material subsets.
- **Links**: [arXiv](https://arxiv.org/abs/2610.39353) | [PDF](https://arxiv.org/pdf/2610.39353)

---

## 4) Game Foundation Models / Game-Playing World Models

### GameRealm: Grounding Visual Learning in Interactive Games (2611.23140)
- **Title (EN)**: GameRealm: Grounding Visual Learning in Interactive Games
- **Authors**: Weiguang Zhao; Yifan Wang; Ni Yang; Yating Wang; Xingyu Miao; Yankai Jiang; Mulin Yu; Tao Lu; Haoyu Guo; Junting Dong; Weinan Zhang; Chunhua Shen
- **Affiliation**: Shanghai Artificial Intelligence Laboratory (Zhao, Miao, Jiang; PDF first page); Shanghai Jiao Tong University (Wang, Zhang); Zhejiang University (Shen)
- **Venue/conference**: arXiv preprint; project page: weiguangzhao.github.io/GameRealm
- **Date**: 2026-11-17
- **Abstract**: Visual foundation models are central to physical intelligence, yet their development remains constrained by fragmented training datasets, inconsistent annotation quality, and limited multimodal supervision. To address these challenges, we introduce GameRealm, a large-scale, richly annotated dataset that grounds visual observations in synchronized, game-native supervision. GameRealm encompasses over 120 million RGB frames and 1,000 hours of gameplay footage across all views. Beyond its unprecedented scale, GameRealm provides rich multimodal supervision, including metric depth, camera parameters, synchronized audio, control inputs, and 3D point trajectories. Its diversity further extends to flexible view configurations, spanning single-view, stereo, multi-view, and panoramic recordings. To enable scalable acquisition across diverse game environments, we develop a unified data collection pipeline that combines human-operated interaction with agentic exploration. Extensive experiments across diverse visual learning tasks demonstrate that GameRealm consistently strengthens visual foundation models in both visual generation and geometric learning. These results establish GameRealm as a versatile and valuable data resource, unlocking new opportunities for advancing visual intelligence.
- **Key innovations**:
  - GameRealm: >120M RGB frames, 1000h gameplay across views, with game-native supervision: metric depth, camera params, synchronized audio, control inputs, 3D point trajectories; view-config diversity.
  - Unified human-operated + agentic-exploration data pipeline for scale-out across games; strengthens visual foundation models in generation AND geometric learning.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23140) | [PDF](https://arxiv.org/pdf/2611.23140)

### Algebraic World Model: From Exploration to Proofs (2610.40503)
- **Title (EN)**: Algebraic World Model: From Exploration to Proofs
- **Authors**: Guancheng Pan; Qixin Tan; Yang Yuan; Andrew C. Yao
- **Affiliation**: Guancheng Pan — Zhejiang University; Qixin Tan — Tsinghua University; Yang Yuan & Andrew C. Yao — Shanghai QiZhi Institute — PDF first page
- **Venue/conference**: arXiv preprint (29 pages, 9 figures, 14 tables; project page: https://ephemeral6.github.io/awm-site/; ancillary Lean 4 model)
- **Date**: 2026-10-30
- **Abstract**: AI has made remarkable progress in mathematics, solving challenging problems with machine-checkable proofs in Lean, yet typically relying on predefined mathematical definitions and formal specifications. This raises a natural question: can it reason rigorously about an unknown world? We introduce the Algebraic World Model (AWM), a framework that turns interaction with unfamiliar environments into explicit mathematical models supporting formal reasoning. AWM explores the environment and develops executable Python hypotheses, continually testing and revising them against observations. It then structures its hypotheses into typed objects and shared rules, simplifies their structure through category-theory-guided transformations, and formalizes the resulting model in Lean 4 to prove reachability and impossibility. AWM can formally prove that a goal is unreachable, even beyond explored trajectories. On two impossible game levels, it constructs closed, kernel-checked Lean proofs excluding every legal winning sequence in all six runs, while Claude Opus 5.5 and GPT-6 Astra, equipped with coding tools, produce none in twelve baseline runs. Four of AWM's six initial bounds are correct, compared with one for Opus 5.5 and none for GPT-6 Astra; given only feedback that a cheaper win exists, AWM revises its rules and constructs new proofs, reaching six of six correct bounds. Moreover, AWM produces interpretable mathematical models whose rules can be inspected and tested step by step. Across all 25 public ARC-AGI-3 games, these models enable Lean to replay the winning trajectories of all 183 levels and generalize beyond observed play, predicting unseen transitions and detecting changes in game mechanics. With Claude Opus 5, AWM clears all levels with a score of 99.9, while its certified winning trajectories use only 43% of the human baseline's actions.
- **Key innovations**:
  - AWM: interaction with unknown environments → typed, category-theory-refined models formalized in Lean 4; proofs of reachability/impossibility; provably-unreachable goals beyond exploration.
  - Model surgery: 6/6 correct bounds after revising rules given a cheaper-win hint; certified trajectories use 43% of human baseline actions on Opus 5.
  - Generalizes across 25 ARC-AGI-3 games (183 levels replayable); interpretable rules.
- **Links**: [arXiv](https://arxiv.org/abs/2610.40503) | [PDF](https://arxiv.org/pdf/2610.40503)

---

## 5) Procedural Content Generation

No new PCG papers (level generation / automated game design / PCG-RL) in the 2026-10-23 → 2026-11-22 window. PCG appears within the digest via benchmarks (Piccolo's game examples) — see Coverage Notes and Gaps.

---

## 6) Game Benchmarks

### On Evaluating User Simulators for Interactive Agents (2611.24892)
- **Title (EN)**: On Evaluating User Simulators for Interactive Agents
- **Authors**: Hengguang Zhou; I-Hung Hsu; Li Chen; Priyanshi Shrivastava; Anastasios Angelopoulos; Wei-Lin Chiang; Ion Stoica; Cho-Jui Hsieh
- **Affiliation**: 1 UCLA (Zhou, Hsieh); 2 Arena (Ion Stoica & Cho-Jui Hsieh; affiliation label on PDF first page unverified — Ion Stoica co-founded the agent platform Arena)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-18
- **Abstract**: User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. This uncertainty makes it difficult to interpret simulator evaluation. To understand what a high benchmark score tells us about simulator quality, we (meta-)evaluate the metrics themselves. To instantiate this meta-evaluation, we deliberately perturb simulated replays to induce failures such as altered goals, omitted constraints, premature stopping, and acceptance of broken work, then test whether the metrics penalize these failures. Evaluation methods from three prior studies detect only 5-6 of the 10 perturbations; their combined scores even favor populations instructed to accept broken work over unmodified controls. Motivated by these gaps, we propose a new evaluation suite that combines utility of user simulators for evaluating agents and two measures of fidelity to real users: population-level fidelity assesses collective interaction patterns, while trace-level fidelity assesses the preservation of individual users' goals, constraints, and persona. Under the same detection criterion, our evaluation suite detects all 10 perturbations. Evaluating six user simulators on 351 real multi-turn sessions in which 348 distinct users across 23 languages and agents work together to create and refine artifacts such as full-stack web apps, games, design assets, and automated workflows, we find that population-level measures can miss when a simulated user pursues the wrong goal, ignores a constraint, or behaves out of character, highlighting the need to assess fidelity at comprehensive granularities.
- **Key innovations**:
  - Meta-evaluation of user-simulator metrics: utility + population-level fidelity + trace-level fidelity (goal/constraint/persona preservation).
  - Detects all 10 induced perturbations vs 5–6 for prior methods; finds gap: population-level measures miss wrong-goal/constraint/out-of-character behaviors on 351 real multi-turn sessions (348 users, 23 languages).
- **Links**: [arXiv](https://arxiv.org/abs/2611.24892) | [PDF](https://arxiv.org/pdf/2611.24892)

### Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement (2611.24651)
- **Title (EN)**: Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement
- **Authors**: Zhenqing Ling; Qirui Jiao; Daoyuan Chen; Cheng Chen; Xinji Mai; Haowen Gao; Zhuo Zhang; Xuchen Pan; Mengsu Ding; Jiaji Deng; Yuexiang Xie; Xiaoming Qin; Weirui Kuang; Zhaoyang Liu; Yaliang Li; Bolin Ding; Jingren Zhou
- **Affiliation**: Not stated on PDF first page (PDF shows "Piccolo Team†"); project: https://decisionplayground.agentscope.io/piccolo.html
- **Venue/conference**: arXiv preprint (22 pages, 13 figures, 11 tables)
- **Date**: 2026-11-18
- **Abstract**: We present Piccolo, a family of multimodal decision models (0.8B to 27B) that coevolves model capabilities and training data via Agentic Data Engineering and recursive self-improvement (RSI). The models predict probabilities over candidate answers for general-purpose text and visual judgments, agent harnesses, data workflows, and interactive games. Piccolo-27B tops the Decision Index Vision Full leaderboard with a score of 75.59, while Piccolo-9B and Piccolo-4B achieve 68.35 and 67.46, respectively. All three rank first on the Private benchmark in their respective model-size categories. Research agents analyze model behavior, construct training data, conduct experiments, and use the results to refine subsequent proposals. Semantic slices and a shared research memory connect these actions across the model family's development. With training recipes comprising hundreds of thousands of examples, data selection and feedback-driven refinement are central to the self-improvement process. Our large-scale RSI exploration yields three counter-intuitive insights for decision-model development: (1) Backbone-recipe co-adaptation outweighs raw model recency — earlier backbones can surpass newer generations on visual tasks under identical recipes; (2) Targeted data curation enables 4B–9B models to rival 27B baselines on specialized workflows; and (3) Continuous loss reduction can decouple from and even degrade discrete decision accuracy. Together with the released weights and tools from the Data-Juicer and AgentScope ecosystems, Piccolo provides an actionable blueprint for building frontier decision models and scaling data-driven RSI.
- **Key innovations**:
  - Piccolo: 0.8B–27B multimodal decision models; agentic decision interface (candidate-probability readout) for text, visuals, games, workflows; Agentic Data Engineering + RSI loop.
  - Decision Index Vision Full leaderboard: Piccolo-27B 75.59 (top), Piccolo-9B/4B 68.35/67.46; Private benchmark #1 in each size class.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24651) | [PDF](https://arxiv.org/pdf/2611.24651)

---

## 7) Industry Game AI

### CoToan: Executable Rules and a Representation Contract for Reproducible Game AI Evaluation (2610.39353)
- **Industry signal**: Vin University (Hanoi, Vietnam), accepted at RIVF 2027 — represents industry/game-adjacent AI deployment; reproducible-benchmark focus.
- **Coverage note**: industry-paper coverage is thin this window (1 paper, above).

---

## Cross-Cutting Observations

- **AI enters games as infrastructure**: CoSlice (O-RAN RAN slicing as coordinated MARL, mo-POSG, LLM coordinator), PIVOT (teacher-correction RLVR on logic games), Discrete Flow Matching (offline→online RL on MinAtar).
- **Robustness/efficiency of game training**: Audit Where Hacks Pay (budgets audits where they bite, analysis of audit probability), Regularized Score Centering (async RL stability), Zero-Shot Coordination with Diverse Reward Shapings (robustness to shaping heterogeneity).
- **LLM agents cooperating**: Learning Robust Social Strategies with LLMs (Advantage Alignment + Trust-and-Split; TMRL-published).
- **Benchmarks expanding in fidelity**: On Evaluating User Simulators (meta-eval, 351 real sessions); Piccolo (decision-model leaders); GameRealm (game-native visual+geometric supervision); CoToan (executable rules for reproducible game AI).
- **World models for games**: Algebraic World Model (formally proven game-level reachability/impossibility in Lean 4); GameRealm (data asset feeding them).

## Coverage Notes and Gaps

- **Dedup**: every included ID is new to the wiki (grep-verified absent from the whole-wiki baseline: 10,838 arXiv IDs across `wiki/synthesis/**`, incl. all prior `game-rl-daily` digests).
- **Affiliations**: PDF page-1 (pypdf) verified for 13/13 papers. Two papers print no affiliation on PDF first page — marked as such: Safe Multi-Agent Reinforcement Learning with Convergence to Generalized Nash Equilibrium (2411.15036), Piccolo (2611.24651). Verify from full text if needed.
- **Window/freshness**: all 13 papers submitted 2026-10-23 → 2026-11-22 (today); freshest 2026-11-18.
- **Limitations**: arXiv Export API rate-limited (429/400) → arXiv website search (`arxiv.org/search`, ordered by `-announced_date_first`); `websearch` unavailable; discovery via ~32 topic queries (~16 unique candidates after dedup; 13 selected). Abstracts from arXiv website search; abbreviations in PDF text (e.g., `\$` in 2411.15036) not expanded. All metrics/claims are author-reported; no full-text review beyond PDF page 1.
- **Trends**: multi-agent + LLM agents in games; AI in network-game infrastructure (O-RAN); benchmark explosion with higher fidelity; world models maturing from pixels to typed/provable structures.
