---
title: LLM 技术报告速览 — 2026-10-28
type: synthesis
created: 2026-10-28
updated: 2026-10-28
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, scaling-law, daily-digest]
---

# LLM 技术报告速览 — 2026-10-28

> 覆盖窗口：2026-10-21 → 2026-10-28（以 2026-10-28 抓取为准）。10-28 当日未检索到新的一手技术报告；本期重点复核 10-21 至 10-27 的关键材料，并补正 [[tech-report-digest]]（2026-10-27）中的参数与版本误差。
>
> 口径：优先使用官方模型卡、系统卡、技术报告与开发者文档；厂商自报 benchmark 与第三方报道分开标注；未证实传闻不进入主表。

## 本期结论

- **小版本系统卡密集落地**：OpenAI 在 10-26 追加 GPT-6.1 Terra 系统卡，Anthropic 在 10-07 发布 Haiku 5.5，Google 在 10-13 更新 Gemini 4 Argon。三家的共同点是「低成本高吞吐 + computer use / 视觉推理」，而不是继续堆参数。
- **开放权重继续逼近 frontier**：Meta Muse Spark Open（816B/42B）、Muse Glimmer 30B、NVIDIA Nemotron 3.5、DeepSeek V4.1-Flash、Qwen3.8-Flash-Next、Kimi K3、GLM-5.3 构成 2026 年 7–10 月的开放权重梯队。
- **1M context 已成旗舰标配**：差异化从「能不能 1M」转向「1M 下的 KV cache、prefill/decode 激活参数、输出 token 成本」。DeepSeek 的 CED + FP4 KV、Qwen 的 GDN/QSA hybrid、Mistral 的 52B active 都是同一方向。
- **后训练成为独立 scaling 轴**：GLM-5.3 与 GLM-5.2 同基座，全部增益来自 post-training；Kimi K3.1 Pro 也以大规模 post-training 为主。预训练差距缩小后，RL 环境、数据与 agent harness 成为新的护城河。
- **架构收敛**：MoE + 混合线性/稀疏注意力 + MTP/speculative decoding + n-gram embedding 的组合反复出现；纯 dense 只在中端模型（Muse Glimmer、AFM 3 Core）保留。
- **本期最大未决项**：Mistral Large 4 权重在 10-27 仍未发布，HF 倒计时指向 10-31 15:00Z；Phi-5 仍无官方技术报告；Apple AFM 3 仍只有模型文档，没有 arXiv 报告。

## 公司与组织覆盖

