---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-13
updated: 2026-08-13
sources: [tech-report-digest-2026-08-12.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-13（每日更新；今日重点：**DeepSeek V4 Pro 官方 GA 落地（08-12）**——OpenRouter 上线 `deepseek-v4-pro-0813`（1M ctx、$0.435/$0.87 每 M tokens），V4 Pro（1.6T 总参 / 49B 激活 MoE + CSA）与 V4 Flash（284B / 13B 激活）均 **MIT 开放权重**，"官方窗口第 4 天"悬念终结；**Qwen3.8-Max 开源权重兑现（08-12/13）**——HF 出现 `Qwen/Qwen3.8-2.4T-A95B`（2.4T 总参 / 95B 激活、1M ctx、license `qwen3.8-max`），08-12 双验收日第二个"承诺制发布"落地；**Grok 4.6 官方信息补全（08-12）**——500K ctx、text+image 输入 / text-only 输出、**无输出上限**、$2/$0.50/$6（<200k）与 $4/$1/$12（>200k）、reasoning 四档 low/medium/high/xhigh，"上线无 model card"文档差距收窄；**OpenAI Astra 安全评估（08-07 Preparedness）或首次触及 Critical 网络安全阈值**；**Meta Llama 4 405B 开放权重仍未兑现（持续第 2 天）**——仅 NeuralStack 07-28 预告反复出现，无发布实据；**MiniMax M3 取代 M2.7 成现役旗舰（BenchLM 核实）**；**Mistral 欧洲主权 AI 路线（08-11）**——in-region inference + 开放模型 + 欧洲基础设施，另有 Shieldstral（08-04）与机器人方向 Robostral Navigate；字节 Doubao 155M 周活 / 全球第 4 大 GenAI 应用；智谱口径维持 GLM-5.2 旗舰、GLM-5.3 传闻）
> 交叉观察：08-12 双验收日两大"承诺制发布"在 08-13 兑现其二（DeepSeek V4 Pro GA + Qwen3.8-Max 权重），Meta 405B 独留悬案——"承诺→兑现"信用分化局部修复；中国开源阵营集中放量（DeepSeek V4 MIT + Qwen3.8-Max 2.4T + Baichuan-M2）；Grok 4.6 文档差距收窄但 Grok 4.7/5 仍为传闻；智能体/自我进化叙事延续（MiniMax M3、Mistral Agent 化、Robostral 机器人）。

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek V4 Pro 官方 GA（今日最大落地，08-12）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V4 Pro 官方版上线（OpenRouter GA） |
| **英文标题** | DeepSeek V4 Pro GA on OpenRouter |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4 Pro（**1.6T 总参 / 49B 激活 MoE + CSA**）；V4 Flash（284B 总参 / 13B 激活 MoE + CSA） |
| **发布日期** | GA：**2026-08-12**（08-10~08-20 传闻窗口第 4 天，终落地） |
| **核心创新** | OpenRouter 上架 `deepseek-v4-pro-0813`：**1M ctx**、$0.435 in / $0.87 out 每 M tokens（与官方人民币价 3/6 元一致）；**V4 Pro 与 V4 Flash 均 MIT 开放权重** |
| **论文** | https://releasebot.io/updates/deepseek；V4 技术报告 arXiv:2606.19348 |

> 今日核实：08-06 涨价公告（"涨价先行、GA 随后"）+ API 文档"V4-Pro 正式版将尽快发布"的预期今日兑现——官方窗口（08-10~08-20）第 4 天 GA。Preview 自 04-24 预览近 4 个月后转正；MIT 开放权重意味着 V4 家族全线开源。

### 1.2 DeepSeek-V4-Flash 官方 API 公开 beta（继承 08-12，保留）

- V4-Flash（284B/13B）Agent 能力：Terminal Bench 2.1 **82.7**、NL2Repo **54.2**、Cybergym **76.7**、DeepSWE **54.4**、Toolathlon verified **70.3**、Agent Last Exam **25.2**、Automation Bench **25.1**、DSBench-FullStack **68.7**、DSBench-Hard **59.6**。

---

## 2. OpenAI

### 2.1 Astra 安全评估 / Preparedness 报告（今日新增核实，08-07）

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI Astra Preparedness 评估——或首次触及 Critical 网络安全阈值 |
| **英文标题** | OpenAI Astra Preparedness: potential first Critical cyber threshold |
| **发布机构** | OpenAI |
| **模型系列** | Astra（"next major model"，为 long-running workloads 设计） |
| **发布日期** | 定名 2026-08-01；Preparedness 评估 2026-08-07 |
| **核心创新** | 安全评估或首次将某个能力域评为 **Critical**（网络安全类）；08-01 官方博客确认已解决 10 道数学/理论计算机难题（非软 sofic、Connes rigidity 反例、sphere packing 界、Erdős 问题等） |
| **论文** | OpenAI 官方博客（08-01）+ Preparedness（08-07） |

> 今日核实：公开旗舰仍为 GPT-5.6（System Card 07-09；Sol 为 Plus/Pro 默认、Luna 覆盖 Free/Go、Think 按钮）；"GPT-6"命名官方未确认；Critical 阈值若落地将为 OpenAI 首次，属重大信号（待官方完整报告）。

---

## 3. Meta

### 3.1 Llama 4 405B 开放权重——持续未兑现（第 2 天，08-13 核实）

> ⚠️ **验收结论延续（08-13）："Meta Llama 4 405B 开放权重 08-12 发布"仍未兑现**——08-13 检索仅反复命中 NeuralStack 07-28 同一条预告（405B、原生多模态 text/image/audio、15T tokens 含 2.4T 图文对、11/14 基准匹配或超越 GPT-5、单 H100 32 tok/s、蒸馏 70B 边缘版），**无任何来源证实已实际发布**；llama.com 目录仍仅 Llama 4 Scout/Maverick（2025-04 时代）。

| 项目 | 内容 |
|------|------|
| **中文标题** | Meta Llama 4 405B 开放权重（预告 08-12，未兑现） |
| **英文标题** | Meta Llama 4 405B open weights (promised Aug 12, not delivered) |
| **发布机构** | Meta AI |
| **发布日期** | 预告 08-12；截至 08-13 撰写时未发布 |
| **核心创新** | （预告口径）405B 原生多模态、15T tokens（含 2.4T 图文对）、11/14 基准超 GPT-5 且推理计算量少 38%、70B 蒸馏边缘版 |
| **论文** | NeuralStack 2026-07-28（单一来源，非官方）；官方技术报告仍缺 |

> 延续 08-12 口径：以实际发生为准——实际重大事件为 08-10 开放权重战略转向（开源 30B Muse Glimmer：Apache 2.0、128K ctx、由 Muse Spark 蒸馏 + 承诺数周内开源 Muse Spark 1.2 权重 + Zuckerberg 6000 字文章）。405B 与早期 Behemoth"近 2T"口径矛盾不再适用。

### 3.2 Muse 系列（继承 08-12，保留）

- **Muse Spark Safety & Preparedness Report**（2026-07，arXiv:2606.12429）。
- **Muse Code**（08-05）：AI 编程智能体，$0.20/百万输出 token 低价策略。
- **Muse Spark 1.2**（08-05）：Terminal-Bench 82.9%；权重承诺数周内开源。

---

## 4. Google DeepMind

### 4.1 状态（继承 08-12，保留）

- **领导层改组**（08-05）：Hassabis 转任主席（兼 Alphabet 首席科学家）；Kavukcuoglu 升 SVP（接任实质 CEO）；Jeff Dean 离职创办 Discovery Loop。
- **Gemini 系列**：Gemini 3.1 Pro Model Card（2026-02）为最新 Pro 级卡；**Gemini 4 预训练中**（07-21，"most ambitious pretraining run yet"）；Gemini 3.6 Flash（07-21）；Gemini Robotics 2 / ER 2 / On-Device 2（07-30）。

> 今日核实：8 月无新模型卡（releasebot 仅 Classroom 集成类更新）；Gemini 3.5（2026-05-20）+ Gemini Omni 已在位。

---

## 5. Anthropic

### 5.1 状态（继承 08-12，保留）

- **Fable 5.1 事实核查**（08-03）：无任何官方公告——仅两条 X 泄漏；$10/$50 定价为传闻；Opus 5 已部分超越原 Fable 5。继续不写入正式条目。
- **Claude Mythos Preview System Card**（04-07）：当前最先进闭源前沿；首个按 RSP v3 发布决策审查的系统卡。
- **Claude Opus 5 System Card**（07-24）：SWE-bench Verified 96.0、SWE-bench Pro 79.2、Frontier-Bench v0.1 43.3、ARC-AGI-3 30.2；effort dial $5/$25 每 M in/out。

> 今日核实：08-13 仅 Claude Code 2.1.228 更新，无新模型技术报告。

---

## 6. Mistral

### 6.1 欧洲主权 AI 基础设施（今日新增核实，08-11）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral：in-region 推理、开放模型与欧洲主权 AI 新基础设施 |
| **英文标题** | Mistral: in-region inference, open models, new European infrastructure for sovereign AI |
| **发布机构** | Mistral AI |
| **发布日期** | 2026-08-11（官方博客） |
| **核心创新** | 整合推理基础设施 + 开放模型 + 对欧洲主权 AI 的长期承诺——欧洲数据在欧盟境内处理、开放权重模型为根基 |
| **论文** | mistral.ai 官方博客（08-11） |

### 6.2 Shieldstral 安全产品（今日新增核实，08-04）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 发布 Shieldstral 安全防护产品 |
| **英文标题** | Mistral launches Shieldstral |
| **发布机构** | Mistral AI |
| **发布日期** | 2026-08-04 |
| **核心创新** | 安全/guardrail 产品线（具体规格待官方技术文档） |
| **论文** | mistral.ai 官方发布（08-04） |

### 6.3 机器人方向：Robostral Navigate（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 机器人导航——Robostral Navigate |
| **英文标题** | Robostral Navigate (Mistral AI Science Robotics) |
| **发布机构** | Mistral AI Science Robotics（Théo Cachet、Arjun Majumdar、Srijan Mishra 等） |
| **核心创新** | 面向机器人的导航系统（Navigation）；Mistral 从模型向具身智能方向延伸 |
| **论文** | mistral.ai 研究页（Robostral Navigate） |

> 今日核实：仍无新 LLM 技术报告；"夏季大而稀疏开放 MoE"预告（08-02）未发布，观察项。战略重心转向 Agent / 主权 AI / 具身。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-Max 开源权重兑现（今日落地，08-12/13）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max 开源权重上架（验收日 08-12，今日确认） |
| **英文标题** | Qwen3.8-Max open weights live on HF (acceptance day Aug 12, confirmed) |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8-Max（**2.4T 总参 Sparse MoE / 95B 激活 / 1M ctx / 原生视觉多模态**）；Qwen3.8-27B（同日，27B dense） |
| **发布日期** | API GA：2026-08-03；**权重：2026-08-12/13 上架** |
| **核心创新** | 首个开源权重的 Max 级模型；HF 仓库 `Qwen/Qwen3.8-2.4T-A95B`；**license `qwen3.8-max`**；1M ctx |
| **论文** | https://qwen.ai/blog?id=qwen3.8 |

> 今日核实：08-12 实时检查时 HF 仍无条目、license 未发布，08-13 撰写时**权重已上架**——08-12 双验收日第二个"承诺制发布"兑现（对照 Meta 405B）。此前草案 license 曾含 US/EU/UK/Korea 地域限制争议，最终 license 命名 `qwen3.8-max`，条款需细读。

### 7.2 其他 Qwen 条目（继承 08-12，保留）

- **Qwen3.8-27B**（08-03）；**Qwen3.7-Flash**（07-25）；**Qwen-Audio-3.0-ASR-Flash**（07-30）；**Qwen-UI-Agent TR**（07，arXiv:2607.28227）。

---

## 8. Microsoft（Phi）

### 8.1 Phi-5 状态（继承 08-12，保留）

> 截至 08-13 **仍无 Phi-5 官方技术报告**；MSR 最新技术报告仍为 Phi-4-reasoning-vision-15B（2026-03）；16B/MMLU 86.7% 报道仍为 single-source（GogoAI），未确认。8 月无任何 Phi 新发布（检索核实）。

---

## 9. Apple

### 9.1 AFM 状态（继承 08-12，保留）

- **AFM 3**（技术报告 2026-06-08，WWDC26）：AFM 3 Core（3B 端侧 dense）/ Core Advanced（20B 端侧稀疏，IFP 激活 1–4B）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像）/ AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU）；IFP（Instruction-Following Pruning）；正式发布承诺 "later this summer" 仍未兑现。
- **上一代技术报告**：Apple Intelligence Foundation Language Models Tech Report 2025（2025-07-17）——~3B 端侧 + 服务器 PCC 双模型。

> 今日核实：08-13 仍在"summer"窗口内，无新技术报告。

---

## 10. NVIDIA

### 10.1 Nemotron 3 家族状态（继承 08-12，保留）

- **Nemotron 3.5 Lightning**（08-11）：**30B-A3B** 开放 MoE，面向 always-on agents。
- **Ultra**（06-09）：550B/55B hybrid Mamba-Attention MoE + LatentMoE + MTP + NVFP4；1M ctx。
- **Super**（04-03）：120B/12B；25T tokens。
- **Nano**（08-04）：30B-A3B；吞吐最高 3.3×。

> 今日核实：8 月无新家族技术报告；官方 Nemotron 3 家族总报告仍待发布。

---

## 11. xAI

### 11.1 Grok 4.6 官方信息补全（今日新增核实，08-12）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 官方规格确认 |
| **英文标题** | Grok 4.6 official specs confirmed |
| **发布机构** | xAI |
| **模型系列** | Grok 4.6（基于 Grok 4.5 V9 基座，1.5T 参数） |
| **发布日期** | 约 08-07 上线（第三方 kie.ai）；官方规格 08-12 |
| **核心创新** | **500K ctx**；**text+image 输入 / text-only 输出**；**无输出上限**；定价 $2 in / $0.50 out / $6 cache（**<200k ctx**）与 $4 / $1 / $12（**>200k ctx**）；reasoning 档位 **low / medium / high / xhigh** |
| **论文** | https://x.ai；docs.x.ai（08-12 规格补全） |

> 今日核实：08-12 官方目录补全 4.6 条目——此前"上线无 model card"的文档差距收窄（对比 08-12 时 docs.x.ai 仍仅列 grok-4.5）。Grok 4.7（2.1T）计划 3-4 周后、Grok 5 年内——仍为传闻。

---

## 12. Amazon

### 12.1 Nova 家族状态（继承 08-12，保留）

- **Nova 2 Sonic 2.1**（05-21~05-28 部署）：自回归 transformer 架构（无视觉编码器）。
- **Nova 原版技术报告**（2024）仍为唯一正式技术报告。
- **战略收缩**（07-28）：Nova Premier/Omni/Reel/Canvas 弃用；新旗舰目标 re:Invent 2026 秋。

> 今日核实：无 8 月新报告；re:Invent 2026（11-30~12-04，早鸟注册 08-25 截止）为下一观察点。

---

## 13. ByteDance（字节跳动）

### 13.1 Doubao 应用规模核实（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | 豆包——中国最常用 AI 应用 |
| **英文标题** | Doubao: China's most-used AI app |
| **发布机构** | 字节跳动 |
| **核心创新** | **155M 周活用户**、全球第 4 大 GenAI 应用、2026 春节峰值日活约 **145M**；底层模型品牌 **Seed**（字节 Seed 团队），经**火山引擎**提供 |
| **旗舰模型** | **Doubao Seed 2.0 Pro**（2026-02-14）：text / native video / 全双工语音多模态 |

### 13.2 其他（继承 08-12，保留）

- **>5T/10T 参数新模型训练传闻**（08-06/07，晚点 + FT）：项亮主导、沈科合作；张一鸣 Seed 全员会反蒸馏表态；**未发布，观察项**。
- **Seed2.1 Pro + Turbo**（07）：Agent/代码工程；视频理解多评测 SOTA（含小时级长视频）。

---

## 14. Zhipu（智谱）

### 14.1 GLM 家族状态（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | 智谱 GLM 家族——GLM-5.2 旗舰、GLM-4.7 预算默认 |
| **英文标题** | Zhipu GLM family: GLM-5.2 flagship, GLM-4.7 budget default |
| **发布机构** | 智谱 AI |
| **模型系列** | **GLM-5.2**（2026-06-13）：**744B MoE / 1M ctx / 约 40B active / 成本约 GPT-5.5 的 1/6**；GLM-4.7：预算编码默认（SWE-bench Verified **73.8%**） |
| **发布日期** | GLM-5.2 2026-06-13（MIT 权重） |
| **核心创新** | GLM 系列 MIT 开源；GLM-5.2 为当前确认旗舰 |
| **论文** | 智谱开放平台（GLM-5.2） |

> 今日核实：**GLM-5.5 传闻（"8 月前后"）未确认**——官方叙事已转向 **GLM-5.3**（>1T，新浪财经 07-20 + JPMorgan 8 月预测口径，未发布）；唐杰此前回应"史诗级 plus"。均不入正式条目。

---

## 15. Moonshot（月之暗面）

### 15.1 状态（继承 08-12，保留 + 更新）

- **Kimi K3**（API 07-16；全量权重 + 47 页技术报告 07-27）：2.8T/104B 激活；93 层（69 KDA + 24 Gated MLA）；896 experts；AttnRes；MoonViT-V2；MXFP4/8；1M ctx；首个开源 3T 级模型；WebDev Arena #1。
- **Kimi K4 训练中**（The Information 07-28/29）：寻求更多 NVIDIA Blackwell 芯片，未发布。

> 今日新增核实：08-06 发布 **Kimi Code CLI 0.34.0**（kimi-code@0.34.0）——会话恢复改进、Windows 版 Kimi Computer Use 支持、文件处理优化；**无新模型技术报告**。

---

## 16. InternLM（上海 AI 实验室）

### 16.1 家族状态（今日新增核实，无 8 月新报告）

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM 家族最新状态 |
| **英文标题** | InternLM family latest status |
| **发布机构** | 上海 AI 实验室 |
| **模型系列** | **InternLM3-8B-Instruct**（2026-01-15，4T tokens 训练、训练成本 -75%）；**InternThinker**（2025-11-25，长思维链推理）；**Intern-S2-Preview**（35B 07-17 / 397B 07-18，科学多模态，Apache-2.0）；InternBootCamp & InternThinker·Go（2026-05-23） |
| **发布日期** | 最新 InternBootCamp & InternThinker·Go：2026-05-23 |
| **论文** | https://github.com/InternLM/InternLM |

> 今日核实：无 8 月新报告；InternLM4 官方状态不明（04-13 传闻，未确认）。

---

## 17. Baichuan（百川智能）

### 17.1 家族状态（继承 08-12，保留）

- **Baichuan-M2**（08-11）：**32B** 开源医疗增强；HealthBench **60.1**——以 32B 超 OpenAI 最新开源 gpt-oss-120B。
- **Baichuan-M4**（05-26/06-22）：临床级医疗 Agent；HealthBench 68.6 世界第一；hallucination 3.3%；arXiv:2606.08982。
- **Baichuan-M3**（2026-01）：235B；HealthBench 65.1。
- 家族背景：Baichuan 1–4（通用，2023–2024）+ Baichuan-M1–M4（医疗系列，2025–2026）。

> 今日核实：战略全面转向医疗垂直；M2 为开源线最新，无 8 月新通用模型。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 家族状态（今日新增核实，无 8 月新报告）

| 项目 | 内容 |
|------|------|
| **中文标题** | 阶跃星辰 Step 家族最新状态 |
| **英文标题** | StepFun Step family latest status |
| **发布机构** | 阶跃星辰（StepFun） |
| **模型系列** | **Step 3**（2025-07-31 开源）：**321B 总参 / 38B 激活** MoE，MFA 注意力 + AFD 解码 + StepMesh，8×48GB 显卡可推理；**Step3-VL-10B**（2026-01 开源，10B 多模态，PaCoRe 并行协调推理，arXiv:2601.09668）；**Step 3.7 Flash**（~2026-03 开源，稀疏 MoE 196B+1.8B 总参 / 11B 激活，400 tokens/s，适配 Claude Code/OpenClaw/Hermes） |
| **发布日期** | 最新开源：Step 3.7 Flash（~2026-03，single-source） |
| **论文** | https://github.com/stepfun-ai/Step3 |

> ⚠️ 规格修正：08-12 页 Step-3 记"198B 稀疏 MoE"与官方公告 **321B 总参 / 38B 激活** 不符，本期以官方口径修正（IT之家/InfoQ/维基百科一致）。Step 4 训练（2026-02 宣布启动）为下一观察点。

---

## 19. Yi / 01.AI

### 19.1 状态（今日新增核实，2026 无新旗舰）

| 项目 | 内容 |
|------|------|
| **中文标题** | 零一万物转向企业 AI / 主权 AI 战略 |
| **英文标题** | 01.AI pivots to enterprise & sovereign AI |
| **发布机构** | 01.AI（零一万物） |
| **模型系列** | 最新模型仍为 **Yi-Lightning**（2024-10-16，千亿参数 MoE，Chatbot Arena #6，arXiv:2412.01253） |
| **发布日期** | 最新动态：万策平台（2026-07，企业 AI 决策中枢：老板 AI/投资官 AI/销冠 AI）；哈萨克斯坦 Q.AI 合资企业（2026，前 AI 副部长 Dmitry Mun 任 CEO） |
| **论文** | https://www.01.ai |

> 今日核实：2026 无新旗舰或新技术报告；公司重心转向企业级解决方案、主权 AI 与行业落地，模型开源节奏自 2024 后放缓。

---

## 20. MiniMax

### 20.1 M3 取代 M2.7 成现役旗舰（今日核实 BenchLM）

| 项目 | 内容 |
|------|------|
| **中文标题** | MiniMax M3 为现役旗舰，M2.7 已退出 |
| **英文标题** | MiniMax M3 supersedes M2.7 |
| **发布机构** | MiniMax |
| **模型系列** | **M3**（2026-06-01 发布）：428B、1M ctx、开放权重；BenchLM **68.6**；定价 **$0.3 in / $1.2 out** 每 M tokens。**M2.7**（2026-03-18）：200K ctx、开放权重、非 reasoning；BenchLM #44/218、**63/100**；同价 $0.3/$1.2——**已退役（superseded）** |
| **发布日期** | M3：2026-06-01 |
| **论文** | benchlm.ai（MiniMax 档案）；MiniMax 官方新闻（08-08，M2.7 自我进化全量上线） |

> 今日核实：08-08 新闻中 M2.7"自我进化"（MLE Bench Lite 66.6% 得牌率）为 **M2.7 的最后一个重大动态**，其开源/旗舰地位已被 M3 取代；M4 仍为 H2 2026 承诺；MiniMax H3（07-31/08-02，33B dense 单流 Omni Transformer）在视频生成评测列全球第一。

---

## 交叉观察

- **08-12 双验收日两"承诺制发布"在 08-13 兑现其二**——①DeepSeek V4 Pro **GA + MIT 开放权重**（OpenRouter `deepseek-v4-pro-0813`）；②Qwen3.8-Max **权重上架 HF**（`Qwen/Qwen3.8-2.4T-A95B`、license `qwen3.8-max`）；独余 **Meta Llama 4 405B** 持续未兑现（第 2 天）——"承诺→兑现"信用分化局部修复，Meta 成唯一失约方。
- **中国开源阵营集中放量**：DeepSeek V4 Pro/Flash（MIT）+ Qwen3.8-Max（2.4T 首个 Max 级开源）+ 本月 Baichuan-M2（32B 医疗）+ 7 月 Kimi K3（2.8T，47 页报告）——开放权重追赶速度加快，与闭源前沿"文档差距"形成对照。
- **闭源前沿"文档差距"局部收窄**：Grok 4.6 官方规格补全（500K ctx、无输出上限、reasoning 四档）；OpenAI Astra 或首次触及 Critical 网络安全阈值（重大信号）；DeepSeek V4 Pro GA 终结窗口悬念——但 Meta 405B（无报告）与 Apple AFM 3（"summer"承诺）缺口仍在。
- **智能体 / 自我进化 / 具身叙事延续**：MiniMax M3 接棒 M2.7 自我进化叙事；Mistral 全面转向 Agent 化 + 欧洲主权 AI + 机器人（Robostral Navigate）；字节反蒸馏表态 + Doubao 155M 周活规模化；Step 3.7 Flash 面向生产级 Agent（400 tok/s）。
- **传闻需谨慎（未确认不入正式条目）**：Meta Llama 4 405B（未兑现）、GLM-5.3/5.5（>1T，未发布）、Grok 4.7（2.1T）/Grok 5、Kimi K4、MiniMax M4（H2 2026）、Phi-5（single-source）、Fable 5.1（无官方公告）、InternLM4、字节 >5T/10T 新模型、Mistral 夏季"大而稀疏"开放权重、Astra"GPT-6"命名。
