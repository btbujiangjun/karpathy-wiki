---
title: arXiv AI Paper Search Report
type: synthesis
created: 2026-07-23
updated: 2026-07-23
tags: [arxiv, ai, llm, recommendation, ctr, advertising, sequential-modeling, games, reinforcement-learning]
---

# arXiv Recent Papers Report — 2026-07-23

Curated report of recent arXiv papers across AI, LLMs, Recommendation Systems, CTR Prediction, Advertising, Sequential Modeling, and Game AI.

---

## 1. Large Language Models (LLMs)

### 1.1 Survey: Accelerating Masked Diffusion LLMs
- **Title**: Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques
- **Authors**: Not specified (survey)
- **Institution**: Not specified
- **Abstract**: Provides a unified latency decomposition framework and comprehensive taxonomy of acceleration techniques for masked diffusion LLMs to address inference efficiency challenges.
- **Key Innovations**: Introduced unified latency decomposition framework for dLLMs; categorized acceleration techniques across algorithms, architectures/systems, and inference-time scaling axes; provided reproducible benchmarking guidelines.
- **arXiv**: [2607.12829](https://arxiv.org/abs/2607.12829)

### 1.2 Survey: Dynamic Agent Skills
- **Title**: Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries
- **Authors**: Not specified (survey)
- **Institution**: Not specified
- **Abstract**: Comprehensive survey and taxonomy of dynamic skill libraries for LLM agents, establishing a lifecycle-based framework for managing evolving reusable procedures.
- **Key Innovations**: Six-sense taxonomy for skill artifacts; eight-stage lifecycle architecture for skill management; standardized schema for comparing dynamic library updates in agent systems.
- **arXiv**: [2607.10113](https://arxiv.org/abs/2607.10113)

### 1.3 Survey: LLM Watermarking
- **Title**: A Survey on LLM Watermarking: Theory and Deployment
- **Authors**: Not specified (survey)
- **Institution**: Not specified
- **Abstract**: Deployment-oriented survey of LLM watermarking techniques, categorizing methods by operational requirements, threat models, and security-utility trade-offs.
- **Key Innovations**: Systematic taxonomy for LLM watermarking; analysis of security-utility trade-offs; review of attack/evasion strategies; practical deployment guidance.
- **arXiv**: [2607.10103](https://arxiv.org/abs/2607.10103)

### 1.4 Survey: KV Cache Optimization for LLM Serving
- **Title**: Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization
- **Authors**: Not specified (survey)
- **Institution**: Not specified
- **Abstract**: Comprehensive taxonomy of system-aware KV cache optimization techniques for efficient LLM serving.
- **Key Innovations**: Three-dimensional framework (temporal, spatial, structural) for KV cache optimization; analysis of cross-behavior co-design; future research directions for LLM serving infrastructure.
- **arXiv**: [2607.08057](https://arxiv.org/abs/2607.08057)

### 1.5 Survey: Memory Compaction in LLMs
- **Title**: What to Keep, What to Forget: A Rate-Distortion View of Memory Compaction in LLMs and Agents
- **Authors**: Not specified (survey)
- **Institution**: Not specified
- **Abstract**: Unified rate-distortion framework for memory compaction in LLMs and agents with taxonomy and benchmarks.
- **Key Innovations**: Rate-distortion theoretical framework for memory compaction; seven-axis taxonomy for cross-layer memory management; new benchmarks and design principles for compaction-aware LLM systems.
- **arXiv**: [2607.08032](https://arxiv.org/abs/2607.08032)

### 1.6 Survey: LLMs for Medical Reasoning
- **Title**: Aligning Clinical Needs and AI Capabilities: A Survey on LLMs for Medical Reasoning
- **Authors**: Not specified (survey)
- **Institution**: Not specified
- **Abstract**: Bridges clinical competency levels with computational reasoning patterns in medical LLMs, supported by a new multi-level benchmark.
- **Key Innovations**: Dual-view framework mapping Miller's Pyramid to computational reasoning; five-level medical reasoning benchmark; evaluation of 18 SOTA models identifying performance gaps.
- **arXiv**: [2607.07761](https://arxiv.org/abs/2607.07761)

### 1.7 Survey: Understanding LLMs
- **Title**: Understanding Large Language Models
- **Authors**: Not specified (survey)
- **Institution**: Not specified
- **Abstract**: Comprehensive overview of LLM mechanisms, emergent cognitive capabilities, and debate on machine understanding vs pattern memorization.
- **Key Innovations**: Synthesizes LLM architecture and cognitive-like behaviors; provides nuanced philosophical argument against reductionist views of AI cognition.
- **arXiv**: [2607.01006](https://arxiv.org/abs/2607.01006)

### 1.8 LLM-as-a-Verifier Framework
- **Title**: LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: Identifies verification (determining correctness of a solution) as a new scaling axis for LLMs. Introduces a framework providing fine-grained feedback for agentic tasks without additional training.
- **Key Innovations**: Novel verification scaling axis; fine-grained feedback for agentic tasks; no additional training required.
- **arXiv**: Referenced in DeepPaper weekly (2026-07-08)

---

## 2. Recommendation Systems

### 2.1 Agentic Recommender Systems Roadmap
- **Title**: Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems
- **Authors**: Xinyu Lin, Yashar Deldjoo, Sunhao Dai, Honghui Bao et al.
- **Institution**: Not specified
- **Abstract**: Survey providing a comprehensive roadmap for LLM agent-based recommender systems shifting from static ranking to autonomous interactive systems.
- **Key Innovations**: Comprehensive framework for agentic recsys; taxonomy of autonomous information seeking behaviors; analysis of reasoning, planning, and acting in recommendation.
- **arXiv**: [2607.04433](https://arxiv.org/abs/2607.04433)

### 2.2 Multimodal Memory-Enhanced Agent for Rec
- **Title**: Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation
- **Authors**: Hao Cong, Huizu Lin, Zihan Wang, Chengkai Huang et al.
- **Institution**: Not specified
- **Abstract**: Extends LLM-based agentic recsys with multimodal inputs and fine-grained memory updates to address limitations of text-centric approaches.
- **Key Innovations**: Multimodal agent collaboration; fine-grained memory update mechanisms; visual+textual preference modeling.
- **arXiv**: [2607.07108](https://arxiv.org/abs/2607.07108)

### 2.3 Recursive Refinement for Sequential Rec
- **Title**: RecRec: Recursive Refinement for Sequential Recommendation
- **Authors**: Pervez Shaik, Prosenjit Biswas, Abhinav Thorat, Ravi Kolla et al.
- **Institution**: Not specified
- **Abstract**: Revives recursive refinement in sequential recsys, challenging single-pass encoding paradigm that relies on increasingly deep architectures.
- **Key Innovations**: Recursive refinement mechanism replacing single-pass encoding; iterative preference capture without deeper architectures.
- **arXiv**: [2607.10541](https://arxiv.org/abs/2607.10541)

### 2.4 Generative Retrieval (DaV-Gen)
- **Title**: DaV-Gen: End-to-End Generative Retrieval via Draft-and-Verify
- **Authors**: Meng Zhao, Chunmei Liu, Qinyong Wang
- **Institution**: Not specified
- **Abstract**: Proposes draft-and-verify paradigm for generative retrieval in industrial search/rec/advertising, replacing traditional multi-stage cascade architectures.
- **Key Innovations**: Draft-and-verify generative retrieval; end-to-end framework replacing coarse-to-fine retrieval-ranking pipelines.
- **arXiv**: [2607.08365](https://arxiv.org/abs/2607.08365)

### 2.5 LLM for Offline Rec Evaluation
- **Title**: User Preference Induction with LLMs for Offline Top-N Recommendation Evaluation
- **Authors**: David Otero, Javier Parapar
- **Institution**: Not specified
- **Abstract**: Uses LLMs to induce user preferences for offline evaluation of top-N recommender systems, addressing incomplete relevance information in benchmark datasets.
- **Key Innovations**: LLM-based preference induction for offline evaluation; addresses unjudged items problem in benchmarks.
- **arXiv**: [2607.11354](https://arxiv.org/abs/2607.11354)

### 2.6 ZoRRO: Zero-Weight Personalized News Rec
- **Title**: ZoRRO: A Zero-Weight Personalized Recommender System for Scalable News Recommendation
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: Training-free, zero-weight framework for personalized news recommendation that outperforms neural baselines in offline ranking.
- **Key Innovations**: Zero-weight, training-free paradigm; scalable deployment architecture; competitive with neural baselines.
- **arXiv**: [2607.10910](https://arxiv.org/abs/2607.10910)

### 2.7 Long-History Transformers for Ad Ranking
- **Title**: Long-History User Transformers for Real-Time Ad Ranking
- **Authors**: Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova et al.
- **Institution**: Not specified
- **Abstract**: Addresses the challenge of using long interaction histories for CTR prediction under tight serving latency constraints (few hundred milliseconds) in online advertising.
- **Key Innovations**: Efficient transformer for long user histories under real-time latency constraints; practical deployment for ad ranking.
- **arXiv**: [2607.14331](https://arxiv.org/abs/2607.14331)

### 2.8 LLM-based Cold-Start Rec Diagnosis
- **Title**: Diagnosing and Mitigating Retrieval Bottlenecks in LLM-Based Cold-Start Recommendation
- **Authors**: Zhe Dong, Fang Qin, Manish Shah, Yicheng Wang
- **Institution**: Not specified
- **Abstract**: Tests LLM rerankers in cold-start/long-tail regimes across a five-domain benchmark, diagnosing retrieval bottlenecks.
- **Key Innovations**: Five-domain benchmark for cold-start evaluation; diagnosis of LLM reranker limitations; mitigation strategies.
- **arXiv**: [2606.29947](https://arxiv.org/abs/2606.29947)

### 2.9 Diffusion Generative Reasoning Re-ranker
- **Title**: Diffusion-GR2: Diffusion Generative Reasoning Re-ranker
- **Authors**: Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, Mingfu Liang et al.
- **Institution**: Not specified
- **Abstract**: Addresses the speed bottleneck of autoregressive reasoning re-rankers in recommendation by using diffusion-based generation.
- **Key Innovations**: Diffusion-based reasoning re-ranker replacing slow AR decoders; chain-of-thought before re-ordering with parallel generation.
- **arXiv**: [2607.01170](https://arxiv.org/abs/2607.01170)

### 2.10 Topology-Aware Tokenization for Gen Rec
- **Title**: Topology-Aware Tokenization for Generative Recommendation
- **Authors**: Yaokun Liu, Yifan Liu, Zhenrui Yue, Gyuseok Lee et al.
- **Institution**: Not specified
- **Abstract**: Addresses topology distortion in item tokenization for generative recommendation (autoregressive sequential rec reformulation).
- **Key Innovations**: Topology-aware tokenization preserving item relationships; addresses overlooked issue in gen-rec paradigm.
- **arXiv**: [2607.18600](https://arxiv.org/abs/2607.18600)

### 2.11 Multimodal Sequential Rec with Denoising
- **Title**: Beyond Noisy Signals: Dual-Level Denoising for Multi-modal Sequential Recommendation
- **Authors**: Jie Luo, Qi Jin, Xinming Zhang
- **Institution**: Not specified
- **Abstract**: Addresses the Dual-Noise Dilemma in multi-modal sequential recommendation from textual and visual features.
- **Key Innovations**: Dual-level denoising framework for multi-modal SR; addresses both modality noise and behavioral noise.
- **arXiv**: [2607.18786](https://arxiv.org/abs/2607.18786)

### 2.12 ShopX: Foundation Model for Agentic Shopping
- **Title**: ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping
- **Authors**: Jiacheng Chen, Tao Zhang, Manxi Lin, Dunxian Huang et al.
- **Institution**: Not specified
- **Abstract**: Foundation model for intent-driven shopping experiences orchestrated by LLM agents, moving beyond page/feed-based browsing.
- **Key Innovations**: Intent-to-item fulfillment paradigm; LLM-agent-orchestrated shopping; foundation model for e-commerce.
- **arXiv**: [2606.31693](https://arxiv.org/abs/2606.31693)

### 2.13 Long-term Engagement Optimization
- **Title**: Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning
- **Authors**: Dingsu Wang, Filip Ryzner, Kelly He, Armando Ordorica et al.
- **Institution**: Not specified
- **Abstract**: Shifts optimization from short-term behavioral signals to long-term user engagement and retention in recsys.
- **Key Innovations**: Model-agnostic downstream reward learning for long-term engagement; avoids direct optimization of intractable long-term metrics.
- **arXiv**: [2607.14192](https://arxiv.org/abs/2607.14192)

---

## 3. CTR Prediction & Advertising

### 3.1 Dual-Stream MLP for CTR
- **Title**: Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China (inferred from authors)
- **Abstract**: Proposes a dual-stream MLP architecture for CTR prediction, suggesting simplicity can rival complex architectures.
- **Key Innovations**: Dual-stream MLP architecture; demonstrates that simple MLP structures can achieve competitive CTR prediction performance.
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)

### 3.2 Sparse Attention for Long-term CTR
- **Title**: Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction
- **Authors**: Weijiang Lai, Beihong Jin, Di Zhang, Siru Chen, Jiongyan Zhang, Yuhang Gou, Jian Dong, Xingxing Wang
- **Institution**: Chinese Academy of Sciences, Meituan
- **Abstract**: SparseCTR model efficiently processes long user behavior sequences using sparse attention (EvoAttention), achieving 8.9x inference speedup and 1.72% CTR increase in online A/B testing.
- **Key Innovations**: EvoAttention sparse attention mechanism; 8.9x inference speedup; demonstrated CTR scaling law; online deployment at Meituan.
- **arXiv**: [2601.17836](https://arxiv.org/abs/2601.17836)

### 3.3 CADET: Decoder-Only Transformer for Ads CTR
- **Title**: CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya K. Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil K. Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Quang Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang
- **Institution**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction, successfully deployed on LinkedIn's advertising platform.
- **Key Innovations**: Decoder-only transformer for CTR; end-to-end training; production deployment at LinkedIn scale.
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)

### 3.4 Generative CTR for Search Advertising
- **Title**: Generative Click-through Rate Prediction with Applications to Search Advertising
- **Authors**: Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao
- **Institution**: Not specified (e-commerce platform)
- **Abstract**: Two-stage training leveraging generative pre-training for next-item prediction to enhance discriminative CTR models, validated by online A/B testing on large e-commerce platform.
- **Key Innovations**: Generative pre-training + discriminative fine-tuning paradigm; conditional self-attention decoder; validated on production platform.
- **arXiv**: [2507.11246](https://arxiv.org/abs/2507.11246)

### 3.5 Bench-CTR: CTR Benchmark Platform
- **Title**: Toward a benchmark for CTR prediction in online advertising: datasets, evaluation protocols and perspectives
- **Authors**: Shan Gao, Yanwu Yang
- **Institution**: Not specified
- **Abstract**: Unified architecture of CTR prediction benchmark (Bench-CTR) platform offering flexible interfaces with datasets and components for fair model comparison.
- **Key Innovations**: Standardized CTR benchmark platform; flexible interfaces for datasets and model components; evaluation protocol standardization.
- **arXiv**: [2512.01179](https://arxiv.org/abs/2512.01179)

---

## 4. Sequential Modeling

### 4.1 Multi-Behavior Sequential Modeling (TGA)
- **Title**: Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network for E-Commerce Recommendation
- **Authors**: Hanqi Jin, Gaoming Yang, Zhangming Chan, Yapeng Yuan, Longbin Li, Fei Sun, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Institution**: Alibaba (inferred from authors)
- **Abstract**: TGA jointly models user-item interactions and behavior transition types (click, favorite, cart, purchase) via transition-aware graph attention, deployed in large-scale industrial production. Accepted at WWW 2026.
- **Key Innovations**: Transition-aware graph attention for behavior type modeling; linear complexity vs polynomial in transformers; production deployment at scale.
- **arXiv**: [2601.14955](https://arxiv.org/abs/2601.14955)

### 4.2 SeqUDA-Rec: GAN-based Data Augmentation
- **Title**: SeqUDA-Rec: Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation
- **Authors**: Ruihan Luo, Xuanjing Chen, Ziyang Ding
- **Institution**: Southwest University of Finance and Economics, Columbia Business School, Stanford University
- **Abstract**: Combines GAN-based data augmentation with global user-item graph contrastive learning for sequential recommendation under data sparsity.
- **Key Innovations**: GAN-generated user sub-sequences for augmentation; global graph contrastive learning for cross-user relationships; Transformer-based temporal modeling.
- **arXiv**: [2509.17361](https://arxiv.org/abs/2509.17361)

### 4.3 NextFlow: Unified Sequential Modeling
- **Title**: NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors**: Huichao Zhang, Liao Qu, Yiheng Liu, Hang Chen et al. (35 authors)
- **Institution**: Not specified
- **Abstract**: Decoder-only autoregressive transformer trained on 6 trillion interleaved text-image tokens for unified multimodal understanding and generation.
- **Key Innovations**: 6T token training; prefix-tuning for RL; robust training recipe for multi-scale generation instabilities.
- **arXiv**: [2601.02204](https://arxiv.org/abs/2601.02204)

### 4.4 POEM: Real-Time Sequential Modeling
- **Title**: POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation
- **Authors**: Linxiao Che, Yijia Sun, Siyuan Lou, Shanshan Huang et al.
- **Institution**: Not specified
- **Abstract**: Addresses dynamic drift of user interests and varying contextual conditions in real-time recommendation, beyond static historical click sequences.
- **Key Innovations**: Partial-order modeling for real-time sequential recommendation; captures instant interest dynamics beyond static sequences.
- **arXiv**: [2606.29946](https://arxiv.org/abs/2606.29946)

---

## 5. Game AI & Reinforcement Learning

### 5.1 Augmenting Game AI with Deep RL (Vision Paper)
- **Title**: Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslen
- **Institution**: Electronic Arts (EA), Stockholm, Sweden
- **Abstract**: Vision paper from Conference on Games 2026 surveying how RL can create more believable game AI. Identifies key bottlenecks: sample efficiency, generalization, and the tension between optimal vs believable behavior.
- **Key Innovations**: Genre-level readiness framework for RL game AI; identifies believability (not optimality) as the hard problem; practical deployment examples from EA games.
- **arXiv**: [2606.20210](https://arxiv.org/abs/2606.20210)

### 5.2 StraTA: Agentic RL with Strategic Trajectory Abstraction
- **Title**: StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction
- **Authors**: Xue et al.
- **Institution**: Shanghai AI Lab, Oxford
- **Abstract**: New RL training approach for LLM agents through explicit strategy planning before action execution using hierarchical GRPO.
- **Key Innovations**: Strategic trajectory abstraction for LLM agent RL; hierarchical GRPO; surpasses closed-source frontier systems on SciWorld benchmark.
- **arXiv**: [2605.06642](https://arxiv.org/abs/2605.06642)

### 5.3 GameCraft-Bench: Game Building Agents
- **Title**: GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?
- **Authors**: Tongxu Luo, Rongsheng Wang et al. (25 authors)
- **Institution**: Not specified
- **Abstract**: Benchmark for evaluating LLM agents' ability to build playable games end-to-end in real game engines.
- **Key Innovations**: End-to-end game construction benchmark; real game engine evaluation; multi-agent game building assessment.
- **arXiv**: [2606.17861](https://arxiv.org/abs/2606.17861)

### 5.4 Comprehensive Review of MARL in Video Games
- **Title**: A Comprehensive Review of Multiagent Reinforcement Learning in Video Games
- **Authors**: Z. Li, Q. Ji, X. Ling, Q. Liu
- **Institution**: Not specified
- **Abstract**: Comprehensive review covering foundational work through landmark achievements (AlphaStar, OpenAI Five) in multiagent RL for games.
- **Key Innovations**: Systematic review of MARL techniques including self-play, supervised learning, and deep RL; analysis of superhuman performance across diverse game environments.
- **Published in**: IEEE Transactions on Games, vol. 17, no. 4, Dec. 2025

---

## 6. Cross-Cutting Themes

### Key Trends Observed

1. **Generative Paradigm Shift in CTR/Rec**: Multiple papers (GenCTR, DaV-Gen, Diffusion-GR2, Topology-Aware Tokenization) explore replacing discriminative models with generative approaches for CTR prediction and retrieval.

2. **LLM Agents in Recommendation**: Growing movement toward agentic recommender systems (Autonomous Information Seeking, Seeing and Reflecting, ShopX) that reason, plan, and act autonomously.

3. **Sparse Attention for Long Sequences**: SparseCTR and Long-History Transformers address the fundamental tension between modeling long user histories and real-time serving constraints.

4. **Behavior Transition Modeling**: TGA (WWW 2026) highlights the importance of modeling transitions between behavior types (click -> favorite -> cart -> purchase) rather than treating all interactions equally.

5. **Simplicity Can Win**: Dual-Stream MLP paper and ZoRRO (zero-weight, training-free) challenge the assumption that increasingly complex architectures are necessary.

6. **Game AI Believability**: EA's vision paper frames the hard problem in game AI as believability, not optimality — agents that play perfectly feel inhuman.

7. **Verification as Scaling Axis**: LLM-as-a-Verifier identifies verification capability as a new scaling dimension alongside pre-training, post-training, and test-time compute.

---

## References

| Category | Count |
|----------|-------|
| LLM Surveys & Methods | 8 |
| Recommendation Systems | 13 |
| CTR & Advertising | 5 |
| Sequential Modeling | 4 |
| Game AI & RL | 4 |
| **Total Papers** | **34** |

---

*Report generated on 2026-07-23 via arXiv search across AI, LLM, recommendation, advertising, sequential modeling, CTR, and game topics.*