| 公司/组织 | 最新已核实材料 | 日期 | 关键规格 / 状态 |
|---|---|---|---|
| [OpenAI](https://openai.com/) | [Introducing GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra/) + [System Card Addendum](https://deploymentsafety.openai.com/gpt-6-1-terra) | 2026-10-26 | 闭源；1.05M context / 922K max input / 128K output；text+image；cyber Critical |
| [Anthropic](https://www.anthropic.com/) | [Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) + System Card | 2026-10-07 | 1M context / 128K output；$0.10/$0.50 per MTok；adaptive thinking |
| [Google DeepMind](https://deepmind.google/) | [Gemini 4 Argon Model Card](https://deepmind.google/models/model-cards/gemini-4-argon/) | 2026-10-13 | 稀疏 MoE；1M 输入+输出；原生 text/image/audio；knowledge cutoff 2026-03 |
| [Meta AI](https://ai.meta.com/) | [Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) + [Muse Glimmer 30B](https://arxiv.org/abs/2610.24628) | 2026-10-15 / 2026-10-23 | 816B/42B open-weight；30B dense，128K+，Apache 2.0 |
| [NVIDIA](https://research.nvidia.com/labs/nemotron/) | [Nemotron 3.5 Super & Lightning Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf) | 2026-10-21 | Super 120B/12B 多模态；Lightning 30B/3B 文本；hybrid Mamba-Transformer MoE |
| [xAI](https://x.ai/) | [Grok 4.7 Model Card](https://media.x.ai/v1/website/4p7card-5eccc980.pdf) | 2026-09-21 | 500K context；text+image；CursorBench 4.0 46.3（xhigh）；$2/$6 |
| [DeepSeek](https://www.deepseek.com/) | [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) | 2026-09-17 | 552B backbone；16B decode / 8B prefill；1M context；CED + FP4 KV |
| [Qwen (Alibaba)](https://qwen.ai/) | [Qwen3.8-Flash-Next Tech Report](https://github.com/QwenLM/Qwen3.8-Flash-Next) | 2026-08-26 | 125B/6B + 51B n-gram + 4B MTP；262,144 native / 1M extensible |
| [Moonshot AI](https://www.kimi.com/) | [Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) + [Kimi K3](https://arxiv.org/abs/2607.24653) | 2026-10-23 / 2026-07-27 | 3T-class / 2.8T-104B；1M context；KDA + Attention Residuals |
| [Zhipu AI](https://z.ai/) | [GLM-5.3](https://z.ai/blog/glm-5.3) | 2026-08-14 | 753B/~40B；与 GLM-5.2 同基座，全部增益来自 post-training |
| [Mistral AI](https://mistral.ai/) | [Mistral Large 4](https://mistral.ai/news/mistral-large-4/) | 2026-10-06 preview | 1.05T total / 52B active / 1.6B vision；1M context；权重待发布 |
| [Apple](https://machinelearning.apple.com/) | [AFM 3](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) | 2026-06-08 | Core 3B dense；Core Advanced 20B sparse 1–4B active；共 5 个模型 |
| [Amazon](https://www.amazon.science/) | [Nova 2 Technical Report](https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf) | 2025-12-02 | Lite/Pro/Omni/Sonic；1M context；Omni 输出 text+image |
| [Microsoft AI](https://microsoft.ai/) | [MAI-Base-2](https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai/) | 2026-10-15 | 2.8T total / 80B active；50T tokens；不开放权重 |
| [Microsoft (Phi)](https://azure.microsoft.com/en-us/products/phi) | Phi-4-reasoning-vision-15B | 2026-03 | Phi-5 仅二手传闻，无官方技术报告 |
| [ByteDance Seed](https://seed.bytedance.com/) | [Seed2.0 Model Card](https://arxiv.org/abs/2607.00248) | 2026-06-30 | Pro/Lite/Mini；参数未披露；长尾知识 + 复杂指令 |
| [StepFun](https://www.stepfun.com/) | Step 5 Preview + [Step 3.7 Flash](https://static.stepfun.com/blog/step-3.7-flash) | 2026-10-15 / 2026-05-29 | 600B/27B；198B/11B；均无正式 arXiv 技术报告 |
| [Shanghai AI Lab / InternLM](https://www.shlab.org.cn/) | [Intern-S2-Preview](https://arxiv.org/abs/2608.13505) | 2026-08-13 | 科学 agentic foundation model；397B 变体；Apache-2.0 |
| [Baichuan AI](https://www.baichuan-ai.com/) | [Baichuan-M4](https://arxiv.org/abs/2606.08982) | 2026-06-08 | 临床级医疗 agent system；参数未披露 |
| [01.AI (Yi)](https://www.01.ai/) | 无可验证的 2026 新技术报告 | — | 最新公开报告仍为 Yi-Lightning（2024-10） |

## 重点报告

### 1. OpenAI — GPT-6.1 Terra

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6.1 Terra：面向视觉推理、精确 computer use 与高吞吐专业工作的小版本 |
| English title | Introducing GPT-6.1 Terra / GPT-6.1 Terra System Card Addendum |
| 发布机构 | OpenAI |
| 模型系列 | GPT-6.1（Terra） |
| 发布日期 | 2026-10-26 |
| 核心参数 | 参数未披露；1,050,000 context；最大输入 922K；最大输出 128K；text+image 输入、text 输出 |
| 价格 | $1 / MTok input；$0.05 cached；$5 / MTok output |
| 链接 | [发布博客](https://openai.com/index/introducing-gpt-6-1-terra/)；[系统卡增补](https://deploymentsafety.openai.com/gpt-6-1-terra)；[API 文档](https://developers.openai.com/api/docs/models/gpt-6.1-terra) |

**主要创新点**

- 定位不是「最强推理」，而是「高吞吐专业工作 + 视觉/屏幕操作」：产品图与目录匹配、技术图纸理解、应用界面操作、文本起草与修订。
- `reasoning.effort` 支持 `none / low / medium / high / xhigh / max`，默认 `medium`；工具调用要求 Responses API。
- 与 GPT-6.1 Sol、GPT-6 Astra 共用同一套 safeguards / Preparedness 评估栈，属于同代系统卡的增补，而不是独立架构报告。

**关键数据（厂商自报）**

- ARC-AGI-2 Verified：**18.1%**（GPT-6.1 Sol 11.4%，GPT-6 Astra 11.4%）。
- Terminal-Bench 4.0：**50.3%**（Sol 48.3%，Astra 45.9%）。
- OSWorld-Verified：**86.7%**（Sol 84.4%，Astra 83.1%）。
- ScreenSpot-Pro：**96.4%**；MMMU-Pro：**76.4%**；Vals Index：**68.9%**。
- 每 1000 字符事实错误：**4.3**（GPT-6.1 Sol 16.7）；Artificial Analysis Intelligence Index：**52**（Sol 50）。
- Preparedness：**Cybersecurity Critical**；**Bio/Chem High**；系统卡称其为 OpenAI 迄今 cyber 风险最高的公开模型。

**限制与判断**

- 这是 Addendum，不是完整的架构/训练报告；参数、数据配比、训练算力均未披露。
- 安全等级为 Critical 意味着部署限制与监控成本会上升；benchmark 均为首方口径，缺少独立复现。
- 对开发者的实际意义：在 1M context 档位提供了明显低于 Sol 的价格，适合「大量截图/文档 + 中等推理」的 agent 工作流。

### 2. Anthropic — Claude Haiku 5.5（及 Opus 5.5 背景）

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Haiku 5.5：面向高吞吐、低延迟任务的最强小模型 |
| English title | Claude Haiku 5.5 System Card |
| 发布机构 | Anthropic |
| 模型系列 | Claude 5.5（Haiku / Sonnet / Opus） |
| 发布日期 | 2026-10-07（Haiku 5.5）；2026-09-22（Opus 5.5） |
| 核心参数 | 1M context；128K max output（Batch API beta 可到 300K）；text+image 输入；参数未披露 |
| 价格 | $0.10 / MTok input；$0.50 / MTok output；长 prompt 超过 100K 后加价 |
| 链接 | [Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)；[System Card PDF](https://assets.claude.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5.pdf)；[模型文档](https://platform.claude.com/docs/en/models/haiku-5-5/overview) |

**主要创新点**

- 比 Haiku 4.5 平均便宜约 **75%**，但 context 从 200K 提升到 1M，输出从 64K 提升到 128K。
- 使用与 Claude 4.7 之后相同的新 tokenizer；同一段文本约多 **30%** token，做成本迁移时必须重算。
- 支持 adaptive thinking 与 `effort` 参数；默认 `medium`。面向分类、路由、抽取、subagent 等高频任务。
- 同步下调 Sonnet 5.5 的 cache read 价格（约减半），使 agentic 工作负载整体成本下降约 20%；并为 Max/Team 订阅新增月度 API credit。

**关键数据（厂商自报）**

- GDPval-AA v2.1：**1620**（Haiku 4.5 为 735；GPT-6 Luna 1437；Sonnet 5.5 1840）。
- Humanity's Last Exam：**45.9%**（无工具）/ **57.4%**（有工具）。
- OSWorld-Verified：**78.7%**；Terminal-Bench 2.1：**70.8%**。
- Anthropic 称其在若干 agentic 任务上「接近甚至超过 Sonnet 5.5」，但整体仍低于 Sonnet/Opus。
- 未跨越新的 RSP 阈值；安全评估没有触发 CB-2 级别部署限制。

**限制与判断**

- 小模型 benchmark 的方差较大，尤其 HLE / OSWorld 对 scaffold 敏感；不应把单表数值当作稳定能力。
- Opus 5.5 的系统卡（09-22）仍按 **CB-1** 处理，AI R&D 能力略高于 Mythos 5.1；本窗口没有新的 Opus 报告。
- 价格优势明显，但长上下文与高分辨率图像会显著增加 token 数，真实成本需按业务重算。

### 3. Google DeepMind — Gemini 4 Argon

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 Argon 模型卡 |
| English title | Gemini 4 Argon Model Card |
| 发布机构 | Google DeepMind |
| 模型系列 | Gemini 4 |
| 发布日期 | 2026-10-13 |
| 核心参数 | 大规模稀疏 MoE Transformer；原生多模态（text / image / audio）；1M 输入 + 1M 输出统一 context；参数未披露 |
| 知识截止 | 2026-03（可靠知识截止）；训练数据截止更晚但未公开 |
| 链接 | [Model Card](https://deepmind.google/models/model-cards/gemini-4-argon/)；[PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf) |

**主要创新点**

- 不是 Gemini 3.x 的微调，而是新的 frontier 预训练模型；统一 1M 输入/输出上下文，长输出不再单独切模型。
- 原生多模态输入（文本、图像、音频），面向 agentic 长任务与视频/音频理解。
- 安全框架同时评估 CBRN、cyber、harmful manipulation；Google 表示不能排除 CCL（Critical Capability Level）。

**关键数据（厂商自报）**

- Vals Index：**68.9%**；DeepSWE：**77.9%**；Terminal-Bench 4.0：**57.4%**。
- GraphWalks：**84.2%**；LVBench：**91.7%**；MMMU-Pro：**81.3%**。
- AA Intelligence Index：**59**（第三方口径，单独标注）。
- 美国区价格：$2 / $10 per MTok 到 2026-11-30，之后 $4 / $20。

**限制与判断**

- 模型卡没有给出总参数、激活参数、训练 token 数；「稀疏 MoE」是唯一架构确认。
- 1M 输出 context 的实际可用长度与质量衰减仍需独立评测；长输出成本高。
- CBRN/cyber 的 CCL 判定会影响高风险场景部署，企业需要额外的 use-case 审查。

### 4. Meta AI — Muse Spark Open 与 Muse Glimmer 30B

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse Spark Open：可本地部署的 816B 开放权重模型；Muse Glimmer 30B：从 Muse Spark 蒸馏的 dense 小模型 |
| English title | Muse Spark Open / Muse Glimmer 30B |
| 发布机构 | Meta Superintelligence Labs |
| 发布日期 | 2026-10-15（Spark Open）；2026-10-23（Glimmer，arXiv 2610.24628） |
| 核心参数 | Spark Open：816B total / 42B active，1M context，原生多模态；Glimmer：~29.6B dense，128K+ context，4-bit，Apache 2.0 |
| 链接 | [Muse Spark Open](https://research.meta.ai/blog/muse-spark-open)；[Muse Glimmer arXiv](https://arxiv.org/abs/2610.24628) |

**Muse Spark Open**

- 816B 总参数 / 42B 激活，1M context，原生多模态，面向 coding、agentic、长程任务。
- 首次可在 **2× Apple M5 Ultra Mac Studio + MLX** 上本地运行；同时上 SageMaker、GCP Model Garden、Hugging Face、Microsoft Foundry。
- 托管侧覆盖 Baseten、Fireworks、Groq、Modal、Nebius、OpenRouter、Together；推理引擎覆盖 SGLang、vLLM、TensorRT-LLM、HF Transformers、MLX、llama.cpp、Unsloth。
- 自评：AA Index **39**；GPQA-D **89.0**；Terminal-Bench 2.1 **76.4**；DeepSWE 1.1 **60**；MCP Atlas **89.2**；OSWorld-Verified **80.4**。

**Muse Glimmer 30B**

- dense causal transformer，约 **29.6B** 总参数：LM 约 25.16B + 两份未 tied embedding 各 1.34B + perception encoder 1.8B。
- hidden 6656、52 层、32 Q / 2 KV heads（GQA 16:1）、head dim 128、SwiGLU 19968、sliding window 2048。
- attention pattern 为 `[Local, Local, Local, Global]`；RoPE theta 500000 只用于 local layers；gated attention；vocab 202,048。
- 128K+ context；text+image 输入、text 输出；4-bit 量化；Apache 2.0；从 Muse Spark 蒸馏，对标 Gemma4-31B / Qwen3.6-27B。
- 自评：SWE-bench Verified **76.0**；SWE-bench Pro **51.2**；MCPAtlas **75.5**；AIME **94.7**；OSWorld **65.9**。

**限制与判断**

- Spark Open 的「开放权重」仍需核对 license 的具体商用条款；本地 2× M5 Ultra 是演示配置，不等于通用消费级硬件可跑。
- Glimmer 是蒸馏模型，benchmark 接近大模型不代表训练方法可复制；4-bit 结果与 BF16 不可直接横比。
- Meta 同时推进「超大开放权重」与「小 dense 蒸馏」两条线，后者更适合端侧与低成本 agent。

### 5. NVIDIA — Nemotron 3.5 Super / Lightning

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Super 与 Lightning：混合 Mamba-Transformer MoE 的高效开放模型 |
| English title | NVIDIA Nemotron 3.5 Super and Lightning Technical Report |
| 发布机构 | NVIDIA |
| 发布日期 | 2026-10-21 |
| 核心参数 | Super：120B total / 12B active，多模态；Lightning：30B total / 3B active，文本 |
| 架构 | hybrid Mamba-Transformer MoE；原生 speculative decoding；MTP boosting |
| 链接 | [Technical Report PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf) |

**主要创新点**

- 用 **12B active** 的 Super 超过 Nemotron 3 Ultra，active 参数约少 **4.6×**，把「每 active 参数智能」推到新档位。
- 预训练 + 蒸馏 + 长上下文训练；后训练包含 SFT、RLVR、RLHF、多教师 on-policy distillation（MOPD）。
- Super 额外做 Indic continued pretraining（最高 **+9.82pp**）与 agentic software-engineering mid-training。
- 原生 speculative decoding：MTP boosting 提升 acceptance rate；test-time scaling 探索 parallel agent execution 与 self-verification。
- 许可 OpenMDW-1.1；提供 BF16 与 NVFP4。

**关键数据（厂商自报）**

- SWE-bench Pro：**51.78%**，高于 Nemotron 3 Ultra，但 active 参数约少 4.6×。
- 长上下文与 agentic coding 是主要卖点；Lightning 面向 3B active 的本地/边缘部署。
- 报告详细给出训练稳定性、蒸馏配方与 speculative decoding 的 acceptance 分析，工程价值高于单点 benchmark。

**限制与判断**

- 「超过 Nemotron 3 Ultra」是家族内比较，不等于超过同期所有 frontier 模型。
- 多教师蒸馏 + RL 的组合对数据与算力要求高，复现门槛不低。
- Super 的多模态能力与 Lightning 的文本定位不同，不能按同一价格/延迟比较。

### 6. Mistral AI — Mistral Large 4（权重仍未落地）

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4：1.05T 总参数 / 52B 激活的开放权重多模态 MoE |
| English title | Introducing Mistral Large 4 |
| 发布机构 | Mistral AI |
| 发布日期 | 2026-10-06（Public Preview） |
| 核心参数 | 1.05T total / **52B active**；1.6B vision encoder；1M context；text+image 输入；reasoning+text 输出 |
| 价格 | $1.36 / MTok input；$0.14 cached；$4.18 / MTok output |
| 链接 | [发布博客](https://mistral.ai/news/mistral-large-4/)；[模型文档](https://docs.mistral.ai/models/mistral-large-4)；[技术文档 PDF](https://legal.mistral.ai/documents/Mistral%20Large%204%20-%20Technical%20Documentation%20For%20Downstream%20Providers.pdf) |

**主要创新点**

- granular MoE；1.05T 总参数但只激活 52B，配 1.6B 视觉编码器，原生多模态。
- 统一 instruct + reasoning 的混合推理；1M context；多语言与视觉 grounding 是重点。
- 官方定位是「open-weight」，但截至 2026-10-27 权重仍未发布：HF 页面显示 **Upcoming release**，倒计时至 **2026-10-31 15:00Z**，仓库无模型文件，`LICENSE` 返回 **HTTP 404**，waitlist 约 969。
- Forkast 在 10-27 的报道标题即「The reported date arrived and the weights did not」；Mistral 没有给出新的确定日期。

**关键数据**

- 官方 docs 明确写 **52B active / 1.05T total / 1M context**；此前 10-27 digest 的 49B 应以此为准。
- 第三方早期测评（AA Intelligence Index 38、Cybench 93、CyberGym-E2E 82、DeepSWE 61.7）样本有限，仅作参考，不进入主表。
- 没有 arXiv 技术报告；只有发布博客与合规技术文档，架构细节（层数、专家数、注意力模式）未公开。

**限制与判断**

- 这是本期最大的「发布状态风险」：预览 API 可用不等于开放权重可用；license 未落地前不能做商用/再分发判断。
- 52B active 在 1T 级模型中偏高，推理成本不会接近 10B 级小模型；1M context 的真实吞吐需实测。
- 若 10-31 仍不发布，应把「open-weight」标签改为「open-weight promised」，并在后续 digest 继续追踪。

### 7. xAI — Grok 4.7

| 字段 | 内容 |
|---|---|
| 中文标题 | Grok 4.7 模型卡 |
| English title | Model Card: Grok 4.7 |
| 发布机构 | SpaceXAI（XAI LLC DBA） |
| 发布日期 | 2026-09-21 |
| 核心参数 | 500K context；text+image 输入、text 输出；参数未披露；knowledge cutoff 2026-05 |
| 价格 | $2 / MTok input；$0.50 cached；$6 / MTok output；Fast 变体 2× 价格 |
| 链接 | [Model Card PDF](https://media.x.ai/v1/website/4p7card-5eccc980.pdf)；[发布页](https://x.ai/news/grok-4-7)；[开发者文档](https://docs.x.ai/developers/models/grok-4.7) |

**主要创新点**

- 在 Grok 4.6 基础上继续扩展 coding、engineering、office work 的自主任务长度；强调「更少步骤、更少输出 token」。
- 用匿名化的 **Cursor workflow 数据**做补充训练，提升 coding / agentic 表现；这是模型卡明确披露的数据来源。
- 默认 `high` reasoning，支持 `low / medium / high / xhigh`；输出无硬上限，500K context 超过 200K 后按长上下文价格计费。
- 渠道：xAI API、Grok Build、Cursor 全档、Word/PowerPoint/Excel add-ins、OpenRouter/Vercel/Cloudflare 等网关。

**关键数据（厂商自报）**

- CursorBench 4.0：**46.3%**（xhigh）/ **43.9%**（high）；4.0 与 3.2 不可直接比较。
- 模型卡强调「score vs cost」：在同等成本下输出 token 更少，长任务成本低于部分 frontier 模型。
- 训练数据：文本 >10T tokens、图像 >10 亿、音频/视频各 >100 万小时；数据采集不晚于 2026-08。

**限制与判断**

- 500K context 是官方文档口径，但模型卡本身未给 context 表；本条目以 docs 为准。
- 用 Cursor 数据训练 coding agent 会带来「工具/工作流过拟合」的风险，跨 harness 泛化需独立评测。
- 参数未披露；「更少 token」是厂商自报的效率指标，缺少统一 tokenizer 校准。

### 8. DeepSeek — DeepSeek-V4.1-Flash

| 字段 | 内容 |
|---|---|
| 中文标题 | DeepSeek-V4.1-Flash：面向百万上下文的高效多模态 MoE |
| English title | DeepSeek-V4.1-Flash Technical Report |
| 发布机构 | DeepSeek-AI |
| 发布日期 | 2026-09-17（arXiv 2609.19969；HF 报告日期 2026-09-10） |
| 核心参数 | 552B backbone 多模态 MoE；decode 激活 16B；prefill 仅 8B；最高 1M context |
| 架构 | Causal Encoder-Decoder（CED）；CSA2 跨层 KV 复用；FP4 KV caching；SWA Bounded Replay |
| 链接 | [arXiv 2609.19969](https://arxiv.org/abs/2609.19969)；[Hugging Face](https://huggingface.co/deepseek-ai) |

**主要创新点**

- **Causal Encoder-Decoder（CED）**：把 prefill 与 decode 的计算解耦，prefill 只激活 8B，decode 激活 16B。
- **CSA2**：跨层 KV 复用 + FP4 KV caching；global KV footprint 降到 **890 bytes/token**，约为 V4-Flash 的 1/4。
- **SWA Bounded Replay**：把 persistent KV 进一步压到约 **1/8**，用于超长上下文。
- 45T 多模态 token 预训练；checkpoints 已发布；原生视觉输入。

**关键数据（厂商自报）**

- GPQA Diamond：**90.9**；Codeforces：**3471**；Terminal-Bench 2.1：**90.6**；DeepSWE：**74.2**。
- 1M context 下的 KV cache 与 prefill FLOPs 是核心卖点；官方称相对 V4-Flash 显著下降。
- 报告给出 CED、CSA2、FP4 KV 的消融与吞吐数据，工程细节完整度较高。

**限制与判断**

- 「prefill 8B / decode 16B」是非对称激活，不能简单用「552B/16B」概括全部推理成本。
- 1M context 的有效召回、长文档一致性仍需独立评测；FP4 KV 的数值稳定性依赖实现。
- 这是技术报告，不是产品系统卡；安全/部署限制不在报告范围内。

### 9. Qwen (Alibaba) — Qwen3.8-Flash-Next

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.8-Flash-Next：GDN + QSA 混合注意力与 n-gram embedding 的高效 MoE |
| English title | On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability |
| 发布机构 | Qwen Team, Alibaba Group |
| 发布日期 | 2026-08-26 |
| 核心参数 | 125B total / 6B active；额外 51B n-gram embedding（off-accelerator）+ 4B MTP；262,144 native / 1M extensible |
| 架构 | 48 层 = 12 ×（3 × GDN → MoE + 1 × QSA → MoE）；hidden 2560；512 experts，10 routed + 1 shared |
| 链接 | [GitHub / Tech Report](https://github.com/QwenLM/Qwen3.8-Flash-Next)；[Hugging Face](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) |

**主要创新点**

- **GDN + QSA hybrid**：Gated DeltaNet 以线性成本压缩历史；QSA 用压缩轻量 indexer 在 micro-block 粒度选重要上下文，每 4 层保留 1 层 full attention。
- **Gated Residual（GR）**：残差流扩成 4 分支，用 elementwise gate 控制读写，提升跨层信息流与训练稳定性。
- **N-gram Embedding**：单层 bigram/trigram 表，参数放在 host memory，异步预取；增加容量但几乎不增加每 token FLOPs。
- **Muon 优化器**：重新拟合 scaling law，提升最优学习率/ batch size，减少 warmup，压力测试下更稳定。

**关键数据（厂商自报）**

- 14 个预训练 benchmark 中 **8 个超过** 397B-A17B 前代，其余最多落后 **2.6 分**。
- 只用了约 **1/3** 的激活参数、**1/3** 的训练 token、约 **1/9** 的训练 FLOPs。
- 报告强调「loss、benchmark、效率、稳定性是一个联合设计问题」；n-gram 词表扩大能持续降 loss，但下游精度会饱和。

**限制与判断**

- 这是 base model 的架构报告，不是 chat/agent 系统卡；后训练与安全评估不在其中。
- 51B n-gram 表不占 accelerator，但会增加 host 内存与预取复杂度；部署门槛不等于 6B 小模型。
- 10-27 digest 以 Qwen3.8-Max 为「最新」，本期应改为 **Qwen3.8-Flash-Next 是 latest architecture report**；两者不是同一模型。

### 10. Moonshot AI — Kimi K3.1 Pro / K3

| 字段 | 内容 |
|---|---|
| 中文标题 | Kimi K3.1 Pro：基于 K3 的大规模后训练；Kimi K3 技术报告 |
| English title | Kimi K3.1 Pro Tech Blog / Kimi K3 Technical Report |
| 发布机构 | Moonshot AI |
| 发布日期 | 2026-10-23（K3.1 Pro）；2026-07-27（K3，arXiv 2607.24653） |
| 核心参数 | K3：2.8T total / 104B active MoE，原生视觉，1M context；K3.1 Pro 为 3T-class 后训练版本 |
| 链接 | [K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro)；[K3 arXiv](https://arxiv.org/abs/2607.24653) |

**主要创新点**

- **Kimi Delta Attention（KDA）** + **Attention Residuals** + **Stable LatentMoE**：896 routed experts 中激活 16 个，兼顾容量与稳定性。
- 原生视觉；1M context；百万 token 级 agentic RL，面向长周期 coding / 3D / 金融研究。
- K3.1 Pro 以 K3 为基座做大规模 post-training，编码、3D 创作、金融研究与长时 agent 能力提升；Highspeed 变体吞吐 2–3×。
- 计划 **2026-11-04** 发布 K3.1 Pro 全量权重。

**关键数据（厂商自报）**

- K3 相对 K2 约 **2.5× scaling 效率**；K3.1 Pro 在多项 agentic/coding 评测中接近 frontier，但落后 Fable 5 / GPT-5.6 Sol。
- 官方强调长周期任务与工具调用，而不是单轮知识问答。
- K3 权重已发布；K3.1 Pro 权重待 11-04。

**限制与判断**

- 3T-class 的具体总参数未在博客中完全披露；「3T-class」是官方措辞，不应写成精确 3T。
- K3.1 Pro 的增益主要来自后训练，base model 能力边界没有变化；benchmark 为厂商自报。
- 11-04 权重发布是计划，存在延期风险；本期不把它当作已落地开放权重。

### 11. Zhipu AI — GLM-5.3

| 字段 | 内容 |
|---|---|
| 中文标题 | GLM-5.3：同一基座上的纯后训练跃迁与 emergent cyber 能力 |
| English title | GLM-5.3: Frontier Coding with Emergent Cyber Capabilities |
| 发布机构 | Zhipu AI（Z.ai） |
| 发布日期 | 2026-08-14 |
| 核心参数 | 753B total / ~40B active MoE；与 GLM-5.2 同 base；300K 评测上下文，服务支持 1M |
| 链接 | [Z.ai Blog](https://z.ai/blog/glm-5.3)；[Hugging Face](https://huggingface.co/zai-org/GLM-5.3)；[GLM-5 技术报告](https://arxiv.org/abs/2602.15763) |

**主要创新点**

- 与 GLM-5.2 **同基座**，所有能力增益来自 post-training；这是「后训练作为独立 scaling 轴」的最清晰案例。
- `reasoning_effort` 三档：`low / high / max`，默认 `max`；面向长时 agent 与复杂编程。
- CyberGym 漏洞发现达到开源 SOTA；exploitation benchmark 较 5.2 翻倍以上，官方称出现「emergent cyber capabilities」。
- GLM-5.3-Flash（2026-08-26，320B/18B）提供原生多模态与更低推理成本，属于另一条产品线。

**关键数据（厂商自报）**

- Z.ai Code Bench：较 GLM-5.2 **+50%**。
- Terminal-Bench 3.0：**28.3**（GLM-5.2 为 4.6）；Terminal-Bench 2.1：**88.2**。
- DeepSWE：**66.9**；NL2Repo：**58.0**；ProgramBench：**19.0**。
- Terminal-Bench 3.0 与 Agents' Last Exam 开源 SOTA；CyberGym 漏洞发现开源 SOTA。
- 对比表中出现 Kimi K3（TB3.0 17.4）、DeepSeek-V4 Pro-0813、Qwen3.8-Max、Opus 4.8、Fable 5、GPT-5.6 Sol（TB3.0 34.6）等。

**限制与判断**

- 没有新的完整技术报告；GLM-5.3 只有 model card / blog，架构细节仍引用 GLM-5 报告。
- 纯后训练提升意味着基座能力上限未变；在需要新知识的任务上不会自动变强。
- cyber 能力的提升会带来滥用风险，部署方需要额外的权限与监控。

### 12. Apple — AFM 3

| 字段 | 内容 |
|---|---|
| 中文标题 | 第三代 Apple Foundation Models（AFM 3） |
| English title | Introducing the Third Generation of Apple Foundation Models |
| 发布机构 | Apple（与 Google 合作） |
| 发布日期 | 2026-06-08 |
| 核心参数 | 5 个模型：AFM 3 Core 3B dense；AFM 3 Core Advanced 20B sparse（按请求激活 1–4B）；3 个 PCC 服务端模型 |
| 链接 | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |

**主要创新点**

- 端侧 + Private Cloud Compute 的统一家族；Core Advanced 使用稀疏架构，按请求激活 1–4B，兼顾质量与能耗。
- 原生多模态；与 Google 合作训练；Foundation Models 框架向开发者开放。
- 隐私优先：端侧推理 + PCC 可验证隐私；服务端模型不保留用户数据。

**限制与判断**

- 截至 2026-10-28 仍**没有 arXiv 技术报告**，只有模型文档与 WWDC 材料；架构细节（层数、专家数、注意力）不完整。
- 20B sparse / 1–4B active 是官方口径，但缺少独立 benchmark；Apple 的评测以内部任务为主。
- 不应把 AFM 3 与开放权重模型直接比较；它的约束是设备内存、功耗与隐私。

### 13. Amazon — Nova 2

| 字段 | 内容 |
|---|---|
| 中文标题 | Amazon Nova 2：多模态推理与生成模型家族 |
| English title | Amazon Nova 2: Multimodal Reasoning and Generation Models |
| 发布机构 | Amazon AGI / AWS |
| 发布日期 | 2025-12-02 |
| 核心参数 | Nova 2 Lite / Pro / Omni / Sonic；最高 1M context；Omni 支持 text+image 输出；Sonic 为 speech-to-speech |
| 链接 | [Technical Report PDF](https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf)；[Amazon Science](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models) |

**主要创新点**

- Lite / Pro 支持可配置的 extended thinking，三档 thinking budget，在精度、速度、成本间权衡。
- Omni 是统一多模态模型：text / image / video / audio 输入，text + image 输出，减少多模型编排。
- Sonic 是第二代 speech-to-speech，面向实时语音 agent；官方称在英法意德西五语的对话质量上超过 GPT-Realtime（2025-08）与 Gemini 2.5 Flash Live（2025-09）。
- 全家族 1M context；集成 Responsible AI guardrails。

**关键数据（厂商自报）**

- Nova 2 Lite：MMLU-Pro **80.9**；GPQA Diamond **79.6**；AIME 2025 **91.0**；IF-Bench **70.8**；MultiChallenge **76.6**；LongCodeBench 1M **84.0**。
- Nova 2 Pro：MMLU-Pro **81.6**；GPQA Diamond **81.4**；AIME 2025 **92.3**；IF-Bench **80.2**；MultiChallenge **77.7**；LongCodeBench 1M **84.0**。
- 官方称 Lite 在多数标准 benchmark 上匹配或超过 Claude Haiku 4.5、GPT-5 Mini、Gemini 2.5 Flash；Pro 对标 Sonnet 4.5 / GPT-5.1 / Gemini 3 Pro Preview。

**限制与判断**

- 这是 2025-12 的报告，不是 2026 新发布；列入覆盖表是为了「最新正式技术报告」的完整性。
- 对比基线多为 2025 年模型，不能与 2026 的 GPT-6.1 / Gemini 4 / Claude 5.5 直接横比。
- 参数未披露；Nova 2 Pro 的 MMLU-Pro 低于部分竞品，但在 IF / MultiChallenge 上更强，说明定位不同。

### 14. Microsoft — MAI-Base-2 与 Phi

| 字段 | 内容 |
|---|---|
| 中文标题 | 微软完成 MAI-Base-2 预训练：2.8T/80B 原生多模态 MoE 基座 |
| English title | Frontier Pre-training at Microsoft AI |
| 发布机构 | Microsoft AI |
| 发布日期 | 2026-10-15 |
| 核心参数 | 2.8T total / 80B active；102 层；hidden 8704；每层 MoE（1 shared + 7 routed / 512 experts）；50T tokens |
| 训练 | 16k GB200 × 38 天（2026-08~09）；平均 MFU 21%；goodput 89%；Muon 优化器；MXFP8 |
| 链接 | [Microsoft AI](https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai/) |

**主要创新点**

- 原生 VLM：视觉从预训练起纳入，没有独立图像编码器；视觉-语言占 18%（约 9T，其中 4.5T unique）。
- 比最强开放基座 DeepSeek-V4-Pro-Base **4–12× 更 FLOPs-efficient**（BPB–FLOPs scaling law 外推，不是 benchmark 对打）；较 MAI-Base-1 提升 6.3–12.7×。
- 不使用蒸馏；强调数据 provenance；权重计划通过 Foundry 授权给受信伙伴，**不开放**。
- MAI-Base-2 仍在 post-training；MAI-Base-3 已开始筹备。

**Phi 线**

- Phi-5 目前只有 2026-05 的二手传闻（MoE 2/8 专家、GQA、4-bit 动态量化、500M draft speculative decoding、128K 滑窗；Phi-5-mini 3.8B / Phi-5 5.6B / Phi-5-vision 7.2B），**没有官方技术报告**。
- Microsoft 官方 Phi 页面最新仍是 Phi-4 mini / multimodal；最新正式报告为 **Phi-4-reasoning-vision-15B**（2026-03）。
- 本 digest 不把 Phi-5 当已证实发布；如需跟踪，应等待官方 model card。

**限制与判断**

- 效率声明是 scaling law 外推，不是直接 benchmark；不能写成「比 DeepSeek-V4-Pro 强 4–12×」。
- 不开放权重，复现只能看报告；对学术界的直接价值有限。
- 50T token / 16k GB200 的训练规模说明 frontier pre-training 仍是少数玩家的游戏。

### 15. ByteDance Seed — Seed2.0

| 字段 | 内容 |
|---|---|
| 中文标题 | Seed2.0：面向真实世界复杂度的模型系列 |
| English title | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity |
| 发布机构 | ByteDance Seed |
| 发布日期 | 2026-06-30（arXiv 2607.00248） |
| 核心参数 | Pro / Lite / Mini 三尺寸；参数未披露；多模态（图像/视频/音频/文本） |
| 链接 | [arXiv](https://arxiv.org/abs/2607.00248)；[Seed 官方](https://seed.bytedance.com/en/public_papers/seed2-0-model-card-towards-intelligence-frontier-for-real-world-complexity) |

**主要创新点**

- 以真实用户需求构建评估体系，重点解决 **long-tail knowledge** 与 **complex instruction following**。
- 强化视觉/多模态理解（截图、图表、扫描文档、混合媒体），降低幻觉、提升结构化抽取。
- 三尺寸覆盖延迟/成本；面向大规模在线部署（豆包/Volcano Engine，模型 id `Doubao-Seed-2.0-pro`）。
- 推理、视觉理解、搜索是官方强调的三项世界领先能力。

**限制与判断**

- 参数、训练 token、架构均未披露；更像 model card + 部署报告，不是完整技术报告。
- 评测以真实业务场景为主，缺少与 frontier 模型的统一 benchmark 横比。
- 6 月发布，不是本窗口新增；列入覆盖表是为了中国模型梯队的完整性。

### 16. 其他中国模型 — StepFun / InternLM / Baichuan / Yi

**StepFun**

- **Step 5 Preview**（2026-10-15）：600B total / 27B active，1M context，FP8/BF16/NVFP4，开放权重，StepFun Model License 1.0，33T tokens；面向长时 agent 与复杂推理。
- **Step 3.7 Flash**（2026-05-29）：198B total / 11B active（196B LM + 1.8B ViT），256K context，sparse MoE top-8/288 experts，MTP；原生多模态理解与行动、web/visual search、tool orchestration；兼容 Claude Code、KiloCode、Hermes Agent、OpenClaw；Android Daily 61.87%（Gemini 3 Flash 63.21%）。
- 两者都没有正式 arXiv 技术报告；Step-3 的 arXiv 2507.19427 是 2025-07 旧报告。

**InternLM / Shanghai AI Lab**

- **Intern-S2-Preview**（arXiv 2608.13505，2026-08-13）：科学 agentic foundation model，支持多模态科学理解、推理、生成与长程任务；397B 变体。
- 训练管线：SFT + 多任务 RL + 黑盒/白盒 agentic RL + on-policy distillation；partial rollout with off-policy correction、adaptive length regularization、online speculative decoding、trace-aware experience assembly。
- 另有 **Intern-S2-Mobius** 技术报告（GitHub `InternLM/Intern-S2-Mobius`，`Technical_Report_Intern_S2_Mobius.pdf`），细节本期未展开。
- Apache-2.0；vLLM day-0 支持（397B 版本）。

**Baichuan**

- **Baichuan-M4**（arXiv 2606.08982，2026-06-08）：Baichuan AI + THUBPM Group（Tsinghua）；临床级医疗 LLM agent system，面向医生监督下的 continuous care；Baichuan-Harness 统一 runtime；SFT/RL；参数未披露。
- 官方称事实性幻觉率 **3.3%**；HealthBench 等医疗评测是重点，不是通用基础模型报告。

**Yi (01.AI)**

- 未检索到可验证的 2026 新技术报告/系统卡；最新公开报告仍为 **Yi-Lightning**（2024-10）。
- 本期不把产品更新当作技术报告；如需纳入，需等待官方 model card 或 arXiv。

## 跨公司趋势

| 方向 | 观察 | 代表工作 |
|---|---|---|
| 架构 | MoE 仍是主流；混合线性注意力（GDN/Mamba/SSM）+ 少量 full attention 成为长上下文标配；n-gram embedding 作为「廉价容量」出现 | Qwen3.8-Flash-Next（GDN+QSA）、Nemotron 3.5（Mamba-Transformer）、DeepSeek V4.1-Flash（CED）、Mistral Large 4（granular MoE） |
| 后训练 | 从「RLHF 收尾」变成独立 scaling 轴；纯 post-training 也能带来大幅 coding/agent 提升 | GLM-5.3（同基座 +50% Code Bench）、Kimi K3.1 Pro、Nemotron 3.5（MOPD + RLVR） |
| 长上下文 | 1M 成为旗舰标配；竞争点转向 KV cache 字节数、prefill/decode 非对称激活、长输出成本 | DeepSeek（890 bytes/token、8B prefill）、Qwen（262K native/1M）、Claude Haiku 5.5（1M/128K）、GPT-6.1 Terra（1.05M） |
| 多模态 | 原生多模态从「能看图」转向「能操作屏幕/软件」；Omni 模型统一输入输出 | GPT-6.1 Terra（computer use）、Gemini 4 Argon、Nova 2 Omni、Muse Spark Open |
| 小模型 | 高吞吐小模型成为 agent 的默认执行层；价格战集中在 $0.1–$1 / MTok | Claude Haiku 5.5、Nova 2 Lite、Muse Glimmer 30B、Nemotron Lightning |
| 开放权重 | 1T 级开放权重出现，但「发布」与「权重可下载」之间的时间差扩大 | Mistral Large 4（延迟）、Muse Spark Open（已发）、Kimi K3.1 Pro（待 11-04）、Qwen3.8-Flash-Next（已发） |
| 安全 | Preparedness / RSP 从「报告附件」变成部署门槛；cyber 风险等级上升 | GPT-6.1 Terra（cyber Critical）、Gemini 4 Argon（CCL 不能排除）、GLM-5.3（emergent cyber） |

## 与 2026-10-27 digest 的修订

| 条目 | 10-27 记录 | 10-28 核实 |
|---|---|---|
| Mistral Large 4 | 1T total / 49B active | **1.05T total / 52B active**；1M context；1.6B vision encoder（官方 docs） |
| Mistral 权重 | 「预计月底发布」 | 截至 10-27 仍未发布；HF 倒计时 **10-31 15:00Z**；无模型文件；LICENSE **404** |
| Qwen | 以 Qwen3.8-Max 为最新 | 最新架构报告是 **Qwen3.8-Flash-Next**（125B/6B + 51B n-gram + 4B MTP；262K native / 1M） |
| DeepSeek | V4.1-Flash-1017 仅有 HF 页面 | 技术报告 **arXiv 2609.19969**：552B、CED、16B decode / 8B prefill、890 bytes/token |
| NVIDIA | Bolt E4B / Bolt 74B | 另有 **Nemotron 3.5 Super 120B/12B + Lightning 30B/3B** 技术报告（10-21） |
| OpenAI | GPT-6.1 Sol | **GPT-6.1 Terra** Addendum（10-26）；1.05M context；cyber Critical |
| Meta | Muse Wonder | **Muse Spark Open**（10-15）+ **Muse Glimmer 30B**（10-23） |
| Kimi | K3.1 Pro（10-23） | 补充 K3 技术报告细节（KDA、Attention Residuals、Stable LatentMoE、2.5× scaling efficiency） |
| Apple | AFM 2026 | **AFM 3**（2026-06-08）；仍无 arXiv 技术报告 |
| Microsoft | Phi-4-reasoning-vision / Nemotron Bolt | 补充 **MAI-Base-2**（2.8T/80B，10-15）；Phi-5 仍无官方报告 |

## 可信度与口径

- **所有 benchmark 均为厂商自报**，除特别标注的第三方（AA Index）外，没有独立复现；跨厂商表格不可直接横比。
- **闭源模型参数未披露**：GPT-6.1 Terra、Claude Haiku 5.5、Gemini 4 Argon、Grok 4.7 均无总参数/激活参数。
- **Mistral Large 4 的「open-weight」尚未兑现**：截至 10-27 权重、license 都不可用；10-31 是 HF 倒计时，不是官方承诺。
- **GPT-6.1 Terra 是系统卡增补**，不是完整技术报告；安全等级 Critical 的判定依据在 deploymentsafety 页面。
- **Apple AFM 3 没有 arXiv 报告**；只有模型文档与 WWDC 材料，架构细节不完整。
- **Phi-5 是未证实传闻**；本 digest 不纳入主表，等待官方 model card。
- **Qwen3.8-Flash-Next 的 1M 是 extensible**，native 为 262,144；不要写成「原生 1M」。
- **NVIDIA / Microsoft 的效率声明**是 scaling law 外推或家族内比较，不是与所有 frontier 模型的直接对打。
- **StepFun / InternLM / Baichuan** 的部分材料是博客或 model card，不是完整技术报告；已逐条标注。

## 结论

- 如果只看「本窗口真正新增的一手材料」，优先级是：**GPT-6.1 Terra 系统卡（10-26）> Muse Glimmer 30B（10-23）> Nemotron 3.5（10-21）> Mistral 权重延期（10-27）**。
- 如果看「架构创新」，最值得读的是 **Qwen3.8-Flash-Next**（GDN+QSA+GR+n-gram）与 **DeepSeek V4.1-Flash**（CED+CSA2+FP4 KV）；两者都把 1M context 的成本拆开优化。
- 如果看「后训练」，**GLM-5.3** 是最干净的对照实验：同基座、纯 post-training、coding/cyber 大幅提升。
- 如果看「开放权重落地」，**Muse Spark Open** 已可用，**Mistral Large 4** 仍需等待 10-31，**Kimi K3.1 Pro** 需等待 11-04。

---

*Generated for karpathy-wiki. 外部链接与厂商自报数据以抓取时点为准；后续 digest 应继续跟踪 Mistral 权重、Kimi K3.1 Pro 权重与 Phi-5 官方报告。*
