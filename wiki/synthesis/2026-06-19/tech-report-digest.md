---
title: 各大 AI 公司最新技术报告汇总 — 2026-06-19 全面更新版
type: synthesis
created: 2026-06-19
updated: 2026-06-19
sources: [web-search]
tags: [tech-report, system-card, survey, llm, reasoning, multimodal, moe, scaling-law]
---

# 各大 AI 公司最新技术报告汇总

> **范围**: 20+ 家机构, 40+ 份技术报告 / System Card
> **日期**: 2026-06-19（基于公开 arXiv / 官方发布的最新版本）
> **重点**: 大模型新架构 · 训练方法 · Scaling Law · 多模态 · 长上下文 · 推理模型

---

## 一、美国 / 西方 AI 公司

### 1. OpenAI — GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5 (gpt-5-main, gpt-5-thinking, gpt-5-main-mini, gpt-5-thinking-mini, gpt-5-thinking-nano, gpt-5-thinking-pro) |
| **发布日期** | 2025-08-13（2026-04-24 更新 Chain of Thought 评估章节） |
| **核心参数** | 未公开参数量；统一系统含实时路由器；支持并行 test-time compute |
| **上下文长度** | 未明确公开（GPT-5.2 后续版本达 200K+） |
| **主要创新** | 统一 fast/slow 双模型 + 实时路由器自动切换；safe-completions 安全训练；显著降低幻觉率 |
| **论文链接** | https://arxiv.org/abs/2601.03267 |

### 2. Meta AI — Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 家族：架构、训练、评估与部署 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout (17Bx16E), Llama 4 Maverick (17Bx128E), Behemoth (teacher) |
| **发布日期** | 2025-04-05 |
| **核心参数** | Scout: 109B total / 17B active; Maverick: 400B total / 17B active |
| **训练数据** | Scout ~40T tokens, Maverick ~22T tokens |
| **上下文长度** | Scout: 10M tokens; Maverick: 1M tokens |
| **主要创新** | MoE 架构；early-fusion 原生多模态；iRoPE 长上下文扩展；Scout 单 H100 可部署 |
| **论文链接** | https://arxiv.org/abs/2601.11659（已撤回，详见官方 Model Card） |

### 3. Google DeepMind — Gemini 3 / 3.1 Pro

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3 技术报告 / Gemini 3.1 Pro 模型卡 |
| **英文标题** | Gemini 3 Technical Report / Gemini 3.1 Pro Model Card |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3 Pro, Gemini 3.1 Pro (Preview) |
| **发布日期** | Gemini 3 Pro: 2025-11; Gemini 3.1 Pro: 2026-02-19 (Preview) |
| **核心参数** | 未公开；估计 MoE ~1.5T total / ~180B active |
| **上下文长度** | 2,000,000 tokens（行业最长） |
| **主要创新** | Sparse MoE 架构；Deep Think 增强推理模式；extended-locality attention 支持 2M 上下文；原生多模态输入（text/audio/image/video/code） |
| **论文链接** | https://deepmind.google/models/gemini/pro/ (Model Card) |

### 4. Anthropic — Claude 4 系列 System Cards

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4 & Sonnet 4 系统卡 / Opus 4.6 / Opus 4.8 / Fable 5 & Mythos 5 |
| **英文标题** | System Card: Claude Opus 4 & Sonnet 4 / Opus 4.6 / Opus 4.8 / Fable 5 & Mythos 5 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Sonnet 4, Opus 4 (May 2025); Opus 4.6 (Feb 2026); Opus 4.8 (May 2026); Fable 5 & Mythos 5 (Jun 2026) |
| **核心参数** | 未公开参数量（推测数万亿参数 MoE） |
| **主要创新** | Hybrid reasoning（hybrid reasoning LLM）；首次 ASL-3 部署（Opus 4+）；深度 alignment assessment 含 model welfare；activation oracles / attribution graphs / sparse autoencoder 可解释性 |
| **论文链接** | https://www.anthropic.com/system-cards |

