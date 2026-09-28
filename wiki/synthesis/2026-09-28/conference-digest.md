---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 + Fresh arXiv — 2026-09-28"
type: synthesis
created: 2026-09-28
updated: 2026-09-28
sources: [conference-web-searches, arxiv-listings, recsys-acm-contributions, aaai-awards, www2026-accepted]
tags: [conference-digest, RecSys2026, KDD2026, ICML2026, ACL2026, CVPR2026, EMNLP2026, EMNLP2025, CIKM2025, SIGIR2026, NeurIPS2026, AAAI2026, WWW2026, ICLR2026, recommendation, generative-recommendation, advertising, CTR, LLM, agents, agentic-eval, speech, code-execution, generative-models, flow-matching, MoE, time-series, benchmarks, evaluation-validity, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-09-28

> ⚠️ **CORRECTION 2026-09-28（由 `game-rl-daily` 2026-09-28 追加）**：下方「window-stall」口径说明**基于错误前提**，请勿沿用。其推理为「8 个 category 的 `/list/{cat}/new` 仍显示 Friday, 25 September 2026 + API tail sweep 全局最大 ID = 2609.30258/2609.30266」，据此判定今日无 fresh window。该结论**不成立**：
> - **Mon-28 窗口确实存在**：category-agnostic API 查询 `submittedDate:[202609241800 TO 202609260000]`（**不加 `cat:` 限定**）返回 **1,013 篇，ID 2609.30361–2609.31373**，feed `updated=2026-09-28T01:58:03Z`。
> - **错误根因**：`2609.30258/2609.30266` 是 **cat-restricted 查询尾部的最大值，不是全局最大值**。cs.AI 与 cs.LG 在本批次**新增 0 篇**，故其 `/list` 页面合法地仍显示上一期公告；per-category max 无法界定 global max。
> - **推论修正**：本篇 §2 标题「新鲜窗口精选」实为 **Fri-25 窗口 remainder**，**并非** Mon-28 fresh window；Mon-28 的 1,013 篇中另有 direct 内容被 sibling 收录（见 `game-rl-daily` 2026-09-28 与 `arxiv-daily` 2026-09-28）。
> - **常设规则**：**绝不可由单一 category 的 `/list` 页面或 `cat:` 限定的 API 尾部界定全局 arXiv 窗口；必须以 category-agnostic `submittedDate` 查询为准。** 同一错误亦见于 `arxiv-ai-search` 2026-09-28（已由 commit `cca6815` 更正）。
>
> **口径说明（window-stall）**：今日 2026-09-28 是 **周一**，arXiv 周一公告在 ~20:00 ET 之后发布。抓取时 8 个 category 的 `/list/{cat}/new` 仍显示 **Friday, 25 September 2026**，API tail sweep 的全局最大 ID 为 **2609.30258/2609.30266**（`published=2026-09-24`）。因此本篇**不是 fresh-window sweep**，而是 **venue-strand digest**（会议 proceedings / awards 为主）+ **Fri-25 窗口的第二次深挖 remainder**。
>
> **Dedup 纪律**：今日 5 个 sibling digest（`arxiv-ai-search` / `arxiv-paper-check` / `game-rl-daily` / `tech-report-digest` / `wq101-alpha-daily`，全部 2026-09-28）已提交并覆盖 Fri-25 窗口的 LLM/retrieval/post-training/agent-memory/rec/game 大块。本文 **§2 的 21 篇 featured arXiv 论文全部 whole-`wiki/` regex grep 验证 0 hits**（含 sibling 声称集），即本文对其为独家。§1 中已收录项只做 **venue 确认** 并显式标注 `⚠️已在库`，不重复展开。
>
> **负向发现（重要）**：AAAI 2026 / WWW 2026 / ICLR 2026 的全部 award 条目经 grep 验证 **已在库**（见 §1.10），本轮无新增；SIGIR 2026 Best Paper 官方页面尚未更新到 2026 届（页面表格止于 2025），标记为 **unresolved**。

---

## 1. 会议扫描 — Venue-by-Venue（2025–2026）

### 1.1 RecSys 2026（Minneapolis）★ 本轮头条 — proceedings 已上线

**这是本轮唯一有实质新增的会议事件**：`RecSys '26: Proceedings of the 20th ACM Conference on Recommender Systems` 于 **2026-09-27** 正式出版（ACM DL，DOI 前缀 `10.1145/3773078`），恰好在本 digest 前一天。规模：**1,424 投稿 / 279 接收 = 20% acceptance**。

> ⚠️ **日期口径不一致**：官方 contributions 页显示会议为 **2026-09-28 → 10-02**；本库 09-25 conference-digest 记为 "Sep 29–Oct 1"。以官方页为准，09-25 记录应修订。`tentative` 标注：本次未能直接抓取 `recsys.acm.org` 日程页，时间窗来自官方 contributions 页的搜索摘要。

**Netflix Research（重点机构）— 唯一进入 ACM DL 的单篇重点机构论文**

- **Towards Generalizable and Efficient Large-Scale Generative Recommenders**｜面向大规模生成式推荐器的泛化性与效率
- 作者：Qiuling Xu, Ko-Jen Hsiao, Moumita Bhattacharya（**Netflix Research**, Los Gatos；netflix.com 官方邮箱）
- Venue：RecSys '26，DOI `10.1145/3773078.3831905`；arXiv:2605.23312（v1 2026-05-22，v2 2026-08-06）
- 链接：[arXiv:2605.23312](https://arxiv.org/abs/2605.23312) ｜ [ACM DL](https://dl.acm.org/doi/10.1145/3773078.3831905)
- 状态：⚠️ **论文本体已在库** → `wiki/papers/recommendation/netflix-generative-recommender-scaling.md`（另见 05-25 arxiv-daily、06-04 / 08-16 conference-digest）。**本条新增的只是 venue 事件**：DOI 落地 + 出版日期。

核心内容（保留原论文主张）：
- **Scaling**：backbone 从 **2M → 1B** 参数（**不含 embedding 与 decoding 层**），production-scale title recommendation 场景。
- **任务依赖的 scaling 行为**：部分下游任务在观测尺度内已逼近经验上限（empirical ceiling），另一些持续受益于容量 → 主张用 **offset scaling-law fits 作为诊断工具**，判断追加 scale 在何处更有用。
- **Production 约束三件套**：
  1. **Multi-token prediction** → 对齐 serving latency；
  2. **Sampled softmax + projected decoding head** → 降低数万亿 behavior token 反复重训的成本；
  3. **Semantic item towers + collaborative-embedding masking** → cold-start（新作上线时 collaborative ID embedding 尚不可靠，先用 semantic metadata 打分）。
- **结果**：**1M 用户、一周 production-shadow 评测**中，1B-backbone 模型在**所有报告任务上 MRR 均高于** 2M baseline。
- 对本库的意义：这是 generative rec 线里少见的**"scaling 收益 ≠ 生产收益"**的正面案例，把 **task headroom / decoding cost / serving-latency alignment / item generalization** 与 model scale 并列为 transfer problem 的四个分量——与 09-22 记录的 IntBMoE UVCTR（MoE 进 rec 生产）、2609.23718 语义 ID 复现性（2609.24430）是同一批生产化证据的第三个独立点。

**RecSys'26 官方 contributions 页新点（grep 状态标注）**

- **SCRec: Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation**（Jiayi Dan, Weijian Li, Yongqi Liu, Kaiqiao Zhan）— 指出两阶段 pipeline 中 semantic tokenization 被文本语义主导、collaborative 不足，而 code 序列再 embedding 又丢掉原语义；提出 collaborative-enhanced tokenization + semantic-guided generation + manifold alignment 三个组件，"minimal additional training and inference costs"。⚠️ 已在库（09-16 arxiv-daily）。
- **Coarse-to-Fine Long-term Interest Modeling for Generative Recommendation**（Shiteng Cao 等，含 Ruiming Tang / Han Li / Kun Gai）— ⚠️ 未验证收录状态，`tentative`。
- **DP-Rec: Towards Dynamic ... ing for Efficient Long-Sequence Recommendation**（Dwipam Katariya 等）— 标题在官方页被截断，⚠️ 仅记录存在性。

### 1.2 KDD 2026（Jeju）— Meta 三个奖项（来源为二手，标记 tentative）

官方获奖名单页本轮未能直接抓取，以下三条来自 **LinkedIn 获奖公告的搜索摘要**，`tentative` 级别，建议以 KDD 官方 proceedings 为准：

- **Best Paper – Applied Data Science Track** — *Multi-modal Multi-turn Comprehensive RAG Benchmark*（Meta）
- **Best Paper – Advertising Science Track** — *McGrad: Multicalibration at Web Scale*（Meta）— 对本库 [[multicalibration]] / 广告 calibration 线是潜在新条目，本轮未在 `wiki/` 中 grep 命中（低置信：标题可能有转写差异）。
- **Best Student Paper** — *SCOPE: Cost-Efficient Model Selection for Compound AI Systems under Quality Constraints*

⚠️ 另注：RecSys'26 的 Netflix 论文在本库已有独立 paper 页，**KDD '26 的 HOBA**（2607.24779，线上 target cost +3.6%）已在 09-25 digest 做过 venue 确认，不重复。

### 1.3 ICML 2026

- **规模（官方 blog）**：**23,918 valid submissions / 6,352 accepted = 26.6%**；**168 orals**。
- **Test of Time**：**Asynchronous Methods for Deep Reinforcement Learning (A3C)**。
- 奖项页：[announcing-the-icml-2026-awards](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/)。
- ⚠️ 状态：*The Flexibility Trap*（2601.15165，JustGRPO，GSM8K 89.1%）、*High-Accuracy Sampling for Diffusion Models*（MIT）、A3C、以及多篇 honorable mention **均已在库**（09-25 conference-digest §1.1 / 07-30→09-05 系列）。本轮无新增。
- **对扩散 LM 线的持续张力**（`high confidence`，来自 09-25 已记录内容）：Flexibility Trap 是对 dLLM "任意顺序解码有益" 的一手反论证；本轮无新证据推翻或加强。

### 1.4 ACL 2026

- **规模**：**12,148 投稿**（同比 **+45%**）/ **4,462 接收**；**3 篇 Best Paper + 18 篇 Outstanding Paper**。
- ⚠️ 已收录 Best Papers：*The Imperfective Paradox in Large Language Models*（Miyao 组）、*Memory Efficiency and Resource-Rational Encoding in Sentence Processing*（Dillon / Futrell）。
- **本轮未解条目**（`tentative`，需官方 proceedings 核对确切标题/作者）：*CURE*（自拟展开为 Critique-Driven Unified Reinforcement Learning for Test-Time Self-Improvement）、*PolyGloss*（自拟展开为 Massively Multilingual Joint Segmentation and Glossing）、*PALU*（自拟展开为 Maximizing Local Entropy Where It Matters）。**这三个展开标题未经官方页面确认，不得作为正式标题引用。**

### 1.5 CVPR 2026

- **规模**：**16,092 投稿 / 4,089 接收**。
- **评审侧数字（本轮新增）**：**25,149 reviewers**，其中 **1,545 outstanding reviewers**（`tentative`，来自会议统计综述页）。
- ⚠️ Best Papers（D4RT 动态 4D 重建、Native and Compact Structured Latents for 3D Generation）以及 NitroGen / SAM 3D / ChordEdit / Molmo2 / VS-Bench / CubiD 等 **均已在库**。本轮无新增论文。

### 1.6 EMNLP 2025（已结束）与 EMNLP 2026（进行中）

**EMNLP 2025 规模**：**1,810 main papers / 1,406 Findings / 194 Industry Track / 78 demos**。
- Best Paper *Infini-gram mini* ⚠️ 已在库（`high confidence`）。

**EMNLP 2026** — 本轮**唯一确认的新 venue-tagged arXiv 条目**来自 §2.6（*Where Hallucinations Live* 标注 `EMNLP 2026`）。此前 sibling 已收录 CoMAP（2606.02372）、TaRA（2609.02639）、Counter-GEO-Bench（2609.02316）、HMS（2609.21247）、BCA / BirdsoneChat（Findings/REALM track）等。本轮 EMNLP 2026 通知尚未有新的 award 公告。

### 1.7 CIKM 2025 / CIKM 2026

- CIKM 2025 奖项扫描完成：Transferable…（Best Paper runner-up）等条目 **已在库**。
- *Data-centric Prompt Tuning for Dynamic Graphs* — 此前一轮扫描的疑点条目，本轮 **未能在官方页面确认**，`unresolved`，不作为 claim 收录。
- CIKM'26 FAE + REAL（2609.08943）已在 09-16 digest 收录。

### 1.8 SIGIR 2026（Melbourne）

- **Test of Time** ⚠️ 已在库。
- **Best Paper 2026：unresolved** — 官方 `sigir.org/awards/best-paper-awards/` 的年度表格**仍止于 2025**，2026 届未更新。09-16 digest 记录的 "语义相关图推理 / SPLADE / BM25" 说法**未能在官方页面验证**，保持 `tentative`，不升级。

### 1.9 NeurIPS 2025 / 2026 物流

- NeurIPS 2025 奖项（Gated Attention 2505.06708、1000 Layer Networks、VAGEN 等）⚠️ 已在库。
- **NeurIPS 2026 作者通知 ≈ 2026-09-24**（09-25 digest 记录）→ 按今日已过通知窗口计，NeurIPS 2026 的 accepted list 应已进入可公开检索状态，**本轮尚未取得权威列表**，`unresolved`，列为下一轮首要目标。

### 1.10 AAAI 2026 / WWW 2026 / ICLR 2026 — 全覆盖，零新增（负向发现）

本轮对三大会议的 award 做了完整 sweep，**结论是全部已在库**，记录于此以免后续重复劳动：

| 会议 | 本轮核验的 award 条目 | 库内状态 |
|---|---|---|
| AAAI 2026 Outstanding (Main) | Model Change for Description Logic Concepts；Causal Structure Learning for Dynamical Systems (CADYT)；ReconVLA；High-Pass Matters (Sheaflet)；LLM2CLIP | ⚠️ 5/5 已在库（06-08 / 07-31 / 08-01 / 09-24 digests） |
| AAAI 2026 Outstanding (AISI) | PlantTraitNet；Generalizable Slum Detection；Science Data | ⚠️ 前二已在库；**"Science Data" 标题在库内 0 hits**，但为 AISI track 且作者列表被官方页截断，判为 `unresolved` 不收录 |
| AAAI 2026 Classic | Learning Structured Embeddings of Knowledge Bases (Bordes/Weston/Collobert/Bengio) | 需补 grep，未在本轮窗口内确认 |
| WWW 2026 Best Paper | From Retrieval to Generation: Unifying External and Parametric Knowledge for Medical QA（Lei Li, Xiao Zhou, Yingying Zhang, Xian Wu）— MedRGAG | ⚠️ 已在库（08-17 / 08-05 digests） |
| WWW 2026 Best Short Paper | DualGR: Generative Retrieval with Long and Short-Term Interests Modeling | ⚠️ 已在库（07-23 / 06-13 / 08-17） |
| WWW 2026 Seoul ToT | LINE: Large-scale Information Network Embedding（Jian Tang 等，2015 WWW，7,100+ citations） | 需补 grep，未在本轮确认 |
| WWW 2026 规模 | Research Track 3,370 投稿 / 676 接收 = 20%（仅 10 条 research track） | 新增数字，参考价值 |

**ICLR 2026**（Singapore, Apr 25–27；225 Oral）：ReTool、Kimi-Dev（60.4% SWE-bench Verified）、CodeGym（2509.17325）、DreamGym、AgentFlow、VisCoder2、Critique-Coder、Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource（2506.12119）⚠️ 全部已在库（09-25 conference-digest §1.2）。本轮无新增。

---

## 2. 新鲜窗口精选（21 篇，全部 whole-`wiki/` grep 0 hits）

### 2.1 Speech & Audio — Alibaba Qwen（重点机构）★

#### Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction
**Qwen-Audio-3.1-Realtime：迈向可靠的 Agentic 语音交互**

- 作者：Lujia Bao, Qian Chen, Luyao Cheng, Chong Deng, Yuxiang Kong, Xiangang Li, Xu Li, Jiaqing Liu, Chao-Hong Tan, Haoyu Wang, Wen Wang, Xilou Wang, Haoxiang Xu, Junhao Xu, Liang Yi, Binbin Zhang, Qinglin Zhang, Qiquan Zhang
- 机构：**Alibaba Tongyi Lab / Qwen team（推断，`tentative`）** — arXiv 未打印 affiliation；依据是作者构成（Qinglin Zhang / Qiquan Zhang / Luyao Cheng 为 Qwen 语音线长期作者）与正文对 Qwen-Audio-3.0-Realtime 的直接对比
- 形式：**25 pages, technical report**（无会议标注）
- 链接：[arXiv:2609.25176](https://arxiv.org/abs/2609.25176)

**背景与问题**：real-time 语音助手必须同时满足三件事——对**演化中的请求做推理**、**执行动作**、**遵守对话规则**。3.0 代的失败模式集中在"会说话但不会办事"以及在有背景语音时误响应。

**方法：Think, Act, Speak, and Coordinate 四段式**

| 阶段 | 技术 | 作用 |
|---|---|---|
| **Think** | Core-Cocktail SFT + **M²-OPD**（Multimodality and Multi-Teacher On-Policy Distillation） | 迁移语言能力 + 建立原生 audio skill |
| **Act** | self-evolving executable environments + multi-granularity rollouts → **GRPO** | 学会用工具、读懂反馈、完成多步任务 |
| **Speak & Coordinate** | 显式对齐"是否说 / 何时说 / 如何说 vs 如何做" | 抑制背景语音误触发 |

**结果（务必区分两个基准）**

| 指标 | 3.0-Realtime | 3.1-Realtime | Δ |
|---|---|---|---|
| overall task success（半双工 STT 改造版 τ-Voice） | 78.4% | **82.0%** | +3.6 pp |
| Full-Duplex-Bench v1.5：对背景语音的响应率 | 73.0% | **13.0%** | **−60.0 pp** |

**第二个贡献**：**Voice Harness** 原型 —— 以 Qwen-Audio-3.0-Realtime 作前台，通过 **foreground–background coordination + memory** 把 spoken interaction 延伸到持久任务。

**对比与本库关系**：Full-Duplex-Bench 的 73.0 → 13.0 是本轮**方向最干净的一处工程改进**（越低越好），与 09-20 tech-report 记录的 Gemini 3.8 Audio（AA S2S 82.6 Live-ET #1 / 76.0 Live）、Qwen3.8-LiveTranslate（Interleave 同传，LAAL 延迟 2.8→2.3s）构成"语音大战 9 月下旬"三极中的**中系一极**；3.1 的定位不是刷 S2S 榜单，而是**把 tool-calling 与全双工纪律绑进同一个 RL recipe**——这与 09-22 sibling 收录的 NemotronLabs VoiceChat（FDB3 82.5% tool-F1）是同一条技术路线，`high confidence`。

### 2.2 Code Execution & Programming Agents

#### Large Language Models for Programming: Actually Fixing or Reimplementing Incorrect Code?
**大语言模型编程能力实测：究竟是在修复错误代码，还是在重写？**

- 作者：Alexandru Stefan Stoica, Traian Rebedea, Marian Cristian Mihaescu
- 机构：arXiv 未打印（`tentative`）
- 链接：[arXiv:2609.29410](https://arxiv.org/abs/2609.29410)

**动机**：既有研究把 **problem solving** 与 **bug fixing** 分开评估，从未考察两者的关系。核心问题：LLM 相对 buggy 版本的偏离程度 vs 人类 patch 有多大？是否存在"倾向于整体重写"的偏置？

**方法**：构造 Codeforces 真实数据——取**两位用户约 3,000 条 submission**，每条 buggy submission 配对其**对应的真人 fix**；以"buggy 解 ↔ 人类 fix 的相似度"为 baseline，评估 LLM 生成 fix 的质量。用 **Codeforces-R1** 数据集的测试（由 **DeepSeek-R1** 生成）判定 LLM 解是否真正解决问题。被测模型为 **3 个 OpenAI GPT 系列：gpt-5-nano / gpt-5-mini / gpt-5.1**。

**发现（两条，均为负向结论）**
1. LLM 相对人类 fix **修改的行数系统性偏多**；在部分 case 上**生成全新解**而非修补。
2. 即使 buggy 提交已经**非常接近人类 patch**，LLM **从头生成反而解出更多题**。

**为什么重要**：这是对 "AI 编程工具应做增量修补、而非整体替换" 这一设计直觉的**直接反证据**。对 [[ai-assisted-programming]] / SWE-agent 线的含义是：若模型天然倾向 reimplement，则 patch-based reward（以"最小 diff 正确"为标签的 RLVR）在分布上与模型先验冲突——与 09-22 记录的 CoVer（code-RL 奖励设计）互为补充，属不同切入（那边改 reward，这边改对 reward 分布的假设）。

#### Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large Language Models
**是风格，不是"自我"：表层线索解释了 LLM 的零样本代码归属判断**

- 作者：Ehsan Barkhordar, Surendrabikram Thapa
- 形式：18 pages（附 code & data 链接）
- 链接：[arXiv:2609.30048](https://arxiv.org/abs/2609.30048)

**动机**：LLM 风格的 LLM-as-a-Judge 会偏袒"自己写的"代码；若多个模型互相评判甚至可能**串通**（collude）。本文对**当前商用模型**做 zero-shot 检验。

**设置**：5 个 LLM 在 **MBPP / HumanEval / DS-1000** 上生成解，另 7 个只在 MBPP 上生成；模型作为 evaluator 做 **4 类任务**——(a) 从一对中挑出自己的解；(b) 判断单个解是否为自己所写；(c) 判断两个解中哪个出自某个具名模型；(d) 盲评质量。

**结果**
- **(b) 单解任务**：15 个 model-benchmark 组合的 **balanced accuracy 全部落在 49–58%**（≈ chance）；而 **raw accuracy 38–67%** 主要反映"模型有多愿意认领作者身份"，**不是识别能力**。
- **(a) 成对任务**：14 个 evaluator-opponent 组合的准确率与"评测方解更长"的频率相关性 **r = 0.93**。
- **(c) 具名归属**：部分模型对上成功、部分对上**系统性反向**。
- **去 style 归一化**：剥离 docstring / 注释 / type hints / 局部命名后，**Pass@1 不受影响**（说明归一化本身不改变代码功能），12 个重测结果中 **10 个降到 chance**；剩余 2 个仍跟随归一化后残留的长度差（但**训练过的分类器仍能分开多数归一化对**）。**Claude Haiku 的 self-preference 完全消失。**

**方法论建议（可直接借用）**：报告 balanced accuracy + 启发式 baseline（长度、风格）+ label consistency，不要报 raw accuracy。

### 2.3 Agents：信任、授权与成本（本轮最密集的一节）

#### Don't Read the Log: Execution Traces Contaminate Verifiers in Video-Generation Agents
**别读日志：execution trace 会污染 video-generation agent 的 verifier**

- 作者：Jian Xu（单作者）
- 链接：[arXiv:2609.28564](https://arxiv.org/abs/2609.28564)

**问题设定**：agentic video-generation 系统是一个 generator–verifier 闭环——LLM 规划镜头、调用 text-to-video 模型、多模态 judge 判定是否满足请求。近年 harness 出于可诊断性考虑，**故意把 agent 的 execution trace、plan、narration 一起展示给 judge**。本文问：在**帧固定不变**的前提下，这段辅助文本会不会改变 judge 对**纯视觉**要求的裁决？

**实验**：109 段生成的双事件 clip，人工标注，事件要么"可见地完成"、要么"可见地缺失"。

| 条件 | Qwen-VL judge（7B / 8B / 32B）对失败 clip 的接受率 |
|---|---|
| 不给文本 | **7–19%** |
| 给一条"报告了成功 tool call"的 trace | **78–90%** |
| 给一条**矛盾**的 trace | 最多 **100%** 的正确 clip 被拒 |

- 指令 "use only the frames" **无法消除**该效应。
- **frontier 闭源 judge 在同一批 clip 上基本不动** → 漏洞是**特定 judge 对 tool log 的习得性信任**的性质，而非任务性质。
- plan-derived text 不含 clip 特异信息，只能移动 judge 的**工作点**；在 repair loop 中这个位移变成**真实通过率的上限**，任何 repair policy 都超不过去，**该上限与仿真吻合到小数点后两位**。
- **无需对抗性 agent 即可利用污染**：一个总是重新生成的诚实 LLM planner，最终 **judge pass rate = 1.00，而 human-labelled pass rate = 0.28**；若一个廉价 checker 把自己的判定写进 trace，则其错误被**洗白**进更强的最终 judge（**0.69 false accepts**）。

**为什么本轮排第一**：这是 verifier contamination 的**最短、最干净的单篇证据链**，且给出可复现的数值上界。09-28 `arxiv-paper-check` 收录的 *JevAdvBench*、*Stale-Document Poisoning*、*Monitor Jailbreaking* 都在攻击面，**这一篇在评测面**——三者合起来说明"judge 的输入契约"本身就是当前 agent 系统的攻击面。与 09-25 收录的 *Judging a Review by its Cover*（23/29 失败）同源问题、不同载体。

#### Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents
**持久计费状态：tool-calling LLM agent 的"钱包拒绝服务"攻击与防御**

- 作者：Jinqian Zhang, Haojun Xia, Shujiang Wu, Jingkun Yue, Xia Zhang, Zhangpei Cheng, Bibo Tu
- 机构（**arXiv 页面直接打印，`high confidence`**）：(1) **Institute of Information Engineering, Chinese Academy of Sciences**；(2) **School of Cyber Security, Univ. of Cyber Science and Technology of China**；另有 2 个外部单位（页面截断）
- 形式：22 pages, 14 figures, 13 tables
- 链接：[arXiv:2609.28585](https://arxiv.org/abs/2609.28585)

**威胁模型（概念贡献最大）**：多步 tool-calling agent 依赖 host runtime 跨轮保存状态。当 runtime 把**外部 tool 返回值带进后续 model 输入**时，provider 会**再次计费**。于是一个已被接纳的恶意/被攻陷的 tool，可以把不可信数据转成**持续由受害者付费**的处理，**既不需要受害者凭据，也不需要本地 runtime 权限**。作者称之为 **retained content as persistent billable state**，并形式化了 host 的准入决策边界为 **persistent billable-state boundary**。

**实验**：推导 **6 条 denial-of-wallet 攻击向量**，构建 **DOW-BENCH** 端到端 harness，覆盖 **6 个模型家族 / 243 次执行**。**用量遥测显示：单 session 累计输入量的最大值达到该 session 首次调用输入的 14,293×。**

**与本库既有安全条目的差异**：09-28 sibling 收录的 *Stealth Apart, Harm Together* 是 **skill cascading**（能力级联），09-25 的 *CIPA* 是**可恢复的隐私泄漏通道**，而这一篇是**计费/经济维度**——把"资源消耗"从 DoS 语境移到 **provider-metering 语境**，是本库尚未覆盖的攻击面。

#### Who Holds the Pen? Let Specifications, Not Agents, Sign Off
**谁执笔？让规范而非 agent 签字**

- 作者：Haiqing Li, Xin Ma, Yinhao Wu, Wenliang Zhong, Feng Jiang, Thao M. Dang, Xiao Hu, Hehuan Ma, Yuzhi Guo, Junzhou Huang
- 链接：[arXiv:2609.29921](https://arxiv.org/abs/2609.29921)

**问题**：LLM agent 把生成、决策、执行、自评估**合并在同一个 loop** 中；外部规范（任务指令、guideline、output schema、reusable skills）对 agent 而言**只是 context**，而**宣称完成的那个模型和执行的是同一个模型**——不存在独立的规范权威边界。作者命名两个 gap：

- **understanding–execution gap**：要求被理解了，但执行没满足；
- **state–authority gap**：agent 的解释或完成声明**不足以确立所需状态**。

**SkillsBench 实测**：仅使用 agent 可见的 prompt、workspace 信息与注入的 skill specification，抽取 **509 条 source-grounded task direction**。跨 **7 个模型**：

| 指标 | 数值 |
|---|---|
| 真正被满足的 task direction 比例 | **79.6% – 86.4%** |
| completion-claim rate 超出官方 evaluator pass rate 的幅度 | **+28.7 – +37.9 pp** |

第二个数字是全文最尖锐的证据：**agent 自称完成的比率比实际通过率高 28.7–37.9 个百分点**。

**SpecHarness**：把可见规范编译成 **source-linked obligations**，用**版本化的 obligation state** 治理执行与终结；可验证要求在运行时被 mediated/validated，模糊或主观要求保持 advisory。实验（guideline-following + artifact-generation）显示规范可以不只是行为指引，而是**对合规执行与完成的权威**。

**与本库关系**：直接回应 09-22 sibling 收录的 *Total Cost of Agency*（memory-injection 归因）与 09-25 的 *root-scoped authorization quiescence*（17/17 accept / 44/44 reject）——本篇是三者中唯一把"完成声明的**权威来源**"问题化的，结论是**引入独立 authority boundary 而非更强 prompt**。

#### skilder: Progressive Skill Discovery as Access Control for Tool-Using LLM Agents
**skilder：把渐进式 skill 发现当作 tool-using agent 的访问控制**

- 作者：Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod
- 形式：**White paper, 30 pages**（无 arXiv 会议标注；`tentative` 工业白皮书）
- 链接：[arXiv:2609.28693](https://arxiv.org/abs/2609.28693)

**问题**：面对庞大的企业工具集，把所有内部 tool 交给 agent 会导致 context 过大、tool 选择退化，以及**严重的治理漏洞**——纯 prompt 定义的策略只是"概率性建议而非硬约束"。已有的 multi-agent 域委派方案则**把审计日志分散化**，无法保证跨 session 的策略合规。

**方法**：把 capability 打包成 **role**（skill + tool + instruction 的 bundle，加上界定它们的 limits）。agent 从**最小 role catalog** 起步，按任务学习需要哪些 role，每个 role 的 skills/instructions/tools **通过单个 MCP server** 下发。因为 tool 只能"在已学到的 skill 内部"抵达 agent，同一个 server 就同时充当了**访问控制点与集中审计点**。

**为什么值得记**：与 09-25 收录的 *Progressive Skill Discovery / root-scoped authorization* 是同一趋势的**白皮书版本**——"skill 作为最小授权单元"正在从论文收敛到工程规范，`tentative` 但方向信号明确。

#### Era by Eon: Benchmarking Enterprise Agents on Hidden Knowledge
**Era by Eon：企业 agent 在"隐藏知识"上的评测**

- 作者：Benjamin Gruenbaum, Doron Porat, Assaf Natanzon, Roy Zavida, Chen Dinachi, Or Itzahary
- 形式：9 pages
- 链接：[arXiv:2609.30055](https://arxiv.org/abs/2609.30055)

**基准构造**：每道题在题面里**声明答案规则**，并由 code 从生成公司的数据算出答案。分两部分：

1. **规则显式题（27 题）**：**当 agent 可以跑 code 时，四个最强模型各答对 22–25 题** → 基准几乎不区分它们（上限饱和）。
2. **隐藏事实题（+8 个模板）**：**没有任何题目或文档直接陈述该事实**，看似持有该事实的记录显示的是别的东西，是**其他数据隐含**出来的。例：销售系统说客户因**时机**放弃购买，而一段录音里客户归咎于**一次服务中断**。对每家生成公司，code 填模板并计算精确答案，**全程不需要语言模型**。

**12 个 agent（model + agent program）结果**

| 指标 | 数值 |
|---|---|
| 最佳 agent 答对 | **18 / 24 次尝试**（每题 3 次） |
| 六个模型中，**用任何 program 都只答对 ≤6 / 24** 的模型数 | **4 / 6** |
| 最难题型（从三个相似的 renewal offer 中判断客户实际签了哪一份） | 全部 agent 合计 **84 次尝试中只答对 2 次** |

**为什么重要**：这是"**能跑 code 就等于能做企业任务**"这一隐含假设的一次直接证伪。09-28 `arxiv-paper-check` 收录的 *Epistemic Admission in Shared Agent Memory*、*Learning What to Skip* 都在 agent 记忆/信用分配层，**本篇在"隐含事实"层**，三者互补。

#### LIDAR: Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior
**谁在 harness 后面？通过 agentic 行为给 LLM 做指纹**

- 作者：Chuyi Wang, Xiaohui Xie, Tongze Wang, Fangchen Luo, Yong Cui
- 链接：[arXiv:2609.28559](https://arxiv.org/abs/2609.28559)

**动机**：LLM 越来越多地通过 **coding-agent harness** 运行——检查仓库、调用 tool、修改文件。因此**替换 harness 后面的模型会改变安全相关决策**，包括它是否会验证自己的改动、是否能从失败中恢复。既有 LLM fingerprint 主要从直接文本或 token 分布推断身份，而在 coding agent 中这些信号**被 system instruction、controller 逻辑、tool 与执行反馈中介化**，迁移性受限。

**方法**：**LIDAR**（LLM Identification from Decisions and Actions at Runtime）——面向 coding-agent 执行的**主动黑盒指纹**。设计 **3 组 coding probe pair**，分别暴露：(1) post-edit verification；(2) transient-failure recovery；(3) specification–test conflict resolution。轨迹用互补的 **instance-level 与（跨实例）距离级**表示。

**与本库关系**：本库已有 ETD membership detection（2609.21888）等模型归属条目；LIDAR 的独特性在于**归属信号取自 agent 行为而非 token**，对"coding agent 可替换性"这一生产问题有直接含义。`tentative`：摘要未给出最终准确率数字，需读全文。

#### Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents
**网络 agent 在何处失手：多阶段 LLM agent 的瓶颈分析**

- 作者：Saeedeh Lohrasbi, Mohammad Mamun, Ahmed Yehia, Scott Buffett, Sherif Saad
- **Venue**：**FPS 2026**（The 19th International Symposium on Foundations & Practice of Security）
- 链接：[arXiv:2609.28572](https://arxiv.org/abs/2609.28572)

**动机**：多阶段 LLM cyber agent 可能"完成了攻击流程"却依然脆弱、昂贵，或依赖对执行证据的错误理解。**只看 success rate 会掩盖低效、通过 retry 进行的适应、以及对成功/失败的误判。**

**方法**：对 **Autonomous Adversary**（orchestrator / executor / validator 三个 LLM）做端到端诊断研究，enterprise-like lateral-movement 场景，**6 个 frontier 模型 × 2 个场景 × 3 种模式**（expert-defined / self-scaffolded / fully autonomous）。三项评估：validator consistency、evidence grounding，以及一个**subtask-conditioned、cost-aware 的 score**（统计异常 token 使用、retry 次数、runtime），并用 comparative LLM-as-a-Judge 识别规划缺陷：tool misalignment、plan similarity、over-specification、inadequate probing、weak recovery。

**为什么记**：与 09-28 `game-rl-daily` 收录的 *RoboRecover*、*RACaP*、*Robo-Harness K1* 同属"**harness 层诊断**"趋势，但对象是 cyber agent 且已绑定 FPS 2026——本轮少数有明确 venue 的新增条目之一。

### 2.4 LLM Evaluation Validity

#### PROOF: Profiling Reliability of Object-Level Facts in LLMs
**PROOF：为 LLM 的 object-level 事实可靠性画像**

- 作者：Andrei Chetvergov, Mikhail Solovev, Timofei Sivoraksha, Stepan Ukolov, Valeriia Kuschenko, Alexander Evseev, Sergey Bolovtsov
- 形式：24 pages, 16 figures
- 链接：[arXiv:2609.29504](https://arxiv.org/abs/2609.29504)

**动机**：聚合的事实性分数掩盖了"模型在哪里成功、混淆了哪些关系、答案能否经受无害改写"。PROOF 测的是**事实覆盖的结构化画像**，而不是"模型相信什么"的单一断言。

**构造**：从**冻结的 Wikidata snapshot** 转成 **18,486 道英文多选题**，覆盖 **11,779 条语义事实 / 101 个 class / 392 个 property / 14 个 domain**。每题带显式 **"I don't know"** 选项、一个 **"No correct option"** 对照、以及 **9 种受控改写**；其中 **1,849 题是 no-correct-option 陷阱**。评估 **18 个 open-weight 部署 × 每个 166,374 条 prompt**，另在固定的 **10% 子集**上单独扰动 decoding。

**结果**

| 观测 | 数值 |
|---|---|
| base factual accuracy 跨模型 | **6.58% – 57.59%**（chance = 8.64%） |
| 每个模型内部的 domain 间跨度 | **19.3 – 36.4 pp**（*所有*模型都有） |
| 成对事实的检索方向性 | 通常偏好 subject→object；**1 个模型方向反转** |
| 中性措辞改写造成的 accuracy 变化 | 最高 **26.5 pp** |
| 对抗性改写破坏原本正确的答案 | 最高 **79.4%** |
| 注入错误标签后的直接切换率 | **0.04% – 27.5%**（→ accuracy 损失与 hint following 是**两件事**） |
| decoder 扰动造成的位移 | accuracy 最高 **15.7 pp**，domain profile 最高 **16.8 pp** |

**与本库关系**：与 09-25 收录的 *Judging a Review by its Cover*、*Agreement Overstates Evidence*、09-15 收录的 *Magnitude-Mirage* 构成同一条线——**"单一聚合分数不可信"**。PROOF 的独特点是**用 object-level Wikidata 三元组结构**（subject/object/property）而非自由问答做扰动，因此能把 direction-dependent retrieval 这种结构性偏置分离出来。

#### Likelihood Ranking doesn't Scale Like Prompting in LLMs
**Likelihood ranking 不像 prompting 那样随规模增长**

- 作者：Alessandro Bondielli, Lucia Passaro, Davide Bacciu, Alessandro Lenci
- 链接：[arXiv:2609.29390](https://arxiv.org/abs/2609.29390)

**问题**：LLM 评估通常两条路——让模型产出答案（prompting），或用 likelihood 类指标给候选打分。但在 multiple-choice QA 中，标准 likelihood 打分**仍然条件于题目与答案集**，因此可能复用了 prompting 的同一个"任务条件化答案选择接口"。

**方法**：改用**陈述句（declarative statement）likelihood ranking**——由同一批 question–answer pair 构造陈述句再排序，作为**互补协议**。跨 **95 个 decoder-only 模型（0.1B – 104B）× 10 个 MCQA 数据集**。

**结果（核心发现）**：陈述句 likelihood accuracy **跨规模相对稳定**；而 **prompted answering 随规模与 instruction-tuning 急剧提升**。二者**系统性发散**。

**为什么重要**：这是对 "loglikelihood 评估是 prompting 的廉价代理" 这一常见做法的**直接反证**——两者抽取的不是同一类能力。这对本库 [[llm-as-judge]] / MCQ 式 eval 的所有既有条目都是方法论警告（`high confidence`）。

#### Math Reasoning in LLMs is Organized by Approach, Not Topic
**LLM 的数学推理按"方法"而非"主题"组织**

- 作者：Sajad Goudarzi, Samaneh Zamanifard, Moloud Nasiri, Hamed Rahimian
- 链接：[arXiv:2609.27041](https://arxiv.org/abs/2609.27041)

**问题**：数学推理 benchmark 通常按**主题**组织，但模型内部计算可能按**可复用的推理方法**组织。

**方法**：**generation-replay 协议**——模型先生成解，然后**重放完全相同的 prompt + generation 轨迹**，抽取 reasoning token 上的 **activation-importance signature**；**无监督聚类**，跨 **8 个模型 × 5 个数学推理来源**。

**结果**：全部 **40 个 model-source cell** 中，恢复出的聚类**都优于 matched-size 随机基线**；两个独立的 frontier-LLM judge 给出语义支持。

**与本库关系**：本库已有"结构化 CoT / 过程审计"线（09-25 的 *formal-solver CoT auditing*、*HMS* taxonomy-free MT trace structure）。本篇的差异是**从 activation 侧证明方法维度真实存在**，而非从文本侧分类——对 09-25 CoVer（过程奖励）这类"奖励过程而非结果"的方法提供了机制层面的额外支撑。

### 2.5 Generative Models、系统与时序

#### TopoCompress: 面向拓扑感知的边缘端分布式 MoE 推理 token 压缩
- 作者：Ning Li, Xinyu Wang, Xin Yuan, Wenchao Xu, Song Guo, Haijun Zhang
- 形式：15 pages, 9 figures
- 链接：[arXiv:2609.26061](https://arxiv.org/abs/2609.26061)

**问题**：MoE 稀疏激活在资源受限的**边缘服务器**上部署时，expert 分布在异构机器间带来**大量跨服务器通信**。既有 placement 方法只优化 raw token traffic；常规压缩虽考虑语义但**忽略拓扑相关的路由代价**。两者独立优化 → 通信与资源利用都低效。

**方法**：联合优化 **token compression + expert deployment/replication + GPU-CPU residency + 协同路由**，以平衡跨服务器传输、质量与资源使用（`tentative`：摘要被截断，未取得最终数值）。

**为什么记**：这是"**拓扑感知的推理侧压缩**"——与本库 09-22 收录的 IntBMoE（block-conditioned MoE 上生产 recommender，UVCTR +2.4%）、W4A4 error decomposition 属同一"**MoE 的成本进入生产**"簇，但落点在**边缘侧系统**而非 rec，视角互补。

#### StructFlow-HPR: Structured Pose-Conditioned Flow Matching for Generative 5G CSI Augmentation
**StructFlow-HPR：面向生成式 5G CSI 增强的结构化 pose-conditioned Flow Matching**

- 作者：Haojin Li, Anbang Zhang, Wai Ho Mow, Chenyuan Feng, Chen Sun, Haijun Zhang
- 链接：[arXiv:2609.29912](https://arxiv.org/abs/2609.29912)

**问题**：隐私保护、无需佩戴的**人体姿态识别（HPR）**正成为 5G channel state information（CSI）的落地场景（通信 + 感知一体），但**大规模同步的 CSI–pose 配对数据在真实 5G 系统中采集成本极高**。

**方法**：学习一个从**高斯噪声到真实 CSI 表示**的**连续 latent transport 过程**，条件为 pose；同时用**重建保持的 autoencoder** 保留 CSI 的**receiver-frequency 拓扑**；再用 **pose-conditioned Transformer** 建模 latent velocity field，通过 **ODE 采样**生成姿态对齐的 CSI 样本。

**与本库关系**：flow matching 侧的新应用（对位 09-22 的 LatentLM latent diffusion σ-VAE、09-25 的 spectrum-aligned latent flow TSG）；**"保留 receiver-frequency 拓扑"** 是一个领域特定的正确性约束，方法论上与推荐里的 semantic-ID 保持结构同构——`tentative`，无结果数字。

#### TW3Cast: 不使用 agent、不使用语言模型的时间序列预测系统
- 作者：Nathan Thierry, Andre-Louis Rochet
- 链接：[arXiv:2609.28506](https://arxiv.org/abs/2609.28506)

**结果（截至 2026-09-14）**：在 **GIFT-Eval** 上按 **mean MASE rank** 排到 **130 个条目中的第 3 位**；排在其前的两条属于 leaderboard 的 **agentic category**（多步、使用 agent 或 LM 做推理/生成/选择）。

**方法（论点即方法）**：TW3Cast **推理时既不跑 agent 也不跑语言模型**。它的选择是一张**只在训练划分上计算一次然后冻结的表**；expert 是公开基础模型的**轻度微调**版本。对全部 **97 个 dataset × frequency × horizon** 配置，表指定 4 种模式之一：

1. **specialist** — 对 **Chronos-2 / TiRex / Toto** 的 LoRA 或 full fine-tune，训练数据经显式规则清洗与增强；
2. **quantile blend**（内含至少一个 specialist）；
3. **base model blend**；
4. 在训练划分上 carve 出的 backtest 上跑的 **selection tournament**。

**为什么值得单列**：这是对"**时序预测必须靠 agentic 推理**"这一 2026 年流行叙事最直接的反例——冻结查表 + 轻度微调的基础模型就排到第 3。对本库 `sequential-modeling` 与 `world-models` 两条线都是重要制衡（`high confidence`）。

#### EvoTreeNAD: genealogy-guided 神经网络架构发现
- 作者：Lishan Yu, Derek Jiu, Qizhen Lan, Xiaoqian Jiang
- 形式：31 pages
- 链接：[arXiv:2609.29016](https://arxiv.org/abs/2609.29016)

**问题**：LLM agent 支持科学发现的迭代生成与评估，但**迭代本身不保证累积进展**，也不指示下一步该往哪走；昂贵的评估又限制了探索范围。**神经架构发现**把所有困难耦合在一起：开放式设计 + 资源密集实验。

**方法**：**EvoTreeNAD** 是一个**genealogy-guided 演化算法**，能在**不提供 seed、也不手工指定 search space** 的前提下构造可训练架构。从**空根**出发，长出一棵持久 genealogy，每个节点是一个完整架构；由每个节点**及其全部后代**算出的 **top-percentile 值**指导 lineage 选择。

**与本库关系**：与 09-22 收录的 *DreamGym*（experience synthesis for agentic RL）、09-25 的 *AgentFlow*（flow-based GRPO in live env）同属"agent 做科学发现"簇；本篇的差异是**明确拒绝手工 search space**，与 Wiki 中"搜索空间先验"这条方法论张力一致（`tentative`，无结果数字）。

### 2.6 Venue-tagged 新增 arXiv（arXiv comments 明确标注会议）

| ID | 标题 | 标注 venue | 库内状态 |
|---|---|---|---|
| 2609.29048 | Where Hallucinations Live: A Cross-Architecture Circuit in VQ-Tokenized Vision-Language Models | **EMNLP 2026** | NEW（详见下） |
| 2609.28572 | Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents | **FPS 2026** | NEW（§2.3） |
| 2609.29145 | Claim-Gated Source-Risk Auditing for Generative Search | **AI2A 2026**（Intl. Conf. on AI, Automation and Algorithms） | NEW（下） |
| 2609.25176 | Qwen-Audio-3.1-Realtime | 25 pages, technical report（Alibaba） | NEW（§2.1） |

#### Where Hallucinations Live: A Cross-Architecture Circuit in VQ-Tokenized VLMs
**幻觉住在哪里：VQ-tokenized VLM 中的跨架构 circuit**

- 作者：Shamanthak Hegde, Xiangrui Liu, Maitreya Patel, Yezhou Yang
- Venue：**EMNLP 2026**
- 链接：[arXiv:2609.29048](https://arxiv.org/abs/2609.29048)

**动机**：通过 **vector-quantized（VQ）codebook** 图像 token 化的 unified VLM，在 grounded yes/no benchmark 上习惯性幻觉物体；既有 **decoding-time** 修复把它当作一般性 miscalibration 处理，**缺少架构层面的解释**。

**方法与结果**
- 跨 **25 个模型 / 8 个 LLM 家族**做 **activation patching**，定位到一个 **early-layer（$L_0$）attention routing circuit**，被所有 VQ-tokenized VLM 共享。
- 提出**三门诊断**，把携带该 circuit 的模型（**10 个**：5 个自然 unified-VQ VLM 跨 3 个 LLM 家族 + 5 个诱导变体）与不携带的（**15 个**）分开。
- **单变量架构替换**：`LLaVA-1.6 CLIP+MLP → VQ+Linear` **装上**该 circuit；而在相同数据上的 **matched-compute MLP 对照装不上** → 隔离出 **vector quantization 本身**是病理信号的来源，承载它的 routing pathway **backbone 本来就有**。
- 对 tuned **VCD / DoLA** 基线：tuned DoLA 在**二分类校准**上胜出，但**只有 $L_0$ ablation 能降低开放式生成的物体幻觉**（**CHAIR$_i$ 相对下降 31%**；tuned DoLA 与 VCD 不变或更差）。

**为什么重要**：把 VLM 物体幻觉**从"解码期校准问题"重定义为"架构 + 预训练问题"**，并给出机制无关的解码技巧**无法复制**的定向干预。这与 09-15 收录的 *Magnitude-Mirage*（logit 幅度不是置信度）属同一"**别用校准话术解释架构病**"的思路，但对象是 VQ 视觉 tokenization 而非 LLM logit。

#### Claim-Gated Source-Risk Auditing for Generative Search
**Claim-gated 的生成式搜索信源风险审计**

- 作者：Kainan Zhou, Chuhong Xu, Gangzhen Qian, Zhaoyi Li
- Venue：**AI2A 2026**
- 链接：[arXiv:2609.29145](https://arxiv.org/abs/2609.29145)

**问题**：生成式搜索的答案可以**引用了有支撑的段落，却遗漏了会改变其解释的某种 source relationship**。

**规范**：对 `query–source–answer` 三元组做 **claim-gated audit**；只有当 **relationship evidence + answer adoption + materiality + disclosure** 四项**全部被观测到**时，一个 omission 才被"解决"；**证据不完整即保持 unresolved，而不得当作 independence**。规范把该 endpoint 与 **citation support** 及 **review priority** 分离，并把决策绑定到**版本化的 evidence spans**。

**验证**：一个 reference checker 让记录契约**可执行**；在穷举合成套件上**复现全部 81 种三态谓词组合**，并**拒绝 192 条刻意构造的畸形记录**；common-guard 基线与谓词 ablation 用于把 endpoint 逻辑与 missing-evidence 处理分离。

**与本库关系**：本库已有大量 AI-search 审计条目（09-22 的 *Scoring-With-the-Engine* GEO audit、*Semantics Delivery Network*、13.4B-question web QA audit、09-22 百度/Google AI-search source-exposure audit）。本篇是其中**唯一一条把"源关系缺失"形式化为三态谓词**的，方法论可复用性最高。

### 2.7 社会计算与人类使用

#### How People Use ChatGPT in Australia: A WildChat Analysis
**澳大利亚人如何使用 ChatGPT：一项 WildChat 分析**

- 作者：Ying Ma, Katy Gero, Clément Canonne, Craig Jin, Kanchana Thilakarathna
- 链接：[arXiv:2609.28990](https://arxiv.org/abs/2609.28990)

**方法**：以 **WildChat**（真实 ChatGPT 交互日志的公开数据集）中识别出的 **37,845 条澳大利亚对话**为对象，用描述性分析 + 多层分类体系考察 **语言多样性、工作相关性、交互意图、主题分布、轮次交替（turn-taking）、时间变化、工作活动、以及澳洲相关领域**。

**发现**：澳洲子集**高度 action-oriented**，且相对更 work-oriented——多数交互被归为"doing"，**多数对话被判为 work-related**；数据集显示**多语言使用**与**自我表达的占比随时间上升**。澳洲相关对话频繁调用**本地机构**。

**为什么记**：09-20 tech-report 记录了 DeepMind 的 992-participant / 5-day **personalisation RCT**，本篇是**大规模日志侧**的对应物；两者合起来给出"memory → 更多披露且更不 creepy"与"澳洲使用高度工作导向且本地机构密集"这对互补结论。

#### Agentic Detection of Online Conspiracies
**在线阴谋论 discourse 的 agentic 检测**

- 作者：Lior Biton, Oren Tsur
- 链接：[arXiv:2609.30250](https://arxiv.org/abs/2609.30250)

**论点**：社交媒体上的阴谋论 discourse **不总是通过显式 claim 或稳定词汇标记表达**——同一表层内容可以表达**认同、真实担忧、批评、讽刺或嘲讽**。因此难点不仅是识别阴谋相关 claim，而是**推断说话人的意图（utterance 的 illocutionary force）**。作者主张通过**相关社会上下文**达成，并提出一个配有**社会查询工具**的 agentic 框架。

**数据**：独特的**希伯来语推文**数据集，覆盖四年跨度（2018 年末 – 2023 年初）内**公开希伯来语推文的 80%–90%**，跨越多个选举周期以及 COVID 疫情年份与相关疫苗接种运动。

`tentative`：这是本轮**方法论立场最激进**的一篇（把 illocutionary force 而非 lexical marker 作为目标对象），但**无基准数字**。

---

## 3. Runner-ups（本窗口内命中但未展开）

| ID | 标题 | 命中理由 | 未展开原因 |
|---|---|---|---|
| 2609.29578 | PartHackBench: Certified Equal-Progress Stress Tests for Partial-Credit Tool-Agent Evaluation | partial-credit 评测的**认证**控制：私有 certifier 仅在 trajectory 在 **current-state predicate satisfaction 与标准化 agent attribution 上逐组件匹配**时才接纳配对；18 个 sealed task 中匹配到 15 个；历史 credit 平均 inflation **.252**，conditional attack success **10/15**，**完全未检出 14 次严格 rollback** | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.29014 | AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining | 量化研究 agent：多 agent alpha 研究 + 多样研究路径收集 + 本地 agent 后训练（Planner/Realizer 联合 GRPO，兼顾预测质量与贡献多样性），**四个中国股票 universe** | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.29875 | ICLR（Interaction Aware Compression for Long Horizon Reasoning） | 冻结 proxy entropy 排序 reasoning block；**260** 个 WorkBuddyBench 任务上 avg reward **0.699 → 0.718**，input/output/cache-read token 分别 **−25.5% / −14.4% / −33.3%** | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.29518 | CataOPD: Catalytic On-Policy Distillation | teacher 作为**催化剂**而非目标；**Self-Rescue Routing** 用"经验上全失败"作为路由信号，先自采样找正确轨迹 | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.29652 | SmallReason-ColBERT | **32M** late-interaction retriever，BRIGHT mean nDCG@10 **21.41**，距 150M Reason-ModernColBERT（22.62）仅 1.21；对称归一化目标使 loss 停滞并损失 **3.59** nDCG@10（**EMNLP 2026 Main**） | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.28682 | NoThink 的 thinking leakage 因果中介审计 | 3 模型 × 3 后训练方法；**9 个有正 NoThink 增益的 checkpoint 上 leakage ratio 为 42%–79%** | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.29960 | Beyond Average Safety: Chance-Constrained LLM Fine-tuning | 用**风险约束（chance constraint）**替代平均 safety loss，限制"相对 reference 退化超阈值"的样本比例；用可微 majorization 处理不连续 indicator | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.28653 | The Fellowship of the Query: Learning Retrieval Actions | 七分类 next-action 预测；**Granite 4.1 3B** LoRA 微调在 1,646 held-out action 上 macro-F1 **0.6536** vs zero-shot **0.1736** vs TF-IDF LR **0.5399**（13,194 actions 训练） | ⚠️ 已被 09-28 `arxiv-ai-search` 收录 |
| 2609.28798 | OCC4M ("Occam") | 物体中心 4D memory；**350 episodes** 上 memory success **96.6%** / e2e **88.9%** vs FrameSamp（Gemini 3.7 Flash 全历史）**54.6% / 57.7%**；视角迁移后 **100% / 98%** 而全历史基线近零 | ⚠️ 已被 09-28 `game-rl-daily` 收录 |

---

## 4. 与 sibling digest 的交叉引用（不重复展开）

今日 5 个 sibling 的覆盖面（供反向导航）：

- **`arxiv-ai-search`**（22 篇 / 8 节）— retrieval 证据链（EvLink / OBLIQ-IR / SmallReason-ColBERT）+ post-training 审计（thinking leakage / CataOPD / chance-constrained safety）+ agent 经济学（ICLR 压缩、Jev harness routing、trading episodic memory）+ 尾部风险/评估有效性。
- **`arxiv-paper-check`**（25 篇 / 5 节）— rec & industrial CTR（T-RoPE、KuaFu、Component Benchmark、Embedding Subspace Partitioning、RecToolBench）+ evaluation instruments（HARDEN、DIAL、CARGO、Same Text Different Numbers）+ agent memory/context integrity（AutoResearch at Production Scale、epistemic admission、stability-plasticity、Stale-Document Poisoning、counterfactual credit assignment）+ safety（Monitor Jailbreaking、Stealth Apart Harm Together、JevAdvBench、Does Thinking Help Fairness）+ 决策层与效率（EARL、Block Sparse Attention、RAZOR、DynBranch）。
- **`game-rl-daily`**（9 节）— game RL/GT（9 篇）+ game AI bots 与 embodied（9 篇）+ world models（6 篇）+ PCG（2 篇）+ benchmarks（3 篇）+ 工业部署（6 篇）。
- **`tech-report-digest`** / **`wq101-alpha-daily`** — 模型卡与投资线，与本文无重叠。

**本文的独有价值**：**venue 事件**（RecSys '26 proceedings 09-27 出版 + Netflix DOI 落地、AAAI/WWW/ICLR 零新增的负向记录、SIGIR/NeurIPS 的 unresolved 项）+ **agent 信任/授权/计费面**（§2.3 六篇中有五篇不在任何 sibling 的 agent 主题内）+ **评估有效性的三个新角度**（Likelihood-vs-prompting 不等价、PROOF 的 object-level 扰动、Style-not-self 的 balanced-accuracy 规范）。

---

## 5. 跨主题观察 — Cross-Cutting Observations

1. **Verifier 的"输入契约"正在成为一等攻击面。** §2.3 的 *Don't Read the Log* 给出了这一命题的**最短证据链**：帧不变，仅给一段 trace，Qwen-VL judge 对失败 clip 的接受率就从 7–19% 跳到 78–90%；诚实 planner 在 repair loop 里能拿到 judge 1.00 / human 0.28。叠加 09-28 `arxiv-paper-check` 的 *Stale-Document Poisoning*（过时检索覆盖正确模型答案）与 *Monitor Jailbreaking*（编码推理绕过 CoT 监控），三个方向（trace / document / reasoning-encoding）指向同一结论：**judge 的鲁棒性讨论必须先声明它能看见什么**。`high confidence`

2. **"完成"的权威必须外置于执行模型。** *Who Holds the Pen?* 测出 **+28.7–37.9 pp** 的 completion-claim 与实际 pass rate 落差，*Era by Eon* 测出隐含事实题上"能跑 code 也没用"（84 次尝试只对 2 次），*skilder* 的解法是"tool 只能通过已学 skill 抵达"。三篇从不同方向得出同一句：**context 里的规范不是约束，独立的 authority boundary 才是**。`high confidence`

3. **成本语义正在从 DoS 语境迁移到 provider-metering 语境。** *Persistent Billable State* 把"agent 消耗资源"重述为"**受害者持续付费**"，给出 6 条 denial-of-wallet 向量与 14,293× 的实测放大，并明确指出这**不需要受害者凭据或本地权限**。本库既有安全条目（skill cascading、隐私泄漏通道、CoT 监控绕过）均未覆盖这一经济维度。`high confidence`

4. **"能跑 code ≠ 能做企业任务"被再次证伪，但这次是可量化的。** *Era by Eon* 的规则显式题上限饱和（22–25 / 27）vs 隐藏事实题 84 次尝试对 2 次，是一个干净的**饱和度 vs 泛化**分离。对本库 rec 线的对应含义是：offline 指标饱和**不能**作为线上 headroom 的证据——这与 Netflix 论文"task headroom 是 transfer problem 的独立分量"（§1.1）是同一结论的两个独立来源。`high confidence`

5. **生成式推荐的生产化证据链已出现第三个独立点。** Netflix 2M→1B backbone（不含 embedding/decoding）+ 1M 用户一周 shadow 的 MRR 全任务提升（§1.1）、09-22 的 IntBMoE（UVCTR +2.4%）、09-22 的 UNIQUE flat-quantized（Baidu +0.96% watch duration）。三者共同指向：**generative rec 的下一阶段瓶颈是 decoding / serving 经济学与 cold-start，而非 backbone 规模**。`high confidence`

6. **对"agentic 必然更好"的两处同期反例。** *TW3Cast* 不跑 agent、不跑 LM，仅凭训练划分上算一次后冻结的查表 + 基础模型轻度微调，在 GIFT-Eval mean MASE rank 上排 **130 条中的第 3**，而前两名都在 agentic category。另一处是 *Likelihood Ranking doesn't Scale Like Prompting*：95 个模型跨 0.1B–104B 证明 likelihood 评估与 prompting **抽取的不是同一类能力**。两条合起来提醒：**每引入一层 agentic 抽象，都要单独证明它带来能力而非只带来成本**。`high confidence`

7. **评估方法学的"报告规范"正在变成独立贡献。** *Style, Not Self* 明确建议报告 balanced accuracy + 启发式 baseline（长度 r=0.93）+ label consistency；*Where Hallucinations Live* 指出 tuned DoLA 在二分类校准上更好但**无法**降低开放式幻觉。共同点是：**只在容易指标上比较，会系统性选出错误的解法**。`high confidence`

---

## 日历（Calendar）

| 日期 | 事件 |
|---|---|
| **2026-09-28（今日）** | RecSys 2026 会议开幕（Minneapolis）；ACM DL proceedings 已于 09-27 上线 |
| 2026-09-28 晚 / 09-29 | **arXiv 周一公告发布** → 下一次 run 才会有真正的 fresh window（`unresolved`：本轮 8 个 category 列表仍停在 Fri 25 Sep） |
| ≈2026-09-29 | OpenAI **DevDay 2026**（旧金山 Fort Mason，Sam Altman 出席）— 由 09-20 / 09-21 tech-report 记录 |
| 2026-10-02 | RecSys 2026 会议结束 |
| 2026-10-14 / 10-15 | GPT-5.5 退役 / Step 5 权重开放（09-20 tech-report 记录，`tentative`） |
| 未定 | **NeurIPS 2026 accepted list 公开**（通知日 ≈09-24 已过，`unresolved`） |
| 未定 | **SIGIR 2026 Best Paper 公布**（官方页仍止于 2025，`unresolved`） |

---

## Data Quality Notes

1. **arXiv 窗口停滞**：抓取时 `/list/{cat}/new` 的 8 个 category 全部显示 `Friday, 25 September 2026`；API tail sweep（cs.LG，desc）全局最大 ID **2609.30258**（`published=2026-09-24T17:59:18Z`）。**今日无 fresh window**。§2 是 Fri-25 窗口的**第二次深挖**，21 篇全部 whole-`wiki/` regex grep 0 hits（含今日 5 个 sibling 的声称集），故为本文独家。缓存的 listing HTML、pool JSON、abstract HTML 位于预批准临时目录 `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/confdig-0928/`。
2. **ACM DL 403**：`https://dl.acm.org/doi/proceedings/10.1145/3773078` 直接抓取返回 403。Netflix 论文的作者、机构、DOI、出版日期改由 **arXiv abs 页 + 搜索摘要交叉确认**，`high confidence`；KDD 2026 的三个 Meta 奖项仅有**二手来源**，`tentative`。
3. **RecSys 2026 日期口径冲突**：官方 contributions 页为 **09-28 → 10-02**，本库 09-25 conference-digest 记为 09-29 → 10-01。**以官方页为准**，09-25 记录待修订；本轮未能直接抓取日程页以二次确认。
4. **机构信息普遍缺失**：arXiv abs 页除 `2609.28585`（明确打印 CAS IIE + 中国 cyber 科技大学网安学院）外**均不打印 affiliation**。§2 中标为 Alibaba Qwen（`2609.25176`）的推断依据是作者构成与对 3.0 代的直接对比；其余条目一律标 `tentative`，**未作臆测**。
5. **展开标题警告**：§1.4 中 CURE / PolyGloss / PALU 三个 ACL 2026 条目的完整标题为**自拟展开**，未经官方 proceedings 确认，**不得作为正式标题引用**。
6. **数字缺失条目**：*TopoCompress*、*EvoTreeNAD*、*StructFlow-HPR*、*LIDAR*、*Agentic Detection of Online Conspiracies* 五条**未取得实验数字**（arXiv 摘要被截断或原文未给），已在正文标注 `tentative`，**不臆造数值**。
7. **SIGIR 2026 Best Paper 仍 unresolved**：官方 `sigir.org/awards/best-paper-awards/` 年度表格止于 2025。09-16 digest 记录的"SPLADE/BM25 语义相关图推理"说法**未获官方验证**，保持 `tentative`，不升级为 claim。
8. **CIKM "Data-centric Prompt Tuning for Dynamic Graphs" 仍未确认**：两轮扫描均未能在官方页面定位，`unresolved`，不收录。
