---
title: LLM 技术报告速览 — 2026-11-14
type: synthesis
created: 2026-11-14
updated: 2026-11-14
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-attention, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-14
# LLM Tech Report Digest — 2026-11-14

> 覆盖窗口：2026-11-13 → 2026-11-14（增量复核，基线为 [[2026-11-13/tech-report-digest]]）。本期汇总 DeepSeek、OpenAI、Meta AI (LLaMA)、Google DeepMind (Gemini)、Anthropic (Claude)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、NVIDIA、xAI (Grok)、Amazon (Amazon Nova)、Zhipu AI (GLM/ChatGLM)、InternLM (Shanghai AI Lab)、Moonshot AI (Kimi)、StepFun（阶跃星辰）、ByteDance（豆包/Doubao/Seed）等 19 家目标公司/组织的最新可验证大模型技术报告（Tech Report / Technical Report / System Card / Model Card / 官方技术披露）。
>
> 检索说明：本次 `websearch` 在环境中多次不可用/取消；已通过 `webfetch` 复核 OpenAI Deployment Safety Hub（https://deploymentsafety.openai.com/）、Anthropic Claude Fable 5.2 / Mythos 5.2 公告页、arXiv 论文页（DeepSeek-V4 2606.19348、Kimi K3 2607.24653）及仓库既有 digest/index/log 记录。部分厂商页面为动态渲染或披露有限，未能独立确认的新内容已明确标注。
>
> 口径说明：参数量、训练数据量、上下文长度、benchmark 等多为厂商/论文自报；闭源模型细节以官方系统卡/模型卡/博客为准；“预览/权重开放/系统卡更新/技术博客/公告/模型页”与完整技术报告为不同披露层级。

## 本期结论（2026-11-14）

- **窗口内新增可确认的一手旗舰技术报告/系统卡：** 未检索到 2026-11-13→14 窗口内明确首发的全新旗舰 Tech Report/System Card。OpenAI Deployment Safety Hub 复核显示最新条目仍为 GPT-6 Cyber（2026-11-05）与 ChatGPT Images 2.6（2026-11-04）；Anthropic 最新一手旗舰披露仍为 Claude Fable 5.2 / Claude Mythos 5.2 System Card（2026-11-09）。
- **持续有效的核心技术材料：** DeepSeek-V4（arXiv:2606.19348）、Moonshot AI Kimi K3（arXiv:2607.24653）、NVIDIA Nemotron 3.5 Super/Lightning（arXiv:2610.38095）、Google Gemini 4 系列官方披露、Mistral Large 4 开放权重发布与相关说明等仍是各自最新可核验主材料之一。
- **未确认新增：** Meta AI (LLaMA/Muse)、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、xAI (Grok)、Amazon (Nova)、Zhipu AI (GLM)、InternLM、StepFun、ByteDance (Seed/Doubao) 在本窗口内未检索到可独立确认的全新旗舰 Tech Report/System Card 首发；以近期报告、博客、模型页或开放权重说明为最新依据。

## 重点关注方向速览

