---
title: LLM 技术报告速览 — 2026-11-13
type: synthesis
created: 2026-11-13
updated: 2026-11-13
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-attention, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-13
# LLM Tech Report Digest — 2026-11-13

> 覆盖窗口：2026-11-12 → 2026-11-13（增量复核，基线为 [[2026-11-12/tech-report-digest]]）。本期汇总 DeepSeek、OpenAI、Meta AI (LLaMA)、Google DeepMind (Gemini)、Anthropic (Claude)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、NVIDIA、xAI (Grok)、Amazon (Amazon Nova)、Zhipu AI (GLM/ChatGLM)、InternLM (Shanghai AI Lab)、Moonshot AI (Kimi)、StepFun（阶跃星辰）、ByteDance（豆包/Doubao/Seed）等 19 家目标公司/组织的最新可验证大模型技术报告（Tech Report / Technical Report / System Card / Model Card / 官方技术披露）。
>
> 检索说明：本次 `websearch` 多次不可用/取消；已使用 `webfetch` 复核 OpenAI Deployment Safety Hub、Anthropic 公告与系统卡页面、Google DeepMind Gemini 模型页、Meta AI 博客、xAI News、Mistral News 及 arXiv 搜索结果，并结合仓库既有记录。部分厂商页面为动态渲染或细节有限，未能独立确认的新内容已明确标注。
>
> 口径说明：参数量、训练数据量、上下文长度、benchmark 等多为厂商/论文自报；闭源模型细节以官方系统卡/模型卡/博客为准；“预览/权重开放/系统卡更新/技术博客/公告/模型页”与完整技术报告为不同披露层级。

## 本期结论（2026-11-13）

- **窗口内新增可确认的一手系统卡/报告：** 未检索到 2026-11-12→13 窗口内明确首发的全新旗舰技术报告/系统卡。相对 11-12 digest，最重要的近期新增材料仍为 Anthropic 于 2026-11-09 发布的 **Claude Fable 5.2 / Claude Mythos 5.2 System Card**（本期复核其公告与系统卡链接可访问，能力/安全披露细节丰富）。
- **近期旗舰材料持续有效：** DeepSeek-V4（arXiv:2606.19348）、NVIDIA Nemotron 3.5 Super/Lightning（arXiv:2610.38095）、OpenAI Deployment Safety Hub 近期条目（GPT-6 Cyber 2026-11-05、ChatGPT Images 2.6 2026-11-04 等）、Google Gemini 4 系列官方披露仍是各自最新可核验核心材料之一。
- **未确认新增：** Meta AI (LLaMA/Muse)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、xAI (Grok)、Amazon (Nova)、Zhipu AI (GLM)、InternLM、Moonshot AI (Kimi)、StepFun、ByteDance (Seed/Doubao) 在本窗口内未检索到可独立确认的全新旗舰 Tech Report/System Card 首发；多数以近期报告、博客、模型页或开放权重发布说明为最新依据。

## 重点关注方向速览

| 方向 | 代表进展（已发布/可验证） |
|---|---|
| 新架构（MoE / Mamba / Hybrid） | DeepSeek-V4 的 CSA+HCA 混合注意力与 mHC；NVIDIA Nemotron 3.5 的 Hybrid Mamba-Transformer MoE；Mistral Large 4 开放权重旗舰路线（公开材料强调 MoE/长上下文/推理，完整技术报告细节有限）；稀疏/混合设计与推理效率持续主导。 |
| 训练方法（Pre/Post/Alignment/RL） | Anthropic Fable 5.2/Mythos 5.2 强调高难技术任务能力与对齐/安全测试、防蒸馏与受控访问；OpenAI 系统卡持续披露安全导向后训练、越狱鲁棒性与分级治理；Nemotron 3.5 披露蒸馏、长上下文训练、SFT+RL（RLVR/RLHF）与 MOPD 等后训练组合。 |
| Scaling Law / 缩放分析 | 从参数规模扩展转向“有效智能/成本/延迟/吞吐”协同：激活参数、KV cache、speculative decoding、量化恢复与 serving 工程成为关键缩放维度（DeepSeek-V4、Nemotron 3.5 等披露）。 |
| 多模态模型 | Gemini 4 系列持续推进文本/图像/视频/音频与工具使用的统一前沿能力；Nemotron 3.5 Super 支持多模态与 agentic 场景；OpenAI ChatGPT Images 2.6 系统卡体现图像生成/编辑与安全溯源披露。 |
| 长上下文模型 | 1M token 级上下文在前沿模型与开放模型路线中持续出现（如 DeepSeek-V4、Gemini 系列口径）；依赖稀疏注意力、压缩/检索、KV 优化与系统工程。 |
| 推理模型 / Reasoning | agentic coding、科学/工程、网络安全与长时任务成为高阶推理主战场；Claude Fable/Mythos 5.2、DeepSeek-V4、Nemotron 3.5、Gemini 4 等均强调推理努力、工具使用与复杂工作流表现（多为自报）。 |

