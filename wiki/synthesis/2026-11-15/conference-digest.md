---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-15 Daily Edition"
type: synthesis
created: 2026-11-15
updated: 2026-11-15
sources: [arXiv recent listings cs.IR/cs.CL/cs.LG/cs.CV, arXiv abstracts (2611.16795,2611.16053,2611.16000,2611.12180,2611.11013,2611.15426,2611.16433,2611.17294,2611.16956), ICML 2026 virtual site, ICLR 2026 virtual site, AAAI 2026 site, prior wiki conference digests]
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-15 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-15 每日版）

> Daily curated digest covering requested venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) and recent arXiv papers in AI, LLMs, recommendation systems, advertising, CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks.
>
> **Method & limitations (2026-11-15):** Compiled from arXiv recent listings and abstract pages (`cs.IR`, `cs.CL`, `cs.LG`, `cs.CV`) retrieved 2026-11-15, plus limited conference-site checks (ICML/ICLR 2026 virtual paper pages are JavaScript-rendered and did not yield machine-readable accepted-paper lists in this run; AAAI 2026 accepted-papers URL returned 404). The `websearch` integration was unavailable. Venue sections therefore combine (a) a status snapshot, (b) recent arXiv papers with explicit venue/workshop comments where available, and (c) recent industrial/research papers relevant to requested topics and target labs/companies. **All metrics/results are author-reported unless noted.** Affiliations are reported as stated in arXiv metadata/abstract text when available; when not explicitly listed, this is noted (with deployment/company context only when explicitly stated by authors).

---

## 1. Venue Snapshot (requested conferences)

| Venue | Status (as of 2026-11-15 digest) | Notes |
|---|---|---|
| **ICML 2026** (Seoul, Jul 6–12, 2026) | Program/awards announced; full accepted-paper crawl not refreshed this run | Virtual papers page is dynamic/JS-rendered in this environment. Prior wiki digests cover flagship highlights (e.g. diffusion LM sampling theory, A3C test-of-time). |
| **AAAI 2026** (Singapore, Jan 20–27, 2026) | Conference completed; accepted-papers list not directly retrieved (404 on attempted path) | No newly verified AAAI-2026 main-track paper extracted today; IAAI/industry items may appear on arXiv with comments. |
| **NeurIPS 2025** (San Diego + Mexico City, Dec 2–7, 2025) | Completed; proceedings not re-crawled | NeurIPS 2026-tagged papers/workshop items are appearing on arXiv (see below). |
| **ICLR 2026** (Rio, Apr 28–May 2, 2026) | Program/awards announced; full crawl not refreshed | Virtual papers page dynamic in this environment. |
| **KDD 2026** | No fresh accepted-paper crawl this run | Industrial recommendation/ads/CTR systems continue to appear on arXiv (e.g. Taobao Shangou generative ad retrieval). |
| **CVPR 2026** | No fresh crawl this run | Vision/generative multimodal papers in today’s scan mostly arXiv preprints without confirmed CVPR tags. |
| **ACL 2026** | No fresh crawl this run | No newly verified ACL-2026-tagged paper added today. |
| **EMNLP 2025** | Completed; not re-crawled | Prior wiki coverage remains reference. |
| **SIGIR 2026** | Workshop signals visible on arXiv in recent days | e.g. ReNeuIR @ SIGIR 2026 items appeared in recent listings (see prior digests). |
| **WWW 2026** | No fresh crawl this run | Gap noted. |
| **CIKM 2025** | Completed | CIKM 2026-tagged recsys explanation work appeared recently (see prior digests). |
| **RecSys 2025** | Completed; RecSys 2026 workshop papers visible on arXiv | DaQuaMRec/RecSys workshop-tagged POI/recsys work appeared recently. |

---

## 2. NeurIPS 2026 (accepted/tagged on arXiv) — Recommendation, Agents, Vision, Benchmarks
## NeurIPS 2026（arXiv 标注/接收）— 推荐、智能体、视觉与基准

### 2.1 KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and Multi-task Recommendation
**KuaiRecV2：面向多样化与多任务推荐的大规模持续学习基准**

