---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-10)
type: synthesis
created: 2026-10-10
updated: 2026-10-10
sources: []
tags:
  - arxiv
  - ai
  - llm
  - recommendation
  - advertising
  - sequential-modeling
  - ctr
  - games
  - daily-digest
---

# arXiv Daily Report (2026-10-10)

Search scope: primary sweep = the **2026-10-08 (Thu) arXiv announcement day**, the latest indexed in the export API as of the 2026-10-10 ~10:00 run (no 2026-10-09 or 2026-10-10 announcements were present). Full category sweeps of `cs.AI` (237), `cs.LG` (230), `cs.CL` (119), `cs.IR` (16), `cs.GT` (8) → 480 unique entries. Because the recsys/advertising/games lanes were empty in that batch, dedicated `abs:`-field topical sweeps ran over the wider window **2026-10-04 → 2026-10-09** for recommendation, sequential modeling, advertising/click-through, auctions / mechanism design, and games; those finds are tagged with their own publication dates. **All 47 featured papers are new to the wiki (grep-verified 0-hit against 6,960 repo-wide arXiv IDs).**

> ⚠️ Metadata note: The arXiv Atom API does **not** expose author affiliations. **Institution/company** is filled only where the abstract, comments, or code link state it; otherwise marked `not stated (arXiv metadata omits affiliations)`. Where the abstract names corpora/platforms (DiDi, Alibaba), this is quoted as the *data source*, not necessarily the authors' employer. No HTTP 429/rate-limiting was observed on this run.

## Core AI / LLM / Agents

### 1. NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents
- **Authors**: Min-Young Yu, Tony Kim, Jang Won Choi
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CR; cs.AI; cs.LG
- **Abstract**: Tool-using LLM agents violate the policies they are deployed to enforce, often silently. Prior defenses hand-write rules, query an LLM verifier per action, or compile policies through heavy formal machinery — and naive compilation fails (extracted rules block the tool satisfying their own precondition, or read arguments the tool lacks).
- **Key innovations**: `NOMOS`, a four-pass compiler turning natural-language policy into a deterministic tool-call gate; statically verifies with **tool-schema-level checks only** (no prover, solver, or LLM), repairing or rejecting 37% (airline) / 13% (retail) of candidates. On `τ²-bench` gates violations of reference clauses among state-changing calls from 66.3%→2.6% (airline) and 30.8%→6.9% (retail); zero ASR on banking (nine attack families collapse onto three structural rules), ≤3.6% on the other three suites. Microseconds per decision with no LLM call; a 26B open-weight on-premise compilation is not significantly worse than hand-written or frontier-compiled rules.
- **arXiv**: https://arxiv.org/abs/2610.11030

### 2. What to Admit and How to Present: Governing Persistent Memory in LLM Agents
- **Authors**: Chang Liu, Deliang Ding
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Persistent memory improves personalization in LLM agents but can also induce sycophancy and cross-domain leakage. The paper separates two governance decisions — *admission* (what recalled information enters the working context) and *presentation* (how admitted information is expressed).
- **Key innovations**: Two training-free inference designs: factor-compiled admission (FC; assesses whole memory entries) and permission-semantic admission (PS; decomposes entries into typed units), both translated into eligibility decisions via deterministic policies. FC/PS cut pooled judge-assessed failure by 6.7 / 8.8 pts (p=2.7e-7 / 4.1e-12) vs. verbatim injection; cross-domain leakage down up to 29.5 pts; tightening admission alone further cuts cross-domain failure 17.5 pts. Cautionary: both designs *increase* personalization failures — selection improves safety while "preserving beneficial memory use remains unresolved."
- **arXiv**: https://arxiv.org/abs/2610.11188

