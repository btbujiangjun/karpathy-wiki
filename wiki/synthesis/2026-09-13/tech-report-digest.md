---
title: "LLM Tech Report Digest — 2026-09-13"
type: synthesis
created: 2026-09-13
updated: 2026-09-13
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv, model-card, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, open-source, daily-digest]
---

# LLM Tech Report Digest — 2026-09-13

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-13）
> 本篇聚焦自 2026-09-12 摘要后的新增项（★ = 新收录；⭐ = 相对历史摘要的 catch-up，此前未被本 wiki 收录）
> 本日主线：**开放权重"以小博大"加速（Mistral Small 4 / Qwen3.8-27B / Nemotron 3.5 Lightning / Muse Spark 1.3）** + **Kimi K3 追踪更新** + **Grok 4.7 跳票持续**

---

## 1. DeepSeek — DeepSeek-AI

### 1.1 DeepSeek-V4.1-Flash（参照，已收录于 09-12 摘要）
- 发布日期: 2026-09-10（HF）；552B backbone MoE + 196B Engram；CED + CSA2 + SWA Bounded Replay；KV 890 bytes/token
- 链接: [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

### 1.2 DeepSeek-V4.1-Pro 上市路线（★ NEW — 今日动态）
- **动态**: 自 **2026-09-14 12:00（北京时间）** 起，API `deepseek-v4-pro` 将**临时路由至 deepseek-v4.1-flash**，并按 Flash 价格计价，直至 V4.1-Pro 正式上线（DeepSeek 官方公告口径）
- **意义**: 转换窗口期内用户可低成本使用 V4.1 架构（新 CED/CSA2 家族），正式 Pro 版 release 待定；一天前 API 曾短暂开放 V4.1-Flash 体验
- **状态**: V4.1-Pro 无模型卡/报告，发布日期未公开
- **链接**: [DeepSeek 官方](https://api-docs.deepseek.com/) / [Ollama deepseek-v4.1-flash](https://ollama.com/library/deepseek-v4.1-flash)

---

## 2. OpenAI

### 2.1 GPT-6 Astra System Card（参照，已收录于 09-12 摘要）
- 2026-09-03 发布 / 09-06 系统卡视觉评估更新；首个 Preparedness Framework Critical 网络安全级别模型
- 链接: [deploymentsafety.openai.com](https://deploymentsafety.openai.com/gpt-6-astra)

### 2.2 OpenAI 动态（★ 补充）
- GPT-6 Astra 面向企业/开发者广泛开放（rolling 进行中）；本窗口无新增技术/系统卡
- 社区消息：下一代 GPT（代号未定）仍在预训练阶段，无官方报告（low confidence，未验证）

---

## 3. Anthropic — Claude

### 3.1 Claude Fable 5.1 & Mythos 5.1 System Card（参照，已收录于 09-12 摘要）
- 2026-09-01; CB-1 化学/生物能力；Mythos 5.1 网络安全评估最强
- **预期动向**: 社区消息称 Fable 5.2 预计 2026-09 中旬发布（未验证），本窗口无新增报告

---

## 4. Meta AI — LLaMA / Muse

### 4.1 Muse Spark 1.3（★ NEW）
- **中文标题**: Muse Spark 1.3 模型卡（Agentic & Coding）
- **英文标题**: Muse Spark 1.3 — Agentic & Coding (Meta Research)
- **发布机构**: Meta AI
- **模型名称**: Muse Spark 1.3（Meta AI 底层模型版本）
- **发布日期**: 2026-09-02
- **核心参数**: 参数量未公开；开放 API（Muse Code + Meta Model API）
- **主要创新点**:
  - 面向 **agentic 与 coding** 场景的模型升级（与 09-12 摘要收录的 Muse Spark Safety & Preparedness Report 为同一模型家族的安全/能力两条线）
  - **~20% 更少 tool calls、~25% 更少 tokens** 完成同等 agent 任务（效率导向）
  - 对抗性鲁棒性（adversarial robustness）改进，与 safety report 呼应
- **链接**: [research.meta.ai](https://research.meta.ai/blog/introducing-muse-spark-1-3/)

### 4.2 Muse Spark Safety & Preparedness Report（参照，已收录于 09-12 摘要）
- [arXiv:2606.12429](https://arxiv.org/abs/2606.12429)；CBRN 缓解前 high risk

---

## 5. Google DeepMind — Gemini

### 5.1 Gemini 4 泄露线索（★ NEW — 低置信度）
- **动态**: 2026-09-05 前后首个 Gemini 4 **内部 checkpoint 泄露**（第三方抓取到早期预训练快照，非官方发布）
- **预期时间线**（均为第三方泄露/传闻，low confidence）:
  - Gemini 4 公开版预计 **2026-10** 左右推出；9 月可能先有 **Gemini 4 Flash-Lite 与 NB2Lite**（2B-class 端侧）
  - **Gemini 3.5 Pro 被搁置（shelved）**，资源集中到 Gemini 4
- **可信度**: 以上均为 leak/rumor，官方无公告；Gemini 4 仍在"significantly larger"预训练阶段（07-21 官方确认后无更新）

### 5.2 Gemini 3.6 Flash / Gemma 4（参照）
- Gemini 3.6 Flash: 2026-09-02 产品更新（Gemini Enterprise release notes）
- Gemma 4 Technical Report: 已收录于 09-12 摘要 | [arXiv:2607.02770](https://arxiv.org/abs/2607.02770)

---

## 6. Microsoft — Phi

### 6.1 Phi 系列（参照，无新增）
- Phi-4-reasoning-vision-15B 已收录于 09-12 摘要；Phi-5 处于 pre-release 预告阶段，正式技术报告未发布

---

## 7. Mistral AI

### 7.1 Mistral Small 4（⭐ NEW — catch-up，本日头条）
- **中文标题**: Mistral Small 4：统一 Reasoning / Multimodal / Agentic Coding 的开放混合模型
- **英文标题**: Mistral Small 4 (119B-A6B)
- **发布机构**: Mistral AI
- **模型名称**: Mistral Small 4（mistral-small-2603，119B-A6B MoE）
- **发布日期**: **2026-03-16**（Mistral 博客 / HF / NVIDIA NIM / NGC 多源一致；早前搜索引用的 09-10 为 crawler 日期，已核实排除）
- **核心参数**: 119B 总参数 / ~6B-6.5B 激活（MoE，8B 含 embedding/output）；**128 experts，4 active per token**；上下文 **256K**；Apache 2.0；多模态输入（文本+图像）；支持 11+ 语言
- **主要创新点**:
  - **首次将三条旗舰线合一**：Magistral（reasoning）+ Pixtral（multimodal）+ Devstral（agentic coding）→ 单一 checkpoint，`reasoning_effort` 可配置（low/medium/high）
  - **效率**: 相对 Mistral Small 3，latency-optimized 下 end-to-end 完成时间 -40%，throughput-optimized 下吞吐 3×
  - **基准**: AA LCR 0.72（仅 1.6K 字符输出，Qwen 需 3.5-4× 输出量）；LiveCodeBench 超越 GPT-OSS 120B 且输出 -20%
  - **生态**: 成为 **NVIDIA Nemotron Coalition 创始成员**；配套 eagle head（speculative decoding）+ NVFP4 checkpoint（llm-compressor，与 vLLM/Red Hat/NVIDIA 合作）
  - API 定价 $0.15/M input、$0.6/M output
- **链接**: [Mistral Blog](https://mistral.ai/news/mistral-small-4/) / [HF](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) / [Mistral Docs](https://docs.mistral.ai/models/mistral-small-4-0-26-03)
- ⚠️ 说明: 模型发布于 2026-03，但本 wiki 历史 digest（07-23/07-24/07-26/07-27/09-11/09-12）均未收录，故今日补录（catch-up）

### 7.2 Shieldstral / Ministral 3 / Mistral 3（参照）
- 均已收录于 09-12 摘要

---

## 8. Alibaba — Qwen

### 8.1 Qwen3.8-27B（★ NEW）
- **中文标题**: Qwen3.8-27B：开放的端侧级旗舰视觉-语言模型
- **英文标题**: Qwen3.8-27B (Apache 2.0, vision-language)
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3.8-27B（dense）
- **发布日期**: 2026-09（098x 快照线）
- **核心参数**: 27B dense；Apache 2.0；原生 vision-language（图像+视频输入）；1M 上下文（hosted 版）；QwenCloud
- **主要创新点**:
  - **端侧级 27B 开放权重**，延续 Qwen3.8 系列 Apache 2.0 开源路线（与 27B-A3B MoE 路线并行的 dense 版本）
  - **灵活思考控制**: `reasoning_effort` + `preserve_thinking` 参数（可保留/丢弃思考过程）
  - 原生多模态（vision-language 指令，与 09-12 收录的 Qwen3.8-Flash-Next 混合注意力线互补）
- **链接**: [HF Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)

### 8.2 Qwen3.8-Max-0902 快照（★ NEW）
- **动态**: 2026-09-02 更新 Qwen3.8-Max snapshot（`-0902`），面向编码/agentic/视觉能力微调升级
- **核心参数**: Qwen3.8-Max 基线 = **2.4T-A95B MoE** + 原生 vision + 1M ctx；-0902 为迭代快照
- **链接**: [HF Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

### 8.3 Qwen3.8-Flash-Next / Qwen3.8-Max（参照）
- 均已收录于 09-12 摘要

---

## 9. xAI — Grok

### 9.1 Grok 4.7 跳票持续（★ NEW — 今日动态更新）
- **动态**: 2026-09-11 马斯克称仍需"a few more days" RL tuning（2026-09-13 仍无正式发布）；原预期 09-12 前发布，现目标 09-15+
- **第三方分析（Data Studios 2026-09-12）**: Grok 4.7 延迟源于 **RL 后训练的自我校验（self-checking）问题** ——
  - 响应长度惩罚设置过激进（response-length penalty too aggressive）→ 模型过早停止（premature stopping）
  - 自我校验不足：长链推理中未充分 self-check 即收敛
  - 需在 response-length 正则与推理质量间重调平衡
- **参数传闻**: ~2.1T（较 Grok 4.6 的 1.5T 提升 ~40%，第三方报道，未验证）
- **状态**: 无 Grok 4.7 模型卡/报告
- **链接**: [cryptobriefing](https://www.cryptobriefing.com/xai-delays-grok-4-7-release/) / [Data Studios](https://www.datastudios.org/post/xai-grok-4-7-delay-reinforcement-learning-self-checking)

### 9.2 Grok 4.6 Model Card（参照）
- 已收录于 09-12 摘要 | [Model Card PDF](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf)

---

## 10. NVIDIA — Nemotron

### 10.1 Nemotron 3.5 Lightning（★ NEW）
- **中文标题**: Nemotron 3.5 Lightning：面向长程 Agent 的开源推理模型
- **英文标题**: NVIDIA Nemotron 3.5 Lightning (30B-A3B)
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3.5 Lightning（开放权重，MoE）
- **发布日期**: 2026-08 (blog 2026-08-20, "Aug 11, 2026" 条目)
- **核心参数**: 30B 总参数 / **3B 激活**；MoE；**NVFP4 量化 checkpoint**；NeMo Switchyard 路由
- **主要创新点**:
  - 超低激活参数（3B/30B）针对 **long-running agents** 优化（成本与延迟路线）
  - **NVFP4 量化版本**发布（延续 Nemotron 3 Ultra 的 FP4 路线）
  - **NeMo Switchyard**：全新 MoE 路由框架
  - 加入 NVIDIA Nemotron Coalition 生态（与 Mistral 等成员协作）
- **链接**: [NVIDIA Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning/)

### 10.2 Nemotron 4 传闻（★ NEW — 低置信度）
- 2026-08-11 前后泄露 **Nemotron 4 在研（~1T 参数）** 相关信息；无官方公告/报告（tentative）
- Nemotron 3 Ultra Model Card 已收录于 09-12 摘要

---

## 11. Moonshot AI — Kimi

### 11.1 Kimi K3（⭐ NEW — catch-up，本日头条级）
- **中文标题**: Kimi K3：开放前沿智能（首个开放 3T-class 模型）
- **英文标题**: Kimi K3 — Open Frontier Intelligence（Kimi K3 Technical Report）
- **发布机构**: Moonshot AI
- **模型名称**: Kimi K3（2.8T-A104B MoE）
- **发布日期**: 2026-07-16 发布（API/公告）→ **2026-07-27 权重全量开源**；技术报告 `k3_tech_report.pdf` 随仓库发布
- **核心参数**: **2.8T 总参数 / 104B 激活**；896 experts（16 routed + 2 shared per token）；93 层（69 KDA + 24 Gated MLA）；上下文 **1M**；原生 vision（文本+图像，MoonViT-V2 视觉编码器 401M）；vocab 160K；**MXFP4 weights / MXFP8 activations（quantization-aware training，SFT 起）**；SiTU-GLU 激活
- **主要创新点**:
  - **KDA（Kimi Delta Attention）**: 线性注意力主导 + 周期 full-attention 层混合（长序列高效）
  - **AttnRes（Attention Residuals）**: 跨深度选择性检索表征，替代单一残差流累积
  - **Stable LatentMoE**: 极高稀疏（16/896 active），~2.5× 相对 Kimi K2 的 scaling 效率提升
  - **首个开放 3T-class 模型**；Kimi K3 License（open-weight）
  - 基建: vLLM 合作 **FlashKDA**/fused KDA decode/projection、KDA prefill cache（vLLM 社区实现随模型发布）；推理引擎 vLLM/SGLang/TokenSpeed day-0 支持
  - 基准亮点: GPQA-D 93.5；DeepSWE 67.5；Terminal-Bench 2.1 88.3；BrowseComp 91.2（无 context compaction）；Kimi Code Bench 2.0 72.9；reasoning_effort low/high/max（默认 max）
- **链接**: [HF moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) / [GitHub MoonshotAI/Kimi-K3 + k3_tech_report.pdf](https://github.com/MoonshotAI/Kimi-K3) / [Kimi Blog](https://www.kimi.ai/blog/kimi-k3) / [vLLM 预览](https://github.com/vllm-project/vllm-project.github.io/blob/main/_posts/2026-07-22-kimi-k3-preview.md)
- ⚠️ 说明: K3 发布于 2026-07 但此前 digest 均未收录（07-23~09-12 只覆盖到 K2.7 Code 与 K2.5），今日补录（catch-up）；激活参数 104B（此前第三方 ThunderCompute 报道称 ~50B，以官方 README 104B 为准）

### 11.2 Kimi K2.7 Code（参照）
- 已收录于 09-12 摘要（2026-09-04, 1T-A32B, Kimi Code Bench v2 62.0 +21.8%）

---

## 12. Amazon — Nova

### 12.1 Nova Premier 退役 + 新前沿模型预期（★ NEW）
- **动态**: **Nova Premier 定于 2026-09-14 停止提供服务（EOL）**，当前主力为 **Nova 2 Omni（KTLO）**
- **Nova Premier Technical Report / Model Card** 存在官方文档（Amazon Science，2025-12）+ arXiv:2506.12103（Nova Family，参照）；2026 re:Invent 预期发布全新前沿模型（第三方预期，未验证）
- **Nova 2 家族**已收录于 09-12 摘要（2025-12-02, Nova Act ~90% browser 可靠性）
- **链接**: [Amazon Science — Nova Premier TR & Model Card](https://www.amazon.science/publications/amazon-nova-premier-technical-report-and-model-card)

---

## 13. Apple — Apple Intelligence Foundation Models

### 13.1 AFM 3 系列（参照，无新增）
- AFM 3 第三代已收录于 09-12 摘要；2026 年度技术报告官网承诺 "later this summer"，截至 2026-09-13 **仍未发布**

---

## 14. ByteDance — Seed / 豆包

### 14.1 Seed / Doubao（参照，无新增）
- Seed2.0 Model Card 已收录于 09-12 摘要（[arXiv:2607.00248](https://arxiv.org/abs/2607.00248)）；本窗口无新报告

---

## 15. 智谱 AI — GLM

### 15.1 GLM 系列（参照，无新增）
- GLM-5.2 / GLM-5.3 Flash（国产芯片全流程）/ GLM-6 在研已收录于 09-12 摘要；本窗口无新报告

---

## 16. InternLM / 上海 AI Lab

### 16.1 Intern 系列（参照，无新增）
- Intern-S2-Preview / Intern-S1-Pro / InternVideo3 / InternVL3.5 均已收录于 09-12 摘要；本窗口无新报告

---

## 17. StepFun — 阶跃星辰

### 17.1 Step AOS / STEPX Neo AI 手机（★ NEW — 产品线，非技术报告）
- **动态**: 2026-07-13 发布 **Step AOS（自研 AI 操作系统）** 并推出 **STEPX Neo AI-native 手机**；2026-07-12 发布 **Step Edge** 端侧小模型家族
- **定位**: AI 原生设备/OS 产品线（操作系统 + 端侧模型），区别于模型技术报告
- 技术报告类: Step-3.7-Flash / Step3-VL-10B 已收录于 09-12 摘要

---

## 18. 01.AI — Yi

### 18.1 Yi 系列（无新增）
- 截至 2026-09-13 无 2026 年新 Yi 技术报告；最新综合报告 Yi-Lightning 2024-12

---

## 19. Baichuan

### 19.1 Baichuan 系列（参照，无新增）
- Baichuan-M3 已收录于 09-12 摘要（HealthBench-Hard 44.4 超 GPT-5.2）；本窗口无新报告

---

## 本日头条与动态（相对 2026-09-12 摘要的 Delta）

### 1. 开放权重扩容：今天最重要的新收录
| 新增项 | 要点 | 类型 |
|--------|------|------|
| Mistral Small 4（⭐ catch-up） | 119B-A6B MoE，128e/4active，256K，Apache 2.0，Magistral+Pixtral+Devstral 三合一，Nemotron Coalition 创始成员 | 模型卡/开放权重 |
| Kimi K3（⭐ catch-up） | 2.8T-A104B，KDA+AttnRes+Stable LatentMoE(16/896)，1M ctx，首个开放 3T-class，k3_tech_report.pdf | 技术报告/开放权重 |
| Nemotron 3.5 Lightning（★） | 30B-A3B，NVFP4，NeMo Switchyard，长程 agent | 模型卡/开放权重 |
| Muse Spark 1.3（★） | agentic+coding，tool calls -20%/tokens -25%，adversarial robustness | 模型卡 |
| Qwen3.8-27B（★） | 27B dense vision-language，Apache 2.0，1M ctx | 模型卡/开放权重 |

### 2. Grok 4.7 跳票持续（2026-09-11 起）
- RL tuning 自我校验问题：response-length 惩罚过激 + 过早停止 + self-check 不足（Data Studios 分析）
- 目标 ~09-15+；参数传闻 2.1T

### 3. DeepSeek 路线图更新
- 09-14 12:00 起 `deepseek-v4-pro` 临时路由至 V4.1-Flash（Flash 价格），V4.1-Pro 正式发布待定

### 4. 今日新增/更新汇总（★ 共 10 项，含 2 项 catch-up）
| 公司 | 新增项 | 日期 | 类型 |
|------|--------|------|------|
| Mistral | Mistral Small 4 ⭐ | 2026-03-16 | 模型卡/开放权重 |
| Moonshot | Kimi K3 ⭐ + tech report | 2026-07-16/27 | 技术报告/开放权重 |
| Meta | Muse Spark 1.3 | 2026-09-02 | 模型卡 |
| NVIDIA | Nemotron 3.5 Lightning | 2026-08 | 模型卡 |
| NVIDIA | Nemotron 4 在研（传闻） | 2026-08-11 | tentative |
| Qwen | Qwen3.8-27B / Max-0902 | 2026-09 | 模型卡/快照 |
| xAI | Grok 4.7 跳票 + RL 分析 | 2026-09-11/12 | 动态 |
| DeepSeek | V4.1-Pro 临时路由至 Flash | 2026-09-14 起 | 动态 |
| Google | Gemini 4 泄露线索 + 时间线传闻 | 2026-09-05 | leak（low confidence） |
| Amazon | Nova Premier EOL 09-14 | 2026-09-14 | 动态 |
| StepFun | Step AOS / STEPX Neo / Step Edge | 2026-07 | 产品线 |

### 5. 未发布新正式报告的公司
- Anthropic（Fable 5.2 传闻 09 中旬，未验证）、Apple（AFM 3 报告持续爽约）、ByteDance、Zhipu、InternLM、Microsoft（Phi-5 未发布）、01.AI、Baichuan
- OpenAI: 仅 GPT-6 Astra 系统卡（无技术报告）

---

## 交叉主题分析

### 1. 开放权重方向："3T-class 时代"开启 + "统一能力"成为卖点
- **Kimi K3**: 首个开放 3T-class（2.8T-A104B）；KDA 线性注意力 + AttnRes + Stable LatentMoE(16/896)
- **Mistral Small 4**: 首次把 推理/多模态/agentic-coding 三线统一到单一开放 checkpoint（reasoning_effort 可配置）
- 对比 09-12 的开放阵营（DeepSeek V4.1-Flash、Gemma 4、Qwen3.8-Flash-Next），开放模型在 参数量级、稀疏化、能力融合 三线同时发力

### 2. 效率指标继续内卷（活跃参数/输出 token 竞争）
| 模型 | 总/激活参数 | 效率卖点 |
|------|------------|---------|
| Kimi K3 | 2.8T / 104B | 16/896 experts，~2.5× K2 scaling 效率 |
| Mistral Small 4 | 119B / 6B | AA LCR 1.6K 字符输出达 0.72；LiveCodeBench 输出 -20% |
| Nemotron 3.5 Lightning | 30B / 3B | 3B active 支撑 long-running agents |
| Qwen3.8-27B | 27B (dense) | 端侧级 vision-language |

### 3. 量化技术成为开放权重标配
- Kimi K3: MXFP4 weights / MXFP8 activations（QAT，SFT 起）
- Nemotron 3.5 Lightning: NVFP4 checkpoint
- Mistral Small 4: NVFP4 checkpoint（llm-compressor，vLLM/Red Hat/NVIDIA 协作）
- 与 09-12 摘要 DeepSeek FP4 (E2M1) KV caching 呼应 → FP4 生态（NVFP4/MXFP4）从推理量化走向协同训练/后训练 QAT

### 4. 发布节奏观察：多家公司在研/预告，正式发布空窗
- 在研/预告: Grok 4.7（RL tuning 中）、DeepSeek V4.1-Pro（待定）、Gemini 4（10 月传闻）、Nemotron 4（1T 传闻）、Phi-5（pre-release）、Anthropic Fable 5.2（09 中旬传闻）、Amazon 新前沿模型（re:Invent 传闻）
- 空窗期内的主要供给来自 开放权重（Mistral/Qwen/NVIDIA/Kimi）与 存量报告的 catch-up 补录

### 5. 安全与产品线动态
- Meta Muse Spark 系列双线（1.3 模型卡 + Safety & Preparedness Report）持续
- Amazon Nova Premier 退役（09-14）→ Nova 2 Omni KTLO，re:Invent 新模型预期
- StepFun 转向 AI-native 设备/OS（Step AOS + STEPX Neo），模型层保持 Step-3.7 系列