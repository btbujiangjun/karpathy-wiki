---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-16
updated: 2026-08-16
sources: [tech-report-digest-2026-08-15.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax, daily-digest]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-16（每日更新；今日重点：**DeepSeek V4 新定价 08-16 生效**——V4 Flash $0.14 in / $0.28 out（cache hit $0.0028）、V4 Pro $0.435/$0.87 每 M tokens，SGLang Day-0 支持（PR #23600）+ LMSYS Miles 同步，峰谷/分层定价成国产 API 标配；**Grok 4.6 上线 GitHub Copilot（08-14）**——xAI 生态渠道再扩（此前 Grok Bot 08-11 持久云算力 AI teammate）；**Step 3.7 Flash 由 single-source 升级为正式条目**——05-29 多源确认（官方博客/IT之家/NVIDIA/OpenRouter）：196B+1.8B ViT ≈198B/11B 激活、256K ctx、400 tok/s、原生多模态、Advisor Mode 达 Claude Opus 4.6 编码性能 97% 成本 1/9，**无正式 arXiv 报告**（官方引用 arXiv:2605.27761 为 AndroidDaily 论文）；**Apple AFM 3 规格补全**——IFP 稀疏化（20B 存 flash 激活 1-4B）、Google TPU 合作训练、Cloud Pro 跑 Google Cloud NVIDIA GPU、评测（Cloud 64.7% vs 8.7% 偏好/dictation 44.7%/TTS MOS 4.15）、EU/大陆首发不可用，技术报告仍承诺 "later summer"；**Meta Llama 4 405B 开放权重持续未兑现（第 5 天）**）
> 交叉观察：**后训练 Scaling 成为新的竞争前沿**（GLM-5.3 "同基座、纯后训练提智"叙事延续）；**中国开源旗舰"周更"节奏**（Kimi K3 → DeepSeek V4-Pro → Qwen3.8 Max+27B → GLM-5.3）持续；**开放权重"能力/许可证双轨"分化**（Qwen3.8 2.4T 定制 license vs 27B Apache 2.0）；**稀疏注意力/稀疏激活进入收敛期**（MSA/CSA/IndexShare/Delta Attention/IFP）；**Agent 化能力成官方评测主战场**（GLM-5.3 Terminal-Bench 3.0/DeepSWE/CyberGym、Grok 4.6 Copilot、Step 3.7 Flash Advisor Mode、Gemini 3.7 Flash agentic coding）；**Meta 仍是唯一持续失约方（第 5 天）**。

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek V4 技术报告（继承 08-15，今日补新定价生效）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V4 技术报告——CSA 稀疏注意力与混合注意力架构 |
| **英文标题** | DeepSeek-V4 Technical Report |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4-Pro（**1.6T 总参 / 49B 激活 MoE**）；V4-Flash（284B 总参 / 13B 激活 MoE） |
| **发布日期** | 论文 arXiv:2606.19348（2026-04-26）；V4-Pro 官方 GA **2026-08-12** |
| **核心创新** | **CSA（Compression Sparse Attention）+ HCA 混合注意力**；mHC 残差连接；Muon 优化器；32T+ tokens 预训练；1M ctx；V4-Pro 单 token FLOPs 仅 V3.2 的 **27%** |
| **论文** | https://arxiv.org/html/2606.19348 |

> 今日核实（08-16）：**新定价今日生效**——V4 Flash $0.14 in / $0.28 out（cache hit $0.0028）、V4 Pro $0.435 in / $0.87 out（cache hit $0.0036）每 M tokens；**SGLang Day-0 支持**（PR #23600）、LMSYS Miles 同步上线；V4-Pro 官方 GA 获 Reuters 08-13 报道确认（旗舰 vs 性价比分层明确）；OpenRouter `deepseek-v4-pro-0813` 与 V4 Flash 均 MIT 开放权重，V4 家族全线开源。

### 1.2 V4-Flash Agent 能力（继承 08-15，保留）

- V4-Flash（284B/13B）：Terminal Bench 2.1 **82.7**、NL2Repo **54.2**、Cybergym **76.7**、DeepSWE **54.4**、Toolathlon verified **70.3**、Agent Last Exam **25.2**。

---

## 2. OpenAI

### 2.1 GPT-5.6 System Card——GPT-Red 自动红队更新（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 System Card 更新——GPT-Red 自动红队评估 |
| **英文标题** | GPT-5.6 System Card: GPT-Red automated red teaming update |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（**Sol** 旗舰 / **Terra** 低成本 / **Luna** 最快最省） |
| **发布日期** | System Card 2026-07-09；**GPT-Red 增补 2026-08-03** |
| **核心创新** | **GPT-Red**：以自博弈 RL 训练的自动红队评估机制，纳入 System Card 发布后监测；Sol 为 Plus/Pro 默认、Luna 覆盖 Free/Go |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6 |

