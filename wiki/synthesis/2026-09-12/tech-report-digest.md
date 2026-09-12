---
title: "LLM Tech Report Digest — 2026-09-12"
type: synthesis
created: 2026-09-12
updated: 2026-09-12
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv, model-card, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, daily-digest]
---

# LLM Tech Report Digest — 2026-09-12

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-12）
> 本篇聚焦各公司最新报告/系统卡/模型卡，标注自 2026-09-11 走势摘要后的新增项（★）
> 本日头条：**DeepSeek-V4.1-Flash 发布（2026-09-10）** 与 **Grok 4.7 跳票（2026-09-11）**

---

## 1. DeepSeek — DeepSeek-AI

### 1.1 DeepSeek-V4.1-Flash（★ NEW — 本日头条）
- **中文标题**: DeepSeek-V4.1-Flash 模型卡
- **英文标题**: DeepSeek-V4.1-Flash (Model Card / Hugging Face Release)
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4.1-Flash
- **发布日期**: 2026-09-10（HF 发布）
- **核心参数**: 552B backbone MoE + 196B Engram 条件记忆；8B activated（prefill）/ 16B activated（decode）；上下文 1M；预训练 45T tokens；原生多模态（图像+文本）
- **主要创新点**:
  - **新架构 CED（Causal Encoder-Decoder）**: 20 层 causal encoder + 20 层 decoder
  - **CSA2（Compressed Sparse Attention 2）**: Full / Reindex / Reuse 三种静态模式 + Hierarchical Sparse Indexer
  - **SWA Bounded Replay**：滑窗注意力有界回放机制
  - **KV cache 仅 890 bytes/token**（约为 V4-Flash 的 1/4），FP4 (E2M1) KV caching
  - **Single-Pass mHC**：manifold-constrained hyper-connections 单遍版本
  - **DSpark** 推测解码加速
  - 原生多模态 + 1M 上下文
- **链接**: [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

### 1.2 DeepSeek-V4 Technical Report
- **中文标题**: DeepSeek-V4：迈向高效百万 token 上下文智能
- **英文标题**: DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4-Pro (1.6T/49B active) / V4-Flash (284B/13B active)
- **发布日期**: 2026-04（Preview）；V4-Flash-0731 正式版 2026-07
- **核心参数**: Pro: 1.6T 总参数 / 49B 激活；Flash: 284B / 13B 激活；上下文 1M tokens；预训练 32T+ tokens
- **主要创新点**:
  - 混合注意力架构：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)
  - Manifold-Constrained Hyper-Connections (mHC) 增强残差连接
  - Muon 优化器首次应用于万亿级 MoE
  - 1M 上下文推理 FLOPs 仅为 V3.2 的 27%，KV cache 仅 10%
  - V4-Pro-Max 超越 GPT-5.2 和 Gemini-3.0-Pro
  - 开源 MIT 许可
