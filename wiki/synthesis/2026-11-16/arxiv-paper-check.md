---
title: "arXiv Paper Check — AI & CTR (2026-11-16)"
type: synthesis
created: 2026-11-16
updated: 2026-11-16
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=40
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR+OR+all:%22click-through+rate%22+OR+all:CTR+AND+all:recommendation&sortBy=submittedDate&sortOrder=descending&max_results=30
  - https://rss.arxiv.org/rss/cs.AI
  - https://rss.arxiv.org/rss/cs.IR
  - https://rss.arxiv.org/rss/cs.LG
  - https://rss.arxiv.org/rss/cs.CL
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - advertising
  - retrieval
  - agents
  - llm
  - generative-recommendation
  - daily-digest
---

# arXiv Paper Check — AI & CTR (2026-11-16)

> **Window note:** Checked on **2026-11-16** (Mon). arXiv RSS feeds for cs.AI/cs.IR/cs.LG/cs.CL showed no fresh announcement items in the immediate 24-hour window at query time (weekend/skip-day timing), and API queries sorted by submission date surfaced the latest visible batch primarily from **2026-11-12–2026-11-13**. This report curates the most interesting **recent** papers relevant to **AI** and **CTR / click-through rate** (including recommendation, advertising, ranking, and retrieval systems where CTR or engagement objectives are central) from that latest available window. All results and metrics below are **author-reported** unless noted.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| AI / Multimodal | **Unbundling Multimodal Vision Encoding** (2611.17334) | Controlled study disentangles visual prior, dedicated vision capacity, and pre-fusion placement; finds dedicated jointly trained vision capacity matters most. |
| AI / LLM Architecture Research | **ArchSpace** (2611.17332) | Public platform for recording/reviewing/referencing LLM architecture experiments with scaling-law-guided evaluation. |
| AI / Agents / SSL | **AgentSSL** (2611.17323) | Studies MLE agents in semi-supervised regimes; strong gains in some settings but program selection under weak feedback is a major bottleneck. |
| AI / Coding Agents / Memory | **CoReMem** (2611.17316) | Cost-internalizing memory for successive coding tasks via prospective valuation and provenance-gated credit. |
| AI / Diffusion LMs | **Learning When Diffusion Language Models Should Regenerate** (2611.17320) | DiVR verifier decides when/what to regenerate, improving reasoning accuracy over fine-tuned generators with controlled compute overhead. |
| AI / Reasoning / Energy Models | **CRAM** (2611.17309) | Learned Hopfield-Tank-style energy solves Sudoku-Extreme/Maze-Unique extremely quickly with far fewer FLOPs than looped baselines. |
| AI / LLM Interpretability | **Goal Encoding in LLMs** (2611.17297) | Localizes causal, transferable next-subgoal representations in sparse attention heads and proposes a non-recurrent goal-seeking account. |
| CTR / Recsys Benchmark | **KuaiRecV2** (2611.16795) | Large-scale industrial benchmark for continual learning, accuracy-diversity trade-offs, and multi-task generative recommendation. |
| Ads / Triggered Recommendation | **TriGen** (2611.16395) | Generative trigger-induced recommendation balancing instant intent and long-term preference, with reported production deployment. |
| Generative Retrieval / Long-tail | **ReSID** (2611.16404) | Improves long-tail reachability in generative recommendation via parallel SIDs, debiased semantic beam search, and partial SID matching. |

## 1) AI

