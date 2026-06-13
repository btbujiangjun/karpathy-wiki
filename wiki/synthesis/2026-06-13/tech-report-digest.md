---
title: 大模型技术报告摘要（2025-2026）
type: synthesis
created: 2026-06-13
updated: 2026-06-13
tags: [tech-report, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, xai, apple, microsoft, nvidia, amazon, zhipu, internlm, moonshot, stepfun, bytedance, baichuan, yi]
sources: []
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告综合摘要。整理时间：2026-06-13。

---

## 1. DeepSeek

### DeepSeek-V3 技术报告
- **中文标题**：DeepSeek-V3 技术报告
- **英文标题**：DeepSeek-V3 Technical Report
- **发布机构**：DeepSeek-AI
- **模型名称**：DeepSeek-V3
- **发布日期**：2024-12-27
- **核心参数**：671B 总参数 / 37B 激活参数（MoE）；预训练数据 14.8T tokens；上下文长度 128K
- **主要创新**：
  - Multi-head Latent Attention (MLA) 实现高效推理
  - 辅助损失无负载均衡策略（auxiliary-loss-free load balancing）
  - Multi-Token Prediction (MTP) 训练目标
  - FP8 混合精度训练
  - 仅需 2.788M H800 GPU hours 完成全部训练
- **论文链接**：https://arxiv.org/abs/2412.19437

### DeepSeek-R1 技术报告
- **中文标题**：DeepSeek-R1：通过强化学习激励 LLM 推理能力
- **英文标题**：DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **发布机构**：DeepSeek-AI
- **模型名称**：DeepSeek-R1 / DeepSeek-R1-Zero
- **发布日期**：2025-01-20
- **核心参数**：基于 DeepSeek-V3-Base；纯 RL 训练（R1-Zero）；多阶段训练 pipeline
- **主要创新**：
  - 首次展示纯 RL（无 SFT）即可激发强推理能力
  - DeepSeek-R1-Zero：直接对 base model 应用 RL，涌现 Chain-of-Thought
  - DeepSeek-R1：冷启动数据 + 多阶段训练 pipeline
  - 将推理能力蒸馏到小模型
- **论文链接**：https://arxiv.org/abs/2501.12948

### DeepSeek-V3.2 技术报告
- **中文标题**：DeepSeek-V3.2：推动开源大模型前沿
- **英文标题**：DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models
- **发布机构**：DeepSeek-AI
- **模型名称**：DeepSeek-V3.2 / V3.2-Speciale
- **发布日期**：2025-12 (approx)
- **核心参数**：基于 V3 架构改进；Speciale 版本与 Gemini-3.0-Pro 性能持平
- **主要创新**：
  - DeepSeek Sparse Attention (DSA)：降低长上下文计算复杂度
  - 可扩展强化学习框架，达到 GPT-5 级别性能
  - 大规模 Agentic 任务合成 Pipeline
  - 在 IMO 2025、IOI 2025 获得金牌水平
- **论文链接**：https://arxiv.org/pdf/2512.02556

---

## 2. OpenAI

### GPT-5 System Card
- **中文标题**：GPT-5 系统卡
- **英文标题**：GPT-5 System Card
- **发布机构**：OpenAI
- **模型名称**：GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-thinking-pro)
- **发布日期**：2025-08-07
- **主要创新**：
  - 统一系统：fast model + deep reasoning model + 实时路由器自动选择
  - gpt-5-main（GPT-4o 的后继） + gpt-5-thinking（o3 的后继）
  - 幻觉率比 o3 降低约 6 倍
  - Safe-completions 安全训练方法
  - 写作、编码、健康三大场景大幅提升
- **论文链接**：https://arxiv.org/abs/2601.03267 / https://cdn.openai.com/gpt-5-system-card.pdf

---

## 3. Meta AI (LLaMA)

### Llama 4 技术报告
- **中文标题**：Llama 4 系列：架构、训练、评估与部署说明
- **英文标题**：The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes
- **发布机构**：Meta AI
- **模型名称**：Llama 4 Scout / Llama 4 Maverick / Llama 4 Behemoth
- **发布日期**：2025-04-05
- **核心参数**：
  - Scout: 17B 激活 / 109B 总参数 (16 experts)；10M 上下文；~40T tokens
  - Maverick: 17B 激活 / 400B 总参数 (128 experts)；1M 上下文；~22T tokens
  - Behemoth (teacher): 未公开参数，性能超 GPT-4.5 / Claude Sonnet 3.7
