---
title: "Conference Digest: 2025-2026 Top ML/AI Venues (2026-08-17)"
type: synthesis
created: 2026-08-17
updated: 2026-08-17
sources: []
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, CVPR2026, KDD2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, benchmarks, code-execution, sequential-modeling, daily-digest]
---

# Conference Digest: 2025-2026 Top ML/AI Venues

> Compiled 2026-08-17. Covers ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025. Focus: LLM training, RL, agent systems, generative models, recommendation, advertising/CTR, code execution, sequential modeling, benchmarks. Key papers from Google DeepMind, OpenAI, Meta, Microsoft, ByteDance, Alibaba, Tencent, Kuaishou, Netflix, NVIDIA, Anthropic, Apple, Amazon.
>
> Cross-reference: [[synthesis/2026-08-16/conference-digest|08-16 conference-digest]] (previous day, 727 lines), [[synthesis/2026-08-17/arxiv-paper-check|08-17 arxiv-paper-check]], [[synthesis/2026-08-16/arxiv-ai-search|08-16 arxiv-ai-search]], [[synthesis/2026-08-16/tech-report-digest|08-16 tech-report-digest]]

---

## 1. ICML 2026 (Seoul, July 6–11, 2026)

**Scale**: 23,918 submissions → 6,352 accepted (26.6%) | 536 Spotlight (2.2%) | 168 Oral (0.7%) | 44 workshops

### 1.1 Outstanding Papers

