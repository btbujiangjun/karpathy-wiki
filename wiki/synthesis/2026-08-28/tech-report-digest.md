---
title: "LLM Tech Report Digest — 2026-08-28"
type: synthesis
created: 2026-08-28
updated: 2026-08-28
tags: [tech-report, llm, moe, mamba, multimodal, reasoning, scaling, digest]
sources: []
---

# LLM Tech Report Digest — 2026-08-28

> 最近半年主流厂商 LLM 技术报告/系统卡摘要，附核心参数、架构创新与链接。
> Last updated: 2026-08-28

---

## 目录 / Table of Contents

| # | 机构 | 模型 | 发布日期 | 核心架构 |
|---|------|------|----------|----------|
| 1 | DeepSeek | DeepSeek-V4 (Pro/Flash) | 2026-06~08 | MoE 1.6T/49B + CSA/HCA |
| 2 | OpenAI | GPT-5.6 (Sol/Terra/Luna) / GPT-5 | 2025-08~2026-07 | Closed, Router 架构 |
| 3 | Meta AI | Muse Glimmer 30B / Llama 4 | 2026-08 | 多模态 agent 模型 (DFlash) |
| 4 | Google DeepMind | Gemini 3.1 Pro | 2026-02 | 1M ctx, 64K 输出 |
| 5 | Anthropic | Claude Fable 5 / Mythos 5 | 2026-06 | Closed, ASL-3 blocker |
| 6 | Mistral AI | Shieldstral / Small 4 | 2026-08 | 3B 多模态安全分类器 |
| 7 | Qwen (Alibaba) | Qwen3.5-397B-A17B / Omni | 2026 | Hybrid Attention MoE, ARIA |
| 8 | Microsoft | Phi-4-reasoning-vision-15B / Phi-5 | 2026-03 | Dense + 视觉推理 |
| 9 | NVIDIA | Nemotron 3.5 Lightning | 2026-08-11 | 30B MoE agentic |
| 10 | xAI | Grok 4.6 | 2026-08-12 | 1.5T 家族, closed |
| 11 | Amazon | Nova family | 2024 | 多模态多任务 |
| 12 | Zhipu AI | GLM-5.3 | 2026-08-14 | Coding 聚焦, 后训练 Scaling |
| 13 | Moonshot AI | Kimi K3 | 2026-07-27 | 2.8T/104B MoE, Delta Attention |
| 14 | StepFun | Step3 | 2025-07 | MFA + AFD |
| 15 | ByteDance | Seed2.0 (Doubao-Seed-2.0-pro) | 2026 | MoE MaaS |
| 16 | Baichuan | Baichuan-M4 | 2026-06-09 | 临床医疗 agent, SPAR++ |
| 17 | InternLM (上海AI Lab) | InternLM3-8B | 2025-01 | 轻量高效 |
| 18 | 01.AI | Yi-Lightning | 2024-12 | Enhanced MoE |

---

## 1. DeepSeek — DeepSeek-V4 (Pro / Flash)

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4 系列技术报告 |
| **英文标题** | DeepSeek-V4: Efficient Large Language Models with Higher Compactness and Speed |
| **发布机构** | DeepSeek AI |
| **模型系列** | V4-Pro / V4-Flash |
| **发布日期** | 2026-06（arXiv: 2606.19348）；V4-Pro GA 2026-08-13 |
| **参数量** | V4-Pro: 总参 1.6T / 49B active；V4-Flash: 284B / 13B active |
| **数据量** | 32T+ tokens |
| **上下文长度** | 1M |
| **主要创新点** | (1) CSA (Compressed Sparse Attention) + HCA (Heavily Compressed Attention)：极强 KV cache 压缩；(2) Manifold-Constrained Hyper-Connections (mHC)；(3) Muon optimizer；(4) 较 V3.2 节约约 27% FLOPs 与 90% KV cache；(5) 双模型均 MIT 开放权重，OpenRouter 已上线 `deepseek-v4-pro-0813`（今日 08-13 首个 GA 落地） |
| **论文链接** | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) |