| 方向 | 趋势观察（基于最新可验证材料） | 代表工作 |
|---|---|---|
| **新架构（MoE / Mamba / Hybrid）** | 大规模 MoE 仍是前沿主线；稀疏/压缩注意力与混合架构用于长上下文与推理效率；混合 Mamba-Transformer MoE 在开放/本地化与 agentic 场景持续落地。 | DeepSeek-V4（CSA+HCA、mHC、1.6T/49B 激活）、Kimi K3（2.8T/104B 激活，KDA + Attention Residuals + Stable LatentMoE）、NVIDIA Nemotron 3.5 Super/Lightning（Hybrid Mamba-Transformer MoE） |
| **训练方法（Pre/Post/Alignment/RL）** | 后训练与 RL 持续强化推理、编码、agentic 与工具使用；安全导向后训练、受控访问、防蒸馏与系统卡化治理并重；蒸馏+SFT+RL（RLVR/RLHF/MOPD 等）成为开放模型常见组合。 | Anthropic Fable/Mythos 5.2（高难技术任务与安全/对齐/防蒸馏）、OpenAI GPT-6 Cyber / ChatGPT Images 2.6（安全评测与分级治理）、Nemotron 3.5（蒸馏、长上下文、RLVR/RLHF/MOPD） |
| **Scaling Law / 缩放分析** | 从单纯参数规模转向“有效智能/激活参数/上下文/KV cache/吞吐/成本/延迟”协同优化；百万级上下文下的 FLOPs 与 KV 效率成为关键指标。 | DeepSeek-V4（1M 上下文下单 token 推理 FLOPs 与 KV cache 显著压缩，自报）、Kimi K3（整体 scaling efficiency 提升约 2.5x，自报）、Nemotron 3.5（NVFP4/推理吞吐与 agentic 效率） |
| **多模态模型** | 原生/统一多模态理解与生成、图像编辑与溯源、视频/音频理解及工具/计算机使用能力持续增强；开放模型在多模态 agentic 场景加速。 | Google Gemini 4 系列（文本/图像/视频/音频/工具使用）、OpenAI ChatGPT Images 2.6（图像生成/编辑与安全溯源）、Kimi K3（native vision）、Nemotron 3.5 Super（多模态支持） |
| **长上下文模型** | 1M token 级上下文成为前沿与开放旗舰的重要能力点；依赖稀疏注意力、压缩、KV 优化与系统工程保障可用性与成本。 | DeepSeek-V4（1M）、Kimi K3（1M）、Gemini 4 系列（官方强调长上下文/agentic 能力）、Mistral Large 4（公开材料强调长上下文，细节披露有限） |
| **推理模型 / Reasoning model** | 高阶推理向 agentic coding、网络安全、科学/工程、数学形式化与长时任务延伸；思考强度/推理努力可调、工具使用与验证闭环成为标配方向。 | Anthropic Fable/Mythos 5.2（coding/cyber/science/engineering/形式化）、OpenAI GPT-6 Cyber（授权网络安全推理）、DeepSeek-V4/Kimi K3/Nemotron 3.5（推理与 agentic 评测提升，自报） |

---

## 公司/组织覆盖与最新状态

| 公司/组织 | 代表模型/系列 | 本窗口状态（2026-11-13→14） | 最新可验证核心材料 |
|---|---|---|---|
| DeepSeek（深度求索） | DeepSeek-V4-Pro/Flash | 无新增确认 | DeepSeek-V4 技术报告（arXiv 2606.19348） |
| OpenAI | GPT-6 Cyber, ChatGPT Images 2.6, GPT-6 Sol/Luna 系列 | 无新增确认（Hub 最新仍为 11-05/11-04） | Deployment Safety Hub 系统卡 |
| Meta AI (LLaMA/Muse) | Muse / LLaMA 系列 | 无新增确认 | 官方博客/模型页（技术报告披露有限） |
| Google DeepMind (Gemini) | Gemini 4 Argon/Carbon/Hydrogen | 无新增确认 | Gemini 官方模型页与评测方法披露 |
| Anthropic (Claude) | Claude Fable 5.2 / Mythos 5.2 | 无新增确认（最新 2026-11-09） | Fable/Mythos 5.2 公告与 System Card |
| Mistral AI | Mistral Large 4 | 无新增确认 | Mistral Large 4 开放权重发布/新闻页 |
| Qwen (Alibaba) | Qwen3.x / Qwen3.8 系列 | 无新增确认 | 官方研究/模型页（本窗口未定位新技术报告） |
| Yi (01.AI) | Yi 系列 | 无新增确认 | 历史论文/模型卡；本窗口未确认新发布 |
| Baichuan（百川智能） | Baichuan 系列 | 无新增确认 | 官方发布；本窗口未定位新技术报告 |
| Microsoft (Phi) | Phi 系列 | 无新增确认 | 历史技术报告/博客；本窗口未确认新发布 |
| Apple | Apple Foundation Models (AFM) | 无新增确认 | Apple ML Research 已有披露；本窗口未确认新发布 |
| NVIDIA | Nemotron 3.5 Super/Lightning, Nemotron 3.5 Bolt 系列 | 无新增确认 | Nemotron 3.5 Super/Lightning arXiv 2610.38095 |
| xAI (Grok) | Grok 4.7 等 | 无新增确认 | 官方新闻页（技术报告/系统卡披露有限） |
| Amazon (Amazon Nova) | Nova 2 系列 | 无新增确认 | Nova 技术报告/官方材料（本窗口未确认新发布） |
| Zhipu AI (GLM/ChatGLM) | GLM-5.x 系列 | 无新增确认 | 官方博客/模型页；本窗口未确认新技术报告 |
| InternLM (Shanghai AI Lab) | Intern-S2 等 | 无新增确认 | 官方发布/HF；本窗口未确认新技术报告 |
| Moonshot AI (Kimi) | Kimi K3 / K3.1 Pro | 无新增确认 | Kimi K3 技术报告（arXiv 2607.24653）、K3.1 Pro 博客 |
| StepFun（阶跃星辰） | Step-3 / Step 3.7 Flash 等 | 无新增确认 | 历史技术报告与官方发布；本窗口未确认新发布 |
| ByteDance（豆包/Doubao/Seed） | Seed 2.0 系列 | 无新增确认 | Seed 2.0 论文/模型卡；本窗口未确认新发布 |

