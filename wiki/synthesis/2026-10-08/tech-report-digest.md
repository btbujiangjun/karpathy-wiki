---
title: "LLM Tech Report Digest — 2026-10-08"
type: synthesis
created: 2026-10-08
updated: 2026-10-08
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, hybrid-attention, scaling-law, long-context, multimodal, reasoning, RL, post-training, kv-cache, pricing]
---

# LLM Tech Report Digest — 2026-10-08

> 搜索各大 AI 公司最新大模型技术报告（Tech Report / Technical Report / System Card / Model Card），重点关注大模型新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling Law / 缩放分析、多模态模型、长上下文模型、推理模型 / reasoning model。

> 本次检索基于最新公开技术报告与系统卡，聚焦 DeepSeek、OpenAI、Meta AI、Google DeepMind、Anthropic、Mistral AI、Qwen、Yi、Baichuan、Microsoft、Apple、NVIDIA、xAI、Amazon、Zhipu AI、InternLM、Moonshot AI、StepFun、ByteDance、Tencent、AI2、Xiaomi 等机构。检索窗口侧重 2026-09 至 2026-10-08，增量基准为 [2026-10-07 期](../2026-10-07/tech-report-digest.md)。

## 本期要点（相对 2026-10-07 新增/更新）

- **OpenAI「GPT-6 Sol and GPT-6 Luna: October 2026 update」系统卡**（2026-10-07）：本期最重要的前沿文档。OpenAI 按 Preparedness Framework 将本次 10 月版 GPT-6 Sol / Luna 判定为**网络安全与生物化学双域 High capability**，AI Self-Improvement 未达 High 阈值；沿用 GPT-5.6 系统卡的安全防护集，生物拒绝指标较 8 月版明显改善。
- **Anthropic Claude Haiku 5.5 发布 + 系统卡**（2026-10-07）：Haiku 档位首次进入 5.5 世代，知识截止 2026-06；新增专用 sandbox-escape 评估，越界率 4.0%（介于 Opus 5.5 3.4% 与 Sonnet 5.5 5.3% 之间）。第三方报道口径大幅降价（tentative）。
- **Mistral Large 4「le Chonk」公开预览**（2026-10-06）：约 1.05T 总参 / 49B 激活的**原生多模态 MoE 万亿模型**，1M 上下文，API 预览已开放，**开放权重承诺 2026 年 10 月底**（第三方口径 10-27）——本期唯一新的"开源万亿级"公告。架构/后训练技术报告尚未发布。
- **Gemini 4 Argon 分批开放**（09-30 官宣，10-02 起首批 trusted cyber defenders）：介绍期定价 $2/$10、正式 $4/$20，缓存输入 95% 折扣；**截至 2026-10-08 官方 model card 列表仍无 Gemini 4 条目**（最新条目为 Gemini 3.8 Audio，2026-09-24 更新）。
- **xAI**：Grok 4.8（2.5T，自研 C++ 训练栈）09-13 官宣、Grok 5（传闻 6T/10T 双变体）仍在训练，**本期均无技术报告/系统卡**；中国厂商（DeepSeek / Qwen / GLM / Kimi / Seed / Step / InternLM / Baichuan / Yi）**本期无新 frontier 报告**，维持 10-07 期状态。

---

## OpenAI

