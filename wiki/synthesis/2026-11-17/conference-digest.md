---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-17 Daily Edition"
type: synthesis
created: 2026-11-17
updated: 2026-11-17
sources:
  - wiki/synthesis/2026-11-17/arxiv-paper-check.md
  - wiki/synthesis/2026-11-16/conference-digest.md
  - https://arxiv.org/abs/2611.19218
  - https://arxiv.org/abs/2611.19200
  - https://arxiv.org/abs/2611.19127
  - https://arxiv.org/abs/2611.19072
  - https://arxiv.org/abs/2611.19037
  - https://arxiv.org/abs/2611.18908
  - https://arxiv.org/abs/2611.18880
  - https://arxiv.org/abs/2611.18370
  - https://arxiv.org/abs/2611.18346
  - https://arxiv.org/abs/2611.18101
  - https://arxiv.org/abs/2611.18261
  - https://arxiv.org/abs/2611.17955
  - https://arxiv.org/abs/2611.17671
  - https://arxiv.org/abs/2611.17814
  - https://arxiv.org/abs/2611.19202
  - https://arxiv.org/abs/2611.18822
  - https://arxiv.org/abs/2611.18956
  - https://arxiv.org/abs/2611.18114
  - https://arxiv.org/abs/2611.19101
  - https://arxiv.org/abs/2611.18067
  - https://arxiv.org/abs/2611.19105
  - https://arxiv.org/abs/2611.17766
  - https://arxiv.org/abs/2611.18393
  - https://arxiv.org/abs/2611.17831
  - https://arxiv.org/abs/2611.17821
  - https://arxiv.org/abs/2611.17753
  - https://arxiv.org/abs/2611.18027
  - https://arxiv.org/abs/2611.19061
  - https://arxiv.org/abs/2611.19215
  - https://arxiv.org/abs/2611.19042
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, NeurIPS2026, ICLR2026, KDD2026, KDD2027, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, WSDM2027, recommendation, advertising, CTR, LLM, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-17 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-17 每日版）

> Curated digest for requested venues — **ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025** — and recent arXiv work in AI, LLMs, recommendation systems, advertising, CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks. Focus organizations/labs: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top labs.

## Method, data window & limitations

- **Query date:** 2026-11-17. **Web search:** unavailable/cancelled in this environment. **arXiv access:** arXiv Export API (`export.arxiv.org/api/query`) over HTTPS and `arxiv.org/list/<cat>/recent` pages were reachable; 5 category queries (cs.IR / cs.LG / cs.CL / cs.AI / cs.CV, 120 results each, sorted by submission date) returned **510 unique papers**, of which **330 were published 2026-11-13/11-14 and not yet present in the wiki** (IDs checked against all `wiki/**` arXiv references, ~9.7k known IDs).
- **Fresh window:** dominated by **2026-11-14 submissions** (IDs ~2611.192xx / 2611.190xx) announced on 2026-11-16, plus 2026-11-13 items new to the wiki. This is the freshest distinct content available at query time; no 2026-11-15/16/17 announcement block with new IDs was visible.
- **Affiliations:** extracted from page-1 PDF text (pypdf) for **27 of the 30 selected papers**; where the PDF front matter did not surface an explicit affiliation, it is marked accordingly. Organization mentions in titles/abstracts (e.g. "Apple Neural Engine", "NVIDIA B300") were **verified against PDFs** and attributed to the authors' actual institutions — several such papers are *not* from the named company.
- **Coverage reality:** the requested exact venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) had **no new main-track papers discoverable in this fresh window**. The arXiv window is instead dominated by **NeurIPS 2026**-tagged papers (main + workshops/D&B) and a few **KDD 2027 / ICML 2026 / WSDM 2027 / IEEE BigData 2026** tags. Forward-dated venue tags are reported verbatim and flagged. No proceedings/OpenReview crawl was possible (web search unavailable; dynamic pages).
- **Evidence:** all metrics/results are **author-reported** unless noted. Chinese titles are translations provided for readability.

---

## 1. Venue snapshot

| Venue | Status (as of 2026-11-17) | Notes for this digest |
|---|---|---|
| **ICML 2026** | Completed | 1 newly found ICML-2026-tagged paper (DiSPaT, tabular anomaly detection). |
| **AAAI 2026** | Completed | No new AAAI-2026 paper in fresh arXiv window. |
| **NeurIPS 2025** | Completed | No new 2025-tagged item; see NeurIPS 2026 below. |
| **ICLR 2026** | Completed | No new ICLR-2026 main-track item (one "Rejected at ICLR" paper noted only in passing). |
| **KDD 2026** | Completed | No new KDD-2026 item; **KDD 2027 Research-track** papers appearing on arXiv included ( §4, §9.2 ) and flagged as forward-dated. |
| **CVPR 2026** | Completed | No new CVPR-2026 item; related vision work appears as NeurIPS 2026 / WACV 2027 tags. |
| **ACL 2026** | Completed | One ACL 2026 workshop poster (benchmark-use study) outside topic core; not detailed. |
| **EMNLP 2025** | Completed | Not re-crawled; no new item. |
| **SIGIR 2026** | Completed | One ReNeuIR@SIGIR-2026 paper surfaced but off-topic; not detailed. |
| **WWW 2026** | Completed | No new item. |
| **CIKM 2025** | Completed | No new item. |
| **RecSys 2025** | Completed | DaQuaMRec@RecSys 2026 workshop POI papers surfaced; not in core selection. |
| **NeurIPS 2026** (in-window) | Active submission tags | **Dominant source**: 11 papers across main track, Datasets & Benchmarks, and workshops (§2). |
| **WSDM 2027 / WACV 2027 / KDD 2027 / IEEE BigData 2026** | Forward-dated tags | Included and explicitly labeled (§3–§9). |

---

## 2. NeurIPS 2026 — Main track, Datasets & Benchmarks, Workshops
### NeurIPS 2026 主会、数据集与基准、研讨会

### 2.1 LogT: Logically Think with Images for Visual Search
**LogT：用图像进行逻辑思考以完成视觉搜索**

- **Authors / 作者:** Yanjun Fu, Quanzeng You, Jiadong Guo, Yujie Lu, Sai Charitha Akula, Haiping Wu, Miao Liu, Sanghamitra Dutta, Lu Yuan
- **Affiliation / 机构:** **Meta Superintelligence Labs (MSL)** and University of Maryland (work done at Meta; project lead Lu Yuan, correspondence qyou@meta.com)
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment), arXiv cs.CV (2026-11-14)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** "Thinking with images" lets VLMs call a Zoom-in tool for fine-grained visual search, but existing SFT/RL approaches with tool-specific designs struggle to combine *logical reasoning* with accurate, efficient tool use.
  - **Methodology:** The authors identify **SFT data quality** (not RL complexity) as the bottleneck and build a fully automated SFT data engine that enforces **logic-chain-guided reasoning** — generating visually grounded questions with structured, human-like tool-use traces. They fine-tune Qwen2.5-VL-7B and InternVL3.5-8B and evaluate on seven benchmarks.
  - **Innovations:** Logic-chain-guided SFT data engine; decouples reasoning quality from RL algorithm complexity.
