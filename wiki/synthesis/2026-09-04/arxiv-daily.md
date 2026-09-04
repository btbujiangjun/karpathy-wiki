---
title: arXiv Daily - 2026-09-04
type: synthesis
created: 2026-09-04
updated: 2026-09-04
tags: [arxiv, daily, LLM, recommendation, CTR, advertising, sequential-modeling, games, AI]
---

# arXiv Daily Report — 2026-09-04

> Curated selection of recent arXiv papers across LLMs, recommendation systems, CTR prediction, advertising, sequential modeling, and games.
>
> **Note on methodology**: The arXiv Atom API was rate-limited (HTTP 429) during this run, so paper data was gathered via websearch over arXiv abstract pages plus cached listing data. This run prioritizes **fresh** papers not yet covered by the 2026-09-01 → 2026-09-03 sibling digests (each entry is verified to be absent from those reports).

---

## Large Language Models (LLMs)

### 1. Language Models Can Control Their Own Attention

| Field | Detail |
|-------|--------|
| **Authors** | (opencode-compiled from arXiv 2609.02737) |
| **Institution** | Academic (long-context inference) |
| **arXiv** | [2609.02737](https://arxiv.org/abs/2609.02737) |
| **Published** | Sep 2026 |

**Abstract**: Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. The authors take an intrinsic approach motivated by the question "wouldn't the model already know which parts of the context are relevant?" Declarative Attention (DA) elicits the model to *declare* where it needs to attend within its chain-of-thought, partitioning generation into three modes: full context, a specific region, and recent output only. The inference engine parses these declarations (like tool calls) and skips most of the KV cache read.

**Key innovations**:
- **Declarative Attention (DA) protocol** — zero-shot, training-free; the model states its attention span in text that a human can read.
- **Three attention modes** (global / focus / local) parsed by the engine, replacing the full KV scan with a small read.
- On Gemma-4-31B and Qwen-3.6-27B across 15 long-context tasks: attended tokens cut by 52.0% / 31.1% with modest accuracy drops (1.27pp / 2.75pp) that shrink with model scale.
- Opens a new axis of sparse attention; results are a floor (prompting-only) with more headroom under training-based methods.

---

### 2. PROSE: Provenance through Relational Organization of Semantic Expression

| Field | Detail |
|-------|--------|
| **Authors** | (opencode-compiled from arXiv 2609.02553) |
| **Institution** | Academic |
| **arXiv** | [2609.02553](https://arxiv.org/abs/2609.02553) |
| **Published** | Sep 2026 |

**Abstract**: As LLMs are redistributed, adapted, and served through opaque APIs, model ownership can no longer be reliably established by inspecting internals or deployment records. PROSE addresses this with behavioral signatures observable through black-box interaction. Rather than fixed query-key associations, PROSE encodes ownership in how the model *semantically organizes* its in-domain conclusions, using Abstract Meaning Representation (AMR) structures internalized as domain-conditioned response behavior.

**Key innovations**:
- **Domain-conditioned semantic fingerprinting** — replaces fixed query sets with a semantic target domain and brittle keys with semantic structures.
- Mixed fine-tuning on structurally verified responses, verified by detecting designated structures in responses to held-out natural queries.
- 100% fingerprint detection rate with no false positives; preserves model utility; robust to quantization, pruning, fine-tuning, prompting, and black-box distillation.

---

### 3. GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions

| Field | Detail |
|-------|--------|
| **Authors** | (opencode-compiled from arXiv 2609.01491) |
| **Institution** | Academic / industry research |
| **arXiv** | [2609.01491](https://arxiv.org/abs/2609.01491) |
| **Published** | Sep 2026 |

**Abstract**: GlossoGen is a platform for studying language evolution in multi-LLM-agent settings. In the SaveVeyru scenario, agents with partial information must communicate under pressure. The authors find that language evolution *does* occur between LLM agents, that the resulting languages are compositional and morphologically productive, and that they deviate from the LLMs' English prior in ways that render them incomprehensible to humans.

**Key innovations**:
- **Emergent private languages** between LLM agents — new, non-English, inscrutable languages (safety/monitorability concern).
- Necessary conditions identified: pressure toward efficiency, model strength, and a "postmortem" stage for agreeing on conventions.
- **Transmission asymmetry**: stronger models create languages, but weaker models can acquire an existing one from usage alone.
- Evidence for **cumulative cultural evolution** in mixed populations of LLM agents.

---

### 4. Beyond Human-Likeness: Mapping the Scientific Critique Profiles of LLMs and Human Reviewers

| Field | Detail |
|-------|--------|
| **Authors** | Yunhan Yang et al. |
| **Institution** | Academic |
| **arXiv** | [2609.01895](https://arxiv.org/abs/2609.01895) |
| **Published** | 1 Sep 2026 |

**Abstract**: This study shifts attention from whether LLMs resemble human reviewers to what *functions* of scientific critique they perform. Using ICLR 2025 peer-review data, it compares human reviews with LLM reviews generated under baseline and expert prompts, annotating point-level text with five theory-guided frameworks (Anderson's knowledge types, Toulmin's argumentation, Graesser's question depth, SOLO cognitive complexity, Hattie's feedback functions).

**Key innovations**:
- **Functional (not similarity) analysis** of LLM peer review via five theory-guided annotation frameworks.
- Human reviewers emphasized scientific framing and revision guidance; LLMs showed higher explanatory depth, integrative reasoning, and explicit argument structuring.
- Expert prompting did not make LLM critique uniformly more human-like — it mainly amplified LLM-specific tendencies (integration, formal argumentation).

---

## Recommendation Systems

### 5. CORAL: An LLM-Native Harness for Production Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Muhammad Rafay Azhar, Yuhang Zhou, et al. |
| **Institution** | Meta |
| **arXiv** | [2609.02730](https://arxiv.org/abs/2609.02730) |
| **Published** | 2 Sep 2026 |

**Abstract**: PRODUCTION — CORAL (Constraint-Optimized Recommender via an Agentic Loop) is an LLM-native harness that closes a continual, closed loop around a live recommender. Each cycle the agent observes operating signals, reasons over a memory of its past decisions and their measured effects, and invokes tools — including a numerical optimizer that keeps every change within a fixed operating budget — to reconfigure the live recommender, after which the measured outcome informs the next cycle. Formulated as a partially observed, non-stationary, constrained optimization problem in which the policy improves in context, without parameter updates.

**Key innovations**:
- **Agentic closed-loop control of a live recommender** — the LLM acts on the recommender's control surface (budget allocation across components) rather than serving recommendations directly.
- **In-context improvement without parameter updates**; budget-feasible changes via a numerical optimizer.
- Evaluated with A/B experiments across two large-scale social platforms: improves engagement (incl. low-signal/new users) at no extra serving cost on one, and delivers substantial efficiency savings without degrading engagement on the other — spanning the engagement–efficiency frontier.
- Path from human-supervised toward autonomous operation under guardrails.

---

### 6. SwapRec: Warming Up Cold Items Through Training-Time Swaps

| Field | Detail |
|-------|--------|
| **Authors** | Marta et al. (Albatross AI / Johannes Kepler University Linz) |
| **Institution** | Albatross AI; Johannes Kepler University Linz |
| **arXiv** | [2609.00913](https://arxiv.org/abs/2609.00913) |
| **Published** | Sep 2026 (DaQuaMRec @ RecSys 2026) |

**Abstract**: Interactions with cold items negatively impact real-time personalization of ID-based recommenders. A common industrial heuristic swaps (replaces) cold-start items with their most similar "warm" neighbor at inference time. This paper demonstrates that sequential models are *not robust* to such swaps, and proposes SwapRec — applying the same swap heuristic at training time.

**Key innovations**:
- **Training-time swaps** make sequential recommenders robust to the inference-time swap heuristic used for item cold-start.
- Applies to SASRec and transformer/ID-based sequential recommenders; three domains (online shopping, movie, music).
- Improves accuracy with cold items and surfaces a larger portion of the cold catalog (better coverage), irrespective of the underlying sequential architecture.
- Simple, no architectural change, no extra training components.

---

## CTR Prediction & Advertising

### 7. ReST: From Language to Behavior — Scaling Sequence Transformers for Industrial Recommendation Ranking

| Field | Detail |
|-------|--------|
| **Authors** | (opencode-compiled from arXiv 2609.01240) |
| **Institution** | Industrial AD platform (production) |
| **arXiv** | [2609.01240](https://arxiv.org/abs/2609.01240) |
| **Published** | Sep 2026 |

**Abstract**: ReST is a recommendation-native Transformer scaling framework. For signal quality, it introduces a sequence encoder with dual-gated attention, rotary positional and temporal embedding, stabilized residual normalization, and training-only auxiliary objectives. For computation asymmetry, it factorizes ranking into a heavy reusable encoder and a lightweight cross decoder with projection-free KV attention and token-specific parameterization — co-designing shared-prefix training with shared-prefix serving for "compute-once, decode-many-times" ranking.

**Key innovations**:
- **Asymmetric encoder–decoder** for behavior-sequence ranking: heavy sequence encoder builds reusable per-user memory; lightweight cross decoder scores many candidates.
- **Compute-once, decode-many-times** — shared-prefix training + serving amortizes prefix computation across candidates within a request.
- Restores consistent scaling along sequence length, depth, and width where LLM-style blocks saturate.
- One-week online A/B test: online AUC +1.31%, core revenue metric +11.93% within a 50 ms P99 budget; fully deployed in production.

---

### 8. PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks

| Field | Detail |
|-------|--------|
| **Authors** | (opencode-compiled from arXiv 2608.30449) |
| **Institution** | Academic |
| **arXiv** | [2608.30449](https://arxiv.org/abs/2608.30449) |
| **Published** | Aug 2026 |

**Abstract**: CTR models vary in feature-interaction design, yet their top networks usually remain a single MLP shared by all examples. Heterogeneous user/item/context subgroups update the same parameters, and weakly aligned learning signals make the aggregate gradient a compromise among competing directions (subgroup gradient competition). PRIME (Plug-in Residual Input-conditioned Mixture of Experts) is a Dense-anchored mixture of low-rank residual experts.

**Key innovations**:
- **Function-preserving conditional residuals** — anchors the original Dense prediction with zero-residual initialization so it matches the Dense baseline exactly at training onset.
- Input-dependent routing weights low-rank experts for example-specific logit corrections; multi-bag aggregation + EMA load biases stabilize conditional estimation.
- Semantic subgroups show 0.23–0.37 lower Top-NN gradient cosine similarity than random groups; PRIME reduces the competition gap by 34.3%.
- Improves mean AUC for 11 of 13 architectures on Avazu and Criteo; beats APG on FiBiNET and DCNv2 in all seed-level comparisons with fewer params / lower latency.

---

## Sequential Modeling & Sequential Recommendation

### 9. SpecTran: Spectral-Aware Transformer-based Adapter for LLM-Enhanced Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Yu Cui, Feng Liu, Zhaoxiang Wang, Changwang Zhang, Jun Wang, Can Wang, Jiawei Chen |
| **Institution** | Academic (Zhejiang University group) |
| **arXiv** | [2601.21986](https://arxiv.org/abs/2601.21986) |
| **Published** | Jan 2026 |

**Abstract**: Traditional sequential recommendation learns low-dimensional item ID embeddings, often ignoring text. LLM-based methods encode text into high-dimensional semantic embeddings and transform them into SR models, but adapter-based methods suffer from dimension collapse while SVD-based methods are rigid and discard spectrum. SpecTran is a spectral-aware transformer-based adapter that operates in the spectral domain, attending to the full spectrum to select and aggregate informative components.

**Key innovations**:
- **Spectral-domain adapter** — attends over the full spectrum instead of pruning to principal components, overcoming both dimension collapse (adapters) and rigidity (SVD).
- **Learnable spectral-position encoding** injects singular-value cues as an inductive bias, guiding attention to salient components and promoting diversity across embedding dimensions.
- Lightweight and model-agnostic; consistent gains on four real-world datasets / three SR backbones, avg +9.17% improvement.

---

### 10. GrIT: Group Informed Transformer for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Adamya Shyam, Venkateswara Rao Kagita, Bharti Rana, Vikas Kumar |
| **Institution** | Indian Institute of Technology (academic) |
| **arXiv** | [2602.19728](https://arxiv.org/abs/2602.19728) |
| **Published** | Feb 2026 |

**Abstract**: Sequential recommenders predict future interests from behavior history using transformer architectures, but often overlook group-level features capturing the collective behavior of similar users. GrIT explicitly models *temporally evolving* group features alongside individual user histories using latent group representations with learnable, time-varying membership weights.

**Key innovations**:
- **Time-varying group membership** — models drift-aware membership weights from both short- and long-term user preferences.
- Latent group embeddings weighted by membership scores are fused with the user's sequential representation inside the transformer block.
- Consistent outperformance over SOTA sequential methods on five benchmark datasets.

---

### 11. GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, Yankai Chen, Wenhao Yu, et al. (Jianting Chen, Irwin King) |
| **Institution** | Academic (WWW 2026) |
| **arXiv** | [2606.11023](https://arxiv.org/abs/2606.11023) |
| **Published** | 2026 (WWW '26) |

**Abstract**: Item representation quality is a bottleneck in sequential recommendation. GenAIR uses an LLM to infer the textual "Archetype" — the conceptual profile of an item's ideal target audience — then grounds these generative archetypes in real-world behavior with a behavioral calibration objective.

**Key innovations**:
- **Archetype grounding (STP framework)** — item identity shaped by target audience, not just attributes.
- **Behavioral calibration objective** — adjusts the embedding space to reflect empirical interaction patterns, closing the gap between semantic representations and actual behavior.
- Seamless integration with existing models, no inference overhead; improves various sequential recommender models on three real-world datasets.

---

## Games & Reinforcement Learning / World Models

### 12. AWoMo: Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models

| Field | Detail |
|-------|--------|
| **Authors** | (opencode-compiled from arXiv 2608.25518) |
| **Institution** | Academic / industry research |
| **arXiv** | [2608.25518](https://arxiv.org/abs/2608.25518) |
| **Published** | Aug 2026 |

**Abstract**: Scaling world models by training on more crawled video is inefficient; it requires a *recursive data engine with grounded reward signals*. Game development provides this: a scene encoded by a game engine is an executable world specification that can be efficiently checked for collision, physics, navigability, and bounded playability, while the developer supplies global acceptance feedback. RLHEV (Reinforcement Learning with Human-Engine Verification) combines dense engine signals with implicit human acceptance feedback.

**Key innovations**:
- **RLHEV post-training paradigm** — dense engine signals + sparse human acceptance rewards, mirroring how code agents get rewards from compilers/runtimes.
- **AWoMo (Agentic World Model)** — a world-building agent that proposes scene edits, observes human-engine verification, and converts accepted/repaired multimodal traces into training data.
- Best on UnitySceneBench; positive cross-engine transfer to Unreal and Godot; AWoMo-augmented data improves embodied performance on R2R, Gymnasium/MuJoCo, and D4RL.

---

### 13. ReWorld: An Interactive World Model with Long-Horizon Memory

| Field | Detail |
|-------|--------|
| **Authors** | Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang, Tianshuo Xu, Yihua Du, Wei Wang, Tianyi Gui, Lianghua Huang, Yingcong Chen |
| **Institution** | Academic (ShanghaiTech / CUHK line) |
| **arXiv** | [2608.23565](https://arxiv.org/abs/2608.23565) |
| **Published** | Aug 2026 |

**Abstract**: An interactive world model must at once follow user actions, remember places already shown, and stream in real time — control wants a short horizon, memory an unbounded one. ReWorld separates the two during training and bounds them at inference via mixed per-head attention windows (most heads local, a small global set) with random head routing and random chunk dropping. At inference a bounded KV cache is backed by a pose-indexed landmark bank.

**Key innovations**:
- **Mixed per-head attention windows + random head routing** — trains both control and memory without binding either capability to particular heads.
- **Bounded memory at inference** — pose-indexed landmark bank under a fixed KV budget; chunk-drop training makes sparse cached histories in-distribution.
- Metric-scale-aligned 8-source data engine (Unreal fly-throughs, game roaming, real footage) on one physical action scale; palindrome trajectories supply revisit evidence.
- 4-step LoRA distillation streams 704×1280 video in real time; best control fidelity and generation quality vs. six recent interactive world models; regenerates the starting view on minute-long rollouts.

---

### 14. ActSWM: Action-Sensitive World Models for Long-Horizon Planning in Open-World Games

| Field | Detail |
|-------|--------|
| **Authors** | (opencode-compiled from arXiv 2607.26712) |
| **Institution** | Academic |
| **arXiv** | [2607.26712](https://arxiv.org/abs/2607.26712) |
| **Published** | Jul 2026 |

**Abstract**: Latent world models support model-predictive control by optimizing future control sequences in latent space, but existing predictors lack stable long-horizon rollout ability. ActSWM identifies **Context Collapse** — a failure mode where autoregressive latent predictors keep high similarity to future states while producing nearly indistinguishable futures under different action sequences. It enforces a transition-separation principle.

**Key innovations**:
- **Transition-separation principle** — a planning-useful latent dynamics model must keep alternative-action futures distinguishable and make the action recoverable from each local transition.
- Action sensitivity enforced as a *constraint on latent rollouts* (rollout branch + frozen action-readout branch), not just an auxiliary prediction target.
- Produces ~380× larger separation between recorded- vs. zero-action rollouts than the strongest baseline; improves task success in long-horizon Minecraft planning and offline action recovery.

---

## Cross-Cutting Observations

- **Agentic recommender control is now an industrial reality**: Meta's CORAL (2609.02730) puts an LLM in a continual closed loop over a production recommender, improving engagement and efficiency via A/B tests — echoing the agentic-recommender trend seen in rec systems (AgentX, Nova, Memrec) surfacing across sibling digests.
- **Scaling behavior-sequence transformers is the active CTR/ranking frontier**: ReST (2609.01240) shows LLM-style blocks saturate while rec-native designs keep scaling (aligning with Taobao EST and Baidu GRAB covered in earlier digests).
- **World models converge on reward/verification scarcity**: AWoMo (2608.25518) argues for game engines as executable verifiers (analogous to code execution for LLM RL), while ReWorld (2608.23565) and ActSWM (2607.26712) push control+memory separation and action-sensitivity for interactive planning.
- **LLM provenance/ownership verification** is an emerging security topic (PROSE, 2609.02553), alongside emergent-language safety concerns (GlossoGen, 2609.01491).

> ⚠️ NOTE: For several entries (marked "opencode-compiled"), the full author/institution lists were not fully captured from the search snippets; IDs, titles, abstracts, and arXiv links are as retrieved. Verify against the arXiv abstract pages before citing in formal writing.
