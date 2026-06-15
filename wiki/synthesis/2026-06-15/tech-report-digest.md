---
title: 大模型技术报告摘要（2025-2026）— 2026-06-15 更新
type: synthesis
created: 2026-06-15
updated: 2026-06-15
tags: [tech-report, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, xai, apple, microsoft, nvidia, amazon, zhipu, internlm, moonshot, stepfun, bytedance]
sources: []
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告综合摘要。整理时间：2026-06-15。涵盖 20 家机构的 30+ 份报告。

---

## 1. DeepSeek

### DeepSeek-V4 技术报告（2026.04）
- **中文标题**：DeepSeek-V4：面向高效百万 Token 上下文智能
- **英文标题**：DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**：DeepSeek-AI
- **模型名称**：DeepSeek-V4-Pro / DeepSeek-V4-Flash
- **发布日期**：2026-04-24
- **核心参数**：
  - V4-Pro：1.6T 总参数 / 49B 激活参数（MoE）
  - V4-Flash：284B 总参数 / 13B 激活参数（MoE）
  - 预训练数据：32T+ tokens
  - 上下文长度：1M tokens（原生支持）
- **主要创新**：
  - Hybrid Attention Architecture：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)
  - 1M 上下文下 V4-Pro 仅需 V3.2 的 27% FLOPs、10% KV Cache
  - Manifold-Constrained Hyper-Connections (mHC) 替代标准残差连接
  - Muon Optimizer 替代 AdamW
  - 两阶段 post-training：specialization → consolidation
  - 训练于华为 Ascend 950PR 芯片
- **链接**：Hugging Face (DeepSeek-V4-Pro / V4-Flash)

### DeepSeek-V3 技术报告（2024.12）
- **英文标题**：DeepSeek-V3 Technical Report
- **模型**：DeepSeek-V3 (671B / 37B active)
- **预训练**：14.8T tokens, 128K context
- **创新**：MLA, MTP, auxiliary-loss-free load balancing, FP8 training
- **链接**：https://arxiv.org/abs/2412.19437

### DeepSeek-R1（2025.01）
- **英文标题**：DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **创新**：纯 RL 激发推理能力，冷启动 + 多阶段训练，蒸馏到小模型
- **链接**：https://arxiv.org/abs/2501.12948（Nature vol.645, 2025）

---

## 2. OpenAI

### GPT-5 System Card（2025.08）
- **中文标题**：GPT-5 系统卡
- **英文标题**：GPT-5 System Card
- **发布机构**：OpenAI
- **模型名称**：GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-thinking-pro / gpt-5-main-mini / gpt-5-thinking-mini / gpt-5-thinking-nano)
- **发布日期**：2025-08-07（System Card 更新至 2026-04-24）
- **主要创新**：
  - 统一系统架构：fast model + deep reasoning model + 实时路由器自动选择
  - gpt-5-main（GPT-4o 后继）+ gpt-5-thinking（o3 后继）
  - 路由器基于用户行为信号持续训练
  - 幻觉率比 o3 降低约 6 倍
  - Safe-completions 安全训练
  - 达到 Preparedness Framework 生物/化学 High capability 级别
- **链接**：https://arxiv.org/abs/2601.03267

### GPT-5.4 Thinking System Card（2026.03）
- **英文标题**：GPT-5.4 Thinking System Card
- **发布机构**：OpenAI
- **发布日期**：2026-03-05
- **主要创新**：
  - 首个实现 Cybersecurity High capability 通用模型
  - 强化 reasoning + 安全 mitigation
  - Conversation monitor 等安全机制
- **链接**：https://deploymentsafety.openai.com/gpt-5-4-thinking/gpt-5-4-thinking.pdf

---

## 3. Meta AI

### Llama 4（2025.04）
- **中文标题**：Llama 4 模型族：原生多模态 AI 创新新时代
- **英文标题**：The Llama 4 Herd: The Beginning of a New Era of Natively Multimodal AI Innovation
- **发布机构**：Meta AI
- **模型名称**：Llama 4 Scout / Llama 4 Maverick / Llama 4 Behemoth（教师模型）
- **发布日期**：2025-04-05
- **核心参数**：
  - Scout：17B active / 109B total (16 experts), 40T tokens, 10M context
  - Maverick：17B active / 400B total (128 experts), 22T tokens, 1M context
  - Behemoth：超 GPT-4.5 / Claude Sonnet 3.7 / Gemini 2.0 Pro（未开源）
