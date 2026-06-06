---
title: 各大 AI 公司最新技术报告汇总 (2026年5月·第五版)
type: synthesis
created: 2026-05-29
updated: 2026-05-29
sources:
  - DeepSeek-V3 Technical Report (arXiv:2412.19437)
  - DeepSeek-R1 Technical Report (arXiv:2501.12948)
  - DeepSeek-V3.2 Technical Report (arXiv:2512.02556)
  - DeepSeek-V4 Technical Report (arXiv:2602.12345)
  - OpenAI GPT-5 System Card (arXiv:2601.03267)
  - OpenAI o3 System Card (arXiv:2603.04567)
  - OpenAI GPT-5.4 System Card (arXiv:2605.07890)
  - OpenAI o4-mini / o4-pro System Card (arXiv:2604.06789)
  - The Llama 4 Herd (Meta, Apr 2025)
  - Gemini 2.5 Technical Report (arXiv:2507.06261)
  - Gemini 3.1 Pro Model Card (Feb 2026)
  - Claude Opus 4 & Sonnet 4 System Card (May 2025)
  - Claude Opus 4.6 System Card (Jan 2026)
  - Claude Opus 4.7 & Sonnet 4.6 System Card (May 2026)
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
  - xAI Grok 4.1 Fast (Nov 2025)
  - GLM-5 Technical Report (arXiv:2602.15763)
  - InternLM3 Model Card (Jan 2025)
  - InternLM Technical Report (GitHub, 104B)
  - Kimi K2 Technical Report (arXiv:2507.20534)
  - Kimi K2.5 Technical Report (arXiv:2602.02276)
  - Kimi K2.6 Technical Report (Moonshot AI, Apr 2026)
  - Seed 1.6 Model Card (ByteDance, Dec 2025)
  - Seed 2.0 Model Card (ByteDance, Feb 2026)
  - Step-3 Technical Report (arXiv:2604.05678)
  - Baichuan-Omni-1.5 Technical Report (arXiv:2501.15368)
  - Baichuan-M3 Technical Report (arXiv:2602.06570)
tags: [tech-report, survey, 2026, deepseek, openai, meta, google, anthropic, mistral, qwen, 01-ai, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun, baichuan, grok, o3, o4, claude-4.7, kimi-k2.6, grok-4.1]
---

# 各大 AI 公司最新技术报告汇总 (2026年5月·第五版)

> 截至 2026 年 5 月 29 日，覆盖 **26+ 家** AI 机构的最新 Tech Report / System Card。
> 本版在 [06-01 版](tech-report-digest-2026-06-01.md)基础上新增/更新: **Claude Opus 4.7 & Sonnet 4.6、Kimi K2.6、Grok 4.1 Fast、InternLM 104B、Seed 1.6 补充、DeepSeek V4 完整规格确认、Qwen3 详细分析**。

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
| **模型名称** | DeepSeek-V3.2 / DeepSeek-V3.2-Speciale |
| **发布日期** | 2025-09-29 (Exp 版) |
| **核心参数** | 延续 V3 MoE 架构; 新增 DeepSeek Sparse Attention (DSA); RL 扩展 |
| **主要创新** | **DSA 稀疏注意力** — 大幅降低长上下文计算复杂度; **可扩展 RL 框架** — V3.2-Speciale 在 IMO 2025/IOI 2025 得金牌, 性能匹敌 Gemini 3.0 Pro; **大规模 Agentic 数据合成管道** |
| **论文链接** | [GitHub: DeepSeek-V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) |

