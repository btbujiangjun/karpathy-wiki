---
title: "OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender"
title-zh: "OneTrans: 工业推荐中一个 Transformer 统一特征交互与序列建模"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2025
venue: arXiv
arxiv: 2510.26104
tags: [unified, transformer, sequence-modeling, feature-interaction, bytedance]
category: ctr
---

## 问题背景

传统推荐模型将特征交互（Feature Interaction）与序列建模（Sequence Modeling）分离为独立模块，导致信息流通受限且架构冗余。

## 方法详述

提出 OneTrans 统一架构：

1. **统一分词器（Unified Tokenizer）**：将多域特征和行为序列统一编码为 token 序列
2. **因果注意力**：所有 token 在单一 Transformer 中做因果注意力建模
3. **KV 缓存复用**：用户侧 token 的 KV 缓存可在请求间复用
4. **联合优化**：特征交互和序列建模在统一空间中完成
5. **工业部署**：抖音场景全量部署

## 主要创新点

1. 首个将特征交互和序列建模完全统一的 Transformer 架构
2. KV 缓存复用显著降低计算冗余
3. 统一分词器消除多模块间信息损耗
4. 字节跳动全量部署验证

## 实验结果对比

| 模型 | AUC | 计算量 | 推理延迟 | 参数量 |
|------|-----|-------|---------|-------|
| DCN-V2 + Transformer | 0.8120 | 1.0× | 1.0× | 200M |
| OneTrans | 0.8165 | 0.7× | 0.8× | 180M |

## 局限性

统一 token 空间可能导致特征交互被序列建模"淹没"；KV 缓存随用户序列长度线性增长。
