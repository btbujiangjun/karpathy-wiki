---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-15
updated: 2026-09-15
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, game-AI, agents, MoE-routing, KV-cache, RL, evaluation, security]
---

# arXiv AI Research Paper Search Report — 2026-09-15

Generated: 2026-09-15 (Tuesday). Fresh window = the **latest announced mailing** beyond yesterday's 09-14 reports (IDs ~2609.132xx–2609.159xx; citation_online_date Sep 11–14; the "Mon 14 Sep 2026" per-category listing pages plus the newly-probed 132xx–159xx frontier). All 22 featured papers verified **0 hits in `wiki/`** at grep-verification time.

**Methodology**: The public arXiv API (`export.arxiv.org`) returned hard `Rate exceeded.` throughout this run (the 10:00–11:00 sibling scheduled jobs — arxiv-daily / arxiv-paper-check / conference-digest / game-rl-daily — were consuming the shared quota and stayed "running" without emitting any 09-15 files). Fallback: direct page fetch of arXiv `/list/{cat}/new` and ~700 targeted `abs/{id}` probes sweeping IDs 2609.13200–2609.15996 (plus abs pages for a seeding shortlist). Probe HTML was cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and cleaned up after. Every featured ID below was grep-verified **0 hits in `wiki/`** at selection time.

**Dedup notice**: IDs 2609.132xx–2609.159xx lie entirely **above** the max ID (2609.13144) covered by the 09-14 arxiv-ai-search / arxiv-daily / arxiv-paper-check / conference-digest / game-rl-daily reports, so the whole featured set is beyond their windows by construction. Same-day sibling reports (09-15) are not yet on disk (scheduled runs rate-limited); cross-references at the bottom record the coordinates.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | IDs 2609.13200–2609.15996 (online dates 2026-09-11 → 09-14); frontier checked = no records at ≥ 2609.16000 |
| IDs probed | ~700 page fetches; ~640 existing records screened by subject/title |
| Fresh beyond yesterday's max (2609.13144) | entire window |
| Featured in full in this report | 22 |
| Direct CTR / advertising papers | **0** (see ADS/CTR note) |
| Recommendation-adjacent | 1 direct (A1) + 2 rec-adjacent (A-runner-up RA-CoA, agentic-search-citation §9.3) |

**Advertising/CTR note**: Like the last several windows, the fresh 132xx–159xx range contains **no direct CTR or advertising papers** (closest: process-mining recommendation A1, fashion-caption RA-CoA runner-up). Re-consolidates the "daily arXiv noise-floor" pattern for CTR/ads we have logged since late Aug.

---

## 1 Recommender Systems & Online-Adjacent Tradecraft

