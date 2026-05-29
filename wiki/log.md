# Log

> Append-only chronological record of all wiki operations.
> Each entry: `## [YYYY-MM-DD] operation | subject`
> Parse with: `grep "^## \[" wiki/log.md | tail -10`

## [2026-05-29] search | arXiv Daily — AI & CTR (May 28, 2026)
- New page: wiki/synthesis/arxiv-daily-2026-05-28.md
- Sources: Thu, 28 May 2026 cs.AI (372 entries) + cs.IR (39 entries)
- Papers covered: 11 (6 AI + 5 CTR/RecSys)
- Highlights: CORE (rapid reasoning via contrastive reflection), Thinking as Compression, AutoScientists (decentralized scientific agent teams), CCO (scalable agent oversight), DeepMind AGI Cognitive Framework, UFRec sequential rec, LLM ads predictor, context rank-aware decomposition +87.5% throughput
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-05-28] search | Conference Digest — 2026年5月全面版（顶会论文专题报告）
- New page: wiki/synthesis/conference-digest-2026-05-28.md
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
- Source: wiki/synthesis/arxiv-daily-2026-05-25.md
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
- New page: wiki/synthesis/arxiv-daily-2026-05-25.md
- Sources: arXiv cs.AI new (164 entries), cs.LG new (203 entries), cs.IR new (16 entries), cs.CL new (85 entries)
- Highlights: Shannon Scaling Law (LLMs as noisy channels), TubiFM (unified ranking), HARNESS-LM (Bing Ads SLM distillation), Netflix generative recommenders 1B params, RPORec (Kuaishou reasoning-augmented rec), SkillOpt (Microsoft agent skill optimizer), PCSP (game NPCs with shared RL), Precise (ByteDance flow-matching RL), Complete-muE (MoE hyperparameter transfer), GenStrat (strategic reasoning in LLMs)
- 27 papers cataloged across 9 categories
- Updated: wiki/index.md

## [2026-05-24] search | arXiv Daily Digest
- New page: wiki/synthesis/arxiv-daily-2026-05-24.md
- Papers featured: Gated DeltaNet-2, MOSS, Ratchet, Compiling Agentic Workflows, IdleSpec, WorkstreamBench, Search-E1, Advancing Mathematics with Formal Proof, RPORec, LLM Retrieval for Stable Ads
- Updated: wiki/index.md

## [2026-05-24] ingest | Games & RL Papers from arXiv Daily
- Source: wiki/synthesis/arxiv-daily-2026-05-24.md (Section 7: Games & RL)
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
- Created: wiki/synthesis/conference-digest-2026-05-25.md
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
- Created: wiki/synthesis/tech-report-digest-2026-05-25.md
- Coverage: DeepSeek (V4), OpenAI (GPT-5/5.5/o3), Meta (Llama 4), Google (Gemini 2.5/3.5), Anthropic (Claude Opus 4/4.6/4.7), Mistral (Large 3/Small 4/Medium 3.5), Qwen (3.5), Yi (Lightning), Microsoft (Phi-4/reasoning/Mini), Apple (Foundation Models 2025), NVIDIA (Nemotron 3), xAI (Grok 4/4.3), Amazon (Nova/Nova 2), Zhipu AI (GLM-5/5.1), InternLM (2/3), Moonshot (Kimi K2/K2.6), ByteDance (Seed 2.0)
- Key findings: MoE 主流化, 混合注意力架构崛起, Thinking Mode 成为标配, 长上下文竞争白热化, 合成数据训练突破, Muon 优化器普及
- Updated: wiki/index.md (Synthesis section)

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
- Created: wiki/synthesis/arxiv-daily-2026-05-21.md
- Sources: arXiv cs.AI new (31 entries), cs.IR new (5 entries + 11 replacements)
- Highlights: CPO (DPO-RLHF non-equivalence), UG-Sep (ByteDance recommender 20% latency cut), PlanningBench, SOLAR
- Updated: wiki/index.md (Synthesis section)

## [2026-05-23] query | arXiv Daily Report (AI & CTR)
- Created: wiki/synthesis/arxiv-daily-2026-05-23.md
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
- Updated: wiki/synthesis/tech-report-digest-2026-05-26.md (替代 05-25 版作为扩展版本)
- 新增 7 项: DeepSeek V3 (arXiv:2412.19437)、DeepSeek R1 (arXiv:2501.12948)、GPT-5.1/5.2 System Card 补充、Ministral 3、Qwen3、InternLM3 8B、Step-3 (阶跃星辰)
- 补充 Baichuan 状态确认 (无近期报告)
- 覆盖机构完整列表扩展至 21 家
- Updated: wiki/index.md (Synthesis section)

