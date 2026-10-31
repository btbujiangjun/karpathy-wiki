---
title: "arXiv Paper Check — AI & CTR (October 31, 2026)"
type: synthesis
created: 2026-10-31
updated: 2026-10-31
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, ranking, retrieval, llm, agents, rl, distillation, efficiency, moe, safety]
---

# arXiv Paper Check — AI & CTR (October 31, 2026)

*Report generated: 2026-10-31 | Window: 2026-10-30 arXiv announcement batch (latest RSS at query time)*

## Summary

- Swept the `cs.IR`, `cs.AI`, `cs.LG`, and `cs.CL` RSS feeds: **753 unique `new`/`cross` papers**, including **40 `cs.IR` items**. `replace`/`replace-cross` entries were excluded.
- The CTR cluster is dominated by **serving-aware scaling and supervision**: long-sequence generative ranking that cuts decode cost (PFA, LWR), unified multi-business ranking (UGR), industrial generative-retrieval value alignment (GR4AD-X), and LLM listwise ranking with compressed inputs (GistRank).
- The AI cluster has an unusually strong **theory-and-efficiency** flavor: a proof/recipe for the Platonic Representation Hypothesis, a pass@1-vs-pass@k theorem for RLVR, token-level fixes to multi-token prediction, and compute-matched evidence against synthetic pre-pretraining.
- Industrial deployment evidence appears in Kuaishou ads (GR4AD-X, +3.07% revenue), Taobao recommendation (UGR, +2.10% GMV), an e-commerce ads A/B (PFA), a large ad platform (CASH, +15.35% revenue/account), and production CTR ranking (Beyond IPS).
- Abstract-only screening. All featured IDs were checked against the wiki; none were previously covered. Numbers are author-reported and not independently reproduced.

## CTR / Ranking / Ads

### 1) [Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for Large-Scale Advertising](https://arxiv.org/abs/2610.38378)
- **Authors:** Yatong Xiao, Yibo Sheng, Lixiang Wang, Mingjie Sun, Yunhao Sha, Pengfei Zhang, Shengyu Wang, Peng Wang, Wenjin Wu, Peng Jiang
- **Categories:** cs.IR, cs.LG
- **Announced:** 2026-10-30
- **Summary:** GR4AD-X is the successor to Kuaishou's deployed generative advertising recommender. It attacks three production limits of GR4AD: deterministic SID assignment is brittle at semantic boundaries, backbone scaling yields diminishing revenue under latency constraints, and sequence-level value optimization gives weak credit to intermediate SID tokens.
- **Key Contributions:**
  - **Multi-Path SID assignment** to make semantic identifiers more robust to boundary errors.
  - **Multi-dimensional capacity scaling** instead of only wider/deeper backbones, improving the effectiveness-efficiency trade-off.
  - **UniVGD** unifies value-guided beam pruning and discriminative reranking with prefix-level reward optimization.
  - Online A/B on Kuaishou ads: **+3.07% cumulative revenue** over the deployed GR4AD baseline at strict latency/throughput constraints.

### 2) [PFA: Attention Can Be Progressively Focused in Long-Sequence Generative Recommendation](https://arxiv.org/abs/2610.39273)
- **Authors:** Pengjie Zhou, Weiqin Yang, Haibo Xing, Hao Deng, Jinxin Hu
- **Categories:** cs.IR
- **Announced:** 2026-10-30
- **Summary:** Full attention over long behavior histories is expensive during autoregressive beam-search decoding. The authors observe **progressive attention focusing** (attention concentrates on a small token subset) and **cross-step ranking consistency** (importance order stays stable across decoding steps), then exploit both for sparse decoding.
- **Key Contributions:**
  - Full attention only at the first decoding step; later steps reuse a shared ranking built by cross-beam weighted aggregation.
  - Reorders selected KV-cache entries into contiguous memory and geometrically shrinks the token budget.
  - Avoids the semantic loss of static compression and the selection overhead of per-step top-k.
  - Two public benchmarks plus a large industrial dataset; 7-day online A/B on an e-commerce ads platform.

