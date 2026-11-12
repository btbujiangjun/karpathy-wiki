---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-12 Daily Edition"
type: synthesis
created: 2026-11-12
updated: 2026-11-12
sources: [arXiv recent listings cs.CL/cs.IR/cs.LG, arXiv abstracts, prior wiki conference digests]
tags: [conference-digest, ICML2026, ICLR2026, NeurIPS2025, AAAI2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-12 Daily Edition

> Daily digest covering requested venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) and recent arXiv papers in AI, LLMs, recommendation systems, advertising, CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks.
>
> **Method & limitations (2026-11-12):** Compiled from arXiv recent listings/abstracts (`cs.CL`, `cs.IR`, `cs.LG`, cross-lists) and existing wiki synthesis pages. The `websearch` integration was unavailable in this run, so full accepted-paper/proceedings crawls for some conferences were not independently refreshed today; venue sections include latest verifiable highlights from accessible public/arXiv signals and clearly note gaps. All results/metrics are **author-reported** unless stated otherwise. Affiliations are reported as stated in arXiv metadata/abstract text; when not explicitly listed, this is noted (with deployment/company context only when explicitly stated by authors).

---

## 1. Conference / Venue Snapshot (2025–2026)

| Venue | Status (as of this digest) | Notes |
|---|---|---|
| **ICML 2026** (Seoul, Jul 6–12, 2026) | Proceedings/awards publicly announced earlier; full machine-readable crawl not refreshed in this run | Prior highlights in wiki include outstanding papers on diffusion LMs/sampling theory and A3C test-of-time; see `wiki/synthesis/2026-11-11/conference-digest.md`. |
| **ICLR 2026** (Rio, Apr 28–May 2, 2026) | Awards/program announced earlier; accepted-paper page fetch failed in this run (404 path attempted) | Prior highlights: Transformer succinctness, multi-turn conversation degradation, Muon/matrix-sign methods. |
| **NeurIPS 2025** (San Diego + Mexico City, Dec 2–7, 2025) | Completed; incremental proceedings mining limited in this run | Several 2026-track benchmark papers appear on arXiv with NeurIPS/CIKM/RecSys workshop comments. |
| **AAAI 2026** | Not fully crawled in this run | Gap: no fresh verified accepted-paper list extracted today. |
| **KDD 2026** | Not fully crawled in this run | Industrial rec/ads papers continue to appear on arXiv with deployment claims (see below). |
| **CVPR 2026** | Not fully crawled in this run | Gap: no fresh verified accepted-paper list extracted today. |
| **ACL 2026** | Not fully crawled in this run | No newly verified ACL-2026-tagged paper added in this scan beyond prior wiki context. |
| **EMNLP 2025** | Completed; not fully re-crawled today | Prior wiki digests contain EMNLP highlights; no new verified extraction in this run. |
| **SIGIR 2026** | Workshops/papers appearing in arXiv comments (e.g. ReNeuIR @ SIGIR 2026) | Example: StaRSE accepted to ReNeuIR @ SIGIR 2026 (arXiv 2611.14236). |
| **WWW 2026** | Not fully crawled in this run | Gap noted. |
| **CIKM 2025/2026** | Some 2026 proceedings references appear on arXiv | Example: counterfactual rec explanation work published at CIKM 2026 (arXiv 2611.13914). |
| **RecSys 2025/2026** | Workshop/track papers visible on arXiv | Examples: LUMIR accepted at DaQuaMRec Workshop (RecSys 2026), AST comments RecSys '26, sponsored-search ranking at RecSys 2026 Workshop CARS context in prior digest. |

---

## 2. Recommendation Systems, Advertising, CTR & Sequential Modeling

### 2.1 Industrial Generative Recommendation / Ads Retrieval / CTR

