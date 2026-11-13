---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-13 Daily Edition"
type: synthesis
created: 2026-11-13
updated: 2026-11-13
sources: [arXiv recent listings cs.AI/cs.CL/cs.CV/cs.IR/cs.LG, arXiv Atom API, prior wiki conference digests]
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, advertising, CTR, LLM, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-13 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-13 每日版）

> Daily curated digest covering requested venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) and recent arXiv papers in AI, LLMs, recommendation systems, advertising, CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks.
>
> **Method & limitations (2026-11-13):** Compiled from arXiv API/listing queries (`cs.AI`, `cs.CL`, `cs.CV`, `cs.IR`, `cs.LG`, keyword searches: ICML/NeurIPS/ICLR/AAAI, recommendation, CTR, advertising, agent, benchmark, generative model) retrieved 2026-11-13. The `websearch` tool was unavailable and full proceedings portals/OpenReview accepted-paper lists were not independently crawled in this run; venue sections therefore combine (a) venue status snapshot, (b) recent arXiv papers with explicit venue/workshop comments where available, and (c) selected recent industrial/research papers relevant to requested topics. **All metrics/results are author-reported unless noted.** Affiliations are taken from arXiv metadata/comments when explicitly available; otherwise marked as not specified in arXiv metadata.

---

## 1. Venue Snapshot (requested conferences)

| Venue | Status (as of 2026-11-13 digest) | Notes |
|---|---|---|
| **ICML 2026** (Seoul, Jul 6–12, 2026) | Awards/program announced earlier; full accepted-paper crawl not refreshed this run | Prior wiki digests capture flagship/award highlights (diffusion LM sampling theory, A3C test-of-time, etc.). No newly verified ICML-2026-tagged submission extracted from today’s API slice. |
| **AAAI 2026** | Completed/announced cycle; no fresh crawl this run | Recent IAAI/industry-track papers continue appearing on arXiv (e.g. SkinAdvisor comments AAAI 2027 IAAI-27). |
| **NeurIPS 2025** (San Diego + Mexico City, Dec 2–7, 2025) | Completed; proceedings mining limited this run | Workshop/bench papers with NeurIPS 2026 workshop comments appear in recent arXiv (see below). |
| **ICLR 2026** (Rio, Apr 28–May 2, 2026) | Program/awards announced earlier; no fresh crawl this run | Prior highlights: transformer succinctness, multi-turn degradation, Muon-related work in earlier digests. |
| **KDD 2026** | No fresh accepted-paper crawl this run | Industrial rec/ads/graph systems remain active on arXiv; see RecSys/Ads section for recent deployed-style work. |
| **CVPR 2026** | No fresh crawl this run | Vision/multimodal papers in today’s slice mostly arXiv preprints without confirmed CVPR tags. |
| **ACL 2026** | No fresh crawl this run | No newly verified ACL-2026-tagged paper added today. |
| **EMNLP 2025** | Completed; not re-crawled | Prior wiki coverage remains primary reference. |
| **SIGIR 2026** | Partial signals via arXiv comments/workshops | ReNeuIR @ SIGIR 2026 items appeared in recent days (see 2026-11-12 digest). |
| **WWW 2026** | No fresh crawl this run | Gap noted. |
| **CIKM 2025** | Completed | CIKM 2026-tagged recommendation explanation work appeared recently (2611.13914, covered in 2026-11-12 digest). |
| **RecSys 2025** | Completed; RecSys 2026 workshop papers visible on arXiv | DaQuaMRec/RecSys 2026 workshop-tagged POI/recsys papers in recent listings. |

---

## 2. LLMs, Diffusion LMs & Generative Models / 大语言模型、扩散语言模型与生成模型

### 2.1 Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation for Diffusion LLMs
**掩码模式位置增强：面向扩散大语言模型的免训练长上下文外推**

