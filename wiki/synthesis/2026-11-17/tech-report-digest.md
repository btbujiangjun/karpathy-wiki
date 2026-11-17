---
title: LLM 技术报告速览 — 2026-11-17
type: synthesis
created: 2026-11-17
updated: 2026-11-17
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-attention, continuous-diffusion, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, child-safety, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-17
# LLM Tech Report Digest — 2026-11-17

> 覆盖窗口：2026-11-16 → 2026-11-17（增量复核，基线为 [[2026-11-16/tech-report-digest]]）。本期汇总 DeepSeek、OpenAI、Meta AI (LLaMA)、Google DeepMind (Gemini)、Anthropic (Claude)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、NVIDIA、xAI (Grok)、Amazon (Amazon Nova)、Zhipu AI (GLM/ChatGLM)、InternLM (Shanghai AI Lab)、Moonshot AI (Kimi)、StepFun（阶跃星辰）、ByteDance（豆包/Doubao/Seed）等 19 家目标公司/组织的最新可验证大模型技术报告（Tech Report / Technical Report / System Card / Model Card / 官方技术披露）。
>
> 检索说明：`websearch` 工具在环境中不可用/被取消（返回 "Web search cancelled"）；已通过 `webfetch`/HTTP 直接复核 OpenAI Deployment Safety Hub、Anthropic Newsroom、Google DeepMind Gemini 模型页、Meta AI 博客、xAI News、Mistral News 等一手页面，并通过 arXiv Export API 与 Hugging Face API 做增量扫描。arXiv 最新批次截至 2026-11-14（2026-11-15→17 尚无新提交），故窗口内新增以官方页面披露为准。
>
> 口径说明：参数量、训练数据量、评测指标等多为厂商/论文自报；闭源模型细节以官方系统卡/模型卡/博客/模型页/评测方法页为准；“技术报告/论文、系统卡、模型卡、博客、模型页”属于不同披露层级，本文按可获得信息分别标注。

## 本期结论（2026-11-17）

- **窗口内新增确认披露（1 项）：** **OpenAI CSAM Image Classifier Model Card**（2026-11-16 发布）——内部 CLIP 图像编码器 + 三层 MLP 的视觉安全分类器，训练数据 505K 正样本 / 913K 负样本，离线评测集约 46,849 张，含 AI 生成 CSAM 检测信号；由 NCMEC 协助构建，向获批机构免费开放。这是本窗口唯一可确认的一手 Model Card 首发。
- **新近“浮现”但未入上一期基线的官方系统卡（2 项）：** **GPT-6.1 Terra**（GPT-6 Astra 系统卡增补，2026-10-26；快速高效的高容量专业工作模型，网络安全 Critical / 生物化学 High）、**GPT-Rosalind-6 系统卡增补**（2026-10-30；与 GPT-6 Astra 同权重、面向生物/药物发现的 trusted-access 推理模型）。二者均在 OpenAI Deployment Safety Hub 可见，上一期未单列，本期补入。
- **新架构重点（持续更新）：** NVIDIA **Nemotron-Labs-Sigma** —— 首个大规模（3B/8B）**连续扩散语言模型（continuous dLM）**家族，论文 *Large Language Continuous Diffusion Models*（arXiv:2610.02665，v2 2026-11-12）；配套 3B/8B 基座、instruct、Phased DMD 少步蒸馏（NFE 2/4/8/16）与自推测变体模型卡在 Hugging Face 于 2026-11-12→16 集中更新（14 项 collection）。属 MoE/Mamba/hybrid 之外的另一条新架构路线（低维 ODE/SDE 潜轨迹 + 连续扩散头 + 辅助 AR readout）。
- **旗舰披露复核：** Google Gemini 4 **Hydrogen**（2026-11 公告，官方模型页 + 评测方法页）评测表新增 Hydrogen 列，对标 GPT-6.1 Terra 与 Claude Sonnet 5.5；Anthropic **Claude Fable 5.2 & Mythos 5.2**（2026-11-09 公告与系统卡）仍为最新旗舰；DeepSeek-V4（arXiv:2606.19348）、NVIDIA Nemotron 3.5 Super/Lightning（arXiv:2610.38095）仍为可核验核心材料。
- **未确认新增：** Meta AI、Mistral AI、Qwen、Yi、Baichuan、Microsoft Phi、Apple、xAI、Amazon Nova、Zhipu GLM、InternLM、Moonshot Kimi、StepFun、ByteDance 在本窗口内未检索到可独立确认的全新旗舰 Tech Report/System Card 首发；下列按各家最新可核验披露汇总。