#### 1) SepLRM: A Foundation Model Paradigm for Recommendation / 《SepLRM：面向推荐的基础模型范式》
- **Authors:** Di Chen, Xijun Xiao, Qin Ren, Weijiang Lai, Zhijian Pan, Zhentao Pan, Pengfei Nie, Cheng Yuan, Zixuan Tan, Xuyang Liu, Tao Wang, Yunwen Huang, Hao Fang, Yichao Wang, Hao Zhang, Siyuan Wu, Hao Chen, Han Diao, Mingyu Yang, Yongkang Feng, Beihong Jin, Jinfeng Yang, Deping Xie, Peng Xu, Zheng Chai, Yuchao Zheng
- **Affiliation (company/institution):** Not individually enumerated in arXiv metadata; **deployment and online A/B tests stated at ByteDance** in abstract (industry-scale production context).
- **Venue/conference:** arXiv preprint (submitted 2026-11-07), cs.IR
- **Abstract and key innovations:** 
  - **Problem background:** Large recommendation models (LRMs) gain from longer behavior sequences and larger capacity, but ROI degrades because expensive long-sequence encoding is repeatedly executed across stages/scenarios.
  - **Methodology:** SepLRM reorganizes multiple end-to-end LRMs into one shared **Recommendation Foundation Model (RFM, encoder-decoder)** and multiple independently optimized **Vertical Models (VMs)**. RFM exports final-layer encoder state as a shared **KV cache** independent of downstream candidates; VMs issue candidate-conditioned queries over shared KV.
  - **System co-design:** Cache compression, train/serve workflow, and **LG-Store** distributed KV-cache storage to make transfer efficient.
  - **Key innovations:** Native KV interface preserves fine-grained behavioral information (vs logits/pooled embeddings), enabling high-fidelity transfer while avoiding duplicated sequence encoding.
- **Comparison with prior methods / experimental results (author-reported):**
  - On three large-scale datasets: **state-of-the-art offline performance** with **~100% transfer rate**.
  - Strong transferability across model iterations, recommendation stages, and business scenarios.
  - Deployment in two large-scale industrial scenarios: **substantially improves ROI of sequence scaling** and delivers **consistent gains in online A/B tests at ByteDance** (exact metric deltas not specified in abstract).
  - Compared to separate E2E LRMs per scenario/stage, SepLRM reduces redundant encoding while preserving/improving effectiveness.
- **arXiv/PDF:** https://arxiv.org/abs/2611.10356 · https://arxiv.org/pdf/2611.10356

#### 2) TS-GEAR: Taobao Shangou GEnerative Ad Retrieval / 《TS-GEAR：淘宝闪购生成式广告检索》
- **Authors:** Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Affiliation (company/institution):** **Taobao Shangou / Alibaba ecosystem** (stated by problem setting and deployment in Taobao Shangou search advertising pipeline).
- **Venue/conference:** arXiv preprint (submitted 2026-11-09), cs.IR / cs.AI / cs.CL
- **Abstract and key innovations:**
  - **Problem background:** On-demand delivery ads require delivery reachability (geography) as a hard validity constraint, not just ranking preference; generative retrieval must handle geo validity, location/query-conditioned interests, and set-level redundancy.
  - **Methodology:** (1) **Geo-Semantic ID** splits merchant IDs into geographic prefixes + semantic suffixes, making reachability a prediction target; (2) **Query-Geo Target Attention** aggregates history conditioned on real-time query/location and encodes behavior location in keys; (3) **GMPO (Group Marginal Policy Optimization)** rewrites advantages with deduplicated group rewards/marginal advantages to discourage near-duplicates.
  - **Key innovations:** Jointly addresses hard geographic validity, geo/query-aware interest modeling, and set-level diversity/value in autoregressive generative ad retrieval.
- **Comparison with prior methods / experimental results (author-reported):**
  - Deployed online with lightweight **0.1B backbone**, serving **>150M queries/day** in Taobao Shangou search advertising.
  - **Consistently outperforms state-of-the-art generative retrieval methods** on HitRate and geographic validity.
  - Online gains: **+3.8% ad impressions, +4.2% ad revenue**.
  - Compared to prior semantic-ID/generative retrieval approaches, TS-GEAR turns geography from post-hoc truncation into learned generation constraints and adds set-level optimization.
