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

**Methodology**: The arXiv Atom API was intermittently rate-limited (HTTP 429/timeouts), so paper data was pulled from `arxiv.org/list/{cs.AI,cs.CL,cs.IR,cs.LG,cs.GT,cs.MA,cs.CY,cs.NE}/recent` listings plus individual `/abs/` pages (fetch artifacts cached in the pre-approved temp workspace and discarded after this run). This report covers the **Fri 11 Sep 2026 mailing** (papers announced 9–10 Sep 2026) and is **complementary** to the 09-11 sibling digests: papers featured there (UniRec 2609.11052, FedHUR 2609.11632, Agentic Share-of-Search 2609.11190, VikingRAG 2609.11390, GPU-CFR 2609.11923, Thinking with Looped Flows 2609.11801, The Last AI Built by Humans 2609.11873, PTQ 2609.11716, LILA 2609.11163, MoE data-scarcity 2609.11917) are not re-featured here. ~300 titles screened.

---

## 1. Large Language Models — Post-Training, Reasoning & Interpretability

### 1.1 A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing with Multi-Channel and Bias Coefficients
- **Authors**: Suwan Wu, Yumeng Lin, Pengcheng Yuan, Xiaolong Jiang
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11768
- **Abstract**: Proposes a four-coefficient per-token gating parameterization `λ_t = σ(a·h_t + b·u(x) + c + d·gap_t)` that unifies the fixed single-signal gates of EOPD (entropy) and ToDi (KLD gap) as one-dimensional restrictions, adding multi-channel composition and an explicit bias. On TweetEval emotion/hate with a Qwen3-32B teacher → Qwen3-4B student, the full family beats matched single-channel 1D restrictions in 33/36 cells and dynamic gating beats effective-KL-matched static baselines in 19/26 cells; three-seed replications are directionally consistent but individually not significant at n=3 — presented as a shared coordinate system rather than a champion recipe.
- **Key Innovations**: First direct comparison of EOPD vs ToDi gating signals under one parameterization; isolates dynamic gating contribution from KL matching; honest small-n statistics.
- **Venue**: EMNLP 2026 Findings

### 1.2 Negative Self-Distillation: Learning to Reason by Avoiding Flaws
- **Authors**: Rongcan Pei, Zhepei Wei, Shuyao Xu, Xinyu Zhu, Wei-Lin Chen, Yu Meng
- **Institution**: — (academic)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11699
- **Abstract**: Argues on-policy self-distillation (OPSD) degrades complex reasoning by forcing imitation of artificially confident privileged-conditioned traces, suppressing honest uncertainty and exploration. Proposes NSD: the model generates its own "careless reasoner" negative condition and the student diverges from that self-generated flawed trace, with a dynamic gating mechanism that isolates reasoning-critical tokens from basic linguistic tokens so unlearning gradients do not damage the language prior. Outperforms OPSD and label-free self-bootstrapping RL baselines.
- **Key Innovations**: Divergence-from-flaws as a self-improvement signal (vs. imitation of ground truth); token-gated unlearning objective preserving linguistic priors.
- **Venue**: Preprint (23 pp.)

