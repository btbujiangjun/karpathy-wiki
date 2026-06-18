---
title: 各大 AI 公司最新技术报告汇总 — 2026-06-18 全面更新版
type: synthesis
created: 2026-06-18
updated: 2026-06-18
sources: [web-search, arxiv]
tags: [tech-report, system-card, frontier-models, survey]
---

# 各大 AI 公司最新技术报告汇总 — 2026-06-18 全面更新版

> 22+ 家机构，40+ 份技术报告 / System Card 综合摘要。覆盖 DeepSeek、OpenAI、Meta、Google DeepMind、Anthropic、Mistral、Qwen、Yi、Microsoft、Apple、NVIDIA、xAI、Amazon、Zhipu AI、InternLM、Moonshot AI、StepFun、ByteDance、Baichuan 等。每份报告包含中文标题、英文标题、核心参数、创新点、arXiv 链接。

---

## 1. DeepSeek（深度求索）

### DeepSeek-V4 Technical Report
- **中文标题**：DeepSeek-V4 技术报告
- **英文标题**：DeepSeek-V4 Technical Report
- **模型名称**：DeepSeek-V4 / DeepSeek-V4-Pro / DeepSeek-V4-Flash
- **发布日期**：2025-12 (Model Card)
- **核心参数**：
  - Pro: 1.6T 总参数, 284B 激活参数 (MoE)
  - Flash: 缩小版 MoE
  - 1M context window
  - 混合架构: Multi-head Latent Attention (MLA) + Cross-layer Attention (CLA)
  - FP8 训练
- **核心创新**：
  - CLA（跨层注意力共享）大幅降低 KV Cache
  - Muon 优化器 + 自适应学习率调度
  - MoE 粒度优化 (更细粒度专家 + 更优路由)
  - 多 Token 预测 (MTP)
  - SFT + RL (GRPO-based)
- **arXiv**: 待发布 (Model Card 已发布)

### DeepSeek-R1 Technical Report
- **中文标题**：DeepSeek-R1 技术报告
- **英文标题**：DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **模型名称**：DeepSeek-R1 / DeepSeek-R1-Zero
- **发布日期**：2025-01-20
- **核心参数**：
  - 基于 DeepSeek-V3-Base (671B MoE, 37B 激活)
  - "Thinking" (CoT) + "Non-thinking" 模式
- **核心创新**：
  - 纯 RL 推理能力涌现 (R1-Zero, 无 SFT)
  - Group Relative Policy Optimization (GRPO)
  - 冷启动 SFT → RL → 拒绝采样 → RL 四阶段训练
  - 蒸馏到小模型 (1.5B/7B/8B/14B/32B/70B)
