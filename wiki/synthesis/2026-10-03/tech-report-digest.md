---
title: "LLM Tech Report Digest — 2026-10-03"
type: synthesis
created: 2026-10-03
updated: 2026-10-03
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-architecture, scaling-law, long-context, multimodal, reasoning, RL, agent, open-source, daily-digest]
---
# LLM Tech Report Digest — 2026-10-03

> 全球主要 AI 公司大模型技术报告速览（覆盖窗口 2026-10-02，arXiv 补扫至 2026-10-03）
>
> **本日窗口判定：19 家目标机构在 2026-10-02 至 10-03 期间无任何新的 frontier 技术报告 / System Card 发布。** 10-03 为周六，10-02 为周五，两日均无 arXiv 新公告批次（最近批次为 2026-09-30 / 10-01）。
>
> 与前几日 digest 不同的是：本日的实质增量不来自"当日新闻"，而来自**对 9 月下旬 arXiv 技术报告的补扫**——筛出 4 篇此前尚未被本 wiki 收录、且直接对应目标机构的技术报告（美团 LongCat-DeepResearch、小米 Xiaomi-OCR-0、阿里 Qwen-Audio-Agent、阶跃 StepAudio 3 Realtime），外加 2 项模型发布但**未附基准/未附报告**的发布事件（美团 LongCat-2.5-Preview、月之暗面 Kimi K3 进入 OpenAI 企业渠道）。全部条目已做 arXiv ID 去重核验（写入前 `grep` 全 wiki 命中 0）。

---

## 1. 美团 LongCat — LongCat-DeepResearch 技术报告（★ 新收录）

