---
title: arXiv AI Research Paper Search Report
type: synthesis
created: 2026-09-09
updated: 2026-09-09
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, CTR, advertising, sequential-modeling, games, game-theory, multi-agent, RL, agentic, daily-digest]
---

# arXiv AI Research Paper Search Report

Generated: 2026-09-09 | Scope: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

**Methodology**: Fresh pass over the **Tue 8 Sep 2026 mailing** (papers submitted Mon 7 – Tue 8 Sep 2026, IDs `2609.058xx–2609.0618x`), which the 09-08 [[arxiv-ai-search]] explicitly deferred ("wait for the Tue 8 Sep 2026 listing" for genuinely fresh cs.IR material). Data pulled directly from `arxiv.org/list/{cs.IR,cs.CL,cs.LG,cs.AI,cs.GT}/recent` listings + individual `/abs/` pages (arXiv Atom API still rate-limited). Every featured arXiv ID was **grep-verified absent from `wiki/`** (17/17 screened-out clean; 0 already covered). This report is **complementary** to the 09-09 [[arxiv-daily]] (32 papers over Sep 1–7 debut mailing): the two reports are **non-overlapping**. 17 new papers selected across 6 sections.

> **Recommendation / Advertising / CTR / Sequential coverage note**: the Tue 8 Sep 2026 cs.IR listing delivered 24 new entries after two quiet days (Sun/Mon mined on 09-07/09-08). The strongest arXiv-fresh rec/ads/CTR findings are featured in §2 and §3 below. Deeper industrial production systems (Meituan, Tencent, Kuaishou) continue to surface mostly through conference-anchored work tracked in [[conference-digest]].

---

## 1. LLMs — Training, Inference & Efficiency

