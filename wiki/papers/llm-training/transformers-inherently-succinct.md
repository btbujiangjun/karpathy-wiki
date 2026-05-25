---
title: "Transformers are Inherently Succinct"
title-zh: "Transformer 天生简洁"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin]
year: 2026
venue: ICLR 2026 Outstanding Paper
tags: [transformer, theory, representation, succinctness]
category: llm-training
---

## 问题背景

Transformer 相比 RNN、CNN 等架构在语言建模和推理任务上展现出显著优势，但其底层能力来源缺乏严格的理论解释。为什么 Transformer 在某些任务上比其他架构更加参数高效？这个问题缺乏正式的理论框架来回答。

## 方法详述

从计算复杂性理论角度证明 Transformer 在编码某些概念时的简洁性：

1. **形式化简洁性**：定义 Transformer 简洁性为表示特定函数所需的最小参数规模
2. **复杂度对比**：证明 Transformer 在表示某些正则语言和层次结构时，参数量远小于 RNN 等架构
3. **理论下界**：给出特定函数类的 Transformer 参数下界

## 主要创新点

1. 提出 Transformer 简洁性的理论框架
2. 严格的复杂度对比分析
3. 激发对架构表示的进一步研究

## 实验结果对比

| 架构 | 表示层次结构所需参数 | 表示正则语言所需参数 |
|------|-------------------|-------------------|
| Transformer | O(log n) | O(1) |
| RNN | O(n) | O(n) |
| 传统电路 | O(n) | O(log n) |

## 局限性

理论结果在极大规模模型上的实证验证有限；目前分析主要覆盖特定函数类。
