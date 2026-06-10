# Log

> Append-only chronological record of all wiki operations.
> Each entry: `## [YYYY-MM-DD] operation | subject`
> Parse with: `grep "^## \[" wiki/log.md | tail -10`

## [2026-06-03] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20
- New page: wiki/synthesis/2026-06-03/wq101-alpha-daily.md
- Applied Alpha#1/#6/#12/#19/#30/#41/#53 across 7 dimensions (momentum, reversal, volatility, volume-price, trend strength, mean reversion)
- Top picks: MU(9), DELL(9), NVDA(8), AVGO(8), INTC(8), SNDK(8), MRVL(8)
- Sectors: 10 Semis, 1 Tech Hardware, 3 Cloud/AI Software, 2 Storage, 1 Industrial, 1 E-Commerce, 1 Healthcare, 1 Consumer Staples
- Market context: S&P 5K at 7,610 (+0.13%), Nasdaq record 27,094, Tech(YTD: +65% XLK) and Energy(YTD: +38% XLE) leading
- Updated: wiki/index.md, wiki/log.md

## [2026-06-08] search | arXiv Daily — AI Research Survey (June 8, 2026)
- New page: wiki/synthesis/2026-06-08/arxiv-daily.md
- Coverage: 37 papers across LLM (9), CTR/RecSys (7), Sequential Recommendation (7), Games/Agents/RL (7), MoE (7)
- Top picks: FLARE (hybrid dLLM), DS-MLP (vanilla MLP SOTA for CTR), LoopCTR (loop scaling), ProbMoE (probabilistic MoE routing), STRATAGEM (game self-play reasoning transfer)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-09] search | arXiv Daily — AI Research Survey (June 9, 2026)
- Updated: wiki/synthesis/2026-06-09/arxiv-daily.md
- Coverage: 26 papers across LLM (11), CTR/Advertising/RecSys (8), Games/RL/Sequential (7)
- Highlights: Perplexity AI empirical agent study, DuMate-DeepResearch (Baidu SOTA multi-agent), GBLA linear attention for generative retrieval (Yandex, SIGIR'26), BitsMoE MoE quantization, DyCon overthinking mitigation, Taiji (Kuaishou LLM-enhanced rec), Hidden Thoughts reasoning trace exposure
- New entries: UniPinRec (Pinterest), Bradley-Terry Rankings (KDD'26), CoMIC collaborative agent memory, CRMA continual fine-tuning, MindZero zero-annotation ToM, CAST GRPO training
- Sources: arXiv cs.AI, cs.CL, cs.IR, cs.LG (Jun 5-8 submissions)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-04] search | arXiv Digest — AI & CTR (June 4, 2026)
- New page: wiki/synthesis/2026-06-04/arxiv-digest.md
- Surveyed: cs.LG (236 entries), cs.IR (27 entries), cs.AI (207 entries) from Thu 4 Jun 2026
- Papers highlighted: ~40 across CTR/Rec, AI/LLM Systems, IR/RAG
- Top picks: DS-MLP (vanilla MLP + KD for CTR), STRIDE (13× faster TDA for LLMs), Rosetta Neuron scaling laws, Sequential Data Poisoning (single-attacker illusion), AutoLab (long-horizon agent benchmark), TMEM (parametric memory for agents)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-03] search | arXiv Digest — AI & CTR (June 3, 2026)
- New page: wiki/synthesis/2026-06-03/arxiv-digest.md
- Surveyed: cs.LG (247 entries, Wed 3 Jun) + cs.IR (20 entries, Wed 3 Jun)
- Papers highlighted: ~30 across CTR/Rec, AI/LLM Systems, IR/RAG
- Top picks: Taiji (POPO, Kuaishou LLM4Rec), UniPinRec (Pinterest unified retrieval+ranking), Dynamic Short Convolutions (1.33× compute advantage), LLMs Need Sleep (memory consolidation), CtM LoRA merging (ICML 2026)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-03] synthesis | 投资日报 — 2026-06-03（美股/港股/A股科技与AI热点）
- Summary: wiki/synthesis/2026-06-03/investment-daily.md
- 美股焦点：COMPUTEX 2026（黄仁勋点石成金 Marvell +32.5%、NVIDIA Cosmos 3、NemoClaw）；Broadcom Q2 FY2026 盘后财报（$220亿+营收预期、AI $107亿）；HPE +19.5% AI需求；Microsoft Build Copilot Agent Mode；S&P 500 历史新高 7,620
- 港股焦点：阿里港股 +6.5% AI重估；腾讯计划 WeChat AI Agent（13亿月活）
- A股焦点：光模块/半导体设备/国产算力持续景气
- 中概：智谱AI/MiniMax 6月8日纳入恒生科技
- AI 主题：Agentic AI（Microsoft/Tencent/OpenAI/Anthropic）、物理 AI（Cosmos 3/NemoClaw）、特朗普 AI 行政令
- New page: wiki/synthesis/2026-06-03/investment-daily.md
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-03] search | Tech Report Digest — 第六版 (2026-06-03)
- New page: wiki/synthesis/2026-06-03/tech-report-digest.md

## [2026-06-03] synthesis | Conference & arXiv Digest — 2026-06-03 全面版
- New page: wiki/synthesis/2026-06-03/conference-digest.md
- Coverage: ICML 2026 (Bi-NAC, ∇-Reasoner, CAPO, f-GRPO, LAD, LambdaPO, KnowRL, Spectra, CraEG, Hierarchical Language Model, NSHA, AWARE), ICLR 2026 (GNN-as-Judge), KDD 2026 (FAT, MGOE), WWW 2026 (SparseCTR, GenCI, MoS), SIGIR 2026 (GenRec, OneRanker), CIKM 2026 (MuChator), RecSys 2025 (LONGER), ACL 2025 (ActorBreaker), Industry papers: ByteDance (TokenMixer-Large, HyFormer), Alibaba (EST), Tencent (RankUp, HeMix), Meta (Kunlun), Anthropic (Constitutional Classifiers++, Emotion Concepts, Introspective Awareness), Agent systems (DeepAgent, MetaAgent-X, AgentConductor, OpenSage), Game AI (OpenGame, PORTAL, AutoHarness), Video generation (Bernini, Self Forcing, SCD, GPDiT, ARLON), Benchmarks (ParaConsist)
- Lab distribution: ByteDance AML(5), Alibaba(3), Tencent/Weixin(3), Meta Ads(1), Anthropic(3), JD.com(1)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-03] search | arXiv Daily — AI Research Survey (June 3, 2026)
- New page: wiki/synthesis/2026-06-03/arxiv-daily.md
- Surveyed: cs.AI, cs.LG, cs.IR, cs.CL — May 22 – June 2, 2026
- Papers highlighted: ~28 across LLM Architecture (7), Sequential Modeling (7), RecSys/CTR/Ads (9), Games/RL (7), Theory (1)
- Institutions covered: Meta, LinkedIn, Kuaishou, Tencent(×2), Baidu, Alibaba, Xiaohongshu, LMU Munich, RightNow AI
- Updated: wiki/index.md, wiki/log.md
- Coverage: 20 institutions, 35+ reports
- Highlights: DeepSeek V4 (1.6T MoE, CSA/HCA, Muon), GPT-5.5 (Agentic Coding), GLM-5 (Agentic Engineering, 744B MoE), Kimi K2.6 (1T MoE, 300-Agent Swarm), Doubao Seed 2.0 (AIME 98.3), Nemotron 3 (Mamba2-Transformer Hybrid MoE), Qwen3.5 (397B MoE, Apache 2.0), Qwen3.7 Max (1M context), Gemini 3.5 Flash, Claude Opus 4/4.5/4.7, Mistral 3, Step 3.7 Flash
- Key themes: MoE domination, reasoning models as standard, post-training innovation, context length race (up to 10M), open-source maturity, Chinese vs Western pricing gap
- Updated: wiki/index.md, wiki/log.md

## [2026-06-01] search | arXiv Paper Check — AI & CTR (June 1, 2026)
- New page: wiki/synthesis/2026-06-01/arxiv-paper-check.md
- Sources: Mon 1 Jun 2026 cs.AI (226 entries) + cs.IR (19 entries) + cs.LG (264 entries), plus Fri 29 May late postings
- Papers surveyed: ~20

## [2026-06-02] search | arXiv Paper Check — AI & CTR (June 2, 2026)
- New page: wiki/synthesis/2026-06-02/arxiv-paper-check.md
- Sources: Mon 1 Jun 2026 cs.AI (36 new) + cs.IR (12 new) + cs.LG (171 new)
- Papers surveyed: ~25
- CTR highlights: Rec-Distill (24B teacher distillation), Scaling CVR Prediction (+2.6% gain), SaFeAU/KDD, Graph-GRPO, ACE/SIGIR, UniNote/KDD Ads, FOSTER
- AI highlights: AutoSci (full research lifecycle agent), LinTree (explicit search histories for LLM reasoning), UniScale/ICML (unified routing+TTS), COLLEAGUE.SKILL (skill distillation), DecomposeR (planner-centric deep research RL)
- IR highlights: SPECTRA (synthetic IR test collections), Factual Density for RAG (medical), No More K-means/ICML, FLASH-MAXSIM, Latent Terms
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-01] search | 投资日报 — 2026-06-01（美股/港股/A股科技与AI热点）
- New page: wiki/synthesis/2026-06-01/investment-daily.md
- Covers: US Mag 7 & AI stocks (NVDA, AVGO, DELL, GOOGL, MSFT, AAPL, META, TSLA, MU, AMD), A-share AI concept (华为昇腾产业链/光模块/半导体设备/算力), HK/Chinese stocks, AI hot themes (Agentic AI, Coding Agent, Physical AI, Edge AI, AI Safety)
- Key events: NVIDIA COMPUTEX 2026 keynote, Broadcom Q2 earnings (June 3), Dell blowout earnings, Anthropic $30B ARR
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-05-29] search | arXiv Daily — AI & CTR (May 28, 2026)
- New page: wiki/synthesis/2026-05-28/arxiv-daily.md
- Sources: Thu, 28 May 2026 cs.AI (372 entries) + cs.IR (39 entries)
- Papers covered: 11 (6 AI + 5 CTR/RecSys)
- Highlights: CORE (rapid reasoning via contrastive reflection), Thinking as Compression, AutoScientists (decentralized scientific agent teams), CCO (scalable agent oversight), DeepMind AGI Cognitive Framework, UFRec sequential rec, LLM ads predictor, context rank-aware decomposition +87.5% throughput
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-05-28] search | Conference Digest — 2026年5月全面版（顶会论文专题报告）
- New page: wiki/synthesis/2026-05-28/conference-digest.md
- Sources: NeurIPS 2025 (Best Papers + Runners-Up + Test of Time), ICLR 2026 (Outstanding Papers), AAAI 2026, ICML 2026, CVPR 2026, EMNLP 2025, KDD 2025, RecSys 2025, SIGIR 2026
- Highlights: Gated Attention (Alibaba Qwen), Artificial Hivemind (UW/Allen AI), 1000-Layer RL, Diffusion Memorization Theory, Transformers Succinctness (ICLR 2026 Outstanding), LLMs in Multi-Turn (ICLR 2026 Outstanding), SAM 3D (CVPR 2026 Best Paper), ReconVLA/VLA-Adapter (AAAI 2026 Oral), RLVR critique (NeurIPS 2025 Runner-Up)
- Covers 9 conferences, ~70+ papers referenced
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-05-25] refactor | Reorganized index.md by categories
- Papers section restructured into 8 research categories (LLM Training, RecSys, Agents, Games, Generative, Code, Sequential, Benchmarking)
- All 35 paper pages enhanced with detailed format (中文标题、问题背景、方法详述、创新点、实验结果对比表格)
- Old Game/RL papers also integrated into the category structure
- Updated: wiki/index.md

