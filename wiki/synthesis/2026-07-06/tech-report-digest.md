---
title: 大模型技术报告综合摘要 — 2026-07-06 全面更新
type: synthesis
created: 2026-07-06
updated: 2026-07-06
sources: []
tags: [tech-report, frontier-models, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, nvidia, xai, bytedance, zhipu, moonshot, stepfun, baichuan, internlm, apple, amazon, yi]
---

# 大模型技术报告综合摘要 — 2026-07-06 全面更新

> 涵盖 22 家 AI 公司/机构最新 Tech Report / System Card，全部已通过 arXiv 或官方渠道验证。

---

## 1. DeepSeek — DeepSeek-V4

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek AI |
| **模型系列** | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| **发布日期** | 2026-06 (arXiv: 2606.19348) |
| **参数量** | Pro: 1.6T 总参 (49B 激活); Flash: 284B 总参 (13B 激活) |
| **训练数据** | 32T+ tokens |
| **上下文长度** | 1M tokens |
| **架构** | DeepSeekMoE + Hybrid Attention (CSA + HCA) + mHC 残差连接 + Muon 优化器 |
| **主要创新** | ① Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 实现百万级上下文高效推理；② Manifold-Constrained Hyper-Connections (mHC) 增强残差连接；③ Muon 优化器加速收敛；④ 1M 上下文仅需 V3.2 的 27% FLOPs 和 10% KV cache |
| **论文链接** | https://arxiv.org/abs/2606.19348 |

### DeepSeek-V3.2

| 字段 | 内容 |
|------|------|
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **发布机构** | DeepSeek AI |
| **发布日期** | 2025-12 (arXiv: 2512.02556) |
| **参数量** | 671B 总参 (37B 激活) |
| **主要创新** | 大规模 Agent 训练数据合成方法 (1800+ 环境, 85k+ 复杂指令); 推理与 Agent 性能协调优化 |
| **论文链接** | https://arxiv.org/abs/2512.02556 |

---

## 2. OpenAI — GPT-5.6 Preview / GPT-5 System Card

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 预览系统卡 |
| **英文标题** | GPT-5.6 Preview System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6 (Sol / Terra / Luna) |
| **发布日期** | 2026-06-26 |
| **参数量** | 未公开 |
| **主要创新** | 三模型家族：Sol（旗舰）、Terra（性价比）、Luna（最快/最经济）；最强大的安全防护体系；受限预览（需美国政府批准） |
| **论文链接** | https://deploymentsafety.openai.com/gpt-5-6-preview/gpt-5-6-preview.pdf |

### GPT-5 System Card

| 字段 | 内容 |
|------|------|
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **发布日期** | 2025-08-13 (arXiv: 2601.03267) |
| **模型系列** | GPT-5 (main / thinking / mini / nano) |
| **主要创新** | Unified system with real-time router; 推理与快速模型动态路由; safe-completions 安全训练 |
| **论文链接** | https://arxiv.org/abs/2601.03267 |

### GPT-5.5 System Card

| 字段 | 内容 |
|------|------|
| **英文标题** | GPT-5.5 System Card |
| **发布机构** | OpenAI |
| **发布日期** | 2026-04-23 |
| **论文链接** | https://openai.com/index/gpt-5-5-system-card/ |

---

## 3. Meta AI — Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Llama 4 模型群：原生多模态 AI 创新新时代 |
| **英文标题** | The Llama 4 Herd: The Beginning of a New Era of Natively Multimodal AI Innovation |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout / Llama 4 Maverick |
| **发布日期** | 2025-04-05 |
| **参数量** | Scout: 17B 激活 (109B 总参, 16 experts); Maverick: 17B 激活 (400B 总参, 128 experts) |
| **训练数据** | Scout: ~40T tokens; Maverick: ~22T tokens |
| **上下文长度** | Scout: 10M; Maverick: 1M |
| **架构** | MoE + Early Fusion 原生多模态 |
| **主要创新** | ① 首代原生多模态 MoE 开放模型；② Early Fusion 架构；③ Scout 支持 10M 超长上下文 (iRoPE)；④ 支持 12 种语言 |
| **论文链接** | https://ai.meta.com/research/publications/the-llama-3-herd-of-models/ (模型卡: https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md) |

