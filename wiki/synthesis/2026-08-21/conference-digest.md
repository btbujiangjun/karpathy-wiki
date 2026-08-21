---
title: 会议与 arXiv 论文日报（2026-08-21）
title-en: Conference & arXiv Paper Daily Digest (2026-08-21)
type: synthesis
created: 2026-08-21
updated: 2026-08-21
tags: [arxiv-daily, conference-digest, ICML2026, code-world-models, agents, video-generation, time-series, benchmark]
sources: []
---

# 会议与 arXiv 论文日报（2026-08-21）

> **日期**：2026-08-21  
> **覆盖范围**：ICML 2026（含 DL4Code Workshop）/ AAAI 2026 / NeurIPS 2025 / ICLR 2026 / KDD 2026 / CVPR 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025，以及 AI、LLM、推荐系统、广告与 CTR、游戏、代码执行预测、Agent 系统、生成模型、Sequential Modeling、Benchmark 等方向的近期 arXiv 论文  
> **来源**：arXiv, OpenReview, DBLP, 各会议官网  
> **去重说明**：本期 15 篇论文均经全库检索确认未在 wiki 此前任何日报中收录，与本日 `[[arxiv-ai-search]]`、`[[arxiv-paper-check]]` 两份日报无重叠

---

## 目录

- [1. 本期概览与会议时间线](#1-本期概览与会议时间线)
- [2. ICML 2026（8/9–13 温哥华，已闭幕）](#2-icml-20268913-温哥华已闭幕)
- [3. 代码执行预测与 Code World Models](#3-代码执行预测与-code-world-models)
- [4. Agent 系统与 Agentic RL](#4-agent-系统与-agentic-rl)
- [5. 生成模型与视频生成加速](#5-生成模型与视频生成加速)
- [6. Sequential Modeling 与时间序列基准](#6-sequential-modeling-与时间序列基准)
- [7. 热门主题与趋势](#7-热门主题与趋势)
- [8. 值得关注的论文（Top Picks）](#8-值得关注的论文top-picks)

---

## 1. 本期概览与会议时间线

ICML 2026 与 KDD 2026 已于上周（8/9–13）闭幕，本期开始出现会议 Workshop 放榜后的后续产出（如 ICML 2026 DL4Code Workshop 接收论文）。本期重点：

| 方向 | 篇数 | 关键词 |
|------|------|--------|
| 代码执行预测 / Code World Models | 5 | 并行代码世界模型、执行语义鲁棒性、工业级 ICWM |
| Agent 系统与 Agentic RL | 2 | 记忆充分性路由、多时间尺度 Credit Assignment |
| 生成模型与视频生成加速 | 4 | 幅值-方向解耦、亚二次注意力蒸馏、少步蒸馏 |
| Sequential Modeling / 时间序列基准 | 3 | 十亿级工业语料基准、防泄漏评测框架、Break-even 分析 |
| ICML 2026 正式论文 | 2 | 多模态时序预测评测（主会）、隐式软件世界模型评测（Workshop） |

---

## 2. ICML 2026（8/9–13 温哥华，已闭幕）

> **状态**：主会已于 2026/8/13 闭幕；Outstanding Paper Awards（含 *The Flexibility Trap*、*High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions*）此前已在 [[conference-digest-2026-06-08]] 等页面跟踪。本期补充两篇新确认的接收论文。

### 2.1 主会论文

#### TimesX: Rethinking Multimodal Time-Series Forecasting Evaluation（重新思考多模态时间序列预测评估）

| 项目 | 内容 |
|------|------|
| 作者 | Haoxin Liu, Yichen Zhou, Rajat Sen, B. Aditya Prakash, Abhimanyu Das |
| 机构 | Georgia Institute of Technology, Google Research |
| 发表 | **ICML 2026 主会** |
| 链接 | [arXiv:2607.06973](https://arxiv.org/abs/2607.06973) |

**问题背景**：现有多模态时间序列预测（multimodal TSF）基准存在三大缺陷：(1) 数据规模小且多为合成数据，泛化性差；(2) 文本上下文类型极为有限；(3) 无法缓解数据泄漏导致的虚高评估。

**方法与创新点**：
- 构建 **TimesX** 基准：真实世界、跨域、大规模时间序列 + 细粒度文本上下文，由自动化数据生成管线产出；
- 管线采用严格 timestamp 对齐与隔离（time isolation），并设计 **hypothesizer-verifier-enricher** 框架对文本上下文做事实核查与增强；
- 基准可自动刷新（refreshable）：只需使用晚于模型预训练截止日的任务即可避免污染（默认 cutoff 2024-07-01），是首个可持续更新以评估未来预训练方法的多模态 TSF 基准。

**实验结果**：开展超过 **31.2 万次独立 LLM inference** 的实证研究。关键发现：
- 早期合成基准**严重高估** LLM 相对 TSF 模型的能力——合成上下文恰好提供了改进预测所需的全部信息，而真实上下文过于微妙；
- Agentic 方法（CodeRev：LLM 写代码修订 TFM 预测）表现反而**劣于其单独组件**，推翻了先前基准上的结论；
- 简单 ensemble 最强：`AvgEns(TimesFM-2.5 + Gemini-2.0-Flash)` 取得 MASE **0.619**（第 1）、CRPS **4.249**（第 1）。

**对比先前方法**：与既有基准相比，TimesX 在真实数据规模、上下文多样性、防泄漏机制三个维度全面升级；结论层面直接修正了"LLM 预测强于专用 TSF 模型""agentic 修订优于简单集成"两个流行叙事。

### 2.2 Workshop 论文（DL4Code @ ICML 2026）

#### Towards Evaluation of Implicit Software World Models in Coding LLMs（编码 LLM 中隐式软件世界模型的评估）

| 项目 | 内容 |
|------|------|
| 作者 | Egor Bogomolov, Yaroslav Zharov |
| 机构 | JetBrains Research |
| 发表 | **ICML 2026 DL4Code Workshop** |
| 链接 | [arXiv:2606.27406](https://arxiv.org/abs/2606.27406) |

**问题背景**：软件工程（无论人类还是 AI agent 执行）都要求对软件行为的推理能力。作者将支撑这种推理的内部模型称为 **software world model**，并指出当前代码执行基准只覆盖了其中一个被充分研究的切片——control flow。

**方法与创新点**：将可观测轴从 control flow 扩展到**执行资源（execution resources）**：除测试结果与异常类型外，同时预测峰值内存、wall-clock 耗时、以及 method/line 粒度的排序 profiler 输出。数据源采用 **SWE-bench Verified**，使测试贴近真实软件工程任务。

**实验结果**：所有受测模型（包括 frontier 模型）均表现平平且行为脆弱，表明模型对"软件如何被执行"的理解显著欠缺——与其"源码如何书写"的能力形成反差。

**对比先前方法**：此前的 CRUXEval 类基准聚焦输出预测（control flow 切片）；本文首次将执行资源维度纳入 software world model 评测体系，与本期 [§3](#3-代码执行预测与-code-world-models) 的执行语义鲁棒性研究形成互补视角。

---

## 3. 代码执行预测与 Code World Models

> 本期该方向集中爆发 5 篇，覆盖训练（PCWM、InCoder）、诊断（Debugging CWM）、鲁棒性评测（Execution Semantics）与隐式世界模型评测（见 §2.2），标志 "Code World Models" 正在成型为一个独立研究方向。

### 3.1 PCWM: Learning Reasoning World Models for Parallel Code（面向并行代码的推理世界模型学习）

| 项目 | 内容 |
|------|------|
| 作者 | Gautam Singh, Arjun Guha, Bhavya Kailkhura, Harshitha Menon |
| 机构 | UMass Amherst, Lawrence Livermore National Laboratory (LLNL) |
| 发表 | arXiv preprint (v3) |
| 链接 | [arXiv:2604.20926](https://arxiv.org/abs/2604.20926) |

**问题背景**：LLM 在串行代码生成上表现出色，但在并行代码上挣扎——训练数据相对稀缺。常见补救是让 coding agent 与外部工具交互（如运行 race detector、profiler），但工具调用成本高，且对部分写成的代码常常不可行。

**方法与创新点**：
- 提出 **Parallel-Code World Models (PCWM)**：推理型 LLM 直接从并行源码预测工具输出（data race 结果、性能 profile），把外部工具交互内化为内部模拟；
- 设计新颖的探索式数据生成管线：跨多个领域采样多样化并行编码问题与候选实现，通过工具执行记录 data race 与性能 profile，再合成**因果连接源码与观测工具输出的 reasoning trace**；
- 在合成数据上微调得到具备"预测-验证"能力的推理世界模型。

**实验结果**：
- 7B 世界模型 race-outcome prediction 准确率 **64.3% → 72.8%**；
- 8B 模型性能剖析（performance profiling）任务准确率 **49.3% → 58.6%**；
- 下游应用：用 PCWM 辅助修复 data race，7B 模型带来 **2.7%–9.1%** 提升，14B 模型带来 **6.1%–11.1%** 提升。

**对比先前方法**：与依赖外部工具的 coding agent 相比，PCWM 免去昂贵且常不可行的工具调用；与通用代码 LLM 相比，其显式建模了"代码 → 运行时行为"的因果动力学。

### 3.2 Debugging Code World Models（调试代码世界模型）

| 项目 | 内容 |
|------|------|
| 作者 | Babak Rahmani（独立作者） |
| 机构 | 未标注（单作者，会议审稿中） |
| 发表 | arXiv preprint (v2, under review) |
| 链接 | [arXiv:2602.07672](https://arxiv.org/abs/2602.07672) |

**问题背景**：Code World Models（CWM，如 Meta 开创的逐命令预测显式运行时状态的范式）通过 execution-based world modeling 实现模型内部验证，作为自然语言 chain-of-thought 的替代。但其错误来源与局限本质仍不清楚。

**方法与创新点**：从**局部语义执行**与**长程状态追踪**两个互补视角系统诊断 CWM，在真实代码基准上识别出两大失败模式：
1. 密集运行时状态产生 token 密集的执行轨迹，导致长执行历史程序的 **token 预算耗尽**；
2. 失败不成比例地集中在**字符串值状态**上，归因于 subword tokenization 的局限而非程序结构本身。

进一步构造受控的 permutation-tracking 基准隔离"动作执行下的状态传播"，证明长程退化主要由不正确的状态传播驱动。

**对比先前方法**：先前工作主要展示 CWM 的能力上限，本文首次给出失败模式的系统性分类学，为后续架构改进（如状态表示压缩、tokenization 方案）提供靶点。

### 3.3 InCoder-32B-Thinking: Industrial Code World Model for Thinking（工业级思考型代码世界模型）

| 项目 | 内容 |
|------|------|
| 作者 | Jian Yang, Wei Zhang, Jiajun Wu, Junhang Cheng, Tuney Zheng, Fanglin Xu, Weicheng Gu, Lin Jing, Yaxin Du, Joseph Li, Yizhi Li, Yan Xing, Chuan Hao, Ran Tao, Ruihao Gong, Aishan Liu, Zhoujun Li, Mingjie Tang, Chenghua Lin, Siheng Chen, Wayne Xin Zhao, Xianglong Liu, Ming Zhou, Bryan Dai, Weifeng Lv 等 |
| 机构 | 国内高校与企业联合团队（含北京航空航天大学、中国人民大学等背景作者，据作者名单推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2604.03144](https://arxiv.org/abs/2604.03144) |

**问题背景**：芯片设计、GPU 优化、嵌入式系统等工业软件开发中，缺少展示工程师如何围绕硬件约束与时序语义进行推理的专家 reasoning trace。

**方法与创新点**：
- 提出 **ECoT（Error-driven Chain-of-Thought）** 合成框架：通过与环境的错误反馈多轮对话合成思考内容，显式建模纠错过程；
- 训练 **ICWM（Industrial Code World Model）**：在 Verilog 仿真、GPU profiling 等领域特定执行轨迹上学习"代码如何影响硬件行为"的因果动力学，支持在实际编译前预测执行结果实现自我验证；
- 所有合成 reasoning trace 经领域工具链验证，使训练数据的推理深度分布匹配工业任务的自然分布。

**实验结果**：在 **14 个通用基准 + 9 个工业基准**上评估，LiveCodeBench v5 达到 **81.3%**。

**对比先前方法**：通用代码思维链数据缺乏硬件约束语义；ECoT+ICWM 将世界模型的"预测执行结果"能力注入工业场景（Verilog/GPU/嵌入式），填补了通用 CWM 工作（如 §3.1、§3.2）未覆盖的硬件相关执行语义空白。

### 3.4 How Robustly do LLMs Understand Execution Semantics?（LLM 对执行语义的理解有多鲁棒？）

| 项目 | 内容 |
|------|------|
| 作者 | Claudio Spiess, Prem Devanbu, Earl T. Barr |
| 机构 | University of California Davis, University College London (UCL) |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2604.16320](https://arxiv.org/abs/2604.16320) |

**问题背景**：LLM 展现出卓越推理能力，但其究竟依赖内部世界模型还是精巧的模式匹配仍是开放问题。作者以标准 program-output prediction 任务为透镜，研究代码理解的**鲁棒性**。

**方法与创新点**：在 CRUXEval 式的程序输出预测任务上施加代码变换与输入扰动，测量准确率稳定性；并针对异常（exception）预测设计补救方案实验。

**实验结果**（核心发现）：
- 开源推理模型（DeepSeek-R1 系列）在扰动下保持稳定但整体较低的准确率（**38%–67%**）；
- frontier 模型 **GPT-5.2 表现出显著脆弱性**：原始无扰动 CRUXEval 上近乎满分（**99%**），扰动输入下准确率下降 **20–24 个百分点**；
- 多数模型在预测"会抛异常的扰动输入"的行为时表现差得多，且性能依赖于异常类型；
- 所研究的补救措施可改善异常预测，作者同时评估其对非异常行为预测的影响。

**对比先前方法**：与 §2.2（JetBrains，资源维度）不同，本文从**扰动鲁棒性**维度切入，两者共同指向同一结论：模型对执行语义的掌握远不如其对代码表面模式的拟合，为"pattern matching vs world model"之争提供了新证据。

---

## 4. Agent 系统与 Agentic RL

### 4.1 Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents（Router-Mem：证据充分即停止的渐进式执行框架）

| 项目 | 内容 |
|------|------|
| 作者 | Yidan Lin, Kaixiang Wang, Jiong Lou, Jie Li |
| 机构 | 浙江大学（据作者团队推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.01285](https://arxiv.org/abs/2608.01285) |

**问题背景**：LLM 向持久化、自适应智能发展，越来越需要跨交互保存与复用信息的长期记忆机制。现有两类方案各有短板：压缩结构化历史类系统在线成本低但可能遗漏时序/因果/跨步依赖；对完整轨迹做深度研究的系统证据覆盖好但延迟与推理成本高。

**方法与创新点**：提出 **Router-Mem**，一个 evidence-conditioned progressive execution 框架：
1. 先执行共享的低成本检索前缀获取证据；
2. 轻量级 sufficiency router 预测当前上下文是否足以回答，若是则**单 token 决策提前终止**；
3. router 以 evidence-level 监督 + rationale-conditioned 表示蒸馏训练；
4. 证据不足时才升级到更深的检索/研究流程。

**对比先前方法**：在"低成本压缩派"与"高成本深研派"之间引入按需分层的中间路径，以单 token 路由决策实现在保证答案质量的同时压低在线延迟——与 wiki 已收录的 LongHorizon-Harness、SINKFLEX-RL 等 harness 侧优化形成互补（前者优化执行脚手架，本篇优化记忆访问策略）。

### 4.2 Learning from Environmental Feedback: Credit Assignment across Multiple Timescales for Agentic RL（EFCA：基于环境反馈的多时间尺度 Credit Assignment）

| 项目 | 内容 |
|------|------|
| 作者 | Yifu Huo, Shunjie Xing, Chenglong Wang, Peinan Feng, Qiaozhi He, Yan Ding, Anxiang Ma, Yuxin Gao, Tongran Liu, Tong Xiao, Jingbo Zhu |
| 机构 | 东北大学 / NiuTrans |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.08255](https://arxiv.org/abs/2608.08255) |

**问题背景**：Agentic RL 在真实环境中普遍遭受**延迟且稀疏的奖励**。Credit assignment 旨在分解轨迹级奖励、为中间决策提供细粒度监督，但现有方法忽略了环境交互过程中天然产生的丰富过程信息（如交互历史）。

**方法与创新点**：提出 **Environmental Feedback-based Credit Assignment (EFCA)**，用两条直接从环境反馈中提取的过程信号补充长期结果信号：
- **短期反馈信号**：捕捉当前动作的即时效果；
- **中期状态-历史信号**：从近期交互中识别无效模式；
两路信号通过 return 重加权整合进 RL 目标，构成短/中/长三个时间尺度的信用分配体系。

**对比先前方法**：先前 credit assignment（如 step-level reward model、hindsight 方法）依赖额外模型或人工标注；EFCA 的信号完全来自环境自身反馈，无需额外监督源，更适合奖励稀疏的真实 agent 环境。与 wiki 已收录的 VeRO、SSR-GRPO 同属 agentic RL 训练信号设计路线，差异在于本篇的多时间尺度分解视角。

---

## 5. 生成模型与视频生成加速

> 本期 4 篇覆盖视频生成加速的三条技术路线：轨迹偏差校正（MDD）、注意力复杂度优化（SQuad）、少步蒸馏（TMD），以及统一音视频生成（Vorch-Omni）。

### 5.1 Magnitude-Direction Decoupling for Fast Video Generation with Flow Matching Models（MDD：面向快速视频生成的幅值-方向解耦）

| 项目 | 内容 |
|------|------|
| 作者 | Haonan Xu, Feiyang Chen, Songkui Chen, Hongpeng Pan, Zhefeng Wang, Xinyu Duan, Baoxing Huai, Yang Yang |
| 机构 | 未标注（企业界团队风格） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.17695](https://arxiv.org/abs/2608.17695) |

**问题背景**：Flow matching 视频生成模型因迭代去噪计算开销巨大。原模型并非每一步去噪都必要——部分步骤可用轻量替代以加速采样；但直接使用缓存或轻量模型会偏离原始去噪轨迹，导致次优质量。

**方法与创新点**：经验分析发现关键规律——**轻量模型能稳健捕捉原模型输出的幅值（magnitude）分量，而缓存能提供可靠的方向（direction）指引**。据此提出 **Magnitude-Direction Decoupling (MDD)**：
- 自适应地用"方向校准过的轻量模型"替代原模型进行推理，有效纠正去噪轨迹偏差；
- 进一步在 classifier-free guidance (CFG) 下复用幅值信息，再度降低推理成本。

**实验结果**：在 **Wan2.1** 上取得最高 **2.95× 加速**（单卡实测，质量保持）。

**对比先前方法**：纯缓存方法（如 TeaCache 类）与纯轻量化蒸馏各自都会造成轨迹偏移；MDD 的解耦视角将两者的优势分量正交组合，是缓存-蒸馏混合加速路线的新代表。

### 5.2 SQuad: Sub-Quadratic Attention Distillation for Efficient Video Generation（SQuad：面向高效视频生成的亚二次注意力蒸馏）

| 项目 | 内容 |
|------|------|
| 作者 | Animesh Karnewar, Denis Korzhenkov, Amirhossein Habibian, Mohsen Ghafoorian |
| 机构 | Qualcomm AI Research（据作者团队推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.16585](https://arxiv.org/abs/2608.16585) |

**问题背景**：Video Diffusion Transformer (DiT) 的算力大头在 Self-Attention，其代价随 latent token 数 n 二次增长 O(n²)。视频生成 token 数极大，该项主导运行时与显存，直接封顶可生成的分辨率与时长。线性 O(n) 与低秩 O(nk) 替代核虽便宜，但很少能恢复原始 softmax 注意力的表达力，留下顽固的质量差距。

**方法与创新点**：提出 **SQuad**，将蒸馏后注意力的复杂度定在 **O(n√n)**，在效率-表达力权衡上取自然平衡点。不从零训练 Video DiT（代价过高），而是把预训练的全 softmax Self-Attention DiT 蒸馏适配进 SQuad-Attention，分两阶段：
1. **Flow-Matching Supervised Fine-Tuning (SFT)**；
2. 改进的分布匹配（distribution matching）阶段。

**对比先前方法**：相较线性注意力/低秩近似"换核丢表达力"的老路，SQuad 用蒸馏保表达力、用 √n 因子控复杂度，为长时长高分辨率视频 DiT 提供了介于全注意力和线性注意力之间的第三选择。

### 5.3 Transition Matching Distillation for Fast Video Generation（TMD：面向快速视频生成的转移匹配蒸馏）

| 项目 | 内容 |
|------|------|
| 作者 | Weili Nie, Julius Berner, Nanye Ma, Chao Liu, Saining Xie, Arash Vahdat |
| 机构 | NVIDIA, New York University |
| 发表 | arXiv preprint (v2) |
| 链接 | [arXiv:2601.09881](https://arxiv.org/abs/2601.09881) |

**问题背景**：大型视频 diffusion/flow 模型在高保真生成上成就卓著，但低效的多步采样使其难以进入实时交互应用。

**方法与创新点**：提出 **Transition Matching Distillation (TMD)** 蒸馏框架，核心思想是将扩散模型的多步去噪轨迹匹配为一个**少步概率转移过程**，每次转移建模为轻量的 conditional flow。为实现高效蒸馏，将原始扩散骨干分解为两部分：
1. **main backbone**（占绝大多数早期层）：在每个外层转移步提取语义表示；
2. **flow head**（最后几层）：利用这些表示执行多次内层 flow 更新。

训练流程：给预训练视频 flow 模型加装 flow head → 适配为 conditional flow map → 施加蒸馏。

**对比先前方法**：与一致性模型/distribution matching distillation 等少步化方案相比，TMD 的 backbone-flow head 分解让内层多次 flow 更新复用外层语义表示，在极少步数下逼近多步教师质量；定位明确指向实时交互式视频应用，与 wiki 已收录的 NVIDIA 系加速工作（GalaxyDiT 训练无关加速）形成"训练时蒸馏 vs 推理时加速"的互补。

### 5.4 Vorch-Omni: Multi-Task Orchestration of Sight and Sound（Vorch-Omni：视觉与声音的多任务编排）

| 项目 | 内容 |
|------|------|
| 作者 | Vorch Team 及 Xiaoyu Chen, Yang Ding, Cong Han, Menglin Han, Yuxin Hong, Jiebo Hou, Zequn Jie, Xiang Li, Jing Liu, Qi Liu, Yulei Lu, Siyuan Luo, Lin Ma, Xin Ma, Yinlong Qian, Peng Shi, Fang Wan, Siqi Wang, Yaohui Wang, Yaole Wang, Yidi Wu, Siqian Yang, Mingyu Yin, Haoran Yu, Gang Yue, Lisai Zhang, Yuting Zhang 等 |
| 机构 | Vorch Team（团队署名，Lin Ma 在列） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.05803](https://arxiv.org/abs/2608.05803) |

**问题背景**：生成式视频建模已支持多样生成、参考引导合成、扩展与编辑，但现有方法依赖碎片化的任务专用模型。通用模型必须区分异构的 target、source、reference 信号以决定"生成什么、保留什么、用什么做引导"，同时抑制任务间干扰；联合音视频生成又叠加了跨模态的多样条件与输出配置。

**方法与创新点**：提出 **Vorch-Omni**，基于 **arbitrary-condition-to-arbitrary-output** 形式的统一多任务音视频合成框架：
- 视频/音频信号可灵活充当条件输入或生成目标；
- **token 级条件掩码 + 任务标识符**区分目标、源内容与参考；
- **位置类型**分离时序上下文与独立条件；
- 采用互补的视觉条件通路：由 vision-language model 解读语义、另一通路保留结构信息（摘要截断处）。

**对比先前方法**：相较每个任务一个模型的传统做法（文生视频、视频续写、参考驱动编辑、音视频联合生成各自为政），Vorch-Omni 用单一模型统一编排，是继 wiki 已收录 OneModel（小红书，推荐域统一模型）之后又一"one model for all tasks"理念在生成域的落地。

---

## 6. Sequential Modeling 与时间序列基准

> 本期 3 篇与 §2.1 TimesX 共同勾勒出时间序列评测的"新一代范式"：数据新鲜度、防泄漏、regime-aware、部署决策导向。工业界（蚂蚁集团、Google）深度参与。

### 6.1 QuitoBench: A High-Quality Open Time Series Forecasting Benchmark（QuitoBench：高质量开放时间序列预测基准）

| 项目 | 内容 |
|------|------|
| 作者 | Siqiao Xue, Zhaoyang Zhu, Wei Zhang, Rongyao Cai, Rui Wang, Yixiang Mu, Fan Zhou, Jianguo Li, Peng Di, Hang Yu |
| 机构 | Ant Group（支付宝） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2603.26017](https://arxiv.org/abs/2603.26017) · [项目页](https://hq-bench.github.io/quito/) |

**问题背景**：时间序列预测横跨金融、医疗、云计算，但进展受制于根本瓶颈：缺乏大规模、高质量基准。现有基准多以应用定义的领域标签组织，无法刻画与预测真正相关的数据性质。

**方法与创新点**：
- 构建十亿级（billion-scale）时间序列语料库 **Quito**：来自支付宝应用流量，横跨 9 个业务领域；
- 在其上构建 **regime-balanced** 基准，覆盖 trend × seasonality × forecastability 八种 **TSF regime**，以预测相关性质而非应用标签组织评测；
- 对来自深度学习、foundation model、统计基线的 **10 个模型**在 **232,200 个评测实例**上密集滚动评测（约 1.6×10⁷ 次预测/模型）。

**实验结果**（四大发现）：
1. **Context-length crossover**：短上下文（L=96）深度学习模型领先 24.6%，长上下文（L≥576）foundation model 反超并在 L=1024 时领先 22.0%——历史长度是模型选型的首要因素；
2. **Forecastability 是主导难度轴**：跨 regime MAE 差距达 **3.64×**；
3. **参数效率**：深度学习模型以 **59× 更少的参数**追平或超越 foundation model（CrossFormer ~1M 参数、MAE 0.279 全面第一，优于 Chronos-2 ~100M 参数）；
4. **数据规模 > 模型规模**：两个家族中增加训练数据的收益都远大于增大模型。

**对比先前方法**：与 GIFT-Eval 等既有基准相比，QuitoBench 以全新工业数据杜绝信息泄漏，并以 regime 维度取代领域标签维度；给出的选型指南（短上下文/资源受限用紧凑 DL 模型，L≥576 且强季节性用 Chronos-2 类 FM）具有直接工程价值。

### 6.2 TempusBench: An Evaluation Framework for Time-Series Forecasting（TempusBench：时间序列预测评估框架）

| 项目 | 内容 |
|------|------|
| 作者 | Denizalp Goktas, Gerardo Riaño-Briceño, Alif Abdullah, Aryan Nair, Chenkai Shen, Beatriz de Lucio, Alexandra Magnusson, Farhan Mashrur, Ahmed Abdulla, Shawrna Sen, Mahitha Thippireddy, Gregory Schwartz, Amy Greenwald 等 |
| 机构 | Brown University |
| 发表 | arXiv preprint (v2, workshop version) |
| 链接 | [arXiv:2604.11529](https://arxiv.org/abs/2604.11529) |

**问题背景**：TSFM 领域缺乏社区公认的评估框架，四大痛点：(1) 基准数据陈旧（如 M3）且与 TSFM 预训练语料重叠，零样本泛化被高估；(2) 任务轴狭窄（仅 horizon/domain），忽略平稳性、季节性等核心统计性质；(3) 对 XGBoost 等领域模型缺乏统一的超参调优约定，比较不公平；(4) 缺乏可视化解释工具。

**方法与创新点**：开源评估框架 TempusBench 四大组件：
1. 不在任何现有 TSFM 预训练语料中的全新数据集；
2. 超越 horizon/frequency/domain 的新任务类型：平稳性、季节性形态、变量类型（连续/计数/二值/类别）、稀疏性、噪声质量等；
3. 标准化自动化超参搜索管线：滚动窗口内调参、下一窗口测试，严格保持时序顺序、避免 look-ahead bias；
4. TensorBoard 可视化界面。内置 **20 个预测模型**（含此前从未被纳入评估框架的 XGBoost）。

**对比先前方法**：GIFT-Eval 曾被发现除 Moirai2 外所有受评 TSFM 的测试数据都在其预训练语料中；TempusBench 从数据新鲜度、统计性质任务轴、公平调优三方面系统性回应，并规划动态刷新基准（合成周期性测试 + 自然更新的真实数据流）。与 QuitoBench（工业语料路线）、TimesX（多模态路线）互为补充。

### 6.3 When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters（基础模型何时回本？预训练时间序列预测器的 Break-even 分析）

| 项目 | 内容 |
|------|------|
| 作者 | Nicholas Tan Jerome, Frank Simon |
| 机构 | 未标注 |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2607.04919](https://arxiv.org/abs/2607.04919) · [代码](https://github.com/nicolaisi/fm-breakeven) |

**问题背景**：部署时间序列 foundation model 需要 GPU 基础设施与工程开销，且不保证胜过 XGBoost。何时这笔投资划算？此前没有系统性答案。

**方法与创新点**：首个系统性 **break-even 分析**：30 个基准数据集 × 6 个训练集规模档位（2%–100%）× foundation model（Chronos、Moirai、Lag-Llama 的 zero-shot 与 LoRA 微调）vs 经典基线（Naive、ETS、ARIMA、XGBoost），共 **10,800 个实验配置**。将数据集划分为 FM-dominant / early / mid / late break-even 四类，并提出无需训练的两步部署决策框架。

**实验结果**：
- **15/30 数据集为 FM-dominant**：zero-shot FM 在所有训练比例下都胜过经典方法，GPU 部署无条件合理；
- **6 个数据集 early break-even**：经典方法仅需 2% 训练数据（21–2,768 样本）即反超 zero-shot FM；
- 其余 9 个 break-even 点分布在 24–8,361 样本之间；
- 一条稳健免训练规则：若 `n_train < 700` 且季节性不可忽略（S≥0.05），直接用 FM zero-shot、跳过微调——可立即解决 10/30 的部署决策；
- **LoRA 微调可能适得其反**：短序列上主动降低性能（如 ILI 数据集 MASE 从 2.472 恶化至 2.766）；
- XGBoost 是强劲对手：30 个数据集中的 14 个在全量数据下取得经典方法最佳成绩。

**对比先前方法**：先前 FM-vs-classical 比较多为固定数据规模的排行榜式评测；本文引入经济学 break-even 视角，结论是"FM 优势并非普适而是高度依赖数据集性质与数据量"，为业界提供了可操作的决策规则，与 QuitoBench 的参数效率发现（59× 参数差距）相互印证。

---

## 7. 热门主题与趋势

### 7.1 本期趋势

| 趋势方向 | 代表论文 | 说明 |
|---------|---------|------|
| **Code World Models 成型为独立方向** | PCWM, Debugging CWM, InCoder-32B-Thinking, Execution Semantics, Implicit SWM (ICML WS) | 训练、诊断、评测、工业化四条线同周齐发；"执行语义理解"正在取代"代码生成"成为新的能力评测轴心 |
| **执行语义评测双轴展开** | Implicit SWM（资源轴：内存/耗时/profiler）, Execution Semantics（鲁棒性轴：扰动稳定性） | JetBrains 与 UC Davis/UCL 从不同维度得出一致结论：frontier 模型懂代码写法、不懂代码执行 |
| **视频生成加速三线合流** | TMD（蒸馏）, SQuad（注意力复杂度）, MDD（轨迹偏差校正） | 少步化、亚二次注意力、缓存-轻量混合三种路线并行推进，目标共同指向实时交互应用 |
| **时间序列评测范式换代** | TimesX (ICML 2026), QuitoBench, TempusBench, Break-even | 共同关键词：数据新鲜度、防泄漏、regime-aware、部署决策；工业界（蚂蚁、Google）主导数据供给 |
| **Agentic RL 信号精细化** | EFCA（多时间尺度环境反馈）, Router-Mem（记忆充分性路由） | 从"更多数据/更大模型"转向"更精细的训练信号与更低成本的运行时决策" |

### 7.2 Top Labs 动向

| 机构 | 本期动作 |
|------|---------|
| **NVIDIA** | TMD 少步视频蒸馏（与 NYU 合作），延续其在生成模型加速上的布局 |
| **Google Research** | TimesX（ICML 2026 主会）主导多模态时序预测评测标准 |
| **Ant Group / 支付宝** | QuitoBench 开放十亿级工业时序语料，输出 regime-aware 选型指南 |
| **JetBrains Research** | 将 software world model 评测推入 ICML 2026 DL4Code Workshop |
| **Qualcomm AI Research** | SQuad 亚二次注意力蒸馏，端侧视频生成效率路线 |
| **东北大学/NiuTrans** | EFCA 多时间尺度 credit assignment 进入 agentic RL 前沿 |

---

## 8. 值得关注的论文（Top Picks）

### 🏆 本日精选

| # | 论文标题 | 方向 | 核心贡献 |
|---|---------|------|---------|
| 1 | **PCWM: Learning Reasoning World Models for Parallel Code** | 代码世界模型 | 首个并行代码世界模型：race 预测 64.3%→72.8%，下游 race 修复提升最高 11.1%，将昂贵工具调用内化为内部模拟 |
| 2 | **TimesX: Rethinking Multimodal Time-Series Forecasting Evaluation** | ICML 2026 / Benchmark | 修正多模态 TSF 评测范式：31.2 万次 inference 证明简单 ensemble 胜过 agentic 方案，合成基准严重高估 LLM |
| 3 | **How Robustly do LLMs Understand Execution Semantics?** | 代码理解评测 | GPT-5.2 在 CRUXEval 近满分但扰动下暴跌 20–24pp，为"pattern matching vs world model"之争提供关键证据 |
| 4 | **InCoder-32B-Thinking** | 工业代码世界模型 | ECoT+ICWM 将世界模型带入 Verilog/GPU/嵌入式工业场景，LiveCodeBench v5 81.3% |
| 5 | **EFCA: Environmental Feedback-based Credit Assignment** | Agentic RL | 短/中/长三时间尺度信用分配，过程信号全部取自环境反馈、零额外监督 |
| 6 | **TMD: Transition Matching Distillation** | 视频生成加速 | NVIDIA backbone+flow head 分解蒸馏，少步生成剑指实时交互应用 |
| 7 | **QuitoBench** | 时间序列基准 | 十亿级支付宝语料 + 8 regime 平衡设计；context-length crossover 与 59× 参数效率两大实用发现 |
| 8 | **When Do Foundation Models Pay Off?** | 时间序列部署决策 | 首个 FM-vs-classical break-even 分析（10,800 配置），给出免训练部署决策规则 |

---

> **维护者注**：本报告数据来源于 arXiv、OpenReview、DBLP、各会议官网。部分机构标注为据作者名单推断（已注明），正式版本可能有所不同。所有论文均经全库查重确认首次收录。
