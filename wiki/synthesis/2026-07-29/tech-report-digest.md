---
title: LLM Tech Report Digest 2026-07-29
type: synthesis
created: 2026-07-29
updated: 2026-07-29
sources: []
tags: [tech-report, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, stepfun, bytedance, 01-ai]
---

# LLM Tech Report Digest 2026-07-29

> 各大 AI 公司最新技术报告汇总。覆盖 20 家机构、30+ 篇报告。

---

## 1. DeepSeek

### DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：面向高效百万 Token 上下文智能 |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| **发布日期** | 2026-04-26 |
| **参数量** | Pro: 1.6T total, 49B activated; Flash: 284B total, 13B activated |
| **训练数据** | Flash 32T tokens, Pro 33T tokens |
| **上下文长度** | 1M tokens |
| **核心架构** | MoE + Hybrid Attention (CSA + HCA) + Manifold-Constrained Hyper-Connections (mHC) + Muon optimizer |
| **主要创新** | Compressed Sparse Attention (CSA) 与 Heavily Compressed Attention (HCA) 混合注意力机制；Muon 优化器实现更快收敛；FP4 量化感知训练；MoE 单融合 kernel |
| **arXiv** | https://arxiv.org/abs/2606.19348 |

### DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3.2：推动开源大语言模型前沿 |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V3.2 / V3.2-Speciale |
| **发布日期** | 2025-12-02 |
| **参数量** | 671B total, 37B activated (MoE) |
| **训练数据** | 14.8T+ tokens |
| **上下文长度** | 128K |
| **核心架构** | MoE + DeepSeek Sparse Attention (DSA) + MLA |
| **主要创新** | DSA 大幅降低长上下文计算复杂度；可扩展 RL 框架（post-training 算力达 pre-training 10%+）；大规模 Agentic 任务合成管线（1800+ 环境、85000+ 复杂 prompt）；Speciale 版本在 IMO 2025 / IOI 2025 获金牌 |
| **arXiv** | https://arxiv.org/abs/2512.02556 |

---

## 2. OpenAI

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **发布机构** | OpenAI |
| **模型系列** | gpt-5-main / gpt-5-thinking / gpt-5-thinking-pro / gpt-5-main-mini / gpt-5-thinking-mini / gpt-5-thinking-nano |
| **发布日期** | 2025-08-13 (v1), 2026-04-24 (v2 with CoT evaluations) |
| **参数量** | 未公开 |
| **训练数据** | 未公开 |
| **上下文长度** | 未公开 |
| **核心架构** | 统一系统：fast model (main) + deep reasoning model (thinking) + 实时 router |
| **主要创新** | Safe-completions（安全完成，替代二元拒绝）；Router 持续训练（用户切换/偏好/正确性信号）；幻觉率降低 5×（vs o3）；HealthBench Hard 46.2%（vs o3 31.6%）；CoT 可监控性评估；CoT 可控性评估 |
| **arXiv** | https://arxiv.org/abs/2601.03267 |

---

## 3. Meta AI (LLaMA)

### Llama 4 模型家族

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4：原生多模态 AI 创新的新时代 |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout (17B×16E) / Llama 4 Maverick (17B×128E) / Llama 4 Behemoth (288B×16E, preview) |
| **发布日期** | 2025-04-05 |
| **参数量** | Scout: 17B activated, 109B total; Maverick: 17B activated, 400B total; Behemoth: 288B activated, ~2T total |
| **训练数据** | Scout ~40T tokens, Maverick ~22T tokens |
| **上下文长度** | Scout 10M, Maverick 1M |
| **核心架构** | MoE + Early Fusion 原生多模态 + iRoPE (interleaved attention layers without positional embeddings) |
| **主要创新** | Meta 首个 MoE 模型；原生多模态（early fusion 统一文本+视觉预训练）；Scout 10M 上下文窗口（业界最长）；Behemoth 教师模型用于共蒸馏（codistillation）；iRoPE 注意力温度缩放实现长度泛化 |
| **技术文档** | https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md |

---

## 4. Google DeepMind (Gemini)

