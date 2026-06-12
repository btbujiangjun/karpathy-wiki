---
title: 各大 AI 公司最新技术报告汇总 (第十一版) — 2026-06-12
type: synthesis
created: 2026-06-12
updated: 2026-06-12
tags: [tech-report, system-card, llm, survey, ai-companies]
---

# 各大 AI 公司最新技术报告汇总 (第十一版) — 2026-06-12

> 截止 2026 年 6 月 12 日，22+ 家机构的 40+ 技术报告/System Card 汇总。
> 重点关注：新架构 (MoE, Mamba, hybrid)、训练方法、Scaling Law、多模态、长上下文、推理模型。

---

## 1. DeepSeek（深度求索）

### DeepSeek V4 Model Card
- **中文标题**: DeepSeek V4 模型卡
- **模型系列**: DeepSeek V4 (V4-Pro, V4-Flash)
- **发布日期**: 2026-04-24
- **核心参数**:
  - V4-Pro: 1.6T 总参数 / 49B 激活 (MoE)
  - V4-Flash: 284B 总参数 / 13B 激活 (MoE)
  - 上下文: 1M tokens
  - 训练数据: 33T tokens
- **主要创新**:
  - Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)
  - Manifold-Constrained Hyper-Connections (mHC)
  - Muon Optimizer 加速收敛
  - 三种推理模式: Non-think / Think High / Think Max
- **链接**: [Model Card PDF](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **中文标题**: 通过强化学习激励大语言模型的推理能力
- **发布日期**: 2025-01-20
- **核心参数**: 671B total, 37B active, 128K context (基于 V3-Base)
- **主要创新**:
  - 纯 RL (GRPO) 无需 SFT 即可涌现推理能力 (R1-Zero)
  - 多阶段训练: 冷启动 → RL → 拒绝采样 → SFT → 全面 RL
  - 蒸馏至 Qwen/Llama 小模型
- **链接**: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)

