---
title: "arXiv Paper Check — 2026-07-19"
type: synthesis
created: 2026-07-19
updated: 2026-07-19
sources: []
tags: [arxiv, ctr, recommendation, survey]
---

# arXiv Paper Check — 2026-07-19

Recent papers from cs.IR and cs.LG, focusing on CTR prediction, recommendation systems, and ranking.

## 1. TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search

- **Authors**: Zhentao Song, Yufeng Gao, Xing Fang et al. (Alibaba/Tmall)
- **arXiv**: [2607.13398](https://arxiv.org/abs/2607.13398)
- **Key contribution**: A scalable Transformer ranking architecture for Tmall search. Proposes Hierarchical Distribution-Calibrated Tokenization (FSR + DCP), a Field-Adaptive Gated Transformer Backbone with per-field QKV projections, Decoupled FiLM Late Fusion, Context-Aware Bias Net, and Error-Aware Progressive Training. Substantial online gains in UCTCVR and GMV on Tmall Search. *(high confidence)*

## 2. Long-History User Transformers for Real-Time Ad Ranking

- **Authors**: Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin et al. (Yandex)
- **arXiv**: [2607.14331](https://arxiv.org/abs/2607.14331)
- **Key contribution**: Decouples long user history encoding from real-time ad inference. A high-capacity offline Transformer asynchronously encodes full cross-surface history into a compact cached representation; a lightweight runtime model combines it with recent events. Recovers 72–80% of full-history runtime quality. +2.77% ranking metric in search ads, +2.1% on Yandex Ad Network, revenue gains of +2.26% and +0.43% without latency increase. *(high confidence)*

## 3. SlimPer: Make Personalization Model Slim and Smart

- **Authors**: Siqi Wang, Xianjie Chen, Shaofeng Deng et al. (Meta/Instagram)
- **arXiv**: [2607.12281](https://arxiv.org/abs/2607.12281)
- **Key contribution**: Reformulates personalized ranking as iterative refinement of a compact user-item knowledge base. O(N) per-layer cost with fixed-size intermediate representation — decouples model depth from history length. Unifies sparse, dense, and sequence features in one backbone. Deployed on Instagram Reels and Feed, enabling modeling of 10k+ fine-grained history events. *(high confidence)*

## 4. Mutable Low-Rank Sketches for Retrain-Free Recommendation

- **Authors**: Hector J. Garcia, Nick Clayton
- **arXiv**: [2607.15242](https://arxiv.org/abs/2607.15242)
- **Key contribution**: Proposes KP-tree mutable sketches that allow on-the-fly embedding recomputation as ratings arrive, eliminating retrain cycles. Achieves 0.810 RMSE on KuaiRec at 1.8% data read vs ALS 0.822 at 100%, with 8x faster batch updates. New users get personalized recommendations in <1ms after first rating. *(single-source, promising)*

## 5. RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation

- **Authors**: Wenhao Deng, Junchen Fu, Hanwen Du et al.
- **arXiv**: [2607.12945](https://arxiv.org/abs/2607.12945)
- **Key contribution**: RL-free recursive reasoning framework that decouples reasoning from prediction. Uses Context Compressor + Recursive Reasoner with deep supervision — reasoning depth can be adjusted at inference without retraining. Outperforms state-of-the-art reasoning-enhanced methods on 4 real-world datasets. Accepted at RecSys 2026. *(high confidence)*

## 6. Learning to Forget: Satiation-Aware Long-Sequence Transducers

- **Authors**: Yipin Dai, Ruocong Tang, Xing Fang et al. (Alibaba/Tmall)
- **arXiv**: [2607.12714](https://arxiv.org/abs/2607.12714)
- **Key contribution**: Addresses post-purchase redundancy in e-commerce recommendations. Proposes SAM (Satiation-Aware Mechanism) with Dual-path Cross-Attention, Adaptive Satiation Gating, and self-supervised Time-to-Next-Purchase auxiliary task. Reduces Post-Purchase Repeat Rate by >60% in online A/B tests. SIGIR '26 Industry Track. *(high confidence)*

## 7. Cheaper is Better: A Discount-Aware Network for CVR Prediction

- **Authors**: Ruocong Tang, Yang Huang, Xing Fang et al. (Alibaba/Tmall)
- **arXiv**: [2607.12578](https://arxiv.org/abs/2607.12578)
- **Key contribution**: DANet models discount rate effects on conversion rate using Fourier transform frequency analysis, distribution de-bias module, and supervised regression auxiliary task. +1.61% offline AUC, +3.63% pCVR and +2.23% GMV online. Deployed on Tmall. SIGIR '26 Industry Track. *(high confidence)*

## 8. Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning

- **Authors**: Dingsu Wang, Filip Ryzner, Kelly He et al. (Pinterest)
- **arXiv**: [2607.14192](https://arxiv.org/abs/2607.14192)
- **Key contribution**: Model-agnostic framework for optimizing long-term user retention. Formulates downstream reward learning with offline screening to identify session-level behaviors predictive of retention. Deployed across Pinterest Homefeed, Related Pins, Search, and Notifications. RecSys 2026. *(high confidence)*

## 9. Deep-learning Causal Retrieval Optimization for Efficient e-commerce Distribution in Pinterest

- **Authors**: Junpeng Hou, XianXing Zhang, Sai Xiao et al. (Pinterest)
- **arXiv**: [2607.14161](https://arxiv.org/abs/2607.14161)
- **Key contribution**: Causal decision framework for triggering shopping candidate generators in early retrieval. Deep multi-task model jointly predicts outcomes and uplift (doubly-robust). Cuts shopping triggers by up to 85% while holding key shopping sessions neutral, improving total sessions (+0.26%) and Pin saves (+1.10%). KDD '26. *(high confidence)*

## 10. CoSimRec: Measuring Coordinated-Content Penetration in Recommender Feedback Loops

- **Authors**: Nan Li, Jiahong Shao, Jiuyang Lyu
- **arXiv**: [2607.15114](https://arxiv.org/abs/2607.15114)
- **Key contribution**: Offline agent-based evaluation framework for measuring how coordinated activity (bot accounts) penetrates recommender systems. Introduces Algorithmic Penetration Rate (APR) metric family. Shows popularity-based and feedback-sensitive ranking produce significant positive APR-Lift across datasets. *(high confidence)*

---

## Themes

- **Transformerization of CTR/ranking**: TMallGS, Long-History Transformers, and SlimPer all shift from DLRM-style architectures to Transformer backbones, with innovations to handle heterogeneous features and latency constraints.
- **Decoupling compute from history length**: Both Long-History Transformers (Yandex) and SlimPer (Meta) cache user representations so that deep modeling does not increase per-request latency.
- **Causal and long-term optimization**: Pinterest's papers on downstream rewards and causal retrieval reflect a shift from short-term CTR to retention and uplift.
- **E-commerce-specific signals**: SAM (post-purchase satiation) and DANet (discount awareness) show the industry is moving beyond generic user modeling to domain-specific behavioral modeling.