- **主要创新**：
  - 首个开源原生多模态 MoE 模型（early fusion）
  - iRoPE + 长度泛化策略（Scout 10M 上下文）
  - Scout 单卡 H100 可跑（INT4 量化）
  - 训练 pipeline：pre-training → mid-training（长上下文扩展）→ post-training（lightweight SFT + online RL + lightweight DPO）
- **论文**：https://arxiv.org/abs/2601.11659

---

## 4. Google DeepMind

### Gemini 3 Pro（2025.11）
- **中文标题**：Gemini 3 Pro 模型卡
- **英文标题**：Gemini 3 Pro Model Card
- **发布机构**：Google DeepMind
- **发布日期**：2025-11（Model Card 更新于 2026-05）
- **核心参数**：
  - 架构：Sparse MoE Transformer（参数量未公开，估计 ~1.5T total / ~180B active）
  - 原生多模态：text, audio, images, video, code repositories
  - Deep Think mode：增强推理模式
- **主要创新**：
  - 最全面的安全评估（Frontier Safety Framework）
  - 减少 sycophancy、抵抗 prompt injection
  - MoE 架构 + 原生多模态预训练
- **链接**：deepmind.google/models/model-cards/gemini-3-pro

### Gemini 3.1 Pro（2026.02）
- **发布日期**：2026-02-19（Preview 于 2026-03-18）
- **核心参数**：
  - 2M token 上下文窗口
  - Extended-locality attention（ring attention 变体）
  - Deep Think mode
- **表现**：LMSys Arena Elo ~1500（#1），GPQA Diamond 94.3%
- **链接**：deepmind.google/models/model-cards/gemini-3-1-pro

### Gemini 3 Technical Report（2026.03）
- **英文标题**：Gemini 3 Technical Report
- **发布日期**：2026-03-18
- **文档**：Sparse MoE, native multimodal input, extended-locality attention

---

## 5. Anthropic

### Claude Opus 4 & Sonnet 4（2025.05）
- **中文标题**：Claude Opus 4 和 Claude Sonnet 4 系统卡
- **英文标题**：System Card: Claude Opus 4 & Claude Sonnet 4
- **发布机构**：Anthropic
- **发布日期**：2025-05-22
- **核心参数**：
  - Opus 4：ASL-3 安全等级，Sonnet 4：ASL-2
  - 混合推理模型（hybrid reasoning）：近即时响应 + extended thinking
  - Opus 4：SWE-bench 72.5%, Terminal-bench 43.2%
- **主要创新**：
  - Constitutional AI + RLHF 对齐
  - 首次包含 alignment assessment + model welfare assessment
  - 65% 减少 reward hacking 行为
  - Opus 4 支持长时间自主编程（数小时连续工作）
- **链接**：https://anthropic.com/claude-4-model-card

### Claude Opus 4.7（2026.04）
- **发布日期**：2026-04
- **改进**：软件工程能力显著提升，最难任务上增益最大
- **知识截止**：2026-01
- **安全等级**：CB-1

---

## 6. Mistral AI

### Mistral Large 3（2025.12）
- **中文标题**：Mistral Large 3 技术文档
- **英文标题**：Mistral Large 3 Technical Documentation
- **发布机构**：Mistral AI
- **发布日期**：2025-12-02
- **核心参数**：
  - Sparse MoE：41B active / 675B total
  - 上下文长度：256K tokens
  - 训练于 ~3,000 H200 GPUs
  - 原生多模态（text + image）
- **主要创新**：Apache 2.0 开源，训练于 exascale NVIDIA 集群，granular MoE
- **链接**：https://docs.mistral.ai