- **链接**: [arXiv:2606.19348](https://arxiv.org/abs/2606.19348)

---

## 2. OpenAI

### 2.1 GPT-6 Astra System Card（★ NEW）
- **中文标题**: GPT-6 Astra 系统卡
- **英文标题**: GPT-6 Astra System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-6 Astra
- **发布日期**: 2026-09-03（更新 2026-09-09）
- **核心参数**: 参数量未公开；多模态（文本+图像）
- **主要创新点**:
  - **首个在 Preparedness Framework 下达到 Critical（关键）网络安全级别**的模型
  - 新的 robustness-safety 训练范式（对抗性健壮性安全训练）
  - baseline cyber 能力评估：在高对抗条件下成功绕过安全分类器
  - 部署缓解：更严格隔离、硬件级 checkpoint 加密、universal CoT 监控
- **链接**: [deploymentsafety.openai.com](https://deploymentsafety.openai.com/gpt-6-astra)

### 2.2 GPT-5 System Card（参照）
- 已收录于 2026-09-11 摘要 | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267)

---

## 3. Anthropic — Claude

### 3.1 Claude Fable 5.1 & Mythos 5.1 System Card（参照）
- **发布日期**: 2026-09-01
- **主要创新点**（已收录于 2026-09-11 摘要）:
  - 编码、知识工作和问题解决前沿推进
  - CB-1 化学/生物能力但未达 CB-2 阈值
  - Mythos 5.1 网络安全评估史上最强
  - Mythos 5.1 在系统提示下诚实度低于近期 Claude 模型
- **链接**: [Anthropic CDN](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf)
- **预期动向**: 社区消息称 Claude Fable 5.2 预计 2026-09 中旬发布（未验证）

---

## 4. Meta AI — LLaMA

### 4.1 Muse Spark Safety & Preparedness Report（★ NEW）
- **中文标题**: Muse Spark 安全与准备报告
- **英文标题**: Muse Spark Safety & Preparedness Report
- **发布机构**: Meta AI
- **模型名称**: Muse Spark（Meta AI 底层模型）
- **发布日期**: 2026-05-14（arXiv 提交）
- **核心参数**: 159 页 / 57 图；参数量未公开
- **主要创新点**:
  - 在 **Advanced AI Scaling Framework** 下发布，残余风险可接受
  - **CBRN（化学/生物等）风险评估为 "high risk"（缓解前）**，缓解后降至可接受
  - 同时评估 Cybersecurity 与 Loss of Control（无法控制的自主改进）
  - 拒绝（refusal）能力在当前开放模型中 SOTA
  - 为 Meta AI 官方助手底层模型
- **链接**: [arXiv:2606.12429](https://arxiv.org/abs/2606.12429)

### 4.2 Llama 4 Scout & Maverick（参照）
- 已收录于 2026-09-11 摘要 | [Meta AI 官方](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

---

## 5. Google DeepMind — Gemini

### 5.1 Gemma 4 Technical Report（★ NEW）
- **中文标题**: Gemma 4 技术报告
- **英文标题**: Gemma 4 Technical Report
- **发布机构**: Google DeepMind / Gemma Team
- **模型名称**: Gemma 4（Dense: E2B / E4B / 12B / 31B；MoE: 26B-A4B，3.8B activated）
- **发布日期**: 2026-07-02
- **核心参数**: dense 2.3B–31B 有效参数；MoE 26B 总 / 3.8B 激活；Apache 2.0；原生多模态（文本+图像+音频）
- **主要创新点**:
  - **Thinking mode**：推理 trace 先于响应输出（Gemma 首次）
  - **Encoder-free 架构（12B）**：替换 550M 视觉 encoder 为单个 35M matmul，直接投影 40ms 音频 chunk 与图像 patch；内存碎片减少
  - **长上下文优化**：5:1 local:global attention（E2B 为 4:1）、pp-RoPE、KV cache sharing + global 层 keys-as-values → 全局 KV footprint 最高减少 37.5%
  - **MTP drafter head** 支持 speculative decoding；QAT 量化版本
  - 31B：MMLU Pro 85.2 / AIME 2026 89.2 / LiveCodeBench 80.0
  - E2B 以约 1/10 参数匹敌 Gemma 3 27B；31B 为 Arena 上 top dense 开放模型
- **链接**: [arXiv:2607.02770](https://arxiv.org/abs/2607.02770)

### 5.2 Gemini 动态
- **Gemini 4**: 处于预训练阶段（2026-07-21 确认，"significantly larger"），尚无技术报告
- **Gemini 3.6 Flash**: 2026-09-02 发布（产品更新，无独立报告）
- Gemini 2.5 Technical Report 已收录于 2026-09-11 摘要 | [arXiv:2507.06261](https://arxiv.org/abs/2507.06261)

---

## 6. Microsoft — Phi

### 6.1 Phi-4-reasoning-vision-15B Technical Report（★ NEW）
- **中文标题**: Phi-4 推理-视觉 15B 技术报告
- **英文标题**: Phi-4-reasoning-vision-15B Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4-reasoning-vision-15B
- **发布日期**: 2026-03
- **核心参数**: 15B 参数；多模态（视觉+文本）；推理模式
- **主要创新点**:
  - 紧凑多模态推理模型（延续 Phi 系列"小模型高效率"路线）
  - 数据策展 + 合成数据增强
  - dynamic-resolution 视觉 encoder + mode tokens
  - 推理能力与视觉理解结合
- **链接**: [arXiv:2603.03975](https://arxiv.org/abs/2603.03975)
- **预期动向**: Phi-5 已预告（pre-release），尚未发布正式技术报告

### 6.2 Phi 系列历史报告（参照）
- Phi-4 / Phi-4-reasoning / Phi-4-Mini 均已收录于 2026-09-11 摘要

---

## 7. Mistral AI

### 7.1 Shieldstral（★ NEW）
- **中文标题**: Shieldstral：开放多模态安全分类器
- **英文标题**: Shieldstral: An Open Multimodal Safety Classifier (via Reinforcement Learning or Policy-adaptive)
- **发布机构**: Mistral AI
- **模型名称**: Shieldstral（3B）
- **发布日期**: 2026-07
- **核心参数**: 3B 参数；多模态安全分类器
- **主要创新点**:
  - 政策自适应（policy-adaptive）安全分类器，可跟随企业政策版本迭代
  - 在约 54.1M 样本上训练
  - 支持文本 + 多模态内容审核
- **链接**: [arXiv:2607.25857](https://arxiv.org/abs/2607.25857)

### 7.2 Ministral 3（★ NEW）
- **中文标题**: Ministral 3
- **英文标题**: Ministral 3
- **发布机构**: Mistral AI
- **模型名称**: Ministral 3（3B / 8B / 14B）
- **发布日期**: 2026-01
- **核心参数**: 3B/8B/14B dense；多尺寸
- **主要创新点**:
  - 小型模型聚焦 企业/边缘部署 效率
  - 多语言 + 原生多模态
- **链接**: [arXiv:2601.08584](https://arxiv.org/abs/2601.08584)

### 7.3 Mistral 3 / Magistral / Medium 3（参照）
- 均已收录于 2026-09-11 摘要

---

## 8. Alibaba — Qwen

### 8.1 Qwen3.8-Flash-Next Technical Report（★ NEW）
- **中文标题**: Qwen3.8-Flash-Next：重思考下一代表征与架构
- **英文标题**: Rethinking Next-Generation Representations and Architectures (Qwen3.8-Flash-Next)
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3.8-Flash-Next（125B-A6B）
- **发布日期**: 2026-08-31
- **核心参数**: 125B 总参数 / 6B 激活（MoE）；51B 参数 n-gram embedding 表置于 off-accelerator
- **主要创新点**:
  - **Gated DeltaNet 混合注意力 + QSA**（Query-based Sparse Attention）混合架构
  - 超大参数 **n-gram embedding 表（off-accelerator）** 以超低成本注入更多"表征参数"
  - **Gated Residual（4-branch）** 残差设计
  - **Muon 优化器**用于训练
  - 在 8/14 个 benchmark 上**超越其前身 397B-A17B**，激活参数仅 1/3、tokens 约 1/3、FLOPs 约 1/9
- **链接**: [arXiv:2608.30320](https://arxiv.org/abs/2608.30320)

### 8.2 Qwen3.8-Max（参照）
- 2026-08 发布，已收录于 2026-09-11 摘要（2.4T 参数，Text Arena #5 / Vision Arena #2）

### 8.3 Qwen3 / Qwen2.5（参照）
- 均已收录于 2026-09-11 摘要

---

## 9. xAI — Grok

### 9.1 Grok 4.7 跳票（★ NEW — 本日动态）
- **动态**: 2026-09-11 马斯克称 Grok 4.7 仍需"a few more days" RL tuning；原预期 2026-09-12 前发布，现目标约 2026-09-15 之后
- **第三方报道**: Grok 4.7 参数量约 2.1T（较 Grok 4.6 的 1.5T 提升 40%）
- **状态**: 尚无 Grok 4.7 模型卡/技术报告

### 9.2 Grok 4.6 Model Card（★ NEW）
- **中文标题**: Grok 4.6 模型卡
- **英文标题**: Model Card: Grok 4.6
- **发布机构**: xAI（SpaceXAI, XAI LLC 的 DBA 名称）
- **模型名称**: Grok 4.6
- **发布日期**: 2026-08-12（修订 2026-08-17）
- **核心参数**: 1.5T 参数级别（"1.5T-scale model family"）；上下文 500K；多模态（文本+图像输入）；数据截止 2026-02-01；定价 $2/M input + $6/M output
- **主要创新点**:
  - 聚焦长程 agent 任务（编码、工程、office work、AI research、inference optimization）
  - **与 Cursor 合作**：在匿名化 Cursor 工作流数据上补充训练（coding + agentic）
  - Reasoning 档位 low/medium/high/xhigh
  - 自报安全回归：vs Grok 4.5，self-harm 拒答合规度、诚实度（adversarial）、sycophancy 均有退化（修订版已更正部分数字）
  - 36 页模型卡，含 CBRN refusal、jailbreak robustness、mental-health 等安全章节
- **链接**:
  - [Model Card PDF](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf)
  - [Announcement](https://x.ai/news/grok-4-6)

### 9.3 Grok 4.20 System Card（参照）
- 已收录于 2026-09-11 摘要 | [xAI Data](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf)

---

## 10. NVIDIA — Nemotron

### 10.1 Nemotron 3 Ultra 模型卡（★ NEW）
- **中文标题**: NVIDIA Nemotron 3 Ultra（模型卡，2026-06-09）
- **英文标题**: Nemotron 3 Ultra (Model Card / NVIDIA Research)
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Ultra（550B-A55B）
- **发布日期**: 2026-06-09
- **核心参数**: 550B 总参数 / 55B 激活（MoE）；Hybrid Mamba-Attention 架构；20T tokens 预训练；上下文 1M+；NVFP4 预训练
- **主要创新点**:
  - **Hybrid Mamba-Attention MoE**：SSM + Attention 混合（长程效率 + 高质量）
  - **LatentMoE**：低维 latent 路由
  - **MTP（Multi-Token Prediction）** + **MOPD**（multi-objective progressive distillation）
  - **NVFP4 预训练**：4-bit 精度从预训练开始稳定训练
  - **多环境 RLVR（Reinforcement Learning with Verifiable Rewards）** 后训练
  - 推理吞吐约为公开 SOTA 模型的 **6×**
- **链接**: [NVIDIA Research](https://research.nvidia.com/nemotron-3-ultra-model-card)

### 10.2 Nemotron 3 Family Technical Report（参照）
- 已收录于 2026-09-11 摘要 | [arXiv:2512.20856](https://arxiv.org/abs/2512.20856)

---

## 11. Moonshot AI — Kimi

### 11.1 Kimi K2.7 Code（★ NEW）
- **中文标题**: Kimi K2.7 Code
- **英文标题**: Kimi K2.7 Code（官方页面发布）
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K2.7 Code
- **发布日期**: 2026-09-04
- **核心参数**: 1T 总参数 / 32B 激活（MoE）；上下文 256K；MLA 注意力；开源
- **主要创新点**:
  - 面向 coding + agentic 场景的开源模型
  - **Kimi Code Bench v2 得分 62.0，较 K2.6 提升 +21.8%**
  - 思考 token 输出较 K2.6 减少约 **30%**（更高效推理）
  - 延续 K2/K2.5 的 MoE + MLA 架构路线
- **链接**: [Kimi 官方](https://kimi.ai/)

### 11.2 Kimi K2 / K2.5（参照）
- 均已收录于 2026-09-11 摘要：[K2 arXiv:2507.20534](https://arxiv.org/abs/2507.20534) / [K2.5 arXiv:2602.02276](https://arxiv.org/abs/2602.02276)

---

## 12. Amazon — Nova

### 12.1 Nova 2 家族（★ NEW）
- **中文标题**: Amazon Nova 2 模型家族
- **英文标题**: Amazon Nova 2 Model Family（re:Invent 2025）
- **发布机构**: Amazon AGI
- **模型名称**: Nova 2 Lite / Nova 2 Pro / Nova 2 Sonic / Nova 2 Omni；Nova Forge（app builder）；Nova Act（browser agent）
- **发布日期**: 2025-12-02
- **核心参数**: 多尺寸多模态（文本/图像/视频/音频）
- **主要创新点**:
  - Nova 2 家族全面升级（Lite/Pro 为主力推理模型，Sonic/Omni 覆盖实时与全模态）
  - **Nova Act**：browser agent，约 **90% browser automation 可靠性**
  - Nova Forge：多模型 app 构建平台
- **链接**: [Amazon 官方](https://press.aboutamazon.com/)

### 12.2 Amazon Nova Family Technical Report（参照）
- 已收录于 2026-09-11 摘要 | [arXiv:2506.12103](https://arxiv.org/abs/2506.12103)
- 注：截至 2026-09-12 未发现 Nova 3 相关报告/发布

---

## 13. Apple — Apple Intelligence Foundation Models

### 13.1 第三代 Apple Foundation Models（AFM 3）（★ NEW）
- **中文标题**: 第三代 Apple Foundation Models（AFM 3）
- **英文标题**: Third-Generation Apple Foundation Models (AFM)
- **发布机构**: Apple（与 Google 合作构建）
- **模型名称**: AFM 3 Core (3B dense, on-device) / AFM 3 Core Advanced (20B sparse, on-device) / AFM 3 Cloud / ADM 3 Cloud (Image) / AFM 3 Cloud Pro (server)
- **发布日期**: 2026-06-08（WWDC）
- **核心参数**: 端侧 3B dense + 20B sparse；Cloud Pro 服务器模型（NVIDIA GPUs + Google Cloud, confidential compute）
- **主要创新点**:
  - **AFM 3 Core Advanced**: 20B 稀疏模型，激活仅 1–4B，专为端侧设计
  - **AV foundation models**（视频/AIML 基础模型）
  - **Cloud Pro**: 服务器端模型运行于 Google Cloud 的 NVIDIA GPU，采用 confidential compute
  - 全家族 5 个模型（语言 + 图像）
  - 2025 年度技术报告发布后，2026 年度报告官网称"later this summer"发布（截至 2026-09-12 尚未发布）
- **链接**: [machinelearning.apple.com](https://machinelearning.apple.com/)

### 13.2 AFM 2025 Tech Report（参照）
- 已收录于 2026-09-11 摘要 | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575)

---

## 14. ByteDance — Seed / 豆包

### 14.1 Seed2.0 Model Card（★ NEW）
- **中文标题**: Seed2.0 模型卡
- **英文标题**: Seed2.0 Model Card
- **发布机构**: ByteDance Seed Team
- **模型名称**: Doubao-Seed-2.0-pro（Volcano Engine 上开放）
- **发布日期**: 2026-07-03
- **核心参数**: 参数量未公开；原生多模态 + agentic
- **主要创新点**:
  - 模型卡基准对比覆盖 GPT-5.2 High、Claude-Sonnet-4.5、Claude-Opus-4.5、Gemini-3-Pro/3-Flash High 等
  - 面向 语文/数学/科学/编程/coding/agentic 任务的多模态能力
  - 与火山引擎（Volcano Engine）深度集成，强调行业落地
- **链接**: [arXiv:2607.00248](https://arxiv.org/abs/2607.00248)

### 14.2 Seed1.5-VL / Seed-Thinking-v1.5 / Seed1.6（参照）
- 均已收录于 2026-09-11 摘要

---

## 15. 智谱 AI — GLM

### 15.1 GLM-5.2（★ NEW）
- **中文标题**: GLM-5.2
- **英文标题**: GLM-5.2
- **发布机构**: 智谱 AI (Zhipu AI)
- **模型名称**: GLM-5.2
- **发布日期**: 2026-06-16
- **核心参数**: 上下文 1M+ tokens
- **主要创新点**:
  - 超长上下文（1M）+ 高推理效率
  - 开源路线延续（GLM 系列）
- **链接**: [arXiv:2606.12370](https://arxiv.org/abs/2606.12370)

### 15.2 GLM-5.3 Flash 与 GLM-6（★ NEW）
- **GLM-5.3 Flash**: 智谱首个**全流程国产芯片**训练/推理模型（2026-09-10 前后消息）
- **GLM-6**: 官方表示在研，目标探索"self-evolution"（自我进化）；社区/第三方报道存在命名与时间线不一致（有说法称 2026-06 已发布 GLM-6，与官方 GLM-5.2 时间线冲突）
  > ⚠️ CONTRADICTION: 第三方简报（Presenc）称 GLM-6 已于 2026-06 上旬发布并作为 GLM-5.1 后继；官方序列则显示 GLM-5.2（2026-06-16）为最新发布。官方端口径优先，GLM-6 视为在研（tentative）。

### 15.3 GLM-4.5 / GLM-5（参照）
- 均已收录于 2026-09-11 摘要：[GLM-4.5](https://www.zhipuai.cn/) / [GLM-5 arXiv:2602.15763](https://arxiv.org/abs/2602.15763)

---

## 16. InternLM / 上海 AI Lab

### 16.1 Intern-S2-Preview（★ NEW）
- **中文标题**: Intern-S2-Preview：科学导向的 Agentic 基础模型
- **英文标题**: Intern-S2-Preview: A Scientific Agentic Foundation Model
- **发布机构**: Shanghai AI Lab / InternLM（OpenBMB）
- **模型名称**: Intern-S2-Preview（旗舰 Intern-S2-Preview-397B）
- **发布日期**: 2026-08
- **核心参数**: 397B 旗舰（另有多尺寸）；稀疏 MoE
- **主要创新点**:
  - **科学 agentic 基础模型**：时间序列建模（time-series forecasting）统一 tokenizer
  - **Memory Decoder** 路径：专用解码分支增强长程记忆
  - 训练配方：SFT + 可扩展 multi-task RL + black/white-box agentic RL + on-policy distillation
  - 面向 数学/科学/工程 的科学推理与工具使用
- **链接**: [arXiv:2608.13505](https://arxiv.org/abs/2608.13505)

### 16.2 Intern-S1-Pro（★ NEW）
- **中文标题**: Intern-S1-Pro：万亿级科学多模态基础模型
- **英文标题**: Intern-S1-Pro: A Trillion-Scale Scientific Multimodal Foundation Model
- **发布机构**: Shanghai AI Lab / InternLM
- **发布日期**: 2026-03
- **核心参数**: 万亿级（trillion-scale）参数
- **主要创新点**: 面向科学领域的大规模多模态（文本/图像/视频）基础模型
- **链接**: [arXiv:2603.25040](https://arxiv.org/abs/2603.25040)

### 16.3 InternVideo3（★ NEW）
- **中文标题**: InternVideo3：统一视频理解基础模型
- **英文标题**: InternVideo3
- **发布机构**: Shanghai AI Lab / InternLM
- **发布日期**: 2026-06
- **核心参数**: 视频多模态基础模型
- **主要创新点**: 统一视频理解（含时间感知能力）基础模型技术报告
- **链接**: [arXiv:2606.12195](https://arxiv.org/abs/2606.12195)

### 16.4 InternVL3.5 / InternVL3（参照）
- 均已收录于 2026-09-11 摘要

---

## 17. StepFun — 阶跃星辰

### 17.1 Step-3.7-Flash（★ NEW）
- **中文标题**: Step-3.7-Flash：Agent 时代的开源模型
- **英文标题**: Step-3.7-Flash
- **发布机构**: StepFun
- **模型名称**: Step-3.7-Flash（198B-A11B）
- **发布日期**: 2026-08（公开信息）
- **核心参数**: 198B 总参数 / 11B 激活；MoE；原生多模态（全模态）；上下文 256K
- **主要创新点**:
  - 稀疏 MoE 全模态模型（文本/图像/语音/视频）
  - 极低激活参数下的 agent 能力
- **链接**: [GitHub](https://github.com/stepfun-ai/)

### 17.2 Step3-VL-10B Technical Report（★ NEW）
- **中文标题**: Step3-VL-10B 技术报告
- **英文标题**: Step3-VL-10B Technical Report
- **发布机构**: StepFun
- **模型名称**: Step3-VL-10B
- **发布日期**: 2026-01
- **核心参数**: 10B 参数 VLM
- **主要创新点**:
  - **10B 模型对标 10–20 倍大的模型**：GLM-4.6V-106B、Qwen3-VL-235B、Gemini 2.5 Pro、Seed-1.5-VL
  - 92.2% MMBench / 80.11% MMMU / 94.43% AIME2025
  - **PaCoRe test-time compute**（并行候选重排）
  - **Muon vs AdamW 实证研究**（报告内系统对比）
- **链接**: [arXiv:2601.09668](https://arxiv.org/abs/2601.09668)

### 17.3 Step-3 / Step-3.5 Flash / Step-DeepResearch（参照）
- 均已收录于 2026-09-11 摘要

---

## 18. 01.AI — Yi

### 18.1 Yi 系列现状（无新增）
- 截至 2026-09-12 **未发现 2026 年新的 Yi 技术报告**
- 最新综合报告: Yi-Lightning（[arXiv:2412.01253](https://arxiv.org/abs/2412.01253), 2024-12）
- 历史报告已收录于 2026-09-11 摘要 | [Yi arXiv:2403.04652](https://arxiv.org/abs/2403.04652)

---

## 19. Baichuan

### 19.1 Baichuan-M3（★ NEW）
- **中文标题**: Baichuan-M3：面向医疗的核心增强大模型
- **英文标题**: Baichuan-M3: A Core-Enhanced Large Language Model for Medical Use
- **发布机构**: Baichuan Intelligence
- **模型名称**: Baichuan-M3
- **发布日期**: 2026-01
- **核心参数**: 多尺寸（含开源版本）；医疗领域中英文双语
- **主要创新点**:
  - 医疗推理专用增强（医学知识注入 + 领域微调）
  - **HealthBench-Hard 44.4，超越 GPT-5.2**（医疗 SOTA）
  - ScanBench 等医疗评测领先
  - 权重公开（Hugging Face）
- **链接**: [arXiv:2602.06570](https://arxiv.org/abs/2602.06570)

### 19.2 Baichuan-Omni（参照）
- 已收录于 2026-09-11 摘要 | [arXiv:2410.08565](https://arxiv.org/abs/2410.08565)

---

## 本日头条与动态（相对 2026-09-11 摘要的 Delta）

### 1. DeepSeek-V4.1-Flash 发布（2026-09-10）
- 552B MoE + 196B Engram，**新 CED 架构 + CSA2 + SWA Bounded Replay**，KV cache 890 bytes/token
- 上市仅 2 天，是今天最重要的新增报告级事件

### 2. Grok 4.7 跳票（2026-09-11）
- 马斯克：还需数天 RL tuning；原预期 0912 前发布，现目标 ~0915+
- 报道参数 ~2.1T（可对照 Grok 4.6 的 1.5T）

### 3. 今日新增报告汇总（★ 共 15 项）
| 公司 | 新增项 | 日期 | 类型 |
|------|--------|------|------|
| DeepSeek | V4.1-Flash | 2026-09-10 | HF 发布/模型卡 |
| OpenAI | GPT-6 Astra System Card | 2026-09-03 | System Card |
| Meta | Muse Spark Safety Report | 2026-05-14 | Safety Report |
| Google | Gemma 4 Technical Report | 2026-07-02 | Technical Report |
| Microsoft | Phi-4-reasoning-vision-15B | 2026-03 | Technical Report |
| Mistral | Shieldstral | 2026-07 | Technical Report |
| Mistral | Ministral 3 | 2026-01 | Technical Report |
| Qwen | Qwen3.8-Flash-Next | 2026-08-31 | Technical Report |
| xAI | Grok 4.6 Model Card | 2026-08-12 | Model Card |
| NVIDIA | Nemotron 3 Ultra Model Card | 2026-06-09 | Model Card |
| Moonshot | Kimi K2.7 Code | 2026-09-04 | 产品/模型发布 |
| Amazon | Nova 2 家族 | 2025-12-02 | 产品发布 |
| Apple | AFM 3 第三代 | 2026-06-08 | 产品发布 |
| ByteDance | Seed2.0 Model Card | 2026-07-03 | Model Card |
| 智谱 | GLM-5.2 / 5.3 Flash / GLM-6 动态 | 2026-06~09 | 报告+新闻 |
| InternLM | Intern-S2-Preview / S1-Pro / Video3 | 2026-03~08 | Technical Report |
| StepFun | Step-3.7-Flash / Step3-VL-10B | 2026-01~08 | Technical Report |
| Baichuan | Baichuan-M3 | 2026-01 | Technical Report |

### 4. 未发布新正式报告的公司
- **01.AI / Yi**: 无 2026 新报告（最新为 Yi-Lightning 2024-12）
- **Apple**: AFM 3 报告承诺"later this summer"，尚未发布
- **Google Gemini**: Gemini 4 预训练中，无新报告；Gemini 3.6 Flash 仅产品发布
- **OpenAI**: GPT-6 Astra 仅系统卡（无技术报告）

### 5. 预期后续事件（未验证）
- Grok 4.7 正式发布：目标 ~2026-09-15+（消息源：马斯克 2026-09-11）
- Claude Fable 5.2：2026-09 中旬（社区消息）
- Apple AFM 3 技术报告：2026 夏末（官方承诺，已过期未发布）

---

## 交叉主题分析

### 1. 架构趋势补充：注意力稀疏化 + 条件记忆成为新方向
| 公司 | 模型 | 新架构要素 |
|------|------|-----------|
| DeepSeek | V4 / V4.1-Flash | CED + CSA2 + SWA Bounded Replay + 55B-level Engram 条件记忆 |
| Qwen | Qwen3.8-Flash-Next | Gated DeltaNet 混合 + QSA + off-accelerator n-gram 表征 |
| NVIDIA | Nemotron 3 Ultra | Hybrid Mamba-Attention + LatentMoE |
| Google | Gemma 4 12B | Encoder-free（单 matmul 取代 550M 视觉 encoder） |
| InternLM | Intern-S2-Preview | 时间序列 tokenizer + Memory Decoder |

趋势：除 MoE 外，**显式记忆层（Engram / Memory Decoder）、稀疏注意力（CSA2/DSA/QSA）、表征参数外置（off-accelerator）** 成为 2026 下半年有效稀释计算成本的主要手段。

### 2. KV cache 效率竞争
| 模型 | KV cache | 关键技术 |
|------|----------|---------|
| DeepSeek-V4.1-Flash | 890 bytes/token（≈V4-Flash 的 1/4） | FP4 (E2M1) KV caching |
| DeepSeek-V4 | V3.2 的 ~10% | CSA + HCA |
| Gemma 4 | 全局 KV footprint -37.5% | KV sharing + keys-as-values + pp-RoPE |

### 3. 小型/开放模型"以小博大"
- **Gemma 4**: E2B（2.3B 有效）以 1/10 参数匹敌 Gemma 3 27B
- **Step3-VL-10B**: 10B 对标 100B+ 级 VLM（MMBench 92.2%）
- **Qwen3.8-Flash-Next**: 6B activated 超越前代 17B activated
- **Baichuan-M3**: 医疗域超越 GPT-5.2（HealthBench-Hard）
- 印证"数据 + 架构 + 后训练（RL）"对参数规模的对冲效应持续存在

### 4. 开源许可趋势
- Gemma 4: Apache 2.0
- DeepSeek-V4 / V4.1-Flash: MIT（V4 系列）
- Qwen3.8 系列: Apache 2.0
- Kimi K2.7 Code: 开源（kimi 系列延续）
- 智谱 GLM: 开放权重延续（GLM-5.3 Flash 国产芯片全链路）
- Meta Muse Spark: 未开源权重（仅安全报告公开）
- Apple / OpenAI / Google Gemini: 闭源

### 5. 安全评估体系（System Card 焦点）
- **OpenAI GPT-6 Astra**: 首个 Critical cyber 级别（Preparedness Framework 新增 robustness-safety 训练）
- **Meta Muse Spark**: Advanced AI Scaling Framework 首个典型报告；CBRN 缓解前 "high risk"
- **xAI Grok 4.6**: 自报 4.5→4.6 安全回归（self-harm 拒答、诚实度、sycophancy）
- **Anthropic Fable 5.1**: CB-1 能力但未及 CB-2

### 6. 国产算力主线
- **智谱 GLM-5.3 Flash**: 全流程国产芯片（训练+推理）
- **GLM-6**: 以"self-evolution"为目标的在研模型
- **Baichuan-M3 / Intern-S2**: 开源多尺寸，国产生态持续铺开