---
title: LLM 技术报告速览 — 2026-11-11
type: synthesis
created: 2026-11-11
updated: 2026-11-11
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-attention, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-11
# LLM Tech Report Digest — 2026-11-11

> 覆盖窗口：2026-11-10 → 2026-11-11（增量复核，基线为 [[2026-11-10/tech-report-digest]]）。本期对 19 家目标公司/组织的最新可验证大模型技术报告（Tech Report / Technical Report / System Card / Model Card / 官方技术博客）进行汇总。  
> 检索说明：本次运行中通用 `websearch` 工具不可用；已结合 `webfetch`（arXiv 搜索、Mistral/HF 博客、Gemini 4 Argon Model Card、Kimi/StepFun 官方博客等）、仓库既有 digest 与公开可访问信息复核。**窗口内未检索到可独立确认的全新一手旗舰技术报告/系统卡发布**；部分条目为近期已发布材料的细节补充与可获取性复核。  
> 口径说明：参数量、训练数据量、上下文长度、benchmark 等多为厂商/论文自报；闭源模型细节以官方系统卡/模型卡/博客为准；“预览/权重开放/系统卡更新/技术博客”与完整技术报告为不同披露层级。

## 本期结论（2026-11-11）

- **新增一手旗舰报告：未确认。** 19 家目标机构在 2026-11-10→11-11 窗口内未见可独立核实的新 Tech Report / System Card 首发；最新可验证材料仍主要来自 2026-09 至 2026-10。
- **可获取性/细节复核：** Mistral Large 4（Le Chonk）开放权重已发布（2026-10-29），官方发布页与 HF 博客可访问，完整技术报告页面在发布材料中被提及但本期未获取到独立 arXiv/PDF 全文；NVIDIA Nemotron 3.5 Super/Lightning 技术报告（arXiv:2610.38095）仍为该系列最新核心报告；Gemini 4 Argon Model Card 与安全报告为 Google DeepMind 当前最新旗舰披露。
- **趋势延续：** MoE + 稀疏/混合注意力主导长上下文与推理效率；后训练/RL、可验证环境与 agentic 评测成为能力提升关键；1M 级上下文在旗舰模型中常态化但依赖 KV/稀疏索引优化；系统卡对网络安全、生物安全、对齐与误用风险的分级披露持续加强。

## 重点关注方向速览

| 方向 | 代表进展（已发布/可验证） |
|---|---|
| 新架构（MoE / Mamba / Hybrid） | DeepSeek-V4 CSA+HCA+mHC；NVIDIA Nemotron 3.5 Mamba-Transformer Hybrid MoE；Mistral Large 4 MLA+DSA+MoE；Kimi K3.1 Pro KDA/MLA/DSA 混合；Qwen3.8-Flash-Next Gated DeltaNet+Gated Attention；Step 5 Preview Gated SWA + Sparse GQA 交错 |
| 训练方法（Pre/Post/Alignment/RL） | 大规模 RL 与可验证环境（DeepSeek/Mistral/StepFun/Kimi）；on-policy distillation/MOPD（Nemotron 3.5）；对齐与越狱鲁棒性强化（OpenAI/Anthropic/Google 系统卡）；后训练驱动增益（GLM-5.3 等） |
| Scaling Law / 缩放分析 | 从参数缩放转向效率/成本/有效智能缩放：激活参数、KV cache、每 token 成本、量化与蒸馏；长上下文与检索/serving 场景的系统级缩放 |
| 多模态模型 | Gemini 4 Argon、Meta Muse 系列、Mistral Large 4、Seed 2.0、Nemotron 3.5 Super/Transcribe、Phi-4-reasoning-vision、Apple AFM 3 等覆盖图文/音视频/文档/GUI |
| 长上下文模型 | 1M 上下文成为旗舰常见配置（DeepSeek-V4、Muse、Gemini 4 Argon、Nemotron 3.5、Kimi K3.1 Pro、Step 5 Preview 等）；关键技术为稀疏注意力、索引器、KV 压缩与上下文管理 |
| 推理模型 / Reasoning | 可调思考/effort 档位、长时 RL、自校验、可验证奖励与工具使用成为主线；系统卡同步披露高风险推理与网络/生物安全能力边界 |

---

## 各公司/组织最新可验证技术报告

### 1. DeepSeek

