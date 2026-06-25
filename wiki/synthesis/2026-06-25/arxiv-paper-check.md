---
title: "arXiv Paper Check — AI & CTR (June 25, 2026)"
type: synthesis
created: 2026-06-25
updated: 2026-06-25
sources: [arxiv.org]
tags: [arxiv, ai, ctr, recommendation, retrieval, advertising]
---

# arXiv Paper Check — AI & CTR (June 25, 2026)

> Scanned cs.IR, cs.AI, cs.LG new submissions from the last 24 hours.

## CTR & Advertising

### 1. Recommendation as Generation (RaG)
- **Authors**: Yanhua Cheng, Bo Wang, Haotian Zhang, Xinyuan Gao, Zhihui Yin, Ben Xue, Yongzhi Li, Jieting Xue, Ye Ma, Minquan Wang, Jiahui Li, Tianyu Xu, Zhiqiang Liu, Xiao Lin, Shiyang Wen, Changcheng Li, Liu Liu, Quan Chen, Peng Jiang, Kun Gai (Kuaishou)
- **arXiv**: 2606.25496
- **Key contribution**: Unifies generative recommendation and video generation through shared Semantic IDs (SIDs). Video Generation Agents (VGAs) create personalized videos on demand. Deployed on 400M+ DAU platform, online A/B test shows **1.87% ad revenue improvement** over strong GRM baseline.
- **Tags**: #generative-recommendation #video-generation #SID #advertising

### 2. TokenMinds: Pretrained User Tokens and Embeddings for Large Recommender Systems
- **Authors**: Qingyun Liu, Bo Yan, Yang Liu, Yuji Roh, Ekansh Sharma, Likang Yin, Emma Olowo, Min-hsuan Tsai, Yuxuan Li, Diego Uribe, Saksham Aggarwal, Siqi Wu, Yuan Hao, Vikas Kedigehalli, Lukasz Heldt, Lichan Hong, Li Wei, Xinyang Yi (Google/YouTube)
- **arXiv**: 2606.25147
- **Key contribution**: Extends PLUM framework to user modeling, generating both discrete SID-based user tokens and dense user embeddings via encoder-decoder LLM architecture. Validated on full YouTube traffic (billions of users). Unifies long-form and short-form video behaviors into a single model.
- **Tags**: #user-modeling #SID #recommender-systems #YouTube #LLM

### 3. Extreme Meta-Classification for Large-Scale Zero-Shot Retrieval (IRENE)
- **Authors**: Sachin Yadav, Deepak Saini, Anirudh Buvanesh, Bhawna Paliwal, Kunal Dahiya, Siddarth Asokan, Yashoteja Prabhu, Jian Jiao, Manik Varma
- **arXiv**: 2606.25237 (KDD 2024)
- **Key contribution**: IRENE algorithm synthesizes classifiers on-the-fly for novel zero-shot items. Improves zero-shot retrieval Recall@10 by up to **15% points**. Online A/B test in a major search engine ad retrieval task shows **4.2% CTR improvement**.
- **Tags**: #zero-shot-retrieval #extreme-classification #CTR #ad-retrieval

### 4. DynamicPO: Dynamic Preference Optimization for Recommendation
- **Authors**: Xingyu Hu, Kai Zhang, Jiancan Wu, Shuli Wang, Chi Wang, Wenshuai Chen, Yinhua Zhu, Haitao Wang, Xingxing Wang, Xiang Wang
- **arXiv**: 2605.00327 (DASFAA 2026 **Best Paper**)
- **Key contribution**: Identifies "preference optimization collapse" where more negatives degrade performance. Proposes DynamicPO with Dynamic Boundary Negative Selection and Dual-Margin Dynamic beta Adjustment. Prevents optimization collapse in LLM-based recommendation.
- **Tags**: #DPO #recommendation #preference-optimization #LLM

### 5. DADF: Distribution-Aware Debiasing for Watch-Time Regression
- **Authors**: Yiqing Yang, Xinlong Zhao, Zhao Liu, Xiao Lv, Ruiming Tang, Han Li, Kun Gai
- **arXiv**: 2605.17863
- **Key contribution**: Second-stage multiplicative residual correction for watch-time prediction. Combines dynamic distribution-aware transformation, debias-factor-aware module, and multi-label-aware module. Online lift of **0.649% avg time spent** and **0.656% total app time** per device.
- **Tags**: #watch-time #debiasing #short-video #regression

### 6. AutoRelAnnotator: Calibrated Model Cascades for Relevance Evaluation
- **Authors**: Md Omar Faruk Rokon, Shasvat Desai, Hong Yao, Kuang-chih Lee
- **arXiv**: 2606.25871 (SIGIR 2026 E-commerce Workshop)
- **Key contribution**: Calibrated model cascade routing queries through progressively larger fine-tuned classifiers. Fine-tuning contributes 20 accuracy points; cascading halves compute cost. Processed **150M+ annotations** in production across 6 offline use cases.
- **Tags**: #relevance-annotation #model-cascades #search #advertising

### 7. S2-CAR: Segmentation-Supervised Complexity-Adaptive Recommendation
- **Authors**: Linjiang Guo, Nitin Bisht, Shiqing Wu, Xianzhi Wang, Guandong Xu
- **arXiv**: 2606.25415
- **Key contribution**: Models user intent as continuous latent energy state using Context-Aware Soft Temporal Point Process (Soft-TPP) for intent segmentation. Outperforms 13 baselines across movie, e-commerce, and gaming domains.
- **Tags**: #sequential-recommendation #intent-segmentation #TPP

