---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-20 Daily Edition"
type: synthesis
created: 2026-11-20
updated: 2026-11-20
sources:
  - https://export.arxiv.org/api/query?search_query=all:%22ICML%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22AAAI%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22NeurIPS%202025%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22ICLR%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22KDD%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22CVPR%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22ACL%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22EMNLP%202025%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22SIGIR%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22WWW%202026%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22CIKM%202025%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:%22RecSys%202025%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  - General queries: all:recommendation / all:CTR / all:advertising / all:agent / all:generative / all:sequential / all:code execution / all:benchmark / all:LLM / all:game / all:MARL / all:diffusion / all:recommendation systems (max 40 each, sorted by submittedDate)
  - Supplement queries: all:MARL / all:Atari / all:chess / all:video game / all:gaming / all:Atari 2600 / all:board game (video-games/game-AI supplement)
  - id_list=2611.20445, 2611.20405, 2611.18370 (ICML 2026 allowlist — already covered by 2026-11-18 digest)
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, advertising, CTR, LLM, agents, generative-models, sequential-modeling, games, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-20 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-20 每日版）

> Venues covered: **ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025** — plus general recent papers in AI, LLMs, recommendation systems, advertising/CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks. Focus organizations: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon and top labs.

## Method, data window & limitations

- **Query date:** 2026-11-20. **Web search:** unavailable in this environment (`Web search cancelled`). **arXiv access:** arXiv Export API (`export.arxiv.org/api/query`) over HTTPS — 24 venue queries (quoted `all:"<Venue> <Year>"` + broad `all:<Venue>` fallback, venue-tagged results deduplicated and sorted by `submittedDate` desc) + 13 general topic queries + 7 video-games/game-AI supplement queries. ~1,300 venue-matched and ~200 general candidates scanned; 107 papers selected (62 venue + 45 general). Every selected ID grep-verified absent from the ~9.8k arXiv IDs referenced in `wiki/**`.
- **Venue papers:** accepted by the venue, from arXiv entries whose title/comments/abstract contain the venue name + year (e.g., "ICML 2026", "Accepted by AAAI 2026"); later-edition tags (e.g., "AAAI 2027 IAAI") excluded via venue-exclusion predicates. **ICML 2026 allowlist:** 3 published ICML 2026 main-track papers (2611.20445, 2611.20405, 2611.18370) already covered by the 2026-11-18 digest — still listed here for completeness.
- **General papers:** arXiv papers matching topic keywords (AI/LLMs, recommendation, advertising, CTR, games, code execution, agents, generative, sequential, benchmarks); capped at 30 (+10 video-games/game-AI supplement) — duplicates across queries removed by ID.
- **Affiliations:** recovered from arXiv PDF page-1 author/affiliation blocks (pypdf). **Evidence:** all metrics/results/claims are **author-reported** from abstracts; no full-text review beyond PDF page 1; no OpenReview/proceedings crawls possible (web search unavailable, dynamic venue pages). Chinese titles are translation aids.

---

## 1. Venue snapshot

| Venue | Status (as of 2026-11-20) | Papers (arXiv IDs, newest first) |
|---|---|---|
| **ICML 2026** | Published (PMLR 306, Seoul; 3 papers already covered by the 2026-11-18 digest, re-listed) | 2611.22557, 2611.20445, 2611.20405, 2611.18370, 2611.16361, 2611.10891, 2611.10684, 2611.07873 |
| **AAAI 2026** | Published — AAAI-2027 IAAI-tagged papers excluded | 2611.23609, 2611.15538, 2611.10023, 2611.05979 |
| **NeurIPS 2025** | Published | 2611.10906, 2611.10228, 2611.07370, 2611.02253, 2611.00438 |
| **ICLR 2026** | Published (rolling review) | 2611.19054, 2611.18409, 2611.17834, 2611.17811, 2611.13641 |
| **KDD 2026** | Published (SIGKDD 33rd) | 2611.19330, 2611.12725, 2611.12219, 2611.00885, 2610.41368 |
| **CVPR 2026** | Published | 2611.23887, 2611.22506, 2611.20625, 2611.09191, 2611.03438 |
| **ACL 2026** | Published | 2611.23218, 2611.21232, 2611.20191, 2611.19220, 2611.19030 |
| **EMNLP 2025** | Published (Findings) | 2610.33749, 2608.09280, 2607.07895, 2605.26840, 2604.24052 |
| **SIGIR 2026** | Published | 2611.14236, 2611.04619, 2611.03727, 2610.37231, 2610.33078 |
| **WWW 2026** | Published (ACM Web Conference) | 2611.03090, 2610.36010, 2609.23405, 2609.10260, 2608.04883 |
| **CIKM 2025** | Published (SIGIR 2025→CIKM 2025) | 2601.11954, 2603.21024, 2512.09260, 2511.20729, 2511.18816 |
| **RecSys 2025** | Published (ACM SIGIR) | 2611.13972, 2511.14865, 2510.22865, 2510.13359, 2510.11402 |

---

## 2. ICML 2026 — Published Proceedings (PMLR 306, Seoul)

### 2.1 Balancing Exploration and Exploitation in Constrained Combinatorial Optimization with U(1)-Symmetric Tensor Trains
**在 U(1)-对称张量列训练中，在约束的组合优化中平衡探索与利用**

- **Authors / 作者:** Sergei Iudin, Mikhail Podobrii, Dmitry Zheltkov, Stanislav Moiseev
- **Affiliation / 机构:** 1Moscow Independent Research Institute of Artificial Intelligence (miRAI), 23 rubles 3rd floor, bldg.1, Golovinskaya St. (PDF page 1); corresponding: Sergei Iudin <iudin.s@miriai.org> (truncated).
- **Venue / 会议:** **ICML 2026**, 39 pages incl. supplementary material. Code: https://github.com/antientropic-guy/OhMyU1_public
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Tensor Train (TT) decomposition mitigates the curse of dimensionality in combinatorial optimization and generative modeling, but incorporating hard linear constraints is hard: existing interpolation/sampling approaches fail when feasible points are rare.
  - **Methodology:** A general TT-based framework for constrained combinatorial optimization built upon U(1)-symmetric tensor networks; the method "introduces..." — TT-based generative models that explore high-dimensional discrete spaces where the cost function structure is unknown.
  - **Key innovations:** U(1)-symmetric tensor-network TT framework; handles hard linear constraints (unlike prior methods); model-agnostic.
