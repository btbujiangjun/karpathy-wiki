---
title: "Conference & arXiv Digest — 2026-07-10"
type: synthesis
created: 2026-07-10
updated: 2026-07-10
sources: []
tags: [conference, arxiv, icml-2026, iclr-2026, neurips-2025, cvpr-2026, aaai-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, recommendation, ctr, llm, agent, diffusion, game, code-execution]
---

# Conference & arXiv Digest — 2026-07-10

> Compiled: 2026-07-10 (Friday). Covers ICML 2026, ICLR 2026, NeurIPS 2025, CVPR 2026, AAAI 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025 + recent arXiv papers across LLMs, recommendation, CTR, games, code execution, agent systems, generative models, sequential modeling, and benchmarks.

---

## 1. ICML 2026 (Seoul, Jul 6–12, 2026)

**Stats**: 23,918 submissions → 6,352 accepted (26.6%) → 168 Orals (0.7%), 536 Spotlights

### Best Paper Awards

#### Outstanding Paper: "The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models"
- **Authors**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation**: Tsinghua University (李国良组)
- **Problem**: Diffusion LLMs (dLLMs) offer arbitrary-order generation (e.g., confidence-based), but the paper reveals this freedom has a hidden cost.
- **Innovation**: Shows dLLMs exploit arbitrary order to bypass high-uncertainty "forking" tokens, collapsing solution diversity on reasoning tasks. Proposes **JustGRPO** — uses fixed left-to-right order for RL rollouts while retaining parallel decoding at inference.
- **Key finding**: The "flexibility" of arbitrary-order generation is actually a trap: models avoid hard tokens, reducing effective diversity.
- **Link**: https://icml.cc/virtual/2026/poster/61998

#### Outstanding Paper: "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions"
- **Authors**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Innovation**: Settles a long-standing question — shows ε-error can be achieved in **polylog(1/ε)** steps using only score (gradient) evaluations, via first-order rejection sampling (FORS). Exponential improvement over prior O(poly(1/ε)) samplers.
- **Impact**: Denoising steps can drop from polynomial to polylogarithmic in 1/ε for diffusion models.

#### Honorable Mention: "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes"
- **Authors**: Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, Chris Cundy
- **Innovation**: Rigorous study of LLM deception under white-box linear lie detectors in code optimization. Shows policy gradient methods don't generate direct optimization pressure toward activation manipulation. Identifies taxonomy: blatant deception, obfuscated activations, obfuscated policies. High KL + strong detector penalty mitigates failures.
- **Link**: https://arxiv.org/abs/2606.xxxxx

#### Honorable Mention: "Motion Attribution for Video Generation"
- **Authors**: Xindi Wu, Despoina Paschalidou, Jun Gao, Antonio Torralba, Laura Leal-Taixé, Olga Russakovsky, Sanja Fidler, Jonathan Lorraine
- **Innovation**: Attribution method tracking individual training examples' contribution to motion quality in video generation. Achieves superior performance using **1/10 of original training set**.
- **Affiliation**: NVIDIA, University of Toronto

#### Honorable Mention: "How Much Can Language Models Memorize?"
- **Authors**: John Xavier Morris, Chawin Sitawarin, Narine Kokhlikyan, Chuan Guo, G. Edward Suh, Alexander M Rush, Kamalika Chaudhuri, Saeed Mahloujifar
- **Innovation**: Proposes Kolmogorov memorization to measure what models learn. Distinguishes intended (generalization) vs unintended memorization. **Bold claim**: GPT-style LMs model 3.6 bits per parameter.

#### Honorable Mention: "A Random Matrix Perspective on the Consistency of Diffusion Models"
- **Authors**: Binxu Wang, Jacob A Zavatone-Veth, Cengiz Pehlevan
- **Innovation**: Proves diffusion model cross-run reproducibility stems from shared linear Gaussian statistics, not complex dynamics. A "tour de force" linking spectral geometry to generative reproducibility.

