---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-16 Daily Edition"
type: synthesis
created: 2026-11-16
updated: 2026-11-16
sources:
  - wiki/synthesis/2026-11-16/arxiv-paper-check.md
  - wiki/synthesis/2026-11-16/arxiv-daily.md
  - wiki/synthesis/2026-11-15/conference-digest.md
  - wiki/synthesis/2026-11-13/conference-digest.md
  - https://arxiv.org/abs/2611.17334
  - https://arxiv.org/abs/2611.17332
  - https://arxiv.org/abs/2611.17323
  - https://arxiv.org/abs/2611.17316
  - https://arxiv.org/abs/2611.17320
  - https://arxiv.org/abs/2611.17309
  - https://arxiv.org/abs/2611.17297
  - https://arxiv.org/abs/2611.16795
  - https://arxiv.org/abs/2611.16395
  - https://arxiv.org/abs/2611.16404
  - https://arxiv.org/abs/2611.16159
  - https://arxiv.org/abs/2611.12180
  - https://arxiv.org/abs/2611.11013
  - https://arxiv.org/abs/2611.16053
  - https://arxiv.org/abs/2611.16000
  - https://arxiv.org/abs/2611.16433
  - https://arxiv.org/abs/2611.17294
  - https://arxiv.org/abs/2611.15426
  - https://arxiv.org/abs/2611.15029
  - https://arxiv.org/abs/2611.15006
  - https://arxiv.org/abs/2611.14505
  - https://arxiv.org/abs/2611.14938
  - https://arxiv.org/abs/2611.15023
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, LLM, recommendation, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, multimodal, diffusion, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-16 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-16 每日版）

> Curated digest for requested venues — **ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025** — and recent arXiv work in AI, LLMs, recommendation systems, advertising, CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks. Focus organizations/labs: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top labs.

## Method, data window & limitations

- **Query date:** 2026-11-16. **Web search:** unavailable/cancelled in this run. **arXiv API/RSS:** RSS feeds (cs.AI/cs.IR/cs.LG/cs.CL) showed no fresh 24h announcement items at query time (weekend/skip-day timing) and direct API queries were constrained in this environment; latest visible submissions in related wiki checks were primarily **2026-11-12–2026-11-13**.
- **Coverage strategy:** synthesized from latest verified wiki digests (`arxiv-paper-check`/`arxiv-daily` 2026-11-16 and conference digests 2026-11-15/2026-11-13), prioritizing venue-tagged/accepted papers and industrial systems relevant to requested topics and focus companies.
- **Proceedings status:** full accepted-paper crawls/OpenReview portals for all requested conferences were not independently refreshed today (dynamic/JS pages, unavailable search, or access limits noted in prior runs). Venue sections therefore combine status snapshots, explicit arXiv venue/workshop tags, and recent relevant preprints.
- **Evidence:** all metrics/results are **author-reported** unless noted. Affiliations are given when explicitly stated in arXiv metadata/abstract text; otherwise marked **not explicitly specified in available metadata** (company/deployment context noted only when explicitly stated by authors).

---

## 1. Venue snapshot

| Venue | Status (as of 2026-11-16) | Notes for this digest |
|---|---|---|
| **ICML 2026** (Seoul, Jul 6–12, 2026) | Program/awards announced; fresh crawl not completed | No newly verified ICML-2026 main-track paper extracted today; prior digests cover flagship/award items. |
| **AAAI 2026** (Singapore, Jan 20–27, 2026) | Completed; fresh crawl not completed | No newly verified AAAI-2026 paper added today. |
| **NeurIPS 2025** (San Diego/Mexico City, Dec 2–7, 2025) | Completed | NeurIPS 2026-tagged/workshop items appearing on arXiv included below. |
| **ICLR 2026** (Rio, Apr 28–May 2, 2026) | Program/awards announced | No newly verified ICLR-2026 paper extracted today. |
| **KDD 2026** | No fresh crawl | Industrial rec/ads systems represented via recent arXiv/deployment papers (e.g. TS-GEAR). |
| **CVPR 2026** | No fresh crawl | Recent multimodal/generative vision work included as arXiv preprints. |
| **ACL 2026** | No fresh crawl | No newly verified ACL-2026 tag extracted today. |
| **EMNLP 2025** | Completed | Not re-crawled. |
| **SIGIR 2026** | Workshop signals seen recently (prior digests) | No newly verified SIGIR-2026 item added today. |
| **WWW 2026** | No fresh crawl | Gap noted. |
| **CIKM 2025** | Completed | Not re-crawled. |
| **RecSys 2025** | Completed; RecSys 2026 workshop-tagged items visible recently | DaQuaMRec/RecSys workshop context noted where relevant. |

