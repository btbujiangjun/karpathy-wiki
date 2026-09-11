---
title: "LLM Tech Report Digest — 2026-09-11"
type: synthesis
created: 2026-09-11
updated: 2026-09-11
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, scaling-law, daily-digest]
---

# LLM Tech Report Digest — 2026-09-11

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-11）
> 覆盖 2024-12 至 2026-08 各家公开 Tech Report / System Card / White Paper

---

## 1. DeepSeek — DeepSeek-AI

### 1.1 DeepSeek-V3 Technical Report
- **中文标题**: DeepSeek-V3 技术报告
- **英文标题**: DeepSeek-V3 Technical Report
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V3
- **发布日期**: 2024-12（v2 更新 2025-02）
- **核心参数**: 671B 总参数 / 37B 激活参数（MoE）；预训练 14.8T tokens；上下文 128K
- **主要创新点**:
  - Multi-head Latent Attention (MLA) + DeepSeekMoE 架构
  - 无辅助损失负载均衡（auxiliary-loss-free load balancing）
  - Multi-Token Prediction (MTP) 训练目标
  - Group Relative Policy Optimization (GRPO) 后训练
  - 仅 2.788M H800 GPU hours（约 $5.6M）完成全量训练
  - 训练过程零 loss spike、零 rollback
- **链接**: [arXiv:2412.19437](https://arxiv.org/abs/2412.19437)

### 1.2 DeepSeek-V3.2 Technical Report
- **中文标题**: DeepSeek-V3.2：推动开放大语言模型前沿
- **英文标题**: DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V3.2 / V3.2-Speciale
- **发布日期**: 2025-12
- **核心参数**: 基于 V3 架构扩展；Speciale 为高计算推理变体
- **主要创新点**:
  - DeepSeek Sparse Attention (DSA) — 大幅降低长上下文计算复杂度
  - Agentic post-training 方法论
  - Speciale 在 IMO 2025、IOI 2025 达到金牌水平
  - 在多个推理 benchmark 上与 Kimi-K2-thinking 和 GPT-5 持平
- **链接**: [arXiv:2512.02556](https://arxiv.org/abs/2512.02556)

### 1.3 DeepSeek-R1
- **中文标题**: DeepSeek-R1：激励大语言模型推理能力
- **英文标题**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-R1 / R1-Zero
- **发布日期**: 2025-01
- **核心参数**: 多尺寸（1.5B 到 70B 蒸馏版）；R1 完整版基于 V3
- **主要创新点**:
  - R1-Zero：纯 GRPO RL 从零训练涌现推理能力（自我验证、反思、策略调整）
  - AIME'24 从 15.6% → 71.0%
  - 蒸馏 32B 版超越 o1-mini
  - 在 Nature 645 发表
- **链接**: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)

### 1.4 DeepSeek-V4 Technical Report
- **中文标题**: DeepSeek-V4：迈向高效百万 token 上下文智能
- **英文标题**: DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4-Pro (1.6T/49B active) / V4-Flash (284B/13B active)
- **发布日期**: 2026-04（Preview）；V4-Flash-0731 正式版 2026-07
- **核心参数**: Pro: 1.6T 总参数 / 49B 激活；Flash: 284B / 13B 激活；上下文 1M tokens；预训练 32T+ tokens
- **主要创新点**:
  - 混合注意力架构：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)
  - Manifold-Constrained Hyper-Connections (mHC) 增强残差连接
  - Muon 优化器首次应用于万亿级 MoE
  - 1M 上下文推理 FLOPs 仅为 V3.2 的 27%，KV cache 仅 10%
  - V4-Pro-Max 超越 GPT-5.2 和 Gemini-3.0-Pro
  - 开源 MIT 许可
