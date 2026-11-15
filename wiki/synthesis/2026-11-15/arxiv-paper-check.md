---
title: "arXiv Paper Check — AI & CTR (2026-11-15)"
type: synthesis
created: 2026-11-15
updated: 2026-11-15
sources:
  - https://export.arxiv.org/api/query
  - https://rss.arxiv.org/rss/cs.AI
  - https://rss.arxiv.org/rss/cs.IR
  - https://rss.arxiv.org/rss/cs.LG
tags:
  - arxiv
  - daily-check
  - ai
  - llm
  - agents
  - ctr
  - recommendation
  - advertising
  - sequential-modeling
  - generative-recommendation
---

# arXiv Paper Check — AI & CTR (2026-11-15)

> **Window note:** Checked on **2026-11-15**. arXiv RSS feeds for cs.AI/cs.IR/cs.LG showed no fresh announcement items in the immediate 24-hour window at query time (weekend/skip-day timing), and API queries for recent submissions surfaced primarily **2026-11-11–2026-11-12** papers as the latest available batch. This report curates the most interesting **recent** papers relevant to **AI** and **CTR / click-through rate** (and closely related recommendation, advertising, and ranking) from that latest available window. All results and metrics below are **author-reported** unless noted.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| AI / Agents / SSL | **AgentSSL** (2611.17323) | Frames semi-supervised learning for MLE agents as program search; strong gains in low-label regimes but exposes program selection as a bottleneck. |
| AI / Coding Agents / Memory | **CoReMem** (2611.17316) | Cost-internalizing memory for successive coding tasks with prospective valuation and provenance-gated credit. |
| AI / LLM Interpretability | **Goal Encoding in LLMs** (2611.17297) | Localizes causal, transferable next-subgoal representations in sparse attention heads. |
| AI / RAG / Attribution | **Cited but Unused** (2611.17161) | Shows RAG citations can misstate provenance; counterfactual substitution finds memory-derived claims despite citations. |
| AI / Long-horizon Agents | **Actor, Judge, or Teacher?** (2611.17167) | A poor-acting decision model can still teach well; trajectory-level judging improves policy learning. |
| CTR / Conversion Modeling | **Serving-Aligned ESMM via CTR KD** (2611.15137) | Distills logged serving pCTR into ESMM auxiliary tower to reduce train-serve pCTCVR mismatch. |
| CTR / Recsys Benchmark | **KuaiRecV2** (2611.16795) | Industrial-scale continual-learning benchmark for diversified, multi-task recommendation (NeurIPS 2026). |
| Ads / Triggered Recommendation | **TriGen** (2611.16395) | Generative trigger-induced recommendation balancing instant intent and long-term preference; production deployment reported. |
| Sequential / Trajectory Prediction | **TraGR** (2611.16159) | Behavior-aware generative trajectory prediction with parallel within-interaction decoding and uncertainty-aware feedback. |
| Generative Retrieval / Long-tail | **ReSID** (2611.16404) | Improves long-tail reachability via parallel SIDs, debiased/semantic beam search, and partial SID matching. |

## 1) AI

