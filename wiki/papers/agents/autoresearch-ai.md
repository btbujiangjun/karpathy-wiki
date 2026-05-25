---
title: "AutoResearch AI: Towards AI-Powered Research Automation for Scientific Discovery"
title-zh: "AutoResearch AI：面向科学发现的 AI 驱动研究自动化"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Guiyao Tie, Jiawen Shi, Dingjie Song, Yixiao Huang, Ziji Sheng, Xueyang Zhou, Daizong Liu, Pan Zhou, Yongchao Chen, Ran Xu, Lifang He, Qingsong Wen, Manling Li, Cong Lu, Shuai Li, Pengtao Xie, Yixuan Yuan, Rui Meng, Lei Xing, Lichao Sun, Caiming Xiong, Philip S. Yu, Jianfeng Gao]
year: 2026
arxiv: 2605.23204
affiliation: Salesforce Research
tags: [research-automation, agents, scientific-discovery]
category: agents
---

## 问题背景

科学研究流程涉及多个环节：假设生成 → 实验设计 → 代码实现 → 数据采集 → 结果分析 → 论文撰写。目前每个环节都有独立的 AI 工具辅助，但缺少将这些环节串联为一个完整自动化工作流的系统。AutoResearch AI 的目标是构建end-to-end的 AI 科研自动化平台。

## 方法详述

AutoResearch AI 是一个多 Agent 协作的科研自动化框架，包含四个核心 Agent 角色：

1. **研究员 Agent**：分析已有文献，识别研究空白，生成可验证的假设
2. **实验员 Agent**：将假设转化为具体实验方案，包括数据集选择、模型架构、评估指标
3. **分析员 Agent**：执行实验脚本，分析结果数据，生成图表和统计摘要
4. **撰写 Agent**：将实验过程和结果整理为论文初稿（含引言、方法、实验、结论）

工作流在 Agent 之间迭代传递，每个步骤可多次反馈修正。

## 主要创新点

- **end-to-end闭环**：覆盖科学研究全生命周期，从假设生成到论文撰写
- **多 Agent 协作架构**：每个环节使用专门的 Agent，而非单一 AI 处理所有步骤
- Salesforce Research 出品

## 实验结果与对比

| 研究阶段 | 自动化程度 | 质量 (vs 人类研究者) |
|---------|-----------|-------------------|
| 文献检索与假设生成 | 全自动 | 可生成合理假设但缺乏创新性 |
| 实验方案设计 | 可生成模板 | 基础方案可行，复杂方案需人工 |
| 代码实现 | 全自动 | 可运行但需要调试边界情况 |
| 结果分析 | 半自动 | 统计正确但缺乏领域洞察 |
| 论文撰写 | 全自动 | 框架性内容可用，创新论述不足 |

**核心结论：** 当前最有价值的场景是作为研究助手——自动完成重复性工作，让研究者集中在核心科学问题上。

## 局限性

- 真正创新的假设仍需要人类科学家提出
- 结果分析缺乏真正的科学判断力
- 全自动化流程需要大量的 LLM 调用，成本较高