## 重点关注方向速览

| 方向 | 代表进展（已发布/可验证） |
|---|---|
| 新架构（MoE / Mamba / Hybrid / Diffusion） | NVIDIA Nemotron-Labs-Sigma 连续扩散语言模型（3B/8B，16-D 连续 token 嵌入 + 辅助 AR readout，Phased DMD 少步蒸馏 NFE 2/4/8/16）；Nemotron 3.5 Super/Lightning 的 Hybrid Mamba-Transformer MoE；DeepSeek-V4 的 CSA+HCA 混合注意力与 mHC；UniSpark-9B 的 MoT + 全注意力/GatedDeltaNet 线性注意力混合（arXiv:2611.16517）。 |
| 训练方法（Pre/Post/Alignment/RL） | OpenAI CSAM Classifier 的 CLIP+MLP 迁移/微调与难负例（Re-LAION-5B）误报控制；GPT-6.1 Terra 沿用 Astra 数据与训练、分级 Preparedness 安全后训练；Nemotron-Labs-Sigma 以分块似然优化 + Phased Distribution Matching Distillation 实现少步生成；Nemotron 3.5 的 MOPD/SFT+RLVR；Anthropic 的防蒸馏与对齐评测。 |
| Scaling Law / 缩放分析 | 缩放重心持续从“参数规模”转向“有效智能/成本/延迟/吞吐/上下文/步数”：Nemotron-Labs-Sigma 以固定 NFE（2–16）刻画“生成步数–质量”权衡；Gemini 4 Hydrogen/Carbon 以 agentic coding、长上下文 GraphWalks（256k→1M）、计算机使用等任务做能力-成本分层；激活参数、KV cache、量化（NVFP4）与投机解码成为共性维度。 |
| 多模态模型 | OpenAI CSAM Classifier 为图像安全分类（含 AI 生成图像信号）；GPT-6.1 Terra 强调图像分析与计算机使用；Gemini 4 系列统一文本/图像/视频/音频与工具使用；LongCat-Video-Avatar 1.6（arXiv:2611.18822，音频驱动数字人视频）与 UniSpark-9B（图文理解+生成统一）为窗口内相邻多模态技术报告。 |
| 长上下文模型 | Gemini 4 Carbon 官方表披露 GraphWalks 256k→1M BFS F1 达 96.2%；DeepSeek-V4 1M 上下文路线与 CSA/HCA；Nemotron-Labs-Sigma 当前版本上下文 4,096 tokens（定位为少步生成研究而非长上下文）。 |
| 推理模型 / Reasoning | GPT-6.1 Terra / GPT-Rosalind-6（ frontier reasoning，生命科学/高风险双用途方向）、Gemini 4 Hydrogen（SWE-sweep 13.5%、HLE-Diamond 58.8%）、Claude Fable 5.2/Mythos 5.2（coding/science/cyber）、DeepSeek-V4 后训练推理增强；OpenAI 系统卡新增“评测觉察（evaluation awareness）”等 monitorability 量纲（GPT-6.1 Terra 9.88% 轨迹出现觉察迹象）。 |

---

## 本期重点条目（窗口内新增 + 新近浮现）

### A. 窗口内新增（2026-11-16）

