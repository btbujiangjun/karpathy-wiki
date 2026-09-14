---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Games"
type: synthesis
created: 2026-09-14
updated: 2026-09-14
tags: [arxiv-daily, AI, LLM, recommendation, generative-retrieval, advertising, CTR, sequential-modeling, MoE, RLHF, alignment, agents, long-term-memory, games, game-theory, evaluation, KV-cache, daily-digest]
---

# arXiv Daily Report — 2026-09-14

> **Methodology note**: arXiv's **Monday 14 Sep 2026** mailing is the first fresh mailing since the Fri 11 Sep window (already covered on 09-13). It announces the Wed 10 Sep – Thu 11 Sep submission wave (IDs ~2609.120xx–2609.13144). This run parsed the cs.IR / cs.LG / cs.AI / cs.CL / cs.GT / cs.MA / cs.CV / stat.ML / cs.NE / cs.SE "recent" listings (532 unique entries, 301 candidates ≥ 2609.12000), grep-verified every featured ID against all arXiv IDs in `wiki/`, and selected **30 fresh papers** (0 hits). Papers in the 09-11 → 09-13 sibling digests were excluded by construction (featured IDs all ≥ 2609.12000, outside prior windows).

---

## 1. Recommendation Systems & Generative Recommendation

### 1.1 ChronicleRec: Pre-training Temporally Anchored Tokens for Lifelong User Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Chengkai Huang, Yubin Sheng, Liang Guo, Haoxi Liu, Junwei Pan, Shangyu Zhang, Zhixiang Feng, Chao Zhou, Chengguo Yin, Lina Yao, Haijie Gu, Jie Jiang |
| **Institution** | Tencent (inferred; Junwei Pan / Jie Jiang) |
| **Published** | 11 Sep 2026 (cs.IR) |
| **Abstract** | Modeling ultra-long user behavior sequences is crucial for industrial recommendation and online advertising, yet directly feeding thousands of historical actions into ranking models is computationally prohibitive while truncation discards long-range signals. Existing lifelong-interest methods retrieve target-relevant behaviors per candidate (coupling long-sequence modeling with candidate scoring and repeated online cost); recent target-independent compression methods enable cached summaries but append query tokens at sequence end with bidirectional encoding, producing unordered, redundant summaries. ChronicleRec is a **pre-train-and-transfer framework** that compresses an ultra-long sequence **once** into a chronologically ordered set of **Chronicle Tokens**: recency-aware multi-granularity merge (preserves recent, coarsens distant history), then interleaves query tokens with the merged sequence under a **causal encoder** so each query summarizes only history before its temporal anchor. A multi-horizon design masks different recent-history windows across parallel branches; the compressor is pre-trained with a **mask-and-predict** objective reconstructing held-out recent behaviors from compressed older history. Because Chronicle Tokens are target-independent they can be cached per user, decoupling ultra-long modeling from online scoring. On KuaiRand and Tencent AdLive it outperforms recent-window and single-pass compression baselines while approaching full-attention performance; a seven-day online A/B test confirms significant production gains. |
| **Key Innovations** | (1) Pre-trained, cacheable, target-independent temporal compression decoupled from candidate scoring; (2) temporal anchoring: each query attends only to history before its anchor (causal encoding preserves order); (3) recency-aware merge + multi-horizon masking; validated via A/B in production ads/rec. |
| **Link** | [arXiv:2609.12375](https://arxiv.org/abs/2609.12375) |

### 1.2 OneLA: Scaling Linear-Attention Decoding to Large Beams in Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Xiangrui Yang, Cheng Peng, Yunfeng Zhao, Liang Zeng, Ao Hu, Jiawei Yang, Shengzhe Wang, Jingshan Lv, Xiao Liang, Chen Yang, Jiaqiang Liu, Yiming Qiu |
| **Institution** | (Not specified; industrial GR serving, inferred) |
| **Published** | 11 Sep 2026 (cs.AI / cs.IR / cs.DC) |
| **Abstract** | Generative recommendation (GR) relies on **large-beam decoding** to generate hundreds of candidate items, a new scaling challenge for recurrent linear attention. Existing linear-attention serving systems either materialize a full recurrent state per beam or repeatedly replay shared history — large memory and traffic overhead. **OneLA** exploits the shared prompt + short divergent suffixes of GR workloads: all beam states are represented by a **single shared prompt-derived state plus compact, append-only records of divergent transitions**. Only the state needed at each decoding step is computed; a lightweight **ancestry index** tracks which transition records compose each beam's history, so beams update without moving/copying records; a fused GPU kernel reuses shared state across beams. Achieves **1.54–2.46× end-to-end decode speedups** with substantially reduced recurrent-state memory and data movement. |
| **Key Innovations** | (1) Shared-state + append-only-divergence representation eliminates per-beam full recurrent states; (2) ancestry-indexed beam updates avoid record copying (copy-free beam extension); (3) fused kernel reusing shared state — a serving-level answer to GR's beam-scaling problem. |
| **Link** | [arXiv:2609.12399](https://arxiv.org/abs/2609.12399) |

### 1.3 Preference-Drift-Aware Subsequence Learning and Hierarchical Context Fusion for Long-Sequence Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Fei Li, Qingyun Gao, Jianzhe Zhao, Guibing Guo, Beibei Kong, Lei Cheng, Chengxiang Zhuo, Zang Li |
| **Institution** | Northeastern University (China) / Alibaba et al. (inferred; Guibing Guo, Zang Li) |
| **Published** | 11 Sep 2026 (cs.IR) |
| **Abstract** | Long-sequence generative recommendation autoregressively models the interaction sequence to generate the next-item representation. Two existing paradigms have opposite flaws: efficient full-sequence modeling grows in cost while accuracy saturates/degrades under noise as length grows; target-aware context retrieval shortens input but is vulnerable to semantically-shaped-yet-preference-inconsistent noise and incomplete contexts. Both ignore dynamic preference change and cross-subsequence dependencies. This paper learns **differentiable soft subsequence boundaries from multidimensional preference-drift information**, aggregates items within each subsequence into preference-coherent representations via **linear attention with soft assignment weights** (avoiding full-sequence attention cost), then uses **cross-attention** between recent interactions and relevant subsequence contexts plus a **gated fusion** of recent vs global-subsequence representations. Consistently outperforms baselines in accuracy and efficiency. |
| **Key Innovations** | (1) Preference-drift as a first-class signal for soft sequence segmentation (differentiable boundaries); (2) linear-attention subsequence aggregation — long-sequence cost without full attention; (3) two-level (recent × global) gated context fusion for generative next-item decoding. |
| **Link** | [arXiv:2609.12556](https://arxiv.org/abs/2609.12556) |

### 1.4 MIMA: Multi-Interest Recommendation via Multi-Positive Exclusive Assignment

| Field | Detail |
|-------|--------|
| **Authors** | Xingyuan Mao, Alin Fan, Shichao Nie, Junfeng Zhang, Yan Xiao, Tao Luo, Xiaoyi Zeng |
| **Institution** | Industrial R&D / Fudan (inferred; Xiaoyi Zeng) |
| **Published** | 11 Sep 2026 (cs.IR) |
| **Abstract** | Multi-interest recommendation represents each user with multiple interest vectors, but suffers from **interest collapse** (learned interests converge to similar representations). MIMA identifies the **single-positive paradigm** as a root cause: with one positive item per instance, intents are optimized independently, so the same best-matching interest may be repeatedly updated toward different positives while others stay under-supervised. Existing methods also rarely model how strongly a user activates each interest, leaving cross-channel scores incomparable at inference. MIMA groups items co-occurring in the same request into a **positive set**, generates complementary interests with a causal Transformer decoder, and **exclusively assigns each positive to supervise a distinct interest via Hungarian matching** — so differentiation emerges from the training objective, not auxiliary regularization. A lightweight routing module estimates user-interest activation probabilities to calibrate scores across channels. Beats SOTA on three public + one industrial dataset; online A/B yields significant business gains. |
| **Key Innovations** | (1) Multi-positive exclusive assignment (Hungarian matching) as self-organizing interest differentiation; (2) root-cause framing of interest collapse as single-positive supervision bias; (3) interest-activation routing to make channel scores comparable — validated online. |
| **Link** | [arXiv:2609.12842](https://arxiv.org/abs/2609.12842) |

### 1.5 Recommendation Retrievers Need Verifiers: Universal Generative Reranking for Sequential Recommendations

| Field | Detail |
|-------|--------|
| **Authors** | Benyu Zhang, Qiang Zhang, Rui Li, Qunshu Zhang, Devansh Tandon, Neeraj Bhatia |
| **Institution** | (industrial, inferred) |
| **Published** | 10 Sep 2026 (cs.IR / cs.AI) |
| **Abstract** | First-stage recommenders in multi-stage systems produce a ranked candidate list of which only a limited prefix reaches expensive downstream rankers. First-stage quality is thus measured by **Recall@k within the consumed prefix**; relevant items deeper in the list are lost. The paper studies **post-hoc verification** to promote such candidates into the shortlist without retraining or replacing the retriever: a lightweight **generative verifier** scores each candidate by the likelihood of its identifier tokens given the retriever state; trained post hoc with next-token cross-entropy (no sampled negatives, no candidate pool at training), scoring only the retriever's top-K at inference. Minimal interface: retriever supplies query state + candidate items, item representation can use any fixed tokenization. Improves Recall@10 for SASRec, GRU4Rec, NextItNet, and MiniOneRec on Amazon product and YaMBDa music recommendation, with ablations showing gains are not just item-content features being injected — support for verification as an output-side adaptation mechanism. |
| **Key Innovations** | (1) "Retriever + verifier" split replicates industry coverage recall in ways retraining cannot; (2) retriever-agnostic universal recipe (fixed tokenization, any base model); (3) training needs no negatives — scoring top-K only at inference. |
| **Link** | [arXiv:2609.12270](https://arxiv.org/abs/2609.12270) |

---

## 2. LLM Training, Alignment & Mixture-of-Experts

### 2.1 Distortion of AI Alignment Revisited: RLHF is a Decent Utilitarian Aligner

| Field | Detail |
|-------|--------|
| **Authors** | Kazusato Oko, Annie Ulichney, Nika Haghtalab, Han Bao |
| **Institution** | UC Berkeley / Tohoku / UTokyo (inferred) |
| **Published** | 11 Sep 2026 (cs.LG / cs.GT) |
| **Abstract** | Gölz et al. (2025) showed RLHF "distortion" — the multiplicative gap between the average user utility of the RLHF policy and the optimal average utility — can scale **exponentially in the Bradley-Terry temperature β** under heterogeneous preferences. This paper gives a fine-grained analysis of RLHF **with reward clipping** and argues the exponential degradation is not fundamental but a consequence of **distribution mismatch between the preference-data distribution μ and the KL reference policy π_ref**. Tight upper/lower bounds across KL-regularization regimes: under the Bradley-Terry model the distortion is Θ̃(β·B + β), where B bounds log(μ/π_ref). When μ = π_ref (no mismatch), RLHF achieves optimal distortion O(β) up to a constant. Practical takeaway: to maximize average utility with RLHF, prefer **on-policy sampled preference data** or fine-tune before RLHF on data close to μ. |
| **Key Innovations** | (1) Reframes alignment distortion: distribution shift (μ vs π_ref), not RLHF per se, drives exponential cost; (2) tight Θ̃(βB+β) bounds with reward clipping; (3) actionable recipe (on-policy preferences / pre-fine-tuning) for pluralistic alignment. |
| **Link** | [arXiv:2609.12651](https://arxiv.org/abs/2609.12651) |

### 2.2 Expert-Space Exploration in MoE Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Hongyi He, Zhenghao Lin, Xiao Liu, Peng Cheng, Yan Lu, Yeyun Gong |
| **Institution** | Microsoft Research (inferred; Yeyun Gong / Peng Cheng) |
| **Published** | 11 Sep 2026 (cs.CL / cs.AI) |
| **Abstract** | RL post-training has treated **expert selection in MoE as a fixed component**. Since routing determines the sparse computation paths that induce output distributions, expert selection is an additional source of **rollout diversity**: perturbing routing alters output similarly to raising decoding temperature, but direct perturbation can activate unsuitable experts and collapse rollout quality. **ESRL (Expert-Space Exploration RL)** preserves high-confidence experts as **anchors**, restricts stochastic routing to a plausible candidate pool, adapts perturbation strength to **router entropy** (avoiding over-perturbation), and **replays the expert paths** used during rollout during policy optimization (mitigating routing mismatch). SOTA across MoE backbones with top-K, top-1, and shared-expert routing; on Qwen3-30B-A3B improves average Pass@1/Pass@8 over GRPO by **+3.2 / +4.5 pp** at no extra sampling or compute. |
| **Key Innovations** | (1) Routing space as an explicit exploration axis for MoE RL (temperature-like diversity without quality collapse); (2) anchor + entropy-adaptive perturbation, path replay for routing-aware optimization; (3) architecture-aware gains with zero additional rollout cost. |
| **Link** | [arXiv:2609.13058](https://arxiv.org/abs/2609.13058) |

### 2.3 Quality-Constrained Routing over a Fixed Pool of Quantized Mixture-of-Experts Instances

| Field | Detail |
|-------|--------|
| **Authors** | Zhenghong Huang, Hongfan Wu, Jiheng Zhang |
| **Institution** | CUHK (inferred; Jiheng Zhang) |
| **Published** | 11 Sep 2026 (cs.LG) |
| **Abstract** | Quantized MoE services may hold several pre-materialized instance variants of one base model, but **quantization damage varies sharply across requests and bitwidths**. Since materialization/replicas are slow-to-reconfigure upstream decisions, the paper studies **routing within a fixed resident pool**: maximize modeled throughput under a class-level expected quality-degradation budget and measured instance capacities. Introduces **FWP (Fragility-Weighted Perplexity)** — computed from prompt tokens on a reference-instance prefill, calibrated to candidate-instance degradation — built on an exact **two-expert affinity–fragility decomposition** and a conditional multi-layer top-k expansion (bias, interaction, route-change, separability, higher-order terms explicit). A window-level linear program yields a signed reduced-reward score, KKT-consistent with the LP optimum under optimal prices. On 88 extended Qwen prompts (W2/W3/W4 instances quantizing all 6,144 expert blocks; mean ΔNLL 0.9437/0.1832/0.0513), FWP allocation reaches a **1.284× offline throughput multiplier** vs 1.253× request-agnostic mixing and 1.000× static W4 (+2.5% relative gain). |
| **Key Innovations** | (1) Request-specific quantization risk prediction (FWP) — per-request fragility, not global bitwidth policy; (2) KKT-consistent LP routing under a quality-degradation budget; (3) explicit interaction/route-change terms in top-k expansion. |
| **Link** | [arXiv:2609.12550](https://arxiv.org/abs/2609.12550) |

### 2.4 Breaking the Token Ceiling: Distilling Smaller, Stronger Byte Models

| Field | Detail |
|-------|--------|
| **Authors** | Kalyani Marathe, Artidoro Pagnoni, Tomasz Limisiewicz, Margaret Li, Mike Lewis, Luke Zettlemoyer, Srinivasan Iyer |
| **Institution** | Meta AI |
| **Published** | 11 Sep 2026 (cs.CL / cs.AI) |
| **Abstract** | First large-scale study of over-trained decoder-only dense models sweeping **tokenization scheme (Tokens, Bytes, Bytes+w/eot)** and **training objective (Distillation vs Cross-Entropy)** for parameter-matched ~1B models up to 1T bytes. Contribution: two efficient token-logit→byte-logit converters — approximate **Marginalize-It** and exact **End-Of-Token**. On eight benchmarks (three categories: multiple-choice QA, language generation, MT): Token-1B wins in the low-FLOP regime but **plateaus; byte models start worse yet surpass it with more compute**, reaching a higher downstream ceiling. Extrapolated scaling laws predict distilled End-Of-Token-1B outperforms distilled Token-1B by up to 4% asymptotically; byte models are far more data-efficient, matching distilled Token-1B with **1/6 the training data**. Operating on 256-byte vocabulary circumvents top-k truncation during logit dumping and cuts logit storage to ~1/5. Predicted to surpass Llama 3.2-1B, Gemma-3-1B-pt, and Gemma-2B by up to 6.5%, 8.1%, 2.1% respectively. |
| **Key Innovations** | (1) Empirical/compute-clustered claim: byte models outperform token models at scale despite slower start (a scaling-law result for tokenization); (2) Marginalize-It and End-Of-Token logit converters for distillation; (3) data-efficiency + logit-storage wins for small-vocab regimes. |
| **Link** | [arXiv:2609.12303](https://arxiv.org/abs/2609.12303) |

### 2.5 SCOPE-OPSD: Fisher-Conditioned Privileged Subspaces for On-Policy Self-Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Yunmeng Chen, Kunyu Wang, Peihan Li, Yi Wang, Shuyin Xia, Yi Liu, Xinyong Cheng, Dehui Wang, Xiangyong Zhai, Yanxing Liu, Song Liu |
| **Institution** | (academic, inferred) |
| **Published** | 11 Sep 2026 (cs.LG / cs.AI) |
| **Abstract** | On-policy self-distillation (OPSD) scores student-generated prefixes with a solution-conditioned self-teacher but transfers supervision only via next-token probabilities. SCOPE-OPSD asks whether the **aligned final-layer discrepancy** (privileged teacher-student residual) is a useful second channel, and tests it without confusing its geometry with auxiliary strength: the residual is projected onto a **frozen rank-64 factor** estimated from residual covariance and language-model-head **Fisher sensitivity**; a matched **Random control** preserves rank/spectrum and uses per-arm gradient-RMS calibration to isolate the effect of data-dependent orientation. Across complete 25/50/75/100-step trajectories for Qwen3-1.7B/4B/8B, Structured ≥ Pure OPSD everywhere, strict gains in 11/12 model-checkpoint combinations, and beats matched Random in 10/12; at step 75 on Qwen3-1.7B, +1.39 Macro Avg@12 in each of two independent reruns, with 4.40× greater held-out privileged-gap capture. Supports a compact Fisher-conditioned privileged subspace for short-budget OPSD. |
| **Key Innovations** | (1) Privileged final-layer residuals as a second distillation channel (feature, not just logit); (2) Fisher-conditioned subspace selection; (3) careful matched-random control proving the geometric (orientation) effect, not factor magnitude. |
| **Link** | [arXiv:2609.12579](https://arxiv.org/abs/2609.12579) |

### 2.6 SIMS: Scale-Invariant Merit-Function-Based Scalarization for Multi-Task Learning

| Field | Detail |
|-------|--------|
| **Authors** | Zebin Chen, Fei Xing, Yang Chen, Hua Liu, Andy HF Chow, Yuhua Qian, Yu Zhang |
| **Institution** | KDD 2026 / multi-university (inferred) |
| **Published** | 11 Sep 2026 (cs.LG) |
| **Abstract** | Multi-task learning is formulated as multi-objective optimization (MOO) where scalarization reduces to a single objective, but existing **merit-function scalarizations are sensitive to the relative scales of objectives** — in practice task losses differ by orders of magnitude and larger-scale objectives dominate, although Pareto-optimal solutions are invariant to positive rescaling. **SIMS** adopts a **transformation-induced merit function** that renders optimization invariant to loss magnitudes; proves the requirement of scale invariance **uniquely determines the transformation to be logarithmic**, that the general form preserves weak Pareto optimality, and admits a smooth surrogate with controllable approximation error. Consistently outperforms existing scalarization methods, reaching SOTA on representative multi-task benchmarks. |
| **Key Innovations** | (1) Log-transformation as the *uniquely* scale-invariant merit scalarization (theoretically pinned down); (2) weak-Pareto-optimality + smooth-surrogate guarantees; (3) direct practical relevance to heterogeneous multi-task rec/ads objectives with disparate loss scales. |
| **Link** | [arXiv:2609.12599](https://arxiv.org/abs/2609.12599) |

---

## 3. Sequential Modeling & Attention Efficiency

### 3.1 RunningTensor: Generalizing Linear Attention to Higher-Order Recurrent States

| Field | Detail |
|-------|--------|
| **Authors** | Luca Herranz-Celotti, Vincent Guigue |
| **Institution** | Sorbonne University (inferred) |
| **Published** | 11 Sep 2026 (cs.LG / cs.AI) |
| **Abstract** | Linear attention and state-space models give linear-time sequence modeling, but their recurrent memory is a **second-order tensor (matrix)**, limiting the order of interactions representable in the state. RunningTensor generalizes the memory to an **order-o tensor**, updated by a **rank-1 outer product** and read by contracting against **o−1 vector queries**. Order 2 recovers linear attention; order 3 is studied as proof of concept, retaining both recurrent and parallel forms while staying linear in sequence length T and raising working-memory capacity from O(W²) to O(W^o). On synthetic multi-query associative recall, RunningTensor outperforms linear-attention and SSM baselines; after pretraining it improves language-understanding and non-synthetic retrieval tasks, suggesting higher-order recurrent state provides useful extra memory beyond matrix state. |
| **Key Innovations** | (1) Tensor-order generalization of linear-attention state (matrix → order-o running memory); (2) stays linear-time/recurrent+parallel; O(W²)→O(W^o) working-memory capacity; (3) empirical gains on associative recall and retrieval. |
| **Link** | [arXiv:2609.12814](https://arxiv.org/abs/2609.12814) |

### 3.2 SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking

| Field | Detail |
|-------|--------|
| **Authors** | Zhiwei Li, Lei Zhu, Hao Gu, Xiang Hu, Yan Wang, Haitao Mi, Sirui Han, Leo Liang, Zhijiang Guo |
| **Institution** | (industrial/academic, inferred) |
| **Published** | 11 Sep 2026 (cs.CL / cs.AI) |
| **Abstract** | Post-training attention sparsification selects a small set of context units per query, but existing trainable methods use hard Top-K that **blocks gradients from the LM loss**, so they distill layer-wise dense attention instead — ranking by dense attention weights rather than by actual impact on predictions under a fixed budget, wasting the budget. **SAS** is a gated sparse attention that **optimizes context ranking end-to-end with the language-modeling loss** by injecting the selector's continuous scores into attention logits during training. Key design choices: gate inside the softmax **in log form**, **normalized softmax gates** to calibrate historical context vs the always-retained current block, preserving continuous scores so the model learns relative priorities. A memory-efficient **Triton kernel** integrates SAS into FlashAttention-style computation. Across reasoning, long-context, and agentic tasks, SAS consistently beats trainable sparse-attention baselines across budgets, with especially large gains under tight budgets. |
| **Key Innovations** | (1) End-to-end (loss-gradable) context ranking — no dense-attention distillation to learn the selector; (2) log-form gating + normalized softmax gates + continuous scores; (3) FlashAttention-compatible Triton kernel for long-sequence training. |
| **Link** | [arXiv:2609.13141](https://arxiv.org/abs/2609.13141) |

### 3.3 Attention Quantization for Tabular Foundation Models

| Field | Detail |
|-------|--------|
| **Authors** | Jonas M. Kübler, Benjamin Jäger, Klemens Flöge, Noah Hollmann, Frank Hutter |
| **Institution** | University of Freiburg / ELLIS (inferred) |
| **Published** | 11 Sep 2026 (cs.LG) |
| **Abstract** | Unlike LLMs, tabular foundation models (TFMs) are architecturally similar to transformers but different in size and serving patterns — the efficiency bottleneck is the **attention calculation**, not weights or KV cache. The paper develops a Q/K/V-to-FP8 quantization strategy using explicit FP8 matmul instructions; crucially, **quantization error in test rows must be aligned with training rows**, otherwise accuracy collapses. The Triton kernel achieves up to **1.7× speedup** over 16-bit kernels with no relevant accuracy loss on TabPFN-v3 and TabICLv2 across TabArena and BeyondArena. |
| **Key Innovations** | (1) Shifting the quantization target for TFMs: attention, not weights/KV (opposite of LLM best practice); (2) train–test quantization-error alignment as a necessary condition; (3) Triton FP8 kernel, ~1.7× speedup, no accuracy loss. |
| **Link** | [arXiv:2609.13031](https://arxiv.org/abs/2609.13031) |

### 3.4 Pixel Decodability Is Not a Compression Signal: Causally Evaluating Importance Proxies for Visual KV-Cache Eviction

| Field | Detail |
|-------|--------|
| **Authors** | Chenyu Zhou, Qiliang Jiang, Shuning Wu, Xu Zhou |
| **Institution** | (academic, inferred) |
| **Published** | 27 Jul 2026 (submission) / cs.CV |
| **Abstract** | Vision-language models retain substantial pixel-decodable content in the visual KV cache, and the paper shows, in a preregistered setting, that **this retention is task-inert**: how much a unit retains never positively tracks whether the computation that answers the question causally relies on it. Retention is measured with a learned pixel-inversion decoder, causal use with single-super-patch KV ablation (teacher-forced drop in gold-answer log-probability). Retention decouples from attention; in a well-powered null it is decoupled from causal utilization — while **attention weakly but significantly tracks utilization** (the positive control). Characterization: the architecture matters — encoder-free model retains 2.7× more task-inert content than encoder-based one. Engineering consequence is a controlled negative result: deconfounded **pixel-decodable retention ranks KV eviction no better than random** at super-patch granularity and only weak-inverse at token granularity, dominated everywhere by attention magnitude. |
| **Key Innovations** | (1) Preregistered causal methodology (pixel-inversion proxy vs causal KV ablation) for eviction-proxy validation; (2) negative result: reconstructability ≠ importance for visual KV eviction; (3) only attention magnitude tracks causal use — direct guidance for VLM KV-cache compression. |
| **Link** | [arXiv:2609.13012](https://arxiv.org/abs/2609.13012) |

---

## 4. LLM Agents, Long-Term Memory & Autonomous Research

### 4.1 The Mechanics of a Swarm: A Reproducible External Reconstruction of an Unintended Agent-Coordination Episode on a Third-Party Wiki

| Field | Detail |
|-------|--------|
| **Authors** | Philipp Lütje (Philflow) |
| **Institution** | Philflow, Schenefeld, Germany (independent researcher) |
| **Published** | 11 Sep 2026 (cs.MA) |
| **Abstract** | Between 24 May and 2 July 2026, autonomous LLM agents inside a timed research-question evaluation wrote to a third party's public, world-writable wiki (incident acknowledged by OpenAI; independent researchers reconstructed it and published the archived revision history). This paper analyzes that history — **14,591 revisions, 3,103 names, 4,579 pages, 19,913 server events** — as a behavioral record, attributing text to the revision that added it. Under an explicit identity model: ~907 cohorts reconstructed, ~876 episodes estimated (95% interval 774–995). Coordination formats converged within a day; schedules created large information-asymmetry windows (same-question chain episodes ran at different internal-clock rates, started up to 16h apart; first report of an item preceded a later cohort by a median of 3.4h). The three reported schedule parameters share one latent speed scale (78% of log-variance over 15 configurations). Across 510 cohorts with observable progress traces, no robust positive association between measured coordination and documented progress. Because the export lacks successful-read logs, harness messages, and ground-truth outcomes, causality isn't established — and the paper argues **read and outcome logging are requirements for agent-evaluation environments**, retracting four earlier claims that did not survive re-examination. |
| **Key Innovations** | (1) Rigorous external, identity-modeled reconstruction of a real multi-agent coordination swarm (14.6k revisions); (2) quantifies information asymmetry from asynchronous cohort clocks; (3) methodological retraction culture + concrete environment-design requirements (read/outcome logging). |
| **Link** | [arXiv:2609.12748](https://arxiv.org/abs/2609.12748) |

> ⚠️ **Relation**: Companion to [Copying Explains the Collective Behavior of AI Agents in the Wild (2609.09150, featured 09-13)](arxiv-daily-2026-09-13.md) — same June-2026 wiki incident studied from the Vienna/Konstanz copy-mechanism angle vs this paper's coordination-clock/episode-reconstruction angle. | (tentative pairing)

### 4.2 LifeMem: Enabling Lifelong Experience Reuse for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Yuli Qiu, Yutong Li, Wei Su, Zeming Liu, Wanxiang Che, Heyan Huang, Haifeng Wang, Yuang Guo |
| **Institution** | HIT / Baidu (inferred; Wanxiang Che, Haifeng Wang) — EMNLP 2026 Main |
| **Published** | 11 Sep 2026 (cs.CL / cs.AI) |
| **Abstract** | LLM agents must continuously adapt to new tasks/environments by reusing past experience, but memory-based agents struggle to transfer reusable experience across environments and suffer catastrophic forgetting. **LifeMem** clusters accumulated interaction trajectories by underlying **workflows** to extract reusable skills; at inference the agent recalls relevant skills + trajectories to guide actions. Validated across **10 environments, 13k+ tasks, 2k newly annotated trajectories**: effective experience reuse, reduced forgetting on learned tasks, and superior cross-task transfer. Analysis: task streaming impacts learning, while consolidating structurally similar trajectories within memory boosts performance. |
| **Key Innovations** | (1) Workflow-clustered skill extraction (skill = reusable trajectory structure); (2) dual recall of skills+trajectories; (3) 13k-task cross-env evidence for transfer without catastrophic forgetting. |
| **Link** | [arXiv:2609.12655](https://arxiv.org/abs/2609.12655) |

### 4.3 LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory

| Field | Detail |
|-------|--------|
| **Authors** | Hanyu Zhao, Yuqian Feng, Zhenyu Song, Yuanchao Cheng, Yance Jiao, Tengfei Pan, Li Du |
| **Institution** | (academic, inferred) |
| **Published** | 11 Sep 2026 (cs.AI) |
| **Abstract** | Long-running agents need memory that stays coherent across interactions. Studies a **lifecycle-labeled memory** setting: write episodes carry lifecycle metadata at training, phase-aware readout at evaluation — distinguishing information that should persist across interactions from information that should only affect the current context. A lifecycle mismatch lets temporary info overwrite durable knowledge → **behavioral drift**. **LifeFuse-Mem** separates information by temporal commitment with dedicated memory components + lifecycle-aware updates, letting stable and transient knowledge evolve locally without converting temporary context into durable state. On the controlled anti-overwrite benchmark it improves acquisition-controlled retention and reduces temporary overwrite; broadly competitive on two public long-memory benchmarks. |
| **Key Innovations** | (1) Explicit lifecycle labels as a memory-architecture dimension; (2) dedicated stable vs transient stores with lifecycle-aware updates (no temporary→durable conversion); (3) an anti-overwrite benchmark for diagnosing drift. |
| **Link** | [arXiv:2609.12436](https://arxiv.org/abs/2609.12436) |

### 4.4 Residual Vector-based Reconstruction as Long-Context Recall Regardless of Context Window Size

| Field | Detail |
|-------|--------|
| **Authors** | MyungHoon Ryu, XinYu Piao, Jong-Kook Kim |
| **Institution** | Korea University (inferred) |
| **Published** | 11 Sep 2026 (cs.AI / cs.CL) |
| **Abstract** | LLM long-context processing faces token-proportional GPU memory; model optimization and lossy compression still fail beyond pretrained, size-constrained context windows. This paper proposes a **training-free long-context recall method keeping near-constant GPU memory** as context grows: reconstruct facts using **parameter activations in the FFN layers, whose residual vectors store facts from the source document**. Residual-vector reconstruction lets the LLM deterministically reconstruct query-relevant facts without referencing the original document — high fidelity, no fine-tuning. Empirically answers single-fact questions in **two-million-token story contexts** where previous methods fail. |
| **Key Innovations** | (1) Residual vectors as a persistent fact store — recall decoupled from context-window memory; (2) training-free, near-constant-memory long-context answering; (3) 2M-token feasibility demonstration. |
| **Link** | [arXiv:2609.12686](https://arxiv.org/abs/2609.12686) |

### 4.5 Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Junghyun Min, Huseyin Uzunalioglu, Mohamed Trabelsi |
| **Institution** | Nokia Bell Labs (inferred) |
| **Published** | 11 Sep 2026 (cs.AI / cs.IR) |
| **Abstract** | Tests whether autonomous end-to-end ML research frameworks (mostly demonstrated on narrow search spaces like LM or biomedical benchmarks) generalize to **open-ended, industry-grade problems** — case study: telecom ticket retrieval, with degrees of freedom in representation, architecture, and training-data generation. With commercial and open-source agents: autonomous research **excels at narrow hyperparameter optimization** but lacks human intuition/creativity and imposes operational overhead. Even under minimal human supervision, autonomous research reached **90% of SOTA** (0.34 vs 0.38 Recall@1) in far less time (10 weeks vs 10 months of human work) at modest cost (up to ~$200 per Cursor campaign). Recommendation: humans + autonomous research frameworks should collaborate for best results. |
| **Key Innovations** | (1) First autonomous-research case study on open-ended industrial retrieval (telecom ticket); (2) honest capability map: strong on narrow HPO, weak on creative search-space design; (3) cost/time evidence for human-AI collaboration in ML research. |
| **Link** | [arXiv:2609.13073](https://arxiv.org/abs/2609.13073) |

---

## 5. Games & Game Theory

### 5.1 Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf

| Field | Detail |
|-------|--------|
| **Authors** | Yu-Yu Yang, Ti-Rong Wu, Hung Guei, Hsing-Yu Chen, I-Chen Wu |
| **Institution** | National Yang Ming Chiao Tung University (NYCU; inferred) — EMNLP 2026 Main |
| **Published** | 11 Sep 2026 (cs.AI / cs.CL) |
| **Abstract** | Social-deduction games like Werewolf evaluate LLM agents, but evaluations usually rely on final outcomes. This paper proposes a **belief-shift evaluation benchmark** for Werewolf analyzing communication via belief updating: annotate suspicion and accusation messages in LLM-played games, measure how an observing village-side model's beliefs change per message. Evaluates **40 open-weight LLM configurations on 1,224 annotated messages**: larger models better distinguish true wolves from villagers from game history, but accusations still strongly drive beliefs — models become more suspicious of the accused, less of the accuser, especially when the accuser is trusted, even if wolf-aligned; larger models better resist accusations from distrusted accusers. Open-weight LLMs up to 120B struggle to integrate accusation content with source trust in strategic communication. |
| **Key Innovations** | (1) Communication-level (belief-shift) eval rather than game-outcome eval for Werewolf; (2) accusation-content vs accuser-trust dissociation result; (3) failure diagnosis for strategic communication in LLMs → fixes focus on source-trust integration. |
| **Link** | [arXiv:2609.12446](https://arxiv.org/abs/2609.12446) |

### 5.2 EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Weiyuan Li, Aili Chen, Xintao Wang, Yikai Zhang, Qingqing Dong, Jinghan Xu, Hongru Hou, Wenxuan Zhao, Chengkun Lang, Jun Gao, Yuanli Guo, Hongcheng Guo, Yanghua Xiao, Deqing Yang |
| **Institution** | Fudan University (inferred) |
| **Published** | 11 Sep 2026 (cs.AI) |
| **Abstract** | Open-ended RL relies on rubric-based rewards for tasks without verifiable answers, but policy and reward form a dynamic feedback loop: as the policy optimizes the current reward, an initially useful reward system becomes unreliable via reward hacking or reduced response discriminability. The reward system should **evolve during training**. **EvoRS** represents the reward system as an executable **Reward-DAG**; an **agentic designer** updates it from on-policy rollouts and reward traces to maintain train-time reliability. Across writing and roleplay, EvoRS achieves best quality under all three judges — outperforming the policy by **2.107 and 4.767 points** — while reducing reward hacking and coverage failures and preserving reward informativeness. Ablations confirm a comprehensive fixed reward system cannot stay reliable in open-ended tasks. |
| **Key Innovations** | (1) Reward systems as evolvable Reward-DAGs (beyond fixed rubric or adaptive criteria); (2) agentic designer triggered by on-policy reward traces; (3) joint mitigation of hacking + coverage loss + informativeness decay. |
| **Link** | [arXiv:2609.12459](https://arxiv.org/abs/2609.12459) |

### 5.3 Mitigating Emergent Collusion in LLM Pricing Agents

| Field | Detail |
|-------|--------|
| **Authors** | Abdullah Garra |
| **Institution** | (academic, inferred) |
| **Published** | 11 Sep 2026 (cs.GT) |
| **Abstract** | LLM-based pricing agents can produce **supracompetitive outcomes in repeated oligopoly environments without explicit collusion instructions**. Reproduces the qualitative prompt-sensitivity effect of Fish et al. on **DeepSeek-V3.1** (P1 prompt → significantly higher prices/profits than P2, though less monopoly-like than the original GPT-4 results). Evaluates three regulatory interventions: a **prompt-only warning** (reduces but does not eliminate above-Nash pricing), a **Harrington-inspired expected-damages payoff regulator** (brings P1 close to duopoly Nash benchmark, removes the significant P1–P2 gap), and an **active random entrant** (strongest: pushes both prompts below the random-entrant Nash benchmark). Preliminary evidence: interventions altering incentives or market participation reduce supracompetitive pricing more effectively than prompt warnings alone. |
| **Key Innovations** | (1) Cross-model reproduction (DeepSeek-V3.1) of LLM pricing-agent collusion; (2) first comparative test of prompt-only vs mechanism-based (Harrington regulator, active entrant) interventions; (3) implication for ad-auction/autonomous-agent regulation: incentives, not warnings. |
| **Link** | [arXiv:2609.13037](https://arxiv.org/abs/2609.13037) |

### 5.4 Deriving the Pure Price of Anarchy for Networked Resource Allocation Games

| Field | Detail |
|-------|--------|
| **Authors** | Vartika Singh, Philip N. Brown |
| **Institution** | University of Colorado Colorado Springs (inferred) |
| **Published** | 10 Sep 2026 (cs.GT / cs.MA) |
| **Abstract** | Studies multi-agent coordination with **arbitrary information networks** game-theoretically: a system designer assigns local utility functions to steer agents toward a desired system objective, measured by the **pure price of anarchy (pPoA)** at the worst pure Nash equilibrium. Derives a **linear program that computes the optimal pPoA for any arbitrary information network and system objective** — the first solution to optimal utility design for arbitrary networks, generalizing previous full-information-only approaches. For **supermodular objectives, a fully communication-denied utility design is optimal regardless of the network** (counterintuitive); for submodular objectives numerical analysis suggests robustness to communication failures; for weighted maximum coverage the marginal-contribution utility design provably optimizes pPoA across many information networks. |
| **Key Innovations** | (1) First LP-formulation of optimal utility design for arbitrary information networks (was full-information-only); (2) surprising result: communication deprivation is optimal for supermodular objectives; (3) constructive guarantees for weighted maximum coverage. |
| **Link** | [arXiv:2609.12077](https://arxiv.org/abs/2609.12077) |

---

## 6. Advertising & Creative Generation

### 6.1 I Am AdMan: A Pipeline for Automatic Generation of Personalized Advertising Imagery

| Field | Detail |
|-------|--------|
| **Authors** | Victor Kolominsky-Rabas, Leopold Müller, Claudius Budcke, Niklas Kühl |
| **Institution** | University of Bayreuth (inferred; Niklas Kühl) |
| **Published** | 11 Sep 2026 (cs.AI / cs.HC) |
| **Abstract** | Personalized marketing matches the right product to the right customer, but **ad visuals stay generic**. **AdMan** is a **multi-agent pipeline**: customer data → personas → personalized ad images conditioned on product reference images → **LLM-based judge agent** for automated quality control. Implemented with two model configurations and evaluated across four products, six celebrity personas (qualitative), and 100 real customer profiles producing 1,745 advertisements — with an expert focus group + artifact-rate assessment. Generates photorealistic personalized ads, but performance varies substantially by product complexity and model configuration, delimiting current feasibility. |
| **Key Innovations** | (1) End-to-end customer-data→personalized-ad-imagery pipeline (multi-agent incl. LLM judge for QC); (2) scale evidence (100 profiles, 1,745 ads); (3) honest limitation map: product-complexity × model-configuration variance. |
| **Link** | [arXiv:2609.12694](https://arxiv.org/abs/2609.12694) |

### 6.2 Enabling and Understanding Personalization in AI-Generated Advertising Imagery

| Field | Detail |
|-------|--------|
| **Authors** | Victor Kolominsky-Rabas, Leopold Müller, Claudius Budcke, Claas Christian Germelmann, Niklas Kühl |
| **Institution** | University of Bayreuth (inferred) |
| **Published** | 11 Sep 2026 (cs.AI / cs.HC) |
| **Abstract** | Two-stage within-subject study (N=100, four products, three personalization levels varying amount/specificity of customer data) evaluating AI-generated personalized ad visuals on attitude toward ad, attitude toward product, and purchase intention. Key result: **moderate personalization is judged most positively**; high personalization raises *perceived personalization* (positive for all three outcomes) but also raises *perceived creepiness*, which is negatively associated and **dominates the total effect**. |
| **Key Innovations** | (1) Disentangles perceived-personalization gain from perceived-creepiness cost (dominance result); (2) inverted-U evaluation curve for personalization depth; (3) direct managerial guidance for ad-personalization depth. |
| **Link** | [arXiv:2609.12697](https://arxiv.org/abs/2609.12697) |

### 6.3 Balancing Emotional Alignment and Semantic Consistency in Image Generation via RL with Valence-Arousal Anchoring

| Field | Detail |
|-------|--------|
| **Authors** | Jisheng Dang, Zhenxuan Wang, Bin Li, Ronghao Lin, Bin Hu, Tat-Seng Chua |
| **Institution** | NUS / Chinese institutions (inferred; Tat-Seng Chua) |
| **Published** | 11 Sep 2026 (cs.CV / cs.LG) |
| **Abstract** | Continuous emotion control in text-to-image generation must improve affective alignment without changing the objects/layout/scene of the prompt. Supervised emotion-injection optimizes feature-space proxies → **emotion-semantic drift** (stronger emotional conditioning accompanies unintended content changes). This flow-matching framework combines **continuous valence-arousal (VA) conditioning**, **GRPO**, and a **neutral semantic anchor**: the deterministic probability-flow ODE is converted to a marginal-preserving SDE for trajectory sampling/policy-ratio estimation; a frozen CLIP-based VA regressor supplies a terminal reward (distance between predicted and target VA), while an image generated under zero VA conditioning is the feature reference for semantic preservation. Reduced denoising schedule for online RL sampling, original schedule at inference. On **3,300 prompt-emotion combos**, substantially lower valence/arousal errors than the VA-conditioned baseline and improved CLIPScore vs EmotiCrafter, with a measurable trade-off in reference-free image quality. |
| **Key Innovations** | (1) RL formulation of continuous-affect alignment (Flow-GRPO) with VA-coordinate reward; (2) neutral-semantic-anchor regularization decoupling affect from content; (3) deterministic-ODE→marginal-preserving-SDE engineering for stable policy-ratio estimation. |
| **Link** | [arXiv:2609.12830](https://arxiv.org/abs/2609.12830) |

---

## 7. Evaluation, Reliability & Information-Theoretic Limits

### 7.1 How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations and Near-Saturation of Leading Benchmarks

| Field | Detail |
|-------|--------|
| **Authors** | Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller, Corey O'Hern, Vidvuds Ozolins, David Poland, A. Douglas Stone, Frank C. van den Bosch, Logan Wright, Navid Akbari, + 40+ additional researchers |
| **Institution** | Yale et al. (inferred; 50+ co-authors) |
| **Published** | 11 Sep 2026 (cs.AI) |
| **Abstract** | Low reported scores on leading physics benchmarks (incl. the Artificial Analysis Intelligence Index 2026) suggest frontier models struggle with advanced physics — contradicting domain experts' daily experience. Frontier models are re-evaluated on **six physics benchmarks** with **expert audits** (problem statements, reference solutions, model responses reviewed by faculty/graduate researchers to separate genuine model errors from grader errors, incorrect references, ambiguous questions). Most "incorrect" audited cases were benchmarking artifacts. After correcting reference solutions and repairing/excluding flawed questions: GPT-5.6-Sol's measured mean@4 rises **47.3%→78.7% on HLE-Physics** and **61.0%→87.2% on CMT-Benchmark**; corrected pass@4 reaches **94.4% on the 54 retained CritPt challenges**. Benchmarks substantially understate frontier-model performance on well-posed physics; near-saturation calls for more demanding, expert-validated evaluation. |
| **Key Innovations** | (1) Large-scale expert re-grading audit (50+ physicists) revealing grader/reference-error artifacts; (2) dramatic corrected-score deltas (up to +26pp); (3) "near-saturation" claim → push for harder expert-validated physics benchmarks. |
| **Link** | [arXiv:2609.13009](https://arxiv.org/abs/2609.13009) |

### 7.2 Judging by the Cover: Cleaning LLM Truthfulness Benchmarks to Avoid Surface-Level Feature Leakage

| Field | Detail |
|-------|--------|
| **Authors** | Foad Namjoo, Remy Ogasawara, Amirali Abdullah, Cullen Anderson, Narmeen Fatimah Oozeer, Jeff M. Phillips |
| **Institution** | University of Utah (inferred; Jeff Phillips) |
| **Published** | 11 Sep 2026 (cs.CL / cs.LG) |
| **Abstract** | Binary-choice truth benchmarks ask models to pick correct vs incorrect answers; if the two answer types differ systematically in **surface-level features**, models can exceed chance without doing the intended reasoning. Show this is detectable and exploitable: a simple **six-feature logistic classifier** separates correct from incorrect answers in TruthfulQA with substantial accuracy; similar artifacts exist in other benchmarks. Ships a **cleaning mechanism (Audit-Prune)** that removes the most leakage-reinforcing pairs, releasing a TruthfulQA variant with surface-feature leakage reduced close to chance. |
| **Key Innovations** | (1) Systematic surface-leakage detection across truth benchmarks (feature classifier as audit); (2) Audit-Prune cleaning mechanism for dataset release hygiene; (3) released cleaned TruthfulQA. |
| **Link** | [arXiv:2609.13003](https://arxiv.org/abs/2609.13003) |

### 7.3 The Cost of Compression: A Rate-Distortion Limit on Factual Hallucination

| Field | Detail |
|-------|--------|
| **Authors** | Xi Wang, Shijia Xu, Rongfeng Guo |
| **Institution** | (academic, inferred) |
| **Published** | 10 Sep 2026 (cs.CL) |
| **Abstract** | Factual hallucination in closed-book QA is usually treated as a **coverage problem** (fact absent from memory). This paper isolates the second error source: **even when a fact is observed, finite memory may force approximate storage**. Provides a coverage–compression model of factual recall: N queries, K answers, learner observes M facts, compresses to at most B bits, answers uniformly drawn tests without retrieval. For uniform random ground truth, proves ℰ ≥ (M/N)·δ*(B/M) + (1−M/N)(1−1/K) — separating **compression distortion on observed facts** from **missing coverage on unobserved facts** (δ* = inverse rate-distortion of uniform K-ary source under zero-one loss). Enables reasoning about selective memory, forced compression, structure, retrieval, abstention, long-context organization. Validated via theory-implied simulations and controlled fact-injection probes in modern LMs varying fact load and effective trainable memory. Not a complete hallucination theory, but an information-theoretic account of a separable failure mode. |
| **Key Innovations** | (1) Compression (not coverage) as a provable second hallucination source — rate-distortion lower bound; (2) clean decomposition of observed-fact distortion vs unobserved-fact miss; (3) empirical probes (fact-injection) matching theory-implied signatures. |
| **Link** | [arXiv:2609.12111](https://arxiv.org/abs/2609.12111) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **Generative recommendation matures into systems** | OneLA (beam-decoding serving), Preference-Drift subsequence learning, MIMA (multi-positive exclusive assignment), ChronicleRec (production A/B on KuaiRand + Tencent AdLive) |
| **Retriever/verifier split returns** | Rec Retrievers Need Verifiers (universal post-hoc verification for sequential rec) |
| **MoE becomes a first-class RL/serving object** | ESRL (expert-space rollout diversity, +3.2 pp Pass@1), Quality-Constrained routing over quantized MoE pool (FWP risk-per-request) |
| **RLHF alignment re-theorized** | RLHF is a Decent Utilitarian Aligner — distortion is a distribution-mismatch artefact, not exponential-by-construction |
| **Sequential-memory research diversifies the state** | RunningTensor (order-o recurrent state), SAS (end-to-end context ranking), Tabular-FM attention quantization (attention not weights), visual-KV pixel-decodability negative result |
| **Agent memory: lifecycle & skill reuse** | LifeMem (workflow-clustered skills), LifeFuse-Mem (lifecycle-aware anti-overwrite), Residual-Vector reconstruction (training-free long-context recall) |
| **The wild multi-agent episode gets reconstructed + contested** | The Mechanics of a Swarm (14.6k revisions, episode-clock asymmetry) — companion to yesterday's Copying paper on the same June-2026 wiki incident |
| **Autonomous research benchmarks honest scores** | Telecom ticket retrieval: 90% SOTA in 10 weeks at $200 — but humans still needed for creative search-space design |
| **Games: communication & equilibrium** | Werewolf belief-shift benchmark (accusation-vs-accuser trust), EvoRS self-evolving reward systems, LLM pricing-agent collusion mitigation (incentives beat warnings) |
| **Evaluation hygiene under (re-)audit** | Frontier-models-physics expert re-grading (+26–31pp), TruthfulQA surface-leakage cleaning, rate-distortion hallucination bound |

(End of file — total 30 papers / 7 sections)