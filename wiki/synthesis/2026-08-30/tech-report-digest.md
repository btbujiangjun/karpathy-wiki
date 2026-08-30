---
title: "LLM Tech Report Digest — 2026-08-30"
type: synthesis
created: 2026-08-30
updated: 2026-08-30
tags: [tech-report, llm, moe, mamba, multimodal, reasoning, scaling, agentic, hybrid-architecture, linear-attention, safety, open-weights, daily-digest]
sources: []
---

# LLM Tech Report Digest — 2026-08-30

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要。
> 覆盖 19 家目标机构，聚焦 2026 年（尤其 7–8 月）最新发布与更新，附每机构一表格。
> 与当日 arXiv 相关去重：arXiv 论文层面（RLVR/TTPO 等）见 [[conference-digest]]（同目录）。
> Last updated: 2026-08-30

---

## 目录 / Table of Contents

| # | 机构 | 模型 | 发布日期 | 核心架构 |
|---|------|------|----------|----------|
| 1 | DeepSeek | DeepSeek-V4 (Pro/Flash/Vision) | 2026-04~08 | MoE 1.6T/49B + CSA/HCA |
| 2 | OpenAI | GPT-5.6 (Sol/Terra/Luna) | 2026-07/08 | Closed, Router 架构 |
| 3 | Meta AI | Muse Glimmer 30B / Llama 4 | 2026-08 | 多模态 agent 模型 (DFlash) |
| 4 | Google DeepMind | Gemini 3.5 Audio / 3.7 Flash / Omni Flash | 2026-08 | 1M ctx, 多模态 |
| 5 | Anthropic | Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5 | 2026-06/07 | Closed, ASL-3 blocker |
| 6 | Mistral AI | Shieldstral / Small 4 | 2026-03/08 | 3B 安全分类器 / 119B MoE |
| 7 | Qwen (Alibaba) | Qwen3.8-Flash(-Next) / 3.8-Max | 2026-08 | Sparse MoE + Hybrid / Linear Attention |
| 8 | Microsoft | MAI-Thinking-1 / Phi-4-reasoning-vision | 2026-08 | 1T MoE (35B active), hill-climbing RL |
| 9 | NVIDIA | Nemotron 3 Ultra / 3 Super | 2026-06/08 | Hybrid Mamba-Attention MoE |
| 10 | xAI | Grok 4.6 | 2026-08-12 | 1.5T 家族, closed (Grok 5 延后) |
| 11 | Amazon | Nova 2 (Lite/Pro/Omni/Sonic) | 2025-12/2026 | 多模态 1M ctx |
| 12 | Zhipu AI | GLM-5.3 / GLM-5.3-Flash | 2026-08 | 后训练 Scaling + Hybrid Sparse/Linear Attention |
| 13 | Moonshot AI | Kimi K3 | 2026-07-27 | 2.8T/104B MoE, KDA + Gated MLA |
| 14 | StepFun | Step 3.7 / 3.5 Flash | 2025~2026 | MFA + AFD 高效推理 |
| 15 | ByteDance | SeedRealtime / Seed2.1 | 2026-06/08 | 音视频全双工 / agent 生产力 |
| 16 | Baichuan | Baichuan-M4 / M3 | 2026-06/01 | 临床医疗 agent, SPAR++ |
| 17 | InternLM (上海AI Lab) | Intern-S2-Preview | 2026-08-17 | 35B 科学多模态, task scaling |
| 18 | 01.AI | Yi-Lightning | 2024-12 | Enhanced MoE（2026 无新旗舰） |
| 19 | Apple | AFM 3 Core / Core Advanced | 2026-06-08 | Dense + Sparse on-device |

---

