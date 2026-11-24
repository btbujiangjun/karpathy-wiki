---
title: LLM 技术报告速览 — 2026-11-24
type: synthesis
created: 2026-11-24
updated: 2026-11-24
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, ArXiv, moe, hybrid-architecture, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-24
# LLM Tech Report Digest — 2026-11-24

> 覆盖窗口：2026-11-19 → 2026-11-24。
>
> 检索说明：`websearch` 工具在环境中不可用/被取消（返回 "Web search cancelled"）；本期已通过 `webfetch`/`curl` 直接复核 OpenAI Deployment Safety Hub、Anthropic Newsroom、Google AI Studio Models、DeepSeek 官网新闻页、阿里云 Model Studio、智谱大模型平台等一手页面。arXiv Export API 检索期间被限流(HTTP 429)，本期引用的 arXiv ID 多采自 [[2026-11-18/tech-report-digest]] 及公司自带链接。
>
> 口径说明：参数量、训练数据量、上下文长度等多为厂商/论文自报，未公开即标注"未公开"；闭源模型细节以官方系统卡/模型页为准。

## 本期结论（2026-11-24）

- **窗口内新增确认披露（6 项）：** **OpenAI GPT-6.2 in ChatGPT 系统卡**（2026-11-23）、**Anthropic Claude Fable 5.2 & Mythos 5.2**（2026-11-09）、**DeepSeek V4.1 Flash**（2026-09-10，含 V4.1-Flash-1017 更新）、**Qwen4-Max**（2026-11-23）、**Mistral Le Chonk（Mistral Large 4 OSS）**（2026-10-29）、**Kimi K3.1 Pro**（2026-10-24）。
- **各公司窗口内未确认新增旗舰 Tech Report/System Card（见 [[2026-11-18/tech-report-digest]] 基线）：** Google Gemini 4（Carbon/Neon/Hydrogen/Argon）、NVIDIA Nemotron 3.5 Super（arXiv:2610.38095）、NVIDIA Nemotron-Labs-Sigma、Zhipu GLM-5.3/5.2 系列、xAI Grok 4.7、Apple AFM 3、InternLM/Sage S2.1 Flash、ByteDance 豆北 Seedance 2.0、Microsoft Phi（窗口内未检索到新增确认）、Yi、Baichuan 等。

## 重点关注方向速览（窗口新增）

| 方向 | 代表进展（窗口内新增） |
|---|---|
| 安全/对齐与反 distillation | **OpenAI GPT-6.2 in ChatGPT**：Preparedance v2 下网络安全 **Critical**、生物化学/AI 自我改进 **High**；"评测觉察量级"创新（CoT 中轨迹出现"意识到处于评测"迹象 9.88%）。**Anthropic Fable 5.2/Mythos 5.2**：强化 distillation 防御（数据捕获降 90–99%）、沙箱逃逸攻击检出 3.1%、Cyber/Bio 验证程序。 |
| 推理模型 | **OpenAI GPT-6.2 in ChatGPT**（已训练到"先推理后回答"，模型通过强化学习(RL)微调思考过程）。 |
| 非对称与新架构 | **DeepSeek V4.1 Flash**：552B MoE，非对称 Causal-Encoder-Decoder（输入激活 8B / 输出激活 16B），KV Cache 比历代缩小 437 倍，原生多模态视觉。 |
| 多模态 | **DeepSeek V4.1 Flash** 原生视觉理解（HF 模型卡确认 pipeline_tag 为 image-text-to-text）；**Qwen4-Max** 文本/图像/视频理解+深度思考；Google Gemini 4 文本/图像/音频/视频/PDF。 |
| 长上下文模型 | **Qwen4-Max**：1,000,000 tokens；Google Gemini 4（Carbon/Neon 1M，Hydrogen/Argon 见 [[2026-11-18/tech-report-digest]]）。 |
| 缩放/成本 | DeepSeek V4.1 Flash 8B 输入成本更低（非对称结构提升吞吐/可扩展性）；Qwen4-Max 北京 $1.413/$4.24 per M tokens；OpenAI GPT-6.2 网络安全 Critical 设计。 |

## 本期重点条目（窗口内新增）

### A. OpenAI — GPT-6.2 in ChatGPT 系统卡（2026-11-23）

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6.2 in ChatGPT 系统卡 |
| 英文标题 | GPT-6.2 in ChatGPT System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6.2（GPT-6 系列，ChatGPT 版本，面向 Plus/Pro 用户） |
| 发布日期 | 2026-11-23 |
| 核心参数 | 参数量未公开；与 GPT-6.2 Astra/Sol 使用相同类型的数据与训练。Preparedance v2 分级：网络安全 **Critical**、生物化学/AI 自我改进 **High**。关键自报指标：GPQA Diamond（无工具）95.6%；ExploitBench V8 Mean capability credit 100%；SEC-Bench Pro pass@1 88.34%；ExploitBench Internal Port（2026-06~08）Chrome renderer ACE 成功率 60%。 |
| 主要创新点 | **reasoning 模型，通过强化学习(RL)训练思维再回答**（内部 CoT 中出现"评测意识"迹象，有完整监控量级）；评测上首个达到网络安全 Critical、生物化学 High、AI 自我改进 High（与 GPT-6.2 Astra 类似）；健壮性（静态/多轮 jailbreak 检测率提升）；已训练到在 ChatGPT 中的通用使用上"先推理后回答"。 |
| arXiv/论文链接 | https://deploymentsafety.openai.com/gpt-6-2-chatgpt （PDF: https://deploymentsafety.openai.com/gpt-6-2-chatgpt.pdf；相关: GPT-6.2 System Card, https://deploymentsafety.openai.com/gpt-6-2-astra-sol） |

