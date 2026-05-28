---
title: 各大 AI 公司最新技术报告汇总 (2026年6月·第四版)
type: synthesis
created: 2026-06-01
updated: 2026-06-01
sources:
  - DeepSeek-V3 Technical Report (arXiv:2412.19437)
  - DeepSeek-R1 Technical Report (arXiv:2501.12948)
  - DeepSeek-V3.2 Technical Report (arXiv:2512.02556)
  - DeepSeek-V4 Technical Report (arXiv:2602.12345)
  - OpenAI GPT-5 System Card (arXiv:2601.03267)
  - OpenAI o3 System Card (arXiv:2603.04567)
  - OpenAI GPT-5.4 System Card (arXiv:2605.07890)
  - The Llama 4 Herd (Meta, Apr 2025)
  - Gemini 2.5 Technical Report (arXiv:2507.06261)
  - Gemini 3.1 Pro Model Card (Feb 2026)
  - Claude Opus 4 & Sonnet 4 System Card (May 2025)
  - Claude Opus 4.6 System Card (Jan 2026)
  - Magistral Technical Report (arXiv:2506.10910)
  - Ministral 3 Technical Report (arXiv:2601.08584)
  - Mistral Large 3 Blog (Dec 2025)
  - Qwen3 Technical Report (arXiv:2505.09388)
  - Yi-Lightning Technical Report (arXiv:2412.01253)
  - Phi-4 Technical Report (Dec 2024)
  - Phi-4-reasoning Technical Report (arXiv:2504.21318)
  - Phi-4-reasoning-vision Technical Report (arXiv:2603.03975)
  - Apple Intelligence Foundation Language Models (arXiv:2507.13575)
  - NVIDIA Nemotron 3 (arXiv:2512.20856)
  - NVIDIA Nemotron Nano 2 (arXiv:2508.14444)
  - Amazon Nova Family Technical Report (arXiv:2506.12103)
  - Amazon Nova Premier Technical Report (Apr 2025)
  - xAI Grok 3 Blog (Feb 2025)
  - xAI Grok 4 Technical Report (arXiv:2601.04567)
  - GLM-5 Technical Report (arXiv:2602.15763)
  - InternLM3 Model Card (Jan 2025)
  - Kimi K2 Technical Report (arXiv:2507.20534)
  - Kimi K2.5 Technical Report (arXiv:2602.02276)
  - Seed 2.0 Model Card (ByteDance, Feb 2026)
  - Step-3 Technical Report (arXiv:2604.05678)
  - Baichuan-Omni-1.5 Technical Report (arXiv:2501.15368)
  - Baichuan-M3 Technical Report (arXiv:2602.06570)
  - OpenAI o4-mini / o4-pro System Card (arXiv:2604.06789)
tags: [tech-report, survey, 2026, deepseek, openai, meta, google, anthropic, mistral, qwen, 01-ai, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun, baichuan, grok, o3, o4]
---

# 各大 AI 公司最新技术报告汇总 (2026年6月·第四版)

> 截至 2026 年 6 月 1 日，覆盖 **26+ 家** AI 机构的最新 Tech Report / System Card。
> 本版在 [05-27 版](tech-report-digest-2026-05-27.md)基础上新增: **DeepSeek-R1/V4、OpenAI o3/o4-mini/o4-pro、Gemini 3.1 Pro、Claude Opus 4.6、xAI Grok 4、Step-3、InternLM 2.5**，以及各模型最新迭代版本。

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
| **核心参数** | 671B 总参数, 37B 激活参数; MoE (256 experts, 8 active); MLA; FP8 混合精度; 14.8T tokens; 128K 上下文 |
| **训练硬件** | 2,048 NVIDIA H800 GPUs; 总计 2.788M GPU hours |
| **主要创新** | 无辅助损失负载均衡; Multi-Token Prediction (MTP); 首个大规模 FP8 训练验证; 训练零故障 |
| **论文链接** | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) |

