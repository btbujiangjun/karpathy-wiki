---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-23
updated: 2026-09-23
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, games, RecSys, time-series, MoE, quantization, KV-cache, speculative-decoding, world-models, agentic-engineering, mechanism-design, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-23

Generated: 2026-09-23 (Wednesday). **Topic-targeted sweep of the fresh Wednesday 23 Sep 2026 mailing** (IDs **2609.25006–2609.26796**). **449 unique IDs parsed** from 10 category listing pages (cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.SI, cs.CY, cs.CV), **0 pre-claimed** in `wiki/` at build time (5,552-ID known set); **22 papers featured in full + 6 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/`** at selection time.

**Methodology**: Direct page fetches of `/list/{cat}/new` for the ten categories (all announce **Wednesday, 23 September 2026**); ~45 title-keyword screened on target topics (AI / LLM / recommendation / advertising / sequential modeling / long-tail / CTR / games / agentic engineering / time series / MoE / quantization / KV cache / mechanism design), full abstracts fetched for 37 via the arXiv API (`export.arxiv.org`). Probe HTML/API XML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search-0923/`. Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).

> **Dedup note**: At write time this was the 09-23 window's first claim (`arxiv-daily`/`arxiv-paper-check`/`game-rl-daily`/`conference-digest` for 09-23 had not yet written); all 28 curated IDs are **disjoint from every 09-21/09-22 sibling-claimed set** (09-21 daily 49 IDs, 09-21/09-22 ai-search features, 09-22 daily 320 IDs) — verified by the 5,552-ID full-wiki grep at build time plus per-ID greps. Post-hoc cross-check against the concurrently-written 09-23 `arxiv-daily`: **one shared feature — 2609.25825 (Spotify QSS)** — was independently claimed by both reports in the same window race (the daily's §1.2, this report's §1.3); all other 27 curated IDs remain exclusive to this report. Future same-window sweeps should treat 2609.25825 as already covered by either report and skip the remaining IDs listed here.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Wed 23 Sep 2026 mailing; IDs 2609.25006–2609.26796 (fresh, all 10 categories parsed) |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.SI, cs.CY, cs.CV |
| Unique IDs parsed | 449 (all fresh; 0 already claimed in `wiki/`) |
| Featured in full in this report | 22 papers (6 sections) + 6 shortlisted runner-ups |
| Direct advertising / CTR / pCTR papers | **0** (`rg -i "advertis|click|CTR|bidd|auction"` over all 449 titles → only DSA "Click, Branch, Audit" toolkit + Auction Bridge card game; no commercial CTR/advertising ML) |
| Rec/interaction relevance | 3 production-adjacent rec/search papers (YouTube Light Heads multitask, Spotify QSS LLM reranking, TailSpec-EASE long-tail KG rec) + Traffic/TS lines |
| Mailing status | `/new` pages announce Wed-23 at fetch time; window terminated at **2609.26796** (cs.CL max) |

**Theme of the window**: the Wed-23 window concentrates **recommendation & search engineering** (YouTube multi-task head injection, Spotify behavioural-stat LLM reranking with feature dropout, long-tail KG-regularized linear rec), **probabilistic/streaming time-series foundations** (zero-shot TSFM reliability benchmark, training-free marginal coupling, streaming interactive TS), **MoE & quantization for serving** (dynamic expert pruning in fine-grained MoE, disaggregated prefill/decode quantization, activation-aware mixed-precision), **KV-cache/attention engineering** (HySparse2 two-level KV sharing, CompKV compensation-aware selection, exact-match attention theory), **reasoning & test-time scaling** (learned search policies, hill climbing sampling, rollout-efficiency taxonomy) and a **strong agentic-engineering + world-model cluster** (SWE-Serve inference-serving benchmark, Agensh 1,024-agent, CliffCompaction, CoDeR, GameDirector). Games side is thin at the daily layer but includes a solid mechanism-design entry (prophet inequalities beyond utilitarian welfare) and Auction Bridge CFR analysis.

---

## 1 Recommendation, Search & Ranking

### 1.1 Lightweight Ranking Heads — Multi-Task Head Injection at YouTube Scale (2609.25433)
- **Title**: Lightweight Ranking Heads: Accelerating Multi-Task Experimentation in Production Recommender Systems
- **Authors**: Sanjay Surendranath Girija, Aniruddh Nath, Li Wei, Yanhao Jiang, Shawn Andrews, Lukasz Heldt, Yi Wu, Aditya Mahajan, Mohit Sharma
- **Institution**: Google / YouTube (tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG); **ACM RecSys 2026 — Online and Adaptive Recommender Systems workshop**
- **arXiv**: https://arxiv.org/abs/2609.25433
- **Abstract**: Production-scale multi-task ranking models make adding a new prediction task costly and risky — negative task conflicts with existing tasks, plus expensive retraining of backbones/downstream heads and reward-combination tuning. **Light Head framework** enables **dynamic injection of new tasks** into existing multi-task ranking models for continuous online learning, **without model cold-start or backbone retraining**. Stop-gradients + stateless daily training strictly isolate new heads → adverse task conflicts suppressed; a **centralized configuration** lets one head be added to several models at once, unblocking faster training-data generation and downstream co-training. Deployed at **YouTube scale**: iteration cycle for multi-task experimentation cut from weeks to days.
- **Key Innovations**: (1) head-level task injection obviating backbone retraining (no cold-start, stateless daily training); (2) stop-gradient task isolation as conflict control; (3) centralized multi-model head config = the production rec "experimentation velocity" win (weeks → days).
- **Venue**: RecSys 2026 (OARS workshop).