- **主要创新**：
  - 首批原生多模态开源 MoE 模型（early fusion）
  - Scout 支持 10M token 上下文（iRoPE 长度泛化）
  - 轻量级 SFT + 在线 RL + 轻量级 DPO 后训练
- **论文链接**：https://arxiv.org/abs/2601.11659（已撤稿，但技术内容可用）

---

## 4. Google DeepMind (Gemini)

### Gemini 3 技术报告 + 模型卡
- **中文标题**：Gemini 3 Pro 模型卡
- **英文标题**：Gemini 3 Pro Model Card
- **发布机构**：Google DeepMind
- **模型名称**：Gemini 3 Pro / Gemini 3.1 Pro / Gemini 3 Deep Think
- **发布日期**：2025-11-18 (Gemini 3); 2026-02-19 (Gemini 3.1 Pro); 2026-02-12 (Deep Think)
- **核心参数**：稀疏 MoE 架构（Sparse MoE Transformer）；原生多模态（text + image + audio + video）；2M 上下文窗口 (3.1 Pro)
- **主要创新**：
  - 原生多模态模型（预训练阶段即融合多模态）
  - Deep Think 模式：强化推理，IMO 2025 金牌水平
  - Extended-locality attention 支持 2M 上下文
  - 在 GPQA Diamond 达 94.3%（3.1 Pro）
- **模型卡链接**：https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf

---

## 5. Anthropic (Claude)

### Claude Opus 4 & Sonnet 4 System Card
- **中文标题**：Claude Opus 4 & Sonnet 4 系统卡
- **英文标题**：System Card: Claude Opus 4 & Claude Sonnet 4
- **发布机构**：Anthropic
- **模型名称**：Claude Opus 4 / Claude Sonnet 4
- **发布日期**：2025-05-22
- **核心参数**：Hybrid reasoning model（混合推理模型）；支持 extended thinking mode；Opus 4 在 ASL-3 标准下部署
- **主要创新**：
  - Hybrid reasoning：即时响应 + extended thinking 双模式
  - Opus 4 是 SWE-bench 最佳编码模型（72.5%）
  - 支持持续数小时的自主编码 Agent 工作流
  - 首次包含 alignment assessment 和 model welfare assessment
  - Thought summarization 机制（5% 长思维链被摘要）
- **论文链接**：https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf

---

## 6. Mistral AI

### Mistral Large 3 / Ministral 3
- **中文标题**：Mistral 3 模型家族技术文档
- **英文标题**：Mistral Large 3 Technical Documentation / Ministral 3 Technical Report
- **发布机构**：Mistral AI
- **模型名称**：Mistral Large 3 (MoE) / Ministral 3 (3B/8B/14B)
- **发布日期**：2025-12-02
- **核心参数**：
  - Mistral Large 3: 500B-1T 总参数 / 15B-50B 激活参数（MoE）
  - Ministral 3: 3B/8B/14B 稠密模型
  - 所有模型支持图像理解，Apache 2.0 许可
- **主要创新**：
  - Mistral 首个 MoE 模型（自 Mixtral 系列后）
  - Ministral 3 通过 Cascade Distillation（迭代剪枝 + 蒸馏）高效训练
  - 仅用 1-3T tokens 训练，通过蒸馏达到竞品水平
  - 上下文长度达 256K (128K for reasoning variants)
- **论文链接**：https://arxiv.org/pdf/2601.08584 (Ministral 3)

### Magistral (Mistral 推理模型)
- **中文标题**：Magistral：Mistral 的首个推理模型
- **英文标题**：Magistral
- **发布机构**：Mistral AI
- **模型名称**：Magistral Small / Magistral Medium
- **发布日期**：2025-06 (approx)
- **核心参数**：基于 Mistral Small 3 / Medium 3 的推理模型；纯 RL 训练
- **主要创新**：
  - 纯 RL 训练推理能力（无蒸馏）
  - RL on text 保持多模态、指令遵循、函数调用能力
  - Magistral Small 开源（Apache 2.0）
- **论文链接**：https://arxiv.org/pdf/2506.10910

---

## 7. Qwen (Alibaba)

