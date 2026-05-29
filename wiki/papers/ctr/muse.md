---
title: "MUSE: Multimodal Search-Based Framework for 100K-Length Lifelong User Interest Modeling"
title-zh: "MUSE: 基于多模态搜索的十万级终身用户兴趣建模框架"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Alibaba]
year: 2025
venue: arXiv
arxiv: 2512.07216
tags: [multimodal, lifelong-interest, long-sequence, search-based, alibaba]
category: ctr
---

## 问题背景

用户终身行为（数月甚至数年）包含数万至数十万条记录，现有方法在扩展至 10 万级序列时面临严重的计算和存储挑战。

## 方法详述

提出 MUSE 多模态搜索框架：

1. **多模态编码**：将文本、图像、视频等多模态内容统一编码
2. **搜索式兴趣提取**：以目标物品为查询，在用户终身行为库中做高效搜索
3. **分层检索**：粗排→精排的两阶段搜索策略
4. **终身行为存储**：高效的向量存储和索引架构
5. **100K 序列验证**：在阿里场景验证超长序列的有效性

## 主要创新点

1. 首个 10 万级用户行为建模方案
2. 搜索式兴趣提取范式
3. 多模态统一编码的工业应用

## 实验结果对比

| 方案 | 序列长度 | AUC | 检索延迟 | 存储成本 |
|------|---------|-----|---------|---------|
| SIM | 1000 | 0.8055 | 5ms | 1.0× |
| ESD | 5000 | 0.8070 | 10ms | 2.0× |
| MUSE | 100000 | 0.8105 | 8ms | 1.5× |

## 局限性

多模态编码质量依赖预训练模型；搜索式方法可能在冷启动场景下失效。
