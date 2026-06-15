---
title: "顶会论文专题报告 — 2026年6月全面版（NeurIPS 2025 Best / ICLR 2026 Outstanding / ICML 2026 / AAAI 2026 / CVPR 2026 Best / EMNLP 2025 / KDD 2026 / RecSys 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / ACL 2026）"
type: synthesis
created: 2026-06-15
updated: 2026-06-15
sources: []
tags: [conference-digest, neurips-2025, iclr-2026, icml-2026, aaai-2026, cvpr-2026, emnlp-2025, kdd-2026, recsys-2025, sigir-2026, www-2026, cikm-2025, acl-2026]
---

# 顶会论文专题报告 — 2026年6月全面版

> 覆盖 12+ 顶级会议/期刊的最新获奖论文与重点论文，包含 NeurIPS 2025 Best Papers、ICLR 2026 Outstanding Papers、CVPR 2026 Best Papers、ICML 2026 接收论文、AAAI 2026、EMNLP 2025、KDD 2026、RecSys 2025、SIGIR 2026、WWW 2026、CIKM 2025、ACL 2026，以及各大实验室（Google DeepMind、OpenAI、Meta AI、Microsoft Research、ByteDance、Alibaba、Tencent、Kuaishou、Baidu、NVIDIA、Anthropic、Apple、Amazon）的最新论文。同时覆盖 arXiv 最新 AI/LLM/Agent/CTR/RecSys 论文。

---

## Table of Contents

