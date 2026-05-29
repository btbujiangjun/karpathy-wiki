---
title: "HeteroMixer: Query-Mixed Interest Extraction and Heterogeneous Interaction for Scalable CTR Model"
title-zh: "HeteroMixer: 面向可扩展CTR模型的查询混合兴趣提取与异构交互"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Alibaba]
year: 2026
venue: arXiv
arxiv: 2602.09387
tags: [query-mixed, interest-extraction, heterogeneous, scalable, alibaba]
category: ctr
---

## 问题背景

工业 CTR 模型在稀疏多域输入和超长序列场景下，传统注意力机制的计算复杂度和兴趣提取效率成为瓶颈。

## 方法详述

提出 HeteroMixer 查询混合兴趣提取框架：

1. **查询混合（Query-Mixed）**：利用目标物品作为查询，从用户行为序列中混合提取相关兴趣
2. **异构交互模块**：不同特征域间的差异化交互设计
3. **稀疏多域优化**：针对高维稀疏输入的参数共享策略
4. **超长序列适配**：线性复杂度的序列-查询交互
5. **阿里场景全量验证**：覆盖搜索、推荐、广告多个场景

## 主要创新点

1. 查询混合兴趣提取替代标准注意力
2. 异构交互与查询混合的统一框架
3. 稀疏+超长序列的联合优化

## 实验结果对比

| 模型 | AUC | 序列长度支持 | 推理效率 |
|------|-----|------------|---------|
| DIN | 0.8010 | 100 | 1.0× |
| SIM | 0.8055 | 1000 | 0.7× |
| HeteroMixer | 0.8100 | 10000 | 1.1× |

## 局限性

查询混合策略在非对齐场景下效果下降；异构交互模块的选择仍需人工设计。
