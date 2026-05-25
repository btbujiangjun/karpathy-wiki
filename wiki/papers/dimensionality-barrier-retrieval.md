---
title: "Is Dimensionality a Barrier for Retrieval Models?"
title-zh: "维度是检索模型的瓶颈吗？"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Kiril Bangachev, Guy Bresler, Jonathan Kogan, Yury Polyanskiy]
year: 2026
arxiv: 2605.23556
affiliation: MIT
tags: [retrieval, theory, dimensionality]
category: sequential-modeling
---

## 问题背景

检索模型（如 Dense Retrieval、双编码器）通常在高维 embedding 空间中计算相似度。传统直觉认为：维度越高，模型的表达能力越强，因此应该能实现更精确的匹配。但高维空间存在已知的问题（维度灾难），过高的维度可能导致检索质量下降。本文从信息论和统计学角度理论分析了维度对检索模型的影响。

## 方法详述

使用信息论和统计学习的工具，分析检索模型的维度屏障（Dimensionality Barrier）：

1. **容量分析**：计算在不同维度下检索模型的信息容量上限
2. **泛化边界**：推导维度与泛化误差之间的关系
3. **最优维度**：理论上找出给定数据量下的最优 embedding 维度

## 主要创新点

- **理论框架**：首次系统分析维度对检索模型的影响
- **维度屏障定理**：证明了一定条件下存在一个维度上限，超过该上限后检索精度不再提升甚至下降
- MIT 出品（信息论和统计学专家团队）

## 局限性

- 纯理论分析，缺乏大规模实验验证
- 理论假设（数据分布、损失函数等）在实际中可能不完全满足
- 没有给出针对不同数据规模的实用维度推荐