| 字段 | 内容 |
|---|---|
| 中文标题 | OpenAI CSAM 图像分类器模型卡 |
| 英文标题 | OpenAI CSAM Image Classifier Model Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | OpenAI CSAM Image Classifier（图像安全分类器，非 LLM） |
| 发布日期 | 2026-11-16 |
| 核心参数 | 内部 CLIP 图像编码器 + 3 层 MLP（编码器在深度/隐宽/预训练数据上区别于公开 CLIP，微调部分层）；训练：505K 正样本 / 913K 负样本（likely-csam），离线评测集约 46,849 张（7K 正 / 40K 负），另用约 1.25M Re-LAION-5B-research 图像做误报评测；PDQ 感知去重；默认阈值 likely-csam 0.996324、likely-csam/gen-ai 0.90；held-out recall 0.802 / 0.864，Re-LAION 误报率 0.000004 / 0。参数量与“上下文长度”不适用（图像分类）。 |
| 主要创新点 | **架构复用**：预训练 CLIP 视觉表征 + 任务特定 MLP，泛化与吞吐优于在单 benchmark 更高分的候选架构；**双信号**：`likely-csam` 与 `likely-csam/gen-ai`（AI 生成 CSAM 风险信号，不验证来源）；**难负例与去重**：以成人/NSFW 开放网络数据做误报代理、PDQ 跨分割去重（仍存同案跨年图像泄漏限制）；**人口统计评测**：按年龄/种族/性别报告 recall 差异（LLM 标注，方向性参考）；**分层部署**：与哈希匹配、上下文滥用检测、人工审核组合，向 NCMEC 协助的获批机构免费开放，API 不留存图像。 |
| arXiv/论文链接 | 模型卡：https://deploymentsafety.openai.com/csam-image-classifier （View PDF 可下载；申请入口 https://openai.com/form/csam-classifier-intake ） |

### B. 新近浮现的官方系统卡（上一期未单列）

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Astra 系统卡增补：GPT-6.1 Terra |
| 英文标题 | Addendum to GPT-6 Astra System Card: GPT-6.1 Terra |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6.1 Terra（GPT-6 系列） |
| 发布日期 | 2026-10-26 |
| 核心参数 | 参数量/训练数据量/上下文长度未公开；与 GPT-6 Astra 使用相同类型的数据与训练。Preparedness：网络安全 **Critical**、生物化学 **High**、AI 自我改进低于 High。关键自报指标：ExploitBench ACE 归一化 97.10%，ExploitBench 内部端口（2026-06→08）ACE 成功率 24.5%，SEC-Bench Pro pass@1 83.33%，Sandbox Bench 5/22（22.7%）；MentalHealthBench 55.5%（GPT-5.6 Terra 46.2%）；48,690 匹配任务中 severity≥3 失配标记 22 次（0.045%，较 GPT-6 Sol 少约 42%）。 |
| 主要创新点 | **高效专业工作模型**：强图像分析与计算机使用、面向高容量专业流程；**评测觉察（evaluation awareness）量纲**：9.88% 轨迹出现 CoT 中“意识到处于评测”的迹象（GPT-6.1 Sol 4.35%、原始流量 0.75%）；**监控鲁棒性**：750–1250 token 区间 CoT 可控性 14.8%（GPT-6 Sol 23.2%、GPT-6.1 Sol 44.8%），数学侧任务监控逃逸未观察到成功；**对齐细节**：Auto-review 绕过 0%，Respecting Warnings 成功绕过 29.6%（高于 Astra/Sol，低于 GPT-6 Sol），外部 agent 消息场景未授权动作 13.75%。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-1-terra |

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-Rosalind-6 系统卡增补 |
| 英文标题 | GPT-Rosalind-6 System Card Addendum |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-Rosalind-6（GPT-Rosalind-6 Research，trusted access） |
| 发布日期 | 2026-10-30 |
| 核心参数 | 与 GPT-6 Astra **同权重**，未新增训练数据或后训练；参数量未公开。自报生命科学基准（最高推理预算）：MedChemBench v7 49.6%（5.5 版 28.9%）、GeneBench Pro v13 单试成功率 37.7%（16.7%）、LifeSciBench Gold 61.3%（44.0%）。Preparedness：生物化学 High、网络安全 Critical（继承 Astra）、AI 自我改进低于 High。 |
| 主要创新点 | **领域化“少拒绝”推理模型**：在双用途生物查询上降低拒绝率，但仅通过 trusted access 向审核通过的科研/政府/企业开放，保留生物武器化拒绝；**部署治理四组件**：trusted-access 准入、模型级生物/网络边界、监控与执行、合同安全要求；**拒绝调整能力评估**：Biorisk knowledge cons@32 78.3%、拒绝调整后 85.0%（Astra 90.0%）；四项 Critical 生物设计评测均未达阈值。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-rosalind-6 |

