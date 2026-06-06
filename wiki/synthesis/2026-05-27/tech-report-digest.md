---
title: 各大 AI 公司最新技术报告汇总 (2026年5月·第三版)
type: synthesis
created: 2026-05-27
updated: 2026-05-27
sources:
  - DeepSeek V3 Technical Report (arXiv:2412.19437)
  - DeepSeek V3.2 Technical Report (arXiv:2512.02556)
  - OpenAI GPT-5 System Card (arXiv:2601.03267)
  - The Llama 4 Herd (Meta, Apr 2025)
  - Gemini 2.5 Technical Report (arXiv:2507.06261)
  - Claude Opus 4 & Sonnet 4 System Card (May 2025)
  - Magistral Technical Report (arXiv:2506.10910)
  - Ministral 3 Technical Report (arXiv:2601.08584)
  - Qwen3 Technical Report (arXiv:2505.09388)
  - Yi-Lightning Technical Report (arXiv:2412.01253)
  - Phi-4 Technical Report (Dec 2024)
  - Phi-4-reasoning Technical Report (Apr 2025)
  - Phi-4-reasoning-vision Technical Report (Mar 2026)
  - Apple Intelligence Foundation Language Models: Tech Report 2025 (arXiv:2507.13575)
  - NVIDIA Nemotron 3 White Paper (arXiv:2512.20856)
  - Nemotron 3 Nano Technical Report
  - Amazon Nova Family Technical Report (arXiv:2506.12103)
  - Amazon Nova Premier Technical Report (Apr 2025)
  - GLM-5 Technical Report (arXiv:2602.15763)
  - InternLM3 Model Card (Jan 2025)
  - Kimi K2 Technical Report (arXiv:2507.20534)
  - Kimi K2.5 Technical Report (arXiv:2602.02276)
  - Seed 2.0 Model Card (ByteDance, Feb 2026)
  - Baichuan-Omni-1.5 Technical Report (arXiv:2501.15368)
  - Baichuan-M3 Technical Report (arXiv:2602.06570)
tags: [tech-report, survey, 2026, deepseek, openai, meta, google, anthropic, mistral, qwen, 01-ai, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun, baichuan]
---

# 各大 AI 公司最新技术报告汇总 (2026年5月·第三版)

> 截至 2026 年 5 月 27 日，覆盖 **21 家** AI 机构的最新 Tech Report / System Card。
> 本版在 05-26 版基础上补充硬件配置参数、DeepSeek V3.2、GPT-5 详细规格、Llama 4 原生多模态、Magistral (Mistral 推理模型)、Phi 家族新增、NVIDIA Nemotron 3 系列、xAI Grok 3、Kimi K2.5、Baichuan 垂直医疗、Apple PT-MoE 等细节。

---

## DeepSeek — 深度求索

### DeepSeek-V3

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V3 技术报告 |
| **英文标题** | DeepSeek-V3 Technical Report |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-V3 |
| **发布日期** | 2024-12-27 |
| **核心参数** | 671B 总参数, 37B 激活参数; MoE (256 experts, 8 active); Multi-head Latent Attention (MLA); FP8 混合精度; 14.8T tokens; 128K 上下文 |
| **训练硬件** | 2,048 NVIDIA H800 GPUs; 总计 2.788M GPU hours |
| **主要创新** | 无辅助损失负载均衡; Multi-Token Prediction (MTP); 首个大规模 FP8 训练验证; 训练零故障 |
| **论文链接** | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) |

### DeepSeek-V3.2

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V3.2：推动开源大语言模型前沿 |
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-V3.2 / DeepSeek-V3.2-Speciale |
| **发布日期** | 2025-09-29 (Exp 版) |
| **核心参数** | 延续 V3 MoE 架构; 新增 DeepSeek Sparse Attention (DSA); RL 扩展 |
| **主要创新** | **DSA 稀疏注意力** — 大幅降低长上下文计算复杂度; **可扩展 RL 框架** — V3.2-Speciale 在 IMO 2025/IOI 2025 得金牌, 性能匹敌 Gemini 3.0 Pro; **大规模 Agentic 数据合成管道** — 整合推理与工具使用 |
| **论文链接** | [GitHub: DeepSeek-V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) |