### 2.2 GPT-5.6 Sol Ultrafast——Cerebras 加速服务（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 Sol Ultrafast——Cerebras 托管加速版 |
| **英文标题** | GPT-5.6 Sol Ultrafast (Cerebras) |
| **发布机构** | OpenAI + Cerebras 合作 |
| **模型系列** | GPT-5.6 Sol（Ultrafast 加速服务） |
| **发布日期** | 2026-08-14 |
| **核心创新** | Cerebras 平台托管 GPT-5.6 Sol 的加速推理服务；官方口径 **chart 上 14×、end-to-end 5.6×** 提速（非新模型，为部署/基础设施合作） |
| **论文** | Cerebras Ultrafast tier 公告 |

> 今日核实：公开旗舰仍为 GPT-5.6；Astra（08-01 定名，"next major model"）Preparedness 评估（08-07）或首次触及 Critical 网络安全阈值——仍为待官方完整报告的观察项。

---

## 3. Meta

### 3.1 Llama 4 405B 开放权重——持续未兑现（第 5 天，08-16 核实）

> ⚠️ **验收结论延续（08-16）：** "Meta Llama 4 405B 开放权重"仍无发布实据——仅 NeuralStack 07-28 同一条预告反复出现（405B、原生多模态 text/image/audio、15T tokens 含 2.4T 图文对、单 H100 32 tok/s）；llama.com 目录仍仅 Llama 4 Scout/Maverick（2025-04 时代）。annlive 04-24 "Llama 4 405B is out" 报道已判定为**低可信度内容农场文章**（与 llama.com 目录、innFactory 家族表、07-27 官方预告均矛盾），不采信。实际重大事件仍为 08-10 开放权重战略转向（开源 30B Muse Glimmer：Apache 2.0、128K ctx、由 Muse Spark 蒸馏 + 承诺数周内开源 Muse Spark 1.2 权重）。

### 3.2 Muse 系列（继承 08-15，保留）

- **Muse Spark Safety & Preparedness Report**（2026-07，arXiv:2606.12429）；**Muse Code**（08-05）；**Muse Spark 1.2**（08-05，Terminal-Bench 82.9%）。

---

## 4. Google DeepMind

### 4.1 Gemini 3.7 Flash GA（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.7 Flash 正式发布（GA） |
| **英文标题** | Gemini 3.7 Flash GA |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.7 Flash |
| **发布日期** | GA：**2026-08-13** |
| **核心创新** | **1M input / 64K output** 上下文；$0.75 in / $3.75 out 每 M tokens（intro pricing 至 **2026-12-31**）；**Terminal-Bench 2.1 85.8**；主打 **agentic coding 与 terminal execution**，接近 Pro 级 agentic 能力 |
| **论文** | https://deepmind.google/models/gemini/flash/ |

> 今日核实：Gemini 3.6 Flash Model Card（07-21）为上一代；Gemini 3.1 Pro Model Card（2026-02）仍为最新 Pro 级卡；**Gemini 4 预训练中**（07-21，"most ambitious pretraining run yet"）。Flash-Lite 定价（综合 $2.80）此前已被 GPT-5.6 Luna（$1.40）超越。

---

## 5. Anthropic

### 5.1 Claude Sonnet 5 / Opus 5 System Cards（继承 08-15）

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

> 今日核实：Claude Fable 5 为当前 frontier（Mythos Preview System Card 04-07 仍为最先进闭源前沿卡）；Fable 5.1 仍无官方公告（08-16 复核，仅两条 X 泄漏与 geeky-gadgets 07-28 "8 月 beta 发布"预告，$10/$50 为传闻）——观察项；8 月 Anthropic 动态集中在企业功能（MCP 支持 07-28、skill/plugin 安全扫描 08-06），无新模型卡。

---

## 6. Mistral

### 6.1 Shieldstral 安全分类器（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 发布 Shieldstral——3B 开源多模态安全分类器 |
| **英文标题** | Mistral launches Shieldstral |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B 开放权重） |
| **发布日期** | 2026-08-04 |
| **核心创新** | 开源多模态安全分类器；**Apache 2.0**；策略自适应 QA 框架（policy-adaptive）；单 token 校准安全分数；匹配 **7× 体积模型**；16GB GPU 可跑；12 语言；Open Secure AI Alliance 成员 |
| **论文** | https://mistral.ai/news/shieldstral/ |