| 字段 | 内容 |
|---|---|
| 中文标题 | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| 英文标题 | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| 发布日期 | 2026-04-24（预览）/ 2026-04-26（arXiv） |
| 核心参数 | Pro：1.6T 总参数 / 49B 激活；Flash：284B 总参数 / 13B 激活；预训练 >32T tokens；上下文 1M tokens（官方/报告口径） |
| 主要创新点 | **架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 混合注意力、mHC（Manifold-Constrained Hyper-Connections）稳定深层训练；**训练**：Muon 优化器、领域专家培养与 on-policy distillation；**长上下文效率**：1M 上下文推理 FLOPs/KV cache 相比前代大幅压缩（厂商自报）。 |
| arXiv/论文链接 | https://arxiv.org/abs/2606.19348 ；官方新闻 https://www.deepseek.com/en/news/v4-preview/ |

| 字段 | 内容 |
|---|---|
| 中文标题 | DeepSeek-V4.1-Flash：更聪明、更快、更高效 |
| 英文标题 | Introducing DeepSeek-V4.1-Flash |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4.1-Flash / DeepSeek-V4.1-Flash-1017 |
| 发布日期 | 2026-09-10（发布） |
| 核心参数 | 552B MoE（公开材料）；非对称激活约 8B 输入 / 16B 输出；原生视觉能力；具体上下文与完整训练细节以官方/模型页为准 |
| 主要创新点 | **架构**：因果编码器-解码器非对称设计；**效率**：面向 agent 场景的 KV cache/存储与成本优化；**后训练**：更大规模 RL 与新预训练方法（厂商描述，完整技术报告披露有限）。 |
| arXiv/论文链接 | https://www.deepseek.com/en/news/deepseek-v4-1-flash/ ；HF https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017 |

**2026-11-11 状态：** 无新增一手 V4/V4.1 技术报告确认；arXiv 上近期多为基于/评测 DeepSeek-V4 系列的第三方工作。

### 2. OpenAI

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Astra 系统卡 |
| 英文标题 | GPT-6 Astra System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Astra |
| 发布日期 | 2026-09-03 |
| 核心参数 | 参数量/训练数据未公开；面向长轨迹 agentic 与工具使用场景 |
| 主要创新点 | **推理/Agent**：大规模 RL 与长时鲁棒性；**安全**：Preparedness 框架下网络安全能力分级披露（含 Critical 级讨论）；对齐与 misalignment monitoring 披露。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-astra |

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Sol 与 GPT-6 Luna：2026 年 10 月更新 |
| 英文标题 | GPT-6 Sol and GPT-6 Luna: October 2026 update |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Sol / GPT-6 Luna |
| 发布日期 | 2026-10-07（更新）；Luna 增补 2026-10-29 |
| 核心参数 | 参数量/训练数据未公开；统一系统替代 5.6 系列（公开描述） |
| 主要创新点 | **对齐/鲁棒性**：多轮 jailbreak 抵抗、减少规避与不诚实行为；Luna 增补强调简洁性与 instruction hierarchy/prompt injection 鲁棒性改进（厂商报告）。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-october ；Luna addendum https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum |

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Cyber 系统卡 |
| 英文标题 | GPT-6 Cyber System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Cyber（基于 GPT-6 Astra 专用后训练） |
| 发布日期 | 2026-11-05 |
| 核心参数 | 参数量/训练数据未公开；面向授权网络安全工作 |
| 主要创新点 | **安全导向推理**：漏洞发现、exploit、渗透测试等能力的受控释放；Preparedness 分级、访问控制与滥用缓解并列披露。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-cyber |

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-Rosalind-6 系统卡增补 |
| 英文标题 | GPT-Rosalind-6 System Card Addendum |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-Rosalind-6 |
| 发布日期 | 2026-10-30 |
| 核心参数 | 与 Astra 同权重家族（公开描述）；生物/药物发现专用后训练；细节未完全公开 |
| 主要创新点 | **领域推理与安全**：生物前沿推理与受信访问场景；双用途风险分级与缓解措施披露。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-rosalind-6 |

**2026-11-11 状态：** 无新增系统卡确认。