- **Authors:** Chenxu Li, Shuchang Liu, Hantao Shu, Wei Yuan, Zhe Xu, Guoqing Hu, Yan Wang, Biao Yang, Xiang Li, Cheng Ling, Fan Yang, Yongqi Liu, Lantao Hu, Han Li, Kaiqiao Zhan, Kun Gai, An Zhang, Xiang Wang
- **Affiliation (company/institution):** Affiliations not individually enumerated in arXiv metadata; dataset/context stated as **industrial-level data from Kuaishou** (快手) in abstract.
- **Venue/conference:** **Accepted to NeurIPS 2026** (arXiv comment), arXiv preprint cs.IR, 2026-11-12 (v1)
- **Abstract and key innovations:**
  - **Problem background:** Offline recommender evaluation often diverges from complex online outcomes. Key gaps include (1) large-scale continual learning under dynamic item pools/distribution shifts, (2) combinatorial accuracy-diversity trade-offs at token and item levels, and (3) multi-task reward balancing for generative models that model sequences well but are hard to control for multi-objective demands.
  - **Methodology/benchmark design:** **KuaiRecV2** provides a large-scale industrial interaction dataset with million-scale multimodal item information and long-term interaction records across **30 days** with a dynamic video candidate pool. It introduces a unified evaluation rubric for retrieval accuracy, diversity, and multi-task performance.
  - **Key innovations:** A realistic benchmark where an effective method must improve all rubric dimensions (not trade one off silently), explicitly targeting continual learning, token/item-level diversity, and multi-task controllability in modern/generative recommendation.
- **Comparison with prior methods / experimental results (author-reported):**
  - The paper positions KuaiRecV2 against simpler offline setups by emphasizing dynamic pools, long-term shifts, and joint metrics; detailed baseline numbers and leaderboard comparisons are provided in the paper/benchmark resources (see PDF/code). The core claim is a more faithful evaluation protocol for real-world recommendation progress.
  - Code: https://github.com/cxli2333/KuaiRecV2
- **arXiv/PDF:** https://arxiv.org/abs/2611.16795 · https://arxiv.org/pdf/2611.16795

### 2.2 Wayfinder: Adaptive Resource Routing from Agent Citations
**Wayfinder：基于智能体引用的自适应资源路由**

- **Authors:** Miguel Romero, George Karypis
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** **Accepted to NeurIPS 2026** (arXiv comment), arXiv preprint cs.LG/cs.IR, 2026-11-11 (v1)
- **Abstract and key innovations:**
  - **Problem background:** Agents must find information across heterogeneous resources (chat, issue trackers, email, knowledge bases) without knowing where answers live; static tool descriptions often fail for overlapping resources and cannot learn from interactions.
  - **Methodology:** **Wayfinder** is an adaptive router that uses documents cited by downstream agents as feedback to update internal resource representations and prioritize likely-relevant resources in future interactions. Uses **resource augmentation** during offline RL (anonymize/permute resource identities) to reduce overfitting to training environments.
  - **Key innovations:** Citation-driven closed-loop routing adaptation; controlled testbeds (**NFCorpus, FEVER, Tech Startup**) pairing realistic queries with resource-access patterns.
- **Comparison with prior methods / experimental results (author-reported):**
  - Under a shared closed-loop protocol, Wayfinder outperforms supervised, tool-retrieval, and contextual bandit baselines when resources are semantically overlapping and static descriptions are insufficient.
  - Description-based tool retrieval remains sufficient when resources come from distinct corpora; augmentation helps most with few training environments (ablations in paper).
- **arXiv/PDF:** https://arxiv.org/abs/2611.16053 · https://arxiv.org/pdf/2611.16053

### 2.3 Predicting the Needle in a Petabyte Scale Haystack: Open-Vocabulary Event Anticipation in Satellite Imagery
**在 PB 级大海中预测“针”：卫星影像中的开放词汇事件预测**

- **Authors:** Shreelekha Revankar, Mikhail Klassen, Creon Levit, Ash Hoover, Kavita Bala, Bharath Hariharan
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata (authors include researchers associated with academic vision labs in prior work; verify affiliations in PDF).
- **Venue/conference:** **To be published in NeurIPS 2026** (arXiv comment), arXiv preprint cs.CV/cs.IR, 2026-11-11 (v1)
- **Abstract and key innovations:**
  - **Problem background:** Daily global satellite imagery captures event lifecycles (deforestation, urban construction), but anticipating where/what/when an event will complete across open vocabulary is challenging and annotation is infeasible at scale.
  - **Methodology:** Represents change as vector difference between vision-language model embeddings at different times, enabling latent-space search for semantic transformations. Builds (1) automated data engine for global event discovery, (2) large dataset (21,000+ locations, 64+ event types, ~2M images from PlanetScope/Sentinel-2, six continents), and (3) global-scale event anticipation model.
  - **Key innovations:** Embedding-arithmetic change representation for scalable discovery and open-vocabulary anticipation (detection + retrieval + completion forecasting).
