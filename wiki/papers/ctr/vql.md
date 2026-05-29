---
title: "VQL: Context-Aware Vector Quantization Attention for Ultra-Long Behavior Modeling"
title-zh: "VQL: 面向超长行为建模的上下文感知向量量化注意力"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Kuaishou]
year: 2025
venue: arXiv
arxiv: 2508.17125
tags: [vector-quantization, attention, long-behavior, kuaishou]
category: ctr
---

## 问题背景

超长用户行为序列（>10K）的注意力计算中，大部分 token 的相关性极低，但仍然参与全量计算。

## 方法详述

提出 VQL 上下文感知向量量化注意力：

1. **向量量化注意力**：将行为 token 量化到离散码本，注意力计算在码本级别进行
2. **上下文感知量化**：量化过程引入当前上下文作为条件，避免信息丢失
3. **码本索引检索**：推理时仅需查表和简单计算
4. **码本学习**：端到端训练码本
5. **超长行为验证**：在快手验证 10K+ 序列长度的有效性

## 主要创新点

1. 向量量化方法在序列注意力中的首次应用
2. 上下文感知的 VQ 策略
3. 码本索引的高效推理

## 实验结果对比

| 模型 | 复杂度 | AUC | 序列长度 | 推理延迟 |
|------|-------|-----|---------|---------|
| 标准注意 | O(n²) | 0.8090 | 500 | 1.0× |
| 稀疏注意 | O(n log n) | 0.8100 | 2000 | 1.2× |
| VQL | O(n) | 0.8115 | 10000+ | 0.7× |

## 局限性

码本容量对模型性能敏感；上下文感知条件可能引入分布偏移。