### Gemini 2.5 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5：以高级推理、多模态、长上下文和下一代 Agent 能力推动前沿 |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 Pro / Gemini 2.5 Flash / Gemini 2.0 Flash / Gemini 2.0 Flash-Lite |
| **发布日期** | 2025-07-07 (arXiv) |
| **参数量** | 未公开 |
| **训练数据** | 未公开 |
| **上下文长度** | 1M+ tokens |
| **核心架构** | 原生多模态 Transformer + Thinking 机制 + 可调控思考预算 |
| **主要创新** | Thinking 模型（可控制推理预算）；原生多模态（文本/图像/音频/视频统一理解）；1M+ token 长上下文；处理 3 小时视频；Aider Polyglot / GPQA Diamond / Humanity's Last Exam SoTA；Agentic 工作流能力 |
| **arXiv** | https://arxiv.org/abs/2507.06261 |

---

## 5. Anthropic (Claude)

### Claude Opus 4 & Sonnet 4 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4 和 Claude Sonnet 4 系统卡 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4 / Claude Sonnet 4 |
| **发布日期** | 2025-05-22 |
| **参数量** | 未公开 |
| **训练数据** | 截至 2025 年 3 月的互联网公开信息 + 第三方许可数据 + 用户贡献数据 + 合成数据 |
| **上下文长度** | 未公开 |
| **核心架构** | Hybrid Reasoning LLM（即时响应 + Extended Thinking 双模式） |
| **主要创新** | Hybrid reasoning 双模式；SWE-bench 72.5% (Opus 4)，Terminal-bench 43.2%；ASL-3 安全标准（Opus 4 首次）；Thinking summaries 压缩长思维链；Claude Code SDK；持续数小时的自主编码能力 |
| **系统卡** | https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285/Claude%204%20System%20Card.pdf |

2026 年更新版：已发布 Claude Opus 4.7 / 4.8 / Sonnet 4.6 / 5 / Fable 5 / Mythos 5 等，详见 https://www.anthropic.com/system-cards

---

## 6. Mistral AI

### Mistral 3 家族

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 3：下一代开源多模态多语言 AI |
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 / Ministral 3 (14B/8B/3B) |
| **发布日期** | 2025-12-02 |
| **参数量** | Large 3: 675B total, 41B activated (MoE); Ministral 14B/8B/3B dense |
| **训练数据** | Large 3: 未公开（3000 H200 GPU 训练） |
| **上下文长度** | 256K tokens |
| **核心架构** | Sparse MoE (Large 3) / Dense Transformer (Ministral) + Pixtral vision encoder |
| **主要创新** | Mistral 首个大规模 MoE（自 Mixtral 系列以来）；Apache 2.0 开源；NVFP4 量化（Blackwell 优化）；Cascade Distillation 迭代剪枝+蒸馏（Ministral）；GRPO + ODPO 训练管线；所有模型支持多模态 |
| **Ministral arXiv** | https://arxiv.org/abs/2601.08584 |
| **官方公告** | https://mistral.ai/news/mistral-3/ |

---

## 7. Qwen (Alibaba)

### Qwen3 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **发布机构** | Alibaba Cloud / Qwen Team |
| **模型系列** | Qwen3-0.6B / 1.7B / 4B / 8B / 14B / 32B dense + Qwen3-30B-A3B / 235B-A22B MoE |
| **发布日期** | 2025-05-14 |
| **参数量** | 0.6B ~ 235B (旗舰: 235B total, 22B activated) |
| **训练数据** | 36T tokens, 119 种语言 |
| **上下文长度** | 128K (256K 通过 YaRN 扩展) |
| **核心架构** | Dense + MoE 混合架构 / Thinking + Non-Thinking 双模式融合 |
| **主要创新** | 统一 thinking/non-thinking 模式到单一模型；Thinking budget 机制（可控制推理算力分配）；Strong-to-Weak Distillation（降低小模型训练成本）；119 语言支持；Apache 2.0 开源 |
| **arXiv** | https://arxiv.org/abs/2505.09388 |
| **后续更新** | Qwen3-2507 (2025.07): 支持 1M tokens; Qwen3.5 (2026.02): 397B-A17B; Qwen3.6 (2026.04): 35B-A3B / 27B; Qwen3.5-Omni (2026.04): 全模态 MoE |