- **Comparison with prior methods / experimental results (author-reported):**
  - Change detection: **93.5% max F1**.
  - Predicted event retrieval: **3.6×** improvement over baselines.
  - Completion-date forecasting: **3-day median error**, even **nine months** before completion.
  - Code: https://github.com/ShreelekhaR/predicting-the-needle
- **arXiv/PDF:** https://arxiv.org/abs/2611.16000 · https://arxiv.org/pdf/2611.16000

### 2.4 Slim Foundation Models for Latency-Critical Recommendation Serving (SlimFM)
**面向低延迟关键推荐服务的轻量基础模型（SlimFM）**

- **Authors:** Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** **NeurIPS 2026 Workshop — Long Context Foundation Model** (journal-ref on arXiv), arXiv preprint cs.IR/cs.AI, 2026-11-07 (v1)
- **Abstract and key innovations:**
  - **Problem background:** LLMs improve CTR prediction (especially cold-start/long-tail) but are too expensive for online serving; prior LLM-enhanced CTR often caches outputs offline.
  - **Methodology:** **SlimFM**: (1) dependency-aware structured pruning compresses **LLaMA3-8B → 4.5B** (44% reduction); (2) LoRA-based field-aware fine-tuning produces discriminative field-level semantic embeddings from lightweight prompts; (3) semantic-guided fusion injects embeddings into conventional CTR model feature interactions.
  - **Key innovations:** Practical online LLM semantic modeling for latency-critical CTR via pruning + field-aware adaptation + fusion.
- **Comparison with prior methods / experimental results (author-reported):**
  - Across **4 datasets and 6 CTR backbones**: retains **>99%** of uncompressed-model accuracy.
  - Reduces inference latency by **up to 3.4×** relative to existing LLM-enhanced baselines.
- **arXiv/PDF:** https://arxiv.org/abs/2611.11013 · https://arxiv.org/pdf/2611.11013

---

## 3. Advertising, CTR & Industrial Recommendation Systems (Recent arXiv)
## 广告、CTR 与工业推荐系统（近期 arXiv）

### 3.1 TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
**TS-GEAR：淘宝闪购生成式广告检索**

- **Authors:** Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Affiliation (company/institution):** **Taobao Shangou / Alibaba ecosystem** (deployment stated in Taobao Shangou search advertising pipeline; individual affiliations not enumerated in arXiv metadata).
- **Venue/conference:** arXiv preprint cs.IR/cs.AI/cs.CL, 2026-11-09 (v1)
- **Abstract and key innovations:**
  - **Problem background:** On-demand delivery ads have hard geographic reachability constraints (merchants outside delivery range are invalid), query/location-dependent preferences, and set-level redundancy issues in autoregressive generative retrieval.
  - **Methodology:** (1) **Geo-Semantic ID** splits IDs into geographic prefixes + semantic suffixes so reachability becomes a prediction target; (2) **Query-Geo Target Attention** conditions history aggregation on real-time query/location and encodes behavior location in keys; (3) **GMPO (Group Marginal Policy Optimization)** uses deduplicated group rewards/marginal advantages within GRPO to discourage near-duplicates without auxiliary diversity objectives.
  - **Key innovations:** Differentiable geographic validity, geo/query-aware interest modeling, and set-level optimization for generative ad retrieval.
- **Comparison with prior methods / experimental results (author-reported):**
  - Deployed online with **0.1B backbone**, serving **>150M queries/day** in Taobao Shangou search advertising.
  - Consistently outperforms state-of-the-art generative retrieval methods on **HitRate** and **geographic validity**.
  - Online gains: **+3.8% ad impressions, +4.2% ad revenue**.
- **arXiv/PDF:** https://arxiv.org/abs/2611.12180 · https://arxiv.org/pdf/2611.12180

---

## 4. LLMs, Agent Systems & Code/Execution Prediction (Recent arXiv)
## 大语言模型、智能体系统与代码/执行预测（近期 arXiv）

### 4.1 daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving
**daVinci-Prover：面向形式化定理证明的智能体原生中期训练**

