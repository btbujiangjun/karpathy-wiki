---
title: "ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization"
title-zh: "ImProver 2：面向神经符号证明优化的迭代自改进语言模型"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Riyaz Ahuja, Tate Rowney, Jeremy Avigad, Sean Welleck]
year: 2026
arxiv: 2605.22885
affiliation: Carnegie Mellon University
tags: [code-execution, formal-proof, self-improvement, neurosymbolic]
category: code-reasoning
---

## 问题背景

形式化证明（如 Lean、Coq 中的数学证明）的编写是一项高难度技能。LLM 可以辅助生成证明，但生成的证明往往冗长、低效或结构不佳。ImProver 2 提出让 LLM 对自己生成的证明进行迭代优化，结合神经符号方法（neurosymbolic）在保持正确性的同时提升证明质量。

## 方法详述

**迭代自改进循环：**
1. LLM 生成一个证明草稿
2. 形式验证器检查证明的正确性
3. 将验证器的反馈（错误位置、类型信息）和证明质量度量（长度、可读性）反馈给 LLM
4. LLM 根据反馈改进证明
5. 重复直到证明满足质量标准

**神经符号组件：**
使用符号验证器（Lean）提供刚性反馈，LLM 提供灵活修改能力，二者结合实现"符号验证 + 神经网络化改进"的协同。

## 主要创新点

- 自改进无需人类反馈，仅使用形式验证器的自动反馈
- 神经符号方法结合了符号系统的精确性和神经网络的灵活性
- CMU 出品（Sean Welleck 团队）

## 局限性

- 迭代优化可能陷入局部最优，无法产生结构性的证明重写
- 依赖于 Lean 验证器的反馈质量
- 证明质量度量的定义（如简洁性、可读性）需要人工设计
