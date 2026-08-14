---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-14
updated: 2026-08-14
sources: [tech-report-digest-2026-08-13.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax, daily-digest]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-14（每日更新；今日重点：**MiniMax M3 完整规格补全**——官方技术报告/开源权重齐备（GitHub `MiniMax-AI/MiniMax-M3` + arXiv:2606.13392），**428B 总参 / 23B 激活** 原生多模态 MoE，1M ctx 下相对 M2 **prefill 9× / decode 15× 提速**（每 token 计算 1/20），核心创新 MSA（MiniMax Sparse Attention）+ 7-MTP 投机解码；**Gemini 3.7 Flash GA（08-13）**——1M input / 64K output ctx、$0.75/$3.75 每 M tokens（intro pricing 至 2026-12-31）、主打 agentic coding 与 terminal execution，接近 Pro 级 agentic 能力；**GPT-5.6 System Card 增补（08-03）**——新增 GPT-Red 自动红队评估（自博弈 RL）；**Grok 4.6 Model Card（08-12 修订）**——1.5T 参数级家族、text+image 输入 / text-only 输出、与 Cursor 联合开发；**NVIDIA Nemotron 3.5 Lightning（08-11）**——30B-A3B 面向 always-on agents；**Kimi K3 技术报告（07-27，arXiv:2607.24653）**——2.8T/104B 激活、Delta Attention + Attention Residuals + Stable LatentMoE、约 2.5× scaling efficiency；**Microsoft Phi 本轮核实**——仍无 Phi-5 官方报告，最新为 Phi Silica Platform Card（2026-06-24/07-08，NPU 端侧 SLM）；**Meta Llama 4 405B 开放权重持续未兑现（第 3 天）**）
> 交叉观察：MiniMax M3 以 "1M 上下文 + 原生多模态 + frontier coding/agent" 三项齐备成为**国内首个开放世界旗舰**（BrowseComp 83.5 超 Opus 4.7 的 79.3、TrainBench 37.1 位列第三）；稀疏注意力进入**收敛期**——MSA（MiniMax）/ CSA（DeepSeek V4）/ IndexShare（GLM-5.2）/ Delta Attention（Kimi K3）各自独立提出相似方案，1M+ 长上下文成为旗舰标配；闭源前沿"文档差距"仍在——Meta 405B（无报告）、Apple AFM 3（"summer"承诺）缺口持续；Agent 化能力（coding、cowork、computer use）成为 2026 下半年官方评测主战场。

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek V4 技术报告（继承 08-13，本轮补全论文细节）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V4 技术报告——CSA 稀疏注意力与混合注意力架构 |
| **英文标题** | DeepSeek-V4 Technical Report |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4-Pro（**1.6T 总参 / 49B 激活 MoE**）；V4-Flash（284B 总参 / 13B 激活 MoE） |
| **发布日期** | 论文 arXiv:2606.19348（2026-04-26）；V4-Pro 官方 GA **2026-08-12** |
| **核心创新** | **CSA（Compression Sparse Attention）+ HCA 混合注意力**；mHC 残差连接；Muon 优化器；32T+ tokens 预训练；1M ctx；V4-Pro 单 token FLOPs 仅 V3.2 的 **27%** |
| **论文** | https://arxiv.org/html/2606.19348 |

> 今日核实：V4 Pro（OpenRouter `deepseek-v4-pro-0813`，$0.435/$0.87 每 M tokens）与 V4 Flash 均 MIT 开放权重，V4 家族全线开源。

### 1.2 V4-Flash Agent 能力（继承 08-13，保留）

- V4-Flash（284B/13B）：Terminal Bench 2.1 **82.7**、NL2Repo **54.2**、Cybergym **76.7**、DeepSWE **54.4**、Toolathlon verified **70.3**、Agent Last Exam **25.2**。

---

## 2. OpenAI