### 6.2 欧洲主权 AI 基础设施 & 机器人方向（继承 08-15，保留）

- **08-11 官方博客**：in-region inference + 开放模型 + 欧洲基础设施；**Robostral Navigate**（机器人导航系统，具身智能延伸）。

### 6.3 Mistral 3 开源家族（继承 08-13 备忘，保留）

- **Mistral 3**（2025-12）：开源 **3B / 8B / 14B** × base / instruct / reasoning 变体，边缘设备可运行。

> 今日核实：仍无新 LLM 技术报告；"夏季大而稀疏开放 MoE"预告（08-02）未发布，观察项。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-27B 正式开源（继承 08-15，08-14 发布）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-27B 正式开源——Apache 2.0 + 原生多模态 |
| **英文标题** | Qwen3.8-27B open-sourced (Apache 2.0, native vision) |
| **发布机构** | Alibaba Qwen |
| **模型系列** | **Qwen3.8-27B**（27B dense，原生 vision-language，image+video 输入）；另有 FP8 量化变体 |
| **发布日期** | **2026-08-14**（HF `Qwen/Qwen3.8-27B` + FP8、ModelScope、GitHub `AlibabaCloud-Official/Qwen3.8-27B`；OpenRouter 同日上架 $0.45/$3.20 每 M tokens） |
| **核心创新** | **Apache 2.0**（Qwen3.8 家族最宽松许可）；64 层 = **16 组 Hybrid Gated DeltaNet + Gated Attention 重复块**；**262,144 native ctx**（YaRN 可扩至 ~1M）；thinking 默认开启 + `reasoning_effort` xhigh/medium/low 可调；整体超越 **Qwen3.7-Plus** |
| **评测** | DeepSWE v1.1 **42.2**（vs 3.6-27B 13.3，近 3×）；Terminal-Bench 2.1 **73.0**；SWE-bench Pro **61.7**；OSWorld-Verified **84.3**；WebArena-Verified **64.8**；LiveCodeBench v6 **90.3**；GPQA Diamond **89.2**；CoWorkBench **70.7**（超 Opus 4.6 Max 的 68.2）；QwenSWEBench **79.0** |
| **部署** | BF16 ~56GB / FP8 ~28GB（单 48GB 卡）/ 4-bit ~14-17GB（社区估算）；本地 agent 工作负载友好 |
| **论文** | https://huggingface.co/Qwen/Qwen3.8-27B；https://github.com/AlibabaCloud-Official/Qwen3.8-27B |

> 关键对比：**Qwen3.8 开放权重出现"能力/许可证双轨"**——27B 为 Apache 2.0 + 原生多模态（image+video）+ thinking 可调；2.4T 旗舰权重则为定制 `qwen3.8-max` license + **text-only + thinking 强制开启**。Reddit r/LocalLLaMA 称 27B 为 "beloved Qwen 的 renewal，unmatched intelligence density"。

### 7.2 Qwen3.8-Max 开源权重兑现（继承 08-15，今日补 PaperBench）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max 开源权重上架（验收日 08-12/13，今日补评测） |
| **英文标题** | Qwen3.8-Max open weights live on HF |
| **发布机构** | Alibaba Qwen |
| **模型系列** | **Qwen3.8-2.4T-A95B**（2.4T 总参 Sparse MoE / ~95B active / 512 专家：10 routed + 1 shared / 1M ctx extensible）；Qwen3.8-27B（同日） |
| **发布日期** | API GA：2026-08-03；**权重：2026-08-12/13 上架 HF/ModelScope** |
| **核心创新** | 首个开源权重的 Max 级模型；**text-only 权重**（与多模态 API 明确区分）；**thinking required-on**；**license `qwen3.8-max`**（定制，大客户 revenue share 条款未公开）；三阶段 post-training（real-environment scaling + unified reward + online data balancing）；**PaperBench 93%**；4-bit 量化约 1.2TB VRAM |
| **论文** | https://qwen.ai/blog?id=qwen3.8 |

### 7.3 其他 Qwen 条目（继承 08-15，保留）

- **Qwen3.7-Flash**（07-25）；**Qwen-Audio-3.0-ASR-Flash**（07-30）；**Qwen-UI-Agent TR**（07，arXiv:2607.28227）。

---

## 8. Microsoft（Phi）

### 8.1 Phi-5 仍无官方技术报告（今日复核无变化）