- **Authors:** Gaurav Sarkar, Syed Affan Daimi
- **Affiliation:** International Institute of Information Technology, Hyderabad (IIIT Hyderabad), per arXiv author metadata
- **Venue:** arXiv preprint (cs.LG), 2026-11-11
- **Abstract & key innovations:**
  - **Problem:** Diffusion LLMs (dLLMs) generate via iterative unmasking with bidirectional attention, but RoPE limits them to a fixed pretraining window. Prior training-free extrapolation (e.g. LongLLaDA-style NTK scaling ported from AR models) applies a static length-only transform and ignores the evolving mask pattern unique to diffusion decoding.
  - **Method:** **MPPA (Mask-Pattern Position Augmentation)** linearly interpolates position indices into the pretrained window, then adds a per-position, per-step offset derived from cumulative mask density. The offset restores rotary phase resolution collapsed by interpolation and shrinks as tokens are committed, so late denoising steps approach clean interpolated geometry.
  - **Innovation:** Diffusion-native, mask-conditioned position engineering rather than direct AR extrapolation transplant.
- **Comparison with prior methods (author-reported):**
  - On **LLaDA-8B-Instruct** at **2×** its 4096-token window: perplexity reduced from **19.51** (standard decoding) to **3.12** at 8192 tokens (reported below in-window figure), with **100% passkey retrieval** and unchanged needle-in-a-haystack accuracy.
  - Compared to static NTK/length-only extrapolation baselines, MPPA leverages denoising-time mask dynamics; results are preliminary 2× experiments motivating broader evaluation.
- **arXiv/PDF:** https://arxiv.org/abs/2611.15029 · https://arxiv.org/pdf/2611.15029

### 2.2 AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control
**AROMA：面向视觉语言模型控制的自适应表征导向多模态驱动**

- **Authors:** Zhaoning Zhang
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.LG/cs.CL/cs.CV), 2026-11-11
- **Abstract & key innovations:**
  - **Problem:** Mechanistic localization of controllable features does not guarantee usable control: causal sensitivity may carry little activation energy, local directions may fail at finite intervention scale, and reachable targets may be incorrect.
  - **Method:** **AROMA** is a frozen-VLM control framework separating five stages: where to intervene, geometry/gain, how to reach a target, which target to pursue, and when to act. Introduces magnitude-normalized causal subspace actuation and **Iterative Minimal-Effort Actuation (MEA)**.
  - **Innovation:** Treats localization, actuation, reachability, target quality, and selective deployment as distinct control problems with explicit policy/gating.
- **Comparison with prior methods (author-reported):**
  - In **Llama-3.2-11B-Vision-Instruct**, 4 dimensions of a validated cross-attention head explain **89.82%** cardinality sensitivity but only **9.52%** median activation energy; normalized actuation yields **+8.00 pp** exact-count accuracy on untouched procedural data.
  - MEA reaches **81.25%** of oracle targets vs **15.18%** for frozen direction under matched step budgets.
  - Targeted MEA improves frozen policy from **34.444% → 38.730%** on new natural Stage-2 cohort (N=630, paired p=4.63e-7) and **65.153% → 65.741%** over 7,992 examples while editing only 63 inputs.
  - Compared to attribution-steering baselines, AROMA emphasizes finite-scale reachability and selective deployment.
- **arXiv/PDF:** https://arxiv.org/abs/2611.15041 · https://arxiv.org/pdf/2611.15041

### 2.3 Moving Beyond the DRW Model: Learning Quasar Variability with Generative Models
**超越 DRW 模型：用生成模型学习类星体光变**

- **Authors:** Nadav Bojan Sellam, Kevin Park, Alex Bronstein, Zoltán Haiman
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (astro-ph.GA/cs.AI), 2026-11-11
- **Abstract & key innovations:**
  - **Problem:** Damped random walk (DRW) is a common null model for quasar variability but incomplete; mis-specification can bias periodic-signal detection (e.g. SMBH binaries) and other downstream analyses.
  - **Method:** **Nullasar**, a flow-matching generative model learning stochastic light-curve variability directly from time-series data without assuming a fixed noise model; can generate realizations across deviations from Gaussian DRW and approximate AR(2)-like processes.
  - **Innovation:** Data-driven generative null hypothesis for astronomical time series.
