---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-18 Daily Edition"
type: synthesis
created: 2026-11-18
updated: 2026-11-18
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR&sortBy=submittedDate&sortOrder=descending&max_results=200
  - https://export.arxiv.org/api/query?search_query=cat:cs.LG&sortBy=submittedDate&sortOrder=descending&max_results=200
  - https://export.arxiv.org/api/query?search_query=cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=200
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=200
  - https://arxiv.org/abs/2611.20445
  - https://arxiv.org/abs/2611.20405
  - https://arxiv.org/abs/2611.21251
  - https://arxiv.org/abs/2611.21241
  - https://arxiv.org/abs/2611.21486
  - https://arxiv.org/abs/2611.20403
  - https://arxiv.org/abs/2611.20377
  - https://arxiv.org/abs/2611.21538
  - https://arxiv.org/abs/2611.20671
  - https://arxiv.org/abs/2611.20644
  - https://arxiv.org/abs/2611.20605
  - https://arxiv.org/abs/2611.20844
  - https://arxiv.org/abs/2611.21852
  - https://arxiv.org/abs/2611.21964
  - https://arxiv.org/abs/2611.22098
  - https://arxiv.org/abs/2611.20381
  - https://arxiv.org/abs/2611.20398
  - https://arxiv.org/abs/2611.20608
  - https://arxiv.org/abs/2611.20691
  - https://arxiv.org/abs/2611.20726
  - https://arxiv.org/abs/2611.20734
  - https://arxiv.org/abs/2611.20811
  - https://arxiv.org/abs/2611.20702
  - https://arxiv.org/abs/2611.20034
  - https://arxiv.org/abs/2611.20771
  - https://arxiv.org/abs/2611.22115
  - https://arxiv.org/abs/2611.21974
  - https://arxiv.org/abs/2611.22191
  - https://arxiv.org/abs/2611.22215
  - https://arxiv.org/abs/2611.20882
  - https://arxiv.org/abs/2611.22171
  - https://arxiv.org/abs/2611.22103
  - https://arxiv.org/abs/2611.21299
  - https://arxiv.org/abs/2611.22085
  - https://arxiv.org/abs/2611.21020
  - https://arxiv.org/abs/2611.21449
  - https://arxiv.org/abs/2611.22055
  - https://arxiv.org/abs/2611.22017
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, NeurIPS2026, ICLR2026, ICLR2027, KDD2026, KDD2027, CVPR2026, ACL2026, EMNLP2025, EMNLP2026, SIGIR2026, WWW2026, CIKM2025, RecSys2025, IAAI27, recommendation, advertising, CTR, LLM, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-18 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-18 每日版）

> Curated digest for the requested venues — **ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025** — plus recent arXiv work in AI, LLMs, recommendation systems, advertising, CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks. Focus organizations/labs: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top labs.

## Method, data window & limitations

- **Query date:** 2026-11-18. **Web search:** unavailable/cancelled in this environment (`Web search cancelled`). **arXiv access:** arXiv Export API (`export.arxiv.org/api/query`) over HTTPS was reachable; 10 category/keyword queries (cs.IR / cs.LG / cs.CL / cs.AI / cs.CV / cs.GT / cs.MA + rec/ads/agent/code-topical sweeps, up to 200 results each, sorted by `submittedDate`) returned **1,260 unique papers** after dedup.
- **Fresh window:** **2026-11-15 → 2026-11-17 submissions** (IDs ~2611.19xxx–2611.222xx), emphasizing the newest 11-16/11-17 batch. Every selected ID was grep-verified absent from the ~9,800 arXiv IDs already referenced in `wiki/**`, hence new to the wiki. The same-day sibling reports `arxiv-paper-check.md` and `arxiv-ai-search.md` cover other 11-16/11-17 papers; overlap is avoided by construction (their IDs are already in the wiki).
- **Affiliations:** recovered from **arXiv PDF page-1 author blocks (pypdf) for all 38 selected papers**, not just from metadata; organization mentions in titles/hardware names were checked against the PDFs (e.g. "NVIDIA B200"/"NVIDIA GB10" are *platforms*, not necessarily affiliations — the actual affiliation of 2611.21974 is ThakiCloud).
- **Coverage reality:** the exact requested venues had **no new main-track paper discoverable in this fresh submission window**. The window is instead dominated by **NeurIPS 2026** tags (main track, Datasets & Benchmarks, workshops), with two **ICML 2026 published-proceedings** papers (PMLR 306), one **EMNLP 2026 Main** paper, and several **forward-dated / adjacent** tags (**KDD 2027, ICLR 2027 decision-pending, AAAI 2027 IAAI-27, CVPR 2027 submission**) which are reported verbatim and flagged. No proceedings/OpenReview crawl was possible (web search unavailable; dynamic pages).
- **Evidence:** all metrics/results are **author-reported** unless noted; no experimental table was invented. Chinese titles are translation aids. Full-text review beyond page 1 was not performed.

---

## 1. Venue snapshot

| Venue | Status (as of 2026-11-18) | Notes for this digest |
|---|---|---|
| **ICML 2026** | Completed (PMLR 306, Seoul) | **2 published-proceedings papers** found in the fresh arXiv window (§2). |
| **AAAI 2026** | Completed | No new AAAI-2026 paper; see AAAI **2027 IAAI-27** applied paper (§4). |
| **NeurIPS 2025** | Completed | No new 2025-tagged item; see NeurIPS **2026** (§3, dominant source). |
| **ICLR 2026** | Completed | No new ICLR-2026 main-track paper; an **ICLR 2027** decision-pending audit is flagged (§4). |
| **KDD 2026** | Completed | No new KDD-2026 item; **KDD 2027** papers included and flagged (§4). |
| **CVPR 2026** | Completed | No new CVPR-2026 item; a CVPR **2027 submission** noted in §8 flags only. |
| **ACL 2026** | Completed | No new ACL-2026 item in window. |
| **EMNLP 2025** | Completed | No new 2025-tagged item; **EMNLP 2026 Main** paper included and flagged (§4). |
| **SIGIR 2026** | Completed | No new SIGIR-2026 item in window (cs.IR papers below are untagged preprints). |
| **WWW 2026** | Completed | No new item. |
| **CIKM 2025** | Completed | No new item. |
| **RecSys 2025** | Completed | No new item. |
| **NeurIPS 2026** (in-window) | Active submission tags | **Dominant source**: 13 papers across main track, workshops (Meta-Agents, IAB, DiffuLM, Sim2Science, Continual Learning, Evaluation of Interactive Agents, InterpScience) and D&B (§3). |
| **EMNLP 2026 / ICLR 2027 / KDD 2027 / AAAI 2027 IAAI-27 / CVPR 2027** | Adjacent / forward-dated tags | Included and explicitly labeled (§4, §8). |

---

## 2. ICML 2026 — Published proceedings (PMLR 306)
### ICML 2026 — 已发表论文集

### 2.1 xFedAlign: Explainable Federated Learning via Global-Local Attribution Alignment
**xFedAlign：通过全局-局部归因对齐实现可解释联邦学习**

