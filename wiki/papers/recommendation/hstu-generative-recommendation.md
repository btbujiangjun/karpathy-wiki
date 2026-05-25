---
title: "Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations"
title-zh: "HSTU: 万亿参数序列生成式推荐"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Meta AI]
year: 2024
venue: ICML 2024
arxiv: 2402.17152
tags: [hstu, generative-recommendation, trillion-params, sequential, meta]
category: recommendation
---

## 问题背景

传统推荐系统采用多阶段级联架构（召回→粗排→精排→重排），各阶段模型独立优化，信息损失严重。能否用单一巨大的序列模型end-to-end生成推荐结果？

## 方法详述

提出 Hierarchical Sequential Transduction Unit (HSTU)，将推荐建模为序列生成任务：

1. **序列生成范式**：将推荐重新定义为用户行为序列的下一个物品预测
2. **分层转换单元**：高效处理稀疏多字段输入的 Transformer 变体
3. **万亿参数扩展**：在 Meta 的 GPU 集群上训练万亿参数模型

## 主要创新点

1. 首个万亿参数推荐模型
2. 生成式推荐范式替代级联架构
3. 序列转换替代Feature Interaction

## 实验结果对比

| 指标 | 级联基线 (多模型) | HSTU (单模型) |
|------|-----------------|--------------|
| 推荐质量 | 基线 | +12% |
| 系统延迟 | 多阶段累积 | 单阶段 |
| 参数量 | ~500M | 1T+ |

## 局限性

训练成本极高；序列生成在冷启动场景下表现不如传统方法；推理延迟需特殊优化。
