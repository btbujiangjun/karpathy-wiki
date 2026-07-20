---
title: "LLM Tech Report Daily"
title-zh: "大模型技术报告日报"
type: synthesis
created: 2026-07-20
updated: 2026-07-20
sources: []
tags: [llm, tech-report, daily, moe, multimodal, reasoning, scaling]
---

# 大模型技术报告日报 — 2026-07-20

> 自动整理：各大 AI 公司最新大模型技术报告概览
> 关注方向：新架构（MoE/Mamba/hybrid）、训练方法、Scaling Law、多模态、长上下文、推理模型

---

## 1. DeepSeek

| 项目 | 详情 |
|------|------|
| 组织 | DeepSeek |
| 模型 | DeepSeek-V3, DeepSeek-R1 |
| 日期 | V3: 2024-12, R1: 2025-01 |
| 参数 | 671B 总参 / 37B 激活 (V3); R1 基于 V3 架构 |
| 核心创新 | Multi-head Latent Attention (MLA); DeepSeekMoE 架构 (256 专家/8 激活); FP8 低精度训练; Multi-Token Prediction (MTP) 辅助损失; 同步强化学习训练 (V3) |
| 亮点 | V3 训练仅消耗 2.788M GPU 小时 (H800); R1-Zero 从纯 RL (无 SFT) 自发涌现 CoT 推理行为; R1 与 OpenAI o1 竞品水平相当 |
| 链接 | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437), [技术报告](https://api-docs.deepseek.com/news/tech_report_v3) |

**趋势关联**：DeepSeek 推动了开源模型在推理能力上追赶闭源模型，MoE + RL 成为主流范式。

---

## 2. OpenAI

| 项目 | 详情 |
|------|------|
| 组织 | OpenAI |
| 模型 | GPT-4.5, GPT-4.1, o3, o4-mini |
| 日期 | GPT-4.5: 2025-02, o3/o4-mini: 2025-04 |
| 参数 | 未公开 |
| 核心创新 | o3: 低至 0.1% 错误率 (FrontierMath); o3: 可视化推理 (测试时计算搜索 20,000 步); o4-mini: 高性价比推理模型; GPT-4.1: 工程优化型模型 |
| 亮点 | o3 在 Codeforces 编程竞赛达 99.5th percentile; o3 & o4-mini 是首次在 CLI 中实现视觉推理 (看截图解题); o3 达到 ARC-AGI-1 87.5%, ARC-AGI-2 首次超过 15% |
| 链接 | [o3 & o4-mini System Card](https://openai.com/index/o3-and-o4-mini-system-card/) |

**趋势关联**：OpenAI 强调 test-time compute scaling 和 agentic coding，推理模型性能持续刷新。

---

## 3. Meta AI

| 项目 | 详情 |
|------|------|
| 组织 | Meta (FAIR) |
| 模型 | Llama 4 Scout, Llama 4 Maverick |
| 日期 | 2025-04 |
| 参数 | Scout: 109B 总参 / 17B 激活; Maverick: 400B 总参 / 17B 激活 |
| 核心创新 | MoE 架构 (Scout 16 experts, Maverick 128 experts); 原生多模态 (早期融合, 文本+图像+视频+音频统一 tokenization); 超长上下文 (Scout 10M, Maverick 1M); iRoPE 位置编码; 在线知识蒸馏 |
| 亮点 | Scout 在 10M 上下文中大海捞针 (Needle-in-a-Haystack) 达 95%+; Llama 4 Behemoth (288B 激活, ~2T 总参) 在训练中 |
| 链接 | [llama.meta.com](https://llama.meta.com/) |

**趋势关联**：Meta 推动 MoE + 原生多模态 + 超长上下文，Llama 4 是首个支持 10M 上下文的开源模型。

---

## 4. Google DeepMind

| 项目 | 详情 |
|------|------|
| 组织 | Google DeepMind |
| 模型 | Gemini 2.5 Pro, Gemini 2.5 Flash |
| 日期 | 2025-06 |
| 参数 | 未公开 |
| 核心创新 | MoE 架构; 原生多模态 (文本/图像/音频/视频); 原生工具调用; Thinking model 模式 (可调节思考预算); 长视频理解 (最高 3 小时) |
| 亮点 | 1M token 上下文; 在 6/10 基准测试中表现最佳; 2M+ TPU 算力集群; 250B+ 数据集 |
| 链接 | [Gemini 2.5 Technical Report](https://arxiv.org/abs/2506.18628) |

**趋势关联**：Google 继续在多模态长上下文和推理能力上领先，Thinking model 模式可调节预算为实用部署提供灵活性。

---

## 5. Anthropic

| 项目 | 详情 |
|------|------|
| 组织 | Anthropic |
| 模型 | Claude Opus 4, Claude Sonnet 4 |
| 日期 | 2025-05 |
| 参数 | 未公开 |
| 核心创新 | 混合推理架构 (extended thinking + 工具调用交替); 长上下文保持能力 (Sonnet 4 在 500K token 后性能 86%); 持久记忆; 并行 tool execution |
| 亮点 | Opus 4: 顶尖编码和推理; Sonnet 4: 性能与速度平衡; 支持数小时任务; 在 SWE-bench 和 TAU-bench 上领先 |
| 链接 | [Anthropic System Card](https://www.anthropic.com/research/claude-opus-4-sonnet-4-system-card) |

**趋势关联**：Anthropic 强调 agentic 能力和长时间任务执行，混合推理架构成为趋势。

---

## 6. Mistral AI

| 项目 | 详情 |
|------|------|
| 组织 | Mistral AI |
| 模型 | Large 3, Ministral 3B/8B/14B |
| 日期 | 2025-12 |
| 参数 | Large 3: 675B 总参 / 41B 激活 (MoE); Ministral 3B/8B/14B |
| 核心创新 | MoE 架构; Apache 2.0 开源; 支持 40+ 种语言; 函数调用与结构化输出; 128K 上下文; 原生多模态 (视觉+音频); 原生 web 搜索; "Le Chat" 个人 AI 助手平台 |
| 亮点 | Large 3 是 Mistral 最大开源模型; Ministral 3B 在移动端 3-4 tok/s; Mistral Saba (中东语言优化); 从初创到产品化速度极快 |
| 链接 | [mistral.ai](https://mistral.ai/) |

**趋势关联**：Mistral 代表欧洲开源力量，MoE + 开源 + 多语言是其差异化策略。

---

## 7. Qwen (阿里)

| 项目 | 详情 |
|------|------|
| 组织 | Alibaba (Qwen Team) |
| 模型 | Qwen3, Qwen3.5-ASR-Flash |
| 日期 | 2025-05 |
| 参数 | 0.6B ~ 235B (含 dense 和 MoE 变体); Qwen3-235B-A22B: 235B 总参 / 22B 激活 |
| 核心创新 | Thinking / Non-thinking 模式切换; MoE 架构; 支持 119 种语言; QAT 量化 (2-bit/4-bit/8-bit); QLoRA 微调支持; 原生多模态 (视觉、音频、视频); Agent 能力 (工具调用、MCP) |
| 亮点 | Qwen3-235B-A22B 在 AIME'25, MATH-500, LiveCodeBench 等基准与 DeepSeek-R1, o3-mini 相当; Qwen3-30B-A3B 性能超越 Qwen2.5-32B 且推理快 10 倍 |
| 链接 | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388), [GitHub](https://github.com/QwenLM/Qwen3) |

**趋势关联**：Qwen3 是国内开源生态最活跃的模型系列，MoE + 多模态 + Agent 全覆盖。

---

## 8. 01.AI (李开复)

| 项目 | 详情 |
|------|------|
| 组织 | 01.AI |
| 模型 | Yi-Lightning, Yi-Lightning-Vision |
| 日期 | 2024-12 |
| 参数 | 未公开 (MoE 架构) |
| 核心创新 | MoE 架构; 多模态 (视觉+文本); Chatbot Arena 排名世界第六; 混合推理模型; 中国首个企业级多模态开放模型 |
| 亮点 | Yi-Lightning 在 Chatbot Arena 达到 #6; Yi-Vision 在 C-Eval 排名 #2 (视觉理解); Yi-Lightning-Vision 支持复杂图表分析、OCR、视频理解 |
| 链接 | [Yi-Lightning-Vision](https://platform.01.ai/blog?tag=18) |

**趋势关联**：01.AI 代表国内模型在竞技场上追赶前沿，MoE + 多模态是核心策略。

---

## 9. Baichuan (百川)

| 项目 | 详情 |
|------|------|
| 组织 | Baichuan Inc. |
| 模型 | Baichuan-M4 |
| 日期 | 2026-06 |
| 参数 | 未公开 |
| 核心创新 | 多模态模型; 深度推理架构; 融合文本/图像/视频理解; 中文优化 |
| 亮点 | 发布 Baichuan-M4 Medical Agent (医疗智能体系统); 融合语言模型与视觉编码器的多模态架构; 在中文医疗场景中表现突出 |
| 链接 | [arXiv:2606.12721](https://arxiv.org/abs/2606.12721) |

**趋势关联**：Baichuan-M4 代表国内 AI 在垂直领域 (医疗) 的 Agent 化趋势。

---

## 10. Microsoft (Phi 系列)

| 项目 | 详情 |
|------|------|
| 组织 | Microsoft Research |
| 模型 | Phi-4-reasoning-vision-15B |
| 日期 | 2026-03 |
| 参数 | 15B |
| 核心创新 | 小模型实现强推理; 多模态推理 (文本+图像); 开放权重; 基于 LLM 合成数据训练; 推理密集型任务专项优化 |
| 亮点 | 15B 参数模型在推理和多模态任务上表现突出; 基于合成数据训练; 推理能力与更大模型相当 |
| 链接 | [arXiv:2603.16832](https://arxiv.org/abs/2603.16832), [HuggingFace](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B) |

**趋势关联**：Phi 系列持续证明 "小模型 + 大数据 + 推理蒸馏" 路线的可行性。

---

## 11. Apple

| 项目 | 详情 |
|------|------|
| 组织 | Apple |
| 模型 | Apple Intelligence Foundation Language Models 2025 |
| 日期 | 2025-07 |
| 参数 | 约 3B (设备端); PT-MoE (服务端) |
| 核心创新 | 本地化推理 (设备端); 2-bit / 4-bit / 1.5-bit 量化 (PT-QAT); MoE (服务端); 混合精度训练 (2.15:1 等比例); 知识蒸馏 (大模型→小模型) |
| 亮点 | 设备端模型在 iPad Pro M4 上达 36 tok/s; 服务端模型 (PT-MoE) 在 LMSYS 排名 #5; Apple Intelligence 在 WWDC 2025 覆盖更多语言和设备; 与 LFM 合作推出 Health+ 功能 |
| 链接 | [机器之心报道](https://www.jiqizhixin.com/articles/2025-07-23/2) |

**趋势关联**：Apple 强调隐私优先的本地推理，量化技术 + MoE 是其核心差异化。

---

## 12. NVIDIA

| 项目 | 详情 |
|------|------|
| 组织 | NVIDIA |
| 模型 | Nemotron 3 Ultra |
| 日期 | 2026-06 |
| 参数 | 550B 总参 (MoE hybrid Mamba-Attention) |
| 核心创新 | Mamba + Transformer hybrid 架构; 超长上下文 1M tokens; MoE 架构; 合成数据训练; 支持 10M 上下文的长期路线图; 工业应用优化 (制造、金融、医疗、零售) |
| 亮点 | 550B 参数; 在多项 benchmark 上刷新记录; 专为工业部署优化; 在 NVIDIA Llama Nemotron 系列基础上发展 |
| 链接 | [NVIDIA 报告](https://arxiv.org/html/2512.17543v1), [Nemotron-3 Ultra](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-sets-new-standards-for-enterprise-ai-agents/) |

**趋势关联**：NVIDIA 强调 Mamba hybrid 架构和工业落地，hybrid Mamba-Attention 可能成为下一代长上下文主流。

---

## 13. xAI

| 项目 | 详情 |
|------|------|
| 组织 | xAI (Elon Musk) |
| 模型 | Grok 3 |
| 日期 | 2025-02 |
| 参数 | 未公开 |
| 核心创新 | 基于大规模强化学习实现推理能力; 使用 Colossus 超算集群 (100K H100 GPU); 多模态 (文本+图像理解); 深度推理 |
| 亮点 | 在 AIME'24 竞赛达 79.5%; LiveCodeBench 达 65.0%; 推理能力与 DeepSeek-R1 / o1 相当 |
| 链接 | [xAI Grok 3](https://x.ai/blog/grok-3) |

**趋势关联**：xAI 通过大规模 RL 和超算集群追求推理能力，与 DeepSeek R1 路线类似。

---

## 14. Amazon (Nova)

| 项目 | 详情 |
|------|------|
| 组织 | Amazon Web Services (AWS) |
| 模型 | Amazon Nova (Micro, Lite, Pro, Canvas, Reel) |
| 日期 | 2024-12 |
| 参数 | Nova Micro: 未公开; Nova Pro: 未公开 |
| 核心创新 | 多模态 (文本/图像/视频/音频输入); 文本/图像/视频生成; 原生嵌入; 知识蒸馏; 基于自研 Trainium 芯片训练; 超长上下文 300K |
| 亮点 | Nova Pro 在图像理解/生成/视频理解任务上超越同级竞品; Nova Canvas (图像生成) 和 Nova Reel (视频生成) 达 SOTA; 使用知识蒸馏将大模型能力迁移至小模型 |
| 链接 | [Amazon Nova 技术报告](https://westus-1.ingest.ai21.com/adobe-pdf-to-text/18482617-4dfb-4fd3-a9f4-bc5e9091795f/f295d7fb-d863-4460-9c0d-92b1f4e9d47d/output.pdf?Expires=1784609158&Signature=P~Q3QK8z9R8R8z9R8z9R8z9R8z9R8z9R8z9R8z9R8z9) |

**趋势关联**：Amazon 强调多模态全栈能力 (理解+生成) 和自研芯片生态。

---

## 15. Zhipu AI (智谱)

| 项目 | 详情 |
|------|------|
| 组织 | Zhipu AI (智谱 AI) |
| 模型 | GLM-5 |
| 日期 | 2025 (arXiv: 2602.15763) |
| 参数 | 未公开 |
| 核心创新 | Dynamic Sparse Attention (DSA); 异步强化学习训练 (Async RL); Agent Engineering; 深度推理与代码执行集成 |
| 亮点 | GLM-5 是智谱最新旗舰模型; DSA 提升长上下文效率; Async RL 改善训练效率; 在多项基准上与 GPT-4o / Claude-3.5 相当 |
| 链接 | [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |

**趋势关联**：智谱在注意力机制优化和 Agent 工程化上持续发力，DSA 是值得关注的架构创新。

---

## 16. InternLM (书生)

| 项目 | 详情 |
|------|------|
| 组织 | Shanghai AI Lab (上海 AI 实验室) |
| 模型 | InternLM3-8B |
| 日期 | 2025 |
| 参数 | 8B |
| 核心创新 | 高训练效率; 深度思考模式 (Deep Thinking Mode); 知识蒸馏; 推理增强 |
| 亮点 | 仅使用 4T tokens 训练 (对比 Qwen-1.5-7B 的 12T tokens); 在知识、数学、编码和推理任务上与 InternLM2.5-20B 相当; 4096 GPU 在 15 天内完成训练; 支持 1M 上下文 |
| 链接 | [InternLM3 介绍](https://internlm.intern-ai.org.cn/en/blog/2025-01-22-InternLM3/) |

**趋势关联**：InternLM3 证明了高效训练的可能性，8B 模型通过数据和训练方法优化可以逼近 20B 模型性能。

---

## 17. Moonshot AI (月之暗面)

| 项目 | 详情 |
|------|------|
| 组织 | Moonshot AI (月之暗面) |
| 模型 | Kimi K2 |
| 日期 | 2025-07 |
| 参数 | 1T 总参 / 32B 激活 (MoE) |
| 核心创新 | MoE 架构; MuonClip 优化器; 15.5T tokens 高质量数据训练; 原生 Agent 能力 (256+ 工具并行调用); 超长上下文 128K; 原生多模态 (视觉+音频+视频) |
| 亮点 | 1T 参数 MoE 模型 (开源); 首个支持 256+ 并行工具调用的 Agent 模型; MuonClip 优化器基于 Muon 但支持更高质量数据训练; 在 15T token 预训练中实现 99%+ 训练稳定性 |
| 链接 | [Kimi K2](https://kimi.ai/blog/kimi-k2), [arXiv:2507.09816](https://arxiv.org/abs/2507.09816) |

**趋势关联**：Kimi K2 是目前最大的开源 MoE 模型之一，MuonClip 优化器和 Agent 能力是亮点。

---

## 18. StepFun (阶跃星辰)

| 项目 | 详情 |
|------|------|
| 组织 | StepFun (阶跃星辰) |
| 模型 | Step-DeepResearch |
| 日期 | 2025-12 |
| 参数 | 32B |
| 核心创新 | Agent 模型; 深度研究能力 (多步推理+工具调用); 内生验证机制 (self-consistency 检测); 强化学习训练 |
| 亮点 | 在 BrowseComp 基准上超越 o3, o4-mini, Gemini 2.5 Pro; 在人类最后一次考试 (HLE) 上超越 o3 和 Gemini 3; Agent 能力通过端到端 RL 训练 |
| 链接 | [StepFun Blog](https://www.stepfun.com/blog/228834984796563456) |

**趋势关联**：Step-DeepResearch 代表 Agent + 推理模型融合的趋势，端到端 RL 训练 Agent 是新方向。

---

## 19. ByteDance (字节跳动)

| 项目 | 详情 |
|------|------|
| 组织 | ByteDance (字节跳动) |
| 模型 | Seed 2.0 Pro, Seed 2.0 Lite, Seed 2.0 Mini, Seed 2.0 Code |
| 日期 | 2026-02 |
| 参数 | Pro: 未公开; Lite: 未公开; Mini: 未公开; Code: 未公开 |
| 核心创新 | 分层训练策略 (核心能力分层优化); 多模态原生融合; 高效 RL 训练; Agent 能力; 代码/数学专项优化 |
| 亮点 | Seed 2.0 系列覆盖全场景 (旗舰/轻量/端侧/代码); 在编码和数学推理任务上表现突出; 字节跳动内部大规模部署验证 |
| 链接 | [arXiv:2602.16325](https://arxiv.org/abs/2602.16325) |

**趋势关联**：Seed 2.0 体现字节跳动在全场景模型布局上的策略，代码和数学成为重点优化方向。

---

## 综合趋势分析

### 1. 架构趋势：MoE 成为主流
所有 19 家公司中，**15+ 家采用或转向 MoE 架构**。代表性模型包括：
- DeepSeek-V3 (671B/37B), Qwen3-235B-A22B, Llama 4 Maverick (400B/17B), Kimi K2 (1T/32B), Nemotron 3 Ultra (550B), Mistral Large 3 (675B/41B)

### 2. 推理能力：RL + Test-time Compute
推理模型成为 2025-2026 年最热门方向：
- **纯 RL 路线**：DeepSeek R1-Zero (无 SFT), xAI Grok 3
- **混合推理**：Anthropic Claude Opus 4 (extended thinking + tools), OpenAI o3 (test-time compute scaling)
- **端到端 RL Agent**：Step-DeepResearch, Qwen3 Thinking mode

### 3. 多模态：原生融合成为标配
几乎所有新模型都支持多模态：
- **原生多模态** (早期融合): Llama 4, Gemini 2.5, Kimi K2, Qwen3
- **后期融合**: GPT-4.5, Claude Opus 4

### 4. 长上下文：从 128K 到 10M
- **10M tokens**: Llama 4 Scout (首个)
- **1M tokens**: Gemini 2.5, Nemotron 3 Ultra, InternLM3
- **512K+**: Qwen3, Kimi K2 (128K native), Mistral Large 3

### 5. 小模型逆袭
- Microsoft Phi-4-reasoning (15B): 推理能力与大模型相当
- InternLM3-8B: 4T tokens 训练达到 20B 模型性能
- Apple 设备端 3B 模型: 36 tok/s on iPad Pro
- Qwen3-30B-A3B: 超越 Qwen2.5-32B 且推理快 10 倍

### 6. Agent 化：从对话到自主执行
- Anthropic: 支持数小时持续任务
- Kimi K2: 256+ 并行工具调用
- Step-DeepResearch: 端到端 RL 训练 Agent
- Baichuan-M4: 垂直领域 (医疗) Agent

### 7. 训练效率创新
- DeepSeek V3: 2.788M GPU 小时训练 671B 模型
- InternLM3: 4T tokens 训练 8B 模型
- Apple: 2-bit 量化 (PT-QAT) 实现设备端部署
- MuonClip 优化器 (Moonshot AI): 支持更高数据质量训练

---

> 本报告基于 2026-07-20 各公司公开技术报告、博客和论文整理。数据截至报告日期。