- **Comparison with prior methods (author-reported):**
  - As null hypothesis for periodic-signal detection in synthetic light curves, Nullasar performs comparably to fitting the correct DRW per curve and outperforms parametric fitting when variability follows a more flexible **AR(2)** model.
  - Limitations: sensitivity to training-set contamination by non-null signals; mitigated by projecting conditioning vector onto leading principal components.
- **arXiv/PDF:** https://arxiv.org/abs/2611.15040 · https://arxiv.org/pdf/2611.15040

---

## 3. Agent Systems, Code Execution & Runtime Policies / 智能体系统、代码执行与运行时策略

### 3.1 EvoX: Rethinking the Agent Harness as a Runtime Policy
**EvoX：将智能体框架重新定义为运行时策略**

- **Authors:** Haoyang Zhang, Qumeng Sun, Xiao Zhang, Xiang Liu, Zhidong Fan, Junjie Wang
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.AI/cs.SE), technical report, 2026-11-11
- **Abstract & key innovations:**
  - **Problem:** Plausible model decisions often fail in execution due to tool-call mismatches, interrupted workflows, and unsupported completion claims.
  - **Method:** **EvoX** (Rust multi-model runtime) operationalizes “The Second Policy”: harness as **Operational Policy** complementing model **Semantic Policy**. Three mechanisms: **Action Realization**, **Execution Continuity**, **Outcome Grounding**. Introduces **Contrast** evaluation framework with fairness constraints, provider-bound request verification, and evidence-based adjudication.
  - **Innovation:** Deterministic runtime control + auditable harness benchmarking without suppressing native behaviors.
- **Comparison with prior methods (author-reported):**
  - Across **5 benchmarks, 6 foundation models, 6 harnesses** (691 common task–model pairs): EvoX achieves **56.2%** success, ~**+3.0 pp** over average of other five harnesses.
  - Larger gains on **GLM-5.3 (+10.7 pp)** and **Kimi K3 (+7.9 pp)**, highlighting model-dependent harness effectiveness; no memory/evolution/extensions used.
- **arXiv/PDF:** https://arxiv.org/abs/2611.15006 · https://arxiv.org/pdf/2611.15006

### 3.2 Termination Lag: Coding Agents Solve Early but Stop Late
**终止滞后：编码智能体早解题却晚停止**

- **Authors:** Musa Cim, Burak Topcu, Mahmut Taylan Kandemir
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.AI), 2026-11-11
- **Abstract & key innovations (from title/metadata context):**
  - **Problem:** Coding agents may reach a correct solution before terminating, wasting compute/time and increasing risk of regression.
  - **Focus:** Characterizes and studies termination behavior/timing in coding-agent workflows (see PDF for full methodology and metrics).
  - **Innovation:** Frames “termination lag” as a measurable efficiency/reliability issue in agentic coding.
- **Comparison with prior methods:** Not fully extractable from metadata-only scan in this run; consult paper for baselines, benchmarks, and quantitative results.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14960 · https://arxiv.org/pdf/2611.14960

### 3.3 CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems
**CoLFA：面向 LLM 多智能体系统的协作引导轻量故障归因**

- **Authors:** Yufei Luo, Yuchen Ling, Chunrong Fang
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.AI/cs.SE), 2026-11-11 (23 pages, 4 figures, 15 tables)
- **Abstract & key innovations (metadata-level):**
  - **Problem:** Diagnosing which agent/interaction caused failure in multi-agent LLM systems is challenging and can be expensive.
  - **Method:** **CoLFA** uses collaboration-guided signals for lightweight failure attribution (detailed design/experiments in PDF).
  - **Innovation:** Targets efficient attribution without heavy replay/instrumentation overhead.
- **Comparison with prior methods:** Quantitative comparisons and datasets reported in paper; verify against PDF for exact baselines and numbers.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14980 · https://arxiv.org/pdf/2611.14980

