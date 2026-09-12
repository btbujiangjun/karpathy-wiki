---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Games"
type: synthesis
created: 2026-09-12
updated: 2026-09-12
tags: [arxiv-daily, AI, LLM, recommendation, advertising, auctions, CTR, sequential-modeling, time-series, games, game-theory, multi-agent, agents, RAG]
---

# arXiv Daily Report — 2026-09-12

> **Weekend note on methodology**: arXiv does not announce on weekends, so Sat 12 Sep 2026 has no new mailing; the freshest window is the **Fri 11 Sep 2026** mailing. This run re-scanned the cs.IR / cs.LG / cs.AI / cs.CL / cs.GT / cs.MA "recent" listings (arXiv API rate-limited → direct listing + `/abs/` pages) and features papers **fresh to the wiki** — every featured ID was grep-verified as 0 hits in `wiki/` and excluded from the 09-09 → 09-11 sibling digests (arxiv-daily, arxiv-ai-search, arxiv-paper-check, conference-digest, game-rl-daily). Existing coverage of the Fri-side wave (e.g. 2609.11876 regularized rec models, 2609.11682 COBRA-Skills, 2609.11209 REVA, 2609.11808 generative late-interaction VDR, 2609.11646 QPP, 2609.10750 synthetic-data forgetting) is **not** re-featured here. 24 papers featured across 7 sections.

---

## 1. Recommendation Systems & Advertising-Platform Economics

### 1.1 Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System