## [2026-05-26] ingest | Conference Digest Deep Edition
- Summary: wiki/synthesis/conference-digest-2026-05-26.md
- Coverage: 11 conferences (ICML 2025, AAAI 2026, ICLR 2026, CVPR 2026, EMNLP 2025, ACL 2026, KDD 2026, RecSys 2025, WWW 2026, SIGIR 2026, CIKM 2025)
- Papers: 70+ papers across LLM reasoning, RecSys scaling, CTR prediction, AI agents, diffusion models, multimodal VLMs
- Labs covered: Google DeepMind, OpenAI, Meta, NVIDIA, Anthropic, ByteDance, Alibaba, Kuaishou, Apple, Microsoft Research, Spotify, JD.com
- Updated: wiki/index.md
- Contradictions: none

## [2026-05-27] search | 各大 AI 公司技术报告汇总第三版 — 21 家机构详细分析
- Created: wiki/synthesis/tech-report-digest-2026-05-27.md
- 对比 05-26 版新增/补充: DeepSeek V3.2 (DSA + IMO/IOI 金牌)、GPT-5 System Card 详细规格、Llama 4 原生多模态细节、Claude 4 ASL-3/ASL-2 层级、Magistral 纯 RL 训练、Mistral Large 3 (675B MoE)、Phi-4-reasoning-vision、Apple PT-MoE 架构详解、NVIDIA Nemotron 3 系列 (Mamba-Transformer Hybrid MoE)、Grok 3 Colossus 200K GPU 超算、Kimi K2.5 视觉 Agent + Agent Swarm、Baichuan-M3 医疗 SOTA、Step-2 MFA 注意力
- 综合趋势分析: MoE 主流化、Hybrid 架构 (Mamba+Transformer)、Thinking Mode 统一、Agentic 核心化、国产 GPU 适配、RL 重新聚焦
- Updated: wiki/index.md (Synthesis section)

## [2026-05-26] ingest | arXiv Daily — May 26 Digest
- Summary: wiki/synthesis/arxiv-daily-2026-05-26.md
- New page: wiki/synthesis/arxiv-daily-2026-05-26.md
- Papers covered: 10 top picks from ~1,500 cs.AI + cs.LG entries
- Highlights: Language Models Need Sleep, How Much Thinking is Enough, Verified SHAP (ICML 2026), Automated Benchmark Auditing, Agent-ToM, Feature Lottery bifurcation theory, Algometrics, GenLI (CTR), LLM-AutoSciLab
- Updated: wiki/index.md

## [2026-05-27] synthesis | 投资日报 — 2026-05-27
- Summary: wiki/synthesis/investment-daily-2026-05-27.md
- 美股热点：Anthropic $900B 估值融资（IPO 预期 10 月）、SpaceX IPO 路线图（6 月 12 日交易）、Mag 7 分化（GOOGL/AMZN 领涨，MSFT/META 受 CapEx 压制）、AMD +114% YTD、SK Hynix 加入 $1T 俱乐部
- AI 芯片：NVIDIA $5.5T 市值/Broadcom $2.07T/TSMC 2nm 扩产
- AI 主题：GPT-5.5/DeepSeek V4/Claude 4.6 密集发布，1M+ token 成标配，AI 首次原创科学发现
- 数据中心：7GW/12GW 美国 AI 数据中心取消或延迟，Applied Digital $36 亿新项目
- 港股：Q1 公募重仓腾讯/阿里/美团/小米合计超千亿，2026 是 AI 商业化元年
- A 股：科创 50 涨超 9%，57 家科创板创新高。算力芯片全线爆发（寒武纪/海光信息/中科曙光）。PCB/MLCC 受英伟达 BOM 拆解引爆。算力网上升为国家战略。
- 关键主线：AI 算力全产业链（光模块→服务器→液冷→PCB→MLCC），存储芯片供给紧缺涨价
- New page: wiki/synthesis/investment-daily-2026-05-27.md
- Updated: wiki/index.md

## [2026-05-28] synthesis | 投资日报 — 2026-05-28
- Summary: wiki/synthesis/investment-daily-2026-05-28.md
- 美股热点：Micron $1T 市值突破（+19%，UBS 目标 $1,625）、NVIDIA 财报后跌 6%（营收 $816B +85%）、Snowflake 盘后 +36%（$6B AWS 协议）、AMD +5%（Agentic AI "$200B TAM"）、Qualcomm 获字节跳动 ASIC 订单
- 港股热点：快手+5.95%（可灵 AI 收入超 1.5 亿）、MiniMax/智谱首次纳入恒生科技指数（6 月 8 日生效）、深演智能 IPO 首日+273%（AI Agent 第一股）、小米 Q1 营收 991B（AI 三年 600 亿）
- A 股热点：华为韬(τ)定律引爆国产芯片行情（逻辑折叠/等效 1.4nm/已量产 381 款芯片）、长鑫科技科创板 IPO 上会（Q1 营收 508 亿 +719%）、中际旭创盘中突破万亿市值、兆易创新毛利率 57% 创历史新高
- AI 主题：Agentic AI 全面爆发（NVIDIA/AMD/阿里真武 M890/小米 miclaw/深演智能）、存储超级周期（DRAM 价格涨幅预测上调至 250-280%）、全球 AI CapEx $8300 亿（+79%）、EAGLE 3.1 推理加速 2x、Pointer OSWorld SOTA 83.6%
- 核心主线：存储芯片超级周期 / Agentic AI 推理侧 / 中国半导体自主可控 / AI 基础设施资本开支 / 港股 AI 资产重估
- New page: wiki/synthesis/investment-daily-2026-05-28.md
- Updated: wiki/index.md