## 1. DeepSeek — DeepSeek-V4 (Pro / Flash / Vision)

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4 系列：迈向高效百万 token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek AI |
| **模型系列** | V4-Pro / V4-Flash / V4-Flash-Vision-Exp（及 -Base 基座） |
| **发布日期** | 论文 2026-04-26（arXiv: 2606.19348）；V4-Pro GA 2026-08-13；V4-Flash-Vision-Exp 2026-08-21 |
| **参数量** | V4-Pro: 1.6T / 49B active；V4-Flash: 284B / 13B active |
| **数据量** | 32T+ tokens（两阶段，含领域专家独立培养 + on-policy 蒸馏合并） |
| **上下文长度** | 1M |
| **主要创新点** | (1) Hybrid Attention：Compressed Sparse Attention (CSA, m=4) + Heavily Compressed Attention (HCA, m'=128) 交错配置，1M ctx 下仅需 V3.2 的 27% 推理 FLOPs、10% KV cache；(2) mHC 残差投影约束在 doubly-stochastic 流形；(3) Muon optimizer；(4) Hash-MoE bootstrap + Sqrt(Softplus) 激活亲和力；(5) Lightning Indexer (FP4)；(6) 三档推理 effort；(7) FP4+FP8 混合精度，MIT 开放权重。**新增 (08-21)**: V4-Flash-Vision-Exp 视觉实验版。**融资 (08-26, SCMP)**: pre-IPO 轮估值 ~$74B（报道 ¥500B），拟于 8 月底前完成 |
| **论文链接** | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) · [HF V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) · [API updates](https://api-docs.deepseek.com/updates/) |

---

## 2. OpenAI — GPT-5.6 (Sol / Terra / Luna)

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card（含 2026-08 月度更新） |
| **英文标题** | GPT-5.6 System Card — August Updates |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 低成本 / Luna 最快） |
| **发布日期** | 初版 2026-07-09/17；August 更新 2026-08（08-19 changelog） |
| **参数量** | 未公开 |
| **上下文长度** | 400K input tokens |
| **主要创新点** | (1) Router 架构 + 动态 thinking budget（effort slider）；(2) 全模态（文本+图像+音频+视频）；(3) GPT-Red 自博弈红队（08-03 增补）；(4) Preparedness：Sol/Terra/Luna 均 High (Bio/Chem 与 Cyber)；(5) August 更新：ChatGPT 默认模型升级 Sol/Luna，替换 GPT-5.5 Instant；(6) 08-19 勘误 GPT-5.5 蛋白质结合 pass@4。**新增 (08-18 blog)**: "Pacing model development in an era of cyber-critical capabilities" — 称 Astra 已接近 Critical 网络等级，最大 frontier RL run 暂停 + 2 周全模型 RL-training 缓冲（10% 计算量引入对抗红队），OpenAI 首次因能力阈值主动"减速"开发节奏 |
| **论文链接** | [GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf) · [August Updates](https://deploymentsafety.openai.com/gpt-5-6-august-update/safety) |

---

## 3. Meta AI — Muse Glimmer 30B / Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Muse Glimmer 30B / Llama 4 家族 |
| **英文标题** | Muse Glimmer / Llama 4 |
| **发布机构** | Meta AI |
| **模型系列** | Muse Glimmer 30B（Muse 系列）；Llama 4 Scout / Maverick |
| **发布日期** | Muse Glimmer: 2026-08-10；Llama 4: 2025-04-05 |
| **参数量** | Muse Glimmer: 30B（Apache 2.0，DFlash 投毒解码）；Llama 4 Scout: 109B 总 / 17B active |
| **上下文长度** | Muse Glimmer: 128K；Llama 4 Scout: 10M；Maverick: 1M |
| **主要创新点** | **Muse Glimmer**: 开放权重战略重心，30B 多模态 agent 模型，DFlash 投机解码，Apache 2.0，24-32GB Mac 本地运行（26.6-50.2 tok/s），由 Muse Spark 蒸馏。**Llama 4**: 原生多模态 MoE + early fusion + iRoPE；**注意**：Llama 4 405B/Behemoth 开放权重持续"未兑现"，开源旗舰实际为 Muse 系列（今日无新增） |
| **论文链接** | [Meta AI Blog](https://ai.meta.com/blog/) · [Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |

---

## 4. Google DeepMind — Gemini 3.5 Audio / 3.7 Flash / Omni Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 3.5 Audio / Gemini 3.7 Flash / Omni Flash Model Card |
| **英文标题** | Gemini 3.5 Audio · Gemini 3.7 Flash · Gemini Omni Flash Model Card |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.x Flash；Gemini 3.5 Audio；Gemini Omni Flash |
| **发布日期** | 3.7 Flash: 2026-08-13（GA）；Omni Flash: 2026-05 发布、08-27 更新；**Gemini 3.5 Audio: 2026-08-26（Model Card 上线）** |
| **参数量** | 未公开 |
| **上下文长度** | Gemini 3.x Flash 系列 1M ctx；3.5 Audio: Live Translate 128K / Transcribe 96K |
| **主要创新点** | **Gemini 3.5 Audio (新增, 08-26)**: 基于 Gemini 3 Pro 的语音模型，提供 Live Translate（128K ctx，实时语音翻译）与 Transcribe / Transcribe Live（96K ctx）。**Gemini 3.7 Flash**: "most intelligent workhorse"，agentic coding 聚焦，可配置 thinking，Intro 价格 $0.75/$3.75 per 1M tokens；驱动 Gemini Spark 24/7 agent。**Gemini Omni Flash (08-27 更新)**: 边对边多模态——创建与编辑视频（world understanding + editing）。Gemini 3.1 Pro 仍为旗舰 (1M/64K, 2026-02-19) |
| **论文链接** | [Gemini 3.5 Audio Model Card](https://deepmind.google/models/model-cards/gemini-3-5-audio/) · [3.7 Flash](https://deepmind.google/models/model-cards/gemini-3-7-flash/) · [Omni Flash](https://deepmind.google/models/model-cards/gemini-omni-flash/) |

---

## 5. Anthropic — Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5 System Card |
| **英文标题** | Claude Opus 5 System Card / Claude Fable 5 & Mythos 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Opus 5 / Sonnet 5 / Fable 5 / Mythos 5 |
| **发布日期** | Opus 5: 2026-07-24；Fable 5 & Mythos 5: 2026-06-09；Sonnet 5: 2026-06-30 |
| **参数量** | 未公开 |
| **上下文长度** | 未公开 |
| **主要创新点** | **Opus 5 (07-24)**: Opus 4.8 升级，agentic coding / computer use / long-horizon knowledge work / 数学与科学推理全面提升，约接近 Fable 5 前沿智力而半价（$5/$25 per 1M），不推进 risky dual-use。**Fable 5**: 带 misuse safeguards 的前沿模型。**Mythos 5**: 限受信合作伙伴，集成 ASL-3 blocking classifiers。**Sonnet 5 (06-30)**: 两档（标准/Extended Thinking），**$2/$10 intro 定价 08-10 起改为永久价格**（此前 GLM-3.5-Flash 等中国模型进入德/日市场后 Anthropic 回应性降价，初始为临时促销）。三者构成 Anthropic 2026 闭源前沿双轨 + Opus 主力线 |
| **论文链接** | [Opus 5 System Card](https://www.anthropic.com/research/claude-opus-5) · [System Cards](https://www.anthropic.com/system-cards) |

---

## 6. Mistral AI — Shieldstral / Mistral Small 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Shieldstral / Mistral Small 4 |
| **英文标题** | Shieldstral / Mistral Small 4 |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B）；Mistral Small 4 |
| **发布日期** | Shieldstral: 2026-08-04；Small 4: 2026-03-16 |
| **参数量** | Shieldstral: 3B；Small 4: 119B 总 / 6.5B active（128 experts, 4 active） |
| **上下文长度** | Small 4: 256K |
| **主要创新点** | **Shieldstral (3B)**: 首个 Apache 2.0 多模态安全分类器，"policy-adaptive"——接受用户提供的自定义安全策略文本 + 图像输入做合规判定，而非固定分类头；支持 12 种语言，可单张 16GB GPU 运行；由 OpenAI/Anthropic 对齐方向适配而来，亦是 Open Secure AI Alliance 成员作品。**Small 4**: 统一 Magistral ÷ Pixtral ÷ Devstral 三合一 MoE，可配置 reasoning_effort (none/high)，40% 时延降低 / 3× 吞吐。另：欧洲主权 AI 路线（08-11 in-region inference） |
| **论文链接** | [Shieldstral](https://mistral.ai/news/shieldstral/) · [Small 4](https://mistral.ai/news/mistral-small-4/) · [HF Shieldstral](https://huggingface.co/mistralai/Shieldstral) |

---

## 7. Qwen (Alibaba) — Qwen3.8-Flash(-Next) / Qwen3.8-Max

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Flash / Flash-Next：多模态与 Qwen4 架构预览 |
| **英文标题** | Qwen3.8-Flash · Qwen3.8-Flash-Next (Qwen4 architecture preview) |
| **发布机构** | Alibaba / Qwen Team |
| **模型系列** | Qwen3.8-Flash；Qwen3.8-Flash-Next；Qwen3.8-Max；Qwen3.8-27B |
| **发布日期** | **Flash: 2026-08-26**；**Flash-Next: 2026-08-26（权重开放）**；Qwen3.8-Max: 2026-08-03 |
| **参数量** | Flash: 多模态 125B 级（Reuters 推测，官方未全公开）；Flash-Next: 未公开（open weights）；Max: 总参 2.4T / 95B active |
| **数据量** | Flash 训练成本约为 Qwen3.7-Plus 的 1/9（训练效率大幅提升） |
| **上下文长度** | Flash: 默认 262,144，可扩展至 1M；Max: 1M |
| **主要创新点** | **Qwen3.8-Flash (08-26)**: 原生多模态（文本/图像/音频/视频），可扩展 1M ctx；API 定价 ¥1/¥3 per 1M tokens（输入/输出），训练成本仅 Qwen3.7-Plus 的 1/9——"以小算力实现越级能力"的典型。**Qwen3.8-Flash-Next (新增)**: **开放权重**实验模型，采用 Gated DeltaNet + Gated Attention 混合架构（linear attention + 全注意力），官方明确为 **"Qwen4 架构的 early preview"**，附技术报告《On the Design of Qwen3.8-Next Architecture》——Qwen 首次公开线性注意力换代路线。**Qwen3.8-Max (2.4T/95B)**: 首个开源 Max 级模型，Sparse MoE + Hybrid Attention，OSWorld-Verified 86.1 / PaperBench 93.0，权重 08-12 兑现。Qwen3.5-Omni (ARIA) 为多模态 Omni 线 |
| **论文链接** | [Qwen Blog](https://qwen.ai/blog) · [Qwen3.8 Flash](https://qwen.ai/blog?id=qwen3.8-flash) · [Flash-Next](https://qwen.ai/blog?id=qwen3.8-flash-next) · [GitHub Qwen3.8-max](https://github.com/AlibabaCloud-Official/Qwen3.8-max) |

---

## 8. Microsoft — MAI-Thinking-1 / Phi-4-reasoning-vision

| 字段 | 内容 |
|------|------|
| **中文标题** | MAI-Thinking-1：构建一台攀登者 | Phi-4-reasoning-vision 技术报告 |
| **英文标题** | MAI-Thinking-1: Building a Hill-Climbing Machine (MSR-TR-2026-24) |
| **发布机构** | Microsoft Research / MAI |
| **模型系列** | MAI-Thinking-1；MAI-Thinking-1-Coder；Phi-4 家族；Phi Silica |
| **发布日期** | MAI-Thinking-1 技术报告: 2026-08-12；Phi-4-reasoning-vision: 2026-03 |
| **参数量** | **MAI-Thinking-1: 总参 1T / 激活 35B MoE**（MAI-1 基座派生构型）；Phi-4-rv: 15B |
| **数据量** | 企业级数据 from-scratch 训练（非第三方蒸馏） |
| **主要创新点** | **MAI-Thinking-1 (新增)**: Microsoft "从零训练"的思考型 MoE 旗舰——SWE-Bench Pro 52.8%、AIME 2025 97.0%、LiveCodeBench v6 87.7%；方法论核心是**持续性的自博弈式 RL 爬坡**（"hill-climbing"：不依赖单轮 SFT 校准，而是用持续 RL + 弱监督难例泵持续逼近超优），主打 enterprise-grade 数据源（代码/长文/结构化企业语料）与长时思考（long-form reasoning）。**Phi-4-reasoning-vision-15B**: 融合视觉感知与推理的密度模型。**Phi Silica Platform Card**: Windows NPU 端侧 SLM。**Phi-5**: 仍无官方报告 |
| **论文链接** | [MAI-Thinking-1 Report](https://microsoft.ai/pdf/mai-thinking-1.pdf) · [Phi-4-rv (MSR-TR-2026-10)](https://www.microsoft.com/en-us/research/) |

---

## 9. NVIDIA — Nemotron 3 Ultra / Nemotron 3 Super

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：开源、高效的混合 Mamba-Transformer 推理模型 |
| **英文标题** | Nemotron 3 Ultra: Open, Efficient Hybrid Mamba-Transformer Reasoning Models (technical report, 2026-06-09) |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Ultra / Super / Nano；3.5 Lightning |
| **发布日期** | **3 Ultra 技术报告: 2026-06-09**（boarding）；3 Super: 2026（arXiv: 2604.12374）；3.5 Lightning: 2026-08-11 |
| **参数量** | **Ultra: 总参 550B / 激活 55B**（Hybrid Mamba-Attention MoE，多 experts）；Super: 120B 总 / 12B active（512 experts, top-22）；3.5 Lightning: 30B MoE（~3B active） |
| **数据量** | Ultra: 20T tokens；Super: 25T（两阶段 20T+5T） |
| **上下文长度** | Ultra: 1M；Super: 1M |
| **主要创新点** | **Nemotron 3 Ultra (新增技术报告, 550B/55B)**: 家族旗舰。(1) 周期交错 Mamba-2 块 + Attention 块的 hybrid MoE（常数规模 state，1M ctx 下 KV 开销近常量化）；(2) LatentMoE：latent 维专家提高 accuracy/FLOP 与 accuracy/param；(3) MTP 投机解码（native speculative decoding，6× 推理吞吐提升）；(4) NVFP4 低精度预训练（首个在各层以 NVFP4 位宽开展预训练的旗舰）；(5) MOPD（Multi-Objective Policy Decoding / 多目标策略蒸馏与合并）+ 多环境 RLVR（代码、数学、科学、agentic）。**Nemotron 3 Super (120B/12B)**: 同 hybrid 家族，25T tokens。**3.5 Lightning (30B)**: always-on agents 4× speculative 提速。权重 + 数据开源（Nemotron 许可） |
| **论文链接** | [Nemotron 3 Ultra Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) · [Super arXiv:2604.12374](https://arxiv.org/abs/2604.12374) · [NVIDIA Blog](https://developer.nvidia.com/blog/) |

---

## 10. xAI — Grok 4.6（Grok 5 延后）

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 Model Card / Grok 5 发布窗口多次延后 |
| **英文标题** | Grok 4.6 Model Card |
| **发布机构** | xAI (SpaceXAI) |
| **模型系列** | Grok 4.x；Grok 5（仍在训练） |
| **发布日期** | Grok 4.5: 2026-07-08；Grok 4.6: 2026-08-12（API/Model Card）；Grok 5: 原计划 Q1→Q2→更晚，**截至 2026-08-30 仍未发布** |
| **参数量** | Grok 4.6: 1.5T 家族（报道称 2T 设计），未完全公开；Grok 5: 传闻 6T 与 10T 双变体（Colossus 2，~550K GPUs） |
| **上下文长度** | Grok 4.6: 500K |
| **主要创新点** | (1) long-running agents / interactive and visual work；(2) text+image 输入 / text-only 输出；(3) reasoning 四档 low/medium/high/xhigh；(4) 与 Cursor 联合开发 + Grok Build；(5) 定价 $2/$6 per 1M；(6) 仅 Model Card，无完整技术报告。**Grok 5 (关键状态)**: 原计划 Q1 2026 发布 → Q2 → 此后接连错过 8 月中旬窗口；Grok 4.5 (07-08) 与 4.6 (08-12) 充当过渡；多源报道指喂料 10T 参数 + 550K 卡集群，agentic coding 偏向（含 Cursor 开发者工作流数据）。xAI 的"承诺窗口兑现"持续承压 |
| **论文链接** | [xAI Grok 4.6](https://x.ai/news/grok-4-6) · [API release notes](https://docs.x.ai/developers/release-notes) |

---

## 11. Amazon — Nova 2 (Lite / Pro / Omni / Sonic)

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **英文标题** | Amazon Nova 2: Multimodal reasoning and generation models |
| **发布机构** | Amazon AGI / AWS |
| **模型系列** | Nova 2 Lite / Pro / Omni / Sonic；Nova Multimodal Embeddings |
| **发布日期** | 2025-12-02（Nova 2 家族，AWS Technical Report）；**Sonic refresh: 2026-05-21→05-28 在现有部署内原位更新** |
| **参数量** | 未公开 |
| **上下文长度** | 1M tokens（Lite/Pro/Omni） |
| **主要创新点** | (1) 四变体覆盖企业需求：Lite/Pro = 动态推理（extended thinking，low/medium/high）；Omni = 统一多模态；Sonic = speech-to-speech；(2) 内置 tools（Web Grounding + Code Interpreter）+ remote MCP；(3) Lite 支持 SFT/RFT 定制，Nova Forge 可控预训练自建 frontier；(4) Nova Multimodal Embeddings；(5) **Sonic**: 2026-05 原位刷新（response latencies/dialogue robustness/背景音乐分隔等改进，7 语言、polyglot voices）；(6) Nova 1 原始报告 arXiv:2506.12103 (2025-06) 为基线。(今日无新增) |
| **论文链接** | [Nova 2 Tech Report](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models) · [Nova 1 arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |

---

## 12. Zhipu AI — GLM-5.3 / GLM-5.3-Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5.3：基座权重开源 + GLM-5.3-Flash 多模态 |
| **英文标题** | GLM-5.3 Open-Weight Release · GLM-5.3-Flash: Multimodal at Flash Cost |
| **发布机构** | Zhipu AI (智谱AI / Z.ai/THUDM) |
| **模型系列** | GLM-5.x；GLM-5.3-Flash |
| **发布日期** | GLM-5.3: 2026-08-14 宣布、**08-28 权重正式开源**；GLM-5.3-Flash: 2026-08-26 |
| **参数量** | GLM-5.3: 743B–744B（与 GLM-5.2 相同基座，40B active）；GLM-5.3-Flash: **总 320B / 激活 18B** |
| **数据量** | Flash: 30T-token 多模态预训练语料（首个 GLM-5 原生多模态） |
| **上下文长度** | 两者均 1M |
| **主要创新点** | **GLM-5.3 权重开源 (08-28, 本轮最重新闻)**: HuggingFace `GLM-5.3-Plus` 权重开放，支持 Transformers / vLLM / SGLang 推理栈；配套**自定义 "GLM-5.3 License"**——个人/科研/商业（含 SaaS）均可免费商用，但 **MaaS 服务的云厂商需满足"近 12 个月合并营收 < $10B"才免安全审查**（多篇报道标题写 $100B，阈值口径待核实，见注意）。安全审查针对" emergent cyber capability"（模型具备 real-world exploit 能力）。纯后训练 Scaling：SAO + IndexShare + Slime。**GLM-5.3-Flash (08-26, 新增多模态)**: 首款 GLM-5 系列原生多模态——**Hybrid Sparse + Linear Attention 混合架构**（ULAT + sparsity-level KV）+ mHC；30T 多模态语料；Artificial Analysis Intelligence Index v4.1.1 约 57 分，mini 价位版（API $0.045/任务级别），全面超越 GLM-5.2 系列。GLM-5.3 编码: Terminal-Bench 3.0 28.3 / DeepSWE v1.1 66.9 / GDPval-AA 1,769；CyberGym 84.5% |
| **论文链接** | [GLM-5.3 Blog](https://z.ai/blog/glm-5.3) · [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) · [HF GLM-5.3](https://huggingface.co/zai-org/GLM-5.3-Plus) · [GLM-5 arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |

> ⚠️ **NOTE**: GLM-5.3 许可中 MaaS 安全审查的营收阈值，多数信源写 **$10B（12 个月合并营收）**，亦有头部报道写 **$100B**。此处取多数字源（$10B），标注 uncertain。

---

## 13. Moonshot AI — Kimi K3

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K3：开源前沿智能 |
| **英文标题** | Kimi K3: Open Frontier Intelligence |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K3 |
| **发布日期** | 2026-07-27（arXiv: 2607.24653）；GitHub README 全参数披露 |
| **参数量** | 总参 2.8T / 104B active（MoE）；**93 层 = 69 KDA + 24 Gated MLA + 1 dense**；**896 专家 top-16 激活 + 2 shared** |
| **上下文长度** | 1,048,576（1M） |
| **主要创新点** | (1) Kimi Delta Attention (KDA)：固定大小 recurrent state 替代增长 KV cache + periodic full-attention 层；Gated MLA 承接全注意层；(2) Stable LatentMoE：latent 维专家 + Quantile Balancing（router-score 分位数分配，免手动平衡超参）+ Per-Head Muon；(3) SiTU-GLU 激活；(4) 相比 K2 整体 scaling 效率 ~2.5×；(5) 1M ctx 原生视觉（MoonViT-V2, 401M）；(6) **full weights 开源（首个开源 3T 级）**，MXFP4 orig + MXFP8 激活 QAT；K3 于 GitHub 开源即登顶 stars（~8.6K，首个周末）。post-training 覆盖 general/agentic/coding RL 多 effort 层次 |
| **论文链接** | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) · [GitHub](https://github.com/MoonshotAI/Kimi-K3) |

---

## 14. StepFun — Step 3.7 Flash / Step 3.5 Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Step-3：模型系统协同设计的高效推理 |
| **英文标题** | Step-3: Model-System Co-Design for Cost-Effective Decoding |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step-3（技术报告）；Step 3.7 Flash；Step 3.5 Flash（产品线） |
| **发布日期** | 技术报告 2025-07-31（arXiv: 2507.19427）；**产品线当前并列 Step 3.7 Flash + Step 3.5 Flash** |
| **参数量** | Step3: 总 321B / 38B active；Step 3.7 Flash: 198B |
| **主要创新点** | (1) Multi-Matrix Factorization Attention (MFA)；(2) Attention-FFN Disaggregation (AFD)；(3) 原生多模态；(4) Hopper 上吞吐较 DeepSeek-R1 +70%；(5) model-system co-design。**产品现状**: 平台同时挂出 Step 3.7 Flash（生产/agent 场景高频版）与 Step 3.5 Flash（agent 聚焦）——Step 4 尚未确认。国内 agent 一股（MCP-first） |
| **论文链接** | [arXiv:2507.19427](https://arxiv.org/abs/2507.19427) |

---

## 15. ByteDance — SeedRealtime / Seed2.1

| 字段 | 内容 |
|------|------|
| **中文标题** | SeedRealtime：原生音视频全双工 LLM | Seed2.1：推进 AI 生产力 |
| **英文标题** | SeedRealtime natively Audio-Visual Full-Duplex LLM · Seed2.1 Officially Released |
| **发布机构** | ByteDance (字节跳动) / Volcano Engine / Seed 团队 |
| **模型系列** | SeedRealtime；Seed2.1 Pro / Turbo（Doubao） |
| **发布日期** | **SeedRealtime: 2026-08-05**；Seed2.1: 2026-06-23/24 |
| **参数量** | 未公开 |
| **上下文长度** | Seed2.1: 256K |
| **主要创新点** | **SeedRealtime (新增, 08-05)**: 原生 audio-visual **全双工** LLM——统一单架构同时处理接收-感知-生成（输入视觉/音频，输出语音+口型），低延迟可打断交互，已面向 Doubao 用户灰度（视频通话场景）。定位"统一架构的多模态实时对话"。**Seed2.1 Pro/Turbo (06-23)**: agent 生产力模型（一般 agent + 代码工程），GDPVal 87.9 超 GPT-5.5 (84.9)/Claude Opus 4.7 (82.7)/Gemini 3.1 Pro (67.3)；视频理解多 SOTA（小时级长视频）；闭源 MaaS，CNY ¥6/¥30 (Pro)、¥3/¥15 (Turbo) per 1M |
| **论文链接** | [SeedRealtime Blog](https://seed.bytedance.com/blog/seedrealtime) · [Seed2.1](https://research.doubao.com/en/seed2_1) |

---

## 16. Baichuan — Baichuan-M4 / Baichuan-M3

| 字段 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4：临床级医疗 Agent 系统 |
| **英文标题** | Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care |
| **发布机构** | Baichuan Intelligence (百川智能) / 清华合作 |
| **模型系列** | Baichuan-M4；M3-235B（Apache 2.0） |
| **发布日期** | M4 技术报告: 2026-06-09（arXiv: 2606.08982）；**M4 对外发布新闻: 2026-08-26**；M3-235B: 2026-01-12（arXiv: 2602.06570） |
| **参数量** | M4: 未完全公开；M3: 235B |
| **主要创新点** | **Baichuan-M4 (医疗 agent 系统, 08-26 发布新闻)**: 面向"医生监督的持续照护"而非单轮问答。(1) **Baichuan-Harness** 统一运行时（RL 训练与部署同构，强制动作约束/工具调用/长期患者记忆/多 agent 协调）；(2) **SPAR++** span 级奖励建模 + 质量门控（效率奖励仅当医疗质量达标才生效）；(3) reasoning-path compression（内部思维链压缩至 1/6）；(4) 两阶段 curriculum RL + SAPO/R3 稳定策略优化；(5) 临床工具层：患者记忆（Structured Profile + Unstructured Summaries，渐进披露）、PICO 分解六层循证检索（Citation Precision 90.0 vs GPT-5.5 54.7）、文档 OCR / 胸片 / 皮肤科 VLM 工具；(6) **HealthBench 68.6 世界第一（超越 GPT-5.5 58.4）、hallucination 3.3% 行业最低、long-context clinical memory 86.9（+21.1 vs M3）**。**M3-235B**: 临床问诊建模，W4 量化省 74% 显存 + Gated Eagle3 投机解码 96% 提速，Apache 2.0 |
| **论文链接** | [M4 arXiv:2606.08982](https://arxiv.org/abs/2606.08982) · [M3 arXiv:2602.06570](https://arxiv.org/abs/2602.06570) · [GitHub M3](https://github.com/baichuan-inc/Baichuan-M3-235B) |

---

## 17. InternLM (上海AI Lab) — Intern-S2-Preview

| 字段 | 内容 |
|------|------|
| **中文标题** | Intern-S2-Preview：科学多模态任务缩放 |
| **英文标题** | Intern-S2-Preview: An Efficient 35B Scientific Multimodal Foundation Model |
| **发布机构** | Shanghai AI Lab (上海AI实验室) / InternLM Team |
| **模型系列** | Intern-S2-Preview；Intern-S1 / S1-Pro；Intern-S2-Mobius（架构） |
| **发布日期** | **Intern-S2-Preview: 2026-08-17（HF 开放）**；S1-Pro: 2026-03（arXiv: 2603.25040）；InternLM3-8B: 2025-01 |
| **参数量** | **S2-Preview: 35B**（Qwen3.5 持续预训练续接）；S1-Pro: 1T MoE |
| **主要创新点** | **Intern-S2-Preview (新增)**: 35B 科学多模态基础模型——核心卖点 **"task scaling"**：不靠参数/数据更大，而是把成百专业科学任务的**难度/多样性/覆盖面**从预训练协同扩展到 RL 全链路，从而以 35B 在小分子结构生成、材料晶体结构生成（首个同时具备该能力与通用能力的开源模型）等核心科学任务逼近 1T 级 Intern-S1-Pro，同时保持强通用推理 / 多模态 / agent。**Intern-S2-Mobius (08-17, 架构)**: knowledge/reasoning 分层——共享 FFN 存知识向量 + 独立 self-attention 做组合推理，7B 从零训练用 62.6% 数据达到同规格性能，Qwen3.5-35B 续训 4× 推理加速。**Intern-S1-Pro**: 万亿级科学多模态 |
| **论文链接** | [HF Intern-S2-Preview](https://huggingface.co/internlm/Intern-S2-Preview) · [S1-Pro arXiv:2603.25040](https://arxiv.org/abs/2603.25040) · [GitHub Intern-S1](https://github.com/internlm/Intern-S1) |

---

## 18. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告（2026 无新旗舰） |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI (零一万物) |
| **模型系列** | Yi-Lightning；Yi-Large；Yi-Coder |
| **发布日期** | Yi-Lightning: 2024-12-02（arXiv: 2412.01253）；Yi-Coder: 2024-09 |
| **参数量** | Enhanced MoE，100B 级 |
| **主要创新点** | (1) Enhanced MoE：细粒度专家分割 + 高级路由 + KV-caching；(2) Chatbot Arena 第 6（2024）；(3) RAISE 安全框架。**2026 现状**: 发布节奏显著放慢（相对 DeepSeek/Qwen/Moonshot），重心转向企业产品（TrueNorth 企业 AI 决策平台 / Boss AI / Investor AI / TopSales AI，2026-07 发布）；最新旗舰仍为 Yi-Lightning，开源线 Yi-Coder 仍主打小模型代码。与 Baichuan-M3/M4 医疗线形成对照：开源高频 vs 企业产品化 |
| **论文链接** | [arXiv:2412.01253](https://arxiv.org/abs/2412.01253) · [01.AI](https://01.ai/) |

---

## 19. Apple — AFM 3 (第三代 Foundation Models)

| 字段 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple Foundation Models (AFM3) |
| **英文标题** | Introducing the third generation of Apple Foundation Models |
| **发布机构** | Apple |
| **模型系列** | AFM 3 Core / Core Advanced / Cloud；ADM 3 Cloud / Cloud Pro |
| **发布日期** | 2026-06-08（WWDC26） |
| **参数量** | AFM 3 Core: 3B dense；**AFM 3 Core Advanced: 20B sparse（1–4B active）**；Clouder 未公开 |
| **主要创新点** | (1) 五模型矩阵：端侧 AFM 3 Core (3B) / AFM 3 Core Advanced (20B sparse, IFP Instruction-Following Pruning 实现 1–4B 动态激活) + 云端 AFM 3 Cloud / ADM 3 Cloud（自研 diffuser）/ AFM 3 Cloud Pro；(2) on-device IA 子系统 + Jointly-trained、system Essentially built on stable branch from previous gen；(3) selective attention、interleaved local/global attention（PT-MoE 延续）；(4) 第三方 SLM 评测领先同规模。加入此表作为第 19 项基线——专注端侧 + 隐私，与云端巨头差异化。(今日无新增) |
| **论文链接** | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |

---

## 今日追踪更新 / Today's Delta (vs 2026-08-29)

- **Zhipu GLM-5.3 权重正式开源（08-28）**：自定义 License，MaaS 云厂商加入营收阈值/安全审查条款（$10B 或 $100B 口径待核实）——"因安全延后开源"后兑现。
- **Zhipu GLM-5.3-Flash（08-26，新增）**：首个 GLM-5 系列原生多模态，320B/18B，Hybrid Sparse + Linear Attention + mHC，30T 多模态语料，~57 AA Index @ $0.045/任务。
- **Qwen3.8-Flash（08-26，新增）**：多模态，262K→1M ctx，训练成本仅 Qwen3.7-Plus 的 1/9，API ¥1/¥3。
- **Qwen3.8-Flash-Next（08-26，新增）**：开放权重，Gated DeltaNet + Gated Attention 混合线性注意力，官方定位为 **Qwen4 架构 early preview**。
- **Microsoft MAI-Thinking-1（新增）**：1T/35B MoE，from-scratch 企业级数据，"hill-climbing"持续 RL，SWE-Bench Pro 52.8 / AIME 2025 97.0。
- **NVIDIA Nemotron 3 Ultra（新增，06-09 报告）**：550B/55B hybrid Mamba-Attention MoE，20T tokens，LatentMoE + MTP + NVFP4 + MOPD，6× 吞吐。
- **Google Gemini 3.5 Audio（08-26，新增）**：Live Translate 128K / Transcribe 96K，基于 Gemini 3 Pro。
- **ByteDance SeedRealtime（08-05，新增）**：原声音视频全双工 LLM，Doubao 已部署。
- **Moonshot Kimi K3**：GitHub README 补齐精确规格（93 层 = 69 KDA + 24 Gated MLA + 1 dense；896 专家 → 16 + 2 shared）。
- **DeepSeek**：V4-Flash-Vision-Exp（08-21）+ pre-IPO 估值 ~$74B（08-26 SCMP）。
- **xAI Grok 5**：Q1→Q2→8 月中旬窗口接连错过，仍训练中（6T/10T，~550K GPUs）。
- **Anthropic**：Sonnet 5 $2/$10 定价由临时改为永久（08-10）。
- **OpenAI**：08-18 "Pacing"长文——Astra 接近 Critical 网络阈值，frontier RL run 暂停 + 2 周缓冲期。
- **Baichuan**：M4 发布新闻（08-26，6-09 技术报告）+ M3-235B（Apache 2.0）首次纳入表格。
- **InternLM**：Intern-S2-Preview（08-17）+ S2-Mobius 架构论文首次纳入。
- **Apple**：从"趋势备注"升级为正式条目 #19（AFM 3 全家）。
- **StepFun**：产品线现状确认（Step 3.7 Flash + 3.5 Flash 并列）。

---

## 行业趋势总结 / Key Industry Trends

1. **Linear/混合线性注意力正式商品化**：Qwen3.8-Flash-Next（Gated DeltaNet）+ GLM-5.3-Flash（Sparse + Linear Hybrid）+ Kimi KDA（recurrent fixed-state）+ Nemotron 3 Ultra（Mamba hybrid）——"用常数规模序列状态换 1M 长上下文 + 低 KV"从论文走进旗舰产品；Qwen 首次公开把线性注意力写进新一代架构预览是风向标。

2. **MoE + 稀疏激活仍是绝对主流**：DeepSeek-V4 (1.6T/49B)、Kimi K3 (2.8T/104B)、Qwen3.8-Max (2.4T/95B)、MAI-Thinking-1 (1T/35B)、Nemotron 3 Ultra (550B/55B)、GLM-5.3-Flash (320B/18B)——激活参数占比普遍 1/20~1/30，推理成本与训练算力解耦。

3. **后训练 / 测试时 Scaling 全面接管增量**：GLM-5.3（同 base 纯后训练 SAO）、MAI-Thinking-1（hill-climbing 持续 RL）、OpenAI（effort slider + RL 暂停缓冲）、Nemotron（RLVR→SWE-RL→RLHF→MOPD）——"训多大"让位于"怎么训/训多长"。

4. **多模态 Flash 化：低成本原生多模态成标配**：Qwen3.8-Flash（1/9 训练成本）、GLM-5.3-Flash（30T multimodal 语料）、Gemini 3.5 Audio、SeedRealtime（音视频全双工）、Intern-S2（科学多模态）——多模态 + 低激活参数同时卷。

5. **安全监管进入"文档即产品"阶段**：GLM-5.3 自定义 License 的营收阈值/安全审查条款、OpenAI "Pacing"（前沿 RL 主动暂停）、Anthropic ASL-3 blockers、Mistral Shieldstral 开源分类器——开放权重与能力安全在许可与发布节奏层面正面碰撞；GLM-5.3 开源虽迟到但兑现。

6. **开放权重许可"双轨"分化加剧**：Apache-2.0 大众版（Qwen3.8-27B、Mistral Small 4、Baichuan-M3-235B、Shieldstral）vs 自定义 HPC 旗舰（GLM-5.3 License、Kimi K3、DeepSeek-V4 MIT、Qwen3.8-Max）——兼并"最强能力"与"可控商业化"。

7. **Agentic 能力成官方评测主战场**：MAI-Thinking-1 SWE-Bench Pro 52.8、GLM-5.3 DeepSWE 66.9 + Terminal-Bench 28.3、Qwen3.8-Max OSWorld 86.1/PaperBench 93.0、Grok 4.6 long-running agents——评测重心持续从静态 LLM 基准转向长程 agent 工作负载。

8. **中国轮动加快 / 发布窗口纪律分化**：Kimi K3 权重兑现、GLM-5.3 兑现（迟到但到）、DeepSeek 融资 + Vision exp；xAI Grok 5 连续错过 Q1/Q2/8 中窗口、Meta Llama 4 405B 持续悬置——"承诺-兑现"信用成为竞争维度。

9. **效率 = 系统工程而非单点优化**：1M ctx 下 Nemotron 3 Ultra（MTP 6× 吞吐）+ GLM IndexShare（1M 降 2.9× FLOPs）+ Qwen 训练成本 1/9 + Step-3 MFA/AFD——架构、推理栈、数据、许可四位一体。

10. **Agent 系统/工具层成为新报告载体**：Baichuan-M4（Harness 多 agent 医疗系统）、SeedRealtime（音视频全双工端到端）、Gemini 3.5 Audio（实时翻译/转写）、OpenAI Twin（test-time digital twin）——"模型 + 系统 + 工具链"的整体报告取代单模型卡趋势明显。

---

(End of file)