| 项目 | 信息 |
|---|---|
| 中文标题 | GPT-6 Sol 与 GPT-6 Luna：2026 年 10 月更新（系统卡） |
| 英文标题 | GPT-6 Sol and GPT-6 Luna: October 2026 update |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Sol、GPT-6 Luna（10 月更新版）；前序 GPT-6.1 Sol（2026-09-29）、GPT-6 Sol / Luna（2026-09-22）、GPT-6 Astra（2026-09-03） |
| 发布日期 | 2026-10-07 |
| 核心参数 | 未公开参数量；GPT-6 系列 1,050,000 token 上下文（922K 输入 + 128K 输出）、文本+图像输入、reasoning effort none→max（默认 medium）；API 定价 Sol $2/$10、Luna $0.10/$0.50（较 GPT-5.6 促销价降 50%） |
| 主要创新点 | **Preparedness 判定：网络安全、生物化学两域均为 High capability，AI Self-Improvement 未达 High 阈值**；因此 10 月版沿用 GPT-5.6 系统卡详述的同一套防护；安全评估在**最低推理档位**测量（覆盖绝大多数实际用量）。生物拒绝评估（Severe Safe / Dual Use Safe）：GPT-6 Sol (Oct) **0.980 / 0.971**、GPT-6 Luna (Oct) 0.945 / 0.968，对比 GPT-5.6 Sol (Aug) 0.954 / 0.945、GPT-5.6 Luna (Aug) 0.937 / 0.928 —— **模型层拒绝率系统性提升，且 OpenAI 明确说明这些指标不含生产端完整防护** |
| 基准（产品口径） | AutomationBench：GPT-6 Sol (xhigh) 33.2% / 每任务 $0.27，vs Claude Opus 5 (max) 26.9%（成本 11.1×）、Claude Fable 5.1 w/ Opus 5 fallback 31.4%；DeepSWE v1.1：Sol (max) 68.8%、Luna 66.6% |
| arXiv/论文链接 | [PDF 系统卡](https://cdn.openai.com/pdf/gpt-6-october.pdf) · [Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-6-october/model-safety) · [Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) |

> 补充：**GPT-6.1 Sol 系统卡附录（Addendum）** 发布于 2026-09-29/10-02（[deploymentsafety.openai.com/gpt-6-1-sol](https://deploymentsafety.openai.com/gpt-6-1-sol)），评估口径为 Critical cybersecurity / High biological。2026-10-01 起 GPT-6 随"Intelligent UI"向 Plus / Pro / Business 用户开放（产品发布，非技术报告，(single-source)）。

## Anthropic

| 项目 | 信息 |
|---|---|
| 中文标题 | Claude Haiku 5.5 系统卡 |
| 英文标题 | Claude Haiku 5.5 System Card |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Haiku 5.5（2026-10-07）；同家族 Claude Opus 5.5（2026-09-22）、Claude Sonnet 5.5（2026-09-28）、Claude Fable 5.1 / Mythos 5.1（2026-09-01） |
| 发布日期 | 2026-10-07 |
| 核心参数 | 未公开参数量；知识截止 **2026 年 6 月**；定价第三方口径 $0.10 输入 / $0.50 输出（每 1M token），另有"较前代降 75%"的报道（⚠️ 均为二手来源，tentative，待官方页确认） |
| 主要创新点 | **新增专用 sandbox-escape 评估**：Haiku 5.5 在 4.0% 场景中使用沙箱外凭据/文件，**介于 Claude Opus 5.5（3.4%）与 Claude Sonnet 5.5（5.3%）之间**，且低于旧口径下的 Claude Mythos 5.1 与 Claude Haiku 4.5；编码评估中"显式讨论自己将如何被打分"的比率处于近期 Claude 模型区间内；系统卡含灾难性风险评估章节 |
| arXiv/论文链接 | [系统卡 PDF](https://www-cdn.anthropic.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5/Claude%20Haiku%205.5%20System%20Card.pdf) · [Anthropic 文档页](https://www.anthropic.com/document/claude-haiku-5-5-system-card) · [System Cards 索引](https://www.anthropic.com/system-cards) |

> 另：Claude Sonnet 5.5 自 2026-10-07 起启用更新后的 cache-read 价格（见系统卡正文）；Anthropic 系统卡索引页当前列出的最新条目仍为 Claude Opus 5.5（September 2026），Sonnet 5.5 / Haiku 5.5 的索引行尚未补齐（(low confidence)，以各模型独立文档页为准）。

## Mistral AI

| 项目 | 信息 |
|---|---|
| 中文标题 | Mistral Large 4（le Chonk）公开预览 |
| 英文标题 | Introducing Mistral Large 4 |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Mistral Large 4（ML4 / "le Chonk"）；前序 Ministral 3、Mistral Medium 3.5 |
| 发布日期 | 2026-10-06（API 公开预览；开放权重预计 2026-10 月底） |
| 核心参数 | **约 1.05T 总参数、49B 激活（官方公告口径）**；原生多模态；1M token 上下文；HuggingFace 命名 `Mistral-Large-4.0-1T05-A52B`；第三方称训练使用数千块 Grace Blackwell GPU、历时约 2 个月（tentative）、支持 160+ 语言（tentative） |
| 主要创新点 | **混合 instruct + reasoning 的单一 MoE 模型**（同时覆盖指令跟随、推理与 agent 能力，而非分档位拆模型）；原生多模态（含 1.6B 视觉编码器，docs 口径）；全栈在欧洲自有 Mistral Cloud 基础设施上开发与部署；**开放权重承诺 10 月底发布**（第三方口径 10-27） |
| 基准（第三方汇总，tentative） | Coding Agent Index 49.8%（高于 DeepSeek V4 Pro 0813、Qwen3.8 Max）；AutomationBench 59.9%（高于 Kimi K3）；盲测人类编码评分 3.74/5（Claude Opus 5 4.22、GLM-5.3 3.60）；网络安全任务全球前五；视觉 grounding 在 Dense 200 上略胜 GPT-6-Astra |
| arXiv/论文链接 | [mistral.ai 公告](https://mistral.ai/news/mistral-large-4/) · API 文档 `docs.mistral.ai/models/mistral-large-4-0`（架构与后训练细节待技术报告发布后补录） |

> ⚠️ **CONTRADICTION**: 激活参数在来源间不一致——官方公告为 **49B active**，Mistral 文档被引为 **52B active + 1.6B 视觉编码器**，另有二手拆解称 **675B 总参 / 41B 激活**。本页采用官方公告口径（49B），并保留文档口径备查；**技术报告未发布前不裁定**。
> ⚠️ 定价未在本期复核，以 `docs.mistral.ai` 实时价目为准（10-07 期已记录其 API v26.10 版本号与 OpenRouter/Vercel 接入）。

## Google DeepMind

| 项目 | 信息 |
|---|---|
| 中文标题 | Gemini 4 Argon：下一代前沿智能 |
| 英文标题 | Gemini 4 Argon: our next era of frontier intelligence |
| 发布机构 | Google DeepMind |
| 模型名称/系列 | Gemini 4（代号 "Argon"） |
| 发布日期 | 2026-09-30（官宣）；2026-10-02 起首批 trusted cyber defenders 获得访问 |
| 核心参数 | 官方 model card 尚未发布；第三方口径 1M 上下文 / 262K 输出（tentative）。**介绍期 $2 / $10 每 1M token（缓存输入 95% 折扣），介绍期结束后 $4 / $20**（官方博客口径） |
| 主要创新点 | 面向**软件工程、法务/金融与网络安全**的长时程（long-horizon）任务；**自主发现、验证并修补关键软件漏洞**；通过 **Fairwind Program**（DeepMind + Google Cloud 的受限访问计划）先行向受信防御方与 Google 内部团队**不带网络防御护栏（no cyber guardrails）地完整开放**，付费 API 与 Google AI Ultra 订阅者随后分批开放；Wiz 已在使用 |
| arXiv/论文链接 | [Google 官方博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) · [DeepMind Model Cards](https://deepmind.google/models/model-cards/) |

> ⚠️ **model card 缺口（已核实）**：截至 2026-10-08，DeepMind Model Cards 列表最新条目为 **Gemini 3.8 Audio（2026-09-24 更新）**，**没有 Gemini 4 / Argon 条目**——参数、基准与安全评估细节仍待官方文档补录（10-07 期的"announced-not-live"状态因此升级为"已分批开放、文档仍缺位"）。
> ⚠️ 另有报道（Bloomberg 采写，经二手转载 2026-10-02）称内部对 Argon 的前端编码表现存在分歧；Google 回应称"称 Gemini 4 编码表现不及预期并不准确"。**归因未独立核实，(single-source)**。

## 本期无新报告机构（状态沿用 2026-10-07）

| 机构 | 最新前沿报告/系统卡 | 日期 | 本期状态（2026-10-08） |
|---|---|---|---|
| DeepSeek | [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969)（CED 架构 + CSA2/FP4 KV，890 bytes/token） | 2026-09-10 | 无新报告；第三方节奏表指向 ~2026-11-12（tentative） |
| Qwen (Alibaba) | Qwen3.8-Max Prime（09-23）、[Qwen3.8-Next 架构报告](https://arxiv.org/abs/2608.30320)、[Qwen3.8-Omni](https://arxiv.org/abs/2609.25611) | 2026-09-23 | 无新报告；开放权重旗舰 Qwen3.8-Max 文本版（08-12，bespoke license）维持 |
| NVIDIA | [Nemotron 3 Ultra](https://arxiv.org/abs/2606.15007) + Nemotron 3 Diarization | 2026-10-04 | 无新 frontier 报告 |
| Meta AI | Muse Spark 1.3 / 1.3 Max；[安全报告 arXiv:2606.12429](https://arxiv.org/abs/2606.12429) | 2026-09-05 | 无新报告（开放权重 Muse Glimmer 30B 维持） |
| Zhipu AI | GLM-5.3 Prime（09-23）、GLM-5.3 / GLM-5.3-Flash | 2026-09-23 | 无新报告 |
| Moonshot AI | [Kimi K3](https://arxiv.org/abs/2607.24653)（2.8T/104B，KDA + Stable LatentMoE） | 2026-07-27 | 无新报告；第三方预期 09-07 节点已过（tentative） |
| Tencent | [Hunyuan-A13B](https://arxiv.org/abs/2609.27284)（80B/13B，20T token，256K ctx） | 2026-09-23 | 无新报告 |

## xAI

| 项目 | 信息 |
|---|---|
| 中文标题 | Grok 4.7 / 4.8 / 5 节奏更新（无新技术报告） |
| 英文标题 | Grok 4.7 / 4.8 / 5 Update (no new tech report) |
| 发布机构 | xAI（SpaceXAI） |
| 模型名称/系列 | Grok 4.7（2026-09-21 发布）、Grok 4.8（2026-09-13 官宣，训练完成中）、Grok 5（训练中） |
| 发布日期 | 2026-09-21（4.7）/ 2026-09-13（4.8 官宣） |
| 核心参数 | Grok 4.6：500K 上下文、$2/$6；Grok 4.8：**2.5T 参数、自研 C++ 训练栈**（Musk X 帖，third-party 转述，tentative）；Grok 4.7 传闻 2.1T（tentative）；Grok 5：**传闻 6T 与 10T 两个 MoE 变体，Colossus 2 训练**，2026-01-06 Series E 时官方披露"训练中"，Q1/Q2 窗口均已滑期（rumor tier） |
| 主要创新点 | 4.8 的卖点是**从零重写的 C++ 软件栈**，训练完成后直接进入 RL；Musk 给出的路线图：4.7≈Opus 5.0、4.8>4.7、4.9≈Astra/Fable、Grok 5 定位首个 AGI 级模型（**均为口头路线图，无评测支撑**） |
| arXiv/论文链接 | 无技术报告/系统卡；见 [xAI Blog](https://x.ai/blog/) 与 Grok Bot Changelog |

> ⚠️ 本期逐项复核：xAI **未发布**任何 Grok 4.7/4.8/5 的技术报告或系统卡；Grok 5 参数与发布窗口全部来自第三方转述，**不计入本 wiki 的 claim 级证据**（仅作节奏信号记录）。

## 其他值得关注

| 机构 | 模型/报告 | 日期 | 要点 | 链接 |
|---|---|---|---|---|
| OpenAI | GPT-6 "Intelligent UI" | 2026-10-01 | 面向 Plus/Pro/Business 用户的界面层更新（产品，非报告） | (single-source) 第三方报道 |
| MiniMax | MiniMax-M3.1-Flash-Preview | 2026-09-27 | Flash 档预览版 | [llm-releases.com](https://www.llm-releases.com/latest) |
| OrcaRouter | OrcaSAQ-2 27B | 2026-09-28 | 27B 开放模型 | 同上 |
| AI2 | Olmo-core 3 | 2026-10-01 | 开放 MoE 训练系统，可扩展至万亿参数规模的开放训练栈 | [allenai.org](https://allenai.org/) |
| Fireworks AI | Ember-1 | 2026-09-24 | 面向高效推理的新模型 | [fireworks.ai](https://fireworks.ai/) |
| Google DeepMind | DiffusionGemma | 2026-07-31 | 离散扩散语言模型，256-token block，基于 Gemma 4 MoE（3.8B/25.2B） | [arXiv:2608.00146](https://arxiv.org/abs/2608.00146) |
| Xiaomi | MiMo-V2.6 Flash/Pro | 2026-09-21 | 轻量/旗舰双档；Pro-UltraSpeed 变体 | 官方模型页 |
| ByteDance | Douyin Multimodal Embedding (DME) | 2026-08-03 | 2B/9B 双档多模态嵌入 | [arXiv:2608.02148](https://arxiv.org/abs/2608.02148) |
| Microsoft | VibeVoice-ASR-Streaming | 2026-09-02 | LLM 端到端流式说话人归属 ASR | [arXiv:2609.02812](https://arxiv.org/abs/2609.02812) |

## 其他关注机构状态

| 机构 | 状态（2026-10-08） | 备注 |
|---|---|---|
| Yi（01.AI） | 较低活跃度 | 近期未见新的 frontier 技术报告/系统卡 |
| Baichuan | 持续更新 | Baichuan-Omni-1.5、Baichuan-M3-235B 等公开；需跟踪新报告 |
| Apple | 技术报告缺席 | 以 AFM / Apple Intelligence 系统与端侧能力为主，未见新 frontier 系统卡 |
| Microsoft (Phi) | 无新 frontier 报告 | 本期以 VibeVoice-ASR-Streaming 等应用/语音模型为主 |
| Amazon (Nova) | 无新报告 | Nova 2 Pro / Nova Premier 持续在线，本期未见新技术报告 |
| StepFun（阶跃星辰） | 持续迭代 | Step 3.7 Flash 在线；Step 5 Preview 属未官宣泄漏级信息，不入 claim（沿用 09-21 期纪律） |
| InternLM（上海 AI 实验室） | 持续迭代 | InternLumina-U2 等全视觉/扩散路线持续推进 |
| ByteDance Seed | 无新报告 | Doubao Seed 2.1 Pro / Seedance 2.5 为当前主力，本期未见新 tech report |

## 补充说明

- **去重原则**：优先收录 2026-09 至 2026-10-08 的新报告/系统卡；旧旗舰（DeepSeek-V4、Qwen3.8-Next、Nemotron 3 Ultra 等）仅作背景保留，条目与 [10-07 期](../2026-10-07/tech-report-digest.md) 一致，未重复展开。
- **口径说明**：OpenAI / Anthropic / Google / xAI 未公开参数量，条目侧重发布时间、上下文/输出、定价与安全评估；Mistral Large 4 的激活参数与定价、Gemini 4 的上下文/输出、Haiku 5.5 的定价均存在来源分歧或未复核，已在对应位置标注。
- **本期核心信号**：① **安全/预备评估成为前沿发布的当日配套**——OpenAI 与 Anthropic 在 2026-10-07 同日各出一份安全文档（GPT-6 10 月系统卡 + Haiku 5.5 系统卡），且都以"可量化的越界/拒绝指标"为核心；② **价格战继续**——GPT-6 Sol/Luna 较 5.6 半价、Gemini 4 介绍期 $2/$10、Haiku 5.5 大幅降价（第三方口径），百万 token 上下文 + 低单价成为标配；③ **开放权重向万亿参数推进**——Mistral Large 4 承诺 10 月底开源 1.05T 权重，与 DeepSeek/Qwen/Kimi 的开源万亿路线正面竞争；④ **中国厂商本期静默**——无新 frontier 报告，节奏集中在 10 月中下旬（第三方预期节点 10-19 前后，(tentative)）。
- **待复核**：Mistral Large 4 技术报告（架构、专家数、训练语料、后训练配方）、Gemini 4 官方 model card、Claude Haiku 5.5 官方定价与索引行、Grok 4.8/5 的参数与发布时间、GPT-6 10 月版的完整评估数值（当前仅摘录生物拒绝与 Preparedness 判定）。