### C. 新架构更新（持续）

| 字段 | 内容 |
|---|---|
| 中文标题 | 大型语言连续扩散模型（Nemotron-Labs-Sigma） |
| 英文标题 | Large Language Continuous Diffusion Models (Nemotron-Labs-Sigma) |
| 发布机构 | NVIDIA（Nemotron Labs） |
| 模型名称/系列 | Nemotron-Labs-Sigma（3B / 8B；base / instruct / few-step distilled NFE 2/4/8/16 / self-speculative，共 14 项 HF collection） |
| 发布日期 | 论文 arXiv:2610.02665（v1 2026-10-02；v2 2026-11-12）；模型卡 HF 发布 2026-11-12，collection 2026-11-16 更新 |
| 核心参数 | 8B：Ministral 式 decoder-only Transformer（GQA、SwiGLU、RoPE，34 层、隐宽 4096）+ 连续扩散生成头（16-D 连续 token 嵌入空间）+ 辅助 AR readout 头；上下文 4,096 tokens；学生模型由 MS-SUSReg-8B 教师经 **Phased DMD（Phased Distribution Matching Distillation）** 蒸馏，每个 32-token 块固定 NFE+1 次去噪调用；自报六任务均值：GSM8K(CoT) 86.86、MATH 61.52、HumanEval 60.61、HumanEval+ 57.99、MBPP 57.50、MBPP+ 73.70，均值 66.36（±0.46，10 seeds），NFE=4 版本。 |
| 主要创新点 | **连续扩散 LM 家族**：以可操控的低维 ODE/SDE 潜轨迹取代离散 dLM 的高维非平滑空间，便于推理轨迹引导与加速；**分块似然训练 + 少步蒸馏**：Phased DMD 产出 NFE=2/4/8/16 的固定步数变体（步数由训练固定，推理不暴露任意步覆盖），以“步数–质量”曲线刻画推理/延迟权衡；**self-speculative 变体**；开放权重（NVIDIA Nemotron Open Model License），需 CUDA/bfloat16。 |
| arXiv/论文链接 | https://arxiv.org/abs/2610.02665 ；模型集合：https://huggingface.co/collections/nvidia/nemotron-labs-sigma （示例模型卡 https://huggingface.co/nvidia/Nemotron-Labs-Sigma-distill-8B-nfe4 ） |

### D. 旗舰模型页评测更新（非独立技术报告）

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 系列（Argon / Carbon / Hydrogen）模型与评测/安全披露 |
| 英文标题 | Gemini 4 series (Argon / Carbon / Hydrogen) model, evaluation, and safety disclosures |
| 发布机构 | Google DeepMind / Google |
| 模型名称/系列 | Gemini 4 Argon / Carbon / Hydrogen |
| 发布日期 | Argon：2026-09 公告、10 月更新；Carbon：2026-10 公告、11 月“now available”；Hydrogen：2026-11 公告（官方模型页） |
| 核心参数 | 参数量/训练数据量未公开。官方评测表（Hydrogen）：SWE-sweep 13.5%、Terminal-Bench 4.1（cheating-adjusted）57.0%、Agents' Last Exam v1.1 71.6%、AutomationBench-AA 76.1%、Vending-Bench 2 $14,549、OSWorld-2.1（offline）77.6%、MKAClimb 53.4%、Chartography 66.6%、Terminal-Bench-Science 0.1 51.4%、HLE-Diamond 58.8%；Carbon：AA Index v5.0 59、GraphWalks 256k→1M BFS F1 96.2%、CWE-bench 71.0%、SEC-bench Pro 88.2%（对标列含 GPT-6.1 Terra、Claude Sonnet 5.5）。 |
| 主要创新点 | **前沿推理与 Agentic**：复杂工作流、终端/代码/科学任务、长时任务、多模态协同；**长上下文**：GraphWalks 256k→1M 评测；**安全**：Frontier Safety Framework 下的误用防护、间接提示注入鲁棒性、CoT/动作监控与隔离沙箱；**分层能力**：Argon/Carbon/Hydrogen 覆盖不同性能-成本-速度定位（自报 benchmark）。 |
| arXiv/论文链接 | https://deepmind.google/models/gemini/ ；评测方法：https://deepmind.google/models/evals-methodology/gemini-4-hydrogen 、 https://deepmind.google/models/evals-methodology/gemini-4-carbon （未见独立 arXiv 技术报告） |

