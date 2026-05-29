---
title: "MTmixAtt: Integrating Mixture-of-Experts with Multi-Mix Attention for Large-Scale Recommendation"
title-zh: "MTmixAtt: 面向大规模推荐的混合专家与多混合注意力集成"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meituan]
year: 2025
venue: arXiv
arxiv: 2510.15286
tags: [moe, multi-mix-attention, scaling, meituan]
category: ctr
---

## 问题背景

推荐模型在扩展到 10 亿参数以上时，MoE 和多头注意力的组合面临专家利用不均衡和高计算开销问题。

## 方法详述

提出 MTmixAtt 集成 MoE 与多混合注意力：

1. **MoE 层**：稀疏激活专家网络，每 token 路由到 top-2 专家
2. **多混合注意力（Multi-Mix Attention）**：在注意力中混合多种聚合操作（max/mean/softmax）
3. **AutoToken**：自动 tokenization 策略，动态决定序列分割方式
4. **负载均衡**：专家级别的负载均衡损失
5. **1B 参数部署**：美团场景的十亿参数模型全量部署

## 主要创新点

1. MoE + 多混合注意力的首次工业应用
2. AutoToken 动态序列分割
3. 十亿参数 CTR 模型的线上验证

## 实验结果对比

| 模型 | 参数量 | AUC | 推理延迟 | 线上 CTR 提升 |
|------|-------|-----|---------|-------------|
| DCN-V2 | 200M | 0.8070 | 1.0× | 基准 |
| MoE-DCN | 1B (分散活) | 0.8105 | 1.2× | +1.2% |
| MTmixAtt | 1B (稀疏) | 0.8120 | 1.1× | +2.0% |

## 局限性

MoE 路由的负载均衡在大规模场景下仍需手工调整；AutoToken 策略的泛化性有待验证。
