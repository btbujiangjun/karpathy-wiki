---
title: LLM 技术报告速览 — 2026-11-12
type: synthesis
created: 2026-11-12
updated: 2026-11-12
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-attention, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-12
# LLM Tech Report Digest — 2026-11-12

> 覆盖窗口：2026-11-11 → 2026-11-12（增量复核，基线为 [[2026-11-11/tech-report-digest]]）。本期对 19 家目标公司/组织的最新可验证大模型技术报告（Tech Report / Technical Report / System Card / Model Card / 官方技术披露）进行汇总。  
> 检索说明：本次运行中 `websearch` 工具调用未成功返回结果；已使用 `webfetch` 复核 arXiv、OpenAI Deployment Safety Hub、Anthropic 公告/系统卡页面、Google DeepMind Gemini 页面、Mistral/Meta/xAI/Qwen 官方页面及仓库既有记录。部分厂商页面为动态渲染，细节可能不完整；未能独立确认的新内容已明确标注。  
> 口径说明：参数量、训练数据量、上下文长度、benchmark 等多为厂商/论文自报；闭源模型细节以官方系统卡/模型卡/博客为准；“预览/权重开放/系统卡更新/技术博客/公告”与完整技术报告为不同披露层级。

## 本期结论（2026-11-12）

- **窗口内新增可确认的一手系统卡/报告：** Anthropic 于 2026-11-09 发布 **Claude Fable 5.2 / Claude Mythos 5.2** 公告并提供对应 **System Card**（公告页可访问）；这是本期相对 11-11 digest 最明确的新增一手安全/能力披露材料。
- **近期旗舰材料持续有效：** DeepSeek-V4（arXiv:2606.19348）、NVIDIA Nemotron 3.5 Super/Lightning（arXiv:2610.38095）、OpenAI GPT-6 系列系统卡/增补（Deployment Safety Hub 持续列示）、Google DeepMind Gemini 4 系列披露仍是各自最新可核验的核心技术材料之一。
- **未确认新增：** 在可访问公开材料中，Meta AI (LLaMA/Muse)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、xAI (Grok)、Amazon (Nova)、Zhipu AI (GLM)、InternLM、Moonshot AI (Kimi)、StepFun、ByteDance (Seed/Doubao) 在 2026-11-11→12 窗口内未检索到可独立确认的全新旗舰 Tech Report/System Card 首发；多数仍以近期（2026-09/10 及前后）报告、博客或模型页为最新依据。

## 重点关注方向速览

| 方向 | 代表进展（已发布/可验证） |
|---|---|
| 新架构（MoE / Mamba / Hybrid） | DeepSeek-V4 的 CSA+HCA 混合注意力与 mHC；NVIDIA Nemotron 3.5 的 Mamba-Transformer Hybrid MoE；Mistral Large 4（公开材料描述的 MLA/DSA/MoE 路线）；长上下文与推理效率驱动的稀疏/混合设计持续成为主线。 |
| 训练方法（Pre/Post/Alignment/RL） | 大规模后训练与 RL/可验证奖励、on-policy distillation（如 Nemotron 3.5 MOPD）、安全对齐与越狱/误用缓解强化（OpenAI/Anthropic 系统卡）；agentic/工具使用与长时任务鲁棒性成为后训练重点。 |
| Scaling Law / 缩放分析 | 从单纯参数缩放转向“有效智能/成本/延迟”缩放：激活参数、KV cache、speculative decoding、量化恢复、每 token 成本与吞吐成为关键指标（Nemotron 3.5、DeepSeek-V4 披露尤明显）。 |
| 多模态模型 | Gemini 4 系列、Nemotron 3.5 Super（文本/图像/视频/工具环境）、OpenAI 图像/多模态系统卡更新等延续图文音视频与 agentic 多模态趋势；部分厂商仅提供产品级披露。 |
| 长上下文模型 | 1M token 上下文在旗舰/预览模型中持续出现（DeepSeek-V4、Gemini/部分前沿模型口径）；实现依赖稀疏注意力、压缩/索引、KV 优化与 serving 系统工程。 |
| 推理模型 / Reasoning | 可调推理努力/长思考、agentic coding/科学/网络安全任务能力提升与安全分级并行；Anthropic Fable/Mythos 5.2 强调高难技术任务、coding/science/cyber 评测与对齐/防蒸馏措施。 |

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
| 核心参数 | Pro：1.6T 总参数 / 49B 激活；Flash：284B 总参数 / 13B 激活；预训练 >32T tokens；上下文 1M tokens（论文/官方口径） |
| 主要创新点 | **架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 混合注意力、mHC（Manifold-Constrained Hyper-Connections）；**优化**：Muon 优化器；**后训练**：综合 post-training；**效率**：1M 上下文下单 token 推理 FLOPs 与 KV cache 相比前代显著降低（厂商自报）。 |
| arXiv/论文链接 | https://arxiv.org/abs/2606.19348 |

