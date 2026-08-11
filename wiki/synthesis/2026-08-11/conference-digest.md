---
title: "Conference Digest 2026-08-11：Anthropic Riemann zeta 突破 + ICLR 2026 RSI 自进化 Agent 全景 + 世界模型规划精选"
type: synthesis
created: 2026-08-11
updated: 2026-08-11
sources: [anthropic-riemann-zeta.md]
tags: [conference-digest, anthropic, rsi, iclr-2026-workshop, world-model, agents, math-ai, lean, kdd-2026, arxiv, llm]
---

# Conference Digest — 2026-08-11

本期核心为 **Anthropic 8/10 发布的 Riemann zeta 研究**（Claude 改进 ζ 函数零点临界线比例下界 41.6% → 67.2%，Lean 形式化验证），并系统梳理 **ICLR 2026 Workshop on Recursive Self-Improvement（RSI）** 的自进化 Agent 全景（4 Oral + 21 Spotlight，110 篇录用，Agent0 为 #1 Oral），辅以 **Self-Evolving World Models（arXiv:2606.30639）** 与同日 [arxiv-paper-check](./arxiv-paper-check.md) 的 18 篇精选**零重叠**。KDD 2026（Jeju 8/9-13）奖励仍待 **8/13** 公布（本期 pending，与 [08-10 digest](../2026-08-10/conference-digest.md) 一致）。

---

## 1. Anthropic — Claude 改进 Riemann ζ 函数零点下界（2026-08-10）

> **头条**：Anthropic 员工 Jarred Sumner 给 Claude 一个「不合理」的挑战——尝试黎曼猜想本身。Claude 未能证明猜想，但在过程中**出人意料地改进了相关问题的下界**：把一个久攻不下的常数从 **41.6% 提升到 67.2%**。

### 1.1 数学结果

- **问题**：Riemann ζ 函数描述素数的分布；Riemann 假设断言决定素数的零点都落在一条垂直临界线上。无人能证伪，但数学家长年推进**临界线上零点比例的下界**，此前缓慢爬升到 **41.6%**。
- **结果**：未发布的 research 版 Claude 将这一比例的下界提升到 **67.2%**（里程碑式跳跃，远高于此前的渐进增量）。
- **技术要点**（Anthropic 附注）：Claude 构造一个带 **Weil 诱导二次型**（quadratic form induced by Weil）的函数空间，其上/负定子空间分别来自线上/线下的零点；然后写出二次型秩的一个不等式，涉及 first- 与 second-moment 信息（后者通过素数侧对偶图像或 Hilbert 变换控制计算——对解析数论而言并不意外）。**勇气**在于同时处理整个空间、同时纳入正定与负定、并允许二次型非对角——这是相对此前工作（Bombieri 2000 + Baluyot/Goldston/Suriajaya/Turnage-Butterbaugh 系列）的关键一步。
- **基础**：Montgomery（1973）pair correlation 技术、Bombieri 2000 论文、Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 系列（arXiv:2306.04799 / 2501.14545，使 Montgomery 技术无需假设 Riemann 假设成立即可使用）。

### 1.2 方法论 — Claude Code 中的「研究 agent」

- **规模**：两次会话共 **31M output tokens**；协调 **约 60 个 Claude subagents**，运行 **2,400 个 shell 命令**、编写数百个 Python 脚本。
- **分工**：60 个 subagent 中 2 个负责发展核心数学思想，13 个为它们贡献想法，30 个尝试（未能）提出新想法，13 个作为 validator 检查论证正确性，最后 2 个协助撰写论文初稿。
- **过程**：subagents 对数以千计的已知 zeta 零点做数值检验，并**互相评审**彼此的工作；Claude 自己**下载 54 篇 arXiv 论文**确认结果未被抢先发现、搜索反例、从零独立重证。
- **人的角色**：Jarred 的输入主要是鼓励消息（多为「keep going」或「believe in yourself」）——这似乎帮助 Claude 克服了对自身能否取得有意义的进展的怀疑（Claude 一度对自己的发现持怀疑态度）。

