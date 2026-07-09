---
title: LLM Tech Report Digest 2026
type: synthesis
created: 2026-07-09
updated: 2026-07-09
sources: []
tags: [tech-report, digest, llm, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, xai, nvidia, apple]
---

# LLM 技术报告速览 2026

> 各大 AI 公司最新技术报告、System Card 汇总。更新至 2026 年 7 月。

---

## 1. DeepSeek — DeepSeek-V4

- **中文标题**: DeepSeek-V4：面向高效百万 Token 上下文智能
- **英文标题**: DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4-Pro / DeepSeek-V4-Flash
- **发布日期**: 2026-04-24 (arXiv: 2026-06-19)
- **核心参数**:
  - V4-Pro: 1.6T 总参数, 49B 激活, MoE
  - V4-Flash: 284B 总参数, 13B 激活, MoE
  - 上下文: 1M tokens
  - 预训练: 32T+ tokens
- **主要创新点**:
  - 混合注意力架构: Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)，KV cache 降至 V3.2 的 10%
  - Manifold-Constrained Hyper-Connections (mHC) 增强残差连接
  - Muon 优化器实现更快收敛
  - On-Policy Distillation 替代 RL 进行后训练
  - V4-Pro-Max 在 Codeforces 达 3206 Elo
- **arXiv**: [2606.19348](https://arxiv.org/abs/2606.19348)
- **HuggingFace**: [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

---

## 2. OpenAI — o3 & o4-mini System Card

- **中文标题**: OpenAI o3 和 o4-mini 系统卡
- **英文标题**: OpenAI o3 and o4-mini System Card
- **发布机构**: OpenAI
- **模型名称**: o3 / o4-mini
- **发布日期**: 2025-04-16
- **核心参数**:
  - o3: 推理模型，支持思维链、工具调用、图像理解
  - o4-mini: 轻量推理模型
  - 上下文: 未公开详细参数
  - 支持浏览、Python 执行、图像生成
- **主要创新点**:
  - 推理模型可主动调用工具（搜索、Python、图像生成）
  - o3 在 Codeforces、SWE-bench、MMMU 达 SOTA
  - 相比 o1 减少 20% 重大错误
  - 指令层级 (Instruction Hierarchy) 机制
  - Agentic 编码能力大幅提升
- **System Card**: [OpenAI o3 and o4-mini System Card (PDF)](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)
- **公告**: [Introducing o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini)

---

## 3. Meta AI — Llama 4

- **中文标题**: Llama 4 家族：架构、训练、评估与部署
- **英文标题**: The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes
- **发布机构**: Meta AI
- **模型名称**: Llama 4 Scout / Llama 4 Maverick / Llama 4 Behemoth
- **发布日期**: 2025-04-05
- **核心参数**:
  - Scout: 109B 总参数 (17B 激活), 16 experts, MoE, 10M 上下文
  - Maverick: 400B 总参数 (17B 激活), 128 experts, MoE, 1M 上下文
  - Behemoth: ~2T 总参数 (288B 激活), 16 experts (教师模型)
  - 预训练: 40T tokens
  - 原生多模态 (early fusion)
- **主要创新点**:
  - Llama 系列首次采用 MoE 架构
  - iRoPE 实现 10M 超长上下文
  - 原生多模态理解（文本 + 图像）
  - Scout 可在单张 H100 上运行 (INT4)
  - 轻量 SFT → 在线 RL → 轻量 DPO 的后训练管线
- **Model Card**: [developer.meta.com](https://developer.meta.com/ai/models/llama-4/)
- **arXiv (withdrawn)**: [2601.11659](https://arxiv.org/abs/2601.11659)

---

## 4. Google DeepMind — Gemini 2.5

- **中文标题**: Gemini 2.5：以高级推理、多模态、长上下文和下一代 Agent 能力推动前沿
- **英文标题**: Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 2.5 Pro / Gemini 2.5 Flash
- **发布日期**: 2026-03 (技术报告)
- **核心参数**:
  - MoE Transformer 架构
  - 训练于 TPUv5p
  - 上下文: 1M+ tokens
  - 原生多模态 (文本、图像、音频、视频)
- **主要创新点**:
  - 推理时计算 (thinking) — 强化学习训练的 inference-time compute
  - Gemini 2.5 Pro: GPQA Diamond 86.4%, HLE 21.6%, FACTS Grounding 87.8%
  - Flash 支持可控 thinking budget
  - Deep Think 模式：并行推理生成+批判多个假设
  - 编码能力飞跃：LiveCodeBench 从 29.7% → 74.2%, Aider Polyglot 16.9% → 82.2%
  - 知识蒸馏 (k-sparse) 训练小模型
- **技术报告 PDF**: [Gemini 2.5 Report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf)
- **后续模型**: Gemini 3 Pro (2025-11), Gemini 3.5 Flash (2026-05)
- **Model Card**: [Gemini 3 Pro](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf)

---

## 5. Anthropic — Claude Opus 4.7 / Fable 5 & Mythos 5

### Claude Opus 4.7 System Card

- **中文标题**: Claude Opus 4.7 系统卡
- **英文标题**: Claude Opus 4.7 System Card
- **发布机构**: Anthropic
- **发布日期**: 2026-04-16
- **核心参数**: 1M 上下文, 128K 最大输出, AI Safety Level 3
- **主要创新点**:
  - SWE-bench Verified: 80.8% → 87.6%
  - SWE-bench Pro: 53.4% → 64.3%
  - XBOW 视觉精度: 54.5% → 98.5%
  - 长上下文检索出现退化 (8-needle @256k: 91.9% → 59.2%)
- **System Card**: [anthropic.com](https://anthropic.com/claude-opus-4-7-system-card)

### Claude Fable 5 & Mythos 5 System Card

- **中文标题**: Claude Fable 5 和 Claude Mythos 5 系统卡
- **英文标题**: Claude Fable 5 & Claude Mythos 5 System Card
- **发布机构**: Anthropic
- **发布日期**: 2026-06-09
- **核心参数**: Anthropic 迄今最强模型
- **主要创新点**:
  - Mythos 5: 无防护的极致能力版，仅限合作伙伴使用
  - Fable 5: 通用版本，带安全分类器
  - 网络安全能力显著提升
  - CB-1 级别能力（接近 CB-2 门槛）
- **System Card**: [Claude Fable 5 & Mythos 5 System Card (PDF)](https://www-cdn.anthropic.com/2f9323abbcc4abe219577539efe19a623c9ca2bd/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf)

---

## 6. Mistral AI — Mistral 3 系列

- **中文标题**: Mistral 3 介绍
- **英文标题**: Introducing Mistral 3
- **发布机构**: Mistral AI
- **模型名称**: Mistral Large 3 / Ministral 3 (14B, 8B, 3B) / Mistral Small 4
- **发布日期**: 2025-12-02 (Large 3), 2026-03-16 (Small 4)
- **核心参数**:
  - Mistral Large 3: 675B 总参数, 41B 激活, MoE, 256K 上下文
  - Mistral Small 4: 119B 总参数, ~6B 激活, 128 experts, 256K 上下文
  - Ministral 3: 密集模型 (14B/8B/3B)
  - 全部 Apache 2.0
- **主要创新点**:
  - Large 3: Mistral 首个 MoE 模型（继 Mixtral 之后）
  - Small 4: 统一推理 (Magistral) + 视觉 (Pixtral) + 编程 (Devstral) 三合一
  - 可配置推理 (configurable reasoning)
  - 与 NVIDIA 合作优化，支持 NVFP4 量化
- **公告**: [mistral.ai/news/mistral-3](https://mistral.ai/news/mistral-3/), [Mistral Small 4](https://mistral.ai/news/mistral-small-4/)

---

## 7. Alibaba Qwen — Qwen3

- **中文标题**: Qwen3 技术报告
- **英文标题**: Qwen3 Technical Report
- **发布机构**: Alibaba Cloud (Qwen Team)
- **模型名称**: Qwen3 系列 (0.6B ~ 235B)
- **发布日期**: 2025-04-29 (发布), 2025-05-14 (arXiv)
- **核心参数**:
  - Qwen3-235B-A22B: MoE, 235B 总 / 22B 激活, 128K 上下文
  - Qwen3-32B: 密集, 128K 上下文
  - Qwen3-30B-A3B: MoE, 30B 总 / 3B 激活, 128K 上下文
  - 支持 119 种语言和方言
  - Apache 2.0
- **主要创新点**:
  - 统一 thinking mode + non-thinking mode 框架
  - Thinking budget 机制：自适应分配推理计算
  - 密集 + MoE 双架构系列
  - 从 29 种语言扩展到 119 种
  - 代码生成、数学推理、Agent 任务 SOTA
- **arXiv**: [2505.09388](https://arxiv.org/abs/2505.09388)
- **后续**: Qwen3.5 系列 (2026-02), Qwen3-VL (2025-11), Qwen3-TTS (2026-01)

---

## 8. Microsoft — Phi-4 / Phi-4-Reasoning-Vision

### Phi-4 Technical Report

- **中文标题**: Phi-4 技术报告
- **英文标题**: Phi-4 Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4
- **发布日期**: 2024-12
- **核心参数**: 14B, 密集 decoder-only, 16K 上下文, 9.8T tokens, MIT
- **主要创新点**:
  - 数据质量优先于规模 — 40% 合成数据
  - 超越教师模型 GPT-4 (STEM QA)
  - 多智能体提示、Web 重写、自修订合成数据
  - 16K 上下文中训练扩展
- **arXiv**: [2412.08905](https://arxiv.org/abs/2412.08905)

### Phi-4-Reasoning-Vision-15B

- **中文标题**: Phi-4-Reasoning-Vision-15B 技术报告
- **英文标题**: Phi-4-Reasoning-Vision-15B Technical Report
- **发布机构**: Microsoft Research
- **发布日期**: 2026-03
- **核心参数**: 15B, 多模态 (文本+图像), 推理+非推理双模式
- **主要创新点**:
  - 小巧多模态推理模型
  - 系统性过滤、纠错和合成增强
  - 动态分辨率编码器
  - 推理/直接回答双模式
- **arXiv**: [2603.03975](https://arxiv.org/abs/2603.03975)

---

## 9. xAI — Grok 4

- **中文标题**: Grok 4
- **英文标题**: Grok 4
- **发布机构**: xAI
- **模型名称**: Grok 4 / Grok 4 Heavy / Grok 4 Mini
- **发布日期**: 2025-07-09
- **核心参数**:
  - Grok 4: 128K 上下文 (后扩展至 2M)
  - Grok 4 Heavy: 多智能体配置, 多并行推理链
  - 训练于 Colossus 超算 (200,000+ NVIDIA GPU)
  - 原生多模态
- **主要创新点**:
  - Humanity's Last Exam (HLE) 达 50.7% (Heavy 模式) — 首个超过 50% 的模型
  - ARC-AGI-2 达 15.9% — 接近 2 倍此前 SOTA
  - 多智能体推理架构
  - 集成 X 平台实时数据
  - 强化学习贯穿预训练
- **参考**: [Grok 4 AI Wiki](https://aiwiki.ai/wiki/grok_4)

---

## 10. NVIDIA — Nemotron 3 系列

- **中文标题**: NVIDIA Nemotron 3：混合 Mamba-Transformer MoE 推理模型
- **英文标题**: NVIDIA Nemotron 3: Hybrid Mamba-Transformer MoE Reasoning Model
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Nano / Super / Ultra
- **发布日期**: 2026 (持续更新)
- **核心参数**:
  - Ultra 550B-A55B: 550B 总 / 55B 激活, MoE
  - Super 49B: 基于 Llama-3.3
  - Nano 4B/8B: 紧凑推理模型
  - 1M 上下文 (部分型号)
- **主要创新点**:
  - 混合 Mamba-Transformer MoE 架构
  - Neural Architecture Search (NAS) 压缩
  - GRPO (Group Relative Policy Optimization) 多阶段 RL
  - 垂直模型压缩技术
  - 与 Mistral 合作 Nemotron 联盟
- **参考**: [NVIDIA Nemotron](https://developer.nvidia.com/topics/ai/nemotron), [Llama-3.1-Nemotron-Ultra-253B](https://build.nvidia.com/nvidia/llama-3_1-nemotron-ultra-253b-v1)

---

## 11. Apple — Apple Foundation Models (AFM) Tech Report 2025

- **中文标题**: Apple Intelligence 基础语言模型 2025 技术报告
- **英文标题**: Apple Intelligence Foundation Language Models: Tech Report 2025
- **发布机构**: Apple
- **模型名称**: AFM 3 Core / AFM 3 Core Advanced / AFM 3 Cloud / AFM 3 Cloud Pro
- **发布日期**: 2025-07-17 (Tech Report), 2026-06-08 (AFM 3 代)
- **核心参数**:
  - 端侧模型: ~3B 参数, KV-cache 共享, 2-bit 量化训练
  - 服务端: Parallel-Track MoE (PT-MoE), 多语言多模态
  - AFM 3 Core Advanced: 20B 总 / 1-4B 激活
  - 多语言 + 图像理解 + 工具调用
- **主要创新点**:
  - Parallel-Track Mixture-of-Experts (PT-MoE)
  - KV-cache 共享和 2-bit 量化感知训练
  - Private Cloud Compute 隐私保护
  - Swift Foundation Models 框架
  - 与 Google 合作，基于 Gemini 蒸馏
- **arXiv**: [2507.13575](https://arxiv.org/abs/2507.13575)
- **公告**: [Apple Machine Learning](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models)

---

## 12. Google DeepMind — Gemma 4

- **中文标题**: Gemma 4 12B：统一的无编码器多模态模型
- **英文标题**: Introducing Gemma 4 12B: a unified, encoder-free multimodal model
- **发布机构**: Google DeepMind
- **模型名称**: Gemma 4 12B
- **发布日期**: 2026-06
- **核心参数**: 12B, 无编码器多模态, 开源
- **主要创新点**: 无编码器 (encoder-free) 统一多模态架构
- **公告**: [Google DeepMind Blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)

---

## 关注要点总结

### 大模型新架构
| 公司 | 架构 | 特点 |
|------|------|------|
| DeepSeek V4 | MoE + CSA/HCA + mHC | KV cache 降至 10%, 1M 上下文 |
| Meta Llama 4 | MoE (首次) | 16/128 experts, 10M 上下文 |
| Mistral Large 3 | MoE | 128 experts, 256K 上下 |
| NVIDIA Nemotron 3 | Hybrid Mamba-Transformer MoE | SSM + Attention 混合 |
| Apple AFM 3 | PT-MoE | Parallel-Track MoE |

### 训练方法
- **Pre-training**: 数据质量 > 数据量 (Phi-4), 合成数据大规模使用
- **Post-training**: On-Policy Distillation (DeepSeek V4), GRPO (NVIDIA), 在线 RL (Llama 4)
- **Alignment**: Instruction Hierarchy (o3), AI Safety Level 3 (Claude), RSP 3.0 (Anthropic)

### Scaling Law
- DeepSeek V4 用更少激活参数超越更大模型
- Phi-4 证明小模型 + 高质量数据可超越教师模型
- Apple AFM 3 端侧模型 1-4B 激活参数实现强能力

### 多模态
- 大部分新模型原生多模态 (Llama 4, Gemini 2.5, Qwen3, o3, Claude 4)
- Early fusion 成为主流 (而非 bolt-on 视觉编码器)
- Apple AFM 3 支持文本 + 图像 + 语音

### 长上下文
| 模型 | 上下文长度 |
|------|-----------|
| Llama 4 Scout | 10M tokens |
| Llama 4 Maverick | 1M tokens |
| DeepSeek V4 | 1M tokens |
| Gemini 2.5 | 1M+ tokens |
| Claude 4.x | 1M tokens |
| Grok 4 | 2M tokens |
| Mistral Large 3 | 256K tokens |

### 推理模型 / Reasoning
- OpenAI o3/o4-mini: 推理 + 工具调用一体化
- DeepSeek V4-Pro-Max: 最大推理努力模式
- Gemini 2.5/3: Thinking 模式 + Deep Think
- Claude Opus 4.7+: 混合推理
- Qwen3: 统一 thinking + non-thinking 框架
- Mistral Small 4: 可配置推理
