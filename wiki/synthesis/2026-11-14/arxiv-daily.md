---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-11-14)"
type: synthesis
created: 2026-11-14
updated: 2026-11-14
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, agents, recommendation, generative-recommendation, sequential-modeling, advertising, ctr, ranking, evaluation, continual-learning]
---

# arXiv Daily Report (2026-11-14)

> **Query time**: 2026-11-14. This report surveys recently submitted/indexed arXiv papers visible via the arXiv Export API at query time (primarily **2026-11-11 to 2026-11-12** submissions, e.g. `2611.15434`–`2611.17334`) across AI, LLMs, agents, recommendation, advertising/CTR-adjacent ranking and evaluation, sequential/generative recommendation, and related modeling topics.
>
> **Method**: arXiv Export API queries over `cs.AI`, `cs.CL`, `cs.LG`, `cs.IR`, `cs.GT` and keyword searches for recommendation, advertising, click-through/CTR, sequential modeling/recommendation, and games; sorted by `submittedDate` (descending) with title/abstract screening. Abstracts are condensed from arXiv metadata/pages; all results and metrics are **author-reported**. Affiliations are listed when identifiable from arXiv abstract/metadata pages retrieved at query time; otherwise marked as **not specified in arXiv metadata/abstract page**.
>
> **Caveats**: Abstract-level review only (no reproduction, no PDF-first affiliation audit beyond retrieved abs pages). Some papers span multiple categories; each is placed in its primary theme. A strict “last 24 hours” window cannot be guaranteed due to arXiv announcement/indexing timing.

## Summary

- **LLM/agent infrastructure is shifting toward architecture research process, memory economics, and decision-role analysis.** ArchSpace proposes a public record/review/reference loop with scaling-law-based early validation; CoReMem internalizes memory write/read costs and prospective value for successive coding tasks; Actor/Judge/Teacher analysis shows poor actors can still provide useful teaching signals.
- **Goal and behavior representations remain central to reliable LLM agents.** Goal Encoding localizes causal, plastic next-subgoal representations in sparse attention heads; AgentSSL studies agents leveraging unlabeled data for semi-supervised ML engineering, highlighting program selection as a bottleneck.
- **Generative recommendation is tackling trigger intent, long-tail reachability, trajectory structure, and continual evaluation.** TriGen targets trigger-induced recommendation, ReSID improves long-tail semantic-ID retrieval/recovery, TraGR reframes generation around user-behavior trajectories, and KuaiRecV2 provides a large-scale continual-learning benchmark with accuracy/diversity/multi-task evaluation.
- **Advertising/ranking-adjacent work emphasizes listwise utility and market/policy design.** SurvEval models exposure as a survival process with multi-objective value estimation for re-ranking evaluation, while Media Trading studies censored auction-price feedback and bidding under budget/performance trade-offs.
- **Interactive evaluation remains challenging when users adapt.** A formal analysis distinguishes common-distribution vs. induced-distribution effects, explaining why offline benchmarks and live A/B tests can recommend different models.

---

## A. AI, LLMs, and Agents

