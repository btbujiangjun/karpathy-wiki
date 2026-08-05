---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-02
updated: 2026-08-02
sources: [tech-report-digest-2026-08-01.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-02（每日更新；今日重点核实：Anthropic Claude Opus 5 System Card、NVIDIA Nemotron 3 Ultra、xAI Grok 4.5 Model Card、Amazon Nova 2、Zhipu GLM-5、Moonshot Kimi K3、Baichuan-M4、StepFun Step 3.5 Flash、InternLM Intern-S1-Pro、Apple AFM 3）

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4（已于 07-31/08-01 收录，今日核实无更新）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：迈向高效百万 token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V4-Pro / V4-Flash / V4-Pro-Max / V4-Flash-Max |
| **发布日期** | 2026-04-24（预览）/ 2026-04-26（技术报告） |
| **架构** | MoE + CSA（Compressed Sparse Attention）+ HCA；mHC；Muon；V4-Pro（1.6T 总参，49B 激活）；V4-Flash（284B 总参，13B 激活） |
| **训练数据** | 32T+ tokens |
| **上下文长度** | 1M（默认），384K 最大输出 |
| **核心创新** | CSA（token 级压缩 + DSA，KV 压缩 4:1）稀疏注意力；thinking / non-thinking 双模式；MIT 开源；V4-Pro-Max SWE-bench Verified 80.6%（开源最高，llm-stats 2026-06）、GPQA Diamond 90.1（官方自报） |
| **论文** | https://arxiv.org/abs/2606.19348 |

> 今日核实：确认技术报告（arXiv:2606.19348）无更新版本，未发现 V4.1 或新的 V4 系列 flash 版官方报告。

---

## 2. OpenAI

### 2.1 GPT-5.6 System Card（已于 07-31/08-01 收录，今日核实无更新）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡 |
| **英文标题** | GPT-5.6 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 低配 / Luna 最快最省） |
| **发布日期** | 2026-07-09 |
| **核心创新** | 三模型家族：Sol（旗舰）/ Terra（低配）/ Luna（最快最省）；Preparedness：Bio/Chem High、Cyber High、Self-Improvement below High；Sol bio/chem 评分 4 最高 |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6 |

> 今日核实：2026-07-09 卡片无更新。

---

## 3. Meta

### 3.1 Muse Spark Safety & Preparedness Report（已于 08-01 收录，今日核实无新增）

| 项目 | 内容 |
|------|------|
| **中文标题** | Muse Spark 安全与准备度报告 |
| **英文标题** | Muse Spark Safety & Preparedness Report |
| **发布机构** | Meta Superintelligence Labs（Meta AI） |
| **模型系列** | Muse Spark（Meta AI 底层模型） |
| **发布日期** | 2026-05-26 |
| **核心创新** | 在 Advanced AI Scaling Framework 下评估；Chem/Bio 缓解前达 "high risk" 类别，已实施多层级缓解；危险化学/生物工作流拒绝率达到 SOTA；低欺骗率、同行中最低 cyber-misuse 合规率；部分行为维度仍待改进 |
| **论文** | https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ |

> 今日核实：无 2026 新模型卡/报告（仅旧 Llama 3 模型卡，非 2026 发布）。

---

## 4. Google DeepMind

### 4.1 Gemini 3.6 Flash Model Card（已于 07-31/08-01 收录，今日核实无新增）

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.6 Flash 模型卡 |
| **英文标题** | Gemini 3.6 Flash Model Card |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026-07-21 |
| **核心创新** | Gemini 3 系列原生多模态推理；基于 Gemini 3.5 Flash，token 效率更高；知识截止 2026-03 |
| **论文** | https://deepmind.google/models/model-cards/gemini-3-6-flash/ |

> 今日核实：无新报告。

---

## 5. Anthropic

### 5.1 Claude Opus 5 System Card（今日核实确认）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 系统卡 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 5（Opus 4.8 升级） |
| **发布日期** | 2026-07-24 |
| **核心创新** | Agentic coding / computer use / long-horizon knowledge work / 数学科学推理均有提升；系统卡片 + 风险报告并存；定价 $5/$25 每 M tokens；API 名 `claude-opus-5` |
| **论文** | PDF: https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf |

> 今日核实：确认 2026-07-24 发布；与 GPT-5.6 / Grok 4.5 / Muse Spark 同列，安全/准备度报告已成发布标配。

---

## 6. Mistral

### 6.1 Leanstral 1.5（已于 08-01 收录，今日核实无新 LLM 报告）

| 项目 | 内容 |
|------|------|
| **中文标题** | Leanstral 1.5：形式化验证模型 |
| **英文标题** | Leanstral 1.5 |
| **发布机构** | Mistral AI |
| **模型系列** | Leanstral 1.5（119B 总参 / 6B 激活） |
| **发布日期** | 2026-07-02 |
| **架构** | 稀疏 MoE；Apache-2.0 开源 |
| **核心创新** | 面向 Lean 4 形式化验证：miniF2F 100%（饱和）、PutnamBench 587/672、FATE-H 87%、FATE-X 34%；三阶段训练（mid-training → SFT → RL，RL 用 CISPO）；在 57 个开源仓库中发现 5 个此前未知的 bug |
| **论文** | https://mistral.ai/news/leanstral-1-5/ |

> 今日核实：未找到新的 LLM 技术报告（唯一新报告为 Voxtral TTS，音频/语音模型，不收录进主 digest）。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.5-Omni（已于 07-31 收录，今日核实无新 LLM 报告）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba Qwen |
| **发布日期** | 2026-04 |
| **核心创新** | 千亿级参数、256K 上下文；100M+ 小时音视频数据；Thinker/Talker 均用 Hybrid Attention MoE；Qwen3.5-Omni-Plus 215 项 SOTA、超 Gemini-3.1 Pro 关键音频项；10 语言 + 零样本音色定制 |
| **论文** | https://arxiv.org/abs/2604.15804 |

> 今日核实：无主要 LLM 新报告（Qwen3.8-Max 仅有产品页、无技术报告；Qwen-Audio-3.0-TTS 为音频报告 arXiv:2607.23938，不收录进主 digest）。

---

## 8. Microsoft（Phi）

### 8.1 Phi-4-reasoning-vision-15B Technical Report（已于 08-01 收录，今日核实无更新）

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-reasoning-vision-15B（15B 紧凑开源） |
| **发布日期** | 2026-03-04（MSR-TR-2026-10） |
| **核心创新** | 数据质量（系统过滤、纠错、合成增强）为最大性能杠杆；高分辨率动态分辨率视觉编码器；推理/非推理数据混合 + 显式 mode token，单一模型双模式 |
| **论文** | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

> 今日核实：无新报告。

---

## 9. Apple

### 9.1 AFM 3：第三代 Apple Foundation Models（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple Foundation Models（AFM 3） |
| **英文标题** | Introducing the Third Generation of Apple's Foundation Models |
| **发布机构** | Apple（与 Google 合作定制） |
| **模型系列** | AFM 3 Core（3B 本地）/ AFM 3 Core Advanced（20B 稀疏，激活 1–4B，多模态）/ AFM 3 Cloud / ADM 3 Cloud（图像生成/编辑）/ AFM 3 Cloud Pro（推理/Agentic，跑在 Private Cloud Compute 上） |
| **发布日期** | 2026-06-08 |
| **核心创新** | 五模型家族（与 Google 合作）；端侧（3B Core + 20B 稀疏 Core Advanced）+ 云端（Cloud / Cloud Pro）+ 图像生成（ADM 3 Cloud）分层；Cloud Pro 面向复杂推理与 Agentic 任务 |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

> 补充背景：Apple Intelligence Foundation Language Models Tech Report 2025（2025-07-17，端侧 ~3B + 服务端 PT-MoE on Private Cloud Compute，arXiv:2507.19038）仍为 2025 基线报告。

---

## 10. NVIDIA

### 10.1 Nemotron 3 Ultra Technical Report（今日新增核实，家族旗舰）

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra 技术报告 |
| **英文标题** | NVIDIA Nemotron 3 Ultra Technical Report |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Ultra（550B 总参 / 55B 激活） |
| **发布日期** | 2026-06-09 |
| **架构** | MoE Hybrid Mamba-Attention；LatentMoE |
| **训练数据** | 20T tokens 预训练（NVFP4 预训练） |
| **上下文长度** | 1M tokens |
| **核心创新** | 面向 Agentic Reasoning 的开源高效旗舰；MTP 投机解码；多环境 RLVR + MOPD 后训练；推理预算控制；吞吐约 6× 提升（vs 同档开源）；权重开源 |
| **论文** | PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf |

### 10.2 Nemotron 3 Super Technical Report（已于 07-31 收录）

- **Nemotron 3 Super**（2026-04-03）：120B 总 / 12B 激活；Mamba-Attention 混合 MoE；NVFP4 预训练、LatentMoE、MTP；25T tokens；1M 上下文；吞吐 2.2× vs GPT-OSS-120B、7.5× vs Qwen3.5-122B；HF 开源。PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf

---

## 11. xAI

### 11.1 Grok 4.5 Model Card（今日核实确认）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.5 模型卡 |
| **英文标题** | Grok 4.5 Model Card |
| **发布机构** | xAI（SpaceXAI 品牌；与 Cursor 合作） |
| **发布日期** | 2026-07-14 |
| **核心创新** | Agentic + 推理高效：多数任务的推理步骤数为其他前沿模型的一半；与 SpaceXAI / Cursor* 合作发布；安全/防护域：网络、生物知识、生物 Agentic、反越狱、尽力输出安全（含视觉与 CBRN 拒答）、心理健康、行为 |
| **论文** | PDF: https://media.x.ai/v1/website/card-7f81d41b.pdf |

---

## 12. Amazon

### 12.1 Amazon Nova 2（今日新增核实，更正 08-01"无 2026 新报告"结论）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2：多模态推理与生成模型 |
| **英文标题** | Amazon Nova 2 |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova 2 Lite / Pro / Omni / Sonic |
| **发布日期** | 2026（Amazon AGI 技术报告） |
| **上下文长度** | 全系 1M tokens |
| **核心创新** | Nova 2 Lite / Pro 带 "extended thinking" 可配置推理；Nova 2 Omni：文本+图像+视频+音频输入 / 文本+图像输出；Nova 2 Sonic：语音到语音；全系 1M 上下文 |
| **论文** | PDF: https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf |

> ⚠️ 修正：08-01 版记录"Amazon 无 2026 新报告"，实际 Amazon Nova 2 技术报告已发布，本轮更正。2024/2025 原始 Nova 家族报告（arXiv:2504.13186）仍为背景。

---

## 13. ByteDance（字节跳动）

### 13.1 Seedance 2.5（已于 08-01 收录，今日核实无新增）

| 项目 | 内容 |
|------|------|
| **中文标题** | Seedance 2.5 正式发布 |
| **英文标题** | Seedance 2.5 |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seedance 2.5（视频生成） |
| **发布日期** | 2026-07-31 |
| **核心创新** | 单次 30 秒生成 + 多轮延长；参考输入最多 30 图 + 10 视频 + 10 音频；统一多模态音视频联合生成架构；时间戳级编辑、绿幕/黏土渲染参考；10+ 语言 |
| **论文** | https://seed.bytedance.com/zh/blog/一键成片-随心参考-seedance-2-5-正式发布 |

> 今日核实：无新增报告。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5（今日新增核实，2026-02 基础报告）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：稀疏注意力 + DSA |
| **英文标题** | GLM-5 |
| **发布机构** | Zhipu AI（智谱），与清华大学合作 |
| **模型系列** | GLM-5（GLM 系列基础版） |
| **发布日期** | 2026-02-17 |
| **核心创新** | DSA 降低训练/推理成本；异步 RL 基础设施 + 异步 agent RL；在常见开源基准上 SOTA；强调端到端真实软件工程 |
| **论文** | https://arxiv.org/abs/2602.15763 |

### 14.2 GLM-5.2（已于 08-01 收录，当前旗舰）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.2：稀疏注意力 + IndexShare |
| **英文标题** | GLM-5.2 |
| **发布机构** | Zhipu AI（智谱） |
| **模型系列** | GLM-5.2（MoE，总量 753B 量级） |
| **发布日期** | 2026-06-13 |
| **核心创新** | MIT 开放权重；1M 上下文；Terminal-Bench 2.1 81.0（vs Claude Opus 4.8 的 85.0）；稀疏注意力 + IndexShare（每 4 层一次注意力索引器）+ MoE 路由；无原生视觉（视觉在 GLM-V 产品线） |
| **论文** | https://zhipu-ai.cn/glm-5.2 |

> GLM-5.3 截至今日仍未正式发布，仅社区传言（可能跳过 5.3/5.4 直接发布 GLM-5.5，预计 2026-08，可能 >1T 参数）。不写入正式条目。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3（已于 08-01 收录全量技术细节，今日补充 arXiv）

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K3 技术报告 |
| **英文标题** | Kimi K3 Technical Report |
| **发布机构** | Moonshot AI（月之暗面） |
| **模型系列** | Kimi K3（2.8T 总参 MoE，104B 激活） |
| **发布日期** | 2026-07-16（API）/ 2026-07-27（全量权重 + 47 页技术报告） |
| **架构** | 93 层：69 层 KDA + 24 层 Gated MLA；896 experts（16 selected/token + 2 shared）；KDA（Kimi Delta Attention，固定大小 recurrent state）；AttnRes（Attention Residuals）；SiTU-GLU；MoonViT-V2 视觉编码器（401M） |
| **量化** | MXFP4 / MXFP8 量化感知训练 |
| **上下文长度** | 1,048,576（1M） |
| **核心创新** | 首个开源 3T 级模型；原生多模态（text/image/video）；Kimi K3 License（带 caveat）；vLLM/SGLang/TokenSpeed 支持；118 tok/s on 16×GB300（无投机解码），370 tok/s with DSpark draft（3.14×）；~2.5× scaling efficiency vs K2 |
| **论文** | https://kimi.ai/k3-technical-report ；arXiv:2607.24653 |

---

## 16. InternLM（上海 AI 实验室）

### 16.1 Intern-S1-Pro（已于 08-01 收录，今日核实无新报告）

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿参数科学多模态模型 |
| **英文标题** | Intern-S1-Pro |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | Intern-S1-Pro（1T 总参 MoE，512 experts，激活 8 experts / 22B） |
| **发布日期** | 2026-02-04 |
| **核心创新** | SAGE "通专融合" 架构；Fourier 位置编码 + 时间编码器；AI4S 2.0；奥赛金牌级数学/物理推理；跨化学/材料/生命科学/地球科学等 AI4Science 领域领先 |
| **论文** | https://intern.shai-lab.cn/intern-s1-pro |

> 今日核实：无 2026 新技术报告。

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4（今日补充细节 + 更正 arXiv ID）

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4：临床级医疗 Agent 系统 |
| **英文标题** | Baichuan-M4 |
| **发布机构** | Baichuan AI（百川智能），与清华大学团队合作 |
| **发布日期** | 2026-06 |
| **核心创新** | 临床级医疗 Agent 系统；Baichuan-Harness 运行时；SPAR++ 跨度奖励、推理路径压缩、课程学习、稳定策略优化；多模态医学感知；幻觉率 3.3% |
| **论文** | https://arxiv.org/abs/2606.08982 |

> ⚠️ 修正：08-01 版记录 Baichuan-M4 为 arXiv:2606.12721，今日核实为 **arXiv:2606.08982**（single-source，官方 arXiv 列表）。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3.5 Flash（已于 08-01 收录，今日补充 arXiv + 基准细节）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：高效稀疏 MoE |
| **英文标题** | Step 3.5 Flash |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step 3.5 Flash（196B 总 / 11B 激活稀疏 MoE） |
| **发布日期** | 2026-01-31（Apache-2.0） |
| **核心创新** | 3:1 滑动窗口/全注意力交错 + MTP-3 多 token 预测；IMO-AnswerBench 85.4%、LiveCodeBench-v6 86.4%、BrowseComp 69.0%（带上下文管理）；性能对齐 GPT-5.2 xHigh 与 Gemini 3.0 Pro |
| **论文** | https://arxiv.org/abs/2602.10604 |

---

## 19. Yi / 01.AI

### 19.1 Yi-Lightning（已于 07-31 收录）

- **Yi-Lightning**（2025-10-16）：01.AI 旗舰 MoE，MIT 开源；混合专家 + 轻量级注意力；无今日新增信息。https://github.com/01-ai/Yi-Lightning

> 今日核实：01.AI 相关搜索受速率限制（429）未完全完成；未发现 2026 新报告。

---

## 交叉观察

- **开源 3T 级时代开启**：Kimi K3（2.8T）首次将 3T 级权重完全开源，配合 DeepSeek-V4（1.6T, MIT）与 GLM-5.2（MIT），开源旗舰参数量级快速逼近闭源。
- **美国开源权重旗舰之争成型**：NVIDIA Nemotron 3 Ultra（550B/55B，Hybrid Mamba-Attention + LatentMoE，20T tokens）正面挑战 DeepSeek-V4 / GLM-5.2 / Kimi K3 的开源领先地位——本轮美国实验室最强的开源权重发布。
- **安全/准备度报告成为新发布标配**：OpenAI GPT-5.6 System Card、Anthropic Claude Opus 5 System Card、xAI Grok 4.5 Model Card、Meta Muse Spark Safety & Preparedness Report 四家同月发布，Preparedness / Scaling Framework 框架趋同。
- **端侧 + 云端计算边界被重画**：Apple AFM 3（与 Google 合作）用 20B 稀疏模型（激活 1–4B）覆盖端侧，同时把最强大的 Cloud Pro 留在 Private Cloud Compute——"谁的硬件 + 谁的密钥"成为隐私叙事核心。
- **Agentic 基准（DeepSWE/SWE-bench Pro/Terminal-Bench 2.1）取代通用榜成为发布主战场**：Grok 4.5（与 Cursor 联合训练）、Nemotron 3 Ultra（Agentic Reasoning + 推理预算控制）均以 agentic 能力为头条。
- **Amazon Nova 2 补齐闭源多模态叙事**：Lite/Pro 的可配置 extended thinking + Omni 全模态输入/Sonic 语音到语音，全系 1M 上下文（今日更正 08-01"无 2026 报告"的误判）。
- **中国医疗垂直模型崛起**：Baichuan-M4（hallucination 3.3%，SPAR++ 跨度奖励）在临床决策支持上代表"通用模型→受监管垂直领域"的差异化路径。

---

## 待核实/待办

- **384K 最大输出长度归属**：此前记录中 384K 最大输出可能属于 DeepSeek-V4 或 GPT-5.6 Sol，未经独立来源证实，暂沿用 DeepSeek-V4 条目（后续核实）。
- **01.AI 2026 状态**：搜索受速率限制，待重试。