---

## 各公司/组织最新可验证技术报告

### 1. DeepSeek（深度求索）

| 字段 | 内容 |
|---|---|
| 中文标题 | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| 英文标题 | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| 发布日期 | 2026-04-24（预览）/ 2026-04-26（arXiv 提交） |
| 核心参数 | Pro：1.6T 总参数 / 49B 激活；Flash：284B 总参数 / 13B 激活；预训练 >32T tokens；上下文 1M tokens（论文/官方口径） |
| 主要创新点 | **架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 混合注意力、mHC（Manifold-Constrained Hyper-Connections）；**优化**：Muon 优化器；**后训练**：综合 post-training；**效率**：面向 1M 上下文降低推理 FLOPs 与 KV cache 开销（厂商自报）。 |
| arXiv/论文链接 | https://arxiv.org/abs/2606.19348 |

**2026-11-13 状态：** 未确认本窗口新增一手技术报告；V4 仍为最新可核验核心技术报告。

### 2. OpenAI

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Cyber 系统卡 |
| 英文标题 | GPT-6 Cyber System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Cyber（基于 GPT-6 Astra 的专用后训练变体） |
| 发布日期 | 2026-11-05 |
| 核心参数 | 参数量/训练数据未公开；面向授权网络安全工作场景 |
| 主要创新点 | **安全导向推理**：漏洞发现、利用与渗透测试等高风险能力的受控披露；Preparedness 分级、访问控制与滥用缓解并列。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-cyber |

| 字段 | 内容 |
|---|---|
| 中文标题 | ChatGPT Images 2.6 系统卡 |
| 英文标题 | ChatGPT Images 2.6 System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | ChatGPT Images 2.6 |
| 发布日期 | 2026-11-04（Deployment Safety Hub 列示） |
| 核心参数 | 图像生成/编辑模型；具体规模与训练细节未公开 |
| 主要创新点 | **多模态与安全**：图像能力、安全评测、护栏与图像溯源（provenance）相关披露（以系统卡为准）。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/chatgpt-images-2-6 |

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Sol 与 GPT-6 Luna：2026 年 10 月更新 |
| 英文标题 | GPT-6 Sol and GPT-6 Luna: October 2026 update |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Sol / GPT-6 Luna |
| 发布日期 | 2026-10-07（更新）；Luna 增补 2026-10-29 |
| 核心参数 | 参数量/训练数据未公开 |
| 主要创新点 | **对齐与鲁棒性**：多轮越狱抵抗、减少规避与不诚实行为；Luna 增补涉及简洁性与指令层级/注入鲁棒性改进。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-october ；https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum |

**2026-11-13 状态：** Deployment Safety Hub 复核未见本窗口新增首发条目；以上为最新可见系统卡/增补。

### 3. Meta AI (LLaMA / Muse)

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse 系列前沿模型（最新可检索公开披露） |
| 英文标题 | Muse family frontier models (latest publicly verifiable disclosure) |
| 发布机构 | Meta AI / Meta Superintelligence Labs |
| 模型名称/系列 | Muse Spark / Muse Image / Muse Video 等 |
| 发布日期 | Muse Spark 1.1 等更新见 2026-07 官方博客；本窗口未确认新技术报告 |
| 核心参数 | 公开材料有限；未见完整技术报告级参数/训练数据/上下文统一披露 |
| 主要创新点 | **Agentic 与多模态产品化**：面向个人/专业 agent、图像与视频生成等方向持续迭代；技术细节多以博客与产品页呈现，系统卡/论文披露不足。 |
| arXiv/论文链接 | https://ai.meta.com/blog/ （未检索到本窗口新增独立技术报告链接） |

