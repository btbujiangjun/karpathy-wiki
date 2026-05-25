---
title: "GE4Rec: From Feature Interaction to Feature Generation — A Generative Paradigm of CTR Prediction Models"
title-zh: "GE4Rec: 从特征交互到特征生成——CTR 预测的生成式范式"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Tencent]
year: 2025
venue: arXiv
arxiv: 2512.14041
tags: [generative-ctr, feature-generation, tencent, paradigm-shift]
category: ctr
---

## 问题背景

传统 CTR 模型遵循discriminative paradigm：给定特征，预测点击概率。这种范式受限于已有特征的质量和交互方式，无法主动生成新的有信息量的特征表示。

## 方法详述

提出 GE4Rec，将 CTR 建模从判别式Feature Interaction转向监督式特征生成：

1. **特征生成机制**：模型不仅交互已有特征，还生成新的语义特征表示
2. **监督信号**：生成的特征通过下游 CTR 任务的损失进行监督优化
3. **生成-预测联合训练**：特征生成与 CTR 预测end-to-end联合优化

## 主要创新点

1. 判别式→生成式 CTR 范式转换
2. 特征生成替代Feature Interaction
3. end-to-end生成-预测统一框架

## 实验结果对比

| 方法 | 范式 | AUC | 特征利用率 |
|------|------|-----|-----------|
| DCN-V2 | 判别式交互 | 基线 | 低 (固定特征) |
| AutoInt | 判别式交互 | +0.2% | 低 |
| GE4Rec | 生成式 | +0.7% | 高 (动态生成) |

## 局限性

生成式计算成本较高；生成的特征可解释性有限；在极稀疏特征场景下生成质量不稳定。
