---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-04
updated: 2026-08-04
sources: [tech-report-digest-2026-08-01.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-04（每日更新；今日重点：Anthropic Claude Opus 5 System Card、Qwen3.8-Max 发布、DeepSeek-V4-Flash-0731 官方确认、MiniMax H3、Mistral Medium 3、GPT-5.7 / GLM-5.5 传闻核实）

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4-Flash-0731（今日官方确认）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4-Flash-0731 刷新版 |
| **英文标题** | DeepSeek-V4-Flash-0731 |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4-Flash（284B 总参 / 13B 激活 MoE） |
| **发布日期** | 2026-07-31 |
| **架构** | 与 4 月 V4-Flash 同架构（CSA Compressed Sparse Attention），重新后训练（re-post-trained） |
| **核心创新** | 官方构建版，在 DeepSeek 全部 9 项 agent benchmark 上超越 V4-Pro-Preview；MIT 权重开源（HF）；API $0.14 in / $0.28 out 每 M tokens，98% cache-hit 折扣 |
| **论文** | https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731 |

> 延续 V4-Flash 序列快速迭代节奏；确认 08-03 版"AI Release Tracker 记录、日期待官方确认"的说法（现官方已确认）。

### 1.2 DeepSeek-V4 基础条目（08-01 已收录）

- **DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence**（2026-04-24 预览 / 04-26 技术报告）：MoE + CSA；V4-Pro（1.6T 总参 / 49B 激活），V4-Flash（284B / 13B）；32T+ tokens；1M ctx；MIT 开源；V4-Pro-Max SWE-bench Verified 80.6%（开源最高）。arXiv:2606.19348。

---

## 2. OpenAI

### 2.1 GPT-5.6 System Card（已收录；今日核实传闻）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡 |
| **英文标题** | GPT-5.6 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 低配 / Luna 最快最省） |
| **发布日期** | 2026-07-09 |
| **核心创新** | Preparedness 框架下三模型均 Bio/Chem High + Cyber High；Sol bio/chem 评分 4（最高）；持续被各家闭源基准交叉引用 |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6 |

> ⚠️ 传闻（未确认，不写入正式条目）：WinCentral 2026-07-30 报道 **GPT-5.7**（内部代号可能为中间旗舰，8 月发布，新的 pretraining foundation，~10T 规模 tokens），并称 GPT-6 或推迟至 9 月。单源泄漏，待官方确认。

---

## 3. Meta

### 3.1 Muse Spark 1.1 & Muse Image（08-01 已收录，今日无新增）

| 项目 | 内容 |
|------|------|
| **中文标题** | Muse Spark Safety & Preparedness Report（+ Muse Spark 1.1 / Muse Image） |
| **英文标题** | Muse Spark Safety & Preparedness Report |
| **发布机构** | Meta Superintelligence Labs（Meta AI） |
| **模型系列** | Muse Spark → Muse Spark 1.1（2026-07-09 向开发者开放） |
| **核心创新** | 免费多模态消费级系列，标志 Llama 时代结束；Spark 1.1 面向 agent 的多模态推理（tool/computer use、coding gains），Meta Model API public preview；Muse Image 独立图像模型（07-07）；DeepSWE 1.1 评测 53.3%（对比集最高）；Chem/Bio 缓解前 high risk 已实施多层缓解 |
| **论文** | https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ |

> 今日核实：无 Llama 5 新消息；Muse 系列为当前主线。

---

## 4. Google DeepMind

### 4.1 Gemini 3.6 Flash Model Card（已收录，今日无新增）

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.6 Flash 模型卡 |
| **英文标题** | Gemini 3.6 Flash Model Card |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026-07-21 |
| **核心创新** | 基于 Gemini 3.5 Flash；原生多模态推理；workhorse / 广泛部署；知识截止 2026-03（部分领域 2025-01） |
| **论文** | https://deepmind.google/models/model-cards/gemini-3-6-flash/ |

> 今日无新报告；Gemini 3.5 Flash Model Card（2026-05-19）仍为上一代有效报告。

---

## 5. Anthropic

### 5.1 Claude Opus 5 System Card（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 系统卡 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 5（Opus 4.8 升级） |
| **发布日期** | System Card PDF: 2026-07-24 |
| **核心创新** | agentic coding、computer use、long-horizon knowledge work、math/science reasoning；effort dial 可调（$5/$25 每 M in/out，比 Fable 5 的 $10/$50 便宜）；SWE-bench Verified 96.0、SWE-bench Pro 79.2、Frontier-Bench v0.1 43.3（xhigh 下 44.4%）、ARC-AGI-3 30.2；定价与 Opus 4.8 一致 |
| **论文** | PDF: https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf |

### 5.2 Claude Sonnet 5 System Card（08-03 已收录，保留）

- **Claude Sonnet 5**（2026-06-30）：1M ctx / 128K 输出；最强大 Sonnet-class 但不推进能力前沿；MASK 诚实性说谎率 3.1%（对比集最低，vs Sonnet 4.6 的 13.3%、Opus 4.8 的 6.1%）；hallucination/sycophancy 显著改善；默认开启 cyber safeguards；价格 $2/$10 每 M tokens 至 8/31 后调至 $3/$15。PDF: https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf

### 5.3 Claude Fable 5 & Mythos 5（背景）

- **Claude Fable 5 & Mythos 5 System Card**（2026-06-09）：Fable 5 为闭源能力前沿（SWE-bench 95.5%）；Mythos Preview 244 页 Project Glasswing 系统卡；Anthropic 已接管 SpaceX 的 Colossus 集群（300MW / 22 万张 GPU）。

---

## 6. Mistral

### 6.1 Mistral Medium 3（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Medium 3 |
| **英文标题** | Mistral Medium 3 |
| **发布机构** | Mistral AI |
| **模型系列** | Medium 3（Medium 系列） |
| **发布日期** | 2026-08-02（约） |
| **上下文长度** | 128K |
| **核心创新** | coding / reasoning 侧重；定位 cost-optimized 与 frontier 之间的中档；la Plateforme + Azure AI Foundry（model id `mistral-medium-2505`） |
| **论文** | https://mistral.ai/news/ |

### 6.2 其他 Mistral 条目（保留）

- **Robostral Navigate**（2026-07-08）：具身导航模型，Mistral 向具身领域扩展。
- **Leanstral 1.5**（2026-07-02）：119B 总 / 6B 激活稀疏 MoE，Apache-2.0；miniF2F 100% 饱和；三阶段训练（mid-training → SFT → RL/CISPO）。
- **Mistral Medium 3.5 + OCR 4 上架 Microsoft Foundry**（2026-07-21，Microsoft–Mistral 合作）；**Mistral Large 3** 亦在 HuggingFace（675B）。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-Max（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max |
| **英文标题** | Qwen3.8-Max |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8（Max 旗舰） |
| **发布日期** | 2026-08-03（博客 qwen.ai/blog?id=qwen3.8） |
| **架构** | 2.4T 总参 / 95B 激活 Sparse MoE + hybrid attention |
| **上下文长度** | 1M |
| **核心创新** | 原生视觉多模态基础模型（native vision）；Text Arena #5、Vision Arena #2；权重"下周"开源（开源路线延续 3.5 系）；Available on Alibaba Cloud Model Studio + QwenWork；基于 Qwen 3.5 构建 |
| **论文** | https://qwen.ai/blog?id=qwen3.8 |

> 与 Kimi K3 同属 2T+ 级开源旗舰赛道；此前 K3 发布 3 天后 Alibaba 曾推出 Qwen3.8-Max-Preview 早期版本，本次为正式发布。

### 7.2 Qwen3.7-Flash / Qwen-Audio-3.0-ASR-Flash（08-03 已收录，保留）

- **Qwen3.7-Flash**（2026-07-25）：Flash 系列原生视觉语言升级，全面超越 Qwen3.6-Flash。
- **Qwen-Audio-3.0-ASR-Flash**（2026-07-30）：30 种语言 + 中文七大方言 ASR 家族；与 Qwen3.5-Omni（arXiv:2604.15804）构成音频技术栈。

---

## 8. Microsoft（Phi）

### 8.1 Phi-4-reasoning-vision-15B Technical Report（已收录，今日无新增）

- **Phi-4-reasoning-vision-15B**（2026-03，MSR-TR-2026-10）：数据质量为最大性能杠杆；高分辨率动态分辨率视觉编码器；单一模型双模式（推理/非推理 mode token）。https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/

> 今日核实：无 Phi-5 技术报告；Phi-4-reasoning-vision-15B 仍为最新。

---

## 9. Apple

### 9.1 AFM 3（08-03 已收录；今日补充 Siri Expressive Voices 技术细节）

| 项目 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple Foundation Models（AFM 3） |
| **英文标题** | Introducing the Third Generation of Apple's Foundation Models |
| **发布机构** | Apple（与 Google 合作定制） |
| **模型系列** | AFM 3 Core（3B 端侧）/ Core Advanced（20B 端侧稀疏，IFP 激活 1–4B）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像生成）/ AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU） |
| **发布日期** | 2026-06-08（WWDC26）；Siri Expressive Voices 技术博客 2026-07-28 |
| **核心创新** | IFP（Instruction-Following Pruning，全模型存 flash，每 prompt 加载 routed experts）+ 大量 always-active shared experts；AFM 3 Cloud Pro 首次把 PCC 扩展到 Google Cloud NVIDIA GPU（NVIDIA 机密计算 + Intel TDX + Google Titan，密钥归 Apple）；TTS MOS 4.15 vs 3.87（当前 TTS）、conversational 4.24 vs 3.82；dictation 偏好 44.7% vs 17.6%；技术报告预计 7 月节奏（现仅研究博客） |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

> 今日核实：截至 2026-08-04 仍无正式技术报告；2026-07-28 发布 Siri Expressive Voices（memory-efficient detokenizer + AFM 3 Core Advanced）为最新 ML 研究博客。

---

## 10. NVIDIA

### 10.1 Nemotron 3 Nano Technical Report（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Nano 30B-A3B 技术报告 |
| **英文标题** | NVIDIA Nemotron 3 Nano Technical Report |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 家族（Nano 30B/~3B 激活 · Super 120B/~12B · Ultra 550B/55B） |
| **发布日期** | 技术报告 PDF（Nemotron 3 Nano 30B-A3B） |
| **架构** | MoE 混合 Mamba-Transformer；30B 总 / 3B 激活（6/128 experts） |
| **训练数据** | 25T tokens 预训练（其中 3T+ 为 Nemotron 2 之上新增） |
| **上下文长度** | 1M |
| **核心创新** | agentic reasoning 侧重；吞吐最高达 GPT-OSS 20B / Qwen3-30B-A3B-Thinking-2507 的 ~3.3× |
| **论文** | PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf |

### 10.2 Nemotron 3 Ultra（08-03 已收录，保留）

- **Nemotron 3 Ultra**（2026-06）：550B/55B，108 层 / 512 experts（top-22）/ LatentMoE latent 2048；Mamba-2 + Attention 混合；NVFP4 预训练 ~20T；SFT → RLVR → MOPD；1M ctx；AA Intelligence Index ~48（美国开源最高）；吞吐最高 ~5.9×；OpenMDW-1.1 开源权重/数据/配方。PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf

---

## 11. xAI

### 11.1 Grok 4.5（已收录；今日核实 Grok 5 状态）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.5（SpaceXAI 旗舰） |
| **英文标题** | Introducing Grok 4.5 |
| **发布机构** | xAI（SpaceX 收购后改称 SpaceXAI；2026-06 收购 Cursor） |
| **发布日期** | 2026-07-08（发布）/ 07-16（官方博文）/ Model Card 07-14 |
| **上下文长度** | 500K；$2/$6 每 M tokens |
| **核心创新** | 与 Cursor 联合训练；数万张 NVIDIA GB300；DeepSWE 1.0 62.0%、SWE-bench Pro 64.7%、Terminal-Bench 2.1 83.3%、CursorBench v3.2 91.3%；AA #8/214；EU 初期不可用 |
| **论文** | https://x.ai/news/grok-4-5 ；Model Card PDF: https://media.x.ai/v1/website/card-7f81d41b.pdf |

> ⚠️ Grok 5（传闻 6T/10T MoE 变体）仍在 Colossus 2 上训练，预计 2026 Q3+，未发布（非正式条目）。Grok 4.5 ~1.5T 参数（社区报道）。

---

## 12. Amazon

### 12.1 Amazon Nova 2（08-03 已收录；今日核实技术报告日期）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **英文标题** | Amazon Nova 2: Multimodal Reasoning and Generation Models |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova 2.0 Lite / Pro / Omni / Sonic 2.0 |
| **发布日期** | 技术报告 2025-12-02；Bedrock 2025-12-01 |
| **核心创新** | Hybrid Reasoning（low/medium/high effort）；内置 web grounding + code interpreter + remote MCP；1M ctx；Lite 在前代旗舰 Nova Premier 之上 7× 更低成本 / 最高 5× 更快；agentic：Lite τ²-bench 76.0、Pro 92.7；Nova Multimodal Embeddings 统一多模态向量 |
| **论文** | PDF: https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf |

> 今日核实：技术报告正式出版日期为 **2025-12-02**（此前"2026"表述已更正）；FMSF 评估（Nova 2.0 Lite arXiv:2601.19134）确认 CBRN/Cyber/Auto-AI-R&D 均低于释放阈值。

---

## 13. ByteDance（字节跳动）

### 13.1 Seed2.1（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed2.1 正式发布 |
| **英文标题** | Seed2.1 Official Release |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed2.1 Pro / Turbo |
| **发布日期** | 2026-06-23 |
| **核心创新** | agent + coding E2E；GDPVal（agentic dev benchmark）；Seed2.1 Pro 在 dev crowdsource coding 上以 59.1% 击败 Claude Opus 4.6 |
| **论文** | https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity |

### 13.2 其他 Seed 条目（保留）

- **Seedream 5.0 Pro**：图像生成（理解 design）；**Seed2.0**；**Seed Full-Duplex Speech LLM**（+12% conversational fluency）；**Seed Audio 1.0**；**Seed3D 2.0**。
- **Seedance 2.5**（2026-07-31）：单次 30 秒视频 + 多轮延长；统一多模态音视频联合生成。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5.2（已收录；今日核实 GLM-5.5 传闻）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.2：稀疏注意力 + IndexShare |
| **英文标题** | GLM-5.2 |
| **发布机构** | Zhipu AI（智谱） |
| **模型系列** | GLM-5.2（MoE，~753B 量级） |
| **发布日期** | 2026-06-13 |
| **核心创新** | MIT 开放权重；1M ctx；Terminal-Bench 2.1 81.0；稀疏注意力 + IndexShare（每 4 层一次注意力索引器）+ MoE 路由；无原生视觉 |
| **论文** | https://zhipu-ai.cn/glm-5.2 |

> ⚠️ GLM-5.5 截至 2026-08-03 未发布：JPMorgan 研报（Reuters/CGTN 转载）称可能 2026-08 发布，1T+ 参数、1M ctx。单源传闻，未写入正式条目；GLM-5.2 仍为当前确认旗舰。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3（已收录；今日核实权重与报告状态）

- **Kimi K3**（API 2026-07-16；全量权重 + 47 页技术报告 2026-07-27）：2.8T 总参 / 104B 激活；93 层 = 69 KDA + 24 Gated MLA；896 experts（16 selected + 2 shared）；AttnRes；MoonViT-V2；MXFP4/8 量化感知训练；1M ctx；首个开源 3T 级模型；~2.5× scaling efficiency vs K2；权重 ~594GB MXFP4；WebDev Arena #1（1,678 Elo，超 Fable 5）；Kimi K3 License（非 OSI 开源）。https://kimi.ai/k3-technical-report

### 15.2 MoonEP / FlashKDA 开源（保留）

- **MoonEP**（2026-07-29）：完美负载均衡 Expert Parallelism 库；**FlashKDA**：KDA kernels CUTLASS 实现，prefill 1.72–2.22× speedup（H20）；配合 K3 全链路（attention kernels、MoE 通信库、agent infra）开源。

---

## 16. InternLM（上海 AI 实验室）

### 16.1 Intern-S1-Pro（已收录；今日新发现 Intern-S2 集合）

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿参数科学多模态模型 |
| **英文标题** | Intern-S1-Pro |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | Intern-S1-Pro（1T 总参 MoE，512 experts，激活 8 experts / 22B） |
| **发布日期** | 2026-02-04 |
| **核心创新** | SAGE"通专融合"架构；Fourier 位置编码 + 时间编码器；AI4S 2.0；奥赛金牌级数学/物理推理 |
| **论文** | https://intern.shai-lab.cn/intern-s1-pro ；arXiv:2603.25040 |

> 🔍 新发现（single-source，待核实）：Intern-S1 仓库 README 已出现 **Intern-S2 Model Collections**（HuggingFace），提示 Intern-S2 已在发布或预发布阶段——下一轮重点核实。

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4（已收录，保留）

- **Baichuan-M4**（2026-06-22，与清华合作）：临床级医疗 Agent 系统；Baichuan-Harness 统一运行时（长期患者记忆 + 多智能体协调）；hallucination 3.3%；支持问诊、随访、慢病管理、多模态影像。arXiv:2606.08982（⚠️ 更正：非 2606.12721）。
- **Baichuan-M3**（2026-01 / 02-09 全面开放）：235B；HealthBench 65.1；hallucination 3.5%；arXiv:2602.06570。

> 今日核实：无 2026 年 8 月新报告；公司战略全面转向医疗垂直领域。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3.7 / 3.5 Flash（已收录，保留）

- **Step 3.7 Flash**：多模态 reasoning，256K ctx，low/medium/high 三级 reasoning level。
- **Step 3.5 Flash**（2026-01-31，Apache-2.0）：196B 总 / 11B 激活稀疏 MoE；3-way MTP；SWE-bench Verified 74.4%；256K。
- **Step Image Edit 2**（<6B）：text-to-image + 编辑；**Step TTS Mini**（19 voices）。
- **Step3-Sys Technical Report**：GitHub 仓库发布系统级技术报告 PDF。https://github.com/stepfun-ai/Step3

---

## 19. Yi / 01.AI

### 19.1 Yi-Lightning（已收录；今日核实 2026 仍无新模型）

- **Yi-Lightning**（2024-10-16）：01.AI 旗舰 MoE，Chatbot Arena #6；$0.14/M tokens；技术报告 arXiv:2412.01253。

> 今日核实：2026 无新旗舰或新技术报告，repo 冻结于 Yi-1.5 / Yi-9B-200K；Yi-Lightning 仍为最新旗舰。

---

## 20. MiniMax（新增公司条目）

### 20.1 MiniMax H3（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | MiniMax H3：全模态生成模型 |
| **英文标题** | MiniMax H3 |
| **发布机构** | MiniMax |
| **模型系列** | H3（H 系列 omni-modal） |
| **发布日期** | 2026-07-31 |
| **核心创新** | 文本/图像/视频/音频统一全模态生成（omni-modal generation）；原生 dual-channel audio-visual 输出；最高 15s 2K 视频；技术：Contextual Omni Representation、H3-VAE、H3-Omni Transformer、In-context Regeneration；同类每秒成本最低；open weights 计划中 |
| **论文** | https://www.minimaxi.com/blog/minimax-h3 |

> 背景：MiniMax M2.1（2025-12-23）：Rust/Java/Go/C++ 改进、interleaved thinking、miniMax Agent。

---

## 交叉观察

- **8 月初密集发布期**：Qwen3.8-Max（08-03）、Mistral Medium 3（08-02）、Claude Opus 5 System Card（07-24）与 DeepSeek-V4-Flash-0731、MiniMax H3（07-31）连续落地——闭源旗舰与开源旗舰并行放量。
- **开源 2T+ 级旗舰两强格局**：Kimi K3（2.8T）与 Qwen3.8-Max（2.4T / 95B 激活）正面交锋，均承诺开源权重；NVIDIA Nemotron 3（Nano 25T tokens 预训练 + Ultra OpenMDW-1.1）与美国本土开源叙事持续强化。
- **Anthropic 分层定价与 effort dial 趋同**：Opus 5（$5/$25）< Fable 5（$10/$50）；配合 Sonnet 5 的限时低价——与 OpenAI/Gemini/Grok/Amazon 的 effort 控制全面趋同。
- **Agentic 基准仍是发布主战场**：Claude Opus 5（SWE-bench Pro 79.2、Frontier-Bench v0.1 43.3）、DeepSeek-V4-Flash-0731（9 项 agent benchmark 全超 V4-Pro-Preview）均以 agent/coding 为头条。
- **多模态全模态化**：MiniMax H3（四模态统一生成）与 Qwen3.8-Max（native vision）、Seed2.1（agent E2E）共同代表"单模型全模态"路线加速。
- **安全报告标配化继续**：Claude Opus 5 System Card、GPT-5.6（Bio/Chem/Cyber High）、Nova 2.0 Lite FMSF 评估——System Card 已成为闭源旗舰发布的标准交付物。
- **传闻需谨慎**：GPT-5.7（8 月）、GLM-5.5（8 月，1T+）、Grok 5（Q3，Colossus 2）均为单源/社区报道，未确认不写入正式条目。