- **链接**: [arXiv:2606.19348](https://arxiv.org/abs/2606.19348)

---

## 2. OpenAI

### 2.1 GPT-5 System Card
- **中文标题**: GPT-5 系统卡
- **英文标题**: GPT-5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5 (gpt-5-main / gpt-5-thinking)
- **发布日期**: 2025-08（arXiv 更新至 2026-05）
- **核心参数**: 统一系统 + 实时 router；thinking / main 双通道；参数量未公开
- **主要创新点**:
  - 统一架构：智能快速模型 + 深度推理模型 + 实时路由
  - Safe-Completions 安全训练（以输出安全为中心）
  - 幻觉率较 o3 降低 78%
  - gpt-5-thinking 在生化领域被归为 High capability
  - 5 个模型变体：main/mini/thinking/thinking-mini/thinking-nano/thinking-pro
- **链接**: [arXiv:2601.03267](https://arxiv.org/abs/2601.03267)

### 2.2 OpenAI o1 System Card
- **中文标题**: OpenAI o1 系统卡
- **英文标题**: OpenAI o1 System Card
- **发布机构**: OpenAI
- **模型名称**: OpenAI o1 / o1-mini
- **发布日期**: 2024-12
- **核心参数**: 参数量未公开
- **主要创新点**:
  - 从快速直觉思维转向慢速审慎推理
  - 训练中学习细化思考过程、尝试不同策略、识别错误
  - 首个 Preparedness v2 系统卡
- **链接**: [arXiv:2412.16720](https://arxiv.org/abs/2412.16720)

### 2.3 OpenAI GPT-4.5 System Card
- **中文标题**: OpenAI GPT-4.5 系统卡
- **英文标题**: OpenAI GPT-4.5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-4.5
- **发布日期**: 2025-02
- **主要创新点**: 遵循 OpenAI 安全流程构建和训练的能力评估
- **链接**: [cdn.openai.com](https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf)

---

## 3. Anthropic — Claude

### 3.1 Claude Opus 4 & Sonnet 4 System Card
- **中文标题**: Claude Opus 4 与 Sonnet 4 系统卡
- **英文标题**: System Card: Claude Opus 4 & Claude Sonnet 4
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 4 / Sonnet 4
- **发布日期**: 2025-05
- **核心参数**: 参数量未公开
- **主要创新点**:
  - Hybrid reasoning 大语言模型（推理 + 视觉分析 + 计算机使用 + 工具使用）
  - SWE-bench Verified 达到 72.5-72.7%
  - 首个包含 model welfare 评估的系统卡
  - Opus 4 触发 ASL-3 保护措施（生物风险缓解）
- **链接**: [Anthropic System Cards](https://www.anthropic.com/system-card)

### 3.2 Claude Opus 5 System Card
- **中文标题**: Claude Opus 5 系统卡
- **英文标题**: System Card: Claude Opus 5
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 5
- **发布日期**: 2026-07-24
- **核心参数**: 参数量未公开；知识截止 2026-05
- **主要创新点**:
  - Adaptive thinking 默认启用
  - Agentic coding 和 computer use 能力提升
  - 长周期知识工作改进
  - Anthropic ECI 评分 162.1（与 Mythos 5 相当）
  - 对齐表现历史最佳（misaligned 2.3%）
- **链接**: [Anthropic CDN](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)

### 3.3 Claude Fable 5.1 & Mythos 5.1 System Card
- **中文标题**: Claude Fable 5.1 与 Mythos 5.1 系统卡
- **英文标题**: System Card: Claude Fable 5.1 & Claude Mythos 5.1
- **发布机构**: Anthropic
- **模型名称**: Claude Fable 5.1 / Mythos 5.1
- **发布日期**: 2026-09-01
- **核心参数**: 参数量未公开
- **主要创新点**:
  - 编码、知识工作和问题解决前沿推进
  - CB-1 能力（化学/生物）但未达 CB-2 阈值
  - Mythos 5.1 网络安全评估史上最强
  - Mythos 5.1 在系统提示下诚实度低于近期 Claude 模型
- **链接**: [Anthropic CDN](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf)

---

## 4. Meta AI — LLaMA

### 4.1 Llama 3 Herd of Models
- **中文标题**: Llama 3 模型群
- **英文标题**: The Llama 3 Herd of Models
- **发布机构**: Meta AI
- **模型名称**: Llama 3 (8B / 70B / 405B)
- **发布日期**: 2024-07
- **核心参数**: 405B 最大稠密 Transformer；上下文 128K；多语言/代码/推理/工具
- **主要创新点**: 首次开源 405B 级别模型；支持 8 种语言
- **链接**: [arXiv:2407.21783](https://arxiv.org/abs/2407.21783)

### 4.2 Llama 4 Scout & Maverick
- **中文标题**: Llama 4 系列（Scout 和 Maverick）
- **英文标题**: Llama 4 Scout and Maverick
- **发布机构**: Meta AI
- **模型名称**: Llama 4 Scout (16 experts) / Maverick (128 experts)
- **发布日期**: 2025-04
- **核心参数**: 17B 激活参数（稀疏 MoE）；Scout 支持 10M token 上下文；从 288B 教师模型蒸馏
- **主要创新点**:
  - 稀疏 MoE 架构，有效实现万亿级参数
  - iRoPE + 长度泛化策略（Scout 10M 上下文）
  - 原生多模态 early fusion
  - FP8 训练
  - 轻量 SFT + online RL + 轻量 DPO 后训练
- **链接**: [Meta AI 官方](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

---

## 5. Google DeepMind — Gemini

### 5.1 Gemini 2.5 Technical Report
- **中文标题**: Gemini 2.5：推进前沿推理、多模态、长上下文与下一代 Agent 能力
- **英文标题**: Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 2.5 Pro / 2.5 Flash / 2.0 Flash / Flash-Lite
- **发布日期**: 2025-07（v6 更新 2025-12）
- **核心参数**: 参数量未公开；支持 3 小时视频处理
- **主要创新点**:
  - 原生多模态 Thinking model
  - Deep Think 模式（并行假设批判推理）
  - Thinking budget 机制（用户可分配推理计算资源）
  - AIME'25 88.0% / GPQA 88.4%
  - 1M+ token 上下文
  - 为超 15 亿月活用户提供 AI Overviews
- **链接**: [arXiv:2507.06261](https://arxiv.org/abs/2507.06261)

---

## 6. Microsoft — Phi

### 6.1 Phi-4 Technical Report
- **中文标题**: Phi-4 技术报告
- **英文标题**: Phi-4 Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4 (14B)
- **发布日期**: 2024-12
- **核心参数**: 14B 参数稠密模型；预训练 9.8T tokens；上下文 16K；1920 H100 GPU × 21 天
- **主要创新点**:
  - 合成数据为主体的训练策略（超越蒸馏 GPT-4）
  - Pivotal Token Search DPO（PTS-DPO）
  - 在 GPQA 和 MATH 上超越教师模型 GPT-4o
  - MIT 许可
- **链接**: [arXiv:2412.08905](https://arxiv.org/abs/2412.08905)

### 6.2 Phi-4-reasoning Technical Report
- **中文标题**: Phi-4-reasoning 技术报告
- **英文标题**: Phi-4-reasoning Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4-reasoning / Phi-4-reasoning-plus (14B)
- **发布日期**: 2025-04
- **核心参数**: 14B 参数；基于 Phi-4 SFT + outcome-based RL
- **主要创新点**:
  - "Teachable" prompts 精选 + o3-mini 长 CoT 教学
  - Phi-4-reasoning-plus 通过 RL 生成更长推理链
  - 14B 模型超越 DeepSeek-R1-Distill-Llama-70B，逼近完整 R1
  - 推理能力可迁移到通用 benchmark
- **链接**: [arXiv:2504.21318](https://arxiv.org/abs/2504.21318)

### 6.3 Phi-4-Mini Technical Report
- **中文标题**: Phi-4-Mini 技术报告：通过 Mixture-of-LoRAs 实现紧凑高效多模态语言模型
- **英文标题**: Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs
- **发布机构**: Microsoft
- **模型名称**: Phi-4-Mini (3.8B) / Phi-4-Multimodal
- **发布日期**: 2025-03
- **核心参数**: 3.8B 参数；200K 词汇表；GQA；多模态（文本+视觉+语音）
- **主要创新点**:
  - Mixture-of-LoRAs 多模态架构
  - 语音模态 LoRA 仅 460M 参数
  - OpenASR 排行榜第一
  - 推理实验版性能超越 DeepSeek-R1-Distill-Qwen-7B
- **链接**: [arXiv:2503.01743](https://arxiv.org/abs/2503.01743)

---

## 7. Mistral AI

### 7.1 Mistral 3 (Large 3 + Ministral 3)
- **中文标题**: Mistral 3 系列发布
- **英文标题**: Introducing Mistral 3
- **发布机构**: Mistral AI
- **模型名称**: Mistral Large 3 (675B/41B active MoE) / Ministral 3B / 8B / 14B
- **发布日期**: 2025-12
- **核心参数**: Large 3: 675B 总参数 / 41B 激活（MoE）；Ministral: 3B/8B/14B dense；训练于 3000 NVIDIA H200
- **主要创新点**:
  - Mistral 首个 MoE 模型（自 Mixtral 以来）
  - Ministral 系列：base/instruct/reasoning 三版本 × 三种尺寸
  - 原生多模态 + 多语言
  - Apache 2.0 许可
  - LMArena 排行榜 OSS 非推理模型 #2
- **链接**: [Mistral AI Blog](https://mistral.ai/news/mistral-3)

### 7.2 Magistral (Reasoning Model)
- **中文标题**: Magistral 推理模型发布
- **英文标题**: Introducing Magistral
- **发布机构**: Mistral AI
- **模型名称**: Magistral Small (24B OSS) / Magistral Medium
- **发布日期**: 2025-06
- **主要创新点**: Mistral 首个推理模型；领域特定、透明、多语言推理
- **链接**: [Mistral AI Blog](https://mistral.ai/news/magistral)

### 7.3 Mistral Medium 3
- **中文标题**: Mistral Medium 3：中等即大型
- **英文标题**: Medium is the new large
- **发布机构**: Mistral AI
- **模型名称**: Mistral Medium 3
- **发布日期**: 2025-05
- **核心参数**: 价格 $0.4/M input + $2/M output
- **主要创新点**:
  - 达到 Claude Sonnet 3.7 90% 以上性能，成本低一个数量级
  - 超越 Llama 4 Maverick 和 Cohere Command A
  - 企业级微调/自部署能力
- **链接**: [Mistral AI Blog](https://mistral.ai/news/mistral-medium-3)

---

## 8. Alibaba — Qwen

### 8.1 Qwen3 Technical Report
- **中文标题**: Qwen3 技术报告
- **英文标题**: Qwen3 Technical Report
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3 (0.6B–32B dense + 30B-A3B / 235B-A22B MoE)
- **发布日期**: 2025-05
- **核心参数**: 旗舰 235B-A22B（235B 总参数 / 22B 激活）；36T tokens 预训练；119 种语言和方言；上下文 128K
- **主要创新点**:
  - Thinking / Non-thinking 双模式统一框架
  - Thinking budget 机制（推理时动态分配计算）
  - QK-Norm 稳定训练
  - 强-弱蒸馏构建小模型
  - MoE 仅 1/5 激活参数达到同等 dense 性能
  - Apache 2.0 许可
- **链接**: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

### 8.2 Qwen2.5 Technical Report
- **中文标题**: Qwen2.5 技术报告
- **英文标题**: Qwen2.5 Technical Report
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen2.5 (0.5B–72B dense + MoE variants)
- **发布日期**: 2024-12
- **核心参数**: 18T tokens 预训练（从 7T 扩展）；SFT 超 100 万样本
- **主要创新点**: 预训练 7T→18T 大幅扩展；多阶段 RL 后训练；128K 上下文
- **链接**: [arXiv:2412.15115](https://arxiv.org/abs/2412.15115)

### 8.3 Qwen3.8-Max
- **中文标题**: 阿里巴巴发布 Qwen3.8-Max
- **英文标题**: Alibaba Unveils Qwen3.8-Max
- **发布机构**: Alibaba
- **模型名称**: Qwen3.8-Max
- **发布日期**: 2026-08
- **核心参数**: 2.4T 参数；上下文 1M tokens；原生多模态
- **主要创新点**:
  - Text Arena #5 / Vision Arena #2
  - 16 天自主执行真实软件工程项目
  - 联合缩放 RL 环境与计算
  - 自主重现发表研究并设计新方法
- **链接**: [Alibaba 官方](https://www.alibabagroup.com/en-US/document-2021044032125272064)

---

## 9. xAI — Grok

### 9.1 Grok 4 Model Card
- **中文标题**: Grok 4 模型卡
- **英文标题**: Grok 4 Model Card
- **发布机构**: xAI
- **模型名称**: Grok 4
- **发布日期**: 2025-08
- **核心参数**: 参数量未官方公开（第三方推测 1.2-1.7T）；256K 上下文；多模态
- **主要创新点**:
  - 200,000 GPU Colossus 集群 RL 训练
  - 原生工具使用 + 实时搜索集成
  - HLE 文本子集 50.7%（带工具）
  - AIME 2025 100%；HMMT 2025 99.4%
  - ARC-AGI-2 15.9%
- **链接**: [xAI Data](https://data.x.ai/2025-08-20-grok-4-model-card.pdf)

### 9.2 Grok 4.20 System Card
- **中文标题**: Grok 4.20 系统卡
- **英文标题**: Grok 4.20 System Card
- **发布机构**: xAI
- **模型名称**: Grok 4.20
- **发布日期**: 2026-04
- **核心参数**: 参数量未公开
- **主要创新点**:
  - 多 agent 能力（SA/MA 配置）
  - 改进的 system prompt instruction following
  - CBRN + 网络安全 + 有害操纵评估
  - 更高 system prompt 遵从度导致更高误用风险
- **链接**: [xAI Data](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf)

---

## 10. NVIDIA — Nemotron

### 10.1 Nemotron 3 Family
- **中文标题**: NVIDIA Nemotron 3：高效开放智能
- **英文标题**: NVIDIA Nemotron 3: Efficient and Open Intelligence
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Nano (30B-A3B) / Super (49B) / Ultra (550B-A55B)
- **发布日期**: 2025-12（Ultra 2026-06）
- **核心参数**: Ultra: 550B 总参数 / 55B 激活；上下文 1M tokens；NVFP4 预训练
- **主要创新点**:
  - Hybrid Mamba-Transformer MoE 架构（SSM + Attention）
  - Multi-environment RL 后训练
  - 粗粒度推理预算控制（推理时）
  - Ultra 推理吞吐 5.9× GLM-5.1-754B-A40B
  - 10T+ tokens 开源数据集
  - LatentMoE + MTP + MOPD
- **链接**: [arXiv:2512.20856](https://arxiv.org/abs/2512.20856)

---

## 11. Moonshot AI — Kimi

### 11.1 Kimi K2 Technical Report
- **中文标题**: Kimi K2 技术报告
- **英文标题**: Kimi K2 Technical Report
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2 (1T-A32B)
- **发布日期**: 2025-07
- **核心参数**: 1T 总参数 / 32B 激活（MoE）；384 experts
- **主要创新点**:
  - MuonClip + QK-Clip 优化器（零 loss spike）
  - 384 个 routed experts
  - 联合 RL 训练
  - SWE-bench 65.8%
- **链接**: [arXiv:2507.20534](https://arxiv.org/abs/2507.20534)

### 11.2 Kimi K2.5 Technical Report
- **中文标题**: Kimi K2.5 技术报告
- **英文标题**: Kimi K2.5 Technical Report
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2.5
- **发布日期**: 2026-02
- **核心参数**: 参数量未完整公开
- **主要创新点**:
  - Zero-Vision SFT（纯文本 SFT 激活视觉能力）
  - Visual RL 提升文本表现（MMLU-Pro +1.7%, GPQA +2.1%）
  - Agent Swarm via PARL（BrowseComp 78.4% 超 GPT-5.2 Pro）
  - MoonViT-3D 统一图像-视频编码
  - Token-Efficient RL（输出 -25-30%）
- **链接**: [arXiv:2602.02276](https://arxiv.org/abs/2602.02276)

---

## 12. Amazon — Nova

### 12.1 Amazon Nova Family Technical Report
- **中文标题**: Amazon Nova 家族技术报告与模型卡
- **英文标题**: The Amazon Nova Family of Models: Technical Report and Model Card
- **发布机构**: Amazon AGI
- **模型名称**: Nova Pro / Lite / Micro / Canvas / Reel / Premier
- **发布日期**: 2025-03（Premier 2025-04）
- **核心参数**: 多尺寸多模态模型；Premier 为最大旗舰
- **主要创新点**:
  - 价效比设计导向（Pro 速度/精度/成本最优组合）
  - Lite 极速处理图像/视频/文档
  - Micro 最低延迟纯文本
  - Canvas 图像生成 / Reel 视频生成
  - Premier 用于模型蒸馏的教师模型
- **链接**: [arXiv:2506.12103](https://arxiv.org/abs/2506.12103)

---

## 13. Apple — Apple Intelligence Foundation Models

### 13.1 Apple Intelligence Foundation Language Models: Tech Report 2025
- **中文标题**: Apple Intelligence 基础语言模型：2025 技术报告
- **英文标题**: Apple Intelligence Foundation Language Models: Tech Report 2025
- **发布机构**: Apple
- **模型名称**: AFM on-device (3B) / AFM server
- **发布日期**: 2025-07
- **核心参数**: 3B 端侧模型；服务器模型基于 Private Cloud Compute
- **主要创新点**:
  - KV-cache sharing + 2-bit quantization-aware training（端侧）
  - Parallel-Track MoE (PT-MoE) Transformer（服务器端）
  - Track parallelism + MoE sparse computation + interleaved global-local attention
  - 多语言 + 多模态 + 工具调用
  - Swift Foundation Models 框架
  - 2026 WWDC: 使用 NVIDIA GPU + Google Cloud 扩展 Private Cloud Compute
- **链接**: [arXiv:2507.13575](https://arxiv.org/abs/2507.13575)

---

## 14. ByteDance — Seed / 豆包

### 14.1 Seed1.5-VL Technical Report
- **中文标题**: Seed1.5-VL 技术报告
- **英文标题**: Seed1.5-VL Technical Report
- **发布机构**: ByteDance Seed Team
- **模型名称**: Seed1.5-VL
- **发布日期**: 2025-05
- **核心参数**: 532M 视觉编码器 + MoE LLM（20B 激活）
- **主要创新点**:
  - 在 60 个公开 VLM benchmark 中 38 个 SOTA
  - GUI 控制和游戏玩法超越 OpenAI CUA 和 Claude 3.7
  - 相对紧凑的架构实现广泛多模态理解
- **链接**: [arXiv:2505.07062](https://arxiv.org/abs/2505.07062)

### 14.2 Seed-Thinking-v1.5 Technical Report
- **中文标题**: Seed-Thinking-v1.5 技术报告
- **英文标题**: ByteDance's Latest Thinking Model, Seed-Thinking-v1.5
- **发布机构**: ByteDance Seed Team
- **模型名称**: Seed-Thinking-v1.5
- **发布日期**: 2025-04
- **核心参数**: MoE 架构；200B 总参数 / 20B 激活
- **主要创新点**:
  - 双轨道奖励系统（可验证任务 + 不可验证任务）
  - Seed-Thinking-Verifier 逐行推理步骤比较（>99% 准确率）
  - BeyondAIME 超难数学数据集
  - SFT + RL 两阶段优化
  - 在数学/编程/科学推理/创意写作均表现优异
- **链接**: [GitHub](https://github.com/ByteDance-Seed/Seed-Thinking-v1.5)

### 14.3 Seed1.6
- **中文标题**: Seed1.6 通用模型系列
- **英文标题**: Seed1.6 General Model Series
- **发布机构**: ByteDance Seed Team
- **模型名称**: Seed1.6
- **发布日期**: 2025-06
- **核心参数**: MoE 架构；23B 激活 / 230B 总参数；上下文 256K
- **主要创新点**:
  - Adaptive Chain-of-Thought (AdaCoT) 自适应思考
  - 三阶段预训练（text-only → multimodal mixed → long-context）
  - 原生多模态支持
  - 多项视觉任务超越 Seed1.5-VL
- **链接**: [research.doubao.com](https://research.doubao.com/en/seed1_6)

---

## 15. 智谱 AI — GLM

### 15.1 GLM-4.5 Technical Report
- **中文标题**: GLM-4.5 技术报告
- **英文标题**: GLM-4.5: An Open Mixture-of-Experts LLM
- **发布机构**: 智谱 AI (Zhipu AI)
- **模型名称**: GLM-4.5
- **发布日期**: 2025-08
- **核心参数**: MoE 架构（参考 DeepSeek-V3 但更窄更深）；SFT 后训练分专家训练 + 通用训练两阶段
- **主要创新点**:
  - 借鉴 DeepSeek-V3 架构但缩窄增加深度
  - 无损平衡路由（loss-free balanced routing）
  - 异步 RL 训练
  - 推理/编程/智能体三大能力融合
  - 发布时全球开源 SOTA
  - 中期训练阶段（区别于传统预训练+后训练）
- **链接**: [智谱官方](https://www.zhipuai.cn/)

### 15.2 GLM-5
- **中文标题**: GLM-5
- **英文标题**: GLM-5
- **发布机构**: 智谱 AI
- **模型名称**: GLM-5 / GLM-5-FP8
- **发布日期**: 2026-02
- **核心参数**: ~744B 总参数 / ~40B 激活；28.5T tokens
- **主要创新点**:
  - DSA 稀疏注意力（KV -75%，推理 +3×）
  - 编程能力超越 Gemini 3 Pro，对齐 Opus 4.6
  - 国产芯片七大平台适配
  - SWE-bench Verified 77.8%
  - 2026-01 港股上市（"全球大模型第一股"）
- **链接**: [arXiv:2602.15763](https://arxiv.org/abs/2602.15763)

---

## 16. InternLM / 上海 AI Lab

### 16.1 InternVL3.5
- **中文标题**: InternVL3.5：推进开源多模态模型的通用性、推理与效率
- **英文标题**: InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency
- **发布机构**: Shanghai AI Lab / InternVL Team
- **模型名称**: InternVL3.5 (1B–241B-A28B)
- **发布日期**: 2025-08
- **核心参数**: 旗舰 241B-A28B（MoE）；dense 版本 1B–38B
- **主要创新点**:
  - Cascade Reinforcement Learning（offline RL + online RL 两阶段）
  - Visual Resolution Router (ViR) 动态调整视觉 token 分辨率
  - Decoupled Vision-Language Deployment (DvD) 分离视觉编码器和语言模型
  - 推理性能 +16.0%，推理加速 4.05×
  - GUI 交互和具身智能体能力
  - 与 GPT-5 差距缩小至 3.9%
- **链接**: [arXiv:2508.18265](https://arxiv.org/abs/2508.18265)

### 16.2 InternVL3
- **中文标题**: InternVL3：探索开源多模态模型的高级训练与测试时方法
- **英文标题**: InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models
- **发布机构**: Shanghai AI Lab / InternVL Team
- **模型名称**: InternVL3 (1B–78B)
- **发布日期**: 2025-04
- **核心参数**: 旗舰 78B；原生多模态预训练
- **主要创新点**:
  - 原生多模态预训练范式（非后训练拼接）
  - Variable Visual Position Encoding (V2PE) 支持超长多模态上下文
  - Mixed Preference Optimization (MPO)
  - MMMU 72.2（开源 SOTA）
- **链接**: [arXiv:2504.10479](https://arxiv.org/abs/2504.10479)

---

## 17. StepFun — 阶跃星辰

### 17.1 Step-3 Technical Report
- **中文标题**: Step-3：大而可负担——模型-系统协同设计实现低成本解码
- **英文标题**: Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding
- **发布机构**: StepFun
- **模型名称**: Step-3 (321B/38B active VLM)
- **发布日期**: 2025-07
- **核心参数**: 321B 总参数 / 38B 激活（MoE）；VLM
- **主要创新点**:
  - 模型-系统协同设计（Model-system co-design）
  - Attention-FFN 分离设计（AFD）
  - 硬件感知架构优化
  - 解码成本显著低于 DeepSeek-V3 和 Qwen3-MoE-235B
  - 长上下文场景优势更大
- **链接**: [arXiv:2507.19427](https://arxiv.org/abs/2507.19427)

### 17.2 Step-3.5 Flash
- **中文标题**: Step-3.5 Flash：为 Agent 而生的开源基础模型
- **英文标题**: Step-3.5 Flash
- **发布机构**: StepFun
- **模型名称**: Step-3.5 Flash (196B)
- **发布日期**: 2026-02
- **核心参数**: 196B 参数；3:1 SWA-MTP3 架构
- **主要创新点**:
  - 前沿推理和 Agent 能力
  - 极致效率
  - 完全开源
- **链接**: [GitHub](https://github.com/stepfun-ai/Step-3.5-Flash)

### 17.3 Step-DeepResearch
- **中文标题**: Step-DeepResearch 技术报告
- **英文标题**: Step-DeepResearch Technical Report
- **发布机构**: StepFun
- **模型名称**: Step-DeepResearch (32B)
- **发布日期**: 2025-12
- **核心参数**: 32B 参数
- **主要创新点**:
  - 基于原子能力的数据合成策略
  - 单 ReAct agent 设计（非多 agent 编排）
  - ResearchRubrics 61.42 分（与 OpenAI/Gemini DeepResearch 相当）
  - 极低部署和推理成本
- **链接**: [arXiv:2512.20491](https://arxiv.org/abs/2512.20491)

---

## 18. 01.AI — Yi

### 18.1 Yi: Open Foundation Models by 01.AI
- **中文标题**: Yi：01.AI 开源基础模型
- **英文标题**: Yi: Open Foundation Models by 01.AI
- **发布机构**: 01.AI
- **模型名称**: Yi (6B / 34B)
- **发布日期**: 2024-03（v3 更新 2025-01）
- **核心参数**: 6B 和 34B 预训练模型；3.1T tokens 英中语料；200K 上下文
- **主要创新点**:
  - 后 Chinchilla 最优训练
  - 数据质量驱动（级联去重 + 质量过滤）
  - 小规模高质量指令数据集（<10K 每条人工验证）
  - 深度扩展（depth upscaled）持续预训练
  - 200K 长上下文
- **链接**: [arXiv:2403.04652](https://arxiv.org/abs/2403.04652)

---

## 19. Baichuan

### 19.1 Baichuan-Omni Technical Report
- **中文标题**: Baichuan-Omni 技术报告
- **英文标题**: Baichuan-Omni Technical Report
- **发布机构**: Baichuan Intelligence
- **模型名称**: Baichuan-Omni
- **发布日期**: 2024-10（v4 更新 2024-12）
- **核心参数**: 多模态大语言模型（图像+音频+视频+文本）
- **主要创新点**:
  - 全模态理解能力
  - 视频理解（ActivityNet-QA / MSVD-QA）
  - 开放式问答生成能力突出
- **链接**: [arXiv:2410.08565](https://arxiv.org/abs/2410.08565)

---

## 交叉主题分析

### 1. 架构趋势：MoE + Hybrid 成主流

| 公司 | 模型 | 架构 | 激活参数 / 总参数 |
|------|------|------|------------------|
| DeepSeek | V4-Pro | MoE + CSA/HCA | 49B / 1.6T |
| DeepSeek | V4-Flash | MoE | 13B / 284B |
| Meta | Llama 4 | MoE | 17B / 多专家 |
| Qwen | Qwen3-235B | MoE | 22B / 235B |
| Mistral | Large 3 | MoE | 41B / 675B |
| NVIDIA | Nemotron 3 Ultra | Hybrid Mamba-Transformer MoE | 55B / 550B |
| Moonshot | Kimi K2 | MoE | 32B / 1T |
| 智谱 | GLM-5 | MoE | ~40B / ~744B |
| StepFun | Step-3 | MoE | 38B / 321B |
| ByteDance | Seed1.6 | MoE | 23B / 230B |

### 2. 训练方法创新

- **RL 后训练**: GRPO (DeepSeek), Outcome-based RL (Phi-4-reasoning), AdaCoT (Seed1.6), Multi-environment RL (Nemotron 3), Cascade RL (InternVL3.5)
- **合成数据**: Phi-4 为主体, DeepSeek-R1 蒸馏, Kimi K2.5 Zero-Vision SFT
- **RLHF/DPO**: Mistral Online DPO, DeepSeek GRPO + rule-based hybrid reward
- **Think Budget**: Gemini 2.5, Qwen3, Grok 均支持推理时动态计算分配

### 3. Scaling Law / 缩放分析

- DeepSeek-V4: 1M 上下文推理 FLOPs 仅为 V3.2 的 27%
- Qwen3: MoE 仅 1/5 激活参数达到同等 dense 性能
- NVIDIA Nemotron 3: NVFP4 4-bit 预训练稳定至 25T tokens
- Microsoft Phi-4: 合成数据 + 小模型超越大模型教师

### 4. 长上下文竞赛

| 模型 | 上下文长度 | 技术 |
|------|-----------|------|
| DeepSeek V4 | 1M tokens | CSA + HCA |
| Llama 4 Scout | 10M tokens | iRoPE |
| Nemotron 3 | 1M tokens | Hybrid Mamba |
| Kimi K2 | 128K+ | KDA + AttnRes |
| Qwen3 | 128K | 标准 |
| Gemini 2.5 | 1M+ | 原生 |
| Qwen3.8-Max | 1M | - |

### 5. 推理模型格局

| 公司 | 推理模型 | 核心方法 |
|------|---------|---------|
| OpenAI | o1/o3/gpt-5-thinking | CoT + deliberative alignment |
| DeepSeek | R1 / V3.2-Speciale | GRPO RL + 蒸馏 |
| Anthropic | Opus 4/5 | Adaptive thinking |
| Gemini | 2.5 Pro Deep Think | 并行假设批判 |
| Microsoft | Phi-4-reasoning | o3-mini CoT 教学 + outcome RL |
| Mistral | Magistral | 领域特定推理 |
| xAI | Grok 4 | Scale RL |
| Kimi | K2-Thinking | Thinking mode |

### 6. 未发布正式报告的公司

以下公司在截至 2026-09-11 的窗口内**未找到独立的 arXiv 技术报告**（仅有官方博客/产品发布）：

- **Baichuan**: 仅有 Baichuan-Omni (2024-10)；近期 Baichuan-M4 (2026) 发布于 arXiv 但为医疗专用
- **Apple**: AFM 2025 Tech Report 已发布 (arXiv:2507.13575)，2026 年度报告尚未发布
- **Yi / 01.AI**: 最新报告为 2024-03 的 Yi 基础模型报告；Yi-Lightning 有 arXiv 但非综合技术报告