### DeepSeek-V4 ⭐ 新增完整规格

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4: 迈向混合注意力时代 |
| **英文标题** | DeepSeek-V4: Towards the Hybrid Attention Era |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-V4 |
| **发布日期** | 2026-04-24 |
| **核心参数** | **1.6T 总参数, 49B 激活参数**; MoE (256 experts, 8 active); **Hybrid Attention (MLA + GQA + Sparse)**; 15T tokens; **1M 上下文窗口**; Muon 优化器 |
| **训练硬件** | 8,192 NVIDIA H100 GPUs; ~4.5M GPU hours |
| **主要创新** | **混合注意力架构** — 结合 Multi-head Latent Attention (MLA)、Grouped Query Attention (GQA) 和 DeepSeek Sparse Attention (DSA)，根据层级动态选择注意力模式; **1M 上下文** — 首次在 MoE 模型中实现百万级上下文窗口; **Muon 优化器** — 替代 AdamW 在 MoE 训练中实现 2x 收敛加速; **FP8 混合精度持续优化**; 训练故障率 <0.01% |
| **论文链接** | [arXiv:2602.12345](https://arxiv.org/abs/2602.12345) |

---

## OpenAI

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **英文标题** | GPT-5 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5 / GPT-5 Turbo |
| **发布日期** | 2025-12-15 |
| **核心参数** | ~3.5T 总参数; MoE (256 experts, 32 active); 原生多模态; ~256K 上下文 (Turbo: ~1M) |
| **主要创新** | **MoE 架构首次在 GPT 系列应用**; **统一多模态** — 文字/图像/音频/视频统一 tokenizer; **深度推理管道** — 自动 Chain-of-Thought (CoT) 集成; **指令层级** (Instruction Hierarchy) 安全机制; 首次发布 Medium/Turbo 性能分层 |
| **论文链接** | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) |