### 5. Mistral AI — Ministral 3 / Magistral

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3 / Magistral：Mistral 推理模型 |
| **英文标题** | Ministral 3 / Magistral: Mistral's First Reasoning Model |
| **发布机构** | Mistral AI |
| **模型系列** | Ministral 3 (3B/8B/14B), Magistral Small (24B), Magistral Medium |
| **发布日期** | Ministral 3: 2026-01; Magistral: 2025-06 |
| **核心参数** | Dense 架构（Ministral 3 系列）；MoE（Magistral） |
| **上下文长度** | 256K (Ministral 3), 128K (reasoning variants) |
| **主要创新** | Cascade Distillation：迭代剪枝+蒸馏产生小模型；仅需 1-3T tokens 训练即可达到 SOTA；纯 RL 训练推理模型（不依赖蒸馏）；Apache 2.0 开源 |
| **论文链接** | Ministral 3: https://arxiv.org/pdf/2601.08584; Magistral: https://arxiv.org/pdf/2506.10910 |

### 6. Microsoft — Phi-4 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 / Phi-4-reasoning / Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4 Technical Report / Phi-4-reasoning / Phi-4-reasoning-vision-15B |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 (14B), Phi-4-reasoning (14B), Phi-4-reasoning-plus, Phi-4-reasoning-vision-15B |
| **发布日期** | Phi-4: 2024-12; Phi-4-reasoning: 2025-04; Phi-4-reasoning-vision: 2026-03 |
| **核心参数** | 14B–15B 参数（Dense Transformer） |
| **主要创新** | Data quality > data scale：合成数据远超教师模型 GPT-4o；多模态推理（vision）；SFT + outcome-based RL 提升推理链；reasoning/non-reasoning 混合模式 token |
| **论文链接** | Phi-4: https://arxiv.org/abs/2412.08905; Phi-4-reasoning-vision: https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

### 7. Apple — Apple Intelligence Foundation Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型技术报告 2025 |
| **英文标题** | Apple Intelligence Foundation Language Models Tech Report 2025 |
| **发布机构** | Apple |
| **模型系列** | On-device ~3B, Server PT-MoE |
| **发布日期** | 2025-07-17 |
| **核心参数** | On-device: ~3B; Server: Parallel-Track MoE (PT-MoE) |
| **主要创新** | KV-cache sharing + 2-bit QAT 用于 on-device；PT-MoE：track parallelism + MoE sparse + interleaved global-local attention；Private Cloud Compute |
| **论文链接** | https://arxiv.org/abs/2507.13575 |

### 8. NVIDIA — Nemotron 3 系列 & Llama-Nemotron

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 / Llama-Nemotron 技术报告 |
| **英文标题** | Nemotron 3: Open, Efficient MoE Hybrid Mamba-Transformer / Llama-Nemotron: Efficient Reasoning Models |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Nano (30B-A3B), Super (120B-A12B), Ultra (550B-A55B); Llama-Nemotron Nano (8B), Super (49B), Ultra (253B); Nemotron Nano 2 (9B) |
| **发布日期** | Nemotron 3: 2025–2026; Llama-Nemotron: 2025-05; Nemotron Nano 2: 2026 |
| **核心参数** | MoE + Hybrid Mamba-Transformer；NVFP4 预训练；LatentMoE；Multi-Token Prediction (MTP) |
| **上下文长度** | 128K–1M tokens |
| **主要创新** | **Hybrid Mamba-Attention**：以 Mamba-2 替换大部分 self-attention 层，大幅提升推理吞吐；LatentMoE 提升 accuracy/parameter 比；NVFP4 低精度预训练；动态 reasoning toggle（chat/reasoning 模式切换）；最高 5.9× 推理吞吐提升 |
| **论文链接** | Nemotron 3 Ultra: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf; Llama-Nemotron: https://arxiv.org/abs/2505.00949; Nemotron 3 Nano: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf |

### 9. xAI — Grok 4 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 / Grok 4 Fast / Grok 4.1 模型卡 |
| **英文标题** | Grok 4 Model Card / Grok 4 Fast Model Card / Grok 4.1 Model Card |
| **发布机构** | xAI |
| **模型系列** | Grok 4, Grok 4 Heavy, Grok 4 Fast, Grok 4.1 (Thinking/Non-Thinking) |
| **发布日期** | Grok 4: 2025-07-09; Grok 4 Fast: 2025-09-19; Grok 4.1: 2025-11-17 |
| **核心参数** | 未公开（MoE 架构）；200K H100 Colossus 集群训练 |
| **上下文长度** | 256K tokens |
| **主要创新** | 首个 HLE 50%+ 模型（Grok 4 Heavy）；native tool use（code interpreter + web search）；parallel test-time compute；RL + verifiable rewards + model grading |
| **论文链接** | Grok 4: https://data.x.ai/2025-08-20-grok-4-model-card.pdf |

### 10. Amazon — Amazon Nova 家族

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族技术报告与模型卡 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Micro (text-only), Nova Lite (multimodal), Nova Pro (multimodal), Nova Premier, Nova Canvas (image gen), Nova Reel (video gen) |
| **发布日期** | 2024-12-03（Nova Premier: 2025-04-30 增补） |
| **核心参数** | 未公开；Pro/Lite 为多模态（text/image/video → text） |
| **上下文长度** | Premier: 1M tokens |
| **主要创新** | 全系列模型覆盖文本/多模态/图像生成/视频生成；Nova Premier 作为 teacher model 支持蒸馏；strong agentic & long-context 表现 |
| **论文链接** | https://arxiv.org/abs/2506.12103 |

---

## 二、中国 AI 公司

### 11. DeepSeek — DeepSeek-V4

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek |
| **模型系列** | V4-Pro (1.6T total / 49B active), V4-Flash (284B total / 13B active) |
| **发布日期** | 2026-04-24 |
| **核心参数** | MoE；32T+ tokens 预训练 |
| **上下文长度** | 1M tokens（所有官方服务默认） |
| **主要创新** | **Hybrid Attention (CSA + HCA)**：Compressed Sparse Attention + Heavily Compressed Attention；**Manifold-Constrained Hyper-Connections (mHC)** 改进残差连接；**Muon Optimizer** 加速收敛；1M 上下文中仅需 V3.2 的 27% FLOPs 和 10% KV cache；MIT 开源 |
| **论文链接** | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf |

### 12. Qwen（阿里巴巴）— Qwen3 / 3.5 / 3.6 / 4 Coder

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 / Qwen3.5 / Qwen3.5-Omni / Qwen3.6 / Qwen 4 Coder 技术报告 |
| **英文标题** | Qwen3 / Qwen3.5 / Qwen3.5-Omni / Qwen3.6 / Qwen 4 Coder Technical Report |
| **发布机构** | Alibaba Qwen Team |
| **模型系列** | Qwen3 (0.6B–235B-A22B), Qwen3.5 (397B-A17B), Qwen3.5-Omni (Plus/Flash), Qwen3.6 (27B, 35B-A3B), Qwen 4 Coder (32B-A3B) |
| **发布日期** | Qwen3: 2025-05-14; Qwen3.5: 2026-02; Qwen3.5-Omni: 2026-04; Qwen3.6: 2026-04; Qwen 4 Coder: 2026-06-02 |
| **核心参数** | Dense + MoE 双线；最大 397B-A17B MoE |
| **上下文长度** | 128K–256K tokens |
| **主要创新** | **Think/Non-Think 统一框架** + thinking budget 机制；119 语言支持；Omni 原生多模态（text/image/audio/audio-visual）；Hybrid Attention MoE；Qwen 4 Coder SWE-Verified 82%（开源最强） |
| **论文链接** | Qwen3: https://arxiv.org/abs/2505.09388; Qwen3.5-Omni: https://arxiv.org/abs/2604.15804 |

### 13. Zhipu AI — GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-5 (744B total / 40B active) |
| **发布日期** | 2026-02-12 |
| **核心参数** | MoE；28.5T tokens 预训练 |
| **上下文长度** | 200K tokens |
| **主要创新** | **DSA (DeepSeek Sparse Attention)** 显著降低部署成本；**异步 RL 基础设施 "slime"** 解耦生成与训练；三阶段 RL pipeline（Reasoning RL → Agentic RL → General RL）；On-Policy Cross-Stage Distillation 防止灾难性遗忘；全栈国产芯片适配（华为昇腾/摩尔线程等） |
| **论文链接** | https://arxiv.org/abs/2602.15763 |