- **Authors:** Wenhong Zhu, Xuefeng Li, Jiashuo Zhang, Yu Chen, Tiantian Mi, Qipeng Guo, Pengfei Liu
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata.
- **Venue/conference:** arXiv preprint cs.CL, 2026-11-12 (v1)
- **Abstract and key innovations:**
  - **Problem background:** Progress in LLM-based theorem proving is constrained by lack of transparent, effective data recipes combining mathematical priors and long-horizon interactive proof construction.
  - **Methodology:** Synthesizes an **agent-native 33.7B-token mid-training corpus** (decomposition, search, self-verification, revision) plus verifier-grounded agentic trajectories. Introduces **daVinci-Prover harness** for isolated Lean verifier interaction and collects ~**36K** high-quality agent trajectories for SFT.
  - **Key innovations:** Agent-native mid-training + verifier-grounded trajectories + interactive proving harness for stronger agentic provers.
- **Comparison with prior methods / experimental results (author-reported):**
  - Average improvement of **+13.7 points** over matched **Qwen3-8B SFT-only** baseline across **MiniF2F, FATE-M, ProofNet**.
  - Applied to **Qwen3.5** series: strong theorem-proving performance and **near-saturating MiniF2F** with memory compaction.
- **arXiv/PDF:** https://arxiv.org/abs/2611.16433 · https://arxiv.org/pdf/2611.16433

### 4.2 Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon
**Metal Sandbox：面向 Apple Silicon 上 GPU 编码智能体的隔离执行与命令调度**

- **Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, Zheng Ge, Daxin Jiang, Junchi Yan
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata (authors include researchers active in LLM/agent systems; verify affiliations in PDF).
- **Venue/conference:** arXiv preprint cs.LG/cs.AI/cs.CL/cs.DC, 2026-11-12 (v1)
- **Abstract and key innovations:**
  - **Problem background:** Generating efficient Apple Metal kernels for on-device inference benefits from native macOS tools and concurrent agent sessions, but agent rollouts alternate between model requests, dev commands, and GPU execution, leaving GPU capacity idle.
  - **Methodology:** **Metal Sandbox** provides restricted per-instance file access, native command execution, and command-level scheduling across interconnected Macs. Parallel commands run concurrently; serial commands share one execution slot per node; eligible waiting commands can migrate to available Macs. Integrated with **Harbor** for task execution, verification, and rollout collection.
  - **Key innovations:** Infrastructure for efficient training/evaluation of GPU coding agents on Apple Silicon clusters with isolation and cross-node scheduling.
- **Comparison with prior methods / experimental results (author-reported):**
  - Controlled experiments on **4 Mac mini M4 nodes**: **1.68×–2.05×** command throughput gains under concentrated demand.
  - Sixteen static agent traces: estimated **2.14×** sustained-throughput gain for four sessions/node vs one (assumptions stated).
  - Dynamic scheduling replay: **18.8%** reduction in mean tool waiting and **22.3%** reduction in batch elapsed time (assumptions stated).
  - Code: https://github.com/WangHaoZhe/metal-sandbox and https://github.com/WangHaoZhe/harbor
- **arXiv/PDF:** https://arxiv.org/abs/2611.17294 · https://arxiv.org/pdf/2611.17294

### 4.3 SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction
**SimRec：从模拟交互中学习搜索、提问与推荐**

- **Authors:** Yaxin Zhang, Xingyu Wu, Yuchen Yan, Yuqin Dai, Hong Zhao, Lixing Shen, Zhan Chen, Jian Shao, Yongliang Shen
- **Affiliation (company/institution):** Not explicitly listed in arXiv metadata (code hosted under ZJU-REAL; verify author affiliations in PDF).
- **Venue/conference:** arXiv preprint cs.CL/cs.AI/cs.IR, 2026-11-11 (v1)
- **Abstract and key innovations:**
  - **Problem background:** LLM-based recommendation agents can search, inspect, ask, and revise, but behaviors are often hand-designed and training typically optimizes isolated components rather than full interaction policy.
  - **Methodology:** **SimRec** (RL framework) trains the full tool-integrated recommendation agent policy with: (1) task-anchored user simulator providing feedback on every recommendation (conditioned on task need; external LLM or self-play), and (2) task-aligned reward optimized over whole trajectory with **GRPO**, crediting retrieval quality and valid tool use plus final hit, with training-only target injection for sparse hits.
  - **Key innovations:** End-to-end policy learning for agentic recommendation over multi-turn tool use and interaction recovery.
