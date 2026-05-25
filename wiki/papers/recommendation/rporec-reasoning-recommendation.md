---
title: "RPORec: Reinforced Preference Optimization for Reasoning-Augmented Recommendations"
title-zh: "RPORec：面向推理增强推荐系统的强化偏好优化"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Jingtong Gao, Zeyu Song, Chi Lu, Xiaopeng Li, Derong Xu, Maolin Wang, Peng Jiang, Kun Gai, Qingpeng Cai, Xiangyu Zhao]
year: 2026
arxiv: 2605.21967
affiliation: Kuaishou
tags: [recommendation, rl, reasoning, cot]
category: recommendation
---

## 问题背景

大语言模型可以用推理能力（Chain-of-Thought）来增强推荐系统的可解释性和效果，但存在两个核心问题：(1) LLM 的推理过程（CoT）不一定与推荐目标对齐——模型可能在"推理"一些与推荐无关的内容；(2) 如何让推理能力真正服务于推荐指标（点击率、转化率等），而不是仅停留在"看起来合理"的阶段。

## 方法详述

RPORec 提出两阶段框架：

**阶段 1：推理增强推荐建模 (RARM)**
训练一个推荐特定的大语言模型，输入用户行为序列 + 候选 item 信息，模型不仅输出推荐分数，还输出一段自然语言推理过程（CoT）。这段 CoT 被送入一个轻量级推荐头（RecHead）作为辅助特征。

**阶段 2：强化推理精炼 (ARR)**
这是核心创新：使用强化学习（带可验证奖励的 RL）来优化 CoT 推理过程。具体来说：
- 将 CoT 生成视为策略 π
- 奖励信号来自推荐头 RecHead 对推荐结果的评分（点击率预估的准确性）
- 如果一段 CoT 帮助 RecHead 做出更准确的推荐，则获得高奖励；否则获得低奖励
- 通过Policy Gradient优化 CoT 生成策略

## 主要创新点

- **RL 对齐 LLM 推理与推荐目标**：首次将可验证奖励的 RL（类似 RLVR）应用于推荐场景，确保推理过程服务于推荐指标
- **推荐头作为验证器**：RecHead 充当 CoT 质量的"裁判"，CoT 好不好不靠人判断，而看它是否帮助了推荐决策
- **end-to-end推理-推荐联合优化**：CoT 生成和推荐决策在同一框架中联合优化，而非流水线式拼接

## 实验结果与对比

| 方法 | 推荐 AUC | 推理质量 (人工评分) | 线上效果 |
|------|---------|------------------|---------|
| 传统 DNN 推荐 | 0.812 | 无推理 | 基线 |
| LLM 直接推荐 (无 CoT) | 0.827 | 无推理 | +1.8% |
| LLM + 固定 CoT | 0.831 | 3.2/5 | +2.3% |
| LLM + CoT (未 RL 对齐) | 0.833 | 3.5/5 | +2.6% |
| **RPORec (RL 对齐 CoT)** | **0.842** | **4.1/5** | **+3.7%** |

**核心结论：**
- RL 对齐后的 CoT 不仅推荐效果更好（AUC 从 0.833 → 0.842），人工评分也更高（3.5→4.1）
- "推理质量"和"推荐效果"高度相关——更好的推理确实带来更好的推荐，证实了方法的有效性
- 线上部署后比 SOTA LLM 推荐方法提升 3.7%，说明 RL 对齐推理过程是值得的

## 局限性

- 两阶段训练流程复杂，需要同时维护推荐模型和 RL 策略
- RecHead 作为验证器的质量决定了 RL 的上限——如果 RecHead 本身不够准确，RL 会优化到错误方向
- CoT 推理增加了推理时的延迟开销，线上部署需要考虑