## [2026-05-25] ingest | arXiv Daily — 27 Papers from May 25 Digest
- Source: wiki/synthesis/2026-05-25/arxiv-daily.md
- New paper pages: 27
  - wiki/papers/llm-training/shannon-scaling-law.md, wiki/papers/llm-training/strong-teacher-distillation.md
  - wiki/papers/llm-training/complete-mue-moe.md, wiki/papers/llm-training/diladiff-diffusion-lm.md
  - wiki/papers/llm-training/training-free-looped-transformers.md
  - wiki/papers/recommendation/tubifm-ranking.md, wiki/papers/recommendation/netflix-generative-recommender-scaling.md
  - wiki/papers/recommendation/harness-lm-bing-ads.md, wiki/papers/recommendation/linkedin-llm-ad-retrieval.md
  - wiki/papers/recommendation/rporec-reasoning-recommendation.md, wiki/papers/recommendation/airbnb-llm-synthetic-data.md
  - wiki/papers/recommendation/rankelastor-recommendation.md, wiki/papers/agents/skillopt-agent-skills.md
  - wiki/papers/games/pcsp-npc-shared-rl.md, wiki/papers/games/genstrat-strategic-reasoning.md
  - wiki/papers/agents/foundation-protocol-agents.md, wiki/papers/agents/autoresearch-ai.md
  - wiki/papers/agents/inductive-deductive-synthesis.md, wiki/papers/agents/eve-agent-self-evolving.md
  - wiki/papers/agents/push-your-agent-persistence.md, wiki/papers/generative-models/precise-sde-sampling.md
  - wiki/papers/code-reasoning/improver-2-proof-optimization.md, wiki/papers/code-reasoning/agentic-proving-verification.md
  - wiki/papers/code-reasoning/rma-research-math.md, wiki/papers/sequential-modeling/preisach-attention.md
  - wiki/papers/sequential-modeling/dimensionality-barrier-retrieval.md, wiki/papers/benchmarking/benchmark-rigging-analysis.md
- New method pages: 2 (sde-consistent-sampling, pcsp-shared-policy)
- New concept pages: 1 (shannon-scaling-law)
- New entity pages: 2 (tubifm, harness-lm)
- Updated: wiki/index.md (Papers, Methods, Concepts, Entities sections)

## [2026-05-25] search | arXiv Daily Digest (AI & CTR)
- New page: wiki/synthesis/2026-05-25/arxiv-daily.md
- Sources: arXiv cs.AI new (164 entries), cs.LG new (203 entries), cs.IR new (16 entries), cs.CL new (85 entries)
- Highlights: Shannon Scaling Law (LLMs as noisy channels), TubiFM (unified ranking), HARNESS-LM (Bing Ads SLM distillation), Netflix generative recommenders 1B params, RPORec (Kuaishou reasoning-augmented rec), SkillOpt (Microsoft agent skill optimizer), PCSP (game NPCs with shared RL), Precise (ByteDance flow-matching RL), Complete-muE (MoE hyperparameter transfer), GenStrat (strategic reasoning in LLMs)
- 27 papers cataloged across 9 categories
- Updated: wiki/index.md

## [2026-05-24] search | arXiv Daily Digest
- New page: wiki/synthesis/2026-05-24/arxiv-daily.md
- Papers featured: Gated DeltaNet-2, MOSS, Ratchet, Compiling Agentic Workflows, IdleSpec, WorkstreamBench, Search-E1, Advancing Mathematics with Formal Proof, RPORec, LLM Retrieval for Stable Ads
- Updated: wiki/index.md

## [2026-05-24] ingest | Games & RL Papers from arXiv Daily
- Source: wiki/synthesis/2026-05-24/arxiv-daily.md (Section 7: Games & RL)
- New paper pages: 8
  - wiki/papers/games/odysseus-vlm-games.md
  - wiki/papers/games/opengame-agentic-coding.md
  - wiki/papers/agents/hgpo-policy-optimization.md
  - wiki/papers/games/sensi-llm-game-agents.md
  - wiki/papers/games/spiral-self-play-reasoning.md
  - wiki/papers/games/nemobot-game-agents.md
  - wiki/papers/games/dark-souls-iii-lifelong.md
  - wiki/papers/games/cross-entropy-games.md
- New method pages: 4
  - wiki/methods/turn-level-critic.md
  - wiki/methods/hierarchical-group-policy-optimization.md
  - wiki/methods/structured-test-time-learning.md
  - wiki/methods/cross-entropy-curriculum.md
- New concept pages: 2
  - wiki/concepts/cognitive-training.md
  - wiki/concepts/skill-graph.md
- New entity pages: 1
  - wiki/entities/gamecoder-27b.md
- Updated: wiki/index.md (Papers, Methods, Concepts, Entities sections)

## [2026-05-25] analyze | arXiv Broad Survey — 121 Papers Across 10 Categories
- New synthesis pages:
  - wiki/synthesis/arxiv-broad-2026-05-25.md (categorized paper list with details)
  - wiki/synthesis/affiliation-landscape.md (10 institutions analysis)
  - wiki/synthesis/technical-roadmap.md (9 technical routes analysis)
- Coverage: LLM Training & Theory (16), RecSys (12), CTR (10), Ad Retrieval (9), Agents (14), Games (12), Code/Repair (12), Diffusion (12), Sequence Modeling (13), Benchmarks (11)
- Affiliations tracked: Google DeepMind, NVIDIA, Microsoft, ByteDance, Alibaba, Tencent, Kuaishou, Netflix, LinkedIn, Walmart, Meituan, Xiaohongshu, Baidu, Salesforce, Arcee AI, CMU, MIT, UC Berkeley, IIIT Ranchi, NTU, CityU HK, NYCU
- Updated: wiki/index.md (Synthesis section)

## [2026-05-25] query | 顶会论文专题报告 — 覆盖9个会议的最新接收论文
- Created: wiki/synthesis/2026-05-25/conference-digest.md
- Conferences covered: ICML 2026, AAAI 2026, KDD 2026, SIGIR 2026, CVPR 2026, WWW 2026, NeurIPS 2025, ICLR 2026, ACL/EMNLP 2025
- Total papers detailed: 45+ papers with full 5-part analysis (问题背景、方法详述、主要创新点、实验结果对比、局限性)
- Topics: LLM training & theory, recommender systems, CTR prediction, ad retrieval, agents, game AI/RL, code generation, diffusion models, sequence modeling, benchmarks
- Key findings: RL for diffusion LLMs (NeurIPS 2025/ICLR 2026), agentic recommendation systems (WWW 2026), tree-search code generation (ACL 2025), representation collapse in deep recommenders (KDD 2026)
- Updated: wiki/index.md (Synthesis section)

## [2026-05-25] ingest | 13 篇顶会论文消化
- Created paper pages:
  - wiki/papers/generative-models/self-flow-matching.md — Self-Flow (ICML 2026, 自监督流匹配)
  - wiki/papers/llm-training/gated-attention.md — Gated Attention (NeurIPS 2025 Best Paper)
  - wiki/papers/llm-training/transformers-inherently-succinct.md — Transformer简洁性理论 (ICLR 2026 Outstanding)
  - wiki/papers/recommendation/thinkrec.md — ThinkRec (WWW 2026, 思考式推荐)
  - wiki/papers/ctr/rankup-advertising.md — RankUp (KDD 2026, 腾讯微信广告)
  - wiki/papers/ctr/genci-ctr.md — GenCI (WWW 2026, 生成式CTR)
  - wiki/papers/agents/mem1-agent.md — MEM1 (ICLR 2026, 长时域智能体记忆)
  - wiki/papers/games/alive-frontend-games.md — ALIVE (ICML 2026, 前端游戏RL)
  - wiki/papers/code-reasoning/tree-of-evolution.md — Tree-of-Evolution (ACL 2025, 树结构指令进化)
  - wiki/papers/code-reasoning/codetree-code-generation.md — CodeTree (ACL 2025, 树搜索代码生成)
  - wiki/papers/llm-training/ladir-diffusion-reasoning.md — LaDiR (ICLR 2026, 潜扩散推理)
  - wiki/papers/generative-models/arcache-video-diffusion.md — ARCache (CVPR 2026, 视频扩散缓存加速)
  - wiki/papers/generative-models/uniar-multimodal.md — UniAR (ICML 2026, 统一多模态自回归)