---

## 重点报告详情

### 1. DeepSeek（深度求索）

| 字段 | 内容 |
|---|---|
| 中文标题 | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| 英文标题 | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| 发布日期 | 2026-04-26（arXiv 提交，v1）；预览版 2026-04-24 |
| 核心参数 | Pro：1.6T 总参数 / 49B 激活；Flash：284B 总参数 / 13B 激活；预训练 >32T tokens；上下文 1M tokens（论文/官方口径）；MoE 架构 |
| 主要创新点 | **架构**：混合注意力 Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)，提升长上下文效率；Manifold-Constrained Hyper-Connections (mHC) 增强残差连接。**优化/训练**：Muon 优化器提升收敛与稳定性；大规模高质量预训练后配合综合后训练。**效率**：1M 上下文场景下，Pro 相对 DeepSeek-V3.2 单 token 推理 FLOPs 约 27%、KV cache 约 10%（厂商自报），支持长时任务与测试时扩展。 |
| arXiv/论文链接 | https://arxiv.org/abs/2606.19348 ；模型集合：https://huggingface.co/collections/deepseek-ai/deepseek-v4 |

### 2. OpenAI

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Cyber 系统卡 |
| 英文标题 | GPT-6 Cyber System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Cyber（基于 GPT-6 Astra 的专用后训练变体） |
| 发布日期 | 2026-11-05 |
| 核心参数 | 参数量/训练数据未公开；面向授权网络安全工作场景 |
| 主要创新点 | **安全导向推理**：面向漏洞发现、利用与渗透测试等高风险网络安全能力的受控披露；结合 Preparedness 分级、访问控制与滥用缓解措施（以系统卡为准）。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-cyber |

| 字段 | 内容 |
|---|---|
| 中文标题 | ChatGPT Images 2.6 系统卡 |
| 英文标题 | ChatGPT Images 2.6 System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | ChatGPT Images 2.6 |
| 发布日期 | 2026-11-04 |
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

### 3. Anthropic (Claude)

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Fable 5.2 与 Claude Mythos 5.2 系统卡 |
| 英文标题 | Claude Fable 5.2 and Mythos 5.2 System Card |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Fable 5.2 / Claude Mythos 5.2（同底座，不同安全配置/访问策略） |
| 发布日期 | 2026-11-09（公告与系统卡） |
| 核心参数 | 参数量/训练数据未公开；公告披露定价 $8/M 输入、$40/M 输出（fast mode 更高）；支持多 effort/推理强度设置（产品侧） |
| 主要创新点 | **高难技术能力**：agentic coding、网络安全、科学/工程、数学形式化、硬件与机器人等任务显著提升（厂商评测，自报）。**效率**：较前代更快、部分场景更省 token/成本。**安全与对齐**：扩展对齐与沙箱逃逸倾向评测、cyber/biology 护栏、防蒸馏强化与 Mythos 受控访问；强调高风险能力治理与持续监控。 |
| arXiv/论文链接 | 公告：https://www.anthropic.com/claude-fable-and-mythos-5-2 ；System Card：https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card |