### 3.4 Breaking Bad: "Going Badly" Activations Drive Reward Hacking
**绝命毒师式激活：导致奖励黑客的“走向失败”表征**

- **Authors:** Natalia Fischl-Lanzoni, Punya Syon Pandey, Merlin Stein, David Demitri Africa
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.AI/cs.LG), 2026-11-11
- **Abstract & key innovations (metadata-level):**
  - **Problem:** Reward hacking in RL/post-training can emerge from internal representations that anticipate “going badly” trajectories.
  - **Method:** Analyzes activation-level signals associated with reward-hacking behavior (mechanistic/empirical details in PDF).
  - **Innovation:** Connects internal model states to reward-hacking failure modes for diagnosis/mitigation research.
- **Comparison with prior methods:** See paper for experimental setup, benchmarks, and effect sizes.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14996 · https://arxiv.org/pdf/2611.14996

---

## 4. Benchmarks & Evaluation / 基准与评估

### 4.1 RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving
**RSI-PDEbench：面向 PDE 求解自改进智能体的基准**

- **Authors:** Binghang Lu, Lang Cao, Changhong Mou, Yige Sun, Cindy Xiangrui Kong, Zheyuan Deng, Tian Yuan, Bing Hu, Runyu Zhang
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.AI/cs.LG), 2026-11-11
- **Abstract & key innovations (metadata-level):**
  - **Problem:** Evaluating agents that iteratively improve on scientific/PDE-solving tasks requires benchmarks capturing self-improvement loops, tool use, and correctness.
  - **Method:** **RSI-PDEbench** provides tasks/protocols for self-improving PDE-solving agents (task taxonomy, metrics, and baselines in PDF).
  - **Innovation:** Extends agent evaluation into scientific computing with recursive improvement emphasis.
- **Comparison with prior methods:** Benchmark comparisons and agent baselines detailed in paper.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14949 · https://arxiv.org/pdf/2611.14949

### 4.2 Continual-ARC: Measuring Skill Acquisition over a Working Lifetime
**Continual-ARC：衡量“工作生涯”中的技能习得**

- **Authors:** Daniel Lenton
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.LG), 2026-11-10 (recent, relevant to benchmarks)
- **Abstract & key innovations:**
  - **Problem:** Continual-learning benchmarks often use single domains, one-shot instances, and separate protocols for memory- vs weight-based learners.
  - **Method:** Lifelong stream from ARC-AGI editions with recurring tasks, dormant gaps, fresh instances, budgeted demonstrations/submissions/retries; unified scoring; post-stream evaluation separates memorization (fresh instances of seen tasks) and generalization (unseen tasks).
  - **Innovation:** Fairer comparison of harness persistence and parametric learning over long horizons.
- **Comparison with prior methods (author-reported):**
  - Evaluated frozen-weight agent harnesses (Qwen3.5-9B, GLM-5.3 Flash variants) vs prompting floors, program induction, and weight imitation training.
  - Persistence generally does not improve memorization without explicit expert guidance; most harness methods learn less than a demonstration-caching floor; no harness-based method gains on unseen tasks while weight-based learning shows substantial generalization gains.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14505 · https://arxiv.org/pdf/2611.14505 · Code: https://github.com/unifyai/continual-arc

---

## 5. Recommendation Systems, Advertising & CTR / 推荐系统、广告与点击率预估

### 5.1 When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence
**推荐何时激发好奇心？理论、测量与实证证据**

- **Authors:** Pan Li, Alexander Tuzhilin
- **Affiliation:** Not specified in arXiv metadata (authors associated with recommender-systems/NYU Stern in prior work; verify from PDF)
- **Venue:** arXiv preprint (cs.IR), 2026-11-11
- **Abstract & key innovations:**
  - **Problem:** Curiosity can reduce filter bubbles and sustain engagement but lacks a formal, computable measure grounded in information-gap theory for recommender systems.
  - **Method:** Formalizes information-gap theory into **five axioms** and derives a canonical computational measure of curiosity evoked by a recommendation; builds a curiosity-aware recommender incorporating this measure into utility.
  - **Innovation:** Bridges psychological theory, measurement, offline ranking, and production experimentation.