- Updated: wiki/index.md (Papers in LLM Training, RecSys, CTR, Agents, Games, Generative, Code sections)
- Total paper pages now: 48

## [2026-05-25] ingest | Awesome-CTR-Scaling Repository — 49 Papers CTR 缩放全景
- Created synthesis: wiki/synthesis/ctr-scaling-landscape.md (按公司+技术路线+时间线三维度组织)
- Created paper pages (8 new):
  - wiki/papers/recommendation/wukong-scaling-law.md — Wukong (Meta, ICML 2024, 推荐缩放律奠基)
  - wiki/papers/recommendation/hstu-generative-recommendation.md — HSTU (Meta, ICML 2024, 万亿参数生成推荐)
  - wiki/papers/recommendation/kunlun-scaling-law.md — Kunlun (Meta, 2026, 统一架构缩放律)
  - wiki/papers/ctr/fat-ctr-scaling.md — FAT (Alibaba, Rademacher CTR 缩放律理论)
  - wiki/papers/ctr/suan-ctr-scaling.md — SUAN (Meituan, RecSys 2025, 线上缩放方法学)
  - wiki/papers/ctr/ge4rec-generative-ctr.md — GE4Rec (Tencent, 生成式 CTR 范式)
  - wiki/papers/recommendation/lirank-linkedin-ranking.md — LiRank (LinkedIn, 大规模工业排序)
  - wiki/papers/recommendation/climber-scaling-laws.md — Climber (NetEase, WWW 2025, 持续线上缩放)
- Companies covered: Meta (9), ByteDance (9), Alibaba (8), Meituan (4), Tencent (3), Kuaishou (4), LinkedIn (2), Google, NetEase, Shopee
- Updated: wiki/index.md (RecSys, CTR sub-sections, Synthesis section)
- Total paper pages now: 56

## [2026-05-25] search | 各大 AI 公司技术报告汇总 — 覆盖 17 家机构 22 份报告
- Created: wiki/synthesis/2026-05-25/tech-report-digest.md
- Coverage: DeepSeek (V4), OpenAI (GPT-5/5.5/o3), Meta (Llama 4), Google (Gemini 2.5/3.5), Anthropic (Claude Opus 4/4.6/4.7), Mistral (Large 3/Small 4/Medium 3.5), Qwen (3.5), Yi (Lightning), Microsoft (Phi-4/reasoning/Mini), Apple (Foundation Models 2025), NVIDIA (Nemotron 3), xAI (Grok 4/4.3), Amazon (Nova/Nova 2), Zhipu AI (GLM-5/5.1), InternLM (2/3), Moonshot (Kimi K2/K2.6), ByteDance (Seed 2.0)
- Key findings: MoE 主流化, 混合注意力架构崛起, Thinking Mode 成为标配, 长上下文竞争白热化, 合成数据训练突破, Muon 优化器普及
- Updated: wiki/index.md (Synthesis section)

## [2026-06-08] synthesis | Conference Digest — 2026年6月全面版（顶会论文专题报告）
- New page: wiki/synthesis/2026-06-08/conference-digest.md
- Coverage: 12 conferences (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) + arXiv
- Papers covered: 100+ across LLM training theory, recommendation/CTR (ByteDance TokenMixer-Large/HyFormer, Kuaishou Taiji/GR4AD/OneMall, JD GenRec), agent systems (GrandCode Codeforces triple crown, MiRA, MetaClaw, AgentFlow), multimodal/generative models (Self-Flow, UniAR, PixelDiT, Molmo2), games/RL (NitroGen, ALIVE, PCSP), code/reasoning (Aletheia, Agentic Verifier), NeurIPS 2025 Best Papers deep dive (Gated Attention, Artificial Hivemind, 1000-Layer RL, Diffusion Memorization), RLVR critique (Runner-Up)
- Key themes: Diffusion LLM rise, RLVR paradigm shift, Agent systems maturity, CTR LLM-ification, Reasoning models as default, Multi-modal unification
- Labs covered: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, JD.com, Pinterest
- Updated: wiki/index.md, wiki/log.md

## [2026-04-15] init | Wiki Created
- Scaffolded by llm-wiki-bootstrap
- Domain: Research on Andrej Karpathy's X posts, talks, and related source materials on neural networks, LLMs, and deep learning
- Source types: Web articles, PDFs / papers, Meeting notes / transcripts, Personal notes / journals
- Schema: CLAUDE.md
- Editor: Obsidian

## [2026-04-15] ingest | The Growing Gap in Understanding AI Capability
- Source: raw/4.10.md (Karpathy X post, 4/10)
- Summary: wiki/sources/ai-capability-gap.md
- New pages:
  - wiki/entities/andrej-karpathy.md
  - wiki/entities/openai-codex.md
  - wiki/entities/claude-code.md
  - wiki/concepts/agentic-models.md
  - wiki/concepts/verifiable-rewards.md
  - wiki/concepts/peaky-capability.md
  - wiki/concepts/ai-psychosis.md
  - wiki/methods/reinforcement-learning.md
- Updated: wiki/index.md, wiki/overview.md
- Contradictions: none (first substantive source)

## [2026-04-17] ingest | Software Is Changing (Again) — YC AI Startup School Keynote
- Source: raw/youtube-transcript/andrej-karpathy-software-is-changing-again/transcript.md
- Summary: wiki/sources/software-is-changing-again.md
- Updated:
  - wiki/entities/andrej-karpathy.md (fully rewritten as hub page)
  - wiki/entities/claude-code.md
  - wiki/entities/openai-codex.md
- New pages:
  - wiki/concepts/software-3-0.md
  - wiki/concepts/llm-os.md
  - wiki/concepts/people-spirits.md
  - wiki/concepts/jagged-intelligence.md
  - wiki/concepts/partial-autonomy-apps.md
  - wiki/concepts/autonomy-slider.md
  - wiki/concepts/vibe-coding.md
  - wiki/concepts/iron-man-analogy.md
  - wiki/concepts/build-for-agents.md
  - wiki/entities/openai.md
  - wiki/entities/cursor.md
  - wiki/entities/perplexity.md
  - wiki/entities/tesla.md
  - wiki/entities/tesla-autopilot.md
  - wiki/entities/hugging-face.md
  - wiki/entities/menugen.md
  - wiki/entities/model-context-protocol.md
  - wiki/entities/llama.md
- Contradictions: YC talk places current LLM era at "1960s of computing"; Berkeley 2024 keynote places it at "1980s." Flagged in wiki/concepts/llm-os.md.

## [2026-04-17] ingest | We're Summoning Ghosts, Not Building Animals — Dwarkesh Interview
- Source: raw/youtube-transcript/andrej-karpathy-were-summoning-ghosts-not-building-animals/transcript.md
- Summary: wiki/sources/summoning-ghosts-not-animals.md
- Updated:
  - wiki/concepts/peaky-capability.md
  - wiki/concepts/verifiable-rewards.md
  - wiki/concepts/ai-psychosis.md
  - wiki/concepts/agentic-models.md
  - wiki/methods/reinforcement-learning.md
- New pages:
  - wiki/concepts/animals-vs-ghosts.md
  - wiki/concepts/cognitive-core.md
  - wiki/concepts/march-of-nines.md
  - wiki/concepts/decade-of-agents.md
  - wiki/concepts/rl-is-terrible.md
  - wiki/concepts/model-collapse.md
  - wiki/concepts/llm-cognitive-deficits.md
  - wiki/concepts/in-context-learning.md
  - wiki/concepts/agi-blends-into-2-percent-growth.md
  - wiki/entities/dwarkesh-patel.md
  - wiki/entities/waymo.md
  - wiki/entities/eureka.md
  - wiki/entities/deepseek-v3-2.md
- Contradictions: none new; Tesla/Waymo contrast now articulated as complementary priors rather than competing claims.

## [2026-04-17] ingest | Berkeley SkyDeck AI Hackathon 2024 — Keynote
- Source: raw/youtube-transcript/andrej-karpathy-berkeley-ai-hackathon-2024-keynote/transcript.md
- Summary: wiki/sources/berkeley-ai-hackathon-2024-keynote.md
- New pages:
  - wiki/concepts/feel-the-agi.md
  - wiki/concepts/snowballs.md
  - wiki/concepts/10000-hours.md
  - wiki/concepts/ramps-to-knowledge.md
  - wiki/entities/cs231n.md
  - wiki/entities/zero-to-hero.md
  - wiki/entities/llm101n.md
  - wiki/entities/awesomemovies-life.md
- Contradictions: "1980s of computing" framing here vs. "1960s" in YC 2025 talk — noted in wiki/concepts/llm-os.md as reflecting the speed of reframing in Karpathy's own thinking.

## [2026-04-17] ingest | GPU MODE IRL 2024 — Karpathy on llm.c
- Source: raw/youtube-transcript/andrej-karpathy-gpu-mode-irl-2024-keynote/transcript.md
- Summary: wiki/sources/gpu-mode-irl-2024-keynote.md
- New pages:
  - wiki/entities/llm-c.md
  - wiki/entities/micrograd.md
  - wiki/entities/nanogpt.md
  - wiki/entities/nanochat.md
  - wiki/entities/pytorch.md
  - wiki/entities/github.md
- Contradictions: none (llm.c is a systems topic with few overlapping claims to the other sources).

## [2026-04-17] bulk-update | index.md reflow
- Added: 5 sources, 23 entities, 22 concepts (alphabetically sorted)
- Methods source count: reinforcement-learning → 2
- No content changes to existing pages beyond cross-reference backfills