### 2.1 GPT-5.6 System Card——GPT-Red 自动红队更新（今日新增核实，08-03）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card 更新——GPT-Red 自动红队评估 |
| **英文标题** | GPT-5.6 System Card: GPT-Red automated red teaming update |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（**Sol** 旗舰 / **Terra** 低成本 / **Luna** 最快最省） |
| **发布日期** | System Card 2026-07-09；**GPT-Red 增补 2026-08-03** |
| **核心创新** | **GPT-Red**：以自博弈 RL 训练的自动红队评估机制，纳入 System Card 发布后监测；Sol 为 Plus/Pro 默认、Luna 覆盖 Free/Go |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6 |

> 今日核实：公开旗舰仍为 GPT-5.6；Astra（08-01 定名，"next major model"）Preparedness 评估（08-07）或首次触及 Critical 网络安全阈值——仍为待官方完整报告的观察项。

---

## 3. Meta

### 3.1 Llama 4 405B 开放权重——持续未兑现（第 3 天，08-14 核实）

> ⚠️ **验收结论延续（08-14）：** "Meta Llama 4 405B 开放权重"仍无发布实据——仅 NeuralStack 07-28 同一条预告反复出现（405B、原生多模态 text/image/audio、15T tokens 含 2.4T 图文对、单 H100 32 tok/s）；llama.com 目录仍仅 Llama 4 Scout/Maverick（2025-04 时代）。实际重大事件仍为 08-10 开放权重战略转向（开源 30B Muse Glimmer：Apache 2.0、128K ctx、由 Muse Spark 蒸馏 + 承诺数周内开源 Muse Spark 1.2 权重）。

### 3.2 Muse 系列（继承 08-13，保留）

- **Muse Spark Safety & Preparedness Report**（2026-07，arXiv:2606.12429）；**Muse Code**（08-05）；**Muse Spark 1.2**（08-05，Terminal-Bench 82.9%）。

---

## 4. Google DeepMind

### 4.1 Gemini 3.7 Flash GA（今日新增核实，08-13）

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.7 Flash 正式发布（GA） |
| **英文标题** | Gemini 3.7 Flash GA |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.7 Flash |
| **发布日期** | GA：**2026-08-13** |
| **核心创新** | **1M input / 64K output** 上下文；$0.75 in / $3.75 out 每 M tokens（intro pricing 至 **2026-12-31**）；主打 **agentic coding 与 terminal execution**，接近 Pro 级 agentic 能力 |
| **论文** | https://deepmind.google/models/gemini/flash/ |

> 今日核实：Gemini 3.6 Flash Model Card（07-21）为上一代；Gemini 3.1 Pro Model Card（2026-02）仍为最新 Pro 级卡；**Gemini 4 预训练中**（07-21，"most ambitious pretraining run yet"）。Flash-Lite 定价（综合 $2.80）此前已被 GPT-5.6 Luna（$1.40）超越。

---

## 5. Anthropic

### 5.1 Claude Sonnet 5 / Opus 5 System Cards（本轮补全，新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Sonnet 5 System Card（RSP+agentic 升级） |
| **英文标题** | Claude Sonnet 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Sonnet 5（升级自 Sonnet 4.6） |
| **发布日期** | System Card：**2026-06-30** |
| **核心创新** | agentic coding 增益；MASK 说谎率 3.1%（对比集最低）；hallucination/sycophancy 显著改善 |
| **论文** | anthropic.com（System Card 文档） |

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 System Card——agentic coding / long-horizon 能力 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Opus 5 |
| **发布日期** | 2026-07-24 |
| **核心创新** | SWE-bench Verified **96.0**、SWE-bench Pro **79.2**、Frontier-Bench v0.1 **43.3**、ARC-AGI-3 **30.2**；effort dial $5/$25 每 M in/out；接近 Claude Fable 5 智能、半价 |
| **论文** | anthropic.com（System Card + 风险报告） |

> 今日核实：Claude Fable 5 为当前 frontier（Mythos Preview System Card 04-07 仍为最先进闭源前沿卡）；Fable 5.1 仍无官方公告（08-03 复核，仅两条 X 泄漏，$10/$50 为传闻）。

---

## 6. Mistral