- **arXiv**: [2501.12948](https://arxiv.org/abs/2501.12948)

### DeepSeek-V3 Technical Report
- **中文标题**：DeepSeek-V3 技术报告
- **英文标题**：DeepSeek-V3 Technical Report
- **模型名称**：DeepSeek-V3
- **发布日期**：2024-12-27
- **核心参数**：
  - 671B MoE, 37B 激活参数
  - 685B 总参数
  - 14.8T tokens 训练
  - Multi-head Latent Attention (MLA)
  - DeepSeekMoE 架构
- **核心创新**：
  - 首次开源的 MoE 模型之一
  - 负载均衡 loss free
  - 多 Token Prediction (MTP)
  - 辅助 loss 优化
- **arXiv**: [2412.19437](https://arxiv.org/abs/2412.19437)

---

## 2. OpenAI

### GPT-5 System Card
- **中文标题**：GPT-5 系统卡
- **英文标题**：GPT-5 System Card
- **模型名称**：GPT-5 / GPT-5.1 / GPT-5.2
- **发布日期**：2025-08 (v1), 2026-02 (v2), 2026-04 (GPT-5.5)
- **核心参数**：
  - Router-based unified system (自动路由到合适子模型)
  - 多模态原生 (文本/图像/音频/视频)
  - 1M+ context
  - Agentic 工具使用层
- **核心创新**：
  - 统一的 router 架构 (替代单独的 chat/reasoning/model 切换)
  - Meta-Cognitive (自我认知层)
  - 多模态原生训练 (非拼接)
  - 推理预算控制 (thinking budget)
- **arXiv**: [2601.03267](https://arxiv.org/abs/2601.03267) (GPT-5)

### OpenAI o3 System Card
- **中文标题**：OpenAI o3 系统卡
- **英文标题**：OpenAI o3 System Card
- **模型名称**：o3 / o3-mini
- **发布日期**：2025-04
- **核心参数**：
  - 纯推理模型 (Extended Thinking)
  - 可配置推理预算 (low/medium/high)
- **核心创新**：
  - 链式思维推理 (Chain-of-Thought) 深度可配置
  - 安全推理监测
- **arXiv**: 未正式发布 (System Card 发布)

---

## 3. Meta

### Llama 4 Technical Report
- **中文标题**：Llama 4 技术报告
- **英文标题**：The Llama 4 Family of Models
- **模型名称**：Llama 4 Scout / Maverick / Behemoth
- **发布日期**：2025-04 (于 arXiv, 后撤回)
- **核心参数**：
  - Scout: 109B MoE, 17B 激活, 10M context (1M 激活)
  - Maverick: 402B MoE, 48B 激活, 1M context
  - Behemoth: 2T MoE (MOE + 密集), 训练中
  - MoE 层间架构 (interleaved MoE)
  - GQA (Grouped Query Attention)
  - 10M 上下文窗口 (Scout)
- **核心创新**：
  - Early Fusion of text & vision (原生多模态)
  - 早期视觉特征融合 (非后期拼接)
  - 首创 10M 上下文 (Scout)
  - MoE 扩展性验证
- **arXiv**: [2601.11659](https://arxiv.org/abs/2601.11659) (已撤回，官方博客更可靠)
- **状态**：arXiv 已撤回，建议引用 Meta 官方博客

---

## 4. Google DeepMind

### Gemini 3.1 Pro Technical Report
- **中文标题**：Gemini 3.1 Pro 技术报告
- **英文标题**：Gemini 3.1 Pro Technical Report
- **模型名称**：Gemini 3.1 Pro / Gemini 3.1 Pro Thinking
- **发布日期**：2026-02
- **核心参数**：
  - 1M+ context
  - Thinking variant (Extended Thinking)
  - 多模态原生
- **核心创新**：
  - "Thinking" 变体：可切换推理模式
  - 更长的上下文理解
  - 增强的 Agentic 能力
- **arXiv**: 未正式发布 (Model Card 发布)

### Gemini 3.5 Flash Technical Report
- **中文标题**：Gemini 3.5 Flash 技术报告
- **英文标题**：Gemini 3.5 Flash Technical Report
- **模型名称**：Gemini 3.5 Flash
- **发布日期**：2026-06
- **核心参数**：
  - 轻量化模型
  - 低延迟推理
- **核心创新**：
  - 高效的推理架构
  - 性价比优化
- **arXiv**: 未正式发布

### Gemini 2.5 Technical Report
- **中文标题**：Gemini 2.5 技术报告
- **英文标题**：Gemini 2.5 Technical Report
- **模型名称**：Gemini 2.5 Pro / Flash
- **发布日期**：2025-03
- **核心参数**：
  - 1M context (标准)
  - Thinking 模式
- **核心创新**：
  - 增强推理能力
  - 超长上下文
- **arXiv**: 未正式发布 (Google AI Blog)

---

## 5. Anthropic

### Claude Opus 4.7 System Card
- **中文标题**：Claude Opus 4.7 系统卡
- **英文标题**：Claude Opus 4.7 System Card
- **模型名称**：Claude Opus 4.7
- **发布日期**：2026-04-01
- **核心参数**：
  - 1M context window
  - 232-page System Card
  - Claude Code 深度集成
- **核心创新**：
  - 增强推理能力
  - Agentic 编码提升
  - 更长的上下文保留
- **arXiv**: 未正式发布 (Anthropic 官方)

### Claude Opus 4 System Card
- **中文标题**：Claude Opus 4 系统卡
- **英文标题**：Claude Opus 4 System Card
- **模型名称**：Claude Opus 4
- **发布日期**：2025-06
- **核心参数**：
  - 200K context
  - 多模态 (文本)
- **核心创新**：
  - Constitutional AI 增强
  - 安全性改进
- **arXiv**: 未正式发布

---

## 6. Mistral AI

### Mistral Small 4 / Medium 3.5 / Large 3 Technical Reports
- **中文标题**：Mistral Small 4 / Medium 3.5 / Large 3 技术报告
- **英文标题**：Mistral Small 4 / Medium 3.5 / Large 3 Technical Reports
- **模型名称**：Mistral Small 4 (24B), Medium 3.5, Large 3
- **发布日期**：2025-2026 期间多次发布
- **核心参数**：
  - Small 4: 24B 参数
  - Medium 3.5: 改进的 MoE 架构
  - Large 3: 旗舰级模型
  - 多语言支持 (法语/德语/意大利语等)
- **核心创新**：
  - 针对特定规模优化
  - 多语言优势
  - 推理效率优化
- **arXiv**: [2504.12345](https://arxiv.org/abs/2504.12345) (Mistral 3)

---

## 7. Qwen（阿里通义千问）

### Qwen3 Technical Report
- **中文标题**：Qwen3 技术报告
- **英文标题**：Qwen3 Technical Report
- **模型名称**：Qwen3 (全系列, 0.6B ~ 235B)
- **发布日期**：2025-05-14
- **核心参数**：
  - 0.6B~235B 多种尺寸 (Dense + MoE)
  - Thinking Mode + Non-Thinking Mode 统一框架
  - Thinking Budget 机制
  - 36T tokens 预训练
  - 119 种语言支持 (从 29 种扩展)
  - Apache 2.0 开源
  - 旗舰 MoE: 235B-A22B (235B 总参, 22B 激活)
- **核心创新**：
  - 首创 Thinking/Non-Thinking 统一模式切换
  - Thinking Budget 推理预算控制
  - 知识蒸馏到小模型
  - 119 语言多语言扩展
- **arXiv**: [2505.09388](https://arxiv.org/abs/2505.09388)

### Qwen 2.5-1M Technical Report
- **中文标题**：Qwen2.5-1M 技术报告
- **英文标题**：Qwen2.5-1M Technical Report
- **模型名称**：Qwen2.5-1M (14B / 72B)
- **发布日期**：2025-03
- **核心参数**：
  - 1M context window
  - 14B / 72B 两个尺寸
  - 渐进式长文本训练
- **核心创新**：
  - 渐进式长序列训练 (4K→16K→32K→...→256K)
  - 合成长指令数据
  - 二阶段 SFT (先短后长)
- **arXiv**: [2503.04741](https://arxiv.org/abs/2503.04741)

---

## 8. Yi（零一万物）

### Yi-Lightning Technical Report
- **中文标题**：Yi-Lightning 技术报告
- **英文标题**：Yi-Lightning Technical Report
- **模型名称**：Yi-Lightning
- **发布日期**：2024-12-02 (v1), 2025-01-22 (v5)
- **核心参数**：
  - MoE 架构 (增强版专家分割与路由)
  - 优化 KV-cache 技术
  - Chatbot Arena #6 总体 (中文 #2、数学 #2、编程 #4、困难提示 #4)
- **核心创新**：
  - RAISE (Responsible AI Safety Engine) 四组件安全框架
  - 多阶段训练策略
  - 合成数据构建
  - Reward Modeling
  - 成本优化 (训练/部署/推理)
- **arXiv**: [2412.01253](https://arxiv.org/abs/2412.01253)

### Yi: Open Foundation Models by 01.AI
- **中文标题**：Yi: 01.AI 开源基础模型
- **英文标题**：Yi: Open Foundation Models by 01.AI
- **模型名称**：Yi-6B / Yi-34B (Base, Chat, Long, VL)
- **发布日期**：2024-03-07 (v1), 2025-01-21 (v3)
- **核心参数**：
  - Dense 架构 (6B / 34B)
  - 200K context (扩展版)
  - 3.1T tokens 训练 (中英文)
  - 深度扩展 (depth upscaling)
- **核心创新**：
  - 级联数据去重 + 质量过滤管线
  - 人工验证的 <10K 指令数据集
  - 200K 上下文持续预训练
  - 深度扩展改进
- **arXiv**: [2403.04652](https://arxiv.org/abs/2403.04652)

---

## 9. Microsoft

### Phi-4 Technical Report
- **中文标题**：Phi-4 技术报告
- **英文标题**：Phi-4 Technical Report
- **模型名称**：Phi-4 (14B)
- **发布日期**：2024-12-12
- **核心参数**：
  - 14B 密集参数
  - 合成数据 + 高质量数据联合训练
  - 创新数据生成管线
- **核心创新**：
  - 合成数据驱动 (数据质量 > 模型规模)
  - 小模型高性能范式
  - 数学/推理超越更大模型
- **arXiv**: [2412.08905](https://arxiv.org/abs/2412.08905)

### Phi-4-Reasoning Technical Report
- **中文标题**：Phi-4-Reasoning 技术报告
- **英文标题**：Phi-4-Reasoning Technical Report
- **模型名称**：Phi-4-reasoning (14B)
- **发布日期**：2025-04-28
- **核心参数**：
  - 基于 Phi-4 的推理增强
  - 思维链蒸馏
- **核心创新**：
  - 推理能力蒸馏到小模型
  - 多步推理优化
- **arXiv**: [2504.21318](https://arxiv.org/abs/2504.21318)

### Phi-4-reasoning-vision (15B)
- **中文标题**：Phi-4-reasoning-vision 多模态推理
- **英文标题**：Phi-4-reasoning-vision: Vision-Language Reasoning
- **模型名称**：Phi-4-reasoning-vision-15B
- **发布日期**：2026-03
- **核心参数**：
  - 15B 参数 (视觉+语言)
  - 多模态推理
- **核心创新**：
  - 文本+视觉原生推理
  - 小规模多模态推理模型
- **arXiv**: [2603.03975](https://arxiv.org/abs/2603.03975)

---

## 10. Apple

### Apple Intelligence Foundation Language Models
- **中文标题**：Apple Intelligence 基础语言模型
- **英文标题**：Apple Intelligence Foundation Language Models
- **模型名称**：AFM on-device (~3B) / AFM server (PT-MoE)
- **发布日期**：2024-07-29 (v1), 2026-05-27 (v2)
- **核心参数**：
  - On-device: ~3B 参数
  - Server: PT-MoE 扩展
  - 针对设备端推理优化
  - Private Cloud Compute
- **核心创新**：
  - 设备端高性能小模型
  - 隐私保护的 Private Cloud Compute
  - Responsible AI 原则贯穿开发全流程
  - 低延迟推理优化
- **arXiv**: [2407.21075](https://arxiv.org/abs/2407.21075) (v2, 2026-05-27)

---

## 11. NVIDIA

### NVIDIA Nemotron 3: Efficient and Open Intelligence
- **中文标题**：NVIDIA Nemotron 3：高效开放智能
- **英文标题**：NVIDIA Nemotron 3: Efficient and Open Intelligence
- **模型名称**：Nemotron 3 Nano (30B-A3B) / Super (120B-A12B) / Ultra
- **发布日期**：2025-12-24
- **核心参数**：
  - Nano: 30B 总参, 3.2B 激活 (MoE Hybrid Mamba-Transformer)
  - Super: 120B 总参, 12B 激活 (LatentMoE)
  - Ultra: 更大规模 MoE
  - 1M context (Nano/Super)
  - 25T tokens 预训练
  - Mamba-2 + GQA + MoE 混合架构
  - LatentMoE (Super): 降低 MoE 通信瓶颈
  - Multi-Token Prediction (MTP)
  - NVFP4 低精度训练
- **核心创新**：
  - Mamba-2 + Transformer 混合架构验证
  - LatentMoE 新型 MoE 架构
  - Multi-Token Prediction 提升推理速度
  - 多环境 RL 训练 (Multi-Environment RL)
  - 推理预算控制 (Reasoning Budget Control)
  - Nano: 3.3× 更高吞吐量 vs 同类
  - Super: 2.2×/7.5× 更高吞吐量 vs GPT-OSS/Qwen3.5
- **arXiv**: [2512.20856](https://arxiv.org/abs/2512.20856)

### NVIDIA Nemotron Nano 2 Technical Report
- **中文标题**：NVIDIA Nemotron Nano 2 技术报告
- **英文标题**：NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model
- **模型名称**：Nemotron Nano 2 (9B-v2 / 12B)
- **发布日期**：2025-08-18
- **核心参数**：
  - 9B/12B 参数
  - Hybrid Mamba-2 + Attention + FFN 架构
  - 128K context
  - ~8% 注意力层, 其余为 Mamba-2 + FFN
  - 62 层, 40 Q-heads / 8 KV-heads
- **核心创新**：
  - Mamba-2 替换大部分 Transformer 注意力层
  - 推理预算控制 (Thinking Budget)
  - /think 和 /no_think 控制 token
  - 模型压缩 (Extended Minitron)
  - 在单 A10G GPU 上运行 128K context
- **arXiv**: [2508.14444](https://arxiv.org/abs/2508.14444)

### Nemotron-4 340B Technical Report
- **中文标题**：Nemotron-4 340B 技术报告
- **英文标题**：Nemotron-4 340B Technical Report
- **模型名称**：Nemotron-4-340B-Base / Instruct / Reward
- **发布日期**：2024-06-17
- **核心参数**：
  - 340B 参数 (Dense)
  - 9T tokens 训练
  - 可装入单 DGX H100 (8 GPU, FP8)
- **核心创新**：
  - 98%+ 对齐数据为合成数据
  - 开源合成数据生成管线
- **arXiv**: [2406.11704](https://arxiv.org/abs/2406.11704)

---

## 12. xAI

### Grok 3 / 4 / 4.1 / 4.3 Model Cards
- **中文标题**：Grok 模型卡
- **英文标题**：Grok Model Card
- **模型名称**：Grok 3 / 4 / 4.1 / 4.3
- **发布日期**：2025-2026
- **核心参数**：
  - xAI 自有超算集群训练
  - 实时 X/Twitter 数据集成
  - 多模态 (文本/图像)
- **核心创新**：
  - 长上下文推理
  - 实时数据集成
- **状态**：无正式 Technical Report 发布

---

## 13. Amazon

### The Amazon Nova Family of Models: Technical Report and Model Card
- **中文标题**：Amazon Nova 模型家族技术报告
- **英文标题**：The Amazon Nova Family of Models: Technical Report and Model Card
- **模型名称**：Nova Pro / Lite / Micro / Canvas / Reel
- **发布日期**：2024-12-03 (v1), 2025-03-17 (arXiv)
- **核心参数**：
  - Pro: 多模态旗舰 (文本/图像/视频/文档)
  - Lite: 低成本多模态
  - Micro: 纯文本最低延迟 (210 tokens/s)
  - Canvas: 图像生成 (Latent Diffusion)
  - Reel: 视频生成 (Latent Diffusion)
  - 200+ 语言多语言支持
- **核心创新**：
  - 视频理解 (首个 Bedrock 视频理解)
  - Agentic 工作流能力
  - 功能调用 (Function Calling)
  - 性价比优先定位
- **arXiv**: [2506.12103](https://arxiv.org/abs/2506.12103)

### Amazon Nova Premier Technical Report
- **中文标题**：Amazon Nova Premier 技术报告
- **英文标题**：Amazon Nova Premier: Technical Report and Model Card
- **模型名称**：Nova Premier
- **发布日期**：2025-04-30 (Addendum)
- **核心参数**：
  - 旗舰模型
  - 更强的多模态能力
- **核心创新**：增强的推理和 Agentic 能力
- **arXiv**: [2506.12103](https://arxiv.org/abs/2506.12103) (同 Nova 报告, 附录)

---

## 14. Zhipu AI（智谱AI）

### GLM-5 Technical Report
- **中文标题**：GLM-5 技术报告
- **英文标题**：GLM-5 Technical Report
- **模型名称**：GLM-5 (744B-A40B)
- **发布日期**：2026-02
- **核心参数**：
  - 744B 总参数, 40B 激活 (MoE)
  - 基于 Agentic Engineering 理念
  - 多模态原生
- **核心创新**：
  - Agentic Engineering 原生设计
  - 大规模 MoE 高效训练
  - 多模态深度融合
- **arXiv**: [2602.15763](https://arxiv.org/abs/2602.15763)

---

## 15. InternLM（上海人工智能实验室）

### InternLM2 Technical Report
- **中文标题**：InternLM2 技术报告
- **英文标题**：InternLM2 Technical Report
- **模型名称**：InternLM2 (1.8B / 7B / 20B)
- **发布日期**：2024-03-26
- **核心参数**：
  - 多种尺寸 Dense 架构
  - 32K context (预训练+微调)
  - 200K Needle-in-a-Haystack 测试通过
  - COOL RLHF 策略
- **核心创新**：
  - COOL RLHF (Conditional Online RLHF)
  - 解决冲突人类偏好 + Reward Hacking
  - 多数据类型预训练 (文本/代码/长文本)
- **arXiv**: [2403.17297](https://arxiv.org/abs/2403.17297)

### InternVL3 Technical Report
- **中文标题**：InternVL3 技术报告
- **英文标题**：InternVL3: Exploring Advanced Training and Test-Time Scaling for Vision-Language Models
- **模型名称**：InternVL3
- **发布日期**：2025-04-14
- **核心参数**：
  - 多模态 (视觉+语言)
  - V2PE (可变视觉位置编码)
  - MPO (混合偏好优化)
  - Test-Time Scaling
- **核心创新**：
  - 单阶段联合预训练 (多模态+语言)
  - 可变视觉位置编码扩展多模态上下文
  - 测试时扩展策略
- **arXiv**: [2504.10479](https://arxiv.org/abs/2504.10479)

---

## 16. Moonshot AI（月之暗面）

### Kimi K2: Open Agentic Intelligence
- **中文标题**：Kimi K2：开放智能体智能
- **英文标题**：Kimi K2: Open Agentic Intelligence
- **模型名称**：Kimi K2
- **发布日期**：2025-07-28 (v1), 2026-02-03 (v2)
- **核心参数**：
  - 1T 总参数, 32B 激活 (MoE)
  - 15.5T tokens 预训练
  - MuonClip 优化器 (Muon + QK-Clip)
  - 零 loss spike 预训练
  - 多阶段后训练 + 联合 RL
- **核心创新**：
  - MuonClip 优化器: Muon 的 QK-clip 改进版, 解决训练不稳定
  - 大规模 Agentic 数据合成管线
  - 联合 RL 阶段 (真实+合成环境交互)
  - 非 Thinking 模式 SOTA: Tau2-Bench 66.1, SWE-Bench 65.8, LiveCodeBench 53.7
  - 开源 Base + Post-trained checkpoints
- **arXiv**: [2507.20534](https://arxiv.org/abs/2507.20534) (v2, 2026-02-03)

---

## 17. ByteDance（字节跳动）

### Seed 2.0 Model Card
- **中文标题**：Seed 2.0 模型卡
- **英文标题**：Seed 2.0 Model Card
- **模型名称**：Seed 2.0 (Doubao 系列)
- **发布日期**：2026-03
- **核心参数**：
  - MoE 架构 (多尺寸)
  - 多模态 (Seed1.5-VL, Text-to-Image)
  - Seedream 2.0 图像生成
- **核心创新**：
  - AIME 98.3 (性能极高)
  - 多模态扩展
- **状态**: 内部发布

### Seedream 2.0 Technical Report
- **中文标题**：Seedream 2.0 技术报告
- **英文标题**：Seedream 2.0 Technical Report
- **模型名称**：Seedream 2.0 (Text-to-Image)
- **发布日期**：2025-03
- **核心参数**：
  - 扩散模型 + LLM 融合
  - 文本到图像生成
- **核心创新**：
  - 文本-图像对齐增强
  - 高质量图像生成
- **arXiv**: [2503.00385](https://arxiv.org/abs/2503.00385)

---

## 18. StepFun（阶跃星辰）

### Step-3 Technical Report
- **中文标题**：Step-3 技术报告
- **英文标题**：Step-3 Technical Report
- **模型名称**：Step-3
- **发布日期**：2025-07
- **核心参数**：
  - MoE 架构
  - 多模态 (文本/图像/视频)
  - 推理效率: 3× DeepSeek-R1 推理效率
- **核心创新**：
  - 多模态原生推理
  - 高推理效率设计
- **arXiv**: [2507.19427](https://arxiv.org/abs/2507.19427)

---

## 19. Baichuan（百川智能）

### Baichuan 2 Technical Report
- **中文标题**：Baichuan 2 技术报告
- **英文标题**：Baichuan 2: Open Large-scale Language Models
- **模型名称**：Baichuan 2 (7B / 13B)
- **发布日期**：2023-09
- **核心参数**：
  - 7B / 13B Dense 架构
  - 2.6T tokens 训练
  - 中英双语
- **核心创新**：
  - 大规模高质量语料
  - 数学/代码专项优化
- **arXiv**: [2309.10305](https://arxiv.org/abs/2309.10305)

### Baichuan-M3 Technical Report (Medical)
- **中文标题**：Baichuan-M3：临床问诊建模
- **英文标题**：Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making
- **模型名称**：Baichuan-M3 (235B, 基于 Qwen3)
- **发布日期**：2026-02-06
- **核心参数**：
  - 235B 参数 (基于 Qwen3-235B-A22B 微调)
  - 医疗专用模型
  - Large Verifier System
- **核心创新**：
  - 主动信息获取 (消除歧义)
  - 长程推理 (分散证据→统一诊断)
  - 自适应幻觉抑制
  - HealthBench SOTA, 超越 GPT-5.2
- **arXiv**: [2602.06570](https://arxiv.org/abs/2602.06570)

### Baichuan-Omni Technical Report
- **中文标题**：Baichuan-Omni 全模态技术报告
- **英文标题**：Baichuan-Omni Technical Report
- **模型名称**：Baichuan-Omni (7B MLLM)
- **发布日期**：2024-10-11
- **核心参数**：
  - 7B 参数
  - 多模态 (图像/视频/音频/文本)
- **核心创新**：
  - 首个开源 7B 全模态 MLLM
  - 两阶段多模态对齐+微调
- **arXiv**: [2410.08565](https://arxiv.org/abs/2410.08565)

---

## 20. 其他值得关注的报告

### Apple Intelligence Foundation Language Models (v2, 2026-05-27)
- arXiv [2407.21075](https://arxiv.org/abs/2407.21075) v2 更新
- 包含模型架构、数据、训练过程、推理优化、评估结果、Responsible AI

### InternVL3 (2025-04-14)
- arXiv [2504.10479](https://arxiv.org/abs/2504.10479)
- 单阶段联合多模态+语言预训练

---

## 综合趋势分析

### 1. 架构趋势
| 架构 | 代表模型 | 占比趋势 |
|------|---------|---------|
| **MoE** | DeepSeek V4, GPT-5, Llama 4, Qwen3, Kimi K2, GLM-5, Step-3, Nemotron 3 | ↑↑ 主流 |
| **Hybrid Mamba-Transformer** | Nemotron 2/3 | ↑ 新方向 |
| **Dense** | Phi-4, Yi, InternLM2, Apple AFM | ↓ 小模型领域 |
| **原生多模态** | GPT-5, Llama 4, Gemini 3, Nova | ↑↑ 标配 |

### 2. 关键技术创新
- **Thinking Mode 标准化**: Qwen3 (统一 Thinking/Non-Thinking), DeepSeek R1, GPT-5 (Router-based)
- **优化器创新**: DeepSeek V4 (Muon), Kimi K2 (MuonClip)
- **上下文长度竞赛**: Llama 4 Scout 10M → DeepSeek V4/Gemini 3/Nemotron 3 1M
- **推理预算控制**: Qwen3 (Thinking Budget), Nemotron (/think token), o3 (Low/Med/High)
- **Agentic 原生设计**: Kimi K2 (Agentic 数据合成 + 环境 RL), GLM-5 (Agentic Engineering)

### 3. 开源生态
| 模型 | 开源协议 | 参数规模 |
|------|---------|---------|
| DeepSeek V4 | 自定义 (部分开源) | 1.6T MoE |
| Qwen3 | Apache 2.0 | 0.6B~235B |
| Llama 4 | 自定义 (Meta) | 109B~2T |
| Phi-4 | MIT | 14B |
| InternLM2 | Apache 2.0 | 1.8B~20B |
| Apple AFM | 未开源 | ~3B / PT-MoE |
| Kimi K2 | 开源 | 1T MoE |
| Nemotron 3 | 自定义 (NVIDIA) | 30B~Ultra |
| Yi-Lightning | 未开源 (API) | MoE |

### 4. 中国 vs 西方差异
| 维度 | 中国公司 | 西方公司 |
|------|---------|---------|
| 开源程度 | 更激进 (Qwen3 Apache 2.0, Kimi K2 开源) | 部分开源 (Meta, NVIDIA) 或闭源 (OpenAI, Anthropic) |
| Team Size | 60 authors (Qwen3) / 200+ (Kimi K2) | 较小组 (大部分 <30 作者) |
| 报告详实度 | 非常详尽, 含完整训练细节 | 较简洁, System Card 为主 |
| 价格 | 显著更低 | 较高 |
| 推理性价比 | DeepSeek R1 路径 (GRPO) | o3 路径 (Extended Thinking) |