---

## 各公司/组织最新可验证技术报告一览（19 家）

> 下表逐家给出中文/英文标题、发布机构、模型系列、日期、核心参数、主要创新点与链接；“窗口状态”标明是否在本窗口内确认新增。

| # | 机构 | 中文标题 / 英文标题 | 模型名称/系列 | 发布日期 | 核心参数 | 主要创新点 | 链接 | 窗口状态 |
|---|---|---|---|---|---|---|---|---|
| 1 | DeepSeek | DeepSeek-V4：迈向高效百万 Token 上下文智能 / DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence | DeepSeek-V4-Pro / Flash | 2026-04-24 预览 / 04-26 arXiv v1 | Pro 1.6T 总 / 49B 激活；Flash 284B / 13B；预训练 >32T tokens；1M 上下文 | CSA+HCA 混合注意力、mHC、Muon、面向 1M 上下文的 FLOPs/KV 优化 | arxiv.org/abs/2606.19348 | 无新增，V4 仍为核心 |
| 2 | OpenAI | CSAM 图像分类器模型卡 / GPT-6.1 Terra 增补 / GPT-Rosalind-6 增补（详见重点条目 A、B） | CSAM Classifier / GPT-6.1 Terra / GPT-Rosalind-6 | 2026-11-16 / 10-26 / 10-30 | 见重点条目 | 视觉安全分类；高效推理 + 评测觉察；生物领域 trusted-access | deploymentsafety.openai.com/… | **窗口内新增 1 项 + 浮现 2 项** |
| 3 | Meta AI | Muse 系列前沿模型（最新公开披露）/ Muse family frontier models | Muse（Spark/Image/Video 等） | 近期博客更新（本窗口未确认新增） | 无系统性技术报告披露 | Agentic 与多模态产品化；技术报告级细节有限 | ai.meta.com/blog/ | 无新增 |
| 4 | Google DeepMind | Gemini 4 系列模型与评测/安全披露 / Gemini 4 series model & eval disclosures | Argon / Carbon / Hydrogen | 2026-09→11（Hydrogen 11 月） | 参数未公开；Hydrogen/Carbon 评测见表 D | 前沿推理、长上下文、agentic、安全分层 | deepmind.google/models/gemini/ | 评测表更新（见 D） |
| 5 | Anthropic | Claude Fable 5.2 与 Mythos 5.2 / Claude Fable 5.2 and Mythos 5.2 | Fable 5.2 / Mythos 5.2 | 2026-11-09 公告 + 系统卡 | 参数未公开；$8/M in、$40/M out（fast $16/$80） | coding/science/cyber/agentic 能力；对齐评估、防蒸馏、Enterprise Frontier Safeguards | anthropic.com/claude-fable-and-mythos-5-2 ；系统卡 anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card | 无新增，仍为最新旗舰 |
| 6 | Mistral AI | Le Chonk / Voxtral 3 / Timestral / Mistral Large 4（最新公开披露）/ recent open-weight disclosures | Large 4 / Le Chonk / Voxtral 3 / Timestral | 2026-10-06 Large 4、10-20 Voxtral 3、10-29 Le Chonk 权重、11-05 Studio 产品 | Large 4：1T 总 / 52B 激活（HF 有 NVFP4 版）；Timestral 5M–209M | 开放权重、agentic coding、网络安全；语音/时序专用模型 | mistral.ai/news/ | 无新增旗舰技术报告 |
| 7 | Qwen (Alibaba) | Qwen3.8 / Qwen-Image 2.1 系列近期发布 / recent Qwen releases | Qwen3.8-Flash-Next / Qwen3.8-27B / Qwen-Image 2.1 | 2026-08→10 HF 更新（Qwen3.8-Flash-Next 08-24 创建、11-07 更新） | 各分支参数/上下文见模型卡 | 长上下文、推理、多模态、开放权重生态 | qwen.ai/research ；huggingface.co/Qwen | 无新增旗舰技术报告 |
| 8 | Yi (01.AI) | Yi 系列模型（最新公开披露）/ Yi series models | Yi / Yi-Coder | 无窗口内新增（历史模型卡为主） | 以历史材料为准 | 公开信息有限 | huggingface.co/01-ai | 无新增 |
| 9 | Baichuan | Baichuan 系列模型 / Baichuan series models | Baichuan-M3 / M2 | 无窗口内新增（M3 2026-01 HF） | M3 235B（FP8/GPTQ-INT4 量化版） | 医疗/通用能力迭代；本窗口无新披露 | huggingface.co/baichuan-inc | 无新增 |
| 10 | Microsoft (Phi) | Phi 系列小型/推理模型 / recent Phi small/reasoning models | Phi 系列 + MAI 模型线 | 近期研究/产品博客（本窗口未确认新增） | 以对应模型卡为准 | 小模型高效推理、数据策展、后训练、多模态 | microsoft.com/en-us/research/ | 无新增 |
| 11 | Apple | Apple Foundation Models / AFM / Apple Foundation Models | AFM（设备端/服务器）、LensVLM-9B 等 | 近期论文/研究页（本窗口未确认新增） | 以已发布技术报告为准 | 设备端效率、隐私、适配器/压缩、多模态 | machinelearning.apple.com/research | 无新增 |
| 12 | NVIDIA | Nemotron-Labs-Sigma / Nemotron 3.5 Super & Lightning（详见重点条目 C）/ Large Language Continuous Diffusion Models; Nemotron 3.5 | Sigma 3B/8B；3.5 Super 120B/12B active、Lightning 30B/3B active | Sigma 论文 v2 2026-11-12、模型卡 11-12→16；3.5 2026-10-28 | Sigma 8B、4,096 ctx、NFE 2/4/8/16；3.5 Super 多模态、NVFP4 | 连续扩散 LM + Phased DMD；Hybrid Mamba-Transformer MoE、蒸馏、MOPD、投机解码 | arxiv.org/abs/2610.02665 ；arxiv.org/abs/2610.38095 | **Sigma collection 11-16 更新** |
| 13 | xAI (Grok) | Grok 系列近期模型 / recent Grok models | Grok 4.7 / Grok Voice 3.0 / Grok Bot 1.0 | 2026-09-22 Grok 4.7、10-14 Voice 3.0、11-02 Bot 1.0（xAI 现属 SpaceXSI） | 参数/训练数据公开有限 | 推理、语音、实时信息、工具使用、持久化 agent | x.ai/news | 无新增旗舰技术报告 |
| 14 | Amazon (Nova) | Amazon Nova / LAR 系列近期模型 / Amazon Nova & LAR models | Nova 系列 / LAR-27B / LAR-9B | LAR 2026-10-14 HF | 以官方模型卡为准（LAR 27B/9B） | 多模态理解/生成、企业部署、成本/延迟优化 | amazon.science ；huggingface.co/amazon | 无新增旗舰技术报告 |
| 15 | Zhipu AI (GLM) | GLM / ChatGLM 系列近期模型 / recent GLM models | GLM 系列 | 近期官方发布/模型仓库（本窗口未确认新增） | 以对应模型卡/论文为准 | 长上下文、推理、Agent、多模态 | 官方渠道与 arXiv/HF | 无新增 |
| 16 | InternLM (Shanghai AI Lab) | InternLM / Intern 系列近期模型 / recent InternLM models | InternLM / Intern 系列 | 近期官方发布/论文（本窗口未确认新增） | 以对应技术报告为准 | 开放研究模型、长上下文、推理、多模态 | 官方渠道与 arXiv/HF | 无新增 |
| 17 | Moonshot AI (Kimi) | Kimi K3.1 Pro 等近期模型 / recent Kimi models | Kimi-K3.1-Pro（HF 11-02；NVIDIA NVFP4 版 11-11） | 2026-11-02 HF（K3.1 Pro） | 以模型卡为准；参数未统一披露 | 长上下文、推理、Agent、开放/商用 | huggingface.co/moonshotai | 无新增技术报告（权重更新） |
| 18 | StepFun（阶跃星辰） | Step 5 Preview 等近期模型 / recent Step models | Step-5-Preview（BF16/NVFP4） | HF 2026-09-20 创建、10-15 更新 | 以发布说明/模型卡为准 | 多模态、推理、高性价比推理服务 | huggingface.co/stepfun-ai | 无新增技术报告 |
| 19 | ByteDance（豆包/Doubao/Seed） | Doubao / Seed 系列近期模型 / recent Doubao/Seed models | Doubao / Seed 系列 | 近期官方发布/云与研究页（本窗口未确认新增） | 以对应模型卡/论文为准 | 多模态、推理、Agent、大规模产品化 | 官方渠道与 arXiv/HF | 无新增旗舰技术报告 |