- **Authors / 作者:** Dawood Wasif, Terrence J. Moore, Chang-Tien Lu, Jin-Hee Cho
- **Affiliation / 机构:** Virginia Tech (Dept. of Computer Science, Falls Church, VA); DEVCOM Army Research Laboratory (Adelphi, MD) — PDF page-1 footnote
- **Venue / 会议:** **ICML 2026**, Proceedings of the 43rd International Conference on Machine Learning, Seoul, South Korea, PMLR 306 (arXiv comment; 26 pages, 2 figures, 9 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Federated learning (FL) trains on-device without centralizing data, but explanations are hard to make both *locally faithful* and *globally consistent* under privacy/bandwidth limits. Prior work either silos explanations per client, transmits heavy/sensitive artifacts, or replaces the task model with an interpretable surrogate that loses accuracy.
  - **Methodology:** Model-agnostic **xFedAlign** decouples task optimization in parameter space from explanation coordination in a compact *group space*. Each client distills a lightweight surrogate producing private per-class **top-k attribution artifacts**; the server robustly aggregates them into a **Global Explanation Prior** that softly aligns client explanations without constraining task learning.
  - **Innovations:** private attribution artifacts + server-side global prior; model-agnostic; only a few kilobytes of extra communication per round.
- **Comparison & results / 对比与结果（author-reported）:** Across image, text and tabular benchmarks with IID and non-IID partitions, xFedAlign **matches FedAvg accuracy** while consistently reducing explanation drift and improving **deletion and insertion AUC** vs Local-XAI, FedAttr-Agg and Fed-XAI; privacy evaluation shows reduced membership-inference advantage and higher resistance to attribution poisoning.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20445) · [PDF](https://arxiv.org/pdf/2611.20445)

### 2.2 Refusal Register is Causally Steerable: Decomposing the Refusal Direction into Category-Aligned Components in Gemma-2-9B-IT
**拒绝语域可被因果操控：在 Gemma-2-9B-IT 中将拒绝方向分解为类别对齐的分量**

- **Authors / 作者:** Janhavi Khindkar, Nataliia Povarova
- **Affiliation / 机构:** **Independent Researcher** (PDF footnote: "Independent Researcher"; correspondence `research.iiit.ac.in`) — *not* an IIIT campus affiliation
- **Venue / 会议:** Code repository tagged `valueshift-icml-2026`; arXiv comment has no explicit acceptance note and PDF is marked "Preprint" — **treat as ICML-2026-associated, acceptance unverified**
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Arditi et al. (2024) showed refusal can be ablated via one residual-stream direction; later work found multiple directions/concept cones. This paper asks whether refusal directions encode *register* — **how** the model refuses, not only **whether**.
  - **Methodology:** In Gemma-2-9B-IT, two SVM-derived linear directions at layer 20: **B1** (harmful-content vs neutral), **B2** (self-reference vs neutral), with cos(B1,B2) = **0.252** (~75°, far from parallel). Adding the harmful-vs-neutral difference-of-means direction (cosine 0.68 with B1) to the residual stream of self-reference prompts at α = 2.0.
  - **Innovations:** category-aligned decomposition of the refusal direction; causal switch of refusal *style* (meta-style "as a language model…" → content-style "this would be harmful") while refusal itself is preserved.
- **Comparison & results / 对比与结果（author-reported）:** Content-safety vocabulary rises **2.55 → 10.37 hits/100 tokens** vs magnitude-matched random direction **1.13–2.16**; replicated in Gemma-2-2B-IT at layer 12 (**1.72 → 6.37** at α = 1.0 vs random 1.35). B1's causal effects consistently larger than B2's (asymmetry is part of the finding).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20405) · [PDF](https://arxiv.org/pdf/2611.20405)

---

## 3. NeurIPS 2026 — Main track, workshops & Datasets/Benchmarks
### NeurIPS 2026 — 主会、研讨会与数据集/基准

### 3.1 The Price of Choosing Examples: Context Overfitting in Adaptive In-Context Learning
**选择样例的代价：自适应 In-Context Learning 中的上下文过拟合**

- **Authors / 作者:** Xiaoyu Li, Jiangxuan Long (equal contribution)
- **Affiliation / 机构:** University of New South Wales (Xiaoyu Li); The University of Hong Kong (Jiangxuan Long) — PDF page 1
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment; 31 pages, 8 figures, 5 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** ICL is usually analyzed as if prompt examples were sampled *before* the learner is chosen; deployed systems retrieve, filter, re-rank, edit and repeatedly test examples *after* seeing the query and datastore.
  - **Methodology:** Formalizes prompt construction as **adaptive data analysis** via a conditional stochastic-kernel calculus. Main quantity = **context capacity** κ (mutual information / approximate max-information between datastore and final prompt transcript). Proves a finite-sample context-generalization bound of order **√(κ/k)** for any frozen ICL learner and adaptive pipeline, with a **matching lower bound** (exact constant when log k ≪ κ ≪ k). Derives two PAC-Bayesian retrieval rules: first-order Gibbs (charges data-dependent candidate gates their prior mass) and self-normalized second-order.
  - **Innovations:** separates context *quality* from context *certification* — longer/more relevant contexts improve risk only if the selection procedure is stable enough.
- **Comparison & results / 对比与结果（author-reported）:** On Banking77 with 64 retrieval recipes and two model families, certificates hold in **all 24,000 resampled selection events**; from 64 (Qwen2.5-7B) or 128 (GPT-4.1-mini) reused validation queries, the Gibbs rule certifies risk below zero-shot error in **>99%** of validation draws.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21251) · [PDF](https://arxiv.org/pdf/2611.21251)

### 3.2 Anytime-Valid PAC-Bayes Certificates for Adaptive Test-Time Scaling
**自适应 Test-Time Scaling 的随时有效 PAC-Bayes 证书**

- **Authors / 作者:** Xiaoyu Li, Jiangxuan Long (equal contribution)
- **Affiliation / 机构:** University of New South Wales; The University of Hong Kong — PDF page 1
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment; 31 pages, 7 figures, 15 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Test-time scaling recipes choose sample budget, prompt, verifier and aggregation *after* repeatedly inspecting a calibration set; standard validation error bars are invalid after such adaptive selection.
  - **Methodology:** Models a recipe as a randomized predictor with random cost and proves a **time-uniform PAC-Bayes certificate** valid simultaneously over all calibration times, posterior mixtures over recipes, and data-dependent stopping rules — covering the recipe *search*, not just the final reported recipe. Penalty for a finite grid is the familiar log M/n. Specializes to self-consistency and derives a **margin law**: plurality voting improves exponentially with budget only when the correct answer is the generator's unique mode; otherwise more compute can provably amplify errors. Yields an oracle water-filling law for compute allocation.
  - **Innovations:** distribution-free risk+compute reporting for adaptive inference; margin-based explanation of when self-consistency fails.
- **Comparison & results / 对比与结果（author-reported）:** With two models on GSM8K and MATH-500, selected-best error bars fall below out-of-split GSM8K risk in up to **22.5%** of random splits at nominal 5% while the certificate **never** does; on the full GSM8K test split the certificate tightens to **0.109** (held-out risk 0.039). A 192-example GSM8K audit uses gpt-4.1-mini generations.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21241) · [PDF](https://arxiv.org/pdf/2611.21241)

### 3.3 Differentiable Exact Learning
**可微精确学习**

- **Authors / 作者:** Hristo Papazov, Francesco D'Angelo, Nicolas Flammarion
- **Affiliation / 机构:** Department of Computer Science, **EPFL** — PDF page 1
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Learn a neural controller that interacts with an unbounded environment from **policy-trajectory observations (PTOs)** — traces exposing observations/actions but hiding internal states.
  - **Methodology:** Introduces **Differentiable Finite-State Transducers (DFSTs)** with multilinear updates, log-parallel training, able to emulate arbitrary finite-state controllers, giving computational universality through environmental interaction. Recipe: **State-Tracking Controller + Unbounded External Environment + PTOs = Extreme Length Generalization**. A metric-extraction protocol recovers interpretable discrete controllers provably equivalent to target algorithms.
  - **Innovations:** For Softmax DFSTs, simply taking `argmax` over transition probabilities yields discrete controllers that provably perform **universal Turing-machine simulation and binary arithmetic** — exact, not approximate, learning.
- **Comparison & results / 对比与结果（author-reported）:** From tiny training datasets (e.g. **25 PTOs / 891 parameters**, 250 PTOs / 8,227 params), compact DFSTs achieve extreme length generalization on arithmetic and universal-simulation tasks; success replicated on RNNs and GRUs. Code/ weights/ proof checkers released.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21486) · [PDF](https://arxiv.org/pdf/2611.21486)

### 3.4 Attention Sinks as Spectral Spikes: A Mechanism Analysis of Gated Attention
**注意力汇聚点作为谱尖峰：门控注意力的机制分析**

- **Authors / 作者:** Seojin Kim, Yehjin Shin, Noseong Park
- **Affiliation / 机构:** **KAIST** — PDF page 1 ({seojinkim, yehjin.shin, noseong}@kaist.ac.kr)
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment: "The 40th Conference on Neural Information Processing Systems")
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Attention sinks (few tokens absorb disproportionate attention) are reduced by post-SDPA output gating; sinks are also linked to gradient sinks/massive activations via backward dynamics — how one gate affects forward sink structure, backward gradient concentration and training-time signatures was unclear.
  - **Methodology:** Formulates sinks as **sink-induced low-rank modes in token-space covariance**, directions aligned to high-mass attention columns. Post-SDPA gating = mode-dependent contraction: attenuates sink-induced spectral energy forward and locally reduces value-path gradients through sink columns backward.
  - **Innovations:** unified forward/backward/training-time mechanism analysis of gated attention via random-matrix diagnostics.