---

## 2. NeurIPS 2026 / Workshop-tagged & Recommendation Benchmarks
### NeurIPS 2026 / 研讨会标注与推荐基准

### 2.1 KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
**KuaiRecV2：面向多样化与多任务推荐的大规模持续学习基准**

- **Authors / 作者:** Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Affiliation / 机构:** Individual affiliations not fully enumerated in available metadata; benchmark/data context explicitly stated as **industrial-level data from Kuaishou (快手)**.
- **Venue / 会议:** **Accepted to NeurIPS 2026** (arXiv comment), arXiv cs.IR (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Offline recommendation evaluation often diverges from online reality. Key gaps: (1) continual learning under dynamic item pools/distribution shifts, (2) token/item-level accuracy-diversity trade-offs, (3) multi-task reward balancing for generative recommenders.
  - **Methodology:** KuaiRecV2 provides million-scale multimodal item information and long-term interactions across **30 days** with a dynamic video candidate pool, plus a unified rubric for retrieval accuracy, diversity, and multi-task performance.
  - **Innovations:** A realistic benchmark requiring joint improvement across dimensions (continual learning, diversity, controllable multi-objective/generative recommendation) rather than isolated metric optimization.
- **Comparison & results / 对比与结果（author-reported）:**
  - Positioned against simpler static/offline setups by emphasizing dynamic pools, long-horizon shifts, and joint metrics; detailed baselines/leaderboard are in the paper and code. Core claim: more faithful evaluation for real-world recommender progress.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16795) · [PDF](https://arxiv.org/pdf/2611.16795) · [Code](https://github.com/cxli2333/KuaiRecV2)

### 2.2 Wayfinder: Adaptive Resource Routing from Agent Citations
**Wayfinder：基于智能体引用的自适应资源路由**

- **Authors / 作者:** Miguel Romero, George Karypis
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** **Accepted to NeurIPS 2026** (arXiv comment), arXiv cs.LG/cs.IR (2026-11-11)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Agents must locate information across heterogeneous/overlapping resources (chat, issue trackers, email, KBs) where static tool descriptions are insufficient.
  - **Methodology:** Adaptive router uses documents cited by downstream agents as feedback to update internal resource representations; **resource augmentation** (anonymize/permute identities) during offline RL reduces overfitting.
  - **Innovations:** Citation-driven closed-loop routing and controlled testbeds (**NFCorpus, FEVER, Tech Startup**) pairing queries with resource-access patterns.
- **Comparison & results / 对比与结果（author-reported）:**
  - Outperforms supervised, tool-retrieval, and contextual bandit baselines under shared closed-loop protocol when resources overlap and descriptions are weak. Description-based retrieval remains sufficient for distinct corpora; augmentation helps most with few training environments.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16053) · [PDF](https://arxiv.org/pdf/2611.16053)

### 2.3 Predicting the Needle in a Petabyte Scale Haystack: Open-Vocabulary Event Anticipation in Satellite Imagery
**在 PB 级大海中预测“针”：卫星影像中的开放词汇事件预测**

- **Authors / 作者:** Shreelekha Revankar, Mikhail Klassen, Creon Levit, Ash Hoover, Kavita Bala, Bharath Hariharan
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify in PDF).
- **Venue / 会议:** **To be published in NeurIPS 2026** (arXiv comment), arXiv cs.CV/cs.IR (2026-11-11)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Anticipating open-vocabulary events (where/what/when completion) from global daily satellite imagery is hard and annotation-infeasible at scale.
  - **Methodology:** Represents change as vector differences between vision-language embeddings across time; automated global data engine; dataset of **21,000+ locations, 64+ event types, ~2M images** (PlanetScope/Sentinel-2, six continents).
  - **Innovations:** Embedding-arithmetic change representation for scalable discovery and open-vocabulary anticipation (detection, retrieval, completion forecasting).
