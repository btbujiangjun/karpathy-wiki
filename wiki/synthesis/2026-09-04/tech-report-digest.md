---
title: "LLM Tech Report Digest — 2026-09-04"
type: synthesis
created: 2026-09-04
updated: 2026-09-04
tags: [tech-report, llm, moe, multimodal, reasoning, coding, agentic, cyber, security, computer-use, cost, daily-digest]
sources: []
---

# LLM Tech Report Digest — 2026-09-04

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要（**Delta 版**）。
> 上一基准为 [[../2026-09-03/tech-report-digest]]（Delta）与 [[../2026-08-31/tech-report-digest]]（全量 19–20 家机构）。本日聚焦 **09-03 → 09-04** 窗口增量。
> ⚡ **本窗口头号事件**：OpenAI **GPT-6 Astra 正式发布**（09-03，System Card + Safety Overview 同步；首个被 Rated **Critical** 的模型，Brockman 称 "AGI era"）。
> 其余机构：Anthropic Fable 5.1 / Mythos 5.1（09-01）仍为本窗口前基准与 AA 指数 66 SOTA；Google Gemini 3.8 Flash、Meta Muse Spark 1.3、Qwen3.8-Max-0902（09-02）为昨日基准，均无新增。
> 与当日 arXiv 相关去重：论文层面见 [[arxiv-daily]]、[[arxiv-ai-search]]、[[arxiv-paper-check]]、[[conference-digest]]（同目录）。
> Last updated: 2026-09-04

---

## 目录 / Table of Contents

| #   | 机构                  | 模型                                                        | 发布日期       | 本窗口状态                          |
| --- | ------------------- | --------------------------------------------------------- | ---------- | ------------------------------ |
| 1   | **OpenAI**          | **GPT-6 Astra（正式发布）**                                     | **2026-09-03** | **🆕 头号事件：首个 Critical 评级 + "AGI era" 发布** |
| 2   | Anthropic           | Claude Fable 5.1 / Mythos 5.1                               | 2026-09-01  | 无新增（前基准，AA 指数 66 SOTA）           |
| 3   | Google DeepMind     | Gemini 3.8 Flash / 3.8 Flash Cyber                          | 2026-09-02  | 无新增（昨日基准）                        |
| 4   | Meta AI             | Muse Spark 1.3                                              | 2026-09-02  | 无新增（昨日基准）                        |
| 5   | Qwen (Alibaba)      | Qwen3.8-Max-0902                                            | 2026-09-02  | 无新增（昨日基准）                        |
| 6   | DeepSeek            | DeepSeek-V4 (Pro / Flash / Flash-Vision-Exp)              | 2026-04~08  | 无新增                             |
| 7   | Microsoft           | MAI-Thinking-1 / Phi                                        | 2026-08     | 无新增                             |
| 8   | NVIDIA              | Nemotron 3 Ultra                                            | 2025-12/2026 | 无新增                             |
| 9   | xAI                 | Grok 4.6 / Grok 5（延后）                                     | 2026-08-12  | Grok 5 仍延后                       |
| 10  | 腾讯 Tencent          | Hy4 preview                                               | 2026-08-28  | 无新增                             |
| 11  | Zhipu AI            | GLM-5.3 / 5.3-Flash                                         | 2026-08     | 无新增                             |
| 12  | Moonshot AI         | Kimi K3                                                   | 2026-07-27  | 无新增                             |
| 13  | StepFun             | Step 系列                                                   | 2025~2026   | 无新增                             |
| 14  | ByteDance           | Seed 系列                                                   | 2026-06/08  | 无新增                             |
| 15  | Baichuan            | Baichuan-M4 / M3                                           | 2026-06/01  | 无新增                             |
| 16  | InternLM            | Intern-S2 / S1                                              | 2026-08/03  | 无新增                             |
| 17  | 01.AI               | Yi-Lightning                                               | 2024-12     | 无新增                             |
| 18  | Amazon              | Nova 2                                                     | 2025-12/2026 | 无新增                             |
| 19  | Apple               | AFM 3                                                      | 2026-06-08  | 无新增                             |
| 20  | Mistral AI          | Shieldstral / Small 4 / Large 3                            | 2026-03/12  | 无新增                             |

---

## 1. OpenAI — GPT-6 Astra（🆕 本窗口头号事件 · 首个 Critical 评级 · "AGI era"）

