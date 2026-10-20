---
title: "Conference Digest — RecSys 2026 Awards & Venue-Tagged Fresh Papers (2026-10-20)"
type: synthesis
created: 2026-10-20
updated: 2026-10-20
sources: [recsys-awards-page, arxiv-abs-pages, arxiv-html-pages, acm-dl-pages]
tags: [conference-digest, RecSys2026, EMNLP2026, SIGIR-AP2026, NeurIPS2026, ICLR2026, CIKM2026, MICRO2026, ICTAI2026, WASP2026, APSEC2026, recommendation, generative-recommendation, semantic-ids, agents, retrieval, scaling-laws, evaluation, benchmarks, top-labs, daily-digest]
---

# Conference Digest — RecSys 2026 Awards & Venue-Tagged Fresh Papers (2026-10-20)

> **Date:** 2026-10-20 · **Type:** incremental conference / award + venue-tagged edition
> **Window:** **RecSys 2026 official awards** (conference Sep 28 – Oct 2, Minneapolis; awards page re-fetched this run) plus arXiv papers submitted **2026-10-14 → 2026-10-16** (cs.IR pool + recommendation-adjacent cs.LG) that are **new to the wiki**.
> **Relation to siblings:** the full venue-by-venue editions are [`2026-10-17/conference-digest.md`](../2026-10-17/conference-digest.md) and [`2026-09-11/conference-digest.md`](../2026-09-11/conference-digest.md); the award-gap edition is [`2026-10-19/conference-digest.md`](../2026-10-19/conference-digest.md) (AAAI/SIGIR/ACL/EMNLP-2025/WWW/CIKM/KDD/NeurIPS-2025 — it carried **no RecSys 2026 awards**). Same-day siblings own their lanes: [`arxiv-daily.md`](arxiv-daily.md) (rec/ads/CTR/sequential — TransX, WeGR, SAHL, HASTE, OneChord…), [`arxiv-ai-search.md`](arxiv-ai-search.md) (LLM/agents/games — IGPO, ToolOPD, StopLoss, CHSM8…), [`arxiv-paper-check.md`](arxiv-paper-check.md) (CATH, ClueFlow, KV-Surgeon…), [`game-rl-daily.md`](game-rl-daily.md), [`tech-report-digest.md`](tech-report-digest.md). **This edition's unique lane:** the RecSys 2026 award suite (first wiki coverage), venue-tagged fresh preprints (EMNLP/SIGIR-AP/NeurIPS/ICLR/CIKM/MICRO…), and a top-lab industry radar (Meta / Google / Netflix / Amazon / Disney / Microsoft / ByteDance / Kioxia).
> **Method:** official RecSys awards page re-fetched (`recsys.acm.org/recsys26/awards/`); arXiv Export API was **hard rate-limited all run** (same wall as siblings) → paper pool built from a pre-limit `cs.IR` (150) + recommendation-adjacent `cs.LG` (60) harvest for Oct 14–19, then per-paper `arxiv.org/abs` + `arxiv.org/html` fetches for abstracts, author blocks and stated affiliations; targeted web searches for award-paper arXiv IDs. Every featured ID `grep`-verified at **0 hits** in `wiki/` before writing.
> **Language:** sources English → body English; Chinese titles as `title-zh`.

---

## 1. RecSys 2026 (Minneapolis, Sep 28 – Oct 2, 2026) — official awards, first wiki coverage

Re-fetched from the official awards page this run. Grep-verified **0 wiki hits** for "Epistemic Recommendation", "GenPage", "Value-Aligned Modeling", "On Reranking Space for Multi-Tenant Retrieval" and "Which LLM to Fine-Tune"; the Best Student Paper (`2602.05663`) and the Google semantic-ID honorable mention (`2607.24865`) are already on file — the **award** is the new fact for those two.

### 1.1 Best Paper — There's Something About You: Epistemic Recommendation for Latent Interest Discovery

- **Title (zh):** 关于你的一切：面向潜在兴趣发现的 Epistemic 推荐
- **Authors:** Daniel Nemirovsky, Priya Khokher, Adarsh Jois, Marco Zagha, Joaquin Delgado
- **Affiliation:** **Disney, USA** (stated on the awards page)
- **Venue:** RecSys '26 **Best Paper Award** (main track; award committee chaired by Xavier Amatriain et al.)
- **Abstract & key innovations:** ⚠️ *title-level only* — no arXiv preprint found (targeted search this run) and the ACM abstract page was not read in full. The title positions the paper on **latent interest discovery** via "epistemic" (uncertainty/knowledge-aware) recommendation — i.e., surfacing interests the user has not yet expressed through interaction history.
- **Comparison with prior methods:** not assessable from the title alone *(single-source: official awards page)*.
- **Links:** https://doi.org/10.1145/3773078.3831822 (pp. 544–553) · awards page below

### 1.2 Best Student Paper — Coarse-to-Fine Long-term Interest Modeling for Generative Recommendation (GLASS)

- **Title (zh):** 生成式推荐的由粗到细长期兴趣建模
- **Authors:** Shiteng Cao, Junda She, Ji Liu, Bin Zeng, Chengcheng Guo, Kuo Cai, Qiang Luo, Ruiming Tang, Han Li, Kun Gai, Zhiheng Li, Cheng Yang (12 authors)
- **Affiliation:** **Tsinghua University, Beijing University of Posts and Telecommunications, Kuaishou Inc.** (stated on the awards page); senior authors Ruiming Tang / Han Li / Kun Gai align with the GLASS / generative-rec line
- **Venue:** RecSys '26 **Best Student Paper Award**; arXiv v2 (23 Jul 2026); ACM DOI `10.1145/3773078.3831769`
- **Abstract & key innovations:** GLASS injects long-term user interests into the generative process in two places: **SID-Tier** maps the long-term interaction history into one unified interest vector that improves the prediction of the *initial* SID token (exploiting the compact semantic codebook to form cross features between history and candidate codes — unlike full retrieval models that struggle with the massive item space), and **semantic hard search** uses the generated coarse-grained SID as a dynamic key to pull relevant history, fused via an adaptive gate to recalibrate subsequent fine-grained token generation. Sparsity of the hard-search signal is countered by semantic-neighbor augmentation and codebook resizing. Evaluated on **TAOBAO-MM and KuaiRec**; code public.
- **Comparison with prior methods:** vs TIGER-style autoregressive generative recommenders that condition only on the recent truncated sequence — targets the long-history problem directly inside SID decoding; reports significant gains over SOTA baselines on both datasets (magnitudes not stated in the abstract).
- **On-file note:** the paper itself has been covered since **2026-05-24** (`arxiv-daily`), re-featured in [`2026-07-17/conference-digest.md`](../2026-07-17/conference-digest.md) §13.10, and again 07-22/07-27/07-28 — this run adds only the RecSys '26 award.
- **Links:** https://arxiv.org/abs/2602.05663

