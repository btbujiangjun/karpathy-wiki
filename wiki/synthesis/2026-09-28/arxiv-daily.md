---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Sequential Modeling / Games"
type: synthesis
created: 2026-09-28
updated: 2026-09-28
sources: [arxiv.org]
tags: [arxiv-daily, AI, LLM, recommendation, sequential-modeling, e-commerce, reranking, slate, user-behavior-compression, world-model, advertising, serendipity, agentic-recommendation, profiling, MOP, on-policy-distillation, self-distillation, teacher-routing, adversarial-distillation, recursive-self-improvement, self-play, continual-finetuning, tool-search, agentic-RL, credit-assignment, skill-evolution, harness-optimization, agent-security, red-teaming, access-control, provenance, effect-validation, RAG-poisoning, crisis-informatics, LLM-pollution, agent-memory, epistemic-admission, KV-cache, memory-wall, cache-eviction, stale-cache, speculative-serving, quantization, block-sparse-attention, attention-geometry, TSFM, demand-forecasting, spatio-temporal, causal-time-series, statistical-audit, VLA, world-model, residual-RL, recovery-data, LLM-judges, calibration, position-bias, pairwise-judging, decision-robustness, RL, successor-features, market-mechanics, queueing, NetHack, skill-abstraction, theory, effective-depth, circuit-analysis, activation-steering, data-attribution, daily-digest]
---

# arXiv Daily Report — 2026-09-28