## [2026-04-17] ingest | Karpathy X posts 2026 — FSD Coast-to-Coast
- Source: raw/2026/1.1.md
- Summary: wiki/sources/karpathy-x-2026-fsd-coast-to-coast.md
- Updated: wiki/concepts/march-of-nines.md, wiki/entities/tesla-autopilot.md, wiki/entities/tesla.md
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — nanochat & GPT-2 Reproduction
- Sources: raw/2026/1.8.md, 1.29.md, 2.2.md
- Summary: wiki/sources/karpathy-x-2026-nanochat-gpt2-reproduction.md
- Updated: wiki/entities/nanochat.md
- New pages: wiki/entities/modded-nanogpt.md
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — Claude Coding Reflections
- Source: raw/2026/1.27.md
- Summary: wiki/sources/karpathy-x-2026-claude-coding-reflections.md
- Updated: wiki/entities/claude-code.md, wiki/concepts/vibe-coding.md, wiki/concepts/build-for-agents.md
- New pages: wiki/concepts/atrophy.md, wiki/concepts/10x-engineer.md
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — Agentic Engineering
- Sources: raw/2026/2.5.md, 2.25.md
- Summary: wiki/sources/karpathy-x-2026-agentic-engineering.md
- New pages: wiki/concepts/agentic-engineering.md, wiki/concepts/slopacolypse.md
- Contradictions: Karpathy pivots "vibe coding" → "agentic engineering" as primary frame — flagged in wiki/concepts/vibe-coding.md

## [2026-04-17] ingest | Karpathy X posts 2026 — Malleable Software
- Sources: raw/2026/2.12.md, 2.17.md, 2.20.md, 2.21.md
- Summary: wiki/sources/karpathy-x-2026-malleable-software.md
- New pages: wiki/concepts/bacterial-code.md, wiki/concepts/app-store-outdated.md, wiki/entities/microgpt.md, wiki/entities/deepwiki.md, wiki/entities/matx.md
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — Agent Networks
- Sources: raw/2026/2.4.md, 2.13.md
- Summary: wiki/sources/karpathy-x-2026-agent-networks.md
- New pages: wiki/entities/simile-ai.md, wiki/concepts/org-code.md
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — autoresearch & Claws
- Sources: raw/2026/2.26.md, 2.28.md, 3.6.md, 3.8.md, 3.9.md, 3.10.md, 3.11.md, 3.12.md, 3.20.md
- Summary: wiki/sources/karpathy-x-2026-autoresearch-and-claws.md
- New pages: wiki/concepts/claws.md, wiki/concepts/autoresearch.md, wiki/concepts/intelligence-brownouts.md, wiki/entities/autoresearch.md, wiki/entities/nanoclaw.md
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — Supply Chain Attacks
- Sources: raw/2026/3.19.md, 3.31.md
- Summary: wiki/sources/karpathy-x-2026-supply-chain.md
- New pages: wiki/concepts/supply-chain-attacks.md
- Updated: wiki/concepts/bacterial-code.md (stronger "Why this matters in 2026" section)
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — LLM Knowledge Bases & BYOAI
- Sources: raw/2026/4.3.md, 4.5.md
- Summary: wiki/sources/karpathy-x-2026-llm-wiki.md
- New pages: wiki/concepts/llm-knowledge-bases.md, wiki/concepts/byoai.md, wiki/concepts/government-legibility.md
- Note: karpathy-wiki itself is an instance of the LLM Knowledge Base pattern described Apr 3 / Apr 5.
- Contradictions: none

## [2026-04-17] ingest | Karpathy X posts 2026 — Miscellaneous
- Sources: raw/2026/1.7.md, 1.31.md, 2.1.md, 3.25.md, 3.27.md, 3.28.md
- Summary: wiki/sources/karpathy-x-2026-misc.md
- Updated: wiki/concepts/ai-psychosis.md (memory-overfit note)
- Contradictions: none

## [2026-04-17] ingest | Andrej Karpathy self-bio (karpathy.ai)
- Source: raw/Andrej Karpathy.md
- Summary: merged directly into wiki/entities/andrej-karpathy.md (no new source page — it is a bio reference)
- Updated: wiki/entities/andrej-karpathy.md (added verified career-date table, CS231n growth numbers, internship list, advisers)
- Contradictions: none

## [2026-04-17] bulk-update | index.md reflow
- Added: 10 source pages, 7 entity pages (autoresearch, deepwiki, matx, microgpt, modded-nanogpt, nanoclaw, simile-ai), 14 concept pages (10x-engineer, agentic-engineering, app-store-outdated, atrophy, autoresearch, bacterial-code, byoai, claws, government-legibility, intelligence-brownouts, llm-knowledge-bases, org-code, slopacolypse, supply-chain-attacks)
- Source counts updated across: andrej-karpathy (10+), claude-code (3), cursor (2), github (3), cs231n (2), nanochat (5), tesla (3), tesla-autopilot (3), modded-nanogpt (3), openai-codex (3), model-context-protocol (2), march-of-nines (3), nanogpt (3), vibe-coding (2), build-for-agents (2), agentic-engineering (4), bacterial-code (3), claws (2), autoresearch (3), supply-chain-attacks (3), app-store-outdated (2), atrophy (2), slopacolypse (2), org-code (2), 10x-engineer (3)

## [2026-05-21] query | arXiv Daily Report (AI & CTR)
- Created: wiki/synthesis/2026-05-21/arxiv-daily.md
- Sources: arXiv cs.AI new (31 entries), cs.IR new (5 entries + 11 replacements)
- Highlights: CPO (DPO-RLHF non-equivalence), UG-Sep (ByteDance recommender 20% latency cut), PlanningBench, SOLAR
- Updated: wiki/index.md (Synthesis section)

## [2026-05-23] query | arXiv Daily Report (AI & CTR)
- Created: wiki/synthesis/2026-05-23/arxiv-daily.md
- Sources: arXiv cs.AI new (78 entries), cs.IR new (7 entries + replacements)
- Highlights: FLUID (ID-free livestreaming rec), Sycophancy taxonomy, RPORec (RL + reasoning for rec), Airbnb LLM cold-start, ThinkGR (CoT + generative retrieval), ActiveGraph (event-sourced agents)
- Updated: wiki/index.md (Synthesis section)

## [2026-04-18] ingest | Karpathy X posts 2025 (full corpus)
- Scope: All 69 files in raw/2025/ — Karpathy's X posts from Apr–Dec 2025
- Method: Clustered into 16 thematic source bundles, each with its own summary page
- Source summaries created:
  - wiki/sources/karpathy-x-2025-power-to-the-people.md (Apr 8 essay)
  - wiki/sources/karpathy-x-2025-software-paradigm.md (Jul 19 / Nov 17 / Dec 20)
  - wiki/sources/karpathy-x-2025-ghosts-and-psychology.md (Oct 2 / Nov 22 / Dec 8)
  - wiki/sources/karpathy-x-2025-bacterial-code-origin.md (Jul 6)
  - wiki/sources/karpathy-x-2025-rl-and-learning-paradigms.md (May 11 / Jul 14–30 / Aug 28)
  - wiki/sources/karpathy-x-2025-cognitive-core.md (Jul 27)
  - wiki/sources/karpathy-x-2025-ai-assisted-coding.md (9 posts Apr–Dec)
  - wiki/sources/karpathy-x-2025-build-for-agents.md (Apr 22 / May 1 / Jul 20–25 / Nov 24)
  - wiki/sources/karpathy-x-2025-evals-and-model-vibes.md (Apr 30 / Aug 29 / Nov 19–23)
  - wiki/sources/karpathy-x-2025-nanochat-saga.md (Oct 13–24 / Dec 9)
  - wiki/sources/karpathy-x-2025-tesla-fsd.md (Jul 24 / Nov 13–14)
  - wiki/sources/karpathy-x-2025-dwarkesh-recap.md (Oct 19)
  - wiki/sources/karpathy-x-2025-llm-reading.md (Nov 18 / Dec 11)
  - wiki/sources/karpathy-x-2025-education.md (Nov 25)
  - wiki/sources/karpathy-x-2025-video-gen.md (Jul 3 / Jul 18)
  - wiki/sources/karpathy-x-2025-misc.md (23 remaining posts)
- New concept pages:
  - wiki/concepts/system-prompt-learning.md (May 11)
  - wiki/concepts/context-engineering.md (Jul 25)
  - wiki/concepts/llm-gui.md (May 1 / Jul 20)
  - wiki/concepts/verification-gap.md (Jul 26 / Aug 25)
  - wiki/concepts/galaxy-brain-reasoning.md (Dec 11)
  - wiki/concepts/verifiability.md (Nov 17)
  - wiki/concepts/rlvr.md (Dec 20)
  - wiki/concepts/power-to-the-people.md (Apr 8)
  - wiki/concepts/code-post-scarcity.md (Oct 27)
  - wiki/concepts/prompt-injection.md (Jul 11)
- New entity pages:
  - wiki/entities/reader3.md (Nov 18)
  - wiki/entities/hn-time-capsule.md (Dec 11)
  - wiki/entities/llm-council.md (Nov 23)
  - wiki/entities/richard-sutton.md (Oct 19)
  - wiki/entities/tinker.md (Oct 19)
  - wiki/entities/openrouter.md (Aug 29)
  - wiki/entities/simon-willison.md (Jul 11)
  - wiki/entities/decart.md (Jul 18)
  - wiki/entities/prime-intellect.md (May 11)
  - wiki/entities/anthropic.md (multiple)
- Updated: index.md (full reflow — Sources, Entities, Concepts sections)
- Contradictions: none (2025 corpus pre-dates 2026 and is mostly *consistent with* the 2026 frame it set up; the Nov 17 verifiability essay restates the Software 2.0 automation predicate without contradicting the earlier Software 3.0 frame).
- Note: This fills the 2025 gap between the Apr 10 post (already ingested) and the 2026 X-post corpus. The whole corpus coheres as "the year RLVR made reasoning models real and agentic engineering became thinkable."

## [2026-05-26] search | AI 公司技术报告汇总第二版 — 新增至 21 家机构
- Updated: wiki/synthesis/2026-05-26/tech-report-digest.md (替代 05-25 版作为扩展版本)
- 新增 7 项: DeepSeek V3 (arXiv:2412.19437)、DeepSeek R1 (arXiv:2501.12948)、GPT-5.1/5.2 System Card 补充、Ministral 3、Qwen3、InternLM3 8B、Step-3 (阶跃星辰)
- 补充 Baichuan 状态确认 (无近期报告)
- 覆盖机构完整列表扩展至 21 家
- Updated: wiki/index.md (Synthesis section)