### 14. Moonshot AI — Kimi K2 / K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放智能体智能 / Kimi K2.5 原生多模态智能体 |
| **英文标题** | Kimi K2: Open Agentic Intelligence / Kimi K2.5: Native Multimodal Agentic Model |
| **发布机构** | Moonshot AI |
| **模型系列** | Kimi K2 (1T total / 32B active), Kimi K2.5 (1T total / 32B active) |
| **发布日期** | K2: 2025-07-28; K2.5: 2026-01-30 |
| **核心参数** | MoE；384 专家 + 1 shared expert；MLA attention |
| **上下文长度** | K2: 128K; K2.5: 256K |
| **主要创新** | **MuonClip Optimizer**（QK-Clip 训练稳定性改进）；大规模 Agentic 数据合成管线；联合 RL（real + synthetic environments）；K2.5 原生多模态（MoonViT 视觉编码器）；非 thinking 模式下 SOTA agentic 性能 |
| **论文链接** | K2: https://arxiv.org/abs/2507.20534; K2.5: https://github.com/MoonshotAI/Kimi-K2.5 |

### 15. ByteDance — Seed 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed1.8 / Seed-Thinking-v1.5 / Seed2.0 / Seed-Coder 技术报告/模型卡 |
| **英文标题** | Seed1.8 / Seed-Thinking-v1.5 / Seed2.0 / Seed-Coder Technical Report |
| **发布机构** | ByteDance Seed Team |
| **模型系列** | Seed1.8, Seed-Thinking-v1.5 (200B total / 20B active), Seed2.0 (Pro/Lite/Mini/Code), Seed-Coder (8B) |
| **发布日期** | Seed-Thinking-v1.5: 2025-04-14; Seed-Coder: 2025-05; Seed1.8: 2025-12; Seed2.0: 2026-02-14 |
| **核心参数** | MoE 架构；Seed-Thinking-v1.5: 200B total / 20B active |
| **主要创新** | 四种 thinking mode（no_think/low/medium/high）；Streaming Reasoning System (SRS) 3× 训练加速；三重数据清洗管线 + BeyondAIME 超难数学基准；KARP 算法优化 GPU 利用率 |
| **论文链接** | Seed1.8: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/research/Seed-1.8-Modelcard.pdf; Seed-Coder: https://arxiv.org/abs/2506.03524 |

### 16. StepFun（阶跃星辰）— Step3 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Step3：大而经济的多模态推理模型 / Step 3.5 Flash |
| **英文标题** | Step3: Cost-Effective Multimodal Intelligence / Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step3 (321B total / 38B active), Step 3.5 Flash (196B total / 11B active), Step3-VL-10B |
| **发布日期** | Step3: 2025-07; Step 3.5 Flash: 2026-02; Step3-VL-10B: 2026-01 |
| **核心参数** | MoE；48 experts |
| **上下文长度** | 65K (Step3)；Step 3.5 Flash 支持 MTP-3 |
| **主要创新** | **Multi-Matrix Factorization Attention (MFA)** + **Attention-FFN Disaggregation (AFD)** 协同设计降低解码成本；3:1 Sliding Window / Full Attention 混合；大规模 off-policy RL 框架（verifiable signals + preference feedback）；170 tok/s 推理速度（Hopper GPU） |
| **论文链接** | Step3: https://arxiv.org/abs/2507.19427; Step 3.5 Flash: https://arxiv.org/abs/2602.10604 |