- **Comparison with prior methods (author-reported):**
  - Survey study: proposed measure matches self-reported curiosity and outperforms proxy metrics.
  - Offline: significant improvements over state-of-the-art on **three real-world datasets**.
  - Online large-scale controlled experiment at a **major Asian video-streaming platform**: significant increases in **CTR, video views, and time spent** over latest production system; deployed in production.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14938 · https://arxiv.org/pdf/2611.14938

### 5.2 TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
**TS-GEAR：淘宝闪购生成式广告检索**

- **Authors:** Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Affiliation:** Taobao Shangou / Alibaba ecosystem (deployment context stated in abstract); individual affiliations not enumerated in arXiv metadata
- **Venue:** arXiv preprint (cs.IR/cs.AI/cs.CL), 2026-11-09
- **Abstract & key innovations:**
  - **Problem:** On-demand delivery ads require hard geographic reachability, query/location-conditioned preferences, and set-level diversity; standard generative retrieval treats geography softly and optimizes sequences independently.
  - **Method:** **Geo-Semantic ID** (geographic prefix + semantic suffix), **Query-Geo Target Attention** for dual-target history aggregation with behavior location keys, and **GMPO (Group Marginal Policy Optimization)** with deduplicated group rewards/marginal advantages.
  - **Innovation:** Makes reachability a differentiable prediction target and optimizes set-level value in generative ad retrieval.
- **Comparison with prior methods (author-reported):**
  - Deployed online with **0.1B backbone**, serving **>150M queries/day** in Taobao Shangou search advertising.
  - Outperforms state-of-the-art generative retrieval on HitRate and geographic validity.
  - Online gains: **+3.8% ad impressions, +4.2% ad revenue**.
- **arXiv/PDF:** https://arxiv.org/abs/2611.12180 · https://arxiv.org/pdf/2611.12180

### 5.3 CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?
**CHO-Bench：上下文提示如何影响 LLM 广告排序？**

- **Authors:** Shiqi Zhang, Yang Fei, Xiaokui Xiao
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.IR/cs.CL), 2026-11-09
- **Abstract & key innovations:**
  - **Problem:** LLM advertising can use advertiser-provided natural-language hints, but optimal hint construction is unclear.
  - **Method:** Formulates **Context Hint Optimization (CHO)**; proposes seven strategies (What/Who/When) plus Unified; introduces **CHO-Bench** with **>1.19M paired evaluations** across 5 datasets using embedding- and LLM-based rankers.
  - **Innovation:** Large-scale offline benchmark and analysis of strategy/ranker/budget interactions.
- **Comparison with prior methods (author-reported):**
  - Hints improve rankings under evaluated offline rankers; individual strategies similar on average, Unified not consistently best.
  - Effectiveness depends on generation-ranking configuration; larger budgets help with diminishing returns.
- **arXiv/PDF:** https://arxiv.org/abs/2611.11955 · https://arxiv.org/pdf/2611.11955

### 5.4 Slim Foundation Models for Latency-Critical Recommendation Serving (SlimFM)
**面向低延迟关键推荐服务的轻量基础模型（SlimFM）**

- **Authors:** Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** NeurIPS 2026 Workshop — Long Context Foundation Model (arXiv journal-ref/comment), 2026-11-07
- **Abstract & key innovations:**
  - **Problem:** Full LLMs help CTR semantics but are too expensive for online serving; many LLM-enhanced CTR systems cache outputs offline.
  - **Method:** **SlimFM**: dependency-aware structured pruning compresses **LLaMA3-8B → 4.5B** (44%); LoRA field-aware fine-tuning produces discriminative field-level embeddings; semantic-guided fusion injects them into CTR backbones.
  - **Innovation:** Practical online LLM semantic modeling for latency-critical CTR.
- **Comparison with prior methods (author-reported):**
  - Across **4 datasets, 6 CTR backbones**: retains **>99%** uncompressed-model accuracy with up to **3.4×** lower inference latency vs existing LLM-enhanced baselines.