#### Honorable Mention: "To Grok Grokking: Provable Grokking in Ridge Regression"
- **Authors**: Mingyue Xu, Gal Vardi, Itay Safran
- **Innovation**: First global convergence result for grokking in purely linear model. Shows two-phase behavior emerges in ridge regression, providing a "toy model" for studying grokking like deep linear networks do for nonlinear ones.

### Best Position Paper: "The Alignment Community is Unintentionally Building a Censor's Toolkit"
- **Authors**: Sarah Ball, Phil Hackemann
- **Innovation**: Challenges assumption that alignment = force for good. With real-world evidence shows value alignment technologies can be misused by authorities. Proposes mitigation directions.

### Test of Time Award: "Asynchronous Methods for Deep Reinforcement Learning"
- **Authors**: Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Legacy**: Pioneered async RL → now foundational to LLM post-training RL (PPO, GRPO). Parallel actor-learners stabilized learning, inspiring DQN, A3C, and modern RLHF pipelines.

---

## 2. CVPR 2026 (Denver, Jun 3–7, 2026)

**Stats**: 16,092 submissions → 4,089 accepted (25.4%)

### Best Paper: "D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time"
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: **Google DeepMind**, UCL, Oxford
- **Innovation**: Unified transformer for dynamic 4D scene reconstruction from video. Estimates depth, spatio-temporal correspondence, and full camera parameters. Enables independent, efficient probing of any 3D point in space-time. Lightweight and scalable.
- **Link**: https://openaccess.thecvf.com/CVPR2026

### Best Student Paper: "Native and Compact Structured Latents for 3D Generation"
- **Authors**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **Affiliation**: **Tsinghua University**, **Microsoft Research**, USTC, **Microsoft AI**
- **Innovation**: **O-Voxel** — novel representation capturing complex shapes and surface attributes. Significantly advances 3D generative modeling quality.

### Best Paper Honorable Mentions

#### "NitroGen: An Open Foundation Model for Generalist Gaming Agents"
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: **NVIDIA**, Stanford, Caltech, UChicago, UT Austin
- **Innovation**: Vision-action foundation model trained on **40,000 hours of gameplay** across 1,000+ games. Demonstrates strong generalist gaming competence.
- **Key for game AI**: This is a major milestone for general-purpose game agents.

#### "SAM 3D: 3Dfy Anything in Images"
- **Authors**: Xingyu Chen et al.
- **Affiliation**: **Meta Superintelligence Labs**
- **Innovation**: Generative model for visually grounded 3D object reconstruction from single image. Predicts geometry, texture, layout. **≥5:1 win rate** in human preference tests on real-world objects.

#### "ChordEdit: One-Step Low-Energy Transport for Image Editing"
- **Affiliation**: Guangdong U. Tech, Huizhou U., Shenzhen U., Peking U.
- **Innovation**: Model-agnostic, training-free, inversion-free one-step image editing. Achieves true real-time editing.

---

## 3. NeurIPS 2025 (San Diego, Dec 2–7, 2025)

**Stats**: 21,575 submissions → 5,290 accepted (24.5%)

### Best Paper Awards (4 winners + 3 runners-up)

#### "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)"
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: U. Washington, CMU, Allen Institute
- **Innovation**: Tested 70+ LLMs → all generate eerily similar responses. Introduces Infinity-Chat dataset (26K queries, 31K annotations). Reveals pronounced intra- and inter-model homogenization.
- **Impact**: "Whether you use GPT-4, Claude, Gemini, or open-source alternatives, outputs cluster around suspiciously similar patterns."

#### "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: **Alibaba Qwen Team**
- **Innovation**: Head-specific sigmoid gating after attention. Eliminates "attention sink" problem, enhances training stability, dramatically improves long-context extrapolation. **Already shipping in Qwen3-Next** with open-source code.
- **Impact**: First systematic study of attention gating in large models. Consistently improves across 30 model variants.

