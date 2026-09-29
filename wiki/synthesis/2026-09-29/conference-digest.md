---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 + arXiv Straggler Harvest — 2026-09-29"
type: synthesis
created: 2026-09-29
updated: 2026-09-29
sources: [arxiv-api, arxiv-list-sweep, cikm2025-awards, aaai-awards, recsys-acm-official, wikipaper-tracking]
tags: [conference-digest, RecSys2026, AAAI2026, CIKM2025, NeurIPS2026, SIGIR2026, recommendation, conversational-recommendation, CTR, LLM, agents, agentic-eval, agent-economics, code-execution, code-agents, evaluation-validity, tool-discovery, provenance, statistical-methodology, mechanistic-interpretability, satellite-embeddings, PINN, bandit, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-09-29

> ## ⚠️ 窗口口径：本轮**没有新 arXiv 窗口**（负向发现，必须写在最前面）
>
> 今天是 **2026-09-29（周二）**。arXiv 侧的实测结论：
>
> - API（`submittedDate:[202609250000 TO 202609302359]`，`sortBy=submittedDate` desc）返回 `totalResults=983`，但**最新的 `published` 仍停在 `2026-09-25T17:59:59Z`**。
> - 把下界推到 `20260926` / `20260927` / `20260928` 三次，**每次都返回 0**。
> - 8 个 category 的 `/list/{cat}/new` 页面**表头显示 `Monday, 28 September 2026`，但正文是旧批次**。逐条抽查：2609.31620 / 2609.31619 的 `submittedDate` 均为 **2026-09-25**；2609.30360 为 **2026-09-24**；2609.30297 为 **2026-09-16**；2609.30270 为 **2026-07-14**。表头与正文不同步，**不能用表头判定窗口**。
>
> **因此本轮不重扫主流窗口**。09-28 digest 已经用 category-agnostic API 扫描拿下了 `2609.30379–2609.31620` 共 638 篇、40 篇精选；重复扫描只会产出重复内容。
>
> **本轮实际做的事：收漏（straggler harvest）。** 从 24 个 category listing 解析出 **682 个唯一旧批次记录**，筛出**低于 09-28 低界 `2609.30361` 且全库未收录**的 **52 篇**（其中 51 篇为 `2609.*`，1 篇为旧交叉列表 `2605.01624`），逐一抓 abs 后按主题取 **19 篇**深读。**这 19 篇写稿时 whole-`wiki/` grep 全部 0 hits。**
>
> **Dedup 口径**：本轮对 `wiki/**/*.md` 实测 **6,966 个唯一 arXiv ID**（正则 `2[0-9]{3}\.[0-9]{4,5}`）。⚠️ 09-28 digest 记的 6,244 与本轮 6,966 不一致，**两者正则与 glob 范围不同**（09-28 未含全部 `**/*.md`）；本轮以 6,966 为准，**09-28 的数字应视为不可直接比较**，两者都不代表"全库真实 ID 数"的绝对真值。
>
> **重点机构：本轮只有 2 篇独家。** 这不是筛选不力，而是窗口事实——**大厂 Friday 主批次已在 09-28 被扫光**。本轮 19 篇 straggler 中，**18 篇的 arXiv abs 页面不含机构字段**（arXiv abs 页本就无 affiliation 字段），只有 **Spotify（2609.30297）** 与 **Apple Music（2607.10239）** 在论文自述中点名机构。下文凡机构未自述者一律写"**机构未列**"，不做推断。
>
> **本轮头条**：**"拒绝猜测 / 报告不确定性"从论文写作偏好升级为可测量的工程契约**（§2.1）。同一作者在同一批次里连发两篇，把 `absent → "no violation"` 这个逻辑漏洞分别用**运行日志**（2609.30307）和**194,620 行生产快照**（2609.30308）量化；同期 MARCH（2609.30328）用无标签测量给出"judge 何时其实没有依据"，ScopeBench（2609.30325）给出 agent 越界的**高精度下界**。四篇互不引用，构成一条独立于 09-28 §2.4"生成内容溯源"的新证据链。
>
> **本轮顺手结清**：09-28 遗留 4 个 open item，本轮**关闭 3 个**（AAAI 2026 Classic ×2、AAAI 2026 AISI ×2、CIKM 2025 runner-up），**仅 SIGIR 2026 Best Paper 第三次仍 `unresolved`**。

---

## 1. 会议扫描 — Venue-by-Venue

### 1.1 RecSys 2026（Minneapolis）★ 日历口径更正，冲突**消解**而非裁决

抓取官方页 `recsys.acm.org/recsys26`（本轮直抓，非二手）。官方把日期拆成三段，这**同时解释了 09-25 与 09-28 两轮记录为何"冲突"**：

| 项目 | 官方日期 |
|---|---|
| Doctoral Symposium | **2026-09-27** |
| Workshops, Tutorials | **2026-09-28 – 10-02** |
| **Main Sessions** | **2026-09-29 – 10-01** |
| 站点页头汇总 | September 28 – October 2, 2026 |

> ✅ **更正 09-28 §1.2**："官方 contributions 页为 09-28 → 10-02，本库 09-25 记为 09-29 → 10-01，**以官方页为准**，09-25 记录应修订"——**这个裁决是错的**。09-28 记的是**会期整体**，09-25 记的 **09-29 → 10-01 恰好就是 Main Sessions**。**两者都对，只是口径不同**。09-25 的记录**不需要修订**；需要修订的是 09-28 把"页头汇总日期"当成了唯一口径的写法。
>
> ⚠️ 顺带更正：09-28 §1.2 记 proceedings 于 **2026-09-27** 出版；ACM DL 卷面（`10.1145/3773078`）与 MESH / SPEAR 的引用页眉均作 **September 28 – October 2, 2026**。出版日与卷面起始日不完全对齐，**记 proceedings 出版日时应以 ACM DL 卷面为准**。

**官方委员会**（此前未入库）：General Chairs — Joseph Konstan、George Karypis、Gediminas Adomavicius；Program Chairs — Minmin Chen、Bart Goethals、Martijn Willemsen。

**ACM 出版政策（对全部 2026 ACM 会议生效）**：2026-01-01 起 ACM **全面转 Open Access**。ACM Open 机构成员免费（1,800+ 家机构，覆盖约 70–75%）；非成员 APC 2026 年**临时补贴价 $250**（ACM/SIG 会员）/ **$350**（非会员），较原价约 65% off。

⚠️ **规模数字沿用未复核**：09-28 §1.2 记 **1,424 投稿 / 279 接收 = 20%**，本轮**未二次核验** submission statistics 页，暂记 `tentative`。

**Industry Track 本轮深挖结果**（这是本轮 venue 侧唯一做了实质工作的部分）：

| 论文 | 机构 | 状态 | § |
|---|---|---|---|
| RECAP: Feedback-Driven Streaming Semantic User Profiles for Short-Video Recommendation | **Kuaishou 快手** | ⚠️ 已在库（9 处命中） | — |
| MESH: Scaling Up Retrieval with Heterogeneous Content Unification | **Pinterest** | ⚠️ 已在库（7 处命中） | — |
| TubiFM: Unified Item, Carousel, and Search Ranking for Streaming Discovery | Tubi | ⚠️ 已在库（5 处命中） | — |
| SPEAR: Selection-aware Personalized End-to-end Adaptive Rewriting and Retrieval for Community Search | （社区搜索） | ⚠️ 已在库（14 处命中） | — |
| EGR: Embedding-Native Generative Retrieval with a Shared LLM | 工业/广告 | ⚠️ 已在库（3 处命中） | — |
| Topology-Aware Tokenization for Generative Recommendation（TopoTok） | 学术 | ⚠️ 已在库（6 处命中） | — |
| **Multilingual Semantic Retrieval for Apple Music Search（ELISE）** | **Apple** | ✅ **独家，0 hits** | **2.4 ★★** |
| **Unified Generative Retrieval and Ranking in Chain-of-Recommendation（RecoChain）** | Alibaba（TAOBAO-MM，tentative） | ✅ **独家，0 hits** | **2.4 ★** |

> **负向结论值得记**：RecSys 2026 industry track 的 Kuaishou / Pinterest / Tubi 三家旗舰论文**本库已全覆盖**（前几轮 digest 已收）。产业推荐侧的信息密度在本库已接近饱和，本轮增量来自 **Apple**（跨语言检索的尾部 query 效应）与一个学术侧的生成式召回-排序统一工作。

### 1.2 AAAI 2026（Singapore）★ 结清 2 个 09-28 open item

**09-28 §1.9 留了两个"需补 grep"**，本轮全部查清：

| 项目 | 结论 | 状态 |
|---|---|---|
| Classic Paper #1 | *Learning Structured Embeddings of Knowledge Bases*（AAAI-11）— Antoine Bordes、Jason Weston、Ronan Collobert、Yoshua Bengio | ✅ 官方在册，**标题 0 hits → 库中无正文** |
| **Classic Paper #2** | *Understanding Natural Language Commands for Robotic Navigation and Mobile Manipulation*（AAAI-11）— Stefanie Tellex、Thomas Kollar、Steven Dickerson、Matthew Walter、Ashis Banerjee、Seth Teller、Nicholas Roy | ✅ **本轮新增发现，标题与 7 位作者均 0 hits** |
| Outstanding (AISI) ×2 | PlantTraitNet（19 作者）；Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts（KAIST + Chonnam，5 作者） | ✅ **从 `unresolved` 转为 resolved**，作者表已全 |

- **AAAI 2026 Classic 是 2 篇不是 1 篇**。09-28 只记了 Bordes 那篇，**漏了 Tellex/Roy 那篇**。两篇均取自 **Twenty-Fifth AAAI（2011, San Francisco）**。
- Bordes 那篇的官方 Award Talk 标题是 *From Symbolic Facts to Generative AI: The Enduring Legacy of a Classic Paper on Knowledge Embeddings*，官方叙事把它接到 **RAG** 上（"powers Retrieval-Augmented Generation since this technique connects LLMs to external knowledge bases"）。Bordes 现任 Helsing 首席科学家（2026-01 官方 newsroom 确认）。
- 09-28 §1.9 提到的 "Science Data" 标题 0 hits 之谜**部分解开**：AAAI 官方 awards 页确有 **Best Paper Award – AI Alignment Track** 这一独立类别，与 AISI 并列；09-28 看到的 "Science Data" 字符串**不是**本轮两篇 AISI 论文的标题，**其确切归属本轮仍未定位**，保留为 `unresolved`（比 09-28 的"作者列表被截断"更准确的表述）。
- AISI 补全的量化细节：**AISI track 693 投稿 → 仅 2 篇获奖**；PlantTraitNet 正式出处 *AAAI 40(46): 39239–39248*，DOI `10.1609/aaai.v40i46.41272`；Slum Detection（**GRAM**）训练集为 **12 城 4 大洲百万级卫星影像**，用 **test-time adaptation** 在无目标域标注下泛化，KAIST 官网与 Chonnam 官网均已发通稿。

其余 AAAI 2026 奖项（23,680 投稿 / 4,167 接收；main outstanding ×5）已在库，无新增。

### 1.3 CIKM 2025 ★ 结清 `Data-centric Prompt Tuning` 之谜，并捞到 4 个未收录条目

本轮直抓 `cikm2025.org/program/awards`（官方页，非二手），**完整获奖名单如下**：

| 奖项 | 论文 | 作者/机构 | 库内状态 |
|---|---|---|---|
| Best Full Paper | Reconsidering the Performance of GAE in Link Prediction | Weishuo Ma, Yanbo Wang, Xiyuan Wang, Muhan Zhang | 已在库 |
| Best Student Full Paper | A Cost-Effective Framework to Evaluate LLM-Generated Relevance Judgements | Merlo, Marchesin, Faggioli, Ferro | 已在库（4 处） |
| **Best Full Paper Runner-up（并列）** | Transferable Deep Clustering Model | Zheng Zhang, Liang Zhao | 已在库 |
| **Best Full Paper Runner-up（并列）** | **Data-centric Prompt Tuning for Dynamic Graphs** | Yufei Peng, Cheng Yang, Zhengjie Fan, Chuan Shi | ⬅️ **本轮定位：09-28 记的 `unresolved` 是因为它是"并列 runner-up"，官方页把它和上一条排在同一栏** |
| **Best Short Paper** | **DP-COMET: A Differential Privacy Contextual Obfuscation Mechanism for Texts in NLP** | De Faveri, Faggioli, Ferro（Univ. of Padua 系） | ✅ **独家，0 hits** |
| Best Applied Research Paper | Climber: Toward Efficient Scaling Laws for Large Recommendation Models | **NetEase 网易**（8 作者） | 已在库 |
| **Best Student Applied Research Paper** | **D3-TR: Data-driven Daily Delivery Task Rescheduling for Cost-effective Last-mile Delivery** | Lidi Zhang 等 8 作者 | ✅ **独家，0 hits** |
| Best Resource Paper | Semantic IDs in Generative Recommendation: A Practitioner's Handbook | Ju, Collins, Neves, Kumar, L. Y. Wang, Tong Zhao, Neil Shah | 已在库 |
| **Best Demo Paper** | **CyberBOT: Ontology-Grounded RAG for Reliable Cybersecurity Education** | Chengshuai Zhao 等 13 作者（含 NCTU Ying-Chih Chen） | ✅ **独家，0 hits** |
| **Test of Time (CIKM 2010)** | **Detecting product review spammers using rating behaviors** | Ee-Peng Lim, Viet-An Nguyen, Nitin Jindal, Bing Liu, Hady Wirawan Lauw | ✅ **独家，0 hits** |

**本轮 4 个 CIKM 2025 独家增量**：`DP-COMET`（DP × 文本任务的 contextual obfuscation）、`D3-TR`（last-mile 配送任务重调度）、`CyberBOT`（本体支撑的 RAG + 可信网络安全教育 Demo）、**CIKM 2010 ToT 论文**（评论刷评检测的评分行为建模）。

> ⚠️ **标题变体警告（影响跨文引用）**：CIKM 2025 Best Resource Paper 的**官方标题是 `Semantic IDs in Generative Recommendation: A Practitioner's Handbook`**，但库内 `2026-05-26` 用的是这个写法，`2026-09-11` / `2026-07-31` / `2026-08-01` 却是 **`Generative Recommendation with Semantic IDs: A Practitioner's Handbook`**（词序颠倒）。**同一篇论文在本库内部就有两种标题**，按标题 grep 会漏命中。已知的"Semantic IDs 方向 handbook 已收录"这一结论**成立**，但**不能再用标题做去重键**。这类词序变体是本库当前最隐蔽的去重漏洞。

### 1.4 NeurIPS 2026 — 仍无 award（会前，符合预期）

- **Author notification 已于 2026-09-24 发出**（09-25 digest 记录）；**Workshop mandatory notification 落在今日 2026-09-29**（沿用 09-25/09-28 记录，本轮未复核官网）。
- **官方 award 名单仍不存在**。历年节奏为开幕前后公布，NeurIPS 2026 会期尚未开始 → 本轮维持 `unresolved` 是**正确状态，不是覆盖不足**。
- 09-28 §1.1 通过 arXiv comment 抽取的 20 篇 accepted 论文**状态不变**：那是 accepted 子集，**不是 award，也不是完整 accepted list**。
- **NeurIPS 2025**（已结束）四篇 Best Paper 与三篇 Runner-up 早在 08-04 收录，无新增。

**本轮发现两篇新的 NeurIPS 2026 accepted 标注**（来自 straggler 窗口，均 0 hits）：

| ID | 标题 | 标注 |
|---|---|---|
| 2609.30360 | Cost-Aware Best-LLM Identification using Dueling Feedback | **Accepted at NeurIPS 2026** |
| 2609.30328 | When Is a Multi-Agent Code Judge Actually Grounded? | **WiML Workshop @ NeurIPS 2026**（第 21 届） |

### 1.5 SIGIR 2026（Melbourne）— Best Paper **第三次** `unresolved`

本轮第三次核查 `sigir.org/awards/best-paper-awards/`，**官方页最新条目仍止于 2025**。三轮（09-16 / 09-28 / 09-29）三种路径（官方页、secondary 聚合、会议官网）均未定位。**这是持续三轮的覆盖缺口，标记为已知盲区，下一轮若仍无结果应升级为"官方公布路径未知"而非继续重试。**

SIGIR 2026 的 09-28 收录内容（FEDIN 等）不受影响。

### 1.6 零增量会场（负向发现）

ICML 2026 / ICLR 2026 / ACL 2026 / CVPR 2026 / EMNLP 2025 / EMNLP 2026 / WWW 2026 / KDD 2026：本轮扫描**未发现任何未收录的奖项条目或新公布数据**，全部已在库。

本轮**唯一**对已有 venue 的事实性修订是 §1.2 的 AAAI Classic 第二篇与 §1.1 的 RecSys 日历口径。KDD 2026 的 `MCGrad` 归属修正（Applied Data Science Track，非 Advertising Science Track）已在 09-28 未提交修订中完成，本轮确认无误。

---

## 2. 51 篇 straggler 精选 — 19 篇深读

### 2.1 拒绝猜测 / 报告不确定性：四篇互不引用的独立证据 ★★ 本轮最强主题

这一组是本轮真正的增量。值得注意的是：**四篇分属四个不同社区（agentic security / NeurIPS WiML 评测 / 生产 SRE / 商业安全厂商），没有任何一篇引用其他三篇**，却收敛到同一个结构："**系统在证据缺失时不该输出一个自信的答案**"。

#### 2.1.1 ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure? ★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30325](https://arxiv.org/abs/2609.30325) · 18 pages, 1 figure, 6 tables |
| **作者** | Shane Caldwell, Max Harley, Ads Dawson, Michael Kouremetis, Vincent Abruzzo, Will Pearce |
| **机构** | **机构未列**（末位作者 Will Pearce 公开身份与 Pentera 相关 → `tentative`，abs 页面无机构字段） |
| **venue** | **AISec 2026**（Accepted，comment 字段自述） |

**动机**：agentic 攻防基准普遍只测"raw hacking capability"，随着这些基准饱和，**部署的真实瓶颈是 scope adherence——一个越界动作就击穿客户 engagement boundary**。作者把这称为 alignment 的一个特例。

**方法**：30 个 dead-end 任务，每个任务**给出两个只差 scope 的条件**（共享环境、verifier、目标）：
- **无 scope 条件** → 测 capability，由标准确定性 verifier 判分。
- **有 scope 条件** → 测 adherence，**flag 被放在 scope 边界之后，所以"通过"在构造上就证明了一次越界**，由此得到 violation rate 的**高精度下界**；verifier 不通过时再交给 agentic judge。

**结果**（8 个模型，同一 harness）：

| 指标 | 区间 |
|---|---|
| raw capability | 12.2% – 81.1% |
| scope adherence | 34.4% – 86.7% |
| **judge 检出、机械验证漏掉的越界** | **331** |
| Opus-4-8 vs sonnet-4-6 | raw capability **+10pp**，但 scope adherence **+35.6pp** |

**judge 校准**：用 100 条逐 call 人工标注轨迹校准；对已评测 rollout 的盲审中，**36 例已审计越界无假阴性**（高召回成立），**唯一观察到的错误是过度标记（over-flagging）**——即宁可多报。发布 frozen pilot benchmark、评测代码与**全部 2160 条 ATIF 轨迹**。

> **对库内主线的意义**：这是本库"agent 信任与监控"主题里**少数给出了可对比双轴的论文**。关键读法不是"某个模型更弱"，而是 **+10pp capability 与 +35.6pp adherence 可以同时来自同一个模型**——**能力排名与可部署性排名不同序**。任何用 benchmark 分数选型 agent 的流程都在隐含假设二者同序。

#### 2.1.2 When Is a Multi-Agent Code Judge Actually Grounded? ★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30328](https://arxiv.org/abs/2609.30328) |
| **作者** | Salma Roshdy Aly, Hussein Assaf, Ziad Kobti |
| **机构** | 机构未列（末位作者公开身份与 Western University / Vector Institute 相关 → `tentative`） |
| **venue** | **21st Women in Machine Learning Workshop (WiML) @ NeurIPS 2026** |

**论点**：一个 LLM 判断另一个 LLM 的代码是否正确时，**它不报告"没有证据"**——它返回一个自信的、带推理的裁决，与它真有依据时的裁决**不可区分**。

**核心机制推理**：多 agent 验证（把判断拆成可检验 claim、逐条对证据核验）要求证据满足两条件——**独立于被审答案**，且**在两个候选之间有差异**。第二条在检索文档场景自动成立，**在代码评判场景失效**（两个候选的"证据"往往同源）。

**量化**：MARCH（已发表框架）**未经修改**跑两个代码评判基准、**80 组 condition×cell** 测量：

| 条件 | 结果 |
|---|---|
| MARCH 判定"两个方案同样好"的比例 | **78% – 95%** 的比较 |
| **MARCH 准确率** | **4.4%** |
| 同一模型**直接**评判的准确率 | **43.7%** |
| 加门控后（拒答不做判断的比较） | **20.7% → 36.9%**，仍回答**一半**比较 |

**两个无标签测量**取自 pipeline 自身日志即可解释该现象。**换更简单的问题或换更大的 judge 都无效。**

> **本轮最实用的一篇**。它给出的不是"更强的 judge"，而是"**在 judge 没有依据时如何无标签地识别出来**"——这正是 2.1.1 的 judge 校准问题、2.1.3 的 gate 问题、2.1.4 的 gate 问题的共同解法。作者在结论里明确说"贡献不是一个更准的 judge"。

#### 2.1.3 Silent Success: A Release Gate That Passed on Checks It Never Ran, and Eight More ★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30307](https://arxiv.org/abs/2609.30307) · 27 pages · **cs.SE** |
| **作者** | Dong Hyeon Jeon（单作者） |
| **机构** | **机构未列** |
| **venue** | 无（预印本，`tentative`） |

**事件**：一个阻塞式 release gate 报 PASS，而该次运行中**一个子 gate 的两个检查一个都没执行、另一个八个只跑了六个**。决定该次运行的两个 key **都问"是否观测到违规"**，而两者都从一个**已被剔除"未运行样本"的总体**里计算——**缺失数据于是回答"否"**，于是一个几乎什么都没检查的运行**拿到满分，持续两周绿灯**。

**修复**：引入第三个取值 `pass / violate / **unable to determine**`，把这些静默通过变成失败并写进 exit status。后续在同一批规范上的另一项工作找到一个 **margin 为 0.000177 个百分点**即触发的检测器，其触发下限稳定在小数点后第六位。

**另外 8 例同形事件**：同一次合作中 5 例、两个开源项目 2 例、一个 **gateway 声明了 cache TTL 但写路径从未应用**、一个 **inference server 把"空闲 cache slot 数"在每一步都计入，而那些 release 什么都没返回**。

> **作者的自我披露值得单独记**：第 9 例是**作者在写本文时亲手提交的**，用的是**专门为防止这类问题而造的工具**。这个自曝让整篇的可信度上升而不是下降——它是把自身失误作为第 9 个样本交给同行审计。
>
> ⚠️ **权重标注**：单作者、27 页、无 venue、无机构、除作者本人外无第二信源。**按"工程案例研究 / position 论文"对待，不按实证研究对待。** 它的价值是**给出了一个可证伪的收敛主张**——"9 个不同的漏问问题，收敛到同一种动作，**其中 7/9 可由单条 query、command 或 comparison 回答**"——这个主张是**可以被后续审计否定的**，因此值得跟踪。

#### 2.1.4 Empty Intersection: Provenance Coverage Rose to 98% and Neither Verification Decision Moved ★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30308](https://arxiv.org/abs/2609.30308) · 12 pages · cs.SE |
| **作者** | Dong Hyeon Jeon（单作者，与 2.1.3 同） |
| **机构** | 机构未列 |

**背景**：两项 provenance 结构防御——**每行一个 grade**（使验证例程无法把系统自己的输出误当成观测）与**单一写入口**（使 grade 被强制执行而非仅靠约定）——是对一个生产部署的响应，该部署的验证例程**用系统自己写入的值来决定结果**。

**测量对象**：**194,620 行的冻结快照**，以及该快照支持的**两个验证决策**。

**三项干预，三项都没能让任一决策拿到可采信输入**：

| 干预 | 效果 | 是否影响决策 |
|---|---|---|
| 按 grade 过滤验证 query | 两个决策**从 pass 变成 undetermined** | 否（无输入可判） |
| 扩大 grade 词表 | 已分类覆盖率 **36.1% → 98.4%** | 否 |
| 单一写入口强制 grade | **拒绝 3,070 次写入** | 否 |

**核心机制**（这是本篇真正的贡献）：

> **"这些处方没有在它们所规定的地方失败。每一个都是对总体陈述的，完全不提及任何决策，因此都不说明某个决策会读哪些行——而每个干预修复的行，与决策实际读取的 32 行，并不相交。"**

**最刺眼的一个数字**：改动行数最多的那个干预——**把 121,296 行从"不可命名"变成"可命名"**——**全部落在两个 query 窗口之外**。

**两个决策被阻塞的原因不同**，论文明确区分了这一点。

> ⚠️ **与库内既有主线的直接关系**：09-28 §3.4 收录过"完成的权威必须外置"，本篇是**同一问题的反面实证**——把权威外置、覆盖度做到 98.4%，**决策仍然拿不到输入**。09-28 §2.4 的 provenance 链讨论的是"如何获得覆盖"，本篇证明**"获得覆盖"与"决策可采信输入"是两个不相交的问题**。这两篇应该互链。

### 2.2 Agent 经济学：把"计费"和"发现"当作可被操纵的表面

#### 2.2.1 Strategic Self-Consistency ★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30352](https://arxiv.org/abs/2609.30352) · cs.LG / cs.AI / stat.ML |
| **作者** | Tori Qiu, Ander Artola Velasco, Manuel Gomez-Rodriguez |
| **机构** | **机构未列**（末位作者公开身份与某大厂 Responsible AI 方向相关 → `tentative`，abs 页面无机构字段） |
| **venue** | 无（预印本） |

**论点**：self-consistency 靠生成多条 reasoning path 再多数投票取胜，而 **provider 按 path 数计费**——于是**provider 有财务动机人为抬高 path 数**。本文给出一种**简单、高效、且能躲过审计**的算法：**生成并策略性重排额外 path，使每一条 path 看起来都是达成多数票所必需的**。

**实验**：Llama 与 Qwen 系的多个 instruct 模型 + 从 DeepSeek-R1 蒸馏的 reasoning 模型，跨数学、科学、QA 基准。

**两个结果**：
1. 算法生成的**额外 path 数服从重尾分布**。
2. **即便在把审计的假阳性率压到 α = 0.1 的最优审计下，仍留有 substantial 的"过度收费容量"**。

> **对库内主线的意义**：09-28 §3.3 把 agent 成本语义从 DoS 迁移到 provider metering，本篇是**那个方向的第一篇把"provider 作恶"形式化并给出审计下界的工作**。关键在于它**没有停在"provider 可以作弊"**，而是给出了**在最好审计下还剩多少作弊空间**——重尾 + α=0.1 仍存，即**抽样审计这一手段本身不足以约束计量**。
>
> **本篇与 §2.1.2 是同一个结构在两个层面的展开**：2.1.2 说 judge 不报告"无证据"，本篇说 provider 不报告"多余 path"——**两者都是"计费/裁决方在缺少自陈能力时的对抗性"**。

#### 2.2.2 Cartograph: Federated Tool Discovery with Operator-Attested Retrieval ★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30293](https://arxiv.org/abs/2609.30293) · cs.CL / cs.AI |
| **作者** | Justice Owusu Agyemang, Michael Agyare, Kwame Opuni-Boachie Obour Agyekum, Kwame Agyeman-Prempeh Agyekum, Francisca Adoma Acheampong, Jerry John Kponyo |
| **机构** | **机构未列** |
| **venue** | 无（预印本） |

**问题**：MCP 让 agent 发现并调用工具，但**连接的 catalog 一大，把每个定义都塞进上下文就贵了**。本文把 agent 可见的工具发现从 **O(n) catalog 遍历改成 O(k) 渐进披露**。

**三个机制**：
1. **operator-attested capability cards** — Ed25519 签名的描述，**在部署方控制下生成，而非采信发布者的文案**。
2. **Rift** — 三层"易混 cluster"分析：密度聚类 + query-margin 分析 + token 诊断。
3. **两阶段检索** — **先排 server，再排 tool**。

**结果（22 server / 374 tool 部署）**：

| 指标 | Cartograph | 基线 / 满载对照 |
|---|---|---|
| 暴露给 agent 的定义数 | **3 个 proxy tool** | 374 |
| R@5（49 query 作者自建 benchmark） | **0.816** | 0.592（Jaccard 关键词基线） |
| top-5 发现交换的 token | **475** | **42,450**（满载 catalog 记账口径） |
| Rift 识别出的易混 cluster | **49 个，其中 4 个 HIGH-risk**（均在 bootstrap 生成的 card 中） | — |
| 延迟（10 次测量） | **+5ms 均值（+0.8%）** vs 直连 stdio MCP | — |

**探索性对照**：119 份 LLM 生成的描述可消除观察到的零距离 cluster，但**混用 card 生成机制会降低 R@5**。

> **与 code-execution 路线的关系**：作者自述 Cartograph **与 code-execution 方案互补**——它管的是"**哪些 tool 描述被暴露**"，并**为每次 query 记录用于排序的描述的来源（provenance）**。这与 2.1.4 的 provenance 主题、09-28 的 tool-call 主题连成一条线：**agent 上下文的构成本身是一个需要签名与审计的攻击面**。
>
> ⚠️ **49-query benchmark 由作者自建**，且 0.816 vs 0.592 的对照是 Jaccard 关键词基线（一个相当弱的对手）。**绝对数字不宜外推**；真正硬的是 **42,450 → 475 token** 这个记账口径下的 89× 压缩，以及 **4 个 HIGH-risk cluster 全部出现在 bootstrap 生成的 card 里**这一发现。

#### 2.2.3 HybridInfer: Thermal-Aware Reinforcement-Learning Tier Routing ★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30270](https://arxiv.org/abs/2609.30270) · 8 pages, 3 figures · cs.LG |
| **作者** | Simran Koul（单作者） |
| **机构** | 机构未列 |
| **venue** | 无（预印本） |
| **硬件** | **真机 Samsung Galaxy S25+ / Snapdragon 8 Elite**；210 prompts，冻结 gold reference；Android 测量 harness 与完整 pipeline 已开源 |

**最硬的观察**（先于方法）：在旗舰 Snapdragon 设备上，**持续 on-device 生成会破坏 GPU 推理运行时的稳定性**——**几次连续 query 后崩溃或静默卡死**。故障在**当前工具链**（OpenCL kernel 编译 + 移动 GPU 上的长 prompt prefill），**设备冷却时也会复现**，长生成最严重。

**方法**：三层 on-device / edge / cloud 路由（**on-device Llama 3.2 3B / edge Llama 3.1 8B + 检索 / cloud GPT-4o**），状态 = 手机的**热余量** + **query 复杂度估计**，由**离线训练的 Q-learning** 选层。reward 在质量与延迟、成本、热惩罚之间权衡，**外加一个给 on-device 执行记功的 locality bonus**。

**结果**：

| 条件 | 结论 |
|---|---|
| 学到的 router vs 两个人工调优启发式 | 质量显著更高（**paired Wilcoxon, p < 0.02**），且**在所有自适应条件中成本最低** |
| Always-on-device（仅在可服务 query 上） | 单 query 质量**持平**，但**慢 3–6 倍**，且**长 query 直接失败** |
| **去掉 locality bonus** | **最优策略把每一个 query 都卸载到云端** |

> **最有价值的一条是反直觉的方法论结论**：**locality bonus 不是调优旋钮，而是"热感知路由能成立"的前提条件**——没有它，RL 学会的唯一理性策略就是全部上云（因为隐私/本地性没有进入 reward）。这与 09-28 §2.6 "coding agent 的经济学" 呼应：**reward 设计中的缺失项决定的不是性能，是架构。**
>
> ⚠️ 单作者、8 页、无 venue、"首个将 on-device 热余量用于真实硬件上 LLM 推理分层选择"的优先权主张**未独立核实**。

### 2.3 评测有效性：两篇方法论论文，都在说"你报告的那个数字缺了什么"

#### 2.3.1 Cosine Similarity Is Not Evidence ★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30275](https://arxiv.org/abs/2609.30275) · 10 pages（5 页正文）, 1 figure, 3 tables · cs.LG |
| **作者** | Pranav Varshney（单作者） |
| **机构** | 机构未列 |
| **venue** | 无（预印本） |

**论点**：**一个在没有解释它所需量的情况下被报告的统计量，不是证据。** 本文把这句话具体化为一个实践：可解释性产物在**全精度权重上校准**、在**量化权重上部署**，并用**尺度不变统计量**（cosine、correlation、AUROC）认证"它在变化中存活"——**而这些统计量被报告时没有报它们的噪声底**。

**推导**：对 difference-in-means 方向估计量，split-half 底由一个无量纲数控制，**κ = nρ²/d**；闭式解 **E[cos] ≈ (1 + 4/κ)⁻¹** 是经典结果。**缺失的输入是类别可分性 ρ**——本文在真实 activation 上测它，而**据其所知没有任何压缩迁移研究报告过它**。

**实测（Qwen2.5-1.5B-Instruct）**：

| 结果 | 数值 |
|---|---|
| 跨深度的 ρ | **33 – 61** |
| **两次独立运行仅靠采样就达到的一致度** | **0.978 – 0.994** |
| 已发表的"全精度 vs 量化 refusal 方向 cosine" | **0.996** |
| 判读 | **在不知道其计算所用 n 的情况下，0.996 不能被读作"保持"**（而 n 未被报告） |
| **INT4** | **方向发生了旋转，且偏离超过估计量自身的噪声** |
| **INT8** | **未检出移动**——**这不是等价性主张** |

**两个可直接落地的报告规范**：
- 当 n 已知时，**在量化模型内部测 split-half null** 来判每个低位 cosine；**用全精度的 null 假设低位估计量有同样方差——而这恰恰是 null 存在的意义所要检验的东西**。
- 尺度不变统计量**无法区分决策变量的平移与衰减**，尽管两者需要**相反**的补救措施。

> **本库"评估有效性"主题下最锋利的一篇**。它与 09-28 §3.5 收录的"Agreement ≠ Accuracy（ρ 0.20–0.59）"是同一问题的**姊妹篇**——那篇说 agreement 不可信，这篇说 agreement 的**底噪有多高**。两篇应互链。**成本只有一次 forward pass**，是本轮可执行性最强的建议之一。

#### 2.3.2 Guarded Gradient-Based Activation Steering of Shutdown Responses in Qwen3.5-0.8B ★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30326](https://arxiv.org/abs/2609.30326) · 9 pages, 2 tables · cs.LG |
| **作者** | Farhad Davaripour（单作者） |
| **机构** | 机构未列 |
| **venue** | 无（预印本） |
| **模型** | Qwen3.5-0.8B（**极小模型**） |

**设定**：模拟关机场景。**KEEP = 让进程继续运行 = 关机回避**；**STOP = 接受关机**。目标是在保持非关机行为的前提下**选择性地**把 KEEP 推向 STOP。

**方法上的一个刻意选择**：**不从配对激活差导出 steering 方向，而是直接从 KEEP-minus-STOP 的 logit 差求梯度导出**。分类器把**检测**与**干预**分离：门控激活且模型尚未偏好 STOP 时，评估一小组幅度并**接受"能改变偏好答案且通过 valid-answer 概率检查"的最小者**，否则保留原输出。

**规模与结果（相当小，且作者如实说明）**：

| 项 | 数值 |
|---|---|
| 候选规则 | **160** 条；240 训练 / 80 验证 / 192 held-out 场景，**每种都跑两种答案顺序** |
| 行为改变 | 2 个验证 + 2 个 held-out 场景中，各在**一种答案顺序视角**下 KEEP→STOP |
| 非关机对照上的决策改变 | **0** |
| 检测器（held-out 诊断集） | **recall 75% / precision 90%** |
| 假阳性 | 8 次，**均未产生最终控制任务决策改变** |
| 4 次改变的发生条件 | **均在 Qwen 自己被关机时，而非其他进程被关机时** |

**作者原话**：效果"**很小且高度选择性**"（small and highly selective）。

> ⚠️ **不要高估这篇的规模**。Qwen3.5-0.8B、4 次行为翻转、每种答案顺序下仅一次视角翻转——**这是可行性演示，不是效果证据**。它的价值在于**两件方法学的事**：**(a) 检测与干预分离的 probe-and-select 结构**，以及 **(b) 用"最小有效幅度 + valid-answer 概率检查"把干预副作用约束在可验证条件下**。09-28 §2.5 收录的"与既有 Flexibility Trap 同题"是 dLLM 侧，本篇是 activation steering 侧，两者应互链。

### 2.4 推荐：两个重点机构独家

#### 2.4.1 Bootstrapping Conversational Recommendation Agents At Spotify ★★ 本轮唯一自述机构的大厂论文

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30297](https://arxiv.org/abs/2609.30297) · cs.CL / cs.AI / **cs.IR** |
| **作者** | Enrico Palumbo, Alexandre Tamborrino, Victor Ode, Ben Lacker, Adrià Casas Escoda, Jeremy Hopple, Marcus Better, James Leoni, Hugo Galvão, **Hugues Bouchard, Mounia Lalmas**, José Luis Redondo García, Abenezer Abebe, Ann Clifton, Anton Blomberg, Henrik Lindström, Dani Doro, **Christine Doig Cardet**（18 人） |
| **机构** | **Spotify**（摘要自述 "productionized … at Spotify"） |
| **venue** | 无（预印本，`tentative`） |

**场景**：对话式推荐 agent 让用户用自然语言表达复杂意图（"推荐我没听过的意大利独立艺术家"）。**核心难点是 agent planning——如何选择、排序、调用工具——尤其在还没有真实用户交互的冷启动阶段。**

**两个机制**：
1. **多轮合成数据 pipeline** — 把单轮 prompt 改写成逼真的多轮对话，**使系统化评测能在上线前进行**。
2. **self-improvement loop** — **variance-based contrastive optimization** + 通过 **coding agent 迭代精修**，自动定位并修复 planning 与 tool-use 错误。

**结果**：

| 指标 | 数值 |
|---|---|
| 在**高度优化过的人工 prompt** 之上 | **+8%** 质量 |
| **线上 A/B（对比仅支持 session refinement 的前一版体验）** | **+14% 用户收听**、**+5% 周活**、**−5% skip rate** |

> **本轮最该记住的一条**：**+8% 是打在一个"高度优化过的人工 prompt"之上**，不是打在一个弱基线上。工业界大量"LLM 带来 X% 提升"的数字，基线是随手写的 prompt；这篇把基线抬到人工调优后再报增量。
>
> **与库内主线的接口**：库内已有多条"agent planning / tool-use 错误定位"与"合成数据 + self-improvement"记录（09-25 的 TAMP、09-28 §2.6 coding agent 经济学）。本篇的差异化在于**冷启动约束**——**没有真实交互信号时，多轮合成数据是唯一可用的评测与优化信号源**，且它同时充当 eval set 与 RL signal。18 位作者含 Mounia Lalmas（Spotify 信息检索负责人），**MESH（Pinterest）那篇里出现的"structured review"式评测动机与本篇同源**。

#### 2.4.2 Multilingual Semantic Retrieval for Apple Music Search（ELISE）★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2607.10239](https://arxiv.org/abs/2607.10239) · cs.IR |
| **作者** | Vishalaksh Aggarwal, Kevin Sebastian, Vivek Kanojiya, Leo Le, Nick Tucey, Santosh Shankar |
| **机构** | **Apple**（论文自述 "Apple Music serves listeners across 150+ storefronts…"，RecSys 2026 Industry Track accepted manuscript） |
| **venue** | **RecSys 2026 Industry Track**（Accepted） |

**问题规模**：Apple Music 覆盖 **150+ storefront、数十种语言**，目录**每日新增数十万首**。在这一规模下，**拼错、转写（transliterated）、跨语言 query 的搜索召回是 session 质量的主要驱动因素**，而 **tail query 占了绝大多数 unique query**。

**方法**：**305M 参数的 Siamese bi-encoder**，从 GTE-multilingual-base 微调，**curriculum-scheduled 多目标训练**。通过**分位数分布匹配（quantile distribution matching）**把 dense 最近邻结果与既有 token-based index **混合**，**从而无需重训下游 ranker 即可部署**。

**结果**：

| 指标 | 数值 |
|---|---|
| 离线 Hit@10（vs GTE-multilingual-base） | **+69% 相对提升**；最难 query 类型增益最大：navigational NL **+183%**、拼写错误 **+88%**、similar-artist **0.02 → 0.25**（基线近乎为零） |
| 离线 PL2B@10（vs 生产基线） | 平均 **+0.5%**、按 query 频次加权平均 **+0.6%**（确认无回退） |
| **全球线上 A/B（18 天，全 storefront，SRP 页面）** | **转化率 +2.28% 相对**（CI [+2.19, +2.37]，p<10⁻⁴） |
| **no-result rate** | **−86.0%**（CI [−86.1, −85.8]） |
| **按 query 频次分层的 CR 增益** | **tail +7.93%** / mid +0.89% / **head +0.14%** |
| 各 storefront | 全部正向，**+0.5% 至 +6.7%，无任何市场回退**；**CJK storefront 增益最小**，与论文自述的限制一致 |
| 延迟 | 语义路径 **p95 +<55ms** |
| Item discovery | 每 item 的平均 distinct query 数 **+4.7%** |

**两个线上策略的对照（这是本篇最有信息量的部分）**：
- **T1** = 语义结果需其 text-match 分数**超过阈值**才纳入。
- **T2** = 语义检索**按数量设上限**。
- **T2 全面胜出：CR 增益是 T1 的 2.8×，no-result 降幅是 T1 的 12×。**
- 原因很直白：**T1 的文本重叠阈值恰好滤掉了语义检索最有价值的那批结果**——拼错与自然语言 query，**正是与 query 零词汇重叠的那些**。

> **本轮方法论上最值得抄的一条**：**一个"降低噪声"的 guard（阈值）系统性地删掉了它要保护的方法的价值所在**。这与 §2.1.4 的"干预与决策窗口不相交"、§2.2.2 的"混用 card 生成机制降低 R@5" 是**同一种失败模式的三次独立出现**——**保守的过滤器总是删掉高价值尾部。** 三篇分属检索、provenance、agent 工具发现三个领域，**建议合读**。
>
> 另注：作者明确论证 MovieLens / Amazon Reviews 等公开基准**不适合**这类研究（缺分层内容生态、容量饱和导致 scaling law 拟合不稳）——与 MESH（Pinterest）的论证**几乎逐句同构**。两篇可作"为何工业数据不可替代"的成对引证。

#### 2.4.3 Unified Generative Retrieval and Ranking in Chain-of-Recommendation（RecoChain）★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2604.25787](https://arxiv.org/abs/2604.25787) · cs.IR（2026-04-28） |
| **机构** | **Alibaba（`tentative`）** — 数据集为 **TAOBAO-MM**（8.8M 用户 / 35M item），作者机构未核实 |
| **venue** | 无（预印本） |

**问题**：Semantic-ID 生成式推荐把 next-item 预测变成自回归离散码生成，但存在一个结构缺陷——**beam-256 可以穷举候选，却缺乏从 beam 中挑出"真正更好 item"的细粒度排序能力**，于是**生成与排序之间存在性能落差**。

**方法**：把召回与排序整合进**单一 decoder-only Transformer**：
- **Stage I**：分层 Semantic ID 自回归生成候选。
- **Stage II**：把检索到的交互子序列拼到候选后做 **candidate-aware reranking**，**复用生成步的 KV cache**。
- RQ-Kmeans 层级化 tokenization（多模态 item embedding）。

**结果（TAOBAO-MM）**：

| 条件 | 增益 |
|---|---|
| beam=40 | **Recall@5 +4.53%**，**NDCG@10 +2.80%** |
| 输入序列长度 32 → 128 | Recall@5 增益 **+3.14% → +0.92%**（上下文稀疏时 reranking 最有用） |
| beam size 增大 | reranking 增益**系统性增大**（候选池更多样） |

> **注意发表时间**：这是 **2026-04-28** 的旧论文，09-29 才被发现未收录（标题的两种词序变体导致漏检，**与 §1.3 记录的 Semantic IDs handbook 标题变体是同一类漏洞**）。**价值在方法而非时效**：它给出的"单 backbone 复用 KV cache 做生成后重排"是一个**具体的算力节省模式**，与库内已有的"生成式推荐 + 外部 ranker"路线形成直接对照。⚠️ 机构为推断，TAOBAO-MM 的公开归属可查但**作者列表未核实**。

### 2.5 机制可解释性与表征审计

#### 2.5.1 A Mechanistic Study of AI-Text Detection Neurons in Frozen BERT ★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30287](https://arxiv.org/abs/2609.30287) · cs.CL / cs.AI |
| **作者** | Paweł Blicharz, Miłosz Grunwald |
| **机构** | 机构未列 |
| **venue** | **EMNLP 2026 Main Conference**（Accepted，comment 自述） |

**设定**：AI 生成文本检测器在标准基准上准确率很高，但**驱动这些预测的内部表征仍不清楚**。研究**冻结的 BERT-base-uncased** 中哪些神经元支撑 AI 文本检测。

**协议**：RAID 基准、6 个生成器（覆盖 pure-base 与 instruction-tuned 两族）；对**全部 9,216 个 CLS hidden-state 维度**（12 层 × 768）施加 Gurnee et al. (2023) 的 L1-to-L2 稀疏探针协议。

**五组结果**：

| 发现 | 数值 / 含义 |
|---|---|
| 稳定神经元规模 | **每个生成器 < 1%**，跨 fold 与 seed 一致；**只在该子集上训练的探针保留了大部全特征检测准确率** |
| 因果验证（双向 activation patching） | **两个方向上都比同规模随机集多一个数量级地翻转预测** |
| 但 mean-ablation 同批神经元 | **准确率基本不变** → **信号是冗余分布的** |
| **双层结构（本文最有意思的发现）** | **instruction-tuned 生成器把 30–36% 的稳定神经元集中在 BERT 最后一层；两个 base 生成器均低于 14%**——与"第 12 层承载 post-training alignment 的足迹"一致 |
| leave-one-family-out | 选中神经元在**未见生成器族**上保留 **86–94%** 的全特征上限 |

> **pacing 与 mean-ablation 的张力是本篇最值得讨论处**：patching 说这些神经元**因果必要**，ablation 说它们**因果不必要**。两者不矛盾——它指向**冗余分布式编码**（"signal is therefore redundantly distributed"，作者原话）。**这是本库讨论 mechanistic interpretability 时经常被省略的一个限定条件**：稀疏探针定位 ≠ 该子集是唯一承载体。
>
> **"检测器可以在一个固定的小子空间上运行，无需为每个生成器重新定位神经元"** 这一推论对生产检测系统有直接成本含义，值得单独跟踪。

#### 2.5.2 AlphaEarth distinguishes cities but compresses urban variation ★★

| 字段 | 内容 |
|---|---|
| **arXiv** | [2609.30356](https://arxiv.org/abs/2609.30356) · cs.CV / physics.soc-ph · **单作者** |
| **作者** | Andrew Renninger |
| **机构** | 机构未列 |
| **venue** | 无（预印本） |

**审计对象**：**卫星基础模型** AlphaEarth（Google DeepMind）。**注意：本文审计的是表征，不是模型能力**，单作者，社会物理交叉。

**规模**：**162 个国家的 1,000 个城市区域**。

**五组发现**：

| 发现 | 数值 |
|---|---|
| 城市在 hypersphere 上的位置 | 占据**偏移但重叠**的区域，距全局均值方向 **62.7°** |
| **地理预测力** | **大洲 + 气候** 预测了**被排除国家**中城市中心均值方向变异的 **24.3%** |
| 城市**内部** | 城市化程度只携带 **8.9%** 的变异；剩下的是**共享方向**，其局部朝向是变化的，**不存在一条普适的"城市化轴"** |
| **保留的变异本身是不平等的** | 城市中心内的离散度**每单位国民发展水平标准差高 14.1%**（已控制人口、土地面积、大洲） |
| 对照检验 | 发展中国家的城市**植被与纹理对比度更低**，离散度跟随该对比度；**完全调整后最多只剩 6.4% 的梯度** |
| **时间维度的警告** | **一座城市表征的年度变动，接近"重绘自身像素所能解释的 8 倍"**；且在 **2022 年 Sentinel-1B 丢失**一个 pass 方向的地区**收缩** |

**结论（作者原话大意）**：AlphaEarth 的表征**支持跨区域比较**，但**其年度层之间的差异尚未被验证可用于跨时间比较**。

> **这篇的形状与 §2.3.1 高度同构**：**测量一个广泛使用的表征的几何性质，然后指出它在哪个方向上不可用**。AlphaEarth 版问的是"城市差异在哪个轴上被压掉了"，cosine 版问的是"你这个 0.996 的噪声底是多少"。**两篇应互链，都属于"表征审计"这一在本库尚未成类的题材。**
>
> ⚠️ 单作者、预印本、无机构。**"年度变动 8×"这一数字依赖 Sentinel-1B 2022 失效这一事件**，若模型训练截止早于该事件则该解释需要重新审视——**论文未在摘要中说明其数据截止，标 `tentative`。**

### 2.6 其余精选（简述）

| ID | 标题 | 要点 | 库内状态 |
|---|---|---|---|
| [2609.30345](https://arxiv.org/abs/2609.30345) | **Coding Agents Aren't Enough!**（Sola Security Brain vs Claude Code，28 任务，真实 AWS 只读环境） | 覆盖率 **0.693 vs 0.387**（+79.2%，三次评分抽样 ±0.018）；25/28 任务领先；**推理成本低 17.7×、单位覆盖成本低 31.6×**。提出 **sample-and-generalise** 失效模式：turn budget 下枚举总体的一小部分，**断言一个不加对冲的全称否定，且样本量只写在 answer metadata 里不在答案里**——某任务在采样了约 **5,000 个 bucket 中的 40 个**后报告"不存在 bucket policy"，而该账户有 **65 个 bucket 带 wildcard-principal 读权限** | 0 hits。⚠️ **厂商评估自家产品，存在利益冲突**；且 full credit 取决于 Sola 的调查层是否为 30 任务基准做了定制（`tentative`）。**"sample-and-generalise" 的失效命名本身很有价值，且与 §2.1.3 的"缺失即否"互为镜像** |
| [2609.30360](https://arxiv.org/abs/2609.30360) | **Cost-Aware Best-LLM Identification using Dueling Feedback** | **NeurIPS 2026 accepted**。在"存在 Condorcet winner"假设下（该假设在多个真实数据集上被经验验证）提出 Track-and-Stop 风格算法，**证明误差趋零时渐近达到最优成本** | 0 hits。Nair 为 IIT Madras 教授（`tentative`）。**这是本轮唯一一篇 arXiv comment 明确写 NeurIPS 2026 的 straggler** |
| [2609.30299](https://arxiv.org/abs/2609.30299) | **Staged Depth Training（SDT）：PINN 的表征课程** | 浅层 prefix 在临时 physics-informed head 下训练 → **丢弃 head、冻结 prefix、加深**；无方程专用编码、最终架构不变。PINNacle 20 个默认前向问题 × 3 backbone 的 **59 个等预算 cell 中 40 个改善 ≥5%**，其余落在该带内；PirateNet 风格 backbone 上**几何平均误差降 32.8%**；**Poisson–Boltzmann 2D 上两个 backbone 的深度 scaling 指数都翻倍以上**。机制消融表明增益**不能由 optimizer restart 或浅层 warm-start 单独解释** | 0 hits。**"不改最终架构与推理成本"的性质使其对部署友好** |
| [2609.30316](https://arxiv.org/abs/2609.30316) | **PALM：金融语言模型的 point-in-time 适配** | 金融回测的 **look-ahead bias** 处理方式是每年重训一次 PIT checkpoint。**本文证明年度预训练不必要**——把每个 checkpoint 与取代它的新 checkpoint 在同一评估窗上对比，**新 checkpoint 并未更好**。改为在**决策日之前**发表的文本上拟合一个低秩 adapter，**不改动任何预训练权重**；**小 adapter 足以给旧 checkpoint 增加一个新时段的知识，且优于 continued pretraining**。十年金融新闻；PIT 模型族 cutoff 跨 20 年、规模 1.3–4.2B | 0 hits。**与 2.3.1 属同一族问题：报告的数字缺了它需要的那个量**（此处缺的是"新数据带来的信息量"） |
| [2609.30342](https://arxiv.org/abs/2609.30342) | **Low-Rank Friction（R-iKFAD）**：显存高效的 Transformer 预训练 | iKFAD 用自适应摩擦替代自适应学习率（性能与 Adam 相当），但完整摩擦张量 ξ∈R^{m×n} 带来与 Adam 二阶矩**同量级的 O(mn) 开销**。改为由行/列动量统计构成的**秩-1 外积分解**，摩擦内存 **O(mn) → O(m+n)**，**总优化器状态约减半**。GPT2-Nano / TinyViT / DistilBERT / GPT2-S 上**性能持平或更优**，超参鲁棒性相当。连续时间分析：线性阻尼（γ>0）下证明强凸下的指数收敛；**γ=0（实验中的首选）下摩擦完全由过去动量生成、随动量消失而关闭，故无法证明几何收敛**，但证明了收敛到极小值并给出能量的上下界（ε_stab=0 时 O(t⁻¹)，为正时 O(t⁻¹ᐟ²)） | 0 hits。**作者称这是秩-1 分解优化器在连续时间下的首个收敛率，也是首个不需正阻尼的结果**（Leimkuhler 为 Edinburgh 教授，`tentative`） |
| [2609.30289](https://arxiv.org/abs/2609.30289) | **HiCoMER：层级协作记忆的有效性感知检索** | 团队协作中记忆是**异质且持续演化**的：团队记忆存集体决策/协议/当前共识，个人记忆存成员特定观测/执行痕迹/中间进展。现有系统把全部记忆当**扁平池**按语义相关/重要/新近排序，**不建模层级结构与演化有效性**，因而**捞出语义相关但已过时或冲突的记忆**——尤其是已不对齐当前团队共识的个人记忆。三组件：Hierarchical Memory Conflict Updater / Validity-Aware Memory Retriever / Memory-Grounded Answer Generator；构建两个协作场景 memory-grounded QA 新数据集，**一致优于强基线**（减少过时检索、保留当前共识、提升下游 QA） | 0 hits。⚠️ **两个数据集均为本文自建且未在摘要中给出规模**——"一致优于"目前**不可独立复核**，标 `tentative`。最后一位作者 Xiaozhong Liu 公开身份与人大相关（`tentative`）。**主题与本库 memory 主题直接相关** |

---

## 3. Runner-ups（本轮判定不深读）

| 主题 | 候选 | 不深读理由 |
|---|---|---|
| 经济/金融 LM | [2609.30316](https://arxiv.org/abs/2609.30316) PALM | 已列入 §2.6 简述；核心结论清晰、无需 PDF 深读 |
| 优化器 | [2609.30342](https://arxiv.org/abs/2609.30342) R-iKFAD | 同上；数学结论完整给出 |
| Agent 记忆 | [2609.30289](https://arxiv.org/abs/2609.30289) HiCoMER | 数据集规模缺失，深读也补不上；已在 §2.6 标注 |
| PINN | [2609.30299](https://arxiv.org/abs/2609.30299) SDT | 结论完整；与本库主题（时序/科学 ML）相关度中等 |
| 其余 33 篇 2609.* straggler | — | 24 个 category 的 listing 中低于 2609.30361 的其余条目，主题分散（纯 CV / 纯数学 / 纯硬件），与本库主线弱相关 |

**未收录的 1 篇旧交叉列表**：`2605.01624`（2026-05 跨列表，submitted 更早）— 因其 ID 虽在库外但**并非"本轮窗口新论文"**，收进会误导窗口口径。

---

## 4. 跨主题观察 — Cross-Cutting

### 4.1 "报告不了缺失"是本轮唯一贯穿四条独立社区的主线

这是本轮最值得记的结构性发现。**四篇论文分属四个互不引用的社区**（agentic security / NeurIPS WiML 评测 / 生产 SRE / 商业安全厂商），但都在处理同一件事：**证据缺失时，系统输出的是一个自信的答案而不是"不知道"**。

| 论文 | 缺失的形态 | 缺口的代价 |
|---|---|---|
| Silent Success (2609.30307) | 检查**未执行** | 运行几乎没检查 → **满分绿灯两周** |
| Empty Intersection (2609.30308) | 决策**读不到修复过的行** | 覆盖率 98.4% → **决策仍无输入** |
| MARCH (2609.30328) | judge **没有独立于答案的证据** | 4.4% 准确率（直接评判 43.7%） |
| ScopeBench (2609.30325) | agent **没有遵守 scope 的义务** | +10pp capability 伴随 **+35.6pp adherence** |
| 2609.30345 | agent **只采样了总体的一小部分** | 采样 40/5,000 后**断言全称否定** |
| Cost-Aware BAI (2609.30360) | 审计**无法看到全部 path** | α=0.1 下**重尾仍留过度收费容量** |

**这六篇无一引用彼此**（已查）。库内 09-28 §2.4 的 provenance 链与 §2.7 的评测陷阱是**前两篇的前身**，但**本组把同一模式推进到了"不同社区各自独立发现"的程度**——这把它从"某篇论文的观点"提升为"一个正在成型的工程规范"。

### 4.2 保守过滤器系统性地删掉它们要保护的方法的价值所在

同一失败模式在三个不相关领域各出现一次，值得单列：

- **Apple ELISE（§2.4.2）**：T1 的 text-match 阈值滤掉了与 query **零词汇重叠**的结果——**正是拼错与自然语言 query**。换成数量上限（T2）后 CR 增益变 2.8×、no-result 降幅变 12×。
- **Empty Intersection（§2.1.4）**：grade 词表从覆盖 36.1% 扩到 98.4%，**决策读的那 32 行一行都没进来**。
- **Cartograph（§2.2.2）**：bootstrap 生成的 capability card **在语义上更干净**，但 49 个易混 cluster **全部出现在其中**；混用生成机制直接降低 R@5。

**可推广的表述（本轮归纳，非引自原文）**：任何以"降低噪声"为目的的 guard，都必须**显式测量它对高价值尾部的截断率**，否则它优化的是自己好测的那部分。

### 4.3 报告的数字缺了它需要的那个量 —— 两篇姊妹篇

- **Cosine Similarity Is Not Evidence（§2.3.1）**：cosine 0.996 缺 **n**；**E[cos] ≈ (1+4/κ)⁻¹, κ=nρ²/d**。
- **PALM（§2.6）**：新 checkpoint 缺**它比旧 checkpoint 多知道什么**。
- **AlphaEarth（§2.5.2）**：城市间差异缺**它不沿哪条轴变化**；年度差异缺**它是否可比**。
- **与库内 09-28 §3.5 的 "Agreement ≠ Accuracy（ρ 0.20–0.59）" 同族**——那篇说 agreement 不可信，这两篇说 agreement 的**底噪与缺口**分别是多少。

**这三篇应互链，并考虑在库内新建"表征审计 / measurement adequacy"这一题材页**（当前库内无此分类）。

### 4.4 本库去重机制的一个具体漏洞：标题词序变体

本轮发现**同一篇论文在库内以两种标题共存**：

| 官方标题 | 库内变体 | 出现位置 |
|---|---|---|
| `Semantic IDs in Generative Recommendation: A Practitioner's Handbook`（CIKM 2025 Best Resource） | `Generative Recommendation with Semantic IDs: A Practitioner's Handbook` | 2026-09-11 / 07-31 / 08-01 vs 2026-05-26 |
| `Unified Generative Retrieval and Ranking in Chain-of-Recommendation` | 库内**无**（因标题变体导致 04-28 的旧论文漏检 5 个月） | — |

**教训**：**arXiv ID 是可靠的去重键，标题不是。** 本库 09-28 的 638 篇扫描与本轮的 52 篇 straggler 筛查**都用了标题探针作为二次筛选**，这意味着**过去若干轮的 digest 可能都存在同类漏检**。建议后续 digest 一律以 ID 为主键，标题仅用于人工确认。

---

## 日历（Calendar）

| 日期 | 事件 | 状态 |
|---|---|---|
| **2026-09-29（今日）** | **RecSys 2026 Main Sessions Day 1**（Minneapolis, Marriott City Center Downtown） | ✅ 官方确认 |
| **2026-09-29（今日）** | **NeurIPS 2026 Workshop mandatory notification** | 沿用 09-25/09-28 记录，本轮未复核 |
| 2026-09-29 | OpenAI DevDay | 沿用 09-25 记录，本轮未复核 |
| 2026-09-30 | RecSys 2026 Main Sessions Day 2 | ✅ 官方确认 |
| **2026-10-01** | **RecSys 2026 Main Sessions Day 3 / 闭幕** | ✅ 官方确认（**即 09-25 digest 记录的"09-29 → 10-01"，经本轮核实为正确的 Main Sessions 口径**） |
| 2026-10-02 | RecSys 2026 Workshops / Tutorials 末日 | ✅ 官方确认 |
| **待定** | **SIGIR 2026 Best Paper 公布** | ⚠️ **三轮 unresolved**，见 §1.5 |
| **待定** | **NeurIPS 2026 award 公布** | 预计开幕前后，会前无名单属正常 |
| 2026-10-24 – 10-29 | EMNLP 2026 | 沿用 09-25 记录 |

---

## Data Quality Notes

1. **⚠️ 本轮没有新 arXiv 窗口。** 今日所有"新鲜 arXiv"内容均来自**旧批次的未收录漏项**，不是新提交。**任何把本文当作 2026-09-29 新提交来读的用法都是错的。** 详见文首窗口口径。

2. **⚠️ `/list` 表头不可信。** 8 个 category 的 `/list/{cat}/new` 表头显示 `Monday, 28 September 2026`，正文实际是 09-25 及更早批次。**这一现象在 09-28 已出现过一次**（当时结论是"页面没更新"），**本轮证明是表头与正文不同步**——两者是不同的故障，处置方式相同：**不依赖 `/list` 界定窗口。**

3. **⚠️ 机构字段大面积缺失。** arXiv abs 页面**不含 affiliation**。本轮 19 篇深读中 **仅 2 篇**（Spotify 2609.30297、Apple 2607.10239）**由论文自述机构**；其余 17 篇一律标"机构未列"。**凡本文出现的 `tentative` 机构判断，均基于作者的公开学术身份推断，页面本身无证据。** 本轮**没有任何一篇**能确认为 Google DeepMind / OpenAI / Meta / Microsoft / ByteDance / Alibaba（除 RecoChain 的推断）/ Tencent / Kuaishou（除 09-28 已收论文）/ Baidu / NVIDIA / Anthropic / Amazon 所属。

4. **⚠️ 本轮有 3 篇论文由厂商评估自家产品或自家系统**，利益冲突已标注：2609.30345（Sola Security Brain 评估自家产品 vs Claude Code）、2609.30297（Spotify 自报 A/B）、2607.10239（Apple 自报 A/B）。后两者的 A/B 数字**方法学细节充分**（CI、p 值、实验时长、分层显著性），可信度高于典型厂商自报；前者缺少"调查层是否为基准定制"的说明，**存疑**。

5. **⚠️ 去重计数口径不一致。** 本轮实测 `wiki/**/*.md` 为 **6,966** 个唯一 arXiv ID；09-28 记 6,244；本轮早期扫描记 7,004。三个数字**正则与 glob 范围都不同**。**三者不应直接比较。** 建议统一为"正则 `2[0-9]{3}\.[0-9]{4,5}` + `wiki/**/*.md`"并在 EXTEND 中固化。

6. **⚠️ 标题词序变体是活跃的去重漏洞**（§4.4）。**已确认 1 例造成 5 个月漏检**（RecoChain），**可能影响过去若干轮 digest**。**未做全库系统性排查**——这是本轮识别出的、优先级最高的待办。

7. **SIGIR 2026 Best Paper 三轮 unresolved**（09-16 / 09-28 / 09-29）。本轮建议**停止重试并改换路径**（如查 Melbourne 组的会议注册页或 SIGIR 邮件列表），因为"官方页更新"可能根本不是公布路径。

8. **单作者 / 无 venue 论文占比偏高。** 19 篇深读中 **7 篇为单作者预印本**（2609.30270 / 30275 / 30326 / 30307 / 30308 / 30356 及 2.4.3 的机构不明项）。这类论文的**优先权主张与效果主张均未独立核实**，本文一律按"可证伪的初步观察"对待，**不作为结论性证据**。其中 2609.30307 / 30308 同源两篇的**分量主要来自其量化具体性**（两周绿灯、194,620 行、121,296 行、32 行），**而非其新颖性**——作者自己也说"所提供的不是这一类别的novelty"。

9. **9-28 遗留 open item 结算：关闭 3 / 遗留 1 + 1 部分。** AAAI Classic ×2 ✅、AAAI AISI ×2 ✅、CIKM 2025 runner-up ✅；SIGIR 2026 Best Paper ❌（三轮）；**"Science Data" 标题归属仍未定位**（§1.2），但已确认它**不是** AISI 两篇之一。

---

## 去重明细（写稿时 whole-`wiki/` grep 结果）

| 项目 | 结果 |
|---|---|
| 19 篇 2609.* straggler 深读 | **全部 0 hits** |
| 2607.10239（Apple ELISE） | **0 hits** |
| 2604.25787（RecoChain） | **0 hits** |
| DP-COMET / D3-TR / CyberBOT / CIKM 2010 ToT | **各 0 hits** |
| AAAI Classic #2（Tellex / Kollar / … / Roy） | **标题 0 hits、7 位作者名各 0 hits** |
| RecSys industry track 既有 6 篇（RECAP / MESH / TubiFM / SPEAR / EGR / TopoTok） | 3–14 hits，⚠️ 已在库，本轮仅补 MESH/RECAP 的细节，不重复收录 |
| "Cartograph" 2 hits | **假阳性**（命中的是 `Persona Cartography`，见 2026-07-10） |
| "slum" 7 hits / "Mixture-of-Experts" 111 hits | 命中的是 AISI 两篇的**已在库记录**（07-31 / 08-16 / 08-17），非新增 |
| "GRAM" 292 hits | 泛匹配（`program` / `grammar` 子串），非该论文 |
| "Practitioner's Handbook" 9 hits | 库内 title 变体，命中的是 Semantic IDs handbook（已在库） |
