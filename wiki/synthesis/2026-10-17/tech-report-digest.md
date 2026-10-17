---
title: "LLM Tech Report Digest — 2026-10-17"
type: synthesis
created: 2026-10-17
updated: 2026-10-17
sources: []
tags: [tech-report, LLM, technical-report, model-card, arXiv, microsoft, mai-base-2, nvidia, nemotron, midtraining, reflection, beam, open-weights, apache-2.0, openai, gpt-6-astra, google-deepmind, gemini-4-argon, mistral-large-4, long-context, moe, daily-digest]
---

# LLM Tech Report Digest — 2026-10-17

> **窗口判定：2026-10-16 → 2026-10-17。** 本期有 **两份目标机构的一手技术报告/技术博文** 落地：**Microsoft AI 的 MAI-Base-2 预训练报告（10-15 发布 / 10-16 广泛覆盖，10-16 期漏收）** 与 **NVIDIA 的开放 midtraining 配方 arXiv 论文（2610.22019，10-16）**。同时 **Reflection AI 的 501B 开放权重模型 Beam 1.0（10-16）正式释出**，把 10-05/10-09 期"承诺开放权重、待落地"的悬案结清。其余为**产品更新与首方博文**：**OpenAI GPT-6 Astra Pro 并行 agents（10-16）**、**Google DeepMind Gemini 4 Argon 机器人物理推理博文（10-16）**、**Mistral Large 4 STEMBench 公告（10-16）**。

> **本期主线：① 基座预训练报告回归——Microsoft 用 2.8T/80B 原生多模态 MoE（16k GB200、38 天、MFU 21%）把"自研全栈 + 无蒸馏 + 4.2–12.3× FLOPs 效率"摆上台面，但不开放权重；② NVIDIA 把"pretraining 与 post-training 之间的 midtraining 阶段"首次以开放配方形式（256K 上下文、软件工程数据 + 少量 agentic traces）公开，并给出 SWE-bench 增益的消融；③ 开放权重端由非目标机构 Reflection 接力——Beam 1.0 以 Apache 2.0 释出，是"美国实验室 500B 级开放权重"的又一落地；④ 产品层 OpenAI 把多 agent 并行搬进 ChatGPT Pro。**

---

## 本期要点（相对 2026-10-16 新增/更新）

