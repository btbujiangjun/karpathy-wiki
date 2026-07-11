---
title: "AI Papers Compilation: June-July 2026"
type: synthesis
created: 2026-07-11
updated: 2026-07-11
sources: [web-search-results.md]
tags: [LLM, agents, code-generation, recommendation, diffusion, flow-matching, benchmarks, evaluation, sequential-modeling]
---

# AI Papers Compilation: June-July 2026

## Overview

Comprehensive compilation of the most impactful AI papers and model releases from June-July 2026, organized by topic. Covers work from Google DeepMind, OpenAI, Meta AI, Anthropic, ByteDance, Alibaba, NVIDIA, DeepSeek, and leading academic institutions.

---

## 1. LLMs — Training, Inference, Scaling, Alignment

### P1. DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **Title (CN):** DeepSeek-V4：迈向高效百万Token上下文智能
- **Authors:** DeepSeek-AI (230+ authors)
- **Affiliation:** DeepSeek
- **Venue:** arXiv, April 2026
- **Summary:** Introduces DeepSeek-V4-Pro (1.6T params, 49B active) and DeepSeek-V4-Flash (284B params, 13B active), both supporting 1M token context. Builds on MLA + DeepSeekMoE innovations from V2/V3. Major efficiency gains in both training and inference.
- **Link:** https://arxiv.org/abs/2606.19348

### P2. GPT-5.6 (Sol, Terra, Luna) — OpenAI
- **Title (CN):** GPT-5.6（Sol, Terra, Luna）
- **Authors:** OpenAI Team
- **Affiliation:** OpenAI
- **Venue:** Public release, July 9, 2026
- **Summary:** Three tiers: Sol (flagship with Ultra subagent mode, Max reasoning-effort), Terra (GPT-5.5 quality at half cost), Luna (fast tier). All run on ~4T-parameter Spud pretrain. ARC-AGI-3 Sol scored 7.8%. First model to beat a public game. 700+ tokens/sec on Cerebras.
- **Link:** https://openai.com/research/

### P3. Muse Spark 1.1 — Meta AI
- **Title (CN):** Muse Spark 1.1 与 Meta 模型 API
- **Authors:** Meta AI Team
- **Affiliation:** Meta AI
- **Venue:** Public release, July 9, 2026
- **Summary:** 1M-token-context agentic model rivaling GPT-5.5/Opus 4.8 on agentic evals. #1 on MCP Atlas, JobBench, Humanity's Last Exam, Finance Agent V2. Meta's first paid developer API ($20 free credits). Computer use across desktop, browser, mobile.
- **Link:** https://ai.meta.com/blog/introducing-muse-spark-msl/

### P4. Claude Sonnet 5 — Anthropic
- **Title (CN):** Claude Sonnet 5
- **Authors:** Anthropic Team
- **Affiliation:** Anthropic
- **Venue:** Public release, June 30, 2026
- **Summary:** Frontier performance across coding, agents, and professional work at scale. Part of the Claude 5 family alongside Fable 5 (red-teaming release). Anthropic also published interpretability research on emergent mental workspace (July 6).
- **Link:** https://www.anthropic.com/news

### P5. Gemma 4 Technical Report
- **Title (CN):** Gemma 4 技术报告
- **Authors:** Gemma Team, Google DeepMind
- **Affiliation:** Google DeepMind
- **Venue:** arXiv:2607.02770, June 2026
- **Summary:** Open-weight natively multimodal models (2.3B–31B params, plus MoE 3.8B/26B). Unified encoder-free architecture for 12B model. Thinking mode integration. Leap in STEM, multimodal, and long-context benchmarks.
- **Link:** https://arxiv.org/abs/2607.02770

