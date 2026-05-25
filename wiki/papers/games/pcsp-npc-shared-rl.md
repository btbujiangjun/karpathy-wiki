---
title: "PCSP: One Policy, Infinite NPCs — Persona-Traceable Shared RL Policies for Scalable Game Agents"
title-zh: "PCSP：一个策略无限 NPC——面向可扩展游戏角色的角色可追踪共享强化学习策略"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Yoosung Hong]
year: 2026
arxiv: 2605.23652
category: games
tags: [games, rl, npc, persona, shared-policy]
category: games
---

## 问题背景

开放世界游戏需要大量非玩家角色（NPC），传统方法是每个 NPC 独立训练策略或使用基于规则的行为树。独立训练的计算成本随 NPC 数量线性增长；行为树则缺乏灵活性和真实性。理想情况下，应该有一个共享策略能控制任何 NPC，且能根据角色设定（Persona）产生不同的行为。

## 方法详述

**PCSP（Persona Conditioned Shared Policy）** 的核心思想是将角色设定与决策策略分离：

1. **角色嵌入**：将 NPC 的角色描述（如"性格暴躁的酒馆老板"）通过冻结的 LLM 编码为固定 embedding
2. **条件策略**：PPO 策略以角色 embedding 为条件，输入当前环境状态，输出动作
3. **多样性损失**：InfoNCE 一致性损失确保具有相似角色描述的 NPC 行为相近，不同角色描述的 NPC 行为不同
4. **KL 多样性正则**：额外 KL 散度regularization防止所有 NPC 收敛到相同的策略模式

## 主要创新点

- **零样本角色泛化**：未见过的角色描述，只需 LLM 编码即可控制，无需重新训练——17× 高于随机猜测的组合式角色识别率
- **22× 推理加速**：相比用 LLM 直接输出策略的基线，PCSP 使用轻量级 PPO 策略网络，推理只需 1-2ms
- **95%+ 语义-行为对齐**：Spearman ρ ≈ 0.73 表明角色描述的语义相似度与行为相似度高度一致

## 实验结果与对比

| 方法 | 角色行为分化度 | 推理延迟 (64 agents) | 零样本新角色 | 语义-行为对齐 (ρ) |
|------|--------------|-------------------|------------|----------------|
| 独立策略 (每个 NPC 1 个策略) | 最高 | 64× | ❌ 需要训练 | N/A |
| LLM-as-policy (GPT-4o) | 高 | 6.4s | ✅ | N/A |
| 共享策略 (无角色条件) | 无分化 | 1× | ❌ | N/A |
| **PCSP (本文)** | **高** | **1× (sub-frame)** | **✅ (17× above chance)** | **0.73** |

**核心结论：** PCSP 在 Unreal Engine 5 中实现了 64 个 NPC 同时以 sub-frame 延迟运行（22× 快于 LLM-as-policy 基线），且不同角色之间表现出可区分的行为模式。Spearman ρ ≈ 0.73 意味着角色的性格描述可以精确对应到行为差异。

## 局限性

- 角色 embedding 的质量依赖于 LLM 编码器，固定编码器无法处理极度微妙的角色差异
- InfoNCE 一致性损失的设计需要精心调参，否则角色差异度不够或过度分化
- 当前验证基于 300 个角色的仿真环境，在真实复杂游戏中的表现有待验证