### Qwen3 技术报告
- **中文标题**：Qwen3 技术报告
- **英文标题**：Qwen3 Technical Report
- **发布机构**：Alibaba (Qwen Team)
- **模型名称**：Qwen3 系列（0.6B-235B，含稠密和 MoE）
- **发布日期**：2025-05-14
- **核心参数**：
  - 旗舰模型 Qwen3-235B-A22B: 235B 总参数 / 22B 激活（MoE, 128 experts, 8 activated）
  - 预训练: 36T tokens, 119 种语言
  - 上下文: 128K（YaRN 扩展）
  - 稠密模型: 0.6B, 1.7B, 4B, 8B, 14B, 32B
- **主要创新**：
  - 统一 thinking / non-thinking 模式于同一模型
  - Thinking budget 机制：自适应分配推理计算量
  - 语言支持从 29 种扩展到 119 种
  - 所有模型 Apache 2.0 开源
- **论文链接**：https://arxiv.org/abs/2505.09388

---

## 8. Yi (01.AI)

### Yi-Lightning 技术报告
- **中文标题**：Yi-Lightning 技术报告
- **英文标题**：Yi-Lightning Technical Report
- **发布机构**：01.AI (零一万物)
- **模型名称**：Yi-Lightning
- **发布日期**：2024-12-02
- **核心参数**：MoE 架构；Chatbot Arena 第 6 名；中/数/编程/Hard 分类第 2-4 名
- **主要创新**：
  - 增强 MoE 架构：高级 expert 分割和路由
  - 优化的 KV-caching 技术
  - RAISE (Responsible AI Safety Engine) 安全框架
  - 多阶段训练 + 合成数据 + 奖励建模
- **论文链接**：https://arxiv.org/abs/2412.01253

---

## 9. Microsoft (Phi)

### Phi-4 技术报告
- **中文标题**：Phi-4 技术报告
- **英文标题**：Phi-4 Technical Report
- **发布机构**：Microsoft Research
- **模型名称**：Phi-4 (14B)
- **发布日期**：2024-12
- **核心参数**：14B 稠密 Transformer；合成数据为主训练
- **主要创新**：
  - 数据质量优先的训练策略
  - 合成数据贯穿训练全过程
  - 超越教师模型（GPT-4）的 STEM QA 能力
- **论文链接**：https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/

### Phi-4-reasoning 技术报告
- **中文标题**：Phi-4-reasoning 技术报告
- **英文标题**：Phi-4-reasoning Technical Report
- **发布机构**：Microsoft Research
- **模型名称**：Phi-4-reasoning / Phi-4-reasoning-plus (14B)
- **发布日期**：2025-04
- **核心参数**：14B 参数；SFT on "teachable" prompts + outcome-based RL
- **主要创新**：
  - 仅 14B 参数的推理模型，超越 DeepSeekR1-Distill-Llama-70B
  - 精心筛选的可教学提示训练集
  - RL 阶段进一步提升推理能力
- **论文链接**：https://arxiv.org/abs/2504.21318

### Phi-4-reasoning-vision 技术报告
- **中文标题**：Phi-4-reasoning-vision-15B 技术报告
- **英文标题**：Phi-4-reasoning-vision-15B Technical Report
- **发布机构**：Microsoft Research
- **模型名称**：Phi-4-reasoning-vision-15B
- **发布日期**：2026-03-04
- **核心参数**：15B 参数多模态推理模型
- **主要创新**：
  - 紧凑多模态推理模型，科学和数学推理表现优异
  - 混合推理/非推理数据 + 显式模式 token
  - 高分辨率动态分辨率编码器
  - 系统过滤、纠错、合成增强
- **论文链接**：https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/

---

## 10. Apple

### Apple Intelligence Foundation Language Models (2025)
- **中文标题**：Apple Intelligence 基础语言模型 2025 技术报告
- **英文标题**：Apple Intelligence Foundation Language Models Tech Report 2025
- **发布机构**：Apple
- **模型名称**：AFM on-device (~3B) / AFM server (PT-MoE)
- **发布日期**：2025-07-17
- **核心参数**：
  - 设备端: ~3B 参数稠密模型，KV-cache sharing + 2-bit QAT
  - 服务器端: Parallel-Track Mixture-of-Experts (PT-MoE)
- **主要创新**：
  - KV-cache sharing 和 2-bit 量化感知训练
  - PT-MoE：track parallelism + MoE + interleaved global-local attention
  - 异步 RL 训练平台
  - 多语言多模态 + 工具调用
- **论文链接**：https://arxiv.org/abs/2507.13575

