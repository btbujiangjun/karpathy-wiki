---
title: LLM Tech Report Digest — 2026-08-17
type: synthesis
created: 2026-08-17
updated: 2026-08-17
sources: [web-search]
tags: [tech-report, moe, scaling, multimodal, reasoning, daily-digest]
---

# LLM Tech Report Digest — 2026-08-17

> 19 家主流 AI 公司/实验室最新技术报告与旗舰模型汇总。沿用 08-11/12/13 基线结构，每家一节：最新模型 + 发布日期 + 核心参数 + 架构创新 + 论文链接。

---

## 1. DeepSeek

| 项 | 值 |
|---|---|
| 最新旗舰 | DeepSeek-R1 |
| 发布日期 | 2025-01 |
| 开源状态 | ✅ MIT License |
| 核心参数 | 671B 总参 / 37B 激活 MoE（沿用 V3 基座） |
| 上下文窗口 | 128K |
| 架构创新 | 纯 RL 推理（Group Relative Policy Optimization, GRPO）；端到端 RL 训练涌现 CoT 推理，无需 SFT 冷启动；6 个蒸馏密集模型（1.5B–70B）用于端侧部署 |
| 核心贡献 | 首次证明纯 RL 路线可从基座模型直接获得强推理能力；GRPO 替代 PPO 降低训练成本 |
| 论文 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) |
| 最新动态 | V4 Pro 官方 GA（08-13，OpenRouter 上架 `deepseek-v4-pro-0813`）：1M ctx，$0.435/$0.87/M tokens；V4 Pro 1.6T 总参/49B 激活 MoE + CSA；V4 Flash 284B/13B，均 MIT 开放权重 |

---

## 2. OpenAI