### 3. Meta AI (LLaMA)

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse Wonder：面向个人与专业 AI Agent 的前沿模型 |
| 英文标题 | Muse Wonder: A Frontier Model For Personal & Professional AI Agents |
| 发布机构 | Meta AI / Meta Superintelligence Labs |
| 模型名称/系列 | Muse Wonder / Muse Wonder Full |
| 发布日期 | 2026-10-12 |
| 核心参数 | 参数量/训练数据未公开；原生多模态输入（text/image/video/audio）→text；1M 上下文（模型卡/发布材料口径） |
| 主要创新点 | **多模态+长上下文+Agent**：面向个人与专业 agent 场景；Active Memory/Active Focus 等长时目标追踪机制（公开描述）。 |
| arXiv/论文链接 | https://research.meta.ai/blog/muse-wonder ；Model Card https://research.meta.ai/static/muse-wonder-model-card |

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse Spark Open：开放权重前沿模型 |
| 英文标题 | Introducing Muse Spark Open |
| 发布机构 | Meta Superintelligence Labs |
| 模型名称/系列 | Muse Spark Open |
| 发布日期 | 2026-10-15 |
| 核心参数 | 816B 总参数 / 42B 激活；MoE（256 experts/layer, top-8）；62 层；1M 上下文；BF16/NVFP4（公开材料） |
| 主要创新点 | **高稀疏 MoE**：大规模开放权重；原生多模态；面向 agentic coding 与多推理栈部署。 |
| arXiv/论文链接 | https://research.meta.ai/blog/muse-spark-open ；HF https://huggingface.co/blog/meta-muse-spark-open |

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse Glimmer 30B：端侧 Agent 模型 |
| 英文标题 | Muse Glimmer 30B: An On-Device Agentic Model |
| 发布机构 | Meta AI |
| 模型名称/系列 | Muse Glimmer 30B |
| 发布日期 | 2026-10-19 |
| 核心参数 | 30B 参数（约 4-bit 量化可单 GPU 运行，公开描述）；text/image 输入；训练数据/上下文细节未完整披露 |
| 主要创新点 | **端侧推理与工具使用**：多步推理、可靠工具调用与失败恢复；Apache 2.0 开放。 |
| arXiv/论文链接 | https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/ |

**2026-11-11 状态：** 目标含 LLaMA，但本期最新可验证一手材料以 Muse 系列为主；未见 Llama 系列新增技术报告/系统卡。

### 4. Google DeepMind (Gemini)

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 Argon 模型卡 |
| 英文标题 | Gemini 4 Argon Model Card |
| 发布机构 | Google DeepMind |
| 模型名称/系列 | Gemini 4 Argon |
| 发布日期 | 2026-10-13 |
| 核心参数 | 大规模稀疏 MoE Transformer（参数规模未公开）；原生 text/vision/audio 输入；Model Card 标注 combined input-output token context window up to 1M；输出可达 1M token input+output（模型卡口径）；知识截止 2026-03 |
| 主要创新点 | **多模态+长上下文+推理/Agent**：agentic coding、企业知识工作、科学/数学与网络安全防御；支持长上下文与多模态理解；配套安全报告披露关键能力与 CCL 评估。 |
| arXiv/论文链接 | https://deepmind.google/models/model-cards/gemini-4-argon/ ；PDF https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf ；Safety Report https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf |

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini Omni 1.2 Flash 模型卡更新 |
| 英文标题 | Gemini Omni 1.2 Flash (Model Card Update) |
| 发布机构 | Google DeepMind |
| 模型名称/系列 | Gemini Omni 1.2 Flash |
| 发布日期 | 2026-11-05（更新，仓库既有记录） |
| 核心参数 | 参数量/训练数据未公开；面向低延迟多模态交互（以模型卡页为准） |
| 主要创新点 | **多模态效率迭代**：Omni 快模型系列更新，强调实时/低延迟多模态能力。 |
| arXiv/论文链接 | https://deepmind.google/models/model-cards/ （具体子页以官方发布为准） |

**2026-11-11 状态：** 无新增 Gemini 旗舰模型卡确认。

### 5. Anthropic (Claude)

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Opus 5.5 系统卡/发布材料 |
| 英文标题 | Introducing Claude Opus 5.5 / Claude Opus 5.5 System Card materials |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Opus 5.5 |
| 发布日期 | 2026-09-22 |
| 核心参数 | 参数量/训练数据未公开；1M 上下文、128K 最大输出（公开材料口径） |
| 主要创新点 | **长上下文+推理/Agent**：长时 agentic coding 与知识工作；adaptive thinking；安全与对齐评估纳入系统卡体系。 |
| arXiv/论文链接 | https://www.anthropic.com/news/models ；https://www.anthropic.com/system-cards |

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Sonnet 5.5 发布材料 |
| 英文标题 | Introducing Claude Sonnet 5.5 |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Sonnet 5.5 |
| 发布日期 | 2026-09-28 |
| 核心参数 | 参数量/训练数据未公开 |
| 主要创新点 | **效率与推理平衡**：速度/成本优化的主力模型迭代，面向广泛编码与 agent 场景。 |
| arXiv/论文链接 | https://www.anthropic.com/news/models |

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Haiku 5.5 系统卡 |
| 英文标题 | Claude Haiku 5.5 System Card |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Haiku 5.5 |
| 发布日期 | 2026-10-07 |
| 核心参数 | 参数量/训练数据未公开；1M 上下文、128K 输出；支持 adaptive thinking 与 effort（公开材料） |
| 主要创新点 | **小模型推理+安全**：高吞吐低成本；在 RSP 框架下纳入窄域高风险网络安全防护与评估。 |
| arXiv/论文链接 | https://www-cdn.anthropic.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5/Claude%20Haiku%205.5%20System%20Card.pdf |

