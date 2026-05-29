---
title: "ENCODE: Efficient Clustering-Based Two-Stage Approach for Long-Term User Interest Modeling"
title-zh: "ENCODE: 基于高效聚类的两阶段长程用户兴趣建模"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Alibaba]
year: 2025
venue: TKDE 2025
arxiv: 2508.13567
tags: [clustering, long-term, interest-modeling, two-stage, alibaba]
category: ctr
---

## 问题背景

用户长期兴趣建模需要处理数万级的行为序列，传统方法在存储和计算上都难以支持。

## 方法详述

提出 ENCODE 两阶段聚类方法：

1. **第一阶段-聚类压缩**：对长历史序列做离线聚类，将行为聚为兴趣簇
2. **第二阶段-兴趣融合**：在线推理时基于目标物品查询相关兴趣簇
3. **高效索引**：聚类中心的高效向量检索
4. **兴趣动态更新**：增量式聚类更新策略
5. **可扩展架构**：与现有 CTR 模型的即插即用

## 主要创新点

1. 聚类方法的推荐长程兴趣建模
2. 离线-在线结合的高效方案
3. 增量更新支持兴趣漂移

## 实验结果对比

| 方法 | AUC | 存储成本 | 推理时间 | 支持序列长度 |
|------|-----|---------|---------|------------|
| 全量序列 | 0.8080 | 1.0× | 1.0× | ~500 |
| 随机采样 | 0.8040 | 0.3× | 0.3× | 5000 |
| ENCODE | 0.8075 | 0.2× | 0.4× | 10000+ |

## 局限性

聚类质量对兴趣表达有较大影响；聚类数目的选择缺乏自动化。