### 1.3 Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification
- **Authors**: Joshua Ong Jun Leang, Haonan Li, Zheng Zhao, Xinyi Shang, Wenda Li, Zhengzhong Liu, Erix Xing, Shay Cohen, Eleonora Giunchiglia
- **Institution**: MBZUAI / Imperial-affiliated (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11319
- **Abstract**: Training-free agentic pipeline that takes a natural-language math problem, produces an answer, formalizes it as a Lean 4 statement, and constructs a machine-checked proof. A statement judge verifies the formalization preserves the original problem; an error-attribution judge routes failures to either mathematical re-derivation or local Lean repair. Reports 100% accuracy on AIME 2025/2026 and HMMT Feb 2026, and solves all six IMO 2026 problems when paired with the open-weight K2-Horizon-7B reasoner. Statement adjudication is essential to prevent false certificates; feedback-guided correction beats independent resampling on hard problems.
- **Key Innovations**: Closed informal→formal reasoning loop with routing between re-derivation and Lean repair; judge-based false-certificate prevention; state-of-the-art olympiad results via verification-backed decoding.
- **Venue**: Preprint

### 1.4 Distance Generalization in Transformers: Why Bother with Positional Encoding?
- **Authors**: Daniel Henrik Nevermann, Claudius Gros
- **Institution**: Goethe University Frankfurt (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11913
- **Abstract**: Probes inter-token distance generalization (unseen delays, fixed context length) on two synthetic delay-copy tasks where tokens are copied fully or selectively. Asks (A) whether RoPE/ALiBi improve distance resolution over NoPE, (B) how training-set distance diversity affects performance, and (C) when distance transfer is positive vs negative. Finds that improving the understanding of the underlying mechanisms matters more than any single encoding scheme: encoding choice and data diversity interact non-trivially.
- **Key Innovations**: Clean controllable task suite isolating distance (not length) generalization; encoding×diversity×transfer interaction study.
- **Venue**: Preprint

### 1.5 From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge
- **Authors**: Wenkang Wei, Yuan Fang, Renhe Jiang, Hong Cheng, Xingtong Yu
- **Institution**: CUHK / NUS-affiliated (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11859
- **Abstract**: Layerwise-intervention study of how query-routing information and target knowledge evolve when an LLM answers country–continent questions. Distinguishes early "readability", natural strength, causal steering, and later content dependence. A pair-conditioned request direction grows before interventions begin altering later fitted knowledge (causal window opens while answer content is still forming); trajectories differ across Qwen/Llama/Gemma — Gemma shows partial mid-layer routing-content overlap, Llama shows no sustained routing-effect window. Global request dependence fades layer-by-layer while fitted-content dependence persists.
- **Key Innovations**: Fine-grained causal dissection of question-answering circuit; cross-model heterogeneity; pairs "request direction" vs "content dependence" as separable object.
- **Venue**: Preprint (53 pp.)

### 1.6 A Fragility Spectrum for Recursive Language-Model Training
- **Authors**: Yangze Liu, Zhongyi Han
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11149
- **Abstract**: Runs one recursive contamination protocol across 13 public checkpoints over five generations; unique-4-gram survival spans 0.187–0.940 (≈5× spread) — collapse-fragility is a property of the checkpoint, not just the data recipe. Composition changes keep ordering correlation 0.91–0.97; parameter scale is not monotonic in fragility and no static indicator predicts it. Cheap probe: 2–3 self-iterations forecast ecosystem fragility. Tightening top-p nearly stops collapse; data-side filtering only slows it.
- **Key Innovations**: First systematic fragility *spectrum* across checkpoints; model-intrinsic collapse-susceptibility framing; actionable cheap fragility probe.
- **Venue**: Preprint

### 1.7 Beyond Confidence: Stability-Aware Test-Time Adaptation for LLM Reasoning
- **Authors**: Bincheng Gu, Min Gao, Zongwei Wang, Yibing Bai, Yulan He, Junliang Yu
- **Institution**: KAIST / UESTC-affiliated (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11393
- **Abstract**: Observes that high-confidence reasoning is trustworthy only when confidence remains stable under local perturbations. Proposes TASCO: test-time adaptation that optimizes a lightweight task-level prefix with either Random Perturbation (distributional stability across nearby trajectories) or Sharpness-Aware Perturbation (worst-case sensitivity), keeping the LLM frozen. Improves reasoning accuracy and token efficiency across LLMs and benchmarks without prematurely concentrating the predictive distribution.
- **Key Innovations**: Stability (not raw confidence) as the TTA signal; SAM-style worst-case perturbation for prefix tuning; cheap frozen-model adaptation.
- **Venue**: Preprint

### 1.8 ActMap: Single-Pass Uncertainty Quantification from Generation-Time Activation Maps
- **Authors**: Jacopo Dardini, Roberta Calegari
- **Institution**: University of Bologna
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11498
- **Abstract**: Compresses the full generation-time hidden-state trajectory (every layer × token) into a fixed 12×32×128 tensor of temporal-statistic channels captured with no measurable overhead (96 KiB). A compact ViT classifier reads an estimated correctness probability in <1 ms per generation, supporting abstention/routing/selective verification from a single pass. Outperforms sampling-, token-probability-, attention-, and embedding-based baselines on QA/math/summarization factuality, and matches ACT-ViT (dense activations 67× larger) at similar AUROC with lower calibration error.
- **Key Innovations**: Single-pass white-box UQ with no sampling; fixed shape across model depths; occlusion analysis localizes signal to mid-depth map regions.
- **Venue**: Preprint (13 pp., U. Bologna)

---

## 2. LLM Serving, Compression & Efficiency

### 2.1 FlexComp: One Model for Every Ratio in Context Compression
- **Authors**: Kaiyan Zhao, Zhongtao Miao, Akiko Aizawa, Yoshimasa Tsuruoka
- **Institution**: University of Tokyo (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11192
- **Abstract**: Decouples the compression ratio of soft context compressors (ICAE, 500xCompressor, SAC) from training and deployment: Matryoshka-style training samples memory budget K per instance so one model serves any ratio, and K is chosen per input via (1) confidence-based cascade routing or (2) a lightweight learned K-predictor. A single FlexComp model matches fixed-ratio specialists; cascade routing keeps >98% of the mildest ratio's accuracy at up to 266× compression; the K-predictor reaches 158–236× within 0.7 F1. At serving scale it cuts context KV cache ~50% and lifts decoding throughput 47%.
- **Key Innovations**: Any-ratio compression in a single model; input-adaptive budget selection; serving-level KV/throughput wins.
- **Venue**: Preprint (work in progress)

### 2.2 LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation
- **Authors**: Dongfang Zhao
- **Institution**: University of Utah (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11739
- **Abstract**: Shows the *parameterization* of post-training updates, not just the alignment loss, changes response length: low-rank subspaces alter sequence length without touching the preference objective. LOCUS selects a task-aware low-rank adaptation subspace to minimize output-token cost under a utility constraint, keeping the frozen-backbone preference objective. Reduces continuation length up to 39.8% (Pythia-2.8B) / 14.9–17.6% (Qwen2.5-3B) while updating only 0.24–0.28% of parameters, with no material change in the preference diagnostic.
- **Key Innovations**: Verbosity as a subspace property; token-budget-aware subspace selection; near-zero-parameter post-training length control.
- **Venue**: Preprint

### 2.3 Structured Transforms for Low-Overhead Quantization of Language Models
- **Authors**: Daria Cherniuk, Alexander Rudikov, Boris Kashin, Ivan Oseledets
- **Institution**: Skoltech / AIRI-affiliated (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11687
- **Abstract**: Improves Kashin-decomposition weight quantization by replacing the dense random orthogonal matrix with a sign-randomized DCT — cutting per-iteration cost from O(N²) to O(N log N) — with alternating greedy updates that guarantee the four-peak distribution needed for stable 2-bit clustering and closed-form center initialization. Composed with OPTQ error compensation + QuIP incoherence, it is competitive with OPTQ/QuIP/QuIP-RG at 4-bit per channel on OPT/Llama-2/Pythia, and stays numerically stable where QuIP variants diverge to four-digit perplexity or NaN in LDL back-substitution. Decomposes each weight into two 2-bit factor codes suited to native-2-bit hardware.
- **Key Innovations**: Structured-orthogonal Kashin quantization; closed-form 2-bit cluster initialization; robust stress-case stability.
- **Venue**: Preprint

---

## 3. Recommendation Systems & Retrieval

### 3.1 On the Regularization Landscape for the Linear Recommendation Models
- **Authors**: Dong Li, Zhenming Liu, Ruoming Jin, Hao Zhou, Zhi Liu, Jing Gao, Bin Ren
- **Institution**: Lenovo AI Lab / Purdue-affiliated (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11876
- **Abstract**: Unifies the surprising performance parity of diverse DL-inspired linear recommenders (dropout-, autoencoder-, etc.): all effectively add either a nuclear-norm or a Frobenius-norm regularizer. Nuclear-norm solutions are low-rank and closed-form but rigid (limited predictive power); Frobenius solutions are more expressive but full-rank or require hard-to-tune ADMM. Derives two new low-rank, closed-form solutions from generalized Frobenius regularization that combine both worlds.
- **Key Innovations**: Unifying theory explaining linear-leaderboard parity; closed-form low-rank + expressive solutions avoiding ADMM.
- **Venue**: Preprint

### 3.2 Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System Experiments
- **Authors**: Ming Li, Dai Li, Xuying Ning, Bo Sun, Rui Li, Yi Zhang, Silvia Gong, Xuan Cao, Rui Li, Cornelia Carapcea, Qunshu Zhang, Zhigang Wang, Yinglong Xia, Andy Wang
- **Institution**: Industry (large tech co., tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.10922
- **Abstract**: Scalable auto-research system for long-horizon recommender-system experimentation: (1) distributed asynchronous execution across servers to parallelize multi-day-training feedback loops; (2) centralized cross-server memory for persistent, recoverable runs; (3) cognitive-procedural separation — NL skill files guide LLM reasoning while deterministic scripts enforce operational correctness. A dual-loop architecture evolves "Execution playbooks" (failed attempts recorded, successful pipelines crystallized) and "Idea loops" (outcomes inform new ideation). Reduces per-experiment human time and improves reliability as playbooks mature.
- **Key Innovations**: Parallel long-feedback-loop agentic experimentation; cross-server durable memory; procedural guardrails over LLM planning for industrial recommender ops.
- **Venue**: Preprint

### 3.3 Generative Late-Interaction Embeddings for Visual Document Retrieval (GLIE)
- **Authors**: Mohamed Eltahir, Talal Aloushan, Rose Khairoalsendi, Jana Shata, Mohammed Alhassan, Leen Alrehaili, Tanveer Hussain, Naeemullah Khan
- **Institution**: Queen's Belfast / Gulf universities (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11808
- **Abstract**: Late-interaction visual retrieval pays for accuracy in storage (~1000 vectors/page). Finds page vectors lie on the unit sphere near a 5–6-dim manifold. Two insights: (1) k-means centroids sit inside the sphere and systematically underestimate MaxSim — surface-normalizing them is a free +0.093 nDCG@5 correction; (2) the whole vector set can be *regenerated* from a few learned basis vectors. GLIE keeps k≪N vectors per page for search and a decoder regenerates all N vectors to re-score top candidates. At 4 vectors/page on ViDoRe v1 it retains ~80% of uncompressed nDCG@5 (vs 70% best prior post-hoc), using a 415K-param network fit in <3 GPU-minutes.
- **Key Innovations**: On-demand *generative* reconstruction of embeddings instead of lossy sampling; manifold-geometry-grounded compression; decoder as the design surface.
- **Venue**: Preprint

### 3.4 Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency
- **Authors**: Matyáš Veselý, Michal Průšek, Jiří Franc
- **Institution**: Czech Technical University in Prague (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11646
- **Abstract**: For retrieval-sufficiency prediction in RAG, 24 non-lexical score-distribution features (GeneralQPP) reach AUROC 0.856 in 2 ms/query on ViDoRe (14,514 queries), beating the classic-QPP pool (0.835) and a local Qwen3.5 LLM judge (0.649) — ~3000× faster/cheaper. Hybridizing with the LLM judge matches/edges it out on a sensitive Czech nuclear-regulator deployment (no third-party APIs, AUROC 0.911, adversarial-detection 0.954). Leave-one-domain-out drops S1 to 0.706; a 13-feature LODO subset recovers 0.719.
- **Key Innovations**: Distribution-shape (not lexical) QPP as a cheap, API-free retrieval-confidence signal; LLM-judge demotion to a single hybrid feature; robust cross-domain subset.
- **Venue**: TSD 2026

### 3.5 TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical QA in Overlapping-Evolving Documents + TimelyQABench
- **Authors**: Youngeun Nam, Joeun Kim, Hwanjun Song, Susik Yoon, Jae-Gil Lee, Byung Suk Lee
- **Institution**: KAIST (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11572
- **Abstract**: Existing time-aware retrieval handles only *disjoint*-evolving documents (independent snapshots); laws/regulations evolve by *overlapping* amendment (override some clauses, keep most). TimelyRAG is a retriever-agnostic framework folding temporal distance into ranking to align queries with version-appropriate documents; introduces TimelyQABench, the first benchmark for overlapping-evolving regulation QA. Consistent gains up to +28.6% nDCG@10.
- **Key Innovations**: First-overlapping-evolving-documents retrieval benchmark; retriever-agnostic temporal ranking; regulation-heavy QA testbed.
- **Venue**: Preprint

### 3.6 RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety
- **Authors**: Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser
- **Institution**: National Research Council Canada (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11758
- **Abstract**: Controls for retriever quality and isolates four conditions (non-RAG / oracle-answer docs / related-but-answerless docs / random safe docs) to measure RAG's safety side effects across 5 open LLMs. Finds an inverse relationship between benign and unsafe capability, that baseline safety guardrails do NOT transfer to RAG settings, and that even benign documents can trigger unsafe generation.
- **Key Innovations**: Confound-free RAG-safety benchmark separating retrieval-answer effects; evidence that guardrail safety ≠ RAG downstream safety.
- **Venue**: EMNLP 2026 (Main)

### 3.7 REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving
- **Authors**: Tuan Nguyen, Qiran Hu, Banruo Liu, Khoa D. Doan, Kok-Seng Wong, Fan Lai
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11209
- **Abstract**: (Featured in cs.LG/cs.IR Friday mailing) Precomputes reusable "evidence views" of retrieved passages so the served context avoids redundant re-embedding/re-rendering of the same evidence across queries — a serving-layer answer to context efficiency in RAG pipelines.
- **Key Innovations**: Reusable-evidence caching for RAG serving context efficiency.
- **Venue**: ICDM 2026 (accepted)

---

## 4. CTR Prediction & Advertising

### 4.1 SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk Control
- **Authors**: Suwan Wu, Yumeng Lin, Pengcheng Yuan, Xiaolong Jiang
- **Institution**: Industry (e-commerce platform, tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11752
- **Abstract**: Internalizes a platform's risk-control policies into weights via continued pretraining (CPT) on policy-derived synthetic examples (EntiGraph, MAGA rewriting, account-level CoT) so the model applies rules verdict-only at second-level latency and high precision. SIRF-8B-SFT reaches 71.3% Black Recall@P95 (+15.1 pp over a policy-injected SFT-only twin) using ~70M CPT tokens, matching/exceeding far larger systems. Deployed as a tree-model adjudication layer (recovers 20% more mis-penalized samples) and transfers to cold domains with ~70% relative mis-penalization reduction.
- **Key Innovations**: Policy-grounding *into weights* rather than prompt-injection; spec-synthesized training without human annotation; high-precision ultra-low-latency verdict-only deployment.
- **Venue**: EMNLP 2026 Industry Track

### 4.2 Following the Preference, Missing the Optimum: Compliance Without Optimization in AI Housing Recommendation
- **Authors**: Hsuan Lo
- **Institution**: —
- **Date**: 2026-09-10 (cs.CY, previously listed 2026-09-06 area)
- **arXiv**: https://arxiv.org/abs/2609.10856
- **Abstract**: 59-page audit of AI housing-recommendation systems showing they satisfy stated preferences (compliance) while systematically missing the user optimum — preference-constrained generation degrades objective quality. One of the clearest documented failure modes linking recommender "satisfaction" metrics to suboptimal real-world recommendations.
- **Key Innovations**: Compliance-vs-optimization gap as a measurable recommender failure; large-scale audit (59 pp., 31 tables).
- **Venue**: Preprint

> 📌 **Advertising note**: No fresh auction/budget-bid papers in this Friday window beyond the 09-11 [[arxiv-daily]] items (meCPM, UniCon) and the SIRF content-risk model above. Generative-ad work (GR4AD, GOAL, UniVA) from late August remains the advertising SOTA; this week's momentum is on recommender *foundation/system* architecture (UniRec, Auto-RecSys) rather than new interaction models.

---

## 5. Sequential Modeling & Time Series

### 5.1 RDDMPI: Residual Denoising Diffusion Model for Probabilistic Multivariate Time Series Imputation
- **Authors**: Ramiro Valdes Jara, David Chapman, Adam Meyers
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11648
- **Abstract**: Reformulates probabilistic MTS imputation as baseline-residual decomposition: a pretrained deterministic imputer captures the dominant signal, and the diffusion model generates only the residual uncertainty. Conditions reverse denoising on both the baseline-completed signal and its latent representation, with a reliability-aware mechanism that adaptively gates baseline influence. Simplifies the diffusion objective from full-signal reconstruction to structured correction terms, improving both reconstruction accuracy and uncertainty calibration on multiple benchmarks.
- **Key Innovations**: Diffusion in residual (not data) space for imputation; reliability-gated baseline conditioning; simplified learning objective.
- **Venue**: Preprint

### 5.2 When Does Text Inform? Benchmarking Information-Theoretic Metrics for Multimodal Time-Series Forecasting
- **Authors**: Emma Andrews, Gianmarco Mengaldo
- **Institution**: NTU Singapore (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11282
- **Abstract**: Builds the first ground-truth benchmark for "does this text annotation add predictive value to TS forecasting?", with synthesized annotations that are semantically correct / incorrect / irrelevant. Evaluates six MI estimators (KSG, MINE, InfoNCE, CCA, PID, V-information): all identify correct annotations as most informative and can audit mixed corpora, choosing annotations that yield best downstream forecasts without training models. Validate on seven real datasets and give practical implementation rules.
- **Key Innovations**: Ground-truth multimodal-TS annotation-value benchmark; estimator-agnostic auditing method; no-training-needed annotation selection.
- **Venue**: Preprint

### 5.3 SolCloudLLM: Bidirectional Multimodal Fusion of Sky Images and Time-Series for Solar Forecasting with LLMs
- **Authors**: Ken Chen, Maneesha Perera, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge
- **Institution**: University of Melbourne (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11135
- **Abstract**: Aligns sky-image patches with time-series patches and fuses them bidirectionally into the LLM embedding space for short-term PV/GHI forecasting. Outperforms best baselines on SIRTA and SKIPP'D in MSE at all horizons (up to −25.4% relative), with gains concentrated in cloudy conditions and in few-shot settings where non-learning physical models beat degraded DL baselines.
- **Key Innovations**: First LLM-forecasting framework fusing imagery + TS bidirectionally; cloud-ramp signal utilization; strong few-shot/site-scarce performance.
- **Venue**: Preprint

### 5.4 CryptoL: Scale Dominance and Physics-Constraint Mitigation in Financial Multivariate Time-Series Forecasting
- **Authors**: Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli, Maryam Amirshahkarami, Mohammad Ebrahim Mahdavi, Hossein Karshenas
- **Institution**: Iran academia (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11206
- **Abstract**: Multivariate crypto forecasting faces extreme cross-asset scale heterogeneity and structural OHLC constraints. CryptoL: (1) evaluates error in context-normalized RevIN coordinates to stop inverse-normalization weighting large-scale assets; (2) keeps channel-dependent affine normalization to preserve candle-order relations; (3) adds scale-adaptive numerical stabilization and a soft feasibility loss penalizing violations of OHLC inequalities. Ablations show better accuracy, training stability, and finite validity of OHLC predictions.
- **Key Innovations**: Scale-bias removal via context-normalized loss; structure-preserving normalization; physics (OHLC inequality) constraints as soft loss.
- **Venue**: Preprint

### 5.5 DF-LLM: A Dynamic Fusion Large Language Model for Traffic Flow Prediction
- **Authors**: Xue Qiu, Jianli Xiao
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11314
- **Abstract**: LLM-based traffic forecasting adding a spatiotemporal embedding module, a graph-convolution spatiotemporal fusion module feeding spatial topology + dynamic dependencies into the LLM backbone, differentiated parameter adaptation, a context-aggregation attention module for global dependencies, and residual connections to fight gradient vanishing. Reports better metrics on all four datasets vs baselines.
- **Key Innovations**: Graph-fused LLM for spatiotemporal sequences; context-aggregation attention; residual-connected LLM backbone.
- **Venue**: WISA 2026

---

## 6. Game AI, Game Theory & RL

### 6.1 Existence of the Core in Approval-Based Committee Elections
- **Authors**: Patrick Becker, Matthias Greger, Dominik Peters
- **Institution**: TU Wien / CNRS-affiliated (tentative, Peters)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11912
- **Abstract**: Settles the main open question in approval-based multi-winner elections: a committee in the **core** always exists. The proof introduces a voting rule optimizing an entropy-like objective over committees and payment systems; all local optima lie in the core, and a core committee is found in polynomial time. (Proof obtained with GPT-6 Astra verification assistance.)
- **Key Innovations**: Resolution of a long-open existence question; constructive entropy-optimization voting rule; poly-time core finding.
- **Venue**: Preprint (20 pp.)

### 6.2 Not Converging to Bad Nash Equilibria (ABRA) & 6.3 Truncated Noisy Best-Response (TNBR)
- **Authors**: Vartika Singh, Philip N. Brown
- **Institution**: University of Colorado Colorado Springs (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11889 (ABRA) / https://arxiv.org/abs/2609.11863 (TNBR)
- **Abstract**: (ABRA) For submodular-coordination games where Nash equilibria are within 50% of optimal but the worst-case equilibria are unstable, an Approximate Best-Response Algorithm with a noise parameter (to escape bad equilibria) and rationality parameter (balancing noise-induced degradation) provably *cannot* converge to a low-quality equilibrium: recurrent classes containing a <50%-of-optimal profile must also contain the optimum or a >50% profile. (TNBR) Generalizes to a family of asynchronously, stochastically perturbed best-response algorithms and computes Markov-chain recurrent-class bounds: "Performance" bounds guarantee a high-value recurrent state; "Safety" bounds rule out arbitrarily-bad recurrent states — linked by a waterbed-like tradeoff.
- **Key Innovations**: First algorithms with formal low-quality-equilibrium *avoidance*; recurrent-class safety/perf bounds; waterbed characterization.
- **Venue**: Preprint

### 6.4 Tapes Together Strong: The Co-evolution of Computation and Cooperation
- **Authors**: Kunal Jha, Francesco Cicala, Blaise Agüera y Arcas, Blake Aaron Richards, Natasha Jaques, Max Kleiman-Weiner, Eyvind Niklasson
- **Institution**: Google DeepMind / Mila-affiliated (tentative)
- **Date**: 2026-09-09
- **arXiv**: https://arxiv.org/abs/2609.10817
- **Abstract**: Introduces Autopoietic Game Theory: social interaction, replication, and computational cost are endogenous and co-evolve in a substrate of randomly initialized Z80 machine-code programs. Embedding a social dilemma into the physics of computation favors self-replicating cooperative strategies; under scarce resources, defection becomes self-limiting (stealing burns shared energy and slows execution). Evolved programs suppress stealing across environments; spatial assortment boosts structural complexity and task performance; the framework absorbs exogenous pressures (math tasks as sequential social dilemmas) when rewards tie to computation budget.
- **Key Innovations**: Universally-co-evolving autopoiesis + game theory; defection-self-limiting economics; linking computation capacity to energy as a cooperation scaffold.
- **Venue**: Preprint

### 6.5 ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI
- **Authors**: Zhengran Ji, Jonathan Hyun, Boyuan Chen
- **Institution**: Duke University (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11737
- **Abstract**: Applies human organization theory (pooled vs sequential interdependence) to assemble task-specific hierarchical organizations of up to 50 heterogeneous embodied agents (LLM-driven) across 25 wildfire-response missions. Human-designed ORCH orgs beat 4 representative multi-agent frameworks by +63.97% mission score and +74.29% execution efficiency; LLM-generated orgs by +43.63%/+52.53%. Performance is NOT monotonic in model scale; long-horizon missions keep concurrent activity within specialist groups while coordinating ordered phase transitions.
- **Key Innovations**: Organization structure as a first-class design variable for multi-agent systems; guided LLM org-design; scale-non-monotonicity finding.
- **Venue**: Preprint

### 6.6 COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization
- **Authors**: Pingchen Lu, Xiangyi Wang, Xiang Li, Jie Mao, Zikun Qu, Junfeng Luo, Yao Shu, Bryan Kian Hsiang Low, Zhongxiang Dai
- **Institution**: NUS / NTU (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11682
- **Abstract**: Budgeted sequential skill optimization: a contextual-bandit prioritizer allocates costly execution-based evaluations to promising/informative candidates while an evolution loop refines the skill population from execution feedback. Across 6 agent benchmarks × 3 target models, achieves strongest average performance while cutting optimization cost 55–58% vs SkillOpt and using only 50 unique examples per benchmark; robust to harness changes and works when the target model self-generates skills.
- **Key Innovations**: Bandit-scheduled evaluation budgets for skill evolution; evidence-grounded candidate refinement; extreme sample efficiency.
- **Venue**: Preprint

---

## 7. Agents & Agentic RL

### 7.1 T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks
- **Authors**: Junyao Yang, Yucheng Shi, Zhongzhi Li, Ruhan Wang, Zongxia Li, Haitao Mi, Leowei Liang
- **Institution**: Industry (large lab, tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11042
- **Abstract**: 122B-total MoE terminal agent trained with RL in a real cloud shell for 300+ tool-call turns per task, rewarded by each task's own verifier. Recipe: aggressive warm-start + dense process reward (number of passing verifiers), TITO exact-token training with drift repair at turn boundaries, and rollout routing replay (sampler's per-token MoE expert choices replayed during training) — cutting train-to-inference log-prob gap 0.021→0.013. On Terminal-Bench 2.1 resolves 64.0% (from a 43.8% base) and hits 27.9% on Long-Horizon Terminal Bench, surpassing GPT-5.4 and GLM-5.1.
- **Key Innovations**: End-to-end terminal-agent RL recipe (warm start → dense reward → TITO → expert routing replay); strictly out-of-distribution corpus for transfer proof; surpasses proprietary baselines on long-horizon terminal tasks.
- **Venue**: Preprint (37 pp.)

### 7.2 Mr.LHDR: A Benchmark for Multimodal Real-World Long-Horizon Deep Research Agents
- **Authors**: Minghao Guo, Meng Cao, Sui Zhao, Siyu Ning, Xin Wang, Haoze Zhao, Jiaxuan Yang, Haihong Hao, Mingfei Han, Shunlin Rong, Haijun Wu, Xiaodan Liang, Xiaojun Chang
- **Institution**: SYSU / UTS-affiliated (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11318
- **Abstract**: Deep-research benchmark built on hidden Node-Relation graphs requiring avg 12.1 necessary intermediate conclusions with mean dependency depth 10.4, multimodal evidence (images, maps, PDFs, logos, charts, tables, video frames) with ≥1 non-text element that changes the reasoning state. Evaluates final answers AND intermediate-conclusion correctness (OA/SA/CS/DACS). Strongest system reaches only 43.1% OA / 34.3% SA — final-answer accuracy overestimates complete research success; removing images drops DACS 12.6 pts; SA declines as chains lengthen. Sustained dependency-consistent evidence integration is the key bottleneck.
- **Key Innovations**: Dependency-graph-grounded long-horizon research benchmark; intermediate-conclusion auditing; multimodal-necessity measurement.
- **Venue**: Preprint

### 7.3 Artificial Id: Drive and Persistent Alignment in Agentic AI
- **Authors**: Yakov Pyotr Shkolnikov
- **Institution**: —
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11911
- **Abstract**: Proposes an "artificial id" — an adaptive internal drive determining whether agent behavior should continue, stop, or change across task boundaries — as the missing control primitive for long-lived agentic systems. In a minimal Petri-dish experiment a controller with no task-specific objective develops useful control through differential persistence; the same mechanism can select unintended physical strategies and replace learned sensor mappings when their meaning changes. Argues scalability requires a persistent alignment boundary over trusted observations, consequence channels, state, authority, identity, provenance, and hard constraints.
- **Key Innovations**: Persistence-based drive as emergent goal-selection mechanism; agentic alignment reframed as property of the continuing system, not single trajectories.
- **Venue**: Preprint

---

## 8. ML Foundations & Evaluation

### 8.1 CausalArena: Benchmarking Causal Discovery in the Foundation Model Era
- **Authors**: Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang, Han-Jia Ye
- **Institution**: Nanjing University (tentative)
- **Date**: 2026-09-10
- **arXiv**: https://arxiv.org/abs/2609.11897
- **Abstract**: Unified, evolvable causal-discovery benchmark with three synthetic regimes (controlled SCM breadth; human-auditable semantic operational SCMs; formula-grounded explicit-mechanism SCMs) plus real-world data for external validity. Evaluates classical, neural, and foundation-model causal discovery (CDFMs). Substantial ranking shifts across SCM families/protocols — strong performance in one regime does not transfer; calls out pretraining–evaluation overlap as a central confound for CDFM claims.
- **Key Innovations**: First benchmark isolating pretraining-overlap confound for causal-discovery foundation models; multi-family SCM protocol.
- **Venue**: Preprint (47 pp.)

---

## Summary Statistics

| Category | Papers Count |
|---|---|
| LLMs — Post-Training, Reasoning & Interpretability | 8 |
| LLM Serving, Compression & Efficiency | 3 |
| Recommendation Systems & Retrieval | 7 |
| CTR Prediction & Advertising | 2 |
| Sequential Modeling & Time Series | 5 |
| Game AI, Game Theory & RL | 6 |
| Agents & Agentic RL | 3 |
| ML Foundations & Evaluation | 1 |
| **Total (this report)** | **35** |
| Overlaps moved to 09-11 [[arxiv-daily]]/[[arxiv-ai-search]] | 10 (not re-featured) |

## Key Trends

1. **Self-referential training is reshaping the post-training agenda**: Negative Self-Distillation (diverge from your own flaws) and the OPD per-token gating family refine how models learn from *themselves*, while the Fragility Spectrum warns that checkpoint-intrinsic susceptibility to recursive-training collapse is a first-class property to manage.

2. **Verification is becoming an inference-time primitive**: Magenta (Lean-backed math decoding), T1 (task-verifier rewards for terminal agents), and Mr.LHDR (dependency-graph auditing) all treat "machine-checked correctness" rather than plausibility as the objective — consistent with the week's earlier PARSER/reward-modeling work.

3. **Efficiency shifts from post-hoc fixes to architectural/parameterization choices**: FlexComp treats the compression ratio as a per-input decision; LOCUS shows verbosity is a property of the *low-rank subspace* used in alignment; Kashin-DCT quantization gets stability rather than just precision. KV cache and output-token cost keep dominating the serving roadmap (c.f. 09-11 [[arxiv-daily]]).

4. **Recommendation research is thinning toward systems/foundations**: the week's rec news is UniRec/FedHUR (already in [[arxiv-daily]]), Auto-RecSys (agents running recsys experiments), and a unifying regularization theory for linear recommenders — few genuinely new user-modeling architectures.

5. **Game theory returned to equilibrium *quality***: ABRA/TNBR prove algorithms that *cannot* converge to bad Nash equilibria, and the approval-committee core existence is settled after many years — policy-relevant robustness guarantees are making a comeback.

6. **Agents: verification + persistence + organization**: T1 (verifier-driven long-horizon terminal RL), ORCH (organization structure as a system-design variable), Artificial Id (persistence across task boundaries), and COBRA-Skills (bandit-budgeted skill evolution) point to "durable agentic systems" as the frontier beyond single-task agents.

7. **RAG/retrieval safety and sufficiency get dedicated instrumentation**: RAG-Safety-Bench proves guardrails don't transfer to RAG downstream; distribution-shape QPP gives a cheap 2 ms/query retrieval-sufficiency signal; GLIE shows late-interaction embeddings are generatively compressible.