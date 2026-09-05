---
title: "LLM Tech Report Digest — 2026-09-05"
type: synthesis
created: 2026-09-05
updated: 2026-09-05
tags: [tech-report, llm, moe, multimodal, reasoning, coding, agentic, cyber, security, computer-use, cost, daily-digest, open-weights]
sources: []
---

# LLM Tech Report Digest — 2026-09-05

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要（**Delta 版**）。
> 上一基准为 [[../2026-09-04/tech-report-digest]]（Delta）与 [[../2026-08-31/tech-report-digest]]（全量 19–20 家机构）。本日聚焦 **09-04 → 09-05** 窗口增量。
> 📉 **本窗口无任何新 tech report / system card 发布**——09-03 GPT-6 Astra 正式发布与 09-01 Fable 5.1 发布后处于短期真空。窗口内变化集中在**即将到来的发布预告**（xAI Grok 4.7）与**既有发布的规格细化/生态落地**（Qwen3.8-Flash-Next = Qwen4 架构预览、Fable 5.1 GA 全面铺开）。
> 与当日 arXiv 相关去重：论文层面见 [[arxiv-daily]]、[[arxiv-ai-search]]、[[arxiv-paper-check]]、[[conference-digest]]（同目录）。
> Last updated: 2026-09-05

---

## 目录 / Table of Contents

| #   | 机构                  | 模型                                                        | 发布日期       | 本窗口状态                          |
| --- | ------------------- | ----------------------------------------------------------- | ---------- | --------------------------------- |
| 1   | OpenAI              | GPT-6 Astra（正式发布）                                        | 2026-09-03  | 无新增（昨日头号事件）                      |
| 2   | Anthropic           | Claude Fable 5.1 / Mythos 5.1                               | 2026-09-01  | 无新增（前基准）；GA 落地方案/迁移风险 09-04 逐项拆解 |
| 3   | Google DeepMind     | Gemini 3.8 Flash / 3.8 Flash Cyber                          | 2026-09-02  | 无新增（前基准）；Model Card 09-02 已录       |
| 4   | Meta AI             | Muse Spark 1.3                                              | 2026-09-02  | 无新增（前基准）                         |
| 5   | Qwen (Alibaba)      | Qwen3.8-Flash-Next（Qwen4 架构预览）                            | 2026-08-26  | **规格细化：125B / ~6B active（20:1）+ 51B 系统 RAM 组件** |
| 6   | DeepSeek            | DeepSeek-V4 系列                                             | 2026-04~08  | 无新增                              |
| 7   | Microsoft           | MAI-Thinking-1 / Phi                                        | 2026-08     | 无新增                              |
| 8   | NVIDIA              | Nemotron 3 Ultra                                            | 2026-06     | 无新增                              |
| 9   | xAI                 | **Grok 4.7（未发布）**                                         | 预期 09-12   | **首个官方时间线：2.1T 新预训练，SpaceX 补充训练** |
| 10  | 腾讯 Tencent          | Hy4 preview                                               | 2026-08-28  | 无新增                              |
| 11  | Zhipu AI            | GLM-5.3 / 5.3-Flash                                         | 2026-08     | 无新增                              |
| 12  | Moonshot AI         | Kimi K3                                                   | 2026-07-16  | 无新增                              |
| 13  | StepFun             | Step 系列                                                   | 2025~2026   | 无新增                              |
| 14  | ByteDance           | Seed 系列                                                   | 2026-06/08  | 无新增                              |
| 15  | Baichuan            | Baichuan-M4 / M3                                           | 2026-06/01  | 无新增                              |
| 16  | InternLM            | Intern-S2 / S1                                              | 2026-08/03  | 无新增                              |
| 17  | 01.AI               | Yi-Lightning（2024）                                         | 2024-10     | 无新增（已转企业应用/主权 AI 方向）             |
| 18  | Amazon              | Nova 2                                                     | 2025-12/2026 | 无新增                              |
| 19  | Apple               | AFM 3                                                      | 2026-06-08  | 无新增（2026 技术报告仍处 "later this summer" 承诺期） |
| 20  | Mistral AI          | Shieldstral / Small 4 / Large 3                            | 2026-03/08  | 无新增                              |

---

## 9. xAI — Grok 4.7（📅 未发布 · 预期 09-12 · 首个正式时间线）

> ⚠️ **NOTE**：本窗口无新 report，但 **Grok 4.7 迎来首个创始人层面的正式倒计时**——Musk 于 09-02 发帖称 "Grok 4.7 comes out in 10 days"，指向 **09-12**。这取代了此前 08-12 "3–4 周" 的窗口估计。**截至 09-04 仍无 xAI 官方 spec sheet**：docs.x.ai 模型列表仍止步 grok-4.6，无 model ID、无定价、无 context window、无 benchmark card——所有参数数字均为 Musk 声明，非 xAI 文档。