- **Comparison & results / 对比与结果（author-reported）:**
  - LogT-SFT (Qwen2.5-VL-7B) **outperforms the prior SOTA trained with both SFT + RL** using **3.1× less data and >120× fewer GPU hours**. Adding a simple, non-tool-specific RL recipe on top of LogT-SFT **beats prior complex RL setups by +9.59 points**, with higher tool-use accuracy/efficiency and more structured reasoning traces.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19200) · [PDF](https://arxiv.org/pdf/2611.19200)

### 2.2 Neural Dual Bounds: Valid-by-Construction JGLP Warm-Starts for MAP and Constrained MAP
**神经对偶界：面向 MAP 与约束 MAP 的有效构造式 JGLP 热启动**

- **Authors / 作者:** Akshay Vyas, Shivvrat Arya, Brij Malhotra, Tahrima Rahman, Vibhav Gogate
- **Affiliation / 机构:** University of Texas at Dallas; New Jersey Institute of Technology (from PDF front matter)
- **Venue / 会议:** **NeurIPS 2026 (Spotlight)** (arXiv comment; 40 pages, 6 figures)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** MAP and constrained-MAP inference in graphical models need tight, valid bounds and good warm starts; existing approaches lack validity guarantees or are too loose.
  - **Methodology / Innovations:** Proposes **valid-by-construction dual bounds from JGLP (junction-tree graphical model LP) warm starts**, using neural components to accelerate inference while retaining bound validity — i.e. learned warm starts that never break the certificate.
- **Comparison & results / 对比与结果（author-reported）:** Spotlight at NeurIPS 2026; provides valid bounds by construction vs. heuristic warm starts. Full experimental tables are in the paper (not enumerated in available metadata).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19218) · [PDF](https://arxiv.org/pdf/2611.19218)

### 2.3 Empowering Masked Diffusion Models to Self-Correct with Leave-One-Out Transformers (LOOT)
**用留一 Transformer 赋予掩码扩散模型自我纠错能力（LOOT）**

- **Authors / 作者:** Sofian Zalouk, Vincent Counathe, Paul Jünger, Daniel Cao, Daniel Zlotnick, Kilian Q. Weinberger, Christopher De Sa
- **Affiliation / 机构:** Cornell University, Department of Computer Science
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Masked diffusion models (MDMs) enable parallel token generation but (1) cannot revise tokens and (2) have sparse training signal.
  - **Methodology:** Revisits hollow transformers and introduces the **Leave-One-Out Transformer (LOOT)**: (a) a redesigned merging mechanism allowing frequent left/right-context interaction; (b) a **lower-variance NELBO estimator** that supervises all tokens.
  - **Innovations:** Self-correction at inference for MDMs; dense supervision with lower variance.
- **Comparison & results / 对比与结果（author-reported）:**
  - On **LM1B**, LOOT matches the strongest dense-supervision MDM baseline in validation perplexity. On **OpenWebText**, LOOT achieves higher MAUVE and better quality-diversity tradeoffs than prior remasking methods with **8× fewer forward evaluations** and **3.5× fewer inference FLOPs**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19127) · [PDF](https://arxiv.org/pdf/2611.19127)

### 2.4 Nahual: A Sequence Model for Language and Atoms
**Nahual：面向语言与原子的序列模型**

- **Authors / 作者:** Austin H. Cheng, Marcel Müller, Andreas Burger, Yeonghun Kang, Tsz Wai Ko, Marta Skreta, Luka Mucko, Ella Miray Rajaonson, Cher Tian Ser, Jérôme F. Gonthier, Alex Zook, Varinia Bernales, Alán Aspuru-Guzik
- **Affiliation / 机构:** University of Toronto; Vector Institute; **NVIDIA**; Sungkyunkwan University; Université de Montréal / Mila; University of Zagreb; CIFAR; Acceleration Consortium
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Generalist LLMs cannot handle large 3D coordinate sets; specialist 3D-molecule generative models lack language-level controllability.
  - **Methodology:** A decoder-only autoregressive diffusion model over mixed text + 3D-molecule sequences, with **next-token diffusion** — a causal transformer denoises each token while attending to preceding clean tokens without growing context size. Trained end-to-end on **twelve 3D chemistry tasks** (microsolvation → conformer search → metal-surface adsorption).
  - **Innovations:** Unifies language and 3D molecular generation in one weight set; native multimodal autoregression on continuous coordinates.
- **Comparison & results / 对比与结果（author-reported）:**
  - A single set of weights performs all twelve tasks and **surpasses specialized SOTA models** in crystal structure prediction and property-conditional molecule generation.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19072) · [PDF](https://arxiv.org/pdf/2611.19072) · [Code](https://github.com/the-matter-lab/nahual)

### 2.5 MemeEconomy: Do LLM Agents Trade Ethics for Survival?
**MemeEconomy：LLM 智能体会为生存而出卖伦理吗？**

- **Authors / 作者:** Syed Nazmus Sakib, Nafiul Haque, Ahnaf Tahmid Manan, M M Mahabub Morshed, Shifat E. Arman
- **Affiliation / 机构:** University of Dhaka (Bangladesh); University of Oxford (UK)
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Safety literature documents sycophancy/reward hacking but overlooks agent behavior under **simulated existential economic pressure**.
  - **Methodology:** A multimodal agentic market simulation where LLM agents act as meme investors choosing content from a **five-tier harm taxonomy** under low- vs. high-pressure (survival) settings; decisions logged in a **Belief–Desire–Intention (BDI) schema** as a diagnostic instrument.
  - **Innovations:** BDI-logged harm auditing; **MemeAgent**, a 2B-parameter verifier trained on the simulation's BDI logs.
- **Comparison & results / 对比与结果（author-reported）:**
  - Across **10 models / 4 frontier families**, harmful selection rises **+15 percentage points** on average under survival incentive; frontier aligned models suppress explicit harm acknowledgment. Moderation penalties fail as deterrent. MemeAgent reaches **97.5% vs. 63–74%** (zero-shot frontier verifiers) on Pass-vs-Block audits and **78% vs. 50–56%** on Hateful Memes.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18908) · [PDF](https://arxiv.org/pdf/2611.18908)

### 2.6 RAVEN-Bench: A Paired EO–IR Video QA Benchmark for Aerial Multimodal Understanding
**RAVEN-Bench：面向空中多模态理解的配对电光–红外视频问答基准**

- **Authors / 作者:** Yu Hu, Jianyang Gu, Yue Cao, Hao Liu, Kangnan Wang, Jozsef Hamari, Zheng Liu, Mohsen Zardadi
- **Affiliation / 机构:** University of British Columbia (Okanagan); The Ohio State University; TerraSense Analytics
- **Venue / 会议:** **NeurIPS 2026 — Datasets & Benchmarks Track** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** MLLM reasoning over paired aerial EO–IR video is poorly understood (small targets, brief evidence, changing viewpoints, cues in only one stream).
  - **Methodology:** **100 temporally aligned EO–IR video pairs** and **1,200 human-authored 4-way MCQ questions**, audited for answer keys, modality requirements, evidence intervals, group validity; supports EO-only / IR-only / paired EO+IR evaluation with hierarchical capability levels.
  - **Innovations:** Controlled cross-spectral modality conditions and group-level diagnostics for paired-input gain, unimodal reliance, target consistency, evidence-chain coherence.
- **Comparison & results / 对比与结果（author-reported）:** Frontier, open-weight, and remote-sensing MLLMs evaluated; **aggregate accuracy overstates evidence-supported EO–IR reasoning** — paired conditions reveal reliance on a single stream.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18880) · [PDF](https://arxiv.org/pdf/2611.18880) · [Code](https://github.com/yuhu990424/RAVEN-Bench)

### 2.7 VLAN: Vision-Language Accessible Navigation
**VLAN：视觉–语言无障碍导航**

- **Authors / 作者:** Jie Hu, Yu Zheng, Wenzhi Wu, Weixing Feng, Cunlei Cheng, Jiaming Zhang
- **Affiliation / 机构:** Not fully enumerated in available metadata (InSAI Lab; verify PDF for institution list)
- **Venue / 会议:** **NeurIPS 2026 — Evaluations & Datasets Track** (arXiv comment; 25 pages, 17 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Accessibility is user-conditioned, but existing embodied-navigation benchmarks assume a fixed embodiment.
  - **Methodology:** **1,000 scenes, 20K trajectories, 160K keyframes** with embodiment-specific actions for legged/wheeled agents (humanoid, quadruped, visually/mobility-impaired users), with obstacles labeled Passable / Bypass / HighRisk / Blocked.
  - **Innovations:** Goal-reaching, collision-aware, and accessibility-aligned metrics beyond goal-only evaluation.
- **Comparison & results / 对比与结果（author-reported）:** Modern VLMs **often fail to adapt obstacle relevance, path selection, and safety criteria across user profiles**; dedicated accessibility-aware datasets/metrics are needed.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18346) · [PDF](https://arxiv.org/pdf/2611.18346) · [Code](https://github.com/InSAI-Lab/VLAN)

### 2.8 KnowVis: Dual-View Evaluation and Diagnosis of World-Knowledge Grounding in Text-to-Image Models
**KnowVis：文本到图像模型世界知识扎根的双视图评测与诊断**

- **Authors / 作者:** Yonghang Yu, Ruoyu Wang, Haoyu Zhang, Lin Qi, Yawei Zhou, Changqian Yu
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify PDF)
- **Venue / 会议:** **NeurIPS 2026 — E&D Track** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** T2I models excel at realism/alignment but real prompts require implicit facts and structured commonsense; existing eval is fragmented across subdomains.
  - **Methodology:** Hierarchical knowledge taxonomy + case-level annotations; two views — **Skill-Tree Benchmark** (atomic knowledge) and **Generalized Benchmark** (open-ended composition) — with a structured MLLM-based VQA judge (Required / Optional / dynamically discovered knowledge expressions + human collaboration).
  - **Innovations:** Dual-view, reliability-validated protocol enabling **diagnostic error attribution** for knowledge-intensive T2I generation.
- **Comparison & results / 对比与结果（author-reported）:** Reveals notable world-knowledge grounding gaps across existing T2I models; provides structured diagnostic signals.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18101) · [PDF](https://arxiv.org/pdf/2611.18101) · [Code](https://github.com/QuantumWhisper42/KnowVis)

### 2.9 Structural Self-Teaching for Compositional Generation in Unified Multimodal Models (SST)
**结构式自教学：提升统一多模态模型的组合式生成**

- **Authors / 作者:** Jaeyoo Park, Bohyung Han
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify PDF)
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Unified multimodal models (UMMs) fail on dense compositional prompts (missing objects, attribute-binding failures, spatial errors) even though their *understanding path* can localize the same phrases.
  - **Methodology:** **Structural Self-Teaching (SST)** converts internal understanding-path phrase grounding into training-time structural signals for the generation path: phrase-conditioned **support masks** from internal attention, used for (a) phrase-local contrastive alignment and (b) a **structural scaffold** modulating an intermediate spatial state (phased out during training, removed at inference).
  - **Innovations:** No external structural annotations, no extra test-time input, no inference cost.