### 17. InternLM（上海 AI 实验室）— InternLM2 / InternLM3

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM2 / InternLM3 技术报告 |
| **英文标题** | InternLM2 / InternLM3 Technical Report |
| **发布机构** | 上海人工智能实验室 (Shanghai AI Lab) |
| **模型系列** | InternLM2 (7B–104B), InternLM3 (8B) |
| **发布日期** | InternLM2: 2024-03; InternLM3: 2025-01-15 |
| **核心参数** | InternLM3-8B 仅用 4T tokens 训练；COOL RLHF 策略 |
| **主要创新** | **数据效率突破**：4T tokens 达到其他模型 18T tokens 性能（IQPT 提升）；"通用-专长融合"架构统一 deep thinking + 常规对话；训练成本降低 75%+ |
| **论文链接** | InternLM2: https://arxiv.org/abs/2403.17297; InternLM3: https://openmmlab.medium.com/internlm3-open-source-achieving-high-performance-models-with-4t-data |

### 18. 01.AI — Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI（零一万物） |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024-12-02 |
| **核心参数** | MoE 架构（enhanced expert segmentation + routing） |
| **主要创新** | 优化 KV-caching 降低部署成本；RAISE 安全框架（四组件）；多阶段训练 + synthetic data + reward modeling |
| **论文链接** | https://arxiv.org/abs/2412.01253 |

### 19. Baichuan（百川智能）— Baichuan-M3

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M3：建模临床问诊实现可靠医疗决策 |
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | Baichuan Intelligence（百川智能） |
| **模型系列** | Baichuan-M3 (235B), Baichuan-Omni-1.5 |
| **发布日期** | M3: 2026-02; Omni-1.5: 2025-01 |
| **核心参数** | MoE 架构 |
| **主要创新** | **SPAR 算法**（Step-Penalized Advantage with Relative baseline）处理医疗长链推理；三阶段多专家融合训练（领域 RL → 离线蒸馏 → MOPD 在线优化）；HealthBench 超越 GPT-5.2；Gated Eagle3 投机解码 96% 加速 |
| **论文链接** | M3: https://arxiv.org/abs/2602.06570; Omni-1.5: https://arxiv.org/abs/2501.15368 |

---

## 三、综合趋势分析

### 架构趋势

| 方向 | 代表模型 | 占比趋势 |
|------|----------|----------|
| **MoE (Mixture-of-Experts)** | 几乎所有旗舰模型 | 绝对主流 |
| **Hybrid Mamba-Transformer** | Nemotron 3 系列, Nemotron Nano 2 | ⬆ 新兴趋势 |
| **Hybrid Attention (CSA/HCA/DSA)** | DeepSeek V4, GLM-5 | ⬆ 长上下文效率 |
| **Multi-Head Latent Attention (MLA)** | Kimi K2/K2.5, DeepSeek V3 | ⬆ KV cache 优化 |
| **Multi-Token Prediction (MTP)** | Nemotron 3, Step 3.5 Flash | ⬆ 推理加速 |
| **Dense (小模型)** | Phi-4, Ministral 3, Seed-Coder | 边缘场景 |

### 训练方法趋势

| 方向 | 关键进展 |
|------|----------|
| **纯 RL 训练推理** | Magistral (Mistral) 证明纯 RL 无需蒸馏即可训练推理模型 |
| **异步 RL 基础设施** | GLM-5 "slime", ByteDance SRS — 生成与训练解耦 |
| **数据质量 > 数据规模** | Phi-4 合成数据超越教师；InternLM3 4T→18T 效率突破 |
| **Muon 优化器** | DeepSeek V4, Kimi K2 (MuonClip) — 替代 AdamW 趋势 |
| **强化学习联合训练** | K2 joint RL (real + synthetic)；Step 3.5 off-policy RL |

### 多模态 & 长上下文

| 方向 | 最新进展 |
|------|----------|
| **2M 上下文** | Gemini 3.1 Pro (2M tokens, 行业最长) |
| **1M 上下文** | DeepSeek V4, Nova Premier, Llama 4 Scout (10M), Nemotron 3 |
| **原生多模态 (Early Fusion)** | Llama 4, Gemini 3, Qwen3.5-Omni, Kimi K2.5 |
| **音频+视频+文本统一** | Qwen3.5-Omni (100M+ 小时音视频预训练) |

### 推理模型 (Reasoning Model)