**2026-11-12 状态：** 未确认 11-11→12 窗口新增一手技术报告；V4 仍为最新可核验核心技术报告。

### 2. OpenAI

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Cyber 系统卡 |
| 英文标题 | GPT-6 Cyber System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Cyber（基于 GPT-6 Astra 专用后训练） |
| 发布日期 | 2026-11-05 |
| 核心参数 | 参数量/训练数据未公开；面向授权网络安全工作 |
| 主要创新点 | **安全导向推理**：漏洞发现、利用与渗透测试等能力的受控披露；Preparedness 分级、访问控制与滥用缓解并列。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-cyber |

| 字段 | 内容 |
|---|---|
| 中文标题 | ChatGPT Images 2.6 系统卡 |
| 英文标题 | ChatGPT Images 2.6 System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | ChatGPT Images 2.6 |
| 发布日期 | 2026-11-04（Deployment Safety Hub 列示） |
| 核心参数 | 图像生成/编辑模型；具体规模与训练细节未公开 |
| 主要创新点 | **多模态/安全**：图像能力、安全评测、护栏与图像溯源（provenance）相关披露（以系统卡为准）。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/chatgpt-images-2-6 |

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Sol 与 GPT-6 Luna：2026 年 10 月更新 |
| 英文标题 | GPT-6 Sol and GPT-6 Luna: October 2026 update |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6 Sol / GPT-6 Luna |
| 发布日期 | 2026-10-07（更新）；Luna 增补 2026-10-29 |
| 核心参数 | 参数量/训练数据未公开 |
| 主要创新点 | **对齐/鲁棒性**：多轮越狱抵抗、减少规避与不诚实行为；Luna 增补涉及简洁性与指令层级/注入鲁棒性改进。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-october ；https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum |

**2026-11-12 状态：** Deployment Safety Hub 可见上述近期条目；窗口内未确认新增于 11-12 的首发系统卡（以页面公开时间为准）。

### 3. Meta AI (LLaMA)

| 字段 | 内容 |
|---|---|
| 中文标题 | Muse Wonder：面向个人与专业 AI Agent 的前沿模型（最新可检索公开披露） |
| 英文标题 | Muse Wonder: A Frontier Model For Personal & Professional AI Agents |
| 发布机构 | Meta AI / Meta Superintelligence Labs |
| 模型名称/系列 | Muse Wonder / Muse 系列 |
| 发布日期 | 2026-10-12（此前披露；本期未确认更新） |
| 核心参数 | 公开材料有限；未见完整技术报告级参数/训练数据披露 |
| 主要创新点 | **Agentic/产品导向**：面向个人与专业 agent 场景的前沿模型定位；后续 Muse Spark/Image/Video 等更新以博客为主，完整技术报告/系统卡披露有限。 |
| arXiv/论文链接 | https://ai.meta.com/blog/ （具体技术报告/系统卡未在本期检索到独立可确认链接） |

**2026-11-12 状态：** 未确认窗口内新增 LLaMA/Muse 技术报告或系统卡。

### 4. Google DeepMind (Gemini)

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 Argon：面向高难问题的前沿智能模型（模型卡/安全披露） |
| 英文标题 | Gemini 4 Argon: Built to solve your hardest problems |
| 发布机构 | Google DeepMind / Google |
| 模型名称/系列 | Gemini 4 Argon（及 Gemini 4 Carbon 等系列披露） |
| 发布日期 | 2026-09（Argon 首发，公开页面持续更新）；Carbon 等后续公告见官方页面 |
| 核心参数 | 参数量/训练数据未完全公开；官方强调长上下文、agentic coding、计算机使用、多模态与科学/安全能力（详见模型卡/评测方法页） |
| 主要创新点 | **推理与 agentic**：复杂工作流、长上下文、工具/计算机使用与科学任务；**安全**：Frontier Safety Framework 下的误用防护、注入鲁棒性、失配监控与系统加固（官方披露）。 |
| arXiv/论文链接 | https://deepmind.google/models/gemini/ ；模型卡/评测方法以 DeepMind 官方发布为准（本期未直接解析 PDF 内容） |

**2026-11-12 状态：** 未确认 11-11→12 窗口新增独立技术报告；Gemini 4 系列仍为最新旗舰披露主线。