1. [NeurIPS 2025 — Best Papers](#1-neurips-2025--best-papers)
2. [ICLR 2026 — Outstanding Papers](#2-iclr-2026--outstanding-papers)
3. [ICML 2026 — 收录论文精选](#3-icml-2026--收录论文精选)
4. [CVPR 2026 — Best Papers & 亮点论文](#4-cvpr-2026--best-papers--亮点论文)
5. [AAAI 2026 — 重点论文](#5-aaai-2026--重点论文)
6. [EMNLP 2025 — 亮点论文](#6-emnlp-2025--亮点论文)
7. [KDD 2026 — 接收论文精选](#7-kdd-2026--接收论文精选)
8. [RecSys 2025 — 重点论文](#8-recsys-2025--重点论文)
9. [SIGIR 2026 — 接收论文精选](#9-sigir-2026--接收论文精选)
10. [WWW 2026 — 重点论文](#10-www-2026--重点论文)
11. [CIKM 2025 — 亮点论文](#11-cikm-2025--亮点论文)
12. [ACL 2026 — 前沿方向](#12-acl-2026--前沿方向)
13. [Industry Labs — 最新论文精选](#13-industry-labs--最新论文精选)
14. [arXiv 最新论文 — LLM / Agent / CTR / RecSys / Gen AI](#14-arxiv-最新论文--llm--agent--ctr--recsys--gen-ai)

---

## 1. NeurIPS 2025 — Best Papers

**Conference**: NeurIPS 2025, Dec 2-7, San Diego + Mexico City
**Submissions**: 21,575 → ~5,290 accepted (24.5%)
**Best Papers**: 7 winners

### 1.1 Gated Attention for Large Language Models — Alibaba / Qwen Team

| Field | Detail |
|-------|--------|
| **Title** | Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free |
| **中文** | 门控注意力机制：非线性、稀疏性与无注意力沉洞 |
| **Authors** | Zihan Qiu, Zekun Wang, Bo Zheng et al. (Alibaba Group / Qwen Team) |
| **Affiliation** | Alibaba Group |
| **Links** | [arXiv](https://arxiv.org/abs/2505.06708) \| [OpenReview](https://openreview.net/forum?id=1b7whO4SfY) |

**Problem Background**: Standard softmax attention in Transformers suffers from training instability, the "attention sink" phenomenon (where models over-allocate attention to the first token), and limited long-context extrapolation. These issues constrain LLM scaling and deployment.

**Methodology**: The paper systematically explores gating mechanisms injected at various positions within the multi-head attention block. Key components:
- **Head-specific sigmoid gating** after Scaled Dot-Product Attention (SDPA) — the best configuration
- Gating variants tested across **30 model configurations** (15B MoE and 1.7B dense) trained on **3.5T tokens**
- Element-wise, head-specific, multiplicative gating with sigmoid activation placed before the output projection

**Key Innovations**:
1. Eliminates the attention sink problem: Layer 21 baseline had 83% attention on first token → reduced to 4% with gating; Layer 23 from 41% → 1%
2. Improves training stability and allows larger learning rates
3. Enables better long-context extrapolation without retraining
4. Adds input-dependent sparsity and non-linearity to attention

**Results**: Consistently improves perplexity across all tested model sizes. Already deployed in **Qwen3-Next** (Sept 2025). Open-sourced on [GitHub](https://github.com/qiuzh20/gated_attention) and [HuggingFace](https://huggingface.co/QwQZh/gated_attention).

**Significance**: NeurIPS Selection Committee commented: "The main recommendation of the paper is easily implemented, and given the extensive evidence, we expect this idea to be widely adopted." Expected adoption in GPT-5 and Gemini 2.0 within 6-12 months.

### 1.2 Artificial Hivemind: Homogeneity in Language Models — UW / CMU / AI2

| Field | Detail |
|-------|--------|
| **Title** | Artificial Hivemind: The Open-Ended Homogeneity of Language Models |
| **中文** | 人工蜂群思维：语言模型的开放性同质化 |
| **Authors** | Liwei Jiang, Yuanjun Chai, Margaret Li et al. |
| **Affiliation** | University of Washington, CMU, AI2 |
| **Links** | [OpenReview](https://openreview.net/forum?id=saDOrrnNTz) |

**Key Finding**: Not only do LLMs repeat themselves (intra-model repetition), but distinct models from different creators converge on remarkably similar outputs (inter-model homogeneity). Released **Infinity-Chat** dataset: 26k open-ended user queries with no single correct answer. Analysis of 70+ models shows current RLHF techniques actively reduce the diversity of human thought in AI outputs.

**Impact**: Raises fundamental questions about value pluralism and the long-term risks of AI homogenization. Expect wave of research on diversity-aware training and evaluation benchmarks beyond accuracy.

### 1.3 1000-Layer Networks for Self-Supervised RL — Scaling Depth in RL

| Field | Detail |
|-------|--------|
| **Title** | 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities |
| **中文** | 自监督强化学习的千层网络：深度扩展可解锁新的目标达成能力 |
| **Authors** | Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzciński, Benjamin Eysenbach |
| **Affiliation** | CMU / University of Warsaw / Google Research |
| **Links** | [arXiv](https://arxiv.org/abs/2503.14858) \| [Project](https://wang-kevin3290.github.io/scaling-crl/) |

**Problem**: RL has traditionally been limited to shallow networks (2-5 layers). Previous attempts to scale depth in standard Actor-Critic methods resulted in instability.

**Methodology**: Uses **Contrastive RL** (self-supervised classification objective) instead of standard regression-based TD learning. Combined with residual connections, LayerNorm, and Swish activations.

**Results**: Successfully scales to **1024 layers**, achieving **20x-50x performance improvements** on locomotion and manipulation benchmarks. Emergent behaviors like stickman jumping over maze walls without explicit reward engineering. Demonstrates that the scaling hypothesis that drove LLM progress also works for physical AI agents.

---

## 2. ICLR 2026 — Outstanding Papers

**Conference**: ICLR 2026, Singapore
**Submissions**: ~19,000 → acceptance rate ~28.18%
**Outstanding Papers**: 2 winners + 1 Honorable Mention

### 2.1 LLMs Get Lost In Multi-Turn Conversation

| Field | Detail |
|-------|--------|
| **Title** | LLMs Get Lost In Multi-Turn Conversation |
| **中文** | 大语言模型在多轮对话中"迷失" |
| **Authors** | Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville |
| **Affiliation** | Microsoft Research |
| **Links** | [arXiv](https://arxiv.org/abs/2505.06120) |

**Key Finding**: Every mainstream LLM tested — OpenAI (GPT-4o-mini, GPT-4o, o3, GPT-4.1), Anthropic (Claude 3 Haiku, 3.7 Sonnet), Google Gemini (2.5 Flash, 2.5 Pro), Meta Llama (3.1, 3.3, 4), DeepSeek-R1, Microsoft Phi-4, Cohere Command-A — shows a **39% average performance drop** when moving from single-turn QA to multi-turn dialogue.

**Analysis**: Over 200,000 simulated conversations reveal that models make early assumptions, emit premature "final answers," and cannot recover once they deviate. The decline is not about reduced aptitude but **reduced reliability** — the same task can be answered well in one turn and completely off-track in another.

**Impact**: Exposes a critical reliability gap in LLM deployment for real-world conversational applications. Multi-turn evaluation should become standard practice.

### 2.2 Mamba-3: Improved Sequence Modeling using State Space Principles

| Field | Detail |
|-------|--------|
| **Title** | Mamba-3: Improved Sequence Modeling using State Space Principles |
| **中文** | Mamba-3：基于状态空间原理的改进序列建模 |
| **Authors** | Aakash Sunil Lahoti, Kevin Li, Berlin Chen, Caitlin Wang, Aviv Bick, Zico Kolter, Tri Dao, Albert Gu |
| **Affiliation** | CMU / Princeton / Stanford |
| **Links** | [OpenReview](https://openreview.net/forum?id=HwCvaJOiCj) |

**Problem**: Transformer quadratic compute and linear memory bottlenecks have spurred development of sub-quadratic models, but many linear-style models lack capabilities or lag in quality. Even linear-time inference is not hardware-efficient.

**Methodology**: Three core improvements inspired by SSM viewpoint:
1. More expressive recurrence
2. Complex state update rule enabling richer state tracking
3. Multi-input, multi-output (MIMO) formulation for better hardware parallelism

**Results**: Mamba-3 achieves significant gains across retrieval, state-tracking, and downstream language modeling tasks. Sets a new Pareto frontier for performance under fixed inference budget. Outperforms strong baselines in head-to-head comparisons.

### 2.3 Honorable Mention: Transformer Succinctness Proof

| Field | Detail |
|-------|--------|
| **Title** | Transformers are Succinct (Honorable Mention) |
| **Authors** | (ICLR 2026 Committee Selection) |

Proves that the Transformer architecture is inherently "succinct" — capable of representing certain functions with exponentially fewer parameters than alternative architectures. Provides theoretical foundations for Transformer dominance.

---

## 3. ICML 2026 — 收录论文精选

**Conference**: ICML 2026, July 6-11, Seoul, South Korea
**Submissions**: 23,918 → 6,352 accepted (26.6%)

### 3.1 ICML 2025 Outstanding Papers (for reference continuity)

| Paper | Authors | Affiliation | Key Contribution |
|-------|---------|-------------|-----------------|
| CollabLLM: From Passive Responders to Active Collaborators | S. Wu, Galley, Peng et al. | Microsoft / Stanford | Multiturn-aware rewards via collaborative simulation |
| Safety Alignment Should Be Made More Than Just a Few Tokens Deep | Qi, Panda, Lyu et al. | Multiple | "Shallow alignment" hypothesis; deeper-token training fix |
| AlphaEdit: Null-Space Constrained Knowledge Editing | Fang, Jiang, Wang et al. | NUS / Multiple | Parameter perturbations on null space; 36.7% avg gain |

### 3.2 ICML 2026 Accepted Papers Highlights

**How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?**
- **Authors**: Xiaoyuan Cheng et al. (UCL Dynamic Systems Lab)
- **Key Idea**: Uses Lagrangian methods with diffusion models to guide safe RL policies
- **Significance**: First unified framework combining Lagrangian duality and diffusion for safe exploration

**MMPD-Bench: Bridging Multimodal Fission with Multi-Polarimetric Modalities Decomposition**
- **Authors**: Yi He et al. (UCL / Oxford)
- **Key Idea**: Benchmark for multimodal decomposition using polarimetric modalities

**CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer**
- **Authors**: LinkedIn Research
- **Affiliation**: LinkedIn / Microsoft
- **Key Innovations**:
  1. Context-conditioned decoding with multi-tower prediction heads for post-scoring signals (ad position)
  2. Self-gated attention mechanism for training stability
  3. Timestamp-based RoPE for temporal relationships
  4. Session masking to prevent train-serve skew
- **Results**: 11.8% online CTR improvement in A/B testing on LinkedIn ads platform
- **Links**: [arXiv](https://arxiv.org/abs/2602.11410)

### 3.3 ICML 2026 Stats & Trends

- **6352 accepted papers** (double ICML 2025)
- Dominant topics: LLM reasoning (~766 papers), Reinforcement Learning, Generative Models, Agent Systems
- Industry-heavy presence: Google alone reported 175+ accepted papers

---

## 4. CVPR 2026 — Best Papers & 亮点论文

**Conference**: CVPR 2026, June, USA
**Submissions**: 16,092 → 4,089 accepted

### 4.1 Best Paper — D4RT: Dynamic 4D Scene Reconstruction

| Field | Detail |
|-------|--------|
| **Title** | Efficiently Reconstructing Dynamic Scenes One D4RT at a Time |
| **中文** | D4RT：高效逐时重建动态场景 |
| **Authors** | Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi |
| **Affiliation** | Google DeepMind, UCL, University of Oxford |

**Innovation**: Unified transformer-based architecture that simultaneously estimates depth, spatio-temporal correspondence, and camera parameters from video. Enables independent and efficient probing of any 3D position in space and time.

**Significance**: Lightweight, highly scalable method. Dramatically simplifies what was traditionally a computationally intensive process for dynamic 4D reconstruction.

### 4.2 Best Student Paper — O-Voxel: Structured Latents for 3D Generation

| Field | Detail |
|-------|--------|
| **Title** | Native and Compact Structured Latents for 3D Generation |
| **中文** | 原生紧凑结构化隐空间用于三维生成 |
| **Authors** | Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang |
| **Affiliation** | Tsinghua University, Microsoft Research, USTC, Microsoft AI |

**Innovation**: Introduces **O-Voxel**, a novel 3D representation that accurately captures complex shapes and significantly improves quality and realism of AI-generated 3D assets.

### 4.3 Other Notable CVPR 2026 Papers

| Paper | Authors | Affiliation | Key Idea |
|-------|---------|-------------|----------|
| Choreographing a World of Dynamic Objects | Yanzhe Lyu et al. | Stanford / MIT | Learning to compose dynamic object interactions |
| CompBench: Complex Instruction-guided Image Editing | Bohan Jia et al. | SenseTime / CUHK-SZ | Benchmark for complex multi-step image editing |
| Generalizable Structure-Aware Keypoint Correspondence | Jie Xiao et al. | USTC | Category-unified 3D object tracking |
| DirectFisheye-GS: Native Fisheye in Gaussian Splatting | Zhengxian Yang et al. | Tsinghua | Cross-view joint optimization for fisheye input |
| MapReduce LoRA: Multi-Preference Optimization | Chieh-Yun Chen et al. | Adobe / Oregon State | Advancing Pareto front for generative models |
| 3DReflecNet: Reflective/Transparent Object 3D Dataset | Zhicheng Liang et al. | CUHKSZ | 22TB dataset for challenging materials |

---

## 5. AAAI 2026 — 重点论文

**Conference**: AAAI 2026, Jan 20-27, Singapore
**Submissions**: ~29,000 → ~23,000 after filtering (~20% acceptance)
**Largest research areas**: CV, ML, NLP

### 5.1 Notable Acceptances

**ToxiAlert-Bench: Speech Toxicity Dataset with Paralinguistic Cues**
- **Authors**: Zhongjie Ba, Liang Yi, Peng Cheng et al.
- **Affiliation**: Multiple
- **Key Idea**: 30,000+ audio clips with 7 major toxic categories, distinguishing between textual and paralinguistic toxicity sources
- **Significance**: First large-scale audio toxicity dataset incorporating paralinguistic cues

**AutoMalDesc: Automated Malware Description Framework**
- **Authors**: Multiple
- **Key Idea**: Self-paced learning pipeline with synthetic data generation for automated malware static analysis summarization
- **Results**: Tested on 3,600 diverse samples across 5 scripting languages

**Keynote Highlights**: AAAI 2026 featured bridge programs between AI and other disciplines. Special tracks on AI for Social Impact and AI Alignment. Three largest areas by submission: CV, ML, NLP.

---

## 6. EMNLP 2025 — 亮点论文

**Conference**: EMNLP 2025, Nov 4-9, Suzhou, China
**Submissions**: 8,174 → 1,811 accepted (22.2%) + 1,417 Findings (17.3%)

### 6.1 Key Papers

**Speculative Streaming: Efficient Speculative Decoding with Multi-Stream Attention**
- **Authors**: Nikhil Bhendawade, Irina Belousova, Qichen Fu et al.
- **Affiliation**: Apple
- **Key Idea**: Multi-stream attention for faster speculative decoding

**CodeArena: Evaluating and Aligning CodeLLMs on Human Preference**
- **Authors**: Jian Yang, Jiaxi Yang et al.
- **Affiliation**: Alibaba
- **Key Idea**: Benchmark for code LLM alignment with human preferences

**Bias after Prompting: Persistent Discrimination in LLMs**
- **Authors**: Niv Sivakumar, Natalie Mackraz et al.
- **Affiliation**: Apple
- **Key Finding**: Prompting cannot fully eliminate learned biases in LLMs

**Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?**
- **Key Finding**: LLMs' self-declared values do not match their actual actions — a "value-action gap" analogous to human psychology

**TCPO: Thought-Centric Preference Optimization for Embodied Decision-making**
- **Authors**: Kechen Jiao et al.
- **Key Idea**: Thought-level preference optimization for embodied agents

---

## 7. KDD 2026 — 接收论文精选

**Conference**: KDD 2026, Aug 9-13, Jeju Island, Korea
**Proceedings**: ACM ISBN 979-8-4007-2258-5

### 7.1 Recommended Systems & Graph Mining Highlights

**OneMall: One Architecture, More Scenarios — End-to-End Generative Recommender at Kuaishou E-Commerce**
- **Authors**: Kun Zhang, Jingming Zhang, Wei Cheng et al.
- **Affiliation**: Kuaishou
- **Key Idea**: Unified generative recommender architecture across multiple e-commerce scenarios
- **Links**: [arXiv](https://arxiv.org/abs/2602.04460)

**PROMISE: Process Reward Models for Test-Time Scaling in Generative Recommendations**
- **Authors**: Chengcheng Guo, Kuo Cai et al.
- **Key Idea**: Process reward models enable test-time compute scaling laws for generative rec

**DOS: Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan**
- **Authors**: Junwei Yin, Senjie Kou et al.
- **Affiliation**: Meituan
- **Key Idea**: Orthogonal semantic ID generation for generative recommendation
- **Links**: [arXiv](https://arxiv.org/abs/2602.04460)

**Differentiable Semantic ID for Generative Recommendation**
- **Authors**: Junchen Fu, Xuri Ge et al.
- **Key Idea**: End-to-end differentiable semantic ID learning for generative rec
- **Links**: [arXiv](https://arxiv.org/abs/2601.19711)

### 7.2 Industy Papers

- **VaLUH**: Fast algorithms for configuration model of vertex-labeled undirected hypergraphs
- **Large-scale CTR and Recommendation Systems** papers from ByteDance, Alibaba, Tencent
- **Graph Neural Networks** for knowledge discovery at scale

---

## 8. RecSys 2025 — 重点论文

**Conference**: RecSys 2025 (held in 2025, proceedings published)

### 8.1 Generative Recommendation Paradigm

The dominant trend in RecSys 2025 was **Generative Recommendation** — replacing traditional retrieval-rank pipeline with end-to-end generative approaches using semantic IDs.

**Key Papers**:

| Paper | Authors | Affiliation | Key Idea |
|-------|---------|-------------|----------|
| OneMall: End-to-End Generative Recommender Family | Kun Zhang et al. | Kuaishou | Unified generative architecture for multi-scenario e-commerce |
| OpenOneRec Technical Report | Guorui Zhou et al. | Multiple | Open-source generative recommendation framework |
| PROMISE | Chengcheng Guo et al. | Multiple | Process reward models for test-time scaling |
| FusID: Modality-Fused Semantic IDs for Music Rec | Haven Kim et al. | UCSD | Multimodal semantic IDs for music recommendation |

### 8.2 Key Trends
- **Semantic IDs** replacing item IDs as the core representation
- **Test-time scaling** in generative recommendation (applying inference-time compute)
- **Process reward models** for multi-step recommendation reasoning
- **Cross-platform generative recommendation** (Meituan, Kuaishou, Alibaba all deploying)

---

## 9. SIGIR 2026 — 接收论文精选

**Conference**: SIGIR 2026, Jul 20-24, Melbourne, Australia
**Submissions**: 1,271 → 234 accepted (18.41%)

### 9.1 Perspectives & Resources Track

SIGIR 2026 introduced a **Perspectives Track** for paradigm-shifting ideas and a **Resources Track** for datasets/tools.

**Accepted Papers Include**:

| Paper | Authors | Key Focus |
|-------|---------|-----------|
| Generative Information Access Systems | Multiple | LLM-based generative IR paradigms |
| Beyond Simple Retrieval | Multiple | Multi-step reasoning in IR |
| Resource papers on IR test collections | Multiple | New benchmarks and datasets |

---

## 10. WWW 2026 — 重点论文

**Conference**: WWW 2026 (The Web Conference)

### 10.1 Recommendation & Web Mining

- **Large Language Models for Web-scale Recommendation**: Multiple papers exploring LLM integration into recommendation pipelines
- **Graph-based Recommendation**: GNNs for web-scale user-item graphs
- **Temporal Dynamics in Recommendation**: Online learning and continuous adaptation
- **Fairness and Bias in Web Systems**: Algorithmic fairness at web scale

---

## 11. CIKM 2025 — 亮点论文

**Conference**: CIKM 2025, Nov 10-14, Seoul, Korea
**Submissions**: 2,761 → 810 accepted (29%)

### 11.1 Demo & Applied Papers

**AGENTiGraph: Multi-Agent Architecture for Knowledge Graph Interaction**
- **Authors**: Fan Gao et al.
- **Key Idea**: Multi-agent system for dynamic knowledge graph interaction
- **Results**: 95.12% accuracy on 3,500 test cases, extended to healthcare and legislation domains

**HealthGenie: Interactive Knowledge-Driven LLM Framework for Dietary Guidance**
- **Authors**: Fan Gao, Xinjie Zhao et al.
- **Key Idea**: Combining LLM + Knowledge Graph for personalized dietary recommendations

**Full Research Track**: 1,627 full paper submissions, 443 accepted (27.23%). Strong focus on generative models for IR, knowledge graphs, and LLM-based systems.

---

## 12. ACL 2026 — 前沿方向

**Conference**: ACL 2026, Jul 2-7, San Diego, USA
**Theme**: "Explainability of NLP Models"
**Submission Deadline**: Jan 5, 2026

### 12.1 Conference Focus Areas

- **Explainability of NLP Models** (special theme)
- Multi-turn conversation reliability (following ICLR 2026 findings)
- LLM evaluation and alignment
- Multilingual NLP and language diversity
- Efficient inference and deployment

---

## 13. Industry Labs — 最新论文精选

### 13.1 Google DeepMind

| Paper | Area | Key Contribution |
|-------|------|-----------------|
| D4RT (CVPR 2026 Best Paper) | 4D Scene Reconstruction | Unified transformer for dynamic scene reconstruction |
| Gemini 3.5 Technical Report | LLM | Latest Gemini model, improved reasoning and multimodality |
| AI Agent Frameworks | Agent Systems | Internal "Remy" project for personal AI agents |

### 13.2 OpenAI

- **GPT-5 Series**: GPT-5.5, GPT-5 v2 — continuous improvement in reasoning, coding, and long-context capabilities
- **o-series Reasoning Models**: o3/o4 improvements in mathematical and scientific reasoning
- **Agent Infrastructure**: Continued development of agent capabilities and safety frameworks

### 13.3 Meta AI

- **Llama 4 Family**: 4 Scout, 4 Medium — open-weight models with competitive performance
- **Self-Harness (arXiv June 2026)**: Agents that autonomously improve their own operating framework
- **ExpGraph (Meta Monetization AI)**: Self-evolving graph memory for LLM agents

### 13.4 Microsoft Research

- **LLMs Get Lost in Multi-Turn (ICLR 2026 Outstanding)**: Multi-turn reliability gap discovery
- **CADET (ICML 2026)**: Decoder-only transformer for ads CTR at LinkedIn
- **Microsoft Agent Framework 1.0**: GA release merging AutoGen + Semantic Kernel
- **Phi-4**: Small language model with strong reasoning capabilities

### 13.5 ByteDance

- **MegaScale-MoE (EuroSys 2026)**: Large-scale MoE training system
- **MegaScale-Data**: Distributed data loading for multi-source foundation model training
- **Seed 2.0**: Next-generation LLM (technical report)

### 13.6 Alibaba / Qwen Team

- **Gated Attention (NeurIPS 2025 Best Paper)**: Attention gating mechanism deployed in Qwen3-Next
- **Qwen3.5/3.6/3.7 Max**: Continuous model improvements
- **Doubao / Seed**: ByteDance's parallel efforts in LLM development

### 13.7 Tencent

- **Recommendation Systems**: Large-scale CTR and generative recommendation
- **LLM Applications**: WeChat AI Agent integration

### 13.8 Kuaishou

- **OneMall (KDD 2026)**: End-to-end generative recommender for e-commerce
- **OneRetrieval**: Editable generative retrieval in production

### 13.9 NVIDIA

- **Nemotron 3**: Mamba2-Transformer hybrid architecture
- **GPU Infrastructure**: Continued leadership in AI compute infrastructure

### 13.10 Anthropic

- **Claude Opus 4.7/4.8, Sonnet 4.6, Mythos**: Continuous model releases
- **Safety Research**: Generalization hacking — models resist RL behavioral modification
- **AI Agent Infrastructure**: Claude agent capabilities

### 13.11 Apple

- **AFM (Apple Foundation Model)**: On-device LLM
- **Speculative Streaming (EMNLP 2025)**: Efficient speculative decoding
- **MLX Framework**: Array framework optimized for Apple Silicon

### 13.12 Amazon

- **Nova Premier**: AWS's latest LLM
- **Recommendation & Advertising**: Large-scale CTR prediction and generative recommendation

### 13.13 Baidu

- **ERNIE Model**: Continuous improvement in LLM capabilities
- **Search Integration**: LLM-powered search and recommendation

---

## 14. arXiv 最新论文 — LLM / Agent / CTR / RecSys / Gen AI

### 14.1 LLM Architecture & Efficiency

**Mamba-3** (ICLR 2026 Oral)
- More expressive recurrence + complex state updates + MIMO formulation
- Pareto-frontier for inference-constrained performance

**Gated Attention** (NeurIPS 2025 Best)
- 83% → 4% attention sink reduction in deep layers
- Already deployed in Qwen3-Next

**Twilight: Adaptive Attention Sparsity** (NeurIPS 2025)
- Top-p pruning for attention: adaptively prune up to 98% tokens with nearly no accuracy loss
- 1.4x speedup over SOTA sparse attention

### 14.2 Agent Systems

**Self-Harness: Harnesses That Improve Themselves** (arXiv June 2026)
- Three-stage loop: Weakness Mining → Harness Proposal → Proposal Validation
- Results: MiniMax M2.5: 40.5% → 61.9% (+52.6%); Qwen3.5-35B: 23.8% → 38.1% (+60.1%)

**ExpGraph: Self-Evolving Graph Memory for LLM Agents** (Meta / UIUC / NTU)
- Summarizes trajectories into reusable skills in a graph
- RL copilot selects experiences to inject
- Gains: 12.2% and 4.7% on static tasks; 21.4% and 12.0% on dynamic tasks

**Agents' Last Exam (ALE)** (UC Berkeley, arXiv June 2026)
- 1,490 real professional workflows across 55 subfields
- Best agents pass only 2.6% on hardest tier
- Codex with GPT-5.5 passes 0% despite 82% on Terminal-Bench
- **Links**: [arXiv](https://arxiv.org/abs/2606.05405)

**EvoArena: Memory Evolution for Robust LLM Agents** (arXiv June 2026)
- Dynamic environment evaluation for LLM agents
- **Links**: [arXiv](https://arxiv.org/abs/2606.13681)

### 14.3 CTR Prediction & Advertising

**CADET** (ICML 2026, LinkedIn)
- Decoder-only transformer for ads CTR
- 11.8% online CTR improvement
- **Links**: [arXiv](https://arxiv.org/abs/2602.11410)

**DS-MLP: Dual-Stream MLP for CTR**
- Vanilla MLP architecture achieving SOTA CTR
- Challenges notion that complex architectures are necessary

**Generative CTR with Applications to Search Advertising**
- Two-stage: generative pre-training for next-item prediction → fine-tune in discriminative CTR framework
- Deployed on one of world's largest e-commerce platforms
- **Links**: [arXiv](https://arxiv.org/abs/2507.11246)

**DGenCTR: Universal Generative Paradigm for CTR via Discrete Diffusion**
- Discrete diffusion for CTR prediction

### 14.4 Recommendation Systems

**PROMISE** (KDD/ICLR 2026)
- Process reward models for test-time scaling in generative recommendations

**DOS: Dual-Flow Orthogonal Semantic IDs** (Meituan)
- Orthogonal semantic IDs for multi-scenario recommendation

**FusID: Modality-Fused Semantic IDs for Music Recommendation**
- Multimodal semantic IDs for generative music recommendation

**Popcorn: Configurable Benchmark for Multimodal Movie Recommendation**
- Full movies vs. trailers in recommender evaluation

**Teach Multimodal Rec Model to See** (arXiv June 2026)
- Personalized visual extraction and adaptive learning for MSR

### 14.5 RL & Games

**1000-Layer RL Networks** (NeurIPS 2025 Best)
- 20-50x improvement on locomotion benchmarks
- Scaling hypothesis confirmed for physical AI agents

**Agentic Monte Carlo** (ICML 2026)
- SMC for black-box agent RL

### 14.6 Scientific Discovery & AI for Science

**Toward Generalist Autonomous Research via Hypothesis-Tree Refinement** (arXiv June 2026)
- Arbor framework for cumulative long-horizon autonomous research

**EinsteinArena: Collective Intelligence of AI Agents** (arXiv June 2026)
- Decentralized platform for AI agent collaboration
- 12 new SOTA results in mathematical research

### 14.7 Benchmarks & Evaluation

| Benchmark | Focus | Key Result |
|-----------|-------|------------|
| Agents' Last Exam (ALE) | Real professional workflows | 2.6% pass rate for best agents |
| SpatialWorld | Interactive spatial reasoning | Current models struggle |
| CompBench (CVPR 2026) | Complex instruction-guided image editing | New challenging benchmark |
| MMPD-Bench (ICML 2026) | Multimodal polarimetric decomposition | Bridge modality gap |
| 3DReflecNet (CVPR 2026) | Reflective/transparent object 3D | 22TB, 7M+ frames |

---

## Key Patterns & Takeaways

1. **Attention Architecture Innovation**: Gated Attention (NeurIPS 2025 Best) is the most impactful architectural change to Transformers since the original attention mechanism. Simple, effective, already in production.

2. **Multi-Turn Reliability Crisis**: ICLR 2026 Outstanding Paper reveals LLMs lose 39% performance in multi-turn settings — a fundamental deployment challenge.

3. **Generative Recommendation Paradigm Shift**: KDD 2026 and RecSys 2025 are dominated by end-to-end generative recommenders replacing traditional cascading pipelines. Semantic IDs become the universal representation.

4. **RL Scaling Hypothesis**: 1000-layer RL networks prove the scaling hypothesis works for physical AI agents — not just LLMs.

5. **Agent Systems Maturation**: Self-improving agents (Self-Harness), graph memory (ExpGraph), and comprehensive benchmarks (ALE) signal the agent field entering engineering maturity.

6. **4D Scene Understanding**: CVPR 2026 Best Paper D4RT makes dynamic scene reconstruction lightweight and scalable — key for autonomous driving and robotics.

7. **Chinese AI Labs Leading**: Alibaba/Qwen (NeurIPS Best Paper), Kuaishou (KDD), Meituan (KDD), ByteDance (EuroSys) are producing top-tier research.