### DeepSeek-V3 Technical Report
- **中文标题**: DeepSeek-V3 技术报告
- **发布日期**: 2024-12-27
- **核心参数**: 671B total, 37B active, 14.8T tokens, 128K context
- **主要创新**: 无辅助损失负载均衡, Multi-Token Prediction (MTP), MLA 注意力, FP8 混合精度训练
- **链接**: [arXiv:2412.19437](https://arxiv.org/abs/2412.19437)

---

## 2. OpenAI

### GPT-5.5 System Card
- **中文标题**: GPT-5.5 System Card
- **模型系列**: GPT-5.5 / GPT-5.5 Pro
- **发布日期**: 2026-04-23
- **主要创新**:
  - 复杂真实世界任务（写代码、在线研究、文档创建、跨工具操作）
  - 理解任务更早、需更少指导、更有效使用工具
  - 并行 test-time compute 提升 (Pro)
  - 最强安全防护 (safe-completions)
- **链接**: [System Card](https://openai.com/index/gpt-5-5-system-card/)

### GPT-5 System Card
- **中文标题**: GPT-5 System Card
- **模型系列**: GPT-5 (main / main-mini / thinking / thinking-mini / thinking-nano / thinking-pro)
- **发布日期**: 2025-08-13
- **主要创新**:
  - 统一系统: 快速模型 + 深度推理模型 + 实时路由器
  - 路由器持续训练于用户切换/偏好/正确性信号
  - 显著减少幻觉、改进指令遵循、减少 sycophancy
- **链接**: [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) | [PDF](https://cdn.openai.com/gpt-5-system-card.pdf)

### OpenAI o3 and o4-mini System Card
- **中文标题**: OpenAI o3 和 o4-mini System Card
- **发布日期**: 2025-04-16
- **主要创新**:
  - 最先进推理 + 完整工具能力（Web 浏览、Python、图像/文件分析等）
  - 大规模 RL 训练 chain-of-thought
  - Deliberative alignment（推理安全策略）
- **链接**: [PDF](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)

---

## 3. Meta AI (LLaMA)

### The Llama 4 Herd: Natively Multimodal AI
- **中文标题**: Llama 4 系列：原生多模态 AI
- **模型系列**: Llama 4 Scout / Maverick / Behemoth
- **发布日期**: 2025-04-05
- **核心参数**:

| 模型 | 激活参数 | 总参数 | Experts | Tokens | 上下文 |
|------|---------|-------|---------|--------|--------|
| Scout (17B×16E) | 17B | 109B | 16 routed + 1 shared | ~40T | 10M |
| Maverick (17B×128E) | 17B | 400B | 128 routed + 1 shared | ~22T | 1M |
| Behemoth (teacher) | 未公开 | 未公开 | 16 routed + 1 shared | 未公开 | 未公开 |

- **主要创新**:
  - 首个 MoE 模型家族（替代 Llama 2/3 的 dense transformer）
  - Early Fusion 原生多模态（视觉和语言从训练开始即融合）
  - Behemoth 作为教师模型进行蒸馏
  - Scout 可在单张 H100 GPU (int4 量化) 上运行
  - Maverick: 超越 GPT-4o 和 Gemini 2.0，与 DeepSeek V3.1 竞争
- **训练计算**: Scout 5.0M H100 GPU hours + Maverick 2.38M H100 GPU hours
- **链接**: [Blog](https://ai.meta.com/blog/Llama-4-multimodal-intelligence/) | [Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md)

---

## 4. Google DeepMind (Gemini)

### Gemini 3.1 Pro Model Card
- **中文标题**: Gemini 3.1 Pro 模型卡
- **模型系列**: Gemini 3.1 Pro
- **发布日期**: 2026-02-19
- **主要创新**:
  - 基于 Gemini 3 Pro 的迭代升级
  - 大幅提升推理和多模态能力
  - Deep Think 模式：针对科学、研究和工程的高级推理
  - 数学/物理/化学奥赛金牌级表现
- **链接**: [Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)

### Gemini 2.5 Technical Report
- **中文标题**: Gemini 2.5 技术报告
- **模型系列**: Gemini 2.5 Pro / 2.5 Flash / 2.0 Flash / 2.0 Flash-Lite
- **发布日期**: 2025-06-16
- **核心参数**: >1M token 上下文, 原生多模态 + 原生工具使用
- **主要创新**:
  - 4 个模型覆盖完整 Pareto 前沿
  - 2.5 Pro: 最强智能推理模型
  - 2.5 Flash: 可控推理预算的混合推理模型
  - Agentic 系统能力（如 Gemini Plays Pokémon）
- **链接**: [PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf)

### Gemini Embedding 2
- **中文标题**: Gemini Embedding 2 — 原生多模态嵌入模型
- **发布日期**: 2026
- **主要创新**:
  - 统一嵌入视频、音频、图像、文本
  - 大规模多任务多阶段对比学习训练
  - SOTA 跨模态检索性能
- **链接**: [arXiv:2605.27295](https://arxiv.org/html/2605.27295v1)

---

## 5. Anthropic (Claude)

### Claude Opus 4 & Sonnet 4 System Card (May 2025)
- **中文标题**: Claude Opus 4 与 Claude Sonnet 4 System Card
- **模型系列**: Claude Opus 4 / Sonnet 4
- **发布日期**: 2025-05-22
- **主要创新**:
  - Hybrid reasoning 模型（近即时响应 + 扩展思考）
  - SWE-bench 72.5%, Terminal-bench 43.2%（最佳编码模型）
  - Opus 4 按 ASL-3 Standard 部署
  - Sonnet 4 按 ASL-2 Standard 部署
  - 首次包含详细 alignment 评估和 model welfare 评估
- **链接**: [System Card PDF](https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf)

### Claude Opus 4.5 / 4.6 / 4.7 / 4.8 / Sonnet 4.5 / 4.6 / Fable 5 & Mythos 5 System Cards
- **中文标题**: Claude 系列后续版本 System Cards
- **最新状态** (截至 2026-06):
  - Opus 4.8: 2026-05
  - Fable 5 & Mythos 5: 2026-06（最新）
  - Opus 4.7: 2026-04
  - Sonnet 4.6: 2026-02
  - Haiku 4.5: 2025-10
- **链接**: [System Cards 索引](https://www.anthropic.com/system-cards)

---

## 6. Mistral AI

### Mistral Medium 3.5
- **中文标题**: Mistral Medium 3.5
- **模型系列**: Mistral Medium 3.5（128B dense）
- **发布日期**: 2026-05-22
- **核心参数**: 128B dense, 256K context window
- **主要创新**:
  - 首个旗舰 merged model（指令遵循 + 推理 + 编码统一）
  - 可配置推理 effort 级别
  - 全新训练的视觉编码器（支持可变图像大小和宽高比）
  - SWE-Bench Verified 77.6%
  - 开源 (modified MIT license)，4 GPU 可自托管
- **链接**: [Blog](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5/)

### Magistral: Mistral's First Reasoning Model
- **中文标题**: Magistral — Mistral 首个推理模型
- **模型系列**: Magistral Medium / Magistral Small (24B)
- **发布日期**: 2026-06
- **主要创新**:
  - 纯 RL 训练（基于 Mistral Medium 3）
  - 提出 RLVR 框架（RL from Verifiable Rewards）
  - 冷启动 SFT + RL 提升小模型
  - Magistral Small 开源 (Apache 2.0)
- **链接**: [arXiv:2506.10910](https://arxiv.org/pdf/2506.10910)

### Mistral Large 3
- **中文标题**: Mistral Large 3
- **发布日期**: 2025-12-02
- **核心参数**: 675B total / 41B active (MoE), 训练于 3000 H200 GPUs
- **主要创新**:
  - 首个 MoE 模型（自 Mixtral 系列之后）
  - 最佳多语言非中英文性能
  - Apache 2.0 开源
- **链接**: [Blog](https://mistral.ai/news/mistral-3/)

---

## 7. Qwen (Alibaba)

### Qwen3 Technical Report
- **中文标题**: Qwen3 技术报告
- **模型系列**: Qwen3 (0.6B ~ 235B, Dense + MoE)
- **发布日期**: 2025-05-14
- **核心参数**:
  - 旗舰: Qwen3-235B-A22B (MoE, 235B total, 22B active)
  - 思考/非思考统一模式 + 思考预算控制
  - 119 种语言支持（从 29 种扩展）
- **主要创新**:
  - 统一 thinking / non-thinking 模式，无需切换模型
  - Thinking budget 机制（自适应分配推理计算）
  - 全系列 Apache 2.0 开源
- **链接**: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

### Qwen3.5-Omni Technical Report
- **中文标题**: Qwen3.5-Omni 技术报告
- **发布日期**: 2026
- **核心参数**: 数百亿参数, 256K context
- **主要创新**:
  - Hybrid Attention MoE (Thinker + Talker)
  - 100M+ 小时音视频数据训练
  - ARIA (Adaptive Rate Interleave Alignment) 流式语音合成
  - 10+ 小时音频理解, 400 秒 720P 视频
- **链接**: [arXiv:2604.15804](https://arxiv.org/pdf/2604.15804)

### Qwen3.6-35B-A3B
- **中文标题**: Qwen3.6-35B-A3B 开源模型
- **发布日期**: 2026-04-17
- **核心参数**: 35B total / 3B active (MoE)
- **主要创新**: 仅 3B 激活参数即超越 Qwen3.5-27B dense 的编码性能
- **链接**: [Blog](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-agentic-coding-power-now-open-to-all_603043)

---

## 8. Microsoft (Phi)

### Phi-4 Technical Report
- **中文标题**: Phi-4 技术报告
- **模型系列**: Phi-4 (14B)
- **发布日期**: 2024-12-12
- **核心参数**: 14B dense
- **主要创新**:
  - 数据质量为中心的训练策略
  - 战略性使用合成数据（超越教师模型 GPT-4）
  - STEM 推理 SOTA
- **链接**: [arXiv:2412.08905](https://arxiv.org/abs/2412.08905)

### Phi-4-Reasoning Technical Report
- **中文标题**: Phi-4-Reasoning 技术报告
- **模型系列**: Phi-4-reasoning / Phi-4-reasoning-plus (14B)
- **发布日期**: 2025
- **主要创新**:
  - SFT 于 o3-mini 生成的推理轨迹
  - RL (outcome-based) 进一步提升
  - 超越 DeepSeek-R1-Distill-Llama-70B
- **链接**: [arXiv:2504.21318](https://arxiv.org/abs/2504.21318)

### Phi-4-reasoning-vision-15B Technical Report
- **中文标题**: Phi-4-reasoning-vision-15B 技术报告
- **发布日期**: 2026-03-04
- **核心参数**: 15B, 多模态推理
- **主要创新**:
  - 紧凑开源多模态推理模型
  - 系统过滤、纠错、合成增强
  - 高分辨率动态分辨率编码器
  - 混合推理/非推理数据 + 显式模式 token
- **链接**: [arXiv:2603.03975](https://arxiv.org/html/2603.03975) | [MSR](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/)

---

## 9. Apple

### Apple Intelligence Foundation Language Models Tech Report 2025
- **中文标题**: Apple Intelligence 基础语言模型技术报告 2025
- **模型系列**: On-device (~3B) + Server (PT-MoE)
- **发布日期**: 2025-07-17
- **核心参数**:
  - 设备端: ~3B 参数, KV-cache sharing, 2-bit QAT
  - 服务端: Parallel-Track MoE Transformer
- **主要创新**:
  - KV-cache sharing + 2-bit 量化感知训练（设备端优化）
  - PT-MoE: track parallelism + MoE + 交错全局-局部注意力
  - 异步训练平台
  - 16 种语言支持, 图像理解, 工具调用
- **链接**: [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) | [Apple ML Research](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025)

---

## 10. NVIDIA

### Nemotron 3 Ultra Technical Report
- **中文标题**: Nemotron 3 Ultra 技术报告
- **模型系列**: Nemotron 3 Ultra (550B-A55B)
- **发布日期**: 2026-06-04
- **核心参数**: 550B total / 55B active (MoE + Hybrid Mamba-Transformer)
- **主要创新**:
  - 首个 MoE + Hybrid Mamba-Attention 架构
  - LatentMoE + Multi-Token Prediction (MTP)
  - NVFP4 预训练和量化（5× 推理吞吐提升）
  - Multi-Teacher On-Policy Distillation (MOPD)
  - 预训练 20T tokens, 1M context
  - 5.9× 吞吐量 vs GLM-5.1-754B
- **链接**: [Technical Report PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) | [Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)

### Nemotron 3 Super Technical Report
- **中文标题**: Nemotron 3 Super 技术报告
- **模型系列**: Nemotron 3 Super (120B-A12B)
- **核心参数**: 120B total / 12B active (MoE + Hybrid Mamba-Attention)
- **主要创新**: 25T tokens 预训练, 2.2× throughput vs GPT-OSS-120B
- **链接**: [arXiv:2604.12374](https://arxiv.org/pdf/2604.12374)

### Llama-Nemotron: Efficient Reasoning Models
- **中文标题**: Llama-Nemotron: 高效推理模型
- **模型系列**: Nano (8B) / Super (49B) / Ultra (253B)
- **发布日期**: 2025
- **主要创新**: NAS 推理优化 + FFN Fusion + 恢复训练 + RL, 动态推理切换
- **链接**: [arXiv:2505.00949](https://export.arxiv.org/pdf/2505.00949)

---

## 11. xAI (Grok)

### Grok 4 Model Card
- **中文标题**: Grok 4 模型卡
- **模型系列**: Grok 4 (Web + API)
- **发布日期**: 2025-08-20
- **主要创新**:
  - 先进推理 + 工具使用
  - 多阶段 RL (human feedback, verifiable rewards, model grading)
  - Risk Management Framework (RMF) 评估框架
- **链接**: [Model Card PDF](https://data.x.ai/2025-08-20-grok-4-model-card.pdf)

### Grok 4.1 Model Card
- **中文标题**: Grok 4.1 模型卡
- **发布日期**: 2025-11-17
- **配置**: Non-Thinking / Thinking 两种模式
- **主要创新**: 更自然流畅对话 + 强推理能力 + 改进的输入过滤器
- **链接**: [PDF](https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf)

### Grok 4 Fast Model Card
- **中文标题**: Grok 4 Fast 模型卡
- **发布日期**: 2025-09-19
- **特点**: 近 Grok 4 推理能力，更低延迟和成本
- **链接**: [PDF](https://data.x.ai/2025-09-19-grok-4-fast-model-card.pdf)

---

## 12. Amazon (Amazon Nova)

### Amazon Nova 2: Multimodal Reasoning and Generation
- **中文标题**: Amazon Nova 2: 多模态推理与生成
- **模型系列**: Nova 2 Lite / 2 Pro / 2 Omni / 2 Sonic
- **发布日期**: 2025-12-02
- **核心参数**: 1M token context window
- **主要创新**:
  - 2 Pro: 可配置 "extended thinking" 动态推理控制
  - 2 Omni: 统一多模态（文本/图像/视频/音频输入 + 文本/图像输出）
  - 2 Sonic: 语音到语音基础模型
- **链接**: [Amazon Science](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models)

### Amazon Nova Family: Technical Report and Model Card
- **中文标题**: Amazon Nova 系列技术报告与模型卡
- **发布日期**: 2024-12-03 (v1), 2025-04-30 (Premier addendum)
- **模型**: Nova Micro (text-only) / Lite (multimodal) / Pro (multimodal) / Canvas (image gen) / Reel (video gen) / Premier (最强)
- **链接**: [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) | [Amazon Science](https://www.amazon.science/publications/the-amazon-nova-family-of-models-technical-report-and-model-card)

---

## 13. Zhipu AI / 智谱 AI (GLM/ChatGLM)

### GLM-5: From Vibe Coding to Agentic Engineering
- **中文标题**: GLM-5: 从 Vibe Coding 到 Agentic Engineering
- **模型系列**: GLM-5 (744B-A40B)
- **发布日期**: 2026-02-17
- **核心参数**:
  - 744B total / 40B active (MoE)
  - 28.5T 预训练 tokens
  - DeepSeek Sparse Attention (DSA) 集成
  - 200K context
- **主要创新**:
  - DSA 大幅降低部署成本，保持长上下文能力
  - Asynchronous RL 基础设施（"slime" 框架）
  - 异步 Agent RL 算法（group-wise policy optimization）
  - 全栈适配国产 GPU 芯片（华为昇腾、摩尔线程等 7 个平台）
  - MIT License 开源
- **链接**: [arXiv:2602.15763](https://arxiv.org/html/2602.15763) | [Blog](https://z.ai/blog/glm-5) | [Hugging Face](https://huggingface.co/zai-org/GLM-5)

---

## 14. Moonshot AI (Kimi)

### Kimi K2: Open Agentic Intelligence
- **中文标题**: Kimi K2: 开放 Agentic 智能
- **模型系列**: Kimi K2 (1T-A32B)
- **发布日期**: 2025-07
- **核心参数**: 1.04T total / 32B active, 384 experts (8 activated), 15.5T tokens, 256K context, MLA attention
- **主要创新**:
  - MuonClip 优化器（Muon + QK-Clip 稳定性提升）
  - 大规模 agentic 数据合成管线
  - 联合 RL 训练（真实 + 合成环境交互）
  - SWE-Bench Verified 65.8%, LiveCodeBench v6 53.7%, AIME 2025 49.5%
  - 开源权重
- **链接**: [arXiv:2507.20534](https://arxiv.org/html/2507.20534) | [GitHub](https://github.com/MoonshotAI/Kimi-K2)

### Kimi K2.5: Visual Agentic Intelligence
- **中文标题**: Kimi K2.5: 视觉 Agentic 智能
- **模型系列**: Kimi K2.5 (1T-A32B, 原生多模态)
- **发布日期**: 2026-01-30
- **核心参数**: 1T total / 32B active, 256K context, MLA + MoonViT 视觉编码器 (400M)
- **主要创新**:
  - 联合文本-视觉预训练 + Zero-Vision SFT + 联合文本-视觉 RL
  - Agent Swarm: 自导向并行 agent 编排（4.5× 延迟降低）
  - 图像/视频 → 代码生成 SOTA
  - 开源权重
- **链接**: [arXiv:2602.02276](https://arxiv.org/pdf/2602.02276) | [GitHub](https://github.com/MoonshotAI/Kimi-K2.5)

### Kimi Linear: Expressive, Efficient Attention Architecture
- **中文标题**: Kimi Linear: 高效线性注意力架构
- **核心参数**: 3B active / 48B total (Hybrid KDA + MLA)
- **主要创新**: Kimi Delta Attention (KDA), 6× 解码吞吐 (1M context), 75% KV cache 减少
- **链接**: [arXiv:2510.26692](https://export.arxiv.org/pdf/2510.26692)

---

## 15. ByteDance (豆包/Doubao / Seed)

### Seed 2.0 Model Card
- **中文标题**: Seed 2.0 模型卡
- **模型系列**: Seed 2.0 Pro / Lite / Mini / Code
- **发布日期**: 2026-02-14
- **主要创新**:
  - 面向大规模生产部署的系统优化
  - 长尾知识覆盖、复杂指令遵循、长上下文稳定性
  - Pro + Code 模型已部署于豆包 App 和 TRAE
- **链接**: [Model Card PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/seed2/0214/Seed2.0%20Model%20Card.pdf) | [Blog](https://seed.bytedance.com/blog/seed-2-0-official-launch)

### Seed1.5-VL Technical Report
- **中文标题**: Seed1.5-VL 技术报告
- **发布日期**: 2025-05-11
- **核心参数**: 532M 视觉编码器 + MoE LLM (20B active)
- **主要创新**: 38/60 公开 benchmark SOTA, 超越 OpenAI CUA 和 Claude 3.7 在 GUI 控制/游戏
- **链接**: [arXiv:2505.07062](https://arxiv.org/abs/2505.07062)

---

## 16. Shanghai AI Lab (InternLM)

### Intern-S1 Technical Report
- **中文标题**: Intern-S1 技术报告
- **模型系列**: Intern-S1 (241B-A28B MoE)
- **发布日期**: 2025-08
- **核心参数**: 241B total / 28B active, 5T tokens (2.5T 科学领域), 多模态 MoE
- **主要创新**:
  - 科学多模态专家 + 通用推理
  - 在线 RL 训练（InternBootCamp 框架）
  - 分子合成规划、反应条件预测等科学任务 SOTA
- **链接**: [arXiv:2508.15763](https://export.arxiv.org/pdf/2508.15763)

### Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale
- **中文标题**: Intern-S1-Pro: 万亿参数科学多模态基础模型
- **核心参数**: 1T+ 参数
- **主要创新**: 首个万亿参数科学多模态模型，覆盖 100+ 科学任务
- **链接**: [arXiv:2603.25040](https://arxiv.org/pdf/2603.25040)

### InternLM3-8B-Instruct
- **中文标题**: InternLM3-8B 指令模型
- **发布日期**: 2025-01-15
- **核心参数**: 8B, 仅 4T tokens 训练
- **主要创新**: 仅 4T tokens 即达到 SOTA（节省 75%+ 训练成本），支持深度思考 + 正常响应
- **链接**: [Docs](https://internlm.readthedocs.io/en/latest/model_card/InternLM3.html)

---

## 17. StepFun / 阶跃星辰 (Step)

### Step3: Cost-Effective Multimodal Intelligence
- **中文标题**: Step3: 高性价比多模态智能
- **模型系列**: Step3 (321B-A38B MoE)
- **发布日期**: 2025-07
- **核心参数**: 321B total / 38B active, 48 experts (3 activated), MFA attention, 65K context
- **主要创新**:
  - Multi-Matrix Factorization Attention (MFA)
  - Attention-FFN Disaggregation (AFD)
  - 端到端优化解码成本
  - Apache 2.0 开源
- **链接**: [arXiv:2507.19427](https://arxiv.org/abs/2507.19427) | [GitHub](https://github.com/stepfun-ai/Step3)

### Step-DeepResearch Technical Report
- **中文标题**: Step-DeepResearch 技术报告
- **发布日期**: 2025-12
- **核心参数**: 32B
- **主要创新**:
  - 基于原子能力拆解的数据合成策略
  - 渐进式训练: agentic mid-training → SFT → RL
  - Checklist-style Judger 奖励设计
  - ADR-Bench 中文 Deep Research 基准
  - Scale AI ResearchRubrics 61.42
- **链接**: [arXiv:2512.20491](https://arxiv.org/abs/2512.20491)

### StepAudio 2.5
- **中文标题**: StepAudio 2.5 — 统一音频语言模型
- **发布日期**: 2026-05-22
- **主要创新**: 统一语音识别/合成/实时对话，所有任务 SOTA
- **链接**: [arXiv:2605.23463](https://arxiv.org/abs/2605.23463)

---

## 18. 01.AI (Yi)

### Yi-Lightning Technical Report
- **中文标题**: Yi-Lightning 技术报告
- **模型系列**: Yi-Lightning (MoE)
- **发布日期**: 2024-10-16
- **主要创新**:
  - 增强 MoE 架构（高级专家分割 + 路由机制）
  - 多阶段训练 + 合成数据构造 + Reward Modeling
  - RAISE (Responsible AI Safety Engine) 四组件安全框架
  - Chatbot Arena 第 6 名整体（中文/数学/编码 第 2-4 名）
- **链接**: [arXiv:2412.01253](https://arxiv.org/html/2412.01253v5)

### Yi: Open Foundation Models
- **中文标题**: Yi: 开放基础模型
- **发布日期**: 2024-03
- **核心参数**: 6B / 34B, 3.1T tokens, GQA + SwiGLU + RoPE ABF
- **链接**: [arXiv:2403.04652](https://arxiv.org/html/2403.04652v1)

---

## 19. Baichuan (百川智能)

### Baichuan-Omni Technical Report
- **中文标题**: Baichuan-Omni 技术报告
- **模型系列**: Baichuan-Omni (7B MLLM)
- **发布日期**: 2024-10
- **主要创新**: 首个开源 7B 全模态模型（图像/视频/音频/文本同时处理）
- **链接**: [arXiv:2410.08565](https://arxiv.org/html/2410.08565)

### Baichuan-M1: Medical Capability LLM
- **中文标题**: Baichuan-M1: 医疗大语言模型
- **模型系列**: Baichuan-M1-14B
- **发布日期**: 2025-02
- **核心参数**: 14B, 20T tokens
- **主要创新**: 从头训练医学专用 LLM，超越 Qwen2.5-72B-Instruct 在医疗任务
- **链接**: [arXiv:2502.12671](https://export.arxiv.org/pdf/2502.12671)

---

## 综合趋势分析

### 🔴 MoE 主导地位巩固
几乎所有新一代模型都采用 MoE 架构：DeepSeek V4 (1.6T)、Kimi K2 (1T)、GLM-5 (744B)、Nemotron 3 (550B)、Qwen3 (235B)、Mistral Large 3 (675B)。Dense 模型主要存在于中小规模（Mistral Medium 3.5 128B, Phi-4 14B, Apple 3B）。

### 🟢 Hybrid Mamba-Transformer 崛起
NVIDIA Nemotron 3 系列是 MoE + Hybrid Mamba-Attention 的先驱，实现 5-7× 推理吞吐提升。这是对纯注意力架构的重要替代方向。

### 🔵 推理模型成为标配
从 DeepSeek-R1 开始，几乎所有公司都推出了推理模型变体：
- OpenAI: GPT-5-thinking / o3
- Anthropic: Hybrid reasoning（Opus 4/Sonnet 4）
- Mistral: Magistral (纯 RL 推理)
- NVIDIA: Llama-Nemotron (动态推理切换)
- Qwen: Unified thinking/non-thinking
- Kimi: K2.5 Thinking

### 🟣 多模态成为基础能力
Llama 4、Gemini 2.5/3、Qwen3.5-Omni、Baichuan-Omni、Step3、Kimi K2.5 均原生支持多模态。视觉-语言联合训练已成标配。

### 🟡 Agentic Capability 竞争白热化
Kimi K2 的 agentic 评估 (SWE-Bench, Tau2-Bench) 成为关键指标。GLM-5 提出从 "Vibe Coding" 到 "Agentic Engineering" 的范式转变。GPT-5.5 强调自主完成复杂真实世界任务。

### ⚪ Scaling Law 持续演进
- 预训练规模：33T (DS V4) → 28.5T (GLM-5) → 25T (Nemotron 3 Super) → 20T (Nemotron 3 Ultra)
- 上下文窗口：1M (DS V4, Nova, Gemini, Nemotron 3) → 256K (Kimi, Qwen3.5, Mistral Medium 3.5) → 128K (DeepSeek V3)
- 激活参数增长：37B (DS V3) → 49B (DS V4) → 55B (Nemotron 3 Ultra) → 40B (GLM-5)