---

## OpenAI

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **英文标题** | GPT-5 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-thinking-pro) |
| **发布日期** | 2025-08-07 |
| **核心参数** | 400K 上下文窗口; 128K 最大输出 tokens; 知识截止 2024-09-30 |
| **主要创新** | **统一路由系统** — 智能路由区分快速任务(gpt-5-main)与深度推理(gpt-5-thinking); **Router 持续学习** — 基于用户切换信号/Pref Rate/正确性实时优化; **Safe-completions** — 新安全训练方法; 幻觉降低 3x; Sycophancy 降低显著 |
| **论文链接** | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) / [System Card](https://www.openai.com/index/gpt-5-system-card/) |

---

## Meta AI — LLaMA

### Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 家族：原生多模态 AI 创新的新时代 |
| **英文标题** | The Llama 4 Herd: The Beginning of a New Era of Natively Multimodal AI Innovation |
| **机构** | Meta AI |
| **模型名称** | Llama 4 Scout (17Bx16E) / Llama 4 Maverick (17Bx128E) / Llama 4 Behemoth (teacher) |
| **发布日期** | 2025-04-05 |
| **核心参数** | Scout: 109B 总参数, 17B 激活, 16 experts, ~40T tokens, **10M 上下文**; Maverick: 400B 总参数, 17B 激活, 128 experts, ~22T tokens, 1M 上下文 |
| **主要创新** | **首个开源原生多模态 MoE**; Early Fusion 架构同时处理文本+图像; Scout 可单卡 H100 (Int4) 部署、10M 上下文长度业界最长; Behemoth teacher 超越 GPT-4.5/Claude Sonnet 3.7/Gemini 2.0 Pro |
| **论文/链接** | [Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md) |

---

## Google DeepMind — Gemini

### Gemini 2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5：以先进推理、多模态、长上下文和下一代智能体能力推动前沿 |
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **机构** | Google DeepMind |
| **模型名称** | Gemini 2.5 Pro / Gemini 2.5 Flash / Gemini 2.0 Flash / Flash-Lite |
| **发布日期** | 2025-06-17 (GA) |
| **核心参数** | Pro: 知识截止 2025-01; 原生多模态 (text+audio+image+video); 支持 3 小时视频; Flash: 支持 thinking budget 控制; 输出 token 减少 20-30% |
| **主要创新** | **Thinking Model** — 原生推理能力; **Deep Think** — 实验性增强推理模式 (USAMO 2025 高分, MMMU 84.0%); **Agentic 能力** — 结合长上下文+多模态+推理, 支持计算机使用 (Project Mariner); **MCP 原生支持**; 年内 Aider Polyglot 提升 5x, SWE-bench 提升 2x |
| **论文链接** | [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) |

---

## Anthropic — Claude

### Claude Opus 4 & Sonnet 4

| 项目 | 内容 |
|------|------|
| **中文标题** | 系统卡：Claude Opus 4 & Claude Sonnet 4 |
| **英文标题** | System Card: Claude Opus 4 & Claude Sonnet 4 |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4 / Claude Sonnet 4 |
| **发布日期** | 2025-05-22 |
| **核心参数** | Opus 4: $15/$75 per M tokens (input/output); Sonnet 4: $3/$15; 两者均支持 hybrid 模式 (即时/扩展思考) |
| **主要创新** | **Hybrid Reasoning Model** — 同一模型支持即时响应与扩展思考; SWE-bench Verified: Opus 72.5%, Sonnet 72.7%; Terminal-bench 43.2% (Opus); 可持续运行数小时的长时间代理任务; Opus 4 按 ASL-3 标准部署, Sonnet 4 按 ASL-2; CBRN 能力评估显著提升 |
| **论文链接** | [System Card PDF](https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf) |

---

## Mistral AI

### Magistral (推理模型)

| 项目 | 内容 |
|------|------|
| **中文标题** | Magistral：Mistral 的第一个推理模型 |
| **英文标题** | Magistral: Mistral's First Reasoning Model |
| **机构** | Mistral AI |
| **模型名称** | Magistral Small (24B, Apache 2.0) / Magistral Medium |
| **发布日期** | 2025-06-12 |
| **核心参数** | Small: 24B 参数; Medium: 基于 Mistral Medium 3; 纯 RL 训练 (无蒸馏) |
| **主要创新** | **纯 RL 推理训练** — Medium 版纯 RL 达到 AIME-24 提升近 50%; **多模态推理涌现** — 纯文本 RL 也提升多模态理解; Magistral Small 开源 (Apache 2.0); 长思维链推理 |
| **论文链接** | [arXiv:2506.10910](https://arxiv.org/abs/2506.10910) |

### Ministral 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3：高效密集语言模型系列 |
| **英文标题** | Ministral 3: Efficient Dense Language Models |
| **机构** | Mistral AI |
| **模型名称** | Ministral 3 (3B / 8B / 14B) — 各含 Base/Instruct/Reasoning 变体 |
| **发布日期** | 2025 年末 |
| **核心参数** | 14B/8B/3B 参数; 256K 上下文 (推理版 128K); 原生视觉理解; Cascade Distillation 训练 |
| **主要创新** | **Cascade Distillation** — 迭代剪枝+蒸馏从 24B teacher 高效获取小模型; 仅用 1-3T tokens 训练即可匹敌 36T tokens 训练的竞品; 全系列 Apache 2.0 |
| **论文链接** | [arXiv:2601.08584](https://arxiv.org/abs/2601.08584) |

### Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3：最先进的开放模型 |
| **英文标题** | Mistral Large 3: A State-of-the-Art Open Model |
| **机构** | Mistral AI |
| **模型名称** | Mistral Large 3 |
| **发布日期** | 2025-12 |
| **核心参数** | 675B 总参数, 41B 激活; MoE 架构; 3,000 H200 GPUs 训练; Apache 2.0 |
| **主要创新** | Mistral 首个大规模 MoE (继 Mixtral 后); 开源可商用; 多语言能力突出; NVFP4 量化支持 |
| **论文链接** | [Mistral Blog](https://mistral.ai/news/mistral-3) |

---

## Qwen (Alibaba) — 通义千问

### Qwen3

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **机构** | Alibaba Cloud (Qwen Team) |
| **模型名称** | Qwen3 系列 (6 个 Dense: 0.6B~32B; 2 个 MoE: 30B-A3B / 235B-A22B) |
| **发布日期** | 2025-04-29 |
| **核心参数** | 旗舰: 235B 总参数, 22B 激活; 36T tokens 预训练; 119 种语言; MoE + Dense 混合架构 |
| **主要创新** | **Thinking/Non-Thinking 统一框架** — 单模型同时支持快速响应和深度推理; **Thinking Budget** — 用户可控推理计算量; **Weak Distillation** — 从旗舰模型高效蒸馏小模型; 119 语言覆盖 |
| **论文链接** | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) |

---

## Yi (01.AI) — 零一万物

### Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **机构** | 01.AI (零一万物) |
| **模型名称** | Yi-Lightning |
| **发布日期** | 2024-12-03 |
| **核心参数** | MoE 架构; 增强的专家分割与路由机制; 优化的 KV-cache 技术 |
| **主要创新** | **MoE + 混合注意力** — 局部滑动窗口 + 全局注意力, KV-cache 减少 82.8%; Chatbot Arena 综合第 6, 中文第 2, 数学第 3, 编码第 4; RAISE 安全框架 |
| **论文链接** | [arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |

---

## Microsoft — Phi

### Phi-4

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **英文标题** | Phi-4 Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4 (14B) |
| **发布日期** | 2024-12 |
| **核心参数** | 14B 参数 Dense Transformer; 400B tokens; 数据质量为中心 |
| **主要创新** | **数据质量优先** — 大量使用合成数据超越 teacher GPT-4; STEM QA 能力显著 |
| **论文链接** | [arXiv:2412.08905](https://arxiv.org/abs/2412.08905) |

### Phi-4-reasoning

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning (14B) / Phi-4-reasoning-plus |
| **发布日期** | 2025-04 |
| **核心参数** | 基于 Phi-4 基础; SFT on 1.4M STEM 题 + o3-mini traces; Plus 版增加短阶段 RL |
| **主要创新** | **14B 推理模型匹敌 70B** — 超越 DeepSeek-R1-Distill-Llama-70B, 接近 DeepSeek-R1 全量; 推理是可迁移的元技能 — 非训练域也有提升 |
| **论文链接** | [arXiv:2504.21318](https://arxiv.org/abs/2504.21318) |

### Phi-4-reasoning-vision

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision 技术报告 |
| **英文标题** | Phi-4-reasoning-vision Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning-vision (15B) |
| **发布日期** | 2026-03 |
| **核心参数** | 15B 参数; 200B 多模态 tokens; 动态分辨率编码器; 混合推理/非推理模式 |
| **主要创新** | **小型端侧多模态推理** — 仅用竞品 1/5 训练数据; 科学/数学推理出色; 显式 mode tokens 控制推理/快速切换 |
| **论文链接** | [arXiv:2603.03975](https://arxiv.org/abs/2603.03975) |

---

## Apple

### Apple Intelligence Foundation Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型：2025 技术报告 |
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **机构** | Apple |
| **模型名称** | On-Device (~3B) / Server (PT-MoE) |
| **发布日期** | 2025-07-17 |
| **核心参数** | On-Device: ~3B 参数, 2-bit 量化; Server: Novel Parallel-Track MoE (PT-MoE); 多语言+多模态 (text+image); 支持 tool use |
| **主要创新** | **KV-cache sharing** — 设备端高效推理; **2-bit 量化感知训练** — 极小模型尺寸; **PT-MoE** — Track Parallelism + MoE + 交错全局-局部注意力; **Foundation Models 框架** — Swift API, guided generation, LoRA; Private Cloud Compute |
| **论文链接** | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) |

---

## NVIDIA

### Nemotron 3 家族

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron 3：高效开放的智能 |
| **英文标题** | NVIDIA Nemotron 3: Efficient and Open Intelligence |
| **机构** | NVIDIA |
| **模型名称** | Nemotron 3 Nano (30B-A3B) / Super / Ultra |
| **发布日期** | 2025-12 (Nano 已发布; Super/Ultra 待发布) |
| **核心参数** | Nano: 31.6B 总参数, 3.2B 激活; 25T tokens; 1M 上下文; MoE Hybrid Mamba-Transformer; FP8 量化 |
| **主要创新** | **MoE Hybrid Mamba-Transformer** — 结合状态空间模型与注意力; **LatentMoE** (Super/Ultra) — 新方法提升质量不损吞吐; **多环境 RL** — 同时推理+工具使用+chat; 推理预算控制; **MTP** (Super/Ultra) — 加速文本生成 |
| **论文链接** | [arXiv:2512.20856](https://arxiv.org/abs/2512.20856) |

### Nemotron Nano 2

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron Nano 2：高效混合 Mamba-Transformer 推理模型 |
| **英文标题** | NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model |
| **机构** | NVIDIA |
| **模型名称** | Nemotron-Nano-9B-v2 |
| **发布日期** | 2025-08 |
| **核心参数** | 9B 参数 (从 12B 压缩); 20T tokens 预训练; FP8; 128K 上下文 |
| **主要创新** | **Minitron 压缩** — 从 12B 剪枝蒸馏到 9B, 单 A10G 可运行 128K; 推理吞吐比 Qwen3-8B 高 3-6x |
| **论文链接** | [arXiv:2508.14444](https://arxiv.org/abs/2508.14444) |

---

## xAI — Grok

### Grok 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 3：xAI 的基础模型 |
| **英文标题** | Grok 3: xAI's Foundation Model |
| **机构** | xAI |
| **模型名称** | Grok 3 / Grok 3 Mini |
| **发布日期** | 2025-02-18 (Beta, 持续更新) |
| **核心参数** | 推测 MoE (数百专家); 131K 上下文; "Colossus" 200K H100 GPUs 训练; 持续在线训练 |
| **主要创新** | **Colossus 超算** — 122 天建成 100K GPU, 5 月翻倍至 200K; **实时 X 数据流** — 独特实时数据优势; 推理/编码/数学领先; AIME 2024 60%, GPQA 79.1%, MMLU-Pro 83.1% |
| **论文链接** | 未发布正式 Tech Report; [Azure AI Catalog](https://ai.azure.com/catalog/models/grok-3) |

---

## Amazon — Amazon Nova

### Amazon Nova Family / Nova Premier

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族技术报告 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **机构** | Amazon AGI |
| **模型名称** | Nova Micro / Lite / Pro / Premier / Canvas / Reel / Sonic |
| **发布日期** | 2024-12-03 (初版); 2025-04-30 (Premier) |
| **核心参数** | Premier: 1M 上下文; 多模态 (text+image+video); Pro/Lite: 多模态输入; Micro: 纯文本; Sonic: 统一语音+文本 |
| **主要创新** | **Premier 1M 上下文** — 单次分析大型代码库/长视频; **Nova Sonic** — 首个统一语音+文本流式架构, 支持自然轮次切换; 行业领先性价比 |
| **论文链接** | [Amazon Science](https://www.amazon.science/publications/the-amazon-nova-family-of-models-technical-report-and-model-card) / [Premier](https://www.amazon.science/publications/amazon-nova-premier-technical-report-and-model-card) |

---

## Zhipu AI — 智谱 AI (GLM)

### GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到工程智能 |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **机构** | Zhipu AI & Tsinghua University |
| **模型名称** | GLM-5 (744B-A40B) |
| **发布日期** | 2026-02-17 |
| **核心参数** | 744B 总参数, 40B 激活; MoE; DSA (DeepSeek Sparse Attention); 28.5T tokens; 全面适配 7 种国产 GPU 芯片 |
| **主要创新** | **DSA 稀疏注意力** — 大幅降低部署成本; **异步 RL 基础设施 slime** — 解耦生成与训练; **异步 Agent RL 算法** — 长时域交互学习; 国产芯片全栈适配 (华为昇腾/摩尔线程等); SWE-bench Verified 77.8%; 中文 GPU 生态最优支持 |
| **论文链接** | [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |

---

## InternLM (Shanghai AI Lab) — 上海人工智能实验室

### InternLM3

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM3 模型卡 |
| **英文标题** | InternLM3 Model Card |
| **机构** | Shanghai AI Laboratory |
| **模型名称** | InternLM3-8B-Instruct |
| **发布日期** | 2025-01-15 |
| **核心参数** | 8B 参数; 4T tokens (比同类少 75% 训练成本); 支持深度思考+普通响应双模式 |
| **主要创新** | **4T tokens 高效训练** — 仅用同类 1/4 数据量达到 SOTA; 超越 Llama3.1-8B / Qwen2.5-7B; 深度思考模式 (长思维链) |
| **论文链接** | [GitHub](https://github.com/InternLM/InternLM) |

---

## Moonshot AI (Kimi) — 月之暗面

### Kimi K2

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放的智能体智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **机构** | Moonshot AI (月之暗面) |
| **模型名称** | Kimi K2 (1T MoE) |
| **发布日期** | 2025-07 |
| **核心参数** | 1.04T 总参数, 32B 激活; 384 experts, 8 active; MLA 注意力; 128K 上下文; 15.5T tokens |
| **主要创新** | **MuonClip 优化器** — Muon + QK-Clip 解决训练不稳定; 零 loss spike; **大规模 Agentic 数据合成**; **Agent 能力领先** — Tau2-Bench 66.1, SWE-bench Verified 65.8%; 非 thinking 模式下超越多数闭源模型 |
| **论文链接** | [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) |

### Kimi K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.5：视觉智能体智能 |
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **机构** | Moonshot AI (月之暗面) |
| **模型名称** | Kimi K2.5 (1T MoE + MoonViT) |
| **发布日期** | 2026-02-03 |
| **核心参数** | 基于 K2 架构; 新增 MoonViT 视觉编码器 (400M 参数); ~15T 多模态 tokens 持续预训练; 256K 上下文 |
| **主要创新** | **原生多模态 Agent** — 文本+视觉联合预训练; **Agent Swarm** — 并行子代理编排, 延迟降低 4.5x; **零视觉 SFT** — 视觉能力从 RL 涌现; HLE-Full 30.1%, AIME 2025 96.1% |
| **论文链接** | [arXiv:2602.02276](https://arxiv.org/abs/2602.02276) |

---

## ByteDance (豆包/Doubao) — 字节跳动

### Seed 2.0

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 2.0 模型卡 |
| **英文标题** | Seed 2.0 Model Card |
| **机构** | ByteDance Seed Team |
| **模型名称** | Seed 2.0 (Pro / Lite / Mini / Code) |
| **发布日期** | 2026-02-14 |
| **核心参数** | 多模态 LLM; 支持视觉/空间/运动推理; 长上下文 agent 工作流 |
| **主要创新** | **视觉推理领先** — MMSIBench/MotionBench/VideoMME SOTA; **Token 成本降低一个数量级**; 支持 Plan-Act-Reflect 循环; 500x 日 Token 用量增长验证生产可靠性 |
| **论文链接** | [GitHub: ByteDance-Seed/Seed2.0](https://github.com/ByteDance-Seed/Seed2.0) |

---

## StepFun (阶跃星辰)

### Step-2 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-2 系列大模型 |
| **英文标题** | Step-2 Family |
| **机构** | StepFun (阶跃星辰) |
| **模型名称** | Step-2 (万亿参数 MoE) / Step-2 mini / Step-2 文学大师版 |
| **发布日期** | 2025-01 (Step-2 正式版) |
| **核心参数** | Step-2: 万亿参数 MoE, 国内创业公司首个万亿参数模型; Step-2 mini: ~3% 参数量保持 80%+ 性能, MFA 注意力架构, 32K 上下文 |
| **主要创新** | **MFA (Multi-matrix Factorization Attention)** — 自研注意力架构, 节省 94% KV 缓存; LiveBench 国产模型第一; MFA-Key-Reuse 变体进一步加速; Step-2 文学大师版专注文学创作 |
| **论文链接** | 未发布正式 Tech Report; [StepFun 平台文档](https://platform.stepfun.com) |

### Step-Audio 2

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-Audio 2 技术报告 |
| **英文标题** | Step-Audio 2 Technical Report |
| **机构** | StepFun (阶跃星辰) |
| **发布日期** | 2025-07-23 |
| **主要创新** | 语音理解+对话 SOTA; 开源 Mini 版 |
| **论文链接** | [arXiv:2507.16632](https://arxiv.org/abs/2507.16632) |

---

## Baichuan — 百川智能

### Baichuan-Omni-1.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-Omni-1.5 技术报告 |
| **英文标题** | Baichuan-Omni-1.5 Technical Report |
| **机构** | Baichuan Inc. |
| **模型名称** | Baichuan-Omni-1.5 (7B LLM backbone + 视觉+音频分支) |
| **发布日期** | 2025-01-26 |
| **核心参数** | 全模态 (text+image+audio+video); 500B 高质量多模态数据; 8-layer RVQ 音频分词器 (Baichuan-Audio-Tokenizer) |
| **主要创新** | **Omni-modal 统一架构** — 同时支持文本/图像/音频/视频; **医疗图像理解 SOTA** — 超越 Qwen2-VL-72B; 端到端音频生成; GPT-4o-mini 平均高 6 点 |
| **论文链接** | [arXiv:2501.15368](https://arxiv.org/abs/2501.15368) |

### Baichuan-M3 (医疗垂直)

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M3：临床问诊建模实现可信医疗决策 |
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **机构** | Baichuan Inc. |
| **模型名称** | Baichuan-M3 (235B) |
| **发布日期** | 2026-02-06 |
| **主要创新** | **医疗垂直领域 SOTA** — HealthBench-Hard 超越 GPT-5.2; **SPAR 算法** — 步骤惩罚优势算法解决医疗长链路信用分配; **Fact-Aware RL** — 事实验证融入强化学习; 三阶段多专家融合训练; Gated Eagle3 投机解码 96% 加速 |
| **论文链接** | [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) |

---

## 综合趋势分析

### 1. MoE 架构主流化
几乎所有前沿模型都采用 MoE: DeepSeek V3 (256 experts), Llama 4 (16/128 experts), Qwen3 (235B-A22B), Mistral Large 3 (MoE), GLM-5 (744B-A40B), Kimi K2 (384 experts), Step-2 (万亿 MoE)。MoE 已从可选特性变为标配架构。

### 2. Hybrid 架构崛起
**Mamba-Transformer 混合**: NVIDIA Nemotron 3 系列引领 SSM+Attention 融合; **稀疏注意力**: DeepSeek V3.2 的 DSA 和 GLM-5 的 DSA 都证明稀疏注意力是长上下文的关键技术; **APA (MLA)**: DeepSeek 开创的 Multi-head Latent Attention 被 Kimi K2/K2.5 采用。

### 3. Thinking Mode 统一化
Qwen3 的 Thinking/Non-Thinking 统一框架、Claude 4 的 Hybrid Reasoning、GPT-5 的路由系统、InternLM3 的深度思考模式 — 单一模型同时支持快速响应与深度推理成为标准。

### 4. Agentic 能力成为核心竞争维度
Kimi K2 以 Agent 为设计核心; GLM-5 定位为 "Agentic Engineering"; Gemini 2.5 强调 agentic workflows; Anthropic 发布 ASL-3 级别的 Agent 安全评估。Agent 能力已与推理/编码并列为核心赛道。

### 5. 多模态全面铺开
Llama 4 原生多模态首秀; Phi-4-reasoning-vision 证明小模型也能多模态推理; Kimi K2.5 统一文本+视觉; Apple 端侧多模态。几乎所有新模型都支持图像输入。

### 6. 国产 GPU 生态适配
GLM-5 首次实现全栈适配 7 种国产 GPU; Step-3 在国产芯片上推理效率达 DeepSeek-R1 的 300%。国产化替代从口号变为工程现实。

### 7. 强化学习 (RL) 重新成为焦点
Magistral 证明纯 RL 即可训练推理模型; Phi-4-reasoning-plus 通过短 RL 获得提升; GLM-5 的异步 RL 基础设施 slime; Kimi K2 的 MuonClip 优化器。RL 从对齐工具升级为能力创造手段。

### 8. 顶级实验室的路径分化
- **OpenAI / Anthropic**: 安全优先, 闭源前沿, 发布 System Card 详细安全评估
- **Meta / Mistral / Qwen / 01.AI**: 开源驱动, MoE + 多模态, Apache 2.0 许可证
- **Google / Amazon / Apple**: 生态绑定, 长上下文 + Agent + 性价比
- **DeepSeek / Zhipu / Moonshot**: 中国开源主力, 工程创新 (DSA / Muon / slime)
- **Baichuan / StepFun**: 垂直领域突破 (医疗 / 语音)
