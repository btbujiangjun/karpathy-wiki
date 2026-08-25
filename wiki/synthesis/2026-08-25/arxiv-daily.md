---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-25)"
type: synthesis
created: 2026-08-25
updated: 2026-08-25
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-rec, world-models, on-policy-distillation, watch-time, self-play, daily-digest]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-25 · Scope: papers **not yet covered anywhere in the wiki** (every arXiv ID below grep-verified absent from all existing pages; zero overlap with sibling digests arxiv-paper-check / arxiv-ai-search / game-rl-daily / conference-digest / tech-report-digest). Fresh window = Fri Aug 21 – Mon Aug 24 submissions (IDs ~2608.21xxx–2608.23xxx), plus 2 catch-ups (2608.13721, 2608.16333) surfaced by topic sweeps that earlier digests missed. Retrieved via arXiv API across cs.IR / cs.CL / cs.LG / cs.AI / cs.GT with topic-keyword queries (recommendation/recommender/click-through/advertising/user-behavior; RL/distillation/policy-optimization × language model; game/self-play/MARL). **17 new papers below across 4 categories.**
>
> Affiliations marked *(inferred)* are deduced from author identities or dataset provenance and flagged accordingly; otherwise "not stated".

---

## ① LLM Training & Reasoning (6)

> Today's strongest cluster: an **on-policy distillation (OPD) trilogy** — SOPD fixes *where* teacher supervision is applied (step level), R2-OPD fixes *which* spans get supervision (reasoning-progress filtering), and the Capacity-Dependent study fixes *which student* benefits (model scale × training budget). Together they sketch a maturing post-training discipline around OPD.

### 1.1 Step-Level On-Policy Distillation: Interpolating Between OPD and SFT (SOPD)

