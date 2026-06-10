---
title: 各大 AI 公司最新技术报告汇总 (第九版) — 2026-06-10
type: synthesis
created: 2026-06-10
updated: 2026-06-10
sources: []
tags: [tech-report, system-card, deepseek, openai, meta, google, anthropic, mistral, qwen, xai, microsoft, apple, nvidia, amazon, zhipu, kimi, bytedance, internlm]
---

# 各大 AI 公司最新技术报告汇总 (第九版)

> 覆盖 22+ 家机构，35+ 篇 Tech Report / System Card 最新动态。持续追踪大模型新架构、训练方法、Scaling Law、多模态、长上下文、推理模型六大方向。

---

## 目录

1. [DeepSeek — DeepSeek V4](#1-deepseek--deepseek-v4)
2. [OpenAI — GPT-5 / GPT-5.5 / GPT-5.1-Codex-Max](#2-openai--gpt-5--gpt-55--gpt-51-codex-max)
3. [Meta AI — Llama 4 / Muse Spark](#3-meta-ai--llama-4--muse-spark)
4. [Google DeepMind — Gemini 3.1 Pro / 3.5 / Omni](#4-google-deepmind--gemini-31-pro--35--omni)
5. [Anthropic — Claude Opus 4.8 / 4.7 / Mythos](#5-anthropic--claude-opus-48--47--mythos)
6. [Mistral AI — Mistral Large 3](#6-mistral-ai--mistral-large-3)
7. [Alibaba Qwen — Qwen3 / Qwen3.5 / Qwen3.6](#7-alibaba-qwen--qwen3--qwen35--qwen36)
8. [xAI — Grok 3 / 4 / 4.3](#8-xai--grok-3--4--43)
9. [Microsoft — Phi-4 / Phi-4-mini](#9-microsoft--phi-4--phi-4-mini)
10. [Apple — Apple Intelligence Foundation Language Models](#10-apple--apple-intelligence-foundation-language-models)
11. [NVIDIA — Nemotron 3 (Nano / Super / Ultra)](#11-nvidia--nemotron-3-nano--super--ultra)
12. [Amazon — Amazon Nova / Nova Premier](#12-amazon--amazon-nova--nova-premier)
13. [Zhipu AI (Z.ai) — GLM-5 / GLM-5.1](#13-zhipu-ai-zai--glm-5--glm-51)
14. [Moonshot AI (Kimi) — Kimi K2 / K2.5 / K2.6](#14-moonshot-ai-kimi--kimi-k2--k25--k26)
15. [ByteDance (Doubao/Seed) — Seed 1.8 / Seed 2.0](#15-bytedance-doubaoseed--seed-18--seed-20)
16. [Shanghai AI Lab — InternLM3](#16-shanghai-ai-lab--internlm3)
17. [StepFun (阶跃星辰) — Step 系列](#17-stepfun-阶跃星辰--step-系列)
18. [01.AI (Yi) — Yi 系列](#18-01ai-yi--yi-系列)
19. [Baichuan — Baichuan 系列](#19-baichuan--baichuan-系列)

---

## 1. DeepSeek — DeepSeek V4

- **中文标题**: DeepSeek V4 技术文档
- **英文标题**: DeepSeek V4 Technical Documentation
- **发布机构**: DeepSeek AI（深度求索）
- **模型名称**: DeepSeek-V4-Pro / DeepSeek-V4-Flash
- **发布日期**: 2026年4月24日
- **核心参数**:
  - V4-Pro: 1.6T 总参数 (MoE), 49B 激活参数/token, 1M context, 33T tokens 训练数据
  - V4-Flash: 284B 总参数 (MoE), 13B 激活参数/token, 1M context, 33T tokens 训练数据
  - 注意力机制: Hybrid CSA (Compressed Sparse Attention) + HCA (Heavily Compressed Attention)
  - 优化器: Muon (AdamW for embeddings)
  - 许可证: MIT
  - 推理模式: Non-think / Think High / Think Max
- **主要创新点**:
  - CSA 压缩 KV cache 4x 后做稀疏 attention；HCA 做 128x 压缩后做稠密 attention
  - Manifold-Constrained Hyper-Connections (mHC): 将残差映射约束在双随机矩阵流形上
  - Muon 优化器加速收敛
  - V4-Pro 相比 V3.2 在 1M context 下 FLOPs 降至 27%、KV cache 降至 10%
  - V4-Pro-Max: SWE-bench Verified 80.6%, LiveCodeBench 93.5
  - 多 token 预测 (MTP) 策略延续自 V3
- **论文链接**: [DeepSeek V4 Model Card PDF](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)

## 2. OpenAI — GPT-5 / GPT-5.5 / GPT-5.1-Codex-Max

### GPT-5 System Card

- **英文标题**: GPT-5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-thinking-pro etc.)
- **发布日期**: 2025年8月7日
- **核心参数**:
  - 统一路由系统: fast model (main) + deep reasoning model (thinking) + real-time router
  - Router 持续训练，基于用户切换、偏好率、正确性度量
  - 所有 GPT-5 模型支持 safe-completions 安全训练方法
- **主要创新点**:
  - 从 hard refusal 转向 safe-completions: 输出中心安全训练
  - 减少 hallucination、improve instruction following、minimize sycophancy
  - 三层模型设计 (main / thinking / mini) 统一路由
  - Preparedness Framework: Biology (High), Cybersecurity, AI Self-Improvement 评估
  - GPT-5-thinking 视为 o3 继任者
- **论文链接**: [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) | [System Card](https://openai.com/index/gpt-5-system-card)

### GPT-5.5

- **英文标题**: Introducing GPT-5.5
- **发布机构**: OpenAI
- **模型名称**: GPT-5.5 / GPT-5.5 Pro
- **发布日期**: 2026年4月23日
- **主要创新点**:
  - 最强 agentic coding、computer use、knowledge work、early scientific research
  - 匹配 GPT-5.4 延迟但显著更智能
  - 更少 tokens 完成相同 Codex 任务
  - 最大规模安全防护升级: 内外红队测试、~200 早期合作伙伴反馈
- **论文链接**: [Blog](https://openai.com/index/introducing-gpt-5-5)

### GPT-5.1-Codex-Max System Card

- **英文标题**: GPT-5.1-Codex-Max System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5.1-Codex-Max
- **发布日期**: 2025年11月19日
- **主要创新点**:
  - 首个原生多 context window 训练模型 (compaction 技术)
  - 可处理数百万 tokens 的单个任务
  - 专注于 agentic coding: PR creation, code review, frontend coding
  - Cybersecurity domain 非常强但不达 High threshold
- **论文链接**: [System Card](https://openai.com/index/gpt-5-1-codex-max-system-card)

## 3. Meta AI — Llama 4 / Muse Spark

### Llama 4 系列

- **英文标题**: The Llama 4 Herd of Models
- **发布机构**: Meta AI (Meta)
- **模型名称**: Llama 4 Scout / Maverick / Behemoth (shelved)
- **发布日期**: 2025年4月 (初始发布)
- **核心参数**:

| 模型 | 总参数 | 激活参数 | Context | 架构 | 状态 |
|------|--------|---------|---------|------|------|
| Scout | 109B | 17B | 10M tokens | MoE, 16 experts | ✅ 已发布 |
| Maverick | 400B | 17B | 1M tokens | MoE, 128 experts | ✅ 已发布 |
| Behemoth | ~2T | 288B | TBD | MoE, 16 experts | ❌ 搁置 |

- **主要创新点**:
  - Meta 首个 MoE 架构系列，早期融合多模态 (text+image)
  - Scout 10M context window — 最长开源 context
  - Behemoth 作为 teacher model 做 codistillation
  - SFT + online RL + DPO 多阶段 post-training
  - FP8 训练
- **论文链接**: [Meta Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence)

### Muse Spark

- **英文标题**: Muse Spark
- **发布机构**: Meta Superintelligence Labs (MSL)
- **发布日期**: 2026年4月8日
- **特点**: Meta 首个 closed-weight 推理模型，API-only
- **主要创新点**:
  - 原生多模态推理 + tool-use + visual chain-of-thought + multi-agent orchestration
  - Index 52 on Artificial Analysis (第4)
  - HealthBench Hard 42.8 (领先 Gemini 3.1 Pro 的 20.6)
  - 无开放权重、无架构论文

## 4. Google DeepMind — Gemini 3.1 Pro / 3.5 / Omni

### Gemini 3.1 Pro

- **英文标题**: Gemini 3.1 Pro - Model Card
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 3.1 Pro
- **发布日期**: 2026年2月19日
- **核心参数**:
  - 1M token context window
  - 原生多模态输入 (text + image + audio + video + code)
  - Sparse MoE Transformer 架构
  - Thinking mode: High / Max
- **主要创新点**:
  - ARC-AGI-2: 77.1% (vs GPT-5.2 52.9%)
  - GPQA Diamond: 94.3%
  - Humanity's Last Exam: 44.4% (no tools), 51.4% (with tools)
  - SWE-bench Verified: 80.6%
  - Terminal-Bench 2.0: 68.5%
  - LiveCodeBench Pro Elo: 2887
- **论文链接**: [Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)

### Gemini 3.5

- **发布机构**: Google DeepMind
- **发布日期**: 2026年5月
- **特点**: Frontier intelligence with action — 最新旗舰系列
- **论文链接**: [Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

### Gemini Omni

- **发布机构**: Google DeepMind
- **发布日期**: 2026年5月
- **特点**: Create anything from anything — 视频输入/输出多模态

## 5. Anthropic — Claude Opus 4.8 / 4.7 / Mythos

### Claude Opus 4.8

- **英文标题**: Claude Opus 4.8 System Card
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 4.8
- **发布日期**: 2026年5月28日
- **核心参数**:
  - 1M context window, 128K max output tokens
  - 输入 $5/M, 输出 $25/M
  - AI Safety Level 3
- **主要创新点**:
  - SWE-Bench Pro: 69.2% (+4.9% vs 4.7)
  - Terminal-Bench 2.1: 74.6% (+8.5%)
  - Humanity's Last Exam: 49.8% (no tools), 57.9% (with tools)
  - OSWorld-Verified: 83.4% (+5.4%)
  - Finance Agent v2: 53.9%
  - GDPval-AA: 1890 (+137)
- **论文链接**: [System Card](https://anthropic.com/claude-opus-4-8-system-card)

### Claude Opus 4.7

- **英文标题**: Claude Opus 4.7 System Card
- **发布机构**: Anthropic
- **发布日期**: 2026年4月16日
- **主要创新点**:
  - SWE-bench Verified: 87.6% (from 80.8%)
  - SWE-bench Pro: 64.3% (from 53.4%)
  - 视觉分辨率提升 3x
  - 长 context 检索有退化 (MRCR 8-needle @ 256K: 59.2% vs 4.6 的 91.9%)
  - 232 页 system card
- **论文链接**: [System Card](https://anthropic.com/claude-opus-4-7-system-card)

### Claude Mythos Preview

- **发布机构**: Anthropic
- **发布日期**: 2026年4月
- **特点**: Anthropic 最强内部对齐模型，未广泛发布，244 页 system card
- **论文链接**: [System Card](https://www.anthropic.com/claude-mythos-preview-system-card)

### Claude Opus 4.6 / Sonnet 4.6

- **发布日期**: 2026年2月
- **Sonnet 4.6 中文标题**: Claude Sonnet 4.6 System Card
- **Opus 4.6 主要指标**: SWE-bench Verified 80.8%, 1M context
- **论文链接**: [Opus 4.6](http://anthropic.com/claude-opus-4-6-system-card) | [Sonnet 4.6](http://anthropic.com/claude-sonnet-4-6-system-card)

## 6. Mistral AI — Mistral Large 3

- **中文标题**: Mistral 3 发布 / Mistral Large 3 技术规格
- **英文标题**: Introducing Mistral 3 / Mistral Large 3
- **发布机构**: Mistral AI
- **模型名称**: Mistral Large 3 (675B MoE) / Ministral 3 (14B/8B/3B)
- **发布日期**: 2025年12月2日
- **核心参数**:
  - Mistral Large 3: 675B 总参数 (sparse MoE), 41B 激活参数, 256K context
  - 在 ~3000 NVIDIA H200 GPU 上训练
  - Apache 2.0 许可证
  - NVFP4 量化版本可在单节点 8×A100/H100 运行
- **主要创新点**:
  - Mistral 首个 MoE 大模型 (自 Mixtral 系列以来)
  - LMArena OSS 非推理模型 #2
  - MMLU (8-language): ~85.5%
  - HumanEval pass@1: ~92%
  - 多语言能力领先 (非英/中场景最强)
  - 支持文本+图像多模态
- **论文链接**: [Blog](https://mistral.ai/news/mistral-3/) | [HuggingFace](https://huggingface.co/collections/mistralai/mistral-large-3)

## 7. Alibaba Qwen — Qwen3 / Qwen3.5 / Qwen3.6

### Qwen3

- **中文标题**: Qwen3 技术报告
- **英文标题**: Qwen3 Technical Report
- **发布机构**: Alibaba Cloud (阿里巴巴通义千问团队)
- **模型名称**: Qwen3 (0.6B ~ 235B, Dense + MoE)
- **发布日期**: 2025年5月14日
- **核心参数**:
  - 参数范围: 0.6B (dense) ~ 235B (MoE, 激活参数待确认)
  - 训练数据: 36T tokens (119 种语言)
  - 架构: Dense + MoE 双架构可选
  - 许可证: Apache 2.0
  - 多语言支持从 29→119 语言/方言
- **主要创新点**:
  - Thinking + Non-thinking 双模式统一框架 (无需切换模型)
  - Thinking budget 机制: 用户可根据任务复杂度分配推理计算
  - Strong-to-weak distillation: 从旗舰模型蒸馏到小模型
  - 长 CoT 冷启动数据 + 两阶段过滤
  - 在 code、math、agent 任务上达到 SOTA
- **论文链接**: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) | [PDF](https://arxiv.org/pdf/2505.09388)

### Qwen3.6-Plus

- **发布日期**: 2026年 (后续版本)
- **核心参数**: 1M token context, 支持 201 种语言
- 全球下载量接近 10亿，占开源模型下载量 50%+

## 8. xAI — Grok 3 / 4 / 4.3

### Grok 3

- **英文标题**: Grok 3
- **发布机构**: xAI
- **模型名称**: Grok 3 / Grok 3 Mini
- **发布日期**: 2025年2月17日
- **核心参数**:
  - 训练使用 Colossus 集群 (200,000+ GPU)
  - 10x 前代计算资源
  - 1M context window
  - Think Mode (Big Brain Mode) + DeepSearch
- **主要创新点**:
  - 大规模 RL 训练推理能力
  - AIME 2025: 93.3%, GPQA: 84.6%, LiveCodeBench: 79.4%
  - LMArena 1402 ELO (launch)
  - 实时 X (Twitter) 数据集成
- **论文链接**: [x.ai/news/grok-3](https://x.ai/news/grok-3)

### Grok 4.3

- **英文标题**: Grok 4.3
- **发布机构**: xAI
- **发布日期**: 2026年4月30日
- **核心参数**:
  - 1M context window
  - 推理配置: none/low/medium/high
  - 输入 $1.25/M, 输出 $2.50/M
- **主要创新点**: Agentic workflows, long-document analysis, deep research

## 9. Microsoft — Phi-4 / Phi-4-mini

### Phi-4

- **中文标题**: Phi-4 技术报告
- **英文标题**: Phi-4 Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4 (14B)
- **发布日期**: 2024年12月12日
- **核心参数**:
  - 14B 参数 (Dense)
  - Context: 16K tokens
  - 训练核心: 数据质量 > 数据数量
- **主要创新点**:
  - 策略性使用合成数据 (超越 teacher model GPT-4 的 STEM 能力)
  - "Textbooks Are All You Need" 路线延续
  - MATH: 80.4%, GPQA Diamond 超越 GPT-4o
  - Pivotal Token DPO 训练
- **论文链接**: [arXiv:2412.08905](https://arxiv.org/abs/2412.08905)

### Phi-4-mini-instruct

- **发布机构**: Microsoft
- **发布日期**: 2025年2月
- **核心参数**: 128K context window, 轻量级
- **许可证**: MIT

## 10. Apple — Apple Intelligence Foundation Language Models

- **中文标题**: Apple Intelligence 基础语言模型
- **英文标题**: Apple Intelligence Foundation Language Models
- **发布机构**: Apple
- **模型名称**: AFM-on-device (~3B) / AFM-server (large)
- **发布日期**: 2024年7月 (v1) / 2025年7月 (v2 Tech Report)
- **核心参数**:
  - On-device: ~3B 参数, 量化至 <4-bit
  - Server: 大模型, Private Cloud Compute 部署
  - 训练: 8192 TPUv4 (server), 2048 TPUv5p (on-device)
  - LoRA adapter 架构: 每个功能独立 adapter
- **主要创新点**:
  - KV-cache sharing + 2-bit quantization-aware training
  - 2025 版本: Parallel-Track Mixture-of-Experts (PT-MoE) transformer
  - iTeC (rejection sampling with teacher committee)
  - MDLOO (mirror descent policy optimization + leave-one-out advantage)
  - 设备端隐私优先设计
- **论文链接**: [arXiv:2407.21075](https://arxiv.org/abs/2407.21075) | [2025 Tech Report](https://machinelearning.apple.com/research/apple-intelligence-foundation-language-models)

## 11. NVIDIA — Nemotron 3 (Nano / Super / Ultra)

### Nemotron 3 Family

- **英文标题**: NVIDIA Nemotron 3 Family
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Nano (30B) / Super (120B) / Ultra (550B)
- **发布日期**: 2025年12月15日 (Nano/Super) / 2026年6月4日 (Ultra)
- **核心参数**:

| 模型 | 总参数 | 激活参数 | Context | 架构 |
|------|--------|---------|---------|------|
| Nano 4B | 30B | 3.5B | 1M | MoE Hybrid Mamba2-Transformer (23 Mamba2/MoE + 6 Attn) |
| Super | 120B | 12B | 1M | MoE Hybrid Mamba-Attention |
| Ultra | 550B | 55B | 1M | MoE Hybrid Mamba-Attention + LatentMoE |

- **主要创新点**:
  - **Hybrid Mamba-Attention**: Mamba 层亚二次方扩展 + Attention 层精确召回
  - **LatentMoE** (Ultra): 提升 accuracy per active parameter
  - **Multi-teacher On-Policy Distillation (MOPD)**: 10+ 专用 teacher 蒸馏到一个 student
  - **MTP 层**: 原生推测解码加速推理
  - **NVFP4 预训练**: 单个 NVFP4 checkpoint 同时支持 Blackwell/Hopper/Ampere
  - **Reasoning budget control**: 推断时可配置推理深度
  - 预训练 20T tokens，长上下文扩展到 1M
  - Ultra: 5.9x 吞吐量提升 vs GLM-5.1 (8K/64K 设定)
  - AA-Omniscience 非幻觉评分 78.7 (最高)
  - 许可证: OpenMDW-1.1 (开放权重、数据、recipe)
- **论文链接**: [Ultra Tech Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) | [Nano 2](https://arxiv.org/abs/2508.14444)

## 12. Amazon — Amazon Nova / Nova Premier

- **中文标题**: Amazon Nova 模型家族：技术报告与模型卡
- **英文标题**: The Amazon Nova Family of Models: Technical Report and Model Card
- **发布机构**: Amazon (AWS)
- **模型名称**: Amazon Nova Micro / Lite / Pro / Premier / Canvas / Reel / Sonic
- **发布日期**: 2024年12月3日 (初版) / 2025年4月30日 (Premier)
- **核心参数**:
  - Nova Pro: 多模态 (text+image+video), 高精度/速度/成本平衡
  - Nova Lite: 低价多模态, 快速处理 image/video/document
  - Nova Micro: 纯文本, 最低延迟
  - Nova Premier: 最强多模态, 1M context window
  - Nova Canvas: 图像生成
  - Nova Reel: 视频生成
- **主要创新点**:
  - Premier 作为 teacher model 做模型蒸馏
  - Nova Pro 可蒸馏到 Micro/Lite
  - Bedrock 原生集成
  - Agentic performance、long context、functional adaptation 全面评估
- **论文链接**: [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) | [Amazon Science](https://www.amazon.science/publications/the-amazon-nova-family-of-models-technical-report-and-model-card) | [Premier](https://www.amazon.science/publications/amazon-nova-premier-technical-report-and-model-card)

## 13. Zhipu AI (Z.ai) — GLM-5 / GLM-5.1

### GLM-5

- **中文标题**: GLM-5：从 Vibe Coding 到 Agentic Engineering
- **英文标题**: GLM-5: From Vibe Coding to Agentic Engineering
- **发布机构**: Zhipu AI (智谱AI) / Z.ai
- **模型名称**: GLM-5 / GLM-5.1 / GLM-5V-Turbo
- **发布日期**: 2026年2月11日 (GLM-5) / 2026年4月8日 (GLM-5.1)
- **核心参数**:
  - GLM-5: 744B 总参数 (MoE), 40B 激活, 128K context, 训练 28.5T tokens
  - GLM-5.1: ~754B 总参数, ~42B 激活, 128K context
  - 许可证: MIT
  - 集成 DeepSeek Sparse Attention (DSA)
- **主要创新点**:
  - 异步 RL 基础设施 (slime): 大幅提升 RL 训练吞吐
  - GLM-5.1 可自主工作长达 8 小时
  - SWE-bench Verified: 77.8%, SWE-bench Pro: 58.4% (超越 GPT-5.4 57.7%)
  - Vending Bench 2: #1 开源 ($4,432 最终账户余额)
  - CC-Bench-V2: 接近 Claude Opus 4.5
  - 专注 long-horizon agentic tasks
- **论文链接**: [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) | [Blog](https://z.ai/blog/glm-5) | [GitHub](https://github.com/zai-org/GLM-5)

## 14. Moonshot AI (Kimi) — Kimi K2 / K2.5 / K2.6

### Kimi K2 / K2 Thinking

- **中文标题**: Kimi K2: 开放 Agentic Intelligence
- **英文标题**: Kimi K2: Open Agentic Intelligence
- **发布机构**: Moonshot AI (月之暗面)
- **模型名称**: Kimi K2 / K2 Thinking / K2.5 / K2.6
- **发布日期**: 2025年7月 (K2) / 2025年11月 (K2 Thinking) / 2026年1月 (K2.5) / 2026年4月 (K2.6)
- **核心参数**:
  - K2/K2.5/K2.6: 1.04T~1.1T 总参数 (MoE), 32B 激活参数
  - 384 experts (8 active + 1 shared), 61 layers
  - Multi-head Latent Attention (MLA)
  - 262K context window (K2.6)
  - 400M MoonViT 视觉编码器 (K2.5+)
  - K2 预训练 15.5T tokens
- **主要创新点**:
  - **MuonClip 优化器**: Muon update + QK-Clip 防止 attention logit 爆炸
  - **自批判 rubric reward**: 将 RLVR 扩展到主观任务
  - **Synthetic agentic data pipeline**: ~20,000 工具, 数千 agents, 多轮 rubric 评估
  - **Agent Swarm**: K2.6 支持 300 sub-agents, 4000 steps
  - SWE-bench Pro: 58.6% (K2.6, 领先 GPT-5.4 57.7%)
  - HLE-Full (with tools): 54.0% (领先)
  - 训练成本仅 $4.6M (K2 Thinking)
  - 修改 MIT 许可证
- **论文链接**: [K2 技术报告](https://moonshotai.github.io/Kimi-K2/) | [K2 Thinking](https://moonshotai.github.io/Kimi-K2/thinking.html)

## 15. ByteDance (Doubao/Seed) — Seed 1.8 / Seed 2.0

### Seed 1.8

- **中文标题**: Seed1.8 模型卡：迈向通用真实世界代理
- **英文标题**: Seed1.8 Model Card: Towards Generalized Real-World Agency
- **发布机构**: ByteDance Seed (字节跳动)
- **模型名称**: Seed1.8 (Pro / Lite / Mini)
- **发布日期**: 2025年 (Seed1.8) / 2026年2月 (Seed2.0)
- **核心参数**:
  - 多模态 (text + image + video + code)
  - 可配置 thinking modes
  - 为 Agentic 交互而设计: search, code execution, GUI interaction
- **主要创新点**:
  - 统一 agentic interface: 单模型内集成 perception + reasoning + action
  - 优化视觉编码减少 image/video token 消耗
  - LMSYS Chatbot Arena 高分
- **论文链接**: [Seed1.8 Model Card PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/research/Seed-1.8-Modelcard.pdf)

### Seed 2.0

- **英文标题**: Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity
- **发布机构**: ByteDance Seed
- **模型名称**: Seed2.0 Pro / Lite / Mini
- **发布日期**: 2026年2月14日
- **核心参数**:
  - 三个尺寸 (Pro / Lite / Mini) 满足不同场景
  - 强多模态理解 + 复杂指令执行
  - 支持 Erdos problems + Scientific Coding
- **主要创新点**:
  - 向 research-level reasoning 推进
  - 降低视觉幻觉
  - DS (Doubao) 日消费 120 万亿 tokens, 200M+ DAUs
- **论文链接**: [Seed2.0 Model Card PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/seed2/0214/Seed2.0%20Model%20Card.pdf)

## 16. Shanghai AI Lab — InternLM3

- **中文标题**: InternLM3 技术报告
- **英文标题**: InternLM3 Technical Report
- **发布机构**: Shanghai AI Laboratory (上海人工智能实验室)
- **模型名称**: InternLM3-8B-Instruct
- **发布日期**: 2025年1月15日
- **核心参数**:
  - 8B 参数 (Dense)
  - 训练仅 4T tokens (达到传统 18T 效果, 节省 75% 成本)
  - 许可证: Apache-2.0
- **主要创新点**:
  - 精炼数据框架 (Refined Data Framework): 4T 数据达到 18T 效果
  - 首次在通用模型中融合 deep thinking (长 CoT) + 常规对话能力
  - MMLU: 76.6, GPQA-Diamond: 37.4, MATH-500: 83.0, AIME2024: 20.0
- **论文链接**: [GitHub](https://github.com/InternLM/InternLM) | [arXiv:2403.17297](https://arxiv.org/abs/2403.17297)

## 17. StepFun (阶跃星辰) — Step 系列

- **发布机构**: StepFun (阶跃星辰)
- **模型名称**: Step-3 / Step-3.7 Flash
- **发布日期**: 2026年 (Step-3.7 Flash)
- **核心参数**: 多模态模型
- **特点**: 中文大模型新锐, 侧重多模态理解与生成

## 18. 01.AI (Yi) — Yi 系列

- **发布机构**: 01.AI (零一万物)
- **模型名称**: Yi-1.5 (9B/34B/etc.)
- **发布日期**: 2024年 (后续版本持续更新)
- **核心参数**: 开源 bilingual (中英) 模型系列
- **论文链接**: [GitHub](https://github.com/01-ai/Yi)

## 19. Baichuan — Baichuan 系列

- **发布机构**: Baichuan Intelligence (百川智能)
- **模型名称**: Baichuan 系列
- **发布日期**: 持续更新
- **核心参数**: 开源中英双语大模型
- **特点**: 侧重医疗、法律等垂直领域

---

## 六大方向总结

### 1. 大模型新架构 (MoE, Mamba, Hybrid)

- **MoE 成为主流**: DeepSeek V4, Llama 4, Qwen3, Mistral Large 3, GLM-5, Kimi K2/K2.6, Nemotron 3 全线 MoE
- **Hybrid Mamba-Transformer**: NVIDIA Nemotron 3 是最大规模 Hybrid 部署 (Mamba2 + Attention + MoE)
- **压缩注意力**: DeepSeek V4 CSA/HCA, GLM-5 DSA

### 2. 训练方法 (Pre-training, Post-training, Alignment, RL)

- **Muon 优化器**: DeepSeek V4 (Muon), Kimi K2 (MuonClip) — 替代 AdamW 的趋势
- **多阶段后训练**: SFT + RL + DPO + RLHF 已是标配
- **多 teacher 蒸馏**: NVIDIA MOPD (10+ teachers), Amazon Nova Premier distillation, Llama 4 codistillation
- **异步 RL**: GLM-5 slime 框架
- **Safe-completions**: OpenAI GPT-5 从 hard refusal 转向 output-centric safety

### 3. Scaling Law / 缩放分析

- DeepSeek V4, Kimi K2, GLM-5 均报告了 sparsity scaling law
- 开源模型参数规模持续增长: DeepSeek V4 1.6T, Kimi K2.6 1.1T, GLM-5 744B, Nemotron 3 Ultra 550B

### 4. 多模态模型

- Claude Opus 4.7/4.8: 视觉分辨率 3x 提升
- Kimi K2.5/K2.6: 原生多模态 (MoonViT encoder)
- Google Gemini 3.1/3.5/Omni: 最全多模态 (text+image+audio+video+code)
- Amazon Nova: 理解 + 生成 (Canvas + Reel)
- ByteDance Seed: 视觉+语言 unified

### 5. 长上下文模型

| 模型 | Context 长度 |
|------|-------------|
| Llama 4 Scout | 10M |
| DeepSeek V4 Pro | 1M |
| Gemini 3.1/3.5 | 1M |
| Claude Opus 4.x | 1M |
| Nemotron 3 Ultra | 1M |
| Amazon Nova Premier | 1M |
| Kimi K2.6 | 262K |
| GLM-5 | 128K |

### 6. 推理模型 / Reasoning Model

- **GPT-5 thinking + router**: 自动路由 fast vs deep reasoning
- **Claude Opus 4.x**: hybrid reasoning, extended thinking mode
- **DeepSeek V4**: Non-think / Think High / Think Max 三级推理
- **Qwen3**: Thinking + Non-thinking 统一框架 + thinking budget
- **Kimi K2.5/K2.6**: Thinking + Instant 双模式
- **Nemotron 3**: 推理 budget control
- **Grok 4.3**: 四级推理配置 (none/low/medium/high)
- **InternLM3**: 首次在通用模型融合 deep thinking + 常规对话