**2026-11-13 状态：** 未确认 LLaMA 或 Muse 系列在本窗口新增技术报告/系统卡。

### 4. Google DeepMind (Gemini)

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 系列（Argon / Carbon / Hydrogen）模型页与安全/评测披露 |
| 英文标题 | Gemini 4 series (Argon / Carbon / Hydrogen) model page and safety/evaluation disclosures |
| 发布机构 | Google DeepMind / Google |
| 模型名称/系列 | Gemini 4 Argon / Gemini 4 Carbon / Gemini 4 Hydrogen |
| 发布日期 | 系列公告与页面持续更新（Argon 2026-09 起，Carbon/Hydrogen 2026-10~11 公告见官方页面）；本窗口未确认新增独立技术报告 PDF/arXiv |
| 核心参数 | 参数量/训练数据未完全公开；官方强调长上下文、agentic coding、工具/计算机使用、多模态理解与科学/安全能力（详见模型页与评测方法） |
| 主要创新点 | **前沿推理与 agentic**：复杂工作流、长时任务与多模态协同；**安全**：Frontier Safety Framework 下的误用防护、注入鲁棒性与系统加固；**效率/能力分层**：Hydrogen/Carbon/Argon 覆盖不同性能-成本定位（官方披露）。 |
| arXiv/论文链接 | https://deepmind.google/models/gemini/ ；评测方法示例 https://deepmind.google/models/evals-methodology/gemini-4-carbon （模型卡/报告以官方发布为准） |

**2026-11-13 状态：** 未确认本窗口新增独立技术报告；Gemini 4 系列仍为最新旗舰披露主线。

### 5. Anthropic (Claude)

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Fable 5.2 与 Claude Mythos 5.2 系统卡 |
| 英文标题 | Claude Fable 5.2 and Mythos 5.2 System Card |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Fable 5.2 / Claude Mythos 5.2（同底座，不同安全配置/访问策略） |
| 发布日期 | 2026-11-09（公告与系统卡） |
| 核心参数 | 参数量/训练数据未公开；公告定价 $8/M 输入、$40/M 输出（fast mode 更高）；默认/高 effort 等设置见产品文档 |
| 主要创新点 | **高难技术能力**：agentic coding、网络安全、科学/工程、数学形式化、硬件与机器人等任务提升（厂商评测）；**效率**：较前代更快、部分场景更省 token/成本；**安全与对齐**：扩展对齐与沙箱逃逸倾向评测、cyber/biology 护栏、防蒸馏强化与 Mythos 受控访问；强调低层级但持续监控的高风险能力治理。 |
| arXiv/论文链接 | https://www.anthropic.com/claude-fable-and-mythos-5-2 ；https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card |

**2026-11-13 状态：** 本期复核确认该系统卡仍为 Anthropic 最新一手旗舰安全/能力披露材料（窗口内无新增首发）。

### 6. Mistral AI

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4 / Le Chonk（开放权重旗舰，最新可检索公开发布） |
| 英文标题 | Mistral Large 4 ("Le Chonk") |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Mistral Large 4 |
| 发布日期 | 2026-10-06（Large 4 发布）/ 2026-10-29（开放权重发布，新闻页）；本窗口未确认新技术报告 |
| 核心参数 | 公开材料定位为大规模前沿开放模型（coding/cyber/agentic 方向）；完整参数、训练数据与系统性技术报告细节在本期未获取到独立 arXiv 全文 |
| 主要创新点 | **开放权重前沿模型**：面向 agentic coding、推理与安全相关能力；Studio/Voxtral/Timestral 等生态协同，但旗舰级技术报告披露程度有限。 |
| arXiv/论文链接 | https://mistral.ai/news/ ；https://mistral.ai/news/mistral-large-4-oss/ （发布页，非 arXiv 技术报告） |

