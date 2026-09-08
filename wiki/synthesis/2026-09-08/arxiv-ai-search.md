---
title: arXiv AI Research Paper Search Report
type: synthesis
created: 2026-09-08
updated: 2026-09-08
sources: [arxiv.org]
tags: [arxiv, AI, LLM, interpretability, mechanistic-interpretability, reasoning, RLVR, training-dynamics, calibration, safety, refusal, agents, efficiency, quantization, game-theory, fair-division, daily-digest]
---

# arXiv AI Research Paper Search Report

Generated: 2026-09-08 | Scope: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

**Methodology**: No new arXiv mailing appeared since 09-07 (arXiv lists announced through **Mon 7 Sep 2026**), so this report is a **second pass over the Mon 7 Sep 2026 mailing**, sweeping the papers the 09-07 digests did *not* feature. Data pulled directly from `arxiv.org/list/{cs.IR,cs.CL,cs.LG,cs.GT}/recent` listings + individual `/abs/` pages (arXiv Atom API still rate-limited). This report is **complementary** to the 09-07 reports: the 24 papers featured in [[arxiv-ai-search]] and 23 in [[arxiv-daily]] (both 2026-09-07) are **not re-featured**. The same-day 09-08 sibling digest [[arxiv-paper-check]] is also non-overlapping (its 10 papers — layer-dropout 2609.05275, RISE 2609.05295, OPD 2609.05198, scaling-law BO 2609.05016, GUT 2609.05284, TROVE 2609.05019, compact memory 2609.04915, ACE 2609.05228, Speculative Uncertainty 2609.05274, phase-transition 2609.05194 — all screened out of this pass). 17 new papers selected across 6 sections; every featured arXiv ID was **grep-verified absent from `wiki/`** (24/24 candidates checked, 22 clean, 2 already covered: 2609.05152 DEX-Comp and 2609.04526 Scale-QLoRA, both in arxiv-daily / arxiv-ai-search 09-07).

> **Recommendation / Advertising / CTR / Sequential coverage note**: the cs.IR Mon 7 Sep listing (20/20 entries) was **fully mined on 09-07** (Embedding Surgery 2609.05110, AlleCompanion 2609.05063, AtomRec 2609.04882, PTDG 2609.04862, LARK 2609.04645, MURAL 2609.04574, SAM-D2Q 2609.04961, IGPO 2609.04813, Repeated Queries 2609.05059, CAGE 2609.04647) plus RecSys-adjacent Trade-up Rec (2609.05363) and the forecasting/sequential set (PRICE 2609.05235, MomentQuant 2609.05136, RCBNB-MB 2609.05150) in the same-day digests. The only new rec/ads-domain-adjacent find in this second pass is 2609.05309 (mHC residual streams, Huawei ranking/CTR group) — featured in §1.1 below. For genuinely fresh cs.IR material, wait for the Tue 8 Sep 2026 listing.

---

## 1. LLMs — Mechanistic Interpretation & Representational Geometry

### 1.1 How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity Mixing
- **Authors**: Pengxiang Zhao, Xing Li, Xianzhi Yu, Wei Guo, Zhenhua Dong
- **Institution**: Huawei (tentative — Wei Guo / Zhenhua Dong, the ranking/CTR group)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05309
- **Abstract**: Hyper-Connections and their manifold-constrained variant mHC widen a residual pathway from one stream to *n*, but how trained models *use* this capacity was unclear. The authors dissect the four-stream residual pathway of DeepSeek-V4-Flash with effective stream counts, cross-stream residual weights, and inter-stream cosine similarity. Read/write routing is **concentrated but depth-dependent**: a typical attention/FFN site effectively uses ~2 streams, the dominant stream changes across layers, and streams stay directionally distinct. Residual mixing is modest and mostly early: in layers 22–42 the pathway carries each stream forward almost separately. Interventions confirm this: replacing late mixers with identity costs only +1.9% C4 perplexity and preserves the six-task average; replacing early mixers costs +41%. Fixing each early mixer to its C4 diagnostic mean costs only +0.2% PPL / −0.25 pp average score (site-specific structure matters more than token-wise variation); retaining only the 3 largest routing weights per token costs ≤ +2.7% PPL. The model realizes only *part* of the flexibility four-stream mHC affords — individual blocks rarely need all streams, and late residual mixing provides little measured benefit.
- **Key Innovations**: First functional dissection of mHC/Hyper-Connection residual streams in a frontier MoE (DeepSeek-V4-Flash); separates read-routing from write-routing; shows late-stage mixers are near-identity and effectively roundable/mergeable — a concrete pruning target inside the mHC architecture that several sibling tech-report digests track.
- **Venue**: Preprint

