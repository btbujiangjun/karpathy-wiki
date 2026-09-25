---
title: "LLM Tech Report Digest — 2026-09-25"
type: synthesis
created: 2026-09-25
updated: 2026-09-25
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, medical-ai, inference-infra, on-device, open-source, daily-digest]
---

# LLM Tech Report Digest — 2026-09-25

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-25）
> 增量版：自 2026-09-24 覆盖版续接（★ = 09-25 新增确认；⭐ = 官源补 pin）
> 本日主线：**frontier 官方"卡面"静默第 2 天（Opus 5.5 / Sol / Luna / Grok 4.7 均为 09-23 已录；官方 anthropic.com/system-cards 页复核确认列出 Claude Opus 5.5 = September 2026，无矛盾），今日增量集中在非-frontier 专项：中系开源医疗（Baichuan-M2 开源 32B，HealthBench 60.1@32B 反超 gpt-oss-120b 57.6，单卡可部）、国产推理基础设施 RSI 最小闭环（GLM-5.3-Flash 生产推理全量 10万+ 国产加速器 + Infra Agent 自主优化）、多模态编程迭代（Doubao-Seed-2.1-Pro 0915，token 消耗 −30%+ / 成本较 Claude Opus 4.6 降 ~80%）、图像模型卡补pin（MS MAI-Image-2.6/2.6-Flash 20B diffusion）、Step 5 Preview 官方页 pin、Mistral €3B Series D（事件层）**。事件节点维持：**09-29 OpenAI DevDay（T-4）**、10-14 GPT-5.5 系列退役、10-15 Step 5 权重开源、Mistral Leanstral 1.5 退役 09-30。纪律重申：Fable 5.2 rumor 不采信、Grok 4.7 参数量（2.1T）low confidence、DeepSeek 763B/552B 计量口径差异 tentative、Kimi K4 单一信源 rumor。

---

## 自 2026-09-24 digest 的 Delta（★ = 09-25 新增确认；⭐ = 官源补 pin；✅ = 复核结论）

- ★ **Baichuan-M2 开源**（2026-09-24 新闻/HF 发布；技术报告 arXiv:2509.02208，2025-09 投稿）——32B 医疗推理模型，**Large Verifier System = Patient Simulator（脱敏病历）+ Clinical Rubrics Generator**；多阶段 RL + 改进 GRPO；**HealthBench 60.1 @32B 反超 gpt-oss-120b（57.6）为开源模型最高**，HealthBench Hard 34.7（此前仅 GPT-5 超 32）；单 RTX4090 + 4-bit 可部署；MTP（multi-token prediction）提升解码吞吐；Apache-2.0 开源。Baichuan-M4（arXiv:2606.08982，06 月 SPAR++）维持。
- ★ **Doubao-Seed-2.1-Pro 0915**（2026-09-16 火山引擎发布，产品级更新非报告）——多模态编程国内领先；**28万行 Java ERP 无文档老系统，录屏 + 草图→输出可执行代码**；图像/视频推理 token 消耗 **−30%+**；**¥6/M input · ¥30/M output · 缓存 ¥1.2/M**，综合成本较 Claude Opus 4.6 降近 80%；TRAE / 豆包工作 / 火山方舟 API 全量接入。
- ★ **智谱 GLM RSI 博客**（z.ai 2026-09-17）+ 融资事件（09-13 ~$5B，媒体口径 60% 指向下一代 GLM + RSI）——**GLM-5.3-Flash 全部生产推理跑在 100,000+ 台国产 AI 加速器上**；Infra Agent（GLM-5.3 驱动）构造/调优推理栈；EPD（Encode-Prefill-Decode）解耦、ReplaySSM、W8A8、INT8/FP8/BF16 混合 KV cache、Layer Split；端到端吞吐 **~3×**；匿名模型 62T tokens / 6 天（OpenCode/OpenRouter 榜单）；**修复 3 个真实 bug（TF32 KDA 精度漂移、DeepEP GIL 阻塞、4× 冗余 normalization→1.71×）**。属 research blog，非 model card。
- ★ **Microsoft MAI-Image-2.6 / 2.6-Flash Model Card**（08-14 / 09-04 发布）——**20B non-embedding 参数 diffusion + flow-matching**；text-to-image + image-to-image（外科级编辑）、多图参考、web grounding、动态宽高比；**32K ctx、最大输出 2,359,296 px（1536×1536）**；**Flash 2.8× 快于 GPT-Image-2-Medium**。
- ⭐ **Step 5 Preview 官方页**（stepfun.com/step-5-preview，published 2026-09-23）——**600B-A27B 稀疏 MoE、1M ctx、vision input**、agentic 工作/金融场景旗舰、权重 **10-15 开源**；确认 09-18/20 已录条目。⚠️ HF `SHSLab/Step-5-Preview-BF16` 镜像自称权重"现可获取 / released 09-20"，与官方 10-15 开源口径冲突（tentative，待复核）。
- ★ **Mistral €3B Series D**（2026-09-08，事件层补 pin）——**Samsung 电子 + 欧盟 Scaleup Europe Fund（EQT 管理）+ PSG Equity 领投**；post-money **>€21B（约 $24B）**；欧洲科技公司史上最大股权融资（前一轮 €11.7B / 一年前）。非技术报告。
- ★/⚠️ **NVIDIA Nemotron-3 Ultra Math RL**（ModelDex 09-24 提及）——550B 家族数学推理专精成员、HuggingFace 卡、IMO 2026 金牌集合之一；**日期 low confidence（tentative，官方卡/新闻日期未直接核到）**，先记 signal-layer。
- ✅ **复核清除上一版悬置**：live anthropic.com/system-cards 页**确认列出 Claude Opus 5.5 System Card（September 2026）**——09-22/09-23 记录站得住，无矛盾条目。Apple WWDC26 FM 相关 session（319 PCC / 242 agentic）实为 06-08 WWDC 内容，非 09-24 新，Apple = 维持（AFM 3 年度技术报告仍缺席）。
- ✅ **维持严格不重复**：Claude Opus 5.5（09-22）、GPT-6 Sol/Luna（09-22）、Grok 4.7 Model Card（09-21）、Qwen3.8-Omni（arXiv:2609.25611，09-22）、DeepSeek DSec（arXiv:2609.22978，09-19/23）、Meta Muse Realtime Avatar（09-23）、NVIDIA Nemotron 3 Diarization（09-23）、Google Gemini 3.8 Flash TTS / Flash-Lite TTS（09-23，产品发布非报告）、DeepSeek V4.1-Flash TR（2609.19969）。

