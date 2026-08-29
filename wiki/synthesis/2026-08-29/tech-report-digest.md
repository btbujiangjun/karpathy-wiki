---
title: "LLM Tech Report Digest — 2026-08-29"
type: synthesis
created: 2026-08-29
updated: 2026-08-29
tags: [tech-report, llm, moe, mamba, multimodal, reasoning, scaling, agentic, hybrid-architecture, daily-digest]
sources: []
---

# LLM Tech Report Digest — 2026-08-29

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要。
> 覆盖 18 家目标机构，聚焦 2026 年（尤其 7–8 月）最新发布与更新，附每机构一表格。
> Last updated: 2026-08-29

---

## 目录 / Table of Contents

| # | 机构 | 模型 | 发布日期 | 核心架构 |
|---|------|------|----------|----------|
| 1 | DeepSeek | DeepSeek-V4 (Pro/Flash) | 2026-04~08 | MoE 1.6T/49B + CSA/HCA |
| 2 | OpenAI | GPT-5.6 (Sol/Terra/Luna) | 2026-07/08 | Closed, Router 架构 |
| 3 | Meta AI | Muse Glimmer 30B / Llama 4 | 2026-08 | 多模态 agent 模型 (DFlash) |
| 4 | Google DeepMind | Gemini 3.7 Flash / Omni Flash | 2026-08 | 1M ctx, 多模态 |
| 5 | Anthropic | Claude Opus 5 / Fable 5 / Mythos 5 | 2026-06/07 | Closed, ASL-3 blocker |
| 6 | Mistral AI | Shieldstral / Small 4 | 2026-03/08 | 3B 安全分类器 / 119B MoE |
| 7 | Qwen (Alibaba) | Qwen3.8-Max 2.4T / Omni | 2026-08 | Sparse MoE + Hybrid Attention |
| 8 | Microsoft | Phi-4-reasoning-vision-15B / Phi Silica | 2026-03/06 | Dense + 视觉推理 |
| 9 | NVIDIA | Nemotron 3 Super / 3.5 Lightning | 2026-08 | Hybrid Mamba-Attention MoE |
| 10 | xAI | Grok 4.6 | 2026-08-12 | 1.5T 家族, closed (Grok 5 训练中 6T/10T) |
| 11 | Amazon | Nova 2 (Lite/Pro/Omni/Sonic) | 2025-12/2026 | 多模态 1M ctx |
| 12 | Zhipu AI | GLM-5.3 | 2026-08-14 | Coding 聚焦, 后训练 Scaling |
| 13 | Moonshot AI | Kimi K3 | 2026-07-27 | 2.8T/104B MoE, Delta Attention |
| 14 | StepFun | Step3 | 2025-07 | MFA + AFD |
| 15 | ByteDance | Seed2.1 (Doubao) | 2026-06-23 | Agent 生产力模型 Pro/Turbo |
| 16 | Baichuan | Baichuan-M4 | 2026-06-09 | 临床医疗 agent, SPAR++ |
| 17 | InternLM (上海AI Lab) | InternLM3-8B | 2025-01 | 轻量高效 |
| 18 | 01.AI | Yi-Lightning | 2024-12 | Enhanced MoE |

---

