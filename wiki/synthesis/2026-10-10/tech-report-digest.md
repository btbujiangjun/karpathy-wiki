---
title: "LLM Tech Report Digest — 2026-10-10"
type: synthesis
created: 2026-10-10
updated: 2026-10-10
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, hybrid-attention, scaling-law, long-context, multimodal, reasoning, RL, post-training, kv-cache, rsi, agentic, voice, daily-digest]
---

# LLM Tech Report Digest — 2026-10-10

> 搜索各大 AI 公司最新大模型技术报告（Tech Report / Technical Report / System Card / Model Card），重点关注大模型新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling Law / 缩放分析、多模态模型、长上下文模型、推理模型 / reasoning model。

> 本次检索基于最新公开技术报告与系统卡，聚焦 DeepSeek、OpenAI、Meta AI、Google DeepMind、Anthropic、Mistral AI、Qwen、Yi、Baichuan、Microsoft、Apple、NVIDIA、xAI、Amazon、Zhipu AI、InternLM、Moonshot AI、StepFun、ByteDance、Tencent、AI2、Xiaomi 等机构。检索窗口侧重 **2026-10-09 至 2026-10-10**，增量基准为 [2026-10-09 期](../2026-10-09/tech-report-digest.md)。

## 本期要点（相对 2026-10-09 新增/更新）

- **窗口判定：19 家目标机构在 10-09→10-10 仍无新增 frontier 技术报告 / 系统卡，官方"卡面"静默延续。** 本期增量全部来自**信号层与第三方分析**，而非官方文档：一家中国实验室的下一代路线演讲、一篇跨机构长上下文弱点实证、一项被前几期漏掉的语音模型 GA 补录。
- **⭐ 智谱 AI 唐杰演讲暗示下一代 GLM-5.4/5.5（2026-10-08）**——预训练数据/规模扩大到"几个 T"、参数量由 GLM-5.3 的 **7,430 亿**级迈向**至少 1 万亿（1T+）**；强化 RL 后训练（SFT/RLHF/RLVR）；提升长程推理与 Agent 能力。归纳为"两条新路"：**RSI 自主迭代升级** 与 **更长更自主的 Agent**；并明确 GLM-5.4/5.5 预计只有**部分 RSI 成果**，完全自主 RSI 留待 GLM-6。→ 本 wiki 09-30 期记为"GLM-5.4 仅见于 Manifold 预测市场（38%），维持不采信"，本期**升级为创始人公开演讲级信号**（仍未发布）。
- **⭐ ByteDance Seed「Phase Sensitivity」实证（arXiv:2609.36322，09-28 投稿 / 10-09 报道）**——采用**分块 KV cache 压缩**的模型存在系统性 **phase（token 相对压缩窗口边界的位置）敏感**：DeepSeek-V4-Flash-Base 在 128K 检索上**跨位置准确率差达 40.2pp**，后训练与换代逐步收窄（V4-Pro-Base 34.8 → V4-Flash-0731 19.1 → V4-Pro-0813 14.8 → **V4.1-Flash-0910 6.1pp**，仍未消除）；波动周期恰等于该代压缩步长（V4 **4 token**、V4.1 **2 token**）。从零预训练对照（Qwen3-0.6B 架构）证实**分块压缩本身**是来源，full-attention 对照组无此周期；机制侧发现 **phase specialization**（不同 attention head 对不同 phase 贡献不对称）。
- **Amazon Nova 2.5 Sonic 正式可用（2026-10-05，补录）**——面向实时语音 agent 的 speech-to-speech 模型，改进推理 / 指令遵循 / tool-calling 并降时延；**256K 上下文**、7 语言、同会话语音+文本、异步 tool calling；Bedrock 四区域、**定价与 Nova 2 Sonic 相同**；随 Strands Bidi Agents（同期 GA）配套。⚠️ **无独立技术报告/模型卡**（纯 GA 公告）；本系列此前各期未收录，本期**补录**。
- **已覆盖（本期不重复）**：OpenAI GPT-6 Sol/Luna Oct 2026 update 与 GPT-6.1 Sol addendum、Anthropic Claude Haiku 5.5 System Card（均 10-07）→ [10-08 期](../2026-10-08/tech-report-digest.md)；Mistral Large 4、Aleph Alpha Kolibri-1、Reflection AI Beam、JetBrains Mellum2.1 → 10-08 / 10-09 期；vLLM-Omni（arXiv:2610.09307）→ [10-08 arxiv-paper-check](../2026-10-08/arxiv-paper-check.md)。
- **⚠️ 旧闻排除**：Mistral docs changelog 出现的 "10-09 Ministral 3B/8B" 经核实为 **2024 年条目**（model id `ministral-3b-2410` / `ministral-8b-2410`），**非新发布**，不予收录。