- **Comparison with prior methods / experimental results (author-reported):**
  - On **ESCI** and **Amazon C4**: **NDCG@100** improves from **32.23% → 35.42%** and **22.94% → 24.72%** for a **Qwen3-4B** agent.
  - Outperforms training-free agents on far larger backbones and task-aligned baselines on NDCG.
  - Analysis: trained agent more often verifies candidates, uses preferences, and recovers from rejected recommendations.
  - Code: https://github.com/ZJU-REAL/SimRec
- **arXiv/PDF:** https://arxiv.org/abs/2611.15426 · https://arxiv.org/pdf/2611.15426

### 4.4 Lara Mini Base: Language Diversity as a Resource, Not a Trade-off
**Lara Mini Base：语言多样性是资源而非权衡**

- **Authors:** Translated (company) and collaborators (large author list; see arXiv page/PDF)
- **Affiliation (company/institution):** **Translated** (company-led model release; full contributor list in arXiv metadata).
- **Venue/conference:** arXiv preprint cs.CL/cs.AI, 2026-11-12 (v1)
- **Abstract and key innovations:**
  - **Problem background:** Most general-purpose LMs are English-heavy; European-language-focused small models often underperform same-size general models, raising concerns about capacity competition among languages.
  - **Methodology:** **Lara Mini Base** trained from scratch on **6T tokens** in English + **44 other languages** (covering all 24 EU official languages), with non-English share growing over training. **MoE architecture** with **7.2B total / 0.6B active** parameters; **128k** context.
  - **Key innovations:** Multilingual-first scaling/data mix with sparse MoE to reduce language capacity competition while maintaining efficiency.
- **Comparison with prior methods / experimental results (author-reported):**
  - Among open base models with **up to 2B active parameters**, highest average score across standard English, multilingual, math, and code benchmarks; ahead of models trained on **4–6×** more tokens.
  - Largest margins on multilingual benchmarks in supported languages and on math benchmarks.
  - For single-user single-GPU inference (no quantization), generates text **≥1.8× faster** than any model with higher average score.
  - Weights: https://huggingface.co/translated/Lara-4-Mini-Base (license as stated by authors: CC BY-NC-SA 4.0).
- **arXiv/PDF:** https://arxiv.org/abs/2611.16956 · https://arxiv.org/pdf/2611.16956

---

## 5. Games, Sequential Modeling & Generative Models — Coverage Note
## 游戏、序列建模与生成模型 — 覆盖说明

- **Games / game agents / RL in games:** No clearly venue-tagged, high-confidence new game-playing/RL-for-games paper from the target companies was extracted in today’s limited arXiv+site scan. Related adjacent work appears in agent systems and world/event modeling (e.g. satellite event anticipation as temporal/generative forecasting in Section 2.3), but dedicated game benchmarks/agents should be refreshed in the next crawl with broader `cs.AI`/`cs.MA` and proceedings search.
- **Sequential modeling:** Sequential/user-trajectory and continual recommendation themes are represented by **KuaiRecV2** (long-term 30-day dynamics, continual learning) and **SimRec** (multi-turn interaction policy). Additional POI/sequential papers appeared in recent days in prior digests (e.g. LUMIR/SHARP context in 2026-11-12/13 digests).
- **Generative models:** Generative retrieval/recommendation and agentic generation are covered by **TS-GEAR** (generative ad retrieval) and **KuaiRecV2** (generative recommendation evaluation challenges); vision-language generative/anticipative modeling appears in Section 2.3.

---

## 6. Daily Notes: Focus Labs/Companies & Gaps

- **Target-company relevance observed:** **Kuaishou** (KuaiRecV2 dataset/context), **Alibaba/Taobao Shangou** (TS-GEAR deployment). Other papers involve strong academic/industry-adjacent teams but do not explicitly list the requested companies in arXiv metadata; affiliations should be verified from PDFs for precise attribution.
- **Requested companies with limited/no fresh verified papers in this run:** Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Tencent, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon. This may reflect retrieval limits (no websearch, dynamic proceedings pages) rather than absence of work; recommend a follow-up crawl of official proceedings/OpenReview/company research pages.
- **Benchmarks highlighted:** KuaiRecV2 (continual/diverse/multi-task recommendation), NFCorpus/FEVER/Tech Startup routing testbeds in Wayfinder, MiniF2F/FATE-M/ProofNet in daVinci-Prover, ESCI/Amazon C4 in SimRec, large-scale satellite event dataset in NeurIPS 2026 vision work.

---

*Compiled on 2026-11-15 for `wiki/synthesis/2026-11-15/conference-digest.md`. Preference file active: `EXTEND.md` (repo root, bm25 mode `auto_prompt`).*
