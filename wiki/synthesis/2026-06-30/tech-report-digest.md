---
title: "大模型技术报告摘要 — LLM Tech Report Digest (2026-06-30)"
type: synthesis
created: 2026-06-30
updated: 2026-06-30
tags: [llm, tech-report, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, nvidia, xai, amazon, zhipu, kimi, bytedance]
sources: []
---

# 大模型技术报告摘要 — LLM Tech Report Digest

> 截至 2026 年 6 月 30 日，全球主要 AI 公司最新发布的大模型技术报告汇总。
> 聚焦：MoE 架构、训练方法、Scaling Law、多模态、长上下文、推理模型。

---

## 1. DeepSeek — DeepSeek-V4

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：面向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek AI |
| **模型名称** | DeepSeek-V4-Pro, DeepSeek-V4-Flash |
| **发布日期** | 2026-04-24 |
| **参数量** | V4-Pro: 1.6T 总参数, 49B 激活; V4-Flash: 284B 总参数, 13B 激活 |
| **训练数据** | 32T+ tokens |
| **上下文长度** | 1M tokens（默认） |
| **架构** | MoE + Hybrid Attention (CSA + HCA) |
| **主要创新** | (1) 混合注意力架构：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)，1M 上下文下 V4-Pro 仅需 V3.2 的 27% FLOPs 和 10% KV Cache; (2) Manifold-Constrained Hyper-Connections (mHC) 改进残差连接; (3) Muon 优化器加速收敛; (4) 支持国产芯片（华为昇腾）推理 |
| **arXiv** | https://arxiv.org/html/2606.19348 |

---

## 2. OpenAI — GPT-5 System Card

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型名称** | GPT-5 (gpt-5-main, gpt-5-thinking, gpt-5-thinking-pro) |
| **发布日期** | 2025-08-07 |
| **参数量** | 未公开（推测为密集 Transformer + MoE 混合） |
| **训练数据** | 未公开 |
| **上下文长度** | 未公开（推理时支持长 CoT） |
| **架构** | 统一系统：快速模型 + 深度推理模型 + 实时路由器；Router 可持续从用户信号学习 |
| **主要创新** | (1) 统一系统设计：根据问题复杂度自动路由到 main/thinking 模式; (2) 幻觉率比 o3 降低约 6 倍; (3) safe-completions 安全训练新方法; (4) gpt-5-thinking-pro 使用并行 test-time compute |
| **arXiv** | https://arxiv.org/abs/2601.03267 |

---

## 3. Meta AI — Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Llama 4 模型卡 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型名称** | Llama 4 Scout (17Bx16E), Llama 4 Maverick (17Bx128E) |
| **发布日期** | 2025-04-05 |
| **参数量** | Scout: 109B 总, 17B 激活; Maverick: 400B 总, 17B 激活 |
| **训练数据** | Scout: ~40T tokens; Maverick: ~22T tokens |
| **上下文长度** | Scout: 10M; Maverick: 1M |
| **架构** | MoE + Early Fusion 原生多模态 |
| **主要创新** | (1) 原生多模态 MoE，早期融合图像与文本; (2) Scout 支持 10M token 上下文（iRoPE 长度泛化）; (3) Scout 可在单张 H100 上运行（INT4 量化）; (4) 训练管线：Pre-training → Mid-training (长上下文) → Lightweight SFT → Online RL → Lightweight DPO |
| **arXiv** | https://arxiv.org/abs/2601.11659 (已撤回, 见 Zenodo) |

---

## 4. Google DeepMind — Gemini 2.5

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5：以高级推理、多模态、长上下文和下一代 Agent 能力推动前沿 |
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **发布机构** | Google DeepMind |
| **模型名称** | Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.0 Flash, Gemini 2.0 Flash-Lite |
| **发布日期** | 2025-03 (Pro Experimental), 2025-06 (GA) |
| **参数量** | 未公开 |
| **训练数据** | 未公开 |
| **上下文长度** | 1M tokens (Pro & Flash), 2M coming |
| **架构** | Thinking Model（所有模型内置推理能力） |
| **主要创新** | (1) "Thinking" 模型，所有模型默认具备推理能力; (2) 原生多模态（文本/音频/图像/视频）; (3) 支持 3 小时视频理解; (4) Agentic 工作流; (5) 3435 位作者（最大规模技术报告之一） |
| **arXiv** | https://arxiv.org/abs/2507.06261 |

---

## 5. Anthropic — Claude 系列 System Cards