### Apple Foundation Models 第三代 (AFM 3)
- **中文标题**：Apple 基础模型第三代
- **英文标题**：Third Generation of Apple's Foundation Models
- **发布机构**：Apple
- **模型名称**：AFM 3 Core (3B) / AFM 3 Core Advanced (20B sparse) / AFM 3 Cloud
- **发布日期**：2026-06-08
- **核心参数**：
  - AFM 3 Core Advanced: 20B 稀疏激活（1-4B per request）
  - Instruction-Following Pruning (IFP) 技术
- **主要创新**：
  - IFP 实现超稀疏架构，仅需少量 DRAM
  - AFM 3 Core Advanced 原生多模态
  - PT-MoE 架构持续演进
- **论文链接**：https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models

---

## 11. NVIDIA

### Nemotron 3 系列 (Nano / Super / Ultra / Omni)
- **中文标题**：Nemotron 3 系列技术报告
- **英文标题**：Nemotron 3 (Nano/Super/Ultra) Technical Reports
- **发布机构**：NVIDIA
- **模型名称**：Nemotron 3 Nano (30B-A3B) / Super (120B-A12B) / Ultra (550B-A55B) / Nano Omni
- **发布日期**：2025-12 起
- **核心参数**：
  - Nano: 30B 总 / 3B 激活 -> 实际为 31.6B-A3.2B
  - Super: 120B 总 / 12B 激活
  - Ultra: 550B 总 / 55B 激活
  - 全部为 Mamba-Attention Hybrid MoE
  - 预训练 20-25T tokens，支持 1M 上下文
- **主要创新**：
  - 首个 Mamba-Attention Hybrid MoE 模型系列
  - LatentMoE：新型 MoE 架构，优化 accuracy per FLOP
  - Multi-Token Prediction (MTP) + 原生推测解码
  - NVFP4 预训练
  - Nano Omni: 原生音频输入 + 多模态 token 缩减
- **论文链接**：
  - White Paper: https://research.nvidia.com/labs/nemotron/Nemotron-3/
  - Super: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf
  - Ultra: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf
  - Nano Omni: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf

---

## 12. xAI (Grok)

### Grok 3
- **中文标题**：Grok 3 Beta — 推理智能体时代
- **英文标题**：Grok 3 Beta — The Age of Reasoning Agents
- **发布机构**：xAI
- **模型名称**：Grok 3 / Grok 3 mini / Grok 3 DeepSearch
- **发布日期**：2025-02-19
- **核心参数**：Colossus 超算集群训练（10x 前代算力）；大规模 RL 训练推理能力
- **主要创新**：
  - 大规模 RL 实现推理能力（AIME 2025: 93.3%@cons64）
  - 实时 X 平台数据集成
  - Grok 3 mini 成本高效推理
  - Chatbot Arena Elo 1402
- **论文链接**：https://x.ai/news/grok-3

---

## 13. Amazon (Nova)

### Amazon Nova (2024) / Nova Premier (2025) / Nova 2 (2025)
- **中文标题**：Amazon Nova 模型家族技术报告
- **英文标题**：The Amazon Nova Family of Models / Amazon Nova Premier / Amazon Nova 2
- **发布机构**：Amazon (AGI)
- **模型名称**：Nova Micro / Lite / Pro / Canvas / Reel / Premier / Nova 2 Lite/Pro/Omni/Sonic
- **发布日期**：2024-12-03 (Nova); 2025-04-30 (Premier); 2025-12-02 (Nova 2)
- **核心参数**：
  - Nova Pro: 多模态（text/image/video/document），1M 上下文
  - Nova Premier: 最强大的多模态基础模型，1M 上下文
  - Nova 2: 支持 extended thinking 动态推理
- **主要创新**：
  - 全系列多模态模型覆盖（文本、图像、视频、音频）
  - Nova Premier 作为教师模型支持蒸馏
  - Nova 2 引入 extended thinking 动态推理
  - Nova 2 Omni: 统一多模态（text/image/video/audio 输入 + text/image 输出）
  - Nova 2 Sonic: 语音到语音基础模型
- **论文链接**：
  - Nova: https://arxiv.org/abs/2506.12103
  - Nova Premier: https://www.amazon.science/publications/amazon-nova-premier-technical-report-and-model-card
  - Nova 2: https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models

---

## 14. Zhipu AI (GLM)

### GLM-5 技术报告
- **中文标题**：GLM-5：从 Vibe Coding 到 Agentic Engineering
- **英文标题**：GLM-5: From Vibe Coding to Agentic Engineering
- **发布机构**：Zhipu AI & Tsinghua University
- **模型名称**：GLM-5 (744B-A40B) / GLM-5.1
- **发布日期**：2026-02-12
- **核心参数**：
  - 744B 总参数 / 40B 激活参数（MoE）
  - 预训练 28.5T tokens
  - 集成 DeepSeek Sparse Attention (DSA)
  - MIT 开源许可