- **arXiv/PDF:** https://arxiv.org/abs/2611.12180 · https://arxiv.org/pdf/2611.12180

#### 3) Slim Foundation Models for Latency-Critical Recommendation Serving / 《面向低延迟关键推荐服务的轻量基础模型（SlimFM）》
- **Authors:** Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** NeurIPS 2026 Workshop — Long Context Foundation Model (journal-ref on arXiv); arXiv preprint (submitted 2026-11-07), cs.IR / cs.AI
- **Abstract and key innovations:**
  - **Problem background:** Full LLMs improve CTR prediction semantics (especially cold-start/long-tail) but are too expensive for online serving; prior LLM-enhanced CTR often caches outputs offline.
  - **Methodology:** **SlimFM** pipeline: (1) dependency-aware structured pruning compresses **LLaMA3-8B → 4.5B** (44% reduction); (2) LoRA-based field-aware fine-tuning produces discriminative field-level semantic embeddings from lightweight textual prompts; (3) semantic-guided fusion injects embeddings into conventional CTR model feature interactions.
  - **Key innovations:** Makes online LLM semantic modeling practical for latency-critical CTR by combining structured pruning, field-aware adaptation, and fusion into existing backbones.
- **Comparison with prior methods / experimental results (author-reported):**
  - Across **4 datasets and 6 CTR backbones**: retains **>99%** of uncompressed-model accuracy.
  - Reduces inference latency by **up to 3.4×** relative to existing LLM-enhanced baselines.
  - Compared to offline-cached LLM enhancement, SlimFM targets practical online serving with strong accuracy/latency tradeoff.
- **arXiv/PDF:** https://arxiv.org/abs/2611.11013 · https://arxiv.org/pdf/2611.11013

#### 4) CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising? / 《CHO-Bench：上下文提示如何影响LLM广告排序？》
- **Authors:** Shiqi Zhang, Yang Fei, Xiaokui Xiao
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint (submitted 2026-11-09), cs.IR / cs.CL
- **Abstract and key innovations:**
  - **Problem background:** LLM advertising (e.g. conversational ad ranking) can use advertiser-provided natural-language context hints, but effective hint construction is unclear.
  - **Methodology:** Formulates **Context Hint Optimization (CHO)** to improve ad ranking under budget; develops seven hint strategies (What/Who/When) plus Unified strategy; introduces **CHO-Bench** with **>1.19M paired evaluations** across 5 datasets using embedding-based and LLM-based rankers.
  - **Key innovations:** First large-scale offline benchmark framing ad-side hint construction and measuring ranker/strategy/budget interactions.
- **Comparison with prior methods / experimental results (author-reported):**
  - Context hints improve rankings under evaluated offline rankers.
  - Individual strategies yield similar average gains; Unified is not consistently best.
  - Strategy effectiveness depends on generation-ranking configuration (embedding vs LLM rankers favor different dimensions); larger hint budgets improve rankings with diminishing returns.
  - Provides benchmark baseline rather than claiming a single SOTA production system.
- **arXiv/PDF:** https://arxiv.org/abs/2611.11955 · https://arxiv.org/pdf/2611.11955

