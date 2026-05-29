---
title: "UG-Sep: Compute Only Once: UG-Separation for Efficient Large Recommendation Models"
title-zh: "UG-Sep: 用户通用特征分离——大规模推荐模型只需计算一次"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2026
venue: arXiv
arxiv: 2602.10455
tags: [efficiency, user-model, redundancy-reduction, bytedance]
category: ctr
---

## 问题背景

推荐模型在扩展时，同一用户在不同广告/物品上的请求重复计算用户侧的不变特征，导致大量冗余计算。

## 方法详述

提出用户通用特征（User-General, UG）分离机制：

1. **UG 分离**：将模型分为用户通用部分（UG）和物品相关部分（Item-Specific）
2. **计算一次**：同一用户的 UG 部分在每个请求批次中只计算一次
3. **缓存策略**：UG 特征的跨请求缓存与增量更新
4. **一致性保证**：UG 缓存与模型参数更新的版本同步
5. **架构适配**：兼容 DLRM、DCN、Transformer 等主流架构

## 主要创新点

1. 用户通用特征分离的正式化与系统化
2. 计算冗余的量化分析与消除
3. 低成本实现模型有效扩展

## 实验结果对比

| 策略 | 推理 FLOPs | 延迟 | AUC | 线上 QPS |
|------|-----------|------|-----|---------|
| 基线 (无分离) | 1.0× | 10ms | 0.8000 | 10K |
| UG-Sep (1×) | 0.45× | 6ms | 0.8015 | 18K |
| UG-Sep (2×放大) | 0.70× | 8ms | 0.8055 | 14K |

## 局限性

UG 分离假设用户侧特征在短期内不变，高频更新场景下可能引入缓存失效开销。