- **Comparison & results / 对比与结果（author-reported）:** Gating reduces outlier mass, weakens sink-subspace alignment, increases effective rank; backward analysis shows active-gate attenuation of first-token value gradients; training-time diagnostics show gating suppresses co-emergence of attention concentration, value-gradient amplification and representation dominance. (No single headline number in the abstract.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20403) · [PDF](https://arxiv.org/pdf/2611.20403)

### 3.5 Halting in Recurrent Sequence Models
**循环序列模型中的停止机制**

- **Authors / 作者:** Simon Dräger
- **Affiliation / 机构:** **Salk Institute for Biological Studies** — PDF page 1
- **Venue / 会议:** **NeurIPS 2026 Workshop on Interpretability as a Science (InterpScience)** — arXiv comment (16 pages, 7 figures, 2 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** RNNs/SSMs are trained to emit EOS as just another token with no special loss term; how they decide to stop is poorly understood.
  - **Methodology:** Minimal task: emit an input sequence an instructed number of times, then EOS. Trains tanh RNNs and linear SSMs; intervenes on hidden states at sequence boundaries via affine transformations; rotates rotation planes in SSMs.
  - **Innovations:** Identifies two candidate primitives of EOS halting: a **shared linear-subspace encoding of remaining token count** in tanh RNNs, and **phase alignment across fixed 2-D rotation planes** in linear SSMs.
- **Comparison & results / 对比与结果（author-reported）:** Modulating the RNN hidden state at the boundary shifts it to the representation of "one fewer copy remaining"; the **unchanged** network emits EOS one copy early while reproducing the shortened target in **94.4%** of new sequences — causal evidence. In SSMs, independently rotating the planes removes most intended stopping while preserving copied content.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20377) · [PDF](https://arxiv.org/pdf/2611.20377)

### 3.6 Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle
**乐观验证器会被攻击：精确过程 Oracle 下的 Reward Hacking**

- **Authors / 作者:** Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R., Arun Prakash, S. Senthilkumar
- **Affiliation / 机构:** University College of Engineering, BIT Campus, Anna University (Tiruchirappalli); Central University of Karnataka; NIT Tiruchirappalli; Jawaharlal Nehru University — PDF page 1
- **Venue / 会议:** **NeurIPS 2026 Workshop on Meta-Agents** (short version "The Verifier Gap", non-archival); full arXiv 30 pages
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** RLVR inherits whatever its verifier gets wrong. Outside math/code the verifier is a proxy/rubric/judge and its distance from the true objective is never measured, so a rising reward cannot be distinguished from a hack.
  - **Methodology:** Executable authorization policies over **124,416 contexts** admit an oracle listing every minimal sufficient reason for every decision → true process-level reward exactly computable. Degrades the verifier along **seven axes** (outcome-only, sufficiency, recall-only, extraction noise, coarse taxonomy, stale policy, LLM judge), trains against each while the exact verifier scores every rollout.
  - **Innovations:** Four phenotypes (sufficiency→padding hack; outcome-only→saturation; noise→dilution; ranking-preserving gaps→harmless) plus a **model-free verifier audit** (selection error + gap sign + saturation pilot) that anticipates which phenotype a run will produce. Releases 14 real public policies (Cedar, OPA, Gatekeeper) ported to executable oracles.
- **Comparison & results / 对比与结果（author-reported）:** Sufficiency proxy ends at **0.940** while true faithfulness falls **0.731 → 0.667** on 96 held-out episodes. Across 9 configurations (2 frameworks, 2 vendors, 2 adapter sizes, 3 precisions, 2 initializations, 2 seeds), sufficiency damage is positive in all 10 replication cells and >2 SE in 7; optimistic gaps stay the steeper branch. Damage *magnitude* did not replicate (5 pre-registered explanations reported as they fell).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21538) · [PDF](https://arxiv.org/pdf/2611.21538)

### 3.7 MASTA: A Feedback-Scheduled Multi-Agent System for End-to-End Tamarin Modeling and Analysis
**MASTA：面向端到端 Tamarin 建模与分析的反馈调度多智能体系统**

- **Authors / 作者:** Yongkang Xiao, Qiyi Deng, Jing Chen, Min Shi, Ju Ma, Ruiying Du
- **Affiliation / 机构:** School of Cyber Science and Engineering, **Wuhan University** — PDF page 1
- **Venue / 会议:** **NeurIPS 2026 Main Track (poster)** — arXiv comment (19 pages)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Tamarin security-protocol verification requires expert-authored multiset-rewriting rules and temporal-logic lemmas; translating natural language into a complete formal model compounds syntactic, reachability and property-level errors, and a single self-evaluating agent cannot localize them.
  - **Methodology:** Three innovations: (1) **operational–evaluative role decomposition** — Architect (rule modeling), Auditor (property modeling), Arbiter (pure dispatch, no authoring duties); (2) Tamarin-anchored scheduler dispatching the next agent from the latest verifier verdict, routing problem-tagged fixes through a modification list with a **six-class problem taxonomy** + LLM dedup check against routing deadlock; (3) benchmark of **10 protocols × 139 mutation variants** with 5 fine-grained metrics (M1–M3 correctness, M4–M5 completeness).
  - **Innovations:** verifier-anchored multi-agent scheduling; separation of authoring from evaluation for formal methods.
- **Comparison & results / 对比与结果（author-reported）:** MASTA on Qwen 3.5-plus improves over OpenCode on the same backbone by up to **+0.27** on individual metrics and ranks first on both correctness and completeness averages, **surpassing Codex (GPT-5.5) and Claude Code (Opus 4.7) despite a weaker LLM**. Ablations on 5 protocols: removing the Arbiter collapses property/verification scores to **zero**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20671) · [PDF](https://arxiv.org/pdf/2611.20671)

### 3.8 Instrumenting Failure: Scoring Language Model Agents at Every Decision Node in Imperfect-Information Games
**失败的可观测化：在不完美信息博弈中于每个决策节点为语言模型智能体打分**

- **Authors / 作者:** Michael Kingston, Sonit Singh, Alan Blair
- **Affiliation / 机构:** School of Computer Science and Engineering, **UNSW Sydney** — PDF page 1
- **Venue / 会议:** **NeurIPS 2026 Workshop on Interpreting Agent Behavior (IAB)** — arXiv comment (26 pages, 6 figures)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Agent evaluations report task success but rarely say what the agent did at each decision node.
  - **Methodology:** Scores every decision node of three **12B–14B instruct-tuned LMs** playing **5 zero-sum imperfect-information games** against 4 opponents on 8 decision/game-theoretic properties, **5 of them against a CFR+ equilibrium reference**; in a separate call the LM states a belief about the opponent's hidden state.
  - **Innovations:** node-level instrument plus a **gate** that withholds, with a stated reason, any belief score the run cannot support — distinguishes agent failure from instrument/representation failure.
- **Comparison & results / 对比与结果（author-reported）:** Without memory at T=0, stated beliefs sit **0.250–0.288** TV distance from the equilibrium posterior; action–belief agreement exceeds chance by −0.04 to 0.19; LM action never varies with state in **10 of 38** cells where CFR+ varies. Memory lowers constant-action share in 9 of 13 testable ladders at T=0; at T=0.2 cells at 1 drop from **16 → 5** of 46 informative cells. 7 of 8 non-zero defect rates attributable to instrument/representation/LMs (behavioural inconsistency only — no claim about internal beliefs).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20644) · [PDF](https://arxiv.org/pdf/2611.20644)

### 3.9 AdMem: Expectation-Grounded Procedural Memory for Long-Horizon Task-Solving Agents
**AdMem：面向长程任务求解智能体的期望锚定过程记忆**

- **Authors / 作者:** Runzhe Wang, Huilin Lu, Shengjie Liu, Li Dong, Zhihuai Zhu
- **Affiliation / 机构:** **Princeton University** (Runzhe Wang); **Amazon** (Huilin Lu, Shengjie Liu, Li Dong; Zhihuai Zhu affiliation truncated in extracted page 1 — PDF-verified Amazon for the named three) — PDF page 1
- **Venue / 会议:** **NeurIPS 2026**, Workshop "Agents in the Wild: Safety, Security, and Beyond" — arXiv comment
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Naively accumulating cross-task memory can make an agent **worse** than no memory: on AgentBoard a workflow-induction memory solves fewer tasks than memoryless ReAct in **7 of 8 domains**; a per-step procedural store loses half of ReAct's completions on Jericho.
  - **Methodology:** Before each action the actor commits to an **expected outcome**; a concurrent critic scores the realized outcome against it and writes a procedural entry with a binary reward + reflection (credit lands on the action, no environment reward needed). Each entry carries scalar **utility** updated online under a noisy-OR reward model, used for retrieval ranking jointly with similarity and for **eviction/merging** (forgetting + consolidation instead of unbounded growth).
  - **Innovations:** per-action credit assignment + explicit memory life cycle; all memory stays human-readable text (diagnosable/auditable, also attackable).
- **Comparison & results / 对比与结果（author-reported）:** Across **707 tasks in 8 AgentBoard domains**, AdMem solves **441** vs **388** for ReAct and **312** for the workflow-induction baseline (pooled gain significant under two-sided Fisher exact test), concentrated in domains with transferable cross-task structure.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20605) · [PDF](https://arxiv.org/pdf/2611.20605)

### 3.10 DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact Minimum-Action Bounds
**DetourBench：带精确最小动作下界的交互式智能体轨迹级评估**

- **Authors / 作者:** Hanlin Tian, Sihan Zhu, Zhao Yang, Yuxiang Wang, Zhiquan Hu, Yu Mi, Hongquan Zhu, Qiufei Hu
- **Affiliation / 机构:** **Datagrids.ai**; Northwest Polytechnical University; Nanyang Technological University; East China Normal University; Tongji University; Peking University — PDF page 1
- **Venue / 会议:** **NeurIPS 2026 Workshop: Evaluation of Interactive Agents** — arXiv comment
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Endpoint scoring cannot separate an agent that retrieved exactly the needed evidence from one that read most of the environment, nor a near-miss from a wanderer; authored solutions only prove solvability, not minimality.
  - **Methodology:** Constrains each task to a finite partially observable transition system with unit-cost accesses whose resources become globally addressable after discovery. Exhaustive search yields **exact full-information minimum action count L₀** with a replayable witness, and exact **residual work R_T** from graph-recoverable terminal states; irreversible wrong commitments are recorded as *no finite residual distance* rather than assigned one.
  - **Innovations:** reports success, attainment, residual progress and **normalized detour** separately; open-sources instances, oracle witnesses and harness.
- **Comparison & results / 对比与结果（author-reported）:** Across **375 scored episodes** (5 model endpoints × 25 integrated tasks × 3 repeats), success ranges **58.7%–96.0%** while conditional attainment ranges **0.803–0.890** and **orders the models differently**; residual work separates near-complete from costly-incomplete and irreversible-commitment trajectories.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20844) · [PDF](https://arxiv.org/pdf/2611.20844)

### 3.11 The Hidden Cost of MoE Diffusion Decoding: Profiling and Fixing the Sampler
**MoE 扩散解码的隐性代价：剖析并修复采样器**

- **Authors / 作者:** Harshit Samrat, Ramakrishna Paramahamsa Kompella
- **Affiliation / 机构:** Indian Institute of Technology Madras — PDF page 1 (the "NVIDIA GB10" in the abstract is the *evaluation accelerator*, not an affiliation)
- **Venue / 会议:** **NeurIPS 2026 Workshop DiffuLM** — arXiv comment
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Masked diffusion LMs decode by denoising a full canvas; each forward pass runs sampling/stopping over the entire canvas×vocabulary logits tensor. After weight quantization this logits pipeline — **not** expert GEMMs — becomes the largest decode-time consumer. Diffusion processes **S×** more logit entries per output token than autoregressive decoding (S = denoising steps).
  - **Methodology:** Two lossless tiers: a **bit-exact** tier (byte-identical output to reference decoder) and an **accuracy-parity** tier (fused single-pass entropy kernel + Gumbel-max sampling), combined with a W4A16 expert kernel.
  - **Innovations:** first profiling result that the sampler — not the MoE experts — dominates quantized diffusion decoding; releases code and quantized weights.
- **Comparison & results / 对比与结果（author-reported）:** On a 26B diffusion MoE on NVIDIA GB10 (273 GB/s), full stack reaches **2.4–2.7×** end-to-end speedup over bf16 at unchanged GSM8K/HumanEval/MATH accuracy. Confirmed on LLaDA2.0-mini (pipeline **28.8%** of decode; fused W4A16 **3.3×** at accuracy parity); effect disappears on a dense diffusion model (**3.6%**).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21852) · [PDF](https://arxiv.org/pdf/2611.21852)

### 3.12 Solver to System: LLM Reasoning Across Representations and Execution in Scientific Simulation
**从求解器到系统：LLM 在科学仿真中的跨表征推理与执行**

- **Authors / 作者:** Eliza Berman, Rohan Subramanian, Shreya Jha, Lohit Jagarapu, Romain Lopez, Rajesh Ranganath
- **Affiliation / 机构:** **New York University** — PDF page 1
- **Venue / 会议:** **NeurIPS 2026 Workshop: Sim2Science — ML with Imperfect Scientific Models** — arXiv comment (23 pages, 14 figures, 9 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** PDE simulators are widely used, but LLM generation/interpretation of solver code is hard: one system has code/equations/natural language/numerical trajectories as representations, and **code can execute successfully while implementing invalid physics** — a direct code-execution-prediction testbed.
  - **Methodology:** Introduces **Solver2System**, a dataset of PDE solvers with multiple representations, controlled corruptions and lexical perturbations; evaluates cross-representation consistency plus static and **agentic** detection of physical invalidity across 8 open-weight models.
  - **Innovations:** separates "code runs" from "physics is right"; tests whether lexical perturbations to code change interpretation of *unchanged* representations.
- **Comparison & results / 对比与结果（author-reported）:** LLMs systematically favor some representations when evidence conflicts; lexical perturbations to code alter interpretation of other unchanged representations; execution improves physical-validity judgments, but weaker agents can judge correctly **without identifying the causal defect**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21964) · [PDF](https://arxiv.org/pdf/2611.21964)

### 3.13 MOSAIC: Every Measurement, Every Direction, All at Once — Multimodal Flow Matching for Molecules and Spectra
**MOSAIC：每次测量、每个方向，一次完成 —— 面向分子与光谱的多模态 Flow Matching**

- **Authors / 作者:** Thorben Prein, Elton Pan, Rafael Gómez-Bombarelli, Santiago Miret
- **Affiliation / 机构:** **Lila Sciences** (all four, PDF page 1 emails @lila.ai)
- **Venue / 会议:** **NeurIPS 2026** — arXiv comment (30 pages, 12 figures)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Scientific generative modeling is data-limited; each experiment yields several coupled measurements of one entity, but standard models train on a single direction, discarding supervision.
  - **Methodology:** **MOSAIC**, a multimodal flow-matching transformer over molecular 3D structure and UV/IR/Raman spectra. Random masking lets measurements serve as conditioning inputs *or* prediction targets, giving multiple denoising tasks per experiment; a **single model** does **any-to-any** generation (any subset of modalities from any disjoint subset).
  - **Innovations:** any-to-any objective for science; supports arbitrary subsets of available measurements and molecular identification by matching generated spectra to experimental references.
- **Comparison & results / 对比与结果（author-reported）:** On **QM9S**, MOSAIC achieves **88.8% molecular graph recovery**, outperforming the strongest spectra-to-structure baseline by **23.2%** in structure generation while also beating a structure-to-spectra specialist in spectral generation. Ablations show any-to-any improves structure generation over structure-only across model sizes.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22098) · [PDF](https://arxiv.org/pdf/2611.22098)

---

## 4. EMNLP / AAAI / ICLR / KDD — adjacent & forward-dated tags (flagged)
### EMNLP / AAAI / ICLR / KDD —— 相邻与前置日期标签（已标注）

### 4.1 Trait Collapse in Text-to-Image Generation: Evaluating and Mitigating Personality Inconsistency in Visual Storytelling
**文生图中的特质坍缩：视觉叙事中人格不一致的评估与缓解**

- **Authors / 作者:** Yuanbo Tong, Haoyuan Li, Jibiao Jiang, Zirui Wang, Yuchen Li, Jiamou Liu
- **Affiliation / 机构:** School of Computer Science, **The University of Auckland** (New Zealand) — PDF page 1
- **Venue / 会议:** **EMNLP 2026 Main Conference Paper** (forward of the requested EMNLP 2025; arXiv comment, 26 pages, 5 figures)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** T2I models preserve visual appearance but fail to maintain personality-relevant *behavior* — "**trait collapse**". CLIP Score / DINO similarity are blind to it; abstract trait labels and scene emotion labels give no consistent gain over neutral prompts.
  - **Methodology:** **ViStoryBench-Personality**, a story-level benchmark with an expert-validated **Visual Cues Lexicon (Fleiss' κ = 0.757)** and a six-dimensional metric suite (personality alignment, cross-scene stability, behavioral coherence). **TBV (Trait-Behavior-Visual)**, a training-free prompting framework decomposing traits into renderable visual constraints.
  - **Innovations:** first operationalization of personality (not just identity) consistency in visual storytelling; shows visual identity consistency does **not** imply personality consistency.
- **Comparison & results / 对比与结果（author-reported）:** Across **7 T2I systems**, a persistent semantic gap between abstract trait labels and visual evidence; TBV improves **Personality Alignment Score by up to +22.1%**, with larger gains for models with stronger language-conditioning capacity.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20381) · [PDF](https://arxiv.org/pdf/2611.20381)

### 4.2 Deploying a Control-Logic LLM Assistant in Air-Gapped Power Plants: Lessons in Source Authority and Bounded Retrieval
**在气隙电厂部署控制逻辑 LLM 助手：来源权威与受限检索的经验**

- **Authors / 作者:** Yiwei Fu, Nicholas Gabriel
- **Affiliation / 机构:** **GE Vernova Advanced Research Center**, Niskayuna, NY — PDF page 1
- **Venue / 会议:** Extended version of a paper accepted at **IAAI-27 (AAAI 2027)** — arXiv comment (8 pages, 2 figures, 3 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Industrial OT settings forbid data leaving the plant, have limited on-prem compute, and wrong causal attribution can mislead incident response.
  - **Methodology:** Reports lessons from two prototypes at **two gas power plants**. V1: VLM reconstructs control topology from 6,979-page PDF printouts — poor precision and slow; controls engineers revealed a native structured export. V2: LLM tool-calling agent plans repeatedly over 8 predefined graph operations — replaced by explicit execution plans. Deployed design ingests the authoritative export into a versioned **knowledge graph**, executes bounded graph operations in fixed software, and confines the LLM to fallback intent classification + evidence-grounded explanation.
  - **Innovations:** practical division of labor for high-consequence AI: LLMs interpret/explain, deterministic software constructs/retrieves evidence; abstention, entity disambiguation, graph versioning, read-only integration.
- **Comparison & results / 对比与结果（author-reported）:** VLM extraction over 6,979 pages gave **0.51 connection precision** and **3.1 hours on 4×H200**. Replacing the tool-calling agent with explicit plans cut mean token use **20×** and median latency **3×** with identical retrieved node sets on 40 template-generated questions. Deployed graph: **221K nodes across 7 controllers** at one site.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20398) · [PDF](https://arxiv.org/pdf/2611.20398)

### 4.3 Same Papers, Different Verdicts: Tracing Version Drift in LLM Peer Review
**同一论文，不同判决：追踪 LLM 同行评审中的版本漂移**

- **Authors / 作者:** Jizhou Guo
- **Affiliation / 机构:** Not stated on PDF page 1 (independent author; no institutional footnote) — **verify in later versions**
- **Venue / 会议:** Preprint; tests pre-registered before **ICLR 2027** decisions, results to be added after 16 December 2026 (forward-dated tag) — arXiv comment (19 pages, 5 figures)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Venues/benchmarks read LLM review scores as measurements of a paper, but providers replace models within months — a version-drift validity problem for evaluation.
  - **Methodology:** Audits **20 frontier models from OpenAI, Google and Anthropic** on ICLR 2027 submissions *while under review*, with tests registered before decisions. Swaps score-stripped critiques across versions; uses a third-party scorer and a rewrite removing evaluative wording; runs retrospective memory tests on decided papers.
  - **Innovations:** quantifies how model-version drift changes accept/share and critique severity, separating score percentile from accept threshold and detecting memorization of decided papers.
- **Comparison & results / 对比与结果（author-reported）:** Between earlier/later Claude Opus and Gemini versions, accept-side share falls **52 and 53 percentage points** (183 and 60 random submissions) and **43–79 points** in 6 further paired comparisons, **no paper moving up in any**. Prompting a 30% acceptance rate still leaves a **79-point** gap between two Opus versions. Swapped later critiques alone lower accept share by **35 (Opus) / 51 (Gemini)** points. On 57 papers, Opus 4.6/5.5 percentiles correlate **0.73** while accept shares differ **44 points**. All 20 models give 2 or 3 in **473/475** reviews vs 60/72 human reviews. Opus 5.5 names the true first author of **27** decided ICLR 2026 papers from titles alone with no wrong name.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20608) · [PDF](https://arxiv.org/pdf/2611.20608)

### 4.4 SpeCal: Spectral Calibration for Unsupervised RLVR
**SpeCal：面向无监督 RLVR 的谱校准**

- **Authors / 作者:** Kai Tang, Xing Zheng, Haobo Wang, Guangcheng Zhu, Shenzhi Yang, Zhengqing Zang, Yingfan Ma, Cheng Peng, Bowen Song, Weiqiang Wang
- **Affiliation / 机构:** **Zhejiang University** and **Ant Group** (Hangzhou) — PDF page 1 (multiple authors dual-affiliated)
- **Venue / 会议:** **KDD 2027** (forward-dated tag, arXiv comment) — **not** KDD 2026
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** RLVR improves LLM reasoning but needs ground-truth answers/verifiers; unsupervised RLVR derives rewards from the model's own rollouts, but self-supervision reliability varies across rollout groups and responses, and existing methods refine rewards only from decoded outcomes/statistics.
  - **Methodology:** **SpeCal** uses **hidden-state spectra** as a complementary reliability signal. Group level: combines spectral mass with a Gaussian band-pass gate over normalized entropy-based **effective rank**, favoring groups with real representation variation in a preferred effective-dimensionality regime. Rollout level: group effective rank sets how many dominant directions are retained in a leave-one-out spectral subspace of the remaining rollouts, measuring each held-out rollout's conditional support.
  - **Innovations:** calibrates reward-induced advantages at group and rollout levels **without redefining the unlabeled reward**; spectrum-based (not endpoint-based) supervision quality estimate.
- **Comparison & results / 对比与结果（author-reported）:** No numeric results in the available abstract; contribution is the bi-level calibration framework. (Full tables in paper.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20691) · [PDF](https://arxiv.org/pdf/2611.20691)

---

## 5. Recommendation, Advertising, CTR, Retrieval & E-commerce (general recent arXiv)
### 推荐、广告、CTR、检索与电商（近期 arXiv 通稿）

### 5.1 PEETS: Preference-aware Embeddings with Explicit Tree Structure for Auxiliary Product Bundling
**PEETS：具有显式树结构的偏好感知嵌入，用于辅助产品捆绑推荐**

- **Authors / 作者:** Maolei Huang, Jing Tian, Dexuan Duan, Yan Chen, Huawei Cao, Shuhan Song
- **Affiliation / 机构:** **Fliggy, Alibaba Group** (Beijing) — first author; **University of Chinese Academy of Sciences** (Beijing) — co-authors — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI), submitted 2026-11-16; no venue tag
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Auxiliary products (flight protection, flexible-change services) are recommended alongside primary travel purchases. **Granularity ambiguity**: SKUs in one product type share semantics but differ in price/coverage, and rejecting one offer does not imply disinterest in the whole type.
  - **Methodology:** Training-time framework regularizing an existing **click–conversion predictor** through two conditional comparisons: **Hierarchical Contrastive Loss** (uses the pair's common ancestor as reference) and **Negative Contrastive Loss** (conditions structural sampling/comparison shifts on logged rejection events). Both act on shared SKU representations during training.
  - **Innovations:** separates catalog relatedness from individual preference supervision; **leaves the predictive serving path intact** — no auxiliary-loss computation at serving.
- **Comparison & results / 对比与结果（author-reported）:** **78.20% AUC**, +0.90 pp over TWIN V2 and +1.15 pp over matched base. 14-day online evaluation: gross auxiliary GMV per exposed user-day **+8.20% vs Policies, +3.06% vs Base, +0.84% vs TWIN V2** (all user-bootstrap 95% intervals >0); bundling rate 0.51 pp below Policies; cancellation interval's upper limit exceeds the prespecified margin (flag). **p95 latency 42.1 ms vs 42.0 ms base**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20726) · [PDF](https://arxiv.org/pdf/2611.20726)

### 5.2 Can LLMs Give Good Product Advice? A Framework for Diagnosing Failures
**LLM 能给出好的产品建议吗？一个失败诊断框架**

- **Authors / 作者:** Assaf Hallak, Yftah Ziser, Gal Chechik
- **Affiliation / 机构:** **NVIDIA Research** (all); University of Groningen; Bar-Ilan University — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.CL), submitted 2026-11-16; no venue tag
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Evaluating product advice cannot rely on string-matching a product in a reply — several products may be suitable, and the recorded answer may itself be poor advice.
  - **Methodology:** Diagnostic framework separating the user's **stated needs**, the model's **added assumptions**, **candidate generation**, **filtering**, and **final choice**, with **19 possible failure modes** and the evidence needed to assess each. Applied to product-advice data and a separate product-selection task with externally assigned relevance labels.
  - **Innovations:** distinguishes *naming* a community-listed product from *selecting* it; analyzes how answer extraction and candidate-list construction change measured outcomes.
- **Comparison & results / 对比与结果（author-reported）:** When shown a community-listed alternative alongside their own sampled car recommendation, **six models prefer the alternative in 1.9%–6.5%** of eligible disagreements, consistently across both source-blind presentation orders.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20734) · [PDF](https://arxiv.org/pdf/2611.20734)

### 5.3 Auditing World-Model Explanations in Retail Forecasting: Faithfulness, Accuracy and Price Response
**零售预测中世界模型解释的审计：忠实性、准确性与价格响应**

- **Authors / 作者:** Karthik Iyer
- **Affiliation / 机构:** No institution on PDF page 1 (independent; correspondence `karthik.iyer.au@gmail.com`, ORCID given) — **independent author**
- **Venue / 会议:** arXiv preprint (cs.LG, cs.AI), submitted 2026-11-16; no venue tag
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Forecasting models that read price/promotion plans explain each forecast as a **baseline** (nothing planned) + **lift** (plan's effect); merchants order stock on the lift. An explanation can pass trust checks yet still be wrong enough to cost money.
  - **Methodology:** Defines **eight checks** for any forecaster stating a plan lift (six with pass rules fixed *before* any result), run on a world model and LightGBM. Uses generated store data with **known effects**, plus a noisy real benchmark from Dominick's (38 price episodes where a store's regular prices diverged from zone peers).
  - **Innovations:** distinguishes explanation *faithfulness* (does it reflect the model?) from *correctness about the world* (is it right?) — shows the first does not imply the second; pre-registered pass rules.
- **Comparison & results / 对比与结果（author-reported）:** World model passes construction/stability/price-direction/agreement checks yet states **1.33–1.40× the true lift** in high-demand weeks (**1.23–1.42×** in 8 variants); LightGBM also overstates (1.26; 1.16–1.35). Stock ordered to the world model's lift is off by **0.44–0.48** of true lift. Stated response to a lasting regular-price change is **4.7–6.5× the true −0.5**. Across **703 configurations**, checks passed were unrelated to forecast accuracy (Spearman **0.02**, 95% CI −0.02–0.05). Dominick's pooled 8-week response −0.33 (95% CI −0.68–0.01).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20811) · [PDF](https://arxiv.org/pdf/2611.20811)

### 5.4 When the Bill Falls: Reusing the Old Index Defers, Never Avoids, Re-encoding in Complete Embedding-Model Migration
**账单到期时：复用旧索引只是推迟、而非避免完整嵌入模型迁移中的重新编码**

- **Authors / 作者:** Nannan Zhao, Jiameng Zhang, Taoyu Zhong, Hao Wang, Bo Wang
- **Affiliation / 机构:** **Northwestern Polytechnical University**, Xi'an, China — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.IR, cs.CL), submitted 2026-11-16; tagged "[Experiment, Analysis, and Benchmark]"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Upgrading an embedding model behind a vector index requires re-encoding the corpus; recent work claims to reuse the old index via adapters or window re-ranking.
  - **Methodology:** Tests **16 model pairs** on passage and code corpora + **11 on Natural Questions**. Proves a bound that prices window re-ranking cost from the old index alone; pre-registered replays on all **8,841,823 passages**; 36 further pre-registered Zipf-skewed replays.
  - **Innovations:** three pre-migration rules (whether reuse is worthwhile; which strategy; how deep a window). Key correction: **adapters must be compared with the old model, not just the new one**.
- **Comparison & results / 对比与结果（author-reported）:** Reuse **never avoids re-encoding** — every strategy eventually encodes every document. Of five adapter families, only same-family LLM bridges beat the old model, by a negligible margin. Window-cost prediction confirmed on all 3 tested pairs; planned strategy held on **32/36** Zipf replays; depth rule priced every window reaching target quality to within **4 parts in 10⁵**. On NQ a pre-committed plan selected the family on **10/11** pairs and priced every window exactly.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20702) · [PDF](https://arxiv.org/pdf/2611.20702)

### 5.5 EchoSpec: Training Search Agents to Weigh Evidence Above Echoes
**EchoSpec：训练搜索智能体重视证据而非回声**

- **Authors / 作者:** Shihao Yang, Can Zeng, Xinzhe Li
- **Affiliation / 机构:** **Tsinghua University** — PDF page 1 (`@mails.tsinghua.edu.cn`)
- **Venue / 会议:** arXiv preprint (cs.IR), submitted 2026-11-15; 24 pages, 5 figures, 15 tables; code: github.com/unihsy/EchoSpec
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** RL-trained search agents decide what to retrieve, when to search again, when to answer. In real corpora a claim is copied/paraphrased across many pages while the primary source appears once; agents grant **echoes** the credence of independent sources and lose abstention.
  - **Methodology:** **EchoSpec** specifies reliability across **5 corpus transformations** with known target answers. Two-stage training: (1) **verification warm-start** teaching multi-hop bridge-entity recovery past echoes; (2) group RL optimizing an **evidence-gated λ-reward** with an outcome-independent acquisition bonus and scale-preserving advantages retaining the optimal rule λ/(1+λ).
  - **Innovations:** isolates the failure to **evidence acquisition** — once primary evidence is in context, agents overrule eight echoes as reliably as one; bigger budgets/forced search/passive filtering alone do not recover displaced evidence.
- **Comparison & results / 对比与结果（author-reported）:** Across 5 base models (3B–32B) and 7 released RL agents, **eight paraphrased false-claim echoes overturn 58–73%** of previously correct answers; exact-match RL drives deleted-evidence abstention below 15%. EchoSpec cuts eight-echo deference by **30–44 points** (Qwen2.5-7B) down to **29–31%**, nearly quadruples eight-echo reach to **26–27%** with zero-shot transfer to unseen BGE/BM25 retrievers, and raises standalone QA precision to **47–55%**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20034) · [PDF](https://arxiv.org/pdf/2611.20034)

---

## 6. LLM Systems, Efficiency & Generative / Sequential Modeling
### LLM 系统、效率与生成式/序列建模

### 6.1 Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents
**Nemotron 3.5 Bolt E4B 4GB：面向快速对话智能体的开放高效小语言模型**

- **Authors / 作者:** NVIDIA (author list begins with "NVIDIA:"; 100+ contributors incl. Adi Margolin, Bryan Catanzaro, Oleksii Kuchaiev, etc.)
- **Affiliation / 机构:** **NVIDIA** — PDF page 1 attribution; project page `research.nvidia.com/labs/nemotron/...`
- **Venue / 会议:** arXiv technical report (cs.CL, cs.AI, cs.LG), submitted 2026-11-16 (PDF dated 2026-10-23)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Voice/device assistants, interactive characters and robotic/IoT interfaces need conversational quality, multi-turn tool use and grounding within a tiny memory footprint on RTX/Jetson/RTX-DGX-Spark.
  - **Methodology:** Further post-training from **Gemma-4-E4B-it**, optimized for **intelligence per GB**; released with a **DFlash drafter** (speculative decoding).
  - **Innovations:** combines natural conversation with multi-turn agentic capabilities in a ~4GB-effective model; open release with drafter and blog figures.
- **Comparison & results / 对比与结果（author-reported）:** On **21 benchmarks**, highest average accuracy while generating the **fewest output tokens** in both reasoning and non-reasoning modes vs Gemma-4-E4B-it and Qwen3.5-4B. With DFlash: **2.74×** per-user decode speed vs no speculative decoding at concurrency ~1, and **1.21×** generation throughput of Gemma-4-E4B-it with MTP at batch size 1.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20771) · [PDF](https://arxiv.org/pdf/2611.20771)

### 6.2 TeleChat to Xing 4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks
**从 TeleChat 到星晨 4：在国产芯片与框架上推进前沿智能体模型**

- **Authors / 作者:** Xingchen AGI Lab (technical report; ~120 contributors incl. Baotian Hu, Bingkai Yang, Zhongjiang He, etc.)
- **Affiliation / 机构:** **Xingchen AGI Lab, China Telecom** — PDF page 1
- **Venue / 会议:** arXiv technical report (cs.AI), submitted 2026-11-17
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Most open models are trained on GPUs; scaling on domestic chips/frameworks (Ascend + MindSpore) poses systems challenges.
  - **Methodology:** Coordinated architecture + infrastructure design: MLA + DSA + cross-layer **IndexShare** for long context, optimized **MHC** operators, wider-and-shallower **MoE**, block-wise draft model + lightweight correction heads for speculative decoding. Pretraining on **MindSpore HyperParallel** (topology-aware hybrid sharding, distributed optimizer, long-sequence/activation-memory management, CPU affinity/core isolation). **TeleGym** unified agent execution platform: disaggregated asynchronous execution, bounded oversampling, partial rollout for heterogeneous task durations.
  - **Innovations:** open-sourced **29B MoE** trained entirely on Ascend NPUs with MindSpore, 4B active params/token, native **256K** context; documents 285B pretraining on 8,192 Ascend 910C cards.
- **Comparison & results / 对比与结果（author-reported）:** Paper is a systems/engineering report; headline numbers are the 285B/8,192-card scale, 29B/4B-active/256K open model and the TeleGym rollout design (no benchmark accuracy table in the abstract).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22115) · [PDF](https://arxiv.org/pdf/2611.22115)

### 6.3 Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual LLM Inference on NVIDIA Blackwell
**超越位宽：面向 NVIDIA Blackwell 多语言 LLM 推理的部署约束混合精度量化**

- **Authors / 作者:** Hyojung Han
- **Affiliation / 机构:** **ThakiCloud** — PDF page 1 (`hyojung.han@thakicloud.com`). "NVIDIA Blackwell/B200" is the **evaluation platform**, not the author's affiliation.
- **Venue / 会议:** arXiv preprint (cs.IR, cs.CL, cs.LG), submitted 2026-11-16; 18 pages, 2 figures
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Low-bit quantization is useful only if service-relevant accuracy is preserved, supported GPU kernels execute, and measured memory/latency limits are met — bitwidth alone is a bad proxy.
  - **Methodology:** Studies **Qwen3-8B on NVIDIA B200 with vLLM**: INT2/INT3, GPTQ, NVFP4 and mixed-precision configs; verifies native packed execution/precision on all **144 fused linear modules**; evaluates Korean/English/numerical/reasoning quality under **preregistered gates**.
  - **Innovations:** pre-registered, deployment-level evaluation with a held-out **FINAL-81** set; shows isolated module-restoration effects are strongly **non-additive** and sensitivity rankings disagree across Korean vs reasoning.
- **Comparison & results / 对比与结果（author-reported）:** Packed INT2/INT3 execute but **all seven INT2 grids degenerate** on generation. A config with 16-bit activations + **98 NVFP4 weight-only modules, 46 INT8 modules, INT8 output head** passes all gates: **5.917 GiB** weights (limit 5.98), Korean teacher-correct retention **0.904** (gate 0.90), TPOT ratio **0.939** vs BF16; paired accuracy **+1.4 pp** over NVFP4 W4A4 (Bonferroni CI +0.2–+2.6) vs +3.4 pp on the selection set. Final checkpoints not retained; bitwise rebuild unverified (flags).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21974) · [PDF](https://arxiv.org/pdf/2611.21974)

### 6.4 RISA: Recoverable Sparse Attention for Block-Diffusion Language Models
**RISA：面向块扩散语言模型的可恢复稀疏注意力**

- **Authors / 作者:** Xinrui Zhong, Fanjiang Ye, Yuke Wang
- **Affiliation / 机构:** **Rice University** — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.CL, cs.LG), submitted 2026-11-17
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Block-wise diffusion LMs refine tokens in parallel, but long-context inference is bottlenecked by memory-bound attention: every denoising step re-reads a growing KV cache. Naive sparse attention inflates the block's collective read set, adds repeated support-construction overhead, and permanent eviction can discard needed information.
  - **Methodology:** **RISA** exploits that historical KV is fixed within a block while queries evolve across steps. Newly generated history is organized into **exact priority and recovery tiers**; seed queries build a protected, bounded **read plan** whose indices are reused across the block while attention is recomputed with fresh queries + current-block KV. Separates history preservation from repeated reading.
  - **Innovations:** recoverable (not permanent) eviction + shared read plan; backbone/decoder unchanged.
- **Comparison & results / 对比与结果（author-reported）:** On **DreamReasoner-8B**, comparable task performance; at **32K**, **2.67×** attention speedup and **1.36×** fixed-trajectory request speedup over dense; on H200 at **128K**, **5.53×** attention speedup. Across 8 settings on 3 models, faster than tested MAGE, QUEST and LoSA budgets at matched KL.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22191) · [PDF](https://arxiv.org/pdf/2611.22191)

### 6.5 Communicate the Change: Efficient Expert Parallelism via Activation Compression
**通信变化：通过激活压缩实现高效专家并行**

- **Authors / 作者:** Fengyuan Liu, Jay Gala, Siva Reddy, Dzmitry Bahdanau
- **Affiliation / 机构:** **Mila – Quebec AI Institute**; **McGill University**; **Periodic Labs**; Canada CIFAR AI Chair — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.LG, cs.AI, cs.DC), submitted 2026-11-17
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** MoE inference requires two synchronous collectives per layer (dispatch + combine); as compute throughput outpaces interconnect bandwidth these are a scaling bottleneck.
  - **Methodology:** **EchoMoE** uses a hidden state from an earlier layer as a **reference** and communicates only the **compressed difference** to the current state, periodically refreshing references — motivated by incremental residual-stream updates. Retrofits existing MoE models with ~**8,500× fewer training tokens** than full pretraining.
  - **Innovations:** delta-communication for expert parallelism; tolerates quantization of communicated representations; released implementation + vLLM integration.
- **Comparison & results / 对比与结果（author-reported）:** **−58%** inter-node communication volume, **+22.6%** throughput, average performance within **3.8 pp** across **18 benchmarks**; up to **2.38×** inference throughput on bandwidth-constrained Ethernet; no measurable quality loss from quantizing communicated representations.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22215) · [PDF](https://arxiv.org/pdf/2611.22215)

---

## 7. Agents, Code Execution Prediction & Benchmarks
### 智能体、代码执行预测与基准

### 7.1 Accelerate Bench: Evaluating Agents for Application-Level Program Optimization
**Accelerate Bench：评估面向应用级程序优化的智能体**

- **Authors / 作者:** Bowen Liu, Yuhan Li, Nuo Chen, Weile Luo, Miao Peng, Qintong Zhang, Qifan Zhang, Jia Li, Ziqi Gao, Lydell Huang
- **Affiliation / 机构:** **Tencent Hy Team** (most authors; Bowen Liu internship there); HKUST; HKUST (Guangzhou); Tsinghua University; Peking University — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI), submitted 2026-11-16; 49 pages, 8 figures; project page `acceleratebench.com`
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Application optimization requires coding agents to find useful changes and **coordinate them across a whole program** while preserving required computation — beyond single-function benchmarks.
  - **Methodology:** **32 CPU optimization tasks** adapted from scientific applications and supercomputing competitions; each provides a working program with workload, correctness requirements, timing boundaries and permitted edits. Public testing for iteration; separate verifier scores final submission. Evaluates **16 coding agents** (model × harness) on v1.1.
  - **Innovations:** pairs executable workloads with agent programs **and trajectories**; controlled replays isolate build/runtime settings from source-code changes.
- **Comparison & results / 对比与结果（author-reported）:** Score@1 ranges **25.5%–67.4%**; most programs correct, but the two leading agents are **≥2× faster on ≥22/32** tasks while the other 14 reach 2× on only 8–17 and leave **125 of 412** correct outcomes below 1.25×. Identical source runs **0.29×–2.12×** depending only on build/runtime settings; one code change is worth **1.01× or 6.4×** depending on another.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20882) · [PDF](https://arxiv.org/pdf/2611.20882)

### 7.2 Readie: Low-Latency Code Sandboxes for AI Agents
**Readie：面向 AI 智能体的低延迟代码沙箱**

- **Authors / 作者:** Arjun Sivaraman, Zhaoheng Li, Alan Shi, Sanjay Malisetty, Eugene Wu, Yongjoo Park
- **Affiliation / 机构:** **University of Illinois Urbana-Champaign**; **ByteDance** (Zhaoheng Li); **Columbia University** (Eugene Wu) — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI, cs.DB, cs.SE), submitted 2026-11-17
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Agents offload execution to code sandboxes (Modal/E2B/Daytona); startup is slow because one compact, pre-warmed snapshot cannot cover the diverse artifacts (packages, datasets) of agent-generated code.
  - **Methodology:** **Learned startup snapshots**: a *set* of small, fast-initializing snapshots each covering a fraction of workloads, together covering most. Snapshot construction is formulated as an optimization problem solved with an approximation algorithm, planned on **15K public + LLM-synthesized scripts**.
  - **Innovations:** shifts from single fat image / single snapshot to a learned portfolio of snapshots at a fixed storage budget — directly the infrastructure behind code-execution agents.
- **Comparison & results / 对比与结果（author-reported）:** Reduces startup latency **3–22×** and end-to-end runtime **1.3–3.3×** vs existing approaches at the same storage budget.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22171) · [PDF](https://arxiv.org/pdf/2611.22171)

### 7.3 From Sorry to QED: Refining LLM Math Proofs via Angelic Execution
**从 Sorry 到 QED：通过 Angelic Execution 精炼 LLM 数学证明**

- **Authors / 作者:** Yanju Chen, Hanzhi Liu, Ruizhe Qian, Jiaming Shan, Xu Yang, Yufei Ding, Osbert Bastani, Yu Feng
- **Affiliation / 机构:** UC San Diego; UC Santa Barbara; Penn State; University of Pennsylvania — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI), submitted 2026-11-17
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLMs generate Lean proof scripts capturing high-level structure, but one missing side condition or misapplied lemma aborts the prover and discards a viable outline.
  - **Methodology:** **MathEye** converts imperfect scripts into fully verified Lean proofs via **angelic proof checking**: an optimistic execution model replacing failing fragments with placeholders while preserving structure, isolating exact unresolved obligations. Because obligations are interdependent, a **proof dependence graph** captures symbol-level data flow; obligation selection is a **MaxSAT** optimization choosing a minimal-cost essential set. Answers are requested in ordinary mathematical language and used to reconstruct the complete proof.
  - **Innovations:** angelic execution + MaxSAT minimal-human-input obligation selection for formal proof repair.
