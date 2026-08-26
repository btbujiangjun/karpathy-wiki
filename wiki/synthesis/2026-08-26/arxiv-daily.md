---
title: "arXiv Daily: AI/LLM/Rec/Ad/CTR/Games"
type: synthesis
created: 2026-08-26
updated: 2026-08-26
tags: [arxiv, daily, recommendation, CTR, LLM, advertising, sequential-modeling, game-AI]
---

# arXiv Daily Report — 2026-08-26

Papers from arXiv covering LLMs, recommendation systems, CTR prediction, advertising/auto-bidding, sequential modeling, multimodal embeddings, and game AI. Focus on recent submissions (August 2026).

---

## 1. LLM × Recommendation

### UniSpecRec: Rethinking Semantic Alignment in LLM-Enhanced Collaborative Filtering — A Spectral Decoupling Approach
- **Authors:** Yedong Jin, Shaowen Peng, Tsunenori Mine, Shoko Wakamiya, Eiji Aramaki
- **Institution:** Nara Institute of Science and Technology
- **Key Innovation:** Demonstrates that LLM semantic alignment with CF embeddings degrades non-principal semantic information. Proposes signal-specific spectral filtering (UniSpecRec) that preserves collaborative and semantic representations in separate spaces without cross-space alignment, eliminating trainable parameters for alignment.
- **Link:** [arXiv:2608.24363](https://arxiv.org/abs/2608.24363)

### A Dual-Expert Strategy Integrating LLMs to Mitigate Negative Transfer in Cross-Domain Sequential Recommendation
- **Authors:** Hyeongjun Yun, Kihyuk Song, Jaegul Choo, Chung Park
- **Institution:** Korea University
- **Key Innovation:** DuELRec uses a domain-gated dual-expert framework: single-domain expert restricts attention within domain, cross-domain expert allows cross-domain attention. A gating mechanism reduces negative transfer. Dual-sampling token-to-item contrastive learning captures item-level collaborative signals.
- **Link:** [arXiv:2608.23131](https://arxiv.org/abs/2608.23131) (Accepted CIKM 2026)

### The Disconnect Between Better Descriptive Reasoning Trace Quality and Recommendation Effectiveness
- **Authors:** Gustavo Penha, Juan Elenter, Claudia Hauff, Hugues Bouchard, Paul Bennett, Mounia Lalmas
- **Institution:** TU Delft / Spotify
- **Key Innovation:** First controlled 2×2 factorial study comparing descriptive reasoning traces for generative recommendation. Finding: improving reasoning trace quality (via better SIDs or NL titles) does NOT consistently improve offline recommendation effectiveness under standard SFT/RL training.
- **Link:** [arXiv:2608.23154](https://arxiv.org/abs/2608.23154) (Accepted RecSys'26 Workshop)

### Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms to Semantic Subwords
- **Authors:** Xinrui Miao, Mingjia Yin, Jiaqing Zhang, Wei Guo, Yong Liu, Yuyang Ye, Hao Wang, Enhong Chen
- **Institution:** University of Science and Technology of China
- **Key Innovation:** Proposes Semantic Subword Tokenization (SST) — merges adjacent atom tokens into variable-length semantic subwords, reducing intra-item attention overload. Behavior-induced Co-occurrence Augmentation (BCA) injects coarse-grained semantic prefix transition signals to guide inter-item behavioral modeling.
- **Link:** [arXiv:2608.22734](https://arxiv.org/abs/2608.22734) (Accepted CIKM 2026)

---

## 2. CTR Prediction

### Native Multimodal Representation Learning for CTR Prediction in E-Commerce Scenarios
- **Authors:** Chao Yi, Feifan Yang, Jiawei Feng, Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu
- **Institution:** Alibaba Group
- **Key Innovation:** Identifies that end-to-end multimodal+CRT training fails due to ambiguous supervision from non-multimodal factors in CTR data. Proposes Mine-Then-Train: mines high-quality, multimodally interpretable samples from CTR data, then fine-tunes multimodal encoder on these samples for better alignment with click preferences.
- **Link:** [arXiv:2608.24091](https://arxiv.org/abs/2608.24091) (Accepted CIKM 2026)

### PaletteID: Prototype-Composed Semantic Identifiers for Multimodal CTR Prediction
- **Authors:** Huanyu Liu, Baining Chen, Hui Liu, Zengyang Li, Ziyi Huang
- **Institution:** (Not specified)
- **Key Innovation:** Uses a compact set of representative prototype items as semantic anchors (inspired by palette-based color composition) to bridge pretrained multimodal content space and recommendation models. SQ-DPP selects prototypes jointly considering local content density and global semantic diversity.
- **Link:** [arXiv:2607.29000](https://arxiv.org/abs/2607.29000)

### Dual-Stream MLP is All You Need for CTR Prediction
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution:** Renmin University of China
- **Key Innovation:** DS-MLP consolidates explicit feature interaction learning into a main MLP via knowledge distillation, while a parallel MLP captures implicit interactions. Two alignment strategies optimize dual-stream compatibility. Achieves SOTA with only vanilla MLP structure — highly efficient for large-scale deployment.
- **Link:** [arXiv:2606.04944](https://arxiv.org/abs/2606.04944) (Accepted TKDD)

### Selective Test-Time Compute Scaling for CTR Prediction via Uncertainty-Triggered Feature Path Exploration
- **Authors:** Moyu Zhang, Yun Chen, Yujun Jin, Jinxin Hu, Yu Zhang, Xiaoyi Zeng
- **Institution:** (Not specified)
- **Key Innovation:** UTTSI is a training-free framework that scales inference depth proportionally to per-instance uncertainty. Dual-signal estimator (logit confidence + frequency prior) distinguishes epistemic vs aleatoric uncertainty. Uncertain instances get stochastic feature-path explorations with consistency-weighted ensembling. +5.3% CTR in online A/B test.
- **Link:** [arXiv:2605.24989](https://arxiv.org/abs/2605.24989)

### Deferred is Better: A Framework for Multi-Granularity Deferred Interaction of Heterogeneous Features
- **Authors:** Yi Xu, Moyu Zhang, Chaofan Fan, Jinxin Hu, Yu Zhang, Xiaoyi Zeng
- **Institution:** (Not specified)
- **Key Innovation:** MGDIN addresses feature heterogeneity in CTR models. Multi-granularity feature grouping partitions features by information density. Hierarchical masking defers introduction of low-information features — model builds robust understanding from high-information features first, then progressively incorporates sparser features.
- **Link:** [arXiv:2603.12586](https://arxiv.org/abs/2603.12586)

---

## 3. Sequential Modeling / User Behavior

### Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling
- **Authors:** Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Institution:** (Not specified)
- **Key Innovation:** Mixed-polarity behavior sequences — chronologically interleaving positive and negative tokens within a fixed length budget — consistently outperform positive-only sequences across diverse model architectures. Proposes Target-Aware Polarity Fusion (TAPF) to differentiate behavioral evidence. +1.9% to +9.6% AUC across five architectures.
- **Link:** [arXiv:2606.15252](https://arxiv.org/abs/2606.15252)

### Generative Long-term User Interest Modeling for Click-Through Rate Prediction (GenLI)
- **Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Institution:** (Not specified)
- **Key Innovation:** Interest Generation Module (IGM) generates multiple interest distributions target-independently, incorporating behavior interaction information. Behavior Retrieval Module (BRM) selects related behaviors via simple lookup (O(1) per behavior). Avoids complex matching-based behavioral retrieval while improving diversity.
- **Link:** [arXiv:2605.15905](https://arxiv.org/abs/2605.15905)

### Similar Users-Augmented Interest Network (SUIN)
- **Authors:** Xiaolong Chen, Haoyi Zhao, Xu Huang, Defu Lian
- **Institution:** (Not specified)
- **Key Innovation:** Enhances target user's behavior sequence with behaviors from similar users. User-specific target-aware position encoding identifies source user of each behavior. User-aware target attention jointly considers item-item and user-user correlations to mitigate noise from similar users' behaviors.
- **Link:** [arXiv:2604.23810](https://arxiv.org/abs/2604.23810)

### Deep Situation-Aware Interaction Network (DSAIN) for CTR Prediction
- **Authors:** Yimin Lv, Shuli Wang, Beihong Jin, Yisong Yu, Yapeng Zhang, Jian Dong, Yongkang Wang, Xingxing Wang, Dong Wang
- **Institution:** Meituan
- **Key Innovation:** Introduces "situation" concept — captures behavior type, time, location beyond just interacted items. Reparameterization trick reduces noise in behavior sequences. Heterogeneous situation aggregation learns embeddings. Deployed on Meituan food delivery, serving main traffic. +2.70% CTR, +2.62% CPM, +2.16% GMV online.
- **Link:** [arXiv:2604.12298](https://arxiv.org/abs/2604.12298) (RecSys'23 Full Paper)

---

## 4. Advertising / Auto-Bidding

### Generative Optimization for Incentivized Advertising with Global Level Constraints (GOAL)
- **Authors:** Gege Chen, Ning Luo, Hao Jiang, Da Li, Wenzheng Shu, Teng Sha, Yanxiang Zeng, Wenxin Tai, Fan Zhou, Xialong Liu
- **Institution:** (Industry)
- **Key Innovation:** Formulates incentive allocation as conditional sequence generation. Hierarchical causal state encoder captures local behavioral dynamics and long-range dependencies. Safe Constrained Policy Optimization (SCPO) learns a single generative policy generalizing across ROI constraints without retraining.
- **Link:** [arXiv:2608.04421](https://arxiv.org/abs/2608.04421)

### Less Traffic, Better Outcomes: Competition-Aware Request Dispatch in Real-Time Ad Exchanges
- **Authors:** Jonaid Shianifar, Blaz Mramor, Fangda Zou, Matthieu C. Martin, Xingsheng Guo, Zhihua Zhu, Rong Zhou, Bichen Shi
- **Institution:** (Industry — ad exchange)
- **Key Innovation:** Reduces DSP request volume by 34.2% while increasing net revenue by 4.6%. Uses distributional bid prediction and probabilistic forwarding to selectively route requests. Lightweight policy optimization tracks non-stationary market conditions. Tested on 20B+ daily requests.
- **Link:** [arXiv:2608.03705](https://arxiv.org/abs/2608.03705) (Accepted AdKDD 2026 @ KDD)

### LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising in Multi-Turn LLM Conversations
- **Authors:** Yan Fang, Jialin Chen, Chun Gan, Hang Yu, Mingjun Nie, Yeyu Zhang, Fengxiang He, Ching Law
- **Institution:** (Academic)
- **Key Innovation:** First dynamic auction for LLM-native advertising that jointly optimizes timing and allocation. Bellman optimal stopping + envelope pricing ensures truthful bidding. Bid-independent LLM layer estimates contextual click quality. +11% net revenue over fixed-timing baselines.
- **Link:** [arXiv:2608.00123](https://arxiv.org/abs/2608.00123) (Submitted AAAI 2027)

### HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising
- **Authors:** Ji Wu, Yunshan Peng, Wentao Bai, Yunke Bai, Wenzheng Shu, Jinan Pang, Yanxiang Zeng, Xialong Liu
- **Institution:** (Industry)
- **Key Innovation:** Three-level hierarchy: LLM infers hyperparameters via Think-Act-Observe-Reflect loop → SARSA agent selects among expert models with causal adjustment → dynamic expert pool (PID, MPC, IQL, Decision Transformer) executes bids. Online learning confined to discrete expert selection, reducing exploration risk. +3.6% target cost in production.
- **Link:** [arXiv:2607.24779](https://arxiv.org/abs/2607.24779) (Accepted KDD 2026 Ads Track)

### AIGB-R1: Self-Evolving Generative Auto-Bidding via Hierarchical Planner-Executor Optimization
- **Authors:** Yuejia Dou, Hesong Wang, Xinyu Zhang, Tianyu Wang, Zhilin Zhang, Chuan Yu, Jian Xu, Bo Zheng, Qi Qi
- **Institution:** Alibaba Group
- **Key Innovation:** High-level LLM Planner for macro strategy + low-level Executor for fine-grained decisions. Experience-driven self-evolving loop for autonomous strategy exploration. Decoupled Group Relative Policy Optimization (D-GRPO) enables end-to-end optimization via advantage decoupling.
- **Link:** [arXiv:2607.17281](https://arxiv.org/abs/2607.17281)

### Beyond Single-Episode Optimization: Sliding-Window Aware Generative Auto-Bidding (SWAG-Bid)
- **Authors:** Binglin Wu, Chuan Yue, Yingyi Zhang, Xianneng Li, Ruyue Deng, Weiru Zhang, Xiaoyi Zeng
- **Institution:** (Industry)
- **Key Innovation:** Addresses sparse advertiser value where per-day efficiency ratios are unreliable. Decomposes into episode-level planning (Masked Trajectory Model) and step-level execution. Multi-Window Model Predictive Control Sampling (MWMS) scores candidate plans across all overlapping windows with exponential confidence decay.
- **Link:** [arXiv:2607.25233](https://arxiv.org/abs/2607.25233)

### TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction in Online Advertising
- **Authors:** Kaiyuan Li, Kun Wang, Zhongbo Wang, Teng Sha, Ming Yan, Yanhua Cheng, Xialong Liu
- **Institution:** Kwai
- **Key Innovation:** Factorizes long-horizon CVR into target-window conversion probability and grouped elapsed-delay CDF. Two clocks provide complementary supervision (click-clock for timely status, conversion-clock for long-tail delays). Single learned CDF produces monotone predictions for all horizons. Deployed to full traffic at Kwai: +2.486% expected revenue.
- **Link:** [arXiv:2607.25404](https://arxiv.org/abs/2607.25404)

### RAMP: Robust Ad Recommendation Under Limited Personalized-Feature Availability
- **Authors:** Dairui Liu, Zhongyi Lu, Roger Zhe Li, Changhong Jin, Jitao Lu, Xinyang Shao, Bichen Shi, Mete Sertkan, Aghiles Salah, Aonghus Lawlor, Barry Smyth, Tri Kurniawan Wijaya, Ruihai Dong, Xingsheng Guo
- **Institution:** University College Dublin / Industry
- **Key Innovation:** Handles CTR/CVR prediction when personalized features (age, gender) are unavailable due to privacy regulations. Dual-tower personalized pathway with output masking, separate non-personalized pathway, and distillation-inspired prediction alignment. Consistently outperforms SOTA when personalized features are missing.
- **Link:** [arXiv:2607.17473](https://arxiv.org/abs/2607.17473) (Accepted ICTIR '26)

### Long-History User Transformers for Real-Time Ad Ranking
- **Authors:** Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin
- **Institution:** Yandex
- **Key Innovation:** Decouples history encoding from real-time inference. Offline transformer pre-trained autoregressively with dual objective (feedback + next-item prediction) encodes full cross-surface history into cached representation. Lightweight runtime model combines cached rep with recent events. Recovers 72-80% of full-runtime quality. +2.77% ranking metric in search ads, +2.1% on Yandex Ad Network.
- **Link:** [arXiv:2607.14331](https://arxiv.org/abs/2607.14331)

### MARCO: Click-Intent Decomposition for Calibrated Ads Conversion Prediction
- **Authors:** Shiwen Shen, Xiru Huang, Liang Luo, Jianbo Sun, He Lyu, Zihang Fu, Ivonne Xu, Zhizhuo Li, Zhengyu Zhang, Pei-Ju Sung, Yunmiao Wang, Zixuan Wang, Zhengli Zhao, Qiang Jin, Mike Jermann, Mingda Li, Yang Xiao, Bhavana Challa, Brooke Bian, Yang Li, Ashish Chamoli, Bibek Bhusal, Danning Di, Yuan Jin, Meet Raval et al.
- **Institution:** Google
- **Key Innovation:** Different click types on same ad show 4-fold conversion rate difference. MARCO decomposes each click by intent using logged click type as behavioral label, trains per-intent CVR heads, composes at serving time under predicted intent distribution. +2.80% conversions per click, +0.98% topline improvement.
- **Link:** [arXiv:2608.10562](https://arxiv.org/abs/2608.10562)

### PlatformBid: An Auto-Bidding Benchmark from a Unified Advertising Platform's Perspective
- **Authors:** Shengtian Yang, Yewen Li, Peng Jiang, Zhiyi Lyu, Bo An, Peng Jiang, Qingpeng Cai, Lei Feng
- **Institution:** Kuaishou
- **Key Innovation:** First benchmark from unified ad platform perspective (SSP+DSP+Exchange). Three settings: homogeneous, heterogeneous, and promotional competition. Proposes BidFlow using flow-matching for effective policy representation in dynamic competitive environments. +0.68% target cost in online experiments.
- **Link:** [arXiv:2607.27265](https://arxiv.org/abs/2607.27265)

### Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization
- **Authors:** Jiayi Dan, Bo Li, Lu Deng, Yong Wang
- **Institution:** (Not specified)
- **Key Innovation:** Develops a doubly robust causal effect estimator for chain-structured outcomes (CVR) from semiparametric theory. Achieves faster convergence rate than nuisance parameter estimation, making it robust with neural networks. Targeted regularization framework improves numerical stability.
- **Link:** [arXiv:2608.13461](https://arxiv.org/abs/2608.13461)

---

## 5. Multimodal / Embedding for Recommendation

### WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report
- **Authors:** Junjie Zhou, Ke Mei, Lei Li, Tianyi Wang, Fengyun Rao, Jing Lyu
- **Institution:** Tencent
- **Key Innovation:** Universal multimodal embedding family (2B/4B/9B) supporting text, images, videos, visual documents, and interleaved inputs. Two-stage training: multimodal alignment + refinement with fine-grained relevance supervision. 2B variant surpasses 8B baseline on MMEB-v2; 9B achieves SOTA 80.6. Deployed across WeChat Channels, Official Accounts, Moments, e-commerce. Open-sourced.
- **Link:** [arXiv:2608.24053](https://arxiv.org/abs/2608.24053)

### Multi-Modal Semantic Expansion with Constrained LLM Reranking for Conversational Music Recommendation
- **Authors:** Naman Garg, Sarika Jain, George Fazekas
- **Institution:** (RecSys 2026 Challenge)
- **Key Innovation:** Three-stage pipeline: multi-modal retrieval (7 dense embedding spaces + BM25 + artist match) fused via optimized RRF → lightweight reranking → persona-diversified response generation. Unconstrained LLM injection causes catastrophic regression; conservative injection yields best results. RRF weight optimization via differential evolution improves MRR +19.5%.
- **Link:** [arXiv:2608.23484](https://arxiv.org/abs/2608.23484)

### Adaptive Item-based Collaborative Structures via Noise Rescheduling in Diffusion for Generative Recommendation (ANR-DiffRec)
- **Authors:** Jiaqi Wang, Tianying Liu, Heng Chang, Jihong Guan, Wengen Li, Shuigeng Zhou
- **Institution:** Fudan University
- **Key Innovation:** Incorporates item co-occurrence matrix as collaborative prior for discrete diffusion training. Item-based adaptive noise rescheduling dynamically adjusts denoising weights according to contextual recoverability and behavior-aware item dependencies. Structure-aware denoising during diffusion.
- **Link:** [arXiv:2608.23400](https://arxiv.org/abs/2608.23400)

### SA-RSQ: A Versatile Sparse Representation Framework for Multi-modal Recommender Systems
- **Authors:** Xiang Wang, Shigang Quan, Tingzhen Chang, Kang Yang, Sitong Chen, Yabo Fan, Xingxing Wang, Zhaodian He
- **Institution:** Meituan
- **Key Innovation:** Sparse Activation-based Residual Soft Quantization (SA-RSQ) uses Top-K sparse routing and softmax weights to store compact (Index, Probability) tuples. Decouples per-item storage from codebook dimensionality. +2.51% CTR, +3.66% CPM in online A/B test on food-delivery advertising.
- **Link:** [arXiv:2608.22979](https://arxiv.org/abs/2608.22979)

### From Gradient-Boosted Trees to Deep Recommenders: Practical Lessons from Migrating a Production Customer Support Recommender
- **Authors:** Sonia Sharma, Jeyendran Balakrishnan, Shreya Rajpal, Swapnil Parekh, Nagaraj Janardhana, Andrew Mattarella-Micke
- **Institution:** (Industry)
- **Key Innovation:** Practical lessons migrating production recommender from CatBoost to deep model. Pairwise binary prediction learns jointly from user/item features. Attention pooling over transcript chunks efficiently incorporates long conversation context. Explores two-tower, DeepFM, contrastive loss. Outperforms CatBoost at later conversational stages.
- **Link:** [arXiv:2608.24132](https://arxiv.org/abs/2608.24132)

### TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search
- **Authors:** Zhentao Song, Yufeng Gao, Xing Fang, Jing Wang, Guangxin Song, Bokang Wang, Yipin Dai, He Guo
- **Institution:** Alibaba Group
- **Key Innovation:** Hierarchical Distribution-Calibrated Tokenization combines Field-wise Saliency Reweighting + Distribution-Calibrated Projection. Field-Adaptive Gated Transformer with per-field QKV projections and noise-adaptive gating. Decoupled FiLM Late Fusion + Context-Aware Bias Net + Error-Aware Progressive Training.
- **Link:** [arXiv:2607.13398](https://arxiv.org/abs/2607.13398)

### Quantizing Intent: Cross-Domain Semantic IDs from Organic Activity for Industrial Ranking
- **Authors:** Julie Choi, Haoran Ye, Zhiwei Ding, Bo Long, Benjamin Zelditch, Arpita Vats
- **Institution:** (Industry)
- **Key Innovation:** Cross-domain user SIDs from organic feed activity transferred to ads ranking. Behavioral activity richness governs transfer quality. RQ-FSQ (residual finite scalar quantization) matches dense embedding AUC at 30-280x smaller storage. Hierarchical Discrete Embedding module for multi-level SIDs. +1.522% for cold-start users.
- **Link:** [arXiv:2606.01396](https://arxiv.org/abs/2606.01396)

### From Click Modeling to Offline and Off-Policy Evaluation in Carousel Recommendation
- **Authors:** Jingwei Kang
- **Institution:** (PhD Research)
- **Key Innovation:** PhD thesis research on carousel recommendation evaluation. Develops click model design framework prioritizing mathematical relationships over latent behavioral assumptions. Uses discrete choice models for clicks as choices. Develops carousel-specific offline metrics and plans off-policy evaluation methods.
- **Link:** [arXiv:2608.22022](https://arxiv.org/abs/2608.22022)

---

## 6. Game AI / Reinforcement Learning

### Hierarchical Reinforcement Learning in StarCraft Micromanagement with Influence Maps and Cluster-based Scripts
- **Authors:** Chunhui Bai, Changhe Li, Dequan Li, Xinye Cai, Shengxiang Yang
- **Institution:** (Academic)
- **Key Innovation:** Influence map hashing encodes global battlefield into compact hex codes capturing spatial control. Cluster-based scripts enable dynamic local coordination. Hierarchical multi-Q-table decomposes decisions into clustering strategy selection and tactical execution. Competitive with deep RL baselines while offering sample efficiency and interpretability.
- **Link:** [arXiv:2606.30092](https://arxiv.org/abs/2606.30092)

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors:** Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Institution:** (Industry — EA/Ubisoft)
- **Key Innovation:** Vision paper proposing framework for training RL models suited for game AI and game development. Discusses practicalities of deploying player-facing ML agents in modern games, identifying bottlenecks and promising research directions to accelerate ML adoption in game industry.
- **Link:** [arXiv:2606.20210](https://arxiv.org/abs/2606.20210) (Conference on Games 2026)

### A Differentiable Atari VCS: A Complex, Fully Known Ground Truth for Explainable AI
- **Authors:** Andreas Maier, Siming Bayer, Patrick Krauss
- **Institution:** (Academic)
- **Key Innovation:** Two independent end-to-end differentiable Atari 2600 emulators (Julia: jutari, JAX: jaxtari). Bit-for-bit validated against xitari. Treats cartridge ROM as weight tensor, RAM as soft tape, control flow as gates. GPU path reaches millions of environment-steps/s. Enables gradient-based XAI with fully known ground truth.
- **Link:** [arXiv:2606.22447](https://arxiv.org/abs/2606.22447) (Submitted AAAI 2027)

### Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners
- **Authors:** Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, Laurence Hunt, Chris Summerfield, Joshua B. Tenenbaum, Rui Ponte Costa, Marcelo G. Mattar, Momchil Tomov
- **Institution:** Oxford / MIT
- **Key Innovation:** Using complex gameplay + concurrent fMRI, finds frontier LRMs most closely match human behavioral patterns during game discovery and predict brain activity an order of magnitude better than RL alternatives. Brain alignment reflects model's in-context game state representation, not planning/reasoning.
- **Link:** [arXiv:2505.08019](https://arxiv.org/abs/2505.08019)

### Outbidding and Outbluffing Elite Humans: Mastering Liar's Poker via Self-Play and Reinforcement Learning
- **Authors:** Richard Dewey, Janos Botyanszki, Ciamac C. Moallemi, Andrew T. Zheng
- **Institution:** Columbia University / JPMorgan
- **Key Innovation:** First AI agent (Solly) to achieve elite human play in reduced-format Liar's Poker with extensive multi-player engagement. Model-free actor-critic deep RL via self-play. Outperformed LLMs (including reasoning models). Developed novel bidding strategies, effective randomization, robust to world-class human players.
- **Link:** [arXiv:2511.03724](https://arxiv.org/abs/2511.03724)

### Human-Like Goalkeeping in a Realistic Football Simulation
- **Authors:** Alessandro Sestini, Joakim Bergdahl, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Brady Chen, Fabio Zinno, Michael Jones, Linus Gisslén
- **Institution:** (Industry — EA Sports)
- **Key Innovation:** Sample-efficient DRL for industrial game development. Pre-collected data + increased network plasticity. Goalkeeper agent in EA SPORTS FC 25 outperforms built-in AI by 10% in ball saving rate. Trains 50% faster than standard DRL. Adopted for production use in the most recent FC release.
- **Link:** [arXiv:2510.23216](https://arxiv.org/abs/2510.23216)

### NetworkGames: Simulating Cooperation in Network Games with Personality-driven LLM Agents
- **Authors:** Xuan Qiu
- **Institution:** (Academic)
- **Key Innovation:** Framework connecting LLM agents with geometric deep learning for social simulation. MBTI-personality-endowed LLM agents in network structures. Finding: macro-level cooperation is co-determined by network topology and personality distribution, not predictable from dyadic interactions alone. Hub placement of pro-social personalities significantly promotes cooperation.
- **Link:** [arXiv:2511.21783](https://arxiv.org/abs/2511.21783)

---

## 7. General Recommendation / IR

### R^3: Advertisement Compliance Rectification via Group-Relative Experience Extractor and Curriculum Reinforcement
- **Authors:** Yuan Chen, Zhenyu Hu, Mengge Xue, Te Cao, Liqun Liu, Peng Shu, Huan Yu, Jie Jiang
- **Institution:** (Industry)
- **Key Innovation:** Rectifies textual violations in video ads (speech transcripts + on-screen text). Group-Relative compliance experience extractor bootstraps high-quality supervision. Curriculum RL with hierarchical rewards enforces compliance while maximizing semantic consistency. Full pipeline: text recognition → rewriting → re-rendering.
- **Link:** [arXiv:2607.07318](https://arxiv.org/abs/2607.07318) (ACL 2026 Industry Track)

### FedMM: Federated Collaborative Signal Quantization for Multi-Market CTR Prediction
- **Authors:** Jun Zhang, Dugang Liu, Xing Tang, Xiuqiang He, Zhong Ming
- **Institution:** (Academic)
- **Key Innovation:** Privacy-preserving multi-market recommendation via discrete codebook mechanism. Hierarchical codebook: global federated codebook (updated via aggregation for shared patterns) + local codebook (market-specific semantics). RQ-VAE with dual-layer codebook per market quantizes collaborative embeddings.
- **Link:** [arXiv:2605.11433](https://arxiv.org/abs/2605.11433) (Accepted SIGIR 2026)

### CRAFT: Learn the Schema, Execute the Plan
- **Authors:** Aakash Kolekar, Sahika Genc, Shahriar Shariat, Bunyamin Sisman, Tibor Mezi, Barbara Poblete, Shree Vandana Kachroo, Calvin Chi, Parth Parmar, Ari Singer, Prayaas Jain, Cindy Barker, Benoit Dumoulin
- **Institution:** (Industry)
- **Key Innovation:** Two-stage post-training for schema-grounded coding agents. Schema-stripped PLAN SFT learns domain-structured plans without prompt-time schema injection. Execution-shaped RL aligns policy for tool selection, code quality, and plan-code consistency. Reduces input-token burden by ~9x, schema-discovery loops by up to 5x.
- **Link:** [arXiv:2607.22642](https://arxiv.org/abs/2607.22642)

---

*Report generated on 2026-08-26. Source: arXiv search across AI, LLM, recommendation, advertising, sequential modeling, CTR, and game AI topics.*
