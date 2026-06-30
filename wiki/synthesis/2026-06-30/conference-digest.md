---
title: "Conference Digest 2026-06-30"
type: synthesis
created: 2026-06-30
updated: 2026-06-30
sources: [arxiv-api-query]
tags: [conference-digest, ICML-2026, KDD-2026, ECCV-2026, NeurIPS-2025, recommendation, LLM, diffusion, agent, RL, benchmark]
---

# Conference Digest — June 2026

> Comprehensive survey of recent papers from top ML/AI venues: ICML 2026, KDD 2026, ECCV 2026, NeurIPS 2025, and arXiv preprints. Covers LLMs, recommendation systems, diffusion models, agents, RL, games, benchmarks, and CTR prediction.

---

## Table of Contents

1. [ICML 2026](#icml-2026)
2. [KDD 2026](#kdd-2026)
3. [ECCV 2026](#eccv-2026)
4. [NeurIPS 2025](#neurips-2025)
5. [Recommendation &amp; Advertising Systems](#recommendation--advertising-systems)
6. [LLMs, Agents &amp; Code](#llms-agents--code)
7. [Reinforcement Learning &amp; Games](#reinforcement-learning--games)
8. [Diffusion Models &amp; Generation](#diffusion-models--generation)
9. [Benchmarks &amp; Evaluation](#benchmarks--evaluation)
10. [Key Industry Papers](#key-industry-papers)

---

## ICML 2026

### 1. GoodDiffusion: Proactive Copyright Protection for Diffusion Bridge Models

| Field | Detail |
|-------|--------|
| **Title (EN)** | GoodDiffusion: Proactive Copyright Protection for Diffusion Bridge Models via Learnable Sample-specific Signatures |
| **Title (ZH)** | GoodDiffusion：通过可学习样本特定签名对扩散桥接模型进行主动版权保护 |
| **Authors** | Shixi Qin, Zhiyong Yang, Shilong Bao, Zitai Wang, Qianqian Xu, Qingming Huang |
| **Affiliation** | CAS, UCAS |
| **Venue** | ICML 2026 **Oral** |
| **Link** | https://arxiv.org/abs/2606.29759 |

**Innovation:** Proposes backdoor-inspired model-level use-time control that preserves high-quality generation for authorized queries but refuses unauthorized inputs. Introduces Learnable Signature Network (LSN) for sample-specific signatures, preventing surrogate recovery via gradient-based optimization.

### 2. Causal Perturbative Elicitation (CPE) for Latent Behaviors in LLMs

| Field | Detail |
|-------|--------|
| **Title (EN)** | Mechanistically Eliciting Latent Behaviors in Language Models |
| **Authors** | Andrew Mack, Nina Panickssery, Alexander Matt Turner |
| **Affiliation** | Independent |
| **Venue** | ICML 2026 |
| **Link** | https://arxiv.org/abs/2606.29604 |

**Innovation:** Unsupervised method (CPE) that discovers interpretable LoRAs eliciting latent model behaviors via tensor decomposition. Data-efficient — learns from single examples. Competitive with GRPO on Countdown (85% vs 87%). Can surface hidden failure modes like sandbagging and alignment-faking, restoring 85% of locked BigCodeBench performance.

### 3. Accelerating Q-learning through Efficient Value-Sharing

| Title (EN) | Accelerating Q-learning through Efficient Value-Sharing across Actions |
| Authors | Prabhat Nagarajan, Brett Daley, Martha White, Marlos C. Machado |
| **Venue** | ICML 2026 **Spotlight** |
| **Link** | https://arxiv.org/abs/2606.29806 |

**Innovation:** Introduces mean-expansion layer that shares values across actions within a state, reducing value overestimation. Improves aggregate performance across 57 Atari games while increasing action gaps.

### 4. Concept Removal Guidance for Safe Diffusion Sampling

| Title (EN) | Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling |
| Authors | Yoonseok Choi, Chaeyoung Oh, Hyunjun Choi, Seokin Seo, Kee-Eung Kim |
| **Venue** | ICML 2026 |
| **Link** | https://arxiv.org/abs/2606.29801 |

**Innovation:** Training-free method estimating unwanted-concept presence at each diffusion step. Adaptive calibration via closed-form constrained update reduces attack success rates while preserving benign fidelity.

### 5. Robust Strategic Classification under Decision-Dependent Cost

| Authors | Sura Alhanouti, Guzin Bayraksan, Parinaz Naghizadeh |
| **Venue** | ICML 2026 |
| **Link** | https://arxiv.org/abs/2606.30136 |

**Innovation:** Two-stage robust optimization with decision-dependent uncertainty sets for strategic classification where manipulation costs depend on past decisions.

### 6. SoftBinary Coding: New Neural Compression Paradigm

| Authors | Ezgi Ozyilkan, Sharang M. Sriramu, Elza Erkip, Aaron B. Wagner, Jona Ballé |
| **Venue** | ICML 2026 |
| **Link** | https://arxiv.org/abs/2606.29578 |

**Innovation:** End-to-end learnable stochastic binary latent space compression. Achieves state-of-the-art on vector quantization of i.i.d. sources, exceeding Trellis Coded Quantization.

### 7. Faults in Formal Benchmarking: Lean Theorem Proving

| Authors | Pawan Sasanka Ammanamanchi, Siddharth Bhat, Stella Biderman |
| **Venue** | ICML 2026 |
| **Link** | https://arxiv.org/abs/2606.29493 |

**Innovation:** Audits 5 Lean theorem-proving benchmarks, surfacing 4,833 findings including 398 mechanically certified issues (counterexamples, vacuous theorems, unsound axioms).

### 8. Robust Recovery for Non-Monotonic Link Functions (Single-Index Models)

| Authors | Santanu Das, Sagnik Chatterjee, Jatin Batra |
| **Venue** | ICML 2026 |
| **Link** | https://arxiv.org/abs/2605.29497 |

**Innovation:** First robust recovery algorithm for generic non-monotonic link functions (GeLU, Swish) under adversarial contamination. Proves constant-radius convex basin around ground truth with near-linear sample complexity.

### 9. SoftBinary Coding

| Title (EN) | SoftBinary Coding: A New Information-Theoretic Neural Compression Paradigm |
| Authors | Ezgi Ozyilkan, Sharang M. Sriramu, Elza Erkip, Aaron B. Wagner, Jona Ballé |
| **Venue** | ICML 2026 |
| **Link** | https://arxiv.org/abs/2606.29578 |

**Innovation:** End-to-end learned compression via stochastic binary latents with novel fast binary channel simulation that achieves rate-optimality. Exceeds Trellis Coded Quantization.

### 10. Hessian Eigenvector Dynamics

| Title (EN) | Characterizing Optimizer-Dependent Training Dynamics Through Hessian Eigenvector Displacement and Localization |
| Authors | Marcelina Marjankowska, Valerio Modugno, Paolo Barucca |
| **Venue** | ICML 2026 Workshop (HiLD) |
| **Link** | https://arxiv.org/abs/2606.30226 |

**Innovation:** Reveals SGD stabilizes curvature directions while Adam reorganizes eigenvectors throughout training. Adam causes localization where few parameters dominate leading curvature.

---

## KDD 2026

### 11. Benchmarking on Tasks That Matter: Dataset Selection

| Title (EN) | Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings |
| Authors | Rostislav Gusev, Alexey Zaytsev |
| **Venue** | KDD 2026 |
| **Link** | https://arxiv.org/abs/2606.27997 |

**Innovation:** Framework for selecting small representative dataset subsets while preserving global model rankings. On TSC, achieves Spearman correlation 0.95 with full benchmark using only 5 datasets.

### 12. Generative Pretrained Controllers (GPC) for Motor Control

| Title (EN) | GPC: Large-Scale Generative Pretraining for Transferable Motor Control |
| Authors | Yi Shi, Yifeng Jiang, Chen Tessler, Xue Bin Peng |
| **Venue** | SIGGRAPH 2026 |
| **Link** | https://arxiv.org/abs/2606.29148 |

**Innovation:** Uses tokenization + next-token prediction (GPT-style) to create general-purpose generative controllers for physics-based character animation. RL jointly optimizes motion vocabulary via Finite Scalar Quantization. 99.98% success in reproducing motion corpus.

---

## ECCV 2026

### 13. VisReflect: Latent Visual Reflection for Fine-Grained Perception

| Title (EN) | VisReflect: Latent Visual Reflection for Fine-Grained Perception in Long Visual Context |
| Authors | Xiaoqian Shen, Mohamed Elhoseiny |
| **Venue** | ECCV 2026 |
| **Link** | https://arxiv.org/abs/2606.30288 |

**Innovation:** Generates continuous visual reflection in latent space to selectively emphasize salient regions without decoding to discrete tokens. 4.1% gain on image benchmarks, 1.8% on video, 44% inference time reduction vs zooming methods.

### 14. ViDiHand: Video Diffusion for Hand Motion Reconstruction

| Title (EN) | The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction |
| Authors | Yuxi Wang, Chengkai Jin, Yufei Liu, Wenqi Ouyang, Tianyi Wei, Zhiwei Zeng, Siyuan Huang, Zhiqi Shen, Xingang Pan |
| **Venue** | ECCV 2026 |
| **Link** | https://arxiv.org/abs/2606.30308 |

**Innovation:** Leverages pretrained video diffusion model features for 4D two-hand pose reconstruction from egocentric video. No detector, no infiller, no test-time optimization. Outperforms prior methods on ARCTIC, HOT3D, HOI4D.

### 15. IR-Guided Diffusion for One-and-Only Alignment

| Title (EN) | Intermediate Text Representation Guided Text-to-Image Generation for Enhancing One-and-Only Alignment |
| Authors | Soyoun Won, Aryan Yazdan Parast, Basim Azam, Jean Honorio, Naveed Akhtar |
| **Venue** | ECCV 2026 |
| **Link** | https://arxiv.org/abs/2606.30262 |

**Innovation:** Injects intermediate hidden states of text encoder into conditioning signal during early denoising steps. Up to 19.1 percentage-point improvement in VQAScore on OAO objects (celestial bodies, landmarks, artworks).

### 16. Shell-LCC for Text-to-Video Generation

| Title (EN) | Your Data Manifold is Secretly a Reward Model: Shell-LCC for Text-to-Video Generation |
| Authors | Shihao Zhang, Yuguang Yan, Junzhe Zhang, Wei Zhao, Bohan Wang, Hanwang Zhang |
| **Venue** | ECCV 2026 |
| **Link** | https://arxiv.org/abs/2606.30248 |

**Innovation:** Models manifold structure of SFT data via Shell Local Coordinate Coding for dense, differentiable, nearly cost-free reward signals. Improves realism, enhances high-frequency details, reduces motion blur.

### 17. Nemotron-Labs-Diffusion-Image (NVIDIA)

| Title (EN) | Nemotron-Labs-Diffusion-Image: Advancing Masked Discrete Diffusion for High-Resolution Image Synthesis |
| Authors | Shufan Li, Greg Heinrich, Hanrong Ye, Yonggan Fu, Aditya Grover, Jan Kautz, Pavlo Molchanov |
| **Affiliation** | NVIDIA |
| **Venue** | arXiv / NVIDIA Labs |
| **Link** | https://arxiv.org/abs/2606.29814 |

**Innovation:** SOTA masked discrete diffusion model with token-editing mechanism for self-correction and Grouped Cross-Entropy (GCE) for large-vocabulary training. Achieves GenEval 0.90, DPG 86.9, HPSv3 10.76.

### 18. HomeDiffusion: Zero-Shot Object Customization

| Authors | Guoqiu Li, Jin Song, Yiyun Fei |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29828 |

**Innovation:** Multi-viewpoint image-based object customization in indoor scenes using diffusion models with cross-attention for detail preservation.

---

## Recommendation & Advertising Systems

### 19. POEM: Partial-Order Enhanced Real-Time Sequential Modeling (Kuaishou)

| Title (EN) | POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation |
| Authors | Linxiao Che, Yijia Sun, Siyuan Lou, Shanshan Huang, Qiang Luo, Ruiming Tang, Han Li, Kun Gai |
| **Affiliation** | Kuaishou |
| **Venue** | arXiv / Industry |
| **Link** | https://arxiv.org/abs/2606.29946 |

**Innovation:** Builds dynamic partial-order sequences from real-time multi-task ranking scores (predicted CTR, watch duration) for fine-grained interest modeling. Deployed on Kuaishou online traffic: +0.249% watch time on KS Single Page, +0.213% on KS Lite.

**Key Results:**
- Partial-order construction enriches vanilla chronological sequences
- Multi-objective score fusion into quintuple representation
- Graph-mined hard negatives with margin-based pairwise loss
- **Online gains:** 0.249% watch time lift (KS Single Page)

### 20. CMSL: Constructive Multi-Sequence Learning (Meta)

| Title (EN) | CMSL: Constructive Multi-Sequence Learning for Recommendation Systems |
| Authors | Zikun Cui, Renzhi Wu, Junjie Yang, Li Sheng, Jijie Wei, Linfeng Liu, Tai Guo, Tao Jia, Xiaodong Wang, Hong Li, Li Yu, Sri Reddy, Hong Yan |
| **Affiliation** | Meta |
| **Venue** | arXiv / Industry |
| **Link** | https://arxiv.org/abs/2606.28533 |

**Innovation:** Paradigm shift from single-sequence ingestion to multi-sequence "context engineering." Disentangles user history into thematic strands via learnable Sequence Construction Module + linear attention. Deployed across ranking, retrieval, and four major surfaces at Meta.

### 21. AgentX: Agent-Driven Self-Iteration of Industrial Recommender Systems (Kuaishou)

| Title (EN) | AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems |
| Authors | 50+ authors from Kuaishou (Changxin Lao, Kun Gai, Ruiming Tang et al.) |
| **Affiliation** | Kuaishou |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.26859 |

**Innovation:** Production multi-agent system autonomously generates, implements, evaluates, and learns from recommendation experiments. Four-stage closed loop: Brainstorm Agent → Developing Agent → Evaluation Agent → Harness Evolution (SGPO). Self-improving without human engineers.

### 22. Recommendation as Generation (RaG) — Kuaishou

| Title (EN) | Recommendation as Generation: Unifying Personalized Video Generation and Recommendation at Industrial Scale |
| Authors | Yanhua Cheng, Bo Wang, Haotian Zhang, Xinyuan Gao, Zhihui Yin, Ben Xue, Kun Gai et al. |
| **Affiliation** | Kuaishou |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.25496 |

**Innovation:** Generates personalized videos on-demand from inferred user interest via shared Semantic IDs (SIDs). Video Generation Agents (VGAs) with hierarchical planning. Deployed on 400M+ DAU platform. **Online A/B: 1.87% ad revenue improvement** over strong GRM baseline.

### 23. Diagnosing Retrieval Bottlenecks in LLM Cold-Start Recommendation

| Authors | Zhe Dong, Fang Qin, Manish Shah, Yicheng Wang |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29947 |

**Innovation:** Five-domain benchmark separating reranking from retrieval coverage. Standard retrievers place gold item in 200-item pool only 4.6-22.9% of the time. Proposes LHF hybrid fusion layer recovering 17-61% oracle coverage on content-rich domains.

### 24. Monosemanticity in Recommender Systems

| Authors | Yagel Alfasi, Eden Rzezak, Eadan Schechter |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29341 |

**Innovation:** Applies Matryoshka Sparse Autoencoders to collaborative filtering embeddings. Discovers hierarchical interpretable structure. Demonstrates gender-associated latent neuron intervention on Amazon Fashion dataset.

### 25. A Rank-One Popularity Component in Dot-Product Recommender Scores

| Authors | Yang Cheng |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.21275 |

**Innovation:** Proves population-optimal score decomposes into PMI + item-marginal term log p(i). Separating log p(i) reduces popularity-aligned score energy by 98.6%. Shows representation anisotropy is decoder-level, not Transformer-specific.

### 26. Monosemanticity in Recommender Systems

| Authors | Yagel Alfasi, Eden Rzezak, Eadan Schechter |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29341 |

### 27. Fairness Attacks on Recommender Systems

| Authors | Yanan Wang, Yong Ge |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29064 |

**Innovation:** Structure-aware RL-based fairness attack using graph encoder + RNN. Jointly learns item selection and gender selection policies to exacerbate unfairness across 4 recommendation models.

### 28. Scoring Is Not Enough: Utility-fairness Trade-offs for Ranking

| Authors | Shubham Singh, Ian A. Kash, Mesrob I. Ohannessian |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.26369 |

**Innovation:** Shows scoring is suboptimal for utility-fairness trade-offs via counter-examples. Semi-greedy post-processing achieves near-ideal trade-offs.

---

## LLMs, Agents & Code

### 29. Does Verbose Chain-of-Thought Really Help?

| Title (EN) | Does Verbose Chain-of-Thought Really Help? In-Distribution Evidence that Content, Not Length, Matters |
| Authors | Wenlong Wang, Fergal Reid |
| **Venue** | ICML 2026 Workshop |
| **Link** | https://arxiv.org/abs/2606.30128 |

**Innovation:** Across 25 models, extra tokens leave accuracy unchanged. Verbose traces improve accuracy 1-4 points but only due to reasoning/validation content, not verbosity. Length-matched non-reasoning filler recovers none of the gain.

### 30. SEVA: Self-Evolving Verification Agent

| Title (EN) | SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution |
| Authors | Aojie Yuan, Yi Nian, Haiyue Zhang, Zijian Su, Yue Zhao |
| **Venue** | ICML 2026 Workshop |
| **Link** | https://arxiv.org/abs/2606.29713 |

**Innovation:** Structured verification agent with evidence alignments, step-by-step reasoning, calibrated confidence, and 6-category error diagnosis. Process reward decomposes verification into 5 components. SEVA-3B matches GPT-4o-mini (69.0 vs 69.8 F1) with richer auditable output.

### 31. TACO: Tool-Augmented Credit Optimization

| Title (EN) | TACO: Tool-Augmented Credit Optimization for Agentic Tool Use |
| Authors | Mingkuan Feng, Jinyang Wu, Hao Gu, Fangrui Lv, Ruihan Jin, Chuyuan Zhang, Zhengqi Wen, Jianhua Tao |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30251 |

**Innovation:** GRPO variant for code-tool agents with Differential Answer-Probe Reward (DAPR) — self-supervised, judge-free tool-contribution advantage. Probe tokens measure tool impact on correctness. Outcome-Gated Advantage Routing (OGAR) suppresses wasted tool calls.

### 32. ManimAgent: Self-Evolving Multimodal Agents

| Authors | Wenjia Jiang, Zongyuan Cai, Yuanhang Shao, Chenru Wang, Boyan Han, Zhixue Song, Keyu Chen, Shengwei An, Xu Yang, Zhou Yang |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30296 |

**Innovation:** Dual-channel Episodic Memory Bank (M+ positive, M- negative) carrying reflection experience across code-generation tasks. Blind human Pass@1 rises as memory grows without weight updates.

### 33. MCP Server Architecture Patterns

| Title (EN) | MCP Server Architecture Patterns for LLM-Integrated Applications |
| Authors | Carson Rodrigues, Oysturn Vas |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30317 |

**Innovation:** Catalogues 5 MCP server patterns (Resource Gateway, Tool Orchestrator, Stateful Session Server, Proxy Aggregator, Domain-Specific Adapter). Tool-selection accuracy drops below 90% between 10-15 tools for Claude Haiku, 20-30 for Sonnet 4.

### 34. Clarus: Coordinating Autonomous Research Agents

| Authors | Zihan Guo, Zeyi Chen, Zhiyu Chen, Zicai Cui, Shuai Shao, Bo Huang, Zhi Han, Yuanyi Song, Yuan Yuan, Weinan Zhang et al. |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30246 |

**Innovation:** Collaboration infrastructure for web-scale scientific collaboration with project-agent-resource object model. Four-layer architecture: Research Application, Digital Collaboration, Physical Substrate, Physical World.

### 35. DuoMem: On-Device Memory Agents

| Authors | Peyman Hosseini, Ondrej Bohdal, Ahmed Alajrami, Andrea Maracani, Ignacio Castro, Matthew Purver, Mete Ozay, Savas Ozkan, Taha Ceritli |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29961 |

**Innovation:** Dual-space distillation (context-space + parameter-space). Boosts 4B model from 4.3% to 77.9% on ALFWorld (teacher 72B: 87.1%). 3x faster than teacher, fewer than 10M trainable parameters.

### 36. SWE-Together: Interactive Coding Agent Evaluation

| Authors | Yifan Wu, Zhuokai Zhao, Songlin Li, Ho Hin Lee, Jiacheng Zhu, Shirley Wu, Tianhe Yu, Serena Li, Lizhu Zhang, Xiangjun Fan, Shengzhi Li |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29957 |

**Innovation:** Multi-turn benchmark from 11,260 real user-agent coding sessions. 109 repository-level tasks with reactive LLM-based user simulator. Measures both correctness and corrective feedback turns.

### 37. SpreadsheetBench 2

| Authors | Jian Zhu, Yuzheng Zhang, Zeyao Ma, Bohan Zhang, Armin Schoepf, Daniel Woloch, Peter Yiliu Wang, Guangyu Robert Yang et al. |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29955 |

**Innovation:** Workflow-level benchmark for spreadsheet agents. 321 tasks, 11.8 worksheets avg, 593.5 cell modifications per instance. Best model (frontier LLM) achieves 34.89% accuracy. Debugging accuracy as low as 12%.

---

## Reinforcement Learning & Games

### 38. Dual-Flow RL with State-Aware Exploration

| Title (EN) | Dual-Flow Reinforcement Learning with State-Aware Exploration |
| Authors | Qijun Li, Zheng Fu, Qi Song, Yifei He, Weitao Zhou, Kun Jiang, Diange Yang |
| **Venue** | arXiv (submitted to IEEE) |
| **Link** | https://arxiv.org/abs/2606.29820 |

**Innovation:** Unified actor-critic with conditional flow matching for multimodal return and policy distributions. Entropy-Covariance Exploration Regulator (ECER) for state-aware exploration. SOTA on DeepMind Control Suite and Humanoid-Bench.

### 39. Hierarchical RL in StarCraft Micromanagement

| Title (EN) | Hierarchical Reinforcement Learning in StarCraft Micromanagement with Influence Maps and Cluster-based Scripts |
| Authors | Chunhui Bai, Changhe Li, Dequan Li, Xinye Cai, Shengxiang Yang |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30092 |

**Innovation:** HRL-IM/CBS with influence map hashing for spatial control encoding and cluster-based scripts for dynamic local coordination. Hierarchical multi-Q-table architecture. Competitive with deep RL baselines with superior sample efficiency and interpretability.

### 40. ACPO: Agent-Chained Policy Optimization

| Title (EN) | ACPO: Agent-Chained Policy Optimization for Multi-Agent Reinforcement Learning |
| Authors | Daiki E. Matsunaga, Junho Na, Tri Wahyu Guntara, Scott Sanner, Pascal Poupart, Jongmin Lee, Kee-Eung Kim |
| **Venue** | RLC 2026 |
| **Link** | https://arxiv.org/abs/2606.30072 |

**Innovation:** Proves joint policy gradient admits exact decentralized decomposition. Actors trained independently, updates together form single joint gradient step. Outperforms strong baselines on Multi-Robot Warehouse, SMACv2, MA-MuJoCo; gap widens with more agents.

### 41. DreamForge-World: Real-Time Controllable World Model

| Title (EN) | DreamForge-World 0.1 Preview: A Low-Compute Real-Time Controllable World Model |
| Authors | Daniyel Ayupov, Artur Markov-Tsoy |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30292 |

**Innovation:** Real-time interactive world simulation at 14-15 FPS on single RTX 4090. Supports keyboard/mouse control, multimodal initialization, mid-stream reprompting, minute-scale interactive rollouts at 480p.

### 42. Chronos: Non-Markovian Robot Manipulation

| Title (EN) | Chronos: A Physics-Informed Full-History Framework for Non-Markovian Long-Horizon Manipulation |
| Authors | Yulin Zhou, Yimeng Wang, Nengyu Wang, Shaojia Xing, Shiyun Tu, Xiang Li, Jingkai Zhang, Ningbo Jiang, Yuankai Lin, Hua Yang, Xiangrui Zeng, Zhouping Yin |
| **Venue** | arXiv (submitted to IEEE TRO) |
| **Link** | https://arxiv.org/abs/2606.30318 |

**Innovation:** Elevates observation history to latent state of policy dynamics. Selective state space model + Schrodinger-inspired bridge for acceleration fields. On RMBench: 73.6% success vs pi0.5 11.2% (6.6x improvement) with 10x fewer parameters. Real-world: 78% vs pi0.5 7%.

---

## Diffusion Models & Generation

### 43. Multi-View Aggregated Score Distillation (MV-SDI)

| Title (EN) | Variance Reduction on the Camera Axis: Multi-View Score Distillation for 3D |
| Authors | Marian Lupascu, Mihai Sorin Stupariu, Ionut Mironica |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29964 |

**Innovation:** Aggregates gradients from K views per step via gradient accumulation with frozen 2D prior. Antithetic antipodal pairs for angular coverage. At fixed 10K UNet budget, K=2 raises CLIP R-Precision from 74.8% to 83.8%.

---

## Benchmarks & Evaluation

### 44. EvalSafetyGap: LLM Evaluation-Safety Framework

| Authors | Bugra Alperen Uluiirmak, Rifat Kurban |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30219 |

**Innovation:** Comprehensive survey spanning 8 evidence streams (2018-2026). EvalSafetyGap hypothesis: comparing evaluation-side and alignment-side proxy failures under optimization pressure. Ten-model audit reveals association between capability and adversarial robustness is statistically indeterminate (r=+0.232, p=0.520).

### 45. CORTEX: Cross-Domain Corpus Organization

| Authors | Chengtao Gan, Xiaoke Guo, Yushan Zhu, Zhaoyan Gong, Zhiqiang Liu, Songze Li, Huajun Chen, Wen Zhang |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30175 |

**Innovation:** First framework elevating web-scale corpus construction from flat filtering to structured knowledge organization via Ontological Corpus Graph (OCG). Releases 24.14B-token refined corpus and CortexBench.

### 46. TIGRAG: Token-Induced GraphRAG

| Authors | Gianluca Bonifazi, Christopher Buratti, Michele Marchetti, Federica Parlapiano, Giulia Quaglieri, Davide Traini, Domenico Ursino, Luca Virgili |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.30093 |

**Innovation:** Efficient graph-augmented RAG based on token co-occurrence KG. Sliding-window co-occurrence statistics for scalable graph construction. Outperforms dense retrieval and graph-based RAG methods on multi-hop QA while reducing indexing time and inference latency.

### 47. SABER-Math: Automated Benchmark for Math IR

| Authors | Nikolay Georgiev, Maria Drencheva, Kseniia Ibragimova, Ivo Petrov, Dimitar I. Dimitrov, Martin Vechev |
| **Venue** | ICML 2026 Workshop |
| **Link** | https://arxiv.org/abs/2606.29894 |

**Innovation:** First fully automated benchmark for evaluating mathematical IR without expert annotation. 283K problems. Finds MTEB does not predict math retrieval performance.

### 48. Rigel: Self-Distilled Captioning Evaluation

| Authors | Shuitsu Koyama, Kazuki Matsuda, Yuiga Wada, Shinnosuke Hirano, Daichi Yashima, Komei Sugiura |
| **Venue** | arXiv |
| **Link** | https://arxiv.org/abs/2606.29997 |

**Innovation:** Self-distilled score adaptation using evaluation-specific scoring head distilled from frozen LLM. Vid-Lepus dataset: 3,338 video clips, 33,380 reference captions. Over 10-point improvements on ActivityNet-Fact.

---

## Key Industry Papers (by Company)

### Kuaishou
- **POEM** — Partial-order sequential modeling. Online: +0.249% watch time. [[19]](#19-poem-partial-order-enhanced-real-time-sequential-modeling-kuaishou)
- **AgentX** — Multi-agent self-iterating recommendation. [[21]](#21-agentx-agent-driven-self-iteration-of-industrial-recommender-systems-kuaishou)
- **RaG** — Recommendation-as-Generation. 1.87% ad revenue lift on 400M+ DAU platform. [[22]](#22-recommendation-as-generation-rag--kuaishou)

### Meta
- **CMSL** — Constructive Multi-Sequence Learning deployed across 4 surfaces. [[20]](#20-cmsl-constructive-multi-sequence-learning-meta)

### NVIDIA
- **Nemotron-Labs-Diffusion-Image** — SOTA masked discrete diffusion. GenEval 0.90. [[17]](#17-nemotron-labs-diffusion-image-nvidia)

### Anthropic / Community
- **MCP Architecture Patterns** — 5 patterns, 4 anti-patterns for LLM tool integration. [[33]](#33-mcp-server-architecture-patterns)

---

## Cross-cutting Themes

| Theme | Key Papers |
|-------|-----------|
| **LLMs for Recommendation** | POEM, CMSL, AgentX, RaG, LLM Cold-Start Diagnosis |
| **Multi-Agent Systems** | AgentX, ACPO, Clarus, ManimAgent |
| **Diffusion Models** | GoodDiffusion, CRG, Nemotron, ViDiHand, MV-SDI |
| **RL + Flow Matching** | Dual-Flow RL, Chronos |
| **Evaluation & Benchmarks** | EvalSafetyGap, SpreadsheetBench 2, SWE-Together, SABER-Math |
| **AI Safety & Alignment** | CPE (latent behaviors), EvalSafetyGap, GoodDiffusion |
| **Frontier Theory** | SoftBinary Coding, Single-Index Model Robust Recovery, Hessian Dynamics |
