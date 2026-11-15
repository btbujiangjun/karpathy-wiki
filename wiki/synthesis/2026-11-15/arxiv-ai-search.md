# arXiv AI Search Report (2026-11-15)

## Scope and method
- **Date:** 2026-11-15
- **Topics covered:** AI, LLMs, recommendation systems, advertising/CTR prediction, sequential modeling, and AI for games/agents.
- **Sources:** arXiv API queries and selected abstract pages from `cs.IR`, `cs.AI`, `cs.CL`, `cs.LG`, plus targeted searches for recommendation/CTR/advertising/sequential modeling, LLMs, and game agents.
- **Selection window:** Recent submissions from 2026-11-09 to 2026-11-12 (as returned by arXiv at query time).
- **Notes:** "Institution/Company" is listed when explicitly stated on arXiv; otherwise marked as *Not explicitly listed on arXiv* (inferred affiliations from author names are not assumed). Abstracts are summarized from arXiv metadata/pages. Key innovations are distilled from the stated contributions.

---

## 1) TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
- **arXiv:** [2611.12180](https://arxiv.org/abs/2611.12180) (cs.IR/cs.AI/cs.CL, submitted 2026-11-09)
- **Authors:** Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Institution/Company:** Taobao Shangou / Alibaba ecosystem implied by title and deployment context; *affiliations not explicitly listed on arXiv*
- **Abstract:** Proposes TS-GEAR, a generative retrieval framework for on-demand delivery advertising where candidates outside a user's delivery range are invalid. It addresses three challenges: (1) geographic reachability is usually enforced via non-differentiable post-generation filtering, (2) user preferences vary across regions and queries making naive history aggregation biased, and (3) autoregressive training lacks set-level signals to reduce redundant candidates. TS-GEAR introduces Geo-Semantic IDs that split identifiers into geographic prefixes and semantic suffixes, Query-Geo Target Attention that conditions behavior aggregation on real-time query/location while encoding behavior locations in keys, and GMPO (Group Marginal Policy Optimization) to incorporate deduplicated group rewards/marginal advantages within GRPO-style optimization. Deployed with a lightweight 0.1B backbone, it serves over 150 million queries/day in Taobao Shangou search advertising.
- **Key innovations:**
  - **Geo-Semantic ID design** makes geographic reachability a learnable/predictable target instead of a post-hoc hard filter.
  - **Query-Geo Target Attention** jointly conditions on current query and location and injects each historical behavior's location into attention keys for better regional/query-aware interest modeling.
  - **GMPO set-aware optimization** uses deduplicated group rewards and marginal advantages to discourage near-duplicate retrievals without separate diversity objectives.
  - Demonstrated large-scale production impact (reported gains: +3.8% ad impressions, +4.2% ad revenue).

## 2) KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
- **arXiv:** [2611.16795](https://arxiv.org/abs/2611.16795) (cs.IR, submitted 2026-11-12; accepted to NeurIPS 2026 per arXiv comment)
- **Authors:** Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Institution/Company:** *Not explicitly listed on arXiv* (industry-scale dataset sourced from Kuaishou as stated in abstract)
- **Abstract:** Introduces KuaiRecV2, a benchmark aimed at closing the offline-online evaluation gap in recommender systems, especially for large-model and generative recommendation settings. The benchmark targets three challenges: large-scale continual learning under dynamic item pools/distribution shifts, combinatorial diversity balancing accuracy and diversity at token/item levels, and multi-task reward balancing for generative models. It provides a large-scale industrial dataset with million-scale multi-modal item information, long-term interaction records over 30 days, a dynamic candidate pool, and a unified evaluation rubric covering retrieval accuracy, diversity, and multi-task performance.
- **Key innovations:**
  - **Industrial-scale continual-learning benchmark** with dynamic candidate pools and long-horizon interaction data for realistic recsys evaluation.
  - **Unified multi-objective rubric** requiring simultaneous improvements in accuracy, diversity, and multi-task metrics.
  - **Multi-modal, million-scale item corpus** enabling evaluation of modern semantic/generative recommendation methods under practical constraints.
  - Code released: `https://github.com/cxli2333/KuaiRecV2`.

## 3) TriGen: A Generative Paradigm for Trigger-Induced Recommendation
- **arXiv:** [2611.16395](https://arxiv.org/abs/2611.16395) (cs.IR, submitted 2026-11-12)
- **Authors:** Muyu Zou, Haibo Xing, Shunye Tang, Liyan Tie, Lingyu Mu, Yandong Wang, Jinxin Hu
- **Institution/Company:** *Not explicitly listed on arXiv*
- **Abstract:** Addresses Trigger-Induced Recommendation (TIR), where a user action (e.g., click) immediately triggers a follow-up feed requiring alignment with instant intent while preserving long-term preferences. Existing discriminative TIR methods cannot guide token-level generation, and generative recommenders often lack mechanisms to reconcile this tension. TriGen proposes a tailored generative paradigm featuring calibrated tail injection to re-encode local history, dynamic gating to arbitrate persistent tastes vs immediate impulses, and position-specific transformations for level-aware trigger guidance during decoding. The method shows offline gains and online A/B improvements across six country markets, leading to production deployment.
- **Key innovations:**
  - **Calibrated tail injection** to better encode recent/local interaction context relevant to the trigger.
  - **Dynamic gating between long-term and immediate intent** for controllable trigger-aware generation.
  - **Position-specific decoding transformations** to sustain trigger guidance across generation steps.
  - Validated by multi-market online A/B tests and full production deployment.

## 4) From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction
- **arXiv:** [2611.16159](https://arxiv.org/abs/2611.16159) (cs.IR, submitted 2026-11-12)
- **Authors:** Jiaqi Wang, Hanchen Yang, Hengyu Zhang, Hongxu Ma, Wenqi Rao, Hongyang Wang, Zhongbo Sun, Renliang Qian, Weixin Chen, Wengen Li, Jihong Guan, Shuigeng Zhou, Qingpeng Cai, Peng Jiang, Hong Cheng
- **Institution/Company:** *Not explicitly listed on arXiv*
- **Abstract:** Studies user behavior trajectory prediction (UBTP), which forecasts sequences of future interactions from user histories. The authors argue that generative recommendation methods based on autoregressive semantic-ID decoding couple token generation with behavior transitions, ignore predictive uncertainty, and suffer train-inference mismatch from teacher forcing. They propose TraGR, a behavior-aware generative framework that predicts SID tokens in parallel within each interaction, models behavioral transitions via recurrent state updates, provides probability feedback combining selected and alternative behaviors, and uses relation-aware trajectory learning with collaborative transition signals and later credit assignment on model-generated trajectories.
- **Key innovations:**
  - **Behavior-level generation architecture**: parallel SID prediction within interactions plus recurrent cross-interaction state transitions.
  - **Probability-weighted feedback** that preserves uncertainty/alternatives to guide subsequent predictions.
  - **Relation-aware trajectory learning** incorporating collaborative transition signals and credit assignment on generated trajectories to reduce exposure bias.
  - Consistent gains across four datasets and multiple prediction horizons; code available at `https://github.com/CalmaQi/GR4UBT`.

## 5) Serving-Aligned Entire-Space Conversion Modeling via Click-Through Rate Knowledge Distillation
- **arXiv:** [2611.15137](https://arxiv.org/abs/2611.15137) (cs.LG, submitted 2026-11-11)
- **Authors:** Pavel Dolin, Xun Zou, Jiatian Wu, Deguang Kong
- **Institution/Company:** *Not explicitly listed on arXiv*
- **Abstract:** Targets ranking systems that use predicted click-through conversion rate (pCTCVR = pCTR × pCVR). In ESMM-style models, the auxiliary pCTR tower used during joint training may differ from the separately trained pCTR model used at serving time, causing training-serving mismatch in pCTCVR. The paper proposes distilling logged serving pCTR scores into ESMM's auxiliary pCTR tower (KD-α) to improve alignment. Experiments on Ali-CCP show that KD-0.3 improves serving pCTCVR and pCVR metrics (ROC-AUC and PR-AUC), with additional evaluation under negative downsampling.
- **Key innovations:**
  - **Serving-log CTR knowledge distillation** into the auxiliary ESMM tower to align offline training with online ranking composition.
  - **Simple, deployable alignment mechanism** controlled by a hard-label/distillation loss weight (α) without changing ESMM's core structure.
  - Demonstrates improvements in both **pCTCVR alignment and pCVR quality**, including robustness checks with negative downsampling.

## 6) When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence
- **arXiv:** [2611.14938](https://arxiv.org/abs/2611.14938) (econ.GN/cs.IR/cs.LG, submitted 2026-11-11)
- **Authors:** Pan Li, Alexander Tuzhilin
- **Institution/Company:** *Not explicitly listed on arXiv* (large-scale online experiment conducted at a major video-streaming platform in Asia, per abstract)
- **Abstract:** Formalizes the information-gap theory of curiosity into axioms and derives a computational measure of the curiosity evoked by a recommended item. The measure is validated via survey studies against self-reported curiosity and alternative proxies, then integrated into a curiosity-aware recommender system. Offline experiments on three real-world datasets and a large-scale online A/B test on a major Asian video-streaming platform show improvements in engagement metrics (CTR, video views, time spent) over the production system.
- **Key innovations:**
  - **Axiomatic, computable curiosity measure** grounded in information-gap theory for recommender systems.
  - **Curiosity-aware utility/ranking objective** that complements relevance to reduce filter-bubble effects and sustain engagement.
  - **End-to-end validation pipeline** from theory to survey validation, offline gains, and deployed online A/B impact.

## 7) AgentSSL: Can MLE Agents Leverage Unlabeled Data?
- **arXiv:** [2611.17323](https://arxiv.org/abs/2611.17323) (cs.AI/cs.LG, submitted 2026-11-12)
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **Institution/Company:** *Not explicitly listed on arXiv*
- **Abstract:** Frames semi-supervised learning (SSL) for machine-learning engineering (MLE) agents as a program search problem under scarce labels and abundant unlabeled data. The study finds agents can synthesize code that combines/adapts SSL techniques and outperform strong human-engineered baselines in many settings, but identifies program selection under weak feedback as a major bottleneck. The authors introduce ProgramSelectBench (16,977 agent-generated and human-engineered SSL programs) to study selection methods, and evaluate AgentSSL on real-world ecology detection tasks.
- **Key innovations:**
  - **Agentic SSL as program search**, extending MLE-agent evaluation beyond fully supervised regimes.
  - **ProgramSelectBench** for systematic study of unsupervised/active program selection at scale.
  - Empirical insight that **selection/feedback, not just generation**, is a key limitation for agent-driven ML pipeline design.

## 8) Goal Encoding in LLMs
- **arXiv:** [2611.17297](https://arxiv.org/abs/2611.17297) (cs.CL/cs.AI/cs.LG, submitted 2026-11-12)
- **Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
- **Institution/Company:** *Not explicitly listed on arXiv*
- **Abstract:** Investigates whether LLMs encode internal goal representations that precede and guide actions across multiple realizations. In a multi-subtask coding setting, the authors localize next-subgoal encodings in sparse attention-head outputs, decode them into natural-language descriptions of intended actions, and show causal/plastic properties (including transfer across environments/languages). They propose a non-recurrent goal-seeking (NRGS) account in which models repeatedly re-read goals from context and compare progress, and test this with causal interventions.
- **Key innovations:**
  - **Localization and causal analysis of goal/subgoal representations** in transformer attention heads.
  - Evidence of **representational plasticity**: transplanted goal encodings trigger equivalent operations in different execution contexts.
  - **NRGS interpretability account** explaining sustained goal pursuit without explicit recurrent state, supported by intervention experiments.
  - Project resources: `https://goals.baulab.info/`.

## 9) Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games
- **arXiv:** [2611.16981](https://arxiv.org/abs/2611.16981) (cs.AI/cs.LG, submitted 2026-11-12)
- **Authors:** Jens Lehmann
- **Institution/Company:** *Not explicitly listed on arXiv*
- **Abstract:** Studies weight-space programming (WSP), where language models construct neural network weights directly (without conventional training) to compile known game mechanics into compact agents. Evaluated on 20 privately authored ARC-AGI-3-style game families, the work tests generalization to held-out levels/renderings/start states. With a fixed 57k-parameter recurrent architecture and feedback, the strongest writer reaches 56% held-out-level success, while Python players reach much higher success; exploratory free architectures perform better but remain below programmatic baselines in some settings. The resulting networks are sparse and program-like, but fragile and difficult to improve with standard PPO fine-tuning.
- **Key innovations:**
  - **Rule-to-weight compilation paradigm (WSP)** for building neural game agents from known mechanics without gradient training.
  - Analysis of **generalization, sparsity/structure, and brittleness** of compiled networks versus symbolic/Python implementations.
  - Findings on **robustness prompts and RL fine-tuning limits** (e.g., PPO can erase compiled behavior), informing future neuro-symbolic/game-agent design.

## 10) Stack more levels: how to get general and human-like Mario playing
- **arXiv:** [2611.16175](https://arxiv.org/abs/2611.16175) (cs.AI, submitted 2026-11-12)
- **Authors:** Shinichi Arimura, Yuchen Li, Julian Togelius
- **Institution/Company:** *Not explicitly listed on arXiv*
- **Abstract:** Investigates whether model-free RL can reliably win unseen Super Mario Bros. levels. PPO agents are trained on increasingly large sets of procedurally generated levels and evaluated on 1,000 held-out levels, showing that broader training diversity generally improves generalization. Competent policies are then shaped into runner/killer/collector archetypes and fine-tuned with Diffusion-Reward Adversarial Imitation Learning (DRAIL) using human demonstrations, improving action-level human-likeness while largely preserving PPO-induced persona behavior.
- **Key innovations:**
  - Empirical evidence that **scaling training-level diversity** improves generalization in classic platformer RL.
  - **Persona shaping + imitation fine-tuning pipeline** (PPO archetypes followed by DRAIL) to balance competence, style, and human-likeness.
  - Provides practical insights for **general and human-like game-playing agents** in PCG-based evaluation settings.

---

## Cross-topic takeaways
- **Advertising/CTR & recommendation systems:** Production-oriented generative retrieval and conversion modeling (TS-GEAR, TriGen, KD-aligned ESMM) emphasize serving constraints, trigger intent, and train-serve alignment alongside ranking quality.
- **Sequential modeling:** TraGR reframes trajectory prediction around behavior-level transitions and uncertainty-aware feedback, complementing trigger-aware generative recommendation.
- **LLMs & AI foundations:** Recent LLM work spans mechanistic interpretability (goal encoding) and agentic/automated ML pipelines (AgentSSL), highlighting both capability gains and evaluation/selection bottlenecks.
- **Games/agents:** Results in Mario and ARC-style game families show progress in generalization and rule compilation, but also expose robustness and fine-tuning challenges for learned/compiled agents.
