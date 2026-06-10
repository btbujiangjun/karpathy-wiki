---
title: "会议摘要: 2026年AI/ML顶级会议论文全景"
title-en: "Conference Digest: Panorama of Top AI/ML Conference Papers"
type: synthesis
created: 2026-06-10
updated: 2026-06-10
sources: [arxiv.org, icml.cc, neurips.cc, iclr.cc, aaai.org, cvpr.thecvf.com, 2026.aclweb.org, kdd2026.kdd.org, sigir2026.org, www2026.thewebconf.org, recsys.acm.org]
tags: [conference-digest, 2026, icml, neurips, iclr, aaai, cvpr, acl, kdd, sigir, www, recsys, emnlp, arxiv]
---

# 会议摘要: 2026年AI/ML顶级会议论文全景

> 涵盖2025-2026年主要AI/ML会议的最新论文、研究趋势与关键突破。
> 结构化按会议/方向分类，包含详细描述与实验数据。

---

## 目录

1. [ICML 2026 — 国际机器学习大会](#1-icml-2026)
2. [NeurIPS 2025 — 神经信息处理系统大会](#2-neurips-2025)
3. [ICLR 2026 — 国际学习表征大会](#3-iclr-2026)
4. [AAAI 2026 — 人工智能促进会年会](#4-aaai-2026)
5. [CVPR 2026 — 计算机视觉与模式识别大会](#5-cvpr-2026)
6. [ACL / EACL 2026 — 计算语言学协会](#6-acl--eacl-2026)
7. [EMNLP 2025 — 自然语言处理实证方法](#7-emnlp-2025)
8. [KDD 2026 — 知识发现与数据挖掘](#8-kdd-2026)
9. [SIGIR 2026 — 信息检索研发](#9-sigir-2026)
10. [WWW 2026 — ACM Web大会](#10-www-2026)
11. [RecSys 2025 — 推荐系统大会](#11-recsys-2025)
12. [CTR预测与广告系统 — 工业前沿](#12-ctr预测与广告系统)
13. [生成式模型与扩散模型](#13-生成式模型与扩散模型)
14. [Agent系统与多智能体](#14-agent系统与多智能体)
15. [游戏AI与代码执行](#15-游戏ai与代码执行)
16. [序列建模与状态空间模型](#16-序列建模与状态空间模型)
17. [LLM推理、对齐与效率](#17-llm推理对齐与效率)
18. [推荐系统新范式](#18-推荐系统新范式)

---

## 1. ICML 2026

**第43届国际机器学习大会 (ICML 2026)**
- **地点**: 韩国首尔, COEX
- **日期**: 2026年7月6-11日
- **投稿/接收**: 23,918 投稿 → 6,352 接收 (26.6%)
- **Spotlight**: 536 (2.2%)
- **链接**: [icml.cc](https://icml.cc/)

### 1.1 Best Paper / Oral 亮点

#### Learning Unmasking Policies for Diffusion Language Models
| | |
|---|---|
| **作者** | Metod Jazbec, Theo X. Olausson, Louis Béthune, Pierre Ablin, Michael Kirchhof, Joao Monteiro, Victor Guilherme Turrisi da Costa, Jason Ramapuram, Marco Cuturi |
| **机构** | Apple, Google DeepMind |
| **类型** | Oral |
| **链接** | ICML 2026 Oral |

**背景**: Diffusion Language Models (dLLMs) 在多项任务上已达AR模型的水平,但采样策略(选择哪些token在每一步去掩码)仍依赖人工启发式如置信度阈值。

**核心创新**: 将掩码扩散采样形式化为马尔可夫决策过程(MDP),dLLM作为环境,训练一个轻量级单层Transformer策略来学习去掩码决策。在full-diffusion设置下超越现有SOTA启发式方法。

**方法**: 基于强化学习训练采样策略,提出轻量级策略网络(单层Transformer),将dLLM token置信度映射为去掩码决策。在semi-autoregressive (block)生成模式下匹配SOTA启发式表现,在纯扩散模式下全面超越。

#### Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis (Self-Flow)
| | |
|---|---|
| **作者** | Hila Chefer, Patrick Esser, Dominik Lorenz, Dustin Podell, Vikash Raja, Vinh Tong, Antonio Torralba, Robin Rombach |
| **机构** | MIT, Stability AI, Runway |
| **类型** | Spotlight/Poster |

**背景**: 多模态生成中,有监督flow matching依赖大量标注数据。

**核心创新**: 提出Self-Flow,自监督flow matching范式,在生成框架内集成表征学习,无需配对数据即可学习多模态联合分布。

### 1.2 Agent-Related Papers (465篇)

ICML 2026专门整理了Agent相关论文达465篇,涵盖:

- **Benchmarks & Evaluation** (99篇): 长期任务、GUI/Web、编码、科学、金融、医疗等场景的agent评估
- **Multi-Agent Systems & MARL** (93篇): 多智能体协作、社会模拟、communication
- **Tool Use, Training & RL** (58篇): 从prompt-based转向trainable agents,包括tool-use RL、GRPO、轨迹SFT、自进化
- **Safety, Security & Governance** (51篇): 安全对齐、jailbreak防御
- **Theory, Behavior & Interpretability** (39篇): agent行为理解与可解释性

来源: [GitHub: jiaxianyan/icml-2026-agent-papers](https://github.com/jiaxianyan/icml-2026-agent-papers)

### 1.3 其他值得关注的论文

| 论文 | 作者/机构 | 方向 |
|------|----------|------|
| SVRG and Beyond via Posterior Correction | Nico Daheim (TU Darmstadt) et al. | 优化 |
| Fair Classification with Efficient Fairness-Accuracy Trade-off | Maaya Sakata (U Tokyo / RIKEN) | 公平性 |
| A Decision-Theoretic View of Test-Time Training | Tomoya Wakayama (RIKEN) | Test-Time Training |
| Sample Efficiency of Curriculum Post-Training for Transformer Reasoning | Dake Bu (CityU / RIKEN) | 推理 / Curriculum |
| Revisiting Regularized Policy Optimization for Two-Player Games | Kazuki Ota (U Tokyo / RIKEN) | 博弈 / RL |
| Sign Lock-In: Randomly Initialized Weight Signs Persist | RIKEN AIP | 深度学习理论 |
| Refining Dual Spectral Sparsity in Transformed Tensor Singular Values | Andong Wang (RIKEN) | 张量分析 |

---

## 2. NeurIPS 2025

**第39届NeurIPS**
- **地点**: 美国圣地亚哥
- **日期**: 2025年12月2-7日
- **投稿/接收**: ~21,575 投稿 → 5,275 接收 (24.5%)
- **Oral**: 77 (1.39%), **Spotlight**: 683 (12.36%)
- **最佳论文奖**: 4篇最佳论文 + 3篇Runner-up

### 2.1 Best Papers — 最佳论文

#### 1️⃣ Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
| | |
|---|---|
| **作者** | Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin |
| **机构** | Qwen Team (Alibaba) |
| **论文** | [arXiv:2505.06708](https://arxiv.org/abs/2505.06708) |
| **代码** | [github.com/qiuzh20/gated_attention](https://github.com/qiuzh20/gated_attention) |

**背景**: Transformer attention机制在长上下文和稳定性方面存在"attention sink"问题。

**核心创新**: 在缩放点积注意力(SDPA)之后插入逐头sigmoid门控。在1.7B和15B MoE模型上(训练至3.5T tokens)验证:门控显著提升稳定性和长上下文性能,消除attention sink。这是对标准Transformer最小的改动之一却带来显著收益,预计将被广泛采用。委员会评价:简单改动,广泛影响。

**实验结果**: 在15B MoE和1.7B dense模型上,门控注意力在多项benchmark上持续超越标准注意力基线。

#### 2️⃣ 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
| | |
|---|---|
| **作者** | Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzciński, Benjamin Eysenbach |
| **机构** | Princeton, University of Warsaw |
| **链接** | [OpenReview](https://openreview.net/forum?id=s0JVsx3bx1) |

**核心创新**: 首次证明在自监督RL中扩展深度(至1000层)可以带来定性不同的新能力——到达命令目标,超越之前仅增加宽度的方式。在模拟 locomotion 和 manipulation 任务上,超越其他目标条件基线2×-50×。

#### 3️⃣ Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training
| | |
|---|---|
| **作者** | Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mézard |
| **机构** | ENS Paris |
| **论文** | [arXiv:2505.17638](https://arxiv.org/abs/2505.17638) |

**核心创新**: 理论分析和实证研究分数匹配扩散模型的训练动力学。识别两个不同时间尺度:τgen(生成有效样本)和τmem(开始记忆)。解释扩散模型为何在标准训练设置下不记忆训练数据——隐式动力学正则化。

#### 4️⃣ Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
| | |
|---|---|
| **作者** | Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi |
| **机构** | University of Washington, Allen AI, CMU |
| **论文** | [arXiv:2510.22954](https://arxiv.org/abs/2510.22954) |

**核心创新**: 发布大规模开放prompt数据集,发现LLM倾向于产生"人工蜂群思维"(artificial hivemind)——生成惊人的相似答案。系统衡量多样性坍塌现象。*(Datasets & Benchmarks Track Best Paper)*

### 2.2 Best Paper Runners-Up

#### Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
| | |
|---|---|
| **作者** | Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang |
| **机构** | Tsinghua University |
| **论文** | [arXiv:2504.13837](https://arxiv.org/abs/2504.13837) |

**核心发现**: 系统研究RL(特别是RLVR/GRPO)是否能超越基础模型激发推理能力。观察发现当前训练并没有完全开发模型的推理能力——模型生成更长的推理轨迹但推理深度并未同比提升。

#### Superposition Yields Robust Neural Scaling
| | |
|---|---|
| **链接** | NeurIPS 2025 |

**核心创新**: 理论证明超位(superposition)如何产生鲁棒的神经缩放定律,解释为何过参数化模型在分布偏移下仍表现良好。

#### Optimal Mistake Bounds for Transductive Online Learning
| | |
|---|---|
| **链接** | NeurIPS 2025 |

**核心创新**: 解决了一个30年之久的开放问题:证明对于具有Littlestone维度d的假设类,最优错误界为Θ(√d)。给出未标注数据在在线学习中如何提供精确的二次优势。

### 2.3 NeurIPS 2025 关键趋势

1. **LLM门控注意力** (Gated Attention) 获得最高认可——简单而impactful
2. **扩散模型理论** (不记忆机制) 获最佳论文,推动理论理解
3. **深度自监督RL** 首次证明深度scale可以带来qualitative变化
4. **AI评估多样性** ("蜂群思维"现象) 获DB Track最佳论文,反映领域对评估质量的关注
5. **RL for LLM Reasoning** 热度极高但存在局限——runner-up论文指出RLVR可能并未真正激发深层推理

来源: [NeurIPS Blog](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)

---

## 3. ICLR 2026

**第14届国际学习表征大会 (ICLR 2026)**
- **地点**: 巴西里约热内卢
- **日期**: 2026年4月23-27日
- **投稿/接收**: 19,525 投稿 → 5,355 接收 (27.4%)
- **Oral**: 225篇 (1.13%)
- **杰出论文奖**: 2篇Outstanding + 1篇Honorable Mention

### 3.1 Outstanding Papers

#### Transformers are Inherently Succinct
| | |
|---|---|
| **作者** | Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin |
| **机构** | ETH Zurich |
| **类型** | Outstanding Paper |

**核心创新**: 理论工作提出新视角解释Transformer架构的优势——相比于RNN等替代模型,Transformer可以更简洁(succinct)地编码概念。可能激发更多关于Transformer和其他架构概念表征简洁性的理论和实证研究。

#### Multi-Turn Language Model Evaluation
*(论文标题未完整公开)*

**核心创新**: 设计了可扩展的多轮评估方法。发现大多数LLM训练数据为单轮完成或单轮对话,但部署中本质上是多轮交互。测量了在指令不明确的多轮交互中LLM能力和可靠性的显著下降。展示了出色的实验设计和方法论。委员会认为结论和方法对最先进的模型依然相关。

#### Honorable Mention: The Polar Express — Optimal Matrix Sign Methods for Muon Algorithm
| | |
|---|---|
| **作者** | Noah Amsel, David Persson, Christopher Musco, Robert M. Gower |

**核心创新**: 使用逼近论设计极分解(Polar Decomposition)的最优多项式逼近,应用于流行的Muon优化器。特别关注GPU和低精度算术环境。虽然实证提升有时有限,但改进最流行优化器的原则性方法受到认可。

### 3.2 Oral Papers 亮点

| 论文 | 作者/机构 | 方向 |
|------|----------|------|
| **Common Corpus** — The Largest Collection of Ethical Data for LLM Pre-Training | 多机构 | 数据 / LLM预训练 |
| **Q-RAG** — Long Context Multi-Step Retrieval via Value-Based Embedder Training | - | 检索 / RAG |
| **FIRE** — Frobenius-Isometry Reinitialization for Stability-Plasticity Tradeoff | - | 持续学习 |
| **Why DPO is a Misspecified Estimator and How to Fix** | - | 偏好优化 / DPO理论 |
| **SafeDPO** — Simple Approach to DPO with Enhanced Safety | - | 安全性 / RLHF |
| **MedAgentGym** — Scalable Agentic Training for Biomedical Code Reasoning | - | Agent / 医学 |
| **WebDevJudge** — Evaluating (M)LLMs as Critiques for Web Development | - | LLM-as-Judge |
| **Enhancing Generative Auto-bidding with Offline Reward Evaluation** | - | 竞价 / RL |

### 3.3 其他重要论文

| 论文 | 方向 | 关键点 |
|------|------|--------|
| **Mamba-3** — Improved Sequence Modeling using State Space Principles | SSM | 详见 §16 |
| **Mixture-of-Experts Can Surpass Dense LLMs Under Equal Resource** | MoE | 在严格等资源下MoE超越Dense |
| **RAIN-Merging** — Gradient-Free Method for Reasoning Models | 模型合并 | 保持思考格式增强指令遵循 |
| **Verifying Chain-of-Thought Reasoning via its Computational Graph** | 推理验证 | 计算图级CoT验证 |
| **TileLang** — Bridge Programmability and Performance in Neural Kernels | 系统 | 高性能kernel编译 |
| **Mastering Sparse CUDA Generation through Pretrained Models and Deep RL** | 系统 | Deep RL生成CUDA |
| **In-The-Flow Agentic System Optimization** | Agent | 规划与工具使用的系统优化 |
| **Overthinking Reduction with Decoupled Rewards and Curriculum Data** | 推理 | 减少过度思考 |
| **GLASS Flows** — Efficient Inference for Reward Alignment of Flow/Diffusion | 生成模型 / 对齐 | Flow模型奖励对齐 |

### 3.4 ICLR 2026 关键数据

- **审稿危机**: 约45%的身份泄露,21%的审稿完全由AI生成——这是学术界的重大问题
- **投稿增长**: 19,525篇,同比增长67%
- **关键趋势**: 多模态AI、Agent系统、RAG与推理融合、对齐与安全

---

## 4. AAAI 2026

**第40届AAAI人工智能大会 (AAAI 2026)**
- **地点**: 新加坡
- **日期**: 2026年1月20-27日
- **投稿/接收**: ~29,000 投稿 → ~23,000 通过合规审查 → 约23%接收率
- **规模**: 超过75,000位作者,来自中国的贡献约20,000篇

### 4.1 亮点论文

| 方向 | 论文 | 要点 |
|------|------|------|
| **NLP** | LogicCat — Chain-of-Thought Text-to-SQL Benchmark for Complex Reasoning | CoT推理的Text-to-SQL基准 |
| **ML** | FedGRPO — Privately Optimizing Foundation Models with Group-Relative Rewards | 联邦GRPO优化基础模型 |
| **CV** | StreamingTalker — Audio-driven 3D Facial Animation with Autoregressive Diffusion | 音频驱动3D面部动画 |
| **CV** | High-Fidelity Visual Text Rendering via Glyph-Aware Multimodal Diffusion | 字形感知多模态文字渲染 |
| **CV** | Contextually Adaptive Token Pruning for Efficient Multimodal ICL | Token剪枝 / 多模态 |
| **GNN** | Attribute-guided Dynamic Prompt Learning for Graph Neural Networks | GNN提示学习 |
| **GNN** | MUG — Meta-path-aware Universal Heterogeneous Graph Pre-Training | 异构图预训练 |
| **ML** | MLP Knowledge Distillation with Efficient Trade-offs | 知识蒸馏 |
| **ML** | Targeted Data Poisoning of Linear Classifiers | 数据投毒攻击 |

### 4.2 AAAI 2026 关键趋势

1. **投稿量暴增**: 从AAAI-25的~12,000篇增至~29,000篇(翻倍)
2. **中国学术力量**: 约20,000篇投稿来自中国,占总投稿的约69%
3. **三大领域**: CV、ML、NLP为投稿量前三
4. **审稿委员会扩充**: 扩至28,000+人,是前一年的3倍

---

## 5. CVPR 2026

**第43届IEEE/CVF计算机视觉与模式识别大会**
- **地点**: 美国丹佛
- **日期**: 2026年6月5-7日
- **投稿/接收**: 16,092 投稿 → 4,089 接收 (25.4%)
- **Oral**: 141篇

### 5.1 最佳论文奖

#### Best Paper: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
| | |
|---|---|
| **作者** | Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi |
| **机构** | Google DeepMind, UCL, University of Oxford |
| **类型** | Best Paper 🏆 |

**核心创新**: D4RT是一种统一的Transformer架构,可以从视频中重建4D动态场景的几何和运动。模型估计深度、时空对应和完整相机参数,允许独立高效地探测任何点在空间和时间中的3D位置。将传统计算密集型过程简化为轻量级、高可扩展的方法,实现非常高效的训练和推理。

#### Best Student Paper: Native and Compact Structured Latents for 3D Generation (O-Voxel)
| | |
|---|---|
| **作者** | Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang |
| **机构** | Tsinghua University, Microsoft Research, USTC, Microsoft AI |
| **类型** | Best Student Paper 🏆 |

**核心创新**: O-Voxel是一种新型3D表示方法,能准确捕捉复杂形状和表面属性。生成资产的几何和质量远超现有模型,在用户偏好对比中取得显著优势。

### 5.2 关键趋势 (CVPR 2026)

1. **生成式&多模态论文占比翻倍**: 从约14%增至22%
2. **具身AI(Embodied AI)** 占比几乎翻倍
3. **视觉-语言和多模态LLM** 增长最大,从4.9%增至10.6%
4. **五大热门方向**: 图像视频生成、视觉语言推理、多模态学习、3D视觉、医学视觉
5. **接收量增长42%**: 从去年的2,878篇增至4,089篇

### 5.3 其他Oral/亮点论文

| 论文 | 方向 | 机构 |
|------|------|------|
| **SAM 3** — Segment Anything with Concepts | 分割/检测 | Meta, FAIR |
| **Molmo2** — Open Weights and Data for VLMs with Video Understanding | VLM | Allen AI, 多机构 |
| **SenseSearch** — High-Resolution Agentic Search-Reasoning via RL | VLM / Agent | 多机构 |
| **EcoSplat** — Feed-forward 3D Gaussian Splatting | 3D重建 | KAIST |
| **AToken** — A Unified Tokenizer for Vision | 视觉Tokenizer | - |
| **Weaver** — Decoupled Training for Interleaved Multi-modal Generation | 多模态生成 | - |
| **Visual Autoregressive Modeling** | 视觉生成 | - |
| **4D-RGPT** — Region-level 4D Understanding via Perceptual Distillation | 4D理解 | NVIDIA |
| **B³-Seg** — Camera-Free, Training-Free 3DGS Segmentation | 3D分割 | - |
| **OccuFly** — 3D Vision Benchmark for Semantic Scene Completion | 自动驾驶 | - |

---

## 6. ACL / EACL 2026

**第64届ACL年会**
- **地点**: 美国圣地亚哥
- **日期**: 2026年7月2-7日
- **主题**: 可解释NLP

**EACL 2026**
- **地点**: 摩洛哥拉巴特
- **日期**: 2026年3月
- **投稿/接收**: 2,200 → 445 Main (20.2%) + 355 Findings (16.1%)

### 6.1 关键论文

#### COMPACT — Building Compliance Paralegals via Clause Graph Reasoning over Contracts
| | |
|---|---|
| **作者** | Ayush Singh, Dishank Aggarwal, Pranav Bhagat, Ainulla Khan, Sameer Malik, Amar Prakash Azad |
| **机构** | - |
| **链接** | [ACL Anthology](https://aclanthology.org/2026.eacl-long.377/) |

**核心创新**: 提出COMPACT框架,通过结构化子句图建模跨子句依赖关系。引入ACE基准——包含633份真实合同、4,700个合规场景。多子句推理对SOTA模型是根本性挑战(34-57%基础准确率),在ACE上训练可提升22-43个百分点。

#### ACPS — Debiasing LLMs via Adaptive Causal Prompting with Sketch-of-Thought
| | |
|---|---|
| **作者** | Bowen Li et al. |
| **机构** | - |
| **链接** | [ACL Anthology](https://aclanthology.org/2026.findings-eacl.234/) |

**创新**: 利用结构因果模型推断查询对答案的因果效应,用简洁的Sketch-of-Thought替代冗长的CoT。在多种推理benchmark和LLM上一致超越现有prompt方法。

#### GRAFF — GRaph-Augmented Fine-grained Fusion for LLMs
| | |
|---|---|
| **链接** | [ACL Anthology](https://aclanthology.org/2026.findings-eacl.293.pdf) |

**创新**: 通过轻量结构适配器将细粒度节点级结构信息融入LLM。引入双通道图输入机制,GAT模块集成在LLM decoder中间层。在四个数据集上平均超越基线10.14%。

---

## 7. EMNLP 2025

**第30届EMNLP**
- **地点**: 中国苏州
- **日期**: 2025年11月
- **投稿/接收**: 8,172 → 1,811 Main (22.16%) + 1,417 Findings (17.34%)

### 7.1 最佳论文与Outstanding Papers

#### Best Paper: Infini-gram mini — Exact n-gram Search at Internet Scale with FM-Index
| | |
|---|---|
| **作者** | Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi |
| **机构** | University of Washington, Allen AI |

**核心创新**: 使用FM-index实现互联网规模的精确n-gram搜索,极大加速了基于统计的语言模型分析。

#### Outstanding Papers 精选

1. **S1: Simple Test-time Scaling** — Niklas Muennighoff et al. (Stanford): 最简单的test-time scaling方法,通过40次采样+预算强制,在推理任务上达到GPT-4o级别。

2. **LingGym**: How Far Are LLMs from Thinking Like Field Linguists? — UChicago: 评估LLM的语言学家能力。

3. **Mind the Value-Action Gap** — Hua Shen et al. (U Maryland): 发现LLM的陈述价值观与实际行为存在差距(价值-行动差距),链接到心理学中信念与行为分离现象。

4. **Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps** — 通过遗忘方法测试CoT的忠实度。

5. **MiCRo** — Mixture Modeling and Context-aware Routing for Personalized Preference Learning: 混合模型+上下文感知路由进行个性化偏好学习。

6. **CodeArena** — Evaluating LLMs on Human Preference for Coding: 40类别、44种编程语言的全面编码评估。

7. **Causal Interventions Reveal Shared Structure Across English Filler-Gap Constructions** — Stanford: 用因果可解释性方法研究LLM中的句法知识。

8. **ZoomEye** — Tree-based Image Exploration for Multimodal LLMs: 免训练、模型无关的树搜索算法用于视觉推理。

### 7.2 EMNLP 2025 关键趋势

1. **Agent系统**: Agentic systems成为核心主题之一
2. **深度可解释性** (Deep Transparency): 从得出解释方法转向理解模型内部机制
3. **推理与对齐**: CoT忠实度、RL for Reasoning广泛关注
4. **不确定性量化**: 第二届不确定性量化workshop
5. **模型训练**: 灾难性遗忘、选择性剪枝、高效微调

---

## 8. KDD 2026

**第32届ACM SIGKDD知识发现与数据挖掘大会**
- **地点**: 韩国济州岛, ICC Jeju
- **日期**: 2026年8月9-13日
- **主讲嘉宾**: Jeff Dean (Google), Jingren Zhou (Alibaba)

### 8.1 已公开论文

#### EvoDS — Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management
| | |
|---|---|
| **作者** | - |
| **机构** | - |
| **链接** | [arXiv:2606.03841](https://arxiv.org/abs/2606.03841) |

**核心创新**: 自进化数据科学Agent,具备自主技能获取和上下文管理能力。在四个数据科学benchmark上,相比最强开源基线DataInterpreterB,平均性能绝对提升9.5%,相对提升28.9%。

#### GraphSeek — Next-Generation Graph Analytics with LLMs
| | |
|---|---|
| **链接** | [arXiv:2602.11052](https://arxiv.org/abs/2602.11052) |

**创新**: LLM驱动的下一代图分析框架,结合大语言模型的推理能力与图数据处理。

### 8.2 2025年最有影响力KDD论文(来自Paper Digest)

| 排名 | 论文 | 领域 |
|------|------|------|
| 1 | Benchmarking and Defending Against Indirect Prompt Injection Attacks on LLMs | LLM安全 |
| 2 | DUET: Dual Clustering Enhanced Multivariate Time Series Forecasting | 时序预测 |
| 3 | LLMLight: Large Language Models As Traffic Signal Control Agents | LLM Agent |
| - | Taming Recommendation Bias with Causal Intervention on Evolving Personal Popularity | 推荐/去偏 |
| - | When Heterophily Meets Heterogeneity: A Large-Scale Graph Benchmark | 图学习 |

---

## 9. SIGIR 2026

**第49届ACM SIGIR信息检索研发大会**
- **地点**: 澳大利亚墨尔本
- **日期**: 2026年7月20-24日

### 9.1 关键论文

#### Rank-R1: Enhancing Reasoning in LLM-based Document Rerankers via Reinforcement Learning
| | |
|---|---|
| **作者** | Shengyao Zhuang, Xueguang Ma, Zheng Yao, Shuai Wang, Bevan Koopman, Jimmy Lin, Guido Zuccon |
| **机构** | University of Waterloo, University of Queensland, CSIRO |
| **链接** | [PDF](https://cs.uwaterloo.ca/~jimmylin/publications/Zhuang_etal_SIGIR2026_RankR1.pdf) |

**核心创新**: 将R1推理增强应用于文档重排序。通过强化学习训练LLM重排序器,使其在排序过程中产生推理链,显著提升重排序质量。

#### LTRR: Learning To Rank Retrievers for LLMs
| | |
|---|---|
| **机构** | - |
| **链接** | [arXiv:2506.13743](https://arxiv.org/abs/2506.13743) |

**创新**: 学习为LLM排序检索器的query routing框架。使用utility感知的retriever选择,基于AC效用度量和pairwise learning-to-rank,超越标准单检索器RAG系统。

#### Attribution-Guided Query Rewriting
| | |
|---|---|
| **链接** | [arXiv:2602.11841](https://arxiv.org/abs/2602.11841) |

**创新**: 利用神经检索器的token级归因分数指导LLM进行查询改写。在SPLADE和TCT-ColBERT上,nDCG、MAP、Precision一致提升。

#### LLM-Oriented Information Retrieval: A Denoising-First Perspective
| | |
|---|---|
| **链接** | [arXiv:2605.00505](https://arxiv.org/abs/2605.00505) |

**创新**: 提出"去噪优先"视角,重新思考面向LLM的信息检索设计原则。

#### SA²CRQ — Anchored Curriculum with Sequential Adaptive Quantization for Generative Retrieval
| | |
|---|---|
| **机构** | 工业搜索引擎 |
| **链接** | [arXiv:2602.23978](https://arxiv.org/abs/2602.23978) |

**创新**: 顺序自适应残差量化框架,动态分配码本长度:头部项用更长、更具区分性的ID,尾部项用更短、更具泛化性的ID。在大规模工业搜索系统中一致提升,冷启动场景提升尤为显著。

#### Revisiting BM25 Feedback Models using HyDE
| | |
|---|---|
| **作者** | Nour Jedidi, Jimmy Lin |
| **机构** | University of Waterloo |
| **链接** | [PDF](https://cs.uwaterloo.ca/~jimmylin/publications/Jedidi_Lin_SIGIR2026.pdf) |

**创新**: 在HyDE增强检索的背景下重新审视经典的BM25反馈模型,发现BM25反馈模型和HyDE互补:简单交换top-ranked文档即可共赢。

---

## 10. WWW 2026

**ACM Web大会 2026**
- **地点**: 阿联酋迪拜
- **原定日期**: 2026年4月13-17日 → **重排**: 2026年6月29日-7月3日
- **论文提交截止**: 2025年10月7日

### 10.1 会议结构

| 轨道 | 说明 |
|------|------|
| Research Tracks | 8页内容+4页附录 |
| Short Papers | 短文 |
| Industry Track | 工业实践 |
| Web4Good Special Track | AI向善 |
| Demos | 系统演示 |

### 10.2 投稿主题

涵盖Web的所有方面:计算社会学、经济学、政治学、信息检索、推荐系统、Web挖掘、语义Web、社交网络分析、隐私与安全、AI for Web等。

---

## 11. RecSys 2025

**第19届ACM推荐系统大会**
- **地点**: 捷克布拉格
- **日期**: 2025年9月22-26日
- **投稿/接收**: 260 → 49篇长文 (18.85%), 161 → 33篇短文 (20.50%)

### 11.1 最佳论文

#### Best Full Paper: You Don't Bring Me Flowers — Mitigating Unwanted Recommendations Through Conformal Risk Control
| **作者** | Giovanni De Toni, Erasmo Purificato, Emilia Gomez, Andrea Passerini, Bruno Lepri, Cristian Consonni |

**创新**: 使用共形风险控制(Conformal Risk Control)方法来缓解用户不想要的推荐。

#### Best Short Paper: Beyond Top-1 — Addressing Inconsistencies in Counterfactual Explanations for RecSys
| **作者** | Amir Reza Mohammadi, Andreas Peintner, Michael Müller, Eva Zangerle |

### 11.2 工业界亮点论文

| 论文 | 作者/机构 | 方向 |
|------|----------|------|
| **PinFM** — Foundation Model for User Activity Sequences at Billion-scale | Xiangyi Chen et al. (Pinterest) | 用户序列基础模型 |
| **GRACE** — Generative Recommendation via Journey-Aware Sparse Attention | Luyi Ma et al. (Walmart) | 生成式推荐 |
| **LLM-RecG** — Semantic Bias-Aware Framework for Zero-Shot Sequential Rec | UIUC | LLM增强序列推荐 |
| **Enhancing Sequential Rec with LLMs for Joint Video and Comment Rec** | Kuaishou + Renmin Univ | 多模态推荐 |
| **Not Just What, But When** — Irregular Intervals to LLM for Sequential Rec | 丰田 | 时间间隔建模 |
| **Test-Time Alignment with SSM for Tracking User Interest Shifts** | 多机构 | SSM / 序列推荐 |
| **Scaling Retrieval for Web-Scale Recommenders** | Yuchin Juan et al. | 大规模检索 |
| **Agentic Personalisation of Cross-Channel Marketing** | Sami Abboud et al. | Agent个性化 |

---

## 12. CTR预测与广告系统

> 2026年CTR预测领域正经历从传统DLRM/MLP架构向Transformer、LLM启发架构和生成式推荐的重大转变。

### 12.1 工业界前沿论文

#### CADET — Context-Conditioned Ads Decoder-Only Transformer (LinkedIn)
| | |
|---|---|
| **论文** | [arXiv:2602.11410](https://arxiv.org/abs/2602.11410) |

**核心创新**: LinkedIn部署的端到端Decoder-Only Transformer用于广告CTR预测。五大创新: (1) 上下文条件解码 + 多头预测; (2) 自门控注意力(self-gated attention); (3) 时间戳RoPE; (4) Session掩码策略; (5) 生产级工程优化。

**在线效果**: A/B测试中CTR提升11.04%,对比生产基线LiRank(DCNv2+序列编码器混合)。

#### EST — Efficiently Scalable Transformer (Alibaba Taobao)
| | |
|---|---|
| **论文** | [arXiv:2602.10811](https://arxiv.org/abs/2602.10811) |

**核心创新**: 高效可扩展Transformer架构,统一异构输入。提出轻量交叉注意力(LCA)和内容稀疏注意力(CSA)。

**在线效果**: 淘宝展示广告场景CTR +1.22%, RPM +3.27%; 购后场景CTR +2.01%, RPM +2.66%。清晰的幂律缩放趋势。

#### GRAB — Generative Ranking for Ads at Baidu
| | |
|---|---|
| **论文** | [arXiv:2602.01865](https://arxiv.org/abs/2602.01865) |

**核心创新**: 百度首页feed广告的端到端生成式CTR框架。提出Causal Action-aware Multi-channel Attention (CamA)。

**在线效果**: CTR +3.49%, CPM +3.05%。缩放分析显示表达能力随模型容量单调线性提升。

#### LoopCTR — Loop Scaling for CTR (Alibaba)
| | |
|---|---|
| **论文** | [arXiv:2604.19550](https://arxiv.org/abs/2604.19550) |

**核心创新**: 三明治架构(Entry→Loop→Exit)。循环块使用超连接残差+MoE,过程监督使多循环训练编码到共享参数中。实现train-multi-loop, infer-zero-loop。

**效果**: 零循环推理已超越所有基线(Amazon: 0.8728 AUC)。Oracle分析揭示0.02-0.04 AUC未开发空间。

#### DS-MLP — Dual-Stream MLP for CTR
| | |
|---|---|
| **论文** | [arXiv:2606.04944](https://arxiv.org/abs/2606.04944) |

**核心创新**: 知识蒸馏将显式特征交互能力整合到主MLP网络,并行MLP捕获隐式交互。尽管仅使用vanilla MLP结构,在三个广泛使用的benchmark上达到SOTA。

#### SparseCTR — Sparse Attention for Long-term Behaviors
| | |
|---|---|
| **论文** | [arXiv:2601.17836](https://arxiv.org/abs/2601.17836) |

**核心创新**: 个性化分块+三分支稀疏自注意力(全局兴趣+兴趣转移+短期兴趣)+复合相对时间编码。

**在线效果**: CTR +1.72%, CPM +1.41%, 推理延迟仅40ms。在三个数量级的FLOPs范围内保持性能提升。

#### GR4AD — Generative Recommendation for Advertising (Kuaishou)
| | |
|---|---|
| **论文** | [arXiv:2602.22732](https://arxiv.org/abs/2602.22732) |

**核心创新**: UA-SID统一广告语义ID + MGMR多粒度多分辨率量化 + LazyAR解码器 + RSPO排序引导RL。

**在线效果**: 广告收入提升4.2%,<100ms延迟,500+ QPS/L20,已全量部署在4亿+用户广告系统。

#### TokenMixer-Large (ByteDance)
| | |
|---|---|
| **论文** | [arXiv:2602.06563](https://arxiv.org/abs/2602.06563) |

**核心创新**: 混合-逆操作+层间残差+Sparse Per-token MoE。成功扩展到7B参数(在线)和15B(离线)。

**在线效果**: 电商订单+1.66%,人均GMV+2.98%;广告ADSS+2.0%;直播收入+1.4%。已部署在抖音多个场景。

#### HeMix (AMAP/Alibaba)
| | |
|---|---|
| **论文** | [arXiv:2602.09387](https://arxiv.org/abs/2602.09387) |

**创新**: Query-Mixed Interest Extraction + HeteroMixer块(多头token融合+异构交互+组对齐重建)。

**在线效果**: GMV+3.61%, PV_CTR+2.78%, UV_CVR+2.12%。

#### HyFormer (ByteDance Douyin Search)
| | |
|---|---|
| **论文** | [arXiv:2601.12681](https://arxiv.org/abs/2601.12681) |

**创新**: 统一混合Transformer,交替Query Decoding和Query Boosting。在30亿样本的抖音搜索系统上验证。

#### RankUp (Tencent WeChat)
| | |
|---|---|
| **论文** | [arXiv:2604.17878](https://arxiv.org/abs/2604.17878) |

**创新**: 缓解嵌入坍塌,提升潜在表示多样性。在线AUC提升,全量部署于微信视频号、朋友圈、公众号。

**在线效果**: GMV提升3.41%(视频号)、4.81%(朋友圈)、2.12%(公众号)。

#### S-GRec — Semantic-Aware Generative Recommendation (Tencent WeChat)
| | |
|---|---|
| **论文** | [arXiv:2602.10606](https://arxiv.org/abs/2602.10606) |

**创新**: 解耦在线轻量生成器 + 离线LLM语义评判器。A2PO锚定在业务奖励上,仅当与业务一致时注入语义优势。

**在线效果**: CTR +1.16%, GMV +1.19%, 不喜欢率-2.02%。

#### DAIAN — Deep Adaptive Intent-Aware Network
| | |
|---|---|
| **论文** | [arXiv:2602.13971](https://arxiv.org/abs/2602.13971) |

**创新**: 触发诱导推荐(TIR)场景的动态意图感知。CTR +1.99%, 推荐多样性+1.73%, 成交额+2.37%。

---

## 13. 生成式模型与扩散模型

#### FLARE — Diffusion for Hybrid Language Model
| | |
|---|---|
| **作者** | Yuchen Zhu, Jing Shi, Chongjian Ge, Hao Tan, Yiran Xu, Wanrong Zhu, Jason Kuen, Koustava Goswami, Rajiv Jain, Yongxin Chen, Molei Tao, Jiuxiang Gu |
| **机构** | Adobe Research, Georgia Tech |
| **论文** | [arXiv:2606.01774](https://arxiv.org/abs/2606.01774) |

**核心创新**: 系统性的AR到dLLM转换配方。三大贡献: (1) Transfer诊断——识别传输数据质量和分布匹配为保持AR能力的关键因素; (2) 高效训练——为softmax+linear-attention混合骨干开发hardware-aware算法; (3) 推理加速。发现有监督的block-diffusion训练方案。

#### Self-Flow — Self-Supervised Flow Matching (ICML 2026)
*(详见 §1.1)*

#### Sparse Feature Attention (SFA) — Feature-level Sparsity for Attention
| | |
|---|---|
| **论文** | [arXiv:2603.22300](https://arxiv.org/abs/2603.22300) |

**创新**: 学习k-稀疏Q/K编码,仅通过支撑集重叠计算注意力分数。将QK^T复杂度从Θ(n²d)降至Θ(n²k²/d)。FlashSFA IO-aware kernel直接在稀疏重叠上操作。

---

## 14. Agent系统与多智能体

#### Aletheia — Autonomous Mathematics Research Agent (Google DeepMind)
| | |
|---|---|
| **作者** | Tony Feng, Junehyuk Jung, Sang-hyun Kim et al. (Google DeepMind + 多学术机构) |
| **论文** | [arXiv:2602.21201](https://arxiv.org/abs/2602.21201) |

**核心创新**: 基于Gemini 3 Deep Think的数学研究Agent。在FirstProof挑战中,10个问题中自主解决6个(P2/P5/P7/P8/P9/P10),专家评估一致认可(除P8有分歧)。

#### KAIJU — Executive Kernel for Intent-Gated Execution of LLM Agents
| | |
|---|---|
| **论文** | [arXiv:2604.02375](https://arxiv.org/abs/2604.02375) |

**核心创新**: 将Agent工作流执行与LLM推理层解耦。IGX安全范式在4个维度(scope, intent, impact, clearance)上强制执行意图。三种自适应执行模式(Reflect/nReflect/Orchestrator)。

**效果**: 简单查询因规划开销略慢;复杂查询nReflect超越ReAct (9.5s vs 28.9s);计算查询25.2s vs 43.7s。

#### HyperAgents — Self-Improving Meta-Learning Agents (Meta FAIR)
| | |
|---|---|
| **作者** | Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Minqi Jiang, Sam Devlin, Tatiana Shavrina |
| **机构** | UBC, Meta FAIR, Meta Superintelligence Labs, Vector Institute |
| **论文** | [arXiv:2603.19461](https://arxiv.org/abs/2603.19461) |

**核心创新**: 超智能体(Hyperagents)——将任务Agent和元Agent集成到单个可编辑程序中。元级修改过程本身也是可编辑的,实现元认知自修改。基于Darwin Gödel Machine的DGM-H扩展。

**效果**: 在编码、论文评审、机器人奖励设计、奥数评分等多领域持续超越基线。元级改进跨domain迁移、跨run累积。

#### Discovering Multiagent Learning Algorithms with LLMs (Google DeepMind)
| | |
|---|---|
| **论文** | [arXiv:2602.16928](https://arxiv.org/abs/2602.16928) |

**核心创新**: AlphaEvolve框架,LLM作为进化算子自动发现多Agent RL算法。发现VAD-CFR和SHOR-PSRO两个算法,在18个博弈游戏套件上一致与SOTA人类设计算法竞争。通过消融提炼出WOP-CFR和PM-PSRO最小求解器。

#### Subgoal-driven Framework for Long-Horizon LLM Agents (Google DeepMind)
| | |
|---|---|
| **论文** | [arXiv:2603.19685](https://arxiv.org/abs/2603.19685) |

**核心创新**: (1) 专有模型的在线子目标分解规划; (2) MiRA——基于里程碑密集奖励的RL训练框架。Gemini在WebArena-Lite上绝对成功率提升≈10%。Gemma3-12B从6.4%→43.0%,超越GPT-4-Turbo(17.6%)和GPT-4o(13.9%)。

#### ARTIS — Agentic Risk-Aware Test-Time Scaling via Iterative Simulation
| | |
|---|---|
| **论文** | [arXiv:2602.01709](https://arxiv.org/abs/2602.01709) |

**创新**: 在模拟环境中迭代探索多个行动尝试,风险感知模拟器基于失败驱动数据生成训练。在BFCL-v3和ACEBench上显著超越现有方法。

---

## 15. 游戏AI与代码执行

#### OpenGame — Open Agentic Coding for Games
| | |
|---|---|
| **论文** | [arXiv:2604.18394](https://arxiv.org/abs/2604.18394) |

**核心创新**: 150个浏览器游戏任务的编码Agent。OpenGame-Bench自动化评估管线。搭配Claude Sonnet 4.6, OpenGame在Build Health=72.4, Visual Usability=67.2, Intent Alignment=65.1,超越Cursor+Claude方案5-6点。

#### GameDevBench — Evaluating Agentic Capabilities Through Game Development
| | |
|---|---|
| **论文** | [arXiv:2602.11103](https://arxiv.org/abs/2602.11103) |

**核心创新**: 首个评估Agent游戏开发能力的基准。132个任务,平均解决方案需3倍SWE-bench的代码行数和文件变更。最佳Agent仅解决54.5%的任务。

#### PlayCoder — Making LLM-Generated GUI Code Playable (Tencent)
| | |
|---|---|
| **论文** | [arXiv:2604.19742](https://arxiv.org/abs/2604.19742) |

**核心创新**: 多Agent框架(PlayDeveloper + PlayRefiner)用于GUI代码生成和修复。Play@k指标衡量可玩游戏性。PlayCoder将Play@3从接近0提升至20.3%。

#### SWE-EVO — Coding Agents in Long-Horizon Software Evolution
| | |
|---|---|
| **论文** | [arXiv:2512.18470](https://arxiv.org/abs/2512.18470) |

**核心创新**: 长期软件演化基准。48个任务,平均涉及21个文件,874个测试。GPT-5.4仅达25%(对比SWE-Bench Verified上GPT-5.2达72.80%)。

#### Evaluating Interactive Reasoning — Hierarchical Benchmark with Executable Games
| | |
|---|---|
| **论文** | [arXiv:2606.00103](https://arxiv.org/abs/2606.00103) |

**创新**: 474个可执行游戏的交互推理基准。5个难度级别。评估框架包括上下文鲁棒性和元认知适应性。发现上下文扰动导致中等下降,而反事实修正和必要性判断导致大幅下降。

#### Agentick — Unified Benchmark for General Sequential Decision-Making
| | |
|---|---|
| **论文** | [arXiv:2605.06869](https://arxiv.org/abs/2605.06869) |

**创新**: 统一评估RL/LLM/VLM/混合/人类Agent的37个任务基准。GPT-5 mini以0.309归一化得分领先,PPO主导规划和多Agent任务。

---

## 16. 序列建模与状态空间模型

#### Mamba-3 — Improved Sequence Modeling using State Space Principles
| | |
|---|---|
| **作者** | Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu |
| **机构** | Carnegie Mellon, Princeton |
| **论文** | [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) |
| **代码** | [github.com/state-spaces/mamba](https://github.com/state-spaces/mamba) |

**核心创新**: 三大改进: (1) 指数-梯形离散化(exponential-trapezoidal discretization)实现更具表现力的动力学; (2) 复数值状态更新规则实现更丰富的状态追踪; (3) 多输入多输出(MIMO)公式提升建模能力且不增加解码延迟。

**实验结果**: 1.5B规模,平均下游准确率超Gated DeltaNet 0.6个百分点;MIMO变体再提升1.2个百分点。状态大小减半情况下媲美Mamba-2的perplexity。

#### Sparse Feature Attention (SFA)
*(详见 §13)*

#### NVIDIA Nemotron 3 Ultra — Hybrid Mamba-Transformer for Agents
| | |
|---|---|
| **机构** | NVIDIA |
| **链接** | [NVIDIA Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/) |

**核心创新**: 550B参数MoE(55B激活)。混合Mamba-Transformer层: Mamba层高效处理长上下文,Transformer层保留精确召回。NVFP4量化实现跨架构GPU部署(5×吞吐量提升)。LatentMoE + 多头预测。

**效果**: Ruler @1M达95%。SWE-bench和Terminal bench 2.0上总token数和每轮token数均更低,Agent成本降低30%。

---

## 17. LLM推理、对齐与效率

#### NF-CoT — Latent Reasoning with Normalizing Flows
| | |
|---|---|
| **论文** | [arXiv:2606.06447](https://arxiv.org/abs/2606.06447) |

**核心创新**: 在LLM骨干网内实例化TARFlow-style归一化流,定义在从显式CoT蒸馏的连续思想上的可处理概率模型。保留KV缓存解码兼容性、概率采样和精确似然估计。

**效果**: 在代码生成(MBPP/MBPP+/HumanEval/HumanEval+/LiveCodeBench v6)上超越显式CoT和先前的潜在推理基线,同时大幅降低中间推理成本。

#### LLM Self-Recognition — Steering and Retrieving Activation Signatures
| | |
|---|---|
| **论文** | [arXiv:2606.06315](https://arxiv.org/abs/2606.06315) |

**核心创新**: 通过注入随机稀疏向量产生可检测指纹,使文本归属于特定LLM。在多种检测设置下达98%+准确率且不降低生成质量。

#### Spectral Scaling Laws of Muon Optimizer
| | |
|---|---|
| **论文** | [arXiv:2606.04058](https://arxiv.org/abs/2606.04058) |

**核心创新**: 首次系统研究Muon优化器中动量矩阵奇异值谱在训练过程中的行为。发现层类型和模型大小决定的稳定化值遵循幂律。早期层M^-0.25,后期层可达M^-0.96。

**背景**: Muon已被DeepSeek-V4、Kimi K2、GLM-5等SOTA开源模型采用。

#### SigmaScale — SVD-based LLM Compression with Learned Scaling Matrices
| | |
|---|---|
| **论文** | [arXiv:2606.07098](https://arxiv.org/abs/2606.07098) |

**核心创新**: 为基于SVD的LLM压缩学习辅助缩放矩阵。通过激活感知压缩损失优化缩放变换。在Llama 3.1 8B和Qwen3-8B上超越SVD压缩SOTA。

#### Generative Criticality in LLM Temperature Scaling
| | |
|---|---|
| **论文** | [arXiv:2606.06238](https://arxiv.org/abs/2606.06238) |

**核心创新**: 将LLM生成的文本建模为1D链上的自旋变量。在Tc≈1.4附近观察到尖锐的磁化率峰、序参量快速变化、内在维度最小值。在Qwen3全系列(0.6B-32B)上验证。

#### How LLMs Detect and Correct Their Own Errors (Google DeepMind)
| | |
|---|---|
| **论文** | [arXiv:2604.22271](https://arxiv.org/abs/2604.22271) |

**核心创新**: 从决策神经科学视角研究LLM的自我纠错。发现LLM在答案后换行符(PANL)处缓存置信度表征。该信号不仅预测错误检测还预测模型是否有知识修复它。

#### Learning to Learn from Language Feedback (Google DeepMind)
| | |
|---|---|
| **论文** | [arXiv:2602.16488](https://arxiv.org/abs/2602.16488) |

**创新**: 社交元学习(SML)作为微调方法论,训练LLM在模拟教学对话中主动征求和学习语言反馈。数学→编码跨域泛化35%↓→90%+。

#### Improving Interactive In-Context Learning from Language Feedback (Google DeepMind)
| | |
|---|---|
| **论文** | [arXiv:2602.16066](https://arxiv.org/abs/2602.16066) |

**创新**: 将多轮可验证任务转化为信息不对称驱动的教学交互。Gemini 2.5 Flash多轮性能接近Gemini 2.5 Pro。数学训练泛化到编码、谜题、迷宫导航。

#### HRM-Text — Hierarchical Recursive Model (1B params for $1,000)
| | |
|---|---|
| **链接** | [36Kr报道](https://eu.36kr.com/en/p/3845426151835906) |

**核心创新**: 分层递归架构:低层模块快速局部计算,高层模块长期依赖。仅答案部分计算损失。1B参数,ARC-Challenge从51.91→81.91。

---

## 18. 推荐系统新范式

#### UniMixer — Unified Architecture for Scaling Laws in Recommendation (Kuaishou)
| | |
|---|---|
| **论文** | [arXiv:2604.00590](https://arxiv.org/abs/2604.00590) |

**核心创新**: 统一缩放框架,桥接attention-based/TokenMixer-based/FM-based三类主流架构。UniMixer-Lite在参数和计算效率上达到最佳。已部署在Kuaishou多个场景。

#### OneMall — End-to-End Generative Recommender Family (Kuaishou E-Commerce)
| | |
|---|---|
| **论文** | [arXiv:2601.21770](https://arxiv.org/abs/2601.21770) |

**创新**: 基于SID的生成式推荐家族。GRPO优于DPO(特别在Top10上+0.040% CTR, +0.012% CTCVR, +0.228% GPM)。

#### Mitigating Collaborative Semantic ID Staleness in Generative Retrieval (SIGIR 2026)
| | |
|---|---|
| **论文** | [arXiv:2604.13273](https://arxiv.org/abs/2604.13273) |

**创新**: 生成式检索中语义ID的checkpoint兼容更新策略。对齐更新在时间漂移下保持Recall@500 ≈ Full retrain水平。

#### General AgentBench — Benchmarking Test-Time Scaling of General LLM Agents
| | |
|---|---|
| **论文** | [arXiv:2602.18998](https://arxiv.org/abs/2602.18998) |

**核心发现**: 通用Agent在search/coding/reasoning/tool-use统一环境中表现大幅下降。无论sequential scaling还是parallel scaling在实践中的增益都很有限——上下文天花板(Context Ceiling)和验证鸿沟(Verification Gap)是根本限制。

---

## 总结：2025-2026 AI研究全景图

### 按领域的核心趋势

| 领域 | 关键趋势 |
|------|----------|
| **LLM架构** | Gated Attention (NeurIPS 2025 Best Paper); Mamba-3发布; HRM循环模型成本骤降 |
| **LLM推理** | Test-time scaling实证遇冷(General AgentBench); CoT忠实度受质疑; 潜在推理(NF-CoT)兴起 |
| **Diffusion模型** | AR→dLLM转换(FLARE); 扩散LM采样策略学习(ICML Oral); 不记忆机制被解密(NeurIPS Best) |
| **Agent系统** | 465篇ICML Agent论文; HyperAgents自改进; Aletheia数学证明Agent; 长期Agent仍是瓶颈 |
| **CTR/广告** | LLM启发架构全面进入工业界(CADET/GRAB/EST); LoopCTR开创循环缩放; 生成式推荐(GR4AD/OneMall)兴起 |
| **推荐系统** | SSM用于兴趣追踪; SID生成式推荐成熟化; 语义ID碰撞问题被解决 |
| **信息检索** | Rank-R1推理增强排序; RL for RAG成熟化; 自适应量化解决冷启动 |
| **游戏AI** | LLM Agent发现MARL算法(AlphaEvolve); GUI代码生成专用Agent出现 |
| **优化器** | Muon取代AdamW成为SOTA模型标配; Polar Express优化Muon多项式逼近 |
| **序列建模** | Mamba-3复数值状态+MIMO; 混合Mamba-Transformer(NVIDIA/Helix); 稀疏特征注意力 |

### 重要会议统计对比

| 会议 | 投稿 | 接收 | 接收率 | 年份 |
|------|------|------|--------|------|
| ICML 2026 | 23,918 | 6,352 | 26.6% | 2026 |
| NeurIPS 2025 | ~21,575 | 5,275 | 24.5% | 2025 |
| ICLR 2026 | 19,525 | 5,355 | 27.4% | 2026 |
| AAAI 2026 | ~29,000 | ~6,700 | ~23% | 2026 |
| CVPR 2026 | 16,092 | 4,089 | 25.4% | 2026 |
| EMNLP 2025 | 8,172 | 1,811 | 22.2% | 2025 |
| EACL 2026 | 2,200 | 445+355 | 36.4% | 2026 |
| RecSys 2025 | 260 | 49 | 18.9% | 2025 |

AAAI 2026以近3万投稿成为投稿量最大的会议,但ICML/NeurIPS/ICLR均增长40-70%,论文总量持续暴增。CVPR增长24%创新高。工业界CTR论文在arXiv上形成独立活跃社区。
