---
title: "CHIME: Compressive Framework for Holistic Interest Modeling with LLM and Residual VQ"
title-zh: "CHIME: 基于LLM编码与残差VQ压缩的全方位兴趣建模框架"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Kuaishou]
year: 2025
venue: arXiv
arxiv: 2504.06780
tags: [llm, vq, compression, interest-modeling, kuaishou]
category: ctr
---

## 问题背景

用户行为建模需要同时考虑短期上下文、长期兴趣和动态意图，但统一建模这些维度的计算成本极高。

## 方法详述

提出 CHIME 压缩式全方位兴趣建模框架：

1. **LLM 编码**：使用 LLM 对用户行为序列做深层语义编码
2. **残差 VQ 压缩**：多级残差向量量化将长序列压缩为紧凑表示
3. **全方位融合**：短期上下文 + 长期兴趣 + 动态意图的三元融合
4. **压缩-解压缩架构**：编码器端压缩，解码器端按需解压缩
5. **快手工业场景验证**

## 主要创新点

1. LLM 编码 + 残差 VQ 的非配对组合
2. 压缩式全方位兴趣建模
3. 编码器-解码器的非对称设计

## 实验结果对比

| 模型 | AUC | 序列压缩率 | 存储成本 | 推理时间 |
|------|-----|-----------|---------|---------|
| 基线 (未压缩) | 0.8080 | 0% | 1.0× | 1.0× |
| CHIME-4× | 0.8095 | 75% | 0.3× | 0.6× |
| CHIME-16× | 0.8080 | 93.75% | 0.1× | 0.4× |

## 局限性

LLM 编码的推理开销较高；残差 VQ 的训练稳定性对超参数敏感。
