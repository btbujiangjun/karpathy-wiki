---
title: 大模型技术报告摘要（2025-2026）— 2026-06-17 更新
type: synthesis
created: 2026-06-17
updated: 2026-06-17
tags: [tech-report, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, xai, apple, microsoft, nvidia, amazon, zhipu, internlm, moonshot, stepfun, bytedance, yi, baichuan]
sources: []
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告综合摘要。整理时间：2026-06-17。涵盖 22 家机构的 40+ 份报告。

---

## 1. DeepSeek

### DeepSeek-V4 技术报告（2026.04）
- **中文标题**：DeepSeek-V4：面向高效百万 Token 上下文智能
- **英文标题**：DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**：DeepSeek-AI
- **模型名称**：DeepSeek-V4-Pro / DeepSeek-V4-Flash
- **发布日期**：2026-04-24
- **核心参数**：
  - V4-Pro：1.6T 总参数 / 49B 激活参数 (MoE)
  - V4-Flash：284B 总参数 / 13B 激活参数 (MoE)
  - 预训练数据：32T+ tokens
  - 上下文长度：1M tokens（原生，max output 384K）
  - MIT License，open weights
- **主要创新**：
  - Hybrid Attention：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)
  - 1M 上下文下 V4-Pro 仅需 V3.2 的 27% FLOPs、10% KV Cache
  - Manifold-Constrained Hyper-Connections (mHC)
  - Muon Optimizer
  - 两阶段 post-training
  - 训练于华为 Ascend 950PR 芯片
- **SWE-bench Verified**：80.6%（自报，未独立复现）
- **链接**：HuggingFace deepseek-ai/DeepSeek-V4

### DeepSeek-V3.2（2025.12）
- **英文标题**：DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
- **模型**：671B / 37B active (MoE)
- **创新**：DeepSeek Sparse Attention (DSA)，可扩展 RL 框架，Agentic 任务合成管线
- V3.2-Speciale：IMO 2025 + IOI 2025 金牌级性能
- **链接**：https://arxiv.org/abs/2512.02556

### DeepSeek-R1（2025.01）
- **英文标题**：DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **模型**：671B / 37B active，128K context
- **创新**：纯 RL 激发推理能力（R1-Zero），冷启动 + 多阶段 RL（R1），蒸馏到小模型
- **链接**：https://arxiv.org/abs/2501.12948（Nature vol.645）

---

## 2. OpenAI

### GPT-5 System Card（2025.08）
- **中文标题**：GPT-5 系统卡
- **英文标题**：GPT-5 System Card
- **模型系列**：GPT-5 (main / thinking / thinking-pro / main-mini / thinking-mini / thinking-nano)
- **发布日期**：2025-08-13（System Card 更新至 2026-04-24）
- **主要创新**：
  - 统一架构：fast model + deep reasoning + 实时路由器
  - gpt-5-main = GPT-4o 后继，gpt-5-thinking = o3 后继
  - 路由器基于用户行为信号持续训练
  - 幻觉率比 o3 降低约 6 倍
  - Safe-completions 安全训练
  - 达到 Preparedness Framework Bio/Chem High capability 级别
- **链接**：https://arxiv.org/abs/2601.03267

### GPT-5.5 Instant System Card（2026.05）
- **英文标题**：GPT-5.5 Instant System Card
- **发布日期**：2026-05-04
- **创新**：首个 Instant 模型达到 Cybersecurity 和 Bio/Chem High capability 级别
- **链接**：https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf

### OpenAI o3 / o4-mini System Card（2025.04）
- **模型**：o3（reasoning）+ o4-mini（轻量 reasoning）
- **发布日期**：2025-04-16
- **创新**：state-of-the-art reasoning + 工具能力（web browsing, Python, image, canvas）
- 首个在 updated Preparedness Framework v2 下发布的系统卡
- **链接**：OpenAI 官网

### GPT-4.5 System Card（2025.02）
- **英文标题**：OpenAI GPT-4.5 System Card
- **发布日期**：2025-02-27
- **创新**：最大预训练规模模型，新监督技术，降低幻觉，增强 EQ
- **链接**：https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf

---

## 3. Meta AI (LLaMA)

### Llama 4 系列（2025.04）
- **中文标题**：Llama 4 羊群：原生多模态 AI 创新新时代的开端
- **英文标题**：The Llama 4 Herd: The Beginning of a New Era of Natively Multimodal AI Innovation
- **发布机构**：Meta AI
- **模型系列**：Llama 4 Scout / Llama 4 Maverick / Llama 4 Behemoth（teacher）
- **发布日期**：2025-04-05
- **核心参数**：
  - Scout：17B active / 109B total，16 experts，MoE，10M context
  - Maverick：17B active / 400B total，128 experts，MoE，1M context
  - Behemoth（teacher model，未发布）
  - Scout 训练数据 ~40T tokens，Maverick ~22T tokens
- **架构**：首个原生多模态 MoE（early fusion），文本+图像统一处理
- **链接**：https://ai.meta.com/blog/llama-4-multimodal-intelligence/

### Llama 3 Herd of Models（2024.07）
- **英文标题**：The Llama 3 Herd of Models
- **模型**：8B/70B/405B（dense），128K context，15T+ tokens
- **链接**：https://arxiv.org/abs/2407.21783

### Llama 5（2026.04 传闻）
- 媒体报道参数 600B+，1M context，原生多模态
- 声称支持 recursive self-improvement（推理时权重优化）
- 尚未经独立验证
- **arXiv**： reportedly 2604.11002（未确认）

---

## 4. Google DeepMind (Gemini)

### Gemini 2.5 技术报告（2025.07）
- **中文标题**：Gemini 2.5：以前沿推理、多模态、长上下文和下一代 Agent 能力推动边界
- **英文标题**：Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **发布机构**：Google DeepMind
- **模型系列**：Gemini 2.5 Pro / Gemini 2.5 Flash / Gemini 2.0 Flash / Gemini 2.0 Flash-Lite
- **发布日期**：2025-07-07（technical report）
- **核心参数**：
  - Sparse MoE Transformer 架构
  - 1M token 上下文（Pro），64K token output
  - 知识截止：2025.01
  - 原生多模态（text, image, audio, video）
  - 视频处理：最高 3 小时（1M context 内）
- **主要创新**：
  - Thinking model（推理时思考）
  - Deep Think 模式（IO 2025 发布）
  - 可配置 thinking budget
  - Agentic capabilities（自动玩 Pokémon）
  - Sparse MoE 架构延续
  - Aider Polyglot: 82.2%（SOTA）
- **链接**：https://arxiv.org/abs/2507.06261

---

## 5. Anthropic (Claude)

### Claude Opus 4 & Sonnet 4 System Card（2025.05）
- **中文标题**：Claude Opus 4 和 Claude Sonnet 4 系统卡
- **英文标题**：System Card: Claude Opus 4 & Claude Sonnet 4
- **发布机构**：Anthropic
- **发布日期**：2025-05-22
- **主要创新**：
  - Hybrid reasoning model（即时 + extended thinking 双模式）
  - Opus 4：SWE-bench Verified 72.5%，Terminal-bench 43.2%
  - Sonnet 4：coding + reasoning 显著升级
  - Opus 4 在 ASL-3 标准下发布
  - 首次包含 alignment assessment 和 model welfare assessment
- **链接**：https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf

### Claude Opus 4.6 System Card（2026.02）
- **发布日期**：2026-02-06
- **创新**：
  - 首个 Opus 级 1M token 上下文
  - Adaptive thinking（4 级 effort: low/medium/high/max）
  - Context compaction（自动压缩历史上下文）
  - 128K token output
- **链接**：Anthropic 官网

### Claude Opus 4.7（2026.04）
- **发布日期**：2026-04-16
- **改进**：软件工程能力显著提升，更新 tokenizer，在 agentic 场景下思考更多
- 安全的 profile 稳定或改善
- Claude Mythos Preview 同期发布
- **链接**：https://www.anthropic.com/news/claude-opus-4-7