### P6. Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs
- **Title (CN):** Scaling Law 与模型架构的结合：面向推理高效的 LLM
- **Authors:** Song Bian, Tao Yu, Shivaram Venkataraman, Youngsuk Park
- **Affiliation:** University/Industry
- **Venue:** ICLR 2026, arXiv:2510.18245
- **Summary:** Conditional scaling law augmenting Chinchilla with architectural info. 200+ models (80M–3B params) trained. Optimized architectures achieve 2.1% higher accuracy and 42% greater inference throughput vs LLaMA-3.2.
- **Link:** https://arxiv.org/abs/2510.18245

### P7. Qwen ParScale — Parallel Scaling Law
- **Title (CN):** 并行 Scaling Law：超越参数和推理时间扩展
- **Authors:** Qwen Team
- **Affiliation:** Alibaba (Qwen)
- **Venue:** arXiv:2505.10475
- **Summary:** Third scaling paradigm: parallel computation during training/inference. P diverse transformations run in parallel with dynamic aggregation. Logarithmic scaling law: parallel streams comparable to scaling params by O(log P).
- **Link:** https://github.com/QwenLM/ParScale

### P8. Federation of Experts: Communication Efficient Distributed Inference
- **Title (CN):** 专家联邦：LLM 的通信高效分布式推理
- **Authors:** (Multiple)
- **Affiliation:** Industry
- **Venue:** arXiv:2605.06206, 2026
- **Summary:** Restructures MoE into clusters with one KV head per cluster. Eliminates all-to-all communication. 5.2x forward-pass latency reduction, 3.62x TTFT reduction, 1.95x TBT reduction on LongBench.
- **Link:** https://arxiv.org/abs/2605.06206

### P9. A3: Automated Alignment Agent for Safety Finetuning
- **Title (CN):** A3：用于安全微调的自动对齐 Agent
- **Authors:** Jifan Zhang, Henry Sleight, Joe Benton
- **Affiliation:** Anthropic
- **Venue:** March 2026
- **Summary:** Agentic framework for automated safety alignment. Adaptively generates training data, performs iterative finetuning with weighted mixing strategy. Open-sourced.
- **Link:** https://alignment.anthropic.com/2026/automated-alignment-agent/

### P10. Anthropic Global Workspace in Language Models
- **Title (CN):** 语言模型中的全局工作空间
- **Authors:** Anthropic Interpretability Team
- **Affiliation:** Anthropic
- **Venue:** July 6, 2026
- **Summary:** Reveals emergent mental workspace in Claude holding internal thoughts not appearing in output. Major interpretability breakthrough.
- **Link:** https://www.anthropic.com/research

---

## 2. Agent Systems / Tool Use / Multi-Agent

### P11. The Evolution of Tool Use in LLM Agents
- **Title (CN):** LLM Agent 中工具使用的演进：从单一调用到多工具编排
- **Authors:** He T., Liu X., Wang Z., et al.
- **Affiliation:** Harbin Institute of Technology + others
- **Venue:** arXiv:2603.22862, March 2026
- **Summary:** Comprehensive review organizing around 6 dimensions: inference-time planning, training/trajectory construction, safety/control, efficiency, capability completeness, benchmarks.
- **Link:** https://arxiv.org/abs/2603.22862

### P12. Scaling Parallel Tool Calling for Efficient Deep Research
- **Title (CN):** 扩展并行工具调用实现高效深度研究 Agent
- **Authors:** (Referenced in Zylos Research survey)
- **Affiliation:** Industry
- **Venue:** arXiv:2602.07359, February 2026
- **Summary:** Scaling along width dimension achieves 4x speedup in agentic search vs sequential execution. All parallel calls reasoned about in same model turn.
- **Link:** https://arxiv.org/abs/2602.07359

### P13. Self-Evolving Recommendation System with LLM Agents (YouTube)
- **Title (CN):** 自进化推荐系统：基于 LLM Agent 的端到端自主模型优化
- **Authors:** Haochen Wang, Yi Wu, et al.
- **Affiliation:** Google (YouTube)
- **Venue:** arXiv:2602.10226, February 2026
- **Summary:** Uses Gemini LLMs to autonomously generate, train, and deploy model changes. Offline Agent (inner loop) for hypothesis generation; Online Agent (outer loop) for production validation.
- **Link:** https://arxiv.org/abs/2602.10226