### 5.1 Claude Opus 4 & Sonnet 4 (May 2025)

| 字段 | 内容 |
|------|------|
| **英文标题** | System Card: Claude Opus 4 & Claude Sonnet 4 |
| **发布日期** | 2025-05 |
| **架构** | Hybrid Reasoning LLM |
| **主要创新** | Opus 4 部署于 ASL-3 标准; Sonnet 4 部署于 ASL-2; 首次包含 alignment assessment 和 model welfare assessment; 强大的 computer use 和 coding 能力 |
| **链接** | https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf |

### 5.2 Claude Opus 4.8 (May 2026)

| 字段 | 内容 |
|------|------|
| **英文标题** | System Card: Claude Opus 4.8 |
| **发布日期** | 2026-05-28 |
| **参数量/上下文** | 未公开; 1M token 上下文; 128K 最大输出 |
| **主要创新** | Opus 系列最强通用模型; 自适应思考 (adaptive thinking); Fast Mode (2.5x 输出速度); 最小可缓存 prompt 长度降至 1024 tokens; 在软件工程、agentic 任务、知识工作上全面超越 Opus 4.7 |
| **链接** | https://www-cdn.anthropic.com/0f0c97ad20d8005706296bd92aa1c27c6b2f4f61.pdf |

### 5.3 Claude Fable 5 & Mythos 5 (June 2026)

| 字段 | 内容 |
|------|------|
| **英文标题** | System Card: Claude Fable 5 and Mythos 5 |
| **发布日期** | 2026-06-09 |
| **上下文长度** | 1M tokens; 128K 最大输出 |
| **架构** | Anthropic 第 5 代旗舰模型 |
| **主要创新** | Fable 5 是 Anthropic 最强大的公开发布模型，含安全分类器（生物/化学/网络）；Mythos 5 为同模型去除安全限制版本，仅限 Glasswing 合作伙伴；支持 Task Budgets、Memory Tool、Code Execution |
| **链接** | https://www.anthropic.com/system-cards |

---

## 6. Mistral AI — Ministral 3 & Medium 3.5

### 6.1 Ministral 3 (Jan 2026)

| 字段 | 内容 |
|------|------|
| **英文标题** | Ministral 3 |
| **发布机构** | Mistral AI |
| **模型名称** | Ministral 3 (3B/8B/14B) — Base/Instruct/Reasoning 各三种 |
| **发布日期** | 2026-01-13 |
| **参数量** | 3B, 8B, 14B（密集 Dense） |
| **上下文长度** | 256K tokens |
| **架构** | Dense Transformer + Vision |
| **主要创新** | (1) Cascade Distillation：迭代剪枝 + 持续训练 + 蒸馏; (2) 每个尺寸三种变体（Base/Instruct/Reasoning）; (3) 发现"capacity gap"——更强的教师不一定产生更强的学生; (4) Apache 2.0 开源 |
| **arXiv** | https://arxiv.org/abs/2601.08584 |

### 6.2 Mistral Medium 3.5 (May 2026)

| 字段 | 内容 |
|------|------|
| **英文标题** | Mistral Medium 3.5 |
| **发布机构** | Mistral AI |
| **模型名称** | Mistral Medium 3.5 |
| **发布日期** | 2026-05-22 |
| **参数量** | 128B Dense |
| **上下文长度** | 256K |
| **主要创新** | 首个旗舰"merged model"——指令跟随、推理、编码统一于单套权重；可配置推理 effort；从头训练视觉编码器；SWE-Bench Verified 77.6% |
| **链接** | https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5/ |

---

## 7. Alibaba Qwen — Qwen3 & Qwen3.5-Omni

### 7.1 Qwen3 (April 2025)

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba Qwen Team |
| **模型名称** | Qwen3 系列（Dense: 0.6B~32B; MoE: 30B-A3B, 235B-A22B） |
| **发布日期** | 2025-04-29 |
| **参数量** | 0.6B ~ 235B（旗舰: 235B 总, 22B 激活 MoE） |
| **训练数据** | 36T tokens |
| **上下文长度** | 128K~256K（后续更新到 1M） |
| **架构** | Dense + MoE（Hybrid Reasoning） |
| **主要创新** | (1) 统一 thinking/non-thinking 模式; (2) Thinking Budget 机制; (3) 多语言从 29 → 119 种语言; (4) 四阶段训练：长 CoT cold start → Reasoning RL → Thinking mode fusion → General RL |
| **arXiv** | https://arxiv.org/abs/2505.09388 |

