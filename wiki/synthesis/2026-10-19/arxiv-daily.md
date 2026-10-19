---
title: arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-19)
type: synthesis
created: 2026-10-19
updated: 2026-10-19
sources: []
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation]
---

# arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-19)

> Auto-generated from recent arXiv publications (primarily 2026)

## Summary

Recent research in AI/ML for recommendation and advertising focuses on: scaling laws for sequence models in production (LLaTTE, ReST), generative/LLM-backed ranking (GRAB, GenRec, OneRanker), multimodal/cold-start with LLMs (IDProxy, LLM-HYPER), live-streaming/adapting to temporal dynamics (TAGR), efficient long-sequence modeling (SparseCTR), unified context-centric modeling (UniCon), and lightweight LLM enhancement (LLaCTR).

---

## 1. LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation

- **arXiv**: [2601.20083](https://arxiv.org/pdf/2601.20083)
- **Date**: 2026-01-27
- **Authors**: Lee Xiong, Zhirong Chen, Rahul Mayuranath, Shangran Qiu, Arda Ozdemir, Lu Li, Yang Hu, Dave Li, Jingtao Ren, Howard Cheng, Fabian Souto Herrera, Ahmed Agiza, Allen Lin, Baruch Epshtein, Anuj Aggarwal, Julia Ulziisaikhan, Chao Wang, Dinesh Ramasamy, Parshva Doshi, Sri Reddy, Arnold Overwijk (Meta AI)
- **Institution/Company**: AI at Meta

### Abstract

LLaTTE (LLM-Style Latent Transformers for Temporal Events) is a scalable transformer architecture for production ads recommendation. It demonstrates that sequence modeling in recommender systems follows predictable power-law scaling similar to LLMs; semantic features "bend" scaling curves (prerequisite for effective scaling with depth/length). To satisfy latency constraints, LLaTTE uses a two-stage architecture: a heavy asynchronous upstream user model produces cached compressed user embeddings; online ranking combines cached embeddings with fresh short-horizon signals via a lightweight LLaTTE. Upstream improvements transfer predictably (~50%) to downstream ranking. Deployed at Meta (largest user model), multi-stage framework drives 4.3% conversion uplift on Facebook Feed and Reels with minimal serving overhead.

### Key Innovations

- **Target-Aware Adaptive Transformer**: Integrates non-sequence sparse/candidate features into extended query tokens; leverages Multi-head Latent Attention (MLA); supports adaptive pyramidal output extraction to reduce compute.
- **Multi-Stage Architecture**: Upstream runs large LLaTTE (>>45× FLOPs of online) triggered by high-value events to asynchronously cache user embeddings; online uses lightweight counterpart with fresh short signals.
- **Scaling Law Insights**: Performance follows log-linear scaling (sequence length key); semantic content embeddings are prerequisite for steeper scaling (bend curves beyond IDs); cross-stage transfer ratio ~50%; width is bottleneck before depth becomes effective.
- **Production Impact**: 0.25% NE reduction on flagship ads ranker; 4.3% conversion uplift on Facebook Feed/Reels.

---

## 2. GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm

- **arXiv**: [2602.01865v2](https://arxiv.org/abs/2602.01865v2)
- **Date**: 2026-02-02 (v1), revised 2026-02-03 (v2)
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin
- **Institution/Company**: Baidu

### Abstract

GRAB (Generative Ranking for Ads at Baidu) is an end-to-end generative framework for CTR prediction inspired by LLM scaling. It introduces Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics and specific action signals in user behavior sequences. Full-scale online deployment shows significant gains (3.05% revenue increase, 3.49% CTR increase). Model shows monotonic, approximately linear improvement as sequence length increases.

### Key Innovations

- **Sequence-First Generative Paradigm** for CTR prediction inspired by LLM scaling success.
- **Causal Action-aware Multi-channel Attention (CamA)**: Effectively models temporal dynamics and specific action signals within user behavior sequences.
- **Strong Online Impact**: 3.05% revenue uplift, 3.49% CTR uplift in full-scale deployment.
- **Favorable Scaling**: Expressive power improves monotonically and roughly linearly with longer interaction sequences.

---

## 3. From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs

- **arXiv**: [2609.01240](https://arxiv.org/abs/2609.01240)
- **Date**: 2026-09-01
- **Authors**: Jie Chen, Xiangqian Yu, Yanchao Lian, Tan Lu, Run Yang, Zhengchun Shang, Xing Wang, Cheng Chen, Ke Hu, Qiang Li, Tianjiu Yin, Xiaobing Liu
- **Institution/Company**: (unspecified in abstract)

### Abstract

ReST is a recommendation-native Transformer scaling framework addressing: (1) signal quality—behavior sequences are noisy, temporally irregular, sparsely supervised; (2) computation asymmetry—each request scores many candidates against shared user history under tight latency. Signal-quality mechanisms: dual-gated attention, rotary positional and temporal embedding, stabilized residual normalization, training-only auxiliary objectives. Compute asymmetry handled by factorization into heavy reusable encoder + lightweight cross decoder with projection-free KV attention and token-specific parameterization; couples user-level shared-prefix training with shared-prefix serving (compute-once, decode-many). Outperforms LLM-style blocks on industrial/public benchmarks; scales better with sequence length/depth/width. One-week A/B test improves online AUC by 1.31% and core revenue metric by 11.93% under 50ms P99; fully deployed.

### Key Innovations

- **Rec-Native Encoder**: Dual-gated attention, rotary positional+temporal embeddings, stabilized residual normalization, training-only auxiliary objectives to handle noisy/irregular/sparsely supervised behavior.
- **Encoder+Cross-Decoder Factorization**: Heavy reusable encoder; lightweight cross decoder with projection-free KV attention and token-specific parameterization.
- **Shared-Prefix Training/Serving**: Compute-once, decode-many-times for ranking under tight latency.
- **Strong Production Results**: +1.31% online AUC, +11.93% core revenue metric (1-week A/B); 50ms P99 budget.

---

## 4. UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction

- **arXiv**: [2609.03290](https://doi.org/10.48550/arxiv.2609.03290)
- **Date**: 2026-09-03
- **Authors**: Jiajun Cui, Zhengqi Xu, Fan Zhang, Zhangteng, Gu Tang, Honghong Zhu et al.
- **Institution/Company**: Meituan Search Advertising

### Abstract

Existing unified CTR models split sequential/non-sequential signals at token level in shared backbone—misaligned with decision process (history vs request differ only in observed/predicted). UniCon treats request context as basic modeling unit; history and prediction targets as homogeneous context units. Intra-context attention captures local coupling (Locality); inter-context attention models dynamic evolution across contexts (Dynamics). Bridges history-target gap and improves scaling. Context-unit sequence compression reduces deployment overhead. On Meituan search ads: +0.0139 offline AUC vs strong production baseline; online +3.09% RPM, +2.07% CTR, +2.95% revenue.

### Key Innovations

- **Context-Centric Unitization**: Treats request context as basic unit; history and prediction targets as homogeneous context units (vs heterogeneous split).
- **Intra/Inter-Context Attention**: Locality (within context) + Dynamics (across contexts) to capture evolution.
- **Context-Unit Compression**: Reduces deployment overhead.
- **Strong Online Impact (Meituan Search Ads)**: +3.09% RPM, +2.07% CTR, +2.95% revenue.

---

## 5. OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation

- **arXiv**: [2603.02999v2](https://arxiv.org/abs/2603.02999v2)
- **Date**: 2026-03-03 (v2)
- **Authors**: (not fully listed in abstract)
- **Institution/Company**: Tencent WeiXin Channels Advertising

### Abstract

Addresses three challenges in end-to-end generative ads: misalignment between interest objectives and business value, target-agnostic generation, disconnection between generation/ranking. OneRanker achieves deep integration: (1) Value-aware multi-task decoupling with task token sequences and causal mask to separate interest coverage/value optimization; (2) Coarse-to-fine collaborative target awareness via Fake Item Tokens (implicit) and ranking decoder (explicit value alignment); (3) Input-output dual-side consistency via Key/Value pass-through and Distribution Consistency (DC) Constraint Loss for end-to-end collaboration. Deployed on Tencent WeiXin Channels Ads: significant GMV-Normal improvement (+1.34%).

### Key Innovations

- **Value-Aware Multi-Task Decoupling**: Task tokens + causal mask to separate interest coverage and value optimization spaces.
- **Coarse-to-Fine Target Awareness**: Fake Item Tokens (generation-time implicit) + ranking decoder (candidate-level explicit).
- **Dual-Side Consistency**: KV pass-through + Distribution Consistency (DC) loss between generation and ranking.
- **Production Impact**: +1.34% GMV-Normal on Tencent WeiXin Channels Ads.

---

## 6. DMGIN: How Multimodal LLMs Enhance Large Recommendation Models for Lifelong User Post-click Behaviors

- **AAAI 2026 / arXiv context**: [10.1609/aaai.v40i19.38626](https://doi.org/10.1609/aaai.v40i19.38626) (AAAI Proceedings 2026)
- **Date**: 2026-03-14
- **Authors**: Zhuoxing Wei (PKU), Qingchen Xie (Meituan), Qi Liu (USTC), Jingsong Yu (PKU)
- **Institution/Company**: PKU, Meituan, USTC

### Abstract

Modeling lifelong user behavior sequences is key for CTR prediction, but long post-click sequences are computationally expensive. DMGIN reorganizes complete lifelong post-click sequences by grouping repeated/highly relevant shops (identified via consistent shop names/images) using MLLMs—almost no extra overhead vs directly injecting multimodal embeddings. To mitigate info loss: (1) analyze behaviors within each group via interest statistics + intra-group transformers to capture group traits; (2) inter-group transformers on temporally ordered groups to capture evolution. Extensive offline+online tests in Meituan/LBS advertising show effectiveness/efficiency. Online A/B test: +4.7% CTR, +2.3% RPM vs two-stage long-sequence CTR baseline.

### Key Innovations

- **MLLM-Guided Grouping**: Groups repeated/relevant shops from lifelong post-click sequences using MLLMs (efficient vs raw multimodal embedding injection).
- **Intra-Group Modeling**: Interest statistics + intra-group transformers capture group traits.
- **Inter-Group Temporal Modeling**: Inter-group transformers on temporally ordered groups capture interest evolution.
- **Production Impact (LBS Ads)**: +4.7% CTR, +2.3% RPM.

---

## 7. LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks

- **arXiv**: [2604.12096](https://arxiv.org/abs/2604.12096)
- **Date**: 2026-04-13
- **Authors**: Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, K.C. Yao, et al.
- **Institution/Company**: Top U.S. e-commerce platform (unspecified)

### Abstract

For newly introduced ads with insufficient feedback (cold-start), LLM-HYPER treats LLMs as hypernetworks to directly generate parameters of CTR estimator in training-free manner. Uses few-shot Chain-of-Thought over multimodal ad content (text+images) to infer feature-wise weights for linear CTR predictor. Retrieves semantically similar past campaigns via CLIP embeddings as demonstrations. Applies normalization/calibration to align generated weights with production-ready CTR distributions. Offline: significantly outperforms cold-start baselines (NDCG@10 +55.9%). Real-world online A/B test on top U.S. e-commerce platform: drastically reduces cold-start period and achieves competitive performance; successfully deployed in production.

### Key Innovations

- **LLM-as-Hypernetwork**: Training-free generation of CTR estimator parameters for cold-start ads.
- **Multimodal Few-Shot CoT**: Reasons over ad text+images with retrieved similar past campaigns (CLIP) as demonstrations.
- **Feature-Wise Linear Weights**: Generates weights for linear CTR predictor with normalization/calibration to production distributions.
- **Strong Results**: Offline NDCG@10 +55.9% vs cold-start baselines; online A/B shows drastic cold-start reduction and competitive performance.

---

## 8. GenRec: An LLM-Backed Recommendation Ranker at Netflix

- **arXiv**: [2608.10257v2](https://arxiv.org/html/2608.10257v2)
- **Date**: 2026-08-21 (v2)
- **Authors**: Agarwal et al.
- **Institution/Company**: Netflix

### Abstract

GenRec is LLM-backed recommendation ranker built on in-house foundational LLM. Two-phase: (1) adapt open-source LLM to Netflix data (catalog/member behavior, balance content understanding + instruction following); (2) post-train with recommendation-ranking specific data/labels/rewards to align with business requirements and long-term member satisfaction. Transition from discriminative ranker with thousands of engineered features to LLM-backed ranker driven by verbalized user histories/context. Describes input verbalization/context engineering, post-training data, reward integration, architecture, cost-constrained serving (prefill-only). Large-scale A/B test vs production ranker: GenRec trained with substantially fewer Phase-2 labeled examples and input signals achieves statistically significant gains in offline and online metrics. Discusses paradigm shift (feature engineering → context engineering; bespoke → shared foundation).

### Key Innovations

- **Foundation-Model Approach**: Adapts open-source LLM to Netflix domain, then post-trains for ranking with business-aligned rewards.
- **Verbalized Inputs**: Replaces thousands of engineered features with verbalized user histories and context.
- **Efficient Serving**: Cost-constrained design using prefill-only inference.
- **Data/Signal Efficiency**: Achieves significant offline/online gains with fewer labeled examples and fewer input signals than production ranker.

---

## 9. TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming Advertising

- **arXiv**: [2608.24034](https://doi.org/10.48550/arxiv.2608.24034)
- **Date**: 2026-08-25
- **Authors**: Wencai Ye, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, et al.
- **Institution/Company**: Large-scale e-commerce live-stream advertising platform

### Abstract

Live-streaming ads require freshness due to rapidly changing live content, promoted products, user feedback. TAGR provides temporal adaptation at three levels: (1) **Live Semantic-Collaborative ID (LSID)**: periodically refreshes each active ad's SID based on current live scene and promoted products; retains stable hierarchical token vocabulary for autoregressive generation. (2) **Intent-Aware Generation (IAG)**: models live-room entry histories at multiple temporal granularities as primary intent sequence; keeps auxiliary behaviors separate; weights next-token prediction using post-request intent evidence and business value. (3) **Intermittent On-Policy Preference Optimization (IOPO)**: periodically samples fresh candidate groups from current policy and performs behavior- and value-aligned preference updates interleaved with supervised NTP to preserve behavior distribution. Deployed on large-scale e-commerce live-stream ads platform: +8.5% live-room entry rate, +7.4% shopping-cart click rate, +16.1% revenue lift vs production baseline.

### Key Innovations

- **LSID (Live Semantic-Collaborative IDs)**: Periodic refresh of ad SIDs reflecting current live scene/promoted products while keeping stable hierarchical vocabulary.
- **IAG (Intent-Aware Generation)**: Multi-granularity live-room entry history as primary intent; auxiliary behaviors separate; NTP weighted by post-request intent evidence + business value.
- **IOPO (Intermittent On-Policy Preference Optimization)**: Fresh on-policy candidate sampling with behavior/value-aligned preference updates interleaved with supervised NTP.
- **Massive Online Impact**: +8.5% live-room entry, +7.4% cart clicks, +16.1% revenue lift.

---

## 10. Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction (SparseCTR)

- **arXiv**: [2601.17836v1](https://arxiv.org/abs/2601.17836v1)
- **Date**: 2026-01-25
- **Authors**: Weijiang Lai, Beihong Jin†, Di Zhang, Siru Chen, Jiongyan Zhang, Yuhang Gou, Jian Dong, Xingxing Wang (Meituan)
- **Institution/Company**: Institute of Software CAS + Meituan; WWW'26

### Abstract

Deploying Transformer-style models with quadratic self-attention for long-term user behaviors is challenging in production. SparseCTR introduces efficient sparse attention tailored to recommendation (personalization + temporal non-uniformity). Key components: (1) **TimeChunking**: personalized time-aware chunking segments sequences into same number of varied-length chunks (high cohesion within, low coupling between), enabling parallel processing. (2) **RelTemporal**: composite relative temporal encoding via learnable head-specific bias coefficients capturing time duration/hour/weekend (sequential + periodic). (3) **EvoAttention**: three-branch sparse self-attention over chunks to jointly capture global interests, interest transitions, and short-term interests. Extensive offline tests show SOTA performance and clear scaling laws across 3 orders of magnitude in FLOPs. Online A/B: +1.72% CTR, +1.41% CPM.

### Key Innovations

- **Personalized TimeChunking**: Varied-length chunks preserving behavioral continuity while enabling parallelism.
- **RelTemporal Encoding**: Learnable head-specific biases for relative time (duration/hour/weekend) to model sequential+periodic relations.
- **EvoAttention (Three-Branch)**: Global + transition + local sparse attention over chunks for multi-perspective interest modeling.
- **Scaling Laws + Online Gains**: Clear scaling across 3 FLOP orders; online +1.72% CTR, +1.41% CPM.

---

## 11. UniPolicy: Unified Objective-Specific Policies for Generative Search Advertising

- **arXiv**: [2609.20630v1](https://arxiv.org/pdf/2609.20630v1)
- **Date**: (not specified precisely; recent 2026)
- **Authors**: Kun Yao*, Yuhang Zhou*, Yichi Zhang, Zeliang Tong, Shengri Xue, Haitao Wang, Siyu Lu, Qianlong Xie, Xingxing Wang (*equal)
- **Institution/Company**: Meituan

### Abstract

Search advertising must balance heterogeneous objectives (relevance, click propensity, commercial value). UniPolicy is objective-aware multi-policy alignment: uses objective-specific prefix tokens, sparse MoE-LoRA routing, and objective-specific residual FFNs to hierarchically decouple parameters in shared backbone (differentiated spaces). Constructs pairwise preferences from multi-stage behavioral feedback to supplement exposed-but-unclicked samples and strengthen relative advantage of clicked candidates. At inference, supports parallel business-customizable multi-policy beam search to allocate candidate quotas across objectives under fixed retrieval budget. Offline: balanced improvements across metrics while preserving retrieval quality. 7-day online A/B on real search ads system: +0.71% CTR, +1.58% RPS, +1.32% advertising revenue; stable serving latency.

### Key Innovations

- **Hierarchical Parameter Decoupling**: Objective-specific prefix tokens + sparse MoE-LoRA routing + objective-specific residual FFNs.
- **Preference Construction from Multi-Stage Feedback**: Leverages exposed-but-unclicked samples to enrich relative preference signals.
- **Parallel Multi-Policy Beam Search**: Business-customizable quota allocation across objectives under fixed retrieval budget.
- **Production Impact (7-day A/B)**: +0.71% CTR, +1.58% RPS, +1.32% ad revenue.

---

## 12. Field Matters: A Lightweight LLM-enhanced Method for CTR Prediction (LLaCTR)

- **WWW'26**: [10.1145/3774904.3792387](http://dl.acm.org/doi/10.1145/3774904.3792387)
- **Date**: 2026-04-12
- **Authors**: Yu Cui, Feng Liu, Jiawei Chen, Xingyu Lou, Changwang Zhang, Jun Wang, Yuegang Sun, Xiaohu Yang, Can Wang
- **Institution/Company**: Zhejiang University + Ant Group + OPPO Research Institute

### Abstract

Existing LLM-enhanced CTR methods often require heavy processing of detailed textual descriptions for large-scale instances/entities (high compute). LLaCTR uses field-level enhancement: (1) distills crucial lightweight semantic knowledge from small-scale feature fields via self-supervised field-feature fine-tuning of LLM; (2) leverages this field-level semantic knowledge to enhance both feature representation and feature interactions. Integrated with 6 representative CTR models across 4 datasets; outperforms existing LLM-enhanced methods in effectiveness and efficiency. Code: [https://github.com/istarryn/LLaCTR](https://github.com/istarryn/LLaCTR).

### Key Innovations

- **Field-Level Enhancement Paradigm**: Lightweight vs instance/entity-level heavy text processing.
- **Self-Supervised Field-Feature Fine-Tuning**: Distills compact semantic knowledge from small-scale feature fields.
- **Dual Enhancement**: Improves both feature representation and feature interactions.
- **Efficiency Gains**: Better effectiveness/efficiency than prior LLM-enhanced CTR methods.

---

## 13. Fine-Tuned LLM as a Complementary Predictor Improving Ads System

- **arXiv**: [2605.27856v1](https://arxiv.org/html/2605.27856v1)
- **Date**: 2026-05-27
- **Authors**: Hui Yang et al. (Pinterest)
- **Institution/Company**: Pinterest, Inc.

### Abstract

LLM gains rarely translate to production ads systems. This work proposes fine-tuned open-source LLM as **complementary ancillary predictor** (not ranker) forecasting likely advertisers from user profiles and histories. Approach: (1) structured compilation + prompt template over user profiles and ads-centric histories (past conversions, top advertisers/brands/categories/URLs, demographics); (2) SFT to predict next-advertiser candidates and auxiliary tags (user interests); (3) inject predictions into early retrieval (advertiser-targeted candidate filtering) and late-stage conversion models as features. Production deployment shows consistent offline gains (AUC improvements in late-stage ranking) and measurable online business impact from retrieval-level targeting guided by LLM signals.

### Key Innovations

- **Ancillary Predictor Paradigm**: Uses LLM to predict likely advertisers/interests as signals, not as end-to-end ranker.
- **Structured Prompting + SFT**: Trains on ads-centric user histories (conversions, top entities, demographics).
- **Dual Injection Points**: Feeds LLM signals to both early retrieval (advertiser-targeted filtering) and late-stage conversion models.
- **Production Validation**: Offline AUC gains in late-stage ranking + measurable online business impact.

---

## 14. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs

- **arXiv**: [2603.01590v1](https://arxiv.org/abs/2603.01590v1)
- **Date**: 2026-03-02
- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu
- **Institution/Company**: Xiaohongshu

### Abstract

CTR models rely heavily on item ID embeddings, which struggle in cold-start (no usage). IDProxy uses MLLMs to generate proxy embeddings from rich content signals, enabling CTR prediction for new items without usage data. Proxies are explicitly aligned with existing ID embedding space and optimized end-to-end under CTR objectives with ranking model (seamless integration). Offline experiments + online A/B tests validate effectiveness. Deployed in Content Feed and Display Ads on Xiaohongshu Explore Feed, serving hundreds of millions of users daily.

### Key Innovations

- **MLLM-Generated Proxy Embeddings**: Content-based proxies replace missing ID embeddings for cold-start items.
- **Embedding Space Alignment**: Proxies explicitly aligned to existing ID embedding space.
- **End-to-End Joint Optimization**: Trained with ranking model under CTR objectives for seamless pipeline integration.
- **Large-Scale Production**: Deployed in Content Feed and Display Ads on Xiaohongshu Explore Feed (hundreds of millions of users/day).

---

## 15. HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction

- **arXiv**: [2601.12681](https://ui.adsabs.harvard.edu/abs/2026arXiv260112681H/abstract)
- **Date**: 2026-01-26
- **Authors**: Yunwen Huang, Shiyong Hong, Xijun Xiao, Jinqiu Jin, Xuanyuan Luo, Zhe Wang, Zheng Chai, Shikang Wu, Yuchao Zheng, Jingjian Lin
- **Institution/Company**: (industrial LRMs, unspecified)

### Abstract

Industrial LRMs must jointly model long-range user behavior sequences and heterogeneous non-sequential features under efficiency constraints. Decoupled pipelines (sequence compressor like LONGER → fusion via RankMixer) limit capacity/flexibility. HyFormer is unified hybrid transformer: alternates **Query Decoding** (expands non-sequential features into Global Tokens and performs long-sequence decoding over layer-wise KV representations of behavior sequences) and **Query Boosting** (enhances cross-query/cross-sequence heterogeneous interactions via efficient token mixing). Iterative across layers refines representations. Extensive billion-scale experiments show HyFormer outperforms LONGER+RankMixer under comparable params/FLOPs with better scaling. Large-scale online A/B tests show significant gains over SOTA deployed models.

### Key Innovations

- **Unified Hybrid Transformer**: Tightly integrates long-sequence modeling and feature interaction in single backbone (vs decoupled).
- **Query Decoding**: Global Tokens from non-sequential features + decoding over layer-wise KV representations of behavior sequences.
- **Query Boosting**: Efficient token mixing for cross-query and cross-sequence heterogeneous interactions.
- **Strong Scaling + Production Gains**: Better scaling with params/FLOPs; significant online A/B gains over deployed SOTA.

---

## Methodological Themes (2026)

- **Scaling Laws in Recsys**: LLaTTE, ReST, SparseCTR all demonstrate/validate scaling behavior (predictable power laws, width-before-depth, scaling with sequence length) analogous to LLMs.
- **Two-Stage/Asymmetric Compute**: LLaTTE (async upstream + lightweight online) and ReST (encoder+cross-decoder with shared-prefix serving) tackle latency by offloading heavy sequence work.
- **Generative/LLM-Backed Ranking**: GRAB, OneRanker, GenRec move toward generative paradigms; GenRec shifts feature engineering → context engineering with verbalized inputs.
- **Multimodality + Cold-Start**: IDProxy (MLLM proxies aligned to ID space), LLM-HYPER (LLM as hypernetwork generating CTR weights), DMGIN (MLLM-guided grouping of post-click behaviors).
- **Temporal/Freshness for Live**: TAGR adapts SIDs, intent modeling, and on-policy preference optimization to rapidly changing live-stream context.
- **Context-Centric Unification**: UniCon rethinks history/request as homogeneous context units to improve scaling.
- **Efficiency-Focused Attention**: SparseCTR introduces personalized chunking + RelTemporal + three-branch sparse attention for long-term behaviors.
- **Lightweight LLM Enhancement**: LLaCTR does field-level distillation (not heavy entity/instance text processing).
- **Objective-Aware Multi-Policy**: UniPolicy uses parameter decoupling + multi-policy beam search to balance heterogeneous objectives.
- **Ancillary LLM Signals**: Pinterest’s approach injects LLM-predicted advertiser/interests into retrieval and ranking without making LLM the ranker.

---

## Notes

- All arXiv links above are the primary sources found via web search (2026 publications). Some papers are from WWW'26/AAAI'26 proceedings as indicated.
- This report focuses on AI/LLMs, recommendation, advertising, sequential modeling, CTR, and games-related recent work.
- File saved to: `wiki/synthesis/2026-10-19/arxiv-daily.md`
