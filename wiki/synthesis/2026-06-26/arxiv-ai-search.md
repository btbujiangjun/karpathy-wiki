---
title: "arXiv AI Research Scan — June 26, 2026"
type: synthesis
created: 2026-06-26
updated: 2026-06-26
tags: [arxiv, survey, llm, recommendation, ctr, advertising, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Research Scan — June 26, 2026

Scan of recent arXiv submissions (Jun 23–26, 2026) across cs.LG, cs.CL, cs.IR, cs.AI. Papers selected for relevance to LLMs, recommendation systems, advertising/CTR, sequential modeling, games/RL, and time-series forecasting.

---

## Large Language Models

### 1. RiVER: Reinforcement Learning without Ground-Truth Solutions can Improve LLMs
- **Authors**: Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang, et al.
- **Affiliation**: Microsoft / academia
- **Link**: https://arxiv.org/abs/2606.27369
- **Key Innovation**: Ranking-induced VERifiable framework (RiVER) trains LLMs on score-based optimization tasks without ground-truth answers. Uses deterministic execution feedback as continuous reward. Introduces calibrated reward shaping to handle *scale dominance* and *frequency dominance*. Trained on AtCoder Heuristic Contest tasks, RiVER improves Qwen3-8B by 8.9% and GLM-Z1-9B by 9.4% in ALE rating, and transfers to exact-solution benchmarks (LiveCodeBench +2.4%, USACO +3.5%).
- **Tags**: `llm-training`, `rl`, `code-generation`

### 2. GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning
- **Authors**: Ting Zhou, Zhenqing Ling, Yiyang Zhao, Ying Shen, Daoyuan Chen
- **Affiliation**: Academia
- **Link**: https://arxiv.org/abs/2606.26917
- **Key Innovation**: Identifies *directional inconsistency* failure in online LLM RL — rollouts with divergent representation-space preference directions cause high-variance updates. GEOALIGN detects directionally inconsistent rollouts via angular deviation from batch consensus and rectifies them. Forward-pass only, negligible overhead. Outperforms PF-PPO, PAR, PODS, Seed-GRPO. **ICML 2026**.
- **Tags**: `llm-alignment`, `rl`, `icml-2026`

### 3. Nemotron-TwoTower: Diffusion Language Modeling with Pretrained Autoregressive Context
- **Authors**: Fitsum Reda, John Kamalu, Roger Waleffe, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro
- **Affiliation**: NVIDIA
- **Link**: https://arxiv.org/abs/2606.26493
- **Key Innovation**: Decouples context representation and iterative denoising into two towers — frozen AR context tower + trainable diffusion denoiser with bidirectional block attention. Built on Nemotron-3-Nano-30B-A3B (open-weight 30B hybrid Mamba-Transformer MoE). Retains 98.7% of AR quality while offering 2.42× wall-clock generation throughput. Code/weights released.
- **Tags**: `diffusion-lm`, `llm-architecture`, `nvidia`

### 4. Erase-then-Delta Attention: Decoupling Erase and Write Addresses in Delta-Rule Linear Attention
- **Authors**: Xiao Li, Chengruidong Zhang, Hao Luo, et al. (Alibaba)
- **Affiliation**: Alibaba
- **Link**: https://arxiv.org/abs/2606.26560
- **Key Innovation**: Proposes EDA, a memory update rule that decouples *where to erase* from *where to write* in linear attention. First applies targeted erase along a learned direction, then delta-style corrective write. Pretraining experiments at 2.5B dense and 25B-A2.8B MoE show best results; gains persist through 80B-token long-context midtraining up to 128k context.
- **Tags**: `linear-attention`, `efficient-transformers`, `long-context`

### 5. CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs
- **Authors**: Shigeng Wang, Chao Li, Yangyuxuan Kang, Jiawei Fan, Anbang Yao
- **Affiliation**: Intel / academia
- **Link**: https://arxiv.org/abs/2606.26650
- **Key Innovation**: Ternary quantization for LLMs achieving cost-efficient accuracy. **ICML 2026 Oral**.
- **Tags**: `llm-compression`, `quantization`, `icml-2026`

### 6. Reasoning Quality Emerges Early: Data Curation for Reasoning Models
- **Authors**: Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari, Carlos Morato, Baharan Mirzasoleiman
- **Affiliation**: Academia
- **Link**: https://arxiv.org/abs/2606.26797
- **Key Innovation**: Studies when reasoning quality emerges during training and proposes data curation strategies for reasoning models. **ICML 2026**.
- **Tags**: `reasoning`, `data-curation`, `icml-2026`

### 7. Structure Before Collapse: Transient Semantic Geometry in Next-Token Prediction
- **Authors**: Yize Zhao, Isabel Papadimitriou, Christos Thrampoulidis
- **Affiliation**: Academia (UC Berkeley / UBC)
- **Link**: https://arxiv.org/abs/2606.26749
- **Key Innovation**: Studies the transient semantic geometry that emerges in next-token prediction before the representation space collapses. Links to linguistic structure.
- **Tags**: `interpretability`, `representation-learning`

### 8. Information-Aware KV Cache Compression for Long Reasoning
- **Authors**: Jushi Kai, Zhuiri Xiao, Alexandra Birch, Zhouhan Lin
- **Affiliation**: Academia
- **Link**: https://arxiv.org/abs/2606.26875
- **Key Innovation**: Information-theoretic KV cache compression for long-context reasoning tasks.
- **Tags**: `kv-cache`, `inference-efficiency`, `long-context`

---

## Recommendation Systems

### 9. NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems
- **Authors**: Shaohua Liu, Liang Fang, Yilong Sun, et al. (Alibaba)
- **Affiliation**: Alibaba
- **Link**: https://arxiv.org/abs/2606.27243
- **Key Innovation**: LLM-agent-driven framework for evolving recommender architectures. Uses *architecture gradient* (SGD-inspired update signal) + verification cascade (structure→executability→offline→online). L1–L4 task-level control. Deployed in industrial advertising: 54.5%/60.0% pass rate on ScaleUp/Literature-to-Production tasks, 13× reduction in human time. Online: +1.25%–2.02% GMV on pCVR, 37–67% bias reduction.
- **Tags**: `recommender-systems`, `llm-agent`, `automl`

### 10. AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors**: Changxin Lao, Fei Pan, Guozhuang Ma, et al. (Kuaishou)
- **Affiliation**: Kuaishou
- **Link**: https://arxiv.org/abs/2606.26859
- **Key Innovation**: Multi-agent system (Brainstorm → Developing → Evaluation → SGPO Harness Evolution) that autonomously generates, implements, evaluates, and learns from recommendation experiments in a closed loop. Self-improving via semantic-gradient updates.
- **Tags**: `recommender-systems`, `multi-agent`, `kuaishou`

### 11. UniFormer: Efficient and Unified Model-Centric Scaling for Industrial Recommendation
- **Authors**: Bo Chen, Jinlong Jiao, Tijian Hu, et al. (Kuaishou)
- **Affiliation**: Kuaishou
- **Link**: https://arxiv.org/abs/2606.27058
- **Key Innovation**: Decomposes modeling space into feature and task spaces. Semantic-based tokenization enables request-level inference acceleration. Multi-sequence cross-attention for heterogeneous behavior patterns. Multi-view FFNs for flexible parameter scaling. Online A/B in Kuaishou: +0.101%/+0.260% Stay Time, +0.729%/+1.113% Watch Time.
- **Tags**: `recommender-systems`, `scaling`, `kuaishou`

### 12. TokenMinds: Pretrained User Tokens and Embeddings for User Understanding in Large Recommender Systems
- **Authors**: Qingyun Liu, Bo Yan, Yang Liu, et al. (Google, YouTube)
- **Affiliation**: Google / YouTube
- **Link**: https://arxiv.org/abs/2606.25147
- **Key Innovation**: Extends PLUM framework to user modeling — generates both discrete SID-based user tokens and dense user embeddings via encoder-decoder from pretrained LLMs. Shared SID vocabulary enables cross-scenario modeling (long-form + short-form video). Deployed on YouTube full user traffic (billions of users).
- **Tags**: `recommender-systems`, `user-modeling`, `youtube`, `google`

### 13. Recommendation as Generation: Unifying Personalized Video Generation and Recommendation at Industrial Scale
- **Authors**: Yanhua Cheng, Bo Wang, Haotian Zhang, et al. (Kuaishou)
- **Affiliation**: Kuaishou
- **Link**: https://arxiv.org/abs/2606.25496
- **Key Innovation**: RaG — generates personalized videos on demand via shared Semantic IDs (SIDs) that disentangle content semantics from creative style. Video Generation Agents (VGAs) for hierarchical planning/refinement. Cross-domain reward learning. Online A/B: +1.87% ad revenue on 400M DAU platform. Closed-loop generative system.
- **Tags**: `recommender-systems`, `video-generation`, `kuaishou`, `generative-ai`

---

## Sequential / Session-Based Recommendation

### 14. TRUST: Item-Calibrated Interval Evidence for Temporal Session-Based Recommendation
- **Authors**: Linjiang Guo, Nitin Bisht, Shiqing Wu, Yifan Yin, Guandong Xu
- **Affiliation**: Academia
- **Link**: https://arxiv.org/abs/2606.27214
- **Key Innovation**: Challenges the assumption that time intervals carry uniform signals across items. Proposes item-calibrated interval scoring using empirical interval distribution per item. Model-agnostic plug-in that improves existing temporal session recommenders.
- **Tags**: `session-based-recommendation`, `temporal-modeling`

### 15. S2-CAR: Segmentation-Supervised Complexity-Adaptive Recommendation
- **Authors**: Linjiang Guo, Nitin Bisht, Shiqing Wu, Xianzhi Wang, Guandong Xu
- **Affiliation**: Academia
- **Link**: https://arxiv.org/abs/2606.25415
- **Key Innovation**: Models user intent as continuous latent energy state via Context-Aware Soft Temporal Point Process (Soft-TPP). Segments behavior by natural decay of latent-state energy rather than fixed intervals. Segment-Count-Adaptive Multi-Intent Extraction. Outperforms 13 baselines across movie, e-commerce, and gaming datasets.
- **Tags**: `sequential-recommendation`, `user-intent`, `temporal-point-process`

### 16. From Clicks to Intent: Cross-Platform Session Embeddings with LLM-Distilled Taxonomy for Financial Services Recommendations
- **Authors**: Dianjing Fan, Yao Li, Kyaw Hpone Myint, et al. (JPMorgan)
- **Affiliation**: JPMorgan Chase
- **Link**: https://arxiv.org/abs/2606.26277
- **Key Innovation**: Self-supervised Transformer encodes multi-modal clickstreams into session embeddings; LLM-based taxonomy generation and distillation pipeline produces interpretable intent labels. Deployed in financial services: macro Recall@1 +1.88%, Log Loss -13.38% on mobile homepage ranking.
- **Tags**: `sequential-modeling`, `financial-services`, `session-embeddings`

---

## Advertising / CTR / Attribution

### 17. AIGP: An LLM-Based Framework for Long-Term Value Alignment in E-Commerce Pricing
- **Authors**: Chennan Ma, Yanning Zhang, Siqi Hong, et al. (Alibaba)
- **Affiliation**: Alibaba (Tao Factory)
- **Link**: https://arxiv.org/abs/2606.26787
- **Key Innovation**: LLM-based dynamic pricing with Long-Term Value Estimator (LTVE) trained via offline RL. DPO for policy alignment. Online A/B: +13.21% GMV, +7.59% ROI, +8.20% milestone achievement over 14 days. **KDD 2026 Oral**.
- **Tags**: `e-commerce`, `pricing`, `llm`, `kdd-2026`

### 18. Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising
- **Authors**: Donghui Li, Bowen Yuan, Zili Yang, Qinxin Chen, Lijing Song
- **Affiliation**: TikTok
- **Link**: https://arxiv.org/abs/2606.26690
- **Key Innovation**: Experiment-calibrated attribution correction framework using incrementality experiments as causal anchors. Converts sparse lift measurements into daily correction estimates. Deployed across global TikTok markets, reducing cannibalization rate by ~15 percentage points. **ADKDD 2026**.
- **Tags**: `advertising`, `attribution`, `tiktok`

### 19. AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search
- **Authors**: Md Omar Faruk Rokon, Shasvat Desai, Hong Yao, Kuang-chih Lee
- **Affiliation**: (E-commerce / Search advertising)
- **Link**: https://arxiv.org/abs/2606.25871
- **Key Innovation**: Calibrated model cascade routing queries through progressively larger fine-tuned classifiers. Fine-tuning adds 20 accuracy points; cascading halves cost. Per-class isotonic calibration. Processed 150M+ annotations in production. **SIGIR 2026 E-commerce Workshop**.
- **Tags**: `sponsored-search`, `relevance-annotation`, `cascading`

### 20. Cross-Head Attention Uplift Network with Inverse Propensity Score under Unobserved Confounding
- **Authors**: Haoran Zhang, Chuanpu Li, Yuxin Fu, et al. (Alibaba)
- **Affiliation**: Alibaba
- **Link**: https://arxiv.org/abs/2606.27114
- **Key Innovation**: CHAUN uplift model with cross-head attention for ITE estimation. Robust Adversarial IPS (RA-IPS) for unobserved confounding. Up to 25.6% QINI improvement on CRITEO-UPLIFT/LAZADA. Production e-commerce validation.
- **Tags**: `uplift-modeling`, `causal-inference`, `e-commerce`

### 21. Unified Multi-Task Relevance Modeling for E-Commerce (SIGIR 2026 E-Commerce Workshop)
- **Authors**: Md Omar Faruk Rokon et al.
- **Link**: https://arxiv.org/abs/2606.23919
- **Key Innovation**: Compares task routing architectures across LLMs and cross-encoders for e-commerce relevance.
- **Tags**: `e-commerce`, `multi-task`, `relevance`

### 22. INSPIRE: Intent-aware Neural Sponsored Product Retrieval for E-commerce
- **Authors**: Shasvat Desai et al.
- **Link**: https://arxiv.org/abs/2606.23889
- **Key Innovation**: Intent-aware retrieval for sponsored products. **SIGIR 2026 E-commerce Workshop**.
- **Tags**: `sponsored-search`, `e-commerce`

### 23. GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices
- **Authors**: Ashutosh Sharma
- **Link**: https://arxiv.org/abs/2606.26441
- **Key Innovation**: GPU-accelerated sparse retrieval with parallel inverted indices.
- **Tags**: `retrieval`, `gpu`, `sparse-retrieval`

---

## CTR Prediction (recent, from web search)

### 24. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: LinkedIn
- **Link**: https://arxiv.org/abs/2602.11410
- **Key Innovation**: Decoder-only transformer for ads CTR at LinkedIn. Context-conditioned decoding, self-gated attention, timestamp-based RoPE, session masking. Online A/B: +11.04% CTR lift vs LiRank (DCNv2 + sequential encoders). Deployed on LinkedIn homefeed sponsored updates.
- **Tags**: `ctr-prediction`, `transformer`, `linkedin`

### 25. Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, et al. (Renmin Univ / ByteDance / Meituan)
- **Link**: https://arxiv.org/abs/2606.04944
- **Key Innovation**: Dual-stream MLP architecture for CTR. Published in ACM TKDD 2026.
- **Tags**: `ctr-prediction`, `mlp`

### 26. EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling
- **Authors**: Taobao / Alibaba
- **Link**: https://arxiv.org/abs/2602.10811
- **Key Innovation**: Efficiently Scalable Transformer (EST) with power-law scaling relationship. Lightweight Cross-Attention (LCA) prunes redundant self-interactions. Deployed on Taobao display advertising: +3.27% RPM, +1.22% CTR.
- **Tags**: `ctr-prediction`, `scaling-laws`, `taobao`

### 27. GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm
- **Authors**: Baidu
- **Link**: https://arxiv.org/abs/2602.01865
- **Key Innovation**: Generative Ranking for Ads at Baidu (GRAB) — end-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA). Online: +3.05% revenue, +3.49% CTR. Linear scaling with longer sequences.
- **Tags**: `ctr-prediction`, `baidu`, `generative-ctr`

