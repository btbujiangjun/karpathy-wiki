---
title: "GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction"
title-zh: "GenCI: 基于生成式兴趣分群建模的用户兴趣迁移 CTR 预估"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: []
year: 2026
venue: WWW 2026
arxiv: 2601.18251
tags: [generative-ctr, user-intent, cohort, interest-shift]
category: ctr
---

## 问题背景

现有 CTR 模型的discriminative paradigm过分拟合历史行为中的主导特征，无法适应快速兴趣迁移。点式排序（Pointwise Ranking）丢弃了候选集整体的上下文信号。用户兴趣经常随时间变化，但传统方法缺乏对兴趣动态变化的建模能力。

## 方法详述

提出 GenCI 生成式用户意图框架：

1. **层次量化构建语义兴趣分群（Semantic Cohort）**：通过层次聚类将用户聚类为语义兴趣群组
2. **基于 Transformer 的 NTP 任务**：提取长/短期意图，将用户行为Sequence Modeling为意图预测
3. **层次候选感知模块**：通过交叉注意力优化兴趣信号，融合候选物品信息

## 主要创新点

1. 生成式用户意图建模替代判别式匹配
2. 语义兴趣分群作为显式意图表示
3. end-to-end联合优化兴趣建模和 CTR 预测

## 实验结果对比

| 数据集 | 传统 CTR 方法 | GenCI |
|--------|-------------|-------|
| Amazon Beauty | AUC 基线 | +2.3% |
| Amazon Sports | AUC 基线 | +2.8% |
| Amazon Toys | AUC 基线 | +3.1% |

## 局限性

生成式模型的计算开销相比传统 CTR 模型更大；对冷启动物品和新用户的意图建模精度有待提高。