#### 5) RecoGEM: A Serving System for Production-Scale Generative Recommendation / 《RecoGEM：面向生产级生成式推荐的服务系统》
- **Authors:** Xiangrui Yang, Yunfeng Zhao, Jiawei Yang, Fangyu Zhang, Enrui Zhao, Liang Zeng, Cheng Peng, Minhui Xie, Jiaqiang Liu, Xiao Liang, Yiming Qiu
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata; abstract states deployment for **over nine months across production lines**, serving applications with **hundreds of millions of users** and supporting **>10 GR model families**.
- **Venue/conference:** arXiv preprint (submitted 2026-11-09), cs.DC / cs.AI / cs.IR
- **Abstract and key innovations:**
  - **Problem background:** Generative recommendation shifts from scoring to autoregressive ID generation, creating serving challenges (dependent decoding steps, large item spaces, latency-critical candidate selection) mismatched with conventional RecSys and LLM serving stacks.
  - **Methodology:** **Runtime–engine decoupling** moves GR-specific responsibilities (candidate-state transitions, live artifact updates) to runtime; execution engine optimizes self-attention, candidate selection, and planning for short sequences/large candidate populations/predictable step shapes.
  - **Key innovations:** Production-oriented GR serving architecture co-designed for GR workload characteristics rather than direct reuse of LLM serving systems.
- **Comparison with prior methods / experimental results (author-reported):**
  - On OneModel production workloads: **>1,000 QPS per serving instance**, **P99 latency <35 ms**, and **2.88× throughput improvement** over representative baselines.
  - Compared to conventional RecSys pipelines and LLM-serving baselines, RecoGEM better matches GR decoding/selection patterns in production.
- **arXiv/PDF:** https://arxiv.org/abs/2611.12296 · https://arxiv.org/pdf/2611.12296

### 2.2 Sequential / POI / User Modeling

#### 6) SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory / 《SHARP：面向下一POI预测的语义分层智能体推理与动态记忆》
- **Authors:** Yuhang Zhan, Silin Zhou, Zhuo Chen, Haoxiang Lei, Yunren Feng, Lisi Chen, Shuo Shang
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint (submitted 2026-11-10), cs.IR
- **Abstract and key innovations:**
  - **Problem background:** Next-POI prediction requires bridging LLM semantic reasoning with specific POI decisions, handling evolving user mobility under limited context, and preserving time-specific transition patterns lost in global graphs.
  - **Methodology:** Hierarchical agentic framework where category-level reasoning guides POI prediction; trajectory memory agent maintains dynamic memory bank; multi-granularity time-aware category transition graphs (global + time-conditioned); semantic IDs learned via RQ-VAE and jointly optimized with category-guided POI predictor.
  - **Key innovations:** Combines agentic memory, temporal graph views, and learned semantic IDs in an end-to-end next-POI architecture.
- **Comparison with prior methods / experimental results (author-reported):**
  - On three real-world datasets: improves **Acc@5 by +5.29 pp** and **Acc@10 by +4.52 pp** on average over strongest baseline.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14220 · https://arxiv.org/pdf/2611.14220

#### 7) LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation / 《LUMIR：面向下一POI推荐的异构多模态解耦表示学习》
- **Authors:** Zehui Wang, Wolfram Höpken, Dietmar Jannach
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** Accepted at DaQuaMRec Workshop, co-located with ACM RecSys 2026 (arXiv comment); arXiv preprint (submitted 2026-11-10), cs.IR / cs.LG / cs.MM
- **Abstract and key innovations:**
  - **Problem background:** Multimodal tourism/POI data is heterogeneous and existing fusion methods often couple representation learning tightly to a specific downstream recommender.
  - **Methodology:** Decoupled contrastive framework; LLMs semantically unify heterogeneous modalities into shared textual space; interaction-aware fusion models cross-modal interactions; sequential signals act as structural constraints.
  - **Key innovations:** Reusable multimodal representations learned independently of downstream optimization architecture.
- **Comparison with prior methods / experimental results (author-reported):**
  - On multimodal POI dataset across multiple sequential recommendation backbones: **consistently outperforms existing multimodal fusion baselines** in both accuracy-oriented and beyond-accuracy metrics (specific numbers in paper).
- **arXiv/PDF:** https://arxiv.org/abs/2611.14004 · https://arxiv.org/pdf/2611.14004