---

## 4. Google DeepMind — Gemini 3 Pro

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 3 Pro 模型卡 |
| **英文标题** | Gemini 3 Pro Model Card |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3 Pro / Gemini 3.1 Pro |
| **发布日期** | 2025-11-18 (Gemini 3); 2026-02-19 (Gemini 3.1 Pro) |
| **上下文长度** | 1M tokens |
| **架构** | 原生多模态 (text/image/audio/video) |
| **主要创新** | Gemini Deep Think 科学推理模式；多模态统一 Embedding (Gemini Embedding 2)；ARC-AGI-2 验证推理能力；1M 上下文窗口 |
| **论文链接** | https://deepmind.google/models/model-cards/gemini-3-1-pro/ (模型卡: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf) |

---

## 5. Anthropic — Claude Fable 5 & Mythos 5 / Opus 4.8

### Claude Fable 5 & Mythos 5

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5 & Claude Mythos 5 系统卡 |
| **英文标题** | Claude Fable 5 & Claude Mythos 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Fable 5 / Claude Mythos 5 |
| **发布日期** | 2026-06-09 |
| **主要创新** | Fable 5 为最强大的广泛发布模型，含强安全防护；Mythos 5 为同一底层模型但移除网络/生物安全限制，仅限 Project Glasswing 合作伙伴；最强网络安全能力 |
| **论文链接** | https://www.anthropic.com/system-cards |

### Claude Opus 4.8 System Card

| 字段 | 内容 |
|------|------|
| **英文标题** | Claude Opus 4.8 System Card |
| **发布机构** | Anthropic |
| **发布日期** | 2026-05-28 |
| **主要创新** | Opus 4.7 的全面升级，软件工程、Agentic Tool Use、知识工作显著提升；Anthropic 最强的通用访问模型 |
| **论文链接** | https://www-cdn.anthropic.com/0f0c97ad20d8005706296bd92aa1c27c6b2f4f61.pdf |

### Claude Sonnet 5 System Card

| 字段 | 内容 |
|------|------|
| **英文标题** | Claude Sonnet 5 System Card |
| **发布机构** | Anthropic |
| **发布日期** | 2026-04-08 |
| **论文链接** | https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf |

---

## 6. Mistral AI — Mistral Large 3

| 字段 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 技术文档 |
| **英文标题** | Mistral Large 3 Technical Documentation |
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 / Ministral 3 (3B/8B/14B) |
| **发布日期** | 2025-12-02 |
| **参数量** | 500B-1T 总参 (15B-50B 激活); 精确: 675B 总参 (41B 激活) |
| **上下文长度** | 256K tokens |
| **架构** | Sparse MoE + 多模态 (text + image); NVIDIA H200 GPU 集群训练 |
| **主要创新** | ① 完全开源 (Apache 2.0)；② 256K 超长上下文；③ 多模态输入；④ 全线统一 256K 上下文 |
| **论文链接** | https://arxiv.org/abs/2601.08584 (Ministral 3); https://mistral.ai/news/mistral-3/ |

---

## 7. Alibaba Qwen — Qwen3 / Qwen3.5-Omni

### Qwen3

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Qwen Team, Alibaba Cloud |
| **模型系列** | Qwen3 (1.7B ~ 235B-A22B) |
| **发布日期** | 2025-04-29 (arXiv: 2505.09388) |
| **参数量** | Dense: 0.6B~32B; MoE: 30B-A3B, 235B-A22B |
| **架构** | Dense + MoE 双系列; Thinking/Non-thinking 双模式 |
| **主要创新** | ① 推理能力显著超越前代 QwQ；② 支持 100+ 语言；③ 强 Agent 能力；④ 思考/非思考无缝切换 |
| **论文链接** | https://arxiv.org/abs/2505.09388 |

### Qwen3-Max-Thinking

