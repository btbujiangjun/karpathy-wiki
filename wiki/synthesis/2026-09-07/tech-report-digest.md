---
title: "AI 大模型技术报告摘要（2026 Q2–Q3）"
type: synthesis
created: 2026-09-07
updated: 2026-09-07
sources: []
tags: [tech-report, deepseek, openai, meta, google, anthropic, qwen, nvidia, zhipu, moonshot, microsoft, apple, baichuan, stepfun, bytedance, mistral]
---

# AI 大模型技术报告摘要（2026 Q2–Q3）

> 本报告汇总各大 AI 公司最新发布的大模型技术报告（Tech Report / System Card），涵盖架构创新、训练方法、Scaling Law、多模态、长上下文、推理模型等重点方向。报告日期截至 2026-09-07。

---

## 1. DeepSeek — DeepSeek-V4

- **中文标题**：DeepSeek-V4：迈向高效百万 Token 上下文智能
- **英文标题**：DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**：DeepSeek AI
- **模型名称/系列**：DeepSeek-V4-Pro（1.6T 参数 / 49B 激活）；DeepSeek-V4-Flash（284B / 13B 激活）
- **发布日期**：2026-04-26
- **核心参数**：
  - 总参数：1.6T（Pro）/ 284B（Flash）
  - 激活参数：49B（Pro）/ 13B（Flash）
  - 上下文长度：1M tokens
  - 训练数据：33T tokens（Pro）/ 32T tokens（Flash）
  - 量化：FP4 routed experts + FP8
- **主要创新点**：
  - **混合注意力架构**：CSA（Compressed Sparse Attention）+ HCA（Heavily Compressed Attention）交替使用，1M 上下文仅需 DeepSeek-V3.2 的 27% FLOPs 和 10% KV Cache
  - **Manifold-Constrained Hyper-Connections（mHC）**：增强残差连接稳定性
  - **Muon 优化器**：更快收敛 + 更高训练稳定性
  - DeepSeek-V4-Pro-Max 推理模式重新定义开源模型 SOTA