### Ministral 3（2026.01）
- **英文标题**：Ministral 3
- **发布日期**：2026-01
- **核心参数**：3B / 8B / 14B 三个尺寸，每个有 base/instruct/reasoning 三种变体
- **主要创新**：Cascade Distillation — 迭代剪枝 + 继续训练 + 蒸馏；Apache 2.0；256K context；图像理解
- **链接**：https://arxiv.org/abs/2601.08584

### Magistral 推理模型（2025.06）
- **英文标题**：Magistral: Mistral's First Reasoning Model
- **发布日期**：2025-06
- **核心参数**：Magistral Small (Apache 2.0) / Magistral Medium
- **主要创新**：纯 RL 训练推理模型；RL on text 保持多模态/指令遵循/函数调用能力；冷启动数据蒸馏
- **链接**：https://arxiv.org/abs/2506.10910

### Mistral Medium 3.5（2026.05）
- **发布日期**：2026-05-22
- **核心参数**：128B Dense, 256K context; SWE-Bench 77.6%
- **主要创新**：首款 flagship merged model（指令遵循+推理+编码合并）；可配置 reasoning effort
- **链接**：https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5/

---

## 7. Alibaba / Qwen

### Qwen3 Technical Report（2025.04）
- **中文标题**：Qwen3 技术报告
- **英文标题**：Qwen3 Technical Report
- **发布机构**：Alibaba Cloud / Qwen Team
- **发布日期**：2025-04-29
- **核心参数**：
  - Dense 系列：0.6B / 1.7B / 4B / 8B / 14B / 32B
  - MoE 系列：30B-A3B / 235B-A22B
  - 总训练数据 36T tokens（部分尺寸）
  - 扩展至 1M context（2507 更新版）
- **主要创新**：
  - 统一 thinking mode + non-thinking mode（动态切换）
  - Thinking budget 机制：自适应分配推理计算
  - 四阶段训练：long CoT cold start → reasoning RL → thinking mode fusion → general RL
  - 覆盖 119 语言和方言
- **论文链接**：https://arxiv.org/abs/2505.09388

### Qwen3.5-Omni（2026.04）
- **英文标题**：Qwen3.5-Omni Technical Report
- **发布日期**：2026-04
- **核心参数**：Plus / Flash 变体, 256K context
- **主要创新**：
  - Thinker-Talker 架构 + Hybrid-Attention MoE
  - 原生全模态 agent：文本/图像/音频/视频理解 + 语音生成 + FunctionCall
  - ARIA 动态对齐文本和语音单元
  - 113 语言语音识别，36 语言语音合成
- **论文链接**：https://arxiv.org/abs/2604.15804

---

## 8. Microsoft

### Phi-4 Technical Report（2024.12）
- **英文标题**：Phi-4 Technical Report
- **发布机构**：Microsoft Research
- **发布日期**：2024-12
- **核心参数**：14B 参数，dense transformer
- **主要创新**：
  - 数据质量优先：大规模合成数据
  - 超越教师模型 GPT-4o（STEM QA）
  - Pivotal Token Search (PTS) for DPO
- **论文链接**：https://arxiv.org/abs/2412.08905

### Phi-4-reasoning Technical Report（2025.04）
- **英文标题**：Phi-4-reasoning Technical Report
- **发布日期**：2025-04
- **核心参数**：14B 参数
- **主要创新**：
  - SFT on o3-mini reasoning traces（1.4M teachable prompts）+ outcome-based RL
  - 超越 DeepSeek-R1-Distill-Llama-70B
  - 非平凡迁移到通用 benchmark
- **论文链接**：https://arxiv.org/abs/2504.21318

### Phi-4-reasoning-vision-15B（2026.03）
- **英文标题**：Phi-4-reasoning-vision-15B Technical Report
- **发布日期**：2026-03
- **主要创新**：小模型多模态推理；high-resolution dynamic-resolution encoder；hybrid reasoning/non-reasoning data
- **论文链接**：https://arxiv.org/abs/2603.03975

---

## 9. Apple

