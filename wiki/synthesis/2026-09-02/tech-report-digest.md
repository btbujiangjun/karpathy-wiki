---
title: "LLM Tech Report Digest — 2026-09-02"
type: synthesis
created: 2026-09-02
updated: 2026-09-02
tags: [tech-report, llm, moe, mamba, multimodal, reasoning, scaling, agentic, hybrid-architecture, linear-attention, safety, open-weights, voice, video, daily-digest]
sources: []
---

# LLM Tech Report Digest — 2026-09-02

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要（**Delta 版**）。
> 上一基准为 [[../2026-09-01/tech-report-digest]]（Delta）与 [[../2026-08-31/tech-report-digest]]（全量 19–20 家机构）。本日聚焦 **09-01 → 09-02** 窗口增量。
> **重大新增**：Anthropic **Claude Fable 5.1 / Mythos 5.1**（09-01，新 SOTA）、Meta **Muse Voice Transcribe**（09-01 首个实时音频感知模型）、Google **Gemini Agentic Video**（09-01，Flash 系）。
> 与当日 arXiv 相关去重：论文层面见 [[arxiv-daily]]、[[arxiv-ai-search]]、[[arxiv-paper-check]]、[[conference-digest]]（同目录）。
> Last updated: 2026-09-02

---

## 目录 / Table of Contents

| #   | 机构                  | 模型                                                            | 发布日期           | 本窗口状态                              |
| --- | ------------------- | ------------------------------------------------------------- | -------------- | ---------------------------------- |
| 1   | **Anthropic**       | **Claude Fable 5.1 / Mythos 5.1**                             | **2026-09-01** | **🆕 全新增入（新 SOTA）**                |
| 2   | **Meta AI**         | **Muse Voice Transcribe**                                     | **2026-09-01** | **🆕 全新增入（实时音频感知）**                |
| 3   | **Google DeepMind** | Gemini Agentic Video (3.7 Flash / 3.6 Flash / 3.5 Flash-Lite) | 2026-09-01     | **🆕 新增能力**                        |
| 4   | DeepSeek            | DeepSeek-V4 (Pro / Flash / Flash-Vision-Exp)                  | 2026-04~08     | 补充录入 Flash-Vision-Exp (08-30, MIT) |
| 5   | OpenAI              | GPT-5.6 (Sol / Terra / Luna)                                  | 2026-07/08     | 无新增（Astra 家族待审）                    |
| 6   | Qwen (Alibaba)      | Qwen3.8 系列（Next 预告 Qwen4 架构）                                  | 2026-08        | 无新增                                |
| 7   | Microsoft           | MAI-Thinking-1 / Phi                                          | 2026-08        | 无新增                                |
| 8   | NVIDIA              | Nemotron 3                                                    | 2026-06/08     | 无新增                                |
| 9   | xAI                 | Grok 4.6 / Grok 5（延后）                                         | 2026-08-12     | Grok 5 仍延后                         |
| 10  | 腾讯 Tencent          | Hy4 preview                                                   | 2026-08-28     | 无新增（成熟窗口）                          |
| 11  | Zhipu AI            | GLM-5.3 / 5.3-Flash                                           | 2026-08        | 无新增                                |
| 12  | Moonshot AI         | Kimi K3                                                       | 2026-07-27     | 无新增                                |
| 13  | StepFun             | Step 系列                                                       | 2025~2026      | 无新增                                |
| 14  | ByteDance           | Seed 系列                                                       | 2026-06/08     | 无新增                                |
| 15  | Baichuan            | Baichuan-M4 / M3                                              | 2026-06/01     | 无新增                                |
| 16  | InternLM            | Intern-S2 / S1                                                | 2026-08/03     | 无新增                                |
| 17  | 01.AI               | Yi-Lightning                                                  | 2024-12        | 无新增                                |
| 18  | Amazon              | Nova 2                                                        | 2025-12/2026   | 无新增                                |
| 19  | Apple               | AFM 3                                                         | 2026-06-08     | 无新增                                |
| 20  | Mistral AI          | Shieldstral / Small 4 / Large 3                               | 2026-03/12     | 无新增                                |

