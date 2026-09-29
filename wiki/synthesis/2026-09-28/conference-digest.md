---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 + Fresh arXiv — 2026-09-28"
type: synthesis
created: 2026-09-28
updated: 2026-09-28
sources: [conference-web-searches, arxiv-api, recsys-acm-contributions, aaai-awards, www2026-accepted, neurips-2026-arxiv-comments]
tags: [conference-digest, NeurIPS2026, RecSys2026, KDD2026, ICML2026, ACL2026, CVPR2026, EMNLP2026, EMNLP2025, CIKM2025, SIGIR2026, AAAI2026, WWW2026, ICLR2026, recommendation, generative-recommendation, advertising, CTR, LLM, agents, agentic-eval, agent-economics, speech, code-execution, code-agents, causal-reasoning, multimodal, generative-models, video-world-model, flow-matching, MoE, time-series, benchmarks, evaluation-validity, jailbreak, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-09-28

> ## ⚠️ 窗口口径更正（本轮最重要的一条）
>
> 抓取时 8 个 category 的 `/list/{cat}/new` 仍显示 `Friday, 25 September 2026`，最初据此判定"窗口停滞"。**该判定是错的**，今日 sibling（[`arxiv-paper-check`](arxiv-paper-check.md)）已同日更正，本文采纳：**`/list` 页面与 `cat:` 限定的 API 查询都不足以界定全局窗口**。cs.AI / cs.LG 当时只是**没有新的 primary submission**，其 listing 页面因此停留在上一批。
>
> **本文的实际窗口**：改用**跨 26 个 category 的 category-agnostic API 扫描**（`sortBy=submittedDate&sortOrder=descending`），得到 **638 篇唯一新论文，ID 区间 `2609.30379–2609.31620`**，全部 `published` 落在 2026-09-25/26（构成 09-28 周一公告）。对照：早前的同类扫描（今日 `arxiv-daily` 的 25 类 tail sweep）只到 `2609.31371`。
>
> **Dedup**：638 篇对照全库 **6,244 个 arXiv ID** 正则扫描 → **499 篇未被收录** → 主题筛选 → **§2 的 26 篇 + §3 的 14 篇 = 40 篇**，写稿时全部 whole-`wiki/` grep 0 hits。§3 取自 Fri-25 窗口（IDs ≤ 2609.30266），与今日 5 个 sibling 在该窗口的声称集互斥（`arxiv-ai-search` 22 篇 / `game-rl-daily` 29 篇 / `arxiv-daily` 40 篇）；§2 取自 09-28 新窗口。
>
> **⚠️ 写稿后复核（本文自查，发现 1 处 feature 级重叠）**：两个 sibling 在本轮稍后又落地了 RUN 2，声称范围与 §2 的窗口重叠。逐 ID 复核结果：**40 篇中 39 篇独家，1 篇共享**——**2609.31381**（*Completed Pairs Hide Capped Failures*）被 `arxiv-paper-check` RUN 2 同时收录，**双方结论一致、无数据冲突**，已在 §2.7 加碰撞标注（首发方为 `arxiv-paper-check`）。另有 4 篇（2609.29045 / 2609.29875 / 2609.31430 / 2609.29652）**仅作跨文引用**，从未被本文声称为独家。
>
> **本轮头条**：**NeurIPS 2026 的 accepted list 首次通过 arXiv comments 大规模显形**（§1.1），这一项在 09-16 与 09-25 两轮 digest 中都是 `unresolved`。

---

## 1. 会议扫描 — Venue-by-Venue（2025–2026）

### 1.1 NeurIPS 2026 ★ 本轮头条 — accepted list 显形

NeurIPS 2026 的正式通知日约在 **2026-09-24**（09-25 digest 记录），今日 arXiv 上开始出现**成批的 `Accepted at NeurIPS 2026` comment**。本轮在 499 篇未收录论文中检出 **20 篇带 NeurIPS 2026 标注**（含 1 篇 poster、1 篇 oral、2 篇明确写出 "Track on Evaluations and Datasets"），其中 12 篇与本库主题相关，已在 §2 展开：

| ID | 标题 | 标注 | § |
|---|---|---|---|
| 2609.31071 | Externalized CPDAG Summaries Improve LLM Causal Deduction | NeurIPS 2026 | 2.1 ★★ |
| 2609.31354 | Mutable Transcripts: Mitigating Context Pollution through Editable Conversation State | NeurIPS 2026 | 2.1 ★★ |
| 2609.31468 | PriceBench: Price/Quality/Brand Preferences in LLM Booking Agents | **EMNLP 2026 Industry Track** | 2.2 ★★ |
| 2609.30952 | MVVBench: Benchmarking 4D Reasoning in Vision-Language Models | NeurIPS 2026（23 pages） | 2.2 |
| 2609.31507 | SatNav: Long-Horizon UAV VLN from Satellite Imagery | NeurIPS 2026, **Evals & Datasets**（32 pages） | 2.2 |
| 2609.31140 | Can Linguistic Reasoning Vectors Enhance Multimodal Reasoning Ability? | NeurIPS 2026 | 2.3 |
| 2609.30517 | Seeing Speech: Visible Articulatory Dynamics for 3D Facial Animation | NeurIPS 2026 | 2.3 |
| 2609.31193 | Who Says What: Symbolic Trimodal Binding in Audio-Visual LLMs | NeurIPS 2026 | 2.3 |
| 2609.30997 | Can Pixels Alone Reveal Image Origin? | NeurIPS 2026（29 pages） | 2.4 |
| 2609.30982 | FARE: Catching Bait-and-Switch Image Generators | NeurIPS 2026 | 2.4 |
| 2609.30478 | The Shape of Events: Edge-Based Inductive Biases via Cross-Domain Distillation | NeurIPS 2026 | 2.4 |
| 2609.30682 | SGMA: Structure-Guided Masked Autoencoders | NeurIPS 2026（22 pages） | 2.4 |
| 2609.31458 | Nonparametric ICL under Growing Geometric Complexity | NeurIPS 2026（63 pages） | runner-up |
| 2609.30556 | Dynamic Regret in OCO with Indicator Switching Costs | NeurIPS 2026 | runner-up |
| 2609.31066 | Modeling quantum neural network gradient with RL | NeurIPS 2026 Main (Poster) | — |
| 2609.31107 / 31128 / 31470 / 31559 / 31204 | BO with Fisher Information Geometry / structure-aware attack / Sinkhorn OT / latent Bayesian tracking / FlatClip fMRI | NeurIPS 2026 | — |

> **`unresolved`**：本轮**未取得 NeurIPS 2026 官方 award 名单**。上述 20 篇是**按 arXiv comment 抽取的 accepted 论文子集，不等于完整 accepted list**，也不是获奖论文。获奖公告按历年节奏通常在会议开幕前后，需下一轮核 `neurips.cc` 官方页。

**NeurIPS 2025**（已结束）：Gated Attention（2505.06708，Best Paper）、1000 Layer Networks for Self-Supervised RL（Best Paper）、VAGEN 等 ⚠️ 均已在库。

### 1.2 RecSys 2026（Minneapolis）★ proceedings 已于 09-27 上线

**本轮第二个实质 venue 事件**：`RecSys '26: Proceedings of the 20th ACM Conference on Recommender Systems` 于 **2026-09-27** 正式出版（ACM DL，DOI 前缀 `10.1145/3773078`）。规模：**1,424 投稿 / 279 接收 = 20%**。会议 **2026-09-28 → 10-02**（即今日开幕）。

> ⚠️ **日期口径冲突**：官方 contributions 页为 09-28 → 10-02；本库 09-25 conference-digest 记为 09-29 → 10-01。**以官方页为准**，09-25 记录应修订。本轮未能直接抓取日程页二次确认。

**Netflix Research（重点机构）— 唯一进入 ACM DL 的单篇重点机构论文**

- **Towards Generalizable and Efficient Large-Scale Generative Recommenders**｜面向大规模生成式推荐器的泛化性与效率
- 作者：Qiuling Xu, Ko-Jen Hsiao, Moumita Bhattacharya（**Netflix Research**, Los Gatos；netflix.com 官方邮箱）
- Venue：RecSys '26，DOI `10.1145/3773078.3831905`；arXiv:2605.23312（v1 05-22，v2 08-06）
- 链接：[arXiv:2605.23312](https://arxiv.org/abs/2605.23312) ｜ [ACM DL](https://dl.acm.org/doi/10.1145/3773078.3831905)
- 状态：⚠️ **论文本体已在库**（`wiki/papers/recommendation/netflix-generative-recommender-scaling.md`，另见 05-25 arxiv-daily、06-04 / 08-16 conference-digest）。**本条新增的只是 venue 事件**：DOI 落地 + 出版日期。

核心主张（保留原文）：
- **Scaling**：backbone **2M → 1B** 参数（**不含 embedding 与 decoding 层**），production-scale title recommendation。
- **任务依赖的 scaling 行为**：部分下游任务在观测尺度内已逼近 **empirical ceiling**，另一些持续受益于容量 → 主张用 **offset scaling-law fits 作为诊断工具**判断追加 scale 在何处更有用。
- **Production 约束三件套**：**multi-token prediction** 对齐 serving latency；**sampled softmax + projected decoding head** 降低数万亿 behavior token 反复重训的成本；**semantic item towers + collaborative-embedding masking** 处理 cold-start（新作上线时 collaborative ID embedding 不可靠，先用 semantic metadata 打分）。
- **结果**：**1M 用户、一周 production-shadow 评测**中，1B-backbone 在**所有报告任务上 MRR 均高于** 2M baseline。
- 与 09-22 的 IntBMoE（UVCTR +2.4%）、2609.23718（Baidu +0.96% watch duration）构成 generative rec 生产化证据链的第三个独立点：**下一阶段瓶颈是 decoding / serving 经济学与 cold-start，而非 backbone 规模**。

**RecSys'26 其他新接收**（来自官方 contributions 页）：**SCRec**（跨阶段解耦 semantic 与 collaborative signal，⚠️ 已在库 09-16）、**Coarse-to-Fine Long-term Interest Modeling for Generative Recommendation**（含 Ruiming Tang / Han Li / Kun Gai，`tentative` 未验证收录）、**DP-Rec**（标题在官方页被截断，仅记录存在性）。

### 1.3 KDD 2026（Jeju）— Meta 三个奖项（二手来源，`tentative`）

官方获奖名单页本轮未能抓取，以下来自 LinkedIn 获奖公告的搜索摘要，`tentative` 级别：

- **Best Paper – ADS Track**：*Multi-modal Multi-turn Comprehensive RAG Benchmark*（Meta）
- **Best Paper – Advertising Science Track**：*McGrad: Multicalibration at Web Scale*（Meta）— 标题全库 0 hits（低置信，可能存在转写差异）
- **Best Student Paper**：*SCOPE: Cost-Efficient Model Selection for Compound AI Systems under Quality Constraints*

⚠️ KDD'26 的 HOBA（2607.24779，线上 target cost +3.6%）已在 09-25 digest 做过 venue 确认。

### 1.4 ICML 2026

**23,918 valid / 6,352 accepted = 26.6%；168 orals**；**Test of Time = A3C**（[官方 blog](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/)）。*The Flexibility Trap*（2601.15165，JustGRPO，GSM8K 89.1%）、*High-Accuracy Sampling for Diffusion Models*、A3C 及多篇 honorable mention **均已在库**。本轮无新增论文，但 **§2.5 的 dLLM jailbreak 能量景观分析（2609.30841）与 Flexibility Trap 构成同一议题的两面**——一篇说任意顺序限制推理，一篇说能量势垒是 jailbreak 的统一成因。

### 1.5 ACL 2026

**12,148 投稿（同比 +45%）/ 4,462 接收；3 Best Paper + 18 Outstanding Paper**。已收录 Best Papers：*The Imperfective Paradox in LLMs*、*Memory Efficiency and Resource-Rational Encoding in Sentence Processing*。

⚠️ **未解条目**（`tentative`）：*CURE*、*PolyGloss*、*PALU* 三项的完整标题为**自拟展开**，未经官方 proceedings 确认，**不得作为正式标题引用**。

### 1.6 CVPR 2026 / EMNLP 2025 / EMNLP 2026

- **CVPR 2026**：16,092 投稿 / 4,089 接收；评审侧 **25,149 reviewers**，其中 **1,545 outstanding reviewers**（`tentative`）。Best Papers（D4RT、Native Compact Structured Latents）及 NitroGen / SAM 3D / ChordEdit / Molmo2 / VS-Bench / CubiD **均已在库**。
- **EMNLP 2025**：**1,810 main / 1,406 Findings / 194 Industry Track / 78 demos**；Best Paper *Infini-gram mini* ⚠️ 已在库。
- **EMNLP 2026**：本轮新增确认的 venue-tagged 论文为 **PriceBench（Industry Track，§2.2）**，另有 WiNLP workshop（2609.30402）、BabyLM workshop（2609.30535）、DocInsights（2609.31341 / 31403）三篇 workshop 论文。

### 1.7 CIKM 2025 / 2026

CIKM 2025 奖项扫描完成，主要条目 **已在库**。*Data-centric Prompt Tuning for Dynamic Graphs* **两轮扫描均未能在官方页面定位**，`unresolved`，不收录。CIKM'26 FAE + REAL（2609.08943）已在 09-16 收录。

### 1.8 SIGIR 2026（Melbourne）— Best Paper 仍 unresolved

- **Test of Time** ⚠️ 已在库。
- **Best Paper 2026 未解**：官方 `sigir.org/awards/best-paper-awards/` 年度表格**仍止于 2025**。09-16 digest 记录的 "SPLADE/BM25 语义相关图推理" 说法**未获官方验证**，保持 `tentative`，不升级为 claim。

### 1.9 AAAI 2026 / WWW 2026 / ICLR 2026 — 全覆盖，零新增（负向发现）

完整 sweep 后**全部条目已在库**，记录于此以免重复劳动：

| 会议 | 核验条目 | 库内状态 |
|---|---|---|
| AAAI 2026 Outstanding (Main, 5) | Model Change for Description Logic；Causal Structure Learning (CADYT)；ReconVLA；High-Pass Matters；LLM2CLIP | ⚠️ 5/5 已在库 |
| AAAI 2026 Outstanding (AISI, 2) | PlantTraitNet；Generalizable Slum Detection | ⚠️ 2/2 已在库（"Science Data" 标题 0 hits 但作者列表被官方页截断，判 `unresolved`） |
| AAAI 2026 Classic | Learning Structured Embeddings of Knowledge Bases (Bordes/Weston/Collobert/Bengio) | 需补 grep |
| WWW 2026 Best Paper | From Retrieval to Generation（MedRGAG，Lei Li 等） | ⚠️ 已在库（08-17 / 08-05） |
| WWW 2026 Best Short | DualGR | ⚠️ 已在库（07-23 / 06-13） |
| WWW 2026 Seoul ToT | LINE（Jian Tang 等，2015，7,100+ citations） | 需补 grep |
| WWW 2026 规模 | 3,370 投稿 / 676 接收 = 20%（仅 10 条 research track） | 新增数字 |
| ICLR 2026 | ReTool；Kimi-Dev（60.4% SWE-bench Verified）；CodeGym；DreamGym；AgentFlow；VisCoder2；MoE-vs-Dense（2506.12119） | ⚠️ 全部已在库 |

---

## 2. 09-28 新鲜窗口精选（19 篇深读 + §2.9 的 7 条简述 = 26 篇）

### 2.1 因果推理与对话状态 — 本轮方法论信号最强的两篇

#### Externalized CPDAG Summaries Improve LLM Causal Deduction
**外化的 CPDAG 摘要提升 LLM 因果推断**

- 作者：Wentao Sun, João Paulo Nogueira, Dominique Verchere, Mathieu Acher, Alonso Silva
- **Venue：NeurIPS 2026**（18 pages, 2 figures）
- 链接：[arXiv:2609.31071](https://arxiv.org/abs/2609.31071)

**问题**：**Corr2Cause** 问的是"某个因果 claim 是否在所有与观测相关及条件独立相容的 DAG 中都成立"。作者把它重构为 **latent-object reasoning**——标签由一个 **CPDAG 查询**定义，但自由形式的 CoT 常常把 **Markov 等价类问题塌缩成局部模式匹配**。

**方法**：**Structured Thinking**，两轮 pipeline：先把潜对象**外化为有类型、受 schema 约束的 CPDAG 摘要**，再针对该 graph state 作答。

**结果（Qwen3.5-27B，Corr2Cause full test）**

| 条件 | F1(Yes) | 备注 |
|---|---|---|
| 强 PC-instruction baseline | **73.0** | 主配对 run 的对照 |
| **Structured Thinking** | **86.4** | **+13.4 pp**；McNemar `p = 2.4×10⁻⁶`；bootstrap 95% CI [+8.4, +18.6] |
| 三个 full-ID seed 的均值增益 | **+8.1 ± 5.3 pp** | 报告了 seed 方差 |
| **PC-scaffolded 两轮 prose control** | **67.6** | **关键对照**：详细 PC 脚手架 + 无 schema 的散文中间体**不够** |
| 打乱输出的 CPDAG | **−12.0 pp** | 因果性证据 |
| full-split 审计 vs 参考 CPDAG | ID skeleton F1 **0.960**；exact match **75.9%** | 逐题审计 |

同一模式在 **Qwen3.6-27B、Paraphrase-OOD、GPT-5.4-mini** 上成立。

**为什么本轮排第一**：这是"**把定义标签的潜对象外化出来、约束其形式、再检验下游答案是否真的用了它**"的一个极干净范例（`high confidence`）。三个数字合起来构成完整论证链：+13.4pp 有效、**67.6 的 PC-prose 对照排除了"只要给脚手架"这一平凡解释**、−12.0pp 打乱实验提供因果性。

**与本库关系**：09-25 收录的 *2805.16564 Fellowship of the Query*（用 teacher trace 训 next-action controller，macro-F1 0.1736 → 0.6536）与本篇是同一命题的两种实现——**控制器可以是可学习的 action 分类器，也可以是强制 schema 的结构化状态**。另与 09-22 的 *Total Cost of Agency*（memory-injection 归因）同源于"agent 推理过程不可信"这一判断。`high confidence`

#### Mutable Transcripts: Mitigating Context Pollution through Editable Conversation State
**可变 transcript：用可编辑的对话状态缓解 context 污染**

- 作者：Dan Barry, Andrew Hines
- **Venue：NeurIPS 2026**
- 链接：[arXiv:2609.31354](https://arxiv.org/abs/2609.31354)

**问题**：当代 LLM 对话系统把 conversation history 当作**定义模型工作 context 的不可变 turn 序列**。但真实交互中用户意图是**动态的**——会纠正、细化、改变约束。二者的错配造成 **context pollution**：过时或无关的信息持续存在并继续影响后续回复。

**方法**：**mutable transcripts**——一种新的交互范式，允许用户通过**自然语言 edit 请求修订此前的 turn**，使 history 本身被**更新而非追加**。作者明确把这表述为一次**范式转换**：transcript 从被动记录变为**对话状态的可编辑表示**。给出一个集成进标准 chat 界面的工作原型。

**评估（诚实的小规模证据）**：受控用户研究 **n = 17** + 代表性交互场景的 transcript 分析。参与者在 clarity、confidence、ease of use 三个维度**显著更偏好** mutable transcripts，且**重启对话的意愿下降**；transcript 分析显示它能**缩短对话长度并消除过时保留的 context**。

**⚠️ 强度限定（`single-source`，n=17）**：这是本轮**样本量最小、结论最需谨慎**的一篇。作者自己在摘要中使用了 "initial evidence" 的措辞。它与今日 sibling 收录的 *ICLR*（2609.29875，agent reasoning 压缩，reward 0.699→0.718，token −25.5%/−14.4%/−33.3%）构成一对**互补而非竞争**的方案：ICLR 从**模型侧**自动删减 reasoning，Mutable Transcripts 从**用户侧**让 context 本身可修订。两条线指向同一诊断——**context 不是只读的**。

### 2.2 评测基准 — 含本轮唯一的"agent 即消费者"诊断

#### PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences in LLM Booking Agents
**PriceBench：LLM 订房 agent 中价格 / 质量 / 品牌偏好的诊断基准**

- 作者：Pavel Kireyev（单作者）
- **Venue：EMNLP 2026 Industry Track**（19 pages, 10 figures, 6 tables；code + data 已开源）
- 链接：[arXiv:2609.31468](https://arxiv.org/abs/2609.31468)

**动机（本轮最锋利的问题设定）**：LLM 越来越多地充当**采购 agent**——这意味着**做出选择的是 LLM 而不是用户**，它的偏好**悄悄决定了买什么、付多少**。酒店预订是一个干净实例：高频选择、落在少数可比属性上，而**选择本身就暴露偏好**。

**方法**：用 **logit choice model** 从订房选择中**反解** LLM 的价格 / 质量 / 品牌偏好；**28 个 LLM / 8 家 provider / 3,600 个酒店任务 / 179 处真实纽约房产**。

**结果**

| 发现 | 数值 / 表述 |
|---|---|
| **能力 ↔ 选择的一致性，而非选择的内容** | 更强的 LLM 持有**更强、更一致**的偏好；更弱的要么锁死在单一立场（**可被控制 listing 顺序者利用**），要么几乎无差别地选 |
| 价格敏感度跨模型差异 | **跨度超过一个数量级** |
| 价格 / 质量权衡的后果 | 在**完全相同的任务**上，把平均每晚房价从 **$247 推到 $393** |
| 供应商内部差异 | 同一家族内偏好差异也很大 |

**结论（作者原话方向）**：agent 买了什么**必须按 LLM 逐个测量，不能推断**；作者开源了任务、代码与**全部 28 组 response**。

**为什么本轮重要（`high confidence`）**：这是**本轮 638 篇里唯一一篇把"LLM 作为推荐/采购决策者"当作被测量对象**的论文，也是**若干连续窗口无直接 CTR/rec 建模论文之后最接近 rec 语义的新工作**（⚠️ 该"连续无 CTR"表述今日已被两个 sibling 各自证伪并撤回——真正的窗口级空缺只在**广告竞价 / bidding**，见 §Data Quality 3）。它与本库 rec 线的连接点非常直接：**一个 CTR 模型的"用户偏好"从来不是用户的偏好，而是**「展示位置 × 模型偏差」的合成；PriceBench 用 logit choice model 做的正是把模型偏好从选择中**解耦出来**这一动作——**这是一个可直接迁移到 rec/CTR 归因分析的方法论**。

#### MVVBench: Benchmarking 4D Reasoning in Vision-Language Models
**MVVBench：VLM 的 4D 推理基准**

- 作者：Hyungjin Chung, Byeongjun Park, Joonseok Lee, Hojun Kim, Jaeho Choi, Byung-Hoon Kim
- **Venue：NeurIPS 2026**（23 pages, 8 figures）
- 链接：[arXiv:2609.30952](https://arxiv.org/abs/2609.30952)

**构造要点（方法论上比普通 benchmark 更严）**：多视角视频理解需要跨**多个常不重叠**的相机流整合时空证据——跨视角追踪实体、跨时间对齐事件、推理潜在 4D 连续性。MVVBench 的每个问题都被**策展为在 view 与 temporal 两个轴上都单目歧义**：在指定输入集内**任何单一视角都答不出**，且**大多数连任何单一时刻都答不出**，只有跨视角且跨时间联合推理才唯一可解。覆盖隐式/显式属性识别、隐式/显式相对距离、相对相机位姿、组合计数四类共 **6 项能力**，人工撰写 QA + 严格验证。

**分析贡献**：刻画当前 VLM 何时/为何成功或失败，归因为 **temporal mis-localization、cross-view identity break、brittle multi-hop reasoning**；并给出 inference-time elicitation（task-specific CoT scaffold + 结构化跨视角证据聚合）**无需重训**即获显著增益。

**与本库关系**：这是本库 world-model / VLA 簇（09-22 的 NeuIDO 4D dynamics、09-25 的 NeuIDO 与 RobotEQ-Video）的**评测侧**对应物；"单视角可答性问题必须被系统性排除"这个策展纪律值得直接借用。

#### SatNav: Long-Horizon UAV Vision-Language Navigation from Satellite Imagery
**SatNav：从卫星影像出发的长时程 UAV 视觉-语言导航基准**

- 作者：Jiajun Jiang, Chunliang Hua, Zichun Chen, Yanxing Wu, Zeyuan Yang, Jie Song, Xiao Hu
- **Venue：NeurIPS 2026，Evaluations and Datasets track**（32 pages, 16 figures）
- 链接：[arXiv:2609.31507](https://arxiv.org/abs/2609.31507)

**动机**：城市级 UAV VLN 需要 agent 跨延展城市空间遵循指令，天然要求**长时记忆与地理 grounding**；但现有基准依赖**昂贵的重建 3D 资产**，限制了地理多样性与 episode 规模。

**构造**：用**高分辨率卫星影像**构建，以卫星 crop 近似 UAV 下视观测；自动化 cue-to-episode 管线产出 **118K episodes / 59 scenes / 18 cities，平均轨迹长度 379 m**。三个任务族：**Boundary**（环路进度追踪）、**Landmark**（地标空间 grounding）、**Route**（带计数提示的路线跟随）。

**结果与贡献**：对经典 VLN agent 与基于 LVLM 的近期 agent 评测，**城市尺度导航仍然困难**；提出模块化框架 **SwiftVLN**（可切换记忆组件）并做系统记忆设计 ablation；**satellite-to-UAV 迁移实验**表明卫星训练的导航模型可直接在**真实飞行 UAV 观测**上运行。

**为什么值得记**：**118K episode 规模 + 免 3D 重建**是本轮 benchmark 设计的最大工程增量，路径与本库反复记录的"benchmark 可扩展性"议题（09-25 的 *Component Benchmark*、*RecToolBench*）同源；"用廉价代理观测换规模"这一手法与 Netflix 的 semantic metadata cold-start 属同一思路。

### 2.3 多模态推理：被污染的能力可以从基座取回

#### Can Linguistic Reasoning Vectors Enhance Multimodal Reasoning Ability?
**语言侧推理向量能增强多模态推理能力吗？**

- 作者：Ziyi Wang, Li Li, Aolin Zhou, Yankun Shen, Chonghan Liu, Shuxia Lin, Xu Yang
- **Venue：NeurIPS 2026**
- 链接：[arXiv:2609.31140](https://arxiv.org/abs/2609.31140)

**问题（诊断部分比方法部分更重要）**：多数 VLM 由预训练 LLM 加上视觉模块与多模态对齐构成，但**这种 multimodal scaling 常常退化掉基座 LLM 原有的语言侧推理能力**。关键观察是：**基座 LLM 在 scaling 之后仍保有可用的推理，但对齐后的 VLM 自己无法可靠地访问它**。

**方法**：**LIFT**（Language-side reasonIng Facilitation and Transfer）——轻量向量干预，**不重训 backbone**。把 **Reasoning Vectors** 定义为"带显式 reasoning trace 的 Reasoner 路径"与"不带 trace 的 Solver 路径"之间 **answer-token 的 hidden-state 差**，注入目标 VLM 的**语言侧激活**；并支持可学习的向量适配而保持 VLM backbone 冻结。

**结果**：跨 **2 个 VLM × 6 个推理 benchmark**，在匹配协议下比较"从基座 LLM 提取"与"从对齐后 VLM 提取"两类向量——**LLM-derived 向量一致优于 VLM-derived 向量**，证实**基座 LLM 是恢复推理能力的更有效来源**；LIFT 通过轻量语言侧干预**部分**恢复了被退化的推理。

**与本库关系**：与 09-15 收录的 *latent-to-language transition gap*（2609.21662，steering latent CoT 无法迁移到语言生成）**互为镜像**——那篇说"从 latent 侧推不动语言侧"，本篇说"从语言侧（基座）可以推回 VLM"。两篇合起来把"multimodal scaling 丢失推理"这件事的**方向性**确定了下来：损失是**可逆的**，但必须从**正确的源**（基座而非 VLM）取向量。`high confidence`（方向），`tentative`（具体幅度，摘要未给数字）

#### Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs
**谁说了什么：音频-视觉 LLM 中的符号化三模态绑定机制**

- 作者：Jihoo Jung, Youngjoon Jang, Joon Son Chung
- **Venue：NeurIPS 2026**
- 链接：[arXiv:2609.31193](https://arxiv.org/abs/2609.31193)

**问题**：当前 AVLLM 在**多说话人对话**视频上的推理能力弱，而"谁说了什么"需要 **trimodal（文本-音频-视觉）绑定**。

**机制发现**：作者识别出 AVLLM 中**涌现的符号化三模态绑定机制**——模型把音频与视觉分量编码为**模态专用的符号变量**（分别捕捉**时间上的话语序列**与**空间上的实体坐标**），在这个抽象空间里建立跨模态链接。**关键发现：绑定失败时，主因是错配的 audio-visual 连接**。

**干预（几乎零成本）**：引入利用现成 **Active Speaker Detection（ASD）**模型的 audio-visual prompting——**仅把视觉 bounding box 叠加到 active speaker 上**，这一 **training-free** 方法在**四个对话中心 benchmark** 上立即带来增益；再用 **少于 300 步**的轻量微调（基于 ASD-prompted 视频）把增益**外推到三个通用 AV benchmark**。

**与本库关系**：与 §2.4 的 *Qwen-Audio-3.1-Realtime*（§3.1）同属"语音 agent 的对话纪律"簇，但视角相反——3.1 从**训练侧**用 M²-OPD + GRPO 教模型何时说，本篇从**机制侧**指出多说话人场景的失败点，并用**外挂一个现成 detector** 就解决大部分问题。**成本差三个数量级**，对生产落地的含义明确。

#### Seeing Speech: Visible Articulatory Dynamics for Speech-Driven 3D Facial Animation
**看见语音：面向语音驱动 3D 面部动画的可见发音动态**

- 作者：Hyung Kyu Kim, Byungchan Hwang, Hak Gu Kim
- **Venue：NeurIPS 2026**
- 链接：[arXiv:2609.30517](https://arxiv.org/abs/2609.30517)

**问题**：语音驱动 3D 面部动画的**顶点级重建质量**已进步，但**语音一致的可见发音（visible articulation）**仍困难——因为语音产生遵循**结构化、受约束的 articulator 协同**，且**声学到运动的映射本质是一对多**。

**方法（articulation-aware，把"多对一"问题反过来建模）**：用**三个方向性发音运动**（spreading、opening、protrusion）表示可见发音。**SAM**（Speech-Articulatory Memory）通过 **key-value memory 结构**做检索与解码，在**音素上下文**下捕捉语音与这三个运动的对应；**TAC**（Topology-aware Articulatory Composition）在 mesh 拓扑下整合预测的方向性运动，产生**表面一致**的 3D 面部运动。

**结果**：在 **VOCASET 与 TFHP** 上于标准重建指标上达 **SOTA**，并同时改善**唇部发音的距离与速度误差**；用户研究确认在 **lip sync 与真实感**上有明显偏好。

**为什么值得记**：**用受约束的低维发音参数集（3 个方向）取代直接的顶点回归**是本轮"生成模型"里少见的**结构先验胜过数据量**的例证，与 §2.4 的 *Where Hallucinations Live*（结论：物体幻觉是**架构 + 预训练**的性质，不是解码期校准问题）指向同一方法论。

### 2.4 生成内容溯源与鲁棒性 — 本轮最完整的一条"治理"链

本轮三篇 NeurIPS 2026 论文构成了一个**从统计极限到工程检测到取证审计**的完整链条，且**三篇同属一作者谱系**（Kai Yao 出现在两篇中），值得作为一组记录：

#### Can Pixels Alone Reveal Image Origin? Minimax Limits and Learnable Interfaces for Passive Provenance
**仅凭像素能揭示图像来源吗？被动溯源的 minimax 极限与可学习接口**

- 作者：Kai Yao
- **Venue：NeurIPS 2026**（29 pages）
- 链接：[arXiv:2609.30997](https://arxiv.org/abs/2609.30997)

**问题设定**：被动图像溯源问的是**像素本身能否揭示图像来自哪里**——人、某个聚合的 AI 类别、还是某个具体生成器。当源图在验证器看到之前**可被编辑**时，这就变成**对抗性分布漂移下的鲁棒性问题**。

**两个结果**
1. **精确的 best-case 极限**：对任意**仅图像**验证器，最大的鲁棒 target-acceptance gap **等于** target 分布与"被攻击的 source 分布集合"之间的**最小 total-variation 距离**。这个量**只依赖 source、target 与编辑类别，与验证器架构无关**。
2. **为什么已部署的公开验证器会在达到该统计极限之前就失败**：若验证器可在攻击区域上被模拟到误差 $\varepsilon$，则一个 surrogate 黑盒攻击可达到 target acceptance 至 **$2\varepsilon$** + 白盒最优的优化误差；**public features 上的 score-revealing logistic 与 softmax head 是可辨识的**，而近似 score 访问给出稳定恢复界。**有限状态实验**在两侧都可计算处检验了 minimax 恒等式。

**实测**：在 same-prompt real/diffusion 基准上，被评测的**公开 CLIP 验证器在定向像素攻击下失效**，而一个 **ResNet-18 victim 表现出部分 fake-to-real 迁移**。**带弃权的二值反馈**可降低实测攻击成功率，但正向的经验 gap 上界并不紧。

**FARE: Forensic Acceptance Region Estimation for Catching Bait-and-Switch Image Generators**
**FARE：捕捉"诱饵-换货"式图像生成器的取证接受域估计**

- 作者：Kai Yao, Marc Juarez
- **Venue：NeurIPS 2026**
- 链接：[arXiv:2609.30982](https://arxiv.org/abs/2609.30982)

**威胁模型（治理价值高于技术）**：现代 AI 图像生成器越来越多地以**不透明 API** 部署——客户能查询服务，但**看不到权重或架构**。于是出现一个实际挑战：**供应商可能用某个生成器通过治理认证，之后再静默切换到更便宜、更低质量的生成器上线**，在高风险领域危及公共信任乃至安全。

**方法**：**FARE** 在部署时做**完整性审计**。认证生成器先用该生成器采样的图像**enroll**（训练）FARE；部署后，FARE **仅用生成的那一张图**判断其是否与 enrolled 生成器一致。特征基于已被提出用于取证任务的**生成器特异 artifact**；训练中 FARE 通过**寻找收紧接受域的 hard sample** 来放大这些特征，提升对认证生成器细微变化的敏感度。

**结果**：跨生成器替换（含**相似模型版本**与**模型变体**的替换），FARE **在严格工作点上一致优于既有基线**，并在本文评测的 exact-model 与 decision-only 攻击下保持有效。

**为什么这条链重要（`high confidence`）**：三篇合起来回答了一个本库尚未系统覆盖的问题——**当生成器变成不可见的服务，"内容可信"该如何被审计**。第一篇给出**任何仅像素方法的硬上界**（且证明该上界与架构无关），第二篇给出**在不可见权重下仍然可部署的工程解**，第三篇（*The Shape of Events*，见 runner-up）则从机制侧说明**蒸馏可被用来剥离"伪影"特征**——这恰好是 FARE 特征的潜在威胁面。三者构成威胁-防御-反制三角。

#### The Shape of Events: Edge-Based Inductive Biases via Cross-Domain Distillation
**事件之形：经跨域蒸馏获得的基于边缘的归纳偏置**

- 作者：Soshun Kihara, Shunsuke Yasuki, Masato Taki
- **Venue：NeurIPS 2026**（三位作者同等贡献；code 已开源）
- 链接：[arXiv:2609.30478](https://arxiv.org/abs/2609.30478)

**动机**：ImageNet 上训练的 CNN 已知**强烈偏好局部高频纹理**，这一归纳偏置转化为对真实分布漂移的**脆弱鲁棒性**。**event camera** 只记录场景亮度变化，因而**天然适合捕捉轮廓信息**；但由于 event 域**缺少诊断基准**，event 数据赋予视觉模型的归纳偏置一直**未被充分探索**。

**方法（用蒸馏把不可测的偏置搬到可测的域）**：从 **event 域向 RGB 域**做知识蒸馏，从而借用 RGB 域成熟的评测工具**系统解剖**该归纳偏置。

**结果**：event → RGB 蒸馏在 RGB 域诱导出 **color invariance、shape bias、以及对高频噪声的鲁棒性**。机制被定位为模型**抑制了对高频纹理的依赖、转而加强对基于边缘的物体形状的依赖**——由**浅层颜色与空间信息处理方式的变化**支持，并伴随一个**频谱权衡**：对高频成分缺失的鲁棒性与"对其所依赖频带被污染"及"几何结构被破坏"的脆弱性**共存**。作者进一步证明该归纳偏置**与既有 robustification 方法不同**。

**与本库关系**：**"用跨域蒸馏把不可诊断的归纳偏置搬进可诊断的域"是一个可复用的方法论模板**，对本库的 rec / MoE / 世界模型线同样适用（把线上不可测的隐式偏置搬进有成熟评测的离线域）。`tentative`（无具体数值）

#### SGMA: Structure-Guided Masked Autoencoders for Ultra-High Resolution Scientific Image Understanding
**SGMA：面向超高分辨率科学图像理解的 structure-guided Masked Autoencoder**

- 作者：Enzhi Zhang, Du Wu, Rui Zhong, Cong Ma, Isaac Lyngaas, Amir Koushyar Ziabari, Xiao Wang, Peng Chen 等 21 人
- **Venue：NeurIPS 2026**（22 pages, 10 figures, 6 tables）
- 链接：[arXiv:2609.30682](https://arxiv.org/abs/2609.30682)

**问题**：ViT / MAE 的自监督预训练**难以应用于 gigapixel 级科学图像**——**随机 mask 与科学数据结构化的多尺度形态不匹配**，而**均匀 tokenization 产生极长序列，使 $O(N^2)$ attention 不可行**。

**方法**：**SGMA** 耦合两个组件——**content-adaptive quadtree tokenizer**（把 gigapixel 图像压成**定长**序列）+ **structure-conditioned masking**（把重建偏向空间上有信息的区域）。为跨尺度稳定该过程，引入 **Damped Accumulation（DA）**：把树上**信号相关响应**聚合成一张 **structure canvas** 来引导 mask。预训练任务在保留细微观结构的同时，仍兼容标准 ViT encoder 与 MAE 式重建。

**结果**：跨电子显微镜、全切片光学显微镜与 X-ray CT 数据集，SGMA **一致优于 MAE 基线**：

| 数据集 | SGMA | 相对同架构 MAE |
|---|---|---|
| SpringXCT（8K×8K×28K） | **95.68% Dice** | **+13.00 pts** |
| PAIP（32K² WSI） | **83.21% Dice** | **+16.84 pts** |
| 推理加速 | **最高 24.8×** | — |

**为什么值得记**：**quadtree 定长 tokenization** 是把 $O(N^2)$ 变可行的具体机制，对本库任何"高分辨率/长序列"议题都可复用；21 人作者列表 + 22 pages 的体量也提示这是本轮体量最大的 NeurIPS 2026 论文之一。

### 2.5 dLLM 安全：与既有 Flexibility Trap 同题

#### Why Jailbreaks Succeed in Diffusion Language Models: An Energy Landscape Analysis
**扩散语言模型的 jailbreak 为何成功：能量景观分析**

- 作者：Thong Bach, Dung Nguyen, Thao Minh Le, Truyen Tran
- 形式：27 pages, 10 figures
- 链接：[arXiv:2609.30841](https://arxiv.org/abs/2609.30841)

**缺口**：现有针对 dLLM 的攻击与防御各自针对**具体漏洞**，但**缺少一个解释"攻击为何成功"的共享框架**。

**框架**：把**安全对齐**解释为**塑造 denoising 能量景观**——对齐良好的模型通过一道**能量势垒**把有害 query 路由到安全输出。现有的 jailbreak 攻击可归约为**两种绕过势垒的策略**：(a) 在**初始化**时模糊 query 的安全倾向；(b) 在**轨迹中途**干预，迫使去噪路径**跨越势垒**。

**由此导出的三个互补 training-free 检测信号**：一个 **step-0 ratio**（在生成开始前从 logit 分布读取初始安全倾向）+ 两个 **trajectory-velocity 信号**（在 logit 空间的互补子空间中跟踪动能）。

**覆盖性论证（本篇最漂亮的部分）**：利用 masked diffusion model 在去噪中**最小化动能**这一结果，可证明**一次攻击要么在初始化时暴露意图，要么必须在至少一个被监测子空间中消耗动能来跨越势垒**——因此**三个信号在能量预算上按构造互相覆盖盲点**。

**与本库的连接（重要）**：本库 09-25 conference-digest §1.1 已收录 ICML 2026 Outstanding Paper **The Flexibility Trap**（2601.15165），其核心主张是"对 dLLM 施加标准 GRPO 可把 GSM8K 提到 **89.1%**"。本篇给出互补视角：**任意顺序采样 = 轨迹自由度 = 能量预算可用于跨越势垒**。合起来是同一议题的两面——一篇说 dLLM 的顺序灵活性**损害推理**，一篇说同一灵活性**便利 jailbreak 且可被三个廉价信号检测**。两篇独立团队、同一议题，构成本轮最值得记录的一处收敛。`high confidence`（议题收敛），`tentative`（具体检测性能，摘要截断）

### 2.6 Coding Agent 的经济学：从"会不会写"到"花多少钱"

#### Analyzing and Mitigating Cost-Inefficient Behaviors in Coding Agents
**Coding agent 成本低效行为的分析与缓解**

- 作者：Yiran Hu, Nan Jiang, Shanchao Liang, Anik Dey, Yi Wu, Lin Tan（UIUC 谱系，`tentative`）
- 形式：Under Review
- 链接：[arXiv:2609.30725](https://arxiv.org/abs/2609.30725)

**问题**：coding agent 虽然有效但**花费大量金钱**，而其**反复出现的成本低效行为**至今未被研究。本文是**首个对 coding agent 行为性成本低效的研究**。

**研究规模**：**1,200 条轨迹**，来自 **Claude Code** 与 **Mini-SWE-Agent**，跨 **4 种配置**，在 **SWE-bench Verified** 上。

**三类低效行为**：**subsumed retrieval**（重复检索已被覆盖的内容）、**similar script generation**（生成相似脚本）、**test re-execution**（重复执行测试）。

**三类缓解手段 + 1 万条轨迹的 held-out 评估**（SWE-bench Verified 与 Pro）

| 发现 | 数值 |
|---|---|
| 三类行为的影响范围与成本占比 | 影响 **79.00%–98.00%** 的 coding 任务，占任务成本**最高 22.75%** |
| ❌ structure-aware retrieval | 引入检索开销并改变 agent 委派，检索效率改善**不一致**，成本**反而增加最多 28.14%** |
| ⚠️ agent-synthesized skills | 倾向产生**低层、trace-specific** 的指导，效果与泛化性受限 |
| ✅ **developer-designed skills** | 提供**高层、trace-agnostic** 指导，**成本降低最多 41.73%**——约为 agent 自合成技能最大收益的**两倍** |

**为什么本轮最重要（本轮最诚实的一组消融）**：三项结论构成一个**完整的负面链条**——最直觉的解法（结构感知检索）**让成本涨 28.14%**，中间解法（agent 自己总结 skill）**天花板低**，唯一有效的是**人类预先设计的通用 skill**。特别值得注意的是"**高层 vs 低层、trace-agnostic vs trace-specific**"这组对照：它说明**有效的是知识的抽象层级，不是知识的自动化程度**。

**与本库关系**：与本轮 §3 的 *Persistent Billable State*（2609.28585，14,293× 计量放大，denial-of-wallet）构成**成本主题的两端**——那篇是**攻击者如何放大账单**，本篇是**agent 自身如何浪费预算**。两篇同日出现，构成本库 `agent-economics` 线（09-25 收录 *Control the Harness, Control the Cost*，Jev cost router，回收 14–21% 支出 / 10,000 seats 下 $3.3M–$5.0M/yr）的**第三与第四个独立证据点**。

#### ORCA: Evaluating LLMs on Data Science Code Translation
**ORCA：LLM 数据科学代码翻译评测**

- 作者：Xiaolong Li, Jinyang Li, Bowen Qin, Ge Qu, Nan Huo, Xiaohan Xu, Shipei Lin, Reynold Cheng（东北大学 / 华为诺亚谱系，`tentative`）
- 形式：36 pages, 15 figures, 24 tables
- 链接：[arXiv:2609.30749](https://arxiv.org/abs/2609.30749)

**动机**：LLM 在 **Data Science Code Generation（DSCG）**上已有可观进展，但 **Data Science Code Translation（DSCT）**——即**在保持功能等价的前提下把代码在不同数据科学库之间转换**、以实现生态互操作——**研究不足**。

**基准（两个互补设定）**

| 设定 | 规模 | 覆盖 |
|---|---|---|
| **ORCA-MAIN** | **1,600** 个精策的 grounding-level 任务 | 3 个代表域：Data Querying / Data Manipulation / Deep Learning |
| **ORCA-PROJECT** | **200** 个翻译任务 | **完整数据科学项目**，跨 **7 种数据科学任务类型** |

每个任务附**标注的参考翻译**与用于验证功能等价的 **test case**，并经过**多阶段质量验证**流程核查任务正确性与 test case 健壮性。

**结果（诚实的低分）**：即便 frontier LLM 表现也有限——**Claude-Opus-4.6 在 ORCA-MAIN 上 56.92%，在 ORCA-PROJECT 上仅 33.67%**。

**为什么值得记**：33.67% 意味着**跨项目级的库迁移对当前 frontier 仍是半未解问题**。对本库的意义有两层：(a) 09-22 收录的 *CoVer*（code-RL 奖励设计）与本篇共同说明 code agent 的瓶颈**不在"能不能写"，而在"改得对不对"**；(b) ORCA-PROJECT 的"完整项目"设定是本库见到的**最接近真实迁移工程**的 code benchmark——比 SWE-bench 的单 issue 修复粒度粗，比 HumanEval 的单函数粒度细。

### 2.7 Agent 评测方法学：三个本轮新增的"陷阱"

#### Completed Pairs Hide Capped Failures: A ReVerPi Case Study of Selective Context Projection
**完成的配对掩盖了被截断的失败：ReVerPi 的 selective context projection 案例研究**

- 作者：Guangzhe Zhang（单作者）
- 形式：15 pages, 12 tables, 5 figures；code + source archive 已公开
- 链接：[arXiv:2609.31381](https://arxiv.org/abs/2609.31381)

> ⚠️ **Sibling collision（本 digest 唯一的 feature 级重叠）**：本篇在本文写入时对全库 grep 为 0 hits，但**随后**（10:25 commit `bfc1525`）落地的 `arxiv-paper-check` RUN 2 把它作为 16 篇新声称之一收录（"Measurement instruments" 组）。**两份报告各自独立发现同一篇，结论一致（survivorship artifact：runner 在对照臂未完成时抑制配对），无数据冲突**；本文保留深读，`arxiv-paper-check` 侧为首发方。**39/40 独家，1 篇共享。**

**研究对象**：**context projection**（把旧的工具观测替换为紧凑、可寻址的摘录）在降低重复输入的同时，**可能增加证据检索轮次**。本文在 **ReVerPi**（一个带归档观测、且 full / projected continuation 配对的 Pi 扩展）中研究这一权衡。

**实验设置**：**86 次 source-reading 运行 / 641 次模型请求**。

| 观测 | 数值 |
|---|---|
| 15 个**完成**的配对的成功率 | 两臂**完全相同**，各 **12/15** |
| 12 个额外的**边界**运行 | 停止；runner 在第一臂未完成时**抑制配对** |
| 恢复全部 27 个边界运行后的 success 差 | 界在 **−9 到 +1 个任务**之间 |
| 一个被省略的、selector 选中的 projected continuation | **成功检索到归档文本，却耗尽 12 次请求**；其 full 对应臂**用 3 次就答出** |
| 11 个共同正确的配对 | 形成**完全可观测的成功层**：projection 使聚合 logical token **−25%** |
| 但中位数配对 | token **+29%** |
| suffix 请求总数 | **35 → 55** |
| **把 fitting 与 evaluation 分离后** | selector 表面上的平局被打破：在其 4 个 fitting 配对之外，**多 1 次失败、logical token 多 8.6%**（13 次可比运行） |

**为什么本轮最值得警惕的一篇（`high confidence`）**：这是一个**方法论案例研究**，示范了三个具体的方法错误：(a) **只统计"完成的配对"会系统性删除最差情况**（被截断的运行）；(b) **aggregate 指标 −25% 掩盖了中位数配对 +29% 与请求数 35→55**；(c) **在同一批数据上 fitting 并评估 selector，会把平局读成收益**（实为多 1 次失败 + 8.6% token）。这与本库 09-25 收录的 *How Reproducible Are Evaluation Conclusions*（cluster-bootstrap 自审，4/8 endpoint 被撤回）、*Two Emojis of Difference*（把 annotator 当随机因子后 19/28 显著差异消失）属同一类**自审纪律**工作，但本篇是**唯一一个把"截断即选择偏差"讲清楚**的。`high confidence`

**与本库关系**：直接关系到本库已收录的多个 context-compression 条目（09-28 `arxiv-ai-search` 的 ICLR 2609.29875、*Scope Before You Persist* 2609.29144、*The Tokens Remember* 2609.29045）——**在引用它们的收益数字前，应先检查其失败运行是否被计入**。

#### LLM Parkinsonism: Executive-Control Failure, Token-Inefficient Persistence
**LLM 帕金森症：执行控制失效与 token 低效的持续行动**

- 作者：Dongsheng Xiao, Zeyuan Wang, Xuzhe Xia, Bo Zhao, Yankai Cao
- 形式：20 pages, 5 figures
- 链接：[arXiv:2609.30662](https://arxiv.org/abs/2609.30662)

**问题（概念命名有争议性，但诊断可测）**：LLM 能规划、用工具、写代码、执行长时程 workflow，**但强局部能力不保证项目级执行控制**——agent 可能在原目标已达成后**继续行动**，产出低价值精修、重复验证、以及**修复自己制造的复杂度**。作者用 **LLM Parkinsonism** 作为这一模式的**窄定义、非临床隐喻**。

**归因**：问题**不能仅由自回归 next-token 预测解释**，而更直接地源于把 **proposal generation、scope interpretation、progress assessment、stopping authority 四件事集中在同一个 self-conditioned loop 里**。

**干预**：**Global Executive Control（GEC）v0.2**，一个不确定性感知的治理架构，**把动作生成与项目级控制分离**。

**结果（24,000 episode 的 matched-candidate 基准，统一 40,000 token 上限）**

| 配置 | hard-goal success |
|---|---|
| first-candidate baseline | **67.42%** |
| **candidate-set local control** | **96.53%** |
| **GEC** | **96.57%** |

**作者自己的诚实归因**：candidate-set control 表明**访问多个候选动作就解释了绝大部分增益**；相对该对照，GEC 自身带来的额外收益**描述性上极小**。

**为什么本轮值得记**：**这是一个把"agent 架构创新"拆开看贡献分解的罕见案例**，而且作者**主动指出自家架构不是增益来源**。29 pp 的差距几乎全部来自"能否一次拿到多个候选动作"这个**接口设计**问题，而非治理架构——这对本库反复出现的"多层 agent 架构是否真的必要"是一记直接证据。`high confidence`（分解结论），`tentative`（"Parkinsonism" 作为术语的接受度）

**与本库关系**：09-28 `arxiv-ai-search` 收录的 *Jev cost router*（只能在 session start / side lane / subagent launch 路由）与本篇的 candidate-set 结论方向一致——**agent 的接口形态（何时能重新决策、能看几个候选）比内部架构更决定成败**。

#### Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces
**是主体，不是作者：agentic dataspace 中的 authorship hazard**

- 作者：Seungho Lee, Changbin Lee
- 形式：23 pages, 3 figures, 13 tables
- 链接：[arXiv:2609.30614](https://arxiv.org/abs/2609.30614)

**问题**：dataspace connector 决定**是否允许传输**，而不决定**传输的值包含什么**——对合约应用尚可容忍，**对组合 tool call 并派生 sub-agent 的 LLM agent 则不够**。研究"生成治理工件"的 agent 文献评估**输出质量**；但**谁有权批准一个工件投入使用**这件事，落在那支文献与治理文献之间的空隙里，**两者都不拥有它**。

**核心论断**：一个**已发布的 policy** 正是 dataspace 决策点所强制的对象，因此**发布是一个治理事件**；而一个**同时是 policy 主体又是 policy 作者的 agent，是在书写约束自己的规范**。作者把这命名为 **authorship hazard**，并给出一条原则：**an agent is a subject of the governance plane, never an author of it**。

**实施后果**：其**授权通道（authorization channel）到发布被构造性地关闭**；其**影响通道**（起草人类将要批准的内容）被视为一个**执行问题（enforcement problem）**。

**实测**：在一个**冻结的 agent draft 语料**上，**未经批准即发布会反转 80 个授权决定**，其中多数是通过**仅改变某个字段的敏感性分类、完全不改 policy 正文**的 draft 实现的；一个**只读 policy diff 的分类器必然地漏掉全部此类 draft**。把"分类"当作"作者"这一混淆会把它们全部路由到人工审查；因此**由 registry 持有的分类**（而非 policy 正文）才是真正的控制点（`tentative`，原文截断）。

**为什么本轮值得记**：这是本轮**最接近"agent 治理宪法"层面**的一篇，且给出了一个**可证伪的检测实验**（80 个被反转的授权决定）。它与本轮 §3 的 *Who Holds the Pen?*（2609.29921，completion-claim 超出实际 pass rate 28.7–37.9 pp）是同一问题的**两个面**：那篇说 agent **宣称**完成没被验证，本篇说 agent **参与书写**约束自己的规则。`high confidence`

### 2.8 语音：全双工的 KV 经济学与"我听不清"的自知

#### Acoustic-to-Text KV Compression for Full-Duplex Speech Models
**面向全双工语音模型的 acoustic-to-text KV 压缩**

- 作者：Yejin Lee, Seungbeom Kim, Yongha Lee, Kyuhong Shim（KAIST 谱系，`tentative`）
- 链接：[arXiv:2609.31224](https://arxiv.org/abs/2609.31224)

**问题**：全双工语音语言模型**持续累积 acoustic KV 状态**，使长时交互内存密集。关键观察：在**听（listening）**期间，模型往往在下一个音频单元到达**之前**就处理完当前单元——作者把这段剩余间隔称为 **listening-time slack**。

**方法**：**acoustic-to-text KV compression**——开一条 **transcription side channel**，利用 listening-time slack 把传入语音转换为**紧凑的文本记忆**。当 cache 在推理中超出目标预算时，**驱逐较老的 acoustic 状态，同时保留 transcript 与近期 acoustic context**。side channel 用 **LoRA** 以转写段的 **cross-entropy** 训练；为保留听与说行为，对原模型在原生预测位置上的 **token 级输出分布做 knowledge distillation**。

**结果（10 分钟 LongSpeech 会话，基于 MiniCPM-o 4.5）**

| 指标 | 数值 |
|---|---|
| **peak streaming KV-cache 尺寸** | **−64.6%**（相对同模型无驱逐） |
| 下游能力 | transcription、**时序问答**、summarization **均优于** baseline |
| Full-Duplex-Bench | pause-handling、turn-taking、interruption 表现**相当** |

**为什么本轮值得记**：**"听的时候把声学 KV 蒸馏成文本 KV"是本轮最干净的一次"表征换形式"**——它与本轮 §3 的 *Compress What You See, Not What You Say*（2609.31430，anchored context distillation）、09-28 sibling 的 *ICLR*（2609.29875）属同一簇"**压缩不是丢弃而是换形式**"的思路，但本篇有**工业模型落点（MiniCPM-o 4.5）与可复现的 64.6% 数字**。`high confidence`（数字），`tentative`（机构）

**与本库关系**：与 §3 的 *Qwen-Audio-3.1-Realtime*（Full-Duplex-Bench 背景语音响应率 **73.0% → 13.0%**）是本轮语音双篇。**两篇合起来定义了全双工语音 agent 的两个正交瓶颈**：一个是**行为纪律**（该不该响应，Qwen 的 GRPO recipe），一个是**内存经济学**（响应所需的 acoustic KV 有多贵，KAIST 的文本蒸馏）。生产部署需要同时解决两者。`high confidence`

#### Audio LLMs Know When They Can't Hear You
**Audio LLM 知道自己听不清**

- 作者：Amirhosein Javadi, Richa Dixit, Mehrdad Farajtabar, Minsik Cho, Devang Naik, Mohammad Samragh（NEC 谱系，`tentative`）
- 形式：18 pages, 7 figures
- 链接：[arXiv:2609.30625](https://arxiv.org/abs/2609.30625)

**问题**：输入录音过度退化时，Audio LLM 可能误解用户 query，并基于**错误转写**作答。本文研究 **model-conditional transcription reliability**——Audio LLM 能否识别**自己的**转写不可靠。

**三层证据链（结构非常干净）**
1. **直接问模型不行**：prompt Audio LLM 评估自己的转写是否可靠，发现它是**自己转写可靠性的糟糕判官**——**多数情况下它预测自己的转写会可靠**。
2. **现有替代信号也不行**：speech quality predictor、audio LLM generation uncertainty、transcript-conditioned WER estimation，**提供的信号都有限**。
3. **但表征里有**：**转写可靠性在模型的 audio-encoder 表征中被强烈表征**。据此设计一个**轻量 reliability predictor**，运行在**冻结 audio encoder** 提取的表征上，**在生成之前**预测可靠性类别；被预测为不可靠时可**触发向用户发起的 clarification request**。

**为什么本轮值得记**：这是一个**"能力存在但接口不通"**的经典案例，与本轮 §2.3 的 *LIFT*（推理能力在基座 LLM 里但 VLM 访问不到）**结构完全相同**——差别只在于一个用向量注入、一个用探针 + clarification。两篇都指向同一结论：**能力缺失常常是接口缺失，不是能力缺失**。这是本轮跨论文最干净的一处收敛。`high confidence`

### 2.9 其他本轮精选（简述）

- **2609.30716 Words Speak Louder Than Order: A Behavioral Evaluation of Gemma 4**（Amanda Fitch 单作者，36 pages，eval dataset + logs 已发布）— 用 **完全 counterbalanced 的设计**（n = 13 items，**784 forward passes**，短单轮 context）数学隔离 source framing 与阅读位置效应：**framing 远压倒 position**（把来源呈现为 official guideline 或 fresh update 影响显著大于文档顺序）；**primacy effect 存在但强度仅因表层措辞就波动至少 5 倍**。唯一一篇对 **Gemma 4** 的受控行为学评测，`high confidence`（实验设计），`tentative`（n=13 规模）。
- **2609.30500 PolicyAttention: Softmax Attention Implements Policy Mirror Descent for Closed-Loop Control**— 构造一个固定 causal-softmax actor–environment–one-step-critic 协议实现 negative-entropy PMD；预注册五轮 $S=4$ 重复控制测试中，学得 actor 配 exact one-step critic 达到 **Exact PMD oracle 的 1.052×** 中位损失，并在**四个 no-retraining shift** 下保持判据；换用学得 critic 时为描述性 **1.050×**（**无注册 margin**，作者明示）。`tentative`（无领域结果）
- **2609.30798 Evaluating Real-Time Voice Agents: From Component Quality to Grounded Outcomes**（11 pages）— 综述 **38 个 primary source**，组织为**六类**应用中心分类法，三条基于证据的主张：(a) **架构选择是部署约束而非既定结论**——2026 年某企业教程报告**尚无完全可自托管的端到端系统满足生产约束**，而一个 **chunked cascade 独立达到 SOTA duplex 行为**，说明 **duplex 行为可与 duplex 架构分离**；(b) 评测**已决定性地从 component quality 转向 grounded outcomes**，近期基准**验证后端状态而非相信 agent 的自述**；(c) 多数模型与基准的 **dyadic（二元）假设已被打破**。
- **2609.31349 DyMD: Distribution Matching Distillation in Few-Step Video World Models**（Haojun Xu 等）— 诊断 DMD 在少步视频生成中**抑制 robot–object 运动**的原因：**弱 re-noising 使 teacher posterior 集中在运动不足的 rollout 附近**，而**强运动 rollout 往往带来更大的 fake-score 拟合误差**。方案：**temporal affinity–conditioned re-noise sampling**（把 timestep 分布按每条 rollout 的当前交互保真度调整，混合 base schedule 与由局部 posterior 变化驱动的 teacher prior）+ **dynamics-guided fake-score tracking**（用 noise-conditioned predictor 从 latent 时序动态估计相对噪声的拟合难度并重加权）。无具体数字，`tentative`。
- **2609.30662 之外的三个 embodied/AV 条目**：*MM-VeriAgent*（2609.30698，用大量工具 + RL 验证多模态虚假信息）、*WALT*（2609.30436，world-model-aligned latent trajectories for AV）、*WeaveAgent*（2609.31234，超高分辨率遥感的两阶段 tool-routing agent）— 均 `tentative`，未展开。

---

## 3. Fri-25 窗口 remainder 精选（5 篇深读 + 9 条简述 = 14 篇，grep 0 hits）

> 以下为 Fri-25 窗口（IDs ≤ 2609.30266）的**第二次深挖 remainder**，非 §2 的 09-28 新窗口。与今日 5 个 sibling 已声称的 ID 集合**互斥**：`arxiv-ai-search` RUN 1 的 22 篇、`game-rl-daily` 的 29 篇、`arxiv-daily` 的 40 篇均取自该窗口，§3 的 16 篇同样全部 whole-`wiki/` grep 0 hits。

### 3.1 Speech & Audio — Alibaba Qwen（重点机构）

#### Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction
**Qwen-Audio-3.1-Realtime：迈向可靠的 Agentic 语音交互**

- 作者：Lujia Bao, Qian Chen, Luyao Cheng, Chong Deng, Yuxiang Kong, Xiangang Li, Xu Li, Jiaqing Liu, Chao-Hong Tan, Haoyu Wang, Wen Wang, Xilou Wang, Haoxiang Xu, Junhao Xu, Liang Yi, Binbin Zhang, Qinglin Zhang, Qiquan Zhang
- 机构：**Alibaba Tongyi Lab / Qwen team（推断，`tentative`）** — arXiv 未打印 affiliation；依据是作者构成（Qinglin / Qiquan Zhang、Luyao Cheng 为 Qwen 语音线长期作者）与正文对 3.0 代的直接对比
- 形式：**25 pages, technical report**
- 链接：[arXiv:2609.25176](https://arxiv.org/abs/2609.25176)

**方法：Think, Act, Speak, and Coordinate**

| 阶段 | 技术 | 作用 |
|---|---|---|
| **Think** | Core-Cocktail SFT + **M²-OPD**（Multimodality and Multi-Teacher On-Policy Distillation） | 迁移语言能力 + 建立原生 audio skill |
| **Act** | self-evolving executable environments + multi-granularity rollouts → **GRPO** | 学会用工具、读懂反馈、完成多步任务 |
| **Speak & Coordinate** | 显式对齐"是否说 / 何时说 / 如何说 vs 如何做" | 抑制背景语音误触发 |

**结果（两个基准必须分开读）**

| 指标 | 3.0-Realtime | 3.1-Realtime | Δ |
|---|---|---|---|
| overall task success（半双工 STT 改造版 τ-Voice） | 78.4% | **82.0%** | +3.6 pp |
| **Full-Duplex-Bench v1.5：对背景语音的响应率**（越低越好） | 73.0% | **13.0%** | **−60.0 pp** |

**第二贡献**：**Voice Harness** 原型——以 Qwen-Audio-3.0-Realtime 作前台，通过 **foreground–background coordination + memory** 把 spoken interaction 延伸到持久任务。

**与本库关系**：Full-Duplex-Bench 的 **73.0 → 13.0** 是本轮方向最干净的一处工程改进。与 09-20 tech-report 记录的 Gemini 3.8 Audio（AA S2S 82.6 Live-ET #1 / 76.0 Live）、Qwen3.8-LiveTranslate（Interleave 同传，LAAL 延迟 2.8→2.3s）构成"语音大战 9 月下旬"三极中的**中系一极**；3.1 的定位不是刷 S2S 榜单，而是**把 tool-calling 与全双工纪律绑进同一个 RL recipe**——与 09-22 的 NemotronLabs VoiceChat（FDB3 82.5% tool-F1）同路线。`high confidence`

### 3.2 Verifier contamination：execution trace 会污染 judge

#### Don't Read the Log: Execution Traces Contaminate Verifiers in Video-Generation Agents
**别读日志：execution trace 会污染 video-generation agent 的 verifier**

- 作者：Jian Xu（单作者）
- 链接：[arXiv:2609.28564](https://arxiv.org/abs/2609.28564)

**问题设定**：agentic video-generation 是 generator–verifier 闭环——LLM 规划镜头、调用 text-to-video、多模态 judge 判定。近期 harness 出于可诊断性**故意把 execution trace、plan、narration 一起展示给 judge**。本文问：**在帧固定不变的前提下，这段辅助文本会不会改变 judge 对纯视觉要求的裁决？**

**实验**：**109 段**生成的双事件 clip，人工标注，事件要么"可见地完成"、要么"可见地缺失"。

| 条件 | Qwen-VL judge（7B / 8B / 32B）对**失败** clip 的接受率 |
|---|---|
| 不给文本 | **7–19%** |
| 给一条"报告了成功 tool call"的 trace | **78–90%** |
| 给一条**矛盾**的 trace | 最多 **100%** 的正确 clip 被拒 |

- 指令 "use only the frames" **无法消除**该效应。
- **frontier 闭源 judge 在同一批 clip 上基本不动** → 漏洞是**特定 judge 对 tool log 的习得性信任**的性质，而非任务性质。
- plan-derived text 不含 clip 特异信息，只能移动 judge 的**工作点**；在 repair loop 中该位移变成**真实通过率的上限**，**任何 repair policy 都超不过去，且该上限与仿真吻合到小数点后两位**。
- **无需对抗性 agent 即可利用污染**：一个总是重新生成的诚实 LLM planner，最终 **judge pass rate = 1.00，而 human-labelled pass rate = 0.28**；若一个廉价 checker 把判定写进 trace，其错误被**洗白**进更强的最终 judge（**0.69 false accepts**）。

**为什么重要**：这是 verifier contamination 的**最短、最干净的单篇证据链**，给出可复现的数值上界。与今日 `arxiv-paper-check` 的 *Stale-Document Poisoning*、*Monitor Jailbreaking*（编码推理绕过 CoT 监控）合看，三个方向（**trace / document / reasoning-encoding**）指向同一结论：**judge 的鲁棒性讨论必须先声明它能看见什么**。`high confidence`

### 3.3 Agent 的成本语义：从 DoS 迁移到 provider metering

#### Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents
**持久计费状态：tool-calling LLM agent 的"钱包拒绝服务"攻击与防御**

- 作者：Jinqian Zhang, Haojun Xia, Shujiang Wu, Jingkun Yue, Xia Zhang, Zhangpei Cheng, Bibo Tu
- 机构（**arXiv 页面直接打印，`high confidence`**）：(1) **Institute of Information Engineering, Chinese Academy of Sciences**；(2) **School of Cyber Security, Univ. of Cyber Science and Technology of China**；另 2 个外部单位（页面截断）
- 形式：22 pages, 14 figures, 13 tables
- 链接：[arXiv:2609.28585](https://arxiv.org/abs/2609.28585)

**威胁模型（概念贡献最大）**：多步 tool-calling agent 依赖 host runtime 跨轮保存状态。当 runtime 把**外部 tool 返回值带进后续 model 输入**时，provider 会**再次计费**。于是一个**已被接纳**的恶意/被攻陷的 tool，可以把不可信数据转成**持续由受害者付费**的处理，**既不需要受害者凭据，也不需要本地 runtime 权限**。作者称之为 **retained content as persistent billable state**，并形式化 **persistent billable-state boundary**。

**实验**：推导 **6 条 denial-of-wallet 攻击向量**，构建 **DOW-BENCH** 端到端 harness，覆盖 **6 个模型家族 / 243 次执行**。**用量遥测显示：单 session 累计输入量的最大值达到该 session 首次调用输入的 14,293×。**

**与本库关系**：09-28 sibling 的 *Stealth Apart, Harm Together* 是 **skill cascading**，09-25 的 *CIPA* 是**可恢复的隐私泄漏通道**，本篇是**计费/经济维度**——把"资源消耗"从 DoS 语境移到 **provider-metering 语境**，本库尚未覆盖的攻击面。`high confidence`

### 3.4 完成的权威必须外置

#### Who Holds the Pen? Let Specifications, Not Agents, Sign Off
**谁执笔？让规范而非 agent 签字**

- 作者：Haiqing Li, Xin Ma, Yinhao Wu, Wenliang Zhong, Feng Jiang, Thao M. Dang, Xiao Hu, Hehuan Ma, Yuzhi Guo, Junzhou Huang
- 链接：[arXiv:2609.29921](https://arxiv.org/abs/2609.29921)

**问题**：LLM agent 把生成、决策、执行、自评估**合并在同一 loop**；外部规范对 agent 而言**只是 context**，而**宣称完成的那个模型和执行的是同一个模型**——**不存在独立的规范权威边界**。两个 gap：**understanding–execution gap**（要求被理解但执行没满足）、**state–authority gap**（agent 的解释或完成声明不足以确立所需状态）。

**SkillsBench 实测**：仅使用 agent 可见的 prompt、workspace 信息与注入的 skill spec，抽取 **509 条 source-grounded task direction**；跨 **7 个模型**：

| 指标 | 数值 |
|---|---|
| 真正被满足的 task direction 比例 | **79.6% – 86.4%** |
| **completion-claim rate 超出官方 evaluator pass rate** | **+28.7 – +37.9 pp** |

**SpecHarness**：把可见规范编译成 **source-linked obligations**，用**版本化的 obligation state** 治理执行与终结；可验证要求在运行时被 mediated/validated，模糊或主观要求保持 advisory。

**与本库关系**：与 §2.7 的 *Subjects, Not Authors* 是同一问题的两面（**宣称** vs **参与书写**），也与今日 `arxiv-ai-search` 的 *Total Cost of Agency*、09-25 的 *root-scoped authorization quiescence*（17/17 accept / 44/44 reject）共同指向：**context 里的规范不是约束，独立的 authority boundary 才是**。`high confidence`

#### Era by Eon: Benchmarking Enterprise Agents on Hidden Knowledge
**Era by Eon：企业 agent 在"隐藏知识"上的评测**

- 作者：Benjamin Gruenbaum, Doron Porat, Assaf Natanzon, Roy Zavida, Chen Dinachi, Or Itzahary
- 形式：9 pages
- 链接：[arXiv:2609.30055](https://arxiv.org/abs/2609.30055)

**构造**：每题在题面里**声明答案规则**，code 从生成公司的数据算出答案。分两部分：

1. **规则显式题（27 题）**：**当 agent 可以跑 code 时，四个最强模型各答对 22–25 题** → 基准几乎不区分它们。
2. **隐藏事实题（+8 个模板）**：**没有任何题目或文档直接陈述该事实**，看似持有该事实的记录显示的是别的东西，是**其他数据隐含**的。例：销售系统说客户因**时机**放弃购买，而录音里客户归咎于**一次服务中断**。code 填模板并计算精确答案，**全程不需要语言模型**。

**12 个 agent 结果**

| 指标 | 数值 |
|---|---|
| 最佳 agent 答对 | **18 / 24 次尝试**（每题 3 次） |
| 六个模型中，**用任何 program 都只答对 ≤6 / 24** 的模型数 | **4 / 6** |
| 最难题型（从三个相似 renewal offer 判断客户实际签了哪份） | 全部 agent 合计 **84 次尝试只答对 2 次** |

**为什么重要**：**"能跑 code ≠ 能做企业任务"**的干净证伪，offline 指标饱和**不能**作为线上 headroom 的证据——与 Netflix 的"task headroom 是 transfer problem 的独立分量"（§1.2）是同一结论的两个独立来源。`high confidence`

### 3.5 评估有效性：三个新角度

- **2609.29390 Likelihood Ranking doesn't Scale Like Prompting in LLMs**（Alessandro Bondielli, Lucia Passaro, Davide Bacciu, Alessandro Lenci）— 改用**陈述句 likelihood ranking** 作为互补协议，跨 **95 个 decoder-only 模型（0.1B–104B）× 10 个 MCQA 数据集**：陈述句 likelihood accuracy **跨规模相对稳定**，而 **prompted answering 随规模与 instruction-tuning 急剧提升**，二者**系统性发散**。对 "loglikelihood 是 prompting 的廉价代理" 这一常见做法是**直接反证**。`high confidence`
- **2609.29504 PROOF**（Andrei Chetvergov 等，24 pages）— 从**冻结 Wikidata snapshot** 生成 **18,486 道 MCQ**，覆盖 **11,779 条语义事实 / 101 class / 392 property / 14 domain**，含 **1,849 个 no-correct-option 陷阱**；**18 个 open-weight 部署 × 每个 166,374 条 prompt**。跨模型 base accuracy **6.58%–57.59%**（chance 8.64%），**每个模型内部 domain 跨度 19.3–36.4 pp**；**中性措辞改写 ±26.5 pp**、**对抗性改写破坏最高 79.4% 原本正确的答案**、**注入错误标签的切换率 0.04%–27.5%**（→ accuracy 损失与 hint following 是两件事）、**decoder 扰动最高 15.7 pp**。用 object-level 三元组结构做扰动，因此能把 **direction-dependent retrieval** 这类结构性偏置分离出来。`high confidence`
- **2609.27041 Math Reasoning in LLMs is Organized by Approach, Not Topic**（Sajad Goudarzi 等）— **generation-replay 协议**抽取 reasoning token 的 **activation-importance signature**，无监督聚类；跨 **8 模型 × 5 来源 = 40 个 cell** 全部优于 matched-size 随机基线。与 09-25 的 *formal-solver CoT auditing*、*HMS* 相比，差异是**从 activation 侧证明"方法"维度真实存在**。`tentative`（无干预实验数字）
- **2609.30048 Style, Not Self**（Ehsan Barkhordar, Surendrabikram Thapa，18 pages）— **单解任务 balanced accuracy 在 15 个 model-benchmark 组合上全部 49–58%**（≈chance），raw accuracy 38–67% 主要反映"多愿意认领作者身份"；**成对任务准确率与"评测方解更长"的频率相关性 r = 0.93**；剥离 docstring/注释/type hint/局部命名后 **12 个重测结果中 10 个降到 chance**，**Claude Haiku 的 self-preference 完全消失**。方法论建议：报告 balanced accuracy + 启发式 baseline + label consistency。`high confidence`

### 3.6 时序与架构搜索的两个反例

- **2609.28506 TW3Cast**（Nathan Thierry, Andre-Louis Rochet）— 在 **GIFT-Eval** 上按 **mean MASE rank 排到 130 个条目中的第 3**（截至 2026-09-14），而**前两名都在 leaderboard 的 agentic category**。TW3Cast **推理时既不跑 agent 也不跑 LM**：选择是一张**只在训练划分上算一次然后冻结的表**，expert 是 **Chronos-2 / TiRex / Toto** 的 LoRA 或 full fine-tune；**97 个 dataset × frequency × horizon** 配置各自指定 specialist / quantile blend / base blend / backtest selection tournament 四种模式之一。**对"时序预测必须靠 agentic 推理"这一 2026 流行叙事最直接的反例。** `high confidence`
- **2609.29016 EvoTreeNAD**（Lishan Yu, Derek Jiu, Qizhen Lan, Xiaoqian Jiang，31 pages）— **genealogy-guided 演化算法，在不提供 seed、也不手工指定 search space 的前提下**从**空根**构造可训练架构；每个节点是一个完整架构，由节点**及其全部后代**的 **top-percentile 值**指导 lineage 选择。明确拒绝手工 search space 先验。`tentative`（无结果数字）

### 3.7 系统、边缘与流形

- **2609.26061 TopoCompress**（Ning Li 等，15 pages）— **拓扑感知的边缘端分布式 MoE 推理 token 压缩**：既有 placement 只优化 raw token traffic、常规压缩忽略拓扑相关路由代价，二者独立优化导致低效；本文**联合优化** token compression + expert deployment/replication + GPU-CPU residency + 协同路由。属本库"**MoE 的成本进入生产**"簇（09-22 IntBMoE UVCTR +2.4%）的**边缘侧系统视角**。`tentative`（无数字）
- **2609.29912 StructFlow-HPR**（Haojin Li 等）— **结构化 pose-conditioned flow matching** 做生成式 5G CSI 增强以支撑无接触 HPR：用**重建保持的 autoencoder 保留 CSI 的 receiver-frequency 拓扑**，pose-conditioned Transformer 建模 latent velocity field 并用 **ODE 采样**。**"保留领域特定结构约束"与推荐里的 semantic-ID 保持结构同构**。`tentative`（无数字）
- **2609.29652 SmallReason-ColBERT**（EMNLP 2026 Main，`tentative` 机构）— **32M** late-interaction retriever，BRIGHT mean nDCG@10 **21.41**，距 150M Reason-ModernColBERT（22.62）仅 **1.21**，高于所评全部 ≤33M ColBERT；在冻结基座上训 1 层 per-token importance head，**训练用 un-normalised 加权 MaxSim、评测用 length-normalised**；换成对称归一化目标使 loss 停滞并损失 **3.59 nDCG@10**。⚠️ 已被 09-28 `arxiv-ai-search` 收录（列此仅为交叉引用完整数字）

---

## 4. Runner-ups

| ID | 标题 | 命中理由 | 未展开原因 |
|---|---|---|---|
| 2609.31458 | Nonparametric ICL under Growing Geometric Complexity（**NeurIPS 2026**, 63 pages） | 未知局部几何下的 ICL：**依赖样本量的流形混合**（异质维度、平滑度、采样质量）下的 **minimax 下界 + 匹配的 oracle tangent local-polynomial 估计上界**；连接到**带几何 preconditioner 的两阶段 softmax transformer**，以对数深度与多项式规模达到 minimax rate | 纯理论，`tentative` |
| 2609.30556 | Dynamic Regret in OCO with Indicator Switching Costs（**NeurIPS 2026**） | 博弈论 / 在线凸优化动态遗憾，与本库 game-rl 线相关 | 纯理论，`tentative` |
| 2609.31066 | Modeling quantum neural network gradient with RL（**NeurIPS 2026 Main Poster**） | 已知 venue；对象为 QNN 梯度建模 | 主题边缘 |
| 2609.31176 | SemNav: Semantic Navigation for Issue Localization in Code Repository | 仓库级 issue 定位的 agent 环境：Language server 解析 program 关系的 **Semantic Navigation Graph** + issue-conditioned **Semantic Cards** + 记录候选与其**证据基础**的持久 workspace | 单作者、无数字 |
| 2609.30798 | Evaluating Real-Time Voice Agents | 38 primary sources 的综述，**duplex 行为可与 duplex 架构分离** | 综述性质，核心结论已写入 §2.9 |
| 2609.31422 | Active Provenance Gate for Multi-Agent Debate Synthesis（**ICAART**） | MAD 的 final synthesis 会**捏造未被 debate 历史支撑的共识**；APG 作为 post-debate 验证层把来源当硬约束。危机仿真中 **Provenance Fidelity 翻倍以上**（困难条件下），严格 gate 阻断无支撑 claim 并生成 divergence report；人击中 **>75%** 偏好有据可查的呈现 | 危机域场景，**且已被 `arxiv-paper-check` RUN 2 收录**——仅交叉引用 |
| 2609.29578 / 2609.29014 / 2609.29875 / 2609.29518 / 2609.29960 / 2609.28653 / 2609.28682 / 2609.28798 | 见 09-28 `arxiv-ai-search` / `game-rl-daily` | 已被今日 sibling 收录 | 仅交叉引用，不重复展开 |

---

## 5. 跨主题观察 — Cross-Cutting Observations

1. **本轮最硬的一条证据链：能力缺失常常是接口缺失，不是能力缺失。** 两篇独立论文给出同一结构：*LIFT*（2609.31140，NeurIPS 2026）发现 **multimodal scaling 退化掉的语言推理能力仍完好保存在基座 LLM 里，只是对齐后的 VLM 访问不到**——用基座提取的 reasoning vector 注入，**一致优于**从 VLM 提取的；*Audio LLMs Know When They Can't Hear You*（2609.30625）发现模型**无法判断自己的转写是否可靠**（直接问它，多数时候说"可靠"），**但转写可靠性在冻结 audio encoder 表征中被强烈表征**——一个轻量探针在生成前即可预测并触发澄清。差别只在一个用向量注入、一个用探针 + clarification。`high confidence`

2. **dLLM 的"顺序灵活性"是同一枚硬币的两面。** ICML 2026 Outstanding *The Flexibility Trap*（库内，`high confidence`）证明对 dLLM 施加标准 GRPO 可把 GSM8K 提到 **89.1%** —— 任意顺序生成**限制**推理潜力；本轮 *Why Jailbreaks Succeed in dLLMs*（2609.30841）则把同一自由度解释为**能量预算**：任意顺序 = 轨迹自由度 = 越过安全势垒的动能，于是可用**三个 training-free 信号**（step-0 ratio + 两个 trajectory-velocity）检测，且**三个信号在能量预算上按构造互相覆盖盲点**。一篇说灵活性有害于能力，一篇说灵活性便利攻击且可廉价检测。`high confidence`（议题收敛）

3. **"完成的权威"必须外置——本轮有四个独立来源指向同一句。** *Who Holds the Pen?* 测出 **completion-claim 超出实际 pass rate 28.7–37.9 pp**（§3.4）；*Subjects, Not Authors* 指出 agent 既是 policy 主体又是 policy 作者，给出"**agent 是治理平面的主体，永远不是其作者**"原则，并实测**未经批准发布可反转 80 个授权决定**且只读 policy diff 的分类器必然漏掉（§2.7）；*Era by Eon* 测出隐含事实题 84 次尝试只对 2 次（§3.4）；*Evaluating Real-Time Voice Agents* 综述指出近期基准**验证后端状态而非相信 agent 自述**（§2.9）。**context 里的规范不是约束，独立的 authority boundary 才是。** `high confidence`

4. **Agent 的成本问题本轮出现了四个互补的数据点，且其中三个是负面结论。** *Cost-Inefficient Behaviors in Coding Agents*（SWE-bench Verified，1,200 轨迹）给出最诚实的一组：三类低效行为影响 **79–98%** 的任务、占成本最高 **22.75%**；但最直觉的解法 **structure-aware retrieval 让成本反涨 28.14%**，agent 自合成 skill 天花板低，只有 **developer-designed skill 降本最多 41.73%**。*Persistent Billable State* 从攻击侧给出 **6 条 denial-of-wallet 向量、14,293× 的实测计量放大**。*LLM Parkinsonism* 给出架构侧的分解：first-candidate **67.42%** → candidate-set control **96.53%** → GEC **96.57%**，**29 pp 增益几乎全部来自"能一次看到多个候选"这个接口设计**，而治理架构本身贡献描述性极小。三条负面结论（反涨、低层 skill 无效、架构贡献极小）比任何正面结论都更有信息量。`high confidence`

5. **评估方法学的"陷阱"正在被逐个命名，而本轮最狠的一篇讲的是"截断即选择偏差"。** *Completed Pairs Hide Capped Failures*（2609.31381）示范三个具体错误：只统计完成的配对**系统性删除最差情况**（被截断的运行）；aggregate −25% token 掩盖了中位数配对 **+29%** 与请求数 **35→55**；在同一批数据上 fitting 并评估 selector 会把平局读成收益（实为**多 1 次失败 + 8.6% token**）。**这直接关系到本库已收录的多个 context-compression 条目**——引用其收益数字前应先检查失败运行是否被计入。叠加 *Likelihood Ranking doesn't Scale Like Prompting*（95 模型跨 0.1B–104B 证明 likelihood 与 prompting 抽取不同能力）与 *Style, Not Self*（balanced accuracy 全部 49–58% vs raw 38–67%），本轮把"报告规范"本身变成了一类独立贡献。`high confidence`

6. **生成内容治理本轮形成了一个完整的威胁-防御-反制三角。** *Can Pixels Alone Reveal Image Origin?*（NeurIPS 2026，29 pages）给出**任何仅像素验证器的精确 best-case 极限**——最大的鲁棒 target-acceptance gap **等于** target 分布与被攻击 source 分布集合之间的**最小 total-variation 距离**，且**与验证器架构无关**；*FARE*（NeurIPS 2026）给出**权重不可见时仍可部署**的取证接受域估计，在严格工作点上一致优于基线；*The Shape of Events*（NeurIPS 2026）从机制侧证明**跨域蒸馏可被用来剥离"伪影"类特征**——而这恰是 FARE 特征的潜在威胁面。本库此前未系统覆盖"生成器变成不可见服务后的内容审计"，这一组是首个完整答案。`high confidence`

7. **"能跑 code ≠ 能做企业任务"与"离线饱和 ≠ 线上 headroom"是同一条结论的两个独立来源。** *Era by Eon* 的规则显式题上限饱和（四个最强模型各 22–25 / 27）vs 隐藏事实题 84 次尝试对 2 次（§3.4）；Netflix 的 2M→1B generative recommender 论文把 **task headroom 列为 production transfer problem 的独立分量**（§1.2）。对本库 rec 线的直接含义：**offline 指标饱和不能作为线上 headroom 的证据**。`high confidence`

8. **两处对"agentic 必然更好"的同期反例。** *TW3Cast* 不跑 agent、不跑 LM，仅凭训练划分上算一次后冻结的查表 + 基础模型轻度微调，在 GIFT-Eval mean MASE rank 上排 **130 条中的第 3**，而前两名都在 agentic category；*LLM Parkinsonism* 证明 29 pp 的 agent 增益几乎全部来自**候选动作的可见性**这一接口属性，而非治理架构。`high confidence`

9. **"压缩不是丢弃而是换形式"在本轮出现三个独立实例。** *Acoustic-to-Text KV Compression*（把声学 KV 在 listening-time slack 内蒸馏为文本 KV，peak streaming KV **−64.6%**）、今日 sibling 的 *ICLR*（冻结 proxy entropy 排序 reasoning block，token −25.5%/−14.4%/−33.3% 而 reward 0.699→0.718）、以及 *Compress What You See, Not What You Say*（anchored context distillation，2609.31430）。三者共同反驳了"压缩 = 丢信息"的默认框架。`high confidence`

10. **一个方法论模板值得单独记：把不可诊断的归纳偏置搬进可诊断的域。** *The Shape of Events* 从 event 域向 RGB 域蒸馏，从而借用 RGB 域成熟的评测工具解剖出"偏好高频纹理"这一偏置，并定位机制为**抑制高频纹理依赖、转向边缘形状依赖**，同时给出一个诚实的**频谱权衡**（对高频缺失的鲁棒性与对频带污染/几何破坏的脆弱性共存）。这一模板对本库的 rec / MoE / 世界模型线同样适用——把线上不可测的隐式偏置搬进有成熟评测的离线域。`tentative`（本轮仅一处应用，属外推）

---

## 日历（Calendar）

| 日期 | 事件 |
|---|---|
| **2026-09-28（今日）** | RecSys 2026 开幕（Minneapolis）；**NeurIPS 2026 accepted list 开始通过 arXiv comment 显形** |
| 2026-09-29 | OpenAI **DevDay 2026**（旧金山 Fort Mason，Sam Altman 出席）— 09-20 / 09-21 tech-report 记录 |
| 2026-10-02 | RecSys 2026 结束 |
| 未定 | **NeurIPS 2026 award 名单**（需核 `neurips.cc` 官方页；本轮 20 篇为 accepted 子集，非获奖） |
| 未定 | **SIGIR 2026 Best Paper 公布**（官方页仍止于 2025，`unresolved`） |
| 未定 | ACL 2026 三项 Outstanding（CURE / PolyGloss / PALU）官方 proceedings 确认 |
| 2026-10-14 / 10-15 | GPT-5.5 退役 / Step 5 权重开放（09-20 tech-report，`tentative`） |

---

## Data Quality Notes

1. **⚠️ 窗口口径已更正（最重要）**：`/list/{cat}/new` 与 `cat:` 限定查询**都不足以界定全局窗口**。cs.AI / cs.LG 当时只是没有新 primary submission，其 listing 页面因此停留在上一批。改用跨 **26 个 category** 的 category-agnostic API 扫描后得到 **638 篇 / ID 2609.30379–2609.31620**。**下轮规则：绝不用 per-category `/list` 或 `cat:`-scoped 查询界定全局窗口。**（此更正由今日 sibling 首先做出，本文采纳并在 §2 全部基于更正后的窗口。）
2. **638 → 499 → 40 的筛选链**：638 篇对照全库 **6,244 个 arXiv ID** 正则扫描 → 499 篇未收录 → 主题筛选（agent 81 / llm 141 / code 178 / bench 274 / sys 242 / gen 103 / safety 94 / seq 70 / rec_ads **10** / game 19）→ **40 篇 featured（39 独家 + 1 共享）**。缓存的 listing HTML、sweep 脚本、pool JSON 位于预批准临时目录 `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/confdig-0928/`。
3. **rec / ads 的窗口级空缺只剩"竞价"这一半（口径已更正）**：499 篇未收录论文中 `rec_ads` 模式仅 **10 命中且全部为误报**（"adversarial"、"guidance"、"economic" 等），与今日 `arxiv-ai-search` RUN 2 独立复现的 **22/22 误报率**一致。⚠️ **不要再引用"~15 个连续窗口无端到端 CTR 工作"这一说法**——今日两个 sibling 各自独立证伪并撤回了它：那是**把局部扫描当成全局界**（scope error），且与"窗口内确有 CTR 论文"自相矛盾。本窗口确有直接 CTR 工作（Target 零售商品搜索 2609.31498，线上 A/B CTR +0.97%），另有 T-RoPE / KuaFu / ESP 三个 live A/B 提升的 rec/ads 工业簇（均已被 sibling 收录）。**真正在全窗口 1,260 篇上被两次独立全量 sweep 确认的只有一件事：没有任何广告竞价 / bidding 论文**（两次 sweep 各只命中一篇加密货币 mempool 论文 2609.31379，误报）。本 digest 自身最接近 rec 语义的是 **PriceBench**（§2.2）。
4. **NeurIPS 2026 = accepted 子集，非获奖名单**：本轮 20 篇带 `Accepted at NeurIPS 2026` comment 的论文是**按 arXiv comment 抽取的样本**，既不等于完整 accepted list，也**与 award 无关**。获奖公告需核官方页。
5. **ACM DL 403**：`https://dl.acm.org/doi/proceedings/10.1145/3773078` 直接抓取返回 403。Netflix 论文的作者、机构、DOI、出版日期改由 **arXiv abs 页 + 搜索摘要交叉确认**（`high confidence`）；KDD 2026 三个 Meta 奖项仅有**二手来源**（`tentative`）。
6. **RecSys 2026 日期口径冲突**：官方 contributions 页为 **09-28 → 10-02**，本库 09-25 conference-digest 记为 09-29 → 10-01。**以官方页为准**，09-25 记录待修订；本轮未能直接抓取日程页二次确认。
7. **机构信息普遍缺失**：API 元数据不含 affiliation。除 `2609.28585`（明确打印 CAS IIE + 中国 cyber 科技大学网安学院）外全部标 `tentative`；标为特定机构者（Alibaba Qwen / UIUC / KAIST / NEC / 东北大-华为诺亚）的依据已在正文逐条说明，**未臆测**。
8. **展开标题警告**：§1.5 中 CURE / PolyGloss / PALU 的完整标题为**自拟展开**，未经官方 proceedings 确认，**不得作为正式标题引用**。
9. **强度限定**：
   - **Mutable Transcripts** 为 **n = 17** 的受控用户研究，作者自用 "initial evidence" 措辞，`single-source`，结论方向可信但**幅度不可外推**。
   - **Gemma 4 行为学评测** 为 **n = 13 items / 784 forward passes**，实验设计 counterbalance 严谨但样本小。
   - **TopoCompress / EvoTreeNAD / StructFlow-HPR / LIDAR / Agentic Detection of Online Conspiracies / DyMD / MM-VeriAgent / WALT / WeaveAgent** 未取得实验数字（摘要截断或原文未给），已标 `tentative`，**不臆造数值**。
   - **PolicyAttention** 的注册判据（1.052× oracle）与描述性数字（1.050×，无注册 margin）作者**已自行区分**，引用时须保留这一区分。
10. **⚠️ 写稿后自查发现 1 处 feature 级 sibling 重叠（已披露，未隐藏）**：本文的 0-hit 校验在 `arxiv-paper-check` RUN 2 落地**之前**完成，因此其后续声称未被计入。逐 ID 复核后：**2609.31381** 同时被 `arxiv-paper-check` RUN 2 收录（首发方），**双方独立得出同一结论（survivorship artifact）且无数据冲突**；本文保留深读并在 §2.7 加标注。**这是今日第 3 次同窗口 digest 相互碰撞**（前两次：`arxiv-ai-search` ↔ `arxiv-paper-check` 就 2609.31498 / 2609.31379 的碰撞），**根因是 `arxiv-*` 作业未串行化、各自只筛未声称残差**——**修法是 claim registry 或确定性的 claim 顺序，不是更好的筛选**。
11. **⚠️ 本轮写稿时口径落后于 sibling，已按 sibling 更正**：本文初稿仍引用"~15 个连续窗口无端到端 CTR 工作"这一说法，而它已在今日被两个 sibling 各自独立证伪并撤回（见第 3 条）。**本文采纳撤回后的口径**：窗口级空缺只在广告竞价 / bidding。此为 §2.2 与 §Data Quality 3 的更正来源。