| 方法 | 代表 |
|------|------|
| **Test-time compute scaling** | GPT-5 (router ± thinking), Gemini Deep Think, Grok 4 Heavy |
| **Thinking budget 控制** | Qwen3, DeepSeek V4, Seed1.8 (no_think→think-high) |
| **Hybrid reasoning (chat+think)** | Claude 4 系列, Llama-Nemotron (dynamic toggle) |
| **纯 RL 激发推理** | Magistral, GRPO-based 方法 |

### 中国 vs 西方生态差异

| 维度 | 中国公司 | 西方公司 |
|------|----------|----------|
| **开源策略** | 更积极开源（DeepSeek MIT, Qwen Apache 2.0, GLM-5 MIT） | 更保守（除 Meta Llama、Mistral、NVIDIA 外多为闭源） |
| **架构创新** | MoE + MLA + 长上下文优化领先 | Mamba-Attention hybrid 领先（NVIDIA） |
| **专注领域** | Agentic engineering (GLM-5, K2)；医疗 (Baichuan) | 多模态统一（Google, Apple）；AI Safety（Anthropic, OpenAI） |
| **训练效率** | InternLM3 4T 数据效率突破 | Phi-4 合成数据技术 |
| **生态适配** | 国产芯片全栈适配（GLM-5） | NVIDIA 生态主导 |

---

## 四、报告总览表

| # | 机构 | 最新报告 | 日期 | 参数量 | 架构 | 上下文 |
|---|------|----------|------|--------|------|--------|
| 1 | DeepSeek | DeepSeek-V4 | 2026-04 | 1.6T-A49B / 284B-A13B | MoE + CSA/HCA | 1M |
| 2 | OpenAI | GPT-5 System Card | 2025-08 | 未公开 | Unified + Router | ~200K |
| 3 | Meta AI | Llama 4 | 2025-04 | 109B–400B | MoE + Early Fusion | 1M–10M |
| 4 | Google | Gemini 3.1 Pro | 2026-02 | ~1.5T MoE (est.) | Sparse MoE | 2M |
| 5 | Anthropic | Claude Opus 4.8/Fable 5 | 2026-05/06 | 未公开 | Hybrid Reasoning | — |
| 6 | Mistral | Ministral 3 / Magistral | 2026-01 | 3B–14B (dense) / 24B (MoE) | Dense / MoE + RL | 128K–256K |
| 7 | Microsoft | Phi-4-reasoning-vision | 2026-03 | 15B | Dense | — |
| 8 | Apple | AFM Tech Report 2025 | 2025-07 | ~3B + Server PT-MoE | PT-MoE | — |
| 9 | NVIDIA | Nemotron 3 Ultra | 2026 | 550B-A55B | MoE + Mamba-Attn | 1M |
| 10 | xAI | Grok 4.1 | 2025-11 | 未公开 | MoE | 256K |
| 11 | Amazon | Nova Premier | 2025-04 | 未公开 | — | 1M |
| 12 | Alibaba (Qwen) | Qwen3.5-Omni / Qwen 4 Coder | 2026-02/06 | 397B-A17B / 32B-A3B | MoE + Hybrid Attn | 256K |
| 13 | Zhipu AI | GLM-5 | 2026-02 | 744B-A40B | MoE + DSA | 200K |
| 14 | Moonshot AI | Kimi K2.5 | 2026-01 | 1T-A32B | MoE + MLA | 256K |
| 15 | ByteDance | Seed2.0 | 2026-02 | 200B-A20B | MoE | — |
| 16 | StepFun | Step 3.5 Flash | 2026-02 | 196B-A11B | MoE + MFA | 65K |
| 17 | Shanghai AI Lab | InternLM3 | 2025-01 | 8B | Dense | — |
| 18 | 01.AI | Yi-Lightning | 2024-12 | MoE (未公开) | MoE | — |
| 19 | Baichuan | Baichuan-M3 | 2026-02 | 235B | MoE | — |

---

## 五、数据源说明

- 所有报告基于 arXiv / 官方发布的最新版本
- 部分参数数据为行业估计（标注 est.）
- 报告日期以首次发布/公开日期为准
- 数据截至 2026-06-19