### Claude Fable 5 & Mythos 5（2026.06）
- 最新一代 Claude，2026 年 6 月发布
- 系统卡已发布

---

## 6. Mistral AI

### Mistral 3 / Mistral Large 3（2025.12）
- **中文标题**：Mistral 3 系列
- **英文标题**：Introducing Mistral 3
- **发布机构**：Mistral AI
- **发布日期**：2025-12-02
- **模型系列**：Mistral Large 3 + Ministral 3 (14B/8B/3B)
- **核心参数**：
  - Large 3：675B total / 41B active (MoE)，256K context
  - Ministral 3：14B/8B/3B dense，256K context，多模态
  - 训练于 3000×H200 GPU
  - 全部 Apache 2.0 开源
- **主要创新**：
  - Mistral 首个 MoE 模型（自 Mixtral 以来）
  - 原生图像理解 + 多语言能力
  - Cascade Distillation 技术（迭代剪枝 + 蒸馏）
- **链接**：https://mistral.ai/news/mistral-3/

### Magistral（2025.06）
- **英文标题**：Magistral
- **模型**：Magistral Medium（enterprise）/ Magistral Small（24B open-source）
- **创新**：Mistral 首个推理模型，纯 RL 训练（从头搭建 RL 管线）
- RL on text 可保持多模态理解/function calling 能力
- **链接**：https://arxiv.org/abs/2506.10910

### Mistral Small 4（2026.03）
- **英文标题**：Introducing Mistral Small 4
- **创新**：首个 unified 模型（推理+多模态+agentic coding 合一）
- 可配置 reasoning effort
- Apache 2.0，NVIDIA Nemotron Coalition 创始成员
- **链接**：https://mistral.ai/news/mistral-small-4

### Mistral Medium 3.5（2026.04）
- 128B dense，256K context，多模态
- 修改版 MIT license（open weights）
- SWE-bench Verified: 77.6%
- 替代 Devstral 2 / Pixtral / Medium 三合一
- **链接**：https://mistral.ai/news/

---

## 7. Qwen (Alibaba)

### Qwen3 技术报告（2025.05）
- **中文标题**：Qwen3 技术报告
- **英文标题**：Qwen3 Technical Report
- **发布机构**：Alibaba Qwen Team
- **模型系列**：Qwen3 (0.6B ~ 235B)
- **发布日期**：2025-05-10
- **核心参数**：
  - 旗舰模型 Qwen3-235B-A22B (MoE)
  - Dense + MoE 两种架构
  - 多语言扩展至 119 种语言/方言
- **主要创新**：
  - Thinking + Non-thinking 统一框架
  - Thinking budget 机制
  - 动态 mode switching
  - 所有模型 Apache 2.0 开源
- **链接**：https://arxiv.org/abs/2505.09388

### Qwen3.5-Omni（2026.03）
- **英文标题**：Qwen3.5-Omni Technical Report
- **发布日期**：2026-03
- **创新**：
  - 原生全模态模型（Thinker-Talker 架构）
  - Hybrid-Attention MoE
  - 256K context，10+ hours audio，400+ sec 720p video
  - 113 语言语音识别，36 语言语音生成
  - 215 项 audio/audio-visual SOTA
- **链接**：https://arxiv.org/abs/2604.15804

### Qwen3-Max（2025.10）
- 1T+ 参数，36T tokens 预训练
- SWE-bench Verified: 69.6%，Tau2-Bench: 74.8%
- Thinking 变体 AIME 25 / HMMT 100%
- **链接**：Alibaba Cloud Blog

### Qwen3.6-27B（2026.04）
- 首个 Qwen3.6 dense 模型
- Hybrid Gated DeltaNet + Gated Attention
- SWE-bench Verified: 77.2%，Terminal-Bench 2.0: 59.3
- 262K context (YaRN 可扩至 1M)
- Apache 2.0
- **链接**：HuggingFace

---

## 8. xAI (Grok)