### 3. Thinking Inertia: LLMs Keep Thinking When Told Not To
- **Authors**: Dianqiao Lei, Kevin Qinghong Lin, Pan Lu, Philip Torr, James Zou
- **Institution**: not stated (author list Oxford/Stanford-adjacent; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: LLMs increasingly ship with explicit "thinking modes," yet "no-thinking" behavior is under-studied. Prior proxies (disabled thinking mode, absence of long traces) are unreliable.
- **Key innovations**: Three-level measurement — Empty-Thinking Rate (answer-only compliance), instruction-aware Question-Pre-answer Relevance, and LLM-as-judge Explicit Inference Rate — distinguishing answer-only, relevant-but-non-inferential, and visible-inference outputs. Across six interventions × six LLMs, explicit no-think controls **cannot reliably eliminate visible inference** ("Thinking Inertia" grows as the answer space opens); supplying candidate answers makes answer-only responses easier. Establishes no-thinking as a non-trivial capability worth systematic evaluation.
- **arXiv**: https://arxiv.org/abs/2610.11765

### 4. Language Modeling is Monotone Compression
- **Authors**: Noam Mazor, Andrew Morgan, Rafael Pass
- **Institution**: not stated (authors Cornell-adjacent; unconfirmed)
- **Subjects**: cs.IT; cs.AI; cs.CR
- **Abstract**: A long-standing hypothesis ties intelligence to compression; empirical work shows LLM compression ability correlates with benchmark performance. This work initiates the *theoretical* study.
- **Key innovations**: Proves LLMs (as next-token predictors) are equivalent to **monotone (order-preserving) compression algorithms** — each constructible from the other with error preserved up to an additive gap of 2. Monotonicity is required for this equivalence **if and only if** cryptographic one-way functions exist. Corollary: next-bit pseudoentropy ≡ monotone incompressibility (previously only incompressibility→pseudoentropy was known).
- **arXiv**: https://arxiv.org/abs/2610.11031

### 5. Looking Inside LLMs: Small-World Connectivity as a Signature of Reasoning Performance
- **Authors**: Zheng Huang, Sansheng Cao, Enpei Zhang, Weikang Qiu, Elynn Chen, Xiang Zhang, Yaoqing Yang, Rex Ying, Dawei Zhou, Yujun Yan
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Understanding LLM reasoning requires looking beyond behavioral performance. Analogous to neuroscience findings linking intelligence to small-world brain organization, this work studies small-world functional connectivity in LLMs.
- **Key innovations**: Functional graphs from attention-head activation similarities; a higher **small-world index (SWI)** correlates with better fluid reasoning across models/checkpoints. High "core" / low "bridge" scores on performance-critical heads → `SWA` (Small-World Allocation), a hierarchical sparsity allocation for pruning that preserves small-world structure and cuts WikiText perplexity by up to 20% across six LLMs. A structural, mechanism-level complement to behavioral evaluation.
- **arXiv**: https://arxiv.org/abs/2610.12304

### 6. Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict
- **Authors**: Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, Jingyu Zhang, Jie Gao, Mark Dredze, Daniel Khashabi
- **Institution**: not stated (JHU-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.CL
- **Abstract**: When retrieved evidence contradicts an agent's prior beliefs, does it revise, hedge, or persist? Existing agentic evaluations focus on task success, not how agents handle conflict.
- **Key innovations**: Operationalizes **epistemic humility (EH)** via three trajectory-level dimensions — Identify / Solve / Escalate (ISE) — evaluated under controlled and naturally-occurring knowledge conflict with matched no-conflict controls. Finding: **higher task accuracy ⇏ greater humility**; agents detect conflicts early but fail to maintain/resolve them in later steps; interventions improve EH but often at the cost of accuracy. Argues EH emerges from the interaction of backbone, harness, and environment.
- **arXiv**: https://arxiv.org/abs/2610.12360

### 7. Not Every Change Is Necessary: Recoverable Drift in Large Language Model Unlearning (PTP-U)
- **Authors**: Xunlei Chen, Qinghui Gong, Jingkun Xue, Qihe Liu, Shijie Zhou, Fei Ye
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Machine unlearning aims to remove unwanted knowledge while preserving other capabilities; achieving target forgetting can still leave unlearned collateral change.
- **Key innovations**: `Propose-Then-Project Unlearning (PTP-U)` — local analytic edits weaken target associations, then non-target output distributions are aligned to the original model under fixed forgetting constraints. Across three benchmarks: **81.22–91.03% forgetting while preserving 94.20% non-target utility** on average; at matched forgetting, PTP-U consistently retains higher non-target utility.
- **arXiv**: https://arxiv.org/abs/2610.11915

### 8. Minimax Gaussian Mechanisms for Continual Machine Unlearning
- **Authors**: Qi Kuang, Yin Xia
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: stat.ML; cs.LG
- **Abstract**: Machine unlearning updates a trained model after record deletions to match exact retraining without re-running training — a sequential, continual problem under repeated deletion requests.
- **Key innovations**: Gaussian mechanisms for **Newton updates under a stream of deletions**, giving full-sequence indistinguishability from exact retraining certified via Gaussian differential privacy + adaptive composition. Match/improve on minimax noise among fixed Gaussian covariances; random-walk noise asymptotically matches single-release worst-case variance (independent noise pays order-M more); set-based bounds leverage per-record gradients/Hessians. Includes parameter and predictive consistency results with a credit-default application.
- **arXiv**: https://arxiv.org/abs/2610.11628

### 9. Agentic-TTT: Training Test-Time Policy for Test-Time Training
- **Authors**: Jiahao Lu, Mohan Kankanhalli
- **Institution**: not stated (NUS-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI; cs.CL
- **Abstract**: Test-time training (TTT) adapts an LLM's parameters with test-input signals and can give striking gains in pre-specified settings, but no single TTT algorithm fits every setting — each works in different regimes and an ill-suited method wastes compute or hurts.
- **Key innovations**: `Agentic-TTT` learns a *test-time policy* deciding **whether to TTT, which algorithm to invoke, and whether an existing skill can be reused** — turning TTT procedures into callable tools over an evolving deployment environment, trained on observed utility gains. Nearly doubles utility over the backbone, learns utility-vs-compute trade-offs, and generalizes to unseen domains. Argues toward autonomous, deployment-driven self-improvement.
- **arXiv**: https://arxiv.org/abs/2610.12002

### 10. Cost-Aware Mixture-of-Experts Coordination for Model Markets
- **Authors**: Yizhou Ma, Wenbo Wu, Xikun Jiang, Zhuoqin Yang, Luis-Daniel Ibáñez
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.DB; cs.LG
- **Abstract**: Model marketplaces trade/select individual models as indivisible units, ignoring complementarities among heterogeneous experts. This work lifts MoE from a model-level architecture to a market-level coordination mechanism.
- **Key innovations**: Brokers use gating networks to coordinate multiple frozen heterogeneous experts into a composite service; a welfare objective combines predictive utility with execution costs; a **cost-aware gating + market-aware training objective** and a cost-adjusted revenue allocation rule (budget balance, participation monotonicity, cost sensitivity). Best mean welfare on all 15 tabular/image benchmarks, lower expected cost than standard MoE in every case, ~Shapley-comparative allocation at far lower overhead. Relevant to the wiki's model-economy / BYOAI themes.
- **arXiv**: https://arxiv.org/abs/2610.11908

## Reasoning / RL / Test-Time Compute / Scaling

### 11. Learning to Plan by Looking Back: Hindsight Hierarchies for Training Reasoning Models
- **Authors**: Lars Simon, Holger Eble, Manuel Radons
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.LG; cs.LO
- **Abstract**: When a problem exceeds a model's current solving ability, an *additionally supplied* solution may let it extract useful solution ideas in hindsight.
- **Key innovations**: `Hindsight Hierarchies` — a self-improvement loop jointly training one model to (i) predict solution ideas from problems alone, (ii) reverse-engineer ideas from problems + known solutions, and (iii) solve using provided ideas, cycling reverse-engineering→extra supervision. Formal specification + concrete instantiation for interactive theorem proving in Lean (empirical evaluation noted as future work). A clean idea-extraction framing for reasoning RL.
- **arXiv**: https://arxiv.org/abs/2610.12168

### 12. When KL Regularization Misfires in Group Policy Optimization (ZCPO)
- **Authors**: Fei Ding
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: Why does removing reference-policy KL sometimes *improve* group policy optimization? This studies how reference-policy information should enter group-relative updates.
- **Key innovations**: Catalogues **seven failure modes** in the KL↔reward interaction (residual KL after clipping / gradient cancellation, identical-reward groups, length-dependent KL growth, token-concentrated KL, sampling noise when KL enters rewards). Proposes `ZCPO` (Zero-Sum Calibrated Policy Optimization), which uses relative drift measured by *conditional* KL to calibrate within-group reward coefficients; validated on math-reasoning experiments and ablations. Directly relevant to GRPO/RLVR (see also [[rlhf]]-adjacent wiki pages).
- **arXiv**: https://arxiv.org/abs/2610.12161

### 13. RL-ARC: Calibrating Large Reasoning Models via Reasoning-guided Uncertainty
- **Authors**: Gukhyeon Lee, SangKeun Lee
- **Institution**: not stated (Korea Univ. author list; unconfirmed)
- **Subjects**: cs.AI; cs.CL; cs.LG
- **Abstract**: RLVR improves reasoning but does not account for calibration, causing overconfidence. Calibration-aware trained LMs still overconfident under distribution shift while sacrificing reasoning.
- **Key innovations**: `RL-ARC` jointly uses **reasoning confidence as an auxiliary signal** for answer confidence — reasoning-guided regularization on correct cases, overconfidence penalty on incorrect ones. ID + OOD results: better calibration *and* adaptive confidence estimation without substantially sacrificing reasoning performance.
- **arXiv**: https://arxiv.org/abs/2610.11352

### 14. Balancing Reference Guidance and Free Generation in Trajectory Rollouts for Reasoning RL (ARG)
- **Authors**: Hanyu Wang, Nakul Agarwal, Hossein Nourkhiz Mahjoub, Ehsan Moradi Pari, Makoto Fukushima, Jinghui Chen, Vaishnav Tadiparthi
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: A verified reference gives a correct trajectory; a prefix-guided model generates its own. How much reference guidance is right? Compared via prefix continuation whose KL to the ideal (verify-conditioned) distribution is derived in closed form.
- **Key innovations**: KL decreases with (probability of generating a different correct trajectory) × (reference surprisal) — so longer prefixes raise the former but lower the latter; continuation success alone doesn't decide. Learns a shared **prefix selector (ARG)** from continuation outcomes without estimating success probabilities or extra generation. Applied to all-failure groups in GRPO: highest aggregate pass@12 on Qwen3-4B/8B across five math-reasoning benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.11128

### 15. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization
- **Authors**: Ming Chen, Rong-Xi Tan, Ke Xue, Yu-Jie Zhou, Taiye Lu, Zhi-Xuan Gao, Peng Xie, Zijun Shen, Chen Lu, Haopu Shang, Chao Qian
- **Institution**: not stated (University of Science and Technology of China-adjacent author list; unconfirmed); code: github.com/lamda-bbo/agentic-bbo
- **Subjects**: cs.LG; cs.AI; cs.NE
- **Abstract**: LLM agents doing black-box optimization (BBO) combine task semantics, computation, and feedback; existing studies differ in domains/configs, so effects of design choices can't be isolated.
- **Key innovations**: `AgenticBBO-Bench`, a cross-domain benchmark (synthetic, HPO, DB tuning, chip design, molecular design) under a unified finite-budget protocol. Agentic BBO beats direct LLM baselines in all five domains and the best numerical optimizers in four. Findings: extra numerical tools don't consistently help, task semantics broadly useful / specific priors less reliable, and numerical optimizers absorb search gains well. GPT-6 Astra and DeepSeek-V4.1-Flash sit on the performance–cost Pareto frontier.
- **arXiv**: https://arxiv.org/abs/2610.12183

### 16. Softmax Attention on Gaussian Mixtures: Linear When It Can, Selective When It Must
- **Authors**: Simon Gabet, Etienne Boursier, Claire Boyer
- **Institution**: not stated (ETH-adjacent author list; unconfirmed)
- **Subjects**: stat.ML; cs.LG
- **Abstract**: In the infinite-prompt limit on pure Gaussian data, softmax attention reduces to a linear map — removing exactly the query-dependent selection that distinguishes it from linear attention.
- **Key innovations**: Extends the analysis to **Gaussian mixtures**, which keep tractability but introduce multimodality/nonlinear dependencies. Softmax attention represents and learns (via gradients) optimal solutions for supervised classification and denoising: it matches linear attention on linear tasks **and** exploits query-dependent context selection for nonlinear tasks beyond linear attention's reach — a precise statement of why "selective" attention pays off in structured latent data.
- **arXiv**: https://arxiv.org/abs/2610.11798

### 17. Emergent Inverse-Depth Scaling From Nonlinearity In Attention
- **Authors**: Zirui Peng, Yizhou Liu, Ziming Liu, Jeff Gore
- **Institution**: not stated (MIT-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Scaling laws describe power-law gains in model size, but the mechanism is not fully understood. In linear-attention theory, parameter-count scaling ties to the power-law spectrum of data.
- **Key innovations**: Shows nonlinear attention yields **inverse-depth decay of loss across all tested data spectra** — a novel depth-scaling law. Nonlinearity lets attention focus selectively on relevant tokens so strong/weak spectral directions are learned in parallel; layer-wise focusing motivates a central-limit-theorem-style aggregation picture (shared error sets the plateau, aggregation turns layer differences into gains). Suggests depth scaling may *arise from attention nonlinearity*, making global covariance less relevant.
- **arXiv**: https://arxiv.org/abs/2610.11063

## Efficiency / Inference / Deployment

### 18. PageWeaver: KV-Guided Query Unions for Sparse Attention
- **Authors**: Zhiyuan Li, Zihan Li, Zefang Yuan, Lei Wang, Hao Wang
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.DC; cs.LG
- **Abstract**: Dynamic sparse attention limits KV pages per query, but small per-query support does not yield efficient GPU work; grouped queries share page loads and populate Tensor Core tiles.
- **Key innovations**: `PageWeaver` assembles query groups by **selected-page affinity** (a bounded GPU search producing query IDs consumed by an ID-aware two-CTA kernel, no reordered Q or cross-page partials). With FP8 KV, 1.70× geometric-mean complete-call speedup vs. FlashInfer on H200 (six captures); 7.88–14.36% whole-model prefill gains; online regrouping cuts latency 3.26–7.66% on 64K-context captures but is marginal at 8K; B300 comparison locates where preparation cost negates the win.
- **arXiv**: https://arxiv.org/abs/2610.11201

### 19. SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference
- **Authors**: Qitong Wang, Xinwei Niu, Mingluo Su, Shanwei Zhao, Shiai Zhu, Huan Wang
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: Layer-wise training-free pruning is a standard fix for memory-bound LLM decoding, but typical Hessian-based calibration uses pre-collected natural sequences while the model generates its own tokens at decode time — a distribution shift that hurts pruned performance.
- **Key innovations**: Calibration matrices built from **layer-wise activations during dense-model autoregressive generation (excluding prefill)** align pruning with decode-time activations; plus an optimized **N:M sparse-matrix-vector kernel** (bitmask indexing, fixed-step traversal) for the SpMV operations that dominate decoding. Up to **1.48× end-to-end decoding speedup** on A100 with Llama-3.1-8B/70B, Qwen3-14B/32B, consistently beating fixed-text calibration on long-form generation.
- **arXiv**: https://arxiv.org/abs/2610.12327

### 20. Where Draft Trees Lose Target Mass: Exit-Guided Speculative Decoding (TEV)
- **Authors**: Shijing Hu, Xuancheng Ren, Zhihui Lu, Pan Zhou
- **Institution**: not stated (arXiv metadata omits affiliations); code: github.com/hsj576/TEV
- **Subjects**: cs.AI
- **Abstract**: Tree-based speculative decoding verifies multiple draft continuations per target pass, but finite trees from draft scores face a fundamental draft–target mismatch.
- **Key innovations**: A **target-flow analysis** proves "1 + target coverage" bounds the expected output-block length of any exact path verifier, and all optimal verifiers share the same exit/bonus-token law. `TEV` is an exact, level-parallel verifier using one exit-node and one bonus-token decision; the exit law also yields node-level feedback for `ExitTrain` draft-tree training. +13% average block length (ExitTrain), −15% verifier latency, ~14% end-to-end speedup over DDTree.
- **arXiv**: https://arxiv.org/abs/2610.11750

### 21. DynaTE: Accelerating Diffusion LLMs via Dynamic Token Execution
- **Authors**: Minghan Jiang, Jiayi Wang, Shuaiting Li, Haibin Shen, Kejie Huang
- **Institution**: not stated (Zhejiang Univ.-adjacent author list; unconfirmed)
- **Subjects**: cs.AR; cs.AI
- **Abstract**: Diffusion-based LLMs (dLLMs) decouple from autoregressive sequential decoding, but their iterative parallel refinement mismatches both AR accelerators and continuous-denoising DiT accelerators.
- **Key innovations**: Hardware–software co-design that **adapts execution to evolving token states**: skip low-utility token computation with a dimension-reconfigurable PE array; FLDD dependency tracking refines few locally-dependent tokens per iteration (cuts denoising iterations); a streaming vocabulary engine interleaves LM-head token streams. 2.05–2.78× speedup / 2.99–3.93× energy-efficiency over SOTA dLLM accelerators.
- **arXiv**: https://arxiv.org/abs/2610.11284

### 22. Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State Quantization (ZIP-SR / ZE-EDEN)
- **Authors**: Hanyang Li, Shao Tang, Daniel Thomas Braithwaite, Gregory Dexter, Leonardo Neves, Aman Gupta, Hiroto Udagawa, Abhishek Shivanna, Daniel Silva, Rohan Ramanath
- **Institution**: not stated (industry author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Quantizing AdamW's second-moment optimizer state saves storage but quantization errors propagate through moment recurrences into adaptive updates.
- **Key innovations**: Recasts 4-bit optimizer-state quantization in **rounding space**: `ZIP-SR` keeps zero in the second-moment codebook and computes stochastic-rounding probabilities in *preconditioner* space; `ZE-EDEN` uses a zero-excluding codebook with rescaling to fix preconditioner distortion from the positive floor. Across 130M–2.7B GPT/Llama pretraining and SFT, both cut TorchAO 4-bit AdamW's validation-loss gap to 32-bit by up to **70%**.
- **arXiv**: https://arxiv.org/abs/2610.12444

### 23. Rehearse Everything, Remember Nothing: Attic-KV Rehearses What Will Be Read
- **Authors**: Zhiyun Shi
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.LG
- **Abstract**: Many KV caches are compressed before anyone knows what will be asked; the prevailing approach "rehearses" — rereads context and keeps what it attends to. Under tight budgets this backfires.
- **Key innovations**: Diagnosis: rereading spreads the budget, so the answer's own entries survive at chance (31.5 vs 96.5 RULER points at 3% keep ratio). `Attic-KV` is a training-free rehearsal where the model **quizzes itself with Q-A pairs quoting the context** (+ content-adaptive anchors) — "test yourself, don't reread." Best training-free method in 8/8 settings on RULER/LongBench; boosts KVgrad / RestoreKV+ by up to 17.1 / 28.1 pts; +41.9 pts over full rereading at 3% keep ratio.
- **arXiv**: https://arxiv.org/abs/2610.12133

### 24. Smoothing the Top-k Exposure Boundary for Sparse Mixture-of-Experts (Elastic Expert Routing)
- **Authors**: Yunkai Chai, Tong Zhu, Xiaoye Qu, Xuyang Hu, Guanjie Chen, Qipeng Guo, Yu Cheng
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.LG
- **Abstract**: Static top-k expert selection converts a continuous routing distribution into a rigid step function, arbitrarily splitting highly-competitive experts into full-supervision vs zero-feedback zones.
- **Key innovations**: `Elastic Expert Routing` stochastically samples the active-expert budget from a localized discrete distribution around k, softening the threshold into a gradual density while matching expected compute cost. SFT: +0.84 (OLMoE-1B-7B) / +2.02 (Qwen3-30B-A3B) macro-averages; from-scratch pretraining: +1.6 pts average over static top-k. A choose-your-own-adventure cousin of "soft top-k" long used in CTR models — worth linking to [[ctr-scaling-landscape]].
- **arXiv**: https://arxiv.org/abs/2610.11575

### 25. Mid-Training Language Models on Raw Video
- **Authors**: Jaedong Hwang, Xiaoqian Shen, Ernie Chang, Changsheng Zhao, Chong Zhou, Saksham Suri, Qi Qian, Zechun Liu, Lemeng Wu, Qinsi Wang, Raghuraman Krishnamoorthi, Wei Wen
- **Institution**: not stated (industry+academic author list; Meta-adjacent; unconfirmed)
- **Subjects**: cs.CV; cs.AI; cs.LG
- **Abstract**: Multimodal LLMs mostly learn from paired image-text or annotated video; raw web video (no captions) is rarely used to further train a language model.
- **Key innovations**: Mid-train Qwen3-1.7B on **raw YT-Temporal-1B clips by predicting next visual tokens** (no text loss, no captions), then apply identical image-text tuning to isolate the mid-training effect. +2.9 on four video benchmarks, +5.1 on ten image benchmarks, text preserved (48.9 vs 48.0). Gains emerge within 30% of training and plateau; **next-visual-token beats caption prediction**, keeping video mid-training purely self-supervised. Relevant to the wiki's world-model / multimodal direction.
- **arXiv**: https://arxiv.org/abs/2610.11019

## Recommendation / IR / Personalization / Ads-adjacent

*Lane note: no classical CTR-prediction or ad-auction-served ranking paper appeared in the window (dedicated `abs:` sweeps for "CTR", "click-through rate", "advertis*", "recommend*" included); the closest items are the retrieval/system-1 entries below, the industrial thumbnail bandit (§32), and the auction theory in §6. This continues the gap flagged in the 2026-10-09 digest.*

### 26. Autoregressive Retriever: Improving Query Understanding from Item Feedback for Universal Multimodal Retrieval (ARR)
- **Authors**: Jianfei Zhao, Yifan Wang, Feng Zhang, Xin Sun, Chong Feng, Zhixing Tan, Yang Luo, Boyuan Pan, Xu Kai, Yao Hu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR; cs.CV
- **Abstract**: Universal multimodal retrieval encodes a query once and ranks by embedding similarity; retrieved items never get to refine the query.
- **Key innovations**: `ARR` alternates **retrieve → refine query embedding → retrieve** and ranks with the final embedding. SFT gives stepwise contrastive supervision; RL treats feedback items as actions optimized by the final reciprocal rank of a relevant item, via a query-side adapter against a fixed item index. Strong in-domain and zero-shot retrieval; feedback improves inference-time results **and** the initial query embedding itself.
- **arXiv**: https://arxiv.org/abs/2610.11666

### 27. Compact and Efficient Indexes for Learned Sparse Retrieval
- **Authors**: Franco Maria Nardini, Luca Rizzo, Cosimo Rulli, Rossano Venturini
- **Institution**: not stated (university author list; unconfirmed)
- **Subjects**: cs.IR; cs.DB
- **Abstract**: Learned sparse retrieval (e.g., SPLADE-family) indexes are memory-hungry; the paper revisits both inverted-index (candidate selection) and forward-index (scoring) levels on top of SEISMIC.
- **Key innovations**: Inverted side collapses per-block metadata to a single **medoid document id**; forward side reorders the vocabulary by co-occurrence, Δ-gap encodes with SIMD-friendly DOTPACKING8, quantizes values with per-component 4-bit codebooks, and adds the JUMPDOT blocked kernel for sparse queries. At equal accuracy: up to **5.3× faster, ~3× less memory** vs best competitor on MS MARCO; ~1.9× faster and up to 3.9× less memory in the memory-constrained regime. Forward-index compression is SEISMIC-independent (integrated into KANNOLO).
- **arXiv**: https://arxiv.org/abs/2610.12300

### 28. Chaos in the Text: Revealing the Modality Preference in Mixed-Modality Retrievers (Trident)
- **Authors**: Yubo Sun, Chunyi Peng, Yukun Yan, Zhenghao Liu, Zhipeng Xu, Sen Mei, Linlin Xin, Zheni Zeng, Maosong Sun
- **Institution**: not stated (Tsinghua-adjacent author list; unconfirmed)
- **Subjects**: cs.IR
- **Abstract**: Whether dense retrievers extend reliably to mixed corpora of text, image, and fused text-image documents is unclear; performance is strongly sensitive to modality composition.
- **Key innovations**: A striking **V-shaped performance curve** as image documents are replaced with semantically-corresponding text — and irrelevant *text* degrades retrieval more than irrelevant images ("Chaos in the Text"), with text representations systematically outranking relevant images (modality preference). Mitigation: `Trident` co-equals text/image/fused **positive views** with Multi-Positive View InfoNCE (relevance discrimination + view balance). Improves mixed-modality retrieval on CLIP- and VLM-based architectures and raises single-modality performance.
- **arXiv**: https://arxiv.org/abs/2610.11816

### 29. Learning Multi-Step Query Rewriting via Corpus Feedback for Conversational Search
- **Authors**: João Coelho, Hong Wang, Jie Yuan, Zhuoer Wang, Samson Koelle, Wei Niu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR
- **Abstract**: Conversational query rewriting (CQR) usually rewrites once from dialogue history before a single retrieval pass — no corpus evidence is available to correct reference resolution or vocabulary.
- **Key innovations**: Recasts CQR as **sequential retrieval**: an agent rewrites → retrieves → rewrites again conditioned on returned passages, in a typed action space (standalone query / lexical reformulation / pseudo-document / stop), trained by SFT then RL on retrieval-quality reward **without human rewrite annotations**. Outperforms retrieval-aligned baselines on TopiOCQA/QReCC; generalizes to CAsT without retraining. Analysis shows reward-optimization alone induces grounded pseudo-document behavior.
- **arXiv**: https://arxiv.org/abs/2610.10955

### 30. Personalization Matters: Long-Horizon Conversation Agent with User-Centric Information in Online Shopping Interactions
- **Authors**: Rena Gao, Yue Dai, Hao Guan, Shengxiang Gao, Wangyang Wu, Yixin Shen, Jey Han Lau
- **Institution**: not stated (arXiv metadata omits affiliations); code: github.com/RenaGao/Multimodel_RAG_Indexing
- **Subjects**: cs.MA
- **Abstract**: Personalized conversational shopping requires preference consistency over multi-turn interactions where users reveal constraints gradually; static profiles and un-controlled long-horizon behavior fall short.
- **Key innovations**: Multi-agent, multimodal RAG framework decomposing dialogue-state tracking, recommendation retrieval, preference-aware reasoning, and response generation over product metadata + reviews + image-derived descriptions + user history; trajectory-level evaluation across four dimensions (Global Preference Consistency, Cumulative Information Synthesis, Interaction Trajectory, Tone Consistency). Retrieval variants score 4.82 vs 3.74 (no-RAG) on Amazon Reviews 2023; a small human study rates the full variant 4.60/5 vs 2.20 baseline. Relevant to the wiki's conversational/agentic-recommendation thread.
- **arXiv**: https://arxiv.org/abs/2610.11375

### 31. DPPM: Dual-Path Parametric Memory for Personalized Language Models
- **Authors**: Yuhao Chen, Shuochen Liu, Jiayao Shi, Jian Hong, Chen Cheng, Xinyun Ding, Tao Wang, Ya Li, Quan Liu, Tong Xu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Parametric memory encodes interaction history into adapters to avoid context bloat, but independent context compilation leaves cross-session integration unspecified while recurrent updates attenuate early evidence.
- **Key innovations**: `DPPM` — an **Evidence path** directly pools interaction-history representations (preserves earlier evidence) and a **Delta path** sequentially updates an associative state (captures change); fused outputs give history-conditioned LoRA adapters. 54.22% on PersonaMem-v2, 86.79% on PrefEval across backbones. A clean "evidence + delta" design for cross-session personalized memory (see [[memory in LLM agents]]-adjacent wiki content).
- **arXiv**: https://arxiv.org/abs/2610.11776

### 32. Billion-Scale Thumbnail Optimization for Uncurated Short-Form Videos via Multi-Armed Bandits
- **Authors**: Ying Han, Ling Liu, Fabio Soldo, Vu Nguyen, Danio Wang, Liz Kidd, Yongle Cao, Theodore Rose, Su-Lin Wu, Romer Rosales
- **Institution**: not stated (industry author list; a major short-form video platform, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Many short-form videos are published without human-selected artwork, so platform thumbnail choices default to static frames; this paper deploys real-time thumbnail optimization at O(B) scale.
- **Key innovations**: **First published O(B)-scale online MAB for uncurated short-form video discovery**: multi-stage candidate generation + low-latency serving, seeded by image-specific priors from a deep visual-quality model to cut exploration cost. Global deployment reports statistically significant gains in discovery/engagement core metrics. Strong industrial evidence for bandit-based creative selection — relevant to the wiki's ads/creative lane.
- **arXiv**: https://arxiv.org/abs/2610.04931

### 33. Can a System-One LLM Perform Knowledge Tracing When Few or No Learners Are Logged? (JevKT)
- **Authors**: Unggi Lee, Haeun Park
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.CY; cs.LG
- **Abstract**: Knowledge-tracing (KT) models need many logged learners, so a new course/platform starts without a model; LLM-based "System-Two" KT is slow and gives coarse probabilities.
- **Key innovations**: Off-the-shelf **System-One LLM (Jev)** reaches mean AUC 0.706 with **zero target-platform data**, beating the best of 28 deep KT models trained on 8 learners (0.689) at ~1/100 the API cost; adding a similar-learner statistic (`JevKT`) reaches 0.722 and stays ahead of deep KT up to ~64 learners. Gains are reader-specific (three other LLMs fall behind on all seven datasets) and robust to contamination checks. Interesting for cold-start user modeling.
- **arXiv**: https://arxiv.org/abs/2610.11135

### 34. Long Text to Predictive Features: LLM-Guided Blockwise Feature Engineering via Executable Program Search (LLM-BlockFE)
- **Authors**: Ziming Dai, Dabiao Ma, Ziheng Guo, Jack Dong, Zimu Zhou
- **Institution**: not stated (industry risk-control author list; unconfirmed)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: Industrial risk-control systems use structured models but leave long-text information untapped; manual feature engineering is laborious and per-input LLM calls are impractical at serving.
- **Key innovations**: `LLM-BlockFE` converts long text into **executable feature programs offline** (no LLM calls at inference), building programs by appending immutable code blocks with a block-level rollback (depth-calibrated credit) plus interleaved multi-trajectory search. +0.0069–0.0358 absolute AUC over strongest baselines on 2 public + 2 private datasets; post-launch KS gains of 0.02–1.56 pts across five deployed financial risk-control apps. The most operationally-CTR-flavored paper of the window (structured feature engineering for risk/ranking).
- **arXiv**: https://arxiv.org/abs/2610.12390

## Sequential Modeling / Time Series

### 35. Timer-M1: A Multivariate Time Series Foundation Model via Learning Primitives
- **Authors**: Haoran Zhang, Haixuan Liu, Xingjian Su, Yong Liu, Zhi Chen, Yuxuan Wang, Jianmin Wang, Mingsheng Long
- **Institution**: not stated (Tsinghua-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Cross-domain time series share elementary temporal/relational patterns ("primitives") but differ in how primitives manifest; existing foundation models struggle to generalize to complex real-world scenarios.
- **Key innovations**: Primitive-based synthesis + pretraining (temporal primitives shared across domains, relational primitives assembling multivariate samples) and episode construction with distinct channel roles (target / past-only / known-future covariates). `Timer-M1` uses gated 2D Transformer blocks allocating cross-variate attention per layer. Ranks first on **FEV and TIME** and second on GIFT-Eval among recent TSFMs — solid evidence for primitive-based pretraining for general forecasting.
- **arXiv**: https://arxiv.org/abs/2610.11734

### 36. RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting
- **Authors**: Shengsheng Lin, Jing Hu, Zhengyang Hu, Jiazheng Sun, Zichun Cao, Siwei Sun, Zhichao Zou, Enyun Yu, Dongdong Li, Xinyi Hu, Weiwei Lin
- **Institution**: not stated (data from **DiDi** marketplace; affiliation unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Ride-hailing demand forecasting faces weather, holiday, and large-event shocks; benchmarks so far miss exogenous conditioning at scale.
- **Key innovations**: `Ride-Hailing` dataset — 4 years, half-hourly, 200 spatial areas, synthesized from **DiDi** Marketplace data with three exogenous scenarios; `RideBench` evaluates **30+ methods** on week-ahead and long-horizon (up to 2,688-step) forecasting. Future-known exogenous variables clearly help, but current models still fail to capture disturbance-induced pattern changes; no model simultaneously gets low pointwise error, accurate broad trends, and reliable near-term forecasts.
- **arXiv**: https://arxiv.org/abs/2610.11164

### 37. AdaCast: Conditional Parameter Generation for Adaptive Time Series Forecasting
- **Authors**: Darahaas Nallagatla, Darryl Cherian Jacob, Pan He
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Time-series foundation models (TSFMs) adapt statically — one dataset-level update applied to every input regardless of each series' dynamics — so forecasts aren't tailored to heterogeneous inputs.
- **Key innovations**: `AdaCast` uses a **generator to produce input-specific low-rank parameter updates** for a frozen pretrained TSFM during both training and inference. Beats static adaptation in-domain across six benchmarks and improves zero-shot generalization to held-out cross-domain datasets. A parameter-generation view of conditional forecasting (echoes hypernetwork / LoRA-conditioning ideas).
- **arXiv**: https://arxiv.org/abs/2610.12240

### 38. AdaptLSTM: Efficient Adaptive Online Learning for Cloud Workload Forecasting under Distribution Drift
- **Authors**: Xinhua Miao, Bowei Yang, Zhengong Cai
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Web-scale cloud workload forecasting degrades quickly under distribution drift (viral content, launches); naive online retraining recovers accuracy at prohibitive per-step cost.
- **Key innovations**: `AdaptLSTM` detects drift via **validation-calibrated thresholds** and applies selective targeted updates. On Alibaba Machine Trace recovers 54% of Naive Online's improvement at 20% cost (2.7× efficiency); on volatile Container Trace 96% at 20% cost (4.8× efficiency, +75% MAE reduction over static). Classical drift detectors (ADWIN/DDM/P-H) fail to trigger on regression-scale error; framework is model-agnostic (LSTM/GRU/Transformer). Practical for serving-volume forecasting under shift — relevant to the wiki's ops/serving lane.
- **arXiv**: https://arxiv.org/abs/2610.12265

### 39. PulseBound: Future-Beat State Forecasting Under an Explicit Information Boundary
- **Authors**: Chenyang Xu, Donglin Xie, Xi Xiang, Xiaoyu Li, Yufan Lu, Jiqiun Gao, Yi Zhao, Xin-Yi Li, Guangpu Zhu, Zijian Wang, Xiwen Yang, Dezhen Wang, Lin Chen, Shenda Hong, Leilei Li
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Predictive representation learning from photoplethysmography (PPG) can leak future information even with causal attention (normalization, nonlocal transforms, companion views).
- **Key innovations**: `PulseBound` = physiologically structured future-beat prediction + an **explicit stored-window information boundary** (prefix-only normalization, suffix replacement before derived-view construction, aligned masking) giving stored-suffix invariance. Nine rhythm/morphology descriptors for up to 4 future beats; reduces transformed-space MAE vs persistence by 28.06% (MIMIC) / 22.22% (VitalDB) and best mean downstream performance on 16 tasks. A rigorous causal-boundary methodology that transfers to any sequential sensor modeling.
- **arXiv**: https://arxiv.org/abs/2610.12010

## Auctions / Mechanism Design / Games / Fair Allocation

*Lane note: the window contained no game-playing / board-game / strategy-game RL paper. The nearest content is auction theory and mechanism design — the theory layer under ad delivery — plus one fair-sequential-allocation result. All are fresh to the wiki.*

### 40. Protecting Losers Undermines Auction Credibility
- **Authors**: Yuta Nakamura, Noriaki Okamoto
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: econ.TH
- **Abstract**: A second-price auction must determine its price but need not learn exactly how far losing values lie below it; protecting that information from the seller conflicts with credibility.
- **Key innovations**: Deterministic private-communication protocols: lower-tail privacy forces the first informative question to reveal whether a bidder has the highest possible value, letting the seller manipulate the winner's payment undetectably (never reducing revenue). A descending protocol conceals losing values but permits manipulation; with mandatory sale, a credible *ascending* protocol reveals them. Relevant to ad-auction trust/integrity debates.
- **arXiv**: https://arxiv.org/abs/2610.12204

### 41. Payment Design under Belief Disagreement: Rent Placement, Bid Resolution, and Auction Choice
- **Authors**: Lijian Lu, Ce Zhang
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT; econ.TH; math.OC
- **Abstract**: When bidders misperceive rivals, a seller can change not just the amount of information rent but the states in which it is delivered.
- **Key innovations**: Payment design as a **linear program in nonnegative bidder rents**; a single state safely carries a report's rent when cheapest for its type and least attractive to mimics; own-type projection gives a unique optimal expected-payment rule per fixed allocation. Calibration on 1,000 eBay records shows partition-dependent reversals (first-price beats no-subsidy rules in one scenario; richer contingent rules win another). Guidance: choose interface resolution, payment dependence, and integrity tolerances jointly. Directly about auction/pricing in marketplaces.
- **arXiv**: https://arxiv.org/abs/2610.05650

### 42. Coexistence of Shill-Proof and Non-Shill-Proof Equilibria in a Public Auction
- **Authors**: Benjamin Marsh
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT; econ.TH
- **Abstract**: A single auction can have both a shill-proof equilibrium and a non-shill-proof one in the Komo-Kominers-Roughgarden model.
- **Key innovations**: Explicit single-item, three-position example with publicly observed actions, positive winning prices, and a strictly regular i.i.d. value distribution where real bidders have strict incentives in both equilibria; an initial public action flips the middle bidder's response and reverses the first shill's strict preference. Verifies both equilibria and computes expected revenues. A caution for shill-bidding defenses in ad/product marketplaces.
- **arXiv**: https://arxiv.org/abs/2610.06262

### 43. The Hardness of Dominant Strategy Mechanism Design, Revisited
- **Authors**: Frederick V. Qiu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT
- **Abstract**: Communication complexity of DSIC mechanisms for combinatorial auctions.
- **Key innovations**: Unified proof establishing `DSIC_GEN = Ω(m/γ)`, `DSIC_XOS = Ω((m/γ)^{1/5})`, `DSIC_GS = Ω((m/γ)^{1/7})` for 2^γ-communication mechanisms over m items. The **gross-substitutes lower bound answers an open question**: despite the poly-communication deterministic truthful VCG for welfare maximization, no good approximation holds for deterministic DSIC mechanisms. Also: hardness of 1.0001-approx for two weighted matroid-rank bidders vs a new φ≈1.618-approx for two submodular bidders.
- **arXiv**: https://arxiv.org/abs/2610.06773

### 44. Pessimistic Minimax Learning for Public-Private Information Games under Unilateral Coverage
- **Authors**: Shuze Daniel Liu, Claire Chen, Jiuqi Wang, David Simchi-Levi
- **Institution**: not stated (MIT-adjacent author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Offline learning in two-player zero-sum contextual games with public and private information (auctions/negotiations with private valuations).
- **Key innovations**: Introduces **unilateral prescriptive concentrability** — asymmetric information changes offline coverage through equilibrium behavior. A pessimistic algorithm achieves Õ(1/√n) exploitability (matching fully-observed minimax), and `PPA-PMD` extends to general function approximation with unified Õ(1/√n + 1/√T) rates. First theoretical framework for offline equilibrium learning under public-private information.
- **arXiv**: https://arxiv.org/abs/2610.04997

### 45. Nash Social Welfare for Multi-Armed Bandits: Trajectory-wise Expected and High Probability Regret
- **Authors**: Avishek Ghosh
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: stat.ML; cs.LG
- **Abstract**: Fair MAB under Nash Social Welfare measures performance via geometric mean of rewards, but existing "Nash regret" applies the geometric mean to per-round *marginal* expectations, ignoring the joint distribution across rounds.
- **Key innovations**: **Trajectory-wise Nash regret** (geometric mean over complete sample paths) and **high-probability Nash regret**; both are strictly stronger metrics (Jensen: trajectory-wise ≥ marginal). `RR-NCB` (round-robin exploration + Nash confidence bound index) achieves Õ(√(k log T / T)) in both, matching the optimal rate with a matching lower bound. Simulation-validated.
- **arXiv**: https://arxiv.org/abs/2610.07737

### 46. Minimizing Cumulative Envy in Allocating a Sequence of Items
- **Authors**: Paul W. Goldberg, Isaac Robinson, Nicholas Teh
- **Institution**: not stated (Oxford-adjacent author list; unconfirmed)
- **Subjects**: cs.GT; cs.MA
- **Abstract**: Temporal fair division of indivisible goods arriving sequentially and allocated irrevocably, with valuations and future arrivals known in advance.
- **Key innovations**: Defines **cumulative maximum envy** (area under the worst-envy curve — magnitude *and* duration). Hardness: minimizing it is strongly NP-complete with no constant-factor approximation (even identical/binary valuations); a dynamic program gives pseudopolynomial solutions for constant agents, plus FPTAS for fixed n / identical integer valuations. Sequencing variant: NP-complete even for two agents, but greedy gives 3/2-approx (n=2) and n/(n−1)-approx generally. Feeds the wiki's fairness/feed-allocation thread.
- **arXiv**: https://arxiv.org/abs/2610.09843

### 47. Asymptotically Optimal Public Project Redistribution without Bounded Precision: A Complex-Analytic Proof
- **Authors**: Mingyu Guo
- **Institution**: not stated (University of Adelaide-adjacent author list; unconfirmed)
- **Subjects**: cs.GT
- **Abstract**: Worst-case VCG redistribution for the public project problem; prior work could approach a 1-efficiency ratio only under a bounded-precision (rational types) assumption, with best-known guarantee otherwise ~1/2.
- **Key innovations**: Removes the assumption with a deterministic, anonymous, strategy-proof, deficit-free mechanism for arbitrary real types in [0,1] with worst-case efficiency **1 − O(1/log log n)**. Construction: iterative estimation ("estimate the shortfall, then the error, then the error of the error..."), proven via a trigonometric representation + **Poisson–Jensen inequality** — a rare complex-analysis argument in mechanism design.
- **arXiv**: https://arxiv.org/abs/2610.10995

## Notes
- **Harvest window**: primary category sweep = 2026-10-08 announcement (480 unique entries: cs.AI 237, cs.LG 230, cs.CL 119, cs.IR 16, cs.GT 8); topical `abs:` sweeps 2026-10-04 → 2026-10-09 for the recsys/ads/games lanes. 47 papers featured; **all 47 grep-verified new to the wiki** (0-hit against a 6,960-ID repo-wide baseline).
- **API state**: no 2026-10-09 or 2026-10-10 announcements were indexed at run time (Sat 2026-10-10 ~10:00); the 2026-10-08 batch is the latest available. No HTTP 429/rate-limiting occurred this run.
- **Coverage gaps (explicit)**: zero classical CTR-prediction / ad-serving / generative-recommendation papers in the window — the 10-08 batch is dominated by agent work, reasoning/RL, and efficiency; the recsys/ads/games lanes were filled only via the wider topical sweep and are dominated by **auction/mechanism theory**, retrieval, and one industrial bandit (§32). No game-playing RL paper exists in-window; the games parenthetical in this digest's brief is therefore served by mechanism-design theory. This extends the "no new CTR architecture" observation from the 2026-10-07/09 digests — [[ctr-scaling-landscape]] (GRAB, LoopCTR, EST, CADET) again gains no entrant.
- **Recurring arcs**: (1) agent governance layer — memory admission/presentation (§2), policy-compiled tool gates (§1), epistemic humility (§6), no-thinking as a first-class capability (§3); (2) decoding/efficiency — KV rehearsal (§23), decoding-aware pruning (§19), speculative trees (§20), sparse-attention GPU scheduling (§18), 4-bit optimizer states (§22); (3) unlearning is now an active ML problem with minimax and recoverable-drift results (§7–8); (4) theory catching up to deep nonlinearity — monotone compression (§4), small-world connectivity (§5), attention-nonlinearity depth scaling (§17), Gaussian-mixture softmax (§16); (5) personalization migrating into parametric memory and agent RAG (§30–31).
- **Institution data**: arXiv metadata omits affiliations; institution fields above are best-effort and marked unconfirmed where inferred from author groups/code links. A follow-up could enrich from Semantic Scholar / OpenAlex / paper PDFs.
- **Cross-links**: concepts touched match wiki threads on [[agent memory]], agent harness/governance, test-time compute, time-series foundation models, auction/mechanism design, and CTR-scaling (no new entrant). Left as conceptual references; no wiki pages were created or edited for this digest.