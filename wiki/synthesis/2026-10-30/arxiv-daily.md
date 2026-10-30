---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, CTR, Sequential Modeling, Games (2026-10-30)"
type: synthesis
created: 2026-10-30
updated: 2026-10-30
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, sequential-recommendation, creative-optimization, moe, prompt-injection, rlvr]
---

# arXiv Daily Report (2026-10-30)

> Query time: 2026-10-30. Latest indexed mailing batch covers submissions from **2026-10-26 to 2026-10-27**; this report covers that batch. Abstracts are condensed from the arXiv API and all numbers are author-reported, not independently reproduced. Institutions are parsed from the rendered HTML author block or the PDF first page; where arXiv lists no affiliation, that is stated.
>
> Companion report: today's [arxiv-ai-search](arxiv-ai-search.md) covers a separate 30-paper sweep from the same window. The 18 papers below were selected to avoid overlap with that report.

## Summary

- **Sequential recommendation is being re-architected around what history to read and how much to compute.** LESSRec restricts cross-level token interference in semantic-ID recommenders; RELAY reuses one query for both preference readout and behavioral routing at 2.04M predictor parameters; BehaveRec quantifies *when* 90-day history actually helps and derives a ~20-interaction deployment threshold.
- **Generative recommendation (GR) is the densest cluster.** KL-MOPD fixes token-level teacher imbalance in multi-objective distillation and reports online A/B gains on an e-commerce ads platform; JevRec makes semantic-ID length frequency-dependent; Refiner adds latent residual reasoning to ranking; DARTS diagnoses sampling collapse in diffusion recommenders and recovers diversity.
- **Industrial CTR work focuses on input geometry and feature drift.** TRIP replaces inherited positional encodings with target-aware rank–time encoding (+4.45% AUC); an LY Corporation study shows daily item embeddings drift in norm by ~102% after eight days and that global rescaling recovers GAUC; OptIDC and HiRank are covered in the companion report.
- **Advertising is moving from slot auctions to generated inventory.** Roblox ships hierarchical empirical-Bayes Thompson sampling for creative pre-ranking (+8.14% predicted pTR, +0.2% serving time); DiffAuction auctions *configurations of a shared generated image*, with a VLM/LLM click-intent evaluator and a DSIC affine-maximizer auction.
- **Games serve as data and evaluation infrastructure.** GameVerse releases 1,655 hours of minute-scale gameplay for long-horizon world models; DECE and the Riichi Mahjong replication (companion report) use games to stress-test LLM agent configurations rather than game-playing skill alone.
- **LLM training and safety papers are unusually concrete.** Heads of Security cuts black-box prompt-injection ASR from 97% to 10% via learned per-head attention gates; EnergyCal removes ~99.5% of Muon MoE loss-spike burden with no persistent optimizer state; Guided-RLVR injects steering tokens to counter RLVR rollout collapse.

## Methodology and scope

- **Sweep**: arXiv Export API, sorted by `submittedDate`, over `cs.CL`, `cs.LG`, `cs.AI`, `cs.IR`, `cs.GT`, `cs.MA`, `stat.ML`, plus keyword queries for recommendation, advertising/auction, CTR, sequential, games, and LLM. 1,006 unique records were pooled; the in-window slice (2026-10-26→27) was screened by title/abstract.
- **Selection**: 18 papers balanced across recommendation/sequential modeling (11), CTR/advertising (3), games/world models (1), and LLM training/safety (3). Overlap with today's companion `arxiv-ai-search` report was removed.
- **Caveats**: abstract-level review only. Offline gains are not normalized across papers; online A/B results are single-company reports. Several papers withhold raw dataset sizes or item-level results (noted inline).

---

## A. Recommendation and Sequential Modeling