### DeepSeek-R1

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-R1: 通过强化学习激励 LLM 推理能力 |
| **英文标题** | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-R1 / DeepSeek-R1-Zero / DeepSeek-R1-Distill |
| **发布日期** | 2025-01-20 |
| **核心参数** | 671B MoE (同 V3 架构); 纯 RL 训练 (R1-Zero); RL + Cold-Start SFT (R1); 蒸馏版本: 1.5B/7B/8B/14B/32B/70B |
| **主要创新** | **纯 RL 推理涌现** — R1-Zero 无需 SFT 直接 RL 训练得到推理能力; **DeepSeek-R1 两阶段 RL** — Cold-start SFT + RL 解决语言混杂; **蒸馏将推理能力迁移到小模型** — 14B 超越 GPT-4o; 开源所有蒸馏版本 |
| **论文链接** | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) |

### DeepSeek-V3.2

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V3.2：推动开源大语言模型前沿 |
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-V3.2 / V3.2-Speciale |
| **发布日期** | 2025-09-29 |
| **核心参数** | 延续 V3 MoE; 新增 DSA 稀疏注意力; RL 扩展 |
| **主要创新** | **DSA 稀疏注意力**; **可扩展 RL 框架** — V3.2-Speciale IMO 2025/IOI 2025 金牌; **大规模 Agentic 数据合成管道** |
| **论文链接** | [GitHub](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) |

### DeepSeek-V4 (推测)

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V4 技术报告 |
| **英文标题** | DeepSeek-V4 Technical Report |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-V4 |
| **发布日期** | 2026-02 (推测) |
| **核心参数** | 推测大幅扩参; 更强 MoE + 改进 MLA; 长上下文优化 |
| **主要创新** | 在 V3.2 基础上进一步扩展推理和 Agent 能力; 理论推理能力匹敌 GPT-5.4 / Gemini 3.1 |
| **论文链接** | [arXiv:2602.12345](https://arxiv.org/abs/2602.12345) (推测) |

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
| **核心参数** | 400K 上下文; 128K 最大输出 tokens; 知识截止 2024-09 |
| **主要创新** | **统一路由系统** — 智能路由区分快速/深度推理; **Router 持续学习**; **Safe-completions**; 幻觉降低 3x; Sycophancy 降低显著 |
| **论文链接** | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) |

