---
title: "Preisach Attention: A Hysteretic Model of Sequential Memory"
title-zh: "Preisach 注意力：基于迟滞模型的序列记忆注意力机制"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Piotr Frydrych]
year: 2026
arxiv: 2605.23603
tags: [attention, sequential-modeling, memory, transformers]
category: sequential-modeling
---

## 问题背景

标准 Transformer 的自Attention擅长捕捉序列中元素之间的相关性，但缺乏对"历史依赖路径"的建模能力——它不知道序列中的某个状态是如何通过一系列决策到达现在的。Preisach Attention 引入物理学中的迟滞（Hysteresis）模型来替代标准注意力，让序列模型具备"路径依赖"的记忆能力。

## 方法详述

**Preisach 迟滞模型简介：**
在物理学中，Preisach 模型用于描述具有记忆效应的系统（如铁磁材料），其当前状态不仅取决于当前输入，还取决于达到当前状态的完整路径。

**Preisach 注意力的实现：**
用 Preisach 算子替代标准注意力中的 softmax 加权：每个序列位置的历史对当前位置的影响，不仅取决于"距离"（如位置编码），还取决于从起点到该位置的"路径"（上下文历史）。这将注意力从"点对点的加权和"变为"路径依赖的积分"。

## 主要创新点

- 首次将 Preisach 迟滞模型引入深度学习Attention
- 为标准 Transformer 增加了路径依赖记忆能力，超越了位置编码和 RNN 的隐性记忆
- 为Sequence Modeling提供了一种全新的数学视角

## 局限性

- Preisach 算子的计算复杂度高于简单 dot-product attention
- 在标准 NLP 基准上的实证验证尚不充分
- 路径依赖在语义层面的可解释性需要进一步研究