### 1. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
- **arXiv**: [2611.17332](https://arxiv.org/abs/2611.17332)
- **Authors**: Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.CL, cs.LG (submitted 2026-11-12)
- **Abstract**: Introduces ArchSpace, a public platform for recording LLM architecture proposals with experiments/reasoning, community review, and later reference. To reduce the cost of large-scale validation, it uses scaling laws to predict larger-scale loss from smaller experiments and provides initial baselines (including Qwen3.5 and OLMo3), fitted scaling laws, and a reusable training recipe.
- **Key innovations**:
  - **Research process infrastructure**: unifies recording, reviewing, and referencing of architecture ideas, including negative/abandoned results.
  - **Scaling-law prevalidation**: uses small-scale experiments to estimate larger-scale behavior before expensive training.
  - **Reusable starting point**: ships baselines, scaling-law fits, and training recipes to make community comparison more consistent.
- **arXiv link**: https://arxiv.org/abs/2611.17332

### 2. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
- **arXiv**: [2611.17316](https://arxiv.org/abs/2611.17316)
- **Authors**: Peiwen Li (Yale University), Harshit Verma (Yale University), Sophia Zhou (Yale University), Haiwen Wang (Yale University), Ngoc Bui (Yale University), Heng Chang (Tsinghua University), Fei Fei (Goodvision AI), David van Dijk (Yale University), Rex Ying (Yale University)
- **Institution/Company**: Yale University, Tsinghua University, Goodvision AI (as listed in arXiv abstract)
- **Categories**: cs.AI, cs.CL, cs.SE (submitted 2026-11-12)
- **Abstract**: Studies memory selection for coding agents across successive repository tasks where future tasks are unknown. CoReMem values trajectory segments prospectively by comparing next-task runs with/without segments, builds compact memory around anchors (locations and executable checks), and adapts actors using on-policy memory value with provenance-gated credit. On ChainSWE, a 27B actor improves resolve rate from 21.0% to 25.7% with 17% fewer steps and 11% fewer cache-aware tokens (author-reported).
- **Key innovations**:
  - **Prospective segment valuation**: measures next-task usefulness of memory candidates rather than relying only on past-task salience.
  - **Cost-internalizing memory design**: balances future utility against write/read costs and encourages compact anchor-based memory.
  - **Provenance-gated actor adaptation**: credits memory use when supplied anchors are actually acted on while retaining outcome credit.
- **arXiv link**: https://arxiv.org/abs/2611.17316

### 3. Goal Encoding in LLMs
- **arXiv**: [2611.17297](https://arxiv.org/abs/2611.17297)
- **Authors**: Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.CL, cs.AI, cs.LG (submitted 2026-11-12)
- **Abstract**: Investigates whether LLMs encode internal goal representations that precede and guide action. In a multi-subtask coding setting, the authors localize next-subgoal encodings to sparse attention heads, decode them into natural-language descriptions of future actions, and show causal/plastic effects via interventions (including transfer across environments/languages). They propose a non-recurrent goal-seeking account where models repeatedly re-read task specifications and compare progress in context.
- **Key innovations**:
  - **Localized goal representations**: identifies sparse attention-head outputs encoding the next subgoal.
  - **Causal and plastic interventions**: demonstrates that transplanted goal encodings can steer behavior across execution contexts.
  - **NRGS account**: explains sustained goal pursuit without recurrence via repeated context re-reading and progress comparison.
- **arXiv link**: https://arxiv.org/abs/2611.17297

### 4. AgentSSL: Can MLE Agents Leverage Unlabeled Data?
- **arXiv**: [2611.17323](https://arxiv.org/abs/2611.17323)
- **Authors**: Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.AI, cs.LG (submitted 2026-11-12)
- **Abstract**: Frames semi-supervised learning for ML engineering agents as program search over pipelines that can use scarce labels and abundant unlabeled data. Under weak feedback and matched compute, agents synthesize SSL code that exceeds strong human-engineered baselines in 8/12 settings (up to +21.8%, author-reported), but program selection is a major bottleneck (up to 47% drop). Introduces ProgramSelectBench with 16,977 agent-generated and human-engineered SSL programs and evaluates selection methods, including on real-world ecology detection tasks.
- **Key innovations**:
  - **Agentic SSL formulation**: treats SSL pipeline design as agent-driven program synthesis/search.
  - **ProgramSelectBench**: large benchmark for studying selection of candidate SSL programs.
  - **Selection bottleneck diagnosis**: separates code synthesis capability from reliable selection under limited supervision.
- **arXiv link**: https://arxiv.org/abs/2611.17323

### 5. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents
- **arXiv**: [2611.17167](https://arxiv.org/abs/2611.17167)
- **Authors**: Haochen Liu, Qianhao Zhu, Zixuan Wang, Dingming Li, Tongbo Chen, Peng Qiu, Yingqi Qu, Weiming Lu, Jun Xiao, Yongliang Shen
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.AI, cs.CL (submitted 2026-11-12)
- **Abstract**: Compares decision models used as actors, judges, and teachers in long-horizon agent settings. Models that act poorly can still judge trajectories effectively when given full outcomes, and judging per-action helpfulness can separate useful from useless actions. Using JEV as a teacher improves a Qwen2.5-1.5B policy over GRPO from 72.8% to 82.9% on ALFWorld and 56.8% to 71.4% on WebShop (author-reported).
- **Key innovations**:
  - **Role-separated evaluation**: distinguishes acting, judging, and teaching capabilities of the same decision model.
  - **Post-hoc consequence signal**: shows trajectory-level hindsight can reveal action value missed during acting.
  - **Practical teacher transfer**: demonstrates gains from a decision model as RL teacher despite limited acting performance.
- **arXiv link**: https://arxiv.org/abs/2611.17167

### 6. When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems
- **arXiv**: [2611.17239](https://arxiv.org/abs/2611.17239)
- **Authors**: Hannah Li
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: stat.ME, cs.AI (submitted 2026-11-12)
- **Abstract**: Analyzes evaluation when users adapt prompts/tasks in response to model behavior, making prompts endogenous. Defines and contrasts common-distribution effects (same prompt distribution) and induced-distribution effects (each model’s interaction-induced prompt distribution), showing offline benchmarks and live A/B tests can target different estimands and even rank models differently. Provides conditions for ranking agreement and discusses implications for variance, reward hacking, and novelty effects.
- **Key innovations**:
  - **Estimand clarification**: formally separates common-distribution and induced-distribution model comparisons.
  - **Benchmark-vs-A/B diagnosis**: explains systematic discrepancies between offline evaluation and live experiments.
  - **Decision guidance**: characterizes when rankings can reverse and when offline evaluation may suffice.
- **arXiv link**: https://arxiv.org/abs/2611.17239

---

## B. Recommendation, Generative Recommendation, and Sequential/User Modeling

### 7. KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
- **arXiv**: [2611.16795](https://arxiv.org/abs/2611.16795)
- **Authors**: Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Institution/Company**: Not specified in arXiv metadata/abstract page (dataset sourced from Kuaishou per abstract)
- **Categories**: cs.IR, cs.AI (submitted 2026-11-12)
- **Abstract**: Presents KuaiRecV2, an industrial-scale benchmark for recommendation under continual learning with dynamic item pools/distribution shifts, combinatorial diversity (token-level and item-level), and multi-task reward balancing. Provides million-scale multimodal item information, 30-day interaction records, a dynamic candidate pool, and a unified evaluation rubric requiring improvements across retrieval accuracy, diversity, and multi-task performance.
- **Key innovations**:
  - **Continual-learning benchmark**: targets realistic long-term model maintenance under changing inventories and distributions.
  - **Diversity-aware evaluation**: measures both fine-grained token-level and holistic item-level diversity trade-offs.
  - **Unified multi-metric rubric**: evaluates accuracy, diversity, and multi-task objectives together.
- **arXiv link**: https://arxiv.org/abs/2611.16795

### 8. TriGen: A Generative Paradigm for Trigger-Induced Recommendation
- **arXiv**: [2611.16395](https://arxiv.org/abs/2611.16395)
- **Authors**: Muyu Zou, Haibo Xing, Shunye Tang, Liyan Tie, Lingyu Mu, Yandong Wang, Jinxin Hu
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.IR, cs.AI (submitted 2026-11-12)
- **Abstract**: Addresses trigger-induced recommendation (TIR), where a click triggers an immediate follow-up feed requiring alignment to instant intent while preserving long-term preferences. TriGen adapts generative recommendation with calibrated tail injection for local history, dynamic gating to arbitrate persistent tastes vs. immediate impulses, and position-specific transformations for level-aware trigger guidance during decoding. Reports offline gains and online A/B improvements across six country markets with production deployment (author-reported).
- **Key innovations**:
  - **TIR-specific generative paradigm**: explicitly models the tension between trigger intent and historical preference continuity.
  - **Calibrated tail injection + dynamic gating**: re-encodes local context and balances short-term impulses with long-term tastes.
  - **Position-aware decoding guidance**: sustains trigger influence throughout token-level generation.
- **arXiv link**: https://arxiv.org/abs/2611.16395

### 9. ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability
- **arXiv**: [2611.16404](https://arxiv.org/abs/2611.16404)
- **Authors**: Muyu Zou, Shunye Tang, Yi Xu, Haibo Xing, Yandong Wang, Lingyu Mu, Jinxin Hu
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.IR (submitted 2026-11-12)
- **Abstract**: Studies long-tail item reachability in semantic-ID generative recommendation across SID construction, decoding, and matching. Finds parallel SIDs outperform sequential SIDs for tail items under equal code lengths and that partial matches can recover relevant items when full generation fails but beam search can prune recoverable prefixes. ReSID combines long parallel SIDs, popularity-debiased/user-semantic-aware beam search, and partial SID matching; reports strong long-tail retrieval, competitive overall accuracy, lower latency/higher throughput under narrow beams, and production deployment (author-reported).
- **Key innovations**:
  - **Reachability analysis**: diagnoses long-tail failures across the full GR pipeline rather than a single stage.
  - **Parallel SID + partial matching recovery**: preserves and exploits locally consistent decoded tokens for tail retrieval.
  - **Debiased, semantic-aware beam search**: keeps promising tail paths alive under tight serving budgets.
- **arXiv link**: https://arxiv.org/abs/2611.16404

### 10. From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction
- **arXiv**: [2611.16159](https://arxiv.org/abs/2611.16159)
- **Authors**: Jiaqi Wang, Hanchen Yang, Hengyu Zhang, Hongxu Ma, Wenqi Rao, Hongyang Wang, Zhongbo Sun, Renliang Qian, Weixin Chen, Wengen Li, Jihong Guan, Shuigeng Zhou, Qingpeng Cai, Peng Jiang, Hong Cheng
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.IR, cs.AI (submitted 2026-11-12)
- **Abstract**: Targets user behavior trajectory prediction (UBTP), where future interaction sequences must reflect evolving user needs. Proposes TraGR, a behavior-aware generative recommendation framework that predicts semantic-ID tokens in parallel within each interaction, models behavioral transitions via recurrent state updates, combines selected-behavior feedback with probability-weighted alternatives, and trains with relation-aware trajectory learning on model-generated trajectories. Reports consistent gains over state-of-the-art baselines across four public datasets and prediction horizons (author-reported).
- **Key innovations**:
  - **Behavior-level generation**: decouples intra-interaction token prediction from inter-interaction behavioral transitions.
  - **Probability-weighted feedback**: uses both chosen behavior and alternative distribution to guide subsequent predictions.
  - **Trajectory-aware training**: incorporates collaborative transition signals and credit assignment on generated trajectories.
- **arXiv link**: https://arxiv.org/abs/2611.16159

---

## C. Advertising, Ranking, and CTR-Adjacent Evaluation

### 11. SurvEval: Listwise Re-Ranking Evaluator via Survival-Based Exposure and Multi-Objective Value Modeling
- **arXiv**: [2611.15434](https://arxiv.org/abs/2611.15434)
- **Authors**: YaChen Yan, Liubo Li
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: cs.IR (submitted 2026-11-11)
- **Abstract**: Proposes a listwise evaluator for re-ranking that models sequential browsing as a discrete-time survival process, yielding monotonically decreasing reaching probabilities, and estimates multi-objective item value with per-objective heads and uncertainty-based loss weighting. The components are jointly optimized with a transformer backbone, and listwise utility is computed by summing products of reaching probabilities and conditional value estimates. Reports superior performance over state-of-the-art baselines on KuaiRand and Avito (author-reported).
- **Key innovations**:
  - **Survival-based exposure modeling**: captures cascading browsing behavior with principled reaching probabilities.
  - **Multi-objective value estimation**: balances heterogeneous objectives via dedicated heads and uncertainty weighting.
  - **Unified listwise utility**: integrates exposure and conditional value for re-ranking/CTR-adjacent evaluation.
- **arXiv link**: https://arxiv.org/abs/2611.15434

### 12. Media Trading with Censored Auction Prices: A Stochastic Control and Reinforcement Learning Approach
- **arXiv**: [2611.16992](https://arxiv.org/abs/2611.16992)
- **Authors**: Yun-Ithry Gamrani, Huyên Pham
- **Institution/Company**: Not specified in arXiv metadata/abstract page
- **Categories**: q-fin.TR, cs.LG, math.OC (submitted 2026-11-12)
- **Abstract**: Studies real-time bidding where agencies balance campaign performance, margins, and finite budgets under censored market-clearing prices observed only on winning bids. Formulates a continuous-time stochastic control model with latent prices, constructs price signals via randomized exploratory subcampaigns with consistency/MSE guarantees, and compares model-based control (forward-equation calibration + HJB policy iteration + PINN) with entropy-regularized actor-critic learning from observable information.
- **Key innovations**:
  - **Censored-feedback bidding formulation**: explicitly models information dependence on the bidding policy in ad auctions.
  - **Exploratory price estimation**: uses randomized subcampaigns to obtain consistent latent-price signals under stylized assumptions.
  - **Model-based vs. model-free comparison**: contrasts HJB/PINN and actor-critic approaches for budgeted advertising decisions.
- **arXiv link**: https://arxiv.org/abs/2611.16992

---

## Notes

- **Coverage**: The visible arXiv window at query time was centered on 2026-11-11–2026-11-12 submissions; papers from earlier dates were excluded from main picks unless necessary for topic balance. Dedicated, newly visible CTR-prediction architecture papers were limited in this window, so CTR-adjacent advertising/ranking/evaluation work is included.
- **Affiliations**: arXiv Export API/abs pages did not consistently expose structured affiliations for all papers; where unavailable, this report states “Not specified in arXiv metadata/abstract page” rather than guessing. For stronger institution coverage, verify author blocks in each PDF.
- **Duplicates/overlap**: This report avoids re-centering papers already highlighted in recent `wiki/synthesis/2026-11-12/*` and `wiki/synthesis/2026-11-13/*` digests (e.g. LUMIR, MANA) except where contextually relevant.
- **Follow-up (optional)**: Fetch PDFs for exact affiliations/venues, and re-run after the next arXiv announcement to capture 2026-11-13/14 batches if newly indexed.