### 1.2 TailSpec-EASE — Knowledge-Graph-Regularized Linear Rec for Long-Tail Discovery (2609.26143)
- **Title**: TailSpec-EASE: Knowledge-Graph-Regularized Linear Recommendation for Web Long-Tail Discovery
- **Authors**: Jianru Shen
- **Institution**: single author (*tentative*)
- **Date**: online 08 Aug 2026, listed Wed 23 Sep 2026 (cs.IR); **WISE 2026** (main research track)
- **arXiv**: https://arxiv.org/abs/2609.26143
- **Abstract**: Recs over-serve popular items; item-side KGs (RDF/linked data) can link sparse items via shared semantics, but top KG-aware recs need GNN architectures while strong shallow linear models (EASE-R) ignore side info and can be infeasible in global closed form. **TailSpec-EASE** injects a **relation-aware spectral KG prior** into a **local closed-form reconstruction objective**, with prior strength adapting to item popularity (stronger guidance for long-tail items). Across 4 public benchmarks vs classical/linear/graph-CF/KG-neural/score-level baselines: favorable accuracy–long-tail–cost trade-off; **+24% NDCG@20 over the no-KG counterpart**; tail gains statistically significant (paired bootstrap). Amazon-book timing: **37 s CPU** vs 2,584 s GPU (KGAT) and 15,800 s reference run.
- **Key Innovations**: (1) spectral KG prior inside a *local* closed-form EASE objective (no GNN, no global closed form); (2) popularity-adaptive regularization targeting the long tail; (3) cost evidence: CPU trainable ~70–430× cheaper than KG-NN baselines.
- **Venue**: WISE 2026 main track.

### 1.3 Robust LLM Reranking with Behavioural Feature Dropout — Audio Streaming Personalisation (2609.25825)
- **Title**: Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised Search
- **Authors**: Aleksandr V. Petrov, Nathan Stein, Erik Lybecker, Emma Schüldt, Daniel Lazarovski, Hugues Bouchard, Mounia Lalmas
- **Institution**: Spotify-aligned (Lalmas, Bouchard; tentative)
- **Date**: Wed 23 Sep 2026 (cs.IR); **RecSys 2026 USRW workshop**
- **arXiv**: https://arxiv.org/abs/2609.25825
- **Abstract**: Personalised search must balance query intent with user context/history. LLM cross-encoders give a single rerank interface, but injecting predictive behavioural statistics in the prompt encourages **shortcut learning** — leaning on historical signals at the expense of semantics that generalize to sparse/unseen searches. On a large-scale **audio-streaming platform** search system, Query Slice Stats (QSS) summarize historical success per query–candidate pair. Naive QSS injection lifts ranking when available but hurts robustness when removed. **Deterministic dual-sample feature-dropout training** shows each example once with QSS and once without. Offline: QSS injection +13.3% when present; dual-sample keeps those gains and improves QSS-removed evaluation by **+4.0%** vs naive training. **Live online**: both QSS-aware variants ≈ +2% search success; cold-start comparison directionally confirms offline.
- **Key Innovations**: (1) names shortcut learning in behavioural-prompt LLM reranking; (2) dual-sample feature-dropout as a cheap robustness fix; (3) rare RecSys 2026 online-test evidence (+2% live search success) pairing offline conditioning.
- **Venue**: RecSys 2026 USRW workshop.

---

## 2 Sequential Modeling, Time Series & Probabilistic Forecasting

### 2.1 Zero-Shot TSFM Reliability — Accuracy vs Calibration Across Six Foundation Models (2609.25788)
- **Title**: Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models
- **Authors**: Panagiotis Michael, Moysis Symeonides, Demetris Trihinas
- **Institution**: University of the Aegean-aligned (Trihinas; tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG); **ADBIS 2026**
- **arXiv**: https://arxiv.org/abs/2609.25788
- **Abstract**: TSFMs promise zero-shot forecasting without task-specific training, but prior work under-checks the **accuracy–calibration trade-off**. Benchmark of **six TSFMs** on energy/traffic/financial datasets vs statistical baselines + a supervised DL model. TSFMs beat statistical and supervised baselines, yet show a fundamental point-accuracy vs probabilistic-reliability trade-off: **xLSTM architectures give robust probabilistic calibration across horizons**; **patch-based transformers are accurate but miscalibrated at long horizons**; transformer-based models show context-saturation points for optimal zero-shot reasoning.
- **Key Innovations**: (1) first systematic accuracy–calibration joint evaluation of TSFMs against supervised DL; (2) architecture-level finding (xLSTM calibration vs patch-transformer long-horizon miscalibration); (3) practical guidance for balancing generalization and UQ in zero-shot deployment.
- **Venue**: ADBIS 2026.

