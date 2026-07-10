---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-07-10
updated: 2026-07-10
tags: [arxiv, ai, llm, ctr, recommendation, sequential-modeling, advertising, games, multi-agent, reasoning]
---

# arXiv AI Research Paper Search Report — 2026-07-10

> Curated selection of recent papers across AI, LLMs, CTR prediction, recommendation systems, sequential modeling, advertising, game theory, and multi-agent systems.

---

## 1. CTR Prediction & Recommendation Systems

### 1.1 LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation

| Field | Details |
|-------|---------|
| **Title** | LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation |
| **Authors** | Lee Xiong, Zhirong Chen, Rahul Mayuranath, Shangran Qiu, Arda Ozdemir, Lu Li, Yang Hu, Dave Li, Jingtao Ren, Howard Cheng, Fabian Souto Herrera, Ahmed Agiza, Baruch Epshtein, Anuj Aggarwal, Julia Ulziisaikhan, Chao Wang, Dinesh Ramasamy, Parshva Doshi, Sri Reddy, Arnold Overwijk |
| **Institution** | Meta |
| **Date** | Jan 27, 2026 |
| **arXiv** | [2601.20083](https://arxiv.org/abs/2601.20083) |

**Abstract:** We present LLaTTE (LLM-Style Latent Transformers for Temporal Events), a scalable transformer architecture for production ads recommendation. Through systematic experiments, we demonstrate that sequence modeling in recommendation systems follows predictable power-law scaling similar to LLMs. Crucially, we find that semantic features bend the scaling curve: they are a prerequisite for scaling, enabling the model to effectively utilize the capacity of deeper and longer architectures. To realize the benefits of continued scaling under strict latency constraints, we introduce a two-stage architecture that offloads the heavy computation of large, long-context models to an asynchronous upstream user model. We demonstrate that upstream improvements transfer predictably to downstream ranking tasks. Deployed as the largest user model at Meta, this multi-stage framework drives a 4.3% conversion uplift on Facebook Feed and Reels with minimal serving overhead, establishing a practical blueprint for harnessing scaling laws in industrial recommender systems.

**Key Innovations:**
- Demonstrates that CTR/recommendation sequence modeling follows power-law scaling laws analogous to LLMs
- Semantic features are a prerequisite for scaling — they "bend" the scaling curve
- Two-stage async architecture: large upstream user model + lightweight downstream ranker
- Deployed at Meta as the largest user model, achieving 4.3% conversion uplift

---

### 1.2 GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm

| Field | Details |
|-------|---------|
| **Title** | GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm |
| **Authors** | Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin |
| **Institution** | Baidu |
| **Date** | Feb 2, 2026 |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |

**Abstract:** Traditional Deep Learning Recommendation Models (DLRMs) face increasing bottlenecks in performance and efficiency, often struggling with generalization and long-sequence modeling. Inspired by the scaling success of Large Language Models (LLMs), we propose Generative Ranking for Ads at Baidu (GRAB), an end-to-end generative framework for Click-Through Rate (CTR) prediction. GRAB integrates a novel Causal Action-aware Multi-channel Attention (CamA) mechanism to effectively capture temporal dynamics and specific action signals within user behavior sequences. Full-scale online deployment demonstrates that GRAB significantly outperforms established DLRMs, delivering a 3.05% increase in revenue and a 3.49% rise in CTR. Furthermore, the model demonstrates desirable scaling behavior: its expressive power shows a monotonic and approximately linear improvement as longer interaction sequences are utilized.

**Key Innovations:**
- End-to-end generative CTR framework inspired by LLM scaling success
- Causal Action-aware Multi-channel Attention (CamA) captures temporal dynamics and action-specific signals
- Demonstrates monotonic scaling: performance improves linearly with longer sequences
- Full-scale deployment at Baidu: +3.05% revenue, +3.49% CTR

---

### 1.3 EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling

| Field | Details |
|-------|---------|
| **Title** | EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling |
| **Authors** | Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, Jian Xu, Xinyang Chen |
| **Institution** | Alibaba (Taobao) |
| **Date** | Feb 11, 2026 |
| **arXiv** | [2602.10811](https://arxiv.org/abs/2602.10811) |

**Abstract:** Efficiently scaling industrial Click-Through Rate (CTR) prediction has recently attracted significant research attention. Existing approaches typically employ early aggregation of user behaviors to maintain efficiency. However, such non-unified or partially unified modeling creates an information bottleneck by discarding fine-grained, token-level signals essential for unlocking scaling gains. In this work, we revisit the fundamental distinctions between CTR prediction and Large Language Models (LLMs), identifying two critical properties: the asymmetry in information density between behavioral and non-behavioral features, and the modality-specific priors of content-rich signals. Accordingly, we propose the Efficiently Scalable Transformer (EST), which achieves fully unified modeling by processing all raw inputs in a single sequence without lossy aggregation. EST integrates two modules: Lightweight Cross-Attention (LCA), which prunes redundant self-interactions to focus on high-impact cross-feature dependencies, and Content Sparse Attention (CSA), which utilizes content similarity to dynamically select high-signal behaviors. Extensive experiments show that EST exhibits a stable and efficient power-law scaling relationship, enabling predictable performance gains with model scale. Deployed on Taobao's display advertising platform, EST significantly outperforms production baselines, delivering a 3.27% RPM increase and a 1.22% CTR lift.

**Key Innovations:**
- Fully unified modeling — all raw inputs in a single sequence without lossy early aggregation
- Identifies information density asymmetry as key distinction between CTR and LLM
- Lightweight Cross-Attention (LCA) + Content Sparse Attention (CSA) for efficiency
- Stable power-law scaling demonstrated in CTR prediction
- Deployed at Taobao: +3.27% RPM, +1.22% CTR

---

### 1.4 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs

| Field | Details |
|-------|---------|
| **Title** | IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs |
| **Authors** | Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu |
| **Institution** | Xiaohongshu Inc. / Shanghai Jiao Tong University / Fudan University |
| **Date** | Mar 2, 2026 |
| **arXiv** | [2603.01590](https://arxiv.org/abs/2603.01590) |

**Abstract:** Click-through rate (CTR) models in advertising and recommendation systems rely heavily on item ID embeddings, which struggle in item cold-start settings. We present IDProxy, a solution that leverages multimodal large language models (MLLMs) to generate proxy embeddings from rich content signals, enabling effective CTR prediction for new items without usage data. These proxies are explicitly aligned with the existing ID embedding space and are optimized end-to-end under CTR objectives together with the ranking model, allowing seamless integration into existing large-scale ranking pipelines. Offline experiments and online A/B tests demonstrate the effectiveness of IDProxy, which has been successfully deployed in both Content Feed and Display Ads features of Xiaohongshu's Explore Feed, serving hundreds of millions of users daily.

**Key Innovations:**
- Uses MLLM (InternVL) to generate proxy item embeddings for cold-start CTR
- Two-stage coarse-to-fine alignment: contrastive pre-training + end-to-end CTR fine-tuning
- Structural reuse: injects proxy embeddings into Atomic ID Slots of existing ranker
- Deployed at Xiaohongshu (300M+ MAU) serving Content Feed and Display Ads
- +1.93% Advertiser Value, +1.28% impressions in online A/B tests

---

### 1.5 GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation

| Field | Details |
|-------|---------|
| **Title** | GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation |
| **Authors** | Jun Zhang, Yi Li, Yue Liu, Changping Wang, Yuan Wang, Yuling Xiong, Xun Liu, Haiyang Wu, Qian Li, Enming Zhang, Jiawei Sun, Xin Xu, Zishuai Zhang, Ruoran Liu, Suyuan Huang, Zhaoxin Zhang, Zhengkai Guo, Shuojin Yang, Meng-Hao Guo, Huan Yu, Jie Jiang, Shi-Min Hu |
| **Institution** | Tencent (Weixin Channels) |
| **Date** | Nov 13, 2025 (revised Feb 12, 2026) |
| **arXiv** | [2511.10138](https://arxiv.org/abs/2511.10138) |

**Abstract:** As an intelligent infrastructure connecting users with commercial content, advertising recommendation systems play a central role in information flow and value creation within the digital economy. However, existing multi-stage advertising recommendation systems suffer from objective misalignment and error propagation, making it difficult to achieve global optimality, while unified generative recommendation models still struggle to meet the demands of practical industrial applications. To address these issues, we propose GPR (Generative Pre-trained Recommender), the first one-model framework that redefines advertising recommendation as an end-to-end generative task, replacing the traditional cascading paradigm with a unified generative approach. To realize GPR, we introduce three key innovations spanning unified representation, network architecture, and training strategy. First, we design a unified input schema and tokenization method tailored to advertising scenarios, mapping both ads and organic content into a shared multi-level semantic ID space. Second, we develop the Heterogeneous Hierarchical Decoder (HHD), a dual-decoder architecture that decouples user intent modeling from ad generation. Finally, we propose a multi-stage joint training strategy that integrates Multi-Token Prediction (MTP), Value-Aware Fine-Tuning and the Hierarchy Enhanced Policy Optimization (HEPO) algorithm. GPR has been fully deployed in the Tencent Weixin Channels advertising system.

**Key Innovations:**
- First one-model generative framework replacing the traditional cascading ad recommendation paradigm
- RQ-Kmeans+ quantization for shared semantic ID space across heterogeneous content
- Heterogeneous Hierarchical Decoder (HHD): dual-decoder decoupling user intent from ad generation
- Multi-stage training: MTP + Value-Aware Fine-Tuning + HEPO algorithm
- Fully deployed in Tencent Weixin Channels (WeChat) advertising system

---

### 1.6 GenLI: Generative Long-term User Interest Modeling for Click-Through Rate Prediction

| Field | Details |
|-------|---------|
| **Title** | Generative Long-term User Interest Modeling for Click-Through Rate Prediction |
| **Authors** | Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang |
| **Institution** | (Industry lab, likely Alibaba/DingTalk based on author affiliations) |
| **Date** | May 15, 2026 |
| **arXiv** | [2605.15905](https://arxiv.org/abs/2605.15905) |

**Abstract:** Modeling long-term user interests with massive historical user behaviors enhances click-through rate (CTR) prediction performance in advertising and recommendation systems. Typically, a two-stage framework is widely adopted, where a general search unit (GSU) first retrieves top-k relevant behaviors towards the target item, and an exact search unit (ESU) generates interest features via tailored attention. However, current target-centered GSU would ignore other latent user interests, leading to incomplete and biased interest features. Additionally, the matching-based retrieval process in GSUs depends on the pairwise similarity score between target item and each historical behavior, which not only becomes time-consuming for online services as user behaviors continue to grow, but also overlooks the interaction information among user behaviors. To combat these problems, we propose GenLI for CTR prediction. GenLI consists of an interest generation module (IGM), a behavior retrieval module (BRM), and an interest fusion module (IFM). The IGM generates multiple interest distributions to indicate different aspects of real-time user interests, which is target-independent and incorporates interaction information among behaviors, ensuring complete and diverse interest features. The BRM selects related behaviors via a simple lookup operation, reducing the time complexity for weighting each behavior to O(1).

**Key Innovations:**
- Generative (vs. retrieval-based) approach to long-term user interest modeling
- Interest Generation Module produces target-independent multiple interest distributions
- O(1) complexity behavior retrieval via simple lookup instead of pairwise similarity
- Addresses bias and incompleteness in target-centered GSU approaches

---

### 1.7 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling

| Field | Details |
|-------|---------|
| **Title** | Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling |
| **Authors** | Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang |
| **Institution** | Tencent Inc. |
| **Date** | Jun 13, 2026 |
| **arXiv** | [2606.15252](https://arxiv.org/abs/2606.15252) |

**Abstract:** User behavior sequence modeling has become a central component in modern click-through rate (CTR) prediction. Over the past years, the community has invested substantial effort into improving how sequences are encoded, from target-aware attention and interest evolution networks to unified architectures that jointly process sequential and non-sequential features. However, a more fundamental question remains under-explored: what should constitute the behavior sequence? Current practice constructs sequences exclusively from positive interactions (clicks, purchases, completions), while the far more abundant implicit negative behaviors (skips, low engagement, scroll-past) are largely underutilized. As gains from longer positive sequences approach diminishing returns, we revisit this underutilized data source within the sequential modeling framework. In this paper, we demonstrate that mixed-polarity behavior sequences, which chronologically interleave positive and negative tokens within a fixed length budget, consistently outperform positive-only sequences across diverse model architectures with negligible additional computational overhead. We further identify a semantic indistinguishability problem inherent to naive polarity embeddings and propose Target-Aware Polarity Fusion (TAPF), a lightweight target-conditioned gating mechanism that provides additional gains by differentiating behavioral evidence. Experiments on three public benchmarks demonstrate consistent improvements of +1.9% to +9.6% relative AUC across five architectures.

**Key Innovations:**
- Challenges the dominant paradigm of positive-only behavior sequences
- Mixed-polarity sequences interleaving positive and negative behaviors
- Target-Aware Polarity Fusion (TAPF) solves semantic indistinguishability of polarity embeddings
- Architecture-agnostic: +1.9% to +9.6% AUC across five different architectures
- Particularly effective for low-activity users and cold-start items

---

### 1.8 CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction

| Field | Details |
|-------|---------|
| **Title** | CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction |
| **Authors** | Heyong He, Yuxuan Hu, Jian Chen, Dingwei Chen, Xiyu Chang, Ngai Wong, Liang Zhang, Linjian Mo, Chengming Li, Chuan Yuan, Zhenan Sun |
| **Institution** | Ant Group / City University of Hong Kong / University of Hong Kong / Sun Yat-sen University / Shenzhen MSU-BIT University / Chinese Academy of Sciences |
| **Date** | Aug 5, 2025 (accepted KDD 2026) |
| **arXiv** | [2508.03668](https://arxiv.org/abs/2508.03668) |

**Abstract:** Click-Through Rate (CTR) prediction, a core task in recommendation systems, estimates user click likelihood using historical behavioral data. Modeling user behavior sequences as text to leverage Language Models (LMs) for this task has gained traction, owing to LMs' strong semantic understanding and contextual modeling capabilities. However, a critical structural gap exists: user behavior sequences consist of discrete actions connected by semantically empty separators, differing fundamentally from the coherent natural language in LM pre-training. This mismatch causes semantic fragmentation, where LM attention scatters across irrelevant tokens instead of focusing on meaningful behavior boundaries and inter-behavior relationships, degrading prediction performance. To address this, we propose CTR-Sink, a novel framework introducing behavior-level attention sinks tailored for recommendation scenarios. Inspired by attention sink theory, it constructs attention focus sinks and dynamically regulates attention aggregation via external information. Specifically, we insert sink tokens between consecutive behaviors, incorporating recommendation-specific signals such as temporal distance to serve as stable attention sinks. Experiments on one industrial dataset and two open-source datasets (MovieLens, Kuairec) validate the method's effectiveness across scenarios.

**Key Innovations:**
- Identifies "semantic fragmentation" as the structural gap between user behavior sequences and natural language
- Behavior-level attention sink tokens inserted between consecutive behaviors
- Two-stage training: attention guidance + inter-sink dependency amplification
- Bridges attention sink theory from LLMs to CTR prediction
- Accepted at KDD 2026

---

## 2. LLM Reasoning & Reinforcement Learning

### 2.1 The Periodic Table of LLM Reasoning: A Structured Survey

| Field | Details |
|-------|---------|
| **Title** | The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes |
| **Authors** | Ashutosh Kumar et al. |
| **Date** | Jun 9, 2026 |
| **arXiv** | [2606.11470](https://arxiv.org/abs/2606.11470) |

**Abstract:** By organizing a rapidly expanding literature, this survey offers a unified view of the current capabilities and limitations of reasoning in LLMs. We also identify emerging research directions, including meta-reasoning, self-evolving reasoning frameworks, multimodal reasoning, and socially grounded reasoning. Overall, this work aims to serve as a reference for developing more robust, interpretable, and generalizable reasoning systems in future language models.

**Key Innovations:**
- Comprehensive taxonomy of LLM reasoning paradigms, methods, and failure modes
- Identifies emerging directions: meta-reasoning, self-evolving reasoning, multimodal reasoning
- Unified "periodic table" organizational framework for the field

---

### 2.2 Large Language Model Reasoning Failures

| Field | Details |
|-------|---------|
| **Title** | Large Language Model Reasoning Failures |
| **Authors** | Peiyang Song, Pengrui Han, Noah Goodman |
| **Institution** | Stanford University |
| **Date** | Feb 5, 2026 (Published TMLR 2026) |
| **arXiv** | [2602.06176](https://arxiv.org/abs/2602.06176) |

**Abstract:** Large Language Models (LLMs) have exhibited remarkable reasoning capabilities, achieving impressive results across a wide range of tasks. Despite these advances, significant reasoning failures persist, occurring even in seemingly simple scenarios. To systematically understand and address these shortcomings, we present the first comprehensive survey dedicated to reasoning failures in LLMs. We introduce a novel categorization framework that distinguishes reasoning into embodied and non-embodied types, with the latter further subdivided into informal (intuitive) and formal (logical) reasoning. In parallel, we classify reasoning failures along a complementary axis into three types: fundamental failures intrinsic to LLM architectures that broadly affect downstream tasks; application-specific limitations that manifest in particular domains; and robustness issues characterized by inconsistent performance across minor variations.

**Key Innovations:**
- First comprehensive survey dedicated exclusively to LLM reasoning failures
- Novel categorization: embodied vs. non-embodied (informal/formal) reasoning
- Failure taxonomy: fundamental, application-specific, and robustness issues
- Published at TMLR 2026 with Survey Certification

---

### 2.3 Agentic Reasoning for Large Language Models

| Field | Details |
|-------|---------|
| **Title** | Agentic Reasoning for Large Language Models |
| **Authors** | Renze Qiu, Xiao Lin, Dongqi Fu, Zihao Li, Mengting Ai, Duo Zhou, Wenxuan Bao, Yunzhe Li, Gaotang Li, Cheng Qian, Yu Wang, Xiangru Tang, Yin Xiao, Liri Fang, Hui Liu, Xianfeng Tang, Yuji Zhang, Chi Wang, Jiaxuan You, Heng Ji, Hanghang Tong, Jingrui He |
| **Institution** | University of Illinois Urbana-Champaign / Microsoft / Various |
| **Date** | Jan 18, 2026 |
| **arXiv** | [2601.12538](https://arxiv.org/abs/2601.12538) |

**Abstract:** Reasoning is a fundamental cognitive process underlying inference, problem-solving, and decision-making. While large language models (LLMs) demonstrate strong reasoning capabilities in closed-world settings, they struggle in open-ended and dynamic environments. Agentic reasoning marks a paradigm shift by reframing LLMs as autonomous agents that plan, act, and learn through continual interaction. In this survey, we organize agentic reasoning along three complementary dimensions: foundational agentic reasoning (planning, tool use, search in stable environments); self-evolving agentic reasoning (feedback, memory, adaptation); and collective multi-agent reasoning (coordination, knowledge sharing, shared goals). Across these layers, we distinguish in-context reasoning (scaling test-time interaction) from post-training reasoning (optimizing via RL and SFT).

**Key Innovations:**
- Three-layer taxonomy of agentic reasoning: foundational, self-evolving, collective multi-agent
- Distinguishes in-context reasoning from post-training reasoning
- Comprehensive survey connecting LLM reasoning to autonomous agent capabilities

---

### 2.4 The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning

| Field | Details |
|-------|---------|
| **Title** | The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning |
| **Authors** | Jing Liang, Hongyao Tang, Yi Ma, Yancheng He, Weixun Wang, Xiaoyang Li, Ju Huang, Wenbo Su, Jinyi Liu, Yan Zheng, Jianye Hao, Bo Zheng |
| **Date** | Jun 28, 2026 |
| **arXiv** | [2606.29526](https://arxiv.org/abs/2606.29526) |

**Abstract:** Reinforcement learning (RL) has gained growing attention in large language model (LLM) post-training, yet RL training remains fragile and can suffer from instability or collapse. One vital cause is training-inference mismatch: LLM adopts separate inference and training engines for generation efficiency and training precision, which in practice exhibits inconsistent probabilities for the same trajectories on training and inference sides, even with synchronized model parameters. This naturally induces a special type of off-policyness ever existing and poisoning the training. In this paper, we point out the objective misalignment neglected by existing works that an effective update to the policy in the training engine not necessarily ensures the improvement of the inference policy. To this end, we propose a new policy optimization objective for LLM RL, named Monotonic Inference Policy Improvement (MIPI). Following this principle, we introduce Monotonic Inference Policy Update (MIPU), a two-step LLM RL framework that constructs sampler-referenced candidate updates and selectively accepts synchronized candidates using an inference-side gap proxy.

**Key Innovations:**
- Identifies training-inference mismatch as fundamental cause of RL instability in LLMs
- Proposes MIPI (Monotonic Inference Policy Improvement) objective
- MIPU framework: sampler-referenced candidate updates + inference-side gap proxy
- Addresses the "mirage" of optimizing training-side policies while inference degrades

---

## 3. Game Theory & Multi-Agent Systems

### 3.1 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games

| Field | Details |
|-------|---------|
| **Title** | Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games |
| **Authors** | Yidong He, Yutao Lai, Pengxu Yang, Jiarui Gan, Jiexin Wang, Yi Cai, Mengchen Zhao |
| **Institution** | South China University of Technology / University of Oxford |
| **Date** | May 6, 2026 (accepted ICML 2026) |
| **arXiv** | [2605.04906](https://arxiv.org/abs/2605.04906) |

**Abstract:** While Large Language Models (LLMs) excel in certain reasoning tasks, they struggle in multi-agent games where the final outcome depends on the joint strategies of all agents. In multi-agent games, the non-stationarity of other agents brings significant challenges on the evaluation of the reasoning process and the credit assignment over multiple reasoning steps. Existing single-agent reinforcement learning (RL) approaches and their multi-agent extensions fail to address these challenges as they do not incorporate other agents in the reasoning process. In this work, we propose Strat-Reasoner, a novel RL-based framework that improves LLMs' strategic reasoning ability in multi-agent games. We introduce a novel recursive reasoning paradigm where an agent's reasoning also integrates other agents' reasoning processes. To provide effective reward signals for the intermediate reasoning sequences, we employ a centralized Chain-of-Thought (CoT) comparison module to evaluate the reasoning quality. Finally, we compute an accurate hybrid advantage and develop a group-relative RL approach to optimize the LLM policy. Experimental results show that Strat-Reasoner substantially improves strategic abilities of underlying LLMs, achieving 22.1% average performance improvements across various multi-agent games.

**Key Innovations:**
- Recursive reasoning paradigm integrating opponents' reasoning into agent's decision-making
- Centralized CoT comparison module for fine-grained intermediate reasoning rewards
- Group-relative RL with hybrid advantage estimation for multi-agent credit assignment
- 22.1% average improvement across diverse multi-agent games
- Accepted at ICML 2026

---

### 3.2 Competitive Information Design in Sequential Search

| Field | Details |
|-------|---------|
| **Title** | Competitive Information Design in Sequential Search |
| **Authors** | Zhicheng Du, Hu Fu, Ying Qin, Zihe Wang |
| **Date** | Jun 2, 2026 |
| **arXiv** | [2606.03527](https://arxiv.org/abs/2606.03527) |

**Abstract:** Advertisements often strategically disclose information to consumers who make decisions on further information acquisition and eventual purchase. Anderson and Renault (2006) model this problem using an information design framework, where the advertiser acts as a sender and the consumer as a receiver. We extend this model to a competitive setting with horizontally differentiated senders competing for a unit-demand receiver. Under costly inspection, the receiver's optimal sequential search action is given by Weitzman's Index Algorithm. We give a method, based on duality arguments, to verify whether a sender's given information strategy constitutes a best response against his competitors. We establish the existence of an equilibrium in the game among senders when the prior distributions have no mass; we also illustrate that such equilibria may exhibit intricate behaviors. Finally, we meticulously characterize symmetric equilibria played by the senders for cases when the prior distributions have monotone increasing densities.

**Key Innovations:**
- Extends information design theory to competitive advertising with sequential consumer search
- Connects information design to Weitzman's Index Algorithm for optimal search
- Establishes equilibrium existence in sender games with massless priors
- Characterizes symmetric equilibria for monotone increasing density priors

---

### 3.3 Multi-Agent Reinforcement Learning for Exploring Dominant Strategies in Games

| Field | Details |
|-------|---------|
| **Title** | A multi-agent reinforcement learning framework for exploring dominant strategies in iterated and evolutionary games |
| **Authors** | (Nature publication, authors not fully extracted) |
| **Institution** | (Nature Communications, 2025) |
| **Date** | Dec 8, 2025 |
| **Link** | [Nature Communications](https://www.nature.com/articles/s41467-025-67178-6) |

**Abstract:** This work proposes a multi-agent reinforcement learning approach to explore dominant strategies in iterated and evolutionary games. Agents are trained by interacting with classic strategies and heuristic strategies, and adaptively adjust the Q-table to maximize two objectives: the relative advantage over opponents and their own payoffs. The approach uncovers the memory-two bilateral reciprocity (MTBR) strategy, which dynamically adapts in repeated games, consistently achieving higher payoffs against nearly all strategies studied. The introduction of MTBR into a large-scale population increases the global payoff, consistent across various payoff structures and population structures.

**Key Innovations:**
- RL-based discovery of dominant strategies in iterated/evolutionary games
- Uncovers memory-two bilateral reciprocity (MTBR) strategy
- MTBR shows evolutionary advantage across diverse payoff and population structures
- Bridges RL, game theory, and evolutionary dynamics

---

## 4. Summary of Key Trends

### Scaling Laws Come to Recommendation
Multiple papers (LLaTTE, GRAB, EST) independently demonstrate that CTR/recommendation sequence modeling follows power-law scaling analogous to LLMs. This is a major emerging theme in 2026.

### Generative Paradigm Shift
GPR (Tencent), GRAB (Baidu), and GenLI represent a fundamental shift from discriminative to generative architectures for advertising recommendation, mirroring the broader LLM-to-agentic transition.

### Multimodal LLMs Meet CTR
IDProxy (Xiaohongshu) demonstrates that MLLM hidden states can serve as effective proxy embeddings for cold-start items, bridging multimodal understanding and collaborative filtering.

### Sequence Data Reimagined
Beyond Positive Signals (Tencent) challenges the positive-only sequence paradigm, while CTR-Sink (Ant Group) addresses the structural mismatch between behavior sequences and natural language.

### Strategic Reasoning as RL Frontier
Strat-Reasoner (ICML 2026) and MIPI represent the cutting edge of applying RL to LLM reasoning — the former in adversarial multi-agent games, the latter addressing the training-inference gap.

---

*Report generated on 2026-07-10 from arXiv searches.*