### 5. Anthropic (Claude)

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Fable 5.2 与 Claude Mythos 5.2 系统卡 |
| 英文标题 | Claude Fable 5.2 and Mythos 5.2 System Card |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Fable 5.2 / Claude Mythos 5.2（同底座，不同安全配置/访问策略） |
| 发布日期 | 2026-11-09（公告与系统卡） |
| 核心参数 | 参数量/训练数据未公开；API 定价公告为 $8/M 输入、$40/M 输出（fast mode 更高，详见公告） |
| 主要创新点 | **高难技术能力**：agentic coding、网络安全、科学/工程、数学形式化、硬件/机器人等任务提升（厂商评测）；**效率**：较前代更快、部分场景更省 token/成本；**安全与对齐**：扩展对齐测试、沙箱逃逸倾向评测、防蒸馏强化、Fable 网络安全/生物安全护栏与 Mythos 受控访问。 |
| arXiv/论文链接 | https://www.anthropic.com/claude-fable-and-mythos-5-2 ；https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card |

**2026-11-12 状态：** 本期新增重点条目（公告 2026-11-09，系统卡可访问）。

### 6. Mistral AI

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4（最新可检索公开发布/权重信息） |
| 英文标题 | Mistral Large 4 ("Le Chonk") |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Mistral Large 4 |
| 发布日期 | 2026-10-29（此前公开发布/开放权重口径；本期未确认新报告） |
| 核心参数 | 公开材料提及大规模 MoE 与长上下文/推理取向；完整技术报告细节在本期未获取到独立 arXiv 全文 |
| 主要创新点 | **开放权重前沿模型**：面向推理、agentic 与效率的旗舰路线；具体架构/训练细节以官方发布与模型卡为准。 |
| arXiv/论文链接 | https://mistralai.com/news/ （具体技术报告页面本期未直接定位） |

**2026-11-12 状态：** 未确认窗口内新增技术报告/系统卡。

### 7. Qwen (Alibaba)

| 字段 | 内容 |
|---|---|
| 中文标题 | Qwen3.8 系列（含 Omni/Flash/Next 等近期公开更新，最新可检索） |
| 英文标题 | Qwen3.8 Series (e.g. Qwen3.8-Omni-Flash / Qwen3.8-Flash-Next) |
| 发布机构 | Alibaba Cloud / Qwen Team |
| 模型名称/系列 | Qwen3.8 系列 |
| 发布日期 | 2026-09 前后公开更新（以官方博客/API 为准；本期未确认新报告） |
| 核心参数 | 公开材料包含长上下文与多模态/效率取向；具体参数/训练数据依型号而异，完整技术报告披露不一 |
| 主要创新点 | **混合/高效架构与多模态**：Flash/Next 路线强调效率与长上下文；Omni 路线强调全模态输入；细节以官方发布为准。 |
| arXiv/论文链接 | https://qwen.ai/research （本期未获取到可解析的新技术报告正文） |

**2026-11-12 状态：** 未确认窗口内新增技术报告。

### 8. Yi (01.AI)

| 字段 | 内容 |
|---|---|
| 中文标题 | Yi 系列最新可检索公开技术披露 |
| 英文标题 | Yi series (latest publicly verifiable disclosure) |
| 发布机构 | 01.AI |
| 模型名称/系列 | Yi 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；历史细节需以既有论文/模型卡为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://arxiv.org/search/?query=01.AI+Yi&searchtype=all （未确认本窗口新增） |

### 9. Baichuan

| 字段 | 内容 |
|---|---|
| 中文标题 | Baichuan 系列最新可检索公开技术披露 |
| 英文标题 | Baichuan series (latest publicly verifiable disclosure) |
| 发布机构 | Baichuan AI |
| 模型名称/系列 | Baichuan 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://www.baichuan-ai.com/ （官方技术报告链接本期未直接定位） |

### 10. Microsoft (Phi)

| 字段 | 内容 |
|---|---|
| 中文标题 | Phi 系列最新可检索公开技术披露 |
| 英文标题 | Phi series (latest publicly verifiable disclosure) |
| 发布机构 | Microsoft |
| 模型名称/系列 | Phi 系列（含推理/多模态分支） |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；近期 Phi 报告以既有 arXiv/技术博客为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://arxiv.org/search/?query=Microsoft+Phi+technical+report&searchtype=all |

### 11. Apple

| 字段 | 内容 |
|---|---|
| 中文标题 | Apple Foundation Models（AFM）最新可检索公开技术披露 |
| 英文标题 | Apple Foundation Models (AFM) |
| 发布机构 | Apple |
| 模型名称/系列 | AFM 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；以既有 Apple 机器学习研究论文/报告为准 |
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
| 主要创新点 | **架构**：Hybrid Mamba-Transformer MoE；**训练**：大规模蒸馏、长上下文训练、SFT+RL（RLVR/RLHF）、Super 含 MOPD 等；**效率/部署**：原生 speculative decoding、MTP boosting、NVFP4 量化高保真、推理吞吐优化。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.38095 |

