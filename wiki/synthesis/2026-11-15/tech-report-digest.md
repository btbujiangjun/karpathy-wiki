---
title: LLM 技术报告速览 — 2026-11-15
type: synthesis
created: 2026-11-15
updated: 2026-11-15
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-attention, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-15
# LLM Tech Report Digest — 2026-11-15

> 覆盖窗口：2026-11-13 → 2026-11-15（增量复核，基线为 [[2026-11-13/tech-report-digest]]）。本期汇总 DeepSeek、OpenAI、Meta AI (LLaMA)、Google DeepMind (Gemini)、Anthropic (Claude)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、NVIDIA、xAI (Grok)、Amazon (Amazon Nova)、Zhipu AI (GLM/ChatGLM)、InternLM (Shanghai AI Lab)、Moonshot AI (Kimi)、StepFun（阶跃星辰）、ByteDance（豆包/Doubao/Seed）等 19 家目标公司/组织的最新可验证大模型技术报告（Tech Report / Technical Report / System Card / Model Card / 官方技术披露）。
>
> 检索说明：本次 `websearch` 工具调用被取消/不可用；已通过 `webfetch`/HTTP 复核 OpenAI Deployment Safety Hub、Anthropic 新闻与 Claude Fable 5.2/Mythos 5.2 公告页、Google DeepMind Gemini 4 模型页、arXiv 页面/API 结果等一手公开材料，并结合仓库既有记录。部分厂商页面存在动态渲染、超时或信息有限，未能独立确认的新发布内容已明确标注。
>
> 口径说明：参数量、训练数据量、上下文长度、benchmark 等多为厂商/论文自报；闭源模型细节以官方系统卡/模型卡/博客/评测方法页为准；“技术报告/论文、系统卡、模型卡、官方博客、模型页”属于不同披露层级，本文按可获得信息分别标注。

## 本期结论（2026-11-15）

- **窗口内新增可确认的一手旗舰披露：** 未检索到 2026-11-13→15 窗口内明确首发的全新旗舰 arXiv 技术报告。近期最重要的新增/持续有效一手材料仍包括：**Google DeepMind Gemini 4 系列**（Argon/Carbon/Hydrogen，官方模型页含 2026-09~11 公告与评测方法链接）、**Anthropic Claude Fable 5.2 & Mythos 5.2**（2026-11-09 公告与系统卡链接）、**OpenAI Deployment Safety Hub** 最新条目（GPT-6 Cyber 2026-11-05、ChatGPT Images 2.6 2026-11-04 等）。
- **近期旗舰技术报告持续有效：** **DeepSeek-V4**（arXiv:2606.19348）与 **NVIDIA Nemotron 3.5 Super/Lightning**（arXiv:2610.38095）仍是可核验的最新开放/半开放技术报告代表。
- **未确认新增：** Meta AI (LLaMA/Muse)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、xAI (Grok)、Amazon (Nova)、Zhipu AI (GLM)、InternLM、Moonshot AI (Kimi)、StepFun、ByteDance (Seed/Doubao) 在本窗口内未检索到可独立确认的全新旗舰 Tech Report/System Card 首发；以下按各家最新可核验披露汇总。

## 重点关注方向速览

