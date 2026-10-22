---
title: "LLM Tech Report Digest — 2026-10-22"
type: synthesis
created: 2026-10-22
updated: 2026-10-22
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, scaling-law, daily-digest]
---

# LLM Tech Report Digest — 2026-10-22

> 全球主要 AI 公司大模型技术报告速览（截至 2026-10-22）
> 覆盖 2024-12 至 2026-10 各家公开 Tech Report / System Card / White Paper
> 本次新增窗口重点：DeepSeek-V4（2026-04）、Gemini 4 Argon（2026-10）、Claude Opus 5.5（2026-09）、GPT-6 / GPT-6.1 Sol（2026-09）、Llama 5 / Muse Spark（2026-05/10）、Grok 4.7（2026-09）、Nemotron 3.5（2026-10）、AFM 3（2026-06）

---

## 1. DeepSeek — DeepSeek-AI

### 1.1 DeepSeek-V4 Technical Report
- **中文标题**: DeepSeek-V4：迈向高效百万 token 上下文智能
- **英文标题**: DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4-Pro (1.6T/49B active) / V4-Flash (284B/13B active) / V4-Pro-Max
- **发布日期**: 2026-04-26（arXiv）；模型卡 2026-04-27
- **核心参数**: Pro: 1.6T 总参数 / 49B 激活；Flash: 284B / 13B 激活；上下文 1M tokens；预训练 32T+ tokens
- **主要创新点**:
  - 混合注意力架构：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 交错配置
  - Manifold-Constrained Hyper-Connections (mHC) — 将残差映射约束到 doubly stochastic 矩阵流形（Birkhoff polytope），稳定万亿级训练
  - Muon 优化器首次应用于万亿级 MoE（Newton-Schulz 迭代正交化）
  - 1M 上下文推理 FLOPs 仅为 V3.2 的 27%，KV cache 仅 10%
  - 三种推理模式：Non-think / Think High / Think Max
  - "Sovereign AI" 硬件独立性：TileLang DSL + MXFP4 量化，适配华为 Ascend / Cambricon
  - V4-Pro-Max 在核心任务超越前代，Flash-Max 对标 GPT-5.2 / Gemini-3.0-Pro
  - MIT 许可开源