> 截至 08-16 **仍无 Phi-5 官方技术报告**；MSR 最新技术报告仍为 **Phi-4-reasoning-vision-15B**（2026-03-04，arXiv:2603.03975，SigLIP-2 视觉编码器 + mid-fusion）与 **Phi-Ground-Any-4B**（2026-05，arXiv:2605.12501，GUI grounding）。rateais / Spheron 博客（05-26）提及 "Phi-5 pre-release announcements"，与 systems-analysis 07-11 复核（"no Phi-5 generation announced"）矛盾，判定 **Phi-5 仍为传闻**（single-source），不入正式条目。Phi-4 / Phi-4-mini / Phi-4-multimodal 仍为开放模型家族最新（MIT license，Phi-4 14B 为旗舰小模型）。

### 8.2 Phi Silica Platform Card（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi Silica Platform Card——Windows NPU 端侧 SLM |
| **英文标题** | Phi Silica Platform Card |
| **发布机构** | Microsoft |
| **模型系列** | Phi Silica（端侧 SLM） |
| **发布日期** | Platform Card：2026-06-24（更新 07-08） |
| **核心创新** | Windows PC NPU 本地运行（Copilot+ PC）；**speculative decoding**；Text Intelligence Skills（Summarize / Rewrite / Text-to-Table）；**LoRA 微调支持**；Windows App SDK / Windows AI API 集成 |
| **论文** | https://learn.microsoft.com/en-us/windows/ai/cards/phi-silica-platform-card |

---

## 9. Apple

### 9.1 AFM 3 家族（今日补全规格：IFP、Google TPU 合作、评测数据）

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Foundation Models 3 技术报告——五模型家族 |
| **英文标题** | Apple Foundation Models (AFM 3) Technical Report |
| **发布机构** | Apple |
| **模型系列** | **AFM 3 Core**（3B dense 端侧）；**AFM 3 Core Advanced**（20B sparse 端侧，IFP 激活 1–4B）；AFM 3 Cloud（PCC）；ADM 3 Cloud（图像生成/编辑）；AFM 3 Cloud Pro（最强大、agentic 工具使用，PCC on Google Cloud NVIDIA GPU） |
| **发布日期** | 技术报告：**2026-06-08**（WWDC26） |
| **核心创新** | **IFP（Instruction-Following Pruning）稀疏化**——20B 权重存 flash（NAND）、每次仅激活 1–4B；**与 Google 合作构建**（Google TPU 上训练、复用 Gemini 技术 + Apple 自有数据后训练）；**PCC 首次延伸到 Apple 数据中心之外**（Cloud Pro 跑 Google Cloud NVIDIA GPU，加密证明 + 透明日志 + 只信任 Apple 签名软件）；Foundation Models framework 端侧图像输入免费开放给 Swift 开发者 |
| **评测** | 文本偏好：AFM 3 Cloud **64.7%** vs 2025 Server 8.7%；AFM 3 Core 45.6% vs 23.3%；dictation 偏好 17.6%→**44.7%**；TTS MOS **4.15**（conversational 4.24）vs 3.87/3.82 |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

> 今日核实：正式技术报告承诺 "later this summer"（截至 08-16 仍在窗口内）未兑现；上线地区限制——EU iPhone/iPad 及中国大陆首发不可用（监管原因非技术）；上一代技术报告 Apple Intelligence Foundation Language Models Tech Report 2025（2025-07-17）。

---

## 10. NVIDIA

### 10.1 Nemotron 3.5 Lightning（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron 3.5 Lightning——面向长时运行 Agent 的开放 MoE |
| **英文标题** | NVIDIA Nemotron 3.5 Lightning (blog) |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3.5 Lightning（**30B MoE / 3B active**） |
| **发布日期** | 2026-08-11（developer blog） |
| **核心创新** | 面向 **always-on agents**（OpenClaw / Hermes Agent / NemoClaw）；**speculative decoding**；NVFP4 / BF16 checkpoints；最高 **4× 输出速度**；NeMo Switchyard 路由；开源 |
| **论文** | https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/ |

### 10.2 Nemotron 3 家族（继承 08-15，保留）

- **Ultra**（06-09）：550B/55B hybrid **Mamba-Attention** MoE + LatentMoE + MTP + NVFP4；1M ctx。
- **Super**（04-03）：120B/12B；25T tokens。
- **Nano**（08-04）：30B-A3B；吞吐最高 3.3×。

> 今日核实：官方 Nemotron 3 家族总报告仍待发布。

---

## 11. xAI

