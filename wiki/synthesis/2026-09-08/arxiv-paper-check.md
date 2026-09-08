---
title: arXiv Paper Check — AI & CTR (September 8, 2026)
type: synthesis
created: 2026-09-08
updated: 2026-09-08
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, llm, efficiency, reasoning, agents, moe, distillation, scaling-law, evaluation, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 8, 2026)

> Scanned Mon 7 Sep 2026 arXiv mailing (submission window Thu 4 Sep – Mon 7 Sep). Categories: cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA. Deduped vs same-day 09-07 sibling digests (arxiv-daily, arxiv-ai-search, game-rl-daily, conference-digest). All featured IDs grep-verified 0 hits in wiki/.

## Summary

**10 papers** across 5 themes. **No new CTR-specific papers** in this window — all CTR/recommendation papers from this mailing were already captured by 09-07 arxiv-daily (AlleCompanion, AtomRec, PTDG, LARK, MURAL, Distill-Global-Adapt-Local, AutoLR) and 09-07 arxiv-ai-search (SAM-D2Q, IGPO, Embedding Surgery). This report focuses on **LLM core** papers with high cross-domain relevance to CTR/recommendation infrastructure.

---

## ① LLM Training & Efficiency (4 papers)

### 1. Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference
- **arXiv**: [2609.05275](https://arxiv.org/abs/2609.05275) | **Venue**: ICML 2026
- **Authors**: Mostafa Elhoushi, Alex Pretko, Nolan Dey, Bin Claire Zhang, Gavia Gray, Gurpreet Gosal, Abdulrahman Mahmoud, Shane Bergsma, Joel Hestness (Cerebras)
- **Key contribution**: Layer dropout (stochastic depth) revival for LLMs. With optimal layer distribution/time schedule/optimizer, same-FLOP layer dropout yields lower loss; saves up to 25% training FLOPs; enables 1.5× inference speedup via early exit/layer skipping/self-speculative decoding. **2400+ experiments**, 271M–8.2B params, 160B tokens on Cerebras CS-3.
- **Why it matters**: Resurrects a "dead" technique for modern LLMs; training + inference efficiency in one package. Directly applicable to industrial rec/CTR model serving where FLOP budgets are tight.

### 2. RISE: Recursive Improvement via Self-Extrapolating Policy Distillation
- **arXiv**: [2609.05295](https://arxiv.org/abs/2609.05295)
- **Authors**: Yang Li, Semih Yavuz, Shafiq Joty
- **Key contribution**: Constructs synthetic teacher from model's own RLVR trajectory by extrapolating displacement (parameter or logit space) between current checkpoint and trailing anchor. Converts sparse outcome-induced update into dense token-level target. **Recursive** — teacher refreshes each iteration as student improves. Outperforms RLVR-only and standard self-distillation across math reasoning, STEM, code, and multi-turn agentic tasks.
- **Why it matters**: Eliminates external teacher dependency; recursive loop is a new paradigm beyond one-shot distillation. Relevant to CTR model post-training where teacher models are costly.

### 3. What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection
- **arXiv**: [2609.05198](https://arxiv.org/abs/2609.05198)
- **Authors**: Zhinan Hou, Jiaqi Zhang, Xunliang Cai, Keyou You
- **Key contribution**: 1-shot OPD is consistently effective; improvement driven by **longer CoT paths** (not token entropy). Even "unsolvable" examples that exceed teacher capability are useful. **8 selected hard examples match 17K dataset baseline** across 4 models (1.5B–7B).
- **Why it matters**: Radical data efficiency for post-training; paradigm shift from "more data" to "right data." Relevant to any LLM-enhanced CTR system where post-training data curation matters.

### 4. Amortizing Scaling Law Construction Costs
- **arXiv**: [2609.05016](https://arxiv.org/abs/2609.05016)
- **Authors**: Abhash Kumar Jha et al. (LAION/acad)
- **Key contribution**: Formulates scaling law data collection as Bayesian optimization. Compute-ordered budget expansion + surrogate-fantasy augmentation recovers full-grid fits at **10–100× computational savings**. Metrics for comparing fitting methods under budget constraints.
- **Why it matters**: Scaling laws guide CTR model design (cf. EST, FAT, SUAN in wiki); this reduces the cost of deriving them by 10–100×.

---

## ② Reasoning & Uncertainty (1 paper)

### 5. GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity
- **arXiv**: [2609.05284](https://arxiv.org/abs/2609.05284)
- **Authors**: Shuang Liang, Xin-Yu Hu, Xiang-Jun Ou, Shao-Qun Zhang
- **Key contribution**: Models LLM reasoning branches as DAGs; **GUT-Q** measures uncertainty via graph complexity approximation; **GUT-O** treats negative uncertainty as RL reward. Validated on 4 LLMs × 5 datasets.
- **Why it matters**: Novel uncertainty quantification grounded in graph theory; complements existing logit-entropy / sampling-variance methods. Applicable to any LLM pipeline (including rec/CTR reasoning chains).

---

## ③ Agent Infrastructure (2 papers)

### 6. TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing
- **arXiv**: [2609.05019](https://arxiv.org/abs/2609.05019)
- **Authors**: Tianxing Wang, Mingming Zhao, Shuai Huang, Huiyang Xu, Chaoyue Niu, Shengzhong Liu, Fan Wu (SJTU)
- **Key contribution**: Offline distills workflow-search traces into atomic/composite skills + outcome-conditioned transition graph. Online: treats planned routes as provisional — retains valid continuation, inserts local response, or replaces only invalid suffix. Outperforms dataset-level optimization, query-level selection, and graph-constrained scheduling.
- **Why it matters**: "Selective route editing" as general principle for adaptive agent orchestration; directly relevant to multi-stage CTR pipeline agents (retrieve→rank→rerank).

### 7. Compact-Memory LLM Agents via Online Max-Member Clustering and Atom-Aware Packing
- **arXiv**: [2609.04915](https://arxiv.org/abs/2609.04915)
- **Authors**: Jiahe Geng, Jinpeng Wang, Kun Yuan (PKU)
- **Key contribution**: RSM-full — cosine-gated max-member merge write rule + atom-aware grouped context packer. **83% Full-Context quality @ 32% token cost** at 4K budget on AMA-Bench. Beats Online K-Means by +3.5–6.0pp. Merge rule contributes +5.7pp, packer +5.0pp. On par with BM25-RAG on RealMem.
- **Why it matters**: Compact memory is critical for cost-sensitive LLM-enhanced CTR/rec serving; defines strong Pareto point in 2K–5K token regime.

---

## ④ MoE Efficiency (1 paper)

### 8. ACE: Adaptive Calibration-Free Expert Skipping for MoE-based LLMs
- **arXiv**: [2609.05228](https://arxiv.org/abs/2609.05228)
- **Authors**: Zukang Xu, Zhixiong Zhao, Xing Hu, Jiangyong Yu, Houji Wen, Jun Li, Zhe Jiang, Dawei Yang
- **Key contribution**: Training-free, calibration-free expert skipping. Global Spectral Proxy (GSP) estimates transformation capacity; Router-Conditioned Refinement (RCR) builds expert-specific direction prototypes. Dual-view consistency required to skip; top-1 always retained. At 50% skip ratio on Qwen3.6-35B-A3B: **WikiText-2 PPL −7.96%, downstream +4.15pp**.
- **Why it matters**: MoE is dominant in frontier CTR models (cf. mtmixatt, latent MoE in wiki); this enables 50% compute reduction without retraining.

---

## ⑤ Agentic Safety & Evaluation (2 papers)

### 9. How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method
- **arXiv**: [2609.05274](https://arxiv.org/abs/2609.05274) | **Venue**: EMNLP 2026 Industry Track
- **Authors**: Konstantin Grotov, Valentin Malykh
- **Key contribution**: **Speculative Uncertainty (SU)** — inverts speculative decoding: small draft model scores black-box agent's trajectory in single forward pass (no logits/weights needed). Phase-aware features from reasoning/action spans. Pre-execution veto gate: **−6–8pp execution error, −14–19% token cost** on Qwen3-Coder-480B and Claude 3.5 Sonnet. Transfers OOD without retraining.
- **Why it matters**: Practical failure detection for production agentic systems; applicable to any black-box LLM deployment (rec pipeline agents, CTR model serving agents).

### 10. Phase Transition Frequency as a Training Time Predictor of Test Accuracy in ResNets
- **arXiv**: [2609.05194](https://arxiv.org/abs/2609.05194)
- **Authors**: Arunan J
- **Key contribution**: Phase transition frequency in training dynamics predicts final test accuracy in ResNets. Lightweight metric observable early in training.
- **Why it matters**: Early stopping / model selection signal for CTR backbone networks (ResNet-based feature extractors remain common in DLRMs).

---

## Cross-Cutting Themes

1. **"Data efficiency" becomes the dominant post-training narrative**: 8 examples matching 17K (OPD), recursive self-teaching (RISE), 10–100× cheaper scaling laws — all point to doing more with less.
2. **MoE inference cost reduction without retraining**: ACE's 50% expert skipping at quality gain is the most practically deployable efficiency result.
3. **Agent orchestration matures from "replan everything" to "edit what's broken"**: TROVE's selective suffix replacement is a cleaner architectural pattern than full replanning.
4. **Compact memory defines a serving Pareto point**: RSM-full's 83% quality @ 32% tokens at 4K budget is directly relevant to cost-capped CTR/rec LLM augmentation.
5. **Black-box failure detection without model access**: SU's inverted speculative decoding is the most model-agnostic safety signal to date.

## Method Notes

- Scan source: arXiv list pages (cs.AI/recent, cs.LG/recent) for Mon 7 Sep 2026 mailing; abstracts via /abs/ pages.
- CTR/recommendation gap: zero new CTR papers in this window (all captured by 09-07 sibling digests).
- All featured IDs grep-verified 0 hits in wiki/ prior to this report.
- Affiliations marked where known from paper metadata; otherwise omitted.
