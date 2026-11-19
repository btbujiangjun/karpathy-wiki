# LLM 技术报告速览 — 2026-11-19

> 覆盖 19 家目标机构最新一手 Tech Report / Technical Report / System Card / Model Card / 官方技术披露，重点关注新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling、多模态、长上下文与推理。
> 来源：公司官方新闻/文档页（Anthropic News、DeepMind News、Meta AI Blog、Mistral News、xAI News、Apple ai、AWS Nova、Z.ai、01.ai News、Moonshot Blog、StepFun 站点、Doubao 站点）与 arXiv/HuggingFace 仓库；窗口内 2026-11-18 项见 `synthesis/2026-11-18/tech-report-digest.md`。

## 窗口发现（2026-11-19 核验）

- **未发现语义级新旗舰**：比较 11-18，OpenAI GPT-6.2 System Card（11-17）、NVIDIA AVF 权重（11-16/17）、Apple FastFrames（11-17）、Anthropic Fable 5.2/Mythos 5.2（11-09）、NVIDIA Nemotron 权重更新均无窗口内首发事实。
- **最新确认披露**：Anthropic Fable 5.2/Mythos 5.2（11-09）、Apple Siri AI（2026）、Meta Muse Spark 1.1（2026-07-09）、Kimi K3.1 Pro（2026-10-24）、NVIDIA Nemotron 3.5 Super/Bolt/Kumo Tabular（11-16/17）等。
- **主要趋势**：reasoning model + AI Self-Improvement（Astra）、post-training via RL（NVIDIA Nemotron 3.5 Super）、长上下文（1M）、MoE 混合架构（DeepSeek-V4 CSA+HCA、NVIDIA Nemotron 3.5 Super hybrid MoE）、多模态（Sage S2.1 Flash、Apple Siri AI/AFM 3、NVIDIA AVF）。

## 目标机构覆盖状态（最新核验）

| 机构 | 最新核验报告（型号/日期） | 状态 |
|------|--------------------------|------|
| DeepSeek | DeepSeek-V4 (2606.19348, 2026-04-26) | ✓ 已记录 11-07 |
| OpenAI | GPT-6.2 System Card (Astra/Sol, 2026-11-17) | ✓ 已记录 11-18 |
| Meta AI | Muse Spark 1.1 (2026-07-09) | 新 |
| Anthropic | Fable 5.2 / Mythos 5.2 (2026-11-09) | ✓ 已记录 11-18 |
| Google DeepMind | Gemini 4 Argon/Carbon/Hydrogen (2026) | ✓ 已记录 11-18 |
| Mistral AI | Mistral Large 4 (2026-10-15), Le Chonk (2026-11-05), Voxtral 3, Timestral | ✓ 已记录 11-07/10-31 |
| Qwen (Alibaba) | Qwen3.8-Max (2.4T) | ✓ 已记录 11-07 |
| Yi (01.AI) | Yi-Lightning (2024.10) | 稳定 |
| Baichuan | 无可验证新报告 | — |
| Microsoft | Phi-4-reasoning-vision-15B | ✓ 已记录 11-07 |
| Apple | AFM 3 (20B sparse, IFP) + Siri AI | 新 |
| NVIDIA | Nemotron 3.5 Super (2611.22161, 2026-11-17) | 新 |
| xAI | Grok 4.7 (2026-09-22) | ✓ 已记录 11-07 |
| Amazon Nova | Nova 2 | ✓ 已记录 11-07 |
| Zhipu AI | GLM-5.3 | ✓ 已记录 11-07 |
| InternLM (Shanghai AI Lab) | 未发现新报告 | — |
| Moonshot AI (Kimi) | Kimi K3.1 Pro (2026-10-24) | 新 |
| StepFun (阶跃星辰) | Step 5 Preview (600B/27B, 92 层, Sparse GQA) | ✓ 已记录 11-07 |
| ByteDance (豆北/Doubao/Seed) | Seed 2.0 / doubao-seed-evolving / Recycler | ✓ 已记录 11-07 |
| Shanghai AI Lab | Sage S2.1 Flash (arXiv:2611.21072, 2026-11-16) | ✓ 已记录 11-18 |

