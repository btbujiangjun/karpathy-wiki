---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-11-15)"
type: synthesis
created: 2026-11-15
updated: 2026-11-15
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, memory, generative-recsys, reranking]
---

# arXiv Daily Report (2026-11-15)

> **Query time**: 2026-11-15. This report surveys recently submitted/indexed arXiv papers (primarily the 2026-11-10 to 2026-11-13 submission window visible in arXiv recent listings at query time) across AI, LLMs, agents, recommendation, advertising/CTR-related ranking and experimentation, sequential/trajectory modeling, and games.
>
> **Method**: Manual review of arXiv recent listing pages for `cs.CL`, `cs.LG`, `cs.AI`, `cs.IR`, and `cs.GT`, followed by abstract-level inspection of selected papers spanning the requested domains. Abstracts are condensed from arXiv metadata; results and metrics are **author-reported**. Affiliations are listed when explicitly stated in arXiv metadata/comments/author fields; otherwise marked as not specified in metadata.
>
> **Caveats**: Abstract-level review only (no reproduction). Industrial/online claims are single-paper reports unless noted. Recommendation, ranking, CTR/advertising, and sequential modeling overlap substantially; papers are grouped by primary emphasis.

## Summary

- **LLM internals and architecture research are becoming more explicit and infrastructure-oriented.** New work probes how LLMs encode goals causally, proposes a verifier for when diffusion language models should regenerate, and introduces a public platform for recording/reviewing/referencing architecture experiments with scaling-law predictions.
- **Agent memory is shifting from hand-designed modules to evolved and cost-aware systems.** Program evolution discovers memory designs that improve long-context QA efficiency, while cost-internalizing memory for successive coding tasks balances future usefulness against read/write/compute costs.
- **Generative recommendation is moving toward behavior- and trigger-aware modeling.** Recent papers target long-tail reachability, trigger-induced recommendation, and user trajectory prediction by rethinking tokenization, decoding, and training objectives.
- **Ranking/CTR-adjacent systems emphasize exposure modeling, preference alignment, and efficient experimentation.** Survival-based listwise evaluation/re-ranking and scaling-law-guided A/B experimentation aim to improve decision quality under real-world browsing and compute constraints.
- **Web-behavior prediction and strategic interaction highlight evaluation and dynamics pitfalls.** A benchmark audit shows candidate-support confounds in offline web-action prediction, while a new spatial game model studies convergence vs. fragmentation in competitive resource landscapes.

---

## A. AI, LLMs, and Agent Systems