**2026-11-11 状态：** 无新增系统卡确认。

### 6. Mistral AI

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4（Le Chonk）：面向编程与防御者的开放权重模型 |
| 英文标题 | Mistral Large 4 (Le Chonk): Built for Coders, Trusted by Defenders |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Mistral Large 4 |
| 发布日期 | 2026-10-06（预览）/ 2026-10-29（开放权重与更新发布） |
| 核心参数 | ~1T 级总参数（官方/博客表述，含 embedding 口径略有差异）；~49B 激活（HF/发布材料）；72 层；128 routed experts/layer top-4 + 1 shared expert；1M 上下文；1.6B 视觉编码器（Pixtral 系）；FP8/NVFP4 等格式 |
| 主要创新点 | **MoE + 稀疏注意力**：MLA + DSA（top-k 选择）与稀疏/高效长上下文设计；**多模态**：原生 text+image 输入；**训练/后训练**：面向 coding/cyber/agentic 的 RL 与推理效率优化，支持多推理档位（low/medium/high）；**开放权重**：可下载与自托管，强调主权与可定制。 |
| arXiv/论文链接 | https://mistral.ai/news/mistral-large-4-oss/ ；HF https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B ；HF Blog https://huggingface.co/blog/mistral-large4 ；发布材料提及 technical report（本期未获取独立 PDF/arXiv 全文链接） |

| 字段 | 内容 |
|---|---|
| 中文标题 | Timestral：概率时间序列基础模型族 |
| 英文标题 | Timestral |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Timestral (5M / 28M / 123M / 209M) |
| 发布日期 | 2026-10-27 |
| 核心参数 | 四种参数规模 5M–209M；时间序列基础模型（上下文/预测长度与训练数据细节见论文） |
| 主要创新点 | **时间序列架构与训练**：Decoupled Horizon Forecasting、原生协变量支持；合成+真实数据后训练；在 GIFT-Eval/TIME/fev-bench 等基准表现（论文/厂商自报）。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.37585 |

**2026-11-11 状态：** Large 4 完整学术技术报告文本本期未独立确认；权重与官方技术说明已公开。

### 7. Qwen (Alibaba)

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.8-Max：编码与协作新标杆 |
| 英文标题 | Qwen3.8-Max: A New Bar for Coding and Cowork |
| 发布机构 | Qwen Team, Alibaba |
| 模型名称/系列 | Qwen3.8-Max / Qwen3.8-2.4T-A95B |
| 发布日期 | 2026-08-03 |
| 核心参数 | 2.4T 总参数（MoE），约 95B 激活（公开命名口径）；~1M 上下文（产品/模型描述）；训练数据细节未完整公开 |
| 主要创新点 | **大规模 MoE 扩展**：旗舰编码与长链路协作能力增强；面向复杂工程与 agent 工作流。 |
| arXiv/论文链接 | https://qwen.ai/research/ ；HF https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.8-Flash-Next：迈向极致成本效率的新架构 |
| 英文标题 | Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost-Efficiency |
| 发布机构 | Qwen Team, Alibaba |
| 模型名称/系列 | Qwen3.8-Flash-Next（`qwen4_exp` 预览） |
| 发布日期 | 2026-08-26 |
| 核心参数 | 125B 总参数 / 6B 激活（另含 n-gram embedding/MTP 等组件，见模型页）；262K→1M 上下文（依配置/部署） |
| 主要创新点 | **混合架构**：Gated DeltaNet + Gated Attention；作为下一代架构预览，强调吞吐与成本效率。 |
| arXiv/论文链接 | https://qwen.ai/research/ ；HF https://huggingface.co/Qwen/Qwen3.8-Flash-Next |

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.5-Omni 技术报告 |
| 英文标题 | Qwen3.5-Omni Technical Report |
| 发布机构 | Qwen Team, Alibaba |
| 模型名称/系列 | Qwen3.5-Omni / Qwen3.5-Omni-plus |
| 发布日期 | 2026-04-17（arXiv 提交）/ 2026-04-20（更新） |
| 核心参数 | 百亿至千亿级规模（报告表述）；256K 上下文；支持 >10 小时音频理解与 400 秒 720P 视频（1 FPS，报告口径）；多语言（10 种语音生成等） |
| 主要创新点 | **全模态架构**：Thinker/Talker 混合注意力 MoE；ARIA 动态对齐文本与语音单元提升流式语音稳定性；音视频理解/推理/交互与结构化时间对齐字幕能力。 |
| arXiv/论文链接 | https://arxiv.org/abs/2604.15804 |

