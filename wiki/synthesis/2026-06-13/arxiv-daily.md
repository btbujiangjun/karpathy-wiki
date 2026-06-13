---
title: "arXiv Daily — 2026-06-13"
type: synthesis
created: 2026-06-13
updated: 2026-06-13
sources: []
tags: [arxiv-daily, llm, recommendation, ctr, games, sequential-modeling, reinforcement-learning, transformers, sparse-attention, moe, reasoning, dpo]
---

# arXiv Daily — 2026-06-13

Recent papers spanning AI, LLMs, recommendation systems, CTR prediction, sequential modeling, games, and related areas. Papers are primarily from June 2026 submissions.

---

## LLMs & Architectures

### 1. MiniMax Sparse Attention (MSA)
- **Authors**: Xunhao Lai, Weiqi Xu, Yufeng Yang, Qiaorui Chen, Yang Xu, Lunbin Zeng, Xiaolong Li, Haohai Sun, Haichao Zhu, Vito Zhang, Pengyu Zhao
- **Institution**: MiniMax-AI
- **Link**: https://arxiv.org/abs/2606.13392
- **Abstract**: Introduces blockwise sparse attention built upon GQA. A lightweight Index Branch scores KV blocks and selects Top-k per GQA group for group-specific sparse retrieval; Main Branch performs exact block-sparse attention over selected blocks. Co-designed GPU kernel uses exp-free Top-k selection and KV-outer sparse attention. On a 109B MoE model, MSA matches GQA quality while reducing per-token attention compute by 28.4× at 1M context, achieving 14.2× prefill and 7.6× decoding wall-clock speedups on H800.
- **Key Innovations**: Blockwise sparse attention with group-specific Top-k; lightweight index branch decoupled from main attention; production-grade deployment at 109B scale; open-source inference kernel.

### 2. MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling
- **Authors**: Jiacheng Chen, Xinyu Zhang, Shunkai Zhang, Yanmohan Wang, Lin Li, Tiancheng Qin, Qin Wang, Zhengmao Zhu, Tianle Li, Jingyang Li, Zehan Li, Binyang Jiang, Jin Zhu, Han Ding, Fei Yu, Chenyu Du, Zijian Song, Jiayuan Song, Zhi Zhang, Yunan Huang, Weiyu Cheng, Pengyu Zhao, Yu Cheng
- **Institution**: MiniMax-AI
- **Link**: https://arxiv.org/abs/2606.13473
- **Abstract**: Population-level test-time scaling framework for competition-level math proof (MiniMax-M3 series). Trains proof generation, verification, and critique-conditioned repair using a defense-in-depth generative verifier with low false-positive rate. At test time, searches over a population of candidate proofs via tournament selection. M3 + MaxProof reaches 35/42 on IMO 2025 and 36/42 on USAMO 2026, exceeding human gold-medal threshold.
- **Key Innovations**: Generative verifier with defense-in-depth design; population-level test-time scaling; tournament selection for proofs; exceeds human gold-medal on IMO/USAMO.

### 3. Select and Improve: Understanding the Mechanics of Post-Training for Reasoning
- **Authors**: Akshay Krishnamurthy, Audrey Huang, Nived Rajaraman
- **Institution**: —
- **Link**: https://arxiv.org/abs/2606.13125
- **Abstract**: Mechanistic study of how RL post-training enhances reasoning capabilities. Controlled experiments with Qwen-2.5-1.5B on math reasoning reveal two core mechanisms: strategy selection (activated by SFT on diverse reasoning strategies) and strategy improvement (activated by increasing difficulty in RL data). Provides practical interventions for scaling reasoning capabilities.
- **Key Innovations**: Identifies strategy selection + strategy improvement as distinct RL mechanisms; shows SFT data diversity enables selection; shows RL data difficulty drives improvement.