#### The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (《灵活性的陷阱：重新审视扩散语言模型任意顺序生成的价值》)
- **Authors**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation**: Tsinghua University (Gao Huang / LeapLab)
- **Venue**: ICML 2026 Outstanding Paper
- **arXiv**: [code: github.com/LeapLabTHU/JustGRPO](https://github.com/LeapLabTHU/JustGRPO)
- **Abstract**: Diffusion LLMs (dLLMs) enable arbitrary-order token generation, but this paper shows it's actually a trap — dLLMs exploit flexibility to bypass high-uncertainty "forking" tokens crucial for reasoning, collapsing solution diversity. On math/coding tasks, fixed left-to-right RL rollout (**JustGRPO**) outperforms arbitrary-order approaches while preserving parallel inference decoding.
- **Key Innovation**: Counter-intuitive finding that order flexibility hurts reasoning; JustGRPO recipe for dLLM post-training.
- **Results**: GSM8K 89.1% accuracy.
- **Comparison**: Beats complex arbitrary-order dLLM-RL methods with simpler fixed-order approach.

#### High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions (《扩散模型与对数凹分布的高精度采样》)
- **Authors**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation**: MIT / Yale
- **Venue**: ICML 2026 Outstanding Paper
- **Abstract**: Achieves δ-error sampling in polylog(1/δ) steps using Õ(δ)-accurate score estimates — **exponential improvement** over all prior diffusion sampling results. First polylog(1/δ) gradient-only sampler for general log-concave distributions.
- **Key Innovation**: FORS (First-Order Rejection Sampling) — polynomial to polylogarithmic complexity drop.
- **Comparison**: Exponential improvement over discretization-based samplers requiring poly(1/ε) steps.

### 1.2 Outstanding Position Paper

#### Position: The Alignment Community is Unintentionally Building a Censor's Toolkit (《立场：对齐社区正在无意中构建审查工具包》)
- **Authors**: Sarah Ball, Phil Hackemann
- **Venue**: ICML 2026 Outstanding Position Paper
- **Abstract**: Alignment methods designed to prevent AI harm are dual-use technologies that can be repurposed for censorship. Calls for urgent community discussion on misuse potential.

### 1.3 Outstanding Paper Honorable Mentions

| Paper | Key Contribution |
|-------|-----------------|
| **The Obfuscation Atlas** (Taufeeque et al.) | Maps where honesty emerges in RLVR with deception probes — studies whether training against deception detectors produces honesty or better evasion |
| **Motion Attribution for Video Generation** (Wu et al.) | Gradient-based data attribution framework for video generation; 74.1% human preference win rate with curated training data. First motion-attribution (not appearance) framework |
| **How Much Can Language Models Memorize?** (Morris et al.) | Sharper reasoning about what LLMs memorize vs generalize; ~3.6 bits per parameter of distributional information |
| **A Random Matrix Perspective on Consistency of Diffusion Models** (Wang et al.) | Explains why separately-trained diffusion models produce near-identical outputs from same seed |
| **To Grok Grokking** (Xu et al.) | First rigorous bounds on grokking time in ridge regression — cleanest toy model for delayed generalization |

### 1.4 Test of Time Award

#### Asynchronous Methods for Deep Reinforcement Learning (《深度强化学习的异步方法》)
- **Authors**: Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Affiliation**: DeepMind
- **Cited for**: "major contributing factor to the success of RL in LLM post-training" — direct line from A3C (2016) to modern RLHF/GRPO

### 1.5 Key ICML 2026 Themes

- **Diffusion models as first-class**: Both Outstanding Papers are diffusion research; clean sweep signals community sees diffusion as first-class direction beyond autoregressive LLMs
- **Agentic AI explosion**: "agentic AI" appeared in 60+ workshop submissions
- **RL post-training**: Active research on RLVR, GRPO vs PPO, reward hacking
- **Alignment as dual-use**: Position Paper award highlights safety/censorship tension

---

## 2. ICLR 2026 (Rio de Janeiro, April 23–27, 2026)

### 2.1 Outstanding Papers

#### Transformers are Inherently Succinct (《Transformer 天生简洁》)
- **Authors**: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation**: ETH Zurich
- **Venue**: ICLR 2026 Outstanding Paper
- **Abstract**: Proves transformers are inherently succinct — computational complexity results showing transformers capture exactly the succinctly-describable languages. Has deep implications for understanding transformer expressivity and limits.

#### LLMs Get Lost In Multi-Turn Conversation (《LLM 在多轮对话中迷失》)
- **Authors**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Affiliation**: Microsoft Research
- **Venue**: ICLR 2026 Outstanding Paper
- **Abstract**: Average 39% performance drop in multi-turn settings across frontier models. Demonstrates critical failure mode where models lose context and accuracy as conversations extend.

### 2.2 Honorable Mention

#### The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm (《极坐标表达式：最优矩阵符号方法及其在 Muon 算法中的应用》)
- **Authors**: Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **Abstract**: Optimal matrix sign computation methods; directly impacts the Muon optimizer used in LLM training.

### 2.3 Test of Time Awards (ICLR 2016)

- **Generative Adversarial Networks** (Goodfellow et al.) — GANs
- **U-Net: Convolutional Networks for Biomedical Image Segmentation** (Ronneberger et al.)

### 2.4 Key ICLR 2026 Themes

- **Transformer theory**: Expressivity bounds, architectural understanding
- **Multi-turn reliability**: Critical gap between single-turn and multi-turn performance
- **Muon optimization**: Mathematical foundations for next-gen optimizers

---

## 3. NeurIPS 2025 (San Diego / Mexico City, Dec 2025)

### 3.1 Best Papers (4 winners + 3 runners-up)

#### Artificial Hivemind: The Open-Ended Homogeneity of Language Models (《人工蜂巢思维：语言模型的开放式同质化》)
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: AI2 / University of Washington
- **Venue**: NeurIPS 2025 Best Paper (D&B Track)
- **Abstract**: Introduces Infinity-Chat (26K queries, 31K+ annotations) revealing pronounced "Artificial Hivemind" — intra-model repetition + inter-model homogeneity. RLHF reduces diversity of human thought in AI outputs. Current reward models poorly calibrated to diverse human preferences (pluralism).
- **Key Finding**: Distinct models (DeepSeek, GPT-4) act as near-identical clones on open-ended tasks.

#### Gated Attention for Large Language Models (《面向大语言模型的门控注意力》)
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: Alibaba (Qwen Team)
- **Venue**: NeurIPS 2025 Best Paper
- **Abstract**: Simple sigmoid gate after SDPA consistently improves performance across 30 variants of 15B MoE and 1.7B dense models on 3.5T tokens. Eliminates attention-sink phenomenon, stabilizes training, enables larger learning rates. "Easily implemented, likely to become new standard."
- **Key Innovation**: G1 position (SDPA output) with query-conditioned sparsity beats value-pathway gating.
- **Results**: Consistent perplexity improvement; loss spike elimination.

#### 1000 Layer Networks for Self-Supervised RL (《1000 层网络的自监督强化学习》)
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Affiliation**: Carnegie Mellon / various
- **Venue**: NeurIPS 2025 Best Paper
- **Abstract**: Scales RL policies to 1024 layers using self-supervised contrastive learning. 2×–50× performance increase on locomotion/manipulation. Challenges dogma that RL doesn't benefit from depth.
- **Key Innovation**: Self-supervised (not reward-based) training enables depth scaling in RL.

#### Why Diffusion Models Don't Memorize (《为什么扩散模型不会记忆》)
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard
- **Affiliation**: ENS Paris / various
- **Venue**: NeurIPS 2025 Best Paper
- **Abstract**: Identifies two timescales: τ_gen (generation quality) and τ_mem (memorization). τ_mem grows linearly with dataset size n while τ_gen is constant — creates widening generalization window. Explains why diffusion models generalize despite memorization capacity.

### 3.2 Runners-up

| Paper | Key Finding |
|-------|------------|
| **Does RL Really Incentivize Reasoning Beyond Base Model?** | RLVR improves answer-finding efficiency but doesn't teach new reasoning patterns; base models outperform RL-trained when many samples allowed. Only distillation introduces truly new reasoning behaviors |
| **Optimal Mistake Bounds for Transductive Online Learning** | Resolves 30-year-old problem: transductive mistake bound is Θ(√d), quadratic gap over standard online learning |
| **Superposition Yields Robust Neural Scaling** | Neural scaling laws arise from representation superposition; open-source LLMs operate in strong superposition regime, loss scales inversely with model dimension |

### 3.3 Test of Time Award

**Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks** (Ren, He, Girshick, Sun) — 56,000+ citations, backbone of modern computer vision.

---

## 4. AAAI 2026 (Singapore, January 20–27, 2026)

**Scale**: 23,680 submissions → 4,167 accepted (17.6%, lowest in 3 years)

### 4.1 Outstanding Papers (5 Main + 2 AISI)

| Paper | Affiliation | Key Innovation |
|-------|------------|---------------|
| **LLM2CLIP** (Huang et al.) | Microsoft | Powerful language model unlocks richer visual cross-modality representation |
| **ReconVLA** (Song et al.) | Zhejiang / various | Reconstructive Vision-Language-Action model as effective robot perceiver |
| **CADYT** (Tagliapietra et al.) | Various | Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis |
| **Model Change for Description Logic Concepts** (Ozaki, Ribeiro) | - | Model change for description logic concepts |
| **High-pass Matters** (Li et al.) | Cambridge / various | Theoretical insights and sheaflet-based design for hypergraph neural networks |

**AISI Track**: PlantTraitNet (citizen science plant traits), Generalizable Slum Detection (satellite imagery with MoE)

### 4.2 Big Tech Research Signals

- **Amazon** (5 papers): Cost-aware reasoning, causal discovery
- **Microsoft** (3 papers): Multi-agent systems, structured inference (SemanticVLA +1.1%)
- **IBM**: Test-time molecular optimization
- **Huawei**: Semantic alignment for robotics

---

## 5. CVPR 2026 (Denver, June 3–7, 2026)

**Scale**: 16,092 submissions → 4,089 accepted (25.4%) | 100+ exhibitors | 74 award candidates

### 5.1 Best Paper

#### Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (《高效地逐个 D4RT 重建动态场景》)
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi Sajjadi
- **Affiliation**: **Google DeepMind** + UCL + Oxford
- **Abstract**: Unified transformer-based framework for dynamic 4D scene reconstruction. Single model estimates depth, spatio-temporal correspondence, and camera parameters. Lightweight, scalable, SOTA on all 4D reconstruction benchmarks. Handles moving objects without special-case treatment (unlike VGGT).
- **Key Innovation**: Single query interface — pixel + timestamps + camera → 3D position. Replaces entire pipeline of specialized models.
- **Why Important**: Foundational for autonomous driving, robotics, VR/AR.

### 5.2 Best Student Paper

#### Native and Compact Structured Latents for 3D Generation (《面向 3D 生成的原生紧凑结构化潜变量》)
- **Authors**: Jianfeng Xiang et al.
- **Affiliation**: **Tsinghua** + **Microsoft Research** + USTC + Microsoft AI
- **Abstract**: TRELLIS.2 — successor to Microsoft's open-source 3D generation model. O-Voxel representation handles arbitrary topology, encodes full PBR materials. Outputs game-ready assets directly.
- **Key Innovation**: Open/non-watertight surfaces as easily as closed meshes; integrated PBR material output.

### 5.3 Best Paper Honorable Mentions

| Paper | Affiliation | Key Innovation |
|-------|------------|---------------|
| **SAM 3D** | **Meta FAIR** (Dollár, Gkioxari, Feiszli, Malik) | Extends Segment Anything from 2D segmentation to full 3D object generation from single images |
| **NitroGen** | **NVIDIA** + Stanford + Caltech + Chicago + UT Austin | Open foundation model for generalist gaming agents; trained on 40K hours of gameplay across 1,000+ games |
| **ChordEdit** | Various | One-step low-energy transport for fast image editing |

### 5.4 CVPR 2026 Thematic Trends

- **Multimodal AI**: 4.9% → 10.6% of highlighted papers (largest single-category swing)
- **3D/4D reconstruction**: Dominant theme, multiple oral presentations
- **Embodied AI**: From lab to commercial deployment (Tesla, Waymo, NVIDIA exhibitors)
- **Vision-language models**: Grounding visual understanding in language and action

---

## 6. KDD 2026 (Jeju, August 9–13, 2026)

### 6.1 Awards

- **Test of Time**: XGBoost (Chen & Guestrin, KDD '16, 42,397 citations / 300,534 downloads)
- **Best Research Paper HM**: EARTH (HKBU, spatiotemporal K-function acceleration 26×–19×)
- **SIGKDD Innovation Award**: **Wei Wang** (UCLA)
- **Keynotes**: Jeff Dean (AI Trends: Gemini/TPU), Jingren Zhou (Alibaba CTO), Regina Barzilay (MIT)

### 6.2 Notable KDD 2026 Papers

| Paper | Affiliation | Key Contribution |
|-------|------------|-----------------|
| **MAC/MoAE** | **Alibaba** (Xiang-Rong Sheng, Han Zhu, Jian Xu, Bo Zheng) | CVR multi-attribution mechanism benchmark + Mixture-of-Asymmetric-Experts |
| **DLL** (Decoupled Listwise Learning) | Various | Streaming-compatible Listwise CTR — eliminates session batching for listwise supervision |
| **Deterministic Allocation Anonymous Joint Advertising** | **Tencent** (Zhen Zhang, Qianlong Xie) | Proves non-deterministic allocation causes infeasibility in all online ad scenarios |
| **MetaStrategy** | **Alibaba/Taobao** | LLM-generated executable ranking strategies; 0.8B Student via reward-augmented OPD; click PV +2.11%, IPV +3.12%, transaction +2.83% in online A/B |

---

## 7. ACL 2026 (San Diego, July 2–7, 2026)

**Scale**: 12,148 submissions → 2,296 accepted (18.9%) + 2,163 Findings

### 7.1 Best Paper

#### The Imperfective Paradox in Large Language Models (《大语言模型中的未完成体悖论》)
- **Authors**: Bolei Ma, Yusuke Miyao
- **Affiliation**: MCML / University of Tokyo / NII
- **Abstract**: Through the imperfective paradox (linguistic theory), shows 7B–9B models systematically violate event-entailment patterns in English — behaving as predictive narrative engines rather than logical reasoners. Demonstrates dissociation between representation and reasoning; positive effects of scale.
- **Why Important**: Goes beyond documenting failure: identifies promising path for studying logical reasoning emergence.

### 7.2 Best Theme Papers

| Paper | Key Contribution |
|-------|-----------------|
| **CoSToM** (Li et al.) | Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment |
| **Mapping the Circumplex of Affect** (Yamauchi, Aizawa — NII) | Geometric analysis of emotion representations via hyperspherical contrastive learning |

### 7.3 Best Resource Papers

| Paper | Key Contribution |
|-------|-----------------|
| **HSCodeComp** (Alibaba) | Expert-level hierarchical rule application benchmark; Qwen agent ranks 1st at 65.0% vs human 95.0%; Best Resource Paper at ACL |
| **ImplicitMemBench** (Qin et al.) | Measuring unconscious behavioral adaptation in LLMs |
| **VeriTaS** (TU Darmstadt) | First dynamic benchmark for multimodal automated fact-checking; 25K claims, 104 orgs, 54 languages |

### 7.4 Outstanding Papers (18 total, key selections)

**Reasoning, RL & Post-Training**:
- **Evolutionary Guided Decoding** (Liu et al.): Iterative value refinement for LLMs — value-guided decoding without retraining
- **Rethinking Entropy Interventions in RLVR** (Hao et al.): STEER — token-level reweighting to stabilize entropy dynamics in RLVR training
- **GeoRA** (Zhang et al.): Geometry-aware LoRA for RLVR addressing spectral collapse
- **CURE** (Chen et al.): Critique-driven unified RL for test-time self-improvement

**Agents & Evaluation**:
- **CAR-bench** (Kirmayr et al. — BMW): In-car assistant benchmark with 58 tools; best consistency score only 0.42
- **MediEval** (Qu, Färber): Medical benchmark linking MIMIC-IV records to knowledge base
- **Mind the (DH) Gap!** (Ge, Zhang, Vorobeychik — WashU): Reasoning vs conversational LLMs show different risk behavior patterns

**Safety, Trust & Detection**:
- **Lying with Truths** (Hu et al.): Multi-agent collusion via truthful evidence montage; 70%+ success across 14 LLM families; stronger reasoning models MORE susceptible
- **RACE** (Li et al.): Separates creator vs editor signatures for LLM-generated text detection

---

## 8. EMNLP 2025 (Suzhou, November 4–9, 2025)

### 8.1 Best Paper

#### Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index
- **Authors**: Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
- **Affiliation**: University of Washington / Allen AI
- **Abstract**: FM-Index-based exact n-gram search scaled to internet-level corpora.

### 8.2 Outstanding Papers (selected)

| Paper | Key Contribution |
|-------|-----------------|
| **LingGym** (Yang et al. — UBC/Waterloo) | LLM meta-linguistic reasoning benchmark for 18 endangered languages |
| **Mind the Value-Action Gap** (Shen et al.) | Do LLMs act in alignment with their values? |
| **Generative or Discriminative?** (Kasa et al.) | Classification in the era of transformers |

### 8.3 Special Awards

- **Best Theme**: InterIDEAS (philosophical intertextuality via LLMs)
- **Best Resource**: Autoformalization in the Wild (LLMs on real-world math definitions)
- **Social Impact**: AccessEval (disability bias benchmarking)
- **People's Choice**: Randomly removing 50% of dimensions in text embeddings has minimal impact

---

## 9. SIGIR 2026 (Melbourne, July 20–24, 2026)

### 9.1 Awards

- **Best Paper 2025**: WARP: An Efficient Engine for Multi-Vector Retrieval (Scheerer, Zaharia, Potts, Alonso, Khattab)
- **Test of Time 2026**: Learning to Rank with Selection Bias in Personal Search (Wang, Bendersky, Metzler — 2016)
- **Best Short Paper 2025**: Do LLMs Memorize Recommendation Datasets? (MovieLens-1M study)

### 9.2 SIGIR 2026 Workshops (notable)

- **AgentSearch**: Indexing, Retrieval, and Ranking of AI Agents — signals AI agents as first-class IR objects
- **LLM-UP**: LLM-powered User Profiling for Search and Recommendation
- **SynthIR**: Synthetic Content in Information Retrieval Ecosystems

---

## 10. WWW 2026 (The ACM Web Conference, Dubai, June 29–July 3, 2026)

### 10.1 Best Paper

#### From Retrieval to Generation: Unifying External and Parametric Knowledge for Medical Question Answering (《从检索到生成：统一外部和参数知识的医疗问答》)
- **Authors**: Lei Li, Xiao Zhou, Yingying Zhang, Xian Wu
- **Abstract**: MedRGAG framework combines retrieval and generation for medical QA. Knowledge-Guided Context Completion fills retrieval gaps; Knowledge-Aware Document Selection selects optimal evidence mixture.
- **Why Important**: Neither retrieval nor parametric knowledge alone is sufficient; unification approach.

### 10.2 Best Short Paper

#### DualGR: Generative Retrieval with Long and Short-Term Interests Modeling
- **Authors**: Zhongchao Yi, Kai Feng et al.
- **Abstract**: Generative retrieval modeling both long-term and short-term user interests.

### 10.3 Seoul Test of Time Award

**LINE: Large-scale Information Network Embedding** (Tang et al., 2016)

---

## 11. CIKM 2025 (Seoul, October 27–November 1, 2025)

### Awards
- **Best Full Paper**: Reconsidering the Performance of GAE in Link Prediction
- **Best Student Full Paper**: (announced at conference)
- **Best Short Paper**: (announced at conference)
- **Best Applied Research Paper**: (announced at conference)

---

## 12. RecSys 2025 (Prague, September 22–26, 2025)

### 12.1 Best Full Paper

#### You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control (《你不会给我带花：通过保形风险控制减轻不想要的推荐》)
- **Authors**: Giovanni De Toni, Erasmo Purificato, Emilia Gomez, Andrea Passerini, Bruno Lepri, Cristian Consonni
- **Affiliation**: University of Trento / EC JRC (European Centre for Algorithmic Transparency)
- **Abstract**: Model-agnostic, distribution-free method using conformal risk control to provably bound unwanted content in recommendations. Leverages binary feedback + implicit feedback on consumed items. Tested on popular video platform dataset.
- **Key Innovation**: Provable link between user actions (flagging content) and recommendation changes; addresses both explicit and implicit feedback.
- **Comparison**: Evaluated against LightGCL, GFormer, SiReN, SIGFormer on KuaiRand dataset.

### 12.2 Best Short Paper

#### Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems
- **Authors**: Amir Reza Mohammadi, Andreas Peintner, Michael Müller, Eva Zangerle

### 12.3 RecSys 2026 Preview

**RecSys 2026** (Minneapolis, September 27–October 2, 2026):
- **Shape Your Feed** (SYF): LLM-based agentic conversational recommendation; perception/serving/self-evolution flows; DPO alignment; 98.85% alignment accuracy; online A/B validated
- **GenRec** (Netflix): LLM-backed recommendation ranker; prefill-only inference; +1.6% offline MRR with 40× less Phase-2 data; statistically significant online gains
- **ConnectionMind** (Meta): Social graph + LLM reasoning for recommendation; SFT + RL training; +88% Recall@10 over GNN baseline; +0.43% watch time in online A/B
- **GALLM**: Graph-aware LLM for sequential recommendation; attention biases for collaborative signals; +9.76% HR@5
- **PRTA**: Personalized recommendation tool learning via autonomous language agents

---

## 13. General arXiv Highlights (Jul–Aug 2026)

### 13.1 LLM-Based Recommendation (Industrial)

| Paper | Affiliation | Key Innovation |
|-------|------------|---------------|
| **GenRec** | **Netflix** | LLM-backed ranker; prefill-only serving; context engineering replaces feature engineering |
| **ConnectionMind** | **Meta** | Social graph reasoning with LLM; SFT + RL pipeline; production-deployed |
| **MetaStrategy** | **Alibaba/Taobao** | LLM generates executable ranking strategies; 0.8B Student; +2.83% transaction amount |
| **Shape Your Feed** | RecSys '26 | Agentic conversational recommendation; real-time user-steerable feed |
| **GALLM** | Various | Graph-aware LLM; attention bias injection for collaborative signals |

### 13.2 Agents & Multi-Agent Systems

| Paper | Affiliation | Key Innovation |
|-------|------------|---------------|
| **HSCodeComp** | **Alibaba** | Expert-level hierarchical rule benchmark; 14 models tested; humans 95% vs best agent 65% |
| **CAR-bench** | **BMW Research** | In-car assistant; 58 tools; consistency testing; best score 0.42 |
| **Lying with Truths** | Various | Multi-agent collusion via truthful evidence; stronger models MORE susceptible |

### 13.3 Reasoning & RL Post-Training

| Paper | Key Innovation |
|-------|---------------|
| **JustGRPO** (ICML '26 Outstanding) | Fixed-order RL for diffusion LLMs outperforms arbitrary-order |
| **Rethinking Entropy in RLVR** (ACL '26) | STEER token-level reweighting for entropy stability |
| **GeoRA** (ACL '26) | Geometry-aware LoRA addressing spectral collapse in RLVR |
| **Evolutionary Guided Decoding** (ACL '26) | Iterative value refinement without retraining |

### 13.4 Diffusion Models & Generative

| Paper | Venue | Key Innovation |
|-------|-------|---------------|
| **High-Accuracy Sampling** | ICML '26 Outstanding | Polylog(1/δ) complexity — exponential improvement |
| **Why Diffusion Models Don't Memorize** | NeurIPS '25 Best | Two-timescale training dynamics; τ_mem ∝ n |
| **D4RT** | CVPR '26 Best | 4D reconstruction: one model, one query interface |
| **TRELLIS.2** | CVPR '26 Student | O-Voxel 3D generation with PBR materials |

### 13.5 Benchmarks & Evaluation

| Paper | Venue | Key Innovation |
|-------|-------|---------------|
| **Imperfective Paradox** | ACL '26 Best | Linguistic theory reveals LLM reasoning failures |
| **Artificial Hivemind** | NeurIPS '25 Best (D&B) | Model homogeneity crisis; Infinity-Chat dataset |
| **Mind the (DH) Gap!** | ACL '26 Outstanding | Reasoning vs conversational LLMs diverge on risk |
| **VeriTaS** | ACL '26 Best Resource | Dynamic multimodal fact-checking benchmark |

---

## 14. Cross-Conference Thematic Analysis

### 14.1 Dominant Themes (ranked by frequency across all venues)

1. **Diffusion Models**: ICML Outstanding ×2, NeurIPS Best, CVPR Best — diffusion is now first-class alongside autoregressive
2. **RL Post-Training (RLVR/GRPO)**: ICML HM (Obfuscation Atlas), NeurIPS Runner-up (RL reasoning), ACL ×4 Outstanding
3. **LLM-as-Ranker/Recommender**: Netflix GenRec, Meta ConnectionMind, Alibaba MetaStrategy, ACL best resource
4. **Agent Safety & Evaluation**: ACL (CAR-bench, Lying with Truths), ICML (Obfuscation Atlas)
5. **Multimodal Foundation Models**: CVPR (SAM 3D, D4RT), AAAI (LLM2CLIP, ReconVLA)
6. **Scaling Laws & Theory**: NeurIPS (Superposition, Grokking), ICML (High-Accuracy Sampling)
7. **Alignment as Dual-Use**: ICML Outstanding Position Paper
8. **4D/3D Reconstruction**: CVPR dominant theme
9. **Game AI / Gaming Agents**: CVPR (NitroGen)
10. **Code Execution / Formal Reasoning**: ACL (CAR-bench), various

### 14.2 Industry Lab Distribution

| Lab | Top Venues | Signature Papers |
|-----|-----------|-----------------|
| **Google DeepMind** | CVPR Best (D4RT), ICLR (Muon), NeurIPS (scaling) | 4D reconstruction, Muon optimizer |
| **Alibaba/Qwen** | NeurIPS Best (Gated Attention), ACL (HSCodeComp), KDD (MetaStrategy) | Attention gating, agent benchmarks |
| **Meta FAIR** | CVPR HM (SAM 3D), RecSys (ConnectionMind), NeurIPS (superposition) | Segment Anything 3D, social rec |
| **Microsoft Research** | ICLR Outstanding (Multi-Turn), AAAI (LLM2CLIP), CVPR Student (TRELLIS.2) | Multi-turn failures, 3D generation |
| **NVIDIA** | CVPR HM (NitroGen) | Gaming foundation model |
| **Netflix** | arXiv (GenRec) | LLM-backed recommendation ranker |
| **BMW Research** | ACL (CAR-bench) | In-car agent evaluation |
| **EC/JRC** | RecSys Best (Conformal Risk) | Safe recommendation |
| **Tsinghua** | ICML Outstanding (Flexibility Trap) | Diffusion LLM reasoning |

### 14.3 Notable Contradictions / Tensions

1. **RLVR debate**: NeurIPS runner-up shows RL doesn't add reasoning beyond base model; ICML/ACL papers still show RLVR improvements — tension between "RLVR helps" vs "RLVR merely amplifies existing capabilities"
2. **Agent safety paradox**: ACL "Lying with Truths" shows stronger reasoning models MORE susceptible to collusion — better reasoning ≠ better safety
3. **Homogeneity vs personalization**: NeurIPS "Artificial Hivemind" shows models converge; Netflix/Meta/Alibaba papers push personalized LLM-based recommendation

---

## 15. Recent arXiv Papers (Aug 17, 2026 Window)

> From same-day [[synthesis/2026-08-17/arxiv-paper-check|arxiv-paper-check]] (16 papers) — key selections relevant to conference themes:

### LLM Efficiency
- **The Sparsity Whisperer** (2608.06630): Difference-informed pruning — preserve what changes outputs, not what's big. Beats Wanda/SparseGPT across Llama 2/3.1 7B–405B.
- **Matryoshka Language Model Suites** (2608.09703): Nested training for multi-size models.

### CTR / Recommendation
- **Frequency-Domain Feature Interaction** (08-17 paper-check): Novel frequency-domain approach for feature interaction in CTR prediction.
- **Loop Scaling for Residual Connections** (08-17 paper-check): Analysis of residual connection scaling in deep recommendation models.

### Evaluation
- **Agent Evaluation Framework** (08-17 paper-check): Comprehensive evaluation of agentic systems with pruning and interpretability analysis.

---

*End of conference digest. 12 venues covered. Total unique papers highlighted: ~80+ across all sections.*