### Grok 4 Model Card（2025.08）
- **英文标题**：Grok 4 Model Card
- **发布机构**：xAI
- **发布日期**：2025-08-20
- **核心参数**：~1.7T 参数（估计），多模态，256K context
- **主要创新**：
  - 首个 50%+ Humanity's Last Exam（50.7% text-only）
  - USAMO'25: 61.9%（Heavy 变体）
  - ARC-AGI V2: 15.9%（几乎 2× Opus 4）
  - Native tool use + web search
  - 多种技术：human feedback, verifiable rewards, model grading RL
- **链接**：https://data.x.ai/2025-08-20-grok-4-model-card.pdf

### Grok 4.1 Model Card（2025.11）
- **发布日期**：2025-11-17
- **创新**：Thinking + Non-thinking 双配置，更自然的多轮对话
- 改进的 input filter 模型
- **链接**：https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf

### Grok 4 Fast Model Card（2025.09）
- **发布日期**：2025-09-19
- 低延迟低成本 reasoning，可跳过推理

---

## 9. Apple

### Apple Intelligence Foundation Language Models Tech Report 2025（2025.07）
- **中文标题**：Apple Intelligence 基础语言模型技术报告 2025
- **英文标题**：Apple Intelligence Foundation Language Models Tech Report 2025
- **发布机构**：Apple
- **模型系列**：AFM-on-device (~3B) + AFM-server (PT-MoE)
- **发布日期**：2025-07-17
- **核心参数**：
  - On-device：~3B 参数，KV-cache sharing，2-bit QAT
  - Server：Parallel-Track MoE transformer
  - 多语言（16 种），多模态（text + image）
  - Private Cloud Compute
- **主要创新**：
  - PT-MoE (Parallel-Track Mixture-of-Experts)
  - Track parallelism + interleaved global-local attention
  - KV-cache sharing + 2-bit quantization-aware training
  - 异步 RL 训练平台
  - Swift Foundation Models framework
- **链接**：https://arxiv.org/abs/2507.13575

### AFM 3 第三代（2026.06）
- 5 个模型：AFM 3 Core (3B dense) / AFM 3 Core Advanced (20B sparse, 1-4B active) / AFM 3 Cloud / ADM 3 Cloud (Image) / AFM 3 Cloud Pro
- 与 Google 合作构建，首次在 Google Cloud NVIDIA GPU 上运行 PCC
- Instruction-Following Pruning (IFP) 实现 20B 模型在设备上运行
- **链接**：https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models

---

## 10. NVIDIA

### Nemotron 3 Ultra（2026.04）
- **中文标题**：Nemotron 3 Ultra：用于 Agentic 推理的开放高效 MoE Hybrid Mamba-Transformer 模型
- **英文标题**：Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning
- **发布机构**：NVIDIA
- **模型**：550B total / 55B active (MoE)
- **发布日期**：2026-04
- **核心参数**：
  - Hybrid Mamba-Attention 架构
  - 20T tokens 预训练，1M context
  - LatentMoE + MTP + NVFP4 预训练
- **主要创新**：
  - MoE + Hybrid Mamba-Transformer 结合
  - LatentMoE（更高 accuracy per parameter）
  - Multi-teacher On-Policy Distillation (MOPD)
  - 推理吞吐比 GLM-5.1 高 5.9×，比 Kimi-K2.6 高 4.8×
- **链接**：NVIDIA Nemotron Research

### Nemotron 3 Super（2026.04）
- 12B active / 120B total MoE Hybrid Mamba-Attention
- LatentMoE + MTP，25T tokens 预训练
- 可达 2.2× Qwen3.5-122B 推理吞吐
- **链接**：https://arxiv.org/abs/2604.12374

### Llama-Nemotron（2025.05）
- **英文标题**：Llama-Nemotron: Efficient Reasoning Models
- **模型**：LN-Nano (8B) / LN-Super (49B) / LN-Ultra (253B)
- **创新**：基于 Llama 3 做 NAS 优化推理效率，蒸馏 + RL 训练
- 首个支持 dynamic reasoning toggle 的开源模型
- LN-Ultra 在单个 8×H100 节点上运行
- **链接**：https://arxiv.org/abs/2505.00949