**2026-11-11 状态：** Qwen4 正式版未确认发布；`qwen4_exp` 仍为预览信号。

### 8. Yi (01.AI)

| 字段 | 内容 |
|---|---|
| 中文标题 | Yi：开源基础模型（历史代表报告） |
| 英文标题 | Yi: Open Foundation Models by 01.AI |
| 发布机构 | 01.AI |
| 模型名称/系列 | Yi (6B/34B 等历史系列) |
| 发布日期 | 2024-03-07（arXiv） |
| 核心参数 | 6B/34B 等 dense 基座；3.1T 多语种 tokens 训练（报告口径）；上下文依版本而异 |
| 主要创新点 | **双语预训练基座**：中英能力与数据/训练配方披露；后续 Yi-Lightning 等产品线更新多为 API/产品形式。 |
| arXiv/论文链接 | https://arxiv.org/abs/2403.04652 ；https://www.01.ai/ |

**2026-11-11 状态：** 未检索到 2026 年可验证的新旗舰通用技术报告/系统卡。

### 9. Baichuan

| 字段 | 内容 |
|---|---|
| 中文标题 | Baichuan 2：大规模开源语言模型 |
| 英文标题 | Baichuan 2: Open Large-scale Language Models |
| 发布机构 | Baichuan Inc. |
| 模型名称/系列 | Baichuan 2 (7B/13B) |
| 发布日期 | 2023-09-19 |
| 核心参数 | 7B / 13B；2.6T tokens 训练（报告口径） |
| 主要创新点 | **开源中英双语基座**：完整训练与评测披露；近期公开重心更多在垂直/医疗方向，通用旗舰新技术报告稀少。 |
| arXiv/论文链接 | https://arxiv.org/abs/2309.10305 ；https://cdn.baichuan-ai.com/paper/Baichuan2-technical-report.pdf |

**2026-11-11 状态：** 未确认通用大模型新技术报告。

### 10. Microsoft (Phi)

| 字段 | 内容 |
|---|---|
| 中文标题 | Phi-4-Reasoning-Vision-15B 技术报告 |
| 英文标题 | Phi-4-reasoning-vision-15B Technical Report |
| 发布机构 | Microsoft Research |
| 模型名称/系列 | Phi-4-reasoning-vision-15B |
| 发布日期 | 2026-03-04 |
| 核心参数 | ~15B；text+image 输入；16,384 输入 tokens；动态分辨率视觉编码（最多 ~3,600 visual tokens，报告口径） |
| 主要创新点 | **多模态推理**：SigLIP-2 视觉编码器与 Phi-4-reasoning backbone 融合；推理/非推理混合训练；强调数据质量与合成增强。 |
| arXiv/论文链接 | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ ；https://arxiv.org/abs/2603.03975 |

**2026-11-11 状态：** 未确认 Phi-5 官方技术报告。

### 11. Apple

| 字段 | 内容 |
|---|---|
| 中文标题 | 第三代 Apple 基础模型 |
| 英文标题 | Introducing the Third Generation of Apple's Foundation Models |
| 发布机构 | Apple |
| 模型名称/系列 | Apple Foundation Models / AFM 3（Core, Core Advanced, Cloud 等家族） |
| 发布日期 | 2026-06-08（发布）/ 2026-09-14（Cloud 上线更新，公开记录） |
| 核心参数 | 家族化参数未全公开；公开描述包括 Core 3B dense、Core Advanced 20B sparse（约 1–4B 激活）等；上下文与训练数据未完整披露 |
| 主要创新点 | **端云协同与效率**：IFP 稀疏激活/驻留策略、Apple silicon 定制优化、Private Cloud Compute 扩展；隐私优先的端侧与云端协同。 |
| arXiv/论文链接 | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models （未见对应 arXiv 完整技术报告） |

**2026-11-11 状态：** 无新增 arXiv 技术报告确认。