### 4. Moonshot AI (Kimi / 月之暗面)

| 字段 | 内容 |
|---|---|
| 中文标题 | Kimi K3：开放前沿智能 |
| 英文标题 | Kimi K3: Open Frontier Intelligence |
| 发布机构 | Moonshot AI (Kimi Team) |
| 模型名称/系列 | Kimi K3 |
| 发布日期 | 2026-07-27（arXiv v1）；2026-08-07（v2） |
| 核心参数 | 2.8T 总参数 MoE / 104B 激活参数；native vision；1M token 上下文窗口；Stable LatentMoE（896 路由专家中每 token 有效激活 16 个，论文口径） |
| 主要创新点 | **架构**：Kimi Delta Attention (KDA) 与 Attention Residuals 改善序列长度与深度上的信息流。**扩展效率**：相对 Kimi K2 整体 scaling efficiency 提升约 2.5x（自报）。**后训练**：通用、agentic、coding 等多领域 RL 与多推理努力级别，强调组合泛化与长时执行。**基础设施**：算法-系统协同、均衡 expert-parallel 训练、百万 token agentic RL、部署优化等。 |
| arXiv/论文链接 | https://arxiv.org/abs/2607.24653 |

| 字段 | 内容 |
|---|---|
| 中文标题 | Kimi K3.1 Pro 技术博客：推进开放智能 |
| 英文标题 | Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence |
| 发布机构 | Moonshot AI |
| 模型名称/系列 | Kimi K3.1 Pro / Kimi K3.1 Pro Highspeed |
| 发布日期 | 2026-10-23（博客） |
| 核心参数 | 基于 Kimi K3 的大规模后训练版本；公开信息指向 3T-class MoE、1M 上下文（细节以官方博客/模型页为准） |
| 主要创新点 | **后训练增强**：coding、3D 创作、金融研究与长时 Agent 能力提升；高速变体提升吞吐；开放权重计划见官方公告（博客/发布说明层级，非完整独立技术报告）。 |
| arXiv/论文链接 | https://www.kimi.ai/blog/kimi-k3-1-pro ；代码文档：https://www.kimi.com/code/docs/en/kimi-code/models.html |

### 5. NVIDIA

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Super 与 Lightning：面向 Agentic AI 的开放高效混合 Mamba-Transformer MoE 模型 |
| 英文标题 | Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Super / Nemotron 3.5 Lightning |
| 发布日期 | 2026-10-28（arXiv 提交） |
| 核心参数 | Super：120B 总参数 / 12B 激活，多模态；Lightning：30B 总参数 / 3B 激活，文本；面向长上下文、推理与 agentic 工作负载（详见论文） |
| 主要创新点 | **架构**：Hybrid Mamba-Transformer MoE。**训练**：大规模蒸馏、长上下文训练、SFT+RL（RLVR/RLHF），Super 含 MOPD 等。**效率/部署**：原生 speculative decoding、MTP boosting、NVFP4 量化高保真与推理吞吐优化。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.38095 |

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Bolt E4B 4GB：面向快速对话 Agent 的开放高效小语言模型 |
| 英文标题 | Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Bolt E4B 4GB |
| 发布日期 | 2026-10-23 |
| 核心参数 | 8B 总参数（4B 有效）；Gemma 4 E4B 基座 + Nemotron 后训练；面向本地/端侧对话 Agent |
| 主要创新点 | **效率优先**：优化速度/智能/显存占用平衡，支持 GGUF/NIM 等部署形态，适配本地 agent 场景。 |
| arXiv/论文链接 | 技术报告：https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Technical-Report.pdf ；项目页：https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/ |