#### 8) Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems / 《利用特征不变缩放律实现推荐系统高效A/B实验》
- **Authors:** Zhiliang Chen, Sammy Nammari, Jiahao Su, Xiaoqiang Luo
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint (submitted 2026-11-10), cs.IR / cs.LG
- **Abstract and key innovations:**
  - **Problem background:** Full-scale A/B experiments for feature/model changes are expensive; single small-scale runs are noisy/misleading.
  - **Methodology:** Observes **feature-invariant scaling** in modern recommendation models and uses scaling laws + statistical inference to predict full-scale A/B effects with confidence intervals.
  - **Key innovations:** Compute-efficient screening of neutral/regressive changes using small-scale experiments.
- **Comparison with prior methods / experimental results (author-reported):**
  - Validated on Wukong, HSTU, and LLM-based recommendation models across **>40** architectural/optimization/data changes.
  - Accurately distinguishes beneficial vs neutral/regressive changes with a fraction of full-scale compute; identifies several changes improving HSTU's SOTA on MovieLens-20M.
- **arXiv/PDF:** https://arxiv.org/abs/2611.13539 · https://arxiv.org/pdf/2611.13539

#### 9) From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations / 《从反事实编辑到人类叙事：面向推荐系统解释的LLM驱动解读》
- **Authors:** Vojtech Cahlik, Amir Reza Mohammadi, Rodrigo Alves, Pavel Kordik, Eva Zangerle
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** **CIKM 2026** (Rome, Italy), pp. 6954-6959 (journal-ref/DOI on arXiv); arXiv preprint (submitted 2026-11-10), cs.AI / cs.IR
- **Abstract and key innovations:**
  - **Problem background:** Counterfactual explanations (CFXs) for recommenders can require many low-level edits, making them hard for users to interpret; evaluations often ignore coherence/actionability.
  - **Methodology:** Uses LLMs to summarize raw CFX interaction edit lists into concise natural-language explanations of higher-level preference patterns; optimizes mediators for correctness/informativeness/linguistic quality via preference optimization (DPO) and human-calibrated metrics.
  - **Key innovations:** Bridges valid CFX generation and user-centered communication with LLM-mediated abstraction and targeted evaluation.
- **Comparison with prior methods / experimental results (author-reported):**
  - On MovieLens-1M across multiple counterfactual generators and LMs: summaries achieve high overall linguistic quality; strongest semantic results with high-success CFX methods (e.g. ACCENT, SPINRec).
  - DPO improves semantic metrics in almost all evaluated settings.
  - Compared to raw edit-list explanations, produces more interpretable narratives while preserving correctness signals.
- **arXiv/PDF:** https://arxiv.org/abs/2611.13914 · https://arxiv.org/pdf/2611.13914 · DOI: https://doi.org/10.1145/3799682.3839968 · Code: https://github.com/vcahlik/from-counterfactual-edits-to-human-narratives

---

## 3. LLMs, Agent Systems, Code Execution & Benchmarks

#### 10) AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models / 《AutoScaffold：面向语言模型强化学习的AI引导脚手架》
- **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint (submitted 2026-11-10), cs.LG / cs.CL
- **Abstract and key innovations:**
  - **Problem background:** RLVR outcome rewards discard rich training experience; training-time scaffolds (strategies/hints) are usually hand-designed and domain-specific.
  - **Methodology:** **AutoScaffold** uses a frozen teacher to periodically diagnose student bottlenecks from training experience and generate adaptive scaffolds: (i) class-level strategies and (ii) task-specific hints. Scaffolds are removed at evaluation.
  - **Key innovations:** AI-for-AI adaptive training guidance with minimal domain-specific input and no human intervention; transfers gains to unscaffolded inference.