- ★★★ **Microsoft AI 完成 MAI-Base-2 预训练（Microsoft AI，2026-10-15 技术博文 / 10-16 广泛覆盖）**——**80B 激活 / 2.8T 总参数的 MoE 基座**，**102 层 / hidden 8704 / 每层 MoE**（1 shared + 7 routed / 512 experts）、**原生 VLM**（视觉从预训练起纳入，无独立图像编码器）、**50T tokens（视觉-语言占 18% ≈ 9T，其中 4.5T unique）**、知识截止 **2026-03**。训练口径：**16k GB200 GPU × 38 天（2026-08~09）、平均 MFU 21%、goodput 89%**；**Muon 优化器**（非 embedding 的 2D 参数用 AdamW）、MXFP8 E4M3、全局权重梯度 + 激活梯度裁剪。官方称其**比最强的开放基座 DeepSeek-V4-Pro-Base **4.2–12.3× 更 FLOPs-efficient**、较 MAI-Base-1 提升 **6.3–12.7×**，且**不使用任何蒸馏**。**⚠️ 不开放权重**：MAI-Base-2 仍在 post-training，权重计划**经 Foundry 授权给受信伙伴**；MAI-Base-3 已开始筹备。**（本报告 10-16 期漏收，本期补录。）**
- ★★ **NVIDIA arXiv 2610.22019「Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe」（NVIDIA，2026-10-16）**——把介于 pretraining 与 post-training 之间的 **midtraining 阶段** 首次以**开放配方**公开：**256K 上下文、数千亿 token**，数据为**自然软件工程语料**（packed repositories、pull requests、commit histories、build logs）+ **少量 agentic traces**。**Nemotron 3.5 Lightning** 上 500B midtraining tokens 使 **SWE-bench Verified 60.7→64.5、SWE-bench Multilingual 55.8→62.8、SWE-bench Pro 32.0→35.5**（相同 full SFT 后）；**Nemotron 3.5 Super** 上 280B tokens 使 **DeepSWE 11.7→15.7、SWE-bench Verified 72.9→74.3**。**关键方法教训**：base-model 代理指标与 post-training 结果**不可靠相关**，故评测协议建立在**短固定 SFT run** 之上；并给出配方背后的消融。
- ★★ **Reflection AI Beam 1.0 正式释出开放权重（Reflection AI，2026-10-16，非 19 家目标机构）**——**501B 总参 / 23B 激活的稀疏 MoE**、**1M 上下文**、text-in/out、**Apache 2.0**。**BF16 / FP8 / NVFP4 三份权重 + DFlash2 speculative decoding drafter** 上 Hugging Face（`reflection/Beam-1.0-501B-A23B`，NVFP4 约 280GB），day-0 支持 transformers / SGLang / vLLM / Unsloth / Axolotl，全参数 RL 走 Miles。**reasoning 五档 low/medium/high/xhigh/max** + `preserve_thinking`（跨轮保留推理）+ tool-calling grammar；随附 **Mirror CLI**（Python 前端 + Rust agent core）与 **Beam Safety Technical Report**。**23.8T 预训练 token**；RL 在 **10.5K GB300 上 4 周、>1 亿 rollouts**。OpenRouter 定价 $0.25/$1.00 per M。**10-05/10-09 期"承诺开放权重"悬案结清。**
- ★ **OpenAI：GPT-6 Astra Pro 并行 agents（OpenAI，2026-10-16）**——ChatGPT **Pro 用户**的 GPT-6 Astra Pro 获更新：响应更快、插件/工具调用更好，且**多个 agent 可并行处理同一任务的不同部分**并可跟踪进度——属 **ChatGPT 产品更新**（"28 天体验优化计划"第 12 项），**非技术报告/模型卡**；无 benchmark、无定价、无插件清单、无 agent 数量上限，且未说明 subagent 是否各自计配额。API 侧并行 subagents 为 **Responses API beta（GPT-6.1 Sol / GPT-5.6）**，与 ChatGPT 功能属两套口径。
- ★ **Google DeepMind：Gemini 4 Argon 机器人物理推理博文（Google DeepMind，2026-10-16）**——首方博文把 Argon 定位为**面向机器人全生命周期的通用物理推理模型**，宣称在 **Embodied Reasoning（ERQA）基准上以纯推理取得 87%、超越所有 frontier 模型**；demo 含 Boston Dynamics Spot 踩脚踩式垃圾桶、sketch-to-simulation 的 76-DoF Apollo 2 人形、ALOHA 2 折纸视频标注。**⚠️ 首方声明、未点名对照模型、无 release date/pricing/API、demo 无 trial 计数**——属展示性博文（非 model card；Argon model card 见 10-13/10-14 期）。
- ★ **Mistral：Mistral Large 4 STEMBench 公告（Mistral AI，2026-10-16）**——公布 Mistral Large 4（「Le Chonk」，**1T 总参 / 49B 激活、natively multimodal**）在 Ulam 私有 STEMBench（工程 + 天文）上的表现，并重申"美欧最强开放权重"、SOTA 于 cyber defense / 制造 / 金融、视觉 grounding 超过闭源 frontier；**API 已可用，开放权重承诺 10 月底（HF 占位页标 10-31）**。⚠️ 沿用既有激活参数口径冲突（本报告不裁定）。

---

## 一、Microsoft MAI-Base-2（Microsoft AI，2026-10-15 技术博文 / 10-16 覆盖）