### P14. Bridging Protocol and Production: MCP Design Patterns
- **Title (CN):** 连接协议与生产：MCP 的设计模式
- **Authors:** Vasundra Srinivasan
- **Affiliation:** Enterprise
- **Venue:** arXiv:2603.13417, March 2026
- **Summary:** Identifies 3 missing MCP primitives: identity propagation, adaptive tool budgeting, structured error semantics. Proposes CABP, ATBA, SERF frameworks.
- **Link:** https://arxiv.org/abs/2603.13417

### P15. Deep Research for Recommender Systems (RecPilot)
- **Title (CN)：** 推荐系统的深度研究（RecPilot）
- **Authors:** Kesha Ou, Chenghao Wu, et al.
- **Affiliation:** Renmin University
- **Venue:** arXiv:2603.07605, March 2026
- **Summary:** Multi-agent framework replacing item lists with comprehensive user-centric reports. User trajectory simulation + self-evolving report generation.
- **Link:** https://arxiv.org/abs/2603.07605

---

## 3. Code Generation & Code Execution

### P16. EAGER: Executing as You Generate
- **Title (CN)：** 边生成边执行：隐藏 LLM 代码解释器的执行延迟
- **Authors:** Zhensu Sun, Zhihao Lin, et al.
- **Affiliation:** Singapore Management University
- **Venue:** arXiv:2604.00491, April 2026
- **Summary:** Pipeline for overlapping code generation with execution. AST-based chunking, dynamic batching. Hides up to 99.8% of execution time; 37.3% end-to-end latency reduction.
- **Link:** https://arxiv.org/abs/2604.00491

### P17. SolidCoder: Bridging Mental-Reality Gap in LLM Code Generation
- **Title (CN)：** SolidCoder：弥合 LLM 代码生成中的思维与现实差距
- **Authors:** (Multiple)
- **Affiliation:** Multiple
- **Venue:** arXiv:2604.19825, April 2026
- **Summary:** Integrates live execution into generation loop. Oracle-based assertions, Defensive Accumulation prevents bug regression. Components: Shift-left Planning, Live Execution, Debug, Defensive Accumulation.
- **Link:** https://arxiv.org/abs/2604.19825

### P18. SWE-Bench Verified Leaderboard (May 2026)
- **Title (CN)：** SWE-Bench Verified 排行榜
- **Summary:** Top agents: Claude Code (Opus 4.7) ~78%, OpenAI Codex agent (GPT-5 Pro) ~76%, Cursor Agent ~67%. Benchmark approaching saturation. Real-world PR pass rates estimated 35-50%.
- **Link:** https://www.swebench.com/

### P19. CUDA Agent: Large-Scale Agentic RL for CUDA Kernel Generation
- **Title (CN)：** CUDA Agent：面向高性能 CUDA 内核生成的大规模 Agentic RL
- **Authors:** ByteDance Seed Team
- **Affiliation:** ByteDance
- **Venue:** arXiv, February 2026
- **Summary:** Agentic reinforcement learning for automated high-performance CUDA kernel generation.
- **Link:** https://seed.bytedance.com/en/public_papers

---

## 4. Recommendation Systems

### P20. ULTRA-HSTU: Bending the Scaling Law Curve (Meta)
- **Title (CN)：** ULTRA-HSTU：弯曲大规模推荐系统的 Scaling Law 曲线
- **Authors:** Qin Ding, Kevin Course, et al.
- **Affiliation:** Meta
- **Venue:** arXiv:2602.16986, February 2026
- **Summary:** Semi-Local Attention (linear sparse), input sequence optimization, dynamic topology. 5x training scaling and 21x inference scaling efficiency vs conventional models. 4-8% consumption/engagement improvement.
- **Link:** https://arxiv.org/abs/2602.16986