### 28. LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks
- **Authors**: (E-commerce, US)
- **Link**: https://arxiv.org/abs/2604.12096
- **Key Innovation**: LLM as hypernetwork to generate CTR estimator weights in training-free manner. Few-shot CoT over multimodal ad content. NDCG@10 +55.9% over cold-start baselines. Deployed on top US e-commerce platform.
- **Tags**: `ctr-prediction`, `cold-start`, `llm`, `hypernetwork`

---

## Games / Reinforcement Learning

### 29. Superhuman AI for Generals.io Using Self-Play Reinforcement Learning
- **Authors**: (JAX-native simulator)
- **Link**: https://arxiv.org/abs/2606.23348
- **Key Innovation**: Superhuman agent for Generals.io (RTS game) using policy-gradient from scratch. JAX-native simulator achieves 10,000× speedup. ViT policy trained with sparse win/loss reward, top-advantage sample filtering, EMA. Reaches #1 on 1v1 leaderboard (5000+ humans), beats top two humans 199-70.
- **Tags**: `games`, `rl`, `self-play`, `generals.io`

### 30. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: (Academia)
- **Link**: https://arxiv.org/abs/2605.00347
- **Key Innovation**: RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Adapted PPO with lightweight turn-level critic. Pretrained VLMs provide strong action priors. 3× average game progress over frontier models. Cross-game generalization.
- **Tags**: `vlm`, `games`, `rl`, `decision-making`

