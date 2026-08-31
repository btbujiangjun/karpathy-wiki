---
title: "arXiv Daily — 2026-08-31: On-Policy Distillation Matures (RA-OPD / VISTA / SpikeOPD), Symbolic Backpropagation for Post-Training (PLVR), Recommercial Incentive RL, HubMixer Feature Interaction, Survival Models for Repurchase, WM-R1 World-Model GUI Agents"
type: synthesis
created: 2026-08-31
updated: 2026-08-31
tags: [arxiv, daily, llm, rl, on-policy-distillation, post-training, recommendation, multimodal-rec, advertising, ctr, e-commerce, survival-model, games, world-models, agents, self-play, chess, retrieval, agentic-search, scaling-law, daily-digest]
---

# arXiv Daily — 2026-08-31

Fresh **Monday 31 Aug 2026** submission wave (top listed ID ~**2608.28589**). Prior digests (08-27 → 08-30) covered the Fri Aug 28 mailing up to ID **2608.27455**; this report covers the **unclaimed 2608.27460–2608.28589** range. 324 unique new IDs parsed, **13 featured** across 4 categories + 4 honorable mentions. Every featured arXiv ID is **grep-verified absent** from `wiki/`.

> Method: unlike the 08-30 sibling reports (which had direct arXiv blocked), the `arxiv.org/list/.../new` pages and `arxiv.org/abs/...` pages were directly retrievable via curl in this environment. Listing scraped from cs.AI / cs.LG / cs.CL / cs.IR / cs.GT / cs.MA `new` pages (Monday 31 Aug 2026), metadata fetched per-paper from live abs pages. Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities; otherwise "not stated".

---

## ① Feature Interaction & Multimodal Recommendation (2)

