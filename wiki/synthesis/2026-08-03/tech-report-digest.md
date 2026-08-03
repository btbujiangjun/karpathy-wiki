---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-03
updated: 2026-08-03
sources: [tech-report-digest-2026-08-01.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-03（每日更新；今日重点核实：Amazon Nova 2、Anthropic Claude Sonnet 5、Apple AFM 3、NVIDIA Nemotron 3 Ultra、xAI Grok 4.5 发布细节、Qwen3.7-Flash、Mistral Robostral Navigate、Baichuan-M4、InternLM/Yi 2026 状态）

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4（已于 08-01 收录，补充刷新信息）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：迈向高效百万 token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V4-Pro / V4-Flash / V4-Pro-Max / V4-Flash-Max |
| **发布日期** | 2026-04-24（预览）/ 2026-04-26（技术报告） |
| **架构** | MoE + CSA（Compressed Sparse Attention）；V4-Pro（1.6T 总参，49B 激活）；V4-Flash（284B 总参，13B 激活） |
| **训练数据** | 32T+ tokens |
| **上下文长度** | 1M（默认），384K 最大输出 |
| **核心创新** | CSA（token 级压缩 + DSA，KV 压缩 4:1）稀疏注意力；thinking / non-thinking 双模式；MIT 开源；V4-Pro-Max SWE-bench Verified 80.6%（开源最高）、GPQA Diamond 90.1（官方自报） |
| **论文** | https://arxiv.org/abs/2606.19348 |

> 补充：2026-07-31 发布 **DeepSeek-V4-Flash-0731** 刷新版本（AI Release Tracker 记录），延续 V4-Flash 序列快速迭代节奏（single-source，日期待官方确认）。

---

## 2. OpenAI

### 2.1 GPT-5.6 System Card（已于 07-31/08-01 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡 |
| **英文标题** | GPT-5.6 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 低配 / Luna 最快最省） |
| **发布日期** | 2026-07-09 |
| **核心创新** | 三模型家族：Sol（旗舰）/ Terra（低配）/ Luna（最快最省）；Preparedness：Bio/Chem High、Cyber High、Self-Improvement below High；Sol bio/chem 评分 4 最高 |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6 |

> 今日无新报告；GPT-5.6 Sol 持续作为闭源基准被各家交叉引用（如 Grok 4.5 Terminal-Bench 对比中 91.9% 为最高已核实行）。

---

## 3. Meta

### 3.1 Muse Spark 系列（08-01 已收录 Safety Report，今日补充产品线）

| 项目 | 内容 |
|------|------|
| **中文标题** | Muse Spark Safety & Preparedness Report（+ Muse Spark 1.1 / Muse Image） |
| **英文标题** | Muse Spark Safety & Preparedness Report |
| **发布机构** | Meta Superintelligence Labs（Meta AI） |
| **模型系列** | Muse Spark（Meta AI 底层模型）→ Muse Spark 1.1（2026-07-09 向开发者开放） |
| **发布日期** | Safety Report: 2026-05-26；Muse Spark 1.1: 2026-07-09；Muse Image: 2026-07-07 |
| **核心创新** | 免费多模态消费级模型系列，标志 Llama 时代结束、Muse 系列开启；Spark 1.1 在 DeepSWE 1.1 评测（Datacurve）中 53.3% 为对比集最高（vs Grok 4.5 的 53%）；Muse Image 为独立图像模型（07-07）；Chem/Bio 缓解前达 high risk 类别已实施多层缓解 |
| **论文** | https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ |

---

## 4. Google DeepMind

### 4.1 Gemini 3.6 Flash Model Card（已于 07-31/08-01 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.6 Flash 模型卡 |
| **英文标题** | Gemini 3.6 Flash Model Card |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026-07-21 |
| **核心创新** | Gemini 3 系列原生多模态推理；基于 Gemini 3.5 Flash，token 效率更高；知识截止 2026-03 |
| **论文** | https://deepmind.google/models/model-cards/gemini-3-6-flash/ |

> 今日无新报告；Gemini 3.5 Flash Model Card（2026-05-19，thinking levels 控制质量/成本/延迟）仍为上一代有效报告。

---

## 5. Anthropic

### 5.1 Claude Sonnet 5 System Card（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Sonnet 5 系统卡 |
| **英文标题** | System Card: Claude Sonnet 5 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Sonnet 5（Sonnet 4.6 升级） |
| **发布日期** | 2026-06-30 |
| **上下文长度** | 1M tokens / 128K 最大输出 |
| **核心创新** | 最强大 Sonnet-class 模型，但不推进能力前沿（低于 Opus/Mythos-class）；RSP 评估对齐风险极低但高于以往 Sonnet；hallucination/sycophancy 较 4.6"显著改善"；MASK 诚实性测试说谎率 3.1%（对比集中最低，vs Sonnet 4.6 的 13.3%、Opus 4.8 的 6.1%、Mythos 5 的 8.6%）；"wet blanket"（过度说教）轻微增加；默认开启 cyber safeguards（严于 Opus 类）；新 tokenizer 效率 +1.0~1.x%；价格 $2/$10 每 M tokens 至 8/31，后调至 $3/$15 |
| **论文** | PDF: https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf |

### 5.2 Claude Fable 5 & Claude Mythos 5 System Card（补充背景）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5 & Claude Mythos 5 系统卡 |
| **英文标题** | System Card: Claude Fable 5 & Claude Mythos 5 |
| **发布日期** | 2026-06-09 |
| **核心创新** | 与 Sonnet 5 同期的 244 页级系统卡（Mythos Preview 为 244 页 Project Glasswing）；Fable 5 为闭源能力前沿（SWE-bench 95.5%）；Anthropic 已接管 SpaceX 的 Colossus 集群（300MW/22 万张 GPU） |
| **论文** | PDF: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf |

---

## 6. Mistral

### 6.1 Robostral Navigate（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Robostral Navigate：具身导航模型 |
| **英文标题** | Robostral Navigate |
| **发布机构** | Mistral AI |
| **模型系列** | Robostral Navigate |
| **发布日期** | 2026-07-08 |
| **核心创新** | 面向具身智能的导航/行动模型（embodied navigation）；Mistral 从纯语言模型扩展至具身领域 |
| **论文** | https://mistral.ai/news/（Robostral Navigate 发布页） |

### 6.2 Leanstral 1.5（已于 08-01 收录）

- **Leanstral 1.5**（2026-07-02）：119B 总/6B 激活稀疏 MoE，Apache-2.0；面向 Lean 4 形式化验证：miniF2F 100%（饱和）、PutnamBench 587/672、FATE-H 87%；三阶段训练（mid-training → SFT → RL，RL 用 CISPO）。https://mistral.ai/news/leanstral-1-5/
- **Mistral OCR 4**（2026-06-23）：文档 OCR 迭代。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.7-Flash（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.7-Flash：原生视觉语言 Flash 模型 |
| **英文标题** | Qwen3.7-Flash |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.7-Flash（Flash 系列） |
| **发布日期** | 2026-07-25 |
| **核心创新** | Flash 系列原生视觉语言升级，全面超越 Qwen3.6-Flash；延续 Flash 系列高吞吐低成本定位 |
| **论文** | https://qwenlm.github.io/ |

### 7.2 Qwen-Audio-3.0-ASR-Flash（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen-Audio-3.0-ASR-Flash 模型家族 |
| **英文标题** | Qwen-Audio-3.0-ASR-Flash |
| **发布机构** | Alibaba Qwen |
| **发布日期** | 2026-07-30 |
| **核心创新** | ASR 模型家族，覆盖 30 种语言 + 中文七大方言支持；与 Qwen3.5-Omni（已于 07-31 收录，arXiv:2604.15804，100M+ 小时音视频数据，Hybrid Attention MoE）形成音频技术栈 |
| **论文** | https://huggingface.co/Qwen |

---

## 8. Microsoft（Phi）

### 8.1 Phi-4-reasoning-vision-15B Technical Report（已于 08-01 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-reasoning-vision-15B（15B 紧凑开源） |
| **发布日期** | 2026-03（MSR-TR-2026-10） |
| **核心创新** | 数据质量（系统过滤、纠错、合成增强）为最大性能杠杆；高分辨率动态分辨率视觉编码器；推理/非推理数据混合 + 显式 mode token，单一模型双模式 |
| **论文** | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

> 今日无新报告。

---

## 9. Apple

### 9.1 AFM 3：第三代 Apple Foundation Models（今日新增核实，取代 2025 AFM 条目）

| 项目 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple Foundation Models（AFM 3） |
| **英文标题** | Introducing the Third Generation of Apple's Foundation Models |
| **发布机构** | Apple（与 Google 合作定制） |
| **模型系列** | AFM 3 Core（3B 端侧）/ AFM 3 Core Advanced（20B 端侧稀疏）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像生成）/ AFM 3 Cloud Pro（PCC on Google Cloud） |
| **发布日期** | 2026-06-08（WWDC26） |
| **架构** | 五模型家族：Core=3B dense 端侧；Core Advanced=20B 稀疏、每 prompt 激活 1–4B（Instruction-Following Pruning / IFP，全模型存 flash）；Cloud=PCC 服务端；ADM 3 Cloud=扩散图像生成（Image Playground/Genmoji/Clean Up）；Cloud Pro=最强大，agentic 工具调用 + 复杂推理 |
| **核心创新** | 与 Google 联合定制（TPU 训练）；AFM 3 Cloud Pro 首次将 Private Cloud Compute 扩展到第三方数据中心（Google Cloud 内的 NVIDIA GPU，NVIDIA 机密计算 + Intel TDX + Google Titan 芯片，Apple 持签名密钥，五条 PCC 规则不变）；用户偏好：Core 45.6% vs 旧模型 23.3%，Cloud 64.7% vs 8.7%；技术报告预计按 2025 年节奏（7 月）发布（目前仅有研究博客） |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

---

## 10. NVIDIA

### 10.1 Nemotron 3 Ultra Technical Report（今日新增核实，家族旗舰）

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：面向 Agentic Reasoning 的开源高效 MoE 混合 Mamba-Transformer |
| **英文标题** | Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 家族（Nano 30B/~3B · Super 120B/~12B · **Ultra 550B/55B**） |
| **发布日期** | 2026-06（权重开源 2026-06；技术报告 PDF） |
| **架构** | 108 层 / d_model 8192 / 512 experts（top-22）/ LatentMoE latent 2048 / Mamba-2 + Attention 混合（Mamba-2 承担序列混合，稀疏 Attention 层保精确召回）/ 2 层共享权重 MTP 投机解码 |
| **训练数据** | 预训练 ~20T text tokens；NVFP4 预训练（最大规模稳定 NVFP4 训练，末 15% 网络 + Mamba/attention/MTP 层高精度）；后训练 SFT → RLVR → MOPD（Multi-teacher On-Policy Distillation，10+ 专用 teacher） |
| **上下文长度** | 1M tokens |
| **核心创新** | 面向长程自主 agentic 工作流的 inference-throughput-to-accuracy 前沿；AA Intelligence Index ~48（美国开源权重最高，vs gpt-oss-120b ~33、Super ~36）；吞吐最高 ~5.9× 于同档开源（vs GLM-5.1，8K/64K）；AA-Omniscience 非幻觉分 78.7（对比集最高）；OpenMDW-1.1 开源权重/数据/配方；W4A16 量化 5.03 BPE 单节点部署 |
| **论文** | PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf |

---

## 11. xAI

### 11.1 Grok 4.5 发布细节（08-01 已收录 Model Card，今日补充发布信息）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.5（SpaceXAI 旗舰） |
| **英文标题** | Introducing Grok 4.5 |
| **发布机构** | xAI（SpaceX 收购后改称 SpaceXAI；2026-06 收购 Cursor） |
| **发布日期** | 2026-07-08（发布）；2026-07-16（官方博文）；Model Card 2026-07-14 |
| **上下文长度** | 500K tokens；$2/$6 每 M tokens（>200K 上下文另计） |
| **核心创新** | 与 Cursor 联合训练（jointly trained），定位编码/agentic/知识工作而非通用推理旗舰；数万张 NVIDIA GB300 训练；DeepSWE 1.0 62.0%、SWE-bench Pro 64.7%、SWE-bench Multilingual 78.0%、Terminal-Bench 2.1 83.3%（仅次 Fable 5）、CursorBench v3.2 91.3%；AA 独立榜 #8/214；推理 effort low/medium/high（默认 high）；EU 发布初期不可用；Grok 5 传闻在 Colossus 2 上训练 |
| **论文** | https://x.ai/news/grok-4-5 ；Model Card PDF: https://media.x.ai/v1/website/card-7f81d41b.pdf |

> 家族背景：Grok 4.20（2026-03，2M ctx 多智能体）、Grok 4.3（2026-04，1M ctx，原生视频输入）、Grok 4.5（2026-07，500K ctx）。

---

## 12. Amazon

### 12.1 Amazon Nova 2（今日新增核实，更新 08-01"无 2026 新报告"结论）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **英文标题** | Amazon Nova 2: Multimodal Reasoning and Generation Models |
| **发布机构** | Amazon AGI（Amazon Artificial General Intelligence） |
| **模型系列** | Nova 2.0 Omni / Lite / Pro / Sonic 2.0 |
| **发布日期** | 2026（Nova 2 技术报告；Bedrock 发布，Sonic 2.0 刷新至 2026-05） |
| **核心创新** | Hybrid Reasoning：Lite/Pro 提供 low/medium/high reasoning effort 可配置速度-智能权衡；Nova 2 Lite 在前代旗舰 Nova Premier 之上提升多步问题求解与 agentic 工作流（7× 更低成本、最高 5× 更快）；内置工具 web grounding + code interpreter；agentic 评测：Nova 2 Lite τ²-bench 76.0、Nova 2 Pro 92.7（超 GPT-5.1/Gemini 3 Pro Preview 等闭源）；Nova 2 Omni 多模态理解+生成（图像生成胜率 86.9 物理场景等类别）；长上下文 OpenAI-MRCR（8-needle）；视觉/文档/音视频理解 |
| **论文** | PDF: https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf |

> ⚠️ 修正：08-01 版记录"Amazon 无 2026 新报告"，实际 Amazon Nova 2 技术报告（2026）已发布，本轮更正。2024/2025 原始 Nova 家族报告（arXiv:2504.13186）与 Nova Premier addendum（2025-04-30）仍在。

---

## 13. ByteDance（字节跳动）

### 13.1 Seedance 2.5（已于 08-01 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Seedance 2.5 正式发布 |
| **英文标题** | Seedance 2.5 |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seedance 2.5（视频生成） |
| **发布日期** | 2026-07-31 |
| **核心创新** | 单次 30 秒生成 + 多轮延长；参考输入最多 30 图 + 10 视频 + 10 音频；统一多模态音视频联合生成架构；时间戳级编辑、绿幕/黏土渲染参考；10+ 语言 |
| **论文** | https://seed.bytedance.com/zh/blog/一键成片-随心参考-seedance-2-5-正式发布 |

> 今日无新报告；Doubao-Seed-2.0（2026-02-14）为对话/多模态系列基线。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5.2（已于 08-01 收录，当前旗舰）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.2：稀疏注意力 + IndexShare |
| **英文标题** | GLM-5.2 |
| **发布机构** | Zhipu AI（智谱） |
| **模型系列** | GLM-5.2（MoE，总量 753B 量级） |
| **发布日期** | 2026-06-13 |
| **核心创新** | MIT 开放权重；1M 上下文；Terminal-Bench 2.1 81.0；稀疏注意力 + IndexShare（每 4 层一次注意力索引器）+ MoE 路由；无原生视觉（视觉在 GLM-V 产品线） |
| **论文** | https://zhipu-ai.cn/glm-5.2 |

> GLM-5.3 截至今日仍未正式发布，仅社区传言（可能跳过直接发布 GLM-5.5，预计 2026-08，可能 >1T 参数）。不写入正式条目。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3（已于 08-01 收录全量技术细节）

- **Kimi K3**（API 2026-07-16；全量权重 + 47 页技术报告 2026-07-27）：2.8T 总参 / 104B 激活；93 层 = 69 KDA + 24 Gated MLA；896 experts（16 selected + 2 shared）；AttnRes；MoonViT-V2；MXFP4/8 量化感知训练；1M 上下文；首个开源 3T 级模型；~2.5× scaling efficiency vs K2。https://kimi.ai/k3-technical-report

### 15.2 MoonEP 开源（今日补充）

| 项目 | 内容 |
|------|------|
| **中文标题** | MoonEP：专家并行库 |
| **英文标题** | Moonshot AI Open-Sources MoonEP |
| **发布日期** | 2026-07-29 |
| **核心创新** | 完美负载均衡的 Expert Parallelism 库，面向 MoE 训练；配合 K3 开源链路（attention kernels、MoE 通信库、agent infra 一并开源），形成 MoE 训练全栈 |
| **论文** | https://github.com/MoonshotAI/Kimi-K3 |

---

## 16. InternLM（上海 AI 实验室）

### 16.1 Intern-S1-Pro（已于 08-01 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿参数科学多模态模型 |
| **英文标题** | Intern-S1-Pro |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | Intern-S1-Pro（1T 总参 MoE，512 experts，激活 8 experts / 22B） |
| **发布日期** | 2026-02-04 |
| **核心创新** | SAGE "通专融合" 架构；Fourier 位置编码 + 时间编码器；AI4S 2.0；奥赛金牌级数学/物理推理 |
| **论文** | https://intern.shai-lab.cn/intern-s1-pro |

> 今日核实：截至 2026-08-03 无新技术报告（8/1 后无更新）；InternVL3.5（2025-08，arXiv:2508.18265）为多模态开源系列最新报告，但非 2026 新报告。

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4（08-01 已收录，今日补充细节 + 更正 arXiv ID）

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4：临床级医疗 Agent 系统 |
| **英文标题** | Baichuan-M4 |
| **发布机构** | Baichuan AI（百川智能），与清华大学团队合作 |
| **发布日期** | 2026-06-22 |
| **核心创新** | 面向持续照护的临床级医疗 agent 系统；Baichuan-Harness 统一运行时（长期患者记忆 + 多智能体协调）；hallucination 率降至 3.3%；支持问诊、随访、慢病管理、多模态影像理解；公司战略全面转向医疗垂直领域（2025-03 解散金融/教育 B2B 团队） |
| **论文** | arXiv:2606.08982 |

> ⚠️ 修正：08-01 版记录 Baichuan-M4 为 arXiv:2606.12721，经核实为 **arXiv:2606.08982**（single-source，官方 arXiv 列表）。

### 17.2 Baichuan-M3（补充背景）

- **Baichuan-M3**（2026-01 发布 / 02-09 正式全面开放）：235B 参数；HealthBench 65.1、ScanBench 临床问诊 74.9；hallucination 3.5%；面向临床决策支持（问诊→检验→诊断工作流）而非 trivia QA；arXiv:2602.06570。M3 Plus 2026-01-22。创始人王小川：IPO 目标 ~2027。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3.5 Flash（已于 08-01 收录）

- **Step 3.5 Flash**（2026-01-31，Apache-2.0）：196B 总 / 11B 激活稀疏 MoE；3-way MTP；100–300 tok/s；SWE-bench Verified 74.4%；256K 上下文。

### 18.2 Step3 系统技术报告（今日补充核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step3 系统技术报告 |
| **英文标题** | Step3-Sys Technical Report |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step3（多模态基础模型） |
| **核心创新** | GitHub 仓库发布 Step3-Sys-Tech-Report.pdf（Step3 系统级技术报告）；Step3 为多模态模型（InternVL3.5 论文曾引 Step-3 作为开源 MLLM 对比） |
| **论文** | https://github.com/stepfun-ai/Step3 |

---

## 19. Yi / 01.AI

### 19.1 Yi-Lightning（已于 07-31 收录；今日核实 2026 无新模型）

- **Yi-Lightning**（2024-10-16）：01.AI 旗舰 MoE，Chatbot Arena #6；$0.14/M tokens；开源基础层（Yi-34B/Yi-6B/Yi-Coder）+ 闭源旗舰（Yi-Large/Yi-Lightning）。技术报告 arXiv:2412.01253。

> 今日核实：01.AI 2025-2026 发布节奏明显放缓（相对 DeepSeek/Qwen/GLM/Kimi），2026 无新旗舰或新技术报告，Yi-Lightning 仍为最新旗舰。

---

## 交叉观察

- **Amazon Nova 2 补齐闭源混合推理叙事**：Nova 2 Lite/Pro 的 low/medium/high reasoning effort 与 OpenAI/Gemini/Grok 的 effort 控制趋同；"Hybrid Reasoning + 内置工具（web grounding/code interpreter）"成为 2026 闭源模型标配。今日修正了 08-01"Amazon 无 2026 报告"的误判。
- **美国开源权重旗舰之争成型**：NVIDIA Nemotron 3 Ultra（550B/55B，OpenMDW-1.1，AA Index ~48）正面挑战 DeepSeek-V4 / GLM-5.2 / Kimi K3 的开源领先地位——这是美国实验室本轮最强的开源权重发布。
- **端侧 + 云端计算边界被重画**：Apple AFM 3 用 Instruction-Following Pruning 把 20B 稀疏模型塞进手机，同时把 Private Cloud Compute 首次开到 Google Cloud 的 NVIDIA GPU 上——"谁的硬件 + 谁的密钥"成为隐私叙事核心。
- **Mamba-Attention 混合 + 投机解码成高效长上下文标配**：Nemotron 3 Ultra（Mamba-2 + Attention + MTP）与 DeepSeek CSA、GLM IndexShare 并列，验证混合序列模型路线。
- **Agentic 基准（DeepSWE/SWE-bench Pro/Terminal-Bench 2.1/CursorBench）取代通用榜成为发布主战场**：Grok 4.5、Claude Sonnet 5、Nemotron 3 Ultra 的发布页全部以这些为头条。
- **中国医疗垂直模型崛起**：Baichuan-M3/M4（hallucination 3.5%→3.3%）在临床决策支持上对标 GPT-5.2 级通用模型，代表"通用模型→受监管垂直领域"的差异化路径。
- **开源生态基建同步开源**：Moonshot 开源 MoonEP（专家并行）+ K3 全链路，NVIDIA 开源训练数据/配方，Kimi K3 / GLM-5.2 / Nemotron 3 Ultra 均可复现训练。
