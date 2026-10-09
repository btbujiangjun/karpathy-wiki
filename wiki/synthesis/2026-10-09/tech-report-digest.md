---
title: "LLM Tech Report Digest — 2026-10-09"
type: synthesis
created: 2026-10-09
updated: 2026-10-09
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, hybrid-attention, scaling-law, long-context, multimodal, reasoning, RL, post-training, kv-cache, pricing, open-weights, daily-digest]
---

# LLM Tech Report Digest — 2026-10-09

> 搜索各大 AI 公司最新大模型技术报告（Tech Report / Technical Report / System Card / Model Card），重点关注大模型新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling Law / 缩放分析、多模态模型、长上下文模型、推理模型 / reasoning model。

> 本次检索基于最新公开技术报告与系统卡，聚焦 DeepSeek、OpenAI、Meta AI、Google DeepMind、Anthropic、Mistral AI、Qwen、Yi、Baichuan、Microsoft、Apple、NVIDIA、xAI、Amazon、Zhipu AI、InternLM、Moonshot AI、StepFun、ByteDance、Tencent、AI2、Xiaomi 等机构。检索窗口侧重 2026-10-03 至 2026-10-09，增量基准为 [2026-10-08 期](../2026-10-08/tech-report-digest.md)。

## 本期要点（相对 2026-10-08 新增/更新）

- **美国前沿实验室静默，开放权重成为唯一主线**：OpenAI / Anthropic / Google / xAI 本期均无新系统卡；10-08→10-09 的增量几乎全部来自**开放权重新模型**——Aleph Alpha **Kolibri-1**（欧洲主权开源、10-03）、Reflection AI **Beam**（501B，10-05）、JetBrains **Mellum2.1**（12B 编码 agent，10-08）、Ant Group **Ling-3.1-flash**（560B，09-29）、NaiveAI **Naive-N0.5-Flash**（309B，09-27）、OrcaRouter **OrcaSAQ-2 27B**（09-28）。
- **⭐ Aleph Alpha Kolibri-1 — 本期唯一带完整技术报告的官方发布**（2026-10-03，APACHE 2.0 权重）：78.1B 总参 / 3.46B 激活的德语+英语 MoE，50 层、384 routed experts / 6 active，**hybrid attention**，FP8 E4M3（128×128 block）为主权重，262K 原生上下文可外推 1M；189 页技术报告 + vLLM 插件。
- **⭐ Reflection AI Beam —「西方开源前沿」的最新宣言**（2026-10-05，权重承诺 10 月内 Apache-2.0）：501B 总参 / 23B 激活（52 层）稀疏 MoE，~23.8T tokens 训练，1M 预训练上下文，text-in/text-out；厂商自报 SWE-bench Verified 80.9、Terminal-Bench v2.1 80.1、HLE 36.2。
- **Mistral Large 4「le Chonk」补充数据核实**（10-06 预览，权重月底）：官方 API 定价被第三方列为 **$1.36 / $4.18**（缓存输入 $0.14）每 1M token；Artificial Analysis Intelligence Index **38**（前代 Large 3 为 9，但落后 Claude Opus 5.5 的 58）；Cybench 93% / CyberGym-E2E 82% / DeepSWE v1.1 61.7% / Coding Agent Index 49.8% / Lakera B3 93.3%，均厂商自报。
- **Google DeepMind model card 列表更新**（2026-10-06）：**Nano Banana 2.1** 与 **EmbeddingGemma 2** 现为列表最新条目，**Gemini 4 / Argon 官方条目仍缺席**（缺口延续至第 3 天）。

---

## Aleph Alpha

