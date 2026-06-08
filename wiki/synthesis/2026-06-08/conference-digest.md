---
title: 顶会论文专题报告 — 2026年6月全面版（ICML / AAAI / NeurIPS / ICLR / KDD / CVPR / ACL / EMNLP / SIGIR / WWW / CIKM / RecSys）
type: synthesis
created: 2026-06-08
updated: 2026-06-08
sources:
  - ICML 2026 Proceedings
  - AAAI 2026 Proceedings
  - NeurIPS 2025 Proceedings
  - ICLR 2026 Proceedings
  - KDD 2026 Proceedings
  - CVPR 2026 Proceedings
  - ACL 2026
  - EMNLP 2025 Proceedings
  - SIGIR 2026 Proceedings
  - WWW 2026 Proceedings
  - CIKM 2025
  - RecSys 2025
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, agents, ctr, recommendation, generative-models, reasoning]
---

# 顶会论文专题报告 — 2026年6月全面版

> 覆盖 ICML 2026・AAAI 2026・NeurIPS 2025・ICLR 2026・KDD 2026・CVPR 2026・ACL 2026・EMNLP 2025・SIGIR 2026・WWW 2026・CIKM 2025・RecSys 2025 共 12 个会议 + 各大工业实验室最新论文。2026-06-08 更新。

