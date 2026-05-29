---
title: "Versioned Late Materialization: Data Infrastructure for Ultra-Long Sequence Training"
title-zh: "版本化延迟物化：超长序列训练的数据基础设施"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meta]
year: 2026
venue: arXiv
arxiv: 2604.24806
tags: [data-infrastructure, sequence-training, materialization, meta]
category: ctr
---

## 问题背景

超长用户行为序列（>10K）训练需要实时拼接大量特征数据，传统 ETL 方式在存储和 I/O 上均无法满足需求。

## 方法详述

提出版本化延迟物化（Versioned Late Materialization）数据基建方案：

1. **延迟物化**：仅存储原始事件 ID + 时间戳，训练时按需物化特征
2. **版本化快照**：特征 schema 版本化管理，支持时间旅行查询
3. **分层存储**：热数据在 SSD、温数据在 HDD、冷数据在对象存储
4. **预取优化**：基于训练 pipeline 的 I/O 预取策略
5. **在线/离线一致性**：训练与线上特征物料的一致性保证

## 主要创新点

1. 延迟物化首次应用于推荐训练数据管线
2. 版本化机制解决长序列的特征漂移问题
3. 支撑 >10K 序列长度的可行性

## 实验结果对比

| 方案 | 存储成本 | 训练 I/O 吞吐 | 支持最大序列长度 |
|------|---------|-------------|--------------|
| 传统 ETL | 1.0× | 1.0× | ~500 |
| 延迟物化无版本 | 0.3× | 1.5× | ~2000 |
| Versioned Late Mat. | 0.4× | 2.0× | 10000+ |

## 局限性

延迟物化增加训练 pipeline 复杂度；版本管理的运维成本较高；对 OLAP 类查询场景支持不足。