### 7.2 Qwen3.5-Omni (April 2026)

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba Qwen Team |
| **模型名称** | Qwen3.5-Omni (Plus, Flash) |
| **发布日期** | 2026-04-17 |
| **参数量** | 数百亿（Hybrid Attention MoE） |
| **训练数据** | 文本-视觉对 + 1 亿小时音视频数据 |
| **上下文长度** | 256K |
| **架构** | Hybrid-Attention MoE (Thinker + Talker) |
| **主要创新** | (1) 全模态（文本/图像/音频/视频）原生 Agent; (2) ARIA 自适应语音对齐; (3) Audio-Visual Vibe Coding; (4) 10h+ 音频、400s 视频理解; (5) 113 种语音识别语言 |
| **arXiv** | https://arxiv.org/abs/2604.15804 |

---

## 8. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型名称** | Yi-Lightning |
| **发布日期** | 2024-12-02 |
| **参数量** | 未公开（MoE 架构） |
| **架构** | 增强 MoE（高级专家分割与路由 + 优化 KV-Cache） |
| **主要创新** | (1) Chatbot Arena 综合第 6 名，中文/数学/编程子项第 2-4 名; (2) RAISE 安全框架（四组件）; (3) 多阶段训练 + 合成数据 + 奖励建模; (4) 训练/推理成本显著降低 |
| **arXiv** | https://arxiv.org/abs/2412.01253 |

---

## 9. Baichuan — Baichuan-M3

| 字段 | 内容 |
|------|------|
| **中文标题** | Baichuan-M3：面向可靠临床决策的医疗大模型 |
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | Baichuan Intelligence |
| **模型名称** | Baichuan-M3-235B |
| **发布日期** | 2026-02-06 |
| **参数量** | 235B |
| **架构** | 医疗增强 LLM（基于 Transformer） |
| **主要创新** | (1) 从被动问答转向主动临床决策支持; (2) HealthBench 超越 GPT-5.2; (3) Fact-Aware RL 框架降低幻觉率至 3.3%; (4) W4 量化降低 74% 显存; (5) Gated Eagle3 投机解码 96% 加速 |
| **arXiv** | https://arxiv.org/abs/2602.06570 |

---

## 10. Microsoft — Phi-4 系列

### 10.1 Phi-4 (Dec 2024)

| 字段 | 内容 |
|------|------|
| **英文标题** | Phi-4 Technical Report |
| **模型名称** | Phi-4 (14B) |
| **发布日期** | 2024-12 |
| **参数量** | 14B Dense |
| **主要创新** | 以数据质量为中心的训练配方；大量使用合成数据；多代理提示、自修正、指令反转等数据生成方法；在 STEM QA 上超越教师模型 GPT-4 |
| **链接** | https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/ |

### 10.2 Phi-4-reasoning (April 2025)

| 字段 | 内容 |
|------|------|
| **英文标题** | Phi-4-reasoning Technical Report |
| **模型名称** | Phi-4-reasoning (14B), Phi-4-reasoning-plus |
| **发布日期** | 2025-04 |
| **主要创新** | 基于 Phi-4 的推理模型；SFT on "teachable" prompts + o3-mini 生成的推理链；outcome-based RL 进一步提升；超越 DeepSeek-R1-Distill-Llama-70B；接近完整版 DeepSeek R1 |
| **arXiv** | https://arxiv.org/abs/2504.21318 |

### 10.3 Phi-4-reasoning-vision (March 2026)

| 字段 | 内容 |
|------|------|
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **模型名称** | Phi-4-reasoning-vision (15B) |
| **发布日期** | 2026-03-04 |
| **参数量** | 15B |
| **主要创新** | 紧凑多模态推理模型；动态分辨率编码器；混合推理/非推理数据 + 模式 token；在科学/数学推理和 UI 理解上表现出色 |
| **链接** | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

---

## 11. Apple — Apple Intelligence Foundation Language Models

| 字段 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型技术报告 2025 |
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **发布机构** | Apple |
| **模型名称** | On-device (~3B) + Server (PT-MoE) |
| **发布日期** | 2025-07-17 |
| **参数量** | On-device: ~3B; Server: 未公开（PT-MoE） |
| **架构** | On-device: 密集 KV-cache sharing + 2-bit QAT; Server: Parallel-Track MoE (PT-MoE) |
| **主要创新** | (1) On-device 模型：KV-cache sharing、2-bit 量化感知训练; (2) Server 模型：PT-MoE（track parallelism + MoE + interleaved global-local attention）; (3) Private Cloud Compute; (4) Swift Foundation Models framework |
| **arXiv** | https://arxiv.org/abs/2507.13575 |