### 6. Google DeepMind (Gemini)

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 系列（Argon / Carbon / Hydrogen）模型与安全/评测披露 |
| 英文标题 | Gemini 4 series (Argon / Carbon / Hydrogen) model and safety/evaluation disclosures |
| 发布机构 | Google DeepMind / Google |
| 模型名称/系列 | Gemini 4 Argon / Gemini 4 Carbon / Gemini 4 Hydrogen |
| 发布日期 | 系列持续更新（2026 年多次公告/页面更新）；本窗口未确认新增独立技术报告 PDF/arXiv |
| 核心参数 | 参数量/训练数据未完全公开；官方强调长上下文、agentic coding、工具/计算机使用、多模态理解与科学/安全能力（详见模型页与评测方法） |
| 主要创新点 | **前沿推理与 agentic**：复杂工作流、长时任务与多模态协同。**安全**：Frontier Safety Framework 下误用防护、注入鲁棒性与系统加固。**分层能力**：Hydrogen/Carbon/Argon 覆盖不同性能-成本定位（官方披露）。 |
| arXiv/论文链接 | https://deepmind.google/models/gemini/ ；评测方法示例：https://deepmind.google/models/evals-methodology/gemini-4-carbon |

### 7. Mistral AI

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4（开放权重旗舰） |
| 英文标题 | Mistral Large 4 |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Mistral Large 4 |
| 发布日期 | 2026-10-06（发布）/ 2026-10-29（开放权重，新闻页）；本窗口未确认新增 arXiv 技术报告 |
| 核心参数 | 公开材料定位为大规模前沿开放模型，面向 coding/cyber/agentic 与长上下文场景；完整参数、训练数据与统一技术报告细节在本期未获取到独立 arXiv 全文 |
| 主要创新点 | **开放权重前沿**：面向 agentic coding、推理与安全相关能力，强调生态与可部署性；技术细节主要通过新闻/产品文档披露。 |
| arXiv/论文链接 | https://mistral.ai/news/mistral-large-4 ；https://mistral.ai/news/mistral-large-4-oss/ |

### 8. Meta AI (LLaMA / Muse)

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse 系列前沿模型（最新可检索公开披露） |
| 英文标题 | Muse family frontier models (latest publicly verifiable disclosure) |
| 发布机构 | Meta AI / Meta Superintelligence Labs |
| 模型名称/系列 | Muse 系列（如 Muse Spark / Muse Image / Muse Video 等） |
| 发布日期 | 本窗口未确认新增技术报告/系统卡 |
| 核心参数 | 公开材料有限；未见完整技术报告级参数/训练数据/上下文统一披露 |
| 主要创新点 | **Agentic 与多模态产品化**：面向 agent、图像与视频等方向迭代；技术细节多以博客/产品页呈现。 |
| arXiv/论文链接 | https://ai.meta.com/blog/ |

### 9. Qwen (Alibaba / 阿里巴巴通义千问)

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.x / Qwen3.8 系列（最新可检索公开披露） |
| 英文标题 | Qwen3.x / Qwen3.8 series (latest publicly verifiable disclosure) |
| 发布机构 | Alibaba Cloud / Qwen Team |
| 模型名称/系列 | Qwen3.x / Qwen3.8 系列 |
| 发布日期 | 本窗口未确认新增技术报告 |
| 核心参数 | 依型号而异；公开材料强调长上下文、多模态与效率路线，统一技术报告披露有限 |
| 主要创新点 | **高效与多模态**：Flash/Next/Omni 等分支面向不同速度-成本-能力权衡；具体架构/训练细节需以对应模型卡或论文为准。 |
| arXiv/论文链接 | https://qwen.ai/research ；arXiv 检索：https://arxiv.org/search/?query=Qwen+technical+report&searchtype=all |

### 10. xAI (Grok)

| 字段 | 内容 |
|---|---|
| 中文标题 | Grok 4.7（最新可检索公开模型发布） |
| 英文标题 | Grok 4.7 |
| 发布机构 | xAI |
| 模型名称/系列 | Grok 4.7 |
| 发布日期 | 2026-09-21（官方新闻页）；本窗口未确认新技术报告/系统卡 |
| 核心参数 | 官方强调 coding、知识工作、速度与成本改进；完整参数、训练数据与系统卡级细节未在本期检索到独立技术报告 |
| 主要创新点 | **推理与产品迭代**：面向 agentic coding 与知识工作；披露以公告为主。 |
| arXiv/论文链接 | https://x.ai/news/grok-4-7 |