---

## 8. Microsoft (Phi)

### Phi-4 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 / Phi-4-reasoning / Phi-4-reasoning-plus |
| **发布日期** | 2024-12-12 (Phi-4), 2025-04-30 (Phi-4-reasoning) |
| **参数量** | 14B |
| **训练数据** | ~10T tokens（以合成数据为主） |
| **上下文长度** | 4K (extended to 16K mid-training) |
| **核心架构** | Decoder-only Transformer (类似 Phi-3-medium) + tiktoken tokenizer |
| **主要创新** | 数据质量优先策略：合成数据占主导（multi-agent prompting, self-revision, instruction reversal）；Pivotal Token Search (PTS) 用于 DPO 数据生成；超越教师模型 GPT-4o（STEM 领域）；Phi-4-reasoning: o3-mini 思维链蒸馏 + GRPO RL |
| **Phi-4 arXiv** | https://arxiv.org/abs/2412.08905 |
| **Phi-4-reasoning** | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/ |

---

## 9. Apple

### Apple Intelligence Foundation Language Models: Tech Report 2025

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型：2025 技术报告 |
| **发布机构** | Apple |
| **模型系列** | On-device ~3B / Server PT-MoE |
| **发布日期** | 2025-07-17 |
| **参数量** | On-device ~3B; Server 未公开 |
| **训练数据** | 多语言多模态大规模数据集（负责任爬取+许可语料+合成数据） |
| **上下文长度** | 未公开 |
| **核心架构** | On-device: KV-cache sharing (37.5% 减少); Server: Parallel-Track Mixture-of-Experts (PT-MoE) + Global-Local interleaved attention |
| **主要创新** | PT-MoE 架构（多 track 并行，MoE 局部于每个 track）；KV-cache sharing（后 37.5% 层共享前层 KV cache）；Local sliding window (4096) + Global NoPE attention 交错设计；2-bit quantization-aware training；Swift Foundation Models 框架（LoRA、工具调用） |
| **arXiv** | https://arxiv.org/abs/2507.13575 |

---

## 10. NVIDIA

### Nemotron 3 家族

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3：面向 Agentic Reasoning 的高效 MoE Hybrid Mamba-Transformer |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Nano (30B-A3B) / Super (120B-A12B) / Ultra (550B-A55B) |
| **发布日期** | 2026-04-14 (Super), 2026-06-09 (Ultra) |
| **参数量** | Nano: 31.6B total, 3.2B active; Super: 120B total, 12B active; Ultra: 550B total, 55B active |
| **训练数据** | Nano: 25T tokens; Super: 25T tokens; Ultra: 20T tokens |
| **上下文长度** | 1M tokens (all) |
| **核心架构** | Hybrid Mamba-Attention MoE + LatentMoE + Multi-Token Prediction (MTP) + NVFP4 pre-training |
| **主要创新** | Mamba-2 + GQA 混合架构（大部分层用 Mamba 减少 KV cache）；LatentMoE 提升每参数精度；NVFP4 低精度预训练（首个超大规模验证）；Multi-teacher On-Policy Distillation (MOPD)；Multi-environment RLVR；推理吞吐量比竞品高 2-7×；全开源（权重+数据+recipe） |
| **Ultra arXiv** | https://arxiv.org/abs/2606.15007 |
| **Super arXiv** | https://arxiv.org/abs/2604.12374 |

### Llama-Nemotron: Efficient Reasoning Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama-Nemotron：高效推理模型 |
| **发布机构** | NVIDIA |
| **模型系列** | LN-Nano (8B) / LN-Super (49B) / LN-Ultra (253B) |
| **发布日期** | 2025-05-02 |
| **核心架构** | 基于 Llama 3 的 Neural Architecture Search (NAS) 优化 + FFN Fusion + 推理切换开关 |
| **主要创新** | NAS 搜索硬件高效架构；动态 reasoning toggle（标准/推理模式切换）；开源 post-training 数据集 |
| **arXiv** | https://arxiv.org/abs/2505.00949 |