| 字段 | 内容 |
|------|------|
| **中文标题** | 微软完成 MAI-Base-2 预训练：2.8T/80B 原生多模态 MoE 基座 |
| **英文标题** | Frontier Pre-training at Microsoft AI |
| **发布机构** | Microsoft AI |
| **模型名称** | `MAI-Base-2`（基座，非产品；MAI-Base-1 为 MAI-Thinking-1 底座） |
| **发布日期** | 2026-10-15（技术博文）；本 wiki 于 10-16 覆盖 |
| **核心参数** | **80B 激活 / 2.8T 总参数 MoE**；**102 层、hidden 8704**；**每层 MoE**（1 shared + 7 routed / 512 experts，shared expert 不做 down/up projection）；attention：**每 6 层 1 层 global**，96 heads（local 96 / global 16）；**untied embeddings**；**原生 VLM**（无独立图像编码器）；**50T 训练 token（视觉-语言 18% ≈ 9T，其中 4.5T unique）**；知识截止 **2026-03**；**Muon 优化器**（非 embedding 的 2D 参数用 AdamW）、**MXFP8 E4M3**、全局权重梯度 + 激活梯度裁剪。 |
| **训练基础设施** | **16,000 张 NVIDIA GB200 × 38 天（2026-08~09）**；**平均 MFU 21%**（按 GB200 BF16 理论峰值 2.5 PFLOPS 归一，不含 rematerialization 与优化器 FLOPs）；**goodput 89%**。对比 MAI-Base-1 用约 8,192 张 GB200、30T token。 |
| **主要创新点** | ① **source scaling（固定 TPP）**：保持 unique data / parameters 比值恒定，使 scaling ladder 的小规模实验可可靠外推到 2.8T，是"可靠扩到 2.8T"的关键；② **全栈自有数据管线**（质量分类、网页解析、去重、评测/训练去重）——**明确不使用任何蒸馏**；③ **Muon 优化器**替换 AdamW、MXFP8 精度、激活梯度裁剪；④ **原生 VLM 预训练**（视觉非后接编码器）。 |
| **效率声明（自评）** | **较 DeepSeek-V4-Pro-Base 4.2–12.3× FLOPs-efficient**（对 4 个 held-out 评测各拟合 BPB–FLOPs scaling law）；**较 MAI-Base-1 提升 6.3–12.7×**。⚠️ 以 BPB 拟合外推，非直接 benchmark 对打。 |
| **开放性与后续** | **⚠️ 不开放权重**：仍在 post-training，权重计划**经 Foundry 授权给受信伙伴**（未公布伙伴/日期）；定位为"下一代模型的基座"；**MAI-Base-3** 已开始筹备。 |

> **对照 MAI-Base-1**：35B 激活 / 1T 总参、78 层、hidden 6656、**交替 dense FFN + MoE**、30T token、AdamW、FP8 delay scaling；MAI-Base-2 为**更大更稀疏 + 每层 MoE + Muon + 原生 VLM**。

---

## 二、NVIDIA arXiv 2610.22019「An Open Midtraining Recipe」（NVIDIA，2026-10-16）

| 字段 | 内容 |
|------|------|
| **中文标题** | 为 agentic post-training 铺垫基座模型：一份开放的 midtraining 配方 |
| **英文标题** | Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe |
| **发布机构** | NVIDIA（作者含 Soumye Singhal, Joseph Jennings, Ka Shun Shum, Alexander Bukharin, Khushi Bhardwaj, Zirui Liu, Venkat Srinivasan 等） |
| **模型名称** | Nemotron 3.5 Lightning、Nemotron 3.5 Super |
| **发布日期** | 2026-10-16 |
| **arXiv** | 2610.22019 |
| **核心参数** | midtraining **256K 上下文**、**数千亿 token**；数据为**自然软件工程语料**（packed repositories、pull requests、commit histories、build logs）+ **少量 agentic traces**。 |
| **主要创新点** | ① **首次把 frontier 模型"pretraining → midtraining → post-training"三段中的 midtraining 阶段以开放配方形式公开**；② **软件工程语料 + 少量 agentic traces** 的混合设计（pretraining 短上下文、几乎无 agent 交互，而 SFT 数据多为合成、过长 SFT 反而损害后续 RL）；③ **评测协议建立在短固定 SFT run 之上**，因为 **base-model 代理指标与 post-training 结果不可靠相关**；④ 给出配方背后的**消融**。 |
| **关键结果（相同 full SFT 后）** | **Nemotron 3.5 Lightning**（500B midtraining tokens）：**SWE-bench Verified 60.7→64.5**、**SWE-bench Multilingual 55.8→62.8**、**SWE-bench Pro 32.0→35.5**。**Nemotron 3.5 Super**（280B tokens）：**DeepSWE 11.7→15.7**、**SWE-bench Verified 72.9→74.3**。两模型均**在不同 agent harness 上鲁棒性提升**。 |

