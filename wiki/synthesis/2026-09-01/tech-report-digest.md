---
title: "LLM Tech Report Digest — 2026-09-01"
type: synthesis
created: 2026-09-01
updated: 2026-09-01
tags: [tech-report, llm, moe, mamba, multimodal, reasoning, scaling, agentic, hybrid-architecture, linear-attention, safety, open-weights, recursive-self-improvement, productivity-agent, daily-digest]
sources: []
---

# LLM Tech Report Digest — 2026-09-01

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要（**Delta 版**）。
> 上一基准为 [[../2026-08-31/tech-report-digest]]（全量 19 家机构表格）。本日聚焦 **08-26 → 09-01 窗口** 的增量，重大新增条目为 **腾讯混元 Hy4 preview**，并**化解 GLM-5.3 权重发布矛盾**。
> 与当日 arXiv 相关去重：arXiv 论文层面见 [[arxiv-daily]]、[[arxiv-ai-search]]、[[arxiv-paper-check]]（同目录）。
> Last updated: 2026-09-01

---

## 目录 / Table of Contents

| # | 机构 | 模型 | 发布日期 | 本窗口状态 |
|---|------|------|----------|-----------|
| 0 | **腾讯 (Tencent)** | **Hy4 preview** | **2026-08-28** | **🆕 全新增入** |
| 1 | DeepSeek | DeepSeek-V4 (Pro/Flash/Vision) | 2026-04~08 | 无新增（08-26 pre-IPO ~$74B） |
| 2 | OpenAI | GPT-5.6 (Sol/Terra/Luna) | 2026-07/08 | GPT-5.4 退役、Pentagon 接入 |
| 3 | Meta AI | Muse Glimmer 30B / Llama 4 | 2026-08 | 无新增 |
| 4 | Google DeepMind | Gemini 3.5 Audio / 3.7 Flash / Omni Flash | 2026-08 | Omni Flash 08-27 更新 |
| 5 | Anthropic | Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5 | 2026-06/07 | 无新增 |
| 6 | Mistral AI | Shieldstral / Small 4 | 2026-03/08 | 无新增 |
| 7 | Qwen (Alibaba) | Qwen3.8-Flash(-Next) / 3.8-Max | 2026-08 | 无新增 |
| 8 | Microsoft | MAI-Thinking-1 / Phi-4-reasoning-vision | 2026-08 | 无新增 |
| 9 | NVIDIA | Nemotron 3 Ultra / 3 Super | 2026-06/08 | 无新增 |
| 10 | xAI | Grok 4.6 | 2026-08-12 | Grok 5 仍延后 |
| 11 | Amazon | Nova 2 | 2025-12/2026 | 无新增 |
| 12 | Zhipu AI | GLM-5.3 / GLM-5.3-Flash | 2026-08 | **矛盾化解：权重确已 08-28 开源 744B-A40B** |
| 13 | Moonshot AI | Kimi K3 | 2026-07-27 | 无新增 |
| 14 | StepFun | Step 3.7 / 3.5 Flash / Step3 | 2025~2026 | 无新增 |
| 15 | ByteDance | SeedRealtime / Seed2.1 | 2026-06/08 | 组织调整 08-21 |
| 16 | Baichuan | Baichuan-M4 / M3 | 2026-06/01 | 无新增 |
| 17 | InternLM | Intern-S2-Preview / S1-Pro | 2026-08, 03 | 无新增 |
| 18 | 01.AI | Yi-Lightning | 2024-12 | 无新增 |
| 19 | Apple | AFM 3 | 2026-06-08 | 无新增 |

---

## 0. 腾讯 Tencent — Hy4 preview（🆕 本窗口重大新增）

> ⚠️ **NOTE**：Tencent 不在原清单 19 家内，但因 08-28 开源 preview 具重大关联（国产开源旗舰 "四强格局" 一员），本日 digest 正式收录（第 20 家口径）。