---

## 11. xAI (Grok)

### Grok 4 Model Card / Grok 4 Fast / Grok 4.20 / Grok 4.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 系列模型卡 |
| **发布机构** | xAI |
| **模型系列** | Grok 4 / Grok 4 Fast / Grok 4.20 / Grok 4.5 |
| **发布日期** | Grok 4: 2025-08-20; Grok 4 Fast: 2025-09-19; Grok 4.20: 2026-04-07; Grok 4.5: 2026-07-14 |
| **核心架构** | 推理模型 + 多模态理解（Grok 4.20 支持 multi-agent） |
| **主要创新** | Grok 4.20: 单代理/多代理双模式；Grok 4.5: 前沿编码与 agentic 任务模型；强化学习（人工反馈+可验证奖励+模型评分）；Dual-use capabilities 评估（CBRN、网络安全） |
| **Grok 4 Model Card** | https://data.x.ai/2025-08-20-grok-4-model-card.pdf |
| **Grok 4.20 System Card** | https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf |

---

## 12. Amazon (Amazon Nova)

### Amazon Nova 家族 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族：技术报告与模型卡 |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Micro / Lite / Pro / Premier / Canvas / Reel |
| **发布日期** | 2024-12-03 (original), 2025-04-30 (Premier addendum), 2025-10-28 (Embeddings) |
| **核心架构** | Transformer + SFT + DPO + PPO 对齐 |
| **上下文长度** | Premier: 1M tokens |
| **主要创新** | Premier: 最强大多模态基础模型 + 教师蒸馏模型；Canvas: 扩散模型文本生图；Reel: 文生视频；MME: 首个支持文本/文档/图像/视频/音频 5 模态统一 Embedding 模型；200+ 语言训练 |
| **arXiv** | https://arxiv.org/abs/2506.12103 |

---

## 13. Zhipu AI (GLM/ChatGLM)

### GLM-5: From Vibe Coding to Agentic Engineering

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-5 / 5.1 / 5.2 (744B-A40B) |
| **发布日期** | 2026-02-12 |
| **参数量** | 744B total, 40B activated (MoE) |
| **训练数据** | 28.5T tokens |
| **上下文长度** | 200K tokens |
| **核心架构** | MoE + DeepSeek Sparse Attention (DSA) + 异步 RL 基础设施 (slime) |
| **主要创新** | DSA 降低训练/推理成本；异步 RL 基础设施（解耦生成与训练，极大提升 GPU 利用率）；异步 Agent RL 算法（长程交互学习）；On-Policy Cross-Stage Distillation（防止灾难性遗忘）；全栈适配国产 GPU 生态（7 个国内芯片平台）；MIT 开源 |
| **arXiv** | https://arxiv.org/abs/2602.15763 |

---

## 14. InternLM / Shanghai AI Lab

### Intern-S1 / Intern-S1-Pro

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1：科学多模态基础模型 / Intern-S1-Pro：万亿参数科学多模态基础模型 |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | Intern-S1 (241B-A28B) / Intern-S1-Pro (1T-A??B) |
| **发布日期** | 2025-08 (S1), 2026-03-26 (S1-Pro) |
| **参数量** | S1: 241B total, 28B activated; S1-Pro: ~1T total |
| **训练数据** | S1: 5T tokens (含 2.5T 科学数据); S1-Pro: +6T 高质量多模态数据 |
| **核心架构** | MoE + Grouped Routing + Mixture-of-Rewards (MoR) |
| **主要创新** | S1: 首个开源科学多模态模型；MoR 框架统一 1000+ 任务的多样化奖励信号；InternBootCamp 大规模交互式 RL 环境；S1-Pro: 万亿参数规模；Grouped Routing 解决大规模 MoE 负载不均；科学领域超越 GPT-5.2 / Gemini-3-Pro（SciReasoner 55.5 vs 14.7 vs 13.6）|
| **S1-Pro arXiv** | https://arxiv.org/abs/2603.25040 |
| **S1 arXiv** | https://arxiv.org/abs/2508.15763 |