### 6.1 Shieldstral 安全分类器（本轮补全规格，08-04）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 发布 Shieldstral——3B 开源多模态安全分类器 |
| **英文标题** | Mistral launches Shieldstral |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B 开放权重） |
| **发布日期** | 2026-08-04 |
| **核心创新** | 开源多模态安全分类器；**Apache 2.0**；策略自适应 QA 框架（policy-adaptive）；单 token 校准安全分数；匹配 **7× 体积模型**；16GB GPU 可跑；12 语言；Open Secure AI Alliance 成员 |
| **论文** | https://mistral.ai/news/shieldstral/ |

### 6.2 欧洲主权 AI 基础设施（继承 08-13，保留）

- **08-11 官方博客**：in-region inference + 开放模型 + 欧洲基础设施——欧洲数据在欧盟境内处理、开放权重模型为根基。

### 6.3 机器人方向（继承 08-13，保留）

- **Robostral Navigate**（Mistral AI Science Robotics）：面向机器人的导航系统；Mistral 向具身智能延伸。

> 今日核实：仍无新 LLM 技术报告；"夏季大而稀疏开放 MoE"预告（08-02）未发布，观察项。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-Max 开源权重兑现（继承 08-13，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max 开源权重上架（验收日 08-12，08-13 确认） |
| **英文标题** | Qwen3.8-Max open weights live on HF |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8-Max（**2.4T 总参 Sparse MoE / 95B 激活 / 1M ctx / 原生视觉多模态**）；Qwen3.8-27B（同日，27B dense） |
| **发布日期** | API GA：2026-08-03；**权重：2026-08-12/13 上架** |
| **核心创新** | 首个开源权重的 Max 级模型；HF 仓库 `Qwen/Qwen3.8-2.4T-A95B`；**license `qwen3.8-max`**；1M ctx；三阶段 post-training（real-environment scaling + unified reward + online data balancing）；4-bit 量化约 1.2TB VRAM |
| **论文** | https://qwen.ai/blog?id=qwen3.8 |

### 7.2 其他 Qwen 条目（继承 08-13，保留）

- **Qwen3.8-27B**（08-03）；**Qwen3.7-Flash**（07-25）；**Qwen-Audio-3.0-ASR-Flash**（07-30）；**Qwen-UI-Agent TR**（07，arXiv:2607.28227）。

---

## 8. Microsoft（Phi）

### 8.1 Phi-5 仍无官方技术报告（本轮核实无变化）

> 截至 08-14 **仍无 Phi-5 官方技术报告**；MSR 最新技术报告仍为 Phi-4-reasoning-vision-15B（2026-03）；16B/MMLU 86.7% 报道仍为 single-source（GogoAI），未确认。Phi-4 / Phi-4-mini / Phi-4-multimodal 仍为开放模型家族最新（MIT license，Phi-4 14B 为旗舰小模型）。

### 8.2 Phi Silica Platform Card（本轮新增核实，2026-06-24/07-08）

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi Silica Platform Card——Windows NPU 端侧 SLM |
| **英文标题** | Phi Silica Platform Card |
| **发布机构** | Microsoft |
| **模型系列** | Phi Silica（端侧 SLM） |
| **发布日期** | Platform Card：2026-06-24（更新 07-08） |
| **核心创新** | 在 Windows PC NPU 本地运行的端侧 SLM（Copilot+ PC）；**speculative decoding**（小辅助模型提速）；文本生成 + Text Intelligence Skills（Summarize / Rewrite / Text-to-Table）；**LoRA 微调支持**；Windows App SDK / Windows AI API 集成；组件更新版 1.2607.840.0（07-28 发布） |
| **论文** | https://learn.microsoft.com/en-us/windows/ai/cards/phi-silica-platform-card |

---

## 9. Apple