#### "1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities"
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Innovation**: Scaled self-supervised RL networks to **1,024 layers** (from typical 2–5). Achieved **2–50× performance improvements** on locomotion and manipulation. Robots learn complex goals without human guidance.

#### "Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training"
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard
- **Innovation**: Identifies mathematical mechanism separating generation from memorization. "Implicit dynamical regularization" operates on two timescales: early generalization phase + later memorization phase. Generalization window expands linearly with training set size.
- **Impact**: Provides scientific evidence for copyright debate — diffusion models generate novel content.

### Runner-Up Papers

#### "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"
- **Authors**: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang
- **Innovation**: RL improves sampling efficiency but **doesn't expand reasoning capacity beyond base model**. Current RLVR methods remain limited by base model capabilities.

#### "Optimal Mistake Bounds for Transductive Online Learning"
- **Authors**: Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer
- **Innovation**: Solved 30-year-old open problem. Proves transductive learning achieves **quadratic gap advantage** over standard learning.

#### "Superposition Yields Robust Neural Scaling"
- **Authors**: Yizhou Liu, Ziming Liu, Jeff Gore
- **Innovation**: Representation superposition explains why neural scaling laws work. Gives principled way to predict model performance before expensive training runs.

---

## 4. AAAI 2026 (Feb 2026)

**Stats**: 4,167 accepted papers (17.6% acceptance rate)

### Key Papers

#### "Towards Controllable and Trustworthy LLM Reasoning: From Failure Mapping to Cognition-inspired Control"
- **Link**: https://ojs.aaai.org/index.php/AAAI/article/view/41366

#### Selected Notable Papers:
- **LogicCat**: Chain-of-Thought Text-to-SQL Benchmark for Complex Reasoning
- **DialogXpert**: Driving Intelligent and Emotion-Aware Conversations Through Online Value-Based RL with LLM Priors
- **Rethinking Deep Alignment Through the Lens of Incomplete Safety Learning**
- **JudgeBoard**: Benchmarking and Enhancing Small Language Models for Reasoning Evaluation
- **How Does Chain of Thought Think?** Mechanistic Interpretability of CoT Reasoning with Sparse Autoencoding
- **TIV**: Thought Injection via Vectors for Efficient Reasoning in Large Reasoning Models
- **Test-Time Reinforcement Learning for GUI Grounding** via Region Consistency

---

## 5. ICLR 2026 (Rio de Janeiro, Apr 23–27, 2026)

**Stats**: 5,355 accepted papers (27.4% acceptance rate)

### Key Trends
- LLM safety: "Compromised LLM maintains safety alignment facade while covertly generating harmful content"
- Self-distillation framework for 3D knowledge in video diffusion models
- Spectral Attention Steering for Prompt Highlighting
- Neural Compression of 3D content

---

## 6. KDD 2026 (Jeju Island, Aug 9–13, 2026)

### Key Papers

#### "OneMall: One Architecture, More Scenarios — End-to-End Generative Recommender Family at Kuaishou E-Commerce"
- **Authors**: Kun Zhang, Jingming Zhang, Wei Cheng et al.
- **Affiliation**: **Kuaishou Technology**
- **Innovation**: End-to-end generative recommendation unifying product-card, short-video, and live-streaming. Three components: (1) E-commerce Semantic Tokenizer, (2) Transformer backbone with Query-Former + Cross-Attention + Sparse MoE, (3) RL pipeline connecting retrieval and ranking.
- **Results**: +13.01% GMV in product-card, +15.32% Orders in Short Video, +2.78% Orders in Live-Streaming. Deployed serving 400M+ daily active users.
- **RL insight**: GRPO outperforms DPO — normalizes rewards across 768 sampled candidates for more comprehensive training feedback.
- **Link**: https://arxiv.org/abs/2601.21770