### 1. Goal Encoding in LLMs
- **arXiv**: [2611.17297](https://arxiv.org/abs/2611.17297)
- **Authors**: Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.AI, cs.LG (submitted 2026-11-12)
- **Abstract**: Investigates whether LLMs encode goals as internal neural representations that precede and guide action across different execution paths. In a multi-subtask coding setting, the authors localize next-subgoal encodings in outputs of a sparse set of attention heads, decode them into natural language descriptions of future actions, and show the encoding is causal and transferable across environments (e.g., different programming languages). They propose a non-recurrent goal-seeking (NRGS) account in which the model repeatedly re-reads the goal and compares it with visible progress, and test this with targeted causal interventions.
- **Key innovations**:
  - **Localized goal representations**: identifies sparse attention-head outputs encoding the next sub-goal.
  - **Causal and plastic interventions**: demonstrates that transplanted goal encodings can trigger equivalent operations in new contexts.
  - **NRGS account**: explains sustained goal pursuit without explicit recurrence via repeated goal re-reading and progress comparison.
- **arXiv link**: https://arxiv.org/abs/2611.17297

### 2. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
- **arXiv**: [2611.17332](https://arxiv.org/abs/2611.17332)
- **Authors**: Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.LG (submitted 2026-11-12)
- **Abstract**: Presents ArchSpace, a public platform for recording, reviewing, and referencing LLM architecture research. The platform aims to make architectural successes/failures and reasoning more transparent and comparable by pairing proposals with experiments and community review. To reduce large-scale training costs, it uses scaling laws to predict larger-model loss from smaller experiments and provides initial baselines (Qwen3.5, OLMo3), fitted scaling laws, and a reusable training recipe.
- **Key innovations**:
  - **Architecture research infrastructure**: shared workflow for documenting, reviewing, and referencing model-architecture ideas.
  - **Scaling-law-guided evaluation**: extrapolates small-scale experiments to larger settings before costly training.
  - **Reusable references**: baselines, fitted scaling laws, and training recipes to improve comparability.
- **arXiv link**: https://arxiv.org/abs/2611.17332

### 3. Learning When Diffusion Language Models Should Regenerate
- **arXiv**: [2611.17320](https://arxiv.org/abs/2611.17320)
- **Authors**: Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, Minsik Seol, Jungwoo Lee
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL (submitted 2026-11-12)
- **Abstract**: Studies remasking in diffusion language models and finds that token confidence poorly exposes errors while hidden states contain useful error information; isolated remasking often reproduces errors when context is fixed. Proposes DiVR, a verifier trained on final correctness of the model’s own trajectories to decide when to regenerate a block and which alternative to retain, leaving the generator unchanged. On five reasoning benchmarks with LLaDA-8B-Base, DiVR improves average accuracy from 35.3% to 43.4% at 1.9–3.5× greedy-decoding cost, outperforming search baselines at higher cost and complementing SFT/RL; it also generalizes to other generators such as Dream.
- **Key innovations**:
  - **Correctness verifier for diffusion LMs**: learns when regeneration is likely to help from trajectory outcomes.
  - **Targeted regenerate-and-select policy**: decides both timing and candidate retention without modifying the generator.
  - **Efficiency-quality trade-off**: achieves stronger reasoning gains than search baselines at lower relative compute overhead.
- **arXiv link**: https://arxiv.org/abs/2611.17320

### 4. Discovering Effective Agent Memory Designs through Program Evolution
- **arXiv**: [2611.17068](https://arxiv.org/abs/2611.17068)
- **Authors**: Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang, Tairan Chen, Wenya Xie, Yu Hou, Rui Zhang, Zirui Liu
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.AI (submitted 2026-11-12)
- **Abstract**: Introduces MAPE, a framework that evolves whole agent memory programs from minimal seeds via a standardized lifecycle interface and iterative diagnosis-proposal loop. On LoCoMo and LongMemEval, evolved designs achieve up to +12% absolute accuracy over manually designed baselines at 35% serving cost, with transfer across serving backbones/benchmarks. Analyses identify recurring patterns: retaining raw conversations as retrievable evidence and composing retrieved evidence by query intent; transplanting the composition module improves five existing memory systems.
- **Key innovations**:
  - **Program-evolution search for memory**: automatically discovers end-to-end memory designs rather than tuning fixed modules.
  - **Empirical design principles**: raw-evidence retention and intent-aware evidence composition improve answer quality.
  - **Cost-aware objective shaping**: optimizing cost with accuracy shifts computation toward selective query-time processing.
- **arXiv link**: https://arxiv.org/abs/2611.17068

### 5. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
- **arXiv**: [2611.17316](https://arxiv.org/abs/2611.17316)
- **Authors**: Peiwen Li (Yale University), Harshit Verma (Yale University), Sophia Zhou (Yale University), Haiwen Wang (Yale University), Ngoc Bui (Yale University), Heng Chang (Tsinghua University), Fei Fei (Goodvision AI), David van Dijk (Yale University), Rex Ying (Yale University)
- **Institution/Company**: Yale University; Tsinghua University; Goodvision AI (author-affiliation annotations in arXiv metadata)
- **Categories**: cs.AI, cs.CL, cs.SE (submitted 2026-11-12)
- **Abstract**: Addresses memory selection for coding agents performing successive tasks on evolving repositories, where future tasks are unknown and memory has read/write costs. CoReMem uses prospective segment valuation (with/without trajectory segments on the next task) to build compact anchor-based memories (repository locations and executable checks), and adapts the actor via on-policy memory-value estimation with provenance-gated value credit. On ChainSWE, a 27B actor’s resolve rate rises from 21.0% to 25.7% with 17% fewer steps and 11% fewer total cache-aware tokens (including memory-module calls).
- **Key innovations**:
  - **Prospective memory valuation**: estimates future usefulness of memory segments before the next task is known.
  - **Anchor-based memory representation**: stores actionable repository/check anchors instead of verbose traces.
  - **Provenance-gated credit assignment**: rewards steps that actually use memory-supplied anchors while preserving outcome credit.
- **arXiv link**: https://arxiv.org/abs/2611.17316

---

## B. Recommendation, Sequential Modeling, Advertising, and CTR/Ranking

### 6. KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
- **arXiv**: [2611.16795](https://arxiv.org/abs/2611.16795)
- **Authors**: Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Institution/Company**: Kuaishou (dataset/industrial source stated in abstract); other affiliations not fully specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-12; accepted to NeurIPS 2026 per comments)
- **Abstract**: Introduces KuaiRecV2, an industrial-scale benchmark from Kuaishou to reduce offline-online gaps in recommendation. It targets three challenges: large-scale continual learning under dynamic item pools/distribution shifts, combinatorial diversity at token and item levels, and multi-task reward balancing for controllable generative models. The benchmark provides million-scale multi-modal items and 30-day interaction records with a dynamic video candidate pool, and evaluates retrieval accuracy, diversity, and multi-task performance in a unified rubric.
- **Key innovations**:
  - **Realistic continual-learning benchmark**: long-horizon, dynamic-candidate, multi-modal industrial recommendation data.
  - **Unified evaluation rubric**: jointly measures accuracy, diversity, and multi-task objectives.
  - **Focus on generative recsys controllability**: highlights balancing sequence modeling quality with multi-task reward demands.
- **arXiv link**: https://arxiv.org/abs/2611.16795

### 7. ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability
- **arXiv**: [2611.16404](https://arxiv.org/abs/2611.16404)
- **Authors**: Muyu Zou, Shunye Tang, Yi Xu, Haibo Xing, Yandong Wang, Lingyu Mu, Jinxin Hu
- **Institution/Company**: Not specified in arXiv metadata (deployed in authors’ production system per abstract)
- **Categories**: cs.IR (submitted 2026-11-12)
- **Abstract**: Studies long-tail reachability in generative recommendation across semantic ID (SID) construction, decoding, and matching. Finds parallel SID construction outperforms sequential SIDs for tail items under equal code lengths, and that partial matching can recover relevant tail items even when full generation fails—though beam search pruning can block recovery. Proposes ReSID: long parallel SIDs with popularity-debiased and user-semantic-aware beam search plus partial SID matching. Reports state-of-the-art long-tail retrieval with competitive overall accuracy, lower latency/higher throughput under narrow beams, and production deployment gains.
- **Key innovations**:
  - **Pipeline-level reachability analysis**: diagnoses long-tail failures across SID design, decoding, and matching.
  - **Parallel SIDs + dual beam search**: preserves promising tail candidates via debiased and semantic-aware search.
  - **Partial SID matching recovery**: exploits locally consistent decoded prefixes to retrieve tail items.
- **arXiv link**: https://arxiv.org/abs/2611.16404

### 8. TriGen: A Generative Paradigm for Trigger-Induced Recommendation
- **arXiv**: [2611.16395](https://arxiv.org/abs/2611.16395)
- **Authors**: Muyu Zou, Haibo Xing, Shunye Tang, Liyan Tie, Lingyu Mu, Yandong Wang, Jinxin Hu
- **Institution/Company**: Not specified in arXiv metadata (full production deployment reported across six country markets)
- **Categories**: cs.IR (submitted 2026-11-12)
- **Abstract**: Targets trigger-induced recommendation (TIR), where a user click triggers an immediate follow-up feed requiring alignment with instant intent while preserving long-term preferences—distinct from standard user-induced generative recommendation. Proposes TriGen with calibrated tail injection to re-encode local history, dynamic gating to arbitrate persistent tastes vs. immediate impulses, and position-specific transformations for level-aware trigger guidance during decoding. Shows offline gains and online A/B improvements in revenue/GMV with production deployment.
- **Key innovations**:
  - **Generative TIR formulation**: explicitly models trigger-intent vs. long-term-preference tension in token-level generation.
  - **Calibrated tail injection + dynamic gating**: balances recent/local context and historical user signals.
  - **Position-specific decoding guidance**: maintains trigger relevance throughout autoregressive generation.
- **arXiv link**: https://arxiv.org/abs/2611.16395

### 9. From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction
- **arXiv**: [2611.16159](https://arxiv.org/abs/2611.16159)
- **Authors**: Jiaqi Wang, Hanchen Yang, Hengyu Zhang, Hongxu Ma, Wenqi Rao, Hongyang Wang, Zhongbo Sun, Renliang Qian, Weixin Chen, Wengen Li, Jihong Guan, Shuigeng Zhou, Qingpeng Cai, Peng Jiang, Hong Cheng
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-12)
- **Abstract**: Addresses user behavior trajectory prediction (UBTP), where sequential future interactions must be predicted from history. Argues that serial semantic-ID decoding in generative recommendation couples token generation with behavior transitions, ignores uncertainty, and suffers train-inference mismatch. Proposes TraGR, a behavior-aware framework that predicts SID tokens in parallel per interaction, models transitions via recurrent state updates, uses probability-weighted feedback over alternatives, and trains with relation-aware trajectory learning on model-generated trajectories. Reports consistent gains over SOTA baselines on four public datasets across horizons.
- **Key innovations**:
  - **Behavior-level generation**: parallel within-interaction SID prediction with explicit recurrent behavior-state transitions.
  - **Uncertainty-aware feedback**: combines selected behavior and probability-weighted alternatives for subsequent predictions.
  - **Trajectory learning on generated rollouts**: reduces exposure bias via relation-aware credit assignment and collaborative transition signals.
- **arXiv link**: https://arxiv.org/abs/2611.16159

### 10. ReAlign: Reward-Guided Preference Alignment for Generative Re-Ranking
- **arXiv**: [2611.15445](https://arxiv.org/abs/2611.15445)
- **Authors**: YaChen Yan, Liubo Li
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-11)
- **Abstract**: Proposes ReAlign for listwise re-ranking (CTR/engagement-oriented ranking refinement), coupling a listwise reward model with a candidate-aware autoregressive generator. The reward model decomposes listwise utility into position-wise contributions using survival-based exposure and per-objective value heads with uncertainty-based loss weighting. Training includes supervised pre-training on logged exposure lists and reward-guided post-training aligning generator distributions/rankings to standardized rewards. Extensive offline experiments show consistent gains over SOTA baselines.
- **Key innovations**:
  - **Generator–evaluator coupling**: gives the generative re-ranker direct access to listwise utility signals.
  - **Survival-based exposure + multi-objective value**: models cascading browsing and heterogeneous engagement objectives.
  - **Reward-guided preference alignment**: two-stage training to align generation with listwise rewards.
- **arXiv link**: https://arxiv.org/abs/2611.15445

### 11. SurvEval: Listwise Re-Ranking Evaluator via Survival-Based Exposure and Multi-Objective Value Modeling
- **arXiv**: [2611.15434](https://arxiv.org/abs/2611.15434)
- **Authors**: YaChen Yan, Liubo Li
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-11)
- **Abstract**: Introduces SurvEval, a listwise evaluator for re-ranking that jointly models user exposure and item value. It formulates sequential browsing as a discrete-time survival process to derive monotonically decreasing reaching probabilities and uses per-objective prediction heads with uncertainty-based loss weighting for multi-objective signals. Joint optimization via a shared transformer backbone yields listwise utility as the sum of position-wise exposure-value products. Experiments on KuaiRand and Avito show superior performance over SOTA baselines.
- **Key innovations**:
  - **Survival-model exposure**: principled cascading browsing/reaching probabilities for listwise evaluation.
  - **Multi-objective value estimation**: adaptive balancing of heterogeneous, noisy engagement objectives.
  - **Unified evaluator backbone**: end-to-end exposure-value modeling for re-ranking utility estimation.
- **arXiv link**: https://arxiv.org/abs/2611.15434

### 12. Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems
- **arXiv**: [2611.13539](https://arxiv.org/abs/2611.13539)
- **Authors**: Zhiliang Chen, Sammy Nammari, Jiahao Su, Xiaoqiang Luo
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR, cs.LG (submitted 2026-11-10)
- **Abstract**: Proposes using feature-invariant scaling laws to make A/B experimentation in recommendation systems (including advertising/recs model iteration contexts) more compute-efficient. The authors observe that performance changes follow predictable scaling behavior across feature changes and build a statistical-inference method to predict full-scale A/B effects with confidence intervals from small-scale experiments. Validated on Wukong, HSTU, and LLM-based recommendation models over 40+ changes, the method filters neutral/regressive changes efficiently and identifies improvements to HSTU’s MovieLens-20M performance.
- **Key innovations**:
  - **Feature-invariant scaling-law observation**: stable scaling behavior across diverse recsys feature/model changes.
  - **Predictive A/B inference**: estimates full-scale treatment effects and uncertainty from small-scale runs.
  - **Practical experimentation efficiency**: reduces compute for model/feature screening in industrial-scale recommendation workflows.
- **arXiv link**: https://arxiv.org/abs/2611.13539

### 13. IntentTwin: Deconfounding Candidate Support and the Oracle-to-Deployment Gap in Offline Web Behavior Prediction
- **arXiv**: [2611.12918](https://arxiv.org/abs/2611.12918)
- **Authors**: Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Daren Zha
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.IR, cs.LG (submitted 2026-10-27; v1 listed in recent window)
- **Abstract**: Audits offline web-behavior prediction benchmarks where inserting the demonstrated action into a finite candidate set can create a candidate-support confound. Introduces support-identifiability rate (SIR), constructs support-balanced candidate sets, and evaluates a target-free dual-path proposer combining support retrieval with open-vocabulary DOM/LM proposals. On filtered OPeRA, support balancing reduces SIR from 1.0 to 0.0 and exposes performance gaps (strong conditional reranker 0.7214 overall Exact@1; target-free dual-path 0.5212 vs. oracle conditional 0.7450). Similar audit/gap patterns appear on Mind2Web, with a semantic audit of OOV targets.
- **Key innovations**:
  - **Benchmark confound diagnosis**: formalizes and measures support leakage via SIR in offline action-prediction protocols.
  - **Support-balanced evaluation**: removes shortcut signals to better reflect deployment difficulty.
  - **Target-free dual-path proposal system**: combines retrieval and open-vocabulary generation for realistic candidate construction.
- **arXiv link**: https://arxiv.org/abs/2611.12918

---

## C. Games and Strategic Interaction

### 14. Learning Dynamics of the Influencer's Game in Resource Landscapes
- **arXiv**: [2611.17148](https://arxiv.org/abs/2611.17148)
- **Authors**: Mark Lovett Feng Fu
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.GT, econ.TH, physics.soc-ph (submitted 2026-11-12)
- **Abstract**: Introduces the "influencer’s game," a spatial game where players choose positions in a trait/resource landscape and receive shares based on relative influence. The paper proves a unique symmetric Nash equilibrium under strict log-concavity of the influence kernel and characterizes stability thresholds based on kernel parameters, player count, and resource distribution. Crossing the threshold yields bifurcations into specialist clusters, limit cycles, and self-similar sub-games; results are grounded with real-world resource data and extended to multi-agent reinforcement learning under partial observability and discretized strategies.
- **Key innovations**:
  - **New spatial competition framework**: models strategic positioning in continuous resource landscapes.
  - **Equilibrium and bifurcation analysis**: links kernel/geometry conditions to convergence vs. fragmentation dynamics.
  - **Theory-to-MARL bridge**: shows predicted bifurcation structure persists in learned, partially observed settings.
- **arXiv link**: https://arxiv.org/abs/2611.17148

---

## Notes

- **Coverage scope**: This daily report emphasizes recent papers relevant to the requested themes (AI/LLMs, recommendation, advertising/CTR-adjacent ranking, sequential modeling/trajectories, and games). Not every subdomain had equally explicit fresh hits in the same 1–2 day window; closely related areas (e.g., generative re-ranking, A/B experimentation, web behavior prediction) were included where they inform CTR/ads/recommendation workflows.
- **Affiliations**: arXiv metadata often omits structured institutional affiliations. This report includes explicit affiliations only when present in author annotations/metadata and otherwise marks them as not specified.
- **Potential follow-up**: For stricter affiliation/company completeness and deeper technical comparison (datasets, metrics, ablations), fetch each paper’s PDF/HTML and project pages for a second-pass enriched report.