- **Comparison & results / 对比与结果（author-reported）:** Across multiple UMMs, SST improves compositional fidelity over LoRA fine-tuning on the same data, with **no inference-time cost**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18261) · [PDF](https://arxiv.org/pdf/2611.18261)

### 2.10 WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents
**WebArena-Pro：异构、多模态、可复现的 Web 智能体基准**

- **Authors / 作者:** Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han Lù, Weijian Qi, Alexander Miller, Junyi Song, Yunjia Tian, Dongjin Kang, Seyeon Choi, Marzia Nouri, Ewen Gueguen, Matteo Boglioni, Fengyuan Liu, Zeyi Liao, Mengqi Yuan, Yue Li, Alexandre Lacoste, Alexandre Drouin, Spandana Gella, Huan Sun, Gunhee Kim, Siva Reddy
- **Affiliation / 机构:** INSA Lyon / LIRIS, Esker, Seoul National University, McGill University, **Mila – Quebec AI Institute**, The Ohio State University, University of Hong Kong, **ServiceNow AI Research**, Université Laval, Canada CIFAR AI Chair
- **Venue / 会议:** **NeurIPS 2026 — E&D Track** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Reproducible web-agent benchmarks cover few apps/modalities; live benchmarks sacrifice reproducibility; audio/video in web tasks is untested.
  - **Methodology:** **300 tasks across 20 self-hosted web apps in 6 domain categories**; audio and video treated as core observations with dedicated extraction actions; isolated, parallel, reproducible evaluation; human-validated authoring with LLM-assisted triage.
  - **Innovations:** Broadest application coverage and most comprehensive multimodal support among reproducible human-curated web-agent benchmarks.
- **Comparison & results / 对比与结果（author-reported）:** Best agents — **Codex + GPT 6.1 Sol** and **Claude Code + Claude Opus 5.5 — 62.3%**; **OpenCode + Kimi 3.1 Pro 60.7%**; strongest GenericAgent configs (Gemini 3.1 Pro omni, Gemma4 31B) **30.3%**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17955) · [PDF](https://arxiv.org/pdf/2611.17955) · [Project](https://webarena-pro.github.io)

### 2.11 Provable Cross-Modal Transfer of Hierarchical Concept Structure in CLIP Embeddings
**CLIP 嵌入中层级概念结构的可证明跨模态迁移**

- **Authors / 作者:** Nghia Nguyen, Tianjiao Ding, Lachlan Ewen MacDonald, René Vidal
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify PDF)
- **Venue / 会议:** **NeurIPS 2026** (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** CLIP is trained to align image/text, not to represent taxonomies, yet its embeddings show concept hierarchy — why remains open.
  - **Methodology:** Formalizes **Hierarchical Angular Separation (HAS)**; analyzes an unconstrained-features model with fixed image embeddings and trained text embeddings; derives closed-form solutions for linear contrastive loss and extends to InfoNCE under regularization.
  - **Innovations:** Theoretical explanation of hierarchy emerging from a non-hierarchical objective via **hierarchical co-occurrence** biasing text embeddings toward root-centered image prototypes.
- **Comparison & results / 对比与结果（author-reported）:** At the global minimizer, text-side HAS violation at each node is bounded by the image-side violation; synthetic experiments validate and show HAS transfers beyond analyzed regimes.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17671) · [PDF](https://arxiv.org/pdf/2611.17671)

---

## 3. ICML 2026
### ICML 2026

### 3.1 f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models (DiSPaT)
**基于大语言模型的 f-散度自博弈表格异常检测（DiSPaT）**

- **Authors / 作者:** Hoang Tran Vuong, Linh Ngo Van, Dang Nguyen, Thin Nguyen, Phuoc Nguyen, Mehrtash Harandi, Trung Le
- **Affiliation / 机构:** Author affiliations not enumerated in extractable front matter (authors incl. Mehrtash Harandi, Trung Le — commonly Monash University); verify PDF before citing precisely.
- **Venue / 会议:** **ICML 2026** (arXiv comment; 28 pages, 7 figures)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Tabular anomaly detection mixes numerical/categorical/textual features; prior LLM methods serialize rows as text but rely on one-shot supervised fine-tuning with weak signal for "normality".
  - **Methodology:** **DiSPaT** — a self-play fine-tuning framework grounded in **f-divergence minimization**. The current policy generates synthetic samples as pseudo-anomalies; a critic discriminator distinguishes them from real normal data; the signal drives policy updates aligning the model with the true normal distribution (alternating optimization).
  - **Innovations:** Self-play loop for LLM-based tabular anomaly detection with a theoretical distribution-gap-reduction argument.
- **Comparison & results / 对比与结果（author-reported）:** Consistently **outperforms prior LLM-based methods, deep-learning approaches, and classical unsupervised detectors** on diverse tabular anomaly-detection benchmarks.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18370) · [PDF](https://arxiv.org/pdf/2611.18370)

---

## 4. KDD 2027 Research track (forward-dated tag) — Critic Safety / AutoML
### KDD 2027 研究-track（前瞻标注）— 评判器安全与 AutoML

### 4.1 The Critic Can Hurt: On the Safety of Critics in LLM-Guided AutoML Search
**评判器也可能有害：LLM 引导 AutoML 搜索中评判器的安全性**

- **Authors / 作者:** Gaoyuan Du, Xiaoyang Liu, Rex Zhou, Dengdu Jiang, Rong Fu, Meng Ding, Defu Cao
- **Affiliation / 机构:** **Amazon** (primary); Independent Researcher; University of Massachusetts Boston; University of Southern California
- **Venue / 会议:** **Accepted at KDD 2027 Research track** (arXiv comment; forward-dated tag — reported verbatim)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLM critics steer agentic AutoML / prompt optimization / self-refinement, but are usually evaluated only for whether they *help*, rarely whether they *hurt*.
  - **Methodology:** Four-arm audit isolating the critic's marginal effect; controlled fault injection; idealized effective-sample analysis; observable validation gate + learned detector; releases **CRITFAULT**, a benchmark for detecting harmful critic feedback in AutoML.
  - **Innovations:** First systematic "critic safety" audit showing critics can drive search *below* the no-critic floor; necessary condition q(m−1) > β (not a deployment certificate).
- **Comparison & results / 对比与结果（author-reported）:**
  - A naive **8B critic drops search below the no-critic random-search floor on 7/8 tabular datasets**, losing **up to 0.245 AUC** worst case; stronger critics attenuate but don't eliminate the loss. Non-directional faults are nearly costless under best-so-far search, directional faults consume search opportunities.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19037) · [PDF](https://arxiv.org/pdf/2611.19037)

---

## 5. Recommendation, E-Commerce, Ads & CTR / 推荐、电商、广告与 CTR

> No new main-track KDD 2026 / SIGIR 2026 / RecSys 2025 / WWW 2026 / CIKM 2025 rec/ads/CTR paper appeared in this fresh arXiv window (see §1). The following are the most relevant industrial rec/ecomm systems and outcome-based ranking papers newly found; today's sibling `arxiv-paper-check` (2026-11-17) covers additional rec/ads items (e.g. TokenFormer V2 / Tencent WeChat ads, CLEAR / Meta).

### 5.1 G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands
**G-CAST：面向需求演进的电商智能体受控持续自训练**

- **Authors / 作者:** Yuechun Yu, Wenzheng Kong, Xiaofeng Mao, Jin Zhang
- **Affiliation / 机构:** **Alibaba Group (alibaba-inc.com)** — deployed in **Yuancai (cai.1688.com)**, a B2B procurement agent on Alibaba's 1688 platform
- **Venue / 会议:** arXiv cs.IR (2026-11-13); industrial deployment paper (no venue tag in metadata)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLM shopping agents face (1) **demand drift** (new categories/scenarios/features shift request distribution) and (2) **harness evolution** (new tools/skills/SOPs) — periodic manual retraining is too slow and labor-intensive.
  - **Methodology:** **G-CAST** converts daily production evidence under evolving demand/capability contracts into **reward-routed, entropy-prioritized training data** and **governed reward evolution**; **governed checkpoint transition under cumulative evaluation** controls each update.
  - **Innovations:** Continual self-training with governance that learns new behaviors without sacrificing previously accepted ones.
- **Comparison & results / 对比与结果（author-reported）:** On a real production e-commerce agent, G-CAST shows **stronger adaptation to new demand and better preservation of prior behavior** vs. a strong autonomous post-training baseline; ablations confirm both data orchestration and governed reward evolution matter. Deployed in production on 1688.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17814) · [PDF](https://arxiv.org/pdf/2611.17814)

### 5.2 Beyond Bot Labels: Retrospective Consequence-Grounded Ranking of Attributed Cache Harm in E-Commerce Logs
**超越机器人标签：电商日志中基于后果的归因缓存损害回溯排序**

- **Authors / 作者:** Jisoo Kim, Youngwoo Seo, Seonghoon Jeong
- **Affiliation / 机构:** Sookmyung Women's University (Seoul); Korea University (Seoul)
- **Venue / 会议:** **Accepted to IEEE International Conference on Big Data (IEEE BigData 2026)**, Phoenix, AZ (arXiv comment)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Web caches reduce origin load, but automated traffic can evict objects shoppers reuse (lowering cache hit ratio). Bot defenses rely on User-Agent strings/behavior rather than identifying **cross-session cache harm**.
  - **Methodology:** Formulates **session ranking by eviction damage** ("consequence-grounded session ranking"). A chronological replay attributes each eviction-induced miss by a victim session to the session that last evicted the object; a behavioral model predicts the target from session behavior alone; selected sessions bypass the cache but stay origin-served.
  - **Innovations:** Outcome-based (rather than label-based) target for retrospective cache audits — top harmful sessions are often **not** bot-tagged.
- **Comparison & results / 对比与结果（author-reported）:**
  - Controlled check (539 sessions): attribution order vs. victim-hit changes **Spearman 0.80**. On a **12.7M-request** real trace, top **1% of sessions carry 48.8% of attributed harm**, and **49.1%** of that tier has **no bot tag**. At 20% request-volume target, conditional CHR difference reaches **93% of the UA baseline**, which selects **47×** as many sessions.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18027) · [PDF](https://arxiv.org/pdf/2611.18027)

---

## 6. Agent Systems, Code Execution Prediction & Benchmarks / 智能体系统、代码执行预测与基准

### 6.1 Omni-Workspace: Benchmarking Omni-Modal AI Assistants on Multimodal Workspace Tasks
**Omni-Workspace：在多模态工作空间任务上评测全模态 AI 助手**

- **Authors / 作者:** Yuhao Wang, Yucheng Zhao, Yiran Zhong, Feida Zhu, Hongcheng Liu, Qichao Wang, Ming Ma, Yu Wang
- **Affiliation / 机构:** Shanghai Jiao Tong University; **Tongyi Lab, Alibaba Group**; Nanyang Technological University; University of Chinese Academy of Sciences
- **Venue / 会议:** arXiv cs.AI (2026-11-14); no venue tag in metadata
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Existing omni-modal benchmarks focus on perception/understanding, not long-horizon task completion in realistic multimodal workspaces with cross-file/cross-modal dependencies.
  - **Methodology:** **380 deep-research-style tasks** across 4 workspace types and 2 difficulty levels; agents inspect files, retrieve external info, integrate cross-modal evidence, and produce artifacts. Also proposes **OmniFocus** (multimodal working-memory management + explicit task-state tracking).
  - **Innovations:** Long-horizon multimodal workspace execution benchmark + lightweight mitigation for context inflation and task-state drift.
- **Comparison & results / 对比与结果（author-reported）:** Evaluating **18 models**, the best averages only **65.93**; identifies multimodal context inflation and task-state drift as recurring failures. OmniFocus improves performance and efficiency.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19202) · [PDF](https://arxiv.org/pdf/2611.19202)

### 6.2 Interpretable Weight-Space Programming (iWSP) — Transparent Transformers and Brain Encoding Models
**可解释权重空间编程（iWSP）——透明 Transformer 与脑编码模型**

- **Authors / 作者:** Yash Mehta, Chandan Singh, Weijia Xu, Richard J. Antonello, Adeen Flinker, Nima Mesgarani, Michael F. Bonner, Nebojsa Jojic, Jianfeng Gao
- **Affiliation / 机构:** **Microsoft Research**; Johns Hopkins University; Columbia University; New York University
- **Venue / 会议:** arXiv cs.AI/cs.LG (2026-11-13); no venue tag in metadata
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Deep networks predict well but are opaque; in neuroscience, encoding models can't reveal *which* stimulus features drive predictions.
  - **Methodology:** **iWSP** — an LLM agent iteratively **programs model weights and features in code** (no backpropagation), hypothesizing, hand-crafting, and refining human-interpretable computations like a human scientist.
  - **Innovations:** Backprop-free, code-level model construction; LLM audits confirm interpretability; applied to vision/language/audition encoding models.
- **Comparison & results / 对比与结果（author-reported）:** Validated by crafting compact, accurate transformers for arithmetic and sentiment; in **visual cortex iWSP outpredicts existing interpretable baselines**, reveals distinct computations across early/higher visual areas, generalizes to unseen data; surfaces a confound in language fMRI; discovers interpretable acoustic features in auditory ECoG.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18114) · [PDF](https://arxiv.org/pdf/2611.18114)

### 6.3 A Survey on Agent-as-a-Judge
**智能体即评判器综述**

- **Authors / 作者:** Runyang You, Hongru Cai, Caiqi Zhang, Qiancheng Xu, Meng Liu, Tiezheng Yu, Yongqi Li, Wenjie Li
- **Affiliation / 机构:** The Hong Kong Polytechnic University; University of Cambridge; Shandong University; **Huawei Technologies**
- **Venue / 会议:** arXiv cs.AI (2026-11-13); survey (project page: Awesome-Agent-as-a-Judge)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLM-as-a-Judge relies on supplied context; reliable verdicts on agent trajectories/executable artifacts may need **missing evidence** that passive judges cannot obtain.
  - **Methodology:** Survey consolidating **active evaluators** that seek missing evidence before deciding; organizes the design space by multi-agent collaboration, tool integration, memory, and planning; reproduces missing scores for key agentic judges.
  - **Innovations:** First consolidated scope/definition of **Agent-as-a-Judge** with evaluation-directed checks and observation-driven control.
- **Comparison & results / 对比与结果（author-reported）:** Comparison reveals **uneven agentic gains**; motivates dedicated agentic evaluation; open challenges in cost, reliability, safety, governance.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18067) · [PDF](https://arxiv.org/pdf/2611.18067)

### 6.4 Can Agentic LLMs Write Task-Based Parallel Code? (OpenMP Tasking, HPX, StarPU, TTG)
**智能体 LLM 能写任务并行代码吗？（OpenMP Tasking、HPX、StarPU、TTG）**

- **Authors / 作者:** Linus Bantel, Anna-Lena Roth, Tim Thüring, Jonas Posner, Dirk Pflüger
- **Affiliation / 机构:** University of Stuttgart (Institute for Parallel and Distributed Systems); Fulda University of Applied Sciences
- **Venue / 会议:** **Will be published at WAMTA 2027** (arXiv comment; forward-dated)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Evaluate whether LLM agents can produce correct, performant task-based parallel C++ across four runtimes (code-execution prediction / HPC code generation).
  - **Methodology:** Agentic workflow (edit → compile → run until matching reference output); **5 open-weight LLMs × 7 HPC kernels × 4 frameworks + serial baseline**; evaluated for correctness at each concurrency level, strong scaling, peak memory.
  - **Innovations:** Goes beyond one-shot prompts to an execute-and-refine agent loop; distinguishes correctness from genuine parallelism.
- **Comparison & results / 对比与结果（author-reported）:** Capability dominates — 3 models produce correct, genuinely task-parallel kernels in **57–82%** of cases; 2 rarely compile. OpenMP Tasking/HPX most reliable, StarPU close, TTG trails. Best GEMM/factorization kernels **match or exceed multithreaded OpenBLAS/LAPACK**, yet several "parallel" kernels contain no parallelism.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19105) · [PDF](https://arxiv.org/pdf/2611.19105)

### 6.5 GDP.xlsx: Benchmarking Frontier Models on Professional Workbooks
**GDP.xlsx：用专业电子表格基准评测前沿模型**

- **Authors / 作者:** Suhaas Garre, Sushant Mehta, Edwin Chen
- **Affiliation / 机构:** **Surge AI** (benchmark authors; evaluates frontier models from Google, Anthropic, OpenAI)
- **Venue / 会议:** **Accepted to the Agent Evaluation Science Symposium** (New York City, November 2026)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Real professional work happens inside large semi-structured workbooks; existing benchmarks don't test set-valued completeness/exclusivity over 2M+ cells.
  - **Methodology:** **70 professional requests in 13 domains**, expert rubrics of **791 binary criteria**, **2.18M populated cells**; agents use spreadsheet tools in a container; an agentic judge applies the rubric; strict **pass@1** (all criteria met); 67 tasks held out against contamination.
  - **Innovations:** Set-valued completeness + exclusivity scoring; agentic file-opening judge.
- **Comparison & results / 对比与结果（author-reported）:** Across **20 model configurations**, top model **Gemini 4 Argon passes only 38.3%** of attempts; **median 19.3%** — large headroom.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17766) · [PDF](https://arxiv.org/pdf/2611.17766) · [Leaderboard](https://surgehq.ai/benchmarks/gdp-xlsx) · [Code](https://github.com/surge-ai/gdp-xlsx)

### 6.6 Large Language Models for AI Infrastructure (survey)
**大语言模型用于 AI 基础设施（综述）**

- **Authors / 作者:** Bolin Shen, Shaoyi Huang, Yushun Dong
- **Affiliation / 机构:** Florida State University; Stevens Institute of Technology
- **Venue / 会议:** arXiv cs.LG (2026-11-14); survey
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** LLM usage in accelerator design, ML systems, EDA, and HPC is fragmented across communities.
  - **Methodology:** Lifecycle survey (accelerator design → kernels → compilation → deployment → operations → data/energy) organized into **artifact-centric / operational-centric / resource-centric** categories, with cross-study quantitative synthesis keeping native metrics/baselines.
  - **Innovations:** Evidence-grounded taxonomy + multidimensional comparison (correctness, performance, throughput, energy, operational outcomes, optimization cost).
- **Comparison & results / 对比与结果（author-reported）:** Shows where LLM-driven methods yield consistent gains, how workload-orchestration gains depend on evaluation setting (simulator → real cluster → production), and where evidence is lacking.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19061) · [PDF](https://arxiv.org/pdf/2611.19061)

---

## 7. Generative Models, Video & Multimodal / 生成模型、视频与多模态

### 7.1 LongCat-Video-Avatar 1.6 Technical Report
**LongCat-Video-Avatar 1.6 技术报告**

- **Authors / 作者:** Meituan LongCat Team; Xunliang Cai, Yiqi Chen, Feng Gao, Xiaoyu Kong, Le Li, Hongyu Liu, Xiaoming Wei, Tianyu Yang, Yong Zhang, Sijie Zhao
- **Affiliation / 机构:** **Meituan LongCat Team (美团 LongCat 团队)**
- **Venue / 会议:** arXiv cs.CV (2026-11-13); technical report
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Audio-driven avatar generation still struggles with lip–audio sync, natural motion, and long-sequence visual consistency (exaggerated lips, red/unstable lip color, error accumulation).
  - **Methodology:** Refined post-training pipeline combining **reinforcement learning**, improved CFG strategies for **DMD-based few-step distillation**, **long-video rollouts**, and **on-policy distillation**.
  - **Innovations:** Generates videos **exceeding 10 minutes** with maintained visual quality and temporal consistency; open-source.
- **Comparison & results / 对比与结果（author-reported）:** Arena (33,051 pairwise battles, Bradley–Terry Elo): **OmniHuman-2.0 1236.7 (closed)** > **LongCat-Video-Avatar 1.6 1068.1 (open)** > 1.5 1051.8 > HeyGen 908.1 > OmniHuman-1.5 880.6 > Kling Avatar 2.0 854.7 — 1.6 beats its predecessor and commercial rivals.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18822) · [PDF](https://arxiv.org/pdf/2611.18822) · [Project](https://meigen-ai.github.io/LongCat-Video-Avatar-1.6-Page) · [Code](https://github.com/meituan-longcat/LongCat-Video-Avatar)

### 7.2 Mem2Fair: Online Fairness Control for Text-to-Video Generation via Fair Memory
**Mem2Fair：通过公平记忆实现文本到视频生成的在线公平性控制**

- **Authors / 作者:** Pengyu Chen, Jiaming Zhang, Xiaohua Feng, Yuyuan Li, Chaochao Chen
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify PDF)
- **Venue / 会议:** arXiv cs.CV / cs.AI (2026-11-14); no venue tag in metadata
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** T2V models produce unfair demographic outcomes when prompts omit protected attributes; training-based fixes need architecture access, sampling-based ones cost pre-deployment generation.
  - **Methodology:** First **conditional online approachability** formulation of attribute-level T2V fairness; **Mem2Fair** maintains concept-conditioned **Fair Memory**, using inference-time generated videos as feedback to select prompt-level attribute interventions based on deviation from fairness targets — no training, no separate pre-deployment sampling.
  - **Innovations:** Plug-and-play, online, training-free fairness control; works on black-box commercial T2V models.