**目录**
1. [概述与宏观趋势](#1-概述与宏观趋势)
2. [NeurIPS 2025 最佳论文深度解读](#2-neurips-2025-最佳论文深度解读)
3. [ICLR 2026 亮点论文](#3-iclr-2026-亮点论文)
4. [ICML 2026 亮点论文](#4-icml-2026-亮点论文)
5. [AAAI 2026 亮点论文](#5-aaai-2026-亮点论文)
6. [CVPR 2026 亮点论文](#6-cvpr-2026-亮点论文)
7. [EMNLP 2025 亮点论文](#7-emnlp-2025-亮点论文)
8. [KDD 2026 亮点论文](#8-kdd-2026-亮点论文)
9. [推荐系统/CTR/广告（SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025）](#9-推荐系统ctr广告sigir-2026--www-2026--cikm-2025--recsys-2025)
10. [各大实验室重点论文](#10-各大实验室重点论文)
11. [智能体/Agent 系统](#11-智能体agent-系统)
12. [生成模型与多模态](#12-生成模型与多模态)
13. [代码/推理/数学](#13-代码推理数学)
14. [游戏与强化学习](#14-游戏与强化学习)
15. [总结与展望](#15-总结与展望)

---

## 1. 概述与宏观趋势

2026 年上半年 AI 研究仍然高速推进，各顶级会议接收论文数量持续增长：

| 会议 | 提交数 | 接收数 | 接收率 | 举办时间 |
|------|--------|--------|--------|----------|
| ICML 2026 | 23,918 | 6,352 | 26.6% | Jul 6–11, Seoul |
| CVPR 2026 | 16,092 | 4,089 | ~25% | Jun 2026, Denver |
| NeurIPS 2025 | 21,575 | ~5,200 | 24.5% | Dec 2025, San Diego |
| ICLR 2026 | 12,000+ | ~2,500 | ~21% | Apr 2026 |
| AAAI 2026 | 29,000+ | ~3,700 | ~12.7% | Feb 2026 |
| EMNLP 2025 | 8,174 | 1,811 (Main) | 22.16% | Nov 2025, Suzhou |
| KDD 2026 | — | — | — | Aug 2026, Jeju |
| SIGIR 2026 | — | — | — | Jul 2026, Melbourne |
| WWW 2026 | — | — | — | May 2026 |

**六大宏观趋势**

1. **Diffusion LLM 崛起**：扩散语言模型（dLLM）在 ICML 2026 和 ICLR 2026 爆发，出现多个 Oral 论文讨论 unmasking policy、flexibility trap、最大似然 RL 等核心问题。LLaDA 等从零训练的扩散 LM 挑战了自回归范式的垄断地位。

2. **RLVR 反思与深化**：NeurIPS 2025 Runner-Up 论文质疑 RLVR 是否真正扩展了推理能力（答案：没有，RLVR 只是在基座模型能力范围内提高了采样效率）。ICML 2026 则涌现 MaxRL、GDPO、GRPO 变体等新方法。

3. **Agent 系统成熟化**：从单智能体推理到多智能体协作、Agentic RL、持续学习。ICLR 2026 出现 AgentFlow（7B 击败 GPT-4o）、MetaClaw（持续元学习）、GrandCode（Codeforces 三连冠）等里程碑。

4. **推荐/CTR 大模型化**：ByteDance 的 TokenMixer-Large（7B）/HyFormer、Kuaishou 的 Taiji/UniMixer/GR4AD/OneMall、JD 的 GenRec 都将推荐模型推向 LLM 规模。生成式推荐（Generative Recommendation）成为工业界主流范式。

5. **推理模型成为标配**：Chain-of-Thought + RL post-training 成为各大模型的默认方案。SABER（AAAI 2026）提出可控制推理深度的训练框架。GrandCode 在 Codeforces 击败所有人类选手。

6. **多模态融合加速**：UniAR（ICML 2026）实现统一的自回归多模态框架。CVPR 2026 涌现大量 VLMs 强化学习工作。Molmo2 在视频 grounding 上超越 Gemini 2.5 Pro。

---

## 2. NeurIPS 2025 最佳论文深度解读

NeurIPS 2025（San Diego + Mexico City，Dec 2025）接收 ~5,200 篇论文。以下是获奖论文详细分析：

### 2.1 Best Paper: Gated Attention for Large Language Models

**Title**: Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
**Authors**: Zihan Qiu et al. (Industry lab)
**Links**: https://neurips.cc/virtual/2025/poster/120216

**背景**: Transformers 的 softmax attention 长期以来是 LLM 的核心组件，但其低秩特性限制了表达能力。门控机制在 LSTM、Highway Networks、SSM、linear attention 中都有使用，但在 softmax attention 中的系统研究缺失。

**核心发现**: 在 Scaled Dot-Product Attention (SDPA) 之后添加一个 head-specific sigmoid gate 可以：
- 引入非线性：SDPA 的输出经过低秩映射（因 softmax 的秩通常很低），gate 增加额外的非线性
- 引入稀疏性：query-dependent sparse gating scores 动态调制 SDPA 输出
- 消除 attention sink：gate 自然抑制无用信号

**实验**: 在 30 种变体、15B MoE 模型和 1.7B dense 模型上训练 3.5T token。简单 sigmoid gate 一致提升性能、训练稳定性和长上下文外推能力。

**影响**: 作为 2025 年最具影响力的 LLM 架构改进之一，gated attention 已被多个后续模型采用（如 DeepSeek V4、Qwen3.5 等）。

### 2.2 Best Paper: Artificial Hivemind

**Title**: Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
**Links**: https://neurips.cc/virtual/2025/poster/121421

**背景**: 随着 LLM 广泛使用，模型输出的多样性问题日益突出——不同模型对相同开放式问题往往给出惊人相似的答案。

**核心贡献**: 
- 发布 Infinity-Chat 数据集（26K 开放式用户查询，6 大类 17 子类）
- 首次系统性度量 LM 的 mode collapse
- 揭示 Artificial Hivemind 效应：intra-model repetition、inter-model homogeneity

**影响**: 这项研究引发了关于 AI 对人类思维长期同质化影响的广泛讨论。

### 2.3 Best Paper: Why Diffusion Models Don't Memorize

**Title**: Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training
**Links**: https://neurips.cc/virtual/2025/poster/119372

**核心发现**: 扩散模型在训练中经历"早期好样本 → 后期记忆"两个阶段。更大的数据集会加宽 "generalization window"，推迟过拟合。隐式动态正则化是核心机制。

**理论意义**: 从动力学角度解释了扩散模型为何不易记忆训练数据，为版权和安全评估提供了理论基础。

### 2.4 Best Paper: 1000 Layer Networks for Self-Supervised RL

**Title**: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
**Links**: https://neurips.cc/virtual/2025/poster/115731

**核心发现**: 将 RL 模型深度扩展到 1024 层，在自监督目标条件设置中（无演示、无奖励），性能提升 2×–50×。深度不仅提高成功率，还定性地改变智能体行为。

### 2.5 Best Paper (DB Track): Superposition Yields Robust Neural Scaling

**Title**: Superposition Yields Robust Neural Scaling
**Authors**: Liu et al.
**Links**: https://neurips.cc/virtual/2025/poster/116346

**核心发现**: 表征叠加（superposition）是神经缩放律的核心驱动力。在强叠加条件下，loss 与模型维度成反比缩放（~1/m），与实际 LLM 观察一致。

### 2.6 Runner-Up: Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

**Links**: https://neurips.cc/virtual/2025/poster/119944

**核心发现（负面结果）**: RLVR（Reinforcement Learning with Verifiable Rewards）**并没有**在基座模型能力之外产生新的推理模式。RLVR 模型在 pass@k 的大 k 值下并不优于基座模型。RLVR 的推理路径已包含在基座模型采样分布中，RL 只是提高了采样效率。相反，distillation 可以引入新的推理模式。

**影响**: 这项研究引发了关于当前 RLVR 范式的深刻反思，推动了 ICML 2026 上的 MaxRL 等工作。

### 2.7 Runner-Up: Optimal Mistake Bounds for Transductive Online Learning

解决了 30 年悬而未决的开放问题：在在线学习中，未标记数据能带来多大帮助？证明了一个精确的二次优势。

---

## 3. ICLR 2026 亮点论文

ICLR 2026（Apr 2026, 线上+线下）接收论文约 2,500 篇。以下是各方向亮点：

### 3.1 LLM Reasoning（63 篇笔记）

| 论文 | 作者/机构 | 创新点 | 结果 |
|------|-----------|--------|------|
| **AgentFlow** (In-The-Flow Agentic System Optimization) | Stanford / Lambda | Flow-GRPO：将长时域信用分配分解为单步更新，7B 模型训练 | 超越 GPT-4o，在搜索/数学/科学推理上平均 +14.9% |
| **ExpA (Expanded Action Space)** | — | 将 LLM 的动作空间扩展到 token 之外，引入路由动作与环境交互 | ExpA + EARL (Counterfactual Policy Optimization) 在排序任务上逼近经典算法 |
| **AgentMath** | — | 工具增强数学推理智能体，集成代码解释器 + 多轮交互 RL | 30B-3B 在 AIME24/25 达 90.6%/86.4%，超越 o3-mini |
| **T³** (Reducing Belief Deviation in RL for Active Reasoning) | — | 检测信念漂移并截断轨迹以抑制无信息尾效应 | 在 5 个挑战任务上一致提升 RL 训练效率 |
| **RAIN-Merging** | — | 无梯度方法融合推理模型与指令模型，保留思考格式 | 提升指令遵循 + 保持推理性能 |
| **MedAgentGym** | — | 72K 任务实例的生物医学编码推理环境 | Med-Copilot RL 训练提升 +45.28% |

**ICLR 2026 Workshop 亮点**：
- **Learning Reasoning Reward Models from Expert Demonstration via Inverse RL** (Outstanding Paper Award)
- **GLEAN: Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification** (Best Paper Award, Agentic AI in the Wild Workshop)
- **Retrieval-Augmented LLM Agents: Learning to Learn from Experience (EXPRAG)**：结合 LoRA 微调 + 经验检索，系统研究如何训练 LLM agent 从过去轨迹中学习

### 3.2 推理模式与架构

- **MemAgent**: Multi-Conv RL-based Memory Agent，重塑长上下文 LLM
- **Verifying Chain-of-Thought Reasoning via Its Computational Graph**: 通过计算图验证 CoT
- **Expanding the Action Space of LLMs to Reason Beyond Language (ExpA)**: 将环境交互动作内化为 expanded action space
- **Adaptive Social Learning via Mode Policy Optimization**: 定义四个推理层次模式，AMPO 算法使 agent 自适应切换推理深度，超越 GPT-4o +15.6%，减少 token 消耗 32.8%

---

## 4. ICML 2026 亮点论文

ICML 2026（Jul 6–11, Seoul）接收 6,352 篇论文（23,918 提交，26.6% 接收率）。Oral 论文 168 篇（0.7%）。

### 4.1 扩散语言模型（dLLM）— Oral 论文

| 论文 | 作者 | 创新点 |
|------|------|--------|
| **Learning Unmasking Policies for Diffusion Language Models** | ICML 2026 Oral | 将 masked diffusion sampling 形式化为 MDP，用单层 Transformer 学习 unmasking policy |
| **The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models** | ICML 2026 Oral | 揭示任意顺序生成在通用推理任务中可能**限制**推理潜力，提出 JustGRPO（抛弃任意顺序+标准 GRPO），GSM8K 达 89.1% |
| **Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis (Self-Flow)** | Hila Chefer et al. | 自监督流匹配，将表征学习集成到生成框架内 |
| **Maximum Likelihood Reinforcement Learning (MaxRL)** | ICML 2026 Oral | 提出 pass@k 展开的 compute-indexed 目标族，在二进制正确性任务上一致性优于 GRPO |
| **Reinforcement Learning with Discrete Diffusion Policies for Combinatorial Action Spaces** | ICML 2026 Poster | 提出基于策略镜像下降的离散扩散策略，在 DNA 生成、宏动作、多智能体系统中达到 SOTA |
| **Adversarial Flow Models** | Shanchuan Lin et al. | 同时属于对抗生成和流模型家族的新生成模型类 |

### 4.2 RL 与奖励优化

| 论文 | 创新点 |
|------|--------|
| **GDPO: Group Reward-Decoupled Normalization Policy Optimization** | 揭示 GRPO 在多奖励设置中归一化导致 advantage 坍塌的问题，提出解耦方案 |
| **Agentic Verifier for Competitive Coding** | 执行时重排的 test-time scaling 策略，主动推理程序行为，搜索高判别力测试输入 |
| **ALIVE: Aligning LLMs via Interactive Visual Execution** | 高通量框架自动化评估前端游戏生成，利用 one-shot planning + DOM 分析 |
| **Recursive Models for Long-Horizon Reasoning** | 递归模型可递归调用自身解决子任务，3B 模型在 SAT 上超越前沿 LLM |

### 4.3 表示学习与理解

| 论文 | 创新点 |
|------|--------|
| **You Can Learn Tokenization End-to-End with RL** | 用 score function estimates 直接优化 token 边界，比 straight-through estimates 有更紧的理论保证 |
| **UniAR: Unified Multimodal Autoregressive Modeling** | 单一离散视觉 tokenizer 连接理解与生成，共享上下文无需重新编码 |
| **Towards Unified Multimodal Pretraining** | 系统的 from-scratch 控制实验研究统一多模态预训练设计空间 |
| **From Drift to Coherence: Stabilizing Beliefs in LLMs** | 引入 Prompted Predictive Resampling，揭示 LLM 信念漂移后自稳定 |

---

## 5. AAAI 2026 亮点论文

AAAI 2026（Feb 2026, 29K+ 提交）接收 ~3,700 篇。

### 5.1 Outstanding Paper Awards

| 论文 | 作者/机构 | 方向 |
|------|-----------|------|
| **Model Change for Description Logic Concepts** | Ana Ozaki, Jandson S Ribeiro | 知识表示与推理 |
| **ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver** | Wenxuan Song et al. | 机器人感知 |
| **High-Pass Matters: Theoretical Insights and Sheaflet-Based Design for Hypergraph Neural Networks** | Ming Li et al. | 超图神经网络理论 |
| **LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation** | Weiquan Huang et al. (Microsoft) | 跨模态表示 |

### 5.2 AI Alignment 最佳论文

**On the Alignment of Large Language Models with Global Human Opinion** — Yang Liu, Masahiro Kaneko, Chenhui Chu

### 5.3 智能体/多智能体系统

| 论文 | 核心思想 | 结果 |
|------|----------|------|
| **Adaptive Theory of Mind for LLM-based Multi-Agent Coordination** | LLM agent 间的 ToM 顺序不匹配损害协调 | A-ToM 在博弈/导航/Overcooked 上有效 |
| **MoralReason: Generalizable Moral Decision Alignment** | GRPO + 复合奖励对齐道德决策框架 | 功利主义对齐 +0.757，道义论 +0.450 |
| **Learning to Deliberate: Meta-policy Collaboration (MPDF)** | 元认知动作 Persist/Refine/Concede + SoftRankPO | 6 个推理基准 +4-5% 绝对增益 |
| **SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search** | Planner + Simulator + Critic MCTS | DailyLifeAPIs 准确率 83.6%，+16pp |
| **PRIME: Planning and Retrieval-Integrated Memory** | System 1+2 双过程推理 | LLaMA 3 逼近 GPT-4/4o |
| **HBLR: Hypothesis-driven Backward Logical Reasoning** | 置信感知符号翻译 + 假设驱动反向推理 | 5 个推理基准一致超越基线 |
| **BayesAgent: Bayesian Agentic Reasoning via vPGM** | 概率图模型 + LLM agent | 置信度校准和文本生成质量提升 |
| **ActRe: Act-before-Reasoning Staged RL** | 反转 rollout 顺序（先动作后推理）解决探索收缩 | ALFWorld/WebShop 更高成功率 |
| **SABER: Switchable and Balanced Training for Efficient LLM Reasoning** | Token-budgeted reasoning，四种推理模式 | 推理长度减少 65.4%，准确率 +3.6% |

---

## 6. CVPR 2026 亮点论文

CVPR 2026（Denver, Jun 2026）提交 16,092 篇，接收 4,089 篇。

### 6.1 Award Candidates

| 论文 | 方向 | 核心贡献 |
|------|------|----------|
| **3DReflecNet: Large-Scale Dataset for 3D Reconstruction of Reflective/Transparent Objects** | 3D | 22TB+ 数据集，10K+ 合成 + 1K+ 真实物体，7M+ 多视图帧 |
| **Molmo2: Open Weights and Data for VLMs with Video Understanding and Grounding** | VLM | SOTA 开源 VLM，视频 pointing 超越 Gemini 2.5 Pro（32.9% vs 17%） |
| **D4RT: Efficiently Reconstructing Dynamic Scenes** | 4D | 全新前馈网络，设置 4D 重建 SOTA |
| **PixelDiT: Pixel Diffusion Transformers for Image Generation** | 生成 | 像素级扩散 Transformer |
| **NitroGen: Open Foundation Model for Generalist Gaming Agents** | 游戏 AI | NVIDIA/Stanford，40K 小时玩 1,000+ 游戏，低数据条件 +52% |
| **LCDrive: Latent Reasoning for Autonomous Driving** | 自动驾驶 | 用压缩潜表征替代文本推理，token 减半 |
| **SenseSearch: Empowering VLMs with High-Resolution Agentic Search-Reasoning via RL** | VLM+RL | 强化学习增强 VLM 搜索推理 |
| **Efficiently Reconstructing Dynamic Scenes One D4RT at a Time** | 4D | Google DeepMind，设置 4D 重建 SOTA |
| **A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens** | 世界模型 | 高效世界建模 |

### 6.2 Highlighted Papers

- **AVGGT**: 分析 VGGT/\pi^3 中全局注意力的角色分配，提出 training-free 加速（8-10×）
- **MV-RoMa**: 多视图密集匹配模型，SfM 更可靠更稠密
- **Scal3R**: 大规模 3D 重建的可扩展 test-time training
- **Point4Cast**: 流式动态场景重建与预测
- **CoSMo3D**: LLM 引导的开放世界 3D 语义分割
- **GlyphPrinter**: Region-Grouped DPO 用于精确视觉文本渲染
- **EMO-R3**: 反思式 RL 用于 MLLM 情感推理
- **Unified Generation and Self-Verification via Advantage Decoupled Preference Optimization**

---

## 7. EMNLP 2025 亮点论文

EMNLP 2025（Suzhou, Nov 2025）接收 1,811 篇 Main + 1,417 篇 Findings。

### 7.1 Best Paper

**Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index**
- 作者：Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
- 用 FM-index 实现在互联网规模上的精确 n-gram 搜索

### 7.2 Outstanding Papers

| 论文 | 核心内容 |
|------|----------|
| **LingGym: How Far Are LLMs from Thinking Like Field Linguists?** | 评估 LLM 的语言学推理能力 |
| **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?** | LLM 自称的价值与实际行为存在差异（value-action gap） |
| **Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps** | 通过遗忘推理步骤测量 CoT 忠实度 |
| **MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning** | 混合建模 + 上下文感知路由 |
| **Causal Interventions Reveal Shared Structure Across English Filler-Gap Constructions** | 因果可解释性揭示语言结构共享 |
| **HMoE: Heterogeneous Mixture of Experts for Language Modeling** | 异构 MoE |
| **PAFT: Prompt-Agnostic Fine-Tuning** | 提示无关微调 |
| **DiscoSG: Towards Discourse-Level Text Scene Graph Parsing** | 篇章级文本场景图解析 |

### 7.3 关键趋势

- 智能体系统（AgentMaster 多模态信息检索分析、ReSo 奖励驱动自组织多智能体）
- 模型可解释性（Attention 机制去偏、embedding 过参数化、FFN 神经元分析）
- 不确定性量化（Unconditional Truthfulness、Conformal Prediction for LLM-as-Judge）
- 模型遗忘/去学习（OBLIVIATE 掩码遗忘损失）

---

## 8. KDD 2026 亮点论文

KDD 2026（Jeju, Aug 9–13）Keynote Speakers：Jeff Dean (Google), Jingren Zhou (Alibaba), Regina Barzilay (MIT).

### 8.1 知识图谱与推理

| 论文 | 创新点 |
|------|--------|
| **GRiD: Generating Graph-Like Logical Rules via Diffusion Models** | 将规则发现重构为离散扩散过程，SL 预训练结构先验 + RL 微调，6 个 KG 基准有效 |
| **SPiKE: Semantic Profiles into Knowledge Graphs for Enhanced Recommendation** | LLM 生成语义画像 + KG 传播，4 维度 profiling 方法学 |

### 8.2 因果推断

| 论文 | 创新点 |
|------|--------|
| **DCNAR: From Causal Discovery to Dynamic Causal Inference in Neural Time Series** | 两阶段因果框架，139 国 × 35 年 V-Dem 面板评估 |

### 8.3 推荐/CTR

| 论文 | 创新点 |
|------|--------|
| **HumanLLM: Towards Personalized Understanding and Simulation of Human Nature** | 基于 LLM 的个性化人类特质理解与模拟 |

---

## 9. 推荐系统/CTR/广告（SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025）

### 9.1 SIGIR 2026（Melbourne, Jul 20–24）

| 论文 | 作者/机构 | 核心贡献 |
|------|-----------|----------|
| **GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation** | JD.com | Page-wise NTP + GRPO-SR（NLL 正则化 + Hybrid Rewards），JD App 上线，点击 +9.5%，交易 +8.7% |
| **TimeMM: Time-as-Operator Spectral Filtering for Dynamic Multimodal Recommendation** | — | 时间条件谱滤波，Time-as-Operator + Adaptive Spectral Filtering + Spectral-Aware Modality Routing，+3%–10% Recall/NDCG |
| **LTRR: Learning To Rank Retrievers for LLMs** | — | 将查询路由形式化为学习排序问题，XGBoost pairwise 超越单检索器 RAG |
| **OneTrans: Unified Feature Interaction and Sequence Modeling** | ByteDance/WWW 2026 | 统一 Transformer 骨干同时建模行为序列和特征交互，+5.68% GMV |

### 9.2 WWW 2026

| 论文 | 核心贡献 |
|------|----------|
| **ThinkRec: Thinking-based Recommendation via LLM** | 引入合成推理轨迹的思考激活机制 + 实例级专家融合，推荐准确性和可解释性显著提升 |
| **TopKGAT: Top-K Objective-Driven Architecture** | 从 Precision@K metric 的可微近似直接推导推荐架构，4 个基准一致 SOTA |
| **InteractRank: Personalized Web-Scale Search Pre-Ranking (Pinterest)** | 跨交互特征的双塔预排序模型，在线 +6.5% engagement |
| **DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction** | 自适应意图感知网络，阿里闲鱼在线 CTR +1.59% |

### 9.3 RecSys 2025 最佳论文

**You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control**
- Authors: Giovanni De Toni et al.
- 将 conformal risk control 应用于推荐系统，减少不想要的推荐

### 9.4 CIKM 2025

- **TWIN v2**: Kuaishou 超长行为序列建模扩展版本
- **RankMixer**: ByteDance token-mixing 排名模型（CIKM 2025）

### 9.5 工业 CTR/推荐最新进展

| 公司 | 模型 | 规模 | 线上收益 |
|------|------|------|----------|
| **ByteDance** | TokenMixer-Large | 7B (online) / 15B (offline) | +2.98% GMV, +2% ADSS |
| **ByteDance** | HyFormer | 3B samples, 70 days | +1.11% finish play |
| **ByteDance** | OneTrans | Unified transformer | +5.68% GMV |
| **Kuaishou** | Taiji (LLM-as-Enhancer) | DeepSeek-R1-7B + POPO | +2.83% ADVV, +3.30% Revenue |
| **Kuaishou** | GR4AD (Generative Rec for AD) | UA-SID + LazyAR + RSPO | +4.2% ad revenue |
| **Kuaishou** | OneMall (E-commerce Generative Rec) | End-to-end Transformer RL | +14.7% Product GMV |
| **Kuaishou** | UniMixer | Unified scaling block | +15% CAD |
| **JD.com** | GenRec | Decoder-only + GRPO-SR | +9.5% click, +8.7% transaction |
| **Alibaba (Xianyu)** | DAIAN | Adaptive intent-aware | +1.59% CTR |
| **Pinterest** | InteractRank | Cross-interaction pre-rank | +6.5% engagement |

---

## 10. 各大实验室重点论文

### 10.1 Google DeepMind

| 论文 | 方向 |
|------|------|
| **Aletheia: Towards Autonomous Mathematics Research** | 数学研究 agent，Gemini Deep Think 驱动，IMO-ProofBench 95%，自主解决 Bloch 猜测和 Erdős 问题 |
| **Aletheia Tackles FirstProof** | FirstProof 10 题中自主解决 6 题（多数专家评估） |
| **GrandCode: Grandmaster Level in Competitive Programming** | 多智能体 RL，Codeforces Round 1087/1088/1089 三连冠，击败所有人类选手含传奇大师 |
| **MiRA: Subgoal-driven Framework for Improving Long-Horizon LLM Agents** | 子目标分解 + 里程碑奖励，Gemma3-12B SR 6.4%→43.0% |
| **HyperAgents (DGM-H)** | 自引用 agent 实现元认知自我改进，跨领域迁移自我改进能力 |
| **DeepSearchQA** | 900-prompt 深度搜索评估基准，测试 agent 穷尽检索能力 |
| **Self-Proving Models (NeurIPS 2025)** | 模型自己的输出可被验证算法验证，基于交互式证明系统 |

### 10.2 OpenAI

| 论文/成果 | 方向 |
|-----------|------|
| **GPT-5 Pro High Reasoning** | DeepSearchQA Fully Correct 66.09% |
| **GPT-5.2** | MetaClaw 基座模型对比基线 |

### 10.3 Meta AI

- **ULTRA-HSTU**: 弯曲缩放律曲线（CTR）
- **Credit Assignment with Resets**: 降低回复延迟
- **Sparsity 2:4 Beyond**: 硬件优化

### 10.4 NVIDIA

| 论文/成果 | 方向 |
|-----------|------|
| **NitroGen** (CVPR 2026) | 通用游戏 agent 基础模型，40K 小时 / 1,000+ 游戏训练 |
| **GraspGen-X** (CVPR 2026) | 零样本抓取基础模型 |
| **LCDrive** (CVPR 2026) | 潜表征推理替代文本推理的自动驾驶模型 |

### 10.5 Microsoft Research Asia

- **SkillOpt**: 自进化 agent 技能优化
- **Inductive Deductive Synthesis**: 验证系统的归纳演绎综合

### 10.6 Anthropic

- **Constitutional Classifiers++**: 不需要人类反馈的自纠错
- **Model Context Protocol**: 97M 月下载量
- **TaLK: Speech-to-Speech LLM**: 端到端语音 LLM

### 10.7 ByteDance (AML)

| 模型 | 参数/规模 | 场景 | 线上效果 |
|------|-----------|------|----------|
| **TokenMixer-Large** | 7B (online) / 15B (offline) | Feed Ads, E-Commerce, Live | +2.0% ADSS, +2.98% GMV, +1.4% Pay |
| **HyFormer** | 3B samples / 70 days | Douyin Search | +1.111% finish play |
| **OneTrans** | Transformer backbone | Unified ranking | +5.68% GMV |
| **MixFormer** | Co-scaling dense + seq | — | — |

### 10.8 Kuaishou Technology

| 模型 | 核心贡献 | 线上效果 |
|------|----------|----------|
| **Taiji** (POPO) | LLM-as-Enhancer，Pareto 最优语义-协同权衡 | +2.83% ADVV, +3.30% Rev |
| **GR4AD** | 生成式广告推荐，UA-SID + LazyAR + RSPO | +4.2% ad revenue |
| **OneMall** | 电商端到端生成式推荐 | +14.7% Product GMV |
| **UniMixer** | 统一缩放律框架 | +15% CAD (30-day) |

### 10.9 Alibaba

| 模型 | 方向 |
|------|------|
| **DAIAN** | 触发诱导推荐中自适应意图感知 CTR |
| **ALIVE** (ICML 2026) | 前端小游戏 RL 自动化评估 |
| **UniAR** (ICML 2026) | 统一多模态自回归框架 |

### 10.10 JD.com

| 模型 | 方向 |
|------|------|
| **GenRec** | 生成式推荐，Page-wise NTP + GRPO-SR |

---

## 11. 智能体/Agent 系统

### 11.1 Agent 推理与规划

| 论文 | 会议 | 核心贡献 |
|------|------|----------|
| **AgentFlow** | ICLR 2026 | Flow-GRPO，7B 超越 GPT-4o |
| **SPIRAL** | AAAI 2026 | Planner+Simulator+Critic MCTS |
| **PRIME** | AAAI 2026 | System 1+2 双过程推理框架 |
| **ActRe** | AAAI 2026 | Action-before-Reasoning 训练 |
| **SABER** | AAAI 2026 | 可控制推理深度的 LLM 训练 |
| **MetaClaw** | arXiv 2026 | 持续元学习，Kimi-K2.5 21.4%→40.6% |
| **GrandCode** | arXiv 2026 | Codeforces 三连冠，击败所有人类 |
| **MiRA** | Google DeepMind | 子目标 + 里程碑 RL，WebArena 6.4%→43% |

### 11.2 Multi-Agent 系统

| 论文 | 核心思想 |
|------|----------|
| **Adaptive Theory of Mind** (AAAI 2026) | Agent 间 ToM 顺序对齐 |
| **MPDF + SoftRankPO** (AAAI 2026) | 元认知动作 Persist/Refine/Concede |
| **HyperAgents (DGM-H)** (Google DeepMind) | 自我改进可以自我改进的 agent |
| **Agentic Verifier** (ICML 2026) | 主动推理程序行为的执行时验证 |

### 11.3 Agent 持续学习与记忆

| 论文 | 核心思想 |
|------|----------|
| **MetaClaw** | 技能库 + LoRA 机会窗口微调，零下线时间 |
| **EXPRAG** (ICLR 2026) | 经验检索增强的 LLM agent 训练 |
| **MemAgent** (ICLR 2026) | 多轮 RL 记忆 agent |
| **PRIME** (AAAI 2026) | Planning + Retrieval 集成记忆 |

---

## 12. 生成模型与多模态

### 12.1 扩散模型与流匹配

| 论文 | 会议 | 核心创新 |
|------|------|----------|
| **Self-Flow** | ICML 2026 | 自监督流匹配，表征学习在生成框架内联合优化 |
| **Adversarial Flow Models** | ICML 2026 | 同时属于对抗生成和流模型的新家族 |
| **PixelDiT** | CVPR 2026 | 像素级扩散 Transformer 图像生成 |
| **LLaDA** | NeurIPS 2025 | 从零训练的扩散大语言模型，挑战自回归范式 |
| **UniAR** | ICML 2026 | 统一多模态自回归，单一 tokenizer + 共享上下文 |

### 12.2 视频生成与理解

| 论文 | 会议 | 核心贡献 |
|------|------|----------|
| **D4RT** | CVPR 2026 | 高效 4D 场景重建，Google DeepMind |
| **Point4Cast** | CVPR 2026 | 流式动态场景重建与预测 |
| **EgoX** | CVPR 2026 | 单视角 exocentric 视频生成 egocentric 视频 |
| **StreamingT2V** | CVPR 2025 (most influential) | 自回归长视频生成 2 分钟+ |

### 12.3 视觉语言模型

| 论文 | 会议 | 核心贡献 |
|------|------|----------|
| **Molmo2** | CVPR 2026 | 开源 VLM SOTA，视频 pointing 32.9% vs Gemini 2.5 Pro 17% |
| **LLM2CLIP** | AAAI 2026 Outstanding | 强大语言模型解锁更丰富跨模态表示 |
| **UniVerse** | CVPR 2026 | 知识与推理统一的生成模型 |
| **PersonaVLM** | CVPR 2026 | 长期个性化多模态 LLM |

---

## 13. 代码/推理/数学

### 13.1 代码生成

| 论文 | 会议 | 核心贡献 |
|------|------|----------|
| **GrandCode** | arXiv 2026 | Codeforces 三连冠（Round 1087/1088/1089），Agentic GRPO |
| **Agentic Verifier** | ICML 2026 | 主动推理程序行为的 agentic verifier |
| **AgentMath** | ICLR 2026 | 工具增强数学推理 agent，AIME24 90.6% |
| **CodeTree** | ACL 2025 | Agent 引导的树搜索代码生成 |

### 13.2 数学推理

| 论文 | 核心贡献 |
|------|----------|
| **Aletheia** | 自主数学研究 agent，FirstProof 6/10 解决，Bloom Erdős 4 个开放问题解决 |
| **Agentic Verifier** | 执行时验证的 test-time scaling |
| **Recursive Models** | 3B 模型在 SAT 上超越前沿 LLM |

---

## 14. 游戏与强化学习

### 14.1 游戏 AI

| 论文 | 会议 | 核心贡献 |
|------|------|----------|
| **NitroGen** | CVPR 2026 | NVIDIA/Stanford，40K 小时 / 1,000+ 游戏，低数据 +52% |
| **ALIVE** | ICML 2026 | Alibaba，前端小游戏 RL 自动化评估 |
| **PCSP** | arXiv 2026 | One Policy Infinite NPCs，个性条件共享策略 |

### 14.2 RL 算法创新

| 论文 | 会议 | 核心创新 |
|------|------|----------|
| **MaxRL** | ICML 2026 Oral | 最大似然 RL，pass@k 展开 |
| **GDPO** | ICML 2026 | Group Reward-Decoupled Normalization |
| **Flow-GRPO** | ICLR 2026 | 流程级 GRPO 训练模块化 agent |
| **1000-Layer Networks for Self-Supervised RL** | NeurIPS 2025 Best | 1024 层 RL 网络 |
| **JustGRPO** | ICML 2026 Oral | 抛弃任意顺序 dLLM + 标准 GRPO |

---

## 15. 总结与展望

### 15.1 未来研究热点预测

1. **Diffusion LLM 的 RL post-training**: 多个 ICML 2026 Oral 指出 dLLM 的 RL 训练需要专门设计，任意顺序生成可能是陷阱而非优势。

2. **Agent 的持续学习与进化**: MetaClaw、HyperAgents 展示了 agent 在使用过程中不断进化而不下线的新范式。

3. **推荐系统的 LLM 化**: 多家公司（ByteDance、Kuaishou、JD）已将推荐模型扩展到 7B-15B 参数，生成式推荐与传统 DLRM 的融合将加速。

4. **推理模型的效率与可控性**: SABER 实现了推理深度可控，RAIN-Merging 融合推理和指令执行，推理模型变得可调节。

5. **RLVR 范式进化**: NeurIPS 2025 的负面发现（RLVR 不产生新推理模式）推动了 MaxRL、GDPO、Agentic GRPO 等新方法。

6. **多模态生成的统一框架**: UniAR、Self-Flow 等致力于用一个架构统一理解和生成。

### 15.2 工业界 vs 学术界

- 工业界的优势领域：CTR/推荐系统缩放律（ByteDance、Kuaishou、Meta），大规模 RLVR 训练，agent 系统
- 学术界的优势领域：扩散 LLM 理论，推理能力分析，偏见/安全评估
- 合作交叉地带：Agent 评估基准（DeepSearchQA、MedAgentGym），模型压缩与效率

---

> 本报告基于 2026 年 6 月 8 日的公开信息整理。论文信息请以各会议最终版本为准。arXiv 链接和具体会议信息请参考各论文页面 [[conference-digest] 系列存档](../conference-digest.md)。