### 11.1 Grok 4.6 Model Card（今日补全：Copilot 集成）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 Model Card——与 Cursor 联合开发 |
| **英文标题** | Grok 4.6 Model Card |
| **发布机构** | xAI |
| **模型系列** | Grok 4.6（**1.5T 参数级家族**） |
| **发布日期** | 约 08-07 上线；Model Card 修订 **2026-08-12**；**08-14 上线 GitHub Copilot** |
| **核心创新** | **text+image 输入 / text-only 输出**；与 **Cursor** 合作开发；500K ctx；$2/$0.50/$6（<200k）与 $4/$1/$12（>200k）每 M tokens；reasoning 四档 low/medium/high/xhigh；**Grok Bot**（08-11，持久云算力 AI teammate） |
| **论文** | https://media.x.ai/v1/website/card-7f81d41b.pdf |

> 今日核实：官方 Model Card 已发布，此前"上线无卡"的文档差距收窄；**GitHub Copilot 用户可选 Grok 4.6（08-14）**——生态渠道在 Cursor 后再扩；Grok 4.7（2.1T）计划 3-4 周后、Grok 5 年内——仍为传闻。

---

## 12. Amazon

### 12.1 Nova 2 技术报告（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2 技术报告——全模态家族 |
| **英文标题** | Amazon Nova 2 Technical Report |
| **发布机构** | Amazon |
| **模型系列** | Nova 2 **Lite** / **Pro**（可配置 extended thinking）；Nova 2 **Omni**（统一多模态）；Nova 2 **Sonic**（语音到语音） |
| **发布日期** | 2025 技术报告（"The Amazon Nova Family of Models: Technical Report and Model Card"） |
| **核心创新** | 全系最多 **1M ctx**；Hybrid Reasoning effort 控制 + 内置工具；Lite 以 7× 更低成本 / 5× 更快超 Nova Premier |
| **论文** | Amazon Nova 2 Technical Report（2025） |

> 今日核实：Nova 2 Sonic 2.1（05-21~05-28 部署）自回归 transformer 无视觉编码器；战略收缩（07-28：Nova Premier/Omni/Reel/Canvas 弃用）；新旗舰目标 re:Invent 2026 秋（11-30~12-04）。

---

## 13. ByteDance（字节跳动）

### 13.1 SeedRealtime（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | ByteDance SeedRealtime——音视频全双工 LLM |
| **英文标题** | ByteDance SeedRealtime |
| **发布机构** | 字节跳动 Seed 团队 |
| **模型系列** | SeedRealtime |
| **发布日期** | 2026 年内发布（近期） |
| **核心创新** | **原生 audio/video/text 统一架构**；全双工实时流式生成（边听边说边看）；已全行业大规模部署 |
| **论文** | ByteDance Seed 研究页 |

### 13.2 Doubao 应用规模 & 其他（继承 08-15，保留）

- **Doubao**：155M 周活、全球第 4 大 GenAI 应用、春节峰值约 145M DAU；旗舰 **Doubao Seed 2.0 Pro**（2026-02-14：text / native video / 全双工语音多模态）；Seed 2.0 系列（Pro/Lite/Mini）2026-02、Seed1.8 Agent 2026-03、Seedance 2.0 2026-02。
- **>5T/10T 参数新模型训练传闻**（08-06/07）未发布；**Seed2.1 Pro + Turbo**（07）Agent/代码工程 SOTA（视频理解多评测 SOTA 含小时级长视频）。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5.3 正式发布（继承 08-15，08-14 发布）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.3——同基座纯后训练 Scaling，"编程最强开源模型" |
| **英文标题** | GLM-5.3: post-training scaling on the same base, strongest open-source coder |
| **发布机构** | 智谱 AI |
| **模型系列** | **GLM-5.3**（**与 GLM-5.2 相同 743B 基座**；IndexShare + SAO + 新一代 Slime 框架） |
| **发布日期** | **2026-08-14**（上线 ZCode / AutoClaw / GLM Coding Plan，京东云 MaaS 当日接入；API 即将上线；**完整权重两周后开源**——先完成安全评估与加固） |
| **核心创新** | **"基座不变、后训练提智"**：数十倍长程任务环境、更丰富环境类型、超长后训练时间 → 拉升智能上界并"涌现"网络防御能力；编程体感较 GLM-5.2 **+50%** |
| **评测** | Terminal-Bench 3.0 **4.6→28.3**（开源第一）；DeepSWE v1.1 **46.2→66.9**；Agents' Last Exam **23.8→28.5**（CLI 开源第一）；GDPval-AA v2 **1,769**（超 Kimi K3 1682）；Z.ai Code Bench High 档 **31.4%**（超 Opus 4.8 最高档 29.5%，每任务 ~5 万 tokens vs ~12 万）；Max 档 **34.5%**（低于 Fable 5 的 39.5%）；**CyberGym 漏洞推理 84.5%**（超 Anthropic Mythos 5）；网络安全白盒代码审查/漏洞发现持平 Mythos 5，真实代码库累计识别 **2436** 个安全漏洞 |
| **论文** | https://bigmodel.cn/（官方公告）；IT之家：https://view.inews.qq.com/a/20260814A084MO00 |

