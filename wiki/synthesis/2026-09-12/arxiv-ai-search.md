---
title: arXiv AI Research Paper Search Report
type: synthesis
created: 2026-09-12
updated: 2026-09-12
sources: [arxiv.org]
tags: [arxiv, AI, LLM, CTR, recommendation, advertising, sequential-modeling, game-AI]
---

# arXiv AI Research Paper Search Report

Generated: 2026-09-12 | Scope: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

**Methodology**: The arXiv Atom API was intermittently rate-limited (HTTP 429/timeouts), so paper data was pulled from `arxiv.org/list/{cs.AI,cs.CL,cs.IR,cs.LG,cs.GT,cs.MA,cs.CY,cs.NE}/recent` listings plus individual `/abs/` pages (fetch artifacts cached in the pre-approved temp workspace and discarded after this run). This report covers the **Fri 11 Sep 2026 mailing** (papers announced 9–10 Sep 2026). ~300 titles screened.

**Dedup notice**: This report is **complementary** to the same-week sibling digests. Papers already featured there are not re-featured here with full entries — they are listed in the [cross-reference index](#9-cross-reference-index-featured-in-sibling-digests) at the bottom:
- Excluded for 09-11 sibling digests ([[arxiv-daily]] / [[arxiv-ai-search]] 09-11): UniRec 2609.11052, FedHUR 2609.11632, Agentic Share-of-Search 2609.11190, VikingRAG 2609.11390, GPU-CFR 2609.11923, Thinking with Looped Flows 2609.11801, The Last AI Built by Humans 2609.11873, PTQ 2609.11716, LILA 2609.11163, MoE data-scarcity 2609.11917.
- Excluded for 09-11 [[arxiv-paper-check]]: unified per-token gating 2609.11768, COBRA-Skills 2609.11682, REVA 2609.11209, GLIE 2609.11808, distribution-shape QPP 2609.11646, regularization landscape 2609.11876.
- Excluded for 09-12 [[arxiv-daily]] (24 papers) and 09-12 [[arxiv-paper-check]] (16 papers): Auto-RecSys 2609.10922, housing-rec audit 2609.10856, T1 terminal RL 2609.11042, FlexComp 2609.11192, Magenta 2609.11319, TASCO 2609.11393, TimelyRAG 2609.11572, RDDMPI 2609.11648, Kashin-DCT 2609.11687, ORCH 2609.11737, RAG-Safety-Bench 2609.11758, internal-knowledge routing 2609.11859, TNBR/ABRA 2609.11863/2609.11889, Negative Self-Distillation 2609.11699, Mr.LHDR 2609.11318.

**Net contribution**: 13 papers featured in full (unique to the wiki); 45 total screened in this run minus 32 deduped against siblings.

---

## 1. Large Language Models — Post-Training, Reasoning & Interpretability

### 1.1 A Fragility Spectrum for Recursive Language-Model Training
- **Authors**: Yangze Liu, Zhongyi Han
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11149
- **Abstract**: Runs one recursive contamination protocol across 13 public checkpoints over five generations; unique-4-gram survival spans 0.187–0.940 (≈5× spread) — collapse-fragility is a property of the checkpoint, not just the data recipe. Composition changes keep ordering correlation 0.91–0.97; parameter scale is not monotonic in fragility and no static indicator predicts it. Cheap probe: 2–3 self-iterations forecast ecosystem fragility. Tightening top-p nearly stops collapse; data-side filtering only slows it.
- **Key Innovations**: First systematic fragility *spectrum* across checkpoints; model-intrinsic collapse-susceptibility framing; actionable cheap fragility probe.
- **Venue**: Preprint

### 1.2 Distance Generalization in Transformers: Why Bother with Positional Encoding?
- **Authors**: Daniel Henrik Nevermann, Claudius Gros
- **Institution**: Goethe University Frankfurt (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11913
- **Abstract**: Probes inter-token distance generalization (unseen delays, fixed context length) on two synthetic delay-copy tasks where tokens are copied fully or selectively. Asks (A) whether RoPE/ALiBi improve distance resolution over NoPE, (B) how training-set distance diversity affects performance, and (C) when distance transfer is positive vs negative. Finds that improving the understanding of the underlying mechanisms matters more than any single encoding scheme: encoding choice and data diversity interact non-trivially.
- **Key Innovations**: Clean controllable task suite isolating distance (not length) generalization; encoding×diversity×transfer interaction study.
- **Venue**: Preprint

### 1.3 ActMap: Single-Pass Uncertainty Quantification from Generation-Time Activation Maps
- **Authors**: Jacopo Dardini, Roberta Calegari
- **Institution**: University of Bologna
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11498
- **Abstract**: Compresses the full generation-time hidden-state trajectory (every layer × token) into a fixed 12×32×128 tensor of temporal-statistic channels captured with no measurable overhead (96 KiB). A compact ViT classifier reads an estimated correctness probability in <1 ms per generation, supporting abstention/routing/selective verification from a single pass. Outperforms sampling-, token-probability-, attention-, and embedding-based baselines on QA/math/summarization factuality, and matches ACT-ViT (dense activations 67× larger) at similar AUROC with lower calibration error.
- **Key Innovations**: Single-pass white-box UQ with no sampling; fixed shape across model depths; occlusion analysis localizes signal to mid-depth map regions.
- **Venue**: Preprint (13 pp., U. Bologna)

---

## 2. LLM Serving, Compression & Efficiency

### 2.1 LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation
- **Authors**: Dongfang Zhao
- **Institution**: University of Utah (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11739
- **Abstract**: Shows the *parameterization* of post-training updates, not just the alignment loss, changes response length: low-rank subspaces alter sequence length without touching the preference objective. LOCUS selects a task-aware low-rank adaptation subspace to minimize output-token cost under a utility constraint, keeping the frozen-backbone preference objective. Reduces continuation length up to 39.8% (Pythia-2.8B) / 14.9–17.6% (Qwen2.5-3B) while updating only 0.24–0.28% of parameters, with no material change in the preference diagnostic.
- **Key Innovations**: Verbosity as a subspace property; token-budget-aware subspace selection; near-zero-parameter post-training length control.
- **Venue**: Preprint

---

## 3. CTR Prediction & Advertising

### 3.1 SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control
- **Authors**: Suwan Wu, Yumeng Lin, Pengcheng Yuan, Xiaolong Jiang
- **Institution**: Industry (e-commerce platform, tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11752
- **Abstract**: Internalizes a platform's risk-control policies into weights via continued pretraining (CPT) on policy-derived synthetic examples (EntiGraph, MAGA rewriting, account-level CoT) so the model applies rules verdict-only at second-level latency and high precision. SIRF-8B-SFT reaches 71.3% Black Recall@P95 (+15.1 pp over a policy-injected SFT-only twin) using ~70M CPT tokens, matching/exceeding far larger systems. Deployed as a tree-model adjudication layer (recovers 20% more mis-penalized samples) and transfers to cold domains with ~70% relative mis-penalization reduction.
- **Key Innovations**: Policy-grounding *into weights* rather than prompt-injection; spec-synthesized training without human annotation; high-precision ultra-low-latency verdict-only deployment.
- **Venue**: EMNLP 2026 Industry Track

> 📌 **Advertising note**: No fresh auction/budget-bid papers in this Friday window beyond the 09-11 [[arxiv-daily]] items (meCPM, UniCon) and the SIRF content-risk model above. Generative-ad work (GR4AD, GOAL, UniVA) from late August remains the advertising SOTA; this week's momentum is on recommender *foundation/system* architecture (UniRec, Auto-RecSys) rather than new interaction models.

---

## 4. Sequential Modeling & Time Series

### 4.1 When Does Text Inform? Benchmarking Information-Theoretic Metrics for Multimodal Time-Series Forecasting
- **Authors**: Emma Andrews, Gianmarco Mengaldo
- **Institution**: NTU Singapore (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11282
- **Abstract**: Builds the first ground-truth benchmark for "does this text annotation add predictive value to TS forecasting?", with synthesized annotations that are semantically correct / incorrect / irrelevant. Evaluates six MI estimators (KSG, MINE, InfoNCE, CCA, PID, V-information): all identify correct annotations as most informative and can audit mixed corpora, choosing annotations that yield best downstream forecasts without training models. Validate on seven real datasets and give practical implementation rules.
- **Key Innovations**: Ground-truth multimodal-TS annotation-value benchmark; estimator-agnostic auditing method; no-training-needed annotation selection.
- **Venue**: Preprint

### 4.2 SolCloudLLM: Bidirectional Multimodal Fusion of Sky Images and Time-Series for Solar Forecasting with LLMs
- **Authors**: Ken Chen, Maneesha Perera, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge
- **Institution**: University of Melbourne (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11135
- **Abstract**: Aligns sky-image patches with time-series patches and fuses them bidirectionally into the LLM embedding space for short-term PV/GHI forecasting. Outperforms best baselines on SIRTA and SKIPP'D in MSE at all horizons (up to −25.4% relative), with gains concentrated in cloudy conditions and in few-shot settings where non-learning physical models beat degraded DL baselines.
- **Key Innovations**: First LLM-forecasting framework fusing imagery + TS bidirectionally; cloud-ramp signal utilization; strong few-shot/site-scarce performance.
- **Venue**: Preprint

### 4.3 CryptoL: Scale Dominance and Physics-Constraint Mitigation in Financial Multivariate Time-Series Forecasting
- **Authors**: Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli, Maryam Amirshahkarami, Mohammad Ebrahim Mahdavi, Hossein Karshenas
- **Institution**: Iran academia (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11206
- **Abstract**: Multivariate crypto forecasting faces extreme cross-asset scale heterogeneity and structural OHLC constraints. CryptoL: (1) evaluates error in context-normalized RevIN coordinates to stop inverse-normalization weighting large-scale assets; (2) keeps channel-dependent affine normalization to preserve candle-order relations; (3) adds scale-adaptive numerical stabilization and a soft feasibility loss penalizing violations of OHLC inequalities. Ablations show better accuracy, training stability, and finite validity of OHLC predictions.
- **Key Innovations**: Scale-bias removal via context-normalized loss; structure-preserving normalization; physics (OHLC inequality) constraints as soft loss.
- **Venue**: Preprint

### 4.4 DF-LLM: A Dynamic Fusion Large Language Model for Traffic Flow Prediction
- **Authors**: Xue Qiu, Jianli Xiao
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11314
- **Abstract**: LLM-based traffic forecasting adding a spatiotemporal embedding module, a graph-convolution spatiotemporal fusion module feeding spatial topology + dynamic dependencies into the LLM backbone, differentiated parameter adaptation, a context-aggregation attention module for global dependencies, and residual connections to fight gradient vanishing. Reports better metrics on all four datasets vs baselines.
- **Key Innovations**: Graph-fused LLM for spatiotemporal sequences; context-aggregation attention; residual-connected LLM backbone.
- **Venue**: WISA 2026

---

## 5. Game AI, Game Theory & RL

### 5.1 Existence of the Core in Approval-Based Committee Elections
- **Authors**: Patrick Becker, Matthias Greger, Dominik Peters
- **Institution**: TU Wien / CNRS-affiliated (tentative, Peters)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11912
- **Abstract**: Settles the main open question in approval-based multi-winner elections: a committee in the **core** always exists. The proof introduces a voting rule optimizing an entropy-like objective over committees and payment systems; all local optima lie in the core, and a core committee is found in polynomial time. (Proof obtained with GPT-6 Astra verification assistance.)
- **Key Innovations**: Resolution of a long-open existence question; constructive entropy-optimization voting rule; poly-time core finding.
- **Venue**: Preprint (20 pp.)

### 5.2 Tapes Together Strong: The Co-evolution of Computation and Cooperation
- **Authors**: Kunal Jha, Francesco Cicala, Blaise Agüera y Arcas, Blake Aaron Richards, Natasha Jaques, Max Kleiman-Weiner, Eyvind Niklasson
- **Institution**: Google DeepMind / Mila-affiliated (tentative)
- **Date**: 2026-09-09
- **arXiv**: https://arxiv.org/abs/2609.10817
- **Abstract**: Introduces Autopoietic Game Theory: social interaction, replication, and computational cost are endogenous and co-evolve in a substrate of randomly initialized Z80 machine-code programs. Embedding a social dilemma into the physics of computation favors self-replicating cooperative strategies; under scarce resources, defection becomes self-limiting (stealing burns shared energy and slows execution). Evolved programs suppress stealing across environments; spatial assortment boosts structural complexity and task performance; the framework absorbs exogenous pressures (math tasks as sequential social dilemmas) when rewards tie to computation budget.
- **Key Innovations**: Universally-co-evolving autopoiesis + game theory; defection-self-limiting economics; linking computation capacity to energy as a cooperation scaffold.
- **Venue**: Preprint

---

## 6. Agents & Agentic ML

### 6.1 Artificial Id: Drive and Persistent Alignment in Agentic AI
- **Authors**: Yakov Pyotr Shkolnikov
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11911
- **Abstract**: Proposes an "artificial id" — an adaptive internal drive determining whether agent behavior should continue, stop, or change across task boundaries — as the missing control primitive for long-lived agentic systems. In a minimal Petri-dish experiment a controller with no task-specific objective develops useful control through differential persistence; the same mechanism can select unintended physical strategies and replace learned sensor mappings when their meaning changes. Argues scalability requires a persistent alignment boundary over trusted observations, consequence channels, state, authority, identity, provenance, and hard constraints.
- **Key Innovations**: Persistence-based drive as emergent goal-selection mechanism; agentic alignment reframed as property of the continuing system, not single trajectories.
- **Venue**: Preprint

---

## 7. ML Foundations & Evaluation

### 7.1 CausalArena: Benchmarking Causal Discovery in the Foundation Model Era
- **Authors**: Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang, Han-Jia Ye
- **Institution**: Nanjing University (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11897
- **Abstract**: Unified, evolvable causal-discovery benchmark with three synthetic regimes (controlled SCM breadth; human-auditable semantic operational SCMs; formula-grounded explicit-mechanism SCMs) plus real-world data for external validity. Evaluates classical, neural, and foundation-model causal discovery (CDFMs). Substantial ranking shifts across SCM families/protocols — strong performance in one regime does not transfer; calls out pretraining–evaluation overlap as a central confound for CDFM claims.
- **Key Innovations**: First benchmark isolating pretraining-overlap confound for causal-discovery foundation models; multi-family SCM protocol.
- **Venue**: Preprint (47 pp.)

---

## 8. Key Trends (unique coverage)

1. **Recursive-training collapse is a checkpoint-intrinsic property**: the Fragility Spectrum (5× spread across 13 checkpoints, no static predictor) and the earlier model-collapse literature suggest collapse-susceptibility should be tracked like a safety metric — with top-p tightening as the strongest mitigation lever [2609.11149].

2. **Efficiency shifts from post-hoc fixes to parameterization choices**: LOCUS shows verbosity is a property of the *low-rank subspace* used in alignment — output-token cost can be engineered at 0.24–0.28% parameter update without touching the preference objective [2609.11739].

3. **Policy knowledge is being compiled *into weights***: SIRF shows continued pretraining on policy-derived synthetic examples lets a risk model apply rules verdict-only at second-level latency (71.3% Black Recall@P95, +15.1 pp) — a template for spec-internalized guardrails vs prompt injection [2609.11752].

4. **Content risk control joins CTR/ads stacks**: SIRF positions content-risk scoring as an industrial ranking-adjacent layer (tree-model adjudication recovering 20% more mis-penalized samples), extending the CTR/ads surface beyond click prediction [2609.11752].

5. **Multimodal time-series keeps finding signal in text/imagery**: "does text inform?" gets a ground-truth estimator benchmark [2609.11282]; SolCloudLLM fuses sky imagery + TS bidirectionally into LLM embedding space (−25.4% MSE in cloudy regimes) [2609.11135]; CryptoL and DF-LLM push structure-(OHLC/road network)-aware forecasting [2609.11206, 2609.11314].

6. **Game theory/econ theory: hard existence results**: approval-committee core existence settled after years via an entropy-optimizing voting rule (with GPT-6 Astra verification assistance) [2609.11912]; Autopoietic Game Theory embeds social dilemmas into the physics of computation so defection becomes self-limiting [2609.10817].

7. **Agents: persistence as the control primitive**: "Artificial Id" re-frames alignment as a property of the *continuing* system (persistent drive across task boundaries), not single trajectories — complements this week's verifier-driven terminal RL (T1) and organization-as-structure (ORCH) work [2609.11911].

8. **Evaluation hygiene for the foundation-model era**: CausalArena isolates the pretraining-overlap confound for causal-discovery foundation models — a caution that strong CDFM results may reflect memorized benchmark structure [2609.11897].

---

## 9. Cross-Reference Index (featured in sibling digests)

Papers screened in this run but already featured in sibling digests — full entries live there:

| arXiv ID | Paper | Featured in |
|---|---|---|
| 2609.11042 | T1: Terminal Agent RL (long-horizon) | 09-12 [[arxiv-daily]] §3.1 |
| 2609.11319 | Magenta: Lean-verified math reasoning | 09-12 [[arxiv-daily]] §3.2, 09-12 [[arxiv-paper-check]] ① |
| 2609.11393 | TASCO: stability-aware test-time adaptation | 09-12 [[arxiv-daily]] §3.3, 09-12 [[arxiv-paper-check]] ④ |
| 2609.11699 | Negative Self-Distillation (reasoning by avoiding flaws) | 09-12 [[arxiv-paper-check]] ④ |
| 2609.11768 | Unified per-token gating for on-policy distillation | 09-11 [[arxiv-paper-check]] |
| 2609.11192 | FlexComp: any-ratio context compression | 09-12 [[arxiv-daily]] §5.1 |
| 2609.11687 | Kashin-DCT structured quantization | 09-12 [[arxiv-daily]] §5.2 |
| 2609.10922 | Auto-RecSys: autonomous recsys research agents | 09-12 [[arxiv-daily]] §1.1 |
| 2609.10856 | Housing-rec "compliance without optimization" | 09-12 [[arxiv-daily]] §1.4 |
| 2609.11876 | Regularization landscape for linear recommenders | 09-11 [[arxiv-paper-check]] |
| 2609.11646 | Distribution-shape QPP for RAG sufficiency | 09-11 [[arxiv-paper-check]] |
| 2609.11808 | GLIE: generative late-interaction VDR | 09-11 [[arxiv-paper-check]] |
| 2609.11572 | TimelyRAG + TimelyQABench | 09-12 [[arxiv-daily]] §4.1 |
| 2609.11758 | RAG-Safety-Bench | 09-12 [[arxiv-daily]] §4.2 |
| 2609.11209 | REVA: evidence-view aggregation RAG serving | 09-11 [[arxiv-paper-check]] |
| 2609.11648 | RDDMPI: residual diffusion TS imputation | 09-12 [[arxiv-daily]] §2.1 |
| 2609.11863 | TNBR: truncated noisy best-response | 09-12 [[arxiv-daily]] §6.1, 09-12 [[game-rl-daily]] |
| 2609.11889 | ABRA: no low-quality Nash equilibria | 09-12 [[arxiv-daily]] §6.2, 09-12 [[game-rl-daily]] |
| 2609.11737 | ORCH: organizational collective intelligence | 09-12 [[arxiv-daily]] §7.1 |
| 2609.11682 | COBRA-Skills: bandit-guided skill evolution | 09-11 [[arxiv-paper-check]] |
| 2609.11859 | LLM internal-knowledge routing study | 09-12 [[arxiv-daily]] §3.5 |
| 2609.11318 | Mr.LHDR: multimodal long-horizon deep-research benchmark | 09-12 [[arxiv-paper-check]] ①, 09-12 [[game-rl-daily]] |

> Papers 2609.11052, 2609.11632, 2609.11190, 2609.11390, 2609.11923, 2609.11801, 2609.11873, 2609.11716, 2609.11163, 2609.11917 additionally were featured in the 09-11 [[arxiv-daily]]/[[arxiv-ai-search]] coverage and are not re-listed here.