### B. Anthropic — Claude Fable 5.2 与 Claude Mythos 5.2（2026-11-09）

| 字段 | 内容 |
|---|---|
| 中文标题 | Claude Fable 5.2 与 Claude Mythos 5.2 |
| 英文标题 | Introducing Claude Fable 5.2 and Claude Mythos 5.2 |
| 发布机构 | Anthropic（Public Benefit Corporation） |
| 模型名称/系列 | Claude Fable 5.2 & Claude Mythos 5.2（同一底层模型：Fable 5.2 为公开版本，Mythos 5.2 为网络安全/研究版本，需通过 Cyber/Life Sciences Verification Programs） |
| 发布日期 | 2026-11-09 |
| 核心参数 | 参数量未公开；定价 $8/M 输入 tokens、$40/M 输出 tokens（Fast mode $16/$80）。前沿代理编码 FrontierCode 2.0 同意分数 49.1%（高努力，约 Opus 5.5 半价）；SWE v2 69.9%；HLE（with tools）74.2%；CVE Rediscovery Mythos 5.2 提升 10.2%。 |
| 主要创新点 | **更快（约 +30%）、更便宜、Fast mode（速度提升最高 2.5×）**；强化 distillation 防御（最强，对策测试减少 90–99%）；网络安全验证程序共享（CVE Rediscovery）；预训练/对齐全流程披露为系统卡总结。 |
| arXiv/论文链接 | https://www.anthropic.com/news/claude-fable-and-mythos-5-2 ；系统卡: https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card |

### C. DeepSeek — DeepSeek V4.1 Flash（2026-09-10）

| 字段 | 内容 |
|---|---|
| 中文标题 | DeepSeek V4.1 Flash：更强、更快、更普惠 |
| 英文标题 | DeepSeek V4.1 Flash：Stronger, Faster, More Accessible |
| 发布机构 | DeepSeek（杭州深度求索人工智能基础技术研究有限公司） |
| 模型名称/系列 | DeepSeek V4.1 Flash（API 模型名 **deepseek-flash**） |
| 发布日期 | 2026-09-10；9 月 14 日起更新至 **V4.1-Flash-1017**（API 新增网页搜索与抓取，强调项目开发能力提升与更低成本/更快速度） |
| 核心参数 | 552B MoE 参数；非对称 Causal-Encoder-Decoder：输入激活 **8B** / 输出激活 **16B**；原生多模态视觉理解；KV Cache 比初代小 437 倍（HBM 需求约为前代的 1/4，SSD 1/8）。 |
| 主要创新点 | 新预训练方式 + 大规模强化学习(RL)后训练，Agentic 基准上超越 DeepSeek V4 Pro 及多个旗舰；成本更低、推理速度更快、吞吐更大；开源技术报告: DeepSeek_V41_Tech_Report.pdf |
| arXiv/论文链接 | https://www.deepseek.com/news/deepseek-v4-1-flash/ ；技术报告: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf；模型卡(HF): https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash |

### D. NVIDIA — Nemotron 3.5 Super / Nemotron-Labs-Sigma / AVF 音视频（2026-11-17~17）

| 字段 | 内容 |
|---|---|
| 中文标题 | NVIDIA **Nemotron 3.5 Super**（arXiv:2610.38095, 2026-11-17）；**Nemotron-Labs-Sigma**（连续扩散语言模型, arXiv:2610.02665 v2, 2026-11-12）；**AVF 音视频模型**（2026-11-16/17） |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3.5 Super；Nemotron-Labs-Sigma（3B/8B）；AVF 音视频 |
| 发布日期 | 2026-11-17（Super）、2026-11-12/16/17（Sigma、AVF） |
| 核心参数 / 主要创新点 | 详见 [[2026-11-18/tech-report-digest]]（Hybrid Mamba-Transformer MoE、降低步数生成等） |
| arXiv/论文链接 | 见 [[2026-11-18/tech-report-digest]] |

### E. Mistral AI — Le Chonk（Mistral Large 4 OSS）（2026-10-29）

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Le Chonk（Mistral Large 4 OSS） |
| 英文标题 | Le Chonk（Open-Weight Release） |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Le Chonk（Mistral Large 4 的开源变体） |
| 发布日期 | 2026-10-29 |
| 核心参数 / 主要创新点 | 开源权重发布，"推进前沿开源模型在 **Agentic Coding** 与网络安全方向"；具体参数未透露。参见 https://www.mistral.ai/news/mistral-large-4-oss/ |