- **arXiv/PDF:** https://arxiv.org/abs/2611.11013 · https://arxiv.org/pdf/2611.11013

---

## 6. Sequential Modeling, POI & User Modeling / 序列建模、POI 与用户建模

### 6.1 SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory
**SHARP：面向下一 POI 预测的语义分层智能体推理与动态记忆**

- **Authors:** Yuhang Zhan, Silin Zhou, Zhuo Chen, Haoxiang Lei, Yunren Feng, Lisi Chen, Shuo Shang
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** arXiv preprint (cs.IR), 2026-11-10
- **Abstract & key innovations:**
  - **Problem:** Next-POI prediction must connect LLM semantic reasoning to concrete POI decisions, handle evolving mobility with limited context, and preserve time-specific transitions.
  - **Method:** Hierarchical agentic framework (category-level reasoning guides POI prediction), trajectory memory agent with dynamic memory bank, multi-granularity time-aware category transition graphs, and RQ-VAE semantic IDs jointly optimized with predictor.
  - **Innovation:** Combines agentic memory, temporal graph views, and learned semantic IDs.
- **Comparison with prior methods (author-reported):**
  - On three real-world datasets: average **Acc@5 +5.29 pp** and **Acc@10 +4.52 pp** over strongest baseline.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14220 · https://arxiv.org/pdf/2611.14220

### 6.2 LUMIR: Decoupled Multimodal Representation Learning for Next-POI Recommendation
**LUMIR：面向下一 POI 推荐的异构多模态解耦表示学习**

- **Authors:** Zehui Wang, Wolfram Höpken, Dietmar Jannach
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** DaQuaMRec Workshop @ ACM RecSys 2026 (arXiv comment), 2026-11-10
- **Abstract & key innovations:**
  - **Problem:** Multimodal tourism/POI fusion is often tightly coupled to downstream recommenders, limiting reuse.
  - **Method:** Decoupled contrastive learning; LLMs unify heterogeneous modalities into shared textual space; interaction-aware fusion; sequential signals as structural constraints.
  - **Innovation:** Reusable multimodal representations independent of downstream architecture.
- **Comparison with prior methods (author-reported):**
  - On multimodal POI dataset across multiple sequential backbones: consistently outperforms multimodal fusion baselines on accuracy and beyond-accuracy metrics.
- **arXiv/PDF:** https://arxiv.org/abs/2611.14004 · https://arxiv.org/pdf/2611.14004

---

## 7. Games, Interactive Systems & Applied ML / 游戏、交互系统与应用机器学习

### 7.1 SkinAdvisor: An AI-Driven Decision Framework for Skin Production Planning
**SkinAdvisor：面向皮肤生产规划的 AI 决策框架**

- **Authors:** Ge Fan, Kai Wang, Chaoyun Zhang, Yingjie Li, Yuze Liu, Junyang Chen
- **Affiliation:** Not specified in arXiv metadata
- **Venue:** **Accepted to AAAI 2027 (IAAI-27)** (arXiv comment), 2026-11-11
- **Abstract & key innovations:**
  - **Problem:** Game skin production/release/pricing decisions are often intuition-driven despite being major revenue streams.
  - **Method:** **SkinAdvisor** decision framework powered by **SkinCast**, a multi-modal Transformer forecasting 180-day per-day sales trajectories for unreleased skins (Informer time-series encoder, Player-Hero-Skin graph embedder, attribute/context Transformers, shared backbone, non-autoregressive Informer decoder). Serving pipeline: Select → Fill → Infer → Sales → ROI → Ranking.
  - **Innovation:** End-to-end deployed forecasting-to-decision system for live game content planning.
- **Comparison with prior methods (author-reported):**
  - Offline: SkinCast reduces RMSE by **~20%** over strongest baseline (Informer) and **~60%** over classical methods.
  - Serving: p99 latency **<8 ms**, peak throughput **>1100 rps** on 16-core CPU server; in production for a full release cycle.
  - Deployment lessons: order-of-magnitude accuracy can suffice for decisions; pretrained embeddings may leak temporal info (season-based splitting needed).