## [2026-05-26] ingest | Conference Digest Deep Edition
- Summary: wiki/synthesis/2026-05-26/conference-digest.md
- Coverage: 11 conferences (ICML 2025, AAAI 2026, ICLR 2026, CVPR 2026, EMNLP 2025, ACL 2026, KDD 2026, RecSys 2025, WWW 2026, SIGIR 2026, CIKM 2025)
- Papers: 70+ papers across LLM reasoning, RecSys scaling, CTR prediction, AI agents, diffusion models, multimodal VLMs
- Labs covered: Google DeepMind, OpenAI, Meta, NVIDIA, Anthropic, ByteDance, Alibaba, Kuaishou, Apple, Microsoft Research, Spotify, JD.com
- Updated: wiki/index.md
- Contradictions: none

## [2026-05-27] search | 各大 AI 公司技术报告汇总第三版 — 21 家机构详细分析
- Created: wiki/synthesis/2026-05-27/tech-report-digest.md
- 对比 05-26 版新增/补充: DeepSeek V3.2 (DSA + IMO/IOI 金牌)、GPT-5 System Card 详细规格、Llama 4 原生多模态细节、Claude 4 ASL-3/ASL-2 层级、Magistral 纯 RL 训练、Mistral Large 3 (675B MoE)、Phi-4-reasoning-vision、Apple PT-MoE 架构详解、NVIDIA Nemotron 3 系列 (Mamba-Transformer Hybrid MoE)、Grok 3 Colossus 200K GPU 超算、Kimi K2.5 视觉 Agent + Agent Swarm、Baichuan-M3 医疗 SOTA、Step-2 MFA 注意力
- 综合趋势分析: MoE 主流化、Hybrid 架构 (Mamba+Transformer)、Thinking Mode 统一、Agentic 核心化、国产 GPU 适配、RL 重新聚焦
- Updated: wiki/index.md (Synthesis section)

## [2026-05-26] ingest | arXiv Daily — May 26 Digest
- Summary: wiki/synthesis/2026-05-26/arxiv-daily.md
- New page: wiki/synthesis/2026-05-26/arxiv-daily.md
- Papers covered: 10 top picks from ~1,500 cs.AI + cs.LG entries
- Highlights: Language Models Need Sleep, How Much Thinking is Enough, Verified SHAP (ICML 2026), Automated Benchmark Auditing, Agent-ToM, Feature Lottery bifurcation theory, Algometrics, GenLI (CTR), LLM-AutoSciLab
- Updated: wiki/index.md

## [2026-05-27] synthesis | 投资日报 — 2026-05-27
- Summary: wiki/synthesis/2026-05-27/investment-daily.md
- 美股热点：Anthropic $900B 估值融资（IPO 预期 10 月）、SpaceX IPO 路线图（6 月 12 日交易）、Mag 7 分化（GOOGL/AMZN 领涨，MSFT/META 受 CapEx 压制）、AMD +114% YTD、SK Hynix 加入 $1T 俱乐部
- AI 芯片：NVIDIA $5.5T 市值/Broadcom $2.07T/TSMC 2nm 扩产
- AI 主题：GPT-5.5/DeepSeek V4/Claude 4.6 密集发布，1M+ token 成标配，AI 首次原创科学发现
- 数据中心：7GW/12GW 美国 AI 数据中心取消或延迟，Applied Digital $36 亿新项目
- 港股：Q1 公募重仓腾讯/阿里/美团/小米合计超千亿，2026 是 AI 商业化元年
- A 股：科创 50 涨超 9%，57 家科创板创新高。算力芯片全线爆发（寒武纪/海光信息/中科曙光）。PCB/MLCC 受英伟达 BOM 拆解引爆。算力网上升为国家战略。
- 关键主线：AI 算力全产业链（光模块→服务器→液冷→PCB→MLCC），存储芯片供给紧缺涨价
- New page: wiki/synthesis/2026-05-27/investment-daily.md
- Updated: wiki/index.md

## [2026-05-28] synthesis | 投资日报 — 2026-05-28
- Summary: wiki/synthesis/2026-05-28/investment-daily.md
- 美股热点：Micron $1T 市值突破（+19%，UBS 目标 $1,625）、NVIDIA 财报后跌 6%（营收 $816B +85%）、Snowflake 盘后 +36%（$6B AWS 协议）、AMD +5%（Agentic AI "$200B TAM"）、Qualcomm 获字节跳动 ASIC 订单
- 港股热点：快手+5.95%（可灵 AI 收入超 1.5 亿）、MiniMax/智谱首次纳入恒生科技指数（6 月 8 日生效）、深演智能 IPO 首日+273%（AI Agent 第一股）、小米 Q1 营收 991B（AI 三年 600 亿）
- A 股热点：华为韬(τ)定律引爆国产芯片行情（逻辑折叠/等效 1.4nm/已量产 381 款芯片）、长鑫科技科创板 IPO 上会（Q1 营收 508 亿 +719%）、中际旭创盘中突破万亿市值、兆易创新毛利率 57% 创历史新高
- AI 主题：Agentic AI 全面爆发（NVIDIA/AMD/阿里真武 M890/小米 miclaw/深演智能）、存储超级周期（DRAM 价格涨幅预测上调至 250-280%）、全球 AI CapEx $8300 亿（+79%）、EAGLE 3.1 推理加速 2x、Pointer OSWorld SOTA 83.6%
- 核心主线：存储芯片超级周期 / Agentic AI 推理侧 / 中国半导体自主可控 / AI 基础设施资本开支 / 港股 AI 资产重估
- New page: wiki/synthesis/2026-05-28/investment-daily.md
- Updated: wiki/index.md

## [2026-06-01] search | 各大 AI 公司技术报告汇总第四版 — 扩展至 26+ 家机构
- Created: wiki/synthesis/2026-06-01/tech-report-digest.md
- 覆盖 26+ 家机构, 35+ 份技术报告
- 新增 DeepSeek-R1 (arXiv:2501.12948, 纯 RL 推理涌现)、DeepSeek-V4、OpenAI o3/o4-mini/o4-pro 系统卡 (arXiv:2603.04567)、GPT-5.4 (arXiv:2605.07890)、Gemini 3.1 Pro (2M 上下文)、Claude Opus 4.6、xAI Grok 4 (arXiv:2601.04567)、InternLM 2.5、Step-3 (arXiv:2604.05678)
- 维持 05-27 版已有的 DeepSeek V3/V3.2、GPT-5、Llama 4、Gemini 2.5、Claude Opus 4、Magistral/Ministral 3、Mistral Large 3、Qwen3、Yi-Lightning、Phi 系列、Apple、Nemotron 3、Amazon Nova、GLM-5、InternLM3、Kimi K2/K2.5、Seed 2.0、Step-2/Step-Audio、Baichuan-Omni/M3
- 综合趋势更新: 推理模型爆发 (10 大趋势分析)
- Updated: wiki/index.md (Synthesis section)

## [2026-05-29] synthesis | 投资日报 — 2026-05-29
- Summary: wiki/synthesis/2026-05-29/investment-daily.md
- 美股热点：NVDA财报后消化（-9%）、MU/SK Hynix双双$1T市值（存储超级周期）、AVGO $1.89T+AI网络ASIC龙头、PLTR内幕抛售引关注
- 大模型：GPT-5.5、DeepSeek V4、Claude 4.7、Gemini 3.1密集发布，国产豆包Seed 2.0 Pro杀入全球前五
- 港股/恒科：智谱+MiniMax 6月8日纳入恒生科技指数（$12.5-17.5亿被动资金），腾讯混元Token增长10倍
- A股/算力：寒武纪Q1净利+185%/海光在手订单480亿/中际旭创+262%/工业富联+103%，科创板盘中涨超9%
- 中概：PDD Q1财报受一次性税费拖累跌12%，BABA云AI驱动力最强
- 新能源：4月销量出炉（比亚迪32万/零跑7.1万新势力第一/小米3万冲进前六），超15家车企跟进涨价潮
- AI主线：全球CapEx $700B+/中国Token调用两年1000倍/Agentic AI商业元年/AI算力全产业链业绩兑现
- Updated: wiki/index.md (Synthesis section)

## [2026-05-28] synthesis | arXiv Daily — AI & CTR (May 27, 2026)
- Summary: wiki/synthesis/2026-05-27/arxiv-daily.md
- 8 papers surveyed: AIRA-Compose/Design (agentic architecture discovery), Hierarchical LM with provable reasoning benefits (Ω(n) context vs Θ(log n) reasoning), GRAM (probabilistic recursive reasoning), RL Memory Agents curriculum study, LoopCTR (loop scaling for CTR), CADET (decoder-only transformer for ads at LinkedIn, 11.04% lift), LLM-HYPER (LLM hypernetworks for cold-start CTR), FEDIN (frequency-domain CTR, SIGIR 2026)
- Key themes: agentic research automation, theoretical foundations for reasoning, CTR goes decoder-only, LLM+CTR convergence, inference-time scaling
- New page: wiki/synthesis/2026-05-27/arxiv-daily.md
- Updated: wiki/index.md

## [2026-06-01] update | 各大 AI 公司技术报告汇总 — 精简重构为 12 家核心机构深度版
- Rewritten: wiki/synthesis/2026-06-01/tech-report-digest.md (覆盖 12 家核心机构, 24 份报告)
- 相比此前版本的变化: 精简机构范围 (从 26+ 聚焦到 12 家,弃用低活跃机构), 补充 DeepSeek R1/V3/V4、OpenAI GPT-5/5.5/o3、Meta Llama 4、Google Gemini 2.5、Anthropic Claude Opus 4/4.6/4.8、Mistral Large 3/Small 4/Medium 3.5、Qwen3/3.7-Max、Microsoft Phi-4/Phi-4-Reasoing、Apple AFM 2025、NVIDIA Nemotron 3、xAI Grok 4.1/4.3/4.20、ByteDance Seed 2.0 完整规格
- 综合趋势更新: 8 大趋势分析 (MoE 主流化、混合注意力、百万上下文、Thinking Mode、Agentic 核心化、推理效率、开源分化、安全层级)
- Updated: wiki/index.md (Synthesis section)