---

## 智谱 AI (Zhipu)

| 项目 | 信息 |
|---|---|
| 中文标题 | 唐杰演讲暗示新一代 GLM-5.4/5.5：参数量迈入万亿、走两条新路 |
| 英文标题 | （无官方英文标题；媒体转述） |
| 发布机构 | 智谱 AI (Zhipu) |
| 模型名称/系列 | GLM-5.4 / GLM-5.5（**信号级，未发布**） |
| 发布日期 | 2026-10-08（唐杰新加坡演讲，快科技 / 量子位等转述） |
| 核心参数 | 预训练数据与规模扩大目标"几个 T"；参数量预期由 GLM-5.3 的 **7,430 亿**级提升到**至少 1 万亿（1T+）**（媒体按此前口径推算，官方未给数）；架构细节未披露 |
| 主要创新点 | 唐杰列出三个方向：① 扩大预训练数据与规模以抬升智能上限；② 强化 RL 后训练（SFT / RLHF / RLVR，"后训练仙人"）；③ 提升长程推理与 Agent 能力（更复杂环境、更难任务、更长周期）。归结为"**两条还没有走过的新路**"：**RSI 自主迭代升级** 与 **更长更自主的 Agent**。8 月底财报会议曾把下一代定义为 **fully self-training**（美国同行称 RSI，即递归自我改进）；本次口径明确 **GLM-5.4/5.5 预计只有部分 RSI 成果**，完全自主的 RSI 进化仍待 GLM-6 |
| 基准 | 无 |
| arXiv/论文链接 | [快科技 2026-10-08](https://news.mydrivers.com/1/1155/1155996.htm) · [xix.ai 转述](https://xix.ai/zh/live/7753) · [dtm.com.cn 转述](https://dtm.com.cn/news/202610/307945.html) |

> ⚠️ **信号级、非发布**：无官方博客 / 模型卡 / 权重 / API / 发布日期。本 wiki [2026-09-30 期](../2026-09-30/tech-report-digest.md)曾判定"GLM-5.4 仅出现在 Manifold 预测市场（38% 概率），非发布，维持不采信"；本期**升级为创始人公开演讲级信号**，但仍不作发布处理。
> ⚠️ 演讲内容为媒体二手转述，未取一手全文；1T+ 参数量为记者据"几个 T + 上一代 7,430 亿"推演，**非官方确认**。

## ByteDance Seed

| 项目 | 信息 |
|---|---|
| 中文标题 | 周期性弱区：分块 KV Cache 压缩导致的 Phase Sensitivity |
| 英文标题 | Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression |
| 发布机构 | arXiv 元数据**不列 affiliation**；36kr / 量子位报道署 **ByteDance Seed** 团队（二手署名，待一手确认） |
| 模型名称/系列 | 分析对象 = **DeepSeek-V4 系列**（V4-Flash-Base / V4-Pro-Base / V4-Flash-0731 / V4-Pro-0813 / V4.1-Flash-0910）；自研对照 = 基于 **Qwen3-0.6B** 架构从零预训练的一族 transformer |
| 发布日期 | arXiv **2026-09-28** 投稿（v1）；中文解读 **2026-10-09** |
| 核心参数 | 65 页 / 20 图；cs.LG (+ cs.AI)；作者 Xingyu Zhu, Pu (Luke) Yi, Ziheng Cheng, Ang Lv, Jing Liu, Lexing Ying, Yiyuan Ma, Xin Dong |
| 主要创新点 | 提出 **phase sensitivity**：使用分块 KV cache 压缩（fixed stride）的模型，同一信息在不同 **phase**（token 相对压缩窗口边界的位置）检索难度系统性不同，检索准确率随位置**周期波动**，均值高分会掩盖**周期性弱区**。① DeepSeek-V4-Flash-Base 在 128K Needle-in-a-Haystack 上跨位置准确率差达 **40.2pp**，V4-Pro-Base **34.8pp**；后训练后收窄：V4-Flash-0731 **19.1pp**、V4-Pro-0813 **14.8pp**、**V4.1-Flash-0910 6.1pp**（仍存在）。② 波动周期恰等于该代 KV 压缩步长：V4 **4 token**、V4.1 **2 token**。③ 代码补全实证：对 DeepSeek-V4 官方推理代码中的 FP8 量化函数补全（正确应为 8），仅增删前置 docstring 的若干无关 "=" 字符即可翻转答案；某些 phase 下错答 32 的均值概率 **71.3%**（对答 26.4%），另一些 phase 反转（对答 **91.5%** / 错答 7.2%）。④ 从零预训练实验：所有分块压缩变体均出现与压缩步长对应的周期性（步长 4→周期≈4、6→6、8→8），**full-attention 对照组不出现**；去掉 RoPE 或以简单平均替代可学习压缩权重，现象仍在 → 归因于分块压缩机制本身。⑤ 因果干预发现 **phase specialization**：不同 attention head 对不同 source phase 贡献不对称；理想化检索模型显示 gradient flow 可能偏好尖锐的 phase 专门化，故周期性非随机噪声 |
| 基准（跨 phase 差值） | 见上：40.2 / 34.8 / 19.1 / 14.8 / 6.1 pp（各代模型最高-最低位置准确率差） |
| arXiv/论文链接 | [arXiv:2609.36322](https://arxiv.org/abs/2609.36322) · [36kr / 量子位解读](https://eu.36kr.com/en/p/4018280573833089) |

> ⚠️ **口径注**：arXiv 摘要以 "large open-weight models" 泛指，**未点名 DeepSeek**；逐模型数字（40.2/34.8/19.1/14.8/6.1pp）与"DeepSeek 用自家代码"等细节来自量子位 / 36kr 解读稿，非摘要原文。机构署名亦同（arXiv 元数据不含 affiliation）。
> 🔗 **关联**：本结论直接对应本 wiki 已收录的 **DeepSeek-V4.1-Flash 技术报告**（arXiv:2609.19969；CSA2 + FP4 KV caching + SWA Bounded Replay 等分块/压缩机制，见 [10-07 期](../2026-10-07/tech-report-digest.md)）；本期为这条"用压缩换长上下文成本"的路线补充了一个**第三方弱点实证 + 评测方法学建议**（应按 phase 分层报告，而非只报均值）。

## Amazon

| 项目 | 信息 |
|---|---|
| 中文标题 | Amazon Nova 2.5 Sonic 正式可用：面向语音 agent 的改进推理 |
| 英文标题 | Announcing Amazon Nova 2.5 Sonic with improved reasoning for voice agents |
| 发布机构 | Amazon Web Services (AWS) |
| 模型名称/系列 | Nova 2.5 Sonic（模型 id 二手口径 `nova-2-5-sonic`，官方公告未给 slug） |
| 发布日期 | 2026-10-05（GA，Amazon Bedrock） |
| 核心参数 | speech-to-speech 实时语音模型；**256K 上下文窗口**；7 种语言、表达性语音、可控 turn-taking；同一会话内**语音与文本混用**、**异步 tool calling**；可用 **Strands Bidi Agents**（同期 GA）构建生产语音 agent；上线区域 us-east-1 / us-west-2 / eu-north-1 / ap-northeast-1；**定价与 Nova 2 Sonic 相同** |
| 主要创新点 | 相对 Nova 2 Sonic 提升**推理、指令遵循、tool-calling 准确率**并降低时延；面向客服、互动学习、语音助手等实时语音场景 |
| 基准 | 未披露数值 |
| 来源链接 | [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-sonic/) · [Amazon Nova models](https://aws.amazon.com/nova/models/) |

> ⚠️ **无独立技术报告 / 模型卡**（仅 GA 公告 + 用户指南博客，产品级）。
> ⚠️ **上下文口径分歧**：Nova 2.5 Sonic 公告明确 **256K**；而 Nova 模型概览页对 **Nova 2 Sonic**（上一代）标注 "expanded context window of up to **1M** tokens"。两代产品的官方页面口径不一致，**暂记录不裁定**（第三方对 2.5 Sonic 亦标 262K，与公告 256K 基本吻合）。

---

## 19 家目标机构窗口内复核

| 机构 | 窗口内新 frontier 报告 / 系统卡 | 备注 |
|---|---|---|
| OpenAI | 无 | GPT-6 Sol/Luna Oct 2026 update、GPT-6.1 Sol addendum（10-07）已录于 [10-08 期](../2026-10-08/tech-report-digest.md) |
| Anthropic | 无 | Claude Haiku 5.5 System Card（10-07）已录于 10-08 期 |
| Google DeepMind | 无 | model card 列表仍**无 Gemini 4 / Argon 条目**；最新条目 Nano Banana 2.1 / EmbeddingGemma 2（缺口延续） |
| Meta AI | 无 | |
| Microsoft | 无 | |
| NVIDIA | 无 | |
| xAI | 无 | Grok 4.7（09-21）为最新；Grok 4.8（2.5T、自研 C++ 栈）仍在 RL、**无官方日期/卡**；第三方预测 ~10-20 为 forecast，不作采信 |
| Mistral AI | 无（旧条目） | docs "10-09 Ministral 3B/8B" = 2024 年 `ministral-*‑2410` 条目，**非新报告** |
| DeepSeek | 无 | V4.1-Flash（09-10）仍为最新；**V4.1-Pro 截至 10-04 第三方核查仍未发布**，`deepseek-v4-pro`(0813) 继续提供 |
| Qwen / Alibaba | 无 | |
| Moonshot AI | 无 | |
| Zhipu AI | 无报告（有信号） | GLM-5.4/5.5 演讲信号，见上 |
| ByteDance | 无报告（有分析论文） | Seed phase-sensitivity，见上 |
| Amazon | 无技术报告（有 GA） | Nova 2.5 Sonic，见上 |
| Apple | 无 | AFM 3（06-08）为最新，窗口内无新报告 |
| InternLM | 无 | |
| StepFun | 无 | |
| Baichuan | 无 | |
| 01.AI (Yi) | 无 | |

> 10-08 / 10-09 期新增机构（Tencent / AI2 / Xiaomi）窗口内亦无新报告。

## 本期不重复收录（已在往期）

- **vLLM-Omni 技术报告**（arXiv:2610.09307，10-07，vLLM 团队）已录于 [10-08 arxiv-paper-check](../2026-10-08/arxiv-paper-check.md) 与 `wiki/index.md`。
- **OpenAI** GPT-6 Sol/Luna October 2026 update（10-07）、GPT-6.1 Sol addendum（09-29/10-02）→ 10-08 期。
- **Anthropic** Claude Haiku 5.5 System Card（10-07）→ 10-08 期。
- **Mistral Large 4「le Chonk」**（10-06 预览，权重承诺 10 月底）→ 10-08 / 10-09 期。
- **Aleph Alpha Kolibri-1**（10-03，完整技术报告）、**Reflection AI Beam**（10-05）、**JetBrains Mellum2.1**（10-08）→ [10-09 期](../2026-10-09/tech-report-digest.md)。

---

*Generated 2026-10-10. 口径声明：本期新收录三项均非"带完整技术报告的官方发布"——① 智谱 GLM-5.4/5.5 为创始人演讲信号（媒体转述）；② ByteDance Seed phase-sensitivity 为 arXiv 分析论文（arXiv 元数据不含 affiliation，机构/逐模型数字来自二手解读）；③ Amazon Nova 2.5 Sonic 为产品级 GA（无独立技术报告/模型卡）。官方系统卡/tech report 口径上，19 家机构连续静默。Dedup：写入前以 `rg` 对全库校验，`2609.36322` / `Phase Sensitivity` / `Nova 2.5` / `GLM-5.4` / `GLM-5.5` 在 `wiki/synthesis/2026-10-09/`、`wiki/synthesis/2026-10-10/` 均 0 命中（vLLM-Omni `2610.09307` 除外，已存在，作交叉引用）。*