- **Comparison & results / 对比与结果（author-reported）:** On **30 real-world benchmarks** across analysis and algebra, MathEye solves **93.3%** of problems while reducing required user interactions by **55%**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22103) · [PDF](https://arxiv.org/pdf/2611.22103)

### 7.4 Turing Agent: Agentic Formal Verification for Mathematical Research
**Turing Agent：面向数学研究的智能体形式化验证**

- **Authors / 作者:** Yang Chen, Qianyi Wang, Ronghui Yang, Zhanhao Li, Yu Cong, Chen Zhang, Hangfan Zhang, Shao Zhang, Shuai Li, Toru Takisaka, Chao Xu, Yi Zhou, Zhihao Tang, Xiao Wang, Bo Zhang, Shuyue Hu
- **Affiliation / 机构:** **Agent Center, Shanghai Artificial Intelligence Laboratory** (lead); UESTC; The University of Hong Kong; Shanghai University of Finance and Economics — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI), submitted 2026-11-16
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** AI-generated proofs are proliferating ("proof abundance"); how to ensure correctness and turn them into machine-verified knowledge? Focus on **theoretical computer science** (intricate quantification, dependencies, semantic requirements).
  - **Methodology:** **Turing Agent**, a two-scale harness integrating **theorem-formalization** and **proof-formalization** agents with structured proof decomposition, parallel verification, accumulated proof experience, selective semantic review; evaluated against direct generation and general coding harnesses (Codex CLI, Claude Code) using GLM-5.3 and DeepSeek-V4-Pro.
  - **Innovations:** end-to-end formal verification harness for research-level TCS; byproducts include simpler alternative proofs, unnecessary-dependency exposure and reusable mathematical knowledge.
