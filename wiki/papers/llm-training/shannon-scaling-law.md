---
title: "LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws"
title-zh: "LLM 作为噪声信道：模型容量与缩放定律的香农视角"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Xu Ouyang, Deyi Liu, Yuhang Cai, Jing Liu, Yuan Yang, Chen Zheng, Thomas Hartvigsen, Yiyuan Ma]
year: 2026
arxiv: 2605.23901
venue: ICML 2026
category: llm-training
tags: [scaling-laws, information-theory, llm, theory]
---

## 问题背景

现有的 LLM Scaling Law（如 Chinchilla Scaling Law）假设模型容量和训练数据之间存在平滑的正相关关系：更多的参数和更多的训练数据总是带来更好的性能。但在实际训练中，研究人员观察到两个无法解释的反常现象：

1. **灾难性过训练（Catastrophic Overtraining）**：当训练 token 超过某个阈值后，继续训练反而导致模型性能下降，形成 U 形曲线。
2. **量化退化（Quantization Degradation）**：相同模型在量化后（如 4-bit），其能力退化程度随训练数据量变化呈现非单调模式。

这些现象表明现有Scaling Law是不完整的，缺少一个关键理论组件——噪声。

## 方法详述

本文提出了 **Shannon Scaling Law**，将 LLM 训练过程建模为信息通过噪声信道传输：

**核心类比：**
- 模型参数 ← 信道带宽 (Channel Bandwidth)
- 训练 token ← 信号功率 (Signal Power)
- 训练噪声（量化误差、数据噪声等）← 信道噪声 (Channel Noise)
- 模型性能 ← 信道容量 (Channel Capacity)

**数学形式：**

基于香农-哈特利定理 (Shannon-Hartley Theorem)：
```
C = B · log₂(1 + S/N)
```
其中：
- C: 信道容量（模型最大可能性能）
- B: 带宽（模型参数容量）
- S: 信号功率（训练信号强度）
- N: 噪声功率（量化噪声、数据噪声等）

当映射到 LLM 场景：
```
P_max(N_tokens) = α · N_param · log₂(1 + γ · N_tokens / N_noise)
```
其中 α、γ 是数据集相关的缩放常数，N_noise 是有效噪声功率。

**关键预测：**
该公式预测当训练 token 达到香农容量极限后，继续训练会进入"过噪声区"，模型开始拟合噪声而非信号，性能下降——精确解释了灾难性过训练的 U 形曲线。

## 主要创新点

- **首次建立Scaling Law的香农理论基础**：将信息论与 LLM Scaling Law统一，为后续改进提供了理论基础
- **解释非单调现象**：首次从理论上解释了为什么"更多的训练"不一定更好，以及量化为什么在过训练模型上影响更大
- **可验证的定量预测**：在 Pythia 和 OLMo2 系列上验证，R² = 0.847 的拟合精度表明这是一个强预测模型

## 实验结果与对比

**Scaling Law对比：**

| 能力 | Chinchilla Law | Kaplan Law | Shannon Scaling Law (本文) |
|------|---------------|-----------|--------------------------|
| 基本趋势 | ✅ 正相关 | ✅ 正相关 | ✅ 正相关 |
| 过训练 U 形曲线 | ❌ 无法解释 | ❌ 无法解释 | ✅ 精确预测 |
| 量化退化非单调性 | ❌ 无法解释 | ❌ 无法解释 | ✅ 精确预测 |
| 最优训练量预测 | ✅ 较好 | ⚠️ 欠佳 | ✅ 更优 (R²=0.847) |
| 理论基础 | 经验拟合 | 经验拟合 | **信息论（香农定理）** |

**具体验证结果：**

| 模型 | 预测最优 token 数 | Chinchilla 预测 | Shannon 预测 | 实际观察最优 |
|------|-------------------|-----------------|-------------|------------|
| Pythia-1.4B | 25.7B | 25.7B | 28B | ~30B |
| OLMo2-7B | 131B | 131B | 129B | ~130B |
| Pythia-12B | 305B | 305B | **307B** | 待验证 |

**量化场景预测：**
当模型训练到 3× 最优 token 数时：
- Chinchilla 预测：性能持平或提升
- Shannon 预测：性能下降（过噪声区）
- 实验验证：4-bit 量化下，过训练模型相对于最优训练模型的性能下降 **3.2×**

**核心结论：** 香农Scaling Law不仅拟合精度与 Chinchilla 相当（R²=0.847），还能解释和预测 Chinchilla 无法处理的非单调现象。这说明 LLM 训练本质上是一个有限容量信道的通信问题，而非简单的参数-数据缩放。

## 局限性

- 当前的噪声项 N_noise 是一个聚合值，没有对不同类型的噪声（量化噪声、数据噪声、标签噪声）分别建模
- 主要验证基于 Pythia 和 OLMo2 系列，在更大模型（100B+）上尚未验证
- 框架预测的是理想边界（香农容量），实际训练中优化器效率等因素可能使模型无法达到该边界
- 未讨论数据质量的影响，所有 token 被等同视为"信号"，但低质量数据本身就是噪声源