## 1. DeepSeek — DeepSeek-V4 (Pro / Flash)

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4 系列：迈向高效百万 token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek AI |
| **模型系列** | V4-Pro / V4-Flash（及 -Base 基座） |
| **发布日期** | 论文 2026-04-26（arXiv: 2606.19348）；V4-Pro GA 2026-08-13 |
| **参数量** | V4-Pro: 1.6T / 49B active；V4-Flash: 284B / 13B active |
| **数据量** | 32T+ tokens（两阶段，含领域专家独立培养 + on-policy 蒸馏合并） |
| **上下文长度** | 1M |
| **主要创新点** | (1) Hybrid Attention：Compressed Sparse Attention (CSA, m=4) + Heavily Compressed Attention (HCA, m'=128) 交错配置，1M ctx 下仅需 V3.2 的 27% 推理 FLOPs、10% KV cache；(2) Manifold-Constrained Hyper-Connections (mHC)，残差投影约束在 doubly-stochastic 流形（Sinkhorn 迭代）；(3) Muon optimizer；(4) Hash-MoE bootstrap 层 + Sqrt(Softplus) 激活亲和力；(5) Lightning Indexer (FP4) 稀疏选则压缩 KV；(6) 三档推理 effort（non-think/think high/think max）；(7) FP4+FP8 混合精度，MIT 开放权重 |
| **论文链接** | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) · [HF V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |

---

## 2. OpenAI — GPT-5.6 (Sol / Terra / Luna)

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card（含 2026-08 月度更新） |
| **英文标题** | GPT-5.6 System Card — August Updates |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 低成本 / Luna 最快） |
| **发布日期** | 初版 2026-07-09/17；August 更新 2026-08（08-19 changelog） |
| **参数量** | 未公开 |
| **上下文长度** | 400K input tokens |
| **主要创新点** | (1) Router 架构 + 动态 thinking budget（effort slider）；(2) 多模态（文本+图像+音频+视频）；(3) GPT-Red 自动红队模型（self-play RL 自博弈，尤其擅 prompt injection｜08-03 增补）；(4) Preparedness Framework：Sol/Terra/Luna 均 High (Bio/Chem 与 Cyber)、低于 High (AI Self-Improvement)；(5) August 更新：ChatGPT 默认模型升级（Plus/Pro Sol with effort slider），替换 GPT-5.5 Instant，Sol/Luna 分 July/August 两版；(6) 08-19 勘误 GPT-5.5 蛋白质结合 pass@4 0.4%→1.5% |
| **论文链接** | [GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf) · [August Updates](https://deploymentsafety.openai.com/gpt-5-6-august-update/safety) |

---

## 3. Meta AI — Muse Glimmer 30B / Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Muse Glimmer 30B / Llama 4 家族 |
| **英文标题** | Muse Glimmer / Llama 4 |
| **发布机构** | Meta AI |
| **模型系列** | Muse Glimmer 30B（Muse 系列）；Llama 4 Scout / Maverick |
| **发布日期** | Muse Glimmer: 2026-08-10；Llama 4: 2025-04-05 |
| **参数量** | Muse Glimmer: 30B（Apache 2.0，DFlash 投毒解码）；Llama 4 Scout: 109B 总 / 17B active |
| **上下文长度** | Muse Glimmer: 128K；Llama 4 Scout: 10M；Maverick: 1M |
| **主要创新点** | **Muse Glimmer**: 开放权重战略重心，30B 多模态 agent 模型，DFlash 投机解码（draft model），Apache 2.0，24-32GB Mac 本地运行（26.6-50.2 tok/s），由 Muse Spark 蒸馏。**Llama 4**: 首个原生多模态 MoE + early fusion + iRoPE 长上下文；**注意**：Llama 4 405B/Behemoth 开放权重自 08-10 起持续"未兑现"，开源旗舰实际为 Muse 系列 |
| **论文链接** | [Meta AI Blog](https://ai.meta.com/blog/) · [Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |

---

## 4. Google DeepMind — Gemini 3.7 Flash / Omni Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 3.7 Flash / Gemini Omni Flash Model Card |
| **英文标题** | Gemini 3.7 Flash · Gemini Omni Flash Model Card |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.x Flash；Gemini Omni Flash |
| **发布日期** | 3.7 Flash: 2026-08-13（GA）；Omni Flash: 2026-05 发布、08-27 更新 |
| **参数量** | 未公开 |
| **上下文长度** | Gemini 3.x Flash 系列 1M ctx；Omni Flash 面向视频创建/编辑 |
| **主要创新点** | **Gemini 3.7 Flash**: "most intelligent workhorse"，agentic coding 聚焦，可配置 thinking，Intro 价格 $0.75/$3.75 per 1M tokens（half of 3.6 Flash）；驱动 Gemini Spark 24/7 agent。**Gemini Omni Flash (08-27 更新)**: 边对边多模态——创建与编辑视频，结合 Gemini 智能与生成式媒体模型（world understanding + editing）。Gemini 3.1 Pro 仍为旗舰 (1M/64K, 2026-02-19) |
| **论文链接** | [Gemini 3.7 Flash Model Card](https://deepmind.google/models/model-cards/gemini-3-7-flash/) · [Omni Flash](https://deepmind.google/models/model-cards/gemini-omni-flash/) |

---

## 5. Anthropic — Claude Opus 5 / Fable 5 / Mythos 5

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 / Fable 5 / Mythos 5 System Card |
| **英文标题** | Claude Opus 5 System Card / Claude Fable 5 & Mythos 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Opus 5 / Sonnet 5 / Fable 5 / Mythos 5 |
| **发布日期** | Opus 5: 2026-07-24；Fable 5 & Mythos 5: 2026-06-09 |
| **参数量** | 未公开 |
| **上下文长度** | 未公开 |
| **主要创新点** | **Opus 5 (07-24, 新增)**: Opus 4.8 升级，agentic coding / computer use / long-horizon knowledge work / 数学与科学推理全面提升，约接近 Fable 5 前沿智力而半价（$5/$25 per 1M），安全上不推进 risky dual-use（落后于 Mythos 5）。**Fable 5**: 带 misuse safeguards 的前沿模型。**Mythos 5**: 限受信合作伙伴，集成 ASL-3 blocking classifiers。三者构成 Anthropic 2026 闭源前沿双轨 + Opus 主力线 |
| **论文链接** | [Opus 5 System Card](https://www.anthropic.com/research/claude-opus-5) · [System Cards](https://www.anthropic.com/system-cards) |

---

## 6. Mistral AI — Shieldstral / Mistral Small 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Shieldstral / Mistral Small 4 |
| **英文标题** | Shieldstral / Mistral Small 4 |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B）；Mistral Small 4 |
| **发布日期** | Shieldstral: 2026-08-04；Small 4: 2026-03-16 |
| **参数量** | Shieldstral: 3B；Small 4: 119B 总 / 6.5B active（128 experts, 4 active） |
| **数据量** | 未公开 |
| **上下文长度** | Small 4: 256K |
| **主要创新点** | **Small 4**: 首个统一 Magistral (reasoning) ÷ Pixtral (multimodal) ÷ Devstral (agentic coding) 的三合一 MoE，文本+图像输入，可配置 reasoning_effort (none/high)，Apache 2.0，40% 时延降低 / 3× 吞吐 vs Small 3，NVIDIA Nemotron Coalition 创始成员，支持 vLLM/SGLang/llama.cpp。**Shieldstral**: 3B 多模态安全分类器，policy-adaptive QA，Apache 2.0，Open Secure AI Alliance。另：欧洲主权 AI 路线（08-11, in-region inference） |
| **论文链接** | [Small 4](https://mistral.ai/news/mistral-small-4/) · [HF Small 4 NVFP4](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4) |

---

## 7. Qwen (Alibaba) — Qwen3.8-Max 2.4T / Qwen3.5-Omni

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max：编码与协作新标杆 |
| **英文标题** | Qwen3.8-Max: A New Bar for Coding and Cowork |
| **发布机构** | Alibaba / Qwen Team |
| **模型系列** | Qwen3.8-Max；Qwen3.8-27B；Qwen3.5-Omni |
| **发布日期** | Qwen3.8-Max: 2026-08-03（权重 08-12 开放）；Qwen3.5-Omni: 2026 |
| **参数量** | Qwen3.8-Max: 总参 2.4T / 95B active（激活比 ~3.96%，~256 experts，top-8）；Qwen3.8-27B: 27B Apache 2.0 |
| **上下文长度** | Qwen3.8-Max: 1M（输入 991.8K / 输出 131K） |
| **主要创新点** | (1) 首个开源 Max 级模型（Qwen3.5 架构上 Sparse MoE + Hybrid Attention）；(2) 推理 effort 支持 (low/medium/high)；(3) 自主编码 10+ 天（oh-my-cli 项目全流程）、芯片设计 500+ 轮闭环优化（RTL 8298→678 gates）；(4) OSWorld-Verified 86.1 第一，PaperBench 93.0 (较 3.7-Max 64.8 提升 28.2)；(5) Native 多模态视觉 + long-horizon RL（真实环境 joint RL expansion）；(6) 定价 $2/$6 per 1M；(7) Qwen3.8-Max 权重 08-12 兑现（HF `Qwen3.8-2.4T-A95B`），完成"承诺制发布"验收 |
| **论文链接** | [Qwen3.8 Blog](https://qwen.ai/blog?id=qwen3.8) · [GitHub Qwen3.8-max](https://github.com/AlibabaCloud-Official/Qwen3.8-max) |

---

## 8. Microsoft — Phi-4-reasoning-vision-15B / Phi Silica

| 字段 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision 技术报告 |
| **英文标题** | Phi-4-reasoning-vision (MSR-TR-2026-10) |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 家族；Phi Silica Platform Card |
| **发布日期** | Phi-4-reasoning-vision: 2026-03；Phi Silica: 2026-06-24/07-08 |
| **参数量** | Phi-4-reasoning-vision: 15B |
| **主要创新点** | **Phi-4-reasoning-vision-15B**: 融合视觉感知与推理的密度模型。**Phi Silica Platform Card**: Windows NPU 端侧 SLM，speculative decoding，LoRA 微调。**Phi-5**: 截至 2026-08 仍无官方"Phi-5"技术报告（Phi-4 仍为最新官方报告），Phi-5 相关为传闻未确认 |
| **论文链接** | [MSR-TR-2026-10](https://www.microsoft.com/en-us/research/) |

---

## 9. NVIDIA — Nemotron 3 Super / 3.5 Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Super / Nemotron 3.5 Lightning |
| **英文标题** | Nemotron 3 Super: Open, Efficient MoE Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Super / Nano / Ultra；3.5 Lightning |
| **发布日期** | Nemotron 3 Super: 2026（arXiv: 2604.12374）；3.5 Lightning: 2026-08-11 |
| **参数量** | **Super**: 120B 总 / 12B active（512 experts, top-22），LatentMoE + MTP；**3.5 Lightning**: 30B MoE（~3B active） |
| **数据量** | Super: 25T tokens（两阶段 20T+5T） |
| **上下文长度** | Super: 1M |
| **主要创新点** | **Nemotron 3 Super (新增, arXiv:2604.12374)**: (1) hybrid Mamba-Transformer MoE（周期交错 Mamba-2 块，constant-size state 降低 KV cache）；(2) LatentMoE 优化 accuracy/FLOP 与 accuracy/param；(3) MTP 投机解码（native speculative decoding，最高 2.2× vs GPT-OSS-120B、7.5× vs Qwen3.5-122B 吞吐）；(4) NVFP4 低精度预训练（首个）；(5) 三阶段 RL (RLVR→SWE-RL→RLHF) + MTP healing；权重+数据集开源。**3.5 Lightning**: always-on agents speculative decoding 最高 4×，NeMo Switchyard 开源 router。家族含 Nemotron 3 Ultra (550B/55B) |
| **论文链接** | [arXiv:2604.12374](https://arxiv.org/pdf/2604.12374) · [NVIDIA Blog](https://developer.nvidia.com/blog/) |

---

## 10. xAI — Grok 4.6

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 / Grok 5（训练中） |
| **英文标题** | Grok 4.6 Model Card |
| **发布机构** | xAI (SpaceXAI) |
| **模型系列** | Grok 4.x；Grok 5（未发布） |
| **发布日期** | Grok 4.6: 2026-08-12（API/Model Card）；Grok 5: 训练中，传闻 Q3 2026+ |
| **参数量** | Grok 4.6: 1.5T 家族（沿 4.5 V9 基座，有报道称 2T 设计），未完全公开；Grok 5: 传闻 6T 与 10T 双变体（Colossus 2 训练） |
| **上下文长度** | Grok 4.6: 500K |
| **主要创新点** | (1) long-running agents / interactive and visual work 聚焦；(2) text+image 输入 / text-only 输出；(3) reasoning 四档 low/medium/high/xhigh；(4) 与 Cursor 联合开发 + Grok Build；(5) 定价 $2/$6 per 1M（<200K prompt），fast 变体 2×；(6) 无公开独立技术报告，仅 Model Card；(7) **Grok 5**: 01-06 Series E 确认训练中，6T 与 10T MoE 变体，传闻含 Cursor 开发者工作流数据（agentic coding 偏向），release 窗口多次延后 |
| **论文链接** | [xAI Grok 4.6](https://x.ai/news/grok-4-6) · [API release notes](https://docs.x.ai/developers/release-notes) |

---

## 11. Amazon — Nova 2 (Lite / Pro / Omni / Sonic)

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **英文标题** | Amazon Nova 2: Multimodal reasoning and generation models |
| **发布机构** | Amazon AGI / AWS |
| **模型系列** | Nova 2 Lite / Pro / Omni / Sonic；Nova Multimodal Embeddings |
| **发布日期** | 2025-12-02（Nova 2 家族，AWS Technical Report） |
| **参数量** | 未公开 |
| **上下文长度** | 1M tokens（Lite/Pro/Omni） |
| **主要创新点** | (1) 四变体覆盖企业需求：Lite/Pro = 动态推理（extended thinking，low/medium/high 三档）；Omni = 统一多模态（文本/图像/视频/音频输入，文本+图像输出）；Sonic = speech-to-speech；(2) 内置 tools（Web Grounding + Code Interpreter）+ remote MCP；(3) Lite 支持 SFT/RFT 定制（Bedrock/SageMaker），Nova Forge 可控预训练自建 frontier；(4) Nova Multimodal Embeddings 统一多模态 embedding；(5) Sonic 支持 7 语言、polyglot voices；(6) Nova 1 原始报告 arXiv:2506.12103 (2025-06) 为基线 |
| **论文链接** | [Amazon Nova 2 Tech Report](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models) · [Nova 1 arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |

---

## 12. Zhipu AI — GLM-5.3

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5.3：前沿编码与涌现网络能力 |
| **英文标题** | GLM-5.3: Frontier Coding with Emergent Cyber Capabilities |
| **发布机构** | Zhipu AI (智谱AI / Z.ai) |
| **模型系列** | GLM-5.x |
| **发布日期** | 2026-08-14（权重预计 ~08-28 后开源，安全加固后） |
| **参数量** | 743B–744B（与 GLM-5.2 相同基座，40B active —— "基座不变、后训练提智"） |
| **上下文长度** | 1M；输出 128K |
| **主要创新点** | (1) 纯后训练 Scaling：SAO (Sequential Action Optimization) 单轨迹异步 RL（支持 1000+ 步）+ IndexShare 层级共享 Indexer（1M ctx 降 2.9× FLOPs）+ Slime 异步分布式训练框架（THUDM/slime，吞吐 2.3×）；(2) 编码：Terminal-Bench 3.0 4.6→28.3（开源第一）、DeepSWE v1.1 46.2→66.9、Agents' Last Exam 23.8→28.5、GDPval-AA 1,769；(3) 内生网络能力：CyberGym 84.5%（超 Mythos 5 83.8%、Sol 83.6%），ExploitBench 24.4→54.4%，真实代码库 2,436 漏洞 / 269 项目（最早 ~40 年前）；(4) token 效率：Max effort 34.5%@75K tokens 超 Opus 4.8；仅支持 reasoning (low/high/max)，不可关闭；(5) 首次因安全原因延后开源 |
| **论文链接** | [GLM-5.3 Blog](https://z.ai/blog/glm-5.3) · [Docs](https://docs.z.ai/guides/llm/glm-5.3) · [GLM-5 arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |

---

## 13. Moonshot AI — Kimi K3

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K3：开源前沿智能 |
| **英文标题** | Kimi K3: Open Frontier Intelligence |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K3 |
| **发布日期** | 2026-07-27（arXiv: 2607.24653） |
| **参数量** | 总参 2.8T / 104B active（MoE），93 层（69 KDA + 24 Gated MLA），896 专家激活 16 + 2 shared |
| **上下文长度** | 1,048,576（1M） |
| **主要创新点** | (1) Kimi Delta Attention (KDA)：固定大小 recurrent state 替代随 token 增长的 KV cache + periodic full-attention 层；Attention Residuals (AttnRes) 跨深度选择性取回；(2) Stable LatentMoE：latent 维度专家计算 + Quantile Balancing（router-score 分位数分配，无需手动平衡超参）+ Per-Head Muon；(3) SiTU-GLU 激活 + Gated MLA；(4) 相比 K2 整体 scaling 效率 ~2.5×；(5) 1M ctx 原生视觉（MoonViT-V2, 401M）；(6) 完整开放权重（首个开源 3T 级模型），MXFP4/MXFP8 QAT；post-training 覆盖 general/agentic/coding RL 多 effort 层次 |
| **论文链接** | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) · [GitHub](https://github.com/MoonshotAI/Kimi-K3) |

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
| **主要创新点** | (1) Multi-Matrix Factorization Attention (MFA)；(2) Attention-FFN Disaggregation (AFD)；(3) 原生多模态；(4) Hopper 上吞吐较 DeepSeek-R1 +70%；(5) model-system co-design。Step-3.7 Flash (198B) 为后续产品；尚无 step-4 确认 |
| **论文链接** | [arXiv:2507.19427](https://arxiv.org/abs/2507.19427) |

---

## 15. ByteDance — Seed2.1 (Doubao)

| 字段 | 内容 |
|------|------|
| **中文标题** | Seed2.1：推进 AI 生产力 |
| **英文标题** | Seed2.1 Officially Released: Advancing AI Productivity |
| **发布机构** | ByteDance (字节跳动) / Volcano Engine |
| **模型系列** | Seed2.1 Pro / Turbo（Doubao-Seed-2-1-pro-260628 等） |
| **发布日期** | 2026-06-23/24（Volcano Engine FORCE 大会） |
| **参数量** | 未公开（MoE 未确认） |
| **上下文长度** | 256K（输入/输出/思维链均 256K） |
| **主要创新点** | (1) 新一代 agent 生产力模型（一般 agent + 代码工程）；(2) GDPVal 87.9 (Seed2.1-Pro) 超 GPT-5.5 (84.9)、Claude Opus 4.7 (82.7)、Gemini 3.1 Pro (67.3)；(3) 视频理解多 SOTA（含小时级长视频，TOMATO/VideoMME 等）；(4) 多模态输入（文本/图像/视频），文本输出；(5) 闭源，仅 Doubao / Volcano Engine API；(6) 定价 CNY ¥6/¥30 (Pro)、¥3/¥15 (Turbo) per 1M；(7) Seed 154M+ 周活、全球第 4 大 GenAI 应用 |
| **论文链接** | [Seed2.1](https://research.doubao.com/en/seed2_1) · [Blog](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity) · [Seed2.0 Model Card PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/seed2/0214/Seed2.0%20Model%20Card.pdf) |

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
| **主要创新点** | 4T tokens 训练超越 Llama3.1-8B/Qwen2.5-7B，Apache-2.0，成本大幅降低。截至 2026-08-29 无 2026 新大模型技术报告（Intern-S1-Pro 为最新大规模开源模型，InternVL3 多模态） |
| **论文链接** | [HF InternLM3](https://huggingface.co/internlm/internlm3-8b-instruct) · [GitHub](https://github.com/InternLM) |

---

## 18. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI (零一万物) |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024-12-02（arXiv: 2412.01253） |
| **参数量** | 未完全公开（Enhanced MoE，100B 级） |
| **主要创新点** | (1) Enhanced MoE：细粒度专家分割 + 高级路由 + 优化 KV-caching；(2) Chatbot Arena 第 6；(3) multi-stage 训练（预训练+SFT+RLHF）；(4) RAISE 四组件安全框架；(5) 2026 年转向企业 AI（万策/哈国 Q.AI），无新旗舰技术报告，最新仍为 Yi-Lightning |
| **论文链接** | [arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |

---

## 今日追踪更新 / Today's Delta (vs 2026-08-28)

- **新增 Claude Opus 5**（Anthropic, 07-24）：上版未收录，作为 Opus 主力线重要更新。
- **Google 更新二则**：Gemini 3.7 Flash (08-13 GA) 与 Gemini Omni Flash (08-27 更新)——上版仅列 3.1 Pro。
- **新增 NVIDIA Nemotron 3 Super**（arXiv:2604.12374）：120B/12B hybrid Mamba-Attention MoE + LatentMoE + MTP + NVFP4 预训练，与 3.5 Lightning 并列。
- **OpenAI GPT-5.6 August 更新**：ChatGPT 默认模型升级 Sol/Luna，effort slider，替换 GPT-5.5 Instant；08-19 勘误。
- **xAI Grok 5 状态**：确认训练中（6T 与 10T 变体，Colossus 2），4.6 仍为当前旗舰。
- **Apple AFM 3（06-08）**：第三代五模型（Core/Core Advanced/Cloud/Cloud Pro + ADM 3 Cloud），含 20B sparse on-device（IFP Instruction-Following Pruning，1–4B active）——重建 Apple 条目基线。

---

## 行业趋势总结 / Key Industry Trends

1. **MoE 仍是绝对主流**：DeepSeek-V4 (1.6T/49B)、Kimi K3 (2.8T/104B)、Qwen3.8-Max (2.4T/95B)、Nemotron 3 Super (120B/12B)、Mistral Small 4 (119B/6.5B) 均采用 MoE；激活参数仅占 1/24~1/30，推理成本持续下降。

2. **稀疏/压缩注意力进入收敛期**：DeepSeek CSA/HCA、Kimi KDA、GLM IndexShare、Qwen Hybrid Attention、NVIDIA Mamba-Attention hybrid、Apple PT-MoE interleaved local/global attention——多条独立同构的 KV-cache 压缩 / 稀疏注意力方案成为 1M 长上下文旗舰标配。

3. **hybrid Mamba-Attention 成为新变量**：Nemotron 3 Super (120B/12B) + Kimi KDA (固定 recurrent state) + DeepSeek HCA，序列状态 / 窗口化状态 / 降压缩 KV 三种路线并进，试探替换全密度 attention。

4. **后训练 Scaling 成竞争前沿**：GLM-5.3"基座不变、后训练提智"（同 743B base 纯后训练，编码 +50%）、Nemotron 3 阶段化 RL (RLVR→SWE-RL→RLHF)、OpenAI 动态 thinking budget——"怎么训"而非"训多大"。

5. **中国开源旗舰"双轨"分化**：开放权重呈能力/许可证双轨——Apache-2.0 友好版（Qwen3.8-27B, Muse Glimmer, Mistral Small 4）vs 定制许可证旗舰（Qwen3.8-Max 2.4T, DeepSeek-V4 MIT, Kimi K3 full weights）；Kimi K3/DeepSeek V4-Pro/Qwen3.8-Max 按期放权 vs Meta Llama 4 405B 持续失约形成信用分化。

6. **Agentic 能力成官方评测主战场**：Qwen3.8-Max OSWorld-Verified 86.1 / PaperBench 93.0、GLM-5.3 Terminal-Bench 28.3 + DeepSWE 66.9、Grok 4.6 long-running agents、Nemotron 3.5 Lightning always-on agents——评测从纯 LLM 基准转向 agent 工作负载。

7. **安全分类器 / System Card 成为独立品类**：Mistral Shieldstral (3B 开源安全分类器)、Anthropic Mythos ASL-3 blocking classifiers、GPT-5.6 GPT-Red 自博弈红队、GLM-5.3 网络安全白盒审查（首个因安全延后开源）、Nemotron 3 Agentic；安全已从附加组件变成独立产品向量（"emergent cyber capability" 成为新关注点）。

8. **推理成本优化 = 系统工程**：DeepSeek-V4 (27% FLOPs / 90% KV 节约)、Nemotron 3 Super MTP + speculative decoding (2.2×/7.5× 吞吐)、Step-3 model-system co-design、GPT-5.6 effort slider、GLM-5.3 token 效率——模型与推理系统协同设计成为规模化关键。

9. **全模态 + 长上下文成为 2026 旗舰标配**：Amazon Nova 2 / Qwen3.8-Max (Native 视觉) / Gemini Omni Flash (视频创建) / Kimi K3 (1M ctx 原生视觉) / GPT-5.6 (全模态)——单一能力旗舰已让位于"全模态 + 超长上下文"组合。

10. **超大规模"承诺制发布"与兑现信用**：Qwen3.8-Max 2.4T 权重、DeepSeek V4-Pro GA、Grok 4.6 Model Card 已兑现；Meta Llama 4 405B 持续悬置；xAI Grok 5 (6T/10T) 训练中窗口屡延——开源权重交付信用 + 文档完整性（Model Card vs 完整 Technical Report）成为开源阵营核心竞争维度。

---

(End of file)
