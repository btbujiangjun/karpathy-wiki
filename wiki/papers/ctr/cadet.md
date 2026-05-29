---
title: "CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer"
title-zh: "CADET: 基于仅解码器Transformer的上下文条件广告CTR预测"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [LinkedIn]
year: 2026
venue: arXiv
arxiv: 2602.11410
tags: [decoder-only, ads, ctr, self-gated-attention, linkedin]
category: ctr
---

## 问题背景

广告 CTR 预测需要同时考虑广告上下文（用户、广告、场景）和序列行为，但 encoder-only 架构在条件化建模上存在局限。

## 方法详述

提出 CADET 仅解码器广告 CTR Transformer：

1. **Decoder-only 架构**：使用因果注意力替代双向注意力，更适合条件预测任务
2. **自门控注意力（Self-Gated Attention）**：可学习的门控机制调节各信息源的贡献
3. **时间戳 RoPE**：绝对时间的旋转位置编码，捕获广告投放的时序模式
4. **Flash Attention 集成**：利用 Flash Attention 提升推理效率
5. **全量部署**：LinkedIn 广告平台

## 主要创新点

1. 广告 CTR 预测的 Decoder-only 范式
2. 自门控注意力实现条件化建模
3. 时间戳 RoPE 的时序感知

## 实验结果对比

| 模型 | AUC | 参数量 | 推理延迟 | 上线收益 |
|------|-----|-------|---------|---------|
| DCN-V2 | 0.7950 | 100M | 1.0× | 基准 |
| RoBERTa | 0.8005 | 200M | 1.5× | - |
| CADET | 0.8065 | 150M | 1.1× | +3.5% CVR |

## 局限性

Decoder-only 架构在非自回归推荐场景可能浪费计算能力；自门控机制的参数量随输入规模增长。
