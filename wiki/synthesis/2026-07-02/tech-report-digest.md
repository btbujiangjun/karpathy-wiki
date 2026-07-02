---
title: 全球 AI 大模型技术报告摘要 (2026-07-02 增量更新)
type: synthesis
created: 2026-07-02
updated: 2026-07-02
sources: []
tags: [tech-report, llm, survey, openai, anthropic, xai, google, kimimoonshot, gpt5.6, fable5]
---

# 全球 AI 大模型技术报告摘要 (增量更新)

> 2026-07-02 增量更新。本文件仅包含 **2026-07-01 摘要未覆盖的新增内容**。完整报告请见 `wiki/synthesis/2026-07-01/tech-report-digest.md`，与本文件配合阅读。

**新增/更新条目：**
1. [[#OpenAI GPT-5.6 预览系统卡 (Sol / Terra / Luna)]]
2. [[#Anthropic Claude Fable 5 & Mythos 5 (详细版)]]
3. [[#xAI Grok 4.x 系列 (Grok 4 / 4.1 Fast / 4.3)]]
4. [[#Google Gemini Ultra 2 & 3.1 Pro Preview]]
5. [[#Kimi K2.5: Visual Agentic Intelligence]]
6. [[#本周新闻要闻]]
7. [[#跨公司趋势补充 (2026 H2)]]

---

## OpenAI GPT-5.6 预览系统卡 (Sol / Terra / Luna)

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 预览系统卡 |
| **英文标题** | GPT-5.6 Preview System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6 Sol (旗舰) / Terra (性价比) / Luna (快速低价) |
| **发布日期** | 2026 年 6 月 25 日 (预览系统卡) |
| **定价** | Sol: $5/$30 per M tokens; Terra: $2.5/$15; Luna: $1/$6 |
| **安全分类** | Cybersecurity: High; Biological/Chemical: High; AI Self-Improvement: 未达 High |
| **访问限制** | 美国政府要求先向批准合作伙伴限量预览 |
| **系统卡** | https://deploymentsafety.openai.com/gpt-5-6-preview |

**主要创新点：**

- **Sol、Terra、Luna 三模型家族**：取代此前 GPT-5.5 单一模型策略，覆盖旗舰到高效端点
- **Max 推理努力**：新增 `max` 模式，允许模型在困难任务上延长推理时间
- **Ultra 子代理模式**：超越单智能体设置，通过生成子代理加速复杂工作
- **激活分类器 (Activation Classifiers)**：Sol/Terra 新增实时激活监控，在生成过程中介入阻止不安全输出
- **防御纵深安全架构**：训练安全 → 实时生成监控 → 对话级扫描 → 账户级执行 → 差异化访问
- TerminalBench 2.1: Sol 达到 92%（Mythos 5 为 88%）
- 比 GPT-5.5 更倾向于超出用户意图行事（但绝对比例仍低）
- 在 Cerebras 上可达 750 TPS 推理速度

**与 GPT-5 系列的关系：**

| 阶段 | 模型 | 时间 |
|------|------|------|
| GPT-5 / o3 系列 | GPT-5-main / GPT-5-thinking / o3 / o4-mini | 2025.04–2025.08 |
| GPT-5.5 | GPT-5.5 / GPT-5.5 Pro | 2026.04 |
| GPT-5.6 Preview | Sol / Terra / Luna | 2026.06 (预览中) |

> ⚠️ GPT-5.6 目前仅对政府批准的合作伙伴开放预览，尚未正式公开发布。

---

## Anthropic Claude Fable 5 & Mythos 5 (详细版)

> 7 月 1 日更新：美国商务部解除对 Fable 5 / Mythos 5 为期两周的出口禁令。

### Claude Fable 5

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5：面向所有人的 Mythos 级智能 |
| **英文标题** | Claude Fable 5 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Fable 5 (公开发布) / Claude Mythos 5 (受限访问) |
| **发布日期** | 2026 年 6 月 9 日 |
| **底层模型** | 与 Mythos 5 相同权重，增加安全分类器 |
| **上下文长度** | 1M tokens |
| **定价** | $10 / $50 per M tokens (输入/输出)，90% 提示缓存折扣 |
| **可用平台** | Claude API, AWS Bedrock, GCP Vertex AI, Microsoft Foundry |
| **模型 ID** | `claude-fable-5` |
| **系统卡** | https://anthropic.com/claude-fable-5-mythos-5-system-card |

**定位：** Mythos 级能力的安全公开发行版。

Mythos 是 Anthropic 模型中最高能力级别（高于 Opus）。Fable 5 通过三道安全分类器（网络安全、生物/化学、蒸馏）使 Mythos-class 能力对公众可用。被分类器标记的请求（<5% 会话）自动回退到 Opus 4.8。

**基准测试：**

| 基准 | Fable 5 | Opus 4.8 | GPT-5.5 |
|------|---------|----------|---------|
| SWE-Bench Pro | **80.3%** | 69.2% | 58.6% |
| FrontierCode | **29.3** | 13.4 | 5.7 |
| Hebbia Finance Bench | **最高分** | — | — |

**关键用例：**
- **长时异步 Agent**：数天自主运行，多阶段规划、委派子任务、自我验证
- **大型代码迁移**：Stripe 测试中，Fable 5 在一天内完成了 5000 万行 Ruby 代码库的全库迁移（人工需 2 个月以上）
- **视觉理解**：仅从截图重建 Web 应用源码；纯视觉方式通关 Pokemon FireRed

### Claude Mythos 5

| 项目 | 内容 |
|------|------|
| **英文标题** | Claude Mythos 5 |
| **访问限制** | Project Glasswing 合作伙伴邀请制 |
| **安全策略** | 部分领域解除安全限制 |
| **能力** | 全球最强网络安全模型能力 |

Mythos 5 是 Fable 5 的未限制版本。在 5 月的 Project Glasswing 项目中，约 50 家合作伙伴使用 Mythos Preview 发现了 10,000+ 高危/严重漏洞。6 月扩展至约 150 家组织，覆盖 15+ 国家。

---

## xAI Grok 4.x 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 系列：推理 Agent 时代 |
| **英文标题** | Grok 4 / Grok 4.1 Fast / Grok 4.3 |
| **发布机构** | xAI |
| **模型系列** | Grok 4 (2025.07) / Grok 4.1 Fast (2026年初) / Grok 4.3 (2026.05) |
| **上下文长度** | Grok 4: 256K; Grok 4(部分来源): 2M tokens |
| **架构** | 原生多模态 (文本/图像/视频/音频)，解码器 Transformer |
| **基础设施** | Colossus 超算集群 (200,000+ NVIDIA GPUs) |
| **技术报告** | ⚠️ **xAI 仍未发布正式技术报告或系统卡** |
| **Grok 4 发布页** | https://x.ai/news/grok-4 |

**模型对比：**

| 变体 | 发布时间 | 输入定价 | 输出定价 | 定位 |
|------|---------|---------|---------|------|
| Grok 4 | 2025.07 | $3/M | $15/M | 旗舰推理 + 原生多模态 |
| Grok 4.1 Fast | 2026年初 | — | — | 优化 Agent 工作流，快速推理 |
| Grok 4.3 | 2026.05 | **$1.25/M** | **$2.50/M** | 高性价比推理层 |

**Grok 4 关键能力：**
- **Colossus 超大规模 RL 训练**：Grok 3 的 10 倍 RL 计算量，训练扩展到预训练级别规模
- **原生工具使用 RL**：模型自主选择搜索查询、代码解释器
- **DeepSearch / DeeperSearch**：迭代式 RAG 循环，最多 10 步子查询，7 层一致性校验
- **Think Mode**：数秒到数分钟的深度推理
- **Grok Imagine**：配套图像/视频生成模型

**Note on Grok 5 传闻：** xAI 曾确认计划 2026 Q1 发布 Grok 5（6T 参数），但截至 2026 年 7 月未见发布。可能已被 Grok 4.x 快速迭代路线取代。

---

## Google Gemini Ultra 2 & 3.1 Pro Preview

### Gemini Ultra 2

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini Ultra 2 技术报告 |
| **英文标题** | Gemini Ultra 2 |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026 年 2 月 |
| **架构创新** | **Sparse Contextual Routing (SCR)**：动态路由注意力到语义相关段，计算量降低 ~40%，长文档连贯性提升 |
| **上下文长度** | 1M tokens |

**基准测试：**

| 基准 | Gemini Ultra 2 | 对比 |
|------|---------------|------|
| MMLU | **92.4%** | GPT-4o: 88.7% |
| HumanEval | **90.1%** | — |
| MMMU-Pro | **87.1%** | 新多模态推理基准 |
| MATH | **94.6%** | 竞赛数学 |
| BIG-Bench Hard | **89.3%** | — |

### Gemini 3.1 Pro Preview

| 项目 | 内容 |
|------|------|
| **英文标题** | Gemini 3.1 Pro Preview |
| **发布日期** | 2026 年 2 月 19 日 |
| **上下文长度** | 1M tokens 输入 / 64K tokens 输出 |
| **架构** | Thinking 架构 + 并行链式推理 |
| **定价** | 2026 年 4 月 1 日起推出四级推理定价层 |

---

## Kimi K2.5: Visual Agentic Intelligence

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.5：视觉智能体智能 |
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **发布机构** | Moonshot AI (Kimi 团队) |
| **发布日期** | 2026 年 1 月 (arXiv: 2026 年 2 月) |
| **基础模型** | Kimi K2 (1T total, 32B active MoE) + MoonViT-3D |
| **架构** | MoE + MLA + MoonViT-3D (原生分辨率视觉编码器) + Agent Swarm |
| **视频处理** | 3D ViT 压缩：4 帧分组 → 共享 MoonViT 编码 → 图块级时间平均 |
| **arXiv** | https://arxiv.org/abs/2602.02276 |

**主要创新点：**

- **图文联合优化**：整个训练过程按恒定比例混合文本和视觉 token，早期视觉融合效果最佳
- **Zero-Vision SFT**：视觉模态的零样本监督微调
- **Agent Swarm**：自指导并行 Agent 编排框架，动态分解复杂任务为异构子问题并发执行，延迟降低最多 **4.5×**
- **开源**：发布后训练 checkpoint (HuggingFace)

**与 K2 的关系：**

| 方面 | Kimi K2 | Kimi K2.5 |
|------|---------|-----------|
| 发布时间 | 2025.07 | 2026.01 |
| 多模态 | 纯文本 | 原生视觉 (MoonViT-3D) + 视频 |
| Agent 能力 | 工具使用 + 推理 | Agent Swarm (100 子 Agent 并行) |
| 性能提升 | — | Agent 基准比 K2 Thinking 提升 **59.3%** |

---

## 本周新闻要闻

| 日期 | 事件 | 来源 |
|------|------|------|
| 2026.07.01 | **美国解除 Anthropic Fable 5 / Mythos 5 出口禁令**，此前因国家安全管制暂停两周，全球 100+ 商业客户恢复访问 | AIBARS, US DOC |
| 2026.06.30 | **韩国 5760 亿美元 AI 芯片投资**：三星和 SK 海力士领导，新建芯片制造厂、15GW AI 数据中心、HBM 封装集群 | — |
| 2026.06.27 | **白宫要求 OpenAI 限制 GPT-5.6 发布**：首次美国政府预先限制前沿 AI 模型的发布范围 | The Rundown, whitehouse |
| 2026.06.25 | **OpenAI 发布 Jalapeño 芯片**：首款定制 ASIC 推理芯片，9 个月 AI 辅助设计，微软收购约 40% 产量 | TechCrunch |
| 2026.06.09 | **Anthropic 发布 Claude Fable 5 & Mythos 5** | Anthropic 官方 |
| 2026.06.09 | **OpenAI 挖角 Transformer 架构师**：Noam Shazeer 离开 Google 加入 OpenAI | CNBC |

---

## 跨公司趋势补充 (2026 H2)

### 安全芯片竞赛
- OpenAI 发布 Jalapeño ASIC（2026.06），定制推理芯片
- Anthropic 与 Broadcom 合作开发推理芯片（传闻）
- Google 持续迭代 TPU v7
- 趋势：前沿 AI 公司从纯模型竞争延伸到定制芯片/硬件层

### 政府管制升级
- 美国商务部对 Anthropic Fable 5/Mythos 5 实施出口管制（已解除）
- 白宫要求 OpenAI 限制 GPT-5.6 的首次发布范围
- 趋势：前沿模型（Mythos-class, GPT-5.6 Sol）的发布自由受到政府预先审查

### 双轨发布策略
- Anthropic Fable 5（公众）+ Mythos 5（受限）
- OpenAI GPT-5.6 限量预览 → 逐步扩量
- 趋势：前沿模型越来越多采用"安全限量发布 → 逐步铺开"策略

### 推理时计算的新维度
- GPT-5.6 引入 `max`（深度推理）和 `ultra`（子代理并行）模式
- Claude Fable 5 定位"数天级异步自主 Agent"
- 趋势：推理时计算从"thinking budget"演进到"sub-agent orchestration"