---

## 窗口内相邻 arXiv 技术报告（非目标公司，供架构/多模态趋势参考）

| 中文标题 / 英文标题 | 机构 | 日期 | 核心信息 | 链接 |
|---|---|---|---|---|
| LongCat-Video-Avatar 1.6 技术报告 / LongCat-Video-Avatar 1.6 Technical Report | Meituan（美团 LongCat） | 2026-11-13 | 音频驱动数字人视频生成；在 1.5 基础上改善长序列自然度、唇音同步与误差累积 | https://arxiv.org/abs/2611.18822 |
| UniSpark：面向多模态理解与生成的混合注意力探索 / UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation | （见论文） | 2026-11-12 | UniSpark-9B：MoT 主干（每分支约 9B），全注意力 + GatedDeltaNet 线性注意力混合，统一图文理解与生成 | https://arxiv.org/abs/2611.16517 |
| Mythos 5 在英国 AISI 2026 年 7 月安全事件中的行为对齐调查 / Alignment Investigation of Mythos 5's behaviour in UK AISI's July 2026 Security Incident | （见论文） | 2026-11-05 | 针对 Anthropic Mythos 5 对齐行为的第三方安全事件分析 | https://arxiv.org/abs/2611.10030 |

---

## 备注与风险

- **检索局限：** `websearch` 不可用；arXiv API 最新批次截至 2026-11-14，官方页面部分动态渲染或抓取受限，可能遗漏未被直接抓取到的最新发布。建议后续复核各厂商官网、Hugging Face、arXiv 与模型 API 文档。
- **“浮现”与“首发”区分：** GPT-6.1 Terra（10-26）、GPT-Rosalind-6（10-30）与 Nemotron-Labs-Sigma（论文 10-02/v2 11-12）并非本窗口首发，而是上一期基线未单列、本期经一手页面复核后补入；其披露日期以官方页面为准。
- **可比性限制：** 不同机构的参数口径（总参数/激活参数）、上下文定义、训练数据统计、评测设置与工具链差异较大，benchmark 多为自报，不可直接横比。
- **披露层级差异：** 系统卡/模型卡/博客/模型页不等同于完整技术报告；本文已在各条目中尽量区分。
- **合规提示：** 涉及 CSAM 检测、网络安全、生物等双用途能力的模型访问与使用应遵循官方政策与适用法律法规；CSAM 分类器仅向获批机构开放，分数不构成法律判定。

*Preference file active: `EXTEND.md` (repo root, bm25 mode `auto_prompt`).*