### 4. Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy RL (SWITCH)
- **Authors**: Jiayu Yang, Chao Chen, Shengen Wu, Yinhong Liu, Yuxuan Fan, Lujundong Li, Songning Lai, Chengwei Qin, Zhijiang Guo
- **Institution**: —
- **Link**: https://arxiv.org/abs/2606.13106
- **Abstract**: Proposes SWITCH, using discrete boundary tokens (`<swi>`/`</swi>`) to make latent chain-of-thought compatible with standard on-policy RL (GRPO). Trains via visible-to-latent curriculum and Switch-GRPO objective. Mechanistic analysis reveals: `<swi>` is a sharply localized learned switching policy; the latent step performs causally important computation; computation concentrates at a single hidden-state transition on entry.
- **Key Innovations**: Boundary tokens make latent reasoning RL-trainable; Switch-GRPO objective; mechanistic interpretability of latent reasoning via anchors.

### 5. Parallel Causal Associative Fields: Gated Sparse Memory for Long-Context Language Modeling (PCAF)
- **Authors**: Muhammad Ahmed
- **Institution**: —
- **Link**: https://arxiv.org/abs/2606.10435
- **Abstract**: Parallel content-addressed memory over causal successor records. Writes local records into hash buckets, retrieves bounded candidate set per query, forms sparse cache distribution over successor tokens, mixes with parametric local LM via learned gate. At 303M params / T=2048 on TPU v4-32, PCAF achieves 36.31 PPL (WikiText-103) vs 47.49 for dense Transformer, processing 0.61–0.62M tok/s vs 0.43M tok/s.
- **Key Innovations**: Third primitive beyond attention and RNN/SSM; hash-bucket associative memory; learned gating between cache and local LM; Pareto-improves speed-quality over dense attention.

---

## Recommendation Systems & CTR

### 6. OneRetrieval: Unifying Multi-Branch E-commerce Retrieval with an Editable Generative Model
- **Authors**: Xuxin Zhang, Ben Chen, Yue Lv, Siyuan Wang, Yupeng Li, Yufei Ma, Zihan Liang, Tong Zhao, Ying Yang, Huangyu Dai, Lingtao Mao, Zhipeng Qian, Xinyu Sun, Chenyi Lei, Wenwu Ou, Kun Gai
- **Institution**: Kuaishou
- **Link**: https://arxiv.org/abs/2606.13533
- **Abstract**: First editable generative retrieval method replacing multi-branch e-commerce search with one model. Keyword-Aligned Encoding (KAE) ties each identifier position to an interpretable attribute word. Reserved codebook slots bind to new words post-deployment without retraining. On 5M real requests, matches strongest generative baseline recall with intervention hit rate >10× above closed-codebook methods. Deployed at Kuaishou, lifting order volume when replacing inverted-index branch.
- **Key Innovations**: Editable generative retrieval (first of its kind); Keyword-Aligned Encoding; post-deployment term injection without retraining; 400×+ inference acceleration vs LLM methods; deployed at scale.

### 7. Generative Archetype-Grounded Item Representations for Sequential Recommendation (GenAIR)
- **Authors**: Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, Yankai Chen, Wenhao Yu, Jianting Chen, Irwin King
- **Institution**: CUHK (The Chinese University of Hong Kong)
- **Link**: https://arxiv.org/abs/2606.11023
- **Abstract**: LLM generates "Archetype" descriptions (ideal target audience profile) from item metadata; extracts embeddings in a single forward pass. Behavioral calibration objective adjusts embedding space using real interaction signals. Integrates seamlessly with most existing sequential recommenders. Significant improvements on three real-world datasets. WWW 2026 Oral.
- **Key Innovations**: Archetype-based item representation from LLM; behavioral calibration bridging semantic and behavioral spaces; plug-and-play compatibility with existing models.