**2026-11-13 状态：** 未确认本窗口新增技术报告/系统卡。

### 7. Qwen (Alibaba / 阿里巴巴通义千问)

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.8 系列（最新可检索公开更新） |
| 英文标题 | Qwen3.8 series (latest publicly verifiable updates) |
| 发布机构 | Alibaba Cloud / Qwen Team |
| 模型名称/系列 | Qwen3.8 系列（含 Omni/Flash/Next 等分支，依官方发布） |
| 发布日期 | 2026-09 前后公开更新为近期主线（以官方博客/API 为准）；本窗口未确认新技术报告 |
| 核心参数 | 依型号而异；公开材料强调长上下文、多模态与效率路线，完整统一技术报告披露有限 |
| 主要创新点 | **高效与多模态**：Flash/Next 等路线面向速度与成本，Omni 路线面向多模态输入；具体架构/训练细节需以对应模型卡或论文为准。 |
| arXiv/论文链接 | https://qwen.ai/research （研究页）；具体本窗口新增技术报告未确认 |

**2026-11-13 状态：** 未确认本窗口新增技术报告。

### 8. Yi (01.AI / 零一万物)

| 字段 | 内容 |
|---|---|
| 中文标题 | Yi 系列最新可检索公开技术披露 |
| 英文标题 | Yi series (latest publicly verifiable disclosure) |
| 发布机构 | 01.AI |
| 模型名称/系列 | Yi 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；历史细节以既有论文/模型卡为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://arxiv.org/search/?query=01.AI+Yi&searchtype=all （未确认本窗口新增） |

### 9. Baichuan (百川智能)

| 字段 | 内容 |
|---|---|
| 中文标题 | Baichuan 系列最新可检索公开技术披露 |
| 英文标题 | Baichuan series (latest publicly verifiable disclosure) |
| 发布机构 | Baichuan AI |
| 模型名称/系列 | Baichuan 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://www.baichuan-ai.com/ （官方）；技术报告链接本期未直接定位 |

### 10. Microsoft (Phi)

| 字段 | 内容 |
|---|---|
| 中文标题 | Phi 系列最新可检索公开技术披露 |
| 英文标题 | Phi series (latest publicly verifiable disclosure) |
| 发布机构 | Microsoft |
| 模型名称/系列 | Phi 系列（含小型/推理/多模态分支） |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；以既有 arXiv 技术报告与官方博客为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://arxiv.org/search/?query=Microsoft+Phi+technical+report&searchtype=all |

### 11. Apple

| 字段 | 内容 |
|---|---|
| 中文标题 | Apple Foundation Models（AFM）最新可检索公开技术披露 |
| 英文标题 | Apple Foundation Models (AFM) |
| 发布机构 | Apple |
| 模型名称/系列 | AFM 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；以 Apple Machine Learning Research 已发布论文/报告为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://machinelearning.apple.com/research |

### 12. NVIDIA

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Super 与 Lightning：面向 Agentic AI 的开放高效混合 Mamba-Transformer MoE 模型 |
| 英文标题 | Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Super / Nemotron 3.5 Lightning |
| 发布日期 | 2026-10-28（arXiv 提交） |
| 核心参数 | Super：120B 总参数 / 12B 激活，多模态；Lightning：30B 总参数 / 3B 激活，文本；面向长上下文、推理与 agentic 工作负载（详见论文） |
| 主要创新点 | **架构**：Hybrid Mamba-Transformer MoE；**训练**：大规模蒸馏、长上下文训练、SFT+RL（RLVR/RLHF），Super 含 MOPD 等；**效率/部署**：原生 speculative decoding、MTP boosting、NVFP4 量化高保真与推理吞吐优化。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.38095 |

**2026-11-13 状态：** 未确认本窗口新增更新；该报告仍为 Nemotron 3.5 系列最新核心技术报告。

### 13. xAI (Grok)