- **Comparison & results / 对比与结果（author-reported）:** **≈57–62% faithful formalization success** on Formal TCS Bench and **83% overall pass@1** on a TCS-focused RLMEval subset; built on DeepSeek, it completes formal verification of **3 previously unresolved TCS tasks** from OpenAI's October 2026 collection (one required ~100 formally verified auxiliary claims).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21299) · [PDF](https://arxiv.org/pdf/2611.21299)

### 7.5 ATLAS-Finance: Benchmarking AI Agents in Realistic Banking Environments
**ATLAS-Finance：在真实银行环境中对 AI 智能体进行基准测试**

- **Authors / 作者:** Elaine Lau, Antoine Pangas, Alexandre Finot, Collin Schweiker, Amir Bouzidi, Hui Wen Goh, Andrew Peter Martin, Jonas Mueller
- **Affiliation / 机构:** **Handshake AI** — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI), submitted 2026-11-17
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Professional work is under-specified: relevant information is spread across workplace apps, may conflict, and changes over time — an economically valuable but poorly measured agent setting.
  - **Methodology:** **100 end-to-end investment-banking tasks** across **13 simulated firms**; agents search email, chat, calendars, notes, files to identify requirements, gather info, reconcile conflicts/updates, then build complex financial models. Tasks authored by experienced bankers from real deal work; humans take **15–30 hours** each. Expert-authored rubrics with **median 124.5 criteria** cover financial rationale/results, spreadsheet construction, completeness, formatting.
  - **Innovations:** realistic multi-app, conflicting-evidence bank workflow with expert rubrics rather than short synthetic QA.