### 8. Atomic Intent Reasoning: Bringing LLM Semantics to Industrial Cross-Domain Recommendations (AIR)
- **Authors**: Zhuohang Jiang, Yuxin Chen, Shijie Wang, Haohao Qu, Zhou Jindong, Wenqi Fan, Li Qing, Dongxu Liang, Jun Wang
- **Institution**: Kuaishou / The Hong Kong Polytechnic University
- **Link**: https://arxiv.org/abs/2606.10357
- **Abstract**: LLM-driven cross-domain recommendation framework for content-to-e-commerce platforms. Migrates LLM inference to offline phase; dynamically constructs user intent representations via efficient retrieval and composition online (~400× acceleration). SOTA on multiple public datasets. Online A/B at Kuaishou E-commerce: +3.446% GMV improvement. KDD 2026.
- **Key Innovations**: Offline LLM inference + online retrieval composition; ~400× speedup; atomic intent decomposition; industrial deployment at Kuaishou scale.

### 9. Mult-DPO: Multinomial Direct Preference Optimization for Recommender Systems
- **Authors**: Yaochen Zhu, Harald Steck, James McInerney, Aditya Sinha, Yinhan He, Nathan Kallus, Jundong Li
- **Institution**: Netflix / University of Virginia
- **Link**: https://arxiv.org/abs/2606.10078
- **Abstract**: Generalizes DPO from pairwise to set-wise preferences (multiple positives, multiple negatives). Proposes tractable multinomial surrogate likelihood over set-wise preference events. Proves multinomial DPO loss is a tractable upper bound on marginalized Plackett-Luce DPO loss. Extends to multi-level preference alignment.
- **Key Innovations**: First DPO generalization to set-wise preferences for recsys; closed-form multinomial surrogate; theoretical bound on PL marginalization; multi-level preference extension.

### 10. DiffCold: A Diffusion-based Generative Model for Cold-Start Item Recommendation
- **Authors**: Kangning Zhang, Yingjie Qin, Weinan Zhang, Yong Yu, Jianghao Lin
- **Institution**: Shanghai Jiao Tong University
- **Link**: https://arxiv.org/abs/2606.12245
- **Abstract**: Solves the seesaw dilemma (improving cold items degrades warm items) via conditional diffusion that reconstructs warm item embeddings from content. Retrieval-enhanced Aggregator initializes generation using semantically similar warm items. Simulation-based Representation Alignment enforces distribution consistency via contrastive learning. ECML-PKDD 2026.
- **Key Innovations**: Diffusion-based resolution of cold-warm tradeoff; retrieval-enhanced diffusion initialization; bypasses GAN/VAE limitations for representation generation.

### 11. LLM-Based User Personas for Recommendations at Scale
- **Authors**: Haoting Wang, Haokai Lu, Zheyun Feng, Jenny Huang, Yifat Amir, Gregory Hinkson, Ben Most, Zelong Zhao, Yixin Kelly Cui, Rein Zhang, Fabio Soldo, Yu Xia, Nihar Bhupalam, Minmin Chen, Konstantina Christakopoulou, Lichan Hong, Ed H. Chi
- **Institution**: Google
- **Link**: https://arxiv.org/abs/2606.12198
- **Abstract**: Real-time LLM-based user interest persona generation for large-scale commercial video recommendation. Natural-language personas address exploitation-exploration tradeoff by combining summarized existing interests with novel topics during serving. Cost-efficient architecture via knowledge distillation, async inference, and semantically clustered video representations. Significant improvements in viewer value via offline eval, user studies, and live A/B tests.
- **Key Innovations**: Real-time LLM persona generation at billion-user scale; exploitation-exploration via natural language; knowledge distillation for cost efficiency.

### 12. τ-Rec: A Verifiable Benchmark for Agentic Recommender Systems
- **Authors**: Bharath Sivaram Narasimhan, Karthik R Narasimhan
- **Institution**: Princeton University
- **Link**: https://arxiv.org/abs/2606.10156
- **Abstract**: Replaces subjective "LLM-as-judge" evaluation with verifiable rewards and a reveal-tagged elicitation (RTE) mechanism controlling how task constraints surface during dialogue. Tests 9 configurations across 5 model families (GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Flash, DeepSeek V4 Flash, Qwen3-32B, GPT-5 mini). Reveals steep reliability cliff: best model ~57% at pass^1, ~38% at pass^4.
- **Key Innovations**: Verifiable reward benchmark for agentic recsys; RTE mechanism; pass^k reliability metric; reveals critical reliability gap in current conversational agents.