- **Comparison with prior methods / 对比:** Prior approaches "either interpolate/sample in the unconstrained space and fail when feasible points are rare, or replace expressive task models with interpretable surrogates that sacrifice accuracy" — the method works on constrained spaces directly.
- **Experimental results / 结果：** Results in abstract not visible beyond page-1 excerpt (author-reported).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22557) · [PDF](https://arxiv.org/pdf/2611.22557v1)

### 2.2 Explainable Federated Learning via Global-Local Attribution Alignment (xFedAlign)
**通过全局-局部归因对齐实现可解释联邦学习 (xFedAlign)**

- **Authors / 作者:** Dawood Wasif, Terrence J. Moore, Chang-Tien Lu, Jin-Hee Cho
- **Affiliation / 机构:** Virginia Tech (Dept. of Computer Science, Falls Church, VA); DEVCOM Army Research Laboratory (Adelphi, MD) — PDF page-1 footnote.
- **Venue / 会议:** **ICML 2026** — "Published in Proceedings of the 43rd International Conference on Machine Learning (ICML 2026)"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Federated learning (FL) trains on-device without centralizing data, but explanations are hard to make locally faithful and globally consistent under privacy/bandwidth limits.
  - **Methodology:** xFedAlign (model-agnostic) decouples task optimization in parameter space from explanation coordination in a compact group space; each client distills a lightweight surrogate producing private per-class top-k attribution artifacts; the server aggregates them into a Global Explanation Prior that softly aligns client explanations without constraining task learning.
  - **Key innovations:** private attribution artifacts + server-side global prior; only a few kilobytes extra communication per round.
- **Comparison with prior methods / 对比：** Prior approaches either silo explanations per client, transmit heavy/sensitive artifacts, or replace the task model with an interpretable surrogate losing accuracy.
- **Experimental results / 结果：** Across image/text/tabular benchmarks with IID and non-IID partitions, xFedAlign matches FedAvg accuracy while reducing explanation drift and improving deletion and insertion AUC vs Local-XAI, FedAttr-Agg and Fed-XAI; reduced membership-inference advantage and higher resistance to attribution poisoning.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20445) · [PDF](https://arxiv.org/pdf/2611.20445v1)

### 2.3 Refusal Register is Causally Steerable: Decomposing the Refusal Direction into Category-Aligned Components in Gemma-2-9B-IT
**拒绝语域可被因果操控：在 Gemma-2-9B-IT 中将拒绝方向分解为类别对齐的分量**

- **Authors / 作者:** Janhavi Khindkar, Nataliia Povarova
- **Affiliation / 机构:** Independent Researcher (PDF footnote: "Independent Researcher"; correspondence research.iiit.ac.in) — *not* an IIIT campus affiliation.
- **Venue / 会议:** Code repository tagged `valueshift-icml-2026`; "10 pages, 7 figures. Code: https://github.com/Jank14/valueshift-icml-2026"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Arditi et al. (2024) showed refusal can be ablated via one residual-stream direction; later work found multiple directions/concept cones. The question: do refusal directions encode the *register* of refusal language — how the model refuses — not just whether it refuses?
  - **Methodology:** In Gemma-2-9B-IT, two SVM-derived linear directions at layer 20: **B1** (harmful-content vs neutral) and **B2** (self-reference vs neutral) — cos(B1,B2) = 0.252 (~75°, far from parallel). Adding the harmful-vs-neutral diff-of-means direction (cosine 0.68 with B1) to the residual stream of self-reference prompts at α = 2.0.
  - **Key innovations:** category-aligned decomposition of the refusal direction; causal switch of refusal *style* (meta-style "as a language model…" → content-style "this would be harmful") while refusal itself is preserved.
- **Experimental results / 结果：** Content-safety vocabulary rises **2.55 → 10.37 hits/100 tokens** vs magnitude-matched random direction **1.13–2.16**; replicated in Gemma-2-2B-IT at layer 12 (**1.72 → 6.37** vs random 1.35); B1's causal effects consistently larger than B2's.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20405) · [PDF](https://arxiv.org/pdf/2611.20405v1)

### 2.4 f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models (DiSPaT)
**基于 f-发散自我博弈的表格异常检测 LLM 方法 (DiSPaT)**

- **Authors / 作者:** Hoang Tran Vuong, Linh Ngo Van, Dang Nguyen, Thin Nguyen
- **Affiliation / 机构:** 1Hanoi University of Science and Technology, Hanoi, Vietnam; 2Applied Artificial Intelligence Initiative, Deakin University, Australia; 3Monash University, Clayton, VIC 3800, Australia.
- **Venue / 会议:** **ICML 2026** — "Accepted at ICML 2026. 28 pages, 7 figures"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Anomaly detection in tabular data suffers from heterogeneous feature types (numerical, categorical, textual); recent LLM approaches serialize rows as text but rely on one-shot SFT offering limited signal to tighten the description of normality.
  - **Methodology:** **DiSPaT** — self-play fine-tuning framework built on f-divergence minimization: derives a tight approximation connecting the model's understanding of normality to the divergence between predicted and true row distributions; empirically demonstrated on tabular datasets.
  - **Key innovations:** f-divergence-based self-play fine-tuning for tabular anomaly detection with LLMs.
- **Experimental results / 结果：** (author-reported; see PDF — abstract results section).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18370) · [PDF](https://arxiv.org/pdf/2611.18370v1)

### 2.5 MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects
**MutAtlas：基于 PDB 全面结构引导的蛋白质突变影响能量图谱**

- **Authors / 作者:** Ruihan Guo, Chaoran Cheng, Zhanghan Ni, Neil He
- **Affiliation / 机构:** Siebel School of Computing and Data Science, University of California, Berkeley; Center for Advanced Bioenergy and Bioproducts, University of California, Berkeley (truncated in PDF page 1).
- **Venue / 会议:** **ICML 2026** — "Accepted at the 43rd International Conference on Machine Learning (ICML 2026)"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Protein mutation effect prediction is fundamental to protein engineering and disease variant interpretation, but experimentally measured mutation data remain "accurate but extremely sparse."
  - **Methodology:** Constructs a PDB-wide mutation augmentation dataset exhaustively enumerating single-site substitutions on experimentally resolved protein structures; aligns mutation signals from physics-based energy models, protein language models, and inverse folding models; "Large-scale analysis under a unified mutation preference representation reveals substantial differences in the consistency, concentration, and substitution patterns of mutation distribution..." (truncated).
  - **Key innovations:** PDB-wide mutation augmentation dataset + unified mutation-preference representation analysis.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.16361) · [PDF](https://arxiv.org/pdf/2611.16361v1)

### 2.6 Approximate Recall, Approximate Forecasts: Recall as a Diagnostic for LLM Forecasting Errors
**近似回忆，近似预报：以 LLM 幻觉预测误差的诊断指标为框架**

- **Authors / 作者:** Prashanth Bhaskara, Shubhaankar Gupta, Seojoon Yeon
- **Affiliation / 机构:** Not stated on PDF page 1 (see PDF footer).
- **Venue / 会议:** **ICML 2026** — "Accepted as a Spotlight at the ICML 2026 Workshop on Forecasting as..."
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLMs exhibit *approximate recall*: they retain coarse associations about past events while losing fidelity on details; forecasting ability is not well measured by prediction-market benchmarks because errors may stem from recall issues.
  - **Methodology:** Introduces the **Recall Fidelity Score** — a metric studying how imprecision in internalized knowledge impacts forecasting; example: an LLM correctly recalls "Did Anna Sawai win the Best Drama Actress in the 76th Emmy Awards?" is "Yes" but misstates the date as September 22 vs September 15.
  - **Key innovations:** Recall Fidelity Score — a diagnostic metric for LLM forecasting errors via approximate recall.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.10891) · [PDF](https://arxiv.org/pdf/2611.10891v1)

### 2.7 Audit Before You Merge: Provenance, Probing, and Continual LoRA Composition
**合并前审计：来源、探测与持续 LoRA 组合**

- **Authors / 作者:** Lenny Aharon, Neta Glazer, Lior Aharon
- **Affiliation / 机构:** Columbia University, New York, NY; Bar-Ilan University (PDF page 1).
- **Venue / 会议:** **ICML 2026** — "ICML 2026 Workshop on Continual Adaptation at Scale (CATS). Code: https://gith..."
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Post-hoc merging of public LoRA adapters is attractive for continual adaptation, but measuring catastrophic forgetting depends on infrastructure prior work has not addressed; public adapter hubs contain modules failing basic provenance checks: "silent base-version mismatches and near-zero delta norms whose inclusion inflates measured interference by ~10pp."
  - **Methodology:** Treats each adapter merge as a sequential task; proposes a two-check audit (base-model match, non-trivial delta norm) and a leakage-free... (protocol replicates on Mistral-7B-Instruct-v0.3; PDF page 1).
  - **Key innovations:** two-check audit for LoRA adapter provenance under continual merging.
- **Experimental results / 结果：** Protocol replicates on Mistral-7B-Instruct-v0.3; near-zero delta-norm modules inflate interference by ~10pp without audit.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.10684) · [PDF](https://arxiv.org/pdf/2611.10684v1)

### 2.8 PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation
**PVDepth：基于几何感知时空适应的全景视频深度估计**

- **Authors / 作者:** Chuanxin Song, Peixi Peng
- **Affiliation / 机构:** 1Peking University; 2Pengcheng Laboratory (PDF page 1).
- **Venue / 会议:** **ICML 2026** — "ICML 2026, Project Page: https://chuanxinsong.github.io/pvdepth-project-page"
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Panoramic video depth estimation (ERP) is impeded by scarcity of large-scale training data and ERP geometric distortions; direct transfer of perspective models fails.
  - **Methodology:** Presents **PanoCARLA**, a large-scale synthetic RGB-D panoramic video dataset; **PVDepth** — an end-to-end framework adapted from perspective video depth models; geometrically-aware spatiotemporal adaptation; project page.
  - **Key innovations:** PanoCARLA synthetic dataset + PVDepth framework for ERP depth estimation.
- **Experimental results / 结果：** (author-reported; see PDF/project page).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.07873) · [PDF](https://arxiv.org/pdf/2611.07873v1)

---

## 3. AAAI 2026

### 3.1 Label-Free Role-Aware Segmentation of Classroom Recordings: Recovering the Teacher from Transferable Structure
**无标签角色感知的课堂录音分割：从可迁移结构中恢复教师**

- **Authors / 作者:** Nitin Jain, Tim Fütterer, Babette Bühler, Çağatay Yıldız
- **Affiliation / 机构:** Hector Research Institute of Education Sciences and Psychology, University of Tübingen; Chair of Human-Centered Technologies for Learning, Technical University of Munich; Tübingen AI Center, University of Tübingen (PDF page 1).
- **Venue / 会议:** **AAAI 2026** — "Accepted at the AAAI track is IAAI (Innovative Applications of AI)" (published 2026-11-17)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Classroom audio is among the most sensitive data an AI system can process (minors; GDPR) — pipelines must be label-free, on-device, and calibration-free.
  - **Methodology:** Teacher-student segmentation pipeline: lightweight voice activity detector → compact speaker embeddings → agglomerative clustering → logistic regression assigning the teacher role by session-relative structure.
  - **Key innovations:** label-free at inference, runs on a recording device, no per-session calibration.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.23609) · [PDF](https://arxiv.org/pdf/2611.23609v1)

### 3.2 Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition
**分步忠实：通过查询分解改善 RAG 的泛化与引用**

- **Authors / 作者:** Yue Liu, Zhongying Ru, Shimin Di, Jipeng Zhang
- **Affiliation / 机构:** 1The Hong Kong University of Science and Technology (HKUST); 3School of Computer Science and Engineering, Southeast University; 4Key Laboratory of New Generation Artificial Intelligence Technology and Its Interdisciplinary Applications (PDF page 1).
- **Venue / 会议:** **AAAI 2026** — "Accepted by AAAI 2026" (published 2026-11-11)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Existing attributable-RAG (RAGQ) systems exhibit significant degradation on multi-hop/multi-modal questions — over-citation, implicit entity identification failure, poor generalization.
  - **Methodology:** **QDRAG** breaks the input question into atomic subquestions to identify implicit entities; ... (truncated)
  - **Key innovations:** query decomposition framework for faithful citation in retrieval-augmented generation.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.15538) · [PDF](https://arxiv.org/pdf/2611.15538v1)

### 3.3 Executable Specifications as First-Class Independent Verification and Validation Artifacts for Quantum Information and Machine Learning
**可执行规范作为量子信息与机器学习的一等 IV&V 产物**

- **Authors / 作者:** Ragib Shahariar Ayon, Shibbir Ahmed
- **Affiliation / 机构:** Department of Computer Science, Texas State University.
- **Venue / 会议:** **AAAI 2026** — "4 pages, position paper, published at the Second AAAI Symposium on Quantum Information & Machine Learning (QIML)" (published 2026-11-05)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Executable specifications make software assumptions explicit and checkable, but their role in QIML IV&V remains underexplored (static analysis/testing/simulation/runtime checking give partial evidence).
  - **Methodology:** Treats executable specifications as first-class IV&V artifacts; Design-by-Contract adaptations make quantum-state/measurement/statistical properties checkable. (PDF truncated)
  - **Key innovations:** executable specifications as first-class IV&V artifacts for QIML systems.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.10023) · [PDF](https://arxiv.org/pdf/2611.10023v1)

### 3.4 Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation
**从人类学习以对象为中心的动作先验用于灵巧机器人操作**

- **Authors / 作者:** Zhengdong Hong, Guofeng Zhang
- **Affiliation / 机构:** State Key Lab of CAD&CG, Zhejiang University.
- **Venue / 会议:** **AAAI 2026** — "Accepted as an oral paper at AAAI 2026 (Website: https://ojs.aaai.org/index.php/AAAI/article/view/38892)" (published 2026-11-04)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Manipulating diverse objects with multi-fingered dex hands is challenging (high-dim dynamics); HOI datasets provide rich task info and embodied interaction knowledge, but imitation alone is brittle.
  - **Methodology:** Learns object-centric motion priors from human HOI data: predicts future hand-object states, which serve as generalizable reward terms for RL, reducing task-specific reward engineering and enhancing generalization across tasks; extensive experiments on 3 tasks in simulation and the real world.
  - **Key innovations:** object-centric motion priors from human data — predicted future states as general-purpose RL rewards.
- **Experimental results / 结果：** Extensive experiments on three manipulation tasks in simulation and the real world.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.05979) · [PDF](https://arxiv.org/pdf/2611.05979v1)

---

## 4. NeurIPS 2025

### 4.1 SCorPion: A Strategic, Controllable and Personified Conversational Companion
**SCorPion：战略、可控且人格化的对话伴侣**

- **Authors / 作者:** Luo Ji, Xiyuan Chen, Dan Wang, Qingqing Gu
- **Affiliation / 机构:** Geely AI Lab, Zhejiang, China.
- **Venue / 会议:** **NeurIPS 2025 PersonaLLM Workshop** (published 2026-11-07)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Fixed prompt-based LMs face open-domain conversation challenges (topics need expert advice/demonstrations); goal: maximum universal performance across versatile topics.
  - **Methodology:** Extracts different chatting strategies from varied text corpora; SCorPion — conversational companion using GraphRAG to extract/summarize a global knowledge graph, community-summarized strategies, query-focused optimal strategies; personified voice with strategic thinking.
  - **Key innovations:** personaLLM-style personified conversational companion with GraphRAG strategy extraction and query-focused optimal strategy generation.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.10906) · [PDF](https://arxiv.org/pdf/2611.10906v1)

### 4.2 FAIR Universe Weak Lensing ML Uncertainty Challenge: Dataset and Cosmological Inference Competition
**FAIR Universe 弱引力透镜 ML 不确定性挑战：数据集与宇宙推断竞赛**

- **Authors / 作者:** Biwei Dai, Po-Wen Chang, Erwan Allys, Wahid Bhimji
- **Affiliation / 机构:** Institute for Advanced Study; Lawrence Berkeley National Laboratory; École normale supérieure – Sorbonne Université (APC lab, CNRS); New York University; Tsinghua University; SLAC National Accelerator Laboratory (PDF page 1; multiple affiliates).
- **Venue / 会议:** **NeurIPS 2025** — "10+7 pages, 2+4 figures, 2+1 tables. Key results of the NeurIPS 2025 FAIR Universe Weak Lensing ML Challenge P..." (published 2026-11-06)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Progress on weak-lensing ML has been limited by the lack of standardized benchmarks capturing dataset complexity, simulator imperfections, and realistic systematic biases.
  - **Methodology:** FAIR Universe Weak Lensing ML Uncertainty Challenge — one of the NeurIPS 2025 ML Challenges; standardized benchmark + competition framework for uncertainty quantification in weak-lensing surveys.
  - **Key innovations:** standardized weak-lensing ML uncertainty benchmark with public datasets + competition infrastructure.
- **Experimental results / 结果：** (key challenge results in abstract — truncated).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.10228) · [PDF](https://arxiv.org/pdf/2611.10228v1)

### 4.3 Breaking TraintoDefend via Adaptive Neuron Clustering in Cryptanalytic Model Extraction
**通过自适应神经元聚类打破 TraintoDefend 的密码分析模型提取**

- **Authors / 作者:** Haojie Wu, Haolin Liu, Tianshuo Cong, Guoyan Zhang
- **Affiliation / 机构:** School of Cryptologic Science and Engineering, Shandong University; School of Computer Science, Shanghai Jiao Tong University; School of Cryptologic Science and Engineering, Shandong University (PDF page 1).
- **Venue / 会议:** **NeurIPS 2025** (published 2026-11-05)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Cryptanalytic model extraction is a fundamental threat to DL model confidentiality (precise parameter recovery, functional equivalence).
  - **Methodology:** **TraintoDefend** (NeurIPS 2025) — proposed defense that encourages neurons to learn similar weights so activations switch together; the attack weakens the assumption: neurons with similar weights need not switch activation states together under small perturbations; instead weight si[milarity without activation co-switching] ...
  - **Key innovations:** a new attack showing the neuron-clustering assumption of TraintoDefend is breakable; weight-similarity-without-activation-synchronization.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.07370) · [PDF](https://arxiv.org/pdf/2611.07370v1)

### 4.4 Calibration-Constrained Diagnostics for Evaluating LLM Self-Evaluation
**面向 LLM 自我评估的校准约束诊断**

- **Authors / 作者:** Jae Oh Woo, Mengdie Flora Wang, Rahul Ghosh, Baishali Chaudhury
- **Affiliation / 机构:** AWS Generative AI Innovation Center; authors with @amazon.com addresses (PDF page 1).
- **Venue / 会议:** **NeurIPS 2025** — "38 pages, 7 figures, 17 tables. Extended and substantially revised version of the non-archival NeurIPS 2025 LA..." (published 2026-11-01)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLMs' self-reported confidence must support confidence-gated act-or-defer decisions, but aggregate uncertainty summaries produce deployment-misleading rankings — models ranking best under standard calibration can fail under category-level calibration constraints.
  - **Methodology:** A reusable evaluation artifact (black-box protocol, prompts, judge-reference labels, model outputs, reproduction scripts, calibration-constrained diagnostic metrics) for auditing LLM self-evaluation across math/factual/commonsense tasks.
  - **Key innovations:** calibration-constrained diagnostics: category-level calibration constraints vs aggregate; central finding that aggregate uncertainty rankings can mislead.
- **Experimental results / 结果：** Model appears strongest under standard aggregate calibration but fails under category-level constraints (aggregate rankings unreliable).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.02253) · [PDF](https://arxiv.org/pdf/2611.02253v1)

### 4.5 Statistical Inference under Performativity: From Policy Feedback to Self-Evolving Systems
**准确形态性下的统计推断：从策略反馈到自进化系统**

- **Authors / 作者:** Tianwei Gao, Garrett G. Wen, Huiying Zhong, Lihua Lei
- **Affiliation / 机构:** Yale University; Massachusetts Institute of Technology; Stanford University (PDF page 1).
- **Venue / 会议:** **NeurIPS 2025** — "Extended version of the NeurIPS 2025 paper 'Statistical Inference under Performativity' (arXiv:2505.18493)" (published 2026-10-30)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Performativity arises when prediction-informed decisions change the data-generating process (feedback between deployment and learning); estimation errors propagate across repeated updates.
  - **Methodology:** An end-to-end framework for statistical inference under performativity: for repeated risk minimization and repeated gradient descent, central limit theorems at fixed deployment rounds; covariance recursions capturing current-round sampling ...
  - **Key innovations:** statistical CLT + covariance recursions for repeated-deployment inference under self-evolving data distributions.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00438) · [PDF](https://arxiv.org/pdf/2611.00438v1)

---

## 5. ICLR 2026

### 5.1 When Reviews Gate Access: Collusion, Sabotage and the Scale of Peer Review in the AI Submission Surge
**审稿正规化访问限制：AI 投稿激增中的联合/破坏与审稿规模**

- **Authors / 作者:** Yuchen Li, Xintong Li, Ken-Tye Yong, Nguyen H. Tran
- **Affiliation / 机构:** University of Sydney (PDF page 1).
- **Venue / 会议:** **ICLR 2026** (published 2026-11-14)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** AI tools push submissions to the largest ML venues (tens of thousands per cycle); venues tie access to review (per-author caps, reciprocal reviewing, earned reviewer eligibility, bids-based assignment) — reviewers become competitors of authors.
  - **Methodology:** Agent-based conference calibrated to public statistics of NeurIPS and ICLR; run 6,220 simulated conferences.
  - **Key innovations:** agent-based peer-review simulation quantifying collusion vs sabotage deviations of review-gated access rules.
- **Experimental results / 结果：** Four results stand out: the two deviations do different harm; ..."
  (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19054) · [PDF](https://arxiv.org/pdf/2611.19054v1)

### 5.2 Fuse-PINN: Combining Finite Element Methods and Physics-Informed Neural Networks to enable massively parallel simulations of non-linear PDEs
**Fuse-PINN：结合有限元方法与物理信息神经网络，实现非线性 PDE 的大规模并行仿真**

- **Authors / 作者:** Stanislas Pamela, Nicolas Pailliez, Emmanuel Franck, Victor Michel-Dansac
- **Affiliation / 机构:** Research in the domain of Physics-Informed Neural Networks applied to PDE modelling... (PDF page 1).
- **Venue / 会议:** **ICLR 2026** — "Rejected at ICLR" (published 2026-11-13)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** PINNs are typically unable to scale out on HPC architectures (toy models, few variables, long-time nonlinear physics); "Part of the AI community has even adopted the idea that 'PINNs don't scale'."
  - **Methodology:** Fuse-PINN proves otherwise: combines FEM with PINNs; "This work proves otherwise..." (PDF truncated — author-reported results in abstract).
  - **Key innovations:** FEM+PINN hybrid for massively parallel nonlinear PDE simulation.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18409) · [PDF](https://arxiv.org/pdf/2611.18409v1)

### 5.3 PaperCritic: Training AI Reviewers to Assess the Soundness of Papers
**PaperCritic：训练 AI 评审员评估论文可靠性**

- **Authors / 作者:** Hyun Ryu, Ji Yong Cho, Eunho Yang, Moontae Lee
- **Affiliation / 机构:** 1KAIST AI; 2Carnegie Mellon University Language Technologies Institute; 3LG AI Research (PDF page 1).
- **Venue / 会议:** **ICLR 2026** (published 2026-11-13)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** AI reviewers as an alternative to human reviewing, but the learning objective: maximize precision (soundness/substantiveness of review points) and recall (coverage of high-quality reference review points) — "reviewing serves multiple purposes, including evaluating papers' soundness, interestingness, and clarity, the last two of which are subjective."
  - **Methodology:** Constructs a quality-labeled review point dataset, PaperSoun[dness-oriented]... (truncated).
  - **Key innovations:** precision+recall objective for training sound AI paper reviewers.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17834) · [PDF](https://arxiv.org/pdf/2611.17834v1)

### 5.4 AI Reviews Are Biased Towards the Appendix
**AI 评审存在向附录的偏见**

- **Authors / 作者:** Saptarshi Ghosh, Mohammad Saim, Tianyu Jiang
- **Affiliation / 机构:** University of Cincinnati.
- **Venue / 会议:** **ICLR 2026** (published 2026-11-13)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLMs are increasingly used by reviewers to highlight weaknesses; outputs shape human reviews; little is known about which parts of a paper LLM reviewers actually criticize.
  - **Methodology:** Audits 2,000 papers from ACL, EMNLP, COLM, ICLR; shows the latest GPT and Claude models draw about **50% or more of their review weaknesses from the appendix** (across API/coding-agent/web access methods), while humans draw only **8.4%**.
  - **Key innovations:** systematic audit of LLM-reviewer bias toward the appendix; baselines across access methods.
- **Experimental results / 结果：** LLMs draw ~50%+ of review weaknesses from the appendix vs humans' 8.4%.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17811) · [PDF](https://arxiv.org/pdf/2611.17811v1)

### 5.5 MOAI: Module-Optimizing Architecture for non-interactive secure transformer Inference
**MOAI：面向非交互式安全 Transformer 推理的模块优化架构**

- **Authors / 作者:** Linru Zhang, Xiangning Wang, Jun Jie Sim, Zhicong Huang
- **Affiliation / 机构:** 1Nanyang Technological University; 2Ant International; 3Ant Group (PDF page 1).
- **Venue / 会议:** **ICLR 2026** — "Published elsewhere. Minor revision. ICLR 2026" (published 2026-11-13)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** HE (homomorphic encryption) offers non-interactive secure inference over encrypted inputs; the high computational overhead remains the bottleneck.
  - **Methodology:** **MOAI** — efficient HE-based, non-interactive framework for secure transformer inference; gains efficiency from (1) novel evaluation flow combining column and diagonal packing; (2) rotation-free algorithms for Softmax... (truncated).
  - **Key innovations:** MOAI — column/diagonal packing + rotation-free algorithms for HE-based secure transformer inference.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.13641) · [PDF](https://arxiv.org/pdf/2611.13641v1)

---

## 6. KDD 2026

### 6.1 Benchmarking the State of AI for Crop Yield Forecasting: A Global Assessment Across Modeling Paradigms
**基于多建模范式的全球作物产量预测 AI 状态基准测试**

- **Authors / 作者:** Michiel Kallenberg, Philip Janz, Christoph Jörges, Vageesh Saxena
- **Affiliation / 机构:** Wageningen University and Research; Potsdam Institute for Climate Impact Research (PIK), Germany (PDF page 1).
- **Venue / 会议:** **KDD 2026** — "Accepted for publication in Proceedings of the 33rd ACM SIGKDD Conference on Knowledge Discovery and Data Mining" (published 2026-11-14)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Relative strengths of statistical/process-based/feature-engineered ML/deep-sequence/tabular-foundation-model paradigms for crop yield forecasting remain poorly understood (no large-scale standardized comparisons).
  - **Methodology:** Comprehensive benchmark of five modeling paradigms using the **CY-Bench** benchmark: 63 country-crop datasets spanning >12,000 administrative regions across six continents.
  - **Key innovations:** CY-Bench — large-scale global crop-yield benchmark (63 country-crop datasets, 6 continents); 5-paradigm comparative assessment (KDD 2026).
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19330) · [PDF](https://arxiv.org/pdf/2611.19330v1)

### 6.2 Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal Approach
**基于生成式 AI 的无分类标签法图像标注的可扩展性：多模态方法**

- **Authors / 作者:** Zhenjie Zhang, Sainan Chen, Kshiteesh Hegde, Mengze…
- **Affiliation / 机构:** Sainan Chen, Pinterest, Inc., Toronto, Canada; Pouya Rezazadeh Kalehbasti, Pinterest (truncated PDF page 1 — see PDF).
- **Venue / 会议:** **KDD 2026** — "5 pages, 3 figures, 4th CJ Workshop at KDD 2025 (https://sites.google.com/view/kddcjworkshop2025/accepted-pape…)" (published 2026-11-09)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Real-time multimodal insights from images require low latency, high accuracy, scalable inference — but traditional strategies build taxonomies (golden label sets via humans), train models on them, and deploy — constrained by fixed taxonomy, high labeling cost, limited labeled data.
  - **Methodology:** Generative-AI-based image labeling framework ("TAXON" — see PDF); zero-label multimodal labeling with clustering; "generalizes to members of the [cluster]..." (truncated).
  - **Key innovations:** taxonomy-free generative image labeling for multimodal retail catalogs.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.12725) · [PDF](https://arxiv.org/pdf/2611.12725v1)

### 6.3 An Empirical Evaluation of Quantum Kernel Stability in Network Intrusion Detection
**网络入侵检测中量子核稳定性的实证评估**

- **Authors / 作者:** Sreejonty Chakraborty, Adrita Rahman Tory, Muhammad Aminur Rahaman, Khondokar Fida Hasan
- **Affiliation / 机构:** Department of Computer Science and Engineering, Bangladesh University of Business and Technology; Department of Data Science and Engineering (PDF page 1).
- **Venue / 会议:** **KDD 2026** — "6 pages" (published 2026-11-09)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Quantum kernel methods for network intrusion detection — performance attributed to hardware noise; evaluated "through a controlled analysis of Pegasos-QSVC on the NSL-KDD and ToN-IoT datasets."
  - **Methodology:** 56 quantum experiments: one exact noiseless statevector backend + three noise-simulated superconducting backends, identical preprocessing/PCA/splits/classical baselines; compares with XGBoost baseline (98.94% on NSL-KDD, 99.41% on ToN-IoT vs Pegasos-QSVC 91.80% / 82.98%).
  - **Key innovations:** quantum kernel stability evaluation (seed-dependence, noise) — ToN-IoT accuracy +16.4pp over classical baseline.
- **Experimental results / 结果：** NSL-KDD: XGBoost 98.94% vs Pegasos-QSVC 91.80%; ToN-IoT: XGBoost 99.41% vs Pegasos-QSVC 82.98%; quantum model has substantially greater seed-dependent...
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.12219) · [PDF](https://arxiv.org/pdf/2611.12219v1)

### 6.4 Where Does a Variational Quantum Classifier Lose Accuracy? Angle Encoding, Readout and the Fidelity-Kernel Reference in Cyberattack Detection
**变分量子分类器为何在网络攻击检测中丢失准确率？角度编码、读出与保真度核参考**

- **Authors / 作者:** Angelos Thomos, Theodore Andronikos
- **Affiliation / 机构:** 1 Department of Informatics, Ionian University (PDF page 1).
- **Venue / 会议:** **KDD 2026** (published 2026-10-31)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Hard to diagnose where a poorly performing VQC loses accuracy: encoding, trained circuit, or readout.
  - **Methodology:** Builds on amplitude-encoded classifier (NCLS-KDD benchmark); compares angle vs amplitude encoding, one component at a time, measures each against classical SVM yardstick — "Most of the shortfall lies in the readout. Reading one qubit, or the parity of all qu..." (truncated).
  - **Key innovations:** fine-grained diagnostic of VQC failure modes (encoding/readout/fidelity-kernel).
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00885) · [PDF](https://arxiv.org/pdf/2611.00885v1)

### 6.5 RECITE: Revising Eligibility Criteria Incorporating Textual Evidence
**RECITE：结合文本证据的资格标准修订**

- **Authors / 作者:** Russell Ro, Reza Abbasi-Asl
- **Affiliation / 机构:** 1University of California, San Francisco; 2University of California, Berkeley (PDF page 1).
- **Venue / 会议:** **KDD 2026** — "Extended version of a paper in KDD 2026 (32nd ACM SIGKDD Conference on Knowledg…" (published 2026-10-30)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Overly restrictive eligibility criteria cause widespread enrollment failure in clinical trials; recommendations for broadening are disconnected from trial design at scale.
  - **Methodology:** RECITE — automated discovery/extraction/implementation of evidence-based eligibility criteria revisions; builds a dataset of **11,913 curated instances** across **5,735 trials** from protocol amendment documents on ClinicalTrials.gov (each pairing original criteria with documentary evidence and target revisions); benchmarks 15 LLM configs.
  - **Key innovations:** RECITE pipeline (evidence-based eligibility revision generation using amendments + 15-LLM benchmark).
- **Experimental results / 结果：** 11,913 curated instances; fifteen LLM configurations benchmarked (author-reported).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.41368) · [PDF](https://arxiv.org/pdf/2610.41368v1)

---

## 7. CVPR 2026

### 7.1 Can AI Understand Indonesian Children's Book Illustrations? Compliance, Safety, and the Cultural Alignment Gap
**AI 能否理解印尼儿童图书插图？合规、安全与文化对齐鸿沟**

- **Authors / 作者:** Rian Adam Rajagede, Rochana Prih Hastuti, Fitri Hasanah Amhar
- **Affiliation / 机构:** University of Central Florida (PDF page 1).
- **Venue / 会议:** **CVPR 2026** — "Accepted at Workshop on Computer Vision for Children (CV4CHL) at CVPR 2026 (Non-Proceeding Track)" (published 2026-11-18)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Children's book illustrations carry developmental/pedagogical/cultural responsibilities (Indonesia's Book Leveling Guideline — government-issued, four reading levels); AI evaluators/generators entering children's publishing must "reliably meet the structural, safety, and cultural standards."
  - **Methodology:** Evaluates open-source VLMs on real Indonesian children's books via VLM assessment of guideline compliance, safety, and cultural alignment.
  - **Key innovations:** first cross-level (4 reading levels) VLM audit of Indonesian children's book illustrations (guideline compliance + safety + cultural alignment).
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.23887) · [PDF](https://arxiv.org/pdf/2611.23887v1)

### 7.2 EfficientVPR: Toward Efficient Visual Place Recognition via Scene-Aware Prompt Tuning and Adaptive Feature Enhancement
**EfficientVPR：基于场景感知提示微调与自适应特征增强的高效视觉地点识别**

- **Authors / 作者:** Wenjing Tang, Chuanguang Yang, Zhulin An, Libo Huang
- **Affiliation / 机构:** 1State Key Laboratory of AI Safety, Institute of Computing Technology, Chinese Academy of Sciences (PDF page 1; others).
- **Venue / 会议:** **CVPR 2026** — "18 pages, 11 figures, accepted at CVPR 2026" (published 2026-11-17)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** VPR faces critical challenges: extreme environmental variation + computational constraints of practical applications; methods scale capacity or use reranking stages — significant efficiency bottleneck.
  - **Methodology:** **EfficientVPR** — a lightweight one-stage framework achieving speed-accuracy trade-offs via two innovations: (i) a scene-aware visual prompt tuning method adapting pretrained features with fewer parameters, dynamically adjusting to sample-specific characteristics; (ii) adaptive feature enhancement ... (truncated).
  - **Key innovations:** scene-aware visual prompt tuning + adaptive feature enhancement for efficient VPR.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22506) · [PDF](https://arxiv.org/pdf/2611.22506v1)

### 7.3 ASCG: Adaptive Spatial Classifier Guidance for Surgical Concept Suppression in Diffusion Models
**ASCG：用于生成式模型中手术概念抑制的自适应空间分类器引导**

- **Authors / 作者:** Younghwan Kil, Joonhyeong Park, Giung Nam, Juho Lee
- **Affiliation / 机构:**affiliation on PDF page 1: see PDF (O lines show see-note); see PDF).
- **Venue / 会议:** **CVPR 2026** — "Accepted at the CVPR 2026 Workshop on Synthetic & Adversarial Forensics (SAFE). 9 pages, including references" (published 2026-11-16)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** T2I diffusion models produce harmful content; existing safety mechanisms rely on indiscriminate global interventions → semantic drift and quality degradation.
  - **Methodology:** **Adaptive Spatial Classifier Guidance (ASCG)** — necessity-driven framework that activates guidance selectively upon harm detection via probabilistic monitoring; leverages Grad-CAM for localized suppression, preserving semantic fidelity better than conventional global metrics.
  - **Key innovations:** localized, harm-triggered concept suppression (Grad-CAM-based) vs global interventions.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20625) · [PDF](https://arxiv.org/pdf/2611.20625v1)

### 7.4 Bootstrap Your Own AV-Proxies: Adaptive Contrastive and Prototype Learning for Audio-Visual Segmentation
**自举自己的 AV 代理：用于音视频分割的自适应对比与原型学习**

- **Authors / 作者:** Junbo Zhang, Hang Su, Zhaofan Li, Hang Dong
- **Affiliation / 机构:** 1School of Computer Science, Wuhan University; 2Academy of Advanced Interdisciplinary Studies, Wuhan University; Chao Sun† (PDF page 1).
- **Venue / 会议:** **CVPR 2026** — "Accepted to CVPR 2026" (published 2026-11-06)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Audio-Visual Segmentation (AVS): segment sounding objects in video frames using audio-visual correspondence; challenge: semantic incompleteness within a single modality + semantic gap between audio/visual.
  - **Methodology:** Novel adaptive contrastive + prototype learning framework **BYOAVP**; handles audio-visual correlation; "Specifically..." (truncated).
  - **Key innovations:** BYOAVP — adaptive contrastive and prototype learning for AVS.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.09191) · [PDF](https://arxiv.org/pdf/2611.09191v1)

### 7.5 Align Once to Explain: Feature Alignment for Scalable B-cosification of Foundational Vision Transformers
**一次对齐即可解释：基础 ViT 的 B-cos 化可扩展特征对齐**

- **Authors / 作者:** Raphael Maser, Siddhartha Gairola, Sukrut Rao, Bernt Schiele
- **Affiliation / 机构:** Max Planck Institute for Informatics, Saarland Informatics Campus, Saarbrücken, Germany (PDF page 1).
- **Venue / 会议:** **CVPR 2026** — "CVPR 2026. 29 pages incl. appendix..." (published 2026-11-02)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Foundational VMs are opaque and hard to interpret; B-cos methods need feature alignment (usually trained or expensive).
  - **Methodology:** **ALOE** — one-time, label-free feature alignment that converts foundational VMs into inherently interpretable B-cos variants; once aligned, the B-cos backbone is a drop-in replacement across downstream tasks, amortizing interpretability cost; robust across pre-training paradigms.
  - **Key innovations:** ALOE — label-free one-time feature alignment for scalable B-cosification of ViTs.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.03438) · [PDF](https://arxiv.org/pdf/2611.03438v1)

---

## 8. ACL 2026

### 8.1 What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution
**偏差头到底测量什么？头级偏差归因的可识别性问题**

- **Authors / 作者:** S. M Seefat Alam
- **Affiliation / 机构:** Bangladesh University of Engineering and Technology, Dhaka.
- **Venue / 会议:** **ACL Rolling Review (October 2026 cycle)** — "18 pages, 13 tables. Under review at ACL Rolling Review (October 2026 cycle)" (published 2026-11-17)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Head-level bias attribution is validated only by fairness-metric effects, never by evidence that the statistic selecting the heads measures bias; biases are non-identifiable via effects alone.
  - **Methodology:** Audit on Qwen-2.5-7B-Instruct and Llama-3.1-8B-Instruct: head map correlates at ρ= −0.950 and −0.768 with a label-blind response-length map (apparent surface confound); intervention breaking length-label coupling: response length explains 1% of the statistic's variance; prompt identity explains 64%.
  - **Key innovations:** audit via intervention (breaks length-label coupling) — exposes bias statistics that measure response length, not bias.
- **Experimental results / 结果：** Head map ≈ response length (ρ≈−0.95); after intervention: response length 1% variance vs prompt identity 64%; LM action doesn't vary with state in 10/38 cells.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.23218) · [PDF](https://arxiv.org/pdf/2611.23218v1)

### 8.2 A Generative AI-Driven Architecture for Whole-Home Intelligent Services: Edge Models, Memory Management, and Household Applications
**全屋智能服务的生成式 AI 驱动架构：边缘模型、内存管理与家庭应用**

- **Authors / 作者:** Mo Zhou
- **Affiliation / 机构:** Nanjing Normal University.
- **Venue / 会议:** **ACL 2026** — "31 pages, 3 figures, 2 tables" (published 2026-11-16)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Cloud assistants in smart homes face governance limitations (data transmission, availability, physical action reliability).
  - **Methodology:** Uses the home local server as a unifying axis; design-oriented review; sources (arXiv, CNKI, ACL Anthology, official docs — searched Nov 2026) coded into five evidence categories (reviews, prototypes, benchmarks, HCI/eldercare, official docs).
  - **Key innovations:** design-oriented review framework of generative AI in smart homes.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21232) · [PDF](https://arxiv.org/pdf/2611.21232v1)

### 8.3 Do We Still Need Fine-Tuned Classifiers? Swapping Typed Decision Models into 24 ACL-Venue Papers
**我们仍然需要微调分类器吗？把类型化决策模型换入 24 篇 ACL 会刊论文**

- **Authors / 作者:** Marek Šuppa, Jaroslav Kopčan
- **Affiliation / 机构:** Comenius University in Bratislava; Kempelen Institute of Artificial Intelligence and Center for Advanced AI (truncated PDF page 1).
- **Venue / 会议:** **ACL Rolling Review** — "Typed Decision Models such as TypeSafe's Jev..." (published 2026-11-15)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Typed Decision Models (Jev, System 1) answer typed questions with a probability per option, no training; many NLP papers still fine-tune task-specific classifiers; prompted LLMs trail such classifiers on most text classification benchmarks.
  - **Methodology:** Swaps predictors of 24 ACL-venue papers for Jev, keeping each paper's splits/metric/labels; validates with Cloudflare's Clef, Microsoft-Decision-1 and OpenAI's...
  - **Key innovations:** quantifies how many fine-tuned classifiers a Typed Decision Model can replace under each paper's own evaluation.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.20191) · [PDF](https://arxiv.org/pdf/2611.20191v1)

### 8.4 Revisiting What Makes a Good Context Subset: A Sparse Latent Basis Perspective
**重新审视好的上下文子集有什么：稀疏潜在基视角**

- **Authors / 作者:** Cen-Jhih Li, Siddhant Chaudhary, Aditya Bhaskara
- **Affiliation / 机构:** Kahlert School of Computing; University of Utah (PDF page 1).
- **Venue / 会议:** **ACL 2026** — "17 pages, 2 figures. The format of ACL rolling review" (published 2026-11-14)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Selecting context subsets for LLM inference — what makes a subset effective remains unclear; studied in few-shot demonstration selection.
  - **Methodology:** Hypothesis: demonstrations should collectively provide task-relevant info needed by the target query; assumes query representation is a useful proxy; formulates selection as sparse reconstruction instantiated with **Residual Explanation Search (RES)**, a Matching-Pursuit-style diagnostic.
  - **Key innovations:** RES vs MMR across 7 benchmarks / 8 open-weight LLMs.
- **Experimental results / 结果：** RES outperforms MMR in 34/... (truncated).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19220) · [PDF](https://arxiv.org/pdf/2611.19220v1)

### 8.5 Beyond Controllability: Speaker Diversity in Instruction-Guided Text-to-Speech
**超越可控性：指令式文本转语音中的说话人多样性**

- **Authors / 作者:** Yi-Cheng Lin, Jia-Kai Dong, Kuan-Yu Chen, Szu-Chi Chen
- **Affiliation / 机构:** National Taiwan University; 2NVIDIA; 3Artificial Intelligence Center of Research Excellence, National Taiwan University (PDF page 1).
- **Venue / 会议:** **ACL ARR 2026** — "Submitted to ACL ARR 2026" (published 2026-11-14)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** ITTS lets users specify voice properties by natural language; applications need diverse voices when the same category is requested repeatedly; no prior work audits whether outputs are in fact diverse (vs real speech or across attribute values).
  - **Methodology:** Evaluates seven open-source ITTS systems using speaker embeddings whose capacity we independently validate (7 speaker embeddings).
  - **Key innovations:** speaker-diversity audit of ITTS systems.
- **Experimental results / 结果：** Every system produces speaker distributions markedly narrower than real speech; female prompts produce less diverse voice po[ols].
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19030) · [PDF](https://arxiv.org/pdf/2611.19030v1)

---

## 9. EMNLP 2025

### 9.1 Refined Assessment for Translation Evaluation: Rethinking Machine Translation Evaluation in the Era of Human-Level Systems
**人类水平系统时代下机器翻译评估的再思考**

- **Authors / 作者:** Dmitry Popov, Vladislav Negodin, Ekaterina Enikeeva, Iana Matrosova
- **Affiliation / 机构:** Not stated on PDF page 1 (truncated "♣" abstract-level attributions — see PDF).
- **Venue / 会议:** **EMNLP 2025 Findings** — "Published in Findings of EMNLP 2025. 17 pages. Dataset: https://huggingface.co/datasets/yandex/wmt24-en-ru-rat..." (published 2026-10-24)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** MT systems approach human-level quality; traditional evaluation methods (MQM, ESA) have limitations: inconsistencies from variable annotator expertise, excessive categorization complexity, coarse severity granularity, accuracy bias over fluency, time constraints.
  - **Methodology:** Introduces a high-quality dataset of human evaluations for WMT24 English-Russian from professional linguists; expert assessments without time pressure yield substantially different results from standard evaluations.
  - **Key innovations:** professional-linguist evaluation dataset (WMT24-EN-RU) + analysis of MQM/ESA limitations.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.33749) · [PDF](https://arxiv.org/pdf/2610.33749v1)

### 9.2 Is the ACL Responsible NLP Checklist a Box-Ticking Exercise? A Large-Scale Analysis of EMNLP 2025
**ACL Responsible NLP 清单是否流于形式？EMNLP 2025 的大规模分析**

- **Authors / 作者:** Nusrath Jinnath, Wei Zhao
- **Affiliation / 机构:** The Aberdeen NLP Research Group, University of Aberdeen.
- **Venue / 会议:** **EMNLP 2025** (published 2026-08-10)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Responsible NLP practice includes transparency, ethics, societal impacts; the ACL Responsible NLP Checklist aims to push these goals.
  - **Methodology:** Curates and releases the first two datasets of EMNLP 2025 Main + Findings checklist responses/justifications (**73,922 responses**) and checklist reference linking; provides the first analysis of recent EMNLP Checklists.
  - **Key innovations:** first releases of checklist response/justification datasets + linkage, from 73,922 responses.
- **Experimental results / 结果：** For the Main track, authors isolate ethics questions of the Checklist f[rom business/performance]... (truncated).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2608.09280) · [PDF](https://arxiv.org/pdf/2608.09280v1)

### 9.3 Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration
**通过人类 LLM 协作构建可扩展、文化特定的刻板印象数据集**

- **Authors / 作者:** Weicheng Ma, John Guerrerio, Soroush Vosoughi
- **Affiliation / 机构:** College of Computing, Georgia Institute of Technology; Computer Science Department, Dartmouth College (PDF page 1).
- **Venue / 会议:** **EMNLP 2025 Main** — "published in EMNLP 2025 Main" (published 2026-07-08)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Research on stereotypes in LLMs focused on English-speaking contexts due to lack of datasets in other languages and high cost of manual annotation in underrepresented cultures.
  - **Methodology:** Introduces a cost-efficient human-LLM collaborative annotation framework; applies it to construct **EspanStereo**, a Spanish-language stereotype dataset spanning multiple Spanish-speaking countries across Europe and Latin America; captures well-documented stereotypes + culturally specific biases absent from English-centric resources; LLMs generate candidates, in-culture annotators validate.
  - **Key innovations:** EspanStereo — multi-country Spanish stereotype dataset (human-LLM collaborative).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2607.07895) · [PDF](https://arxiv.org/pdf/2607.07895v1)

### 9.4 Optimising Factual Consistency in Summarisation via Preference Learning from Multiple Imperfect Metrics
**通过来自多个不完美指标的偏好学习优化摘要中的事实一致性**

- **Authors / 作者:** Yuxuan Ye, Raul Santos-Rodriguez, Edwin Simpson
- **Affiliation / 机构:** Intelligent System Laboratory, University of Bristol.
- **Venue / 会议:** **EMNLP 2025 Findings** (published 2026-05-26)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Existing factuality metrics remain underdeveloped, limiting their effectiveness as signals for shaping model behavior; individual metrics are unreliable, but their combination can capture diverse factual errors.
  - **Methodology:** An automated training pipeline that improves factual consistency in summaries by aggregating scores from different weak metrics; maps scores to preferences and filters out cases ...
  - **Key innovations:** preference-learning pipeline over multiple weak factuality metrics (avoids complex reward shaping).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2605.26840) · [PDF](https://arxiv.org/pdf/2605.26840v1)

### 9.5 QEVA: A Reference-Free Evaluation Metric for Narrative Video Summarization with Multimodal Question Answering
**QEVA：基于多模态问答的参考自由叙事视频摘要评估指标**

- **Authors / 作者:** Woojun Jung, Junyeong Kim
- **Affiliation / 机构:** Department of Artificial Intelligence, Chung-Ang University (PDF page 1).
- **Venue / 会议:** **EMNLP 2025 Findings** — "Accepted to Findings of EMNLP 2025" (published 2026-04-27)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Video-to-text summarization evaluation is underdeveloped; traditional n-gram metrics and recent LLM-based metrics depend on human-written references, limiting practicality and sensitivity to semantic aspects.
  - **Methodology:** **QEVA** — reference-free metric evaluating candidate summaries against source videos through multimodal question answering; assesses Coverage, Factuality, Chronology; introduces **MLVU(VS)-Eval**, a new annotated benchmark derived from the MLVU dataset (800 summaries from 200...).
  - **Key innovations:** QEVA — multimodal-QA-based reference-free metric for narrative video summarization + MLVU(VS)-Eval benchmark.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2604.24052) · [PDF](https://arxiv.org/pdf/2604.24052v1)

---

## 10. SIGIR 2026

### 10.1 StaRSE: Compact Russian Sentence Embeddings with a Sign-Coded Static Encoder
**StaRSE：基于符号编码静态编码器的紧凑俄语句子向量**

- **Authors / 作者:** Boris Malashenko, Ivan Jarsky, Egor Soldatov, Vladislav Luzhnov
- **Affiliation / 机构:** ITMO University, Saint Petersburg, Russia (PDF page 1).
- **Venue / 会议:** **ReNeuIR @ SIGIR 2026** — "Accepted to ReNeuIR @ SIGIR 2026. 16 pages" (published 2026-11-10)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Transformer sentence encoders give strong retrieval quality, but inference cost on CPUs / frequent refresh becomes a bottleneck.
  - **Methodology:** **StaRSE** — compact static sentence encoder: token directions stored as sign bits, token norms stored separately, sentences encoded by mean pooling over norm-scaled sign directions; initialized from ruBERT-base; fine-tuned on Russian adjacent-sentence + task-shaped pairs; post-trained with contrastive stage optimizing the sign-projected token table.
  - **Key innovations:** StaRSE — CPU-friendly compact Russian sentence encoder (sign-coded + norm table).
- **Experimental results / 结果：** On RuMTEB, StaRSE reaches a task mean of **51.16** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.14236) · [PDF](https://arxiv.org/pdf/2611.14236v1)

### 10.2 Collaborative Search Meets Large Language Models: An Empirical Study
**协同搜索遇见大语言模型：实证研究**

- **Authors / 作者:** Peiyuan Gong, Jiamian Li, Erhan Zhang, Fengming Liang
- **Affiliation / 机构:** GSAI, Renmin University of China.
- **Venue / 会议:** **SIGIR-AP 2026** — "Accepted by SIGIR-AP 2026" (published 2026-11-03)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLMs enable autonomous agents to support collaborative information seeking within shared communication spaces; little is known about how these agents shape search experiences, behaviors, outcomes vs conventional tools.
  - **Methodology:** User study with 80 students in 40 pairs, four collaborative search tasks under four scenarios: QAAgent (LLM parametric knowledge), CoSearchAgent (multi-user conversational context, reformulate queries, retrieve, generate source...); outcomes vs conventional search tools.
  - **Key innovations:** empirical comparison of QAAgent vs CoSearchAgent in collaborative search.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.04619) · [PDF](https://arxiv.org/pdf/2611.04619v1)

### 10.3 Auditing a Model-Hub Benchmark: Data Quality, Training Budgets, and Side Information in HuggingBench
**审计模型库基准：HuggingBench 的数据质量、训练预算与旁信息**

- **Authors / 作者:** Michal Podstawski
- **Affiliation / 机构:** NASK National Research Institute.
- **Venue / 会议:** **SIGIR 2025** (benchmark being audited) — "12 pages, 10 tables, 2 figures. Code and data: https://doi.org/10.5281/zenodo.23857277" (published 2026-11-01)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Benchmarks built from model hubs combine interaction data, KGs and resource docs; valid files don't guarantee the artifacts describe the same objects.
  - **Methodology:** Audit of HuggingBench (SIGIR 2025 — HF resource-recommendation benchmark) via data validation + replication of 11 recommendation methods + controlled experiments (3 seeds); replicating its four external KGs.
  - **Key innovations:** item-entity identity constraint violation analysis of HuggingBench KGs; correcting the join improves every KG-based method on every seed, by up to **73% in mean Recall@10**.
- **Experimental results / 结果：** Joining valid files → item-entity identity violations in 3 of 4 external KGs; up to 73% mean Recall@10 gains after join correction.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.03727) · [PDF](https://arxiv.org/pdf/2611.03727v1)

### 10.4 TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge
**TaskBridge：SIGIR 2026 电商挑战赛技术报告**

- **Authors / 作者:** Zhiheng Fu, Yupeng Hu, Zixu Li, Zhiwei Chen
- **Affiliation / 机构:** 1Shandong University, 2Harbin Institute of Technology (Shenzhen), 3City University of Hong Kong, 4Southeast University (PDF page 1).
- **Venue / 会议:** **SIGIR 2026 eCommerce Challenge** — "Technical Report on the First-Place Solution for eCommerce Challenge @ SIGIR 2026 eCom Workshop" (published 2026-10-27)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Query Reformulation Task: reformulating task-oriented queries into product-retrieval expressions; activity-level semantics create a lexical gap with catalog descriptions; systems must preserve task intent while adapting reformulation count (Automatic/Interactive protocols).
  - **Methodology:** **TaskBridge** — Catalog Semantic Anchoring; Unified Five-Candidate Rewriting; Protocol-Aware Selection.
  - **Key innovations:** catalog-anchored query reformulation framework (5 candidates + protocol-aware selection).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.37231) · [PDF](https://arxiv.org/pdf/2610.37231v1)

### 10.5 Evaluating Visual Language Models on Visual Grounding for Visually Impaired People
**评估视觉语言模型在视障人群视觉定位任务上的表现**

- **Authors / 作者:** Fairooz Azim, Lydia Achour, Claudia Borg, Lina Rojas-Barahona
- **Affiliation / 机构:** Orange Research; University of Malta, Msida, Malta; University of Malta (PDF page 1).
- **Venue / 会议:** **EvalMG26 @ SIGIR 2026** — "Published at the second workshop on evaluation for multimodal generation EvalMG26 @ SIGIR 2026. July 24th 2026" (published 2026-10-21)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Visual grounding in VQA is a fundamental VLM capability; applied to assistive scenarios (VIP) it is a trust/safety requirement ("not merely a technical feature, but a trust and safety requirement").
  - **Methodology:** Assess open-source VLMs on visual grounding using the **VizWiz-VQA-Grounding dataset and challenge** (real-life conditions; contains real-life...).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.33078) · [PDF](https://arxiv.org/pdf/2610.33078v1)

---

## 11. WWW 2026

### 11.1 GALACTIC CENTERS AS TRACERS OF GALAXY EVOLUTION: Zooming from galaxy large-scale properties into their central massive black holes
**星系中心作为星系演化的追踪器：从星系尺度性质到中心超大黑洞的放大**

- **Authors / 作者:** F. Pinna, N. Hoyer, S. Thater, A. Mastrobuono Battisti
- **Affiliation / 机构:** Leiden University / Center for Astrophysics, Netherlands (see PDF; affiliations truncated on PDF page 1).
- **Venue / 会议:** **WWW 2026** — "29 pages, 4 figures; white paper as proceedings of the workshop 'Galactic Centers as tracers of galaxy evolution'..." (published 2026-11-02)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** How do galactic central regions (MBHs, nuclear structures) connect to global galaxy evolution?
  - **Methodology:** White paper (workshop proceedings); gathered research communities to reveal connection channels between central massive black holes (MBHs), nuclear structures, and global evolutionary processes (gas inflows/outflows, interactions); MBH seeding/formation/growth; AGN feedback; nuclear stellar structure formation.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.03090) · [PDF](https://arxiv.org/pdf/2611.03090v1)

### 11.2 CIVER: Causal Intervention Verification for Reliable Code Review
**CIVER：可靠代码审查的因果干预验证**

- **Authors / 作者:** Xinyuan Song, Hasibul Haque, Jay Somasundaram, Ryan Turner
- **Affiliation / 机构:** Affiliation not stated on PDF page 1 (see PDF).
- **Venue / 会议:** **WWW 2026** (published 2026-10-26)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLM-based coding agents generate code; LLM reviewers evaluate contributions, but reviews contain false positives or lack sufficient evidence; unreliable reviews mislead developers/coding agents.
  - **Methodology:** **CIVER** — causal intervention verification framework; rejects unreliable reviews by intervening on claims that introduce new facts/specifications (truncated).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.36010) · [PDF](https://arxiv.org/pdf/2610.36010v1)

### 11.3 The Anatomy of Address Poisoning on Ethereum: Funding Mechanisms, Scam Signatures, and Laundering via Tornado Cash
**以太坊地址投毒剖析：诈骗资金路径、签名与 Tornado Cash 洗钱通道**

- **Authors / 作者:** Son Hoang Dau, Thanh Nguyen, Phuong Duy Huynh, Hong Yen Tran
- **Affiliation / 机构:** RMIT University.
- **Venue / 会议:** **WWW 2026** (published 2026-09-20)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Address-Poisoning Transfer (APT) — phishing scam poisoning the victim's address book with lookalike addresses (cost users millions).
  - **Methodology:** Beyond detection: investigates three underexplored aspects — scam funding mechanisms, scam signatures, scam-proceeds laundering via public services (in particular Tornado Cash); pool of analogies (Yeet al. WWW'24, Guan-Li CCS'24, Chen et al. NDSS'25, Tsuchiya et al. USENIX'25).
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2609.23405) · [PDF](https://arxiv.org/pdf/2609.23405v1)

### 11.4 Are Unreachable Nodes Truly Safe? Fully Eclipsing Monero's P2P Network!
**Monero P2P 网络是否真的安全？对不可达节点的全面日食攻击！**

- **Authors / 作者:** Ruisheng Shi, Jiaqi Zeng, Lina Lan, Shihan Zhang
- **Affiliation / 机构:** 1Beijing University of Posts and Telecommunications; 3Zhejiang University; 2Hong Kong Polytechnic University; 4CSIRO (PDF page 1).
- **Venue / 会议:** **CCS'26** — "Accepted by ACM CCS'26 (The Hague, The Netherlands)" (published 2026-09-09)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Eclipse attacks isolate blockchain nodes by monopolizing inbound connections; existing Monero/Bitcoin/Ethereum attacks assume inbound connectivity, excluding NAT-behind unreachable nodes — believed "safe."
  - **Methodology:** Challenge: unreachability does NOT imply resilience; first eclipse attack tailored to unreachable Monero nodes — requires no inbound access; poisons peer addresses via self-confirming GET_DATA responses.
- **Experimental results / 结果：** (author-reported; see PDF — state-machine manipulation described).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2609.10260) · [PDF](https://arxiv.org/pdf/2609.10260v1)

### 11.5 Cluster Deletion is as Hard to Approximate as Vertex Cover
**集簇删除与顶点覆盖一样难近似**

- **Authors / 作者:** Yixin Cao, Ying Xu
- **Affiliation / 机构:** Department of Computing, Hong Kong Polytechnic University, Hong Kong, China (PDF page 1).
- **Venue / 会议:** (preprint; WWW 2026 era) — no venue comment.
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Recent Cluster Editing breakthroughs motivated better-than-2 approximations for Cluster Deletion.
  - **Methodology:** Rules out better-than-2 approximations under the Unique Games Conjecture: NP-hard to approximate within a factor of 2−ε for every fixed ε>0, matching the known 2-approximation [Veldt et al., WWW 2018]; NP-hardness of approximation within √2−ε via reduction from Vertex Cover; restricted settings admit better-than-2 approximations.
  - **Key innovations:** UGC-based hardness result for Cluster Deletion + reduction to Vertex Cover.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2608.04883) · [PDF](https://arxiv.org/pdf/2608.04883v1)

---

## 12. CIKM 2025

### 12.1 Data-centric Prompt Tuning for Dynamic Graphs
**面向动态图的数据中心化提示微调**

- **Authors / 作者:** Yufei Peng, Cheng Yang, Zhengjie Fan, Chuan Shi
- **Affiliation / 机构:** Beijing University of Posts and Telecommunications; Tsinghua University (PDF page 1).
- **Venue / 会议:** **CIKM 2025** (published 2026-01-17)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Dynamic graphs attract increasing attention (complex evolving relationships); traditional approaches pre-train via dynamic link prediction and apply to tasks — performance degrades under few-shot settings (strong coupling between prompt and architecture).
  - **Methodology:** Data-centric prompt tuning for dynamic graphs — treats prompts as "prompt tokens" (the [method is not yet visible in excerpt] — see PDF).
  - **Links / 链接:** [arXiv](https://arxiv.org/abs/2601.11954) · [PDF](https://arxiv.org/pdf/2601.11954v1)

### 12.2 Query, Decompose, Compress: Structured Query Expansion for Efficient Multi-Hop Retrieval
**查询、分解、压缩：高效多跳检索的结构化查询扩展**

- **Authors / 作者:** JungMin Yun, YoungBin Kim
- **Affiliation / 机构:** Chung-Ang University (PDF page 1).
- **Venue / 会议:** **CIKM 2025** — "Accepted to CIKM 2025" (published 2026-01-14)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLMs increasingly used for query expansion, but generative nature introduces irrelevant/noisy info, degrading complex multi-hop retrieval.
  - **Methodology:** **DeCoR** (Decompose and Compress for Retrieval) — a framework grounded in structured information refinement: rather than generating additional content, DeCoR restructures the query's reasoning and distills supporting evidence; two components for multi-hop: Query Decomposition (decompose complex queries into exp[eras]) and...
  - **Key innovations:** DeCoR — decompose+compress retrieval framework for multi-hop queries.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2603.21024) · [PDF](https://arxiv.org/pdf/2603.21024v1)

### 12.3 From Forecast to Action: Uncertainty-Aware UAV Deployment for Ocean Drifter Recovery
**从预测到行动：用于海洋漂流物恢复的不确定性感知无人机部署**

- **Authors / 作者:** Jingeun Kim, Yong-Hyuk Kim, Yourim Yoon
- **Affiliation / 机构:** Gachon University; Kwangwoon University (PDF page 1).
- **Venue / 会议:** **CIKM 2025 STIntelligence Workshop** — "This paper has been accepted by CIKM 2025 STIntelligence Workshop" (published 2025-12-10)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Novel predict-then-optimize framework for maritime search operations integrating trajectory forecasting with UAV deployment optimization.
  - **Methodology:** A large language model predicts the drifter's trajectory; spatial uncertainty modeled using Gaussian-based particle sampling; dynamically adapt UAV detection radii based on distance; optimize placement using meta-heuristic algorithms. Experiments on real-world Korean coastline data — "our method, particularly the repair mechanism designed for this problem, significantly outperforms the random search ba[seline]".
  - **Key innovations:** LLM-based trajectory prediction + adaptive UAV placement optimization.
- **Experimental results / 结果：** Outperforms the random-search baseline (author-reported).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.09260) · [PDF](https://arxiv.org/pdf/2512.09260v1)

### 12.4 Spatio-Temporal Trajectory Foundation Model - Recent Advances and Future Directions
**时空轨迹基础模型 —— 近期进展与未来方向（评估综述）**

- **Authors / 作者:** Sean Bin Yang, Ying Sun, Yunyao Cheng, Yan Lin
- **Affiliation / 机构:** 1Aalborg University; 2Chongqing University of Posts and Telecomunications; 3East China Normal University; Kristian Torp, Jilin Hu (PDF page 1).
- **Venue / 会议:** **CIKM 2025 STIntelligence Workshop** — "This paper has been accepted by CIKM 2025 STIntelligence Workshop" (published 2025-11-25)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** FMs enable a diverse range of data analytics/knowledge discovery across scientific fields; spatio-temporal foundation models (STFMs) to improve adaptability/generalization across the spectrum of ST tasks; "Despite rapid progress, a systematic investigation of trajectory foundation models (TFMs), a crucial subclass of STFMs, is largely lacking."
  - **Methodology:** Comprehensive tutorial/survey of recent advances in TFMs, including taxonomy of methodologies and [a ... overview].
  - **Key innovations:** comprehensive tutorial/survey of trajectory foundation models.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2511.20729) · [PDF](https://arxiv.org/pdf/2511.20729v1)

### 12.5 SupLID: Geometrical Guidance for Out-of-Distribution Detection in Semantic Segmentation
**SupLID：语义分割中基于几何引导的分布外检测**

- **Authors / 作者:** Nimeshika Udayangani, Sarah Erfani, Christopher Leckie
- **Affiliation / 机构:** The University of Melbourne.
- **Venue / 会议:** **CIKM 2025** — "10 pages, CIKM 2025" (published 2025-11-24)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** OOD detection in semantic segmentation localizes anomalous regions at the pixel level; classifier-derived confidence scores (energy/entropy, image-level OOD methods adapted to pixel-precise tasks) inherit limitations including vulnerability to overconfidence.
  - **Methodology:** **SupLID** — novel framework guiding classifier-derived OOD scores by exploiting the geometrical structure of the... (truncated).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2511.18816) · [PDF](https://arxiv.org/pdf/2511.18816v1)

---

## 13. RecSys 2025

### 13.1 Data Quality Challenges in Multimodal Tourism Recommender Systems
**旅游推荐中多模态数据质量挑战**

- **Authors / 作者:** Zehui Wang, Wolfram Höpken, Dietmar Jannach
- **Affiliation / 机构:** Affiliation not fully stated on PDF page 1 (authors: Zehui Wang1,2*, Wolfram Höpken 1, Dietmar Jannach 2 — see PDF).
- **Venue / 会议:** **DaQuaMRec Workshop @ ACM RecSys 2025** — "4 pages. Presented at the DaQuaMRec Workshop, co-located with ACM RecSys 2025" (published 2026-11-10)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** R&S increasingly considers diverse data modalities (social media data), but the quality of multimodal data has received limited attention.
  - **Methodology:** Focusing on tourism recommendation, examines real-world challenges using datasets from Yelp and Instagram; issues include noise from fake reviews, hallucinated content from LLMs, modality contradictions, demographic bias; future directions: quality-aware fusion, structured/controlled LLM-based content generation, user group differentiation.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.13972) · [PDF](https://arxiv.org/pdf/2611.13972v1)

### 13.2 FinTRec: Transformer Based Unified Contextual Ads Targeting and Personalization for Financial Applications
**FinTRec：面向金融应用的基于 Transformer 的统一上下文广告定向与个性化**

- **Authors / 作者:** Dwipam Katariya, Snehita Varma, Akshat Shreemali, Benjamin Wu
- **Affiliation / 机构:** See PDF page 1 (one author "Contributed to the study when at Capital One. Now at NVIDIA"; modeling references not reflective of actual activities — see PDF).
- **Venue / 会议:** **CARS @ RecSys 2025** — "10 pages, 7 figures, Accepted at CARS @ RecSys 2025" (published 2025-11-18)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Transformer architectures widely adopted in sequential recommendation, yet FS presents distinct practical/modeling challenges for real-time recommendation: (a) long-range user interactions (implicit/explicit) across digital/physical channels; (b) multiple interrelated products (coordinated models, varied ad placements, personalized feeds); (c) balancing competing business goals.
  - **Methodology:** **FinTRec** — transformer-based framework addressing these challenges and operational objectives in FS (author-reported; PDF page 1).
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2511.14865) · [PDF](https://arxiv.org/pdf/2511.14865v1)

### 13.3 Civic Ground Truth in News Recommenders: A Method for Public Value Scoring
**新闻推荐中的市民标杆真值：一种公共价值打分方法**

- **Authors / 作者:** James Meese, Kyle Herbertson
- **Affiliation / 机构:** School of Media and Communication, RMIT University, Melbourne, Australia (both authors).
- **Venue / 会议:** **NORMalize 2025 Workshop @ RecSys 2025** — "Presented at NORMalize 2025: The Third Workshop on the Normative Design and Evaluation of Recommender Systems" (published 2025-10-26)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:**NRS normative goals (editorial, public service values) — prior efforts use expert input or audience feedback.
  - **Methodology:** Civic ground truth — embeds civic values into NRS through large-scale, structured audience evaluations; generates value-based labels via a nationally representative survey (generalisable across corpus); automated metadata encoding.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2510.22865) · [PDF](https://arxiv.org/pdf/2510.22865v1)

### 13.4 Improving Visual Recommendation on E-commerce Platforms Using Vision-Language Models
**利用视觉语言模型改进电商平台视觉推荐**

- **Authors / 作者:** Yuki Yada, Sho Akiyama, Ryo Watanabe, Yuta Ueno
- **Affiliation / 机构:** E-commerce platforms (Mercari — >20M monthly users, Japan; affiliations not fully stated on PDF page 1 — see PDF).
- **Venue / 会议:** **RecSys 2025 (Spotlight)** — "Accepted to ACM RecSys 2025 (Spotlight)" (published 2025-10-15)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Recommending visually similar products on large-scale e-commerce platforms; VLM demonstrated strong performance in image recognition/image-text retrieval.
  - **Methodology:** Fine-tunes SigLIP (sigmoid-based contrastive loss) using one million product image-title pairs from Mercari collected over three months; application of a VLM to product recommendations on Mercari.
- **Experimental results / 结果：** (author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2510.13359) · [PDF](https://arxiv.org/pdf/2510.13359v1)

### 13.5 On Inherited Popularity Bias in Cold-Start Item Recommendation
**冷启动物品推荐中的继承流行度偏差**

- **Authors / 作者:** Gregor Meehan, Johan Pauwels
- **Affiliation / 机构:** Queen Mary University of London.
- **Venue / 会议:** **RecSys 2025** — "Published at ACM RecSys 2025" (published 2025-10-13)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Cold-start: recommending unseen/'cold' items; cold-start systems can learn to replicate CF models' predictive biases (supervision from warm CF models).
  - **Methodology:** Shows cold-start systems can inherit popularity bias (overfitting to popular items) — a common cause of R&S unfairness — "W..." (truncated).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2510.11402) · [PDF](https://arxiv.org/pdf/2510.11402v1)

---

## 14. General — AI & LLMs

### 14.1 When Should a Voice Agent Speak? End-of-Turn Detection in Turkish
**语音代理何时发言？土耳其语言的结束语轮检测**

- **Authors / 作者:** Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Mustafa Sertaç Türkel, Nur Yağmur Tuncer
- **Affiliation / 机构:** see PDF page 1 (see PDF).
- **Summary / 概要:** A voice agent that waits for a fixed silence either interrupts users who pause mid-utterance or responds late to users who finished. Examines the decision at silence onset using turn ends and turn-internal pauses from the Real-TurnTurk corpus of Turkish dyadic video calls. Compares a fine-tuned Turkish TurnGPT model, a zero-shot Turkish LM, and a deployed multilingual detector with voice-activity timing and facial features under recording-disjoint and speaker-disjoint evaluation with paired cluster bootstrap tests; fine-tuned model separates turn ends from pauses better than baselines on held-out recordings. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25489) · [PDF](https://arxiv.org/pdf/2611.25489v1)

### 14.2 ToolPulse: Side-Channel Eavesdropping on Tool-Using LLM Agents
**ToolPulse：对使用工具的 LLM 代理进行旁路监听**

- **Authors / 作者:** Zihao Dan, Jinyu Zhang, Jinzhao Lian, Yun Chen
- **Affiliation / 机构:** HK, Renmin University of China, HKUST (GZ) (see PDF).
- **Summary / 概要:** Shows that remote inference remains a cache-based side channel when the victim's tools run on the user's machine and share system libraries — agentic execution is more practical than prior shared-hardware assumptions. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25470) · [PDF](https://arxiv.org/pdf/2611.25470v1)

### 14.3 ChronoDossier: Long-Form Personas as Temporal Memory Representations
**ChronoDossier：长期记忆表示为时间化人格档案**

- **Authors / 作者:** Noah Sturgill, Jinho D. Choi
- **Affiliation / 机构:** Emory University.
- **Summary / 概要:** Treats long-form persona dossiers as memory representations of a latent state: invariant identity + timeline of facts/routines/decision rules; constructs a benchmark of 311 synthetic dossiers of 1k–10k words written by seven generators from dated timelines; intrinsic metrics against intended states + extrinsic metrics testing recovery by five readers on a seeded 32-persona GPT-5.1 panel (Author-reported; see PDF).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25407) · [PDF](https://arxiv.org/pdf/2611.25407v1)

### 14.4 Falsifiable Compositional Reasoning in Time Series Forecasting
**时间序列预测中可验证的组合推理**

- **Authors / 作者:** Hao Xue
- **Affiliation / 机构:** HKUST, Guangzhou (see PDF).
- **Summary / 概要:** Models that rank best on historical validation often degrade across non-stationary regime transitions; argues the gap comes from using backtesting as an open-ended search objective vs. testing pre-specified compositional assumptions; under strong historical co-movement, chronological holdout error cannot separate invariant couplings among latent primitives. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25388) · [PDF](https://arxiv.org/pdf/2611.25388v1)

### 14.5 Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization
**超越权重更新：面向领域专业化的演化型代理工具组装**

- **Authors / 作者:** BoHao Chen
- **Affiliation / 机构:** Independent (see PDF).
- **Summary / 概要:** Domain specialization of LLM agents as RL/SFT weight-update problem; studies the complementary axis of evolving the agent *harness* (system prompt, tool schemas, skill library, planning scaffolding) with the policy frozen, casting harness evolution as an RL-style outer loop instantiated with GEPA (reflective evolutionary optimizer); experiments with Codev, a Claude Code-style coding agent, on SWE-bench Verified + others. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25380) · [PDF](https://arxiv.org/pdf/2611.25380v1)

### 14.6 Stop Going in Circles: Loop-Triggered Routing for System 1 Decision Agents
**停止原地打转：System 1 决策代理的环路触发路由**

- **Authors / 作者:** Zeming Yu, Huamin Ma, Yingyu Chen, Yuan Sun
- **Affiliation / 机构:** College of Computer Science, Sichuan University (see PDF).
- **Summary / 概要:** System 1 decision models (Jev) provide fast action selection, but agent integrations do not reliably translate local advantages; recurring state-action pairs signal stalled execution; proposes loop-triggered routing — LLM reasoning introduced when execution stalls; experiments on benchmarks. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25363) · [PDF](https://arxiv.org/pdf/2611.25363v1)

---

## 15. General — Recommendation Systems

### 15.1 Decision Boundaries Matter: Graph-Regularized Residual Adaptation for Cross-Domain Fake Image Detection
**决策边界很重要：跨域伪造图像检测的图正则残差自适应**

- **Authors / 作者:** Shichuang Xie, Qishuai Ding, Tong Qiao, Liquan Shen
- **Affiliation / 机构:** see PDF page 1 (Shanghai University; Hangzhou Dianzi University — see PDF).
- **Summary / 概要:** Analysis shows features from the frozen forensic encoder remain discriminative but the source-trained decision boundary does not fully exploit them; GraRA constructs a co[vering graph] of transferable directions and refines the boundary using only unlabeled target data. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25406) · [PDF](https://arxiv.org/pdf/2611.25406v1)

### 15.2 Intelligent Embedding Pruning for Large-Scale Recommendation Models
**大规模推荐模型的智能嵌入剪枝**

- **Authors / 作者:** Anish Khazane (Meta Research), Alex Saad-Falcon, Guanchu Wu, Marcio Porto
- **Affiliation / 机构:** Meta Research (see PDF); see also university co-authors (see PDF).
- **Summary / 概要:** In-training embedding pruning (ITEP) removes less important embedding rows during training (20–40% memory reduction) but sometimes degrades accuracy because per-table pruning ratios are set by size-based heuristics; uses feature importance (FI) to guide ratios (FI-ITEP). (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25288) · [PDF](https://arxiv.org/pdf/2611.25288v1)

### 15.3 Statistical, Machine Learning and Deep Learning Methods for Missing Covariates: An Empirical Evaluation with Applications to Alzheimer's Disease Research
**缺失协变量的统计、机器与深度学习方法：阿尔茨海默病研究的实证评估**

- **Authors / 作者:** Yiqing Pan, Sharon X. Xie, Shujie Ma, Angela L. Jefferson
- **Affiliation / 机构:** see PDF page 1 (Vanderbilt University Medical Center; University of ... — see PDF).
- **Summary / 概要:** Empirical evaluation of eight missing-data methods (complete-case, multiple imputation, ML-based, DL frameworks like MLPs and variational autoen...) in biomedical settings where covariates are costly to measure. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25219) · [PDF](https://arxiv.org/pdf/2611.25219v1)

### 15.4 A Modified Quasi-Newton Method for Unconstrained Optimization with Nonpositive Curvature Detection and Structured Complexity
**具有非正曲率检测与结构复杂度的改进拟牛顿法**

- **Authors / 作者:** Farhad Rahbarnia, Dominique Monnet, Dominique Orban
- **Affiliation / 机构:** GERAD and Department of Mathematics and Industrial Engineering, Polytechnique Montréal (see PDF).
- **Summary / 概要:** R2N computes a step that approximately minimizes a quadratic model with adaptive regularization; features step-computation strategies (sparse factorization, matrix-free Krylov methods); detects nonpositive curvature directions that are explo...
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25133) · [PDF](https://arxiv.org/pdf/2611.25133v1)

### 15.5 Consistent interfacial flow numerics - Part I: The gravity force term
**界面流体数值方法第一部分：重力项**

- **Authors / 作者:** Johan Roenby, Konstantinos Missios, Kasper Møller, Sithik Aliyar
- **Affiliation / 机构:** see PDF page 1 (Roskilde University; Technical University of Denmark; DLR German Aerospace Center, Bremen — see PDF).
- **Summary / 概要:** Revisits the gravity term in interFoam-style VOF solvers — acts only at the interface, depends on the local density jump (~1000× between phases); continuity corrections for sharp interface advection. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.24841) · [PDF](https://arxiv.org/pdf/2611.24841v1)

---

## 16. General — Advertising

### 16.1 FPGA-GEN: Target-Aware RTL Generation via HLS
**FPGA-GEN：基于 HLS 的面向目标的 RTL 生成**

- **Authors / 作者:** Luke Ztz Hu, Zhihan Xiao, Zhe Zhao, John Imoleayo Adebisi
- **Affiliation / 机构:** 1Shenzhen International Graduate School, Tsinghua University; others (see PDF).
- **Summary / 概要:** Agentic HLS-C generation workflow (FPGA-GEN) — specification, readiness, selection, repair, admission rules in explicit task contracts and bounded tool-feedback loops; 407/425 (95.8%) public-testbench passes on HLS-Eval; 104/107 (97.2%) admitted designs under held-out co-simulation on HLS-LeVeri. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25351) · [PDF](https://arxiv.org/pdf/2611.25351v1)

### 16.2 SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video
**SceneAnything：从单视频进行大规模网格场景的智能体重建**

- **Authors / 作者:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Zahra Montazeri
- **Affiliation / 机构:** see PDF page 1 (see PDF).
- **Summary / 概要:** Automated system for reconstructing mesh scenes from video, enabling text-to-scene construction; a software harness coordinates agents, pretrained vision models, and graphics tools through an explicit reconstruction protocol; shared camera/depth/segmentation estimates ground component construction. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25340) · [PDF](https://arxiv.org/pdf/2611.25340v1)

### 16.3 Towards Restorative Urban Spaces: An Exploratory Field Study of Nature Videos on Public Multi-Display Signage
**建设复原的城市空间：公共多屏幕内容上自然视频的实地研究**

- **Authors / 作者:** Yuri Mikawa, Takumi Yokosaka, Yuki Kubota, Kazushi Maruya
- **Affiliation / 机构:** see PDF page 1 (see PDF; abstract mentions multi-display signage (MDS) installations on Tokyo university campus etc.).
- **Summary / 概要:** Nine-day exploratory field study of AI-generated nature videos across four public displays in a free-admission area of a science museum (incl. 1,263 questionnaire responses). (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25259) · [PDF](https://arxiv.org/pdf/2611.25259v1)

### 16.4 Hierarchical Traffic Engineering for Scalable Software-Defined Satellite Networks
**可扩展软件定义卫星网络的分层流量工程**

- **Authors / 作者:** Mohamed Khiari, Wiem Abderrahim, Olfa Ben Yahia, Fatma Abdelkefi
- **Affiliation / 机构:** Poly-Grames Research Centre (Polytechnique Montréal); MEDIATRON Lab, Higher School of Communications of Tunisia (Sup'Com), Carthage University (see PDF).
- **Summary / 概要:** satellite networks shifting to regenerative payloads; conventional constellation-level routing overlooks intra-payload congestion; proposes hierarchical SDN/TE across constellation and payload levels via a two-level graph (modem banks expanded into networks). (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.24777) · [PDF](https://arxiv.org/pdf/2611.24777v1)

### 16.5 CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation
**CutAgent：面向高点击率电商广告视频创作的创意基因驱动规划与体验引导自优化**

- **Authors / 作者:** Xuyue Huang, Guanbo Huang, Jiasong Feng, Run Ling
- **Affiliation / 机构:** JD.com; Tsinghua University; Tianjin University; Zhejiang University; Zhejiang University; Ao Ma†, ‡, Xi Zhao (see PDF).
- **Summary / 概要:** Dual-agent framework CutAgent = GeneAgent + VideoAgent with a structured creative gene bridging product attributes → strategy → scripts/styles; plans production (creative direction), then executes (video generation/editing), then self-evolves from past production failures. (Author-reported; see PDF.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22418) · [PDF](https://arxiv.org/pdf/2611.22418v1)

---

## 17. General — Games

> Five cooperative-game-theory papers + six video-game/game-AI papers (all published 2026-11-18/19, fresh).

### 17.1 Folk Theorems for Social Learning (Cooperative Games)
**社会学习的民间定理（博弈论）**

- **Authors / 作者:** Daniel Luo, Alex Wolitzky
- **Affiliation / 机构:** Massachusetts Institute of Technology (daniel57@mit.edu; wolitzky@mit.edu).
- **Summary / 概要:** Repeated games with purely informational externalities: players observe a signal then take public actions maximizing discounted payoff (state + own action only). When sufficiently many players and patient, equilibria aggregate information: payoffs approximate full-information; when myopic play reveals state, alternative equilibria aggregate nothing (payoffs ≈ autarky). (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25280) · [PDF](https://arxiv.org/pdf/2611.25280v1)

### 17.2 Stability Bands for Feature Attribution: The Core, the Nucleolus and the Bargaining Set of Explained-Variance Games (Cooperative Games)
**特征归因稳定性带：解释方差博弈的核、核均分配者与谈判集**

- **Authors / 作者:** Fernando Delbianco, Fernando Tohmé
- **Affiliation / 机构:** Universidad Nacional del Sur (UNS), Bahía Blanca, Argentina; Institute of Mathematics – CONICET, Bahía Blanca, Argentina.
- **Summary / 概要:** Feature attribution via the core, nucleolus and bargaining set of an explained-variance game (worth = variance of predictions from feature set). Reports a stability band per feature (share range over the core/least core; nucleolus as distinguished point; certificate of no justified objection). Three results: linear games are exactly 2-additive (multicollinearity creates coalitional structure); nucleolus = prenucleolus = Shapley value in 2-additive games; convex games have closed-form bands. In a hedonic price model, the Shapley value admits a justified coalition {Ratings, ROM, Battery} (capacity > 0.19 variance shares in a gradient-boosting forecaster with empty core). (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25238) · [PDF](https://arxiv.org/pdf/2611.25238v1)

### 17.3 Game-Theoretic Data Allocation for Expert Specialization and Routing (Cooperative Games)
**面向专家分工与路由的博弈数据分配**

- **Authors / 作者:** Mark Lovett, Denis Lim, Soroush Vosoughi
- **Affiliation / 机构:** Dartmouth College; Independent Researcher.
- **Summary / 概要:** Introduces InflEns — a mixture of LoRA experts whose training weights and inference routes come from the same location game; ~90% of prompts have the highest-share expert as lowest held-out NLL (vs ~15% after permutation); retrace harmful behavior to a single expert; lowers HarmBench attack success from 0.51 to 0.02. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25167) · [PDF](https://arxiv.org/pdf/2611.25167v1)

### 17.4 An α-potential linear approximation for LQ differential games (Cooperative Games)
**LQ 微分博弈的 α-potential 线性近似**

- **Authors / 作者:** Balint Varga, Gergely Lóránt Kissa, Andreas Schwung
- **Affiliation / 机构:** Karlsruhe Institute of Technology (KIT), Institute of Control Systems, Kaiserstraße 12, 76131, Germany; South Westphalia University of Applied Science, Lübecker Ring 2, Soest, 59494, Germany.
- **Summary / 概要:** Feedback Nash equilibria of infinite-horizon LQ differential games require solving coupled algebraic Riccati equations; αPL approximation constructs a reference potential game whose equilibrium is a single ARE, then linearizes the cAREs around it; reduces mean iterations on 10⁴ random 2-player games, persists up to N=13. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25149) · [PDF](https://arxiv.org/pdf/2611.25149v1)

### 17.5 Hardness of "Infinite Energy" Puzzles (Cooperative Games)
**“无限能量”谜题的复杂度**

- **Authors / 作者:** Utkarsh Tiwari, Utkarsh Thanvi, Armaan Sethi, Aalok Thakkar, Neeldhara Misra
- **Affiliation / 机构:** TTIC 2BITS Pilani; Ashoka University; IIT Gandhinagar; Alt Earth (see PDF).
- **Summary / 概要:** Puzzle game study: single-player "Infinite Energy" (Light Potato, 2025): wire a socket network so energy circulates after power-off. Variants: colorless (NP-hard by reduction from Hamiltonian Path; in PSPACE; a 7-socket instance winning only via temporary battery loop), unconstrained (TC⁰-complete), geometric k≥2 (NP-hard), 1D open, colored (NP-hard). Can be played at https://infinite-energy-peer-review.netlify.app. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.24918) · [PDF](https://arxiv.org/pdf/2611.24918v1)

### 17.6 Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate (Video Game / Game AI)
**流式 AAA 游戏视频生成：高分辨率、高帧率**

- **Authors / 作者:** (see PDF)
- **Affiliation / 机构:** Tencent AIPD (Speed and latency tested on NVIDIA A800 GPUs — see PDF).
- **Summary / 概要:** Controllable streaming video generation as a route toward interactive game simulation.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26040) · [PDF](https://arxiv.org/pdf/2611.26040v1)

### 17.7 When Agents Play Differently: Localizing Human–Agent Behavioral Divergence
**当智能体扮演不同角色时：定位人类–智能体行为发散**

- **Authors / 作者:** (see PDF)
- **Affiliation / 机构:** King AI Labs, Microsoft Gaming, Stockholm, Sweden; KTH Royal Institute of Technology (see PDF).
- **Summary / 概要:** Evaluating whether AI agents behave like humans requires comparing not just average outcomes but entire behavioral distributions across diverse contexts. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26012) · [PDF](https://arxiv.org/pdf/2611.26012v1)

### 17.8 Safe Subgame Resolving in Multiplayer Games
**多人对弈中的子博弈安全解析**

- **Authors / 作者:** (see PDF)
- **Affiliation / 机构:** Institute for Interdisciplinary Information Sciences, Tsinghua University (see PDF).
- **Summary / 概要:** Poker and other games with hidden information are too large to solve in one pass; strong systems compute complete blueprints offline and refine them in real time inside the reached subgame. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25981) · [PDF](https://arxiv.org/pdf/2611.25981v1)

### 17.9 ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds
**ContextRenderer：交互式游戏世界的动态上下文视频生成**

- **Authors / 作者:** (see PDF)
- **Affiliation / 机构:** 1University of Science and Technology of China; 2Shanghai Jiao Tong University; 3University of British Columbia (see PDF).
- **Summary / 概要:** Interactive game world models separate executable world evolution from visual generation; ContextRenderer renders engine-provided scene representations into detailed observations via dynamic-context video generation. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25838) · [PDF](https://arxiv.org/pdf/2611.25838v1)

### 17.10 Uniqueness, Proximity, and Scaling in Atomic Splittable Polymatroid Congestion Games
**可分可拆多面体拥塞博弈中的唯一性、近似与缩放**

- **Authors / 作者:** (see PDF)
- **Affiliation / 机构:** University of Passau, Tobias Harks (see PDF).
- **Summary / 概要:** Polynomial-time algorithm for exact equilibrium computation in atomic splittable polymatroid congestion games with integral ranks and player-specific affine latencies. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25757) · [PDF](https://arxiv.org/pdf/2611.25757v1)

### 17.11 Embodied Human-Data Interaction
**具身人类数据交互**

- **Authors / 作者:** (see PDF)
- **Affiliation / 机构:** Department of Computer Science, Aarhus University (see PDF).
- **Summary / 概要:** Concept of human-data interaction (HDI) — the human manipulation, analysis and sensemaking of large unstructured datasets, proposing embodied interaction approaches. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25744) · [PDF](https://arxiv.org/pdf/2611.25744v1)

---

## 18. General — Code Execution Prediction

> **Empty in this digest window.** Queries used: `all:code execution`, `all:program execution`, `all:execution prediction` (max 40 results, filtered by topic keywords); no arXiv paper this window is tagged for code-execution prediction (see the venue sections above for execution-related papers — e.g., the ICML 2026 f-divergence self-play work, ICLR 2026 Fuse-PINN).

---

## 19. General — Agent Systems

### 19.1 Distributed Regenerative Resource Allocation with Exact Centralized Optimality
**可精确复制集中最优性的分布式再生资源分配**

- **Authors / 作者:** Rajul Kumar, Goutam Das, Ningshi Yao
- **Affiliation / 机构:** Department of Electrical and Computer Engineering, George Mason University, Fairfax, VA (truncated PDF page 1 — see PDF).
- **Summary / 概要:** Distributed Regenerative Resource Allocation (DRRA) framework for multi-agent networks with utility-driven resource regeneration (next round's resource depends on agents' utilities); fully distributed two-stage inner–outer dynamics (primal–dual allocation + regeneration); exponential convergence to Lyapunov-stable equilibrium; after convergence, exact centralized optimum recovery (author-reported).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25490) · [PDF](https://arxiv.org/pdf/2611.25490v1)

### 19.2 VisualTalk-Bench: Evaluating Question-Driven Avatar-Led Video Explanations
**VisualTalk-Bench：评估提问驱动的虚拟形象主导视频解释**

- **Authors / 作者:** Xin Zhang, Tujie Xu, Zhiyi Chen, Xiaodong Zhang
- **Affiliation / 机构:** see PDF page 1 (see PDF).
- **Summary / 概要:** Benchmark for question-driven avatar-led video explanations (finance, Chinese/English education); 800 curated reference videos + 100 independent evaluation requests; assesses Content Factuality, Speech-Visual Consistency, Visual Quality, Motion Smoothness and ... (truncated). (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25444) · [PDF](https://arxiv.org/pdf/2611.25444v1)

### 19.3 BOOMerang: Autonomous Translation from RTL to Microarchitectural Simulators and Back
**BOOMerang：自主从 RTL 到微架构仿真器及回转翻译**

- **Authors / 作者:** Ferran Hermida-Rivera, Jack Toubes, Angela Cui, Chengyi Lux Zhang
- **Affiliation / 机构:** UC Berkeley; {ferran, jtoubes, angelacui, iansseijelly}@berkeley.edu, sagark@eecs.berkeley.edu (see PDF).
- **Summary / 概要:** Agentic loops translating between high-level simulators (gem5) and RTL implementations; addresses out-of-sync between simulator feedback and hardware reality. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25438) · [PDF](https://arxiv.org/pdf/2611.25438v1)

### 19.4 Stuck in Place: Stall Diagnosis and Remedies for JEPA Planners
**原地打转：JEPA 规划器的停滞诊断与补救**

- **Authors / 作者:** Junhyeok Lee, Dongheon Lee, Kyu Sung Choi
- **Affiliation / 机构:** Seoul National University.
- **Summary / 概要:** JEPA world models plan from pixels with MPC; failures often occur at tasks the model should handle; follows the executed planning loop (pushing tasks): ≥96% of failures are stalls where the object stays in place while the model predicts progress; warm-started GD planner returns the same plan (a fixed point) — proposes stall diagnosis and remedies. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25415) · [PDF](https://arxiv.org/pdf/2611.25415v1)

### 19.5 AI-Native Industrial Control Systems: An Agent Architecture for the Control System Lifecycle
**AI 原生工业控制系统：面向控制系统全生命周期的智能体架构**

- **Authors / 作者:** Lisi Liu, Ang Zhou, Chuan Pang, Feng Gao
- **Affiliation / 机构:** Department of New Networks, Pengcheng Laboratory, Shenzhen, China.
- **Summary / 概要:** AI-native industrial control: agents determine required control functions, construct applications, prepare execution environments; system-level agents coordinate device-level agents within configured resource/permission constraints; physical sorting workstation illustrates adaptation. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25411) · [PDF](https://arxiv.org/pdf/2611.25411v1)

### 19.6 Cognitive Constraints and Misspecification Concern
**认知约束与误差设定担忧**

- **Authors / 作者:** Drew Fudenberg, Florian Mudekereza
- **Affiliation / 机构:** Department of Economics, MIT (drew.fudenberg@mit.edu; florianm@mit.edu).
- **Summary / 概要:** Repeated decision problems where agents have cognitive constraints and are concerned their models are misspecified; weights candidate models by a cognitive-capacity constraint; shows data can leave current behavior unchanged while affecting later responses. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25368) · [PDF](https://arxiv.org/pdf/2611.25368v1)

---

## 20. General — Generative Models

### 20.1 SegAnyFruit: Learning Generalizable and Edge Deployable Fruit Instance Segmentation at Scale
**SegAnyFruit：规模化可泛化且边缘可部署的水果实例分割**

- **Authors / 作者:** Yanan Wang, Yuzheng wang, Yibin Ying, Zhenghao Fei
- **Affiliation / 机构:** 1Zhejiang University; 2Alibaba Token Hub, Alibaba Group; 3University of California, Davis (see PDF).
- **Summary / 概要:** Data construction + progressive training framework distilling foundation-model priors into lightweight, prompt-free fruit segmenters; combines generic mask pre-training, broad mid-training on WebFruits (automatically annotated web imagery), and human-verified agricultural refinement post-training on PaperFruits (733K images, 9.66M masks, 165 fruit types); zero-shot on 7 benchmarks. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25475) · [PDF](https://arxiv.org/pdf/2611.25475v1)

### 20.2 Faithful Generative Modeling for Censored Time-to-Event Data: From Distributional Fidelity to Statistical Inference
**受审核时间结果的忠实生成模型：从分布准确性到统计推断**

- **Authors / 作者:** Yin Liu, Shanshan Zhao, Didong Li
- **Affiliation / 机构:** see PDF page 1 (see PDF).
- **Summary / 概要:** Two-stage generative framework for survival data (TSG): stage 1 trains the generator for distributional fidelity of synthetic survival data; stage 2 uses survival analysis methods for statistical inference on the generated data — fidelity checks and inferential validity. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25464) · [PDF](https://arxiv.org/pdf/2611.25464v1)

---

## 21. General — Sequential Modeling

### 21.1 TAP: Tapping the Discriminative Potential of Frozen Representations for Class-Incremental Learning
**TAP：挖掘冻结表征的判别潜力用于增量类学习**

- **Authors / 作者:** Zihao Wang, Yu-Wei Zhan, Xiao-Qian Liu, Zhen-Duo Chen, Weitong Liu, Xin Luo, Xin-Shun Xu
- **Affiliation / 机构:** 1Shandong University, Jinan, China; 2Zhejiang University of Technology, Hangzhou, China.
- **Summary / 概要:** Class-incremental learning (CIL) with frozen pretrained models (CLIP space): TAP accumulates visual + semantic class info in the frozen embedding space with only lightweight optimization; three modules: class-conditional visual distribution modeling, class-adaptive semantic calibration, visual-semantic posterior fusion; SOTA on 9 datasets × 2 protocols (highest average incremental + final-stage accuracies). (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25478) · [PDF](https://arxiv.org/pdf/2611.25478v1)

### 21.2 Demonstration-Free Skill Composition for Navigation and Manipulation
**无演示技能组合用于导航与操作**

- **Authors / 作者:** Madeleine Nouri, Gelareh Mohammadi, Francisco Cruz
- **Affiliation / 机构:** School of Computer Science and Engineering, University of New South Wales, Sydney, Australia; Escuela de Ingeniería, Universidad Central de Chile, Santiago, Chile.
- **Summary / 概要:** Hierarchical RL pipelines with demonstration-free skill composition: FourRooms navigation (two parameterised skills, unseen layouts) + robotic manipulation (reaching/grasp/lifting trained separately, downstream skills from predecessor rollout states); hierarchical pipeline beats flat DQN on navigation (fewer interactions) and beats flat SAC on manipulation (fewer steps, less seed variance); frozen Pick/Lift reused for stacking via a Place skill. Accepted at ACRA 2026. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25462) · [PDF](https://arxiv.org/pdf/2611.25462v1)

### 21.3 DS3M: Deep structured state space models for nonlinear system identification on modern hardware
**DS3M：现代硬件上的非线性系统辨识深度结构态空间模型**

- **Authors / 作者:** Marco Roschkowski, Hannes Gernandt
- **Affiliation / 机构:** University of Wuppertal, Wuppertal, Germany.
- **Summary / 概要:** Neural state-space identification via SUBNET (encoder estimates initial states from short histories); DS3M combines compact nonlinear dynamical components in parallel/series; Triton custom GPU kernels reduce launch/memory overhead of sequential evaluation; port-Hamiltonian variant; benchmark comparisons of accuracy and training time. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25274) · [PDF](https://arxiv.org/pdf/2611.25274v1)

### 21.4 Scone: Symmetry-aware Neural Combinatorial Optimization for Graph Coloring
**Scone：面向图着色的对称感知神经组合优化**

- **Authors / 作者:** Paolo Pellizzoni, Melanie Weber
- **Affiliation / 机构:** Harvard University.
- **Summary / 概要:** Color-equivariant GNN constructs colorings sequentially (color permutation invariance exploited to reduce effective state space; symmetry breaking for adjacent nodes in same orbit); achieves perfect solution quality with low inference times on sudoku_extreme, register allocation; generalizes to unseen graph families. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25273) · [PDF](https://arxiv.org/pdf/2611.25273v1)

### 21.5 Entanglement Geometry Beyond Polygons: Graph-Theoretic Entanglement Inequalities
**多边形之外的纠缠几何：基于图论的纠缠不等式**

- **Authors / 作者:** Masoud Gharahi
- **Affiliation / 机构:** Faculty of Physics, Astronomy and Applied Computer Science, Jagiellonian University, 30-348 Kraków, Poland.
- **Summary / 概要:** Entanglement entropies of pure multipartite states constrained by organizing subsystem cuts as graph edges (hyperedges); derives constraints from strong subadditivity + pure-state complementarity; determines optimal polygon coefficient for a distinguished two-party cut; cycle/complete-graph inequality recovery; k-marginal and collective hyperstar inequalities with optimal coefficients; bond-dimension bounds for MPS + sequential-recovery error estimates. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25019) · [PDF](https://arxiv.org/pdf/2611.25019v1)

---

## 22. General — Benchmarks

### 22.1 Dynamical Variational Theory of Stochastic Reaction Networks
**随机反应网络的动力学变分理论**

- **Authors / 作者:** Moshir Harsh, Peter Sollich
- **Affiliation / 机构:** 1Department of Mathematics, King's College London, London WC2R 2LS, UK; † Present affiliation: Harvard Medical School (see PDF).
- **Summary / 概要:** Field-theoretic variational approximation for stochastic population dynamics (biochemical reaction networks, gene regulation, epidemic spreading, ecology, population genetics) — predicting mean populations, fluctuations, time-lagged correlations, response functions, steady states. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25491) · [PDF](https://arxiv.org/pdf/2611.25491v1)

### 22.2 Atlas: Accelerating Quantum FTQC Compilation with Optimized Algebraic Rotation Synthesis
**Atlas：利用优化代数旋转合成加速量子 FTQC 编译**

- **Authors / 作者:** Anbang Wu, Pu Pang, Wei Geng
- **Affiliation / 机构:** Anbang Wu and Pu Pang, Shanghai Jiao Tong University; Wei Geng, South China University of Technology (see PDF).
- **Summary / 概要:** Rotation synthesis cost recurs in VQE/VQE-style optimization loops; identified redundancy and uneven synthesis time; proposes optimized algebraic synthesis (mitigates redundancy computation + uneven synthesis time). (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25448) · [PDF](https://arxiv.org/pdf/2611.25448v1)

### 22.3 VisualJevBench: A Benchmark and Black-Box Attacks for Visual Typed Decision Models
**VisualJevBench：视觉类型化决策模型的基准与黑盒攻击**

- **Authors / 作者:** Li Zeng, Yeqi Zeng, Hengkai Liang, Shiguo Wang
- **Affiliation / 机构:** see PDF (see PDF; authors: Li Zeng, Yeqi Zeng, Hengkai Liang, Shiguo Wang, Meng Xie).
- **Summary / 概要:** Typed decision models (Jev) — structured decisions instead of free text; red teaming of Visual Jev: systematic image-manipulation eval lacking + universal visual attacks (typographic manipulations across four scenarios + four visual attack surfaces — see PDF). (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25435) · [PDF](https://arxiv.org/pdf/2611.25435v1)

### 22.4 Covering Location Optimization at GPU Speed
**GPU 速度下的覆盖选址优化**

- **Authors / 作者:** Yun-Tian Zhang, Chen Chen
- **Affiliation / 机构:** National Key Lab of Autonomous Intelligent Unmanned Systems, Beijing Institute of Technology (see PDF).
- **Summary / 概要:** GPU-accelerated parallel search framework for the maximal covering location problem: device-resident multi-trajectory exploration + CPU-side coordination; exact incremental gains evaluated via sparse coverage representations + tiled CUDA kernels; hierarchical reduction for best exchange; destroy-and-repair + elite-guided restarts. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25434) · [PDF](https://arxiv.org/pdf/2611.25434v1)

### 22.5 The Four-Element Theory of Structure-Driven Methodology: A Methodological Shift from the Perspective of Natural Science and Engineering Practice
**结构驱动方法论的四元素理论：从自然科学与工程实践视角出发的方法论转型**

- **Authors / 作者:** Shengchang Chen
- **Affiliation / 机构:** School of Earth Sciences, Zhejiang University, Hangzhou, China.
- **Summary / 概要:** Structure-driven methodology: four irreversible stages — Deconstruction, Structure, Construction, Solving — reconstructs the solving process of complex nonlinear problems; ODI paradigm replaced by interpretable models with OOD generalization; provides a methodological shift for natural science and engineering practice. (Author-reported.)
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25370) · [PDF](https://arxiv.org/pdf/2611.25370v1)

---

*Note: all abstracts/results are author-reported excerpts from arXiv pages; affiliations are page-1 PDF-extracted; venue coverage relies on arXiv venue/comment tags (no OpenReview/proceedings crawls). All metrics are unverified.*