- **Comparison & results / 对比与结果（author-reported）:** Despite completing substantial portions of requested work, current agents rarely produce correct deliverables — the best frontier models (**Claude Opus and Fable**) pass **fewer than 11%** of tasks.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22085) · [PDF](https://arxiv.org/pdf/2611.22085)

### 7.6 SWE-OPD: On-Policy Distillation for Agentic Coding
**SWE-OPD：面向智能体编码的 On-Policy Distillation**

- **Authors / 作者:** Yuhang He, Yanyu Chen, Chuanzhe Guo, Jie Zhu, Zichen Tian, Hongyu Ge, Zixuan Ren, Huang He, Bingjin Chen, Junyuan Shang, Shuohuan Wang, Yongqi Zhang, Irwin King, Jing Liu
- **Affiliation / 机构:** HKUST (Guangzhou); CUHK; Harbin Institute of Technology; **ERNIE Team, Baidu** — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI, cs.LG), submitted 2026-11-16; marked "under review"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** On-policy distillation (OPD) transfers agentic coding from large teachers to small students, but prior work focused on reasoning/short-horizon tasks; SWE tasks involve long interactions with executable repositories.
  - **Methodology:** Minimal OPD study: student interacts with executable repos while the teacher supervises the **prefixes visited by the student**. Three teacher–student pairs, two training sources, three SWE benchmarks. Also tests an **offline variant with cached teacher scores** and a **cross-tokenizer** extension.
  - **Innovations:** first focused OPD study for SWE agents; shows trajectory refresh is not strictly required and identifies a **support-mass gradient term** as a possible cause of repetition under top-K reverse-KL despite a decreasing loss.