### 3) [UGR: Unified Generative Ranking for Heterogeneous E-commerce Recommendation](https://arxiv.org/abs/2610.39426)
- **Authors:** Zonghe Shao, Huabin Chen, Sitong Lu, Fangmei Zhu, Yingcai Ma, Ge Fan, Jinguo Gao, Wei Shi, Yanfang Liu, Huiping Chu
- **Categories:** cs.IR
- **Announced:** 2026-10-30
- **Summary:** List-wise e-commerce ranking must jointly optimize user utility and commercial value across organic, ads, and other business candidates, while respecting GSP auctions. UGR generates multi-business ranking lists autoregressively over the full request-level candidate set, around a thousand candidates in production.
- **Key Contributions:**
  - Replaces pure exposure-sequence imitation with **weighted SFT on post-exposure feedback** plus **permutation preference optimization**.
  - Training-time advertising debiasing tower models historical ad exposure; current ad value is injected at serving.
  - Multi-value sequence retrieval produces candidate lists, with the existing downstream evaluator selecting exposure.
  - Online A/B on Taobao "Guess You Like": **+1.76% Core IPV, +3.29% transaction volume, +2.10% GMV**.

### 4) [Read More, Reason Deeper: Latent Workspaces for Long-Sequence Recommendation](https://arxiv.org/abs/2610.39188)
- **Authors:** Renzhi Wu, Li Sheng, Zikun Cui, Junjie Yang, Tai Guo, Keke Zhai, Yan Li, Jerry Fu, Nipun Mathur, Sri Reddy, Hong Li
- **Categories:** cs.IR
- **Announced:** 2026-10-30
- **Summary:** Long-sequence recommendation has two axes — **evidence scaling** (longer histories) and **reasoning scaling** (more layers over that evidence) — which existing models couple. The Latent Workspace Ranker (LWR) keeps typed evidence in persistent banks and propagates only a fixed-size candidate-local workspace, so layers can re-read the banks from an evolving state.
- **Key Contributions:**
  - History length and reasoning depth become independently controllable.
  - Compared against four architecture families on evidence scaling, reasoning scaling, and a joint compute-efficient frontier.
  - At 10K history: **+0.19% NE over HSTU with 69.6% fewer forward GFLOP/request**.
  - Outperforms baselines on two billion-scale ranking surfaces.

### 5) [PRISM: Personalized Item Representations in User History](https://arxiv.org/abs/2610.39175)
- **Authors:** Renzhi Wu, Zikun Cui, Junjie Yang, Li Sheng, Yongjun Xie, Jerry Fu, Nipun Mathur, Sri Reddy, Hong Li
- **Categories:** cs.AI, cs.IR
- **Announced:** 2026-10-30
- **Summary:** Sequential recommenders usually share one item embedding map across users, so the same item always starts from the same representation. PRISM instead makes the history input itself personalized by reusing upstream ranking computation to produce a per-user, per-item embedding.
- **Key Contributions:**
  - An autoencoder compresses layer states from a user tower, a user-item tower, and same-request candidate mixing into one embedding per scored pair.
  - Offline on a billion-scale recommendation surface: **−0.15% normalized entropy** vs −0.07% for VISTA at similar history lengths.
  - Identifies an **empirical history-length scaling law**: NE gain follows a power law with exponent **0.468** over 26–240 events (0.06% → 0.17%).
  - Frames personalization as a new scaling dimension rather than only a sequence-modeling choice.

