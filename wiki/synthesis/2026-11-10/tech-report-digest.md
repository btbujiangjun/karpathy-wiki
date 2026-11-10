---
title: LLM Tech Report Digest — 2026-11-10
type: synthesis
created: 2026-11-10
updated: 2026-11-10
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, daily-digest]
---

# LLM 技术报告速览 — 2026-11-10
# LLM Tech Report Digest — 2026-11-10

> 覆盖窗口：2026-11-07 → 2026-11-10（增量复核，基线为 [[2026-11-07/tech-report-digest]]）。本期对 19 家目标机构的最新可验证技术报告/系统卡/模型卡进行汇总；窗口内未发现可独立核实的全新一手旗舰技术报告发布，重点更新为状态复核与已发布材料的可获取性确认（如 Kimi K3.1 Pro 权重已在 Hugging Face 可见）。  
> 口径说明：参数、训练数据、上下文长度与 benchmark 多为厂商自报；闭源模型细节以官方系统卡/博客为准；未发布/传闻项单列标注，不计入“已发布报告”。

## 本期结论（2026-11-10）

- **窗口内新增一手旗舰报告：未检索到可独立确认的新发布。** 主要旗舰材料仍集中在 2026-09 至 2026-10（DeepSeek V4/V4.1、OpenAI GPT-6 系列系统卡、Meta Muse 系列、Gemini 4 Argon、Claude 5.5 系列、Mistral Large 4、Nemotron 3.5 等）。
- **权重/可获取性复核：** Moonshot `moonshotai/Kimi-K3.1-Pro` 在 Hugging Face 可见（权重/模型页按官方计划于 11/4–11/5 附近落地，后续仍可下载）；DeepSeek `DeepSeek-V4.1-Flash-1017` 仍为近期活跃版本。
- **趋势延续：** MoE + 稀疏/混合注意力主导长上下文效率；后训练/RL 与可验证环境成为能力跃迁主杠杆；1M 上下文进入旗舰常态但“可用长上下文”依赖 KV/稀疏索引优化；系统卡对网络安全/生物安全/对齐监测的披露力度持续提高。

## 覆盖机构状态总览