### 9.1 AFM 3 家族（继承 08-13，本轮补全规格）

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Foundation Models 3 技术报告——五模型家族 |
| **英文标题** | Apple Foundation Models (AFM 3) Technical Report |
| **发布机构** | Apple |
| **模型系列** | **AFM 3 Core**（3B dense 端侧）；**AFM 3 Core Advanced**（20B sparse 端侧，IFP 激活 1–4B）；AFM 3 Cloud（PCC）；ADM 3 Cloud（图像）；AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU） |
| **发布日期** | 技术报告：**2026-06-08**（WWDC26） |
| **核心创新** | IFP（Instruction-Following Pruning）稀疏化；端侧/云侧 PCC 双轨；**与 Google 合作构建**（Cloud Pro 跑在 Google Cloud NVIDIA GPU 上） |
| **论文** | Apple Foundation Models 3 Technical Report（2026-06-08） |

> 今日核实：正式发布承诺 "later this summer"（截至 08-14 仍在窗口内）未兑现；上一代技术报告 Apple Intelligence Foundation Language Models Tech Report 2025（2025-07-17）。

---

## 10. NVIDIA

### 10.1 Nemotron 3.5 Lightning（本轮补全规格，08-11）

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron 3.5 Lightning——面向长时运行 Agent 的开放 MoE |
| **英文标题** | NVIDIA Nemotron 3.5 Lightning (blog) |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3.5 Lightning（**30B MoE / 3B active**） |
| **发布日期** | 2026-08-11（developer blog） |
| **核心创新** | 面向 **always-on agents**（OpenClaw / Hermes Agent / NemoClaw）；**speculative decoding**；NVFP4 / BF16 checkpoints；最高 **4× 输出速度**；NeMo Switchyard 路由；开源 |
| **论文** | https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/ |

### 10.2 Nemotron 3 家族（继承 08-13，保留）

- **Ultra**（06-09）：550B/55B hybrid Mamba-Attention MoE + LatentMoE + MTP + NVFP4；1M ctx。
- **Super**（04-03）：120B/12B；25T tokens。
- **Nano**（08-04）：30B-A3B；吞吐最高 3.3×。

> 今日核实：官方 Nemotron 3 家族总报告仍待发布。

---

## 11. xAI

### 11.1 Grok 4.6 Model Card（本轮补全，08-12 修订）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 Model Card——与 Cursor 联合开发 |
| **英文标题** | Grok 4.6 Model Card |
| **发布机构** | xAI |
| **模型系列** | Grok 4.6（**1.5T 参数级家族**） |
| **发布日期** | 约 08-07 上线；Model Card 修订 **2026-08-12** |
| **核心创新** | **text+image 输入 / text-only 输出**；与 **Cursor** 合作开发；500K ctx（08-13 口径）；$2/$0.50/$6（<200k）与 $4/$1/$12（>200k）每 M tokens；reasoning 四档 low/medium/high/xhigh |
| **论文** | https://media.x.ai/v1/website/card-7f81d41b.pdf |

> 今日核实：官方 Model Card 已发布，此前"上线无卡"的文档差距收窄；Grok 4.7（2.1T）计划 3-4 周后、Grok 5 年内——仍为传闻。

---

## 12. Amazon

### 12.1 Nova 2 技术报告（本轮补全，2025）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2 技术报告——全模态家族 |
| **英文标题** | Amazon Nova 2 Technical Report |
| **发布机构** | Amazon |
| **模型系列** | Nova 2 **Lite** / **Pro**（可配置 extended thinking）；Nova 2 **Omni**（统一多模态、text+image 输出）；Nova 2 **Sonic**（语音到语音） |
| **发布日期** | 2025 技术报告 |
| **核心创新** | 全系最多 **1M ctx**；Hybrid Reasoning effort 控制 + 内置工具；Lite 以 7× 更低成本 / 5× 更快超 Nova Premier |
| **论文** | Amazon Nova 2 Technical Report（2025） |

> 今日核实：Nova 2 Sonic 2.1（05-21~05-28 部署）自回归 transformer 无视觉编码器；战略收缩（07-28：Nova Premier/Omni/Reel/Canvas 弃用）；新旗舰目标 re:Invent 2026 秋（11-30~12-04）。

---

## 13. ByteDance（字节跳动）