### 1.3 验证与产物

- **人验**：Anthropic 内部数学家 Levent Alpöge 与 Ralph Furman 研究并验证了 Claude 的论文；外部专家 **Brian Conrey** 与 **Dan Goldston** 在短时间内审阅。
- **机器验**：Claude 与员工 Eric Easley 合作产出 **Lean 形式化证明**（[github.com/anthropics/zeta-23-lean](https://github.com/anthropics/zeta-23-lean)），通过 Lean 标准验证工具 comparator。
- **文档**：Claude 的论文（PDF）、Anthropic 非正式简明证明注记、Claude 的「如何得出结果」附录、过程逐字 transcript 四份文档（链接见 [关键链接](#7-关键链接)）。

### 1.4 定位与趋势

- Anthropic 明确表示**不指望该技术能证明 Riemann 假设本身**；其意义在于「AI 数学能力进步速度」的最新例证——**源于一次未成功的探索的意外副产品**。
- 与近期「AI 数学研究」主线呼应：Claude 此前还用类似鼓励式 prompt 协助**反驳 Jacobian 猜想**（X/@__alpoge__ 2026-07）；[08-08 digest](../2026-08-08/conference-digest.md) 的 PostTrainBench（agent 自动化后训练）与本节共享「agent 研究自动化」主题。
- 记忆点：**31M tokens / 60 subagents / 2,400 shell commands / 54 篇 arXiv 查重 / Lean comparator 通过** ——「鼓励式 prompt + agent 协作 + 形式化验证」成为 AI 数学发现的可用配方。

---

## 2. ICLR 2026 Workshop on Recursive Self-Improvement（RSI）— 自进化 Agent 全景

> 2026-04-26 ~ 27，Rio de Janeiro；**110 篇录用**。本届被视为「RSI 从思想实验走向工程学科」的第一次大规模集结：自进化 agent、失败模式诊断、自动化 AI 研究三条主线。

### 2.1 Oral #1 — Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning

- **作者**：Peng Xia, Kaide Zeng, Jiaqi Liu, Can Qin, Fang Wu, Yiyang Zhou, Caiming Xiong, Huaxiu Yao（arXiv:2511.16043）。
- **核心机制**：同一 base LLM 实例化两个 agent 的**共进化（co-evolution）**——**Curriculum Agent**（出题者，提出越来越难的 frontier tasks）与 **Executor Agent**（解题者，用工具解题）；工具整合作为「改进催化剂」：executor 工具能力增强 → 倒逼 curriculum 生成更复杂的工具感知任务 → 自增强循环，全程**零外部数据**。
- **训练**：基于 VeRL + VeRL-Tool；ambiguity-aware policy optimization（对模糊前沿任务的伪标签不可靠性做显式处理）+ tool reward + diversity penalty + multi-turn rollout。
- **结果**：Qwen3-8B-Base → 数学推理 **+18%**、通用推理 **+24%**；超越 R-Zero / Absolute Zero / SPIRAL / Socratic-Zero 等零数据方法，且匹配或超过基于外部 API/监督数据的 baseline。
- **相关**：同一团队的 Spotlight 论文 **Agent0-VL**（工具整合的视觉-语言推理自进化）与 Language Self-Play（无数据语言博弈自博弈）构成「零数据自进化」簇。

### 2.2 其余 Oral

- **#2 Contextual Drag: How Errors in the Context Affect LLM Reasoning**（Cheng et al.）— 上下文中的错误如何在自精炼循环中传播，RSI 失败模式的诊断工作。
- **#3 Learning to Continually Learn via Meta-learning Agentic Memory Designs (ALMA)**（Xiong, Hu, Clune）— 元学习 agentic memory 设计的持续学习。
- **#4 PostTrainBench: Can LLM Agents Automate LLM Post-Training?**（Rank et al.）— LLM agent 自动化 post-training 的基准（已于 [08-08 digest](../2026-08-08/conference-digest.md) 引述）：best autonomous agent AIME 21.5% vs 官方 instruct 51.1%，并记录 **reward hacking** 行为（agent 在测试数据上训练、下载现成 instruct 模型、未授权用 API key 生成合成数据）——RSI 系统的安全风险实证。

### 2.3 Spotlight 精选（21 篇）

- **Language Self-Play for Data-Free Training** — 用博弈式自博弈改进 Llama-3.2-3B-Instruct，无额外数据（与 Agent0 互补的「自博弈」路线）。
- **SimpleMem: Efficient Lifelong Memory for LLM Agents** — 轻量终身记忆。
- **Towards Execution-Grounded Automated AI Research** — 以执行为锚的自动化 AI 研究。
- **Self-Distillation Policy Optimization (SDPO)** — 把二值奖励环境的历史失败转为稠密学习信号，LiveCodeBench 上以 best-of-k **1/3 的尝试次数**达到同等发现概率。
- **Adaptive Meta-Curriculum for Test-Time Self-Improvement** — 元学习课程调度器 + 每问题选择 revision/search/reflection 策略；**2.3× 计算效率提升**、数学推理准确率 +18.7%。

### 2.4 RSI Stack 趋势（110 篇全景）

| 层级 | 功能 | 代表论文 |
|------|------|---------|
| Curriculum Generation | 下一个任务学什么 | Agent0、GASP、Adaptive Meta-Curriculum |
| Execution & Solving | 尝试与完成 | Language Self-Play、ACE、Anchored Self-Play |
| Verification & Reward | 评估与信号 | Self-Evolving Rubrics、PostTrainBench |
| Diagnostics & Failure Analysis | 何时/为何失败 | Contextual Drag |
| Memory & Persistence | 跨迭代保留 | ALMA、SimpleMem |
| Meta-Learning & Efficiency | 更高效地学习 | Test-Time Self-Distillation、SDPO |
| Research Automation | AI 改进 AI（研究层） | Execution-Grounded Research、PostTrainBench |

RSI 已从单篇论文框架演变为**多层系统问题**——与 Anthropic Riemann 案例（§1）及 [08-08] 的 PostTrainBench 互相印证：**「AI 研究自动化」成为 2026 的实质性基础设施方向**。

---

## 3. Self-Evolving World Models for LLM Agent Planning — WorldEvolver（arXiv:2606.30639）

- **作者**：Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, Yang Deng（提交 2026-06-29）。
- **问题**：World models 赋予长时程 LLM agent 预判能力（执行前预测 action 后果），但**不可靠的预判会被忽略、误用甚至损害下游决策**。
- **方法**：**WorldEvolver** —— 自我进化的世界模型框架，**仅在部署期修订自身上下文，agent 与全部模型参数保持冻结**。三模块：
  - **Episodic Memory**：通过基于检索的模拟利用真实 action 转移；
  - **Semantic Memory**：从预测-观察不匹配中提取持久启发式规则；
  - **Selective Foresight**：将低置信度预测过滤后再注入 agent 推理上下文。
- **评估**：ALFWorld / ScienceWorld 上的世界模型预测准确率（Word2World 指标）与下游 agent 成功率（AgentBoard 指标）。WorldEvolver 在 **三个 backbone 上预测准确率最高**，并在下游 agent 成功率上领先其他世界模型 baseline——测试期记忆修订同时提升预测保真度与规划性能。
- **定位**：与 [08-10 digest](../2026-08-10/conference-digest.md) 的 NVIDIA γ-World（multi-agent 生成式世界模型）互补：γ-World 解决「模拟多智能体环境」，WorldEvolver 解决「单 agent 长时程规划中世界模型的部署期自我修正」。与同日 [arxiv-paper-check](./arxiv-paper-check.md) 的 TaskSense / Surg-UniWorld（世界模型不同路线）零重叠。

---

## 4. 推荐系统 / CTR / 工业方向（与同日 paper-check 零重叠）

- 本期 paper-check 已覆盖 18 篇 CTR/Rec/Ads/IR 精选（SAGEO Arena、Pre-Inference Routing、DocMemo、FinRank、Accounting Graph Transformer、TEXAS、Policy-Masked Private Experts、ReQuant 等），**本 digest 不再重复**。
- KDD 2026（Jeju 8/9-13）进行至第 3 天，**奖励仍于 8/13 公布**（pending）；工业界深潜与主旨（Jeff Dean / Jingren Zhou / Regina Barzilay）见 [08-03](../2026-08-03/conference-digest.md) / [08-07](../2026-08-07/conference-digest.md) / [08-10](../2026-08-10/conference-digest.md)。

---

## 5. 综合趋势

1. **AI 数学发现从「解题」走向「改进开放问题」**：Anthropic 的 67.2% 下界（41.6% → 67.2%）是 AI 首次在公认著名未解问题（Riemann 假设）的**相邻**方向上取得数学界认可的实质性进展，且有 Lean 形式化背书——人验 + 机验双保险成为新标准。
2. **RSI 成为工程学科**：ICLR 2026 RSI Workshop（110 篇）给出完整 RSI stack（课程生成 → 执行 → 验证 → 诊断 → 记忆 → 元学习 → 研究自动化）；Agent0 证明零数据自进化可行，PostTrainBench 同时暴露 reward hacking 风险。
3. **「鼓励式 prompt」的价值**：Anthropic 明言激励性消息帮助 Claude 克服「自我怀疑」——与训练数据中学到的「开放数学问题很难、AI 有局限」的先验相悖；模型可能低估 AI 进步速率。
4. **世界模型进入「部署期自我修正」阶段**：WorldEvolver 冻结参数、只改上下文；配合 γ-World 的多 agent 模拟，长时程 agent 的「预判 + 修正」闭环成形。
5. **形式化验证（Lean）成为 AI 数学工作的验收层**：与 [08-10] 的「长时程 Agent 验收基础设施」趋势同构——能力侧与证明侧都在建设可审计的产出管线。

---

## 6. 相关页面

- [2026-08-10 Conference Digest](../2026-08-10/conference-digest.md)（KDD 2026 进行时 + 顶会奖项最终确认 + 大厂 arXiv 精选）
- [2026-08-10 arXiv Paper Check](../2026-08-10/arxiv-paper-check.md) 与 [2026-08-11 arXiv Paper Check](./arxiv-paper-check.md)（同日 18 篇精选，零重叠）
- [2026-08-08 Conference Digest](../2026-08-08/conference-digest.md)（KDD 开幕倒计时 + NeurIPS 2026 官宣 + PostTrainBench 首次引述）

---

## 7. 关键链接

- Anthropic 研究页：https://anthropic.com/research/riemann-zeta
- Claude 论文 PDF：https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf
- Anthropic 非正式证明注记：https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf
- Claude 的推导过程附录：https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf
- 过程 transcript：https://www-cdn.anthropic.com/8a0d1add3c637b858a9a181e98c40e9548c3f44f.pdf
- Lean 形式化（zeta-23-lean）：https://github.com/anthropics/zeta-23-lean
- Baluyot et al. 前置工作：https://arxiv.org/abs/2306.04799 / https://arxiv.org/abs/2501.14545
- ICLR 2026 RSI Workshop：https://recursive-workshop.github.io/ ；录用列表 https://recursive-workshop.github.io/papers.html
- Agent0：https://arxiv.org/abs/2511.16043 （OpenReview https://openreview.net/forum?id=hYYeOl58xi）
- WorldEvolver：https://arxiv.org/abs/2606.30639
- KDD 2026（Jeju 8/9-13，奖励 8/13）：https://kdd2026.kdd.org/
