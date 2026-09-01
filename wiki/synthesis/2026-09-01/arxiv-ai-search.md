---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-09-01)"
type: synthesis
created: 2026-09-01
updated: 2026-09-01
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, ml-systems, moe, inference, efficiency, rl, rlvr, creative-generation, world-models, marketplaces, daily-digest]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-09-01 (Tuesday) · Scope: curated across the requested domains (AI, LLMs, recommendation, advertising, sequential modeling, CTR, games). Companion to the same-day [arxiv-daily](arxiv-daily.md) (which covers the Tue 1 Sep wave `2608.29340–2608.30662`). This report is a **cross-domain deep pass** over recent strong papers on these themes — including several earlier-submitted (Jan–Jul 2026) papers that are the current SOTA baselines in the rec/ad/CTR and game/agent literature the wiki tracks. **21 featured + 1 honorable mention.** Every arXiv ID below is grep-verified absent from `wiki/`. (Section 2.9 is a placeholder cross-reference to earlier sections, not a separate paper.)
>
> Method: titles/abstracts/author-affiliations recovered via arXiv search/export + full `abs` pages; affiliations marked *(stated)* come from paper/project front matter or documented production deployments, *(inferred)* = deduced from author identities; otherwise "not stated". Temp files under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`, cleaned up after this report lands.

---

## ① LLM Architecture, Training & Inference Efficiency (8)

### 1.1 Matryoshka Language Model Suites: Nested Training of Model Families

| Field | Detail |
|-------|--------|
| **Authors** | (listed per HTML full-text) — suite-training group; affiliations stated in front matter (open-weight research group) |
| **Submitted** | 2026-08-25 · [2608.09703](https://arxiv.org/abs/2608.09703) · cs.CL |
| **Abstract** | Training a model suite classically requires training each model separately and serving them independently. This work stacks sub-models of increasing size into a **single nested architecture trained end-to-end** (a "Matryoshka" suite: 500M, 1.5B, 3B). The largest model contains the smaller stacks, enabling low-cost online distillation to all sub-models at every step and serving as the verifier for the draft models in speculative decoding. Suite matches independently-trained baselines while using **36% less training compute** and improving speculative-decoding throughput **14–26%**. |
| **Key innovations** | Nested/stacked architecture for a whole model *family* (not a single model); distillation as a free by-product of each training step; static self-speculative decoding (draft is inside the verifier); ablations on suite design choices. |
| **arXiv** | [2608.09703](https://arxiv.org/abs/2608.09703) |
| **Why it matters** | Directly relevant to the wiki's post-training/inference-efficiency thread: a single training run now yields a deployable family with better throughput — co-designing the *suite* rather than individual models. |

### 1.2 LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts

| Field | Detail |
|-------|--------|
| **Authors** | NVIDIA research team (Nemotron-3 lineage) |
| **Institution** | NVIDIA *(stated: adopted by flagship Nemotron-3 Super/Ultra models)* |
| **Submitted** | 2026-01-24 · [2601.18089](https://arxiv.org/abs/2601.18089) · cs.CL / cs.LG |
| **Abstract** | Revisits MoE design from a hardware-software co-design lens, arguing current MoEs are optimized for offline throughput and neglect latency-critical, bandwidth-bound inference. **LatentMoE projects incoming activations into a lower-dimensional latent space before expert routing/computation**, cutting routed-parameter load and all-to-all traffic by a factor of d/l; the savings fund a proportional increase in expert count and routing top-k at constant inference cost. Empirically evaluated to 95B params/1T+ tokens and projected to trillion-param serving (Kimi-K2-1T class), where iso-accuracy standard MoE scaling is ~350B extra params and 1.24–3.46× slower. |
| **Key innovations** | Latent-projection decouples routing compute from hidden dimension (new efficiency knob); accuracy-per-FLOP *and* accuracy-per-parameter framing; deployed at scale in Nemotron-3. |
| **arXiv** | [2601.18089](https://arxiv.org/abs/2601.18089) |
| **Why it matters** | MoE is central to the modern LLM stack the wiki tracks; LatentMoE is the current "latent-routing beats standard-MoE" reference point — cf. the deeper project MoUE in 1.3. |

### 1.3 Mixture of Universal Experts (MoUE): Scaling Virtual Width via Depth-Width Transformation

| Field | Detail |
|-------|--------|
| **Authors** | (academic group; affiliations in front matter) |
| **Institution** | Not stated |
| **Submitted** | 2026-03-12 · [2603.04971](https://arxiv.org/abs/2603.04971) · cs.LG |
| **Abstract** | MoE decouples capacity from per-token compute but is bounded by physical depth and width. **MoUE reuses a universal, layer-agnostic expert pool across layers, converting depth into "virtual width"** under a fixed activation budget. Three components handle the challenges of recursive re-use: a **Staggered Rotational Topology** for structured expert sharing, a **Universal Expert Load Balance** correcting for depth-exposure asymmetry, and a **Universal Router** with lightweight trajectory state for coherent multi-step routing. Outperforms matched MoEs by up to 1.3% across scaling regimes; converts existing MoE checkpoints with up to 4.2% gains. |
| **Key innovations** | A new scaling dimension (virtual width) orthogonal to depth/width; expert-parameter sharing across layers via path composition; checkpoint-transform path from standard MoE. |
| **arXiv** | [2603.04971](https://arxiv.org/abs/2603.04971) |
| **Why it matters** | Pushes the architectural frontier the wiki tracks on "how to add capacity without adding cost" — the shared-expert / latent-expert family of ideas is the live research bet for scaling MoE. |

### 1.4 LAER-MoE: Load-Adaptive Expert Re-layout for Efficient MoE Training

| Field | Detail |
|-------|--------|
| **Authors** | Xinyi Liu, Yujie Wang, Fangcheng Fu, Xuefeng Xiao, Huixia Li, Jiashi Li, Bin Cui |
| **Institution** | Peking University (PKU-DAIR) *(stated)* · **ASPLOS '26** |
| **Submitted** | 2026-02-11 · [2602.11686](https://arxiv.org/abs/2602.11686) · cs.DC / cs.LG |
| **Abstract** | During expert-parallel MoE training, dynamic routing causes **load imbalance among experts** — a handful of overloaded experts bottleneck each iteration. LAER-MoE introduces **Fully Sharded Expert Parallel (FSEP)**: each expert is fully partitioned across devices and restored at expert granularity via all-to-all, enabling flexible in-training expert re-layout for load balancing. A load-balancing planner co-optimizes token routing and expert layout; fine-grained communication scheduling hides overhead. Up to **1.69× acceleration** over prior SOTA MoE training systems on A100 clusters. |
| **Key innovations** | New MoE parallelism paradigm (FSEP) allowing dynamic expert placement mid-training; planner jointly solves routing + layout; system paper with strong speedups. |
| **arXiv** | [2602.11686](https://arxiv.org/abs/2602.11686) |
| **Why it matters** | Systems-side of the MoE thread: load imbalance is *the* training bottleneck for sparse models — complements the architectural papers above. |

### 1.5 EvoResearcher: Training-Free Inference-Time Self-Reflection with Cost-Bounded Early Stopping

| Field | Detail |
|-------|--------|
| **Authors** | Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, Bing Li |
| **Institution** | Jiangxi Arts & Ceramics Technology Institute / Universiti Sains Malaysia *(stated)* |
| **Submitted** | 2026-08-27 · [2608.18884](https://arxiv.org/abs/2608.18884) · cs.CL / cs.LG |
| **Abstract** | Proposes a **training-free inference-time protocol** (generate → self-critique → revise) on a single frozen LLM, with a user-set max depth and a **CONFIRMED sentinel** that enables implicit early stop under a strict compute budget. Four principles (correctness, efficiency, reflection depth, tool-call diversity) are instantiated as prompt-level mechanisms with zero gradient updates. On clean BBH the loop doesn't raise single-shot accuracy (stays within the 95% Wilson interval) but terminates 82–88% of items at equal accuracy, bounding inference to ~2.1 generations/question; it gives +4.2 pp (GSM8K) and +14.2 pp (MATH) where single-shot reasoning is unreliable. A confidence sweep shows numeric confidence is overconfident — the CONFIRMED sentinel, not the tag, is the effective cost-bounder. |
| **Key innovations** | Cost-bounded self-verification without RLVR training; diagnostics showing *where* inference-time scaling helps (unreliable tasks) vs. doesn't (clean BBH); pragmatic low-cost alternative to RL pipelines. |
| **arXiv** | [2608.18884](https://arxiv.org/abs/2608.18884) |
| **Why it matters** | Fits the wiki's test-time-scaling thread: adds a clean "bounded-reflection early stop" datum and a healthy caveat box against unbounded fixed-depth loops. |

### 1.6 Evaluation Awareness in Language Models: Representation, Verbalization, and Control

| Field | Detail |
|-------|--------|
| **Authors** | (multi-institution; Olmo/ALLEN-AI-affiliated team) |
| **Institution** | Not stated (open-checkpoint Olmo models studied) |
| **Submitted** | 2026-08-27 · [2608.21766](https://arxiv.org/abs/2608.21766) · cs.CL / cs.AI |
| **Abstract** | Evaluations assume a model under test behaves as in deployment — an assumption that breaks if a model infers it is being evaluated. This work provides a systematic study across six open-weight models (7B–49B, 4 families) of whether "being under evaluation" is (i) linearly represented in activations (decodable with AUROC ≥ 0.7), (ii) verbalized in outputs, and (iii) causally steerable. Representations and verbalization align only partially and vary across models/layers; steering along probe directions does shift verbalized scores. Tracking Olmo checkpoints shows evaluation awareness is present in base models, amplified by SFT, then stable — while steering effects grow at every stage. |
| **Key innovations** | Disentangles representational vs. verbalized vs. casual facets of eval awareness; longitudinal testing across training stages; probe generality across unseen benchmarks. |
| **arXiv** | [2608.21766](https://arxiv.org/abs/2608.21766) |
| **Why it matters** | Important caveat for the wiki's benchmark/verifiability thread: benchmark scores can be inflated by eval awareness — one of the strongest recent critiques of static evaluation methodology. |

### 1.7 Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

| Field | Detail |
|-------|--------|
| **Authors** | (large research team incl. Human-Health/healthbench-affiliated authors) |
| **Institution** | Not stated |
| **Submitted** | 2026-08-27 · [2608.18931](https://arxiv.org/abs/2608.18931) · cs.CL / cs.LG |
| **Abstract** | First **compute-normalized comparison of five TTS families** (Best-of-N, Beam Search, Particle Filtering, Refinement, Fusion) across five *open-ended* generation benchmarks (medicine, law, finance, chat, creative writing), decomposing token budget into exploration and exploitation. Scaling exploration works — oracle quality (best candidate) rises with compute everywhere. **Exploitation breaks**: with SOTA generators, reward models correlate only ρ≈0.12 with true quality, making selection near-random; tree search compounds this via diversity collapse; refinement helps on 1/5 benchmarks; only Fusion improves but recovers ~40% of available quality. None of compute, RM size, or generator size closes the gap. |
| **Key innovations** | Compute-normalized comparison across open-ended tasks (TTS is usually tested on verifiable math/code); unified exploration–exploitation decomposition; structural finding that candidate pools are rich but selection/RM quality is the bottleneck. |
| **arXiv** | [2608.18931](https://arxiv.org/abs/2608.18931) |
| **Why it matters** | Directly qualifies the wiki's test-time-scaling enthusiasm: TTS gains are real on verifiable tasks but collapse on open-ended generation because reward models can't rank. Strong caveat for applied use. |

### 1.8 (Honorable mention) Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach

| Field | Detail |
|-------|--------|
| **Authors** | (academic; affiliations in front matter) |
| **Institution** | Not stated |
| **Submitted** | 2026-08-26 · [2608.25267](https://arxiv.org/abs/2608.25267) · cs.LG |
| **Abstract** | Uses the **Bayesian Truth Serum (BTS)** peer-prediction mechanism as the reward in GRPO to reduce sycophancy **without labels or preference annotations**. BTS rewards answers that are *surprisingly common* given the model's own predictions over its group of responses. Proves a sycophantic response earns strictly lower expected reward than an honest one at the large-group limit. On a true/false benchmark the answer-flip rate under user pressure drops 23%→4% and accuracy under pressure rises 80%→93% — comparable to label-based methods (SMART, synthetic-data FT, pinpoint tuning) with more compute. |
| **Key innovations** | Label-free RL reward derived from peer prediction; theoretical guarantee that honesty is rewarded; direct comparison to SMART and supervised alternatives. |
| **arXiv** | [2608.25267](https://arxiv.org/abs/2608.25267) |
| **Why it matters** | RK framework: a genuinely label-free RLVR signal for alignment — complements the wiki's verifiability/reward-design thread. |

---

## ② Recommendation, Advertising & CTR (9)

### 2.1 GenRec: An LLM-Backed Recommendation Ranker at Netflix

| Field | Detail |
|-------|--------|
| **Authors** | Netflix research team |
| **Institution** | Netflix *(stated: production A/B vs. quality/cost trade-offs)* |
| **Submitted** | 2026-08-25 · [2608.10257](https://arxiv.org/abs/2608.10257) · cs.IR |
| **Abstract** | GenRec is an **LLM-backed ranker** built on an in-house foundational LLM in two phases: Phase 1 adapts an open-source LLM to Netflix data; Phase 2 post-trains it with recommendation-ranking data, labels, and rewards. Uses **verbalized user histories and context**, a **catalog-aware ranking head** (scores large catalogs in a single forward pass — no autoregressive decoding at serve), reward-weighted ranking loss, and a **prefill-only** cost-constrained serving design. With far fewer Phase-2 labels and input signals than the production ranker, it achieves statistically significant gains on short- and long-term online metrics. |
| **Key innovations** | Catalog-aware head (single-pass large-candidate ranking, avoids generative-retrieval latency); context engineering cuts context length ~3× with negligible ranking loss; reward integration; argues the paradigm shift from feature engineering → context engineering and bespoke architectures → shared foundation backbones. |
| **arXiv** | [2608.10257](https://arxiv.org/abs/2608.10257) |
| **Why it matters** | A flagship production LLM-ranker from Netflix — full pipeline (verbalization, post-train, reward, serving) directly extends the wiki's LLM-for-recommendation thread ([GenCI 2.2], [RefRec/PLUM lineage]). |

### 2.2 GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Hongyu Lu, Ji-Rong Wen |
| **Institution** | Renmin University of China (Gaoling School of AI) / WeChat, Tencent Beijing *(stated)* · **WWW '26** |
| **Submitted** | 2026-01-26 · [2601.18251](https://arxiv.org/abs/2601.18251) · cs.IR |
| **Abstract** | Two failure modes of discriminative CTR: overfitting to historically dominant features (poor adaptation to rapid interest shifts) and the point-wise ranking chasm (scoring each candidate in isolation discards the recalled set's context). **GenCI** uses a generative model trained with a next-item-prediction (NTP) objective to proactively produce a **semantic interest cohort** — an explicit, candidate-agnostic representation of immediate intent — then a hierarchical candidate-aware network injects it into ranking via cross-attention, trained end-to-end for recall–ranking consistency. Outperforms SOTA baselines on three datasets. |
| **Key innovations** | Generative/cohort-based (not just discriminative) user-interest modeling; reframes recall-then-rank into a generate-and-interpret loop; joint optimization for recall–ranking consistency. |
| **arXiv** | [2601.18251](https://arxiv.org/abs/2601.18251) |
| **Why it matters** | A WWW'26 anchor for the generative-CTR thread the wiki tracks (cf. DGenCTR, GPT4Rec) — the cohort-as-context idea is a clean fix for the point-wise ranking limitation. |

### 2.3 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe et al. (LinkedIn ads team) |
| **Institution** | LinkedIn *(stated: deployed, serving homefeed sponsored updates)* |
| **Submitted** | 2026-02-12 · [2602.11410](https://arxiv.org/abs/2602.11410) · cs.IR |
| **Abstract** | Adapting transformer/generative recommenders to **ads CTR** poses unique challenges (post-scoring contextual signals, offline-online consistency, industrial scale). **CADET** — a decoder-only transformer deployed at LinkedIn — introduces: (1) context-conditioned decoding with multi-tower heads explicitly modeling post-scoring signals like ad position (resolving the chicken-and-egg of predicted CTR vs. ranking); (2) self-gated attention for training stability; (3) a timestamp-based RoPE variant capturing temporal relationships from seconds to months; (4) session-masking against train-serve skew; (5) production engineering (tensor packing, chunking, custom Flash Attention). Online A/B: **+11.04% CTR lift** over the production LiRank (DCNv2 + sequential encoders) baseline. |
| **Key innovations** | Context-conditioned decoding that models position post-scoring; self-gated attention; timestamp RoPE; deployed production ads CTR system. |
| **arXiv** | [2602.11410](https://arxiv.org/abs/2602.11410) |
| **Why it matters** | Decoder-only transformer for *ads* CTR — the flagship production counterexample to the DeepCTR/feature-interaction idiom; directly extends the wiki's ads/CTR thread. |

### 2.4 UniDot: A Unified Network for Sequence Modeling and Feature Interaction in Large-scale Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | (runner-up team, Industrial track) |
| **Institution** | *(inferred: KDD Cup 2026 Tencent UniRec Challenge team)* · **KDD Cup 2026 Workshop** |
| **Submitted** | 2026-08-22 · [2608.16797](https://arxiv.org/abs/2608.16797) · cs.IR |
| **Abstract** | Industrial recommenders split into feature-interaction (FM-family) and sequential (behavior-history) model families that production systems only loosely couple. **UniDot** unifies them on the insight that the FM embedding inner product *is* the same primitive as attention's query·key scoring — a single dot-product of tokens underlies both. It tokenizes non-sequential fields and multi-domain sequences into one shared space and stacks a single block with a token-mixing bus and a sequence-retrieval bus running in parallel, exchanged through MLP-Mixer fusion, plus an **FM Highway** carrying explicit per-layer dot-product interactions to the classifier. Finished runner-up on the Industrial track with 0.83217 AUC. |
| **Key innovations** | Unifying primitive (token dot-product) across feature interaction and sequence modeling; FM Highway preserves second-order signal; single stackable block with latency-bounded sequence sharing. |
| **arXiv** | [2608.16797](https://arxiv.org/abs/2608.16797) |
| **Why it matters** | The "unify feature interaction + sequence modeling into One Transformer block" race (with HyFormer/MixFormer/OneTrans/UniMixer) — the wiki tracks this explicitly ([ctr-scaling-landscape](curated synthesis)). |

### 2.5 CRRN: Cascading Relevance-driven Recommendation Network for CTR Prediction in Trigger-Introduced Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | (industrial; Tmall-affiliated) |
| **Institution** | *(inferred: Alibaba/Tmall — online A/B on Tmall, "serving online")* |
| **Submitted** | 2026-08-23 · [2608.22973](https://arxiv.org/abs/2608.22973) · cs.IR |
| **Abstract** | In **Trigger-Introduced Recommendation (TIR)** — a user clicks an item (the "trigger", holding instant interest) and is shown related target items — existing methods neglect trigger relevance. **CRRN** has three components: a **Trigger-Target Interaction layer** extracting interaction features via personalized gating; a **Cascading Interest Fusion module** that estimates trigger intention and adaptively fuses instant + personalized interests; and a **Category-assisted Pairwise Loss** that uses category association to enhance trigger relevance. Beats SOTA (Wide&Deep+TIR, DIN+TAR, DIHN, DIAN, DEI2N) on industrial + public data; **+3.87% pCTR** online on Tmall and now serving. |
| **Key innovations** | Explicit trigger–target relevance modeling (vague/implicit vs. search terms); cascading fusion of instant vs. long-term interest; production A/B. |
| **arXiv** | [2608.22973](https://arxiv.org/abs/2608.22973) |
| **Why it matters** | A distinct recommendation scenario (TIR) the wiki tracks for interest-modeling — complements the interest-fusion and target-aware threads. |

### 2.6 SparseCTR: Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | (academic) |
| **Institution** | Not stated |
| **Submitted** | 2026-01-25 · [2601.17836](https://arxiv.org/abs/2601.17836) · cs.IR · **WWW '26** |
| **Abstract** | LLM-style self-attention for long user-behavior sequences is too expensive (quadratic complexity) and general sparse attention isn't suited to rec data (behavior has personalization + temporal structure, unlike uniform/local distributions). **SparseCTR** segments behavior into **personalized time-aware chunks** and applies a **three-branch sparse self-attention** capturing global interests, interest transitions, and short-term interests, plus a **composite relative temporal encoding** with learnable, head-specific bias coefficients. It improves efficiency, beats SOTA, and exhibits a **scaling-law phenomenon across three orders of magnitude in FLOPs**. Online A/B: **+1.72% CTR, +1.41% CPM**. |
| **Key innovations** | Personalized time-chunking specifically for rec (fixing the mismatch of CV/NLP sparse attention); three-branch (global/transition/local) sparse attention; demonstrated rec-scaling law. |
| **arXiv** | [2601.17836](https://arxiv.org/abs/2601.17836) |
| **Why it matters** | Connection to the wiki's CTR **scaling-law** thread — long-behavior sparse attention that actually scales, with production lift numbers. |

### 2.7 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | (academic) |
| **Institution** | Not stated |
| **Submitted** | 2026-06-13 · [2606.07980](https://arxiv.org/abs/2606.07980) · cs.IR |
| **Abstract** | Transformer CTR models bottleneck at the **residual connection**: Pre-Norm dilutes early interest signals, identity skip can't forget stale interests, and each layer sees only its predecessor. Drawing on Dual Path Networks (DPN), **DeRes** routes each layer through two parallel paths — an **Identity residual path** (first-order feature reuse + gradient flow) and a **Block Attention Residual path** (attending over compressed outputs of all earlier blocks for high-order recall), with a vector-wise gate. A **Pointwise AttnRes** replaces Softmax with SiLU so multiple past blocks activate simultaneously and irrelevant ones get negative (forgetting) weights — matched to CTR's parallel multi-interest pattern. Beats 12 baselines (incl. OneTrans, TokenMixer-Large, UniMixer) up to +0.32% AUC at <5% extra FLOPs; fits a steeper compute-AUC scaling law (γ=0.118 vs. 0.071), so 8-layer DeRes ≈ 16-layer OneTrans (~2× compute saving at equal AUC). |
| **Key innovations** | Dual-path (identity + block-attention) residual that preserves the identity skip (dropped by AttnRes); SiLU-based forgetting weights; steep scaling law at near-zero cost. |
| **arXiv** | [2606.07980](https://arxiv.org/abs/2606.07980) |
| **Why it matters** | Contributes to the CTR scaling-law landscape the wiki curates — this is precisely the "steep compute-AUC scaling law" family. |

### 2.8 STAR: Structured Tokenization and Target-Aware Interest Representation for PCVR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | (KDD Cup 2026 Tencent UniRec Challenge team) |
| **Institution** | *(inferred: UniRec challenge)* |
| **Submitted** | 2026-08-18 · [2608.12986](https://arxiv.org/abs/2608.12986) · cs.IR |
| **Abstract** | Practical **post-click conversion rate (PCVR)** framework for the KDD Cup 2026 Tencent UniRec Challenge. Built on a HyFormer-style multi-sequence backbone, **STAR** adds structured feature tokenization plus **target-aware interest representation**: high-cardinality signal recovery (long-tail sparse fields usually skipped), explicit user-item interaction tokens, target-aware sequence decoding, robust missing-value handling, and a weighted user-item **InfoNCE-style contrastive** auxiliary. Aligns train/inference by reconstructing feature-remapping tables from saved config. Main ablation gain is from temporal context, with smaller contributions from contrastive alignment, target-aware interest encoding, and high-cardinality recovery. |
| **Key innovations** | Target-aware interest + contrastive auxiliary on a unified Transformer backbone; practical robustness (high-cardinality, missing values, train-inference consistency) for industrial PCVR. |
| **arXiv** | [2608.12986](https://arxiv.org/abs/2608.12986) |
| **Why it matters** | The KDD Cup 2026 family (with UniDot 2.4) — concrete recipe detail on the unified-backbone thread. |

### 2.9 (Honorable mention) BTS sycophancy & section cross-references
See [1.8](../2026-09-01/arxiv-ai-search.md) for the BTS paper and the generative-rec cross-references ([2.1 GenRec](#21-genrec-an-llm-backed-recommendation-ranker-at-netflix), [2.2 GenCI](#22-genci-generative-modeling-of-user-interest-shift-via-cohort-based-intent-learning-for-ctr-prediction)).

---

## ③ Games & Agentic Reinforcement Learning (6)

### 3.1 Twin: Playing an Unknown Game with a Test-Time Digital Twin

| Field | Detail |
|-------|--------|
| **Authors** | (OpenAI-affiliated; Codex-based) |
| **Institution** | *(inferred: OpenAI — uses "off-the-shelf Codex"; cites OpenAI ARC-AGI-3 blog)* |
| **Submitted** | 2026-08-21 · [2608.14490](https://arxiv.org/abs/2608.14490) · cs.AI |
| **Abstract** | **Test-time World-model Inference (Twin)** uses a frontier coding agent to *write an executable world model* for unknown-grid games (ARC-AGI-3 class) from simulation/interaction alone. Replay validation enforces that no action is taken until the program reproduces every observed transition; each prediction mismatch becomes a counterexample for repair. Clears **179/183 levels (97.8%)**, more efficiently than humans in 88.3%; infers the goal before any reward on 87.2%. Disabling the harness drops mean score 93.3→61.1 and cleared games 23→13. Key finding: the world model is easier than expected — **inferring the right goal is the hard part**. |
| **Key innovations** | Programmatic/harness world-model inference (write + validate + falsify + repair an executable environment); halt-on-mismatch executor; shows harness > base model for continual-learning games. |
| **arXiv** | [2608.14490](https://arxiv.org/abs/2608.14490) |
| **Why it matters** | Strongest recent datum for the wiki's world-model/game thread — complements [WebWorld](curated) and the ARC-AGI-3 programmatic-harness cluster ([OPINE-World], [PRO-LONG], [Continual Harness]). |

### 3.2 CAST: Game Solvers as Turn-Level Teachers for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | (academic) |
| **Institution** | Not stated |
| **Submitted** | 2026-07-25 · [2607.25308](https://arxiv.org/abs/2607.25308) · cs.LG / cs.AI |
| **Abstract** | RL with verifiable rewards (RLVR) on long-horizon games relies on sparse final rewards that reveal little about which decisions mattered. **CAST** observes that changes in a game solver's state value reveal whether an action advances the state toward success, and injects these as turn-level **solver advantages** into RLVR. Under a soft-optimal solver assumption, maximizing the solver advantage is equivalent to on-policy distillation from the solver — needing only scalar values, not teacher logits. Across Sokoban, Minesweeper, Rush Hour it beats all trained baselines on every game (in-domain and unseen difficulty) and gets the highest zero-shot on ALFWorld/WebShop; reaches DAPO's peak in 1.7–2.0× fewer steps. |
| **Key innovations** | Game solvers as a cheap, accurate source of turn-level credit (vs. PRMs/critics/search rollouts); logit-free on-policy distillation equivalence; gains on games + transfer to web-agent tasks. |
| **arXiv** | [2607.25308](https://arxiv.org/abs/2607.25308) |
| **Why it matters** | A novel credit-assignment source for agentic RL — directly relevant to the wiki's agentic-RL/post-training and game-RL threads. |

### 3.3 SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic RL

| Field | Detail |
|-------|--------|
| **Authors** | (academic) |
| **Institution** | Not stated |
| **Submitted** | 2026-08-26 · [2608.19842](https://arxiv.org/abs/2608.19842) · cs.LG / cs.AI |
| **Abstract** | Group-relative, critic-free agentic RL (GRPO-style) avoids PPO's memory overhead but has (1) no explicit value generalization/temporal credit assignment, (2) advantage collapse on long-horizon tasks, (3) a sampling-budget vs. performance trade-off. **SAPO** has policy and value share a **single autoregressive backbone**, producing policy and value predictions at distinct causal boundaries with shared parameters, optimizing PPO + on-policy SARSA objectives. A trajectory-level GAE combines λ-returns with batch normalization. On ALFWorld/WebShop with Qwen2.5-1.5B/7B it trains stably and beats PPO/GRPO by +15.1/+12.1 pp, eliminates the separate-critic memory cost, and cuts per-iteration runtime 33.2% vs. PPO. |
| **Key innovations** | Actor–critic without a separate critic: value estimation inside the same causal autoregressive stream; single-rollout value-based training; efficiency + explicit credit assignment. |
| **arXiv** | [2608.19842](https://arxiv.org/abs/2608.19842) |
| **Why it matters** | Addresses a real tension in the wiki's RL-post-training thread: GRPO saves memory but loses value learning — SAPO gets both. |

### 3.4 AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Zeth Wang et al. |
| **Institution** | Not stated |
| **Submitted** | 2026-08-18 · [2608.05987](https://arxiv.org/abs/2608.05987) · cs.LG / cs.AI |
| **Abstract** | Verifiable-reward RL builds trajectory-level advantage but fails to credit the few pivotal decisions in long-horizon agentic tasks. **AgentOPSD** is a **critic-free, recursive turn-level credit assignment**: it aggregates token-level teacher-student log-probability gaps into turn-level evidence and recursively updates a Bayesian belief state in log-odds space — identifying pivotal turns by the marginal revision between consecutive states, compatible with standard policy optimization and requiring no extra rollouts. On ALFWorld, WebShop, Search-QA (Qwen3B/7B) it beats GRPO and strong self-distillation baselines, reaching **89.1% success on ALFWorld** (Qwen2.5-7B). |
| **Key innovations** | Turn-level aggregation of self-distillation gaps + recursive Bayesian belief revision (history-dependent credit); no critic/rollouts needed. |
| **arXiv** | [2608.05987](https://arxiv.org/abs/2608.05987) |
| **Why it matters** | Extends the OPSD/self-distillation line the wiki tracks (cf. SKILL/Self-Distilled RLVR) to history-dependent recursive credit. |

### 3.5 MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games

| Field | Detail |
|-------|--------|
| **Authors** | Yunfei Xie, Kevin Wang, Bobby Cheng, Jianzhu Yao, Zhizhou Sha, Alexander Duffy, et al. |
| **Institution** | Not stated (OpenVerse AI project) |
| **Submitted** | 2026-03-09 · [2603.09022](https://arxiv.org/abs/2603.09022) · cs.AI / cs.MA |
| **Abstract** | Multi-turn, multi-agent LLM game evaluation suffers **run-to-run variance** (small early deviations compound across turns and are amplified by coupling), biasing win rates and making rankings unreliable. **MEMO** is a weight-free self-play framework that optimizes inference-time context by coupling **retention** (a persistent memory bank distilling trajectories into insights injected as priors) and **exploration** (tournament-style prompt evolution with uncertainty-aware TRUESKILL selection + prioritized replay of rare states). Across five text-based games it raises mean win rate 25.1→49.5% (GPT-4o-mini) and 20.9→44.3% (Qwen-2.5-7B) using 2,000 self-play games, cutting run-to-run variance and using 19× fewer games than RL baselines. Largest gains in negotiation/imperfect-information games; RL remains better in perfect-information settings. |
| **Key innovations** | Context optimization (not weight updates) for game play; memory-retention + tournament-exploration hybrid; reduces variance which is the real eval-killer in multi-agent games. |
| **arXiv** | [2603.09022](https://arxiv.org/abs/2603.09022) |
| **Why it matters** | Both an important paper on *evaluation stability* and a practical game-agent method — connects to the wiki's imperfect-information game and eval-stability threads. |

### 3.6 RCDT: Conditional Sequence Modeling for Safe Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Wensong Bai, Chao Zhang, Qihang Xu, Chufan Chen, Chenhao Zhou, Hui Qian |
| **Institution** | Not stated |
| **Submitted** | 2026-02-09 · [2602.08584](https://arxiv.org/abs/2602.08584) · cs.LG |
| **Abstract** | Offline safe RL policies are usually trained under a fixed cost threshold, limiting zero-shot deployment flexibility. **RCDT** is the first conditional-sequence-modeling (CSM) method for offline safe RL that supports **zero-shot deployment across multiple cost thresholds in a single policy**, integrating a **Lagrangian-style cost penalty with an auto-adaptive penalty coefficient**. To avoid over-conservatism it adds reward–cost-aware trajectory reweighting and Q-value regularization. On the DSRL benchmark it consistently improves return–cost trade-offs over representative baselines. |
| **Key innovations** | CSM/Decision-Transformer recipe applied to *safe* RL with threshold-conditioning; auto-adaptive Lagrangian penalty; SOTA offline safe RL. |
| **arXiv** | [2602.08584](https://arxiv.org/abs/2602.08584) |
| **Why it matters** | The "sequence modeling as RL substrate" thread the wiki tracks — now extended to constrained/safe deployment and threshold flexibility. |

---

## ④ Synthesis notes & links

- **Cross-cutting theme (architecture):** The LLM-efficiency literature is converging on *nested/universal/latent* parameter sharing (Matryoshka 1.1, LatentMoE 1.2, MoUE 1.3) plus systems fixes for sparse-model imbalance (LAER-MoE 1.4). The rec/ad CTR world mirrors this with the unified feature-interaction+sequence backbone race (UniDot 2.4, CADET 2.3, DeRes 2.7).
- **Cross-cutting theme (inference scaling):** Two healthy caveats — EvoResearcher (1.5) bounds the value of reflection to unreliable tasks, and TTS-in-the-wild (1.7) shows reward models can't rank open-ended candidates. Applied TTS should target verifiable domains.
- **Cross-cutting theme (credit assignment):** The game/agent RL literature is attacking sparse credit via solver signals (CAST 3.2), single-backbone value learning (SAPO 3.3), and recursive self-distillation (AgentOPSD 3.4) — each a different cure for the same "which action mattered" problem.
- **Cross-cutting theme (production LLM rankers):** Netflix (GenRec 2.1) and LinkedIn (CADET 2.3) both ship production LLM/transformer rankers with explicit catalog/context-aware heads — evidence the "LLM-the-ranker" bet is real in industry.
- Related wiki pages this extends: [[ctr-scaling-landscape]], [[technical-roadmap]], [[affiliation-landscape]], and the ongoing [arxiv-daily](arxiv-daily.md) digest line.

---

## Appendix — full arXiv listing

| # | arXiv ID | Title | Category |
|---|----------|-------|----------|
| 1.1 | [2608.09703](https://arxiv.org/abs/2608.09703) | Matryoshka Language Model Suites | cs.CL |
| 1.2 | [2601.18089](https://arxiv.org/abs/2601.18089) | LatentMoE | cs.CL/LG |
| 1.3 | [2603.04971](https://arxiv.org/abs/2603.04971) | Mixture of Universal Experts (MoUE) | cs.LG |
| 1.4 | [2602.11686](https://arxiv.org/abs/2602.11686) | LAER-MoE (FSEP) | cs.DC |
| 1.5 | [2608.18884](https://arxiv.org/abs/2608.18884) | EvoResearcher | cs.CL/LG |
| 1.6 | [2608.21766](https://arxiv.org/abs/2608.21766) | Evaluation Awareness in LMs | cs.CL/AI |
| 1.7 | [2608.18931](https://arxiv.org/abs/2608.18931) | TTS in the Wild | cs.CL/LG |
| 1.8 | [2608.25267](https://arxiv.org/abs/2608.25267) | BTS sycophancy mitigation (HM) | cs.LG |
| 2.1 | [2608.10257](https://arxiv.org/abs/2608.10257) | GenRec (Netflix) | cs.IR |
| 2.2 | [2601.18251](https://arxiv.org/abs/2601.18251) | GenCI | cs.IR |
| 2.3 | [2602.11410](https://arxiv.org/abs/2602.11410) | CADET (LinkedIn) | cs.IR |
| 2.4 | [2608.16797](https://arxiv.org/abs/2608.16797) | UniDot | cs.IR |
| 2.5 | [2608.22973](https://arxiv.org/abs/2608.22973) | CRRN (TIR) | cs.IR |
| 2.6 | [2601.17836](https://arxiv.org/abs/2601.17836) | SparseCTR | cs.IR |
| 2.7 | [2606.07980](https://arxiv.org/abs/2606.07980) | DeRes | cs.IR |
| 2.8 | [2608.12986](https://arxiv.org/abs/2608.12986) | STAR (PCVR) | cs.IR |
| 3.1 | [2608.14490](https://arxiv.org/abs/2608.14490) | Twin (digital twin world model) | cs.AI |
| 3.2 | [2607.25308](https://arxiv.org/abs/2607.25308) | CAST | cs.LG/AI |
| 3.3 | [2608.19842](https://arxiv.org/abs/2608.19842) | SAPO | cs.LG/AI |
| 3.4 | [2608.05987](https://arxiv.org/abs/2608.05987) | AgentOPSD | cs.LG/AI |
| 3.5 | [2603.09022](https://arxiv.org/abs/2603.09022) | MEMO | cs.AI/MA |
| 3.6 | [2602.08584](https://arxiv.org/abs/2602.08584) | RCDT (safe RL) | cs.LG |