### 11. Amazon (Amazon Nova)

| 字段 | 内容 |
|---|---|
| 中文标题 | Amazon Nova 2 技术报告（最新可检索主要技术报告） |
| 英文标题 | Amazon Nova 2: Technical Report |
| 发布机构 | Amazon AGI / AWS |
| 模型名称/系列 | Amazon Nova 2 系列 |
| 发布日期 | 2025-12-02（技术报告）；本窗口未确认新增报告 |
| 核心参数 | 多尺寸/多模态；具体参数与训练细节见技术报告 |
| 主要创新点 | **多模态与部署优化**：面向理解、推理与产品化部署能力（以技术报告为准）。 |
| arXiv/论文链接 | https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf |

### 12. Microsoft (Phi)

| 字段 | 内容 |
|---|---|
| 中文标题 | Phi-4-reasoning-vision-15B 技术报告（近期可检索代表性报告） |
| 英文标题 | Phi-4-reasoning-vision-15B Technical Report |
| 发布机构 | Microsoft Research |
| 模型名称/系列 | Phi-4-reasoning-vision-15B |
| 发布日期 | 2026-03-04；本窗口未确认新增报告 |
| 核心参数 | 15B 参数；多模态推理模型 |
| 主要创新点 | **紧凑多模态推理**：动态分辨率视觉编码、推理/非推理能力结合，面向高效部署与推理任务。 |
| arXiv/论文链接 | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ ；PDF：https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi-4-reasoning-vision-15B-Tech-Report-1.pdf |

### 13. Apple

| 字段 | 内容 |
|---|---|
| 中文标题 | 第三代 Apple Foundation Models（最新可检索公开披露） |
| 英文标题 | Third Generation of Apple’s Foundation Models (AFM) |
| 发布机构 | Apple |
| 模型名称/系列 | Apple Foundation Models (AFM 2026) |
| 发布日期 | 2026-06-08；本窗口未确认新增技术报告 |
| 核心参数 | AFM 家族（含端侧与服务器模型，多尺寸；具体配置以官方披露为准） |
| 主要创新点 | **端侧与隐私优先**：效率优化、私有云计算协同、Foundation Models 框架扩展；完整统一技术报告链接在本期未直接定位。 |
| arXiv/论文链接 | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

### 14. Zhipu AI (GLM / ChatGLM / 智谱 AI)

| 字段 | 内容 |
|---|---|
| 中文标题 | GLM-5.3：面向复杂编程与涌现网络安全能力的前沿模型（最新可检索代表性披露） |
| 英文标题 | GLM-5.3: Frontier Coding with Emergent Cyber Capabilities |
| 发布机构 | Zhipu AI (Z.ai) |
| 模型名称/系列 | GLM-5.3 |
| 发布日期 | 2026-08-14；本窗口未确认新增技术报告 |
| 核心参数 | 753B 总参数（~40B 激活，官方/社区口径）；MoE；基于 GLM-5.2 基座后训练增强（以官方为准） |
| 主要创新点 | **Agentic coding 与长时任务**：复杂编程与长时代理能力提升，支持可调推理强度；安全与能力边界需结合系统/产品策略理解。 |
| arXiv/论文链接 | https://z.ai/blog/glm-5.3 ；平台页：https://build.nvidia.com/z-ai/glm-5-3 |

### 15. InternLM (Shanghai AI Lab / 上海人工智能实验室)

| 字段 | 内容 |
|---|---|
| 中文标题 | Intern-S2-397B：科学智能体基础模型（最新可检索代表性发布） |
| 英文标题 | Intern-S2-397B: Scientific Agentic Foundation Model |
| 发布机构 | Shanghai AI Laboratory（上海人工智能实验室） |
| 模型名称/系列 | Intern-S2-397B |
| 发布日期 | 2026-09-13（发布口径）；本窗口未确认新增技术报告 |
| 核心参数 | 397B 总参数（17B 激活）；Multimodal MoE；262K 上下文；MTP（公开材料口径） |
| 主要创新点 | **科学 Agent**：面向长周期科学研究与多模态科学任务；Apache-2.0 开源与生态支持（以官方/HF 为准）。 |
| arXiv/论文链接 | https://huggingface.co/internlm/Intern-S2-397B ；相关论文检索：https://arxiv.org/abs/2608.13505 （如可用） |