---

## 15. Moonshot AI (Kimi)

### Kimi K2: Open Agentic Intelligence

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开源 Agentic 智能 |
| **发布机构** | Moonshot AI |
| **模型系列** | Kimi K2 Base / Instruct |
| **发布日期** | 2025-07-28 |
| **参数量** | 1.04T total, 32B activated (MoE) |
| **训练数据** | 15.5T tokens |
| **上下文长度** | 128K (后更新至 256K) |
| **核心架构** | Ultra-sparse MoE (384 experts) + Multi-head Latent Attention (MLA) + MuonClip optimizer |
| **主要创新** | MuonClip 优化器（QK-Clip 解决训练不稳定，零 loss spike）；384 专家超高稀疏度（Scaling Law 分析驱动）；大规模 Agentic 数据合成管线（数百领域、数千工具）；General RL 自我评判机制（verifiable + non-verifiable rewards）；Agentic 能力开源 SOTA（SWE-bench 65.8%，Tau2-Bench 66.1） |
| **arXiv** | https://arxiv.org/abs/2507.20534 |

---

## 16. StepFun (阶跃星辰)

### Step3: Cost-Effective Multimodal Intelligence

| 项目 | 内容 |
|------|------|
| **中文标题** | Step3：高性价比多模态智能 |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step3 (321B-A38B MoE 多模态) / STEP3-VL-10B / Step-DeepResearch |
| **发布日期** | 2025-07-31 (Step3), 2026-01-14 (STEP3-VL-10B) |
| **参数量** | Step3: 321B total, 38B active; STEP3-VL-10B: 10B |
| **核心架构** | MoE + Multi-Matrix Factorization Attention (MFA) + Attention-FFN Disaggregation (AFD) |
| **主要创新** | **Step3**: MFA 将注意力 FLOPs 降至 DeepSeek-V3 的 22%；AFD 解耦 Attention/FFN 到独立子系统实现并行推理；StepMesh 通信库；解码吞吐 4039 tok/s/GPU（4K context）；**STEP3-VL-10B**: 10B 参数匹敌 235B 模型；PaCoRe 并行协调推理；AIME2025 94.43%；**Step-DeepResearch**: 32B agent 实现专家级深度研究，成本 <0.50 RMB/次 |
| **Step3 arXiv** | https://arxiv.org/abs/2507.19427 |
| **STEP3-VL arXiv** | https://arxiv.org/abs/2601.09668 |
| **DeepResearch arXiv** | https://arxiv.org/abs/2512.20491 |

---

## 17. ByteDance (Doubao / Seed)

### Seed 2.0 / Seed 1.8

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 2.0 系列 / Seed 1.8 通用 Agent 模型 |
| **发布机构** | ByteDance Seed Team |
| **模型系列** | Seed 2.0 Pro / Lite / Mini + Code; Seed 1.8 |
| **发布日期** | 2025-12-18 (Seed 1.8), 2026-02-14 (Seed 2.0) |
| **核心架构** | LLM + VLM + Agent 统一框架 |
| **主要创新** | Seed 2.0 Pro: 对标 GPT-5.2 / Gemini 3 Pro；SuperGPQA 超越 GPT-5.2；长链推理+Agent 能力升级；Seed 2.0 Lite (0428): 首个全模态理解模型（视频/图像/音频/文本统一）；Seed 1.8: 通用 Agent 模型（信息检索/代码生成/GUI 交互） |
| **官方** | https://seed.bytedance.com |

---

## 18. 01.AI (Yi)

### Yi-Lightning Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **发布机构** | 01.AI |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024-12-02 |
| **参数量** | 未公开 (MoE) |
| **核心架构** | MoE + 细粒度专家分割 + 跨层 KV cache 共享 |
| **主要创新** | Chatbot Arena 第 6 名（中文第 2，数学第 3，编码第 4）；Fine-grained expert segmentation；Balanced expert routing；RAISE 安全框架（四组件贯穿全生命周期）；指出静态 benchmark 与真实人类偏好之间的显著差距 |
| **arXiv** | https://arxiv.org/abs/2412.01253 |

