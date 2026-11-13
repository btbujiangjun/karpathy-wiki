---
title: "arXiv Daily Digest — 2026-11-13"
type: synthesis
created: 2026-11-13
updated: 2026-11-13
sources: []
tags: [arxiv, daily-digest, llm, recsys, ctr, advertising, sequential-modeling, next-poi, generative-retrieval]
---

# arXiv Daily Digest — 2026-11-13

> Curated recent arXiv submissions (primarily Nov 7–11, 2026) across AI, LLMs, recommendation, advertising, sequential modeling, CTR/ads retrieval, and related areas. Categories checked: cs.LG, cs.IR, cs.CL, cs.AI.

---

## 1. Large Language Models & Post-Training

### 1.1 AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
- **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- **Affiliation:** —
- **Abstract:** Introduces AutoScaffold, an AI-for-AI framework that converts a student's RLVR training experience into adaptive scaffolds with minimal domain-specific information and no human intervention during training. A frozen teacher periodically diagnoses bottlenecks and designs shared strategies and per-task hints, adjusting support as the student improves; scaffolds are removed at evaluation.
- **Key Innovations:**
  - Teacher-driven adaptive scaffolding from training experience (strategies + targeted hints) without human-in-the-loop during training.
  - Unified framework applied across ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation.
  - Reported gains over RL baselines when evaluated without scaffolds (e.g., +7.2 points ALFWorld success, +4.0 average QA exact match; up to +5.0 points correct-and-faster kernels; strong math efficiency vs. reported QuestA setting).
- **arXiv:** https://arxiv.org/abs/2611.14515

### 1.2 A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets
- **Authors:** Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster
- **Affiliation:** —
- **Abstract:** Re-examines the theoretical foundations of policy optimization for LLM post-training, focusing on algorithms that are "coverage-preserving" relative to the base model's ability to sample optimal responses. Shows REINFORCE-style methods (underlying PPO/GRPO) can suffer coverage collapse, proposes reference resets via Approximate Policy Mirror Descent (APMD), and provides global convergence/coverage-preservation results for stylized post-training algorithm families.
- **Key Innovations:**
  - Formal characterization of coverage collapse in REINFORCE/PPO/GRPO-style optimization, including under KL regularization to the base model.
  - APMD meta-algorithm using repeated KL-reference resets to stabilize optimization while enabling convergence.
  - Coverage-preserving guarantees for softmax linear policies over pretrained features, connecting regularization/clipping/objective choices to sampling and optimization costs.
- **arXiv:** https://arxiv.org/abs/2611.14467

---

## 2. Recommendation, Sequential Modeling & Next-POI

### 2.1 SepLRM: A Foundation Model Paradigm for Recommendation
- **Authors:** Di Chen, Xijun Xiao, Qin Ren, Weijiang Lai, Zhijian Pan, Zhentao Pan, Pengfei Nie, Cheng Yuan, Zixuan Tan, Xuyang Liu, Tao Wang, Yunwen Huang, Hao Fang, Yichao Wang, Hao Zhang, Siyuan Wu, Hao Chen, Han Diao, Mingyu Yang, Yongkang Feng, Beihong Jin, Jinfeng Yang, Deping Xie, Peng Xu, Zheng Chai, Yuchao Zheng
- **Affiliation:** ByteDance (deployment reported in two large-scale industrial scenarios)
- **Abstract:** Proposes SepLRM, a recommendation foundation model paradigm that separates reusable sequence encoding from task-specific modeling. An encoder-decoder RFM exports a final-layer encoder KV cache (independent of downstream candidates) shared across multiple vertical models, preserving fine-grained behavior information while avoiding repeated long-sequence encoding. Includes cache compression, training/serving co-design, and LG-Store for distributed KV storage.
- **Key Innovations:**
  - RFM/VM separation via a native KV-cache interface enabling candidate-conditioned queries with high-fidelity transfer from E2E counterparts.
  - System co-design (compression, workflows, LG-Store) for practical large-scale serving of shared sequence representations.
  - Strong transfer across model iterations, recommendation stages, and business scenarios with ~100% offline transfer rate and positive online A/B gains reported at ByteDance.
- **arXiv:** https://arxiv.org/abs/2611.10356

