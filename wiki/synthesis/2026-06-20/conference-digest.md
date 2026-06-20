---
title: "顶会论文专题报告 — 2026年6月全面版（NeurIPS 2025 Best / ICLR 2026 Outstanding / ICML 2026 / AAAI 2026 / CVPR 2026 Best / EMNLP 2025 / KDD 2026 / RecSys 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / ACL 2026）"
type: synthesis
created: 2026-06-20
updated: 2026-06-20
sources: [arxiv]
tags: [neurips-2025, iclr-2026, icml-2026, aaai-2026, cvpr-2026, emnlp-2025, kdd-2026, recsys-2025, sigir-2026, www-2026, cikm-2025, acl-2026, llm, ctr, recommendation, games, agents, generative-models, sequential-modeling, reinforcement-learning, survey]
---

# Conference Digest — 顶会论文专题报告

> 2026年6月20日全面版 | 12+ conferences, 50+ highlighted papers, 13+ industry labs
>
> 涵盖: NeurIPS 2025 Best Papers / ICLR 2026 Outstanding / ICML 2026 / AAAI 2026 / CVPR 2026 Best / EMNLP 2025 / KDD 2026 / RecSys 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / ACL 2026

---

## 目录

1. [NeurIPS 2025 — Best Papers & Runners-Up](#1-neurips-2025)
2. [ICLR 2026 — Outstanding Papers](#2-iclr-2026)
3. [ICML 2026 — Key Papers](#3-icml-2026)
4. [AAAI 2026 — Outstanding Papers](#4-aaai-2026)
5. [CVPR 2026 — Best Papers](#5-cvpr-2026)
6. [EMNLP 2025 — Highlights](#6-emnlp-2025)
7. [KDD 2026 — Acceptances & Trends](#7-kdd-2026)
8. [RecSys 2025 — Key Papers](#8-recsys-2025)
9. [SIGIR 2026 — Acceptances](#9-sigir-2026)
10. [WWW 2026 — Industry Papers](#10-www-2026)
11. [CIKM 2025 / ACL 2026 — Brief](#11-cikm-2025--acl-2026)
12. [Frontier Model Reports — New Releases](#12-frontier-model-reports)
13. [Key Themes & Synthesis](#13-key-themes--synthesis)

---

## 1. NeurIPS 2025

**Location**: San Diego, CA | **Date**: Dec 2-8, 2025 | **Acceptance**: 5,276 papers (25.4%)

### Best Paper Award

#### Gated Attention for LLMs: Non-linearity, Sparsity, and Attention-Sink-Free

- **中文标题**: 门控注意力: 非线性、稀疏性与无注意力沉降
- **Authors**: Alibaba Qwen Team (pending full author list)
- **Affiliation**: Alibaba / Qwen
- **Abstract**: 提出在 Scaled Dot-Product Attention (SDPA) 后添加一个 head-specific sigmoid gate。这一简单修改在多个维度上带来一致提升：训练稳定性增强、对更大学习率的容忍度更高、缩放性质改善。关键创新在于：(1) 在 softmax attention 的低秩映射上引入非线性；(2) 施加 query-dependent 稀疏门控分数来调节 SDPA 输出。值得注意的是，Gated Attention 实现了 attention-sink-free 的长上下文行为。
- **arXiv**: 待确认 (gated-attention)
- **Comparison**: 对比标准 softmax attention，门控机制在长上下文任务上消除 attention sink 问题，训练更稳定。

#### Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)

- **中文标题**: 人工蜂群思维: 语言模型的开放性同质化
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: UW / Allen AI
- **Abstract**: 揭示 LLM 在生成多样化创意内容方面的根本缺陷。发布大规模开放式 prompt 数据集，证明 LLM 倾向于产生"人工蜂群思维"——生成惊人相似的答案。测量了多样性崩溃的程度，警示长期反复接触相似输出可能导致人类思维的同质化。

### Best Paper Runners-Up

#### Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

- **中文标题**: 强化学习真能激励 LLM 超越基础模型的推理能力吗？
- **Authors**: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang
- **Affiliation**: Tsinghua University
- **Abstract**: (RLVR Critique Paper) 系统性质疑当前 RLVR 的效果。通过在大 k 值的 pass@k 评估下对比 RLVR-trained 模型与基础模型，发现 **RLVR 并未激发全新的推理模式**——RLVR 提升的是采样效率（sampling efficiency）而非推理能力本身。基础模型在足够大的 k 下能达到同样水平。对 RL for Reasoning 领域提出根本性质疑。
- **Key Finding**: RLVR 使模型在较小 k 值（如 k=1）下表现更好，但并未真正扩展推理能力的边界。

#### Optimal Mistake Bounds for Transductive Online Learning

- **中文标题**: 转导在线学习的最优错误界
- **Authors**: Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer
- **Abstract**: 解决了 30 年来的开放问题：证明对于每个 Littlestone 维度 d 的概念类，转导错误界至少为 Ω(√d)，将之前的下界从 O(log d) 指数级提升到 Ω(√d)。证明该界是紧的。

### Test of Time Award

#### Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

- **Authors**: Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun
- **Year**: 2015 — 10 年最具影响力论文

---

## 2. ICLR 2026

**Location**: Rio de Janeiro, Brazil | **Date**: April 23-27, 2026 | **Acceptance**: 4,361 papers (from ~5,355 accepted on OpenReview) | **Outstanding**: 3 papers

### Outstanding Papers

#### Transformers are Inherently Succinct

- **中文标题**: Transformer 本质上具有简洁性
- **Venue**: ICLR 2026 Outstanding
- **Abstract**: 从理论上证明 Transformer 架构具有内在的简洁性（succinctness）——即它们可以用比传统模型更少的参数表达某些函数。这一发现解释了 Transformer 在多种任务上的泛化优势。
- **arXiv**: 待补充

#### Multi-Turn LLM Degradation (Mamba-3 related)

- **Venue**: ICLR 2026 Outstanding
- **Related**: Mamba-3 (CMU/Princeton, inference-first SSM)

#### MEM1: Memory-Reasoning Synergy for Long-Horizon Agents

- **中文标题**: MEM1: 面向长时域 Agent 的记忆-推理协同
- **Venue**: ICLR 2026
- **Abstract**: 提出记忆-推理协同框架，解决长时域任务中的记忆衰减和推理退化问题。在需要长期依赖的复杂任务上显著超越现有方法。

#### AgentFlow: 7B Beats GPT-4o

- **Venue**: ICLR 2026
- **Abstract**: 仅 7B 参数的 agent 系统通过流式协作范式在多种 agent 基准上超越 GPT-4o，证明模型大小不是 agent 性能的唯一决定因素。
- **arXiv**: 2510.05592

### Notable ICLR 2026 Papers

| Paper | Affiliation | Topic |
|-------|-----------|-------|
| Planner Aware Path Learning (PAPL) | Multiple | Diffusion LM training-inference alignment |
| Principled RL for Diffusion LLMs (ESPO) | - | RL for discrete diffusion |
| AutoEP: LLMs-Driven Hyperparameter Evolution | - | Metaheuristic optimization |
| In-The-Flow Agentic System Optimization | Stanford | Agent planning & tool use |
| Latent Particle World Models | - | Object-centric self-supervised dynamics |
| ECF8: Exponent-Concentrated FP8 | Multiple | Memory-efficient quantization |
| SPIRAL: Self-Play Incentivizes Reasoning | - | Game self-play for LLM reasoning |
| CDE: Curiosity-Driven Exploration for RLVR | - | RLVR exploration |
| OffTopicEval | - | LLM conversation evaluation |
| Mitigating Non-IID Drift in Federated LLM Fine-Tuning | - | Federated learning |

---

## 3. ICML 2026

**Location**: Seoul, South Korea | **Date**: July 2026 | **Acceptance**: 6,500+ papers (from ~28,000 submissions)

### Key Highlights

#### Shannon Scaling Law: LLMs as Noisy Channels

- **中文标题**: 香农缩放定律: 将 LLM 视为噪声信道
- **Venue**: ICML 2026
- **Abstract**: 从信息论角度重新诠释 LLM 的缩放行为，将 LLM 建模为噪声信道，推导出新的 scaling law 形式。为理解模型规模、数据量和性能之间的关系提供了理论基础。

#### Self-Supervised Flow Matching (Self-Flow)

- **中文标题**: 自监督流匹配
- **Venue**: ICML 2026
- **Abstract**: 提出无需配对数据的自监督流匹配框架，用于可扩展的多模态合成。

#### CTR-RL: Reinforcement Learning for CTR Optimization

- **Venue**: ICML 2026
- **Abstract**: 将 CTR 预测任务形式化为强化学习问题，在长期用户价值优化上取得突破。

#### How Chain-of-Thought Decomposes Tasks

- **中文标题**: CoT 如何分解任务
- **Venue**: ICML 2026
- **Abstract**: 理论分析 Chain-of-Thought 如何将复杂任务分解为可管理的子步骤，解释 CoT 的泛化能力。

#### ALIVE: Interactive Frontend Games via RL

- **中文标题**: ALIVE: 通过强化学习实现交互式前端游戏
- **Affiliation**: Alibaba
- **Venue**: ICML 2026
- **Abstract**: 使用 RL 自动生成交互式前端游戏，展示了游戏生成与 RL 的结合。

#### UniAR: Unified Multimodal Autoregressive Modeling

- **中文标题**: UniAR: 统一多模态自回归建模
- **Affiliation**: Alibaba
- **Venue**: ICML 2026
- **Abstract**: 统一的视觉-语言自回归框架。

#### Complete-muE: MoE Hyperparameter Transfer

- **Affiliation**: -
- **Venue**: ICML 2026
- **Abstract**: 混合专家模型（MoE）的超参数迁移方法。

#### Toward Calibrated Mixture-of-Experts Under Distribution Shift

- **Venue**: ICML 2026
- **Authors**: Gina Wong, Drew Prinster, Suchi Saria, Rama Chellappa, Anqi Liu
- **Abstract**: 在分布漂移下校准 MoE 模型。

### ICML 2026 Statistics & Trends

- **6,500+ accepted papers** (ICML 2025 was ~3,200)
- **Trends**:
  - AI Agents: ~465 papers on agents (significant increase)
  - RL for LLM reasoning: major sub-topic
  - Diffusion / Flow Matching: continued growth
  - Multimodal models: unified architecture trend
  - Efficient ML: quantization, pruning, distillation

---

## 4. AAAI 2026

**Location**: Singapore | **Date**: Jan 20-27, 2026 | **Submissions**: 23,680 | **Acceptance**: 4,167 (17.6%)

### Outstanding Papers (Main Track - 5 papers)

#### Outstanding Paper 1: Model Change for Description Logic Concepts

- **Authors**: Ana Ozaki, Jandson S. Ribeiro
- **Abstract**: 研究了在模型（以 pointed interpretations 表示）下修改描述逻辑概念的问题。定义了三种变更：eviction（移除模型）、reception（合并模型）、revision（结合两者）。证明 revision 不能简化为 eviction 和 reception 的简单组合。

#### Outstanding Paper 2: Causal Structure Learning for [Topic TBD]

- **Abstract**: 因果关系发现的新方法。

#### Other Outstanding Papers

5 main-track + 2 AI for Social Impact 论文获奖。完整列表见 [AIHub 报道](https://aihub.org/2026/01/22/congratulations-to-the-aaai2026-outstanding-paper-award-winners/)。

### Key Topics by Industry Labs

| Lab | Focus Area |
|-----|-----------|
| Amazon | LLM for robotics, NLP at scale |
| Microsoft | AI agents, RAG systems |
| IBM | Trustworthy AI, time-series |
| Huawei | Multimodal AI, efficient training |

### Notable AAAI 2026 Papers

| Paper | Affiliation | Topic |
|-------|-----------|-------|
| LogicCat: Chain-of-Thought Text-to-SQL Benchmark | Multiple | Text-to-SQL, complex reasoning |
| CogniTrust: Robust Hashing with Cognitive Memory | Peking University | Noisy labels, memory models |
| ReconVLA / VLA-Adapter | - | Vision-Language-Action (Oral) |

### Trend: Large-Scale AI Review Pilot

AAAI 2026 进行了史上最大规模的 AI 辅助同行评审实验：使用 AI 为 22,977 篇论文生成评审（不包含分数，不替代人类评审）。这是顶级 AI 会议首次在所有技术轨道部署生成式 AI 评审。

---

## 5. CVPR 2026

**Location**: Denver, CO | **Date**: June 3-7, 2026 | **Submissions**: 16,092 | **Acceptance**: 4,090 (25.42%)

### Best Paper Award

#### D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time

- **中文标题**: D4RT: 高效动态场景重建
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: Google DeepMind / UCL / Oxford
- **Abstract**: 提出 D4RT 网络，从视频中重建动态 4D 场景的几何和运动。使用统一的 transformer 架构估计深度、时空对应关系和完整相机参数。该方法实现了轻量级和高可扩展性的动态场景重建，训练和推理都极为高效。

### Best Student Paper Award

#### Native and Compact Structured Latents for 3D Generation

- **中文标题**: 面向 3D 生成的原生紧凑式结构潜变量
- **Authors**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **Affiliation**: Tsinghua University / Microsoft Research / USTC / Microsoft AI
- **Abstract**: 提出新的 3D 生成建模方法，显著提升 AI 生成 3D 资产的真实感和质量。在真实物体和场景的人类偏好测试中获得至少 5:1 的胜率。

### Best Paper Honorable Mentions

#### NitroGen: An Open Foundation Model for Generalist Gaming Agents

- **中文标题**: NitroGen: 通用游戏智能体的开放基础模型
- **Affiliation**: NVIDIA
- **Venue**: CVPR 2026 Honorable Mention
- **Abstract**: NVIDIA 的通用化游戏智能体基础模型，支持多种游戏类型的智能决策。

### CVPR 2026 Key Statistics

- **16,092 submissions** (+24% from 2025), **4,090 accepted**
- Top affiliations by paper count: Chinese institutions dominate; NVIDIA (50+ papers), Google DeepMind, Meta
- Key trends: 4D vision, 3D generation, generalist gaming agents, multimodal understanding

---

## 6. EMNLP 2025

**Location**: Suzhou, China | **Date**: Nov 4-9, 2025 | **Submissions**: 8,174 | **Acceptance**: 1,811 Main (22.16%) + 1,417 Findings

### Key Papers

#### S1: Simple Test-time Scaling

- **Affiliation**: Stanford
- **Venue**: EMNLP 2025
- **Abstract**: 提出简化的 test-time scaling 方法，为推理时计算扩展提供了实用方案。

#### Speculative Streaming: Efficient and Scalable Speculative Decoding

- **Affiliation**: Apple
- **Venue**: EMNLP 2025
- **Authors**: Nikhil Bhendawade, Irina Belousova, Qichen Fu, Henry Mason, Antonie Lin, Mohammad Rastegari, Mahyar Najibikohnehshahri
- **Abstract**: Apple 提出的 multi-stream attention 投机解码方法，显著提升 LLM 推理效率。

#### Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?

- **中文标题**: 注意价值-行动差距: LLM 的行为与其声称的价值一致吗？
- **Venue**: EMNLP 2025
- **Abstract**: 揭示了 LLM 声称的价值与实际行为之间的不一致，对 AI 对齐研究有重要启示。

#### Evaluating Evaluation Metrics — The Mirage of Hallucination Detection

- **Affiliation**: Apple
- **Venue**: EMNLP 2025
- **Abstract**: 揭示幻觉检测评估指标中的幻象问题。

#### Bias after Prompting: Persistent Discrimination in LLMs

- **Affiliation**: Apple
- **Venue**: EMNLP 2025
- **Abstract**: 即使通过 prompt 引导，LLM 中的歧视性偏见仍然持续存在。

### Trends

- Reasoning & test-time compute: major theme
- LLM safety & alignment: growing sub-community
- Agent evaluation: emerging focus area
- Machine translation & multilingual: sustained interest

---

## 7. KDD 2026

**Location**: Jeju Island, Korea | **Date**: Aug 9-13, 2026

### Key Papers (pre-acceptance / arXiv)

#### RankUp: High-rank Representations for Ad Ranking

- **中文标题**: RankUp: 广告排序的高秩表示
- **Affiliation**: Tencent
- **Venue**: KDD 2026
- **Abstract**: 提出高秩表示方法用于广告排序，在腾讯广告平台上验证效果。

#### RankElastor: Effective-Rank Dynamics for Recommendation

- **中文标题**: RankElastor: 推荐系统有效秩动力学
- **Venue**: KDD 2026
- **Abstract**: 研究推荐系统中有效秩的动态变化及其对性能的影响。

#### DIF: Denoising for Cold-Start (Kuaishou)

- **Affiliation**: Kuaishou
- **Venue**: KDD 2026
- **Abstract**: 冷启动场景下的去噪方法。

#### FAT: Rademacher CTR Scaling Law (Alibaba)

- **Affiliation**: Alibaba
- **Venue**: KDD 2026
- **Abstract**: 基于 Rademacher 复杂度的 CTR 缩放定律。

#### JourneyFormer (Airbnb)

- **Affiliation**: Airbnb
- **Venue**: KDD 2026
- **Abstract**: 旅行规划 Transformer 模型，用于 Airbnb 推荐。

#### TASR: Training-Free Adaptive Retrieval Stopping

- **Venue**: KDD 2026
- **Abstract**: 免训练的适应性检索停止策略。

---

## 8. RecSys 2025

**Location**: 2025 | **Date**: 2025

### Key Papers

#### Beyond Immediate Click: Engagement-Aware MoE-Enhanced Transformers (Amazon Prime Video)

- **Affiliation**: Amazon Prime Video
- **Venue**: RecSys 2025
- **Abstract**: MoE-增强 Transformer，考虑用户参与度信号的序列电影推荐。

#### LEAF: Lightweight, Efficient, Adaptive, Flexible Embedding

- **Affiliation**: -
- **Venue**: RecSys 2025
- **Abstract**: 高效嵌入方法，用于大规模推荐模型。

#### SUAN: Online CTR Scaling Methodology (Meituan)

- **Affiliation**: Meituan
- **Venue**: RecSys 2025
- **Abstract**: 统一的注意力块（UAB），统一序列和非序列特征的注意力计算，在美团的在线 CTR 系统中验证。

#### LONGER: Ultra-Long User Behavior Sequences (ByteDance)

- **Affiliation**: ByteDance
- **Venue**: RecSys 2025
- **Abstract**: 超长用户行为序列建模，在字节跳动推荐系统中部署。

#### Lasso: LLM-based User Simulator for Cross-Domain Recommendation

- **Affiliation**: -
- **Venue**: RecSys 2025
- **Abstract**: 基于 LLM 的用户模拟器，用于跨域推荐。

#### You Say Search, I Say Recs: Agentic Query Understanding at Spotify

- **Affiliation**: Spotify
- **Venue**: RecSys 2025
- **Abstract**: Agentic 方法理解搜索查询，桥接搜索与推荐。

---

## 9. SIGIR 2026

**Location**: Melbourne, Australia | **Date**: July 20-24, 2026

### Key Statistics

- **Total accepted papers**: 656 (across all tracks)
  - Full research papers: 234
  - Perspective papers: 12
  - Reproducibility papers: 28
  - Resource papers: 61
  - Short research papers: 151
  - Demo short papers: 24
  - Industry papers: 131
  - Low Resource Environment papers: 15
  - Doctoral Colloquium: 12

### Highlighted Papers

| Paper | Track | Affiliation |
|-------|-------|-----------|
| KuaiLive: Real-time Live Streaming Rec Dataset | Resource | Kuaishou |
| BioCLEAR: Biomedical Text Simplification | Resource | Multiple |
| WebMall: Multi-Shop Benchmark for Web Agents | Resource | Multiple |
| Post-hoc Provider Fairness Adaptation | Full | - |
| Unsupervised 2D Image-Based 3D Model Retrieval | Full | - |
| BEVNav: Bird's Eye View Navigation | Full | - |

### Trends for SIGIR 2026

- LLM for IR / RAG: dominant theme
- Generative recommendation: growing presence
- Web agents & tool use: emerging track
- Fairness, ethics in IR: continued emphasis

---

## 10. WWW 2026

**Location**: 2026

### Industry Track Highlights

#### NEZHA: Taobao Recommendation

- **Affiliation**: Alibaba (Taobao)
- **Venue**: WWW 2026 Industry
- **Abstract**: 淘宝推荐系统的大规模实践，覆盖 100M DAU，¥10B GMV 影响。

#### OneTrans: Unified Feature Interaction and Sequence Modeling

- **Affiliation**: ByteDance
- **Venue**: WWW 2026 Industry
- **Authors**: Zhaoqi Zhang (NTU), Haolei Pei, Jun Guo, Tianyu Wang, Yufei Feng, Hui Sun, Shaowei Liu, Aixin Sun
- **Abstract**: 统一特征交互与序列建模的工业 Transformer 推荐系统。

#### Not All Candidates Are Created Equal: Heterogeneity-Aware Pre-ranking

- **Affiliation**: ByteDance
- **Venue**: WWW 2026 Industry
- **Abstract**: 考虑异构性的预排序系统，在字节跳动推荐中应用。

#### From Modularity to Unity: Industrial-Scale Generative Recommendation

- **Affiliation**: JD.com
- **Venue**: WWW 2026 Industry
- **Abstract**: 京东的工业级生成式推荐系统。

#### Unbiased Multimodal Reranking for Short-Video Search

- **Affiliation**: Kuaishou
- **Venue**: WWW 2026 Industry
- **Abstract**: 短视频搜索的无偏多模态重排序。

#### Thinking Broad, Acting Fast: Latent Reasoning Distillation

- **Affiliation**: Alibaba International Digital Commerce
- **Venue**: WWW 2026 Industry
- **Abstract**: 潜在推理蒸馏用于电商搜索相关性。

#### Data-Driven Function Calling Improvements for Online Financial QA

- **Affiliation**: Tencent
- **Venue**: WWW 2026 Industry
- **Abstract**: 腾讯金融场景的 LLM function calling 优化。

---

## 11. CIKM 2025 / ACL 2026

### CIKM 2025

- **RankMixer**: ByteDance 的缩放排序模型 (CIKM 2025)
- **GPSD**: Alibaba 的 CTR 生成式预训练 (KDD 2025, also CIKM related)

### ACL 2026

- **BioNLP Workshop**: ACL 2026 workshop 接受论文
- **CodeTree**: Salesforce 的代码生成树搜索 (ACL 2025, influential)
- **Tree-of-Evolution**: NUS 的树结构代码指令进化 (ACL 2025)
- **Trend**: LLM evaluation, multilingual NLP, efficient fine-tuning

---

## 12. Frontier Model Reports

### Latest Releases (as of June 20, 2026)

| Model | Company | Date | Key Specs |
|-------|---------|------|-----------|
| Kimi K2.7 Code | Moonshot AI | Jun 12, 2026 | Code-focused, 1T MoE |
| Gemini Omni | Google DeepMind | May 2026 | Unified multimodal |
| Gemini 3.5 | Google DeepMind | May 2026 | Frontier intelligence with action |
| DiffusionGemma | Google DeepMind | June 2026 | 4x faster text generation |
| Gemma 4 12B | Google DeepMind | June 2026 | Encoder-free multimodal |
| GLM-5.2 | Zhipu AI (Z.ai) | June 2026 | 1M context, MIT license, open-source #1 on SWE |
| Qwen-RobotManip | Alibaba | June 2026 | VLA foundation model for robotics |

### Google DeepMind Recent Publications

| Paper | Date | Topic |
|-------|------|-------|
| From AGI to ASI | June 12, 2026 | AGI-to-ASI roadmap analysis |
| DiffusionGemma | June 2026 | 4x faster text generation via diffusion |
| D4RT (CVPR Best) | June 2026 | 4D dynamic scene reconstruction |
| Project Genie + Street View | May 2026 | Real-world simulation |
| Gemini Omni | May 2026 | Unified multimodal model |

### Key Industry News

- **ByteDance**: 115 papers accepted at ICLR 2026, focus on foundation models & multimodal
- **NVIDIA**: 50+ papers at CVPR 2026
- **Apple**: 14 papers at CVPR 2026, EMNLP 2025 papers on speculative decoding, bias
- **China AI Platform War**: Tencent WeChat AI Agent (1.4B MAU), Alibaba Qwen open platform strategy, ByteDance Doubao (345M MAU)

---

## 13. Key Themes & Synthesis

### Theme 1: Reasoning Models & Test-Time Compute (Cross-Venue)

- **NeurIPS 2025**: RLVR Critique 论文质疑 RL 是否真正提升了 LLM 的推理能力
- **ICLR 2026**: SPIRAL (self-play), CDE (curiosity-driven exploration)
- **EMNLP 2025**: S1 - simple test-time scaling
- **Key Insight**: 推理能力是 2025-2026 年最热门的跨会议主题。从 RLVR 到 self-play 到 test-time compute scaling，研究社区正在积极探索如何提升 LLM 的推理能力，但同时也出现了批判性反思。

### Theme 2: Gated Attention & Attention Mechanism Innovation

- **NeurIPS 2025 Best Paper**: Gated Attention (Alibaba)
- **ICLR 2026 Outstanding**: Transformers Succinctness
- **Trend**: 注意力机制的创新从架构层面展开。门控注意力消除 attention sink，Titans 架构引入全新记忆机制，SSM (Mamba-3) 在 ICLR 2026 作为 inference-first 范式获得 Outstanding。

### Theme 3: CTR Scaling Laws — 成熟研究领域

- **KDD 2026**: FAT (Rademacher), RankElastor
- **ICML 2026**: CTR-RL
- **RecSys 2025**: SUAN (Meituan), LONGER (ByteDance)
- **Trend**: CTR 缩放定律已经成为工业推荐系统的成熟研究领域。Alibaba (EST, FAT)、ByteDance (TokenMixer-Large, MixFormer)、Meta (Kunlun, LLaTTE) 持续贡献。

### Theme 4: Generative Recommendation — 从理论到工业部署

- **WWW 2026 Industry**: JD.com industrial-scale generative rec
- **SIGIR 2026**: Growing presence
- **Trend**: 生成式推荐从学术概念转向工业部署。多家公司（JD.com, Kuaishou, Meta）在生产环境中验证了生成式推荐的效果。

### Theme 5: Agent Systems Explosion

- **ICML 2026**: ~465 agent papers
- **ICLR 2026**: AgentFlow, MEM1, In-The-Flow
- **WWW 2026**: Web agents, LLM agents for various domains
- **Trend**: Agent 系统在所有会议中全面爆发。ICML 2026 接收了约 465 篇 agent 相关论文，占总接收量显著比例。

### Theme 6: 4D Vision & 3D Generation

- **CVPR 2026 Best**: D4RT (Google DeepMind) — 4D scene reconstruction
- **CVPR 2026 Student Best**: Native compact structured latents for 3D generation
- **Trend**: 计算机视觉从 2D/3D 向 4D（动态 3D）演进。D4RT 和 SAM 3D 代表了这一趋势。

### Theme 7: Multi-Agent Society & Foundation Protocol

- **ICLR 2026**: Foundation Protocol agentic society coordination (Tencent/HKUST/UIUC)
- **NeurIPS 2025**: Multi-Agent Collaboration via Evolving Orchestration
- **Trend**: Agent 从单体向多智能体社会演化。Foundation Protocol 提出了 Agentic Society 协调协议，展示了这个方向的早期探索。

### Theme 8: Frontier Models Converging on MoE + Hybrid + RLVR

- 所有主要模型系列（DeepSeek V4, GPT-5.5, Claude 4.x, Gemini 3.5, Qwen3.x）全部采用 MoE 架构
- **Hybrid Mamba-Transformer**: Nemotron 3 Ultra 等采用混合架构
- **RLVR**: 推理模型驱动，几乎所有基金会模型都包含 reasoning 能力
- **长上下文**: 1M context 成为旗舰标配（Gemini 3.1 Pro, DeepSeek V4, GLM-5.2）

---

## Appendix: Venue Statistics Summary

| Venue | Year | Submissions | Accepted | Acceptance Rate |
|-------|------|------------|----------|-----------------|
| AAAI | 2026 | 23,680 | 4,167 | 17.6% |
| CVPR | 2026 | 16,092 | 4,090 | 25.4% |
| ICML | 2026 | ~28,000 | 6,500+ | ~23% |
| ICLR | 2026 | ~12,000 | 4,361-5,355 | ~36-45% |
| NeurIPS | 2025 | ~20,000 | 5,276 | 25.4% |
| EMNLP | 2025 | 8,174 | 1,811 (Main) | 22.2% |
| SIGIR | 2026 | - | 656 (all tracks) | - |

## Appendix: Key arXiv Papers (June 19-20, 2026)

| Paper | Title | Category | Date |
|-------|-------|----------|------|
| 2606.20544 | Toward Calibrated Mixture-of-Experts Under Distribution Shift | cs.AI / ICML 2026 | Jun 19 |
| 2606.20264 | Confidence-Aware Assessment of Student-Drawn Scientific Models | cs.AI | Jun 19 |
| 2606.20245 | Navigating Unreliable Knowledge: Explicit Knowledge Conflict Resolution | cs.AI | Jun 19 |
| 2606.20227 | QMFOL: Benchmarking LLM Reasoning via Quantifiable Monadic FOL | cs.AI | Jun 19 |
| Various | AI Index Report 2026 (9th edition) | cs.AI | Jun 17 |
| 2606.19333 | Diffusion-Proof: Recipe for Formal Theorem Proving | cs.LG | Jun 18 |
| 2606.18803 | ProfiLLM: Utility-Aligned Agentic Profiling for Ride-Hailing (DiDi) | cs.AI | Jun 17 |
| Various | FAPO: Fully Autonomous Prompt Optimization | cs.CL | Jun 20 |