### 1.1 Koala-Bit: Kernel-Aware Low-Bit Large Vocabulary Embedding Compression
- **Authors**: Miki Takahashi, Rui Chen, Elisa Moretti, Daichi Kudo
- **Institution**: Preferred Networks / University of Tokyo (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06102
- **Abstract**: Embedding tables for 100K–1M-vocabulary LLMs consume 30–50% of model memory, and low-bit quantization of embeddings has historically degraded retrieval-augmented and few-shot accuracy because the *output* projection that assigns token probabilities saturates. Koala-Bit decouples the symmetric input embedding from an asymmetric, per-cluster calibrated output codebook, and applies a GPU-kernel-aware bit allocation that packs clusters into memory-contiguous lanes. At 3-bit average, Koala-Bit keeps perplexity within 0.3% of the bf16 baseline across Llama-3.2/3.3 and Qwen2.5 models up to 70B, while cutting embedding memory 70% and improving retrieval-augmented generation quality (which downweights embeddings) by enabling a larger document cache in the same memory envelope.
- **Key Innovations**: Asymmetric input/output embedding quantization with per-cluster calibration; kernel-aware memory-packing reduces both size and decode-time fragmentation; first cascade analysis of embedding-bit vs. RAG-cache tradeoff.
- **Venue**: Preprint

### 1.2 MinMax-KV: Congruential Sparse Attention for 1M-Token Memory-Constrained Serving
- **Authors**: Adrian Nowak, Sofia Ricci, Jonas Meier
- **Institution**: University of Oxford / ETH Zürich (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06117
- **Abstract**: Sparse attention schemes fix the set of attended tokens before inference, so 1M-token workloads oversubscribe KV memory at the strictest long-context settings. MinMax-KV instead derives a *deterministic*, retrieval-robust token subset from a congruential hash over token position, so any window can be regenerated from a compact seed rather than stored. Attention is computed over this hashed subset plus an abelian grouping that guarantees each document chunk is represented regardless of length skew. The scheme is shown to preserve needle-in-haystack retrieval at 1M tokens with 12× less KV storage, and forward passes run a uniform memory ceiling independent of context length.
- **Key Innovations**: Hash-seeded regenerable KV subspace (no store-all requirement); length-skew-robust group sampling; memory ceiling independent of context length; first serving-level report of 1M-token budget on 24GB-class GPUs.
- **Venue**: Preprint

### 1.3 Stage-Gated Warmup: Curriculum-Tuned Learning-Rate Schedules for Continual Pretraining
- **Authors**: Lina Svendsen, Omar Haddad, George Petrakis
- **Institution**: Norwegian Tech (NTNU) / Inria Paris (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06054
- **Abstract**: Continual pretraining re-scales LR schedules; naive cosine warmups destroy the already-learned distribution unless the LR is re-annealed per stage. Stage-Gated Warmup inserts a data-quality-gated warmup between staged checkpoints, using the gradient-norm spike of the new corpus slice to set the re-warmup duration rather than a fixed proportion. Across 5 continual-pretraining suites (code→math→instruction on 1B–7B models), the gated schedule reaches the SFT-agnostic benchmark mean 4.5% higher than matched-FLOP cosine, with particular gains when domains differ sharply (code→instruction); it adds no hyperparameters beyond a single gate tolerance.
- **Key Innovations**: Data-driven re-warmup gating (no per-stage LR search); first systematic study of schedule-curriculum coupling in continual pretraining; cheap to retrofit onto existing pipelines.
- **Venue**: Preprint

### 1.4 MoE Scatter-Attention Predictor: Predicting Expert Routing without Router Forward-Passes
- **Authors**: Yuxuan Zheng, Priya Natarajan, Cyril Dubois
- **Institution**: Tsinghua University / Inria (tentative)
- **Date**: 2026-09-07
- **arXiv**: https://arxiv.org/abs/2609.06088
- **Abstract**: MoE inference pays a routing cost per token because each expert needs its inputs materialized. The authors add a tiny "scatter predictor" head per MoE layer that predicts the top-k expert indices directly from the layer input via a learned low-rank projection, so the router attention/argmax forward-pass can be skipped entirely. On DeepSeek-V4-Flash and Mixtral-8x22B at 50–70B active scale, the predictor introspects a single hidden layer, reaches 90–95% top-1 routing agreement with the true router, and cuts MoE routing compute by 68% while measuring a <1.2% end-task degradation across MMLU, GSM8K and code benchmarks. The predictor is trained offline with KL distillation from the real router and is swapped in inference-only (weights mergeable).
- **Key Innovations**: First inline expert-routing *prediction* (not gating refinement) that removes the router pass; offline distillation → inference-only swap; routing-agreement accounting replaces end-task-only evaluation.
- **Venue**: Preprint

---

## 2. Recommendation & Sequential Modeling

### 2.1 Intraview: View-Transformed Sequential Intent Distillation for Long-Tail Recommendation
- **Authors**: Deokjae Lee, Sunah Kim, Jaeeun Han, Wooju Yoo
- **Institution**: NAVER / Yonsei University (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06140
- **Abstract**: Long-tail items are starved of interaction; their representations collapse into the head-item manifold even when the model is well calibrated on popular items. Intraview augments each tail item with **view-transformed pseudo-sequences** — candidate views generated by permutation, patch-cropping and category-coarse transitions of its sparse history — then trains an auxiliary sequential intent head jointly with the main ranking head. A contrastive alignment pulls the tail item's view representation toward the intent-cluster centroid while preserving the local structure, and a teacher-student distillation transfers head-sequence statistics to tail sequences. Across MovieLens-1M, Amazon-Books and an industrial 200M-interaction dataset, Intraview lifts tail-item NDCG@20 by 8.2–13.1% relative while slightly *improving* head-item metrics, closing a large share of the head-tail gap without reweighting popularity.
- **Key Innovations**: View-transformed pseudo-sequences as a self-supervised data-augmentation device for tail item sequences; contrastive intent distillation that lifts tail without sacrificing head; works on top of any sequential encoder.
- **Venue**: CIKM 2026 (accepted)

### 2.2 Temporal Sepsis State Modeling for Personalized ICU Discharge (Sequential Clinical Modeling)
- **Authors**: Mariana Costa, Johannes Brandt, Arisa Yamamoto
- **Institution**: University of Copenhagen / Karolinska Institute (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06155
- **Abstract**: ICU discharge timing is a sequential decision problem over irregularly-sampled vitals, labs, and treatment events. The authors build a transformer state model with continuous-time event embeddings and a discharge tradeoff objective that balances readmission risk against LOS cost. On 14,000 ICU episodes (two hospital systems), the model is calibrated to discharge time better than the clinician-benchmark heuristic, reduces simulated readmission by 9.4% at equal LOS, and remains interpretable through attention over the *state* of each vital, as opposed to a single global score. This is a transportable sequential-decision formulation for medical discharge.
- **Key Innovations**: Continuous-time event embeddings for irregular ICU vitals; explicit discharge-tradeoff objective (readmission vs LOS); state-level attention interpretability; dual-hospital external validation.
- **Venue**: Preprint

### 2.3 Choice-augmented Collaborative Filtering for Ranking under Position Budgets
- **Authors**: Fabio Rinaldi, Ingrid Solberg
- **Institution**: Criteo / TU Munich (tentative)
- **Date**: 2026-09-07
- **arXiv**: https://arxiv.org/abs/2609.05902
- **Abstract**: Recommender systems are normally trained to predict per-item propensity, but downstream ranking maximizes a constrained reward (e.g. top-N clicks under a position budget). Choice-augmented collaborative filtering re-frames the task as a *set-choice* problem: it learns a sequence-level joint scoring function over candidate subsets, trained with a structured permutation loss that directly optimizes the constrained objective, and decodes greedily at serve time. On the public Outbrain RTB benchmark and two proprietary ad-placement datasets, set-level scoring beats item-level baselines by 3.1–5.7% in constrained reward while cutting the tendency to saturate positions with a single popular item/creative.
- **Key Innovations**: Direct set-choice scoring (not item-wise + post-hoc re-rank) for position-budgeted ranking; structured permutation loss matching the constrained reward; greedy serve-time decode retained.
- **Venue**: Preprint

---

## 3. CTR Prediction & Advertising

### 3.1 Field-Aware Progressive Crosses for CTR (FieldFormer)
- **Authors**: Zhiyong Liu, Wentao Wu, Qiang Guo, Sijie Chen, Yilin Cao
- **Institution**: Ant Group (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06031
- **Abstract**: High-order feature crosses are expensive and leak-prone; low-order embeddings miss the interaction structure. FieldFormer organizes the feature fields into a learned hierarchy and computes **progressive field-aware crosses**: each interaction stage fuses fields via a cross-attention that is sparse over field pairs (a learned field-pair mask), gradually expanding the receptive field from adjacent to distant fields. On two industrial traffic datasets (1.2B and 3.1B samples) and Criteo, FieldFormer reaches AUC comparable to a large DCNv2 at ~1/6 the training FLOPs, and its learned field-pair masks transfer partially across tasks, enabling a *reusable interaction skeleton* for rapid new-placement adaptation.
- **Key Innovations**: Learned sparse field-pair masks (interaction topology as a parameter); progressive receptive-field expansion over field hierarchy; partial cross-task transfer of interaction topology; industrial-scale validation at reduced FLOPs.
- **Venue**: Preprint

### 3.2 AdCreative-Diffusion: Multimodal Creative Synthesis with CTR-Grounded Reward Model
- **Authors**: Kevin Nguyen, Anastasia Petrova, Ling Zhang
- **Institution**: Meta / University of Amsterdam (tentative)
- **Date**: 2026-09-07
- **arXiv**: https://arxiv.org/abs/2609.05840
- **Abstract**: Generating ad creatives is easy; generating creatives that *perform* is hard, because the reward (CTR/installed rate) is only available post-launch. AdCreative-Diffusion trains a diffusion model over composed text+image creatives and learns a **CTR-grounded reward model** distilled from logged auction results, then uses diffusion-sampling guidance to push generated creatives toward high predicted CTR. On a logged e-commerce ad dataset, generated creatives at equal text-image set receive +18% post-hoc CTR-lift over the distribution mean as judged by the reward model, and a small online A/B (36% of traffic, 2 days) confirms a 4.6% CTR improvement with no measured conversion penalty. The reward model is kept separate so the generator can be swapped for lower-cost variants.
- **Key Innovations**: CTR-grounded reward guidance inside creative diffusion (continuous sampling guidance, not rejection sampling); train/serve decoupling of generator and reward model; reward-model-only online attribution to avoid creative treatment bias.
- **Venue**: Preprint

### 3.3 Causal Source Attribution for Sponsored-Search Lift (CSSA)
- **Authors**: Huan Ma, Elisa Krause, Pablo Fernandez
- **Institution**: Google / EPFL (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06076
- **Abstract**: Sponsored-search attribution is confounded by organic clicks (a user may click the ad because the organic result is strong/weak). Standard last-touch overstates performance on strong-organic brands. CSSA estimators use instrumental-variable (IV) style identification: the *auction clearing mechanism* (bid shading / share-of-impressions shocks) is treated as an instrument for the treatment (ad-impression intensity), and incremental lift is estimated with bias-corrected two-stage models per query-brand pair. On a 6-month simulated-ad campaign suite (with known ground-truth lift) and a large sponsored-log dataset (~1.4B impressions), CSSA reduces mean absolute lift error vs. standard last-touch by 41%, and qualitatively re-ranks ad performance mostly downward for brands with strong organic presence.
- **Key Innovations**: Auction-clearing shocks as a natural instrument for ad-lift attribution; per query-brand IV two-stage estimation; synthetic-with-known-truth validation protocol for attribution estimators.
- **Venue**: Preprint

---

## 4. RL, Agents & Multi-Agent Systems

### 4.1 Partial-Observation Reward Shaping Fails: Exact Coverage via Learned Latent States (LatentCover)
- **Authors**: Matthias Gruber, Aisha Rahman, Olli Virtanen
- **Institution**: TU Munich / Aalto University (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.05948
- **Abstract**: Prior work shows reward shaping is not invariant in partially-observable POMDPs, but the practical fix (learned belief state) is often rejected as unstable. LatentCover learns a latent belief state with a contrastive successor-representation objective and applies it as the shaping signal's *condition*, producing a shaping function that is exactly invariant (the shaped and unshaped optimal policies coincide) under a coverage-complete latent state. On a suite of partially-observable gridworlds and a warehouse-dispatch simulator, LatentCover matches the full-observation oracle while accelerating convergence 3–6× vs. raw shaping, and the learned latent state doubles as an interpretable diagnosis map of the actor's world-model error.
- **Key Innovations**: Coverage-complete latent-state conditioning restores reward-shaping invariance under partial observability; contrastive successor-representation objective for the latent belief; convergence + invariance jointly validated.
- **Venue**: Preprint

### 4.2 Skill Graph Routing for Sparse-Verbose Agentic Tool Selection
- **Authors**: Rui Santos, Yuki Tanaka, Dominik Keller
- **Institution**: University of Edinburgh / Kowinei University (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06128
- **Abstract**: Tool-use agents reason about *which* tool, but tool libraries grow and APIs go stale. The authors build a **skill graph** over tools (nodes=tools, edges=dependency/calls-into), learned from execution logs, and route the agent's next-tool decision through a GNN that produces a *path* rather than a single node. When tools are removed or added, the graph is edited locally, so the agent's planner does not need to be retrained; stale tools are reconnected to neighbors. On a 40-tool library across 3 benchmarks (including ToolBench), the graph router reaches 91.8% task success vs 71.2% for an LLM planner with the same backbone, and degrades gracefully when 20% of tools are randomly removed (+2.9% only) because neighbors absorb the deleted functionality.
- **Key Innovations**: Execution-log learned skill graph as a routable planning substrate; local graph edit (add/remove tool) without planner retraining; graceful degradation under tool-library churn — critical for real agent deployments.
- **Venue**: EMNLP 2026 (submitted)

### 4.3 Equivariance-Constrained Policy Optimization for Symmetric Multi-Agent Coordination
- **Authors**: Zhang Wei, Elena Kovacs, Marco Rossi
- **Institution**: Tsinghua University / Politecnico di Milano (tentative)
- **Date**: 2026-09-07
- **arXiv**: https://arxiv.org/abs/2609.06003
- **Abstract**: Multi-agent policies that ignore the system's underlying symmetries (rotation, permutation of homogeneous agents) overfit low-data regimes and over-explore redundant action configurations. The authors enforce known symmetries by constraining the actor network to be *equivariant* (layers are group-convolutional or permutation-shared) and the return baseline to be *invariant*, with a projection step that keeps the exploiter close to the equivariant manifold. Across cooperative and competitive benchmark suites (MPE, SMAC, a 7-agent StarCraft variant) and a heterogeneous MARL setting, equivariance-constrained training improves sample efficiency 1.9–3.4× at matched final reward and, on symmetric games, prevents the "symmetry-breaking drift" that standard PPO exhibits.
- **Key Innovations**: Principled equivariance constraint for both actor and baseline in MARL (not just architecture sugar); projection keeping the policy near the equivariant manifold; drift prevention on symmetric games with heterogeneous masks.
- **Venue**: Preprint

### 4.4 Ask-Before-Act: Explicit Uncertainty Communication in Human-AI Teamwork
- **Authors**: Chiara Lombardi, Daniel Osei, Jiaxin Liu
- **Institution**: University of Trento / Imperial College London (tentative)
- **Date**: 2026-09-07
- **arXiv**: https://arxiv.org/abs/2609.05961
- **Abstract**: Agents in human-AI teams that silently act on low-confidence predictions trigger coordination breakdowns. Ask-Before-Act evaluates per-step action confidence against a learned human **preference threshold** and, when below it, emits a *terse uncertainty query* ("Can you confirm slot booking?") instead of acting. In a mixed-shared-UI collaborative task (flight-booking / calendar-scheduling simulator) with 48 human participants, Ask-Before-Act raises task success by 17.9% and reduces human-rated annoyance by 31% vs. a silent-default agent, while *increasing* perceived competence — because the queries are few (11% of steps) and calibrated to the human's actual tolerance, which is person-specific.
- **Key Innovations**: Personalized calibration of ask-vs-act threshold from a PGM over the human's tolerance; sparse, terse querying (11% of steps) preserving flow; first behavioral study tying uncertainty-query cadence to perceived competence.
- **Venue**: Preprint

---

## 5. Games & Game Theory

### 5.1 Equilibrium Selection in Turn-Based Stochastic Games with Imperfect Information (Postponed-Information Selection)
- **Authors**: Andrei Vasilescu, Sana Gupta
- **Institution**: EPFL / Oxford (tentative)
- **Date**: 2026-09-07
- **arXiv**: https://arxiv.org/abs/2609.05897
- **Abstract**: Turn-based stochastic games with imperfect information admit equilibria, but the *selection* rule (which equilibrium to play) is arbitrary and often fragile across tie-breaking. The authors define **postponed-information selection**: each player chooses a strategy that is robust to having its information sets *delayed* (its private observations released one extra turn later), formalized as a lexicographic refinement of Nash equilibrium (equiv. to a "delay-tolerance" equilibrium). They prove existence, a polynomial-time algorithm to compute delay-robust equilibria in the discounted case, and show the refinement is tight (in the sense that a small information-delay strictly reduces the equilibrium set). Applications to poker-lite and tactical-combat abstractions illustrate that delay-robust selections avoid the pathological coordination equilibria of plain Nash.
- **Key Innovations**: Delay-tolerance equilibrium refinement (first robustness notion w.r.t. information-release timing); poly-time computation in discounted stochastic games; tightness and equilibrium-set-reduction results; clear illustration on poker-lite and combat abstractions.
- **Venue**: Preprint

### 5.2 When Does Emergent Tool-Use Fail? A Causal Analysis of Game-Theoretic Teammate Coordination
- **Authors**: Ben Richardson, Yuxin Lei, Camille Fontaine
- **Institution**: DeepMind / University of Cambridge (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06019
- **Abstract**: Multi-agent teams often "discover" shared tools that benefit coordination (e.g. a shared map or shared loot mechanic), but these emergent conventions are fragile. The authors run a causal analysis on a suite of team coordination games (including a 3-player maze-loot gridworld and a Hanabi variant) with controlled interventions on agent memory and communication bandwidth. The key finding: emergent tool-use *fails* precisely when the tool's causal chain is not common knowledge — one agent privately maps the tool to a benefit while its teammate's private model of the same tool differs, so the shared tool becomes a *negative* signal. They propose a **common-knowledge diagnostic** (a normalized mutual-information-under-interventions score) that predicts emergent-tool fragility 0.88 AUROC before full training.
- **Key Innovations**: Causal (intervention-based) decomposition of emergent tool-use failure; identifies lack of common knowledge of the tool's causal chain as the primary fragility driver; a cheap pre-training diagnostic that predicts failure without full rollouts.
- **Venue**: Preprint

### 5.3 Punishment-Sensitive Equilibria in Repeated Public Good Games with Endogenous Audience
- **Authors**: Josep Vidal, Akiko Mori
- **Institution**: University of Barcelona / Kyoto University (tentative)
- **Date**: 2026-09-08
- **arXiv**: https://arxiv.org/abs/2609.06169
- **Abstract**: Standard repeated public-good models assume a fixed audience observing contributions; the authors introduce **endogenous audience** — each player chooses whether to *publish* its contribution (visible), with a cost — creating a signaling channel that punishment targets. They characterize the symmetric equilibrium: in the low-cost regime, full visibility is an equilibrium and cooperation is sustainable at lower thresholds than in the fixed-audience case (because publishing acts as a commitment device); in the high-cost regime, contributory equilibria are destroyed and free-riding dominates. The result is robust to noise and to a small fraction of "always-punisher" players, and has implications for governance design of on-chain/public ledgers.
- **Key Innovations**: Endogenous visibility (publish-vs-hide) as a strategic choice in public-good games; threshold characterization of cooperation under publishing costs; robustness to noise and zealot punishers — direct relevance to real-world (ledger/AI-audit) governance.
- **Venue**: Preprint

---

## Summary Statistics

| Category | Papers Count |
|---|---|
| LLMs — Training, Inference & Efficiency | 4 |
| Recommendation & Sequential Modeling | 3 |
| CTR Prediction & Advertising | 3 |
| RL, Agents & Multi-Agent Systems | 4 |
| Games & Game Theory | 3 |
| **Total (this report)** | **17** |
| Overlaps with 09-09 [[arxiv-daily]] (Sep 1–7 mailing) | 0 featured |
| Overlaps with 09-07/09-08 [[arxiv-ai-search]] / [[arxiv-paper-check]] / [[conference-digest]] | 0 featured |
| Screen-out redundancy (already covered / dupe) | 0 |

## Key Trends

1. **The "Tuesday fresh cs.IR" harvest paid off**: 3 genuinely-new rec/ads-domain papers (Intraview view-transformed sequential intent, FieldFormer progressive crosses, CSSA auction-IV attribution) surfaced from the Tue 8 Sep listing — the first real rec/ads material since the 09-07 mining, consistent with the 09-08 forecast.

2. **CTR/advertising is moving from architecture war to *causal structure***: 2609.06076 (CSSA) treats auction-clearing shocks as instruments for lift attribution, 2609.05840 grounds creative generation in logged CTR reward, and 2609.06031 learns interaction topology (field-pair masks) as a transferable skeleton — all three treat the *data-generating process* rather than the feature interaction as the frontier.

3. **Inference efficiency is attacking *serving-stage ceremony***: MoE routing *prediction* (2609.06088) removes the router pass entirely; MinMax-KV (2609.06117) replaces stored KV with regenerable hashed subsets; Koala-Bit (2609.06102) packs embeddings under a decoder-aware budget. Each turns a previously "must-compute / must-store" operation into an optional or regenerable one.

4. **MARL / game-theoretic robustness is being re-based on *information structure***: postponed-information equilibrium selection (2609.05897) re-bases equilibrium refinement on information-release timing; Ask-Before-Act (2609.05961) turns uncertainty communication into a calibrated action; the emergent-tool causal analysis (2609.06019) ties fragility to failure of common knowledge. The common thread: robustness problems are increasingly *epistemic* problems.

5. **Multi-agent symmetry and tool-churn become first-class design targets**: Equivariance-constrained MARL (2609.06003) prevents symmetry-breaking drift; skill-graph routing (2609.06128) survives tool-library churn via local graph edits. Reliability, not peak reward, is the dominant experimental value.

6. **Sequential modeling continues to broaden beyond recommenders**: ICU discharge timing (2609.06155) and view-transformed tail-item sequences (2609.06140) both frame their problem as proper sequential decision/synthesis tasks — the "sequences as first-class" theme this wiki has tracked since the June rec-and-seq digests.