## [2026-05-29] search | 各大 AI 公司技术报告汇总第五版 — 新增至 26+ 家机构
- Updated: wiki/synthesis/2026-05-29/tech-report-digest.md (替代 06-01 版作为最新版本)
- 新增: Claude Opus 4.7 & Sonnet 4.6 (Anthropic, May 2026, 3T/800B, GPQA 94.3% / SWE-bench 85.2%)
- 新增: Kimi K2.6 (Moonshot AI, Apr 2026, 1.06T/100B active, 262K context, 288 experts)
- 新增: Grok 4.1 Fast (xAI, Nov 2025, 2M context, 3x speed vs Grok 4)
- 新增: InternLM 104B (Shanghai AI Lab, 104B MoE)
- 新增: Seed 1.6 (ByteDance, Dec 2025, 256K context)
- 补充: DeepSeek V4 完整规格确认 (1.6T total, 49B active, 1M context, Hybrid Attention)
- 补充: Qwen3 详细分析 (arXiv:2505.09388, 235B-22B MoE)
- 覆盖机构完整列表扩展至 26+ 家
- 综合趋势: MoE 全面主流化, Hybrid Attention 架构崛起, 百万级上下文标配, Thinking Mode 标准化, Agentic 核心化, 推理效率军备竞赛, 国产 GPU 适配加速, 安全对齐层级化
- Updated: wiki/index.md (Synthesis section)

## [2026-05-29] search | Conference Digest — 2026年5月全面版（顶会论文专题报告第二版）
- New page: wiki/synthesis/2026-05-29/conference-digest.md
- Sources: arXiv cs.AI, cs.LG, cs.IR, cs.CL, cs.MA recent; ICML 2026, ICLR 2026, NeurIPS 2025, WWW 2026, SIGIR 2026, CIKM 2025, KDD 2026 accepted papers
- Papers covered: 80+ papers across 11 categories/venues
- Highlights: Bi-NAC (ICML 2026 bilevel actor-critic), GSPR (ICLR 2026 safety policy reasoner), NSPO (safety subspace projection), DAR (dual-KL RLHF), OXRL (51-algorithm post-training comparison), CADET (LinkedIn decoder-only CTR +11.04%), LoopCTR (recursive scaling), Memento (Meta RAG long-retention +1% CTR), GRAB (Baidu generative CTR +3.49%), DeepAgent (end-to-end reasoning agent), TRICE (tool-integrated reasoning recipe), SPIRAL (self-play reasoning), DeepMind Gemini Embedding 2, Generative UI, Aletheia math research agent, RePlaid (continuous diffusion LM), MaR (metacognition reward), SpecBench (reward hacking), FeatureBench (complex feature development)
- Labs covered: Google DeepMind, Meta, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, LinkedIn, OpenAI/Microsoft, Anthropic, Top US e-commerce
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-01] search | Conference Digest — 2026年6月全面版（顶会论文专题报告）
- New page: wiki/synthesis/2026-06-01/conference-digest.md
- Sources: ICML 2026 (6,500+ papers, 500 highlights), AAAI 2026 (29K submissions), NeurIPS 2025 Best Papers + Runners-Up, ICLR 2026 Outstanding, KDD 2026, CVPR 2026 (4,090 accepted), ACL 2026, EMNLP 2025 Awards, SIGIR 2026, WWW 2026
- Labs covered: Meta AI (Credit Assignment with Resets, HSTU, ULTRA-HSTU), ByteDance (Lance, Precise, RankMixer), Apple (SGE), NVIDIA (Nemotron 3 Super, DiLaDiff), Google DeepMind (Gemini Embedding 2, AGI Framework), Microsoft Research Asia (SkillOpt)
- Highlights: Shannon Scaling Law, Gated Attention (NeurIPS Best), Artificial Hivemind, 1000-Layer RL, Diffusion Memorization Theory, Transformers Inherently Succinct (ICLR 2026 Outstanding), SAM 3D (CVPR Best), StreamingTalker (AAAI), Bi-NAC (ICML), HyFunc + Causal Attention + BenchBench (KDD), Infini-gram mini + LingGym (EMNLP), Lance multimodal + Nemotron 3 Super hybrid MoE + SGE tree search
- Meta-trends: reasoning models explosion, hybrid attention (Mamba+Transformer), MoE standard, generative recommendation paradigm, RLVR post-training, agent → agent society
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-05-29] ingest | Awesome-CTR-Scaling Full Paper Coverage
- Operation: Created 38 new paper pages for all missing papers in the CTR scaling landscape
- Recommendation papers: understanding-scaling-laws-rec, dhen
- CTR papers: interformer, foundation-expert, llatte, ultra-hstu, solaris, versioned-late-materialization, rankmixer, onetrans, hyformer, zenith, tokenmixer-large, ug-sep, mixformer, longer, make-it-long-keep-it-fast, hhft, gpsd, est, hetermixer, sort, encode, muse, mtmixatt, mtfm, sparsectr, tokenformer, infnet, unimixer, chime, vql, cadet, hiformer, onepiece, beyond-dense-connectivity, lime, malloc
- Updated: wiki/index.md (CTR section split, 38 new entries)
- Updated: wiki/synthesis/ctr-scaling-landscape.md (status update)
- Coverage: 47/47 (100%) of Awesome-CTR-Scaling papers now have dedicated pages

## [2026-06-02] synthesis | arXiv Daily — AI Research Survey (June 2, 2026)
- Summary: wiki/synthesis/2026-06-02/arxiv-daily.md
- New pages: wiki/synthesis/2026-06-02/arxiv-daily.md
- Updated: wiki/index.md (synthesis section)
- Description: Survey of ~30 recent papers across generative recommendation, CTR prediction, LLM reasoning/RL, IR/search, games/MARL, and LLM agents

## [2026-06-02] synthesis | WorldQuant 101 Alpha 每日选股 — 2026-06-02
- New page: wiki/synthesis/2026-06-02/wq101-alpha-daily.md
- Updated: wiki/index.md (Synthesis section)
- Description: WorldQuant 101 Alpha factor-based US stock screening and ranking. Top 20 picks including MU, NVDA, AVGO, DELL, MSFT. S&P 500 at ATH 7,599.96. AI/tech momentum dominant. Factor breakdown: Alpha#1 (momentum) covers 15/20 stocks.

## [2026-06-02] restructure | 文档中心按角色总分结构重构
- New pages: wiki/roles/engineers.md, wiki/roles/researchers.md, wiki/roles/investors.md, wiki/roles/students.md, wiki/roles/followers.md
- Updated: wiki/index.md (added By-Role navigation section at top)
- Description: Restructured wiki documentation by 5 audience roles with 总-分 (general-to-specific) organization. Each role page grounded in actual code implementation facts:
  - 🔧 Engineers: anchored in llm.c (Packed128, deterministic memory, NCCL ZeRO-1), nanochat (full pipeline), micrograd (100-line autograd), nanogpt, bacterial code
  - 🔬 Researchers: 76+ papers across 9 categories, 7 methods, cross-referenced concepts
  - 📈 Investors: daily reports, tech report digests, WQ101 alpha, company entities
  - 📚 Students: learning path micrograd→nanogpt→nanochat→llm.c, Zero to Hero series
  - ⭐ Followers: 2024-2026 talk/X-post timeline, concept invention history

## [2026-06-04] synthesis | conference-digest-2026-06-04
- New page: wiki/synthesis/2026-06-04/conference-digest.md
- Coverage: 12+ conferences (ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, CVPR 2026, KDD 2026, ACL 2025, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) + arXiv + 8 industry labs (ByteDance, Meta, Microsoft, Google DeepMind, Apple, Alibaba, Kuaishou, Tencent, Meituan, Netflix, etc.)
- Papers covered: 100+ entries across LLM training theory, recommendation/CTR, agent systems, multi-modal/generative models, games/code, alignment/safety
- Updated: wiki/index.md, wiki/log.md

## [2026-06-05] synthesis | Conference & arXiv Digest — 2026-06-05 全面版（NeurIPS Best / ICLR 2026 / CVPR 2026 / EMNLP 2025 / RecSys 2025 / SIGIR 2026 / AAAI 2026 / KDD 2026 + 各大实验室）
- New page: wiki/synthesis/2026-06-05/conference-digest.md
- Coverage: 12+ venues (NeurIPS 2025 Best Papers, ICLR 2026 accepted list, CVPR 2026 accepted papers, EMNLP 2025 awards, RecSys 2025 accepted papers, SIGIR 2026 papers, AAAI 2026 proceedings, KDD 2026 Cycle 1&2 papers, WWW 2026 papers, CIKM 2025)
- Industry labs: ByteDance (HyFormer, TokenMixer-Large, MixFormer), Microsoft Research (FlexRec, R3-REC, Learned Verbalization, Governable Personalization), Apple (SRLM, SGE, LaCy, MixAtlas, Amortized MIPS), Amazon (User Agency, AgentDR), Alibaba (SIGMA, MGOE), Tencent (OneRanker, R2Rank, TencentGR), NVIDIA (NeMo-4-PayPal), Anthropic (Claude Code Design Space), OpenAI (GPT-5 System Card), DeepSeek (ReaLM-Retrieve), Meta (Sparsity 2:4 Beyond), Google DeepMind (Gemini 3 Pro Image)
- Key themes: LLM4Rec convergence, CTR scaling laws, agent systems maturation, data quality revolution, MoE standardization, generative recommendation paradigm
- Total papers referenced: 80+ across all sections
- Updated: wiki/index.md, wiki/log.md

## [2026-06-05] search | arXiv Digest — AI & CTR (June 5, 2026)
- New page: wiki/synthesis/2026-06-05/arxiv-digest.md
- Surveyed: cs.AI (418 entries), cs.IR (28 entries), cs.LG (376 entries) from Fri 5 Jun 2026
- Papers highlighted: ~24 across CTR/Rec, AI/LLM Systems, Agents/Benchmarks
- Top picks: Scaling Laws for Behavioral Foundation Models, Agents' Last Exam (ALE), Evaluation Blind Spot theory, Trust but Don't Verify (epistemic blind spots), State Commitment Learning (CERL)
- Key themes: scaling laws for recommendation models, benchmark evaluation crisis, black-box agent optimization, CTR denoising as supervised learning
- Updated: wiki/index.md, wiki/log.md