### 2.2 LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation
- **Authors:** Zehui Wang, Wolfram Höpken, Dietmar Jannach
- **Affiliation:** —
- **Abstract:** Presents LUMIR, a decoupled multimodal representation learning framework for next-POI recommendation. Heterogeneous multimodal tourism data is unified into a shared textual space via LLMs; an interaction-aware fusion mechanism models cross-modal interactions while sequential signals act as structural constraints. Learned representations are evaluated across multiple sequential recommendation backbones.
- **Key Innovations:**
  - Decouples multimodal representation learning from downstream model architecture/objective for reusable representations.
  - LLM-based semantic unification of heterogeneous modalities plus interaction-aware fusion guided by sequential structure.
  - Consistent improvements over multimodal fusion baselines on accuracy and beyond-accuracy metrics in next-POI settings.
- **arXiv:** https://arxiv.org/abs/2611.14004

### 2.3 SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory
- **Authors:** Yuhang Zhan, Silin Zhou, Zhuo Chen, Haoxiang Lei, Yunren Feng, Lisi Chen, Shuo Shang
- **Affiliation:** —
- **Abstract:** Proposes SHARP, an agentic hierarchical framework where category-level reasoning guides specific POI prediction. Combines a dynamic trajectory memory bank, multi-granularity time-aware category transition graphs, semantic IDs learned via RQ-VAE, and a category-guided POI predictor optimized end-to-end.
- **Key Innovations:**
  - Hierarchical agentic reasoning (category → POI) bridging LLM semantic reasoning with specific POI prediction.
  - Dynamic trajectory memory and time-conditioned category transition graphs to capture evolving behavior and temporal regularities.
  - Reported average gains of +5.29 Acc@5 and +4.52 Acc@10 percentage points over strongest baselines on three real-world datasets.
- **arXiv:** https://arxiv.org/abs/2611.14220

### 2.4 INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event Sequences
- **Authors:** Mattias Kvist, Erik Lidman Hillbom, Edoardo de Cal, Davis Siemens, Adam Fredriksson, Rickard Brüel-Gabrielsson
- **Affiliation:** KTH AI Society (code/repo reference)
- **Abstract:** Introduces INTENT, a public benchmark for next-action prediction on user event sequences that evaluates models across seven cells defined by novelty of user, time period, and target item. Audits public datasets, applies a fixed pre-evaluation cutoff rule per dataset, and provides reference results showing which model classes win under different generalization/cold-start regimes.
- **Key Innovations:**
  - Structured evaluation protocol explicitly separating out-of-sample, out-of-time, and cold-start/new-item conditions.
  - Dataset audit and standardized splitting methodology enabling comparable cross-dataset/cell analysis.
  - Empirical findings highlighting regime-dependent winners (e.g., transformers on seen items post-cutoff vs. simple/metadata-aware baselines for new items).
- **arXiv:** https://arxiv.org/abs/2611.13069

### 2.5 Proactive Dimension-Adaptive Denoising for Graph Collaborative Filtering via Representation Coherence
- **Authors:** Wenjun Li, Dong Zhao, Jiaying Shi, Juan Zhang, Zhaoming Pan, Zhimin Zhang
- **Affiliation:** —
- **Abstract:** Proposes Noise-aware Dimension Learning (NDL) for denoising implicit feedback in graph collaborative filtering. Instead of relying only on loss as a passive noise signal, NDL uses Representation Coherence Detection (RCD) in embedding space, fuses it with loss via activity-aware weighting, and applies interaction-level dimension-adaptive masking; a lightweight contrastive regularizer stabilizes embedding geometry.
- **Key Innovations:**
  - Proactive coherence-based noise detection (RCD) complementary to loss-based reliability estimation.
  - Activity-aware fusion and dimension-adaptive masking to limit capacity for unreliable interactions without inference-time overhead.
  - Consistent gains over strong denoising baselines on Amazon-book, Yelp, and MovieLens-1M (e.g., large Recall@5 improvements reported).
- **arXiv:** https://arxiv.org/abs/2611.11801

### 2.6 Not All Branches Are Equal: Adaptive Semantic ID Construction for Generative Recommendation
- **Authors:** Guy Hadad, Haggai Roitman, Bracha Shapira
- **Affiliation:** —
- **Abstract:** Revisits semantic ID construction for generative recommendation and argues IDs should form conditioned hierarchical paths rather than independent tokens across quantization levels. Proposes Adaptive Silhouette Tree (AST), a top-down divisive clustering method that adaptively chooses branching factors by silhouette coefficient, with constrained variants to improve supervision for long-tail items.
- **Key Innovations:**
  - Prefix-conditioned hierarchical view of semantic IDs aligned with generative recommender structure.
  - Adaptive, data-driven branching (AST) instead of fixed-codebook/fixed-factor quantization.
  - Improved performance over strong baselines across five Amazon Review datasets and better handling of heterogeneous density/long-tail regions.