### Apple Intelligence Foundation Language Models Tech Report 2025（2025.07）
- **中文标题**：Apple Intelligence 基础语言模型技术报告 2025
- **英文标题**：Apple Intelligence Foundation Language Models Tech Report 2025
- **发布机构**：Apple
- **发布日期**：2025-07-17
- **核心参数**：
  - On-device：~3B 参数（dense），KV-cache sharing + 2-bit 量化感知训练
  - Server：Parallel-Track MoE (PT-MoE) transformer
  - 覆盖 16 语言，多模态（text + image），工具调用
- **主要创新**：
  - PT-MoE：track parallelism + MoE + interleaved global-local attention
  - Private Cloud Compute 平台
  - Foundation Models framework for developers
  - 负责任 AI + 内容过滤
- **论文链接**：https://arxiv.org/abs/2507.13575

### AFM 3 / 第三代 Apple Foundation Models（2026.06）
- **发布日期**：2026-06-08（WWDC26 预告）
- **核心参数**：5 个模型（3 on-device + 3 server including ADM 3 Cloud for image）
- **特点**：与 Google 合作定制；全新 Siri AI；3B-parameter AFM 3 Core
- **状态**：Technical Report 将在夏季晚些时候发布

---

## 10. NVIDIA

### Nemotron 3 Family（2025-2026）
- **中文标题**：Nemotron 3：高效开源智能
- **英文标题**：NVIDIA Nemotron 3: Efficient and Open Intelligence
- **发布机构**：NVIDIA
- **模型**：Nano (30B-A3B) / Super (120B-A12B) / Ultra (550B-A55B)
- **核心参数**：
  - Mixture-of-Experts hybrid Mamba-Transformer 架构
  - 上下文长度：1M tokens
  - 预训练数据：25T tokens（Nano/Super），20T tokens（Ultra）
  - NVFP4 预训练（Super/Ultra）
  - LatentMoE + Multi-Token Prediction (MTP)
- **主要创新**：
  - Hybrid Mamba-Attention：大幅降低 KV cache + 加速推理
  - Ultram 比 Qwen3.5-397B 高 1.6× 吞吐
  - 多环境 RL（multi-environment RLVR）
  - 推理 budget 控制
- **链接**：https://arxiv.org/abs/2512.20856

### Llama-Nemotron（2025.06）
- **英文标题**：Llama-Nemotron: Efficient Reasoning Models
- **发布日期**：2025-06
- **核心参数**：Nano (8B) / Super (49B) / Ultra (253B)，128K context
- **主要创新**：
  - 基于 Llama 3 的 Neural Architecture Search + Knowledge Distillation
  - 动态 reasoning toggle（standard chat ↔ reasoning）
  - Ultra 超越 DeepSeek-R1
- **论文链接**：https://arxiv.org/abs/2505.00949

---

## 11. xAI

### Grok 3（2025.02）
- **中文标题**：Grok 3 Beta — 推理智能体时代
- **英文标题**：Grok 3 Beta — The Age of Reasoning Agents
- **发布机构**：xAI
- **发布日期**：2025-02-17
- **核心参数**：
  - 参数量未披露（估计 300B-400B active 或 MoE 2.7T total）
  - 上下文：131K tokens
  - 训练于 Colossus 超算（200,000 H100 GPU）
  - 10× 前代计算量
- **主要创新**：
  - 大规模 RL 训练推理能力（RL-at-scale）
  - Think mode：自纠正、回溯、简化中间步骤
  - Grok 3 Mini：高性价比推理
  - DeepSearch：实时互联网 + X 数据访问
  - AIME 2025: 93.3% (cons@64), GPQA: 84.6%, LiveCodeBench: 79.4%
  - Chatbot Arena Elo 1402（首个破 1400 的模型）
- **链接**：https://x.ai/news/grok-3

### Grok 4 Fast Model Card（2025.09）
- **发布日期**：2025-09-19
- **特点**：接近 Grok 4 推理能力但更低延迟和成本；安全评估涵盖 abuse potential, concerning propensities, dual-use capabilities
- **链接**：https://data.x.ai/2025-09-19-grok-4-fast-model-card.pdf

---

## 12. Amazon