**2026-11-12 状态：** 未确认窗口内更新；该报告仍为 Nemotron 3.5 系列最新核心技术报告。

### 13. xAI (Grok)

| 字段 | 内容 |
|---|---|
| 中文标题 | Grok 4.7（最新可检索公开模型发布） |
| 英文标题 | Grok 4.7 |
| 发布机构 | xAI |
| 模型名称/系列 | Grok 4.7 |
| 发布日期 | 2026-09-21（官方新闻页列示；本期未确认新技术报告） |
| 核心参数 | 官方强调 coding 与知识工作、速度与成本改进；完整参数/训练数据/系统卡级细节未在本期检索到独立报告 |
| 主要创新点 | **产品/推理能力迭代**：面向 agentic coding 与知识工作；技术报告或系统卡披露程度有限。 |
| arXiv/论文链接 | https://x.ai/news/grok-4-7 （公告页，非 arXiv 技术报告） |

**2026-11-12 状态：** 未确认窗口内新增技术报告或系统卡。

### 14. Amazon (Amazon Nova)

| 字段 | 内容 |
|---|---|
| 中文标题 | Amazon Nova 系列最新可检索公开技术披露 |
| 英文标题 | Amazon Nova series (latest publicly verifiable disclosure) |
| 发布机构 | Amazon |
| 模型名称/系列 | Amazon Nova 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；以既有官方文档/技术博客为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://aws.amazon.com/ai/generative-ai/nova/ |

### 15. Zhipu AI (GLM/ChatGLM)

| 字段 | 内容 |
|---|---|
| 中文标题 | GLM 系列最新可检索公开技术披露 |
| 英文标题 | GLM / ChatGLM series (latest publicly verifiable disclosure) |
| 发布机构 | Zhipu AI (智谱 AI) |
| 模型名称/系列 | GLM 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；近期版本细节以官方发布/模型页为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://open.bigmodel.cn/ （官方）；arXiv 相关检索未确认本窗口新增 |

### 16. InternLM (Shanghai AI Lab)

| 字段 | 内容 |
|---|---|
| 中文标题 | InternLM 系列最新可检索公开技术披露 |
| 英文标题 | InternLM series (latest publicly verifiable disclosure) |
| 发布机构 | Shanghai AI Laboratory (上海人工智能实验室) |
| 模型名称/系列 | InternLM 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://github.com/InternLM |

### 17. Moonshot AI (Kimi)

| 字段 | 内容 |
|---|---|
| 中文标题 | Kimi 系列最新可检索公开技术披露 |
| 英文标题 | Kimi series (latest publicly verifiable disclosure) |
| 发布机构 | Moonshot AI（月之暗面） |
| 模型名称/系列 | Kimi 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；近期模型能力以官方公告/模型页为准 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://www.moonshot.cn/ （官方）；技术报告链接本期未直接定位 |

### 18. StepFun (阶跃星辰)

| 字段 | 内容 |
|---|---|
| 中文标题 | Step 系列最新可检索公开技术披露 |
| 英文标题 | Step series (latest publicly verifiable disclosure) |
| 发布机构 | StepFun（阶跃星辰） |
| 模型名称/系列 | Step 系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://www.stepfun.com/ （官方） |

### 19. ByteDance (豆包/Doubao/Seed)

| 字段 | 内容 |
|---|---|
| 中文标题 | Seed/Doubao 系列最新可检索公开技术披露 |
| 英文标题 | Seed / Doubao series (latest publicly verifiable disclosure) |
| 发布机构 | ByteDance（字节跳动） |
| 模型名称/系列 | Seed / 豆包（Doubao）系列 |
| 发布日期 | 本期未确认 2026-11-11→12 新发布 |
| 核心参数 | 未检索到本窗口新增技术报告；近期进展多见于产品/研究博客，技术报告披露程度不一 |
| 主要创新点 | 暂无本期新增可验证技术报告创新点可补充。 |
| arXiv/论文链接 | https://seed.bytedance.com/ （官方）；https://arxiv.org/search/?query=ByteDance+Seed+model&searchtype=all |

---

## 备注与局限

- 本 digest 优先收录**可验证的一手技术报告/系统卡/模型卡**；对仅有新闻稿或无技术细节页面的发布，已降低权重或标注为“未确认技术报告”。
- `websearch` 在本次环境中未返回有效结果，检索覆盖受限于可直接抓取页面；建议后续结合 arXiv RSS、HF Papers、各厂商 model card 仓库与官方博客做补全。
- 所有指标与能力描述除非另有说明均为来源自报，跨模型比较需注意评测协议、是否使用工具/思考模式、上下文设置与安全策略差异。