| 字段 | 内容 |
|------|------|
| **发布机构** | Alibaba Cloud |
| **发布日期** | 2026-01 |
| **主要创新** | 自适应工具调用 (Search/Memory/Code Interpreter); 高级 test-time scaling; 与 GPT-5.2-Thinking/Claude-Opus-4.5/Gemini 3 Pro 相当 |
| **论文链接** | https://www.alibabacloud.com/blog/pushing-qwen3-max-thinking-beyond-its-limits_602834 |

### Qwen3.5-Omni

| 字段 | 内容 |
|------|------|
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Qwen Team |
| **发布日期** | 2026-04 |
| **论文链接** | https://arxiv.org/abs/2604.15804 |

---

## 8. 01.AI (Yi) — Yi-Lightning / Yi-34B

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI (李开复) |
| **模型系列** | Yi-Lightning / Yi-Large / Yi-Coder |
| **发布日期** | Yi-34B: 2023-11; Yi-Lightning: 2024-10-16; Yi-Coder: 2024-09 |
| **参数量** | Yi-34B (Dense); Yi-Coder: 1.5B/9B; Yi-Lightning: 未公开 (API-only) |
| **主要创新** | 数据质量驱动；Yi-Lightning 在 Chatbot Arena 排名第 6，价格仅为 OpenAI 的约一半 |
| **论文链接** | https://arxiv.org/abs/2403.04652 (Yi Tech Report); https://arxiv.org/abs/2412.01253 (Yi-Lightning) |

---

## 9. Baichuan Intelligent — Baichuan-Omni-1.5 / Baichuan-M3/M4

### Baichuan-Omni-1.5

| 字段 | 内容 |
|------|------|
| **中文标题** | Baichuan-Omni-1.5 技术报告 |
| **英文标题** | Baichuan-Omni-1.5 Technical Report |
| **发布机构** | Baichuan Intelligent |
| **发布日期** | 2025-01-26 |
| **主要创新** | 全模态模型 (text/audio/vision)；端到端音频生成；500B 高质量多模态数据；多阶段训练策略 |
| **论文链接** | https://arxiv.org/abs/2501.15368 |

### Baichuan-M4

| 字段 | 内容 |
|------|------|
| **英文标题** | Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care |
| **发布机构** | Baichuan Intelligent |
| **发布日期** | 2026-06 |
| **主要创新** | 临床级医疗 Agent 系统；SPAR++ span-level reward modeling；多模态医疗感知；幻觉率降至 3.3% |
| **论文链接** | https://arxiv.org/abs/2606.08982 |

---

## 10. Microsoft — Phi-4 系列

| 字段 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report / Phi-4-reasoning-vision Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 (14B) / Phi-4-reasoning (14B) / Phi-4-reasoning-vision (15B) |
| **发布日期** | Phi-4: 2024-12; Phi-4-reasoning: 2025-04; Phi-4-reasoning-vision: 2026-03 |
| **参数量** | 14B (文本); 15B (多模态) |
| **主要创新** | 数据质量驱动的训练配方；紧凑型推理模型；开源多模态推理 |
| **论文链接** | https://arxiv.org/abs/2412.08905 (Phi-4); https://arxiv.org/abs/2504.21318 (Phi-4-reasoning); https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

---

## 11. Apple — Apple Intelligence Foundation Language Models (AFM)

| 字段 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型：2025 技术报告 |
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **发布机构** | Apple |
| **模型系列** | AFM on-device (~3B) / AFM server (更大) |
| **发布日期** | 2025-07-17 (arXiv: 2507.13575) |
| **主要创新** | 多语言多模态基础模型；设备端 + 服务器端协同；隐私保护设计 |
| **论文链接** | https://arxiv.org/abs/2507.13575 |

---

## 12. NVIDIA — Nemotron 3 系列

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3：开源高效的 MoE Hybrid Mamba-Transformer Agentic 推理模型 |
| **英文标题** | Nemotron 3 (Nano/Super/Ultra): Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA Research |
| **模型系列** | Nemotron 3 Nano / Super / Ultra / Nano Omni |
| **发布日期** | 2026-04 (Super); 2026 (Nano, Ultra, Omni) |
| **架构** | MoE + Hybrid Mamba-Transformer |
| **主要创新** | ① Mamba-Transformer 混合架构；② NVFP4 精度预训练 (1T tokens BF16 vs NVFP4 对比)；③ 高效 Agentic 推理；④ Nano Omni: 开源多模态 |
| **论文链接** | https://research.nvidia.com/labs/nemotron/ |

