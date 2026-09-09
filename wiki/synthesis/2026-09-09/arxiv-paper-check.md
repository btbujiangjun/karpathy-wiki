---
title: arXiv Paper Check — AI & CTR (September 9, 2026)
type: synthesis
created: 2026-09-09
updated: 2026-09-09
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, llm, efficiency, reasoning, evaluation, moe, embedding, distillation, scaling-law, agentic, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 9, 2026)

> Last-24h scan (Wed 9 Sep 2026) of the freshest arXiv material. This window = **Tue 8 Sep 2026 mailing** (papers submitted Mon 7 – Tue 8 Sep, ID range `2609.058xx–2609.0618x`). **All CTR/recommendation papers in this window were already captured by the 09-09 sibling digests** — [[arxiv-daily]] (Sep 1–7 mailing, incl. UniCon) and [[arxiv-ai-search]] (Tue 8 Sep mailing, incl. FieldFormer / AdCreative-Diffusion / CSSA). This report therefore curates the **most cross-domain-interesting AI papers** and analyzes their direct relevance to this wiki's CTR/recommendation scaling focus, cross-linking to existing [[ctr-scaling-landscape]] pillars. No new arXiv IDs featured here are absent from the sibling digests — this is a thematic curation, not a fresh mining pass.

---

## ① CTR & Advertising — the "last 24h" harvest (captured by siblings)

The decisive CTR takeaway of this window is that **the field's frontier has moved from architecture wars to causal / data-generating structure** — a shift flagged across all four new industrial+academic CTR papers:

| Paper | arXiv | Org | Online/Offline result | Covered in |
|-------|-------|-----|----------------------|------------|
| **UniCon** unified context-centric modeling | [2609.03290](https://arxiv.org/abs/2609.03290) | Meituan | +0.0139 offline AUC; +3.09% RPM / +2.07% CTR / +2.95% revenue | [[arxiv-daily]] |
| **FieldFormer** field-aware progressive crosses | [2609.06031](https://arxiv.org/abs/2609.06031) | Ant Group | DCNv2-class AUC @ ~1/6 training FLOPs | [[arxiv-ai-search]] |
| **AdCreative-Diffusion** CTR-grounded creative gen | [2609.05840](https://arxiv.org/abs/2609.05840) | Meta / UvA | +4.6% CTR A/B, no conversion penalty | [[arxiv-ai-search]] |
| **CSSA** causal sponsored-search attribution | [2609.06076](https://arxiv.org/abs/2609.06076) | Google / EPFL | MAE −41% vs last-touch on 1.4B impressions | [[arxiv-ai-search]] |

**Why the four matter as a group** (synthesis across siblings):
1. **UniCon** attacks the same *unified-modeling* axis tracked by the wiki's EST/OneTrans/MixFormer cluster — but re-frames it as a *context-centric* problem (history + target as homogeneous context units) rather than a token-level unification. A design reminder that the "division" between sequential/non-sequential is an artifact of legacy feature engineering.
2. **FieldFormer** makes interaction *topology* (field-pair masks) a learned, transferable parameter — a distinct lever from compute scaling. The impedance-matching question for the [[papers/ctr/est|EST]]-style scaling-law line: does interaction-topology transfer partially decouple from width/depth scaling?
3. **AdCreative-Diffusion** + **CSSA** both treat the *measurement/attribution layer* as the frontier — reward-model-grounded creative generation and IV-based (auction-shock instrument) lift estimation. Consistent with the wiki's observation (see [[ctr-scaling-landscape]]) that industrial ads has absorbed causal-inference tooling.

---

## ② Most interesting for CTR/recommendation infrastructure (from Sep 8 mailing)

Four papers from the sibling harvest have the strongest **serving-cost / data-efficiency** resonance with this wiki's CTR scaling pillars.

### 2.1 Koala-Bit — kernel-aware low-bit embedding compression [2609.06102]
- **Authors / org**: Miki Takahashi et al. (Preferred Networks / U. Tokyo, tentative)
- **What**: Decouples symmetric input embedding from an asymmetric, per-cluster calibrated output codebook; applies GPU-kernel-aware bit allocation packing clusters into memory-contiguous lanes. At 3-bit average, PPL within 0.3% of bf16 across Llama-3.2/3.3 & Qwen2.5 up to 70B; embedding memory cut **70%**; enables larger RAG document cache in the same envelope.
- **Why it matters here**: CTR/ad models are dominated by *sparse embedding tables* (this wiki's `versioned-late-materialization` and `tokenmixer-large` cover the same memory pressure from the data-infra / hardware-utilization side). Koala-Bit's *decoupled output-codebook calibration* is a portable fix for the "embedding quantization destroys the output logit" failure that has historically blocked low-bit CTR embeddings. (Covered in [[arxiv-ai-search]].)

### 2.2 MoE Scatter-Attention Predictor — predict expert routing, skip the router [2609.06088]
- **Authors / org**: Yuxuan Zheng et al. (Tsinghua / Inria, tentative)
- **What**: A tiny low-rank "scatter predictor" head predicts top-k expert indices directly from layer input, skipping the router's attention/argmax forward-pass. 90–95% top-1 routing agreement with the true router, **router compute −68%**, <1.2% end-task degradation (DeepSeek-V4-Flash, Mixtral-8x22B at 50–70B active). Offline KD-trained, inference-only swap.
- **Why it matters here**: Follows the wiki's [[mtmixatt]] / MoE thread. For CTR serving (which uses MoE in the top network, cf. [[papers/ctr/mtmixatt|MTmixAtt]]), routing is pure overhead per example. Removing the router pass — with *routing-agreement* rather than end-task-only evaluation — is a cleaner cost lever than expert skipping alone. (Covered in [[arxiv-ai-search]].)

### 2.3 MinMax-KV — censored/congruential sparse attention for 1M-token serving [2609.06117]
- **Authors / org**: Adrian Nowak et al. (Oxford / ETH, tentative)
- **What**: Deterministic hash-seeded regenerable KV subspace; any window regenerated from a compact seed instead of stored. Preserves needle-in-haystack at 1M tokens with **12× less KV storage**; memory ceiling independent of context length.
- **Why it matters here**: Directly parallels [[papers/ctr/muse|MUSE]]'s 100K-length lifelong-interest and [[papers/ctr/longer|LONGER]]/[[papers/ctr/sparsectr|SparseCTR]] long-user-sequence lines. The "regenerate-don't-store" idea is the natural companion to SparseCTR's sparse-attention chunking (which the wiki tracks as showing a clean CTR scaling law). (Covered in [[arxiv-ai-search]].)

### 2.4 Choice-augmented Collaborative Filtering — set-choice scoring under position budgets [2609.05902]
- **Authors / org**: Fabio Rinaldi, Ingrid Solberg (Criteo / TU Munich, tentative)
- **What**: Re-frames ranking as *set-choice*: learns a sequence-level joint scoring function over candidate subsets, trained with a structured permutation loss that directly optimizes the constrained objective (top-N under position budget); greedy serve-time decode. +3.1–5.7% constrained reward on Outbrain RTB + two proprietary ad datasets; cuts single-item position saturation.
- **Why it matters here**: The wiki's recommendation/ads pages emphasize that industrial CTR separates *prediction* (per-item propensity) from *ranking under constraints*. This "optimize the constrained objective directly" re-framing is the same spirit as the set-wise training in JD's GenRec and TGR's whole-slate HiGR tracked in [[conference-digest]]. (Covered in [[arxiv-ai-search]].)

---

## ③ Broader AI highlights (recommendation-adjacent value)

- **Intraview** [2609.06140] — view-transformed pseudo-sequences + contrastive intent distillation for *long-tail* recommendation, tail NDCG@20 +8.2–13.1% rel while head slightly improves (CIKM'26). Direct attack on the long-tail embedding-collapse problem that also starves CTR tail-placement models. ([[arxiv-ai-search]])
- **Skill Graph Routing** [2609.06128] — execution-log learned skill graph + GNN path routing; 91.8% vs 71.2% task success; degrades only +2.9% when 20% of tools are removed (local graph edit, no planner retrain). Relevant to the agentic-recommendation / multi-stage CTR pipeline agents thread (retrieve→rank→rerank). ([[arxiv-ai-search]])
- **Temporal Sepsis State Modeling** [2609.06155] — continuous-time event embeddings + discharge-tradeoff objective (readmission vs LOS) for irregularly-sampled ICU data; −9.4% readmission at equal LOS. A working example of "sequences as a first-class decision task" that the wiki has tracked since the June rec-and-seq digests — extends the sequential-modeling lens beyond recommenders. ([[arxiv-ai-search]])
- **Stage-Gated Warmup** [2609.06054] — data-quality-gated re-warmup for continual pretraining LR schedules; +4.5% benchmark mean over matched-FLOP cosine across 5 suites, no extra hyperparameters. Useful for CTR/rec continual-pretraining pipelines that re-train embedding+backbone on shifting inventory. ([[arxiv-ai-search]])

---

## Cross-Cutting Themes (this window)

1. **CTR/ads: from architecture war to causal + data-generating structure.** UniCon (unified context), FieldFormer (learned interaction topology), AdCreative-Diffusion (reward-grounded generation), CSSA (IV attribution) all treat *the process* rather than *the feature interaction* as the frontier — reinforcing the [[ctr-scaling-landscape]] thesis that scaling is as much structural/causal as it is parametric.
2. **Serving ceremony is the new efficiency battleground.** Predict-the-router (2.2), regenerate-don't-store KV (2.3), pack-embeddings-under-a-decoder-aware-budget (2.1): each converts a previously "must-compute / must-store" operation into an optional/regenerable one. This is the same philosophy as this wiki's `ug-sep` (compute-once) and `sort`/`versioned-late-materialization` (defer/cache) entries.
3. **Data efficiency dominates post-training.** Across the window, the "fewer, better examples" and "reuse/recompute rather than store" motifs recur — consistent with the 09-07/09-08 [[arxiv-paper-check|sibling paper-checks]] that flagged 8-examples-match-17K (OPD) and recursive self-teaching (RISE).
4. **Sequential modeling keeps overflowing recommenders** into decision/clinical domains (ICU discharge), validating the wiki's "sequences as first-class" framing beyond e-commerce.

## Method Notes

- Scan source: sibling 09-09 digests ([[arxiv-daily]] = Sep 1–7 mailing; [[arxiv-ai-search]] = Tue 8 Sep mailing) + arXiv /abs/ pages via the 09-09 search session. arXiv list pages' newest accessible date was "7 Sep 2026"; the Tue 8 Sep IDs were surfaced and grep-verified by [[arxiv-ai-search]].
- Dedup: no new IDs featured here beyond the sibling harvest; all 4 CTR + 4 infra + 4 broader highlights carry explicit provenance to their covering digest.
- This report is the **curated "most interesting" AI & CTR synthesis** for the window; for exhaustive per-paper detail see the two sibling digests.
- Affiliations marked as tentative where inferred from the sibling digest metadata; venue/ID links preserved.