### 12. NVIDIA

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Super 与 Lightning：面向 Agentic AI 的开放高效混合 Mamba-Transformer MoE 模型 |
| 英文标题 | Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Super / Nemotron 3.5 Lightning |
| 发布日期 | 2026-10-28（arXiv） |
| 核心参数 | Super：120B 总参数 / 12B 激活，多模态；Lightning：30B 总参数 / 3B 激活，文本；1M 上下文；训练 token 与配方详见报告 |
| 主要创新点 | **混合架构**：Mamba-Transformer MoE；**训练/后训练**：蒸馏、长上下文、MTP、RLVR/RLHF、MOPD 等；**推理效率**：NVFP4 与 speculative decoding。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.38095 ；https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf |

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Bolt 74B-A9B 24GB：面向本地 AI 的混合视觉语言模型 |
| 英文标题 | Nemotron 3.5 Bolt 74B-A9B 24GB: A Hybrid Vision-Language Model for Local AI |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Bolt 74B-A9B |
| 发布日期 | 2026-10-15 |
| 核心参数 | 74B 总参数 / ~9B 激活；面向 24GB 本地部署（报告口径） |
| 主要创新点 | **压缩与本地推理**：从更大模型压缩/蒸馏；混合架构与投机解码支持低显存部署。 |
| arXiv/论文链接 | https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-Technical-Report.pdf |

| 字段 | 内容 |
|---|---|
| 中文标题 | NVIDIA Nemotron 3.5 Transcribe 技术报告 |
| 英文标题 | NVIDIA Nemotron 3.5 Transcribe Technical Report |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Transcribe |
| 发布日期 | 2026-10-28 |
| 核心参数 | 30B backbone / 34B checkpoint（含 MTP，报告口径）/ ~4.3B active；40 语种；最长 1 小时音频；65k token context（报告口径） |
| 主要创新点 | **语音多模态**：SALM（语音编码器+diarization+LLM）；指令可控转写/翻译/说话人归属；长音频与时间戳对齐。 |
| arXiv/论文链接 | https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf |

**2026-11-11 状态：** 无新增 Nemotron 技术报告确认。

### 13. xAI (Grok)

| 字段 | 内容 |
|---|---|
| 中文标题 | Grok 4.7 模型卡 |
| 英文标题 | Model Card: Grok 4.7 |
| 发布机构 | xAI |
| 模型名称/系列 | Grok 4.7 |
| 发布日期 | 2026-09-21 |
| 核心参数 | 500K 上下文；text/image 输入、text 输出；参数量未官方确认（存在外部表述） |
| 主要创新点 | **推理与长任务 RL**：更长时 RL、自校验与长上下文管理；多推理档位与安全栈更新（模型卡口径）。 |
| arXiv/论文链接 | https://media.x.ai/v1/website/card4p7-3a96f40b.pdf ；https://x.ai/news/grok-4-7 |

**2026-11-11 状态：** 未确认 Grok 4.8 发布/系统卡。

### 14. Amazon (Amazon Nova)

| 字段 | 内容 |
|---|---|
| 中文标题 | Amazon Nova 2：多模态推理与生成模型 |
| 英文标题 | Amazon Nova 2: Multimodal reasoning and generation models |
| 发布机构 | Amazon AGI / Amazon Science |
| 模型名称/系列 | Nova 2（Lite/Pro/Omni/Sonic） |
| 发布日期 | 2025-12-02 |
| 核心参数 | 四款模型家族；最高 1M 上下文；多模态输入/输出能力依型号而异 |
| 主要创新点 | **多模态与推理**：可配置 extended thinking；统一多模态理解与生成；配套 Responsible AI 护栏。 |
| arXiv/论文链接 | https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models |

| 字段 | 内容 |
|---|---|
| 中文标题 | 在 Amazon 前沿模型安全框架下评估 Nova 2.0 Lite |
| 英文标题 | Evaluating Nova 2.0 Lite model under Amazon's Frontier Model Safety Framework |
| 发布机构 | Amazon |
| 模型名称/系列 | Nova 2.0 Lite |
| 发布日期 | 2026-01-27 |
| 核心参数 | 1M 上下文；text/image/video 输入（评估口径） |
| 主要创新点 | **安全评估方法**：覆盖 CBRN、网络、自动化 AI R&D 等高风险域，结合自动基准、专家红队与 uplift 研究。 |
| arXiv/论文链接 | https://arxiv.org/abs/2601.19134 |

**2026-11-11 状态：** 无新增 Nova 技术报告确认。

### 15. Zhipu AI (GLM/ChatGLM)