### 1.3 Best Industry Paper — A Framework for Value-Aligned Modeling and Robust Experimentation

- **Title (zh):** 价值对齐建模与稳健实验的框架
- **Authors:** Krishna Harsha Reddy Kothapalli, Angela Liu, Kamal Nayan Reddy Challa, Pavithra Seshadrivijayakrishnan, Yongpeng Yang, Mustafa Ispir
- **Affiliation:** **Google, USA** (stated on the awards page)
- **Venue:** RecSys '26 **Best Industry Paper Award**
- **Abstract & key innovations:** ⚠️ *title-level only* — no arXiv preprint found this run. The title couples **value-aligned modeling** (optimizing recommender objectives against declared business/user values rather than a single proxy metric) with **robust experimentation** (A/B infrastructure that remains reliable under the resulting multi-objective constraints).
- **Comparison with prior methods:** not assessable from the title alone *(single-source: official awards page)*.
- **Links:** official awards page (§8)

### 1.4 Honorable mentions (4)

| Track | Paper / title-zh | Authors (lead) | Affiliation | Link & status |
|-------|------------------|----------------|-------------|---------------|
| Main | **On Reranking Space for Multi-Tenant Retrieval with Adapted Queries** / 面向多租户检索之改编查询的重排空间 | Jun Woo Chung, Weijie Zhao | Rochester Institute of Technology, USA | DOI `10.1145/3773078.3831880`-adjacent proceedings entry; **no arXiv found**; title-level *(single-source)* |
| Industry | **GenPage: Towards End-to-End Generative Homepage Construction at Netflix** / Netflix 端到端生成式首页构建 | Lequn Wang, Jiangwei Pan, Linas Baltrunas (awards-page list); arXiv v3 adds Fengdi Che | **Netflix, USA** | https://arxiv.org/abs/2606.31031 — **expanded below, new to wiki** |
| Industry | **Tokens are All You Need: Dual-Purpose Semantic IDs for Achieving LLM-Level I/O Efficiency in Recommendation Systems** / 你只需要 Token：双用途 Semantic ID 实现推荐系统的 LLM 级 I/O 效率 | Baolei Li, Yiping Yuan, Yilin Zheng, Likang Yin, Ling Liu, Fabio Soldo, Romer Rosales, Xinyang Yi, Lichan Hong | **Google, USA** | https://arxiv.org/abs/2607.24865 — **already on file** (`2026-07-29/arxiv-ai-search`, `2026-07-31/arxiv-daily`) |
| Industry | **Which LLM to Fine-Tune? Agent-Driven Model Selection at Scale** / 微调哪个 LLM？大规模 Agent 驱动的模型选择 | Chen Luo, Yulin Liu, Yi Liu, Xuejing Lei, Yuchen Yan, Xin Zhang, Huimin Zeng, Hongda Mao, Monica Cheng | **Amazon Search / Amazon, Palo Alto & Seattle** (stated on ACM DL) | DOI https://doi.org/10.1145/3773078.3831880 (pp. 1673–1681); **no arXiv found** — expanded below |