| 字段 | 内容 |
|------|------|
| **中文标题** | 腾讯混元 Hy4 preview：770B 开源旗舰模型，为生产力而生 |
| **英文标题** | Tencent Hunyuan Hy4 preview: Open-Source 770B Flagship for Productivity |
| **发布机构** | Tencent Hunyuan (腾讯混元) |
| **模型系列** | Hy4 preview（Hy4 正式版待发） |
| **发布日期** | 发布 + 开源 2026-08-28；WorkBuddy/CodeBuddy 两周免费（至 09-10） |
| **参数量** | 770B total / 49B active；MoE 256 routed experts + 1 shared expert，每 token 选 top-8 + shared |
| **数据量** | 未公开 |
| **上下文长度** | 1M tokens |
| **许可证** | Apache License 2.0（商用宽松），权重已上 HF / ModelScope / GitCode / CNB |
| **主要创新点** | (1) **递归自我改进闭环**：Hy4 首次参与自身研发全链路（训练方法/数据策略/评估体系/底层算子四层自动优化，"提方案→跑实验→按结果迭代"），并自主分析推理链路瓶颈做算子融合/通信优化，端到端吞吐较基线提升 **31.8%**；(2) **生产力定位四场景**：软件工程、办公/金融分析、游戏开发、科学研究（AI 研发 / 分子动力学 / 凝聚态物理 / 基础数学）；(3) 内部盲测 **2.99/4.00**（163 专家 / 203 工程任务）略优于 GLM-5.3 (2.92) 与 Kimi K3 (2.94)——差距 <0.1，统计学上基本打平；(4) Arena 代码测试第 5 / 开源模型第 3；(5) Terminal Bench 2.1 85.4、DeepSWE 28.0→64.3；(6) 定价 ¥6 输入 / ¥18 输出 / ¥0.3 缓存命中 per M tokens；(7) Known Limitations：复杂任务推理偏长、有过度验证倾向；(8) 社区 48h 内从 1.5TB 压到 200GB 量化。**注意**：preview 非正式版 |
| **论文/链接** | [GitHub Tencent-Hunyuan/Hy4-preview](https://github.com/Tencent-Hunyuan/Hy4-preview) · [HF tencent/Hy4-preview](https://huggingface.co/tencent/Hy4-preview) · [腾讯官方发布页](https://www.tencent.com/zh-cn/tencent-releases-and-open-sources-tencent-hy4-preview/) |

---

## 1. DeepSeek — DeepSeek-V4 (Pro / Flash / Vision)

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4 系列：迈向高效百万 token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek AI |
| **模型系列** | V4-Pro / V4-Flash / V4-Flash-Vision-Exp（及 -Base） |
| **发布日期** | 论文 2026-04-26（arXiv: 2606.19348）；V4-Pro GA 08-13；V4-Flash-Vision-Exp 08-21 |
| **参数量** | V4-Pro 1.6T / 49B active；V4-Flash 284B / 13B active |
| **数据结构** | 32T+ tokens（两阶段） |
| **上下文长度** | 1M |
| **本窗口增量** | 无新 tech report（08-21 后无新报告）。**08-26 (SCMP)**：pre-IPO 轮估值 ~$74B（报道 ¥500B），拟 8 月底前完成。格式与创新点见 08-31 基准 [[../2026-08-31/tech-report-digest#1-deepseek--deepseek-v4-pro--flash--vision]] |
| **论文链接** | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) · [HF V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |

---

## 2. OpenAI — GPT-5.6 (Sol / Terra / Luna)

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card（含 2026-08 月度更新） |
| **英文标题** | GPT-5.6 System Card — August Updates |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol / Terra / Luna） |
| **发布日期** | 初版 2026-07-09/17；August 更新 08-19 |
| **参数量** | 未公开（closed） |
| **上下文长度** | 未公开 |
| **本窗口增量** | 无新 model card。**08-31**：Codex 中 GPT-5.4 由 GPT-5.6 取代并退役（07-31 起逐步）；**Atlas 浏览器 08-09 关闭**；**08-31 Pentagon 接入 ChatGPT / Grok**（国防场景）。**Seal 模型卡** 待追踪（据称高容量通用模型）。08-18 "Pacing" 博客与 GPT-Red 见 08-31 基准 |
| **论文链接** | [OpenAI System Card](https://openai.com/index/gpt-5-6-system-card/) · [Pacing](https://openai.com/index/pacing/) |

---

## 3. Meta AI — Muse Glimmer 30B / Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Muse Glimmer：本地开源 agentic 模型 |
| **英文标题** | Introducing Muse Glimmer: An Open Agentic Model |
| **发布机构** | Meta Superintelligence Labs |
| **模型系列** | Muse（Glimmer / Spark）+ Llama 4 |
| **发布日期** | Glimmer 2026-08-10（Apache 2.0） |
| **参数量** | Glimmer 30B dense；DFlash drafter ~1.8B；perception encoder ~1.8B |
| **上下文长度** | 128K（+extension） |
| **本窗口增量** | **无新报告**。Muse Spark 1.2 权重"soon"开源承诺未兑现；Llama 4 405B "Behemoth" 仍失约、Llama 5 "Avocado" 推迟。细节见 08-31 基准 |
| **论文链接** | [Meta Research Blog](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) · [HF Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) |

---

## 4. Google DeepMind — Gemini 3.5 Audio / 3.7 Flash / Omni Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 3.5 Audio Model Card 与 3.7 Flash / Omni Flash |
| **英文标题** | Gemini 3.5 Audio Model Card · Gemini 3.7 Flash · Omni Flash |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3（Pro / Flash / Audio / Omni） |
| **发布日期** | 3.5 Audio Model Card 更新 08-26；3.7 Flash GA 08-13；Omni Flash 更新 08-27 |
| **参数量** | 未公开（closed） |
| **上下文长度** | 3.5 Audio Live Translate 128K / Transcribe 96K（基于 Gem 3 Pro） |
| **本窗口增量** | 08-26 3.5 Audio Model Card、08-27 Omni Flash 更新均已入 08-31 基准，本窗口**无再新增**。Gemini 4 pre-training run 已启动 |
| **论文链接** | [Gemini Model Cards](https://deepmind.google/models/model-cards/) · [blog.google](https://blog.google/technology/google-deepmind/) |

---

## 5. Anthropic — Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5 系列 |
| **英文标题** | Claude Opus 5 · Fable 5 · Mythos 5 · Sonnet 5 |
| **发布机构** | Anthropic |
| **模型系列** | Claude 5 世代 |
| **发布日期** | Sonnet 5 06-30；Opus 5 07-24；Fable 5 / Mythos 5 2026；Sonnet 5 永久定价 08-10 |
| **参数量** | 未公开（closed） |
| **上下文长度** | 未公开 |
| **本窗口增量** | **无新报告**（最新为 Opus 5 07-24、Sonnet 5 06-30）。System Card 均见 [[anthropic.md]] 对应实体页。ASL-3 blocker 维持 |
| **论文链接** | [Claude Opus 5 System Card](https://www.anthropic.com/news/opus-5) · [anthropic.com/system-cards](https://www.anthropic.com/system-cards) |

---

## 6. Mistral AI — Shieldstral / Mistral Small 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Shieldstral：开源多模态安全分类器 / Mistral Small 4 |
| **英文标题** | Mistral Shieldstral · Mistral Small 4 |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B 安全分类器）/ Small 4 |
| **发布日期** | Shieldstral 08-04（Apache 2.0）；Small 4 2026-03 |
| **参数量** | Shieldstral 3B；Small 4 ≈119B / 6.5B active |
| **上下文长度** | Small 4: 256K |
| **本窗口增量** | **无新报告**。最新公开最大模型为 Mistral Large 3（2025-12，675B/41B active）。Shieldstral / Magistral 见 08-31 基准 |
| **论文链接** | [HF Shieldstral](https://huggingface.co/mistralai/Shieldstral) · [mistral.ai](https://mistral.ai/news/) |

---

## 7. Qwen (Alibaba) — Qwen3.8-Flash(-Next) / Qwen3.8-Max

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.8 系列：Flash / Flash-Next / Max |
| **英文标题** | Qwen 3.8 Family: Flash, Flash-Next, Max |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8-Flash / Flash-Next / Max |
| **发布日期** | 3.8-Max blog 08-02；Flash & Flash-Next 08-26；Max 权重 08-12 |
| **参数量** | Max 2.4T / 95B active；Flash-Next 125B / 6B active + 51B N-gram + 4B MTP |
| **上下文长度** | Flash 262K→1M；Max 1M |
| **本窗口增量** | **无新报告**（08-26 Flash/Flash-Next 已入 08-31 基准）。Qwen3.8-Max 为 2.4T 参数、多模态、Text Arena 第 5 / Vision Arena 第 2（补充录入） |
| **论文链接** | [Qwen Blog](https://qwen.ai/blog) · [HF Qwen](https://huggingface.co/Qwen) |

---

## 8. Microsoft — MAI-Thinking-1 / Phi-4-reasoning-vision

| 字段 | 内容 |
|------|------|
| **中文标题** | MAI-Thinking-1：持续 RL 推理模型 |
| **英文标题** | MAI-Thinking-1: A reasoning model with continuous RL |
| **发布机构** | Microsoft (MAI + MSR) |
| **模型系列** | MAI-Thinking-1 / MAI-1 / Phi-4-reasoning-vision |
| **发布日期** | MAI-Thinking-1 report 08-12（arXiv）；Phi-4-rv-15B 03 |
| **参数量** | MAI-Thinking-1 1T / 35B active；Phi-4-rv 15B |
| **上下文长度** | 未完全公开 |
| **本窗口增量** | **无新报告**（08-12 后无新）。MAI-Thinking-1 技术细节见 08-31 基准 |
| **论文链接** | [MAI-Thinking-1 arXiv](https://arxiv.org/abs/2608.xxxxx) · [Phi-4-rv arXiv:2603.03975](https://arxiv.org/abs/2603.03975) |

---

## 9. NVIDIA — Nemotron 3 Ultra / Nemotron 3 Super

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：混合 Mamba-Attention 高效 MoE |
| **英文标题** | NVIDIA Nemotron 3 Ultra / Nemotron 3 Super |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3（Ultra / Super）+ 3.5 Lightning + NeMo Switchyard |
| **发布日期** | Ultra tech report 06-09；Super arXiv:2604.12374；3.5 Lightning 06/07 |
| **参数量** | Ultra 550B / 55B active；Super 120B / 12B active |
| **上下文长度** | Ultra 1M |
| **本窗口增量** | **无新报告**（06-09 后无）。Nemotron 3 Ultra（550B-A55B Hybrid Mamba-Transformer MoE + MTP + GenRM-RLHF）技术报告为最新，见 08-31 基准；[PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) |
| **论文链接** | [Nemotron 3 Ultra report](https://research.nvidia.com/) · [arXiv:2604.12374](https://arxiv.org/abs/2604.12374) |

---

## 10. xAI — Grok 4.6（Grok 5 仍延后）

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 Model Card（Grok 5 仍在训练） |
| **英文标题** | Grok 4.6 Model Card (2026-08-12) |
| **发布机构** | xAI |
| **模型系列** | Grok 4.6（1.5T 级）+ Grok 5（训练中） |
| **发布日期** | Grok 4.6 Model Card 08-12（rev 08-17） |
| **参数量** | 1.5T 级家族；未公开 active |
| **本窗口增量** | **无新发布**。Grok 5（约 6T 参数 MoE，Colossus 2 上训练）原计划 2026 Q1，此后一再延后，**截至 09-01 仍未发布**（08-13 后无更新，早期传闻 Q3~）。与 Cursor 合作 / SpaceXAI 见 08-31 基准 |
| **论文链接** | [x.ai](https://x.ai/blog) |

---

## 11. Amazon — Nova 2 (Lite / Pro / Omni / Sonic)

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2 多模态模型家族 |
| **英文标题** | Amazon Nova 2 (Lite / Pro / Omni / Sonic) |
| **发布机构** | Amazon Bedrock / AGI Labs |
| **模型系列** | Nova 2（4 模型） |
| **发布日期** | 2026 初；Sonic refresh 05 |
| **参数量 / 上下文** | 未公开 / 至多 1M |
| **本窗口增量** | **无新报告**（与 07-24、08-31 一致。**Material Nova** 类前端算力产品另计） |
| **论文链接** | [Amazon Nova tech report](https://assets.amazon.science/) · [AWS Nova](https://aws.amazon.com/ai/generative-ai/nova/) |

---

## 12. Zhipu AI — GLM-5.3 / GLM-5.3-Flash（⚡ 矛盾化解）

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5.3 权重开源（矛盾化解：确已兑现）+ GLM-5.3-Flash |
| **英文标题** | Zhipu GLM-5.3 (open weights, CONFIRMED) & GLM-5.3-Flash |
| **发布机构** | Zhipu AI (智谱) |
| **模型系列** | GLM-5.3 / GLM-5.3-Flash (= Ox Alpha) |
| **发布日期** | GLM-5.3 blog 08-14；**权重正式开源 08-28 晚间**；Flash 08-26 |
| **参数量** | **GLM-5.3 官方 744B-A40B**（早前 743B / 753B 为未定稿估数，以官方 744B 为准）；Flash 320B / 18B active |
| **上下文长度** | 1M |
| ⚠️ **矛盾化解** | 上期信源存分歧：explainx.ai 称 GLM-5.3（非 Flash）未兑现 08-28 权重发布。**本窗口多方信源（IT之家 08-29、DataLearner 08-31、智谱官方 HF 卡）一致证实权重确于 08-28 开放下载**（FP8 + BF16 双版，Z.ai 官方 GLM-5 仓库注明 744B-A40B）。→ explainx 说法为过时/错误，予以排除。参数量统一为 **744B-A40B** |
| **License 阈值** | GLM-5.3 License：MaaS 云厂连续 12 个月合计营收 > **$10B USD（100 亿美元）** 才需 Z.AI 安全审查（IT之家 / DataLearner 双源一致）。→ 08-31 digest "$10B vs $100B" 分歧按 **$10B USD** 定案（注意：**$100B 已作废**） |
| **本窗口增量** | GLM-5.3 权重开源确认 + AA 60 分与 Kimi K3 并列开源第一；GLM-5.3-Flash = **Ox Alpha**（320B-A18B，MIT，1M ctx，运行于 10 万中国国产芯片；Unsloth 3-bit GGUF；OrcaRouter 无审查版）。详细方法见 08-31 基准 |
| **论文链接** | [HF zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) · [Zhipu Blog](https://z.ai/blog) · [explainx (过时, 已被推翻)](https://www.explainx.ai/blog/glm-5-3-flash-ox-alpha-official-launch-august-2026) |

---

## 13. Moonshot AI — Kimi K3

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K3：开放前沿智能 |
| **英文标题** | Kimi K3: Open Frontier Intelligence |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K3 |
| **发布日期** | 发布 07-16；完整权重 + 技术报告 07-27（arXiv: 2607.24653）；08-20 更新 |
| **参数量** | 2.8T / 104B active（93 层 = 69 KDA + 24 Gated MLA + 1 dense；896 routed experts top-16 + 2 shared） |
| **上下文长度** | 1,048,576（8K→64K→256K→1M 渐进） |
| **本窗口增量** | **无新报告**（07-27 后无新；08-20 更新已入 08-31 基准）。AAII 60 与 GLM-5.3 并列开放权重第一。KDA + Gated MLA、MXFP4/MXFP8 细节见 08-31 基准 |
| **论文链接** | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) · [HF moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) |

---

## 14. StepFun — Step 3.7 Flash / Step 3.5 Flash / Step3

| 字段 | 内容 |
|------|------|
| **中文标题** | Step 系列高效多模态推理 |
| **英文标题** | StepFun Step Series (Step3, 3.7 Flash, 3.5 Flash) |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step3 / 3.7 Flash / 3.5 Flash |
| **发布日期** | Step3 05；3.7 Flash 05-29；3.5 Flash 开源基座 |
| **参数量** | Step3 321B / 38B active（MFA + AFD）；3.7 Flash 196B / 11B active |
| **本窗口增量** | **无新报告**。MFA + AFD 高效推理、3 档 thinking 见 08-31 基准 |
| **论文链接** | [Step 3.7 Flash Blog](https://static.stepfun.com/) · [Step3-VL-10B arXiv:2601.09668](https://arxiv.org/abs/2601.09668) |

---

## 15. ByteDance — SeedRealtime / Seed2.1

| 字段 | 内容 |
|------|------|
| **中文标题** | SeedRealtime：原生音视频全双工 LLM / Seed2.1 |
| **英文标题** | ByteDance SeedRealtime & Seed 2.1 |
| **发布机构** | ByteDance (Doubao / Seed) |
| **模型系列** | SeedRealtime / Seed2.1 Pro·Turbo |
| **发布日期** | SeedRealtime 08-05；Seed2.1 06/07 |
| **本窗口增量** | **无新模型报告**。**08-21 组织调整**：Seed Foundation Model 设四个一级部门（预训练数据统一由李成刚负责，支撑新 Omni 模型），统一打包新建—该组织变动影响后续报告形态，本质无模型增量 |
| **论文链接** | [Seed Blog](https://seed.bytedance.com/) |

---

## 16. Baichuan — Baichuan-M4 / Baichuan-M3

| 字段 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4：临床级医疗 agent 系统 |
| **英文标题** | Baichuan-M4: A Clinical-Grade Medical Agent System |
| **发布机构** | Baichuan Intelligence + THUBPM, Tsinghua |
| **模型系列** | Baichuan-M4 / M3 |
| **发布日期** | M4 发布新闻 08-26；tech report 06-09（arXiv: 2606.08982）；M3-235B 01 |
| **参数量** | M4 未公开；M3-235B 235B（MoE） |
| **本窗口增量** | **无新报告**（08-26 新闻已入 08-31 基准）。HealthBench 68.6 第一、SPAR++ 三支柱细节见 08-31 基准 |
| **论文链接** | [arXiv:2606.08982](https://arxiv.org/abs/2606.08982) · [GitHub M3](https://github.com/baichuan-inc/Baichuan-M3-235B) |

---

## 17. InternLM (上海AI Lab) — Intern-S2-Preview / Intern-S1-Pro

| 字段 | 内容 |
|------|------|
| **中文标题** | Intern-S2-Preview：35B 科学多模态"任务扩展"模型 |
| **英文标题** | Intern-S2-Preview: 35B Scientific Multimodal Task-Scaling Model |
| **发布机构** | Shanghai AI Laboratory (InternLM) |
| **模型系列** | Intern-S2-Preview / S1-Pro / S1-mini |
| **发布日期** | S2-Preview 08-17（HF）；S1-Pro tech report 03-26（arXiv: 2603.25040） |
| **参数量** | S2-Preview 35B-A3B；S1-Pro 1T |
| **本窗口增量** | **无新报告**（08-17 后无新）。S2-Preview 35B-A3B 从 Qwen3.5 续训、task scaling 细节见 08-31 基准 |
| **论文链接** | [HF Intern-S2-Preview](https://huggingface.co/internlm/Intern-S2-Preview) · [S1-Pro arXiv:2603.25040](https://arxiv.org/abs/2603.25040) |

---

## 18. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning：低成本高效多语言推理 |
| **英文标题** | 01.AI Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型系列** | Yi-Lightning（2026 无新旗舰） |
| **发布日期** | 2024-12（arXiv: 2412.01253v5） |
| **本窗口增量** | **无新报告**；2026 转向企业产品（TrueNorth / Boss / Investor / TopSales AI）+ 主权部署。见 08-31 基准 |
| **论文链接** | [Yi-Lightning arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |

---

## 19. Apple — AFM 3 (第三代 Foundation Models)

| 字段 | 内容 |
|------|------|
| **中文标题** | Apple Foundation Models 第三代（AFM 3） |
| **英文标题** | Apple Foundation Models 3rd Generation (AFM 3) |
| **发布机构** | Apple |
| **模型系列** | AFM 3（Core / Core Advanced / Cloud / ADM Cloud / Cloud Pro） |
| **发布日期** | WWDC26 2026-06-08 |
| **参数量** | Core 3B dense；Core Advanced 20B sparse（1-4B active）；Cloud PT-MoE |
| **本窗口增量** | **无新报告**。IFP (Instruction-Following Pruning)、PCC + Google 合作 Cloud 构建、16 语言支持见 08-31 基准 |
| **论文链接** | [machinelearning.apple.com](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |

---

## 今日 Delta / Today's Delta (09-01 vs 08-31)

本窗口（08-31 → 09-01 早间）**无重大新模型发布**；09-01 的主要故事集中在 **08-26 ~ 08-31** 收尾事件。Delta 要点：

1. **🆕 腾讯混元 Hy4 preview（08-28）正式收录**——770B/49B active、1M ctx、Apache 2.0、递归自我改进闭环（+31.8% 吞吐）、¥6/¥18、内部盲测 2.99/4.00。国产开源旗舰由此形成 **Hy4 / GLM / Kimi / DeepSeek 四强格局**。
2. **⚡ GLM-5.3 权重矛盾化解**——多方信源（IT之家 08-29、DataLearner 08-31、智谱 HF 官方卡）确认权重确于 **08-28** 开源。explainx "未兑现" 说法为过时/错误，**排除**。参数量统一为 **744B-A40B**（743B/753B 为未定稿估数）。License 阈值定为 **$10B USD（100 亿美元）**（原 "$100B" 说法作废）。
3. **GPT-5.4 退役**（08-31）：Codex/API 中由 GPT-5.6 取代；Atlas 浏览器 08-09 关闭；**Pentagon 08-31 接入 ChatGPT / Grok**。
4. **Grok 5 仍延后**：截至 09-01 无发布（最新 Grok 4.6 Model Card 08-12）。原 2026 Q1 目标多次顺延。
5. **其余 14 家机构**：08-31 后均无新 tech report / system card，规格与创新点延续 08-31 基准 [[../2026-08-31/tech-report-digest]]。

> 注：腾讯 Hy4 为新增第 20 家机构口径（原清单 19 家未含）；"四强"/"Openness" 等第三方排序为聚合信源，单源项目标 tentative。

---

## 行业趋势更新 / Key Trends Refresh (2026-08 → 09)

承续 08-31 基准十大趋势，本窗口新增配置：

1. **"模型研发自身"（AI 研发 AI）显性化**：腾讯 Hy4 递归自我改进闭环（自分析推理瓶颈→算子融合→+31.8% 吞吐）与 OpenAI "Pacing"（暂停 frontier RL 缓冲）并置，AI 模型从"被优化"转向"参与优化自身基建"。
2. **国产开源四强格局成形**：Hy4（生产 force Apache 2.0）/ GLM（后训练 Scaling + 自定义 License）/ Kimi K3（3T KDA）/ DeepSeek V4（混合注意力 1M ctx）——差异化定位（生产力/编程安全/通用开放/Agent 推理）取代单纯参数竞赛。
3. **开放权重许可与安全审查双轨进一步分化**：GLM-5.3 以营收阈值 $10B 的 License + 安全审查换得提前开源；Meta 重返 Apache 2.0；Hy4 Apache 2.0 —— "是否能商用" 由单一条款变为分层治理。
4. **模型退役/产品更替节奏加快**：GPT-5.4 退役、Atlas 关闭——说明模型生命周期管理与发布同等重要，成为 system card 之外的新产品层文档。

---

*Generated: 2026-09-01 | Source: Web search aggregation | Next update: 2026-09-02*