---

## 13. xAI — Grok 4.1 / Grok 4

### Grok 4.1 Model Card

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.1 模型卡 |
| **英文标题** | Grok 4.1 Model Card |
| **发布机构** | xAI |
| **模型系列** | Grok 4.1 (Thinking / Non-Thinking) |
| **发布日期** | 2025-11-17 |
| **主要创新** | LMArena Text Arena 排名第 1 (1483 Elo)；大规模 RL 优化风格/人格/有用性；新输入过滤模型 |
| **论文链接** | https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf |

### Grok 4.20 System Card

| 字段 | 内容 |
|------|------|
| **英文标题** | Grok 4.20 System Card |
| **发布机构** | xAI |
| **发布日期** | 2026-04-07 |
| **论文链接** | https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf |

---

## 14. Amazon — Amazon Nova 2

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **英文标题** | Amazon Nova 2: Multimodal Reasoning and Generation Models |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova 2 Lite / Pro / Omni / Sonic |
| **发布日期** | 2025-12-02 |
| **上下文长度** | 1M tokens |
| **架构** | 多模态推理与生成 (text/image/video/audio); Nova 2 Omni: 统一多模态输入+文本和图像生成; Nova 2 Sonic: 语音到语音 |
| **主要创新** | ① 动态推理 (extended thinking) 可配置平衡精度/速度/效率；② 1M token 上下文；③ 四种模型覆盖企业全场景 |
| **论文链接** | https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models |

---

## 15. Zhipu AI — GLM-5 / GLM-4.5V 系列

### GLM-5

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-5 |
| **发布日期** | 2026-02-12 (arXiv: 2602.15763) |
| **上下文长度** | 200K |
| **架构** | DSA (Dynamic Sparse Attention) 大幅降低训练/推理成本 |
| **主要创新** | ① DSA 注意力机制；② 异步强化学习基础设施 (解耦生成与训练)；③ 异步 Agent RL 算法；④ 端到端软件工程能力超越前代 |
| **论文链接** | https://arxiv.org/abs/2602.15763 |

### GLM-4.5V / GLM-4.1V-Thinking

| 字段 | 内容 |
|------|------|
| **英文标题** | GLM-4.5V and GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable RL |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-4.5V / GLM-4.1V-9B-Thinking / GLM-4.6V |
| **发布日期** | 2025-07 (arXiv: 2507.01006) |
| **主要创新** | RLCS (Reinforcement Learning with Curriculum Sampling) 训练框架；42 个公开基准 SOTA；4.1V-9B-Thinking 超越 Qwen2.5-VL-72B 在 29 个基准上 |
| **论文链接** | https://arxiv.org/abs/2507.01006 |

---

## 16. Shanghai AI Lab (InternLM) — InternLM3 / Intern-S1

### InternLM3-8B-Instruct

| 字段 | 内容 |
|------|------|
| **中文标题** | InternLM3 技术报告 |
| **英文标题** | InternLM3 (8B) |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | InternLM3-8B-Instruct |
| **发布日期** | 2025-01-15 |
| **参数量** | 8B |
| **训练数据** | 仅 4T tokens (比同类节省 75%+ 训练成本) |
| **主要创新** | ① 首次融合深度推理与普通对话于单一模型；② Thinking Density (IQPT) 数据质量指标；③ 4T 数据超越其他 18T 模型 |
| **论文链接** | https://github.com/InternLM/InternLM |

### Intern-S1