### RLP（2026.04）
- **英文标题**：RLP: Reinforcement as a Pretraining Objective
- **创新**：将 RL 引入预训练阶段（而非仅 post-training）
- Chain-of-thought 作为探索行为，信息论奖励
- Qwen3-1.7B +19%，Nemotron-Nano-12B +43%
- ICLR 2026
- **链接**：NVIDIA Research

### Nemotron-Labs Diffusion（2026.06）
- Diffusion LLM: 3B/8B/14B，联合 AR + diffusion 训练
- 自推测解码达 6.4× 加速
- **链接**：HuggingFace

---

## 11. Microsoft (Phi)

### Phi-4 技术报告（2024.12）
- **英文标题**：Phi-4 Technical Report
- **模型**：14B 参数
- **发布日期**：2024-12
- **创新**：数据质量驱动（合成数据），超越 teacher GPT-4o
- **链接**：https://arxiv.org/abs/2412.08905

### Phi-4-Reasoning（2025.04）
- **英文标题**：Phi-4-Reasoning Technical Report
- **模型**：14B reasoning，+ variant via RL
- **创新**：
  - SFT on "teachable" prompts + o3-mini demonstrations
  - 超越 DeepSeek-R1-Distill-Llama-70B
  - 接近 full DeepSeek-R1
- **链接**：https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/

### Phi-4-Reasoning-Vision-15B（2026.03）
- **英文标题**：Phi-4-reasoning-vision-15B Technical Report
- **模型**：15B，多模态 reasoning
- **创新**：
  - Mid-fusion（SigLIP-2 + Phi-4-Reasoning）
  - 动态分辨率 vision encoder（up to 3600 visual tokens）
  - 混合 reasoning + non-reasoning 数据
  - MIT license
- **链接**：https://arxiv.org/abs/2603.03975

### Phi-4-Mini / Phi-4-Multimodal（2025.06）
- Mini: 3.8B，vocab 200K
- Multimodal: 文本+视觉+语音/音频，LoRA + modality-specific router
- Mixture-of-LoRAs 技术
- **链接**：https://arxiv.org/abs/2503.01743

---

## 12. Amazon (Nova)

### Amazon Nova Family 技术报告（2024.12 / 2025.03）
- **中文标题**：Amazon Nova 模型家族：技术报告和模型卡
- **英文标题**：The Amazon Nova Family of Models: Technical Report and Model Card
- **发布机构**：Amazon AGI
- **模型系列**：Nova Micro / Lite / Pro / Canvas / Reel
- **发布日期**：2024-12-03（arXiv 2025-03）
- **核心参数**：
  - Pro：多模态，300K context
  - Lite：低成本多模态
  - Micro：仅文本，最低延迟
- **链接**：https://arxiv.org/abs/2506.12103

### Amazon Nova Premier（2025.04）
- **英文标题**：Amazon Nova Premier: Technical Report and Model Card
- **发布日期**：2025-04-30
- **核心参数**：1M context，多模态（text, image, video），作为 teacher model
- **链接**：Amazon Science

### Amazon Nova 2（2025.12）
- **英文标题**：Amazon Nova 2: Multimodal Reasoning and Generation Models
- **模型**：Nova 2 Lite / Nova 2 Pro / Nova 2 Omni / Nova 2 Sonic
- **发布日期**：2025-12-02
- **创新**：
  - Extended thinking（low/medium/high）
  - Code interpreter + web grounding + MCP tools
  - 1M context
  - Nova 2 Sonic：speech-to-speech foundation model
- **链接**：https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models

---

## 13. Zhipu AI (GLM)

