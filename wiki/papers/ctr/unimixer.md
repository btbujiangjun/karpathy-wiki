---
title: "UniMixer: A Unified Architecture for Scaling Laws in Recommendation Systems"
title-zh: "UniMixer: 推荐系统缩放定律的统一架构"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Kuaishou]
year: 2026
venue: arXiv
arxiv: 2604.00590
tags: [unified-architecture, scaling, attention, tokenmixer, fm, kuaishou]
category: ctr
---

## 问题背景

注意力（Attention）、TokenMixer、因子分解机（FM）是推荐系统中三大主流特征交互范式，但彼此间缺乏统一的缩放框架。

## 方法详述

提出 UniMixer 统一缩放框架：

1. **统一公式**：将 Attention/TokenMixer/FM 统一表示为 token 交互的通用形式
2. **缩放维度分析**：在统一框架下对比三种范式的缩放效率
3. **UniMixing-Lite**：提出高效变体，提升缩放 ROI
4. **可插拔设计**：不同交互范式可混搭使用
5. **快手场景验证**

## 主要创新点

1. Attention/TokenMixer/FM 的统一数学框架
2. 系统对比三种范式的缩放行为
3. UniMixing-Lite 高效变体

## 实验结果对比

| 交互范式 | FLOPs 缩放 (1B 参数) | AUC | 缩放 ROI (每 FLOP AUC) |
|---------|---------------------|-----|----------------------|
| Attention | 1.0× | 0.8100 | 基准 |
| TokenMixer | 0.7× | 0.8085 | 高 |
| FM | 0.3× | 0.8050 | 中 |
| UniMixing-Lite | 0.5× | 0.8095 | 最高 |

## 局限性

统一框架对新型交互范式的扩展性有限；UniMixing-Lite 在超长序列场景下表现不如 Attention。