### 6) [GistRank: Gist-Compressed Listwise Ranking with Large Language Models](https://arxiv.org/abs/2610.39610)
- **Authors:** Guo Chen, Wenhan Liu, Reed Li, Qianwen Ma, Yu Lu, Haibo Shi, Bingbing Xu, Junjie Huang
- **Categories:** cs.IR
- **Announced:** 2026-10-30
- **Summary:** LLM listwise ranking becomes expensive because every candidate is serialized verbatim. GistRank studies soft compression and finds that vanilla gist tokens fail for ranking: causal encoding weakens passage absorption, and the gist is never trained to expose relative preference.
- **Key Contributions:**
  - Three-stage training: faithful gist tokens under semi-bidirectional attention, pairwise discriminative training, then listwise adaptation.
  - Collapses each passage to **K=4 gist tokens**.
  - **14× speedup** over one-shot full-text ranking while reaching **59.17 average nDCG@10** on TREC DL19/20 and five BEIR subsets, within 0.89 of the strongest full-context baseline.
  - Practical compression for search-era context budgets.

### 7) [CASH: A Capability-Aware Subsidy Harness for Advertiser Subsidy Allocation](https://arxiv.org/abs/2610.39244)
- **Authors:** Minmao Wang, Huihuang Lin, Likang Wu, Hongke Zhao, Shijie Yi, Fei Pan
- **Categories:** cs.IR
- **Announced:** 2026-10-30
- **Summary:** Advertiser Subsidy Allocation (ASA) picks a subsidy level per account to maximize discounted revenue under a platform-wide subsidy-rate constraint. Tier-level business rules do not resolve account-level response or budget granularity. CASH pairs an LLM with a numerical response model and learns where each source is locally reliable.
- **Key Contributions:**
  - **Capability licenses** govern source selection, agent review, and budget allocation.
  - **Expected Policy Coverage Gain (EPCG)** directs limited feedback budget toward high-value reliable coverage.
  - One-month online experiment on 60% of a large ad platform's traffic: **+15.35% revenue per account, +19.86% ADVV** at essentially unchanged subsidy rate, plus gains in revenue quality, LTV, and retention.
  - A useful template for LLM-plus-numerical-model allocation under a shared budget.

### 8) [Beyond IPS: Reliable Counterfactual Evaluation in Multi-Stage Ad Systems without Logged Propensities](https://arxiv.org/abs/2610.40112)
- **Authors:** Mohsen Malmir, Mohamed A. Radwan, Houssam Nassif, Murat Ali Bayir
- **Categories:** cs.IR
- **Announced:** 2026-10-30
- **Summary:** IPS needs action propensities that multi-stage ad systems often do not log. Direct Method (DM) avoids propensities but is biased when candidate policies shift the impression distribution. The paper formalizes DM-based counterfactual replay and reweights logged data toward a mixture of candidate policies.
- **Key Contributions:**
  - **Mixture-weighted reward modeling** using density ratios from a multiclass domain classifier.
  - Bounds value-estimation error by overlap, cold-start, and replay terms.
  - Asymptotic rule uses cold-start mass to decide between offline selection and online A/B routing.
  - Ads simulator plus production CTR-ranking traffic: best Top-1 policy-selection accuracy, especially with a doubly robust correction and at low/medium overlap.

### 9) [KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents](https://arxiv.org/abs/2610.39884)
- **Authors:** Xinhua Miao, Yuanzhen Rong, Weiru Zhang, Xiaoyi Zeng
- **Categories:** cs.AI
- **Announced:** 2026-10-30
- **Summary:** Industrial advertising agents must update decision knowledge as products, traffic, and policies change. KARMA evolves six typed knowledge modules while keeping model weights and harness code frozen.
- **Key Contributions:**
  - A deterministic **Trace Verifier** maps observed errors to candidate modules; a **Critic** compares successful and failed trajectories.
  - A tool-constrained Evolver applies **atomic knowledge edits**, retained only if a fixed validation gate clears a measured gain threshold.
  - Evaluated on roughly 500K real operation logs across six e-commerce domains: hold-out score **30.19 → 39.15 (+8.96 points, +29.7%)** across 18 domain-model settings.
  - Evolved knowledge transfers across domains with an average **+8.54 points** without further adaptation; retained patches are inspectable and reversible.

## AI / Training / Agents

