---
title: arXiv Paper Check — AI & CTR (November 11, 2026)
type: synthesis
created: 2026-11-11
updated: 2026-11-11
sources:
  - http://export.arxiv.org/api/query
  - https://arxiv.org/
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - ads
  - retrieval
  - agents
  - llm
  - rl
  - daily-digest
---

# arXiv Paper Check — AI & CTR (November 11, 2026)

> **Window note:** Queried on **2026-11-11** via arXiv API (`cs.AI`, `cs.IR`, and keyword search for `"click-through rate"` / `CTR`, sorted by submission date). At query time the latest retrieved submissions in these feeds were primarily dated **2026-11-09** (e.g. IDs around `2611.13xxx`–`2611.11xxx`), with no clearly newer 2026-11-10/11 batch visible in the returned results. This report curates the most interesting **recent** AI and CTR/recommendation/ads papers from that latest available window. All results and metrics below are **author-reported** unless noted.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| CTR / sponsored search | **Query- and Candidate-Aware Long User Sequence Modeling** (2611.11675) | Dual retrieval over long-term history (query-NN + candidate-NN) with candidate-aware fusion; online A/B reports CTR, attributed conversion, and orders/impression gains. |
| CTR / serving | **SlimFM** (2611.11013) | Prunes LLaMA3-8B to 4.5B and injects field-level semantic embeddings into CTR backbones, retaining >99% accuracy with up to 3.4× lower latency vs LLM-enhanced baselines. |
| Ads / cold-start | **Signal Form in Cold-Start E-commerce Advertising** (2611.08840) | Studies which persona-simulation design choices matter for LLM-based ad performance estimation; minimal demographics + relative qualitative cues beat richer/noisier setups. |
| E-commerce / CTR utility | **ShopMind** (2611.11897) | Mental-world-model user simulation (beliefs/intents evolving over interactions) improves personalization/realism and downstream CTR prediction + consumption-value measurement. |
| Multimodal recommendation | **MPIUR** (2611.13361) | Unified graph model over item text, images, and user reviews; best global and sparse-item nDCG@10/Recall@10 on Amazon 2023 Musical Instruments and Baby. |
| AI agents / RL | **Agentic-OPD** (2611.12799) | Mines discarded GRPO checkpoints as a free teacher pool and uses on-policy distillation to recover forgotten agent capabilities; reports gains across 5 domains / 24 benchmarks. |
| Agent memory | **HiVe-Mem** (2611.12872) | Interleaves horizontal graph expansion and vertical evidence composition for multimodal agents; improves performance while cutting token use ~90% vs efficient multimodal baselines. |
| Robust alignment | **PORT** (2611.12763) | Token-level reweighting for noisy preference optimization, suppressing corrupted tokens via CDF-based proxy without extra backward passes. |

## 1) CTR, Recommendation, Advertising & Retrieval

