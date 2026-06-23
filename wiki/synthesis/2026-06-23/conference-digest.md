---
title: "顶会论文专题报告 — 2026年6月全面版（ICML 2026 / AAAI 2026 / NeurIPS 2025 / ICLR 2026 / CVPR 2026 / KDD 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025 + arXiv 前沿）"
type: synthesis
created: 2026-06-23
updated: 2026-06-23
sources:
  - icml-2026-proceedings
  - aaai-2026-proceedings
  - neurips-2025-proceedings
  - iclr-2026-proceedings
  - cvpr-2026-proceedings
  - kdd-2026-proceedings
  - acl-2026-proceedings
  - emnlp-2025-proceedings
  - sigir-2026-proceedings
  - www-2026-proceedings
  - cikm-2025-proceedings
  - recsys-2025-proceedings
  - arxiv-june-2026
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, ctr, recommendation, agents, rl, multimodal]
---

# 顶会论文专题报告 — 2026年6月全面版

> 涵盖 ICML 2026 / AAAI 2026 / NeurIPS 2025 / ICLR 2026 / CVPR 2026 / KDD 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025 及 arXiv 2026 年 6 月前沿论文.
> 聚焦 LLM / 推荐系统 / CTR / 广告 / Agent / 游戏 / 代码执行 / AI 安全 / 生成模型 / 多模态 / 基准测试方向.

---

## 目录