---

## 1. Baichuan — Baichuan-M2 开源（★）

- **中文标题**: 百川 M2：大型验证器系统的医疗推理模型（开源发布）
- **英文标题**: Baichuan-M2: Scaling Medical Capability with Large Verifier System
- **发布机构**: Baichuan AI（百川智能）
- **模型名称**: Baichuan-M2-32B（基于 Qwen2.5-32B）
- **发布日期**: 开源 2026-09-24（HF 官方仓库 + 媒体新闻）；技术报告 arXiv:2509.02208（2025-09 投稿）
- **核心参数**: **32B** 参数；**4-bit 量化可在单张 RTX 4090 部署**；Apache-2.0；MTP（multi-token prediction）提升解码吞吐
- **主要创新点**:
  - **Large Verifier System**：Patient Simulator（基于脱敏病历 + 易出错区域）生成高难度训练样本 + Clinical Rubrics Generator（专家临床评分标准集）评估——把"零错误医疗判断"落成可规模化训练与验证的机器
  - 多阶段 RL 流程 + 改进 GRPO：后训练阶段从判别性（Deliberative）到生成性能力递进强化
  - **HealthBench 60.1 @32B**：反超全部开源模型（gpt-oss-120b 57.6），逼近最强闭源（GPT-5 60.8）；**HealthBench Hard 34.7**——此前全网仅 GPT-5 超过 32 分
  - 百川第二个开源医疗模型（M2 技术报告在前、M4 为 06 月 Agent 线）