| 机构 | 最新可验证代表材料 | 日期 | 2026-11-10 状态 |
|---|---|---|---|
| DeepSeek | DeepSeek-V4 技术报告；DeepSeek-V4.1-Flash 发布材料 | 2026-04-26 / 2026-09-10 | 无窗口内新一手报告确认；V4.1-Flash-1017 仍活跃 |
| OpenAI | GPT-6 Astra / Sol-Luna / Cyber / Rosalind-6 等系统卡 | 2026-09~11-05 | 无窗口内新增系统卡确认（最新已知为 GPT-6 Cyber 11/5） |
| Meta AI (LLaMA/Muse) | Muse Wonder / Muse Spark Open / Muse Glimmer 30B | 2026-10-12~19 | 无窗口内新报告确认 |
| Google DeepMind (Gemini) | Gemini 4 Argon 模型卡+安全报告；Gemini Omni 1.2 Flash 更新 | 2026-10-13 / 2026-11-05 | 无窗口内新增旗舰模型卡确认 |
| Anthropic (Claude) | Claude 5.5 家族系统卡（Opus/Sonnet/Haiku） | 2026-09-22~10-07 | 无窗口内新系统卡确认 |
| Mistral AI | Mistral Large 4（Le Chonk）发布与开放权重；Timestral | 2026-10-06~29 / 2026-10-27 | 权重已开放，完整技术报告仍待发（截至本期） |
| Qwen (Alibaba) | Qwen3.8-Max；Qwen3.8-Flash-Next（qwen4_exp 预览） | 2026-08-03 / 2026-08-26 | Qwen4 正式版未确认发布 |
| Yi (01.AI) | Yi 系列历史报告 | — | 2026 年无可验证新主源技术报告/系统卡 |
| Baichuan | Baichuan 2（通用）/ 医疗线材料 | 2023 / 2026 垂类 | 通用旗舰新技术报告未确认 |
| Microsoft (Phi) | Phi-4-reasoning-vision-15B 技术报告 | 2026-03-04 | Phi-5 无官方技术报告确认 |
| Apple | 第三代 Apple Foundation Models（AFM 3） | 2026-06-08 | 无 arXiv 完整技术报告；云端/端侧文档持续 |
| NVIDIA | Nemotron 3.5 Super/Lightning/Bolt/Transcribe 技术报告 | 2026-10-14~28 | 无窗口内新报告确认 |
| xAI (Grok) | Grok 4.7 模型卡 | 2026-09-21 | Grok 4.8 未确认发布 |
| Amazon (Nova) | Amazon Nova 2 技术报告；Nova 2 Lite 安全评估 | 2025-12-02 / 2026-01-27 | 无窗口内新 Nova 技术报告确认 |
| Zhipu AI (GLM/ChatGLM) | GLM-5.3 / GLM-5.3-Flash；GLM-Omni 研究 | 2026-08 / 2026-10 | GLM-5.4/5.5 未确认发布 |
| InternLM (Shanghai AI Lab) | Intern-S2-Preview-397B；Intern-S2-Mobius | 2026-08~09 | 无窗口内新报告确认 |
| Moonshot AI (Kimi) | Kimi K3.1 Pro 技术博客与权重发布 | 2026-10-23 / 2026-11-04~05 | 权重已可获取（HF），无窗口内新技术报告 |
| StepFun (阶跃星辰) | Step 5 Preview 技术博客/开放权重 | 2026-09-20 / 2026-10-15 | 完整 arXiv 技术报告未见 |
| ByteDance (豆包/Doubao) | Seed 2.0 模型卡；doubao-seed-evolving 更新 | 2026-06-19 / 2026-11 更新 | 无窗口内新完整技术报告确认 |

## 重点报告与系统卡（按机构）

> 字段说明：参数量/训练数据量/上下文长度为公开披露或官方描述；未披露记为“未公开/未披露”。

