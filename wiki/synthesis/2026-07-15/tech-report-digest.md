---
title: "LLM Tech Report Digest 2026 — 各大AI公司最新大模型技术报告汇总"
type: synthesis
created: 2026-07-15
updated: 2026-07-15
sources: [web-search]
tags: [tech-report, llm, moe, reasoning, multimodal, long-context, scaling-law, rl, alignment]
---

# LLM Tech Report Digest 2026 — 各大AI公司最新大模型技术报告汇总

> 2026-07-15 更新，覆盖 19 家主要 AI 机构/公司的最新技术报告。

---

## 1. DeepSeek（深度求索）

### DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **中文标题**: DeepSeek-V4：迈向高效百万Token上下文智能
- **英文标题**: DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4-Pro (1.6T/49B active)、DeepSeek-V4-Flash (284B/13B active)
- **发布日期**: 2026-06 (preview)
- **核心参数**:
  - V4-Pro: 1.6T total, 49B activated, 33T tokens pre-training
  - V4-Flash: 284B total, 13B activated, 32T tokens pre-training
  - 上下文长度: 1M tokens
  - MoE 架构，routed expert 使用 FP4 精度
- **主要创新点**:
  - **混合注意力架构**: CSA (Compressed Sparse Attention) + HCA (Heavily Compressed Attention) 交替使用，1M token 上下文下仅需 V3.2 的 27% 推理 FLOPs 和 10% KV cache
  - **Manifold-Constrained Hyper-Connections (mHC)**: 增强传统残差连接
  - **Muon 优化器**: 更快收敛和更好训练稳定性
  - 高效长上下文：使百万 token 上下文成为实践可行
- **链接**: [arXiv:2606.19348](https://arxiv.org/abs/2606.19348)、[HuggingFace](https://huggingface.co/collections/deepseek-ai/deepseek-v4)

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **中文标题**: DeepSeek-R1：通过强化学习激发LLM推理能力
- **英文标题**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-R1-Zero、DeepSeek-R1
- **发布日期**: 2025-01
- **核心参数**:
  - 基于 DeepSeek-V3-Base
  - 开源 1.5B/7B/8B/14B/32B/70B 蒸馏模型 (基于 Qwen/Llama)
- **主要创新点**:
  - **纯 RL 训练**: R1-Zero 无需 SFT 预步骤，通过 GRPO 直接 RL 训练即涌现推理能力
  - **多阶段训练流程**: 冷启动 SFT → 推理导向 RL → 拒绝采样生成新 SFT 数据 → 二次 RL
  - **语言一致性奖励**: 解决 CoT 语言混合问题
  - **蒸馏**: 800K 推理数据蒸馏至小模型，14B 超越 QwQ-32B-Preview
  - AIME 2024 pass@1: 15.6% → 71.0% (R1-Zero)，匹配 o1-0912
- **链接**: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)

### DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
- **中文标题**: DeepSeek-V3.2：推进开源大语言模型前沿
- **英文标题**: DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V3.2
- **发布日期**: 2025-12
- **核心参数**: 671B total, MoE, 128K context
- **主要创新点**: 高计算效率与强推理/Agent 性能的统一；DeepSeek Sparse Attention (DSA)
- **链接**: [arXiv:2512.02556](https://arxiv.org/abs/2512.02556)

---

## 2. OpenAI

### GPT-5 System Card
- **中文标题**: GPT-5 系统卡片
- **英文标题**: GPT-5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5
- **发布日期**: 2025-08 (系统卡片 2025-12 发布)
- **核心参数**: 统一系统 (smart + fast)，具体参数量未公开
- **主要创新点**:
  - 统一架构：智能与速度兼备
  - 多模态能力
  - 推理能力大幅提升
- **链接**: [arXiv:2601.03267](https://arxiv.org/abs/2601.03267)

### GPT-5.6 System Card
- **中文标题**: GPT-5.6 系统卡片
- **英文标题**: GPT-5.6 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5.6
- **发布日期**: 2026-07-10
- **核心参数**: 具体未公开
- **主要创新点**: 部署安全评估、风险缓解措施
- **链接**: [deploymentsafety.openai.com/gpt-5-6](https://deploymentsafety.openai.com/gpt-5-6)

### GPT-Live System Card
- **中文标题**: GPT-Live 系统卡片
- **英文标题**: GPT-Live System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-Live
- **发布日期**: 2026-07-08
- **核心参数**: 实时多模态交互
- **链接**: [deploymentsafety.openai.com/gpt-live](https://deploymentsafety.openai.com/gpt-live)

---

## 3. Meta AI (LLaMA)

### The Llama 4 Herd
- **中文标题**: Llama 4 家族：架构、训练、评估与部署
- **英文标题**: The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes
- **发布机构**: Meta AI
- **模型名称**: Llama 4 Scout (109B/17B active, 16 experts)、Llama 4 Maverick (400B/17B active, 128 experts)、Llama 4 Behemoth (2T/288B active, 16 experts)
- **发布日期**: 2025-04 (Scout/Maverick)，Behemoth 预告中
- **核心参数**:
  - Scout: 109B total, 17B active, 16 experts, 10M context length
  - Maverick: 400B total, 17B active, 128 experts, 256K context
  - Behemoth: ~2T total, 288B active, 16 experts
  - 原生多模态，早期融合
- **主要创新点**:
  - **iRoPE 架构**: 交错注意力层（无位置编码）+ RoPE 层，实现 10M 上下文长度泛化
  - **MoE 架构首次应用**: 交替 Dense/MoE 层，高效推理
  - **原生多模态 (Early Fusion)**: 文本+视觉 token 统一预训练
  - **Codistillation**: Behemoth 教师模型→Maverick 蒸馏，动态加权软/硬目标
  - **后训练**: 轻量 SFT + Online RL + 轻量 DPO
- **链接**: [Meta AI Blog](https://ai.meta.com/blog/Llama-4-multimodal-intelligence/)、[arXiv:2601.11659](https://arxiv.org/abs/2601.11659)

---

## 4. Google DeepMind (Gemini)

### Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **中文标题**: Gemini 2.5：以高级推理、多模态、长上下文和下一代Agent能力推进前沿
- **英文标题**: Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 2.5 Pro、Gemini 2.5 Flash、Gemini 2.0 Flash、Gemini 2.0 Flash-Lite
- **发布日期**: 2025-07
- **核心参数**:
  - Gemini 2.5 Pro: 最强模型，3小时视频处理，1M+ context
  - 跨越能力-成本 Pareto 前沿
- **主要创新点**:
  - **Thinking 模型**: Gemini 2.5 Pro 支持推理思考模式
  - **超长视频理解**: 最长 3 小时视频
  - **Agent 工作流**: 联合长上下文+多模态+推理能力驱动 agentic 工作流
  - **推理时间 Scaling**: Deep Think 模式实现 IMO 金牌水平
  - Aider Polyglot 5x 提升 (一年内)，SWE-bench 2x 提升
- **链接**: [arXiv:2507.06261](https://arxiv.org/abs/2507.06261)

---

## 5. Anthropic (Claude)

### Claude Fable 5 & Claude Mythos 5 System Card
- **中文标题**: Claude Fable 5 与 Claude Mythos 5 系统卡片
- **英文标题**: Claude Fable 5 & Claude Mythos 5 System Card
- **发布机构**: Anthropic
- **模型名称**: Claude Mythos 5（受限访问）、Claude Fable 5（通用访问）
- **发布日期**: 2026-06-09
- **核心参数**: 具体未公开，两个版本共享底层权重
- **主要创新点**:
  - **双版本发布**: Mythos 5（无安全限制，限 Project Glasswing 合作伙伴）/ Fable 5（通用版，附加网络安全+生物+蒸馏分类器）
  - **自主性风险评估**: 重新评估能力阈值
  - **ASL-3 安全等级**
  - **化学/生物风险评估**: CB-1 和 CB-2 威胁模型
  - **对齐评估**: 与 Claude Mythos Preview 相当
- **链接**: [anthropic.com/system-cards](https://www.anthropic.com/system-cards)

### Claude Opus 4.8 System Card
- **中文标题**: Claude Opus 4.8 系统卡片
- **英文标题**: Claude Opus 4.8 System Card
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 4.8
- **发布日期**: 2026-05-28
- **核心参数**: Anthropic 最强通用模型
- **主要创新点**:
  - 软件工程、Agent 工具使用、知识工作能力提升
  - 不超越 Claude Mythos Preview 能力前沿
  - 生物风险评估未超过 Mythos Preview
- **链接**: [anthropic.com (PDF)](https://www-cdn.anthropic.com/0f0c97ad20d8005706296bd92aa1c27c6b2f4f61.pdf)

### Claude Opus 4 & Claude Sonnet 4 System Card
- **中文标题**: Claude Opus 4 与 Claude Sonnet 4 系统卡片
- **英文标题**: System Card: Claude Opus 4 & Claude Sonnet 4
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 4 (ASL-3)、Claude Sonnet 4 (ASL-2)
- **发布日期**: 2025-05
- **主要创新点**:
  - **混合推理模型**: 推理+视觉分析+计算机使用+工具使用
  - **首次完整对齐评估**: 涵盖多种错位风险
  - **模型福利评估**: 首次纳入
  - Opus 4 在 CBRN 评估中显示显著能力提升
- **链接**: [anthropic.com/claude-4-model-card](http://anthropic.com/claude-4-model-card)

---

## 6. Mistral AI

### Mistral Small 4
- **中文标题**: Mistral Small 4
- **英文标题**: Introducing Mistral Small 4
- **发布机构**: Mistral AI
- **模型名称**: Mistral Small 4
- **发布日期**: 2026-03-16
- **核心参数**:
  - 119B total, 6B active, 128 experts (4 active/token)
  - 256K context window
  - Apache 2.0
- **主要创新点**:
  - **统一模型**: 整合 Magistral (推理)、Pixtral (多模态)、Devstral (agentic coding) 到单一模型
  - **可配置推理深度**: `reasoning_effort` 参数动态调整
  - **原生多模态**: 文本+图像输入
  - 40% 端到端延迟降低，3x 吞吐量提升 (vs Mistral Small 3)
- **链接**: [mistral.ai/news/mistral-small-4](https://mistral.ai/news/mistral-small-4/)

### Mistral Medium 3.5
- **中文标题**: Mistral Medium 3.5
- **英文标题**: Mistral Medium 3.5
- **发布机构**: Mistral AI
- **模型名称**: Mistral Medium 3.5
- **发布日期**: 2026-05-22
- **核心参数**: 128B dense, 256K context, MIT license
- **主要创新点**:
  - **首个旗舰融合模型**: 指令跟随+推理+编程统一
  - SWE-Bench Verified 77.6% (超越 Devstral 2)
  - τ³-Telecom 91.4
  - 从头训练视觉编码器
  - 价格: $1.5/M input, $7.5/M output
- **链接**: [mistral.ai/news/vibe-remote-agents-mistral-medium-3-5](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5/)

### Leanstral 1.5
- **中文标题**: Leanstral 1.5
- **英文标题**: Leanstral 1.5: Proof Abundance for All
- **发布机构**: Mistral AI
- **模型名称**: Leanstral 1.5
- **发布日期**: 2026-07-02
- **核心参数**: 119B total, 6B active, Apache 2.0
- **主要创新点**:
  - miniF2F 100% 饱和，PutnamBench 587/672
  - FATE-H 87%, FATE-X 34% SOTA
  - 通过 mid-training + SFT + RL (CISPO) 训练
  - 发现 5 个未知 GitHub bug
  - Test-time scaling: pass@8 从 50K token 的 44 到 4M token 的 587
- **链接**: [mistral.ai/news/leanstral-1-5](https://mistral.ai/news/leanstral-1-5/)

---

## 7. Qwen (Alibaba / 通义千问)

### Qwen3 Technical Report
- **中文标题**: Qwen3 技术报告
- **英文标题**: Qwen3 Technical Report
- **发布机构**: Alibaba Qwen Team
- **模型名称**: Qwen3 系列
- **发布日期**: 2025-05
- **核心参数**: 多个规模 LLM
- **主要创新点**: Qwen 模型家族最新版本
- **链接**: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

### Qwen3.5-Omni Technical Report
- **中文标题**: Qwen3.5-Omni 技术报告
- **英文标题**: Qwen3.5-Omni Technical Report
- **发布机构**: Alibaba Qwen Team
- **模型名称**: Qwen3.5-Omni
- **发布日期**: 2026-04-17
- **核心参数**:
  - 数百亿参数 MoE
  - 256K context length
  - 4T tokens 预训练 (text/image/audio/video)
  - 100M+ hours 音视频数据
- **主要创新点**:
  - **Thinker-Talker MoE 架构**: Thinker 处理理解/推理/文本生成，Talker 语音生成
  - **ARIA**: 动态对齐文本和语音单位，提升合成稳定性和韵律
  - 215 个音频/音视频理解子任务 SOTA
  - 支持 10+ 小时音频理解，400 秒 720P 视频
  - **Audio-Visual Vibe Coding**: 根据音视频指令直接编码（新能力涌现）
  - 超低延迟: 首包延迟 235-435ms (audio), 426-651ms (video)
- **链接**: [arXiv:2604.15804](https://arxiv.org/abs/2604.15804)

### Qwen-Image-2.0 Technical Report
- **中文标题**: Qwen-Image-2.0 技术报告
- **英文标题**: Qwen-Image-2.0 Technical Report
- **发布机构**: Alibaba Qwen Team
- **模型名称**: Qwen-Image-2.0
- **发布日期**: 2026-05
- **主要创新点**:
  - 统一图像生成+图像编辑的单一框架
  - 超长文本渲染 (1K token instructions)
  - 多语言文字渲染
  - MMDiT + 高压缩 VAE (16x 空间下采样)
  - LMArena 全球 #9，中国模型 #1
- **链接**: [arXiv:2605.10730](https://arxiv.org/abs/2605.10730)

### Qwen-VLA: Unified Vision-Language-Action Model
- **中文标题**: Qwen-VLA：统一视觉-语言-动作模型
- **英文标题**: Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments
- **发布机构**: Alibaba Qwen Team
- **模型名称**: Qwen-VLA
- **发布日期**: 2026-05-28
- **核心参数**: 基于 Qwen3.5-4B backbone + DiT action decoder
- **主要创新点**:
  - 统一 manipulation/navigation/trajectory 预测
  - Embodiment-aware prompt conditioning
  - LIBERO 97.9%, RoboTwin-Hard 87.2%
  - 跨任务/跨实体泛化
- **链接**: [arXiv:2605.30280](https://arxiv.org/abs/2605.30280)

---

## 8. Microsoft (Phi)

### Phi-4-reasoning-vision-15B Technical Report
- **中文标题**: Phi-4-reasoning-vision-15B 技术报告
- **英文标题**: Phi-4-reasoning-vision-15B Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4-reasoning-vision-15B
- **发布日期**: 2026-03-04
- **核心参数**: 15B 紧凑多模态推理模型
- **主要创新点**:
  - 开放权重多模态推理模型
  - 设计选择和实验分析
- **链接**: [arXiv:2603.03975](https://arxiv.org/abs/2603.03975)

### Phi-4-Mini Technical Report
- **中文标题**: Phi-4-Mini 技术报告
- **英文标题**: Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Models
- **发布机构**: Microsoft
- **模型名称**: Phi-4-Mini
- **发布日期**: 2025-03
- **核心参数**: 3.8B 参数
- **主要创新点**: 高质量 web + 合成数据训练，超越同期开源模型
- **链接**: [arXiv:2503.01743](https://arxiv.org/abs/2503.01743)

---

## 9. Apple

### Apple Intelligence Foundation Language Models: Tech Report 2025
- **中文标题**: Apple Intelligence 基础语言模型技术报告 2025
- **英文标题**: Apple Intelligence Foundation Language Models: Tech Report 2025
- **发布机构**: Apple
- **模型名称**: Apple AFM (On-Device ~3B + Server MoE)
- **发布日期**: 2025-07 (WWDC 2025 发布)
- **核心参数**:
  - On-Device: ~3B, Apple Silicon 优化
  - Server: Parallel-Track MoE (PT-MoE)
  - 16 种语言支持
- **主要创新点**:
  - **KV-Cache Sharing**: Block 1/2 共享 KV cache，减少 37.5% 内存，TTFT 降低 ~37.5%
  - **PT-MoE 架构**: Parallel Track Transformer + MoE，track parallelism 减少 87.5% 同步开销
  - **交错全局/局部注意力**: 3 层局部注意力 (sliding window 4096) + 1 层全局注意力
  - **2-bit 量化感知训练 (QAT)**: On-Device 模型
  - Foundation Models Framework: Swift API
- **链接**: [machinelearning.apple.com](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025)、[arXiv:2507.13575](https://arxiv.org/abs/2507.13575)

---

## 10. NVIDIA

### Nemotron 3 Ultra
- **中文标题**: Nemotron 3 Ultra
- **英文标题**: Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Attention Language Model
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Ultra
- **发布日期**: 2026-06
- **核心参数**: 550B total, 55B active, Hybrid Mamba-Attention MoE
- **主要创新点**:
  - Hybrid Mamba-Attention 架构
  - MoE 稀疏计算
  - 开源
- **链接**: [NVIDIA Research (PDF)](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)

### Nemotron 3 Super
- **中文标题**: Nemotron 3 Super
- **英文标题**: Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Super
- **发布日期**: 2026-04
- **核心参数**:
  - 120B total, 12B active, Hybrid Mamba-Attention MoE
  - 25T tokens 预训练
  - 1M context length
- **主要创新点**:
  - **首个 NVFP4 预训练模型**
  - **LatentMoE**: 新 MoE 架构，优化 FLOP 准确率和参数准确率
  - **MTP 层**: 原生投机解码加速推理
  - 2.2x 推理吞吐 (vs GPT-OSS-120B)，7.5x (vs Qwen3.5-122B)
- **链接**: [arXiv:2604.12374](https://arxiv.org/abs/2604.12374)

### Nemotron 3 Nano
- **中文标题**: Nemotron 3 Nano
- **英文标题**: Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Nano 30B-A3B
- **发布日期**: 2025-12
- **核心参数**: 30B total, 3B active, Hybrid Mamba-Transformer MoE, 25T tokens, 1M context
- **主要创新点**:
  - 比前代 Nemotron 2 Nano 激活更少参数却更准确
  - 3.3x 推理吞吐 (vs GPT-OSS-20B)
  - 增强的 Agent/推理/对话能力
- **链接**: [arXiv:2512.20848](https://arxiv.org/abs/2512.20848)

---

## 11. xAI (Grok)

### Grok 4.20 System Card
- **中文标题**: Grok 4.20 系统卡片
- **英文标题**: Grok 4.20 System Card
- **发布机构**: xAI
- **模型名称**: Grok 4.20
- **发布日期**: 2026-04
- **链接**: [data.x.ai (PDF)](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf)

### Grok 4.1 Model Card
- **中文标题**: Grok 4.1 模型卡片
- **英文标题**: Grok 4.1 Model Card
- **发布机构**: xAI
- **模型名称**: Grok 4.1
- **发布日期**: 2025-11-17
- **主要创新点**: 更自然流畅的对话，保持强核心推理能力
- **链接**: [data.x.ai (PDF)](https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf)

### Grok 4 Model Card
- **中文标题**: Grok 4 模型卡片
- **英文标题**: Grok 4 Model Card
- **发布机构**: xAI
- **模型名称**: Grok 4
- **发布日期**: 2025-08-20
- **链接**: [data.x.ai (PDF)](https://data.x.ai/2025-08-20-grok-4-model-card.pdf)

---

## 12. Amazon (Amazon Nova)

### Amazon Nova 2
- **中文标题**: Amazon Nova 2：多模态推理与生成模型
- **英文标题**: Amazon Nova 2: Multimodal reasoning and generation models
- **发布机构**: Amazon AGI
- **模型名称**: Nova 2 Lite、Nova 2 Pro (多模态+动态推理)、Nova 2 Omni (统一多模态)、Nova 2 Sonic (语音-语音)
- **发布日期**: 2025-12-02
- **核心参数**: 1M token context window
- **主要创新点**:
  - **动态推理**: 可配置 "extended thinking" 控制
  - **Nova 2 Omni**: 文本/图像/视频/音频输入，文本+图像输出
  - **Nova 2 Sonic**: 端到端语音-语音基础模型
- **链接**: [amazon.science](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models)

### Amazon Nova Premier
- **中文标题**: Amazon Nova Premier
- **英文标题**: Amazon Nova Premier: Technical report and model card
- **发布机构**: Amazon AGI
- **模型名称**: Amazon Nova Premier
- **发布日期**: 2025-04-30 (技术报告 addendum)
- **核心参数**: 1M token context, 文本/图像/视频
- **主要创新点**: 最强多模态模型，教师模型用于蒸馏
- **链接**: [amazon.science](https://www.amazon.science/publications/amazon-nova-premier-technical-report-and-model-card)

---

## 13. Zhipu AI (智谱 AI / GLM)

### GLM-5: from Vibe Coding to Agentic Engineering
- **中文标题**: GLM-5：从 Vibe Coding 到 Agentic Engineering
- **英文标题**: GLM-5: from Vibe Coding to Agentic Engineering
- **发布机构**: 智谱 AI (Zhipu AI / 5 Team)
- **模型名称**: GLM-5
- **发布日期**: 2026-02-17
- **核心参数**: 744B MoE, 40B activated
- **主要创新点**:
  - **DSA (DeepSeek Sparse Attention)**: 引入动态稀疏注意力，降低成本同时保持长上下文能力
  - **异步多任务强化学习**: 全新异步 RL 基础设施，生成与训练解耦
  - **异步 Agent RL 算法**: 创新算法提升效率
  - **CC-Bench-V2**: 自动化评测集，模拟真实软件开发
  - **国产芯片全栈适配**: 华为昇腾、摩尔线程、海光、寒武纪等
  - 40 页论文公开全部技术细节
- **链接**: [arXiv:2602.15763](https://arxiv.org/abs/2602.15763)

### GLM-5.2: Built for Long-Horizon Tasks
- **中文标题**: GLM-5.2：为长程任务构建
- **英文标题**: GLM-5.2: Built for Long-Horizon Tasks
- **发布机构**: 智谱 AI
- **模型名称**: GLM-5.2
- **发布日期**: 2026-06-16
- **主要创新点**: 长程任务能力大幅跃升
- **链接**: [z.ai/blog/glm-5.2](https://z.ai/blog/glm-5.2)

---

## 14. InternLM (上海 AI Lab)

### Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale
- **中文标题**: Intern-S1-Pro：万亿参数科学多模态基础模型
- **英文标题**: Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale
- **发布机构**: Shanghai AI Lab
- **模型名称**: Intern-S1-Pro
- **发布日期**: 2026-03-26
- **核心参数**: 1T 参数
- **主要创新点**:
  - **首个万亿参数科学多模态模型**
  - 掌握 100+ 专业任务 (化学、材料、生命科学、地球科学)
  - 增强 Agent 能力
  - XTuner + LMDeploy 支撑高效 RL 训练
- **链接**: [arXiv:2603.25040](https://arxiv.org/abs/2603.25040)

### InternVL3.5
- **中文标题**: InternVL3.5：推进开源多模态模型
- **英文标题**: InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency
- **发布机构**: Shanghai AI Lab
- **模型名称**: InternVL3.5-241B-A28B (最大模型)
- **发布日期**: 2025-08
- **主要创新点**:
  - **Cascade RL**: 两阶段 (offline RL + online RL) 粗到细推理增强
  - **Visual Resolution Router (ViR)**: 动态调整视觉 token 分辨率
  - **Decoupled Vision-Language Deployment (DvD)**: 视觉编码器和语言模型分 GPU 部署
  - 推理性能 +16.0%，推理速度 4.05x 提升
  - 与 GPT-5 性能差距缩小
- **链接**: [arXiv:2508.18265](https://arxiv.org/abs/2508.18265)

---

## 15. Moonshot AI (月之暗面 / Kimi)

### Kimi K2: Open Agentic Intelligence
- **中文标题**: Kimi K2：开放 Agent 智能
- **英文标题**: Kimi K2: Open Agentic Intelligence
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2
- **发布日期**: 2025-07
- **核心参数**:
  - 1T total, 32B active, MoE
  - 384 experts, 8 selected per token + 1 shared
  - 15.5T tokens 预训练，零 loss spike
  - 256K context, MLA attention
- **主要创新点**:
  - **MuonClip 优化器**: Muon + QK-clip 技术解决训练不稳定性
  - **大规模 Agent 数据合成管线**
  - **联合 RL 阶段**: 在真实+合成环境中交互学习
  - SWE-Bench Verified 65.8%, LiveCodeBench v6 53.7%
  - Tau2-Bench 66.1%, ACEBench (En) 76.5%
- **链接**: [arXiv:2507.20534](https://arxiv.org/abs/2507.20534)、[GitHub](https://github.com/MoonshotAI/Kimi-K2)

### Kimi K2.5: Visual Agentic Intelligence
- **中文标题**: Kimi K2.5：视觉 Agent 智能
- **英文标题**: Kimi K2.5: Visual Agentic Intelligence
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2.5
- **发布日期**: 2026-02-02
- **核心参数**:
  - 1T total, 32B active, MoE
  - 400M MoonViT 视觉编码器
  - ~15T mixed visual+text tokens 持续预训练
  - 256K context
- **主要创新点**:
  - **原生多模态 Agent**: 文本+视觉联合优化
  - **Agent Swarm**: 自主并行 Agent 编排框架，延迟降低 4.5x
  - **联合文本-视觉预训练 + 零视觉 SFT + 联合文本-视觉 RL**
  - AIME 2025 96.1, SWE-Bench Verified 76.8, BrowseComp 60.6
  - HLE-Full (w/ tools) 50.2 (超过 GPT-5.2 的 45.5)
- **链接**: [arXiv:2602.02276](https://arxiv.org/abs/2602.02276)、[GitHub](https://github.com/MoonshotAI/Kimi-K2.5)

---

## 16. StepFun (阶跃星辰)

### Step-DeepResearch Technical Report
- **中文标题**: Step-DeepResearch 技术报告
- **英文标题**: Step-DeepResearch Technical Report
- **发布机构**: StepFun (阶跃星辰)
- **模型名称**: Step-DeepResearch
- **发布日期**: 2025-12
- **核心参数**: 32B 参数 (基于 Qwen2.5-32B-Base)
- **主要创新点**:
  - **原子能力数据合成策略**: 增强规划/信息搜索/反思/报告写作
  - **渐进训练路径**: Agent mid-training → SFT → RL
  - **Checklist-style Judger 奖励**: 提升多场景鲁棒性
  - ResearchRubrics 61.42 (接近 OpenAI DeepResearch)
  - ADR-Bench: 中文深度研究基准
  - 成本: 不到 ¥0.50/次 (为 Gemini/OpenAI 的 1/10)
- **链接**: [arXiv:2512.20491](https://arxiv.org/abs/2512.20491)、[GitHub](https://github.com/stepfun-ai/StepDeepResearch)

### StepFun-Prover Preview
- **中文标题**: StepFun-Prover Preview
- **英文标题**: StepFun-Prover Preview: Let's Think and Verify Step by Step
- **发布机构**: StepFun
- **模型名称**: StepFun-Prover-Preview-7B/32B
- **发布日期**: 2025-07
- **主要创新点**:
  - miniF2F-test pass@1 70.0% (32B), 超越 DeepSeek-Prover-V2-671B
  - 工具集成推理 RL 训练管线
  - 冷启动数据合成 + 工具集成 RL
- **链接**: [arXiv:2507.20199](https://arxiv.org/abs/2507.20199)

---

## 17. ByteDance Seed (字节跳动)

### Seed1.8 Model Card: Towards Generalized Real-World Agency
- **中文标题**: Seed1.8 模型卡片：迈向通用现实世界 Agent
- **英文标题**: Seed1.8 Model Card: Towards Generalized Real-World Agency
- **发布机构**: ByteDance Seed
- **模型名称**: Seed1.8
- **发布日期**: 2025-12 (模型卡), 2026-03 (arXiv)
- **核心参数**: 支持文本+图像输入，可配置思考模式
- **主要创新点**:
  - **通用 Agent 设计**: 感知+推理+行动统一模型
  - **多轮交互+工具使用+环境反馈**
  - GAIA 93.2 (超越 GPT-5-high 的 76.7)
  - BrowseComp-en 67.6, SWE-Bench Verified competitive
  - **VideoCut 工具**: 高帧率视频回放增强理解
  - **推理效率大幅提升**: 同 token 预算下显著超越 Seed-1.6
- **链接**: [arXiv:2603.20633](https://arxiv.org/abs/2603.20633)

### Seed1.5-VL Technical Report
- **中文标题**: Seed1.5-VL 技术报告
- **英文标题**: Seed1.5-VL Technical Report
- **发布机构**: ByteDance Seed
- **模型名称**: Seed1.5-VL
- **发布日期**: 2025-05
- **主要创新点**: 通用多模态理解与推理视觉-语言基础模型
- **链接**: [arXiv:2505.07062](https://arxiv.org/abs/2505.07062)

---

## 18. 01.AI (零一万物)

### Yi-Lightning Technical Report
- **中文标题**: Yi-Lightning 技术报告
- **英文标题**: Yi-Lightning Technical Report
- **发布机构**: 01.AI
- **模型名称**: Yi-Lightning
- **发布日期**: 2024-10
- **核心参数**: API-only，Chatbot Arena #6
- **主要创新点**: 高性价比 ($0.14/M tokens)，质量接近 GPT 级
- **链接**: [arXiv:2412.01253](https://arxiv.org/abs/2412.01253)
- **备注**: 2025-2026 年发布节奏明显放缓，被 DeepSeek/Qwen/Kimi/GLM 超越

---

## 19. Baichuan (百川智能)

### Baichuan-M4
- **中文标题**: Baichuan-M4：新一代医疗大模型
- **英文标题**: Baichuan-M4
- **发布机构**: 百川智能 + 清华大学 THUBPM
- **模型名称**: Baichuan-M4
- **发布日期**: 2026-06
- **核心参数**:
  - HealthBench 68.6 (世界第一)
  - HealthBench Hard 49.7
  - 幻觉率: 3.3% (全球最低)
  - 证据引用准确率: 90.0%
- **主要创新点**:
  - **事实性感知强化学习算法**: 幻觉率降至 3.3%
  - **Baichuan-Harness 架构**: 统一训练/推理运行框架
  - **SPAR++ RL**: Span-Level Reward 细粒度优化
  - **课程式 RL**: 按临床难度逐步增加
  - **推理路径压缩**: 降低推理成本保持质量
  - **全病程记忆系统**: 跨时段病历调用准确率 98.7%
  - 多工具协同: 长期记忆+医学检索+OCR+视觉理解
  - 三大医疗榜单同时世界第一 (超 GPT-5.5/Opus 4.7/DeepSeek-V4-Pro)
- **链接**: [arXiv:2606.08982](https://arxiv.org/abs/2606.08982)

---

## 跨公司趋势分析

### 1. 架构趋势
| 趋势 | 代表模型 | 详情 |
|------|---------|------|
| **MoE 成为标配** | DeepSeek-V4, LLaMA 4, Qwen3.5-Omni, GLM-5, Kimi K2/K2.5, Mistral Small 4, NVIDIA Nemotron 3, Amazon Nova 2 | 所有主要模型均采用 MoE |
| **Hybrid Mamba-Transformer** | NVIDIA Nemotron 3 (Ultra/Super/Nano) | Mamba-Attention 混合架构提升效率 |
| **Hybrid Attention (CSA+HCA)** | DeepSeek-V4, Apple PT-MoE | 压缩+稀疏注意力实现超长上下文 |
| **iRoPE** | LLaMA 4 Scout | 交错注意力层实现 10M 上下文 |
| **Parallel Track MoE** | Apple Server Model | Track parallelism 减少 87.5% 同步开销 |

### 2. 训练方法
| 趋势 | 代表 | 详情 |
|------|------|------|
| **RL Post-training** | DeepSeek-R1 (GRPO), Anthropic Claude (RLHF), Kimi K2 (agentic RL), GLM-5 (异步 RL) | RL 成为后训练核心 |
| **纯 RL 无 SFT** | DeepSeek-R1-Zero | 直接 GRPO 训练涌现推理 |
| **Cold Start + 多阶段 RL** | DeepSeek-R1 (4阶段), Qwen-VLA (progressive) | 复杂多阶段训练管线 |
| **Agent RL** | Kimi K2.5 (Agent Swarm), GLM-5 (异步 Agent RL), StepFun (Checklist Judger) | Agent 环境交互式 RL |
| **Cascade RL** | InternVL3.5 (offline→online) | 两阶段粗到细对齐 |
| **CISPO RL** | Leanstral 1.5 | 形式化验证专用 RL |

### 3. Scaling Law 趋势
| 趋势 | 详情 |
|------|------|
| **参数规模** | 万亿参数常态化 (Intern-S1-Pro 1T, Kimi K2/K2.5 1T, LLaMA 4 Behemoth 2T) |
| **训练数据** | 30T+ tokens 成为标准 (DeepSeek-V4 32-33T, Nemotron 3 25T, Kimi K2 15.5T) |
| **推理时间 Scaling** | Gemini Deep Think, DeepSeek-R1, Seed1.8 (推理预算动态分配) |
| **效率 Scaling** | DeepSeek-V4 Flash: 10% KV cache, 27% FLOPs (vs V3.2) |

### 4. 多模态
| 趋势 | 代表 | 详情 |
|------|------|------|
| **原生多模态 (Early Fusion)** | LLaMA 4, Qwen3.5-Omni, Kimi K2.5 | 视觉 token 直接混入文本流 |
| **全模态 (Omni)** | Qwen3.5-Omni (Text+Image+Audio+Video), Amazon Nova 2 Omni | 文本/图像/音频/视频统一 |
| **统一生成+编辑** | Qwen-Image-2.0 | 单一框架统一 T2I + 图像编辑 |
| **VLA (Vision-Language-Action)** | Qwen-VLA | 从理解到机器人控制 |
| **医学多模态** | Baichuan-M4 | 医疗文档/影像/OCR/检索 |

### 5. 长上下文
| 模型 | 上下文长度 | 技术 |
|------|-----------|------|
| LLaMA 4 Scout | **10M tokens** | iRoPE + 长度泛化 |
| DeepSeek-V4 | **1M tokens** | CSA+HCA 混合注意力 |
| Gemini 2.5 Pro | **1M+ tokens** | 原生长上下文 |
| NVIDIA Nemotron 3 | **1M tokens** | Hybrid Mamba-Attention |
| Amazon Nova 2 | **1M tokens** | - |
| Kimi K2.5 | **256K tokens** | MLA |
| Mistral Small 4 | **256K tokens** | MoE |
| Qwen3.5-Omni | **256K tokens** | Hybrid Attention MoE |
| Apple Server | **交错 G/L** | Sliding window 4096 + Global |

### 6. 推理模型
| 模型 | 推理方式 | 特点 |
|------|---------|------|
| DeepSeek-R1 | GRPO RL | 纯 RL 涌现推理链 |
| Gemini 2.5 Pro | Thinking 模式 | 深度思考 + 工具使用 |
| Seed1.8 | 可配置思考模式 | 推理预算动态分配 |
| Mistral Small 4 | `reasoning_effort` 参数 | 可调推理深度 |
| Claude Opus 4 | 混合推理 | 推理+视觉+工具 |
| StepFun-Prover | 工具集成推理 | Lean 4 形式化验证 |
| Leanstral 1.5 | Test-time scaling | 50K→4M token 持续提升 |

---

## 关键洞察

1. **MoE 全面普及**: 从 2025 年的 DeepSeek-V3 开始，到 2026 年所有主要模型都采用 MoE，Active parameter 通常在 3B-55B 之间，总参数 30B-2T。

2. **Agent 能力成为核心竞争力**: Kimi K2.5 的 Agent Swarm、GLM-5 的异步 Agent RL、StepFun 的 Deep Research Agent，Agent 不再是外挂而是模型核心能力。

3. **百万 Token 上下文已是标准**: DeepSeek-V4 的 CSA+HCA、LLaMA 4 的 iRoPE、Gemini 的原生长上下文，百万级上下文从"实验性"变为"常规"。

4. **RL 后训练分化为多个范式**: GRPO (DeepSeek)、异步 RL (GLM-5)、Agent RL (Kimi/StepFun)、Cascade RL (InternVL)、CISPO (Leanstral)。

5. **垂直模型崛起**: Baichuan-M4 在医疗领域登顶三大榜单，幻觉率 3.3%，证明垂直领域深耕可超越通用模型。

6. **开源竞争白热化**: Mistral Small 4 (Apache 2.0)、LLaMA 4、Kimi K2/K2.5、GLM-5、NVIDIA Nemotron 3、StepFun-Prover 等均开源，开源模型能力逼近闭源前沿。

7. **推理时间计算 (Test-time Compute) 成为新 Scaling 轴**: Gemini Deep Think、Seed1.8、Leanstral 1.5 都展示了推理时间计算的巨大潜力。