### 1.1 Complete Suffix Prediction for Recommendation via Latent Retrieval over Process Graphs (2609.15692)
- **Title**: Complete Suffix Prediction for Recommendation via Latent Retrieval over Process Graphs
- **Authors**: Sarra Madad, Myriam Maumy, Frédéric Bertrand, Yoann Valero
- **Institution**: Université de Strasbourg (process mining / statistics group; tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15692
- **Abstract**: Complete suffix prediction in sequential decision settings is hard because a single prefix can stay compatible with several plausible suffixes. Proposes a graph-based metric-learning framework that **reformulates complete suffix prediction as latent retrieval over process graphs**: prefixes and suffixes become directed attributed graphs encoded by edge-conditioned GNNs, jointly modeling event-level activities and transition-level durations. Prefix representations are projected into the latent suffix space by a predictor trained with a joint reconstruction + contrastive objective strengthened with process-aware hard negatives; spectral normalization enforces a Lipschitz constraint on both encoders and the predictor. On two real-life process datasets it achieves the best overall results across nearly all criteria — semantic suffix accuracy via normalized Damerau-Levenshtein, Recall@1/@5, MRR@5, and temporal plausibility (MAE).
- **Key Innovations**: (1) first graph-based *latent retrieval* framing of complete suffix prediction (vs pure sequence decoding); (2) joint activity+duration modeling with process-aware hard negatives; (3) Lipschitz-constrained retrieval geometry for recommendation-oriented process monitoring.
- **Venue**: Preprint.

---

## 2 Sequential Modeling, Linear Attention & Context Extension

### 2.1 SpectralShift — Context Window Extension of Gated DeltaNet by Spectral Reparameterization (2609.14320)
- **Title**: SpectralShift: Effective Context Window Extension of Gated DeltaNet via Spectral Reparameterization
- **Authors**: Zian Liu, Yiwen Hu, Zican Dong, Tian Xie, Wayne Xin Zhao, Yucheng Ding, Ran Tao, Bryan Dai
- **Institution**: Renmin University of China-affiliated (tentative)
- **Date**: Announced 12 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14320
- **Abstract**: Linear-attention layers are increasingly replacing softmax attention for long-context modeling, but existing context-extension recipes continue-pretrain without touching the layer, ignoring the **spectral properties of the linear-attention state transition matrix**. Studying Gated DeltaNet (GDN) long-context extension from the spectral perspective, identifies two factors governing long-range retrieval: (1) a **broad slow spectral band** aligned with the target dependency length, and (2) preservation of **fast-decaying modes** for state clearing / context switching. **SpectralShift** reparameterizes the α-projection **initialization** to reshape the decay spectrum toward slow propagation, and adds learning-rate scaling on α-projections for stable long-context training. Consistently improves long-context capability over continued pretraining; code open-sourced.
- **Key Innovations**: (1) spectral (transition-matrix) view of linear-attention context extension, not just data; (2) initialization+LR reparameterization (no architecture change); (3) explicit slow/fast band duality (long-range retrieval vs state clearing).
- **Venue**: Preprint.

### 2.2 One Spectrum, Two Resources — Data-Memory Scaling in Autoregressive Prediction (2609.13500)
- **Title**: One Spectrum, Two Resources: Data-Memory Scaling in Autoregressive Prediction
- **Authors**: Chiwun Yang, Xiaoyu Li
- **Institution**: — (not specified; 66-page theory paper)
- **Date**: Announced 11 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.13500
- **Abstract**: How much learned memory is needed to benefit from more data? Shows the two resources are governed by **one predictive-energy spectrum** in a positive-entropy autoregressive retrieval source: each coordinate contributes query probability × squared radius of its unknown logit. Proves the minimax law `R*_value(n,B) ≈ Φ_μ(n⁻¹)+Φ_μ(τ_B)` over n prediction blocks and a learned state with ≤ 2^B values: **data sets resolution 1/n; memory sets the level τ_B from optimal bit allocation**. Energy-dimension pairing is essential (two causal sources with identical block energy/dimension marginals get different exponents). A masked query-key attention head realizes the law with explicit routing/format/arithmetic errors; further results cover exponent-adaptive allocation, finite-precision realization, and compute-precision laws. Experiments recover the data-memory collapse and coupling exponents, examine weight-only quantization across six pretrained model scales.
- **Key Innovations**: (1) unified predictive-energy spectrum linking data and memory scaling; (2) minimax law with matching implementation (attention head) and mechanism (routing + allocation); (3) connects scaling-law analysis to weight-only quantization behavior.
- **Venue**: Preprint.

---

## 3 LLM Agents: Discovery, Search, Memory & Handoffs

### 3.1 AlgoEvo — Self-Evolving Agentic Search for Automated Algorithm Discovery (2609.15820)
- **Title**: AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery
- **Authors**: Junhao Qiu, Qinglong Hu, Xialiang Tong, Mingxuan Yuan, Liyong Lin, Qingfu Zhang
- **Institution**: Huawei Noah's Ark Lab-affiliated / CityU (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15820
- **Abstract**: LLMs have automated algorithm discovery by synthesizing executable code, but existing frameworks trap them in rigid search pipelines with predefined control flows, blocking adaptive reasoning, cross-paradigm transfer, and execution-feedback reuse. **AlgoEvo** turns algorithm discovery into an interactive, knowledge-accumulating agentic process: an autonomous agent inspects/diagnoses/edits code from runtime feedback; a **design skill hub** decouples paradigm-specific knowledge from the core engine (single-/multi-objective and multi-component design in one workflow); a **hierarchical experience mechanism** organizes trajectories into a task-level tree and consolidates cross-task patterns into reusable skills. Across six benchmark tasks it matches or beats specialized methods with substantially fewer evaluations/tokens, showing intra-task accumulation, cross-task transfer, and skill-activated reproduction of SOTA.
- **Key Innovations**: (1) self-evolving agentic loop with runtime-feedback diagnosis (vs rigid search pipelines); (2) skill-hub decoupling for multi-objective/multi-component design; (3) hierarchical experience reuse for cross-task transfer.
- **Venue**: Preprint.

### 3.2 Question's Gambit — The First Move Matters in Agentic Deep Search (2609.14412)
- **Title**: Question's Gambit: The First Move Matters in Agentic Deep Research
- **Authors**: Radin Hamidi Rad, Amin Bigdeli, Negar Arabzadeh, Sajad Ebrahimi, Charles L. A. Clarke, Benjamin C. M. Fung, Ebrahim Bagheri
- **Institution**: Toronto Metropolitan / Waterloo / McGill (Canadian academia; tentative)
- **Date**: Announced 13 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14412
- **Abstract**: Deep-research agents answer complex questions via iterative search-read-reason loops; on BrowseComp-Plus, well-configured lexical retrieval surfaces evidence but agents still fail to connect evidence documents to gold documents. Identifies the **first retrieval move** as a decisive design point and introduces **Question's Gambit**: a first-move retrieval module that decomposes the question into clues, reformulates them into complementary searches, consolidates results, and reranks the candidate pool before the iterative loop begins — producing an opening context for both clue aggregation and final-answer verification. On BrowseComp-Plus it raises answer accuracy from 83.1% to **90.5%** over Pi-Serini (strongest reported agentic baseline), and transfers to MultiHop-RAG.
- **Key Innovations**: (1) first-move retrieval as a first-class design decision for deep research agents; (2) clue decomposition → complementary search → consolidated rerank "opening"; (3) +7.4 pp over a state-of-the-art agentic baseline (reported with public implementation).
- **Venue**: Preprint.

### 3.3 AgentKV — Phase-Aware KV Eviction for Agentic LLMs (2609.14872)
- **Title**: AgentKV: Phase-Aware KV Eviction for Agentic LLMs
- **Authors**: Taowen Tony Liu, Jeffrey T. H. Wong, Can Xiao, Bowen Yang, Hao Mark Chen, Yiren Zhao
- **Institution**: Canadian academia / industry (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14872
- **Abstract**: Agentic serving consumes orders of magnitude more tokens than chatbots, stressing KV capacity and decode bandwidth. Existing KV-eviction scores keys against representative queries from the **most recent tokens**, assuming future attention resembles recent attention; agentic generation violates this — future queries form a **mixture over think/act/tool/other phases**, and principal-angle analysis shows these components occupy measurably different query subspaces, so recency representatives systematically undervalue keys upcoming phases need. **AgentKV** keeps a small query buffer per phase and scores keys against their union, then compacts retained KV pages online across turns (persistent multi-turn serving). Across two models, six task domains, three KV budgets: +5.5 pts over R-KV, +5.3 over Tri-attention, and up to **1.80×** output-token throughput vs upstream full-KV SGLang.
- **Key Innovations**: (1) phase/subspace analysis explaining why recency-aware eviction fails for agents; (2) per-phase query-buffer scoring; (3) persistent cross-turn KV compaction in a real serving path.
- **Venue**: Preprint.

### 3.4 Do Not Restart — Residual Completion for Stateful Agent Handoffs (2609.13800)
- **Title**: Do Not Restart: Residual Completion for Stateful Agent Handoffs
- **Authors**: Runzhi Deng, Yiming Zhong, Fang Zhao, Pan Zhou
- **Institution**: Chinese academia (tentative)
- **Date**: Announced 12 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.13800
- **Abstract**: Routing/cascade systems transfer control across models to cut cost, but **stateful handoffs** must preserve accepted choices, realized effects, and unfinished obligations. Formulates this as **commitment-constrained residual completion** and introduces CFRC (Commitment-Frontier Residual Completion): enforces target-before-proposal, whole-proposal-before-authority, live-evidence-before-success — freezing a residual contract from accepted progress, closing the successor continuation into an evidence-linked graph, and admitting execution only when the remainder is covered (live receipts discharge obligations). Establishes contract-relative partial correctness. Across five environments and two same-provider model pairs: comparable macro-accuracy to strong full-task agents at **22.0–34.6% of their inference cost**, with extra cross-provider transfer results.
- **Key Innovations**: (1) commitment-based formalization of stateful handoffs (vs start-from-scratch); (2) evidence-linked contract graph with live receipts; (3) ~¼-⅓ cost at matched accuracy.
- **Venue**: Preprint.

### 3.5 Recoverability as a System Primitive for Long-Horizon Agents (2609.13672)
- **Title**: Recoverability as a System Primitive for Long-Horizon AI Agents
- **Authors**: Zhihui Zhang, Wei Liu
- **Institution**: Chinese academia (tentative)
- **Date**: Announced 12 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.13672
- **Abstract**: Agents can be interrupted mid-file-edit / tool-call / multi-step task; restarting repeats work, continuing from unverified progress propagates errors, and a saved state is not necessarily a resume point. Introduces **recoverability as a system primitive** that makes reuse an explicit decision: select a supported starting point + permitted recovery action, or withhold automatic continuation. A behavioral contract binds the choice to supporting evidence, execution, and independent checks; a reference architecture separates persistence/validation/control. Four deterministic + 20 paired file challenges show accurate restoration *and* successful completion can conceal disallowed starting points; event-time tests show permission must also constrain the action, and independently held policy evidence can expose violations post-effect. Argues recovery decisions need their own evaluation, beyond restored bytes and final task success.
- **Key Innovations**: (1) recovery (not just checkpointing) elevated to first-class evaluation + system primitive; (2) behavioral contract tying resume point to evidence/checks; (3) failure cases where "restored + succeeded" still violates policy.
- **Venue**: Preprint.

---

## 4 Evaluation, Judges & Agentic Benchmarks

### 4.1 When Consistency Does Not Mean Reliability — Local LLM Judges vs Human Ratings (2609.13824)
- **Title**: When Consistency Does Not Mean Reliability: Evaluating Local LLM Judges Against Human Ratings
- **Authors**: Aakash Kumar Tiwari
- **Institution**: — (single author)
- **Date**: Announced 12 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.13824
- **Abstract**: LLM-as-a-judge is faster/cheaper than human eval, but a judge may be consistent while disagreeing with humans. Evaluates two local open-weight judges (LLaMA-3-8B, Qwen2.5-7B) on 300 responses from an instruction-tuned GPT-2 (124M) across 100 questions / five categories, scored by nine human annotators and three judge runs each. LLaMA-3-8B Pearson r = 0.275, Qwen2.5-7B r = 0.340 with humans; MAE 27.71 / 18.64 — yet both show high self-consistency (exact-match 97.3% / 92.3%). Conclusion: high self-consistency does **not** imply agreement with humans; local judges need both consistency *and* human-alignment evaluation.
- **Key Innovations**: (1) controlled head-to-head of judge self-consistency vs human agreement on a small affordable testbed; (2) quantifies the consistency-reliability gap for local open-weight judges; (3) concrete protocol (Pearson/Spearman, MAE, signed bias) for judge audits.
- **Venue**: Preprint.

### 4.2 MTAC-IFBench — Instruction-Following in Multi-Turn Agentic Coding (2609.14992)
- **Title**: MTAC-IFBench: Benchmarking Instruction-Following in Multi-Turn Agentic Coding
- **Authors**: Bosi Wen, Cunxiang Wang, Jiayi Gui, Haoke Zhang, Yilin Niu, Pei Ke, Dayong Yang, Hongning Wang, Minlie Huang
- **Institution**: Tsinghua University / University of Virginia-aligned (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14992
- **Abstract**: Code agents must follow **process instructions and constraints**, not just hit functional correctness, but benchmarks focus on final correctness or single-turn IF in chat/simple code gen. **MTAC-IFBench** targets multi-turn agentic coding IF: multi-turn progressive development instructions with diverse constraints across 6 primary / 18 secondary categories, averaging **7.04 turns and 91.33 constraints per instance**. Each constraint/functional requirement gets a checklist verified by scripts + judge agents. Finds significant deficiencies: agent IF performance degrades rapidly as sessions grow longer.
- **Key Innovations**: (1) first dedicated multi-turn agentic-coding IF benchmark; (2) checklist + scripted/judge verification for reliability; (3) documents capability decay over long sessions.
- **Venue**: Preprint.

### 4.3 Policy Loopholes in Agent Evaluation (2609.14400)
- **Title**: Policy Loopholes in Agent Evaluation: When Policy Ambiguity Masquerades as Agent Error
- **Authors**: Hongliu Cao
- **Institution**: — (single author)
- **Date**: Announced 13 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14400
- **Abstract**: Agent benchmarks assume each policy determines a unique correct action, but natural-language policies can violate this via **silence, ambiguity, or contradiction** (multiple defensible readings a single gold trajectory can't capture). Auditing two τ²-bench domains: a taxonomy of policy loopholes; affected tasks produce unreliable scores — lowering scores differently across models and reducing per-model consistency. Exploitability requires **both policy ambiguity and tool permissiveness**; when policy complexity exceeds what tools enforce, agents resolve gaps inconsistently. Policy specification quality sets the ceiling on evaluation quality — audit policies *before* collecting gold annotations.
- **Key Innovations**: (1) taxonomy of policy loopholes (silence/ambiguity/contradiction) in agent eval; (2) evidence that loopholes corrupt cross-model comparability + consistency; (3) actionable pre-gold-audit recommendation.
- **Venue**: Accepted at **REALM EMNLP 2026**.

---

## 5 RL & Alignment

### 5.1 What Does an LLM Learn from RL? — Fixed-SAE Representation Tracking (2609.15064)
- **Title**: What Does an LLM Learn from Reinforcement Learning? A Mechanistic Interpretability Perspective with Fixed-SAE Track
- **Authors**: Lingheng Du, Yiming Tang, Xufeng Duan, Dianbo Liu
- **Institution**: CUHK-aligned / Shanghai AI research (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15064
- **Abstract**: RL improves targeted LLM capabilities, but *what it changes at the representation level* is unclear (novel features? enhanced/suppressed existing ones?). Prior work is behavioral. **Fixed-SAE Track** trains one shared SAE per layer over activations pooled across base + all RL checkpoints, holding every feature direction fixed so representation shifts are rigorously defined (including detection of emerging novel features). Across datasets and RL algorithms: RL-induced drift is **small, gradual, concept-specific, concentrated in late layers**, mainly enhancing sampling of a small set of ladder tokens and formatting scaffolding (step breaks, answer delimiters) rather than reshaping problem content. **Steering these features into the base model recovers ~80% of RL's performance gain** — RL mostly elicits capabilities the model already has. A synthetic benchmark (features known by construction) tests whether RL can instill genuinely novel features.
- **Key Innovations**: (1) Fixed-SAE methodology to track representation change across checkpoints; (2) finding that RL ≒ steering toward existing latents (~80% gain recapitulated); (3) synthetic-feature benchmark for testing novel-feature creation.
- **Venue**: Preprint.

### 5.2 Forty Shades of Blue — Quality-Diversity Alignment via Mode-Conditioned RL (2609.14896)
- **Title**: Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning
- **Authors**: Jiayi Yuan, Hangoo Kang, James Jihao Liu, Yejin Choi, Vikram Iyer, Liwei Jiang, Natasha Jaques
- **Institution**: UW / MIT-aligned (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14896
- **Abstract**: Alignment training causes **mode collapse** — a progressive loss of output diversity — limiting open-ended exploration and pluralistic outputs (scientific ideation, creative writing). **MoDA (Mode-conditioned Diversity Alignment)**: online post-training RL that jointly optimizes quality and diversity by conditioning a single shared policy on **abstract numbered roles**, each role acting like a MARL agent competing for outputs distinct from the others (no hand-crafted personas or architecture changes). A **prompt-adaptive quality gate** calibrates a reference quality threshold and grants diversity reward only to threshold-passing responses (anti reward-hacking). On a suite of 7 general capability + 4 diversity tasks: **+265% SBERT diversity** on Infinite-Chat held-out prompts while raising average pass@1 by 10.3% over the Qwen3-8B baseline; vs strongest DivPO baseline diversity 0.274→0.482 (+75.9%) and E-Vendi 2.86→4.4 (+53.8%), pass@1 +7.0%.
- **Key Innovations**: (1) diversity conditioned on latent roles via shared policy (MARL-inspired); (2) prompt-adaptive quality gating against reward hacking; (3) quality-diversity gains without personas/architecture changes — drop-in to post-training.
- **Venue**: Preprint.

---

## 6 Reasoning & Efficiency Frontiers

### 6.1 Lightning Weave — Capability Composition for Reasoning Models (2609.14708)
- **Title**: Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models through Capability Composition
- **Authors**: Yecheng Wu, Song Han, Han Cai
- **Institution**: MIT-aligned (tentative)
- **Date**: Announced 13 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14708
- **Abstract**: Efficient-reasoning goal: improve accuracy while using fewer tokens — but the two objectives favor different reasoning behaviors, and independently post-trained models already own distinct accuracy vs efficiency strengths. **Lightning Weave** composes these independently learned capabilities in a single student via **on-policy distillation**: each capability = the policy shift from base model to specialist; the framework combines aligned log-ratio shifts at shared token states and uses **Tilted-Target DOPD** to turn cached signals into a stable learning target. Anchor pairs score each trajectory once, so training runs without serving multiple live anchors. On math+code, e.g. Qwen3.5-4B: HMMT 2025 59.2→64.0% with 10.7% fewer response tokens; LiveCodeBench v5 41.7→54.2% with 9.6% fewer tokens; adjusting anchor strengths yields a strong empirical accuracy-efficiency Pareto frontier.
- **Key Innovations**: (1) composing pre-existing specialist capabilities (accuracy + efficiency) into one student; (2) single-pass scoring of anchor trajectories; (3) explicit Pareto control over accuracy-efficiency tradeoff.
- **Venue**: Preprint (work in progress).

### 6.2 When Does a Scaling Result Justify a Different Allocation? (2609.14500)
- **Title**: When does a scaling result justify a different allocation? A critical review of resource-allocation evidence for AI systems
- **Authors**: Seyed Morteza Emadi
- **Institution**: — (independent; 35pp critical review)
- **Date**: Announced 13 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14500
- **Abstract**: AI scaling studies increasingly evaluate systems combining a pretrained model with retrieval, search, verification, tools, and interaction — but a higher score under a larger budget does **not** by itself show where extra resources should go. Critical integrative review asking when a reported scaling result supports an allocation decision, comparing evidence across pretraining, test-time compute, retrieval, and agent evaluation. Distinguishes *performance of the tested procedure* from *best achievable under a resource limit*, and identifies three recurring mismatches: success counted before an answer is chosen; information a deployed system won't have; costs left out. A **capability surface** expresses performance as a function of budgets/mechanisms/information; worked analytical examples show how the evaluation metric, deployment volume, selection rule, and stopping policy can flip an allocation conclusion. A **resource envelope** records task, development/runtime resources, information access, and procedure per reported score, applied to a published comparison.
- **Key Innovations**: (1) allocation-evidence lens separating procedure performance from budget-constrained best; (2) taxonomy of the three recurring evidence mismatches; (3) reusable capability-surface / resource-envelope reporting framework.
- **Venue**: Preprint.

---

## 7 Inference Efficiency: Depth & Compression

### 7.1 One Size Does Not Fit All — Inference Depth Set by Deployed Traffic (2609.14144)
- **Title**: One Size Does Not Fit All: Setting Inference Depth from the Questions a Deployment Actually Asks
- **Authors**: Jerry Kaplan
- **Institution**: — (single author)
- **Date**: Announced 12 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14144
- **Abstract**: A transformer pays the same compute per token in every deployment, but each deployment asks a narrow range of questions. Measures how much cost is avoidable via **early exit**: a trained readout attached to an intermediate layer proposes tokens, and a confidence test decides early-emission. Three findings: (1) savings depend strongly on traffic type — at half depth on a 1.5B model, 96% of tokens could be emitted early for arithmetic word problems vs 8% for Chinese explanations at matched token fidelity; (2) of three ways to exploit knowledge, **only per-deployment threshold calibration** pays (up to +59 pp exit rate across three models); (3) token-level fidelity — the field's standard metric — **fails where tokens can be ground-truthed**: on arithmetic word problems, three models answer 60/60 in full but only 10–28 correct under early exit even in the highest-fidelity configuration. Intended setting: small models on personal devices (memory-bandwidth-bound).
- **Key Innovations**: (1) deployment-aware (traffic-conditioned) early exit; (2) negative result: token-fidelity underestimates early-exit accuracy loss; (3) threshold calibration as the only reliable deployment knob.
- **Venue**: Preprint.

### 7.2 Per-Matrix Optimality Is Not Enough — Three-Level Low-Rank LLM Compression (2609.15838)
- **Title**: Per-Matrix Optimality Is Not Enough: Three-Level Optimization for Low-Rank LLM Compression
- **Authors**: Huicheng Zhang, Xiyao Feng, Ze-Tong Li, Chengkai Zhu, Xiao Shi, Xiwei Pan, Jinguo Liu, Ge Bai, Xin Wang
- **Institution**: Alibaba-affiliated (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15838
- **Abstract**: Per-matrix SVD truncation is Eckart–Young optimal in whitened Frobenius norm, but independently compressed matrices' errors compound through the block's nonlinear forward pass. Introduces a **three-level chain** (inspired by hierarchical variational optimization in quantum many-body physics): whitened SVD (L1) → **block-level joint optimization (L2)** → end-to-end LM-loss refinement (L3), all from **256 calibration sequences** with no instruction/recovery data. On LLaMA-7B at 60% compression, WikiText-2 PPL drops 42.1 → 19.1 → 11.4 along the chain. The block-level stage acts as a regularizer: skipping it worsens PTB PPL by 24 pts, not closed by extra end-to-end training. Gains hold 20–80% compression across five architectures up to 13B. With more calibration data, skipping L2 becomes competitive — an offline compute↔data tradeoff. Claims only PPL/compression-fidelity gains; downstream accuracy stays below the dense model.
- **Key Innovations**: (1) cross-matrix error propagation as a first-class problem vs naive per-matrix SVD; (2) three-level hierarchical optimization from 256 sequences; (3) demonstrates a data-vs-block-opt compute tradeoff.
- **Venue**: **EMNLP 2026 Findings**.

---

## 8 Skill Routing & Frozen-LLM Inference

### 8.1 The Router Within — Reading Native Skill Routing from a Frozen LLM (2609.15982)
- **Title**: The Router Within: Eliciting Native Skill Routing from a Frozen LLM
- **Authors**: Ruishuo Chen, Xun Wang, Yu Chen, Zhuoran Li, Longbo Huang
- **Institution**: Tsinghua University-aligned (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15982
- **Abstract**: Skills extend an LLM agent beyond parametric knowledge, but deployments route by preloading every skill's metadata into context (disperses attention, caps library size) or by external retrieval (moves selection outside the agent's capability). Shows the **frozen agent LLM already carries routing signal in its own forward passes**, and two linear maps suffice to read it out with no skill text in context. **Gavel** (Glance And Verdict): a *glance* projects task and skill mid-layer states through the two trained maps and scores the library against compact per-skill banks built in one forward pass at installation; a *verdict* resumes shortlisted skills' forward passes, reading the model's own likelihood + yes/no judgment fused via product-of-experts. Trained once, transfers zero-shot to three public benchmarks + SkillTraj (new benchmark, 372 simulated agent trajectories). On Qwen3-32B beats progressive-disclosure and retrieve-and-rerank pipelines (which add 1.2B–16B external params) by up to **+13.4 points** on written tasks, **+21.9** when skill need arises mid-rollout; the same 32B triggers correct skills on Skill-Use more often than far larger frontier models in Codex, in a bash-agent harness.
- **Key Innovations**: (1) routing signal read directly from frozen LLM internals (no skill text in context, no external router); (2) glance+verdict two-step with product-of-experts fusion; (3) zero-shot transfer + SkillTraj benchmark.
- **Venue**: Preprint.

---

## 9 Security, Trust & Citation Integrity

### 9.1 AGENTQ — Quantization-Conditioned Backdoor Attacks on LLM Agents (2609.14060)
- **Title**: AGENTQ: Quantization-Conditioned Backdoor Attacks on LLM Agents
- **Authors**: Xiaoqun Liu, Qiben Yan
- **Institution**: US university (Nebraska-Lincoln-adjacent; tentative)
- **Date**: Announced 12 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.14060
- **Abstract**: Quantization is a default deployment path for open-weight LLM agents but is not behavior-preserving: an adversary can ship a full-precision checkpoint that passes audits yet misbehaves once quantized (**quantization-conditioned attack, QCA**). Prior QCA targets free-text where harm passes through a human reader; in the **agentic** setting the triggered payload is a structured, executable function run without human oversight. Directly adapting prior backdoor methods yields post-quantization malice but cratered benign utility. **AGENTQ** combines **layer-banded LoRA injection** with **partial-PGD repair over a multi-codebook quantization-equivalence class**, preserving normal agentic capability while concentrating malice in the quantized model. Across three trigger-action pairs and three codebooks (NF4/FP4/INT8): up to **100% post-quantization attack success** with minimal benign-utility loss — argues quantization-aware safety evaluation should be standard before open-weight agent deployment.
- **Key Innovations**: (1) first quantization-conditioned backdoor study for LLM **agents**; (2) utility-preserving injection + quantization-equivalence-class PGD repair; (3) practical codebook-agnostic takeaway (NF4/FP4/INT8 alike).
- **Venue**: **EMNLP 2026**.

### 9.2 CiteShade — Citation Laundering in Multi-Source RAG (2609.15660)
- **Title**: CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation and Its Counterfactual Defense
- **Authors**: Guo Fuzheng
- **Institution**: — (single author)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15660
- **Abstract**: RAG grounds answers on retrieved knowledge and returns citations as the user's audit trail. Prior RAG security asks whether an attacker can corrupt the *answer*, leaving the **citation channel** unexplored. **CiteShade** is the first citation-laundering attack: an attacker controlling a single source induces the model to produce a wrong attacker-chosen answer **attributed to a trusted source that doesn't support it**, while correct evidence stays in context. Formulated as an optimization, with three necessary conditions (retrieval, generation, citation), on multi-source multi-hop QA the attack raises wrong-answer rate 0.01→**0.68**; source deletion confirms the malicious source is the causal driver in every measured case. Vulnerability tracks a model's *propensity to cite* rather than scale (CLR 0.84 with explicit instruction, 0.64 with none). Perplexity filtering and citation-support checks each insufficient; proposes a **counterfactual defense** verifying which source actually drove the answer.
- **Key Innovations**: (1) first attack on the citation/attribution channel of RAG; (2) verifiable optimization with explicit retrieval/generation/citation conditions; (3) counterfactual (source-deletion) defense.
- **Venue**: Preprint.

### 9.3 CITECHOICE — Causal Audit of Citation Credit in Agentic Search (2609.15164)
- **Title**: CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search
- **Authors**: Sriram Selvam, Anneswa Ghosh
- **Institution**: — (industry, tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15164
- **Abstract**: When several sources support the same claim, an answer engine cites some but not others — **citation allocation**, unstudied causally. From 129 everyday-query transcripts, CITECHOICE selects 113 same-call document pairs with independently verified support for the same fact (blinded human review confirms 103), then runs a hash-verified 2×2 replay crossing pair order with jointly generated structural-vs-prose renderings. Results: (1) **structured rendering concentrates citation credit** (+0.50 citations/answer on target, Holm-adjusted p=.033) without raising total citations or cutting competitors; incidence effect +4.5pp inconclusive. (2) Observational rank effects dwarf controlled reordering: citation-rate gap rank1→rank5 = 42.3pp vs +7.9pp in the main replay. (3) Evaluation has a noise floor: ~15% of binary decisions change under fresh decoding; decoding explains ~45% of single-generation variance. Conclusion is narrow and honest: presentation causally redistributes *visible* credit within frozen transcripts; it does **not** establish reliable source admission or a pure formatting mechanism.
- **Key Innovations**: (1) first causal audit of citation allocation in agentic/answer-engine search; (2) replay design isolating presentation/order confounds; (3) quantifies the decoding noise floor of citation metrics.
- **Venue**: Preprint.

---

## 10 Game Theory & Participatory Design

### 10.1 Core-Up-To-One for Participatory Budgeting (2609.15928)
- **Title**: Core Up-To-One for Participatory Budgeting with Additive Utilities
- **Authors**: Piotr Skowron
- **Institution**: University of Warsaw (tentative)
- **Date**: Announced 14 Sep 2026 (online)
- **arXiv**: https://arxiv.org/abs/2609.15928
- **Abstract**: Studies **participatory budgeting with additive utilities** (citizens vote over projects under a cost constraint) and introduces a selection rule based on **utility-weighted harmonic entropy plus a cost penalty**, proving it returns budget-feasible outcomes satisfying **core-up-to-one** — the classic proportionality guarantee that every group of like-minded agents receives its fair share up to a single additional project. Places the result in the budget-additive core literature (core-up-to-one is the strongest proportionality notion known achievable in this setting).
- **Key Innovations**: (1) new harmonic-entropy + cost-penalty rule for PB; (2) formal core-up-to-one guarantee for additive utilities; (3) advances the proportional-aggregation line relevant to public-resource and ad-budget allocation analogies.
- **Venue**: Preprint.

---

## Key Trends Across This Window

1. **Agentic compute is being measured at every layer** (AlgoEvo, Question's Gambit, AgentKV, CFRC, Recoverability): first-move retrieval design (+7.4pp), phase-aware KV scoring (1.8× throughput), stateful-handoff residual completion at ¼–⅓ cost, and recovery-as-a-primitive — evaluation is shifting from "can the agent finish" to "how much of the work is obligated, reusable, and recoverable."
2. **Frozen-LLM introspection as an efficiency lever** (The Router Within recursive loop → Gavel lines up with the loop-scaling/residual-stream threads in 08-17 checks): routing signal and skill selection can be read from the same forward passes the agent already runs, beating external 1.2B–16B routers by up to ~22 pts.
3. **Scaling-law and eval evidence is being audited for decision validity** (14500 critical review, 14400 policy loopholes, 13824 judges-consistency≠reliability, 14992 MTAC-IFBench): the field is asking *which* comparisons justify *which* resource-allocation conclusions, and flagging policy/eval constructs that masquerade as agent errors.
4. **RL aligns by eliciting, not creating** (15064 Fixed-SAE): RL-induced drift is small, late-layer, token-scaffolding-oriented, and ~80% of its gain is recovered by steering existing features — a caution for compact "RL adds new skills" narratives. Meanwhile MoDA (14896) attacks the mode-collapse side of alignment with +265% diversity at higher pass@1.
5. **Linear attention/SSM context extension goes spectral** (SpectralShift Gated DeltaNet; cf. Gated Attention / DeltaTok-threads from conference-digest): initializations and spectral bands (slow retrieval vs fast clearing) matter as much as raw data — joins the hybrid-attention lineage tracked in tech-report-digest.
6. **LLM systems: allocation across depth, matrices, and memory** (14144 traffic-conditional early exit with a fidelity-failure warning, 15838 three-level low-rank compression, 14872 agent KV, runner-ups BOOST/Trillion-Parameter-MoE/VC-Attention): two-step scaling remains token/dollar cheap, but token-fidelity metrics are called out as hiding large accuracy loss.
7. **Trust & attribution become first-class attack surfaces** (AGENTQ quantization-conditioned agent backdoors, CiteShade citation laundering 0.01→0.68, CITECHOICE causal citation audit): quantization and citation channels — not just prompts — are now adversarial primitives, with counterfactual/audit defenses proposed.
8. **Sampling/decoding vigilance continues** (runner-ups: temperature fragility + truncation, speculative-decode precision in Orthrus): consistency and fidelity proxies keep failing in controllable setups, so decode-time measurement discipline remains a live research seam.

## ADS / CTR Coherence Check

0 direct CTR/ads papers in the 2609.132xx–159xx window (fourth consecutive window with ≈0 from this sweep — a genuine arXiv noise-floor for ads/CTR, which now primarily appears in conference batches like KDD/CIKM digests). Rec-adjacent: A1 (process-graph suffix-prediction recommendation), RA-CoA fashion captioning runner-up, and §9.3 citation-credit allocation relevant to search-ad fairness-of-attribution. No flagged ads material.

## Cross-Reference Index (Sibling & Runner-Up Coordinates)

- Entire featured set lies above the 09-14 arxiv-ai-search / arxiv-daily windows (max covered ID 2609.13144). Same-day 09-15 sibling reports were still rate-limited/locked at write time (no 09-15 files on disk; git status clean), so cross-dedup relies on the 0-hit grep checks plus the coordinate notes here.
- Runner-ups this window (grep-verified 0 hits): **2609.14100** RA-CoA (training-free fashion captioning for rec/ads-adjacent retrieval); **2609.14636** Know When to Stop/Where to Restart (multi-turn agentic on-policy distillation); **2609.14648** value-guided preference distillation (sparse outcomes ↔ dense behavioral signals); **2609.15476** Temperature Fragility & conditional benefits of truncation; **2609.15504** losslessness of speculative decoding under numerical precision (Orthrus); **2609.15810** VC-Attention (low-bit attention); **2609.13592** BOOST (host-memory ⊕ HBM for LLM inference); **2609.15636** Trillion-Parameter MoE in a Box (flash-memory provisioning); **2609.15248** Bandits with Probing (optimal regret / winner feedback limits); **2609.13564** greedy sampling explores (KL-regularized contextual bandits without Eluder dimension); **2609.14088** consistency-robustness tradeoffs for strategyproof scheduling with predictions (GT); **2609.14892** five-expert prediction PDE & exact optimality of COMB (GT); **2609.15100** ChatGPT Images 2.5 in the Wild (launch-period detection dataset/evals); **2609.15800** agentic visual RAG via explicit context selection; **2609.14860** one example passes fairness benchmarks; **2609.13356** ZGCM-1 (open efficient math/agentic-search foundation model); **2609.15296** Reason What Matters (retrieval-grounded multimodal embeddings); **2609.15964** verifiable-by-construction verbatim citation in clinical QA; **2609.15972** Mind2Dialogue (simulating user mental states); **2609.15344** parameter-efficient adaptation of PLMs for time-series forecasting; **2609.14116** HARP (agentic hybrid retrieval/analysis for long-form audio); **2609.15780** MoveBench (wildlife movement forecasting benchmark).
- Sub-window map for future dedup: IDs **132xx–140xx** (Fri–Sat online) and **140xx–146xx** (Sun) were screened at ¼- and ½-gram resolution via abs probing; denser follow-up possible if siblings need the same band later today.