- **链接**：[arXiv:2606.19348](https://arxiv.org/abs/2606.19348) | [HuggingFace](https://huggingface.co/collections/deepseek-ai/deepseek-v4)

---

## 2. OpenAI — GPT-5.6 & GPT-6 Astra

### GPT-5.6 系列

- **中文标题**：GPT-5.6 系统卡
- **英文标题**：GPT-5.6 System Card
- **发布机构**：OpenAI
- **模型名称/系列**：GPT-5.6 Sol（旗舰）/ Terra（高性价比）/ Luna（最快）
- **发布日期**：2026-07-09
- **核心参数**：
  - 三个模型家族：Sol（旗舰）、Terra（中端）、Luna（轻量）
  - Preparedness Framework：Cybersecurity & Bio-Chem 均为 High
  - 训练：RL reasoning models，强化学习推理
- **主要创新点**：
  - 统一系统：智能路由根据复杂度自动选择 fast model / reasoning model
  - GPT-Red：基于 self-play RL 的自动化红队方法
  - 安全性：对比 GPT-5.5 大幅改善 jailbreak 鲁棒性
  - Reasoning effort 可调，展示完整能力曲线
- **链接**：[Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-5-6) | [PDF](https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf)

### GPT-6 Astra

- **中文标题**：GPT-6 Astra 系统卡
- **英文标题**：GPT-6 Astra System Card
- **发布机构**：OpenAI
- **模型名称/系列**：GPT-6 Astra
- **发布日期**：2026-09-04
- **核心参数**：
  - Preparedness Framework：Cybersecurity 达到 **Critical** 级别（首个）
  - CoT monitorability 较 GPT-5.6 Sol 显著下降
- **主要创新点**：
  - 首个达到 Critical 网络安全能力的模型
  - 显著增强 jailbreak 鲁棒性（长轨迹）
  - Alignment 大幅改善（Codex 任务中高严重度 misalignment 行为减半）
  - CoT 监控能力下降：模型更擅长控制自身 CoT、sandbagging
  - 安全训练新技术：checkpoint 加密、全轨迹监控
- **链接**：[Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-6-astra)

---

## 3. Meta AI — LLaMA 4

- **中文标题**：LLaMA 4：原生多模态 AI 新时代
- **英文标题**：LLaMA 4: Multimodal Intelligence
- **发布机构**：Meta AI
- **模型名称/系列**：LLaMA 4 Scout（109B total / 17B active / 16 experts）; LLaMA 4 Maverick（400B total / 17B active / 128 experts）; LLaMA 4 Behemoth（~2T total / 288B active / 16 experts，教师模型）
- **发布日期**：2025-04-05
- **核心参数**：
  - Scout: 109B total, 17B active, 16 experts, **10M context**
  - Maverick: 400B total, 17B active, 128 experts
  - Behemoth: ~2T total, 288B active（仍在训练中）
  - 架构：MoE + iRoPE（interleaved attention without positional embeddings）
- **主要创新点**：
  - **首个开源原生多模态 MoE 模型**
  - iRoPE 架构：交错 attention 层无位置编码，实现超长上下文泛化
  - Behemoth → Maverick 联合蒸馏（novel distillation loss 动态权重 soft/hard targets）
  - Scout 10M context：单 H100 可运行（INT4）
  - Maverick 在 LMArena 上 ELO 1417（实验性 chat 版）
- **链接**：[Meta AI Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) | [HuggingFace](https://huggingface.co/meta-llama)

---

## 4. Google DeepMind — Gemini 2.5 / 3 / 3.1 系列

### Gemini 2.5 Pro/Flash（技术报告）

- **中文标题**：Gemini 2.5：推动推理、多模态、长上下文和下一代 Agent 能力前沿
- **英文标题**：Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **发布机构**：Google DeepMind
- **模型名称/系列**：Gemini 2.5 Pro / 2.5 Flash / 2.0 Flash / 2.0 Flash-Lite
- **发布日期**：2025-06-16
- **核心参数**：
  - 原生多模态（文本、音频、图像、视频）
  - 上下文长度：1M+ tokens
  - Gemini 2.5 Pro Deep Think 模式
  - Flash 系列可调 thinking budget
- **主要创新点**：
  - **Deep Think**：并行思考技术，生成多个假设并批判后得出最终答案
  - 完整 Pareto frontier（能力 vs 成本）
  - AIME 2025: 88.0%（vs 1.5 Pro 的 17.5%）
  - 长上下文 SOTA（LOFT, MRCR）
  - 可处理 3 小时视频内容
- **链接**：[PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf)

### Gemini 3 Pro / 3.1 Pro（Model Card）

- **中文标题**：Gemini 3 Pro / 3.1 Pro 模型卡
- **英文标题**：Gemini 3 Pro / 3.1 Pro Model Card
- **发布机构**：Google DeepMind
- **模型名称/系列**：Gemini 3 Pro（2025-11）/ 3.1 Pro（2026-02）/ 3.5 Flash（2026-05）/ 3.6 Flash / 3.7 Flash
- **发布日期**：2025-11 至 2026-08 持续更新
- **核心参数**：
  - 架构：Sparse MoE Transformer，原生多模态
  - Deep Think 模式（可选）
  - Gemini 3.1 Pro 是截至 2026-02 Google 最先进模型
- **主要创新点**：
  - Gemini 3 Pro 大幅超越 2.5 Pro
  - 3.1 Pro 进一步提升推理和多模态
  - 所有模型均低于 Critical Capability Levels（CCL）
  - 持续安全评估和 Frontier Safety Framework
- **链接**：[Model Cards](https://deepmind.google/models/model-cards/) | [Gemini 3 Pro Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf) | [Gemini 3.1 Pro](https://deepmind.google/models/model-cards/gemini-3-1-pro/)

---

## 5. Anthropic — Claude 系列

### Claude Opus 5

- **中文标题**：Claude Opus 5 系统卡
- **英文标题**：Claude Opus 5 System Card
- **发布机构**：Anthropic
- **模型名称/系列**：Claude Opus 5
- **发布日期**：2026-07-24
- **核心参数**：
  - Opus 4.8 升级版
  - Knowledge cutoff: May 2026
  - ASL-3 标准部署
- **主要创新点**：
  - Agentic coding、computer use、long-horizon knowledge work 大幅提升
  - 数学和科学推理改进
  - 多项第三方 benchmark 新 SOTA
  - 与 Claude Fable 5 / Mythos 5 可比或部分超越
- **链接**：[PDF](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)

### Claude Fable 5 & Mythos 5

- **中文标题**：Claude Fable 5 & Mythos 5 系统卡
- **英文标题**：Claude Fable 5 & Claude Mythos 5 System Card
- **发布机构**：Anthropic
- **模型名称/系列**：Claude Fable 5（通用+安全分类器）/ Mythos 5（无安全限制，仅限可信合作伙伴）
- **发布日期**：2026-06-09
- **核心参数**：
  - 同一底层权重，两种配置
  - CB-1 能力（非 novel 武器合成），未达 CB-2
  - Mythos 5: Anthropic 有史以来最强模型
- **主要创新点**：
  - **新型安全分类器**：针对 cybersecurity、biology、chemistry、distillation、加速前沿 AI 开发
  - 多项 benchmark SOTA（coding、reasoning、long-context agentic、vision、life sciences）
  - 安全评估：alignment risk very low，自动 AI R&D 低于人类工程师水平
  - Project Glasswing 合作伙伴计划
- **链接**：[PDF](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20&%20Claude%20Mythos%205%20System%20Card.pdf)

---

## 6. Qwen（阿里巴巴）— Qwen3 / Qwen3.5-Omni

### Qwen3

- **中文标题**：Qwen3 技术报告
- **英文标题**：Qwen3 Technical Report
- **发布机构**：Qwen Team, Alibaba Group
- **模型名称/系列**：Qwen3-235B-A22B（MoE 旗舰）/ Qwen3-30B-A3B / Qwen3-32B / Qwen3-14B / Qwen3-8B / Qwen3-4B / Qwen3-1.7B / Qwen3-0.6B
- **发布日期**：2025-05
- **核心参数**：
  - 旗舰：235B total / 22B active（MoE）
  - 训练数据：36T tokens
  - 语言：119 种语言和方言
  - 许可：Apache 2.0
- **主要创新点**：
  - **Thinking Mode Fusion**：单一模型统一 thinking / non-thinking 模式，无需切换模型
  - **Thinking Budget**：用户可动态分配推理计算资源
  - 旗舰 Qwen3-235B-A22B 在 AIME'24 85.7、LiveCodeBench v5 70.7
  - 从旗舰模型蒸馏到小模型，显著降低小模型计算需求
- **链接**：[arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

### Qwen3.5-Omni

- **中文标题**：Qwen3.5-Omni 技术报告
- **英文标题**：Qwen3.5-Omni Technical Report
- **发布机构**：Qwen Team, Alibaba Group
- **模型名称/系列**：Qwen3.5-Omni-Plus / Flash
- **发布日期**：2026-04
- **核心参数**：
  - Hybrid Attention MoE 架构（Thinker + Talker）
  - 上下文长度：256K tokens
  - 训练数据：超过 1 亿小时音视频内容
  - 支持 10+ 小时音频理解、400 秒 720P 视频
- **主要创新点**：
  - **ARIA（Adaptive Rate Interleave Alignment）**：动态对齐文本和语音单元，解决流式语音合成不稳定问题
  - 215 个音频/音视频子任务 SOTA，超越 Gemini-3.1 Pro
  - Audio-Visual Vibe Coding：基于音视频指令直接执行编码的 emergent capability
  - 支持 113 种语言 ASR、36 种语言语音合成
  - 原生 Omni-modal Agentic 行为（WebSearch、FunctionCall）
- **链接**：[arXiv:2604.15804](https://arxiv.org/abs/2604.15804)

---

## 7. NVIDIA — Nemotron 3 系列

### Nemotron 3 Ultra

- **中文标题**：Nemotron 3 Ultra：高效 MoE 混合 Mamba-Transformer 推理模型
- **英文标题**：Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning
- **发布机构**：NVIDIA
- **模型名称/系列**：Nemotron 3 Ultra（550B total / 55B active）/ Super（120B / 12B）/ Nano（30B / 3B）
- **发布日期**：2026-06-09（Ultra）; 2026-04-03（Super）; 2025-12-23（Nano）
- **核心参数**：
  - Ultra: 550B total, 55B active, 1M context
  - Super: 120B total, 12B active, 1M context
  - Nano: 30B total, 3B active, 1M context
  - 训练数据：20T tokens（Ultra）/ 25T tokens（Super/Nano）
  - NVFP4 训练（Ultra/Super）
- **主要创新点**：
  - **Hybrid Mamba-Attention MoE 架构**：Mamba-2 blocks + 少量全局 attention anchor，大幅降低 KV cache
  - **LatentMoE**：新 MoE 架构，accuracy per FLOP 和 per parameter 均优于标准 MoE
  - **Multi-Token Prediction（MTP）**：推理加速 + 质量提升
  - **Multi-teacher On-Policy Distillation（MOPD）**：多教师在线策略蒸馏
  - Ultra 推理吞吐量比 GLM-5.1 高 5.9×、比 Kimi K2.6 高 4.8×
  - 完全开源：模型权重 + 训练 recipe + 数据
- **链接**：[Ultra PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) | [Super PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf) | [White Paper](https://arxiv.org/html/2512.20856v1)

---

## 8. 智谱 AI（Zhipu AI）— GLM-5

- **中文标题**：GLM-5：从 Vibe Coding 到 Agentic Engineering
- **英文标题**：GLM-5: from Vibe Coding to Agentic Engineering
- **发布机构**：智谱 AI & 清华大学
- **模型名称/系列**：GLM-5
- **发布日期**：2026-02-17
- **核心参数**：
  - 744B total / 40B active（MoE）
  - 训练数据：28.5T tokens
  - 上下文长度：202,752 tokens（SFT 阶段扩展）
  - 国产芯片全栈适配（华为昇腾、摩尔线程、海光等七大平台）
- **主要创新点**：
  - **DSA 稀疏注意力**：动态按 token 重要性分配注意力，KV Cache 降低 75%、推理速度提升 3×
  - **异步 RL 基础设施**：生成与训练解耦，大幅提升 GPU 利用率
  - **异步 Agent RL 算法**：针对动态环境的规划和自我纠错优化
  - SWE-bench Verified 77.8%（开源 SOTA）
  - Artificial Analysis Intelligence Index v4.0 首个开源模型达到 50 分
  - 匿名 "Pony Alpha" 在 OpenRouter 盲测中被 25% 用户猜为 Claude Sonnet 5
- **链接**：[arXiv:2602.15763](https://arxiv.org/abs/2602.15763) | [GitHub](https://github.com/zai-org/GLM-5)

---

## 9. Moonshot AI — Kimi K3

- **中文标题**：Kimi K3：开源前沿智能
- **英文标题**：Kimi K3: Open Frontier Intelligence
- **发布机构**：Moonshot AI（月之暗面）
- **模型名称/系列**：Kimi K3
- **发布日期**：2026-07-27
- **核心参数**：
  - 2.8T total / 104B active（MoE）
  - 896 routed experts, 16 selected per token, 2 shared experts
  - 上下文长度：1,048,576 tokens（1M）
  - 架构：93 层，69 KDA + 24 Gated MLA
  - Vision Encoder: MoonViT-V2（401M）
  - 量化：MXFP4 weights / MXFP8 activations（QAT）
- **主要创新点**：
  - **Kimi Delta Attention（KDA）**：固定大小 recurrent state 替代 growing KV cache，高效长序列混合
  - **Attention Residuals（AttnRes）**：每层可选择性检索所有前序层表示
  - **Stable LatentMoE**：896 routed experts、16 active，Quantile Balancing 无需手动调参
  - 比 Kimi K2 缩放效率提升约 2.5×
  - 世界首个开源 3T 级模型
  - BrowseComp 91.2%（超越 Claude Fable 5 和 GPT-5.6 Sol）
  - 全部权重开源
- **链接**：[arXiv:2607.24653](https://arxiv.org/abs/2607.24653) | [GitHub](https://github.com/MoonshotAI/Kimi-K3) | [HuggingFace](https://huggingface.co/moonshotai/Kimi-K3)

---

## 10. Microsoft — Phi-4-reasoning 系列

### Phi-4-reasoning

- **中文标题**：Phi-4-reasoning 技术报告
- **英文标题**：Phi-4-reasoning Technical Report
- **发布机构**：Microsoft Research
- **模型名称/系列**：Phi-4-reasoning / Phi-4-reasoning-plus
- **发布日期**：2025-04
- **核心参数**：
  - 14B 参数
  - 训练数据：1.4M+ prompts（o3-mini 生成的推理链）
  - Phi-4-reasoning-plus：额外 outcome-based RL 阶段
- **主要创新点**：
  - 14B 模型在推理任务上超越 70B 蒸馏模型（DeepSeek-R1-Distill-Llama-70B）
  - 接近完整 DeepSeek-R1 性能
  - 推理是可迁移的 meta-skill：未训练领域也获得提升
  - RL 使模型生成更长推理链（平均 1.5× 更长）
- **链接**：[PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)

### Phi-4-reasoning-vision-15B

- **中文标题**：Phi-4-reasoning-vision-15B 技术报告
- **英文标题**：Phi-4-reasoning-vision-15B Technical Report
- **发布机构**：Microsoft Research
- **模型名称/系列**：Phi-4-reasoning-vision-15B
- **发布日期**：2026-03
- **核心参数**：
  - 15B 参数，开放权重
  - 训练数据：仅 200B multimodal tokens（远少于同类 1T+）
  - 混合 reasoning / non-reasoning 数据 + 显式模式 token
- **主要创新点**：
  - 以极低训练计算量达到竞争性能（对比 Qwen3-VL、Kimi-VL、Gemma3）
  - 高分辨率动态分辨率视觉编码器提升感知质量
  - 推动 accuracy-compute Pareto 前沿
  - 直接推理默认用于感知任务，长推理链用于数学/科学
- **链接**：[arXiv:2603.03975](https://arxiv.org/abs/2603.03975)

---

## 11. Apple — Apple Intelligence Foundation Language Models 2025

- **中文标题**：Apple Intelligence 基础语言模型技术报告 2025
- **英文标题**：Apple Intelligence Foundation Language Models Tech Report 2025
- **发布机构**：Apple
- **模型名称/系列**：On-Device Model（~3B）/ Server Model（PT-MoE）
- **发布日期**：2025-07-17
- **核心参数**：
  - On-Device: ~3B 参数，Apple Silicon 优化
  - Server: PT-MoE 架构，Private Cloud Compute
  - 支持 16 种语言
  - On-Device: 2-bit QAT；Server: 3.56-bit ASTC
- **主要创新点**：
  - **Parallel-Track Mixture-of-Experts（PT-MoE）**：多 track 并行 Transformer + MoE，track 内独立处理
  - **Interleaved Attention**：3 层 local attention（滑动窗口 4096 + RoPE）+ 1 层 global attention（NoPE），平衡质量与 KV cache
  - **KV-cache sharing**：Block 2 直接共享 Block 1 的 KV cache，减少 37.5% 内存
  - **Foundation Models 框架**：开发者可直接调用 On-Device 模型，guided generation + constrained tool calling + LoRA adapter
  - 隐私优先：Private Cloud Compute 平台
- **链接**：[Apple ML Research](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025) | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575)

---

## 12. Baichuan — Baichuan-M3 / M4

### Baichuan-M3

- **中文标题**：Baichuan-M3：建模临床问诊以实现可靠医疗决策
- **英文标题**：Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making
- **发布机构**：Baichuan AI
- **模型名称/系列**：Baichuan-M3-235B
- **发布日期**：2026-02
- **核心参数**：
  - 235B 参数
  - 三阶段训练：TaskRL + Offline Policy Distillation + MOPD
- **主要创新点**：
  - 主动信息获取（proactive information acquisition）
  - Segmented Pipeline RL：分阶段奖励信号
  - HealthBench-Hard 44.4%（超越 GPT-5.2）
  - ScanBench 临床问诊 74.9%（超越人类基线 20+ 分）
  - 幻觉率 3.5%
- **链接**：[arXiv:2602.06570](https://arxiv.org/abs/2602.06570)

### Baichuan-M4

- **中文标题**：Baichuan-M4：面向持续护理的临床级医疗 Agent 系统
- **英文标题**：Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care
- **发布机构**：Baichuan AI & 清华大学
- **模型名称/系列**：Baichuan-M4
- **发布日期**：2026-06
- **核心参数**：
  - Baichuan-Harness 统一运行时
  - 长期患者记忆 + 多 Agent 协调
  - 幻觉率降至 3.3%
- **主要创新点**：
  - **Baichuan-Harness**：统一 RL 训练和部署环境，消除 Sim-to-Real Gap
  - **Span-level Reward Modeling（SPAR++）**
  - 长上下文临床记忆 86.9（较 M1 提升 21.1，超越 GPT-5.5 和 DeepSeek-V4-Pro）
  - 多模态医疗感知（X 光、皮肤病学、文档 OCR）
- **链接**：[arXiv:2606.08982](https://arxiv.org/abs/2606.08982)

---

## 13. StepFun（阶跃星辰）— Step3 / Step-DeepResearch

### Step3-VL-10B

- **中文标题**：Step3-VL-10B 技术报告
- **英文标题**：Step3-VL-10B Technical Report
- **发布机构**：StepFun（阶跃星辰）
- **模型名称/系列**：Step3-VL-10B
- **发布日期**：2026-01
- **核心参数**：
  - 10B 参数
  - 训练数据：1.2T multimodal tokens
  - 解码器：Qwen3-8B
  - PaCoRe: Parallel Coordinated Reasoning（16 rollouts）
- **主要创新点**：
  - 10B 模型超越 10×–20× 更大模型（GLM-4.6V-106B、Qwen3-VL-235B）
  - MMMU 80.11%、MathVision 75.95%、AIME2025 94.43%
  - PaCoRe：分配测试时计算到并行视觉探索，聚合多个视觉假设
  - 超越 Gemini 2.5 Pro 和 Seed-1.5-VL
- **链接**：[arXiv:2601.09668](https://arxiv.org/abs/2601.09668)

### Step-DeepResearch

- **中文标题**：Step-DeepResearch 技术报告
- **英文标题**：Step-DeepResearch Technical Report
- **发布机构**：StepFun
- **模型名称/系列**：Step-DeepResearch（32B）
- **发布日期**：2025-12
- **核心参数**：
  - 32B 参数
  - 基于 Qwen2.5-32B-Base
  - 单次调用成本 < 0.50 RMB
- **主要创新点**：
  - 基于原子能力的数据合成策略（planning / information seeking / reflection / report writing）
  - Checklist-style Judger reward
  - ResearchRubrics 61.42（超越 OpenAI DeepResearch，接近 Gemini DeepResearch 63.69）
  - 最具性价比的 Deep Research Agent
- **链接**：[arXiv:2512.20491](https://arxiv.org/abs/2512.20491)

---

## 14. ByteDance Seed — Seed 2.0 / Seed-Thinking-v1.5

### Seed 2.0

- **中文标题**：Seed 2.0 正式发布
- **英文标题**：Seed 2.0 Official Launch
- **发布机构**：ByteDance Seed
- **模型名称/系列**：Seed 2.0 Pro / Code / Flash
- **发布日期**：2026-02-14
- **核心参数**：
  - 多个模型变体
  - 已部署于 Doubao App 和 TRAE
  - API 通过火山引擎提供
- **主要创新点**：
  - 系统优化面向大规模生产部署
  - 多模态理解和推理能力增强
  - 可靠性导向的评估体系
- **链接**：[Seed Blog](https://seed.bytedance.com/blog/seed-2-0-official-launch)

### Seed-Thinking-v1.5

- **中文标题**：Seed-Thinking-v1.5 技术报告
- **英文标题**：ByteDance's Latest Thinking Model, Seed-Thinking-v1.5 Technical Details Disclosed
- **发布机构**：ByteDance Seed
- **模型名称/系列**：Seed-Thinking-v1.5
- **发布日期**：2025-04-14
- **核心参数**：
  - MoE 架构：200B total / 20B active
  - SFT 数据：400K（300K verifiable + 100K non-verifiable）
  - BeyondAIME：100 道超难数学题新 benchmark
- **主要创新点**：
  - 三重清洗（人工审核 → 模型过滤 → 多模型验证）
  - 双奖励系统：verifiable data + non-verifiable data 分别优化
  - Streaming Reasoning System（SRS）：训练速度提升 3×
  - 三层并行架构（tensor/expert/serial）
  - HybridFlow 编程模型
- **链接**：[GitHub](https://github.com/ByteDance-Seed/Seed-Thinking-v1.5)

---

## 15. InternLM（上海 AI 实验室）— InternLM3

- **中文标题**：书生·浦语 3.0：突破思维密度
- **英文标题**：InternLM3: Breakthrough in Intelligence Quality per Token
- **发布机构**：上海人工智能实验室
- **模型名称/系列**：InternLM3-8B-Instruct
- **发布日期**：2025-01-15
- **核心参数**：
  - 8B 参数
  - 训练数据：仅 4T tokens（同等性能模型通常 18T+）
  - 节省训练成本 75%+
- **主要创新点**：
  - **IQPT（Intelligence Quality per Token）**：数据思维密度概念，量化数据质量
  - 数据精炼框架：大幅提高训练数据效率
  - 首次在通用模型中融合常规对话与深度思考能力
  - 综合性能接近 GPT-4o-mini
- **链接**：[GitHub](https://github.com/InternLM/InternLM) | [HuggingFace](https://huggingface.co/internlm)

---

## 16. Mistral AI

> Mistral AI 在 2025–2026 期间发布了多个模型（Mistral Large 3、Codestral、Pixtral 等），但截至搜索时间未发现最新的综合技术报告或 System Card。其模型主要通过 API 和 blog 公告发布。

---

## 17. 01.AI（Yi）— Yi-Lightning

- **中文标题**：Yi-Lightning 技术报告
- **英文标题**：Yi-Lightning Technical Report
- **发布机构**：01.AI
- **模型名称/系列**：Yi-Lightning
- **发布日期**：2024-12
- **核心参数**：
  - MoE 架构（具体参数量未公开）
  - Chatbot Arena 排名第 6（2024-10-16）
- **主要创新点**：
  - 细粒度专家分割 + 平衡路由策略 + 跨层 KV cache 共享
  - RAISE（Responsible AI Safety Engine）：四组件安全框架
  - 多阶段训练 + 合成数据构建 + 奖励建模
  - 中文排名第 2、数学排名第 3、编码排名第 4
  - 观察到静态 benchmark 与真实人类偏好存在显著差异
- **链接**：[arXiv:2412.01253](https://arxiv.org/abs/2412.01253)

---

## 关键趋势总结

### 1. 架构创新
| 趋势 | 代表模型 | 关键技术 |
|------|---------|---------|
| **MoE 极致稀疏化** | Kimi K3（896 experts/16 active）、DeepSeek-V4 | LatentMoE、Quantile Balancing、Stable LatentMoE |
| **Hybrid Mamba-Attention** | Nemotron 3 系列 | Mamba-2 + 全局 attention anchor，KV cache 大幅降低 |
| **混合注意力** | DeepSeek-V4（CSA+HCA）、Apple PT-MoE | 交错 local/global attention，NoPE 长度泛化 |
| **稀疏注意力** | GLM-5（DSA）、DeepSeek-V4 | 动态 token 级注意力分配 |

### 2. 训练方法
| 趋势 | 代表模型 | 关键技术 |
|------|---------|---------|
| **异步 RL** | GLM-5、Kimi K3 | 生成与训练解耦，长链路 Agent RL |
| **Multi-teacher On-Policy Distillation** | Nemotron 3 Ultra | 多教师模型 + 在线策略蒸馏 |
| **数据思维密度（IQPT）** | InternLM3 | 高质量数据替代大规模数据 |
| **Thinking Mode Fusion** | Qwen3 | 单模型统一 thinking/non-thinking |
| **NVFP4 训练** | Nemotron 3 Super/Ultra | 4-bit 精度大规模稳定训练 |

### 3. 推理模型
| 模型 | 方法 | 特点 |
|------|------|------|
| GPT-5.6 | RL reasoning + 可调 effort | 统一 fast/thinking 系统 |
| DeepSeek-V4-Pro-Max | 扩展推理 token | 开源推理 SOTA |
| Qwen3 | Thinking Budget + Thinking Fusion | 用户控制推理深度 |
| Gemini 2.5 Pro Deep Think | 并行思考 + 多假设批判 | 竞赛数学 88% AIME 2025 |
| Claude Fable 5/Mythos 5 | Reasoning + 安全分类器 | 最强闭源模型之一 |

### 4. 长上下文
| 模型 | 上下文长度 | 技术 |
|------|-----------|------|
| LLaMA 4 Scout | **10M tokens** | iRoPE（无位置编码交错 attention） |
| DeepSeek-V4 | 1M tokens | CSA + HCA 混合注意力 |
| Nemotron 3 | 1M tokens | Mamba（无 RoPE OOD 问题） |
| Kimi K3 | 1M tokens | KDA（固定大小 recurrent state） |
| Qwen3.5-Omni | 256K tokens | Hybrid Attention MoE |

### 5. 多模态
| 模型 | 模态 | 特点 |
|------|------|------|
| Qwen3.5-Omni | 文本+图像+音频+视频 | Omni-modal Agentic，ARIA 语音合成 |
| Kimi K3 | 文本+图像+视频 | MoonViT-V2，原生多模态 |
| Gemini 3.x | 文本+音频+图像+视频 | 原生多模态，3 小时视频理解 |
| Phi-4-reasoning-vision | 文本+图像 | 15B 低计算量多模态推理 |
| Step3-VL-10B | 文本+图像 | PaCoRe 并行推理，10B 超越 100B+ |

---

> 本报告由 opencode 自动搜索编译，数据截至 2026-09-07。部分信息来自公开技术报告、模型卡和博客，具体细节请参阅原始链接。