> ⚠️ **修正记录延续（08-15 起）：** 08-14 digest 曾记 "GLM-5.3 传闻（>1T）未发布，不入正式条目"——已核实 GLM-5.3 **于 08-14 正式发布**，参数量为 **743B（与 5.2 同基座）**，此前 ">1T" 传闻口径错误；GLM-5.5 仍无消息。权重开源（约 08-28）与第三方独立复测安全能力为下一观察点。

### 14.2 GLM-5.2（继承 08-15，已被 5.3 取代为发布主线）

- **GLM-5.2**（06-16，MIT）：744B MoE / 约 40B active / **1M ctx**；**IndexShare** 每 4 层复用同一 indexer，1M ctx 下 FLOPs **−2.9×**；MTP acceptance +20%；GLM-4.7 预算默认（SWE-bench Verified 73.8%）。https://z.ai/blog/glm-5.2

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3 技术报告（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K3——首个开源 3T 级模型（Delta Attention + Attention Residuals + Stable LatentMoE） |
| **英文标题** | Kimi K3 Technical Report |
| **发布机构** | Moonshot AI（月之暗面） |
| **模型系列** | Kimi K3（**2.8T MoE / 104B 激活**） |
| **发布日期** | API 07-16；全量权重 + 47 页技术报告 **07-27** |
| **核心创新** | 93 层（69 KDA + 24 Gated MLA）；896 路由专家（激活 16）；**Kimi Delta Attention** + **Attention Residuals** + **Stable LatentMoE**；MoonViT-V2；MXFP4/8；1M ctx；原生视觉；相对 K2 约 **2.5× scaling efficiency**；前后各领域 RL；WebDev Arena #1 |
| **论文** | https://arxiv.org/abs/2607.24653 |

> 今日核实：Kimi K4 训练中（The Information 07-28/29）未发布；K3 仍落后 Claude Fable 5 / GPT-5.6 Sol 的闭源前沿；GDPval-AA v2 1682 已被 GLM-5.3（1769）超越。

---

## 16. InternLM（上海 AI 实验室）

### 16.1 InternGeometry（继承 08-15，ICLR 2026）

| 项目 | 内容 |
|------|------|
| **中文标题** | InternGeometry——复杂度提升 RL 驱动的几何推理 |
| **英文标题** | InternGeometry: complexity-boosted RL for geometry |
| **发布机构** | 上海 AI 实验室 |
| **模型系列** | 基于 **InternThinker-32B** |
| **发布日期** | ICLR 2026 poster |
| **核心创新** | **CBRL（Complexity-Boosted RL）**：随训练提升题目复杂度；符号引擎交互；IMO 2000-2024 几何题 **44/50**（金牌平均 40.9）；仅 13K 训练样例 |
| **论文** | ICLR 2026（InternGeometry） |

### 16.2 家族状态（继承 08-15，今日补旗舰验证）

- **InternLM3-8B-Instruct**（2026-01-15，4T tokens，训练成本 −75%）；**InternThinker**（2025-11-25）；**Intern-S2-Preview**（35B 07-17 / 397B 07-18，Apache-2.0）；**Intern-S1-Pro**（2026-02-05，**1T 参数开放科学推理 MoE**，arXiv:2508.15763——近期最大开放权重旗舰）。

> 今日核实：无 8 月新模型报告；InternLM4 官方状态不明（04-13 传闻，未确认）。

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4 与清华联合（继承 08-15）

| 项目 | 内容 |
|------|------|
| **中文标题** | 百川与清华联合医疗增强模型 Baichuan-M4 登顶 HealthBench |
| **英文标题** | Baichuan-M4 (Tsinghua joint) tops HealthBench |
| **发布机构** | 百川智能 + 清华大学 |
| **模型系列** | **Baichuan-M4**（临床级医疗 Agent）；Baichuan-M3（2026-01，235B）；Baichuan-M2（08-11，32B 开源，HealthBench 60.1）；Baichuan-M1（14B，arXiv:2502.12671） |
| **发布日期** | M4：2026-05-26/06-22；清华合作公布 08-12 |
| **核心创新** | HealthBench **68.6** 世界第一（M4）；hallucination 3.3%；M2 以 32B 超 gpt-oss-120B；Baichuan-Harness 评测框架；SPAR++ 跨度奖励 |
| **论文** | arXiv:2606.08982（M4） |