| 项目 | 信息 |
|---|---|
| 中文标题 | Kolibri-1：面向德国/英语的主权开放权重模型（技术报告） |
| 英文标题 | Kolibri: A Sovereign European Model on the Pareto Frontier (Kolibri-1) |
| 发布机构 | Aleph Alpha（德国，与芬兰协作训练） |
| 模型名称/系列 | Kolibri-1（FP8 旗舰）+ Kolibri-1-BF16（基座）+ 多个量化变体 |
| 发布日期 | 2026-10-03 |
| 核心参数 | **78.1B 总参（78,103,074,560）/ ~3.46B 激活（3,457,573,120）/ 每 token 4.4%**；50 层、**384 routed experts、6 active**；原生 262,144 token 上下文，可外推至 **1,048,576**；文本入/文本出；FP8 E4M3（128×128 block，FP32 per-block scale）、激活按 1×128 动态量化，embedding/norm/LM head/MoE router 保持 BF16，可选 FP8 KV cache；约 78 GB FP8 权重；最低 1×H200/B200/B300 或 2×80GB A100/H100；需 Aleph Alpha 的 vLLM（0.29）插件 |
| 主要创新点 | **欧洲主权路线：在德国与芬兰构建和训练**，德语/英语双语 Pareto 前沿定位；hybrid attention + 细粒度 MoE；训练时即面向 grounding、tool-calling 与**证据不足时拒答（abstention）**；四档 reasoning effort（none→high）；**Apache 2.0 仅覆盖权重与配置文件**，明确不延伸到代码、架构、参数设置或训练方法 |
| 基准（厂商自报） | 后训练总分 **75.5%（英语）/ 70.8%（德语）**；英语数学 96.5%、代码 89.3%；1M 上下文 **RULER 63.2%**；知识截止 2026-06-18 |
| arXiv/论文链接 | [官方博客](https://www.aleph-alpha.com/) · [189 页技术报告 PDF](https://www.aleph-alpha.com/) · HF `Aleph-Alpha/Kolibri-1` · GitHub `Aleph-Alpha/aleph-alpha-inference` |

> ⚠️ 口径分歧：博客把激活参数量取整为「3B active」，技术报告为 3.46B；博客与 model card 给出的**德语训练占比不同**（已由第三方记录，未裁定）。全部基准为厂商自报，**无独立测试**；model card 明确要求「在任何行动前应有人复核其输出」。
> ⚠️ 许可证说明：**Apache 2.0 仅适用于仓库内的权重与配置文件**，不覆盖底层代码/架构/训练方法——「open-weight」而非 fully open。

## Reflection AI

| 项目 | 信息 |
|---|---|
| 中文标题 | 发布 Beam：501B 开放权重模型 |
| 英文标题 | Introducing Beam: Reflection's 501B open-weight model |
| 发布机构 | Reflection AI |
| 模型名称/系列 | Beam（系列首个模型） |
| 发布日期 | 2026-10-05（公告）；权重/技术报告/model card「本月内」 |
| 核心参数 | **501B 总参 / 23B 激活（52 层）稀疏 MoE**；约 23.8T tokens；**1,048,576（1M）预训练上下文**，API beta 请求上限 262,144；text-in / text-out（非多模态）；权重承诺 Apache-2.0 |
| 主要创新点 | 定位「**西方开放权重前沿**」的第一步，主打**编码 / 推理 / agentic 工作负载**与前沿级推理效率（自称在 reasoning 上比肩 Z.ai GLM-5.2 而推理算力少 3–4×）；将通过 hyperscaler/neocloud 与开源库集成分发；目前仅 early-access waitlist（`platform.reflection.ai`），OpenAI 兼容 API beta（`Beam-501B-A23B` @ api.reflection.ai） |
| 基准（厂商自报） | SWE-bench Verified **80.9**、Terminal-Bench v2.1 **80.1**、SWE-Bench Pro v2-Hard 77.2、DeepSWE v1.1 44.4、Humanity's Last Exam **36.2**；⚠️ 在部分 agentic coding 任务上落后 Kimi K3 与 DeepSeek V4.1 Flash |
| arXiv/论文链接 | [localseobot.ai 转载公告](https://localseobot.ai/blog/introducing-beam-501b-open-weight-model/) · [capitalandcompute 复核](https://capitalandcompute.net/blog/reflection-ai-beam-benchmarks/) |

> ⚠️ **权重尚未发布**：截至 2026-10-08 Reflection 称 Beam「正在最终 red-teaming 与评估」，技术报告/model card/开发者工具承诺「本月内」，**无具体日期、无公开 API、无定价**；Artificial Analysis 08 日仍无 Beam 页面。全部基准为厂商自报、无独立复现。

## JetBrains

| 项目 | 信息 |
|---|---|
| 中文标题 | Mellum2.1：面向编码 agent 的快速开放模型 |
| 英文标题 | Mellum2.1 Gets to Work: A Fast Open Model for Coding Agents |
| 发布机构 | JetBrains |
| 模型名称/系列 | Mellum2.1（前序 Mellum 2，2026-06 开源） |
| 发布日期 | 2026-10-08 |
| 核心参数 | **12B MoE / 2.5B 激活**，Apache 2.0；**架构较 2 代未变，改动全在 pre-training 之后**（post-training / 对齐配方重做） |
| 主要创新点 | 面向 coding agents 的紧凑快速开放模型；「一切变化都发生在 pre-training 之后」——强调后训练配方而非架构扩展；HF 已发布，GGUF（llama.cpp / Ollama / LM Studio）与 **MTP 投机解码头（vLLM）**即将跟进 |
| arXiv/论文链接 | [JetBrains Blog](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) |

## Mistral AI

| 项目 | 信息 |
|---|---|
| 中文标题 | Mistral Large 4（le Chonk）预览 — 数据补充 |
| 英文标题 | Introducing Mistral Large 4（信息更新） |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Mistral Large 4（ML4 / "le Chonk"，v26.10）；9 月 €3B（Series D）后首个模型 |
| 发布日期 | 2026-10-06（API 预览）；权重承诺 10 月底（第三方口径 10-27） |
| 核心参数 | 1T–1.05T 总参 / 49B 激活（官方）· 52B+1.6B 视觉编码器（docs）· 675B/41B（二手）三者并存；原生多模态（文本+图像入）；1M ctx；160+ 语言；~3,800–4,000 块 Grace Blackwell GPU、约 2 个月从零训练；**API 定价 $1.36 / $4.18（缓存输入 $0.14）每 1M token**；API 仅两档 reasoning（none / high） |
| 主要创新点 | 混合 instruct+reasoning 的单一原生多模态 MoE；面向 coding、cyberdefense、制造、金融、电气工程；**另有无护栏「安全版」面向受信开发者/安全公司/政府**（与 Anthropic 同周公布的访问计划同构）；RL 仍在进行，发布前将补训练/安全/评测说明 |
| 基准（厂商自报） | Artificial Analysis Intelligence Index **38**（前代 Large 3 为 9；Claude Opus 5.5 为 58）；Cybench **93%**、CyberGym-E2E **82%**、DeepSWE v1.1 61.7%、Coding Agent Index **49.8%**、Lakera B3 安全 93.3%；Cyber Index 自报全球前五 |
| arXiv/论文链接 | [mistral.ai 公告](https://mistral.ai/news/mistral-large-4/) · [tenbrief 复核](https://tenbrief.com/en/2026/10/08/mistral-large-4-one-trillion-open-weight/) |

> ⚠️ **CONTRADICTION（延续 10-08 期，未裁定）**：激活参数三方口径并存（49B 官方 / 52B+1.6B docs / 675B·41B 二手）；总参 1T 与 1.05T 并存；训练 GPU 数 3,800 与 4,000 并存。**技术报告未发布前不裁定**。
> ⚠️ 许可证未公布：docs 将 Large 4 列入「Open」类别（v26.10）但无条款；Large 3 为 Apache 2.0，自定义许可证将收窄「open」含义。

## Google DeepMind

| 项目 | 信息 |
|---|---|
| 中文标题 | DeepMind Model Cards 列表更新（Nano Banana 2.1 / EmbeddingGemma 2） |
| 英文标题 | DeepMind Model Cards update |
| 发布机构 | Google DeepMind |
| 模型名称/系列 | Nano Banana 2.1（图像）、EmbeddingGemma 2（嵌入）；Gemini 4 / Argon 仍未列入 |
| 发布日期 | 2026-10-06（更新） |
| 核心参数 | 官方 model card 均已上线（具体参数未在本期展开） |
| 主要创新点 | Model Cards 列表最新条目由 **Nano Banana 2.1** 与 **EmbeddingGemma 2** 占据，超越此前最新的 Gemini 3.8 Audio（2026-09-24）；**Gemini 4 / Argon 官方条目仍缺席，缺口延续至第 3 天** |
| arXiv/论文链接 | [DeepMind Model Cards](https://deepmind.google/models/model-cards/) · [Google 官方博客：Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) |

> ⚠️ **model card 缺口（已核实延续）**：截至 2026-10-09，DeepMind Model Cards 列表仍**无 Gemini 4 / Argon 条目**——Gemini 4 自 09-30 官宣、10-02 起分批开放，但参数、基准、安全评估细节仍待官方补录。

## 其他开放权重新模型（Ant Group / NaiveAI / OrcaRouter）

| 机构 | 模型 | 日期 | 架构/要点 | 许可 |
|---|---|---|---|---|
| Ant Group (inclusionAI) | **Ling-3.1-flash** | 2026-09-29/30 | 560B 总参 / ~25B 激活（较 Ling-3.0-flash 的 124B/5.1B 翻四倍）；reasoning（显式 thinking mode），面向 agent/search/办公；256K 上下文，目标 1M，最大 32,768 输出；agentic 分 81.0（5 项）、Terminal-Bench 4 40.4%、SWE-Atlas 55.9%、HealthBench Pro 65.3%；先通过 Vercel AI Gateway 两周免费试用，权重随后开放 | 权重/license「将跟进」（未发布） |
| NaiveAI（北京） | **Naive-N0.5-Flash** | 2026-09-27 | 309B 总参 / ~15.5B 激活 MoE，由 Xiaomi MiMo-V2.5 继续预训练（+3.25T tokens）；**注意力栈无任何 full/global attention**：48 层 = 39 层滑动窗口（128-token）+ 9 层 DeepSeek Sparse Attention（top ~2,048），GQA-4，原生 1M 上下文；「Ultrafast」服务模式 ~2,000 tok/s；邀请制 API $0.10/$0.40 | MIT（HF 权重+推理代码） |
| OrcaRouter (Continuum AI) | **OrcaSAQ-2 27B** | 2026-09-28 | Qwen3.8-27B 的敏感度感知混合精度量化（SAQ）：**平均 3.21 bits**，54GB BF16 → 12.3GB（~4.4×），单 16GB GPU 可服务；去掉视觉塔（纯文本）；保留 262,144 ctx 与 hybrid-attention（48 Gated DeltaNet + 16 full-attn）；WikiText-2 PPL 5.6482 vs BF16 5.6468（+0.02%）、93.2% top-1 一致、0.031 平均 KL；SWE-bench Verified 70.0%、Terminal-Bench 2.1 58.4% | Apache 2.0 |
| Atria ASI | **Atria Dawn Preview** | 2026-09-11 | 744B agentic MoE，**基于 GLM-5.2 构建**，面向长时程研究 agent（文献方法→可执行实验→可复现指标→可审查报告）；256K ctx；checkpoint 与代码先于公告出现在 GitHub/HF，~3 天后才出 140 作者技术报告（**倒置了 paper-first 惯例**） | MIT（开放权重，HF `atria-asi/atria-dawn-preview`） |

> 说明：Ant Group 的 Ling-3.1-flash 与 NaiveAI 的 Naive-N0.5-Flash 属**厂商/第三方自报**；Atria Dawn 的「先发 checkpoint 后发报告」已作为发布惯例的一个变体记录。

## 本期无新报告机构（状态沿用 2026-10-08）

| 机构 | 最新前沿报告/系统卡 | 日期 | 本期状态（2026-10-09） |
|---|---|---|---|
| OpenAI | GPT-6 Sol / Luna October 系统卡 | 2026-10-07 | 无新报告；GPT-6.1 Sol 附录 09-29/10-02 维持 |
| Anthropic | Claude Haiku 5.5 系统卡 | 2026-10-07 | 无新报告 |
| DeepSeek | [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969)（CED + CSA2/FP4 KV，890 bytes/token） | 2026-09-10 | 无新报告 |
| Qwen (Alibaba) | Qwen3.8-Max Prime（09-23）、[Qwen3.8-Next](https://arxiv.org/abs/2608.30320)、[Qwen3.8-Omni](https://arxiv.org/abs/2609.25611) | 2026-09-23 | 无新报告 |
| NVIDIA | [Nemotron 3 Ultra](https://arxiv.org/abs/2606.15007) | 2026-10-04 | 无新 frontier 报告 |
| Meta AI | Muse Spark 1.3 / 1.3 Max；[安全报告 arXiv:2606.12429](https://arxiv.org/abs/2606.12429) | 2026-09-05 | 无新报告（开放权重 Muse Glimmer 30B 维持） |
| Zhipu AI | GLM-5.3 Prime（09-23）、GLM-5.3 / GLM-5.3-Flash | 2026-09-23 | 无新报告 |
| Moonshot AI | [Kimi K3](https://arxiv.org/abs/2607.24653)（2.8T/104B，KDA + Stable LatentMoE） | 2026-07-27 | 无新报告 |
| Tencent | [Hunyuan-A13B](https://arxiv.org/abs/2609.27284)（80B/13B，20T token，256K ctx） | 2026-09-23 | 无新报告 |
| xAI | Grok 4.8（09-13 官宣）/ Grok 5（训练中） | — | 无技术报告/系统卡 |

## 其他关注机构状态

| 机构 | 状态（2026-10-09） | 备注 |
|---|---|---|
| Yi（01.AI） | 较低活跃度 | 经复核近期仍未见新 frontier 技术报告/系统卡（公开最新仍为 Yi-Lightning 系列） |
| Baichuan | 持续更新 | 公开最新仍为 Baichuan-Omni-1.5 / Baichuan-M 系列与 Alignment 报告；本期无新报告 |
| Apple | 技术报告缺席 | 以 AFM / Apple Intelligence 端侧能力为主，未见新 frontier 系统卡 |
| Microsoft | 无新 frontier 报告 | 以应用/语音类模型为主 |
| Amazon (Nova) | 无新报告 | Nova 2 Pro / Nova Premier 持续在线 |
| StepFun（阶跃星辰） | 持续迭代 | Step 5 Preview 官方已宣布（600B/27B，1M ctx），HF BF16 权重标注「可用」但官方口径发布日为 **10-15**（tentative，见补充说明） |
| InternLM（上海 AI 实验室） | 持续迭代 | 全视觉/扩散路线持续推进 |
| ByteDance Seed | 无新报告 | Doubao Seed 2.1 Pro / Seedance 2.5 为当前主力 |

## 补充说明

- **去重原则**：本期聚焦 2026-10-03 → 2026-10-09 的新报告/系统卡与开放权重新模型；旧旗舰（DeepSeek-V4.1-Flash、Qwen3.8、Nemotron 3 Ultra、Kimi K3 等）仅作背景保留，条目不重复展开。
- **口径说明**：Aleph Alpha / Reflection / Ant Group / NaiveAI / OrcaRouter 的基准均为**厂商或第三方自报、无独立复现**；Mistral Large 4 的激活参数、总参、价格与训练规模均存在来源分歧，已在对应位置标注。
- **本期核心信号**：① **美国前沿实验室系统卡连续静默**——10-08 的 OpenAI / Anthropic 双卡之后无新增，信号层重新由开放权重接管；② **开放权重竞争从「参数规模」转向「主权 / 效率 / 许可边界」**——Aleph Alpha（德国主权、Apache 仅覆盖权重）、Reflection（西方开源前沿）、JetBrains（12B 快速编码 agent）、NaiveAI（无 full-attention 的 1M ctx）各自代表不同叙事；③ **量化/压缩发布常态化**——OrcaSAQ-2（3.21 bits、单 16GB GPU）与 Kolibri 的 FP8 主权重说明「部署成本」已成发布一等公民；④ **文档缺口延续**——Gemini 4 / Argon 官方 model card 缺口进入第 3 天，Step 5 Preview 的「权重可用 vs 官方 10-15」口径仍冲突。
- **待复核**：Aleph Alpha 独立评测与可商用许可边界、Reflection Beam 权重实际发布日与技术报告、Mistral Large 4 技术报告（架构/专家数/训练语料/后训练配方）与许可证、Ling-3.1-flash 权重视窗、Step 5 Preview 官方发布日（10-15）与 HF 权重可用性冲突、Gemini 4 官方 model card。
