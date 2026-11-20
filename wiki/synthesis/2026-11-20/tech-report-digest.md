# LLM 技术报告速览 — 2026-11-20

> 覆盖 19 家目标机构最新一手 Tech Report / Technical Report / System Card / Model Card / 官方技术披露，重点关注新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling、多模态、长上下文与推理。
> 来源：公司官方新闻/文档页（DeepSeek 官网、Google DeepMind Blog、Anthropic News、OpenAI Deployment Safety Hub、NVIDIA、Apple AI 页、AWS Blog）与 arXiv/HuggingFace 仓库；窗口内 2026-11-19 项见 `synthesis/2026-11-19/tech-report-digest.md`。

## 窗口发现（2026-11-20 核验）

- **新增首发**：Google DeepMind **Gemini 4 Neon**（2026-11-18，全新一级；Artificial Analysis Intelligence Index v5.01 #3, score 61；Vals Index #2；1M 上下文；输入 $3/M tokens、缓存 $0.15/M、输出 $15/M tokens；内部安全：unjustified refusals −3.00pp vs Hydrogen）；OpenAI **GPT-6 Cyber** 系统卡（2026-11-05，阶段 1: 基于 GPT-6 Astra，Daybreak Red 审批通道）。
- **复核情况**：OpenAI sitemap 显示 GPT-6 Astra（2026-11-19T22:57Z 更新）；Anthropic 11-18 新闻为 IPO 新闻（未有新模型报告）；NVIDIA newsroom.nvidia.com 连接失败，NVIDIA 依赖 arXiv/HuggingFace/developer.nvidia.com 口径（Nemotron 3.5 Super 11-17）；Muse Spark 1.3（Meta）目录未标注日期。
- **主要趋势**：reasoning model + AI Self-Improvement（OpenAI GPT-6 Cyber 对齐导向、DeepSeek V4.1 Flash 8B/16B 非对称 MoE）、post-training via RL（NVIDIA Nemotron 3.5 Super CISPO、OpenAI GPT-6 Cyber 后训练 RL）、长上下文（Gemini 4 Neon/Hydrogen 1M、NVIDIA Nemotron 3.5 Super 1M）、多模态（Gemini 4 全系、DeepSeek V4.1 Flash 原生视觉、Muse Spark 全系）、长上下文（NVIDIA Nemotron 3.5 Super 1M、NVIDIA Kumo Tabular 表格预测）、Cybersecurity Critical 设计趋势。

## 目标机构覆盖状态（最新核验）

| 机构 | 最新核验报告（型号/日期） | 状态 |
|------|--------------------------|------|
| DeepSeek | DeepSeek V4.1-Flash-1017 (2026-10-17), 前代 DeepSeek-V4 (arXiv:2606.19348) | ✓ 已记录（新） |
| OpenAI | GPT-6 Cyber 系统卡 (2026-11-05); GPT-6 Astra (sitemap 2026-11-19) | ✓ 已记录（新） |
| Meta AI | Muse Spark 1.3（ai.meta.com/llama/ 模型目录, 未标日期） | 新 |
| Anthropic | Fable 5.2 / Mythos 5.2 (2026-11-09) | ✓ 已记录 |
| Google DeepMind | Gemini 4 Neon (2026-11-18); Gemini 4 Carbon (2026-11-10); Gemini 4 Hydrogen (2026-11-12) | 新 |
| Mistral AI | Le Chonk (2026-11-05), Mistral Large 4 (2026-10-06) | 新（Le Chonk） |
| Qwen (Alibaba) | Qwen3.8-Max (2.4T, 11-07 速览) | ✓ 已记录 |
| Yi (01.AI) | Yi-Lightning (2024.10) | 稳定 |
| Baichuan | 无可验证新报告 | — |
| Microsoft | Phi-4-reasoning-vision-15B; FrogNano-4B (11-18 速览) | ✓ 已记录 |
| Apple | AFM 3 (20B sparse, IFP) + Siri AI（apple.com/ai） | 新（复核） |
| NVIDIA | Nemotron 3.5 Super (2611.22161, 2026-11-17), Bolt E4B 4GB (2611.20771, 2026-11-16) | 新（Super） |
| xAI | Grok 4.7 (2026-09-22) | ✓ 已记录 |
| Amazon Nova | Nova 2 Lite/Sonic（2025-12-02 博客）, Nova 2（11-07 速览） | 新（Nova 2 Lite/Sonic） |
| Zhipu AI | GLM-5.3 (1M 上下文) | ✓ 已记录 |
| InternLM (Shanghai AI Lab) | 未发现新报告 | — |
| Moonshot AI (Kimi) | Kimi K3.1 Pro (2026-10-24) | ✓ 已记录 |
| StepFun (阶跃星辰) | Step 5 Preview (600B/27B, 11-07 速览) | ✓ 已记录 |
| ByteDance (豆北/Doubao/Seed) | Seed 2.0 / doubao-seed-evolving (11-07 速览) | ✓ 已记录 |
| Shanghai AI Lab | Sage S2.1 Flash (arXiv:2611.21072, 2026-11-16) | ✓ 已记录 |