- **Comparison & results / 对比与结果（author-reported）:** Qwen3.6-27B supervision raises Qwen3.5-9B **SWE-bench Pro resolve 35.9% → 39.4%**. Offline variant still beats student baselines while cutting end-to-end GPU-hours **59.4%–72.6%** and halving peak GPU allocation. Cross-tokenizer GLM-4.5-Air ← DeepSeek-V4-Flash-0731: **35.8% → 39.7%** (SWE-bench Pro) and **41.8% → 46.2%** (Multilingual).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21020) · [PDF](https://arxiv.org/pdf/2611.21020)

### 7.7 Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers
**复现并扩展权重空间编程：前沿 LLM 将程序编译进权重并读取输入层**

- **Authors / 作者:** Roksana Goworek, Alexander Hickey, Federico Nanni, Martin O'Reilly
- **Affiliation / 机构:** **The Alan Turing Institute** — PDF page 1
- **Venue / 会议:** arXiv working note (cs.CL, cs.AI), submitted 2026-11-16
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** MIT reported that GPT-6 Astra can write small-network weights in one reply and read weights to say what a network was trained to do — needs independent replication and interpretation.
  - **Methodology:** Three-day sprint replication with four findings: (1) weight-writing reproduces; (2) novelty is **program→weights compilation** (two models independently decompiled Astra's Breakout network into Python with identical actions across all tested states); (3) "reading weights" is mostly **reading the input layer**; (4) weight-only auditing is possible but shallow.
  - **Innovations:** reframes weight-space programming as compiling hand-designed programs, and weight-reading as reading the input-layer layout — a cautious interpretability claim.
- **Comparison & results / 对比与结果（author-reported）:** Astra Breakout networks scored **514/550/307** (MIT: 517) and matched on two novel modified games; decompilation matched actions in **49,189** states. On MNIST, Astra networks averaged **50%** vs a simple template classifier **82%**. Weight-only poisoning audit: detected a training-poisoned small LM **10/10**, post-hoc-poisoned **7/10**, malicious adapter **23/32**, but never identified trigger or malicious behaviour. Open-weight models lag.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21449) · [PDF](https://arxiv.org/pdf/2611.21449)

### 7.8 Weight-Space Programming Doesn't Need Transformers
**权重空间编程不需要 Transformer**

- **Authors / 作者:** Hyunjong Ok, Jaeho Lee
- **Affiliation / 机构:** **POSTECH** (Pohang University of Science and Technology) — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.LG, cs.AI, cs.CL), submitted 2026-11-17; marked "Preprint (Work in progress)"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Transformers were chosen because they train well with gradient descent and run fast on GPUs — reasons that **do not apply** when an LLM writes weights by hand with no gradients.
  - **Methodology:** Given minimal guidance, 10 labeled examples and a sandbox (mainly multiple-choice), three frontier LLMs either generate weights for a fixed architecture or design their own. When free to design, all three compile plain-text facts into a **sparse table queried by a fixed procedure**.
  - **Innovations:** proposes an **associative-memory-based model** that is interpretable (each weight's meaning stateable, wrong rows findable/rewritable) and GPU-efficient without gradients.
- **Comparison & results / 对比与结果（author-reported）:** Up to **54.4%** test accuracy; an LLM-designed model beats the most accurate released Transformer written by the same LLM while using ~**1,800× fewer parameters** (figure caption: 680× vs another reference); associative-memory model up to **17× faster** on GPUs than a same-sized Transformer. Pretrained LLMs remain more accurate — claim concerns structure, not raw accuracy.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22055) · [PDF](https://arxiv.org/pdf/2611.22055)

### 7.9 SkillBuffBench: Measuring What Agent Skills Contribute across Harnesses, Models, Skill Access Modes and Memory
**SkillBuffBench：衡量 Agent Skills 在不同 Harness、模型、技能访问模式与记忆下的贡献**

- **Authors / 作者:** Gengyue Dong, Ye Wei, Zheng Zhu, Yidong Han, Jiale Miao, Xiaojun Jia, Guanghui Li
- **Affiliation / 机构:** University of Oxford; MRC Weatherall Institute of Molecular Medicine (Oxford); Imperial College London; University College London; Nanyang Technological University; **BraneMatrix AI, Shanghai** — PDF page 1
- **Venue / 会议:** arXiv preprint (cs.AI, cs.CL, cs.LG), submitted 2026-11-17; 18 pages, 2 figures, 6 tables; **work in progress — results not yet added**
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Agent Skills (file-based procedural packages discovered/loaded on demand) ship with every major harness, but evidence for their value comes from settings where the right Skill is **hand-picked** and the agent starts **with a blank slate** — neither holds in deployment.
  - **Methodology:** Paired protocol treating Skill access as a 3-level factor (no Skill / curated Skill / automatic invocation from installed library), crossed with **memory off/on**, 4 harnesses, and multiple proprietary (Anthropic/Google/OpenAI) and open-weight Chinese models — every model under every harness. Domain-expert research tasks + their Skills, currently materials science and biology. Deterministic verifier; paired task-level bootstrap; cost/rounds/wall-clock reported separately.
  - **Innovations:** first controlled factorial design isolating Skill contribution from hand-selection and memory carryover.
- **Comparison & results / 对比与结果:** **No results yet** — this version describes design, protocol, tasks and Skills; evaluation in progress, rolling updates. Included for benchmark-design completeness; do **not** cite outcome numbers.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22017) · [PDF](https://arxiv.org/pdf/2611.22017)

---

## 8. Cross-cutting observations & focus-organization coverage

| Organization / lab | Papers in this digest (role) |
|---|---|
| **NVIDIA** | Nemotron 3.5 Bolt E4B 4GB (author, §6.1); "Can LLMs Give Good Product Advice?" — NVIDIA Research (§5.2); GB10 / B200 appear as evaluation platforms in §3.11 / §6.3 (not affiliations). |
| **Tencent** | Accelerate Bench — Tencent Hy Team (§7.1). |
| **Alibaba** | PEETS — Fliggy, Alibaba Group (§5.1). |
| **Baidu** | SWE-OPD — ERNIE Team (§7.6). |
| **ByteDance** | Readie — co-author (§7.2). |
| **Amazon** | AdMem — 3 Amazon authors (§3.9). |
| **Ant Group** | SpeCal — Zhejiang University + Ant Group (§4.4). |
| **China Telecom** | Xing 4 — Xingchen AGI Lab (§6.2). |
| **Shanghai AI Lab** | Turing Agent — Agent Center (§7.4). |
| **Other labs/industry** | GE Vernova (§4.2), Handshake AI (§7.5), Lila Sciences (§3.13), Genloop (noted in §8 note), ThakiCloud (§6.3), Datagrids.ai (§3.10), Alan Turing Institute (§7.7), BraneMatrix AI (§7.9). |
| **Google DeepMind / OpenAI / Meta AI / Microsoft Research / Apple / Netflix / Kuaishou / Anthropic** | **No new first-author paper in this fresh window.** Their models appear as evaluation targets: OpenAI/Google/Anthropic models audited in §4.3; Anthropic/Google/OpenAI + Chinese open-weight models in §7.9; OpenAI's Oct-2026 TCS task collection used in §7.4; Gemma/Qwen backbones in §6.1/§6.3. |

**Thematic cross-cuts**

1. **Verification & trust are the dominant theme.** Exact process oracles for RLVR (§3.6), peer-review version drift (§4.3), verifier-based multi-agent formal methods (§3.7), explanation audits in retail forecasting (§5.3), weight-only model auditing (§7.7), and pre-registered evaluation gates (§6.3) all attack the same problem: a proxy signal that looks good but is not the real objective.
2. **Memory is being engineered, not just accumulated.** AdMem (§3.9) shows naive cross-task memory hurts; EvoDisco and memory-conflict work appear in the sibling 2026-11-18 reports; SkillBuffBench (§7.9) factors memory into Skill evaluation; DetourBench (§3.10) scores the *trajectory*, not just the endpoint.
3. **Code execution is both a bottleneck and a benchmark.** Readie (§7.2) attacks sandbox startup; Solver2System (§3.12) shows executable code can encode invalid physics; Accelerate Bench (§7.1) evaluates whole-program optimization; SWE-OPD (§7.6) and MathEye (§7.3) supervise/repair executed code and proofs.
4. **Systems for MoE/diffusion scale are hitting memory/communication walls.** EchoMoE (§6.5) compresses expert-parallel traffic; RISA (§6.4) makes sparse attention recoverable for block diffusion; the MoE-diffusion sampler profiling (§3.11) shows quantization shifts the bottleneck from GEMMs to logits; Xing 4 (§6.2) details an Ascend-native stack.

---

## Flags & contradictions

- **Exact requested venues:** no new main-track papers in the 11-15→11-17 window. Forward-dated tags (**KDD 2027, ICLR 2027 decision-pending, EMNLP 2026, AAAI 2027 IAAI-27, CVPR 2027 submission**) are reported verbatim, not represented as KDD 2026 / ICLR 2026 / EMNLP 2025 / AAAI 2026 / CVPR 2026 results.
- **Affiliation caution:** "NVIDIA B200/GB10", "Apple Neural Engine"-style hardware mentions and model names (GPT/Claude/Gemma/Qwen) are subjects or evaluation platforms, not author affiliations — all 38 affiliations were checked on PDF page 1. §4.3 author affiliation was not stated; §3.9 third Amazon attribution was truncated in extracted text (first three Amazon authors PDF-verified).
- **§2.2 acceptance status:** `valueshift-icml-2026` code tag + "Preprint" marking — ICML-associated but acceptance not stated in the arXiv record.
- **§7.9** is a benchmark-design paper with **no results** in this version.
- **Author-reported metrics:** all numbers above are from abstracts/PDF page 1; not independently reproduced. Several papers explicitly flag their own negative/limited results (§3.6 damage magnitude not replicating; §5.1 cancellation interval; §6.3 final checkpoints not retained; §7.8 pretrained models still more accurate).
- **Preference file active:** `EXTEND.md` (repo root, bm25 mode `auto_prompt`); BM25 not triggered — no search thresholds crossed / no search behavior requested.