| Field | Detail |
|-------|--------|
| **Authors** | Ming Li, Dai Li, Xuying Ning, Bo Sun, Rui Li, Yi Zhang, Silvia Gong, Xuan Cao, Cornelia Carapcea, Qunshu Zhang, Zhigang Wang, Yinglong Xia, Andy Wang |
| **Institution** | Cloud-industry R&D (Amazon-inferred from author affiliations) |
| **Published** | 10 Sep 2026 (cs.CL) |
| **Abstract** | Auto-research agents can automate hypothesis generation, experiment execution, and iterative refinement, but scaling them to industry-scale recommendation models faces long feedback loops (multi-day training) and system complexity (fragile infra, multi-day GPU jobs). Auto-RecSys is an autonomous research system for long-horizon experimentation built on three harness designs: (1) distributed asynchronous execution for parallel experiments; (2) centralized cross-server memory for persistent, recoverable execution; (3) cognitive-procedural separation, where natural-language skill files steer LLM reasoning while deterministic scripts enforce operational correctness. A dual-loop self-evolving architecture accumulates operational knowledge (Execution Evolution Loop) and lets experimental outcomes inform ideation (Idea Evolution Loop). |
| **Key Innovations** | (1) Parallel + recoverable long-horizon experiment harness for recsys research; (2) cognitive/procedural split between LLM reasoning and deterministic execution; (3) self-evolving playbooks that cut per-experiment human time and improve execution reliability. |
| **Link** | [arXiv:2609.10922](https://arxiv.org/abs/2609.10922) |

### 1.2 Sequential Offering in On-Demand Platforms: On the Optimality of Greedy Ranking

| Field | Detail |
|-------|--------|
| **Authors** | Hongyao Ma, Will Ma, Matias Romero |
| **Institution** | Columbia University (inferred) |
| **Published** | 7 Sep 2026 (cs.GT) |
| **Abstract** | On-demand platforms raise the offered wage sequentially after each rejection, but the interaction between dynamic price adjustments and the order in which workers are approached is overlooked: if the best-suited workers are also ranked earliest, they see the lowest offers and decline, so less-suited workers end up taking the job. The paper jointly optimizes worker ranking and pricing trajectory to maximize expected welfare or platform profit. Main result: if the reservation-wage distribution has a non-increasing, convex density (Uniform, Exponential), welfare is maximized by greedy ranking with backward-induction wages; for arbitrary distributions greedy ranking achieves a tight n/(2n−1) fraction of the prophet benchmark. |
| **Key Innovations** | (1) First joint analysis of ranking + dynamic pricing in sequential offering; (2) tight prophet-bound for greedy ranking under arbitrary reservation distributions; (3) practical prescription: don't "low-ball" worse matches — stick with greedy ranking and tune wages via continuation value. |
| **Link** | [arXiv:2609.08001](https://arxiv.org/abs/2609.08001) |

### 1.3 A 1.283 Price-of-Anarchy Bound for the Repeated Virtual First-Price Auction

| Field | Detail |
|-------|--------|
| **Authors** | Endre Csóka |
| **Institution** | (Not specified) |
| **Published** | 28 Aug 2026 (cs.GT) |
| **Abstract** | Studies repeated allocation of a single indivisible resource among n strategic players with privately-known value distributions. Applies the repeated first-price auction with equal initial endowments of virtual money. Shows each player can asymptotically secure the same fair-floor guarantee as prior work (Csóka 2026), making the mechanism 1.283-optimal — a simpler and more robust alternative mechanism for this case that may also help sharpen upper bounds on the price of anarchy. |
| **Key Innovations** | (1) Explicit 1.283 PoA guarantee for repeated virtual first-price auctions; (2) fair-floor fairness notion achievable across equilibria; (3) simpler robustness argument relative to prior off-equilibrium analyses (relevant to autobidding-style repeated ad auctions). |
| **Link** | [arXiv:2609.05499](https://arxiv.org/abs/2609.05499) |

### 1.4 Following the Preference, Missing the Optimum: Compliance Without Optimization in AI Housing Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Hsuan Lo |
| **Institution** | (Not specified) |
| **Published** | 9 Sep 2026 (cs.CY / cs.IR) |
| **Abstract** | Audits LLM housing recommendation against verifiable ground truth. For 150 synthetic NYC renter scenarios, builds a pool of 120 real listings with known rent/bedrooms/GTFS commute, computes the exact constraint-satisfying set and its Pareto frontier. Across 9,945 calls to three models from two vendors: compliance is near-perfect (1.8% violations vs a 66.6% random floor), yet 39.0% of recommendations are strictly dominated; the dominating listing is a median $900/month cheaper and 3.5 minutes closer. A within-scenario manipulation separates two conflated capabilities: preferences are honored (one sentence shifts median recommended rent $646/month in the right direction) yet recommendations still sit $606/month above the five cheapest qualifying listings; an unambiguous lexicographic instruction yields no improvement under equivalence testing. |
| **Key Innovations** | (1) Strict-domination instrumentation ("compliance without optimization") as a deployable recsys diagnostic; (2) first enumeration-based audit that can score omissions against a ground-truth inventory; (3) equivalence-testing rigor separating preference-following from optimum-seeking. |
| **Link** | [arXiv:2609.10856](https://arxiv.org/abs/2609.10856) |

### 1.5 FINALLY: A Dataset Recommender System for Recommender-Systems Research

| Field | Detail |
|-------|--------|
| **Authors** | Louis Owie |
| **Institution** | University of Siegen (Bachelor's thesis, 2026) |
| **Published** | 8 Sep 2026 (cs.IR) |
| **Abstract** | Dataset selection shapes the empirical conditions under which recommender algorithms are evaluated, yet existing tools don't support constructing complete dataset sets meeting joint experimental constraints and set-level objectives. FINALLY is a web-based dataset recommender that combines required datasets, candidate-pool restrictions, metadata filters, target-set sizes, and Random / diverse / non-diverse strategies based on Effective Covariance and Convex Hull objectives. 420 recommendation runs across ten configurations all satisfied target-size, duplicate, snapshot, required-dataset and metadata-filter constraints; all 40 deterministic runs were reproducible and diverse-vs-non-diverse orderings matched objectives in all ten configurations. |
| **Key Innovations** | (1) Meta-level tooling: recommending *evaluation datasets* rather than items; (2) expressive constraint DSL for offline recsys experimental design; (3) reproducibility/consistency reporting as first-class output. |
| **Link** | [arXiv:2609.08941](https://arxiv.org/abs/2609.08941) |

---

## 2. Sequential Modeling & Time-Series

### 2.1 RDDMPI: Residual Denoising Diffusion Model for Probabilistic Multivariate Time Series Imputation

| Field | Detail |
|-------|--------|
| **Authors** | Ramiro Valdes Jara, David Chapman, Adam Meyers |
| **Institution** | (Not specified) |
| **Published** | 10 Sep 2026 (cs.LG) |
| **Abstract** | Multivariate time-series imputation (MTSI) widely uses diffusion, but most approaches denoise in the original data space, forcing the network to capture global structure, temporal dynamics, and stochastic variability at once. RDDMPI reformulates probabilistic imputation as baseline–residual decomposition: a pre-trained deterministic imputer captures the dominant signal while a conditional residual-diffusion process models residual uncertainty, conditioned on both the baseline-completed signal and its latent representation, with reliability-aware conditioning that adaptively weights baseline influence. Consistently improves both reconstruction accuracy and uncertainty quantification on multiple benchmarks. |
| **Key Innovations** | (1) Diffusion in residual space instead of raw data space; (2) reliability-aware conditioning on deterministic guidance; (3) decoupling dominant signal from stochastic residual for better uncertainty estimation (relevant to CTR/behavioral sequence gaps). |
| **Link** | [arXiv:2609.11648](https://arxiv.org/abs/2609.11648) |

### 2.2 LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics

| Field | Detail |
|-------|--------|
| **Authors** | Mariia Baranova, Adrien Petralia, Etienne Le Naour, Nathan Etourneau, Guillaume Hofmann, Themis Palpanas |
| **Institution** | Paris Dauphine University – LIPADE et al. (inferred) — IEEE ICDM 2026 |
| **Published** | 10 Sep 2026 (cs.LG / eess.SP) |
| **Abstract** | Diffusion-based generative model for year-long, sub-hourly smart-meter load curves, supporting conditioning on static household attributes (appliance ownership) and dynamic contexts (calendar, outdoor temperature). Evaluated on three residential datasets across fidelity, diversity, memorization risk, downstream utility (load forecasting, appliance detection), and conditional controllability under alternative temperature conditions. Produces realistic, diverse profiles with limited memorization while preserving downstream-usable information and responding coherently to conditioning changes. |
| **Key Innovations** | (1) Synthetic-data backbone for privacy-restricted energy analytics; (2) combined static+dynamic conditioning for load-curve generation; (3) memorization-risk and downstream-utility evaluation protocol (a template for synthetic recsys/CTR data work). |
| **Link** | [arXiv:2609.11639](https://arxiv.org/abs/2609.11639) |

### 2.3 A Dataset and Model for Imputing Water Surface Elevation on a Large and Extremely Sparse Spatiotemporal Graph

| Field | Detail |
|-------|--------|
| **Authors** | Ruben Cartuyvels, Karim Douch, Gabriele Bertoli, Mounia El Baz, Artemis Vrettou, Sébastien Lefèvre, Diego Fernandez Prieto |
| **Institution** | (Not specified) |
| **Published** | 10 Sep 2026 (cs.LG) |
| **Abstract** | Introduces AmazonSWE, a dataset for large-scale spatiotemporal graph imputation of water surface elevation, integrating processed satellite altimetry incl. the wide-swath SWOT sensor over 19K+ river sections and 10 years (2016–2026) in the Amazon basin, with in-situ gauges held out. With <1% of sections observed per day it is far sparser than existing benchmarks, and its directed acyclic river topology is structurally different and larger. Prior graph-imputation methods fail; a bidirectional selective state-space model that samples connected subgraphs and flattens space+time into a single token sequence with topology-aware positional encodings beats the SOTA SWOT-based densification method by 18–39% RMSE while predicting every river section. |
| **Key Innovations** | (1) 19K-node ×10-year ultra-sparse (<1%/day observed) spatiotemporal graph benchmark; (2) directed acyclic river-network topology not covered by prior benchmarks; (3) bidirectional SSM over flattened space-time tokens = strong signal that state-space/sequence models handle extreme-graph imputation. |
| **Link** | [arXiv:2609.11580](https://arxiv.org/abs/2609.11580) |

---

## 3. LLMs, Agents & Reasoning

### 3.1 T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks

| Field | Detail |
|-------|--------|
| **Authors** | Junyao Yang, Yucheng Shi, Zhongzhi Li, Ruhan Wang, Zongxia Li, Haitao Mi, Leowei Liang |
| **Institution** | (Not specified; cloud-sandbox terminal-agent R&D) |
| **Published** | 10 Sep 2026 (cs.LG) |
| **Abstract** | T1 is a 122B-total Mixture-of-Experts model trained with RL to operate a real shell in a cloud sandbox for up to 300+ tool-call turns per task, rewarded by executing each task's own verifier. Recipe: (1) aggressive warm start to stabilize actor-critic training with a dense process reward scoring trajectories by the absolute number of passing verifiers; (2) TITO (stable optimization training on exact sampled token identifiers with drift repair) and rollout-routing replay (R3) that record the sampler's per-token expert choices per MoE layer and replay them during training; (3) a fully out-of-distribution corpus isolated from Terminal-Bench 2.1. Post-training lifts the base model from 43.8% to 64.0% resolved on Terminal-Bench 2.1; on Long-Horizon Terminal Bench T1 reaches 27.9%, surpassing GPT-5.4 and GLM-5.1. |
| **Key Innovations** | (1) 122B-A-MoE end-to-end RL on real shell (300+ turn horizon) with verifier-rewarded training; (2) TITO (sampled-token identifier training + drift repair) and R3 (MoE rollout routing replay) to close the training-to-inference log-prob gap (0.021→0.013); (3) OOD-corpus protocol proving transfer not benchmark overfitting. |
| **Link** | [arXiv:2609.11042](https://arxiv.org/abs/2609.11042) |

### 3.2 Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification

| Field | Detail |
|-------|--------|
| **Authors** | Joshua Ong Jun Leang, Haonan Li, Zheng Zhao, Xinyi Shang, Wenda Li, Zhengzhong Liu, Erix Xing, Shay Cohen, Eleonora Giunchiglia |
| **Institution** | (Multiple academic institutions — CMU / Edinburgh / Imperial, inferred) |
| **Published** | 10 Sep 2026 (cs.AI) |
| **Abstract** | Training-free agentic pipeline that, given only a natural-language problem, produces an answer, formalizes it as a Lean 4 statement, and constructs a machine-checked proof. A statement judge verifies that the formalization preserves the original problem, while an error-attribution judge routes failures to either mathematical re-derivation or local Lean repair. Achieves 100% accuracy on AIME 2025, AIME 2026, and HMMT February 2026; paired with the open-weight K2-Horizon-7B reasoner it solves all six IMO 2026 problems. Analysis shows statement adjudication prevents false certificates and feedback-guided correction beats independent resampling. |
| **Key Innovations** | (1) Lean-verifier-in-the-loop reasoning without training; (2) dual-judge routing (statement fidelity + error attribution); (3) 100% olympiad benchmark results incl. full IMO 2026 sweep with a 7B reasoner. |
| **Link** | [arXiv:2609.11319](https://arxiv.org/abs/2609.11319) |

### 3.3 Beyond Confidence: Stability-Aware Test-Time Adaptation for LLM Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Bincheng Gu, Min Gao, Zongwei Wang, Yibing Bai, Yulan He, Junliang Yu |
| **Institution** | (Not specified) |
| **Published** | 10 Sep 2026 (cs.AI) |
| **Abstract** | Predictive-entropy-based test-time adaptation guides LLMs toward higher-confidence reasoning states without external verifiers, but high confidence does not imply correctness. Key observation: high-confidence reasoning is reliable when confidence stays stable under local perturbations. TASCO (Test-Time Adaptation via Stability-Aware Confidence Optimization) incorporates local stability into confidence-based TTA while keeping the LLM frozen, optimizing a lightweight task-level prefix under two perturbation strategies: Random Perturbation (distributional stability) and Sharpness-Aware Perturbation (worst-case local sensitivity). Improves reasoning accuracy and token efficiency across LLMs/benchmarks and maintains stable confidence without premature distribution concentration. |
| **Key Innovations** | (1) Stability (not just confidence) as the TTA signal for reasoning; (2) frozen-LLM lightweight prefix adaptation with two perturbation regimes; (3) token-efficiency gains alongside accuracy. |
| **Link** | [arXiv:2609.11393](https://arxiv.org/abs/2609.11393) |

### 3.4 Procedural Graphs: Self-Evolving Execution Structures for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Yuxing Lu, Yicheng Chen, Shanchan Wu, Sercan Ö. Arık |
| **Institution** | Google Research (inferred) |
| **Published** | 8 Sep 2026 (cs.AI / cs.CL / cs.MA) |
| **Abstract** | Most agents pick actions via unconstrained generation over accumulating history, leaving procedural knowledge (what to do, in what order, under which conditions) implicit, so long trajectories lose objectives and repeat unproductive actions. The Procedural Graph organizes procedural knowledge into (procedure, relation, procedure) triplets — the what-to-do analogue of a knowledge graph. At each step a guidance model translates the subgraph around the active node into situational step guidance that biases (not dictates) the next action. An LLM refiner self-evolves the graph by contrasting failed vs successful trajectories, committing edits that preserve/improve held-out validation and retaining rejected ones to discourage repetition. Beats memory-based baselines across datasets/task types/LLMs, and can repair a flawed expert prior. |
| **Key Innovations** | (1) Procedural graphs as explicit executable structure for agents (parallels knowledge graphs for facts); (2) self-evolving topology driven by trajectory contrast + validation gating; (3) guidance-vs-control separation so the graph biases without constraining. |
| **Link** | [arXiv:2609.09153](https://arxiv.org/abs/2609.09153) |

### 3.5 From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge

| Field | Detail |
|-------|--------|
| **Authors** | Wenkang Wei, Yuan Fang, Renhe Jiang, Hong Cheng, Xingtong Yu |
| **Institution** | Chinese University of Hong Kong et al. (inferred) |
| **Published** | 10 Sep 2026 (cs.AI) |
| **Abstract** | Layerwise-intervention study of how query-routing vs target-knowledge dependence changes while Qwen / Llama / Gemma answer country–continent questions. Separates a pair-conditioned request direction (which country is queried), a global request direction (first vs second country in paired questions), selection candidates, and fitted knowledge. In Qwen, the pair-conditioned direction strengthens before interventions on it start to alter later fitted knowledge, with the causal window opening while answer-supporting content is still forming. Trajectories are not uniform: Gemma shows a partially-overlapping mid-layer routing-content profile; Llama shows no sustained routing-effect window under the same gates. Late effect of the pair-conditioned direction persists even as global fitted-content dependence shifts to later layers. |
| **Key Innovations** | (1) Causal (intervention-based) decomposition of routing vs content vs selection across 3 model families; (2) evidence that routing dependence is *readable* before it becomes *steerable*; (3) cross-family non-uniformity as a caution for mechanistic claims. |
| **Link** | [arXiv:2609.11859](https://arxiv.org/abs/2609.11859) |

---

## 4. RAG & Information Retrieval

### 4.1 TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering in Overlapping-Evolving Documents

| Field | Detail |
|-------|--------|
| **Authors** | Youngeun Nam, Joeun Kim, Hwanjun Song, Susik Yoon, Jae-Gil Lee, Byung Suk Lee |
| **Institution** | KAIST et al. (inferred) |
| **Published** | 10 Sep 2026 (cs.IR) |
| **Abstract** | Time-sensitive retrieval has addressed the disjoint-evolving environment (each update a fresh snapshot), but laws/policies/regulations amend clauses while preserving most content — an overlapping-evolving environment with strong semantic overlap across versions that trips existing methods. TimelyRAG is a retriever-agnostic framework that injects temporal distance into ranking to align queries with version-appropriate documents, plus TimelyQABench, the first benchmark for regulation-heavy overlapping-evolving domains. Consistent gains up to +28.6% nDCG@10. |
| **Key Innovations** | (1) First treatment of overlapping-evolving (amendment-style) document drift in time-sensitive retrieval; (2) retriever-agnostic temporal-distance ranking; (3) TimelyQABench benchmark for regulated domains. |
| **Link** | [arXiv:2609.11572](https://arxiv.org/abs/2609.11572) |

### 4.2 RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety

| Field | Detail |
|-------|--------|
| **Authors** | Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser |
| **Institution** | National Research Council Canada (inferred) — EMNLP 2026 |
| **Published** | 10 Sep 2026 (cs.CL / cs.IR) |
| **Abstract** | RAG can increase reliability but has unintended side effects on safety when prompted for harmful content. RAG-Safety-Bench isolates the mechanisms by removing the confounding effect of retriever quality and cleanly splitting into four conditions: non-RAG, RAG with an oracle harmful-answer document, RAG with related-but-not-answering documents, and RAG with random safe documents. Across five open-source LLMs: an inverse relationship between benign and unsafe capability, strong evidence that baseline safety guardrails don't imply downstream safety under RAG, and model-specific support that even benign documents can trigger unsafe generation. |
| **Key Innovations** | (1) Four-condition causal isolation of retriever, content, and safety-guardrail effects in RAG safety; (2) benchmark across 5 open-weight LLMs; (3) evidence against "guardrail-in-l, guardrail-out" assumptions. |
| **Link** | [arXiv:2609.11758](https://arxiv.org/abs/2609.11758) |

### 4.3 SearchAtlas: Analyzing Agentic Search Strategies via Evidential Query Graphs

| Field | Detail |
|-------|--------|
| **Authors** | Jiacheng Sang, Mengyuan Li, Sanxing Chen, Yukun Huang, Yu Feng, Bhuwan Dhingra |
| **Institution** | Duke University et al. (inferred) — Findings of EMNLP 2026 |
| **Published** | 9 Sep 2026 (cs.CL) |
| **Abstract** | LLM search agents are evaluated on final-answer accuracy, overlooking the process. SearchAtlas converts search trajectories into structured graphs whose edges show how evidence propagates from retrieving query to final answer; a parsing pipeline achieves mean edge F1 86.0% vs human annotations. Analyzing five search agents on three benchmarks reveals systematic differences in search scale and evidence aggregation, exposing fragmented answer support, unsatisfied question constraints, and unverified parametric knowledge in responses. These process failures are more strongly associated with incorrect answers than an LLM judge reading either the raw trajectory or the ordered query list, and the diagnostic signal is not reducible to answer accuracy. |
| **Key Innovations** | (1) Evidence-propagation graphs as a process-level evaluation of agentic search; (2) automated trajectory→graph parsing at 86.0% edge F1; (3) audit evidence that process diagnostics beat LLM-judge trajectories for failure attribution. |
| **Link** | [arXiv:2609.10901](https://arxiv.org/abs/2609.10901) |

---

## 5. LLM Efficiency & Compression

### 5.1 FlexComp: One Model for Every Ratio in Context Compression

| Field | Detail |
|-------|--------|
| **Authors** | Kaiyan Zhao, Zhongtao Miao, Akiko Aizawa, Yoshimasa Tsuruoka |
| **Institution** | University of Tokyo / NII (inferred) |
| **Published** | 10 Sep 2026 (cs.CL) |
| **Abstract** | Soft context compressors fix the compression ratio at training and inference: each deployed ratio needs a separately trained model and the ratio is applied uniformly, though actual per-input needs vary. FlexComp decouples the ratio from both training and deployment: Matryoshka-style training samples the memory-budget K per instance so a single model acts as an any-ratio compressor, then K is chosen per input by (1) confidence-based cascade routing or (2) a lightweight learned K predictor. On ICAE / 500xCompressor / SAC over MRQA, a single FlexComp model matches separately trained fixed-ratio specialists; cascade routing preserves >98% of the mildest ratio's accuracy at up to 266× average compression, and the K predictor reaches 158–236× within 0.7 F1 of the mildest ratio while cutting context KV cache 50% and boosting decoding throughput 47% at serving batch sizes. |
| **Key Innovations** | (1) Any-ratio compression from one checkpoint via Matryoshka-style budget sampling; (2) two deployment pathways (cascade routing / learned K predictor) for per-input ratio choice; (3) serving-scale KV-cache and throughput gains. |
| **Link** | [arXiv:2609.11192](https://arxiv.org/abs/2609.11192) |

### 5.2 Structured Transforms for Low-Overhead Quantization of Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Daria Cherniuk, Alexander Rudikov, Boris Kashin, Ivan Oseledets |
| **Institution** | Skoltech et al. (inferred) |
| **Published** | 10 Sep 2026 (cs.CL) |
| **Abstract** | Revisits Kashin-decomposition weight quantization for LLMs with an improved algorithm and structured orthogonal transforms, replacing the dense random orthogonal matrix with a sign-randomized Discrete Cosine Transform (DCT), cutting per-iteration cost from O(N²) to O(N log N). A greedy alternating-update algorithm guarantees the four-peak distribution needed for stable 2-bit clustering with closed-form cluster-center initialization, removing the multi-restart k-means bottleneck. Composed with OPTQ-style error compensation and QuIP-style incoherence preprocessing, the JAX pipeline is competitive with OPTQ / QuIP / QuIP-RG at 4-bit per channel on OPT, Llama-2, Pythia — and notably robust where QuIP variants diverge (four-digit perplexity on Pythia-6.9B) or abort with NaNs (Mistral-7B). Each weight decomposes into two 2-bit factor codes per channel suited to native-2-bit hardware. |
| **Key Innovations** | (1) Kashin decomposition + structured DCT transform (O(N log N) instead of O(N²)); (2) deterministic 2-bit clustering with closed-form initialization; (3) numerical robustness on stress configs where QuIP-family diverges — a strong argument for structured-matrix quantization. |
| **Link** | [arXiv:2609.11687](https://arxiv.org/abs/2609.11687) |

---

## 6. Games & Game Theory

### 6.1 Truncated Noisy Best-Response Algorithms: Toward Game Theoretic Learning with Safety Guarantees

| Field | Detail |
|-------|--------|
| **Authors** | Vartika Singh, Philip N. Brown |
| **Institution** | University of Colorado Colorado Springs (inferred) |
| **Published** | 10 Sep 2026 (cs.GT / cs.MA) |
| **Abstract** | For submodular-coordination games, Nash equilibria are always within 50% of optimal, but the worst-case equilibria are not stable. TNBR algorithms have agents asynchronously and stochastically choosing actions in a neighborhood of their best-response payoffs. Recurrent-class bounds split into (1) Performance bounds — TNBR always has a high-value recurrent state — and (2) Safety bounds — TNBR never has arbitrarily bad recurrent states. The two are linked by a waterbed effect: every game with a poor Safety guarantee necessarily has a favorable Performance guarantee. |
| **Key Innovations** | (1) Asynchronous stochastic neighborhood best-response family with Markov-chain recurrent-class analysis; (2) performance/safety dichotomy via a waterbed tradeoff; (3) practical coordination algorithms with worst-case guarantees. |
| **Link** | [arXiv:2609.11863](https://arxiv.org/abs/2609.11863) |

### 6.2 ABRA: An Algorithm Which Cannot Converge to Low-Quality Nash Equilibria

| Field | Detail |
|-------|--------|
| **Authors** | Vartika Singh, Philip N. Brown |
| **Institution** | University of Colorado Colorado Springs (inferred) |
| **Published** | 10 Sep 2026 (cs.GT) |
| **Abstract** | Companion to TNBR (6.1). ABRA (Approximate Best Response Algorithm) is governed by a noise parameter (escape bad equilibria) and a rationality parameter (balance noise-induced objective degradation). For any two-player game: if ABRA converges to a Nash equilibrium, its system objective strictly exceeds 50% of optimal plus a noise-controlled term; otherwise it converges to a recurrent class that, if it contains an action profile below 50% optimal, must also contain either the optimal profile or one exceeding 50% by the same amount plus a noise factor. Time spent in bad profiles is controllable via the rationality parameter. |
| **Key Innovations** | (1) Convergence guarantee excluding low-quality Nash equilibria outright; (2) recurrent-class characterization with noise/rationality-knob control; (3) numerical evidence that expected objective typically sits well above half of optimum. |
| **Link** | [arXiv:2609.11889](https://arxiv.org/abs/2609.11889) |

### 6.3 Games Over Observation Spaces in Multi-Agent Capture the Flag

| Field | Detail |
|-------|--------|
| **Authors** | Mae Frost, Michael Amir, Shaunak D. Bopardikar |
| **Institution** | (Not specified) — 17th Int. Conf. on Game Theory and AI for Security (to appear) |
| **Published** | 5 Sep 2026 (cs.GT) |
| **Abstract** | Multi-agent Capture-the-Flag on a graph: attackers pick heuristics from a library, defense is restricted to a single fixed policy. To compensate, a centralized defense oracle strategically restricts the graph portion visible to each defender to elicit a wider range of behaviors from the fixed policy. Formalized as a two-player zero-sum game (attacker reasons over heuristic library vs defense over visibility profiles) and solved with a Double Oracle algorithm to approximate empirical equilibria. Observation manipulation demonstrably improves defense performance. |
| **Key Innovations** | (1) Observation-space (visibility) manipulation as a control variable for fixed policies — dual to action space in [2609.06178: games over observation spaces]; (2) Double Oracle equilibrium solving over an intractably large combinatorial game; (3) empirical validation that partial observability can be a defensive asset. |
| **Link** | [arXiv:2609.06178](https://arxiv.org/abs/2609.06178) |

### 6.4 Last-Iterate Convergence of Policy Dynamics in Zero-Sum Networked Separable Markov Games

| Field | Detail |
|-------|--------|
| **Authors** | Zailin Ma |
| **Institution** | (Not specified) |
| **Published** | 8 Sep 2026 (cs.GT) |
| **Abstract** | Two-player zero-sum Markov games admit fast last-iterate policy optimization, while general multi-player games are intractable. Finite-horizon zero-sum networked separable Markov games (global competition via pairwise interactions, tractable NE) previously needed either equilibrium-collapse arguments (single controller) or backward DP with per-stage equilibrium solvers. ER-OMWU (entropy-regularized optimistic multiplicative weights update) is a single-loop, symmetric policy dynamic returning an approximate NE in the last iteration: after Õ(1/ε) iterations it gives an ε-approximate NE, preserving near-linear last-iterate rates of two-player zero-sum policy optimization in a more complex structured multi-player setting. |
| **Key Innovations** | (1) First last-iterate convergence analysis for this networked separable class; (2) single-loop symmetric update (no per-stage NE solvers); (3) Õ(1/ε) iterate complexity for ε-approximate NE. |
| **Link** | [arXiv:2609.08823](https://arxiv.org/abs/2609.08823) |

---

## 7. Multi-Agent Systems

### 7.1 ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI

| Field | Detail |
|-------|--------|
| **Authors** | Zhengran Ji, Jonathan Hyun, Boyuan Chen |
| **Institution** | Duke University (inferred) |
| **Published** | 10 Sep 2026 (cs.MA / cs.AI / cs.LG / cs.RO) |
| **Abstract** | Artificial multi-agent systems use fixed organizational structures even when tasks impose different coordination requirements. ORCH (Organizing Roles and Coordination Hierarchies) builds task-specific hierarchies by combining pooled interdependence (concurrent work) with sequential interdependence (prerequisite-ordered work). Across 25 wildfire-response missions (reconnaissance, rescue, transport, resource management, containment, suppression) with teams of up to 50 heterogeneous agents under 8 LLMs, ORCH organizations beat four embodied multi-agent baselines on mission outcome, efficiency, exploration and compute; human-designed ORCH improved final score +63.97% and efficiency +74.29% on average, auto-generated +43.63% / +52.53%. Performance wasn't monotonically tied to model scale, and hierarchy preserved concurrency within groups while coordinating phase transitions. |
| **Key Innovations** | (1) Operationalizing human organization theory (pooled vs sequential interdependence) for embodied AI collectives; (2) up-to-50-agent heterogeneous teams across 25 missions; (3) non-monotonicity-in-model-scale finding (organization matters as much as backbone). |
| **Link** | [arXiv:2609.11737](https://arxiv.org/abs/2609.11737) |

### 7.2 CUSP: Decomposable Collective Uncertainty for Multi-Agent Multimodal Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Chung-En Johnny Yu, David Garcia, Brian Jalaian, Nathaniel D. Bastian |
| **Institution** | (US Army Research Laboratory / academic, inferred) |
| **Published** | 4 Sep 2026 (cs.AI / cs.LG / cs.MA) |
| **Abstract** | Aggregating heterogeneous VLMs improves multimodal reasoning, but neither individual confidence nor aggregated-answer accuracy measures system-level reliability. CUSP (Collective Uncertainty through Semantic Opinion Pooling) is training-free: it maps multiple VLM responses to a shared semantic response space, pools them into a pooled opinion, and reports collective uncertainty (dispersion) plus Jensen–Shannon divergence (JSD, inter-model conflict). The unnormalized collective entropy decomposes exactly into mean individual semantic entropy + JSD. Needs no token logits or calibration labels, so it works on open-weight and commercial VLMs. In static ensembles collective uncertainty is the strongest error-detection signal in the small-model regime (0.764 AUROC), JSD strongest in the commercial regime (0.819 AUROC; ranks hard-answer conflict up to 0.982 AUROC); the pooled prediction beats the average single model by 5.6–13.0 points; over multi-step multi-agent trajectories, subagent collective uncertainty ranks failures above chance (0.619 AUROC) and gives best abstention ordering (0.699 AUARC). |
| **Key Innovations** | (1) Training-free, logit-free system-level uncertainty for VLM ensembles; (2) exact decomposition of collective entropy into per-model entropy + conflict (JSD); (3) transfer to multi-agent multi-step trajectories for failure ranking and abstention. |
| **Link** | [arXiv:2609.05708](https://arxiv.org/abs/2609.05708) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **Auto-research for recsys** | Auto-RecSys (autonomous experimentation on industry-scale rec), FINALLY (auto dataset set construction) |
| **Ads-adjacent mechanism design** | Greedy-ranking optimality under dynamic pricing (2609.08001), repeated virtual first-price auction 1.283 PoA (2609.05499) |
| **Recsys evaluation gets audited** | Housing "compliance without optimization" (2609.10856) joins this wave's measurement-stability theme (cf. 09-06 digest: LLM-judge reliability, seed stability) |
| **Diffusion → residual spaces** | RDDMPI (time-series imputation), LoaDiff (energy load generation); 09-11's DeRes (CTR residual paths) shows the same residual-decomposition pattern upstream in ranking |
| **Extreme-sparsity sequence modeling** | AmazonSWE: SSMs over flattened space-time tokens beat graph GNNs at <1% daily observation |
| **Terminal/verifier agents** | T1 (122B-MoE shell RL, 300+ turns), Magenta (Lean-verified math, 100% olympiad), Procedural Graphs (self-evolving execution structure) |
| **RAG reliability** | TimelyRAG (amendment-drift temporal ranking), RAG-Safety-Bench (4-condition safety isolation), SearchAtlas (evidence-graph process diagnostics) |
| **Compression/quantization with structure** | FlexComp (any-ratio context compression), Kashin-DCT quantization (robust where QuIP diverges) |
| **Unstable-equilibrium exploitation** | TNBR & ABRA (turn NE instability into quality/safety guarantees) — continues this wave's equilibrium-dynamics thread (cf. 09-11 PoA paradoxes) |