### Amazon Nova Family Technical Report（2025.03）
- **中文标题**：Amazon Nova 模型族技术报告与模型卡
- **英文标题**：The Amazon Nova Family of Models: Technical Report and Model Card
- **发布机构**：Amazon AGI
- **发布日期**：2025-03
- **核心参数**：
  - Nova Micro：text-only，最低延迟
  - Nova Lite：低成本多模态，300K context
  - Nova Pro：高能力多模态，300K context
  - Nova Canvas：图像生成
  - Nova Reel：视频生成
- **论文链接**：https://arxiv.org/abs/2506.12103

### Amazon Nova Premier（2025.04）
- **发布日期**：2025-04-30
- **特点**：旗舰多模态模型，1M context window，教师模型
- **链接**：amazon.science

### Amazon Nova 2（2025.12）
- **英文标题**：Amazon Nova 2: Multimodal reasoning and generation models
- **发布日期**：2025-12-02
- **核心参数**：
  - Nova 2 Lite / Pro：多模态 + 可配置 extended thinking
  - Nova 2 Omni：统一多模态（text/image/video/audio 输入，text/image 输出）
  - Nova 2 Sonic：speech-to-speech
  - 1M context window
- **链接**：amazon.science

---

## 13. Zhipu AI (GLM)

### GLM-5（2026.02）
- **中文标题**：GLM-5：从 Vibe Coding 到 Agentic Engineering
- **英文标题**：GLM-5: From Vibe Coding to Agentic Engineering
- **发布机构**：Zhipu AI & Tsinghua University
- **发布日期**：2026-02-12
- **核心参数**：
  - 744B 总参数 / 40B 激活参数（MoE）
  - 预训练数据：28.5T tokens
  - 上下文：200K tokens
  - MIT License 开源
- **主要创新**：
  - DeepSeek Sparse Attention (DSA)：降低 1.5-2× 计算成本
  - Asynchronous RL 基础设施（slime 框架）：解耦生成与训练
  - 异步 Agent RL 算法
  - 全栈国产芯片适配（华为昇腾、摩尔线程、海光、寒武纪等）
  - 训练 pipeline：pre-training (27T) → mid-training (4K→200K extension) → post-training (Reasoning RL → Agentic RL → General RL + On-Policy Cross-Stage Distillation)
- **论文链接**：https://arxiv.org/abs/2602.15763

---

## 14. Shanghai AI Lab (InternLM)

### InternLM2 Technical Report（2024.03）
- **英文标题**：InternLM2 Technical Report
- **发布日期**：2024-03-26
- **模型**：InternLM2 系列（1.8B / 7B / 20B）
- **创新**：COOL RLHF（条件在线强化学习）；32K context，200K Needle-in-Haystack
- **论文链接**：https://arxiv.org/abs/2403.17297

### InternLM3（2025.01）
- **发布**：2025-01-15
- **模型**：InternLM3-8B-Instruct
- **创新**：仅 4T 高质量 tokens（节省 75%+ 训练成本）；支持 deep thinking mode + normal response mode

### Intern-S1-Pro（2026.02）
- **英文标题**：Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale
- **发布日期**：2026-02-04
- **核心参数**：
  - 1T 总参数 / 22B 激活参数（MoE, 64 experts, 8 active）
  - 科学多模态基础模型
- **主要创新**：
  - 首个万亿参数科学多模态模型
  - Expert expansion + Grouped Routing
  - XTuner + LMDeploy 基础设施协同优化
  - 覆盖化学、材料、生命科学、地球科学等 100+ 科学任务
- **论文链接**：https://arxiv.org/abs/2603.25040

---

## 15. Moonshot AI (Kimi)

### Kimi K2（2025.07）
- **中文标题**：Kimi K2：开放智能体智能
- **英文标题**：Kimi K2: Open Agentic Intelligence
- **发布机构**：Moonshot AI
- **发布日期**：2025-07-28
- **核心参数**：
  - MoE：1.04T 总参数 / 32B 激活参数（384 experts, 8 active per token）
  - 上下文：128K（后更新至 256K）
  - 预训练：15.5T tokens
  - MLA Attention + SwiGLU