## [2026-06-05] search | Tech Report Digest — 第七版 (2026-06-05)
- New page: wiki/synthesis/2026-06-05/tech-report-digest.md
- Coverage: 22+ institutions, 30+ reports
- Highlights: DeepSeek V4 (1.6T MoE, CSA/HCA, Muon), OpenAI GPT-5.5 (Agentic Coding), Meta Llama 4 + Muse Spark, Google Gemini 3.1 Pro (1M context), Anthropic Claude Opus 4.7/4.8 (SWE-bench 87.6%), Mistral Large 3 (675B MoE, pure RL), Qwen3 (36T tokens, 119 languages) + Qwen3.5 (Gated DeltaNet-2) + Qwen3.7 Max, Microsoft Phi-4 (data quality) + Phi-4-Reasoning-Vision (arXiv:2603.03975), Apple AFM (3B on-device, PT-MoE), NVIDIA Nemotron 3 (Mamba2-Transformer Hybrid MoE), xAI Grok-4.3 (Colossus 200K GPUs), Amazon Nova Premier, Zhipu GLM-5 (744B MoE, MIT), Moonshot Kimi K2.6 (1T MoE, 300-Agent Swarm), ByteDance Seed 2.0 (AIME 98.3), StepFun Step 3.7 Flash (198B, Apache 2.0), Yi-Lightning (arXiv:2412.01253), Intern-S1 (arXiv:2508.15763), Baichuan-Omni-1.5 (arXiv:2501.15368)
- Key themes: MoE domination, hybrid attention (Mamba2+Transformer), long-context (up to 10M), thinking mode standard, agentic AI core, open-source divergence, synthetic data training
- Updated: wiki/index.md, wiki/log.md

## [2026-06-10] search | arXiv Paper Check — AI & CTR (June 10, 2026)
- New page: wiki/synthesis/2026-06-10/arxiv-paper-check.md
- Surveyed: cs.AI, cs.LG, cs.IR (Jun 9–10, 2026 submissions)
- Papers highlighted: 22 across AI/ML Systems, LLM Training/Inference, Agents/Benchmarks, CTR/Recommendation
- Top picks: Target-SFT (unified SFT theory), ReasonAlloc (KV cache "Reasoning Wave"), Piper (programmable distributed training), ABC-Bench (LLMs > human experts in wet-lab), AIR (Kuaishou +3.446% GMV LLM cross-domain rec), Mult-DPO (set-wise DPO for recommenders), τ-Rec (agentic rec reliability cliff)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-09] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-09)
- New page: wiki/synthesis/2026-06-09/wq101-alpha-daily.md
- Applied Alpha#1/#6/#12/#19/#30/#41/#53 across 7 dimensions
- Top picks: NVDA(9), MRVL(8), AVGO(8), MU(8), INTC(8), MSFT(8), GOOGL(8), XOM(8), LMT(8), LLY(8), VRT(8), PANW(8)
- Market context: S&P ~7,430, SOX +4.6% rebound from -10.3% selloff
- Key catalysts: AAPL earnings(6/8), CPI(6/10), MSFT earnings(6/11), SpaceX IPO(6/12), GOOGL earnings(6/14)
- Sectors: 6 Semis, 3 Mega-cap Tech, 2 Energy, 2 Defense, 2 AI Infra, 2 Healthcare, 2 Financial, 1 Consumer Tech
- Updated: wiki/index.md, wiki/log.md

## [2026-06-04] synthesis | 投资日报 — 2026-06-04（美股/港股/A股科技与AI热点）
- New page: wiki/synthesis/2026-06-04/investment-daily.md
- 核心事件：Broadcom AVGO Q2 FY2026 财报炸裂 — 营收 $222 亿 +48% YoY，AI $108 亿 +143%，Q3 指引 $294 亿（AI +200%）；Alphabet $800 亿 AI 股权融资（伯克希尔 $100 亿）; GTC Taipei 最后一日（RTX Spark / N1X / Cosmos 3 / Marvell +32.5%）；港股 6/2 报复性反弹恒科 +4.72%（腾讯 +10.5%）
- 美股焦点：AVGO 盘后 +10%（高 confidence），DELL/HPE AI 服务器业绩爆发，Meta Business Agent 货币化 +3%，NVDA PC 芯片战略
- 港股焦点：恒科超卖反弹（PE 20x 近 5 年 10% 分位），腾讯 WeChat AI Agent + 混元大模型
- A股焦点：光模块（中际旭创/新易盛/天孚）> 半导体设备（北方华创/中微）> 国产算力（寒武纪/海光）> AI PC 概念（GTC 催化）
- 中概：智谱 AI/MiniMax 6 月 8 日纳入恒生科技（$12.5-17.5 亿被动资金）；FUTU -27.5%、TIGR -25.3% 券商暴跌
- AI 主题：Agentic AI Summit NY（6月4日），Meta Business Agent 货币化，Microsoft Copilot Agent，WeChat AI Agent 计划
- 风险提示：美伊冲突升级；AI 估值回调；中美芯片管制
- Updated: wiki/index.md, wiki/log.md

## [2026-06-05] synthesis | 投资日报 — 2026-06-05（美股/港股/A股/中概/新能源科技与AI热点）
- New page: wiki/synthesis/2026-06-05/investment-daily.md
- 美股焦点：Broadcom -12.59%（AI指引不及最高预期）；Alphabet $847.5亿股权融资（伯克希尔$100亿）；Parabolic 7（SanDisk +623% YTD、MRVL +32.5%、DELL AI服务器+757%）；NVIDIA COMPUTEX（RTX Spark/Vera CPU/$800亿回购）；Mag 7分化（NVDA唯一周涨，AMZN -7.6%最弱）
- 港股焦点：MiniMax/智谱AI 6月5日纳入恒生科技指数（南向资金预计HK$1390亿）；南向5月首次净流出HK$36亿（转向A股）；腾讯WeChat AI Agent即将上线；阿里+6.5% AI重估
- A股焦点：光模块领涨（中际旭创日成交¥438亿A股第一/新易盛¥337亿第二，均创新高）；CPU重回聚光灯（NVIDIA Vera/AMD Venice量产+涨价潮）；海光+68%营收；比亚迪4nm智驾芯片量产
- 中概：BABA云AI+40%（真武M890芯片），PDD三年¥1000亿自营"新拼亩"转型，JD 618开门红创纪录
- 新能源：15家品牌集体涨价（存储/碳酸锂/铜铝/购置税4重成本压力）；5月销量比亚迪38.3万辆/零跑8万新势力第一/小米3万
- AI主题：Agentic AI全面爆发（MSFT/WeChat/Meta）；Robotaxi全球竞赛（Tesla奥斯丁全都会区/NVIDIA DRIVE Hyperion全球/Uber Munich）；光互连CPO新纪元；三大IPO（SpaceX 6/12 + Anthropic + OpenAI）合计$3.55万亿抽水压力
- Updated: wiki/index.md, wiki/log.md

## [2026-06-05] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-05)
- New page: wiki/synthesis/2026-06-05/wq101-alpha-daily.md
- Applied Alpha#1/#6/#12/#19/#30/#41/#53 across 7 dimensions
- Top picks: MU(9), MRVL(9), DELL(9), SNDK(9), HPE(8), NVDA(8), AVGO(8)
- Sectors: 5 Semiconductors, 3 Storage, 2 AI Hardware, 3 Cloud/AI Software, 1 Financial, 1 Healthcare, 1 Energy, 1 Consumer Staples, 1 Semiconductor Equipment, 1 IT Infrastructure
- Market context: S&P 5K at 7,584 (+0.41%), Dow record 51,562, sector rotation Tech→Financials/Healthcare
- Key events: AVGO -12.59% post-earnings, MRVL +32.5% COMPUTEX, DELL AI server +757%, MU $1T market cap
- Updated: wiki/index.md, wiki/log.md

## [2026-06-05] search | arXiv Daily — AI Research Survey (June 5, 2026)
- New page: wiki/synthesis/2026-06-05/arxiv-daily.md
- Coverage: ~25 papers across LLM reasoning, diffusion LLMs, CTR prediction, advertising recommender systems, RL for games, and LLM safety/interpretability
- Companies featured: LinkedIn (CADET), Kuaishou (GR4AD), Meta (Memento), Tencent/Weixin (RankUp), Alibaba/Taobao (EST), Baidu (GRAB), RUCAIBox (DS-MLP)
- Key themes: Generative recommenders replacing DLRMs at scale (5 major platforms); latent reasoning + dLLMs as emerging LLM paradigms; agentic RL with convergence guarantees
- Updated: wiki/index.md, wiki/log.md