---

## 三、Reflection AI Beam 1.0（Reflection AI，2026-10-16）

> **⚠️ Reflection AI 不属本期 19 家目标机构清单**（美国新实验室），因规模可观、且为 10-05/10-09 期悬案的落地，作**全条目记录**。

| 字段 | 内容 |
|------|------|
| **中文标题** | Reflection 释出 Beam 1.0：501B/23B 开放权重 MoE，Apache 2.0 |
| **英文标题** | Beam is now available / Welcome Beam: a 501B open model you can own, customize, and scale |
| **发布机构** | Reflection AI |
| **模型名称** | `reflection/Beam-1.0-501B-A23B`（BF16 / FP8 / NVFP4 三份） |
| **发布日期** | 2026-10-16 |
| **核心参数** | **501B 总参 / 23B 激活稀疏 MoE**；**1M 上下文**；text-in / text-out；**Apache 2.0**；**23.8T 预训练 token**；**BF16 / FP8 / NVFP4 + DFlash2 speculative drafter**（NVFP4 约 **280GB**）；**reasoning 五档 low/medium/high/xhigh/max** + `preserve_thinking`（推理跨轮保留）+ tool-calling grammar；tokenizer 内含 response template。 |
| **基础设施 / 生态** | **RL：10.5K GB300 × 4 周、>1 亿 rollouts**；day-0 支持 transformers / SGLang / vLLM / Unsloth / Axolotl，全参数 RL 走 Miles；随附 **Mirror CLI**（Python 前端 + Rust agent core）+ **Beam Safety Technical Report**；**40+ 伙伴**（含 Google Cloud A4X Max / vLLM 融合 kernel）。 |
| **关键 benchmark（模型卡，自评，BF16）** | **SWE-bench Verified 81.6**、**SWE Bench Pro v2-Hard 76.5**、**Terminal Bench v2.1 80.1**、**DeepSWE v1.1 43.3**、SWE Bench Multilingual 78.3；**GPQA Diamond 90.6**、**AIME 2026 97.7**、HLE 36.0（无工具）/ 51.1（有工具）、LiveCodeBench 88.3、SciCode 49.2；MCP Atlas 80.8、tau3 Banking 36.1、BrowseComp 76.8、LongBench v2 67.5、IFBench 79.6。（FP8/NVFP4 分数略降，NVFP4 保留大部分质量。） |
| **定价（第三方）** | OpenRouter **$0.25 input / $1.00 output per M**（第三方观测：性价比高但当前托管缓存命中低、速度偏慢）。 |

---

## 四、OpenAI GPT-6 Astra Pro 并行 agents（OpenAI，2026-10-16，产品更新）

| 字段 | 内容 |
|------|------|
| **中文标题** | OpenAI 为 ChatGPT Pro 的 GPT-6 Astra Pro 加入多 agent 并行 |
| **英文标题** | GPT-6 Astra Pro upgrade — parallel agents in ChatGPT |
| **发布机构** | OpenAI |
| **发布日期** | 2026-10-16（X 帖子 / Help Center 释放说明） |
| **性质** | **ChatGPT 产品更新（非技术报告/模型卡）**，"28 天体验优化计划"第 12 项 |
| **核心内容** | GPT-6 Astra Pro（ChatGPT Pro）响应更快、插件/工具调用更好，**多个 agent 可并行处理同一任务的不同部分**，用户可跟踪各 agent 进度并逐一查看结果；面向 Pro 用户（managed workspace 受设置与 rollout 资格限制）。 |
| **已知缺口** | **无 benchmark、无定价、无插件清单、无 agent 数量上限**；**未说明 subagent 是否各自计配额**（Pro 配额：$100/月 50 条 Astra Pro/周；$200/月 200 条/周、硬上限 200/天）；无中途干预/暂停单个 agent 的机制说明。**"提速 ~50%"为计划第 1 天已公布内容，非本期新增。** |
| **口径区分** | **API 侧并行 subagents** 为 **Responses API beta（GPT-6.1 Sol / GPT-5.6）**，与 ChatGPT 的 Astra Pro 并行功能属两套独立口径。 |