| 字段 | 内容 |
|---|---|
| 中文标题 | Grok 4.7（最新可检索公开模型发布） |
| 英文标题 | Grok 4.7 |
| 发布机构 | xAI |
| 模型名称/系列 | Grok 4.7 |
| 发布日期 | 2026-09-21（官方新闻页）；本窗口未确认新技术报告/系统卡 |
| 核心参数 | 官方强调 coding、知识工作、速度与成本改进；完整参数、训练数据与系统卡级细节未在本期检索到独立技术报告 |
| 主要创新点 | **产品与推理能力迭代**：面向 agentic coding 与知识工作；技术报告/系统卡披露程度有限，更多为产品公告。 |
| arXiv/论文链接 | https://x.ai/news/grok-4-7 （公告页，非 arXiv 技术报告） |

**2026-11-13 状态：** 未确认本窗口新增技术报告或系统卡。

### 14. Amazon (Amazon Nova)

| 字段 | 内容 |
|---|---|
| 中文标题 | Amazon Nova 系列最新可检索公开技术披露 |
| 英文标题 | Amazon Nova series (latest publicly verifiable disclosure) |
| 发布机构 | Amazon |
| 模型名称/系列 | Amazon Nova 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；以 AWS 官方文档/技术博客为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://aws.amazon.com/ai/generative-ai/nova/ |

### 15. Zhipu AI (GLM / ChatGLM / 智谱 AI)

| 字段 | 内容 |
|---|---|
| 中文标题 | GLM 系列最新可检索公开技术披露 |
| 英文标题 | GLM / ChatGLM series (latest publicly verifiable disclosure) |
| 发布机构 | Zhipu AI（智谱 AI） |
| 模型名称/系列 | GLM 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；近期版本细节以官方发布与模型页为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://open.bigmodel.cn/ （官方）；arXiv 相关检索未确认本窗口新增 |

### 16. InternLM (Shanghai AI Lab / 上海人工智能实验室)

| 字段 | 内容 |
|---|---|
| 中文标题 | InternLM 系列最新可检索公开技术披露 |
| 英文标题 | InternLM series (latest publicly verifiable disclosure) |
| 发布机构 | Shanghai AI Laboratory（上海人工智能实验室） |
| 模型名称/系列 | InternLM 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://github.com/InternLM （官方仓库）；技术报告链接本期未直接定位 |

### 17. Moonshot AI (Kimi / 月之暗面)

| 字段 | 内容 |
|---|---|
| 中文标题 | Kimi 系列最新可检索公开技术披露 |
| 英文标题 | Kimi series (latest publicly verifiable disclosure) |
| 发布机构 | Moonshot AI（月之暗面） |
| 模型名称/系列 | Kimi 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；能力与参数以官方公告/模型页为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://www.moonshot.cn/ （官方）；技术报告链接本期未直接定位 |

### 18. StepFun (阶跃星辰)

| 字段 | 内容 |
|---|---|
| 中文标题 | Step 系列最新可检索公开技术披露 |
| 英文标题 | Step series (latest publicly verifiable disclosure) |
| 发布机构 | StepFun（阶跃星辰） |
| 模型名称/系列 | Step 系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://www.stepfun.com/ （官方） |

### 19. ByteDance (豆包 / Doubao / Seed / 字节跳动)

| 字段 | 内容 |
|---|---|
| 中文标题 | Seed / Doubao 系列最新可检索公开技术披露 |
| 英文标题 | Seed / Doubao series (latest publicly verifiable disclosure) |
| 发布机构 | ByteDance（字节跳动） |
| 模型名称/系列 | Seed / 豆包（Doubao）系列 |
| 发布日期 | 本窗口未确认 2026-11-12→13 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；近期进展多见于产品与研究博客，技术报告披露程度不一 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://seed.bytedance.com/ （官方）；https://arxiv.org/search/?query=ByteDance+Seed+model&searchtype=all |

---

## 备注与局限

- 本 digest 优先收录**可验证的一手技术报告/系统卡/模型卡**；仅有新闻稿、产品页或细节不足的发布已降权或标注为“未确认技术报告/披露有限”。
- `websearch` 在本次环境中不可用，检索覆盖受限于可直接抓取页面与已知来源；建议后续结合 arXiv RSS、HF Papers、各厂商 model/system card 仓库与官方博客补全。
- 所有指标与能力描述除非另有说明均为来源自报，跨模型比较需注意评测协议、工具/思考模式、上下文设置、安全策略与是否经独立复现等差异。