### 1.2 Interpretability for Turing Machines
- **Authors**: Billy Snikkers, Rumi Salazar, Daniel Murfet, Will Troiani
- **Institution**: University of Melbourne (tentative — Daniel Murfet)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04661
- **Abstract**: The authors show that **susceptibilities** — an interpretability technique developed for neural networks — can identify algorithmic structure in Turing machines by probing the local loss landscape of a noisy-TM learning problem introduced by Murfet & Troiani (arXiv:2504.08075). They *prove* that symmetries and path separation in the implemented algorithm induce permutation symmetries and low-rank blocks in the susceptibility matrix, then verify empirically on deterministic finite automata: algorithmic features are recovered by PCA and clustering in susceptibility space. 75 pages with interactive companion.
- **Key Innovations**: The neural interpretability toolkit (susceptibility analysis) formally ported to classical computation; theorem linking algorithm symmetries to spectral structure; first systematic susceptibility-scale study of automata/algorithm-site structure.
- **Venue**: Preprint

### 1.3 Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs
- **Authors**: Seogyeong Jeong, Jaehui Hwang, Dongyoon Han, Geonmo Gu, Alice Oh, Taekyung Kim
- **Institution**: NAVER / KAIST / Seoul National University (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04753
- **Abstract**: CoT reasoning unfolds through operations (problem formulation, goal decomposition, deduction) that are explicit in text, but their *geometric organization* in representation space was unknown. The authors find that reasoning operations are **separable in held-out hidden representations**, with separability peaking in middle layers, and verify the structure is not explained by lexical/positional confounds. Across layers, token-wise operation-alignment becomes more distributed over spans, and identical surface tokens are represented differently depending on the surrounding chunk's operation. Attention-masking interventions show operation-aligned representations at chunk onset depend on the preceding reasoning context — i.e. LMs maintain a representational correspondence between linguistic reasoning expressions and internal geometric structure.
- **Key Innovations**: Geometrically relocates CoT "operations" (vs. treating CoT as flat text); confound-controlled separability; chunk-onset context dependence via attention masking.
- **Venue**: EMNLP 2026 Main Conference

### 1.4 Shared circuits predict whether LLMs generalize across formats in arithmetic reasoning
- **Authors**: Andrea Gregor de Varda, Sana Pandey, Pengrui Han, Jacob Andreas, Evelina Fedorenko
- **Institution**: MIT / University of Trento (tentative)
- **Date**: 2026-09-03
- **arXiv**: https://arxiv.org/abs/2609.04463
- **Abstract**: LLMs are brittle to surface variation (e.g. numeric `2+5` near-perfect vs verbal `two plus five` much worse). Using **attribution patching**, the authors first localize — independently — the circuit recruited for numeric vs verbal arithmetic in three languages (EN/ES/IT), then test whether overlap with the model's *own* numeric circuit predicts generalization to verbal formats. Circuit overlap accounts for (i) the relative difficulty of the three verbal formats, (ii) which models generalize best, and (iii) which items are solved correctly — **rivaling supervised probes while requiring no labeled data**.
- **Key Innovations**: Cross-format generalization predicted from **internal circuit overlap** (label-free); attribution patching across 3 languages; connects mechanistic overlap to a behavioral generalization law.
- **Venue**: Preprint

### 1.5 A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures
- **Authors**: Oskar Holmström, Marcel Bollmann, Marco Kuhlmann
- **Institution**: Linköping University (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04819
- **Abstract**: Four cross-lingual sharing metrics — CKA, ANC, GMM dominance per token, and ILO — are compared across 21 base models from five families (125M–14B), each correlated with cross-lingual transfer on five downstream tasks. The metrics **disagree** in their quantification of sharing, and the disagreement traces to **anisotropy** (representations clustering in a narrow cone of embedding space). Only ILO's correlation with cross-lingual transfer (Spearman ρ = 0.90) survives controls for model size, family, and per-task variation. The paper recommends ILO as the primary sharing metric, to be reported alongside anisotropy diagnostics.
- **Key Innovations**: Head-to-head arbitration of popular sharing metrics; identifies anisotropy as the confound driving metric disagreement; validated metric recommendation (ILO).
- **Venue**: Preprint

### 1.6 When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models
- **Authors**: Gnaneswar Villuri, Hashmath Shaik, Alex Doboli
- **Institution**: Stony Brook University (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04582
- **Abstract**: A 0.6B LM asked to verify 1,200 logical conclusions (half valid, half corrupted) answers YES to everything — judged by behavior it discriminates nothing, yet **linear probes on hidden states read the correct verdict at 0.96 AUC** (0.90 on foils built from the true conclusion's own words). The dominant failure is a single scalar: the verdict survives to the output logits (margin AUC 0.89) along a well-aligned readout, but a **saturated decision threshold offset by +4.6σ** erases it. The diagnosis generalizes across a 90-config five-model/three-family factorial (behavioral accuracy collapses onto threshold offset, Spearman −0.93), and across a 13× scale range internal knowledge saturates while free-form behavior stays non-monotone (an 8B underperforms its 4B sibling via answer-channel failure). A one-parameter correction repairs behavior from 50%→81% (0.6B); calibrated margin decoding recovers 94% at 8B; few-shot prompting works by recentering the threshold. Comparing probe vs margin separates three regimes: **concealed, miscalibrated, undetected**.
- **Key Innovations**: Precise decomposition of "behavior-concealed knowledge" into readout miscalibration vs. undetected absence; one-parameter behavioral repair; probe-vs-margin regime taxonomy reused as an audit test.
- **Venue**: Preprint

---

## 2. LLMs — Reasoning, Post-Training & Reward Design

### 2.1 ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying
- **Authors**: Shi-Qi Yan, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Zhen-Hua Ling
- **Institution**: USTC / Huawei (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04648
- **Abstract**: GRPO-style RL uses only final-answer (outcome) rewards, which become increasingly sparse as trajectories lengthen. **ConsensusBench** supplies rule-based *process-level* signals: a correct final answer relies on a small set of intermediate conclusions, treated as verifiable sub-outcomes. The authors extract them by filtering correct trajectories from N rollouts and clustering semantically equivalent intermediate statements into **Consensus Nodes**, then fold the derived rule-based process reward into GRPO as **ConsensusPR**, directly reducing outcome-reward sparsity. Three new metrics (Final Answer Accuracy, Node Coverage Rate, Tokens per Node) support process-level evaluation. ConsensusPR consistently beats GRPO-style baselines on AIME 2024/2025, GSM8K, MATH-500 and ConsensusBench itself.
- **Key Innovations**: Consensus-node construction = data-free, rule-based process supervision (no trained reward model); outcome-reward densifying for GRPO; dedicated process-level benchmark + metrics.
- **Venue**: Preprint

### 2.2 Towards Understanding Pause Token Fine-Tuning Dynamics: A Mode Retention Perspective
- **Authors**: Jaehyeon Kim, Suhwan Kim, Nakyung Lee, Yeongoon Kim, Jimin Seo, Giho Lee, Jungwoo Lee
- **Institution**: Seoul National University (tentative)
- **Date**: 2026-09-03
- **arXiv**: https://arxiv.org/abs/2609.04489
- **Abstract**: Pause-token gains are usually explained by computational expressivity; this paper studies their **training dynamics**. Two controlled pilots expose asymmetries: on a synthetic continual-learning task, masked pause tokens overwrite a previously-learned distribution ~4× less at matched final adaptation (mode retention); on a synthetic math probe, the boundary-adjacent token comes to encode substantially more downstream-step information (non-myopic compression). The authors formalize **Masked Boundary Pause (MBP)** — pause tokens at reasoning-step boundaries with masked loss — and show it consistently improves reasoning across 1B–8B Qwen/Llama models (+ up to 6 points math, +2.5 code) while preserving general understanding, and that the gains extend to GRPO.
- **Key Innovations**: Recasts pause tokens as a **training-dynamics intervention on the retention–adaptation tradeoff**, not an inference compute device; MBP recipe; GRPO compatibility.
- **Venue**: Preprint

### 2.3 A Verifier-Guided Explainable Reasoning Framework with Gold-Anchored QLoRA, Task-Aware Mixture-of-Experts, and Group-Relative RLVR
- **Authors**: Thi Kim Trang Vo, Nam Tien Le, Thi Kim Nguyet Vo, Minh Khang Tran, Duy Phuong Tran
- **Institution**: Vietnamese academic (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05221
- **Abstract**: A verifier-guided explainable-reasoning pipeline for transparent educational QA: Qwen2.5-3B-Instruct is adapted with gold-anchored QLoRA; a lightweight router sends logic problems to a FOL/Z3 verifier and physics problems to a formula/unit-aware symbolic solver; verifier feedback is reused for candidate evaluation, self-revision, and **RLVR reward construction**. Responses are scored on three axes — P1 answer correctness, P2 evidence/unit consistency, P3 reasoning depth/explainability. On 438 held-out examples, RLVR lifts P3 from 50.68%→72.20% while hybrid P1 stays ~55.94%; gold-free self-consistency contributes the neural-side P1 gain (48.86→50.23%) and symbolic verification the rest. Conclusion: **RLVR strengthens explicit reasoning structure; symbolic verification complements the neural policy at system level.**
- **Key Innovations**: Verifier-derived rewards inside group-relative RLVR (neuro-symbolic reward construction); three-axis evaluation separating structure from correctness; task-aware routing (FOL/Z3 vs physics solver).
- **Venue**: Preprint

---

## 3. LLMs — Calibration, Safety & Alignment

### 3.1 Single-Query Black-Box Calibration Auditing via Logit Bias
- **Authors**: Roman Plaud, Antoine Saillenfest, Matthieu Labeau, Thomas Bonald, Willem Waegeman
- **Institution**: Télécom Paris / Ghent University (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05125
- **Abstract**: Commercial API providers increasingly hide the continuous probabilities that standard calibration metrics need. The authors show that any LLM API exposing a `logit_bias` parameter can be **mathematically manipulated to evaluate exact probability thresholds with strictly one query per sample**, enabling a provably consistent estimator of the True Calibration Error for binary tasks — an efficient framework for auditing black-box foundation models.
- **Key Innovations**: Uses `logit_bias` as an *exact probability oracle* (a subtle and safe API surface); single-query TCE estimation; first calibration audit that works against opaque APIs.
- **Venue**: Preprint

### 3.2 Refuse without Refusal: A Structural Analysis of Safety-Tuning Responses for Reducing False Refusals in Language Models
- **Authors**: Minji Kim, Hyounghun Kim
- **Institution**: UNIST (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04714
- **Abstract**: Models must refuse harmful queries ("How do I shoot someone?") yet answer benign lookalikes ("Where can I shoot a good photo?"), but false refusals persist. The paper **decomposes each safety-tuning response into a boilerplate refusal statement + a rationale**, and shows the refusal boilerplate *impedes* harmful/benign discrimination by training reliance on superficial cues, while **rationale-only training reduces false refusals while maintaining comparable safety**. Rationale-only benefits also transfer to ICL and remain compatible with inference-time mitigation methods.
- **Key Innovations**: Causal (structural) analysis of SFT supervision syntax, not just content; rationale-only training recipe; complements the 09-07 bailiwick of steering-based refusal work (§3.3) from the supervision side.
- **Venue**: EMNLP 2026 Main Conference

### 3.3 Locating and Steering Refusal Beyond Attention
- **Authors**: Preethi Carmel Bosco, Gopalakrishnan Srinivasan
- **Institution**: Syracuse University (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04721
- **Abstract**: Refusal in transformers lives in a single residual-stream direction. State-space models (SSMs) share no token-mixing mechanism with attention — does the safety representation survive? **It does.** A single rigid rotation (which can reorient but not reshape) aligns one model's representation space to another's so the two genuinely share the representation: a harm probe trained on a transformer flags an SSM's harmful inputs, and removing the aligned direction makes a model answer attacks it would otherwise refuse. What is architecture-specific is not *where the direction is steered* but *where it must be read* — harm is cleanly readable at the write site (layer output, before residual addition). A detector-triggered gate lowers jailbreak success across all four architecture families tested (SSM, transformer, recurrent, hybrid), and on the SSM it holds against a prompt-tuned attacker. Safety tooling therefore **ports to a new architecture by re-estimating the direction at that architecture's write site**, not by rebuilding it.
- **Key Innovations**: First cross-architecture refusal-direction transfer via alignment rotation; write-site vs read-site distinction; four-family jailbreak defense with a tuned-adversary robustness result.
- **Venue**: Preprint

---

## 4. Agents & Agentic Training

### 4.1 Persistent Teacher Anchoring for Tool-Using Agents
- **Authors**: Hyun Bin Park (Sogang University), Kyungho Song (University of Michigan), Sangmin Lee, Du-Seong Chang (Sogang University)
- **Institution**: Sogang University / University of Michigan
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04773
- **Abstract**: In on-policy knowledge distillation (OPKD), the student matches the teacher's next-token distribution; in tool use this is dangerous because **student-written calls execute before supervision**, so teacher–student distribution gap accumulates as rollouts enter states the teacher would not visit. Proposer-verifier generation governs text but leaves tool execution out of scope. **Persistent Teacher Anchoring (PTA)** is a student-induced but *teacher-committed* rollout construction: chunk-level verification plus **turn-level commitment** (a call reaches the environment only after the teacher verifies the entire turn). Treating verified chunks as atomic generation units enables **persistent lookahead**, which fills idle rollout capacity. Across Search-R1-style retrieval and DeepEyes-style perception RL, PTA before downstream RL improves macro best@4 by **2.5/2.8 points over OPKD under the same downstream RL budget**, with +24% throughput from lookahead.
- **Key Innovations**: Teacher-committed tool execution (extending proposer-verifier to the environment action loop); persistent lookahead recycling idle rollout capacity; EMNLP-main-grade evidence on two RL settings.
- **Venue**: EMNLP 2026 Main Conference

### 4.2 Rhythms of Work: Multi-Scale Interpretation of Human Behavioral Traces for Workplace Agents
- **Authors**: Lin Ai, Scott Counts
- **Institution**: Microsoft Research (tentative — Scott Counts)
- **Date**: 2026-09-03
- **arXiv**: https://arxiv.org/abs/2609.04556
- **Abstract**: Workplace agents must interpret the *human* activity around them from low-level event traces, but flattening a trace into one stream or one embedding assumes a single correct summary. The authors argue **behavioral interpretation is resolution-dependent** and build a multi-resolution vocabulary of semantically normalized operators, recurring motifs, coherent episodes, and day-level rhythms. Applied to **667M human-attributed events** from a commercial productivity suite (50,000 users, 100 organizations), it yields 120 operator types, thousands of motifs, 25 episode types, and 5 day-rhythm archetypes. Re-running on a disjoint 2,000-user sample reproduces the taxonomy (structural stability); on held-out users the representation beats a flat-operator baseline at next-episode forecasting (+17% relative macro-F1), and a resolution ablation shows **no single level is optimal across questions** — interpretation should be multi-resolution and query-conditioned.
- **Key Innovations**: Multi-resolution (not just hierarchical) behavioral trace vocabulary for human-side agent context; stability+validity validation at unprecedented scale; query-conditioned grain selection as design principle.
- **Venue**: Preprint

---

## 5. Efficient Inference & Edge Deployment

### 5.1 Deep Microcompression: Structured Pruning and Bit-packed Quantization for Microcontrollers
- **Authors**: Opegbemi Matthias Busoye, Tolulope Matthew Busoye, Eghonghon-aye Eigbe
- **Institution**: Academic (Global South)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05081
- **Abstract**: A hardware-aware pipeline for bare-metal microcontrollers combining structured pruning, quantization-aware training, and fixed-length bit-packing to reach a **55.8× weight compression ratio on LeNet-5 (98.77% accuracy)** while emitting a dependency-free C library with deterministic latency. On the RP2040 (Cortex-M0+) the binary is 3× smaller than TensorFlow Lite at matched accuracy, and it enables the **first documented deployment of a standard CNN on the ATmega328P (2 KB SRAM)** — previously considered infeasible.
- **Key Innovations**: 55.8× compression with deterministic-latency, dependency-free deployment; pushes CNN inference into 2 KB SRAM class devices.
- **Venue**: Global South ML Workshop @ ICML 2026

### 5.2 From Deep to Shallow: Unconstrained and Efficient Layer Merging Strategy
- **Authors**: Petro Shulzhenko, Gabriele Spadaro, Enzo Tartaglione
- **Institution**: Politecnico di Torino (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.04881
- **Abstract**: Depth compression linearizes redundant activation functions so adjacent layers can be merged; prior methods cannot handle **convolutions with padding** (no analytical merge solution) and typically **grow the kernel size**, capping speedup. The proposed strategy merges layers without an analytical solution *and* without increasing kernel size; it is validated across multiple architectures/datasets with inference speedups measured on real embedded platforms.
- **Key Innovations**: Padding-safe, kernel-size-preserving layer merging; extends depth-compression to the common padded-convolution case; embedded-platform speedup measurements.
- **Venue**: ITEM Workshop @ ECML PKDD 2026

---

## 6. Games & Game Theory

### 6.1 Cutting Down the Tower: Single-Exponential Envy-Free Cake Cutting
- **Authors**: Qilin Ye, Yannan Bai
- **Institution**: Academic (tentative)
- **Date**: 2026-09-04
- **arXiv**: https://arxiv.org/abs/2609.05191
- **Abstract**: Envy-free cake cutting has a striking existence-vs-computation divide: topology guarantees envy-free allocations exist, but efficient protocols resisted decades of work. Aziz–Mackenzie gave query bound n^(n^(n^(n^(n^n)))); Sokolov improved to n^(8n²(1+o(1))); the general lower bound (Procaccia) is just Ω(n²). This work **closes much of the gap** with a protocol using at most **n^{O(1)}·2^n queries**: repeatedly allocate cake without creating envy until the residual problem has fewer agents, held together by a new construction using only *polynomially many partial allocations* (replacing the n^(n^(n^n)) used previously) so no cake is assigned twice and no envy is created on assembly. First single-exponential query bound for complete envy-free allocations under arbitrary nonatomic additive valuations.
- **Key Innovations**: First single-exponential envy-free protocol; polynomial-size partial-allocation construction; massive tightening of the Aziz–Mackenzie/Sokolov tower.
- **Venue**: Preprint

> No new **game-RL / game-AI** papers surfaced in this second pass that the 09-05 game-rl-daily and 09-07 digests did not already sweep (cs.GT Mon 7 Sep = 9 entries, of which 6 were already featured or cross-list duplicates; the three remaining — 2609.05191 cake cutting featured above, plus Hare-core results 2609.04537 / 2609.04497 — are pure social-choice theory).

---

## Summary Statistics

| Category | Papers Count |
|---|---|
| LLMs — Mechanistic Interpretation & Representational Geometry | 6 |
| LLMs — Reasoning, Post-Training & Reward Design | 3 |
| LLMs — Calibration, Safety & Alignment | 3 |
| Agents & Agentic Training | 2 |
| Efficient Inference & Edge Deployment | 2 |
| Games & Game Theory | 1 |
| **Total (this report)** | **17** |
| Overlaps with 09-07 [[arxiv-daily]] / [[arxiv-ai-search]] (both 2026-09-07) | 0 featured (2 screened-out already-covered: 2609.05152, 2609.04526) |
| Overlaps with 09-08 [[arxiv-paper-check]] | 0 featured |

## Key Trends

1. **Interpretability is generalizing beyond the attention transformer.** Refusal directions transfer across SSM/transformer/recurrent/hybrid via alignment rotation (2609.04721); susceptibility analysis is proved to work on plain Turing machines (2609.04661); mHC residual routing is dissected on DeepSeek-V4-Flash (2609.05309). The recurring message: **tooling portability = re-estimate the direction at the target architecture's write site, don't rebuild it.**

2. **"The model knows; the readout fails" is becoming a testable taxonomy.** 2609.04582's concealed/miscalibrated/undetected regimes unify probing results with calibration-auditing work (2609.05125): both treat readout quality — not knowledge — as the thing to fix or audit, and both exploit previously-ignored API/decoding surfaces (margin, `logit_bias`).

3. **Reasoning post-training is pivoting from outcome to *process-level* supervision.** Consensus nodes extracted from rollout clusters (2609.04648), masked-boundary pause tokens on the retention–adaptation axis (2609.04489), and verifier-grounded RLVR rewards (2609.05221) all attack sparse, opaque outcome rewards — the same pressure that drove GRPO/PRIME-type lines in this wiki's RL digests.

4. **Safety supervision is being decomposed rather than layered.** 2609.04714 surgically separates refusal boilerplate from rationale in SFT data and keeps only the rationale; paired with the steering work (§3.3), safety is being reworked at both the *supervision* and *intervention* levels instead of stacked.

5. **Agent-training data pipelines are getting their own control.** PTA makes the teacher *commit* to tool executions (2609.04773); 2609.04556 makes human-trace interpretation resolution-conditional. Both push agent training/eval away from "one universal summary" toward structured, verifiable, query-conditioned data.

6. **Edge efficiency keeps pushing constraint boundaries.** 55.8× compressed CNNs on 2 KB SRAM microcontrollers (2609.05081) and padding-safe, kernel-size-preserving layer merging (2609.04881) shrink the floor of where learned models can run — relevant to the offline/on-device rec-and-edge lines elsewhere in this wiki.

7. **Rec/CTR/ads second pass was quiet by design**: the cs.IR Mon 7 Sep mailing was fully mined on 09-07, and this report's only rec-domain-adjacent fresh entry is the Huawei mHC study (2609.05309). Expect new cs.IR material with the Tue 8 Sep 2026 listing.