### P21. Kunlun: Scaling Laws for Massive-Scale Recommendation (Meta)
- **Title (CN)：** 昆仑：大规模推荐系统的 Scaling Law
- **Authors:** Bojian Hou, Xiaolong Liu, et al.
- **Affiliation:** Meta
- **Venue:** arXiv:2602.10016, February 2026
- **Summary:** Unified architecture with predictable power-law scaling. GDPA, Hierarchical Seed Pooling, Sliding Window Attention. MFU increased from 17% to 37% on NVIDIA B200. Deployed in Meta Ads.
- **Link:** https://arxiv.org/abs/2602.10016

### P22. LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling (Meta)
- **Title (CN)：** LLaTTE：大规模广告推荐中多阶段序列建模的 Scaling Law
- **Authors:** Meta Team
- **Affiliation:** Meta
- **Venue:** arXiv:2601.20083, 2026
- **Summary:** Power-law scaling for ads recommendation; two-stage async architecture; largest user model at Meta.
- **Link:** https://arxiv.org/abs/2601.20083

### P23. MDL: Unified Multi-Distribution Learner (ByteDance/Douyin)
- **Title (CN)：** MDL：通过 Tokenization 实现大规模工业推荐中的统一多分布学习
- **Authors:** Shanlei Mu, Yuchen Jiang, et al.
- **Affiliation:** ByteDance
- **Venue:** arXiv:2602.07520, February 2026
- **Summary:** "Tokenize-and-Interact" paradigm. Domain-aware attention for scenario/task-adaptive activation. Deployed on Douyin Search: +0.0626% LT30 improvement.
- **Link:** https://arxiv.org/abs/2602.07520

### P24. Efficient Sequential Recommendation via Personalization (Meta)
- **Title (CN)：** 通过个性化实现高效长期用户兴趣序列推荐
- **Authors:** Qiang Zhang et al.
- **Affiliation:** Meta (FAIR)
- **Venue:** ICDM 2025, arXiv:2601.03479
- **Summary:** Compresses long histories into learnable tokens. Applied to HSTU and HLLM. Reduces computational costs significantly while maintaining accuracy. Open-sourced.
- **Link:** https://arxiv.org/abs/2601.03479

### P25. Multi-Behavior Sequential Modeling with TGA (Alibaba)
- **Title (CN)：** 基于转换感知图注意力网络的多行为序列建模
- **Authors:** Hanqi Jin, Gaoming Yang, et al.
- **Affiliation:** Alibaba
- **Venue:** arXiv:2601.14955, January 2026
- **Summary:** Linear-complexity approach for multi-behavior transitions. Structured sparse graph from item/category/neighbor-level transitions.
- **Link:** https://arxiv.org/abs/2601.14955

### P26. ByteDance CTR Scaling Papers (2026 Cluster)
- **Key papers:**
  - **HyFormer** (arXiv:2601.12681, SIGIR 2026) — Sequence modeling vs feature interaction
  - **TokenMixer-Large** (arXiv:2602.06563, KDD 2026) — Scaling up ranking models
  - **MixFormer** (arXiv:2602.14110) — Co-scaling dense and sequence features
  - **MSN** (arXiv:2602.07526) — Sparse activation via Product-Key Memory

---

## 5. Generative Models (Diffusion, Flow Matching)

### P27. DiffusionGemma — Google DeepMind + NVIDIA
- **Title (CN)：** DiffusionGemma：Google 的 4x 更快文本扩散模型
- **Authors:** Google DeepMind + NVIDIA
- **Affiliation:** Google DeepMind, NVIDIA
- **Venue:** June 10, 2026, Apache 2.0
- **Summary:** First major open-source text diffusion model. MoE 26B total / 3.8B active. Uniform State Diffusion generates all tokens in parallel. 1,000+ tokens/sec on consumer RTX GPUs.
- **Link:** https://deepmind.google/models/gemini-diffusion