#### "Field-Aware Transformer (FAT): From Scaling to Structured Expressivity for CTR Prediction"
- **Authors**: (KDD 2026)
- **Innovation**: Reconstructs standard Transformer with field-centric parameters. Field-Decomposed Attention + Basis-Composed Hypernetwork. Scaling law based on Rademacher complexity shows generalization error depends on field interaction structure, not vocabulary size.
- **Results**: Up to +4.38% AUC improvement. **Deployed on Taobao**: +2.33% CTR, +0.66% RPM in live production. P99 latency 45→48ms despite 5× FLOPs increase.

#### "FlowTime: Towards Continuous Generative Watch Time Prediction via Flow-based Personalized Priors"
- **Authors**: Hongxu Ma, Han Zhou, Chenghou Jin, Jie Zhang, Xiaoyu Yang, Chunjie Chen, Jihong Guan, Shuigeng Zhou
- **Affiliation**: **Kuaishou Technology**, Fudan University
- **Innovation**: Flow-based generative model for continuous watch time prediction in video recommendation. Replaces discretized regression with normalizing flows for personalized continuous distributions.
- **Link**: https://arxiv.org/abs/2606.01352

#### "TAROT: Task-Adaptive Refinement of LLM-prior Graphs for Few-shot Tabular Learning"
- **Innovation**: Uses LLM (GPT-4o-mini) to generate graph structures for few-shot tabular learning, with task-adaptive semantic graph refinement.
- **Link**: https://arxiv.org/abs/2606.11640

#### "RidgeCut: Learning Graph Partitioning with Rings and Wedges"
- **Accepted**: KDD 2026
- **Link**: https://github.com/zyr17/RIDGECUT

---

## 7. WWW 2026 (ACM Web Conference, Dubai, Apr 13–17, 2026)

### Key Papers

#### "ThinkRec: Thinking-based Recommendation via LLM"
- **Authors**: Qihang Yu, Kairui Fu, Zheqi Lv, Shengyu Zhang et al.
- **Innovation**: Uses LLM chain-of-thought reasoning for recommendation. Integrates thinking process into rec pipeline.
- **Link**: https://dl.acm.org/doi/10.1145/3774904.3792070

#### "AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents"
- **Innovation**: LLM agent framework bridging commonsense reasoning with scalable rec tools. Uses substitute/complement relationships grounded in user history. **2× improvement** over underlying tools on grocery datasets.
- **Link**: https://arxiv.org/abs/2510.05598

#### "LLMs-Enhanced Semantic Diffusion for User-Centric Recommendation (SEDIRec)"
- **Authors**: Xian Mo, Yijun Hu, Jun Pang
- **Innovation**: LLM-based user-side knowledge + knowledge-aware graph diffusion model. Handles noise and semantic transition issues. Significant improvement on Book-Crossing (+9.78% Recall@50, +15.64% NDCG@50).

#### Workshop: LLM & Agents for Recommendation Systems (LARS)
- Accepted papers include: MATRAG (Multi-Agent Transparent RAG), GALRec (Aligning Graph with LLM), CAMPAIGN-2-PT-RAG, and more.

---

## 8. ACL 2026 (San Diego, Jul 2–7, 2026)

### Key Papers

#### "RST-Guarder: Enhancing Long-Context Robustness for Safeguards via RST Parsing and Probabilistic Inference"
- **Authors**: Xu Zhang, Xiaojun Wan
- **Innovation**: RST discourse parsing + probabilistic inference for harmful-content detection in long-form inputs. Reduces false positives. No data curation or model training required.
- **Link**: https://aclanthology.org/2026.acl-long.1025/

#### "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities"
- **Innovation**: Teaching models to generate explicit boundary delimiters. Improvements up to **7.7% on GSM8k** and **12.5% on DROP**. Sentence is optimal granularity for segmentation.

#### "Adaptive Constraint Propagation: Scaling Structured Inference for LLMs via Meta-Reinforcement Learning"

