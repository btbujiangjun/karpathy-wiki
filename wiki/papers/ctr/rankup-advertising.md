---
title: "RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems"
title-zh: "RankUp: 面向大规模广告推荐系统的高秩表示"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Tencent Weixin Team]
year: 2026
venue: KDD 2026
arxiv: 2604.17878
tags: [representation-collapse, ad-ranking, embedding, tencent]
category: ctr
---

## 问题背景

MetaFormer 架构随深度增加面临representation collapse（Representation Collapse）问题——有效秩（Effective Rank）随层数加深不再增长甚至下降。这意味着深层网络虽然参数更多，但实际表达能力并未提升，导致模型容量浪费。

## 方法详述

提出 RankUp，通过多视角嵌入方案缓解representation collapse：

1. **随机置换分割稀疏特征**：将稀疏特征随机分割为多份，每份独立嵌入
2. **多嵌入范式（Multi-Embedding Paradigm）**：同一特征在不同视角下获得不同表示
3. **全局 Token 集成**：引入全局 token 汇总多视角信息
4. **交叉预训练嵌入 Token**：通过预训练增强嵌入表示的协同性

## 主要创新点

1. 首次识别推荐系统中的representation collapse问题
2. 通过多视角嵌入增强表示多样性
3. 全量部署于微信视频号、公众号、朋友圈等场景

## 实验结果对比

| 场景 | GMV 提升 |
|------|---------|
| 微信视频号 | +3.41% |
| 公众号 | +4.81% |
| 朋友圈 | +2.12% |

## 局限性

架构复杂度增加带来了训练和推理成本的提升；多嵌入策略的超参数调优较为复杂。