> 今日核实：战略全面转向医疗垂直；通用线最新为 **Baichuan4 / Baichuan4-Turbo / Baichuan4-Air**（Air 为 PRI 架构 MoE，价格 0.98 厘/千 token）——均为 2024-2025 时代，无 8 月新通用模型。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3（继承 08-15，规格以官方 321B/38B 为准）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3——原生多模态推理大模型开源 |
| **英文标题** | StepFun Step 3 open-sourced |
| **发布机构** | 阶跃星辰（StepFun） |
| **模型系列** | Step 3（**321B 总参 / 38B 激活** MoE） |
| **发布日期** | WAIC 2025 发布；**07-31 开源** |
| **核心创新** | 原生多模态推理；**MFA（Multi-matrix Factorization Attention）** + **AFD（Attention-FFN Disaggregation）**；NVIDIA Hopper 上吞吐较 DeepSeek-R1 **+70%**；8×48GB 显卡可推理 |
| **论文** | https://github.com/stepfun-ai/Step3 |

### 18.2 Step 3.7 Flash（今日由 single-source 升级为正式条目，05-29 多源确认）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3.7 Flash——面向生产级 Agent 的高效率 Flash 模型开源 |
| **英文标题** | StepFun Step 3.7 Flash: efficient Flash model for real-world agents |
| **发布机构** | 阶跃星辰（StepFun） |
| **模型系列** | Step 3.7 Flash（**196B + 1.8B ViT ≈ 198B 总参 / 11B 激活** MoE） |
| **发布日期** | **2026-05-29**（此前 08-13/14/15 记 ~2026-03，今日以官方口径修正） |
| **核心创新** | **原生多模态**（图像+视频）+ 联网/视觉搜索增强；**256K ctx**；最高 **400 tok/s**；高可靠工具调用与编排（兼容 Claude Code / KiloCode / Hermes Agent / OpenClaw 等）；**Advisor Mode**：达到 Claude Opus 4.6 编码性能 **97%**、成本仅 **1/9**；开源（GitHub/HF/ModelScope）+ SGLang / TensorRT-LLM / vLLM / NVIDIA NIM 部署 |
| **评测** | SWE-Bench Pro **56.26**；Terminal-Bench 2.1 **59.55**；Toolathlon **49.51**；ClawEval-v1.1 **67.07**；DeepSearchQA 92.82 F1（较 3.5 Flash 85.48 提升） |
| **论文** | https://static.stepfun.com/blog/step-3.7-flash/ |

> 今日核实：多源交叉确认（官方博客、IT之家、NVIDIA 技术博客、OpenRouter）；**无正式 arXiv 技术报告**（官方引用的 arXiv:2605.27761 经核实为 AndroidDaily 论文，非本模型）；相对 Step 3.5 Flash（2026-02，196B/11B，纯文本）主要增量 = 原生多模态 + Advisor Mode + 搜索增强。Step 4 训练（2026-02 宣布）为下一观察点。Step3-VL-10B（2026-01，PaCoRe，arXiv:2601.09668）。

---

## 19. Yi / 01.AI

### 19.1 状态（继承 08-15，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | 零一万物转向企业 AI / 主权 AI 战略 |
| **英文标题** | 01.AI pivots to enterprise & sovereign AI |
| **发布机构** | 01.AI（零一万物） |
| **模型系列** | 最新模型仍为 **Yi-Lightning**（2024-10-16，千亿参数 MoE，Chatbot Arena #6，arXiv:2412.01253） |
| **发布日期** | 最新动态：万策平台（2026-07）；哈萨克斯坦 Q.AI 合资（2026） |
| **论文** | https://www.01.ai |

> 今日核实：2026 无新旗舰或新技术报告；发布节奏自 2025 起明显放缓（被 DeepSeek / Qwen / GLM / Kimi 全面超越）；重心转向企业级解决方案、主权 AI 与行业落地。

---

## 20. MiniMax

### 20.1 M3 完整规格（继承 08-15，仍为国内首个开放世界旗舰）