## 逐家详情

### 1. DeepSeek（DeepSeek-AI）

- 中文标题：DeepSeek V4 系列与 DeepSeek V4.1 Flash（百万上下文普惠）
- 英文标题：DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence；DeepSeek V4.1 Flash
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek-V4（Pro/Flash 分支）；DeepSeek V4.1-Flash
- 发布日期：V4 预览 2026-04-26（arXiv:2606.19348）；V4.1 Flash 2026-09-10（API 名 deepseek-flash, V4.1-Flash-1017 于 2026-10-17 更新）
- 核心参数：V4-Pro 1.6T（49B 活跃）；V4-Flash 284B（13B 活跃）；1M 上下文；预训练 >32T tokens（自报）；V4.1-Flash 552B MoE（输入激活 8B / 输出激活 16B 非对称）；KV Cache 较历代缩小 437 倍
- 主要创新点：混合注意力架构 CSA+HCA+DSA 提升 1M 上下文效率；强化学习后训练；原生多模态（V4.1 Flash）；KV Cache 压缩降低 Agent 任务成本
- arXiv/链接：[DeepSeek-V4 (arXiv:2606.19348)](https://arxiv.org/abs/2606.19348)、[DeepSeek V4 预览 (官网)](https://www.deepseek.com/news/v4-preview/)、[DeepSeek V4.1 Flash (官网)](https://www.deepseek.com/news/deepseek-v4-1-flash/)、[DeepSeek-V4.1-Flash (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

### 2. OpenAI

**GPT-6 Cyber（最新, 2026-11-05）**

- 中文标题：GPT‑6 Cyber：Advancing the frontier of aligned cybersecurity agents
- 英文标题：GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents
- 发布机构：OpenAI
- 模型名称/系列：GPT‑6 Cyber（基于 GPT‑6 Astra；第一阶段 Daybreak Red 审批通道）
- 核心参数：系统卡正文未公开参数量/参数结构；Preparedness Framework 定位：Cybersecurity: Critical，Biological/Chemical: High，AI Self-Improvement below High；关键评测（vs GPT‑6 Astra）：ExploitGym 48.45%（Astra 42.43%）、ExploitGym Hardened 36.94%（Astra 29.69%）、SEC-Bench Pro 87.02%（Astra 85.38%）、SRE-Bench 92.84%（Astra 87.98%）、ExploitBench 加速度 ACE 均值 100%（Astra 无窗口内可比值）
- 主要创新点：RL 后训练（找漏洞、利用、修复）；对齐训练信号（遵循授权范围、正确报告阻碍）；ExploitGym Honeypot 保留在作用域内（无安全指令 0.07%）；新一系列护栏（阻止对关键基础设施受害者的高风险辅助）；外部评估（Irregular: CyScenarioBench 11/11 可完成，FrontierCyber 90/288 成功，Atomic 22/22）
- arXiv/链接：[GPT-6 Cyber System Card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/gpt-6-cyber/)、[PDF](https://deploymentsafety.openai.com/gpt-6-cyber/gpt-6-cyber.pdf)、[Cyber page (openai.com)](https://openai.com/index/introducing-gpt-6-cyber/)

**GPT-6 Astra（sitemap 更新 2026-11-19）**

- 中文标题：Introducing GPT-6 Astra（"GPT-6.2 Astra/Sol"，2026-11-17 速览：GPQA Diamond 97.0%、ExploitBench Internal ACE 53.5%、MLE-Bench Revised 第 96.06 百分位、NanoGPT 训练时间 −42.87%）
- 英文标题：Introducing GPT-6 Astra
- 发布机构：OpenAI
- 模型名称/系列：GPT‑6 Astra（"GPT‑6.2 Astra/Sol"）
- 发布日期：2026-11-17（系统卡）；sitemap [OpenAI /index/gpt-6-astra/ (lastmod 2026-11-19T22:57Z)](https://openai.com/index/gpt-6-astra/)
- 核心参数：公开页未披露完整参数/训练数据
- 局限：页面在窗口内 403（webfetch 与 curl 均不可获取），正文主要依 11-17/11-18 速览与 Cyber 系统卡引用。

### 3. Google DeepMind（Gemini 4）

**Gemini 4 Neon（最新, 2026-11-18）**

- 中文标题：Introducing Gemini 4 Neon
- 英文标题：Introducing Gemini 4 Neon
- 发布机构：Google DeepMind
- 模型名称/系列：Gemini 4（Argon/Carbon/Hydrogen/Neon）
- 发布日期：2026-11-18
- 核心参数：1M 上下文（Model Card: combined input-output 1M 窗口；默认同步输出 64K，最长 1M；输入含文本/图像/音频/视频）；定价：输入 $3/M tokens（缓存 $0.15/M, 95% 折扣）、输出 $15/M tokens；AA Index v5.01 #3 (score 61)、Vals Index #2；内部安全：unjustified refusals −3.00pp vs Hydrogen
- 主要创新点：frontier coding + 复杂高频工作负载 fast end-to-end；被 Gemini 4 Carbon 适配（architecture/training data 细节在 Carbon card）；MCC 评估在 Argon 上无必要的存量评估被沿用；知识截至 2026-03
- arXiv/链接：[Introducing Gemini 4 Neon (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)、[Gemini 4 Neon Model Card (PDF)](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf)、[evals methodology](https://deepmind.google/models/evals-methodology/gemini-4-neon)、[Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-neon)

**Gemini 4 Hydrogen（2026-11-12, Last updated 2026-11-16）**

- 中文标题/英文标题：Introducing Gemini 4 Hydrogen
- 发布机构：Google DeepMind
- 模型系列：Gemini 4（Hydrogen）
- 核心参数：AA Index 51（默认）/ 54（xhigh）；输入 $1.50/M tokens、输出 $7.50/M tokens；1M 上下文；everyday coding & agentic workflows
- 链接：[Introducing Gemini 4 Hydrogen (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)、[Hydrogen model card (PDF)](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf)

**Gemini 4 Carbon（2026-11-10，is now available）**

- 中文标题/英文标题：Gemini 4 Carbon is now available
- 核心参数：AutomationBench 上 more than 2X lower cost/task vs 下一款外部模型；AAA 强度
- 链接：[Gemini 4 Carbon is now available (blog.google, 2026-11-10)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)、[Gemini 4 Argon（2026-09, 见 11-18 速览）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)

### 4. Meta AI（Muse Spark）

**Muse Spark 1.3（最新, 目录未标日期）**

- 中文标题：Muse Spark 1.3：Frontier Coding, Long-Running Agents & Advanced Computer Use
- 英文标题：Muse Spark 1.3：Frontier Coding, Long-Running Agents & Advanced Computer Use
- 发布机构：Meta AI
- 模型名称/系列：Muse Spark 1.3（页面产品：MuseWonder-1.0、Muse Ember-1.0 变体）— 系列原 Llama 目录（ai.meta.com/llama/）
- 核心参数：参数量未公开（dev.meta.ai/models 目录）；Muse Code Multi-agent coding；capabilities: frontier coding, long-running agents, advanced computer use（Plans long tasks and delegates to sub-agents）
- 主要创新点："Plans long tasks and delegates to sub-agents"；"Cleaner code, fewer tokens"（Muse Spark 1.2 描述）；"The most capable US open-weight model to date"（Muse Spark Open）
- 链接：[ai.meta.com/llama/ 模型目录](https://ai.meta.com/llama/)、[Muse Spark Open (dev.meta.ai/models/muse-spark-open)](https://dev.meta.ai/models/muse-spark-open)、[Introducing Muse Spark 1.1 (blog, 2026-07-09)](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
- 局限：目录无日期；Muse Spark 1.1 为 2026-07-09（最近一次有日期的版本）；dev.meta.ai/models/muse-spark-1.3 为 404（未取得正文）。

**Muse Spark 1.2 / 1.1 / Spark Open**：1.2 "A coding-optimized model purpose-built for agentic workflows."；1.1（2026-07-09）"Built for agentic workflows, coding, computer use & multimodal perception."；Spark Open "The most capable US open-weight model to date."

### 5. Anthropic（Claude）

- 中文标题：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- 英文标题：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- 发布机构：Anthropic
- 模型系列：Claude Fable 5.2 / Claude Mythos 5.2
- 发布日期：2026-11-09
- 核心参数：公开页未披露
- 主要创新点："most capable models for daunting technical work — coding, finance, sciences"（新基准 SWE Bench Pro 等）。
- 官方链接：[Anthropic News (www.anthropic.com/news)](https://www.anthropic.com/news)
- 局限：11-18 新闻为 IPO（roadshow/S-1/股价），无新模型。

### 6. Mistral AI

- 最新报告：**Le Chonk**（2026-11-05, 权重开放 2026-10-29）— "Built for Coders, Trusted by Defenders"（agentic coding & cybersecurity；Studio/Forge/Vibe 生态）。
- 中文/英文标题：Le Chonk: Built for Coders, Trusted by Defenders
- 模型系列：Mistral Large 4（2026-10-06 发布, 2026-10-29 权重开放；1T total/49B active, 1M ctx, MLA+DSA）与 Le Chonk（2026-11-05）
- 官方链接：[Mistral News (www.mistral.ai/news/)](https://www.mistral.ai/news/)、[Le Chonk page (www.mistral.ai/news/le-chonk/)](https://www.mistral.ai/news/le-chonk/)、[Mistral Large 4 page (www.mistral.ai/news/mistral-large-4/)](https://www.mistral.ai/news/mistral-large-4/)

### 7. Qwen (Alibaba Cloud Model Studio)

- 中文/英文标题：Qwen3.8-Max（2.4T）
- 发布机构：Alibaba Cloud（Model Studio）
- 模型系列：Qwen3.8-Max；Qwen3.8-Flash-Next（qwen4_exp 预览）
- 发布日期：~2026（11-07 速览）
- 核心参数：Qwen3.8-Max 参数 2.4T
- 主要创新点：双轨架构（Max/Flash）；面向编码的 open-weight 主流产品。
- 局限：窗口未发现 Qwen 独立 Tech Report。

### 8. Yi (01.AI / 零一万物)

- 中文/英文标题：Yi-Lightning 发布
- 发布机构：01.AI
- 模型系列：Yi-Lightning（千亿参数 MoE）
- 发布日期：2024.10
- 核心参数：千亿参数 MoE（LMSYS 盲测世界第六、中国第一，2024.10）
- 主要创新点：open MoE 模型，LMSYS 盲测排名。
- 官方链接：[01.AI 零一万物 - 大模型赋能千行百业](https://www.01.ai/news/)
- 局限：无新一手报告（窗口内未发现）。

### 9. Baichuan（百川智能）

- 状态：窗口未发现新一手 Tech Report/System Card（11-07 速览“Yi 与 Baichuan 无可验证新报告”）；网站近期不可达（baichuan.io 等 DNS/404）。

### 10. Microsoft

- 中文/英文标题：Microsoft Phi-4-reasoning-vision-15B；FrogNano-4B（11-18 速览型号）
- 发布机构：Microsoft
- 模型系列：Phi-4-reasoning-vision（15B）；FrogNano-4B
- 发布日期：Phi 系列 ~2025/2026（11-07 速览口径）；FrogNano-4B（2026，11-18 速览）
- 核心参数：Phi-4-reasoning-vision 15B（vision+reasoning 合一）；FrogNano-4B（4GB 入门级）
- 主要创新点：vision+reasoning 合一；small-model frontier focus。
- 官方链接：[Microsoft AI（Blogs）](https://blogs.microsoft.com/ai/)、[news.microsoft.com/source/topics/ai/](https://news.microsoft.com/source/topics/ai/)
- 局限：无新 Phi Tech Report（news 页 11/17 为 Copilotforce/TerraNova 等产品新闻）。

### 11. Apple

- 中文标题：Apple AFM 3；Apple Intelligence / Siri AI
- 英文标题：Apple AFM 3；Apple Intelligence and Siri
- 发布机构：Apple
- 模型系列：Apple Foundation Model（AFM）3；Siri AI（Apple Intelligence）
- 发布日期：2026（apple.com/ai 页）
- 核心参数：AFM 3：20B sparse（IFP, PC C）；Siri AI：未公开参数
- 主要创新点：本地计算与隐私（"Truly helpful, truly yours... powered by Apple Intelligence"）；AFM 3 为第三代；不发布传统 Tech Report。
- 官方链接：[Apple Intelligence and Siri - Apple](https://www.apple.com/ai/)

### 12. NVIDIA（Nemotron）

- **Nemotron 3.5 Super（最新, 2026-11-17, arXiv:2611.22161）**
  - 中文/英文标题：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
  - 模型系列：Nemotron 3.5 Super（120B total / 12B active）
  - 核心参数：120B 总量/12B 活跃（含一个 VL 变体，11-18 速览）；1M 上下文；混合 MoE 架构（Mamba-Transformer hybrid，10-31 速览）
  - 主要创新点：post-training via RL — CISPO 算法，每次训练在 Tinker 上用 rank-32 LoRA 针对单一专家构建任务（software engineering、complex constraints、long-horizon tool use、professional chart understanding、enterprise document reasoning）；性能提升：SWE-bench Pro V2 86.9%→92.1%，GDP_pdf +13.8（10.4%→24.2%）等；文档 adapter（无 API 工具）+8.0
  - 链接：[What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super (arXiv:2611.22161)](https://arxiv.org/abs/2611.22161)
- **Nemotron 3.5 Bolt E4B 4GB（2026-11-16, arXiv:2611.20771）**
  - 模型系列：Nemotron 3.5 Bolt E4B 4GB；post-trained from Gemma-4-E4B-it
  - 核心参数：4GB 嵌入式/桌面部署；DFlash drafter → 2.74× per-user decode speed
  - 链接：[Nemotron 3.5 Bolt E4B 4GB (arXiv:2611.20771)](https://arxiv.org/abs/2611.20771)
- **Kumo Tabular（2026-11-17, arXiv:2611.23001）**
  - 模型系列：NVIDIA Kumo Tabular（S 27M / M 61M / L 214M）
  - 主要创新点：open tabular foundation models（classification/regression）；table encoder + in-context learning transformer
- **Nemotron-Labs-Sigma（连续扩散 LM, 2026-11-12, arXiv:2610.02665 v2）**：Phased DMD NFE 2/4/8/16

### 13. xAI（Grok）

- 中文/英文标题：Introducing Grok 4.7
- 发布机构：xAI（SpaceXSI）
- 模型系列：Grok 4.7
- 发布日期：2026-09-22
- 核心参数：500K ctx（11-07 速览）
- 官方链接：[x.ai/news](https://x.ai/news)
- 局限：无新 Grok 报告（x.ai/news 最新为 Grok Bot 1.0 等产品新闻）。

### 14. Amazon Nova（AWS）

- 中文/英文标题：Amazon Nova 2 Lite / Amazon Nova 2 Sonic
- 发布机构：Amazon（AWS）
- 模型系列：Amazon Nova 2 Lite（fast, cost-effective reasoning model, 1M ctx, extended thinking low/medium/high）；Amazon Nova 2 Sonic（speech-to-speech, 对话 AI, 音色代码切换）；Amazon Nova 2（11-07 速览：Bedrock 系列 Pro/Lite/Micro/Sonic/Canvas/Reel）
- 发布日期：Nova 2 Lite / Sonic — 2025-12-02（AWS 博客；Nova 页 "What's new" 定位）；Nova 2 — ~2026（11-07 速览）
- 核心参数：Nova 2 Lite：1M 上下文；extended thinking 低/中/高预算；web grounding + code interpreter 内置工具
- 官方链接：[Introducing Amazon Nova 2 Lite (AWS blogs, 2025-12-02)](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-lite-a-fast-cost-effective-reasoning-model/)、[Introducing Amazon Nova 2 Sonic (AWS blogs, 2025-12-02)](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-sonic-next-generation-speech-to-speech-model-for-conversational-ai/)、[Generative foundation model – Amazon Nova – AWS](https://aws.amazon.com/nova/)

### 15. Zhipu AI（GLM）

- 中文/英文标题：GLM-5.3：Frontier Coding with Emergent Cyber Capabilities
- 发布机构：Zhipu AI（Z.ai）
- 模型系列：GLM-5.3（GLM-5V-Turbo、GLM-5-Turbo）
- 发布日期：2026（Z.ai 页）
- 核心参数：1M 上下文窗口；open-source SOTA for coding
- 官方链接：[Z.ai - Inspiring AGIT](https://www.zhipuai.cn/en)

### 16. InternLM（Shanghai AI Lab）

- 状态：`all:InternLM` 论文检索无新结果（2026-09 起）；本窗口未发现新技术报告。
- 补充：Shanghai AI Lab — Sage S2.1 Flash（arXiv:2611.21072，2026-11-16；320B MoE 科学多模态、Sage SciPerception >10 类科学输入、可验证环境 agentic 后训练、MLE-bench Lite 90.3 第一、MIT 权重）。

### 17. Moonshot AI（Kimi）

- 中文/英文标题：Kimi K3.1 Pro
- 发布机构：Moonshot AI
- 模型系列：Kimi K3.1 Pro
- 发布日期：2026-10-24
- 核心参数：3-trillion-parameter-class model，1M context window；built for long-horizon coding、3D creation、financial research、complex agentic tasks
- 官方链接：[Moonshot AI (www.moonshot.ai/blog/)](https://www.moonshot.ai/blog/)

### 18. StepFun（阶跃星辰）

- 中文/英文标题：Step 5 Preview
- 发布机构：StepFun
- 模型系列：Step 5 Preview
- 发布日期：~2026（11-07 速览）
- 核心参数：600B/27B（total/active），92 层，Sparse GQA
- 官方链接：[阶跃星辰](https://www.stepfun.com/)

### 19. ByteDance（豆北/Doubao/Seed）

- 中文/英文标题：ByteDance Seed 2.0；doubao-seed-evolving
- 发布机构：ByteDance（豆北/Doubao/Seed）
- 模型系列：Seed 2.0；doubao-seed-evolving
- 发布日期：~2026（11-07 速览）
- 核心参数：未给（速览口径）
- 官方链接：[豆北 - 字节跳动旗下 AI 智能助手](https://www.doubao.com/)、[ByteDance Newsroom (www.bytedance.com/en/newsroom/)](https://www.bytedance.com/en/newsroom/)

## 局限说明

- 系统卡/模型卡/博客/模型页披露层级不同；参数与 benchmark 多为自报、口径不一不可横比；GPT-6 Astra、Gemini 4 Neon 页面正文以系统卡/模型卡为准，Muse Spark 1.3 目录无日期。
- OpenAI 部分正文页面（/index/gpt-6-astra/、/index/introducing-gpt-6-2-astra-sol/、/index/introducing-gpt-6-1-sol/、/index/introducing-aardvark/）在窗口内 403（webfetch 与 curl 均失败），sitemap 确认页面存在（lastmod 2026-11-18–20）；内容以系统卡引用与 11-17/11-18 速览为准。
- NVIDIA newsroom.nvidia.com 连接失败（HTTP 000），NVIDIA 依赖 arXiv/HuggingFace/developer.nvidia.com 口径（新产品口径遵循 digest 口径，NVIDIA 企业市场页、MLPerf 等非 LLM 报告不在本次范围）。
- Apple、NVIDIA 以官方“Next What's New”/新闻页为准，部分日期为窗口内速览口径。

## 方法与来源

webfetch/HTTPS 抓取官方页面（DeepSeek 官网、Google DeepMind Blog、Anthropic News、OpenAI Deployment Safety Hub、NVIDIA、Apple AI 页、AWS Blogs、ByteDance Newsroom、Microsoft AI 新闻、x.ai News、Moonshot AI Blog、StepFun 站点、Doubao 站点、Meta AI 站点）；arXiv 导出 API（`export.arxiv.org/api/query`）；HuggingFace 模型卡页（DeepSeek-V4.1-Flash）；Model Card PDF（Gemini 4 Neon，经 pdftotext 提取）；以及既有 wiki 速览（synthesis/2026-11-07…2026-11-19）。所有数据均源自本窗口抓取，无编造。Preference file active: `EXTEND.md`（repo root，bm25 mode `auto_prompt`; BM25 未触发）。