### 1.1 HubMixer: Progressive Latent Hub Mixing for Parameter-Efficient Feature Interaction in Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Jie Zhou, Zixian Gong, Wenhao Li, Chang Liu, Enzhao Shen, Bo Liu, Xu Guo, Fei Pan, Peng Jiang |
| **Institution** | Not stated (Kuaishou short-video recruitment business named in abstract) |
| **Submitted** | 2026-08-28 · [2608.27991](https://arxiv.org/abs/2608.27991) · cs.IR |
| **Abstract** | Recommendation tokens are fundamentally heterogeneous — user profiles, item attributes, behavioral sequences, context, statistical and business-side features live in different semantic spaces and interact in sparse, sample-specific patterns. Token-mixing architectures simplify self-attention, but directly mixing all tokens in the raw heterogeneous token space is parameter-inefficient: the model must implicitly discover which feature groups should interact and how. HubMixer introduces a small set of learnable **latent hubs** to organize interactions via an `induction–interaction–readout` paradigm: hub induction summarizes heterogeneous tokens into compact latent hubs via cross-attention; hub interaction performs high-order interaction in the cleaner hub space; token-conditioned readout lets each token selectively read from the interacted hubs while preserving field identity. |
| **Key innovations** | Latent-hub intermediate space instead of raw-token mixing; keeps field identity via token-conditioned readout; high-order interaction happens on compact hubs (parameter-efficient). |
| **Why it matters** | Directly relevant to the wiki's feature-interaction/CTR corpus: a clean argument that *where* interaction happens (raw vs. latent-hub space) is the design axis. Online A/B in Kuaishou recruitment shows +5.48% resume-submission conversion — real validation on a non-feed surface. |

### 1.2 AMUR: Information-Guided Selective Modality-Interest Alignment for Multimodal Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Wenze Ma, Chenyu Sun, Yanmin Zhu, Qiwen Gu, Xuhao Zhao |
| **Institution** | Shanghai Jiao Tong University *(inferred: Yanmin Zhu's group)* |
| **Submitted** | 2026-08-28 · [2608.27950](https://arxiv.org/abs/2608.27950) · cs.IR (CIKM 2026) |
| **Abstract** | Multimodal recommendation (MMRec) leverages rich item content from multiple modalities, but not all modality signals align with user preference — weak signals can even introduce noise. Recent methods use invariant learning, attention, graph refinement, or contrastive learning, yet their alignment is implicit/heuristic and lacks a clear objective for *selecting* which modality signals match user interests. AMUR refines modality graph structures toward user behavior, then selectively aligns shared interest-related semantics across modalities, preserving useful modality-specific complementarity while downweighting less-aligned signals. |
| **Key innovations** | Information-theoretic selection objective for which modality signals to align; graph refinement toward user behavior before cross-modal alignment. |
| **Why it matters** | Adds a "selectivity" axis to the MMRec debate — not more modalities, but better selection. Complements the wiki-tracked multimodal-rec line (cf. HubMixer's latent-hub view: both operate on the principle that *raw* multi-view fusion is suboptimal). |

---

## ② Advertising / CTR & E-commerce Time Modeling (3)

### 2.1 Learning to Allocate Incentives for Incentivized Advertising via Offline Model-Based RL

| Field | Detail |
|-------|--------|
| **Authors** | Zilin Zhao, Han Yang, Tianpei Yang, Fangsheng Huang, Yanfei Cui, Kan Peng, Yi Li, Yiming Zong, Hao Zhang, Yinsong Xue |
| **Institution** | Not stated (industrial ad platform, large-scale data + online A/B) |
| **Submitted** | 2026-08-28 · [2608.28065](https://arxiv.org/abs/2608.28065) · cs.AI |
| **Abstract** | In incentivized advertising the platform promises users a bonus ("complete your ad view and grab a 5-cent bonus!") *before* downstream ad revenue is realized. Insufficient incentives forfeit monetization; excessive ones reduce net profit; current incentives shape future engagement — so allocation is a sequential decision problem with delayed revenue, cost sensitivity, and carryover effects. The authors formulate it as an MDP and build an **offline model-based RL** framework (world model of user feedback + ad revenue, then conservative policy optimization). An independent counterfactual scorer evaluates each learned policy on held-out logs, enabling pre-launch selection without costly online exposure. |
| **Key innovations** | First decision-making algorithm for this setting (distinct from auto-bidding and targeted promotion); world-model + conservative optimization; offline counterfactual scorer for safe policy selection; causal-inference → offline-RL → Offline-MBRL deployment path. Online: MB-IQL +7.96% per-user net profit over TD3+BC. |
| **Why it matters** | Extends the wiki's auto-bidding/advertising-RL thread into the *incentive-design* setting (dual-sided: cost sensitivity + carryover), and demonstrates the rebuttal of "more data, choose bigger model" — the offline model-based component is what unlocks the gain. |

### 2.2 Fine-Tuning Autobidders with Group Relative Policy Optimization

| Field | Detail |
|-------|--------|
| **Authors** | Anton Safin, Alexandra Khirianova, Andrey Pudovikov, Aleksandr Katrutsa, Egor Samosvat |
| **Institution** | Not stated (industrial advertising research) |
| **Submitted** | 2026-08-28 · [2608.28199](https://arxiv.org/abs/2608.28199) · cs.GT |
| **Abstract** | Auto-bidding lets advertisers delegate sequential bid decisions to algorithms maximizing campaign value under constraints (budget, target CPC). The standard RL framing is actor-critic, but alternating actor/critic training is unstable and noise-sensitive — and the *ground-truth optimal bid is unknown*, a property shared with LLM post-training. The authors adapt **GRPO (critic-free policy gradient, from LLM post-training)** to autobidding: use it to fine-tune a strong heuristic baseline. Compared against actor-critic, heuristics, and controller-based methods on BAT, iPinYou, and AuctionNet, Autobidding-GRPO consistently wins on clicks and is best/second-best on conversions. |
| **Key innovations** | Transfers critic-free GRPO from LLMs to bid generation; fine-tunes a heuristic baseline rather than training from scratch; benchmarked across three industrial ad datasets. |
| **Why it matters** | Notably complements the wiki's CTR/ads corpus: an *advertising-native GRPO* (contrast with LAMA token-level auctions [08-28], SPADE, and the autobidding/simulator thread). Reinforces that the critic-free group-relative family is becoming the default RL update beyond LLMs. |

### 2.3 Timing-Aware Repurchase Prediction for Web-Scale E-Commerce: Survival Models for Multi-Surface Grocery Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Akshay Kekuda, Shreeranjani Srirangamsridharan, Ishan Bhatt, Yanan Cao, Sinduja Subramaniam, Evren Korpeoglu, Kaushiki Nag, Kannan Achan |
| **Institution** | Amazon *(stated)* |
| **Submitted** | 2026-08-28 · [2608.28393](https://arxiv.org/abs/2608.28393) · cs.AI (RecSys 2026) |
| **Abstract** | Repurchase recommenders are usually framed as binary "will this customer buy within W days", requiring a separately trained model per horizon. This work replaces that stack with **survival models predicting time-to-repurchase** directly, evaluated on millions of grocery-e-commerce customers across 30+ ablation configs. Key findings: (1) an empirically *slightly decreasing* marginal hazard (k≈0.9), against the common intuition that grocery items grow more likely to be repurchased over time; Log-Normal fits best marginally (R²=0.998); (2) a single Accelerated Failure Time (AFT) model replaces three per-horizon classifiers, matching/exceeding each at its own horizon with ~3x fewer trees; feature importance reshuffles (channel-cadence and recency rise, aggregate frequency falls); (3) a 4-parameter parametric calibration maps survival CDFs to per-horizon probabilities with zero cross-horizon monotonicity violations, exposing a principled calibration-vs-ranking trade-off (Exponential AFT best ECE ~1e-4; Log-Normal best ranking). |
| **Key innovations** | Ships *time-to-event* (not binary) rec prediction; single AFT model replaces a per-horizon model stack; hazard-rate finding (k≈0.9, decreasing) corrects grocery-repurchase intuition; calibration/ranking trade-off within one family. |
| **Why it matters** | A rare industrial survival-modeling (not classification) view of repurchase — conceptually adjacent to the wiki's watch-time/dwell-time distribution work (HEGM, 08-25) via the same "predict a distribution, not a point" logic, and to DTE temporal decoupling (08-19). |

---

## ③ LLM Training, RL & On-Policy Distillation (4)

### 3.1 RA-OPD: Reward-Aligned On-Policy Distillation — Filtering Misaligned Teacher Guidance

| Field | Detail |
|-------|--------|
| **Authors** | Siyuan Gan, Yuhan Li, Xiran Wang, Linjian Meng, Boyan Wang, Zhen Zhao, Jing Huo, Yang Gao |
| **Institution** | Shanghai Jiao Tong University / Shanghai AI Laboratory *(inferred: Yang Gao's group)* |
| **Submitted** | 2026-08-28 · [2608.27960](https://arxiv.org/abs/2608.27960) · cs.AI |
| **Abstract** | During on-policy distillation (OPD), teacher guidance on student-generated prefixes is not always reliable: the teacher may discourage a move toward a *correct* trajectory, or push the student toward an *incorrect* one — guidance misaligned with outcome reward. RA-OPD keeps only trajectories whose induced updates move the student toward correct trajectories (or away from incorrect ones). For each sampled trajectory it checks whether the trajectory-level distillation return is consistent with outcome reward, then filters out misaligned trajectories — no additional compute cost. On seven math and three code benchmarks (Qwen3 + DeepSeek-R1 families), RA-OPD significantly outperforms standard OPD and other OPD variants. |
| **Key innovations** | Trajectory-level distillation-return vs. outcome-reward consistency check; treats teacher-guidance misalignment as a first-class filtering principle; compute-free relative to OPD. |
| **Why it matters** | Third wiki-tracked OPD reliability patch (after SOPD/R2-OPD [08-25]) converging on *"teacher likelihood is a biased, trajectory-blind signal"*. RA-OPD's filter-on-consistency is complementary to SOPD (granularity), R2-OPD (progress), and Capacity-Dependent selection (student scale) — the OPD-reliability theme is now the strongest recurring storyline of late-August training papers. |

### 3.2 VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Zewen Ding, Zezhong Wu, Zhou Tao, Shida Wang, Shizhuo Hou, YongXiang Hua, Haoyu Cao, Linli Xu |
| **Institution** | University of Science and Technology of China (USTC) *(inferred: Linli Xu)* |
| **Submitted** | 2026-08-28 · [2608.28306](https://arxiv.org/abs/2608.28306) · cs.LG |
| **Abstract** | On-policy self-distillation (OPSD) trains a problem-only student on its own rollouts using dense token-level supervision from a privileged teacher that also sees a reference solution. Standard OPSD treats the teacher distribution as a fixed target and updates only the student — but the teacher target can misdirect the student when misaligned with valid problem-only reasoning. **VISTA** preserves the standard student update while using *outcome-verified rollouts* to adapt the teacher toward the student distribution, restricting adaptation to the top-k positions of largest teacher–student KL divergence. No extra sampling or separate reward objective. Across AIME24/25, HMMT25 with Qwen3 at 1.7B/4B/8B, VISTA reaches the highest Avg@12 at every scale (+0.6/+0.7/+2.1 over OPSD). |
| **Key innovations** | Reverses the supervision direction of OPSD: student-to-teacher adaptation grounded in verified outcomes; targeted (top-K KL) teacher adaptation; reuses OPSD rollout/loss. |
| **Why it matters** | Same OPD-reliability cluster as RA-OPD (3.1): while RA-OPD *filters trajectories*, VISTA *adapts the teacher*. Two independent groups fixing OPD-family misalignment from opposite ends — expect a unified recipe. |

### 3.3 SpikeOPD: Stable On-Policy Distillation for Autoregressive Spiking Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Enqiao Lu, Xingrui Yu, Yiwei Fu, Zhenglin Wan, Pengfei Zhou, Wangbo Zhao, Muqing Jian, Xueyi Zhang, Yang You, Ivor Tsang |
| **Institution** | National University of Singapore (Tsang/You) + collaborators *(inferred)* |
| **Submitted** | 2026-08-28 · [2608.27857](https://arxiv.org/abs/2608.27857) · cs.AI |
| **Abstract** | Spiking neural networks (SNNs) promise energy-efficient language modeling but are hard to train from scratch; a practical route is ANN→SNN migration via knowledge distillation (KD) from a pretrained ANN teacher. Existing migration distills on fixed corpus prefixes while autoregressive inference conditions on self-generated prefixes — a **prefix-source mismatch**. OPD handles this by continuing teacher supervision on self-generated prefixes, but a controlled stress test shows vanilla OPD can suffer delayed rollout-feedback collapse: on-policy coverage alone does not ensure stable adaptation. **SpikeOPD** adds matched-prefix policy anchoring (constrains policy departure from the frozen reference SNN on matched prefixes) and layerwise spike regularization. Gains +0.8/+1.7/+2.9 points over KD SNNs at 0.125B/0.35B/1.3B while preserving sparse-compute profiles. |
| **Key innovations** | Applies OPD to the SNN-energy-efficiency setting for the first time; identifies prefix-source mismatch plus rollout instability as the dual failure mode; matched-prefix policy anchoring as stabilizer. |
| **Why it matters** | Expands the OPD-reliability cluster to a third axis (stability/regularization) and to a non-autoregressive-LLM substrate (SNNs). Also connects to the wiki's efficiency/mobile-AI interest (sparse event-driven compute). |

### 3.4 Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and Loss

| Field | Detail |
|-------|--------|
| **Authors** | Niccolò Ajroldi, Diana Alexandra Onutu, Haider Al-Tahan, Jörg Franke, Sampo Pyysalo, Jenia Jitsev, Aaron Klein |
| **Institution** | (inferred: OpenEuroLLM project — Jitsev at Jülich / RWTH; Pyysalo at Turku NLP) |
| **Submitted** | 2026-08-28 · [2608.28308](https://arxiv.org/abs/2608.28308) · cs.LG |
| **Abstract** | Studies the scaling of learning rate and batch size in pretraining dense LLMs on English-prevalent corpora. Beyond *jointly optimal* LR/batch, it investigates their *marginal* evolution with model capacity and data scale, models these relationships, and — under a Warmup-Stable-Decay schedule — quantifies gains from LR annealing and whether optimal LR/batch *transfer* between stable and decay phases. It also evaluates recently proposed scaling forms that model the loss dependence on capacity × dataset-size interaction, which capture both undertraining and overtraining regimes. |
| **Key innovations** | Marginal (not just joint-optimal) LR/batch scaling laws; LR-annealing-gain quantification + phase-transfer analysis; open-sourced complete pretraining runs as a first OpenEuroLLM baseline. |
| **Why it matters** | Joins the wiki's scaling-law corpus (Kunlun/Wukong/OpenEuroLLM axis, 08-25 Densing Law). The **LR/batch marginal evolution** and **annealing-phase transfer** findings are directly actionable for training-run budgeting — the "hyperparameter scaling" twin to the loss-vs-capacity scaling commonly tracked. |

---

## ④ Program Learning & Verifiable Rewards (1)

### 4.1 PLVR: Program Learning with Verifiable Rewards — Symbolic Backpropagation for Post-Training LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Vishvesh Bhat |
| **Institution** | Not stated |
| **Submitted** | 2026-08-28 · [2608.28421](https://arxiv.org/abs/2608.28421) · cs.AI |
| **Abstract** | SFT and RL both place acquired reasoning inside model weights, where it cannot be inspected, checked step by step, or moved between models. PLVR argues that for tasks with verifiable intermediate steps, reasoning is better placed *outside* the base model's weights as an explicit program composed from deterministic and neural primitives. Its mechanism is **symbolic backpropagation**: each program layer carries a typed ontology, a loss is computed at the output against ground truth, and required input ontologies are propagated backward by type-inference over primitive signatures — credit assignment as a *derivation* rather than an estimate. On LiveCodeBench v6 and Tau2Bench, 30B base models with PLVR beat RL at matched budget by 27.8 points on average and frontier models ~10x larger by 13.6 points; one primitive library serves both benchmarks, so new tasks cost ~100 examples of program search. Ablation shows the backward pass (not the type system) is the source of the advantage. |
| **Key innovations** | Moves reasoning outside weights into an explicit, inspectable program; symbolic backpropagation (type-inference credit assignment) replacing estimated gradients; dense per-step contract rewards vs. RLVR's terminal check. |
| **Why it matters** | A conceptual counterpoint to the entire weight-based post-training cluster (§3): instead of better distillation/RL, it relocates the capability to a symbolic program layer. Relevant to the wiki's "where should reasoning live" thread and to verifier/reward-engineering debates (cf. BPCO critic, RLVR). |

---

## ⑤ Games, World Models & Agents (3)

### 5.1 WM-R1: Training GUI Agents to Reason and Leverage World Models with Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Yu Han, Tianwen Qian |
| **Institution** | Not stated |
| **Submitted** | 2026-08-27 · [2608.27508](https://arxiv.org/abs/2608.27508) · cs.AI |
| **Abstract** | GUI agents trained with RL show strong environment-learning on mobile platforms, but RL demands extensive real-environment interaction — expensive and unstable in GUI scenarios. **WM-R1** is (claimed) the first RL framework training mobile GUI agents with *world models instead of real environments*: world models supply state transitions for all rollouts, replacing the real Android environment in the training loop. WM-R1 also embeds world models into the thinking process (agents reason about candidate-action consequences before committing). It eliminates real-environment interaction, supports massively parallelized, step-level trajectory generation, and uses a multi-dimensional rule-based reward for task success, trajectory efficiency, and world-model utilization. On Android benchmarks it outperforms GRPO-only baselines and inference-time simulation methods. |
| **Key innovations** | World-model-as-environment for agent RL (no real env needed); world-model-in-the-loop reasoning; parallelized step-level trajectories; rule-based multi-objective reward. |
| **Why it matters** | Ties the wiki's world-model thread to *agentic RL training efficiency*: instead of using world models for simulation at inference, it uses them as the training substrate. Complements the world-model corpus (ForgeWM/Marionette/PlayWorld, AcrossVAM below) and the agent-RL thread (WMD?) — the "world model replaces the simulator" theme from 08-25's simulator survey made concrete in imperfect-information GUI control. |

### 5.2 Beyond Search-Imitation: Prior-Directed Exploration for Searchless Chess

| Field | Detail |
|-------|--------|
| **Authors** | Szymon Miłosz, Piotr Duch, Szymon Grabowski |
| **Institution** | Lodz University of Technology *(inferred: Grabowski)* |
| **Submitted** | 2026-08-27 · [2608.27757](https://arxiv.org/abs/2608.27757) · cs.LG |
| **Abstract** | Searchless chess networks reach human-master strength in one forward pass by imitating a stronger search (Lc0's Chessformer distills MCTS visit counts). But imitating a search is a poor proxy for playing without one, so the authors fine-tune for single-pass strength with self-play RL, replacing the usual entropy-bonus exploration (reverse KL to uniform) with a **forward, mass-covering KL toward the network's own MCTS prior** (prior-directed exploration), paired with an entropy-adaptive sampling temperature set by value-head uncertainty. In ~2000 steps it lifts puzzle accuracy 93.9→94.9% and mate-in-four 77→81%, holding searchless strength at/below the base. Key finding: tactical accuracy and playing strength *dissociate* — a puzzle-only control gains the most tactics while shedding ~260 Elo, i.e. a better puzzle-solver is not a stronger player. |
| **Key innovations** | Forward mass-covering KL (prior-directed) replaces reverse-KL entropy exploration for searchless self-play; explicit demonstration that search-imitation ≠ single-pass play; tactical-accuracy/rating dissociation result. |
| **Why it matters** | A clean games/RL result for the wiki's self-play corpus: the exploration-prior choice matters more than imitation fidelity, and it surfaces the "accuracy ≠ strength" evaluation pitfall. Directly extends the WikiSkill / Chessformer / searchless-play thread (cf. 08-30 ConfAL-WM for a contrasting confidence view). |

### 5.3 ITER: Interaction-Aware Retrieval for Agentic Search

| Field | Detail |
|-------|--------|
| **Authors** | Haodong Chen, Shuai Wang, Yu Yin, Shengyao Zhuang, Guido Zuccon, Teerapong Leelanupab |
| **Institution** | University of Queensland (Zuccon's IR group) + collaborators *(inferred)* |
| **Submitted** | 2026-08-28 · [2608.27912](https://arxiv.org/abs/2608.27912) · cs.IR |
| **Abstract** | Deep-research agents answer complex questions through iterative sub-queries, but retriever training typically uses only the current sub-query + current search results, underusing information accumulated from prior interactions. **ITER** is an agent-interaction-aware dense retriever trained with *trajectory-relative* learning signals: each query is represented by the current sub-query *plus* the main question and preceding sub-queries. Across six agent backbones / three model families, ITER beats the prior trajectory-trained retriever LRAT by +7.5% on InfoSeek-Eval and +13.5% on BrowseComp-Plus, with stronger cross-agent robustness than the LLM-judge-based AgentIR. Ablations show the main question + previous sub-queries give the most robust query representation, and previously-visited-but-useful documents (as redundancy negatives) provide the strongest supervision. |
| **Key innovations** | Query representation accumulates agent interaction context (not just current sub-query); trajectory-relative (not step-local) training signals; cross-agent robustness. |
| **Why it matters** | For the wiki's retrieval/agentic-search thread: a training-side answer to "fragmented multi-hop retrieval" — the retriever itself becomes interaction-aware rather than relying on external judge signals. Complements the agent-RAG line (evidence-aware retrieval [08-30]) and RoundTrip-style trajectory learning. |

---

## Honorable mentions (scanned, not featured)

| arXiv ID | Title | Category | One-line takeaway |
|----------|-------|----------|-------------------|
| [2608.27840](https://arxiv.org/abs/2608.27840) | An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark | cs.AI | On the new Trip World benchmark, hometown-aware models lean on destination-region priors rather than user-specific transfer; simplest model is among the strongest; naive agentic next-POI adaptation trails a popularity prior — a scalability/probeing reality-check for cross-city rec. |
| [2608.27826](https://arxiv.org/abs/2608.27826) | Personalized and Multi-View Representation for Federated Cold-Start Recommendation (PMFRec) | cs.IR | Federated cold-item rec under dual-sided privacy (server can't see interactions, clients can't see item attributes); multi-view encoder + single fused representation, reduces communication, improves fairness + LDP robustness. |
| [2608.28491](https://arxiv.org/abs/2608.28491) | AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction | cs.AI | Factorizes robot-video future into object-centric particle motion + dense appearance; 0.28M-param transformer rolls particles forward, cuts trajectory error 21%; candid about weak language grounding (2.8–3.1%) and appearance delivery gaps. |
| [2608.28027](https://arxiv.org/abs/2608.28027) | String: An Agentic OS Where Every App Is a Markdown File | cs.AI | Reframes agent interfaces as an OS problem: SFMD Markdown apps replace re-read context; staged view disclosure (a turn-too-early leaks up to 23 accuracy points, 28%→2% wrong-action), privilege-from-provenance, ~33% fewer tokens. Complements SKILL.state / context-curation thread. |
| [2608.28359](https://arxiv.org/abs/2608.28359) | Every Article Deserves a Video: Contextual Video Matching for Digital Publishers | cs.IR | Dailymotion production system auto-embedding relevant videos in text articles via LLM + embeddings; adopted by hundreds of publishers, boosts engagement. |
| [2608.27757](https://arxiv.org/abs/2608.27757) | (see §5.2) | — | — |

---

## Cross-Cutting Themes (2026-08-31)

1. **OPD-reliability keeps consolidating — now 5 methods in one month.** RA-OPD (filter trajectories by reward-return consistency — [3.1]), VISTA (adapt the teacher instead — [3.2]), SpikeOPD (stabilize with policy anchoring — [3.3]), plus 08-25's SOPD (step granularity) / R2-OPD (progress filtering). The shared belief: *token-level teacher-likelihood is a biased signal that must be filtered, adapted, or stabilized.* Watch for a unified "trustworthy-distillation" recipe absorbing all five.
2. **Post-training is starting to leave the weights.** PLVR's symbolic-backpropagation (program outside weights, credit via type-derivation) is a sharp conceptual alternative to the entire distillation/RL cluster (§3–4). Paired with RA-OPD/VISTA's distrust of teacher signals, the week reads as "where should learned reasoning actually live, and who do we trust to assign credit?"
3. **Advertising RL is absorbing LLM mechanisms.** GRPO (critic-free) is now applied to autobidding ([2.2]); offline model-based RL (world models) is used for additive value (incentive allocation, [2.1]). The show "LLM post-training tooling generalizes to ad systems" is now a mainstream narrative, mirroring how OPD/generative-rec crossed over earlier.
4. **Distribution-over-point prediction is the rec-system frontier.** Survival models for repurchase ([2.3]) join HEGM watch-time mixtures (08-25) in replacing binary/point targets with calibrated distributions — with an explicit calibration-vs-ranking trade-off that offline metrics often hide.
5. **World models as *training substrate*, not just inference simulator.** WM-R1 replaces the real GUI environment with a world model during RL ([5.1]); AcrossVAM uses explicit particle dynamics as a low-dimensional world interface. The simulator-replacement thesis (08-25 survey) is being instantiated in both agent-RL and robot-video settings.

---

## Methodology

- **Listing source**: `arxiv.org/list/{cs.AI,cs.LG,cs.CL,cs.IR,cs.GT,cs.MA}/new` (Monday 31 Aug 2026 mailing), directly fetched via curl this session. 324 unique new IDs in the `2608.27460–2608.28589` range after removing already-known/wiki-covered IDs.
- **Dedup boundary**: prior digests end at **2608.27455** (08-28 siblings + 08-29/08-30 passes). Every featured ID is grep-verified absent from `wiki/**`.
- **Metadata**: per-paper `arxiv.org/abs/...` pages fetched via curl; titles/authors/abstracts/comments extracted. Inferred affiliations flagged conservatively.
- **Temp files**: scraped listings and abs pages under pre-authorized temp path `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`; cleaned up after this report lands.
- **Coverage disclaimer**: paper IDs appearing only via DOI/conference pages (not as arXiv IDs in wiki text) could theoretically overlap; flagged candidates were manually cross-checked against the 08-27→08-30 siblings.
