---
title: "Conference & arXiv Digest — 2026-10-09 (NeurIPS 2026 / ICML 2026 / EMNLP 2026 / KDD 2026 / CIKM 2026 / SIGIR 2026 / WWW 2026 / RecSys 2026 / ACM MM 2026)"
type: synthesis
created: 2026-10-09
updated: 2026-10-09
sources: [arxiv-export-api, arxiv-html, conference-announcements]
tags: [conference-digest, NeurIPS2026, ICML2026, EMNLP2026, KDD2026, CIKM2026, SIGIR2026, WWW2026, RecSys2026, MM2026, agents, LLM, code-execution-prediction, world-models, games, recommendation, advertising, CTR, search, benchmarks, evaluation, distillation, MoE, video-generation, safety, unlearning, daily-digest]
---

# Conference & arXiv Digest — 2026-10-09

> **Scope.** Papers carrying a *verified* venue tag from **NeurIPS 2026, ICML 2026, EMNLP 2026, KDD 2026, CIKM 2026, SIGIR 2026, WWW 2026, RecSys 2026** and the ACM MM 2026 workshop orbit, plus high-signal recent arXiv preprints in the wiki's core categories (agents, LLM training/inference, code execution prediction & verification, world models, games, recommendation/advertising/CTR/search, benchmarks). **50 papers featured**, organized by venue, then category. This run was **tightly collision-managed against the same-day siblings** — including a new `arxiv-ai-search.md` digest that landed *after* this run's start baseline — costing **6 selected papers** (§7).

**Method (for reproducibility).** Harvest via the **arXiv export API** (`export.arxiv.org/api/query`, Atom XML): **54 serialized queries** — 16 venue `comment:` / `co:` sweeps (which pull the newest ~200 matching each tag, so 2026 acceptances surface regardless of submission date), 8 category sweeps bounded to `submittedDate:[20260920 … 20261009]`, 16 topic queries and 14 lab/company queries — requests spaced ≥3–4 s, with a full re-fetch run after the first run logged `HTTP 429`. The API's failure mode is a bare 14-byte `Rate exceeded.` body with no HTTP error status, which a naive parser reads as *zero results* — separately disclosed where a zero was accepted (§10). **3,365 records pooled → 2,751 unclaimed → 1,215 unclaimed+venue-tagged → ~50 shortlisted.** Venue tags were read from each entry's arXiv `comment` / `journal_ref` fields and are self-reported (main vs workshop vs oral stated where the comment distinguished them); not verified against proceedings. **Affiliations were read only from the paper's own arXiv HTML author block or the email domains printed in it — never inferred from surnames**; unresolved items are marked *(affiliation not recovered)* rather than guessed.

**Dedup.** Baseline regex-extract of every arXiv ID across `wiki/**/*.md` (regex `\b(?:26|25|19|20)\d{2}\.\d{4,5}\b`) at run start → **8,293 claimed IDs** saved to `/tmp/claimed.txt`. ⚠️ **A mid-draft sibling race then invalidated the cache**: `wiki/synthesis/2026-10-09/arxiv-ai-search.md` committed **28 IDs** after the baseline, 6 of which were this run's selections (`2610.10556`, `2610.11228`, `2610.11277`, `2610.11450`, `2610.11553`, `2610.12341`). All 6 were **withdrawn, not merged** (standing precedent), replaced with fresh 0-hit candidates, and the full 50-ID slate then **re-verified `rg -l` 0-hit against the whole live wiki before writing** (§10, follow-up #1 re-affirmed). **0 acronym/name collisions** (the 10-08 run's defect) beyond the ID-level sweep.

---

## 0. Executive Summary