- **链接**: [arXiv:2606.19348](https://arxiv.org/abs/2606.19348)

### 1.2 DeepSeek-V3 Technical Report
- **中文标题**: DeepSeek-V3 技术报告
- **英文标题**: DeepSeek-V3 Technical Report
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V3
- **发布日期**: 2024-12
- **核心参数**: 671B 总参数 / 37B 激活参数（MoE）；预训练 14.8T tokens；上下文 128K
- **主要创新点**: MLA + DeepSeekMoE；无辅助损失负载均衡；Multi-Token Prediction；GRPO 后训练；仅 2.788M H800 GPU hours
- **链接**: [arXiv:2412.19437](https://arxiv.org/abs/2412.19437)

### 1.3 DeepSeek-R1
- **中文标题**: DeepSeek-R1：激励大语言模型推理能力
- **英文标题**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-R1 / R1-Zero
- **发布日期**: 2025-01
- **核心参数**: 多尺寸（1.5B–70B 蒸馏版）；完整版基于 V3
- **主要创新点**: R1-Zero 纯 GRPO RL 涌现推理能力；AIME'24 15.6%→71.0%；蒸馏版超越 o1-mini
- **链接**: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)

### 1.4 DeepSeek-V3.2 Technical Report
- **中文标题**: DeepSeek-V3.2：推动开放大语言模型前沿
- **英文标题**: DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V3.2 / V3.2-Speciale
- **发布日期**: 2025-12
- **主要创新点**: DeepSeek Sparse Attention (DSA)；Agentic post-training；Speciale 在 IMO/IOI 2025 达金牌水平
- **链接**: [arXiv:2512.02556](https://arxiv.org/abs/2512.02556)

> 注：DeepSeek-V4.1-Flash-1017 于 2026-10-17 发布（增量更新，无独立 arXiv 技术报告）。

---

## 2. OpenAI

### 2.1 GPT-6 Sol & GPT-6 Luna
- **中文标题**: 推出 GPT-6 Sol 与 GPT-6 Luna
- **英文标题**: Introducing GPT-6 Sol and GPT-6 Luna
- **发布机构**: OpenAI
- **模型名称**: GPT-6 Sol / GPT-6 Luna
- **发布日期**: 2026-09-22
- **核心参数**: 参数量未公开
- **主要创新点**:
  - Sol 为旗舰推理档，Luna 为轻量经济档（双模型策略延续 GPT-5 系谱）
  - 承接 GPT-5.5 的 agentic / 长周期工作能力
  - 系统卡覆盖 Preparedness Framework 完整预部署评估
- **链接**: [OpenAI 官方](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

### 2.2 GPT-6.1 Sol
- **中文标题**: GPT-6.1 Sol
- **英文标题**: GPT-6.1 Sol
- **发布机构**: OpenAI
- **模型名称**: GPT-6.1 Sol
- **发布日期**: 2026-09-29
- **主要创新点**: 在 GPT-6 Sol 基础上迭代；报道称为安全关切延期后的正式发布版本
- **链接**: [OpenAI 官方](https://openai.com/index/introducing-gpt-6-1-sol/)

### 2.3 GPT-5.5 System Card
- **中文标题**: GPT-5.5 系统卡
- **英文标题**: GPT-5.5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5.5 / GPT-5.5 Pro
- **发布日期**: 2026-04-23（04-24 更新 API safeguards）
- **核心参数**: 上下文 1.05M；参数量未公开
- **主要创新点**:
  - 面向复杂真实工作（写码/研究/文档/跨工具执行）
  - Terminal-Bench 2.0 82.7%；Expert-SWE 73.1%；GDPval 84.9%
  - Graphwalks BFS 1M f1 45.4%（较 GPT-5.4 9.4% 大幅跃升）
  - 完整 Preparedness Framework + 近 200 家早期伙伴红队
  - 迄今最强 safeguard 组合
- **链接**: [OpenAI 官方](https://openai.com/index/gpt-5-5-system-card/)

### 2.4 GPT-5 System Card
- **中文标题**: GPT-5 系统卡
- **英文标题**: GPT-5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5 (gpt-5-main / gpt-5-thinking)
- **发布日期**: 2025-08
- **主要创新点**: 统一系统 + 实时 router；Safe-Completions；幻觉率较 o3 降低 78%
- **链接**: [arXiv:2601.03267](https://arxiv.org/abs/2601.03267)

---

## 3. Anthropic — Claude

### 3.1 Claude Opus 5.5 System Card
- **中文标题**: Claude Opus 5.5 系统卡
- **英文标题**: System Card: Claude Opus 5.5
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 5.5
- **发布日期**: 2026-09-22
- **核心参数**: 参数量未公开；知识截止 2026-06
- **主要创新点**:
  - Claude 5.5 家族首个模型；多数任务达到 Fable 5.1 水平，运行成本较 Opus 5 低 40%
  - 编程、agentic、computer use、数学/科学推理、长周期专业工作全面提升
  - Terminal-Bench 4.0 66.4%（xhigh effort）；FrontierCode v1.1 54.4%
  - Artificial Analysis Intelligence Index 58（#1）
  - 三大双用途领域 safeguard：生物 (VCT / Protocols / BioMysteryBench)、网络安全、前沿 AI 开发
  - Cyber 评估全面等同或超过 Mythos 5.1；无新型攻击能力迹象
  - Fast mode 最高 2.5× 加速（$8/$40 per 1M）
- **链接**: [Anthropic CDN](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%2BOpus%2B5.5%2BSystem%2BCard.pdf)

### 3.2 Claude Fable 5.1 & Mythos 5.1 System Card
- **中文标题**: Claude Fable 5.1 与 Mythos 5.1 系统卡
- **英文标题**: System Card: Claude Fable 5.1 & Claude Mythos 5.1
- **发布机构**: Anthropic
- **模型名称**: Claude Fable 5.1 / Mythos 5.1
- **发布日期**: 2026-09-01
- **主要创新点**: 编码/知识工作/问题解决前沿推进；CB-1 能力（未达 CB-2）；Mythos 5.1 网络安全评估史上最强
- **链接**: [Anthropic CDN](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf)

### 3.3 Claude Opus 5 System Card
- **中文标题**: Claude Opus 5 系统卡
- **英文标题**: System Card: Claude Opus 5
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 5
- **发布日期**: 2026-07-24
- **主要创新点**: Adaptive thinking 默认启用；Anthropic ECI 162.1；对齐表现历史最佳（misaligned 2.3%）
- **链接**: [Anthropic CDN](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)

---

## 4. Meta AI — LLaMA / Muse

### 4.1 Muse Spark Open
- **中文标题**: Meta 首个可下载的 Muse Spark
- **英文标题**: Muse Spark Open
- **发布机构**: Meta Superintelligence Labs
- **模型名称**: Muse Spark Open (816B MoE)
- **发布日期**: 2026-10-15
- **核心参数**: 816B 总参数 / ~42B 激活（MoE）；上下文 1M tokens；文本+图像+视频+音频输入
- **主要创新点**:
  - Meta 首个可下载的 MoE 旗舰（区别于闭源 Muse Spark 消费端后端）
  - Muse Model License 许可
  - 原生四模态输入
- **链接**: [Next AI Model 追踪](https://www.nextaimodel.com/)

### 4.2 Llama 5 系列
- **中文标题**: Llama 5 与 Llama 5 Scout
- **英文标题**: Llama 5 (8B) and Llama 5 Scout (109B-A17B)
- **发布机构**: Meta AI
- **模型名称**: Llama 5 8B (dense) / Llama 5 Scout 109B-A17B (MoE)
- **发布日期**: 2026-05-01
- **核心参数**: 8B dense；Scout 109B 总参数 / 17B 激活；上下文 256K
- **主要创新点**:
  - 架构借鉴 Llama 4 Maverick，但采用更密集 router + "activation pruning"（跳过低于学习阈值的专家）
  - Scout 为首个原生多模态开源 Llama（文本 + 图像 + 音频）
  - Llama 5 Community License（700M MAU 门槛条款）
- **链接**: [LLMCheck 综述](https://llmcheck.net/blog/state-of-open-source-local-llms-may-2026/)

### 4.3 Llama 4 Scout & Maverick
- **中文标题**: Llama 4 系列（Scout 和 Maverick）
- **英文标题**: Llama 4 Scout and Maverick
- **发布机构**: Meta AI
- **模型名称**: Llama 4 Scout (16 experts) / Maverick (128 experts)
- **发布日期**: 2025-04
- **核心参数**: 17B 激活参数（稀疏 MoE）；Scout 支持 10M token 上下文
- **主要创新点**: 稀疏 MoE；iRoPE 长度泛化；原生多模态 early fusion；FP8 训练
- **链接**: [Meta AI 官方](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

### 4.4 Llama 3 Herd of Models
- **中文标题**: Llama 3 模型群
- **英文标题**: The Llama 3 Herd of Models
- **发布机构**: Meta AI
- **模型名称**: Llama 3 (8B / 70B / 405B)
- **发布日期**: 2024-07
- **核心参数**: 405B 最大稠密 Transformer；上下文 128K；支持 8 种语言
- **链接**: [arXiv:2407.21783](https://arxiv.org/abs/2407.21783)

> 注：Meta 消费端 Meta AI 后端现运行闭源 **Muse Spark 1.3**（2026-09-02 更新），非 Llama 开源族。

---

## 5. Google DeepMind — Gemini

### 5.1 Gemini 4 Argon
- **中文标题**: Gemini 4 Argon 全球发布
- **英文标题**: Gemini 4 Argon
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 4 Argon
- **发布日期**: 2026-09-30（全球发布 2026-10-13/14）
- **核心参数**: 上下文 1M tokens；参数量未公开；价格 $2/$10 per 1M
- **主要创新点**:
  - Gemini 4 家族首个旗舰；BenchLM Google 榜 #1（82.9）
  - CursorBench 52.8%（与 Opus 5.5 相当）
  - 长上下文 1M
  - 另有 cyber-permissive 变体
- **链接**: [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

### 5.2 Gemma 4 Technical Report
- **中文标题**: Gemma 4 技术报告
- **英文标题**: Gemma 4 Technical Report
- **发布机构**: Google DeepMind (Gemma Team)
- **模型名称**: Gemma 4 (E2B / E4B / 12B / 31B dense + 26B-A4B MoE)
- **发布日期**: 2026-06-19（arXiv 2607.02770）
- **核心参数**: 多尺寸多模态 dense 与 MoE；上下文 256K（E 系列 128K）
- **主要创新点**:
  - 多模态 dense + MoE 架构覆盖不同硬件
  - KV cache sharing + global 层 K=V 复用 → global KV cache footprint 降低最多 37.5%
  - Autoregressive MTP drafter 加速
  - Quantization-Aware Training（mobile int2/int4 + int8 激活）
  - Slice-Granularity Elasticity（TPU 局部故障下减少 slice 继续训练）
  - AIME 2026 no-tools 89.2 / GPQA Diamond 84.3
- **链接**: [arXiv:2607.02770](https://arxiv.org/abs/2607.02770)

### 5.3 Gemini 2.5 Technical Report
- **中文标题**: Gemini 2.5：推进前沿推理、多模态、长上下文与下一代 Agent 能力
- **英文标题**: Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 2.5 Pro / 2.5 Flash / 2.0 Flash / Flash-Lite
- **发布日期**: 2025-07
- **主要创新点**: 原生多模态 Thinking model；Deep Think 模式；Thinking budget；1M+ 上下文
- **链接**: [arXiv:2507.06261](https://arxiv.org/abs/2507.06261)

---

## 6. Microsoft — Phi

### 6.1 Phi-5 Mini
- **中文标题**: Phi-5 Mini
- **英文标题**: Phi-5 Mini
- **发布机构**: Microsoft Research
- **模型名称**: Phi-5 Mini (4B)
- **发布日期**: 2026-04-28
- **核心参数**: 4B 参数；MIT 许可；8 GB Mac 上 140 tok/s
- **主要创新点**: 4B 参数下 MMLU 82%；小模型效率标杆
- **链接**: [LLMCheck 综述](https://llmcheck.net/blog/state-of-open-source-local-llms-may-2026/)

### 6.2 Phi-4-reasoning Technical Report
- **中文标题**: Phi-4-reasoning 技术报告
- **英文标题**: Phi-4-reasoning Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4-reasoning / Phi-4-reasoning-plus (14B)
- **发布日期**: 2025-04
- **主要创新点**: "Teachable" prompts + o3-mini 长 CoT 教学；14B 超越 R1-Distill-Llama-70B
- **链接**: [arXiv:2504.21318](https://arxiv.org/abs/2504.21318)

### 6.3 Phi-4 Technical Report
- **中文标题**: Phi-4 技术报告
- **英文标题**: Phi-4 Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4 (14B)
- **发布日期**: 2024-12
- **核心参数**: 14B 稠密；9.8T tokens；16K 上下文
- **主要创新点**: 合成数据为主训练策略；Pivotal Token Search DPO；MIT 许可
- **链接**: [arXiv:2412.08905](https://arxiv.org/abs/2412.08905)

---

## 7. Mistral AI

### 7.1 Mistral Large 4
- **中文标题**: Mistral Large 4
- **英文标题**: Mistral Large 4
- **发布机构**: Mistral AI
- **模型名称**: Mistral Large 4
- **发布日期**: 2026-10-06
- **核心参数**: 参数量未公开
- **主要创新点**: Mistral 旗舰迭代；与 NVIDIA Nemotron Coalition 协同开发路线
- **链接**: [Vals AI 追踪](https://www.vals.ai/models/)

### 7.2 Mistral Small 4
- **中文标题**: Mistral Small 4：加速开放前沿模型
- **英文标题**: Mistral Small 4
- **发布机构**: Mistral AI
- **模型名称**: Mistral Small 4
- **发布日期**: 2026-03-16
- **主要创新点**: 作为 NVIDIA Nemotron Coalition 创始成员发布；开源；企业级微调/多模态能力
- **链接**: [Mistral AI Blog](https://mistral.ai/news/mistral-ai-and-nvidia-partner-to-accelerate-open-frontier-models/)

### 7.3 Magistral (Reasoning Model)
- **中文标题**: Magistral 推理模型发布
- **英文标题**: Introducing Magistral
- **发布机构**: Mistral AI
- **模型名称**: Magistral Small (24B OSS) / Magistral Medium
- **发布日期**: 2025-06
- **主要创新点**: Mistral 首个推理模型；领域特定、透明、多语言推理
- **链接**: [Mistral AI Blog](https://mistral.ai/news/magistral)

---

## 8. Alibaba — Qwen

### 8.1 Qwen3.8-Max
- **中文标题**: 阿里巴巴发布 Qwen3.8-Max
- **英文标题**: Alibaba Unveils Qwen3.8-Max
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3.8-Max
- **发布日期**: 2026-08
- **核心参数**: 2.4T 参数；上下文 1M tokens；原生多模态；$2/$6 per 1M
- **主要创新点**:
  - Text Arena #5 / Vision Arena #2
  - Intelligence Index 45.4%；Coding Index 76.2%；GPQA Diamond 92.8%；HLE 43.1%
  - 16 天自主执行真实软件工程项目
  - 联合缩放 RL 环境与计算
- **链接**: [Alibaba 官方](https://www.alibabagroup.com/en-US/document-2021044032125272064)

### 8.2 Qwen3.5-Omni Technical Report
- **中文标题**: Qwen3.5-Omni 技术报告
- **英文标题**: Qwen3.5-Omni Technical Report
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3.5-Omni (Plus / Flash)
- **发布日期**: 2026-04-17（v2 2026-04-21）
- **核心参数**: 数百 B 参数级；上下文 256K；250K 词表（较 150K 提升 10–60% 编解码效率）
- **主要创新点**:
  - Thinker–Talker 架构，二者均采用 Hybrid-Attention MoE
  - Gated Delta Net (GDN) 模块加速长音视频序列建模
  - ARIA (Adaptive Rate Interleave Alignment) — 动态对齐文本与语音单元，单流交错，提升流式语音稳定性
  - AuT 音频编码器（4000 万小时音频训练）
  - 支持 >10 小时音频理解 / 400 秒 720P 视频（1 FPS）
  - 215 项音频/视听 benchmark SOTA；Audio-Visual Vibe Coding 涌现能力
- **链接**: [arXiv:2604.15804](https://arxiv.org/abs/2604.15804)

### 8.3 Qwen3 Technical Report
- **中文标题**: Qwen3 技术报告
- **英文标题**: Qwen3 Technical Report
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3 (0.6B–32B dense + 30B-A3B / 235B-A22B MoE)
- **发布日期**: 2025-05
- **核心参数**: 旗舰 235B-A22B；36T tokens；119 种语言；上下文 128K
- **主要创新点**: Thinking/Non-thinking 双模式统一；Thinking budget；QK-Norm；强-弱蒸馏
- **链接**: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

---

## 9. xAI — Grok

### 9.1 Grok 4.7
- **中文标题**: Grok 4.7
- **英文标题**: Grok 4.7
- **发布机构**: xAI
- **模型名称**: Grok 4.7
- **发布日期**: 2026-09-21
- **核心参数**: 上下文 500K tokens（API/Cursor/Grok Build）；$2/$6 per 1M；参数量未公开
- **主要创新点**:
  - 消费端逐步全量推送（部分界面仍为 Grok 4.6）
  - 承接 Grok 4.6 的 reasoning / agentic 能力
- **链接**: [Next AI Model 追踪](https://www.nextaimodel.com/)

### 9.2 Grok 4.8（training/RL 中）
- **中文标题**: Grok 4.8
- **英文标题**: Grok 4.8
- **发布机构**: xAI
- **模型名称**: Grok 4.8 (2.5T)
- **发布日期**: 2026-09-14 宣布（训练中）
- **核心参数**: 2.5T 模型；新 C++ 软件栈训练；同 500K 上下文；$2/$6
- **主要创新点**: 更大 base model，更长 multi-hour agentic 任务训练
- **链接**: [Next AI Model 追踪](https://www.nextaimodel.com/)

### 9.3 Grok 4.20 System Card
- **中文标题**: Grok 4.20 系统卡
- **英文标题**: Grok 4.20 System Card
- **发布机构**: xAI
- **模型名称**: Grok 4.20
- **发布日期**: 2026-02-17
- **核心参数**: 上下文 1M tokens；$1.25/$2.50 per 1M
- **主要创新点**: 多 agent 能力（SA/MA）；改进 system prompt 遵循；CBRN + 网络安全评估
- **链接**: [xAI Data](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf)

### 9.4 Grok 4 Model Card
- **中文标题**: Grok 4 模型卡
- **英文标题**: Grok 4 Model Card
- **发布机构**: xAI
- **模型名称**: Grok 4
- **发布日期**: 2025-08
- **核心参数**: 256K 上下文；多模态；第三方推测 1.2–1.7T
- **主要创新点**: 200,000 GPU Colossus 集群 RL；原生工具使用 + 实时搜索；HLE 文本子集 50.7%（带工具）
- **链接**: [xAI Data](https://data.x.ai/2025-08-20-grok-4-model-card.pdf)

---

## 10. NVIDIA — Nemotron

### 10.1 Nemotron 3.5 Super VL
- **中文标题**: NVIDIA Nemotron 3.5 Super VL
- **英文标题**: Nemotron 3.5 Super VL
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3.5 Super VL (120B/12B active)
- **发布日期**: 2026-10-15
- **核心参数**: 120B 总参数 / 12B 激活；上下文 1M tokens；文本+图像+视频（最长 2 分钟）
- **主要创新点**: 开放权重多模态；超长上下文；视频理解
- **链接**: [Next AI Model 追踪](https://www.nextaimodel.com/)

### 10.2 Nemotron 3.5 Bolt / Lightning
- **中文标题**: Nemotron 3.5 Bolt 与 Lightning
- **英文标题**: Nemotron 3.5 Bolt (74B-A9B) / Lightning (30B-A3B)
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3.5 Bolt / Lightning
- **发布日期**: 2026-10-15（Bolt）/ 2026-08-11（Lightning）
- **核心参数**: Bolt: 74B 总 / 9B 激活；Lightning: 30B 总 / 3B 激活；上下文 262K
- **主要创新点**: 开放权重；面向边缘/消费级 GPU；极低成本（Lightning $0.05/$0.20 per 1M）
- **链接**: [LLM Stats](https://llm-stats.com/models/compare/grok-4-vs-nemotron-3.5-bolt-74b-a9b-24gb)

### 10.3 Nemotron 3 Family
- **中文标题**: NVIDIA Nemotron 3：高效开放智能
- **英文标题**: NVIDIA Nemotron 3: Efficient and Open Intelligence
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Nano (30B-A3B) / Super (49B) / Ultra (550B-A55B)
- **发布日期**: 2025-12（Ultra 2026-06）
- **核心参数**: Ultra: 550B 总 / 55B 激活；上下文 1M；NVFP4 预训练
- **主要创新点**: Hybrid Mamba-Transformer MoE；Multi-environment RL；粗粒度推理预算控制；LatentMoE + MTP + MOPD
- **链接**: [arXiv:2512.20856](https://arxiv.org/abs/2512.20856)

---

## 11. Moonshot AI — Kimi

### 11.1 Kimi K2.6
- **中文标题**: Kimi K2.6：推进开源编程能力
- **英文标题**: Kimi K2.6 Tech Blog: Advancing Open-Source Coding
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2.6
- **发布日期**: 2026-04
- **核心参数**: 上下文 262,144 tokens（thinking mode）；参数量未完整公开
- **主要创新点**:
  - 长周期编程能力：4000+ 工具调用 / 12+ 小时连续执行，Mac 本地部署 Qwen3.5-0.8B 推理吞吐 15→193 tok/s
  - 13 小时自主重构 8 年历史 exchange-core 撮合引擎（1000+ 工具调用 / 4000+ 行代码）
  - 开源权重榜首（Artificial Analysis Intelligence Index 54）
- **链接**: [Kimi Blog](https://www.kimi.com/blog/kimi-k2-6)

### 11.2 Kimi K2.5 Technical Report
- **中文标题**: Kimi K2.5 技术报告
- **英文标题**: Kimi K2.5 Technical Report
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2.5
- **发布日期**: 2026-02
- **核心参数**: 上下文 262K
- **主要创新点**: Zero-Vision SFT；Visual RL 提升文本表现；Agent Swarm via PARL；MoonViT-3D；Token-Efficient RL
- **链接**: [arXiv:2602.02276](https://arxiv.org/abs/2602.02276)

### 11.3 Kimi K2 Technical Report
- **中文标题**: Kimi K2 技术报告
- **英文标题**: Kimi K2 Technical Report
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2 (1T-A32B)
- **发布日期**: 2025-07
- **核心参数**: 1T 总参数 / 32B 激活（MoE）；384 experts
- **主要创新点**: MuonClip + QK-Clip 优化器（零 loss spike）；联合 RL；SWE-bench 65.8%
- **链接**: [arXiv:2507.20534](https://arxiv.org/abs/2507.20534)

---

## 12. Amazon — Nova

### 12.1 Amazon Nova Family Technical Report
- **中文标题**: Amazon Nova 家族技术报告与模型卡
- **英文标题**: The Amazon Nova Family of Models: Technical Report and Model Card
- **发布机构**: Amazon AGI
- **模型名称**: Nova Pro / Lite / Micro / Canvas / Reel / Premier
- **发布日期**: 2025-03（Premier 2025-04）
- **核心参数**: 多尺寸多模态模型；Premier 为最大旗舰
- **主要创新点**: 价效比设计导向；多模态（图像/视频/文档）；Premier 作为蒸馏教师
- **链接**: [arXiv:2506.12103](https://arxiv.org/abs/2506.12103)

> 注：截至 2026-10-22 未检索到 Amazon Nova 2 独立 arXiv 技术报告。

---

## 13. Apple — Apple Intelligence Foundation Models

### 13.1 Apple Foundation Models (AFM 3) — 第三代
- **中文标题**: Apple 第三代 Foundation Models
- **英文标题**: Introducing the Third Generation of Apple's Foundation Models
- **发布机构**: Apple（与 Google 合作）
- **模型名称**: AFM 3 Core (3B) / AFM 3 Core Advanced (20B) / AFM 3 Cloud / ADM 3 Cloud (Image) / AFM 3 Cloud Pro
- **发布日期**: 2026-06（WWDC26，随 iOS 27 / macOS 27 "Golden Gate" 于 2026-09-14）
- **核心参数**:
  - AFM 3 Core: 3B dense 端侧
  - AFM 3 Core Advanced: 20B 总参数 / 1–4B 激活（稀疏）
  - 输入端文本/图像/语音；输出文本/语音；25 种语言
- **主要创新点**:
  - AFM 3 Core Advanced 基于自研 Instruction-Following Pruning (IFP) 的稀疏激活架构
  - 跨 token 复用同一批 experts → 突破传统 MoE 需全模型驻留 RAM/VRAM 的限制
  - dense 静态权重驻 DRAM，FFN experts 驻 NAND flash，按需换入
  - 与 Google 联合定制，"distillation-based, not a wholesale adoption of Gemini"
  - Foundation Models Framework 开源，支持接入 Claude / Gemini 第三方模型
  - Private Cloud Compute 现运行于 NVIDIA GPU（Google Cloud）
  - macOS 27 新增 `/usr/bin/fm` 命令行接口
- **链接**: [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models)

### 13.2 Apple Intelligence Foundation Language Models: Tech Report 2025
- **中文标题**: Apple Intelligence 基础语言模型：2025 技术报告
- **英文标题**: Apple Intelligence Foundation Language Models: Tech Report 2025
- **发布机构**: Apple
- **模型名称**: AFM on-device (3B) / AFM server
- **发布日期**: 2025-07
- **核心参数**: 3B 端侧；服务器模型基于 Private Cloud Compute
- **主要创新点**: KV-cache sharing + 2-bit QAT；Parallel-Track MoE (PT-MoE)；Track parallelism + interleaved global-local attention
- **链接**: [arXiv:2507.13575](https://arxiv.org/abs/2507.13575)

---

## 14. ByteDance — Seed / 豆包

### 14.1 Seed1.6
- **中文标题**: Seed1.6 通用模型系列
- **英文标题**: Seed1.6 General Model Series
- **发布机构**: ByteDance Seed Team
- **模型名称**: Seed1.6
- **发布日期**: 2025-06
- **核心参数**: MoE 架构；23B 激活 / 230B 总参数；上下文 256K
- **主要创新点**: Adaptive Chain-of-Thought (AdaCoT)；三阶段预训练；原生多模态
- **链接**: [research.doubao.com](https://research.doubao.com/en/seed1_6)

### 14.2 Seed1.5-VL Technical Report
- **中文标题**: Seed1.5-VL 技术报告
- **英文标题**: Seed1.5-VL Technical Report
- **发布机构**: ByteDance Seed Team
- **模型名称**: Seed1.5-VL / Seed1.5-Thinking
- **发布日期**: 2025-05
- **核心参数**: 532M 视觉编码器 + MoE LLM（20B 激活 / 200B 总参数）
- **主要创新点**: 60 个公开 VLM benchmark 中 38 个 SOTA；GUI 控制和游戏玩法超越 OpenAI CUA / Claude 3.7
- **链接**: [arXiv:2505.07062](https://arxiv.org/abs/2505.07062)

> 注：Seedance 2.5（视频生成）于 2026-07-31 发布，为非综合技术报告。

---

## 15. 智谱 AI — GLM

### 15.1 GLM-5.3
- **中文标题**: GLM-5.3
- **英文标题**: GLM-5.3
- **发布机构**: 智谱 AI (Z.ai)
- **模型名称**: GLM-5.3 / GLM-5.3-Flash
- **发布日期**: 2026-08-14（权重两周后发布，许可较 MIT 收紧）
- **核心参数**: 承袭 GLM-5 系 ~744B 总 / ~40B 激活 MoE；1M 上下文
- **主要创新点**: 编程/agentic 能力提升；GLM-5.3-flash 支持 1M 上下文 + 多模态输入并可运行于消费级 GPU
- **链接**: [Fello AI 综述](https://felloai.com/glm-5-5/)

### 15.2 GLM-5.2
- **中文标题**: GLM-5.2
- **英文标题**: GLM-5.2
- **发布机构**: 智谱 AI
- **模型名称**: GLM-5.2
- **发布日期**: 2026-06-13
- **核心参数**: ~744B 总 / ~40B 激活（MoE）；1M 上下文
- **主要创新点**: Artificial Analysis Intelligence Index 51（开源最高）；接近 Opus 4.8 的 Terminal-Bench / SWE 编码能力，成本约 1/6；MIT 开源
- **链接**: [kie.ai 综述](https://kie.ai/blog/what-is-glm-5-5)

### 15.3 GLM-5
- **中文标题**: GLM-5
- **英文标题**: GLM-5
- **发布机构**: 智谱 AI
- **模型名称**: GLM-5 / GLM-5-FP8
- **发布日期**: 2026-02
- **核心参数**: ~744B 总 / ~40B 激活；28.5T tokens
- **主要创新点**: DSA 稀疏注意力（KV −75%）；编程超越 Gemini 3 Pro；国产芯片七大平台适配；SWE-bench Verified 77.8%；2026-01 港股上市
- **链接**: [arXiv:2602.15763](https://arxiv.org/abs/2602.15763)

> 注：GLM-5.5 曾传闻 2026-08 发布但实际被 GLM-5.3 取代，截至 2026-10-22 无官方模型卡/benchmark。

---

## 16. InternLM / 上海 AI Lab

### 16.1 InternVL3.5
- **中文标题**: InternVL3.5：推进开源多模态模型的通用性、推理与效率
- **英文标题**: InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency
- **发布机构**: Shanghai AI Lab / InternVL Team
- **模型名称**: InternVL3.5 (1B–241B-A28B)
- **发布日期**: 2025-08
- **核心参数**: 旗舰 241B-A28B（MoE）；dense 1B–38B
- **主要创新点**: Cascade RL（offline + online 两阶段）；Visual Resolution Router (ViR)；Decoupled Vision-Language Deployment (DvD)；推理性能 +16.0%，加速 4.05×
- **链接**: [arXiv:2508.18265](https://arxiv.org/abs/2508.18265)

### 16.2 InternVL3
- **中文标题**: InternVL3：探索开源多模态模型的高级训练与测试时方法
- **英文标题**: InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models
- **发布机构**: Shanghai AI Lab
- **模型名称**: InternVL3 (1B–78B)
- **发布日期**: 2025-04
- **核心参数**: 旗舰 78B；原生多模态预训练
- **主要创新点**: Variable Visual Position Encoding (V2PE)；Mixed Preference Optimization (MPO)；MMMU 72.2（开源 SOTA）
- **链接**: [arXiv:2504.10479](https://arxiv.org/abs/2504.10479)

> 注：截至 2026-10 未检索到 InternLM3 / InternVL4 独立综合技术报告；InternLM GitHub 近期以 CVPR/EMNLP 论文代码为主。

---

## 17. StepFun — 阶跃星辰

### 17.1 Step 5 Preview
- **中文标题**: Step 5 Preview
- **英文标题**: Step 5 Preview
- **发布机构**: StepFun
- **模型名称**: Step 5 Preview
- **发布日期**: 2026-09-28（Vals AI 追踪）
- **核心参数**: 参数量未公开
- **主要创新点**: 阶跃星辰新一代预览模型；Apache 2.0 风格开源路线延续
- **链接**: [Vals AI 追踪](https://www.vals.ai/models/)

### 17.2 Step-3.5 Flash
- **中文标题**: Step-3.5 Flash：为 Agent 而生的开源基础模型
- **英文标题**: Step-3.5 Flash
- **发布机构**: StepFun
- **模型名称**: Step-3.5 Flash (196B-A11B)
- **发布日期**: 2026-02
- **核心参数**: 196B 总 / 11B 激活；3:1 SWA-MTP3 架构
- **主要创新点**: 前沿推理和 Agent 能力；极致效率；数学 benchmark 突出；完全开源
- **链接**: [GitHub](https://github.com/stepfun-ai/Step-3.5-Flash)

### 17.3 Step-3 Technical Report
- **中文标题**: Step-3：大而可负担——模型-系统协同设计实现低成本解码
- **英文标题**: Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding
- **发布机构**: StepFun
- **模型名称**: Step-3 (321B/38B active VLM)
- **发布日期**: 2025-07
- **核心参数**: 321B 总 / 38B 激活（MoE）；VLM
- **主要创新点**: Attention-FFN 分离设计（AFD）；硬件感知架构优化；解码成本显著低于 DeepSeek-V3
- **链接**: [arXiv:2507.19427](https://arxiv.org/abs/2507.19427)

---

## 18. 01.AI — Yi

### 18.1 Yi: Open Foundation Models by 01.AI
- **中文标题**: Yi：01.AI 开源基础模型
- **英文标题**: Yi: Open Foundation Models by 01.AI
- **发布机构**: 01.AI
- **模型名称**: Yi (6B / 34B)
- **发布日期**: 2024-03（v3 更新 2025-01）
- **核心参数**: 6B / 34B 预训练模型；3.1T tokens 英中语料；200K 上下文
- **主要创新点**: 后 Chinchilla 最优训练；数据质量驱动；小规模高质量指令数据集；深度扩展持续预训练
- **链接**: [arXiv:2403.04652](https://arxiv.org/abs/2403.04652)

> 注：Yi-Lightning 有 arXiv 但非综合技术报告；截至 2026-10 无新一代 Yi 综合报告。

---

## 19. Baichuan

### 19.1 Baichuan-M4
- **中文标题**: Baichuan-M4：临床级医疗 Agent 系统
- **英文标题**: Baichuan-M4: A Clinical-Grade Medical Agent System
- **发布机构**: Baichuan Intelligence
- **模型名称**: Baichuan-M4
- **发布日期**: 2026-06（arXiv 2606.08982）
- **核心参数**: 医疗专用；面向持续性照护（非单轮问答）
- **主要创新点**: 临床级医疗大模型；医生监督下的连续照护设计
- **链接**: [arXiv:2606.08982](https://arxiv.org/abs/2606.08982)

### 19.2 Baichuan-Omni Technical Report
- **中文标题**: Baichuan-Omni 技术报告
- **英文标题**: Baichuan-Omni Technical Report
- **发布机构**: Baichuan Intelligence
- **模型名称**: Baichuan-Omni
- **发布日期**: 2024-10
- **核心参数**: 多模态大语言模型（图像 + 音频 + 视频 + 文本）
- **主要创新点**: 全模态理解；视频理解（ActivityNet-QA / MSVD-QA）
- **链接**: [arXiv:2410.08565](https://arxiv.org/abs/2410.08565)

---

## 交叉主题分析

### 1. 架构趋势：MoE + Hybrid 成绝对主流

| 公司 | 模型 | 架构 | 激活参数 / 总参数 |
|------|------|------|------------------|
| DeepSeek | V4-Pro | MoE + CSA/HCA + mHC | 49B / 1.6T |
| DeepSeek | V4-Flash | MoE + CSA/HCA | 13B / 284B |
| Meta | Muse Spark Open | MoE | 42B / 816B |
| Meta | Llama 5 Scout | MoE + activation pruning | 17B / 109B |
| Qwen | Qwen3.8-Max | MoE | — / 2.4T |
| Qwen | Qwen3.5-Omni | Hybrid-Attention MoE + GDN | 数百B |
| NVIDIA | Nemotron 3 Ultra | Hybrid Mamba-Transformer MoE | 55B / 550B |
| NVIDIA | Nemotron 3.5 Super VL | MoE (多模态) | 12B / 120B |
| Moonshot | Kimi K2 | MoE | 32B / 1T |
| 智谱 | GLM-5.2/5.3 | MoE + DSA | ~40B / ~744B |
| Apple | AFM 3 Core Advanced | IFP 稀疏 MoE | 1–4B / 20B |
| Google | Gemma 4 26B | MoE | 4B / 26B |
| xAI | Grok 4.8 | (训练中) | — / 2.5T |

### 2. 训练方法创新

- **优化器**: DeepSeek-V4 Muon（Newton-Schulz 正交化）首次用于万亿级 MoE；Kimi K2 MuonClip + QK-Clip
- **RL 后训练**: GRPO (DeepSeek), Multi-environment RL (Nemotron 3), Cascade RL (InternVL3.5), 联合缩放 RL 环境 (Qwen3.8-Max), RLVR (Baichuan-M2/M4)
- **合成数据 / 蒸馏**: Apple AFM 3 从 Gemini 蒸馏；Phi 系谱合成数据
- **量化感知训练**: Apple 2-bit QAT（AFM 2025）；Gemma 4 mobile int2/int4 QAT；DeepSeek MXFP4；Nemotron NVFP4
- **多模态激活**: Kimi K2.5 Zero-Vision SFT（纯文本 SFT 激活视觉）

### 3. Scaling Law / 缩放分析

- DeepSeek-V4: 1M 上下文推理 FLOPs 仅为 V3.2 的 27%，KV cache 仅 10%
- Qwen3: MoE 仅 1/5 激活参数达到同等 dense 性能
- Kimi K2.6: 4000+ 工具调用的长周期 scaling（12+ 小时连续执行）
- Apple AFM 3 Core Advanced: 稀疏激活突破端侧内存墙（experts 驻 flash）
- Gemma 4: global KV cache footprint 降低 37.5%

### 4. 长上下文竞赛

| 模型 | 上下文长度 | 技术 |
|------|-----------|------|
| DeepSeek V4 | 1M tokens | CSA + HCA |
| Llama 4 Scout | 10M tokens | iRoPE |
| Qwen3.8-Max | 1M tokens | 原生多模态 |
| Qwen3.5-Omni | 256K (+10h 音视频) | Hybrid MoE + GDN |
| Kimi K2.5/K2.6 | 262K | thinking mode |
| Nemotron 3/3.5 | 1M tokens | Hybrid Mamba |
| Gemini 4 Argon | 1M tokens | 原生 |
| Grok 4.7 | 500K | — |
| GLM-5.2 | 1M tokens | DSA |
| Apple AFM 3 | 未公开 | PT-MoE |

### 5. 推理模型格局

| 公司 | 推理模型 | 核心方法 |
|------|---------|---------|
| OpenAI | GPT-6 Sol / GPT-6.1 Sol / GPT-5.5 | CoT + deliberative alignment |
| DeepSeek | R1 / V3.2-Speciale / V4-Pro-Max | GRPO RL + 蒸馏 |
| Anthropic | Opus 5 / Opus 5.5 / Fable 5.1 | Adaptive thinking |
| Gemini | 2.5 Pro Deep Think / 4 Argon | 并行假设批判 |
| Microsoft | Phi-4-reasoning / Phi-5 Mini | o3-mini CoT 教学 + outcome RL |
| Mistral | Magistral | 领域特定推理 |
| xAI | Grok 4.6 / 4.7 / 4.8 | Scale RL |
| Kimi | K2-Thinking / K2.6 | Thinking mode + long-horizon |
| 智谱 | GLM-5.2 / 5.3 | DSA + 异步 RL |
| Qwen | Qwen3.8-Max | 联合缩放 RL 环境 |

### 6. 多模态 / Omni 趋势

- **Qwen3.5-Omni**: Thinker–Talker + ARIA 单流交错，215 项音频/视听 SOTA，Audio-Visual Vibe Coding
- **Apple AFM 3**: 端侧原生多模态（文本/图像/语音）+ 跨 token expert 复用
- **Nemotron 3.5 Super VL**: 视频理解（2 分钟）+ 1M 上下文
- **Meta Muse Spark Open**: 四模态输入（文本/图像/视频/音频）
- **Gemma 4**: 多模态 dense + MoE 双轨

### 7. 未发布正式综合技术报告的公司/模型

以下在截至 2026-10-22 的窗口内**未找到独立的综合 arXiv 技术报告**（仅有官方博客/产品发布/追踪站数据）：

- **Amazon Nova 2**: 无独立技术报告（最新为 2025-03 Nova 族报告）
- **InternLM / Shanghai AI Lab**: InternVL3.5 (2025-08) 为最新综合报告；无 InternVL4 / InternLM3
- **01.AI Yi**: 最新为 2024-03 Yi 基础模型报告
- **Baichuan**: 最新为医疗专用 Baichuan-M4 (2026-06)，无通用旗舰报告
- **Apple**: AFM 3 为官方博客 + ML Research 页面（无 arXiv PDF）；2025 有 arXiv:2507.13575
- **Meta Muse Spark**: 官方无独立技术报告，数据来自追踪站
- **StepFun Step 5**: 仅 Preview，无技术报告
- **Grok 4.7 / 4.8**: 仅产品发布 / 宣布，无系统卡（最新系统卡为 Grok 4.20）
- **GPT-6 / GPT-6.1 Sol**: 已发布但截止撰写点 spec 未公开（官方竞品对比中引用了 GPT-6 Astra 分数）

---

## 数据来源与置信度说明

- **正式技术报告（arXiv）**: DeepSeek-V4 (2606.19348)、Qwen3.5-Omni (2604.15804)、Gemma 4 (2607.02770)、Baichuan-M4 (2606.08982) — 高置信度
- **官方 System Card**: Anthropic Opus 5.5 / Fable 5.1 / Opus 5、OpenAI GPT-5.5、xAI Grok 4.20 / Grok 4 — 高置信度
- **官方博客 + 产品页**: OpenAI GPT-6 Sol/Luna、Apple AFM 3、Mistral Small 4、Kimi K2.6 — 中高置信度
- **聚合追踪站（BenchLM / LLMReference / Next AI Model / Vals AI / LLMCheck）**: Muse Spark Open、Nemotron 3.5、Grok 4.7、GLM-5.3、GPT-6.1 Sol、Step 5 Preview、Qwen3.8-Max、Llama 5、Phi-5 — ⚠️ 中置信度，参数量/日期可能与最终官方口径有差异
- ⚠️ 部分模型（如 GLM-5.5）存在传闻但未证实，已在正文标注