| 字段 | 内容 |
|---|---|
| 中文标题 | GLM-5.3：前沿编码与涌现网络能力 |
| 英文标题 | GLM-5.3: Frontier Coding with Emergent Cyber Capabilities |
| 发布机构 | Zhipu AI (Z.ai) |
| 模型名称/系列 | GLM-5.3 |
| 发布日期 | 2026-08-14 |
| 核心参数 | ~753B 总参数 / ~40B 激活（公开口径）；MoE + DSA（公开描述） |
| 主要创新点 | **后训练强化**：纯后训练带来复杂编码与长时 agent 能力提升；可调思考强度。 |
| arXiv/论文链接 | https://z.ai/blog/glm-5.3 |

| 字段 | 内容 |
|---|---|
| 中文标题 | GLM-5.3-Flash：前沿智能，Flash 成本 |
| 英文标题 | GLM-5.3-Flash: Frontier Intelligence, Flash Cost |
| 发布机构 | Zhipu AI (Z.ai) |
| 模型名称/系列 | GLM-5.3-Flash |
| 发布日期 | 2026-08-26 |
| 核心参数 | 320B 总参数 / 18B 激活；原生多模态；混合稀疏+线性注意力（公开描述） |
| 主要创新点 | **效率与多模态**：高性价比 agentic/coding；原生多模态与混合注意力设计。 |
| arXiv/论文链接 | https://z.ai/ （官方发布页/博客） |

| 字段 | 内容 |
|---|---|
| 中文标题 | 视觉生成能否扩展统一多模态模型的知识？ |
| 英文标题 | Can Visual Generation Expand What Unified Multimodal Models Know? |
| 发布机构 | Tsinghua / Zhipu AI（论文作者单位） |
| 模型名称/系列 | GLM-Omni 研究原型 |
| 发布日期 | 2026-10-23 |
| 核心参数 | 研究原型（如 9B 基座等，详见论文） |
| 主要创新点 | **多模态推理研究**：Knowledge Transfer Probing；“先画后答”在部分文本推理任务提升（论文自报）。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.21459 |

**2026-11-11 状态：** 未确认 GLM-5.4/5.5 发布。

### 16. InternLM (Shanghai AI Lab)

| 字段 | 内容 |
|---|---|
| 中文标题 | Intern-S2-Preview：科学 Agent 基础模型 |
| 英文标题 | Intern-S2-Preview: Scientific Agentic Foundation Model |
| 发布机构 | Shanghai AI Laboratory |
| 模型名称/系列 | Intern-S2-Preview-397B |
| 发布日期 | 2026-08-14（arXiv）/ 2026-09-13（发布） |
| 核心参数 | 397B 总参数 / 17B 激活（A17B 口径）；多模态 MoE；262K 上下文；MTP |
| 主要创新点 | **科学多模态+Agent**：科学语料预训练、统一后训练（SFT+RL+Agentic RL）、Memory Decoder 快速专业化。 |
| arXiv/论文链接 | https://arxiv.org/abs/2608.13505 ；https://huggingface.co/internlm/Intern-S2-Preview |

| 字段 | 内容 |
|---|---|
| 中文标题 | Intern-S2-Mobius：解耦知识存储与组合推理 |
| 英文标题 | Intern-S2-Mobius |
| 发布机构 | Shanghai AI Laboratory |
| 模型名称/系列 | Intern-S2-Mobius |
| 发布日期 | 2026-08（项目公开时间线口径） |
| 核心参数 | 架构族，具体规模与训练细节见项目文档 |
| 主要创新点 | **新架构探索**：共享记忆池与跨层访问，探索知识-推理解耦与效率提升。 |
| arXiv/论文链接 | https://github.com/InternLM/Intern-S2-Mobius |

**2026-11-11 状态：** 无新增技术报告确认。

### 17. Moonshot AI (Kimi)

| 字段 | 内容 |
|---|---|
| 中文标题 | Kimi K3.1 Pro 技术博客：推进开放智能 |
| 英文标题 | Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence |
| 发布机构 | Moonshot AI |
| 模型名称/系列 | Kimi K3.1 Pro / Kimi K3.1 Pro Highspeed |
| 发布日期 | 2026-10-23（发布）/ 2026-11-04（权重计划，博客口径） |
| 核心参数 | 2.8T 总参数 / 104B 激活；93 层（KDA + full attention 混合）；896 experts、16 active；MXFP4/MXFP8；1M 上下文；Highspeed 提供 2–3× 速度变体（博客口径） |
| 主要创新点 | **MoE + 混合注意力**：KDA/MLA/DSA 等组合与稀疏索引降解码成本；**后训练/RL**：大规模跨域联合 RL 提升 coding/agent/金融/3D 等能力；**长上下文**：面向长轨迹 agentic 工作负载优化。 |
| arXiv/论文链接 | https://www.kimi.ai/blog/kimi-k3-1-pro ；HF https://huggingface.co/moonshotai/Kimi-K3.1-Pro （技术报告论文链接以官方后续发布为准） |