- **Comparison with prior methods / experimental results (author-reported):**
  - Domains: ALFWorld, search-based QA, mathematical reasoning, GPU kernel generation.
  - Gains over corresponding RL baselines (all unscaffolded eval): **+7.2** points ALFWorld success, **+4.0** points average QA exact match.
  - GPU kernel generation: **up to +5.0** points in fraction of correct kernels faster than PyTorch reference.
  - Math: surpasses QuestA reported accuracy using **~1/3** as many student training steps.
  - Analyses show teacher shifts from step-by-step workflows to targeted fixes and revised scaffolds outperform fixed/no scaffold.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14515 · https://arxiv.org/pdf/2611.14515

#### 11) Continual-ARC: Measuring Skill Acquisition over a Working Lifetime / 《Continual-ARC：衡量终身技能习得的基准》
- **Authors:** Daniel Lenton
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint (submitted 2026-11-10), cs.LG
- **Abstract and key innovations:**
  - **Problem background:** Continual-learning benchmarks often focus on single domains, serve instances once, and separate memory-based vs weight-based learners, limiting fair comparison.
  - **Methodology:** Lifelong stream from three ARC-AGI editions (domain-knowledge-light), recurring tasks with dormant gaps/fresh instances, budgeted demonstrations/submissions/actions with retries, unified scoring for memory- and weight-based systems.
  - **Key innovations:** Post-stream evaluation separates **memorization** (fresh instances of seen tasks) and **generalization** (unseen tasks); comparable protocol for harness persistence and parametric learning.
- **Comparison with prior methods / experimental results (author-reported):**
  - Evaluated agent harness (frozen weights, with/without persistence) on Qwen3.5-9B and GLM-5.3 Flash vs prompting floors, program induction, and weight imitation training.
  - Persistence generally does not improve memorization without explicit expert guidance; most harness methods learn less than a floor caching task demonstrations.
  - No harness-based method gains on unseen tasks, while weight-based learning shows substantial generalization gains.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14505 · https://arxiv.org/pdf/2611.14505 · Code: https://github.com/unifyai/continual-arc

#### 12) ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces / 《ARE-bench：真实研究会话与工作区中的智能体研究能力基准》
- **Authors:** Jiahang Lin, Wanying Ren, Wanghan Xu, Huayu Sha, Yang Shu, Zhonghang Lu, Chengjun Pan, Yi Dong, Shichun Liu, Yuyang Hu, Shihan Dou, Honglin Guo, Huijie Lv, Pujun Zheng, Zhe Sun, Yuankai Ying, Yiding Wang, Jiahao Chen, Zhixiong Yang, Dingbo Yuan, Yicheng Zou, Zhecan Wang, Guoxiu He, Xiaoyu Xing, Qi Zhang, Tao Gui, Xuanjing Huang
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata (multi-author academic collaboration implied).
- **Venue/conference:** arXiv preprint (submitted 2026-11-10), cs.CL
- **Abstract and key innovations:**
  - **Problem background:** Research-agent benchmarks often use clean/self-contained tasks, overestimating performance on real ongoing projects with session history and messy workspaces.
  - **Methodology:** 75 tasks grounded in recruited researchers' real sessions/workspaces (unfinished/outdated/failed artifacts), spanning 7 research stages, 33 requirements, 150 sub-requirements, **1,173 binary checklist items**; preserves prior-request context and full workspace boundary.
  - **Key innovations:** Context-sensitive evaluation separating delivery contracts/general norms from historical and material/workspace requirements.
- **Comparison with prior methods / experimental results (author-reported):**
  - Across 7 frontier models: strongest passes every checklist item on only **66.2%** of tasks.
  - Three models pass ~**69%** when checking only delivery/general norms, but only **28.4%–40.0%** when historical/workspace requirements are enforced.
  - Demonstrates that clean benchmarks can mask capability gaps and overestimate agent reliability.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14364 · https://arxiv.org/pdf/2611.14364