---

## 12. NVIDIA — Nemotron 3 系列

### 12.1 Nemotron 3 Nano (30B-A3B)

| 字段 | 内容 |
|------|------|
| **英文标题** | Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model |
| **参数量** | 30B 总, 3B 激活 |
| **训练数据** | 25T tokens |
| **上下文** | 1M tokens |
| **主要创新** | MoE + Hybrid Mamba-Attention; 3.3x 推理吞吐 vs Qwen3-30B; Agentic + Reasoning 优化 |
| **链接** | https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf |

### 12.2 Nemotron 3 Super (120B-A12B)

| 字段 | 内容 |
|------|------|
| **英文标题** | Nemotron 3 Super: Open, Efficient Hybrid Mamba-Transformer MoE |
| **参数量** | 120B 总, 12B 激活 |
| **训练数据** | 25T tokens |
| **主要创新** | LatentMoE + MTP + NVFP4 预训练; 2.2x 推理吞吐 vs Qwen3.5-122B |
| **arXiv** | https://arxiv.org/abs/2604.12374 |

### 12.3 Nemotron 3 Ultra (550B-A55B) — 旗舰

| 字段 | 内容 |
|------|------|
| **英文标题** | Nemotron 3 Ultra: Open, Efficient MoE Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **参数量** | 550B 总, 55B 激活 |
| **训练数据** | 20T tokens |
| **上下文** | 1M tokens |
| **主要创新** | (1) LatentMoE + MTP + NVFP4; (2) 混合 Mamba-Attention; (3) ~6x 推理吞吐 vs 同级模型; (4) Multi-environment RLVR + MOPD + reasoning budget control |
| **arXiv** | https://arxiv.org/html/2606.15007 |

---

## 13. xAI — Grok 3 & Grok 4

### 13.1 Grok 3 (Feb 2025)

| 字段 | 内容 |
|------|------|
| **英文标题** | Grok 3 Beta — The Age of Reasoning Agents |
| **发布机构** | xAI |
| **模型名称** | Grok 3, Grok 3 mini (Think) |
| **发布日期** | 2025-02-19 |
| **上下文长度** | 131K tokens |
| **架构** | Transformer (Decoder-only) + RL at-scale |
| **主要创新** | Colossus 超算集群 (10x 前代算力); 大规模 RL 训练推理能力; Chatbot Arena Elo 1402 |
| **链接** | https://x.ai/news/grok-3 |

### 13.2 Grok 4 (July 2025)

| 字段 | 内容 |
|------|------|
| **英文标题** | Grok 4 Model Card |
| **发布机构** | xAI |
| **模型名称** | Grok 4, Grok 4 Heavy, Grok 4 Fast |
| **发布日期** | 2025-07-09 |
| **上下文长度** | 256K tokens |
| **主要创新** | (1) 原生工具使用（RL 训练）; (2) Grok 4 Heavy: 并行 test-time compute, 首个在 Humanity's Last Exam 上达到 50.7%; (3) USAMO'25 61.9%; (4) ARC-AGI V2 15.9% |
| **链接** | https://data.x.ai/2025-08-20-grok-4-model-card.pdf |

---

## 14. Amazon — Amazon Nova 系列

### 14.1 Amazon Nova (Dec 2024) + Nova Premier (April 2025)

| 字段 | 内容 |
|------|------|
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型名称** | Nova Micro, Lite, Pro, Premier, Canvas (图像), Reel (视频) |
| **发布日期** | 2024-12-03 (Nova); 2025-04-30 (Premier) |
| **上下文长度** | Premier 支持 1M tokens |
| **主要创新** | Premier 为教师模型用于蒸馏; Multimodal (text/image/video); 注重成本效益 |
| **链接** | https://www.amazon.science/publications/the-amazon-nova-family-of-models-technical-report-and-model-card |

### 14.2 Amazon Nova 2 (Dec 2025)

| 字段 | 内容 |
|------|------|
| **英文标题** | Amazon Nova 2: Multimodal reasoning and generation models |
| **模型名称** | Nova 2 Lite, Pro, Omni, Sonic |
| **发布日期** | 2025-12-02 |
| **上下文长度** | 1M tokens |
| **主要创新** | (1) 动态推理（extended thinking 可配置）; (2) Nova 2 Omni: 统一多模态输入 + 文本/图像输出; (3) Nova 2 Sonic: 语音到语音基础模型 |
| **链接** | https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models |