### AgentSSL: Can MLE Agents Leverage Unlabeled Data?
- **arXiv:** [2611.17323](https://arxiv.org/abs/2611.17323) (cs.AI, cs.LG; submitted 2026-11-12)
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **Key contributions:**
  - Introduces **Agentic Semi-Supervised Learning (AgentSSL)**, casting SSL for MLE agents as a program-search problem under scarce labels and abundant unlabeled data.
  - Finds agents can synthesize/adapt SSL pipelines and exceed strong human-engineered baselines in 8/12 settings (up to +21.8%, author-reported), while **program selection** under weak feedback is a critical bottleneck (drops up to 47%).
  - Releases **ProgramSelectBench** (16,977 agent-generated and human-engineered SSL programs) and evaluates on real-world ecology detection tasks.

### CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
- **arXiv:** [2611.17316](https://arxiv.org/abs/2611.17316) (cs.AI, cs.CL, cs.SE; submitted 2026-11-12)
- **Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, Heng Chang, Fei Fei, David van Dijk, Rex Ying
- **Key contributions:**
  - Proposes **CoReMem** for successive repository tasks where future tasks are unknown and memory has read/write costs.
  - Uses **prospective segment valuation** (with/without trajectory segments on the next task) to build compact anchor-based memories (repo locations and executable checks).
  - Trains actor adaptation with on-policy memory-value estimation and **provenance-gated value credit**. On ChainSWE (author-reported): 27B resolve rate 21.0%→25.7%, with 17% fewer steps and 11% fewer cache-aware tokens.

### Goal Encoding in LLMs
- **arXiv:** [2611.17297](https://arxiv.org/abs/2611.17297) (cs.CL, cs.AI, cs.LG; submitted 2026-11-12)
- **Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
- **Key contributions:**
  - Localizes next-subgoal encodings in outputs of a **sparse set of attention heads** in multi-subtask coding settings; decodes them into natural-language intended actions.
  - Shows encodings are **causal and plastic** (transplanting can trigger equivalent operations in different environments/languages) and proposes a **non-recurrent goal-seeking (NRGS)** account supported by interventions.
  - Project: https://goals.baulab.info/

### Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation
- **arXiv:** [2611.17161](https://arxiv.org/abs/2611.17161) (cs.AI; submitted 2026-11-12)
- **Authors:** Tanzeel Abbas, Tehseen Zia, David Windridge
- **Key contributions:**
  - Measures RAG provenance via **counterfactual value substitution** (replace facts in retrieved passages and re-query) rather than trusting citations/NLI.
  - Finds a non-trivial fraction of citable claims derived from **parametric memory** (1.2%–15.7% across tested settings; higher in some conservative/substitution analyses, author-reported) with rates rising with model size in-family.
  - Shows standard NLI verification can be indistinguishable from chance and that separating "what model knew" from "what it used" remains open.

### Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents
- **arXiv:** [2611.17167](https://arxiv.org/abs/2611.17167) (cs.AI, cs.CL; submitted 2026-11-12)
- **Authors:** Haochen Liu, Qianhao Zhu, Zixuan Wang, Dingming Li, Tongbo Chen, Peng Qiu, Yingqi Qu, Weiming Lu, Jun Xiao, Yongliang Shen
- **Key contributions:**
  - Compares models as **actors, judges, and teachers** on ALFWorld/WebShop; models that act poorly can still provide useful trajectory-level judgments.
  - Shows post-hoc judging (whether actions helped) better separates useful/useless steps than success prediction during acting.
  - Uses JEV as teacher to improve Qwen2.5-1.5B over GRPO (author-reported): ALFWorld 72.8%→82.9%, WebShop 56.8%→71.4%. Code: https://github.com/ZJU-REAL/decision-agents

## 2) CTR, Advertising & Recommendation

### Serving-Aligned Entire-Space Conversion Modeling via Click-Through Rate Knowledge Distillation
- **arXiv:** [2611.15137](https://arxiv.org/abs/2611.15137) (cs.LG; submitted 2026-11-11)
- **Authors:** Pavel Dolin, Xun Zou, Jiatian Wu, Deguang Kong
- **Key contributions:**
  - Addresses **training-serving mismatch** in pCTCVR when ESMM's auxiliary pCTR tower differs from the separately trained serving pCTR model.
  - Distills **logged serving pCTR scores** into the auxiliary pCTR tower (KD-α) to align composed pCTCVR at serving time.
  - On Ali-CCP (author-reported), best KD-0.3 improves serving pCTCVR and pCVR (e.g., ROC-AUC +2.1%/+1.6%, PR-AUC +9.9%/+8.8% vs ESMM baseline), with benefits persisting under negative downsampling.

### KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
- **arXiv:** [2611.16795](https://arxiv.org/abs/2611.16795) (cs.IR; submitted 2026-11-12; accepted to NeurIPS 2026 per arXiv comment)
- **Authors:** Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Key contributions:**
  - Industrial-scale benchmark (Kuaishou data) targeting **continual learning** under dynamic item pools/distribution shifts, **accuracy-diversity** trade-offs, and **multi-task reward balancing** for generative recommendation.
  - Provides million-scale multi-modal items, 30-day interactions, dynamic candidate pool, and a unified rubric across retrieval accuracy/diversity/multi-task performance.
  - Code: https://github.com/cxli2333/KuaiRecV2

### TriGen: A Generative Paradigm for Trigger-Induced Recommendation
- **arXiv:** [2611.16395](https://arxiv.org/abs/2611.16395) (cs.IR; submitted 2026-11-12)
- **Authors:** Muyu Zou, Haibo Xing, Shunye Tang, Liyan Tie, Lingyu Mu, Yandong Wang, Jinxin Hu
- **Key contributions:**
  - Targets **Trigger-Induced Recommendation (TIR)** where a user action triggers an immediate feed requiring alignment with instant intent while preserving long-term preferences.
  - Proposes **calibrated tail injection**, **dynamic gating** (persistent tastes vs immediate impulses), and **position-specific transformations** for level-aware trigger guidance during generation.
  - Reports offline gains and online A/B improvements across six country markets with full production deployment (author-reported).

### From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction (TraGR)
- **arXiv:** [2611.16159](https://arxiv.org/abs/2611.16159) (cs.IR; submitted 2026-11-12)
- **Authors:** Jiaqi Wang, Hanchen Yang, Hengyu Zhang, Hongxu Ma, Wenqi Rao, Hongyang Wang, Zhongbo Sun, Renliang Qian, Weixin Chen, Wengen Li, Jihong Guan, Shuigeng Zhou, Qingpeng Cai, Peng Jiang, Hong Cheng
- **Key contributions:**
  - Reframes generative recommendation for **user behavior trajectory prediction (UBTP)** around behavior-level transitions rather than purely serial token decoding.
  - Predicts SID tokens in parallel within each interaction, models transitions via recurrent state updates, and uses **probability-weighted feedback** plus **relation-aware trajectory learning** on model-generated rollouts.
  - Reports consistent gains over SOTA baselines on four public datasets across prediction horizons (author-reported). Code: https://github.com/CalmaQi/GR4UBT

### ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability
- **arXiv:** [2611.16404](https://arxiv.org/abs/2611.16404) (cs.IR; submitted 2026-11-12)
- **Authors:** Muyu Zou, Shunye Tang, Yi Xu, Haibo Xing, Yandong Wang, Lingyu Mu, Jinxin Hu
- **Key contributions:**
  - Studies long-tail **reachability** across SID construction, decoding, and matching; finds parallel SIDs and partial matching can improve tail recovery, but beam pruning can block it.
  - Proposes **ReSID**: long parallel SIDs with popularity-debiased and user-semantic-aware beam search plus **partial SID matching**.
  - Reports SOTA long-tail retrieval with competitive overall accuracy, lower latency/higher throughput under narrow beams, and production deployment gains (author-reported). Code: https://github.com/Gabriel-reina/ReSID

## Cross-cutting observations

1. **Train-serve and evaluation realism remain central in CTR/recsys.** KD-based alignment (ESMM CTR KD), continual/dynamic benchmarks (KuaiRecV2), and trigger/trajectory-aware generative modeling (TriGen, TraGR, ReSID) all target gaps between offline abstractions and production behavior.
2. **Agent and LLM research is probing internals and costs, not just headline capability.** Goal-encoding localization, provenance audits in RAG, and cost-internalizing memory suggest increasing emphasis on reliability, attribution, and efficiency.
3. **"Acting" vs "judging/teaching" can diverge.** Decision-model results indicate that post-hoc evaluation signals can be more useful for learning than action-time policy quality alone.

## Caveats

- **Timing:** This is a curated check of the latest papers visible at query time, not a guarantee of exhaustive coverage of a strict 24-hour arXiv announcement window.
- **Evidence level:** Abstract/metadata-level synthesis; metrics and deployment claims are **author-reported**.
- **Affiliations:** Structured affiliations are not always present in arXiv metadata and are omitted here unless clearly stated.
- **Overlap:** CTR is treated broadly to include click/conversion modeling, ranking, retrieval, and advertising/recommendation systems where CTR-related objectives or serving constraints are central.