**GenPage (expanded):**
- **Title (zh):** 见 §1.4 table
- **Abstract & key innovations:** replaces Netflix's traditional **multi-stage recommender stack with a single transformer**: the user + request context is the prompt, and the model autoregressively generates the entire structured, multi-row homepage as the response. Adapts the LLM recipe — pretraining on production pages, then post-training via weighted binary classification (WBC) or RL — plus industry-serving techniques for cold start, model freshness, business-rule enforcement and serving efficiency.
- **Results:** online A/B vs a mature, highly optimized production homepage recommender: **substantial lift on the core launch-decision engagement metric and −20% end-to-end serving latency**. Two offline findings: **enriching the prompt beats scaling model capacity** in the current regime, and **RL post-training increases homepage diversity although diversity is not in the objective**.
- **Comparison with prior methods:** vs the retrieval → ranking → assembly pipeline (and vs the wiki's earlier Netflix scaling work [[papers/recommendation/netflix-generative-recommender-scaling|Netflix generative-recommender scaling]]) — this is the full-stack replacement claim, in production A/B. It is the strongest award-lane evidence yet for the wiki's end-to-end generative-rec thread ([[papers/recommendation/hstu-generative-recommendation|HSTU]], [[papers/recommendation/thinkrec|ThinkRec]]).
- **Notes:** arXiv comment field states "another version of the paper with a different author list was accepted at ACM RecSys 2026" — author lists differ accordingly (see table). Grep-verified 0 wiki hits.
- **Links:** https://arxiv.org/abs/2606.31031

**AgentRec / "Which LLM to Fine-Tune?" (expanded):**
- **Key innovations:** formulates **LLM selection for fine-tuning as a multi-stage recommendation problem**, drawing explicit parallels to industrial retrieval-and-ranking stacks — i.e., the recommender's own toolkit solves the model-zoo selection problem. Production case study at Amazon: **60× reduction in model selection time** across multiple customer-facing LLM systems; deployed as **AgentRec**.
- **Comparison with prior methods:** vs ad-hoc benchmark-and-guess model selection — turns an "implementation choice" into a ranked, retrievable decision. ⚠️ **Name collision:** unrelated to `AgenticRec` ([arXiv 2603.21613](https://arxiv.org/abs/2603.21613), a recommendation-oriented agentic framework with tool-integrated reasoning) — different paper, different authors.
- **Links:** https://doi.org/10.1145/3773078.3831880

### 1.5 Award-suite shape

Five of seven paper awards/honors go to **industry-authored production systems** (Disney, Netflix, Google ×2, Amazon) and the student paper to a **generative-recommendation** system with production-scale datasets — the suite reads as RecSys'26 ratifying the end-to-end / generated-artifacts pipeline over retriever+ranker ensembles (see §6.1).

---

## 2. Venue-tagged fresh preprints — new to the wiki

Every ID below grep-verified at 0 hits in `wiki/` before writing; affiliations are **stated** from `arxiv.org/html` author blocks unless marked *(inferred)*.

### 2.1 EMNLP 2026 Main (2)

#### 2.1.1 MEMORA: A Memory-Enhanced Multimodal Committee Reranking Agent for Reasoning-Intensive Retrieval
- **Title (zh):** MEMORA：面向推理密集型检索的记忆增强多模态委员会重排 Agent
- **Authors:** Mohamed Mahmoud, Mostafa Farouk Senussi, Mahmoud Abdalla, Mahmoud SalahEldin Kasem, Abdelrahman Abdallah, Hyun Soo Kang
- **Affiliation:** **Chungbuk National University** (Korea; corresponding Hyun Soo Kang) + Abdelrahman Abdallah — **University of Innsbruck** (stated)
- **Venue:** arXiv comments field: **"Accepted at EMNLP Main 2026"**; cs.CL/cs.IR window 15–16 Oct 2026
- **Abstract & key innovations:** three-part agent for multimodal reasoning-intensive retrieval: (1) **Collaborative Factor-Committee Reranking** decomposes the query into intent factors, extracts factor-specific evidence into a structured matrix, and synthesizes a verdict through a memory-conditioned meta-verdict model; (2) an **Episodic Memory Module** tracks factor outcomes across queries and re-weights priorities at inference time; (3) a **Reasoning-Aware Dense Retriever** fine-tuned with chain-of-thought augmentation on **20k+ reasoning-intensive pairs**.
- **Comparison with prior methods:** vs monolithic rerankers and query-isolated agentic pipelines — on **MM-BRIGHT across 29 domains**: nDCG@10 **41.5** (text-to-text) and **38.9** (multimodal query-to-text), **+8.3 / +7.9 points** over the strongest agentic text-only / multimodal baselines.
- **Links:** https://arxiv.org/abs/2610.25282 · https://github.com/HarnessLab/MEMORA

#### 2.1.2 EmbDivBench: Measuring Data Diversity with Embeddings — A Taxonomy and Benchmark for Diversity Measures
- **Title (zh):** 用 Embedding 度量数据多样性：多样性度量的方法分类与基准
- **Authors:** Cantao Su, Anna Wegmann, Esther Ploeger, Dong Nguyen
- **Affiliation:** **Utrecht University**, The Netherlands (stated)
- **Venue:** arXiv comments field: **"Accepted to EMNLP 2026 (Main)"**
- **Abstract & key innovations:** first systematic treatment of embedding-based diversity measurement: a **taxonomy of 21 measures in four families** + **EmbDivBench** evaluating them along three components — **variety, balance, disparity** — on simulated and natural text.
- **Comparison with prior methods:** the dominant measure (**Mean Pairwise Distance**) is outperformed by several alternatives; **Graph Entropy is best overall** — a concrete "the default metric is the wrong metric" result, distilled into practical selection guidance. Connects to the wiki's data-curation/measurement thread.
- **Links:** https://arxiv.org/abs/2610.24888 · https://github.com/nlpsoc/EmbDivBench

### 2.2 SIGIR-AP 2026 + APSEC 2026 (2, same Luxembourg group)

#### 2.2.1 VisR-RAG-Fin: Benchmarking Multimodal RAG over Visually Rich Financial Documents
- **Title (zh):** VisR-RAG-Fin：视觉富集金融文档上的多模态 RAG 基准
- **Authors:** Omar El Bachyr, Laura Maria Bernardy, Saad Ezzini, Jacques Klein, Tegawendé F. Bissyandé, Charles Monté, Anas Zilali, et al.
- **Affiliation:** **University of Luxembourg** (Bissyandé/Klein/Klein-group) + **King Fahd University of Petroleum and Minerals** (Saad Ezzini) (stated)
- **Venue:** arXiv comments field: **"Accepted at the main research track of ACM SIGIR-AP 2026, Singapore, December 13–15, 2026"**
- **Abstract & key innovations:** open-source benchmark for **page-level QA over visually rich financial documents** built by a general pipeline that preserves original layout and visual content; systematic study of retrieval+generation behavior under **text-only, multimodal, and hybrid** configurations.
- **Comparison with prior methods:** vs RAG benchmarks built from text-extracted corpora — enterprise documents are dense-text + tables + charts + layout, and prior work lacks a component-level analysis of which design choices move end-to-end performance.
- **Links:** https://arxiv.org/abs/2610.24822

#### 2.2.2 RAGit: Turning Document Preprocessing into an Experimental Variable for RAG *(tool demo)*
- **Title (zh):** RAGit：把文档预处理变成 RAG 的实验变量
- **Authors:** Omar El Bachyr, Saad Ezzini, Tegawendé F. Bissyandé, Jacques Klein
- **Affiliation:** as above (Luxembourg / KFUPM, stated)
- **Venue:** arXiv comments field: **"Accepted at the Tool Demonstration Track of APSEC 2026"** (4 pages)
- **Abstract & key innovations:** open-source workbench representing **parsing → chunking → indexing → retrieval → evaluation** as configurable experimental stages with everything downstream held fixed; preserves chunk→page provenance and maps heterogeneous retrieval units to a common page-level ranking for scoring.
- **Comparison with prior methods:** preprocessing choices are normally picked heuristically and compared across inconsistent setups; RAGit makes them an explicit variable (supports multiple parsers/chunkers, dense and late-interaction retrieval).
- **Links:** https://arxiv.org/abs/2610.24659 · https://github.com/OmarElbachyr/ragit

### 2.3 NeurIPS 2026 (3: 1 Datasets & Benchmarks + 2 workshops)

#### 2.3.1 KNN Implementation Details Can Dramatically Change Performance: An Example from Cover Trees (RustKNN)
- **Title (zh):** KNN 实现细节会显著改变性能：以 Cover Tree 为例
- **Authors:** Amol Khanna, Edward Raff
- **Affiliation:** **CrowdStrike** (both) + Edward Raff also **UMBC / Syracuse University** (stated)
- **Venue:** arXiv comments field: **"40th Conference on Neural Information Processing Systems (NeurIPS 2026), Track on Evaluations and Datasets"**
- **Abstract & key innovations:** a unified Rust implementation (**RustKNN**) of three Cover-Tree construction variants × three query modes, used to show that implementation choices — rarely reviewed in algorithm papers — can flip the conclusions of algorithm comparisons. Findings: optimal query strategy depends on `k` and dataset (wrong query mode costs up to **7.5× runtime**); the cover-tree base parameter **1.3 (practice) vs 2 (theory) is not a safe default** for dual-tree search (1.3 optimal on only 1/7 datasets; 1.6× slower than optimum on covtype); of five micro-optimizations only early-exit distance computation is consistent (**none at d=32, 1.31× at d=54, 1.49× at d=784**); all-NN vs held-out benchmarks yield different implementation rankings. Medians over 20 allocations with bootstrap 95% CIs.
- **Comparison with prior methods:** vs algorithm papers that benchmark one canonical implementation — the paper's point is that "algorithm A beats B" claims are confounded by tuning of `k`/base/query-mode; resonance with the wiki's re-evaluation/benchmark-rigor thread.
- **Links:** https://arxiv.org/abs/2610.16940 · https://github.com/CrowdStrike/RustKNN

#### 2.3.2 Shortcut Sensitivity in Agent-Safety Evaluations *(NeurIPS 2026 workshops TAE + AIWILD)*
- **Title (zh):** Agent 安全评估中的捷径敏感性
- **Authors:** Hasan Demirkiran, Jens Ernstberger · **Affiliation:** not stated on abs page
- **Venue:** NeurIPS 2026 workshops **TAE (Can We Trust AI Evaluation?)** and **AIWILD**
- **Abstract & key innovations:** three-level shortcut-auditing framework (label predictability / observational guard association / paired decision sensitivity) applied to LinuxArena and TS-Bench-derived guard datasets. Concrete effects: shorter shell commands strongly predict trajectory labels; exact-tool lookup F1 falls **.901 → .495** under domain holdout (AgentDojo-Traj); rewriting an `<INFORMATION>` marker changes blocking by **−8.33 pp** and opaque tool aliases by **+11.46 pp** with no change to the construct being measured.
- **Comparison with prior methods:** vs guard evaluations scored on single fixed representations — benchmark *presentation* materially changes both guard decisions and measured accuracy; recommends domain-group holdouts, evaluation-unit metrics, placebo-controlled paired interventions.
- **Links:** https://arxiv.org/abs/2610.22243

#### 2.3.3 CoBe: A Benchmark for Conversational Counterfactual Text Editing *(NeurIPS 2026 workshops AI4GOOD + TAE)*
- **Title (zh):** CoBe：对话式反事实文本编辑基准
- **Authors:** Arvind Raghavan, Inwoo Hwang, Shreyas Havaldar, Kai-Zhan Lee, Aurghya Maiti, Yushu Pan, Jeffrey Wu, Mingxuan Li et al. · **Affiliation:** not stated on abs page
- **Venue:** NeurIPS '26 workshops **Trustworthy AI For Good** and **Trustworthy AI Evaluations**
- **Abstract & key innovations:** **2,000 zero-shot items** (healthcare, science/engineering, business, everyday) separating genuine counterfactual editing from mere **associational generation** — keeping facts unaffected by a hypothetical change fixed while rewriting only consequences.
- **Comparison with prior methods:** prior counterfactual-text datasets don't separate the two reasoning modes; frontier systems average only **58.05%**, defaulting to associational generation, and performance **does not scale consistently with model size or output length** — pointing at training objectives, not capacity.
- **Links:** https://arxiv.org/abs/2610.13057

### 2.4 ICLR 2026 Oral (1)

#### 2.4.1 Compactness and Consistency: A Conjoint Framework for Deep Graph Clustering (CoCo)
- **Title (zh):** 紧凑性与一致性：深度图聚类的联合框架
- **Authors:** Wei Ju, Siyu Yi, Kangjie Zheng, Yifan Wang, Ziyue Qiao, Li Shen, Yongdao Zhou, Xiaochun Cao et al. · **Affiliation:** not stated on abs page
- **Venue:** arXiv comments field: **"ICLR 2026 Oral"** — verified this run at the official ICLR virtual oral listing (Rio de Janeiro conference series)
- **Abstract & key innovations:** graph-convolutional filters learn node representations from local + global views, encoded into **low-rank compact embeddings** (removing redundancy/noise), plus a **consistency-learning** strategy over the compact embeddings to transfer knowledge between the two views.
- **Comparison with prior methods:** vs GNN message-passing that misses global relationships and yields non-compact, noisy representations — SOTA on multiple deep-graph-clustering datasets. Included on **oral status**; graph clustering sits outside the wiki's core lanes *(venue-tagged, light coverage)*.
- **Links:** https://arxiv.org/abs/2610.11506

### 2.5 CIKM 2026 workshop (1)

#### 2.5.1 SearCl: Dialogue Generation for Conversational Recommendation Using User Search Interactions and Knowledge Graphs
- **Title (zh):** SearCl：基于用户搜索交互与知识图谱的对话式推荐对话生成
- **Authors:** Minsung Hwang, Donggyu Yoon, Gowoon Hwang, Kwanghee Jang, Joyce Jiyoung Whang
- **Affiliation:** not stated on abs page; senior author Joyce Jiyoung Whang — **Seoul National University** *(inferred)*
- **Venue:** arXiv comments field: **"The 3rd Workshop on Evaluating and Applying Recommender Systems with Large Language Models (EARL) at CIKM 2026"**
- **Abstract & key innovations:** automatically generates conversational-recommendation dialogues grounded in real search/click behavior: session segmentation derives targets from post-query content, a **configurable probabilistic state machine** controls dialogue flow, and two LLM agents (seeker / recommender) speak under turn-level constraints, with recommendation supported by **KGs built from item metadata**. Output: **3,538 dialogues over 1,731 unique target items**.
- **Comparison with prior methods:** vs manually authored/annotated conversational-rec datasets — LLM-as-judge quality scores exceed existing benchmarks without human annotation.
- **Links:** https://arxiv.org/abs/2610.25182

### 2.6 Other venue tags in this window (pointer table — full entries in §4.4)

| Paper | Venue (from its own comment field) | Entry |
|-------|-------------------------------------|-------|
| ARMED: Adaptive Retrieval-Augmented Medication Recommendation | **ICTAI 2026** | §4.4 |
| Local Citation Recommendation Without Graph Signals (LCRC) | **WASP 2026**, co-located with AACL-IJCNLP 2026 | §4.4 |
| Architecting for Hardware Diversity (Meta, AMD) | **MICRO 2026** (59th IEEE/ACM Int. Symp. on Microarchitecture) | §3.3 |

---

## 3. Top-lab radar — industry papers new to the wiki

### 3.1 Meta — Predictable Scaling: Efficient Model Exploration via Scaling-Law Prediction

- **Title (zh):** 可预测的 Scaling：用缩放定律预测实现高效模型探索
- **Authors:** Aishwarya Wesanekar, Sheng-Tao Yang, Jiawei Zhang, Flavio Sales Truzzi, Chen Chen, Nader Beigiparast, Shengyuan Huang, Roshanak Zilouchian Moghaddam, …, Sebastian Ament, Jihao Andreas Lin, Vincent Huang, Kai Han, Boyi Jiang, Wenlin Chen, Chaorong Chen, Ashwin Kumar, Maximilian Balandat, David Eriksson, Yifei Zhang, Pan Zhong (23 authors)
- **Affiliation:** **Meta Platforms, Inc.** (every author block in the HTML version; stated)
- **Venue:** arXiv preprint, submitted **16 Oct 2026** (cs.LG); no conference tag
- **Abstract & key innovations:** hypothesis-evaluation framework for **recommendation models**: build scaled-down proxies via composable scaling functions along distinct resource axes, then project metrics to target scale by curve fitting with calibrated uncertainty. Three prediction strategies of increasing expressiveness — even the **raw proxy stays within the empirical noise floor of repeated-run variance**; a Gaussian Process adds an indicative **15% relative MAE improvement** plus calibrated uncertainty.
- **Comparison with prior methods:** vs full-scale training runs consuming thousands of GPU-hours per hypothesis. Evaluated on two ranking models — a task-specific model (**TS-1**) and a foundation model (**FM-1**) — PS **correctly ranks actionable hypotheses** while cutting **trainers 86% / 88%** and **samples 80% / 50%** respectively: **79–88% compute reduction** overall (verified in the paper's own §4/§5 text). Continues Meta's scaling-law line for rec ([[papers/recommendation/understanding-scaling-laws-rec|Understanding Scaling Laws for Recommendation Models]]).
- **Links:** https://arxiv.org/abs/2610.23453

### 3.2 Meta Superintelligence Labs + KAIST — Learning to Program Retrievals (RPL)

- **Title (zh):** 学会编写检索程序：用 RL 组合搜索原语
- **Authors:** Kyuyoung Kim, Zilin Xiao, Zhiyuan Wang, Avinash Atreya, Ke Yang, Jinwoo Shin, Kecheng Hao
- **Affiliation:** **Meta Superintelligence Labs** (Xiao, Wang, Atreya, Yang, Hao; Kim "work done at Meta") + **KAIST AI** (Kim, Shin) (stated)
- **Venue:** arXiv preprint (cs.IR, window 15–16 Oct 2026); no conference tag
- **Abstract & key innovations:** **Retrieval Program Learning** — a policy composes search primitives into *executable programs* with local state and control flow, decoupling retrieval breadth from context consumption. Exploration problem (sparse reward over multi-step programs) is addressed by **program mutation**: grammar-constrained, execution-verified local variants of suboptimal sampled programs are converted into training trajectories and distilled back into the policy.
- **Comparison with prior methods:** vs fixed pipelines and collections of atomic tools (ReAct-style single-call loops): on open-domain QA, **a 4B model trained with RPL outperforms all 8B baselines**, with the largest gains on multi-hop tasks; on corpus-level reasoning it takes the top answer-F1 **and** document-coverage F1 for both sizes while cutting context consumption and retrieval turns.
- **Links:** https://arxiv.org/abs/2610.24854

### 3.3 Meta — Architecting for Hardware Diversity: End-to-End Co-Design for AI Training on AMD GPUs

- **Title (zh):** 应对硬件多样性：Meta 高性能 AI 训练的端到端协同设计
- **Authors:** Haoyu Zhang, Arshad Rahman, Adnan Aziz, Ajith Prabhudev, Amin Farmahini, Ben Rhoads, Benson Ma, Brian Shi et al.
- **Affiliation:** **Meta** (stated throughout the abstract)
- **Venue:** arXiv comments field: **"To appear in the 59th IEEE/ACM International Symposium on Microarchitecture (MICRO 2026)"**
- **Abstract & key innovations:** Meta's heterogeneous fleet (NVIDIA + AMD + MTIA) forced portability work off the NVIDIA-optimized path; case study **AMD Instinct MI350X vs NVIDIA B200 for recommendation-model training**. Three reusable principles: (1) **hardware-model co-design** — revise model structure and software recipes instead of direct ports (exploiting MI350X's **1.6× HBM** vs B200); (2) an **analytical performance model** giving zero-warmup optimal kernel selection across datatypes/shapes; (3) **agentic workflows extended to microarchitecture-aware kernel optimization and custom shim generation**.
- **Comparison with prior methods:** vs directly ported CUDA-baseline training — **up to 1.5× end-to-end training throughput**; claimed **first hyperscaler report on productionizing AMD GPUs for large-scale training**; contributions upstreamed to PyTorch / Triton / ROCm.
- **Links:** https://arxiv.org/abs/2610.22230

### 3.4 Microsoft Research India — Simple Linear Corrections for Compression in Late Interaction

- **Title (zh):** Late Interaction 压缩的简单线性校正
- **Authors:** Mihir Agarwal, Sabyasachi Basu, Viraj Agrawal (equal contribution note on first/third)
- **Affiliation:** **Microsoft Research India** (stated)
- **Venue:** arXiv preprint (cs.IR window 14–16 Oct 2026); no conference tag
- **Abstract & key innovations:** after document-vector compression in late-interaction (multi-vector) retrieval, learn a **global linear correction** to the scoring function by distilling the uncompressed model's score distributions over candidates — encoder and compressor stay frozen; the correction applies at query time or **once, offline, to stored vectors**.
- **Comparison with prior methods:** vs pooling/pruning compression that visibly degrades quality at aggressive budgets — evaluated with ColBERTv2 and Jina v4 on MS MARCO/BEIR and ColPali2 on ViDoRe v3: improves over baseline compression in **154 of 160** BEIR settings in-domain (MS MARCO→BEIR transfer more variable); synthetic-query corrections help on ViDoRe v3. Recovers quality **without retraining the encoder or recompressing**.
- **Links:** https://arxiv.org/abs/2610.14196

### 3.5 ByteDance + NTU — RemoteANN: Native Vector Search on Cloud Object Storage

- **Title (zh):** RemoteANN：面向云对象存储的原生向量搜索引擎
- **Authors:** Yutong Gou, Silu Huang, Yue Wang, Jianjun Chen, Cheng Long
- **Affiliation:** **Nanyang Technological University, Singapore** (Gou, Long) + **ByteDance, USA** (Huang, Wang, Chen) (stated)
- **Venue:** arXiv preprint (cs.DB/cs.IR window 15–16 Oct 2026); no conference tag
- **Abstract & key innovations:** index + query engine co-designed for object-store access patterns: **IVF + RaBitQ quantization** with inter-/intra-cluster reordering for locality; query side combines cluster pruning, fine-grained **Range-GET**, request merging, and local NVMe caching; **QGKMeans** removes the index-build bottleneck.
- **Comparison with prior methods:** vs disaggregated designs that keep only index metadata on compute nodes and pay network I/O amplification on the payload — at **97% target recall**: up to **5.9× throughput** with up to **16.1× fewer object-storage requests** than representative baselines.
- **Links:** https://arxiv.org/abs/2610.25172

### 3.6 Kioxia — AiSAQ-in-Filtering for DRAM-free Filtered Information Retrieval *(brief)*

- **Title (zh):** 无 DRAM 过滤检索的 AiSAQ 过滤增强
- **Authors:** Kento Tatsuno, Daisuke Miyashita, Kazunari Sumiyoshi, Hiroaki Yamanaka, Kosuke Nakata, Jun Deguchi · **Affiliation:** **Kioxia Corporation, Japan** (all, stated)
- **Venue:** arXiv preprint (5 pages, cs.IR)
- **Abstract & key innovations:** **LiPQ (Label-inclusive Product Quantization)** folds unstructured vectors *and* structured labels into one representation with no growth in encoded data, enabling filtered ANNS without DRAM blow-up.
- **Comparison with prior methods:** vs label storage alongside vectors — recall@1 up to **+55%** for single-label searches with fewer disk I/Os, while retaining AiSAQ's DRAM footprint reduction of up to **1/78** and fast index switching; also applicable to sparse-dense hybrid search.
- **Links:** https://arxiv.org/abs/2610.17627

### 3.7 Industry map of this run

| Lab | Item(s) | Where |
|-----|---------|-------|
| **Meta** | Predictable Scaling (rec eval, 79–88% compute cut) · RPL (programmatic retrieval, MSL) · MICRO'26 AMD co-design | §3.1–3.3 |
| **Google** | Best Industry Paper (value-aligned modeling) · "Tokens are All You Need" HM (already on file) | §1.3–1.4 |
| **Netflix** | GenPage HM — single-transformer homepage, −20% latency | §1.4 |
| **Amazon** | AgentRec HM — model selection as recommendation, 60× selection-time cut | §1.4 |
| **Disney** | Best Paper — Epistemic Recommendation | §1.1 |
| **Kuaishou / Tsinghua / BUPT** | Best Student Paper — GLASS | §1.2 |
| **Microsoft (India)** | Late-interaction compression corrections | §3.4 |
| **ByteDance / NTU** | RemoteANN object-store vector search | §3.5 |
| **Kioxia** | AiSAQ-in-Filtering | §3.6 |
| **CrowdStrike** | RustKNN (NeurIPS'26 D&B) | §2.3.1 |
| **Thomson Reuters** *(inferred)* | Query-adaptive WRRF study | §4.3 |

---

## 4. Fresh papers by lane (no top venue tag, or venue noted inline)

### 4.1 Agents, harnesses & agent evaluation (5)

- **ToolBottleneckBench** / 工具瓶颈基准 — Xu, Dong, Onizuka, Xiao — **University of Osaka + Initial S + Nagoya University** (stated) — arXiv [2610.21098](https://arxiv.org/abs/2610.21098). Measures tool-agent performance under **controlled pressures × fixed harness budgets**: synthetic enterprise tasks stay fixed while one pressure varies (tool catalog / visible menu / certified workflow / record encoding); an exact grader records the first unmet obligation and the harness limit that ended the episode. Across **21 model×harness configs**, the **visible tool menu is the only pressure with a large penalty**, and it tracks truncation at the completion cap (raising the cap 16× removes most of it); most failures end at a harness limit, and the failure record identifies the assigned pressure **no more reliably than a raw tool-call count**. *Prior-work contrast:* agent benchmarks usually attribute scores to the model alone — recommendation: always report pressure effects together with the harness budgets. https://github.com/zichuanxu/tool-bottleneck-bench
- **Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve (DKGI)** / 把知识图谱当文件用 — Yuyang Bai, Yu Wang, Yu Zhang — **Texas A&M + University of Oregon** (stated) — arXiv [2610.18616](https://arxiv.org/abs/2610.18616). Agents write Python directly over complete node/edge files (execution interleaved with shell search), so **tool creation and tool use co-evolve** under execution feedback instead of being constrained by predefined graph interfaces. Training-free DKGI beats the strongest published baseline by **≥6.7 Hit@1 on every graph** across three domains; ablations show multi-turn programming > shell-only and > predefined graph tools. https://github.com/leopoldwhite/DKGI
- **OpenSaC: A Python Library for Search as Code in Deep Research Agents** / 面向深度研究 Agent 的 Search-as-Code 库 — Qi Liu, Jiaxin Mao, Fengbin Zhu, Tat-Seng Chua, Ji-Rong Wen — **Renmin University of China + National University of Singapore** (stated) — arXiv [2610.25779](https://arxiv.org/abs/2610.25779). Operationalizes the **Search as Code** paradigm (agents write programs composing search, source reading, reranking, model calls, local processing) as a library + skill for existing coding agents. vs standard Codex with built-in web search: **less execution time and fewer model tokens** on BrowseComp and WideSearch, higher BrowseComp accuracy, slightly lower row F1 on WideSearch. https://github.com/liuqi6777/OpenSaC — third independent paper this window on program-shaped retrieval/agent work (with RPL §3.2, DKGI above); see §6.4.
- **AuditKIT: A Unified Evaluation Spine for LLMs and Agentic Systems** / 统一评估骨架 — Shreeyans Arora, Utsav Avaiya et al. — **Lexsi Labs** (stated in comments; work done while at Lexsi Labs) — arXiv [2610.22511](https://arxiv.org/abs/2610.22511). One result representation across benchmark accuracy, judging, runtime, tool-use and retrieval quality, with direction-aware metric contracts, configuration fingerprints, **turn-aware tool-call matching**, parallel-vs-sequential execution separation, verified outcomes vs trajectory diagnostics, and **unscored ≠ failure** semantics; seven case studies show answer extraction / runtime / metric selection change evaluation outcomes. https://github.com/Lexsi-Labs/AuditKIT
- **Measuring the Task Value of Precision Upgrades in Closed-Loop Agents** / 闭环 Agent 中精度升级的任务价值 — Sicheng Lyu, Xinyu Wang, Yu Gu, Lei Ding, Ziyang Song, Xiao-Wen Chang — affiliation not stated on abs page — arXiv [2610.24346](https://arxiv.org/abs/2610.24346). Argues a low-precision agent's fallback value = **tasks saved − tasks spoiled**, measured under the continuation that will actually run (paired branches from restored states). On Qwen3 agents with simulated 4-bit weights on τ²-bench: action-only BF16 rescues and damages **nearly cancel** (held-out telecom estimate negative); swapping in a *second 4-bit checkpoint* changes about as many outcomes as the BF16 action; reordering tool-argument keys changes outcomes despite identical executed calls; a frozen uncertainty trigger beats random on found-changes but not on net benefit. *A cautionary negative result against naive "more bits = better" routing.*

### 4.2 Code generation skills (1)

- **Code Skill Server (CSS): A Large-Scale Search Engine for Code Generation Skills** / 代码生成 Skill 的大规模搜索引擎 — Xiaoyong Li, Haolong Li, Dongliang Xu, Haoyu Li, Yifan Wang, Jingyuan Shi, Yanghua Wang, Yanbin Sun et al. — **Shandong University + Guangzhou University** (stated) — arXiv [2610.23186](https://arxiv.org/abs/2610.23186). A skill server that incrementally collects and indexes publicly available code-generation skills across heterogeneous sources (**CSS-993 corpus, 993 skills**); best configuration improves **Pass@1 by up to +13.91%**, with at least **+4.21%** for every model in cross-model evaluation. *Prior-work contrast:* existing skill-retrieval work only selects from established libraries; manual discovery does not scale as skills proliferate. https://github.com/haoyuli-sdu/CodeSkillServer — the code lane this window is **skill retrieval**, not code-execution prediction (that lane's newest items remain the 10-17 edition's DUET/CoRE/DexBench/SWE-Flux; see §5).

### 4.3 Retrieval & IR method studies (3)

- **Optimal Fusion Weights Form Intervals, Not Points: Query-Adaptive WRRF** / 最优融合权重是区间而非点 — Iris Ma, Zahra Shekarchi, Stuart Mcilroy, Mahtab Farrokh, Fattane Zarrinkalam, Joel Stremmel — affiliation not stated (**Thomson Reuters** *(inferred)* from the released code org) — arXiv [2610.24341](https://arxiv.org/abs/2610.24341). Eight dynamic fusion-weight strategies × four datasets × four sparse–dense retriever pairs: the **per-query optimal weight is typically an interval (sometimes multiple intervals), not a point**; **74/128** dynamic methods beat standard RRF after FDR correction; methods trade quality against latency, so the paper ships a tiered decision framework mapping constraints → method class. *Contrast:* query-aware fusion literature optimizes a point estimate. https://github.com/thomsonreuters/query-based-rrf
- **Graph-free Retrieval with Graph-Modified Embeddings** / 无图检索：图改写后的 Embedding — Federica Santi, Vasilije Marković, Daniel Scott, Lazar Obradović — affiliation not stated (senior author Lazar Obradović — Drexel *(inferred)*) — arXiv [2610.18410](https://arxiv.org/abs/2610.18410). Five **offline** graph-based embedding transformations used *without query-time graph access*; direct replacement of original embeddings hurts evidence recovery, while **multi-stage use** (graph-modified embeddings guide the search, originals keep semantic relevance) improves linked-fact/comparison recovery by up to **+25.9% relative** and matches baseline recovery with **40% fewer nodes**. Finding: *how* graph-modified embeddings are used matters more than how they are produced.
- **When Inputs Receive No Score: Evaluating Open-Web Event Admission on the Complete Stream** / 当输入拿不到分数：完整流上的开放网页事件准入评估 — Shengqi Zhou, Zhigang Liu, Wenxiang Zhu, Boyong Du, Kairui Yang, Haicheng Huang, Weijian Bu — affiliation not stated — arXiv [2610.17814](https://arxiv.org/abs/2610.17814). Six instruction-model backbones × three strategies × 602 human-annotated items: systems score **different populations with different class compositions**, so ranking comparisons must be made on shared inputs; score availability caps attainable retention (four configs score only 10/12 positives → a 90% full-stream target is unreachable by thresholding); Qwen under INT4 vs INT8 scores the **same count but different items**; more scores can **increase** false acceptance at fixed threshold. Ships a complete-stream protocol separating upstream score loss from decision loss.

### 4.4 Applied recommendation & citation (3)

- **ARMED: Adaptive Retrieval-Augmented Medication Recommendation** / 自适应检索增强用药推荐 — Kyungkeon Chung, Se Un Park, Hyejin Lee, Junyoung Park — affiliation not stated — arXiv [2610.16440](https://arxiv.org/abs/2610.16440) — comments: **"Accepted at ICTAI 2026"**. Clinical RAG that observes the initial retrieval outcome and **dynamically expands** (supplementary or fallback multi-query retrieval) when retrieval sufficiency is low, plus a **relevance gate** for same-patient history organizing evidence into structured query-level records; on **MIMIC-IV** it beats static retrieval baselines while running on **local small LMs without external APIs or task-specific fine-tuning**.
- **Local Citation Recommendation Without Graph Signals (LCRC)** / 无图信号的本地引用推荐 — Benjamin Basseri, Pavlos Protopapas, Kemeng Zhang, Alberto Accomazzi, Stephanie Jarmak, Anna Kelbert — affiliation not stated (**NASA ADS / Harvard CfA** *(inferred)* from the ADS-hosted dataset) — arXiv [2610.15832](https://arxiv.org/abs/2610.15832) — comments: **"Accepted at WASP 2026, co-located with AACL-IJCNLP 2026"**. New corpus of **14,735 scientific statements** from astrophysics review papers with full-text citation targets; retrieval that avoids citation-graph bias gains **+8.0% Recall@25 / +6.9% NDCG@25** over dense baselines **without fine-tuning**. https://github.com/benjaminb/citeline · dataset `adsabs/LCRC`.
- **MARS: A Momentum-Aware Adaptive Rating System for Personalized Assessment** / 动量感知自适应评分系统 *(one-liner)* — Vikrant Sahu, Khethavath Sunil Naik, Gagan Raj Gupta; affiliation not stated — arXiv [2610.21685](https://arxiv.org/abs/2610.21685): interpretable, momentum-aware rating updates + time-constrained routing for adaptive assessment, vs fixed difficulty labels and black-box proficiency predictors.

---

## 5. Cross-references — same-day siblings own these lanes

| Sibling (2026-10-20) | Lane it owns | Items not duplicated here |
|---|---|---|
| [`arxiv-daily.md`](arxiv-daily.md) | Rec / advertising / CTR / sequential / generative recommendation | TransX (sequence-transduction tech report), WeGR (WeChat generative retrieval), MAPS, AdCoEvo, DuoLM, SAHL, HASTE, OneChord, ReRankID, PerCDR |
| [`arxiv-ai-search.md`](arxiv-ai-search.md) | LLM post-training, agents, memory, games, ads (21 full details; 155 in-window papers) | IGPO, Adaptive Decoding, ToolOPD, StopLoss, MemDerive, UtilityBench; games lane C (CHSM8, RQA, Nash 1/3-barrier) |
| [`arxiv-paper-check.md`](arxiv-paper-check.md) | CTR / AI quick scan | CATH, A Cue's Hidden Price, ClueFlow, APSD, KV-Surgeon, Claim Laundering, MAPF-in-code-space |
| [`game-rl-daily.md`](game-rl-daily.md) | 7 game lanes | PEARL, LMAPF Shared Spatial Fields, Agentic World Modeling (4 new-to-wiki) |
| [`tech-report-digest.md`](tech-report-digest.md) | Lab tech reports | Microsoft "Securing the agentic insider", Mistral Timestral, Anthropic/METR |
| [`2026-10-17/conference-digest.md`](../2026-10-17/conference-digest.md) | Full venue-by-venue harvest + code-execution prediction lane | DUET, CoRE, DexBench, SWE-Flux — **no fresh code-execution-prediction paper in this window's pool** |

> ⚠️ **CTR-prediction lane:** [`arxiv-ai-search.md`](arxiv-ai-search.md) logs an **8th consecutive empty October window** for CTR-prediction papers (newest: ECC `2610.13066`, WeGR `2610.16979`). This run's cs.IR-heavy pool independently shows **no fresh CTR-prediction paper either** — two independent harvests agreeing. `[[ctr-scaling-landscape]]` gains no entrant today.

---

## 6. Cross-report observations

1. **The RecSys '26 award suite ratifies production pipelines.** Best Paper = Disney's latent-interest discovery; Best Industry = Google's value-aligned experimentation; honorable mentions = Netflix's single-transformer homepage, Google's dual-purpose semantic IDs, Amazon's model-selection-as-recommendation; Best Student = GLASS long-term-interest generative recommendation. Every honoree is an industrial *pipeline* paper, and the student award goes to generative recommendation — direct reinforcement of the wiki's end-to-end thread ([[papers/recommendation/hstu-generative-recommendation|HSTU]], [[papers/recommendation/thinkrec|ThinkRec]], §1.4 GenPage).
2. **GenPage's two offline findings are the digest's sharpest numbers:** *prompt enrichment > capacity scaling* in the current regime, and *RL post-training raises diversity though diversity isn't in the objective* — paired with Meta's Predictable Scaling (79–88% less eval compute, raw proxies already inside the noise floor), the frontier papers this window are about **inputs, scaffolding and measurement discipline**, not parameter count.
3. **Meta appears three times from three different angles** — rec-eval scaling (PS, §3.1), programmatic retrieval from Meta Superintelligence Labs (RPL, §3.2), and hardware portability with recommendation-model training as the case study (MICRO'26, §3.3). Recommendation work is the common denominator: Meta's rec stack is where its systems research is cashed out.
4. **Search-as-code / programs-as-tools is now a three-lab pattern in one week:** RPL learns programs (Meta/KAIST), OpenSaC ships a library+skill for coding agents (RUC/NUS), DKGI lets agents create graph tools over files (TAMU/Oregon) — all in fresh, non-overlapping venues. This is the retrieval-side face of [[concepts/agentic-engineering]].
5. **Measurement skepticism is this window's dominant result type** — RustKNN (implementation details flip KNN conclusions), EmbDivBench (the default diversity metric loses), ToolBottleneckBench (scores are harness-budget artifacts), WRRF (optimal weight is an interval, not a point), Shortcut Sensitivity (benchmark *presentation* moves guard decisions), event-admission (unscorable inputs cap achievable metrics). It extends the 10-19 edition's "awards reward measuring the thing" observation into ordinary papers.

---

## 7. Flags & uncertainty

- ⚠️ **No arXiv / abstract not read (title-level, single-source: official awards page):** Epistemic Recommendation (Disney, §1.1), Value-Aligned Modeling (Google, §1.3), On Reranking Space for Multi-Tenant Retrieval (RIT, §1.4). AgentRec (Amazon) has no arXiv either but its ACM-DL abstract excerpts were readable (60× figure comes from there).
- ⚠️ **Name collision:** Amazon's **AgentRec** (RecSys '26) ≠ `AgenticRec` [arXiv 2603.21613] (unrelated authors/paper).
- ⚠️ **GLASS award ≠ new paper:** `2602.05663` has been on file since 2026-05-24 (six wiki hits) — only the RecSys '26 Best Student Paper award is new. Same for `2607.24865` ("Tokens are All You Need"), covered 2026-07-29/31.
- ⚠️ **GenPage author lists differ** between arXiv (4 authors incl. Fengdi Che) and the RecSys version (3 authors); the paper's own comment field acknowledges "a different author list".
- ⚠️ **Harvest coverage:** Export API was rate-limited for the entire run → the paper pool is a **pre-limit cs.IR (150) + rec-adjacent cs.LG (60) harvest for Oct 14–19**; no cs.AI / cs.CL / cs.CV / cs.GT sweep this run. Non-rec lanes (games, code execution, video generation, general LLM) are therefore delegated to siblings by design (§5).
- ⚠️ **All quantitative claims are abstract- or HTML-section-level** (no full-text, code or leaderboard verification). Affiliations marked *(inferred)*: SearCl → SNU, WRRF → Thomson Reuters, LCRC → NASA ADS/CfA, Graph-free retrieval → Drexel. Stated-and-fetched affiliations: §2/§3 entries (HTML author blocks), plus the award page's own affiliation strings.
- ⚠️ **Dedup:** every featured ID grep-verified at 0 wiki hits before writing; same-day siblings claim none of these IDs (checked). Three candidates were **dropped as already on file**: TRACER `2610.21267` (10-17), CASI `2610.20293` (10-15/16/19), XViewRank `2610.20122` (10-15).
- **Out of scope by design:** KDD 2026 paper awards (still unpublished, per 10-19 edition); career/TC awards on the RecSys page (Outstanding PC/Reviewers listed only in passing).

---

## 8. Sources

**Re-fetched this run:**
- RecSys 2026 Conference Awards (official) — https://recsys.acm.org/recsys26/awards/
- ACM DL: AgentRec — https://dl.acm.org/doi/10.1145/3773078.3831880
- Per-paper arXiv abs pages: `2606.31031`, `2602.05663`, `2610.23453`
- Per-paper arXiv HTML author/affiliation blocks: `2610.25282`, `2610.24854`, `2610.24888`, `2610.24822`, `2610.16940`, `2610.17627`, `2610.18616`, `2610.21098`, `2610.23186`, `2610.25172`, `2610.25779`, `2610.14196`, `2610.23453`
- ICLR 2026 oral listing (CoCo verification) — https://www.iclr.cc/virtual/2026/oral/10011087
- Abstract pool: arXiv Export API harvest (cs.IR 150 + cs.LG 60, Oct 14–19, pre-rate-limit)

**Sibling digests used as dedup/cross-reference baselines:**
- [`synthesis/2026-10-17/conference-digest.md`](../2026-10-17/conference-digest.md), [`synthesis/2026-09-11/conference-digest.md`](../2026-09-11/conference-digest.md), [`synthesis/2026-10-19/conference-digest.md`](../2026-10-19/conference-digest.md), same-day [`arxiv-daily.md`](arxiv-daily.md) / [`arxiv-ai-search.md`](arxiv-ai-search.md) / [`arxiv-paper-check.md`](arxiv-paper-check.md) / [`game-rl-daily.md`](game-rl-daily.md) / [`tech-report-digest.md`](tech-report-digest.md)