| 方向 | 代表进展（已发布/可验证） |
|---|---|
| 新架构（MoE / Mamba / Hybrid） | NVIDIA Nemotron 3.5 的 Hybrid Mamba-Transformer MoE（Super 120B/12B active，Lightning 30B/3B active）；DeepSeek-V4 的 CSA+HCA 混合注意力与 mHC；Gemini 4 系列与 Anthropic Fable/Mythos 强调推理/agentic 能力，底层架构细节披露有限；开放权重旗舰中 MoE+稀疏/混合设计与推理效率仍是主线。 |
| 训练方法（Pre/Post/Alignment/RL） | Nemotron 3.5 披露大规模蒸馏、长上下文训练、SFT+RL（RLVR/RLHF）及 MOPD 等；Anthropic 强调对齐/安全测试、受控访问、防蒸馏与企业前沿保障；OpenAI 系统卡持续披露安全导向后训练、越狱鲁棒性与分级治理；Gemini 4 系列强调 agentic 工作流与安全加固。 |
| Scaling Law / 缩放分析 | 缩放重点从单纯参数规模转向“有效智能/成本/延迟/吞吐/上下文”协同：激活参数、KV cache、speculative decoding、量化恢复、长上下文与 serving 工程成为关键维度（Nemotron 3.5、DeepSeek-V4、Gemini 4 披露）。 |
| 多模态模型 | Gemini 4 系列推进文本/图像/视频/音频与工具/计算机使用的统一前沿能力；Nemotron 3.5 Super 支持文本/图像/视频与交互工具环境；OpenAI ChatGPT Images 2.6 系统卡覆盖图像生成/编辑与溯源安全；Anthropic Fable/Mythos 报告视觉/图表等能力提升。 |
| 长上下文模型 | 1M token 级上下文在 Gemini 4 系列与 DeepSeek-V4 等路线中持续作为前沿能力；Nemotron 3.5 披露长上下文训练与理解；工程侧依赖稀疏/混合注意力、缓存优化与检索/压缩。 |
| 推理模型 / Reasoning | Agentic coding、科学/工程、网络安全、长时任务与工具使用成为高阶推理主战场；Anthropic Fable 5.2/Mythos 5.2、Gemini 4 Argon/Carbon/Hydrogen、Nemotron 3.5、DeepSeek-V4、OpenAI GPT-6 系列均强调复杂工作流与推理能力（多为自报/受控评测）。 |

---

## 各公司/组织最新可验证技术报告

### 1. DeepSeek（深度求索）

| 字段 | 内容 |
|---|---|
| 中文标题 | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| 英文标题 | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| 发布日期 | 2026-04-24（预览）/ 2026-04-26（arXiv 提交，v1） |
| 核心参数 | Pro：1.6T 总参数 / 49B 激活参数；Flash：284B 总参数 / 13B 激活参数；预训练 >32T tokens；上下文 1M tokens（论文/官方口径） |
| 主要创新点 | **混合注意力架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)；**连接/优化**：mHC（Manifold-Constrained Hyper-Connections）、Muon 优化器；**效率**：面向 1M 上下文降低推理 FLOPs 与 KV cache 开销；**后训练**：综合 post-training 提升推理与长上下文能力（厂商/论文自报）。 |
| arXiv/论文链接 | https://arxiv.org/abs/2606.19348 |

**2026-11-15 状态：** 未检索到本窗口新增一手技术报告；V4 仍为最新可核验核心技术报告。

### 2. OpenAI

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Cyber 系统卡 |
| 英文标题 | GPT-6 Cyber System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Cyber（基于 GPT-6 Astra 的专用后训练变体） |
| 发布日期 | 2026-11-05 |
| 核心参数 | 参数量/训练数据量/上下文长度未公开；面向授权网络安全工作场景的专用模型 |
| 主要创新点 | **安全导向推理与受控能力**：针对漏洞发现、利用与渗透测试等高风险能力进行专门评测与披露；强调 Preparedness 分级、访问控制、滥用缓解与部署安全治理。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-cyber |

| 字段 | 内容 |
|---|---|
| 中文标题 | ChatGPT Images 2.6 系统卡 |
| 英文标题 | ChatGPT Images 2.6 System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | ChatGPT Images 2.6 |
| 发布日期 | 2026-11-04（Deployment Safety Hub 列示） |
| 核心参数 | 图像生成/编辑模型；参数量、训练数据量、上下文长度等细节未公开 |
| 主要创新点 | **多模态生成与安全**：图像生成/编辑能力、安全评测、护栏与图像溯源（provenance）相关披露（以系统卡为准）。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/chatgpt-images-2-6 |

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Sol 与 GPT-6 Luna：2026 年 10 月更新（含 Luna 增补） |
| 英文标题 | GPT-6 Sol and GPT-6 Luna: October 2026 update / Addendum to GPT-6 Luna System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Sol / GPT-6 Luna |
| 发布日期 | 2026-10-07（更新）；2026-10-29（Luna 增补） |
| 核心参数 | 参数量/训练数据量/上下文长度未公开 |
| 主要创新点 | **对齐与鲁棒性**：多轮越狱抵抗、减少规避与不诚实行为；Luna 增补涉及简洁性、指令层级与注入鲁棒性改进（以官方披露为准）。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-october ； https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum |

**2026-11-15 状态：** Deployment Safety Hub 复核未见本窗口新增首发条目；上述系统卡/增补仍为近期可核验材料。