### 1. LESSRec: Level-Specific History Modeling for Semantic ID-Based Recommendation
- **arXiv**: [2610.37286](https://arxiv.org/abs/2610.37286)
- **Date**: 2026-10-27
- **Authors**: Shangxin Yang, Zongwei Wang, Jing Long, Junliang Yu, Min Gao
- **Institution/Company**: Chongqing University
- **Categories**: cs.IR
- **Abstract**: Semantic-ID recommenders encode items as residual-quantization token sequences and generate the next item coarse-to-fine, attending to history tokens at every semantic level. Inference-time analysis shows that history tokens at the *target token's own level* are more informative, while other levels introduce interference. LESSRec separately encodes each semantic level's history and, at prediction time, restricts attention to the level-aligned sequence, complementing it with a chronological item-level semantic sequence. The decoder reads both through separate cross-attention branches and fuses them. LESSRec+ uses separate encoders per level at the same total parameter count to cut encoder compute. Gains hold across three datasets and three tokenizers.
- **Key innovations**:
  - Diagnostic showing cross-level history tokens interfere in semantic-ID generation
  - Level-restricted attention plus a global item-level semantic stream
  - LESSRec+ trades shared parameters for level-specific encoders at iso-parameter budget

### 2. Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven Recommendation
- **arXiv**: [2610.37280](https://arxiv.org/abs/2610.37280)
- **Date**: 2026-10-27
- **Authors**: Mingzhe Lu, Jian Qin, Ruize Qin, Jinhao Liu, Yunpeng Li, Hang Su
- **Institution/Company**: Institute of Information Engineering (CAS); University of Chinese Academy of Sciences; University of Melbourne; independent researcher
- **Categories**: cs.IR, cs.CL
- **Abstract**: Narrative-driven recommendation lets users express multi-faceted needs in free text, where preferences qualify and condition one another; existing methods flatten narratives into keywords or unconstrained generative queries. The Preference Dependency Graph Framework (PDG-F) parses a request into a directed acyclic graph of preferences and their mutual qualifications, retrieves open-web evidence along directed paths, and ranks recommendations by topological path score. Experiments across three English and Chinese domains show gains over competitive baselines, retrieval agents, and frontier LLMs; dependency-guided retrieval raises the attainable candidate-pool ceiling.
- **Key innovations**:
  - Explicit DAG structure for inter-preference qualification instead of flat keyword queries
  - Directed-path retrieval + topological path ranking
  - Diagnostic separating retrieval-ceiling gains from ranking gains

### 3. AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems
- **arXiv**: [2610.37228](https://arxiv.org/abs/2610.37228)
- **Date**: 2026-10-27
- **Authors**: Rui Tian, Yi Fang, Yejin Hua, Du Wang, Yuzhe Wang, Minxuan Shan, Zirui Ren, Xinyu Lin, Chongming Gao, Wenjie Wang, Fuli Feng
- **Institution/Company**: University of Science and Technology of China; National University of Singapore
- **Categories**: cs.IR
- **Abstract**: LLM "recommender-systems engineer agents" (RSE-Agents) autonomously modify recommendation algorithms, but lacked a standardized evaluation. AutoRSE spans six industrial-grade recommendation tasks and evaluates three frontier LLMs across three agent harnesses. Agents improve backbones on five of six tasks (+16.1% average relative). Trajectory analysis shows they act as *engineering optimizers* — gains come mostly from hyperparameter tuning, training strategy, and ensembling, with few genuine algorithmic innovations. Injecting ideas from frontier research or human experts yields much larger gains than self-generated ideas, identifying idea generation as the bottleneck.
- **Key innovations**:
  - Standardized six-task benchmark for RSE-Agents with trajectory-level analysis
  - Evidence that current agents optimize engineering knobs, not algorithms
  - Idea-injection experiments isolating ideation as the limiting capability

### 4. KL-MOPD: Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation
- **arXiv**: [2610.36973](https://arxiv.org/abs/2610.36973)
- **Date**: 2026-10-27
- **Authors**: Weiqin Yang, Yandong Wang, Yuan Gao, Hao Deng, Jinxin Hu, Jing Cao, Jiawei Chen
- **Institution/Company**: Zhejiang University (industrial e-commerce advertising deployment)
- **Categories**: cs.IR
- **Abstract**: Multi-objective generative recommendation (e.g., click and conversion) needs token-level supervision because an item is retrieved only if every SID token is selected. Vanilla multi-objective on-policy distillation (MOPD) suffers token-level imbalance and cross-token inconsistency: the harder teacher changes across decoding steps. KL-MOPD weights each teacher per token in proportion to initial student–teacher KL divergence, strengthening supervision for whichever teacher is harder at that step. The authors prove it strictly beats vanilla MOPD on the additive joint objective under mild conditions, with one-time weight calibration and negligible overhead. Results cover three public benchmarks, a billion-scale industrial dataset, and online A/B tests on an e-commerce ads platform.
- **Key innovations**:
  - Token-wise KL-based teacher weighting for multi-objective GR distillation
  - Theoretical improvement guarantee over vanilla MOPD
  - Plug-and-play with billion-scale and online advertising validation

### 5. BehaveRec: When Does Long-Term Behavioral History Help Sequential Recommendation? A Study with Session, History, and Community Signals
- **arXiv**: [2610.36239](https://arxiv.org/abs/2610.36239)
- **Date**: 2026-10-26
- **Authors**: Aysenur Inan, Reza Yousefi Maragheh, Jayesh Uddhav Kudase, Selene Xu, Kaushiki Nag, Jianpeng Xu, Sushant Kumar
- **Institution/Company**: Walmart Global Tech
- **Categories**: cs.AI, cs.IR
- **Abstract**: BehaveRec combines a causal session transformer, a bidirectional 90-day user-history encoder, and GraphSAGE over a user–user graph built from behavioral-embedding similarity (not item co-occurrence), blended by a learned per-user gate. On 137M sequences from 12.6M users it improves R@5 by 3.2% over SASRec; a larger SASRec still trails by 2.5%, ruling out capacity. Stratification shows a dose–response effect: the gain is negligible below ~10 interactions and grows monotonically, reaching +0.017 R@5 for users with 101+ events. This supports a deployment rule of ~20 interactions. The model has 5.67M parameters and trains on one GPU in under two days. The headline result is category-level intent; a single-run full item-level check is directionally mixed and explicitly scoped as open.
- **Key innovations**:
  - Three-signal gated architecture with a behavior-similarity user graph
  - User-level stratification establishing when long history pays off
  - Practical ~20-interaction deployment threshold at 5.67M parameters

### 6. RELAY: One Query, Two Roles for Sequential Recommendation
- **arXiv**: [2610.36000](https://arxiv.org/abs/2610.36000)
- **Date**: 2026-10-26
- **Authors**: Zesheng Li, Chengchang Pan, Honggang Qi
- **Institution/Company**: University of Chinese Academy of Sciences
- **Categories**: cs.IR
- **Abstract**: RELAY uses a single learned query for two roles: semantic preference readout and behavioral-memory routing. The same attention selects direct-history and transition evidence for candidate scoring, with candidate-conditioned gates calibrating the two memory channels. It trains both roles with one catalog likelihood and ranks in a single forward pass. On six datasets it achieves the best Recall@5 and NDCG@5, improving over the previous best by 14.22% and 17.88% on average, with 2.044M predictor parameters (65.12% smaller) and a 1.75–1.79× inference speedup.
- **Key innovations**:
  - Single-query dual-role design coupling preference and behavioral evidence
  - Candidate-conditioned gating of history vs. transition channels
  - Large efficiency win at full-catalog evaluation

### 7. From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn
- **arXiv**: [2610.36383](https://arxiv.org/abs/2610.36383)
- **Date**: 2026-10-26
- **Authors**: Jian Sheng, Sriram Vasudevan, Sundara Raman Ramachandran, Yang Hu, Junyu Zhou, Xiaojing Ma, Haolan Qin, Tiffany Zhou, Vedant Vipul Jhaveri, Ashwini Bhingare, Chinmay Kini, Qing Lan, Xiaoqing Wang, Suleyman Cetintas, Fedor Borisyuk
- **Institution/Company**: LinkedIn
- **Categories**: cs.LG, cs.DC, cs.IR
- **Abstract**: Industrial LLM labelers often pack many candidate labels into one prompt and generate a YES/NO list, coupling otherwise independent decisions and relying on well-formed output. LinkedIn reformulates the labeler as semantic scoring: fine-tune on single-candidate prompts and read each decision as one answer-token score from a prefill-only pass. Multiple-Item Scoring (MIS) extends this to hundreds of candidates per sequence with attention masked between them. In profile-qualification labeling, reordering candidates changes at most 0.01% of decisions, and the scorer matches packed generation's reference agreement with ~4.7× fewer training pairs. The MIS stack raises throughput 1.24× offline and 1.9× in serving under a 1-second p99 target; components were contributed to Ray Data and SGLang.
- **Key innovations**:
  - Generation → prefill-only scoring reformulation for LLM labeling
  - Attention-masked multiple-item scoring for high-throughput batch inference
  - Production deployment with order-invariance and latency evidence

### 8. Latent Residual Reasoning for Ranking in Generative Recommendation (Refiner)
- **arXiv**: [2610.36890](https://arxiv.org/abs/2610.36890)
- **Date**: 2026-10-27
- **Authors**: Haihan Shi, Ruidong Han, Wenjie Wang, Shangyu Chen, Sunhao Dai, Yongqi Li, Yangyang Li, Fei Jiang, Wei Lin, Fuli Feng, Xiangnan He
- **Institution/Company**: University of Science and Technology of China; Meituan; Renmin University of China; Hong Kong Polytechnic University; Academy of Cyber
- **Categories**: cs.IR
- **Abstract**: Generative recommenders for ranking usually make one-shot predictions, while ranking needs fine-grained candidate scores. Refiner adds latent residual reasoning to ID-based generative ranking with three components: cumulative additive residual corrections that progressively refine scores, history queries that condense user behavior for candidate-specific reasoning, and LoRA-based parameter-efficient fine-tuning for latent reasoning. Experiments on two public benchmarks, an offline industrial dataset, and an online A/B test show consistent gains over direct prediction.
- **Key innovations**:
  - Residual latent reasoning as iterative score refinement for GR ranking
  - History-query conditioning for candidate-specific reasoning
  - LoRA adaptation of pretrained GR models without full retraining

### 9. JevRec: Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation
- **arXiv**: [2610.36937](https://arxiv.org/abs/2610.36937)
- **Date**: 2026-10-27
- **Authors**: Qiyong Zhong, Jiajie Su, Ming Yang, Li Zhang
- **Institution/Company**: Zhejiang University
- **Categories**: cs.CL
- **Abstract**: GR assigns uniform semantic-ID length to all items despite unequal interaction frequency, over-spending fine codes on popular items and compressing long-tail semantics when codes are shortened. JevRec encodes items as variable-length "words": frequency-dependent semantic prefixes yield shorter SIDs for popular items and richer descriptions for long-tail items. Because predicting sequence-level length and generating token content conflict under a shared head, a Jev-like decision component predicts a length distribution with a dedicated head and generates content conditioned on length with a separate head, sharing only the history representation. On three public datasets it beats all baselines, runs faster in training and inference than TIGER, and shows reduced gradient conflict.
- **Key innovations**:
  - Frequency-adaptive variable-length semantic IDs
  - Decoupled length-prediction and content-generation heads
  - Lower gradient conflict and lower runtime than TIGER

### 10. When Diffusion Recommenders Stop Sampling: Preserving Generative Diversity (DARTS)
- **arXiv**: [2610.36954](https://arxiv.org/abs/2610.36954)
- **Date**: 2026-10-27
- **Authors**: Louis Castres Saint Martin, Alain Rakotomamonjy, Patrick Gallinari
- **Institution/Company**: Criteo AI Lab; Sorbonne Université / CNRS / ISIR
- **Categories**: cs.IR
- **Abstract**: Target-item diffusion recommenders are supposed to sample alternative plausible continuations, but the authors show severe sampling collapse: independent draws are nearly identical. Two design choices drive it — joint learning of latent space and denoiser, and in-trajectory discrete-loss supervision. DARTS is a three-stage latent diffusion framework that decouples representation learning, generative modeling, and discrete ranking: learn and freeze the latent space before diffusion training, and postpone ranking supervision to final decoding. It characterizes diversity before and after decoding and uses posterior-predictive aggregation. On three Amazon Reviews 2023 categories it preserves substantially more diversity while beating sequential, generative-retrieval, and diffusion baselines by 7–12% on ranking metrics.
- **Key innovations**:
  - Diagnosis of sampling collapse in diffusion recommenders
  - Three-stage decoupling of latent learning, diffusion, and ranking
  - Diversity metrics + posterior-predictive aggregation at inference

### 11. Cross-Day Compatibility of Daily Item Embeddings: An Empirical Study of Alignment, Scale Management, and CTR Adaptation
- **arXiv**: [2610.36408](https://arxiv.org/abs/2610.36408)
- **Date**: 2026-10-26
- **Authors**: Yicheng Wang
- **Institution/Company**: LY Corporation
- **Categories**: cs.IR
- **Abstract**: Daily item co-occurrence embeddings avoid future-behavior leakage, but multi-day CTR training mixes versions whose directions and norms differ for the same item. This industrial study compares Word2Vec and an item-graph XSimGCL adaptation across initialization, inheritance, post-processing, constraints, and augmentation — 48 configurations, 32 common-protocol CTR evaluations. ID-initialization and orthogonal alignment raise cross-day cosine by 51.2% and 93.4% and GAUC by 2.2% and 2.6%. Warm starts help but accumulate scale: the day-matched norm increase reaches 102.5% after eight days; daily global rescaling limits it to 8.2% and gives the highest GAUC gain (4.0%). A trained dimensionality-reducing encoder best adapts residual drift, achieving the highest cross-day cosine for four of six upstream methods. Raw values and exact dataset sizes are withheld.
- **Key innovations**:
  - Controlled 48-configuration study of embedding drift across days
  - Separates direction alignment, norm/scale management, and downstream adaptation
  - Shows retrieval/geometry proxies are insufficient surrogates for CTR

## B. CTR and Advertising

### 12. Rethinking Positional Encoding and Interaction Granularity for CTR Prediction (TRIP)
- **arXiv**: [2610.37140](https://arxiv.org/abs/2610.37140)
- **Date**: 2026-10-27
- **Authors**: Xinxun Zhang, Yuxiang Wang, Xiaokai Zhou, Jiayue Li, Yi Li, Yue Liu, Jun Zhang, Xiaoling Zhou, Tieyun Qian, Xiao Yan, Jiawei Jiang
- **Institution/Company**: Wuhan University; Tencent Inc.; Peking University
- **Categories**: cs.IR
- **Abstract**: Transformer CTR models typically use index-based or temporal positional encodings and token-level causal interaction, yet the authors observe that most such encodings do not beat NoPE, and that relaxing causality within target-relative temporal groups helps. TRIP combines target-aware rank–time positional encoding with temporal-group interaction: factorized rank encoding captures ordinal position via low-rank factorization, target-relative time encoding captures distance to the target at coarse-to-fine scale, and temporal group-causal interaction allows bidirectional intra-group mixing with masked reconstruction while preserving inter-group causal order. Group summaries keep later layers efficient. On four public benchmarks TRIP improves AUC by up to 4.45% over the strongest baseline.
- **Key innovations**:
  - Empirical case that inherited positional encodings often lose to NoPE in CTR
  - Factorized rank + target-relative time encoding
  - Group-causal interaction granularity instead of token-level causality

### 13. Exploratory Creative Pre-ranking: Hierarchical Empirical-Bayes Thompson Sampling for Real-Time Creative Optimization
- **arXiv**: [2610.36020](https://arxiv.org/abs/2610.36020)
- **Date**: 2026-10-26
- **Authors**: Jiale Han, Ajith Moparthi, Dan Xie, Xiaowu Dai
- **Institution/Company**: UCLA Department of Statistics and Data Science; Roblox
- **Categories**: cs.LG, cs.GT
- **Abstract**: Dynamic creative optimization picks which ad creative to render per request. AI-generated creatives are nearly free, but feedback per creative is sparse and latency is tight. The proposed pre-ranker scores every recalled creative and shortlists each campaign's pool before per-user ranking. Creatives sit in a hierarchy (audience segment → advertised item → campaign → creative), so a cold creative borrows from parent levels with a closed-form, one-parameter-per-level amount. To meet latency, it predicts at audience-segment rather than user level from per-attribute counters and selects via one Thompson draw per creative. Replaying Roblox sponsored-ads traffic, the shortlist lifts predicted play-through rate by 8.14% versus 2.80% for a random shortlist, forwards >40% fewer creatives, and adds 0.2% serving time. It now serves in production after a live A/B test.
- **Key innovations**:
  - Hierarchical empirical-Bayes shrinkage with closed-form borrowing
  - Segment-level Thompson sampling for sub-millisecond pre-ranking
  - Production deployment at Roblox with replay and A/B evidence

### 14. DiffAuction: An Auction-Driven Framework for Generative Image Advertising
- **arXiv**: [2610.34917](https://arxiv.org/abs/2610.34917)
- **Date**: 2026-10-26
- **Authors**: Yijie Su, Ruiyang Si, Tonghan Wang
- **Institution/Company**: Tongji University; Tsinghua University; Shanghai Qi Zhi Institute
- **Categories**: cs.CV
- **Abstract**: Diffusion models let multiple advertisers compete for exposure inside one generated image, but generation under varying target shares is costly and outcomes are hard to evaluate and price. DiffAuction integrates controllable generation, click-intent evaluation, and auction design. Training-free Residual Share Calibration decomposes joint-attention updates into product-specific residuals rescaled to target shares, and Share-Conditioned Prompting adapts viewpoint. A VLM extracts visual evidence and an LLM scores Click-Through Intent along prominence, brand recognizability, scene integration, and contextual value, validated against 10 trained annotators on 1,000 images. The setting is formulated as an auction over jointly feasible generation configurations with public expected CTI vectors and private per-unit values; a learnable affine maximizer auction selects the shared configuration and payments, guaranteeing DSIC and IR while raising platform revenue.
- **Key innovations**:
  - Training-free share-controlled multi-advertiser image generation
  - VLM+LLM click-intent evaluator validated with human annotators
  - Auction over generation configurations with DSIC/IR guarantees

## C. Games and World Models

### 15. GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling
- **arXiv**: [2610.37257](https://arxiv.org/abs/2610.37257)
- **Date**: 2026-10-27
- **Authors**: Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu, Zhengyuan Lin, Yuzhe Ding, Donghong Ji, Kaipeng Zhang, Yongtao Ge
- **Institution/Company**: Alaya Lab; Shanghai Innovation Institute; Wuhan University
- **Categories**: cs.CV
- **Abstract**: Interactive world models lose coherence beyond roughly one minute, a data rather than capacity limitation: existing gameplay datasets are mostly sub-10-second clips with coarse whole-clip captions. GameVerse provides 69.7K clips, 1,655 hours, and 349.6M frames of first- and third-person gameplay, including 1,358 hours of continuous two-minute sequences — an order of magnitude longer than prior datasets. A unified pipeline performs scene-consistent segmentation, quality filtering, camera-pose estimation, and event-based captioning; captions separate static scene context from dynamic foreground events and align to event boundaries instead of fixed windows. Training on GameVerse substantially extends the temporal horizon of interactive world models.
- **Key innovations**:
  - Minute-scale gameplay corpus with 1,358 hours of continuous 2-minute sequences
  - Event-aligned captions separating static context from dynamic events
  - Stable camera trajectories spanning minutes for controllable rollouts

## D. LLM Training and Safety

### 16. Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness
- **arXiv**: [2610.37657](https://arxiv.org/abs/2610.37657)
- **Date**: 2026-10-27
- **Authors**: Igor Shilov, Xiaoxue Yang, Alexander Panfilov, Evgenii Kortukov, Matthieu Meeus, Peter Romov, Wojciech Samek, Jonas Geiping, Yves-Alexandre de Montjoye
- **Institution/Company**: Imperial College London; Tübingen AI Center; ELLIS Institute Tübingen; Max Planck Institute for Intelligent Systems; Fraunhofer HHI
- **Categories**: cs.LG, cs.CL, cs.CR
- **Abstract**: Heads of Security (HoS) enforces instruction–data separation with a small set of learned per-head attention gates that redistribute attention between trusted and untrusted tokens, so models can reason over untrusted content without following injected instructions. On Llama-3.3-70B-Instruct and GPT-OSS-20B, the black-box RL-Hammer attack reaches 97% ASR on GPT-OSS-20B and 85% on SecAlign, but 10% on HoS; the white-box Claudini attack needs 3× more FLOPs to reach the same ASR on HoS. HoS preserves base utility on multiple-choice and few-shot prompting where SecAlign and ASIDE degrade, and matches SecAlign on static agentic attacks; ASIDE reaches only 10% utility with tools.
- **Key innovations**:
  - Per-head learned attention gating for instruction–data separation
  - Large ASR reduction against adaptive black- and white-box attacks
  - Better security–utility trade-off than finetuning or architecture baselines

### 17. EnergyCal: Taming Loss Spikes in Muon-Family Optimizers for Sparse MoE Training
- **arXiv**: [2610.37062](https://arxiv.org/abs/2610.37062)
- **Date**: 2026-10-27
- **Authors**: Masato Fujitake
- **Institution/Company**: FA Research, Fast Accounting Co., Ltd.
- **Categories**: cs.LG, cs.AI, cs.CL
- **Abstract**: Sparse MoE language-model training can show large loss spikes with Muon-family optimizers. EnergyCal attenuates routed-expert updates according to the normalized squared Frobenius norm of their finite-step Newton–Schulz directions. It leaves the spectral transform unchanged and adds no persistent optimizer state. On a 4B-parameter MoE, versus a development-selected lower-learning-rate MuonH recipe, EnergyCal–MuonH reduces mean thresholded loss-spike burden by 99.51% and final geometric-mean perplexity by 4.06% at modest throughput cost. With plain Muon at matched nominal learning rate and weight decay, mean spike burden falls 95.98% across two tested exponents with small endpoint improvements.
- **Key innovations**:
  - Update-energy normalization for routed experts in Muon optimizers
  - No change to the spectral transform and no extra optimizer state
  - ~99.5% spike-burden reduction on a 4B MoE

### 18. Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards
- **arXiv**: [2610.37041](https://arxiv.org/abs/2610.37041)
- **Date**: 2026-10-27
- **Authors**: Bo Yang, Zishuai Zhang, Weihua Li, Qinnan Zhang, Sijia Wen, Hainan Zhang
- **Institution/Company**: Beihang University
- **Categories**: cs.AI, cs.CL
- **Abstract**: RLVR improves LLM reasoning on math and code but rollouts collapse onto a narrow set of trajectories. Guided-RLVR adds a lightweight controller that injects semantically meaningful steering tokens into the sampling distribution at critical steps, pushing the model toward multiple reasoning perspectives. On mathematical-reasoning and code-generation benchmarks it consistently outperforms existing RLVR methods while producing more diverse reasoning trajectories.
- **Key innovations**:
  - Controller-injected steering tokens at critical reasoning steps
  - Explicitly targets rollout collapse / exploration width in RLVR
  - Gains on both math and code with higher trajectory diversity

---

## Cross-references

- Companion sweep: [arxiv-ai-search (2026-10-30)](arxiv-ai-search.md) — 30 non-overlapping papers on generative retrieval, auctions, agent memory, looped Transformers, and agent benchmarks.
- Recent CTR/rec context: [ctr-scaling-landscape](../ctr-scaling-landscape.md), [arxiv daily 2026-10-25](2026-10-25/arxiv-daily.md), [arxiv daily 2026-10-23](2026-10-23/arxiv-daily.md).