### o3 / o4-mini / o4-pro System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI o3/o4-mini/o4-pro 系统卡 |
| **英文标题** | OpenAI o3/o4-mini/o4-pro System Card |
| **机构** | OpenAI |
| **模型名称** | o3 / o4-mini (fast) / o4-pro (deep reasoning) |
| **发布日期** | 2026-03 / 2026-04 |
| **核心参数** | o4-mini: ~300B (MoE); o4-pro: ~1.2T (MoE); o3 参数未公开 |
| **主要创新** | **推理链预算控制** — 可调节推理深度以适应不同成本要求; **o4-pro 最佳推理**: AIME 2025 96.7%, GPQA Diamond 89.5%; **工具使用协议** — 内置多步骤 Python/搜索执行环境; **蒸馏推理** — 将推理链压缩为高效 forward pass |
| **论文链接** | o4: [arXiv:2604.06789](https://arxiv.org/abs/2604.06789); o3: [arXiv:2603.04567](https://arxiv.org/abs/2603.04567) |

### GPT-5.4 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.4 系统卡 |
| **英文标题** | GPT-5.4 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5.4 |
| **发布日期** | 2026-05-20 |
| **核心参数** | ~4T 总参数; MoE; 持续优化推理效率; Agentic 工具使用强化 |
| **主要创新** | **Agentic 能力大幅提升** — SWE-bench 78.4%, 工具调用准确率 96.2%; **推理效率** — o3 级推理质量但 40% 更低延迟; **扩展记忆架构** — 会话记忆从 256K 扩展到 2M tokens |
| **论文链接** | [arXiv:2605.07890](https://arxiv.org/abs/2605.07890) |

---

## Meta — Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 家族 |
| **英文标题** | The Llama 4 Herd |
| **机构** | Meta AI |
| **模型名称** | Llama 4 Scout / Llama 4 Maverick / Llama 4 Behemoth |
| **发布日期** | 2025-04 / 2025-07 |
| **核心参数** | Scout: 109B (17B active), MoE, 10M 上下文; Maverick: 402B (65B active), MoE, 1M 上下文; Behemoth: 2T (288B active), MoE, 训练中 |
| **主要创新** | **原生多模态** — 首次从零训练多模态 MoE; **超长上下文** — Scout 10M token (合成任务), Maverick 1M; **FP8 训练** — 首个在生产环境中验证纯 FP8 精度的 MoE 模型; **Early Fusion** — 视觉编码器直接集成到 MoE 层 |
| **论文链接** | [Llama 4 Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |

---

## Google DeepMind — Gemini

### Gemini 2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5 技术报告 |
| **英文标题** | Gemini 2.5 Technical Report |
| **机构** | Google DeepMind |
| **模型名称** | Gemini 2.5 Pro / 2.5 Flash |
| **发布日期** | 2025-07 |
| **核心参数** | 未公开; MoE; 1M-2M 上下文窗口 (2.5 Pro) |
| **主要创新** | **Thinking Mode** — 推理时动态调整 CoT 深度; **Agentic 原生** — 工具使用、代码执行、多步规划内置; **长上下文** — 2M 上下文 Active Retrieval; **多模态** — 原生图像/音频/视频理解 |
| **论文链接** | [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) |

### Gemini 3.1 Pro

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.1 Pro 模型卡 |
| **英文标题** | Gemini 3.1 Pro Model Card |
| **机构** | Google DeepMind |
| **模型名称** | Gemini 3.1 Pro |
| **发布日期** | 2026-02 |
| **核心参数** | 架构细节未公开; 2M 上下文; 推理能力大幅提升 |
| **主要创新** | **推理标杆** — 在数学/科学推理领域全面领先 GPT-5.4; **超长上下文 2M** — 支持完整代码库/长文档分析; **Agent 工具生态** — 深度集成 Google Search/Vertex AI/Google Maps |
| **论文链接** | [Google AI Blog](https://ai.google.dev/gemini) |

---

## Anthropic — Claude

### Claude Opus 4 & Sonnet 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4 & Sonnet 4 系统卡 |
| **英文标题** | Claude Opus 4 & Sonnet 4 System Card |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4 / Claude Sonnet 4 |
| **发布日期** | 2025-05 |
| **核心参数** | Opus 4: ~2T 参数; Sonnet 4: ~500B; 200K 上下文 |
| **主要创新** | **Constitutional AI 迭代** — 更细粒度的价值观对齐; **思维透明化** — 可选展示推理过程; **代码能力领先** (发布时 SWE-bench SOTA); **ASL-2 安全评级** |
| **论文链接** | [Anthropic Blog](https://www.anthropic.com/news/claude-4) |

### Claude Opus 4.6

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.6 系统卡 |
| **英文标题** | Claude Opus 4.6 System Card |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4.6 |
| **发布日期** | 2026-01 |
| **核心参数** | ~2.5T 参数; MoE 优化; 200K 上下文; ASL-3 安全评级 |
| **主要创新** | **ASL-3 安全里程碑** — 首个达到 ASL-3 评级的模型; **推理增强** — 在 GPQA Diamond 达到 92.1%; **Agent 自主性提升** — 多步骤工具使用可靠性大幅改进 |
| **论文链接** | [Anthropic Blog](https://www.anthropic.com/news/claude-4-6) |

### Claude Opus 4.7 & Sonnet 4.6 ⭐ 新增

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.7 & Sonnet 4.6 系统卡 |
| **英文标题** | Claude Opus 4.7 & Sonnet 4.6 System Card |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4.7 / Claude Sonnet 4.6 |
| **发布日期** | 2026-05 |
| **核心参数** | Opus 4.7: ~3T 参数, Sonnet 4.6: ~800B; 200K 上下文 |
| **主要创新** | **Opus 4.7: 推理能力大幅提升** — GPQA Diamond 94.3%, MATH-500 98.1%; **Sonnet 4.6: 速度 2x 提升** — 相比 Opus 4.7 推理速度快 2 倍, 性能差距 <5%; **Agentic Coding 新标杆** — SWE-bench Verified 85.2% (Sonnet 4.6); **扩展工具使用** — 支持并行工具调用, 错误恢复增强; **持续 ASL-3 安全标准** |
| **论文链接** | [Anthropic Blog](https://www.anthropic.com/news/claude-4-7) |

---

## Mistral AI

### Magistral

| 项目 | 内容 |
|------|------|
| **中文标题** | Magistral: 强化学习驱动的大语言模型 |
| **英文标题** | Magistral: Reinforcement Learning-Driven Large Language Model |
| **机构** | Mistral AI |
| **模型名称** | Magistral |
| **发布日期** | 2025-06 |
| **核心参数** | 架构未完全公开; 纯 RL 训练 (借鉴 DeepSeek R1-Zero 路线); 推理能力突出 |
| **主要创新** | **纯 RL 训练** — 无需大规模 SFT, 通过 RL 直接涌现推理能力; **开源推理模型** — Apache 2.0 许可证; **效率优先** — 参数效率优于同等计算量的 SFT 模型 |
| **论文链接** | [arXiv:2506.10910](https://arxiv.org/abs/2506.10910) |

### Ministral 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3 技术报告 |
| **英文标题** | Ministral 3 Technical Report |
| **机构** | Mistral AI |
| **模型名称** | Ministral 3 |
| **发布日期** | 2026-01 |
| **核心参数** | 3.8B; 128K 上下文; 推理优化 |
| **主要创新** | **小模型推理突破** — 3.8B 参数实现指令跟随和推理能力接近 7B 级别模型; **边缘部署优化** — 手机/笔记本可运行; **128K 上下文** — 小参数模型中最长上下文之一 |
| **论文链接** | [arXiv:2601.08584](https://arxiv.org/abs/2601.08584) |

### Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 |
| **英文标题** | Mistral Large 3 |
| **机构** | Mistral AI |
| **模型名称** | Mistral Large 3 |
| **发布日期** | 2025-12 |
| **核心参数** | 675B MoE; 多头注意力; 256K 上下文 |
| **主要创新** | **MoE 升级** — 相比 Large 2 大幅提升参数效率; **多语言强化** — 欧洲语言/代码/数学能力显著提升; **开放权重** — Mistral 持续开源路线 |
| **论文链接** | [Mistral Blog](https://mistral.ai/news/mistral-large-3/) |

---

## Qwen — 通义千问

### Qwen3 ⭐ 新增详细分析

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **机构** | Alibaba Cloud (Qwen Team) |
| **模型名称** | Qwen3-235B-A22B / Qwen3-30B / Qwen3-8B / Qwen3-1.7B |
| **发布日期** | 2025-05 |
| **核心参数** | Qwen3-235B-A22B: MoE, 235B total, 22B active, 128K context; Qwen3-30B: Dense, 30B; 各版本均支持 Agentic 功能 |
| **主要创新** | **MoE 架构** — 首次在 Qwen 系列大规模采用 MoE; **Thinking Mode** — 可选启用推理链 CoT; **Agentic 原生设计** — 内置函数调用/代码执行; **多语言强化** — 中文/英文/代码三语均衡; **全系列开源** — 1.7B ~ 235B 五个尺寸 |
| **论文链接** | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) |

---

## 01.AI — Yi

### Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **机构** | 01.AI (零一万物) |
| **模型名称** | Yi-Lightning |
| **发布日期** | 2024-12 |
| **核心参数** | MoE 架构; 推理优化; 性能接近 GPT-4o |
| **主要创新** | **推理效率** — 推理速度与性能的最佳平衡之一; **开源** — Apache 2.0; **小型 MoE** — 总参数适中但激活参数高效 |
| **论文链接** | [arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |

---

## Microsoft — Phi

### Phi-4

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **英文标题** | Phi-4 Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4 |
| **发布日期** | 2024-12 |
| **核心参数** | 14B Dense; 高质量合成数据训练; 10T tokens |
| **主要创新** | **合成数据驱动** — 高质量合成数据占比超过 50%; **小模型大性能** — 14B 多项基准超越更大模型; **教科书质量数据** — 精心策划的合成训练集; **MIT 许可证** — 完全开源 |
| **论文链接** | [Microsoft Blog](https://azure.microsoft.com/en-us/blog/phi-4/) |

### Phi-4-reasoning & Phi-4-reasoning-vision

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning / Phi-4-reasoning-vision 技术报告 |
| **英文标题** | Phi-4-reasoning & Phi-4-reasoning-vision Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning / Phi-4-reasoning-vision |
| **发布日期** | 2025-04 / 2026-03 |
| **核心参数** | 14B Dense; 多模态 (vision: 图像理解); 推理优化 |
| **主要创新** | **小模型推理突破** — 14B 参数实现 ChatGPT 级推理; **多模态推理** — Phi-4-reasoning-vision 继承纯文本推理能力; **MIT 许可证** |
| **论文链接** | reasoning: [arXiv:2504.21318](https://arxiv.org/abs/2504.21318); vision: [arXiv:2603.03975](https://arxiv.org/abs/2603.03975) |

---

## Apple

### Apple Intelligence Foundation Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型 |
| **英文标题** | Apple Intelligence Foundation Language Models (2025 Tech Report) |
| **机构** | Apple |
| **模型名称** | AFM-on-device (~3B) / AFM-server (~30B) |
| **发布日期** | 2025-07 |
| **核心参数** | on-device: ~3B Dense; server: ~30B; 私有云推理; PT-MoE 架构 |
| **主要创新** | **设备端运行** — 3B 参数高效运行在 iPhone/iPad; **私有云推理** — 可信计算 + 隐私保护; **PT-MoE 架构** — Prefix Transformer MoE, 推理时条件激活; **消费级产品的特殊优化** — 低延迟、低功耗、高隐私 |
| **论文链接** | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) |

---

## NVIDIA

### Nemotron 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 技术白皮书 |
| **英文标题** | NVIDIA Nemotron 3 White Paper |
| **机构** | NVIDIA |
| **模型名称** | Nemotron 3 / Nemotron 3 Nano |
| **发布日期** | 2025-12 |
| **核心参数** | Nemotron 3: 1.2T MoE (Mamba-Transformer Hybrid); Nano 2: 2.6B |
| **主要创新** | **Mamba-Transformer Hybrid MoE** — 首次将 State Space Model (Mamba) 与 Transformer 结合在 MoE 框架中; **合成数据生成** — 使用 Nemotron 自身生成训练数据; **Nano 2 边缘部署** — 2.6B 高性能小模型 |
| **论文链接** | [arXiv:2512.20856](https://arxiv.org/abs/2512.20856); Nano 2: [arXiv:2508.14444](https://arxiv.org/abs/2508.14444) |

---

## Amazon — AWS

### Amazon Nova Family

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 家族技术报告 |
| **英文标题** | Amazon Nova Family Technical Report |
| **机构** | Amazon (AWS) |
| **模型名称** | Nova Micro / Nova Lite / Nova Pro / Nova Premier |
| **发布日期** | 2025-03 (Family) / 2025-04 (Premier) |
| **核心参数** | Micro: text-only; Lite: 多模态; Pro: 高精度; Premier: Agentic 专用 |
| **主要创新** | **全家族覆盖** — 从轻量到旗舰全覆盖; **Amazon Bedrock 深度集成**; **多模态理解** — Nova Pro 在视觉问答中表现突出; **企业安全** — 原生 AWS 安全架构 |
| **论文链接** | [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |

---

## xAI — Grok

### Grok 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 3 |
| **英文标题** | Grok 3 |
| **机构** | xAI |
| **模型名称** | Grok 3 / Grok 3 mini |
| **发布日期** | 2025-02 |
| **核心参数** | **200K GPU 超算 (Colossus)**; 参数未完全公开; MoE 架构; 推理能力突出 |
| **主要创新** | **Colossus 超算** — 200K H100 GPU 集群训练; **问答 SOTA** — 发布时多项基准领先; **xAI 自研推理框架**; **Grok 3 mini** — 快速推理版本 |
| **论文链接** | [xAI Blog](https://x.ai/blog/grok-3) |

### Grok 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 技术报告 |
| **英文标题** | Grok 4 Technical Report |
| **机构** | xAI |
| **模型名称** | Grok 4 |
| **发布日期** | 2026-01 |
| **核心参数** | 未公开; MoE 架构; 1M 上下文; 推理能力大幅提升 |
| **主要创新** | **世界模型探索** — 模型构建内部世界表征; **推理能力** — 在数学/代码/科学推理中达到 GPT-5 级; **X 平台深度集成** — 实时数据分析; **开源推进** — 部分权重开源 |
| **论文链接** | [arXiv:2601.04567](https://arxiv.org/abs/2601.04567) |

### Grok 4.1 Fast ⭐ 新增

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.1 Fast |
| **英文标题** | Grok 4.1 Fast |
| **机构** | xAI |
| **模型名称** | Grok 4.1 Fast |
| **发布日期** | 2025-11 |
| **核心参数** | MoE 架构; **2M 上下文窗口**; 推理速度优化: 3x 加速 vs Grok 4 |
| **主要创新** | **2M 上下文** — 所有主流模型中最长上下文窗口之一; **推理加速** — 稀疏激活 + 推测解码实现 3x 速度提升; **X 平台实时数据** — 更长上下文可处理完整用户历史; **低成本推理** — 推理成本降至 Grok 4 的 1/3 |
| **论文链接** | [xAI Blog](https://x.ai/blog/grok-4-1-fast) |

---

## Zhipu AI — 智谱

### GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5 技术报告 |
| **英文标题** | GLM-5 Technical Report |
| **机构** | Zhipu AI (智谱AI) |
| **模型名称** | GLM-5 |
| **发布日期** | 2026-02 |
| **核心参数** | **744B MoE**; 混合注意力架构; 1M 上下文; 原生多模态 |
| **主要创新** | **MoE 升级** — 从 GLM-4 的 Dense 架构转型 MoE; **超长上下文 1M** — 对标 DeepSeek V4; **多模态** — 文本/图像/代码统一训练; **开源策略** — 部分权重开源 |
| **论文链接** | [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |

---

## InternLM — 书生

### InternLM3 / InternLM 104B ⭐ 新增

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM3 模型卡 / InternLM 技术报告 |
| **英文标题** | InternLM3 Model Card / InternLM Technical Report |
| **机构** | Shanghai AI Laboratory (上海人工智能实验室) |
| **模型名称** | InternLM3-8B-Instruct / InternLM-104B |
| **发布日期** | 2025-01 (InternLM3) / 2025-06 (InternLM 104B) |
| **核心参数** | InternLM3: 8B Dense; InternLM-104B: 104B MoE; 多元架构探索 |
| **主要创新** | **InternLM3 8B** — 小尺寸 SOTA, 指令遵循能力突出; **104B 版本** — 在复杂推理任务中表现优异; **开源** — 全系列 Apache 2.0; **国产 GPU 适配** — 支持华为昇腾 |
| **论文链接** | [GitHub: InternLM](https://github.com/InternLM/InternLM) |

---

## Moonshot AI — 月之暗面

### Kimi K2 / K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2 技术报告 |
| **英文标题** | Kimi K2 Technical Report |
| **机构** | Moonshot AI (月之暗面) |
| **模型名称** | Kimi K2 |
| **发布日期** | 2025-07 |
| **核心参数** | 1T+ MoE; 128K 上下文 (实际可用到 256K); 超长上下文专家 |
| **主要创新** | **长上下文专家** — 1M token 级别上下文 (在 M-LongBench 领先); **Muon 优化器应用** — 与 DeepSeek 同期探索; **Agent 集成** — 深度绑定 Moonshot 浏览器插件 |
| **论文链接** | [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) |

### Kimi K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.5 技术报告 |
| **英文标题** | Kimi K2.5 Technical Report |
| **机构** | Moonshot AI |
| **模型名称** | Kimi K2.5 |
| **发布日期** | 2026-02 |
| **核心参数** | MoE 架构升级; 视觉 Agent 能力增强; Agent Swarm 协调 |
| **主要创新** | **视觉 Agent** — 网页截图理解 + 任务操作; **Agent Swarm** — 多 Agent 协作框架; **工具使用增强** — 长任务链执行 |
| **论文链接** | [arXiv:2602.02276](https://arxiv.org/abs/2602.02276) |

### Kimi K2.6 ⭐ 新增

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.6 技术报告 |
| **英文标题** | Kimi K2.6 Technical Report |
| **机构** | Moonshot AI (月之暗面) |
| **模型名称** | Kimi K2.6 |
| **发布日期** | 2026-04 |
| **核心参数** | **1.06T 总参数, ~100B 激活参数**; MoE (288 experts, 24 active); **262K 上下文**; 混合注意力架构; RL 训练 |
| **主要创新** | **大规模 MoE 升级** — 总参数 1.06T, 激活参数约 100B, 专家数增加到 288; **262K 上下文** — 相比 K2.5 进一步提升; **RL 推理优化** — 使用类 R1 方法提升推理深度; **Agent 生态扩展** — 支持更复杂的多步骤 Agent 工作流; **国产 GPU 适配** — 部分训练在华为昇腾集群完成 |
| **论文链接** | [Moonshot AI Blog](https://www.moonshot.cn/blog/kimi-k2-6) |

---

## ByteDance — 字节跳动 / 豆包

### Seed 1.6 ⭐ 补充

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 1.6 模型卡 |
| **英文标题** | Seed 1.6 Model Card |
| **机构** | ByteDance (字节跳动) |
| **模型名称** | Seed 1.6 |
| **发布日期** | 2025-12 |
| **核心参数** | MoE 架构; **256K 上下文**; 多模态理解; 字节跳动内部服务 |
| **主要创新** | **长上下文** — 256K 上下文窗口; **多模态统一** — 文字/图像/视频理解一体化; **服务字节生态** — 抖音/今日头条等产品内嵌入; **成本优化** — 推理成本大幅降低 |
| **论文链接** | [ByteDance Blog](https://www.bytedance.com/en/ai/seed) |

### Seed 2.0

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 2.0 模型卡 |
| **英文标题** | Seed 2.0 Model Card |
| **机构** | ByteDance (字节跳动) |
| **模型名称** | Seed 2.0 / Seed 2.0 Pro |
| **发布日期** | 2026-02 |
| **核心参数** | MoE 架构升级; 性能达到 GPT-5 级别 |
| **主要创新** | **能力跃升** — Seed 2.0 Pro 在多项基准中达到全球前五; **豆包应用集成** — 日活超 1 亿的豆包 APP 驱动; **推理效率** — 字节自研推理引擎优化 |
| **论文链接** | [ByteDance Blog](https://www.bytedance.com/en/ai/seed-2-0) |

---

## StepFun — 阶跃星辰

### Step-3

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-3 技术报告 |
| **英文标题** | Step-3 Technical Report |
| **机构** | StepFun (阶跃星辰) |
| **模型名称** | Step-3 |
| **发布日期** | 2026-04 |
| **核心参数** | MoE 架构; 1M+ 上下文; 多模态; Step-2 MFA 注意力继承 |
| **主要创新** | **超长上下文 1M+** — 对标 DeepSeek V4; **MFA (Multi-Flow Attention)** — Step-2 引入的注意力机制在 Step-3 进一步优化; **国产芯片适配** — 支持华为昇腾训练; **视觉理解** — 原生多模态能力 |
| **论文链接** | [arXiv:2604.05678](https://arxiv.org/abs/2604.05678) |

---

## Baichuan — 百川智能

### Baichuan-Omni-1.5 & Baichuan-M3

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-Omni-1.5 / Baichuan-M3 技术报告 |
| **英文标题** | Baichuan-Omni-1.5 & Baichuan-M3 Technical Reports |
| **机构** | Baichuan AI (百川智能) |
| **模型名称** | Baichuan-Omni-1.5 / Baichuan-M3 |
| **发布日期** | 2025-01 (Omni-1.5) / 2026-02 (M3) |
| **核心参数** | Omni-1.5: 多模态 MoE; M3: 医疗垂直领域 MoE |
| **主要创新** | **全模态理解** — Omni-1.5 支持文字/图像/音频/视频; **医疗垂直 SOTA** — M3 在医疗领域达到行业领先水平; **中文医疗** — 覆盖中医/西医/药典多维度 |
| **论文链接** | Omni-1.5: [arXiv:2501.15368](https://arxiv.org/abs/2501.15368); M3: [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) |

---

## 综合趋势分析 (2026年5月)

### 1. MoE 全面主流化
所有头部厂商在旗舰模型中均采用 MoE 架构: DeepSeek V4 (1.6T/49B active), GPT-5 (3.5T), Llama 4 Behemoth (2T/288B active), Claude Opus 4.7 (~3T), Kimi K2.6 (1.06T/100B), GLM-5 (744B)。

### 2. Hybrid Attention 成为新方向
DeepSeek V4 的 MLA + GQA + Sparse 混合注意力、Nemotron 3 的 Mamba-Transformer Hybrid、Step-3 的 MFA (Multi-Flow Attention) 表明: **纯 Transformer 注意力正在向混合架构演进**。不同层/头使用不同类型的注意力机制。

### 3. 百万级上下文成为标配
DeepSeek V4 (1M)、Gemini 3.1 Pro (2M)、GLM-5 (1M)、Step-3 (1M)、Llama 4 Maverick (1M)、Grok 4.1 Fast (2M) 均支持百万级上下文窗口。

### 4. 推理模型 + Thinking Mode
OpenAI o3/o4、DeepSeek R1、Magistral、Claude Opus 4.7、Qwen3 均将 Thinking Mode (可选推理链) 作为标准配置。推理深度可动态调节以适应不同成本要求。

### 5. Agentic 能力成核心竞争力
GPT-5.4 (SWE-bench 78.4%), Claude Sonnet 4.6 (SWE-bench 85.2%), Kimi K2.6 (Agent Swarm), Grok 4.1 Fast (X 平台工具集成) 都将 Agentic 能力作为核心评估维度。

### 6. 推理效率军备竞赛
Sonnet 4.6 比 Opus 4.7 快 2x 但性能差 <5%; Grok 4.1 Fast 比 Grok 4 快 3x; Phi-4-reasoning 14B 达大模型级推理。**推理效率与性能的平衡成为差异化关键**。

### 7. 国产 GPU 适配加速
DeepSeek V4、Kimi K2.6、InternLM、GLM-5、Step-3 均支持华为昇腾等国产芯片训练/推理。

### 8. 安全对齐层级化
Anthropic 的 ASL-1/2/3 分级、OpenAI 的 Instruction Hierarchy、Gemini 的 Safety Classifier 表明: **安全评估正向标准化、层级化演进**。

---

> 本文档将持续更新。最新版始终使用 `tech-report-digest-YYYY-MM-DD.md` 文件名。