## 逐家详情

### 1. DeepSeek（DeepSeek-AI）

- 中文标题：DeepSeek-V4：Towards Highly Efficient Million-Token Context Intelligence
- 英文标题：DeepSeek-V4
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek-V4（Pro/Flash 分支）
- 发布日期：2026-04-26（arXiv:2606.19348）
- 核心参数：DeepSeek-V4-Pro 1.6T（49B 活跃）；DeepSeek-V4-Flash 284B（13B 活跃）；两者 1M 上下文；预训练 >32T tokens（自报）；V4.1-Flash（552B，8B/16B 非对称编解码，窗口内已见）
- 主要创新点：混合注意力架构（CSA + HCA）提升 1M 上下文效率；Manifold-Constrained Hyper-Connections（mHC）改进残差；Muon 优化器；DeepSeek-V4-Pro-Max（最大推理模式版）；预训练后统一 post-training 管线。
- arXiv/链接：[DeepSeek-V4 (arXiv:2606.19348)](https://arxiv.org/abs/2606.19348)
- 局限：参数/数据/训练细节为自报，未逐项核对；最新变体 V4.1-Flash 见 digest 11-07/11-18。

### 2. OpenAI

- 中文标题：GPT-6.2 系统卡（Astra/Sol）
- 英文标题：GPT-6.2 System Card (Astra/Sol)
- 发布机构：OpenAI
- 模型名称/系列：GPT-6.2 Astra / GPT-6.2 Sol
- 发布日期：2026-11-17
- 核心参数：公开页未披露完整参数/训练数据；已知结果（11-18 速览）：GPQA Diamond 97.0%、ExploitBench Internal ACE 53.5%、MLE-Bench Revised 第 96.06 百分位、NanoGPT 训练时间 −42.87%。
- 主要创新点：Astra 首个对外部署达 AI Self-Improvement High；Control Room 集中监控/急停；评测觉察 <3% turns；网络安全 Critical + 生物化学 High 双用途（需合规）；CoT 规避与蒸馏提取 <1%。
- 官方链接：[openai.com/gpt-6-2-astra-sol](https://openai.com/gpt-6-2-astra-sol)、[openai.com/news](https://openai.com/news)
- 局限：窗口内 11-18 已核验，无新进展；系统卡与配置页披露层级不同。

### 3. Meta AI

- 中文标题：Introducing Muse Spark 1.1
- 英文标题：Introducing Muse Spark 1.1
- 发布机构：Meta AI
- 模型名称/系列：Muse Spark 1.1（"Scaling Towards Personal Superintelligence"）
- 发布日期：2026-07-09
- 核心参数：公开页未给参数；11-07 速览可见 Muse Spark Open（816B-A42B MoE）
- 主要创新点：个人超级智能方向的 agentic Muse；与 2026 附带 Muse Image/Video 口径不一（公开披露层级分散）。
- 官方链接：[ai.meta.com/blog/](https://ai.meta.com/blog/)

### 4. Anthropic（Claude）

- 中文标题：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- 英文标题：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- 发布机构：Anthropic
- 模型名称/系列：Claude Fable 5.2 / Claude Mythos 5.2
- 发布日期：2026-11-09
- 核心参数：未在公开页面给出（系统卡/模型卡口径不一，未全部核实）
- 主要创新点：Fable 5.2 / Mythos 5.2 被称为 coding、finance、sciences 上的新基准（"most capable models for daunting technical work"）。
- 官方链接：[Anthropic News](https://www.anthropic.com/news)

### 5. Google DeepMind

- 中文标题：Gemini 4 Argon / Carbon / Hydrogen
- 英文标题：Gemini 4 Argon/Carbon/Hydrogen
- 发布机构：Google DeepMind
- 模型名称/系列：Gemini 4（Argon、Carbon、Hydrogen）
- 发布日期：2026（DeepMind 模型页可见）
- 核心参数：Gemini 4 Argon：1M 上下文，Vals 68.9%（11-07/11-18 速览）；10-31 速览可见 Gemini 4 Carbon 仍无 model card。
- 主要创新点：分子命名变体（Argon/Carbon/Hydrogen）+ 安全报告 CCL；多模态 Gemini 生态（Gemini Omni、Audio、Robotics）。
- 官方链接：[deepmind.google/blog/](https://deepmind.google/blog/)

### 6. Mistral AI

- 中文标题：Mistral Large 4 / Le Chonk
- 英文标题：Introducing Mistral Large 4；Le Chonk： Built for Coders, Trusted by Defenders
- 发布机构：Mistral AI
- 模型名称/系列：Mistral Large 4（2026-10-15 发布，10-29 权重开放）；Le Chonk（2026-11-05 权重开放）
- 发布日期：Mistral Large 4 — 2026-10-15；Le Chonk — 2026-11-05
- 核心参数：Mistral Large 4：1T total/49B active，1M ctx，MLA+DSA（128 experts top-4 + shared），FP8/NVFP4（10-31 速览）。
- 主要创新点：open-weight；面向 agentic coding 与 cybersecurity；Studio/Forge/Vibe 生态。
- 官方链接：[Mistral News](https://www.mistral.ai/news/)

### 7. Qwen (Alibaba)

- 中文标题：Qwen3.8-Max（2.4T）
- 英文标题：Qwen3.8-Max（2.4T）
- 发布机构：Alibaba Cloud（Alibaba Cloud Model Studio）
- 模型名称/系列：Qwen3.8-Max（2.4T）；Qwen3.8-Flash-Next（qwen4_exp 预览）
- 发布日期：~2026（11-07 速览）
- 核心参数：Qwen3.8-Max 参数 2.4T（11-07 速览）
- 主要创新点：双轨架构（Max/Flash）；面向编码的 open-weight 主流产品。
- 局限：窗口内未发现 Qwen 独立 Tech Report（参见 11-07 速览）。

### 8. Yi (01.AI)

- 中文标题：Yi-Lightning 发布
- 英文标题：Yi-Lightning
- 发布机构：01.AI（零一万物）
- 模型名称/系列：Yi-Lightning（千亿参数 MoE）
- 发布日期：2024.10（01.ai/news 页）
- 核心参数：千亿参数 MoE（LMSYS 盲测世界第六、中国第一，2024.10）
- 主要创新点：open MoE 模型，LMSYS 盲测排名
- 官方链接：[01.AI 零一万物 - 大模型赋能千行百业](https://www.01.ai/news/)

### 9. Baichuan

- 状态：本窗口未发现新一手 Tech Report/System Card（11-07 速览“Yi 与 Baichuan 无可验证新报告”；此后窗口内无进展）。
- 局限：网站近期不可达（www.baichuan.io、baichuan-inc.com 均 404/DNS 失败）。

### 10. Microsoft

- 中文标题：Microsoft Phi-4-reasoning-vision-15B
- 英文标题：Phi-4-reasoning-vision-15B
- 发布机构：Microsoft
- 模型名称/系列：Phi-4-reasoning-vision（15B）
- 发布日期：~2025/2026（11-07 速览“Microsoft Phi-4-reasoning-vision-15B”口径）
- 核心参数：15B 参数（视觉推理 Phi）
- 主要创新点：vision+reasoning 合一；small-model frontier focus。
- 官方链接：[Microsoft AI（Blogs）](https://blogs.microsoft.com/ai/)

### 11. Apple

- 中文标题：Apple AFM 3；Apple Intelligence / Siri AI
- 英文标题：Apple AFM 3；Apple Intelligence and Siri
- 发布机构：Apple
- 模型名称/系列：Apple Foundation Model（AFM）3；Siri AI（Apple Intelligence）
- 发布日期：2026（11-07 速览 AFM 3；apple.com/ai 页）
- 核心参数：AFM 3：20B sparse（IFP、PC C，11-07 速览）；Siri AI：未公开参数
- 主要创新点：本地计算与隐私（"Truly helpful, truly yours... powered by Apple Intelligence"）；AFM 3 = Apple Foundation Model 第三代；不发布传统 Tech Report（系统卡在其他机构集中出现）。
- 官方链接：[Apple Intelligence and Siri - Apple](https://www.apple.com/ai/)

### 12. NVIDIA — Nemotron 3.5 Super

- 中文标题：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
- 英文标题：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
- 发布机构：NVIDIA
- 模型名称/系列：Nemotron 3.5 Super（120B total / 12B active）
- 发布日期：2026-11-17
- 核心参数：120B 总量/12B 活跃（含一个 VL 变体，11-18 速览）；1M 上下文（Digest 10-31）；混合 MoE 架构（Mamba-Transformer hybrid，10-31）。
- 主要创新点：post-training via RL — CISPO 算法，每次训练在 Tinker 上用 rank-32 LoRA 针对单一专家构建任务（software engineering、complex constraints、long-horizon tool use、professional chart understanding、enterprise document reasoning）；性能提升：SWE-bench Pro V2 86.9%→92.1%，Terminal-Bench 2.1 63.9%→70.3%，MultiChallenge 58.3%→66.6%，AutomationBench 14.8%→27.5%，Chartography 39.4%→50.6%，GDP_pdf +13.8（10.4%→24.2%），IFBench +4.5；文档 adapter（无 API 工具）+8.0。
- 官方链接：[What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super (arXiv:2611.22161)](https://arxiv.org/abs/2611.22161)

### 13. NVIDIA — Nemotron 3.5 Bolt E4B 4GB

- 中文标题：Nemotron 3.5 Bolt E4B 4GB：An Open and Efficient Small Language Model for Fast Conversational Agents
- 英文标题：Nemotron 3.5 Bolt E4B 4GB（same）
- 发布机构：NVIDIA
- 模型名称/系列：Nemotron 3.5 Bolt E4B 4GB
- 发布日期：2026-11-16
- 核心参数：post-trained from Gemma-4-E4B-it；21 个基准上平均准确率最高且输出最少（reasoning 与非 reasoning 模式）；DFlash drafter → 2.74× per-user decode speed；RTX/Jetson/DGX Spark 嵌入式部署。
- 官方链接：[Nemotron 3.5 Bolt E4B 4GB (arXiv:2611.20771)](https://arxiv.org/abs/2611.20771)

### 14. NVIDIA — Kumo Tabular

- 中文标题：NVIDIA Kumo Tabular：Pushing the Accuracy-Efficiency Frontier for Tabular Prediction
- 英文标题：NVIDIA Kumo Tabular
- 发布机构：NVIDIA Research
- 模型名称/系列：Kumo Tabular（S 27M / M 61M / L 214M）
- 发布日期：2026-11-17
- 核心参数：open tabular foundation models（classification/regression）；table encoder + in-context learning transformer；可缩至 150M cells；rank first on 8 benchmarks: TabArena、TALENT、BeyondArena、ScoringBench、STRABLE、MulTaBench、RamanBench、TabBench-Bio。
- 官方链接：[NVIDIA Kumo Tabular (arXiv:2611.23001)](https://arxiv.org/abs/2611.23001)

### 15. xAI（Grok）

- 中文标题：Introducing Grok 4.7
- 英文标题：Grok 4.7
- 发布机构：xAI（SpaceXSI）
- 模型名称/系列：Grok 4.7
- 发布日期：2026-09-22
- 核心参数：公开页未给参数；11-07 速览可见 Grok 4.7（500K ctx）。
- 官方链接：[x.ai/news](https://x.ai/news)

### 16. Amazon（Nova）

- 中文标题：Amazon Nova 2
- 英文标题：Amazon Nova 2
- 发布机构：Amazon（AWS）
- 模型名称/系列：Amazon Nova 2（Bedrock 系列：Nova Pro/Lite/Micro/Sonic/Canvas/Reel）
- 发布日期：~2026（11-07 速览）
- 核心参数：公开页未给；AWS Nova 页列有 Nova 系列全家。
- 官方链接：[Generative foundation model – Amazon Nova – AWS](https://aws.amazon.com/nova/)

### 17. Zhipu AI（GLM）

- 中文标题：GLM-5.3：Frontier Coding with Emergent Cyber Capabilities
- 英文标题：GLM-5.3：Frontier Coding with Emergent Cyber Capabilities
- 发布机构：Zhipu AI（Z.ai）
- 模型名称/系列：GLM-5.3（GLM-5V-Turbo、GLM-5-Turbo）
- 发布日期：2026（Z.ai 页）
- 核心参数：1M 上下文窗口；open-source SOTA for coding。
- 官方链接：[Z.ai - Inspiring AGIT](https://www.zhipuai.cn/en)

### 18. InternLM（Shanghai AI Lab）

- 状态：`all:InternLM` 论文检索无结果（2026-09 起）；本窗口未发现新技术报告。
- 补充：Shanghai AI Lab — Sage S2.1 Flash（arXiv:2611.21072，2026-11-16；320B MoE 科学多模态、Sage SciPerception >10 类科学输入、可验证环境 agentic 后训练、MLE-bench Lite 90.3 第一、MIT 权重；标题/摘要型号不一已标注）。

### 19. Moonshot AI（Kimi）

- 中文标题：Kimi K3.1 Pro
- 英文标题：Kimi K3.1 Pro
- 发布机构：Moonshot AI
- 模型名称/系列：Kimi K3.1 Pro
- 发布日期：2026-10-24
- 核心参数：3-trillion-parameter-class model，1M context window；built for long-horizon coding、3D creation、financial research、complex agentic tasks。
- 官方链接：[Moonshot AI](https://www.moonshot.ai/blog/)

### 20. StepFun（阶跃星辰）

- 中文标题：Step 5 Preview
- 英文标题：Step 5 Preview
- 发布机构：StepFun
- 模型名称/系列：Step 5 Preview
- 发布日期：~2026（11-07 速览）
- 核心参数：600B/27B（total/active），92 层，Sparse GQA
- 官方链接：[阶跃星辰](https://www.stepfun.com/)

### 21. ByteDance（豆北/Doubao/Seed）

- 中文标题：ByteDance Seed 2.0 / doubao-seed-evolving / Recycler（11-07 速览）
- 英文标题：ByteDance Seed 2.0；doubao-seed-evolving；Recycler
- 发布机构：ByteDance（豆北/Doubao/Seed）
- 模型名称/系列：Seed 2.0；doubao-seed-evolving
- 发布日期：~2026（11-07 速览）
- 核心参数：未给（速览口径）
- 说明：Doubao 产品页为简化版（豆北 - 字节跳动旗下 AI 智能助手），未发现新一手 Tech Report。
- 官方链接：[豆北 - 字节跳动旗下 AI 智能助手](https://www.doubao.com/)

## 局限说明

- 系统卡/模型卡/博客/模型页披露层级不同；参数与 benchmark 多为自报、口径不一不可横比；GPT-6.2 Astra、Gemini 4 Carbon、Apple AFM 3、Gemini 4 Argon Vals 为 11-07/11-18 速览口径，未完全重新核实。
- `websearch` 工具窗口内不可用；数据来源为 webfetch/HTTPS 抓取的官方页面（或其变体 URL）+ arXiv/HuggingFace API + 既有 wiki 速览（synthesis/2026-11-07/2026-11-10/2026-11-18/2026-11-18）。
- Apple 未发现独立 Tech Report；Apple AFM 3 与 Siri AI 为 Apple 官方 AI 披露。
- Baichuan、InternLM、Yi 及 11-07 已确认的最新条目在此窗口未更新；除非有新首发事实，维持既有核验。

方法与来源：基于公司官方新闻/文档页（如 Annotated above）+ arXiv 导出 API（`export.arxiv.org/api/query`）+ 各公司站点/品牌页快照；除已标注外，所有数据均源自本窗口抓取，无编造。
