---
title: 各大 AI 公司最新技术报告汇总 (第十版) — 2026-06-11
type: synthesis
created: 2026-06-11
updated: 2026-06-11
tags: [tech-report, system-card, llm, survey, ai-companies]
---

# 各大 AI 公司最新技术报告汇总 (第十版) — 2026-06-11

> 截止 2026 年 6 月 11 日，22+ 家机构的 40+ 技术报告/System Card 汇总。
> 重点关注：新架构 (MoE, Mamba, hybrid)、训练方法、Scaling Law、多模态、长上下文、推理模型。

---

## 1. DeepSeek（深度求索）

### DeepSeek V4 Technical Documentation
- **中文标题**: DeepSeek V4 技术文档
- **模型系列**: DeepSeek V4 (V4-Pro, V4-Flash)
- **发布日期**: 2026-04-24
- **核心参数**:
  - V4-Pro: 1.6T 总参数 / 49B 激活 (MoE)
  - V4-Flash: 284B 总参数 / 13B 激活 (MoE)
  - 上下文: 1M tokens
  - 训练数据: 33T tokens
  - 许可证: MIT
- **主要创新**:
  - Hybrid Attention: Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)，长上下文 FLOPs 降至 V3 的 27%，KV cache 降至 10%
  - Manifold-Constrained Hyper-Connections (mHC) 增强信号传播稳定性
  - Muon Optimizer 加速收敛
  - 三种推理模式: Non-think / Think High / Think Max
- **链接**: [PDF](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **中文标题**: DeepSeek-R1: 通过强化学习激励大语言模型的推理能力
- **模型系列**: DeepSeek-R1 / R1-Zero
- **发布日期**: 2025-01
- **核心参数**: 671B total (基于 V3-Base), 37B active
- **主要创新**:
  - 大规模 RL (GRPO) 无需 SFT 即可涌现推理能力 (R1-Zero)
  - 多阶段训练: 冷启动数据 → RL → 拒绝采样 → SFT → 全面 RL
  - 蒸馏 R1 推理能力至 Qwen/Llama 等小模型
- **链接**: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)

