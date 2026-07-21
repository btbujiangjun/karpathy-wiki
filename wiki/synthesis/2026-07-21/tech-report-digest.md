---
title: "LLM Tech Report Daily"
title-zh: "大模型技术报告日报"
type: synthesis
created: 2026-07-21
updated: 2026-07-21
sources: []
tags: [llm, tech-report, daily, moe, multimodal, reasoning, scaling, mamba, hybrid]
---

# 大模型技术报告日报 — 2026-07-21

> 自动整理：各大 AI 公司最新大模型技术报告概览
> 关注方向：新架构（MoE/Mamba/hybrid）、训练方法、Scaling Law、多模态、长上下文、推理模型
> 数据更新：2026-07-21

---

## 1. DeepSeek

| 项目 | 详情 |
|------|------|
| 组织 | DeepSeek |
| 模型 | DeepSeek-V3, DeepSeek-R1, DeepSeek-V4-Pro (新) |
| 日期 | V3: 2024-12, R1: 2025-01, V4-Pro: 2026-04 |
| 参数 | V3: 671B 总参 / 37B 激活; V4-Pro: 未公开 (MoE + MLA 架构) |
| 核心创新 | Multi-head Latent Attention (MLA); DeepSeekMoE (256 专家/8 激活); FP8 低精度训练; Multi-Token Prediction (MTP); R1-Zero 纯 RL 无 SFT 自发涌现 CoT; V4-Pro: 原生多模态 (视觉+音频+视频) |
| 亮点 | V3 训练成本仅 $5.58M (2.788M GPU 小时 H800); R1-Zero 纯 RL 涌现 CoT; V4-Pro 支持 1M 上下文, 同步多模态输入输出; V3/R1 完全开源 (MIT 协议) |
| 链接 | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437), [arXiv:2501.12948 (R1)](https://arxiv.org/abs/2501.12948), [API 文档](https://api-docs.deepseek.com/news/tech_report_v3) |

**趋势关联**：DeepSeek 推动开源模型在推理能力上追赶闭源模型，MoE + RL 成为主流范式。V4-Pro 进入多模态竞争。

---

## 2. OpenAI

| 项目 | 详情 |
|------|------|
| 组织 | OpenAI |
| 模型 | GPT-5 (arXiv:2601.03267), GPT-5.5 "Ultra" (新), o3, o4-mini, Codex |
| 日期 | GPT-5: 2025-12, GPT-5.5 Ultra: 2026-04, o3/o4-mini: 2025-04, Codex: 2025-06 |
| 参数 | 未公开 |
| 核心创新 | GPT-5 System Card 安全评估框架; o3: 低至 0.1% 错误率 (FrontierMath); o3: 可视化推理 (测试时计算搜索 20,000 步); Codex: agentic coding 框架; GPT-5.5 Ultra: 更快响应速度 |
| 亮点 | o3 在 Codeforces 编程竞赛达 99.5th percentile; o3 首次实现 CLI 视觉推理; ARC-AGI-1 87.5%, ARC-AGI-2 >15%; GPT-5 System Card 是首个详尽 frontier model 安全评估文档 |
| 链接 | [arXiv:2601.03267 (GPT-5)](https://arxiv.org/abs/2601.03267), [o3 System Card](https://openai.com/index/o3-and-o4-mini-system-card/) |

**趋势关联**：OpenAI 强调 test-time compute scaling 和 agentic coding，GPT-5.5 Ultra 提升响应速度。

---

## 3. Meta AI

| 项目 | 详情 |
|------|------|
| 组织 | Meta (FAIR) |
| 模型 | Llama 4 Scout, Llama 4 Maverick, Llama 4 Behemoth (训练中) |
| 日期 | 2025-04 |
| 参数 | Scout: 109B 总参 / 17B 激活 (16 experts); Maverick: 400B 总参 / 17B 激活 (128 experts); Behemoth: ~2T 总参 / 288B 激活 (训练中) |
| 核心创新 | MoE 架构; 原生多模态 (早期融合, 文本+图像+视频+音频统一 tokenization); 超长上下文 (Scout 10M, Maverick 1M); iRoPE 位置编码; 在线知识蒸馏 (Behemoth→Scout/Maverick) |
| 亮点 | Scout 首个支持 10M 上下文的开源模型, NIAH 95%+; Maverick 128 专家 MoE; Behemoth (~2T) 目标最强开源模型; 训练稳定性关键挑战 (需 30 天连续训练) |
| 链接 | [llama.meta.com](https://llama.meta.com/) |

**趋势关联**：Meta 推动 MoE + 原生多模态 + 超长上下文，Llama 4 是首个支持 10M 上下文的开源模型。

---

## 4. Google DeepMind

| 项目 | 详情 |
|------|------|
| 组织 | Google DeepMind |
| 模型 | Gemini 2.5 Pro/Flash, Gemini 3.1 Pro (新) |
| 日期 | Gemini 2.5: 2025-06; Gemini 3.1 Pro: 2026-02 |
| 参数 | 未公开 |
| 核心创新 | MoE 架构; 原生多模态 (文本/图像/音频/视频); 原生工具调用; Thinking model 模式 (可调节思考预算); 长视频理解 (最高 3 小时); Gemini 3.1 Pro: 1M token 上下文, 77.1% ARC-AGI-2 |
| 亮点 | 1M token 上下文; 6/10 基准测试最佳; 3 小时长视频理解; Gemini 3.1 Pro 在 ARC-AGI-2 上达 77.1% (SOTA); 可调节思考预算 (low/medium/high) |
| 链接 | [arXiv:2507.06261](https://arxiv.org/abs/2507.06261), [Gemini 2.5 技术报告](https://arxiv.org/abs/2506.18628) |

**趋势关联**：Google 在多模态长上下文和推理能力上持续领先，Gemini 3.1 Pro 刷新 ARC-AGI-2 记录。

---

## 5. Anthropic

| 项目 | 详情 |
|------|------|
| 组织 | Anthropic |
| 模型 | Claude Opus 4, Claude Sonnet 4, Claude Opus 4.8 (新) |
| 日期 | Opus 4/Sonnet 4: 2025-05; Opus 4.8: 2026-05-28 |
| 参数 | 未公开 |
| 核心创新 | 混合推理架构 (extended thinking + 工具调用交替); 长上下文保持能力 (Sonnet 4 在 500K token 后性能 86%); 持久记忆; 并行 tool execution; ASL-3/ASL-2 安全等级; Opus 4.8: 1M 上下文窗口 |
| 亮点 | Opus 4.8 支持 1M 上下文, 数小时任务执行; 在 SWE-bench 和 TAU-bench 上领先; System Card 详尽披露能力边界; Sonnet 4 平衡性能与速度 |
| 链接 | [Anthropic System Card](https://www.anthropic.com/research/claude-opus-4-sonnet-4-system-card) |

**趋势关联**：Anthropic 强调 agentic 能力和长时间任务执行，混合推理架构成为趋势。

---

## 6. Mistral AI

| 项目 | 详情 |
|------|------|
| 组织 | Mistral AI |
| 模型 | Large 3, Ministral 3B/8B/14B, Magistral Medium (新), Devstral Small (新) |
| 日期 | Large 3: 2025-12; Magistral Medium: 2026-06-02; Devstral Small: 2026-06-10 |
| 参数 | Large 3: 675B 总参 / 41B 激活 (MoE); Ministral: Dense; Magistral Medium: 未公开; Devstral Small: 未公开 |
| 核心创新 | MoE 架构; Apache 2.0 开源; 40+ 种语言; 函数调用与结构化输出; 128K 上下文; 原生多模态; 原生 web 搜索; Magistral Medium: 推理模型 (1200 tokens/sec); Devstral Small: agentic coding |
| 亮点 | Large 3 是 Mistral 最大开源模型 (675B MoE); Magistral Medium 首个推理模型, 1200 tokens/sec; Devstral Small 专为 agentic coding 设计; Mistral Saba 优化中东语言; Le Chat 平台 |
| 链接 | [mistral.ai](https://mistral.ai/) |

**趋势关联**：Mistral 推出首个推理模型 Magistral Medium，代表欧洲开源力量在推理赛道的发力。

---

## 7. Qwen (阿里)

| 项目 | 详情 |
|------|------|
| 组织 | Alibaba (Qwen Team) |
| 模型 | Qwen3, Qwen3.5-ASR-Flash |
| 日期 | 2025-05 |
| 参数 | 0.6B ~ 235B (含 dense 和 MoE 变体); Qwen3-235B-A22B: 235B 总参 / 22B 激活 |
| 核心创新 | Thinking / Non-thinking 模式切换; MoE 架构; 119 种语言; QAT 量化 (2/4/8-bit); QLoRA 微调; 原生多模态 (视觉、音频、视频); Agent 能力 (工具调用、MCP); Qwen3.5-ASR-Flash: 语音识别 |
| 亮点 | Qwen3-235B-A22B 在 AIME'25, MATH-500, LiveCodeBench 与 DeepSeek-R1, o3-mini 相当; Qwen3-30B-A3B 性能超越 Qwen2.5-32B 且推理快 10 倍; Qwen3.5-ASR-Flash 支持实时语音识别 |
| 链接 | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388), [GitHub](https://github.com/QwenLM/Qwen3) |

**趋势关联**：Qwen3 是国内开源生态最活跃的模型系列，MoE + 多模态 + Agent 全覆盖。

---

## 8. 01.AI (李开复)

| 项目 | 详情 |
|------|------|
| 组织 | 01.AI |
| 模型 | Yi-Lightning, Yi-Lightning-Vision |
| 日期 | 2024-12 |
| 参数 | 未公开 (MoE 架构) |
| 核心创新 | MoE 架构; 多模态 (视觉+文本); Chatbot Arena 排名世界第六; 混合推理模型; RAISE 安全框架; Yi-Lightning-Vision: 200K 上下文, 3D MR 安全 |
| 亮点 | Yi-Lightning 在 Chatbot Arena 达到 #6; Yi-Vision 在 C-Eval 排名 #2; Yi-Lightning-Vision 支持复杂图表分析、OCR、视频理解; RAISE 安全框架覆盖幻觉检测和安全边界 |
| 链接 | [Yi-Lightning-Vision](https://platform.01.ai/blog?tag=18) |

**趋势关联**：01.AI 代表国内模型在竞技场上追赶前沿，MoE + 多模态 + 安全是核心策略。

---

## 9. Baichuan (百川)

| 项目 | 详情 |
|------|------|
| 组织 | Baichuan Inc. |
| 模型 | Baichuan-M4, Baichuan Omni-1.5 (新) |
| 日期 | M4: 2026-06; Omni-1.5: 2026-01 |
| 参数 | Omni-1.5: 273B 总参 / 8B 激活 (MoE, 64 experts) |
| 核心创新 | 多模态模型; 深度推理架构; 融合文本/图像/视频理解; 中文医疗领域优化; Omni-1.5: 语音+视觉+语言原生融合, 自适应感知, 无 ASR 前端 |
| 亮点 | M4 Medical Agent 幻觉率仅 3.3%; Omni-1.5 支持实时语音对话, 256K 上下文; Omni-1.5 在 LiveBench 上超越 Gemini 2.5 Pro; Omni-1.5 开源 (Apache 2.0) |
| 链接 | [arXiv:2606.12721](https://arxiv.org/abs/2606.12721), [arXiv:2501.15368 (Omni-1.5)](https://arxiv.org/abs/2501.15368) |

**趋势关联**：Baichuan 在医疗垂直领域和多模态原生融合上持续发力，Omni-1.5 代表国内开源多模态新高度。

---

## 10. Microsoft (Phi 系列)

| 项目 | 详情 |
|------|------|
| 组织 | Microsoft Research |
| 模型 | Phi-4 (14B), Phi-4-multimodal, Phi-4-reasoning, Phi-4-reasoning-vision-15B |
| 日期 | Phi-4: 2024-12; Phi-4-multimodal/reasoning: 2025-03 |
| 参数 | Phi-4: 14B (dense); Phi-4-reasoning-vision: 15B |
| 核心创新 | 小模型实现强推理; 多模态推理 (文本+图像); 开放权重; 基于 LLM 合成数据训练; 推理密集型任务专项优化; 1.5-bit / 2-bit / 4-bit 量化; Phi-4: 9.8T tokens 预训练 |
| 亮点 | Phi-4 (14B) 在推理和多模态任务上表现突出; 基于合成数据训练; 推理能力与更大模型相当; 设备端友好的量化方案; Phi-4-reasoning-vision: 15B 多模态推理 |
| 链接 | [arXiv:2412.08905 (Phi-4)](https://arxiv.org/abs/2412.08905), [arXiv:2603.16832](https://arxiv.org/abs/2603.16832), [HuggingFace](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B) |

**趋势关联**：Phi 系列持续证明 "小模型 + 大数据 + 推理蒸馏" 路线的可行性。

---

## 11. Apple

| 项目 | 详情 |
|------|------|
| 组织 | Apple |
| 模型 | Apple Intelligence Foundation Language Models 2025 |
| 日期 | 2025-07 |
| 参数 | 约 3B (设备端); PT-MoE (服务端) |
| 核心创新 | 本地化推理 (设备端); 2-bit / 4-bit / 1.5-bit 量化 (PT-QAT); MoE (服务端); 混合精度训练 (2.15:1 等比例); 知识蒸馏 (大模型→小模型); Swift 框架集成; Private Cloud Compute (PCC) |
| 亮点 | 设备端模型在 iPad Pro M4 上达 36 tok/s; 服务端模型 (PT-MoE) 在 LMSYS 排名 #5; Apple Intelligence 在 WWDC 2025 覆盖更多语言和设备; PT-QAT 2-bit 量化实现高效设备端部署 |
| 链接 | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575), [arXiv:2407.21075v2](https://arxiv.org/abs/2407.21075v2) |

**趋势关联**：Apple 强调隐私优先的本地推理，量化技术 + MoE 是其核心差异化。

---

## 12. NVIDIA

| 项目 | 详情 |
|------|------|
| 组织 | NVIDIA |
| 模型 | Nemotron 3 Ultra |
| 日期 | 2026-06 |
| 参数 | 550B 总参 (MoE hybrid Mamba-Attention); 55B 激活; 512 experts |
| 核心创新 | Mamba + Transformer hybrid 架构; 超长上下文 1M tokens; MoE 架构 (512 experts); 合成数据训练; 20T tokens 预训练; 支持 10M 上下文的长期路线图 |
| 亮点 | 550B 参数, 55B 激活; hybrid Mamba-Attention 架构为长上下文提供线性复杂度; 在多项 benchmark 上刷新记录; 专为工业部署优化 (制造、金融、医疗、零售) |
| 链接 | [arXiv:2512.17543](https://arxiv.org/abs/2512.17543), [Nemotron-3 Ultra Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-sets-new-standards-for-enterprise-ai-agents/) |

**趋势关联**：NVIDIA 强调 Mamba hybrid 架构和工业落地，hybrid Mamba-Attention 可能成为下一代长上下文主流。

---

## 13. xAI

| 项目 | 详情 |
|------|------|
| 组织 | xAI (Elon Musk) |
| 模型 | Grok 3, Grok 4 "Heavy" (新) |
| 日期 | Grok 3: 2025-02; Grok 4: 2026-07-07 |
| 参数 | Grok 3: 1.2T 总参 (128 experts MoE); Grok 4: 未公开 (推测 ~2T+, 56 experts) |
| 核心创新 | 大规模 MoE 架构 (128/56 experts); 基于大规模强化学习实现推理能力; 使用 Colossus 超算集群 (100K H100 GPU); 多模态 (文本+图像理解); Grok 4: 跨专家注意力门 (cross-expert attention gates) |
| 亮点 | Grok 3: AIME'24 79.5%, LiveCodeBench 65.0%; Grok 4 "Heavy": 首个 "thinking at inference" 推理模型; 4-8x 速度提升; 350B active parameters; Colossus 集群规模达 100K H100 GPU |
| 链接 | [xAI Grok 3](https://x.ai/blog/grok-3) |

**趋势关联**：xAI 通过大规模 RL 和超算集群追求推理能力，Grok 4 引入跨专家注意力门是架构创新。

---

## 14. Amazon (Nova)

| 项目 | 详情 |
|------|------|
| 组织 | Amazon Web Services (AWS) |
| 模型 | Amazon Nova (Micro, Lite, Pro, Canvas, Reel) |
| 日期 | 2024-12 |
| 参数 | Nova Micro: 未公开; Nova Pro: 未公开 |
| 核心创新 | 多模态 (文本/图像/视频/音频输入); 文本/图像/视频生成; 原生嵌入; 知识蒸馏; 基于自研 Trainium 芯片训练; 超长上下文 300K; 支持 200+ 语言; DPO/PPO 后训练 |
| 亮点 | Nova Pro 在图像理解/生成/视频理解任务上超越同级竞品; Nova Canvas (图像生成) 和 Nova Reel (视频生成) 达 SOTA; 使用知识蒸馏将大模型能力迁移至小模型; 基于 Trainium 芯片训练降低成本 |
| 链接 | [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |

**趋势关联**：Amazon 强调多模态全栈能力 (理解+生成) 和自研芯片生态。

---

## 15. Zhipu AI (智谱)

| 项目 | 详情 |
|------|------|
| 组织 | Zhipu AI (智谱 AI) |
| 模型 | GLM-5 |
| 日期 | 2025 (arXiv: 2602.15763) |
| 参数 | 未公开 |
| 核心创新 | Dynamic Sparse Attention (DSA); 异步强化学习训练框架 "Slime"; Agent Engineering; 深度推理与代码执行集成; 200K 上下文; "Vibe Coding to Agentic Engineering" |
| 亮点 | GLM-5 是智谱最新旗舰模型; DSA 提升长上下文效率; Async RL "Slime" 框架改善训练效率; 在多项基准上与 GPT-4o / Claude-3.5 相当; Agentic 设计支持工具调用和代码执行 |
| 链接 | [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |

**趋势关联**：智谱在注意力机制优化和 Agent 工程化上持续发力，DSA 是值得关注的架构创新。

---

## 16. InternLM (书生)

| 项目 | 详情 |
|------|------|
| 组织 | Shanghai AI Lab (上海 AI 实验室) |
| 模型 | InternLM3-8B, Intern-S1-Pro (新) |
| 日期 | InternLM3: 2025; Intern-S1-Pro: 2026-02 |
| 参数 | InternLM3: 8B; Intern-S1-Pro: 1T 总参 (512 experts, 8 active) |
| 核心创新 | 高训练效率 (4T tokens 达 20B 性能); 深度思考模式 (Deep Thinking Mode); 知识蒸馏; 推理增强; 3-stage RL 训练; Intern-S1-Pro: FoPE 位置编码, MoE 架构, 超长上下文 |
| 亮点 | InternLM3 仅使用 4T tokens 训练达 20B 模型性能; 4096 GPU 15 天完成训练; Intern-S1-Pro 1T 参数 MoE, 512 experts/8 active, 支持超长上下文; 支持 1M 上下文 |
| 链接 | [InternLM3 介绍](https://internlm.intern-ai.org.cn/en/blog/2025-01-22-InternLM3/) |

**趋势关联**：InternLM3 证明高效训练可能性，Intern-S1-Pro 进入万亿参数 MoE 竞赛。

---

## 17. Moonshot AI (月之暗面)

| 项目 | 详情 |
|------|------|
| 组织 | Moonshot AI (月之暗面) |
| 模型 | Kimi K2 |
| 日期 | 2025-07 |
| 参数 | 1.04T 总参 / 32B 激活 (MoE); 132T tokens 训练数据; 128 experts |
| 核心创新 | MoE 架构 (128 experts); MuonClip 优化器; 132T tokens 高质量数据训练; 原生 Agent 能力 (256+ 工具并行调用); 原生多模态 (视觉+音频+视频); 196K 上下文 |
| 亮点 | 1T 参数 MoE 模型 (开源); 首个支持 256+ 并行工具调用的 Agent 模型; MuonClip 优化器基于 Muon 但支持更高质量数据训练; 在 132T token 预训练中实现 99%+ 训练稳定性; MMLU 77.4, MATH-500 96.2 |
| 链接 | [Kimi K2](https://kimi.ai/blog/kimi-k2), [arXiv:2507.09816](https://arxiv.org/abs/2507.09816) |

**趋势关联**：Kimi K2 是目前最大的开源 MoE 模型之一，MuonClip 优化器和 Agent 能力是亮点。

---

## 18. StepFun (阶跃星辰)

| 项目 | 详情 |
|------|------|
| 组织 | StepFun (阶跃星辰) |
| 模型 | Step-3, Step 3.5 Flash, Step-DeepResearch |
| 日期 | Step-3: 2025-10; Step 3.5 Flash: 2026-01; Step-DeepResearch: 2025-12 |
| 参数 | Step-3: 528B 总参 / 45B 激活 (MoE); Step 3.5 Flash: 196B MoE; Step-DeepResearch: 32B |
| 核心创新 | 原生多模态推理 (Step-3 首创); 350 TPS 高速推理 (Step 3.5 Flash); Agent 深度研究能力; 端到端 RL 训练; 内生验证机制 (self-consistency 检测); 118B 训练数据 |
| 亮点 | Step-3 是首个原生多模态推理模型 (开源); Step 3.5 Flash 达 350 TPS; Step-DeepResearch 在 BrowseComp 上超越 o3/o4-mini/Gemini 2.5 Pro; 在 HLE 上超越 o3 和 Gemini 3; Step 3.5 Flash 开源 (Apache 2.0) |
| 链接 | [StepFun Blog](https://www.stepfun.com/blog/228834984796563456) |

**趋势关联**：Step-DeepResearch 代表 Agent + 推理模型融合的趋势，端到端 RL 训练 Agent 是新方向。

---

## 19. ByteDance (字节跳动)

| 项目 | 详情 |
|------|------|
| 组织 | ByteDance (字节跳动) |
| 模型 | Doubao Seed 2.0 Pro, Seed 2.0 Lite/Mini/Code, Game-TARS |
| 日期 | 2026-02-14 |
| 参数 | Pro: 未公开; Lite/Mini/Code: 未公开; Game-TARS: 500B tokens 训练 |
| 核心创新 | 分层训练策略 (核心能力分层优化); 多模态原生融合; 高效 RL 训练; Agent 能力; 代码/数学专项优化; 256K 上下文; Game-TARS: 自主游戏推理 |
| 亮点 | Seed 2.0 系列覆盖全场景 (旗舰/轻量/端侧/代码); 在编码和数学推理任务上表现突出; Game-TARS 500B tokens 训练超越 GPT-5; 字节跳动内部大规模部署验证 |
| 链接 | [arXiv:2602.16325](https://arxiv.org/abs/2602.16325) |

**趋势关联**：Seed 2.0 体现字节跳动在全场景模型布局上的策略，代码和数学成为重点优化方向。

---

## 综合趋势分析

### 1. 架构趋势：MoE 成为主流
所有 19 家公司中，**15+ 家采用或转向 MoE 架构**。代表性模型：
| 模型 | 总参 | 激活参 | 专家数 | 上下文 |
|------|------|--------|--------|--------|
| Grok 3 | 1.2T | - | 128 | - |
| Kimi K2 | 1.04T | 32B | 128 | 196K |
| Nemotron 3 Ultra | 550B | 55B | 512 | 1M |
| Mistral Large 3 | 675B | 41B | - | 128K |
| DeepSeek-V3 | 671B | 37B | 256 | 128K |
| Qwen3-235B-A22B | 235B | 22B | - | 128K |
| Llama 4 Maverick | 400B | 17B | 128 | 1M |

### 2. 推理能力：RL + Test-time Compute
推理模型成为 2025-2026 年最热门方向：
- **纯 RL 路线**：DeepSeek R1-Zero (无 SFT, 自发涌现 CoT), xAI Grok 3 (13.4T tokens RL)
- **混合推理**：Anthropic Claude Opus 4 (extended thinking + tools, ASL-3), OpenAI o3 (test-time compute 20K steps)
- **端到端 RL Agent**：Step-DeepResearch (BrowseComp 超越 o3), Qwen3 Thinking mode
- **异步 RL**：智谱 GLM-5 "Slime" 框架
- **首个推理模型**：Mistral Magistral Medium (1200 tokens/sec)

### 3. 多模态：原生融合成为标配
几乎所有新模型都支持多模态：
- **原生多模态** (早期融合): Llama 4 (文本+图像+视频+音频), Gemini 2.5 (3hr 视频), Kimi K2 (视觉+音频+视频), Qwen3 (119 语言), Baichuan Omni-1.5 (语音+视觉+语言)
- **后期融合**: GPT-5, Claude Opus 4
- **设备端多模态**: Apple AFM (3B), Phi-4-RV (15B)

### 4. 长上下文：从 128K 到 10M
- **10M tokens**: Llama 4 Scout (首个, NIAH 95%+)
- **1M tokens**: Gemini 2.5, Nemotron 3 Ultra, InternLM3, Claude Opus 4.8, DeepSeek V4-Pro
- **196K–300K**: Kimi K2 (196K), Amazon Nova (300K), Baichuan Omni-1.5 (256K)
- **128K–200K**: Qwen3, Mistral Large 3, GLM-5 (200K), ByteDance Seed 2.0 (256K)

### 5. 小模型逆袭
- Microsoft Phi-4 (14B): 推理能力与大模型相当, 9.8T tokens 预训练
- InternLM3-8B: 4T tokens 训练达到 20B 模型性能, 4096 GPU 15 天
- Apple 设备端 3B 模型: 36 tok/s on iPad Pro, PT-QAT 2-bit 量化
- Qwen3-30B-A3B: 超越 Qwen2.5-32B 且推理快 10 倍

### 6. Agent 化：从对话到自主执行
- Anthropic: 支持数小时持续任务, 并行 tool execution
- Kimi K2: 256+ 并行工具调用 (首个)
- Step-DeepResearch: 端到端 RL 训练 Agent, BrowseComp SOTA
- Baichuan-M4: 垂直领域 (医疗) Agent, 幻觉率 3.3%
- ByteDance Game-TARS: 500B tokens 训练超越 GPT-5

### 7. 训练效率创新
- DeepSeek V3: 2.788M GPU 小时 (H800), 成本约 $5.58M 训练 671B 模型
- InternLM3: 4T tokens 训练 8B 模型, 4096 GPU 15 天
- Apple: 2-bit 量化 (PT-QAT) 实现设备端 36 tok/s
- MuonClip 优化器 (Moonshot AI): 132T tokens 99%+ 训练稳定性
- NVIDIA Nemotron 3 Ultra: hybrid Mamba-Attention 降低长上下文计算复杂度

### 8. 安全与对齐
- Anthropic Claude Opus 4: ASL-3 安全等级, System Card 详尽披露
- OpenAI GPT-5: 首个详尽的 frontier model 安全评估文档 (arXiv:2601.03267)
- Apple AFM: 本地化推理保障隐私 (Private Cloud Compute)
- 01.AI RAISE: 安全框架覆盖幻觉检测和安全边界

---

> 本报告基于 2026-07-21 各公司公开技术报告、博客和论文整理。数据截至报告日期。