- **主要创新**：
  - MuonClip Optimizer：Muon + QK-Clip 防止训练不稳定（零 loss spike）
  - 大规模 agentic data synthesis pipeline
  - 联合 RL stage（真实 + 合成环境交互）
  - 非 thinking 模型 SOTA：SWE-bench 65.8%, Tau2-Bench 66.1%, ACEBench 76.5%
  - LiveCodeBench v6 53.7（超 GPT-4.1 44.7）
- **论文链接**：https://arxiv.org/abs/2507.20534

### Kimi K2.5（2026.02）
- **英文标题**：Kimi K2.5: Visual Agentic Intelligence
- **发布日期**：2026-02
- **核心参数**：基于 K2，多模态增强
- **主要创新**：joint text-vision pre-training; zero-vision SFT; joint text-vision RL; Agent Swarm（动态任务分解 + 并行执行，加速 4.5×）
- **论文链接**：https://arxiv.org/abs/2602.02276

### Kimi K2.6（2026.04）
- **发布日期**：2026-04-29
- **增强**：300 子 agent 并行编排、4000 步协调、MoonViT (400M) vision encoder、长程编码
- **链接**：Hugging Face (MoonshotAI/Kimi-K2.6)

---

## 16. StepFun (阶跃星辰)

### Step 3（2025.07）
- **中文标题**：Step-3：大而可负担——面向成本高效解码的模型-系统协同设计
- **英文标题**：Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding
- **发布机构**：StepFun（阶跃星辰）
- **发布日期**：2025-07
- **核心参数**：
  - 321B 总参数 / 38B 激活参数（MoE, 48 experts, 3 active）
  - 上下文：65K tokens
  - MFA (Multi-Matrix Factorization Attention)
- **主要创新**：
  - MFA 注意力机制：低秩 query 降低 KV 缓存
  - AFD (Attention-FFN Disaggregation)：解耦 Attention 和 FFN 计算
  - 5B Vision Encoder + 2D 卷积下采样（视觉 token 减少 16×）
  - 在 Hopper GPU 上吞吐 4039 token/gpu/s（DeepSeek V3: 2324）
  - 国产芯片友好（最高达 DeepSeek-R1 300% 效率）
- **论文链接**：https://arxiv.org/abs/2507.19427

### Step 3.5 Flash（2026.02）
- **发布日期**：2026-02-12
- **核心参数**：196B total / 11B active (MoE), 256K context, MTP-3
- **主要创新**：
  - 3-way Multi-Token Prediction (MTP-3)
  - 3:1 Sliding Window Attention ratio
  - SWE-bench Verified 74.4%, Terminal-Bench 2.0 51.0%
  - 生成吞吐 100-300 tok/s（峰值 350）
- **论文链接**：https://arxiv.org/abs/2602.10604

### Step-DeepResearch（2025.12）
- **英文标题**：Step-DeepResearch Technical Report
- **发布日期**：2025-12
- **核心参数**：32B 参数，端到端 Deep Research agent
- **创新**：原子能力拆解（planning/search/reflection/report writing）；渐进式训练（mid-training → SFT → RL）；Checklist Judger 奖励设计
- **论文链接**：https://arxiv.org/abs/2512.20491

---

## 17. ByteDance (豆包/Doubao)

### Seed1.8（2025.12）
- **中文标题**：Seed1.8：通用智能体模型
- **英文标题**：Seed1.8: A Generalized Agentic Model
- **发布机构**：ByteDance Seed
- **发布日期**：2025-12-17
- **核心参数**：
  - 支持四种 thinking mode：no_think / think-low / medium / high
  - 多模态（text + image）
  - 高效 agent 能力（search, coding, tool use, GUI）
- **主要创新**：
  - 动态推理计算分配
  - 真实世界评估体系
  - 多模态 token 效率优化
- **链接**：https://research.doubao.com

### Seed2.0（2026.02）
- **中文标题**：豆包大模型 2.0 / Seed2.0
- **发布日期**：2026-02-14
- **模型**：Pro / Lite / Mini + Code 模型
- **核心参数**：
  - Pro：对标 GPT-5.2 和 Gemini 3 Pro
  - SuperGPQA 超 GPT-5.2
  - HLE-text 最高分 54.2
  - IMO/CMO 金牌水平，ICPC 金牌
  - 大幅降低推理成本（token 定价低一个数量级）