### GLM-5 技术报告（2026.02）
- **中文标题**：GLM-5：从 Vibe Coding 到 Agentic Engineering
- **英文标题**：GLM-5: From Vibe Coding to Agentic Engineering
- **发布机构**：Zhipu AI & Tsinghua University
- **模型**：744B total / 40B active (MoE)
- **发布日期**：2026-02-12
- **核心参数**：
  - 256 experts，8 active per token（sparsity ~5.9%）
  - 202K context
  - 28.5T tokens 预训练
  - MIT License
- **主要创新**：
  - DeepSeek Sparse Attention (DSA) 集成
  - Asynchronous RL infrastructure ("Slime")
  - 异步 Agent RL 算法
  - 全栈适配国产芯片（华为昇腾、摩尔线程等）
  - Agentic engineering 定位
- **链接**：https://arxiv.org/abs/2602.15763

### GLM-4.5（2025.07）
- 355B total / 32B active (GLM-4.5)；106B / 12B (GLM-4.5-Air)
- 混合推理模型（thinking + non-thinking）
- **链接**：https://arxiv.org/abs/2508.06471

---

## 14. InternLM (Shanghai AI Lab)

### Intern-S1-Pro（2026.02）
- **中文标题**：Intern-S1-Pro：万亿级科学多模态基础模型
- **英文标题**：Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale
- **发布机构**：Shanghai AI Laboratory
- **模型**：1T 参数，MoE 架构
- **发布日期**：2026-02-04
- **核心参数**：
  - 1T total ~22B active（per inference）
  - 8 experts
  - 涵盖 100+ 学科任务（化学、材料、生命科学、地球科学）
- **主要创新**：
  - 首个万亿级科学多模态模型
  - Expert expansion + Grouped Routing
  - XTuner + LMDeploy 训推一体化
  - 4× 前代规模仅 ~20% 效率损失
- **链接**：https://arxiv.org/abs/2603.25040

### InternLM3（2025.01）
- InternLM3-8B-Instruct，仅 4T tokens 训练
- 节省 75%+ 训练成本 vs LLaMA 3.1-8B / Qwen2.5-7B
- Deep thinking + normal response 双模式
- **链接**：InternLM 官方

---

## 15. Moonshot AI (Kimi)

### Kimi K2.5 技术报告（2026.01）
- **中文标题**：Kimi K2.5：视觉 Agentic 智能
- **英文标题**：Kimi K2.5: Visual Agentic Intelligence
- **发布机构**：Moonshot AI
- **模型**：1T total / 32B active (MoE)
- **发布日期**：2026-01-27
- **核心参数**：
  - 384 experts，8 active per token
  - 256K context
  - MLA attention + MoonViT vision encoder (400M)
  - 在 Kimi K2 基础上做 15T tokens 图文 joint pre-training
- **主要创新**：
  - Joint text-vision pre-training
  - Zero-vision SFT + joint text-vision RL
  - Agent Swarm：并行 agent 编排框架（最高 4.5× 延迟降低）
  - 开源 post-trained checkpoint
- **AIME 2025**：96.1%（thinking mode）
- **链接**：https://arxiv.org/abs/2602.02276

### Kimi K2（2025.07）
- 1T / 32B MoE，MLA，128K context，MuonClip optimizer
- 开源，state-of-the-art non-thinking 模型
- **链接**：https://arxiv.org/abs/2507.20534

### Kimi-VL（2025.04）
- 2.8B active (16B total) MoE + 400M MoonViT
- 128K context，native-resolution
- + Thinking 变体（Kimi-VL-Thinking-2506）
- **链接**：https://arxiv.org/abs/2504.07491

---

## 16. ByteDance (Seed / Doubao)

### Seed2.0 系列（2026.02）
- **中文标题**：Seed2.0 系列：面向真实世界复杂性的智能前沿
- **英文标题**：Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity
- **发布机构**：ByteDance Seed Team
- **模型系列**：Seed2.0 Pro / Lite / Mini + Code
- **发布日期**：2026-02-14
- **核心参数**：
  - MoE 架构
  - 多模态（图文/视频/音频）
  - Pro 达金牌级数学竞赛水平
  - Lite：首个全模态理解模型
