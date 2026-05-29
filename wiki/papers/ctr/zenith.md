---
title: "Zenith: Scaling Up Ranking Models for Billion-Scale Livestreaming Recommendation"
title-zh: "Zenith: 面向十亿级直播推荐的排序模型规模化"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2026
venue: arXiv
arxiv: 2601.21285
tags: [livestreaming, real-time, ranking, scaling, bytedance]
category: ctr
---

## 问题背景

直播推荐场景对实时性要求极高（秒级响应），且直播内容特征（主播、商品、互动等）具有动态变化特性，传统排序模型无法有效扩展。

## 方法详述

提出 Zenith 直播排序缩放方案：

1. **实时特征交互缩放**：针对直播场景的动态特征交互扩展设计
2. **时间感知编码**：直播事件的时序编码与衰减建模
3. **多模态融合**：直播画面、语音、评论等多模态信号的联合建模
4. **在线学习管道**：支持分钟级模型更新以捕捉直播热度变化
5. **十亿级部署**：在每日数十亿次请求场景下的架构优化

## 主要创新点

1. 首个直播排序模型的缩放架构
2. 时间感知的动态特征交互
3. 实时特征交互的异步-同步混合计算

## 实验结果对比

| 指标 | 基线 DLRM | Zenith | 提升 |
|------|----------|--------|------|
| AUC | 0.7980 | 0.8065 | +0.85% |
| 直播 CTR | - | +3.2% | 线上 |
| 推理延迟 | 8ms | 9ms | +1ms |
| 模型参数量 | 100M | 300M | +200M |

## 局限性

结论局限于直播推荐场景；实时模型更新的稳定性和收敛性需要精细控制。