### P28. Nemotron-Labs Diffusion Language Models (NVIDIA)
- **Title (CN)：** Nemotron-Labs 扩散语言模型
- **Authors:** NVIDIA Team
- **Affiliation:** NVIDIA
- **Venue:** May 23, 2026
- **Summary:** Tri-mode: plain autoregressive, diffusion mode (FastDiffuser), self-speculation (LinearSpec). ~865 tok/s on B200 — 4x AR baseline. Lossless at temperature 0.
- **Link:** https://huggingface.co/blog/nvidia/nemotron-labs-diffusion

### P29. LLaDA2.0-Uni: Unifying Multimodal Understanding & Generation
- **Title (CN)：** LLaDA2.0-Uni：用扩散大语言模型统一多模态理解与生成
- **Authors:** Yi Xin et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2604.20796, April 2026
- **Summary:** Unified discrete diffusion LLM with SigLIP-VQ tokenizer, MoE backbone, diffusion decoder. Block-level masked diffusion for text and images.
- **Link:** https://arxiv.org/abs/2604.20796

### P30. Survey on Diffusion Language Models
- **Title (CN)：** 扩散语言模型综述
- **Authors:** Tianyi Li, Mingda Chen, et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2508.10875, updated June 2026
- **Summary:** Comprehensive taxonomy of DLMs: pre-training, post-training, inference optimizations, multimodal extensions. GitHub: VILA-Lab/Awesome-DLMs.
- **Link:** https://arxiv.org/abs/2508.10875

### P31. Alignment of Diffusion Model and Flow Matching for Text-to-Image
- **Title (CN)：** 扩散模型与 Flow Matching 的对齐
- **Authors:** Yidong Ouyang et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2602.00413, January 2026
- **Summary:** Unifies alignment framework for diffusion and flow matching. Finetuning-free guidance network achieves comparable performance with 60%+ compute reduction.
- **Link:** https://arxiv.org/abs/2602.00413

### P32. FluidFlow: Flow-Matching for Fluid Dynamics Surrogates
- **Title (CN)：** FluidFlow：面向流体动力学代理的 Flow-Matching 生成模型
- **Authors:** David Ramos et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2604.08586, March 2026
- **Summary:** Conditional flow-matching generative model for CFD on structured/unstructured meshes. U-Net and DiT architectures.
- **Link:** https://arxiv.org/abs/2604.08586

---

## 6. Sequential Modeling

### P33. MealRec: Multi-granularity Sequential Modeling via Hierarchical Diffusion
- **Title (CN)：** MealRec：通过层次扩散模型实现多粒度序列建模的微视频推荐
- **Authors:** Xinxin Dong, Haokai Ma, et al.
- **Affiliation:** NUDT + NUS
- **Venue:** arXiv:2603.01926, March 2026
- **Summary:** Temporal-guided Content Diffusion for video representation refinement + Noise-unconditional Preference Denoising for user preference recovery.
- **Link:** https://arxiv.org/abs/2603.01926

### P34. GTS: Transformer-Based Sequential Recommendation
- **Title (CN)：** GTS：基于 Transformer 的序列推荐
- **Authors:** Multiple
- **Affiliation:** Multiple
- **Venue:** EmergentMind compilation, updated April 2026
- **Summary:** Reformulates sequential rec as autoregressive next-item generation with decoder-only transformers. RA aggregation delivers up to 21.5% NDCG@10 improvement.
- **Link:** https://www.emergentmind.com/topics/sequential-recommendation-gts

### P35. SAGE: Global Semantic Alignment with LLMs for Long-Tail Sequential Rec
- **Title (CN)：** SAGE：用 LLM 全局语义对齐实现长尾序列推荐
- **Authors:** City University of Hong Kong team
- **Affiliation:** City University of Hong Kong
- **Venue:** WWW 2026
- **Summary:** Fuzzy-membership prototype mechanism enables tail items to inherit features from semantically related head items. Cross-user semantic alignment/distillation.
- **Link:** https://dl.acm.org/doi/10.1145/3774904.3792456