### 3. Meta AI (LLaMA / Muse)

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse 系列前沿模型（最新可检索公开披露） |
| 英文标题 | Muse family frontier models (latest publicly verifiable disclosure) |
| 发布机构 | Meta AI / Meta Superintelligence Labs |
| 模型名称/系列 | Muse（含 Spark/Image/Video 等产品/模型线，公开材料分散） |
| 发布日期 | 近期更新见 Meta AI 博客（本窗口未独立确认新增技术报告/系统卡首发） |
| 核心参数 | 完整参数量、训练数据量、统一上下文长度等未见系统性技术报告披露 |
| 主要创新点 | **Agentic 与多模态产品化**：面向个人/专业 agent、图像与视频生成等方向持续迭代；公开信息多为博客/产品说明，技术报告级细节有限。 |
| arXiv/论文链接 | https://ai.meta.com/blog/ （未检索到本窗口新增独立技术报告链接） |

**2026-11-15 状态：** 未确认 LLaMA 或 Muse 系列在本窗口新增技术报告/系统卡；本期抓取 Meta 博客遇到超时，状态依据公开可达信息与历史记录标注为待持续复核。

### 4. Google DeepMind (Gemini)

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 系列（Argon / Carbon / Hydrogen）模型与评测/安全披露 |
| 英文标题 | Gemini 4 series (Argon / Carbon / Hydrogen) model, evaluation, and safety disclosures |
| 发布机构 | Google DeepMind / Google |
| 模型名称/系列 | Gemini 4 Argon / Gemini 4 Carbon / Gemini 4 Hydrogen |
| 发布日期 | Argon：2026-09（公告）/2026-10 更新；Carbon：2026-10 公告、2026-11 可用性更新；Hydrogen：2026-11 公告（以官方模型页/博客为准） |
| 核心参数 | 参数量/训练数据量未完全公开；官方强调长上下文、agentic coding、计算机/工具使用、多模态理解、科学/数学与网络安全等前沿能力（细节见模型页与评测方法） |
| 主要创新点 | **前沿推理与 Agentic**：复杂工作流、长时任务、终端/代码/科学任务与多模态协同；**安全**：Frontier Safety Framework 下的误用防护、提示注入鲁棒性与系统加固；**分层产品能力**：Argon/Carbon/Hydrogen 覆盖不同性能-成本-速度定位（官方自报 benchmark）。 |
| arXiv/论文链接 | https://deepmind.google/models/gemini/ ；评测方法：https://deepmind.google/models/evals-methodology/gemini-4-hydrogen ， https://deepmind.google/models/evals-methodology/gemini-4-carbon （技术细节以官方发布为准，未见对应独立 arXiv 技术报告） |

**2026-11-15 状态：** Gemini 4 系列仍为 Google 最新旗舰模型披露主线；本窗口未确认新增独立 arXiv 技术报告。

### 5. Anthropic (Claude)

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Fable 5.2 与 Claude Mythos 5.2 |
| 英文标题 | Claude Fable 5.2 and Claude Mythos 5.2 |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Fable 5.2 / Claude Mythos 5.2（同底层模型，不同安全/访问配置） |
| 发布日期 | 2026-11-09（公告） |
| 核心参数 | 参数量/训练数据量未公开；API 定价 $8/M input、$40/M output（fast mode $16/$80，公告口径）；上下文长度等部署参数以产品/API 文档为准 |
| 主要创新点 | **能力**：agentic coding、科学与工程、网络安全、硬件/机器人、数学形式化等高难技术任务提升（多项内部/公开 benchmark 自报）；**效率**：较 5.1 更快、成本更低，可选 fast mode；**安全与对齐**：扩展安全测试、对齐评估、网络安全/生物 safeguards、反蒸馏保护、Enterprise Frontier Safeguards 等；Fable 面向通用可用，Mythos 面向经验证的高风险双用途研究场景。 |
| arXiv/论文链接 | 公告：https://www.anthropic.com/claude-fable-and-mythos-5-2 ；系统卡：https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card （PDF，获取受限时以公告摘要为准） |

**2026-11-15 状态：** 2026-11-09 发布仍是 Anthropic 最新可核验旗舰系统卡/公告；本窗口未见更新版本。

