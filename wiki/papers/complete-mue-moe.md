---
title: "Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models"
title-zh: "Complete-muE：MoE 模型的最优超参数迁移与缩放"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang]
year: 2026
arxiv: 2605.23893
tags: [moe, hyperparameter-transfer, scaling]
category: llm-training
---

## 问题背景

混合专家模型（Mixture-of-Experts, MoE）通过稀疏激活大幅扩展了模型容量，但超参数搜索变得极其复杂。MoE 的超参数包括：专家数量、激活专家数（top-k）、专家容量（capacity）、专家粒度（fine-grained vs coarse）、是否使用共享专家、是否使用分组平衡等。传统做法需要对每组配置单独调参，成本极高。本文希望实现"稠密模型调一次，所有 MoE 变体直接迁移"。

## 方法详述

Complete-muE 提出**双桥系统 (Two-Bridge System)**：

**桥 I：稠密 → 稠密 MoE**
基于最大更新参数化（μP, Maximal Update Parameterization），建立稠密 FFN 到稠密 MoE 的宽度缩放映射：
- 保持激活宽度（active width）一致时，learning rate可直接迁移
- 稠密 MoE 的 expert 数量与learning rate呈亚线性关系

**桥 II：稠密 MoE → 稀疏 MoE**
建立激活专家数（top-k）与learning rate之间的映射关系：
- 激活专家数增加时，learning rate需要按比例调整
- 专家容量、粒度、共享专家等变体可通过有效参数预算统一

**最终方案：**
"Tune dense once, transfer to all"——只需对稠密模型调一次超参（learning rate、初始化范围等），即可直接迁移到任意 MoE 配置，无需重新搜索。

## 主要创新点

- **首个统一的 MoE 超参数迁移框架**：覆盖激活专家数、容量、粒度、共享/分组平衡等所有常见 MoE 变体
- **双桥系统**：分别处理稠密→稠密 MoE 和稠密 MoE→稀疏 MoE 两个层级，理论清晰
- **大幅降低 MoE 训练成本**：避免对每种配置独立调参，加速 MoE 研究与部署

## 实验结果与对比

| MoE 配置 | 不使用 Complete-muE | 使用 Complete-muE | 差距 |
|----------|-------------------|-------------------|------|
| Top-2, 8 experts | ❌ 需要独立调参 | ✅ 直接迁移 | 收敛速度匹配 |
| Top-4, 32 experts | ❌ 需要独立调参 | ✅ 直接迁移 | 收敛速度匹配 |
| Fine-grained, 64 experts | ❌ 需要独立调参 | ✅ 直接迁移 | 收敛速度匹配 |
| Shared expert + Top-2 | ❌ 需要独立调参 | ✅ 直接迁移 | 收敛速度匹配 |
| Group-balanced MoE | ❌ 需要独立调参 | ✅ 直接迁移 | 收敛速度匹配 |

**核心结论：** 所有测试的 MoE 变体在使用 Complete-muE 迁移超参数后，收敛速度与独立调参得到的最优配置相当，验证了"Tune dense once, transfer to all"的可行性。

## 局限性

- 框架主要验证了learning rate和初始化范围的迁移，未覆盖优化器动量、权重衰减等其他超参
- 极度稀疏配置（如 top-1, 1024 experts）下的迁移效果尚未验证
- 对模型架构的变化（如不同激活函数、归一化层）是否同样鲁棒有待进一步研究
