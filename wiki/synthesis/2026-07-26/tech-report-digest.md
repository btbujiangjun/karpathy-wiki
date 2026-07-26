---
title: "大模型技术报告摘要汇总 (2026年7月)"
type: synthesis
created: 2026-07-26
updated: 2026-07-26
sources: []
tags: [tech-report, LLM, MoE, reasoning, multimodal, long-context, RL]
---

# 大模型技术报告摘要汇总 (2026年7月)

> 本文汇总了截至 2026 年 7 月各大 AI 公司最新发布的大模型技术报告（Tech Report / Technical Report / System Card），涵盖架构创新、训练方法、Scaling Law、多模态、长上下文、推理模型等核心方向。

---

## 目录

1. [DeepSeek — V4 Series](#deepseek--v4-series)
2. [OpenAI — GPT-5.6 / GPT-5.5](#openai--gpt-56--gpt-55)
3. [Meta AI — LLaMA 4](#meta-ai--llama-4)
4. [Google DeepMind — Gemini 3 / 3.1 Pro / 3.6 Flash](#google-deepmind--gemini-3--31-pro--36-flash)
5. [Anthropic — Claude Opus 5 / Fable 5 / Mythos 5](#anthropic--claude-opus-5--fable-5--mythos-5)
6. [Mistral AI — Medium 3.5 / Small 4 / Leanstral 1.5](#mistral-ai--medium-35--small-4--leanstral-15)
7. [Qwen (Alibaba) — Qwen3.5-Omni / Qwen3.8 Max](#qwen-alibaba--qwen35-omni--qwen38-max)
8. [xAI — Grok 4.5 / Grok 4.20](#xai--grok-45--grok-420)
9. [Microsoft — Phi-4-reasoning-vision-15B](#microsoft--phi-4-reasoning-vision-15b)
10. [Apple — Apple Intelligence Foundation LM 2025](#apple--apple-intelligence-foundation-lm-2025)
11. [NVIDIA — Nemotron 3 Ultra / Super / Nano](#nvidia--nemotron-3-ultra--super--nano)
12. [Amazon — Nova Family / Nova Premier](#amazon--nova-family--nova-premier)
13. [智谱 AI (Zhipu AI) — GLM-5 / GLM-5.2](#智谱-ai-zhipu-ai--glm-5--glm52)
14. [InternLM (上海 AI Lab) — Intern-S1-Pro](#internlm-上海-ai-lab--intern-s1-pro)
15. [Moonshot AI — Kimi K3](#moonshot-ai--kimi-k3)
16. [阶跃星辰 (StepFun) — Step 3.5 Flash](#阶跃星辰-stepfun--step-35-flash)
17. [ByteDance — Seedance 2.0 / Seed3D 2.0](#bytedance--seedance-20--seed3d-20)
18. [01.AI — Yi-Lightning](#01ai--yi-lightning)
19. [百川 (Baichuan) — Baichuan-M3 / M4](#百川-baichuan--baichuan-m3--m4)

---

## DeepSeek — V4 Series

### DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型名称/系列** | DeepSeek-V4-Pro (1.6T/49B activated) / DeepSeek-V4-Flash (284B/13B activated) |
| **发布日期** | 2026-04-26 |
| **上下文长度** | 1,000,000 tokens (1M) |
| **最大输出** | 384K tokens |
| **训练数据** | Pro: 33T tokens / Flash: 32T tokens |
| **权重格式** | FP4 + FP8 Mixed |
| **许可证** | MIT |
| **论文链接** | https://arxiv.org/abs/2606.19348 |

**主要创新点：**
- **混合注意力架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)，交替使用实现百万 token 高效推理
- **Manifold-Constrained Hyper-Connections (mHC)**：升级传统残差连接，增强信号传播稳定性
- **Muon 优化器**：替代 AdamW，实现更快收敛和训练稳定性
- **FP4 量化感知训练**：MoE expert 权重和 indexer QK 路径使用 FP4 精度
- **推理效率**：在 1M token 上下文下，V4-Pro 仅需 V3.2 的 27% FLOPs 和 10% KV Cache
- **后训练范式**：两阶段——独立领域专家培养 + 统一模型 on-policy 蒸馏（GRPO + RL）
- **TileLang DSL**：平衡开发效率与运行时性能
- **Bitwise reproducibility**：跨训练和推理的确定性内核

---

## OpenAI — GPT-5.6 / GPT-5.5

### GPT-5.6 System Card

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡片 |
| **英文标题** | GPT-5.6 System Card |
| **发布机构** | OpenAI |
| **模型名称/系列** | GPT-5.6 Sol / Terra / Luna |
| **发布日期** | 2026-07-09 |
| **论文链接** | https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf |

**主要创新点：**
- **三模型家族**：Sol（旗舰）、Terra（高性价比）、Luna（最快最便宜）
- **安全框架**：Preparedness Framework 下 Cybersecurity 和 Biological/Chemical 均为 High 等级
- **推理能力**：支持 reasoning effort 控制，可调节思考深度
- **激活分类器**：新增针对敏感领域的实时激活分类器，在生成过程中干预
- **CoT 可控性**：CoT-Control 评估跟踪模型遵循用户 CoT 指令的能力
- **自动化安全系统**：跨对话扫描不安全模式
- **超过 70 万 A100e GPU 小时**用于自动寻找越狱方法

### GPT-5.5 System Card

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.5 系统卡片 |
| **英文标题** | GPT-5.5 System Card |
| **发布机构** | OpenAI |
| **模型名称/系列** | GPT-5.5 / GPT-5.5 Pro |
| **发布日期** | 2026-04-23 |
| **论文链接** | https://openai.com/index/gpt-5-5-system-card/ |

**主要创新点：**
- 为复杂现实世界工作设计（写代码、在线研究、分析信息、创建文档）
- 相比早期模型：更早理解任务、更少指导、更有效使用工具、自我检查并持续工作
- GPT-5.5 Pro 使用 parallel test time compute 设置
- Cybersecurity 和 Biological/Chemical 均为 High 等级

---

## Meta AI — LLaMA 4

### The Llama 4 Herd

| 字段 | 内容 |
|------|------|
| **中文标题** | Llama 4 系列模型 |
| **英文标题** | The Llama 4 Herd |
| **发布机构** | Meta AI |
| **模型名称/系列** | Llama 4 Scout (17B×16E=109B) / Llama 4 Maverick (17B×128E=400B) |
| **发布日期** | 2025-04-05 |
| **激活参数** | 17B (每 token) |
| **上下文长度** | Scout: 10M / Maverick: 1M |
| **训练数据** | Scout: ~40T tokens / Maverick: ~22T tokens |
| **论文链接** | https://ai.meta.com/blog/llama-4-multimodal-intelligence/ |

**主要创新点：**
- **首个 MoE 架构 LLaMA**：128 routed experts + 1 shared expert
- **原生多模态**：早期融合（early fusion）将文本和视觉 token 统一训练
- **iRoPE 架构**：交错注意力层（无位置编码）+ RoPE 层，实现无限上下文长度目标
- **MetaP 超参数设置**：可靠设置每层学习率和初始化尺度
- **FP8 精度训练**：32K GPU 训练 Behemoth 时达到 390 TFLOPs/GPU
- **200 种语言**：100+ 种语言各有 1B+ tokens
- **Llama 4 Behemoth**（预览）：尚未发布的教师模型，超过 GPT-4.5、Claude Sonnet 3.7、Gemini 2.0 Pro

---

## Google DeepMind — Gemini 3 / 3.1 Pro / 3.6 Flash

### Gemini 3 Pro / 3.1 Pro / 3.6 Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 3 系列模型 |
| **英文标题** | Gemini 3 Pro / 3.1 Pro / 3.6 Flash |
| **发布机构** | Google DeepMind |
| **模型名称/系列** | Gemini 3 Pro (Nov 2025), Gemini 3.1 Pro (Feb/Mar 2026), Gemini 3.6 Flash (Jul 2026) |
| **架构** | Sparse MoE Transformer，原生多模态 |
| **上下文长度** | 1M-2M tokens |
| **训练数据** | ~22T tokens |
| **论文链接** | https://deepmind.google/models/model-cards/gemini-3-pro/ |

**主要创新点：**
- **Deep Think 模式**：增强推理模式，在 Humanity's Last Exam (41.0%)、GPQA Diamond (93.8%)、ARC-AGI-2 (45.1%) 上突破
- **Gemini 3.1 Pro**：2M token 上下文窗口（是 GPT-5.5 和 Opus 4.7 的两倍），HLE 51.4%（Search+Code），ARC-AGI-2 77.1%
- **Extended-locality attention**：ring attention 变体，支持 2M 上下文
- **原生多模态**：文本、音频、图像、视频输入+输出
- **Frontier Safety Framework**：评估 CBRN、Cyber、Harmful Manipulation、ML R&D、Misalignment
- **Sycophancy 减少**、提示注入抵抗力增强

---

## Anthropic — Claude Opus 5 / Fable 5 / Mythos 5

### Claude Opus 5 System Card

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 系统卡片 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **模型名称/系列** | Claude Opus 5 |
| **发布日期** | 2026-07-24 |
| **论文链接** | https://www.anthropic.com/system-cards |

**主要创新点：**
- Opus 4.8 的升级版，在 agentic coding、computer use、long-horizon knowledge work 方面提升
- 数学和科学推理改进
- Responsible Scaling Policy v3.0/v3.1 框架下的评估

### Claude Fable 5 & Mythos 5 System Card

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5 和 Mythos 5 系统卡片 |
| **英文标题** | Claude Fable 5 & Claude Mythos 5 System Card |
| **发布机构** | Anthropic |
| **模型名称/系列** | Claude Fable 5（通用+安全护栏）/ Claude Mythos 5（能力前沿，有限访问） |
| **发布日期** | 2026-06-09 |
| **论文链接** | https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20&%20Claude%20Mythos%205%20System%20Card.pdf |

**主要创新点：**
- **同一模型权重两种配置**：Fable 5（通用访问+安全护栏）/ Mythos 5（仅限 Project Glasswing 受信任合作伙伴）
- Anthropic 训练过的**最强大模型**
- SOTA scores 在 agentic tasks、vision、life sciences research
- METR 外部测试评估
- 模型 welfare 评估——被认为是最"心理稳定"的模型

---

## Mistral AI — Medium 3.5 / Small 4 / Leanstral 1.5

### Mistral Medium 3.5 / Small 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Mistral Medium 3.5 和 Small 4 |
| **英文标题** | Mistral Medium 3.5 & Mistral Small 4 |
| **发布机构** | Mistral AI |
| **模型名称/系列** | Mistral Medium 3.5 / Mistral Small 4 |
| **发布日期** | 2026 (Medium 3.5: v26.04; Small 4: 26.03) |
| **上下文长度** | Small 4: 256K |

**主要创新点：**
- **Mistral Medium 3.5**：前沿级多模态模型，针对 agentic 和 coding 优化，支持 `reasoning_effort` 参数调节推理深度，MIT 改良许可开源
- **Mistral Small 4**：统一 instruct、reasoning 和 coding 的混合模型，256K 上下文
- **Leanstral 1.5**：119B 总参/6B 激活参，Apache 2.0，专为 Lean 4 形式验证设计
  - miniF2F 100% 饱和，PutnamBench 587/672，FATE-H 87%
  - 训练：mid-training → SFT → RL with CISPO
  - 发现 5 个之前未知的开源仓库 bug

---

## Qwen (Alibaba) — Qwen3.5-Omni / Qwen3.8 Max

### Qwen3.5-Omni Technical Report

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba Qwen Team |
| **模型名称/系列** | Qwen3.5-Omni-Plus / Flash |
| **发布日期** | 2026-04 |
| **参数规模** | 数千亿级 MoE |
| **上下文长度** | 256K |
| **训练数据** | 1 亿+ 小时音视频内容 |
| **论文链接** | https://arxiv.org/abs/2604.15804 |

**主要创新点：**
- **Hybrid Attention MoE 架构**：Thinker 和 Talker 均采用混合注意力 MoE
- **ARIA (Adaptive Rate Interleave Alignment)**：动态对齐文本和语音单元，解决流式语音合成不稳定问题
- **多语言**：113 种语言语音识别，36 种语音合成
- **Audio-Visual Vibe Coding**：从音视频指令直接生成可执行代码的涌现能力
- **Thinker-Talker 架构升级**：多码本编解码器实现单帧即时合成
- **215 个音频/音视频任务 SOTA**

### Qwen3.8 Max (Preview)

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.8 Max 旗舰模型预览版 |
| **发布机构** | Alibaba Qwen Team |
| **模型名称/系列** | Qwen3.8 Max |
| **发布日期** | 2026-07-19 |
| **参数规模** | 2.4T |

**主要创新点：**
- 仅次于 Claude Fable 5 的旗舰模型
- 计划开源权重

---

## xAI — Grok 4.5 / Grok 4.20

### Grok 4.5 Model Card

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.5 模型卡片 |
| **英文标题** | Grok 4.5 Model Card |
| **发布机构** | xAI (SpaceXAI) |
| **模型名称/系列** | Grok 4.5 |
| **发布日期** | 2026-07-14 |
| **训练截止** | 2026-01 |
| **论文链接** | https://media.x.ai/v1/website/card-7f81d41b.pdf |

**主要创新点：**
- xAI 最智能模型，专注于 coding、engineering、design 和 professional workflows
- 高度 agentic 和 reasoning-efficient，用更少步骤完成更大更难任务
- 使用 Cursor 工作流数据进行补充训练
- 通过 Cursor、OpenRouter、Vercel、Cloudflare 等平台分发

### Grok 4.20 System Card

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.20 系统卡片 |
| **发布机构** | xAI |
| **发布日期** | 2026-04-07 |

**主要创新点：**
- 支持 single-agent 和 multi-agent 两种模式
- Cybersecurity 和 CBRN 双重评估
- 发布时在 CBRN 方面接近前沿水平

---

## Microsoft — Phi-4-reasoning-vision-15B

### Phi-4-reasoning-vision-15B Technical Report

| 字段 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型名称/系列** | Phi-4-reasoning-vision-15B |
| **发布日期** | 2026-03-04 |
| **参数规模** | 15B |
| **训练数据** | 200B multimodal tokens (基于 Phi-4-Reasoning 16B tokens + Phi-4 400B unique tokens) |
| **论文链接** | https://arxiv.org/abs/2603.03975 |

**主要创新点：**
- **紧凑型多模态推理模型**：仅 15B 参数，远少于同级竞品的训练计算量
- **混合推理/非推理数据**：显式 mode tokens 使单一模型支持快速直接回答和 CoT 推理
- **数据质量为王**：系统过滤、错误纠正、合成增强
- **高分辨率动态分辨率编码器**：精确感知是高质量推理的前提
- **Pareto 最优**：在准确性和计算成本权衡上超越 10x+ 更大计算量的模型

---

## Apple — Apple Intelligence Foundation LM 2025

### Apple Intelligence Foundation Language Models Tech Report 2025

| 字段 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型技术报告 2025 |
| **英文标题** | Apple Intelligence Foundation Language Models Tech Report 2025 |
| **发布机构** | Apple |
| **模型名称/系列** | AFM-on-device (~3B) / AFM-server (PT-MoE) |
| **发布日期** | 2025-07-17 |
| **论文链接** | https://arxiv.org/abs/2507.13575 |

**主要创新点：**
- **Parallel-Track MoE (PT-MoE)**：轨道并行 + MoE 稀疏计算 + 交错全局-局部注意力
- **KV-cache 共享**：5:3 深度比两块设计，减少 37.5% KV cache
- **2-bit 量化感知训练 (QAT)**：on-device 模型压缩到 2 bits-per-weight
- **ASTC 压缩**：server 模型压缩到 3.56 bits-per-weight
- **LoRA 适配器**：运行时动态加载，rank 16 即可恢复精度
- **16 种语言**支持
- **Foundation Models 框架**：Swift 开发者可直接调用 on-device 模型
- **Private Cloud Compute**：隐私保护的服务器推理

---

## NVIDIA — Nemotron 3 Ultra / Super / Nano

### Nemotron 3 Ultra

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：开放高效 Mamba-Transformer 混合模型 |
| **英文标题** | Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型名称/系列** | Nemotron 3 Ultra 550B-A55B |
| **发布日期** | 2026-06-09 |
| **总参数** | 550B |
| **激活参数** | 55B |
| **训练数据** | 20T tokens |
| **上下文长度** | 1M tokens |
| **论文链接** | https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf |

**主要创新点：**
- **Hybrid Mamba-Attention MoE 架构**：Mamba-2 + GQA 交替 + MoE
- **LatentMoE**：优化每 FLOP 和每参数精度
- **Multi-Token Prediction (MTP)**：原生推测解码加速
- **NVFP4 预训练**：首次大规模 NVFP4 训练
- **Multi-teacher On-Policy Distillation (MOPD)**：多教师在线蒸馏
- **多环境 RLVR**：跨环境强化学习
- **Reasoning budget control**：可控推理预算
- **推理吞吐量**：比 GLM-5.1 高 5.9x，比 Kimi-K2.6 高 4.8x
- **开源**：Base、Post-trained、Quantized 权重 + 训练数据 + 配方

### Nemotron 3 Super (120B-A12B)

| 字段 | 内容 |
|------|------|
| **发布日期** | 2026-04-03 |
| **总参数** | 120B |
| **激活参数** | 12B |
| **训练数据** | 25T tokens |

**主要创新点：** 首个 LatentMoE + NVFP4 + MTP 的 Nemotron 模型，比 GPT-OSS-120B 高 2.2x 吞吐量

### Nemotron 3 Nano (30B-A3B)

| 字段 | 内容 |
|------|------|
| **总参数** | 31.6B |
| **激活参数** | 3.2B |
| **训练数据** | 25T tokens |

**主要创新点：** 比 Qwen3-30B-A3B 高 3.3x 吞吐量，128 专家选 6 个

---

## Amazon — Nova Family / Nova Premier

### Amazon Nova Family of Models

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族技术报告和模型卡片 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型名称/系列** | Nova Pro / Nova Lite / Nova Micro / Nova Canvas / Nova Reel |
| **发布日期** | 2024-12-03 (Nova), 2025-04-30 (Premier) |
| **论文链接** | https://arxiv.org/abs/2506.12103 |

### Amazon Nova Premier

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova Premier 技术报告 |
| **英文标题** | Amazon Nova Premier: Technical Report and Model Card |
| **发布日期** | 2025-04-30 |
| **上下文长度** | 1M tokens |

**主要创新点：**
- Nova Premier 是最强多模态基础模型，支持 1M token 上下文
- 可通过 Bedrock 创建 Nova Pro/Lite/Micro 的定制变体（蒸馏）
- 全面支持文本、图像、视频输入
- 集成安全措施和负责任 AI

---

## 智谱 AI (Zhipu AI) — GLM-5 / GLM-5.2

### GLM-5 技术报告

| 字段 | 内容 |
|------|------|
| **中文标题** | 智谱 GLM-5 技术报告 |
| **英文标题** | GLM-5 Technical Report |
| **发布机构** | 智谱 AI (Zhipu AI) |
| **模型名称/系列** | GLM-5 |
| **发布日期** | 2026-02-22 |
| **参数规模** | 744B (MoE) |
| **训练数据** | 28.5T tokens |
| **论文链接** | https://arxiv.org/abs/2602.15763 |

**主要创新点：**
- **DSA 稀疏注意力**：同 DeepSeek，动态分配注意力资源，KV Cache 降低 75%，推理速度提升 3x
- **异步强化学习基础设施**：生成与训练解耦，支持大规模 Agent 轨迹探索
- **异步 Agent RL 算法**：针对动态环境下的规划与自我纠错
- **Token-in-Token-out (TITO)**：替代 Text-in-Text-out，消除重 tokenization 偏差
- **DP 感知路由**：一致性哈希避免冗余预填充
- **国产芯片适配**：华为昇腾、摩尔线程、海光等 7 大平台
- **SWE-bench Verified 77.8%**：开源 SOTA
- **CC-Bench-V2**：自动化真实软件开发评测集

### GLM-5.2

| 字段 | 内容 |
|------|------|
| **中文标题** | 智谱 GLM-5.2 旗舰模型 |
| **发布机构** | 智谱 AI |
| **模型名称/系列** | GLM-5.2 |
| **发布日期** | 2026-07-02 |
| **参数规模** | 753B |
| **上下文长度** | 1M tokens (稳定) |
| **许可证** | MIT |

**主要创新点：**
- **首次实现 1M token 稳定上下文**
- **IndexShare 机制**：每 4 层稀疏注意力层复用索引器，降低 2.9x FLOPs
- **改进 MTP 层**：推测解码接受长度提升 20%
- **ZCode 3.0**：自研 Agent 内核，针对 GLM 深度优化

---

## InternLM (上海 AI Lab) — Intern-S1-Pro

### Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale

| 字段 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿参数科学多模态基础模型 |
| **英文标题** | Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale |
| **发布机构** | Shanghai AI Laboratory |
| **模型名称/系列** | Intern-S1-Pro |
| **发布日期** | 2026-03-26 |
| **参数规模** | 1T (MoE) |
| **训练数据** | 6T multimodal tokens (continual pre-training) |
| **论文链接** | https://arxiv.org/abs/2603.25040 |

**主要创新点：**
- **首个万亿参数科学多模态模型**
- **Group Routing 机制**：强制负载均衡下限，解决大规模 MoE 训练不稳定
- **梯度估计方案**：加速 router embedding 更新
- **XTuner + LMDeploy 协同**：万亿参数级高效 RL 训练
- **科学任务**：覆盖化学、材料、生命科学、地球科学等 100+ 专业任务
- **MMLU 93.1 / MMLU-Pro 86.6**：通用能力开源顶级

---

## Moonshot AI — Kimi K3

### Kimi K3

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K3 旗舰模型 |
| **英文标题** | Kimi K3 |
| **发布机构** | Moonshot AI |
| **模型名称/系列** | Kimi K3 |
| **发布日期** | 2026-07-16 |
| **参数规模** | 2.8T (896 experts, 16 active) |
| **上下文长度** | 1,048,576 tokens (1M) |
| **最大输出** | 1,048,576 tokens |
| **权重格式** | MXFP4 weights / MXFP8 activations (QAT) |

**主要创新点：**
- **Kimi Delta Attention (KDA)**：混合线性注意力机制，3/4 层使用线性注意力，1/4 层保留全注意力
- **Attention Residuals (AttnRes)**：跨深度选择性检索，替代标准残差连接
- **Stable LatentMoE**：896 routed experts，每 token 激活 16 个
- **Quantile Balancing**：基于路由器分数分位数的专家分配
- **Per-Head Muon**：每注意力头独立优化
- **Sigmoid Tanh Unit (SiTU)**：改进激活控制
- **Gated MLA**：改进注意力选择性
- **KDA prefill-cache support**：贡献给 vLLM 社区
- **推理控制**：`reasoning_effort` 参数支持 low/high/max
- **性能**：Artificial Analysis Intelligence Index 仅落后 Claude Fable 5 和 GPT-5.6 Sol

---

## 阶跃星辰 (StepFun) — Step 3.5 Flash

### Step 3.5 Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：开放前沿智能 |
| **英文标题** | Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters |
| **发布机构** | StepFun |
| **模型名称/系列** | Step 3.5 Flash |
| **发布日期** | 2026-02-11 |
| **总参数** | 196B |
| **激活参数** | 11B |
| **上下文长度** | 256K |
| **论文链接** | https://arxiv.org/abs/2602.10604 |

**主要创新点：**
- **极高智能密度**：196B 总参中仅激活 11B
- **3:1 Sliding Window/Full Attention 混合**：SWA 层 query head 从 64 增至 96
- **Head-wise Gated Attention**：输入依赖的注意力汇聚
- **Multi-Token Prediction (MTP-3)**：3 路推测解码，峰值 350 tok/s
- **可扩展 RL 框架**：整合可验证信号和偏好反馈，off-policy 训练稳定
- **IMO-AnswerBench 85.4%**、LiveCodeBench-v6 86.4%、SWE-bench Verified 74.4%
- **本地部署**：可在 Mac Studio M4 Max、NVIDIA DGX Spark 上运行

---

## ByteDance — Seedance 2.0 / Seed3D 2.0

### Seedance 2.0

| 字段 | 内容 |
|------|------|
| **中文标题** | Seedance 2.0：面向世界复杂性的视频生成 |
| **英文标题** | Seedance 2.0: Advancing Video Generation for World Complexity |
| **发布机构** | ByteDance Seed |
| **发布日期** | 2026-02 (中国发布)，2026-04-15 (论文) |
| **论文链接** | https://arxiv.org/abs/2604.14148 |

**主要创新点：**
- 原生多模态音视频生成模型
- T2V、I2V、R2V 任务全面领先
- 中多方言、戏曲、唱歌场景显著提升
- 音视频同步质量大幅提升

### Seed3D 2.0

| 字段 | 内容 |
|------|------|
| **发布日期** | 2026-04 |
| **研究方向** | 3D 内容生成 |

**主要创新点：**
- 粗到细两阶段管线：全局结构 → 高频细节恢复
- 统一 PBR 模型直接生成多视角 albedo 和 metallic-roughness maps
- MoE scaling + VLM 语义条件
- 场景布局规划、部件分解、免训练铰接生成
- 69.0%-89.9% 胜率 vs 5 个近期商业模型

---

## 01.AI — Yi-Lightning

### Yi-Lightning Technical Report

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型名称/系列** | Yi-Lightning |
| **发布日期** | 2024-12 |
| **论文链接** | https://arxiv.org/abs/2412.01253 |

**主要创新点：**
- Chatbot Arena 第 6 名，中文/数学/编码/Hard Prompts 类别 2-4 名
- 细粒度专家分割 + 平衡路由 + 跨层 KV cache 共享
- 多阶段训练策略：预训练 → SFT → 奖励建模 → RLHF
- RAISE (Responsible AI Safety Engine)：四组件安全框架
- 论文指出传统静态 benchmark 与真实人类偏好存在显著差距

---

## 百川 (Baichuan) — Baichuan-M3 / M4

### Baichuan-M3

| 字段 | 内容 |
|------|------|
| **中文标题** | 百川 M3：建模临床问诊实现可靠医疗决策 |
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | 百川智能 (Baichuan AI) |
| **模型名称/系列** | Baichuan-M3-235B |
| **发布日期** | 2026-02 |
| **论文链接** | https://arxiv.org/abs/2602.06570 |

**主要创新点：**
- **SPAR 算法**：Step-Penalized Advantage with Relative baseline，将临床流程解耦为四阶段独立奖励
- **Fact-Aware RL**：事实感知强化学习，在线幻觉检测 + 动态奖励聚合
- **三阶段多专家融合**：领域专项 RL → 离线蒸馏 → MOPD 在线优化
- **Gated Eagle3 投机解码**：96% 加速
- **W4 量化**：仅需 26% 显存
- **HealthBench 65.1**（超 GPT-5.2-High 63.3），HealthBench-Hard 44.4（超 GPT-5.2 42.0）
- **SCAN-bench 三维度榜首**：临床问诊 74.9、实验室检查 72.1、诊断 74.4
- 幻觉率 3.5%（低于 GPT-5.2）

### Baichuan-M4

| 字段 | 内容 |
|------|------|
| **中文标题** | 百川 M4：面向持续照护的临床级医疗 Agent 系统 |
| **英文标题** | Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care |
| **发布日期** | 2026-06 |
| **论文链接** | https://arxiv.org/abs/2606.08982 |

**主要创新点：**
- 从单轮问答升级为持续照护 Agent 系统
- **Baichuan-Harness**：统一运行时，协调 RL 训练与实际部署
- **SPAR++**：span-level 奖励建模 + 推理路径压缩 + 课程学习
- 临床工具层：患者记忆管理、循证检索、多模态医学感知
- 幻觉率 3.3%

---

## 技术趋势总结

### 1. 架构创新

| 趋势 | 代表模型 | 关键技术 |
|------|----------|----------|
| **MoE 成为主流** | DeepSeek-V4, Kimi K3, GLM-5.2, LLaMA 4, Step 3.5 Flash | 极稀疏激活 (1-5% 参数)，数百到近万专家 |
| **Hybrid Attention** | DeepSeek-V4 (CSA+HCA), Step 3.5 Flash (SWA:Full=3:1), Kimi K3 (KDA) | 混合线性/全注意力平衡效率与质量 |
| **Hybrid Mamba-Transformer** | NVIDIA Nemotron 3 系列 | Mamba-2 + GQA 交替，显著提升吞吐量 |
| **超长上下文** | DeepSeek-V4 (1M), Kimi K3 (1M), GLM-5.2 (1M), LLaMA 4 Scout (10M) | 各种压缩/稀疏/混合策略实现百万级上下文 |

### 2. 训练方法

| 趋势 | 代表模型 | 关键技术 |
|------|----------|----------|
| **RL 后训练多样化** | DeepSeek-V4 (GRPO), NVIDIA (MOPD+RLVR), 百川-M3 (Fact-Aware RL) | 多环境 RL、事实感知 RL、多教师蒸馏 |
| **Agent RL** | GLM-5 (异步 Agent RL), Step 3.5 Flash (可扩展 RL) | 面向真实世界 Agent 任务的强化学习 |
| **低精度训练** | NVIDIA (NVFP4), Kimi K3 (MXFP4 QAT) | 4-bit 级别预训练和推理 |
| **推理模式控制** | OpenAI GPT-5.6 (reasoning effort), Kimi K3 (reasoning_effort) | 可调节推理深度和预算 |

### 3. 推理模型 / Reasoning Model

| 模型 | 关键特征 |
|------|----------|
| GPT-5.6 Sol | 支持 reasoning effort 调节，CoT 可控性 |
| Claude Mythos 5 / Fable 5 | Anthropic 最强能力前沿 |
| Gemini 3.1 Pro Deep Think | HLE 51.4%, ARC-AGI-2 77.1% |
| Kimi K3 | 推理始终开启，reasoning_effort 控制 |
| Step 3.5 Flash | 11B 激活参数达到前沿推理水平 |

### 4. 多模态模型

| 模型 | 模态支持 | 关键创新 |
|------|----------|----------|
| Qwen3.5-Omni | 文本+图像+音频+音视频 | ARIA 对齐、Audio-Visual Vibe Coding |
| LLaMA 4 | 文本+图像（原生多模态） | Early fusion、iRoPE |
| Gemini 3.x | 文本+图像+音频+视频 | 原生多模态预训练 |
| Apple AFM | 文本+图像 | PT-MoE、Private Cloud Compute |

### 5. 开源 vs 闭源格局

- **MIT 开源**：DeepSeek-V4, GLM-5.2, Mistral Medium 3.5
- **Apache 2.0**：Leanstral 1.5
- **Llama License**：LLaMA 4
- **即将开源**：Qwen3.8 Max, Kimi K3 (计划 2026-07-27)
- **闭源前沿**：OpenAI GPT-5.6, Anthropic Claude 5 系列, Google Gemini 3.x

---

*本文档由自动化流程生成，数据截至 2026 年 7 月 26 日。*