### 6. Mistral AI

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4 / 近期开放权重与产品模型（最新可检索公开披露） |
| 英文标题 | Mistral Large 4 and recent open-weight/product model disclosures (latest publicly verifiable) |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Mistral Large 系列及相关模型（公开材料分散） |
| 发布日期 | 近期开放权重/产品更新见官方新闻与模型发布页（本窗口未独立确认新增技术报告首发） |
| 核心参数 | 不同版本参数/上下文/训练细节披露不一；完整统一技术报告未在本窗口新确认 |
| 主要创新点 | 公开材料侧重高效推理、开放权重、长上下文与企业/开发者可用性；具体架构与训练细节以对应发布说明/模型卡为准。 |
| arXiv/论文链接 | https://mistral.ai/news/ （本期抓取失败/受限，未确认新增独立技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡；建议后续复核官方新闻与 Hugging Face/文档。

### 7. Qwen (Alibaba / 阿里巴巴通义千问)

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.x / Qwen 系列近期模型发布（最新可检索公开披露） |
| 英文标题 | Qwen3.x / recent Qwen series model releases (latest publicly verifiable) |
| 发布机构 | Alibaba Cloud / Qwen Team |
| 模型名称/系列 | Qwen 系列（含通用、推理、多模态、代码等分支，具体以最新官方发布为准） |
| 发布日期 | 近期发布见 Qwen 官方博客/研究页与代码仓库（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 各模型参数量、上下文长度、训练数据与后训练配方在对应模型卡/论文中披露，未见本窗口新增统一旗舰技术报告 |
| 主要创新点 | 公开路线持续覆盖长上下文、推理、多模态、工具使用与开放权重生态；细节以具体模型发布材料为准。 |
| arXiv/论文链接 | https://qwen.ai/research ；历史博客镜像 https://qwenlm.github.io/ （本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡；需后续复核 qwen.ai 与 arXiv。

### 8. Yi (01.AI / 零一万物)

| 字段 | 内容 |
|---|---|
| 中文标题 | Yi 系列模型（最新可检索公开披露） |
| 英文标题 | Yi series models (latest publicly verifiable disclosure) |
| 发布机构 | 01.AI（零一万物） |
| 模型名称/系列 | Yi 系列 |
| 发布日期 | 未检索到本窗口新增技术报告/系统卡首发 |
| 核心参数 | 以历史已发布模型卡/论文为准；本窗口无新增可核验参数披露 |
| 主要创新点 | 公开信息有限；本期未确认相对既有记录的新旗舰架构/训练/对齐技术报告。 |
| arXiv/论文链接 | 未检索到本窗口新增链接（建议后续复核官方渠道与 arXiv） |

**2026-11-15 状态：** 未确认新增旗舰技术报告/系统卡。

### 9. Baichuan（百川智能）

| 字段 | 内容 |
|---|---|
| 中文标题 | Baichuan 系列模型（最新可检索公开披露） |
| 英文标题 | Baichuan series models (latest publicly verifiable disclosure) |
| 发布机构 | Baichuan AI（百川智能） |
| 模型名称/系列 | Baichuan 系列 |
| 发布日期 | 未检索到本窗口新增技术报告/系统卡首发 |
| 核心参数 | 以历史已发布材料为准；本窗口无新增可核验参数披露 |
| 主要创新点 | 公开信息有限；本期未确认相对既有记录的新旗舰技术报告。 |
| arXiv/论文链接 | 未检索到本窗口新增链接（建议后续复核官方渠道与 arXiv） |

**2026-11-15 状态：** 未确认新增旗舰技术报告/系统卡。

### 10. Microsoft (Phi)

| 字段 | 内容 |
|---|---|
| 中文标题 | Phi 系列近期小型/推理模型（最新可检索公开披露） |
| 英文标题 | Recent Phi series small/reasoning models (latest publicly verifiable disclosure) |
| 发布机构 | Microsoft |
| 模型名称/系列 | Phi 系列（含推理/多模态等分支，具体以最新发布为准） |
| 发布日期 | 近期发布见 Microsoft Research/产品博客与模型卡（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 各版本参数量、训练数据与上下文长度以对应技术报告/模型卡为准；本窗口无新增统一披露 |
| 主要创新点 | 小模型高效推理、数据策展、后训练与多模态能力为常见主线；细节以具体发布材料为准。 |
| arXiv/论文链接 | https://www.microsoft.com/en-us/research/ 及相关 arXiv/Hugging Face 页面（本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 11. Apple