### 31. IRumAI: Reinforcement Learning for Indian Rummy
- **Authors**: Vignesh Mohan (EURECOM)
- **Link**: https://arxiv.org/abs/2606.21975
- **Key Innovation**: First RL agent for Indian Rummy. PPO + meld-aware observation encoding + deadwood-driven reward shaping + dual-branch conv architecture. 53.9% win rate vs strongest search-based opponent. 0.33 ms/action (7,000× faster than heuristic).
- **Tags**: `games`, `rl`, `rummy`, `card-games`

### 32. From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning
- **Authors**: Chao Chen, Chengzu Li, et al.
- **Link**: https://arxiv.org/abs/2606.17682
- **Key Innovation**: LLM-as-Environment-Engineer framework — current policy model analyzes failures and proposes next-stage training environment modifications. MAPF-FrozenLake testbed. Qwen3-4B outperforms GPT/Gemini baselines. Current RL checkpoint serves as better environment engineer than base model.
- **Tags**: `llm`, `rl`, `curriculum-learning`, `environment-design`

---

## Time-Series / Forecasting

### 33. How Good Can Linear Models Be for Time-Series Forecasting?
- **Authors**: Lang Huang, Jinglue Xu, Luke Darlow
- **Affiliation**: Academia
- **Link**: https://arxiv.org/abs/2606.27282
- **Key Innovation**: Challenges the assumption that larger architectures (Transformers, foundation models) are needed. Ridge regression with carefully tuned preprocessing (context length, local normalization, regularization, augmentation) beats Transformer/MLP/CNN baselines on 6/8 benchmarks. Optimal lookback is series-specific with non-monotonic power-law exponents.
- **Tags**: `time-series`, `forecasting`, `linear-models`