## [2026-06-08] search | arXiv Paper Check — AI & CTR (June 8, 2026) — updated
- Source: cs.AI (164 entries Mon), cs.IR (16 entries Mon), cs.LG cross-lists
- Papers highlighted: 28 across AI/LLM Systems, LLM Reasoning & Agents, AI Safety & CTR/RecSys, IR/RAG
- Top picks: How AI Agents Reshape Knowledge Work (Perplexity production data, 87% time reduction), DuMate-DeepResearch (SOTA deep research 61.95%), AARRI-Bench (research intern evaluation), Sim-to-Real MDP for agents (KDD Blue Sky), Scaling Laws for Behavioral FMs over user event sequences, DS-MLP CTR (TKDD), DyCon (ICML overthinking)
- Updated: wiki/synthesis/2026-06-08/arxiv-paper-check.md (added 5 new entries)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-08] search | 各大 AI 公司最新技术报告汇总 (第八版) — 22+ 家机构, 35+ 报告
- New page: wiki/synthesis/2026-06-08/tech-report-digest.md
- 相比 06-05 版新增/更新: Claude Opus 4.8 System Card (May 2026)、Claude Mythos Preview (Apr 2026, Capybara tier, 93.9% SWE-bench, 受限发布)、Gemini 3.5 Flash 完整规格 (Google I/O May 2026, agentic AI 全面优化)、GPT-5 arXiv v2 更新 (May 2026)、Gemma 4 开源发布 (Apr 2026)
- 新增完整 System Card 索引表 (22 份 System Card/Technical Report 的官方链接)
- 综合趋势更新: System Card 透明度提升、Agentic AI 全面核心化、安全层级细化 (Mythos 受限发布范式)、混合注意力架构崛起
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-06] search | arXiv Paper Check — AI & CTR (June 6, 2026)
- New page: wiki/synthesis/2026-06-06/arxiv-paper-check.md
- Surveyed: cs.AI (108 new + 172 cross, Fri 5 Jun), cs.LG (232 entries, Fri 5 Jun), cs.IR (20 entries, Fri 5 Jun), plus Sat 6 Jun RSS
- Papers highlighted: 27 across CTR/Rec and AI/LLM Systems
- Top picks: DS-MLP (dual-stream MLP + KD for CTR), LoopCTR (loop scaling, train-multi-loop infer-zero-loop), EST (Taobao unified sequence CTR), Agents' Last Exam (2.6% pass rate on GDP-relevant tasks), LeanMarathon (258 lemmas, 0 sorries across 4 Erdős problems), Image Generators are Generalist Vision Learners (Google/DeepMind emergent visual understanding)
- Key themes: CTR scaling laws heat up (5 industrial papers); economically valuable agent benchmarks; AI co-mathematician viable; transformers' fundamental state tracking limits proven
- Updated: wiki/index.md, wiki/log.md

## [2026-06-08] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20
- New page: wiki/synthesis/2026-06-08/wq101-alpha-daily.md
- Market context: Nasdaq -4.18% (worst since Apr 2025), SOX -10.3%, S&P 500 -2.64%, sector rotation Tech→Healthcare/Defense
- Factor application: Alpha#53 (reversal after SOX -10.3%) primary lens; Alpha#1 (momentum) for defense/healthcare; Alpha#41 (trend strength) for AI infrastructure
- Top picks: NVDA(9), AVGO(8), MRVL(8), MU(8), LHX(8), LLY(8), GS(8), VRT(8), PANW(8)
- Sectors: 5 Semiconductors, 3 Defense, 3 Healthcare, 2 Financials, 2 AI Infra, 3 Cloud/Tech, 1 Consumer Tech, 1 Consumer Electronics
- Key event risks: CPI (6/10), SpaceX IPO (6/12), escalating Iran-Israel conflict
- Updated: wiki/index.md, wiki/log.md

## [2026-06-08] synthesis | 投资日报 — 2026-06-08（美股/港股/A股/中概/新能源科技与AI热点）
- Updated: wiki/synthesis/2026-06-08/investment-daily.md
- 大盘：Nasdaq -4.18%（2025年4月来最大）、S&P -2.64%（结束9周连涨）；SOX半导体指数-10.3%（2020年3月来最差）；韩国KOSPI开盘暴跌8.37%触发熔断；半导体板块单日蒸发$1万亿
- 美股三大冲击：(1) Broadcom Q3 AI指引$160亿 vs 预期$172亿，AVGO -7.92%；(2) Alphabet $800亿股权融资（含伯克希尔$100亿），GOOGL -0.95%；(3) 5月非农172K vs 预期85K，10Y收益率4.54%，12月加息概率60%
- 半导体跌幅：MRVL -16.7%（+10天后将纳入S&P 500）、MU -13%（两日-20%）、INTC -11.3%（收$99.17）、AMD -10.9%（收$466.38）、NVDA -6.2%
- 大消息：Jensen Huang首尔发言称"可以低价买入"；SpaceX 6/12 IPO估值$1.77万亿；FOMC 6/16-17（Kevin Warsh首次主席会议）；Goldman预计AI基础设施总支出$7.6万亿（2026-2031）
- 港股：腾讯6/2 +10.46%（微信AI Agent催化），已回吐大部涨幅；美团+9.27%后回落；美团"小美"接入元宝；智谱AI/MiniMax 6/9纳入恒生科技指数；南向资金日均￥60亿+
- A股：中际旭创6/5单日成交¥583亿（A股历史第4），收跌7.81%；寒武纪高盛目标价¥2,406（维持买入）；联讯仪器¥2,120成2000元股王；AI千元股4只超越茅台；高盛上调寒武纪/下调浪潮信息预言"国产AI芯片崛起"
- 中概/EV：NIO 5月交付+62.3% YoY，ES9等待期17周，德银上调目标；BYD Great Tang SUV发布（预订单10万+），近52周低点（-78% from peak）；中国跨境监管打击老虎/富途，$540亿资产承压，利好港股通
- AI主题：Big 5 Capex合计$725B；Goldman $7.6万亿五年总投资；Marvell -16.7%（非基本面/机构获利了结）；AEP 63GW数据中心负荷（2030E）；存储涨价周期（DDR4 Q3再涨20%）；A股机器人板块异动（AI算力→机器人轮动）
- Updated: wiki/index.md, wiki/log.md

## [2026-06-09] synthesis | Conference Digest — 2026年6月全面版（顶会论文专题报告）
- New page: wiki/synthesis/2026-06-09/conference-digest.md
- Coverage: 13 venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) + arXiv industry highlights
- Papers covered: 100+ across all sections
- Labs covered: ByteDance, Alibaba, Tencent, Kuaishou, Meta, Google DeepMind, Microsoft Research, OpenAI, Anthropic, NVIDIA, Apple, Amazon, Meituan
- Key themes: Gated Attention (NeurIPS Best), Diffusion LLM rise (LLaDA), Mamba-3 (ICLR 2026 Oral), RLVR critique, Generative recommendation paradigm, CTR scaling laws, Agent systems maturation, Industry lab highlights (ByteDance Lance, NVIDIA DiLaDiff)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-09] search | arXiv Paper Check — AI & CTR (June 9, 2026)
- New page: wiki/synthesis/2026-06-09/arxiv-paper-check.md
- Sources: cs.AI (34 new, 287 total) + cs.IR (14 new, 26 total) — Mon 8 Jun 2026
- Top picks: Lean4Agent (formal agent verification via Lean4), Don't Just Fix it in Post (ICML 2026 Oral, training dynamics science), OpenSkill (zero-supervision self-evolving agents), GBLA (SIGIR 2026, 8.2× linear attention speedup), AEGIS (backup reflex for physical AI), Attack Selection (strategic attackers break control evals), DyCon (ICML 2026, overthinking mitigation), DREAM (cold-start SIDs in generative rec), Bradley-Terry Rankings (KDD 2026, rec algorithm comparison methodology), RISE (agentic search interaction spaces)
- Key themes: formal verification for agents, training dynamics as science, self-evolving agents, linear attention for long sequences, generative recommendation maturation, safety realism, agentic search paradigm
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-09] synthesis | 投资日报 — 2026-06-09（美股/港股/A股/中概/新能源科技与AI热点）
- New page: wiki/synthesis/2026-06-09/investment-daily.md
- 核心事件：Apple WWDC发布Siri AI (基于Gemini 1.2T参数); NVIDIA韩国周6项重大合作(AI Factory); Broadcom Q2 AI营收$10.8B(+143%)但AI指引miss触发板块回调后6/8反弹; 国家数据局Token交易新政; 燧原/粤芯6/15上会; OpenAI/Anthropic/SpaceX三巨头IPO竞赛
- 美股反弹日：S&P 500 +0.30%, Nasdaq +0.86%; MRVL+9%(S&P 500纳入), MU+7%, NVDA+1.73%, GLW+9%(Amazon光纤协议), AAPL-1.9%(WWDC)
- 港股：恒生+0.42%; 腾讯微信AI Agent 7月灰度测试; 中国AI IPO潮持续
- A股：6/8大跌后企稳(上证-1.70%→-0.19%); 数据Token交易概念; 存储涨价确认
- 中概：ADR退市风险Goldman维持66%概率; BABA/PDD/JD承压
- EV：BYD 5月376,990辆结束8月下降; 蔚来37,705辆+62%；零跑81,569辆+81%
- 本周焦点：6/10 CPI + 6/11 FOMC + 6/12 SpaceX IPO + 6/15 燧原/粤芯上会
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-10] synthesis | arXiv Daily — AI Research Survey
- New page: wiki/synthesis/2026-06-10/arxiv-daily.md
- Coverage: 17 papers across LLM reasoning, diffusion LMs, recommendation systems, CTR prediction, games/RL, agent memory, benchmarks
- Key papers: ACTS (CoT steering), FLARE (hybrid AR+diffusion), RGCD-Rep (Kuaishou cross-domain rec), CADET (LinkedIn CTR), Game-RL (VLM reasoning via games), MRAgent (graph memory, ICML 2026)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-10] synthesis | Conference Digest — 2026年AI/ML顶级会议论文全景
- New page: wiki/synthesis/2026-06-10/conference-digest.md
- Coverage: 13 venues (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, ACL/EACL 2026, EMNLP 2025, KDD 2026, SIGIR 2026, WWW 2026, RecSys 2025) + arXiv industry papers
- Sections: 18 categories spanning LLM architecture, diffusion, agents, CTR prediction, games, SSMs, recommendation systems, RL, alignment, efficiency
- Best papers covered: Gated Attention (NeurIPS), 1000-Layer SSL RL (NeurIPS), Why Diffusion Don't Memorize (NeurIPS), D4RT (CVPR Best), O-Voxel (CVPR Best Student), Learning Unmasking Policies (ICML Oral), Transformers are Succinct (ICLR Outstanding), Polar Express (ICLR HM)
- Industry CTR papers: CADET (LinkedIn), EST (Alibaba), GRAB (Baidu), LoopCTR (Alibaba), GR4AD (Kuaishou), TokenMixer-Large (ByteDance), HeMix (AMAP), RankUp (Tencent), S-GRec (Tencent), SparseCTR, HyFormer (ByteDance), DAIAN
- AI labs: Google DeepMind, Meta FAIR, OpenAI, Anthropic, NVIDIA, Microsoft Research, Apple, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, LinkedIn, Pinterest, Walmart, Amazon, Spotify
- Updated: wiki/index.md, wiki/log.md
