---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Games"
type: synthesis
created: 2026-09-11
updated: 2026-09-11
tags: [arxiv-daily, AI, LLM, recommendation, advertising, CTR, sequential-modeling, game-theory]
---

# arXiv Daily Report — 2026-09-11

Papers collected from arXiv listings (cs.AI, cs.LG, cs.IR, cs.GT) and targeted searches, focusing on LLMs, recommendation systems, advertising, CTR prediction, sequential modeling, and games.

---

## 1. Recommendation Systems & Sequential Modeling

### 1.1 SequenceO1: End-to-End Ultra-Long (100K) Sequence Modeling in Recommendation with Low-Rank Caching

| Field | Detail |
|-------|--------|
| **Authors** | Lin Guan, Jia-Qi Yang, Zhishan Zhao, Jiaqi Huang, Hangyu Wang, Longbin Li, Beichuan Zhang, Haonan Jiang, Jinan Ni, Xiangyu Fan, Xiaowen Li, Ziyao Ren, Yuhang Qi, Xiaolong Zhu, Xuanyuan Luo, Qiwei Chen, Yi Cheng, Lele Yu |
| **Institution** | Douyin / ByteDance |
| **Published** | 2026-09-09 (RecSys'26 Industry Track, long oral) |
| **Abstract** | Proposes an end-to-end ultra-long (100K tokens) sequence modeling framework for recommendation with low-rank caching for efficient attention. Deployed in production on Douyin (TikTok China). Topics: industrial recommender systems, sequential recommendation, ultra-long user behavior sequence modeling, long-term user modeling, end-to-end ranking, CTR prediction, efficient attention, sequence compression, user representation caching, and large-scale recommendation systems. |
| **Key Innovations** | (1) Low-rank caching mechanism to handle 100K-length user behavior sequences; (2) End-to-end architecture unifying retrieval and ranking; (3) Production deployment on Douyin demonstrating scalability. |
| **Link** | [arXiv:2609.08443](https://arxiv.org/abs/2609.08443) |

### 1.2 UniRec: Cross-stage Multi-Task Fusion with Preference Alignment for Cascaded Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Lingyuan Kong, Jiaqi Cui, Fanjiao Zeng, Congqi Wang, Yu Li, Yuan Cheng, Jingxin Liu, Xiaoshuang Chen, Kaiqiao Zhan |
| **Institution** | (Not specified) |
| **Published** | 2026-09-11 |
| **Abstract** | Cross-stage multi-task fusion framework for cascaded recommender systems with preference alignment. Addresses the challenge of aligning objectives across retrieval, pre-ranking, and ranking stages. |
| **Key Innovations** | (1) Cross-stage multi-task fusion architecture; (2) Preference alignment mechanism across cascaded stages. |
| **Link** | [arXiv:2609.11052](https://arxiv.org/abs/2609.11052) |

### 1.3 Closing the Long-Short View Gap in Sequential Recommendation without Cached History

| Field | Detail |
|-------|--------|
| **Authors** | Lingfeng Shi, Chengkai Huang, Lina Yao, James Caverlee |
| **Institution** | (Not specified) |
| **Published** | 2026-09-09 (CIKM 2026) |
| **Abstract** | Addresses the gap between long-term and short-term user interest modeling in sequential recommendation without relying on cached history. Proposes methods to bridge long-short view discrepancy. |
| **Key Innovations** | (1) Eliminates dependency on cached history for long-term modeling; (2) Bridges the gap between short-term and long-term interest representations. |
| **Link** | [arXiv:2609.06219](https://arxiv.org/abs/2609.06219) |

### 1.4 Task-Blind No MORE: Multi-Task Information Flow in Unified Ranking Backbones

| Field | Detail |
|-------|--------|
| **Authors** | Yuchen Wang, Feng Niu, Qing Tan, Junting Lu, Baoxin Wu, Jun Gao |
| **Institution** | (Not specified) |
| **Published** | 2026-09-09 (CIKM 2026) |
| **Abstract** | Addresses the problem of task-blind information flow in unified ranking backbones. Demonstrates how multi-task learning in recommendation systems can benefit from explicit task-aware information routing. |
| **Key Innovations** | (1) Multi-task information flow control in unified ranking; (2) Task-aware backbone design for multi-objective optimization. |
| **Link** | [arXiv:2609.07273](https://arxiv.org/abs/2609.07273) |

### 1.5 FedHUR: Learning Hierarchical Utility-Guided Client Relations for Personalized Federated Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Mingzhe Han, Jiahao Liu, Dongsheng Li, Jiankui Zhou, Hansu Gu, Peng Zhang, Ning Gu, Tun Lu |
| **Institution** | Fudan University |
| **Published** | 2026-09-11 |
| **Abstract** | Proposes a federated learning framework that learns hierarchical utility-guided client relations for personalized recommendation. Addresses privacy-preserving recommendation through federated learning. |
| **Key Innovations** | (1) Hierarchical utility-guided client relation learning; (2) Privacy-preserving personalized recommendation via federated learning. |
| **Link** | [arXiv:2609.11632](https://arxiv.org/abs/2609.11632) |

---

## 2. CTR Prediction

### 2.1 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang |
| **Institution** | LinkedIn |
| **Published** | 2026-08-10 (updated) |
| **Abstract** | End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Introduces context-conditioned decoding with multi-tower prediction heads to model post-scoring signals like ad position, resolving the chicken-and-egg problem between predicted CTR and ranking. Achieves 11.04% CTR lift vs. production LiRank baseline. |
| **Key Innovations** | (1) Context-conditioned decoding with multi-tower heads for post-scoring signals; (2) Self-gated attention mechanism for stable training; (3) Timestamp-based RoPE for temporal relationships; (4) Session masking to prevent train-serve skew; (5) Tensor packing, sequence chunking, custom Flash Attention kernels. |
| **Link** | [arXiv:2602.11410](https://arxiv.org/abs/2602.11410) |

### 2.2 Field-Aware Transformer (FAT) for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Bencheng Yan, Yuejie Lei, Zhiyuan Zeng, Zheye Deng, Di Wang, Kaiyi Lin, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng |
| **Institution** | Alibaba Group |
| **Published** | 2026-05-31 (KDD 2026) |
| **Abstract** | Identifies a fundamental structural misalignment in CTR prediction: standard Transformers assume sequential compositionality, whereas CTR data demand combinatorial reasoning over heterogeneous fields. Introduces the Field-Aware Transformer (FAT) to restore alignment, enabling principled scaling laws in CTR prediction. |
| **Key Innovations** | (1) Field-aware self-attention for combinatorial feature interactions; (2) Resolves structural conflict between sequential Transformers and heterogeneous CTR data; (3) Demonstrates clear scaling law in CTR prediction. |
| **Link** | [arXiv:2511.12081](https://arxiv.org/abs/2511.12081) |

### 2.3 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng |
| **Institution** | (Not specified, major social-media platform) |
| **Published** | 2026-06-06 |
| **Abstract** | Addresses the residual connection bottleneck in Transformer-based CTR models. DeRes routes each layer through two parallel paths — an Identity residual path and a Block Attention Residual path — with a vector-wise gate. On a large-scale industrial dataset (331M interactions), achieves +0.32% AUC at under 5% extra FLOPs. Fits a markedly steeper compute-AUC scaling law (gamma=0.118 vs. 0.071 for OneTrans). |
| **Key Innovations** | (1) Dual-path residual routing (Identity + Block Attention); (2) Pointwise AttnRes with SiLU for parallel multi-interest patterns; (3) 1.66x better scaling than OneTrans. |
| **Link** | [arXiv:2606.07980](https://arxiv.org/abs/2606.07980) |

### 2.4 LoopCTR: Unlocking the Loop Scaling Power for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | (See paper) |
| **Institution** | (Not specified) |
| **Published** | 2026-04-21 |
| **Abstract** | Introduces the loop scaling paradigm for CTR prediction, increasing training-time computation through recursive reuse of shared model layers rather than stacking additional parameters. Reveals 0.02–0.04 AUC of untapped headroom, and a counter-intuitive finding that models trained with fewer loops exhibit higher oracle ceilings. |
| **Key Innovations** | (1) Loop scaling paradigm via recursive layer reuse; (2) Parameter-efficient scaling approach; (3) Counter-intuitive finding about oracle ceilings vs. loop count. |
| **Link** | [arXiv:2604.19550](https://arxiv.org/abs/2604.19550) |

### 2.5 LENS: A Staged Design for Interaction Granularity in Sequential CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Yuan Wang, Yue Liu, Jun Zhang, Jie Jiang |
| **Institution** | Tencent Inc., Beijing, China |
| **Published** | 2026-06-11 |
| **Abstract** | Organizes sequential CTR models along interaction granularity: raw-item (DIN-style) vs. latent-query (HyFormer-style). Introduces QueryPos, a position prior providing stable positional information for latent-query architectures. |
| **Key Innovations** | (1) Interaction granularity as an organizing perspective; (2) QueryPos position prior for latent-query sequential CTR; (3) Staged design framework for target-history interaction. |
| **Link** | [arXiv:2605.25583](https://arxiv.org/abs/2605.25583) |

---

## 3. Advertising & LLM-Enhanced Recommendation

### 3.1 Fine-Tuned LLM as a Complementary Predictor Improving Ads System

| Field | Detail |
|-------|--------|
| **Authors** | Hui Yang, Daiwei He, Kevin Jiang, Taejin Park, Kungang Li, Jiajun Luo, Yuying Chen, Xinyi Zhang, Sihan Wang, Haoyu He, Yu Liu, Lakshmi Manoharan, David Xue, Shubham Barhate, Runze Su, Duna Zhan, Ling Leng, Siping Ji, Jinfeng Zhuang, Alice Wu, Leo Lu, Han Sun, Zhifang Liu |
| **Institution** | (Industry — large-scale production advertising system) |
| **Published** | 2026-05-27 |
| **Abstract** | Introduces a complementary paradigm for ads: a fine-tuned open-source LLM used not as a ranker, but as an ads-specific ancillary predictor, forecasting likely advertisers from user profiles and histories. LLM outputs augment candidate generation and provide informative priors to downstream ranking. Demonstrates substantial offline improvements and measurable online business impact. |
| **Key Innovations** | (1) LLM as ancillary predictor (not primary ranker); (2) Targeted advertiser prediction from user profiles; (3) Dual consumption: retrieval filters + ranking features. |
| **Link** | [arXiv:2605.27856](https://arxiv.org/abs/2605.27856) |

### 3.2 LLM Retrieval for Stable and Predictable Ad Recommendations

| Field | Detail |
|-------|--------|
| **Authors** | Vinodh Kumar Sunkara, Satheeshkumar Karuppusamy, Hangjun Xu, Sai Deepika Regani, Kshitij Gupta, Gaby Nahum, Sneha Iyer, Jean-Baptiste Fiot, Yinglong Guo, Xiaowen Guo, Atul Jangra, Yucheng Liu, Jinghao Yan, Vijay Pappu, Benjamin Schulte, Deepak Chandra |
| **Institution** | (Industry — large-scale ads platform) |
| **Published** | 2026-05-21 |
| **Abstract** | Introduces a new evaluation framework for quantifying stability and predictability of an ads recommender system. Presents an online validated semantic candidate generation framework powered by fine-tuned LLMs that extracts hierarchical semantic attributes from ad creatives. Graph-based expansion ensures retrieved candidates encapsulate semantic variants of an ad. |
| **Key Innovations** | (1) Stability and predictability evaluation framework for ads; (2) Hierarchical semantic attribute extraction from ad creatives via LLM; (3) Graph-based semantic variant expansion for consistent delivery. |
| **Link** | [arXiv:2605.21969](https://arxiv.org/abs/2605.21969) |

### 3.3 RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Jin Chen, Shangyu Zhang, Bin Hu, Chao Zhou, Junwei Pan, Gengsheng Xue, Wentao Ning, Gengyu Weng, Wang Zheng, Shaohua Liu, Zeen Xu, Chengyuan Mai, Shijie Quan, Tingyu Jiang, Lifeng Wang, Shudong Huang, Chengguo Yin, Haijie Gu, Jie Jiang |
| **Institution** | Tencent (Weixin Video Accounts, Official Accounts and Moments) |
| **Published** | 2026-04-20 (v3: 2026-05-12) |
| **Abstract** | Proposes RankUp to mitigate representation collapse and enhance expressive capacity through randomized permutation splitting over sparse features, a multi-embedding paradigm, global token integration, and crossed pretrained embedding tokens. Fully deployed in large-scale production across Weixin Video Accounts, Official Accounts and Moments, yielding GMV improvements of 3.41%, 4.81% and 2.12%. |
| **Key Innovations** | (1) Randomized permutation splitting for high-rank representations; (2) Multi-embedding paradigm; (3) Global token integration; (4) Production deployment with measurable GMV gains. |
| **Link** | [arXiv:2604.17878](https://arxiv.org/abs/2604.17878) |

### 3.4 Dual-Stream MLP is All You Need for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen |
| **Institution** | Renmin University of China |
| **Published** | 2026-06-03 |
| **Abstract** | Proposes DS-MLP, a dual-stream MLP framework for CTR prediction. Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, while a parallel MLP captures implicit interactions. Achieves state-of-the-art across three benchmarks with vanilla MLP structure. |
| **Key Innovations** | (1) Dual-stream MLP for explicit/implicit feature interactions; (2) Knowledge distillation for capacity consolidation; (3) Two alignment strategies for MLP compatibility. |
| **Link** | [arXiv:2606.04944](https://arxiv.org/abs/2606.04944) |

---

## 4. LLMs & AI Agents

### 4.1 The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

| Field | Detail |
|-------|--------|
| **Authors** | Yi Duan, Ying Liu, Zirui Tang, Haodong Chen, Jun Zhou, Yumou Liu, Bangrui Xu, Yukai Wu, Sidi Chen, Yuhan Zhou, Haoyu Wang, Xiaoyou Yu, Shaokun Han, Xuzhou Zhu, Le Zhou, Bolin Lu, Wei Zhou, Jiachen Liu, Nuozhou Fang, Jiaxin Tian, Ruoyu Chen, Yuxuan Li, Kai Zuo, Kaiyan Zhang, Jiantao Qiu, Conghui He, Guoliang Li, Bowen Zhou, Zhiyuan Liu, Zhoufutu Wen, Jihua Kang, Xuanhe Zhou, Fan Wu |
| **Institution** | (Multiple institutions) |
| **Published** | 2026-09-11 |
| **Abstract** | Explores the concept of genuine recursive self-improvement in AI systems, examining what it would take for an AI system to autonomously improve its own architecture and capabilities. |
| **Key Innovations** | (1) Framework for genuine recursive self-improvement; (2) Analysis of the "last AI built by humans" threshold. |
| **Link** | [arXiv:2609.11873](https://arxiv.org/abs/2609.11873) |

### 4.2 Rethinking On-Policy Distillation of LLMs II: One Training Example

| Field | Detail |
|-------|--------|
| **Authors** | Zixuan Fu, Bingxiang He, Yuxin Zuo, Haohuan Huang, Jinqian Zhang, Ruhang Xiao, Cheng Qian, Qinyu Luo, Huan-ang Gao, Yudong Wang, Zhiyuan Liu, Ning Ding, Chaojun Xiao |
| **Institution** | (Not specified) |
| **Published** | 2026-09-04 |
| **Abstract** | Investigates on-policy distillation of large language models with extreme data efficiency — using only one training example. 29 pages, 20 figures. |
| **Key Innovations** | (1) Extreme few-shot on-policy distillation for LLMs; (2) Analysis of one-shot training for LLM distillation. |
| **Link** | [arXiv:2609.04172](https://arxiv.org/abs/2609.04172) |

### 4.3 Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments

| Field | Detail |
|-------|--------|
| **Authors** | Jie Wu, Zhenru Zhang, Beichen Zhang, Xuwu Wang, Yuhui Su, Mouxiang Chen, Peng Wang, Zhihai Wang, Que Shen, Hao Zhou, An Yang, Fei Huang, Yujiu Yang, Dayiheng Liu |
| **Institution** | Alibaba / DAMO Academy |
| **Published** | 2026-09-04 |
| **Abstract** | Proposes a framework for converting agent execution trajectories into scalable terminal environments, enabling scalable training and evaluation of AI agents. |
| **Key Innovations** | (1) Agent trajectory to terminal environment conversion; (2) Scalable agent evaluation framework. |
| **Link** | [arXiv:2609.04148](https://arxiv.org/abs/2609.04148) |

### 4.4 Efficient Test-Time Adaptation through Human-AI Interaction

| Field | Detail |
|-------|--------|
| **Authors** | Zora Zhiruo Wang, Apurva Gandhi, Rulin Shao, Aspen Chen, Jonas Mueller, Zhiqi Liang, Jett Chen, Michael Ryan, Qianou Ma, Luxi He, Zhoujun Cheng, Andre He, Seungone Kim, Jiayi Geng, Mingqian Zheng, Weiwei Sun, Zheyuan Zhang, Xinran Zhao, Yike Wang, Abe Hou, Liwei Jiang, Pang Wei Koh, Diyi Yang, Graham Neubig, Daniel Fried |
| **Institution** | CMU, Stanford, Google DeepMind |
| **Published** | 2026-09-04 |
| **Abstract** | Studies how human-AI interaction can enable efficient test-time adaptation, allowing models to quickly adapt to new tasks or distributions at inference time through human feedback. |
| **Key Innovations** | (1) Human-AI interaction protocol for test-time adaptation; (2) Efficient inference-time model adjustment. |
| **Link** | [arXiv:2609.04141](https://arxiv.org/abs/2609.04141) |

### 4.5 How Often Should a Recommender Call an LLM? Value-Weighted Routing, Monitoring, and Seasonal Robustness

| Field | Detail |
|-------|--------|
| **Authors** | Bhavtosh Rath |
| **Institution** | (Not specified) |
| **Published** | 2026-07 (accepted CAESAR workshop, ECML-PKDD 2026) |
| **Abstract** | Addresses the practical question of when a recommender system should invoke an LLM. Proposes value-weighted routing with monitoring and seasonal robustness to optimize the cost-benefit tradeoff of LLM calls in recommendation pipelines. |
| **Key Innovations** | (1) Value-weighted routing for LLM invocation decisions; (2) Seasonal robustness in LLM-recommender interaction; (3) Cost-benefit optimization framework. |
| **Link** | [arXiv:2607.25068](https://arxiv.org/abs/2607.25068) |

### 4.6 LILA: Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry

| Field | Detail |
|-------|--------|
| **Authors** | Sankar Behera, Dhruv Singh, Anshika Agnihotri, Raj Kumar Choudhary, Satyadev Ahlawat, Yamuna Prasad |
| **Institution** | (Not specified) |
| **Published** | 2026-09-11 |
| **Abstract** | Proposes calibration-free structured pruning for LLMs using latent spectral geometry. Eliminates the need for calibration data during pruning. |
| **Key Innovations** | (1) Calibration-free structured pruning; (2) Latent spectral geometry for model compression. |
| **Link** | [arXiv:2609.11163](https://arxiv.org/abs/2609.11163) |

### 4.7 Why Does Post-Training Quantization Work?

| Field | Detail |
|-------|--------|
| **Authors** | Yuxiang Chen, Michael Beyer, Jun Zhu, Jianfei Chen |
| **Institution** | Tsinghua University |
| **Published** | 2026-09-11 |
| **Abstract** | Comprehensive theoretical and empirical analysis (45 pages, 26 figures) of why post-training quantization works for large language models. |
| **Key Innovations** | (1) Theoretical analysis of post-training quantization effectiveness; (2) Comprehensive empirical evaluation across quantization regimes. |
| **Link** | [arXiv:2609.11716](https://arxiv.org/abs/2609.11716) |

### 4.8 Thinking with Looped Flows

| Field | Detail |
|-------|--------|
| **Authors** | Ayhan Suleymanzade, Chanhyuk Lee, Floor Eijkelboom, Nicholas M. Boffi, İsmail İlkan Ceylan, Jinwoo Kim |
| **Institution** | (Not specified) |
| **Published** | 2026-09-11 |
| **Abstract** | Proposes looped flow architectures for thinking/reasoning tasks, connecting flow-based generative models with iterative reasoning. |
| **Key Innovations** | (1) Looped flow architecture for reasoning; (2) Connection between flow models and iterative thinking. |
| **Link** | [arXiv:2609.11801](https://arxiv.org/abs/2609.11801) |

---

## 5. RAG & Information Retrieval

### 5.1 VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents

| Field | Detail |
|-------|--------|
| **Authors** | Peiyuan Gao, Gaoyuan Zhang, Haojie Qin, Yahui Sun, Qianyi Zhang, Yunhao Zhang, Zeyu Wang, Wei Lu |
| **Institution** | (Not specified) |
| **Published** | 2026-09-11 |
| **Abstract** | Accurate and token-efficient RAG framework designed for structured documents. Addresses the challenge of maintaining accuracy while reducing token consumption in RAG pipelines. |
| **Key Innovations** | (1) Token-efficient RAG for structured documents; (2) Balance between accuracy and computational cost. |
| **Link** | [arXiv:2609.11390](https://arxiv.org/abs/2609.11390) |

### 5.2 EAGER: Enrich-and-Align Generative Query Recommendation from Clicked Items in E-commerce Search

| Field | Detail |
|-------|--------|
| **Authors** | Shuwei Yuan, Mingqian Ding, Luxin Liu, Rong Xiao, Xiaoyi Zeng |
| **Institution** | (Not specified) |
| **Published** | 2026-09-09 (EMNLP 2026 Industry Track) |
| **Abstract** | Generative query recommendation system for e-commerce that enriches and aligns queries based on clicked items. |
| **Key Innovations** | (1) Enrich-and-align framework for query generation; (2) Click-based query recommendation for e-commerce search. |
| **Link** | [arXiv:2609.07143](https://arxiv.org/abs/2609.07143) |

### 5.3 Agentic Share-of-Search: A Multi-Agent AI System for Competitive Decision-Making in LLM-Mediated E-Commerce

| Field | Detail |
|-------|--------|
| **Authors** | Spandan Ghose Chowdhury |
| **Institution** | (Not specified) |
| **Published** | 2026-09-11 (Decision Science Institute Annual Conference 2026) |
| **Abstract** | Multi-agent AI system for competitive decision-making in e-commerce, leveraging LLMs for share-of-search analysis. |
| **Key Innovations** | (1) Multi-agent architecture for competitive e-commerce analysis; (2) LLM-mediated search share optimization. |
| **Link** | [arXiv:2609.11190](https://arxiv.org/abs/2609.11190) |

---

## 6. Game Theory & AI in Games

### 6.1 GPU-CFR: 80x Faster Counterfactual Regret Minimization

| Field | Detail |
|-------|--------|
| **Authors** | Boning Li, Longbo Huang |
| **Institution** | (Not specified) |
| **Published** | 2026-09-11 |
| **Abstract** | Achieves 80x speedup in Counterfactual Regret Minimization (CFR) by compiling the game to static dataflow and CUDA graph replay. Dramatically accelerates equilibrium computation in imperfect-information games. |
| **Key Innovations** | (1) 80x speedup in CFR via static dataflow compilation; (2) CUDA graph replay for game solving; (3) Enables large-scale game equilibrium computation. |
| **Link** | [arXiv:2609.11923](https://arxiv.org/abs/2609.11923) |

### 6.2 The Internal Anatomy of Strategic Choice in Large Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Vinícius Ferraz, Leon Houf, Enrico Ferrea |
| **Institution** | (Not specified) |
| **Published** | 2026-09-09 |
| **Abstract** | Investigates how LLMs make strategic choices internally, analyzing the decision-making mechanisms in game-theoretic settings. |
| **Key Innovations** | (1) Analysis of LLM strategic decision-making internals; (2) Connection between LLM reasoning and game-theoretic behavior. |
| **Link** | [arXiv:2609.07478](https://arxiv.org/abs/2609.07478) |

### 6.3 Turn-Based Combat Arena: A New Framework for Multiagent Training and Game Balancing

| Field | Detail |
|-------|--------|
| **Authors** | V. M. Vasyuta, V. V. Malitskyi, O. S. Kushnir, B. I. Horon, V. A. Franiv |
| **Institution** | (Not specified) |
| **Published** | 2026-09-04 |
| **Abstract** | Configurable framework for turn-based strategy games designed to support efficient training and evaluation of ML agents. Enables flexible modification of game rules and supports tens of thousands of games per second with billions of gameplay records. |
| **Key Innovations** | (1) High-throughput simulation (10K+ games/sec); (2) Configurable game balancing framework; (3) Scalable agent training platform. |
| **Link** | [arXiv:2609.03122](https://arxiv.org/abs/2609.03122) |

### 6.4 Paradoxes of Game Theoretic Equilibria and Price of Anarchy

| Field | Detail |
|-------|--------|
| **Authors** | Georgios Piliouras, Ian Gemp, Siqi Liu, Luke Marris |
| **Institution** | (Not specified) |
| **Published** | 2026-07-13 |
| **Abstract** | Shows that reducing multi-agent learning to static equilibrium and black-box regret analysis obscures underlying dynamic disequilibrium. Proves that worst-case pure Nash equilibria dictating robust PoA bounds manifest as topologically unstable strict saddles. Demonstrates O(1/T) swap-regret minimization does not preclude macroscopic turbulence, including chaotic limit sets. |
| **Key Innovations** | (1) Topological instability of Nash equilibria in congestion games; (2) Unbounded PoA under all strictly positive affine costs; (3) Chaotic dynamics in seemingly stable equilibria. |
| **Link** | [arXiv:2607.11752](https://arxiv.org/abs/2607.11752) |

### 6.5 Large Language Models as Strategic Bidding Agents in P2P Energy Trading Markets

| Field | Detail |
|-------|--------|
| **Authors** | Ismail Lotfi, Ali Ghrayeb, Haitham Abu-Rub |
| **Institution** | (Not specified) |
| **Published** | 2026-09-09 (IEEE IECON 2026) |
| **Abstract** | Uses LLMs as strategic bidding agents in peer-to-peer energy trading markets, combining game theory with language model capabilities. |
| **Key Innovations** | (1) LLM-driven strategic bidding in energy markets; (2) Game-theoretic framework for P2P energy trading. |
| **Link** | [arXiv:2609.05462](https://arxiv.org/abs/2609.05462) |

### 6.6 Board Game Arena: A Framework and Benchmark for Assessing LLMs via Strategic Play

| Field | Detail |
|-------|--------|
| **Authors** | (See paper) |
| **Institution** | (Not specified) |
| **Published** | 2025-08-05 (updated 2026-08-24) |
| **Abstract** | Framework for evaluating LLM decision-making through strategic board games using Google's OpenSpiel library. Integrates API access to models via LiteLLM, local model deployment via vLLM, and distributed execution through Ray. |
| **Key Innovations** | (1) OpenSpiel-based LLM evaluation through board games; (2) Distributed execution via Ray; (3) Multi-provider LLM integration. |
| **Link** | [arXiv:2508.03368](https://arxiv.org/abs/2508.03368) |

---

## 7. Scaling Laws & Architecture

### 7.1 Thinking with Looped Flows

| Field | Detail |
|-------|--------|
| **Authors** | Ayhan Suleymanzade, Chanhyuk Lee, Floor Eijkelboom, Nicholas M. Boffi, İsmail İlkan Ceylan, Jinwoo Kim |
| **Institution** | (Not specified) |
| **Published** | 2026-09-11 |
| **Abstract** | Connects looped flow architectures with iterative reasoning/thinking capabilities. |
| **Key Innovations** | (1) Looped flow architecture for reasoning; (2) Bridging generative flows and iterative thinking. |
| **Link** | [arXiv:2609.11801](https://arxiv.org/abs/2609.11801) |

### 7.2 Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data

| Field | Detail |
|-------|--------|
| **Authors** | Atindra Jha, Margaret Li, Jure Leskovec, Percy Liang, Luke Zettlemoyer |
| **Institution** | Stanford, Allen AI |
| **Published** | 2026-09-11 |
| **Abstract** | Studies how MoE models behave under data scarcity and sparsity, finding that they overfit more to repeated data compared to dense models. |
| **Key Innovations** | (1) Analysis of MoE overfitting behavior under data scarcity; (2) Implications for scaling MoE architectures. |
| **Link** | [arXiv:2609.11917](https://arxiv.org/abs/2609.11917) |

### 7.3 Can LLMs Discover Scientific Laws in Real and Parallel Worlds?

| Field | Detail |
|-------|--------|
| **Authors** | Yiming Huang, Ziche Liu, Zhuohang Wu, Yiqian Wang, Junxia Cui, Xinkai Zou, Linjun Mao, Nan Huang, Naicheng Yu, Kaijie Zhu, Yue Ma, Kun Zhou, Letian Peng, Jingbo Shang |
| **Institution** | UCSD, multiple institutions |
| **Published** | 2026-09-01 |
| **Abstract** | Introduces SCILAWS-BENCH, a benchmark for scientific law discovery built from 381 scientific papers with 118 problems and ~8M real data points. Includes two settings: fixed-record law discovery and active recovery of hidden laws. |
| **Key Innovations** | (1) SCILAWS-BENCH benchmark for scientific discovery; (2) Dual-setting evaluation (real + parallel worlds); (3) Reveals memorization vs. discovery dynamics in LLMs. |
| **Link** | [arXiv:2609.01552](https://arxiv.org/abs/2609.01552) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **LLM in Ads/RecSys** | CADET (LinkedIn), FAT (Alibaba), LLM as Predictor (industry), LLM Retrieval (industry), RankUp (Tencent) |
| **Ultra-long Sequence Modeling** | SequenceO1 (Douyin, 100K tokens), LoopCTR (recursive scaling) |
| **CTR Scaling Laws** | FAT (field-aware), DeRes (dual residual), LoopCTR (loop scaling) |
| **LLM + Games** | GPU-CFR (80x CFR speedup), LLM Strategic Choice, LLM Energy Trading |
| **Efficient LLM** | LILA (calibration-free pruning), PTQ analysis (45 pages), Dual-Stream MLP |
| **Agent Systems** | Terminal-Universe, Test-Time Adaptation, Agentic Share-of-Search |
| **Federated Recommendation** | FedHUR (hierarchical utility-guided) |