### 8. Adaptive Re-Ranking
- **Authors**: Ata Cinar Genc, Emir Kaan Korukluoglu, James Allan
- **arXiv**: 2606.25249
- **Key contribution**: Utility-based labeling framework for cost-aware query routing. Achieves **1.15-53x lower latency** vs BGE while maintaining competitive nDCG@10 (-17.5% to +4.0%).
- **Tags**: #re-ranking #cost-aware #latency

## AI / LLM

### 9. Weight-Space Geometry of Offline Reasoning Training
- **Authors**: Aleksandr Nikolich, Igor Kiselev, Vladimir Platonov, Karina Romanova (ICML 2026 Workshop)
- **arXiv**: 2606.23740 (cs.LG, cross cs.AI)
- **Key contribution**: Analyzes 6 offline reasoning methods (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on identical math rollouts. SFT/RFT/RIFT have nearly colinear weight deltas (cosine >= 0.97). DPO reaches highest accuracy (93.5% GSM8K, 30.0% AIME26) but sits in a near-orthogonal subspace with mode-connectivity barrier.
- **Tags**: #reasoning #DPO #GRPO #weight-space #offline-RL

### 10. The Hitchhiker's Guide to Agentic AI
- **Authors**: Haggai Roitman
- **arXiv**: 2606.24937 (cs.AI cross-list)
- **Key contribution**: Comprehensive practitioner's reference covering LLM substrate, alignment (RLHF, PPO, DPO, GRPO), agentic AI (RAG, memory, MCP, A2A protocol, multi-agent architectures), and production deployment.
- **Tags**: #agentic-AI #book #survey #MCP #A2A

### 11. Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions
- **Authors**: Long Chen, Ryan Razkenari, Yuxuan Zhou, Yuan Tian, Rahul Ghosh, Venkatesh Pappakrishnan, Disha Ahuja, Vidya Sagar Ravipati (ACL 2026 GEM Workshop)
- **arXiv**: 2606.25656
- **Key contribution**: Compares 9 standardized RAG scenarios from simple retrieval to GraphRAG and Agentic RAG. Novel context engineering reduces token usage by **19%-53%**. Identifies "retrieval-generation gap" where expanded retrieval doesn't proportionally improve generation quality.
- **Tags**: #RAG #GraphRAG #AgenticRAG #context-engineering

### 12. Catastrophic Compositional Generation: Why Vanilla Diffusion Models Fail to Extrapolate
- **Authors**: Duncan Soiffer, Chandler Squires, Yuan Guan, Jason Hartford, Pradeep Ravikumar
- **arXiv**: 2606.23920 (cs.LG)
- **Key contribution**: Argues compositional generation is infeasible for vanilla conditional diffusion models in certain settings. Score estimation error has catastrophic effect on OOD target distributions. Highlights need for different approach.
- **Tags**: #diffusion-models #compositional-generation #OOD

### 13. BitNet Text Embeddings (BITEMBED)
- **Authors**: Zhen Li, Xin Huang, Liang Wang, Nan Yang, Ting Song, Yan Xia, Xun Wu, Shaohan Huang, Huishuai Zhang, Furu Wei, Dongyan Zhao
- **arXiv**: 2606.25674 (cs.CL cross-list)
- **Key contribution**: Converts pretrained LLM backbones into BitNet-style embedding encoders with ternary weights, quantized activations. Comparable to full-precision teacher embedders on MMTEB. Flexible multi-precision storage.
- **Tags**: #embeddings #quantization #BitNet #retrieval

### 14. Nexus Sampling: Streaming KV-Cache Eviction Under Fixed Budgets
- **Authors**: Duc Duong, Hoang Anh Duy Le, Jianwen Xie, Anshumali Shrivastava, Zhaozhuo Xu
- **arXiv**: 2606.23961 (cs.LG)
- **Key contribution**: Training-free eviction method using Nexus scoring (iterative walk over direct attention) with weighted reservoir sampling. At 80% eviction, matches dense attention within 1% on LongBench. Dominates deterministic top-K in long-run survival of subtly important tokens.
- **Tags**: #KV-cache #inference-efficiency #attention

## Summary

| # | Paper | Venue | Relevance | Impact |
|---|-------|-------|-----------|--------|
| 1 | RaG (Kuaishou) | arXiv | CTR/Advertising | **1.87% ad revenue lift**, 400M DAU |
| 2 | TokenMinds (YouTube) | arXiv | CTR/RecSys | Billions of users, SID user tokens |
| 3 | IRENE | KDD 2024 | CTR/Retrieval | **4.2% CTR lift**, zero-shot retrieval |
| 4 | DynamicPO | DASFAA 2026 Best Paper | RecSys/LLM | Preference optimization collapse |
| 5 | DADF | arXiv | Watch-time/Debiasing | 0.65% time-spent lift |
| 6 | AutoRelAnnotator | SIGIR 2026 Workshop | Search/Ads | 150M+ annotations |
| 7 | S2-CAR | arXiv | Sequential Rec | Energy-based intent segmentation |
| 8 | Adaptive Re-Ranking | arXiv | IR Efficiency | 1.15-53x latency reduction |
| 9 | Weight-Space Geometry | ICML 2026 Workshop | LLM Reasoning | DPO near-orthogonal subspace |
| 10 | Hitchhiker's Guide to Agentic AI | arXiv | Agentic AI | Comprehensive reference |
| 11 | Is GraphRAG Needed? | ACL 2026 Workshop | RAG | 19-53% token reduction |
| 12 | Catastrophic Compositional Gen | arXiv | Diffusion | OOD extrapolation limits |
| 13 | BITEMBED | arXiv | Embeddings | Ternary-weight text embeddings |
| 14 | Nexus Sampling | arXiv | Inference | KV-cache at 80% eviction |