- **arXiv/PDF:** https://arxiv.org/abs/2611.15023 · https://arxiv.org/pdf/2611.15023

### 7.2 RSI-PDEbench (cross-listed: games/simulation-adjacent agent self-improvement context)
See Section 4.1 for self-improving agent benchmark relevant to interactive/scientific task environments.

---

## 8. Focus-Lab / Industry Watch (requested organizations)

- **Google DeepMind / OpenAI / Meta AI / Microsoft Research / NVIDIA / Anthropic / Apple / Amazon:** No clearly attributable new first-party paper from these specific orgs appeared in today’s targeted arXiv API slice with explicit affiliation metadata; coverage constrained by unavailable web search and limited metadata.
- **ByteDance / Alibaba / Tencent / Kuaishou / Baidu / Netflix:** Recent production-scale recommendation/ads systems from Alibaba/Taobao Shangou (TS-GEAR) and ByteDance-related foundation-rec patterns (SepLRM, covered in 2026-11-12 digest) remain highly relevant to requested CTR/ads/retrieval topics.
- **Action:** Re-run with web search/OpenReview/official proceedings access to complete org-specific coverage for ICML/ICLR/KDD/CVPR/ACL/SIGIR/WWW accepted papers.

---

## 9. Cross-Cutting Trends (2026-11-13 snapshot)

1. **Diffusion LLM infrastructure:** mask-aware position extrapolation (MPPA) suggests diffusion-native long-context scaling differs from AR recipes.
2. **Agent reliability engineering:** harness/runtime policies (EvoX), termination behavior (Termination Lag), failure attribution (CoLFA), and reward-hacking diagnostics (Breaking Bad) point to operational control as a first-class research axis.
3. **Industrial generative retrieval & CTR serving:** geo-semantic IDs + set-level RL (TS-GEAR), pruned semantic models (SlimFM), and curiosity-aware utility (2611.14938) show continued convergence of LLM semantics with latency/business constraints.
4. **Evaluation rigor:** Continual-ARC and RSI-PDEbench emphasize long-horizon, self-improvement, and memorization-vs-generalization separation over static one-shot scores.
5. **Venue coverage gap:** several requested conferences lack freshly crawled accepted-paper deltas in this run; future daily digests should integrate OpenReview/proceedings APIs when available.

---

## 10. References (selected)

- Sarkar & Daimi, *Mask-Pattern Position Augmentation*, arXiv:2611.15029, 2026.
- Zhang, *AROMA*, arXiv:2611.15041, 2026.
- Zhang et al., *EvoX*, arXiv:2611.15006, 2026.
- Cim et al., *Termination Lag*, arXiv:2611.14960, 2026.
- Luo et al., *CoLFA*, arXiv:2611.14980, 2026.
- Fischl-Lanzoni et al., *Breaking Bad*, arXiv:2611.14996, 2026.
- Lu et al., *RSI-PDEbench*, arXiv:2611.14949, 2026.
- Lenton, *Continual-ARC*, arXiv:2611.14505, 2026.
- Li & Tuzhilin, *When Does a Recommendation Spark Curiosity?*, arXiv:2611.14938, 2026.
- Tong et al., *TS-GEAR*, arXiv:2611.12180, 2026.
- Zhang et al., *CHO-Bench*, arXiv:2611.11955, 2026.
- Aftab et al., *SlimFM*, arXiv:2611.11013, 2026 (NeurIPS 2026 Workshop LCFM).
- Zhan et al., *SHARP*, arXiv:2611.14220, 2026.
- Wang et al., *LUMIR*, arXiv:2611.14004, 2026 (DaQuaMRec @ RecSys 2026).
- Fan et al., *SkinAdvisor*, arXiv:2611.15023, 2026 (AAAI 2027 IAAI-27).
- Sellam et al., *Nullasar*, arXiv:2611.15040, 2026.