---

## 2. OpenAI — GPT-5.6 (Sol / Terra / Luna) / GPT-5

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card / GPT-5 System Card |
| **英文标题** | GPT-5.6 System Card / GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.x |
| **发布日期** | GPT-5: 2025-08-13；GPT-5.6: 2026-07-17 |
| **参数量** | 未公开 |
| **上下文长度** | GPT-5.6: 400K input tokens |
| **主要创新点** | **GPT-5.6**: Router 架构（main/thinking/mini/nano/pro 变体），Sol 旗舰 / Terra 低成本 / Luna 最快最省；多模态（文本+图像+音频+视频），动态 thinking budget，83.2% SWE-Bench Verified；08-03 System Card 增补新增 GPT-Red 自动红队评估（自博弈 RL）。**GPT-5**: 首版 System Card，统一推理模型。GPT-Red 首次触及 Critical 网络安全阈值相关评估（08-07 Astra Preparedness） |
| **论文链接** | [GPT-5.6 System Card](https://cdn.openai.com/gpt-5-6-system-card.pdf) · [GPT-5 System Card](https://openai.com/index/introducing-gpt-5/) |

---

## 3. Meta AI — Muse Glimmer / Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Muse Glimmer 30B / Llama 4 家族 |
| **英文标题** | Muse Glimmer / Llama 4 |
| **发布机构** | Meta AI |
| **模型系列** | Muse Glimmer 30B（Muse 系列）；Llama 4 Scout / Maverick |
| **发布日期** | Muse Glimmer: 2026-08-10；Llama 4: 2025-04 |
| **参数量** | Muse Glimmer: 30B（Apache 2.0）；Llama 4: MoE 400B+ |
| **上下文长度** | Muse Glimmer: 128K；Llama 4 Scout: 10M+ |
| **主要创新点** | **Muse Glimmer**: Meta 2026-08 开放权重战略重心，30B 多模态 agent 模型，DFlash 投机解码（draft model），Apache 2.0，可在 24-32GB Mac 本地运行（26.6-50.2 tok/s），由 Muse Spark 蒸馏而来。**Llama 4**: MoE + 早期融合原生多模态 + iRoPE 长上下文；注意 Llama 4 405B 开放权重自 08-10 起持续"未兑现"（第 X 天），开源旗舰实际为 Muse 系列 |
| **论文链接** | [Meta AI Blog](https://ai.meta.com/blog/) · [HuggingFace](https://huggingface.co/meta-llama) |

---

## 4. Google DeepMind — Gemini 3.1 Pro

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 3.1 Pro Model Card |
| **英文标题** | Gemini 3.1 Pro Model Card |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.1 Pro |
| **发布日期** | 2026-02-19（基于 Gemini 3 Pro） |
| **参数量** | 未公开 |
| **上下文长度** | 1M（input），64K（output） |
| **主要创新点** | (1) Gemini 3 Pro 基础上升级；(2) 1M context 长上下文；(3) 64K 输出扩展；(4) 强推理/代码/多模态能力；(5) 相关 3.7 Flash 已 GA（08-13，1M/64K，agentic coding 主打） |
| **论文链接** | [Gemini 3.1 Pro Model Card](https://ai.google.dev/gemini-api/docs/models) |

---

## 5. Anthropic — Claude Fable 5 / Mythos 5

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5 / Claude Mythos 5 System Card |
| **英文标题** | Claude Fable 5 System Card / Claude Mythos 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Fable 5 / Mythos 5 |
| **发布日期** | 2026-06-09 |
| **参数量** | 未公开 |
| **上下文长度** | 未公开 |
| **主要创新点** | **Fable 5**: 带丰富安全防护（misuse safeguards）的前沿模型，RSP 治理。**Mythos 5**: 限 Project Glasswing 受信合作伙伴使用，集成 ASL-3 blocking classifiers（自动安全级别阻断分类器），面向最高风险前沿部署。两者构成 Anthropic 2026 闭源前沿双轨 |
| **论文链接** | [Anthropic Research](https://www.anthropic.com/research) |

---

## 6. Mistral AI — Shieldstral / Mistral Small 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Shieldstral / Mistral Small 4 |
| **英文标题** | Shieldstral / Mistral Small 4 |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B）；Mistral Small 4 |
| **发布日期** | Shieldstral: 2026-08-04；Small 4: 2026 |
| **参数量** | Shieldstral: 3B；Small 4: 未公开 |
| **主要创新点** | **Shieldstral**: 3B 多模态安全分类器，policy-adaptive QA（政策自适应问答），Apache 2.0，支持多语言，匹配 7× 体积模型的安全性能，Open Secure AI Alliance 体系。**Mistral Small 4**: 更强 token 感知型视觉模型，更快更便宜。另外 Mistral 欧洲主权 AI 路线（08-11，in-region inference + 开放模型） |
| **论文链接** | [Mistral Blog](https://mistral.ai/news/) |

---

## 7. Qwen (Alibaba) — Qwen3.5-397B-A17B / Qwen3.5-Omni

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.5 Technical Report / Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5 / Qwen3.5-Omni |
| **发布机构** | Alibaba / Qwen Team |
| **模型系列** | Qwen3.5-397B-A17B；Qwen3.5-Omni；Qwen3.8 后续 |
| **发布日期** | 2026（Qwen3.5 系列） |
| **参数量** | Qwen3.5-397B-A17B: 总参 397B / 17B active；Qwen3.5-Omni: 数百 B |
| **数据量** | 未公开 |
| **上下文长度** | Qwen3.5-Omni: 256K |
| **主要创新点** | **Qwen3.5-397B-A17B**: Hybrid Attention MoE。**Qwen3.5-Omni**: ARIA 架构、Hybrid Attention MoE，API 支持 10 种语言，原生全模态（文本/图像/音频/视频）。**Qwen3.8 家族**: Qwen3.8-Max (2.4T-A95B, 1M ctx) 与 Qwen3.8-27B (Apache 2.0, 原生多模态 262K) 构成"双轨"对照（08-14）。Qwen3.8-Max 权重 08-12 双验收日已兑现（HF `Qwen/Qwen3.8-2.4T-A95B`） |
| **论文链接** | [Qwen Blog](https://qwenlm.github.io/blog/) · [HuggingFace](https://huggingface.co/Qwen) |

---

## 8. Microsoft — Phi-4-reasoning-vision-15B / Phi-5

| 字段 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision 技术报告 |
| **英文标题** | Phi-4-reasoning-vision (MSR-TR-2026-10) |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 家族；Phi-5（预计） |
| **发布日期** | 2026-03 |
| **参数量** | 15B |
| **主要创新点** | **Phi-4-reasoning-vision-15B**: 融合视觉感知与推理的密度模型，面向多模态推理任务。**Phi-5**: 截至 2026-08 仍无官方"Phi-5"技术报告（Phi-4 家族仍为最新官方报告），仅 Phi Silica Platform Card (2026-06-24/07-08, Windows NPU 端侧 SLM, speculative decoding, LoRA 微调)；Phi-5 相关为传闻未确认 |
| **论文链接** | [MSR-TR-2026-10](https://www.microsoft.com/en-us/research/) |

---

## 9. NVIDIA — Nemotron 3.5 Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3.5 Lightning |
| **英文标题** | Nemotron 3.5 Lightning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3.5 家族 |
| **发布日期** | 2026-08-11 |
| **参数量** | 30B MoE（约 3B active per token） |
| **主要创新点** | (1) 面向 always-on agents 的开放 MoE；(2) speculative decoding 投机解码，最高 4× 输出速度；(3) 开源；(4) Agentic 工作负载优化；(5) 配套 NeMo Switchyard 开源 router；(6) 家族此前包含 Nemotron 3 Ultra (550B/55B Hybrid Mamba-Attention MoE, 1M ctx, 约 6× 推理吞吐) 与 Super/Nano |
| **论文链接** | [NVIDIA Developer Blog](https://developer.nvidia.com/blog/) |

---

## 10. xAI — Grok 4.6

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 |
| **英文标题** | Grok 4.6 Model Card |
| **发布机构** | xAI |
| **模型系列** | Grok 4.x |
| **发布日期** | 2026-08-12（Model Card，修订 08-17） |
| **参数量** | 1.5T 参数家族（沿 4.5 V9 基座），未完全公开 |
| **上下文长度** | 500K ctx |
| **主要创新点** | (1) text+image 输入 / text-only 输出；(2) 与 Cursor 联合开发；(3) reasoning 四档 low/medium/high/xhigh；(4) 新增 PartBench / DeepSearchQA / KernelBenchInternal 1.1 结果；(5) 无公开独立技术报告，仅 Model Card（文档差距相对于开源阵营仍存在） |
| **论文链接** | [x.ai](https://x.ai) · 无公开技术报告 |

---

## 11. Amazon — Amazon Nova Family

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 家族技术报告 |
| **英文标题** | Amazon Nova: Technical Report |
| **发布机构** | Amazon Web Services (AWS) |
| **模型系列** | Nova Pro / Lite / Micro / Canvas / Reel |
| **发布日期** | 2024（arXiv: 2506.12103 为 2025-06 提交） |
| **参数量** | Micro: 最小高效；Lite: 轻量；Pro: 最强 |
| **上下文长度** | 300K |
| **主要创新点** | (1) 多任务多模态家族：文本/图像/视频/音频统一理解；(2) Nova Canvas: 图像生成；(3) Nova Reel: 视频生成；(4) Amazon Bedrock 集成；(5) 注：Nova 2 报告为 2026（Lite/Pro/Omni/Sonic 全系 1M ctx）据 08-03 修正；2026 战略收缩（Premier/Reel 逐步弃用，Frontier Model Research 领衔） |
| **论文链接** | [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |

---

## 12. Zhipu AI — GLM-5.3

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5.3：Coding Agent 聚焦 |
| **英文标题** | GLM-5.3 |
| **发布机构** | Zhipu AI (智谱AI) |
| **模型系列** | GLM-5.x |
| **发布日期** | 2026-08-14 |
| **参数量** | 743B（与 GLM-5.2 相同基座，"基座不变、后训练提智"） |
| **主要创新点** | (1) 纯后训练 Scaling：数十倍长程环境 + IndexShare + SAO + 新一代 Slime 框架；(2) CyberGym 84.5%，超过 Mythos 5 (83.8%) 与 GPT-5.6 Sol (83.6%)；(3) Terminal-Bench 3.0 4.6→28.3 开源第一、DeepSWE v1.1 46.2→66.9、GDPval-AA 1,769；(4) 权重两周后开源；(5) 与 GLM-5（Vibe Coding→Agentic Engineering, arXiv:2602.15763）同一 Agent 化路线 |
| **论文链接** | [Z.ai](https://z.ai) · [arXiv:2602.15763](https://arxiv.org/abs/2602.15763)（GLM-5） |

---

## 13. Moonshot AI — Kimi K3

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K3：Agentic Intelligence 模型 |
| **英文标题** | Kimi K3 Technical Report |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K3 |
| **发布日期** | 2026-07-27（arXiv: 2607.24653） |
| **参数量** | 总参 2.8T / 104B active（MoE） |
| **上下文长度** | 1M |
| **主要创新点** | (1) 93 层（69 KDA + 24 Gated MLA）；（2）896 专家（激活 16），Stable LatentMoE；(3) Kimi Delta Attention + Attention Residuals 架构创新；(4) 相比 K2 效率提升约 2.5×；(5) 1M ctx 原生视觉；(6) 完整开放权重（full weights），开源信用延续（对照 Qwen/Meta 的"承诺制发布"） |
| **论文链接** | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) |

---

## 14. StepFun — Step3

| 字段 | 内容 |
|------|------|
| **中文标题** | Step-3：模型系统协同设计的高效推理 |
| **英文标题** | Step-3: Model-System Co-Design for Cost-Effective Decoding |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step3（Step-3.7 Flash 后续） |
| **发布日期** | 2025-07-31（arXiv: 2507.19427） |
| **参数量** | 总参 321B / 38B active |
| **主要创新点** | (1) Multi-Matrix Factorization Attention (MFA)；(2) Attention-FFN Disaggregation (AFD)；(3) 原生多模态；(4) Hopper 上吞吐较 DeepSeek-R1 +70%；(5) model-system co-design：同时优化架构与推理系统。Step-3.7 Flash (198B) 为后续产品；尚无 step-4 确认 |
| **论文链接** | [arXiv:2507.19427](https://arxiv.org/abs/2507.19427) |

---

## 15. ByteDance — Seed2.0 / Doubao-Seed-2.0-pro

| 字段 | 内容 |
|------|------|
| **中文标题** | Seed2.0 / Doubao-Seed-2.0-pro Model Card |
| **英文标题** | Seed2.0 Model Card (Doubao-Seed-2.0-pro) |
| **发布机构** | ByteDance (字节跳动) |
| **模型系列** | Seed 系列 / Doubao（豆包） |
| **发布日期** | 2026-02-14（旗舰 Doubao-Seed-2.0-pro） |
| **主要创新点** | (1) MoE 架构，通过 Volcano Engine MaaS 提供；(2) Doubao 155M 周活，全球第 4 大 GenAI 应用；(3) Seed1.8/Seed2.1 延续，Seed2.1 Pro 在 crowdsource coding 击败 Claude Opus 4.6；(4) 2026 传闻字节 >5T~10T 参数新模型训练（项亮主导，反蒸馏、追求差异化） |
| **论文链接** | [Volcano Engine](https://www.volcengine.com/) · [Seed 2.0 Model Card](https://seed.bytedance.com/) |

---

## 16. Baichuan — Baichuan-M4

| 字段 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4：临床级医疗 Agent |
| **英文标题** | Baichuan-M4: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | Baichuan AI (百川智能) |
| **模型系列** | Baichuan-M4 |
| **发布日期** | 2026-06-09（arXiv: 2606.08982） |
| **参数量** | 未完全公开 |
| **主要创新点** | (1) 临床级医疗 agent，建模临床问诊；(2) SPAR++：分段管道强化学习 + 跨度奖励；(3) Baichuan-Harness 评测框架；(4) HealthBench 68.6 世界第一，hallucination 3.3%；(5) 清华合作。延续 M3 (235B) 医疗增强方向 |
| **论文链接** | [arXiv:2606.08982](https://arxiv.org/abs/2606.08982) |

---

## 17. InternLM (上海AI Lab) — InternLM3-8B

| 字段 | 内容 |
|------|------|
| **中文标题** | InternLM3 技术报告 |
| **英文标题** | InternLM3 |
| **发布机构** | Shanghai AI Lab (上海AI实验室) / InternLM Team |
| **模型系列** | InternLM3-8B；Intern-S1-Pro 系列 |
| **发布日期** | InternLM3-8B: 2025-01 |
| **参数量** | InternLM3: 8B；Intern-S1-Pro: 1T MoE |
| **数据量** | InternLM3: 4T 高质量 tokens |
| **主要创新点** | **InternLM3**: 4T tokens 训练超越 Llama3.1-8B/Qwen2.5-7B，Apache-2.0，成本大幅降低。官网/GitHub 截至 2026-08-28 在搜结果未显示 2026 新大模型技术报告（Intern-S1-Pro 为最新大规模开源模型，InternVL3 多模态） |
| **论文链接** | [InternLM3](https://huggingface.co/internlm/internlm3-8b-instruct) · [InternLM GitHub](https://github.com/InternLM) |

---

## 18. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI (零一万物) |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024-12-02（arXiv: 2412.01253） |
| **参数量** | 未完全公开（Enhanced MoE 架构，100B 级） |
| **主要创新点** | (1) Enhanced MoE：细粒度专家分割 + 高级路由 + 优化 KV-caching；(2) Chatbot Arena 第 6，中文/数学/代码/Hard Prompts 第 2–4 名；(3) multi-stage 训练：预训练+SFT+RLHF；(4) RAISE (Responsible AI Safety Engine) 四组件安全框架；(5) 2026 年 01.AI 转向企业 AI（万策, 哈国 Q.AI 合资），无新旗舰模型技术报告，最新仍为 Yi-Lightning |
| **论文链接** | [arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |

---

## 行业趋势总结 / Key Industry Trends

1. **MoE 仍是绝对主流**：DeepSeek-V4 (1.6T/49B), Kimi K3 (2.8T/104B), Qwen3.5-397B-A17B, Nemotron 3.5 Lightning (30B/3B), ByteDance Seed 均采用 MoE；激活参数仅占总量 1/10–1/30，推理成本进一步下降。

2. **稀疏 / 压缩注意力进入收敛期**：DeepSeek CSA/HCA、Kimi Delta Attention、MiniMax MSA、GLM IndexShare、Qwen Hybrid Attention —— 多条独立同构的 KV cache 压缩 / 稀疏注意力方案同时出现，成为 1M 长上下文的旗舰标配。

3. **后训练 Scaling 成竞争前沿**：GLM-5.3"基座不变、后训练提智"（同 743B 基座纯后训练跃升）、MiniMax 自我进化、OpenAI 动态 thinking budget，都指向"在固定参数量上通过后训练/RL 提智"而非单纯换基座。

4. **中国开源旗舰"双轨"分化**：开放权重呈"能力/许可证双轨"——Apache-2.0 友好版（Qwen3.8-27B, Muse Glimmer, Nemotron 3.5 Lightning）vs 定制许可证旗舰（Qwen3.8-Max 2.4T, DeepSeek-V4 MIT, Kimi K3 full weights）；Kimi K3/DeepSeek V4-Pro 按期放权 vs Meta Llama 4 405B 持续失约形成信用分化。

5. **Agentic 能力成官方评测主战场**：Grok 4.6 新增 PartBench/KernelBenchInternal，GLM-5.3 强化 Terminal-Bench/DeepSWE，Nemotron 3.5 Lightning 主打 always-on agents，Nemotron 3 Ultra MOPD 多环境 RLVR；评测从纯 LLM 基准转向 agent 工作负载。

6. **安全分类器 / System Card 成为独立品类**：Mistral Shieldstral (3B 开源安全分类器)、Anthropic Mythos ASL-3 blocking classifiers、GPT-Red 自动红队、GLM-5.3 网络安全白盒审查，安全已从附加组件变成独立产品向量。

7. **推理成本优化 = 系统工程**：DeepSeek-V4 (27% FLOPs / 90% KV 节约)、Step-3 model-system co-design、Nemotron 3.5 Lightning speculative decoding、Mistral 欧洲主权 in-region inference，模型与硬件/系统协同设计成为规模化关键。

8. **多模态 + 长上下文成为 2026 旗舰标配**：Qwen3.5-Omni (全模态/多语言 API)、Muse Glimmer (多模态 agent)、GPT-5.6 (文本+图像+音频+视频)、Kimi K3 (1M ctx 原生视觉)，单一能力旗舰已让位于"全模态 + 超长上下文"组合。

9. **垂直领域差异化持续**：Baichuan-M4 临床医疗 agent 世界第一、Amazon Nova 企业/MaaS 场景、Apple 端侧，垂直领域是闭源厂商差异化竞争点。

10. **发布信用与"承诺制"对决**：2026-08 中旬四大"承诺制发布"（Llama 4 405B、Qwen3.8-Max 权重、Grok 4.6、DeepSeek V4-Pro GA）中，Qwen 权重、V4-Pro GA 已兑现，Grok 4.6 达 Model Card 级，仅 Meta 405B 持续悬而不决；开源权重交付信用成为开源阵营的核心竞争维度。

---

(End of file)