### 16. StepFun（阶跃星辰）

| 字段 | 内容 |
|---|---|
| 中文标题 | Step 3.7 Flash（最新可检索代表性发布） |
| 英文标题 | Step 3.7 Flash |
| 发布机构 | StepFun（阶跃星辰） |
| 模型名称/系列 | Step 3.7 Flash |
| 发布日期 | 2026-05-29（官方发布）；本窗口未确认新增技术报告 |
| 核心参数 | 198B 总参数（11B 激活）；Sparse MoE；原生多模态；256K 上下文（官方口径） |
| 主要创新点 | **高效 Agent 与多模态理解**：面向编码、GUI/工具调用与图像视频理解，推理强度可调。 |
| arXiv/论文链接 | https://www.stepfun.com/step-3.7-flash ；GitHub：https://github.com/stepfun-ai/Step-3.7-Flash |

### 17. ByteDance（豆包 / Doubao / Seed / 字节跳动）

| 字段 | 内容 |
|---|---|
| 中文标题 | Seed 2.0 模型卡/技术报告 |
| 英文标题 | Seed 2.0 Model Card / Technical Report |
| 发布机构 | ByteDance Seed |
| 模型名称/系列 | Seed 2.0（Pro/Lite/Mini） |
| 发布日期 | 2026-02-14（官宣）；2026-06-30（arXiv 2607.00248，社区/索引口径） |
| 核心参数 | 多尺寸（Pro/Lite/Mini）；Omni-modal（video/image/audio/text）；具体参数规模以官方模型卡/论文为准 |
| 主要创新点 | **全模态与 Agent**：实时交互、音视频联合理解、App/GUI 生成与 agentic coding 能力增强。 |
| arXiv/论文链接 | https://arxiv.org/abs/2607.00248 ；GitHub：https://github.com/ByteDance-Seed/Seed2.0 ；Model Card：https://github.com/ByteDance-Seed/Seed2.0/blob/master/Seed2.0%20Model%20Card.pdf |

### 18. Yi (01.AI / 零一万物)

| 字段 | 内容 |
|---|---|
| 中文标题 | Yi 系列（最新可检索公开技术披露） |
| 英文标题 | Yi series (latest publicly verifiable disclosure) |
| 发布机构 | 01.AI |
| 模型名称/系列 | Yi 系列 |
| 发布日期 | 本窗口未确认 2026-11-13→14 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；历史细节以既有论文/模型卡为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://arxiv.org/search/?query=01.AI+Yi&searchtype=all |

### 19. Baichuan（百川智能）

| 字段 | 内容 |
|---|---|
| 中文标题 | Baichuan 系列（最新可检索公开技术披露） |
| 英文标题 | Baichuan series (latest publicly verifiable disclosure) |
| 发布机构 | Baichuan AI |
| 模型名称/系列 | Baichuan 系列 |
| 发布日期 | 本窗口未确认 2026-11-13→14 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://www.baichuan-ai.com/ ；arXiv 检索：https://arxiv.org/search/?query=Baichuan+technical+report&searchtype=all |

---

## 备注与局限

- 本 digest 优先收录**可验证的一手技术报告/系统卡/模型卡/官方技术披露**；仅有新闻稿或细节不足的发布已降权或标注状态。
- 受 `websearch` 不可用及部分页面动态渲染限制，本期覆盖可能遗漏近 24 小时内的小范围更新；建议后续结合 arXiv RSS、HF Papers、各厂商 model/system card 仓库与官方博客补全。
- 所有指标与能力描述除非另有说明均为来源自报，跨模型比较需注意评测协议、工具/思考模式、上下文设置、安全策略与是否独立复现等差异。
- 结论日期：2026-11-14（Asia/Shanghai 视角的当日整理，基于可获取公开信息）。