- **主要创新**：
  - DSA 大幅降低部署成本，200K 上下文下注意力计算降 50%
  - Asynchronous RL infrastructure (slime)：解耦生成与训练
  - 异步 Agent RL 算法
  - 原生适配国产 GPU（华为昇腾、摩尔线程等）
  - CC-Bench-V2 逼近 Claude Opus 4.5
- **论文链接**：https://arxiv.org/abs/2602.15763

---

## 15. InternLM (Shanghai AI Lab)

### InternLM3
- **中文标题**：InternLM3-8B-Instruct
- **英文标题**：InternLM3-8B-Instruct
- **发布机构**：Shanghai AI Laboratory (上海人工智能实验室)
- **模型名称**：InternLM3-8B-Instruct
- **发布日期**：2025-01-15
- **核心参数**：8B 参数；仅 4T tokens 预训练（节省 75% 训练成本）
- **主要创新**：
  - 数据效率革命：IQPT (Intelligence Quality per Token) 指标
  - 4T tokens 达到其他模型 18T tokens 的性能
  - 首次在通用模型融合 deep thinking + 常规对话
  - 通过系统提示一键切换思考/非思考模式
- **论文链接**：https://internlm.readthedocs.io/en/latest/model_card/InternLM3.html

---

## 16. Moonshot AI (Kimi)

### Kimi K2 技术报告
- **中文标题**：Kimi K2：开放智能体智能
- **英文标题**：Kimi K2: Open Agentic Intelligence
- **发布机构**：Moonshot AI
- **模型名称**：Kimi K2 (1T-A32B MoE)
- **发布日期**：2025-07-28
- **核心参数**：
  - 1T 总参数 / 32B 激活参数（MoE, 384 experts, 8 activated）
  - MLA 注意力机制
  - 预训练 15.5T tokens，上下文 128K
  - MuonClip 优化器
- **主要创新**：
  - MuonClip: Muon + QK-Clip 稳定性增强
  - 零 loss spike 预训练
  - 大规模 agentic 数据合成 Pipeline
  - 联合 RL stage（真实 + 合成环境交互）
  - SWE-Bench Verified 65.8，Agent 能力开源最强
- **论文链接**：https://arxiv.org/abs/2507.20534

---

## 17. StepFun (阶跃星辰)

### Step-3 系统技术报告
- **中文标题**：Step-3：大而实惠的模型-系统协同设计
- **英文标题**：Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding
- **发布机构**：StepFun (阶跃星辰)
- **模型名称**：Step-3 (321B-A38B MoE)
- **发布日期**：2025-07-25
- **核心参数**：
  - 321B 总参数 / 38B 激活（MoE, 48 experts, 3 activated）
  - Multi-Matrix Factorization Attention (MFA)
  - 上下文 65K
- **主要创新**：
  - Multi-Matrix Factorization Attention (MFA) 降低 KV cache
  - Attention-FFN Disaggregation (AFD) 架构
  - 端到端多模态推理
- **论文链接**：https://arxiv.org/abs/2507.19427

### Step-DeepResearch 技术报告
- **中文标题**：Step-DeepResearch 技术报告
- **英文标题**：Step-DeepResearch Technical Report
- **发布机构**：StepFun (阶跃星辰)
- **模型名称**：Step-DeepResearch (32B)
- **发布日期**：2025-12-25
- **核心参数**：32B 参数；端到端 Deep Research agent
- **主要创新**：
  - 基于原子能力的数据合成策略（规划、搜索、反思、报告写作）
  - 渐进式训练：mid-training → SFT → RL
  - ADR-Bench 中文 Deep Research 基准
  - Scale AI ResearchRubrics 61.42，媲美 OpenAI DeepResearch
- **论文链接**：https://arxiv.org/abs/2512.20491

---

## 18. ByteDance (豆包/Doubao)