#### 13) Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control / 《Synapse-Control：通过轻量运行时控制实现智能体经验可用化》
- **Authors:** Zhiyuan Huang, Shengan Zheng, Chenghu Yang, Song Zhang, Lingyun Li, Chen Yu, Weiquan Huang, Linpeng Huang
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint (submitted 2026-11-10), cs.CL / cs.AI / cs.LG
- **Abstract and key innovations:**
  - **Problem background:** Experience reuse in tool-using agents (e.g. diagnosis-then-retrieve systems like Sentry) can add costly LLM inference.
  - **Methodology:** Lightweight control plane: rule shortlist + **1.7B classifier** scores candidates instead of generative diagnosis; **micro-contracts** encode reusable interface checks; **Prompt Value Table** tracks guidance/feedback with cooldown/token-budget controls.
  - **Key innovations:** Replaces expensive generative control with cheap selection/verification mechanisms while preserving reliability.
- **Comparison with prior methods / experimental results (author-reported):**
  - Across 1,308 attempts per method on AppWorld and WebShop: **270 successes** (29.8% more than Base), replaces **4,987** generative diagnosis calls.
  - Reduces auxiliary control time relative to Sentry by **50.2% and 51.0%** (respective settings reported).
- **arXiv/PDF:** https://arxiv.org/abs/2611.13615 · https://arxiv.org/pdf/2611.13615

#### 14) Program-Aided Patchable Skill Evolution (PASE) / 《PASE：程序辅助的可补丁技能演化》
- **Authors:** Jiahao Wang, Yuqi Xiong, Qing Yang, Zhipeng Xu, Zhenghao Liu, Zulong Chen, Yubin Bao
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint (submitted 2026-11-10), cs.CL / cs.AI
- **Abstract and key innovations:**
  - **Problem background:** Agent skills stored as natural language entangle procedural logic and descriptive knowledge, making iterative evolution brittle.
  - **Methodology:** Associates skills with executable programs; distills trajectory experience into editable program components and iteratively patches them based on downstream feedback.
  - **Key innovations:** Separates reusable procedural logic from NL docs for targeted, stable skill updates.
- **Comparison with prior methods / experimental results (author-reported):**
  - Across diverse models/benchmarks: **>2.8% improvements** over all baselines; analyses show greater evolutionary stability and generalization.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14019 · https://arxiv.org/pdf/2611.14019

#### 15) OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation / 《OpticalRAG：面向高效RAG的像素空间压缩》
- **Authors:** Senhao Liu, Yuheng Zhang, Chunyu Wei, Yueguo Chen, Xinran Zhang
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** **Accepted at NeurIPS 2026** (comment on arXiv); arXiv preprint (submitted 2026-11-10), cs.CL
- **Abstract and key innovations:**
  - **Problem background:** RAG context/token costs can dominate long-document retrieval-generation pipelines.
  - **Methodology/innovation (per available abstract metadata):** Proposes pixel-space compression for token-efficient RAG, aiming to reduce token budget while preserving retrieval utility (full technical details in PDF).
  - **Key innovations:** Cross-modal compression perspective for RAG efficiency.
- **Comparison with prior methods / experimental results:** Detailed quantitative comparisons are in the paper/PDF; NeurIPS 2026 acceptance indicates peer-reviewed venue validation. Not independently reproduced here.
- **arXiv/PDF:** https://arxiv.org/abs/2611.13675 · https://arxiv.org/pdf/2611.13675

---

## 4. Games, Continual Learning, and Strategic/Interactive Evaluation

#### 16) Continual-ARC (detailed above) — Games/Reasoning-adjacent benchmark
- Also relevant to **game-like skill acquisition and evaluation**: unified scoring of memory-based and weight-based learners on recurring ARC tasks with memorization/generalization split. See Section 3, item 11.