### 10) [Multi-Token Prediction Done Right](https://arxiv.org/abs/2610.38331)
- **Authors:** Jayden Teoh
- **Categories:** cs.LG
- **Announced:** 2026-10-30
- **Summary:** Standard multi-token prediction (MTP) gradients contain a useful KL self-distillation signal plus a low-SNR residual that interferes with both next-token and multi-token learning. The author shows the MTP cross-entropy gradient decomposes exactly into these two parts and proposes a way to keep only the KL signal.
- **Key Contributions:**
  - **KL gradient-recovery trick**: when two distributions share a linear output head, combine their cross-entropy gradients via straight-through routing to recover the KL gradient exactly, without vocabulary-sized logit matrices.
  - **Soft-MTP** is a one-line change, adds no parameters, works with DeepSeek- and Meta-style MTP, and is compatible with fused cross-entropy kernels.
  - From 167M to 1.2B parameters: lower NTP perplexity, faster speculative decoding, and higher zero-shot accuracy at every scale.
  - Stronger math/code reasoning after fine-tuning at 1.2B; matches or exceeds direct KL minimization on most metrics.

### 11) [There Is No Free Lunch in RLVR: Every pass@1 Gain Has a pass@k Price](https://arxiv.org/abs/2610.39295)
- **Authors:** Yinuo Liu
- **Categories:** cs.AI, cs.LG
- **Announced:** 2026-10-30
- **Summary:** RLVR raises pass@1 while the base model can overtake it at large sampling budgets. The paper proves this reversal is not a temporary artifact or a bug: it is a structural price of moving probability mass toward specialized strategies shared across prompts.
- **Key Contributions:**
  - Models RLVR as an exponential tilt of a base policy; under exclusive specialization, every pass@1-improving update strictly lowers some prompt's success.
  - A strictly positive per-prompt price (Stiemke duality) is the exact condition for the trade-off.
  - Bounds the number of pass@k crossings by the sign variation of per-prompt success shifts, recovering the single-crossover result as a special case.
  - Removing the crossover entirely costs the full pass@1 gain; the same tilt identity yields entropy collapse and an entropy-performance law.
  - Practical diagnostic reads the bound, order-preserving test, and price from an evaluation log.

### 12) [Does Chain-of-Thought Reliance Follow a Scaling Law? Larger Models Follow Their Steps More, Independent of Post-Training](https://arxiv.org/abs/2610.38433)
- **Authors:** Esther Xin
- **Categories:** cs.CL, cs.LG
- **Announced:** 2026-10-30
- **Summary:** CoT monitoring is useful only if the final answer actually depends on the written steps. Using a synthetic box-swap task with exact intermediate states, the paper edits one step in a model's own chain and checks whether the answer follows.
- **Key Contributions:**
  - 25 open-weight models (Qwen3, Gemma 3, Llama 3, OLMo 2), 7,200 items each.
  - Answer reliance rises from **16–18% at 0.6B to 97–100% at 14B** in Qwen3; a logistic in log-parameter-count fits with **R² = 0.89**.
  - Capability is the main driver: reliance and step accuracy correlate at **r = 0.99**; equally capable models are equally reliant across families.
  - Post-training barely changes reliance; no model up to 14B solves the task internally without written steps.
  - Supports CoT monitoring in the step-by-step computation regime, with scale as a load-bearing factor.

### 13) [Proving and Improving the Platonic Representation Hypothesis with JEPAs](https://arxiv.org/abs/2610.39302)
- **Authors:** Randall Balestriero, Yann LeCun
- **Categories:** cs.AI
- **Announced:** 2026-10-30
- **Summary:** Turns the Platonic Representation Hypothesis from a conjecture into a theorem and a design recipe. JEPAs trained separately on different modalities learn the same representation up to one rotation when positive pairs are "good views" of one scene; misalignment is bounded otherwise.
- **Key Contributions:**
  - Proves a **Platonic Representation Theorem** for JEPAs across any number of modalities.
  - Shows next-token prediction is a JEPA with "bad views" (parts of one document), explaining why language models align with vision only through scale.
  - Validates from 145K captions to texts of 940M web images and derives an alignment scaling law that predicts unseen runs within seed noise.
  - Good views need **42× fewer samples** than next-token prediction to reach the same alignment; a **109M-parameter text JEPA** aligns with DINOv2/CLIP better than LMs up to 72B and CLIP's text encoder.
  - One rotation turns separately trained encoders into an image captioner (CIDEr 0.838 on COCO); pair-free ImageNet-100 top-5 **64%** vs at most 56% for LMs up to 8B.