| 项 | 值 |
|---|---|
| 最新旗舰 | GPT-5（含 GPT-5.6 Sol） |
| 发布日期 | 2025-08-13（GPT-5 System Card） |
| 开源状态 | ❌ 闭源 |
| 架构创新 | 统一系统 = Fast model + Thinking model + Router（三路混合）；原生多模态（文本/图像/音频/视频输入） |
| 核心贡献 | "Unified System"范式：路由器动态选择快速路径或深度思考路径；System Card 首次系统披露安全评估方法论 |
| 论文 | [GPT-5 System Card](https://openai.com/index/gpt-5-system-card/) |
| 最新动态 | Astra 定名（08-01 官方博客）——"next major model"，内部已解决多道数学/理论计算机难题；GPT-5.6 Sol 仍为最新公开旗舰 |

---

## 3. Meta AI

| 项 | 值 |
|---|---|
| 最新旗舰 | Llama 4 Scout / Maverick |
| 发布日期 | 2025-04-05 |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | Scout: 109B 总参 / 17B 激活；Maverick: 400B 总参 / 17B 激活（均为 MoE） |
| 上下文窗口 | Scout 10M ctx / Maverick 1M ctx |
| 架构创新 | 原生多模态（文本 + 图像统一训练）；早期融合（early fusion）架构；MetaP 自动超参选择 |
| 核心贡献 | 10M 上下文窗口（Scout）；开源 MoE 多模态模型达到商用水平 |
| 论文 | [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |
| 最新动态 | 405B 开放权重承诺持续未兑现（自 08-11 起记录，NeuralStack/Bloomberg 预告口径无发布实据）；Muse Glimmer 30B 开源（08-10，Apache 2.0）；Muse Spark 1.2 权重承诺数周内开源 |

---

## 4. Google DeepMind

| 项 | 值 |
|---|---|
| 最新旗舰 | Gemini 2.5 Pro / Flash |
| 发布日期 | 2025-06-16 |
| 开源状态 | ❌ 闭源 |
| 架构创新 | "Thinking model"范式（内置推理链）；原生多模态（文本/图像/音频/视频）；>1M token 上下文；支持 3 小时视频输入 |
| 核心贡献 | Thinking model 范式引领（o1 路线之后最强推理模型）；1M+ 超长上下文；多模态原生融合 |
| 论文 | [Google AI Blog](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| 最新动态 | Gemini 3.5 Pro 仍延迟，Gemini 4 预期 11-12 月（Pichai "最雄心勃勃预训练"）；Hassabis 转任主席（08-05 Reuters），Kavukcuoglu 升 SVP，Jeff Dean 离职 |

---

## 5. Anthropic

| 项 | 值 |
|---|---|
| 最新旗舰 | Claude Opus 4 / Sonnet 4 |
| 发布日期 | 2025-05（Opus 4）/ 2025-05（Sonnet 4） |
| 开源状态 | ❌ 闭源 |
| 架构创新 | Hybrid reasoning（extended thinking + 直接回答双模式）；多步 agentic 工具调用；ASL-3 / ASL-2 安全分级 |
| 核心贡献 | Agent 能力标杆（Claude Code 成为 agentic coding 主流工具）；RSP v3 安全框架首个实践者 |
| 论文 | [Anthropic System Card](https://www.anthropic.com/research) |
| 最新动态 | Claude Opus 4.6（MLE Bench 75.7% 最佳）；Fable 5.1 泄漏未确认（X 泄漏两条，$10/$50 定价为传闻）；Opus 5 已部分超越 Fable 5 |

---

## 6. Mistral AI

| 项 | 值 |
|---|---|
| 最新旗舰 | Mistral Large 3 |
| 发布日期 | 2025-12-02 |
| 开源状态 | ✅ Apache 2.0 |
| 核心参数 | 675B 总参 / 41B 激活（MoE） |
| 架构创新 | MoE 架构 + 欧洲主权 AI 路线（in-region inference + 开放模型 + 欧洲基础设施） |
| 核心贡献 | 欧洲最大开源 MoE；主权 AI 基础设施定位 |
| 论文 | [Mistral Large 3](https://mistral.ai/) |
| 最新动态 | Shieldstral 安全产品（08-04）；Robostral Navigate（AI Science Robotics，机器人导航）；Code/Apps sections（Vibe/Le Chat）预告；夏季新"大而稀疏"开放 MoE 权重预告（未发布）；无新 LLM 报告 |

---

## 7. Qwen (阿里通义)

| 项 | 值 |
|---|---|
| 最新旗舰 | Qwen3（含 Qwen3.8-Max） |
| 发布日期 | 2025-05-14（Qwen3）；2026-08（Qwen3.8-Max） |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | Qwen3: 0.6B–235B 全系列；Qwen3.8-Max: 2.4T 总参 / 95B 激活 MoE |
| 上下文窗口 | 128K（Qwen3）/ 1M（Qwen3.8-Max） |
| 架构创新 | Thinking / non-thinking 统一模式（hybrid thinking）；119 种语言支持；2.4T MoE 基座（Qwen3.8-Max） |
| 核心贡献 | 中文 LLM 生态标杆；开源 MoE 最大规模之一；混合推理模式（thinking + direct） |
| 论文 | [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) |
| 最新动态 | Qwen3.8-Max 权重 08-12 验收日 HF 实时检查仍未兑现（ModelScope 发布页指向 08-12，但 HF 无条目）；Qwen3.8-27B 同为 08-03 验收；license 争议（US/EU/UK/Korea 地域限制） |

---

## 8. Yi / 01.AI (零一万物)

| 项 | 值 |
|---|---|
| 最新旗舰 | Yi-Lightning |
| 发布日期 | 2024-10-16（Chatbot Arena 首秀）/ 2024-12（技术报告） |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | 未公开具体参数量（MoE 架构） |
| 架构创新 | Enhanced MoE（fine-grained expert segmentation + balanced routing + cross-layer KV cache sharing）；RAISE（Responsible AI Safety Engine）四组件安全框架 |
| 核心贡献 | Chatbot Arena 第 6 名（中文第 2 / Math 第 3 / Coding 第 4）；静态 benchmark vs 真实人类偏好差异观察 |
| 论文 | [Yi-Lightning Technical Report](https://arxiv.org/abs/2412.01253) |
| 最新动态 | 2026 年无新旗舰；转向企业 AI / 主权 AI（万策平台、哈国 Q.AI 合资）；Yi-Lightning 仍为最新模型（2024-10） |

---

## 9. Baichuan (百川智能)

| 项 | 值 |
|---|---|
| 最新旗舰 | Baichuan-M2 |
| 发布日期 | 2026-08-11 |
| 开源状态 | ✅ 开源 |
| 核心参数 | 32B |
| 架构创新 | 医疗增强型大模型；以 32B 尺寸超越 gpt-oss-120B |
| 核心贡献 | HealthBench 60.1（32B 超 120B）；延续医疗垂直战略（M4 HealthBench 68.6 世界第一保留） |
| 论文 | 未发布独立技术报告 |
| 最新动态 | 延续医疗垂直化路线；开源策略 |

---

## 10. Microsoft (Phi 系列)

| 项 | 值 |
|---|---|
| 最新旗舰 | Phi-4 |
| 发布日期 | 2024-12-12 |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | 14B |
| 架构创新 | 合成数据为核心训练范式；focus on STEM reasoning |
| 核心贡献 | 以 14B 参数在 STEM 推理任务上接近更大模型性能；合成数据方法论验证 |
| 论文 | [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905) |
| 最新动态 | Phi-5 仍为 single-source 传闻，无官方报告（2026-08） |

---

## 11. Apple

| 项 | 值 |
|---|---|
| 最新旗舰 | Apple Intelligence Foundation Language Model (AFM) 2025 |
| 发布日期 | 2025-07 |
| 开源状态 | ❌ 闭源 |
| 核心参数 | ~3B（端侧）+ Server PT-MoE（云端） |
| 架构创新 | 端云协同架构；2-bit 量化（PT-MoE with 2-bit weights）；on-device inference 优先 |
| 核心贡献 | 首个大规模量产的端侧 LLM 量化部署方案；隐私优先架构设计 |
| 论文 | [Apple Intelligence Foundation Language Models 2025](https://machinelearning.apple.com/research) |
| 最新动态 | AFM 3 "summer" 承诺未兑现（截至 08-17）；上一代 TR 2025-07-17 仍为最新正式报告 |

---

## 12. NVIDIA

| 项 | 值 |
|---|---|
| 最新旗舰 | Nemotron 3 Ultra |
| 发布日期 | 2026-06-09 |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | 550B 总参 / 55B 激活（MoE Hybrid Mamba-Attention） |
| 上下文窗口 | 1M |
| 架构创新 | Hybrid Mamba-Attention（线性复杂度 + 全注意力混合）；550B MoE；1M 超长上下文 |
| 核心贡献 | 首个超大规模 Hybrid Mamba-Attention MoE；面向 always-on agent 场景 |
| 论文 | [Nemotron 3](https://developer.nvidia.com/blog/nemotron-3-ultra/) |
| 最新动态 | Nemotron 3.5 Lightning（08-11）：30B-A3B 开放 MoE，面向 always-on agents；Nemotron 3 家族（Ultra/Super/Nano）保留 |

---

## 13. xAI

| 项 | 值 |
|---|---|
| 最新旗舰 | Grok 3 Beta |
| 发布日期 | 2025-02-19 |
| 开源状态 | ❌ 闭源 |
| 核心参数 | 未公开（基于 Grok 3 架构，Colossus 集群训练） |
| 架构创新 | RL 推理（reasoning via RL）；Colossus 超算集群（100K H100） |
| 核心贡献 | Chatbot Arena Elo 1402（截至 02-19）；超算规模训练验证 |
| 论文 | 未发布正式技术报告 |
| 最新动态 | Grok 4.6 约 08-07 上线（第三方确认），1.5T 参数，SFT+RL 大幅升级；但 xAI 官方 docs.x.ai 目录仍仅列 grok-4.5，无 model card；Grok 4.7（2.1T）计划 3-4 周后 |

---

## 14. Amazon (AWS)

| 项 | 值 |
|---|---|
| 最新旗舰 | Nova 家族（Pro / Lite / Micro / Canvas / Reel） |
| 发布日期 | 2024 |
| 开源状态 | ❌ 闭源 |
| 架构创新 | 多模态家族（文本/图像/视频生成）；端到端多模态理解 |
| 核心贡献 | AWS 原生 LLM 生态布局；多模态全家桶覆盖 |
| 论文 | [Amazon Nova Technical Report](https://www.amazon.science/publication/amazon-nova) |
| 最新动态 | Nova TR 2024 仍唯一正式报告；re:Invent 2026 为下一观察点 |

---

## 15. Zhipu AI (智谱清言)

| 项 | 值 |
|---|---|
| 最新旗舰 | GLM-5 / GLM-5.2 |
| 发布日期 | 2026-02-17（GLM-5） |
| 开源状态 | ✅ 开放权重（部分） |
| 核心参数 | GLM-5.2: 744B MoE / 约 40B 激活 |
| 上下文窗口 | 1M |
| 架构创新 | DSA（DeepSeek Sparse Attention）稀疏注意力；异步 RL 基础设施；异步 Agent RL 算法；端到端软件工程 |
| 核心贡献 | 国产芯片完全适配；GLM-5.2 成本约 1/6 GPT-5.5；GLM-4.7 预算默认（SWE-bench Verified 73.8%） |
| 论文 | [GLM-5 Technical Report](https://zhipuai.github.io/) |
| 最新动态 | GLM-5.3 口径转向（JPMorgan 8 月 >1T + 新浪财经 07-20）；GLM-5.5 为传闻未确认；GLM-5.2 仍为确认旗舰 |

---

## 16. InternLM (书生系列)

| 项 | 值 |
|---|---|
| 最新旗舰 | Intern-S1-Pro |
| 发布日期 | 2026-03 |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | 1T 参数（科学多模态） |
| 架构创新 | 科学多模态架构；100+ 科学任务覆盖 |
| 核心贡献 | 首个万亿级科学多模态模型；书生·端砚平台 |
| 论文 | [InternLM Technical Report](https://InternLM.github.io/) |
| 最新动态 | Intern-S2-Preview-397B 于 WAIC 2026（07-01）以 397B 追平此前万亿模型；InternLM3-8B-Instruct（01-15，4T tokens，训练成本 -75%）+ InternThinker + InternBootCamp 仍为最新公开成果 |

---

## 17. Moonshot AI (月之暗面)

| 项 | 值 |
|---|---|
| 最新旗舰 | Kimi K3 |
| 发布日期 | 2026-07 |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | 2.8T 总参 / 104B 激活（MoE） |
| 上下文窗口 | 1M |
| 架构创新 | 原生视觉理解（native vision）；MoE 架构；2.8T 规模 |
| 核心贡献 | 开源 MoE 最大规模之一（2.8T 总参）；按期放权建立信用 |
| 论文 | [Kimi K3 Technical Report](https://kimi.moonshot.cn/) |
| 最新动态 | Kimi K4 训练传闻（The Information 07-28/29，寻求更多 NVIDIA Blackwell 芯片）；K3 全量权重 + 47 页技术报告（07-27）仍为最新；Kimi Code CLI 0.34.0（08-06） |

---

## 18. StepFun (阶跃星辰)

| 项 | 值 |
|---|---|
| 最新旗舰 | Step-DeepResearch / Step 3 |
| 发布日期 | 2025-12-23（Step-DeepResearch）/ 2025-07-31（Step 3） |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | Step-DeepResearch: 32B；Step 3: 321B 总参 / 38B 激活（MoE） |
| 架构创新 | Step-DeepResearch: 深度研究 Agent（ADR-Bench 标准制定者）；Step 3: 稀疏 MoE；Step3-VL-10B: PaCoRe 多模态 |
| 核心贡献 | 深度研究 Agent 方向引领；321B 开源 MoE |
| 论文 | [Step 3 Technical Report](https://www.stepfun.com/) |
| 最新动态 | Step 3.7 Flash（196B+1.8B/11B，400 tok/s，~2026-03，single-source）；⚠️ 修正 08-12 页"198B"为官方 321B/38B |

---

## 19. ByteDance (字节跳动)

| 项 | 值 |
|---|---|
| 最新旗舰 | Seed 2.0 系列（Pro / Lite / Mini / Code） |
| 发布日期 | 2026-02-14 |
| 开源状态 | ❌ 闭源（API 通过火山引擎） |
| 核心参数 | Pro / Lite / Mini 三档；Code 专用模型 |
| 架构创新 | Agent 级长链推理（long-chain reasoning）；Omni-modal understanding（视频/图像/音频/文本统一）；端到端实时交互与应用生成 |
| 核心贡献 | 155M 周活用户（Doubao，全球第 4 大 GenAI 应用）；春节峰值 ~145M DAU；SuperGPQA 超越 GPT-5.2 |
| 论文 | [Seed 2.0 Launch](https://seed.bytedance.com/en/blog/seed-2-0-official-launch) |
| 最新动态 | Seed2.1 Model Card（Pro + Turbo，Agent/代码工程，视频理解多评测 SOTA 含小时级长视频）；Seedream 3.0 图像生成（04-11，MMDiT + Cross-modality RoPE，4-8× 加速）；>5T/10T 参数新模型训练传闻（晚点 >5T vs FT 10T，预训练早期 3-6 个月）；张一鸣 Seed 全员会反对蒸馏（"复制 Claude 能力难超越"） |

---

## 交叉观察

### 架构趋势

| 趋势 | 代表公司 | 说明 |
|------|---------|------|
| MoE 统治 | DeepSeek/Qwen/Mistral/ByteDance/Kimi/NVIDIA/StepFun/GLM | 19 家中 8 家采用 MoE，总参 >1T 成标配 |
| Hybrid Attention | NVIDIA（Mamba-Attention）/ DeepSeek（V4 CSA） | 线性复杂度 + 全注意力混合 |
| 原生多模态 | Meta Llama 4 / Google Gemini / ByteDance Seed | 文本/图像/音频/视频统一训练 |
| Thinking 范式 | OpenAI / Anthropic / Google / Qwen | 内置推理链 + 直接回答双模式 |
| 端侧部署 | Apple（2-bit 量化）/ NVIDIA（3.5 Lightning）/ Qwen（0.6B） | 端侧 LLM 进入量产阶段 |

### 开放 vs 闭源格局

| 类型 | 公司 |
|------|------|
| 开放权重 | DeepSeek, Meta, Mistral, Qwen, Yi, Microsoft, Baichuan, NVIDIA, Zhipu, InternLM, Moonshot, StepFun |
| 闭源 | OpenAI, Google, Anthropic, Apple, Amazon, xAI, ByteDance |

### "承诺→兑现"信用追踪

| 承诺 | 状态 | 备注 |
|------|------|------|
| Meta 405B 开放权重 | ❌ 未兑现（08-11 起记录） | NeuralStack/Bloomberg 预告口径无发布实据 |
| Qwen3.8-Max 权重 | ❌ 验收日未兑现（08-12） | HF 无条目，license 争议 |
| Apple AFM 3 "summer" | ❌ 未兑现（截至 08-17） | 上一代 TR 2025-07-17 仍为最新 |
| Moonshot K3 放权 | ✅ 按期兑现（07-27） | 47 页技术报告 + 全量权重 |
| DeepSeek V4 Pro GA | ✅ 兑现（08-13） | OpenRouter 上架 |
| Nemotron 3 Ultra | ✅ 兑现（06-09） | 家族报告齐备 |

### 规模军备竞赛

| 公司 | 规模 | 状态 |
|------|------|------|
| ByteDance | >5T–10T | 预训练早期（3-6 个月） |
| xAI Grok 4.7 | 2.1T | 计划 3-4 周后 |
| Moonshot K4 | 未公开 | 训练中 |
| Zhipu GLM-5.3 | >1T | 传闻 |
| Qwen3.8-Max | 2.4T | 已发布权重（08-12 验收） |
| Kimi K3 | 2.8T | 已发布 |
| NVIDIA Nemotron 3 Ultra | 550B | 已发布 |

---

*Generated 2026-08-17. Source: Web search results. Cross-referenced with wiki/synthesis/2026-08-13/tech-report-digest.md and wiki/synthesis/2026-08-12/tech-report-digest.md.*
