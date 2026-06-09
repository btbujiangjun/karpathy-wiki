---
title: arXiv Daily — 2026-06-09
type: synthesis
created: 2026-06-09
updated: 2026-06-09
sources: []
tags: [arxiv, daily, LLM, CTR, recommendation, games, RL, advertising, IR, agents]
---

# arXiv Daily — 2026-06-09

Selection of recent papers (submitted Jun 5–8, 2026) across LLMs, recommendation, CTR prediction, advertising, games, and sequential modeling.

---

## LLMs & Foundation Models

### 1. Agentopia: Long-Term Life Simulation and Learning in Agent Societies
- **Link**: [2606.07513](https://arxiv.org/abs/2606.07513)
- **Authors**: Xintao Wang, Sirui Zheng, Hongqiu Wu, et al.
- **Institution**: (academic)
- **Key Innovation**: Framework for 10-year life simulation with 100 LLM agents autonomously pursuing personal growth and social relationships. Defines "life reward" mirroring human well-being and trains underlying LLM via rejection sampling. Emergent social behaviors +15.6% improvement on role-playing benchmarks.
- **Abstract**: Studies long-term life simulation and LLM learning in agent societies with two goals: investigating social behaviors from life-long simulation, and developing anthropomorphic capabilities through years of simulated social experience. 100 agents autonomously pursue personal growth, develop social relationships, and fulfill needs over 10 simulated years.

### 2. How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope
- **Link**: [2606.07489](https://arxiv.org/abs/2606.07489)
- **Authors**: Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma
- **Institution**: Perplexity AI
- **Key Innovation**: Empirical study using production data from Perplexity's Search and Computer products. Computer agents perform 26min of autonomous work vs 33sec for Search. Reduces completion time from 269 to 36min (87% reduction), cost by 94%. Per-query dissatisfaction rates 55% lower.
- **Abstract**: Uses production data to study how AI agents accelerate knowledge work. Computer performs 26 minutes of autonomous work per session vs 33 seconds for Search. Shifts follow-up queries toward higher-order work like verification and extension. Reduces time and cost by 87% and 94% respectively.

### 3. BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization
- **Link**: [2606.00079](https://arxiv.org/abs/2606.00079)
- **Authors**: Jiayu Zhao, Zihan Teng, Minhao Fan, et al.
- **Institution**: (academic)
- **Key Innovation**: Spectral energy-guided bit allocation for MoE quantization. Analyzes expert weight matrices in frequency domain to determine optimal bit-width per expert, achieving high compression with minimal perplexity degradation.
- **Abstract**: Proposes BitsMoE for efficient MoE LLM quantization using spectral energy analysis to guide bit allocation across experts. Achieves strong compression-efficiency tradeoffs.

### 4. BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding
- **Link**: [2606.00144](https://arxiv.org/abs/2606.00144)
- **Authors**: Liang He, Jingbo Wen, Qishi Zhan, et al.
- **Institution**: (academic)
- **Key Innovation**: Multi-view training objective for speculative decoding draft models that is acceptance-aware, optimizing for both generation quality and draft acceptance rate with sparse KV cache.
- **Abstract**: Proposes BudgetDraft with acceptance-aware multi-view training for sparse-KV speculative decoding, improving draft model quality and acceptance rates.

### 5. DyCon: Dynamic Reasoning Control via Evolving Difficulty Modeling
- **Link**: [2606.07108](https://arxiv.org/abs/2606.07108)
- **Authors**: Tengyao Tu, Yulin Li, Hui-Ling Zhen, et al.
- **Institution**: (academic)
- **Key Innovation**: ICML 2026. Training-free framework using latent step-level representations to model evolving task difficulty and dynamically control reasoning depth, mitigating "overthinking" in Large Reasoning Models. Works across 4B–32B models on math, QA, and coding.
- **Abstract**: Empirically shows problem difficulty evolves dynamically during reasoning and is linearly encoded in step-level embeddings. Proposes DyCon to explicitly model evolving difficulty and dynamically control reasoning depth.

### 6. CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO
- **Link**: [2606.00172](https://arxiv.org/abs/2606.00172)
- **Authors**: Yang Li, Gongle Xue, Yijia Guo, et al.
- **Institution**: (academic)
- **Key Innovation**: Novel training objective for GRPO (Group Relative Policy Optimization) that uses clipped asymmetric self-teaching with advantage flipping to stabilize RL-based reasoning training without requiring a privileged teacher model.
- **Abstract**: Proposes CAST for GRPO, using non-privileged clipped asymmetric self-teaching with advantage flipping to improve reasoning training stability.

### 7. Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs
- **Link**: [2606.00642](https://arxiv.org/abs/2606.00642)
- **Authors**: Yu-An Lu, Ci-Yang Tsai, Yu-Lin Tsai, Raluca Ada Popa, Chia-Mu Yu
- **Institution**: (academic)
- **Key Innovation**: Security analysis demonstrating LLMs' internal reasoning traces can be exposed even when models are instructed not to reveal them, raising privacy and safety concerns for chain-of-thought reasoning.
- **Abstract**: Shows that reasoning traces in LLMs can be extracted even when models are prompted to keep them hidden. Raises significant concerns for private chain-of-thought reasoning.

### 8. How reliable are LLMs when it comes to playing dice?
- **Link**: [2606.07515](https://arxiv.org/abs/2606.07515)
- **Authors**: Luca Avena, Gianmarco Bet, Bernardo Busoni
- **Institution**: (academic)
- **Key Innovation**: Controlled benchmark on discrete probability problems. Models achieve 0.96 accuracy on standard problems but only 0.59 on counterintuitive ones. Token bias: performance drops >20% with disguised variants. No model proved immune to misleading prompts.
- **Abstract**: Investigates probabilistic reasoning of LLMs through controlled study. 8 SOTA models tested with/without CoT. Token bias documented: performance drops >20% on disguised variants, up to 34% with misleading suggestions.

### 9. Act As a Real Researcher: A Suite of Benchmarks for Research Lifecycle
- **Link**: [2606.07462](https://arxiv.org/abs/2606.07462)
- **Authors**: Jiayu Wang, Weijiang Lv, Bowen Fu, et al.
- **Institution**: (academic)
- **Key Innovation**: AARR (Act As a Real Researcher) benchmark series evaluating whether agents can emulate nuanced human researcher reasoning. Best system (Mini-SWE-Agent + Claude Opus 4.7) achieves only 68.3%, frequently missing subtle but critical details.
- **Abstract**: Introduces AARR benchmark series focusing on researcher-like professionalism and nuanced reasoning. Best configuration achieves 68.3% success rate, showing researcher-like AI requires further exploration of research behavior.

### 10. On Effectiveness and Efficiency of Agentic Tool-calling and RL Training
- **Link**: [2606.00135](https://arxiv.org/abs/2606.00135)
- **Authors**: Tong Liu, Cheng Qian, Matej Cief, et al.
- **Institution**: (academic)
- **Key Innovation**: ICML 2026. Systematic study of tradeoffs in agentic tool-calling, comparing supervised fine-tuning vs RL for tool-use capabilities. Provides practical guidance on when RL training justifies its additional cost.
- **Abstract**: Studies effectiveness-efficiency tradeoffs in agentic tool-calling and RL training. Compares SFT and RL approaches for tool-use capabilities.

### 11. CRMA: A Spectrally-Bounded Backbone for Modular Continual Fine-Tuning of LLMs
- **Link**: [2606.00382](https://arxiv.org/abs/2606.00382)
- **Authors**: Kiran Nayudu, Aswini Nutakki, Sai Vinay Naidu, Ashwin Shanmugasundaram
- **Institution**: (academic)
- **Key Innovation**: Spectral regularization backbone for modular continual fine-tuning that bounds weight updates in frequency domain, preventing catastrophic forgetting while enabling efficient task-specific adaptation.
- **Abstract**: Proposes CRMA, a spectrally-bounded backbone for modular continual fine-tuning of LLMs that prevents catastrophic forgetting while enabling efficient task adaptation.

---

## CTR Prediction & Advertising Recommendation

### 12. UniPinRec: Unifying Generative Retrieval and Ranking at Pinterest Scale
- **Link**: [2606.00422](https://arxiv.org/abs/2606.00422)
- **Authors**: Hanyu Li, Yi-Ping Hsu, Aditya Mantha, et al.
- **Institution**: Pinterest
- **Key Innovation**: Unified generative retrieval and ranking architecture deployed at Pinterest scale, combining semantic ID-based retrieval with learned ranking in a single generative model.
- **Abstract**: Proposes UniPinRec unifying generative retrieval and ranking at Pinterest scale. Combines semantic ID-based retrieval with learned ranking in a single model.

### 13. Gated Bidirectional Linear Attention (GBLA) for Generative Retrieval
- **Link**: [2606.07317](https://arxiv.org/abs/2606.07317)
- **Authors**: Artem Matveev, Vladislav Tytskiy, Sergei Makeev, Sergei Liamaev
- **Institution**: Yandex
- **Key Innovation**: Linear-time bidirectional attention layer extending kernelized linear attention with local causal mixing (Conv1D), sequence-level key gating, and gated RMSNorm. Up to 8.2× single-layer speedup at 32768 history length vs FlashAttention-v3. Accepted at SIGIR 2026.
- **Abstract**: Proposes GBLA for efficient bidirectional attention in generative retrieval encoders. Hybrid 1:2 SA:GBLA matches full bidirectional self-attention quality. 8.2× speedup on long sequences at Yandex Music scale.

### 14. Taiji: Pareto Optimal Policy Optimization with Semantics-IDs Trade-off for Industrial LLM-Enhanced Recommendation
- **Link**: [2606.03866](https://arxiv.org/abs/2606.03866)
- **Authors**: Yuecheng Li, Zeyu Song, Jing Yao, Chi Lu, Peng Jiang, Kun Gai
- **Institution**: Kuaishou
- **Key Innovation**: Pareto optimal framework balancing semantic IDs and traditional ID representations in LLM-enhanced recommendation systems. Addresses the trade-off between semantic richness and collaborative signal preservation.
- **Abstract**: Proposes Taiji for Pareto optimal policy optimization with semantics-IDs trade-off in industrial LLM-enhanced recommendation.

### 15. Bradley-Terry Rankings for Recommender Systems Across Dataset Taxonomies
- **Link**: [2606.07492](https://arxiv.org/abs/2606.07492)
- **Authors**: Ekaterina Grishina, Stepan Kuznetsov, Askar Tsyganov, et al.
- **Institution**: (academic/industry)
- **Key Innovation**: Novel data-driven ranking methodology using Bradley-Terry model for fair comparison of recommendation algorithms. Introduces dataset-specific ranking prediction on unseen datasets via BT trees and covariate models. KDD'26.
- **Abstract**: Introduces BT-based ranking methodology for recommender system comparison. Ranking depends on key dataset statistics. Enables prediction of algorithm rankings on unseen datasets.

### 16. Dual-Stream MLP is All You Need for CTR Prediction
- **Link**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China
- **Key Innovation**: Knowledge distillation consolidates explicit feature interactions into a main MLP with parallel MLP for implicit interactions. SOTA across Criteo, Avazu, MovieLens despite being vanilla MLP. Accepted by TKDD.
- **Abstract**: Proposes DS-MLP using knowledge distillation for CTR prediction. Achieves SOTA across three benchmarks while maintaining low latency.

### 17. Dynamic Spectral Denoising with Global-Context Attention for Multi-Behavior Recommendation
- **Link**: [2606.02417](https://arxiv.org/abs/2606.02417)
- **Authors**: Miaomiao Cai, Yunshan Ma, Fangqi Zhu, et al.
- **Institution**: (academic)
- **Key Innovation**: Spectral denoising in frequency domain combined with global-context attention for multi-behavior recommendation. KDD'26.
- **Abstract**: Proposes dynamic spectral denoising with global-context attention for multi-behavior recommendation, addressing noise in user behavior signals.

### 18. Bridging Short Videos and Live Streams: Reasoning-Guided Multimodal LLMs for Cross-Domain Representation Learning
- **Link**: [2606.04448](https://arxiv.org/abs/2606.04448)
- **Authors**: Le Zhang, Xiaolan Zhu, Yuchen Wang, et al.
- **Institution**: Kuaishou
- **Key Innovation**: Reasoning-guided multimodal LLM framework bridging short video and live stream domains for cross-domain representation learning in recommendation.
- **Abstract**: Proposes reasoning-guided multimodal LLMs for bridging short videos and live streams, enabling cross-domain representation learning.

### 19. LLMs Need Encoders for Semantic IDs Too
- **Link**: [2606.00324](https://arxiv.org/abs/2606.00324)
- **Authors**: Xiangyi Chen, Zelun Wang, Xinyi Li, Yi-Ping Hsu, Jaewon Yang, Jiajing Xu
- **Institution**: Pinterest
- **Key Innovation**: Demonstrates that LLM-based recommenders benefit from dedicated encoders for semantic IDs rather than treating them as flat tokens. Proposes encoder architecture for improved semantic ID utilization.
- **Abstract**: Shows LLMs need dedicated encoders for semantic IDs in recommendation, proposing encoder architecture for better semantic ID utilization.

---

## Games, RL & Sequential Decision Making

### 20. DuMate-DeepResearch: Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning
- **Link**: [2606.07299](https://arxiv.org/abs/2606.07299)
- **Authors**: Lingyong Yan, Can Xu, Yukun Zhao, et al.
- **Institution**: Baidu
- **Key Innovation**: Multi-agent deep research framework with graph-based dynamic planning, recursive two-level search execution, and rubric-based test-time optimization. SOTA on DeepResearch Bench (58.03%) and DeepResearch Bench II (61.95%).
- **Abstract**: Introduces DuMate-DeepResearch, a multi-agent framework decoupling Agent Core from Tool Ecosystem. Graph-based dynamic planning, recursive search, rubric-based test-time optimization. New SOTA on two deep research benchmarks.

### 21. MindZero: Learning Online Mental Reasoning With Zero Annotations
- **Link**: [2606.00240](https://arxiv.org/abs/2606.00240)
- **Authors**: Shunchi Zhang, Jin Lu, Chuanyang Jin, Yichao Zhou, Zhining Zhang, Tianmin Shu
- **Institution**: (academic)
- **Key Innovation**: ICML 2026. Zero-annotation framework for learning Theory of Mind reasoning through online interaction, enabling agents to infer beliefs, desires, and intentions of other agents without any labeled data.
- **Abstract**: Proposes MindZero for learning online mental reasoning with zero annotations. ICML 2026.

### 22. Quantized Reasoning Models Think They Need to Think Longer, but They Do Not
- **Link**: [2606.00206](https://arxiv.org/abs/2606.00206)
- **Authors**: Sanae Lotfi, Polina Kirichenko, Steven Li, Zechun Liu
- **Institution**: (academic)
- **Key Innovation**: Counterintuitive finding that quantized reasoning models generate longer reasoning chains but achieve similar or worse accuracy. Suggests quantization disrupts the efficiency of reasoning without proportional quality loss.
- **Abstract**: Shows quantized reasoning models produce longer reasoning chains without corresponding accuracy improvements, challenging assumptions about quantization's impact on reasoning.

### 23. Robust Shielding for Safe Reinforcement Learning
- **Link**: [2606.00270](https://arxiv.org/abs/2606.00270)
- **Authors**: Edwin Hamel-De le Court, Thom Badings, Alessandro Abate, et al.
- **Institution**: (academic)
- **Key Innovation**: Formal framework for robust shielding in RL that guarantees safety constraints under environmental uncertainty and model misspecification, using abstract interpretation of the shield's safety properties.
- **Abstract**: Proposes robust shielding framework for safe RL, guaranteeing safety constraints under environmental uncertainty.

### 24. Agentic Transformers Provably Learn to Search via Reinforcement Learning
- **Link**: [2606.00183](https://arxiv.org/abs/2606.00183)
- **Authors**: Tong Yang, Yu Huang, Yingbin Liang, Yuejie Chi
- **Institution**: (academic)
- **Key Innovation**: Theoretical proof that transformer-based agents can learn to perform search behaviors through RL training, providing formal guarantees on the emergence of search capabilities from RL objectives.
- **Abstract**: Proves theoretically that agentic transformers learn to search via RL, providing formal guarantees on emergence of search capabilities.

### 25. Regret Minimization with Adaptive Opponents in Repeated Games
- **Link**: [2606.06486](https://arxiv.org/abs/2606.06486)
- **Authors**: (academic)
- **Institution**: (academic)
- **Key Innovation**: Regret minimization framework for repeated games where opponents adapt their strategies over time. Handles non-stationary opponent behaviors that break traditional no-regret guarantees.
- **Abstract**: Studies regret minimization in repeated games with adaptive opponents, addressing non-stationary opponent behaviors.

### 26. CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents
- **Link**: [2606.00756](https://arxiv.org/abs/2606.00756)
- **Authors**: Yannan Wang, Longli Yang, Zhen Liu, et al.
- **Institution**: (academic)
- **Key Innovation**: Cloud-edge multi-agent memory system where agents collaboratively share memories and insights for long-horizon tasks, with mechanisms for memory consolidation and circulation across distributed agents.
- **Abstract**: Proposes CoMIC for collaborative memory and insights circulation in long-horizon LLM agents operating in cloud-edge systems.

---

## Summary Statistics

| Category | Count | Key Venues |
|----------|-------|------------|
| LLMs & Foundation Models | 11 | arXiv cs.CL, cs.LG, cs.AI |
| CTR / Advertising / Recommendation | 8 | arXiv cs.IR, KDD'26, SIGIR'26, TKDD |
| Games, RL & Sequential Decision Making | 7 | arXiv cs.AI, cs.LG, ICML'26 |
| **Total** | **26** | |

**Industry representation**: Perplexity AI, Pinterest, Kuaishou, Baidu, Yandex

**Notable trends**:
- Agentic AI evaluation is maturing — AARR benchmark, Perplexity empirical studies, DuMate-DeepResearch multi-agent frameworks
- Speculative decoding and KV-cache efficiency remain active (BudgetDraft, BitsMoE)
- Generative retrieval with linear attention for long user histories (GBLA at SIGIR'26, UniPinRec at Pinterest)
- Reasoning overthinking is recognized as a problem (DyCon, Quantized Reasoning Models paper)
- LLMs for recommendation increasingly deal with semantic IDs vs traditional ID tradeoffs (Taiji, LLMs Need Encoders for Semantic IDs Too)
- Collaborative agent memory for long-horizon tasks (CoMIC, Agentopia)
- Safety and privacy in reasoning models (Hidden Thoughts Are Not Secret, Robust Shielding)