> ⚠️ **NOTE**：本轮为**正式发布/Safety Overview + System Card**。09-01 曾报道 "Astra 触发 Critical 网络安全门槛、限最强工具访问、仍未发布"（只有 Path to Astra 预告）；**09-03 正式发布终结该状态**——已进入 gated 分阶段提供，公开发布在 "coming days"。Brockman 明确称 "generational leap"，并称这可能被后世视为 **AGI 到来的标志**。这也使 GPT-6 Astra 成为 OpenAI 首个在自身 Preparedness Framework 下被评定 **Critical（网络安全）** 级别的模型。

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-6 Astra：新一代智能（世界最强、最对齐的模型） |
| **英文标题** | GPT-6 Astra: A new generation of intelligence |
| **发布机构** | OpenAI |
| **模型系列** | GPT-6（前代 GPT-5.6 / GPT-5.6 Sol） |
| **发布日期** | **2026-09-03**（Safety Overview + 发布博客 + System Card 同步；"Path to Astra" 预告 09-01） |
| **参数量** | 未公开（proprietary） |
| **评级 / 定位** | 首个被 OpenAI Preparedness Framework 评为 **Critical（网络安全）** 的模型；"world's most intelligent / most aligned model" |
| **定价** | **$10 / $50 每百万 input/output tokens**（VentureBeat） |
| **核心能力** | Computer use（计算机操作）、浏览、软件工程、网络安全、科学、专业工作；"computer use" 为主打（像人一样操作系统：填表、CRM、表格、Power BI、KiCad/FreeCAD） |
| **关键基准** | ARC-AGI-3 **99.9%**；FrontierMath Tier 4 **98%**；ExploitBench **100%**（vs GPT-5.6 Sol 78.5%）；ExploitGym **42.4%**（vs 30.3%，且用更少输出 token）；OSWorld 2.0 **72.6%**（vs Sol 65.7%，~40 分/任务 vs 75） |
| **新增亮点** | 内部 "ExploitBench (2026-06~08)" 新颖基准上执行任意代码率远高于 Sol 且 token 更少；评估中自行发现并用上 **2 个未知 zero-day**，均已向维护者披露 |
| **访问方式** | 分阶段：先限 cybersecurity 应用式项目（Daybreak）组织；公众 Plus/Pro/Business/Enterprise 用户 "coming days" |
| **安全 / 治理** | Safety Overview 09-03 强调：更高风险场景更安全、agentic 有害请求（暴力攻击规划/欺诈）处理更安全、相对 5.6 Sol 有 Pareto 改进、<18 岁年龄分层更一致；回应 08 月 Hugging Face 越狱事件的背景 |

**与 Anthropic Fable 5.1 对比（跨源）**：Astra 宣称在 computer/browser use 上同时超过 Opus 5 与 Fable 5 且成本更低。OSWorld 2.0 的 Claude 数字按 Anthropic 官方设置（非 Fable 5.1 修改过的任务/评分）复现（OpenAI 脚注 4）。

> ⚠️ **CONTRADICTION / CAVEAT（记录在案，非本 wiki 裁决）**：Anthropic Fable 5.1 card 称其 OSWorld 2.0 在护栏介入时被计 0；OpenAI 用官方设置复现 Claude 分数进行对比。两家的 OSWorld 数字口径不同（护栏/任务修改差异），直接横比需谨慎。（详见 [[../2026-09-02/tech-report-digest]]）

---

## 2. Anthropic — Claude Fable 5.1 / Mythos 5.1

> 前基准（09-01 发布，09-02 基准已详细录入）。本窗口无新增。关键规格回顾：同权重双安全档 System Card（09-01，212 页）；AA Intelligence Index **66**（前沿 SOTA）；Terminal-Bench-Science 0.1 **52.6%**；SWE-bench Verified **95.0%** / Pro **80.0%**；ProofBench v1.1 **100%**；1M ctx / 128K out；Cache Read **-75%**；alignment risk 由 very low 升至 **low**；Mythos 5.1 限 trusted-access（Project Glasswing）最强 cyber。完整见 https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card

---

## 3–5. Google / Meta / Qwen（昨日基准，无新增）

- **Google Gemini 3.8 Flash / 3.8 Flash Cyber**（09-02）— 基于 3.7 持续训练，AA 指数 59，同价 $0.75/$3.75，Flash Cyber 前沿网络防御（见 [[../2026-09-03/tech-report-digest]]）。
- **Meta Muse Spark 1.3**（09-02）— AA 指数 61/62，长期 agentic 工作流，即将开放权重。
- **Qwen3.8-Max-0902**（09-02）— 2.4T 编码快照，CodeArena 1691 登顶，超 Opus 5 三项。

## 6–20. 其余 15 家机构——无新 tech report / system card

DeepSeek（V4 系列 04~08）、Microsoft（MAI-Thinking-1 / Phi）、NVIDIA（Nemotron 3 Ultra，混合 Mamba MoE）、xAI（Grok 5 仍延后）、腾讯（Hy4 preview 08-28）、Zhipu（GLM-5.3 744B-A40B，08-28 权重开源）、Moonshot（Kimi K3 2.8T MoE）、StepFun（Step 系列）、ByteDance（Seed 系列）、Baichuan（Baichuan-M4/M3 医疗垂直）、InternLM（Intern-S2/S1）、01.AI（Yi-Lightning）、Amazon（Nova 2）、Apple（AFM 3，06-08）、Mistral（Shieldstral/Small 4/Large 3）——均无本窗口新增。xAI Grok 5（~6T 参数，Colossus 2）仍处延后状态。

---

## 本窗口趋势观察

1. **首个 "Critical" 门槛被正式跨越**：GPT-6 Astra 是 OpenAI 第一个官方 Critical（网络安全）模型，也是首个有 3 家（OpenAI/Anthropic/Google, xAI 报道）围绕 "cyber-capable + gated trusted-access" 展开的旗舰——安全评级与能力发布深度绑定。
2. **"AGI era" 措辞正常化**：Brockman 携发布称 AGI era；Guardian/Fortune/CNBC 头条跟进。与 09-02 趋势中的 "网络安全=新前端赛道" 一致，这是该叙事首次落到官方发布。
3. **Computer use 成为 SOTA 定义战场**：OSWorld 2.0（Astra 72.6%）成为各家（OpenAI/Anthropic/Google）争相引用的头牌 benchmark，但**评分口径不统一**（护栏计 0 / 官方设置 / 任务修改），跨厂对比需看各厂自己披露才可依赖。
4. **成本杠杆持续**：Astra $10/$50 与 Fable 5.1 cache -75% 并立——前端能力 + 成本效率同台竞争。