| 项目 | 内容 |
|------|------|
| **中文标题** | MiniMax M3 技术报告与开源权重——MSA 稀疏注意力 + 7-MTP |
| **英文标题** | MiniMax M3: MSA sparse attention + 7-MTP, open weights |
| **发布机构** | MiniMax |
| **模型系列** | **M3**（**428B 总参 / 23B 激活**，原生多模态，1M ctx）；M2.7 已退役 |
| **发布日期** | 2026-06-01 发布；技术报告 + 开源权重齐备（arXiv:2606.13392，GitHub `MiniMax-AI/MiniMax-M3`） |
| **核心创新** | **MSA（MiniMax Sparse Attention）**：Index Branch O(T) 评分为每 query 选 top-16 KV block（block=128 tokens）+ Main Branch 精确注意力，注意力 FLOPs 与序列长度解耦；1M ctx 下相对 M2 **prefill 9× / decode 15× 提速**、每 token 计算 **1/20**；**7-MTP** 投机解码；60 层（前 3 层 Full Attention GQA 16:1 + 3-59 层 MSA）；128 专家 top-4 **sigmoid 路由** + 1 共享专家；CLIP ViT-32L + 3D RoPE 视觉塔 |
| **评测** | **BrowseComp 83.5**（超 Opus 4.7 的 79.3）；**TrainBench 37.1** 第三（仅次 Opus 4.7 42.4 / GPT-5.5 39.3）；BenchLM 68.6；可自主完成 ICLR 杰出论文复现 |
| **论文** | https://arxiv.org/abs/2606.13392；https://github.com/MiniMax-AI/MiniMax-M3 |

> 今日核实：M4 仍为 H2 2026 承诺；MiniMax H3（07-31/08-02，33B dense Omni Transformer）视频生成评测列全球第一。

---

## 交叉观察

- **后训练 Scaling 成为新的竞争前沿**：GLM-5.3 首次把"**同基座、纯后训练提智**"作为旗舰发布叙事（数十倍长程环境 + 超长后训练时间拉高智能上界），与 Kimi K3（2.5× scaling efficiency）、MiniMax M3（cowork/computer use）、DeepSeek V4（重预训练）并列为两种打法——"预训练基座 + 长程 RL 环境"成为差异化主轴。
- **中国开源旗舰"周更"节奏**：两周内 Kimi K3 权重（07-27）、DeepSeek V4-Pro GA（08-12）、Qwen3.8-Max 2.4T 权重（08-12/13）+ Qwen3.8-27B（08-14）、GLM-5.3（08-14）连续放量（IT之家："国产旗舰月月有新版本"）——开源前沿能力密度与兑现速度均在提升。
- **开放权重"能力/许可证双轨"分化出现**：Qwen3.8 首次出现同代权重的明确分层——2.4T 旗舰（定制 license + text-only + thinking 强制）vs 27B（Apache 2.0 + 原生多模态 + thinking 可调）；对照 GLM-5.3 承诺两周后开源、DeepSeek V4 全系 MIT——中国开源阵营许可策略开始分化。
- **稀疏注意力/稀疏激活进入收敛期**：MSA（MiniMax）、CSA（DeepSeek V4）、IndexShare（GLM-5.2/5.3）、Delta Attention（Kimi K3）、IFP（Apple AFM 3 Core Advanced）各自独立提出相似方案，"context 与计算解耦"成为旗舰共识；1M 上下文 + 原生多模态成为旗舰标配。
- **Agent 化能力成官方评测主战场**：GLM-5.3（Terminal-Bench 3.0 / DeepSWE / CyberGym）、Grok 4.6（Copilot 集成 + Cursor 联合开发）、Step 3.7 Flash（Advisor Mode）、Gemini 3.7 Flash（agentic coding/terminal）、MiniMax M3（cowork/computer use）、Qwen3.8-27B（OSWorld 84.3）——"写代码 + 用工具 + 长程执行 + 挖漏洞"成为发布必述能力。
- **Meta Llama 4 405B 持续未兑现（第 5 天）**：与 DeepSeek V4 Pro GA + MIT 权重、Qwen3.8 双权重兑现、GLM-5.3 开源承诺形成对照，Meta 成唯一持续失约方；Apple AFM 3 技术报告（"summer"承诺窗口内仍未出）为另一待兑现项。
- **传闻需谨慎（未确认不入正式条目）**：Meta Llama 4 405B（未兑现）、GLM-5.5（无消息）、Grok 4.7（2.1T）/Grok 5、Kimi K4、MiniMax M4（H2 2026）、Phi-5（single-source pre-release 传闻）、Fable 5.1（无官方公告）、InternLM4、字节 >5T/10T 新模型、Mistral 夏季"大而稀疏"开放权重、Astra"GPT-6"命名、Step 4 训练。