| 字段 | 内容 |
|------|------|
| **作者声明(非官方)** | ~**2.1T 参数**（vs Grok 4.6 的 1.5T，+40%）；**全新预训练**（非 4.6 后训练刷新）；supplemental training 注入 "massive amount" of **SpaceX 工程数据** |
| **官方时间线** | 07-25 "4 周" → 08-12 "3–4 周" → **09-02 "10 天"（⇒ 09-12）**；三次顺延后首次硬性倒计时 |
| **Musk 声称** | "will exceed all current models"（含 Fable 5 但不明确对 Fable 5.1）；"better than 4.6 in every way, except slightly slower to serve, with better token efficiency"；"Grok will be the best at real-world engineering" |
| **定位** | 4.6（08-12，AA Intelligence Index 61）后的旗舰新基底，主打真实世界工程 / agentic |
| **确认状态** | 截至 09-04 无 model ID / pricing / context window / benchmark card；release 仍属 founder target 而非发布日期 |
| **信源** | techjournal.org / nextbigfuture / orcarouter / x.com @elonmusk（09-02 帖子） |

**跟进要点**：Grok 4.5 / 4.6 实际落地均晚于窗口预告，09-12 仍可能顺延。发布后应追踪：官方 model card、AA 指数、$2/$6 定价是否延续、500K context 是否继承、SpaceX 语料对工程类评测的实际增益（目前仅 Musk 声称）。

---

## 5. Qwen (Alibaba) — Qwen3.8-Flash-Next（Qwen4 架构预览 · 规格细化）

> **非本窗口新发布**（08-26 随 Qwen3.8 Flash 家族发布，08-31 基准已录）。窗口内（09-04 新闻报道）首次补全的**架构细节**值得单独记录——这是 Qwen4 架构的公开预览，也是本月最值得关注的 open-weight 架构信号。

| 字段 | 内容 |
|------|------|
| **模型** | Qwen3.8-Flash-Next（open-weight，**Qwen4 架构 preview**） |
| **总参数量** | **125B 总 / ~6B active**（≈ **20:1 激活稀疏**） |
| **新增架构亮点** | 独立 **51B 参数组件设计为运行在系统 RAM（system memory）中而非 GPU 显存**——异构内存分解（GPU-MoE 主体 + RAM-side 辅助组件） |
| **背景** | 与其同代的 Qwen3.8-Flash / 3.8-Max-0902（09-02，2.4T 编码快照，CodeArena 1691）分属不同骨架 |
| **许可（窗口内新信息）** | 今年夏天共 **4 个 open-weight 版本、4 个不同 license，无一为 Apache 2.0**——Qwen 许可证策略分化明显（与腾讯 Hy4 Apache 2.0 形成对照） |
| **信源** | aitoolsrecap.com/Blog/ai-news-september-04-2026；orcarouter Qwen3.8 Flash 条目（08-26） |

**跟踪点**：Qwen4 架构若把"系统 RAM 侧组件"做成通用范式，将对本地/边缘推理的硬件假设产生实质影响（MoE 激活稀疏 + 冷参数下沉内存）。Qwen3.8-Flash 定价 $0.15/$0.47 per 1M 为窗口内第三方记录。

---

## 2. Anthropic — Claude Fable 5.1 / Mythos 5.1（GA 落地与迁移风险拆解）

> 前基准（09-01 发布，09-02/09-04 已详录 AA 指数 66、Terminal-Bench-Science 52.6%、SWE-bench Verified 95.0%、ProofBench 100%、1M ctx / 128K out、无长上下文溢价）。**本窗口无新发布**；09-03/09-04 出现两篇针对**落地成本与 breaking change** 的拆解，值得作为运维级跟进点：

- **定价结构**（Codersera 09-03）：Fable 5.1 = 09-01 发布，**输入 $10 / 输出 $50 per 1M 与 Fable 5 持平**；**Cache Read 由 $1.00 降至 $0.25 per 1M（-75%）**——Anthropic 估计典型负载 -25%、高 agentic 负载最高 -45% 成本。该价格杠杆主要利好长跑 agent 类负载。
- **Breaking changes**：`tool_choice` 为 `any`/`tool` 的 forced tool use 现返回 **400 错误**；thinking blocks 处理、编辑历史对话（edited conversation histories）语义发生变化——迁移后**必须重跑 evals**（mlq.ai 09-04）。
- **规范细节**：1M context 为 default 且按统一 token 单价计费（无长上下文溢价）；129K→约 30K 语义 counter-intuitive——准确规格为 **128,000 max output**；tokenizer 沿用 Opus 4.7 引入者（同文本 token 数 +~30%）；知识 cutoff **2026-06**；**退役承诺不早于 2027-09-01**（Fable 5 已转入 "Legacy models（仍可用）"）。
- **GA 生态落地**（09-01）：GitHub Copilot **直发 GA**（Copilot Pro+/Max/Business/Enterprise，缺省需数据留存以运行安全分类器，ZDR 仅合格企业豁免至今年底，之后转 Enterprise Frontier Safeguards）；AWS / GCP / Microsoft Foundry 同日可用。
- **安全面**：Fable 5.1/Mythos 5.1 为同一模型不同护栏档；护栏介入时 OSWorld 2.0 / AutomationBench 计 0（与 09-04 基准 OSWorld 口径矛盾记录一致）。09-04 报道背景：AI agent 安全事件成为公众审视焦点。

