---
title: "Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation in Large Language Models"
title-zh: "Tree-of-Evolution: 树结构指令进化用于代码生成"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Ziyang Luo, Kaixin Li, Hongzhan Lin, Yuchen Tian, Mohan Kankanhalli, Jing Ma]
year: 2025
venue: ACL 2025
tags: [code-generation, instruction-evolution, data-synthesis, tree-search]
category: code-reasoning
---

## 问题背景

代码指令数据合成面临单向合成和随机性驱动的限制，导致数据质量和多样性不足。现有数据合成方法缺乏对生成质量的感知，无法根据前一步的生成结果来调整下一步的合成策略。

## 方法详述

将代码指令合成建模为树结构，探索多个进化路径：

1. **树结构进化（Tree-Structured Evolution）**：每个节点代表一种指令变体，分支探索不同进化方向
2. **优化驱动的迭代改进**：每步根据前一步质量（通过自动验证器）改进
3. **路径剪枝和选择**：基于合成质量的动态路径选择

## 主要创新点

1. 树结构指令进化替代线性合成
2. 优化驱动的迭代改进（非随机）
3. 大幅降低数据量需求

## 实验结果对比

| 基准 | ToE (75k 数据) | Qwen2.5-Coder-Instruct (百万级数据) |
|------|---------------|-----------------------------------|
| HumanEval | 92.1% | 92.0% |
| MBPP | 88.5% | 88.3% |

仅用 7.5 万样本即达到百万级数据训练的 SOTA 模型性能。

## 局限性

进化的计算成本随树深度增长；验证器的质量直接影响进化方向的有效性。