### 34. Speaking Numbers to LLMs: Multi-Wavelet Number Embeddings for Time Series Forecasting
- **Authors**: Defu Cao, Zijie Lei, Muyan Weng, Jiao Sun, Yan Liu
- **Affiliation**: Academia (USC)
- **Link**: https://arxiv.org/abs/2606.26487
- **Key Innovation**: Multi-wavelet number embeddings for LLM-based time series forecasting. **IJCAI 2026**.
- **Tags**: `time-series`, `llm`, `embeddings`, `ijcai-2026`

---

## Information Retrieval / Ranking

### 35. Extreme Meta-Classification for Large-Scale Zero-Shot Retrieval
- **Authors**: Sachin Yadav, Deepak Saini, et al. (Microsoft)
- **Link**: https://arxiv.org/abs/2606.25237
- **Key Innovation**: Extreme multi-label classification for zero-shot retrieval at scale. **KDD 2024**.
- **Tags**: `zero-shot-retrieval`, `xmc`, `kdd-2024`

### 36. Adaptive Re-Ranking
- **Authors**: Ata Cinar Genc, Emir Kaan Korukluoglu, James Allan (UMass Amherst)
- **Link**: https://arxiv.org/abs/2606.25249
- **Key Innovation**: Adaptive re-ranking approach for search.
- **Tags**: `re-ranking`, `information-retrieval`

---

## Summary of Trends

| Trend | Papers | Key Players |
|-------|--------|-------------|
| LLM agents for recommender system iteration | NOVA, AgentX | Alibaba, Kuaishou |
| Diffusion / non-autoregressive LMs | Nemotron-TwoTower | NVIDIA |
| RL for LLM alignment w/o ground truth | RiVER, GEOALIGN | Microsoft, academia |
| Linear attention improvements | Erase-then-Delta Attention | Alibaba |
| Generative recommendation (video+rec) | Recommendation as Generation | Kuaishou |
| LLM-powered ad/CTR models | AIGP, CADET, GRAB, LLM-HYPER | Linkedin, Baidu, Alibaba, US e-comm |
| Causal inference in advertising | CHAUN/RA-IPS, Cannibalization-Corrected | Alibaba, TikTok |
| Session/sequential modeling | TRUST, S2-CAR, JPMorgan sessions | Academia, JPMorgan |
| Game AI with RL | Generals.io, Odysseus, IRumAI | Academia, EURECOM |
| Time-series with simple/linear models | Ridge for Forecasting | Academia |