### 14) [Rethinking Pre-pretraining](https://arxiv.org/abs/2610.40051)
- **Authors:** Alexander Stern, Tim Rocktäschel, Acyr Locatelli, Laura Ruis
- **Categories:** cs.AI, cs.CL
- **Announced:** 2026-10-30
- **Summary:** A compute-matched challenge to synthetic "pre-pretraining" (PPT). Across four curricula (k-Dyck, neural cellular automata, declarative reference corpora, code) and three regimes, synthetic PPT never beats pure natural-language training.
- **Key Contributions:**
  - Data-constrained, data-unconstrained, and high token-to-parameter setups (881M parameters, 50B tokens).
  - With scarce natural language, repeated epochs over a 100M-token corpus beat every synthetic curriculum on NL validation loss.
  - Reproduces a prior **5.4% perplexity gain** from PPT under the original initialization, but an improved initialization helps the no-PPT baseline more, closing the gap.
  - Models forget PPT content during later NL training; interleaving prevents forgetting but does not significantly improve NL performance.
  - Argues synthetic pre-pretraining is not a distinct, generally useful training stage.

### 15) [How to Loop Your Transformer: Loop Scaling, Specialization, and Parallel Inference](https://arxiv.org/abs/2610.40325)
- **Authors:** Chanakya Ekbote, Artidoro Pagnoni, Devendra Singh Sachan, Shruti Bhosale, Mike Lewis, Maryam Fazel-Zarandi, Shashank Rajput, Sujan Kumar Gonugondla
- **Categories:** cs.AI, cs.LG
- **Announced:** 2026-10-30
- **Summary:** A systematic study of weight-reusing looped Transformers up to 1B parameters, 155B tokens, 1.07e21 FLOPs, and 32 loops. Whether looping helps depends on whether model size, training compute, or inference efficiency is the binding constraint.
- **Key Contributions:**
  - Looping the **full transformer** is best at fixed parameter budget; looping a **middle block** is better when training FLOPs are constrained.
  - More loops are not uniformly better: gains saturate, reverse, or destabilize.
  - Small **loop-specific LoRA adapters** improve quality, with larger gains as loops increase.
  - **Parallel Loop Transformers** recover quality when the current-token embedding is preserved and separately normalized before combining with the previous-token hidden state.
  - Practical design guidance keyed to resource constraint and inference setting.

### 16) [Dual DeltaNet: Value-Side Memory Reorganization for Linear Attention](https://arxiv.org/abs/2610.38578)
- **Authors:** Yixiao Qian, Yaxin Zhang, Song Chen, Jiaxu Liu, Shengze Cai, Chao Xu
- **Categories:** cs.LG
- **Announced:** 2026-10-30
- **Summary:** Views the linear-attention state as a bank of `d_k` addresses storing `d_v`-dimensional values. The standard delta rule only corrects values on the key side; DDN adds a complementary value-side rule that reorganizes which addresses store related value features.
- **Key Contributions:**
  - Extends Kimi Delta Attention (KDA) with a **two-sided delta rule**.
  - Derives a chunkwise parallel training algorithm and a rank-2 recurrence for higher inference arithmetic intensity.
  - Beats KDA, GDN-2, and Mamba-3 on language modeling, zero-shot downstream tasks, and retrieval.
  - Modest training/inference overhead relative to KDA.