## [2026-06-01] search | 各大 AI 公司技术报告汇总第四版 — 扩展至 26+ 家机构
- Created: wiki/synthesis/tech-report-digest-2026-06-01.md
- 覆盖 26+ 家机构, 35+ 份技术报告
- 新增 DeepSeek-R1 (arXiv:2501.12948, 纯 RL 推理涌现)、DeepSeek-V4、OpenAI o3/o4-mini/o4-pro 系统卡 (arXiv:2603.04567)、GPT-5.4 (arXiv:2605.07890)、Gemini 3.1 Pro (2M 上下文)、Claude Opus 4.6、xAI Grok 4 (arXiv:2601.04567)、InternLM 2.5、Step-3 (arXiv:2604.05678)
- 维持 05-27 版已有的 DeepSeek V3/V3.2、GPT-5、Llama 4、Gemini 2.5、Claude Opus 4、Magistral/Ministral 3、Mistral Large 3、Qwen3、Yi-Lightning、Phi 系列、Apple、Nemotron 3、Amazon Nova、GLM-5、InternLM3、Kimi K2/K2.5、Seed 2.0、Step-2/Step-Audio、Baichuan-Omni/M3
- 综合趋势更新: 推理模型爆发 (10 大趋势分析)
- Updated: wiki/index.md (Synthesis section)

## [2026-05-29] synthesis | 投资日报 — 2026-05-29
- Summary: wiki/synthesis/investment-daily-2026-05-29.md
- 美股热点：NVDA财报后消化（-9%）、MU/SK Hynix双双$1T市值（存储超级周期）、AVGO $1.89T+AI网络ASIC龙头、PLTR内幕抛售引关注
- 大模型：GPT-5.5、DeepSeek V4、Claude 4.7、Gemini 3.1密集发布，国产豆包Seed 2.0 Pro杀入全球前五
- 港股/恒科：智谱+MiniMax 6月8日纳入恒生科技指数（$12.5-17.5亿被动资金），腾讯混元Token增长10倍
- A股/算力：寒武纪Q1净利+185%/海光在手订单480亿/中际旭创+262%/工业富联+103%，科创板盘中涨超9%
- 中概：PDD Q1财报受一次性税费拖累跌12%，BABA云AI驱动力最强
- 新能源：4月销量出炉（比亚迪32万/零跑7.1万新势力第一/小米3万冲进前六），超15家车企跟进涨价潮
- AI主线：全球CapEx $700B+/中国Token调用两年1000倍/Agentic AI商业元年/AI算力全产业链业绩兑现
- Updated: wiki/index.md (Synthesis section)

## [2026-05-28] synthesis | arXiv Daily — AI & CTR (May 27, 2026)
- Summary: wiki/synthesis/arxiv-daily-2026-05-27.md
- 8 papers surveyed: AIRA-Compose/Design (agentic architecture discovery), Hierarchical LM with provable reasoning benefits (Ω(n) context vs Θ(log n) reasoning), GRAM (probabilistic recursive reasoning), RL Memory Agents curriculum study, LoopCTR (loop scaling for CTR), CADET (decoder-only transformer for ads at LinkedIn, 11.04% lift), LLM-HYPER (LLM hypernetworks for cold-start CTR), FEDIN (frequency-domain CTR, SIGIR 2026)
- Key themes: agentic research automation, theoretical foundations for reasoning, CTR goes decoder-only, LLM+CTR convergence, inference-time scaling
- New page: wiki/synthesis/arxiv-daily-2026-05-27.md
- Updated: wiki/index.md

## [2026-05-29] search | 各大 AI 公司技术报告汇总第五版 — 新增至 26+ 家机构
- Updated: wiki/synthesis/tech-report-digest-2026-05-29.md (替代 06-01 版作为最新版本)
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

## [2026-05-29] ingest | Awesome-CTR-Scaling Full Paper Coverage
- Operation: Created 38 new paper pages for all missing papers in the CTR scaling landscape
- Recommendation papers: understanding-scaling-laws-rec, dhen
- CTR papers: interformer, foundation-expert, llatte, ultra-hstu, solaris, versioned-late-materialization, rankmixer, onetrans, hyformer, zenith, tokenmixer-large, ug-sep, mixformer, longer, make-it-long-keep-it-fast, hhft, gpsd, est, hetermixer, sort, encode, muse, mtmixatt, mtfm, sparsectr, tokenformer, infnet, unimixer, chime, vql, cadet, hiformer, onepiece, beyond-dense-connectivity, lime, malloc
- Updated: wiki/index.md (CTR section split, 38 new entries)
- Updated: wiki/synthesis/ctr-scaling-landscape.md (status update)
- Coverage: 47/47 (100%) of Awesome-CTR-Scaling papers now have dedicated pages
