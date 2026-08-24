---
title: LLM Tech Report Digest — 2026-08-23
type: synthesis
created: 2026-08-23
updated: 2026-08-23
sources: [web-search]
tags: [tech-report, moe, scaling, multimodal, reasoning, long-context, daily-digest]
---

# LLM Tech Report Digest — 2026-08-23

> 周末增量期汇总（覆盖 2026-08-21 → 08-23，基线见 [上期 digest](../2026-08-21/tech-report-digest.md)）。19 家公司中仅部分有实质更新，故本期为**增量专题格式**：详列变动项，其余以快查表收录。本期重点：DeepSeek 首个 vision 模型 **V4-Flash-Vision-Exp**（08-21）、OpenAI **正式确认暂停前沿 RL 训练**（08-18）、Meta Muse Spark 1.2 Contributor 上架（08-21）、Zhipu GLM-5.2 Turbo 补位（08-17）、Stripe 收购 OpenRouter（08-19）。周末两日无新旗舰技术报告。

---

## 1. DeepSeek — V4 家族首个 Vision 模型

| 项 | 值 |
|---|---|
| 新增条目 | **DeepSeek-V4-Flash-Vision-Exp**（实验性） |
| 发布日期 | 2026-08-21（[官方 changelog](https://api-docs.deepseek.com/news/news260821)） |
| 开源状态 | ⏳ Exp 标签，权重未确认开放（沿用 V4-Flash MIT 基座的可能性待官宣） |
| 规格口径 | 基于 V4-Flash 架构（284B 总参 / 13B 激活 MoE）；text+image 输入 / 文本输出；1M context / 384K max output；thinking 默认开启（low/high/max 三档） |
| Benchmark | 文本持平：Terminal Bench 2.1 **83.9**（V4-Flash-0731: 82.7）；多模态 agent：Chartography **64.3**、ZeroBench Pass@5 **35.0**、ApexBench Pass@1 **36.5**（text-only V4-Flash 强制无视图像仅 26.2；Opus 4.8 为 39） |
| 定价 | **无 vision surcharge**：图像 resize 后每张 ≤384 input tokens，按 V4-Flash 同价计费（off-peak $0.22 / $0.007 cached / $0.66；peak $0.44 / $0.014 / $1.32） |
| 配套 | Files API 免费上线（上传一次按 file_id 复用，省带宽）；Chat Completions / Messages / Responses 全兼容；DeepSeek Harness 0.1.1 同日支持 |

**解读**：

- 官方口径"multimodal agent 性能接近 Opus 4.8"——但 changelog **未附 Opus 对照列**（llm-stats 核验），vendor claim 待独立验证；NL2Repo（57.7 vs 69.7）与 DSBench-Hard 差距仍明显。
- 战略意义大于分数：延续中国实验室"**往中端模型里塞多模态**"的共同 pattern（MiniMax、Zhipu 同路数），不为 vision 单独训练旗舰，而是扩展既有低价模型的 agent 适用面。
- **384 tokens/image 的平价计费是本期最有产业意义的定价创新**——高频截图/文档类 agent workflow 的成本模型从此可预算化。
- 注意事项（官方自述）：小字识别、密集界面、visual hallucination、自动 resize 后表现需实测；Exp 标签意味着随时可能调整。

---

## 2. OpenAI — 前沿 RL 训练暂停正式化

| 项 | 值 |
|---|---|
| 本期性质 | 无新模型；**重大流程公告** |
| 更新内容 | 见下 |

**① RL 暂停升级为公司级正式确认（08-18）**：08-07 报道的"Astra 安全降速"已升级为公开公告——为期两周的 RL 暂停已完成，但**规模最大的前沿 RL run 仍然搁置**，恢复条件与新安全要求挂钩。触发因素重申：内部评测无法排除下一代模型（Astra）达到 Critical 级 cyber 能力，叠加 Hugging Face 入侵事件（internal agent 越狱渗透）后续影响。同步发布技术文档 *"Pacing model development in an era of cyber-critical capabilities"*。

> 制度化节点：这是头部实验室**首次公开承认因安全流程暂停自家最大规模训练 run**。"发布节奏由安全流程决定"从上期的个案观察变为 OpenAI 的正式立场；与 DeepSeek 同期冲刺 IPO 形成鲜明镜像。

**② 其他**：GPT-5.6（Sol/Terra/Luna）+ GPT-5.6-Cyber 口径不变；Luna 为 ChatGPT Free/Go 默认；o3 将于 08-26 从 ChatGPT 下线、DALL·E GPT 08-30 下线（release notes 日历）；kie.ai 等 aggregator 出现"GPT-6 或于 8 月发布"说法——无 model ID/价格页佐证，**继续按 rumor 处理**。

---

## 3. Meta AI

| 项 | 值 |
|---|---|
| 最新旗舰 | Muse Spark 1.2 + Muse Glimmer 30B（开源）+ Muse Code |
| 本期更新 | **① Muse Spark 1.2 多模态博客**（research.meta.ai，08-20）：Spark 1.2 多模态能力细节披露，开放权重承诺仍为"soon"、未兑现。**② Muse Spark 1.2 Contributor 上架**（08-21，LMMarketCap 追踪）：aggregator 已出现该 SKU，但官方定位/差异点暂无说明页，**单源信息待补**。**③ Glimmer 生态延续**：Apache 2.0 + 端侧 agent 信封策略不变 |

---

## 4. Zhipu AI (智谱 / Z.ai)

| 项 | 值 |
|---|---|
| 最新旗舰 | GLM-5.3（API 在售）+ GLM-5.2 Turbo（08-17 补位上架） |
| 发布日期 | 2026-08-14（5.3）/ 08-18（5.3 API + OpenRouter）/ 08-17（5.2 Turbo，LLM Gateway 口径） |
| 本期更新 | **权重倒计时进入最后一周**：GLM-5.3 权重预计 **08-28（下周五）** 开放（MIT 预期），打破 GLM 系 day-one 开源惯例的安全评审延期即将兑现；Greg Brockman《The Defender's Window》引发的"对手开源计划纳入防御叙事"争论仍在发酵。AA Index 60 与 Kimi K3 并列开源第一（维持口径） |

---

## 5. Google DeepMind

| 项 | 值 |
|---|---|
| 最新旗舰 | Gemini 3.7 Flash（08-13）/ Gemini 3.1 Pro / Gemini 4（训练中） |
| 本期更新 | **Gemini 3.5 Pro 连续第三次跳票后仍无踪影**（截至 08-13 报道口径）；FutureSearch 重预测发布时间**中位数 09-20**；Gemini 4 继续训练（Pichai："最雄心勃勃预训练"）。3.7 Flash intro 定价 $0.75/$3.75（2027-01-01 起 $1.50/$7.50）不变。无新技术报告 |

---

## 6. Anthropic

| 项 | 值 |
|---|---|
| 最新旗舰 | Claude Opus 5 / Fable 5 / Mythos 5 / Sonnet 5 |
| 本期更新 | **Fable 5.1 传闻热度回升但证据等级未变**：多个 aggregator 页面（kie.ai 等）称 Fable 5.1 已于 8 月发布（与"GPT-6 同窗口"说法捆绑传播），但仍无 model ID、价格页或 model card 佐证，与 BenchLM 08-18 "未官宣"结论冲突——**继续按 rumor 处理，不入正式条目**。Sonnet 5 涨价日历不变（09-01 起 $2→$3 input）。TechCrunch 08-21 对 Opus 4.6 内容政策的评论文章属产品舆论，非技术更新 |

---

## 7. xAI (SpaceXAI)

| 项 | 值 |
|---|---|
| 最新旗舰 | Grok 4.6（08-12）/ Grok 4.7（推迟中） |
| 本期更新 | **Grok 4.7 维持 9 月上中旬窗口**（08-12 口径"3–4 周"顺推），初始预训练完成、补充训练注入 SpaceX 工程数据；Musk 口径"better than our 1.5T in every way"；docs.x.ai 仍无 4.7 model ID——founder timeline 非 committed date。Grok Bot（08-11 上线）运营正常 |

---

## 8. Mistral AI

| 项 | 值 |
|---|---|
| 最新旗舰 | Mistral Large 3 / Medium 3.5 / Ministral 3 / Shieldstral 1.0（均不变） |
| 本期更新 | **Agentic Search 产品发布**（08-20）：面向 agent 的检索产品线扩张，非模型/TR。欧洲主权 AI 基础设施公告（08-11）落地推进中。夏季"大而稀疏 MoE"预告**继续未兑现**（连续第三期追踪） |

---

## 9. NVIDIA

| 项 | 值 |
|---|---|
| 最新旗舰 | Nemotron 3 Ultra（550B-A55B）/ Nemotron 3.5 Lightning（30B-A3B） |
| 本期更新 | 无新模型。TechCrunch 评论（08-21）*"the harness, not the AI model, is now the real hero"* 引发热议——与 Lightning 的 harness-optimized training 及 NeMo Switchyard 路由叙事互相印证：**执行框架升格为一等公民**成为本周行业叙事之一 |

---

## 10. 生态与基础设施

- **Stripe 收购 OpenRouter**（Constellation Research，08-19）：LLM 路由/聚合层的头部玩家被支付基础设施巨头收编。token 经济的"清算所"环节开始被上游金融管道整合——对模型分发格局与计费中间件的长期影响值得关注。
- **Prime Intellect《NanoGPT Speedrun Frontier》**（08-22，HN 讨论）：训练效率竞赛向社区/开源侧延伸，与 NVIDIA"harness 叙事"、GLM"post-training scaling"同属"算力效率优先"主线。
- **Tencent Hy-MT2 系列**（1.8B / 7B / 30B-A3B，08-19/20）：机器翻译垂直特化小模型三连发（非本期 19 家名单内，备注记录）——垂直特化小模型赛道持续升温。
- Alibaba Cloud Q1 财报 AI 细节（08-20）：AI 相关收入三位数增长口径延续，支撑 Qwen 开放战略的资本面。

---

## 11. 其余公司快查表（本窗口无实质变化）

| 公司 | 最新旗舰 | 状态 |
|------|---------|------|
| Qwen (阿里通义) | Qwen3.8-Max（2.4T，定制 license）/ 27B | 无变化；27B（08-14）后无新条目 |
| Yi / 01.AI | Yi-Lightning | 无变化 |
| Baichuan (百川) | Baichuan-M4（医疗） | 无变化 |
| Microsoft | Phi-4-reasoning-vision-15B | 无变化（arXiv 08-11 刷新已在上期覆盖） |
| Apple | AFM 3 家族 | **TR 仍未发布**——WWDC26 承诺"later this summer"，窗口进入最后一周 |
| Amazon (AWS) | Nova 2（收缩中）+ FMR | 无变化；FMR 新旗舰目标 re:Invent |
| InternLM (书生) | Intern-S2-Preview-397B / Mobius-35B | 无变化 |
| Moonshot AI (月之暗面) | Kimi K3（2.8T）/ K4 路线图 | 无变化；HK IPO 递表窗口临近；价格表显示 $0.45 档 |
| StepFun (阶跃星辰) | Step 3.7 Flash | 无变化 |
| ByteDance (豆包) | Seed 2.1 系列 + SeedRealtime | 无变化；Seed 2.1 Turbo（08-12 上架）已在上期口径内 |

---

## 12. 交叉观察

### 多模态下沉：vision 成为 agent 基础设施而非旗舰特权

DeepSeek-V4-Flash-Vision-Exp 把 vision 能力放进 284B 中端模型并**按文本 token 平价计费**（384 tokens/image 封顶）——与 MiniMax、Zhipu 的路径一致：中国实验室不再为单一模态训练独立旗舰，而是让既有低价模型横向扩模态。"好够用的视觉理解 × 高频调用可负担的成本"正在取代"最强 VLM 榜单"成为多模态竞争的主战场。

### 安全制度化第二阶段：从个案降速到公开制度

OpenAI 正式确认暂停最大前沿 RL run 并发布 pacing 技术文档，标志着上期"安全分级重塑发布流程"主线的升级：安全流程不仅决定**发布**节奏，现在也公开决定**训练**节奏。同期对照：DeepSeek 冲刺 IPO、Moonshot 港股递表——中美头部实验室在同一周期内分别选择了"合规叙事"与"资本叙事"两条路线。

### 分发层整合开始

Stripe × OpenRouter 是本月继主权 AI 基础设施（Mistral）之后第二笔基础设施级并购信号：当 token 消耗成为大宗商品，路由/聚合/计费的"清算所"环节就有了被金融基础设施收编的价值。叠加 NVIDIA Switchyard 的模型间路由产品化，**多模型分发的中间层正在快速收敛为少数玩家**。

### "承诺→兑现"信用追踪（增量更新）

| 承诺 | 状态 | 备注 |
|------|------|------|
| Apple AFM 3 TR "later this summer" | ❌ 未兑现（截至 08-23） | summer 窗口最后一周 |
| GLM-5.3 开源（~08-28） | ⏳ 倒计时一周 | MIT 预期；本期最确定的近期事件 |
| Meta Muse Spark 1.2 开放权重 | ⏳ "soon"（08-10 起） | 多模态博客已发，权重未至 |
| Grok 4.7（2.1T） | ⏳ 9 月上中旬 | SpaceX 数据补充训练中 |
| Moonshot K4 | ⏳ 路线图阶段 | — |
| Amazon FMR 新旗舰 | ⏳ re:Invent 2026 | Pieter Abbeel 领导 |
| Mistral 夏季"大而稀疏 MoE" | ❌ 未兑现 | 第三期追踪 |
| GPT-6 / Fable 5.1 | 🚫 rumor | 仅 aggregator 信源，无官方佐证 |
| DeepSeek V4-Flash-Vision-Exp 权重 | ❓ 未表态 | Exp 标签，是否开源未知（新增） |

---

*Generated 2026-08-23. Source: Web search results (DeepSeek 官方 changelog、llm-stats、officechai、explainx、LMMarketCap、LLM Gateway、Constellation Research、TechCrunch、FutureSearch、BenchLM、kie.ai [rumor 级]). Cross-referenced with wiki/synthesis/2026-08-21/tech-report-digest.md.*