---

## 五、Google DeepMind Gemini 4 Argon 机器人物理推理博文（2026-10-16，首方博文）

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepMind 展示 Gemini 4 Argon 作为机器人全生命周期的通用物理推理模型 |
| **发布日期** | 2026-10-16 |
| **性质** | **首方产品博文 / demo（非 model card；Argon model card 见 10-13/10-14 期）** |
| **核心内容** | 把 Argon 定位为**通用物理推理模型**，覆盖机器人全生命周期；宣称 **ERQA 基准 87%（纯推理）"超越所有 frontier 模型"**。demo：Boston Dynamics Spot（12-DoF 腿 + 6-DoF 臂）在 MuJoCo 数字孪生练习后踩脚踩式垃圾桶；sketch-to-simulation 生成 76-DoF Apollo 2 人形 mujoco_warp 场景并验证 6/6 box knockdown（pelvis drift <3cm）；ALOHA 2 折纸视频标注（1 goal / 6 subtasks / 17 atomic primitives）。 |
| **⚠️ 局限** | 首方声明、**未点名对照模型**、无 competitor 分数；**无 release date / pricing / API**；demo **无 trial 计数与成功率**，部分无法确认是否真机端到端；Argon 主推把工作**落到代码/场景描述 + 物理仿真闭环**而非直接输出电机指令。 |

---

## 六、Mistral Large 4 STEMBench 公告（Mistral AI，2026-10-16）

| 字段 | 内容 |
|------|------|
| **中文标题** | Mistral Large 4（Le Chonk）公布 STEMBench 工程/天文成绩 |
| **发布日期** | 2026-10-16 |
| **性质** | **benchmark 公告（非新模型；preview 自 10-06 起）** |
| **核心内容** | **1T 总参 / 49B 激活、natively multimodal**；公布于 Ulam 私有 **STEMBench**（工程 + 天文）的表现；重申"美欧最强开放权重"、SOTA 于 cyber defense / 制造 / 金融、视觉 grounding 超闭源 frontier；欧洲端到端、经 Mistral Cloud 可欧洲部署；**API 已可用**。 |
| **⚠️ 待落地** | **开放权重承诺 10 月底（Hugging Face 占位页标 10-31）**；激活参数口径冲突延续（官方 49B vs 既往 docs/二手口径），未裁定。 |

---

## 19 家目标机构窗口内（2026-10-16 → 2026-10-17）复核

| 机构 | 窗口内新报告 / 系统卡 | 备注 |
|------|----------------------|------|
| OpenAI | 无（产品更新） | **GPT-6 Astra Pro 并行 agents（§4，10-16）** 非技术报告；GPT-6.1 Sol 预计 **10-19** |
| Anthropic | 无 | Sonnet 5.5 / Haiku 5.5 分析见 The Batch（10-16，非新发布）；Haiku 5.5 卡见 10-07 |
| Google DeepMind | 无（首方博文） | **Gemini 4 Argon 机器人博文（§5，10-16）** 非 model card；Argon model card / 安全报告见 10-13 / 10-14 期 |
| Meta | 无 | Muse Wonder 系列见 10-12/10-13 期；Muse Spark Open 见 10-16 期 |
| Microsoft AI | **有（★★★，技术报告）** | **MAI-Base-2 预训练报告（§1，10-15/16，10-16 期漏收）**；MAI-Base-3 筹备中 |
| xAI | 无 | Grok Voice 3.0 见 10-14 期；Grok 4.7 见 10-11 期 |
| Mistral | **有（★，benchmark 公告）** | **Mistral Large 4 STEMBench（§6，10-16）**；开放权重承诺 10 月底（HF 占位 10-31） |
| DeepSeek | 无 | V4.1-Flash 见 10-12 期；**V4.1 Pro 仍未发布**（无卡/端点/价格/日期，第三方预告 11-12） |
| Alibaba Qwen | 无 | Qwen4 训练中（未发布）；Qwen3.8-Omni-Flash 候选见 10-14 期 |
| ByteDance Seed | 无 | 产品向（豆包 Seedance 2.0 等） |
| Moonshot | 无 | Kimi K3 往期（权重 07-27）；"10-17 开源"报道判为**旧闻二次传播** |
| Zhipu | 无 | GLM-5.3-Highspeed 见 10-14 期；GLM-5.5 未宣布 |
| Tencent | 无 | Hy4 preview 往期 |
| Baidu | 无 | — |
| Amazon | 无 | Nova 2.5 Sonic GA 见 10-10 期 |
| NVIDIA | **有（★★，arXiv 技术报告）** | **arXiv 2610.22019 midtraining recipe（§2，10-16）**；Nemotron 3.5 Super VL / Bolt 见 10-16 / 10-15 期 |
| Cohere | 无 | — |
| AI2 | 无 | Olmo Hybrid / Bolmo 见 10-12 期 |
| Perplexity | 无 | Decider 往期 |