### 2.2 Interweaving Marginals — Training-Free Dependence Construction for Probabilistic TSFMs (2609.25980)
- **Title**: Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models
- **Authors**: Jinmyeong Choi, Jinkwan Jang, Seul Lee, Taesup Kim
- **Institution**: Seoul National University-aligned (Kim; tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.25980
- **Abstract**: Probabilistic TSFMs emit **coordinate-wise predictive distributions**, but marginals don't determine a joint over multivariate future trajectories. Studies **training-free coupling of frozen TSFM marginals** into joint sample paths. Evaluation fixes the empirical marginal sample multiset at every channel–horizon coordinate to isolate coupling's effect: historical temporal and channel relationships substantially improve dependence diagnostics; the pattern persists when the fixed-marginal constraint is removed and under native multivariate backbone inference.
- **Key Innovations**: (1) treats dependence reconstruction as a *distinct post-processing problem* for probabilistic TSFMs; (2) fixed-marginal experimental design cleanly isolates coupling effects; (3) cross-checked under native multivariate backbones (not only shared-marginal setups).
- **Venue**: Preprint.

### 2.3 TimeInteract — Real-Time Interactive Intelligence for Streaming Time Series (2609.26389)
- **Title**: TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series
- **Authors**: Sheng Pan, Yongli Gu, Yiqing Guo, Warren Jin, Bo Du, Shirui Pan, Ming Jin
- **Institution**: Monash / QUT / Wuhan University-aligned (Pan, Jin; tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.26389
- **Abstract**: Existing TSLMs are static: they consume complete sequences offline or alternate streaming-input vs response generation, blocking new observations during interaction. Introduces the **Time-Series Interaction** regime — a model continuously perceives incoming observations + user intent, autonomously decides when to stay silent or respond, and **keeps processing new observations during response generation**. **TimeInteract**: dual-view streaming TS encoder (local variation + historical dynamics), a response-control mechanism (when to trigger), and **decoupled streaming inference** (control separated from generation so later observations aren't blocked). Defines an interaction-capability hierarchy (Understanding → Adaptivity) and constructs **StreamTSI-34K** (34,588 episodes, 77,505 responses; synthetic + real, single-/multi-turn).
- **Key Innovations**: (1) streaming-by-construction TS interaction (respond while still consuming); (2) decoupled control-vs-generation inference loop; (3) StreamTSI-34K dataset + 4-level capability taxonomy as a benchmark contribution.
- **Venue**: Preprint.

---

## 3 MoE, Quantization & Serving-Oriented Inference

### 3.1 Dynamic Expert Pruning in Fine-Grained MoE — You Only Need 2/3 of Chosen Experts (2609.25809)
- **Title**: You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs
- **Authors**: Yuanteng Chen, Qiwei Lai, Chen Tianqi, Peisong Wang, Yuantian Shao, Nanxin Zeng, Zhilei Liu, Chuangyi Li, Jing Liu, Jian Cheng
- **Institution**: NLPR/CASIA + industrial-aligned (Cheng, Liu; tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.25809
- **Abstract**: Fine-grained MoE (hundreds of experts, many selected per token) makes dynamic expert pruning attractive, but evidence comes mostly from coarser archs and likelihood-choice benchmarks. Systematic study of **12 fine-grained MoE checkpoints across 9 architecture families**, core suite of 11 benchmarks (knowledge QA, math, code, reasoning). Finding: selection is far more redundant than assumed — **uniformly retaining ≈2/3 of selected experts preserves 98.8% of unpruned performance**, via a one-integer change, with **1.2–1.7× measured speedup** on two serving backends. At conservative budgets this simple baseline leaves little headroom for dynamic rules (best published rules differ <1% at matched budgets); their value emerges under aggressive pruning.
- **Key Innovations**: (1) the "2/3 uniform baseline" fact — a strong, embarrassingly simple operating point for fine-grained MoE serving; (2) 12-checkpoint/9-family/11-benchmark evidence base overhauling the coarse-arch consensus; (3) clarifies when dynamic allocation actually matters (aggressive pruning regime).
- **Venue**: Preprint.

### 3.2 Disaggregated Quantization — Specializing LLM Prefill and Decode (2609.26333)
- **Title**: Disaggregated Quantization: Specializing LLM Prefill and Decode
- **Authors**: Andrei Panferov, Maximilian Kleinegger, Sweta Priyadarshi, Tijmen Blankevoort, Dan Alistarh
- **Institution**: IST Austria / Qualcomm AI-aligned (Alistarh, Blankevoort; tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.26333
- **Abstract**: Prefill and decode reward different quantization: low-precision arithmetic accelerates prompt processing, compact weights reduce decode memory traffic. Proposes **disaggregated quantization (DQ)**: separate computation formats, weights, and storage placement per phase. On Qwen 3 / Gemma 3, **removing activation quantization on decode alone** improves decode-heavy accuracy at no inference cost. Trained compute-native **prefill weights** accelerate prompt processing vs weight-only inference at 2–3-bit decode. With released Qwen3.8-27B GGUF decoders, an NVFP4 prefiller improves **1-bit accuracy by +32.5 (MMLU-Pro) / +35.3 (MMMU-Pro)** without touching the decode checkpoint. **Offloaded disaggregated prefill (ODP)** streams prefill weights from SSD: **1.78× time-to-first-token** at 8K prompt length (llama.cpp) vs weight-only baseline. Validated in vLLM and up to 2.8T-param PTQ.
- **Key Innovations**: (1) phase-disaggregated formats/weights/storage as a first-class design axis; (2) decode-unquantization trick (accuracy for free on decode-heavy tasks); (3) ODP SSD streaming — TTFT speedup without larger device memory.
- **Venue**: Preprint.

### 3.3 HySparse2 — Hybrid Sparse Attention with Two-Level KV Sharing (2609.26368)
- **Title**: HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing
- **Authors**: Jianyu Wei, Yizhao Gao, Qihao Zhang, Shimao Chen, Zhengju Tang, Yu Cheng, Shengjie Zhou, Zihan Jiang, Yifan Song, Hailin Zhang, Liang Zhao, Bo Yang
- **Institution**: academic/industrial (*tentative*)
- **Date**: Wed 23 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.26368
- **Abstract**: Long-horizon/multi-turn agents generate short actions over long tool/environment observations — demanding efficient prefill, small KV cache, accurate long-context retrieval. **HySparse2**: hybrid sparse attention with two-level KV sharing. **Outer**: KV Bridging (YOCO-style self/cross-decoder) but only full-attention layers are bridged; self-decoder uses hybrid SWA, cross-decoder hybrid sparse attention; cross-decoder full-attn KV caches are *generated from self-decoder hidden states*. **Inner**: HySparse's KV Reuse refined by (a) **token-level (not block-level) sparsity** for finer retrieval and (b) folding SWA into sparse selection (no separate SWA branch). All cross-decoder caches derive from self-decoder states → **prefill exits after the self-decoder**, skipping all cross-decoder layers. On **80B-A3B MoE**: beats HySparse and Hybrid SWA on long-context retrieval and multi-turn agentic tasks.
- **Key Innovations**: (1) two-level KV sharing letting prefill terminate mid-network; (2) token-level sparsity + fused sliding window in sparse layers; (3) long-context/multi-turn agentic workload evidence on 80B-A3B.
- **Venue**: Preprint.

### 3.4 CompKV — Compensation-Aware KV Selection for Long-Context Inference (2609.26300)
- **Title**: CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference
- **Authors**: Zhen Huang, Ruizhe Yao, Danyi Liu, Xinrui Chen, Shuwei Li, Siru Zhong, Zijian Cao, Yushan Lai, Mingming Guo, Weijie Zheng, Haohuan Fu
- **Institution**: Tsinghua-aligned (Fu; tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.26300
- **Abstract**: KV-cache traffic bottlenecks long-context inference; sparse attention accelerates by computing exact attention on a selected token subset and *compensating* the omitted tail coarsely. Existing methods pick tokens by attention mass first, compensate second — missing their interaction: selection should prefer tokens whose omission leaves the largest compensation error. **CompKV** is the first **compensation-aware sparse attention** framework: token-block selection is **jointly optimized for the downstream compensation mechanism**. Theory: the residual of block-level mean compensation is governed by *block attention mass + within-block logit variation*, approximated with compact block statistics → deployable criterion + async implementation. On RULER and LongBench-Pro, CompKV is best among evaluated sparse baselines with up to **6.85× self-attention speedup**.
- **Key Innovations**: (1) selection–compensation co-design (vs decoupled mass-then-compensate); (2) a deployable criterion with an information-theoretic-selection justification; (3) async implementation with 6.85× speedup on standard long-context benchmarks.
- **Venue**: Preprint.

### 3.5 TSS — Target-Side Sparsification for Speculative Decoding (2609.26100)
- **Title**: TSS: Target-Side Sparsification for Speculative Decoding in Domain-Specific Large Language Models
- **Authors**: Haibo Hu, Lianming Huang, Qiao Li, Nan Guan, Chun Jason Xue
- **Institution**: City University of Hong Kong-aligned (Guan, Xue; tentative)
- **Date**: online 15 Aug 2026, listed Wed 23 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.26100
- **Abstract**: Speculative decoding accelerates LLM inference via a lightweight drafter + target verifier; prior work focuses on the draft side, keeping the target dense. Shows that in domain-specific inference, **full-depth target verification is not always optimal**: skipping selected target layers can reduce verification cost *while increasing draft acceptance* and preserving/improving performance. **TSS**: acceptance- and metric-aware breadth search over multi-layer skip configurations (no fixed objective priority), stored in a domain→configuration map applied by a lightweight skip controller — one target model supports multiple sparse verification paths **without retraining or permanent pruning**. On Spec-Bench across domains/scales/methods: consistent acceptance + downstream gains — e.g. Translation accept length **2.70→4.53 (+67.8%)**, BLEU **0.131→0.237 (+80.9%)**.
- **Key Innovations**: (1) target-side (not draft-side) sparsification — a convention flip; (2) dual-objective breadth search producing reusable domain configs; (3) no-retrain multi-path verification control.
- **Venue**: Preprint.

---

## 4 LLM Reasoning, Test-Time Scaling & Post-Training RL

### 4.1 Beyond Repeated Sampling — Learning Search Policies for LLM Reasoning (2609.26704)
- **Title**: Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning
- **Authors**: Ismail Labiad, Matthieu Kowalski, Marc Schoenauer, Rémi Munos, Julia Kempe
- **Institution**: INRIA / Google DeepMind / NYU-aligned (Munos, Schoenauer, Kempe; tentative)
- **Date**: Wed 23 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.26704
- **Abstract**: Dominant test-time strategy = naive repeated sampling, whose exploration is limited to local decoding noise → many near-duplicate attempts. Explores **semantic-level exploration**: sample problem-specific *concepts, hints, or strategies* first, then condition answer generation on them; refines into a procedure emitting many diverse concepts in one trajectory; and makes concept generation **trainable** — a small RL-optimized concept generator maximizes downstream pass of a larger frozen answer generator. On hard math reasoning, the trained concept generator **beats naive repeated sampling at equal answer-generation allocation**, surpasses concepts from much larger untuned models, and **transfers to unseen answer generators including cross-family**.
- **Key Innovations**: (1) concept-space search policy as a first-class test-time lever (vs decoding noise); (2) a small model trained into a reusable search policy that transfers across answer models/families; (3) clean pass@k-vs-allocation comparison against repeated sampling.
- **Venue**: Preprint.

### 4.2 Hill Sampling — Simpler Than Evolution or Test-Time Training (2609.25510)
- **Title**: Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training
- **Authors**: Jacob Beck, Philip V. Ogren, Ari Kobren
- **Institution**: MIT-IBM Watson AI Lab-aligned (Kobren; tentative)
- **Date**: Wed 23 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.25510
- **Abstract**: Asks how much evolution/search/test-time-training machinery is necessary. **Hill Sampling**: repeatedly sample candidate program edits from a ***frozen*** LLM, keep the best program, condition all later samples on it. On circle packing, sums/differences-of-sets, and Erdős minimum-overlap: **new SOTA on circle packing** among published methods, **improves over AlphaEvolve** on Erdős, strong on sums/differences — in hours on 8×H100. Also the largest-by-param-count study of evolution strategies applied to **LLM weights at test time**: learning the weights is *worse* than ES learning rate = 0 (fixed random weight perturbations still help).
- **Key Innovations**: (1) a nearly parameter-free frozen-model hill-climbing baseline matching/besting elaborate harnesses; (2) large-scale ES-on-LLM-weights negative result (weight learning < zero-LR perturbations); (3) strong empirical externals (circle packing SOTA, AlphaEvolve reference).
- **Venue**: Preprint.

### 4.3 Rollout Efficiency in RL for Reasoning LLMs — Taxonomy & Directions (2609.25463)
- **Title**: Rollout Efficiency in Reinforcement Learning for Reasoning Large Language Models: A Taxonomy and Future Directions
- **Authors**: Niloofar Gholipour, Marcos Assuncao, Gursimran Singh, Timothy Yu, Rajkumar Buyya, Julien Gascon-Samson, Zhenan Fan, Yong Zhang, Xiaojie Xu, Yaqiang Yao, Xiaolong Bai
- **Institution**: University of Melbourne / Concordia / industry-aligned (Buyya; tentative)
- **Date**: Wed 23 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.25463
- **Abstract**: Reasoning-oriented RL shifts a large share of training cost to **rollout** (trajectory generation). Survey classifies recent research on rollout efficiency from **mechanism and bottleneck perspectives**, analyzes which technique families address which inefficiency sources, where they can combine vs conflict, gaps in efficiency-gain reporting, and open problems (freshness/consistency/statistical validity of rollout data).
- **Key Innovations**: (1) first systematic rollout-efficiency taxonomy for reasoning RL (mechanism + bottleneck axes); (2) combination-conflict analysis across efficiency technique families; (3) a reporting-gap critique of the field's efficiency claims.
- **Venue**: Preprint (survey).

---

## 5 Agents: Serving, Scaling, Compaction & Delivery

### 5.1 SWE-Serve — Benchmarking Agentic Engineering for Production Inference Serving (2609.26777)
- **Title**: SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving
- **Authors**: Jennifer Williams, Dave Farris, Jeff Farris, Jiantao Jiao
- **Institution**: UC Berkeley-aligned (Jiao; tentative)
- **Date**: Wed 23 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.26777
- **Abstract**: Implementing an inference feature requires coordinated changes across model support, runtime execution, and public APIs — existing benchmarks miss this (repo-SWE benchmarks aren't inference-targeted; terminal-agent benchmarks include too few inference tasks; kernel benchmarks isolate single kernels). **SWE-Serve**: **53 repository-grounded tasks** from recent production changes to **SGLang**, spanning **six inference-engineering families**; each runs on CPU or single H100 with hidden functional/regression tests incl. e2e serving tests and calibrated performance gates; executable no-op/oracle controls, adversarial verifier review, closed-book execution preserve validity. Across **11 models × 31 model-effort configs**, best = **75% mean pass@1**, and the benchmark exposes a large local-completion → production-correctness gap.
- **Key Innovations**: (1) first benchmark targeting repository-scale *inference-engineering* feature work (vs kernels or generic SWE); (2) hidden e2e serving tests + calibrated performance gates (not just unit pass); (3) 11-model effort study quantifying the local→production gap.
- **Venue**: Preprint.

### 5.2 Agensh — Organisational Intelligence at 1,024 Agents Without a Central Orchestrator (2609.26781)
- **Title**: Agensh: Scaling Organizational Intelligence to 1,024 Agents
- **Authors**: Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei
- **Institution**: Microsoft Research-aligned (Wei, Dong, Huang; tentative)
- **Date**: Wed 23 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.26781
- **Abstract**: Multi-agent systems reduce latency by concurrent work, but harnesses bottleneck on a **central orchestrator**. **Agensh**: self-organized multi-agent harness with **no central orchestrator** — concurrent workers run a cooperation loop (gather context, claim/self-assign sub-tasks, act + share findings, verify, merge asynchronously), supported by a shared workspace, message interface, and shared context. On the five hardest **ProgramBench** tasks (GPT-5.6-sol): 1→128 agents lifts final test-pass rate **19.31%→28.78% (≈+49% rel)**; on **pandoc**, 1→1,024 agents raises it **33.89%→55.06%**; larger orgs reach comparable rates earlier.
- **Key Innovations**: (1) orchestrator-free, self-assigning multi-agent loop (scales to 1,024); (2) shared-workspace/message/context infrastructure as the scaling medium; (3) measured scaling curves showing ~1.5× pass-rate gains from agent count.
- **Venue**: Preprint.

### 5.3 CliffCompaction — Faithful Autocompaction for Long-Horizon Coding Agents (2609.26779)
- **Title**: CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents
- **Authors**: Trang Nguyen, Eulrang Cho, Bingqing Chen, Tim Dettmers
- **Institution**: University of Washington-aligned (Dettmers; tentative)
- **Date**: Wed 23 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.26779
- **Abstract**: Agents work on problems needing millions of context tokens → cross-session compaction is unavoidable. **CliffCompaction** cuts cost **up to 50%** under a bounded context while maintaining/improving Terminal-Bench and setting new efficiency records on KernelBench: per-rollout savings make test-time scaling cheaper (**+10pp on Terminal-Bench for less than the cost of two full-context runs**); in parallel TTS, it lets **Kimi K2.6 match Opus 4.7** at lower cost. Keeps compaction **faithful by only truncating/dropping original content — never rephrasing or rewriting**; a compaction is never re-compacted (prior compacted output discarded → no context drift). On KernelBench, CUDA speedups reach **2.23× at 200 steps, 3.58× at 400**, beating specialized search and trained agents.
- **Key Innovations**: (1) occlusion-only faithful compaction (no rephrase) as an anti-drift principle; (2) never-compacting-a-compaction rule sustaining million-token continual sessions; (3) cost-efficiency math making parallel test-time scaling viable.
- **Venue**: Preprint.

### 5.4 Trains but Doesn't Learn — A Post-Training Delivery Benchmark for Agents as Forward-Deployed Engineers (2609.25237)
- **Title**: Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers
- **Authors**: Weihang Ding, Junfei Zhan
- **Institution**: industrial/academic (*tentative*)
- **Date**: Wed 23 Sep 2026 (cs.LG); **EMNLP 2026 Industry Track**
- **arXiv**: https://arxiv.org/abs/2609.25237
- **Abstract**: Post-training is becoming a service: a customer gives data + goal and a forward-deployed engineer returns a fine-tuned, evaluated, deployed model under a budget/approval gate/reproducibility constraints. Seats an LLM agent in the FDE seat on a **governed delivery plane** (10 stages, oracle-scored from platform facts). Central silent failure: the **"trains but does not learn" (TBDL)** run — loss falls, all signals green, delivered model no better than base. An operator-run acceptance gate catches every such run pre-payment; a detector calibrated on corrupted runs flags severe corruption mid-run. Evaluated 4 frontier agents (Claude Opus 5, GPT-5.6-luna, Gemini 3.7 Flash, DeepSeek V4-Pro) end-to-end on metered L40S/A100/H200 over 8B–70B bases, plus a human-FDE arm under the same oracle.
- **Key Innovations**: (1) an FDE/post-training-as-a-service evaluation plane with oracle-scored 10-stage pipelines; (2) names + detects the TBDL failure mode (train-but-don't-learn); (3) acceptance-gate economics + frontier-agent/human comparison under identical oracles.
- **Venue**: EMNLP 2026 Industry Track.

---

## 6 Games, World Models & Mechanism Design

### 6.1 CoDeR — Code Plans, Diffusion Renders: Open-Ended Generative World Modeling (2609.26458)
- **Title**: Code Plans, Diffusion Renders: Open-Ended Generative World Modeling
- **Authors**: Zixun Fang, Yawen Shao, Kai Zhu, Jie Xiao, Shihan Chen, Yu Liu, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha
- **Institution**: USTC-aligned (Zha, Fu; tentative)
- **Date**: Wed 23 Sep 2026 (cs.CV)
- **arXiv**: https://arxiv.org/abs/2609.26458
- **Abstract**: Video world models implicitly represent dynamics via visual observations. **CoDeR** instead **explicitly constructs an executable world with code** and uses video generation for visual realization: five complementary roles translate high-level concepts into structured world rules, executable dynamics, and perceptual observations — enabling **long-term memory, open-ended interactions, autonomous world evolution, and persistent multi-agent scenarios** beyond the current observation window. SOTA across multiple evaluation settings; code + weights to be released.
- **Key Innovations**: (1) code-as-executable-world + video-as-render (vs pure latent video dynamics); (2) five-role pipeline (rules→dynamics→perception) enabling authored, persistent world state; (3) open-ended multi-agent persistence beyond the observation horizon.
- **Venue**: Preprint (project page released).

### 6.2 GameDirector — Decoupling Gameplay Logic from Rendering for Player-Configurable Games (2609.25652)
- **Title**: GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models
- **Authors**: Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin
- **Institution**: NTU / BNU-aligned (Wen, Jin; tentative)
- **Date**: Wed 23 Sep 2026 (cs.CV)
- **arXiv**: https://arxiv.org/abs/2609.25652
- **Abstract**: Game world models learn environment dynamics from pixel supervision (perception/memory/state-transition/rendering in one end-to-end stack), but games are governed by **explicit mechanics** (health deduction, skill activation, combat rules, termination) whose precise state transitions generative models can't reliably enforce; game engines enforce them but limit player-driven creation. **GameDirector** — the first agentic framework **decoupling rule-based gameplay logic from visual rendering**: an intelligent director interprets visual observations, updates game state, tactically controls NPCs, and enforces rules, then translates decisions into text prompts for the video world model to render gameplay. Players configure characters/states/rules like a developer, while preserving generative rendering.
- **Key Innovations**: (1) explicit logic (tick-accurate rules) separated from generative rendering — combining engine determinism + world-model flexibility; (2) director-agent as game-state authority (observes → updates → enforces → prompts renderer); (3) player-configurable world models as a design point for the game-AI line.
- **Venue**: Preprint (project page released).

### 6.3 Prophet Inequalities Beyond Utilitarian Social Welfare (2609.25424)
- **Title**: Prophet Inequalities Beyond Utilitarian Social Welfare
- **Authors**: Daniel Halpern, Abhiram Manohara, Alexandros Psomas
- **Institution**: CMU / Purdue-aligned (Halpern, Psomas; tentative)
- **Date**: Wed 23 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.25424
- **Abstract**: Classic i.i.d. prophet inequality maximizes utilitarian welfare; guarantees extend to allocating m indivisible items to sequentially arriving agents. But utilitarian welfare ignores **utility distribution**. Evaluates online rules by **generalized p-mean welfare** (utilitarian at p=1, Nash at p=0, egalitarian as p→−∞). For many items, the fair-division problem collapses exactly to a single-item prophet problem under the p-mean of expected utilities; every online rule is weakly Pareto-dominated by a **quantile-threshold rule**, and the optimal egalitarian rule equalizes agents' expected utilities. For every n, the online optimum ≥ **Γ≈0.7059** × prophet's egalitarian welfare.
- **Key Innovations**: (1) generalized p-mean welfare (Nash→egalitarian spectrum) as the objective for prophet inequalities; (2) quantile-threshold characterization + Pareto dominance for the fair-division regime; (3) an absolute egalitarian-welfare constant (0.7059) with monotone improvement in n.
- **Venue**: Preprint.

---

## Key Trends Across This Window

1. **Recommendation/search returns to the daily layer with production evidence** (25433 Light Heads: weeks→days multi-task experimentation at YouTube scale; 25825 Spotify QSS dual-sample feature dropout with a live +2% metric; 26143 TailSpec-EASE long-tail KG linear rec at 37 s CPU): after a ~9-window drought of pure CTR-ML, this window's rec content is production-systems engineering and long-tail economics rather than model-class papers — consistent with the wiki's observation that end-to-end CTR-ML lives mainly in conference batches.
2. **Serving-oriented ML is the window's spine** (MoE 2/3-expert pruning 25809; disaggregated prefill/decode quantization 26333 with 1.78× TTFT via SSD; HySparse2 KV bridging 26368; CompKV compensation-aware selection 26300; TSS target-side spec-decoding sparsification 26100): architecture and quantization research is now framed by *who pays for what phase*.
3. **Probabilistic time-series foundations mature as post-processing + calibration science** (25788 accuracy-vs-calibration audit incl. xLSTM vs patch-transformer; 25980 dependence reconstruction as a distinct post-processing problem; 26389 streaming interactive TSLM regime + 34k-episode dataset): TSFMs are treated as frozen marginals to be coupled/calibrated/served rather than retrained.
4. **Agentic engineering becomes a benchmarked discipline** (26777 SWE-Serve: repo-scale inference feature implementation on SGLang, 11×31 configs; 26781 Agensh: 1,024-agent orchestrator-free scaling; 26779 CliffCompaction: faithful, never-rephrase compaction with 50% cost cuts; 25237 trains-but-doesn't-learn delivery benchmark): the "agent = deployable engineer" story now has benchmarks, economics, and safety gates.
5. **World modeling converges on code + render** (26458 CoDeR executable-code worlds; 25652 GameDirector decoupled game logic from rendering): the games/world-model cluster consistently separates *dynamics competence* from *visualization competence* — matching the wiki's game-rl/world-model analysis threads.
6. **Games-theory side light but principled** (25424 prophet inequalities under p-mean welfare w/ egalitarian constant 0.7059; runner-up 26265 CFR on Auction Bridge): mechanism design continues to generalize beyond utilitarian objectives, echoing 09-21's Fair Prophets but from the online-allocation side.
7. **Ads/CTR at the daily layer remains ~0** (12th+ consecutive window): no commercial CTR/ad-bidding ML unclaimed; this window's "auction"/"click" matches are Auction Bridge (card game) and the DSA compliance toolkit, keeping conference-digest as the CTR source of record.

## ADS / CTR Coherence Check

0 direct CTR/advertising papers in the Wed-23 window. Closest threads: **Light Heads** (25433, production multi-task ranking experimentation) and **Spotify QSS** (25825, personalized-search reranking with behavioural features + live A/B) are ranking but not click-modeling; TailSpec-EASE (26143) targets long-tail discovery — the causal-distance-from-ads concern many RecSys digests track. The classic end-to-end CTR drought at the daily arXiv layer persists; the `arxiv-paper-check`/`conference-digest` layers remain where CTR content is indexed.

## Cross-Reference Index (Sibling & Runner-Up Coordinates)

- **Same-window coordination**: this report is the 09-23 window's **first claim** (all 449 IDs unclaimed at build time). Sibling jobs running after (09-23 `arxiv-daily`, `arxiv-paper-check`, `game-rl-daily`, `conference-digest`) should treat the 22 featured + 6 runner-up IDs below as claimed and mine the remainder — the strongest unclaimed marquee candidates noted but not featured: **26823/window Qwen omni-agent** (2609.25611 Qwen3.8-Omni + 26760 Grow the Harness), **RecSys-adjacent** (2609.25853 MemoryAthena, 2609.25913 execution-provenance agent memory), **MoE serving** (2609.25655 fine-grained MoE PEFT), **reasoning** (2609.25637, 2609.26566), **quant/LLM** (2609.25916 CASA, 2609.26708 train-where-quantized-goes, 2609.26499).
- Runner-ups this window (grep-verified 0 hits): **2609.25189** GroundedGEO (evidence-gap audit of generative search rankings; unsupported-rich text gains +0.065–0.092 rank on frozen listwise rankers); **2609.25777** ADNet (learning spectral decomposition for multi-step traffic forecasting; best in 20/24 region-horizon-metric settings on TraffiDent); **2609.25916** CASA (cross-layer activation-aware mixed-precision LLM quantization; Hessian-conditioning-rooted sensitivity bound up to 10^13 distortion vs scalar proxies); **2609.26796** Flash-dLLM (I/O-aware fused KV kernel + self-draft-verify decoding for diffusion LLMs); **2609.25802** LEMA (exact-match binary attention; word-RAM equivalence both directions + 834M-param scaling); **2609.26265** A Statistical Analysis of Three Player Auction Bridge (scoring-mechanism redesign; GS-CFR shows shift from separating to partially-pooling bidding).
- Sub-window map for future dedup: Wed-23 window runs **2609.25006–2609.26796**; this report claims 28 IDs across it — remaining unclaimed marquee IDs are the sibling jobs' to take, with the above candidate list as a starter map.

(End of file)