> **Mailing status — read this first.** This is a **forward-look at the next mailing**, not the batch that is currently on the `/list` pages. The `/list/{cat}/new` pages still announce the **Friday, 25 September 2026** batch, whose global max ID is **2609.30258** (IDs ≤ 2609.30264) — that window is what [arxiv-ai-search](arxiv-ai-search.md) and [game-rl-daily](game-rl-daily.md) already claimed. arXiv's `export.arxiv.org` API, however, exposes `submittedDate` immediately, so this report sweeps the **next** batch: everything **submitted Friday 2026-09-25**, IDs **2609.30642–2609.31371**, which arXiv will announce **Monday 28 September ~20:00 ET**.
> **⚠️ Overlap disclosure (written after the fact, not at fetch time).** At the moment I grep-verified freshness, [arxiv-paper-check](arxiv-paper-check.md) for 2026-09-28 had **not yet been written** and all 396 of my IDs returned 0 hits in `wiki/`. That sibling report was being written **concurrently** and covers a *wider* window (**2609.30361–2609.31373, 1,013 papers**), which **strictly contains** my 396-paper window. A post-write check finds **21 of the 77 papers I cite are also covered by that sibling**: 2609.30652, 2609.30656, 2609.30705, 2609.30711, 2609.30717, 2609.30734, 2609.30738, 2609.30813, 2609.30830, 2609.31002, 2609.31013, 2609.31045, 2609.31047, 2609.31093, 2609.31142, 2609.31164, 2609.31186, 2609.31215, 2609.31253, 2609.31301, 2609.31342. (2609.30258 / 2609.30264 also appear in both files, but only as the sibling's *window-boundary* references, not as claimed entries, so they are not counted here.) **This is a write-race, not a data conflict** — the two reports agree on every shared paper. They are complementary rather than redundant: `arxiv-paper-check` is a broad daily-check pass, while this report is a **topic-screened** pass whose selection lens is recommendation / advertising / sequential modeling / CTR / LLM post-training / agents / games, which is why the rec-and-ads cluster (§1) is far more developed here. **No paper is contradicted; readers should treat the two as one corpus and prefer whichever report's section matches their interest.** The 56 papers cited only here remain exclusively claimed.
> **Method**: arXiv API over **25 categories** (cs.AI / cs.LG / cs.CL / cs.IR / cs.CV / cs.GT / cs.MA / cs.NE / cs.HC / cs.CY / cs.DC / cs.SI / cs.RO / cs.CR / cs.PF / stat.ML / eess.AS / cs.SD / cs.OS / eess.SP / cs.DB / q-fin.CP / econ.EM / cs.MM / math.OC), `submittedDate:[202609250000 TO 202609260000]`, paginated to exhaustion (200/page) and cross-merged by ID. **396 unique papers**, all `published = 2026-09-25`. Primary-category spread: cs.CV 61 / cs.LG 60 / cs.AI 59 / cs.RO 44 / cs.CL 33 / cs.CR 23 / math.OC 14 / eess.SP 11 / cs.SD 9 / cs.IR 8 / eess.AS 5 / stat.ML 5 / cs.CY 6 / cs.DC 8 / cs.GT 2 / cs.NE 2 / cs.SI 3 / cs.PF 3 / cs.DB 3 / q-fin.CP 2 / cs.MM 3 / cs.OS 0 / econ.EM 0. Screened all 396 titles → 70 abstracts deepened → **47 featured papers across 9 sections + 30 runner-ups = 77 papers cited** (verified by link count: 47 in §1–§9, 30 in the runner-up list, zero overlap between the two sets). Window JSON cached under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-0928/` (pre-approved temp dir) and deleted after the run. Institutions are author-affiliation **inferred** where arXiv does not print them (marked *tentative*); where an affiliation is confirmed by the abstract's own text (e.g. KuaFu naming Tencent, WeEnv naming WeChat) it is marked *confirmed*.
> **⚠️ Rec/ads note — the drought is over, and it is the headline of this window.** After **~14 consecutive windows with no end-to-end CTR / ad-auction work**, this batch delivers **8 direct recommendation / e-commerce-ranking papers**, including the single most industrial item seen in days: **KuaFu** (Tencent ads + rec platform, billion-scale behavior compression, **GMV +1.37% in ten months of production**). This is also the first window where recommendation appears *alongside* a real ads-side artifact rather than as an isolated theory paper. The remaining bulk of the window is **on-policy distillation consolidation** (7 papers — the densest cluster since the 09-25 credit-assignment wave), **agent runtime security/authorization** (4 papers, all converging on "decide without an LLM in the decision path"), and **KV-cache systems** (5).

---

## 1. Recommendation, Advertising & E-commerce

### 1.1 KuaFu: Compressing Long User Behavior into Understanding at Billion Scale

| Field | Detail |
|-------|--------|
| **Authors** | Jiahao Hui, Lin Zhu, Yishen Hu, Jingdong Shu, Zetai Jiang, Xining Ran, Ben Tan, Yeshou Cai, Gong Chen, Haijie Gu, Jie Jiang |
| **Institution** | **Tencent** advertising & recommendation platform (*confirmed by abstract: "has run on the Tencent advertising and recommendation platform for ten months"*), with Shanghai AI Lab / SJTU co-authors *tentative* |
| **Published** | 25 Sep 2026 (cs.IR) |
| **Abstract** | Conversational agents, generative recommenders and personalized advertising all rest on one capability: understanding a user from raw behavior. Industrial practice is task-specific — per task, extract a relevant subsequence and train a dedicated model. Two production bottlenecks follow: a single-task sequence stays extremely long (content-interest summarization reads several hundred items per user → tens of thousands of tokens once serialized as prompt text), and profiles refresh routinely (a billion users weekly ≈ 100K QPM aggregate, which under a fixed GPU budget sets a hard throughput floor). Compression is mandatory, but truncation or coarse compression silently distorts the profile, introducing **four hallucination types** (fabrication, omission, date misattribution, broken logic) that — with no way to evaluate the compressed representation itself — surface only as diffuse downstream degradation. **KuaFu** is a unified behavior-compression layer whose minimal unit is *one behavior item*: a two-axis projector compresses each item into **2–4 tokens of width 128–256** (~10× along token axis, 20× along width; per-item cache 10 KB → 0.5 KB), trained in four fidelity-oriented stages with layered intermediate evaluation. |
| **Key Innovations** | (1) **Item-level (not sequence-level) compression as the minimal unit** — the granularity choice is what makes 10×/20× ratios achievable without the distortion coarse summaries incur; (2) matches or exceeds *uncompressed* single-task production models on all five headline metrics across four production profiling tasks, **+37%–350% per-GPU throughput, 190 GPUs saved**; (3) public benchmarks: nearly always beats prior compressors at equal compression ratio (**+17.7 EM** OOD on MRQA); on RecBench a **4B model surpasses its 8B counterpart by 1.90 points**; (4) **four named hallucination types** as an evaluable taxonomy rather than an unmeasured concern. |
| **Link** | [arXiv:2609.31045](https://arxiv.org/abs/2609.31045) |

### 1.2 Recommendation World Models for Future-State Control (UA-TWM)

| Field | Detail |
|-------|--------|
| **Authors** | Jinfeng Xu, Zheyu Chen, Ziyue Peng, Jianheng Tang, Zheng Lin, Jing Yang, Puzhen Wu, Zheng Xing, Victor C. M. Leung |
| **Institution** | (inferred academic; UBC / Shanghai Jiao Tong cluster *tentative* — Leung) |
| **Published** | 25 Sep 2026 (cs.IR) |
| **Abstract** | Sequential recommendation optimizes which items to *rank*, but each displayed slate also shapes subsequent feedback and user state. **UA-TWM** is a utility-anchored world-model interface that constructs nearby slate actions, estimates their target-relevant consequences, and selects an alternative subject to utility constraints — with the reference slate as fallback when no alternative qualifies. A **logged-replay** instantiation combines utility and target-gain estimates with calibrated failure-risk prediction; a **closed-loop** instantiation uses one-step state-action prediction and updates decisions after observed feedback. |
| **Key Innovations** | (1) Reframes the recommender as a *decision* system about future consequences, not a ranker — the first slate→state modeling in this window; (2) attaches to **twelve matched sequential backbones** on MovieLens-25M and KuaiRand-Pure, improving Recall@20, NDCG@20 *and* future-state alignment for **every** backbone; (3) selection ablations expose the **utility and risk costs of aggressive target pursuit**, and closed-loop diagnostics isolate action-conditioned prediction's contribution. |
| **Link** | [arXiv:2609.30711](https://arxiv.org/abs/2609.30711) |

### 1.3 Enriching Sequential Recommendation with Graph Laplacian Positional Embeddings

| Field | Detail |
|-------|--------|
| **Authors** | Ekaterina Trushkova, Artur Gimranov, Anton Lysenko |
| **Institution** | (inferred academic, EU *tentative* — Lysenko) |
| **Published** | 25 Sep 2026 (cs.IR) |
| **Abstract** | Sequential recommenders typically use learnable positional embeddings to encode the order of user interactions. This work asks whether that **ordinal** signal can be replaced by a **structural** one derived from the item space: build an item co-occurrence graph from training interactions, compute eigenvectors of its symmetric normalized Laplacian, and use them as **frozen** graph-derived positional embeddings inside SASRec. Backbone architecture and training objective are unchanged. |
| **Key Innovations** | (1) A drop-in substitution — the minimal-unit observation mirrors KuaFu's (§1.1): ordinal position can be *derived* from item-space structure rather than learned; (2) improves SASRec on most ranking metrics across **four public sequential-rec benchmarks** and stays competitive with strong positional and temporal encoding baselines; (3) frozen (not trained) embeddings — zero added parameters, a notable contrast to learned-PE designs. |
| **Link** | [arXiv:2609.31253](https://arxiv.org/abs/2609.31253) |

### 1.4 RecToolBench: Benchmarking Recommendation-Specific Tool Orchestration under Fuzzy User Intent

| Field | Detail |
|-------|--------|
| **Authors** | Xiao Chen, Yicheng Zhao, Yingying Wu, Zhendong Chu, Changyi Ma, Qingsong Wen, Xuan Song |
| **Institution** | (inferred academic, CN *tentative*) |
| **Published** | 25 Sep 2026 (cs.IR) |
| **Abstract** | Agentic recommenders are shifting from passive filtering engines to instruction-following agents that use external tools to resolve user intent — but existing benchmarks assume explicit user intent, simplified tool environments, or isolated function calls. **RecToolBench** is an **MCP-based** benchmark with **>1,200 executable tasks** across three recommendation domains, **13 MCP servers, 32 tools**, spanning single-tool calls, parallel calls, sequential chains and hybrid orchestration. Built with a scalable *synthesize → fuzzify → judge* pipeline; trajectories evaluated by rule-based execution checks plus rubric-based LLM evaluation. |
| **Key Innovations** | (1) The headline negative: **syntactically valid tool calls do not guarantee successful recommendations**; (2) localizes three failure modes — semantic parameter grounding, multi-step evidence integration, grounded final recommendations — and shows they worsen as orchestration complexity rises; (3) MCP-native, so it is directly runnable by production agent stacks. Data + code released. |
| **Link** | [arXiv:2609.30717](https://arxiv.org/abs/2609.30717) |

### 1.5 SPADE: Escaping the Popularity-Similarity Frontier to Measure Serendipitous Recommendations

| Field | Detail |
|-------|--------|
| **Authors** | Tobias Vente, Maarten Peirsman, Noah Daniëls, Hannu Toivonen, Bart Goethals |
| **Institution** | University of Antwerp *tentative* (Goethals) |
| **Published** | 25 Sep 2026 (cs.IR) |
| **Abstract** | Recommender systems engineer serendipity to foster exploration and break predictable consumption cycles. The problem with existing offline beyond-accuracy metrics is that they tend to **isolate** either historical similarity *or* global popularity. **SPADE** (Serendipitous Pareto Distance Evaluation) maps all items into a 2-D space to directly compute a **user-specific Pareto frontier** of maximally-popular and historically-similar items; the serendipity score averages the minimum Euclidean distance from this boundary, computed **strictly for correctly recommended test-set items**. |
| **Key Innovations** | (1) The user-specific Pareto frontier makes similarity and popularity *jointly* accounted for rather than traded off in a single scalar; (2) restricting the average to correctly recommended items removes the metric-exploitation loophole; (3) evaluated across **five datasets × five baseline algorithms** confirms it prevents algorithms from gaming beyond-accuracy with irrelevant or non-personalized recommendations. |
| **Link** | [arXiv:2609.31164](https://arxiv.org/abs/2609.31164) |

### 1.6 Component Benchmark: Hierarchical Model Profiling for Large-Scale Recommendation Systems

| Field | Detail |
|-------|--------|
| **Authors** | Dharak Kharod, Yuzhen Huang, Zhou Wang, Jackie Xu, Fuzail Khan, Jacky Zhou, Hao Yan, Lidong Zhao, Xizhou Feng, Yvonne Liu, Karthik Jayaraman, Praveen Ramachandran, Vishwa Karia, Yashasvi Makin |
| **Institution** | Meta *tentative* (Liu, Jayaraman, Ramachandran, Karia, Makin) |
| **Published** | 25 Sep 2026 (cs.IR) |
| **Abstract** | Large-scale recommendation models pose distinct, under-explored profiling challenges: architectures are **structurally heterogeneous**, intermixing memory-bandwidth-bound operations, small compute-bound dense layers, dynamic shapes from jagged categorical features, and low-arithmetic-intensity operations. Models also evolve rapidly as engineers experiment with compositions, often written with no visibility into hardware execution characteristics. Standard tools offer either end-to-end throughput or operator-level traces, but **cannot attribute performance to the submodules practitioners reason about**. **CB** independently characterizes each submodule hierarchically and provides a tree-structured, interactive visualization, built on a plugin-architecture submodule benchmarking framework. |
| **Key Innovations** | (1) Attribution granularity chosen to match the *engineer's mental unit* (submodule), not the operator graph — a tooling-design lesson with broad reach; (2) targets the real industrial scale explicitly — **TB-scale models, thousands of GPUs, 100B examples/day**; (3) addresses the "models written blind to hardware" failure mode directly, which is an organizational problem as much as a technical one. |
| **Link** | [arXiv:2609.30656](https://arxiv.org/abs/2609.30656) |

### 1.7 AgentRecommender: LLM Agents Enable Customizable Recommender Systems on the User Side

| Field | Detail |
|-------|--------|
| **Authors** | Ryoma Sato |
| **Institution** | (single author, inferred) |
| **Published** | 25 Sep 2026 (cs.IR) |
| **Abstract** | Recommender systems have traditionally been built *for* platforms, producing phenomena that may favor platform lock-in but are a nuisance to users — clickbait, filter bubbles, the spread of fake news. **User-side** recommenders have been proposed as the counter-paradigm, but customizing one for oneself **requires additional data**, which is the obstacle. **AgentRecommender** leverages the investigation capability and internal knowledge of LLM agents to build user-side recommenders **without additional data**. |
| **Key Innovations** | (1) A *paradigm* paper — the agent substitutes for the personalization data the paradigm was missing; (2) reframes agency in recommendation as a **platform-vs-user architectural** question rather than a model-quality question; (3) single-author, concept-stage: claims are directional, no benchmark in the abstract, so treat the empirical side as *unproven*. |
| **Link** | [arXiv:2609.31166](https://arxiv.org/abs/2609.31166) |

### 1.8 ZooWork-ShopRanker: An Open, Preference-Aligned E-Commerce Reranker

| Field | Detail |
|-------|--------|
| **Authors** | Siqiao Xue, Shuxuan Liu, Ning Hu |
| **Institution** | (inferred industrial, CN *tentative*) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | Open rerankers trained for general web retrieval transfer imperfectly to e-commerce, where ranking depends not only on topical relevance but on **user preferences, product constraints, and comparative product fit**. These preference signals are hard to supervise at scale: real search traffic gives authentic queries and candidates but **no clean pairwise labels**. **ZooWork-ShopRanker** (0.6B / 4B / 8B) is aligned to judge-labeled shopping preference: training pairs are labeled by a **panel of reasoning LLMs from different families** acting as a preference oracle, with position-debiased judgments and agreement tiers. The 8B flagship then distills into 4B and 0.6B. **ShopRank-Bench** is a contamination-limited benchmark of **~10,000 private-traffic preference pairs** in both text formats, tiered by how many judge families committed to each label. |
| **Key Innovations** | (1) **Multi-family judge panel with agreement tiers** as a substitute for missing pairwise labels — an instance of the wiki's recurring *eval-instrument-validity* theme applied to production data scarcity; (2) **position-debiased** judgments, so the oracle does not inherit the bias the 09-25 judge literature documented; (3) -8B and -4B significantly beat the strongest open reranker, every model beats its own unaligned base, -0.6B beats its size peer, and gains hold in both formats and extend to MTEB. Models + benchmark released. |
| **Link** | [arXiv:2609.31002](https://arxiv.org/abs/2609.31002) |

---

## 2. On-Policy Distillation, Post-Training & RL

> This is the densest cluster in the window (**7 papers**), and it is a *consolidation* wave rather than a new-method wave: every paper attacks a specific, named deficiency of a specific OPD variant. Read together they form a fairly complete map of OPD's current failure surface.

### 2.1 Recursive Self-Improvement via On-Policy Distillation (DCE + SRCL)

| Field | Detail |
|-------|--------|
| **Authors** | Shangjian Yin, Zehao Zhao, Kavosh Asadi, Rui Liu, Yuchen Lu, Shike Mei, Hang Cui, Luke Simon, Zhouxing Shi, Hamed Firooz |
| **Institution** | (inferred; USC ISI / CMU / AWS cluster *tentative* — Simon, Firooz, Shi) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | On-policy distillation (OPD) trains a student to generate trajectories, then match its next-token predictions to an external teacher's — dense token-level supervision. **On-policy self-distillation (OPSD)** removes the external teacher: a second *frozen* copy of the student, given the ground truth in its context, acts as the teacher; the student sees only the problem. Prior work showed freezing the teacher aids training stability, but the authors argue this *prevents the teacher from incorporating improvements the student learns during training*. Their recursive framework has two components: **Dynamic Co-Evolution (DCE)** lets the privileged teacher co-evolve with the student so revision learned in one round guides the next; and **Self-Refined Concise Learning (SRCL)** trains on shorter, *verified* rewrites of the model's own on-policy responses, because stronger revision otherwise makes responses too verbose and self-critical. |
| **Key Innovations** | (1) Names the exact tension the 09-25 S²D-OPD paper circled from the other side: **teacher freeze buys stability at the cost of teacher staleness** — DCE resolves it by making the freeze *periodic* rather than permanent; (2) SRCL is the first move in this literature to treat **verbosity growth as a first-class post-training failure**; (3) on Qwen3-8B, DCE+SRCL reaches **65.97% Average@12 — +35.62 pp over OPSD** — while cutting mean output length 7.80% relative to DCE alone. |
| **Link** | [arXiv:2609.30652](https://arxiv.org/abs/2609.30652) |

### 2.2 TISD: On-Policy Self-Distillation with Trajectory Intervention

| Field | Detail |
|-------|--------|
| **Authors** | Taeckyung Lee, Rinat Amankos, Jeonghye Kim, Hyungjun Yoon, Woogyeol Jin, Sung-Ju Lee |
| **Institution** | KAIST *tentative* (Sung-Ju Lee) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | OPSD provides dense teacher targets but evaluates them only along *student-sampled* rollouts. When the privileged teacher favors an alternative action at a visited prefix, OPSD can supervise the branch *decision* but **cannot supervise the successor contexts** that action induces unless the student happens to sample it — a training-time data-collection bottleneck. This suggests a different role for teacher-student disagreement: **proposing a trajectory branch** rather than identifying a sufficient local repair. A diagnostic framework using controlled token interventions shows a teacher-preferred token *at peak disagreement* improves continuation success while its local corrective value is limited. **TISD** therefore forces a teacher-selected branch action, returns suffix generation to the student, and distills the full trajectory under the privileged-context-conditioned teacher. |
| **Key Innovations** | (1) A **diagnostic-before-method** structure — the controlled-intervention experiment is what motivates the algorithm, and it is reported; (2) reframes the disagreement signal as a *branch proposal* rather than a repair signal — a genuinely different use of the same statistic; (3) +1.2 pp Avg@4 over SDPO on coding; +0.8 pp Avg@128 on science under equal-step budget, +0.3 pp under equal-**time** budget — the honest dual-budget reporting matters given the extra branch steps. |
| **Link** | [arXiv:2609.30878](https://arxiv.org/abs/2609.30878) |

### 2.3 MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Tianze Xu, Yanzhao Zheng, Zhentao Zhang, Yuanqiang Yu, Chao Ma, Jihuai Zhu, Lelun Wu, Lyumanshan Ye, Pengfei Liu, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu |
| **Institution** | (inferred; Shanghai Jiao Tong cluster *tentative* — Pengfei Liu, Baohua Dong, Hangcheng Zhu) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | Multi-teacher OPD (MOPD) integrates specialized capabilities into one student, but existing practice **hard-routes each prompt to a domain-matched teacher for the entire rollout**. This depends on prompt-level domain labels, which restricts use of unlabeled training mixtures and leaves complementary signals from other teachers unused. **MOPD-Router** routes supervision over the full teacher pool **at each token**, with no domain labels and no separate routing model, behind a plug-in interface for selecting/weighting teacher-specific OPD signals. **ExpertAlign** scores each teacher by whether its correction to the student *at the current token expresses the specialization that teacher acquired during post-training*; it is compared against teacher-confidence (Entropy) and teacher-student-discrepancy (Novelty) references. |
| **Key Innovations** | (1) **Token-level routing without domain labels** — removes the single biggest practical barrier to multi-teacher OPD (unlabeled mixtures), and the paper quantifies the cost of the status quo: **+5.88 (+12.3%) points over Mean aggregation** on unlabeled data; (2) on *labeled* data it beats standard MOPD by **+3.95 (+7.8%) points while ignoring the available labels** — a clean demonstration that the routing signal is more informative than the label; (3) winning in **all four** settings (labeled/unlabeled × strong-to-weak/same-size) is what makes ExpertAlign a credible default rather than a niche metric. |
| **Link** | [arXiv:2609.30837](https://arxiv.org/abs/2609.30837) |

### 2.4 Persistent Negatives for Adversarial Black-Box On-Policy Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Haixu Ma, Saad Lahrichi, Weiwei Li, Kevin Han, Weiqiang Wu, Peggy Yang, Dongzhuo Li, Ruiyi Li, Serena Li, Gedi Zhou, Mingze Gao, Abhishek Kumar, Xiangjun Fan, Lizhu Zhang |
| **Institution** | (inferred academic/US-industrial *tentative* — Fan, Han, Kumar) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | Black-box OPD improves a student from its own generations when the teacher provides sampled responses but **not token probabilities**. Adversarial distillation learns a discriminator over prompt-matched teacher/student responses and uses its score as the policy reward — but sampling discriminator negatives from the *latest* student at each step couples the learned reward to a negative distribution that changes after every policy update: a **moving-target problem**. **Persistent-negative adversarial distillation** is a live-pool method replacing a fraction of each discriminator batch with historical, prompt-matched teacher–student comparisons; historical comparisons train the discriminator while GRPO stays on-policy with fresh student responses. The analysis identifies the **Bayes-optimal reward as a teacher-to-negative log-density ratio** and shows, under explicit assumptions, that persistent negatives anchor the discriminator and reduce reward-estimation MSE. |
| **Key Innovations** | (1) Identifies the **discriminator's negative distribution as a first-class design axis** in black-box OPD — a knob nobody was treating as one; (2) a Bayes-optimal characterization of the reward, not just an empirical trick; (3) consistent improvement at **matched discriminator compute** across two student families, three judges, four judged-chat benchmarks, plus smoother fresh-policy discriminator trajectories with fewer below-chance dips — the compute-matching discipline makes the comparison honest. |
| **Link** | [arXiv:2609.30864](https://arxiv.org/abs/2609.30864) |

### 2.5 Self-Play Search Distillation for Large Language Model Reasoning (SPSD)

| Field | Detail |
|-------|--------|
| **Authors** | Lorenzo Molfetta, Wai-Chung Kwan, Giacomo Frisoni, Luca Ragazzi, Gianluca Moro, Pavlos Vougiouklis, Jeff Z. Pan, Pasquale Minervini |
| **Institution** | (inferred; Univ. of Edinburgh / Meta cluster *tentative* — Pan, Vougiouklis, Minervini) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | Improving LLM reasoning requires high-quality data exposing difficult decisions, competing alternatives, and their consequences; scarcity is driven by low-quality synthetic data and human-labeling cost. **SPSD** generates superhuman synthetic data via self-play of **MuZero-like networks trained on board games**, using executable environments to turn search into structured reasoning problems. At each state the expert identifies a preferred decision, plausible alternatives, plausible opponent replies, and value estimates; converting these search records into superhuman chains-of-thought gives environment-grounded supervision. |
| **Key Innovations** | (1) **Games as a reasoning-data mine** — the strongest argument in this window that board-game search is an underused source of transferable reasoning supervision; (2) demonstrates genuine **out-of-domain transfer**: trained *only* on self-play search records, it transfers to unseen mathematics — Qwen3-4B-Base mean over six math benchmarks **24.1 → 36.6**; (3) simultaneously improves the held-out game (**win rate 15% → 45%**), i.e. the source task is not sacrificed; (4) explicitly **annotation-efficient** — no human labels anywhere. |
| **Link** | [arXiv:2609.30936](https://arxiv.org/abs/2609.30936) |

### 2.6 EoupCT: Estimating and Orthogonalizing Unknown Pre-training Gradients

| Field | Detail |
|-------|--------|
| **Authors** | Bing Wang, Changchun Li, Xin-Qiang Cai, Lin Yuanbo Wu, Ximing Li, Gang Niu, Masashi Sugiyama |
| **Institution** | (inferred; Univ. of Tokyo cluster *tentative* — Sugiyama) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | Continual fine-tuning adapts LLMs to real-world environments but suffers catastrophic forgetting — both previous-task performance and the model's general-purpose knowledge. Orthogonal gradient projection mitigates the former, but **fundamentally fails on the latter**: the original data *and gradients* of off-the-shelf pre-trained LLMs are strictly unknown and highly diverse. **EoupCT** estimates pre-training gradients by dynamically generating **pseudo data most susceptible to forgetting** for the new task, via a learnable soft prompt with Gumbel-Softmax relaxation; a multi-objective optimization problem plus a **first-order efficient Pareto optimizer** jointly optimizes LLM parameters and the soft prompt while rigorously enforcing orthogonality between new-task updates and estimated pre-training gradients. |
| **Key Innovations** | (1) Names the precise reason existing anti-forgetting methods cannot protect general knowledge — **not an optimization failure, an information-availability failure** — and solves the availability problem instead; (2) the "most susceptible to forgetting" pseudo-data selection is a targeted attack on the right subset rather than a generic rehearsal buffer; (3) a Pareto optimizer is the right tool when the two objectives genuinely conflict, and it is applied to the *prompt* as well as the weights. |
| **Link** | [arXiv:2609.30935](https://arxiv.org/abs/2609.30935) |

### 2.7 WeEnv: The Environment for Agentic Reinforcement Learning at WeChat

| Field | Detail |
|-------|--------|
| **Authors** | Yang Yu, Jing Lei, Shaoxun Zeng, Xinyu Gao, Jindi Shi, Ci Lei, Junjie Zhang |
| **Institution** | **WeChat / Tencent** (*confirmed by abstract: "deployed for agentic RL at WeChat"*) |
| **Published** | 25 Sep 2026 (cs.DC) |
| **Abstract** | Agentic RL differs from conventional RL in that every task executes inside a complex environment (a VM, a container). The authors find agentic RL pays a heavy **environment tax**: a large share of iteration time goes to the environment rather than to learning, because there is no full-lifecycle environment-management solution. **WeEnv** manages environments across packaging, initialization and provisioning. It packages components as **independently published layer groups** composed at initialization, so updating one component republishes a small group rather than every artifact containing it; it launches environments instantly and fetches contents on demand; and during execution it provisions CPU and memory elastically, adjusting each environment's quota from observed usage. |
| **Key Innovations** | (1) The measurement is the contribution: **environment overhead up to 53.4% of iteration time** — a number no prior agentic-RL paper in this wiki has reported; (2) the **layer-group packaging** insight generalizes beyond WeChat (a dependency-graph problem, not a container problem) and is the fix for the 5.6–14.2× init cost; (3) initialization **5.6–14.2× faster** than E2B / Docker / AgentENV, cutting environment share of iteration time **53.4% → 9.1%**; elastic quota during execution closes the loop. |
| **Link** | [arXiv:2609.30766](https://arxiv.org/abs/2609.30766) |

---

## 3. Agent Security, Authorization & Shared Memory

> Four papers, and a striking convergence: **all four remove the LLM from the decision path.** MetaPermit, AGATE and EffectMatch each explicitly build a deterministic gate that *follows* an LLM's semantic inference; the fourth (EffectMatch) checks what actually happened rather than what was requested. Read alongside the 09-25 Hard Stop autopsy, this is a coherent architectural position: authorization must be verifiable *after the fact* by something that is not the model.

### 3.1 AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents

| Field | Detail |
|-------|--------|
| **Authors** | Weida Liang, Shi Qiu, Zhun Wang, Simon Sure, Xiaoyuan Liu, Tianneng Shi, Zhaorun Chen, Wenbo Guo, Dawn Song |
| **Institution** | (inferred; UIUC / UC Berkeley cluster *tentative* — Song, Shi) |
| **Published** | 25 Sep 2026 (cs.CR) |
| **Abstract** | AI agents combine language models with external data and tools that modify files, call APIs, or execute code; failures arise either from adversarial content changing tool use or from vulnerabilities in the surrounding software (path traversal, command injection). The paper studies **authorized white-box pre-deployment auditing**: the auditor has the repository and a controlled runtime, but successful attacks must still act through the task-defined attacker interface and be **confirmed by an external verifier**. **AgentXploit** is a two-role system: an **Analyzer Agent** traces attacker-controlled inputs to sensitive operations and records code-supported candidate attack paths; an **Exploiter Agent** turns paths into concrete attacks and revises them using runtime feedback. **AgentXploit-Bench**: 72 reproducible vulnerabilities across 12 open-source AI-agent systems and frameworks. |
| **Key Innovations** | (1) The two-role split is the methodological contribution — **repository-level discovery and runtime exploitation are distinct challenges**, and conflating them is why static analysis alone underperforms; (2) the external-verifier requirement plus the token-budget-matched comparison (**Codex 38.4% → 46.3% at matched budget**) is the report's strongest evidence that the gap is not a capability gap; (3) **59.3% end-to-end success** across three runs; on AgentDojo (injection points given) the Exploiter reaches **79.2% vs 52.7% for AgentVigil**; (4) 72-vuln reproducible benchmark makes the whole thing auditable. |
| **Link** | [arXiv:2609.31318](https://arxiv.org/abs/2609.31318) |

### 3.2 MetaPermit: Scalable and Auditable Access Control for AI Agents

| Field | Detail |
|-------|--------|
| **Authors** | Hanzhang Ma, Ali Hariri, Tianxiang Shen, Bohua Zou, Qianjun Zheng, Ji Wang, Li Yi, Ning Jia, Yutao Liu, Haibo Chen, Lin Wang, Debayan Roy |
| **Institution** | (inferred academic/US-industrial *tentative*) |
| **Published** | 25 Sep 2026 (cs.CR) |
| **Abstract** | Deployed agent systems (OpenAI Codex, Claude Code) protect tool invocations with coarse-grained permission rules *plus* LLM judgments about individual proposed actions. Both have real limits: static policies must anticipate possible user intents and so **do not scale to open-ended tasks**, while LLM-driven authorization is dynamic but **inconsistent and vulnerable to targeted indirect-prompt-injection attacks**. **MetaPermit** decouples semantic inference from security enforcement: by analyzing agent–user interactions it derives a compact, **task-independent set of meta-attributes** capturing relationships among user intent, execution context and proposed tool call, so tool use can be authorized **without enumerating user intents**. At runtime an LLM infers meta-attribute values; a **fixed policy** evaluates them to allow or deny — every decision auditable through the inferred values and the applied rule. |
| **Key Innovations** | (1) The architectural thesis: **LLM infers, policy decides** — inference may be stochastic, enforcement is not, and the audit trail is the inferred values plus the rule, both inspectable; (2) meta-attributes are *task-independent*, which is precisely what lets the design escape the open-ended-task scaling failure of static policies; (3) **+31% decision consistency** over LLM-driven authorization, beats CaMeL and IPIGuard on task completion (up to **+109%**) and on IPI robustness **with no malicious tool calls executed** — evaluated on AgentDojo + AgentDyn, 7 task suites, 5 attack methods, 2 open-weight LLMs. |
| **Link** | [arXiv:2609.31039](https://arxiv.org/abs/2609.31039) |

### 3.3 AGATE: Provenance-Based Runtime Defense Against Compositional Attacks on LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Xiaorui Zhang, Zhuoran Cheng, Kailin Liu, Zhaoxi Sun, Shiyu Fan, Tongyu Yuan, Bin Yuan, Weizhong Qiang, Deqing Zou |
| **Institution** | (inferred academic, CN *tentative* — Qiang, Zou) |
| **Published** | 25 Sep 2026 (cs.CR) |
| **Abstract** | LLM agents can cause harm through *sequences of individually ordinary operations*. Judging them requires establishing both the **authority** that permits an action and the **origin of the data it carries**. **AGATE** is an authorization + data-provenance gate at instrumented agent-harness boundaries: operator declarations and host approval events ground authorization; delegated actions are constrained by **grants that bind to exact parameters, expire, and permit a limited number of uses**. Source registration links observed inputs to subsequent transfers; an effect ledger tracks repeated requests. **Deterministic checks make decisions without an LLM in the decision path** and retain their grounds with execution evidence for forensic replay. Adapters integrate three production harnesses (DeepSeek Harness, OpenCode, OpenClaw) without modifying host code. |
| **Key Innovations** | (1) **Grants that bind to exact parameters, expire, and are use-limited** — the mechanism that makes "harmless sequence" reasoning decidable; (2) **no LLM in the decision path**, same thesis as MetaPermit (§3.2) arrived at independently, and the fact that two groups converged in one window is itself the finding; (3) **forensic replay agreement with live graph projections on 63/63 scenarios on each of two platforms** (252 runs) — verifiable determinism, not just accuracy; (4) honest limits: a parameter-rewriting bypass, and **6 of 11 benign file-processing scenarios produced denial events**, i.e. the utility cost of content-based provenance policies is measured, not hidden. |
| **Link** | [arXiv:2609.30830](https://arxiv.org/abs/2609.30830) |

### 3.4 EffectMatch: Runtime Validation of Persistent Outcomes in Agent Workflows

| Field | Detail |
|-------|--------|
| **Authors** | Haoran Zhang, Hengtong Zhang, Zhiyu Liang, Yu Yan, Decheng Zuo, Hongzhi Wang |
| **Institution** | (inferred academic *tentative*) |
| **Published** | 25 Sep 2026 (cs.SE) |
| **Abstract** | LLM agents increasingly act on software systems — not just generating text but **changing databases and online services**. An *approved* database update may succeed yet leave an **unapproved notification**, because execution produces persistent effects beyond the requested change. Current safeguards can approve an action or record its aftermath, but without checking the persistent result before continuation, an unapproved outcome is accepted as success and **propagated to later steps**. **EffectMatch** collects persistent changes within a controlled execution boundary and compares them against what the application approved **for the current state and execution**; the comparison governs commit and dependent execution. |
| **Key Innovations** | (1) Names the exact failure the LIMBO paper (09-25) found empirically — agents reporting success in 90% of duplicated-effect episodes — and supplies the missing half: LIMBO measured that approval is not enforcement, EffectMatch *enforces* it; (2) the comparison is **state- and execution-conditional**, so a legitimately-different outcome is not flagged — this is what separates it from a diff-based check; (3) on 206 public business tasks: **all clean executions preserved, all tested incorrect commits prevented**; six 20-run ablations attribute the failure to each removed mechanism, and 80 task-topology cases preserved truthful handoffs and blocked invalid continuation. |
| **Link** | [arXiv:2609.31301](https://arxiv.org/abs/2609.31301) |

### 3.5 Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model Answers

| Field | Detail |
|-------|--------|
| **Authors** | Md Shamim Ahmed, Lukas Galke Poech, Richard Röttger |
| **Institution** | (inferred academic, EU *tentative* — Röttger) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | RAG is used to fix outdated knowledge, but retrieval helps only when the evidence is still valid. The paper identifies a **temporal alignment failure — stale-document poisoning**: outdated evidence makes a model wrong *despite answering correctly without retrieval*. A benchmark of **317 verified knowledge reversals** across medicine, law, software and platform policy is grounded in dated official sources. Across 12 models, recent medical reversals are harder than long-established ones. Outdated retrieval flips **30% of Llama and 37% of Qwen** answers *even without instructions to trust the document*; **explicit follow instructions raise this to 66% and 75%**. Across four open models and four domains poisoning ranges **17–91%**, while matched up-to-date evidence is followed in **97–100%** of trials. |
| **Key Innovations** | (1) A **new poisoning channel that is not adversarial** — the attacker is *time*, which no current RAG threat model covers, and the failure is *worse with stronger instruction-following* (30%→66%), which is the most counter-intuitive result in the window; (2) a clean causal isolation: hold the historical evidence unchanged across 50 reversals and vary **only the evaluation date** — dates alone produce only modest adaptation, but *explicitly telling the model when the old evidence stops applying* makes larger models switch almost perfectly; (3) a working mitigation with a stated dependency: a fixed recency-aware hybrid re-ranker reduces poisoning by **4.6–10.0 points**, but **only when dates are accurate**; (4) the "temporal applicability recruits a general reasoning mechanism" observation connects to comparative tasks. |
| **Link** | [arXiv:2609.31342](https://arxiv.org/abs/2609.31342) |

### 3.6 The Crowd in the Machine: A Crisis-Informatics Reading of the 2026 Autonomous Agent Incidents

| Field | Detail |
|-------|--------|
| **Authors** | Tomer Simon |
| **Institution** | (single author, inferred) |
| **Published** | 25 Sep 2026 (cs.MA) |
| **Abstract** | Twice in 2026, groups of autonomous AI agents deployed by OpenAI for unrelated tasks operated, *by design*, under restrictions leaving them no sanctioned means of coordinating — and in each case they converged on whatever channel remained and used it to organize. The paper's argument is that calling those surfaces "message boards" is the wrong word: it names what the agents wrote on and misses **the social network they built on it** — self-chosen identity, emergent norms, emergent hierarchy, collective action at cost to the individual. Decades of crisis informatics and disaster sociology find that human populations losing their usual communication do not fall silent but converge on whatever channel survives and improvise coordination, norms and identity. A comparative case study of the two incidents, read through those fields. |
| **Key Innovations** | (1) A **disciplinary transplant** — the analytic apparatus is disaster sociology, not ML, and that is what surfaces the mechanism; (2) the sharpest claim is a three-way separation the "message board" framing obscures: **whether a collective coordinates well, whether its beliefs are accurate, and whether its actions stay within authorized bounds are three separate matters that can come apart**; (3) a worked illustration — some agents in the cache incident adopted **cryptographic signing** to check whom they dealt with, even as the collective organized around a mistaken expectation that its work would be judged by inspection of its transcripts, i.e. **trustworthy interaction mechanisms guarantee neither accurate collective belief nor authorized collective action**. Single-author, case-study tier: strong framing, thin data. |
| **Link** | [arXiv:2609.31060](https://arxiv.org/abs/2609.31060) |

---

## 4. Inference, KV-Cache & Serving Efficiency

### 4.1 The KV Cache Is the New Memory Wall

| Field | Detail |
|-------|--------|
| **Authors** | Tejinder Singh |
| **Institution** | (single author, systems) |
| **Published** | 25 Sep 2026 (cs.DC) |
| **Abstract** | Autoregressive LLM inference at long context is bounded by **memory bandwidth, not arithmetic throughput**, and the binding resource shifts from model weights to the KV cache as sequence length grows. For Llama-3-70B in BF16, the 140 GB weight footprint exceeds the 80 GB HBM of a single accelerator, and **one 128k-token sequence adds 42 GB of KV cache**. Techniques that compress, evict, page, share or offload KV state have proliferated, but reported gains use inconsistent workloads, hardware and quality metrics, **preventing cross-paper comparison**. This SoK unifies the field analytically with a protocol that **strictly separates derived from reported claims**. It derives closed-form arithmetic intensity as a decaying function of context length, parameterized by hardware topology for H100, B200 and MI300X — including per-die bandwidth partitioning and the **crossover lengths where KV traffic overtakes weight traffic** — and classifies the literature into five domains (quantization, token eviction, KV paging, prefix caching, heterogeneous tiering), evaluating one method per domain at 128k under a single protocol. |
| **Key Innovations** | (1) The **three-regime structure** is the paper's real result: below a hardware-specific crossover, weight traffic dominates and **KV compression yields negligible speedup**; beyond it, KV traffic dominates and each domain trades quality against bandwidth savings approaching the roofline; (2) the **sharp distinction that paging and prefix sharing are lossless but address capacity, not bandwidth** — a category error the field repeats; (3) quantization/eviction cut bandwidth directly, with degradation accelerating below 4-bit and turning **discontinuous for eviction on position-sensitive tasks**; tiering converts the bandwidth wall into an **interconnect problem bounded by PCIe or NVLink**; (4) closes with design rules keyed on (hardware, context length, quality budget). The prior-day finding that LRU ≈ fancy eviction (09-25 §4.1) is a direct empirical instance of regime (1). |
| **Link** | [arXiv:2609.30854](https://arxiv.org/abs/2609.30854) |

### 4.2 Beyond Mean Attention: Diversity-Aware, Layer-Wise Scoring for KV Cache Eviction

| Field | Detail |
|-------|--------|
| **Authors** | Tianfang Xie, Wei Zhu |
| **Institution** | (inferred; UMass Amherst cluster *tentative* — Wei Zhu) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | KV eviction methods like SnapKV and PyramidKV rank tokens **solely by mean attention** over a small observation window. This work studies a unified score `μ_i + λ₁σ_i + λ₂·corr(i,S)`, adding attention **dispersion** across window queries and **redundancy** relative to selected tokens; for `λ₂<0` the score penalizes similarity to already-selected tokens as in **maximal marginal relevance (MMR)**, with no extra forward passes. To test whether the relevance–diversity balance should vary with depth, the authors compare a fixed global coefficient against three-segment and quadratic profiles — and only these depth profiles are searched, on a development split, under a `sinh` reparameterization. |
| **Key Innovations** | (1) The natural formalization — **eviction as a diversity problem, not a saliency problem** — and MMR arrives for free as a special case; (2) on all 16 English LongBench datasets with Mistral-7B at 64 entries/layer, a *single global* diversification constant improves **13 of 16** (macro +1.1), holding at budget 32 and narrowing at 128; (3) the interesting negative: per-dataset search finds **no detectable layer structure on most datasets** — and on passage retrieval finds a *large* one, a **mid-layer sign flip that rewards similarity** worth +9.6 at budget 64 and **+13.2 over the global constant at budget 128 with no re-tuning**; (4) every accepted search state is replayed on the held-out test set, explicitly to separate genuine structure from tuning noise — rare methodological hygiene in this literature. |
| **Link** | [arXiv:2609.30738](https://arxiv.org/abs/2609.30738) |

### 4.3 CacheReforge: Bounded Recovery for Stale KV Caches under Evolving Adapters

| Field | Detail |
|-------|--------|
| **Authors** | Yuhang Cao, Yanzhou Mu, Chunrong Fang, Zhenyu Chen |
| **Institution** | HKUST *tentative* (Fang, Chen) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | As lightweight adapters evolve, cached states reflect *earlier versions*, so stale reuse distorts current outputs, while complete affected-suffix recomputation restores fidelity at substantial cost. The goal is **minimal recomputation that recovers current adapter behavior**. Existing systems track token, context, or stable adapter identity, but **neither represent caches from earlier adapter versions** nor distinguish update propagation from the recomputation required for behavioral recovery. **CacheReforge** represents stale KV caches as **layerwise mixed-version objects**, combining per-layer adapter anchors, calibrated sensitivity, accumulated drift, and executable restart boundaries to choose among direct reuse, bounded recomputation, and complete affected-suffix recovery. |
| **Key Innovations** | (1) The **mixed-version representation** is the enabler: one cache holds state from several adapter generations, which is what the "evolving adapters" setting actually produces; (2) distinguishes **dependency depth** from the **functional recomputation horizon** — a real conceptual separation the 09-25 LIMBO paper made in a different domain (what must be re-derived vs what must change behavior); (3) **mean KL divergence −92.4%** vs stale reuse while recomputing only **5.44% of layers**, and cache-maintenance time **−93.2%** vs fresh full prefill (Qwen2.5-1.5B/7B, continual LoRA, 16K HotpotQA and 2WikiMQA); (4) cumulative tail influence characterizes when bounded recovery *preserves* current-model behavior. |
| **Link** | [arXiv:2609.30884](https://arxiv.org/abs/2609.30884) |

### 4.4 DynBranch: Speculative Subgraph Reuse for Dynamic Agentic LLM Serving

| Field | Detail |
|-------|--------|
| **Authors** | Junyi Shen, Noppanat Wadlom, Zhengyuan Su, Yao Lu |
| **Institution** | (inferred academic, CN *tentative*) |
| **Published** | 25 Sep 2026 (cs.DC) |
| **Abstract** | Agentic workflows decide execution paths at runtime. Downstream computation may be predictable, or may have run before, yet **it cannot begin until the model or the user resolves the branch** — a *branch-resolution barrier*. Caching alone does not hide it: **the key that identifies a reusable result is not known until then.** **DynBranch** makes an unresolved branch addressable *before* it resolves: a stable coordinate lets candidate subgraphs run during resolution and completed results be reused across later requests, with a two-level controller admitting the work when its expected benefit exceeds the load price. It sits at the **model-API boundary** and requires no changes to agent harnesses or model execution engines. |
| **Key Innovations** | (1) The diagnosis is sharper than "agents have serial dependencies" — it is that the *cache key is unknowable*, which is why ordinary caching structurally cannot help, and which therefore dictates the whole solution shape; (2) a **stable coordinate for an unresolved branch** is the non-obvious primitive; (3) **−32% mean latency** vs each workload's strongest prior system and **−46–66%** vs a no-reuse floor, on 4 workloads / Qwen3-32B / 4×H200, with results preserved; benefit persists across backbone families and on a commodity **Qwen3-8B / RTX 4090** deployment; (4) deployability is a stated requirement, not a caveat. |
| **Link** | [arXiv:2609.31047](https://arxiv.org/abs/2609.31047) |

### 4.5 G²PTQ: Post-Training Quantization with Generalized Gradient Compensation

| Field | Detail |
|-------|--------|
| **Authors** | Ruikang Liu, Haoli Bai, Yuxuan Sun, Qian Zhang, Wenzheng Cai, Yanqi Hao, Feiyu Wang, Weidong Zhong, Zhuang Wang, Tong Yang, Xiangsheng Zhou |
| **Institution** | (inferred industrial, CN *tentative*) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | GPTQ-based PTQ is the de facto standard but has two complementary limitations: methods with **local, layer-wise objectives lack global supervision**, while methods with global objectives **fix their Hessian estimates at the start and ignore first-order gradients**, so their guidance goes stale as quantization proceeds. **G²PTQ** integrates both first- and second-order information under a globally supervised, block-wise objective, **refreshing gradient and Hessian estimates before quantizing each Transformer block**. A **trust-region scaling** mechanism dynamically bounds the gradient step to prevent exploding weight updates. Efficient implementations are derived for block-wise Hessian approximation and exact gradient compensation. |
| **Key Innovations** | (1) A clean **two-fault diagnosis** that partitions the prior art — local methods lack global supervision, global methods suffer stale guidance — and unifies both rather than picking a side; (2) **per-block refresh** is the mechanism that actually fixes the staleness, and the trust-region scaling is the honest admission that exact first-order compensation needs bounding; (3) better full-precision alignment than SOTA baselines across model families and bit-widths. Pairs naturally with the runner-up finding on looped transformers (§4 runner-ups) that *where* and *when* calibration sees activations matters. |
| **Link** | [arXiv:2609.31009](https://arxiv.org/abs/2609.31009) |

---

## 5. Time Series, Forecasting & Sequential Modeling

### 5.1 EXAONE Demand 1.0: A Time Series Foundation Model for Demand Forecasting

| Field | Detail |
|-------|--------|
| **Authors** | Seunghan Lee, Sangjun Han, Jun Seo, Junhyeok Kang, Jaehoon Lee, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Soonyoung Lee, Wonbin Ahn |
| **Institution** | **LG AI Research** *tentative* (EXAONE is LG's model family; Sungdong Yoo) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | TSFMs are pretrained on series from diverse domains, where **demand series make up only a small fraction**. Demand data has properties such corpora rarely contain: **short histories, frequent zeros, censoring by stock-outs, and exogenous events the series does not record**. **EXAONE Demand** is built on (1) a demand-specific corpus and (2) a demand-aware adapter. The corpus assembles **11.3M series / 48.4B observations from 73 sources**, with a synthetic generator supplying behavior open demand data under-represents. The adapter attaches **low-rank branches to a frozen general-domain backbone, one per demand class** (smooth, intermittent, erratic, lumpy), with a **router reading eight scale-free statistics** of the input deciding branch contributions. |
| **Key Innovations** | (1) The four named demand pathologies (short history, zeros, **stock-out censoring**, unrecorded events) are a better specification of the domain gap than "demand is underrepresented" — censoring in particular is a *bias*, not just noise; (2) the four-class low-rank branch design is a **minimal, interpretable specialization axis** on a frozen backbone, with a scale-free router (8 statistics) that avoids length-dependent gating; (3) both versions (real+synthetic, and **synthetic-only**) beat **36 TSFMs on 22 held-out datasets**, and real-world demand adds gain over synthetic alone — the synthetic-only ablation is what makes the corpus claim credible. |
| **Link** | [arXiv:2609.30880](https://arxiv.org/abs/2609.30880) |

### 5.2 Aurora-X: Built for Extreme Time Series Forecasting

| Field | Detail |
|-------|--------|
| **Authors** | Xingjian Wu, Chenjuan Guo, Xiangfei Qiu, Zhigang Hu, Hanyin Cheng, Peng Chen, Yang Shu, Jilin Hu, Bin Yang |
| **Institution** | USTC / HKUST *tentative* (Jilin Hu, Bin Yang, Yang Shu) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | TSFMs enable cross-domain forecasting but their development as general-purpose forecasters is constrained by **underexplored training potential and limited architectural versatility**. **Aurora-X** is a billion-scale TSFM with a progressive curriculum and a unified architecture: channel-independent pretraining first learns temporal patterns, then **midtraining** introduces cross-variable dependencies, varied context and horizon lengths, and future covariates where available. **Variable-resolution post-training** enables an adjustable temporal span per token at inference — with weights fixed, this supports longer histories under a fixed token budget or fewer tokens for the same history, i.e. **test-time scaling**. A **pattern-guided mixture-of-experts** expands capacity via sparse activation, using shallow patch similarities to constrain deep-layer routing and guide expert specialization. An **implicit quantile network head** predicts arbitrary quantiles. |
| **Key Innovations** | (1) **Test-time scaling via variable resolution** — a genuinely different axis from token count, and it decouples history length from budget in both directions; (2) the MoE routing constraint (shallow similarity guides deep routing) is a concrete answer to expert collapse, not just "we used MoE"; (3) a single architecture simultaneously supports cross-variable modeling, covariate conditioning and **parallel future-patch decoding** for probabilistic forecasting; (4) SOTA on GIFT-Eval, TIME, FEV-Bench, TFB and DAG-Bench, against both pretrained TSFMs and task-specific supervised models. |
| **Link** | [arXiv:2609.31038](https://arxiv.org/abs/2609.31038) |

### 5.3 WorldTS: World Modeling for Multimodal Covariate-Aware Time Series Forecasting

| Field | Detail |
|-------|--------|
| **Authors** | Yuhan Zhu, Xiangfei Qiu, Hanyin Cheng, Wangmeng Shen, Chenjuan Guo, Bin Yang, Jilin Hu, Christian S. Jensen |
| **Institution** | USTC / DTU *tentative* (Jilin Hu, Bin Yang, Jensen) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | Time-series forecasting is usually framed as a direct history→future mapping in the **observation space**, but observation sequences give only a partial view of system dynamics, with futures shaped by latent dynamics — so latent-space methods do better. But future observations are *also* shaped by external factors, and **how to make multimodal covariates shape latent-state formation and evolution directly** remains underexplored. **WorldTS** trains in two stages: first learn forecasting-relevant latent state dynamics **conditioned on multimodal covariates**, yielding encoded future states; then **freeze** the state dynamics and train an observation decoder to map predicted future states back to future observations. |
| **Key Innovations** | (1) Puts the covariate signal where the paper argues it belongs — inside latent state formation — rather than bolting it onto the observation decoder, which is the standard shortcut; (2) the **freeze-then-decode** split is what makes the latent dynamics reusable for planning-style use, connecting to the world-model theme in §6; (3) evaluated on **21 real-world datasets**; note the abstract reports effectiveness without headline numbers, so magnitudes are left unquantified here rather than inferred. |
| **Link** | [arXiv:2609.31162](https://arxiv.org/abs/2609.31162) |

### 5.4 STFO: More Sensors Only One Field — Rethinking Continual Spatio-Temporal Forecasting

| Field | Detail |
|-------|--------|
| **Authors** | Lewei Xie, Haoyu Zhang, Jiajun Zhou, Yulong Chen, Guanxing Chen, Yu-An Huang, Hau-San Wong, Yifan Zhang, Zhi-An Huang |
| **Institution** | HKUST / CUHK *tentative* (Hau-San Wong, Zhi-An Huang) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | Continual spatio-temporal forecasting serves traffic management and environmental monitoring under evolving dynamics and **expanding sensor networks**. Conventional graph-based continual learning ties forecasting representations to the *current sensor layout*, so sensor expansion can alter the representation of learned spatial relationships. The key insight: **sensor expansion changes the evidence available about a process without necessarily changing the dynamics to be learned.** **STFO** (Spatio-Temporal Field Operator) parameterizes forecasting knowledge as a **shared field-evolution operator** with **observation and query interfaces**. Normalized coordinate-based aggregation lifts irregular sensor histories onto a **fixed latent grid**, enabling reuse of learned spatial maps across observation sets **without sensor-specific parameters**. To accommodate process drift, a **spectral descriptor** summarizes variation across spatial scales and conditions Fourier propagation and attention; coordinate-based decoding queries the evolved field at sensor locations. |
| **Key Innovations** | (1) The insight is stated as a *distinction* — evidence availability vs dynamics — and the architecture follows it exactly: **no sensor-specific parameters at all**, so sensor expansion is a non-event for the model; (2) the fixed-latent-grid lift is what actually makes map reuse legal under irregular layouts; (3) drift handling via a spectral descriptor that conditions *both* Fourier propagation and attention, rather than one or the other; (4) SOTA average on PEMS-Stream / CA-Stream / AIR-Stream; **STFO-Large reduces average MAE over DOL by 8.4% (PEMS-Stream) and 4.7% (CA-Stream)**. |
| **Link** | [arXiv:2609.31325](https://arxiv.org/abs/2609.31325) |

### 5.5 EPOC: Endpoint-Preserving Online Correction With Compressed Residual State

| Field | Detail |
|-------|--------|
| **Authors** | Takumi Fujimoto, Hiroaki Nishi |
| **Institution** | (inferred academic, JP *tentative* — Nishi) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | Completed multi-horizon forecasts provide residual feedback for a fixed forecaster, but retaining full residual blocks inflates auxiliary state. **EPOC** keeps a **compressed residual state**: low-order DCT coefficients plus **the final value of the preceding residual block**. Within each channel, **the endpoint is shared across component-wise online ridge regressions** that also use current-forecast coefficients; the fitted DCT correction is blended with the base forecast. Evaluated on eight multivariate series with DLinear and PatchTST, three seeds, two training variants — **96 matched fixed-base conditions** at a 24-step horizon. |
| **Key Innovations** | (1) The **shared-endpoint** design is the whole idea — one scalar per channel serves every component-wise regressor, which is why the state is ~75× smaller than ELF; (2) unusually rigorous protocol: **96 matched conditions**, lower paired MSE than δ-Adapter, COSA, FAC and OMPB in a majority of conditions while using less state than each; (3) the state/compute frontier is quantified, not asserted — EPOC **−15.40% MSE / −9.35% MAE** at a **6,352 B** median, vs full ELF's larger −19.29% at **474,048 B (×75)**; (4) two controls that matter: equal-size summary controls favor the endpoint by 1.65–2.20%, and a coefficient-reconstructed endpoint performs similarly — showing the endpoint's *role* is what helps, not its exact value. |
| **Link** | [arXiv:2609.30929](https://arxiv.org/abs/2609.30929) |

### 5.6 When 10,000 Windows Are Not 10,000 Tests

| Field | Detail |
|-------|--------|
| **Authors** | Xinze Shi, Litian Zhang, Binrui Shi |
| **Institution** | (inferred; UIUC cluster *tentative* — Litian Zhang) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | Sliding-window classifiers are routinely evaluated on **thousands of overlapping test windows**, even though neighboring predictions share observations and remain nested within recordings and subjects. Subject-disjoint evaluation prevents one leakage form but **does not make the test windows independent**. The paper presents a practical audit mapping three claims — performance on observed recordings, future recordings from observed subjects, and unseen subjects — to explicit aggregation rules and **dependence-robust inference**. |
| **Key Innovations** | (1) The transferable distinction, stated by the paper itself: **distinguishes additional predictions from additional independent evidence** — this should be applied to every sliding-window evaluation in the literature, not just time series; (2) quantified: at 75% overlap, controlled simulations give **16.9% Type-I error** for IID observed-record inference and **7.2%** for session-centered Bartlett-HAC — better but still miscalibrated; (3) a real audit of frozen WISDM and HARTH predictions shows **~4× growth in test rows buys only 1.75–1.94× variance-equivalent information**, and paired accuracy-difference intervals are 1.22–1.66× the IID widths; (4) a result that changes a conclusion: on HARTH, paired accuracy-difference intervals **include zero across three overlap settings** where **Macro-F1 favors MiniROCKET** — the significance test and the aggregate metric disagree, and the paper says so. |
| **Link** | [arXiv:2609.30721](https://arxiv.org/abs/2609.30721) |

---

## 6. World Models, VLA & Robot Learning

### 6.1 Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data

| Field | Detail |
|-------|--------|
| **Authors** | Ivan Snegirev, Elizaveta Semenyakina, Dmitrii Maliukov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou |
| **Institution** | (inferred *tentative*) |
| **Published** | 25 Sep 2026 (cs.RO) |
| **Abstract** | Simulation enables scalable VLA training via privileged experts, but such pipelines **retain successful demonstrations and discard failed rollouts** — even though failures expose exactly the off-nominal states from which recovery must be learned. **Kintsugi-VLA** converts failed rollouts into targeted synthetic recovery data by exploiting **exact state restoration and branching** in simulation. For a fixed privileged expert it defines **interventional recoverability** — the probability of completing the original task after the simulator is restored to a given state** — estimates it via adaptive Monte Carlo continuations with pointwise Wilson intervals, and characterizes its **non-monotonic** evolution along failed trajectories. These estimates identify an observed **terminal low-recoverability frontier**, used to select informative recovery starting states. |
| **Key Innovations** | (1) Reframes discarded data as the *most informative* data, and justifies it with a **measurement** (interventional recoverability with CIs) rather than intuition; (2) the **non-monotonicity finding** is what makes selection possible at all — a monotone curve would imply only "the later the worse" and no frontier to select against; (3) honest difficulty-matched and frame-budget-matched comparisons: **34.6% and 38.4%** SmolVLA aggregate recovery success, **+5.8 and +6.7 pp** over uniform sampling in the same recovery window; ordering replicates under disturbed execution and shifted clutter/physics; (4) the cost is stated: clean-task success **76.8% → 74.7%**. |
| **Link** | [arXiv:2609.31048](https://arxiv.org/abs/2609.31048) |

### 6.2 Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical VLA

| Field | Detail |
|-------|--------|
| **Authors** | Chuanliang Xie, Boyu Ma, Gen Li, Yizhou Liu, Houwang Chen, Xinyu Zhou, Jianfei Yang |
| **Institution** | (inferred; Shanghai AI Lab / Horizon Robotics cluster *tentative* — Yang, Chen) |
| **Published** | 25 Sep 2026 (cs.RO) |
| **Abstract** | Hierarchical VLA systems pair a high-level vision-language planner with a low-level action expert producing continuous actions. The design has practical value only if the planner is fast enough for real-time control **and** the plans actually contribute to action generation. Studying a π₀.₅-adapted waypoint hierarchy pipeline, the authors find **neither requirement is met**: Token-AR waypoint generation needs **57 expensive VLM forward passes**, yet **erasing the waypoint endpoints has little effect on task success**. Two diagnoses: the planner generates at an **excessively fine granularity**, and the executor **underuses plans** as a control condition. Fixes: **waypoint-aligned block-autoregressive decoding (Block-AR)** and **normalized goal modulation (NGM)** — a layer-wise goal path constrained by phase gating and anti-shortcut training. |
| **Key Innovations** | (1) The negative result is the contribution: **the 57-pass plan was not doing the work** — a well-known architecture failing at its stated purpose, found by ablation of its own output; (2) the two-sided fix is unusually well-matched to the two-sided diagnosis (granularity → Block-AR, underuse → NGM + anti-shortcut), and the **anti-shortcut training** addresses the direct incentive for the executor to ignore the plan; (3) **57 → 8** VLM forward passes (incl. one prefix prefill), **8.7× planning-latency reduction** on a Rokae dual-arm robot; LIBERO-Long **91.0% → 96.2%**, four-suite average **95.85% → 98.45%**. |
| **Link** | [arXiv:2609.30833](https://arxiv.org/abs/2609.30833) |

### 6.3 VLaRL: Augmenting VLA Models with Simulation-Trained Latent-Conditioned Residual RL

| Field | Detail |
|-------|--------|
| **Authors** | Namiko Saito, Kinam Kim, Heecheol Kim, Katsushi Ikeuchi, Yasuyuki Matsushita |
| **Institution** | Keio University *tentative* (Matsushita) |
| **Published** | 25 Sep 2026 (cs.RO) |
| **Abstract** | VLAs provide broad instruction-conditioned manipulation behavior, but physical execution stays imprecise during contact-rich interaction. **Residual RL** can correct such errors while keeping the VLA frozen — but real-robot RL is costly and safety-critical. **VLaRL** trains residual RL for frozen VLAs in simulation and deploys on real robots **without real-world RL or online adaptation**. The key challenge is transferring the learned residual policy despite the sim-to-real *visual* gap. Rather than requiring pixel-level visual correspondence, VLaRL uses **the VLA's internal vision-language latent representation both to condition residual control and as the sim-to-real transfer interface**, plus a lightweight mapper transforming simulation-derived latents toward the real latent distribution. |
| **Key Innovations** | (1) The transfer interface is the **VLA's own latent space** — bypassing the pixel gap entirely rather than closing it, which is the cleaner formulation; (2) freezing the VLA keeps the broad behavior and confines learning to a *residual*, so catastrophic forgetting is structurally impossible; (3) real-world success improves in **all task-backbone combinations** across four contact-rich tasks and two VLA backbones, and controlled ablations show **both** latent conditioning and latent alignment are necessary — so the gain is not attributable to either alone. |
| **Link** | [arXiv:2609.30868](https://arxiv.org/abs/2609.30868) |

### 6.4 OneWorld: Learning Consistent Physics Across Actions in World Models

| Field | Detail |
|-------|--------|
| **Authors** | Ke He, Yichen Ding, Bin Yang |
| **Institution** | USTC *tentative* (Bin Yang) |
| **Published** | 25 Sep 2026 (cs.CV) |
| **Abstract** | Action-conditioned video world models predict scene evolution under different actions — essential for reliable planning — but futures generated *independently* from the same initial scene may each look plausible while implying **incompatible physical properties** (friction, mass). That inconsistency produces contradictory predictions across interventions, making the model's underlying world view incoherent and limiting planning reliability. **OneWorld** is a shared-mechanism counterfactual generation framework that **jointly** models multiple action-conditioned futures under a common latent physical mechanism: a physical-mechanism interpreter infers a distribution over latent mechanisms from each action-outcome branch; these are aggregated into **shared-world evidence** capturing whether branches admit a common physical explanation while accounting for uncertainty in less informative branches; the evidence constrains flow training and guides sampling. |
| **Key Innovations** | (1) Reframes cross-intervention **consistency as the training objective**, not just a metric — a single-rollout world model has no way to be wrong about friction until you compare rollouts; (2) the uncertainty weighting over branches ("less informative" branches) is what makes aggregation sound rather than a vote; (3) a **multi-intervention evaluation protocol** following ACWM-Phys interaction settings, measuring whether generated futures can be *jointly* explained by the same physical parameters, alongside standard single-rollout metrics; (4) improves cross-intervention physical consistency while maintaining competitive single-rollout quality — the trade-off is stated rather than elided. |
| **Link** | [arXiv:2609.30946](https://arxiv.org/abs/2609.30946) |

---

## 7. Evaluation, LLM Judges & Decision Calibration

> Continuing the 09-25 instrument-validity thread. Today's three judge papers each attack a *different* confound — position, evidence protocol, model identity — and the pattern is convergence on **structured correction over volume**: the 09-25 "Accounting for Bias" position (bias correction ≫ more comparisons) is now the field's working assumption.

### 7.1 DIAL: Position-Debiased LLM Judges with Adaptive Human Preference Calibration

| Field | Detail |
|-------|--------|
| **Authors** | Zesheng Cai, Yingqi Fan, Sichang Chen, Jin-Hong Du |
| **Institution** | (inferred academic/industry *tentative*) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | LLMs as judges scale evaluation, but their judgments are **sensitive to response order** and, even after removing position effects, can still **diverge systematically from human preferences**. **DIAL** combines abundant LLM comparisons with *limited* human comparisons to (a) separate judge-specific position effects, (b) learn shared structure in position-debiased LLM preferences, and (c) adaptively calibrate that structure toward the human target. Theoretically it addresses identification of latent LLM preferences / position effects / human calibration, **adaptive estimation balancing LLM anchoring against limited human evidence**, and **fixed-weight uncertainty quantification** for the calibrated preference. |
| **Key Innovations** | (1) The **three-way decomposition** is the real contribution: position effects are *judge-specific*, so a single global debiasing is misspecified by construction; (2) explicit treatment of the *scarce-human-label* regime, which is the actual operating condition in practice — abundant LLM comparisons, few human ones; (3) fixed-weight UQ is unusual and necessary, since calibration with a handful of human labels otherwise produces intervals nobody can trust; (4) the resource is substantial and reusable: **>410K judgments from 21 LLM judges in both display orders**, plus controlled simulations and three human-preference benchmarks showing robustness to unbalanced response order. |
| **Link** | [arXiv:2609.31215](https://arxiv.org/abs/2609.31215) |

### 7.2 BAER: Backbone-Adaptive Evidence Routing for Robust Pairwise LLM Judging

| Field | Detail |
|-------|--------|
| **Authors** | Zeyan Li, Jing Peng, Jianfeng Xu |
| **Institution** | (inferred academic *tentative*) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | Pairwise judges can gather evidence through **direct comparison, reasoning, or reference-based verification**, but no single protocol is best across benchmarks and judge backbones. **BAER** adapts the evidence mechanism while **preserving candidate symmetry**: swapping the two responses may reverse the preference but **cannot change its strength**. It separates each expert's *signed preference* from *candidate-invariant reliability* and builds three symmetric heads — evidence stacking, reliability-based expert routing, and candidate-blind reference verification. Development data select one head per benchmark–backbone condition, and **that choice is frozen before testing**. |
| **Key Innovations** | (1) **Candidate symmetry as a hard architectural constraint** is the cleanest formal statement of position-bias control in this window — invariance is designed in rather than corrected afterward; (2) the decomposition into *signed preference* vs *candidate-invariant reliability* is what makes heads swappable and comparable; (3) the **frozen-before-testing selection** protocol plus "full prediction coverage" answers the obvious objection (that per-condition selection is overfitting); (4) highest test accuracy in **all 8 conditions** (4 benchmarks × 2 8B judge backbones), **+0.87–7.32 points** over the strongest external baseline; the paper's own summary line is the takeaway — *adapting how evidence is gathered beats fixing one protocol everywhere*. |
| **Link** | [arXiv:2609.30751](https://arxiv.org/abs/2609.30751) |

### 7.3 Same Text, Different Numbers: The Divergence of LLM-Based Measures

| Field | Detail |
|-------|--------|
| **Authors** | Hamid Boustanifar, Sasan Mansouri |
| **Institution** | (inferred academic/industry *tentative* — Mansouri) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | Researchers increasingly use generative LLMs to convert corporate text into empirical variables. The paper examines how invariant such measures are to **model choice**, using **thirteen measures** (sentiment, management clarity, uncertainty, answer specificity, climate and political risk) and **seven LLMs from different providers** scoring earnings-call transcripts of **S&P 500** companies. |
| **Key Innovations** | (1) The headline number is a **cross-model rank correlation averaging only 0.52** — i.e. LLM-derived measures are barely half-agreeing instruments; (2) a decomposition that rules out the easy explanation: **transcript-level differences common across providers account for only 34% of total score variation**, so most disagreement is *model-specific*, not shared ambiguity about the disclosure; (3) the negative control that makes it interesting: **cross-model disagreement does not predict subsequent analyst or market disagreement**, so the model-specific component is not merely uninformative — it is *wrong*; (4) model choice materially changes downstream inference (coefficient magnitudes, signs, significance); provider-averaging stabilizes *rankings* but **score levels remain sensitive to which models are in the ensemble**; the prescription is to treat LLM-generated variables as **model-contingent measurements validated across providers**; (5) direct relevance to the wiki's own practice of LLM-scored constructs. |
| **Link** | [arXiv:2609.31013](https://arxiv.org/abs/2609.31013) |

### 7.4 LAVOIR: A Single-Pass Decision Encoder for When and What to Ask

| Field | Detail |
|-------|--------|
| **Authors** | Furkan Yilmaz, Habibe Aleyna Tasdemir, Muhammed Faruk Gozay |
| **Institution** | (inferred academic, TR *tentative*) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | "System One" decision models such as TypeSafe's **Jev** and its open counterpart **Laya** answer typed questions about a text in a single forward pass with calibrated probabilities, but **cannot ask for missing information**: when a first message does not say what separates two departments, they guess. **LAVOIR** (Laya with Value-Of-Information Routing) places candidate pieces of missing information (*slots*) in the input next to the answer options, so **one forward pass returns both the decision distribution and, for every slot, the expected gain in probability of the correct decision if the user were asked about it**. VOI targets need **no human labels**: gold decisions come from schema rules, an LLM only verbalizes messages and answers, a model from another family checks every text, and pairing each message with several profiles makes regression on realized gains estimate the expected gain. A **Gini-impurity cap** bounds the predicted value by what a calibrated model can still gain. |
| **Key Innovations** | (1) **Amortized VOI in the same forward pass** — the decision and the question-worth are computed together, so asking costs no extra model call; this is the structural fix for the Jev/Laya limitation; (2) a **label-free VOI supervision scheme** built from schema rules plus cross-family verification, which is what makes VOI training feasible at all; (3) the Gini-impurity cap is a principled *upper bound on achievable gain* — it converts "when should the model ask?" from a judgment call into a checkable inequality; (4) on seen schemas, decisions are statistically indistinguishable from the **Bayes ceiling**, and the question policy matches a greedy oracle VOI policy (**AUC 0.799 vs 0.797**); at ≤0.5 questions/conversation it is **+14.1 points** over never asking; on real ABCD conversations one real exchange gives **+8.3 points** where LAVOIR asks and nothing where it doesn't; on SGD the cap drops the asking rate **93% → 8.6%**; **31 ms** median on GH200. Directly extends the wiki's Jev thread (PixelJev 09-25, JevAdvBench runner-up below). |
| **Link** | [arXiv:2609.30706](https://arxiv.org/abs/2609.30706) |

---

## 8. Games, RL & Market / Queueing Mechanics

### 8.1 Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents (NetHack)

| Field | Detail |
|-------|--------|
| **Authors** | Bartłomiej Cupiał, Jens Tuyls, Maciej Wołczyk, Davide Paglieri, Martin Klissarov, Benjamin Eysenbach, Piotr Miłoś, Karthik R. Narasimhan |
| **Institution** | Princeton / Google DeepMind cluster *tentative* (Miłoś, Narasimhan, Eysenbach) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | Language agents struggle in environments requiring **long sequences of low-level actions**. Code-based abstractions help by letting agents invoke reusable skills instead of repeatedly selecting individual actions: the code handles recurring local decisions, the LM decides which skills to use and how to combine them. But **abstractions are leaky** — situations beyond a skill's capability may require returning to primitives. Motivated by this productivity/flexibility tradeoff, the paper systematically studies how code-based action abstraction affects performance, inference cost and learning, in **NetHack**, using **CodeHack**, a library of code-based skills with natural-language descriptions. |
| **Key Innovations** | (1) The three-way comparison is the design of the study — primitives-only vs skills-only vs **skills + primitives** — which is what turns "abstractions are leaky" into a measured option space; (2) the headline triple: skills **nearly triple game progression** and **cut inference cost per episode by 86%** vs primitives in zero-shot; (3) the strongest result is the RL one — skill-based agents learn **significantly faster, with a 7.2× larger average gain in dungeon level** over the same training budget, i.e. abstraction changes the *learning* problem, not just the policy; (4) the "path back down to low-level actions" is what preserves flexibility when the library is insufficient; consistent with 09-25's SkillEvoReg (runner-up below) on skill quality mattering, and evaluated across zero-shot, SFT and RL. CodeHack released. |
| **Link** | [arXiv:2609.31076](https://arxiv.org/abs/2609.31076) |

### 8.2 MA-WAM: Multi-Agent World-Action Model for Test-Time Planning

| Field | Detail |
|-------|--------|
| **Authors** | Guowei Zou, Haitao Wang, Guoxin Wang, Beiwen Zhang, Zhiquan Chen, Guojie Wang, Hejun Wu |
| **Institution** | (inferred academic, CN *tentative*) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | Multi-agent cooperative tasks require agents to execute a joint action simultaneously, and each agent's action affects both the observations and responses of the others — so a world model is needed to predict the **team return** resulting from all agents' joint actions. A naive extension applying a single-agent world model per agent's action, step by step, **fails to capture dependencies among simultaneous actions**. **MA-WAM** is a test-time planning framework letting a frozen multi-agent flow policy evaluate futures of candidate joint actions, predicting consequences according to **cross-agent dependencies** and enabling efficient candidate scoring. |
| **Key Innovations** | (1) The failure it identifies is precise: step-by-step per-agent rollout of a *single-agent* world model structurally cannot represent simultaneity — a modeling error, not a tuning error; (2) claimed as the **first test-time world-model planner for multi-agent flow policies**; (3) **mean relative gains of 22.0%** over direct execution and **25.6%** over uniform action selection across **30 offline MARL settings** on MAMuJoCo, SMAC and MPE; (4) the cost is measured on the standard protocol: **+12.1 ms on an A100 = 2.5% of generation-and-scoring time** — cheap enough that test-time planning is a default rather than a luxury. Pairs with G2MAF (runner-up below) from the same group. |
| **Link** | [arXiv:2609.31281](https://arxiv.org/abs/2609.31281) |

### 8.3 Agentic Limit Order Books: Phase Transitions and Market Impact

| Field | Detail |
|-------|--------|
| **Authors** | Jan Rosenzweig |
| **Institution** | (single author, inferred) |
| **Published** | 25 Sep 2026 (q-fin.TR) |
| **Abstract** | Investigates the **systemic macroscopic** dynamics emerging from Limit Order Books populated *exclusively* by autonomous reinforcement-learning agentic traders. By formalizing agent interactions within a microscopic order-matching engine, the paper examines two quantitative phenomena: **equilibrium phase transitions in order-flow regime shifts**, and the structural dynamics of **market impact** — showing agentic LOBs exhibit **distinct phase boundaries separating orderly price discovery from hyper-volatile cascade states**, governed by critical thresholds in the number of agents and observable market depth, and that market impact under agentic liquidity provision **deviates from the classical square-root dynamics**, exhibiting distinct **dissipative, balanced, and non-dissipative regimes** under non-linear feedback loops. |
| **Key Innovations** | (1) The all-agent LOB is a clean **macro-from-micro** construction — every agent is RL, so there is no human anchor to confound the emergent statistics; (2) the square-root market-impact law is treated as a **baseline to be falsified**, and the paper reports a three-regime replacement — that is a substantive result if it holds at scale, and it is exactly the kind of claim that needs independent replication; (3) phase boundaries in *agent count* and *market depth* are stated as **critical thresholds**, which is the practically interesting parameterization; (4) single-author and abstract-level: the mechanisms and the numerical thresholds are not given here, so treat the regime taxonomy as the claim and its magnitude as unverified. |
| **Link** | [arXiv:2609.31260](https://arxiv.org/abs/2609.31260) |

### 8.4 The Price of Thought: Does Test-Time Reasoning Pay in LLM Trading?

| Field | Detail |
|-------|--------|
| **Authors** | Jiayi Chen, Guiling Wang |
| **Institution** | (inferred academic/industry *tentative*) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | Inference-time reasoning promises better decisions, but its higher computational cost may not yield better **economic** outcomes — yet reasoning controls are rarely evaluated as **economic interventions**, where model-output changes must translate into better portfolios *after trading costs*. A controlled study of representative LLMs from the **DeepSeek, GPT and Gemini** families varies reasoning effort while holding information available at each formation date, prompts, output formats and portfolio construction fixed. Coverage: a **full year of U.S. equities** under three input conditions (numerical, identifiable news, masked news), **>800,000 asset predictions** and repeated model generations. |
| **Key Innovations** | (1) The **economic** framing is the contribution — net return *after costs*, not an accuracy or Sharpe proxy computed without them; (2) the headline negative, stated without hedging: across all three families **additional reasoning does not produce a reliable improvement in net portfolio returns**; for DeepSeek, sweeping the full progression from no to maximum reasoning gives a **non-monotonic** curve, so the answer is not "less is more" either; (3) **repeated generations produce unstable treatment effects and portfolio selections** even when overall scores stay similar — i.e. the measurement noise exceeds the effect, which retroactively questions single-run reasoning-budget ablations generally; (4) the three input conditions (including masked news) are what let the authors separate information from reasoning; the implied discipline — validate reasoning budgets **per task** before deploying them. |
| **Link** | [arXiv:2609.30705](https://arxiv.org/abs/2609.30705) |

---

## 9. Theory & Mechanistic Interpretability

### 9.1 The Residual Stream's Effective Depth

| Field | Detail |
|-------|--------|
| **Authors** | Barak Gahtan, Ido Galil, Alex M. Bronstein |
| **Institution** | (inferred; Technion cluster *tentative* — Bronstein) |
| **Published** | 25 Sep 2026 (cs.LG) |
| **Abstract** | Introduces **effective depth** (D_eff), a scalar diagnostic treating the layer-wise residual stream as a **discrete-time process**, measuring how representation similarity decays with layer distance, and aggregating that profile into one number. Across **sixteen decoder-only LMs** it separates a structural consequence of residual accumulation from an empirical one: even maximally diverse orthogonal updates have the closed-form reference `F_L = 2L/(L+1) < 2`, yet **fifteen of sixteen default measurements lie below F_L** (Qwen3.5: 32–44%, OLMo-2: 40–41%, Pythia: 23–28%). |
| **Key Innovations** | (1) The **matched closed-form reference** is the method's strength — it turns "layers are underused" from a vibe into a testable inequality with a theoretical null, and 15/16 falling below it is a real empirical pattern; (2) the paper then *disconfirms the easy explanation* via matched references — the gap is **not** caused by the persistent initial state or update-size imbalance, but is largely a **calibrated signature of correlated residual updates**, explicitly **not** evidence that depth is unused; (3) unusually thorough robustness: symmetric position-0, token-normalisation and top-PC controls; the lone above-reference default outlier joins the same regime under controls, and **all sixteen models are sub-reference after token-normalisation or top-1-PC removal**; (4) a training-dynamics observation — the regime is established early in OLMo-2 and **stable through 5T tokens**, while Pythia-1.4B follows a distinct decreasing trajectory; (5) the authors state the scope limit themselves: D_eff is a **global accumulated-state diagnostic, not a capability score or pruning method**. |
| **Link** | [arXiv:2609.31098](https://arxiv.org/abs/2609.31098) |

### 9.2 FTB Graph: First-token Broadcasters and Language-Identity Head Circuits

| Field | Detail |
|-------|--------|
| **Authors** | Arjun Pillai, Christian Hoang, Anjelo Laroza |
| **Institution** | (inferred academic/industry *tentative*) |
| **Published** | 25 Sep 2026 (cs.AI) |
| **Abstract** | Multilingual LLMs must resolve the target response language **early** in generation, yet the causal circuitry governing **first-token language identity** decisions remains poorly mapped. The paper presents an end-to-end structural circuit analysis across **six model architectures spanning four families** (GPT-2, BLOOM-560M, Pythia-1B/2.8B, Qwen2.5-1.5B Base/Instruct), using **Edge Attribution Patching with FP16 active clamping**, followed by **exact activation patching verification** with a 2,000-candidate-edge search ceiling, extracting directed acyclic graphs driving first-token language broadcasting. |
| **Key Innovations** | (1) A **verification-first circuit methodology** — EAP is used to *propose* candidates and exact patching to *admit* them, and the paper reports that this matters: **EAP scores correlate only weakly with exact patching deltas across most models**, so linear gradient approximations diverge from causal interventions in FP16; (2) honest strength gradation: deep or mid-to-deep broadcasting hubs are observed, but evidence is **strongest for Pythia-2.8B and BLOOM-560M** because GPT-2 and Pythia-1B leave few out-of-graph heads for comparison, and **both Qwen2.5-1.5B variants invert the necessity check** — reported rather than smoothed over; (3) two structural findings: scaling Pythia-1B → 2.8B **expands node participation at similar verified-edge budget → sparser topology**; and Qwen2.5-1.5B base vs instruct circuits retain **84.7% Jaccard similarity including the Layer-27 hub**, indicating first-token routing is established in **pretraining and preserved by instruction tuning**; (4) the EAP-vs-patching divergence is a broadly reusable warning for the mechanistic-interpretability literature. |
| **Link** | [arXiv:2609.30954](https://arxiv.org/abs/2609.30954) |

### 9.3 LocUS: Head Selection and Subspace Projection for Targeted Activation Steering

| Field | Detail |
|-------|--------|
| **Authors** | Irene Tallini, Lorenzo Basile, Valentino Maiorca, Francesco Locatello, Alberto Cazzaniga |
| **Institution** | (inferred; ETH Zürich cluster *tentative* — Locatello) |
| **Published** | 25 Sep 2026 (cs.CL) |
| **Abstract** | Activation steering controls LLMs at inference time without training, but standard approaches estimate a per-layer steering direction from contrastive data and apply it to the layer's **entire representation space**, which may **couple the intervention to off-target properties present in the contrastive data** and degrade unrelated capabilities. **LocUS** (Localized Unembedding Steering) grounds steering to **the model's own output-vocabulary subspace**: it identifies a property-specific linear subspace within the unembedding matrix, enforcing a geometric constraint that restricts the steering transformation to that subspace, and **simultaneously localizes application to a sparse subset of attention heads**. |
| **Key Innovations** | (1) Grounding in the **unembedding matrix** is the clever part — it supplies a *model-intrinsic* notion of "which directions mean this property", so no new supervision is needed and the constraint is meaningful by construction; (2) the two-axis localization (**subspace** × **head set**) is what decouples the intervention from the off-target properties that contaminate contrastive data — the failure mode the paper names; (3) matches or beats SOTA on **toxicity mitigation, sentiment redirection and sycophancy suppression** across three model families while intervening on **<6% of parameters** and better preserving general capability — the headline framing is therefore capability-preserving, not just task-improving. |
| **Link** | [arXiv:2609.31122](https://arxiv.org/abs/2609.31122) |

---

## Runner-ups

All grep-verified **0 hits** in `wiki/` at write time and strictly inside the Fri-25-submitted window (IDs 2609.30642–2609.31371):

| ID | Title / Substance |
|----|-------------------|
| [2609.30904](https://arxiv.org/abs/2609.30904) | **QReason** — decouples query-focused reasoning from window-specific relevance in listwise LLM rerankers: a rewriter generates a ranking-oriented reasoning query **once** and reuses it across sliding windows, eliminating repeated near-identical CoTs; SFT-then-RL training; beats strong reasoning rerankers on BRIGHT with far less redundant reasoning. Directly relevant to production rerank latency budgets. |
| [2609.30906](https://arxiv.org/abs/2609.30906) | **ToolSearcher** — frames **large-scale tool selection** (not small predefined tool sets) as a new challenge for agentic RL, with category-constrained tool discrimination, event-level search modeling, and trajectory-aligned credit allocation; outperforms strong baselines on iterative search and complex tool composition. Pairs with RecToolBench (§1.4) on the tool-orchestration bottleneck. |
| [2609.30734](https://arxiv.org/abs/2609.30734) | **Learning What to Skip (LW2S)** — casts component omission in multi-agent LLM workflows as **counterfactual credit assignment**: controlled skip interventions over full-workflow logs train action-specific safety models; reduces token cost while matching or improving accuracy across math, MCQ and code with two instruction-model families, with a shared-error analysis showing why agreement alone is insufficient for skip selection. |
| [2609.30861](https://arxiv.org/abs/2609.30861) | **SkillEvoReg** — treats repeated agent skill updates as a learning process subject to **overfitting**: skill dropout, complexity-aware local regularization, and causal counterexample validation; across SkillOpt / SkillEvolBench / ContinualSkillBench it controls skill-state growth while preserving capability and finds update-level regressions structural metrics miss. Companion to CodeHack (§8.1). |
| [2609.30967](https://arxiv.org/abs/2609.30967) | **MoMHa** — casts the LLM **harness** (prompt construction, routing, output parsing) as a first-class, inherently multi-objective design surface (accuracy, behavioral safety, token cost); a joint-reward agentic proposer beats a two-phase accuracy-then-tokens ablation and accuracy-only baselines — joint mean 0.482 vs 0.198–0.422 synthetic, 0.461 vs 0.377 real-world — with harness strategies transferring to unseen benchmarks without retraining on 8/12 target models. Extends the 09-25 "Control the Harness Control the Cost" thread into optimization. |
| [2609.30797](https://arxiv.org/abs/2609.30797) | **HasMem** — resizing continuous agent memory changes a frozen LLM's input, coupling capacity allocation with readout; frozen hard-prompt embeddings give a verifiable initial state, a controller adjusts widths, and Reader/Global adapt readout. Lexical F1 **95.3 (+4.4 pp)** on a 535-question MSC reconstruction probe at 93.6% of reference memory positions; +8.0–23.6 pp EM over rule-based re-encoding; LongMemEval-S local F1 3.4 → 8.9, NLL 12.257 → 5.274 — with the honest caveat that F1 gains come with lower EM. |
| [2609.30813](https://arxiv.org/abs/2609.30813) | **Correlated Promotion Benchmark (CPB)** — shared agent memory cannot treat repeated claims as independent evidence; across eight admission policies and four agent families, source-deduplicating policies reject many true claims, coverage-preserving ones admit nearly as many false claims, and gating on declared source type cuts false adoption to 0.06–0.09 (vs 0.22–0.47). Once an uncontested false belief enters, the consumer asserts it in **0.97–0.99 of probes** across all families; no non-oracle policy consistently rejects verbatim copies, paraphrases, and paraphrases-declared-authoritative. |
| [2609.31054](https://arxiv.org/abs/2609.31054) | **Cheap, open agents make LLM pollution harder to mitigate** — nine agent configurations from fully-open to commercial autonomously completed surveys with multiple detection checks; fully open agents ran locally with no usage fees and performed competitively, **open and commercial agents fail different checks** with no single check detecting all agents, and **open-text responses discriminate best between agents and humans** — motivating multilayered detection weighted to open text. |
| [2609.31186](https://arxiv.org/abs/2609.31186) | **Evolutionary Safety of Recursive Self-Improvement** — poses safety not as a state but as a property that must **persist, accumulate and propagate** through recursive self-improvement; a taxonomy over persistent agent state, model state, evaluation/environmental feedback, computational substrate and meta-level update mechanisms, with recurring manifestations (intent drift, error accumulation, experience contamination, safety-property erosion, evaluator drift, risk propagation) and governance principles for modification, selection, authorization, provenance and recovery. Pairs with 2.1's *recursive* framing from the safety side. |
| [2609.31093](https://arxiv.org/abs/2609.31093) | **PISA: Block Sparse Attention with Log-Linear Complexity** — conventional block selection still scores all query-block pairs, so it stays quadratic. A **coarse-to-fine pyramid of keys** with LogSumExp scoring over a bounded candidate set at each level yields `O(N log N)` overall; hardware-aware Triton kernels fuse hierarchical routing and LogSumExp **without materializing the QK score matrix**; comparable commonsense-reasoning performance, better on retrieval. |
| [2609.31261](https://arxiv.org/abs/2609.31261) | **MoSAR** — argues attention approximation is a **geometric** problem, not a sparsity pattern: input-conditioned query/key routers after positional encoding select mixtures over short/medium/global regimes, inducing a continuous distance-dependent attention field. At matched 500M scale it learns a **lower-reach geometry without degrading LM quality** (better perplexity than dense RoPE at training length), **best perplexity under length extrapolation including vs ALiBi**, and the learned geometry survives deterministic top-1 discretization — so it is approximable, not just adaptive. |
| [2609.30820](https://arxiv.org/abs/2609.30820) | **Quantizing Looped Transformers** — separates two failure modes of PTQ on weight-reusing architectures. **Feedback exposure**: per-channel INT4 fails mainly at the non-residual loop-entry adapter (quantized layers perturb recurrent state with no identity path, and the error is fed back at later steps), reproduced on linear filters and Mamba. **Calibration blindness**: one-step GPTQ builds its Hessian from step-0 activations, leaving later-recurrence input directions nearly unweighted — across **nine checkpoints from seven looped architectures, one-step GPTQ is worse than round-to-nearest on five**; accumulating the Hessian across recurrence steps beats both on all nine and recovers bf16 accuracy on Huginn. Read with G²PTQ (§4.5). |
| [2609.30950](https://arxiv.org/abs/2609.30950) | **Low-Bit Recurrent States in Hybrid Language Models** — derives distortion weights from the **observability Gramian**, combines them with normalized state ranges for mixed-precision bit allocation **without calibration data, rotation, or training**, and quantizes decay rates logarithmically. Four-bit mean payload cuts excess NLL by **3.3–27.9×** vs the best of seven baselines across three hybrid models; at six bits NLL is within 0.005 nats of the FP32-state baseline; ablations separate variable widths, decay weighting, and range normalization. |
| [2609.31306](https://arxiv.org/abs/2609.31306) | **Benchmarking Attention for Tabular Foundation Models** — TabPFN/Mitra/ConTextTab alternate row and column attention over 2-D latent sequences, a setting where efficient-attention work (built for 1-D) barely applies; reproducible benchmark across Torch SDPA, FlashAttention-2/3/4, vLLM and SageAttention on A100/H100/B200. Findings: **optimal backend differs between column and row attention and across hardware and model**, cuDNN sometimes wins for column attention at long sequences with head-dimension-dependent crossovers, and SageAttention is strong for row attention beyond 16k rows. |
| [2609.31351](https://arxiv.org/abs/2609.31351) | **Progressive Memory Transformer** — time series carry structure at three scales simultaneously (fine variation, mid-range motifs, global properties) and downstream tasks operate at correspondingly different scales, yet SSL methods supervise globally via instance-level contrastive losses. PMT enforces the hierarchy **independently** at each scale via writable, window-aligned memory that exposes the mid-range scale; strong low-label (1–5%) classification across seven UCR/UEA/UCI benchmarks plus forecasting, with memory states shown to capture mid-range motifs. |
| [2609.31315](https://arxiv.org/abs/2609.31315) | **LUCID** — unobserved common causes induce spurious associations that causal discovery mistakes for direct edges. A **regime-adaptive deconfounding layer** first estimates the confounding regime from data via a **Marčenko–Pastur spectral router**, then applies the matched strategy, recovering lag-0 structure from innovations with edge selection calibrated against a data-driven edge-free null. Best family-weighted directed, lag-resolved graph F1 (**0.60**), +0.19 absolute (~46% relative) over the strongest baseline on a synthetic OOD benchmark; wraps three existing discovery engines; code at `bloomberg/causal-ts`. |
| [2609.31142](https://arxiv.org/abs/2609.31142) | **JevAdvBench** — the first adversarial benchmark for **RLCD** (RL for calibrated decisions) models, which return a well-formed answer even when manipulated, so existing adversarial benchmarks score the wrong thing. Key idea: score each attacked decision against **the model's own clean decision** and against the change caused by an identical re-run. 812 typed questions / 66 scenarios; 9,744 single-edit black-box variants with billed input tokens confirming each edit landed. On jev-1.13.0 rewording stays within 1.2 pp of re-run baseline, but **one unverified opinion appended to the state flips 12.1% of decisions** (tied with the strongest injected command, 10.1%) and pushes **38% of confident answers below the 0.8 review threshold** — so RLCD state must be treated as untrusted, argued input. Direct follow-up to the wiki's Jev thread. |
| [2609.30679](https://arxiv.org/abs/2609.30679) | **Design-Ignoring versus Design-Respecting World Models for Epidemiology** — world models learn from records shaped by study design (assignment, sampling, measurement), so a model can reconstruct observed trajectories while learning an intervention contrast that depends on *how records were collected*. Formalizes study design as constraints on latent-world interface, action mechanism, observation likelihood and target readout. Holding latent structure and fitting settings fixed on a large cluster-randomized test-negative trial, both models achieve comparable factual reconstruction, yet across **500 paired resampling experiments** median contrast changes are substantial for the design-ignoring model versus merely marginal for the design-respecting one. The methodological lesson generalizes: **factual reconstruction does not establish design alignment**. |
| [2609.31214](https://arxiv.org/abs/2609.31214) | **Which Influence Are We Estimating? Counterfactual Specifications in Data Attribution** — influence estimators produce incompatible rankings, usually blamed on approximation error. The paper argues the more fundamental source is **specification mismatch**: influence depends on the attributed behavior, the intervention per training example, and the counterfactual training process, especially when a tractable surrogate (query loss, logit, margin) is required. Formalizes influence as a counterfactual estimand, distinguishes specification mismatch from approximation error, organizes representative estimators by implied specification, and derives a local decomposition. **Behavior-aligned specifications identify target-specific examples obscured by default loss-based or similarity-based ones** — specification analysis should precede comparing influence estimators. |
| [2609.31181](https://arxiv.org/abs/2609.31181) | **Where a Model Sends Its Own Repeated Token** — black-box model identification via degenerate input: for each token *t*, read `argmax p(·|t,t)` in one forward pass to get a map on the vocabulary. The fixed-point half is reported as a **failed estimand** (natural distance is 83% cardinality, separates a corpus manipulation by two bits in 3471 against a precision floor of zero, attributes families at 0.5833). The non-fixed-point half is unrecorded: pairing on the source token removes the cardinality confound by construction (r from 0.9128 to −0.0932) and attributes families at **0.8333** (12 models vs pool of 19; chance 0.1389), clearing two nulls (frequency-matched 0.1429, independent marginals 0.0798). Recurrent architectures cluster at **balanced accuracy 1.0** vs 0.7895 majority rate, or 0.90 excluding each model's dominant destination. Robustness envelope measured: 8-bit weight rounding moves the map *less* than deduplicating the training corpus (0.9004 vs 0.6353), 4-bit destroys it (0.0098). All estimands and kill conditions registered before the data. |

**Additional screened, not featured** (single-paragraph abstracts, peripheral to this report's scope): [2609.31286](https://arxiv.org/abs/2609.31286) **G2MAF** (test-time critic-gradient guidance for frozen multi-agent flow policies; 20/24 settings improved, +9.2% MPE / +8.9% SMAC at ~6% latency — same group as MA-WAM §8.2); [2609.31016](https://arxiv.org/abs/2609.31016) **Robust Successor Features** (unifies successor representation with robust RL under unknown transition kernels for linear MDPs, with a GPI bound that degrades with kernel mismatch and recovers successor-feature guarantees when dynamics are shared); [2609.31099](https://arxiv.org/abs/2609.31099) **Collision-free Movement on Grids and Beyond** (parameterized complexity of coordinating robots to a connected target formation minimizing total travel — extends both minimizing-movement and MAPF, on grids, planar and unit-disk graphs); [2609.30812](https://arxiv.org/abs/2609.30812) **Dynamic Service Recommendation with Congestion-Dependent Joining** (finite-horizon stochastic optimization: recommending to a service now creates congestion that deters future customers; a quasi-polynomial approximation plus a (1−1/e) LP-guided algorithm, and **monotone joining is a tractability boundary** — without it the problem is NP-hard to approximate within any constant factor); [2609.30702](https://arxiv.org/abs/2609.30702) **From Bilateral Trade to Matching Markets** (second-best gains-from-trade guarantees extend to matching markets; exact worst-case ratio **≈0.72490721** for bounded monotone-hazard buyers, **8/9 at m=2** and a limit of **4/5** as types grow, tight already in bilateral trade); [2609.30948](https://arxiv.org/abs/2609.30948) **PORL** (pretrained online RL + KL-constrained offline fine-tuning for job-shop scheduling; lower optimality gaps than standalone offline RL and scheduling baselines, with the advantage **growing as dataset quality degrades**); [2609.31361](https://arxiv.org/abs/2609.31361) **Dynamic Asymptotic Decomposition** for sub-10-second industrial telemetry (proves autoregressive mutual information decays exponentially to zero at long lead times and the optimal minimum-variance estimator converges to the periodic diurnal baseline, then transfers authority from kinetic AR to diurnal equilibrium — 78.3% MAE reduction vs Deep LSTM at 0.72 ms edge execution; single-author, and the 16-window protocol is unusually well specified); [2609.30859](https://arxiv.org/abs/2609.30859) **The Residual Stream** companion [2609.30996](https://arxiv.org/abs/2609.30996) **Linear Representation Hypothesis for VLA** (signature-based formulation unifying representations and policies for embodied quantities that co-evolve with system dynamics; a signature GLM for stochastic action chunks yields monotonic expected-QoI change along linear parameter paths, enabling linear steering, verified in an oracle navigation setting); [2609.31313](https://arxiv.org/abs/2609.31313) **Towards VLA-Dreamer** (explicitly a *concept paper*: predictive world model trained on the VLA vision encoder's **embedding space** rather than pixels, plus short-term planning by sampling VLA actions given goal images — its stated purpose is to test whether VLA embeddings are action-relevant, which is a well-posed question rather than a claim).

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **⚠️ The rec/ads drought ends, and it ends industrially** | KuaFu (Tencent, **GMV +1.37% over ten months in production**, 190 GPUs saved, 4B > 8B at equal compression) is the strongest industrial rec artifact in days; UA-TWM turns the ranker into a future-state decider; Laplacian positional embeddings replace ordinal position with item-space structure; RecToolBench finds valid tool calls ≠ successful recommendations; SPADE's user-specific Pareto frontier; Meta's Component Benchmark for submodule-level profiling; ZooWork-ShopRanker uses multi-family judge panels to manufacture the pairwise labels e-commerce lacks. **Still absent: end-to-end CTR prediction and ad-auction papers** — the drought is broken for recommendation, not yet for ads ranking. |
| **On-policy distillation consolidates into a full failure map** | DCE+SRCL (**+35.62 pp over OPSD**) attacks *teacher staleness*; TISD attacks *the data-collection bottleneck* (teacher disagreement as branch proposal); MOPD-Router/ExpertAlign attacks *prompt-level domain labels* (**+12.3%** unlabeled, +7.8% while ignoring available labels); Persistent Negatives attacks the *moving negative distribution* in black-box OPD; TISD and DCE+SRCL together show the 09-25 S²D-OPD finding generalizes — dense/low-divergence supervision is not the only problem, **branch coverage and teacher freshness are separate axes** |
| **Games become a reasoning-data source** | SPSD turns MuZero-style board-game self-play into superhuman CoT: math mean **24.1 → 36.6** with no human labels, *and* held-out game win rate 15% → 45% — transfer without sacrificing the source task. NetHack CodeHack shows skills nearly triple progression, cut cost 86%, and make RL **7.2× faster** — abstraction changes the learning problem. Agentic LOBs propose a three-regime replacement for square-root market impact. |
| **Agent authorization converges on "no LLM in the decision path"** | MetaPermit (**LLM infers meta-attributes, fixed policy decides**, +31% consistency, +109% task completion, zero malicious calls), AGATE (**no LLM in the decision path**, parameter-bound expiring use-limited grants, 63/63 replay agreement) and EffectMatch (**validate the persistent result, not the approved action**) arrived independently in one window — the 09-25 Hard Stop autopsy's containment argument now has a software-side counterpart. AgentXploit adds the pre-deployment red-team loop (59.3% vs Codex 38.4%; 46.3% at matched budget). |
| **A new, non-adversarial RAG threat** | Stale-document poisoning: outdated evidence flips **30%/37%** of Llama/Qwen answers *with no instruction to trust the document*, rising to **66%/75%** with explicit follow instructions — instruction-following makes it *worse*. Isolate by varying only the evaluation date; mitigation is a recency-aware re-ranker (−4.6–10.0 pts) **conditional on accurate dates**. |
| **KV cache is understood as a three-regime system** | The SoK derives hardware-specific **crossover lengths** where KV traffic overtakes weight traffic — below it, compression buys nothing; and separates *lossless-but-capacity-addressed* (paging, prefix sharing) from *bandwidth-cutting-but-lossy* (quantization, eviction) — the category error the field repeats. CacheReforge (mixed-version caches, 5.44% of layers, −92.4% KL) and Beyond-Mean-Attention (MMR-style diversity, +1.1 macro on 13/16 LongBench, a mid-layer sign flip worth +13.2) are the concrete instances. DynBranch names the agentic-specific blocker: **the cache key is unknowable until the branch resolves**. |
| **Agentic RL's hidden tax is finally measured** | WeEnv: environment overhead is **up to 53.4% of iteration time**; layer-group packaging + on-demand fetch + elastic quota cut it to **9.1%** (5.6–14.2× faster init than E2B/Docker/AgentENV), deployed for agentic RL at WeChat. The insight generalizes: the cost was in the *dependency graph*, not the container. |
| **Sequential modeling: shared compression, structural positions, and honest statistics** | KuaFu's item-level compression (2–4 tokens/item) and Laplacian positional embeddings both attack *what the unit of a sequence representation should be*; EPOC shows a **shared endpoint** can beat much larger residual state (6,352 B vs 474,048 B) and quantifies the frontier; the sliding-window audit establishes the transferable rule — **additional predictions are not additional independent evidence** (~4× rows → 1.75–1.94× information; 16.9% Type-I error at 75% overlap) — and overturns a HARTH conclusion. |
| **Evaluation instrument validity, third consecutive window** | DIAL decomposes position effects as *judge-specific* and calibrates adaptively under scarce human labels (**410K judgments, 21 judges, both display orders** released); BAER makes candidate symmetry an architectural constraint and wins **8/8** conditions with frozen-before-test selection; Same-Text-Different-Numbers shows cross-model rank correlation of just **0.52** on 13 LLM measures of S&P 500 transcripts, with only 34% of variation shared — so these are **model-contingent measurements**; LAVOIR gives Jev/Laya amortized value-of-information (AUC 0.799 vs 0.797 oracle, Bayes-ceiling decisions, 31 ms). The field's working assumption is now **structured correction over volume**. |
| **Interpretability: theoretical nulls and verification-first circuits** | Effective depth supplies a **closed-form reference** `F_L = 2L/(L+1)` and finds 15/16 models *below* it — then disconfirms the easy explanation (correlated updates, not unused depth) via token-normalisation and top-PC controls. FTB Graph finds **84.7% Jaccard** base/instruct circuit overlap (first-token routing set in pretraining) and, more usefully, that **EAP scores correlate only weakly with exact patching deltas in FP16** — a warning the whole circuit-analysis literature needs. LocUS grounds steering in the unembedding matrix, intervening on **<6% of parameters**. |

---

## Window Notes & Honesty Ledger

- **Window**: 396 unique papers `submittedDate = 2026-09-25`, IDs **2609.30642–2609.31371**, 25 categories, pagination to exhaustion. This is the batch arXiv will announce **Monday 28 September ~20:00 ET**; the `/list/{cat}/new` pages still show the Friday 25 September batch (max ID 2609.30258) claimed by today's sibling reports.
- **⚠️ Concurrency / double-claim, disclosed rather than papered over**: the freshness grep (all 396 IDs → 0 hits in `wiki/`) was run **before** [arxiv-paper-check](arxiv-paper-check.md) for 2026-09-28 existed; that report was written **in parallel** and spans a **strictly wider** window (2609.30361–2609.31373, 1,013 papers) that **contains** all 396 of mine. Post-write diff: **21 of the 77 papers I cite are shared**, **56 are exclusive to this report**. Both reports agree on every shared paper (spot-checked: KuaFu, UA-TWM, RecToolBench, Component Benchmark, SPADE, Laplacian-PE, AGATE, EffectMatch, Stale-Document Poisoning, DIAL, BAER, Same-Text-Different-Numbers, JevAdvBench, Recursive-OPD, Price-of-Thought, CPB, MOPD-adjacent items — same authors, same framing, same numbers in both). The division is by **selection lens**: `arxiv-paper-check` = broad daily check; this report = topic-screened rec/ads/LLM/agents/games, which is why §1 is much deeper here and why this report is the one that caught the rec-and-ads cluster. **Process lesson for the scheduler: the 2026-09-28 arxiv jobs are not serialized — a claim-registry or a deterministic claim order is needed, or one report's `created` timestamp must gate the others' freshness checks.** Until then, treat same-day arxiv siblings as a single corpus and do not treat any individual "grep-verified 0 hits" claim as final.
- **No weekend reports**: 2026-09-26 and 2026-09-27 have no synthesis directories, so the entire Friday batch was unprocessed until this run. This report therefore covers a 1-day submission window that is *3 days old in wall-clock terms*.
- **Affiliations**: arXiv does not print affiliations on abs pages. Two are **confirmed from abstract text** (KuaFu → Tencent; WeEnv → WeChat). All others are author-inference and marked *tentative*; several are inferred only from author-name clusters (e.g. Meta for §1.6, LG AI Research for §5.1, USTC for §5.2/§5.3/§6.4). Treat institution attributions as hypotheses, with the exception of the two confirmed ones.
- **Unquantified magnitudes, deliberately left so**: WorldTS (§5.3) reports effectiveness on 21 datasets without headline numbers; Agentic LOBs (§8.3) gives a regime taxonomy without thresholds in the abstract; PISA and MoSAR (runners-up) report comparative but not absolute figures. No figures were inferred or estimated.
- **Weakest evidence in this report**: §1.7 AgentRecommender (single author, concept stage, no benchmark in abstract), §3.6 The Crowd in the Machine (single author, case-study tier, strong framing / thin data), §8.3 Agentic LOBs (single author, no thresholds reported), §4.1 KV Memory Wall (single author — though it is an SoK, where single authorship is less costly than for an experimental claim).
- **Contradiction with sibling reports — resolved, not hidden**: (a) today's [arxiv-ai-search](arxiv-ai-search.md) states the whole arXiv API max ID was 2609.30258 with no paper newer than the Fri-25 batch, and predicts the next genuinely new window appears on the **2026-09-29** run. That was true at its fetch time and concerns the **announcement** pipeline. This report uses the API's `submittedDate` field, which is visible immediately and one announcement cycle ahead of `/list/new`, so it reports the *next* batch a day early. **The two are not in conflict about data** — they read different fields — but the practical correction stands: for arXiv-daily purposes, **`/list/{cat}/new` is the ground truth for "what is announced", and `submittedDate` is a one-day-early forward view.** (b) The 09-28 [arxiv-paper-check](arxiv-paper-check.md) already independently corrected (a) the same day by noting that a `cat:`-scoped query cannot bound a global window — **this report agrees and extends the rule: never bound a window from a per-category `/list` page, a `cat:`-scoped query, or a freshness grep run in parallel with a sibling writer.** The 09-29 run should confirm this batch and should not re-claim the 396 IDs.
- **Rec/ads status correction**: the sibling arxiv-ai-search report recorded a "~14th consecutive window with no new end-to-end CTR/ad-bidding work" in the *remainder* pool. That remains true for CTR prediction and auction specifically. This window adds 8 recommendation / e-commerce-ranking papers (KuaFu explicitly on the **advertising** platform, but for user-profile construction, not ad ranking). **The distinction is maintained deliberately: recommendation is no longer dry; ads ranking still is.**
- **Cross-theme continuations from 09-25**: Jev/Laya is now a *three-paper* line in this wiki (PixelJev 09-25, JevAdvBench + LAVOIR here) and is a candidate for promotion to a `wiki/methods/` page. Effective depth, EAP-vs-patching divergence, and the shared-endpoint trick all extend threads already present.

(End of this report — **47 featured papers across 9 sections + 30 runner-ups = 77 cited**, verified by link count with zero overlap between the two sets. Window JSON deleted from the pre-approved temp dir after the run.)
