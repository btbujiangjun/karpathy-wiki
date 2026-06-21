---
title: 全球 AI 大模型技术报告摘要 (截至 2026-06)
type: synthesis
created: 2026-06-21
updated: 2026-06-21
sources: []
tags: [tech-report, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun]
---

# 全球 AI 大模型技术报告摘要

> 截至 2026 年 6 月的各主要 AI 公司最新技术报告汇总。涵盖架构、训练方法、Scaling Law、多模态、长上下文、推理模型六大维度。

## 目录

1. [[#DeepSeek]]
2. [[#OpenAI]]
3. [[#Meta AI (LLaMA)]]
4. [[#Google DeepMind (Gemini)]]
5. [[#Anthropic (Claude)]]
6. [[#Mistral AI]]
7. [[#Qwen (Alibaba)]]
8. [[#Yi (01.AI)]]
9. [[#Baichuan]]
10. [[#Microsoft (Phi)]]
11. [[#Apple]]
12. [[#NVIDIA]]
13. [[#xAI (Grok)]]
14. [[#Amazon (Nova)]]
15. [[#Zhipu AI (GLM)]]
16. [[#InternLM (Shanghai AI Lab)]]
17. [[#Moonshot AI (Kimi)]]
18. [[#ByteDance (Doubao / Seed)]]
19. [[#StepFun (阶跃星辰)]]
20. [[#跨公司趋势总结]]

---

## DeepSeek

### DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：面向高效百万 Token 上下文智能 |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| **发布日期** | 2026 年 6 月 |
| **总参数量** | V4-Pro: 1.6T (49B activated); V4-Flash: 284B (13B activated) |
| **训练数据** | 32T+ tokens |
| **上下文长度** | 1,000,000 tokens |
| **架构** | MoE + 混合注意力 (CSA + HCA) + mHC + Muon optimizer |
| **arXiv** | https://arxiv.org/abs/2606.19348 |

**主要创新点：**
- **混合注意力架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 实现百万级高效上下文
- **Manifold-Constrained Hyper-Connections (mHC)**：改进残差连接，提升训练稳定性
- **Muon optimizer**：加速收敛并提高训练稳定性
- 百万 token 上下文下，V4-Pro 仅需 V3.2 的 27% FLOPs 和 10% KV cache
- 保留 DeepSeekMoE 框架和 Multi-Token Prediction (MTP)

### DeepSeek-V3 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3 技术报告 |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V3 |
| **发布日期** | 2024 年 12 月 |
| **总参数量** | 671B (37B activated) |
| **训练数据** | 14.8T tokens |
| **上下文长度** | 128K |
| **训练成本** | 2.788M H800 GPU hours |
| **架构** | MoE + MLA + MTP + 无辅助损失负载均衡 |
| **arXiv** | https://arxiv.org/abs/2412.19437 |

**主要创新点：**
- 开创无辅助损失（auxiliary-loss-free）负载均衡策略
- Multi-Token Prediction (MTP) 训练目标
- Multi-head Latent Attention (MLA) 高效推理
- 整个训练过程零回滚

---

## OpenAI

### GPT-5.5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.5 系统卡 |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.5 / GPT-5.5 Pro / GPT-5.5 Instant |
| **发布日期** | 2026 年 4 月 23 日 |
| **上下文长度** | 1M (API) / 400K (Codex) |
| **价格** | $5/M 输入, $30/M 输出 (标准); Pro: $30/$180 |
| **链接** | https://openai.com/index/gpt-5-5-system-card/ |

**主要创新点：**
- 改进的内部思维链推理（reasoning）能力
- 并行测试时计算（parallel test time compute）用于 Pro 版本
- 更强的工具使用、代码编写和信息检索能力
- 最强安全防护体系（Preparedness Framework 评估）
- 近乎 200 家早期合作伙伴的反馈收集
- GPT-5.5 Instant 首次被归类为"高能力"网络安全和生物化学领域

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5 (gpt-5-main, gpt-5-thinking, gpt-5-thinking-pro) |
| **发布日期** | 2025 年 8 月 (arXiv: 2026 年 1 月) |
| **架构** | 统一系统含 router（智能路由）+ thinking/main/mini 模型 |
| **arXiv** | https://arxiv.org/abs/2601.03267 |

**主要创新点：**
- 统一系统：智能路由器动态选择 thinking 或 main 模型
- 显著减少幻觉，改进指令遵循
- safe-completions 安全训练方法
- 首次在 System Card 级别公开详细安全评估

---

## Meta AI (LLaMA)

### Muse Spark Safety & Preparedness Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Muse Spark 安全与准备报告 |
| **发布机构** | Meta Superintelligence Labs (MSL) |
| **模型系列** | Muse Spark |
| **发布日期** | 2026 年 5 月 26 日 |
| **架构** | 原生多模态推理模型, 支持 tool-use, visual chain of thought, multi-agent orchestration |
| **链接** | https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ |

**主要创新点：**
- 首个 Muse 系列模型，由 MSL 开发
- 原生多模态推理 + 视觉思维链 + 多智能体编排
- 支持化学/生物、网络安全、失控风险全面评估
- "中等或更低风险"部署阈值

### The Llama 4 Herd

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 家族 |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout / Maverick / Behemoth |
| **发布日期** | 2025 年 4 月 |
| **总参数量** | Scout: 109B (17B active, 16 experts); Maverick: 400B (17B active, 128 experts); Behemoth: 2T (teacher model) |
| **上下文长度** | Scout: 10M tokens; Maverick: 1M tokens |
| **架构** | MoE + 早期融合多模态 |
| **arXiv** | https://arxiv.org/abs/2601.11659 (withdrawn, 非官方整理) |

**主要创新点：**
- 首批开源原生多模态 MoE 模型
- Scout: 10M token 上下文长度（业界最长）
- iRoPE + 长度泛化策略
- 轻量 SFT + 在线 RL + 轻量 DPO 后训练管线
- Behemoth 教师模型在 STEM 基准上超越 GPT-4.5、Claude Sonnet 3.7 和 Gemini 2.0 Pro

---

## Google DeepMind (Gemini)

### Gemini 3.5 Flash (最新)

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.5 Flash |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.5 Flash (3.5 Pro coming soon) |
| **发布日期** | 2026 年 6 月 |
| **链接** | https://deepmind.google/models/gemini/ |

**主要创新点：**
- Agentic coding 大幅领先：Terminal-bench 76.2%（vs GPT-5.5 78.2%）
- MCP Atlas 83.6% 多步骤工作流
- 新 Agentic 基准全面覆盖：OSWorld, Finance Agent, GDPval
- ARC-AGI-2 72.1%（推理能力大幅提升）

### Gemini 3.1 Pro Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.1 Pro 模型卡 |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.1 Pro / Deep Think |
| **发布日期** | 2026 年 2 月 |
| **架构** | 原生多模态推理模型 (text, audio, image, video, code) |
| **链接** | https://deepmind.google/models/model-cards/gemini-3-1-pro/ |

**主要创新点：**
- Deep Think 模式：在数学、物理、计算机科学领域解决专业研究问题
- IMO 金牌水平、ICPC 竞赛级编程能力
- 多项专业研究问题的跨学科合作
- 在 CBRN、有害操纵、ML R&D、misalignment 等维度低于警戒阈值

### Gemini 2.5 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5 技术报告 |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 Pro / Flash / 2.0 Flash-Lite |
| **发布日期** | 2025 年 6 月 |
| **上下文长度** | 最长 3 小时视频输入 |
| **链接** | https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf |

**主要创新点：**
- Thinking model 在编码和推理基准上达到 SoTA
- 多模态理解 + 长上下文 + 推理能力结合 → Agentic workflows
- 完整的 capability vs cost Pareto frontier 覆盖

### Gemini Embedding 2

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini Embedding 2：原生多模态嵌入模型 |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026 年 5 月 |
| **arXiv** | https://arxiv.org/abs/2605.27295 |

**主要创新点：**
- 统一 video/audio/image/text 嵌入空间
- 大规模对比学习 + 多任务多阶段训练
- 超越专用模型：MSCOCO R@1 62.9, MTEB Multilingual 69.9, MTEB Code 84.0

---

## Anthropic (Claude)

### Claude Opus 4.8 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.8 系统卡 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4.8 |
| **发布日期** | 2026 年 5 月 |
| **链接** | https://www.anthropic.com/system-cards |

### Claude Fable 5 & Mythos 5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5 & Mythos 5 系统卡 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Fable 5, Mythos 5 |
| **发布日期** | 2026 年 6 月 |
| **链接** | https://www.anthropic.com/system-cards |

### Claude Opus 4.7 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.7 系统卡 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4.7 |
| **发布日期** | 2026 年 4 月 |
| **架构** | Hybrid reasoning LLM |
| **主要改进** | Advanced software engineering, 最困难任务提升显著 |

### Claude Opus 4.6 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.6 系统卡 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4.6 |
| **发布日期** | 2026 年 2 月 |
| **关键发现** | SWE-bench, OSWorld-Verified, Finance 评估；ASL-3 (AI Safety Level 3) 部署 |

**主要创新点（Anthropic 全线）：**
- 首次在 Sonnet 4.6 中纳入多语言性能评估（低资源语言）
- Alignment assessment 使用激活 oracle、归因图、稀疏自编码器特征探针
- RSP (Responsible Scaling Policy) 全套灾难性风险评估
- Agentic safety evaluation：自主任务运行中的安全性测试

---

## Mistral AI

### Mistral Large 3 Technical Documentation

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 技术文档 |
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 |
| **发布日期** | 2025 年 12 月 2 日 |
| **总参数量** | 500B - 1T (15B - 50B active) |
| **架构** | Multimodal granular MoE |
| **链接** | https://legal.cms.mistral.ai/ |

### Magistral (Mistral's First Reasoning Model)

| 项目 | 内容 |
|------|------|
| **中文标题** | Magistral：Mistral 首个推理模型 |
| **发布机构** | Mistral AI |
| **模型系列** | Magistral Small / Medium |
| **发布日期** | 2026 年 |
| **训练方法** | Pure RL (RLVR framework) on Mistral Medium 3 / Small 3 |
| **arXiv** | https://arxiv.org/abs/2506.10910 |

**主要创新点：**
- 纯 RL 训练推理能力（不依赖已蒸馏的 RL traces）
- 自研 RL pipeline（ground up approach）
- RL on text 维持/改进多模态理解、指令遵循和函数调用
- 强制推理语言（reasoning language）的简单方法

### Ministral 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3 系列 |
| **发布机构** | Mistral AI |
| **模型系列** | Ministral 3B / 8B / 14B (base + instruct + reasoning variants) |
| **发布日期** | 2026 年 1 月 |
| **训练方法** | Cascade Distillation (迭代剪枝 + 继续训练 + 蒸馏) |
| **上下文长度** | 256K (推理模型 128K) |
| **arXiv** | https://arxiv.org/abs/2601.08584 |

**主要创新点：**
- Cascade Distillation：从大教师模型（Mistral Small 3.1, Medium 3）高效蒸馏
- 仅用 1-3T tokens 训练即达竞争对手水平
- 全部 Apache 2.0 开源

### Leanstral

| 项目 | 内容 |
|------|------|
| **中文标题** | Leanstral：面向 Lean 4 的开源代码 Agent |
| **发布机构** | Mistral AI |
| **发布日期** | 2026 年 3 月 16 日 |
| **架构** | 6B active parameters |
| **链接** | https://mistral.ai/news/leanstral/ |

**主要创新点：**
- 首个专注 Lean 4 证明助手的开源代码 agent
- Apache 2.0 开源
- 性价比远超 Claude 系列（$36 vs $549-$1,650）

---

## Qwen (Alibaba)

### Qwen3 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **发布机构** | Alibaba (Qwen Team) |
| **模型系列** | Qwen3 (0.6B - 235B) |
| **发布日期** | 2025 年 5 月 |
| **总参数量** | 旗舰: 235B (22B active, MoE) |
| **架构** | Dense + MoE 双架构 |
| **arXiv** | https://arxiv.org/abs/2505.09388 |

**主要创新点：**
- **Thinking + Non-thinking 统一框架**：单一模型同时支持快速回答和深度推理，无需切换模型
- **Thinking Budget 机制**：用户可自适应分配推理时计算资源
- 多语言从 29 扩至 119 种语言和方言
- 全部模型 Apache 2.0 开源

### Qwen3.5-Omni Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **发布机构** | Alibaba (Qwen Team) |
| **模型系列** | Qwen3.5-Omni Plus / Flash |
| **发布日期** | 2026 年 |
| **参数量** | 数百亿级别 |
| **上下文长度** | 256K |
| **架构** | Hybrid Attention MoE (Thinker + Talker) |
| **arXiv** | https://arxiv.org/abs/2604.15804 |

**主要创新点：**
- 超 1 亿小时音视频数据训练
- 10+ 小时音频理解，400 秒 720P 视频
- **ARIA** (Adaptive Rate Interleave Alignment)：动态对齐文本和语音单元，优化流式语音自然度
- 原生全模态 Agent 模型：感知、推理、行动（WebSearch、FunctionCall、语音输出）
- 超越 Gemini 3.1 Pro 的音频任务表现

### Qwen3-Coder-Next Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3-Coder-Next 技术报告 |
| **发布机构** | Alibaba (Qwen Team) |
| **模型系列** | Qwen3-Coder-Next |
| **发布日期** | 2026 年 |
| **总参数量** | 80B (3B active) |
| **架构** | Hybrid Attention + MoE |
| **arXiv** | https://arxiv.org/abs/2603.00729 |

**主要创新点：**
- 80B 总参/3B 激活的极致参数效率
- Agentic training：大规模可验证编码任务合成 + 环境反馈学习
- 与 DeepSeek-V3.2、GLM-4.7、Kimi-K2.5 竞争

### Qwen3-TTS Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3-TTS 技术报告 |
| **发布机构** | Alibaba (Qwen Team) |
| **模型系列** | Qwen3-TTS (0.6B / 1.7B) |
| **发布日期** | 2026 年 |
| **训练数据** | 5M+ hours 语音数据, 10 种语言 |
| **arXiv** | https://arxiv.org/abs/2601.15621 |

**主要创新点：**
- 3 秒声音克隆 + 自然语言描述控制
- 双轨 LM 架构 + 双 tokenizer 系统
- 最低 97ms 首包延迟（流式场景）

---

## Yi (01.AI)

### Yi-Lightning Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **发布机构** | 01.AI (零一万物) |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024 年 10 月 |
| **架构** | MoE + 高级 expert 分割和路由 + 优化 KV-caching |
| **训练方法** | 多阶段预训练 + SFT + RLHF |
| **arXiv** | https://arxiv.org/abs/2412.01253 |

**主要创新点：**
- Chatbot Arena 第 6 名，中文/数学/编码/Hard 类别第 2-4 名
- **RAISE** (Responsible AI Safety Engine) 四组件安全框架
- 合成数据构造和奖励建模策略
- 注意传统静态基准与动态人类偏好的差异

---

## Baichuan

### Baichuan-Omni-1.5 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-Omni-1.5 技术报告 |
| **发布机构** | Baichuan Inc. |
| **模型系列** | Baichuan-Omni-1.5 |
| **发布日期** | 2025 年 |
| **数据** | 约 500B 高质量多模态 tokens |
| **链接** | https://arxiv.org/abs/2501.15368 |

**主要创新点：**
- 全模态（omni-modal）理解 + 端到端音频生成
- 自研 Baichuan-Audio-Tokenizer（同时捕获语义和声学信息）
- 多阶段训练策略：多模态对齐 + 多任务微调
- 在多模态医疗基准上达到与 Qwen2-VL-72B 相当的水平

---

## Microsoft (Phi)

### Phi-4-reasoning-vision-15B Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-reasoning-vision |
| **发布日期** | 2026 年 3 月 4 日 |
| **总参数量** | 15B |
| **上下文长度** | 16,384 tokens |
| **训练** | 240 B200s, 4 天 |
| **架构** | Mid-fusion: Phi-4-Reasoning backbone + SigLIP-2 vision encoder |
| **arXiv** | https://arxiv.org/abs/2603.03975 |

**主要创新点：**
- **数据质量优先**：系统性过滤、纠错、合成增强
- 混合推理/非推理数据 + 显式 mode tokens：单一模型支持快速回答和思维链
- 动态分辨率视觉编码器（最高 3,600 visual tokens）
- 图像内双向注意力（intra-image bidirectional attention）提升空间推理
- 在科学/数学推理和 GUI/Computer Use 任务上表现突出
- MIT 开源协议

---

## Apple

### Apple Intelligence Foundation Language Models Tech Report 2025

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型 2025 技术报告 |
| **发布机构** | Apple |
| **模型系列** | AFM on-device (~3B) + AFM server (PT-MoE) |
| **发布日期** | 2025 年 7 月 |
| **架构** | On-device: dense; Server: Parallel-Track MoE (PT-MoE) |
| **arXiv** | https://arxiv.org/abs/2507.13575 |

**主要创新点：**
- 设备端模型：KV-cache sharing + 2-bit 量化感知训练
- Server 模型：PT-MoE (track parallelism + MoE + interleaved global-local attention)
- Apple Private Cloud Compute 平台部署
- 异步训练平台
- 支持 16 种语言

### AFM 3 (Apple Foundation Models 3rd Gen)

| 项目 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple 基础模型 |
| **发布机构** | Apple (与 Google 合作) |
| **模型系列** | AFM 3 Core (3B dense), AFM 3 Core Advanced (20B sparse), AFM 3 Cloud, ADM 3 Cloud, AFM 3 Cloud Pro |
| **发布日期** | 2026 年 6 月 |

**主要创新点：**
- AFM 3 Core Advanced：20B 参数稀疏架构，每 token 仅激活 1-4B
- 与 Google 合作定制
- 全新 Siri、Image Playground、Core AI framework
- Core AI framework 支持自定义模型和采样策略

---

## NVIDIA

### Nemotron 3 Ultra Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：开源高效 MoE 混合 Mamba-Transformer Agent 推理模型 |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Ultra / Super / Nano |
| **发布日期** | 2026 年 Q2 |
| **总参数量** | Ultra: 550B (55B active) |
| **训练数据** | 20T text tokens (15T + 5T 两阶段) |
| **上下文长度** | 1M tokens |
| **架构** | LatentMoE + Hybrid Mamba-Attention + MTP |
| **链接** | https://research.nvidia.com/labs/nemotron/ |

**主要创新点：**
- **LatentMoE**：比标准 Granular MoE 更好 accuracy/parameter 比
- **Hybrid Mamba-Attention**：显著提升推理吞吐（降低 attention 成本和 KV cache 占用）
- NVFP4 低精度预训练：稳定、高效
- Multi-Token Prediction (MTP) 加速推理（speculative decoding）
- 推理吞吐最高为竞品 5.9 倍（vs GLM-5.1）
- 专注 Agentic reasoning 的 post-training pipeline

### Nemotron-Labs-Diffusion

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron-Labs-Diffusion：三模式语言模型 |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron-Labs-Diffusion 3B / 8B / 14B |
| **发布日期** | 2026 年 5 月 |
| **架构** | Tri-mode (AR + Diffusion + Self-Speculation) |
| **预训练数据** | 1.3T tokens (AR) + 45B tokens (SFT) |

**主要创新点：**
- 统一 AR + Diffusion + 自推测解码三种模式
- Diffusion 模式单 forward pass 输出多 token，速度提升 5.9x
- 自推测模式：diffusion 草稿 + AR 验证，超越 MTP
- 最佳情况下每秒 token 数提升 76.5%

---

## xAI (Grok)

### Grok 4.3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.3 |
| **发布机构** | xAI |
| **模型系列** | Grok 4.3 |
| **发布日期** | 2026 年 6 月 15 日 |
| **上下文长度** | 1M tokens |
| **推理模式** | 始终开启 + 可配置 (none/low/medium/high) |
| **链接** | https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html |

### Grok 4.1 Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.1 模型卡 |
| **发布机构** | xAI |
| **模型系列** | Grok 4.1 (Thinking + Non-Thinking) |
| **发布日期** | 2025 年 11 月 17 日 |
| **链接** | https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf |

### Grok 4 Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 模型卡 |
| **发布机构** | xAI |
| **模型系列** | Grok 4 |
| **发布日期** | 2025 年 8 月 20 日 |
| **训练方法** | Pre-training + RL (human feedback, verifiable rewards, model grading) + SFT |
| **链接** | https://data.x.ai/2025-08-20-grok-4-model-card.pdf |

**主要创新点：**
- RMF (Risk Management Framework) 三分类评估：abuse potential, concerning propensities, dual-use capabilities
- 多信号 RL：human feedback + verifiable rewards + model grading
- 系统提示词公开（GitHub）
- 生产级 safety filtering

---

## Amazon (Nova)

### Amazon Nova 2: Multimodal Reasoning and Generation Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova 2 Lite / Pro / Omni / Sonic |
| **发布日期** | 2025 年 12 月 2 日 |
| **上下文长度** | 最长 1M tokens |
| **链接** | https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models |

**主要创新点：**
- 动态推理能力（configurable extended thinking）
- Nova 2 Omni：统一多模态，输入 text/image/video/audio，输出 text + image
- Nova 2 Sonic：语音到语音基础模型
- 全部内置 Responsible AI guardrails

### Amazon Nova Premier

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova Premier：技术报告与模型卡 |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Premier |
| **发布日期** | 2025 年 4 月 30 日 |
| **上下文长度** | 1M tokens |
| **特点** | 最强多模态模型 + 教师蒸馏模型 |

---

## Zhipu AI (GLM)

### GLM-5: From Vibe Coding to Agentic Engineering

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-5 (GLM-5-Turbo, GLM-5.1, GLM-5.2) |
| **发布日期** | 2026 年 2 月 |
| **总参数量** | 744B (40B activated) |
| **训练数据** | 28.5T tokens |
| **上下文长度** | 200K (从 4K 逐步扩展) |
| **架构** | MoE + DSA (DeepSeek Sparse Attention) |
| **arXiv** | https://arxiv.org/abs/2602.15763 |

**主要创新点：**
- **DSA (DeepSeek Sparse Attention)**：大幅降低训练和推理成本，同时保持长上下文保真度
- 异步强化学习基础设施：生成与训练解耦，大幅提高 GPU 利用率
- 异步 Agent RL 算法：从复杂长程交互中更有效学习
- 三阶段后训练：Reasoning RL → Agentic RL → General RL，配合 On-Policy Cross-Stage Distillation
- 全栈国产计算生态适配（华为昇腾、摩尔线程、海光、寒武纪等）
- 长序列部署成本降低 50%

---

## InternLM (Shanghai AI Lab)

### InternLM2 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM2 技术报告 |
| **发布机构** | Shanghai AI Lab / SenseTime / CUHK / Fudan |
| **模型系列** | InternLM2 (1.8B / 7B / 20B) |
| **发布日期** | 2024 年 3 月 |
| **训练数据** | 文本 + 代码 + 长上下文数据 |
| **上下文长度** | 32K (训练), 200K (needle-in-haystack 测试) |
| **对齐方法** | SFT + COOL RLHF (Conditional Online RLHF) |
| **arXiv** | https://arxiv.org/abs/2403.17297 |

**主要创新点：**
- COOL RLHF：解决冲突的人类偏好和 reward hacking
- 多阶段预训练：4K → 32K 上下文渐进扩展

### Intern-S1-Pro

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿参数科学多模态基础模型 |
| **发布机构** | Shanghai AI Lab |
| **模型系列** | Intern-S1-Pro |
| **发布日期** | 2026 年 |
| **总参数量** | 1 Trillion (首个万亿科学多模态模型) |
| **架构** | MoE + Expert Expansion + Grouped Routing |
| **arXiv** | https://arxiv.org/abs/2603.25040 |

**主要创新点：**
- 首个万亿参数科学多模态基础模型
- 覆盖化学、材料、生命科学、地球科学等 100+ 专业任务
- XTuner + LMDeploy 协同优化实现万亿级高效 RL 训练
- "Specializable Generalist" 范式：通用能力 + 专业深度

---

## Moonshot AI (Kimi)

### Kimi K2 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放 Agentic 智能 |
| **发布机构** | Moonshot AI |
| **模型系列** | Kimi K2 (K2-Base, K2-Instruct, K2-Thinking) |
| **发布日期** | 2025 年 7 月 |
| **总参数量** | 1T (32B active, 384 experts) |
| **训练数据** | 15.5T tokens |
| **上下文长度** | 128K |
| **架构** | MoE + MLA + MuonClip optimizer + MTP |
| **arXiv** | https://arxiv.org/abs/2507.20534 |

**主要创新点：**
- **MuonClip optimizer**：基于 Muon 添加 QK-Clip 技术解决训练不稳定，零 loss spike
- Agentic 能力突出：SWE-Bench 65.8, Tau2-Bench 66.1, ACEBench 76.5
- 大规模 agentic 数据合成管线
- 联合 RL 训练阶段（real + synthetic environment interaction）

### Kimi K2.6

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.6：原生多模态 Agentic 模型 |
| **发布机构** | Moonshot AI |
| **模型系列** | Kimi K2.6 |
| **发布日期** | 2026 年 2 月 |
| **总参数量** | 1T (32B active) |
| **上下文长度** | 256K |
| **架构** | MoE + MLA + MoonViT (400M vision encoder) |
| **链接** | https://huggingface.co/moonshotai/Kimi-K2.6 |

**主要创新点：**
- 原生多模态（text, image, video）
- 长程编码（Rust, Go, Python, frontend, DevOps）
- 300 子 Agent 并行编排，最多 4,000 步协调执行
- Interleaved Thinking + Multi-Step Tool Call
- Modified MIT License

---

## ByteDance (Doubao / Seed)

### Seed 2.0 / Doubao 2.0

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 2.0 系列 |
| **发布机构** | ByteDance (Seed Team) |
| **模型系列** | Seed 2.0 Pro / Lite / Mini / Code |
| **发布日期** | 2026 年 2 月 14 日 |
| **上下文长度** | 256K |
| **架构** | MoE |
| **链接** | https://seed.bytedance.com/en/blog/seed-2-0-official-launch |

**主要创新点：**
- 系统化增强长尾领域知识
- Agentic coding 作为核心产品方向
- 视觉推理、空间推理、长上下文理解重点提升
- 支持科学领域任务

### Doubao-1.5-pro

| 项目 | 内容 |
|------|------|
| **中文标题** | 豆包 1.5 Pro |
| **发布机构** | ByteDance (Doubao Team) |
| **模型系列** | Doubao 1.5 |
| **发布日期** | 2025 年 |
| **架构** | 高度稀疏 MoE |
| **训练方法** | 大规模 RL + 深度思考模式 |

**主要创新点：**
- 稀疏度 Scaling Law 研究确定最优稀疏比例
- 训练-推理一体化设计
- 动态参数调整：深度、宽度、专家数、激活专家数等多维度
- 异构硬件 + 混合低精度优化策略
- 深度思考模式 AIME 超越 o1-preview

---

## StepFun (阶跃星辰)

### Step 3.5 Flash

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：11B 激活参数的开源前沿模型 |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step 3.5 Flash |
| **发布日期** | 2026 年 2 月 |
| **总参数量** | 196B (11B active) |
| **上下文长度** | 256K |
| **架构** | Sparse MoE + MTP-3 + 3:1 Sliding Window Attention |
| **arXiv** | https://arxiv.org/abs/2602.10604 |

**主要创新点：**
- **3:1 SWA (Sliding Window Attention)**：每 3 个 SWA 层配 1 个 full-attention 层，降低长上下文计算开销
- 生成吞吐 100-350 tok/s
- SWE-bench Verified 74.4%, Terminal-Bench 2.0 51.0%
- 可在消费级硬件（Mac Studio M4 Max, NVIDIA DGX Spark）上运行
- Scaled RL 框架实现持续自我改进

### Step3 (Multimodal Reasoning Model)

| 项目 | 内容 |
|------|------|
| **中文标题** | Step3：经济高效的多模态智能 |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step3 (321B total / 38B active) |
| **发布日期** | 2025 年 7 月 |
| **架构** | MoE + MFA (Multi-Matrix Factorization Attention) + AFD |
| **arXiv** | https://arxiv.org/abs/2507.19427 |

**主要创新点：**
- MFA (Multi-Matrix Factorization Attention)：低秩 Query 维度 (2048)，降低计算复杂度
- AFD (Attention-FFN Disaggregation)：分离 attention 和 FFN 计算，提升解码效率
- 支持低端加速器高效推理

### Step-DeepResearch

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-DeepResearch 技术报告 |
| **发布机构** | StepFun (阶跃星辰) |
| **发布日期** | 2025 年 12 月 |
| **arXiv** | https://arxiv.org/abs/2512.20491 |
| **方法** | 四原子能力分解：规划/搜索/反思/报告生成 |

### StepFun-Prover Preview

| 项目 | 内容 |
|------|------|
| **中文标题** | StepFun-Prover Preview：边思考边验证 |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | StepFun-Prover-Preview (7B / 32B) |
| **发布日期** | 2025 年 7 月 |
| **方法** | RL + 工具集成推理 |
| **亮点** | miniF2F pass@1 70.0%（32B, 超越 DeepSeek-Prover-V2-671B） |
| **arXiv** | https://arxiv.org/abs/2507.20199 |

---

## 跨公司趋势总结

### 1. 大模型新架构
| 趋势 | 代表模型 |
|------|----------|
| **MoE 主流化** | DeepSeek-V4, Llama 4, Qwen3, Mistral Large 3, Kimi K2, GLM-5, Nemotron 3, Step 3.5 |
| **混合 Mamba-Transformer** | NVIDIA Nemotron 3 (Mamba-Attention hybrid) |
| **混合注意力机制** | DeepSeek-V4 (CSA + HCA), Step 3.5 Flash (SWA + full attention) |
| **LatentMoE** | NVIDIA Nemotron 3 (latent routing reduce compute) |
| **AR + Diffusion 统一** | NVIDIA Nemotron-Labs-Diffusion |

### 2. 训练方法
| 趋势 | 代表模型 |
|------|----------|
| **纯 RL 训练推理** | Magistral (Mistral), DeepSeek-R1, StepFun-Prover |
| **异步 RL 基础设施** | GLM-5 (生成-训练解耦) |
| **多阶段后训练** | GLM-5: Reasoning RL → Agentic RL → General RL |
| **Cascade Distillation** | Ministral 3 (迭代蒸馏) |
| **RLVR (RL with Verifiable Rewards)** | Magistral, Grok 4 |
| **Muon / MuonClip 优化器** | DeepSeek-V4, Kimi K2 |

### 3. Scaling Law / 缩放分析
- DeepSeek-V4 在 32T tokens 上验证 MoE scaling
- Doubao 1.5 报告稀疏度 Scaling Law 和 MoE Scaling Law 研究
- NVIDIA LatentMoE 展示更好的 accuracy/parameter 比
- 多家公司关注 "数据质量 > 数据数量"（Ministral 3: 1-3T tokens vs 36T）

### 4. 多模态模型
| 趋势 | 代表模型 |
|------|----------|
| **原生多模态 MoE** | Llama 4, Qwen3.5-Omni, Gemini 3.x |
| **全模态统一** | Baichuan-Omni, Qwen3.5-Omni, Amazon Nova 2 Omni |
| **视觉思维链** | Muse Spark, Phi-4-reasoning-vision |
| **科学多模态** | Intern-S1-Pro (万亿参数, 100+ 科学任务) |
| **多模态嵌入统一** | Gemini Embedding 2 |

### 5. 长上下文模型
| 趋势 | 代表模型 |
|------|----------|
| **百万 token 级别** | DeepSeek-V4 (1M), Grok 4.3 (1M), Gemini 3.1 Pro, Amazon Nova (1M) |
| **千万 token 级别** | Llama 4 Scout (10M) |
| **256K 标准配置** | Qwen3.5-Omni, Step 3.5 Flash, Kimi K2.6, Seed 2.0 |
| **高效长上下文注意力** | CSA/HCA (DeepSeek), SWA (Step 3.5), iRoPE (Llama 4) |

### 6. 推理模型 / Reasoning Models
| 趋势 | 代表模型 |
|------|----------|
| **Thinking + Non-thinking 统一** | Qwen3 (单模型双模式), GPT-5 (router), Phi-4-reasoning-vision |
| **纯 RL 推理涌现** | Magistral, DeepSeek-R1 |
| **思考预算控制** | Qwen3 (thinking budget), Grok 4.3 (configurable effort) |
| **Agentic 推理** | GLM-5 (Agentic Engineering), Kimi K2 (agentic 优先), Nemotron 3 (agentic reasoning) |
| **测试时计算扩展 (Test-Time Scaling)** | GPT-5.5 Pro, Gemini Deep Think |
| **数学定理证明** | StepFun-Prover, Leanstral (Lean 4) |
| **科学推理** | Gemini Deep Think (IMO Gold, ICPC), Intern-S1-Pro |