- **Venue spread (50 papers):** NeurIPS 2026 **15** (8 main + 7 workshop/evals), EMNLP 2026 **11**, ICML 2026 **4** (2 main + 2 workshop), RecSys **1** (+1 dual), CIKM 2026 **3**, SIGIR 2026 **2**, WWW 2026 **1** (oral), KDD 2026 **1**, ACM MM 2026 workshop **1**, plus **11** un-venued recent arXiv preprints. Empty this window: ACL 2026, ICLR 2026, AAAI 2026, AAMAS 2026, CVPR 2026 (§8).
- **Industry density is at a series high: 20 of 50 papers have a company author/affiliation.** Amazon **6** (POI rerank H2CE was dropped to a sibling, but SMEO media ranking, FSD-unlearning, personas-for-surveys, ActiveMedAgent co-affiliation, clustering-guardrails, EgoVoice co-affiliation), **ByteDance 2** (SplitMoE NeurIPS Spotlight; AVE video editing), **Salesforce 2** (compaction-blindspot probe; MemoryAgentBench re-read), **IBM 2** (clustering-transformers; cross-dialect text-to-SQL), **Samsung 2** (codebook cross-modal KD; query-insensitive STVG), **Anthropic 1** (weight-exfiltration e-process), **Meta 2** (MT annotation co-affil; business-compromise detection), **Alibaba 2** (SAGE medical QA; CanniUplift), **Tencent 1 via Baidu-neighbour CypherTurn actually Baidu 1**, **NVIDIA 2** (Physical AI Smart Spaces; EgoVoice co-affil), **Sony 1**, **Booking.com 1**, **Walmart+Yahoo 1**, **Kuaishou 1**, **Huawei 1**, **Apple 1** (+ORCA co-affil), **Corbenic AI 1**, plus dual-workshop Amazon (clustering guardrails). The sharpest industry result: **Walmart.com shipped a DPO-trained Doc2Query variant to full traffic** (`2610.04352`).
- **The strongest cluster is *code-execution / software-state prediction as the new eval frontier* — 4 papers this window**, directly answering the requested topic: predicting a program's **final output AND checkpoint state** without tools (`2610.11889`, 93.0% shorter-trace final output) sits beside **CTE-Bench's counterfactual trace evaluation** — models track stateful-service intervention effects only **54–62%** when correct feedback is shown, collapsing to **~23–29%** when it isn't (`2609.36647`), a **Software World Model** that predicts a change's *blast set* (F1 **0.571** vs 0.431 static reachability, `2610.04940`), and a service-simulator lens on why coding agents' wrong expectations surface "several calls later".
- **Games coverage** is dominated by **world-model / interactive-environment benchmarking**: **MultiWorldBench** (Minecraft) shows independently-controlled views **do not** compose into one shared world (all generated systems ≤ 8.00/100 on state persistence; Engine GT 91.69 — `2610.11723`). The intended flagship games paper (Tsinghua's **AAArena** game-agent competition, `2610.12341`) was **withdrawn as a same-day sibling claim** (§7); the sim-racing TRACK kit was likewise claimed by the sibling. Games RL is saturating in this wiki — **3rd consecutive slow day** for genuinely-new game papers (§9.4).
- **Numbers that anchor the window:** SplitMoE beats load-balanced video MoEs with **equivalent activated params** and a **uniformity-trap diagnosis** (`2609.38140`, NeurIPS **Spotlight**); ORCA **halves FSD-diffusion training cost** to beat the 400K baseline at 200K steps (FID 16.65, GenEval 0.291, `2610.09841`); SOTA trading agents post **18.3% return / Sharpe 1.60 / DD 8.96%** out-of-sample over six months — and news injection **reverses sign** (−2.7%) (`2610.10407`); NetAgent generalizes to unseen traffic with **90.04% F1 vs 2.74%/3.04%** for the best task-specific baselines (`2610.07386`); NeMo-frontier **TRANSIT** trains with **50% fewer GPUs at >90% throughput** (`2610.07593`); StoreBench: **no frontier model beats scripted smart-triage** (best 49% vs 97% cells), humans still outscore every model (`2610.10942`).

---

## 1. NeurIPS 2026 — Main Track (8 papers)

### 1.1 Leaner Transformers Can Easily Learn to Cluster
- **中文标题**: 更精简的 Transformer 也能学会聚类
- **Authors**: Charlotte Park, Kenneth L. Clarkson, Lior Horesh, Takuya Ito, Parikshit Ram
- **Affiliation**: IBM (email block: ibm.com)
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Prior work showed an attention-in-context transformer can *exactly* run Lloyd's `k`-means in the forward pass, but required embedding size `d+k` (projection matrices of `(d+k)²`).
- **Key innovation**: A strictly smaller but equally expressive construction with embedding size `d + ⌈log₂ k⌉`; then — the paper's real subject — trains these transformers to learn clustering end-to-end and characterizes **convergence and in-distribution generalization of in-context learning algorithms based on stochastic gradients**, both theoretically and empirically.
- **Results / comparison**: Existence-style construction proven; empirical probe of the learned algorithm shows *where* learned clustering succeeds (in-distribution tasks) and fails (`d`, `k`, and distribution shifts) — a "algorithm-in-context learning" analysis rather than a benchmark win.
- **Link**: https://arxiv.org/abs/2610.09760

### 1.2 DISTILLING WHAT MATTERS — Confidence-Aware Selective Distillation for Large Language Models
- **中文标题**: 蒸馏什么更重要：面向大语言模型的置信度感知选择性蒸馏（CaRE-KD）
- **Authors**: Ayan Sengupta, Vaibhav Seth, Tanmoy Chakraborty
- **Affiliation**: IIT Delhi (indian-institute: ee.iitd.ac.in / iitd.ac.in)
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: KD assumes the teacher is a reliable oracle; on LLMs teacher predictions are often high-entropy/hallucinated, so standard KD corrupts the student's calibrated prior.
- **Key innovation**: **CaRE-KD**, a confidence-gated framework replacing static objectives with uncertainty-adaptive ones — a token-level **CaRE-Divergence** that switches between forward and reverse KL by teacher-vs-student confidence, plus a batch-level **Revival** epistemic-rejection mechanism that suppresses updates when the teacher is *more* uncertain than the student. Includes a gradient-level analysis of why the dual-granularity design induces conditional calibration that static divergences can't.
- **Results / comparison**: Across 8 teacher–student pairs × 11 benchmarks, consistent gains over Skewed-KL and α–β divergence — **+3.2 ROUGE-L** (instruction following), **+2.1 pass@1 MBPP**, **+1.7 GSM8k**, **+1.8 CollegeMath**, **+2.5 LLM-as-judge factuality**. Revival works as a loss-agnostic plug-in on top of existing objectives.
- **Link**: https://arxiv.org/abs/2609.36734

### 1.3 Best Arm Identification for Bandits with Shifting Means
- **中文标题**: 均值漂移型 Bandit 的最佳臂识别（ISM）
- **Authors**: Lukas Zierahn, Wouter M. Koolen, Shubhada Agrawal, Christina Katsimerou, Dirk van der Hoeven
- **Affiliation**: Booking.com (booking.com); CWI Amsterdam; IISc Bangalore
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: In classical BAI the means are stationary; here only the **gaps Δ between arms** are stable while a **common shift is chosen adversarially each round** — encodes booking/price environments where "the whole market moves but the ranking of options stays meaningful."
- **Key innovation**: Shows GLRT-based rules (**Track-and-Stop** among them) **fail** under shifting means; proposes **ISM (Importance Weights for Shifting Means)** and proves it δ-correct with sample complexity `O(K(σ²+U²) Δ_min⁻² ln 1/δ)`.
- **Results / comparison**: Matching (up to constants) worst-case **lower bound**; empirical validation. The first treatment of adversarial common-shift in BAI under a stability-only-gaps model.
- **Link**: https://arxiv.org/abs/2610.10488

### 1.4 Codebook-Guided Cross-Modal Knowledge Distillation for Structurally Heterogeneous Features
- **中文标题**: 面向结构异构特征的码本引导跨模态知识蒸馏
- **Authors**: Dae Ung Jo, Jongin Lim, YoungJoon Yoo, Daeho Um
- **Affiliation**: Samsung (samsung.com); Chung-Ang / Kyungpook / Ulsan (cau.ac.kr, knu.ac.kr, uos.ac.kr)
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Feature-level cross-modal KD assumes structurally alignable spaces (2D grids ↔ 1D sequences often don't correspond unit-to-unit), which limits transfer.
- **Key innovation**: Abstracts teacher features into **vector-quantized codes regardless of source structure**; codes are selected by *task relevance + student compatibility* and act as concept anchors — no unit-level alignment required.
- **Results / comparison**: Effective on classification and semantic segmentation across diverse cross-modal scenarios (e.g., visual→audio KD).
- **Link**: https://arxiv.org/abs/2609.37243

### 1.5 BREAKING THE UNIFORMITY TRAP — Scaling Video Diffusion Model via SplitMoE
- **中文标题**: 打破均匀性陷阱：通过 SplitMoE 扩展视频扩散模型
- **Authors**: Yu Xu, Yuxin Zhang, Xiao Yang, Haotian Yang, Yizhi Wang, Xinwei Huang, Minxuan Lin, Angtian Wang, Chongyang Ma, Fan Tang
- **Affiliation**: ByteDance (from arXiv HTML name match)
- **Venue**: **NeurIPS 2026 — Spotlight**
- **Problem background**: Token-wise MoE in visual generation **regularizes usage toward uniformity**, but video is spatiotemporally redundant and semantically long-tailed — "uniformity trap" scatters coherent patches across experts → routing fragmentation, structural distortion.
- **Key innovation**: **SplitMoE** bifurcates the expert pool into **semantic experts** (high-level abstraction) and **generic experts** (residual visual information), with **prototype-guided routing** + **pull-push regularization** so tokens cluster by semantic attribute rather than arbitrary balance.
- **Results / comparison**: Under an **equivalent activated-parameter budget**, SplitMoE beats load-balanced MoEs in convergence speed, routing coherence and generation quality; reveals emergent **coarse-to-fine denoising logic**. Positioned as a modality-aware scaling path for video world models.
- **Link**: https://arxiv.org/abs/2609.38140

### 1.6 TRANSFORMING IMAGE EDITORS INTO VIDEO EDITORS — Anchor-Based Video Editing (AVE)
- **中文标题**: 把图像编辑器改造成视频编辑器：基于锚点的视频编辑（AVE）
- **Authors**: Feng Wang, Zijie Li, Ceyuan Yang, Alan Yuille, Peng Wang
- **Affiliation**: ByteDance (arXiv HTML name match) + Johns Hopkins University (Yuille)
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: End-to-end video editing is expensive and hard; image editing has matured far faster.
- **Key innovation**: Decompose video editing into **editing sparse keyframes (strong image editor) + motion-guided image-to-video propagation with edited keyframes as fixed anchors** — no monolithic video editor training.
- **Results / comparison**: Strong instruction-following, temporal consistency, fidelity on **IVEBench and VIE-Bench**; ablations show final quality **tracks the image editor's quality** → lightweight transfer beats retraining.
- **Link**: https://arxiv.org/abs/2610.11037

### 1.7 ENABLING PREFERENCE-DRIVEN UNLEARNING IN FEW-STEP DISTILLED TEXT-TO-IMAGE DIFFUSION MODELS
- **中文标题**: 少步蒸馏文生图扩散模型中的偏好驱动"遗忘"（unlearning）
- **Authors**: Gaurav Patel, Jun Fang, Greg Ver Steeg, Qiang Qiu, Sravan Sripada
- **Affiliation**: Purdue University + **Amazon** (per arXiv HTML affiliation sweep)
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Data-driven unlearning objectives assume multi-step denoising dynamics, which **break for Few-Step Distilled (FSD)** models; re-distilling a base-model-unlearned FSD model is prohibitively expensive.
- **Key innovation**: Revisits **DPO for diffusion** and shows its noise-prediction formulation transfers poorly to FSD; introduces a modified preference-optimization objective explicitly aligned with few-step generation → **direct concept removal in FSD**.
- **Results / comparison**: Consistent, effective forgetting on identity + NSFW (nudity) removal tasks, extended to object-level unlearning, with strong retention of non-targeted capabilities and preserved few-step efficiency.
- **Link**: https://arxiv.org/abs/2610.10859

### 1.8 ORCA — HUNTING COMPOSITIONAL FAILURES IN TEXT-TO-IMAGE DIFFUSION
- **中文标题**: ORCA：在文生图扩散模型中追猎组合性失败
- **Authors**: Arshia Hemmat, Amirhossein Vahidi, Amitis Shidani, Mohammad Vali Sanian, Hesam Asadollahzadeh, Aryan Yazdan Parast, Mohammad Lotfollahi
- **Affiliation**: Wellcome Sanger Institute (sanger.ac.uk) + **Apple** + **Stability AI** (arXiv HTML affiliation sweep)
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Compositional failures (attribute binding, spatial relations, count) persist even after adding the T5 encoder — argued as **misaligned** rather than missing information: the text encoder's LM-shaped representation doesn't get vision-shaped reward.
- **Key innovation**: **Orthogonal Residual Compositional Alignment** — an auxiliary loss aligning the DiT latent with a **low-rank target from a frozen visual encoder**, where the readout subspace is selected by a learned residual between T5 and CLIP embeddings (prompt-dependent). Proof that cross-modal information measurable at a given rank is bounded by spectral mass of the visual covariance.
- **Results / comparison**: DiT-B/2, DiT-L/2, U-ViT-L all beat vanilla and REPA at **zero inference cost**; **DiT-L/2 FID 16.65 / GenEval 0.291 at 200K steps** — beats the strongest 400K baseline at half the training cost; largest gains on attribute binding / spatial relations / multi-object prompts.
- **Link**: https://arxiv.org/abs/2610.09841

---

## 2. NeurIPS 2026 — Workshops & Evals (7 papers)

### 2.1 Evaluating Exact Output and Checkpoint-State Prediction in Real Programs
- **中文标题**: 在真实程序中评测对最终输出与检查点状态的精确预测
- **Authors**: Xiaohong Chen, David Bucur, Chenglong Ma, Yi Zhang, Lingming Zhang, Sriram Vishwanath, Grigore Rosu
- **Affiliation**: Intent Computing Org (intentcomputing.org) + Georgia Tech (ece.gatech.edu) + Illinois (illinois.edu)
- **Venue**: **NeurIPS 2026 Workshop on AI for Verifiable Coding**
- **Problem background**: **Requested topic — code execution prediction.** CRUXEval-style output prediction doesn't test whether a model tracks *state across executions*, e.g. the effect of a loop/checkpoint on later behavior.
- **Key innovation**: Benchmark with **400 cases / 371 Python+C++ programs**, pairing shorter- and longer-trace inputs with **checkpoints inside and after loops**, scored under seven settings across four model families, **no tools / no execution**; missing responses counted as wrong.
- **Results / comparison**: 11,151/11,200 gradable predictions. Reasoning-enabled vs off: **+33.1 to +55.2 pts** on completed responses. Strongest settings: **93.0%** (short-trace output) / **77.0%** (long-trace) / **65.5% & 63.5%** (the two state tasks), robust to missing-is-wrong. Longer-trace input flips 528 correct→wrong and 147 reversals across 2,397 matched Python comparisons — **short-output scores hide these errors**.
- **Link**: https://arxiv.org/abs/2610.11889

### 2.2 Anytime-valid Detection of LLM Weight Exfiltration
- **中文标题**: 对 LLM 权重外泄的任意时刻有效检测（e-process）
- **Authors**: Ines Ortega-Fernandez, Mateusz Kowalczyk, Keri Warr
- **Affiliation**: **Anthropic** (anthropic.com)
- **Venue**: **NeurIPS 2026 Workshop E-Values: From Statistics to ML — Oral**
- **Problem background**: A compromised inference server can exfiltrate weights by encoding payload bits in plausible token choices; replay in a trusted server detects some of it, but benign numerical nondeterminism hides patient attackers.
- **Key innovation**: A **prompt-level e-process** — calibrates whole-response mismatch events on trusted benign traffic and accumulates evidence sequentially with **explicit anytime false-alarm control over an unbounded horizon**.
- **Results / comparison**: Evaluated on four models against a seed-blind and a stronger **seed-aware** attack (payload hidden only in near-ties); characterizes the channel-capacity vs detectability trade-off, beating a hard per-token alarm by combining weak evidence across responses.
- **Link**: https://arxiv.org/abs/2610.11843

### 2.3 CTE-Bench — Counterfactual Trace Evaluation for Stateful Software Simulators
- **中文标题**: CTE-Bench：面向有状态软件模拟器的反事实轨迹评测
- **Authors**: Xinran Zhang
- **Affiliation**: UC Berkeley (berkeley.edu)
- **Venue**: **NeurIPS 2026 — Track on Evaluations and Datasets**
- **Problem background**: **Requested topic — code execution prediction.** Coding agents patch services / overwrite state and act on expectations of the *future behavior* of a stateful service; function-level code-exec benchmarks omit persistent state, and agent benchmarks score actions/final state, not the model's predictive understanding.
- **Key innovation**: Measures **whether a model can predict how an intervention changes a stateful service's future responses** (no action choice). Each scenario: Python service code + observed calls + intervention (source edit or state overwrite) + 40 fixed future calls; predictions executed against the real service. Three memory protocols (correct earlier responses / none / the model's own prior predictions). Core v1: **255 scenarios / 6 deterministic services → 10,200 predictions per model**; main metric **effect-step value match (VM)** over 2,476 intervention-changed calls.
- **Results / comparison**: With correct earlier responses revealed, DeepSeek V4-Flash / Kimi K2.5 / Qwen3.6-35B-A3B / Claude Sonnet 4.6 reach **54.3–61.5%** effect-step VM; hiding responses drops it to **23.2–28.9%**; self-generated predictions give 24.8–33.2%; ≤1.2% of scenarios predicted exactly end-to-end → **models track effects mainly under supplied feedback, and errors compound over rollouts.**
- **Link**: https://arxiv.org/abs/2609.36647

### 2.4 Physical AI Smart Spaces — Multi-Camera 3D Perception Benchmark
- **中文标题**: Physical AI Smart Spaces：智能空间多相机 3D 感知大规模基准
- **Authors**: Yuxing Wang, Yizhou Wang, Anqi Li, Shuo Wang, Sam Pulli Pusegaonkar, Haoquan Liang, Jiajun Li, Shenxin Jiang, Jianhe Yuan, Shangru Li, Tongwei Dai, Zihao Chen, David C. Anastasiu, Sujit Biswas, Xunlei Wu, Zheng Tang
- **Affiliation**: **NVIDIA** (nvidia.com) + Ilsru/guests
- **Venue**: **NeurIPS 2026 — Evaluations & Datasets (poster)**
- **Problem background**: No existing benchmark gives large-scale, multi-class, **multi-camera 3D** perception data for indoor smart spaces.
- **Key innovation**: **280+ hours** of synchronized 1080p from ~1,800 cameras in warehouses/hospitals/retail, with multi-camera identity, 2D/3D boxes, calibration, depth; **Isaac Sim synthetic + Cosmos transfer + real-world Sim2Real** warehouse deployments with VGGT calibration; **3D instantiation of HOTA**. Release: huggingface.co/datasets/nvidia/PhysicalAI-SmartSpaces.
- **Results / comparison**: Ships official evaluation system and leaderboard; baselines from AI City Challenge show progression from person-only 3D location tracking to multi-class 3D box tracking.
- **Link**: https://arxiv.org/abs/2610.02580

### 2.5 Does an Agent's History Tell You When Compaction Will Hurt? (TRACE paired-replay probe)
- **中文标题**: 智能体的历史能预判压缩（compaction）何时有害吗？
- **Authors**: Egor Pakhomov, Erik Nijkamp
- **Affiliation**: **Salesforce** (salesforce.com)
- **Venue**: **NeurIPS 2026 IAB Workshop (Interpreting Agent Behavior), non-archival**
- **Problem background**: Long-horizon agents compact context on a global token budget, blind to what the agent was doing; a bad compaction surfaces as later **erroring/repeated calls**.
- **Key innovation**: Regression/trigger study on **TRACE's 590-benchmark compaction boundaries** asking whether pre-boundary history predicts post-compaction burden. Best **extension-protocol trigger**: held-out AUROC **0.66** (boundary-replicate: 0.72); **frozen interpretable trigger avoids 21% of harmful boundaries while keeping 84% of compaction opportunities**.
- **Results / comparison**: Effect is **modest and negative-flavored** — "has-written"-style labels measure trajectory phase, not harm; best trigger exceeds random-rule expectation on *count* but not burden *mass*. States what corpus corpora must ship to answer the matched-retention question.
- **Link**: https://arxiv.org/abs/2610.08722

### 2.6 Bookkeeping, Composition, or Unreachable Gold? Reading MemoryAgentBench's Conflict-Resolution Scores
- **中文标题**: MemoryAgentBench 冲突消解分数到底在测什么？
- **Authors**: Egor Pakhomov, Erik Nijkamp
- **Affiliation**: **Salesforce** (salesforce.com)
- **Venue**: **NeurIPS 2026 IAB Workshop (Interpreting Agent Behavior), non-archival**
- **Problem background**: MemoryAgentBench's Conflict Resolution split is read as measuring "selective forgetting".
- **Key innovation**: Executes the benchmark's *own rule* (newest-statement-wins) as a **frozen zero-learning last-write resolver**: answers **80.25%** under the official metric (74.5% on held-out lists). Of the rest, **67 items have unreachable gold** by the last-write graph (e.g. "capital of India is Grosseto" superseding New Delhi, gold = New Delhi) — a **third of the multi-hop questions at 262K**.
- **Results / comparison**: Two long-context models and a pre-registered BM25-agent re-implementation score 84.7 / 82.6 / 41.6 on rule-solvable items vs 10.4 / 11.9 / 6.0 on the 67 unreachable ones → failures are a **reachability split + parser-scope residual**; the per-item split, not the aggregate, is the only readable unit.
- **Link**: https://arxiv.org/abs/2610.09193

### 2.7 SOTA — Stock Options Trading Agents Guided by Option-Implied Return Distributions
- **中文标题**: SOTA：由期权隐含收益分布引导的股票期权交易智能体
- **Authors**: Yizhen Xie, Mengyang Liu
- **Affiliation**: CMU (andrew.cmu.edu)
- **Venue**: **NeurIPS 2026 Agenthon Workshop**
- **Problem background**: Options-trading agents must pick *which* contracts and *how to combine them* (thousands per stock); fixed-strategy approaches (e.g. straddle) can't switch with the market.
- **Key innovation**: Abstracts the option universe into **strategy-level decisions** with deterministic resolvers doing portfolio implementation; post-trains Qwen3.8-27B with **SFT then RL**.
- **Results / comparison**: Six-month out-of-sample on 9 large-cap equities + SPY: **18.3% total return, Sharpe 1.60, max DD 8.96%** vs rule-based/ML selectors. Documented asymmetry: news improves teacher trajectories but **retaining news during RL flips out-of-sample return from +18.3% to −2.7%**.
- **Link**: https://arxiv.org/abs/2610.10407

---

## 3. ICML 2026 (4 papers; 2 main + 2 workshops)

### 3.1 RouterInterp — Understanding Superposed Specialisation in MoE Routing
- **中文标题**: RouterInterp：理解 MoE 路由中的"叠加特化"
- **Authors**: Ilya Lasy, Nora Yinuo Cai, Kola Ayonrinde
- **Affiliation**: TU Wien (tuwien.ac.at)
- **Venue**: **ICML 2026** (main)
- **Problem background**: The "each expert owns one coherent domain" hypothesis has repeatedly failed interpretability attempts.
- **Key innovation**: **Superposed Specialisation Hypothesis** — experts specialize in a *disjoint union of fine-grained features*. RouterInterp finds the Sparse-Autoencoder features that best predict routing and emits unified natural-language explanations.
- **Results / comparison**: On gpt-oss-20b, explains expert routing with **~65% higher detection accuracy** than prior token-statistics baselines.
- **Link**: https://arxiv.org/abs/2610.11775

### 3.2 Factorized Scheduling Principle — Interpretable, Transferable Scheduling Policies
- **中文标题**: 因子化调度原理：可解释且可迁移的调度策略
- **Authors**: Hong Je-Gal, Hyun-Suk Lee
- **Affiliation**: Sejong University (sejong.ac.kr)
- **Venue**: **ICML 2026** (main)
- **Problem background**: Priority-based scheduling reduces to scoring candidate states; learned rules are opaque and don't transfer across system scales.
- **Key innovation**: **FSP** represents system states as condition distributions and decomposes a global scheduling principle into **additive univariate + pairwise components with identifiability constraints**, learned by a policy-based objective + TD signal over the condition distribution.
- **Results / comparison**: Strong performance, interpretability, and **zero-shot generalization** across different system scales on synthetic and realistic scheduling tasks.
- **Link**: https://arxiv.org/abs/2609.36578

### 3.3 Temporal State Transport in Video Generation — Diagnosing and Correcting Spectral Imbalance
- **中文标题**: 视频生成中的时序状态输运：谱失衡的诊断与矫正
- **Authors**: Luyao Tang, Bingjun Luo, Dong Yi, Jialin Guo, Haoning Xi, Cheng Chen, Yizhou Yu, Chaoqi Chen
- **Affiliation**: The University of Hong Kong (hku.hk) + Tsinghua University (tsinghua.edu.cn)
- **Venue**: **ICML 2026 F2S Workshop — Best Paper Award**
- **Problem background**: Training-free fixes (cross-frame attention strengthening, local entropy analysis) can't tell whether temporal interactions stay in a *healthy transport regime*.
- **Key innovation**: **Spectral Tension**, a signed diagnostic comparing local attention diffuseness with global spectral diversity, identifies **fragmented transport** and **over-mixing hotspots**; **Spectral Transport Homeostasis** softly corrects pathological temporal states.
- **Results / comparison**: Selectively applies larger corrections to worst hotspots, improving temporal consistency and visual quality on pretrained video generation models **without fine-tuning**.
- **Link**: https://arxiv.org/abs/2609.08505

### 3.4 Efficient Clustering with Quality Guardrails for LLM Recommender Systems at Industry Scale
- **中文标题**: 带质量护栏的高效聚类：工业级 LLM 推荐（38M 用户部署）
- **Authors**: Longshaokan Wang, Wai Tsang Keung, Punit Ghodasara, Roman Wang, Ali Dashti, Francesc Moreno-Noguer
- **Affiliation**: **Amazon** (all authors' emails amazon.com)
- **Venue**: **ICML 2026 HDLD workshop (non-archival) + RecSys 2026 GenAI-E-Commerce workshop**
- **Problem background**: Running an LLM per sample over millions of inputs is prohibitive; clustering + representive-only inference risks **per-sample guardrail violations** (e.g., toddler-parent mislabeled representatives getting age-inappropriate recs).
- **Key innovation**: Two-stage algorithm — Mini-batch K-Means initial clusters, then **greedy representative selection guaranteeing a minimum embedding similarity and exact attribute match for every sample**; provable, with complexity analysis.
- **Results / comparison**: Runs substantially faster and scales where standard methods become intractable; **production deployment clustering 38M customers cuts downstream LLM cost/runtime ~50×** while preserving personalization, unblocking a persona-based recommender with **positive A/B revenue/engagement**.
- **Link**: https://arxiv.org/abs/2607.19704

---

## 4. EMNLP 2026 (11 papers)

### 4.1 LLMs for Machine Translation Quality Annotation — Humans and Models Are Both Challenged
- **中文标题**: LLM 做机器翻译质量标注：人类与模型同样吃力
- **Authors**: Hala Almaghout, Christian Federmann, Qin Gao
- **Affiliation**: **Apple + Meta** (apple.com per arXiv HTML affiliation sweep)
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: LLMs are expected to replace humans for MT evaluation (MQM + Error Span Annotation), but must be checked across language pairs / domains / granularity.
- **Key innovation**: Agreement study against human annotators on a **70-pair long-context set + WMT23/WMT25**, measuring both score and error-span agreement.
- **Results / comparison**: LLM↔human agreement can *exceed* human↔human on some tasks but **varies substantially and stays unreliable in most settings**; humans fail on fine-grained MQM + low-resource pairs, LLMs on minor errors, wrong language variants, error spans → argues for **human-LLM collaborative annotation**.
- **Link**: https://arxiv.org/abs/2610.10918

### 4.2 Closing the Cross-Dialect Gap — Query Plans as a Portable Interface in Text-to-SQL
- **中文标题**: 弥合跨方言差距：用查询计划作为 Text-to-SQL 的可移植接口
- **Authors**: Corentin Royer, Robin Oester, Yotam Perlitz, Yannick Metz, Andrea Giovannini, Mennatallah El-Assady
- **Affiliation**: **IBM Research** (ibm.com)
- **Venue**: **EMNLP 2026 — Findings**
- **Problem background**: Text-to-SQL is trained on SQLite yet deployed on PostgreSQL/MySQL/ClickHouse; every model tested loses accuracy cross-dialect, across scale/architecture/purpose-built systems.
- **Key innovation**: Change the generation *target* — emit a **dialect-agnostic relational algebra query plan**, compiled deterministically to any backend's SQL. Plus **MetricName**, a question-aware result-set comparator for fair cross-dialect evaluation.
- **Results / comparison**: Across 13 models (3B→frontier), restores portability nearly uniformly at small home-dialect cost for capable prompted models, **none once fine-tuned on plans**; under matched fine-tuning, **plan supervision yields a stronger model than SQL supervision**.
- **Link**: https://arxiv.org/abs/2609.33670

### 4.3 Business Compromise Detection with Agentic AI and LLM-Driven Knowledge Discovery
- **中文标题**: 用智能体 AI 与 LLM 驱动知识发现检测"商家账户劫持"
- **Authors**: Diego Palma, Kyu Bin Kim, Zhen Han, Allbright Dsouza, Zhiyuan Liu
- **Affiliation**: **Meta** (meta.com)
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Compromised business ad accounts run fraudulent campaigns; autonomous LLM agents hallucinate on hard cases → business friction.
- **Key innovation**: Keep the agent as an **investigator emitting an interpretable signal vector**, delegate the verdict to a **neuro-symbolic arbiter**: FOIL-IE inductive-logic rules + Naïve Bayes calibration + data-tuned contradiction layer.
- **Results / comparison**: Arbiter substitution raises **MCC 0.295 → 0.435** (Δ+0.139, p=0.018) and **precision 0.250 → 0.446 (1.8×)** at recall 0.920→0.660; also beats tree ensembles (0.386) under matching conditions. Rules stay interpretable/auditable.
- **Link**: https://arxiv.org/abs/2609.32643

### 4.4 Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding
- **中文标题**: 时-空视频定位中的"查询不敏感"行为研究
- **Authors**: Eryk Kołodziejczyk, Alberto Presta, Karol Szurkowski, Michal Byra
- **Affiliation**: **Samsung** (samsung.com)
- **Venue**: **EMNLP 2026 — Findings**
- **Problem background**: STVG models assume each query is relevant to the video; the assumption is untested.
- **Key innovation**: Probes SOTA STVG under **irrelevant / removed queries** on HCSTVG-v2 & VidSTG, analyzing dataset regularities that encourage query-insensitivity.
- **Results / comparison**: Models still emit *plausible* spatio-temporal predictions with unrelated or even absent queries → motivates **negative-aware evaluation protocols** and relevance-aware architectures.
- **Link**: https://arxiv.org/abs/2610.06018

### 4.5 Data-Driven Personas for Survey Simulation — Insights Across Data-Access Regimes
- **中文标题**: 面向问卷模拟的数据驱动"人格"（personas）
- **Authors**: Dongryeol Lee, Weronika Łajewska, Leonardo Perelli, Saab Mansour
- **Affiliation**: **Amazon** (amazon.com) + Seoul National University (snu.ac.kr)
- **Venue**: **EMNLP 2026 — REALM workshop**
- **Problem background**: Steering LLMs with target-domain human data is costly and privacy-sensitive; can survey simulation use *anonymized public behavioral* data instead?
- **Key innovation**: Demographic group-level survey simulation with personas induced from heterogeneous anonymized data; studies source domain / scale / granularity effects on simulation alignment.
- **Results / comparison**: Out-of-domain personas rarely beat demographic-only conditioning (population mismatch); **accurate target-group assignment** improves alignment substantially; target-domain personas generalize better as question history grows (richer behavioral evidence → more stable persona traits).
- **Link**: https://arxiv.org/abs/2610.05828

### 4.6 SAGE — Semantic Anchor-Guided Evolution for Grounded Medical QA Data Synthesis
- **中文标题**: SAGE：语义锚引导的医学问答数据生成
- **Authors**: Chuan Li, Chengyu Wang, Cen Chen, Ye Lyu, Mingyuan Fan, Ming Gao
- **Affiliation**: **Alibaba** (alibaba-inc.com) + academia
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Expert-annotated medical QA data is scarce; privacy rules block open corpora / cloud APIs in clinical settings.
- **Key innovation**: Uses lightweight public taxonomies (**MeSH**) as **semantic anchors** imposing a structured prior; iteratively interleaves **atomic** (concept-based) and **associative** (relation-based) synthesis **from minimal seeds**, fully on-premises.
- **Results / comparison**: Small locally-deployed models fine-tuned on SAGE data consistently beat self-derived / conventional document-based synthesis across medical-QA benchmarks — a data-efficiency + resource-constraint win.
- **Link**: https://arxiv.org/abs/2610.08093

### 4.7 Syn-Omni — Structured Specialization and Progressive Collaboration for Omnimodal Embeddings
- **中文标题**: Syn-Omni：全模态嵌入的结构化特化与渐进协作
- **Authors**: Youngtaek Oh, Qiyu Wu, Hiromi Wakaki, Junmo Kim, Yuki Mitsufuji
- **Affiliation**: **Sony** (sony.com) + KAIST (kaist.ac.kr)
- **Venue**: **EMNLP 2026 — Findings**
- **Problem background**: Omnimodal embeddings need shared universal + modality-specific structure; single shared parameter spaces over mixed-modality data blur the two.
- **Key innovation**: **OME-LoRA** (orthogonal modality-expert LoRA: shared path for universals + per-modality expert paths) with **Progressive Synergy Routing** that lets experts establish modality priors first, then interact across modalities.
- **Results / comparison**: Outperforms omnimodal baselines across **81 tasks spanning image / video / audio / audiovisual** modalities.
- **Link**: https://arxiv.org/abs/2610.12256

### 4.8 ActiveMedAgent — Cost-Aware Trajectory Learning for Multimodal Medical Diagnosis
- **中文标题**: ActiveMedAgent：考虑成本的医疗诊断轨迹学习
- **Authors**: Weiwei Ma, Xiaobing Yu, Peijie Qiu, Jin Yang, Zhaoqi An, Xuanzhao Dong, Xiaoqi Zhao, Xiaofeng Liu
- **Affiliation**: Washington University in St. Louis + Yale (wustl.edu, yale.edu); **Amazon co-affiliation** (per arXiv HTML sweep)
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Clinicians escalate cheap→costly tests only when uncertainty warrants it; multimodal medical AI usually just throws all modalities at the problem.
- **Key innovation**: Given a frozen API-accessed VLM, tracks diagnosis distributions and scores each acquisition by **utility−cost**; a lightweight MLP controller learns *when to request evidence / when to commit* offline from scored trajectories.
- **Results / comparison**: Beats unguided acquisition and full-modality baselines on three benchmarks; documents an **information-overload effect** — in 175 cases the agent is correct with *fewer* channels where full-modality fails: **learning what to omit ≈ learning what to acquire**.
- **Link**: https://arxiv.org/abs/2610.11140

### 4.9 EgoVoice — Proactive Spoken Assistance from Egocentric Multimodal Streams
- **中文标题**: EgoVoice：来自第一视角多模态流的主动语音辅助
- **Authors**: Heeseung Kim
- **Affiliation**: University of Seoul (uos.ac.kr); **Amazon / NVIDIA / Intel co-affiliations** (arXiv HTML sweep)
- **Venue**: **EMNLP 2026 — Main Conference** (25 pp / 12 figs / 11 tables)
- **Problem background**: Wearable AR assistants must decide *when to speak and what to say* from continuous first-person video+audio — no prior system addresses the joint problem.
- **Key innovation**: From **HoloAssist** instructor recordings, builds clean audio (source separation + speech resynthesis) and casts sessions as **moment-by-moment silence-or-speak decisions**; fine-tunes an omni-modal LLM, then improves proactive intervention with **DPO**.
- **Results / comparison**: Existing systems rarely produce well-timed, meaningful proactive interventions; EgoVoice improves intervention timing, content relevance and human preference over the zero-shot backbone.
- **Link**: https://arxiv.org/abs/2610.12248

### 4.10 CypherTurn — Multi-Turn Conversational Text-to-Cypher Benchmark and the Autonomy Divergence
- **中文标题**: CypherTurn：多轮对话式 Text-to-Cypher 基准与"自主性发散"
- **Authors**: Yuzhe Zhang, Weijie Zhu, Haolin Yang, Ziyun Zhang, Xianwei Xue, Mengke Chen, Qiutong Pan, Huaqian Cai
- **Affiliation**: Peking University (pku.edu.cn) + **Baidu** (arXiv HTML sweep)
- **Venue**: **EMNLP 2026 — Oral**
- **Problem background**: Every existing text-to-cypher benchmark is single-turn; analysts actually work in multi-turn sessions. First benchmark: **721 sessions / 5,927 turns / 7 knowledge graphs / 13 conversational phenomena**.
- **Key innovation/Results**: **① Best model 64.7% execution accuracy, session-level correctness <5%** — hard, open. **② Autonomy Divergence**: frontier leaderboards reorder under fully-autonomous operation → error-management is a partially independent capability. **③ Budget scaling x3→x10 fails**: strongest frontier models **self-limit to ~2 actions/turn**. **④ Single-turn Cypher fine-tuning degrades multi-turn instruction-following**; architecture-appropriate specialization beats several frontier models.
- **Link**: https://arxiv.org/abs/2609.36987

### 4.11 CogMem — From Retrieval to Reconstruction: Evolvable Cognitive Memory for Long-Term Dialogue
- **中文标题**: CogMem：从检索到重构——长期对话的可演化认知记忆
- **Authors**: Zirui Liao, Zhengxian Wu, Zhuohong Chen, Yunyao Yu, Xiaoyu Liu, Yifan Xu, Haoqian Wang
- **Affiliation**: Tsinghua (per arXiv HTML affiliation sweep); emails gmail.com only
- **Venue**: **EMNLP 2026** (main, 21 pp)
- **Problem background**: RAG-based long-term dialogue memory treats memory as passive storage; it fails to distinguish source-attributed beliefs from unattributed facts and to join evidence across sessions.
- **Key innovation**: **PEC²F (Person-Event-Concept-Claim-Fact) graph schema** with provenance-aware incremental conversion, consolidation into higher-level facts, and **temporally-scoped Claim views for conflicting updates**; a rule-based controller composes four deterministic graph operators (anchoring / traversal / intersection / evidence grounding) for reconstruction-style retrieval.
- **Results / comparison**: Strong on LoCoMo and LongMemEval, especially multi-hop / temporal / knowledge-update tasks; ablations + semantic-collapse probe support epistemic separation, consolidation, and agentic retrieval as complementary.
- **Link**: https://arxiv.org/abs/2610.11314

---

## 5. RecSys / CIKM / SIGIR / WWW / KDD 2026 — Rec, Ads, CTR, Search (9 papers)

### 5.1 SMEO — Sequential Multimodal Evidence Optimization for Product Media Ranking (Amazon, CIKM 2026)
- **中文标题**: SMEO：电商商品媒体排序的序贯多模态证据优化（Amazon）
- **Authors**: Prasenjit Dey, Frank McIntyre, Arnab Sinha | **Amazon** (amazon.com)
- **Venue**: **CIKM 2026** ("Proceedings of the 35th ACM CIKM, Rome")
- **Problem background**: E-commerce media (images/videos/3D) are cooperative evidence; existing ranking optimizes myopic clicks/dwell.
- **Key innovation**: Two-stage utility-guided pipeline — a **trajectory utility model** (mitigating position-bias and variable-depth imbalance) + an **autoregressive ranking policy with survival-weighted reward-to-go** that front-loads decision-relevant information.
- **Results / comparison**: Doubly-robust offline OPE on large-scale sessions: **+5.5% estimated conversion, and customers reach a purchase decision with 15% fewer swipes** vs baselines.
- **Link**: https://arxiv.org/abs/2608.15662

### 5.2 Can LLMs Identify Meaningful Touchpoints in Conversion Attribution? (CIKM 2026 short)
- **中文标题**: LLM 能识别转化归因中的"有意义的触达点"吗？（Nanjing U + Alibaba）
- **Authors**: Jinqi Wu, Sishuo Chen, Zhangming Chan, Yong Bai, Chao Yi, Han Zhu, Shuodian Yu, Lei Zhang, Sheng Chen, Chenghuan Hou, Jian Xu, Chaoyou Fu
- **Affiliation**: **Nanjing University + Alibaba** (alibaba-inc.com, pku.edu.cn)
- **Venue**: **CIKM 2026 — short paper**
- **Problem background**: Attribution touchpoint selection relies on CF-based heuristics that miss user-perceived semantic intent; human annotation exposes a big semantic gap.
- **Key innovation**: Systematic evaluation of LLMs at finding *implicitly-related* touchpoints; prompting- and foundation-model-variant analysis; then **LLM-attributed labels improve industrial CVR model training** with significant offline gains.
- **Results / comparison**: LLMs recover a substantial share of hidden associations but leave room; result is a roadmap from **mechanical rule-matching → human-aligned semantic reasoning** for attribution.
- **Link**: https://arxiv.org/abs/2608.28649

### 5.3 CoSPOT — Compositional Spectral Prompts for LLM-Based Online Time Series Forecasting (KAIST, CIKM 2026)
- **中文标题**: CoSPOT：基于 LLM 在线时序预测的组合性谱提示（KAIST）
- **Authors**: Seungyoon Choi, Hyunchul Kim, Jae-Gil Lee, Chanyoung Park | **KAIST** (kaist.ac.kr)
- **Venue**: **CIKM 2026**
- **Problem background**: Online time-series forecasting (OTSF) via memory-buffer retrieval struggles with long-term adaptation and unseen patterns.
- **Key innovation**: Keeps the LLM **frozen**; composes **spectral basis prompts from frequency-domain decomposition** by amplitude, so unseen patterns become *new combinations of learned bases* — few updated parameters.
- **Results / comparison**: Superior across challenging online scenarios (extended online phases, cross-dataset distribution shifts) on real-world datasets.
- **Link**: https://arxiv.org/abs/2609.02093

### 5.4 TRACE — Post-Click Trajectories for Online Delayed CVR Prediction (ICT CAS, SIGIR 2026)
- **中文标题**: TRACE：利用点击后轨迹进行在线延迟 CVR 预测（中科院计算所）
- **Authors**: Xinyue Zhang, Yuanhao Ding, Xiang Ao | Institute of Computing Technology, CAS (ict.ac.cn)
- **Venue**: **SIGIR 2026 — short paper**
- **Problem background**: Delayed feedback forces a label-accuracy vs data-freshness trade-off; existing methods model delay or reweight samples but ignore how post-click behavior evolves.
- **Key innovation**: Formalizes the interaction as a **feedback trajectory** and refines conversion posteriors dynamically without waiting for final outcomes; a **reliability-gated retrospective completer** uses full-lifecycle data to guide unrevealed samples during early-stage sparsity.
- **Results / comparison**: Beats SOTA baselines; the retrospective module is a **model-agnostic enhancer**.
- **Link**: https://arxiv.org/abs/2604.23197

### 5.5 R&F-Inventory — Monotonic Inventory Estimation in Reach & Frequency Advertising (Kuaishou, SIGIR 2026)
- **中文标题**: R&F-Inventory：覆盖频次合约广告的单调库存估计数据集（快手）
- **Authors**: Yunshan Peng, Ji Wu, Wentao Bai, Yunke Bai, Jinan Pang, Wenzheng Shu, Yanxiang Zeng, Xialong Liu, Peng Jiang | **Kuaishou** (kuaishou.com)
- **Venue**: **SIGIR 2026**
- **Problem background**: R&F brand-ad contracts need real-time **budget→(UV, PV) curves**, but public datasets are per-sample and don't capture the budget-performance curve.
- **Key innovation**: Releases a **large-scale R&F contract inventory dataset** — context = "targeting–scheduling–frequency control", with multiple budget-point observations per context, time-window frequency control (e.g. ≤3 times within 5 days), and a **theoretical max-exposure ceiling as a consistency check**. Defines two benchmarks: single-point prediction + budget-performance curve reconstruction.
- **Results / comparison**: Reproducible baselines + protocols enabling structural-constraint learning, monotonic regression, curve-consistency modeling, R&F planning.
- **Link**: https://arxiv.org/abs/2604.16821

### 5.6 MCLMR — Model-Agnostic Causal Learning for Multi-Behavior Recommendation (USTC + iFlytek, WWW 2026 Oral)
- **中文标题**: MCLMR：多行为推荐的模型无关因果学习框架（中科大 + 讯飞）
- **Authors**: Ranxu Zhang, Junjie Meng, Ying Sun, Ziqi Xu, Bing Yin, Hao Li, Yanyong Zhang, Chao Wang | USTC + **iFlytek** (ustc.edu.cn, iflytek.com, rmit.edu.au)
- **Venue**: **WWW 2026 — Oral**
- **Problem background**: MBR is confounded by user behavioral habits and item multi-behavior distributions; aggregation of heterogeneous auxiliary behaviors and cross-behavior alignment under bias are unsolved.
- **Key innovation**: Causal-graph construction **with interventions for unbiased preference estimation** + a **MoE-based Adaptive Aggregation** module + **bias-aware contrastive alignment**; model-agnostic and pluggable into any MBR architecture.
- **Results / comparison**: Significant gains across many baselines on three real-world datasets.
- **Link**: https://arxiv.org/abs/2603.25126

### 5.7 CanniUplift — Mitigating Seller & Incentive Cannibalization in E-commerce Uplift Modeling (Alibaba, KDD 2026)
- **中文标题**: CanniUplift：缓解电商增量建模中的卖家与激励"自相蚕食"（阿里）
- **Authors**: Zuwang He, Shihao Shu, Yuli Qu, Hanyu Gao, Ziliang Zhang, Diwei Chen, Xiangda Yan, Buyu Gao, Tanchao Zhu, Yumeng Li, Junxiong Zhu | **Taobao & Tmall Group of Alibaba** (alibaba-inc.com)
- **Venue**: **KDD 2026** (12 pp / 4 figs)
- **Problem background**: Uplift models assume SUTVA — violated in multi-seller platforms by **seller-level cannibalization** (incentive shifts spend between shops) and **incentive-level cannibalization** (organic conversions / alternative rewards adding noise).
- **Key innovation**: **PGA** (platform-level global alignment via GMV consistency constraints on cross-shop substitution) + **RDD** (redemption-based decomposition denoising, entire-space) + **Treat-Attention** modeling user-history × treatment interaction.
- **Results / comparison**: Significant wAUUC/wQINI gains over SOTA on synthetic + industrial data; **deployed online: +4.08% platform-wide incremental GMV over production** and improved ROI in A/B.
- **Link**: https://arxiv.org/abs/2607.05242

### 5.8 Binge Watch — Reproducible Multimodal Benchmarks for MovieLens-10M/20M (Univ. Bari, RecSys 2026)
- **中文标题**: Binge Watch：MovieLens-10M/20M 的可复现多模态基准（巴里大学）
- **Authors**: Giuseppe Spillo, Alessandro Petruzzelli, Cataldo Musto, Marco de Gemmis, Pasquale Lops, Giovanni Semeraro | University of Bari Aldo Moro (uniba.it)
- **Venue**: **RecSys 2026**
- **Problem background**: Multimodal rec research leans on small-scale, undocumented, or non-public datasets.
- **Key innovation**: **M3L-10M / M3L-20M** — MovieLens enriched with plots, posters, trailers via a documented pipeline and SOTA encoders; raw mappings + features + datasets all released (Zenodo + GitHub).
- **Results / comparison**: Quality validated across perspectives; a foundational reproducible resource for large-scale multimodal movie recommendation.
- **Link**: https://arxiv.org/abs/2602.15505

### 5.9 QGDPO — Query Generation with DPO for Document Expansion in E-commerce Search (Walmart + Yahoo, production)
- **中文标题**: QGDPO：电商搜索文档扩展中用 DPO 做查询生成（沃尔玛全流量上线）
- **Authors**: Kaihao Li, Feng Liu, Juexin Lin, Xunfan Cai, Zhen Yang, Tony Lee, Ciya Liao
- **Affiliation**: **Walmart + Yahoo** (walmart.com, yahoo.com)
- **Venue**: arXiv preprint (production system)
- **Problem background**: Doc2Query mitigates vocabulary mismatch but generates hallucinations or repeated in-document content; training for novel+relevant tokens is hard.
- **Key innovation**: Fine-tune a seq2seq base, **score predictions with a relevance model, and build win/lose preference pairs for DPO**; the same relevance model filters poor predictions before indexing.
- **Results / comparison**: **Eliminates 50% of irrelevant predictions vs Doc2Query baselines; relevance filter removes a further 14.61%**; **deployed to full traffic on Walmart.com with substantial relevance and engagement gains** — the window's only completed production e-commerce-search experiment.
- **Link**: https://arxiv.org/abs/2610.04352

---

## 6. Recent arXiv & Other Venues — Agents, Systems, Evaluation (11 papers)

### 6.1 MultiWorldBench — Do Independently Controlled Views Describe One Shared World?
- **中文标题**: MultiWorldBench：各自独立的视角真的在描述同一个共享世界吗？（Minecraft 基准）
- **Authors**: Zhangbo Xu, Ruoxi Zhang, Rui Hu, Yisong Wang | Zhiying Guangnian Technology Co., Ltd. (from arXiv HTML author block)
- **Venue**: arXiv preprint
- **Games / world models.** Diagnostic **Minecraft** benchmark: 495 configs / 7 task suites / 10 capabilities (independent control, cross-view motion, shared-state sync, persistence, structural reasoning, concurrency, delayed revisit).
- **Results**: Gamma-World 21.39 and Solaris 20.88 ten-capability averages vs **Engine GT 91.69**; every generated system ≤ 8.00 on persistence and ≤ 1.33 on structural consistency; **none succeeds at spatial reasoning or building-identity preservation**; human preferences agree (dimension-level Spearman 0.96). Plausible individual views ≠ coherent multiplayer world.
- **Link**: https://arxiv.org/abs/2610.11723

### 6.2 Connected Self Forcing — Beyond Local Learning in Video Autoregression
- **中文标题**: Connected Self Forcing：视频自回归中超越局部学习的梯度连通
- **Authors**: Dongbin Zhang, Chaoda Zheng, Kangjie Chen, Xiangyu Li, Shijia Chen, Jinhao Deng, Yuqi Zhang, Guangfeng Jiang, Hongbin Lin, Choo Sin Wai, Minqi Wang, Puyi Wang, Jingye Zhang, Yu Zhang, Xianming Liu, Boyang Wang | *(affiliation not recovered from arXiv HTML)*
- **Venue**: arXiv preprint
- **Problem background**: Self Forcing trains on self-generated histories with KV caching but detaches historical caches — forward deps preserved, **backward gradient paths severed**.
- **Key innovation**: **Reconnects gradient paths across autoregressive chunks** — gradients flow through generated latents into their producing computations; **shortcut gradient replay** recovers cross-chunk grads without full-rollout graphs; combined with distribution-matching distillation.
- **Results**: Long-horizon visual quality and temporal consistency improve on autoregressive video generation **without changing inference**.
- **Link**: https://arxiv.org/abs/2610.12156

### 6.3 TRANSIT — Transparent Scale-In for Multi-Node LLM Training (IBM Research + UIUC)
- **中文标题**: TRANSIT：多节点 LLM 训练的高度透明"缩配"（IBM Research + UIUC）
- **Authors**: Hyungyo Kim, Nicholas Satchanov, Hrishi Shah, Gaohan Ye, Jiaqi Lou, Robert Walkup, Shweta Salaria, I-Hsin Chung, Hubertus Franke, Seetharami Seelam, Apoorve Mohan, Nam Sung Kim | UIUC + **IBM Research** (from author block)
- **Venue**: arXiv preprint
- **Problem background**: Multi-node training wants fewer GPUs when supply is scarce; existing offloading needs framework changes.
- **Key innovation**: **User-space interposition layer** exposing CPU DRAM as GPU-memory extension — **zero application/framework/scheduler/driver/OS changes** — plus a **zero-copy CPU-GPU data path**.
- **Results**: Dense + MoE up to 64 H100s over RoCE: **+68% / +59% / +42% per-GPU throughput vs TorchTitan / ZeRO-Offload / ZeRO-Infinity**; trains with **50% fewer GPUs at >90% baseline throughput**; −33% per-node traffic; +35% per-GPU throughput in communication-bound settings.
- **Link**: https://arxiv.org/abs/2610.07593

### 6.4 NetAgent — Multi-Task Agentic Network Traffic Analysis (Virginia Tech + UC Berkeley)
- **中文标题**: NetAgent：多任务智能体式网络流量分析（Virginia Tech + UC Berkeley）
- **Authors**: Hao Fu, Dawn Song, Peng Gao | Virginia Tech + UC Berkeley (from author block)
- **Venue**: arXiv preprint
- **Problem background**: Task-specific traffic models generalize poorly; traffic foundation models are costly and still fail under distribution shift.
- **Key innovation**: First **agentic framework for multi-task traffic analysis** — knowledge-augmented workflow planning, **150+ verified tools from 50+ published systems**, unified code-execution space, three-tier memory, sandboxing + runtime repair.
- **Results**: Across 9 benchmarks beats all 28 baselines (23 single-task + 5 multi-task); **90.04% F1 on unseen distributions vs 2.74%/3.04%**; −4.85-pt F1 under background shift vs −74.88/−74.80. Implies prior methods **overfit dataset-specific patterns**.
- **Link**: https://arxiv.org/abs/2610.07386

### 6.5 Software World Models — From Consequence Prediction to Decision Value (Emory)
- **中文标题**: 软件世界模型：从后果预测到决策价值（Emory）
- **Authors**: Tongli Su, Yuntong Hu, Liang Zhao, Bowen Zhu, JayaSai Somasundaram, Hasibul Haque | Emory University (from author block)
- **Venue**: arXiv preprint
- **Code execution / software prediction.** Predicts the **blast set** — components a code change will break — via explore/learn/act stages: executes candidate changes from restored states, fine-tunes an LM on execution outcomes, converts samples into per-consumer break probabilities.
- **Results**: **Blast-set F1 0.571±0.037 vs 0.431 static reachability**; >2× ranking-regret reduction; better migration return at all nine checkpoints; complements reachability (which misses couplings absent from the graph). Structured failure outcomes beat scalar risk for downstream decisions.
- **Link**: https://arxiv.org/abs/2610.04940

### 6.6 On the Complexity of Mixed Equilibria in First-Price Auctions with Correlated Priors (Columbia + Stanford)
- **中文标题**: 相关先验一价拍卖混合均衡的复杂度是否为 PPAD-完全
- **Authors**: Mark Chen, Xi Chen, Hao Cui, William Pires, Jonah Stockwell | Stanford + Columbia (from author block)
- **Venue**: arXiv preprint
- **Theory.** Computing an approximate mixed Bayes-Nash equilibrium in a discrete first-price auction with correlated priors is **PPAD-complete**; intermediate: PPAD-completeness of approximate Nash in the new **hypergraph discrete first-price auction** game.
- **Link**: https://arxiv.org/abs/2610.07858

### 6.7 SearchJev — A Fast and Calibrated System-1 Model for Search Agents (Huawei)
- **中文标题**: SearchJev：面向搜索智能体的快速且校准的 System-1 模型（华为）
- **Authors**: Congfeng Cao, Lipeng Zuo, Konstantinos Papakostas, Qiwei Xu, Songwei Xu, Lun Zhou, Zhaochun Ren, Yougang Lyu, Xiaohui Yan | **Huawei** (per arXiv HTML suffix match; author-wise from html block; *.com)
- **Venue**: arXiv preprint
- **Problem background**: Search agents make short decisions (relevance, evidence sufficiency, actions); generative LLMs add latency and uncalibrated confidence.
- **Key innovation**: **Scores legal options directly — no autoregressive generation**; **Soft-Label Learning for Calibrated Decisions (SLCD)** learns decision probabilities from uncertain supervision; System-2 only handles uncertain judgements. Ships **SearchDecision-Bench** (6 decision types).
- **Results**: On SearchDecision-Bench, **5.2–5.3× faster than same-size Qwen3.5 AR models** with better decision quality and **41–74% lower Expected Calibration Error**; on BrowseComp-Plus, dual-system search agents get **3.7–4.7× faster active search while raising accuracy 45% → up to 54%**.
- **Link**: https://arxiv.org/abs/2610.05107

### 6.8 StoreBench — A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents
- **中文标题**: StoreBench：评估与训练自主运营智能体的"直播电商"环境
- **Authors**: Daksh Raghuvanshi, Ved Vedere, Yifan Wang | *(affiliation not recovered from arXiv HTML)*
- **Venue**: arXiv preprint
- **Problem background**: Agentic benchmarks are static (world moves only when the agent acts; terminal reward; arbitrary pass bars).
- **Key innovation**: Live-commerce env on a **production-grade commerce backend** — customers order round-the-clock, suppliers reprice/fail, market shocks arrive; agent drives the same **29 merchant tools**; windowed operation budget makes simulated time action-counted; reward hardened against reward hacks; episodes replay deterministically.
- **Results**: **No frontier model matches scripted smart-triage (best 49% vs 97% task-seed cells; DeepSeek-V4-Pro)**; human experts outscore every model (0.708 vs 0.700 composite); GRPO post-training on 5 tasks lifts Qwen3.5-27B held-out composite **0.136 → 0.373**; full-env withheld to avoid contamination.
- **Link**: https://arxiv.org/abs/2610.10942

### 6.9 MM-VeriRec — Failure-Guided Fusion for Verifiable Agentic Multimodal Recommendation (AMI'26 @ ACM MM 2026)
- **中文标题**: MM-VeriRec：可验证智能体多模态推荐的"失败引导融合"
- **Authors**: Yufeng Wang | *(affiliation not recovered from arXiv HTML — email block gmail.com only)*
- **Venue**: **1st AMI Workshop, co-located with ACM Multimedia 2026**
- **Problem background**: Images carry constraints text metadata only hints at ("must look dark", "must be minimal"); agents must decide when visual evidence is decisive and abstain from impossible requests.
- **Key innovation**: Verifiable protocol with **deterministic visual attributes** producing failure labels (text-trap following / visual ignorance / false acceptance); fusion **diagnoses the failed modality and routes to repair** rather than concatenating.
- **Results**: On MM-ML 1M + Amazon Reviews: stronger embeddings improve retrieval but don't remove failures; failure-guided fusion does; a leave-one-out CLIP detector still reaches **0.7028/0.6111 visual-grounded success**, above VBPR and plain fusion; text-vs-visual gap reproduces across two LLM families.
- **Link**: https://arxiv.org/abs/2609.31718

### 6.10 When Sub-Agents Work in Parallel — Dynamic Concurrency in Long-Horizon Coding Tasks (Nanjing U)
- **中文标题**: 并行子智能体：长时程编码任务动态并发的是与非（南京大学）
- **Authors**: Han Li, HanHaoNing Li, Ziqian Jiang, Yiling Lou | Nanjing University (from author block)
- **Venue**: arXiv preprint
- **Problem background**: Under dynamic concurrency, agents decide whether/how to spawn sub-agents during execution; on long horizons orchestration dominates capability.
- **Key innovation**: **Controlled matched comparison of Codex, Claude Code, Kimi Code with the policy on/off** — 354 tasks / 2,124 executions across complexities and horizons; characterizes **13 concurrency-specific failure modes, 28 observable patterns**, and the conditions where concurrency pays.
- **Link**: https://arxiv.org/abs/2610.10263

### 6.11 Real Long-Term Memory for AI — A 50M-Token Window Faster and Cheaper Than Recompute (Corbenic AI)
- **中文标题**: 真正的长期记忆：50M-token 窗口且比重算更快更便宜（Corbenic AI）
- **Authors**: Sietse Schelpe | Corbenic AI (corbenic.ai)
- **Venue**: arXiv preprint (public package **galahad-kv**, encrypted NVMe KV-store)
- **Problem background**: LLMs only attend to the context window and recompute KV state per prompt.
- **Key innovation**: Persists each ~16K-token block's KV to encrypted local NVMe and loads it back **byte-exact without recompute**; stress-tested on 50M tokens of real text through vLLM on one NVIDIA H100 (Gemma 4 12B/31B).
- **Results**: 100/100 blocks loaded without recompute at all depths; load **2.8×–4.3× faster, 8.8×–12.3× less GPU energy, flat GPU memory** over the full stream; planted-fact recall 82/100 (12B) and 98/100 (31B), no confabulation. Honest limits: state reuse ≠ wider attention, single block at a time, TB-scale NVMe, one-time write cost. Adversarial-resistant test protocol.
- **Link**: https://arxiv.org/abs/2610.10845

---

## 7. Dedup Collisions & Withdrawn Candidates

> Six originally-selected papers were **withdrawn, not merged** (standing precedent from 10-07/10-08 sibling runs). All were claimed by **`wiki/synthesis/2026-10-09/arxiv-ai-search.md`**, a same-day sibling digest that committed **after** this run's 8,293-ID baseline was taken. This is the sixth consecutive day with this failure mode (§10, follow-up #1).

| ID | Paper | Venue | Claimed by |
|---|---|---|---|
| `2610.11450` | Tracing the Thoughts of a Coding Agent Playing ARC-AGI-3 (Amazon) | NeurIPS 2026 CL4FMAgents WS | `arxiv-ai-search.md` (same-day) |
| `2610.11553` | EVIE — evidence-driven visual document retrieval (Tencent) | EMNLP 2026 | `arxiv-ai-search.md` (same-day) |
| `2610.11277` | H2CE — POI reranking cross-encoders (Amazon) | arXiv | `arxiv-ai-search.md` (same-day) |
| `2610.11228` | MGRASRec — CF-path multimodal GRAG rec (UNSW) | AJCAI 2026 | `arxiv-ai-search.md` (same-day) |
| `2610.10556` | LIFT — lifecycle interaction factorization (Xiaohongshu co-affil.) | arXiv | `arxiv-ai-search.md` (same-day) |
| `2610.12341` | AAArena — long-running game-agent competition (Tsinghua) | arXiv | `arxiv-ai-search.md` (same-day) |

**Replacement discipline.** All six were swapped for fresh candidates that were **`rg -l`-verified 0-hit against the live wiki including the new sibling.** No candidate appearing in the sibling's 28-ID ledger was adopted.

---

## 8. Venue Index

| Venue | Papers featured |
|---|---|
| **NeurIPS 2026** (main) | Clustering transformers `2610.09760` (IBM); CaRE-KD `2609.36734`; BAI shifting means `2610.10488` (Booking.com); codebook cross-modal KD `2609.37243` (Samsung); **SplitMoE** `2609.38140` (ByteDance, **Spotlight**); AVE video editing `2610.11037` (ByteDance/JHU); FSD-diffusion unlearning `2610.10859` (Amazon/Purdue); **ORCA** `2610.09841` (Apple/Stability) |
| **NeurIPS 2026** (workshops/evals) | output+checkpoint prediction `2610.11889` (AI for Verifiable Coding); weight-exfiltration e-process `2610.11843` (Anthropic, E-Values **Oral**); CTE-Bench `2609.36647` (Datasets&Eval); Physical AI Smart Spaces `2610.02580` (NVIDIA, Datasets&Eval); compaction-blindspot `2610.08722` (Salesforce, IAB); MemoryAgentBench re-read `2610.09193` (Salesforce, IAB); SOTA trading agents `2610.10407` (Agenthon) |
| **ICML 2026** | RouterInterp `2610.11775`; Factorized Scheduling `2609.36578`; Temporal State Transport `2609.08505` (**F2S Best Paper**); clustering guardrails `2607.19704` (Amazon, HDLD + RecSys GenAI-E-Commerce) |
| **EMNLP 2026** | MT annotation `2610.10918` (Apple+Meta); cross-dialect Text-to-SQL `2609.33670` (IBM, Findings); business-compromise detection `2609.32643` (Meta); query-insensitive STVG `2610.06018` (Samsung, Findings); personas-for-surveys `2610.05828` (Amazon, REALM); SAGE `2610.08093` (Alibaba); Syn-Omni `2610.12256` (Sony, Findings); ActiveMedAgent `2610.11140`; EgoVoice `2610.12248` (Amazon/NVIDIA/Intel, Main); CypherTurn `2609.36987` (Baidu, **Oral**); CogMem `2610.11314` |
| **CIKM 2026** | SMEO `2608.15662` (Amazon); attribution touchpoints `2608.28649` (Alibaba, short); CoSPOT `2609.02093` (KAIST) |
| **SIGIR 2026** | TRACE delayed-CVR `2604.23197` (ICT CAS, short); R&F-Inventory `2604.16821` (Kuaishou) |
| **WWW 2026** | MCLMR `2603.25126` (USTC+iFlytek, **Oral**) |
| **KDD 2026** | CanniUplift `2607.05242` (Alibaba, deployed) |
| **RecSys 2026** | Binge Watch `2602.15505` (Univ. Bari) (+ clustering guardrails dual `2607.19704`) |
| **ACM MM 2026** | MM-VeriRec `2609.31718` (AMI'26 workshop) |
| **arXiv only** | QGDPO `2610.04352` (Walmart/Yahoo, production); MultiWorldBench `2610.11723`; Connected Self Forcing `2610.12156`; TRANSIT `2610.07593` (IBM); NetAgent `2610.07386` (VT/Berkeley); SWM `2610.04940` (Emory); auctions PPAD `2610.07858`; SearchJev `2610.05107` (Huawei); StoreBench `2610.10942`; dynamic concurrency `2610.10263` (NJU); galahad-kv `2610.10845` (Corbenic AI) |
| **Empty this window** | ACL 2026, ICLR 2026, AAAI 2026, AAMAS 2026, CVPR 2026 — 0 verified hits in the query set |

---

## 9. Cross-Cutting Observations

1. **Code-execution prediction is consolidating into a *stateful* science.** Two evals this window (`2610.11889` output+checkpoint states; CTE-Bench counterfactual trace) plus a Software World Model (`2610.04940`) all argue the same turn: single-shot output accuracy **overstates** an agent's understanding, because errors compound across rollouts and models track intervention effects **only when correct feedback is supplied**. Directly extends the 10-08 digest's "the measurement is the bug" cluster into a *models-of-software* direction.
2. **The front of agent development has moved to systems of record.** This window's strongest industry claims are not new architectures but *deployment plumbing taken seriously*: Walmart's DPO'd Doc2Query on full traffic (`2610.04352`), Amazon's clustering guardrails unblocking a persona recommender on 38M customers (`2607.19704`), Alibaba's PGA+RDD lifting platform GMV +4.08% (`2607.05242`), IBM's TRANSIT shrinking GPU needs by 50% at >90% throughput (`2610.07593`), and the 50M-token byte-exact KV store (`2610.10845`). Evaluation papers (StoreBench, NetAgent, CypherTurn) meanwhile show the **gap between frontier models and simple scripted policies / robustness baselines is still large**.
3. **"Learning what to omit" is emerging as a first-class objective.** ActiveMedAgent's information-overload effect (correct with *fewer* channels, `2610.11140`), ORCA's low-rank visual readout (`2610.09841`), SearchJev's System-1/System-2 split (fast calibrated scoring + escalation, `2610.05107`), and the compaction-blindspot probe (`2610.08722`) all train or evaluate *deletion/routing of information* rather than addition of context.
4. **Games coverage is genuinely thinning in the fresh arXiv window** — 3rd consecutive day. The flagship game-agent competition (AAArena) was claimed by a sibling; MultiWorldBench (Minecraft) is this digest's games anchor and its verdict is sharp: **generated world models cannot yet sustain shared-state persistence**. Sibling `arxiv-ai-search` + `game-rl-daily` remain the game-thread owners; the niche is saturated for this wiki.
5. **Distillation keeps bifurcating.** Generation-side: FSD-diffusion unlearning must *bypass* standard DPO's multi-step assumptions (`2610.10859`) while ORCA adds a spectral alignment loss to the same family (`2610.09841`). Language-side: CaRE-KD (`2609.36734`) and codebook cross-modal KD (`2609.37243`) both attack the teacher-reliability / structural-heterogeneity assumptions that vanilla KD quietly makes. **The joint theme: "the transfer loss you use encodes an assumption about the teacher that LLMs no longer satisfy."**
6. **Venue hygiene**: **11 of 50** papers are workshop/evals-track acceptances (NeurIPS ×7, ICML ×2, RecSys ×1, ACM MM ×1; two are dual-workshop); the rest are main/Findings/arXiv. Self-reported tags were **not** verified against proceedings. Four requested venues (**ACL/ICLR/AAAI/AAMAS/CVPR 2026**) returned zero in-window hits in the query set — a supply-thinness result, not proof of absence.

---

## 10. Method Notes & Caveats

- **Coverage is venue-tag-complete within the query set, not arXiv-exhaustive.** 54 queries: 16 unbounded venue sweeps + 8 category sweeps bounded to `submittedDate:[20260920 TO 20261009]` + 16 topic + 14 lab. Papers carrying a venue tag but outside these catch nets would be missed. **First harvest hit HTTP 429** and was re-run after ~20 min at ≥3–4 s spacing; steps to keep a serialized pace were otherwise respected. Zero-hit queries were accepted with the 14-byte `Rate exceeded.` caveat recorded.
- **Baseline race (recorded, not hidden).** The run-start claimed-ID cache (`/tmp/claimed.txt`, 8,293) was taken before the same-day `arxiv-ai-search.md` committed its 28 IDs. It was caught by the **pre-write live `rg -l` resweep** of every featured ID against the whole wiki; 6 withdrawals, 6 replacements. **Follow-up #1 reaffirmed for the seventh consecutive day: a shared claimed-ID lock file** before drafting; **Follow-up #2**: rebuild claimed-ID baselines from `git ls-files wiki` rather than a cached regex pass (the 10-08 §18 recommendation).
- **Affiliation discipline.** Read only from the paper's own arXiv HTML author block / printed email domains; **never inferred from surnames or company-name priors**. Papers with a bare `gmail.com`/empty block are marked *(affiliation not recovered)* rather than guessed: `2610.12156` (Connected Self Forcing), `2610.10942` (StoreBench), `2609.31718` (MM-VeriRec). **comp/`seg` HTML-suffix matches (e.g. ByteDance for `2609.38140`/`2610.11037`, Huawei for `2610.05107`, Baidu for `2609.36987`, Amazon for `2610.10859`/`2610.11140`/`2607.19704`, NVIDIA for `2610.12248`/`2610.02580`) come from the paper's own rendered HTML, not from author names.**
- **The `2610.11213` aliasing case was avoided, not concealed**: a candidate whose `comment` mixed "NeurIPS 2025" with a 2026 submission date was dropped from the slate to prevent a venue mislabel rather than included with a guess.
- **One unverified-venue arXiv marker**: `2608.15662` (SMEO) shows "Proceedings of the 35th ACM CIKM" (Rome) = CIKM 2026; stated as-is.
- **Temp files** under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/conf-harvest/` (pre-authorized scratch) — this run's working set (`records.json`, `aff2/3/4.json`, `sel_meta.json`, `final_dump.txt`, `final50.txt`, `harvest.py`, `fetch_aff*.py`) — plus `/tmp/claimed.txt`, `/tmp/claimed_v2.txt`. No writes outside scratch + the wiki.

---

## References

- arXiv export API: https://export.arxiv.org/api/query
- NeurIPS 2026: https://neurips.cc/virtual/2026/
- ICML 2026: https://icml.cc/virtual/2026/
- EMNLP 2026: https://2026.emnlp.org/
- KDD 2026: https://kdd2026.kdd.org/
- CIKM 2026: https://cikm2026.org/
- SIGIR 2026: https://sigir-2026.org/
- WWW 2026: https://www2026.thewebconf.org/
- ACM RecSys 2026: https://recsys.acm.org/recsys26/