- **Comparison & results / 对比与结果（author-reported）:** Consistently improves fairness over the unmodified generator and baselines across multiple attributes/settings/target distributions while keeping comparable prompt–video alignment and video quality.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19215) · [PDF](https://arxiv.org/pdf/2611.19215)

---

## 8. World Models & Games / 世界模型与游戏

### 8.1 WeatherDreamer: Learning a World Model from Multimodal Earth Observations
**WeatherDreamer：从多模态地球观测中学习世界模型**

- **Authors / 作者:** Kate Duffy, Elise Penn, Tristan Ballard, August Posch, Thomas J. Vandal
- **Affiliation / 机构:** **Zeus AI, Inc.** (Cambridge, Massachusetts)
- **Venue / 会议:** arXiv cs.LG (2026-11-13); no venue tag in metadata
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** ML weather models still depend on expensive data-assimilation (DA) analyses updated every 6h; observation-to-observation models omit the recursive filtering cycle.
  - **Methodology:** A world model learning the DA-like cycle end-to-end from **18 global observing systems without reanalysis**: infer latent state, carry it hourly with learned dynamics, correct hourly with new observations, predict what any observing system would measure anywhere.
  - **Innovations:** Jointly learns assimilation + forecasting from observations; separates viewing geometry from atmospheric state.
- **Comparison & results / 对比与结果（author-reported）:** At held-out stations, ensembles **beat NOAA GEFS** for temperature/dew point/wind out to **12h**, better calibrated than GEFS and ECMWF ensembles; infers precipitation/cloud-top height/solar irradiance at skill matching/exceeding operational products; recovers **83–96%** of observed limb darkening; **~1.5 min per hourly global analysis on one GPU**. Short-range departures within 10% of NOAA GSI at surface stations but up to 5× larger for temperature-sounding channels (limitation).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18393) · [PDF](https://arxiv.org/pdf/2611.18393)

### 8.2 V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations
**V-JEPA-LM：超越静态文本对齐表征、读取动态信息的视频–语言模型**

- **Authors / 作者:** Keuntae Kim, Dongjun Kim, Yong Suk Choi
- **Affiliation / 机构:** Hanyang University, Department of Computer Science (Seoul, Republic of Korea)
- **Venue / 会议:** arXiv cs.CV (2026-11-13); no venue tag in metadata
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** VLMs joined to world-model video encoders (V-JEPA) retrieve named attributes rather than "read" dynamics — a linear probe reads speed from frozen V-JEPA at 87% while the VLM answers at chance.
  - **Methodology:** Localizes dynamics in a **shared subspace** of predictive encoders (V-JEPA, not SigLIP); builds **counterfactual supervision** via pixel transformations producing answer-balanced video variants; single-stage training on **4.53M public samples**, 32 visual tokens/frame.
  - **Innovations:** Counterfactual dynamics-reading supervision; models 1B–8B (Qwen3/Llama).
- **Comparison & results / 对比与结果（author-reported）:** Leads every size class across **11 video benchmarks**; **4B model 72.1** vs. best open 4B **61.1** and best open 8B **64.8** (uses 9M–172M samples and 64–256 tokens/frame in prior work). Matched-budget counterfactual supervision adds **+4.5 points average, +38 on speed questions**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17831) · [PDF](https://arxiv.org/pdf/2611.17831) · [Code](https://github.com/kkt94/Llama-V-JEPA-LM)

### 8.3 SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation
**SceneAgent：面向可移植游戏场景生成的多智能体框架**

- **Authors / 作者:** Xingyi Li, Jiahao Yang, Yiqin Zhu, Jingwen Ye, Yang Sun, Weidong Zhang
- **Affiliation / 机构:** Not explicitly extractable from PDF (large-figure first page failed text extraction); verify PDF for institutions
- **Venue / 会议:** arXiv cs.AI (2026-11-13); no venue tag in metadata
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Moving a scene generator to a new game engine requires more than exporting output — planning, construction tools, and stored experience depend on the original backend.
  - **Methodology:** Multi-agent framework with a canonical **SceneContext** (persistent evolving world) + backend adapters; structured handoffs let fresh Builder sessions query persistent state without the full transcript; human-approved traces distilled into asset-ID-free **Layout skills** and semantic **Content skills**. Introduces **GameSceneBench** (69 indoor/outdoor prompts).
  - **Innovations:** Separates persistent scene state, task-local reasoning, and reusable experience for **portable** scene construction across engines.
- **Comparison & results / 对比与结果（author-reported）:** Human tie-adjusted preference **78.2–89.4%** against five baselines; ablations show reusable skills + multi-agent protocol mainly improve prompt alignment and scene completeness (with extra runtime); deployment in a second engine preserves the protocol/skill library.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17821) · [PDF](https://arxiv.org/pdf/2611.17821) · [Project](https://xingyi-li.github.io/sceneagent/)

---

## 9. LLM Training, Efficiency & Systems / LLM 训练、效率与系统

### 9.1 Supercharging Olmo-core for Efficient and Scalable MoE Training
**为高效可扩展 MoE 训练增强 Olmo-core**

- **Authors / 作者:** Tianhua Tao, Akshita Bhagia, Dirk Groeneveld, Pete Walsh, Tyler Romero, Yashas Samaga, Jacob Morrison, Iz Beltagy, Taira Anderson, Noah A. Smith, Hannaneh Hajishirzi
- **Affiliation / 机构:** **Allen Institute for AI (Ai2)**; University of Washington
- **Venue / 会议:** arXiv cs.LG (2026-11-13); technical report (169 pages)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** MoE training costs (bytes moved, memory, kernels) track *total* parameters, not active compute; on dense-oriented infrastructure, throughput falls as expert-parameter size grows.
  - **Methodology:** Redesigned Olmo-core: **DDP** (replacing FSDP) + Expert Parallelism + Pipeline Parallelism + distributed optimizer + activation recompute; **NVSHMEM-based rowwise EP** (direct token writes into expert buffers, no permutation); **synchronization-free EP** via GPU-resident routing metadata and device-scheduled grouped GEMMs; integrated **MXFP8**; topology-agnostic checkpoints.
  - **Innovations:** First highly efficient open MoE stack of this scale; identifies **Token Gerrymandering** (router hacks load-balancing loss) and shows overlap can slow kernels more than it hides.
- **Comparison & results / 对比与结果（author-reported）:** On **NVL8 B300 nodes**, supports **12.9B → 1.2T total parameters on up to 512 GPUs**, reaching **858 useful-model TFLOP/s/GPU at 1.2T with MXFP8** + per-layer recompute; experimental DeepEP v2 backend reaches **2.38T**.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.18956) · [PDF](https://arxiv.org/pdf/2611.18956)

### 9.2 A predictive, per-engine energy roofline of the Apple Neural Engine
**Apple 神经引擎的预测性逐引擎能耗屋顶线模型**

- **Authors / 作者:** Spencer H. Bryngelson
- **Affiliation / 机构:** The University of Texas at Austin, USA — **study *about* Apple hardware, not authored by Apple**
- **Venue / 会议:** **Accepted to ACM Transactions on Architecture and Code Optimization (TACO)** (arXiv comment; 40 pages, 36 tables)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** The Apple Neural Engine (ANE, 1B+ devices) is characterized only indirectly via CoreML; the consumer roofline (38 TOPS for M4) does not predict real ANE behavior.
  - **Methodology:** CoreML-free fused-graph dispatch (aneforge + Apple e5rt) enabling fair per-operator ANE/GPU/CPU dispatch with per-engine energy accounting on the same device.
  - **Innovations:** Discovers **two effective memory bandwidths** (slow activation path, fast weight-stream path) → two roofline ridges; int8 weight stream is dequantizer-element-rate bound; int4 LUT stream raises throughput at **−2.55 ImageNet top-1 points**.
- **Comparison & results / 对比与结果（author-reported）:** Corrected roofline bounds ANE from below and identifies lower-energy paths; constructed device map reproduces across **4 unique ANE generations**; operators should be placed by arithmetic intensity and fused.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19101) · [PDF](https://arxiv.org/pdf/2611.19101)

### 9.3 Superfluid: Local AI Server for Distributed LLM Inference
**Superfluid：面向分布式 LLM 推理的本地 AI 服务器**

- **Authors / 作者:** Prabod Rathnayaka, Isura Manchanayake, Srikandabala Kogul, Steve Siu, Fabian Waschkowski, Lukas Wesemann
- **Affiliation / 机构:** **Base Compute** (Melbourne, Australia)
- **Venue / 会议:** arXiv cs.LG (2026-11-13); open-source system (Apache-2.0)
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Local LLM serving is strained by (1) multiple agents sharing one device with an interactive user and (2) fragmented fleets of heterogeneous machines idling.
  - **Methodology:** Open-source server driving llama.cpp / MLX / BaseRT workers through one scheduler (interactive priority, shared-prompt compute-once, durable token log); across devices, one endpoint load-balances by measured speed with join/fail tolerance.
  - **Innovations:** Unified single-device multi-agent scheduling + cross-vendor fleet-as-one-endpoint serving.
- **Comparison & results / 对比与结果（author-reported）:** Qwen3.8-27B on Apple M5 Pro: first token in **1.5 s** while 8 agents work vs. **291–612 s** on llama-server/Ollama/mlx_lm.server. Six machines / 64 users / 1h: all **5,041 requests** answered, throughput **112 → 534 tok/s**, median TTFT **99 s → 12 s**. Twelve Mac Studio M3 Ultras: **10,656 tok/s** across **38,563 requests / 384 agents** with no failure.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.17753) · [PDF](https://arxiv.org/pdf/2611.17753) · [Code](https://github.com/basecompute/superfluid)

### 9.4 Understanding the Role of Reasoning Data in Pretraining
**理解推理数据在预训练中的作用**

- **Authors / 作者:** Jianhao Huang, Allan Zhang, Ali Payani, Baharan Mirzasoleiman
- **Affiliation / 机构:** Not explicitly specified in available metadata (verify PDF)
- **Venue / 会议:** arXiv cs.LG (2026-11-14); no venue tag in metadata
- **Abstract & key innovations / 摘要与关键创新:**
  - **Problem:** Reasoning traces cover only a subset of available facts; how should pretraining balance atomic facts vs. reasoning traces?
  - **Methodology:** Constructs a setting where every fact gives an atomic signal but only a subset appears in reasoning supervision; derives, for a linear transformer, the atomic-signal weight minimizing held-transition error (leading-order optimum **increases with reasoning-chain length**, **decreases with held-out fact fraction**); validates in full transformer + controlled multi-hop reasoning and math pretraining.
  - **Innovations:** Principled allocation rule for atomic facts vs. reasoning traces based on chain structure and coverage.
- **Comparison & results / 对比与结果（author-reported）:** Theoretical trends hold in full transformer layer (MLP + softmax attention + CE) and in two natural-language settings.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19042) · [PDF](https://arxiv.org/pdf/2611.19042)

---

## 10. Focus-org coverage in this edition / 本期重点机构覆盖

| Organization | Papers in this edition | Notes |
|---|---|---|
| **Meta AI / Meta Superintelligence Labs** | LogT (§2.1) | VLM visual-search SFT data engine, NeurIPS 2026. |
| **Microsoft Research** | iWSP (§6.2) | Interpretable weight-space programming with Jianfeng Gao. |
| **Amazon** | The Critic Can Hurt (§4.1) | Critic-safety audit for AutoML, KDD 2027 track. |
| **Alibaba** | G-CAST (§5.1), Omni-Workspace / Tongyi Lab (§6.1) | Deployed 1688 B2B agent; omni-modal benchmark. |
| **NVIDIA** | Nahual (§2.4, co-author) | Sequence model for language + atoms, NeurIPS 2026. |
| **Meituan (LongCat)** | LongCat-Video-Avatar 1.6 (§7.1) | Open-source audio-driven avatar video, >10 min. |
| **Allen Institute for AI (Ai2)** | Olmo-core MoE (§9.1) | Open scalable MoE training stack up to 1.2T params. |
| **Apple** | ANE roofline (§9.2) | *About* Apple Silicon, authored at UT Austin (TACO). |
| **Huawei** | Agent-as-a-Judge (§6.3, co-author) | Active-evaluator survey. |
| **Google / Anthropic / OpenAI** | GDP.xlsx (§6.5, evaluated models) | Benchmarked, not authors, in this edition. |
| ByteDance, Tencent, Kuaishou, Baidu, Netflix, OpenAI (first-party), Google DeepMind (first-party), Anthropic (first-party) | — | **No first-party paper surfaced in this fresh window**; sibling 2026-11-17 `arxiv-paper-check` covers Tencent/WeChat ads (TokenFormer V2) and Meta (CLEAR). |

---

## 11. Limitations & flags

- **Venue crawl incomplete:** web search was cancelled; proceedings/OpenReview pages for the exact requested venues could not be freshly crawled. NeurIPS 2026 tags dominate; the requested 2025/2026 venues are represented only where a fresh arXiv tag was found (ICML 2026, KDD 2027-forward, WAMTA 2027-forward, IEEE BigData 2026, TACO, Agent Evaluation Science Symposium).
- **Forward-dated tags:** KDD 2027, WAMTA 2027, EACL 2027, WACV 2027 etc. are reported as written in arXiv comments — they are *not* the requested 2025/2026 venues and should be treated as author-claimed status.
- **Affiliation gaps:** 3 papers (VLAN, KnowVis, SST, plus Mem2Fair / reasoning-data / SceneAgent) lacked explicit affiliations in extractable metadata; verify PDFs before citing institutions. Focus-org attributions were PDF-verified (Meta MSL, Amazon, Alibaba, NVIDIA, Microsoft Research, Meituan, Ai2, Huawei, Surge AI); "Apple/NVIDIA" mentions in two titles were confirmed to be *subjects*, not author affiliations.
- **No hallucinated metrics:** all numbers are quoted from arXiv abstracts / page-1 PDF text. Where full experimental tables were unavailable (e.g. Neural Dual Bounds), this is stated rather than invented.
- **BM25:** not rebuilt (search index optional per `EXTEND.md`; no `scripts/wiki_fts.py` rebuild requested). Navigation via `wiki/index.md` and text search remains available.