- **Comparison & results / 对比与结果（author-reported）:**
  - Change detection: **93.5% max F1**. Predicted event retrieval: **3.6×** over baselines. Completion-date forecasting: **3-day median error**, even **9 months** before completion.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16000) · [PDF](https://arxiv.org/pdf/2611.16000) · [Code](https://github.com/ShreelekhaR/predicting-the-needle)

### 2.4 Slim Foundation Models for Latency-Critical Recommendation Serving (SlimFM)
**面向低延迟关键推荐服务的轻量基础模型（SlimFM）**

- **Authors / 作者:** Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** **NeurIPS 2026 Workshop — Long Context Foundation Model** (journal-ref/comment), arXiv cs.IR/cs.AI (2026-11-07)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLMs improve CTR semantics (cold-start/long-tail) but are too costly for online serving; many systems cache LLM outputs offline.
  - **Methodology:** (1) dependency-aware structured pruning **LLaMA3-8B → 4.5B** (44% reduction), (2) LoRA field-aware fine-tuning for discriminative field-level semantic embeddings, (3) semantic-guided fusion into conventional CTR feature interactions.
  - **Innovations:** Practical online LLM semantic modeling for latency-critical CTR.
- **Comparison & results / 对比与结果（author-reported）:**
  - Across **4 datasets and 6 CTR backbones**: retains **>99%** of uncompressed-model accuracy and reduces inference latency by **up to 3.4×** vs existing LLM-enhanced baselines.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.11013) · [PDF](https://arxiv.org/pdf/2611.11013)

---

## 3. Advertising, CTR & Generative/Sequential Recommendation (Kuaishou/Alibaba context)
### 广告、CTR 与生成式/序列推荐（快手/阿里相关）

### 3.1 TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
**TS-GEAR：淘宝闪购生成式广告检索**

- **Authors / 作者:** Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Affiliation / 机构:** **Taobao Shangou / Alibaba ecosystem** (deployment stated in abstract); individual affiliations not fully enumerated in metadata.
- **Venue / 会议:** arXiv cs.IR/cs.AI/cs.CL (2026-11-09), industrial/deployed system
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** On-demand delivery ads require hard geographic reachability, query/location-conditioned preferences, and set-level diversity; standard generative retrieval treats geography softly and optimizes sequences independently.
  - **Methodology:** **Geo-Semantic ID** (geographic prefix + semantic suffix) makes reachability a prediction target; **Query-Geo Target Attention** conditions history on real-time query/location with behavior-location keys; **GMPO (Group Marginal Policy Optimization)** uses deduplicated group rewards/marginal advantages (GRPO-style) to reduce near-duplicates.
  - **Innovations:** Differentiable geographic validity, geo/query-aware interest modeling, and set-level optimization for generative ad retrieval.
- **Comparison & results / 对比与结果（author-reported）:**
  - Deployed with **0.1B backbone**, serving **>150M queries/day** in Taobao Shangou search advertising. Outperforms SOTA generative retrieval on **HitRate** and **geographic validity**. Online: **+3.8% ad impressions, +4.2% ad revenue**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.12180) · [PDF](https://arxiv.org/pdf/2611.12180)

### 3.2 TriGen: A Generative Paradigm for Trigger-Induced Recommendation
**TriGen：面向触发式推荐的生成范式**

- **Authors / 作者:** Muyu Zou, Haibo Xing, Shunye Tang, Liyan Tie, Lingyu Mu, Yandong Wang, Jinxin Hu
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.IR (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Trigger-Induced Recommendation (TIR) must align with immediate post-action intent while preserving long-term preferences.
  - **Methodology:** **Calibrated tail injection**, **dynamic gating** (persistent tastes vs immediate impulses), and **position-specific transformations** for level-aware trigger guidance during generation.
  - **Innovations:** Generative TIR balancing instant intent and historical preference with controllable trigger conditioning.
- **Comparison & results / 对比与结果（author-reported）:**
  - Offline gains and online A/B improvements across **six country markets** with **full production deployment** (detailed numbers in paper).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16395) · [PDF](https://arxiv.org/pdf/2611.16395)

### 3.3 ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through Item Reachability
**ReSID：通过物品可达性重新思考生成式推荐中的长尾检索**

- **Authors / 作者:** Muyu Zou, Shunye Tang, Yi Xu, Haibo Xing, Yandong Wang, Lingyu Mu, Jinxin Hu
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.IR (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Long-tail items are hard to reach in generative recommendation across SID construction, decoding, and matching.
  - **Methodology:** **ReSID** uses long parallel SIDs, popularity-debiased and user-semantic-aware beam search, and **partial SID matching** to recover tail candidates.
  - **Innovations:** Explicit reachability-oriented design for long-tail generative retrieval.
- **Comparison & results / 对比与结果（author-reported）:**
  - SOTA long-tail retrieval with competitive overall accuracy, lower latency/higher throughput under narrow beams, and production deployment gains.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16404) · [PDF](https://arxiv.org/pdf/2611.16404) · [Code](https://github.com/Gabriel-reina/ReSID)

### 3.4 From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory Prediction (TraGR)
**从 Token 到行为：面向用户轨迹预测的生成式推荐再思考（TraGR）**

- **Authors / 作者:** Jiaqi Wang, Hanchen Yang, Hengyu Zhang, Hongxu Ma, Wenqi Rao, Hongyang Wang, Zhongbo Sun, Renliang Qian, Weixin Chen, Wengen Li, Jihong Guan, Shuigeng Zhou, Qingpeng Cai, Peng Jiang, Hong Cheng
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.IR (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** User behavior trajectory prediction (UBTP) is often framed as serial token decoding, under-modeling behavior-level transitions.
  - **Methodology:** Predicts SID tokens in parallel within each interaction, models transitions via recurrent state updates, and uses probability-weighted feedback plus relation-aware trajectory learning on model-generated rollouts.
  - **Innovations:** Behavior/trajectory-centric generative recommendation beyond token-by-token generation.
- **Comparison & results / 对比与结果（author-reported）:**
  - Consistent gains over SOTA baselines on **four public datasets** across prediction horizons.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16159) · [PDF](https://arxiv.org/pdf/2611.16159) · [Code](https://github.com/CalmaQi/GR4UBT)

### 3.5 When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence
**推荐何时激发好奇心？理论、测量与实证证据**

- **Authors / 作者:** Pan Li, Alexander Tuzhilin
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify in PDF).
- **Venue / 会议:** arXiv cs.IR (2026-11-11)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Curiosity can mitigate filter bubbles and sustain engagement but lacks a formal, computable recommender-system measure grounded in information-gap theory.
  - **Methodology:** Derives a canonical curiosity measure from **five axioms** and builds a curiosity-aware recommender incorporating it into utility.
  - **Innovations:** End-to-end bridge from psychological theory to measurement, offline ranking, and production experimentation.
- **Comparison & results / 对比与结果（author-reported）:**
  - Survey: measure matches self-reported curiosity and outperforms proxy metrics. Offline: significant improvements on **three real-world datasets**. Online controlled experiment at a **major Asian video-streaming platform**: significant increases in **CTR, video views, and time spent** vs latest production system; deployed in production.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.14938) · [PDF](https://arxiv.org/pdf/2611.14938)

---

## 4. LLMs, Multimodal, Diffusion & Architecture Research
### 大语言模型、多模态、扩散与架构研究

### 4.1 Unbundling Multimodal Vision Encoding
**解构多模态视觉编码**

- **Authors / 作者:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu
- **Affiliation / 机构:** Not explicitly specified in arXiv metadata (project: unbundling.github.io). Author list includes researchers affiliated with major labs in prior work; verify specific affiliations in PDF.
- **Venue / 会议:** arXiv cs.CV/cs.LG (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Multimodal vision encoding choices (pretrained visual prior, dedicated vision capacity, pre-fusion placement) are conflated across prior models/data/compute.
  - **Methodology:** Controlled from-scratch pretraining framework at matched lifetime compute on VQA and language benchmarks to isolate each factor.
  - **Innovations:** Clean factorization showing **dedicated vision capacity** matters most; pretrained visual priors are not necessary when jointly trained; in-fusion early vision modules can match pre-fusion encoders and reduce TTFT.
- **Comparison & results / 对比与结果（author-reported）:**
  - Jointly trained encoder matches pretrained prior; encoder-free model lags even when backbone enlarged by encoder parameter count. Findings hold across backbone sizes, when encoder pretraining treated as free, and from pretrained LM starts.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17334) · [PDF](https://arxiv.org/pdf/2611.17334) · [Project](https://unbundling.github.io)

### 4.2 ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
**ArchSpace：记录、评审与引用 LLM 架构研究**

- **Authors / 作者:** Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.CL/cs.LG (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Architecture progress is fragmented by underreported negative results and inconsistent small-scale baselines.
  - **Methodology:** Public platform to **record** proposals/experiments/reasoning, **review** by community, and **reference** validated ideas; uses scaling-law prediction from smaller experiments before costly large-scale training.
  - **Innovations:** Cumulative infrastructure for architecture research with reusable baselines/recipes (e.g. Qwen3.5/OLMo3 baselines, fitted scaling laws).
- **Comparison & results / 对比与结果:**
  - Platform/infrastructure contribution (not a single-model SOTA claim); aims to improve comparability and reduce wasted large-scale trials via extrapolation-guided screening.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17332) · [PDF](https://arxiv.org/pdf/2611.17332)

### 4.3 Learning When Diffusion Language Models Should Regenerate (DiVR)
**学习扩散语言模型何时应重新生成（DiVR）**

- **Authors / 作者:** Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, Minsik Seol, Jungwoo Lee
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.CL (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Remasking in diffusion LMs needs to know when/what to revise; token confidence misses hidden-state error signals and isolated remasking often reproduces errors with fixed context.
  - **Methodology:** **DiVR** verifier trained on final correctness of the generator’s own trajectories decides when to regenerate a block and which alternative to retain (generator unchanged).
  - **Innovations:** Trajectory-correctness-guided regeneration improving compute/accuracy trade-off without modifying generator weights.
- **Comparison & results / 对比与结果（author-reported）:**
  - On **five reasoning benchmarks** with LLaDA-8B-Base: average accuracy **35.3% → 43.4%** at **1.9–3.5×** greedy-decoding cost, outperforming search baselines using **3.8–7.4×** cost. Complements SFT/RL and generalizes to other generators (e.g. Dream).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17320) · [PDF](https://arxiv.org/pdf/2611.17320)

### 4.4 Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation for Diffusion LLMs (MPPA)
**掩码模式位置增强：面向扩散大语言模型的免训练长上下文外推（MPPA）**

- **Authors / 作者:** Gaurav Sarkar, Syed Affan Daimi
- **Affiliation / 机构:** **International Institute of Information Technology, Hyderabad (IIIT Hyderabad)**.
- **Venue / 会议:** arXiv cs.LG (2026-11-11)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Diffusion LLMs use bidirectional attention and iterative unmasking, but RoPE limits context; static AR-style extrapolation ignores evolving mask patterns.
  - **Methodology:** **MPPA** interpolates positions into pretrained window then adds per-position/per-step offsets from cumulative mask density, restoring rotary phase resolution and shrinking offsets as tokens commit.
  - **Innovations:** Diffusion-native, mask-conditioned position engineering.
- **Comparison & results / 对比与结果（author-reported）:**
  - On **LLaDA-8B-Instruct** at **2×** 4096-token window: perplexity **19.51 → 3.12** at 8192 tokens with **100% passkey retrieval** and unchanged NIAH accuracy (preliminary 2× experiments vs static NTK/length-only baselines).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.15029) · [PDF](https://arxiv.org/pdf/2611.15029)

---

## 5. Agent Systems, Code Execution Prediction & Benchmarks
### 智能体系统、代码执行预测与基准

### 5.1 AgentSSL: Can MLE Agents Leverage Unlabeled Data?
**AgentSSL：MLE 智能体能否利用无标注数据？**

- **Authors / 作者:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment), arXiv cs.AI/cs.LG (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** MLE agents are mostly studied in fully supervised settings; semi-supervised/label-scarce regimes with abundant unlabeled data are underexplored.
  - **Methodology:** **Agentic Semi-Supervised Learning (AgentSSL)** frames SSL pipeline design as program search under weak feedback; releases **ProgramSelectBench** (16,977 agent-generated and human-engineered SSL programs).
  - **Innovations:** Demonstrates agents can synthesize/adapt SSL techniques, while exposing **program selection** as a critical bottleneck.
- **Comparison & results / 对比与结果（author-reported）:**
  - Exceeds strongest human-engineered baselines in **8/12** settings (up to **+21.8%**) under weak feedback/matched compute; selection based on agent feedback metric can drop performance by up to **47%**. Evaluated on controlled benchmarks and real-world ecology detection tasks.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17323) · [PDF](https://arxiv.org/pdf/2611.17323) · [Project](https://codiscovery.ai/AgentSSL)

### 5.2 CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
**CoReMem：面向连续编码任务的成本内化记忆与前瞻性价值评估**

- **Authors / 作者:** Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, Heng Chang, Fei Fei, David van Dijk, Rex Ying
- **Affiliation / 机构:** **Yale University; Tsinghua University; Goodvision AI** (as listed in arXiv per-author metadata).
- **Venue / 会议:** arXiv cs.AI/cs.CL/cs.SE (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Successive repository tasks require memory for unknown future tasks while balancing write/read costs and deciding when to act on memory.
  - **Methodology:** **Prospective segment valuation** compares next-task runs with/without trajectory segments to build compact anchor memories (repo locations, executable checks); actor adaptation uses on-policy memory-value estimation and **provenance-gated value credit**.
  - **Innovations:** Cost-internalizing memory design + credit assignment tied to actual memory use.
- **Comparison & results / 对比与结果（author-reported）:**
  - On **ChainSWE**, 27B actor resolve rate **21.0% → 25.7%** with **17% fewer steps** and **11% fewer cache-aware tokens** vs untrained actor without memory.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17316) · [PDF](https://arxiv.org/pdf/2611.17316)

### 5.3 Classical Energies Learn to Reason 1,000x Faster than Looped Models (CRAM)
**经典能量模型以 1000 倍速度学习推理（CRAM）**

- **Authors / 作者:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.AI/cs.LG (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Looped reasoning models can be unstable, slow to train, and parameter/FLOP-heavy on simple puzzles.
  - **Methodology:** **CRAM**, a learned Hopfield & Tank-style energy model with adaptive compute/early stopping and training without differentiating through a solver.
  - **Innovations:** Energy-based reasoning alternative emphasizing interpretability and efficiency.
- **Comparison & results / 对比与结果（author-reported）:**
  - Solves **99.996%** of Sudoku-Extreme and **100%** of Maze-Unique after **42 ms** and **132 ms** training on one GPU (≥**1,000×** faster than looped models on these tasks). Matches highest looped-model accuracy on Sudoku-Extreme with ≥**282× fewer inference FLOPs**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17309) · [PDF](https://arxiv.org/pdf/2611.17309)

### 5.4 Goal Encoding in LLMs
**大语言模型中的目标编码**

- **Authors / 作者:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.CL/cs.AI/cs.LG (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Understanding how LLMs represent and pursue subgoals in multi-subtask settings.
  - **Methodology:** Localizes next-subgoal encodings in outputs of a **sparse set of attention heads**, decodes them into natural language, demonstrates causal/plastic transfer across environments/languages, and tests a **non-recurrent goal-seeking (NRGS)** account via interventions.
  - **Innovations:** Mechanistic, actionable goal representations with intervention evidence.
- **Comparison & results / 对比与结果（author-reported）:**
  - Provides causal and transplant experiments (qualitative/quantitative details in paper) supporting transferable subgoal encodings rather than purely recurrent state tracking.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17297) · [PDF](https://arxiv.org/pdf/2611.17297) · [Project](https://goals.baulab.info/)

### 5.5 daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving
**daVinci-Prover：面向形式化定理证明的智能体原生中期训练**

- **Authors / 作者:** Wenhong Zhu, Xuefeng Li, Jiashuo Zhang, Yu Chen, Tiantian Mi, Qipeng Guo, Pengfei Liu
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.CL (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLM theorem proving lacks transparent data recipes combining mathematical priors with long-horizon interactive proof construction.
  - **Methodology:** Synthesizes **agent-native 33.7B-token mid-training corpus** (decomposition/search/self-verification/revision) plus verifier-grounded trajectories; **daVinci-Prover harness** for isolated Lean verifier interaction; ~**36K** high-quality agent trajectories for SFT.
  - **Innovations:** Agent-native mid-training + verifier-grounded data + interactive proving harness.
- **Comparison & results / 对比与结果（author-reported）:**
  - Average **+13.7 points** over matched **Qwen3-8B SFT-only** baseline across **MiniF2F, FATE-M, ProofNet**. Applied to **Qwen3.5**: strong proving performance and near-saturating MiniF2F with memory compaction.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16433) · [PDF](https://arxiv.org/pdf/2611.16433)

### 5.6 Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon
**Metal Sandbox：面向 Apple Silicon 上 GPU 编码智能体的隔离执行与命令调度**

- **Authors / 作者:** Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, Zheng Ge, Daxin Jiang, Junchi Yan
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify in PDF).
- **Venue / 会议:** arXiv cs.LG/cs.AI/cs.CL/cs.DC (2026-11-12)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** GPU coding-agent rollouts interleave model requests, dev commands, and GPU execution, leaving GPU capacity idle across concurrent sessions.
  - **Methodology:** **Metal Sandbox** provides restricted per-instance file access, native command execution, command-level scheduling across interconnected Macs (parallel concurrency, serial slot sharing, migration of eligible waiting commands). Integrated with **Harbor** for task execution/verification/rollout collection.
  - **Innovations:** Infrastructure for efficient training/evaluation of GPU coding agents on Apple Silicon clusters (code execution prediction/optimization context).
- **Comparison & results / 对比与结果（author-reported）:**
  - On **4 Mac mini M4 nodes**: **1.68×–2.05×** command throughput under concentrated demand. Sixteen static traces: estimated **2.14×** sustained throughput (4 sessions/node vs 1). Dynamic replay: **18.8%** lower mean tool waiting, **22.3%** lower batch elapsed time (assumptions stated).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17294) · [PDF](https://arxiv.org/pdf/2611.17294) · [Code](https://github.com/WangHaoZhe/metal-sandbox) · [Harbor](https://github.com/WangHaoZhe/harbor)

### 5.7 SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction
**SimRec：从模拟交互中学习搜索、提问与推荐**

- **Authors / 作者:** Yaxin Zhang, Xingyu Wu, Yuchen Yan, Yuqin Dai, Hong Zhao, Lixing Shen, Zhan Chen, Jian Shao, Yongliang Shen
- **Affiliation / 机构:** Not explicitly specified in available metadata (code under ZJU-REAL; verify in PDF).
- **Venue / 会议:** arXiv cs.CL/cs.AI/cs.IR (2026-11-11)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Agentic recommenders often use hand-designed behaviors and optimize components separately rather than full interaction policy.
  - **Methodology:** RL framework trains full tool-integrated policy with task-anchored user simulator (external LLM or self-play), task-aligned trajectory reward optimized via **GRPO**, crediting retrieval quality, valid tool use, and final hit (training-only target injection for sparse hits).
  - **Innovations:** End-to-end policy learning for multi-turn search/ask/recommend agents.
- **Comparison & results / 对比与结果（author-reported）:**
  - On **ESCI** and **Amazon C4**, **NDCG@100**: **32.23% → 35.42%** and **22.94% → 24.72%** for a **Qwen3-4B** agent; outperforms training-free agents on larger backbones and task-aligned baselines. Trained agent more often verifies candidates, uses preferences, and recovers from rejection.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.15426) · [PDF](https://arxiv.org/pdf/2611.15426) · [Code](https://github.com/ZJU-REAL/SimRec)

### 5.8 Continual-ARC: Measuring Skill Acquisition over a Working Lifetime
**Continual-ARC：衡量“工作生涯”中的技能习得**

- **Authors / 作者:** Daniel Lenton
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.LG (2026-11-10), benchmark
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Continual-learning benchmarks often separate memory- vs weight-based learners and use limited domains/one-shot protocols.
  - **Methodology:** Lifelong stream from ARC-AGI editions with recurring tasks, dormant gaps, fresh instances, budgeted demos/submissions/retries; unified scoring and post-stream split for memorization vs generalization.
  - **Innovations:** Fairer long-horizon comparison of harness persistence and parametric learning.
- **Comparison & results / 对比与结果（author-reported）:**
  - Evaluated frozen-weight harnesses (Qwen3.5-9B, GLM-5.3 Flash variants) vs prompting floors, program induction, weight imitation. Persistence generally does not improve memorization without explicit expert guidance; most harness methods learn less than demonstration-caching floor; no harness-based method gains on unseen tasks while weight-based learning shows substantial generalization gains.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.14505) · [PDF](https://arxiv.org/pdf/2611.14505) · [Code](https://github.com/unifyai/continual-arc)

### 5.9 EvoX: Rethinking the Agent Harness as a Runtime Policy
**EvoX：将智能体框架重新定义为运行时策略**

- **Authors / 作者:** Haoyang Zhang, Qumeng Sun, Xiao Zhang, Xiang Liu, Zhidong Fan, Junjie Wang
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** arXiv cs.AI/cs.SE (2026-11-11), technical report
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Plausible model decisions fail in execution (tool-call mismatches, interrupted workflows, unsupported completion claims).
  - **Methodology:** **EvoX** (Rust runtime) operationalizes harness as **Operational Policy** via Action Realization, Execution Continuity, Outcome Grounding; **Contrast** evaluation framework with fairness/request verification/evidence-based adjudication.
  - **Innovations:** Deterministic runtime control and auditable harness benchmarking.
- **Comparison & results / 对比与结果（author-reported）:**
  - Across **5 benchmarks, 6 foundation models, 6 harnesses** (691 common pairs): **56.2%** success, ~**+3.0 pp** over average of other harnesses; larger gains on **GLM-5.3 (+10.7 pp)** and **Kimi K3 (+7.9 pp)**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.15006) · [PDF](https://arxiv.org/pdf/2611.15006)

---

## 6. Games & Interactive Applied Systems
### 游戏与交互应用系统

### 6.1 SkinAdvisor: An AI-Driven Decision Framework for Skin Production Planning
**SkinAdvisor：面向游戏皮肤生产规划的 AI 决策框架**

- **Authors / 作者:** Ge Fan, Kai Wang, Chaoyun Zhang, Yingjie Li, Yuze Liu, Junyang Chen
- **Affiliation / 机构:** Not explicitly specified in available metadata.
- **Venue / 会议:** **Accepted to AAAI 2027 (IAAI-27)** (arXiv comment), arXiv (2026-11-11)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Game skin release/pricing/production decisions are often intuition-driven despite major revenue impact.
  - **Methodology:** **SkinAdvisor** framework powered by **SkinCast** multi-modal Transformer forecasting **180-day** per-day sales trajectories for unreleased skins (Informer time-series encoder, Player-Hero-Skin graph embedder, attribute/context Transformers, shared backbone, non-autoregressive Informer decoder). Serving pipeline: Select → Fill → Infer → Sales → ROI → Ranking.
  - **Innovations:** End-to-end deployed forecasting-to-decision system for live game content planning.
- **Comparison & results / 对比与结果（author-reported）:**
  - Offline: RMSE **~20%** lower than strongest baseline (Informer) and **~60%** lower than classical methods. Serving: p99 latency **<8 ms**, peak throughput **>1100 rps** on 16-core CPU; in production for a full release cycle.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.15023) · [PDF](https://arxiv.org/pdf/2611.15023)

---

## 7. Cross-cutting trends & focus-org notes

1. **Generative retrieval/recommendation in production:** geo-semantic IDs and set-level RL (TS-GEAR, Alibaba/Taobao Shangou), trigger-aware generation (TriGen), and long-tail reachability (ReSID) show continued convergence of generative modeling with ads/CTR/engagement constraints.
2. **Latency-aware foundation-model serving:** SlimFM demonstrates pruning + field-aware adaptation as a practical path to online LLM semantics for CTR.
3. **Agent reliability as systems research:** runtime policies (EvoX), memory cost/provenance (CoReMem), program selection under weak feedback (AgentSSL), and long-horizon skill/memorization evaluation (Continual-ARC) shift focus from raw capability to dependable execution.
4. **Diffusion LMs & reasoning efficiency:** mask-aware extrapolation (MPPA), verifier-guided regeneration (DiVR), and energy-based reasoning (CRAM) highlight alternative scaling/compute trade-offs beyond standard autoregressive loops.
5. **Focus-org coverage (this run):** explicit company/lab context observed for **Kuaishou** (KuaiRecV2) and **Alibaba/Taobao Shangou** (TS-GEAR); author lists include researchers commonly associated with major labs but many papers do not specify institutional affiliations in metadata. **Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Tencent, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon** had no newly verified first-party accepted-paper entries extracted in this constrained run—likely a retrieval/proceedings-access limitation rather than absence of work.

## 8. Follow-up recommendations

- Re-crawl official proceedings/OpenReview/virtual sites for ICML 2026, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, SIGIR 2026, WWW 2026, AAAI 2026 once web search or browser-accessible exports are available.
- Verify author affiliations and full experimental tables from PDFs for papers where metadata is incomplete (especially target-company attribution).
- Add focused searches for games/RL-in-games, code execution prediction benchmarks, and ads/CTR papers from ByteDance, Tencent, Baidu, Netflix, Microsoft Research, Meta AI, NVIDIA, Google DeepMind when API/search access is restored.

*Compiled 2026-11-16. Preference file active: `EXTEND.md` (repo root, bm25 `auto_prompt`).*