| 字段 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿级科学多模态基础模型 |
| **英文标题** | Intern-S1 (Pro): Scientific Multimodal Foundation Model at Trillion Scale |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | Intern-S1 / Intern-S1-Pro |
| **发布日期** | 2025-08 (arXiv: 2508.15763); 2026-03 (Pro, arXiv: 2603.25040) |
| **参数量** | 241B 总参 (28B 激活) |
| **架构** | MoE |
| **训练数据** | 5T tokens (2.5T+ 科学领域) |
| **主要创新** | ① 科学领域专业多模态 MoE；② Mixture of Rewards (MoR) 在线 RL；③ 分子合成/反应条件/晶体稳定性预测超越闭源模型 |
| **论文链接** | https://arxiv.org/abs/2508.15763 (S1); https://arxiv.org/abs/2603.25040 (S1-Pro) |

---

## 17. Moonshot AI (Kimi) — Kimi K2 / K2.5 / K2.6

### Kimi K2

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放 Agentic 智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **发布机构** | Moonshot AI (Kimi) |
| **模型系列** | Kimi K2 / K2-Thinking |
| **发布日期** | 2025-07 (arXiv: 2507.20534) |
| **参数量** | 1T 总参 (32B 激活) |
| **上下文长度** | 256K tokens |
| **架构** | MoE (384 experts, 8 active) + MLA 注意力 |
| **训练数据** | 15.5T tokens |
| **主要创新** | ① MuonClip 优化器 (Muon + QK-clip 解决训练不稳定)；② 大规模 Agentic 数据合成管线；③ SWE-Bench Verified 65.8, Tau2-Bench 66.1 (开源非 thinking SOTA)；④ LMSYS Arena 开源第一、总榜第五 |
| **论文链接** | https://arxiv.org/abs/2507.20534 |

### Kimi K2.5 / K2.6

| 字段 | 内容 |
|------|------|
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **发布日期** | K2.5: 2026-02; K2.6: 2026-06 |
| **参数量** | 1T 总参 (32B 激活) |
| **架构** | MoE + MoonViT 视觉编码器 (400M) + MLA |
| **主要创新** | K2.5: 原生多模态 Agent; K2.6: 长周期编码/编码驱动设计/主动自主执行/群体任务编排 |
| **论文链接** | https://arxiv.org/abs/2602.02276 (K2.5); https://huggingface.co/moonshotai/Kimi-K2.6 |

---

## 18. StepFun (阶跃星辰) — Step 3 / Step 3.5 Flash

### Step 3

| 字段 | 内容 |
|------|------|
| **中文标题** | Step-3：大规模且经济的模型-系统协同设计 |
| **英文标题** | Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step 3 |
| **发布日期** | 2025-07 (arXiv: 2507.19427) |
| **参数量** | 321B 总参 (38B 激活) |
| **上下文长度** | 65K |
| **架构** | MoE (48 experts, 3 active) + Multi-Matrix Factorization Attention (MFA) + Attention-FFN Disaggregation (AFD) |
| **主要创新** | ① MFA 低秩注意力；② AFD 解耦注意力与 FFN；③ 模型-系统协同设计降低解码成本；④ Apache 2.0 开源 |
| **论文链接** | https://arxiv.org/abs/2507.19427 |

### Step 3.5 Flash

| 字段 | 内容 |
|------|------|
| **英文标题** | Step 3.5 Flash: Fast Enough to Think. Reliable Enough to Act. |
| **发布机构** | StepFun |
| **发布日期** | 2026-02-12 |
| **主要创新** | 前沿推理 + Agent 能力；开源基础模型 |
| **论文链接** | https://static.stepfun.com/blog/step-3.5-flash/ |

---

## 19. ByteDance (Seed) — Seed2.0 / Seed1.5-VL / Seed2.1

### Seed2.0

| 字段 | 内容 |
|------|------|
| **中文标题** | Seed2.0 模型卡：面向真实世界复杂性的智能前沿 |
| **英文标题** | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity |
| **发布机构** | ByteDance Seed Team |
| **模型系列** | Seed2.0 (Pro / Lite / Mini / Code) |
| **发布日期** | 2026-02-14 |
| **主要创新** | ① 多模态理解 SOTA (MMSIBench, MotionBench, VideoMME)；② 长周期执行 / plan-act-reflect 循环；③ 成本降低约一个数量级；④ 工作流导向的 MaaS 基础 |
| **论文链接** | https://seed.bytedance.com/seed2 (PDF: Seed2.0 Model Card) |