- **链接**：https://seed.bytedance.com

### UltraMem 架构研究
- **内容**：ByteDance 提出 UltraMem 稀疏架构，推理成本较 MoE 降低最高 83%，速度提升 2-6 倍
- **论文**：ICLR 2025

### Seed-Coder（2025.05）
- **英文标题**：Seed-Coder: Let the Code Model Curate Data for Itself
- **模型**：8B base/instruct/reasoning
- **创新**：模型自策展代码训练数据，SOTA 8B 代码模型
- **论文链接**：https://arxiv.org/abs/2506.03524

---

## 18. Yi (01.AI) & Baichuan

截至 2026-06-15，Yi (01.AI) 和 Baichuan 未发布新的公开 Tech Report。Yi 系列最新公开为 Yi-Lightning / Yi-Large（2024），Baichuan 最新为 Baichuan 4 (2024)。状态：等待新版本发布。

---

## 跨领域趋势总结

### 架构趋势
| 方向 | 代表机构 |
|------|---------|
| MoE 大规模化 | DeepSeek (1.6T), Kimi (1T), GLM-5 (744B), Mistral (675B), Qwen (235B), StepFun (321B) |
| Hybrid Mamba-Transformer | NVIDIA Nemotron 3 全系列 |
| 稀疏注意力（DSA/CSA/HCA） | DeepSeek V4, GLM-5, StepFun MFA |
| 原生多模态（Early Fusion） | Meta Llama 4, Google Gemini 3, Amazon Nova 2 |
| 推理/非推理统一模型 | Qwen3, DeepSeek V4, Phi-4-reasoning, Claude 4 |

### 训练方法趋势
| 方向 | 代表 |
|------|------|
| 纯 RL 激发推理 | DeepSeek-R1, Magistral |
| 异步 RL 基础设施 | GLM-5 (slime), Kimi K2 |
| 数据质量 > 数据规模 | Phi-4, Apple AFM, InternLM3 |
| 合成数据大规模使用 | Phi-4, DeepSeek V4, Kimi K2 |
| 多阶段 post-training | DeepSeek V4 (specialization+consolidation), Qwen3 (4-stage), GLM-5 |

### Scaling Law / 缩放分析
- ByteDance UltraMem 揭示新稀疏架构的 Scaling Law
- DeepSeek V4 证明 Muon Optimizer 在 1.6T 参数规模有效
- Mistral Ministral 3 通过 Cascade Distillation 实现数据高效缩放
- NVIDIA Nemotron 3 展示 hybrid 架构的 scaling 优势

### 多模态
| 能力层级 | 代表模型 |
|----------|---------|
| Text + Image 理解 | 几乎所有模型 |
| Audio + Video 理解 | Gemini 3, Qwen3.5-Omni, Amazon Nova 2 |
| 图像生成 | Amazon Nova Canvas, Seedream 2.0 |
| 视频生成 | Amazon Nova Reel |
| Speech-to-Speech | Amazon Nova 2 Sonic |
| 科学多模态 | Intern-S1-Pro (1T) |

### 长上下文
| 模型 | 上下文长度 |
|------|-----------|
| Gemini 3.1 Pro | 2M tokens |
| DeepSeek V4 | 1M tokens |
| Llama 4 Scout | 10M tokens |
| Amazon Nova 2 | 1M tokens |
| NVIDIA Nemotron 3 | 1M tokens |
| Anthropic Claude Opus 4 | 1M tokens |

### 推理 / Reasoning 模型
| 模型 | 类型 |
|------|------|
| GPT-5 (thinking) | 统一 + 路由器 |
| DeepSeek-R1 | 纯 RL |
| Qwen3 (thinking mode) | 统一模型内切换 |
| Claude 4 (extended thinking) | 混合推理 |
| Magistral | 纯 RL |
| Grok 3 Think | RL-at-scale |
| Phi-4-reasoning | SFT + RL |
| Step 3.5 Flash | MTP-3 加速推理 |