### P36. OD-LLM: On-Device LLMs for Sequential Recommendation
- **Title (CN)：** OD-LLM：面向设备端 LLM 的序列推荐压缩框架
- **Authors:** University of Queensland
- **Affiliation:** University of Queensland
- **Venue:** arXiv:2601.09306, WSDM 2026
- **Summary:** First compression framework for on-device LLM-based sequential rec. 2x model size reduction, zero accuracy loss at 2x compression.
- **Link:** https://arxiv.org/abs/2601.09306

---

## 7. Benchmarks and Evaluation

### P37. Benchmark²: Systematic Evaluation of LLM Benchmarks
- **Title (CN)：** Benchmark²：LLM 基准测试的系统性评估
- **Authors:** Qi Qian, Chengsong Huang, et al.
- **Affiliation:** Fudan University + others
- **Venue:** arXiv:2601.03986, January 2026
- **Summary:** Three metrics: Cross-Benchmark Ranking Consistency, Discriminability Score, Capability Alignment Deviation. Selective benchmark achieves comparable evaluation with 35% of original data.
- **Link:** https://arxiv.org/abs/2601.03986

### P38. TimeSage-MT: Multi-Turn Benchmark for Agentic Time Series Reasoning
- **Title (CN)：** TimeSage-MT：用于 Agentic 时间序列推理的多轮基准测试
- **Authors:** Yaxuan Kong, Qingren Yao, et al.
- **Affiliation:** Oxford + multiple
- **Venue:** arXiv, June 2026
- **Summary:** Evaluates whether LLM agents can conduct reliable time series analysis across multi-turn conversations.
- **Link:** https://arxiv.org/abs/2606.00065

### P39. Cookie-Bench: Continuous On-screen Key Interaction Evaluation
- **Title (CN)：** Cookie-Bench：Web 生成的连续屏幕按键交互评估
- **Authors:** Haoyue Yang et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2505.30000, May 2026
- **Summary:** Benchmark for evaluating web page generation quality through continuous on-screen interaction patterns.
- **Link:** https://arxiv.org/abs/2505.30000

### P40. Google DeepMind ProEval
- **Title (CN)：** ProEval：生成式 AI 评估的主动失败发现与高效性能估计
- **Authors:** Google DeepMind
- **Affiliation:** Google DeepMind
- **Venue:** April 25, 2026
- **Summary:** Proactive failure discovery framework for generative AI evaluation.
- **Link:** https://deepmind.google/research/publications/238239/

---

## Notable July 2026 Model Releases

| Lab | Model | Date | Key Stats |
|-----|-------|------|-----------|
| **OpenAI** | GPT-5.6 Sol/Terra/Luna | Jul 9 | ~4T params (Spud), $5/$30 per 1M tokens |
| **Meta AI** | Muse Spark 1.1 | Jul 9 | 1M context, #1 on MCP Atlas, first paid Meta API |
| **Anthropic** | Claude Sonnet 5 | Jun 30 | Frontier coding/agents, Fable 5 for red-teaming |
| **Anthropic** | Claude Tag | Jun 23 | Lightweight variant |
| **Google** | Gemma 4 | Jun 19 | 2.3B–31B, MoE 3.8B/26B, thinking mode |
| **Google** | DiffusionGemma | Jun 10 | 26B MoE text diffusion, 1000+ tok/s on RTX |

---

## Related Wiki Pages

- [[attention-is-all-you-need]] — Transformer architecture (foundation for most models above)
- [[scaling-laws-for-neural-language-models]] — Original Chinchilla scaling laws
- [[llama-4-maverick]] — Meta's open model preceding Muse Spark
- [[deepseek-r1]] — DeepSeek's reasoning model preceding V4
- [[constitutional-ai]] — Anthropic's alignment approach underlying Claude models