---

## 1, 3, 4, 6–8, 10–20. 其余 17 家机构——无新 tech report / system card

- **OpenAI**（GPT-6 Astra 09-03 正式发布，Critical 评级 / "AGI era"）——本窗口无新增；公开发布仍在 "coming days" / gated Daybreak 阶段。
- **Google DeepMind**（Gemini 3.8 Flash / 3.8 Flash Cyber，09-02）——无新增；3.8 Flash intro 定价有效期至 **12-31**。
- **Meta**（Muse Spark 1.3，09-02）、**DeepSeek**（V4 系列 04~08）、**Microsoft**（MAI-Thinking-1 从零训练 / no-distillation）、**NVIDIA**（Nemotron 3 Ultra，混合 Mamba MoE）、**腾讯**（Hy4 preview 08-28，770B-A49B Apache 2.0）、**Zhipu**（GLM-5.3 744B-A40B）、**Moonshot**（Kimi K3 2.8T MoE）、**StepFun**、**ByteDance**（Seed）、**Baichuan**、**InternLM**（S2/S1）、**Amazon**（Nova 2）、**Apple**（AFM 3，2026 tech report 仍处 "later this summer" 承诺、暂未见发布）、**Mistral**（Agentic Search 08-20 / Shieldstral 08-04 / Small 4）——均无本窗口新增。
- **01.AI 备注**：无新模型活动。2024-12 重组后已从 frontier pretraining 转企业/主权 AI（万智平台 2025-03、万策平台 2026-07 老板 AI / 销冠 AI / 投资官 AI）；被 Presenc AI 评为已被 DeepSeek/Qwen/Kimi/GLM 全面超越；公开模型封顶 Yi-Lightning（2024-10，千亿 MoE，LMSYS 全球第 6）+ Yi tech report（arXiv:2403.04652）。

---

## 近期时间表（09-05 → 09-15）

| 日期 | 事项 |
|------|------|
| 09-08 07:00 UTC | Mercury 2.5 80% 优惠价到期 |
| 09-12（预期） | **xAI Grok 4.7**（2.1T 新预训练 + SpaceX 数据；Musk 09-02 倒计时） |
| 09-14 | Claude Code weekly-limit 调整落地（此前 09-04 观察：settling ~17% lower） |
| 09 月内 | Anthropic **Enterprise Frontier Safeguards（EFS）** 上线（"this fall" 承诺） |
| 12-31 | Google Gemini 3.8 Flash 引入价到期 |
| 11-02 | xAI 退役 grok-imagine-image-quality（路由至 grok-imagine-image-2.0 low quality，降价） |

---

## 本窗口趋势观察

1. **发布真空 = 预告军备**：09-01/09-02/09-03 密集发布后，窗口内无新报告；注意力转向 **Grok 4.7 的 09-12 倒计时**与 9 月中下旬可能的 Fable 5.2 / OpenAI 后续。三家（OpenAI/Anthropic/xAI）竞相把下世代挂到 "数天到数周" 的显式时间线上。
2. **"straight-to-GA" 取代 phased rollout**：Fable 5.1 09-01 同日上 API + Bedrock + GCP + Foundry + Copilot；Astra 09-03 仍走 gated 受信分阶段——**能力越强、Gating 越严的分化在加深**。紧跟的运维成本（cache 定价、breaking change、迁移 re-eval）成为竞争叙事新维度。
3. **Open-weight 架构进入"异构内存"赛道**：Qwen3.8-Flash-Next（125B/6B active + 51B 系统 RAM 组件）把 MoE 稀疏激活与"冷参数下沉系统内存"结合，直指本地/边缘推理的硬件假设——与 NVIDIA Nemotron 3 混合 Mamba、DeepSeek CSA/HCA、腾讯 Hy4 722 的架构创新同台。
4. **许可策略分化**：Qwen 夏秋 4 个 open-weight 版本 4 种 license（无 Apache），对照 Hy4（Apache 2.0）与 GLM-5.3（$10B 门槛）——open-weight 阵营的"开放"定义进入逐家谈判时代。