### 1) DeepSeek

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| DeepSeek-V4：迈向高效百万 Token 上下文智能 | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence | DeepSeek-AI | DeepSeek-V4-Pro / DeepSeek-V4-Flash | 2026-04-24（预览）/ 2026-04-26（arXiv） | Pro：1.6T 总参数 / 49B 激活；Flash：284B / 13B；预训练 >32T tokens；上下文 1M | **架构**：CSA+HCA 混合注意力、DSA 稀疏选择、mHC 超连接稳定化；**训练**：Muon 优化器、领域专家培养+on-policy distillation；**长上下文**：1M 下推理 FLOPs/KV cache 大幅压缩（厂商自报） | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348), [官方新闻](https://www.deepseek.com/en/news/v4-preview/) |
| DeepSeek-V4.1-Flash：更聪明、更快、更高效 | Introducing DeepSeek-V4.1-Flash | DeepSeek-AI | DeepSeek-V4.1-Flash / V4.1-Flash-1017 | 2026-09-10（发布） | 552B MoE（公开材料）；非对称激活：约 8B 输入 / 16B 输出激活；原生视觉；上下文与具体配置以官方/模型页为准 | **架构**：因果编码器-解码器非对称；**效率**：KV cache/存储压缩导向 Agent 成本优化；**后训练**：更大规模 RL 与新预训练方法（厂商描述） | [官方新闻](https://www.deepseek.com/en/news/deepseek-v4-1-flash/), [HF: DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) |

### 2) OpenAI

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| GPT-6 Astra 系统卡 | GPT-6 Astra System Card | OpenAI | GPT-6 Astra | 2026-09-03 | 参数/数据未公开；面向长轨迹 agentic 与工具使用 | **推理/Agent**：大规模 RL、长时鲁棒性；**安全**：首次达 Preparedness 网络安全 Critical；对齐与 misalignment monitoring 披露 | [System Card](https://deploymentsafety.openai.com/gpt-6-astra) |
| GPT-6 Sol 与 GPT-6 Luna：2026 年 10 月更新 | GPT-6 Sol and GPT-6 Luna: October 2026 update | OpenAI | GPT-6 Sol / GPT-6 Luna | 2026-10-07（+10/29 Luna 增补） | 参数/数据未公开；统一系统替代 5.6 系列 | **对齐/鲁棒性**：多轮 jailbreak 抵抗、减少规避与不诚实；Luna 增补强调简洁与 instruction hierarchy 鲁棒性（厂商报告高分） | [System Card](https://deploymentsafety.openai.com/gpt-6-october), [Luna Addendum](https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum) |
| GPT-6 Cyber 系统卡 | GPT-6 Cyber System Card | OpenAI | GPT-6 Cyber（基于 GPT-6 Astra 专用后训练） | 2026-11-05 | 参数/数据未公开；授权安全工作场景 | **推理/安全**：漏洞发现、exploit、渗透测试导向；Preparedness 分级披露（Cyber Critical 等）；受限访问与身份/网络控制 | [System Card](https://deploymentsafety.openai.com/gpt-6-cyber) |
| GPT-Rosalind-6 系统卡增补 | GPT-Rosalind-6 System Card Addendum | OpenAI | GPT-Rosalind-6 | 2026-10-30 | 与 Astra 同权重家族（公开描述）；生物/药物发现专用后训练 | **领域推理**：生物前沿推理与受信访问；双用途风险分级与缓解并列披露 | [System Card](https://deploymentsafety.openai.com/gpt-rosalind-6) |

### 3) Meta AI (LLaMA / Muse)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Muse Wonder：面向个人与专业 AI Agent 的前沿模型 | Muse Wonder: A Frontier Model For Personal & Professional AI Agents | Meta AI | Muse Wonder / Muse Wonder Full | 2026-10-12 | 参数/训练数据未公开；原生多模态输入（text/image/video/audio）→text；1M 上下文 | **多模态+长上下文+Agent**：Active Memory/Active Focus 长时目标追踪；面向个人与专业 agent 场景 | [Blog](https://research.meta.ai/blog/muse-wonder), [Model Card](https://research.meta.ai/static/muse-wonder-model-card) |
| Muse Spark Open：开放权重前沿模型 | Introducing Muse Spark Open | Meta Superintelligence Labs | Muse Spark Open | 2026-10-15 | 816B 总参数 / 42B 激活；MoE（256 experts/layer, top-8）；62 层；1M 上下文；BF16/NVFP4 | **MoE 架构**：高稀疏激活；原生多模态；面向 agentic coding；开放权重与多推理栈支持 | [Blog](https://research.meta.ai/blog/muse-spark-open), [HF Blog](https://huggingface.co/blog/meta-muse-spark-open) |
| Muse Glimmer 30B：端侧 Agent 模型 | Muse Glimmer 30B: An On-Device Agentic Model | Meta AI | Muse Glimmer 30B | 2026-10-19 | 30B 参数（约 4-bit 量化可单 GPU 运行，公开描述）；text/image 输入 | **端侧+推理/工具**：多步推理、可靠工具调用与失败恢复；Apache 2.0 | [Meta Research](https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/) |

> 注：用户目标含“Meta AI (LLaMA)”；本期最新可验证一手材料以 Muse 系列为主，Llama 系列未见窗口内新增技术报告/系统卡更新。

### 4) Google DeepMind (Gemini)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Gemini 4 Argon 模型卡 | Gemini 4 Argon Model Card | Google DeepMind | Gemini 4 Argon | 2026-10-13 | 大规模稀疏 MoE Transformer（规模未公开）；原生 text/vision/audio 输入；1M 输入+输出上下文（模型卡描述）；知识截止 2026-03 | **多模态+长上下文+推理/Agent**：agentic coding、科学/数学与长上下文增强；配套安全与安全报告披露 CCL 风险评估 | [Model Card](https://deepmind.google/models/model-cards/gemini-4-argon/), [Safety Report](https://www.datocms-assets.com/142357/1792511849-gemini_4_safety_report.pdf) |
| Gemini Omni 1.2 Flash 模型卡更新 | Gemini Omni 1.2 Flash (Model Card Update) | Google DeepMind | Gemini Omni 1.2 Flash | 2026-11-05（更新） | 参数/数据未公开 | **多模态效率**：统一 Omni 快模型系列迭代，面向低延迟多模态交互（以模型卡页为准） | [Model Cards](https://deepmind.google/models/model-cards/) |

### 5) Anthropic (Claude)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Claude Opus 5.5 系统卡/发布材料 | Introducing Claude Opus 5.5 | Anthropic | Claude Opus 5.5 | 2026-09-22 | 参数/数据未公开；1M 上下文默认、128K 最大输出（公开材料） | **长上下文+推理/Agent**：长时 agentic coding 与知识工作；always-on adaptive thinking（厂商描述） | [News](https://www.anthropic.com/news/models), [System Cards](https://www.anthropic.com/system-cards) |
| Claude Sonnet 5.5 发布材料 | Introducing Claude Sonnet 5.5 | Anthropic | Claude Sonnet 5.5 | 2026-09-28 | 参数/数据未公开 | **效率与推理平衡**：速度/成本优化的主力模型迭代 | [News](https://www.anthropic.com/news/models) |
| Claude Haiku 5.5 系统卡 | Claude Haiku 5.5 System Card | Anthropic | Claude Haiku 5.5 | 2026-10-07 | 参数/数据未公开；1M 上下文、128K 输出；adaptive thinking + effort | **小模型推理+安全**：高吞吐低成本；纳入窄域高风险网络安全防护（RSP 框架内） | [System Card PDF](https://www-cdn.anthropic.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5/Claude%20Haiku%205.5%20System%20Card.pdf) |

### 6) Mistral AI

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Mistral Large 4（Le Chonk） | Introducing Mistral Large 4 | Mistral AI | Mistral Large 4 | 2026-10-06（预览）/ 2026-10-29（开源权重） | ~1.05T 总参数 / ~49B 激活（含 embedding 口径 ~52B）；72 层；128 routed experts top-4 + 1 shared；1M 上下文；1.6B 视觉编码器 | **MoE + 稀疏注意力**：MLA + DSA（top-2048）；原生多模态；agent-authored 可验证环境+RL 后训练；多推理档位；开放权重 | [Blog](https://mistral.ai/news/mistral-large-4/), [OSS](https://mistral.ai/news/mistral-large-4-oss/), [HF Blog](https://huggingface.co/blog/mistral-large4) |
| Timestral：概率时间序列基础模型族 | Timestral | Mistral AI | Timestral (5M/28M/123M/209M) | 2026-10-27 | 四尺寸参数量 5M–209M；时间序列基础模型（上下文/预测长度见论文） | **架构/训练**：Decoupled Horizon Forecasting、原生协变量支持；合成+真实后训练；GIFT-Eval/TIME/fev-bench 表现（厂商/论文自报） | [arXiv:2610.37585](https://arxiv.org/abs/2610.37585) |

### 7) Qwen (Alibaba)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Qwen3.8-Max：编码与协作新标杆 | Qwen3.8-Max: A New Bar for Coding and Cowork | Qwen Team, Alibaba | Qwen3.8-Max / Qwen3.8-2.4T-A95B | 2026-08-03 | 2.4T 总参数（MoE），约 95B 激活（公开命名口径）；~1M 上下文（产品/模型描述） | **MoE 扩展**：大规模旗舰 MoE；编码与长链路协作能力增强 | [Qwen Research](https://qwen.ai/research/), [HF](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) |
| Qwen3.8-Flash-Next：迈向极致成本效率的新架构 | Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost-Efficiency | Qwen Team, Alibaba | Qwen3.8-Flash-Next（`qwen4_exp` 预览） | 2026-08-26 | 125B 总参数 / 6B 激活（另含 n-gram embedding/MTP 组件，见模型页）；262K→1M 上下文（配置依部署） | **混合架构**：Gated DeltaNet + Gated Attention 混合；作为下一代架构预览，强调吞吐与成本效率 | [Qwen Research](https://qwen.ai/research/), [HF](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) |

> 2026-11-10 状态：Qwen4 正式发布未获可验证一手确认。

### 8) Yi (01.AI)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| （无 2026 年可验证新技术报告） | No verifiable new 2026 technical report/system card found | 01.AI | Yi 系列 | — | — | 公开主源未见 2026 年新旗舰技术报告/系统卡；以历史 Yi/Yi-Lightning 资料与产品更新为主 | [01.AI](https://www.01.ai/) |

### 9) Baichuan

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Baichuan 2：大规模开源语言模型 | Baichuan 2: Open Large-scale Language Models | Baichuan Inc. | Baichuan 2 (7B/13B) | 2023-09-19 | 7B / 13B；2.6T tokens 训练（报告口径） | **预训练基座**：中英双语开源基座；后续通用旗舰完整技术报告公开稀少 | [arXiv:2309.10305](https://arxiv.org/abs/2309.10305), [PDF](https://cdn.baichuan-ai.com/paper/Baichuan2-technical-report.pdf) |

> 2026-11-10 状态：通用大模型新技术报告未确认；近期公开重心偏垂直/医疗方向材料。

### 10) Microsoft (Phi)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Phi-4-Reasoning-Vision-15B 技术报告 | Phi-4-reasoning-vision-15B Technical Report | Microsoft Research | Phi-4-reasoning-vision-15B | 2026-03-04 | ~15B；text+image 输入；16,384 输入 tokens；动态分辨率视觉编码（最多 ~3,600 visual tokens） | **多模态推理**：SigLIP-2 编码器 + Phi-4-reasoning backbone 融合；推理/非推理混合训练；数据质量与合成增强 | [MSR](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/), [arXiv:2603.03975](https://arxiv.org/abs/2603.03975) |

### 11) Apple

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| 第三代 Apple 基础模型 | Introducing the Third Generation of Apple's Foundation Models | Apple | AFM 3（Core / Core Advanced / Cloud 等家族） | 2026-06-08（发布）/ 2026-09-14（Cloud 上线更新） | 家族化参数未全公开；Core 3B dense、Core Advanced 20B sparse（1–4B 激活）等公开描述；上下文/训练数据未完整披露 | **端云协同与效率**：IFP 稀疏激活/驻留策略、Apple silicon 定制、Private Cloud Compute 扩展；端侧隐私优先 | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |

### 12) NVIDIA

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Nemotron 3.5 Super 与 Lightning 技术报告 | Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI | NVIDIA | Nemotron 3.5 Super / Lightning | 2026-10-28（arXiv） | Super：120B / 12B 激活，多模态；Lightning：30B / 3B 激活，文本；1M 上下文；训练 token 与配方见报告 | **混合架构**：Mamba-Transformer MoE；**训练**：蒸馏、长上下文、MTP、RLVR/RLHF、MOPD；**推理效率**：NVFP4 与 speculative decoding | [arXiv:2610.38095](https://arxiv.org/abs/2610.38095), [PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf) |
| Nemotron 3.5 Bolt 74B-A9B 24GB 技术报告 | Nemotron 3.5 Bolt 74B-A9B 24GB: A Hybrid Vision-Language Model for Local AI | NVIDIA | Nemotron 3.5 Bolt 74B-A9B | 2026-10-15 | 74B 总参数 / ~9B 激活；面向 24GB 本地部署 | **压缩与端侧推理**：从更大模型压缩/蒸馏（Star Elastic 等，见报告）；混合架构与投机解码 | [PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-Technical-Report.pdf) |
| Nemotron 3.5 Transcribe 技术报告 | NVIDIA Nemotron 3.5 Transcribe Technical Report | NVIDIA | Nemotron 3.5 Transcribe | 2026-10-28 | 30B backbone / 34B checkpoint（含 MTP）/ ~4.3B active；40 语种；最长 1h 音频；65k token context（报告口径） | **多模态/语音**：SALM（语音编码器+diarization+LLM）、指令可控转写/翻译/说话人归属、长音频与时间戳对齐 | [PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) |

### 13) xAI (Grok)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Grok 4.7 模型卡 | Model Card: Grok 4.7 | xAI | Grok 4.7 | 2026-09-21 | 500K 上下文；text/image 输入、text 输出；参数量未官方确认（存在外部表述） | **推理/长任务 RL**：更长时 RL、self-verification、长上下文管理；推理档位与安全栈更新 | [Model Card PDF](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf), [xAI News](https://x.ai/news/grok-4-7) |

### 14) Amazon (Amazon Nova)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Amazon Nova 2：多模态推理与生成模型 | Amazon Nova 2: Multimodal reasoning and generation models | Amazon AGI | Nova 2（Lite/Pro/Omni/Sonic） | 2025-12-02 | 四款模型；最高 1M 上下文；多模态输入/输出能力依型号 | **多模态与推理**：可配置 extended thinking；统一多模态理解与生成；Responsible AI 护栏 | [Amazon Science](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models) |
| 在 Amazon 前沿模型安全框架下评估 Nova 2.0 Lite | Evaluating Nova 2.0 Lite model under Amazon's Frontier Model Safety Framework | Amazon | Nova 2.0 Lite | 2026-01-27 | 1M 上下文；text/image/video | **安全评估方法**：CBRN/网络/自动化 AI R&D 高风险域评估，自动基准+专家红队+uplift 研究 | [arXiv:2601.19134](https://arxiv.org/abs/2601.19134) |

### 15) Zhipu AI (GLM/ChatGLM)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| GLM-5.3：前沿编码与涌现网络能力 | GLM-5.3: Frontier Coding with Emergent Cyber Capabilities | Zhipu AI (Z.ai) | GLM-5.3 | 2026-08-14 | ~753B 总参数 / ~40B 激活（公开口径）；MoE + DSA | **后训练驱动提升**：纯后训练强化复杂编码与长时 Agent；可调思考强度 | [Blog](https://z.ai/blog/glm-5.3) |
| GLM-5.3-Flash：前沿智能，Flash 成本 | GLM-5.3-Flash: Frontier Intelligence, Flash Cost | Zhipu AI (Z.ai) | GLM-5.3-Flash | 2026-08-26 | 320B 总参数 / 18B 激活；原生多模态；混合稀疏+线性注意力（公开描述） | **效率+多模态**：高性价比 agentic/coding；原生多模态与混合注意力 | [Z.ai](https://z.ai/) |
| 视觉生成能否扩展统一多模态模型的知识？ | Can Visual Generation Expand What Unified Multimodal Models Know? | Tsinghua / Zhipu AI | GLM-Omni 研究（基于 GLM-4.1V-Thinking 等） | 2026-10-23 | 研究原型（9B 基座等，见论文） | **多模态推理研究**：Knowledge Transfer Probing；“先画后答”提升文本推理（论文自报） | [arXiv:2610.21459](https://arxiv.org/abs/2610.21459) |

### 16) InternLM (Shanghai AI Lab)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Intern-S2-Preview：科学 Agent 基础模型 | Intern-S2-Preview: Scientific Agentic Foundation Model | Shanghai AI Laboratory | Intern-S2-Preview-397B | 2026-08-14（arXiv）/ 2026-09-13（发布） | 397B 总参数 / A17B 激活；多模态 MoE；262K 上下文；MTP | **科学多模态+Agent**：科学语料预训练、统一后训练（SFT+RL+Agentic RL）、Memory Decoder 快速专业化 | [arXiv:2608.13505](https://arxiv.org/abs/2608.13505), [HF](https://huggingface.co/internlm/Intern-S2-Preview) |
| Intern-S2-Mobius：解耦知识存储与组合推理 | Intern-S2-Mobius | Shanghai AI Laboratory | Intern-S2-Mobius | 2026-08 | 架构族（具体规模见项目） | **新架构探索**：共享记忆池与跨层访问；推理效率与知识-推理解耦（项目宣称） | [GitHub](https://github.com/InternLM/Intern-S2-Mobius) |

### 17) Moonshot AI (Kimi)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Kimi K3.1 Pro 技术博客：推进开放智能 | Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence | Moonshot AI | Kimi K3.1 Pro / Highspeed | 2026-10-23（发布）/ 2026-11-04~05（权重） | 2.8T 总参数 / 104B 激活；93 层（KDA + full attention 混合）；896 experts、16 active；MXFP4/MXFP8；1M 上下文 | **MoE + 混合注意力**：KDA/MLA/DSA 组合与稀疏索引降解码成本；**后训练/RL**：大规模跨域联合 RL 与长上下文推理优化；Highspeed 吞吐变体 | [Blog](https://www.kimi.ai/blog/kimi-k3-1-pro), [HF](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) |

### 18) StepFun (阶跃星辰)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| 深入 Step 5 Preview：面向 Agentic 工作的架构与训练 | Inside Step 5 Preview: Architecture and Training for Agentic Work | StepFun | Step 5 Preview | 2026-09-20（API 预览）/ 2026-10-15（开放权重+技术博客） | 600B 总参数 / 27B 激活；92 层；1M 上下文、64K 输出；text+image/video 输入；BF16/FP8/NVFP4 | **架构**：Gated SWA 与稀疏 full-attention 交错、Sparse GQA；**训练**：稳定性优化、百万级可验证环境 RL、上下文压缩纳入策略训练 | [Blog](https://platform.stepfun.ai/blog/inside-step-5-preview), [官网](https://www.stepfun.com/step-5-preview/) |

### 19) ByteDance (豆包/Doubao)

| 中文标题 | 英文标题 | 发布机构 | 模型名称/系列 | 发布日期 | 核心参数（参数量/训练数据量/上下文长度等） | 主要创新点 | arXiv/论文链接 |
|---|---|---|---|---|---|---|---|
| Seed 2.0 模型卡：面向真实世界复杂度的智能前沿 | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity | ByteDance Seed | Seed 2.0（Pro/Lite/Mini） | 2026-06-19 | 参数/训练数据未公开；多模态（video/image/audio/text）与实时交互能力 | **全模态与 Agent**：App 生成、音视频理解、agentic coding/GUI 等综合能力 | [arXiv:2607.00248](https://arxiv.org/abs/2607.00248), [GitHub](https://github.com/ByteDance-Seed/Seed2.0) |
| Recycler：通过隐状态复用实现零成本潜在推理 | Recycler: Cost-Free Latent Reasoning via Hidden State Recycling | ByteDance Seed | Recycler（研究方法） | 2026-09-28 | 轻量 adapter（论文细节） | **推理效率研究**：隐状态回灌实现近零成本 latent reasoning，提升 loss/效率（论文自报） | [Seed Paper](https://seed.bytedance.com/zh/public_papers/1792932657675) |

## 按重点领域归纳

### 1. 大模型新架构（MoE, Mamba, hybrid）
- **稀疏 MoE 常态化**：DeepSeek-V4、Mistral Large 4、Kimi K3.1 Pro、Qwen3.8-Max、Muse Spark Open 等均采用大规模 MoE 与稀疏激活。
- **混合/稀疏注意力降本**：CSA+HCA（DeepSeek）、MLA+DSA（Mistral/Kimi/GLM 系）、Sparse GQA/交错窗口（Step 5）用于长上下文与解码效率。
- **Mamba-Transformer 混合落地**：NVIDIA Nemotron 3.5 系列在吞吐与长上下文场景体现 hybrid 优势；Intern-S2-Mobius 探索记忆解耦架构。

### 2. 训练方法（pre-training, post-training, alignment, RL）
- **后训练/RL 成主战场**：联合跨域 RL、agent-authored 可验证环境、多教师 on-policy distillation（MOPD 等）成为提升 coding/agent 的关键。
- **纯后训练显著增益**：GLM-5.3 等案例显示同基座后训练可带来可观能力提升。
- **对齐与安全训练前置**：OpenAI/Anthropic/Google 系统卡强化对齐、监测、越狱鲁棒性与高风险能力门控。

### 3. Scaling Law / 缩放分析
- **从参数缩放转向效率缩放**：关注每 token 成本、KV cache、每 GB 可用智能、量化与蒸馏带来的有效缩放。
- **蒸馏与压缩“造小做强”**：Nemotron 3.5 Bolt/Lightning、Muse Glimmer 等体现“teacher→student + 低比特/压缩”的实用路径。
- **时间序列/检索等子领域出现专用 scaling 规律**：如 Timestral 规模族与检索侧数据受限 scaling（参考近期开源研究与产品报告）。

### 4. 多模态模型
- **原生多模态成为旗舰默认**：Gemini 4 Argon、Muse 系列、Mistral Large 4、Seed 2.0、Nemotron 3.5 Super/Transcribe 等覆盖图文/音视频/文档。
- **理解-生成一体化与工具耦合**：Omni 系列与多模态 agent 强调“看-想-做”闭环；语音模型向长音频、说话人归属、可控转写演进。

### 5. 长上下文模型
- **1M 上下文普及，效率成瓶颈**：各家通过稀疏注意力、KV 压缩/索引、跨层共享与上下文管理策略提升可用性。
- **长时 Agent 场景驱动**：长上下文不只服务文档问答，更服务多步工具调用、代码库级任务与长轨迹规划。

### 6. 推理模型 / reasoning model
- **可调思考与混合推理普及**：low/medium/high/xhigh 或 effort 档位成为产品与模型接口常见设计。
- **推理与 RL/验证器耦合**：可验证环境、过程/结果奖励与自校验用于提升数学、代码与 agent 任务稳定性。
- **高风险能力评估制度化**：Preparedness/RSP/Frontier Safety Framework 成为系统卡核心组成，网络安全与生物安全能力分级披露更细。

## 数据来源与备注

- **保存路径**：`wiki/synthesis/2026-11-10/tech-report-digest.md`
- **数据来源**：arXiv、官方博客/新闻、模型卡与系统卡、Hugging Face、GitHub、NVIDIA Research、公司官网等公开渠道；并参考本仓库 `wiki/synthesis/2026-11-07/tech-report-digest.md` 的已整理条目进行增量复核。
- **局限性**：本次运行环境中通用网页搜索工具返回取消，部分“最新”状态依赖可直接抓取的 API/页面与仓库既有材料；如需逐篇 2026-11-07→11-10 新 arXiv 补全，建议后续补跑联网检索并更新本页。
- **口径提示**：闭源模型参数/数据细节多未披露；benchmark 为厂商或论文自报，跨模型不可简单横比；“发布/预览/权重开放/系统卡更新”为不同事件类型。

---
*注：本文档用于 LLM Wiki 日常技术报告追踪，信息以 2026-11-10 可获取公开材料为准，后续若出现新一手报告应追加修订并记录 log。*
