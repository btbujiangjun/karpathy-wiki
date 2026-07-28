---
title: 2026-07-28 Tech Report Digest
type: synthesis
created: 2026-07-28
updated: 2026-07-28
sources: []
tags: [tech-report, digest, LLM, 2026]
---

# 2026-07-28 技术报告摘要 | Tech Report Digest

本页汇总 19 家主要 AI 公司/机构截至 2026 年 7 月的最新技术报告。
This page summarizes the latest technical reports from 19 major AI organizations as of July 2026.

---

## 1. DeepSeek

| 字段 | 内容 |
|------|------|
| 英文标题 | DeepSeek-V4 Technical Report |
| 中文标题 | DeepSeek-V4 技术报告 |
| 机构 | DeepSeek |
| 模型 | V4-Pro (1.6T total / 49B activated MoE), V4-Flash (284B / 13B activated) |
| 发布日期 | 2026-04 |
| 训练数据 | V4-Pro: 33T tokens; V4-Flash: 32T tokens |
| 上下文长度 | 1M tokens |
| 核心创新 | Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) — 在 1M tokens 下仅用 27% FLOPs 和 10% KV cache；Manifold-Constrained Hyper-Connections (mHC)；Muon optimizer；FP4+FP8 混合精度；两阶段后训练 (domain expert SFT+GRPO RL → on-policy distillation) |
| 链接 | [arxiv.org/abs/2606.19348](https://arxiv.org/abs/2606.19348) · [HuggingFace 开源](https://huggingface.co/deepseek-ai) |

---

## 2. OpenAI

| 字段 | 内容 |
|------|------|
| 英文标题 | GPT-5 System Card |
| 中文标题 | GPT-5 系统卡 |
| 机构 | OpenAI |
| 模型 | GPT-5 (GPT-5 / GPT-5 Pro / GPT-5 Chat) |
| 发布日期 | 2025-08 (revised 2026-05) |
| 训练数据 | 未披露；描述为 "massive scale web + licensed data" |
| 上下文长度 | 128K tokens |
| 核心创新 | 知识蒸馏 (distill from larger models)；动态推理 (adaptive reasoning — auto / thinking / fast)；SME 网络 (Subject Matter Expert networks — 1400+ domain-specific experts on demand)；256K tokenizer；原生多模态 (text/image/audio/video) |
| 链接 | [openai.com/index/gpt-5-system-card](https://openai.com/index/gpt-5-system-card/) (仅模型卡，无 arXiv 技术报告) |

---

## 3. Meta AI (LLaMA)

| 字段 | 内容 |
|------|------|
| 英文标题 | The Llama 4 Herd of Models |
| 中文标题 | Llama 4 模型群 |
| 机构 | Meta AI |
| 模型 | Scout (17B act / 109B total, 16 experts), Maverick (17B act / 400B, 128 experts), Behemoth (preview, >1.8T total / 288B act) |
| 发布日期 | 2025-04 |
| 训练数据 | Scout: ~40T tokens; Maverick: ~22T tokens；含 Instagram/Facebook 公开数据 |
| 上下文长度 | Scout: 10M tokens; Maverick: 1M tokens |
| 核心创新 | 首个开源原生多模态 MoE (early fusion text+image)；iRoPE + 长度泛化策略 (Scout)；Scout 量化后可在单张 H100 上运行；后训练: SFT + online RL + lightweight DPO |
| 链接 | [ai.meta.com/blog/llama-4-multimodal-intelligence](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) · [arxiv.org/abs/2601.11659](https://arxiv.org/abs/2601.11659) (**WITHDRAWN**) |

> ⚠️ 注意：arXiv 论文已被撤回，官方信息以 Meta 博客和 GitHub 模型卡为准。

---

## 4. Google DeepMind (Gemini)

| 字段 | 内容 |
|------|------|
| 英文标题 | Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context |
| 中文标题 | Gemini 1.5：解锁跨百万 token 的多模态理解 |
| 机构 | Google DeepMind |
| 模型 | Gemini 1.5 Pro, Gemini 1.5 Flash |
| 发布日期 | 2024-03 (v2, 最新版) |
| 训练数据 | 未披露；描述为 "multimodal and multilingual"，在 TPUv4 pods 上训练 |
| 上下文长度 | Pro: 10M tokens (99.2% recall at 10M on needle-in-a-haystack)；Flash: 2M tokens (100% recall) |
| 核心创新 | MoE 架构；10M token 上下文窗口 (generational leap)；原生多模态 (text + image + audio + video)；在上下文中学习 Kalamang 语 (仅 200 说话者) |
| 链接 | [arxiv.org/abs/2403.05530](https://arxiv.org/abs/2403.05530) |

> ⚠️ 注意：论文未披露总参数量、训练 FLOPs 和数据集大小。

---

## 5. Anthropic (Claude)

| 字段 | 内容 |
|------|------|
| 英文标题 | Claude Opus 4.7 System Card |
| 中文标题 | Claude Opus 4.7 系统卡 |
| 机构 | Anthropic |
| 模型 | Claude Opus 4.7, Claude Sonnet 4.6 |
| 发布日期 | 2026-04 |
| 训练数据 | 未披露；安全对齐采用 Constitutional AI + RLHF；训练数据截至 2026 年初 |
| 上下文长度 | Opus 4.7: 1M tokens；Sonnet 4.6: 200K tokens |
| 核心创新 | 安全对齐 (Constitutional AI + RLHF + Red Teaming)；多模态 (文本+图像+代码)；SWE-bench 73.2% (Opus 4.7)；AIME 2025 92.3% (Sonnet 4.6)；自主代理模式 (Computer Use, tool calling) |
| 链接 | [anthropic.com/research/claude-opus-4-7-system-card](https://www.anthropic.com/research/claude-opus-4-7-system-card) (仅系统卡，无 arXiv) |

---

## 6. Mistral AI

| 字段 | 内容 |
|------|------|
| 英文标题 | Magistral Technical Report |
| 中文标题 | Magistral 技术报告 |
| 机构 | Mistral AI |
| 模型 | Magistral-Small (24B), Magistral-Medium (未披露参数) |
| 发布日期 | 2025-06 |
| 训练数据 | 未披露 |
| 上下文长度 | 128K tokens |
| 核心创新 | Mistral 首个 reasoning 模型；多语言推理 (35+ 语言)；支持 "thinking mode" 与 "non-thinking mode" 切换；SWE-bench Verified 72.7%；在 128K 上下文内完成长链推理 |
| 链接 | [mistral.ai/magistral](https://mistral.ai/magistral/) (仅博客，无 arXiv 技术报告) |

---

## 7. Qwen (Alibaba)

| 字段 | 内容 |
|------|------|
| 英文标题 | Qwen3 Technical Report |
| 中文标题 | Qwen3 技术报告 |
| 机构 | Alibaba Cloud (通义千问) |
| 模型 | Dense: 0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B, 235B-A22B；MoE: 30B-A3B (128 experts, 8 active), 235B-A22B (128 experts, 8 active) |
| 发布日期 | 2025-05 |
| 训练数据 | 约 36T+ tokens；8 种语言 + 119 种文本和 119 种代码方言 |
| 上下文长度 | 32K (base) → 128K (after long-context extension) |
| 核心创新 | Hybrid Thinking (thinking/non-thinking 动态切换)；支持 119+ 编程语言；Agent 能力 (function calling, MCP 工具集成)；全部开源 (Apache 2.0 / Qwen 许可)；3 种推理预算模式 |
| 链接 | [arxiv.org/abs/2505.09388](https://arxiv.org/abs/2505.09388) |

---

## 8. 01.AI (Yi)

| 字段 | 内容 |
|------|------|
| 英文标题 | Yi-Lightning Technical Report |
| 中文标题 | Yi-Lightning 技术报告 |
| 机构 | 01.AI (零一万物) |
| 模型 | Yi-Lightning (Enhanced MoE，参数未披露) |
| 发布日期 | 2024-12 |
| 训练数据 | 未披露 |
| 上下文长度 | 未披露 |
| 核心创新 | Enhanced MoE + 高级 expert segmentation & routing；优化的 KV-caching；多阶段 pre-training + SFT + RLHF pipeline；RAISE (Responsible AI Safety Engine) 四组件安全框架；Chatbot Arena 总分第 6，中文/数学/编码第 2-4 |
| 链接 | [arxiv.org/abs/2412.01253](https://arxiv.org/abs/2412.01253) |

---

## 9. Baichuan (百川智能)

| 字段 | 内容 |
|------|------|
| 英文标题 | Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care |
| 中文标题 | Baichuan-M4：面向持续医疗照护的临床级医疗 Agent 系统 |
| 机构 | Baichuan Intelligence + Tsinghua University |
| 模型 | Baichuan-M4 (Jun 2026), Baichuan-M3 (235B, Feb 2026) |
| 发布日期 | M4: 2026-06; M3: 2026-02 |
| 训练数据 | 未披露 |
| 上下文长度 | 未披露 |
| 核心创新 | Baichuan-Harness — 统一 RL training + deployment runtime；Continuous-care RL + SPAR++ span-level reward；reasoning-path compression + curriculum learning；临床工具层 (patient-memory, evidence-based retrieval, 多模态医学感知)；幻觉率降至 3.3%；M3 在 HealthBench-Hard 上超 GPT-5.2 (44.4 vs 42.0) |
| 链接 | [arxiv.org/abs/2606.08982](https://arxiv.org/abs/2606.08982) (M4) · [arxiv.org/abs/2602.06570](https://arxiv.org/abs/2602.06570) (M3) |

---

## 10. Microsoft (Phi)

| 字段 | 内容 |
|------|------|
| 英文标题 | Phi-4-reasoning-vision-15B Technical Report |
| 中文标题 | Phi-4-reasoning-vision-15B 技术报告 |
| 机构 | Microsoft Research |
| 模型 | Phi-4-reasoning-vision-15B (Mar 2026), Phi-4-reasoning (14B, Apr 2025), Phi-4-Mini (3.8B, Mar 2025) |
| 发布日期 | 2026-03 (vision), 2025-04 (reasoning), 2025-03 (Mini) |
| 训练数据 | 仅 200B multimodal tokens (远少于同类 1T+) |
| 上下文长度 | 未披露 |
| 核心创新 | 15B 视觉推理模型竞争力媲美更大模型；Mixture-of-LoRAs — 模态特定 LoRA + frozen base LM；o3-mini teacher distillation；hybrid reasoning/non-reasoning mode tokens；高分辨率 dynamic-resolution vision；200K vocabulary 多语言 |
| 链接 | [arxiv.org/abs/2603.03975](https://arxiv.org/abs/2603.03975) (15B vision) · [arxiv.org/abs/2504.21318](https://arxiv.org/abs/2504.21318) (reasoning) · [arxiv.org/abs/2503.01743](https://arxiv.org/abs/2503.01743) (Mini) |

---

## 11. Apple

| 字段 | 内容 |
|------|------|
| 英文标题 | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| 中文标题 | Apple Intelligence 基础语言模型技术报告 2025 |
| 机构 | Apple |
| 模型 | Apple Intelligence Foundation Models (on-device ~3B + server PT-MoE) |
| 发布日期 | 2025-07 |
| 训练数据 | 未披露 |
| 上下文长度 | 未披露 |
| 核心创新 | Parallel-Track Transformer — 模型分区为独立处理的 "tracks"，仅在边界同步；PT-MoE (track 内 MoE 层)；interleaved global-local attention (3 local sliding window 4096 + 1 global NoPE)；2-bit QAT (on-device)；3.56 bpw ASTC compression (server)；支持 16 种语言 + 图像理解 + 工具调用 |
| 链接 | [arxiv.org/abs/2507.13575](https://arxiv.org/abs/2507.13575) |

---

## 12. NVIDIA

| 字段 | 内容 |
|------|------|
| 英文标题 | Nemotron 3 Ultra Technical Report |
| 中文标题 | Nemotron 3 Ultra 技术报告 |
| 机构 | NVIDIA |
| 模型 | Nemotron 3 Ultra (550B total / 29B activated，Mamba-Attention Hybrid MoE) |
| 发布日期 | 2026-06 |
| 训练数据 | 未披露 (描述为大规模合成 + 真实数据混合) |
| 上下文长度 | 128K tokens |
| 核心创新 | Hybrid Mamba-Attention — 9 层 Mamba (SSM) + 33 层 Attention，每 4 层交替；384 experts per layer (top-8 routing)；3-stage RL pipeline (SFT → Rejection Sampling → DPO/GRPO)；512K vocabulary；full-precision routing + shared expert |
| 链接 | [arxiv.org/abs/2607.01484](https://arxiv.org/abs/2607.01484) |

---

## 13. xAI (Grok)

| 字段 | 内容 |
|------|------|
| 英文标题 | Grok 4 Model Card |
| 中文标题 | Grok 4 模型卡 |
| 机构 | xAI |
| 模型 | Grok 4, Grok 4 Heavy |
| 发布日期 | 2025-07 (card dated 2025-08-20) |
| 训练数据 | 未披露；Colossus 集群 200,000 H100；比 Grok 2 多 100× compute；训练数据截至 2024-12 |
| 上下文长度 | 256K tokens |
| 核心创新 | pretraining 阶段大规模 RL (verifiable rewards)；原生工具使用 (code interpreter, web browsing, X search) 通过 RL 嵌入训练；Grok 4 Heavy: 并行 test-time compute (最多 32 agents)；Humanity's Last Exam 50%；ARC-AGI V2 SOTA (15.9% vs Claude Opus ~8.6%) |
| 链接 | [data.x.ai/2025-08-20-grok-4-model-card.pdf](https://data.x.ai/2025-08-20-grok-4-model-card.pdf) (仅模型卡，无 arXiv) |

---

## 14. Amazon (Nova)

| 字段 | 内容 |
|------|------|
| 英文标题 | The Amazon Nova Family of Models: Technical Report and Model Card |
| 中文标题 | Amazon Nova 模型家族技术报告与模型卡 |
| 机构 | Amazon AGI |
| 模型 | Nova Pro, Nova Lite, Nova Micro, Nova Premier (Apr 2025，最新旗舰) |
| 发布日期 | 2024-12 (original), 2025-03 (arXiv), 2025-04 (Premier) |
| 训练数据 | 200+ 种语言，重点 15 种主要语言 |
| 上下文长度 | Nova Premier: 1M tokens |
| 核心创新 | 分层产品线 (Pro=accuracy+speed+cost, Lite=ultra-fast, Micro=lowest-latency)；原生多模态 (text+image+document+video)；Nova Premier 作为 teacher distill 到 smaller models；agentic performance (BFCL tool calling)；DPO + PPO 对齐 |
| 链接 | [arxiv.org/abs/2506.12103](https://arxiv.org/abs/2506.12103) |

---

## 15. Zhipu AI (GLM)

| 字段 | 内容 |
|------|------|
| 英文标题 | GLM-5 Technical Report |
| 中文标题 | GLM-5 技术报告 |
| 机构 | Zhipu AI (智谱 AI) |
| 模型 | GLM-5 (744B total / 40B activated, 256 experts, 80 layers) |
| 发布日期 | 2026-02 |
| 训练数据 | 28.5T tokens (base) |
| 上下文长度 | 200K tokens (progressively: 32K→128K→200K) |
| 核心创新 | DeepSeek Sparse Attention (DSA) — 长序列 attention 计算减少 ~1.5-2×；异步 RL 基础设施 (TITO gateway + Direct Double-sided Importance Sampling)；异步 Agent RL；Sequential post-training RL pipeline (Reasoning→Agentic→General RL)；3 shared MTP layers (higher acceptance rate)；适配 7 个国产 GPU 平台 (华为昇腾、摩尔线程、海光、寒武纪等)；开源 BF16+FP8 |
| 链接 | [arxiv.org/abs/2602.15763](https://arxiv.org/abs/2602.15763) |

---

## 16. InternLM (上海 AI Lab)

| 字段 | 内容 |
|------|------|
| 英文标题 | Intern-S1-Pro Technical Report |
| 中文标题 | Intern-S1-Pro 技术报告 |
| 机构 | Shanghai AI Laboratory (上海 AI 实验室) |
| 模型 | Intern-S1-Pro (1T total / 56B activated, MoE + Mamba + Hybrid) |
| 发布日期 | 2026-03 |
| 训练数据 | 约 20T tokens |
| 上下文长度 | 256K tokens |
| 核心创新 | 全球首个开源 Science Foundation Model；Hybrid Mamba + Attention + MoE；1T total / 56B activated；Science Agent (集成实验设计、数据分析、文献检索)；20B science tokens；3 阶段训练 (generic→science→agent)；agent training (RLHF + Tool-Integrated Reasoning)；20 科学工具集成 (RDKit, MDAnalysis, PySCF 等) |
| 链接 | [arxiv.org/abs/2603.02715](https://arxiv.org/abs/2603.02715) |

---

## 17. Moonshot AI (Kimi)

| 字段 | 内容 |
|------|------|
| 英文标题 | Kimi K2.5 Technical Report |
| 中文标题 | Kimi K2.5 技术报告 |
| 机构 | Moonshot AI (月之暗面) |
| 模型 | Kimi K2.5 (1T total / 32B activated, 384 experts, 8 active + 1 shared)；Kimi K3 (Jul 2026 announced，2.8T total / 33B activated，tech report pending) |
| 发布日期 | 2026-02 |
| 训练数据 | ~15T mixed visual + text tokens (continual pretrain on Kimi-K2-Base) |
| 上下文长度 | 256K tokens |
| 核心创新 | Joint text-vision pre-training (early fusion 优于 late fusion)；Zero-vision SFT (text-only SFT 激活视觉推理)；Joint RL (text+vision bidirectional enhancement)；Agent Swarm — self-directed parallel agent orchestration (Parallel-Agent RL / PARL)；MoonViT-3D (400M params) + NaViT packing；K3: 2.8T total / 33B activated (Jul 2026 announced, tech report pending) |
| 链接 | [arxiv.org/abs/2602.02276](https://arxiv.org/abs/2602.02276) |

---

## 18. StepFun (阶跃星辰)

| 字段 | 内容 |
|------|------|
| 英文标题 | Step 3.5 Flash / Step3 Technical Report |
| 中文标题 | Step 3.5 Flash / Step3 技术报告 |
| 机构 | StepFun (阶跃星辰) |
| 模型 | Step 3.5 Flash (196B MoE / 11B active, Feb 2026), Step3 (321B / 38B active, Jul 2025), Step3-VL-10B (Jan 2026) |
| 发布日期 | Step 3.5: 2026-02; Step3: 2025-07; Step3-VL: 2026-01 |
| 训练数据 | Step3-VL: 1.2T tokens unified pre-training |
| 上下文长度 | 256K tokens (Step 3.5 Flash) |
| 核心创新 | Step 3.5 Flash: 3-way Multi-Token Prediction (MTP-3) — 100-300 tok/s throughput；3:1 Sliding Window Attention + Head-wise Gated Attention；SWE-bench 74.4%；Step3-VL: Parallel Coordinated Reasoning (PaCoRe)；Step3: Multi-Matrix Factorization Attention (MFA) + Attention-FFN Disaggregation |
| 链接 | [blog: static.stepfun.com/blog/step-3.5-flash/](https://static.stepfun.com/blog/step-3.5-flash/) · [arxiv.org/abs/2507.19427](https://arxiv.org/abs/2507.19427) (Step3) · [arxiv.org/abs/2601.09668](https://arxiv.org/abs/2601.09668) (VL) |

---

## 19. ByteDance (Seed / 豆包)

| 字段 | 内容 |
|------|------|
| 英文标题 | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Tasks |
| 中文标题 | Seed2.0 模型卡：迈向真实世界的智能前沿 |
| 机构 | ByteDance Seed Team (字节跳动 Seed 团队) |
| 模型 | Seed2.0 (Pro / Lite / Mini / Code, 3 tiers, 参数未披露)；Seed1.8 (Mar 2026)；Seed1.5-VL (May 2025) |
| 发布日期 | Seed2.0: 2026-02 (card Jun 2026); Seed1.8: 2026-03; Seed1.5-VL: 2025-05 |
| 训练数据 | 未披露 |
| 上下文长度 | 未披露 |
| 核心创新 | Seed2.0 聚焦 long-tail domain knowledge + complex instruction following；4 维评估 (Science Discovery / Vibe Coding / Context Learning / Real-World Tasks)；agentic capabilities (plan-act-reflect cycles)；性能媲美 GPT-5.2 High / Claude-Opus-4.5 / Gemini-3-Pro，成本约 1/10；Seed1.8: unified agentic interaction (search, code execution, GUI interaction)；三个尺寸提供 cost/performance 灵活性 |
| 链接 | [arxiv.org/abs/2607.00248](https://arxiv.org/abs/2607.00248) (Seed2.0) · [arxiv.org/abs/2603.20633](https://arxiv.org/abs/2603.20633) (Seed1.8) · [seed.bytedance.com/zh/seed2](https://seed.bytedance.com/zh/seed2) |

---

## 横向对比 | Cross-Company Comparison

### 模型规模对比

| 公司 | 模型 | 总参数 | 激活参数 | 架构 |
|------|------|--------|----------|------|
| DeepSeek | V4-Pro | 1.6T | 49B | MoE (DeepSeekMoE) |
| DeepSeek | V4-Flash | 284B | 13B | MoE |
| Meta | LLaMA 4 Behemoth | >1.8T | 288B | MoE |
| Meta | LLaMA 4 Maverick | 400B | 17B | MoE (128 experts) |
| Meta | LLaMA 4 Scout | 109B | 17B | MoE (16 experts) |
| Zhipu | GLM-5 | 744B | 40B | MoE (256 experts) |
| InternLM | Intern-S1-Pro | 1T | 56B | MoE + Mamba Hybrid |
| Moonshot | Kimi K2.5 | 1T | 32B | MoE (384 experts) |
| Moonshot | Kimi K3 (preview) | 2.8T | 33B | MoE |
| StepFun | Step3 | 321B | 38B | MoE |
| StepFun | Step 3.5 Flash | 196B | 11B | MoE |
| Baichuan | Baichuan-M3 | 235B | — | — |
| NVIDIA | Nemotron 3 Ultra | 550B | 29B | Mamba-Attention Hybrid MoE |
| Qwen | Qwen3-235B-A22B | 235B | 22B | MoE (128 experts) |
| Microsoft | Phi-4-vision | 15B | 15B | Dense + Mixture-of-LoRAs |
| Apple | AFM (on-device) | ~3B | ~3B | Dense (PT-MoE server) |

### 上下文长度对比

| 公司 | 模型 | 上下文长度 |
|------|------|------------|
| Meta | LLaMA 4 Scout | 10M |
| Google | Gemini 1.5 Pro | 10M |
| DeepSeek | V4-Pro | 1M |
| Amazon | Nova Premier | 1M |
| Anthropic | Claude Opus 4.7 | 1M |
| Moonshot | Kimi K2.5 | 256K |
| xAI | Grok 4 | 256K |
| InternLM | Intern-S1-Pro | 256K |
| StepFun | Step 3.5 Flash | 256K |
| Zhipu | GLM-5 | 200K |
| Anthropic | Claude Sonnet 4.6 | 200K |
| OpenAI | GPT-5 | 128K |
| Mistral | Magistral | 128K |
| NVIDIA | Nemotron 3 Ultra | 128K |
| Alibaba | Qwen3 | 128K (after extension) |

### 开源 vs 闭源

| 开源 | 闭源 |
|------|------|
| DeepSeek V4-Pro/Flash | OpenAI GPT-5 |
| Meta LLaMA 4 (Scout/Maverick) | Anthropic Claude Opus 4.7 |
| Qwen3 (全系列) | xAI Grok 4 |
| Zhipu GLM-5 | Mistral Magistral |
| InternLM Intern-S1-Pro | Apple Intelligence FM |
| Moonshot Kimi K2.5 | Amazon Nova Premier |
| NVIDIA Nemotron 3 Ultra | ByteDance Seed2.0 |
| Microsoft Phi-4 系列 | Google Gemini 1.5 |
| 01.AI Yi-Lightning | |
| Baichuan M3/M4 | |
| StepFun Step3-VL-10B | |

---

## 趋势观察 | Trend Observations

### 1. MoE 成为绝对主流
19 家公司中 15+ 家采用 MoE 架构。DeepSeek 的 MLA + Compressed Attention、GLM-5 的 DSA、NVIDIA 的 Mamba-Attention Hybrid 代表了 MoE 的最新演进方向。

### 2. 长上下文竞赛白热化
Meta Scout (10M) 和 Google Gemini 1.5 Pro (10M) 将上限推至千万级；DeepSeek V4 (1M)、Amazon Nova Premier (1M)、Claude Opus 4.7 (1M) 稳守百万级。

### 3. Reasoning 模型分化
- 独立 reasoning 模型: Mistral Magistral, OpenAI o3/o4-mini, Qwen3
- Hybrid reasoning/non-reasoning 切换: OpenAI GPT-5, Qwen3, Microsoft Phi-4
- 原生 reasoning: DeepSeek V4 (GRPO RL), GLM-5 (Reasoning RL stage)

### 4. Agent 能力成标配
几乎所有 2026 年发布的新模型都强调 agentic capabilities — tool calling、code execution、GUI interaction、multi-step planning。从 GPT-5 的 SME agents 到 Kimi K2.5 的 Agent Swarm。

### 5. Mamba/SSM 复兴
NVIDIA Nemotron 3 Ultra (9 层 Mamba + 33 层 Attention) 和 InternLM Intern-S1-Pro (Mamba + Attention Hybrid) 代表了 SSM 在超大规模模型中的实际部署。GLM-5 的 MTP 层也借鉴了 SSM 思想。

### 6. 国产 GPU 适配加速
GLM-5 明确适配华为昇腾、摩尔线程、海光、寒武纪等 7 个国产平台，InternLM 也在国产硬件上训练。中美 AI 竞争推动基础设施多元化。

### 7. 多模态走向原生
Meta LLaMA 4、OpenAI GPT-5、Qwen3、Gemini 1.5、Seed1.5-VL 均采用原生多模态 (early fusion)，而非后期拼接。Moonshot Kimi K2.5 的 Joint text-vision pre-training 是典型代表。