---

## 15. Zhipu AI — GLM-5

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: from Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型名称** | GLM-5 (744B-A40B) |
| **发布日期** | 2026-02-12 |
| **参数量** | 744B 总, 40B 激活 |
| **训练数据** | 28.5T tokens |
| **上下文长度** | 200K |
| **架构** | MoE + DeepSeek Sparse Attention (DSA) |
| **主要创新** | (1) 采用 DeepSeek Sparse Attention (DSA) 降低部署成本; (2) 异步 RL 基础设施 "slime" 框架; (3) 三阶段 RL：Reasoning RL → Agentic RL → General RL; (4) On-Policy Cross-Stage Distillation 防止遗忘 |
| **arXiv** | https://arxiv.org/abs/2602.15763 |

---

## 16. Shanghai AI Lab — InternLM3

| 字段 | 内容 |
|------|------|
| **中文标题** | InternLM3 技术报告 |
| **英文标题** | InternLM3 |
| **发布机构** | Shanghai AI Laboratory |
| **模型名称** | InternLM3-8B-Instruct |
| **发布日期** | 2025-01-15 |
| **参数量** | 8B |
| **训练数据** | 仅 4T tokens（比同类节省 75%+ 成本） |
| **架构** | Dense Transformer（深度思考 + 正常对话统一） |
| **主要创新** | (1) 数据效率革命：仅 4T tokens 达到 18T 水平; (2) IQPT (Intelligence Quality per Token) 概念; (3) 首次在通用模型中融合深度推理与日常对话; (4) 世界知识树驱动合成数据 |
| **链接** | https://internlm.readthedocs.io/en/latest/model_card/InternLM3.html |

---

## 17. Moonshot AI — Kimi K2 & K2.5

### 17.1 Kimi K2 (July 2025)

| 字段 | 内容 |
|------|------|
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **模型名称** | Kimi K2 (1T-A32B) |
| **发布日期** | 2025-07-28 |
| **参数量** | 1T 总, 32B 激活 |
| **训练数据** | 15.5T tokens |
| **上下文长度** | 128K (后续更新至 256K) |
| **架构** | MoE + MLA |
| **主要创新** | (1) MuonClip 优化器（Muon + QK-clip）解决训练不稳定; (2) 大规模 agentic 数据合成管线; (3) 联合 RL 训练（真实 + 合成环境）; (4) SWE-Bench Verified 65.8%, Tau2-Bench 66.1 |
| **arXiv** | https://arxiv.org/abs/2507.20534 |

### 17.2 Kimi K2.5 (Feb 2026)

| 字段 | 内容 |
|------|------|
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **模型名称** | Kimi K2.5 (1T-A32B + MoonViT 视觉编码器) |
| **发布日期** | 2026-02-02 |
| **参数量** | 1T 总, 32B 激活 + 400M 视觉编码器 |
| **上下文长度** | 256K |
| **主要创新** | (1) 联合文本-视觉预训练 + Zero-Vision SFT + 联合文本-视觉 RL; (2) Agent Swarm 并行编排框架（最高 4.5x 延迟降低）; (3) 原生多模态 agentic 模型 |
| **arXiv** | https://arxiv.org/abs/2602.02276 |

---

## 18. StepFun (阶跃星辰) — Step 系列

| 字段 | 内容 |
|------|------|
| **中文标题** | Step-2 万亿参数 MoE 语言大模型 |
| **英文标题** | Step-2: Trillion-Parameter MoE Language Model |
| **发布机构** | 阶跃星辰 (StepFun) |
| **模型名称** | Step-2, Step-2 mini |
| **发布日期** | 2024-07 (Step-2 正式版), 2026 (Step-2 mini) |
| **参数量** | Step-2: 万亿级 MoE; Step-2 mini: 轻量级（3% 参数保留 80%+ 性能） |
| **架构** | MoE + MFA (Multi-Matrix Factorization Attention, Step-2 mini) |
| **主要创新** | (1) 国内创业公司首个万亿参数 MoE; (2) 6D 并行训练; (3) MFA 注意力架构（节省 94% KV Cache）; (4) LiveBench 国内第一、全球第五 |
| **链接** | https://www.stepfun.com/ |

---

## 19. ByteDance Seed — Seed2.0