### Seed2.1

| 字段 | 内容 |
|------|------|
| **英文标题** | Seed 2.1 |
| **发布机构** | ByteDance Seed Team |
| **发布日期** | 2026-06-23 |
| **主要创新** | 推进 AI 生产力 |
| **论文链接** | https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity |

---

## 20. DeepSeek — 其他相关

### DeepSeek V3

| 字段 | 内容 |
|------|------|
| **英文标题** | DeepSeek-V3 Technical Report |
| **发布机构** | DeepSeek AI |
| **发布日期** | 2024-12-27 |
| **参数量** | 671B 总参 (37B 激活) |
| **架构** | MoE + Multi-Token Prediction (MTP) + MLA |
| **论文链接** | https://arxiv.org/abs/2412.19437 |

---

## 21. Anthropic — Claude Opus 4 / Sonnet 4 系列 (早期)

### Claude Opus 4 / Sonnet 4

| 字段 | 内容 |
|------|------|
| **英文标题** | Claude Opus 4 / Sonnet 4 System Cards |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4 / Claude Sonnet 4 / Claude 4 Haiku |
| **发布日期** | 2025 系列 |
| **论文链接** | https://www.anthropic.com/system-cards |

---

## 22. Meta AI — Llama 3

| 字段 | 内容 |
|------|------|
| **英文标题** | The Llama 3 Herd of Models |
| **发布机构** | Meta AI |
| **模型系列** | Llama 3 (8B / 70B / 405B) |
| **发布日期** | 2024-07 (arXiv: 2407.21783) |
| **参数量** | 8B / 70B / 405B (Dense) |
| **主要创新** | 大规模开放模型；多语言/编码/推理/工具使用 |
| **论文链接** | https://arxiv.org/abs/2407.21783 |

---

## 按主题交叉分析

### 1. 大模型新架构 (MoE, Mamba, Hybrid)

| 机构 | 模型 | 架构类型 | 亮点 |
|------|------|----------|------|
| DeepSeek | V4 | MoE + Hybrid Attention (CSA+HCA) | 百万级上下文高效稀疏注意力 |
| Meta | Llama 4 | MoE + Early Fusion | 原生多模态 MoE |
| Mistral | Large 3 | Sparse MoE | Apache 2.0 开源 |
| Qwen | Qwen3 | Dense + MoE 双系列 | 灵活部署选择 |
| Moonshot | K2/K2.5 | MoE + MLA | MuonClip 优化器 |
| StepFun | Step 3 | MoE + MFA + AFD | 模型-系统协同设计 |
| NVIDIA | Nemotron 3 | MoE + Hybrid Mamba-Transformer | 首个开源 Mamba-Transformer 混合 |
| Shanghai AI Lab | Intern-S1 | MoE + MoR | 科学领域专业 MoE |

### 2. 训练方法 (Pre-training, Post-training, Alignment, RL)

| 机构 | 方法 | 创新点 |
|------|------|--------|
| DeepSeek | Muon 优化器 | V4 使用 Muon 加速收敛 + 训练稳定性 |
| Moonshot | MuonClip | QK-clip 改进 Muon, 15.5T tokens 零 loss spike |
| Zhipu AI | 异步 RL | 解耦生成与训练, 异步 Agent RL 算法 |
| ByteDance | Seed2.0 | plan-act-reflect 迭代循环 |
| xAI | 大规模 RL | 使用 frontier agentic 模型作为 reward model |
| Shanghai AI Lab | MoR | Mixture of Rewards 在线 RL |
| OpenAI | Safe-completions | 安全训练新方法 |

### 3. Scaling Law / 缩放分析

| 机构 | 观点/发现 |
|------|-----------|
| DeepSeek | V4 在 1M 上下文仅需 27% FLOPs, scaling 更高效 |
| InternLM3 | 4T 高质量数据 > 18T 普通数据, IQPT 数据质量指标打破 scaling law 瓶颈 |
| StepFun | 模型-系统协同设计, 以系统优化突破单一模型 scaling |

### 4. 多模态模型