| 字段 | 内容 |
|---|---|
| 中文标题 | Apple Foundation Models / 设备端与服务器模型（最新可检索公开披露） |
| 英文标题 | Apple Foundation Models / on-device and server models (latest publicly verifiable disclosure) |
| 发布机构 | Apple |
| 模型名称/系列 | Apple Foundation Models (AFM) 等 |
| 发布日期 | 近期技术细节见 Apple Machine Learning Research 与相关论文/博客（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 以已发布技术报告/论文为准；本窗口无新增可核验统一披露 |
| 主要创新点 | 设备端效率、隐私保护、适配器/压缩与多模态能力为公开关注点；细节以对应论文为准。 |
| arXiv/论文链接 | https://machinelearning.apple.com/research （本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 12. NVIDIA

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Super 与 Lightning：面向 Agentic AI 的开放高效混合 Mamba-Transformer MoE 模型 |
| 英文标题 | Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Super / Nemotron 3.5 Lightning |
| 发布日期 | 2026-10-28（arXiv v1） |
| 核心参数 | Super：120B 总参数 / 12B 激活参数，多模态；Lightning：30B 总参数 / 3B 激活参数，文本模型；两者面向高效部署（上下文长度等细节见论文） |
| 主要创新点 | **架构**：Hybrid Mamba-Transformer MoE；**训练**：大规模蒸馏、长上下文训练、native speculative decoding，Super 另含 Indic continued pretraining 与 agentic 软件工程 mid-training；**后训练**：SFT + RL（RLVR/RLHF）、专用 teacher 训练与 multi-teacher on-policy distillation (MOPD)；**能力**：文本/图像/视频/工具交互与 agentic reasoning；**效率**：MTP boosting 提升 speculative decoding 接受长度，NVFP4 量化高保真，推理吞吐优化（论文自报）。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.38095 |

**2026-11-15 状态：** 未检索到本窗口新增 Nemotron 技术报告；3.5 Super/Lightning 论文仍为最新可核验核心材料。

### 13. xAI (Grok)

| 字段 | 内容 |
|---|---|
| 中文标题 | Grok 系列近期模型（最新可检索公开披露） |
| 英文标题 | Recent Grok series models (latest publicly verifiable disclosure) |
| 发布机构 | xAI |
| 模型名称/系列 | Grok 系列 |
| 发布日期 | 近期更新见 xAI 新闻/产品发布（本窗口未独立确认新增技术报告/系统卡首发） |
| 核心参数 | 参数量、训练数据量、上下文长度等细节公开披露有限；以官方公告为准 |
| 主要创新点 | 公开重点通常包括推理、实时信息、工具使用与多模态能力；本期未确认新增可核验技术报告级细节。 |
| arXiv/论文链接 | https://x.ai/news （本期抓取超时/受限，未确认新增独立技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 14. Amazon (Amazon Nova)

| 字段 | 内容 |
|---|---|
| 中文标题 | Amazon Nova 系列模型（最新可检索公开披露） |
| 英文标题 | Amazon Nova series models (latest publicly verifiable disclosure) |
| 发布机构 | Amazon |
| 模型名称/系列 | Amazon Nova 系列 |
| 发布日期 | 近期发布见 Amazon/AWS 官方渠道（本窗口未独立确认新增技术报告首发） |
| 核心参数 | 以官方模型卡/文档为准；本窗口无新增可核验统一技术报告披露 |
| 主要创新点 | 多模态理解/生成、企业部署、成本与延迟优化等方向；细节以官方发布为准。 |
| arXiv/论文链接 | https://www.amazon.science/ 及 AWS/Amazon 官方页面（本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 15. Zhipu AI（智谱 AI, GLM/ChatGLM）

| 字段 | 内容 |
|---|---|
| 中文标题 | GLM / ChatGLM 系列近期模型（最新可检索公开披露） |
| 英文标题 | Recent GLM / ChatGLM series models (latest publicly verifiable disclosure) |
| 发布机构 | Zhipu AI（智谱 AI） |
| 模型名称/系列 | GLM / ChatGLM 系列 |
| 发布日期 | 近期更新见官方发布与模型仓库（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 以对应模型卡/论文为准；本窗口无新增可核验统一披露 |
| 主要创新点 | 长上下文、推理、Agent 与多模态能力持续迭代；细节以具体发布材料为准。 |
| arXiv/论文链接 | 官方渠道与 arXiv/Hugging Face（本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 16. InternLM（上海人工智能实验室 / Shanghai AI Lab）