- **链接**: [arXiv:2509.02208](https://arxiv.org/abs/2509.02208)；[HF baichuan-inc/Baichuan-M2-32B](https://huggingface.co/baichuan-inc/Baichuan-M2-32B)
- **口径注**: 技术报告（2025-09）与开源发布（2026-09-24）相隔近一年，属权重开源事件；HealthBench Hard 数据以 HF README 口径为准（tentative 复现待核）。与 Baichuan-M4 之关系：M4 为临床级长期护理 Agent（SPAR++，幻觉 3.3%），已录于 06 月基线。

## 2. 字节/豆包 — Doubao-Seed-2.1-Pro 0915（★）

- **中文标题**: 豆包大模型 Doubao-Seed-2.1-Pro 0915 版本（新一代多模态编程更新）
- **英文标题**: Doubao-Seed-2.1-Pro 0915 — multimodal coding & inference-efficiency update
- **发布机构**: 字节跳动 / 火山引擎（Volcano Engine）
- **模型名称**: Doubao-Seed-2.1-Pro-0915（Doubao-Seed-Evolving 同步升同版本）
- **发布日期**: 2026-09-16（火山方舟 API 全量开放）
- **核心参数**: 多模态（图像/视频/文本）；图像与视频推理 token 消耗 **−30%+**；定价 **¥6/M input、¥30/M output、缓存 ¥1.2/M**，综合成本较 Claude Opus 4.6 **降近 80%**
- **主要创新点**:
  - **多模态编程国内领先（发布口径）**：28万行 Java ERP 无文档老系统，仅凭录屏 + 草图即产出可执行代码——"看/听/写"统一多模态编程闭环
  - Agent 任务交付可靠性提升（发布口径）；证据溯源 + 幻觉减少
  - VLM 3D 物体识别与密集文档解析增强
  - **Doubao-Seed-Evolving 同步升级**：同一版本底座用于模型迭代（训练-推理同权重），既有 1M ctx / 混合专家路径
  - TRAE（豆包编程 IDE）、豆包工作、火山方舟 API 全量接入
- **链接**: [火山引擎发布（aibase 报道）](https://www.aibase.com/zh/news/31090)；财中社 2026-09-17
- **口径注**: 产品级版本更新（非技术报告/非 System Card）；基准（Terminal Bench 2.1 / SWE-Pro / SciCode 第一梯队等）为发布方口径；"每日 token 调用 180 万亿（截至 2026-06）"为行业统计口径，非本版本专属指标。

## 3. 智谱 GLM — "Toward Recursive Self-Improvement" 推理基础设施博客（★）

- **中文标题**: 迈向递归式自我改进：GLM 如何自建推理基础设施（技术博客）
- **英文标题**: Toward Recursive Self-Improvement: How GLM Built Its Own Inference Infrastructure
- **发布机构**: 智谱 AI（Zhipu AI）
- **模型名称**: GLM-5.3-Flash（博客主体）+ Infra Agent
- **发布日期**: 2026-09-17（z.ai/blog）；融资 09-13（~$5B，媒体口径）
- **核心参数**: GLM-5.3-Flash **全部生产推理跑在 100,000+ 台国产 AI 加速器**上；端到端吞吐 **~3×**（发文口径 3.2×）；匿名模型 6 天训 **62T tokens**（OpenCode/OpenRouter 榜单领跑）
- **主要创新点**:
  - **RSI（Recursive Self-Improvement）最小闭环**：GLM-5.3 驱动 **Infra Agent** 自主构造/调优走国产卡推理栈——"AI 设计 AI（为其后代构建基础设施）"的最小生产化样例
  - 关键工程点：**EPD（Encode-Prefill-Decode）解耦**、**ReplaySSM** 推理状态复用、W8A8、INT8/FP8/BF16 混合精度 KV cache、Layer Split、Sparse attention
  - **Infra Agent 发现并自主修复 3 个真实 bug**：TF32 默认精度在 KDA 路径的精度漂移、DeepEP 分组被 GIL 阻塞、4× 冗余 normalization 合并至 1.71×
  - 叙事：智谱以国产卡栈成本对标境外主流（字节等），重心转向"单位 token 成本 + RSI 迭代速度"
- **链接**: [z.ai/blog/glm-built-its-inference-infrastructure](https://www.z.ai/blog/glm-built-its-inference-infrastructure)
- **口径注**: research blog（非 model card/非技术报告）；吞吐倍数与 62T token 数为博客口径（自评）；智谱融资 ~$5B 为媒体口径，60% 投向下一代 GLM + RSI 是公司声明方向，未单列账目。与 09-24 已录 GLM 条目（CyberGym 84.5、NIST CAISI 补 pin、GLM-5.3 ≈ 5.3-Flash 维持）同线。

## 4. Microsoft — MAI-Image-2.6 / 2.6-Flash Model Card（★）

- **中文标题**: Microsoft MAI-Image-2.6 系列（图像生成与编辑）模型卡
- **英文标题**: Microsoft MAI-Image-2.6 & MAI-Image-2.6-Flash Model Card
- **发布机构**: Microsoft（MAI）
- **模型名称**: MAI-Image-2.6 / MAI-Image-2.6-Flash
- **发布日期**: MAI-Image-2.6 08-14、2.6-Flash 09-04（公开）
- **核心参数**: **20B non-embedding 参数**；diffusion + flow-matching 训练；**32K 上下文**；最大输出 **2,359,296 px（1536×1536）**；动态宽高比
- **主要创新点**:
  - 一个模型同时覆盖 **text-to-image 与 image-to-image 外科级编辑**（多图参考、局部保持）
  - web grounding（联网参考）与多图 reference editing
  - Flash 版面向成本敏感场景：**比 GPT-Image-2-Medium 快 2.8×**（官方口径）
  - 微软 09-04 "Pushing the quality-cost frontier" 叙事：图像生成走向"质量×成本"双轴竞争
- **链接**: [MAI-Image-2.6 Model Card (PDF)](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- **口径注**: 模型卡为官方 PDF（08-14/09-04 两份发布时间戳）；"2.8×"与质量对比为微软自评口径。此为图像线 Model Card，与 06-02 MAI-Thinking-1 白皮书 / 08 月 MAI-Code-1.1-Flash 并列，微软 MAI 家族目前三线（推理/编码/图像）齐备。

## 5. StepFun — Step 5 Preview 官方页 pin（⭐ / ⚠️）

- **中文标题**: 阶跃星辰 Step 5 Preview（旗舰稀疏 MoE）官方页
- **英文标题**: Step 5 Preview — flagship sparse MoE for agentic work
- **发布机构**: StepFun（阶跃星辰）
- **模型名称**: Step 5 Preview
- **发布日期**: 官方页 published 2026-09-23（确认 09-18/20 已录条目）
- **核心参数**: **600B total / 27B active 稀疏 MoE**；**1M ctx（Sparse GQA）**；原生 text + vision input；四档 reasoning effort；并行工具调用 + 严格 JSON schema 输出；OpenAI 兼容 API
- **主要创新点**:
  - Agentic work / 金融计算场景旗舰（发布口径）；成本化部署强调"单任务成本 ≈ 1/8 Claude Opus 5"
  - **权重开源时间承诺 10-15**——与 GPT-5.5 系列退役（10-14）相邻，构成 10 月中旬事件窗口
- **链接**: [stepfun.com/step-5-preview](https://www.stepfun.com/step-5-preview)；[HF SHSLab/Step-5-Preview-BF16](https://huggingface.co/SHSLab/Step-5-Preview-BF16)
- **口径注**: 维持 09-18/20 记录，本日补官源。⚠️ HF `SHSLab/Step-5-Preview-BF16` 镜像 README 自称"released 2026-09-20 / weights available now"，与官方页"open weights 10-15"冲突——判为镜像/第三方仓库，不替代官方口径（tentative，待官方确认）。

---

## 6. 其他目标机构（逐家复核 — 无新增技术报告，参照 09-24 覆盖版）

| 机构 | 最新有效报告 | 日期 | 状态 |
|------|-------------|------|------|
| Anthropic | Claude Opus 5.5 System Card（官方 system-cards 页确认 = September 2026；SOTA Terminal-Bench 4.0/CursorBench/GDPval-AA；成本 -40%） | 09-22 | 维持（官方页复核无矛盾） |
| OpenAI | GPT-6 Sol & Luna（$2/$10、$0.10/$0.50；Astra System Card 09-22 附录）；**DevDay 09-29（T-4）** | 09-22 | 维持 |
| xAI | Grok 4.7 官方 Model Card（500K ctx、四档 effort；参数量 2.1T low confidence） | 09-21 | 维持 |
| Google/DeepMind | Gemini 3.8 Flash Model Card + 3.8 Live/ET；3.8 Flash TTS & Flash-Lite TTS（产品发布非报告） | 09-02 起 | 维持 |
| Meta（模型线） | Muse Spark 1.3（1.05M ctx）；Muse Realtime Avatar 已录（09-23 ★） | 09-02 起 | 维持 |
| DeepSeek | V4.1-Flash TR（2609.19969）；DSec 已录（09-23 ★）；763B/552B 口径 tentative | 09-17 起 | 维持 |
| NVIDIA | Nemotron 3 Family TR + 3.5 Lightning；Diarization 已录（09-23 ★）；**★/⚠️ Ultra Math RL（ModelDex 09-24 提及，tentative）** | 2025-12 起 | 维持 + signal |
| Apple | AFM 3（Core 3B / Core Advanced 20B）；年度技术报告仍缺席；WWDC26 FM session 为 06-08 内容 | 06-08 | 维持 |
| Qwen | Qwen3.8-Omni TR（2609.25611，09-22 ★ 已录）；⭐ **Qwen4 家族路线图（Apsara 09-22 预告：Max/Flash/Plus/27B, "Coming Soon"，仍在训练）** | 09-22 起 | 维持 + 补 pin |
| Moonshot | Kimi K3（2607.24653）+ AWS 收入分成（09-18）；KimiCode Desktop（09-21）；K4 = 单一信源 rumor | 07-16 起 | 维持 |
| Mistral | Ministral 3（2601.08584）；**★ 09-08 €3B Series D（>€21B post-money，欧洲最大）**；Leanstral 1.5 退役 09-30 | 2026-01 | 维持 + 事件 |
| Amazon | Nova 2 Family TR（Lite/Pro/Omni/Sonic，≤1M ctx） | 2025-12-02 | 维持 |
| Baichuan | **★ M2 开源（09-24，HealthBench 60.1 @32B）；M4（2606.08982）维持** | 06 / 09 | ★ 见 §1 |
| InternLM | Intern-S2-397B（Apache-2.0，09-13）；Intern-S2-Preview（2608.13505） | 09-13 | 维持 |
| 01.AI | Yi-Lightning（2024-10-16）零动态（第六次复核一致） | — | 维持 |
| MiniMax | M3（428B-A23B）；H3 视频（08-26）；M3.1/M3 Pro 预告（MSA 2.0、~3T，财报口径） | 06-16 | 维持 |

---

## 本日头条与动态（相对 2026-09-24 覆盖版）

### 1. 卡面静默第 2 天 + 增量重心转向"开源医疗与国产推理闭环"
- 09-22 三卡窗口（Opus 5.5 / Sol / Luna / Grok 卡）后第 2 天无新卡；官方 system-cards 页复核确认 Opus 5.5 在列（无矛盾）。今日增量由**中系公司担纲**：Baichuan 开源医疗 32B（HealthBench 反超开源之最）、智谱自建国产卡 RSI 闭环（10万+ 卡 + Infra Agent 修复真实 bug）、字节多模态编程迭代（0915）——与 09-24 的 DeepSeek DSec（Agent 沙盒）同属"中国 AI 公司把功夫下在模型以外的规模与基础设施"叙事。**09-29 DevDay 为下一个卡面观察节点（T-4）**。

### 2. "开源 + 垂直能力"成为中系 Top 特征
- Baichuan-M2（医疗）、Intern-S2（通用 397B 闭源对标开源）、DeepSeek V4.1-Flash（推理成本）、GLM RSI（国产卡栈）——一周内中系开源的差异化不再是"参数对标 frontier"，而是**单域能力密度（医疗基准反超）与基建闭环（国产卡 RSI）**。

### 3. 今日 Delta 汇总（★ 新增 5 项；⭐ 补 pin 3 项；✅ 复核 1 项）
| 公司/机构 | 新增项 | 日期 | 类型 |
|-----------|--------|------|------|
| Baichuan | **M2 开源 32B**（Large Verifier System，HealthBench 60.1@32B 反超 gpt-oss-120b，单卡 4-bit，Apache-2.0）★ | 2026-09-24 | 开源模型/模型卡级 |
| 字节/豆包 | **Doubao-Seed-2.1-Pro 0915**（多模态编程、token −30%+、¥6/¥30、vs Opus 4.6 −80% 成本）★ | 2026-09-16 | 产品级版本更新 |
| 智谱 GLM | **RSI 推理基础设施博客**（10万+ 国产卡、EPD/ReplaySSM、Infra Agent 修 3 bug、62T/6天）★ | 2026-09-17 | 技术博客 |
| Microsoft | **MAI-Image-2.6 / 2.6-Flash Model Card**（20B diffusion、32K ctx、2.6-Flash 2.8×）★ | 08-14 / 09-04 | Model Card |
| Mistral | **€3B Series D**（Samsung + EU Scaleup Europe + PSG，>€21B，欧洲最大）★ | 2026-09-08 | 融资事件 |
| StepFun | **Step 5 Preview 官方页 pin**（600B-A27B、1M ctx、权重 10-15；⚠️ HF 镜像口径冲突）⭐ | 2026-09-23 | 官源确认 |
| Qwen | **Qwen4 家族路线图预告**（Apsara 09-22：Max/Flash/Plus/27B "Coming Soon"）⭐ | 2026-09-22 | 路线图事件 |
| NVIDIA | **Nemotron-3 Ultra Math RL**（ModelDex 09-24 提及，550B 数学专精，IMO 金牌集合；日期 tentative）★/⚠️ | ~09-24 | signal-layer |
| Anthropic | **官方 system-cards 复核：Opus 5.5 在列（Sept 2026）**——无矛盾 ✅ | 09-25 复核 | 复核结论 |

---

## 交叉主题分析

### 1. "卡面静默"的正确读法：三层输出并行
- 本周无新 frontier 卡，但 arXiv（Qwen3.8-Omni、DSec、V4.1-Flash）+ Model Card（Nemotron Diarization、MAI-Image-2.6）+ research blog（Meta Avatar、GLM RSI）三层输出连续。**"tech-report digest"跟踪的是卡面 + 论文 + 模型卡三轨**，静默期反而进入"农历月季末技术释放季"（中系密集开源）。

### 2. 中国"基建叙事"本周四连胜
- DeepSeek DSec（沙盒规模化，每日 3M 沙盒）+ GLM RSI（国产 10万+ 卡推理栈 + Infra Agent 自主修 bug）+ Baichuan-M2 开源（医疗单域密度）+ 字节 Doubao 0915（token 成本 −30%）——四个不同维度同一主题：**竞争焦点从"单模型指标"转向"训练/推理基建闭环 + 单域能力密度 + 单位成本"**。

### 3. 医疗专用模型进入"达 FM 级但更轻"赛道
- Baichuan-M2（32B/单卡）HealthBench 60.1 逼近 GPT-5（60.8），Hard 34.7 仅 GPT-5 更高——主流通用 frontier 模型的医疗面被一个国产开源 32B 近距离贴上；与 Baichuan-M4 的 Agent 线（只读病历→治病）汇流成"医疗 = 首个'垂直卡面化'的领域"。

### 4. 纪律复核（维持 + 新增观察）
- 维持：Fable 5.2 rumor 不采信；Grok 4.7 参数量 2.1T low confidence；DeepSeek 763B vs 552B 口径 tentative；Kimi K4 单一信源；Opus 5.2 灰度 signal-layer 不入 claim 页。
- 新增观察：Nemotron-3 Ultra Math RL 为 ModelDex 单一信源且日期未独立核到（tentative）；Step 5 Preview HF 镜像（SHSLab）与官方 10-15 开源口径冲突（待复核）；Baichuan-M2 HealthBench 为 HF README 自评口径；GLM 吞吐/62T 为博客自评。Apple 无新（WWDC26 FM 内容为 06-08）。

---

*Generated 2026-09-25. Sources: Web 复核（anthropic.com/system-cards【确认 Opus 5.5 = Sept 2026】、arXiv:2509.02208 Baichuan-M2 + HF baichuan-inc/Baichuan-M2-32B、火山引擎 Doubao-Seed-2.1-Pro 0915 0916（aibase/财中社 09-17）、z.ai/blog/glm-built-its-inference-infrastructure 09-17 + 智谱融资 09-13 媒体报道、microsoft.ai MAI-Image-2.6/2.6-Flash Model Card 08-14/09-04、stepfun.com/step-5-preview 09-23 + HF SHSLab/Step-5-Preview-BF16、Mistral 09-08 Series D（Reuters/CNBC）、ModelDex 09-24（GPT-6 Sol/Luna 降价 50%、Opus 5.5 发布、Grok 4.7、Nemotron-3 Ultra Math RL、Muse Spark 1.3）。Cross-referenced with wiki/synthesis/2026-09-24/tech-report-digest.md（覆盖版基线）、wiki/synthesis/2026-09-23/tech-report-digest.md、wiki/synthesis/2026-09-22/tech-report-digest.md（增量基线）、wiki/synthesis/2026-09-24/arxiv-daily.md 与 2026-09-25/arxiv-daily.md / arxiv-ai-search.md（arXiv 互证）。*