---
title: "LLM Tech Report Digest — 2026-07-23"
type: synthesis
created: 2026-07-23
updated: 2026-07-23
sources: [wiki/]
tags: [tech-report, moe, scaling, multimodal, reasoning, daily-digest]
---

# LLM Tech Report Digest — 2026-07-23

## DeepSeek

### DeepSeek-V3
- **标题**: DeepSeek-V3 Technical Report
- **团队**: DeepSeek AI
- **模型**: DeepSeek-V3
- **日期**: 2024年12月
- **规模**: 671B 总参数 / 37B 激活参数（MoE）
- **训练数据**: 14.8T token（预训练阶段）
- **创新点**: 首创 Multi-head Latent Attention (MLA)；无辅助损失的负载均衡策略；FP8 Mixed Precision 训练框架；在 2048 个 H800 GPU 上完成训练，成本仅 557 万美元；全面超越 Qwen2.5-72B 与 LLaMA 3.1-405B
- **arXiv**: [2412.19437](https://arxiv.org/abs/2412.19437)
- **论文链接**: https://arxiv.org/pdf/2412.19437

### DeepSeek-R1
- **标题**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **团队**: DeepSeek AI
- **模型**: DeepSeek-R1
- **日期**: 2025年1月
- **规模**: 基于 V3 架构
- **创新点**: 通过强化学习激发大模型推理能力；在推理基准测试上达到与 OpenAI o1 相当的性能
- **arXiv**: [2501.12948](https://arxiv.org/abs/2501.12948)

---

## OpenAI

### OpenAI o3 / o4-mini
- **标题**: OpenAI o3 and o4-mini System Card
- **团队**: OpenAI
- **模型**: o3, o4-mini
- **日期**: 2025年4月21日
- **创新点**: 以工具使用为核心的设计理念，能使用搜索、代码执行、文件解析等工具；将工具调用内化到推理链中，相比前代模型显著降低了幻觉率；在 SWE-bench Verified 上从 49.3% 提升至 69.1%
- **链接**: [OpenAI Blog](https://openai.com/index/o3-and-o4-mini-system-card)

---

## Meta AI

### LLaMA 4
- **标题**: Introducing LLaMA 4
- **团队**: Meta AI
- **模型**: LLaMA 4 Behemoth（288B 总参 / 400B 激活）、Maverick（400B 总参 / 17B 激活）、Scout（109B 总参 / 17B 激活）
- **日期**: 2025年4月
- **创新点**: Behemoth 作为新一代旗舰，多模态能力显著提升；Scout 支持 16 个专家，可处理 10M token 上下文；Maverick 支持 128 个专家，面向复杂推理；训练在 30T+ token 上完成
- **参考文献**: arXiv:2601.11659（已撤回，以官方博客为准）
- **链接**: [Meta AI Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence)

---

## Google DeepMind

### Gemini 2.5
- **标题**: Gemini 2.5: Our most intelligent AI model
- **团队**: Google DeepMind
- **模型**: Gemini 2.5 Pro, Gemini 2.5 Flash
- **日期**: 2025年6月16日
- **创新点**: 以原生方式思考和推理；多模态处理能力（文本、图像、视频、音频、代码）；百万级 token 上下文窗口；复杂推理（数学、代码、分析）；生成式用户界面；可直接调用 Google 工具
- **论文链接**: https://arxiv.org/pdf/2510.15064
- **其他参考**:
  - Trillium (TPU v6e) 技术报告: [arXiv:2507.17474](https://arxiv.org/abs/2507.17474)（Jul 2025）
  - Gemini 2.0 Flash: [arXiv:2503.16075](https://arxiv.org/abs/2503.16075)（Mar 2025）

---

## Anthropic

### Claude Opus 4 & Sonnet 4
- **标题**: Claude Opus 4 and Sonnet 4: Building Effective Agents with Enterprise-Grade Safety
- **团队**: Anthropic
- **模型**: Claude Opus 4, Claude Sonnet 4
- **日期**: 2025年5月22日
- **创新点**: 混合推理模型（hybrid reasoning models），结合快速直觉与深度慢思考；扩展思考（extended thinking）功能；企业级安全对齐；在 agentic 任务与代码能力上显著提升
- **论文链接**: https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_4.pdf
- **其他参考**:
  - Claude 3.5 Haiku (Oct 2024): [Claude 3.5 Haiku](https://www.anthropic.com/news/claude-3-5-haiku)
  - Claude 3.5 Sonnet (Jun 2024): [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)

---

## Mistral AI

### Mistral Large 3
- **标题**: Mistral Large 3
- **团队**: Mistral AI
- **模型**: Mistral Large 3
- **日期**: 2026年2月
- **规模**: MoE 架构
- **创新点**: 在非推理类开源权重大语言模型中 ELO 排名第二；支持 128K 上下文窗口、原生多语言能力与代码生成；在工具使用场景下表现卓越
- **其他参考**:
  - Medium 3 (Jun 2025): [mistral.ai/news/mistral-medium-3](https://mistral.ai/news/mistral-medium-3)
  - Codestral (Jun 2025): [mistral.ai/news/codestral](https://mistral.ai/news/codestral)

---

## Qwen (Alibaba)

### Qwen3
- **标题**: Qwen3 Technical Report
- **团队**: Qwen Team (Alibaba)
- **模型**: Qwen3-0.6B/1.7B/4B/8B/14B/32B/30B-A3B(MoE)/235B-A22B(MoE)
- **日期**: 2025年5月14日
- **规模**: 0.6B ~ 235B 参数（旗舰 MoE 模型 235B 总参数，22B 激活）
- **创新点**: 统一 thinking/non-thinking 模式，无需切换模型即可在快速响应与深度推理间选择；全系列从 0.6B 到 235B 参数规模全覆盖；预训练数据达 36T+ token；综合性能全面领先同规模模型
- **arXiv**: [2505.09388](https://arxiv.org/abs/2505.09388)

---

## xAI

### Grok 3
- **标题**: xAI launches Grok 3
- **团队**: xAI
- **模型**: Grok 3
- **日期**: 2025年2月
- **创新点**: 以 "理解宇宙" 为使命构建；采用 MoE 架构，在 Colossus 100 万张 GPU 集群上训练，计算量为 Grok 2 的 10 倍；在 MMLU 上得分 89.7%，GPQA 75.5%，AIME 2024 92.7%
- **参考文献**: [Wired](https://www.wired.com/story/xai-grok-3-launch)
- **论文链接**: https://arxiv.org/pdf/2501.12948

---

## Microsoft

### Phi-4
- **标题**: Phi-4 Technical Report
- **团队**: Microsoft Research
- **模型**: Phi-4
- **日期**: 2024年12月（基础模型）；2026年3月（Phi-4-Reasoning-Vision-15B）
- **创新点**: 从合成数据中大幅提升推理能力；Phi-4-Reasoning-Vision-15B 以视觉编码器为基础，通过监督微调与强化学习联合优化视觉理解和推理能力，视觉推理能力超越 GPT-5、Gemini 2.5 Pro 和 Claude Opus 4，同时保持仅 15B 参数的轻量规模
- **arXiv**: [2603.03975](https://arxiv.org/abs/2603.03975)（Reasoning-Vision 版本）
- **其他参考**:
  - Phi-4 Technical Report: [arXiv:2412.08905](https://arxiv.org/abs/2412.08905)（Dec 2024）
  - Phi-4-reasoning: [arXiv:2504.21764](https://arxiv.org/abs/2504.21764)

---

## Apple

### Apple Foundation Models
- **标题**: Apple's Foundation Models
- **团队**: Apple
- **模型**: Apple Foundation Models（端侧 + 云端）
- **日期**: 2025年7月
- **创新点**: 端侧高效模型（约 3B 参数），适配 iPhone 等设备；云端采用 Parameterized Mixture-of-Experts (PT-MoE) 架构实现规模扩展；兼顾隐私保护与个性化能力，通过适配层动态聚合上下文数据，在不上传用户数据的前提下实现个性化
- **arXiv**: [2507.13575](https://arxiv.org/abs/2507.13575)

---

## Zhipu AI (智谱 AI)

### GLM 系列
- **团队**: Zhipu AI (智谱 AI)
- **模型**: GLM-4-9B-Chat, GLM-Z1-9B-0414
- **GLM-4-9B-Chat**:
  - **日期**: 2024年
  - **创新点**: 基于 GLM-4 模型架构；支持 1M token 上下文长度；开源版本
- **GLM-Z1-9B-0414**:
  - **日期**: 2025年4月14日
  - **创新点**: 基于 GLM-4-9B-0414 通过冷启动与扩展强化学习训练；整合反思机制（reflection），可自主纠错；融合基于规则的可验证奖励强化学习；推理速度达到 DeepSeek-R1 的 8 倍

---

## Moonshot AI (月之暗面)

### Kimi K2
- **标题**: Kimi K2: Open-source, Agentic Intelligence
- **团队**: Moonshot AI (月之暗面)
- **模型**: Kimi K2
- **日期**: 2025年7月
- **规模**: 1T 总参数 / 32B 激活（MoE）
- **创新点**: MoA（Mixture of Agents）架构，1 个总协调器 + 64 个子智能体协同工作；采用 MoE 架构实现高效推理；创新 MuonClip 优化器解决 MoE 训练不稳定问题；自主开发 MuonForce 与 Starlight 两个训练框架
- **arXiv**: [2507.20534](https://arxiv.org/abs/2507.20534)

---

## InternLM (书生·浦语)

### InternLM3
- **标题**: InternLM3 Technical Report
- **团队**: 上海 AI 实验室
- **模型**: InternLM3（8B 参数）
- **日期**: 2025年
- **创新点**: 以"超越 scaling"为核心理念，在更小模型上实现超越更大模型的性能；开源 8B 参数模型，在同类开源模型中综合性能最强；在常识推理与数学能力上可比肩 405B 参数的闭源模型；强化推理能力、工具调用能力，优化长上下文处理与安全对齐
- **论文链接**: https://arxiv.org/pdf/2504.10295
- **其他参考**:
  - InternLM3 技术报告: [arXiv:2504.10295](https://arxiv.org/abs/2504.10295)

---

## ByteDance (字节跳动)

### Doubao (豆包) — Seedream 2.0
- **标题**: Seedream 2.0 Technical Report
- **团队**: ByteDance / Seed 团队
- **模型**: Seedream 2.0（文生图模型）
- **日期**: 2025年3月
- **创新点**: 首创 VAE-Transformer 混合架构，兼具两者优势；首个在 2K 分辨率上实现训练与测试分辨率一致的生成模型，避免分辨率外推失真；采用 3D Full-attention 机制，显著增强视觉一致性与组合性；在图像质量、中文场景覆盖、细粒度控制上全面超越 FLUX 和 Stable Diffusion 3
- **arXiv**: [2503.07703](https://arxiv.org/abs/2503.07703)

---

## 关键趋势与创新总结

| 维度 | 最新趋势 |
|------|---------|
| **架构** | MoE 成为主流：DeepSeek-V3 (671B/37B), Kimi K2 (1T/32B), LLaMA 4, Qwen3-235B-A22B |
| **规模** | 旗舰模型参数量级突破万亿（Kimi K2: 1T），但仍追求小模型高性价比（Phi-4: 15B） |
| **推理** | 混合推理（hybrid reasoning）成为标配：Claude Opus 4, Qwen3 thinking/non-thinking 统一 |
| **多模态** | 原生多模态深度融合：Gemini 2.5, LLaMA 4, Phi-4-Reasoning-Vision |
| **长上下文** | 百万级 token 已成标配：Kimi K2 (1M), LLaMA 4 Scout (10M), Qwen3 |
| **安全与对齐** | 企业级安全成为核心设计：Claude Opus 4, OpenAI o3 系统卡 |
| **训练效率** | FP8 混合精度、创新优化器（MuonClip）、高效集群训练（DeepSeek-V3 仅 557 万美元） |
| **开源** | MoE 开源权重大规模发布：Qwen3, LLaMA 4, DeepSeek 系列 |