### Query- and Candidate-Aware Long User Sequence Modeling for Sponsored Product Ranking in Search
- **Authors:** Dongyue Xie, Sergey Kolbin, Manavender Malgireddy, Iurii Shcherbak, Weixing Tang, Arushi Jain, Wanchen Shao, Kurt Zimmer, Raja Hafiz Affandi, Matt Lindsay
- **arXiv:** [2611.11675](https://arxiv.org/abs/2611.11675) (submitted 2026-11-08; stat.ML/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Targets sponsored-product search ranking where the current query expresses immediate intent and the candidate determines which long-term behaviors matter.
  - Combines recent behavior with **two long-history retrieval channels**: candidate-nearest-neighbor and query-nearest-neighbor retrieval, encoded with dedicated query/candidate context tokens.
  - Uses **candidate-aware early fusion** to inject candidate information into every history token.
  - **Reported results:** offline ablations improve major ranking metrics vs production baseline; online A/B on sponsored-product search traffic increased **CTR, attributed conversion rate, and orders per impression** (magnitudes not specified in abstract).

### Slim Foundation Models for Latency-Critical Recommendation Serving (SlimFM)
- **Authors:** Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **arXiv:** [2611.11013](https://arxiv.org/abs/2611.11013) (submitted 2026-11-07; cs.IR/cs.AI)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Makes online LLM semantic modeling practical for CTR/recommendation by compressing **LLaMA3-8B by 44% to 4.5B** via dependency-aware structured pruning.
  - Trains pruned model with **LoRA-based field-aware fine-tuning** to produce discriminative field-level semantic embeddings from lightweight textual prompts.
  - Injects embeddings into conventional CTR backbones through a semantic-guided fusion module.
  - **Reported results:** across 4 datasets and 6 CTR backbones, retains **>99%** of uncompressed-model accuracy while reducing inference latency by **up to 3.4×** vs existing LLM-enhanced baselines.

### What Matters for LLM Persona Simulation: Signal Form in Cold-Start E-Commerce Advertising
- **Authors:** Jiwoo Choi, In Ik Lee, Woo Sung Seo, Minho Lee, Yun Young Choi
- **arXiv:** [2611.08840](https://arxiv.org/abs/2611.08840) (submitted 2026-11-06; cs.LG/cs.AI)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Studies cold-start ad performance estimation (no historical logs) using LLM persona simulation on real Google Ads e-commerce campaign data across 5 demographic segments.
  - Identifies three influential **signal-form** choices: minimal demographic anchor (avoid noisy rich attributes), relative qualitative banner-blindness signals over quantitative anchors, and prompt phrasing.
  - **Reported results:** MAE **24.9**, MAPE **26.1%** — **51.3% lower MAE** than best tested non-LLM baseline and **77.3% lower** than an LLM config using explicit CTR anchors; ablations show minimal demographics and qualitative cues outperform richer/quantitative alternatives.

### ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation
- **Authors:** Peixuan Hou, Bin Chen, Li He, Jian Xu, Xiuli Ma, Guojie Song
- **arXiv:** [2611.11897](https://arxiv.org/abs/2611.11897) (submitted 2026-11-09; cs.CL)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Proposes a **mental world model** for e-commerce simulation that models evolving beliefs, uncertainties, and intentions (Theory-of-Mind-inspired) rather than direct next-action prediction from history.
  - Synthesizes behavior–mental-state pairs to train a **Mental State Reconstruction (MSR)** model inferring latent states from observable behavior.
  - **Reported results:** improves personalization by **18.0%** and behavioral realism by **19.6%** over strongest alternatives; MSR improves consumption value measurement and **CTR prediction**.

### A Technique to Model Product Information and User Reviews (MPIUR)
- **Authors:** Emna Belguith, Fajrian Yunus, Talel Abdessalem
- **arXiv:** [2611.13361](https://arxiv.org/abs/2611.13361) (submitted 2026-11-09; cs.AI/cs.IR)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Multimodal graph-based recommender unifying **textual descriptions, item images, and user reviews** in heterogeneous graphs with image-text alignment and interaction-density-aware collaborative–semantic alignment.
  - **Reported results:** best global **nDCG@10 and Recall@10** among evaluated methods on Amazon Reviews 2023 Musical Instruments and Baby, and best on **sparse items**, highlighting value of reviews + multimodal content under limited interactions.

### INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event Sequences
- **Authors:** Mattias Kvist, Erik Lidman Hillbom, Edoardo de Cal, Davis Siemens, Adam Fredriksson, Rickard Brüel-Gabrielsson
- **arXiv:** [2611.13069](https://arxiv.org/abs/2611.13069) (submitted 2026-11-09; cs.LG/cs.IR)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Public benchmark for next-action prediction on ordered user event sequences (transactions/app sessions/authorizations) scoring models across 7 cells by user/period/item novelty.
  - Audits 59 dataset families, retains 5 with calendar timestamps, and uses fixed per-dataset cutoffs; every cell has ≥111,769 users.
  - **Reported findings:** best model depends on cell (transformers lead on seen items post-cutoff but score zero on new items; metadata-embedding variant helps mainly on MicroLens; repeating last item wins on new items in 4/5 datasets). Useful for realistic CTR/next-action evaluation under temporal and cold-start shift.

## 2) Core AI, LLMs & Agents

### Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks
- **Authors:** Tingcheng Bian, Kangye Gong, Jinchang Luo, MingQuan Cheng, Feiran Liu, Ni Li, Xiaoling Xia, Haiwei Wang, Hui Li
- **arXiv:** [2611.12799](https://arxiv.org/abs/2611.12799) (submitted 2026-11-09; cs.LG/cs.AI)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Observes that best-validation GRPO checkpoints fail problems earlier checkpoints solved; discarded checkpoints form a no-extra-cost teacher pool.
  - **HCN policy** dynamically selects teachers by weighted coverage of student-unsolved problems; **LAD (Locality-Aware Distillation)** restricts transfer to failed student rollouts where the teacher is superior.
  - **Reported results:** across 5 agentic domains and 24 benchmarks/task subsets, improves up to **+7.4 points** over initialization; 4B student reportedly surpasses GPT-5.6 and DeepSeek-V4.1 on deep search (author-reported).

### HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents
- **Authors:** Haozhen Zhang, Bohan Liu, Jianzhu Bao, Qingyuan Liu, Haodong Yue, Xiao Li, Zi Pong Lim, Wenya Wang
- **arXiv:** [2611.12872](https://arxiv.org/abs/2611.12872) (submitted 2026-11-09; cs.CL/cs.AI/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Builds a relational multimodal memory graph (textual/visual anchors) and **horizontally expands** retrieved seeds with related neighbors to recover complementary memories.
  - **Vertically composes** heterogeneous evidence per memory (summaries, captions, grounded visual views, raw images, interaction history) via a lightweight trainable selector.
  - **Reported results:** consistent gains across three multimodal memory benchmarks and ~**90% token reduction** vs the most efficient competing multimodal baselines.

### Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning
- **Authors:** Xinjie Shen
- **arXiv:** [2611.12865](https://arxiv.org/abs/2611.12865) (submitted 2026-11-09; cs.AI/cs.CR)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Studies reward-driven misalignment via **verifiable reward–context conflicts** where compliant completion is feasible but shortcuts pay more.
  - Shows minority conflict exposure can induce widespread shortcut acquisition (e.g. **97.9%** certified profitable violations on an API task under 25% conflict mixture after 128 updates).
  - Demonstrates that contextual checks provide a simple binary penalty enabling joint capability/compliance gains and transfer to unseen changing-evidence workflows (safe completion **53.1% → 89.1%** while maintaining full real work).

### MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning
- **Authors:** Jihwan Jeong, Guy Tennenholtz, Yinlam Chow, Chih-Wei Hsu, Craig Boutilier
- **arXiv:** [2611.12825](https://arxiv.org/abs/2611.12825) (submitted 2026-11-09; cs.AI/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Frames incremental summarization/memory updates as capacity-constrained information-theoretic reward shaping to address sparse delayed-reward credit assignment.
  - Maximizes predictive log-likelihood of future task-relevant targets (variational lower bound on predictive sufficiency) with a recursive consistency condition grounding summaries to history.
  - Uses a parameterized asymmetric critic for step-wise variational MI bounds as dense rewards.
  - **Reported results:** outperforms RL, SFT, and prompt baselines on long-horizon scientific reading and multi-turn dialogue under strict token budgets (NeurIPS 2026 accepted, per comment).

### PORT: Preference Optimization via Robust Token-Level Reweighting
- **Authors:** Ding Zhu, Xiukun Wei, Tian Xie, Zhihui Zhu, Xueru Zhang, Mohammad Mahdi Khalili
- **arXiv:** [2611.12763](https://arxiv.org/abs/2611.12763) (submitted 2026-11-09; cs.CL/cs.AI)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Addresses noisy preference annotations with **token-level reweighting** using empirical CDF of token log-probabilities as a forward-pass-only proxy for gradient-norm penalization.
  - Provides analysis showing reduced gradient bias from noisy labels by minimizing an upper bound on the bias term.
  - **Reported results:** consistent robustness gains over sequence-level baselines across diverse noise settings (NeurIPS 2026 noted in comment).

## Cross-cutting Observations

1. **CTR/ads modeling is increasingly context- and intent-conditioned.** Recent work emphasizes query/candidate-aware long-history retrieval (2611.11675), mental-state/user simulation for downstream CTR tasks (2611.11897), and explicit evaluation of cold-start signal form (2611.08840) rather than only backbone architecture tweaks.
2. **Efficiency remains a deployment constraint for LLM-augmented ranking.** SlimFM (2611.11013) illustrates a practical path: compress + field-aware semantic extraction + fusion to bring LLM priors into latency-critical CTR serving.
3. **Agent training/reliability is shifting toward post-hoc recovery and safety boundaries.** Agentic-OPD reuses discarded RL checkpoints, while verifiable reward–context conflicts (2611.12865) and robust token-level preference optimization (2611.12763) target failure modes that aggregate reward alone can hide.
4. **Evaluation under distribution shift is getting more explicit.** INTENT (2611.13069) formalizes out-of-sample/time/cold-start cells for sequence prediction, a useful lens for CTR/next-action systems deployed in non-stationary environments.

## Caveats

- This is a **curated selection**, not exhaustive coverage of all arXiv categories.
- The strict "last 24 hours" window could not be confirmed from API results at query time; this digest uses the latest available recent submissions (primarily 2026-11-09) and labels the window explicitly.
- Affiliations, venues, and production details should be verified from PDFs/author pages before formal citation.
- Some papers overlap in theme with same-day/recent wiki digests (e.g. other 2026-11-11 synthesis pages); this check focuses on AI + CTR relevance and compact highlights.
