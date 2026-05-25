---
title: "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"
title-zh: "SkillOpt：面向自进化 Agent 技能的执行级优化策略"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo]
year: 2026
arxiv: 2605.23904
affiliation: Microsoft Research Asia
tags: [agents, skill-optimization, llm, code-execution]
category: agents
---

## 问题背景

大语言模型 Agent（如 GPT-5.5、Claude Code、Codex）依赖精心设计的 system prompt 或工具调用来执行任务。但这些"Agent 技能"通常由人工手动设计、调试和优化，耗时且难以规模化。SkillOpt 提出了一种自动化方法：让 AI 自己优化自己的技能——一个"元技能优化器"来分析 Agent 的表现并调整其技能定义。

## 方法详述

SkillOpt 是一个**文本空间的技能优化器**，核心流程如下：

**输入：** 当前 Agent 技能定义（system prompt + 工具描述）+ 历史执行轨迹 + 评估分数
**输出：** 优化后的技能定义

**优化循环：**
1. **评分滚动**：在当前技能下执行一组基准任务，记录每个任务的执行轨迹和分数
2. **差异分析**：分析得分轨迹中存在问题的步骤，识别技能中的薄弱环节
3. **有界编辑**：优化器生成针对性的文字修改（而非随机搜索），每次修改有大小限制（文本learning rate预算）
4. **验证接受**：只在 hold-out 验证集上提升时才接受修改；否则回退（拒绝编辑缓冲区）
5. **周期迭代**：Epoch-wise 的慢更新 + 元更新策略，防止overfitting到特定任务

## 主要创新点

- **首个系统性的文本空间 Agent 技能优化器**：以往的方法要么是人工调 prompt，要么是超参数搜索，SkillOpt 直接优化技能文本本身
- **零推理开销**：优化只在训练阶段进行，部署时技能已固化，不增加任何推理延迟
- **强泛化性**：在所有 52 个 (模型, 基准, 框架) 组合上取得最优或并列最优

## 实验结果与对比

| 模型 | 直接使用 | 人工调优 | 自动 prompt 搜索 | **SkillOpt** |
|------|---------|---------|----------------|-------------|
| GPT-5.5 Chat | 62.3 | 68.1 | 71.4 | **85.7** (+23.4) |
| Codex | 55.1 | 61.2 | 64.8 | **79.9** (+24.8) |
| Claude Code | 58.7 | 64.3 | 67.2 | **77.8** (+19.1) |
| GPT-5.5 Agent | 71.4 | 75.6 | 78.9 | **89.2** (+17.8) |

**核心结论：**
- SkillOpt 在所有 52 个测试配置中均取得最优或并列最优（100% 成功率）
- 在 GPT-5.5 上提升 +23.4 分（直接使用 → 85.7），效果远超人工调优和自动 prompt 搜索
- Claude Code 和 Codex 也有显著提升（+19.1 ~ +24.8），说明方法不依赖于特定模型
- 优化后的技能在未见任务上同样有效，验证了泛化能力

## 局限性

- 优化过程需要大量的基准测试执行（数十轮迭代），训练成本较高
- 文本learning rate（修改大小的约束）需要人为设定，过大会破坏原有技能，过小则收敛慢
- 对于完全失败的任务（得分接近 0），优化器缺乏足够信息来定位问题