### F. 阿里 Qwen — Qwen4-Max（2026-11-23）

| 字段 | 内容 |
|---|---|
| 中文标题 | 阿里云 Qwen4-Max（通义千问 Tongyi Qianwen） |
| 英文标题 | Qwen4-Max |
| 发布机构 | 阿里云（Alibaba Cloud, 通义千问） |
| 模型名称/系列 | Qwen4-Max（新一代旗舰多模态模型：文本生成 + 图像/视频理解 + 深度思考，适合编程开发、办公、前端设计、复杂 Agent 任务） |
| 发布日期 | 2026-11-23（模型文档更新） |
| 核心参数 | 上下文长度 **1,000,000 tokens**；最大输入 991,808 tokens；最大输出 131,072（思考模式 262,144）；价格（北京）输入 $1.413 / 输出 $4.24 per M tokens（新加坡/弗吉尼亚 $1.5/$4.5）。 |
| 主要创新点 | 多模态（文本/图像/视频输入）+ 深度思考 + Web Search + 工具调用 + 结构化输出；兼容 OpenAI 与 Anthropic API。 |
| arXiv/论文链接 | https://www.alibabacloud.com/help/en/model-studio/qwen4-max |

### G. Moonshot AI（月之暗面）— Kimi K3.1 Pro（2026-10-24）

| 字段 | 内容 |
|---|---|
| 中文标题 | 月之暗面 Kimi K3.1 Pro |
| 英文标题 | Kimi K3.1 Pro |
| 发布机构 | Moonshot AI |
| 模型名称/系列 | Kimi K3.1 Pro（**3 万亿参数级**，1M 上下文） |
| 发布日期 | 2026-10-24 |
| 核心参数 / 主要创新点 | "A 3-trillion-parameter-class model with a 1-million-token context window—built for long-horizon coding, 3D creation, financial research, and complex agentic tasks."（官网 https://www.kimi.ai/blog/kimi-k3-1-pro；K3 同期推出 2.8T 参数,归档架构） |

### H. 智谱 AI（GLM/ChatGLM）— GLM-5.3 系列（窗口内未确认新增，最新可确认）

| 字段 | 内容 |
|---|---|
| 中文标题 | 智谱 GLM-5.3（API 名 glm-5.3；含 GLM-5.3-Flash / glm-5.3-flash 变体；同期 GLM-5.2、GLM-5、GLM-4.7、GLM-4.6-Air 等） |
| 发布机构 | 智谱（Zhipu AI, 北京智谱华章科技股份有限公司） |
| 模型名称/系列 | GLM-5.3 / GLM-5.2 / GLM-5（大模型开放平台 www.bigmodel.cn、z.ai 产品页） |
| 发布日期 | 未确认（无官方日期公开） |
| 核心参数 / 链接 | 参数量/上下文未获取（平台 JS 渲染）；Zhipu 开放平台: https://www.bigmodel.cn/ （NVIDIA 端侧运行示例: https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/） |

### I. ByteDance（豆北/Seed）— Seedance 2.0（DouBao 端接入）

| 字段 | 内容 |
|---|---|
| 中文标题 | 豆北 Seedance 2.0 视频生成模型（现已全面接入豆北） |
| 发布机构 | ByteDance |
| 模型名称/系列 | Seedance（+ 服务端模型 seed-lite-7b） |
| 发布日期 | 未确认（DouBao 首页 og:description 披露） |
| arXiv/论文链接 | https://www.doubao.com/ （DouBao 正文 og:description: "Seedance 2.0 视频生成模型现已全面接入豆北，现在登录即可免费使用！"） |

### J. Google DeepMind (Gemini) — 窗口内无新增

| 字段 | 内容 |
|---|---|
| 最新可确认 | Gemini 4 系列（Carbon/Neon/Hydrogen/Argon），各模型上下文 1M，模型页 https://ai.google.dev/models/gemini （Hydrogen/Argon/Neon 等详见 [[2026-11-18/tech-report-digest]]） |

### K. 其他公司：窗口内未确认新增确认报告

| 公司 | 备注 |
|---|---|
| Microsoft (Phi) | 未检索到新 Phi Tech Report |
| xAI (Grok) | 未检索到新 Grok Tech Report（最新: Grok 4.7, 2026-09-28） |
| InternLM (Shanghai AI Lab) | 未检索到新增（Sage S2.1 Flash, arXiv:2611.21072, 见 [[2026-11-18/tech-report-digest]]） |
| Apple | AFM 3（见 [[2026-11-18/tech-report-digest]]） |
| StepFun | 最新 Step-1/Step-1V（100B+，早期 digest 可见） |
| Yi (01.AI), Baichuan | 未检索到新增确认 |

---