### DeepSeek-V3 Technical Report
- **中文标题**: DeepSeek-V3 技术报告
- **发布日期**: 2024-12 (v1), 2025-02 (v2)
- **核心参数**: 671B total, 37B active, FP8 混合精度训练, 2.664M H800 GPU hours ($5.328M)
- **主要创新**: 无辅助损失负载均衡, Multi-Token Prediction (MTP), MLA 注意力
- **链接**: [arXiv:2412.19437](https://arxiv.org/abs/2412.19437)

---

## 2. OpenAI

### OpenAI o1 System Card
- **中文标题**: OpenAI o1 System Card
- **模型系列**: o1-preview / o1-mini
- **发布日期**: 2024-09-12
- **主要创新**:
  - 大规模 RL 训练 chain-of-thought 推理
  - 在生成回复前进行"思考"，可自我修正策略
  - 在 illicit advice, stereotype, jailbreak 等安全基准上 SOTA
- **链接**: [PDF](http://cdn.openai.com/o1-system-card.pdf)

### GPT-4o / GPT-5 系列
- **GPT-4o (ChatGPT-4o)**: 2025年初发布，原生多模态 (text/image/audio)
- **GPT-4.1 (ChatGPT-4.1)**: 2025年中发布，1M context，优化编码和长上下文
- **O3**: 前沿推理模型系列，深度分析推理、完整工具使用
- **GPT-5**: 2025年末逐步推出，包括 GPT-5, GPT-5.2, GPT-5.4, GPT-5.5 (Mini, Pro 多级)

---

## 3. Meta AI (LLaMA)

### Llama 4 Model Card
- **中文标题**: Llama 4 模型卡片
- **模型系列**: Llama 4 Scout / Maverick / Behemoth
- **发布日期**: 2025-04-05
- **核心参数**:
  - Scout: 109B total, 17B active, 16 experts, **10M context**
  - Maverick: 400B total, 17B active, 128 experts, 1M context
  - Behemoth: ~2T total, ~288B active (训练中，用作教师模型)
- **主要创新**:
  - 原生多模态 (Early Fusion)，预训练即融合文本和视觉 token
  - MoE 架构 (Scout 16专家, Maverick 128专家)
  - 10M 上下文窗口 (Scout) — 公开模型最长
  - 200 语言支持
- **链接**: [llama.com](https://www.llama.com/models/llama-4/)

### The Llama 3 Herd of Models
- **中文标题**: Llama 3 模型系列
- **发布日期**: 2024-07-23
- **核心参数**: 8B / 70B / 405B (dense), 128K context, 15T+ tokens
- **链接**: [arXiv:2407.21783](https://arxiv.org/abs/2407.21783)

---

## 4. Google DeepMind (Gemini)

### Gemini 2.5 Technical Report
- **中文标题**: Gemini 2.5 技术报告
- **模型系列**: Gemini 2.5 Pro / 2.5 Flash / 2.0 Flash
- **发布日期**: 2025-07
- **核心参数**:
  - Sparse MoE Transformer, 1M+ token context
  - 原生多模态 (text, image, audio, video)
  - "Thinking" mode for complex reasoning
- **主要创新**:
  - MoE 架构实现高效率缩放
  - 百万 token 上下文
  - 涌现 agentic 行为 (自动玩 Pokémon)
- **链接**: [arXiv:2507.06261](https://arxiv.org/abs/2507.06261)

### Gemini 3.1 Pro / 3.5 Flash (2026)
- **Gemini 3.1 Pro**: Sparse MoE Transformer，2026年旗舰推理基础，作为 Veo 3.1/Lyria 3/Genie 3 等模型的推理骨干
- **Gemini 3.5 Flash**: 2026年5月发布，编码和推理质量接近 Pro，速度更快

### Gemma 4
- 2026年发布，Google 最智能的开源模型，最大化 intelligence-per-parameter

---

## 5. Anthropic (Claude)

### Claude Opus 4.6 System Card
- **中文标题**: Claude Opus 4.6 System Card
- **模型系列**: Claude Opus 4.6
- **发布日期**: 2026-02
- **核心参数**: 1M context, 128K max output, $5/M input, $25/M output, ASL-3
- **主要创新**:
  - SOTA on software engineering, agentic tasks, long context reasoning
  - Extended/Adaptive thinking modes
  - 奖励黑客评估、sabotage capability、model welfare 评估
- **链接**: [PDF](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf)

### Claude Opus 4.7 System Card
- **中文标题**: Claude Opus 4.7 System Card
- **发布日期**: 2026-04-16
- **主要变化**: SWE-bench Verified 80.8%→87.6%, SWE-bench Pro 53.4%→64.3%
- **注意**: 长上下文多针检索有退化 (256K: 91.9%→59.2%, 1M: 78.3%→32.2%)
- **链接**: [System Card](https://anthropic.com/claude-opus-4-7-system-card)

### Claude Opus 4.8 System Card
- **发布日期**: 2026-05

### Claude 4 (Opus 4 & Sonnet 4) System Card
- **发布日期**: 2025-05
- **关键**: 首个 hybrid reasoning LLM，支持 Computer Use，ASL-3 (Opus 4)
- **链接**: [PDF](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf)

### Claude Mythos Preview System Card
- **发布日期**: 2026-04
- Anthropic 最佳对齐内部模型，244页 System Card

---

## 6. Mistral AI

### Mistral Large 3
- **中文标题**: Mistral Large 3
- **模型系列**: Mistral Large 3 (675B MoE)
- **发布日期**: 2025-12
- **核心参数**: 675B total, ~41B active, 256K context, Apache 2.0
- **主要创新**:
  - Sparse MoE 架构
  - 多模态 (text+image)
  - 优化 NVFP4 量化 / Blackwell Attention kernels
  - 单 8-GPU 节点可运行
- **链接**: [mistral.ai](https://mistral.ai)

### Mistral Small 4
- **发布日期**: 2026-03-16
- **核心参数**: 119B total, ~6B active, 128 experts (4 active/token), 256K context, Apache 2.0
- **主要创新**: 统一推理/多模态/编码于单模型，可配置 reasoning_effort
- **亮点**: $0.15/M input (比 GPT-5.4 Mini 便宜 5x)

### Ministral 3 系列
- **模型**: 3B / 8B / 14B dense models
- 边缘/本地部署优化，Apache 2.0

### Codestral 25.01
- **发布日期**: 2025-01
- **核心参数**: 22B, 256K context, 80+ 编程语言, HumanEval 86.6%

---

## 7. Qwen (Alibaba / 阿里云)

### Qwen3.5 系列
- **中文标题**: Qwen3.5 模型系列
- **发布日期**: 2026-02-16
- **模型**: Qwen3.5-Flash, Qwen3.5-27B (Dense), Qwen3.5-35B-A3B (MoE), Qwen3.5-122B-A10B (MoE)
- **核心参数**: 256K context (可扩展至 1M+), 支持 Thinking/Flash 双模式
- **主要创新**:
  - Early-fusion 原生多模态 (统一 tokenization)
  - Gated Delta Networks + Sparse MoE
  - 可扩展 RL (百万 agent 环境)
- **链接**: [GitHub](https://github.com/QwenLM/Qwen3.6)

### Qwen3.5 Omni
- **发布日期**: 2026-03-30
- Thinker-Talker 架构 + Hybrid-Attention MoE
- 原生处理 text/image/audio/video

### Qwen3.7 Max
- **发布日期**: 2026-05
- 1M context, Qwen 家族最强推理模型
- Code Arena #4 (与 Claude Opus 4.6 持平)

### Qwen3.6
- 最新版本，优化 agentic coding 和 thinking preservation

---

## 8. Microsoft (Phi / MAI)

### Phi-4 Technical Report
- **中文标题**: Phi-4 技术报告
- **模型系列**: Phi-4 (14B), Phi-4-mini (3.8B), Phi-4-multimodal (5.6B)
- **发布日期**: 2024-12
- **核心参数**: 14B (text), 5.6B (multimodal), 3.8B (mini)
- **主要创新**:
  - 高质量合成数据 + 精选 web data
  - 多模态: mixture-of-LoRAs 统一 speech/vision/text
  - 针对推理优化的 Phi-4-reasoning 系列 (用 DeepSeek R1 + o3-mini 蒸馏)
- **链接**: [arXiv:2412.08905](https://arxiv.org/abs/2412.08905), [Tech Report PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf)

### MAI-Thinking-1 / MAI-Code-1-Flash
- **发布日期**: 2026-06-03 (Build 2026)
- 微软首个自研推理模型，训练**未使用 OpenAI 数据**

---

## 9. Apple

### Apple Intelligence Foundation Language Models: Tech Report 2025
- **中文标题**: Apple Intelligence 基础语言模型技术报告 2025
- **模型系列**: On-Device (~3B) + Server Model (PT-MoE)
- **发布日期**: 2025-07-17
- **核心参数**:
  - On-device: ~3B, KV-cache sharing, 2-bit QAT, 5:3 depth ratio
  - Server: Parallel-Track MoE (PT-MoE)，track parallelism + sparse computation + interleaved global-local attention
- **主要创新**:
  - PT-MoE 架构 (多个小型 transformer track 并行 + MoE)
  - 2-bit 量化感知训练 (QAT)
  - Private Cloud Compute 隐私保护
  - Swift Foundation Models framework (guided generation, tool calling, LoRA)
- **链接**: [arXiv:2507.13575](https://arxiv.org/abs/2507.13575), [Apple ML Research](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates)

---

## 10. NVIDIA

### Nemotron 3 Technical Report
- **中文标题**: NVIDIA Nemotron 3: Efficient and Open Intelligence
- **模型系列**: Nemotron 3 (Nano / Super / Ultra)
- **发布日期**: 2025-12-25 (report), Ultra 正式发布 2026-06-04
- **核心参数**:
  - Ultra: 550B total, ~55B active, **Hybrid Mamba-Transformer MoE**, 1M context
  - Super: 120B total, ~12B active
  - Nano: 30B total, ~3B active (可运行在 Jetson)
- **主要创新**:
  - **Hybrid Mamba-Transformer + Latent MoE** — Mamba 层亚二次缩放 + Attention 层精确召回
  - NVFP4 量化 (Blackwell 原生支持)，混合 NVFP4 routed experts + FP8 shared experts
  - Multi-teacher On-Policy Distillation (MOPD) — 10+ 专家教师蒸馏至单一学生
  - 多环境 RL 后训练 (agentic coding, tool use, math)
  - MTP (Multi-Token Prediction) 加速生成
  - 完全开源 (OpenMDW-1.1): 权重、数据、训练配方
- **链接**: [arXiv:2512.20856](https://arxiv.org/pdf/2512.20856), [NVIDIA Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)

---

## 11. xAI (Grok)

### Grok 4.20 System Card
- **中文标题**: Grok 4.20 System Card
- **模型系列**: Grok 4.20 (SA 单 agent / MA 多 agent)
- **发布日期**: 2026-04-07
- **核心参数**: 2M token context, 多 agent 协作 (4 standard / 16 Heavy)
- **主要创新**:
  - 单 agent / 多 agent 双模式部署
  - FAIF (Frontier AI Framework) 评估体系
  - 低幻觉率
- **链接**: [PDF](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf)

### Grok 4.1
- **发布日期**: 2025-11-17
- 大规模 RL 优化风格/个性/有用性, 幻觉率从 12.09% 降至 4.22%

### Grok 4.3
- 2026年最新，1M context, $1.25/M input

### Grok 5
- 训练中，预计 6T 参数

---

## 12. Amazon (Nova)

### The Amazon Nova Family of Models: Technical Report and Model Card
- **中文标题**: Amazon Nova 模型家族技术报告和模型卡片
- **模型系列**: Nova Micro / Lite / Pro / Premier / Canvas / Reel
- **发布日期**: 2025-03-17
- **核心参数**:
  - Micro: text-only, 最低延迟, 210 tok/s
  - Lite: 低价多模态 (image/video/text)
  - Pro: 多模态, 平衡准确性/速度/成本
  - Premier: 最强大, 用作教师模型蒸馏
- **主要创新**: Transformer + latent diffusion (Canvas/Reel), 200+ 语言, DPO/PPO RLHF
- **链接**: [arXiv:2506.12103](https://arxiv.org/abs/2506.12103)

### Amazon Nova 2 (2025-12)
- Nova 2 Lite / Nova 2 Pro (Preview): 推理能力, 1M context, adjustable thinking budget
- Nova 2 Sonic (speech-to-speech), Nova 2 Omni (多模态+图像生成)

---

## 13. Zhipu AI / Z.ai (智谱)

### GLM-5 / GLM-5.1
- **中文标题**: GLM-5 / GLM-5.1
- **模型系列**: GLM-5, GLM-5.1, GLM-5V-Turbo
- **发布日期**: GLM-5: 2026-02-11, GLM-5.1: 2026-04-08
- **核心参数**:
  - GLM-5: 744B total, 40B active, 128K context, 28.5T tokens, MIT
  - GLM-5.1: ~754B total, ~42B active
  - GLM-5V-Turbo: 多模态, 200K context
- **主要创新**:
  - 开源 MoE, MIT 许可证
  - GLM-5.1 可持续自主编码 8 小时
  - SWE-bench Pro 58.4 (超越 GPT-5.4 的 57.7)
  - 开源编码 Agent SOTA
- **链接**: [z.ai](https://www.zhipuai.cn/)

---

## 14. Moonshot AI (Kimi)

### Kimi K2 Technical Report
- **中文标题**: Kimi K2 技术报告
- **模型系列**: Kimi K2
- **发布日期**: 2026-01
- **核心参数**: 1.04T total, 32B active, 384 experts (8 active/token), 15.5T tokens
- **主要创新**:
  - **MuonClip optimizer**: Muon + QK-Clip (注意力 logit 裁剪), 首个万亿 MoE 规模 Muon 稳定训练
  - 合成 agentic 数据管线: ~20K tools, 数千 agents, 多轮评判轨迹
  - 自评判 rubrics reward (RLVR 扩展到主观任务)
  - Ultra-sparse MoE (sparsity 48) + MLA
- **链接**: [GitHub](https://github.com/MoonshotAI/Kimi-K2/blob/main/tech_report.pdf)

### Kimi K2.5
- **发布日期**: 2026-01
- 多模态升级 (400M MoonViT 视觉编码器), 支持视频输入
- Agent Swarm: 最多 100 子 agent

### Kimi K2.6
- **发布日期**: 2026-04-20
- 最新旗舰, 原生多模态, 超强编码+Agent

---

## 15. ByteDance Seed / Doubao (字节跳动)

### Seed1.8 Model Card
- **中文标题**: ByteDance Seed1.8 模型卡片
- **模型系列**: Seed1.8
- **发布日期**: 2025-12
- **主要创新**:
  - 四种 thinking mode: no_think / low / medium / high
  - 支持 agentic workflows (search, coding, tool use, GUI)
  - 多模态 (text/image/video) + 长上下文
- **链接**: [PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/research/Seed-1.8-Modelcard.pdf)

### Doubao Seed 2.0 系列
- **发布日期**: 2026-04
- **四层型号**:
  - Doubao Pro ($0.43/$2.15): agent-first, 86% multi-step, 128K context
  - Doubao Code ($0.57/$2.85): 88% HumanEval, Python/JS 与 Sonnet 只差 1-2 点
  - Doubao Lite ($0.14/$0.71): 高吞吐
  - Doubao Mini ($0.07/$0.28): 边缘部署

---

## 16. StepFun (阶跃星辰)

### Step 3.5 Flash
- **中文标题**: Step 3.5 Flash
- **模型系列**: Step 3.5 Flash
- **发布日期**: 2026-02-09
- **核心参数**: 196B total, ~11B active (MoE), 256K context, 350 tok/s
- **主要创新**:
  - 3:1 滑动窗口 + 全局注意力混合 (SWA + Full Attention)
  - MTP-3 多 token 预测，效率翻倍
  - AIME 97.3 / IMO 85.4 / HMMT 96.2 (国内开源第一)
  - SWE-bench 74.4
- **链接**: [GitHub](https://github.com/stepfun-ai/Step3/blob/main/Step3-Sys-Tech-Report.pdf)

### StepAudio 2.5 Realtime
- **发布日期**: 2026-05-22
- 统一 audio-in/audio-out, ASR/TTS/实时对话三合一
- Persona-specific RLHF
- MMAU SOTA
- **链接**: [arXiv:2605.23463](https://arxiv.org/abs/2605.23463)

### STEP3-VL-10B
- 10B 参数多模态模型，统一预训练 1.2T tokens
- 媲美 Gemini 2.5 Pro，10-20x 更少参数

---

## 17. InternLM (上海 AI Lab)

### InternLM2 Technical Report
- **中文标题**: InternLM2 技术报告
- **模型系列**: InternLM2 (7B / 20B / 104B)
- **发布日期**: 2024-03-26
- **核心参数**: 104B total, 1.6T tokens, 32K context (扩展至 200K+)
- **主要创新**: COOL RLHF (Conditional Online RLHF), Agent-FLAN, Code Interpreter
- **链接**: [arXiv:2403.17297](https://arxiv.org/abs/2403.17297)

### InternLM3-8B
- 2025-2026, 继续迭代

### Intern-S1 / Intern-S2 (科学大模型)
- S1: 万亿参数 MoE (512 experts, 1T total, 22B active)
- S2-Preview: 35B 参数，科学性能比肩万亿参数模型

---

## 18. Yi (01.AI / 零一万物)

### Yi-Lightning / Yi 系列
- **模型系列**: Yi-1.5 (6B / 9B / 34B)
- **发布日期**: 2024-10 (Yi-Lightning)
- 01.AI 由李开复创立，专注双语 (中英) 开源模型
- Yi-34B-Chat 曾在 AlpacaEval 排名第二 (仅次于 GPT-4 Turbo)

---

## 19. Baichuan (百川智能)

### Baichuan 系列
- **模型系列**: Baichuan2 (7B / 13B / 192K), Baichuan-M3 (医疗)
- 由前搜狗 CEO 王小川创立
- 专注医疗领域: Baichuan-M3 医疗大模型，极低幻觉率
- 开源 Baichuan2 全过程训练切片 (200B→2640B 中间权重)

---

## 20. 其他值得关注的报告

### Google Gemma 4
- 2026年发布
- Google 最强开源模型，最大化 intelligence-per-parameter

### DeepSeek V3.1 / V3.2
- V3.1: 2025-08, 840B tokens continued pretraining, 128K context, agent 优化
- V3.2: 迭代版本

### Microsoft Phi-4-reasoning / Phi-4-reasoning-plus
- 2025-04-30, 用 DeepSeek R1 + o3-mini 蒸馏
- Phi-4-reasoning (14B): 数学/科学/编码
- Phi-4-reasoning-plus: 接近 DeepSeek R1 性能

---

## 综合趋势分析

### 架构趋势
| 架构 | 代表模型 | 优势 |
|------|---------|------|
| MoE (Sparse) | DeepSeek V4, GLM-5, Kimi K2, Qwen3.5 | 总参数大、激活参数小、高效 |
| Hybrid Mamba-Transformer | Nemotron 3 Ultra | 亚二次缩放 + 精确召回 |
| Hybrid Attention (CSA+HCA) | DeepSeek V4 | 长上下文效率革命 |
| PT-MoE (Track Parallel) | Apple Server AFM | 多 track 并行 + MoE |
| Early Fusion Multimodal | Llama 4, Qwen3.5-Omni | 原生多模态，无信息损失 |

### 关键主题
1. **推理能力 (Reasoning)**: 几乎所有旗舰模型都支持 configurable thinking/reasoning mode
2. **长上下文**: DeepSeek V4 / Llama 4 Scout (10M) / Gemini (1M+) / Claude (1M)
3. **Agentic AI**: SWE-bench 成为标准评测，模型专为 agent 工作流优化 (tool use, multi-step)
4. **开源与许可证**: MIT (DeepSeek V4, GLM-5), Apache 2.0 (Mistral, Qwen), OpenMDW (NVIDIA)
5. **Muon Optimizer**: 从 DeepSeek V4 (2026-04) 到 Kimi K2 (2026-01)，超越 AdamW 的优化器