- **主要创新**：
  - 面向大规模生产部署的系统性优化
  - Agent + Coding 深度优化
  - Streaming Reasoning System (SRS)：3× 训练加速
  - 三层并行架构
- **链接**：https://seed.bytedance.com/zh/seed2

### Seed1.5-VL（2025.05）
- 532M vision encoder + 20B active MoE LLM
- 38/60 公开 benchmarks SOTA
- Agent 任务超越 OpenAI CUA + Claude 3.7
- **链接**：https://arxiv.org/abs/2505.07062

### Seed-Thinking-v1.5（2026.04）
- MoE 200B total / 20B active
- 数学/代码/科学推理特化
- BeyondAIME 全新超难数据集
- **链接**：ByteDance Seed Blog

---

## 17. StepFun (阶跃星辰)

### Step 3 系统技术报告（2025.07）
- **中文标题**：Step-3：大而经济——模型-系统协同设计实现经济高效解码
- **英文标题**：Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding
- **发布机构**：StepFun（阶跃星辰）
- **模型**：321B total / 38B active (MoE)
- **发布日期**：2025-07-25
- **核心参数**：
  - 48 experts，3 active per token
  - MFA (Multi-Matrix Factorization Attention)
  - AFD (Attention-FFN Disaggregation)
  - 65K context
- **主要创新**：
  - Multi-Matrix Factorization Attention (MFA)
  - Attention-FFN Disaggregation (AFD)
  - 在国产芯片上推理效率可达 DeepSeek-R1 的 300%
  - 在 NVIDIA Hopper 相比 DeepSeek-R1 吞吐提升 70%+
  - Apache 2.0 开源
- **链接**：https://arxiv.org/abs/2507.19427

### Step 3.5 Flash（2026.02）
- 196B+1.8B(ViT) / 11B active (MoE)
- ResearchRubrics: 65.27
- 前沿级 Deep Research 能力
- **链接**：https://arxiv.org/abs/2602.10604

### Step-DeepResearch（2025.12）
- **英文标题**：Step-DeepResearch Technical Report
- 32B 模型达 Scale AI ResearchRubrics 61.42
- ADR-Bench 中文深度研究基准
- **链接**：https://arxiv.org/abs/2512.20491

### Step 3.7 Flash（2026.05）
- Agent 生产化，196B+ / 11B active
- 400 tokens/s，原生多模态
- Claude Code / KiloCode 等主流框架深度兼容
- **链接**：https://github.com/stepfun-ai/Step-3.7-Flash

---

## 18. Yi (01.AI)

### Yi-Lightning（2025）
- 01.AI 最新旗舰模型
- 高推理效率，多模态支持
- 暂未发现独立技术报告 arXiv

---

## 19. Baichuan

### Baichuan 系列（2025-2026）
- 百川智能持续迭代中
- 2025 年发布 Baichuan 4 系列
- 暂未发现独立技术报告 arXiv

---

## 20. 其他值得关注的报告

### MiniMax-M2（2025-2026）
- 万亿参数 MoE，强 agentic 能力
- MiniMax 已港交所 IPO

### GPT-OSS（2025）
- OpenAI GPT-OSS 120B / 20B 开源模型
- 开放权重，社区可用

---

## 跨公司趋势总结

### 架构趋势
1. **MoE 全面主流化**：几乎所有公司旗舰模型均采用 MoE 架构（DeepSeek, Meta, Google, Mistral, Qwen, NVIDIA, Zhipu, Moonshot, ByteDance, StepFun）
2. **Hybrid Mamba-Transformer**：NVIDIA Nemotron 3 系列率先大规模验证
3. **Hybrid Attention**：DeepSeek CSA+HCA, MFA, Kimi Linear/KDA, Gated DeltaNet
4. **Sparse Attention 普及**：DSA 被 DeepSeek V3.2/V4 和 GLM-5 采用

