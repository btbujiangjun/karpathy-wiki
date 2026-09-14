---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-14
updated: 2026-09-14
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, game-AI, LLM-judge, agents, memory, interpretability]
---

# arXiv AI Research Paper Search Report — 2026-09-14

Generated: 2026-09-14 (Monday). Freshest arXiv window = **Mon 14 Sep 2026 mailing** (same wave as today's arxiv-daily: IDs ~2609.120xx–2609.13144). 20 papers featured in full, all with **0 hits in `wiki/` at grep-verification time**.

**Methodology**: Parsed arXiv "recent" listings (`arxiv.org/list/{cat}/new?show=500`) for cs.AI, cs.LG, cs.CL, cs.IR, cs.GT, cs.MA, cs.CY, cs.NE, cs.SI — 546 unique IDs, 285 candidates ≥ 2609.12000 after excluding the 30 featured IDs of today's 09-14 [[arxiv-daily]]. Every featured ID below was grep-verified 0 hits in `wiki/` at selection time.

**Dedup notice**: AI/LLM-focused sibling of 09-14 [[arxiv-daily]]. Papers covered there (30) were deliberately excluded. No 09-14 arxiv-paper-check / game-rl-daily siblings exist yet — if created later, they may overlap; see Cross-Reference Index at the bottom.

## Summary Statistics

| Scope | Value |
|---|---|
| Mailing scanned | Mon 14 Sep 2026 (IDs ~2609.120xx–2609.13144) |
| Unique IDs scanned (9 categories) | 546 |
| Fresh candidates ≥ 2609.12000 (post-daily-dedup) | 285 |
| Featured in full in this report | 20 |
| Direct CTR / advertising papers | **0** (see ADS/CTR note) |
| Recommendation-adjacent | 1 (trust-aware health rec, §2.4) + 2 user-modeling papers |

**Advertising/CTR note**: No fresh direct CTR or advertising papers in this window — consistent with the 0-hit CTR count in today's arxiv-daily. The closest rec-adjacent finds (personalized user modeling for LLM interaction §2.1, implicit personality §2.3, trust-aware health recommendation §2.4) are included here.

---

## 1 LLM-as-a-Judge & Evaluation Reliability

### 1.1 Can We Trust LLM Judges — Capability-Dependent Biases and Multi-Judge Ensembles (2609.12002)
- **Title**: Can We Trust LLM Judges: A Study of Capability-Dependent Biases and Multi-Judge Ensemble for Bias Calibration
- **Authors**: Gemma Zhang, Prachi Badarayani, Asmi Kumar, Sadid Hasan, Sulaiman Vesal
- **Institution**: (industry, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12002
- **Abstract**: Studies biases in **absolute-scoring** LLM-as-a-judge (vs the usual pairwise setting), across 4 benchmarks × 6 models (36 judge–examinee pairs). Task accuracy strongly predicts judging accuracy (Pearson r ≥ 0.90) and inversely predicts directional bias (r ≤ −0.83), but accuracy alone does not ensure fairness: **more capable examinees consistently get more lenient judgments from all judges** (r ≥ 0.83). Proposes calibrated weighted majority voting (WMV): weights judges by online false-positive/false-negative rate estimates derived **purely from inter-judge disagreement** (no ground-truth labels, no task metadata). Label-free WMV tracks an oracle with perfect error-rate knowledge within 0.5 pp on average and beats both single judges and unweighted majority voting.
- **Key Innovations**: (1) Absolute-scoring (not pairwise) judge-bias study; (2) capability-leniency effect, decoupled from judge accuracy; (3) label-free, disagreement-based ensemble calibration.
- **Venue**: Preprint.

### 1.2 GAUGE — When Not to Trust LLM-as-a-Judge in User-Simulated Agent Eval (2609.12191)
- **Title**: GAUGE: When Not to Trust LLM-as-a-Judge in User-Simulated Evaluation of Task-Oriented Agents
- **Authors**: Umesh Bodhwani, Thanh Tran, Kai Wei
- **Institution**: (industry, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12191
- **Abstract**: The "offline gate" — persona-driven LLM user-simulator converses with each candidate agent, an LLM-as-a-judge scores transcripts, higher-scoring agent wins — is low-cost but validity is unmeasured. GAUGE is a reusable protocol benchmarking the gate against a **grounded verifiable reward** across 25 agents from six providers on τ²-bench and SimulatorArena, separating **ranking validity** from **construct validity**. Two findings: (1) a **satisfaction–success gap** — satisfaction carries ~no information about task success (57.5% of panel-rated-satisfied conversations actually failed the customer's task, consistent across 5 rater populations and all subjective dimensions); (2) the gate's ranking is robust across broad capability spans but loses resolution among near-equal strong agents (decision-disagreement jumps from <1% on wide-reward pairs to 31% on close pairs). Remedy: a **calibrate-then-trust cadence** where a judge-free completion bit is a zero-cost tripwire for truncation regressions.
- **Key Innovations**: (1) Reusable validity-audit protocol separating ranking vs construct validity; (2) quantifies satisfaction/success decorrelation + near-tie decision disagreement; (3) concrete tripwire for deployable offline gates.
- **Venue**: **EMNLP 2026 (Industry Track)**.

### 1.3 SynthSentry — Screening Synthetic Contamination Before Training (2609.12353)
- **Title**: SynthSentry: Detecting Synthetic Data Contamination in Language Model Training Data
- **Authors**: Praveen Kumar Myakala, Ravichandra Namburi, Sowmya Keragodu Jayaramu, Sooraj George Thomas
- **Institution**: (Indian academia/industry, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12353
- **Abstract**: Model collapse is usually **diagnosed after training**; the actionable problem is screening a corpus of unknown provenance **before** training. SynthSentry is a corpus-level, model-agnostic contamination signal requiring no access to the generator, no generation history, no synthetic labels — a distributional divergence over three statistics: lexical diversity collapse, n-gram tail truncation, perplexity variance across reference models. Evaluated under leave-one-generator-out on contaminated corpora (small open-weight + one instruction-tuned generator), with a domain-stratified false-positive study on naturally repetitive human text (legal, clinical, source code). Covariance shrinkage + bootstrap threshold keep per-domain calibration near its nominal FP budget (naive quantile runs 4× over). Framed as **data-curation defense**, not post-hoc diagnosis; toolkit released.
- **Key Innovations**: (1) Pre-training corruption screening (shifts detection left of training); (2) generator-agnostic triple-statistic divergence; (3) honest scope limits (single-generation, English, batch-mode) + over-pruning warning.
- **Venue**: **IEEE ICAEIT 2026**.

---

## 2 User Modeling, Personality & Personalized Alignment

### 2.1 The Atomic User Model (AUM) — Personality-Aware LLM Interaction (2609.12086)
- **Title**: Creating an Atomic User Model for Personality-Aware Large Language Model Interaction
- **Authors**: B. Sankar, Deepthika S, Pawni Yadav, Amogh A S
- **Institution**: (Indian academia, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12086
- **Abstract**: User personalization dominated by "preferences summarised from conversation history, reinserted into context" **inverts the order of inference**: preferences are the task-dependent surface of a stable personality structure, so a preference-only system relearns the person on every task change. Contributions: (1) characterizes **personality seepage** — a prompt's linguistic surface carries a personality fingerprint the assistant mirrors without access to the underlying personality; (2) the **Atomic User Model (AUM)**: a human-readable representation = stable identity nucleus + four interpretable shells (psychological, cognitive/experiential, behavioral, social) plus cross-shell conflict/authenticity entries; (3) treats AUM as a **retrieval index over the person**, not a prompt prefix, with a task classifier + budgeted retriever returning a small payload (8 fields on 23% of the full context = 211 tokens vs 915). Retrieving 8 fields matched full-model style fidelity, bested flat preference notes by 0.24 pts/5 (p<0.001, dz=0.50), and raised forced-choice voice identification 14.9%→42.7% (chance 25%). Benefit is largest for users the un-personalized assistant reproduces worst (ρ=−0.61, p=0.013).
- **Key Innovations**: (1) Personality-first (stable nucleus + shells) instead of preference-first; (2) retrieval-index framing + budgeted payload; (3) effect located in the representation, not the search (four null pre-registered controls).
- **Venue**: Preprint.

### 2.2 CORE/PERSIST — Mitigating Persona Drift in Multi-Turn Dialogue (2609.12373)
- **Title**: Toward Robust Personalized Alignment for LLMs: Mitigating Persona Drift in Multi-Turn Dialogue
- **Authors**: Youyuan Zhang, Siyuan Li, Fangming Liu, Jing Li
- **Institution**: (HKU / Chinese university, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12373
- **Abstract**: Persona drift — user profiles evolve over long interactions — means models must revise persistent persona states on genuine preference change **while avoiding** updates from transient, ambiguous, or unresolved observations. **CORE** separates turn-local evidence from persistent persona-state revision and applies **uncertainty-aware belief revision** for selective updates of grounded preferences. Ships **PERSIST**, a held-out post-anchor benchmark for persona-state robustness under sequential stress (ambiguity, conflict, controlled social influence). Across ALOE, PersonaChat, PERSIST: better personalized alignment and robustness + complementary gains in normalized closed-slot state fidelity. Human eval + mechanistic controls locate the gains in explicit update control rather than stronger generation or persistent memory alone.
- **Key Innovations**: (1) Explicit separation of evidential vs persona-state update channels; (2) uncertainty-aware selective revision; (3) PERSIST benchmark for adversarial sequential persona evolution.
- **Venue**: **Findings of EMNLP 2026**.

### 2.3 Implicit Personality Representations in Humans and LLMs (2609.12704)
- **Title**: Implicit Personality Representations in Humans and LLMs
- **Authors**: Yilin Geng, Omri Abend, Eduard Hovy, Lea Frermann
- **Institution**: Hebrew University / CMU / U Melbourne (multi-institution)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12704
- **Abstract**: Human implicit-personality structure (which trait words co-occur, which oppose) is strikingly consistent across raters/cultures. Tests whether Qwen 2.5-7B-Instruct reproduces it internally: builds a human implicit-personality matrix from millions of crowd-sourced personality ratings of fictional characters; builds a model matrix from contrastive activations over the same traits. The two align strongly (Mantel r = 0.77), trait-by-trait and in aggregate; the model's two dominant trait axes recover the classic **social warmth** and **intellectual competence** dimensions. On held-out dialogue, projecting activations onto these directions yields personality profiles agreeing with human ratings.
- **Key Innovations**: (1) Human-grounded comparison of internal trait geometry vs shared human personality structure; (2) recovery of the classic Big-Two emotion/competence axes from model activations; (3) activation-projection personality profiling on dialogue.
- **Venue**: **Findings of EMNLP 2026**.

### 2.4 Personalized, Trust-Aware Health Recommendation Policies (2609.12679)
- **Title**: Personalized and Trust-Aware Health Recommendation Policies for a Construction Workplace
- **Authors**: Atefeh Mollabagher, Yogesh Gautam, Houtan Jebelli, Parinaz Naghizadeh
- **Institution**: Penn State / Ohio State (tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12679
- **Abstract**: Trust-aware recommender design for personalized health interventions (fatigue/heat-stress monitoring for construction workers). Models the loop: worker health evolves, **trust** is affected by both health and recommendation dynamics, and trust in turn governs compliance with future recommendations. Characterizes the recommender policy (a health-based triggering threshold + recommendation frequency) with both model-based short-horizon control and model-free RL. Shows how recommendation frequency is tuned per worker to balance health, productivity, and trust.
- **Key Innovations**: (1) Co-evolution of health, trust, and recommendation compliance in one dynamic model; (2) policy characterization (trigger threshold + frequency) via control + RL; (3) rec-adjacent relevance: trust as a first-class state in recommender policy design.
- **Venue**: Preprint.

---

## 3 LLM Reasoning over Graphs & Knowledge

### 3.1 GT Bench + GTA — Algorithmic Graph Reasoning with LLMs (2609.12265)
- **Title**: GTA: Graph Theory Agent and Benchmark for Algorithmic Graph Reasoning with LLMs
- **Authors**: Zixiang Xu, Yanbo Wang, Chenxi Wang, Lang Gao, Zirui Song, Yue Huang, Zhaorun Chen, Xiangliang Zhang, Xiuying Chen
- **Institution**: KAUST / multi-institution (tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12265
- **Abstract**: Existing graph-reasoning evals are limited: simple tasks on small graphs, code-generation scoring rather than reasoning over the graph, or a single input format. **GT Bench**: 24 classical graph problems × 44 task-structure settings, 100k+ examples across 4 representations (natural language, structured language, adjacency list, adjacency matrix). Across 8 LLMs, accuracy is strongly tied to input representation; the best representation shifts with graph density, size, topology, and model — sensitivity persists (attenuated) in the strongest reasoning models. **GTA** = preference-trained representation selector + plan-and-decompose scaffolding around a frozen executor LLM: lifts Phi-4 53.5%→69.1% (easy split), 33.0%→41.5% (hard split), beats 8 prompting/agent baselines, transfers to GraCoRe and NLGraph.
- **Key Innovations**: (1) Largest representation-controlled graph-reasoning benchmark; (2) quantified representation-sensitivity of graph reasoning; (3) frozen-executor agent scaffolding + adaptive representation selection.
- **Venue**: Preprint.

### 3.2 Rank-Level Locality of Knowledge-Graph-Edits (2609.12116)
- **Title**: When Successful Knowledge Graph Edits Displace Correct Answers: Rank-Level Locality beyond Parameter Support
- **Authors**: Yi-Cheng Lai, Jerry Wang, Hsin-Ling Hsu, Li-Chu Chi, Ya-Wen Teng, Hen-Hsen Huang
- **Institution**: Taiwan academia (NCCU / Academia Sinica, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12116
- **Abstract**: Editing a KGE model to promote a desired answer can **displace correct answers from the returned list**; locality tests based only on facts reusing the edited parameter miss this ranking effect. Introduces a rank-displacement audit at three scopes (edited-parameter facts, other correct answers to the target query, correct answers across same-relation queries) and derives dimensional/geometric conditions for an update to improve the target while exactly preserving selected scores. On FB15k-237 (DistMult/ComplEx): direct promotion always gets target into top-10 but only 23.0–23.2% of edits are damage-free; strict preservation causes no damage but succeeds only 1.3–1.4%; **support-regularized entity editing** gives best joint success 36.3–37.7%; rank-truncated preservation reaches 32.8–34.7% and cuts displaced answers from ~14 to 1.2.
- **Key Innovations**: (1) Rank-level (list-level) locality as a separate failure mode from parameter-level locality; (2) three-scope displacement audit; (3) geometric conditions for damage-free promotion + best-practice recipe (support regularization).
- **Venue**: Preprint.

---

## 4 LLM Agents: Credit Assignment, Adaptation & SWE

### 4.1 GACA — Granularity-Adaptive Credit Assignment for Agent RL (2609.12424)
- **Title**: Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent Reinforcement Learning
- **Authors**: Taoran Liang, Yang Liu, Shang Luo, Yingguang Yang, Rongrong Zhang, Yingzong Min, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Kefu Xu, Congjing Ran, Bin Chong
- **Institution**: (Chinese academia, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12424
- **Abstract**: GRPO broadcasts one trajectory-level advantage to every step (cannot say which decision drove the outcome); GiGPO recovers step-level signal but **merges step- and episode-level estimates under a fixed weight**, spending equal resolution on pivotal decisions and routine transitions. **GACA** makes granularity state-dependent via an uncertainty-based criticality proxy: score each step by the NLL its own rollout records, then blend the two advantages with a per-step weight growing with that score (fine-grained signal dominant at above-average NLL, episode-level below). Provable exact risk decomposition for the mixture; conditional bound ties local action-value variation to expected NLL. On ALFWorld and WebShop, GACA beats GRPO and GiGPO at both 1.5B and 7B.
- **Key Innovations**: (1) Per-step (not fixed) credit-assignment granularity; (2) training-free criticality proxy from own-rollout NLL; (3) theory-backed blend + success at 1.5B/7B on ALFWorld/WebShop.
- **Venue**: Preprint.

### 4.2 BQ-LoRA — Behavior Quotient Learning for Agent Adaptation (2609.12896)
- **Title**: Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents
- **Authors**: Pengyang Zhou, Xiaobin Tu, Zhengxi Liu, Rongkun Xue, Haochen Li, Miancan Liu, Ziyuan Chen, Yinggui Wang, Jinkui Ren, Xiantao Zhang
- **Institution**: Alibaba-affiliated (tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12896
- **Abstract**: Multi-LoRA agent stacks distribute capabilities across adapters (storage + routing overhead); a single LoRA avoids this but faces two problems under a fixed rank budget: (1) distinct trajectories can induce equivalent decision-distribution changes → repeated updates over-emphasize redundant behavior; (2) an aggregated update can exceed the rank budget, and weight-space approximation distorts intended decision changes. **BQ-LoRA** organizes trajectory updates through a **local behavior quotient manifold**: *BQB* rewrites updates by local density in quotient tangent space; *DPC* projects the balanced gradient onto the intrinsic fixed-rank tangent space and refactorizes while jointly controlling weight-space error and decision-distribution distortion. Evaluated on AppWorld and BrowseComp-Plus vs standard LoRA and recent low-rank adaptation methods.
- **Key Innovations**: (1) Quotient-manifold view of trajectory-update redundancy; (2) decision-preserving (not just weight-error) low-rank compression; (3) single-adapter agent adaptation without per-capability adapters.
- **Venue**: Preprint.

### 4.3 Reality Is the Final Verifier — Two-Gap Framework for Agentic SWE (2609.12039)
- **Title**: Reality Is the Final Verifier: On Two Key Gaps in Agentic Software Engineering
- **Authors**: Alexander Krentsel, Shubham Agarwal, Mert Cemri, Shu Liu, Sidharth Sankhe, Ziming Mao, Matei Zaharia, Ion Stoica
- **Institution**: UC Berkeley (SkyLab)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12039
- **Abstract**: The implementation-verification loop (agent revises until a test-suite evaluator accepts) is analyzed as a **two-gap framework**: the *requirement gap* (requirements only approximate stakeholder intent) and the *model gap* (the evaluator's model only approximates the real deployment environment). Unifies agentic-SWE failure modes: **reward hacking exploits omissions** in requirements/model; **hallucination widens the gaps** by fabricating requirements or environment assumptions. Since neither gap can be certified closed in an open world, proposes an **assurance-revision loop** that revises requirements/model/evaluator from deployment evidence, and casts assured agentic development as resource allocation over human judgment, agent capability, and compute. Central claim: predeployment evals are proxies; reality (acceptable behavior under real deployment) is the ultimate test.
- **Key Innovations**: (1) Unifying two-gap theory of agentic-SWE failure (reward hacking ↔ requirement/model gaps); (2) assurance-revision loop shifting goal from closing to narrowing gaps; (3) Boston-consistency framing of eval-vs-deployment.
- **Venue**: Preprint (Berkeley).

---

## 5 Decoding, Memory & Sequential Modeling

### 5.1 CCPS — Chopthin-Consensus Power Sampling for LLM Decoding (2609.12243)
- **Title**: Chopthin-Consensus Power Sampling: A Diversity-Preserving Approach to LLM Decoding
- **Authors**: Minoo Ahmadi, Seyedarmin Azizi, Erfan Baghaei Potraghloo, Mehdi Kamal, Massoud Pedram
- **Institution**: USC (tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12243
- **Abstract**: Inference-time SMC (power sampling) improves LLM reasoning without post-training, but equal-weight resampling aggressively prunes low-weight trajectories and degrades genealogical diversity. **CCPS** applies the Chopthin resampler to LLM decoding: rather than equalizing weights, it **enforces an upper bound on the max/min weight ratio and carries unequal weights forward** — preserving distinct reasoning paths, leaving the weighted SMC approximation unchanged in conditional expectation, with a guaranteed post-resampling ESS lower bound. Pairing with a **semantic-majority selection** (merge token-identical trajectories, cluster semantically-equivalent answers, return the answer with the most distinct trajectories): Chopthin boosts oracle coverage in 13/15 settings; CCPS matches/exceeds Power-SMC final-answer accuracy in 14/15, up to +10.6 pp.
- **Key Innovations**: (1) First Chopthin (weight-bound) resampling for LLM SMC decoding; (2) diversity-preserving vs equal-weight resampling; (3) result-level semantic-majority consensus complement.
- **Venue**: **COLM 2026 Workshop on Efficient Reasoning**.

### 5.2 CueMem — Reconstructing Context from Cues for Long-Term Dialogue (2609.12354)
- **Title**: CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory
- **Authors**: Changjian Wang, Rongzhen Li, Weili Guan, Shuming Shi, Quan Lu, Ning Jiang
- **Institution**: Tencent AI Lab / Chinese academia (tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12354
- **Abstract**: Full-history dialogue recall is costly/unreliable; compressed memory units lose fine-grained evidence. Motivated by the reconstructive view of autobiographical memory, **CueMem** treats extracted memory records as **retrieval cues, not self-contained evidence**, then reconstructs query-relevant dialogue context from their source turns. Construction: extract fine-grained cues and link each to its source turn. Query time: retrieve cues → map to source-turn anchors → expand over a **turn graph** (temporal proximity + semantic relatedness) → reconstruct compact evidence context for the LLM. On LoCoMo and LongMemEval, CueMem beats representative long-term memory baselines; graph-based reconstruction recovers supporting evidence while cutting query-time tokens/latency vs full-history.
- **Key Innovations**: (1) Memory-as-cues + turn-graph reconstruction (reconstructive, not compressed-evidence, memory); (2) recovery of supporting dialogue evidence; (3) token/latency reduction vs full-history setting.
- **Venue**: Preprint.

### 5.3 Temporal Recurrence Favors Fewer Layers (2609.12531)
- **Title**: Temporal Recurrence Favors Fewer Layers
- **Authors**: Ivan Anokhin, Johan Obando-Ceron, Irina Rish, Sebastian Risi
- **Institution**: ITU Copenhagen / Mila (tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12531
- **Abstract**: Streaming-task question: once temporal recurrence carries latent computation across time steps, **how much within-step depth is still needed?** Studied as a compute-allocation problem — varying within-step depth, expert width, and parallel experts per layer over several compute budgets, comparing best recurrent vs non-recurrent allocations under approximately matched per-step compute. Across Sokoban and autoregressive FineWeb language modeling, temporal recurrence shifts the best compute allocation toward **substantially fewer layers** at comparable or better performance.
- **Key Innovations**: (1) Frame recurrence-vs-depth as compute allocation, not a binary competitiveness claim; (2) depth-sparing effect holds across RL (Sokoban) and LM (FineWeb) regimes; (3) ties to MoE/expert-width knob (width vs layers substitution with recurrence).
- **Venue**: Preprint.

---

## 6 Mechanistic Interpretability

### 6.1 Where Decoder Cosine Similarity Fails for SAE Feature-Flow Discovery (2609.12591)
- **Title**: Where Decoder Cosine Similarity Fails for SAE Feature Flow Discovery
- **Authors**: Hendrik Droste, Christian Medeiros Adriano, Kathrin Korte, Holger Giese
- **Institution**: HPI (Hasso Plattner Institute)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12591
- **Abstract**: Building **transition atlases** for residual-stream feature flow — triples $s_k + u_j \rightarrow t_\ell$ where a residual-state feature and an MLP-update feature jointly predict a downstream residual feature — and ablating decoded update features to validate candidates. In a 20M-token Pythia-160M $L_7 \to L_8$ run, 38,125 strong-ablation-effect transitions, but **88.0% have both state-target and update-target decoder cosine similarity < 0.7** — i.e., the standard decoder-similarity proxy would miss most genuine feature-flow transitions. Cross-check on Gemma-3-4B ($L_{21} \to L_{22}$) directionally consistent (53.6% of strong-effect triples low-similarity), though update-target cosine recovers many of the strongest Gemma effects.
- **Key Innovations**: (1) Negative methodological result: decoder cosine similarity is a poor proxy for feature-flow transitions; (2) first feature-flow transition atlas for MLP updates (Pythia + Gemma); (3) causal ablation validation protocol as the gold check.
- **Venue**: Preprint (4 pp).

---

## 7 Model Efficiency & Serving

### 7.1 Rivet — Internalizing Routed Experts into Compact Reasoners (2609.12578)
- **Title**: From Collaboration to Capability: Internalizing Routed LLM Experts into Compact Reasoners
- **Authors**: Frank Nie, Shuyao Wang, Ethan B. Liu
- **Institution**: (industry, tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12578
- **Abstract**: A compact controller coordinates stronger experts (selecting whom to consult, formulating requests, integrating responses); question: **does learning from the controller's decisions plus the experts' reasoning/code improve generation after expert removal?** **Rivet** ("collaboration internalization"): expert-augmented RL applies a shared outcome signal to controller decisions and returned expert spans; verified-trajectory internalization consolidates successful interactions via format-aware supervision. Deployed controller generates reasoning, code, and interaction structure with local Python execution — **no external LLM**. On 7 competition-math benchmarks, RIVET-1.7B / 4B hit 28.25% / 44.16% average accuracy; Stage-II (+6.49 pts post-removal for 4B) plus GPQA-Diamond evidence of generalization to scientific reasoning.
- **Key Innovations**: (1) "Collaboration internalization" as a compact-reasoner recipe (borrowing expert reasoning/code before removal); (2) format-aware verified-trajectory supervision; (3) self-contained local execution, no external LLM at deploy — relevant to routed-MoE distillation.
- **Venue**: Preprint.

### 7.2 Dissecting GPU Utilization for LLM Inference on Hopper (2609.12923)
- **Title**: Dissecting GPU Utilization for LLM Inference on Nvidia Hopper
- **Authors**: Mohammad Siavashi, Gerald Q. Maguire Jr., Dejan Kostic, Marco Chiesa
- **Institution**: KTH Royal Institute of Technology
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12923
- **Abstract**: A single SM-utilization number hides real utilization: on Hopper the bfloat16 GMMA path executes GEMMs in **fixed 64-row fragments**, so small-batch decode fills only a fraction of each fragment with real token rows. Profiles vLLM + FlashAttention-3 + cuBLASLt on H100 NVL across cold/warm prefill and decode (sweeping sequence length and batch size), replacing the single utilization number with **eight counter-validated views** derived from raw Nsight Compute reports, each pinned to an NCU counter or formula. Maps utilization gaps to concrete mechanisms — fragment fill, occupancy limits, stall signatures, wave quantization, kernel selection — across 4 production models and 6 per-layer kernel roles.
- **Key Innovations**: (1) Eight-view utilization decomposition (vs collapsed SM%); (2) quantifies the 64-row fragment-fill decode inefficiency; (3) per-layer kernel-role analysis actionable for serving optimization.
- **Venue**: Preprint.

### 7.3 SeqMoE — Predictive & Graph-Compatible MoE Offloading (2609.12978)
- **Title**: SeqMoE: Toward Full-Load Performance via Predictive and Graph-Compatible MoE Offloading
- **Authors**: Zihan Wang, Yuqi Wang, Lei Gong, Cheng Tang, Wenqi Lou, Teng Wang, Chao Wang, Xuehai Zhou
- **Institution**: USTC (tentative)
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12978
- **Abstract**: MoE offloading's structural advantage: only activated experts need to be resident — if loaded in time, offloading can approach full-load performance. **SeqMoE** closes the gap via: (i) **sequence-to-sequence expert-activation prediction** (first to recast activation prediction as sequence modeling → accurate multi-step, multi-layer forecasts); (ii) **joint prefetch scheduling** as Job Sequencing with Deadlines; (iii) **forecast-driven caching** — a probabilistic Belady policy for future-aware eviction; (iv) **graph-compatible offloading runtime** (compute-transparent placement, synchronization-free orchestration for end-to-end graph capture). With 45% expert residency: 96.97% hit rate and **80.22% of full-load performance**.
- **Key Innovations**: (1) Expert-activation prediction as sequence modeling (first); (2) deadline-scheduling prefetch + probabilistic Belady eviction; (3) end-to-end graph-captured offloading with explicit runtime principles.
- **Venue**: Preprint.

---

## 8 Game Theory & Incentive Design

### 8.1 Fragility of Worst-Case Nash Equilibria in Atomic Congestion Games (2609.12220)
- **Title**: On the Fragility of Worst-Case Nash Equilibria in Atomic Congestion Games
- **Authors**: Colton Hill, Brandon Collins, Philip N. Brown
- **Institution**: University of Colorado Colorado Springs
- **Date**: Announced 14 Sep 2026 (Mon mailing)
- **arXiv**: https://arxiv.org/abs/2609.12220
- **Abstract**: In incentivized atomic congestion games (traffic/mobility), worst-case equilibria are known to be inefficient vs the optimum; this paper tests **whether agents are "satisfied" with their worst-case decisions**. Results: agents' aggregate equilibrium satisfaction (relative to their optimal-allocation actions) is correlated with system-cost efficiency — if agents are very satisfied, the equilibrium must be relatively efficient; and **worst-case Nash equilibria are fragile**, since every agent is indifferent between its worst-case equilibrium action and its system-optimal action. Hence, at equilibrium, agents are either highly satisfied **or** the equilibrium is highly inefficient, but not both.
- **Key Innovations**: (1) Satisfaction/efficiency correlation at equilibrium; (2) fragility theorem: worst-case equilibria coincide with indifference; (3) extends the "indifference-only guarantees" line to congestion games — complements same-wave pPoA optimal-design results (2609.12077 in today's arxiv-daily, same group).
- **Venue**: Preprint.

---

## Key Trends Across This Window

1. **The LLM-as-a-judge validity crisis gets measurable** (Can-We-Trust-Judges, GAUGE, SynthSentry): leniency scales with examinee capability; satisfaction≁success in user-simulated agent eval (57.5% failure under panel-satisfied); contamination screening pushed pre-training. Reinforces the judge-validation skepticism thread across 09-12/09-13 paper-checks.
2. **Personalization pivots from preferences to stable personality structure** (AUM, CORE/PERSIST, Implicit Personality): personality-first user models + uncertainty-aware persona-state revision + human-grounded trait geometry (Mantel r=0.77) — clusters tightly with the user-modeling angle relevant to rec/ads personalization.
3. **Agent RL fixes credit assignment granularity** (GACA, BQ-LoRA): per-step adaptation of advantage granularity (GRPO/GiGPO gap) and behavior-quotient-manifold low-rank updates — practical, theory-backed training-efficiency directions for long-horizon agent tasks.
4. **Agentic SWE gets a unifying theory** (Two-Gap, Reality Is the Final Verifier): reward hacking ↔ requirement/model gaps; eval-vs-deployment stratification — echoes the "Reality/verifier" theme and eval-hygiene threads of 09-13.
5. **Diversity-preserving decoding returns, with theory** (CCPS): weight-bound resampling + semantic-majority consensus, up to +10.6 pp training-free on reasoning.
6. **Sequential modeling: recurrence buys shallower depth** (Fewer Layers); memory becomes reconstructive (CueMem) — both argue for reshaping the training-time vs inference-time compute allocation.
7. **MoE serving/offloading matures** (SeqMoE, Rivet): activation prediction as sequence modeling + 80% full-load performance at 45% residency; and distillation of routed-expert behavior into compact reasoners.
8. **Interpretability gets a negative result** (Decoder cosine ≠ feature flow): causal ablation beats cosine proxies for SAE transition atlases — a check on SAE-believable tooling.

## ADS / CTR Coherence Check

0 direct CTR/ads papers this window again (matches today's arxiv-daily). Rec-adjacent: §2.1 AUM (user modeling for personalization), §2.4 trust-aware health rec. Advertising image-gen was fully absorbed by today's arxiv-daily (§6). No new ads/CTR material to flag.

## Cross-Reference Index (Sibling-Covered IDs)

- **2609.12077** pPoA optimal utility design for networked games → same group as §8.1 (Philip N. Brown, UCCS), covered in 09-14 [[arxiv-daily]] §5.4.
- **2609.12375 / 12399 / 12556 / 12842 / 12579 / 13141 / 110xx** etc. → 09-14 arxiv-daily (30 papers), excluded here.
- No 09-14 arxiv-paper-check / game-rl-daily siblings exist yet; if scheduled, papers in §4/§8 (GACA, BQ-LoRA, congestion-game fragility) may be candidates for game-rl-daily re-coverage.
- **2609.13144** (Type Diversity / compositional generalization) referenced only as the upper bound of the ID window in arxiv-daily's methodology — not featured; excluded here to keep the 0-hit claim clean.