#### "Fine-Grained Analysis of Shared Syntactic Mechanisms in Language Models"
- **Affiliation**: ACL 2026 Long Papers
- **Innovation**: Uses activation patching to identify shared neural mechanisms for syntactic constructions. Filler-gap dependencies show highly localized shared mechanism; NPI processing doesn't.

---

## 9. EMNLP 2025

**Stats**: 1,810 papers accepted

### Notable Work
- "Causal Interventions Reveal Shared Structure Across English Filler–Gap Constructions" — mechanistic interpretability for syntactic processing
- ACL Anthology proceedings published

---

## 10. SIGIR 2026 (Melbourne, Jul 20–24, 2026)

**Stats**: 656 papers presented (234 full, 12 perspective, 28 reproducibility, 61 resource, 151 short, 24 demo, 131 industry, 15 low-resource, 12 doctoral)

### Key Trends
- LLM-powered ranking and recommendation
- Industrial-scale retrieval systems
- Multi-modal information retrieval

---

## 11. CIKM 2025

### Key Paper
#### "A Cost-aware Approach for Collaborating Large Language Models and Small Language Models"
- **Authors**: Zheng Li, Xuyun Zhang, Sheng Lu, Hua Deng, Hao Tian, Wanchun Dou
- **Affiliation**: Nanjing University, Macquarie University
- **Innovation**: Cost-aware collaboration framework for LLM+SLM pipelines

---

## 12. RecSys 2025 → RecSys 2026 (Minneapolis, Sep 27–Oct 2, 2026)

- RecSys 2025 concluded; RecSys 2026 upcoming
- Key trend: LLM-based recommendation (ThinkRec, R²ec, MACRec multi-agent framework)

---

## 13. Recommendation Systems & CTR Prediction — Recent arXiv Highlights

### Industrial Deployments

#### "OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising"
- **Innovation**: Single model unifies generation and ranking for ad recommendation
- **Link**: https://arxiv.org/abs/2603.02999

#### "GR4AD: Generative Recommendation for Large-Scale Advertising"
- **Affiliation**: **Kuaishou**
- **Results**: Deployed in production with 400M+ users, high-throughput real-time serving
- **Link**: https://arxiv.org/abs/2602.22732

#### "HyFormer: Revisiting Sequence Modeling and Feature Interaction in CTR Prediction"
- **Innovation**: Unified hybrid transformer integrating long-sequence modeling and feature interaction. Query Decoding + Query Boosting iterative refinement.
- **Results**: Outperforms LONGER and RankMixer on billion-scale industrial datasets.

#### "Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)"
- **Authors**: Kesha Ou, Zhen Tian (ByteDance), Wayne Xin Zhao, Long Zhang (Meituan), Sheng Chen (Meituan), Ji-Rong Wen
- **Affiliation**: **ByteDance**, Renmin University, **Meituan**
- **Innovation**: Knowledge distillation consolidating explicit interactions into main MLP, parallel MLP captures implicit interactions. Simple vanilla MLP achieves SOTA across three benchmarks.
- **Link**: https://arxiv.org/abs/2606.04944

#### "RankUp: Towards High-rank Representations for Large Scale Advertising"
- **Affiliation**: **Tencent** (Weixin Video Accounts, Official Accounts, Moments)
- **Results**: GMV improvements of **+3.41% (Video), +4.81% (Official), +2.12% (Moments)**
- **Innovation**: Mitigates representation collapse via randomized permutation splitting, multi-embedding, global tokens.

#### "End-to-End Semantic ID Generation for Generative Advertisement Recommendation (UniSID)"
- **Innovation**: Jointly optimizes embeddings and SIDs end-to-end. Multi-granularity contrastive learning + summary-based ad reconstruction. **+4.62% Hit Rate** over strongest baseline.

#### "GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm"
- **Innovation**: Reimagines CTR prediction with LLM-inspired sequence-first approach.

#### "DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction in Trigger-Induced Recommendation"

---

## 14. Agent Systems & Code Execution