> 附注（非 19 家，同窗口）：**Reflection AI Beam 1.0 开放权重落地（§3，10-16，美国新实验室）**。

---

## 本期不重复收录（交叉引用）

- **Meta Muse Spark Open（816B/42B）/ NVIDIA Nemotron 3.5 Super VL 120B-A12B / StepFun Step 5 Preview 权重 / 蚂蚁 Ling-3.1-flash**：见 10-16 期。
- **Google Gemini 4 Argon GA + Model Card**：见 10-14 期（本期仅新增机器人博文）。
- **Meta Muse Wonder / Muse Wonder Full**：见 10-12 / 10-13 期。
- **NVIDIA Nemotron 3.5 Bolt 74B-A9B / E4B、Nemotron 3.5 Lightning/Ultra、Zhipu GLM-5.3-Highspeed、xAI Grok Voice 3.0、DeepSeek V4.1-Flash、Mistral Large 4 preview**：往期已录。
- **Anthropic weight-based replicator / Claude Haiku 5.5 系统卡 / Claude Sonnet 5.5**：见 10-07 / 10-12 / 10-14 期。

---

## 口径与不确定性声明

- **窗口边界**：主窗口 **2026-10-16 → 2026-10-17**。Reflection Beam 1.0（10-16）、NVIDIA arXiv 2610.22019（10-16）、OpenAI GPT-6 Astra Pro（10-16）、Gemini 4 Argon 机器人博文（10-16）、Mistral Large 4 STEMBench（10-16）为窗口内；**Microsoft MAI-Base-2（公告 10-15）为窗口邻接补录**（10-16 期漏收，本期明确标注）。
- **首次建档**：本期首次为 **Microsoft MAI-Base-2**、**NVIDIA arXiv 2610.22019 midtraining 配方**、**Reflection AI Beam 1.0 开放权重** 建立 wiki 记录。
- **目标机构 vs 非目标机构**：**Reflection AI 不属 19 家目标机构**，本期作全条目邻近记录（与 10-09 期处理 Beam 承诺时一致）。
- **自评 / 首方声明**：Microsoft 效率声明为 **BPB–FLOPs scaling law 外推**（非直接 benchmark 对打），MAI-Base-2 的 benchmark 数值未在本报告采用（官方以 held-out BPB 曲线呈现）；NVIDIA 结果为其自身 SFT 协议下；Reflection benchmark 为厂商自评（AA / OpenRouter 定价为第三方）；Gemini 4 Argon ERQA 87% 与 Mistral STEMBench 均为**首方声明、对照信息不全**。**各厂商 benchmark 表不可跨厂商横向比较。**
- ⚠️ **待落地项**：**Mistral Large 4 开放权重承诺 10 月底（HF 占位 10-31）**；**DeepSeek V4.1 Pro 仍未发布**（第三方预告 11-12，官方仅 09-10 条件性提及）；**Reflection Beam 自 10-16 上 OpenRouter，托管缓存/速度仍在优化**。
- **旧闻排除**：**"Moonshot 10-17 开源 Kimi K3"报道**判为旧闻二次传播（K3 权重为 07-27），不采信；**Anthropic Sonnet/Haiku 5.5** 的 10-16 报道为 The Batch 分析，非新发布。
- **语言**：本期沿用 tech-report-digest 系列既有约定（中文正文 + 英文技术术语），与 10-11 → 10-16 期保持一致。
