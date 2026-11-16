# Recent arXiv Papers: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

**Date:** 2026-11-16  
**Sources:** arXiv recent listings (cs.CL, cs.IR, cs.AI, cs.LG past-week pages) and arXiv search, retrieved 2026-11-16.  
**Scope:** Recent papers spanning large language models/agents, recommender systems, advertising/CTR prediction, sequential/time-series modeling, and games. Institution/company is listed when identifiable from the arXiv abstract page metadata/comments; otherwise noted as not specified on the abstract page.

---

## LLMs and Language/Agent Modeling

### 1. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
- **Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.17332](https://arxiv.org/abs/2611.17332) (submitted 13 Nov 2026)
- **Subjects:** Computation and Language (cs.CL); Machine Learning (cs.LG)
- **Abstract:** Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult to establish whether improvements hold at larger scales or translate into broader impact. ArchSpace addresses both gaps as a public platform for Recording, Reviewing, and Referencing Architecture Research: each proposal is recorded with its experiments and reasoning, reviewed by the community, and referenced by later work. To evaluate ideas before costly large-scale training, ArchSpace leverages scaling laws to predict model loss at larger scales from smaller experiments, a practice widely adopted in industry. We provide initial references that make the platform usable: Qwen3.5 and OLMo3 baselines, fitted scaling laws, and a reusable training recipe. Ideas validated through this review can in turn become new baselines, and ArchSpace thereby aims to broaden the range of ideas that shape the next generation of models.
- **Key innovations:**
  - Proposes **ArchSpace**, a public platform to record, review, and reference LLM architecture proposals with experiments and rationale (addressing under-documented industry iteration and weak academic baselines).
  - Uses **scaling-law-based extrapolation** to predict larger-scale loss from smaller experiments for early validation before expensive training.
  - Seeds the platform with **Qwen3.5 and OLMo3 baselines, fitted scaling laws, and reusable training recipes**, enabling a feedback loop where validated ideas become new baselines.

### 2. Goal Encoding in LLMs
- **Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
- **Institution/Company:** Not specified on arXiv abstract page (project/code page referenced in comments: https://goals.baulab.info/)
- **arXiv:** [arXiv:2611.17297](https://arxiv.org/abs/2611.17297) (submitted 13 Nov 2026)
- **Subjects:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Abstract:** We investigate whether and how LLMs encode goals: internal neural representations that precede and guide action, and that are flexible enough to be realized through many different execution paths. We construct a coding setting with multiple sub-tasks that allows us to evaluate goal-seeking behavior and the selection of sub-goals. In this setting, we localize an encoding of the next sub-goal in the outputs of a sparse set of attention heads. The same heads can be used to decode the LM's future actions in natural language (e.g., "I'm checking if a word is a palindrome"). We verify that this encoding is causal for next action and is plastic: transplanting it into a different environment, e.g., another programming language, triggers the same operation realized with a different sequence of tokens. The LM also sustains the encoding throughout the action's execution, which is puzzling because a transformer LM without recurrence cannot carry a state forward for more tokens than it has layers left. We propose that it does not need to. Under a non-recurrent goal-seeking (NRGS) account, the LM frequently re-reads the goal from the task specification, compares it with the progress visible in the growing context, and pursues what remains. We test the predictions of this account with targeted causal interventions.
- **Key innovations:**
  - Localizes **next-subgoal representations** to a sparse set of attention heads that can be decoded into natural-language descriptions of future actions.
  - Demonstrates **causal and plastic goal encodings**: interventions affect next actions and transplanted encodings trigger the same operation in different environments (e.g., different programming languages).
  - Introduces the **Non-Recurrent Goal-Seeking (NRGS)** account explaining sustained goal-directed behavior without recurrence via repeated re-reading of goals/progress in context, supported by targeted causal interventions.

### 3. Discovering Effective Agent Memory Designs through Program Evolution
- **Authors:** Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang, Tairan Chen, Wenya Xie, Yu Hou, Rui Zhang, Zirui Liu
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.17068](https://arxiv.org/abs/2611.17068) (submitted 13 Nov 2026)
- **Subjects:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
- **Abstract:** Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness. We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative diagnosis-proposal loop. Experiments on LoCoMo and LongMemEval yield an absolute accuracy gain of up to 12% over manually designed baselines at 35% of the serving cost, with further evaluations supporting transfer across serving backbones and benchmarks. Empirical analyses and ablations identify and validate two recurring design patterns: retaining raw conversations as retrievable evidence preserves details omitted from extracted memories, while composing retrieved evidence according to query intent helps the answering model use it effectively. Transplanting the composition module into five existing memory systems improves accuracy across all five. Beyond these patterns, the search objective shapes where computation goes: optimizing serving cost alongside accuracy shifts computation from LLM-based memory construction to selective processing at query time while retaining competitive accuracy. Together, these findings offer empirical lessons for agent memory design.
- **Key innovations:**
  - **MAPE** evolves complete agent memory programs (not just prompts/components) via a standardized lifecycle interface and iterative diagnosis–proposal loop.
  - Achieves up to **+12% absolute accuracy at ~35% serving cost** versus manual baselines on LoCoMo/LongMemEval, with transfer across backbones/benchmarks.
  - Identifies reusable design patterns: **retain raw conversations as retrievable evidence** and **compose retrieved evidence by query intent**; transplanting the composition module improves five existing memory systems.

### 4. Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning
- **Authors:** Dawei Zhang, Yubin Huangfu, Jessica Fan, Boyu Wei, Likang Wu, Hongke Zhao, Ming He, Zhu Teng
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.16816](https://arxiv.org/abs/2611.16816) (submitted 13 Nov 2026)
- **Subjects:** Computation and Language (cs.CL)
- **Abstract:** To keep long interaction contexts tractable, stepwise group-relative training for multi-turn LLM agents materializes each source trajectory into multiple response rows and valid tokens. This expansion creates an outer-accounting problem distinct from within-trajectory credit assignment: row-based outcome statistics can count one episode outcome multiple times, while token-level reduction can assign unequal aggregate objective mass across trajectories. We term these effects outcome-statistics multiplicity and objective-mass imbalance. We introduce Outcome-Mass Alignment (OMA), a two-component method that makes both accounting choices explicit. Outcome Alignment computes outcome statistics over unique source trajectories, while Mass Alignment controls aggregate objective mass after within-trajectory aggregation of optimizer-native token objectives. Neither redesigns the base optimizer's credit assignment, importance ratios, or clipping. Across matched ALFWorld GRPO comparisons at two model scales, where failed trajectories typically expand much more than successful ones, OMA improves matched-horizon endpoint success by 7.0-9.4 percentage points. Ordinary WebShop exhibits weak or reversed expansion-outcome coupling and correspondingly mixed effects, whereas in a success-oriented WebShop setting, WebShop-SOL, OMA improves success nAUC from 0.399 to 0.511. Component ablations and GiGPO and GSPO comparisons further support component separability and cross-optimizer compatibility. These results show that trajectory expansion always defines an implicit weighting rule, but its practical effect depends on how expansion couples to outcomes and optimizer-native updates.
- **Key innovations:**
  - Diagnoses **outcome-statistics multiplicity** and **objective-mass imbalance** in multi-turn agent RL caused by materializing trajectories into multiple rows/tokens.
  - Proposes **Outcome-Mass Alignment (OMA)**: Outcome Alignment computes statistics over unique source trajectories; Mass Alignment controls aggregate objective mass after within-trajectory aggregation.
  - Improves ALFWorld endpoint success by **+7.0–9.4 pp** (matched GRPO settings) and WebShop-SOL success nAUC from **0.399 to 0.511**, with compatibility across optimizers (GRPO/GiGPO/GSPO).

### 5. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents
- **Authors:** Haochen Liu, Qianhao Zhu, Zixuan Wang, Dingming Li, Tongbo Chen, Peng Qiu, Yingqi Qu, Weiming Lu, Jun Xiao, Yongliang Shen
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.17167](https://arxiv.org/abs/2611.17167) (submitted 13 Nov 2026)
- **Subjects:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract:** Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well. We compare three decision models and three general LLMs as actors and judges on ALFWorld, and use JEV as a teacher on ALFWorld and WebShop. As actors, all six models are pulled away from a subgoal that must come first by an easier one. As judges that see the whole trajectory, the same models credit the steps toward that subgoal, and asking whether each action helped, rather than whether the task will succeed, separates useful from useless actions. As a teacher, JEV raises a Qwen2.5-1.5B policy over GRPO from 72.8% to 82.9% success on ALFWorld and from 56.8% to 71.4% on WebShop. These results suggest that a poor actor can still teach well, because judging an action after the episode ends reveals the consequences that acting must anticipate.
- **Key innovations:**
  - Separates decision-model roles (**actor, judge, teacher**) and shows acting quality does not fully predict teaching value in long-horizon tasks.
  - Finds **trajectory-level judging** (post-hoc, action-helpfulness framing) better credits prerequisite subgoals than outcome-success framing or acting.
  - Uses **JEV as a teacher** to improve a Qwen2.5-1.5B policy over GRPO: **72.8%→82.9%** (ALFWorld) and **56.8%→71.4%** (WebShop).

---

## Recommendation Systems

### 6. KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
- **Authors:** Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Institution/Company:** Includes Kuaishou authors/affiliation context implied by dataset source (Kuaishou) and authorship; specific affiliations not fully listed on arXiv abstract page
- **arXiv:** [arXiv:2611.16795](https://arxiv.org/abs/2611.16795) (submitted 13 Nov 2026; accepted to NeurIPS 2026 per comments)
- **Subjects:** Information Retrieval (cs.IR)
- **Abstract:** Recommender systems, which retrieve items of interest to users based on their interaction histories, have recently witnessed several key technological advancements, benefiting from the semantic representation space and model-data scaling. Nevertheless, practitioners and researchers have frequently encountered critical inconsistencies between simple offline evaluations and complex online results, and this gap still exists in the era of large models. In this work, we address several key factors that contribute to this inconsistency: 1) the *large-scale continual learning challenge* that assumes a practical demand to maintain long-term model effectiveness under dynamic item pools and distributional shifts; 2) the *combinatorial diversity challenge* that requires the generation strategy to solve the accuracy-diversity trade-off in both the finer token level and the holistic item level; and 3) the *multi-task reward balancing challenge*, which is particularly critical for modern generative models that can accurately model the sequence distribution but are less controllable for the multi-task demands. To address these challenges and further pave the way for the development of more realistic recommendation solutions, we introduce KuaiRecV2, a deliberately constructed benchmark with industrial-level datasets from Kuaishou. Specifically, we provide a large-scale interaction dataset with million-scale multi-modal item information and long-term interaction records across 30 days, with a dynamic video candidate pool. Additionally, we provide a rigorous benchmark that evaluates retrieval accuracy, diversity, and multi-task performance in one rubric system, where an effective advancement occurs if and only if the new method improves all metrics.
- **Key innovations:**
  - **KuaiRecV2 benchmark** targeting offline–online gaps via three challenges: continual learning under dynamic pools/shifts, accuracy–diversity trade-offs (token and item level), and multi-task reward balancing for generative recommenders.
  - Industrial-scale dataset from Kuaishou: **million-scale multimodal items, 30-day long-term interactions, dynamic candidate pool**.
  - **Unified evaluation rubric** requiring simultaneous improvement in retrieval accuracy, diversity, and multi-task performance.

### 7. ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability
- **Authors:** Muyu Zou, Shunye Tang, Yi Xu, Haibo Xing, Yandong Wang, Lingyu Mu, Jinxin Hu
- **Institution/Company:** Not specified on arXiv abstract page (deployed in authors' production system per abstract)
- **arXiv:** [arXiv:2611.16404](https://arxiv.org/abs/2611.16404) (submitted 13 Nov 2026)
- **Subjects:** Information Retrieval (cs.IR)
- **Abstract:** Generative recommendation (GR) represents items with discrete Semantic IDs (SIDs) and casts retrieval as sequence generation. Under skewed interaction distributions and tight serving budgets, GR struggles to retrieve long-tail items. In this work, we are the first to study long-tail reachability across the complete pipeline of SID construction, decoding, and matching. We find that under equal code lengths, parallel SID construction consistently outperforms sequential SIDs on tail items. Moreover, even when full generation fails, decoded sequences carry locally consistent information that retrieves relevant tail items via partial matching. Yet this recovery is bounded by upstream search, failing once beam search prunes all prefixes completable within a fixed mismatch tolerance. Motivated by these findings, we propose ReSID to jointly preserve and recover tail candidates. Built on long parallel SIDs, ReSID pairs popularity-debiased and user-semantic-aware beam search to keep promising paths alive with partial SID matching to recover items from surviving tokens. ReSID achieves state-of-the-art long-tail retrieval while maintaining competitive overall accuracy, with lower latency and higher throughput under narrow beams. ReSID is deployed in our production system, serving main user traffic with substantial business gains.
- **Key innovations:**
  - Analyzes **long-tail reachability end-to-end** in generative recommendation (SID construction, decoding, matching), showing parallel SIDs help tail retrieval and partial matches can recover candidates.
  - **ReSID** combines long parallel SIDs, **popularity-debiased and user-semantic-aware beam search**, and **partial SID matching** to preserve/recover tail items under narrow beams.
  - Reports SOTA long-tail retrieval with competitive overall accuracy, lower latency/higher throughput, and **production deployment with business gains**.

### 8. TriGen: A Generative Paradigm for Trigger-Induced Recommendation
- **Authors:** Muyu Zou, Haibo Xing, Shunye Tang, Liyan Tie, Lingyu Mu, Yandong Wang, Jinxin Hu
- **Institution/Company:** Not specified on arXiv abstract page (deployed in production across six country markets per abstract)
- **arXiv:** [arXiv:2611.16395](https://arxiv.org/abs/2611.16395) (submitted 13 Nov 2026)
- **Subjects:** Information Retrieval (cs.IR)
- **Abstract:** Generative recommendation typically operates under the User-Induced Recommendation (UIR) setting, predicting target items by autoregressively generating semantic IDs as a passive continuation of long-term user history. However, this paradigm overlooks Trigger-Induced Recommendation (TIR), an essential industrial scenario where a user click triggers an immediate follow-up feed. In TIR, recommendations must dynamically align with the instant trigger intent without compromising historical preference continuity. Traditional TIR methods rely on discriminative scoring and cannot guide token-level generation, while existing generative models lack mechanisms to reconcile this structural tension. To address this challenge, we propose TriGen, establishing a tailored generative paradigm for trigger-induced recommendation. TriGen introduces calibrated tail injection to re-encode local history, adaptively arbitrates between persistent tastes and immediate impulses via dynamic gating, and applies position-specific transformations to sustain level-aware trigger guidance across decoding steps. Extensive offline evaluations confirm consistent gains over competitive baselines. Furthermore, online A/B tests across six country markets demonstrate significant revenue and GMV improvements, leading to the full production deployment of TriGen.
- **Key innovations:**
  - Formulates and targets **Trigger-Induced Recommendation (TIR)** (click-triggered follow-up feeds) as distinct from user-history continuation (UIR) in generative recommendation.
  - **TriGen** uses **calibrated tail injection** (re-encode local history), **dynamic gating** to arbitrate long-term preferences vs immediate trigger intent, and **position-specific transformations** for level-aware trigger guidance during decoding.
  - Demonstrates offline gains and **online A/B improvements in revenue/GMV across six country markets** with full production deployment.

### 9. From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction
- **Authors:** Jiaqi Wang, Hanchen Yang, Hengyu Zhang, Hongxu Ma, Wenqi Rao, Hongyang Wang, Zhongbo Sun, Renliang Qian, Weixin Chen, Wengen Li, Jihong Guan, Shuigeng Zhou, Qingpeng Cai, Peng Jiang, Hong Cheng
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.16159](https://arxiv.org/abs/2611.16159) (submitted 13 Nov 2026)
- **Subjects:** Information Retrieval (cs.IR)
- **Abstract:** User behavior trajectory prediction (UBTP) aims to capture how a user's needs evolve over time by predicting the sequence of future interactions from that user's interaction history. Recent generative recommendation (GR) methods address this task through autoregressive generation of semantic IDs (SIDs). However, serial SID decoding couples token generation with behavior state transitions and requires multiple dependent steps per interaction. Discrete item feedback overlooks predictive uncertainty, and teacher-forced training leaves a training-inference gap in trajectory generation. To address these limitations, we propose TraGR, a behavior-aware generative recommendation framework that aligns generation, feedback, and learning with successive user behaviors. Its behavior-level architecture predicts SID tokens in parallel within each interaction and models behavioral transitions through recurrent state updates, with joint SID and item-level supervision. Probability feedback combines the selected behavior with a probability-weighted summary of alternatives to guide subsequent predictions. Relation-aware trajectory learning incorporates collaborative transition signals and later credit assignment into training on model-generated trajectories. Experiments on four public datasets demonstrate that TraGR consistently outperforms state-of-the-art baselines across different prediction horizons.
- **Key innovations:**
  - **TraGR** reframes generative recommendation around **behavior-level trajectory prediction**: parallel SID token prediction within an interaction plus recurrent state updates across interactions.
  - Introduces **probability feedback** (selected behavior + probability-weighted alternatives) and **joint SID/item-level supervision** to better represent uncertainty and transitions.
  - Uses **relation-aware trajectory learning** on model-generated trajectories with collaborative transition signals and later credit assignment, improving performance across horizons on four datasets.

---

## Advertising and CTR Prediction

### 10. Serving-Aligned Entire-Space Conversion Modeling via Click-Through Rate Knowledge Distillation
- **Authors:** Pavel Dolin, Xun Zou, Jiatian Wu, Deguang Kong
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.15137](https://arxiv.org/abs/2611.15137)
- **Subjects:** (as indexed on arXiv search; related to CTR/CVR/ads modeling)
- **Abstract:** Recommendation systems may use predicted click-through conversion rate (pCTCVR), the product of predicted click-through rate (pCTR) and post-click conversion rate (pCVR), to guide ranking decisions. Many pCVR models build on the Entire Space Multi-Task Model (ESMM), which jointly trains pCVR and auxiliary pCTR towers using pCTR and pCTCVR losses, but deploys only the pCVR tower. At serving time, this tower may be paired with a separately trained pCTR model, creating a training-serving mismatch in pCTCVR when its predictions differ from those of the auxiliary pCTR tower. In this paper, we use knowledge distillation (KD) from logged serving pCTR scores to supervise ESMM's auxiliary pCTR tower and improve training-serving pCTCVR alignment. We denote variants by KD-α, where α controls the hard-label loss weight. On the Ali-CCP dataset, KD-0.3, the best variant on serving pCTCVR, increases ROC-AUC not only for serving pCTCVR but also for pCVR by 2.1% and 1.6%, respectively, and PR-AUC by 9.9% and 8.8%, respectively, relative to the ESMM baseline. We also test negative downsampling with 5% nonclick retention. Downsampled KD-0.3 increases mean AUC for serving pCTCVR and pCVR by 1.2% and 0.9%, respectively, -and PR-AUC by 8.5% and 4.5%, respectively, relative to downsampled ESMM.
- **Key innovations:**
  - Addresses **training–serving mismatch** in ESMM-style pCTCVR pipelines when deployed pCTR differs from the auxiliary training pCTR tower.
  - Uses **knowledge distillation from logged serving pCTR scores** to supervise the auxiliary pCTR tower (KD-α variants), improving alignment with production ranking.
  - On Ali-CCP, KD-0.3 improves serving pCTCVR/pCVR **ROC-AUC by +2.1%/+1.6%** and **PR-AUC by +9.9%/+8.8%** over ESMM (with gains retained under negative downsampling).

### 11. Slim Foundation Models for Latency-Critical Recommendation Serving
- **Authors:** Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.11013](https://arxiv.org/abs/2611.11013)
- **Subjects:** (as indexed on arXiv search; CTR/recommendation serving)
- **Abstract:** Click-through rate (CTR) prediction is a core component of recommendation and advertising systems. Large language models (LLMs) offer rich semantic priors that improve prediction quality, particularly in cold-start and long-tail settings. Injecting a full-scale LLM into a CTR pipeline is, however, prohibitively expensive at inference time: existing LLM-enhanced CTR methods avoid this cost by caching LLM outputs offline rather than serving the LLM online. We propose a resource-efficient pipeline, SlimFM, that makes online LLM-based semantic modeling practical: (1) dependency-aware structured pruning compresses LLaMA3-8B by 44% to a 4.5B-parameter backbone; (2) LoRA-based field-aware fine-tuning trains the pruned model to produce discriminative field-level semantic embeddings from lightweight textual prompts; (3) a semantic-guided fusion module injects these embeddings into the feature interactions of a conventional CTR model. Across four datasets and six CTR backbones, SlimFM retains over 99% of uncompressed-model accuracy while reducing inference latency by up to 3.4x relative to existing LLM-enhanced baselines.
- **Key innovations:**
  - **SlimFM** enables **online** LLM-based semantic modeling for CTR (instead of offline-cached LLM outputs) under latency-critical serving constraints.
  - Pipeline: **dependency-aware structured pruning** (LLaMA3-8B → 4.5B), **LoRA field-aware fine-tuning** for field-level semantic embeddings, and **semantic-guided fusion** into conventional CTR feature interactions.
  - Retains **>99%** of uncompressed-model accuracy across 4 datasets/6 CTR backbones while reducing inference latency by up to **3.4×** vs LLM-enhanced baselines.

---

## Sequential / Time-Series Modeling

### 12. Time Flies When You Parallelise: Pareto-efficient Time Series Foundation Models with Linear Recurrences
- **Authors:** Torben Berndt, Lingyi Yang, Federico Nardi, Yi Heng Lim, AJ Shears, Benjamin Walker
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.16934](https://arxiv.org/abs/2611.16934) (submitted 13 Nov 2026)
- **Subjects:** Machine Learning (cs.LG)
- **Abstract:** Time series foundation models have demonstrated strong zero-shot forecasting performance, but computational efficiency remains a central architectural challenge. Temporal self-attention incurs quadratic cost in the number of temporal tokens, while nonlinear recurrent state transitions restrict parallel computation along the temporal dimension. We introduce ci-proto, a family of time series foundation models based on Mamba-3, whose linear state recurrences support chunk-wise parallel-in-time computation during training, and inference costs that scale linearly with sequence length. The architecture alternates recurrent temporal processing with cross-variate attention, supporting multivariate probabilistic forecasting with past-only and future-known covariates. Across fev-bench's 100 forecasting tasks, ci-proto XL sets a new state of the art among time series foundation models. The five ci-proto variants also make up the entire Pareto frontier for mean scaled quantile loss and mean absolute scaled error against both parameter count and median runtime.
- **Key innovations:**
  - **ci-proto** family (Mamba-3-based linear-recurrence TSFMs) enables **chunk-wise parallel-in-time training** and **linear-time inference** versus quadratic temporal attention / nonlinear RNN constraints.
  - Hybrid architecture alternates **recurrent temporal processing** with **cross-variate attention**, supporting multivariate probabilistic forecasting with past-only and future-known covariates.
  - Sets SOTA on **fev-bench (100 tasks)** with ci-proto XL; all five variants form the **Pareto frontier** for accuracy vs parameter count and median runtime.

---

## Games

### 13. Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games
- **Authors:** Jens Lehmann
- **Institution/Company:** Not specified on arXiv abstract page
- **arXiv:** [arXiv:2611.16981](https://arxiv.org/abs/2611.16981) (submitted 13 Nov 2026)
- **Subjects:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Abstract:** Weight-space programming (WSP) uses language models to construct neural network weights without training. We test whether known game mechanics can be compiled into compact agents that generalise to held-out levels, renderings and start states within a game family. Writers receive simulator source with held-out level data removed for 20 privately authored, unpublished ARC-AGI-3-style game families. With a fixed 57k-parameter recurrent architecture, the strongest writer reaches 56% held-out-level success with feedback, while the four main writers' Python players reach 97-100%. An exploratory free-architecture condition reaches 68-90%. Learning from support-level examples transfers much less well, but these learners lack the source information given to writers. Written networks have a program-like structure: 93% of parameters are zero, and 90% of the rest are small integers or powers of two. NumPy players under comparable computation caps reach 91%, versus the networks' 79%. Training the strongest writer's architectures from scratch yields about 1% success within our budget. Written fixed-network weights are fragile, and standard PPO removes most of their success. Prompts for noise robustness increase tolerance by about four orders of magnitude for two of three writers, but PPO makes larger updates and still removes most success. These results demonstrate rule-to-network compilation in this setting, while showing limited benefits over Python programs and no successful combination with the tested PPO fine-tuning.
- **Key innovations:**
  - Studies **weight-space programming (WSP)** for compiling known game rules/mechanics into compact neural agents that generalize across held-out levels, renderings, and start states (20 unpublished ARC-AGI-3-style game families).
  - Finds written networks exhibit **program-like sparsity/structure** (93% zeros; most remaining weights small integers/powers of two) and reach 56% held-out success (fixed 57k-param recurrent) with feedback, while Python/NumPy baselines remain strong.
  - Characterizes limitations: **fragility of written weights**, poor transfer from example-only learning in this setup, and **PPO fine-tuning largely erases compiled success** despite robustness-oriented prompting.

---

## Notes
- **Institution/company:** arXiv abstract pages often omit structured affiliation metadata; this report lists affiliations only when clearly available on-page and otherwise marks them as not specified.
- **Recency:** All listed papers are recent arXiv submissions (primarily mid-November 2026 IDs in the 2611.xxxxx range), selected to cover the requested domains.
- **"Key innovations"** are concise syntheses derived from each paper's abstract. For definitive claims and experimental details, consult the linked arXiv pages/PDFs.