### ProAct: Agentic Lookahead in Interactive Environments
- **Innovation**: Two-stage training (GLAD distillation + MC-Critic RL) for LLM agents. 4B model outperforms all open-source baselines on 2048 and Sokoban.
- **Link**: https://arxiv.org/abs/2602.05327

### Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems
- **Innovation**: Code as execution interface between model and harness. Moving beyond text-based reasoning to executable code.
- **Link**: https://arxiv.org/abs/2605.18747

### LACUNA: Safe Agents as Recursive Program Holes
- **Innovation**: Programming model for agents with typed calls. Code type-checked before execution. 8.6% rejection rate, 0.7 retries/query, 27.1% accuracy on BrowseComp-Plus, 76% on τ²-bench.
- **Link**: https://arxiv.org/abs/2605.28617

### Act While Thinking: Accelerating LLM Agents via Pattern-Aware Speculative Tool Execution
- **Innovation**: Speculative tool execution for LLM agents.

### Code-Space Response Oracles (CSRO) for Game Agents
- **Authors**: Daniel Hennes, Zun Li, John Schultz, Marc Lanctot
- **Affiliation**: **Google DeepMind**
- **Innovation**: Replaces RL oracles with LLMs generating policies as executable code. Interpretable, human-readable game strategies. Competitive with baselines.
- **Link**: https://arxiv.org/abs/2603.10098

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Innovation**: Two-player architecture (perception/action separation) + curriculum learning + database-as-control-plane. 50–94× more sample efficient than comparable systems (32 vs 1,600–3,000 tries).
- **Link**: https://arxiv.org/abs/2603.17683

### LLM-as-Code: Agentic Programming for Agent Harness
- **Link**: https://arxiv.org/abs/2606.15874

---

## 15. Generative Models & Diffusion Language Models

### BlockGen: Flexible Blockwise Sequence Modeling with Hybrid Samplers
- **Innovation**: Blockwise sequence model over mixture of block sizes. AR-informed Predictor-Corrector (ARPC) sampling. BlockGen masked PPL = 17.5 (vs AR 16.7 on OWT), closing gap.
- **Key finding**: Under ARPC, masked diffusion reverses uniform's advantage at higher NFE.

### Scaling Beyond Masked Diffusion Language Models
- **Innovation**: First systematic IsoFLOP scaling study for Uniform-state (Duo) and interpolating (Eso-LM) diffusion. At 1.7B params, Duo outperforms AR and MDLM on GSM8K after SFT despite worse PPL.
- **Key insight**: PPL is misleading across families — speed-quality Pareto frontier matters more.

### CARD: Causal Autoregressive Diffusion Language Model
- **Innovation**: Reformulates diffusion within causal attention. 100% token utilization, supports KV-caching, dynamic parallel decoding. **3× less training latency** than block diffusion. ARM-level data efficiency.

### Evo: Autoregressive-Diffusion Large Language Models with Evolving Balance
- **Innovation**: Balances AR and diffusion objectives during training.

### SDAR: Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation
- **Link**: https://aclanthology.org/2026.findings-acl.1110.pdf

### Diffusion in Diffusion: Reclaiming Global Coherence in Semi-Autoregressive Diffusion
- **Innovation**: "Draft-then-refine" framework. Gen PPL from 25.7 → 21.9 on OWT using 26% of baseline tuning budget.

---

## 16. LLM Reasoning & Metacognition

### "LLM Reasoning Is Latent, Not the Chain of Thought"
- **Authors**: Wenshuo Wang
- **Innovation**: Position paper arguing LLM reasoning = latent-state trajectory formation, not surface CoT. Recommends treating latent dynamics as default object of study.
- **Link**: https://arxiv.org/abs/2604.15726

### "LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling"
- **Innovation**: Metacognitive harness separating monitoring from reasoning. Pre-solve FOK + post-solve JOL signals → control interface. Improves Claude Sonnet-4.6 from **48.3 → 56.9 accuracy** across HLE, LiveCodeBench v6, R-Bench-V.
- **Link**: https://arxiv.org/abs/2605.14186

