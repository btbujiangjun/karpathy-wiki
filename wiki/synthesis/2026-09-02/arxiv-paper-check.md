---
title: "arXiv Paper Check — AI & CTR (September 2, 2026)"
type: synthesis
created: 2026-09-02
updated: 2026-09-02
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, llm, agents, tool-calling, agentic-rl, critic, pretraining, data-augmentation, efficient-attention, long-context, retrieval, rag, causal-inference, reranking, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 2, 2026)

Complement to the same-day [arxiv-daily](./arxiv-daily.md) (featured 13 + 5 HM). **Fresh-wave check over the late-Aug → Sep 1–2, 2026 submissions** (IDs trailing `2608.30xxx`), focused on AI, LLM agents, CTR/rec/IR, and efficiency-oriented LLM training/serving. **4 verified-new papers + 4 honorable mentions**, each grep-verified absent (0 hits) from `wiki/` and not claimed by the sibling digest.

> **Method & dedup boundary:** Papers compiled via live web search of arXiv abs/html pages. The 09-01 `arxiv-daily` claimed IDs up to `2608.30662`; the 09-02 sibling `arxiv-daily` claims its own set (CoVeMem `2608.26895`, CADET `2602.11410`, Stageboost `2608.27366`, weak-model RLVR `2608.27420`, etc.). All featured/HM IDs below are **grep-verified absent** from `wiki/**` and disjoint from those claimed sets.

---

## ① LLM Agents — Reliable Tool-Calling via Critique-Aware Training (1)

### CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents

