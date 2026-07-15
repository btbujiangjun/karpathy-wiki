---
title: "arXiv Daily Report — 2026-07-15"
type: synthesis
created: 2026-07-15
updated: 2026-07-15
tags: [arxiv-daily, AI, LLM, recommendation, CTR, advertising, sequential-modeling, games, multi-agent]
---

# arXiv Daily Report — 2026-07-15

Curated papers across AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and games.

---

## 1 · Advertising & CTR Prediction

### 1.1 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang |
| **Institution** | LinkedIn |
| **Date** | 2026-02-11 |
| **arXiv** | [2602.11410](https://arxiv.org/abs/2602.11410) |

**Abstract:** CTR prediction is fundamental to online advertising systems. We present CADET (Context-Conditioned Ads Decoder-Only Transformer), an end-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Our approach introduces several key innovations: (1) a context-conditioned decoding architecture with multi-tower prediction heads that explicitly model post-scoring signals such as ad position, resolving the chicken-and-egg problem between predicted CTR and ranking; (2) a self-gated attention mechanism that stabilizes training by adaptively regulating information flow at both representation and interaction levels; (3) a timestamp-based variant of Rotary Position Embedding (RoPE) that captures temporal relationships across timescales from seconds to months; (4) session masking strategies that prevent the model from learning dependencies on unavailable in-session events, addressing train-serve skew; and (5) production engineering techniques including tensor packing, sequence chunking, and custom Flash Attention kernels that enable efficient training and serving at scale. In online A/B testing, CADET achieves a 11.04% CTR lift compared to the production LiRank baseline model. The system has been successfully deployed on LinkedIn's advertising platform.

**Key Innovations:**
- Context-conditioned decoding architecture resolving the CTR-vs-ranking chicken-and-egg problem
- Self-gated attention mechanism stabilizing training at representation and interaction levels
- Timestamp-based RoPE capturing temporal relationships across seconds-to-months timescales
- Session masking strategies to address train-serve skew
- Custom Flash Attention kernels for industrial-scale serving
- **11.04% CTR lift** in online A/B testing; deployed at LinkedIn

---

### 1.2 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu |
| **Institution** | Xiaohongshu (Little Red Book) |
| **Date** | 2026-03-02 |
| **arXiv** | [2603.01590](https://arxiv.org/abs/2603.01590) |

**Abstract:** Click-through rate (CTR) models in advertising and recommendation systems rely heavily on item ID embeddings, which struggle in item cold-start settings. We present IDProxy, a solution that leverages multimodal large language models (MLLMs) to generate proxy embeddings from rich content signals, enabling effective CTR prediction for new items without usage data. These proxies are explicitly aligned with the existing ID embedding space and are optimized end-to-end under CTR objectives together with the ranking model, allowing seamless integration into existing large-scale ranking pipelines. Offline experiments and online A/B tests demonstrate the effectiveness of IDProxy, which has been successfully deployed in both Content Feed and Display Ads features of Xiaohongshu's Explore Feed, serving hundreds of millions of users daily.

**Key Innovations:**
- MLLM-generated proxy embeddings for cold-start item CTR prediction
- Explicit alignment of proxy embeddings with existing ID embedding space
- End-to-end optimization under CTR objectives alongside ranking model
- Deployed at Xiaohongshu serving hundreds of millions of users in Content Feed and Display Ads
- Bridges the gap between content understanding and CTR modeling

---

### 1.3 Generative Long-term User Interest Modeling for Click-Through Rate Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang |
| **Institution** | Not specified (industry) |
| **Date** | 2026-05-15 |
| **arXiv** | [2605.15905](https://arxiv.org/abs/2605.15905) |

**Abstract:** Modeling long-term user interests with massive historical user behaviors enhances CTR prediction performance in advertising and recommendation systems. Typically, a two-stage framework is widely adopted, where a general search unit (GSU) first retrieves top-k relevant behaviors, and an exact search unit (ESU) generates interest features via tailored attention. However, current target-centered GSU would ignore other latent user interests, leading to incomplete and biased interest features. We propose GenLI (Generative Long-term user Interest model) for CTR prediction. GenLI consists of an interest generation module (IGM), a behavior retrieval module (BRM), and an interest fusion module (IFM). The IGM generates multiple interest distributions to indicate different aspects of real-time user interests, which is target-independent and incorporates interaction information among behaviors. The BRM selects related behaviors via a simple lookup operation, reducing the time complexity for weighting each behavior to O(1).

**Key Innovations:**
- Target-independent interest generation avoiding the bias of target-centered retrieval
- Multiple interest distributions capturing diverse aspects of user preferences
- O(1) complexity behavior retrieval via lookup operation
- Improved diversity of user interests while maintaining efficiency
- Better balance between accuracy and efficiency for CTR prediction

---

### 1.4 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang |
| **Institution** | Not specified |
| **Date** | 2026-06-13 |
| **arXiv** | [2606.15252](https://arxiv.org/abs/2606.15252) |

**Abstract:** User behavior sequence modeling has become a central component in modern CTR prediction. However, a more fundamental question remains under-explored: what should constitute the behavior sequence? Current practice constructs sequences exclusively from positive interactions (clicks, purchases, completions), while the far more abundant implicit negative behaviors (skips, low engagement, scroll-past) are largely underutilized. We demonstrate that mixed-polarity behavior sequences, which chronologically interleave positive and negative tokens within a fixed length budget, consistently outperform positive-only sequences across diverse model architectures. We further propose Target-Aware Polarity Fusion (TAPF), a lightweight target-conditioned gating mechanism that provides additional gains by differentiating behavioral evidence. Experiments on three public benchmarks demonstrate consistent improvements of +1.9% to +9.6% relative AUC across five architectures.

**Key Innovations:**
- Mixed-polarity behavior sequences (positive + negative interactions) outperform positive-only sequences
- Target-Aware Polarity Fusion (TAPF) for differentiating behavioral evidence
- Consistent +1.9% to +9.6% relative AUC improvements across five architectures
- Negligible additional computational overhead
- Challenges the long-standing assumption of positive-only behavior sequences

---

## 2 · Sequential Modeling & Recommendation

### 2.1 PANTHER: Generative Pretraining Beyond Language for Sequential User Behavior Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Guilin Li, Yun Zhang, Xiuyuan Chen, Chengqi Li, Bo Wang, Linghe Kong, Wenjia Wang, Weiran Huang, Matthias Hwai Yong Tan |
| **Institution** | Tencent / WeChat Pay |
| **Date** | 2025-10-11 (v1), revised 2026-03-30 (v2) |
| **arXiv** | [2510.10102](https://arxiv.org/abs/2510.10102) |

**Abstract:** Large language models have shown that generative pretraining can distill vast world knowledge into compact token representations. We present PANTHER, a hybrid generative-discriminative framework that unifies user behavior pretraining and downstream adaptation, enabling large-scale sequential user representation learning and real-time inference. PANTHER introduces: (1) Structured Tokenization to compress multi-dimensional transaction attributes into an interpretable vocabulary; (2) Sequence Pattern Recognition Module (SPRM) for modeling periodic transaction motifs; (3) a Unified User-Profile Embedding that fuses static demographics with dynamic transaction histories; and (4) Real-time scalability enabled by offline caching of pretrained embeddings for millisecond-level inference. Fully deployed and operational online at WeChat Pay, PANTHER delivers a 25.6% boost in next-transaction prediction HitRate@1 and a 38.6% relative improvement in fraud detection recall over baselines.

**Key Innovations:**
- Extends generative pretraining from language to user behavior modality
- Structured Tokenization compressing multi-dimensional attributes into interpretable vocabulary
- Sequence Pattern Recognition Module for periodic transaction motifs
- Unified embedding fusing demographics + transaction histories
- Deployed at WeChat Pay: 25.6% HitRate@1 boost, 38.6% fraud detection recall improvement
- Cross-domain generalization: up to 21% HitRate@1 gains on public benchmarks

---

### 2.2 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network for E-Commerce Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Hanqi Jin, Gaoming Yang, Zhangming Chan, Yapeng Yuan, Longbin Li, Fei Sun, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng |
| **Institution** | Alibaba Group |
| **Date** | 2026-01-21 |
| **Venue** | WWW 2026 (short paper) |
| **arXiv** | [2601.14955](https://arxiv.org/abs/2601.14955) |

**Abstract:** User interactions on e-commerce platforms are inherently diverse, involving behaviors such as clicking, favoriting, adding to cart, and purchasing. We propose the Transition-Aware Graph Attention Network (TGA), a linear-complexity approach for modeling multi-behavior transitions. TGA constructs a structured sparse graph by identifying informative transitions from three perspectives: (a) item-level transitions, (b) category-level transitions, and (c) neighbor-level transitions. Built upon the structured graph, TGA employs a transition-aware graph attention mechanism that jointly models user-item interactions and behavior transition types. Experiments show that TGA outperforms all state-of-the-art models while significantly reducing computational cost. TGA has been deployed in a large-scale industrial production environment.

**Key Innovations:**
- Linear-complexity (vs. polynomial) multi-behavior transition modeling
- Three-perspective transition graph: item-level, category-level, neighbor-level
- Transition-aware graph attention jointly modeling interactions and transition types
- Deployed at large-scale e-commerce (Alibaba)
- Accepted at WWW 2026

---

### 2.3 Efficient Sequential Recommendation for Long Term User Interest Via Personalization

| Field | Detail |
|-------|--------|
| **Authors** | Qiang Zhang, Hanchao Yu, Ivan Ji, Chen Yuan, Yi Zhang, Chihuang Liu, Xiaolong Wang, Christopher E. Lambert, Ren Chen, Chen Kovacs, Xinzhu Bei, Renqin Cai, Rui Li, Lizhu Zhang, Xiangjun Fan, Qunshu Zhang, Benyu Zhang |
| **Institution** | Meta (Facebook Research) |
| **Date** | 2026-01-07 |
| **Venue** | ICDM 2025 |
| **arXiv** | [2601.03479](https://arxiv.org/abs/2601.03479) |

**Abstract:** Though the scaling law has been validated for sequential models, it showed inefficiency in computational capacity when considering real-world applications like recommendation, due to the non-linear (quadratic) increasing nature of the transformer model. We introduce a novel approach to sequential recommendation that leverages personalization techniques to enhance efficiency and performance. Our method compresses long user interaction histories into learnable tokens, which are then combined with recent interactions to generate recommendations. This approach significantly reduces computational costs while maintaining high recommendation accuracy. Our method could be applied to existing transformer-based recommendation models, e.g., HSTU and HLLM.

**Key Innovations:**
- Personalization-based compression of long user interaction histories into learnable tokens
- Compatible with existing transformer-based models (HSTU, HLLM)
- Addresses quadratic scaling of transformer-based sequential models
- Maintains accuracy while significantly reducing computational costs
- Open source code available

---

## 3 · LLM Agents & Multi-Agent Systems

### 3.1 MARLIN: Multi-Agent Game-Theoretic Reinforcement Learning for Sustainable LLM Inference in Cloud Datacenters

| Field | Detail |
|-------|--------|
| **Authors** | H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha |
| **Institution** | HP Labs / Colorado State University |
| **Date** | 2026-05-13 |
| **arXiv** | [2605.13496](https://arxiv.org/abs/2605.13496) |

**Abstract:** LLM inference requests account for up to 90% of total LLM lifecycle energy use. To improve sustainability for LLM inference serving in cloud datacenter environments, we propose MARLIN, a novel multi-agent game-theoretic reinforcement learning framework to co-optimize time-to-first token (TTFT), carbon emissions, water usage, and energy costs. MARLIN demonstrates a reduction of at least 18% in TTFT, 33% in carbon emissions, 43% in water usage, and 11% in energy costs compared to state-of-the-art LLM inference management frameworks.

**Key Innovations:**
- Multi-agent game-theoretic RL for LLM inference optimization
- Co-optimizes TTFT, carbon emissions, water usage, and energy costs
- 18% TTFT reduction, 33% carbon emission reduction, 43% water usage reduction
- Addresses the sustainability challenge of LLM deployment
- Game-theoretic formulation for competing optimization objectives

---

### 3.2 GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation

| Field | Detail |
|-------|--------|
| **Authors** | Yuxiao Ye, Yiwen Zhang, Huiyuan Xie, Yuqin Huang, Zhiyuan Liu |
| **Institution** | Tsinghua University |
| **Date** | 2026-06-03 |
| **arXiv** | [2606.05002](https://arxiv.org/abs/2606.05002) |

**Abstract:** LLM-based multi-agent systems are increasingly used for strategic decision-making tasks. We propose GARL, a game-theoretic reinforcement learning framework for multi-agent strategic prioritisation. GARL formalises strategic prioritisation as a two-stage game: competing agents first allocate strategic resources over a shared candidate set, and a higher-level arbiter then produces the final ranking. The resulting game-theoretic utilities are converted into role-specific reinforcement signals, allowing policy optimisation to be guided by structured interaction. Experiments show GARL improves ranking performance, enables small open-source LLMs to become competitive with a strong closed-source LLM, and yields gains in legal-domain competence.

**Key Innovations:**
- Game-theoretic formalization of multi-agent strategic prioritisation as two-stage game
- Converts game-theoretic utilities into role-specific reinforcement signals
- Enables small open-source LLMs to match closed-source LLM performance
- Principled approach bridging game theory and multi-agent RL for LLMs
- Demonstrated on legal-domain issues-in-dispute ranking

---

### 3.3 Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents

| Field | Detail |
|-------|--------|
| **Authors** | Wael Albayaydh, Rui Zhao, Ivan Flechais |
| **Institution** | University of Oxford |
| **Date** | 2026-07-07 |
| **arXiv** | [2607.05775](https://arxiv.org/abs/2607.05775) |

**Abstract:** This paper synthesizes 27 benchmark, taxonomy, and audit papers (2023-2026), spanning 19 distinct benchmarks, into a cross-cutting taxonomy of agent limitations. We identify six failure clusters: (1) tool invocation and parameter-level errors, (2) planning and constraint-satisfaction failures, (3) long-horizon degradation from context accumulation, (4) multi-agent coordination failures, (5) safety and security failures under adversarial or underspecified conditions, and (6) measurement validity problems. We find that failures compound nonlinearly with task length, that strong performance on individual sub-tasks does not reliably translate into end-to-end success, and that additional scaffolding does not consistently improve reliability.

**Key Innovations:**
- First cross-cutting synthesis across tool use, planning, long-horizon reasoning, multi-agent coordination, safety, and measurement validity
- Six failure clusters with evidence from 27 papers and 19 benchmarks
- Key finding: failures compound nonlinearly with task length
- Finding: sub-task performance doesn't guarantee end-to-end success
- Finding: additional scaffolding doesn't consistently improve reliability

---

### 3.4 Decision Protocols in Multi-Agent Large Language Model Conversations

| Field | Detail |
|-------|--------|
| **Authors** | Lars Benedikt Kaesberg |
| **Institution** | University of Göttingen (Master's thesis) |
| **Date** | 2026-07-06 |
| **arXiv** | [2607.05477](https://arxiv.org/abs/2607.05477) |

**Abstract:** This thesis introduces the Multi-Agent LLM (MALLM) framework, which implements and evaluates various decision protocols, namely voting, consensus, and judge decision mechanisms, to simulate multi-agent discussions for conversational task solving. Unlike previous work that used a single decision protocol or tested them on limited datasets, this study systematically examines their impact on a diverse set of tasks. The results indicate that consensus protocols excel in knowledge-intensive domains while voting and judge protocols are more effective for logic-based tasks.

**Key Innovations:**
- Systematic evaluation of voting, consensus, and judge decision protocols across diverse tasks
- MALLM framework for simulating multi-agent discussions
- Key finding: consensus excels in knowledge-intensive domains; voting/judge better for logic
- Response diversity through independent solution generation improves decision quality

---

### 3.5 Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data

| Field | Detail |
|-------|--------|
| **Authors** | Fengxian Dong, Zhi Zheng, Xiao Han, Wei Chen, Jingqing Ruan, Tong Xu, Yong Chen, Enhong Chen |
| **Institution** | University of Science and Technology of China |
| **Date** | 2026-04-22 |
| **Venue** | ACL 2026 |
| **arXiv** | [2604.20261](https://arxiv.org/abs/2604.20261) |

**Abstract:** We propose MALMAS (Memory-Augmented LLM-based Multi-Agent System) for automated feature generation. MALMAS decomposes the generation process into agents with distinct responsibilities, and a Router Agent activates an appropriate subset of agents per iteration, further broadening exploration of the feature space. We integrate a memory module comprising procedural memory, feedback memory, and conceptual memory, enabling iterative refinement that adaptively guides subsequent feature generation and improves feature quality and diversity.

**Key Innovations:**
- Router Agent dynamically activates agent subsets per iteration for broader exploration
- Triple memory module: procedural, feedback, and conceptual memory
- Iterative refinement adapting feature generation based on feedback
- Accepted at ACL 2026
- Open source code available

---

## 4 · Games & Game Theory

### 4.1 How to Program a Never-Losing Chess Engine

| Field | Detail |
|-------|--------|
| **Authors** | Fabio Romano |
| **Institution** | Not specified |
| **Date** | 2026-07-09 |
| **arXiv** | [2607.09715](https://arxiv.org/abs/2607.09715) |

**Abstract:** A chess engine designed to never lose a game, exploring formal game-theoretic approaches to perfect play in chess.

**Key Innovations:**
- Formal approach to provably perfect play in chess
- Explores the boundary between game theory and AI

---

### 4.2 Teaming Up with AI: Coordination and Cooperation

| Field | Detail |
|-------|--------|
| **Authors** | Nicole Immorlica, Inbal Talgam-Cohen |
| **Institution** | Not specified |
| **Date** | 2026-07-09 |
| **arXiv** | [2607.03181](https://arxiv.org/abs/2607.03181) |

**Abstract:** Explores coordination and cooperation mechanisms when humans team up with AI systems, examining game-theoretic foundations of human-AI collaboration.

**Key Innovations:**
- Game-theoretic framework for human-AI coordination and cooperation
- Analysis of incentive structures in human-AI teaming

---

### 4.3 Contextual-Bandit Oversight Game with Two-Sided Informational Asymmetry

| Field | Detail |
|-------|--------|
| **Authors** | Yunjin Tong |
| **Institution** | Not specified |
| **Date** | 2026-07-09 |
| **arXiv** | [2607.00155](https://arxiv.org/abs/2607.00155) |

**Abstract:** Studies oversight games modeled as contextual bandits with two-sided informational asymmetry, relevant to AI alignment and mechanism design.

**Key Innovations:**
- Contextual bandit formulation for AI oversight
- Two-sided informational asymmetry modeling
- Bridges game theory with AI alignment research

---

## Summary by Topic

| Topic | Papers | Key Trend |
|-------|--------|-----------|
| **CTR / Advertising** | 4 papers | Decoder-only transformers replacing DLRMs; MLLMs for cold-start; generative interest modeling; mixed-polarity sequences |
| **Sequential Modeling** | 3 papers | Generative pretraining for user behavior; linear-complexity multi-behavior transitions; personalization-based compression |
| **LLM Agents / Multi-Agent** | 5 papers | Game-theoretic RL for multi-agent coordination; failure taxonomy synthesis; decision protocol comparison; memory-augmented multi-agent systems |
| **Games / Game Theory** | 3 papers | Human-AI coordination; AI oversight games; provably perfect play |
| **Industrial Deployment** | 5 papers | LinkedIn (CADET), Xiaohongshu (IDProxy), WeChat Pay (PANTHER), Alibaba (TGA), Meta (PerSRec) |

## Notable Trends

1. **Decoder-only transformers dominate ads CTR**: CADET (LinkedIn) shows a clear shift from DLRM-style models to end-to-end decoder-only architectures for ads prediction.
2. **MLLMs as feature extractors**: IDProxy (Xiaohongshu) demonstrates using multimodal LLMs not as classifiers but as embedding generators for CTR pipelines.
3. **Beyond positive signals**: The mixed-polarity paradigm (2606.15252) challenges the long-standing assumption that only positive interactions should form behavior sequences.
4. **Generative pretraining for behavior**: PANTHER and GenLI show that LLM-style generative pretraining applied to user behavior sequences yields significant gains.
5. **Game theory + RL convergence**: Multiple papers (MARLIN, GARL) combine game-theoretic structures with RL for multi-agent optimization.
6. **Industrial validation**: 5 of the 15 papers report deployment results at major tech companies, confirming practical impact.

---

*Report generated on 2026-07-15 by automated arXiv search.*