### 13. Representation Curriculum: Stagewise Training for Robust Ranking and Allocation
- **Authors**: Ehsan Ebrahimzadeh, Sina Baharlouei, Abraham Bagherjeiran
- **Institution**: —
- **Link**: https://arxiv.org/abs/2606.09891
- **Abstract**: Training-time intervention that temporally stages feature utilization for ranking. Foregrounds content-based merit signals initially, then introduces exposure-dependent belief signals while anchoring content pathway. Derives closed-form solutions and sufficient conditions where RC strictly reduces cold-start population risk. Validated on public LTR/recsys benchmarks and large-scale e-commerce search A/B.
- **Key Innovations**: Stagewise curriculum for ranking features; mitigates shortcut reliance on exposure-confounded signals; theoretical guarantees for cold-start generalization; e-commerce deployment.

---

## Reinforcement Learning, Multi-Agent & Games

### 14. Multi-Agent RL from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch
- **Authors**: Haochen Wu, Yi Hou, Shiguang Xie
- **Institution**: DoorDash
- **Link**: https://arxiv.org/abs/2606.13604
- **Abstract**: Deployed RL system at DoorDash adapting dispatch objective weights using delayed marketplace signals. A store-level policy selects discrete multipliers shifting the dispatch optimizer's tradeoff between delivery quality and batching efficiency. Uses centralized offline data + decentralized store-level execution with Double Q-learning and conservative regularization. Production switchback shows increased batching and reduced courier time without degrading delivery quality.
- **Key Innovations**: RL from world feedback in three-sided marketplace; discrete multiplier interface to combinatorial optimizer; safe offline-to-online policy deployment; real logistics platform at scale.

### 15. Stability in Competitive Search with Results Diversification
- **Authors**: Itamar Reinman, Omer Madmon, Moshe Tennenholtz, Oren Kurland
- **Institution**: Technion
- **Link**: https://arxiv.org/abs/2606.10053
- **Abstract**: Game-theoretic analysis of competitive search with diversification. Publishers strategically modify documents in response to rankings. Reveals inherent tradeoff between corpus diversity and stability (equilibrium). Analyzes two diversification methods showing stability may not be reached. Proposes diversification-based ranking functions guaranteed to lead to stability. ICTIR 2026.
- **Key Innovations**: Formal game-theoretic model of competitive search with diversification; identifies diversity-stability tradeoff; diversification functions with stability guarantees.

---

## Tool Use & RAG

### 16. ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs
- **Authors**: Ashutosh Hathidara, Sai Shruthi Sistla, Sebastian Schreiber, Sahil Bansal
- **Institution**: —
- **Link**: https://arxiv.org/abs/2606.12451
- **Abstract**: Open-source diagnostic framework for auditing parametric tool knowledge in LLMs. Automatically generates three benchmarks from any tool catalog: Realistic Retrieval Benchmark (RRB) with 3 ambiguity tiers, MCQ probing benchmark, and QA probing benchmark. Applied to ToolBench (~47k tools) revealing knowledge-retrieval dissociation: RRB collapses ~50-64pp vs fully-specified benchmarks; near-random on factual probes despite strong retrieval.
- **Key Innovations**: Automatic diagnostic benchmark generation; reveals dissociation between retrieval performance and actual tool knowledge; realistic ambiguity-tiered queries.

---

<details>
<summary>Summary Statistics</summary>

- **Total papers**: 16
- **Categories**: LLM Architectures (5), Recommendation/CTR (8), RL/Multi-Agent/Games (2), Tool Use/RAG (1)
- **Notable venues**: KDD 2026, WWW 2026 Oral, ECML-PKDD 2026, ICTIR 2026, ICML 2026 Workshops
- **Industry deployments**: Kuaishou (OneRetrieval, AIR), DoorDash (MARL dispatch), Google (LLM Personas), Netflix (Mult-DPO)
</details>