### 13.1 SeedRealtime（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | ByteDance SeedRealtime——音视频全双工 LLM |
| **英文标题** | ByteDance SeedRealtime |
| **发布机构** | 字节跳动 Seed 团队 |
| **模型系列** | SeedRealtime |
| **发布日期** | 2026 年内发布（近期） |
| **核心创新** | **原生 audio/video/text 统一架构**；全双工实时流式生成（边听边说边看）；已全行业大规模部署 |
| **论文** | ByteDance Seed 研究页 |

### 13.2 Doubao 应用规模（继承 08-13，保留）

- **Doubao**：155M 周活、全球第 4 大 GenAI 应用、春节峰值约 145M DAU；底层 Seed 模型经火山引擎提供；旗舰 **Doubao Seed 2.0 Pro**（2026-02-14：text / native video / 全双工语音多模态）。

### 13.3 其他（继承 08-13，保留）

- **>5T/10T 参数新模型训练传闻**（08-06/07，晚点 + FT）：未发布，观察项。
- **Seed2.1 Pro + Turbo**（07）：Agent/代码工程；视频理解多评测 SOTA（含小时级长视频）。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5.2（本轮补全规格，06-16）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.2——IndexShare 索引共享与 1M 上下文 |
| **英文标题** | GLM-5.2: 1M context with IndexShare |
| **发布机构** | 智谱 AI |
| **模型系列** | GLM-5.2（744B MoE / 约 40B active / **1M ctx**） |
| **发布日期** | 2026-06-16（**MIT** 开源） |
| **核心创新** | **IndexShare**：每 4 层稀疏注意力复用同一 indexer，1M ctx 下 FLOPs **−2.9×**；**MTP** 投机解码 acceptance **+20%**；FrontierSWE 仅差 Opus 4.8 **1%**、超 GPT-5.5 1%；GLM-4.7 预算默认（SWE-bench Verified 73.8%） |
| **论文** | https://z.ai/blog/glm-5.2 |

> 今日核实：GLM-5.3 传闻（>1T，新浪财经 07-20 + JPMorgan 8 月口径）与 GLM-5.5 均未发布，不入正式条目。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3 技术报告（本轮补全，arXiv:2607.24653）

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K3——首个开源 3T 级模型（Delta Attention + Attention Residuals + Stable LatentMoE） |
| **英文标题** | Kimi K3 Technical Report |
| **发布机构** | Moonshot AI（月之暗面） |
| **模型系列** | Kimi K3（**2.8T MoE / 104B 激活**） |
| **发布日期** | API 07-16；全量权重 + 47 页技术报告 **07-27** |
| **核心创新** | 93 层（69 KDA + 24 Gated MLA）；896 路由专家（激活 16）；**Kimi Delta Attention** + **Attention Residuals** + **Stable LatentMoE**；MoonViT-V2；MXFP4/8；1M ctx；原生视觉；相对 K2 约 **2.5× scaling efficiency**；前后各领域 RL；WebDev Arena #1 |
| **论文** | https://arxiv.org/abs/2607.24653 |

> 今日核实：Kimi K4 训练中（The Information 07-28/29，寻求更多 Blackwell 芯片）未发布；K3 仍落后 Claude Fable 5 / GPT-5.6 Sol 的闭源前沿。

---

## 16. InternLM（上海 AI 实验室）

### 16.1 InternGeometry（今日新增核实，ICLR 2026）

| 项目 | 内容 |
|------|------|
| **中文标题** | InternGeometry——复杂度提升 RL 驱动的几何推理 |
| **英文标题** | InternGeometry: complexity-boosted RL for geometry |
| **发布机构** | 上海 AI 实验室 |
| **模型系列** | 基于 **InternThinker-32B** |
| **发布日期** | ICLR 2026 poster |
| **核心创新** | **CBRL（Complexity-Boosted RL）**：随训练提升题目复杂度；符号引擎交互；IMO 2000-2024 几何题 **44/50**（金牌平均 40.9）；仅 13K 训练样例 |
| **论文** | ICLR 2026（InternGeometry） |

### 16.2 家族状态（继承 08-13，保留）

