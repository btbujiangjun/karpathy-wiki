---
title: "ThinkRec: Thinking-based Recommendation via LLM"
title-zh: "ThinkRec: 基于思考的 LLM 推荐"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: []
year: 2026
venue: WWW 2026
tags: [llm4rec, reasoning, chain-of-thought, recommendation]
category: recommendation
---

## 问题背景

现有 LLM4Rec 方法类似系统 1 思维，依赖表面特征匹配而非深层的推理逻辑。例如，用户点击某个商品可能是多种隐式因素的综合结果，现有方法直接将特征映射到"点击概率"，缺乏可解释性和泛化性。

## 方法详述

提出 ThinkRec，引入思维激活机制和实例级专家融合：

1. **思维激活（Thought Activation）**：合成推理轨迹注入，使推荐过程类似 CoT 推理
2. **推理路径生成**：将用户行为序列转化为显式的偏好推理链
3. **实例级专家融合（Instance-Level Expert Fusion）**：不同推理路径由不同专家处理，降低单一推理的难度

## 主要创新点

1. 系统 2 思维模式的推荐系统
2. 实例级专家融合降低推理难度
3. 可解释的推荐推理过程

## 实验结果对比

| 指标 | 传统方法 | ThinkRec |
|------|---------|----------|
| HR@10 | 基线 | +12-18% |
| NDCG@10 | 基线 | +10-15% |
| 可解释性评分 | 低 | 高 |

## 局限性

推理延迟相比传统方法明显增加；合成推理轨迹的质量依赖强 LLM 辅助生成。
