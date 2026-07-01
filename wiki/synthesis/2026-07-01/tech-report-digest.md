---
title: 全球 AI 大模型技术报告摘要 (2026-07-01 全面更新)
type: synthesis
created: 2026-07-01
updated: 2026-07-01
sources: []
tags: [tech-report, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun, baichuan, yi]
---

# 全球 AI 大模型技术报告摘要

> 截至 2026 年 7 月，各主要 AI 公司最新技术报告/System Card 综合汇总。涵盖 22 家机构 40+ 报告。关注架构、训练方法、Scaling Law、多模态、长上下文、推理模型。

## 目录

1. [[#DeepSeek]]
2. [[#OpenAI]]
3. [[#Meta AI (LLaMA)]]
4. [[#Google DeepMind (Gemini)]]
5. [[#Anthropic (Claude)]]
6. [[#Mistral AI]]
7. [[#Qwen (Alibaba)]]
8. [[#Yi (01.AI)]]
9. [[#Baichuan]]
10. [[#Microsoft (Phi)]]
11. [[#Apple]]
12. [[#NVIDIA]]
13. [[#xAI (Grok)]]
14. [[#Amazon (Nova)]]
15. [[#Zhipu AI (GLM)]]
16. [[#InternLM (Shanghai AI Lab)]]
17. [[#Moonshot AI (Kimi)]]
18. [[#ByteDance (Doubao / Seed)]]
19. [[#StepFun (阶跃星辰)]]
20. [[#跨公司趋势总结]]

---

## DeepSeek

### DeepSeek-V4 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：面向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| **发布日期** | 2026 年 6 月 |
| **总参数量** | V4-Pro: 1.6T (49B activated); V4-Flash: 284B (13B activated) |
| **训练数据** | 32T+ tokens |
| **上下文长度** | 1,000,000 tokens |
| **架构** | MoE + 混合注意力 (CSA + HCA) + mHC + Muon optimizer |
| **arXiv** | https://arxiv.org/abs/2606.19348 |

**主要创新点：**
- **混合注意力架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 实现百万级高效上下文
- **Manifold-Constrained Hyper-Connections (mHC)**：改进残差连接
- **Muon optimizer**：加速收敛并提高训练稳定性
- 百万 token 上下文下，V4-Pro 仅需 V3.2 的 27% FLOPs 和 10% KV cache

### DeepSeek-V3.2 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3.2：推动开源大语言模型前沿 |
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V3.2 / V3.2-Speciale |
| **发布日期** | 2025 年 12 月 |
| **总参数量** | 685B MoE (基于 V3 架构) |
| **上下文长度** | 128K+ |
| **架构** | MoE + MLA + DSA (DeepSeek Sparse Attention) + MTP |
| **arXiv** | https://arxiv.org/abs/2512.02556 |

**主要创新点：**
- **DeepSeek Sparse Attention (DSA)**：细粒度稀疏注意力，大幅降低长上下文计算复杂度
- **可扩展 RL 框架**：V3.2 性能匹敌 GPT-5；Speciale 变体超越 GPT-5，与 Gemini-3.0-Pro 相当
- **IMO/IOI 金牌**：V3.2-Speciale 在 2025 年 IMO 和 IOI 中获得金牌
- **大规模 Agent 任务合成管线**：覆盖 1800+ 环境、85k+ 复杂指令

### DeepSeek-R1 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-R1：通过强化学习激励 LLM 推理能力 |
| **英文标题** | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-R1-Zero / DeepSeek-R1 |
| **发布日期** | 2025 年 1 月 |
| **总参数量** | 671B (37B activated) |
| **上下文长度** | 128K |
| **架构** | MoE (基于 DeepSeek-V3-Base) |
| **arXiv** | https://arxiv.org/abs/2501.12948 |

**主要创新点：**
- **纯 RL 推理**：R1-Zero 验证无需 SFT、仅通过 RL 即可涌现推理能力
- **多阶段训练**：冷启动数据 → 推理 RL → 拒绝采样 SFT → 全场景 RL
- 开源 6 个蒸馏密集模型 (1.5B–70B)
- 性能匹敌 OpenAI o1-1217

### DeepSeek-V3 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3 技术报告 |
| **英文标题** | DeepSeek-V3 Technical Report |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V3 |
| **发布日期** | 2024 年 12 月 |
| **总参数量** | 671B (37B activated) |
| **训练数据** | 14.8T tokens |
| **上下文长度** | 128K |
| **训练成本** | 2.788M H800 GPU hours |
| **架构** | MoE + MLA + MTP + 无辅助损失负载均衡 |
| **arXiv** | https://arxiv.org/abs/2412.19437 |

**主要创新点：**
- 开创无辅助损失负载均衡策略
- Multi-Token Prediction (MTP) 训练目标
- 整个训练过程零回滚

---

## OpenAI

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型系列** | gpt-5-main / gpt-5-main-mini / gpt-5-thinking / gpt-5-thinking-mini / gpt-5-thinking-nano / gpt-5-thinking-pro |
| **发布日期** | 2025 年 8 月 |
| **链接** | https://openai.com/index/gpt-5-system-card/ |
| **arXiv** | https://arxiv.org/abs/2601.03267 |

**主要创新点：**
- **统一系统 + 实时路由器**：根据对话类型智能选择快速模型或深度推理模型
- **推理能力大幅提升**：gpt-5-thinking 接替 o3，gpt-5-main 接替 GPT-4o
- **幻觉显著降低**、指令遵循改进、谄媚行为减少
- **Safe-Completions**：最新的安全训练方法
- 并行测试时计算 (Pro 模式)

### OpenAI o3 and o4-mini System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI o3 和 o4-mini 系统卡 |
| **英文标题** | OpenAI o3 and o4-mini System Card |
| **发布机构** | OpenAI |
| **模型系列** | o3 / o4-mini |
| **发布日期** | 2025 年 4 月 |
| **链接** | https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf |

**主要创新点：**
- 结合推理与完整工具能力 (Web 浏览、Python、图像分析、图像生成)
- 大规模 RL 训练思维链
- **Deliberative Alignment**：模型在上下文中推理安全策略
- 首个基于 Preparedness Framework v2 发布的系统卡

---

## Meta AI (LLaMA)

### Llama 4 Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 模型卡 |
| **英文标题** | Llama 4 Model Card |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout / Llama 4 Maverick |
| **发布日期** | 2025 年 4 月 5 日 |
| **参数量** | Scout: 17B-Act/109B-Total (16 experts); Maverick: 17B-Act/400B-Total (128 experts) |
| **训练数据** | Scout: ~40T tokens; Maverick: ~22T tokens |
| **上下文长度** | Scout: 10M; Maverick: 1M |
| **架构** | MoE + 早期融合原生多模态 |
| **许可证** | Llama 4 Community License |
| **链接** | https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md |

**主要创新点：**
- **原生多模态**：早期融合（early fusion）架构，文本+图像联合训练
- **Scout 10M 上下文**：使用 iRoPE 和长度泛化策略
- **Maverick 128 专家**：极致稀疏，17B 激活 400B 总参
- Scout 可在单张 H100 上通过 int4 量化部署
- 训练后：轻量 SFT + 在线 RL + 轻量 DPO

---

## Google DeepMind (Gemini)

### Gemini 2.5 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5：推动前沿的推理、多模态、长上下文与智能体能力 |
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 Pro / Gemini 2.5 Flash / Gemini 2.0 Flash / 2.0 Flash-Lite |
| **发布日期** | 2025 年 6 月 16 日 |
| **上下文长度** | 1M tokens (Pro) / 最高 2M |
| **模态** | 文本、音频、图像、视频（可处理 3 小时视频） |
| **arXiv** | https://arxiv.org/abs/2507.06261 |

**主要创新点：**
- **Thinking Model**：所有 Gemini 2.5 模型内置思维能力
- **SoTA 编程与推理**：Aider Polyglot、SWE-Bench Verified、AIME 2025 领先
- **长上下文 + 多模态 + 推理三位一体**解锁智能体工作流
- 3435 位作者的巨型技术报告
- 覆盖全部帕累托前沿（从 Pro 到 Flash-Lite）

---

## Anthropic (Claude)

### Claude Opus 4 & Sonnet 4 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4 和 Claude Sonnet 4 系统卡 |
| **英文标题** | System Card: Claude Opus 4 & Claude Sonnet 4 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4 / Claude Sonnet 4 |
| **发布日期** | 2025 年 5 月 |
| **链接** | https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf |

**主要创新点：**
- **Hybrid Reasoning**：混合推理大语言模型
- Opus 4 按 ASL-3 标准发布，Sonnet 4 按 ASL-2 标准
- 首次包含模型福利评估 (model welfare assessment)
- 显著改进的计算机使用 (computer use) 能力

### Claude Opus 4.5 / 4.6 / 4.7 / 4.8 系列

Anthropic 持续迭代 Claude 4 系列：
- **Opus 4.5** (2025.11) - 能力持续增强
- **Haiku 4.5** (2025.10)
- **Sonnet 4.5** (2025.09)
- **Opus 4.6** / **Sonnet 4.6** (2026.02)
- **Opus 4.7** (2026.04) - 重大软件工程改进
- **Opus 4.8** (2026.05)
- **Claude Fable 5 & Mythos 5** (2026.06) - 新一代旗舰

所有系统卡见: https://www.anthropic.com/system-cards

---

## Mistral AI

### Magistral Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Magistral：Mistral 的首个推理模型 |
| **英文标题** | Magistral |
| **发布机构** | Mistral AI |
| **模型系列** | Magistral Medium / Magistral Small |
| **发布日期** | 2025 年 6 月 12 日 |
| **架构** | 基于 Mistral Medium 3，纯 RL 训练推理能力 |
| **arXiv** | https://arxiv.org/abs/2506.10910 |

**主要创新点：**
- 从零构建纯 RL 推理管线，不依赖已有实现或蒸馏痕迹
- 纯 RL 训练保持甚至提升多模态理解、指令遵循和函数调用能力
- Magistral Small 开源 (Apache 2.0)

### Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 |
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 / Ministral 3 (3B/8B/14B) |
| **发布日期** | 2025 年 12 月 |
| **参数量** | Large 3: 675B total, 41B active (MoE); Ministral: 3B/8B/14B dense |
| **上下文长度** | 256K |
| **许可证** | Apache 2.0 |
| **链接** | https://mistral.ai/news/mistral-3/ |
| **arXiv (Ministral 3)** | https://arxiv.org/abs/2601.08584 |

**主要创新点：**
- Mistral 首个 MoE 模型 (自 Mixtral 系列以来)
- 多模态（图像理解）、多语言、强推理
- **Cascade Distillation**：迭代剪枝 + 蒸馏训练技术
- Ministral 3 支持 256K 上下文，全系列开源

---

## Qwen (Alibaba)

### Qwen3 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型系列** | Qwen3 Dense (0.6B–32B) + MoE (30B-A3B, 235B-A22B) |
| **发布日期** | 2025 年 4 月 29 日 (arXiv: 5 月 14 日) |
| **参数量** | 0.6B–235B (235B-A22B MoE 旗舰) |
| **训练数据** | 36T tokens |
| **上下文长度** | 支持 128K+ |
| **语言** | 119 种语言/方言 |
| **架构** | Dense + MoE，统一 thinking/non-thinking 模式 |
| **许可证** | Apache 2.0 |
| **arXiv** | https://arxiv.org/abs/2505.09388 |

**主要创新点：**
- **混合推理**：统一 thinking mode (深度推理) 和 non-thinking mode (快速响应) 于单一模型
- **Thinking Budget 机制**：用户可自适应分配推理计算资源
- **四阶段训练**：长 CoT 冷启动 → 推理 RL → 思维模式融合 → 通用 RL
- 参数范围从 0.6B 覆盖到 235B，适配从移动设备到云端
- 从 29 种语言扩展到 119 种语言

---

## Yi (01.AI)

### Yi-Lightning Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024 年 10 月 16 日 |
| **架构** | 增强 MoE + 高级专家分割和路由 + 优化 KV-cache |
| **Chatbot Arena** | 综合第 6 名；中文/数学/编程/困难提示第 2–4 名 |
| **arXiv** | https://arxiv.org/abs/2412.01253 |

**主要创新点：**
- 高效 MoE 架构，极低推理成本
- **RAISE** 安全框架 (四组件)
- 开源基础模型 Yi-34B / 6B / 9B (Apache 2.0)

注意：01.AI 近一年发布节奏放缓，后续未推出重大更新。2026 年已被 DeepSeek、Qwen、Kimi、GLM 等超越。

---

## Baichuan

### Baichuan4-Finance Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan4-Finance 技术报告 |
| **英文标题** | Baichuan4-Finance Technical Report |
| **发布机构** | Baichuan Inc. |
| **模型系列** | Baichuan4-Finance-Base / Baichuan4-Finance |
| **发布日期** | 2024 年 12 月 |
| **基础模型** | Baichuan4-Turbo |
| **架构** | Transformer，金融领域微调 |
| **arXiv** | https://arxiv.org/abs/2412.15270 |

**主要创新点：**
- 领域自约束训练策略（domain self-constraint），学习金融知识不损失通用能力
- 综合金融评测超越所有基线
- 持续预训练 → SFT → RLHF + AIF

---

## Microsoft (Phi)

### Phi-4-reasoning-vision-15B Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-reasoning-vision-15B |
| **发布日期** | 2026 年 3 月 |
| **参数量** | 15B (多模态推理) |
| **架构** | 基于 Phi-4 语言模型 + 动态分辨率视觉编码器 |
| **许可证** | 开源 (MIT) |
| **链接** | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

**主要创新点：**
- 混合推理/非推理数据 + 显式模式 Token
- 系统过滤、纠错和合成增强——数据质量是首要杠杆
- 在科学和数学推理、用户界面理解上表现出色
- 高分辨率动态分辨率编码器带来一致性改进

### Phi-4-reasoning Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-reasoning / Phi-4-reasoning-plus |
| **发布日期** | 2025 年 4 月 |
| **参数量** | 14B |
| **训练数据** | 140 万+ STEM 和编程问题 (SFT) |
| **架构** | 基于 Phi-4 的密集 Transformer + 结果导向 RL |
| **arXiv** | https://arxiv.org/abs/2504.21318 |

**主要创新点：**
- 超越 DeepSeek-R1-Distill-Llama-70B，接近完整 DeepSeek R1
- 推理改进非平凡地迁移到通用基准
- SFT + 短阶段 RL 增强

### Phi-4 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **英文标题** | Phi-4 Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 |
| **发布日期** | 2024 年 12 月 |
| **参数量** | 14B |
| **训练数据** | 合成数据为主 + 有机数据 |
| **架构** | 密集 Transformer (与 Phi-3 架构相同) |
| **arXiv** | https://arxiv.org/abs/2412.08905 |

**主要创新点：**
- 以数据质量为核心设计训练配方
- 超越教师模型 GPT-4 在 STEM QA 上的能力
- 多智能体提示、自我修正工作流、指令反转等数据合成技术

---

## Apple

### Apple Intelligence Foundation Language Models Tech Report 2025

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型 2025 技术报告 |
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **发布机构** | Apple |
| **模型系列** | ~3B On-Device Model + Server PT-MoE Model |
| **发布日期** | 2025 年 7 月 17 日 |
| **参数量** | On-Device: ~3B; Server: 大规模 PT-MoE |
| **架构** | On-Device: KV-cache sharing + 2-bit QAT; Server: Parallel-Track MoE (PT-MoE) + 交错全局-局部注意力 |
| **arXiv** | https://arxiv.org/abs/2507.13575 |

**主要创新点：**
- **KV-cache 共享** 和 **2-bit 量化感知训练** (设备端)
- **Parallel-Track MoE (PT-MoE)**：结合轨道并行、MoE 稀疏计算、交错全局-局部注意力
- 支持多语言、图像理解和工具调用
- Swift 为中心的 Foundation Models 框架，支持引导生成、约束工具调用、LoRA 微调
- 通过 Private Cloud Compute 保护隐私

---

## NVIDIA

### Nemotron 3 Ultra Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：用于智能体推理的高效开源 MoE 混合 Mamba-Transformer 模型 |
| **英文标题** | Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Ultra / Super / Nano |
| **发布日期** | 2026 年 |
| **参数量** | Ultra: 550B total, 55B active; Super: 120B total, 12B active; Nano: 30B total, 3B active |
| **训练数据** | Ultra: 20T tokens; Super/Nano: 25T tokens |
| **上下文长度** | 1M tokens |
| **架构** | MoE + Hybrid Mamba-Attention + LatentMoE + MTP + NVFP4 |
| **arXiv (Ultra)** | https://arxiv.org/abs/2606.15007 |
| **arXiv (Super)** | https://arxiv.org/abs/2604.12374 |

**主要创新点：**
- **混合 Mamba-Attention 架构**：显著降低注意力成本和 KV cache 占用
- Ultra 比 GLM-5.1/Kimi-K2.6/Qwen-3.5 推理吞吐量高 1.6–5.9 倍
- **LatentMoE**：每参数精度优于标准 Granular MoE
- **Multi-Token Prediction (MTP)**：通过推测解码加速推理
- **NVFP4 预训练**：低精度稳定训练
- 支持推理预算控制，适合长时间自主智能体任务

---

## xAI (Grok)

### Grok 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 3 |
| **英文标题** | Grok 3 Beta — The Age of Reasoning Agents |
| **发布机构** | xAI |
| **模型系列** | Grok 3 / Grok 3 mini / Grok 3 Think |
| **发布日期** | 2025 年 2 月 17 日 |
| **上下文长度** | 131K tokens |
| **架构** | 解码器 Transformer (参数未公开，估计 MoE 300B+ activated) |
| **训练** | Colossus 超算 (10 倍前代计算量) + 大规模 RL |
| **链接** | https://x.ai/news/grok-3 |

**主要创新点：**
- **大规模 RL 训练**：在预训练规模上应用 RL 开发思维链推理
- **Think Mode**：从数秒到数分钟的深度推理，纠错、回溯、多路径探索
- **DeepSearch**：迭代式 Web 搜索 + 分析
- Chatbot Arena Elo 1402，当时最高分
- 未发布正式技术报告 / 系统卡

---

## Amazon (Nova)

### Amazon Nova Family of Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族技术报告 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Pro / Nova Lite / Nova Micro / Nova Canvas / Nova Reel |
| **发布日期** | 2024 年 12 月 |
| **上下文长度** | 最高 1M (Premier) |
| **模态** | 文本、图像、视频、文档 |
| **arXiv** | https://arxiv.org/abs/2506.12103 |

### Amazon Nova Premier

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova Premier 技术报告 |
| **英文标题** | Amazon Nova Premier: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Premier |
| **发布日期** | 2025 年 4 月 30 日 |
| **上下文长度** | 1M tokens |
| **模态** | 文本、图像、视频 |
| **链接** | https://www.amazon.science/publications/amazon-nova-premier-technical-report-and-model-card |

### Amazon Nova 2

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **英文标题** | Amazon Nova 2: Multimodal Reasoning and Generation Models |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova 2 Lite / Pro / Omni / Sonic |
| **发布日期** | 2025 年 12 月 |
| **上下文长度** | 最高 1M |
| **链接** | https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models |

**主要创新点：**
- **Extended Thinking**：可配置的"扩展思考"控制，在准确率、速度、效率间平衡
- **Nova 2 Omni**：统一多模态模型，处理文本/图像/视频/音频输入，生成文本和图像
- **Nova 2 Sonic**：语音到语音基础模型

---

## Zhipu AI (GLM)

### GLM-5 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从氛围编程到智能体工程 |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-5 / GLM-5.1 / GLM-5.2 |
| **发布日期** | 2026 年 2 月 12 日 |
| **总参数量** | 744B total, 40B active (GLM-5); 较 GLM-4.5 (355B/32B) 大幅提升 |
| **训练数据** | 28.5T tokens (GLM-5); 27T (Base) |
| **上下文长度** | 200K |
| **架构** | MoE + DSA (DeepSeek Sparse Attention) |
| **许可证** | MIT License |
| **arXiv** | https://arxiv.org/abs/2602.15763 |

**主要创新点：**
- **DSA (DeepSeek Sparse Attention)**：大幅降低部署成本，保持长上下文质量
- **异步 RL 基础设施 "slime"**：解耦生成与训练，最大化 GPU 利用率
- **序列化 RL 管线**：推理 RL → Agent RL → 通用 RL，配合各阶段同策略蒸馏
- 在推理、编码、Agent 任务中达到开源模型最佳水平
- 面向复杂系统工程和长周期 Agent 任务

---

## InternLM (Shanghai AI Lab)

### InternLM3

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM3：4T 数据实现高性能 |
| **英文标题** | InternLM3: Achieving High-Performance Models with 4T Data |
| **发布机构** | Shanghai AI Lab |
| **模型系列** | InternLM3-8B-Instruct |
| **发布日期** | 2025 年 1 月 15 日 |
| **训练数据** | 4T tokens |
| **架构** | 密集 Transformer，融合深度推理和通用对话 |
| **链接** | https://github.com/InternLM/InternLM |

**主要创新点：**
- **数据效率革命**：4T 数据达到 18T 数据的性能，训练成本降低 75%+
- 首次在通用模型上融合深度推理和日常对话能力
- **世界知识树 (World Knowledge Tree)** 驱动的合成数据策略

### Intern-S1: Scientific Multimodal Foundation Model

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1：科学多模态基础模型 |
| **英文标题** | Intern-S1: A Scientific Multimodal Foundation Model |
| **发布机构** | Shanghai AI Lab |
| **参数量** | 241B total, 28B activated (MoE) |
| **训练数据** | 5T tokens 持续预训练 (2.5T+ 科学领域) |
| **发布日期** | 2025 年 8 月 |
| **架构** | MoE + Mixture-of-Rewards (MoR) |
| **arXiv** | https://arxiv.org/abs/2508.15763 |

**主要创新点：**
- 面向科学领域的专业通用模型 (Specializable Generalist)
- **Mixture-of-Rewards (MoR)**：在 1000+ 任务上协同 RL 训练
- 在分子合成规划、反应条件预测等专业科学任务上超越闭源 SOTA

---

## Moonshot AI (Kimi)

### Kimi K2 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放智能体智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **模型系列** | Kimi K2-Base / K2-Instruct |
| **发布日期** | 2025 年 7 月 28 日 |
| **总参数量** | 1T total, 32B activated (MoE) |
| **训练数据** | 15.5T tokens |
| **上下文长度** | 128K (后更新至 256K) |
| **架构** | MoE + MLA + MuonClip optimizer |
| **专家配置** | 384 experts, 8 selected per token, 1 shared expert |
| **arXiv** | https://arxiv.org/abs/2507.20534 |

**主要创新点：**
- **MuonClip 优化器**：改进 Muon 的 QK-clip 技术，解决训练不稳定
- 零损失尖峰完成 15.5T token 预训练
- SWE-Bench Verified 65.8, AIME 2025 49.5, GPQA-Diamond 75.1
- 在 Agent 任务中超越多数开源和闭源模型
- 大规模 Agent 数据合成管线 + 联合 RL 训练

### Kimi K1.5 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi k1.5：用 LLM 扩展强化学习 |
| **英文标题** | Kimi k1.5: Scaling Reinforcement Learning with LLMs |
| **发布机构** | Moonshot AI |
| **模型系列** | Kimi k1.5 (Long-CoT / Short-CoT) |
| **发布日期** | 2025 年 1 月 22 日 |
| **上下文长度** | 128K |
| **架构** | 多模态 LLM + RL (MoE 架构) |
| **arXiv** | https://arxiv.org/abs/2501.12599 |

**主要创新点：**
- **长上下文 RL 扩展**：将 RL 上下文窗口扩展到 128K，发现继续改进
- **简化框架**：无需 MCTS、价值函数、过程奖励模型
- **Long2Short**：用长 CoT 技术改进短 CoT 模型，短 CoT 性能超越 GPT-4o +550%
- 多模态（文本 + 视觉）联合训练

---

## ByteDance (Doubao / Seed)

### Seed 2.0 Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 2.0 模型卡：面向真实世界复杂性的智能前沿 |
| **英文标题** | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed2.0 Pro / Lite / Mini |
| **发布日期** | 2026 年 2 月 14 日 |
| **模态** | 语言 + 多模态 (视觉理解、空间推理) |
| **链接** | https://seed.bytedance.com/zh/seed2 |

**主要创新点：**
- 系统优化面向大规模生产部署
- 在长尾知识覆盖和长上下文稳定性上重点优化
- **Doubao** 和 **Trae** 产品部署反馈驱动优化
- Olympiad 级别数学推理达到金牌水平

### Seed-Thinking-v1.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed-Thinking v1.5 技术报告 |
| **英文标题** | Seed-Thinking-v1.5 Technical Details |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed-Thinking-v1.5 |
| **发布日期** | 2025 年 4 月 |
| **参数量** | 200B total, 20B active (MoE) |
| **链接** | https://github.com/ByteDance-Seed/Seed-Thinking-v1.5 |

**主要创新点：**
- 三重数据引擎：可验证数据 + 不可验证数据 + 新 Benchmark (BeyondAIME)
- 混合流编程模型 + 流推理系统 (SRS)
- 三层并行架构：张量/专家/序列并行 + 动态负载均衡

---

## StepFun (阶跃星辰)

### Step 3.5 Flash

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：快得足以思考，可靠得足以行动 |
| **英文标题** | Step 3.5 Flash: Fast Enough to Think. Reliable Enough to Act. |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step 3.5 Flash |
| **发布日期** | 2026 年 2 月 12 日 |
| **参数量** | 196B total, 11B activated (MoE) |
| **上下文长度** | 256K |
| **架构** | MoE + 3:1 Sliding Window Attention 混合 |
| **链接** | https://static.stepfun.com/blog/step-3.5-flash/ |

**主要创新点：**
- 极高"智能密度"：196B 参数但仅激活 11B/token
- **3:1 滑动窗口注意力 (SWA)**：3 层 SWA 对 1 层全注意力的混合
- 可在 Apple M4 Max 上本地运行
- 在设计上以推理成本和速度为核心约束

### Step3-VL-10B Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Step3-VL-10B 技术报告 |
| **英文标题** | Step3-VL-10B Technical Report |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step3-VL-10B |
| **发布日期** | 2026 年 1 月 |
| **参数量** | 10B |
| **训练数据** | 1.2T 多模态 tokens |
| **架构** | 语言对齐感知编码器 + Qwen3-8B 解码器 |
| **arXiv** | https://arxiv.org/abs/2601.09668 |

**主要创新点：**
- 10B 参数匹敌 10–20 倍大的模型 (如 GLM-4.6V-106B, Qwen3-VL-235B)
- **PaCoRe (Parallel Coordinated Reasoning)**：并行视觉探索聚合证据
- MMMU 80.11%, MathVision 75.95%, AIME2025 94.43% — 惊人推理性能

---

## 跨公司趋势总结

### 架构趋势

| 方向 | 代表模型 | 说明 |
|------|---------|------|
| **MoE 成为主流** | DeepSeek V3/V4, Qwen3, Llama 4, Kimi K2, GLM-5, Mistral Large 3, Nemotron 3 | 几乎所有前沿模型均采用 MoE |
| **混合架构 (Mamba + Attention)** | NVIDIA Nemotron 3 全系列 | State Space 模型与 Attention 结合，提升推理吞吐量 |
| **稀疏注意力** | DeepSeek DSA (V3.2/V4), Step 3.5 Flash SWA | 大幅降低长上下文计算成本 |
| **MLA (Multi-head Latent Attention)** | DeepSeek V3/V3.2, Kimi K2/K2.5 | 低 KV cache 高效推理 |

### 推理模型 (Reasoning) 趋势

| 方向 | 代表模型 | 说明 |
|------|---------|------|
| **纯 RL 推理** | DeepSeek-R1-Zero, Magistral | 无需 SFT，RL 原生涌现推理能力 |
| **混合推理/非推理模式** | Qwen3, GPT-5, Claude Opus 4/5, Kimi K2.5 | 单一模型切换思考/快速模式 |
| **大规模 RL 训练** | Kimi K1.5/K2, DeepSeek R1, Grok 3 | RL 成为推理能力核心训练方法 |
| **Thinking Budget** | Qwen3, Nemotron 3 | 用户控制推理时计算量 |

### 多模态趋势

| 方向 | 代表模型 | 说明 |
|------|---------|------|
| **原生多模态** | Llama 4, Gemini 2.5, Phi-4-reasoning-vision | 早期融合，联合训练 |
| **统一多模态推理** | Kimi K2.5, Nova 2 Omni, Step3-VL-10B | 一个模型处理文本/图像/视频/音频 |
| **多模态 Embedding** | Amazon Nova MME | 单一 embedding 模型支持 5 种模态 |

### 长上下文趋势

| 模型 | 上下文长度 | 技术 |
|------|-----------|------|
| Llama 4 Scout | 10M | iRoPE + 长度泛化 |
| DeepSeek V4 | 1M | CSA + HCA |
| Gemini 2.5 Pro | 1M | 未知 |
| Nemotron 3 | 1M | Hybrid Mamba |
| Kimi K2.5 | 256K | MLA |
| Step 3.5 Flash | 256K | SWA |
| GLM-5 | 200K | DSA |

### Scaling Law 新方向

1. **数据效率 Scaling**：InternLM3 用 4T 数据达到 18T 数据性能，打破传统 Scaling Law
2. **RL Scaling**：Kimi K1.5 证明上下文长度作为 RL 扩展的新维度
3. **Agent 推理 Scaling**：Nemotron 3 和 DeepSeek V3.2 将 Scaling 从纯推理扩展到 Agent 场景
4. **推理时计算 Scaling**：GPT-5 o3/pro、DeepSeek-V3.2-Speciale 展示推理时计算扩展效果
5. **蒸馏替代预训练**：Ministral 3 的 Cascade Distillation 证明蒸馏可以大幅降低预训练成本

> ⚠️ **注意**：本摘要持续更新中，部分模型的详细参数（如训练 FLOPs、精确架构）尚未公开披露。标注"未公开"的信息应视为估算。