- **InternLM3-8B-Instruct**（2026-01-15，4T tokens，训练成本 −75%）；**InternThinker**（2025-11-25）；**Intern-S2-Preview**（35B 07-17 / 397B 07-18，Apache-2.0）；InternBootCamp & InternThinker·Go（2026-05-23）。

> 今日核实：无 8 月新模型报告；InternLM4 官方状态不明（04-13 传闻，未确认）。

---

## 17. Baichuan（百川智能）

### 17.1 家族状态（今日新增核实：M4 与清华联合）

| 项目 | 内容 |
|------|------|
| **中文标题** | 百川与清华联合医疗增强模型 Baichuan-M4 登顶 HealthBench |
| **英文标题** | Baichuan-M4 (Tsinghua joint) tops HealthBench |
| **发布机构** | 百川智能 + 清华大学 |
| **模型系列** | **Baichuan-M4**（临床级医疗 Agent，05-26/06-22 发布；**08-12 与清华合作**）；Baichuan-M3（2026-01，235B）；Baichuan-M2（08-11，32B 开源，HealthBench 60.1） |
| **发布日期** | M4：2026-05-26/06-22；清华合作公布 08-12 |
| **核心创新** | HealthBench **68.6** 世界第一（M4）；hallucination 3.3%；M2 以 32B 超 gpt-oss-120B；Baichuan-Harness 评测框架；SPAR++ 跨度奖励 |
| **论文** | arXiv:2606.08982（M4）；Baichuan-M2 开源（08-11） |

> 今日核实：战略全面转向医疗垂直；M2 为开源线最新，无 8 月新通用模型。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3（今日新增核实：开源细节）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3——原生多模态推理大模型开源 |
| **英文标题** | StepFun Step 3 open-sourced |
| **发布机构** | 阶跃星辰（StepFun） |
| **模型系列** | Step 3（**321B 总参 / 38B 激活** MoE） |
| **发布日期** | WAIC 2025 发布；**07-31 开源** |
| **核心创新** | 原生多模态推理；**MFA（Multi-matrix Factorization Attention）** + **AFD（Attention-FFN Disaggregation）**；NVIDIA Hopper 上吞吐较 DeepSeek-R1 **+70%**；8×48GB 显卡可推理 |
| **论文** | https://github.com/stepfun-ai/Step3 |

> 规格备忘：08-12 曾记"198B 稀疏 MoE"，本期以官方 **321B 总参 / 38B 激活** 口径为准。Step3-VL-10B（2026-01，PaCoRe，arXiv:2601.09668）；Step 3.7 Flash（~2026-03，196B+1.8B/11B，400 tok/s，single-source）；Step 4 训练（2026-02 宣布）为下一观察点。

---

## 19. Yi / 01.AI

### 19.1 状态（继承 08-13，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | 零一万物转向企业 AI / 主权 AI 战略 |
| **英文标题** | 01.AI pivots to enterprise & sovereign AI |
| **发布机构** | 01.AI（零一万物） |
| **模型系列** | 最新模型仍为 **Yi-Lightning**（2024-10-16，千亿参数 MoE，Chatbot Arena #6，arXiv:2412.01253） |
| **发布日期** | 最新动态：万策平台（2026-07）；哈萨克斯坦 Q.AI 合资（2026） |
| **论文** | https://www.01.ai |

> 今日核实：2026 无新旗舰或新技术报告；重心转向企业级解决方案、主权 AI 与行业落地。

---

## 20. MiniMax

### 20.1 M3 完整规格补全（今日最大新增，arXiv:2606.13392）