1. [ICML 2026 — 机器学习国际会议](#1-icml-2026)
2. [AAAI 2026 — 人工智能会议](#2-aaai-2026)
3. [NeurIPS 2025 — 神经信息处理系统](#3-neurips-2025)
4. [ICLR 2026 — 学习表示国际会议](#4-iclr-2026)
5. [CVPR 2026 — 计算机视觉与模式识别](#5-cvpr-2026)
6. [KDD 2026 — 知识发现与数据挖掘](#6-kdd-2026)
7. [ACL 2026 / EMNLP 2025 — 自然语言处理](#7-acl-2026--emnlp-2025)
8. [SIGIR 2026 / WWW 2026 — 信息检索与Web](#8-sigir-2026--www-2026)
9. [CIKM 2025 / RecSys 2025 — 推荐系统](#9-cikm-2025--recsys-2025)
10. [arXiv 前沿 — 2026年6月](#10-arxiv-前沿--2026年6月)
    - 10.1 LLM 论文 (RLVR / 推理 / 架构)
    - 10.2 Agent 系统与工具
    - 10.3 CTR / 推荐 / 广告工业界
    - 10.4 游戏 RL / 代码执行
    - 10.5 生成模型 / 多模态 / 基准测试
11. [主题趋势总结](#11-主题趋势总结)

---

## 1. ICML 2026

### 概览

| 指标 | 数值 |
|------|------|
| 地点 | 韩国 首尔 |
| 时间 | 2026 年 7 月 |
| 投稿数 | 23,918 |
| 录用数 | 6,352 (26.6%) |
| Spotlight | ~2.2% |
| Oral | ~0.7% |

ICML 2026 收到创纪录的 24,371 篇投稿（较 2025 年翻倍），录用 6,352 篇。研究热点包括 **AI Agent 可靠性**、**多模态模型**、**高效训练技术**、**推理时计算 (Test-Time Compute)**、**扩散语言模型**。

### 精选论文

#### 1.1 Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents
- **Authors**: ICML 2026
- **Affiliation**: 多家机构
- **Venue**: ICML 2026
- **Abstract**: 针对 LLM 搜索 Agent 的 RL 训练中结构异质性（不同搜索步骤需要不同策略）问题，提出分层 GRPO——将搜索过程分层处理，每层独立优化。在复杂搜索任务上显著优于标准 GRPO。
- **Key Innovation**: 分层强化学习解决了单一 reward 信号无法区分搜索树中不同节点质量的问题。在 multi-step reasoning 和 web search 场景中提升 ~15%。
- **arXiv**: https://www.paperdigest.org/paper/?paper_id=icml-63159-2026-05-05

#### 1.2 Agentic Verifier: Execution-Based Re-Ranking for Competitive Coding
- **Key Highlight**: 使用执行结果作为验证信号的 Agentic re-ranking 方法，在竞争性编程中通过执行反馈实现第二遍排序。
- **Practical Use**: 可用于 AI coding agent 的代码选择与验证流水线。

#### 1.3 FPTQuant: Efficient 4-bit Quantization in Transformer Models
- **Key Highlight**: 面向 Transformer 的高效 4-bit 量化方案，在保持模型质量的同时大幅降低推理成本。

#### 1.4 Proximal Decoding: Reducing Copyright Risk in LLM Generation
- **Key Highlight**: 一种解码策略，通过约束生成过程接近原始分布同时避免与受版权保护内容的过度相似性。

#### 1.5 How does Chain of Thought decompose complex tasks?
- **Authors**: Amrut Nadgir, Vijay Balasubramanian, Pratik Chaudhari
- **Affiliation**: UPenn
- **Abstract**: 理论分析 Chain-of-Thought 如何将复杂任务分解为子步骤。揭示了 CoT 成功的内在机制——将高维决策空间投影到低维子步骤序列。
- **arXiv**: https://arxiv.org/abs/2604.08872

#### 1.6 Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control
- **Authors**: Peihao Wang et al.
- **Affiliation**: 多家机构
- **Abstract**: 将推理视为最优控制问题，提出硬件高效的推理学习方法。在数学推理任务上接近 o1 级别性能，但计算成本降低 3-5×。
- **arXiv**: https://arxiv.org/abs/2603.09221

#### 1.7 Correctness-Optimized Residual Activation Lens (CORAL)
- **Authors**: Miranda Muqing Miao, Young Min Cho, Lyle Ungar
- **Affiliation**: UPenn
- **Abstract**: 推理时激活值编辑方法，通过校准感知的残差激活透镜实现可迁移的推理时输出控制。无需训练即可改善模型输出正确性。
- **arXiv**: https://arxiv.org/abs/2602.06022

#### 1.8 Emergent Alignment via Competition
- **Authors**: Natalie Collina, Surbhi Goel, Aaron Roth et al.
- **Affiliation**: UPenn / Microsoft
- **Abstract**: 通过多智能体竞争而非显式 RLHF 实现对齐。智能体在竞争性博弈中自然发展出有益行为，为对齐提供新思路。
- **arXiv**: https://arxiv.org/abs/2509.15090

#### 1.9 BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding
- **Authors**: Liang He et al.
- **Abstract**: 针对稀疏 KV 缓存推测解码的 BudgetDraft 方法，通过多视角训练提升 draft model 的接受率。
- **arXiv**: https://arxiv.org/abs/2606.00144

#### 1.10 Generative AI and Digital Ecosystem Resilience
- **Authors**: Jonghyun Chung et al.
- **Abstract**: 生成式 AI 与数字生态系统弹性的综述性研究，提出基于生命周期的主动式框架。
- **arXiv**: https://arxiv.org/abs/2606.00136

---

## 2. AAAI 2026

### 概览

| 指标 | 数值 |
|------|------|
| 地点 | 新加坡 |
| 时间 | 2026 年 1 月 20-27 日 |
| 投稿数 | ~29,000 → 23,000 (合规过滤后) |
| 录用数 | 4,167 (17.6%) |
| 主题 | Creating Collaborative Bridges Within and Beyond AI |

AAAI 2026 收到近 29,000 篇投稿，创历史新高。**首次在全技术轨道部署 AI 辅助同行评审**（22,977 篇论文在 24 小时内完成 AI 评审）。

### 精选论文

#### 2.1 From AGI to ASI (Outstanding Paper 方向)
- **Authors**: Google DeepMind (14 位作者)
- **Venue**: AAAI 2026 / arXiv:2606.12683
- **Abstract**: 57 页路线图，勾勒 AGI 到 ASI 的四条路径：(1) Scaling AGI, (2) Paradigm Shifts, (3) Recursive Improvement, (4) Multi-Agent Collectives。定义 ASI 为"比大型人类组织更智能"的系统。
- **Key Innovation**: 首次系统性地研究 AGI 到 ASI 的过渡阶段，提出可操作的技术路径分析。
- **Impact**: 数日内 arXiv 浏览量超 54,000，引发广泛讨论。
- **arXiv**: https://arxiv.org/abs/2606.12683

#### 2.2 AI Co-Mathematician: Accelerating Mathematicians with Agentic AI
- **Authors**: Google DeepMind
- **Venue**: AAAI 2026
- **Abstract**: 一个有状态的 AI 工作空间，支持数学家的长期数学发现过程。从问题提出到猜想验证，AI 作为协作伙伴。
- **Key Innovation**: 将 LLM 与形式化数学环境结合，支持迭代式、非线性的数学研究过程。
- **arXiv**: https://arxiv.org/abs/2605.06548 (相关)

#### 2.3 Evaluating Language Models for Harmful Manipulation
- **Authors**: Google DeepMind
- **Venue**: AAAI 2026
- **Abstract**: 构建评估 LLM 在真实人机交互中有害操纵行为的框架。系统性评估多个前沿模型在 deceptive persuasion 场景下的表现。
- **Key Innovation**: 首个针对 LLM 操纵行为的全面评估框架，包含细粒度操纵分类学。

#### 2.4 Contextualizing Recommendation Explanations with LLMs: A User Study
- **Authors**: Yuanjun Feng, Stefan Feuerriegel, Yash Raj Shrestha
- **Affiliation**: LMU Munich
- **Abstract**: 通过用户研究揭示 LLM 生成的推荐解释如何影响用户动机和行为。为以用户为中心的推荐系统提供设计指南。
- **arXiv**: https://arxiv.org/pdf/2501.12152

#### 2.5 Qwen-VL Family 技术进展（多篇论文）
- **Authors**: Alibaba Qwen Team
- **Venue**: AAAI 2026
- **Abstract**: Qwen-VL 系列多模态模型在视觉理解和推理上的持续改进，展示了从语言到多模态的能力扩展路径。

#### 2.6 AI 辅助 Peer Review 实验
- AAAI 2026 与 OpenAI 合作，为 22,977 篇论文生成 AI 评审。AI 报告标有 AI 标识、不包含评分、不推荐接受/拒绝。这是顶级 AI 会议首次在全技术轨道部署生成式 AI 辅助评审。

---

## 3. NeurIPS 2025

### 概览

| 指标 | 数值 |
|------|------|
| 地点 | 美国 圣地亚哥 (+ 墨西哥城卫星会场) |
| 时间 | 2025 年 12 月 2-7 日 |
| 投稿数 | ~21,000+ |
| 录用数 | ~5,526 |

NeurIPS 2025 首次设置双会场（圣地亚哥 + 墨西哥城），Position Papers 作为新轨道引入。

### 精选论文

#### 3.1 Gated Integration of Low-Rank Adaptation for Continual Learning of LLMs
- **Authors**: Yan-Shuo Liang, Jia-Rui Chen, Wu-Jun Li
- **Affiliation**: 南京大学
- **Abstract**: 针对 LLM 连续学习的灾难性遗忘问题，提出门控集成的 LoRA 分支管理方法。通过学习门控机制动态平衡新旧任务知识。
- **Key Innovation**: 解决了现有 LoRA 连续学习中"简单加法"导致的旧任务干扰问题。
- **arXiv**: https://arxiv.org/pdf/2505.15424

#### 3.2 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference
- **Authors**: Jiayi Yuan et al.
- **Affiliation**: 多家机构
- **Abstract**: 首次系统研究数值精度如何影响 LLM 推理的可复现性。发现改变 batch size、GPU 数量等配置会导致 >9% 的准确率差异，特别是在推理模型中。
- **Key Finding**: DeepSeek-R1-Distill-Qwen-7B 在 bfloat16 + greedy decoding 下，因 GPU 配置不同产生高达 9% 准确率波动和 9000 tokens 长度差异。
- **Root Cause**: 浮点数运算在有限精度下的非结合性。

#### 3.3 Default MoE: Dense Backpropagation Improves Training for Sparse Mixture-of-Experts
- **Authors**: Sambit Sahu, Supriyo Chakraborty (Capital One)
- **Abstract**: 为 MoE router 提供稠密梯度更新（而非稀疏），同时保持稀疏参数激活。每个 token 从所有 expert 接收信号，显著提升训练性能而无显著计算开销。
- **arXiv**: https://arxiv.org/abs/2504.12463

#### 3.4 GPO: Learning from Critical Steps to Improve LLM Reasoning
- **Authors**: Zelei Cheng et al. (Northwestern / Capital One)
- **Abstract**: 引导关键步优化 (GPO)，通过 advantage 函数定位推理轨迹中的"关键步骤"，重置策略到该点并优先学习新 rollout。
- **arXiv**: https://arxiv.org/abs/2509.16456

#### 3.5 A-MEM: Agentic Memory for LLM Agents
- **Authors**: NeurIPS 2025
- **Abstract**: Zettelkasten 启发的 agentic 记忆系统。每条记忆自动生成结构化笔记（关键词/标签/上下文描述），动态建立记忆间链接，触发演进式更新。在 LoCoMo 长对话 QA 基准上大幅超越 MemGPT。

#### 3.6 AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents
- **Abstract**: 无训练、记忆增强推理框架，使 LLM 自适应提取结构化语义特征（场景/风险/行为），构建经验记忆库。提出 ASSEBench——首个联合覆盖安全和安全评估的基准（2,293 条记录, 15 种风险类型, 29 种场景）。

#### 3.7 Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding
- **Abstract**: DVD 框架将长视频理解构建为多步信息搜索问题。三级结构化数据库（全局摘要 + 片段字幕嵌入 + 帧级像素），三个搜索工具。在 LVBench 上达 74.2%（超越 SOTA MR.Video 13.4pp）。

#### 3.8 EraseFlow: Learning Concept Erasure Policies via GFlowNet-Driven Alignment
- **Authors**: Naga Sai Abhiram Kusumba et al. (Capital One)
- **Abstract**: 首个将概念遗忘构建为去噪路径空间中的探索问题并用 GFlowNet 优化的框架。用于从文生图模型中擦除有害/专有概念同时保持图像质量。
- **arXiv**: https://arxiv.org/abs/2511.00804

---

## 4. ICLR 2026

### 概览

| 指标 | 数值 |
|------|------|
| 投稿数 | 19,809 |
| 录用数 | 5,343 (26.97%) |
| Oral | 223 (1.13%) |
| Spotlight | — |

### 精选论文

#### 4.1 Planner Aware Path Learning (PAPL) in Diffusion Language Models Training **(Oral)**
- **Authors**: Zhangzhi Peng, Zachary Bezemek, Jarrid Rector-Brooks, Shuibai Zhang, Michael Bronstein, Anru Zhang, Joey Bose, Alexander Tong
- **Abstract**: 理论证明标准离散扩散训练 ELBO 在使用非均匀 planner 时不准确。提出新的 Planned ELBO (P-ELBO) 和 PAPL 训练方案，弥合训练和推断之间的路径分布差异。
- **Key Results**: 蛋白质序列 +40% 相对提升；文本生成 MAUVE 提升 4×；代码生成 HumanEval pass@10 +23%。
- **arXiv**: https://openreview.net/forum?id=lAlI5FuIf7

#### 4.2 MERCI: Motivating Exploration in LLM Reasoning with Count-based Intrinsic Rewards
- **Venue**: ICLR 2026
- **Abstract**: 基于计数的探索方法，使用 Coin Flipping Network (CFN) 估计推理轨迹的伪计数和认知不确定性，转换为内在奖励。集成到 GRPO 框架中，在复杂推理基准上显著提升。
- **Key Innovation**: 解决 RL 推理训练中的探索-利用困境，鼓励更多样化的 Chain-of-Thought。

#### 4.3 AgilePruner: Adaptive Visual Token Pruning in Large Vision-Language Models
- **Authors**: CVSP Lab
- **Abstract**: 首个基于 erank 表征的视觉 token 剪枝方法，动态适应图像复杂度——简单图像保留细粒度高注意力 token，复杂图像增强 token 多样性。
- **Key Results**: 在 ScienceQA / POPE 等基准上表现稳健，有效降低幻觉。
- **arXiv**: https://paper.pnu-cvsp.com/AgilePruner

#### 4.4 Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training
- **Authors**: Pierre-Carl Langlais et al.
- **Abstract**: 迄今最大的合规/伦理 LLM 预训练数据集合，解决预训练数据的版权和伦理问题。

#### 4.5 Principled RL for Diffusion LLMs Emerges from a Sequence-Level Perspective (ESPO)
- **Authors**: ML-GSAI Lab
- **Abstract**: 从序列级视角推导扩散 LLM 的 RL 训练原则。提出 ESPO 方法，将 RL 与扩散 LLM 的自然序列特性对齐。
- **arXiv**: https://arxiv.org/abs/2512.03759

#### 4.6 ECF8: Exponent-Concentrated FP8 — Lossless Compression for Transformer
- **Authors**: Lambda Lab / 多家机构
- **Abstract**: 发现训练权重的指数集中在 FP8 分配的 4 位中仅占 2-3 位熵。ECF8 利用 Huffman 编码压缩冗余，在扩散模型上节省 26.9% 内存，吞吐量提升最高达 177.1%，可无损扩展到 671B LLM。

#### 4.7 In-The-Flow Agentic System Optimization for Effective Planning and Tool Use
- **Authors**: Stanford
- **Abstract**: 面向 agentic 系统的"流程中"优化框架，有效改进规划和工具使用。
- **arXiv**: https://arxiv.org/abs/2510.05592

#### 4.8 OffTopicEval: When Large Language Models Enter the Wrong Chat
- **Authors**: Declare Lab
- **Abstract**: 研究 LLM 在多轮对话中的"话题偏移"问题，提出 OffTopicEval 基准。
- **arXiv**: https://arxiv.org/abs/2509.26495

#### 4.9 Mitigating Non-IID Drift in Zeroth-Order Federated LLM Fine-Tuning
- **Abstract**: 解决联邦 LLM 微调中非独立同分布漂移问题，用可迁移稀疏性方法。
- **arXiv**: https://arxiv.org/abs/2506.03337

---

## 5. CVPR 2026

### 概览

| 指标 | 数值 |
|------|------|
| 地点 | 美国 丹佛 |
| 时间 | 2026 年 6 月 3-7 日 |
| 投稿数 | 16,092 |
| 录用数 | 4,090 (25.42%) |
| 比 CVPR 2025 增长 | +42.5% |

### 关键趋势

1. **多模态语言模型翻倍**: VLM / 多模态 LLM 论文从 2025 年的 4.9% 增长到 10.6%（+5.7pp），成为 CVPR 2026 最大主题
2. **视频生成爆发**: 视频生成相关论文增长 2.3×
3. **经典 CV 检测萎缩**: 传统目标检测等经典方向占比下降

### 精选论文

#### 5.1 Improving Vision-Language Models with Perception-Centric Process Reward Models
- **Venue**: CVPR 2026
- **Abstract**: Perceval reward model 替代 GRPO 的序列级惩罚，提供 token 级过程奖励，仅惩罚与图像证据矛盾的具体短语。显著减少 VLM 幻觉。

#### 5.2 LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning
- **Authors**: Zebin You, Shen Nie, Xiaolu Zhang, Jun Hu et al.
- **Abstract**: 扩散语言模型的视觉指令微调版本。尽管纯语言能力弱于 LLaMA3-8B，但视觉理解达到顶级多模态模型水平——说明扩散架构本身在对齐视觉和语言特征方面具有独特优势。

#### 5.3 AVGGT: Rethinking Global Attention for Accelerating VGGT
- **Authors**: Xianbing Sun et al.
- **Abstract**: 系统分析 VGGT/π³ 中全局注意力模块的贡献：早期层不做匹配，中层做跨视图对齐，末层仅做微调。据此提出训练自由的 8-10× 加速方案。

#### 5.4 MV-RoMa: Multi-View Dense Matching Model
- **Authors**: JongMin Lee, Seungyeop Kang, Sungjoo Yoo
- **Abstract**: 从同源图像联合估计到多个共视目标的密集对应关系。高效架构避免全交叉注意力的高计算成本。

#### 5.5 NitroGen: Open Generalist Gaming Agent
- **Venue**: CVPR 2026
- **Abstract**: 开放的通用游戏智能体，在多个 3D 游戏环境中通过视觉观察学习玩各类游戏。

#### 5.6 AgilePruner (同时入选 ICLR 2026 & CVPR 2026)
- 见 ICLR 2026 部分。

---

## 6. KDD 2026

### 概览

| 指标 | 数值 |
|------|------|
| 地点 | 韩国 济州岛 |
| 时间 | 2026 年 8 月 9-13 日 |
| 两个投稿周期 | Cycle 1 + Cycle 2 |
| 录用率 (Cycle 1) | 256/1,215 (21%) |

### 精选论文

#### 6.1 Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents
- **Authors**: Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Affiliation**: Google (YouTube)
- **Abstract**: 利用 Google Gemini 系列 LLM 自主生成、训练和部署推荐模型变更。Offline Agent (Inner Loop) 用代理指标进行高通量假设生成，Online Agent (Outer Loop) 用真实业务指标验证。
- **Key Results**: 在 YouTube 成功上线多项改进，证明自主 LLM 驱动的进化可以超越传统工程工作流。
- **arXiv**: https://arxiv.org/abs/2602.10226

#### 6.2 Generative Long-term User Interest Modeling for CTR Prediction
- **Authors**: Jiangli Shao et al.
- **Affiliation**: 广告/推荐平台
- **Abstract**: 针对长期用户兴趣建模，提出 GenLI——包含兴趣生成模块 (IGM)、行为检索模块 (BRM)、兴趣融合模块 (IFM)。用生成范式替代传统的 target-centered 检索，避免兴趣偏置。
- **arXiv**: https://arxiv.org/abs/2605.15905

#### 6.3 DLRMv3: Generative Recommendation Benchmark in MLPerf Inference
- **Authors**: MLCommons / Meta
- **Abstract**: MLPerf 第三代推荐基准——基于 HSTU 架构的生成式推荐模型。标志推荐系统基准从 MLP/Cross-Network 向 Transformer-based 顺序模型迁移。
- **Link**: https://mlcommons.org/2026/02/dlrmv3-inference-meta/

#### 6.4 Self-Harness: Harnesses That Improve Themselves
- **Authors**: arXiv 2026 (KDD 2026 相关)
- **Abstract**: LLM 智能体自主优化自身操作框架的三阶段循环（弱点挖掘 → 框架提案 → 提案验证）。MiniMax M2.5 从 40.5% 提升至 61.9%（+52.6%）。
- **arXiv**: https://arxiv.org/abs/2606.08405 (相关)

#### 6.5 Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation
- **Authors**: Junwei Pan et al. (Tencent)
- **Abstract**: 腾讯广告算法挑战赛——全模态生成式推荐范式。发布 TencentGR-1M/10M 多模态数据集，涵盖协同 ID + 多模态嵌入。使用因果 Transformer + InfoNCE loss。
- **arXiv**: https://arxiv.org/abs/2604.04976

#### 6.6 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation
- **Abstract**: 冷启动 CTR 预测方法，使用 ID Proxy 机制处理广告和推荐中的新物品冷启问题。
- **arXiv**: https://arxiv.org/abs/2603.01590

#### 6.7 中国科技公司 CTR 论文全景（KDD 2026）

| 公司 | 论文数 (2025-2026) | 代表方向 |
|------|-------------------|---------|
| Meta | 15+ | Wukong, HSTU, DLRMv3, Scaling Laws |
| ByteDance | 12+ | RankMixer, OneTrans, HyFormer, Zenith |
| Alibaba | 14+ | GPSD, FAT, EST, LoopCTR, ENCODE |
| Tencent | 10+ | GE4Rec, TokenFormer, All-Modality GR |
| Meituan | 5+ | SUAN, MTFM, Next-Scale Generative Reranking |
| Kuaishou | 5+ | On the Equivalence of GR, DIF (KDD 2026) |

---

## 7. ACL 2026 / EMNLP 2025

### ACL 2026

- **投稿**: 通过 ACL ARR 2026 January 周期开放
- **热点方向**: LLM 评估、多语言 NLP、Agent System、代码生成、推理

### EMNLP 2025

| 指标 | 数值 |
|------|------|
| 地点 | 中国 苏州 |
| 时间 | 2025 年 11 月 4-9 日 |
| 投稿数 | 8,000+ |
| 录用数 | 3,490 (Main) + 1,405 (Findings) |
| 纪念 | EMNLP 30 周年 |

#### 7.1 Towards Automated Error Discovery in Conversational AI (Main #1)
- **Authors**: Dominic Petrak, Thy Thy Tran, Iryna Gurevych (TU Darmstadt)
- **Abstract**: 提出 SEEED——基于编码器的对话错误发现框架。改进 Soft Nearest Neighbor Loss，在未知错误检测上超越 GPT-4o 和 Phi-4，准确率提升 8pp。

#### 7.2 QFrCoLA: Quebec-French Corpus of Linguistic Acceptability (Main #6)
- **Authors**: David Beauchemin, Richard Khoury
- **Abstract**: 25,153 句域内 + 2,675 句域外句子组成的法语句法可接受性判断语料库。

#### 7.3 Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs (Main #2)
- **Authors**: Mohsinul Kabir, Ajwad Abrar, Sophia Ananiadou
- **Abstract**: 挑战 LLM 文化对齐的封闭式多项选择评估范式。证明 LLM 在更开放的设置中表现更强文化对齐，而封闭式评估结果不稳定（选项顺序变化即导致不一致）。

#### 7.4 Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding (Main #10)
- **Authors**: Melanie Subbiah et al. (Columbia / UT Austin)
- **Abstract**: 提出 Ambiguity Rewrite Metric (ARM)——用 LLM 生成的摘要编辑量作为故事理解忠实度的连续评估信号，替代二元忠实度判断。

#### 7.5 Coding Agents are Effective Long-Context Processors
- **Authors**: 多家机构
- **Venue**: EMNLP 2025 相关 / arXiv
- **Abstract**: 证明 off-the-shelf coding agent 在处理长文本任务上的惊人迁移能力。将长上下文推理构建为代码操作（分割-处理-合并），显著优于传统纯文本方法。

---

## 8. SIGIR 2026 / WWW 2026

### SIGIR 2026

| 指标 | 数值 |
|------|------|
| 地点 | 澳大利亚 墨尔本 |
| 时间 | 2026 年 7 月 20-24 日 |
| 投稿截止 | 2026 年 1 月 |

#### 8.1 ETEGRec: End-To-End Generative Recommender
- **Abstract**: 统一物品 tokenization 和生成式推荐训练到端到端框架中。当前方法将 tokenization 和 GR 训练分离导致次优性能，ETEGRec 解决这一分离问题。
- **Link**: SIGIR 2025 最具影响力论文 #1

#### 8.2 ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding
- **Abstract**: 检索增强推理 + 可信过程奖励，为推理链的每一步提供细粒度验证。
- **Link**: SIGIR 2025 最具影响力论文 #2

#### 8.3 KuaiLive: A Real-time Interactive Dataset for Live Streaming Recommendation
- **Authors**: Changle Qu, Sunhao Dai et al.
- **Affiliation**: Kuaishou
- **Abstract**: 首个实时直播推荐交互数据集，捕捉直播中的动态用户行为模式。

#### 8.4 WebMall: A Multi-Shop Benchmark for Evaluating Web Agents
- **Abstract**: 多商店 Web Agent 评估基准，测试 LLM Agent 在电商场景中的跨站购物能力。

#### 8.5 Beyond Maintenance: A Benchmark and Multi-Agent Framework for Repository-Usage Code Generation
- **Authors**: Kaitao Lin et al.
- **Abstract**: 超越代码维护的代码生成基准——测试 Agent 在仓库级别代码生成中的能力。

### WWW 2026

- **焦点**: LLM4Rec, Agentic Search, Generative IR
- **热门方向**: 从 LLM for Recommendation 到 Agent-based 交互式信息获取

---

## 9. CIKM 2025 / RecSys 2025

### CIKM 2025

- **最近会议**: 2025 年 10 月举行
- **焦点**: 知识管理、信息检索、推荐系统数据挖掘
- **热门论文方向**:
  - Generative Recommendation (GenRec)
  - Large-scale Foundation Model for Recommendation
  - Multi-modal Recommendation
  - Causality in Recommendation

### RecSys 2025

- **地点**: 意大利
- **热门方向**:
  - **LLM4Rec**: LLM 驱动的推荐系统技术栈（架构、学习范式、部署）
  - **Generative Recommendation**: 生成式推荐从概念到工业部署
  - **Sequential Recommendation with Transformers**: HSTU 类架构在工业界的推广
  - **Multi-task Learning**: 多目标排序的工业实践
  - **User Modeling with Foundation Models**: 基础模型赋能的用户建模

---

## 10. arXiv 前沿 — 2026年6月

### 10.1 LLM 论文 (RLVR / 推理 / 架构)

#### 10.1.1 VIMPO: Value-Implicit Policy Optimization for LLMs
- **Authors**: Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song, Xuandong Zhao
- **Date**: June 2026
- **Abstract**: 无需 critic model 的 RLVR 方法——从策略中隐式提取价值函数。在 AIME / OlympiadBench 上超越 GRPO。
- **arXiv**: https://arxiv.org/abs/2606.20008

#### 10.1.2 Beyond Entropy / Implicit Curriculum Tracing (ICT) — Token-Level Distributional RLVR
- **Date**: June 2026
- **Abstract**: Token 级分布的 RLVR 优化，超越简单熵正则化。在数学推理任务上 pass@4 +4.58%。
- **Link**: arXiv 2606 (上周 arXiv)

#### 10.1.3 StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation
- **Abstract**: 首个用于注意力 KL 散度的融合 GPU 原语。消除二次显存占用，forward 加速 43×，backward 加速 14×，单 GPU 即可实现长上下文蒸馏。
- **arXiv**: https://arxiv.org/abs/2606.20005

#### 10.1.4 Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization via RL
- **Authors**: Yanxi Chen et al. (Alibaba)
- **Abstract**: 面向长期部署 Agent 的 RL 训练框架——LLM 在环境中连续执行任务、探索、从经验中学习、迭代自更新。GRPO-style RL + 细粒度 credit assignment。
- **Key Results**: 验证了在训练域内、跨域、以及到 Ralph-loop 设置中 elicited meta-capability 的 OOD 泛化。
- **arXiv**: https://arxiv.org/abs/2606.20002

#### 10.1.5 Latent Reasoning with Normalizing Flows (NF-CoT)
- **Authors**: Guancheng Tu et al.
- **Date**: June 4, 2026
- **Abstract**: 用归一化流替代显式 chain-of-thought，在连续潜在空间中推理。结合 GRPO-style 的 RL 训练，在 HumanEval / MBPP / LiveCodeBench v6 上提升 pass rate，同时减少中间推理成本。
- **arXiv**: https://arxiv.org/abs/2606.06447

#### 10.1.6 Cola DLM: Continuous Latent Diffusion Language Model
- **Abstract**: 层次化连续潜在扩散语言模型。先用 Text VAE 将文本映射到连续潜在空间，再用 block-causal Diffusion Transformer 进行语义建模。相比 AR 和 diffusion baselines 展现强扩展性。
- **arXiv**: https://arxiv.org/abs/2605.06548

#### 10.1.7 Reinforcement Learning Elicits Contextual Learning of Unseen Language Translation
- **Authors**: Hanxu Hu et al.
- **Abstract**: 使用 chrF reward 信号的 RL 方法用于低资源翻译，将 RL 在编码/数学中的成功泛化到翻译任务。
- **arXiv**: https://arxiv.org/abs/2606.06428

#### 10.1.8 DeepSeek 前沿: Mamba-3, Gated DeltaNet-2 等新架构涌现
- 混合架构 (Hybrid Attention + SSM) 成为 LLM 架构新范式
- 代表: Nemotron 3 交替使用 Attention + Mamba-2 层
- 趋势: 长上下文效率是关键驱动因素

### 10.2 Agent 系统与工具

#### 10.2.1 AI Agent Systems Survey (2601.01743)
- **Authors**: Bin Xu (ASU)
- **Abstract**: 关于 AI Agent 架构的综合综述——deliberation/reasoning、planning/control、tool calling/environment interaction 的统一分类法。涵盖 agent 组件、编排模式、部署设置。
- **arXiv**: https://arxiv.org/abs/2601.01743

#### 10.2.2 Code as Agent Harness Survey (2605.18747)
- **Abstract**: 将代码作为 Agent 的"操纵框架"的综合综述——代码不仅是 LLM 生成的产物，也是可执行、可检查、有状态的推理媒介。
- **Categories**: Planning/Memory/Tool Use → 长时执行; 单 Agent → 多 Agent 扩展; 代码辅助 → GUI/OS 自动化 → 具身 Agent → 科学发现
- **arXiv**: https://arxiv.org/abs/2605.18747

#### 10.2.3 Self-Harness: Agents That Improve Their Own Framework
- **Abstract**: 三阶段自动框架优化：Weakness Mining → Harness Proposal → Proposal Validation
- **Key Results**: Terminal-Bench 2.0: MiniMax M2.5 40.5%→61.9% (+52.6%), GLM-5 42.9%→57.1% (+33.1%)

#### 10.2.4 Connect the Dots (见 10.1.4) — Alibaba 长期 Agent 框架
- 端到端 RL 训练让 Agent 在部署环境中持续自进化

#### 10.2.5 Awesome AI Agent Papers (GitHub: VoltAgent)
- 2026 年已收录 363+ 篇 Agent 论文
- 分类: Multi-Agent (53), Memory & RAG (57), Eval & Observability (80), Agent Tooling (95), AI Agent Security (82)

### 10.3 CTR / 推荐 / 广告工业界

#### 10.3.1 生成式推荐 (Generative Recommendation) 工业成熟化

| 论文 | 公司 | 方法 | 关键创新 |
|------|------|------|---------|
| GenCTR | 大型电商 | 生成预训练 → 判别微调 | 两阶段训练：next-item 生成预训练 + CTR 判别微调 |
| Unified Value Alignment for GR | Tencent | 值对齐生成式推荐 | 在工业广告中统一 GR 的值对齐 |
| TokenFactory | Google | Soft Token 统一信号 | 用软 token 整合多种传统信号到大推荐模型 |
| DLRMv3 | Meta/MLCommons | HSTU 基准 | MLPerf 官方基准迁移到 HSTU 架构 |
| Tencent All-Modality GR | Tencent | 全模态 GR | 多模态 + 协同 ID + 因果 Transformer |
| LoopCTR | Alibaba | 闭环优化 | CTR 模型的在线自优化闭环 |

#### 10.3.2 多任务与跨域

| 论文 | 公司 | 创新 |
|------|------|------|
| OneRank (KDD 2026) | — | 统一多任务排序框架 |
| HORIZON Benchmark | Microsoft | 真实世界用户行为跨域/长时基准 |
| Beyond Dense Connectivity | Alibaba | 显式稀疏化可扩展推荐 |

#### 10.3.3 模型架构演进

- **TokenFormer** (Tencent): 统一多域特征交互和序列推荐
- **FEDIN** (Tencent): 频域增强深度兴趣网络，捕捉周期性模式
- **SparseCTR**: 面向超长用户行为序列的稀疏注意力
- **DGenCTR**: 离散扩散生成式 CTR 预测

#### 10.3.4 检索增强与 Agent 混合

- **Self-Evolving RS** (Google/YouTube): LLM Agent 自动优化推荐模型
- **Agentic NL2SQL**: Datalake Agent 用于交互式推理
- **Multi-Agent Filtering** (Microsoft Research Asia): 多模态多智能体协作推荐过滤

### 10.4 游戏 RL / 代码执行

#### 10.4.1 Game RL 前沿

| 论文 | 方向 | 要点 |
|------|------|------|
| Odysseus | VLM Game RL | 100+ 回合 Mario 游戏，VLM 驱动的强化学习 |
| SPIRAL | Self-Play 零和博弈 | 自对弈在零和博弈中的理论突破 |
| NitroGen (CVPR 2026) | 通用游戏 Agent | 开放通用游戏智能体，多环境泛化 |
| Game-TARS | 大规模通用 Agent | 500B+ token 训练，在 FPS 游戏中超越 GPT-5 |
| Matrix-Game 3.0 | 世界模型 | 40FPS 720p 实时世界模型 |
| GameWorld | 基准测试 | 34 个浏览器游戏，170 个任务 |
| KRAFTON Ally | 工业部署 | PUBG AI 队友系统已上线 |
| Continual Harness | 持续学习 | Gemini Plays Pokémon 框架 |

#### 10.4.2 代码执行与推理

- **Coding Agents as Long-Context Processors** (EMNLP 2025): 编码 Agent 作为长上下文处理器
- **NF-CoT**: 潜在归一化流推理
- **Code as Agent Harness**: 代码作为 Agent 操纵框架
- **DataCOPE**: 无监督技能发现用于 Agentic 数据分析（Python/SQL 代码生成）

### 10.5 生成模型 / 多模态 / 基准测试

#### 10.5.1 扩散语言模型

- **Cola DLM** (arXiv:2605.06548): 连续潜在扩散语言模型
- **PAPL** (ICLR 2026 Oral): Planner Aware Path Learning 对齐训练和推断
- **ESPO** (ICLR 2026): 序列级 RL 用于扩散 LLM
- **LLaDA-V** (CVPR 2026): 视觉指令微调的扩散语言模型

#### 10.5.2 多模态进展

- **CVPR 2026 核心趋势**: 多模态 LLM 论文翻倍 (4.9% → 10.6%)
- **Perceval**: Token 级视觉过程奖励减少 VLM 幻觉
- **AgilePruner**: 自适应视觉 token 剪枝
- **Qwen-VL**: 多模态模型持续进化

#### 10.5.3 基准测试

| 基准 | 方向 | 说明 |
|------|------|------|
| ASSEBench | Agent 安全评估 | 2,293 记录, 15 风险类型, 29 场景 |
| SIMMER | Agent 规划失败检测 | 高达 56% LLM 计划包含潜在失败 |
| ClinHallu | 医学 MLLM 幻觉诊断 | 7,031 实例, 分阶段推理错误诊断 |
| BenchLM | 261 模型 × 249 基准 | 综合 LLM 排行榜 (2026 年 6 月) |
| Horizon | 用户行为建模 | 跨域长时真实用户行为 |
| DLRMv3 | 推荐基准 | MLPerf 第三代推荐系统基准 |
| GameWorld | 游戏 Agent 基准 | 34 游戏, 170 任务 |
| OffTopicEval | LLM 话题偏移 | 多轮对话一致性评估 |
| Common Corpus | 伦理数据 | 最大合规预训练数据集 |

---

## 11. 主题趋势总结

### 11.1 LLM 推理优化 (RLVR) 成为主线

- **GRPO 变体井喷**: VIMPO (无 critic)、ICT (token 级分布奖励)、分层 GRPO (ICML 2026)、MERCI (探索驱动)
- **推理时计算**: Test-Time Compute 从概念到工程实践
- **潜在推理**: 归一化流、连续扩散等非自回归推理路径

### 11.2 扩散语言模型崛起

- ICLR 2026 Oral (PAPL)、ICML 2026 (ESPO)、CVPR 2026 (LLaDA-V)
- 从"替代自回归"转向"与自回归互补"
- 关键优势: 更灵活的解码路径、潜在空间规划

### 11.3 AI Agent 系统工程化

- Agent Harness 成为独立研究方向
- 从单 Agent → 多 Agent → Agent 种群
- 长期部署 Agent 的持续学习能力 (Connect the Dots, Self-Harness)
- 安全评估走向标准化 (ASSEBench, SIMMER)

### 11.4 推荐系统: 生成式范式全面渗透

- 从判别式 → 生成式 (GenCTR, DLRMv3, TokenFactory)
- LLM Agent 驱动的模型自进化 (Self-Evolving RS)
- 多模态 → 全模态推荐 (Tencent All-Modality)
- CTR Scaling Law 成独立研究方向 (Awesome-CTR-Scaling)

### 11.5 多模态融合加速

- CVPR 2026 多模态 LLM 占比翻倍
- 扩散架构在多模态对齐中的独特优势
- 过程奖励模型改善多模态幻觉

### 11.6 评估体系重构

- 从简单基准 → 多维度 + 过程级评估
- 安全/伦理评估成为必要组成部分
- AI 辅助同行评审进入实践 (AAAI 2026)

### 11.7 主要实验室发力方向

| 实验室 | 核心方向 | 代表工作 |
|--------|---------|---------|
| Google DeepMind | AGI→ASI 路径、世界模型、多模态 | From AGI to ASI, Gemini 3.5, Self-Evolving RS |
| OpenAI | 推理模型、Agent、安全评估 | GPT-5.5, o1 家族, Deployment Simulation |
| Meta AI | 推荐 Scaling Law、开源 LLM、MoE | DLRMv3, Llama 4, Wukong |
| Microsoft Research | Agent 框架、CTR 基础模型 | Multi-Agent Filtering, Horizon Benchmark |
| Anthropic | 长上下文、安全对齐、工具使用 | Claude Opus 4.8/Mythos 5, 百万 token |
| ByteDance | 推荐系统、大规模 MoE、Doubao | RankMixer, Seed 2.0, Doubao 1.5-pro |
| Alibaba | CTR 全链路、Qwen 系列、长期 Agent | LoopCTR, EST, Qwen3.5, Connect the Dots |
| Tencent | 全模态 GR、广告系统、WeChat Agent | All-Modality GR, TokenFormer |
| NVIDIA | 推理优化、量化、GPU 系统 | FPTQuant, Nemotron 3 |
| DeepSeek | MoE 架构、推理模型、R1 系列 | DeepSeek V4, R1, 新架构探索 |

---

> **报告日期**: 2026-06-23
> **覆盖范围**: 12+ 会议/venues, 100+ 论文, 15+ 实验室
> **更新**: 持续追踪 arXiv 每日新论文
