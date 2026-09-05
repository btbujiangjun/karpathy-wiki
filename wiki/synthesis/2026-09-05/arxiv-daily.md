---
title: arXiv Daily - 2026-09-05
type: synthesis
created: 2026-09-05
updated: 2026-09-05
tags: [arxiv, daily, LLM, recommendation, CTR, advertising, sequential-modeling, games, AI]
---

# arXiv Daily Report — 2026-09-05

> Curated selection of recent arXiv papers across LLMs, recommendation systems, CTR prediction, advertising, sequential modeling, and games.
>
> **Note on methodology**: The arXiv Atom API was rate-limited (HTTP 429) during this run, so paper data was gathered directly from the arXiv listing pages (cs.IR / cs.LG / cs.CL / cs.AI / cs.GT / cs.MA "recent" listings, Fri 4 Sep + Thu 3 Sep mailings) and individual `/abs/` + `/html/` pages. This run prioritizes **fresh** papers from the Fri 4 Sep 2026 mailing (all featured IDs grep-verified absent from the 09-01 → 09-04 sibling digests).

---

## Large Language Models (LLMs)

### 1. Uno: Unlocking Lossless Speedups in LLMs via Discrete Diffusion

| Field | Detail |
|-------|--------|
| **Authors** | Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham, Jonathan Geuter, Chaitanya Dwivedi, Varad Pimpalkhute, Yash Akhauri, Alexander Moreno, Mikhail Yurochkin, Zhenting Wang, Mostafa Elhoushi, Nolan Dey, Shane Bergsma, Joel Hestness, John Thickstun, Eric Xing, Zhengzhong Liu |
| **Institution** | Cerebras-affiliated researchers + academia (CMU / MBZUAI et al.) — *(opencode-compiled)* |
| **arXiv** | [2609.04010](https://arxiv.org/abs/2609.04010) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: LLMs owe their success to next-token prediction (NTP), but the autoregressive (AR) structure requires slow, sequential token generation. The authors introduce *diffusion-augmented LLMs* — a class that defines an AR model distribution while using diffusion to draw multiple tokens in parallel from that distribution. Model parameters are decoupled into two sets: AR weights (standard NTP objective) and lightweight diffusion weights trained to generate several tokens simultaneously, learned via a simple Diffusion Distillation phase that adds negligible overhead.

**Key innovations**:
- **Decoupled AR + diffusion weights** — augment existing open-weight AR LLMs or train from scratch; the AR model's quality is preserved by construction.
- **Ψ-Spec sampler family** — lossless acceleration and inference-time scaling at fixed context length; *no separate draft model* (unlike speculative decoding), and no quality loss (unlike d-LLMs).
- Uno = 8B: **up to 3× speedup** over the base AR model at full batch size; higher throughput than leading speculative-decoding at every batch size.
- Uno 8B beats the leading open d-LLM (26B DiffusionGemma) and proprietary Mercury 2 on agentic tool use, coding, and long-context reasoning.

---

### 2. Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM

| Field | Detail |
|-------|--------|
| **Authors** | Sergii Kozyrev, Davyd Maiboroda |
| **Institution** | Independent / community quantization researchers — *(opencode-compiled)* |
| **arXiv** | [2609.04098](https://arxiv.org/abs/2609.04098) |
| **Submitted** | 3 Sep 2026 (cs.AI) |

**Abstract**: Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes context in a fixed size. Early community 4-bit quantizations of Qwen3.8-27B left the GDN block (48 of 64 layers) in 8–16-bit on the intuition that recurrent error accumulates over long contexts. The authors test that intuition with *Minima*: NVFP4 W4A4 on all 496 linear layers, GDN included.

**Key innovations**:
- **Quantize everything, ship KV scales** — Minima matches BF16 within seed noise (5-task avg −0.52) while being the smallest (17.5 GiB) and fastest-prefill (+14–19%) recipe compared; 32K perplexity gap shrinks with position; max RULER retrieval to 64K.
- **Four-part mechanism study**: (i) NVFP4's 16-element block scaling localizes residual-stream extreme outliers; (ii) the supposedly fragile gate projections are the *least* sensitive (softplus/exp + sigmoid compress ~11% GEMM error to ~2%); (iii) the delta-rule recurrence holds injected noise at a flat plateau over 32K tokens — each write overwrites the state along the current key direction; (iv) per-token quantization cost washes out with context.
- Also repairs a global-scale mismatch when per-module-calibrated NVFP4 checkpoints are served by module-fusing kernels, and shows calibrated FP8 KV-cache scales are performance-free.
- Takeaway: **the recurrent half of a hybrid LLM is the easy half to quantize.**

---

### 3. Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR

| Field | Detail |
|-------|--------|
| **Authors** | Boyan Li, Bingsen Chen, Chenghao Yang, Ping Nie, Chen Zhao, Xi Ye |
| **Institution** | Academic (University of Chicago / University of Waterloo / University of Alberta) |
| **arXiv** | [2609.04108](https://arxiv.org/abs/2609.04108) |
| **Submitted** | 3 Sep 2026 (cs.CL) |

**Abstract**: RLVR and on-policy distillation (OPD) are the two dominant post-training methods for reasoning LLMs. Prior work fuses their signals within a single step (weighted-additive combination or teacher-modulated rescaling of the RL advantage). This paper shows a simple **two-stage scheme, OPD-then-RL, consistently outperforms pure OPD, pure RLVR, and all joint baselines** across logic and math reasoning.

**Key innovations**:
- **OPD expands coverage, RL sharpens within it** — a unified explanation from pass@k, learning dynamics, and parameter updates; jointly optimizing both signals causes the two to interfere.
- **Practical recipe**: the OPD validation score is the key signal for when to switch to RL; OPD is a better cold start for RL than SFT.
- Positions OPD and RLVR as *complementary stages* rather than entangled signals.

---

### 4. Spurious Advantage Hidden in GRPO

| Field | Detail |
|-------|--------|
| **Authors** | Jiamian Wang, Samyadeep Basu, Koustava Goswami, Tong Yu, Zhiqiang Tao |
| **Institution** | Adobe-affiliated researchers + academic — *(opencode-compiled)* |
| **arXiv** | [2609.04063](https://arxiv.org/abs/2609.04063) |
| **Submitted** | 3 Sep 2026 (cs.AI) |

**Abstract**: GRPO's advantage estimator assigns each rollout a magnitude from within-group reward statistics. In the common case this rewards rollouts that reach the correct answer through reasoning. But an overlooked case shares the same surface: a rollout may land on the answer by guessing, and GRPO still assigns a high magnitude — the *spurious advantage*. It arises in: bounded-answer tasks with small candidate sets; open-answer sets hosting bounded sub-cases; and search agents whose budget opens many paths to the same answer.

**Key innovations**:
- Identifies a guess-vs-reason blind spot in GRPO's group-relative advantage.
- **SIGNBALANCE** — a composition-free magnitude: keeps the verifier sign, uses a global scale, and restores zero-mean balance via stop-gradient per-class rescaling.
- Matches GRPO on open-answer math while **improving bounded-answer math and search agents**; code to be released.

---

### 5. Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Heng Wang, Jielin Qiu, Wenting Zhao, Cheng Qian, Liangwei Yang, Jiawei Han, Heng Ji, Silvio Savarese, Shelby Heinecke, Huan Wang |
| **Institution** | Academic + industry (University of Illinois Urbana-Champaign / Salesforce AI Research) |
| **arXiv** | [2609.03430](https://arxiv.org/abs/2609.03430) |
| **Submitted** | 3 Sep 2026 (cs.CL) |

**Abstract**: Long chains of thought make the KV cache a severe memory bottleneck. Existing compression methods share one paradigm — score each cached token by estimated future importance and keep the top-scoring ones. The authors show **the selection signal contributes almost nothing**: Random Attention keeps the prompt and evicts *uniformly at random* within each attention head, computing no score at all.

**Key innovations**:
- Matches the strongest prior evictor across four models and six reasoning tasks while serving **32–43% higher throughput** in vLLM deployment.
- **Two controlled explanations**: (1) the *prompt* is the fragile part of the cache — most of the gap between selectors is just whether they kept it; (2) the reasoning trace protects itself with redundancy at two levels — in the text (the model restates what it needs) and across heads (each keeps its own copy) — so once the prompt is safe, a random draw suffices.
- Cost-free alternative to scoring-based eviction for reasoning tasks; code public.

---

### 6. response Doesn't Stop Reasoning: Analysis of Spurious CoT Termination

| Field | Detail |
|-------|--------|
| **Authors** | Seunghee Koh, Sungjae Choi, Minchan Kwon, Sunghyun Baek, Junmo Kim |
| **Institution** | Academic (KAIST) |
| **arXiv** | [2609.03633](https://arxiv.org/abs/2609.03633) |
| **Submitted** | 3 Sep 2026 (cs.CL) — **EMNLP 2026 Main Conference** |

**Abstract**: Training-free early-exit methods shorten long CoT traces by injecting an end-of-think token (EoT, `</think>`) at an intermediate point to trigger the reasoning→answering transition. The authors find the injected EoT **does not always induce a clean answering phase**: answering-phase generation can continue before the model regenerates another EoT, the span scaling with the reasoning tokens saved — *spurious CoT termination*, where reasoning-like generation bleeds into the answering phase.

**Key innovations**:
- Documents and characterizes a failure mode of token-injection-based early exit in reasoning models.
- **Exit-token Attention Biasing (EAB)** — biasing attention toward the injected EoT reduces spurious termination and answering-phase length across four LRMs, five benchmarks, and two early-exit methods.
- Broader lesson: controlling LRMs by externally matching their explicit `<think>...</think>` format does not by itself guarantee the intended reasoning→answering transition.

---

### 7. RecurTrace: Adaptive Latent Reasoning with Loop-Time Memory

| Field | Detail |
|-------|--------|
| **Authors** | Yuxiang Wang, Kunyu Feng, Yingda Shen, Haoning Xu, Junyu Wang, Zhizheng Wu |
| **Institution** | Academic / industry research (Shanghai AI Laboratory-affiliated authors) — *(opencode-compiled)* |
| **arXiv** | [2609.03379](https://arxiv.org/abs/2609.03379) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: Repeating a small block of middle layers increases an LM's effective inference depth without adding parameters or tokens; recent work shows this latent recurrence improves reasoning. Two design choices limit the gains: each loop iteration sees only its previous output (no access to earlier computations), and a fixed loop count wastes depth on easy inputs while shortchanging hard ones. RecurTrace addresses both using the loop's own trajectory.

**Key innovations**:
- **Loop Memory Attention** — each looped layer attends to its own states from previous iterations along the loop-time axis, enabling the model to revisit earlier computations.
- **Halting head** — predicts whether to continue, trained with oracle supervision that identifies when extra depth still reduces loss (adaptive loop count).
- MathQA on a controlled looped backbone: **56.9% with ~2.0 loops** vs best fixed loop-depth 54.7% at matched compute; ACT/PonderNet collapse to one loop; CALM reaches 54.1% at 5.6 loops.
- Gains grow with scale: +0.6 → +3.4 points over same-budget fine-tuned baselines from 0.6B to 8B.

---

## Recommendation Systems

### 8. SelfDR: Self-Distillation from Reasoning for LLM-Based Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Chumeng Jiang, Jiayin Wang, Xinjie Lin, Zhiqiang Guo, Hengliang Luo, Min Zhang |
| **Institution** | Academic + industry (Tsinghua University DCST / Quan Cheng Laboratory / Meituan) |
| **arXiv** | [2609.03313](https://arxiv.org/abs/2609.03313) |
| **Submitted** | 3 Sep 2026 (cs.IR) — **CIKM 2026** |

**Abstract**: Reasoning is widely used to help LLM-based recommenders interpret textual signals, but generating intermediate reasoning traces at inference is computationally expensive. SelfDR distills the LLM's *own* reasoning-enhanced predictions into direct recommendations, improving effectiveness while keeping inference efficient — all components on the same base LLM, no external models.

**Key innovations**:
- **Teacher = reasoner** trained with downstream performance as the reward, so it generates targeted rationales; a student for direct recommendation learns via **self-distillation with dynamic weighting**.
- Single-model architecture (no external teacher) — self-improvement within one backbone.
- Validates effectiveness, rationality, and efficiency on three public datasets; fixes the deployment pain point of reasoning-heavy LLM recommenders.

---

### 9. EPIC: Explicit Posterior Item Conditioning for Semantic ID Diffusion Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Tuan-Binh Tran, Thanh Tam Nguyen, Quoc Viet Hung Nguyen, Dung D. Le, Tung Kieu, Thanh Trung Huynh |
| **Institution** | Academic (VinUniversity / Griffith University / Aalborg University) |
| **arXiv** | [2609.03522](https://arxiv.org/abs/2609.03522) |
| **Submitted** | 3 Sep 2026 (cs.IR) |

**Abstract**: Semantic ID (SID) generative recommendation predicts the next item by generating a short tuple of discrete tokens; masked-diffusion methods improve this via bidirectional context and flexible decoding. But at each denoising step a partial SID can correspond to multiple feasible items, and existing methods mostly reason through position-wise token predictions. EPIC introduces **explicit item-level competition** into SID denoising.

**Key innovations**:
- **Item-level posterior over feasible candidates** built from the current generation context + the user's recent interactions, then projected back onto unresolved SID positions to guide token decisions — injecting personalized *transition evidence* into denoising.
- Frozen pretrained backbone, **no additional decoder forward pass**.
- Consistent gains over strong baselines on four Amazon benchmarks; ablations confirm the gains come from preserving promising item hypotheses during denoising.

---

### 10. HypRQ-VAE: Hyperbolic Item Indexing for Long-Tail-Aware Generative Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Longfeng Wu, Tong Zeng, Giovanni Seni, Zhimin Peng, Bhanu Pratap Singh Rawat, Si Zhang, Yao Zhou, Lecheng Zheng, Bo Ji, Yujun Yan, Dawei Zhou |
| **Institution** | Industry + academic (Amazon-affiliated + Virginia Tech et al.) — *(opencode-compiled)* |
| **arXiv** | [2609.03369](https://arxiv.org/abs/2609.03369) |
| **Submitted** | 3 Sep 2026 (cs.IR) — **ICDM 2026** |

**Abstract**: Generative recommender systems cast recommendation as language modeling, but LLMs operate on text tokens while recommenders depend on discrete item indices — a mismatch that causes hallucinations. Existing methods learn item vocabularies in Euclidean space and struggle with the long-tail distribution of real catalogs (few head items dominate, vast tail reflects niche tastes). HypRQ-VAE is the first framework to **learn item indexing in hyperbolic space**.

**Key innovations**:
- Hyperbolic Residual-Quantized VAE — hyperbolic geometry's exponential volume expansion naturally accommodates the power-law structure of user–item interactions (hierarchies and sparsity).
- **Long-tail-aware**: significantly improves recommendation of tail items on three benchmarks while preserving head-item fidelity.
- Attributes gains to hyperbolic capacity for modeling item hierarchies and sparsity; code and data released.

---

### 11. MGDiff: Multi-Interest Sequence Recommendation with Masking GNN-Guided Diffusion

| Field | Detail |
|-------|--------|
| **Authors** | Wenjing Xiao, Hao Ding |
| **Institution** | Industry (Amazon-affiliated) — *(opencode-compiled)* |
| **arXiv** | [2609.01619](https://arxiv.org/abs/2609.01619) |
| **Submitted** | 30 Jun 2026 (cs.IR) |

**Abstract**: Multi-interest diffusion framework for sequential recommendation. MGDiff generates accurate, bias-free user interest information during the diffusion process via two mechanisms: a semantics-enhanced Dual-layer Semantic Guidance (DSG) framework and a Popularity-Aware Guidance (PAG) mechanism.

**Key innovations**:
- **DSG (Dual-layer Semantic Guidance)** — decomposes guidance into extracting latent item semantics + decoupling multidimensional user intent; a Weight-adaptive Masking GNN reconstructs missing links to uncover deep item relationships beyond co-occurrence; a Dynamic Multi-Expert Network projects preferences into distinct semantic subspaces.
- **PAG (Popularity-Aware Guidance)** — item popularity used as a differentiable signal to recalibrate similarity metrics, yielding diverse, popularity-bias-free recommendations.
- Outperforms baselines across four widely used datasets.

---

## CTR Prediction & Advertising

### 12. UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Jiajun Cui, Zhengqi Xu, Fan Zhang, Zhangteng, Gu Tang, Honghong Zhu, Mengxi Wu, Yulin Liang, Xingxing Wang |
| **Institution** | Meituan (industry, production) |
| **arXiv** | [2609.03290](https://arxiv.org/abs/2609.03290) |
| **Submitted** | 3 Sep 2026 (cs.IR) |

**Abstract**: Unified CTR modeling typically unifies sequential and non-sequential signals at the token level in a shared backbone. UniCon argues this division originates from legacy feature engineering and is misaligned with the underlying decision process: user behavior is inherently a sequence of homogeneous *context units*, and history and the current request differ only in whether outcomes are observed. Treating them as heterogeneous signals obscures structural dependencies.

**Key innovations**:
- **Context as the basic modeling unit** — history and prediction targets organized as homogeneous context units; intra-context attention captures local item coupling (**Locality**), inter-context attention models evolution of decision states (**Dynamics**).
- Bridges the structural gap between history and target for more effective scaling of unified CTR models; context-unit-level sequence compression reduces deployment overhead.
- **Production results (Meituan search advertising)**: offline AUC **+0.0139** over a strong production baseline; online A/B **+3.09% RPM / +2.07% CTR / +2.95% revenue** (statistically significant). Reinforces the 2026 trend of context-centric scaling in industrial CTR (cf. ReST, 2609.01240).

---

### 13. Marginal Expected Revenue for Jointly Ranking Auction and Fixed-Price Listings in E-Commerce Sponsored Search

| Field | Detail |
|-------|--------|
| **Authors** | Greg Kocher, Sanjana Arun |
| **Institution** | eBay (industry) |
| **arXiv** | [2609.01628](https://arxiv.org/abs/2609.01628) |
| **Submitted** | 8 Aug 2026 (cs.IR) — **SIGIR eCom '26 Workshop** |

**Abstract**: E-commerce ranking must balance relevance, engagement, and revenue when slotting competing listings. Expected-revenue estimation is well understood for fixed-price items but hard for mixed marketplace formats — pure auctions and hybrid "Auction with Buy It Now" (ABIN) items, where prices evolve and final transaction value is unknown at ranking time. Auction/ABIN listings are a meaningful share of eBay's inventory.

**Key innovations**:
- **Marginal eCPM (meCPM)** — extends the standard eCPM framework to auction and ABIN listings, capturing the *incremental value of one more impression* of a still-evolving-price item; unifies fixed-price, auction, and ABIN ranking under one objective.
- Production implementation approximates the objective and bootstraps cold-start from existing engagement models.
- Online A/B tests at a large e-commerce platform: **positive revenue gains + statistically significant user-metric improvements**; deployed to production.

---

## Sequential Modeling & Time-Series

### 14. RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting

| Field | Detail |
|-------|--------|
| **Authors** | Yuchen He, Yueyang Cang, Zhiyuan Ning, Ningyu Wang, Li Shi |
| **Institution** | Academic / industry research — *(opencode-compiled)* |
| **arXiv** | [2609.03937](https://arxiv.org/abs/2609.03937) |
| **Submitted** | 3 Sep 2026 (cs.LG) |

**Abstract**: RAG complements parametric models with retrieved external evidence; the same idea is attractive for continuous-output regression, but directly reusing retrieved target values is not robust when samples differ in output level, scale, or local dynamics. RATL shifts the retrieved object **from historical target values to base-model-specific historical forecast residuals**.

**Key innovations**:
- **Residual-retrieval + feedback correction** — freezes a base forecaster (iTransformer in the main experiments), turns its historical forecast residuals into a train-only, base-specific memory, applies causal-availability constraints at retrieval.
- **Set-aware router** operating over forecast blocks and variables selects and combines retrieved residual trajectories; validation-based correction-strength selection limits harmful feedback.
- Improves frozen base forecasters in most settings, transfers across backbones, and outperforms strong forecasting baselines on real-world multivariate benchmarks.

---

## Games & Reinforcement Learning

### 15. Turn-Based Combat Arena: A New Framework for Multiagent Training and Game Balancing

| Field | Detail |
|-------|--------|
| **Authors** | V. M. Vasyuta, V. V. Malitskyi, O. S. Kushnir, B. I. Horon, V. A. Franiv |
| **Institution** | Academic (Ivan Franko National University of Lviv) |
| **arXiv** | [2609.03122](https://arxiv.org/abs/2609.03122) |
| **Submitted** | 2 Sep 2026 (cs.GT) |

**Abstract**: First in a series on Turn-Based Combat Arena, a configurable framework for turn-based strategy games designed for efficient ML agent training and evaluation. Rules and parameters are flexibly modifiable for rapid experimentation; the architecture supports high-throughput simulation — tens of thousands of games per second and billions of gameplay records on a single machine.

**Key innovations**:
- **Balancing as optimization** — several optimization approaches converge to comparable, robust unit-balance configurations.
- Positions the arena as a practical platform for both game-design analysis and agent training; throughput + scale are the headline engineering contribution.

---

### 16. LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent Combat Games

| Field | Detail |
|-------|--------|
| **Authors** | Hrithika Deepu Nair, Kayvan Karim |
| **Institution** | Academic (Heriot-Watt University) |
| **arXiv** | [2609.02931](https://arxiv.org/abs/2609.02931) |
| **Submitted** | 27 Aug 2026 (cs.MA) |

**Abstract**: RL NPCs typically keep a fixed policy after training and cannot adapt to different opponents. The authors test a runtime strategy-selection framework where a locally hosted **Mistral 7B LLM reads the live game state every five seconds and assigns one of four tactical tags**, guiding a shared PPO policy without modifying it. Evaluated across 600 episodes against three scripted opponents (Mann-Whitney U).

**Key innovations**:
- **Training-free LLM strategy selection over a fixed RL policy** — explicit demonstration against a Balanced opponent that changes tactics mid-episode: win rate **11% → 24%**, longer episodes.
- Honest failure analysis: against an Aggressive opponent, the LLM's near-constant "Surround" preference was counterproductive; Surround selected in **83.8% of 2,430 selections** regardless of opponent — limited zero-shot strategic differentiation at 7B scale.
- A clean, critical read on the potential *and* limits of LLM-guided runtime game AI.

---

### 17. Towards Scaling Reinforcement Learning to Massive Populations: Learning Mean-Field Representations

| Field | Detail |
|-------|--------|
| **Authors** | Aditya Makkar, Benjamin Unger, Jeongyeol Kwon, Mathieu Laurière, Eugene Vinitsky, Yonathan Efroni |
| **Institution** | Academic + industry (NYU / Courant Institute, Meta FAIR-affiliated) — *(opencode-compiled)* |
| **arXiv** | [2609.02928](https://arxiv.org/abs/2609.02928) |
| **Submitted** | 26 Aug 2026 (cs.MA) |

**Abstract**: Modern multi-agent systems deploy over massive populations (ad-auctions, traffic routing, recommendations). The dominant approach optimizes each policy independently, treating others as a fixed environment. Mean-field RL exploits the fact that dynamics depend on an aggregate population statistic, but modeling the full population distribution is intractable in high-dimensional control. This work studies the question from a **representation-learning** perspective.

**Key innovations**:
- **Low-dimensional aggregate-statistic assumption** — rewards/transitions depend on the population only through an unknown low-dim statistic; provable offline algorithm learns a near-optimal policy from that representation.
- Designed and tested on a one-step routing game motivated by supply-chain optimization: with matched parameter count and optimization budget, learning a low-dim population representation improves **reward prediction and Nash-gap/equilibrium quality** over structure-ignoring baselines.
- A principled bridge from large-population multi-agent RL to representation learning.

---

### 18. PokaiTrainer: Scaling Belief-State Search to Competitive Pokémon VGC

| Field | Detail |
|-------|--------|
| **Authors** | Max Yu |
| **Institution** | Independent researcher |
| **arXiv** | [2608.29197](https://arxiv.org/abs/2608.29197) |
| **Submitted** | 29 Aug 2026 (cs.LG / cs.GT) |

**Abstract**: Decision-time equilibrium search carried poker to superhuman play but relied on tractable subgames. Competitive Pokémon VGC breaks all assumptions at once: simultaneous actions from joint menus in the hundreds, hundreds of stochastic outcomes per joint action, and hidden opponent reserves/stat allocations. PokaiTrainer reports what building a strong VGC agent took.

**Key innovations**:
- **PokaiEngine** (Rust battle engine) — enumerates a joint action's full weighted outcome distribution in one pass at ~99% parity with Pokémon Showdown, far cheaper than sampling.
- **PokaiTrainer** adapts Student of Games to this scale: every decision solved as a **Bayesian matrix game over public belief states**, subgames grown under an explicit compute budget.
- Live Showdown best-of-three: **59% wins** over a human field averaging ~1320 Elo; settles into a 1350–1400 Elo band, briefly entering the format's **top 500**.

---

## Cross-Cutting Observations

- **Parallel token generation is moving inside the objective**: Uno (2609.04010) shows discrete-diffusion-augmented AR LLMs can keep the AR distribution while decoding multiple tokens at once — a "lossless acceleration" alternative to speculative decoding that trades a tiny diffusion-head for up to 3× throughput, and beats far larger open d-LLMs.
- **The recurrent half of hybrid LLMs quantizes cleanly**: Minima (2609.04098) overturns the community intuition that GDN recurrence is fragile under 4-bit — mechanisms (outlier-localizing block scaling, robust gate parameterizations, delta-rule noise forgetting) make "quantize everything, ship KV scales" the practical recipe.
- **Post-training reasoning keeps self-correcting**: sequential OPD-then-RL beats every joint fusion baseline (2609.04108); GRPO's guess-rewarding blind spot is isolated and fixed with a composition-free advantage (2609.04063) — both echo the OPD-reliability / GRPO-mechanics thread running through late-August digests.
- **KV eviction's selection signal is largely placebo** for reasoning workloads: Random Attention (2609.03430) matches the best scorer while evicting at random within heads — cheap, and a direct challenge to scoring-based eviction research. Relatedly, `</think>`-injection early exit has a documented failure mode (spurious CoT termination, 2609.03633); attention biasing, not format-conformance, is the fix.
- **Context-centric CTR scaling continues**: UniCon (2609.03290) makes the request context — not tokens — the atomic modeling unit at Meituan, with strong online lifts (+3.09% RPM / +2.95% revenue), extending the industrial sequence/context-scaling story (ReST 2609.01240, EST, GRAB) into unified context modeling.
- **Auction-grounded revenue ranking**: eBay's meCPM (2609.01628) unifies fixed-price/auction/ABIN ranking under a marginal-eCPM objective — revenue-aware ranking keeps expanding into mixed-inventory marketplaces.
- **Generative rec matures along spatial/hyperspectral axes**: hyperbolic item indexing for long-tail coverage (HypRQ-VAE, 2609.03369), explicit item-level posterior competition inside SID diffusion (EPIC, 2609.03522), and GNN-guided multi-interest diffusion with popularity de-biasing (MGDiff, 2609.01619) — all three push beyond plain token-level generative rec.
- **Games: LLM-guided runtime control and belief-state scaling**: an honest negative/positive read on Mistral-7B tactical tagging over a PPO NPC policy (2609.02931, win rate 11→24% but strategy-selection collapse); belief-state Bayesian matrix-game search finally reaches simultaneous-action, high-stochasticity VGC (2608.29197); and mean-field RL gets a representation-learning treatment for massive populations (2609.02928).

> ⚠️ NOTE: Several entries (marked "opencode-compiled") have institutions/companies inferred from author names, affiliations embedded in papers/HTML versions, or domain knowledge; the arXiv abstract pages do not carry a canonical institution field. Verify against the arXiv `/html/` pages or the papers before citing institution names in formal writing. Titles, IDs, abstracts, and arXiv links are as retrieved from arxiv.org on 2026-09-05.