| 项目 | 内容 |
|------|------|
| **中文标题** | MiniMax M3 技术报告与开源权重——MSA 稀疏注意力 + 7-MTP |
| **英文标题** | MiniMax M3: MSA sparse attention + 7-MTP, open weights |
| **发布机构** | MiniMax |
| **模型系列** | **M3**（**428B 总参 / 23B 激活**，原生多模态，1M ctx）；M2.7（2026-03-18）已退役 |
| **发布日期** | 2026-06-01 发布；技术报告 + 开源权重随承诺兑现（arXiv:2606.13392，GitHub `MiniMax-AI/MiniMax-M3`） |
| **核心创新** | **MSA（MiniMax Sparse Attention）**：Index Branch O(T) 评分为每 query 选 top-16 KV block（block=128 tokens）+ Main Branch 精确注意力，注意力 FLOPs 与序列长度解耦；1M ctx 下相对 M2 **prefill 9× / decode 15× 提速**、每 token 计算 **1/20**；**7-MTP** 多 token 预测投机解码（7 个独立模块接最后一层 hidden）；60 层（前 3 层 Full Attention GQA 16:1 + 3-59 层 MSA）；128 专家 top-4 **sigmoid 路由** + 1 共享专家；RoPE theta 5M；视觉编码器 CLIP ViT-32L + 3D RoPE；原生多模态（第零步即混合模态训练） |
| **评测** | **BrowseComp 83.5**（超 Opus 4.7 的 79.3）；**TrainBench 37.1** 第三（仅次 Opus 4.7 42.4 / GPT-5.5 39.3）；可自主完成 ICLR 杰出论文复现（12 小时/18 commits/23 图表）；CUDA kernel 优化 147 次迭代 9.4× 加速（峰值利用率 7.6%→71.3%） |
| **定价/服务** | Token Plan 三档（Plus $20、Max $50、Ultra 档）；API ≤512K 标准价 / >512K 长上下文价；thinking / non-thinking 双模式同价；服务等级 default / priority |
| **论文** | https://arxiv.org/abs/2606.13392；https://github.com/MiniMax-AI/MiniMax-M3；https://www.minimax.io/blog/minimax-m3 |

> 今日核实：M3 成为**国内首个 "frontier coding + 1M 上下文 + 原生多模态 + 开放世界" 齐备的旗舰**（官方口径："第一个把完整 frontier 能力带进开放世界的模型"）。BenchLM 68.6；定价 $0.3/$1.2 每 M tokens。M4 仍为 H2 2026 承诺；MiniMax H3（07-31/08-02，33B dense Omni Transformer）在视频生成评测列全球第一。

---

## 交叉观察

- **稀疏注意力进入收敛期**：本周集中出现四条独立但高度同构的稀疏注意力方案——MiniMax **MSA**（Index Branch top-16 block 路由）、DeepSeek V4 **CSA**（压缩稀疏注意力）、智谱 GLM-5.2 **IndexShare**（每 4 层共享 indexer）、Moonshot K3 **Delta Attention**——共同目标都是把 1M+ 长上下文的注意力计算与序列长度解耦；"context 成为又一个可 scale 的维度"（MiniMax 官方口径）正在变成行业共识。
- **1M 上下文 + 原生多模态 = 旗舰标配**：M3（428B/1M/原生多模态）、Qwen3.8-Max（2.4T/1M/native vision）、Kimi K3（2.8T/1M/native vision）、GLM-5.2（744B/1M）、Gemini 3.7 Flash（1M input/64K output）、Nova 2（1M）——能力组合已从"可选"变成"默认"。
- **Meta Llama 4 405B 持续未兑现（第 3 天）**：与 DeepSeek V4 Pro GA + MIT 权重、Qwen3.8-Max 权重兑现、"承诺→兑现"信用标准形成对照，Meta 成唯一持续失约方。
- **Agent 化能力成官方评测主战场**：Grok 4.6（与 Cursor 联合开发）、Nemotron 3.5 Lightning（always-on agents）、Gemini 3.7 Flash（agentic coding/terminal）、M3（cowork/computer use）、Claude Sonnet 5/Opus 5（agentic coding 增益）——"写代码 + 用工具 + 长程执行"成为发布必述能力。
- **传闻需谨慎（未确认不入正式条目）**：Meta Llama 4 405B（未兑现）、GLM-5.3/5.5（未发布）、Grok 4.7（2.1T）/Grok 5、Kimi K4、MiniMax M4（H2 2026）、Phi-5（single-source）、Fable 5.1（无官方公告）、InternLM4、字节 >5T/10T 新模型、Mistral 夏季"大而稀疏"开放权重、Astra"GPT-6"命名。
