---
title: "ArXiv & Conference Digest - 2026-06-05"
type: synthesis
created: 2026-06-05
updated: 2026-06-05
sources: []
tags: [arxiv, conference, ICML, AAAI, NeurIPS, ICLR, KDD, CVPR, ACL, EMNLP, SIGIR, WWW, CIKM, RecSys, recommendation, CTR, LLM, agent, generative-models, sequential-modeling]
---

# ArXiv & Conference Digest — 2026-06-05

## Overview

This digest compiles recent papers from top ML/AI conferences and arXiv, covering:
- **Conferences**: ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025/2026, SIGIR 2026, WWW 2026, CIKM 2026, RecSys 2026
- **Topics**: LLMs, Recommendation Systems, CTR Prediction, Agent Systems, Generative Models, Sequential Modeling, Advertising, Code Execution, Benchmarks
- **Labs**: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, Kuaishou

---

## 1. ICML 2026 (Seoul, South Korea, Jul 6-11, 2026)

**6,634 papers accepted** — the largest ICML ever.

### 1.1 Recommendation & CTR Prediction

#### CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction
- **Authors**: Zixuan Li, Binzong Geng et al.
- **Affiliation**: NLPR, Institute of Automation, Chinese Academy of Sciences; Ant Group
- **Venue**: KDD 2026 (also appears in ICML context)
- **Abstract**: Addresses semantic fragmentation challenge in LM-based CTR prediction. Proposes CTR-Sink framework inserting recommendation-signal-fused `[SINK]` tokens between user behaviors, anchoring LM attention at behavioral boundaries. Two-stage training strategy guides LM attention toward sink tokens; attention sink mechanism amplifies inter-sink dependencies.
- **Key Innovations**: (1) Recommendation-specific `[SINK]` tokens with temporal distance signals; (2) Decoder-compatible attention guidance; (3) Behavioral boundary attention anchoring.
- **Results**: 0.2–0.5% AUC improvement over baseline LM-CTR methods on industrial dataset, MovieLens, and KuaiRec datasets.
- **Link**: [arXiv:2508.03668](https://arxiv.org/abs/2508.03668) | [Code](https://github.com/UGUESS-lzx/CTR-SINK)

#### Sparse by Design: Relevance-Driven Scaling for Recommender Systems
- **Authors**: Meta AI Research
- **Affiliation**: Meta
- **Venue**: ICML 2026
- **Abstract**: Discusses why Sparse MoE doesn't transfer naturally from LMs to recommendation. Token-level routing misaligns with user-item relevance prediction. Proposes relevance-driven scaling where sparse computation is designed around relevance signals.
- **Key Innovations**: Relevance-driven routing granularity, expert specialization adapted to recommendation tasks.
- **Link**: [ICML 2026 Poster](https://icml.cc/virtual/2026/poster/66202)

#### CRAMER: Control via Request-Aware Masking for Editing Recommenders
- **Authors**: Renmin University of China / Dalhousie University
- **Venue**: ICML 2026
- **Abstract**: Enables sequence recommendation models to respond to user's natural language requests (e.g., "I want cheaper/lighter/more formal items") without retraining the full network or relying on LLM prompt reasoning.
- **Key Innovations**: Request-aware masking for editing recommender behavior; bridges traditional sequential recommendation and LLM agent recommendation.
- **Link**: [ICML 2026 Poster](https://icml.cc/virtual/2026/poster/62968)

#### GCIB: Graph Contrastive Information Bottleneck for Multi-Behavior Recommendation
- **Authors**: Tianjin University / Anhui University
- **Venue**: ICML 2026
- **Abstract**: Uses graph contrastive information bottleneck to simultaneously denoise auxiliary behaviors and enhance target behavior representation in multi-behavior recommendation.
- **Link**: [ICML 2026 Poster](https://icml.cc/virtual/2026/poster/62097)

#### CARE: Adaptive Calibration for Reliable Recommendations
- **Authors**: University of Technology Sydney
- **Venue**: ICML 2026
- **Abstract**: Wraps any backbone recommender with adaptive calibration, producing variable-size recommendation sets with finite-sample performance guarantees. Uses loss-based behavior change monitoring and online aggregation threshold recalibration.
- **Link**: [ICML 2026 Poster](https://icml.cc/virtual/2026/poster/62132)

#### CORAL: Uncertainty-Aware Regulation of Exposure Concentration in Recommender Systems
- **Authors**: University of Technology Sydney
- **Venue**: ICML 2026
- **Abstract**: Addresses feedback-driven exposure concentration where systems collapse to少数 categories. Models exposure regulation as constrained sequential decision with UCB risk estimation.
- **Link**: [ICML 2026 Poster](https://icml.cc/virtual/2026/poster/63919)

#### ProRL: Effective Reinforcement Learning for Proactive Recommendation
- **Authors**: Fudan University
- **Venue**: ICML 2026
- **Abstract**: Addresses proactive recommendation where system guides user preferences toward target items. Uses rectified policy gradient to fix length-dependent bias and high variance from path-level reward weighting.
- **Link**: [ICML 2026 Poster](https://icml.cc/virtual/2026/poster/61903)

#### RSIR: Can Recommender Systems Teach Themselves?
- **Authors**: University of Science and Technology of China / Huawei
- **Venue**: arXiv (ICML context)
- **Abstract**: Uses closed-loop self-bootstrapping with fidelity control — current model generates user interaction sequences, fidelity filter retains samples aligned with approximate user preference manifold, then retrains successor model.
- **Link**: [arXiv:2602.15659](https://arxiv.org/abs/2602.15659)

#### VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion
- **Authors**: NTU / Beihang University / Alibaba
- **Venue**: ICML 2026
- **Abstract**: Exposes vulnerability in multimodal LLM recommender systems — synchronized multimodal poisoning can manipulate fusion representations along stable semantic directions.
- **Link**: [arXiv:2602.06409](https://arxiv.org/abs/2602.06409)

### 1.2 Generative Models & Diffusion

#### SoftMatcha 2: Fast and Soft Pattern Matcher for Trillion-Scale Corpora
- **Authors**: Masataka Yoneda, Yusuke Matsushita, Go Kamoda et al.
- **Affiliation**: Preferred Networks, RIKEN AIP
- **Venue**: ICML 2026
- **Abstract**: Fast soft pattern matching for trillion-scale text corpora.
- **Link**: [arXiv:2602.10908](https://arxiv.org/abs/2602.10908)

### 1.3 Agent Systems

#### ABCD: All Biases Come Disguised
- **Authors**: Mateusz, Xavier et al.
- **Affiliation**: Dartmouth College
- **Venue**: ICML 2026
- **Abstract**: Studies bias propagation in AI systems.
- **Link**: [arXiv:2602.17445](https://arxiv.org/abs/2602.17445) | [Project](https://futuramistic.github.io/abcd/)

---

## 2. AAAI 2026 (Singapore, Jan 20-27, 2026)

**4,902 papers accepted** from ~29,000 submissions. Largest AAAI ever.

### 2.1 LLM & Agent Systems

#### LLM Collaboration With Multi-Agent Reinforcement Learning
- **Venue**: AAAI 2026
- **Abstract**: Explores how LLM agents can collaborate through multi-agent reinforcement learning for complex task solving.
- **Link**: [arXiv:2508.04652](https://arxiv.org/abs/2508.04652)

#### AutoTool: Efficient Tool Selection for Large Language Model Agents
- **Venue**: AAAI 2026
- **Abstract**: Addresses efficient tool selection for LLM agents, reducing computational overhead while maintaining task performance.
- **Link**: [arXiv:2511.14650](https://arxiv.org/abs/2511.14650)

#### ExtendAttack: Attacking Servers of LRMs via Extending Reasoning
- **Venue**: AAAI 2026
- **Abstract**: Proposes adversarial attack method targeting large reasoning models by manipulating reasoning chains.
- **Link**: [arXiv:2506.13737](https://arxiv.org/abs/2506.13737)

#### BadThink: Triggered Overthinking Attacks on Chain-of-Thought Reasoning
- **Venue**: AAAI 2026
- **Abstract**: Demonstrates vulnerabilities in CoT reasoning through triggered overthinking attacks.
- **Link**: [arXiv:2511.10714](https://arxiv.org/abs/2511.10714)

#### Rethinking the Reliability of Multi-agent System: Byzantine Fault Tolerance
- **Venue**: AAAI 2026
- **Abstract**: Analyzes multi-agent system reliability from Byzantine fault tolerance perspective.
- **Link**: [arXiv:2511.10400](https://arxiv.org/abs/2511.10400)

### 2.2 Vision-Language Models

#### VLA-Adapter: Tiny-Scale Vision-Language-Action Model
- **Venue**: AAAI 2026
- **Abstract**: Efficient paradigm for tiny-scale VLA models with adapter-based transfer.
- **Link**: [arXiv:2509.09372](https://arxiv.org/abs/2509.09372)

#### GUI-G²: Gaussian Reward Modeling for GUI Grounding
- **Venue**: AAAI 2026
- **Abstract**: Novel reward modeling approach for GUI grounding using Gaussian rewards.
- **Link**: [arXiv:2507.15846](https://arxiv.org/abs/2507.15846)

#### X-SAM: From Segment Anything to Any Segmentation
- **Venue**: AAAI 2026
- **Abstract**: Extends SAM architecture to universal segmentation tasks.
- **Link**: [arXiv:2508.04655](https://arxiv.org/abs/2508.04655)

### 2.3 Recommendation

#### RMBRec: Robust Multi-Behavior Recommendation towards Target Behaviors
- **Affiliation**: Multiple institutions
- **Venue**: AAAI 2026
- **Abstract**: Robust multi-behavior recommendation framework focusing on target behavior prediction.
- **Link**: [arXiv:2601.08705](https://arxiv.org/abs/2601.08705)

#### Length-Adaptive Interest Network for Balancing Long and Short Sequence Modeling in CTR Prediction
- **Venue**: AAAI 2026
- **Abstract**: Addresses the trade-off between long and short user behavior sequences in CTR prediction.
- **Link**: [arXiv:2601.19142](https://arxiv.org/abs/2601.19142)

#### Bid Farewell to Seesaw: Long-tail Session-based Recommendation via Dual Constraints
- **Venue**: AAAI 2026
- **Abstract**: Solves long-tail distribution problem in session-based recommendation through dual constraints of hybrid intents.
- **Link**: [arXiv:2511.08378](https://arxiv.org/abs/2511.08378)

---

## 3. NeurIPS 2025 (Mexico City, Dec 2-5, 2025)

**5,275 papers accepted** (95.46% of reviewed papers).

### 3.1 Notable Oral/Spotlight Papers

#### DynamiX: Dynamic Resource eXploration for Personalized Ad-Recommendations
- **Venue**: NeurIPS 2025
- **Abstract**: Dynamic resource exploration framework for personalized ad recommendations.
- **Link**: [arXiv:2511.18331](https://arxiv.org/abs/2511.18331)

#### Boosting Knowledge Utilization in Multimodal Large Language Models via Adaptive Logits Fusion and Attention Reallocation
- **Venue**: NeurIPS 2025 Oral
- **Abstract**: Novel approach to enhance knowledge utilization in MLLMs through adaptive logits fusion.
- **Link**: [NeurIPS 2025 Virtual](https://neurips.cc/virtual/2025/papers.html)

---

## 4. ICLR 2026 (Singapore, Apr 28 - May 2, 2026)

**5,356 papers accepted**.

### 4.1 Vision & Multimodal

#### NEO: Multimodal From Pixels to Words — Native Vision-Language Primitives at Scale
- **Authors**: H. Diao, M. Li, S. Wu et al.
- **Affiliation**: MMLab@NTU
- **Venue**: ICLR 2026
- **Abstract**: Proposes native vision-language primitives for efficient multimodal processing.
- **Link**: [arXiv:2510.14979](https://arxiv.org/abs/2510.14979) | [Project](https://github.com/EvolvingLMMs-Lab/NEO)

#### SeedVR2: One-Step Video Restoration via Diffusion Adversarial Post-Training
- **Authors**: J. Wang, S. Lin, Z. Lin et al.
- **Affiliation**: MMLab@NTU
- **Venue**: ICLR 2026
- **Abstract**: Achieves one-step video restoration through diffusion adversarial post-training.
- **Link**: [arXiv:2506.05301](https://arxiv.org/abs/2506.05301) | [Project](https://iceclear.github.io/projects/seedvr2/)

### 4.2 Recommendation & Sequential

#### CollectiveKV: Decoupling and Sharing Collaborative Information in Sequential Recommendation
- **Venue**: ICLR 2026
- **Abstract**: Decouples and shares collaborative information for improved sequential recommendation.
- **Link**: [arXiv:2601.19178](https://arxiv.org/abs/2601.19178)

### 4.3 Theory & ML

#### InfoNCE Induces Gaussian Distribution
- **Authors**: Roy Betser, Eyal Gofer et al.
- **Venue**: ICLR 2026 Oral
- **Abstract**: Proves that InfoNCE loss induces Gaussian distribution in representation space.
- **Link**: [arXiv:2602.24012](https://arxiv.org/abs/2602.24012)

---

## 5. KDD 2026 (Jeju Island, South Korea, Aug 9-13, 2026)

**1,400+ papers accepted** across two cycles.

### 5.1 Recommendation & CTR

#### GRAB: LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling
- **Authors**: Baidu Research
- **Affiliation**: Baidu
- **Venue**: arXiv (KDD 2026 context)
- **Abstract**: End-to-end generative framework for CTR prediction inspired by LLM scaling. Integrates Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics. Full-scale online deployment shows 3.05% revenue increase and 3.49% CTR rise.
- **Key Innovations**: (1) Sequence-first paradigm for CTR; (2) CamA mechanism; (3) Monotonic scaling with longer sequences.
- **Link**: [arXiv:2602.01865](https://arxiv.org/abs/2602.01865)

#### Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations
- **Affiliation**: Meta
- **Venue**: KDD 2026
- **Abstract**: Redesigns model space for cost-effective large-scale ads recommendation, addressing efficiency-performance tradeoffs at Meta's scale.
- **Link**: [GitHub](https://github.com/guyulongcs/Deep-Learning-for-Search-Recommendation-Advertisements)

#### CTR-Sink: Attention Sink for Language Models in CTR Prediction
- **Authors**: Zixuan Li et al.
- **Affiliation**: CAS / Ant Group
- **Venue**: KDD 2026
- **Abstract**: (See Section 1.1 above — full paper published at KDD 2026)

#### Generalizable Multi-Pass Training of Ads Recommendation Models with Foundation Model Guidance
- **Venue**: KDD 2026
- **Abstract**: Multi-pass training paradigm for ads recommendation models guided by foundation model knowledge.

### 5.2 Data Mining & Knowledge Discovery

#### KDD 2026 Research Track highlights include papers on:
- Federated learning for recommendation
- Causal inference in advertising
- Graph neural networks for user modeling
- Large-scale sequential behavior modeling

---

## 6. CVPR 2026 (New Orleans, Jun 14-19, 2026)

**4,069 papers indexed** in Open Access.

### 6.1 3D Vision & Generation

#### OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer
- **Authors**: H. Peng, H. Li, Y. Dai et al.
- **Affiliation**: MMLab@NTU
- **Venue**: CVPR 2026 (Highlight)
- **Abstract**: Unified visual geometry transformer driven by omni-modality input.
- **Link**: [arXiv:2511.10560](https://arxiv.org/abs/2511.10560) | [Project](https://livioni.github.io/OmniVGGT-official/)

#### PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image
- **Authors**: Z. Cao, F. Hong, Z. Chen, L. Pan, Z. Liu
- **Venue**: CVPR 2026
- **Abstract**: Generates simulation-ready physical 3D assets from single images.
- **Link**: [arXiv:2511.13648](https://arxiv.org/abs/2511.13648) | [Project](https://physx-anything.github.io/)

### 6.2 Video & World Models

#### WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World
- **Authors**: A. Liang et al.
- **Venue**: CVPR 2026 (Oral)
- **Abstract**: Comprehensive benchmarking framework for driving world models.
- **Link**: [arXiv:2512.10958](https://arxiv.org/abs/2512.10958) | [Project](https://worldbench.github.io/worldlens)

#### MatAnyone2: Scaling Video Matting via Learned Quality Evaluator
- **Authors**: P. Yang, S. Zhou, K. Hao, Q. Tao
- **Venue**: CVPR 2026 (Highlight)
- **Abstract**: Scales video matting with learned quality evaluation.
- **Link**: [arXiv:2512.11782](https://arxiv.org/abs/2512.11782) | [Project](https://pq-yang.github.io/projects/MatAnyone2/)

### 6.3 Efficient Inference

#### LLSA: Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers
- **Authors**: Y. Zhou, Z. Xiao, T. Wei, S. Yang, X. Pan
- **Venue**: CVPR 2026 (Highlight)
- **Abstract**: Proposes log-linear sparse attention for efficient diffusion transformer inference.
- **Link**: [arXiv:2512.16615](https://arxiv.org/abs/2512.16615) | [Project](https://github.com/SingleZombie/LLSA)

---

## 7. ACL 2026 (San Diego, Jul 2-7, 2026)

**2,296 Main + 2,163 Findings = 4,459 papers accepted** from 12,148 submissions.

### 7.1 LLM Agents & Reasoning

#### Reasoning While Asking: Transforming Reasoning LLMs from Passive Solvers to Proactive Inquirers
- **Authors**: Xin Chen, Feng Jiang et al.
- **Affiliation**: Nanjing University / CAS
- **Venue**: ACL 2026 Main
- **Abstract**: Transforms reasoning LLMs from passive problem solvers to proactive information seekers.
- **Link**: [arXiv:2601.22139](https://arxiv.org/abs/2601.22139)

#### PEGRL: Post-Editing Guided Reinforcement Learning for LLM-based Machine Translation
- **Authors**: Nanjing University / Tongyi Lab
- **Venue**: ACL 2026 Main
- **Abstract**: Two-stage RL framework introducing post-editing as auxiliary task for stable translation training. On English-to-Turkish, COMETKiwi score comparable to DeepSeek-V3.2.
- **Link**: [arXiv:2511.02626](https://arxiv.org/abs/2511.02626)

#### BootTrans: Bootstrapping Code Translation with Weighted Multilanguage Exploration
- **Authors**: Yuhan Wu et al.
- **Affiliation**: Nanjing University
- **Venue**: ACL 2026 Main
- **Abstract**: Reduces reliance on parallel corpora for multilingual code translation.
- **Link**: [arXiv:2601.03512](https://arxiv.org/abs/2601.03512)

### 7.2 Theme: Interpretability

ACL 2026's special theme is **"Interpretability of NLP Models"**. Key trend shifts:
- LLM Reasoning/Agents/Tool Use: 142→366 papers (+224, +8.2pp)
- Model Training/Fine-tuning/Alignment/RL: 196→295 papers
- RAG/QA/Knowledge Editing: 174→244 papers
- Traditional NLP: declining share

### 7.3 Key Trends

- From "generalization" (ACL 2025) to "interpretability" (ACL 2026)
- Agent and reasoning topics show greatest growth
- Systems that "reason, retrieve evidence, cite correctly, explain itself, and fail less dangerously"

---

## 8. EMNLP 2025 (Suzhou, China, Nov 4-9, 2025) & EMNLP 2026

### 8.1 EMNLP 2025 Highlights

#### Single LLM, Multiple Roles: Unified RAG Using Role-Specific Token Optimization
- **Authors**: Yutao Zhu, Jiajie Jin et al.
- **Venue**: EMNLP 2025 Main
- **Abstract**: Unified retrieval-augmented generation framework using role-specific token optimization for multi-role LLM deployment.
- **Link**: [EMNLP 2025](https://2025.emnlp.org/program/main_papers)

#### Selective Preference Optimization via Token-Level Reward Function Estimation
- **Venue**: EMNLP 2025
- **Abstract**: Token-level reward estimation for fine-grained preference optimization.

### 8.2 EMNLP 2026 Findings

#### Context-Aware Hierarchical Taxonomy Generation for Scientific Papers via LLM-Guided Multi-Aspect Clustering
- **Authors**: kun Zhu, Lizi Liao et al.
- **Venue**: EMNLP 2026

---

## 9. SIGIR 2026

### 9.1 Sequential Recommendation

#### Beyond Item IDs: Scaling Short-Form-Video Recommendation via Semantic-Native Long Sequence Modeling
- **Venue**: SIGIR 2026
- **Abstract**: Scales recommendation for short-form video through semantic-native long sequence modeling beyond traditional item IDs.

#### FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
- **Venue**: SIGIR 2026
- **Abstract**: Enhances interest modeling through frequency-domain analysis for CTR prediction.

#### WPGRec: Wavelet Packet Guided Graph Enhanced Sequential Recommendation
- **Venue**: SIGIR 2026
- **Abstract**: Uses wavelet packet analysis to guide graph-enhanced sequential recommendation.

#### ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation
- **Venue**: SIGIR 2026
- **Abstract**: Controls embedding anisotropy for improved LLM-enhanced sequential recommendation.

#### Learning to Forget: Satiation-Aware Long-Sequence Transducers
- **Venue**: SIGIR 2026
- **Abstract**: Addresses post-purchase redundancy through satiation-aware sequence modeling.

#### RoTE: Coarse-to-Fine Multi-Level Rotary Time Embedding for Sequential Recommendation
- **Venue**: SIGIR 2026
- **Abstract**: Multi-level rotary time embedding for temporal recommendation.

---

## 10. WWW 2026

### 10.1 Recommendation

#### Mixture of Sequence: Theme-Aware MoE for Long-Sequence Recommendation
- **Authors**: Lin X et al.
- **Venue**: WWW 2026
- **Abstract**: Theme-aware mixture-of-experts for long-sequence recommendation at scale.

#### VK-LSVD: Large-Scale Industrial Dataset for Short-Video Recommendation
- **Venue**: WWW 2026
- **Abstract**: Large-scale industrial dataset specifically for short-video recommendation research.

#### Hyena Operator for Fast Sequential Recommendation
- **Venue**: WWW 2026
- **Abstract**: Adapts Hyena operator for efficient sequential recommendation.

#### OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer
- **Venue**: WWW 2026
- **Abstract**: Single Transformer architecture unifying feature interaction and sequence modeling for industrial recommendation.

#### STCRank: Spatio-temporal Collaborative Ranking at Kuaishou E-shop
- **Authors**: Kuaishou
- **Venue**: WWW 2026
- **Abstract**: Spatio-temporal collaborative ranking for interactive recommendation at Kuaishou's e-commerce platform.

#### PRISM: Personalized Recommendation via Information Synergy Module
- **Venue**: WWW 2026

---

## 11. RecSys 2026 (Minneapolis, Sep 27 - Oct 2, 2026)

### 11.1 LLM & Agents for Recommendation

#### Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents
- **Authors**: Haochen Wang et al.
- **Affiliation**: Google (YouTube)
- **Venue**: RecSys 2026
- **Abstract**: First rigorous framework where LLM agents act as expert Machine Learning Engineers to evolve recommendation models. Uses Gemini 2.5 Pro in hierarchical agentic system managing full lifecycle — from hypothesis generation to A/B testing. Successful production deployments at YouTube.
- **Key Innovations**: (1) Autonomous MLE framework at industrial scale; (2) Semantic discovery beyond parameter tuning; (3) Acceleration of experimental velocity.
- **Results**: Agents surpass hand-tuned baselines; successfully deployed to multiple YouTube recommendation surfaces.
- **Link**: [arXiv:2602.10226](https://arxiv.org/abs/2602.10226) | [DOI:10.1145/3773078.3831919](https://doi.org/10.1145/3773078.3831919)

### 11.2 Sequential Recommendation

#### Structure-Preserving Projection for Mitigating Modality Bias in LLM-Based Sequential Recommendation
- **Venue**: RecSys 2026
- **Link**: [arXiv:2608.08583](https://arxiv.org/abs/2608.08583)

#### Deciding When to Rely on Visual Information: Gated Multimodal Fusion in Sequential Recommendation
- **Venue**: RecSys 2026
- **Link**: [arXiv:2608.10700](https://arxiv.org/abs/2608.10700)

#### Topology-Aware Tokenization for Generative Recommendation
- **Venue**: RecSys 2026
- **Link**: [arXiv:2607.18600](https://arxiv.org/abs/2607.18600)

#### RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation
- **Venue**: RecSys 2026
- **Link**: [arXiv:2607.12945](https://arxiv.org/abs/2607.12945)

---

## 12. CIKM 2026

### 12.1 Sequential Recommendation

#### HCGRec: Hint-Conditioned Generative Recommendation with Semantic IDs
- **Venue**: CIKM 2026
- **Link**: [arXiv:2608.11980](https://arxiv.org/abs/2608.11980)

#### From Overlooked to Exploited: Recovering Item Relations via Mixture of Perspectives
- **Venue**: CIKM 2026
- **Link**: [arXiv:2608.11846](https://arxiv.org/abs/2608.11846)

---

## 13. Cross-Conference: LLMs in Recommendation & Advertising

### 13.1 LLM-Enhanced CTR Prediction

#### Field Matters: Lightweight LLM-enhanced Method for CTR Prediction
- **Affiliation**: Alibaba (published at ACM)
- **Venue**: ACM (2026)
- **Abstract**: Lightweight LLM-enhanced CTR method that avoids extensive textual description processing for large-scale instances.
- **Link**: [ACM DL](https://dl.acm.org/doi/abs/10.1145/3774904.3792387)

#### HyFormer: Revisiting Sequence Modeling and Feature Interaction in CTR Prediction
- **Affiliation**: ByteDance
- **Venue**: arXiv (2026)
- **Abstract**: Revisits the roles of sequence modeling and feature interaction through hybrid Transformer architecture for CTR prediction at ByteDance scale.
- **Link**: [GitHub](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising)

#### TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders
- **Affiliation**: ByteDance
- **Venue**: arXiv (2026)
- **Abstract**: Scales up ranking models in industrial recommender systems through token mixing.

### 13.2 Generative Recommendation

#### Towards An Efficient LLM Training Paradigm for CTR Prediction
- **Venue**: arXiv (2026)
- **Abstract**: Proposes efficient training paradigm addressing computational inefficiency in LLM-based CTR prediction.

#### Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation
- **Affiliation**: Northeastern University
- **Venue**: ICML 2026

#### SynGR: Unleashing Cross-Modal Synergy for Generative Recommendation
- **Affiliation**: Beihang University
- **Venue**: ICML 2026

### 13.3 LLM Advertising

#### NaiAD: Initiate Data-Driven Research for LLM Advertising
- **Venue**: arXiv (2026)
- **Abstract**: First comprehensive dataset for LLM-native advertising (58,999 ad-embedded responses). Organized around theoretically grounded evaluation metrics capturing user and platform perspectives.
- **Link**: [arXiv:2605.09918](https://arxiv.org/abs/2605.09918)

---

## 14. Cross-Conference: Agent Systems

### 14.1 LLM Agents

#### Google DeepMind: AI Co-Mathematician
- **Affiliation**: Google DeepMind
- **Abstract**: Stateful AI workspace for long-term mathematical discovery, supporting mathematicians with iterative research assistance.

#### Meta AI: Proactive Memory Agent
- **Affiliation**: Meta FAIR
- **Abstract**: "Remember When It Matters" — proactive memory agent that boosts Claude Sonnet 4.5 by +8.3pp on Terminal-Bench 2.0, +6.8pp on τ²-Bench. Two-phase memory bank runs alongside unmodified action agent.

#### Self-Evolving Recommendation System (YouTube/Google)
- (See Section 11.1 above)

### 14.2 Multi-Agent Systems

#### LLM Collaboration With Multi-Agent Reinforcement Learning
- **Venue**: AAAI 2026
- **Link**: [arXiv:2508.04652](https://arxiv.org/abs/2508.04652)

---

## 15. Cross-Conference: Generative Models & Diffusion

### 15.1 Text Generation

#### Cola DLM: Continuous Latent Diffusion Language Model
- **Venue**: arXiv (2026)
- **Abstract**: Hierarchical latent diffusion model for text generation — plans in latent space then decodes to natural language. Uses Text VAE + block-causal Diffusion Transformer.

### 15.2 Image & Video Generation

#### Image Generators are Generalist Vision Learners
- **Affiliation**: Google DeepMind
- **Abstract**: Shows that training generative models to produce images teaches better visual understanding than discriminative pretraining.

#### GPT-5.5 + Images 2.0
- **Affiliation**: OpenAI
- **Abstract**: Reasoning integrated into image generation pipeline — search, plan, evaluate, generate paradigm. Can web search during generation for real-time information.

---

## 16. Cross-Conference: Sequential Modeling

### 16.1 Key Papers

| Paper | Venue | Key Innovation |
|-------|-------|----------------|
| ONETrans (ByteDance) | WWW 2026 | Unified feature interaction + sequence modeling with one Transformer |
| TokenMixer-Large (ByteDance) | arXiv 2026 | Scaling ranking models via token mixing |
| LONGER (ByteDance) | arXiv 2025 | Scaling long sequence modeling in industrial recommenders |
| RankMixer (ByteDance) | arXiv 2025 | Scaling ranking models at industrial scale |
| STCA (ByteDance) | arXiv 2025 | End-to-End 10k-sequence modeling on Douyin |
| Mixture of Sequence (WWW 2026) | WWW 2026 | Theme-aware MoE for long-sequence recommendation |

---

## 17. Cross-Conference: Benchmarks & Evaluation

### 17.1 Notable Benchmarks

#### IndustryBench: Probing Industrial Knowledge Boundaries of LLMs
- **Venue**: arXiv (2026)
- **Abstract**: Tests LLMs on industrial procurement standards compliance.

#### SLR-Bench: Curriculum Benchmark for Logical Reasoning
- **Venue**: ACL 2026
- **Abstract**: 19k prompts across 20 curriculum levels for relational, arithmetic, and recursive complexity.

#### WorldLens Benchmark for Driving World Models
- **Venue**: CVPR 2026 (Oral)
- **Abstract**: Full-spectrum evaluation of driving world models in real-world scenarios.

---

## 18. Industry Lab Highlights

### 18.1 Google DeepMind (2026 publications)
- **TRecViT**: Recurrent Video Transformer (Jan 2026)
- **Image Generators are Generalist Vision Learners** (Apr 2026)
- **Decoupled DiLoCo**: Distributed training infrastructure (Apr 2026)
- **AI Co-Mathematician**: Stateful AI workspace for math discovery
- **Vision Banana**: Generative models for visual understanding (Apr 2026)

### 18.2 OpenAI (2026)
- **GPT-5.5 + Images 2.0**: Reasoning in generation pipeline
- **GPT-5.6 Sol**: Price reduction (>20% cut)
- **InstantDB acquisition**: Persistent state for AI agents

### 18.3 Meta AI (2026)
- **Meta Lattice**: Cost-effective ads recommendation (KDD 2026)
- **Sparse by Design**: Relevance-driven scaling (ICML 2026)
- **Proactive Memory Agent**: +8.3pp on Terminal-Bench
- **DMC-Optim RL Framework**: Code optimization improvements
- **Muse Spark**: Closed-source model launch
- **AI Business Assistant**: Global rollout to all advertisers

### 18.4 ByteDance (2026)
- **HyFormer**: Hybrid Transformer for CTR
- **TokenMixer-Large**: Scaling ranking models
- **LONGER**: Scaling long sequence modeling
- **RankMixer**: Scaling ranking models
- **STCA**: 10k-sequence modeling on Douyin
- **ONETrans**: Unified architecture for industrial recommendation

### 18.5 Alibaba (2026)
- **Field Matters**: Lightweight LLM-enhanced CTR
- **VENOMREC**: Multimodal LLM recommendation security (ICML 2026)
- **Qwen**: Continued model advancement

### 18.6 Baidu (2026)
- **GRAB**: Generative ranking with CamA for CTR (3.05% revenue increase)
- **Ernie Bot**: Continued integration

### 18.7 Kuaishou (2026)
- **STCRank**: Spatio-temporal collaborative ranking (WWW 2026)
- **TWIN series**: Continued evolution of lifelong behavior modeling

### 18.8 Tencent (2026)
- **Hunyuan**: Continued model advancement
- **WeChat AI integration**: Plugin penetration ~20-30%

---

## Key Trends Summary

1. **LLM → Agent Evolution**: ACL 2026 shows 158% growth in agent/reasoning papers. Systems move from "bigger models" to "reasoning, retrieving, citing, explaining."

2. **Generative Recommendation**: Shift from discriminative CTR to generative paradigms — GRAB (Baidu), ONETrans (ByteDance), Self-Evolving RecSys (Google/YouTube).

3. **Scaling Laws for Recommendation**: ByteDance's LONGER, RankMixer, TokenMixer-Large demonstrate industrial-scale scaling; Meta's Wukong/Lattice explore cost-effective scaling.

4. **MoE in Recommendation**: Theme-aware MoE (WWW 2026), relevance-driven sparse scaling (Meta/ICML 2026) — adapting LLM architectures to recommendation.

5. **Agentic Optimization**: YouTube's Self-Evolving RecSys (RecSys 2026) shows LLM agents can surpass human ML engineers in model evolution.

6. **Security & Adversarial**: VENOMREC (ICML 2026), BadThink (AAAI 2026) highlight growing concerns about multimodal attacks and reasoning vulnerabilities.

7. **Interpretability as Theme**: ACL 2026's special theme signals field maturation — systems must explain, not just perform.

8. **Unified Architectures**: ONETrans, HyFormer converge feature interaction and sequence modeling into single Transformer architectures.

---

*Generated: 2026-06-05 | Sources: arXiv, conference proceedings, paper lists*