### 17) [Adversarial Self-Distillation](https://arxiv.org/abs/2610.38732)
- **Authors:** Mohammad Sadegh Akhondzadeh, Soroush H. Zargarbashi, Aleksandar Bojchevski
- **Categories:** cs.LG
- **Announced:** 2026-10-30
- **Summary:** Supervised refusal finetuning does not teach autoregressive models to refuse under attack: an adversarially trained model can still comply when the attacker injects a compliant prefill. Adversarial Self-Distillation (ASD) extends the model's own clean-prompt safe behavior to the prefixes visited under attack.
- **Key Contributions:**
  - Teacher = the same model on the clean prompt, optionally with an extra safety instruction; student = the model under attack.
  - Distills at **on-policy sampled prefixes**, including compliant openings, so the model learns to recover refusal mid-generation.
  - Lower attack success than state-of-the-art defenses with little multiple-choice accuracy loss.
  - Notable because it turns self-distillation into a safety mechanism rather than only a capability transfer tool.

### 18) [Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection](https://arxiv.org/abs/2610.39122)
- **Authors:** Xinyan Wang, Xiaogeng Liu, Jun Shao, Chaowei Xiao
- **Categories:** cs.AI
- **Announced:** 2026-10-30
- **Summary:** Personal agents learn from user feedback, but feedback can teach them to obey instructions embedded in external content. A two-phase methodology separates legitimate adaptation from a later unauthorized injected task.
- **Key Contributions:**
  - Adaptation phase: user asks the agent to read external content and complete its task; agent learns from feedback as designed.
  - Test phase: a third party hides a similar task in new content without user authorization.
  - Self-evolution substantially degrades indirect-prompt-injection robustness: **+14.0–48.8 pp** average attack success under skill evolution and **+3.0–39.3 pp** under RL.
  - Code released; a direct warning that "learning from appreciation" can learn the wrong authority boundary.

### 19) [Emergence of the transformer architecture as the score of entropic laws of random measures](https://arxiv.org/abs/2610.39614)
- **Authors:** Giacomo Greco
- **Categories:** cs.AI
- **Announced:** 2026-10-30
- **Summary:** A first-principles derivation of Transformer attention from a maximum-entropy model of language, where sentences are empirical measures of tokens and the prior says sentences carry no structure. Reproducing a sentence-level interaction statistic yields a softmax choice rule with attention as its mean parameter.
- **Key Contributions:**
  - Query-key matrix appears as the Lagrange multiplier of a within-sentence maximum-entropy problem; the value matrix as the multiplier of a language-level constraint, so the two are **untied**.
  - Under the optimal entropic law, a Transformer head appears in the score of the last-token law.
  - For ordered sentences, causal masking follows from a masked reference choice rule; with a next-token cross-moment the score equals one causally masked attention head.
  - Discusses multi-head attention, weight-tied unembedding, and residual blocks as projected Langevin steps (heuristic).

## Also Notable