### 训练方法
1. **RL for Reasoning**：从 DeepSeek-R1 到 Magistral 到 RLP，RL 成为推理能力关键
2. **数据质量 > 数据规模**：Phi-4, InternLM3 验证
3. **Thinking/Non-thinking 统一**：Qwen3, GLM-4.5/5, Grok 4.1
4. **Asynchronous RL**：GLM-5 Slime 框架

### 上下文长度
- 1M token 成为旗舰标配：DeepSeek-V4, Gemini 2.5, Claude Opus 4.6, Amazon Nova 2, Llama 4 Scout (10M)
- 256K 成为中端标配

### 关键基准
- SWE-bench Verified：主导 coding agent 能力评估
- AIME 2025：主导推理能力评估
- Humanity's Last Exam：区分顶尖模型

---

## 索引

| # | 机构 | 报告标题 | 日期 | 关键词 |
|---|------|----------|------|--------|
| 1 | DeepSeek | DeepSeek-V4 Technical Report | 2026-04 | MoE, Hybrid Attention, 1M ctx, mHC, Muon |
| 2 | DeepSeek | DeepSeek-V3.2 | 2025-12 | DSA, RL, Agentic |
| 3 | DeepSeek | DeepSeek-R1 | 2025-01 | RL, Reasoning, Distillation |
| 4 | OpenAI | GPT-5 System Card | 2025-08 | Unified Router, Thinking |
| 5 | OpenAI | GPT-5.5 Instant | 2026-05 | Safety, High Capability |
| 6 | OpenAI | o3/o4-mini System Card | 2025-04 | Reasoning, Tools |
| 7 | Meta | Llama 4 | 2025-04 | MoE, Native Multimodal, 10M ctx |
| 8 | Google | Gemini 2.5 | 2025-07 | Thinking, MoE, Agent, 1M ctx |
| 9 | Anthropic | Claude Opus 4/Sonnet 4 | 2025-05 | Hybrid Reasoning, ASL-3 |
| 10 | Anthropic | Claude Opus 4.6 | 2026-02 | 1M ctx, Adaptive Thinking |
| 11 | Mistral | Mistral 3 / Large 3 | 2025-12 | MoE, Open, Multilingual |
| 12 | Mistral | Magistral | 2025-06 | Reasoning, Pure RL |
| 13 | Mistral | Small 4 | 2026-03 | Unified, Apache 2.0 |
| 14 | Qwen | Qwen3 | 2025-05 | Thinking/Non-thinking, 119 langs |
| 15 | Qwen | Qwen3.5-Omni | 2026-03 | Omnimodal, Thinker-Talker |
| 16 | xAI | Grok 4 | 2025-08 | HLE 50%+, Tool Use |
| 17 | Apple | AFM Tech Report 2025 | 2025-07 | PT-MoE, On-device |
| 18 | Apple | AFM 3 | 2026-06 | Google+NVIDIA, IFP |
| 19 | NVIDIA | Nemotron 3 Ultra | 2026-04 | Hybrid Mamba-Attn, LatentMoE |
| 20 | NVIDIA | Llama-Nemotron | 2025-05 | NAS, Reasoning, Open |
| 21 | NVIDIA | RLP | 2026-04 | RL as Pretraining |
| 22 | Microsoft | Phi-4-Reasoning-Vision | 2026-03 | Small Multimodal Reasoning |
| 23 | Amazon | Nova 2 | 2025-12 | Extended Thinking, Speech |
| 24 | Zhipu | GLM-5 | 2026-02 | DSA, Asynchronous RL, 国产 |
| 25 | InternLM | Intern-S1-Pro | 2026-02 | 1T, Scientific, MoE |
| 26 | Moonshot | Kimi K2.5 | 2026-01 | Agent Swarm, Vision |
| 27 | ByteDance | Seed2.0 | 2026-02 | Production, MoE, Agent |
| 28 | ByteDance | Seed1.5-VL | 2025-05 | VL MoE, 38/60 SOTA |
| 29 | StepFun | Step 3 | 2025-07 | MFA, AFD, Efficient |
| 30 | StepFun | Step 3.5 Flash | 2026-02 | Deep Research, 11B active |