| 字段 | 内容 |
|------|------|
| **中文标题** | Seed2.0 模型卡：面向真实世界复杂性的智能前沿 |
| **英文标题** | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity |
| **发布机构** | ByteDance Seed Team |
| **模型名称** | Seed2.0 (Pro, Lite, Mini, Code) |
| **发布日期** | 2026-02-14 |
| **参数量** | 未公开（MoE 架构） |
| **训练数据** | 大规模多模态数据（10x 级增长） |
| **上下文长度** | 长上下文（支持数小时视频） |
| **架构** | MoE LLM + 视觉编码器 |
| **主要创新** | (1) 系统级优化支持大规模生产; (2) 奥数级数学（IMO/CMO 金牌水平）; (3) 多模态理解 SOTA (MMSIBench, MotionBench, VideoMME); (4) Plan-Act-Reflect 自主 agent 循环; (5) 成本降低约 1 个数量级 |
| **链接** | https://github.com/ByteDance-Seed/Seed2.0 |

---

## 对比概览

### MoE 架构采用情况

| 公司 | 模型 | 总参数 | 激活参数 | 架构特色 |
|------|------|--------|---------|---------|
| DeepSeek | V4-Pro | 1.6T | 49B | CSA + HCA 混合注意力 |
| Meta | Llama 4 Maverick | 400B | 17B | Early Fusion 原生多模态 |
| Qwen | Qwen3-235B-A22B | 235B | 22B | Thinking/Non-thinking 统一 |
| NVIDIA | Nemotron 3 Ultra | 550B | 55B | Mamba-Attention Hybrid |
| Zhipu | GLM-5 | 744B | 40B | DSA 稀疏注意力 |
| Moonshot | Kimi K2 | 1T | 32B | MLA + MuonClip |
| StepFun | Step-2 | ~1T | ~100B+ | 异构专家设计 |
| ByteDance | Seed2.0 | 未公开 | 未公开 | 系统级优化 |
| Apple | Server PT-MoE | 未公开 | 未公开 | Track Parallelism |

### 推理模型 (Reasoning/Thinking)

| 公司 | 模型 | 方式 |
|------|------|------|
| OpenAI | GPT-5 thinking | Router 自动选择 |
| Google | Gemini 2.5 | 内置 thinking |
| Anthropic | Claude Opus 4+ | Hybrid reasoning |
| Qwen | Qwen3 | Thinking/Non-thinking 统一框架 |
| DeepSeek | V4 | Thinking mode |
| xAI | Grok 3/4 Think | RL-trained reasoning |

### 长上下文 (≥1M tokens)

| 公司 | 模型 | 上下文长度 |
|------|------|-----------|
| Meta | Llama 4 Scout | 10M |
| DeepSeek | V4-Pro/V4-Flash | 1M |
| Google | Gemini 2.5 Pro | 1M (2M coming) |
| Anthropic | Claude Opus 4.8 | 1M |
| NVIDIA | Nemotron 3 Ultra | 1M |
| Amazon | Nova Premier/2 | 1M |
| Qwen | Qwen3 (2507 update) | 1M |

---

## 关键趋势总结

1. **MoE 成为主流**：几乎所有前沿模型都采用 MoE 架构，DeepSeek-V4 (1.6T)、Kimi K2 (1T)、GLM-5 (744B) 等持续推高总参数量
2. **推理模型融合**：2025-2026 年最大趋势——thinking 模式从独立模型变为统一框架的内置能力（Qwen3, GPT-5, Gemini 2.5）
3. **Mamba-Attention Hybrid**：NVIDIA Nemotron 3 系列引领的状态空间模型 + Attention 混合架构
4. **长上下文成为标配**：1M token 以上上下文已成为前沿模型的标准配置
5. **Agentic 优化**：几乎所有报告都将 agentic 能力（工具使用、编码、多步推理）作为核心优化目标
6. **数据质量 > 数量**：InternLM3 (4T 达 18T 水平)、Phi-4（合成数据驱动）等证明数据质量的关键作用
7. **多模态原生**：Llama 4 等模型将视觉理解作为原生能力集成，而非后期拼接
8. **RL 训练创新**：异步 RL (GLM-5 slime)、Muon/MuonClip 优化器 (DeepSeek, Kimi)、Multi-environment RLVR (NVIDIA) 等新方法涌现

---

*报告编制日期：2026-06-30*
*来源：各公司官方技术报告、arXiv、模型卡、官方博客*