### Seed1.5-VL 技术报告
- **中文标题**：Seed1.5-VL 技术报告
- **英文标题**：Seed1.5-VL Technical Report
- **发布机构**：ByteDance Seed Team
- **模型名称**：Seed1.5-VL (Doubao 1.5 thinking vision pro)
- **发布日期**：2025-05-12
- **核心参数**：532M 视觉编码器 + 20B 激活参数 MoE LLM
- **主要创新**：
  - 38/60 公开 VLM 基准 SOTA
  - Agent 任务（GUI 控制、游戏）超 OpenAI CUA 和 Claude 3.7
  - 多模态推理（视觉谜题、OCR、3D 空间理解）
  - 已部署到豆包 App（doubao-1-5-thinking-vision-pro）
- **论文链接**：https://arxiv.org/abs/2505.07062

### Seed 2.0
- **中文标题**：Seed 2.0 系列
- **英文标题**：Seed 2.0 Series
- **发布机构**：ByteDance Seed Team
- **模型名称**：Seed 2.0 Pro / Lite / Mini / Code
- **发布日期**：2026-02-14
- **主要创新**：
  - 面向生产的大规模 Agent 部署
  - 多模态理解 + 推理能力增强
  - 长尾知识 + 复杂指令跟随
- **论文链接**：https://seed.bytedance.com/en/blog/seed-2-0-official-launch

---

## 19. Baichuan (百川智能)

### Baichuan-M1 / M2 / M3 / M4 (医疗垂直领域)
- **中文标题**：Baichuan 医疗大模型系列
- **英文标题**：Baichuan-M1/M2/M3/M4 Technical Reports
- **发布机构**：Baichuan Intelligence (百川智能)
- **模型名称**：Baichuan-M1 (14B) / M2 (32B) / M3 / M4
- **发布日期**：2025-02 起
- **核心参数**：
  - M1: 14B 参数，从头训练 20T tokens
  - M2: 32B 参数，多阶段 RL，HealthBench Hard >32（仅次于 GPT-5）
  - M3/M4: 临床级医疗 agent 系统
- **主要创新**：
  - 从零训练（非微调）医疗专用模型
  - M2: 动态验证框架 + Patient Simulator RL
  - M3: 临床工作流建模（主动信息采集、长程推理、幻觉抑制）
  - M4: 连续护理医疗 agent 系统（多工具协调、长期记忆）
- **论文链接**：
  - M1: https://arxiv.org/abs/2502.12671
  - M2: https://arxiv.org/abs/2509.02208
  - M3: https://arxiv.org/abs/2602.06570
  - M4: https://arxiv.org/abs/2606.08982

---

## 主题交叉分析

### 新架构趋势
- **MoE 成为主流**：几乎所有公司（DeepSeek, Meta, Qwen, Mistral, Kimi, StepFun, Zhipu, NVIDIA, Apple）均采用 MoE 架构
- **混合架构 (Hybrid)**：NVIDIA Nemotron 3 系列首创 Mamba-Attention Hybrid MoE
- **MLA (Multi-head Latent Attention)**：DeepSeek 首创，被 Kimi K2 等采用
- **DSA (DeepSeek Sparse Attention)**：被 Zhipu GLM-5 采用
- **MFA (Multi-Matrix Factorization Attention)**：Step-3 提出

### 训练方法
- **纯 RL 推理**：DeepSeek-R1-Zero 展示纯 RL 可激发推理；Magistral 也验证
- **Thinking/Non-thinking 统一模型**：Qwen3、InternLM3、Claude 4 均支持双模式
- **异步 RL 基础设施**：GLM-5 (slime)、Apple 都强调解耦生成与训练

### Scaling Law
- **数据效率革命**：InternLM3 仅用 4T tokens 达到竞品 18T 性能，提出 IQPT 指标
- **合成数据 Scaling**：Phi-4、GLM-5、Kimi K2 均大量使用合成数据

### 多模态
- **原生多模态**：Llama 4（early fusion）、Gemini 3、Apple AFM 3 均在预训练阶段融合视觉
- **全模态统一**：NVIDIA Nemotron 3 Nano Omni、Amazon Nova 2 Omni 支持 text/image/video/audio

### 长上下文
- Llama 4 Scout 达 **10M tokens**
- Gemini 3.1 Pro 达 **2M tokens**
- NVIDIA Nemotron 3 系列支持 **1M tokens**
- Amazon Nova 系列支持 **1M tokens**

### 推理模型
- OpenAI GPT-5 thinking (o3 successor)
- Anthropic Claude 4 hybrid reasoning
- DeepSeek R1 / V3.2 Speciale
- Mistral Magistral
- Microsoft Phi-4-reasoning / Phi-4-reasoning-vision
- Qwen3 thinking mode
- Step-3 multimodal reasoning
- Grok 3 reasoning agents