- **中文标题**：LongCat-DeepResearch：面向证据接地深度研究的多智能体工作流
- **英文标题**：LongCat-DeepResearch Technical Report
- **发布机构**：美团（Meituan）LongCat 团队
- **模型名称/系列**：LongCat-DeepResearch（基于增强版 LongCat 通用模型）
- **发布日期**：**2026-09-28**（arXiv v1）
- **arXiv 链接**：[arXiv:2609.36071](https://arxiv.org/abs/2609.36071)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| DeepResearchBench | **55.25** |
| DeepResearchBench II | **51.35** |
| ResearchRubrics | **79.83** |
| 内部基准（4 套系统对比） | **76.04（第 2 名）** |
| 底座模型参数 | 报告未在摘要中披露；LongCat 2.0 为 **1.6T MoE / ~48B 激活**（二手来源，见 §3 注） |
| 上下文 | 底座 LongCat-2.5-Preview 为原生 **1M tokens** |

### 主要创新点

- **工作流分层：全局规划 vs 细节调查彻底解耦**。多个 planning agent 先探索外部信源，迭代收敛出一份可执行的 **ResearchSpec**；随后 research agent **并行**撰写各自负责的章节，在独立上下文中随分析展开**增量补充证据**（而非一次性检索）。
- **章节级修订取代全文重写**。章节装配完成后由 global review 指导**定向的局部修订**，显著降低"重复全文重写"的依赖——这是本报告最可迁移的工程决策。
- **工作流反哺 mid-training / post-training**。同一套 workflow 同时用于构造研究任务的**任务与轨迹数据**，即 DeepResearch 的编排设计直接成为通用 LongCat 模型的中训练/后训练数据来源（workflow-as-data-engine）。
- **开发集分析给出两条负向/混合结论**（值得注意，作者未粉饰）：① 组合多种 planning 视角确有收益；② **进一步的 planning refinement 效果混合**（more refinement ≠ better）；③ 额外编辑能提升两个基准上的平均自动可读性偏好，但**两个基准趋势不一致**。

> **口径注**：四个量化结果均为**单一团队自报**，无第三方复现。内部基准"第 2 名"的对比集仅 4 套系统，样本极小，不宜作横向定位依据。

---

## 2. 小米 Xiaomi-OCR-0 技术报告（★ 新收录）

- **中文标题**：Xiaomi-OCR-0：面向文档解析与 OCR 中心理解的 0.8B 统一模型
- **英文标题**：Xiaomi-OCR-0 Technical Report
- **发布机构**：小米（Xiaomi）
- **模型名称/系列**：Xiaomi-OCR-0（从 **Qwen3.5-0.8B** 初始化）
- **发布日期**：**2026-09-28**（arXiv v1，cs.CV）
- **arXiv 链接**：[arXiv:2609.36136](https://arxiv.org/abs/2609.36136)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| 总参数量 | **0.8B**（统一单模型，非 MoE） |
| 底座 | Qwen3.5-0.8B |
| OCR 中心语料 | **约 1.7 亿（170M）样本** |
| Real5-OmniDocBench | **95.24** |
| OmniDocBench v1.6 | **96.83** |
| Wild-OmniDocBench | **87.94** |
| 5 个 OCR 导向 VQA 基准均值 | **83.2** |

### 主要创新点

- **用自动化数据引擎替代昂贵人工监督**：语料构建结合 **专家共识（expert consensus）+ 渲染校验（render-based verification）+ 定向合成（targeted synthesis）** 三种机制，规模化到 1.7 亿样本。这是本报告最实用的部分——OCR 专用小模型（0.8B）长期受制于监督成本，此路径给出可复制的降本方案。
- **渐进式训练配方**：**Q-Mask 文本锚定（text anchoring）→ continued pretraining → 混合任务强化学习（Mix-RL）** 三段递进，而非一次性混合训练。
- **消融给出一条反直觉结论**：**在解析训练已充分的前提下，额外的 OCR 中心理解监督仍能进一步提升文档解析性能**。这与"解析与理解可互相替代"的朴素假设相反，值得记入 [[wiki 方法页]]候选。

> **口径注**：0.8B 模型在 OmniDocBench v1.6 上 96.83，属专用模型对比通用模型的场景，不可与通用多模态大模型的同类分数直接比较。作者署名为 9 人（小米），未列机构块；机构归属依据论文自身标定的 arXiv 题名与作者构成，**未从姓氏推断**。

---

## 3. 阿里 Qwen — Qwen-Audio-Agent 技术报告（★ 新收录）

- **中文标题**：Qwen-Audio-Agent：全双工语音交互与异步任务执行的前后台架构
- **英文标题**：Qwen-Audio-Agent Technical Report
- **发布机构**：阿里巴巴 Qwen 团队
- **模型名称/系列**：Qwen-Audio-Agent（**架构 harness，非新基座模型**）
- **发布日期**：**2026-09-21**（arXiv v1）
- **arXiv 链接**：[arXiv:2609.25195](https://arxiv.org/abs/2609.25195)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| 座舱内部基准（134 cases）任务成功率 | **混合执行 91.04%** ／ 直接执行 72.39% ／ 全委托 80.60% |
| 匹配成功轮次下的平均任务执行延迟 | 混合执行较两种基线分别降低 **26.73%** 与 **30.91%** |
| 落地场景 | 桌面助手、智能座舱、语音客服 |
| 架构角色 | Frontend Agent（对话 + 工具调用/委托决策）／ Backend Agent（独立上下文执行）／ Orchestration Runtime（状态维护、请求授权、结果回传调度） |

### 主要创新点

- **前台-后台分离**：Frontend Agent 负责对话并**在"直接调用工具"与"委托给后台"之间做选择**；Backend Agent 在**独立上下文**中执行被委托的多步任务。Orchestration Runtime 维护任务状态、协调用户输入与授权请求、调度结果回传。
- **三个"解耦"是本报告的核心设计**（值得单独记）：① **语音打断 ≠ 任务取消**；② **执行完成 ≠ 结果送达**。二者分离后，**对话可在委托任务后台执行期间持续进行**。
- **量化了"混合执行"优于两个极端**：91.04% vs 72.39%（全直接）/ 80.60%（全委托），且延迟更低。即**直接工具调用适合即时操作，后台委托适合多步任务，二者互补**。
- 环境事件 + 持久记忆提供会话内与跨会话上下文；独立 adapter 支持接入不同前端模型、后台 agent 与客户端。

> **口径注**：座舱基准为**内部 134 cases**，无公开评测集，亦无第三方复现。这是"harness 层创新"的典型样本——**架构贡献而非模型能力贡献**，与 §6 的趋势判断直接相关。

---

## 4. 阶跃星辰 StepFun — StepAudio 3 Realtime 技术报告（★ 新收录）

- **中文标题**：StepAudio 3 Realtime：连续"听—说—思—行"循环的音频语言基础模型
- **英文标题**：StepAudio 3 Realtime Technical Report
- **发布机构**：阶跃星辰（StepFun）
- **模型名称/系列**：StepAudio 3 Realtime（StepAudio 3 家族）
- **发布日期**：**2026-09-10**（arXiv v1，**v2 = 2026-09-12**）
- **arXiv 链接**：[arXiv:2609.14005](https://arxiv.org/abs/2609.14005)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| StepAudioChat（推理模式 macro avg） | **73.0** |
| MMSU | **90.6** |
| Artificial Analysis Full-Duplex Bench | **98.9 Overall** |
| τ-Voice（macro 任务成功率） | **56.0%** |
| 核心机制 | **Think-While-Speaking**（私域推理与语音输出**并行执行**） |
| 同系列未收录兄弟篇 | StepAudio 3 Gen（2609.12945）、StepAudio 3 Music（2609.16034）——**同批未收录，供后续 digest 跟进** |

### 主要创新点

- **连续 listen-converse-think-act 循环**为组织主线，而非"语音输入 + 文本输出"的拼接式架构。
- **Deep Perception**：捕捉丰富声学线索以判别用户意图。
- **Seamless Duplex**：建模同步音频流，自然处理**停顿、backchannel（附和）、打断**三类实时对话难点。
- **Think-While-Speaking（本日最值得关注的一处）**：**在说出话的同时并行执行私有推理**，从而化解"深度思考 vs 低延迟"这一通常被当作零和权衡的矛盾。官方称开启该机制后，对话与推理表现**可比肩专用 reasoning model，同时保持实时说话**。
- 内置 **Voice Agent** 处理异步工具执行，**不打断对话流**（与 §3 的 Qwen-Audio-Agent "任务执行 vs 结果送达解耦"属同一设计家族，不同团队独立收敛）。

> **口径注**：Full-Duplex Bench 98.9 与 τ-Voice 56.0% 均为自报/第三方榜单混合口径，**τ-Voice 的 56% 与 MMSU 的 90.6 落差极大**，说明"全双工自然度"与"任务完成度"仍是两个未合并的能力轴，不可合成单一"语音模型能力"分。arXiv 摘要由作者列表给出但未列机构块。

---

## 5. 发布但未附技术报告/基准的事件（2 项）

### 5.1 美团 LongCat-2.5-Preview（2026-09-25/26，API 上线；09-30 二次报道）

- **中文标题**：美团 LongCat-2.5-Preview：1.6T MoE 原生多模态 Agent 模型，1M 上下文
- **英文标题**：Meituan Ships LongCat-2.5-Preview: 1.6T MoE Multimodal Agent Model With 1M Context
- **发布机构**：美团 LongCat
- **发布日期**：**2026-09-25**（API 平台 changelog `2026-09-25`；TechNode 报道 09-30；部分聚合站标 09-26）

| 项 | 值 | 来源与置信度 |
|---|---|---|
| 总参数 / 激活 | **1.6T / ~48B（MoE）** | Pandaily（二手）——**中**，架构沿用 LongCat-2.0 路径 |
| 上下文 | **原生 1M tokens** | 长猫官方 changelog + Pandaily + CloudPrice/Vercel Gateway——**高**（三方独立一致） |
| 最大输出 | **128K**（官方）/ 131K（第三方转录） | **低**，口径不一致 |
| 多模态 | **原生图像理解**（图像问答、摘要、视觉推理）入基座模型 | 官方 changelog——**高** |
| 定价 | 输入 **$0.30/M**、输出 **$1.20/M**、缓存读 **$0.006/M** | Vercel AI Gateway / CloudPrice——**高**；为**限时 Preview 价** |
| Agent 工具链 | Codex、OpenCode、OpenClaw、CatPaw、Claude Code、Hermes、Kilo Code | 官方文档转述——**中** |
| **基准分数** | **本轮官方未发布任何 benchmark** | **高**（多来源一致确认缺失） |

- **主要创新点**：相对 LongCat-2.0 的实质变化是**多模态能力下沉进基座模型**（此前为纯文本），以及定位从"agentic coding"扩展到**终端/浏览器/GUI/电子表格/设计工具**的自主操作链。
- **arXiv/论文链接**：**无**。官方仅有 API changelog（`longcat.chat/platform/docs/change-log`）与产品页。
- **⚠️ 口径注（重要）**：本条**所有能力性表述均为 positioning statement**，因官方本轮未出 scorecard。**不得据此对 LongCat-2.5-Preview 与 Gemini 4 Argon / Kimi K3 / GLM-5.3 做能力排序**。参数量来自二手报道（Pandaily），**未经官方技术报告确认**。

### 5.2 月之暗面 Kimi K3 进入 OpenAI 企业 Codex 渠道（2026-09-30）

- **性质**：**分发/商务事件，非模型发布、非技术报告**。
- **要点**：Kimi K3 经美国推理服务商 Baseten 进入 OpenAI 企业 Codex 渠道与计费体系，企业客户可用既有 OpenAI 采购额度消耗该中国开源模型（TechNode / 新浪财经）。新浪财经称这是**中国开源模型首次进入 OpenAI 企业计费系统**。
- **口径注**：同期另有"Kimi K3.1 标识符出现在月之暗面 API 注册表"的传闻（TechNode 转述），**属未证实线索，本 digest 不采信**。Kimi K3 本身的架构与参数（2.8T MoE / 104B 激活 / KDA + AttnRes / Stable LatentMoE 16-of-896 专家 / 1M 上下文 / 官方 tech report PDF 存于 `MoonshotAI/Kimi-K3` 仓库）已在既往 digest 收录，**此处不重复**。

---

## 6. 19 家目标机构状态复核表（截至 2026-10-03）

| 机构 | 最新状态（复核至 2026-10-03） | 本窗口（10-02→10-03）变化 |
|---|---|---|
| **OpenAI** | GPT-6.1 Sol Pro / Sol（09-29，DevDay 2026 25 项发布）；GPT-6 Sol / Luna（09-22）；Astra 6.1 因安全评估**取消发布**（09-28） | **无新增** |
| **Anthropic** | Claude Sonnet 5.5（09-28，比 Opus 5.5 快 30%）；Opus 5.5（09-22）；Fable 5.1 / Mythos 5.1（09-01）；第三方安全审查进行中 | **无新增** |
| **Google DeepMind** | **Gemini 4 Argon（09-30）**——1M 输入 / **1M 输出** token、DeepSWE v1.1 77.9%、AutomationBench 51.3%、CWE-bench v1 68%；Fairwind Program 限定访问。Gemini 3.5 Pro **已取消** | **无新增**（详见 10-01 digest） |
| **Meta AI（LLaMA / Muse）** | Muse for Small Business（09-29）；Muse Spark 1.3 / 1.3 Contributor（09-02）；Muse SEV-2 漏洞后加强安全警告（09-25） | **无新增** |
| **DeepSeek** | V4.1-Flash（09-10，552B MoE，Causal Encoder–Decoder，8B 输入/16B 输出激活，KV cache 降至 1/4 HBM、1/8 SSD）；V4-Pro 报告（04-26）；mHC 论文（01-01，架构信号）；与华为开源 **Ascend** 编程工具 + **128× Ascend 950** 超节点（10-01 报道） | **无新增技术报告**（Ascend 工具属基础设施开源） |
| **Mistral AI** | Medium 3.5（04-28）为最新有据可查版本；近期动态多为产品更新 | **无新增** |
| **Qwen（阿里）** | Qwen3.8-Max-0902（09-02）、Qwen3.8-Max Prime（09-23）、Qwen3.8-2.4T-A95B 开源（08-13，2.4T 总参/95B 激活/262K→1.01M）；**Qwen-Audio-Agent 报告（09-21）为本 digest 新收录** | **技术报告 +1** |
| **Yi（01.AI）** | 官方仓库最新大版本开源更新仍为 **Yi 1.5**（2024）；公开发布节奏显著慢于 DeepSeek/Qwen | **无新增** |
| **Baichuan** | 开源侧为 Baichuan-Omni-1.5（多模态理解）与医疗向 **Baichuan-M3-235B**（2026）；商业主模型 Baichuan4 / 4-Air / 4-Turbo（32K 上下文） | **无新增** |
| **Microsoft（Phi）** | Copilot 大改版（09-25，Code / Autopilot / 内嵌 Office / 成本可见性）——**产品层，无 Phi 新技术报告** | **无新增** |
| **Apple（Foundation Models）** | 年度技术报告仍**缺席**；无公开 frontier 模型报告 | **无新增** |
| **NVIDIA（Nemotron）** | Nemotron 3 Ultra 技术报告（550B 总参/55B 激活，hybrid Mamba–Transformer MoE，65 页）；Nemotron-TwoTower（2606.26493，扩散 LM + 冻结 AR context，2.42× 吞吐、保留 98.7% 质量）；**GR00T N1.7 one-step drifting action heads 报告（2609.18108，09-16）**；OpenShell / Sentry agent 遏制软件（09-28） | **无新增**（GR00T N1.7 已被本 wiki 收录） |
| **xAI（Grok）** | Grok 4.6（08-12）为官方最新；Grok 4.7 传闻**不采信**；Grok Voice Transcribe 2.0（09-18） | **无新增** |
| **Amazon（Nova）** | Amazon Ads Agent / DVA+ 平台重构（09-下旬）；Amazon 已要求从 Meta Muse 的 agent 列表中移除 | **无新增**（产品/商务层） |
| **Zhipu AI（GLM）** | GLM-5.3 Prime（09-23）；GLM-5.3（08-14，753B MoE / 40B 激活，与 5.2 **同底座**，增益全部来自 post-training 扩展）；CyberGym **84.5%**、ExploitBench 24.4→54.4%；因漏洞发现能力超预期，**权重发布推迟约两周以做安全评估** | **无新增** |
| **InternLM（上海 AI Lab）** | 公开侧以权重发布与工具链为主（xtuner、WildClawBench、Intern-S1）；**未见新的技术报告** | **无新增** |
| **Moonshot AI（Kimi）** | Kimi K3（07-16，2.8T/104B）；Kimi K3 进入 OpenAI Codex 企业渠道（09-30）；K3.1 标识符传闻**不采信** | **无新增报告**（分发事件 1 项，见 §5.2） |
| **StepFun（阶跃星辰）** | Step 5 Preview（开源倒计时页）；Step 3.7 Flash（196B MoE / 11B 激活 / 400 tok/s）；**StepAudio 3 Realtime 报告（2609.14005）为本 digest 新收录**，Gen / Music 两篇同批未收录 | **技术报告 +1** |
| **字节跳动（豆包 / Seed）** | Seed2.1（06-23，多模态与长上下文 MMLongBench-128K）；Seed Full-Duplex Speech LLM（04-09）；Seedance 2.0（02-13）；Seed3D 2.0（04-23）；**豆包个人助手 App 代号 "Spell"，2026-04 起内部测试（09-30 报道）**；实时 3D world model 传闻最早 2026-10 发布——**来源为匿名信源，明确标注"计划可能变更"，不采信为既定日程** | **无新增** |

**旁注（非目标机构但同期重要）**：蚂蚁集团 **Ling-3.1-flash（560B 参数）** 于 2026-09-30 发布（TechNode）。

---

## 7. 六个重点方向的横向归纳

| 方向 | 本窗口证据 | 判断 |
|---|---|---|
| **1. 新架构（MoE / Mamba / hybrid）** | 本窗口**零新增架构类技术报告**。近 30 天架构信号已全部入库：NVIDIA Nemotron 3 的 **hybrid Mamba–Transformer MoE**（+ NVFP4 原生 GEMM 预训练至 25T token）、Kimi K3 的 **KDA + AttnRes + Stable LatentMoE（16/896 专家）**、DeepSeek **mHC（Manifold-Constrained Hyper-Connections）**、GLM-5 采用 **DeepSeek Sparse Attention** | 架构创新节奏自 8 月起放缓；**竞争焦点已从"提出新算子/新混合"转向"把既有算子压到更低精度与更高吞吐"**（NVFP4、MXFP4/MXFP8 QAT 是本期最明确的证据） |
| **2. 训练方法（pre / post / alignment / RL）** | 本窗口新增两处 **post-training-only scaling** 证据：① **GLM-5.3 与 GLM-5.2 同底座，全部增益来自 post-training 扩展**（自建 Code Bench +50%）；② **LongCat-DeepResearch 的 workflow 直接复用为 LongCat 的 mid-train / post-train 数据引擎**。Mix-RL（Xiaomi-OCR-0）则是 SFT→RL 混合任务化的具体实现 | **"post-training 作为独立 scaling 轴"已被至少两家中国机构在 2026-09 各自独立验证**，这是本日最值得记入 [[claims]] 的结论（目前 2 源，置信度**中等**） |
| **3. Scaling Law / 缩放分析** | 本窗口**无新的 scaling law 论文**。可用坐标：Kimi K3 报告相对 K2 有 **~2.5× 整体 scaling 效率提升**（架构 + 训练方法 + 数据配比共同贡献，**三者未解耦**）；NVIDIA 观察到 **MoE hybrid 的 context extension 能力优于 dense hybrid**（Nemotron 2 Nano 对比） | **归因缺口**：厂商报告的"scaling 效率提升"几乎都是**架构/数据/训练方法三项的合量**，缺消融即无法归因。任何引用此类数字时必须保留"合量"标注 |
| **4. 多模态模型** | 本窗口新增 3 条：LongCat-2.5-Preview（图像理解**下沉进基座** 1.6T MoE）、Xiaomi-OCR-0（0.8B 专用 OCR-VLM，170M 样本）、Qwen-Audio-Agent（全双工语音+视觉的 harness 层） | **多模态出现明显分层**：基座内置（LongCat 2.5、Qwen3.8-Max）／ 专用小模型（Xiaomi-OCR-0，0.8B 打 96.83 OmniDocBench）／ harness 编排（Qwen-Audio-Agent）。**专用小模型路线在文档任务上未被基座模型吞掉** |
| **5. 长上下文模型** | **1M tokens 已完全商品化**，本窗口无任何机构再把它当作卖点：Gemini 4 Argon（1M 输入 / 1M 输出）、Kimi K3（1M）、LongCat-2.5-Preview（1M）、Qwen3.8-Max（默认 1M，2.4T-A95B 原生 262K 可扩至 1.01M）、DeepSeek V4.1-Flash（1M）、GLM-5.3（1M） | **1M 上下文的边际价值正在归零**。区分度已转移到**输出上限**（Argon 1M 输出是本期唯一实质差异）与**压缩率**（V4.1-Flash：KV cache 降至 1/4 HBM、1/8 SSD）。长上下文的下一个战场是 **KV cache 成本**，不是窗口数字 |
| **6. 推理模型 / reasoning model** | 本窗口唯一新推理机制是 **Think-While-Speaking（StepAudio 3）**：**推理与语音输出并行**，而非串行（先想后说）。另有两项产品层证据：GLM-5.3 **强制 thinking** 并暴露 low/high/max 三档 effort；Qwen-Audio-Agent 的**混合执行**优于全直接与全委托 | **reasoning effort 显式分档（low/high/max）成为标准接口**（GLM-5.3）。**推理与生成并行化**（而非延长推理链）是一个新方向——把"思考时间"从延迟预算中移出 |

---

## 8. 本日空白与负向发现（明确记录，不以邻近内容填充）

- **19/19 目标机构在 10-02→10-03 窗口内零新增 frontier 技术报告**。arXiv 最近的相关公告批次止于 **2026-09-30**，无 10-01/10-02 新批次。这是**日历性静默（10-03 为周六）**，**不构成"前沿发布停滞"的证据**。
- **无新的 System Card**。OpenAI（GPT-6.1 Sol Addendum, 09-29）与 Google（Gemini 4 Argon）均为博客/评测方法页披露，**独立 System Card PDF 缺位**的状态延续。
- **无新的 Scaling Law 论文**（窗口内）。
- **无新的 MoE 路由/负载均衡方法论文**（窗口内）。
- **无任何目标机构的**已发布模型附带**技术复现（independent replication）**。本期 4 篇新收录报告**全部为单一团队自报**，0 篇有第三方复现。
- **长上下文（1M）已无差异化**，但**尚无公开的"1M 上下文下的真实生产退化曲线"**——所有 1M 声明均为厂商自报，无第三方 needle-in-haystack 之外的端到端长程任务评测。
- **LongCat-2.5-Preview 本轮无 benchmark**，其能力定位不可验证（见 §5.1 口径注）。
- **未采信线索（明确列出以免后续误引）**：Kimi K3.1 标识符传闻；字节跳动实时 3D world model 的"2026-10 发布"时间表（匿名信源 + "计划可能变更"）；Grok 4.7 传闻；GLM-5 的"超出 Gemini 3 Pro"（公司自报且同时承认全面落后 Claude）。

---

## 9. 本次检索方法与局限（自评）

- **检索路径**：① arXiv API 按 `ti:"Technical Report"` / `ti:"report" AND cat:cs.CL` / `abs:"system card"` 按 `submittedDate` 倒序全量扫描（arXiv API 本次**可用**，未复现 10-01 game-rl digest 记录的 429 限流）；② 逐机构 web 检索（DeepSeek、Qwen、Zhipu、Moonshot、StepFun、ByteDance/Seed、NVIDIA、OpenAI/Anthropic/Meta、Yi/Baichuan/InternLM/MiniMax）；③ 二手报道交叉核验（TechNode、MarketingProfs AI Update 10-02、releasebot、lmmarketcap、CloudPrice/Vercel Gateway、cloudprice 规格表）。
- **去重**：4 篇新收录 arXiv ID 在写入前经 `grep -rl` 全 `wiki/` 核验，命中数均为 **0**；另有 6 篇同期技术报告（2609.27284 Hunyuan-A13B、2609.26375 KwaiMind、2609.18310 GR00T N1.7、2609.00791 Instella-MoE、2609.12945 StepAudio 3 Gen、2609.16034 StepAudio 3 Music）**已在库，交叉引用不重复收录**。
- **affiliation 纪律**：arXiv **不暴露机构字段**。本 digest 4 篇新报告中，**LongCat-DeepResearch 由作者块 "Meituan LongCat Team" 显式标注（可验证）**；**Qwen-Audio-Agent、StepAudio 3 Realtime、Xiaomi-OCR-0 三篇的作者块未列机构**，其机构归属依据 arXiv 题名的自标前缀（Qwen / StepAudio / Xiaomi），**已逐条在上文标注为未经机构块独立验证**。未从任何作者姓氏推断机构。
- **局限**：① 10-02/10-03 为静默窗口，公开 web 索引截至 10-01/10-02，**10-03 当日信息可能尚未被索引**；② LongCat-2.5-Preview 的 1.6T/48B 参数为**二手报道**，未经官方报告确认；③ 各家 benchmark 分数来自各自不同评测口径与时间点，**本 digest 的分数表格不可横向直接比较**，仅在同一报告内部有效。
- **无第三方复现**。本页所有数字均为发布方自报。

*Generated 2026-10-03（覆盖 2026-10-02 新闻窗口，arXiv 技术报告补扫至 2026-10-03）。*