| 字段 | 内容 |
|---|---|
| 中文标题 | InternLM / Intern 系列近期模型（最新可检索公开披露） |
| 英文标题 | Recent InternLM / Intern series models (latest publicly verifiable disclosure) |
| 发布机构 | Shanghai AI Laboratory（上海人工智能实验室） |
| 模型名称/系列 | InternLM / Intern 系列 |
| 发布日期 | 近期更新见官方发布与论文/模型卡（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 以对应技术报告/模型卡为准；本窗口无新增可核验统一披露 |
| 主要创新点 | 开放研究模型、长上下文、推理与多模态方向持续演进；细节以具体发布为准。 |
| arXiv/论文链接 | 官方渠道与 arXiv/Hugging Face（本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 17. Moonshot AI（Kimi / 月之暗面）

| 字段 | 内容 |
|---|---|
| 中文标题 | Kimi 系列近期模型（最新可检索公开披露） |
| 英文标题 | Recent Kimi series models (latest publicly verifiable disclosure) |
| 发布机构 | Moonshot AI（月之暗面） |
| 模型名称/系列 | Kimi 系列 |
| 发布日期 | 近期更新见官方发布与模型仓库（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 以对应技术报告/模型卡为准；本窗口无新增可核验统一披露 |
| 主要创新点 | 长上下文、推理、Agent 与开放/商用模型迭代为公开主线；细节以具体发布为准。 |
| arXiv/论文链接 | 官方渠道与 arXiv/Hugging Face（本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 18. StepFun（阶跃星辰）

| 字段 | 内容 |
|---|---|
| 中文标题 | Step 系列近期模型（最新可检索公开披露） |
| 英文标题 | Recent Step series models (latest publicly verifiable disclosure) |
| 发布机构 | StepFun（阶跃星辰） |
| 模型名称/系列 | Step 系列 |
| 发布日期 | 近期更新见官方发布与评测平台收录（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 以对应发布说明/模型卡为准；本窗口无新增可核验统一披露 |
| 主要创新点 | 多模态、推理与高性价比推理服务为公开关注点；细节以具体发布为准。 |
| arXiv/论文链接 | 官方渠道与相关页面（本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

### 19. ByteDance（豆包 / Doubao / Seed）

| 字段 | 内容 |
|---|---|
| 中文标题 | Doubao / Seed 系列近期模型（最新可检索公开披露） |
| 英文标题 | Recent Doubao / Seed series models (latest publicly verifiable disclosure) |
| 发布机构 | ByteDance（字节跳动） |
| 模型名称/系列 | Doubao / Seed 系列 |
| 发布日期 | 近期更新见官方发布、云服务与研究页面（本窗口未独立确认新增旗舰技术报告首发） |
| 核心参数 | 以对应模型卡/论文/发布说明为准；本窗口无新增可核验统一披露 |
| 主要创新点 | 多模态、推理、Agent 与大规模产品化部署为公开主线；细节以具体发布为准。 |
| arXiv/论文链接 | 官方渠道与 arXiv/Hugging Face（本期未确认窗口内新增旗舰技术报告） |

**2026-11-15 状态：** 未确认本窗口新增旗舰技术报告/系统卡。

---

## 备注与风险

- **检索局限：** `websearch` 不可用；部分站点动态渲染或抓取超时，可能遗漏未被直接抓取到的最新发布。建议后续补充复核各厂商官网、Hugging Face、arXiv 与模型 API 文档。
- **可比性限制：** 不同机构的参数口径（总参数/激活参数）、上下文定义、训练数据统计、评测设置与工具链差异较大，benchmark 多为自报，不可直接横比。
- **披露层级差异：** 系统卡/模型卡/博客/模型页不等同于完整技术报告；本文已在各条目中尽量区分。
- **合规提示：** 涉及网络安全、生物等双用途能力的模型访问与使用应遵循官方政策与适用法律法规。

*Preference file active: `EXTEND.md` (repo root, bm25 mode `auto_prompt`).*