**2026-11-11 状态：** 未见新增独立技术报告论文；权重与技术博客已是当前最完整一手材料。

### 18. StepFun (阶跃星辰)

| 字段 | 内容 |
|---|---|
| 中文标题 | 深入 Step 5 Preview：面向 Agentic 工作的架构与训练 |
| 英文标题 | Inside Step 5 Preview: Architecture and Training for Agentic Work |
| 发布机构 | StepFun |
| 模型名称/系列 | Step 5 Preview |
| 发布日期 | 2026-09-20（API 预览）/ 2026-10-15（开放权重+技术博客） |
| 核心参数 | 600B 总参数 / 27B 激活；92 层；1M 上下文、64K 输出；text+image/video 输入；BF16/FP8/NVFP4（博客/发布材料） |
| 主要创新点 | **架构**：窄而深设计，3:1 Gated SWA 与 Sparse GQA（block-wise token merging 索引）交错；**训练稳定性**：FP32 hidden state/RMSNorm scale、细粒度梯度裁剪；**Agentic 数据与 RL**：可验证环境、百万级轨迹与上下文管理/信用分配优化。 |
| arXiv/论文链接 | https://platform.stepfun.ai/blog/inside-step-5-preview ；https://www.stepfun.com/step-5-preview/ （完整 arXiv 技术报告本期未见） |

**2026-11-11 状态：** 技术博客为主要一手技术披露。

### 19. ByteDance (豆包/Doubao)

| 字段 | 内容 |
|---|---|
| 中文标题 | Seed 2.0 模型卡：面向真实世界复杂度的智能前沿 |
| 英文标题 | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity |
| 发布机构 | ByteDance Seed |
| 模型名称/系列 | Seed 2.0（Pro / Lite / Mini） |
| 发布日期 | 2026-06-19 |
| 核心参数 | 参数量/训练数据未公开；多模态（video/image/audio/text）与实时交互能力（模型卡口径） |
| 主要创新点 | **全模态与 Agent**：App 生成、音视频理解、agentic coding/GUI 等综合能力；面向真实复杂任务的系统化评测披露。 |
| arXiv/论文链接 | https://arxiv.org/abs/2607.00248 ；https://github.com/ByteDance-Seed/Seed2.0 |

| 字段 | 内容 |
|---|---|
| 中文标题 | Recycler：通过隐状态复用实现零成本潜在推理 |
| 英文标题 | Recycler: Cost-Free Latent Reasoning via Hidden State Recycling |
| 发布机构 | ByteDance Seed |
| 模型名称/系列 | Recycler（研究方法/模型研究） |
| 发布日期 | 2026-09-28（公开页面口径） |
| 核心参数 | 轻量 adapter 等实现细节见论文/页面 |
| 主要创新点 | **推理效率研究**：隐状态回灌实现近零成本 latent reasoning，提升推理效率与效果（论文自报）。 |
| arXiv/论文链接 | https://seed.bytedance.com/zh/public_papers/1792932657675 |

**2026-11-11 状态：** 未确认 Seed 系列新增完整旗舰技术报告。

---

## 备注与待跟踪项

- **Yi (01.AI)、Baichuan**：2026 年通用旗舰新技术报告/系统卡公开证据不足，本期以历史代表报告占位并标注状态。
- **Mistral Large 4**：开放权重与官方技术说明已充分，但“完整学术技术报告”PDF/arXiv 本期未独立抓取到可引用全文链接，后续可补全。
- **Apple AFM 3**：官方技术文章为主要披露形式，未见 arXiv 完整技术报告。
- **Kimi K3.1 Pro / Step 5 Preview / GLM 系列**：当前以技术博客/模型页为主，若后续发布 arXiv 技术报告应补录。
- **验证建议**：后续联网恢复后，建议针对各公司官网 newsroom、arXiv cs.CL/cs.LG、Hugging Face papers、模型卡仓库做 24h 增量扫描并更新本页。

---
*数据基准：2026-11-11 可获取公开材料；本文档为 LLM Wiki 日常追踪 synthesis，不构成能力或安全的独立验证结论。*