#### 17) PARLEY: Cooperative Asymmetric Puzzle Collaboration (from 2026-11-12 arXiv window, context from sibling digest)
- **Title (EN / 中文):** PARLEY: Cooperative Asymmetric Puzzle Collaboration / 《PARLEY：合作非对称谜题协作基准》
- **Authors:** (See arXiv 2611.14242)
- **Affiliation:** Not specified in metadata snippet reviewed in sibling digest.
- **Venue:** arXiv 2026-11 (cs.AI/cs.CL/cs.MA context in recent listing ecosystem)
- **Abstract & key innovations:** Benchmark for cooperative asymmetric information puzzle solving requiring communication and coordination.
- **Comparison/results (author-reported):** 60.5% → 70.5% with intervention strategies (as reported in recent wiki arXiv daily).
- **Links:** https://arxiv.org/abs/2611.14242 · https://arxiv.org/pdf/2611.14242

> Note: Item 17 included for coverage of requested "games/agent systems/benchmarks" category based on verifiable recent arXiv signal already tracked in today’s wiki context; detailed affiliation/method numbers should be confirmed from PDF for formal citation.

---

## 5. Cross-Cutting Trends Observed (2026-11-12 window)

- **Generative rec/ads moving to production systems:** ByteDance SepLRM and large-scale serving work (RecoGEM) emphasize KV-cache reuse, transfer, and runtime/engine co-design; Taobao Shangou TS-GEAR encodes hard geo constraints directly in generative retrieval.
- **Latency-aware CTR/semantic modeling:** SlimFM shows structured pruning + field-aware adaptation can bring LLM semantics closer to online CTR latency budgets.
- **Advertising evaluation for LLM-native surfaces:** CHO-Bench formalizes ad-side context-hint optimization and highlights ranker-dependent strategy effects.
- **Agent training/eval becoming more realistic:** AutoScaffold targets experience-to-guidance conversion; ARE-bench stresses messy in-progress workspaces; Continual-ARC compares memory vs weight-based lifelong learners.
- **Sequential/POI quality via hierarchy and decoupling:** SHARP and LUMIR combine temporal/multimodal structure with reusable representations and agentic/memory components.
- **Recommendation explainability:** CIKM 2026 work demonstrates LLM-mediated narrative explanations over counterfactual edits with preference optimization.

---

## 6. Target-Lab Coverage Notes (requested focus)

| Requested org/lab | Verifiable papers in this digest/window | Notes |
|---|---|---|
| **ByteDance** | SepLRM (deployment/A-B tests stated at ByteDance) | Strong rec foundation-model/systems signal. |
| **Alibaba / Taobao (Taobao Shangou)** | TS-GEAR | Production generative ad retrieval in local-commerce search ads. |
| **Google DeepMind / OpenAI / Meta AI / Microsoft Research / Tencent / Kuaishou / Baidu / Netflix / NVIDIA / Anthropic / Apple / Amazon** | No newly verified first-party paper in today’s fetched arXiv/conference subset with complete metadata matching all requested fields | Absence here reflects this run’s limited access (no websearch, partial proceedings crawl), not a claim of no publications. Recommend follow-up via vendor blogs, OpenReview, and conference program pages. |

---

## 7. Gaps and Follow-up Actions

- **Proceedings gaps:** AAAI 2026, CVPR 2026, ACL 2026, EMNLP 2025 (recheck), SIGIR 2026 full program, WWW 2026, CIKM 2025/2026 full lists, KDD 2026 full lists, and complete ICML/ICLR 2026 accepted-paper metadata were not exhaustively crawled in this run.
- **Affiliation metadata gaps:** Several arXiv papers omit structured affiliations; verify author institutions from PDFs before downstream use.
- **Metric verification:** All reported gains (CTR/CVR/revenue/throughput/accuracy/latency) are author-reported; independent reproduction not performed.
- **Suggested next crawl targets:** conference OpenReview APIs/pages, official proceedings PDFs, arXiv queries filtered by company/lab names, and KDD/RecSys/SIGIR/WWW industry-track programs for ads/recs/CTR.

*Compiled for the karpathy-wiki synthesis pipeline on 2026-11-12 (EXTEND.md active).*
