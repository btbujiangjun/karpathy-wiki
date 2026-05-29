---
title: "TokenFormer: Unify the Multi-Field and Sequential Recommendation Worlds"
title-zh: "TokenFormer: 统一多域推荐与序列推荐世界"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Tencent]
year: 2026
venue: arXiv
arxiv: 2604.13737
tags: [unified, multi-field, sequential, attention, tencent]
category: ctr
---

## 问题背景

多域特征交互（Multi-Field FI）和用户序列建模（Sequential Modeling）在推荐中通常使用两套独立的架构，导致信息孤岛和"序列坍缩传播"问题——序列注意力坍缩影响多域特征表达。

## 方法详述

提出 TokenFormer 统一架构，解决序列坍缩传播：

1. **Bottom-Full-Top-Sliding 注意力**：四层注意力金字塔，分别处理底层特征、全量交互、顶部聚合和滑动窗口
2. **序列坍缩检测机制**：量化注意力熵，监测坍缩程度
3. **坍缩传播阻断**：通过注意力分流防止坍缩从序列传播到多域特征
4. **统一表示空间**：多域 token 和序列 token 在统一空间中建模
5. **腾讯场景验证**

## 主要创新点

1. 首次识别并解决"序列坍缩传播"问题
2. Bottom-Full-Top-Sliding 四层注意力架构
3. 真正的多域-序列统一建模

## 实验结果对比

| 模型 | AUC | 注意力坍缩度 | 序列长度 |
|------|-----|------------|---------|
| 独立 FI + Seq | 0.8110 | 高 | 100 |
| 统一 Transformer | 0.8080 | 高 | 100 |
| TokenFormer | 0.8145 | 低 | 200 |
| TokenFormer-Large | 0.8170 | 低 | 1000 |

## 局限性

四层注意力的计算开销较高；坍缩检测阈值需要场景特定调优。
