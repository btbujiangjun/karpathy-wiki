---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-01
updated: 2026-08-01
sources: [tech-report-digest-2026-07-31.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-01（每日更新；今日重点核实：Meta Muse Spark、Microsoft Phi-4-reasoning-vision、Mistral Leanstral 1.5、ByteDance Seedance 2.5、Apple AFM 2025、Zhipu GLM-5.2、Moonshot Kimi K3、InternLM、StepFun Step 3.5 Flash）

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4（已于 07-31 收录，补充细节）

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
| **核心创新** | CSA（token 级压缩 + DSA，KV 压缩 4:1）稀疏注意力；thinking / non-thinking 双模式；MIT 开源；V4-Pro-Max SWE-bench Verified 80.6%（开源最高，llm-stats 2026-06），GPQA Diamond 90.1（官方自报） |
| **论文** | https://arxiv.org/abs/2606.19348 |

---

## 2. OpenAI

### 2.1 GPT-5.6 System Card（已于 07-31 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡 |
| **英文标题** | GPT-5.6 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 低配 / Luna 最快最省） |
| **发布日期** | 2026-07-09 |
| **核心创新** | 三模型家族：Sol（旗舰）/ Terra（低配）/ Luna（最快最省）；Preparedness：Bio/Chem High、Cyber High、Self-Improvement below High；Sol bio/chem 评分 4 最高 |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6 |

---

## 3. Meta

### 3.1 Muse Spark Safety & Preparedness Report（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Muse Spark 安全与准备度报告 |
| **英文标题** | Muse Spark Safety & Preparedness Report |
| **发布机构** | Meta Superintelligence Labs（Meta AI） |
| **模型系列** | Muse Spark（Meta AI 底层模型） |
| **发布日期** | 2026-05-26 |
| **核心创新** | 在 Advanced AI Scaling Framework 下评估；Chem/Bio 缓解前达 "high risk" 类别，已实施多层级缓解；危险化学/生物工作流拒绝率达到 SOTA；低欺骗率、同行中最低 cyber-misuse 合规率；部分行为维度仍待改进 |
| **论文** | https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ |

---

## 4. Google DeepMind

### 4.1 Gemini 3.6 Flash Model Card（已于 07-31 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.6 Flash 模型卡 |
| **英文标题** | Gemini 3.6 Flash Model Card |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026-07-21 |
| **核心创新** | Gemini 3 系列原生多模态推理；基于 Gemini 3.5 Flash，token 效率更高；知识截止 2026-03 |
| **论文** | https://deepmind.google/models/model-cards/gemini-3-6-flash/ |

---

## 5. Anthropic

### 5.1 Claude Opus 5 System Card（已于 07-31 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 系统卡 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **发布日期** | 2026-07-24/25 |
| **核心创新** | Opus 4.8 升级；agentic coding / computer use / 长程工作 / 数学科学推理提升；价格 $5/$25 每 M tokens；API 名 `claude-opus-5` |
| **论文** | PDF: https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf |

---

## 6. Mistral

### 6.1 Leanstral 1.5（今日新增核实）

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

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.5-Omni（已于 07-31 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba Qwen |
| **发布日期** | 2026-04 |
| **核心创新** | 千亿级参数、256K 上下文；100M+ 小时音视频数据；Thinker/Talker 均用 Hybrid Attention MoE；Qwen3.5-Omni-Plus 215 项 SOTA、超 Gemini-3.1 Pro 关键音频项；10 语言 + 零样本音色定制 |
| **论文** | https://arxiv.org/abs/2604.15804 |

---

## 8. Microsoft（Phi）

### 8.1 Phi-4-reasoning-vision-15B Technical Report（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-reasoning-vision-15B（15B 紧凑开源） |
| **发布日期** | 2026-03（MSR-TR-2026-10） |
| **核心创新** | 数据质量（系统过滤、纠错、合成增强）为最大性能杠杆；高分辨率动态分辨率视觉编码器；推理/非推理数据混合 + 显式 mode token，单一模型双模式 |
| **论文** | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

---

## 9. Apple

### 9.1 Apple Intelligence Foundation Language Models Tech Report 2025（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型技术报告 2025 |
| **英文标题** | Apple Intelligence Foundation Language Models Tech Report 2025 |
| **发布机构** | Apple |
| **模型系列** | 端侧 ~3B + 服务端 PT-MoE（Parallel-Track MoE） |
| **发布日期** | 2025-07-17 |
| **核心创新** | 端侧 ~3B 模型：KV-cache sharing + 2-bit 量化感知训练；服务端 PT-MoE 跑在 Private Cloud Compute；多语言多模态 + 工具调用；Swift Foundation Models 框架（guided generation、约束工具调用、LoRA） |
| **论文** | https://arxiv.org/abs/2507.19038 |

---

## 10. NVIDIA

### 10.1 Nemotron 3 Super Technical Report（已于 07-31 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron 3 Super 技术报告 |
| **英文标题** | NVIDIA Nemotron 3 Super Technical Report |
| **发布机构** | NVIDIA |
| **发布日期** | 2026-04-03 |
| **核心创新** | 120B 总 / 12B 激活；Mamba-Attention 混合 MoE；NVFP4 预训练、LatentMoE、MTP 投机解码；25T tokens；1M 上下文；吞吐 2.2× vs GPT-OSS-120B、7.5× vs Qwen3.5-122B；HF 开源 |
| **论文** | PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf |

---

## 11. xAI

### 11.1 Grok 4.5 Model Card（已于 07-31 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.5 模型卡 |
| **英文标题** | Grok 4.5 Model Card |
| **发布机构** | xAI |
| **发布日期** | 2026-07-14 |
| **核心创新** | 编码/工程/设计/专业工作流；高 agentic、推理步骤减半；安全域含 cyber、bio knowledge、bio agentic、jailbreaks |
| **论文** | PDF: https://media.x.ai/v1/website/card-7f81d41b.pdf |

---

## 12. Amazon

### 12.1 The Amazon Nova family（今日核实：为 2024 技术报告，无 2026 新报告）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族：技术报告与模型卡 |
| **英文标题** | The Amazon Nova family of models: Technical report and model card |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Pro / Lite / Micro / Canvas / Reel |
| **发布日期** | 2024（无 2026 新报告；当前旗舰为 Nova Pro） |
| **核心创新** | 多模态模型家族，Pro（通用推理）/ Lite（延迟敏感）/ Micro（超低延迟）/ Canvas（图像）/ Reel（视频） |
| **论文** | https://arxiv.org/abs/2504.13186 |

---

## 13. ByteDance（字节跳动）

### 13.1 Seedance 2.5（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Seedance 2.5 正式发布 |
| **英文标题** | Seedance 2.5 |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seedance 2.5（视频生成） |
| **发布日期** | 2026-07-31 |
| **核心创新** | 单次 30 秒生成 + 多轮延长；参考输入最多 30 图 + 10 视频 + 10 音频；统一多模态音视频联合生成架构；时间戳级编辑、绿幕/黏土渲染参考；10+ 语言 |
| **论文** | https://seed.bytedance.com/zh/blog/一键成片-随心参考-seedance-2-5-正式发布 |

---

## 14. Zhipu（智谱）

### 14.1 GLM-5.2（今日新增核实，当前旗舰）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.2：稀疏注意力 + IndexShare |
| **英文标题** | GLM-5.2 |
| **发布机构** | Zhipu AI（智谱） |
| **模型系列** | GLM-5.2（MoE，总量 753B 量级，激活数待确认） |
| **发布日期** | 2026-06-13 |
| **核心创新** | MIT 开放权重；1M 上下文；Terminal-Bench 2.1 81.0（vs Claude Opus 4.8 的 85.0）；稀疏注意力 + IndexShare（每 4 层一次注意力索引器）+ MoE 路由；无原生视觉（视觉在 GLM-V 产品线） |
| **论文** | https://zhipu-ai.cn/glm-5.2 |

### 14.2 GLM-5.3（未发布，仅有社区传言）

> ⚠️ 注意：GLM-5.3 截至 2026-08-01 未正式发布，仅存社区传言（可能跳过 5.3/5.4 直接发布 GLM-5.5，预计 2026-08，可能 >1T 参数）。不写入正式条目。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3（今日新增核实全量技术细节）

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
| **论文** | https://kimi.ai/k3-technical-report |

---

## 16. InternLM（上海 AI 实验室）

### 16.1 Intern-S1-Pro（今日核实补充）

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿参数科学多模态模型 |
| **英文标题** | Intern-S1-Pro |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | Intern-S1-Pro（1T 总参 MoE，512 experts，激活 8 experts / 22B） |
| **发布日期** | 2026-02-04 |
| **核心创新** | SAGE "通专融合" 架构；Fourier 位置编码 + 时间编码器；AI4S 2.0；奥赛金牌级数学/物理推理；未搜到 2026 新报告（7/31 后无更新） |
| **论文** | https://intern.shai-lab.cn/intern-s1-pro |

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4（已于 07-31 收录）

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4 |
| **英文标题** | Baichuan-M4 |
| **发布机构** | Baichuan AI（百川智能） |
| **发布日期** | 2026-06（arXiv:2606.12721） |
| **核心创新** | 医疗/科学领域多模态；无今日新增信息 |
| **论文** | https://arxiv.org/abs/2606.12721 |

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3.5 Flash（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：高效稀疏 MoE |
| **英文标题** | Step 3.5 Flash |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step 3.5 Flash（196B 总 / 11B 激活稀疏 MoE） |
| **发布日期** | 2026-01-31（Apache-2.0） |
| **核心创新** | 3-way MTP（MTP-3 多 token 预测）；吞吐 100–300 tok/s（峰值 350）；SWE-bench Verified 74.4%、Terminal-Bench 2.0 51.0%；256K 上下文；RL 框架持续自改进 |
| **论文** | https://github.com/stepfun-ai/Step-3.5-Flash ；blog: https://static.stepfun.com/blog/step-3.5-flash/ |

---

## 19. Yi / 01.AI

### 19.1 Yi-Lightning（已于 07-31 收录）

- **Yi-Lightning**（2025-10-16）：01.AI 旗舰 MoE，MIT 开源；混合专家 + 轻量级注意力；无今日新增信息。https://github.com/01-ai/Yi-Lightning

---

## 交叉观察

- **开源 3T 级时代开启**：Kimi K3（2.8T）首次将 3T 级权重完全开源，配合 DeepSeek-V4（1.6T, MIT）与 GLM-5.2（MIT），开源旗舰参数量级快速逼近闭源。
- **安全/准备度报告成为新发布标配**：OpenAI GPT-5.6 System Card、Anthropic Claude Opus 5 System Card、xAI Grok 4.5 Model Card、Meta Muse Spark Safety & Preparedness Report 四家同月发布，Preparedness / Scaling Framework 框架趋同。
- **垂直/特殊能力模型涌现**：Mistral Leanstral 1.5（形式化验证）、Microsoft Phi-4-reasoning-vision-15B（多模态推理）、Intern-S1-Pro（AI4S 科学多模态）、Muse Spark（多智能体编排推理）。
- **多模态视频/音频生成持续迭代**：ByteDance Seedance 2.5（30s + 多轮延长 + 多参考输入）代表视频生成进入"长时长 + 可控参考"阶段。