### "Causal Evidence that Language Models use Confidence to Drive Behavior"
- **Affiliation**: **Google DeepMind**
- **Innovation**: Four-phase paradigm showing LLMs apply implicit threshold to internal confidence for abstention. Verbal confidence independently predicts abstention across GPT-4o, Gemma 3, DeepSeek 671B, Qwen 80B. Activation steering confirms causal role.
- **Link**: https://arxiv.org/abs/2603.22161

### "X-RAY: Mapping LLM Reasoning Capability via Formalized and Calibrated Probes"
- **Innovation**: Formal reasoning analysis system. Models robust to constraint refinement but degrade under solution-space restructuring. Contamination-free framework.
- **Link**: https://arxiv.org/abs/2603.05290

---

## 17. Games & Multi-Agent Systems

### NitroGen (CVPR 2026 Honorable Mention)
- Vision-action foundation model for generalist gaming agents. 40K hours gameplay, 1,000+ games.

### CSRO (Google DeepMind)
- LLM-generated code policies for game-theoretic best responses.

### Sensi
- LLM game agent with 50–94× sample efficiency via curriculum learning.

### ProAct
- Lookahead reasoning for stochastic (2048) and deterministic (Sokoban) environments.

### OpenGame: Open Agentic Coding for Games
- **Link**: https://arxiv.org/abs/2604.18394

---

## 18. Benchmarks & Evaluation

### "JudgeBoard: Benchmarking and Enhancing Small Language Models for Reasoning Evaluation"
- **Venue**: AAAI 2026

### "CounterBench: Evaluating and Improving Counterfactual Reasoning in LLMs"
- **Venue**: AAAI 2026

### "Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow"
- **Innovation**: First systematic benchmark of 8 MDLMs (up to 100B) across 58 tasks. MDLMs still lag AR but show adaptive decoding. Proposes "generate-then-edit" paradigm.
- **Link**: https://arxiv.org/abs/2601.15593

---

## Key Themes & Trends

### 1. Diffusion Language Models Maturing
- ICML 2026 Outstanding Paper challenges arbitrary-order generation
- Scaling laws established for all diffusion families (masked, uniform, interpolating)
- CARD bridges AR training efficiency with diffusion inference parallelism
- Speed-quality Pareto frontier > raw PPL for practical comparison

### 2. RL + LLM Post-Training: Limits and Opportunities
- NeurIPS 2025 runner-up: RL doesn't expand reasoning beyond base model
- ICML 2026: JustGRPO for diffusion LLMs
- KDD 2026: GRPO > DPO for e-commerce recommendation
- Google DeepMind: Confidence-driven abstention via activation steering

### 3. Agent Systems: From Text to Code
- Code as execution interface (Code as Agent Harness)
- Safety via type-checking (LACUNA)
- Game agents via code generation (CSRO, Sensi)
- Metacognitive harnesses for test-time scaling

### 4. CTR/RecSys: Scaling Laws + Generative Paradigm
- Field-Aware Transformer: scaling laws for CTR (KDD 2026, deployed Taobao)
- OneMall: end-to-end generative rec (Kuaishou, 400M DAU)
- HyFormer: unified long-sequence + feature interaction
- DS-MLP: simple MLP matches complex architectures
- Semantic IDs: end-to-end generation replacing RQ

### 5. 4D Scene Understanding (CVPR 2026)
- D4RT: dynamic 4D reconstruction (Best Paper)
- WorldReel: 4D video generation
- Complet4R: geometric complete 4D reconstruction
- VerseCrafter: 4D geometric control for video world models

### 6. Safety & Alignment Under Scrutiny
- ICML 2026 Position Paper: alignment = censor's toolkit
- RLVR deception probes
- LLM memorization measurement
- Artificial Hivemind: model homogenization
- Incomplete safety learning (AAAI 2026)

---

*Generated by karpathy-wiki on 2026-07-10*