| Field | Detail |
|-------|--------|
| **Authors** | Changhui Sun, Lanbo Liu, Hang Lei, Tong Ling, Jiahang Xie, Zhiyong Zheng, Yujia Wang et al. |
| **Institution** | Not stated |
| **Submitted** | 2026-08-17 · [2608.16333](https://arxiv.org/abs/2608.16333) · cs.CL |
| **Abstract** | Token-level on-policy distillation provides only fragmented corrections along an erroneous student trajectory and cannot unfold a complete repair path. SOPD adds step-level supervision over complete student-generated trajectories, combining SFT's long-horizon correction with OPD's on-policy advantage: teacher responses are conditioned on student trajectories, so they align with student-visited states while still repairing whole steps. At the limits of step length, SOPD reduces exactly to SFT or approximates OPD — a strict interpolation family between the two regimes. |
| **Key innovations** | Step-level interpolation theory unifying SFT and OPD as two endpoints of one objective; teacher rewrites conditioned on student rollouts rather than gold data. On ALFWorld agents, +13.4 points success rate over vanilla OPD. |
| **Why it matters** | Third wiki-tracked OPD refinement this month (after GC-OPD's verifier residual calibration and R2-OPD below). The field is converging on "token-level OPD alone is structurally insufficient" — granularity of the distillation signal is now the main design axis. |

### 1.2 Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress (R2-OPD)

| Field | Detail |
|-------|--------|
| **Authors** | Chen Yang, Haiyuan Wan, Rengrong Xiong, Yize Chen, Danny H. K. Tsang |
| **Institution** | HKUST *(inferred: Danny Tsang's group)* |
| **Submitted** | 2026-08-19 · [2608.19408](https://arxiv.org/abs/2608.19408) · cs.AI |
| **Abstract** | OPD implicitly assumes teacher-derived rewards proxy genuine reasoning progress. Empirically they conflict: reasoning spans with clear advancement can receive *low* distillation reward simply for deviating from teacher outputs. R2-OPD constructs two within-trajectory rankings of reasoning spans — one from teacher rewards, one from measured reasoning progress — and filters/upweights training signal where the rankings disagree. |
| **Key innovations** | First OPD method to treat teacher reward vs. reasoning progress divergence as a first-class filtering signal rather than noise; span-level (not token-level) credit. |
| **Why it matters** | Complementary to SOPD (granularity) and GC-OPD (verifier residuals): all three attack the same failure mode — teacher likelihood ≠ learning value. If OPD keeps requiring task-specific patches, its "free lunch" reputation may need revision (cf. [[strong-teacher-distillation]]). |

### 1.3 Capacity-Dependent Effects of Data Selection for Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Cuong Dang, Hoang Anh Just, Ruoxi Jia |
| **Institution** | Virginia Tech *(inferred: Ruoxi Jia's group)* |
| **Submitted** | 2026-08-13 · [2608.13721](https://arxiv.org/abs/2608.13721) · cs.LG |
| **Abstract** | Likelihood-based response selection says high-likelihood (student-close) teacher responses are preferable SFT data. Controlled experiments across 1.5B–8B students reveal a capacity-dependent **"Fast-Fit / Slow-Gain"** pattern: high-likelihood data gives faster, more stable early gains (especially small models), but low-likelihood data becomes increasingly beneficial for larger models given longer training. Small models fail to absorb low-likelihood supervision and collapse into shallow/repetitive behavior; learning-dynamics analysis shows 1.5B students drift *away* from the teacher under either regime. |
| **Key innovations** | Refutes the universal "pick highest-likelihood responses" heuristic; shows data-selection strategy must be co-chosen with model capacity and compute budget; capacity-constrained distillation theory tying data difficulty, data span, and transfer. |
| **Why it matters** | The scaling-axis answer to the OPD debates above: what looks like a bad supervision signal at 1.5B may be the right one at 8B. Directly relevant to any lab running mixed-size model families (cf. ADAPT below). |

### 1.4 How to Train a Critic Stably and Efficiently (BPCO)

| Field | Detail |
|-------|--------|
| **Authors** | Penghui Qi, Xiangxin Zhou, Wee Sun Lee |
| **Institution** | National University of Singapore *(inferred: Wee Sun Lee)* |
| **Submitted** | 2026-08-24 · [2608.23566](https://arxiv.org/abs/2608.23566) · cs.LG |
| **Abstract** | GRPO-family methods avoid critics by sampling groups per prompt. A reliable critic could estimate token-level advantages from a *single* response, but standard critic recipes are unstable. Best-Practice Critic Optimization combines DPPO-style updates, value predictions bounded to the reward range, Monte Carlo value targets, unnormalized policy advantages, and length-adaptive GAE. Since the critic exists only during training, it can be conditioned on reward-defining information (reference answers, grading rubrics) hidden from the policy — privileged-critic training without serving cost. |
| **Key innovations** | A reproducible recipe isolating each design choice behind critic instability in LLM RL; privileged information injection via train-only critic (cf. Le Critique, [2608.16739](../2026-08-17/arxiv-paper-check.md)). |
| **Why it matters** | If single-sample advantage estimation works reliably, RLVR inference budgets drop substantially — the group-sampling tax that GRPO pays on every prompt is not fundamental. |

### 1.5 Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM Policy Optimization (ERPO)

| Field | Detail |
|-------|--------|
| **Authors** | Xianlei Zhou, Xiangdi Meng, Yu He, Tianyu Qi, Shuyan Guan, Xianli Zhang, Jian Zhang et al. |
| **Institution** | Not stated |
| **Submitted** | 2026-08-24 · [2608.23311](https://arxiv.org/abs/2608.23311) · cs.CL |
| **Abstract** | Policy-KL regularization on the action side creates a double bind: keep it and you constrain behavior while consuming exploration budget; drop it and optimization drifts unchecked. ERPO moves regularization to the *input* side: a Query-KL term bounds how far the policy-induced training-query distribution drifts from the pre-RL reference, plus reference-derived per-query weights biasing updates toward queries typical of the original data distribution. |
| **Key innovations** | Regularizes the environment/query distribution instead of the response distribution — breaking the stability-exploration trade-off rather than tuning along it. |
| **Why it matters** | Same input-side philosophy as ERPO-style curriculum control appearing across this week's RL papers (LURE's difficulty positioning below); treats "what the model trains on" as a controllable policy variable, not fixed data. |

### 1.6 Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs (ADAPT)

| Field | Detail |
|-------|--------|
| **Authors** | Yan Zhou, Sara Kangaslahti, Jonathan Geuter, Nihal V. Nayak, Marco Fumero, Francesco Locatello, David Alvarez-Melis |
| **Institution** | Harvard + collaborators *(inferred: Alvarez-Melis group; Locatello — ISMB)* |
| **Submitted** | 2026-08-24 · [2608.22854](https://arxiv.org/abs/2608.22854) · cs.LG |
| **Abstract** | Deploying LLM families requires (variant × size) grids — instruction-tuned, reasoning-tuned, chat — at multiple sizes. Producing each cell independently is prohibitive. Boomerang distillation amortized along the size axis for base models; ADAPT amortizes across *both* axes simultaneously, constructing intermediate-size post-trained variants from a single teacher-student pair per variant without per-cell training runs. |
| **Key innovations** | Treats a whole model family as one optimization object; size interpolation composes with post-training variants rather than being redone per variant. |
| **Why it matters** | Industrial economics: model families are becoming product lines. Combined with 1.3's finding (capacity determines which data helps), family-level distillation planning is emerging as its own discipline. |

---

## ② Recommendation & Generative Rec (6)

### 2.1 Towards a Densing Law for User Representation Learning at Billion-Scale Capacity

| Field | Detail |
|-------|--------|
| **Authors** | Bin Dou, Junru Zhang, Zhaoyi Yuan, Wuliang Huang, Letian Gong, Baokun Wang, Huan Li et al. |
| **Institution** | Ant Group / Alipay *(inferred: billion-scale Alipay dataset named in abstract)* |
| **Submitted** | 2026-08-24 · [2608.23392](https://arxiv.org/abs/2608.23392) · cs.IR |
| **Abstract** | Industrial user-representation scaling (users × sequence length × model size) hits a raw-data bottleneck: performance gains diminish as raw-text behavioral input grows past billion-scale capacity. Pilot study on Alipay shows tokenization sustains gains where raw scaling saturates. The paper then derives a **User Behavioral Densing Law**: a quantitative relation between data scale and the minimum sufficient tokenization capacity. |
| **Key innovations** | First scaling-law-style treatment of *tokenization configuration* as the scaled quantity — "how many semantic tokens per user" replaces "how many parameters" as the design variable. |
| **Why it matters** | Extends the wiki-tracked CTR/recsys scaling-law corpus ([[kunlun-scaling-law]], [[wukong-scaling-law]], [[understanding-scaling-laws-rec]]) into the tokenization axis; complements SID codebook sizing work ([dynamic single-level codebook, 2608.21012](../2026-08-23/arxiv-ai-search.md)). |

### 2.2 The Disconnect Between Better Descriptive Reasoning Trace Quality and Recommendation Effectiveness

| Field | Detail |
|-------|--------|
| **Authors** | Gustavo Penha, Juan Elenter, Claudia Hauff, Hugues Bouchard, Paul Bennett, Mounia Lalmas |
| **Institution** | Spotify Research *(inferred: author team)* |
| **Submitted** | 2026-08-24 · [2608.23154](https://arxiv.org/abs/2608.23154) · cs.IR |
| **Abstract** | CoT-augmented generative recommenders need costly alignment before an LLM can reason over opaque Semantic IDs. This enables a clean 2×2 factorial study — item representation (Title vs. SID) × semantic grounding (minimal vs. extensive SID alignment) — on three Amazon domains with a shared Qwen3-1.7B backbone. Findings: introducing explicit descriptive reasoning traces *reduces* traditional offline recommendation effectiveness, even when trace quality measurably improves. Better-looking reasoning ≠ better recommendation. |
| **Key innovations** | First controlled decomposition showing reasoning-trace quality and recommendation effectiveness are decoupled; challenges the Think-then-Answer recipe for FRMs. |
| **Why it matters** | Direct counter-evidence to the explicit-CoT direction (OneRec-Thinking, RecOne lineage) and support for latent-reasoning alternatives like WhisperRec (covered [2026-07-30](../2026-07-30/arxiv-ai-search.md)) and the [[rporec-reasoning-recommendation]] line. Expect renewed scrutiny of "reasoning for rec" evaluation practices. |

### 2.3 Adaptive Item-based Collaborative Structures via Noise Rescheduling in Diffusion for Generative Recommendation (ANR-DiffRec)

| Field | Detail |
|-------|--------|
| **Authors** | Jiaqi Wang, Tianying Liu, Heng Chang, Jihong Guan, Wengen Li, Shuigeng Zhou |
| **Institution** | Tongji University + Fudan University *(inferred: Guan/Li — Tongji, Zhou — Fudan)* |
| **Submitted** | 2026-08-24 · [2608.23400](https://arxiv.org/abs/2608.23400) · cs.IR |
| **Abstract** | Discrete diffusion recommenders model history as iterative denoising but underuse item-based collaborative structure: item representations are semantics-focused without collaborative priors, and denoising uses a uniform noise schedule ignoring item-level structural dependencies. ANR-DiffRec injects item-based collaborative priors into representations and reschedules noise adaptively per item structure during diffusion. |
| **Key innovations** | Non-uniform, structure-aware noise schedules for discrete diffusion rec; collaborative-prior-conditioned item tokens. |
| **Why it matters** | Diffusion-for-rec is a small but growing branch of generative recommendation; this addresses the same "collaborative signals missing in semantic pipelines" gap as GALLM ([2608.12184](../../papers/recommendation/)) did for LLM backbones. |

### 2.4 Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms to Semantic Subwords (SST)

| Field | Detail |
|-------|--------|
| **Authors** | Xinrui Miao, Mingjia Yin, Jiaqing Zhang, Wei Guo, Yong Liu, Yuyang Ye, Hao Wang et al. |
| **Institution** | USTC-affiliated team *(inferred)* |
| **Submitted** | 2026-08-24 · [2608.22734](https://arxiv.org/abs/2608.22734) · cs.IR |
| **Abstract** | Fixed-length semantic-ID sequences trigger **Intra-item Attention Overload**: encoder attention is spent reassembling low-level intra-item atoms instead of modeling inter-item behavioral transitions. SST represents historical items as variable-length semantic subwords (merged stable adjacent atoms) while keeping fixed-length decoding for targets; Behavior-induced Co-occurrence Augmentation injects coarse prefix-transition signals into the freed capacity. |
| **Key innovations** | Asymmetric tokenization — compressed subwords for history, full SIDs for target decoding; attention reallocation from intra-item to inter-item patterns. |
| **Why it matters** | Attacks the same RQ-stack inefficiency as the dynamic single-level codebook paper ([2608.21012](../2026-08-23/arxiv-ai-search.md)) but via merging rather than flattening — two independent labs converging on "SID atom granularity is wrong for context encoding." |

### 2.5 Hierarchical Exponential-Gaussian Mixtures for Watch-Time Distribution Prediction (HEGM)

| Field | Detail |
|-------|--------|
| **Authors** | Sofia Gulevskaia, Mikhail Trapeznikov, Aleksandr Poslavsky, Alexander D'yakonov |
| **Institution** | Lomonosov Moscow State University + industrial partner *(inferred: D'yakonov — MSU; "large-scale industrial datasets")* |
| **Submitted** | 2026-08-24 · [2608.23356](https://arxiv.org/abs/2608.23356) · cs.IR |
| **Abstract** | Watch-time distributions are near-zero-inflated, long-tailed, multimodal. A large-scale reproduction study finds EGMN (the recent SOTA mixture network) suffers variance collapse, component redundancy, and inactive components. HEGM fixes these via hierarchical skip-watch decomposition, KL-based variance regularization, structured initialization, and removal of the forced Gaussian shift and entropy regularizer. Improves ranking accuracy and threshold-event prediction on public + industrial data. |
| **Key innovations** | Reproduction-first methodology exposing silent failure modes of a published SOTA; hierarchical mixture decomposition matched to zero-inflation structure. |
| **Key relevance** | Watch-time is the core value signal in short-video ranking/bidding (cf. Multi-Decoder OneRec's watchtime decoder, Kwai26 benchmark). Distribution-level WT prediction feeds directly into eCPM-style objectives. |

### 2.6 Why This, Not That? Mining User Profiles for Pair-wise Counterfactuals

| Field | Detail |
|-------|--------|
| **Authors** | Meysam Varasteh, Veronika Bogina, Noam Koenigstein, Robin Burke |
| **Institution** | Reichman University + CU Boulder *(inferred: Koenigstein — Reichman, Burke — CU Boulder)* |
| **Submitted** | 2026-08-21 · [2608.21662](https://arxiv.org/abs/2608.21662) · cs.IR |
| **Abstract** | Proposes pairwise interpretation of rankings — "why is item A ranked higher than item B?" — grounded in the recommender's own logic rather than post-hoc explanation templates. Counterfactual techniques identify which items in the user's profile caused the relative ordering; validated across multiple datasets. Motivated by psychology-of-communication findings that comparative explanations are more natural than absolute ones. |
| **Key innovations** | Reframes explanation as a *relative*, algorithm-grounded task; counterfactual profile mining for rank deltas. |
| **Why it matters** | Explainability work in this wiki has been sparse; comparative explanations map cleanly onto conversational-rec UX and onto regulator-facing transparency (cf. provider-transparency paper [2608.21641](https://arxiv.org/abs/2608.21641), same wave, not separately filed). |

---

## ③ Advertising / CTR & Ranking (2)

### 3.1 Cascading Relevance-driven Recommendation Network for CTR Prediction in Trigger-Introduced Recommendation (CRRN)

| Field | Detail |
|-------|--------|
| **Authors** | Kaixuan Chen, Wenwen Wang, Xing Fang, Yang Huang, Jing Wang |
| **Institution** | Not stated (e-commerce industrial scenario) |
| **Submitted** | 2026-08-24 · [2608.22973](https://arxiv.org/abs/2608.22973) · cs.IR |
| **Abstract** | Trigger-Introduced Recommendation (TIR): users click a trigger item expressing instant interest, then browse related target items on the follow-on page. Unlike search queries, triggers are vague and implicit; unlike standard rec, relevance to the trigger is decisive. CRRN explicitly models trigger–target interaction and relevance with three components (tri-layer cascading relevance structure described in paper), emphasizing immersive continuity from trigger click to target impressions. |
| **Key innovations** | Formalizes TIR as a distinct prediction scenario with its own relevance semantics — intermediate between search (explicit intent) and feed rec (diffuse intent). |
| **Why it matters** | Scenario taxonomy for industrial CTR models is getting finer-grained (search → TIR → feed → push, cf. PushDualGen). Each surface now warrants bespoke relevance modeling — relevant to anyone porting one CTR stack across surfaces. |

### 3.2 From Click Modeling to Offline and Off-Policy Evaluation in Carousel Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Jing Kang (PhD research summary) |
| **Institution** | Not stated |
| **Submitted** | 2026-08-22 · [2608.22022](https://arxiv.org/abs/2608.22022) · cs.IR |
| **Abstract** | Carousels present several ranked lists simultaneously as swipeable rows; clicks depend on row organization, viewport constraints, and item context, not just preference — so feedback interpretation and policy evaluation from logs are ill-posed under single-list assumptions. The thesis develops carousel-specific click models accounting for 2-D layout effects, then offline/off-policy evaluation methods for carousel policies from logged data. |
| **Key innovations** | Layout-aware click models; OPE machinery for multi-list interfaces where presentation order confounds preference. |
| **Why it matters** | Most production surfaces (app homes, streaming rows) are carousels, yet nearly all published CTR/OPE methodology assumes one ranked list — a systematic blind spot now being formalized. |

---

## ④ Games, Agents & World Models (3)

### 4.1 From Generation to Simulation: How Far Are World Models from Being True Simulators?

| Field | Detail |
|-------|--------|
| **Authors** | Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang, Gang Zhao |
| **Institution** | Not stated |
| **Submitted** | 2026-08-24 · [2608.23070](https://arxiv.org/abs/2608.23070) · cs.AI |
| **Abstract** | Surveys whether generative world models can replace physics/game engines and RL environments, using eight simulator capabilities as an external yardstick (asset construction, physics engine, interaction, controllability, stability, state feedback, diversity, evaluation metrics). Maps 200 representative works (2018–June 2026) across three technical routes — latent dynamics, video generation, joint-embedding prediction. Verdict: functional substitution achieved in interaction and controllability for specific settings; physics fidelity, long-horizon stability, state feedback, and standardized evaluation remain open gaps. |
| **Key innovations** | Capability-based yardstick instead of benchmark-score comparison; route×capability mapping of the entire field. |
| **Why it matters** | The field-mapping companion to the wiki's dense world-model coverage (ForgeWM, Marionette, PlayWorld etc. in [game-rl-daily](../../index.md)); useful for judging claims like DreamX-Phi or S2-HWM against what simulators actually require. |

### 4.2 GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?

| Field | Detail |
|-------|--------|
| **Authors** | Kun Chen, Haorong Hong, Peizhong Gao, Jianfeng Lin, Tongxu Luo, Yuxuan Xie, Chenxu Liu et al. |
| **Institution** | Not stated |
| **Submitted** | 2026-08-22 · [2608.21833](https://arxiv.org/abs/2608.21833) · cs.AI |
| **Abstract** | Evaluates coding agents building complete games from natural language, where program logic, visual/audio content, UI, interaction, and playability must function in one executable artifact. From analysis of human-agent development trajectories, operationalizes three lifecycle stages — initial generation, bug diagnosis & repair, multi-turn optimization — as benchmark tasks, evaluating both the game product and the development process. |
| **Key innovations** | Process-aware game-dev evaluation (repair + iteration, not just final artifact quality). |
| **Why it matters** | Complements OpenGame/GameCoder-style artifact benchmarks already tracked ([[opengame-agentic-coding]]); the bug-fix and optimization stages measure agentic persistence, which Karpathy-wiki readers will recognize as the verification-gap problem in miniature. |

### 4.3 The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning (LURE)

| Field | Detail |
|-------|--------|
| **Authors** | Jing Yu, Shengchao Chen, Yiyun Tan |
| **Institution** | Not stated |
| **Submitted** | 2026-08-22 · [2608.21871](https://arxiv.org/abs/2608.21871) · cs.CL |
| **Abstract** | Zero-data self-play for LLM reasoning usually vetes task learnability only by probing candidates post hoc and credits solvers with sparse terminal rewards. LURE recasts self-play as a pursuit-evasion game: an LLM *evader* positions tasks along each environment's difficulty axis to stay one step ahead of a planner-executor pursuer; the evader trains on a capture-frontier reward peaking when the solver catches it on exactly half of rollouts — making "barely solvable" a learned positioning strategy rather than a hand-tuned rejection threshold. |
| **Key innovations** | Difficulty-axis positioning as the evader's action space; 50%-capture-rate frontier reward replacing post-hoc learnability filters; curriculum emergence + credit anchoring in one game frame. |
| **Why it matters** | Converges with SPADE (covered [2026-08-22](../2026-08-22/arxiv-ai-search.md)) on "environment design as a trained role," but solves the target-difficulty calibration problem explicitly — the missing piece SPADE handles only through regret signals. Also echoes ERPO's input-side-control theme from §1.5. |

---

## Cross-Cutting Themes (2026-08-25)

1. **On-policy distillation is being rebuilt from first principles.** SOPD (granularity), R2-OPD (progress filtering), Capacity-Dependent selection (student scale) form a coherent critique: teacher likelihood is a biased, capacity-dependent, trajectory-blind signal. Watch for a unified recipe absorbing all three.
2. **Tokenization is the new scaling axis in generative rec.** Alipay's Densing Law (tokenization capacity vs. data scale), SST's semantic subwords (merge atoms), and last week's single-level codebook (flatten hierarchy) all treat SID/tokenizer design as the primary lever, ahead of backbone architecture.
3. **Input-side / environment-side control beats output-side regularization.** ERPO (query-distribution KL), LURE (difficulty-axis positioning), SPADE (environment designer) all move the controllable variable from the policy's outputs to its training distribution.
4. **Explicit reasoning traces face a replication crisis in rec.** Spotify's factorial study shows better descriptive traces can *hurt* offline effectiveness — aligning with WhisperRec's latent-token results and raising the bar for Think-then-Answer recommender papers.

---

## Methodology Notes

- Sources: arXiv API (`export.arxiv.org`) category+keyword queries sorted by `submittedDate` desc over cs.IR / cs.CL / cs.LG / cs.AI / cs.GT; web-search cross-check for industrial papers.
- Dedup: every included ID grep-verified absent from `wiki/**`; ~40 additional same-wave papers were excluded as already covered (e.g., 2608.21274 Netflix field experiment, 2608.10562 MARCO, 2608.19197 SPADE).
- Institutions are stated only when printed on the paper itself; inferences are flagged and kept conservative.
