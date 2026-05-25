---
title: "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
title-zh: "门控注意力：非线性、稀疏性与无注意力下沉"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: []
year: 2025
venue: NeurIPS 2025 Best Paper (Runner-up)
tags: [attention, llm, long-context, architecture]
category: llm-training
---

## 问题背景

标准 Attention在long-context场景中面临attention sink和不稳定的问题。attention sink指模型将过多注意力权重分配给初始 token，限制了long-context建模的有效性。此外，标准注意力缺乏非线性调制能力，导致训练不稳定。

## 方法详述

在缩放点积注意力后添加 sigmoid 门控，引入非线性和稀疏调制：

1. **gating mechanism**：在 softmax 注意力输出后应用 sigmoid 门控，实现逐元素非线性调制
2. **稀疏诱导**：门控值的稀疏性自动抑制低效注意力连接
3. **消除attention sink**：gating mechanism打破初始 token 的注意力聚集效应

## 主要创新点

1. 简单有效的gating mechanism，几乎不增加参数
2. 从根本上消除attention sink问题
3. 提升训练稳定性，支持更大learning rate

## 实验结果对比

| 指标 | 标准注意力 | Gated Attention |
|------|-----------|----------------|
| long-context基准 | 基线 | 显著提升 |
| 最大learning rate | 受限 | 支持更大 LR |
| attention sink | 存在 | 消除 |
| 训练稳定性 | 中等 | 改善 |

## 局限性

对已有预训练模型的后向兼容性需要微调适配；门控引入的额外计算在极端规模下需优化。