### Unbundling Multimodal Vision Encoding
- **arXiv:** [2611.17334](https://arxiv.org/abs/2611.17334) (cs.CV, cs.LG; submitted 2026-11-12)
- **Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu
- **Key contributions:**
  - Disentangles three vision-encoding choices in multimodal LMs: upstream visual prior, dedicated vision capacity, and pre-fusion placement of that capacity.
  - Uses a controlled from-scratch pretraining framework at matched lifetime compute on VQA and language benchmarks.
  - Finds visual priors are not necessary (jointly trained encoder can match pretrained), but dedicated vision capacity matters; in-fusion vision modules in early backbone layers can perform comparably to pre-fusion encoders and reduce time to first token.
- **Why interesting:** Provides actionable architectural guidance for multimodal model design beyond anecdotal comparisons across differently trained systems.

### ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
- **arXiv:** [2611.17332](https://arxiv.org/abs/2611.17332) (cs.CL, cs.LG; submitted 2026-11-12)
- **Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
- **Key contributions:**
  - Proposes **ArchSpace**, a public platform to record architecture proposals with experiments/reasoning, enable community review, and make validated ideas referenceable.
  - Uses scaling-law-based prediction from smaller experiments to evaluate ideas before costly large-scale training.
  - Provides initial references including baselines, fitted scaling laws, and a reusable training recipe to bootstrap comparable architecture research.
- **Why interesting:** Targets reproducibility and cumulative progress in LLM architecture work, where negative results and context are often underreported.

### AgentSSL: Can MLE Agents Leverage Unlabeled Data?
- **arXiv:** [2611.17323](https://arxiv.org/abs/2611.17323) (cs.AI, cs.LG; submitted 2026-11-12)
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **Key contributions:**
  - Introduces **Agentic Semi-Supervised Learning (AgentSSL)**, framing SSL pipeline design for MLE agents as program search with scarce labels and abundant unlabeled data.
  - Reports that agents can synthesize/adapt SSL techniques and exceed strong human-engineered baselines in 8/12 settings (up to **+21.8%**, author-reported), while **program selection** under weak feedback remains a critical bottleneck (drops up to **47%**).
  - Releases **ProgramSelectBench** (16,977 agent-generated and human-engineered SSL programs) and evaluates on real-world ecology detection tasks.
- **Why interesting:** Highlights a practical gap between generating candidate ML pipelines and reliably selecting them when supervision is weak.

### CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
- **arXiv:** [2611.17316](https://arxiv.org/abs/2611.17316) (cs.AI, cs.CL, cs.SE; submitted 2026-11-12)
- **Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, Heng Chang, Fei Fei, David van Dijk, Rex Ying
- **Affiliations (from arXiv metadata):** Yale University; Tsinghua University; Goodvision AI (as listed per author entries)
- **Key contributions:**
  - Proposes **CoReMem** for successive repository tasks where future tasks are unknown and memory has read/write costs.
  - Uses **prospective segment valuation** to compare runs with/without trajectory segments, building compact anchor-based memories (repo locations and executable checks).
  - Trains actor adaptation with on-policy memory-value estimation and **provenance-gated value credit**.
- **Reported results:** On ChainSWE, 27B actor resolve rate improves from **21.0% → 25.7%** with **17% fewer steps** and **11% fewer cache-aware tokens** (author-reported).

### Learning When Diffusion Language Models Should Regenerate (DiVR)
- **arXiv:** [2611.17320](https://arxiv.org/abs/2611.17320) (cs.CL; submitted 2026-11-12)
- **Authors:** Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, Minsik Seol, Jungwoo Lee
- **Key contributions:**
  - Diagnoses that diffusion LM hidden states contain error information not reliably exposed by token confidence, and isolated remasking often reproduces errors when surrounding context is fixed.
  - Introduces **DiVR**, a verifier trained on final correctness of the model's own trajectories to decide when to regenerate a block and which alternative to retain (generator unchanged).
- **Reported results:** On five reasoning benchmarks with LLaDA-8B-Base, average accuracy rises from **35.3% → 43.4%** at **1.9–3.5×** greedy-decoding cost, outperforming search baselines using **3.8–7.4×** cost; complements SFT/RL and generalizes to other generators including Dream.

### Classical Energies Learn to Reason 1,000x Faster than Looped Models (CRAM)
- **arXiv:** [2611.17309](https://arxiv.org/abs/2611.17309) (cs.AI, cs.LG; submitted 2026-11-12)
- **Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **Key contributions:**
  - Presents **CRAM**, a learned Hopfield & Tank-style energy approach for reasoning puzzles, emphasizing interpretability, adaptive compute, and training without differentiating through a solver.
  - Targets efficiency and stability issues of looped reasoning models.
- **Reported results:** Solves **99.996%** of Sudoku-Extreme and **100%** of Maze-Unique after **42 ms** and **132 ms** of training on one GPU (≥ **1,000×** faster than looped models on these tasks, author-reported), and matches highest looped-model accuracy on Sudoku-Extreme with at least **282× fewer inference FLOPs**.

### Goal Encoding in LLMs
- **arXiv:** [2611.17297](https://arxiv.org/abs/2611.17297) (cs.CL, cs.AI, cs.LG; submitted 2026-11-12)
- **Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
- **Key contributions:**
  - Localizes next-subgoal encodings in outputs of a **sparse set of attention heads** in multi-subtask coding settings and decodes them into natural-language intended actions.
  - Demonstrates causal and plastic encodings (transplanting can trigger equivalent operations in different environments/languages).
  - Proposes and tests a **non-recurrent goal-seeking (NRGS)** account via targeted interventions.
- **Resources:** Project page https://goals.baulab.info/

### LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds
- **arXiv:** [2611.17267](https://arxiv.org/abs/2611.17267) (cs.AI; submitted 2026-11-12)
- **Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, Shengqiong Wu, Hao Fei, Mong-Li Lee, Wynne Hsu
- **Key contributions:**
  - Introduces **GeoWorld**, a controllable evolving geographic environment platform, and **LiveGeo**, a benchmark for agent decision-making under changing world states.
  - Requires agents to acquire task-relevant evidence, verify validity of prior evidence, and revise plans when the environment evolves.
- **Why interesting:** Moves geographic/decision-making evaluation beyond static snapshots toward reliability under temporal change.

## 2) CTR, Recommendation, Advertising & Retrieval

### KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
- **arXiv:** [2611.16795](https://arxiv.org/abs/2611.16795) (cs.IR; submitted 2026-11-12; accepted to NeurIPS 2026 per arXiv comment)
- **Authors:** Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Key contributions:**
  - Industrial-scale benchmark (Kuaishou data) targeting **continual learning** under dynamic item pools/distribution shifts, **accuracy-diversity** trade-offs, and **multi-task reward balancing** for generative recommendation.
  - Provides million-scale multi-modal items, 30-day interactions, dynamic candidate pool, and a unified evaluation rubric across retrieval accuracy/diversity/multi-task performance.
  - Code: https://github.com/cxli2333/KuaiRecV2
- **CTR/relevance:** Addresses practical gaps between offline and online recommendation performance in settings where click/engagement and multi-objective rewards must be balanced over time.

### TriGen: A Generative Paradigm for Trigger-Induced Recommendation
- **arXiv:** [2611.16395](https://arxiv.org/abs/2611.16395) (cs.IR; submitted 2026-11-12)
- **Authors:** Muyu Zou, Haibo Xing, Shunye Tang, Liyan Tie, Lingyu Mu, Yandong Wang, Jinxin Hu
- **Key contributions:**
  - Targets **Trigger-Induced Recommendation (TIR)**, where a user action triggers an immediate feed requiring alignment with instant intent while preserving long-term preferences.
  - Introduces **calibrated tail injection**, **dynamic gating** (persistent tastes vs immediate impulses), and **position-specific transformations** for level-aware trigger guidance during generation.
- **Reported results:** Offline gains and online A/B improvements across six country markets with full production deployment (author-reported).
- **CTR/relevance:** Directly optimizes post-trigger feed relevance, a high-impact setting for click-through and downstream conversion.

### ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability
- **arXiv:** [2611.16404](https://arxiv.org/abs/2611.16404) (cs.IR; submitted 2026-11-12)
- **Authors:** Muyu Zou, Shunye Tang, Yi Xu, Haibo Xing, Yandong Wang, Lingyu Mu, Jinxin Hu
- **Key contributions:**
  - Studies long-tail **reachability** across SID construction, decoding, and matching in generative recommendation.
  - Proposes **ReSID**: long parallel SIDs with popularity-debiased and user-semantic-aware beam search plus **partial SID matching** to recover tail candidates.
- **Reported results:** SOTA long-tail retrieval with competitive overall accuracy, lower latency/higher throughput under narrow beams, and production deployment gains (author-reported). Code: https://github.com/Gabriel-reina/ReSID
- **CTR/relevance:** Improving tail retrieval can expand effective candidate pools and engagement opportunities beyond head items.

### From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction (TraGR)
- **arXiv:** [2611.16159](https://arxiv.org/abs/2611.16159) (cs.IR; submitted 2026-11-12)
- **Authors:** Jiaqi Wang, Hanchen Yang, Hengyu Zhang, Hongxu Ma, Wenqi Rao, Hongyang Wang, Zhongbo Sun, Renliang Qian, Weixin Chen, Wengen Li, Jihong Guan, Shuigeng Zhou, Qingpeng Cai, Peng Jiang, Hong Cheng
- **Key contributions:**
  - Reframes generative recommendation for **user behavior trajectory prediction (UBTP)** around behavior-level transitions rather than purely serial token decoding.
  - Predicts SID tokens in parallel within each interaction, models transitions via recurrent state updates, and uses probability-weighted feedback plus relation-aware trajectory learning on model-generated rollouts.
- **Reported results:** Consistent gains over SOTA baselines on four public datasets across prediction horizons (author-reported). Code: https://github.com/CalmaQi/GR4UBT
- **CTR/relevance:** Better trajectory prediction can improve next-interaction/click modeling quality in sequential recommendation pipelines.

## Cross-cutting observations

1. **AI systems work is emphasizing selection, memory cost, and reliability.** AgentSSL and CoReMem show that generating solutions/memories is not enough—selection quality, provenance, and cost-aware retention materially affect outcomes.
2. **Interpretability and controllability are moving toward actionable mechanisms.** Goal encoding in LLMs and DiVR's regenerate decisions both aim to identify/use internal signals rather than treating models as opaque generators.
3. **Recommendation/CTR research continues to close offline-online gaps.** KuaiRecV2's dynamic/continual evaluation and production-oriented generative methods (TriGen, ReSID) reflect pressure to align modeling, serving constraints, and long-tail/triggered engagement behavior.

## Caveats

- **Timing:** Strict "last 24 hours" coverage was limited by arXiv announcement timing (RSS skip days/no fresh items; latest visible API submissions mostly 2026-11-12–13 at query time). This is a curated recent-window check, not an exhaustive announcement digest.
- **Evidence level:** Abstract/metadata-level synthesis; deployment claims and metrics are **author-reported** and not independently reproduced here.
- **Affiliations:** Structured affiliations are not always present in arXiv metadata; included only when explicitly indicated.
- **Scope:** CTR is treated broadly to include recommendation, advertising, ranking, retrieval, and generative systems where click-through/engagement or closely related serving objectives are central.
