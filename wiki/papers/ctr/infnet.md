---
title: "INFNet: Aggregate and Broadcast — Scalable and Efficient Feature Interaction for Recommender Systems"
title-zh: "INFNet: 面向推荐系统的可扩展高效特征交互——聚合与广播"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Kuaishou]
year: 2025
venue: arXiv
arxiv: 2508.11565
tags: [linear-complexity, feature-interaction, hub-tokens, kuaishou]
category: ctr
---

## 问题背景

工业 CTR 模型中特征交互的复杂度通常为 O(n²) 或更高，限制了模型在特征数量增加时的扩展能力。

## 方法详述

提出 INFNet 聚合-广播（Aggregate-and-Broadcast）线性复杂度架构：

1. **Hub Token 机制**：引入少量 Hub Token 作为信息汇聚节点
2. **聚合步骤**：所有特征向 Hub Token 做聚合（线性复杂度 O(n)）
3. **广播步骤**：Hub Token 将聚合信息广播回所有特征（O(n)）
4. **任务感知**：Hub Token 的编码与下游任务相关，实现任务感知特征交互
5. **端到端训练**：Hub Token 数量作为可调超参数

## 主要创新点

1. 线性复杂度的特征交互范式
2. Hub Token 的聚合-广播机制
3. 任务感知特征选择

## 实验结果对比

| 模型 | 计算复杂度 | AUC | 特征数扩展性 | 推理时间 |
|------|-----------|-----|------------|---------|
| DCN-V2 | O(n²) | 0.8035 | 差 | 1.0× |
| AutoInt | O(n² d) | 0.8060 | 差 | 1.3× |
| INFNet | O(n) | 0.8075 | 优 | 0.7× |
| INFNet-Large | O(n) | 0.8100 | 优 | 0.9× |

## 局限性

Hub Token 数量少时可能成为信息瓶颈；聚合-广播机制在高阶交叉场景下表达能力受限。