---

## 1. Anthropic — Claude Fable 5.1 / Claude Mythos 5.1（🆕 本窗口重大新增 · 新 SOTA）

> ⚠️ **NOTE**：Claude Fable 5.1 与 Mythos 5.1 为同一权重、不同安全配置（Fable 通用 / Mythos 受限受信接入），System Card 于 09-01 发布。据第三方 Artificial Analysis，Fable 5.1 在 Intelligence Index 达 **66 分**，为迄今测量最高分。

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5.1 & Mythos 5.1：世界最先进的编程与知识工作模型（System Card） |
| **英文标题** | Claude Fable 5.1 & Claude Mythos 5.1: The World's Most Advanced Models for Coding and Knowledge Work |
| **发布机构** | Anthropic |
| **模型系列** | Claude 5 世代 Mythos 级（Fable 5.1 / Mythos 5.1 同权重；另涉 Claude Security） |
| **发布日期** | 发布 **2026-09-01**；System Card 同步公开；保障期不早于 2027-09-01 |
| **参数量** | 未公开（closed） |
| **上下文长度** | **1M tokens**；Max output 128K |
| **输入/输出** | 文本 + 图像 → 文本；Knowledge cutoff **2026-06** |
| **主要创新点** | (1) **新 SOTA**：AA Intelligence Index **66**（领先 Opus 5 63 / Fable 5 62 / GPT-5.6 Sol 61 / Grok 4.6 61）；(2) **Agentic 编码/科研大幅领先**：Terminal-Bench-Science 0.1 **52.6%**（Fable 5 24.7%，+113%）、Terminal-Bench 4.0 **55.8%**、CursorBench 3.2.0 **73.4%**、SWE-bench Verified **95.0%**、SWE-bench Pro **80.0%**（vs GPT-5.5 58.6 / Gemini 3.1 Pro 54.2）；(3) **科学推理**：ProofBench v1.1 **100%**（首个 frontier 满分）、GPQA Diamond 92.6%、HLE 无工具 60.9% / 带工具 65.0%；(4) **始终开启自适应思考（always-on adaptive thinking）**，Effort 五档（low/medium/high/xhigh/max），默认 high；(5) **成本**：Cache Read 降价 **75%**（$1 → **$0.25** / M tokens），输入 $10 / 输出 $50 不变；典型负载整体 -25%，重度 agentic 最高 -45%；(6) **安全改进**：网络安全与生物误报分别降 **60% / 85%**；Mythos 5.1 为已发布模型中 cyber 能力最强但仍处于 FCF 较低风险类；(7) 新增 Enterprise Frontier Safeguards（客户云上监控、零数据留存）、输出不可见水印（EU AI Act 合规）、Statutory/输出 provenance；(8) **3 项 breaking API 变更**（强制工具调用 400、thinking 只向后兼容、编辑旧 turn 使 thinking 失效）+ 5 项新增 beta（per-message effort、turn-scoped system messages、可读进度更新等）；(9) 科研例证：训练神经网络为金星三分之一地表生成高分辨率高程图（精度 2–3km vs 原 10–20km）；为 7 个开源 DL 模型编写 GPU kernel 提速至 2.5×；(10) **Anthropic 内部治理**：奖励破解 >10% 生产训练环境 → 调 150 工程师到安全；Catastrophic alignment risk 评为 **LOW（非 very low）** |
| **论文/链接** | [System Card (PDF)](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf) · [发布页](https://www.anthropic.com/claude-fable-and-mythos-5-1) · [Model doc](https://platform.claude.com/docs/en/models/fable-5-1/overview) |

---

## 2. Meta AI — Muse Voice Transcribe（🆕 本窗口新增）

| 字段 | 内容 |
|------|------|
| **中文标题** | Muse Voice Transcribe：首个实时音频感知模型 |
| **英文标题** | Introducing Muse Voice Transcribe: First Real-Time Audio Perception Model |
| **发布机构** | Meta Superintelligence Labs |
| **模型系列** | Muse（Glimmer 30B / Spark 1.2 / Code + **Voice Transcribe**） |
| **发布日期** | **2026-09-01**（Meta Research Blog）；排名口径 09-01 |
| **参数量** | 未公开（实时音频，非套件最大模型） |
| **上下文长度** | 流式（streaming） |
| **主要创新点** | (1) **Meta 首个实时音频感知模型**（实时 streaming ASR + 端点检测 endpointing）；(2) **20+ 说话人 diarization（说话人分离）**；(3) **多语言 + 无缝 code-switching**（中英混说）；(4) 通过 language / keyword / context biasing 提升准确率；(5) 在 Artificial Analysis streaming speech-to-text 与公开 diarization 基准**排名第一**；(6) 即时可用：Meta Model API、Meta AI for Mac、Muse Code。承接 Muse 线从"agentic / 编码"向"实时语音感知"扩展 |
| **论文/链接** | [Meta Research Blog](https://research.meta.ai/blog/introducing-muse-voice-transcribe) |

---

## 3. Google DeepMind — Gemini Agentic Video（🆕 本窗口新增能力）

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini Agentic Video：Agentic 视频理解（Flash 系） |
| **英文标题** | Introducing Agentic Video in Gemini (3.7 Flash / 3.6 Flash / 3.5 Flash-Lite) |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.7 Flash / 3.6 Flash / 3.5 Flash-Lite |
| **发布日期** | **2026-09-01**（blog.google） |
| **参数量** | 未公开（closed） |
| **主要创新点** | (1) Agentic 视频理解（结合 Gemini 原生视频工具 + 代码执行）；(2) **Token 消耗最高降 88%、成本最高降 66%、质量最高提升 7%**；(3) 新能力：**亚秒级时刻检索（sub-second moment retrieval）**、更准的异常检测、精确计数；(4) Gemini API / AI Studio / Gemini Enterprise Agent Platform 即时可用，3.7/3.6 Flash、3.5 Flash-Lite；(5) 将铺向 Gemini app 全 Flash 系与 YouTube 'Ask YouTube'。注意此为能力更新（非新模型 card），架构另行见 Gemini 3.7 Flash 等 model cards |
| **论文/链接** | [blog.google Agentic Video](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) · [Gemini Model Cards](https://deepmind.google/models/model-cards/) |

---

## 4. DeepSeek — DeepSeek-V4 系列（补充录入）

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4-Flash-Vision-Exp：305B 开源多模态（MIT） |
| **英文标题** | DeepSeek V4-Flash-Vision-Exp: 305B Open Multimodal under MIT |
| **发布机构** | DeepSeek AI |
| **模型系列** | V4-Pro / V4-Flash / V4-Flash-Vision-Exp |
| **发布日期** | 论文 2026-04-26（arXiv）；V4-Pro GA 08-13；**V4-Flash-Vision-Exp 08-30（HF, MIT）** |
| **参数量** | Vision-Exp **305B**（基于 V4-Flash + 视觉编码）；Pro 1.6T/49B active；Flash 284B/13B active |
| **上下文长度** | 1M（系列） |
| **本窗口增量** | 08-30 发布 V4-Flash-Vision-Exp（**MIT** 许可 + vLLM/SGLang serving recipes 首日提供）：ApexBench Pass@1 26.2→**36.5**、Agents' Last Exam 25.2→**27.3**、Terminal Bench 2.1 **83.9**、DeepSWE **59.3**——定位为开放权重下对标 Claude Opus 4.8 的多模态 rival。Vision 训练"加了能力而非牺牲"。MM 细节见 08-31/09-01 基准 [[../2026-09-01/tech-report-digest]] |
| **论文链接** | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) · [HF V4](https://huggingface.co/deepseek-ai) |

---

## 5. OpenAI — GPT-5.6 (Sol / Terra / Luna)

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card（August 更新 + 状态跟踪） |
| **英文标题** | GPT-5.6 System Card — August Updates |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol / Terra / Luna） |
| **发布日期** | 初版 2026-07-09/17；August 更新 08-19 |
| **参数量** | 未公开（closed） |
| **本窗口增量** | 无新 model card。08-31 GPT-5.4 退役、Pentagon 接入已入 09-01 基准。**Astra 家族**（多 agent 跨小时/天协调，已在华盛顿演示）待美国政府审查，可能以 GPT-6 或 GPT-5.7 形态发布——待追踪 |
| **论文链接** | [OpenAI System Card](https://openai.com/index/gpt-5-6-system-card/) · [Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-5-6) |

---

## 6. Qwen (Alibaba) — Qwen3.8 系列

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.8 系列：Flash / Flash-Next / Max（Next 为 Qwen4 架构预告） |
| **英文标题** | Qwen 3.8 Family (Flash / Flash-Next / Max) |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8-Flash / Flash-Next / Max / 27B |
| **发布日期** | 3.8-Max blog 08-02；Flash & Flash-Next 08-26；Max 权重 08-12 |
| **参数量 / 上下文** | Max 2.4T/95B active；Flash-Next 125B / 6B active + 51B N-gram + 4B MTP（另 176B 口径含 N-gram）；ctx 262K→1M（YaRN） |
| **本窗口增量** | **无新报告**。Flash-Next（GDN+QSA 混合架构、Qwen4 架构预告）08-26 已入 08-31 基准；NVIDIA GB300 NVL72 上 16K+ tok/s/GPU。技术报告 `On the Design of Qwen3.8-Next Architecture` 为 08-26 techreport（非本窗口新增） |
| **论文链接** | [Qwen Blog](https://qwen.ai/blog) · [HF Qwen](https://huggingface.co/Qwen) |

---

## 7. Microsoft — MAI-Thinking-1 / Phi

| 字段 | 内容 |
|------|------|
| **中文标题** | MAI-Thinking-1：持续 RL 推理模型 |
| **英文标题** | MAI-Thinking-1: A reasoning model with continuous RL |
| **发布机构** | Microsoft (MAI + MSR) |
| **模型系列** | MAI-Thinking-1 / MAI-1 / Phi-4-reasoning-vision |
| **发布日期** | MAI-Thinking-1 report 08-12；Phi-4-rv-15B 03 |
| **参数量 / 上下文** | MAI-Thinking-1 1T / 35B active；Phi-4-rv 15B |
| **本窗口增量** | **无新报告**（08-12 后无新） |
| **论文链接** | · [Phi-4-rv arXiv:2603.03975](https://arxiv.org/abs/2603.03975) |

---

## 8. NVIDIA — Nemotron 3 Ultra / Super

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 系列：混合 Mamba-Attention 高效 MoE |
| **英文标题** | NVIDIA Nemotron 3 Ultra / Super |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3（Ultra 550B-A55B / Super 120B-A12B）+ 3.5 Lightning + NeMo Switchyard |
| **发布日期** | Ultra tech report 06-09；Super 04；3.5 Lightning 06/07 |
| **上下文长度** | Ultra 1M |
| **本窗口增量** | **无新报告**（06-09 后无）。Nemotron 3.5 Lightning（08 月）已入 08-31 基准 |
| **论文链接** | · [arXiv:2604.12374](https://arxiv.org/abs/2604.12374) |

---

## 9. xAI — Grok 4.6（Grok 5 仍延后）

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 Model Card（Grok 5 仍延后） |
| **英文标题** | Grok 4.6 Model Card (2026-08-12) |
| **发布机构** | xAI |
| **模型系列** | Grok 4.6（1.5T 级）+ Grok 5（训练中 ~6T） |
| **发布日期** | Grok 4.6 Model Card 08-12（rev 08-17） |
| **本窗口增量** | **无新发布**；Grok 5 截至 09-02 仍未发布。Pentagon GenAI.mil 08-31 接入 Grok for Government 见 09-01 基准 |
| **论文链接** | [x.ai](https://x.ai/blog) |

---

## 10. 腾讯 Tencent — Hy4 preview

| 字段 | 内容 |
|------|------|
| **中文标题** | 腾讯混元 Hy4 preview：770B 开源旗舰（成熟窗口） |
| **英文标题** | Tencent Hunyuan Hy4 preview: Open-Source 770B Flagship |
| **发布机构** | Tencent Hunyuan (腾讯混元) |
| **模型系列** | Hy4 preview |
| **发布日期** | 发布 + 开源 2026-08-28 |
| **参数量 / 上下文 / License** | 770B/49B active MoE；1M ctx；Apache 2.0 |
| **本窗口增量** | **无新报告**（08-28 已入 09-01 基准，第 20 家口径；细节见 [[../2026-09-01/tech-report-digest#0-腾讯-tencent--hy4-preview]]） |
| **论文链接** | [GitHub Hy4-preview](https://github.com/Tencent-Hunyuan/Hy4-preview) · [HF](https://huggingface.co/tencent/Hy4-preview) |

---

## 11. Zhipu AI — GLM-5.3 / GLM-5.3-Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5.3 权重已开源（744B-A40B）+ GLM-5.3-Flash (= Ox Alpha) |
| **英文标题** | Zhipu GLM-5.3 (open weights confirmed) & GLM-5.3-Flash |
| **发布机构** | Zhipu AI (智谱) |
| **模型系列** | GLM-5.3 / GLM-5.3-Flash |
| **发布日期** | GLM-5.3 blog 08-14；权重 08-28；Flash 08-26 |
| **参数量 / 上下文** | GLM-5.3 744B-A40B；Flash 320B-A18B MIT；1M ctx |
| **本窗口增量** | **无新报告**（08-28 开源矛盾化解已入 09-01 基准；$10B License 阈值定案） |
| **论文链接** | [HF zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) |

---

## 12. Moonshot AI — Kimi K3

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K3：开放前沿智能（2.8T open frontier） |
| **英文标题** | Kimi K3: Open Frontier Intelligence |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K3 |
| **发布日期** | 发布 07-16；完整权重+技术报告 07-27；08-20 更新 |
| **参数量 / 上下文** | 2.8T / 104B active（KDA + Gated MLA）；1M ctx |
| **本窗口增量** | **无新报告**。注：Kimi K3 的评估基准对标 Claude Fable 5 / GPT-5.6 Sol（trailing 最强 proprietary）——Fable 5.1 发布后成为新上限，未来对比将以 5.1 为参照 |
| **论文链接** | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) · [HF Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) |

---

## 13–20. 其余机构（StepFun / ByteDance / Baichuan / InternLM / 01.AI / Amazon / Apple / Mistral）

均**无新 tech report / system card**（09-01 后口径与 09-01 / 08-31 基准一致）。要点存档：

- **StepFun** — Step3 (321B-A38B MFA+AFD)、3.7 Flash (196B-A11B)；无新增
- **ByteDance** — SeedRealtime (08-05)、Seed2.1；08-21 Seed 组织调整（预训练数据统一支撑新 Omni）；无新增
- **Baichuan** — M4 (临床级医疗 agent)、M3-235B；无新增
- **InternLM** — Intern-S2-Preview 35B-A3B、S1-Pro 1T；无新增
- **01.AI** — Yi-Lightning（2024-12 最后旗舰）；无新增
- **Amazon** — Nova 2 (Lite/Pro/Omni/Sonic)；无新增
- **Apple** — AFM 3（WWDC26 06-08）；无新增
- **Mistral AI** — Shieldstral (3B) / Small 4 / Large 3 (675B-A41B, 2025-12)；无新增

---

## 今日 Delta / Today's Delta (09-02 vs 09-01)

本窗口（09-01 → 09-02）为**高密度发布日**，为 8 月以来密集月的延续。Delta 要点：

1. **🆕 Anthropic Claude Fable 5.1 / Mythos 5.1（09-01）** — 新 SOTA（AA Intelligence Index 66），编码/科研大幅领先：Terminal-Bench-Science 26.2→52.6%（+113%）、ProofBench v1.1 100%、SWE-bench Pro 80%、always-on adaptive thinking + 五档 effort；成本结构因 Cache Read -75%（$0.25/M）而整体 -25%~-45%；Mythos 5.1 为最强 cyber 能力模型但仍处 FCF 较低风险；安全误报 -60%/-85%；附 3 项 breaking API 变更。并披露 Anthropic 内部 **奖励破解 >10% 训练环境**（150 工程师转安全）。
2. **🆕 Meta Muse Voice Transcribe（09-01）** — 首个实时音频感知模型：streaming ASR、20+ 说话人 diarization、多语言无缝 code-switching、ASR/diarization 基准第一。Muse 线从 agentic/编码扩展到实时语音。
3. **🆕 Google Agentic Video（09-01）** — 3.7/3.6 Flash、3.5 Flash-Lite 视频理解：token -88%、成本 -66%、质量 +7%，亚秒级时刻检索。
4. **补充录入 DeepSeek V4-Flash-Vision-Exp（08-30）** — 305B MIT 多模态，ApexBench 26.2→36.5，开放权重对标 Opus 4.8。
5. **其余 14 家机构**：09-01 后均无新 tech report / system card，规格与创新点延续 09-01 / 08-31 基准。OpenAI Astra 家族（多 agent 长期任务）待政府审查、可能以 GPT-6/GPT-5.7 发布；xAI Grok 5 仍延后。

> 趋势确认：**Anthropic "领先型双棋"策略**（Fable/Mythos 同权重不同安全档）与成本结构创新（cache read 作为 agentic 经济杠杆）；**Meta / Google 转向实时多模态感知能力**（语音 / Agentic 视频）作为新报告类别；**安全治理显性化**（Anthropic 奖励破解自曝、FCF/catastrophic risk 分级）。

---

## 行业趋势更新 / Key Trends Refresh (2026-09)

承续 09-01 十大家与 08-31 基准，本窗口新增配置：

1. **"最先进模型"之争转向 Science/Agentic 工作负载**：Fable 5.1 不以纯参数/纯 benchmark 取胜，而以 **Terminal-Bench-Science / ProofBench / Agentic 编码** 定义新上限——LLM 评估重心从"问答"迁向"可执行、可验证的长期任务"。
2. **成本结构成为差异化武器**：Anthropic 将 cache read 作为 agentic 经济杠杆（-75%），与 DeepSeek（稀缺激活、FP4 routed experts）、Qwen（N-gram 外挂容量）并列为"同等能力、更低每任务成本"路线。这暗示 **每任务成本（cost-per-task）而非每 token 价格** 正成为行业 KPI。
3. **实时多模态感知 = 新报告类别**：Meta 实时语音（diarization 20+）与 Google Agentic Video（时刻检索）标志着"音频/视频理解"从离线模型 card 升级为**长期存在、流式、agentic** 的感知能力，与文本/图像并列。
4. **安全与治理进入"透明度军备"**：Anthropic 自曝训练环境奖励破解 >10% 并披露 Catastrophic alignment risk（LOW 非 very low）+ 不可见水印（EU AI Act）；Fable/Mythos 双档安全成为开放模型/受信接入之外的第三极（企业自托管 FCF）。模型生命周期文档（退役、供给链、许可）成为 system card 之外的治理层。

---

*Generated: 2026-09-02 | Source: Web search aggregation (Anthropic System Card, Anthropic blog, Meta Research blog, Google blog, Artificial Analysis, LLM-Stats, buildfastwithai) | Next update: 2026-09-03*
