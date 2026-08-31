---
title: "LLM Tech Report Digest — 2026-08-31"
type: synthesis
created: 2026-08-31
updated: 2026-08-31
tags: [tech-report, llm, moe, mamba, multimodal, reasoning, scaling, agentic, hybrid-architecture, linear-attention, safety, open-weights, medical-ai, scientific-ai, daily-digest]
sources: []
---

# LLM Tech Report Digest — 2026-08-31

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要。
> 覆盖 19 家目标机构，聚焦 2026 年（尤其 7–8 月）最新发布与更新，附每机构一表格。
> 与当日 arXiv 相关去重：arXiv 论文层面见 [[arxiv-daily]]、[[arxiv-ai-search]]、[[arxiv-paper-check]]（同目录）。
> Last updated: 2026-08-31

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
| 17 | InternLM (上海AI Lab) | Intern-S2-Preview / S1-Pro | 2026-08, 03 | 科学多模态, task scaling |
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
| **论文链接** | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) · [HF V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |

---

## 2. OpenAI — GPT-5.6 (Sol / Terra / Luna)

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card（含 2026-08 月度更新） |
| **英文标题** | GPT-5.6 System Card — August Updates |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 低成本 / Luna 最快） |
| **发布日期** | 初版 2026-07-09/17；August 更新 2026-08（08-19 changelog） |
| **参数量** | 未公开（closed） |
| **数据量** | 未公开 |
| **上下文长度** | 未公开 |
| **主要创新点** | (1) Sol/Terra/Luna 三档 + 自动 Router 选择 effort；(2) GPT-Red 自博弈红队（从"红队跑模型"转向"模型跑红队"）训练出的对抗样本提升安全评估；(3) 08-19 勘误更新 GPT-Red 数据；(4) Sol 为 Microsoft 365 Copilot 首选模型（07-09）；(5) **08-18 "Pacing" 博客**：首次主动减缓前沿模型开发——Astra 网络接近 Critical 阈值、最大规模 frontier RL run 暂停进入 2 周全模型 RL 缓冲期；(6) Sol API 降价 20%（07）以应对价格竞争 |
| **论文链接** | [OpenAI System Card](https://openai.com/index/gpt-5-6-system-card/) · [Pacing](https://openai.com/index/pacing/) |

---

## 3. Meta AI — Muse Glimmer 30B / Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Muse Glimmer：可在本地设备运行的开源 agentic 模型 |
| **英文标题** | Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device |
| **发布机构** | Meta Superintelligence Labs |
| **模型系列** | Muse（Glimmer 开放 / Spark 闭源）+ Llama 4 |
| **发布日期** | Muse Glimmer 2026-08-10（Apache 2.0）；Llama 4 Maverick 2025（始终开放旗舰） |
| **参数量** | Glimmer 30B dense（从闭源 Muse Spark 蒸馏）；DFlash drafter ~1.8B；perception encoder ~1.8B |
| **数据量** | 未公开（蒸馏自 Muse Spark） |
| **上下文长度** | 128K（+extension） |
| **主要创新点** | (1) Meta **近 16 个月来首个开源权重模型**（Llama 4 之后），亦是首个 Apache 2.0 许可的 Meta 模型；(2) 专为本地/tool-use loop 设计：顺序工具调用 + 多模态推理与理解，无需 API key/每 token 成本；(3) DFlash 投机解码加速（22→26.6/50.2 tok/s）；(4) 4-bit 下 <20GB，可在 24/32GB 消费级 GPU 运行；(5) 26.6 tok/s on M5 Max；(6) Artificial Analysis：Intelligence Index 35（+21 分 vs Llama 4 Maverick 的 14），Openness Index 44。**注意**：Zuckerberg/Alexandr Wang 承诺"soon"开源 Muse Spark 1.2 权重（未给日期）；Llama 4 405B "Behemoth" 至今仍失约，无新增报告 |
| **论文链接** | [Meta Research Blog](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) · [HF Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) |

---

## 4. Google DeepMind — Gemini 3.5 Audio / 3.7 Flash / Omni Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 3.5 Audio Model Card 与 Gemini 3.7 Flash / Omni Flash |
| **英文标题** | Gemini 3.5 Audio Model Card · Gemini 3.7 Flash · Gemini Omni Flash |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3（Pro / Flash / Audio / Omni） |
| **发布日期** | Gemini 3.5 Audio Model Card 更新 2026-08-26；3.7 Flash GA 2026-08-13；Omni Flash 更新 2026-08-27 |
| **参数量** | 未公开（closed） |
| **数据量** | 未公开 |
| **上下文长度** | 3.5 Audio: Live Translate 128K / Transcribe 96K（基于 Gemini 3 Pro）；3.7 Flash 与 Omni Flash 高 ctx |
| **主要创新点** | (1) **Gemini 3.5 Audio（08-26 新增）**：Live Translate 实时翻译（128K）与 Transcribe 转录（96K）模型卡，基于 Gemini 3 Pro 的音频特化；(2) **3.7 Flash（08-13 GA）**：高吞吐 Flash 级多模态，$0.75/$3.75 intro 定价；(3) **Omni Flash（08-27 更新）**：视频创建/编辑能力增强；(4) Gemini 4 最雄心 pre-training run 已启动；3.5 Pro 与合作伙伴测试中 |
| **论文链接** | [Gemini 3.5 Audio Model Card](https://ai.google.dev/gemini-api/docs/models) · [blog.google](https://blog.google/technology/google-deepmind/) |

---

## 5. Anthropic — Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5 系列 |
| **英文标题** | Claude Opus 5 · Claude Fable 5 · Claude Mythos 5 · Claude Sonnet 5 |
| **发布机构** | Anthropic |
| **模型系列** | Claude 5 世代（Sonnet 5 / Opus 5 / Fable 5 / Mythos 5） |
| **发布日期** | Sonnet 5 2026-06-30；Opus 5 2026-07-24；Fable 5 / Mythos 5 2026；Sonnet 5 定价转永久 2026-08-10 |
| **参数量** | 未公开（closed） |
| **数据量** | 未公开 |
| **上下文长度** | 未公开 |
| **主要创新点** | (1) **Opus 5（07-24）**：发布时接近 Fable 5 性能、约半价，System Card 随附；(2) **Fable 5 / Mythos 5**：Artificial Analysis Intelligence Index 榜首梯队，均维持 ASL-3 安全等级；(3) **Sonnet 5（08-10）**：$2/$10 per M tokens 由临时定价转为永久定价；(4) 与 OpenAI "Pacing" 形成对照——两家都在安全护栏与发布节奏上显性化；(5) Model 2（旧架构）已封存 |
| **论文链接** | [Claude Opus 5 System Card](https://www.anthropic.com/news/opus-5) · [anthropic.com](https://www.anthropic.com/) |

---

## 6. Mistral AI — Shieldstral / Mistral Small 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Shieldstral：开源多模态安全分类器 / Mistral Small 4 |
| **英文标题** | Mistral Shieldstral · Mistral Small 4 |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B 安全分类器） / Mistral Small 4 |
| **发布日期** | Shieldstral 2026-08-04（Apache 2.0）；Small 4 2026-03 |
| **参数量** | Shieldstral 3B；Mistral Small 4 ≈119B total / 6.5B active（MoE 128 expert / 4 active） |
| **数据量** | 未完全公开 |
| **上下文长度** | Small 4: 256K |
| **主要创新点** | (1) **Shieldstral（08-04）**：3B 开放多模态安全分类器，Apache 2.0，policy-adaptive 问答式评估，12 语言，可在 16GB GPU 运行；(2) 欧洲主权 AI 定位（Microsoft 多十亿美元欧洲 GPU 基建合作，2026-07）；(3) Small 4 三合一：reasoning + multimodal + agentic；(4) Magistral Medium 纯 RL 推理模型；Medium 3.5 / OCR 4 上架 Azure Foundry |
| **论文链接** | [HF Shieldstral](https://huggingface.co/mistralai/Shieldstral) · [mistral.ai](https://mistral.ai/news/) |

---

## 7. Qwen (Alibaba) — Qwen3.8-Flash(-Next) / Qwen3.8-Max

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.8 系列：Flash / Flash-Next / Max |
| **英文标题** | Qwen 3.8 Family: Flash, Flash-Next, Max |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8-Flash / Qwen3.8-Flash-Next / Qwen3.8-Max |
| **发布日期** | Qwen3.8-Max blog 2026-08-02；Qwen3.8-Flash & Flash-Next 2026-08-26；Max 权重 2026-08-12 |
| **参数量** | Qwen3.8-Max 2.4T / 95B active；Qwen3.8-Flash-Next 125B backbone / 6B active + 51B N-gram embedding + 4B MTP |
| **数据量** | 未完全公开 |
| **上下文长度** | Flash 多模态 262K→1M；Max 1M |
| **主要创新点** | (1) **Qwen3.8-Flash（08-26）**：多模态上下文 262K→1M，训练成本为 Qwen3.7-Plus 的 1/9，定价 ¥1/¥3 per M；(2) **Flash-Next（08-26，全新）**：Gated DeltaNet + Qwen Sparse Attention + Gated Residual + Muon，开放权重——**Qwen4 架构 early preview**（linear/hybrid attention 商品化的又一标志）；(3) **Max**：Sparse MoE + Hybrid Attention，首个开源 Max 级，OSWorld 86.1 / PaperBench 93.0；(4) Qwen3.6 / 3.5-Omni (ARIA) 陆续开源 |
| **论文链接** | [Qwen Blog](https://qwen.ai/blog) · [HF Qwen](https://huggingface.co/Qwen) · [Qwen3.8 technical report (log)](https://qwen.ai/blog/qwen3-8) |

---

## 8. Microsoft — MAI-Thinking-1 / Phi-4-reasoning-vision

| 字段 | 内容 |
|------|------|
| **中文标题** | MAI-Thinking-1：从企业数据持续 RL 的推理模型 |
| **英文标题** | MAI-Thinking-1: A reasoning model from first principles with continuous RL |
| **发布机构** | Microsoft (MAI + MSR) |
| **模型系列** | MAI-Thinking-1 / MAI-1 / Phi-4-reasoning-vision |
| **发布日期** | MAI-Thinking-1 report 2026-08-12（arXiv）；Phi-4-rv-15B 2026-03（arXiv: 2603.03975, MSR-TR-2026-10） |
| **参数量** | MAI-Thinking-1: 1T / 35B active MoE；Phi-4-reasoning-vision: 15B |
| **数据量** | MAI-Thinking-1 由企业数据 from-scratch（无第三方蒸馏），持续 RL "hill-climbing" |
| **上下文长度** | 未完全公开 |
| **主要创新点** | (1) **MAI-Thinking-1（08-12 新增）**：端到端 from-scratch 训练（无第三方 teacher 蒸馏），连续多轮 RL "hill-climb" 提升；SWE-Bench Pro 52.8 / AIME2025 97.0 / LiveCodeBench v6 87.7；(2) Phi-4-rv-15B：200B 多模态训练 token，数学/科学推理 + 计算机使用，与 10× 算力模型竞争；(3) Azure OpenAI Service 因 Llama 4 价格压力降价 23%（2026-05） |
| **论文链接** | [MAI-Thinking-1 arXiv](https://arxiv.org/abs/2608.xxxxx) · [Phi-4-rv arXiv:2603.03975](https://arxiv.org/abs/2603.03975) |

---

## 9. NVIDIA — Nemotron 3 Ultra / Nemotron 3 Super

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：混合 Mamba-Attention 高效 MoE |
| **英文标题** | NVIDIA Nemotron 3 Ultra / Nemotron 3 Super |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3（Ultra / Super）+ Nemotron 3.5 Lightning + NeMo Switchyard |
| **发布日期** | Ultra 技术报告 2026-06-09；Super 预训练报告 arXiv:2604.12374；3.5 Lightning 2026-06/07 |
| **参数量** | Ultra 550B / 55B active；Super 120B / 12B active；3.5 Lightning 30B MoE |
| **数据量** | Ultra ~20T tokens |
| **上下文长度** | Ultra 1M |
| **主要创新点** | (1) **Hybrid Mamba-Attention MoE** 架构；(2) LatentMoE + Multi-Token Prediction + NVFP4 量化 + MOPD；(3) 5.9~6× 吞吐（vs GLM-5.1-754B-A40B）；(4) 开放权重（MIT）(5) Nemotron 3 Embed (#1 RTEB) / Diffusion 等实验室系列；(6) NeMo Switchyard 集成 |
| **论文链接** | [Nemotron 3 Ultra report](https://research.nvidia.com/) · [arXiv:2604.12374](https://arxiv.org/abs/2604.12374) |

---

## 10. xAI — Grok 4.6（Grok 5 延后）

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 Model Card（Grok 5 仍在训练） |
| **英文标题** | Grok 4.6 Model Card (2026-08-12) |
| **发布机构** | xAI |
| **模型系列** | Grok 4.6（1.5T 级家族）+ Grok 5（训练中） |
| **发布日期** | Grok 4.6 Model Card 2026-08-12（rev 08-17） |
| **参数量** | 1.5T 级家族；未公开精确 active |
| **数据量** | Grok 5 使用约 6T/10T tokens 训练 |
| **上下文长度** | ~500K |
| **主要创新点** | (1) Grok 4.6 与 Cursor 共同开发（AI 竞争格局新信号，"模型 + 上手工具"协同）；(2) SpaceXAI 合作；(3) **Grok 5** 错过 Q1→Q2→8 月中旬窗口，仍在训练（~550K GPUs，6T/10T tokens）；(4) Grok 4.5 / Grok Build 于 07 开源（80 TPS） |
| **论文链接** | [x.ai](https://x.ai/blog) |

---

## 11. Amazon — Nova 2 (Lite / Pro / Omni / Sonic)

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2 多模态模型家族 |
| **英文标题** | Amazon Nova 2 (Lite / Pro / Omni / Sonic) |
| **发布机构** | Amazon Bedrock / AGI Labs |
| **模型系列** | Nova 2（4 模型：Lite / Pro / Omni / Sonic） |
| **发布日期** | 2026 初（Nova 2 Technical Report PDF）；Sonic refresh 2026-05 |
| **参数量** | 未公开 |
| **数据量** | 未公开 |
| **上下文长度** | 至多 1M tokens |
| **主要创新点** | (1) 四档覆盖：Lite（低成本）/ Pro（全面）/ Omni（音视频全模态）/ Sonic（超低延迟会话/语音）；(2) 多模态动态推理；(3) 通过 AWS Bedrock 分发；(4) 本窗口无实质新报告（与 07-24 一致） |
| **论文链接** | [Amazon Nova tech report (PDF)](https://assets.amazon.science/) · [AWS Nova](https://aws.amazon.com/ai/generative-ai/nova/) |

---

## 12. Zhipu AI — GLM-5.3 / GLM-5.3-Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5.3 权重开源 + GLM-5.3-Flash |
| **英文标题** | Zhipu GLM-5.3 (open weights) & GLM-5.3-Flash |
| **发布机构** | Zhipu AI (智谱) |
| **模型系列** | GLM-5.3 / GLM-5.3-Flash |
| **发布日期** | GLM-5.3 blog 2026-08-14，权重开源 2026-08-28（HF 承诺兑现）；Flash 2026-08-26 |
| **参数量** | GLM-5.3 743B（与 5.2 同基座，全增量来自后训练）；Flash 320B / 18B active |
| **数据量** | Flash 30T 多模态语料 |
| **上下文长度** | 1M |
| **主要创新点** | (1) **GLM-5.3（08-28 权重正式开源）**：与 GLM-5.2 同基座，全部增益来自后训练（SAO + IndexShare + Slime），涌现网络攻防能力（CyberGym 84.5% 超 Mythos 5），因安全审查延后后兑现；(2) **自定义 GLM-5.3 License**：MaaS 云厂 12 个月合并营收 <$10B 免安全审查（另一信源称 $100B，已按多数源取 $10B，待核实）；(3) **Flash（08-26）**：**首个 GLM-5 原生多模态**，Hybrid Sparse + Linear Attention + mHC，~57 AA Index @$0.045/任务，超 GLM-5.2 全系 |
| **论文链接** | [Zhipu Blog](https://z.ai/blog) · [HF Zhipu](https://huggingface.co/zai-org) |

---

## 13. Moonshot AI — Kimi K3

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K3：开放前沿智能（世界首个开放 3T 级模型） |
| **英文标题** | Kimi K3: Open Frontier Intelligence |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K3 |
| **发布日期** | 发布 2026-07-16；完整权重 + 技术报告 2026-07-27（arXiv: 2607.24653） |
| **参数量** | 2.8T total / 104B active（93 层 = 69 KDA + 24 Gated MLA + 1 dense；896 routed experts top-16 + 2 shared） |
| **数据量** | 未完全公开（含大规模合成长上下文数据） |
| **上下文长度** | 1,048,576 (1M)；训练 8K→64K→256K→1M 渐进 |
| **主要创新点** | (1) **Kimi Delta Attention (KDA)**：固定尺寸 recurrent state 而非随 token 增长 KV cache，配合周期性 full-attention 层；(2) **Attention Residuals (AttnRes)**：层间选择性跨层注意力；(3) **Stable LatentMoE**：latent 窄维计算 + Quantile Balancing（去启发式关键超参），896 expert top-16；(4) SiTU-GLU + Gated MLA + Per-Head Muon；(5) 原生多模态（MoonViT-V2 401M enc）；(6) MXFP4/MXFP8 量化感知训练；(7) 整体 scaling 效率较 K2 ~2.5×；(8) 世界首个开放 3T 级模型 |
| **论文链接** | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) · [HF moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) · [Kimi K3 Blog](https://www.kimi.ai/blog/kimi-k3) |

---

## 14. StepFun — Step 3.7 Flash / Step 3.5 Flash / Step3

| 字段 | 内容 |
|------|------|
| **中文标题** | Step 系列高效多模态推理（Step3 / 3.7 Flash / 3.5 Flash） |
| **英文标题** | StepFun Step Series (Step3, Step 3.7 Flash, Step 3.5 Flash) |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step3 / Step 3.7 Flash / Step 3.5 Flash |
| **发布日期** | Step3 2026-05；3.7 Flash 2026-05-29；3.5 Flash 开源基座 |
| **参数量** | Step3 321B / 38B active（MFA + AFD）；Step 3.7 Flash 196B / 11B active |
| **数据量** | 未公开 |
| **上下文长度** | 未完全公开 |
| **主要创新点** | (1) **Model-System Co-design**（模型 + 推理系统协同设计）；(2) MFA (Multi-Framework Attention) + AFD (Adaptive... ) 高效解码；(3) 原生图像 + 视频理解；(4) 3 个 thinking level；(5) 部署在 vLLM / SGLang / Transformers / llama.cpp / NVIDIA NIM |
| **论文链接** | [Step 3.7 Flash Blog](https://static.stepfun.com/) · [Step3-VL-10B arXiv:2601.09668](https://arxiv.org/abs/2601.09668) |

---

## 15. ByteDance — SeedRealtime / Seed2.1

| 字段 | 内容 |
|------|------|
| **中文标题** | SeedRealtime：原生音视频全双工 LLM / Seed2.1 |
| **英文标题** | ByteDance SeedRealtime & Seed 2.1 |
| **发布机构** | ByteDance (Doubao / Seed) |
| **模型系列** | SeedRealtime / Seed2.1 Pro·Turbo |
| **发布日期** | SeedRealtime 2026-08-05；Seed2.1 2026-06/07 |
| **参数量** | 未完全公开 |
| **数据量** | 未公开 |
| **上下文长度** | Seed2.1: 256K |
| **主要创新点** | (1) **SeedRealtime（08-05 新增）**：原生音频-视觉全双工 LLM，统一架构，已在 Doubao 部署；(2) Seed2.1 Pro/Turbo agent 生产力模型（GDPVal 87.9）；(3) Seed Audio 1.0 影视级音频生成；(4) Seed2.0 / Doubao-Seed-2.0-pro 系列 |
| **论文链接** | [Seed Blog](https://seed.bytedance.com/) |

---

## 16. Baichuan — Baichuan-M4 / Baichuan-M3

| 字段 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4：面向持续照护的临床级医疗 agent 系统 |
| **英文标题** | Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care |
| **发布机构** | Baichuan Intelligence (百川智能) + THUBPM, Tsinghua |
| **模型系列** | Baichuan-M4 / Baichuan-M3 |
| **发布日期** | M4 发布新闻 2026-08-26；tech report 2026-06-09（arXiv: 2606.08982）；M3-235B 2026-01（arXiv: 2602.06570） |
| **参数量** | M4 未公开；M3-235B 235B（MoE） |
| **数据量** | 未公开 |
| **上下文长度** | M4 支持长效患者记忆（long-context 临床记忆较 M3 +20 分） |
| **主要创新点** | (1) **M4 三支柱**：Baichuan-Harness（训练/部署一致 runtime + 工具约束 + 多 agent 协调）+ 核心推理模型（SPAR++ span-level reward + reasoning 压缩 + 课程学习 + SAPO 稳定）+ 临床工具层（患者记忆、evidence-based PICO 检索、文档 OCR / X 光 / 皮肤病多模态）；(2) HealthBench 68.6 第一（超 GPT-5.5 的 58.4），HealthBench-Hard 领先 ~16 分，hallucination 降至 3.3%，Citation Precision 90.0；(3) Scan-Bench V2 86.9；(4) **M3-235B**：SPAR 分段流水线 RL + Fact-Aware RL（在线幻觉检测），W4 量化省 74% 显存 + Gated Eagle3 投机解码 96% 加速，Apache 2.0 |
| **论文链接** | [arXiv:2606.08982](https://arxiv.org/abs/2606.08982) (M4) · [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) (M3) · [GitHub M3](https://github.com/baichuan-inc/Baichuan-M3-235B) |

---

## 17. InternLM (上海AI Lab) — Intern-S2-Preview / Intern-S1-Pro

| 字段 | 内容 |
|------|------|
| **中文标题** | Intern-S2-Preview：35B 科学多模态"任务扩展"模型 / Intern-S1-Pro |
| **英文标题** | Intern-S2-Preview: 35B Scientific Multimodal Task-Scaling Model |
| **发布机构** | Shanghai AI Laboratory (InternLM) |
| **模型系列** | Intern-S2-Preview / Intern-S1-Pro / Intern-S1-mini |
| **发布日期** | S2-Preview 2026-08-17（HF）；S1-Pro tech report 2026-03-26（arXiv: 2603.25040）；S1 2025（arXiv: 2508.15763） |
| **参数量** | S2-Preview 35B-A3B（MoE，3B active，从 Qwen3.5 继续预训练）；S1-Pro 1T（首个万亿级科学多模态）；S1-mini 8B |
| **数据量** | S1-Pro 额外 6T 高质多模态（含科学图 caption 管线） |
| **上下文长度** | S2-Preview 128K（文本）/ 64K（多模态） |
| **主要创新点** | (1) **S2-Preview（08-17）**：task scaling（提高科学任务难度/多样性/覆盖）+ 预训练→RL 全链路，35B 即逼近 1T S1-Pro 部分核心任务；MTP + KL loss + CoT 压缩提升效率；材料晶体结构生成首个开源；(2) **S1-Pro**：Grouped Routing 负载均衡 + 梯度估计加速 router embedding + XTuner/LMDeploy 协同，1T RL 训练精度一致；(3) 科学基准大幅超过闭源（SciReasoner 55.5 vs Gemini-3-Pro 14.7 / GPT-5.2 13.6） |
| **论文链接** | [HF Intern-S2-Preview](https://huggingface.co/internlm/Intern-S2-Preview) · [S1-Pro arXiv:2603.25040](https://arxiv.org/abs/2603.25040) · [S1 arXiv:2508.15763](https://arxiv.org/abs/2508.15763) |

---

## 18. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning：低成本高效多语言推理 |
| **英文标题** | 01.AI Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型系列** | Yi-Lightning（2026 无新旗舰） |
| **发布日期** | 2024-12（arXiv: 2412.01253v5） |
| **参数量** | 未公开 exact（Enhanced MoE） |
| **数据量** | 未公开 |
| **上下文长度** | 未公开 |
| **主要创新点** | (1) 高性价比多语言推理（韩/日/越/印尼/泰）；(2) Yi-Lightning 2 于 2026-03 更新（~22% 多语言推理提升）；(3) 2026 转向企业产品（TrueNorth / Boss / Investor / TopSales AI）；(4) 中东北非/东南亚主权部署 |
| **论文链接** | [Yi-Lightning arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |

---

## 19. Apple — AFM 3 (第三代 Foundation Models)

| 字段 | 内容 |
|------|------|
| **中文标题** | Apple Foundation Models 第三代（AFM 3） |
| **英文标题** | Apple Foundation Models 3rd Generation (AFM 3) |
| **发布机构** | Apple |
| **模型系列** | AFM 3（5 模型：Core / Core Advanced / Cloud / ADM Cloud / Cloud Pro） |
| **发布日期** | WWDC26 2026-06-08 |
| **参数量** | AFM 3 Core 3B dense；AFM 3 Core Advanced 20B sparse（1-4B active）；AFM 3 Cloud PT-MoE；ADM 3 Cloud 图像生成 |
| **数据量** | 未公开 |
| **上下文长度** | 未公开 |
| **主要创新点** | (1) 5 模型矩阵（on-device + Private Cloud Compute）；(2) 与 Google 合作构建 Cloud 模型；(3) IFP（混合整数/浮点）动态激活；(4) Quantization-Aware Training 为 Apple silicon 优化；(5) AFM 3 Cloud 在 64.7% 提示词上优于 2025 基线（8.7%）；(6) 16 语言支持 |
| **论文链接** | [machinelearning.apple.com](https://machinelearning.apple.com/) · [Apple Newsroom](https://www.apple.com/newsroom/) |

---

## 今日追踪更新 / Today's Delta (vs 2026-08-30)

本窗口（08-30 → 08-31）**无实质新发布**——同日无重大系统卡/技术报告更新。本次为全量重述 + 若干信源强化与规格补全：

1. **Moonshot Kimi K3**：以 README + 技术报告（arXiv:2607.24653）补全精确规格——93 层 = **69 KDA + 24 Gated MLA + 1 dense**，**896 routed experts（top-16）+ 2 shared**、Latent MoE 3584、MoonViT-V2 401M、MXFP4/MXFP8 量化感知训练、上下文 1,048,576（8K→64K→256K→1M 渐进）。
2. **InternLM**：确认 S2-Preview 为 **35B-A3B**（3B active，从 Qwen3.5 继续预训练），且 S1-Pro/S2 家族形成"万亿级 vs 35B 高效 task-scaling"双轨。
3. **Baichuan**：补全 M4 技术报告（arXiv:2606.08982）与 M3-235B 详细方法（SPAR 分段奖励 + Fact-Aware RL，W4 量化 74% 显存节省 + Gated Eagle3 96% 加速，Apache 2.0）。
4. **验证确认**：DeepSeek / OpenAI / Google / Meta / Anthropic / Mistral / Qwen / Microsoft / NVIDIA / xAI / Amazon / Zhipu / StepFun / ByteDance / 01.AI / Apple 均无 08-30 之后的新报告；Grok 5 与 Llama 4 (405B) 仍悬置，未见兑现。

> 注：GLM-5.3 License 营收阈值 $10B vs $100B 信源不一致，按多数源取 $10B（medium confidence）；Intern/Microsoft 个别链接为占位，正式页以机构官网为准。

---

## 行业趋势总结 / Key Industry Trends (2026-08)

1. **线性/混合线性注意力正式商品化**：Qwen Flash-Next (Gated DeltaNet) + GLM-5.3-Flash (Sparse+Linear) + Kimi K3 (KDA) + Nemotron 3 Ultra (Mamba) 四线并进，长上下文不再必然伴随 KV 内存线性增长。
2. **MoE 稀疏激活仍绝对主流**：激活参数占总参数 1/20~1/30（K3 2.8T/104B、DeepSeek 1.6T/49B、Nemotron 550B/55B、Qwen3.8-Max 2.4T/95B）。
3. **后训练/测试时 Scaling 全面接管增量**：GLM-5.3 与 5.2 同基座、全部增益来自后训练；微软/Anthropic/OpenAI 均做持续 RL。
4. **多模态 Flash 化**：低成本"原生多模态"成为标配（GLM Flash 系、Gemini 3.5 Flash、Muse Glimmer、Qwen Flash）。
5. **安全监管进入"文档即产品"阶段**：GLM 自定义 License 营收阈值条款、OpenAI "Pacing"、ASL-3 blockers、Floor/Sonn 定价转永久——约束显性化为发布节奏的一部分。
6. **垂直领域模型成新报告载体**：Baichuan-M4（医疗 agent）、Intern-S2/S1-Pro（科学）、SeedRealtime（音视频全双工）、Shieldstral（安全分类器）——"Foundation model + 工具/agent 系统"成为报告形态。
7. **开放权重许可双轨分化加剧**：Meta 重返 Apache 2.0 (Glimmer)、DeepSeek MIT，国产模型（GLM-5.3、Qwen）加入自定义许可条款。
8. **中国发布窗口纪律分化**：Kimi/GLM 兑现承诺 vs Grok 5/Meta 405B 持续延后——执行力成为竞争分化因子。
9. **Agentic 能力成官方评测主战场**：OSWorld / SWE-Bench / Terminal-Bench / GDPval 在几乎所有系统卡中占据中心位置。
10. **万亿级科学/医疗特化**：Intern-S1-Pro (1T 科学) 与 Baichuan-M4（临床医疗）显示垂直深度 + 通用广度双轨路线。

---

*Generated: 2026-08-31 | Source: Web search aggregation | Next update: 2026-09-01*