- **arXiv:** https://arxiv.org/abs/2611.11549

### 2.7 IntentLens: Grounding Underspecified Multimodal Queries for Recommendation via Tool-Augmented Reasoning
- **Authors:** Xiao Chen, Dong Fang, Haitao Li, Qing Li
- **Affiliation:** —
- **Abstract:** Addresses recommendation from underspecified multimodal queries (reference image + vague text). IntentLens uses a ground-then-rank pipeline where a shared MLLM leverages visual tools, user memory, and item attribute retrieval to infer latent intent and produce query-conditioned evidence for candidates, followed by a lightweight ranker. Introduces GoogleReview-MMTool and Yelp-MMTool benchmarks.
- **Key Innovations:**
  - Tool-augmented grounding of ambiguous multimodal intent before user-item matching.
  - Query-conditioned candidate evidence augmentation combining visual, memory, and attribute signals.
  - New benchmarks for underspecified multimodal recommendation with reported gains over competitive MLLM/retrieval baselines and generalization to unseen categories/datasets.
- **arXiv:** https://arxiv.org/abs/2611.11346

### 2.8 Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems
- **Authors:** Zhiliang Chen, Sammy Nammari, Jiahao Su, Xiaoqiang Luo
- **Affiliation:** —
- **Abstract:** Studies compute-efficient evaluation of recommendation model changes by leveraging feature-invariant scaling behavior. Proposes a method that combines scaling laws with statistical inference to predict full-scale A/B effects (with confidence intervals) from small-scale experiments, enabling early filtering of neutral/regressive changes.
- **Key Innovations:**
  - Empirical observation and use of feature-invariant scaling laws across Wukong, HSTU, and LLM-based recommendation models.
  - Confidence-interval prediction of full-scale experimental outcomes from limited compute.
  - Demonstrated efficiency in distinguishing beneficial vs. neutral/regressive changes and identifying improvements to HSTU on MovieLens-20M.
- **arXiv:** https://arxiv.org/abs/2611.13539

---

## 3. Advertising, Ad Retrieval & LLM Advertising

### 3.1 TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
- **Authors:** Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi, Hualei Liu
- **Affiliation:** Taobao Shangou (Alibaba ecosystem; deployed in Taobao Shangou search advertising)
- **Abstract:** Proposes TS-GEAR, a generative ad retrieval framework for on-demand delivery where out-of-range merchants are invalid. Addresses geography-aware reachability, region/query-conditioned preference modeling, and set-level retrieval quality in autoregressive generation. Deployed online with a 0.1B backbone serving 150M+ queries/day.
- **Key Innovations:**
  - Geo-Semantic ID (geographic prefixes + semantic suffixes) to make reachability a learnable prediction target.
  - Query-Geo Target Attention to condition behavior aggregation on real-time query/location and encode behavior locations.
  - GMPO (Group Marginal Policy Optimization) for set-level/redundancy-aware training; reported online gains (+3.8% ad impressions, +4.2% ad revenue).
- **arXiv:** https://arxiv.org/abs/2611.12180

### 3.2 CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?
- **Authors:** Shiqi Zhang, Yang Fei, Xiaokui Xiao
- **Affiliation:** —
- **Abstract:** Formulates Context Hint Optimization (CHO) for LLM advertising, where advertisers provide natural-language hints to influence ad ranking in conversational contexts. Introduces CHO-Bench and evaluates seven hint-generation strategies (What/Who/When and Unified) with 1.19M+ paired evaluations across datasets and rankers.
- **Key Innovations:**
  - Benchmark and problem formulation for ad-side context-hint optimization in LLM advertising.
  - Systematic comparison of strategy families under embedding-based vs. LLM-based rankers, revealing ranker-dependent preferences.
  - Findings on budget effects (diminishing marginal gains) and opportunities for model-specific hint selection/aggregation.
- **arXiv:** https://arxiv.org/abs/2611.11955

---

## Notes

- **Scope:** This digest prioritizes papers from recent arXiv listings (Nov 7–11, 2026) relevant to the requested topics (AI/LLMs, recommendation, advertising, sequential modeling, CTR/ads, next-POI/generative retrieval). It is a curated snapshot, not an exhaustive crawl of all categories.
- **Affiliations:** Included when explicitly stated in abstracts/metadata snippets; otherwise marked as not specified.
- **Games:** No clearly matching recent game-focused papers were identified in the sampled recent listings for this window; future digests can broaden search if needed.