---

## 19. Baichuan

> 截至 2026-07-29，未检索到 Baichuan 近期（2025-2026）发布的正式技术报告。Baichuan 目前主要提供商业 API 服务。

---

## 20. 其他值得关注的报告

| 报告 | 机构 | 日期 | 链接 |
|------|------|------|------|
| MiniMax-M2 | MiniMax | 2025 | 未找到完整 arXiv |
| Qwen3.5-Omni | Alibaba | 2026-04 | https://arxiv.org/abs/2604.15804 |
| Amazon Nova Multimodal Embeddings | Amazon | 2025-10 | Amazon Science |
| Leanstral (Lean 4 agent) | Mistral AI | 2026-03 | https://mistral.ai/news/leanstral/ |
| Gemini 2.0 Flash-Lite | Google | 2025-06 | DeepMind |

---

## 分类汇总

### 大模型新架构（MoE, Mamba, Hybrid）
- DeepSeek-V4: MoE + Hybrid CSA/HCA Attention
- Llama 4: MoE + Early Fusion 多模态
- Mistral Large 3: Sparse MoE (回归)
- Nemotron 3: Hybrid Mamba-Transformer MoE + LatentMoE
- Step3: MoE + Multi-Matrix Factorization Attention
- Apple PT-MoE: Parallel Track 并行 MoE
- Kimi K2: Ultra-sparse MoE (384 experts) + MLA

### 训练方法（Pre-training, Post-training, Alignment, RL）
- DeepSeek-V3.2: 可扩展 RL + Agentic 合成管线
- GLM-5: 异步 RL (slime) + On-Policy Cross-Stage Distillation
- Kimi K2: MuonClip + 大规模 Agentic 合成 + General RL
- Phi-4-reasoning: SFT + GRPO + o3-mini 蒸馏
- Intern-S1: Mixture-of-Rewards + 1000+ 任务并行 RL
- Llama-Nemotron: NAS + KD + CPT + RL 五阶段

### Scaling Law / 缩放分析
- Kimi K2: 稀疏度 Scaling Law 分析（384 专家决策依据）
- Step3: Step Law 最优超参数缩放律 (arXiv:2503.04715)
- Nemotron 3: NVFP4 低精度预训练缩放验证
- Intern-S1-Pro: 万亿参数扩展（4× 规模仅 20% 效率损失）

### 多模态模型
- Llama 4: 原生多模态 MoE
- Gemini 2.5: 原生多模态 Thinking 模型
- Qwen3.5-Omni: 全模态 Thinker-Talker MoE
- Step3: 321B 多模态 MoE
- Seed 2.0 Lite: 全模态（视频/图像/音频/文本）
- Intern-S1-Pro: 科学多模态万亿参数模型
- Apple Intelligence: 多模态 on-device + server 模型

### 长上下文模型
- DeepSeek-V4: 1M tokens（高效 27% FLOPs, 10% KV cache）
- Llama 4 Scout: 10M tokens（业界最长）
- Gemini 2.5: 1M+ tokens
- Nemotron 3: 1M tokens
- Qwen3-2507: 支持 1M tokens
- Amazon Nova Premier: 1M tokens

### 推理模型 / Reasoning Models
- GPT-5: gpt-5-thinking（Router + Main + Thinking 统一系统）
- Gemini 2.5 Pro/Flash: Thinking 模型 + 可控制推理预算
- Claude Opus 4: Hybrid reasoning 双模式
- DeepSeek-V4-Pro-Max: 最大推理努力模式
- Phi-4-reasoning: 14B 小模型推理
- Llama-Nemotron: 动态 reasoning toggle
- Qwen3: Thinking/Non-thinking 统一 + Budget 控制
- Step3: PaCoRe 并行协调推理
- GLM-5: 三级 RL（Reasoning → Agentic → General）