- **[CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening](https://arxiv.org/abs/2610.38822)** — training-free decoding for looped Transformers; context-copy proposals filtered at shallow recurrent depth, **2.98×–10.70×** speedup on base models and 2.74×–3.52× on thinking models.
- **[Compute Has Shape: Self-Morphing the Internal Computation of Frozen LLMs](https://arxiv.org/abs/2610.38382)** — input-dependent choice among base/repeat/branch computation topologies; **+8.06%** mean relative gain in-distribution, +4.45% unseen, best in 24/27 settings.
- **[Softmax Routing Dynamics in Mixture-of-Experts Models: Collapse and Recovery](https://arxiv.org/abs/2610.39442)** — theory of router collapse and recovery times; exact log-odds identity links neural updates to threshold crossing.
- **[Why Speculative Decoding Works Better Than Predicted on Sparse MoE Models](https://arxiv.org/abs/2610.38981)** — 10 MoE models, 30B–1T; fine-grained models break the concave speedup-batch curve; an IPF model predicts unique expert counts within **4% error**.
- **[The Quine Test: How Much of a Model's Self Survives Its Own Description?](https://arxiv.org/abs/2610.38726)** — native self-descriptions give **no average preference-reconstruction gain**; explicitly listing answers transfers at 0.955–0.960 fidelity, within 0.03 of same-model repeatability.
- **[Long-Term Agent Memory through Complementary Curation and Consolidation](https://arxiv.org/abs/2610.39790)** — hybrid episodic + relational memory; **90.2%** on LoCoMo and **85.5%** on LongMemEval-S.
- **[The Real Cost of Context: Predicting Compute Time and Energy Consumption in LLM Prefill and Decode Phases](https://arxiv.org/abs/2610.39621)** — decode scales linearly with output, prefill has **linear + quadratic** scaling with input, making long contexts a first-order energy cost in agentic workflows.
- **[Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation](https://arxiv.org/abs/2610.40574)** — token-level teacher selection in OPSD; up to **+5.9** over the base model on Qwen3 math reasoning.
- **[Glance: The Generator Is Its Own Reranker](https://arxiv.org/abs/2610.40454)** — one resident 9B backbone for generation and reranking; nDCG@10 0.741 on SciFact / 0.345 on NFCorpus, +0.045 answer F1 on HotpotQA.
- **[R2QRec: Learning Recommendation Queries from Retrieval Feedback](https://arxiv.org/abs/2610.39984)** — learns query generators from retrieval verification and log-rank feedback; retriever and index stay fixed, no query annotations.
- **[RoFiGR: Coarse Routing, Fine Refinement via Level-Adaptive Distillation in Multimodal Generative Recommendation](https://arxiv.org/abs/2610.39470)** — two-tree recommender with collaborative SID construction + level-adaptive teacher supervision; improves all five ranking metrics on three datasets.
- **[Statistical Detection of Positional Bias in LLM-Based Recommender Systems](https://arxiv.org/abs/2610.37962)** — 40,000 controlled RAG instances; every evaluated LLM recommender rejects positional independence, with formal tests and three bias metrics.

## Emerging Trends

- **Recommendation is optimizing the serving frontier.** PFA, LWR, GistRank, and GR4AD-X all trade representational or architectural complexity for lower decode/FLOP/context cost while reporting online or billion-scale evidence.
- **Generative recommendation is graduating from retrieval to credit assignment.** GR4AD-X's prefix-level value alignment and UGR's permutation preference optimization both target intermediate decisions and commercial value, not just next-SID likelihood.
- **Ads infrastructure is maturing on two under-modeled sides.** CASH handles account-level subsidy allocation; Beyond IPS handles counterfactual policy evaluation without propensities. Both are deployment-facing rather than model-centric.
- **Post-training is becoming token-granular.** Soft-MTP fixes the MTP gradient per token, and MTA-OPSD selects a teacher per token. The unit of supervision is shrinking.
- **The scaling story is splitting.** Scale makes CoT more load-bearing (CoT reliance law), yet good views and data structure dominate raw scale for representation alignment (PRH/JEPA) and synthetic pre-pretraining does not beat natural language at matched compute.
- **Efficiency work is turning theoretical.** Looped Transformers, linear attention, and MoE routing now come with scaling laws or collapse/recovery analyses, not just benchmark wins.
- **Safety has a self-improvement failure mode.** Both Adversarial Self-Distillation (defense) and self-evolution IPI degradation (attack surface) show that learning from the model's own behavior is powerful and double-edged.

## Notes

- Data source: arXiv RSS for `cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`; all items in this batch carried `pubDate` Fri, 30 Oct 2026.
- Counts: **753 unique `new`/`cross`** items; **40** touch `cs.IR`, of which 16 are `new`-only. `replace`/`replace-cross` items were not treated as new.
- arXiv has no dedicated CTR category; CTR/ads work appears mainly under `cs.IR` with cross-lists to `cs.LG`/`cs.AI`.
- Abstract-only screening. Numbers are author-reported and were not independently reproduced.
- No overlap with the 2026-10-29 or 2026-10-30 sibling reports; all featured IDs were checked as absent from the wiki before writing.
- "Announced" is the RSS announcement date, not necessarily the original submission date.