| Field | Detail |
|-------|--------|
| **Authors** | Amir Saeidi, Zehua Zhang, Rishitosh Singh, Naman Ahuja, Vivek Gupta, Ali Payani, Gaowen Liu, Jayanth Srinivasa, Chitta Baral |
| **Institution** | Arizona State University + Cisco Research *(stated)* |
| **Submitted** | 2026-09-01 · [2608.30147](https://arxiv.org/html/2608.30147) · cs.LG |
| **Key contribution** | Long-horizon, stateful tool-calling agents fail irreversibly on a single wrong action, and failures can be sparse across runs. Frontier LLMs cannot reliably *explain* why an action is wrong in long, intertwined, policy-governed trajectories; prompt-based critique agents are inference-only and optimization methods lack rich verification rationales for training. **CAST** converts sparse task outcomes into **action-level supervision** for both a critique model and policy optimization: it analyzes trajectories to synthesize structured rationales about action validity under partial observability, trains a critique model, then builds critique-aware training data to optimize the policy. On dynamic tool-calling benchmarks, fine-tuned Qwen3 models **outperform GPT-OSS-120B by >10% pass⁴ on Retail**, plus a further **+9% on Telehealth in an out-of-domain setting**. |
| **Why it matters** | Moves the critique mechanism from the inference loop into the training loop — "baking the why-it-was-wrong into the policy." Complements the wiki's agentic-RL / tool-calling reliability thread (cf. EVOTOOL, Reinforced-Agent-style reviewer designs) with a training-time, dense-signal alternative to prompt-based or inference-time criticism. |

---

## ② LLM Pre-training — Data Augmentation via Reverse-Engineered Reasoning (1)

### REER-PT: Reverse-Engineered Reasoning for Perplexity-Guided Pre-training Data Augmentation

| Field | Detail |
|-------|--------|
| **Authors** | Haoran Que, et al. |
| **Institution** | Not stated |
| **Submitted** | 2026-08-31 · [2608.30627](https://arxiv.org/abs/2608.30627) · cs.CL |
| **Key contribution** | As compute scales, high-quality pre-training data becomes the bottleneck; standard next-token prediction supervises *what follows a context* but leaves the intermediate reasoning implicit. **REER-PT** extends Reverse-Engineered Reasoning to raw pre-training data: it identifies continuations that are hard to predict yet inferable from context, and inserts **concise reasoning annotations** that reconstruct the missing context→continuation link. Annotations are generated/refined offline with **perplexity as the optimization signal**; length and target-leakage constraints filter trivial/unhelpful ones. The sparse transform preserves the source text and stays compatible with standard next-token prediction (no online reasoning rollouts). Two 680M models trained on source vs augmented corpora (same arch/config): the augmented model gains **up to +2.07 pp on knowledge & reasoning benchmarks**; perplexity reductions range 0.42–7.29, and only ~0.05% of annotation 13-grams appear verbatim in the source. |
| **Why it matters** | A scalable, offline answer to "where does reasoning live in pre-training data?" — injecting chain-of-thought style signal without changing the objective or running RL rollouts. Relevant to the wiki's data-centric / synthetic-data / pre-training line. |

---

## ③ Efficient Attention — Token-Level Dynamic Local-Global Allocation (1)

### LoGo: Token-Level Dynamic Local-Global Attention

| Field | Detail |
|-------|--------|
| **Authors** | Yuqi Pan, et al. |
| **Institution** | Not stated |
| **Submitted** | 2026-08-30 · [2608.29539](https://arxiv.org/abs/2608.29539) · cs.CL (also cs.LG) |
| **Key contribution** | Attention is the scaling bottleneck of long-context Transformers, yet standard models give every token an identical budget. Existing local-global hybrids mix restricted/full-context attention but allocate span **statically** across layers or heads. **LoGo** treats attention span as a proxy for budget and makes allocation **token-level dynamic**: each layer has coupled local (all tokens, restricted window) and global branches, with a learned gate activating full-context global attention **only** for tokens needing long-range info. A threshold-based budget controller holds a target global ratio with no auxiliary loss; a progressive masking schedule stabilizes training before sparse routing kicks in; query-sparse Triton kernels turn the reduced global compute into real speedups. LoGo preserves full-attention scaling behavior across model sizes, beats the full-attention Transformer and matched-budget static hybrids, with clear gains on long-range retrieval and interpretable span-allocation patterns. |
| **Why it matters** | Efficiency-first answer to long-context attention (sibling to the wiki's hybrid/linear-attention thread — L2A-style "learning when to attend"): *token-level* learned selection rather than layer/head-level static span. Direct relevance to the KV-cache/context-efficiency line. |

---

## ④ Retrieval — Causal Reranking for RAG (Adversarial/Serving Trade-off) (1)

### From Association to Causation: Improving Retrieval Precision of RAG via Causal Relations and an Attention Mechanism

| Field | Detail |
|-------|--------|
| **Authors** | Jing Liu, Yongxing Qi, Muchen Jiang, Chengnan Hu, Qingqing Peng, Haoming Wang, Yuqing Wang, Yang Yu, Xu Zhang, Ting Wu |
| **Institution** | Hangzhou Innovation Institute, Beihang University *(stated)* |
| **Submitted** | 2026-08-27 (preprint; announced `2608.21702v1`) · [2608.21702](https://arxiv.org/abs/2608.21702) · cs.IR |
| **Key contribution** | Dense-similarity terminal retrieval (optionally reranked) returns documents that *share keywords* with the query without answering it — a failure growing with enterprise KB size. The paper models the terminal retrieval stage with a causal graph grounded in **Reichenbach's common-cause principle**: query/keywords form a latent common cause **A**, the document's residual keywords a latent set **B**; since a retrieved document is a **collider** (`A → d ← B`), retrieval itself opens an associational path between query and **B**, licensing a **training-free, attention-style re-scoring rule**: cosine similarity between the query embedding and the weighted centroid embedding of **B**. Unlike causality-enhanced RAG variants, it models the causal structure of the *retrieval process* (not the KB content), at negligible cost and no extra LLM calls. On a real 471-document enterprise KB it promotes a relevant guideline from **rank 6 → top 3**; on a keyword-stuffing diagnostic it improves mean target rank **2.88 → 1.25** (a trained cross-encoder reranker only reaches 2.63); on three BEIR benchmarks it *underperforms* the similarity baseline — a documented applicability boundary, gated with a corpus-level calibration check (≥95% reliability, 30–4 probes). Fully local Qwen3-4B/BGE-M3 testbed. |
| **Why it matters** | A principled, training-free reranker that specifically guards the **keyword-stuffing regime** of growing proprietary KBs and complements (rather than replaces) neural rerankers. Feeds the wiki's RAG/retrieval-reliability and adversarial-robustness threads, with an honest scope boundary that other rerankers typically omit. |

---

## Honorable mentions (scanned, not featured)

| arXiv ID | Title | Category | One-line takeaway |
|----------|-------|----------|-------------------|
| [2608.12426](https://arxiv.org/abs/2608.12426) | Constraint Saturation Evaluation (CSE): Large Language Models Can Follow Instructions, But Not Many at Once | cs.CL | Procedural benchmark (15 models, 36 constraint types, k=1–12) showing compositional instruction-following collapses beyond 5–6 simultaneous constraints via multiplicative accumulation; structural constraints degrade 2× faster than lexical; inference-time scaffolding gives little relief. |
| [2608.22557](https://arxiv.org/html/2608.22557) | BLADE: Bilevel Low-rank Augmented-Lagrangian Erasure for LLM Unlearning | cs.CL | Constrained bilevel unlearning with clamped-entropy forget loss + asymmetric augmented Lagrangian + LoRA confinement; +6–9% composite on TOFU/MUSE Books/KnowUndo and stable under 4× scaling. |
| [2608.16249](https://arxiv.org/html/2608.16249) | SAUL: Sharpness-Aware Augmented-Lagrangian Unlearning | cs.CL | Unlearning as constrained minimization ("forget enough, but no more than necessary") with adaptive forget-pressure deactivation; drop-in AL controller improves baselines' post-forgetting utility. |

---

## Cross-Cutting Themes (2026-09-02 AI & CTR pass)

1. **Move the expensive/uncertain operation out of the model's head.** LoGo, REER-PT, and CAST all relocate a capability that naive LLMs do poorly (long-range attention, implicit reasoning, action-grounded critique) into an explicit, learned, *training-time* structure — dynamic routing, inserted reasoning annotations, critique-aware supervision. The shared move: externalize the implicit into trainable signals.
2. **Data quality and optimization signal are converging.** REER-PT uses perplexity as the guide for what to annotate; CAST uses sparse task outcomes as the guide for which action to supervise. Both treat "the objective signal is too coarse / the data is too passive" as the problem, and respond by enriching the *signal* rather than the model size.
3. **Causal structure as a cheap correction primitive.** The causal-RAG reranker applies a collider-opening insight as a training-free re-scoring rule; BLADE/SAUL apply augmented-Lagrangian *constraints* to unlearning. Both use explicit structure (causal graph, constraint) to add robustness that plain data-driven scaling misses — with documented scope boundaries rather than universal claims.
4. **Self-report and similarity remain weak anchors.** CAST's motivation (agents can't explain their wrong actions) and the causal-RAG result (cross-encoders fooled by keyword stuffing) both confirm that parametric/surface evidence is unreliable where policy-governed trajectories or growing KBs concentrate risk — reinforcing the wiki's oversight/reliability line.

---

## Methodology

- **Listing source**: arXiv abs/html pages for the late-Aug → Sep 1–2, 2026 wave (IDs trailing `2608.30xxx`), discovered via live web search (direct arXiv API/curl network access was blocked in this session, so the `websearch` tool was used instead).
- **Dedup**: every featured/HM ID grep-verified **absent** from `wiki/**` and cross-checked against the same-day `arxiv-daily` and the 09-01 sibling claimed-ID sets.
- **Window**: papers in the fresh trailing wave whose submission dates fall on/before Sep 2, 2026, excluding everything already claimed by siblings.
- **Coverage disclaimer**: network-blocked session limited enumeration depth; several same-wave topics (self-evolving rec, CTR, game AI) are already covered by the sibling `arxiv-daily` and intentionally not repeated here; this report therefore emphasizes the *new* LLM-agent / pre-training / efficiency / retrieval angles.

*Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities / prior papers and remain tentative.*