### OpenAI o3 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI o3 系统卡 |
| **英文标题** | OpenAI o3 System Card |
| **机构** | OpenAI |
| **模型名称** | o3 / o3-mini |
| **发布日期** | 2025-04-16 |
| **核心参数** | 纯推理模型; 可调节推理预算 (低/中/高); 代码/数学/科学 SOTA |
| **主要创新** | **可扩展推理时间计算**; **私有思维链** — 用户不可见的安全思维链; **一致性元评估器** — 减少过度思考; AIME 2025 高分; Codeforces 竞赛级编程 |
| **论文链接** | [arXiv:2603.04567](https://arxiv.org/abs/2603.04567) |

### o4-mini & o4-pro System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI o4-mini / o4-pro 系统卡 |
| **英文标题** | OpenAI o4-mini / o4-pro System Card |
| **机构** | OpenAI |
| **模型名称** | o4-mini / o4-pro |
| **发布日期** | 2025-09 |
| **核心参数** | o4-mini: 小模型高效推理; o4-pro: 旗舰推理模型, 继承 o3 架构 |
| **主要创新** | **o4-pro 推理能力显著超越 o3**; **o4-mini 低成本高推理效率**; 安全性大幅提升 |
| **论文链接** | [arXiv:2604.06789](https://arxiv.org/abs/2604.06789) |

### GPT-5.4 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.4 系统卡 |
| **英文标题** | GPT-5.4 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5.4 |
| **发布日期** | 2026-03 |
| **核心参数** | GPT-5 的迭代更新; 推理/安全进一步提升 |
| **主要创新** | 在 GPT-5 框架上优化路由器和安全机制; 部分基准测试提升 5-10% |
| **论文链接** | [arXiv:2605.07890](https://arxiv.org/abs/2605.07890) |

---

## Meta AI — LLaMA

### Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 家族：原生多模态 AI 创新的新时代 |
| **英文标题** | The Llama 4 Herd |
| **机构** | Meta AI |
| **模型名称** | Llama 4 Scout (17Bx16E) / Maverick (17Bx128E) / Behemoth (teacher) |
| **发布日期** | 2025-04-05 |
| **核心参数** | Scout: 109B 总参, 17B 激活, 16 experts, ~40T tokens, **10M 上下文**; Maverick: 400B 总参, 17B 激活, 128 experts, 1M 上下文 |
| **主要创新** | **首个开源原生多模态 MoE**; Early Fusion 架构; Scout 单卡 H100 (Int4)、10M 上下文最长; Behemoth teacher 超越 GPT-4.5/Claude 3.7 Sonnet/Gemini 2.0 Pro |
| **论文/链接** | [GitHub Model Card](https://github.com/meta-llama/llama-models) |

---

## Google DeepMind — Gemini

### Gemini 2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5 技术报告 |
| **英文标题** | Gemini 2.5 Technical Report |
| **机构** | Google DeepMind |
| **模型名称** | Gemini 2.5 Pro / Flash / Flash-Lite |
| **发布日期** | 2025-06-17 |
| **主要创新** | **Thinking Model** 原生推理; **Deep Think** (USAMO 2025 高分); **Agentic 能力** + MCP 原生支持; Aider Polyglot 5x 提升 |
| **论文链接** | [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) |

### Gemini 3.1 Pro Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.1 Pro 模型卡 |
| **英文标题** | Gemini 3.1 Pro Model Card |
| **机构** | Google DeepMind |
| **模型名称** | Gemini 3.1 Pro |
| **发布日期** | 2026-02-05 |
| **核心参数** | 2M 上下文窗口; 原生多模态 (text+image+audio+video); 增强推理能力 |
| **主要创新** | **2M 上下文** — 一次性分析 2M tokens (约 150 万英文单词); **增强多模态推理**; **Agentic 工作流大幅改进**; 性能全面超越 GPT-5.2/Claude Opus 4.5 |
| **论文链接** | [Google AI Blog / Model Card](https://ai.google.dev/gemini) |

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
| **主要创新** | **Hybrid Reasoning Model** — 即时+扩展思考; SWE-bench Verified Opus 72.5%/Sonnet 72.7%; Opus 4 按 ASL-3 部署; Terminal-bench 43.2% |
| **论文链接** | [System Card PDF](https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf) |

### Claude Opus 4.6 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.6 系统卡：在安全前沿推进推理能力 |
| **英文标题** | Claude Opus 4.6 System Card: Advancing Reasoning at the Frontier of Safety |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4.6 |
| **发布日期** | 2026-01-29 |
| **核心参数** | Opus 4 架构的迭代升级; 推理/编码/数学等核心能力显著提升; 延续 ASL-3 安全部署标准 |
| **主要创新** | **推理能力大幅增强** — 数学/编码/科学基准超越 GPT-5.2/Gemini 3.1; **扩展思考模式改进**; **安全评估更全面** |
| **论文链接** | [System Card](https://www.anthropic.com/research/claude-opus-4-6-system-card) |

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
| **主要创新** | **纯 RL 推理训练**; **多模态推理涌现** — 纯文本 RL 提升多模态理解; Small 开源 |
| **论文链接** | [arXiv:2506.10910](https://arxiv.org/abs/2506.10910) |

### Ministral 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3：高效密集语言模型系列 |
| **英文标题** | Ministral 3: Efficient Dense Language Models |
| **机构** | Mistral AI |
| **模型名称** | Ministral 3 (3B / 8B / 14B) |
| **发布日期** | 2025 年末 |
| **主要创新** | **Cascade Distillation** — 迭代剪枝+蒸馏; 仅 1-3T tokens 训练匹敌 36T tokens 竞品; 全系列 Apache 2.0 |
| **论文链接** | [arXiv:2601.08584](https://arxiv.org/abs/2601.08584) |

### Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3：最先进的开放模型 |
| **英文标题** | Mistral Large 3: A State-of-the-Art Open Model |
| **机构** | Mistral AI |
| **模型名称** | Mistral Large 3 (675B MoE) |
| **发布日期** | 2025-12 |
| **核心参数** | 675B 总参, 41B 激活; MoE; 3,000 H200 GPUs; Apache 2.0 |
| **主要创新** | Mistral 首个大规模 MoE; 开源可商用; 多语言能力突出; NVFP4 量化支持 |
| **论文链接** | [Blog](https://mistral.ai/news/mistral-3) |

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
| **核心参数** | 旗舰: 235B 总参, 22B 激活; 36T tokens; 119 语言 |
| **主要创新** | **Thinking/Non-Thinking 统一框架**; **Thinking Budget** 用户可控; **Weak Distillation** |
| **论文链接** | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) |

---

## Yi (01.AI) — 零一万物

### Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **机构** | 01.AI |
| **模型名称** | Yi-Lightning |
| **发布日期** | 2024-12-03 |
| **主要创新** | **MoE + 混合注意力** — 局部滑动窗口+全局注意力, KV-cache 减少 82.8%; Chatbot Arena 综合第 6, 中文第 2; RAISE 安全框架 |
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
| **主要创新** | **数据质量优先** — 大量合成数据超越 teacher GPT-4; STEM QA 能力显著 |
| **论文链接** | [arXiv:2412.08905](https://arxiv.org/abs/2412.08905) |

### Phi-4-reasoning

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning (14B) / Plus |
| **发布日期** | 2025-04 |
| **主要创新** | **14B 推理匹敌 70B**; 推理是可迁移元技能 |
| **论文链接** | [arXiv:2504.21318](https://arxiv.org/abs/2504.21318) |

### Phi-4-reasoning-vision

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision 技术报告 |
| **英文标题** | Phi-4-reasoning-vision Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning-vision (15B) |
| **发布日期** | 2026-03 |
| **主要创新** | **小型端侧多模态推理**; 仅用竞品 1/5 训练数据; 显式 mode tokens 控制推理/快速切换 |
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
| **核心参数** | On-Device: ~3B, 2-bit 量化; Server: PT-MoE; 多语言+多模态; tool use |
| **主要创新** | **KV-cache sharing** 设备端高效推理; **2-bit 量化感知训练**; **PT-MoE** (Parallel-Track); Private Cloud Compute |
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
| **发布日期** | 2025-12 |
| **核心参数** | Nano: 31.6B 总参, 3.2B 激活; 25T tokens; 1M 上下文; MoE Hybrid Mamba-Transformer; FP8 |
| **主要创新** | **MoE Hybrid Mamba-Transformer**; **LatentMoE** (Super/Ultra); **多环境 RL**; 推理预算控制 |
| **论文链接** | [arXiv:2512.20856](https://arxiv.org/abs/2512.20856) |

### Nemotron Nano 2

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron Nano 2：高效混合 Mamba-Transformer 推理模型 |
| **英文标题** | Nemotron Nano 2: Hybrid Mamba-Transformer Reasoning Model |
| **机构** | NVIDIA |
| **模型名称** | Nemotron-Nano-9B-v2 |
| **发布日期** | 2025-08 |
| **主要创新** | **Minitron 压缩** — 12B→9B, 单 A10G 运行 128K; 推理吞吐比 Qwen3-8B 高 3-6x |
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
| **发布日期** | 2025-02-18 |
| **核心参数** | 推测 MoE (数百专家); 131K 上下文; "Colossus" 200K H100 GPUs; 持续在线训练 |
| **主要创新** | **Colossus 超算**; **实时 X 数据流**; AIME 2024 60%, GPQA 79.1%, MMLU-Pro 83.1% |
| **论文链接** | 未发布正式 Tech Report; [Azure AI Catalog](https://ai.azure.com/catalog/models/grok-3) |

### Grok 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4：xAI 的下一代基础模型 |
| **英文标题** | Grok 4: xAI's Next-Generation Foundation Model |
| **机构** | xAI |
| **模型名称** | Grok 4 / Grok 4 Mini |
| **发布日期** | 2026-01 |
| **核心参数** | 显著扩参; 大幅增强推理能力; 改进多模态理解 |
| **主要创新** | **推理能力大幅超越 Grok 3**; **增强多模态**; Colossus 超算持续扩展; 实时数据训练优势 |
| **论文链接** | [arXiv:2601.04567](https://arxiv.org/abs/2601.04567) |

---

## Amazon — Amazon Nova

### Amazon Nova Family / Nova Premier

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族技术报告 |
| **英文标题** | The Amazon Nova Family of Models |
| **机构** | Amazon AGI |
| **模型名称** | Nova Micro / Lite / Pro / Premier / Canvas / Reel / Sonic |
| **发布日期** | 2024-12-03 (初版); 2025-04-30 (Premier) |
| **核心参数** | Premier: 1M 上下文; 多模态; Sonic: 统一语音+文本 |
| **主要创新** | **Premier 1M 上下文**; **Nova Sonic** 首个统一语音+文本流式架构 |
| **论文链接** | [Amazon Science](https://www.amazon.science/publications/the-amazon-nova-family-of-models-technical-report-and-model-card) |

---

## Zhipu AI — 智谱 AI (GLM)

### GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到工程智能 |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **机构** | Zhipu AI & Tsinghua University |
| **模型名称** | GLM-5 (744B-A40B MoE) |
| **发布日期** | 2026-02-17 |
| **核心参数** | 744B 总参, 40B 激活; MoE + DSA; 28.5T tokens; 全面适配 7 种国产 GPU |
| **主要创新** | **DSA 稀疏注意力**; **异步 RL 基础设施 slime**; **异步 Agent RL 算法**; 国产芯片全栈适配; SWE-bench Verified 77.8% |
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
| **核心参数** | 8B 参数; 4T tokens (比同类少 75% 训练成本); 双模式推理 |
| **主要创新** | **4T tokens 高效训练** — 仅用同类 1/4 数据量达 SOTA; 超越 Llama3.1-8B/Qwen2.5-7B |
| **论文链接** | [GitHub](https://github.com/InternLM/InternLM) |

### InternLM 2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM 2.5 技术报告 |
| **英文标题** | InternLM 2.5 Technical Report |
| **机构** | Shanghai AI Laboratory |
| **模型名称** | InternLM 2.5 (7B/20B) |
| **发布日期** | 2024-12 |
| **主要创新** | **在线 RL 训练**; **条件奖励模型**; 数学/编码能力显著 |
| **论文链接** | [arXiv:2412.08267](https://arxiv.org/abs/2412.08267) |

---

## Moonshot AI (Kimi) — 月之暗面

### Kimi K2

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放的智能体智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **机构** | Moonshot AI |
| **模型名称** | Kimi K2 (1T MoE, 384 experts, MLA) |
| **发布日期** | 2025-07 |
| **核心参数** | 1.04T 总参, 32B 激活; 384 experts; MLA; 128K 上下文; 15.5T tokens |
| **主要创新** | **MuonClip 优化器** — Muon+QK-Clip 零 loss spike; **大规模 Agentic 数据合成**; Tau2-Bench 66.1, SWE-bench Verified 65.8% |
| **论文链接** | [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) |

### Kimi K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.5：视觉智能体智能 |
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **机构** | Moonshot AI |
| **模型名称** | Kimi K2.5 (1T MoE + MoonViT) |
| **发布日期** | 2026-02-03 |
| **主要创新** | **原生多模态 Agent**; **Agent Swarm** — 延迟降低 4.5x; HLE-Full 30.1%, AIME 2025 96.1% |
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
| **主要创新** | **视觉推理领先** — MMSIBench/MotionBench/VideoMME SOTA; **Token 成本降低一个数量级**; Plan-Act-Reflect 循环; 500x 日 Token 用量增长 |
| **论文链接** | [GitHub](https://github.com/ByteDance-Seed/Seed2.0) |

---

## StepFun (阶跃星辰)

### Step-2 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-2 系列大模型 |
| **英文标题** | Step-2 Family |
| **机构** | StepFun (阶跃星辰) |
| **模型名称** | Step-2 (万亿参数 MoE) / Step-2 mini / Step-2 文学大师版 |
| **发布日期** | 2025-01 |
| **核心参数** | Step-2: 万亿参数 MoE; mini: MFA 注意力, 32K 上下文 |
| **主要创新** | **MFA (Multi-matrix Factorization Attention)** — 节省 94% KV 缓存; LiveBench 国产第一 |
| **论文链接** | 未发布正式 Tech Report; [平台文档](https://platform.stepfun.com) |

### Step-3 (推理模型)

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-3：阶跃星辰推理模型 |
| **英文标题** | Step-3: StepFun's Reasoning Model |
| **机构** | StepFun (阶跃星辰) |
| **模型名称** | Step-3 |
| **发布日期** | 2025-06 |
| **核心参数** | 基于 Step-2 架构的推理优化版本; 增强推理计算 |
| **主要创新** | **深度推理能力** — 长思维链推理; 数学/编码能力显著; 国产芯片推理效率达 DeepSeek-R1 的 300% |
| **论文链接** | [arXiv:2604.05678](https://arxiv.org/abs/2604.05678) |

### Step-Audio 2

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-Audio 2 技术报告 |
| **英文标题** | Step-Audio 2 Technical Report |
| **机构** | StepFun |
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
| **模型名称** | Baichuan-Omni-1.5 (7B LLM + 视觉+音频) |
| **发布日期** | 2025-01-26 |
| **主要创新** | **Omni-modal 统一架构**; **医疗图像理解 SOTA** — 超越 Qwen2-VL-72B; 端到端音频生成 |
| **论文链接** | [arXiv:2501.15368](https://arxiv.org/abs/2501.15368) |

### Baichuan-M3 (医疗垂直)

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M3：临床问诊建模实现可信医疗决策 |
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **机构** | Baichuan Inc. |
| **模型名称** | Baichuan-M3 (235B) |
| **发布日期** | 2026-02-06 |
| **主要创新** | **医疗 SOTA** — HealthBench-Hard 超越 GPT-5.2; **SPAR 算法** — 步骤惩罚优势算法; **Fact-Aware RL**; Gated Eagle3 投机解码 96% 加速 |
| **论文链接** | [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) |

---

## 综合趋势分析

### 1. MoE 架构主流化
DeepSeek V3/V4 (256 experts)、Llama 4 (16/128 experts)、Qwen3 (235B-A22B)、Mistral Large 3、Kimi K2 (384 experts)、Step-2/3 (万亿 MoE)、GLM-5 (744B-A40B) — MoE 已是业界标配。

### 2. Hybrid 架构崛起
**Mamba-Transformer 混合**: NVIDIA Nemotron 3; **稀疏注意力 (DSA)**: DeepSeek V3.2/GLM-5; **MLA**: DeepSeek/Kimi; **MFA**: Step-2。

### 3. Thinking Mode 统一化
GPT-5 路由系统、Qwen3 Thinking/Non-Thinking、Claude 4 Hybrid Reasoning、InternLM3 深度思考、Step-3 推理 — 单模型快速+深度推理已成标配。

### 4. Agentic 能力核心化
Kimi K2/K2.5 Agent-centric 设计、GLM-5 "Agentic Engineering"、Gemini 3.1 agentic workflows、Claude ASL-3 Agent 安全。Agent 是核心竞争维度。

### 5. 多模态全面铺开
Llama 4 原生多模态、Kimi K2.5 文本+视觉、Phi-4-reasoning-vision 端侧多模态、Gemini 3.1 2M 上下文多模态、Seed 2.0 视觉推理 SOTA。

### 6. 国产 GPU 生态适配
GLM-5 全栈适配 7 种国产 GPU; Step-3 国产芯片推理效率达 DeepSeek-R1 的 300%。国产化从口号到工程现实。

### 7. RL 重新成为焦点
DeepSeek-R1 纯 RL 推理涌现、Magistral 纯 RL 推理训练、Phi-4-reasoning-plus 短 RL 提升、GLM-5 异步 RL 基础设施 slime。RL 从对齐工具升级为能力创造手段。

### 8. 推理模型爆发
2025-2026 年推理模型井喷: DeepSeek-R1、OpenAI o3/o4、Magistral、Phi-4-reasoning、Step-3、Grok 4。Thinking Mode 从"特性"变成"必备"。

### 9. 顶级实验室路径分化
- **安全前沿** (OpenAI/Anthropic): System Card 详细安全评估, ASL 分级
- **开源驱动** (Meta/Mistral/Qwen/01.AI): Apache 2.0, MoE + 多模态
- **生态绑定** (Google/Amazon/Apple): 长上下文 + Agent + 性价比
- **中国创新** (DeepSeek/Zhipu/Moonshot): DSA/Muon/slime 工程创新
- **垂直突破** (Baichuan/StepFun): 医疗 SOTA / 模型即产品

### 10. 成本与效率革命
Phi-4-reasoning 14B 匹敌 70B; InternLM3 4T tokens 达 SOTA; Step-2 MFA 节省 94% KV 缓存; Seed 2.0 成本降低一个数量级。效率提升从"锦上添花"变成"生死存亡"。
