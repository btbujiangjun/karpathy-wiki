---
title: "TubiFM: Unified Item, Carousel, and Search Ranking for Streaming Discovery"
title-zh: "TubiFM：面向流媒体发现的统一条目/轮播/搜索排序模型"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Alexandre Salle, Chenglei Niu, Suchismit Mahapatra, Xiaoxiao Chen, Suvash Sedhain, Yaqi Wang, Shervin Shahryari, Saurabh Agrawal, Qiang Chen, Michael Tamir]
year: 2026
arxiv: 2605.23702
affiliation: Tubi (Fox)
tags: [recommendation, ranking, llm, streaming]
---

## 问题背景

在视频流媒体平台（如 Tubi/Fox），推荐系统通常由多个独立模型组成：一个模型负责首页条目推荐（item ranking），另一个负责内容轮播排序（carousel ranking），第三个负责搜索排序（search ranking）。这种"竖井式"架构存在三个问题：(1) 每增加一个任务就需要独立开发和维护一个新模型；(2) 模型之间无法共享用户行为的跨面信息（例如搜索行为应影响首页推荐，反之亦然）；(3) 维护多套模型的基础设施成本高。Tubi 希望用单一模型统一所有排序任务，同时提升效果和效率。

## 方法详述

TubiFM 的核心思想是 "User Story"——一种序列化的统一用户表示：

**User Story 构建：**
将用户在所有表面的历史行为（观看记录、搜索查询、点击、收藏等）按时间顺序拼接为一条 token 序列。每种行为类型都有特殊的标记予以区分。例如：
```
[USER] [WATCH] movie_1 [WATCH] movie_2 [SEARCH] "action movies" [CLICK] movie_3 [LIKE] movie_4 ...
```

**模型架构：**
使用 Llama 3.2 1B 作为基础模型，通过 prompt 工程（而非微调）控制输出格式。对于不同的排序任务，在 user story 后附加不同的指令：
- 条目推荐：`[TASK: recommend_items]`
- 轮播排序：`[TASK: rank_carousel]`
- 搜索排序：`[TASK: rank_search] [QUERY: ...]`

模型为每个候选项目输出一个相关性分数，按分数排序返回 top-N。

## 主要创新点

- **User Story 统一表示**：首次将跨表面用户行为编码为单一 LLM 可处理的序列，替代多模型多架构方案
- **Prompt-as-Task-Switch**：无需微调，仅通过 prompt 指令切换任务模式，大幅简化模型维护
- **工业级上线验证**：不仅是研究实验，已在 Tubi 线上部署并验证了商业指标的提升

## 实验结果与对比

**离线评估（与独立专业模型对比）：**

| 任务 | 基线方法 | 架构 | 离线指标 | TubiFM | 提升幅度 |
|------|---------|------|---------|--------|---------|
| 条目推荐 | 独立 DNN 排序模型 | 多任务 DNN | NDCG@10 | 超越 | - |
| 轮播排序 | 独立轮播排序模型 | Transformer | 轮播 CTx | 超越 | **+0.30% TVT** |
| 搜索排序 | 独立搜索排序模型 | BERT-based | MRR@10 | 超越 | **+3.9% TVT** |

**线上 A/B 实验：**

| 指标 | 基线 | TubiFM | 提升 |
|------|------|--------|------|
| 搜索总观看时长 (Search TVT) | - | +3.9% | **+3.9%** |
| 轮播总观看时长 (Carousel TVT) | - | +0.30% | **+0.30%** |
| p99 服务延迟 | 500ms | **200ms** | **-60%** |
| GPU 部署 | L40S | L40S | 相同硬件 |

**核心结论：** 单一 Llama 3.2 1B 模型不仅统一了三种排序任务，效果还超越了各任务的专业独立模型。同时延迟降低了 60%（500ms → 200ms），基础设施显著简化。这表明 LLM 统一排序不仅可行，而且在效果和效率上都是更优解。

## 局限性

- 依赖 Llama 3.2 这样的商用/开源 LLM，存在模型许可和 API 依赖风险
- User Story 序列长度可能随用户活跃度增长，长序列的处理延迟和成本是潜在瓶颈
- 论文未对比微调方案与 prompt 方案的效果差异，prompt-only 方法在复杂任务上可能弱于微调