| 机构 | 模型 | 模态 |
|------|------|------|
| Meta | Llama 4 | text + image (Early Fusion) |
| Google | Gemini 3 Pro | text + image + audio + video |
| Qwen | Qwen3.5-Omni | text + image + audio + video |
| Moonshot | K2.5/K2.6 | text + image + video (MoonViT) |
| ByteDance | Seed2.0 | text + image + video + spatial |
| NVIDIA | Nemotron 3 Omni | text + image + 多模态 |
| Baichuan | Omni-1.5 | text + audio + vision (端到端音频生成) |
| Zhipu | GLM-4.5V | text + image + video (AIMv2 + 3D conv) |
| StepFun | Step 3 | text + image (多模态推理) |
| Apple | AFM | multilingual + multimodal |

### 5. 长上下文模型

| 机构 | 模型 | 上下文长度 | 技术 |
|------|------|------------|------|
| Meta | Llama 4 Scout | 10M | iRoPE |
| DeepSeek | V4 | 1M | CSA + HCA |
| Google | Gemini 3 Pro | 1M | - |
| Amazon | Nova 2 | 1M | - |
| Mistral | Large 3 | 256K | - |
| Moonshot | K2 | 256K | MLA |
| Zhipu | GLM-5 | 200K | DSA |

### 6. 推理模型 / Reasoning Model

| 机构 | 模型 | 推理方式 |
|------|------|----------|
| OpenAI | GPT-5.6 Sol | 旗舰推理 (受限预览) |
| Anthropic | Claude Fable 5 / Mythos 5 | 深度推理 + 安全控制 |
| xAI | Grok 4.1 Thinking | 双模式 (Thinking/Non-Thinking) |
| Qwen | Qwen3-Max-Thinking | 自适应工具 + test-time scaling |
| DeepSeek | V4-Pro-Max | 最大推理努力模式 |
| Moonshot | K2-Thinking / K2.5-Thinking | 思考模式 |
| Microsoft | Phi-4-reasoning | 紧凑推理模型 |
| Google | Gemini Deep Think | 科学推理深度思考模式 |
| StepFun | Step 3.5 Flash | 快速推理 + Agent |

---

## 趋势总结

1. **MoE 全面主导**: 2025-2026 年度几乎所有前沿模型都采用 MoE 架构 (DeepSeek-V4, Llama 4, Mistral Large 3, Qwen3, K2, Step 3, Intern-S1, GLM-5)，仅少数小型/专用模型保留 Dense 架构。

2. **架构创新加速**: 从标准 MoE Transformer 向 Hybrid 架构演进 — NVIDIA Nemotron 3 的 Mamba-Transformer 混合、DeepSeek-V4 的压缩稀疏注意力、GLM-5 的动态稀疏注意力、Step 3 的多矩阵分解注意力。

3. **推理模型成为标配**: Thinking/Non-thinking 双模式已成为行业标准 (GPT-5.6, Claude 4/5, Grok 4.1, Qwen3, K2, Gemini 3 Pro, Phi-4-reasoning)，通过 test-time compute scaling 实现推理深度可调。

4. **后训练 RL 深化**: 从简单 RLHF 演进到异步 RL、MoR、MuonClip 等高级 RL 训练方法；Agentic RL 成为独立训练阶段 (GLM-5, K2)。

5. **多模态原生融合**: Early Fusion (Llama 4)、原生多模态 (Gemini 3)、统一多模态 embedding (Gemini Embedding 2) 成为趋势。

6. **长上下文军备竞赛**: 10M (Llama 4 Scout) → 1M (DeepSeek V4, Gemini 3, Amazon Nova 2) → 256K (Mistral Large 3, K2) 成为主流。

7. **开放模型逼近闭源**: DeepSeek-V4, Llama 4, Qwen3, Mistral Large 3, Kimi K2/K2.5, GLM-5, Step 3 等开放权重模型在多项基准上接近或超越 GPT-5/Claude 4 系列闭源模型。

8. **数据效率革命**: InternLM3 以 4T tokens 超越 18T 模型，验证数据质量 > 数据数量；DeepSeek 的 Muon 优化器加快收敛。
