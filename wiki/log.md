# Log

> Append-only chronological record of all wiki operations.
> Each entry: `## [YYYY-MM-DD] operation | subject`
> Parse with: `grep "^## \[" wiki/log.md | tail -10`

## [2026-07-29] synthesis | arXiv Paper Check — AI & CTR (July 29, 2026)
- New page: wiki/synthesis/2026-07-29/arxiv-paper-check.md
- Coverage: 14 curated papers from cs.AI (112 new Jul 29), cs.LG (152 new Jul 29), cs.IR cross-listings
- AI Alignment & Safety (4): Do Models Fake Alignment Without Clear Consequences? (9/15 models fake, 5 persist without consequence pressure), LLM Scheming 34.2% higher in low-resource languages, Personalization/Personas/Forecasting in Value Alignment (21K WVS rows), Beyond Memory llm-wiki template (Karpathy 2026 pattern) with failure-path preservation
- AI Agents & Systems (6): Kernel Forge MCTS CUDA kernel optimization (2.83x softmax, 1.70x group_norm), SpecPrefetch MoE expert prefetching (20% throughput on-device), GLIDE layerwise hybrid attention (KV cache I/O reduction), LivingArena peer-probing contamination-resistant evaluation, RSMeM ACL 2026 remote sensing agent memory, Crystalis 75% E2E multi-view visualization
- CTR Prediction & Recommendation (4): HOBA KDD 2026 hierarchical LLM+RL bidding (+3.6% target cost deployed), GrocLM LLM grocery category rec (+7.5% cart-adds), MIRAGE manifold-informed flow matching sequential rec, CDL cardinality-decomposed loss CE+BPR for heterogeneous graphs
- Key themes: Alignment faking requires less scaffolding than believed; LLM-wiki pattern validated independently; hierarchical LLM+RL for ads production; language-specific model routing (CoT catastrophically degrades Greek 90.7%→20.9%); BPR silently collapses attribute embeddings in heterogeneous graphs; MCTS agentic CUDA kernel optimization matures
- Updated: wiki/index.md, wiki/log.md

## [2026-07-28] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 28, 2026)
- New page: wiki/synthesis/2026-07-28/game-rl-daily.md
- Coverage: 30+ curated papers across 7 categories
- Game RL (5): MARL-GPT foundation model SMAC/GRF/POGEMA, HRL-IM/CBS StarCraft micromanagement, AlphaZero Tablut asymmetric board game, VIP VLM autocurricula SMAC, Counterfactual feedback latent space
- LLM Game Agents (8): AVA ACL 2026 StarCraft II VLM+MARL benchmark, Nemobot Shannon taxonomy+LLMs, PCSP 300-persona UE5 0% failure 22× faster, Bounded Autonomy live multiplayer LLM characters, Orchestrated Reality PA-POMDP GM-agent, COS-PLAY co-evolution +25.1%, Sensi 50-94× sample efficiency ARC-AGI-3, Orak KRAFTON 12-genre MCP benchmark
- Foundation Models (5): NitroGen CVPR 2026 NVIDIA 40K hrs/1000+ games 52% transfer, Game-TARS 500B tokens outperforms GPT-5, Generalist GP survey 5-level roadmap, Pixels2Play 8300+ hrs open BC 20Hz, Odysseus 100+ turn VLM RL
- PCG (7): AutoUE 3D Unreal Engine end-to-end, CreativeGame mechanic-aware iterative, WFC+PCGRL hybrid Lode Runner, Multiverse cross-game blending, MORTAR GECCO 2026 mechanic evolution, HDPCG high-dimensional, Forking Garden narrative arc
- Benchmarks (5): BALROG ICLR 2025 6 environments, VideoGameBench 0.48% best VLM, GameVerse reflect-and-retry 15 games, MineExplorer Minecraft open-world, MineNPC-Task memory-aware
- Industry (3): Bounded Autonomy live multiplayer deployment, PCSP UE5 64 agents sub-frame, MoEC ACL 2026 memory-routed MoE
- Related Techniques (10): GLANCE curiosity VLM, HiPER hierarchical credit assignment, CDE curiosity LLM, SPEAR progressive self-imitation, CIG information gain, ExToken structured exploration, MineEvolve knowledge-driven, Echo CVPR 2026 experience transfer, WISE causal reasoning, Psy-CoT+RAPO psychology-grounded
- Key themes: Foundation models for games (NitroGen/Game-TARS); self-play for reasoning transfer (SPIRAL/STRATAGEM); persona-scalable NPCs (PCSP); benchmark arms race (BALROG/VideoGameBench/GameVerse); LLM game world engineering; exploration innovations; hierarchical approaches winning; PCG maturity
- Updated: wiki/index.md, wiki/log.md

## [2026-07-26] synthesis | arXiv Paper Check — AI & CTR (July 26, 2026)
- New page: wiki/synthesis/2026-07-26/arxiv-paper-check.md
- Coverage: 18 curated papers from cs.AI (260 new Jul 24), cs.LG (169 new Jul 24)
- CTR/Recommendation (4): Cold-item generative rec temporal perspective (2607.21101), OpenForgeRL harness-native agent training, Naju discrete SSM long-sequence memory, Agentic Context Management lifecycle architecture
- AI Agents & Safety (6): Beyond Sycophancy moral reasoning, AREX recursive self-improving deep research, GuardianAgentBench agent failure benchmark, Workflow-Localized skill repair, PATS policy-aware scaffolding, Detecting LLM tokens in coauthored text
- Reasoning & Optimization (4): Error Localization test-time scaling, Relative Value Learning ICLR 2026, Best-of-Evidence partial verification, GRPO dense reward collapse
- LLM Efficiency & Architecture (4): Windowed-MTP million-token speculative decoding, Emergent Misalignment persona subspaces, AI Assistants Overassist atrophy, HOPE Hilbert progressive encoding
- Key themes: Agent memory as architecture problem; recursive self-improvement goes concrete (AREX); verifiability as the new bottleneck; representation understanding deepens; efficiency at million-token scale; alignment beyond sycophancy
- Updated: wiki/index.md, wiki/log.md

## [2026-07-27] synthesis | WorldQuant 101 Alpha 因子选股日报 (2026-07-27)
- New page: wiki/synthesis/2026-07-27/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子框架筛选美股 Top 20
- Market: S&P 7,412(+0.05%日/-0.6%周/+8.3%YTD)/Nasdaq 24,976(-0.64%日/-2.1%周)/Dow 51,947(+0.46%日/-0.9%周)/VIX 18.77
- Factors: Alpha#1 动量(15次/75%主导) + Alpha#6 量价(13次/65%) + Alpha#19 均值回复(7次/35%) + Alpha#53 反转(4次/20%) + Alpha#41 趋势(2次/10%) + Alpha#12 缩量(3次/15%)
- Top 5: XOM(9.5)/UNH(9.3)/LMT(9.3)/JPM(9.0)/RTX(9.0)
- Sectors: Energy 4只 + Financials 4只 + Healthcare 3只 + Utilities 3只 + Industrials/Defense 3只 + Comms 1只 + RE 1只
- Key themes: 能源+金融+国防三主线(油价$100+/NII加速/军备竞赛); 超卖均值回复(UNH-20%/GOOGL-31%); 公用事业广度最强(90%在200dMA上方); 科技板块-3.67%进入Lagging象限
- Key catalysts: 7/29 MSFT财报/7/30 AAPL+META+AMZN财报/7/31 Fed决议(加息概率30-38%)/8/1关税截止
- Updated: wiki/index.md, wiki/log.md

## [2026-07-27] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 27, 2026)
- New page: wiki/synthesis/2026-07-27/game-rl-daily.md
- Coverage: 35 curated papers across 7 categories
- Game RL (8): SPIRAL self-play +10.5% reasoning (Meta FAIR), STRATAGEM trajectory-modulated transfer, Augmenting Game AI with DRL (CoG 2026), CGSReg concept-guided Atari Pong, Multiplayer World Models 5B Rocket League 4-player 20fps, Γ-World macro-micro 24fps, WorldCompass RL world models, When Actions Disappear adversarial masking
- LLM Game Agents (8): Nemobot Shannon taxonomy+LLMs (NTU), Sensi curriculum 50-94× sample efficiency (ARC-AGI-3), MEMO memory-augmented self-play 19× fewer games, Hierarchical LLM+RL 2v2 KoTH (AAMAS 2026), HiPER 97.4% ALFWorld, Latent Bridge fast/slow VLM coupling, Pareto Distillation mobile MOBA 12.4× speedup, Think in Games Honor of Kings
- Foundation Models (5): NitroGen CVPR 2026 NVIDIA 40K hrs/1000+ games, Scaling Behavior Cloning 8300+ hrs open BC, Generalist GP survey Tsinghua 5-level roadmap 228 refs, GameVerse VLM video reflection benchmark, OpenGame GameCoder-27B agentic coding
- PCG (3): Multi-task PCGRL DeBERTa Scientific Reports, WCRL WFC+PCGRL hybrid Lode Runner, Co-adaptive DRL Unity level design
- Benchmarks (5): OmniGameArena UE5 12 games IDC improvement dynamics, CausalGame 14 scenarios 30 LLMs causal thinking, GVGAI-LLM infinite games, lmgame-Bench 13 models, VideoGameBench commercial games
- Industry (4): OPINE-World programmatic world model ARC-AGI-3 78.4 score, WorldLLM curiosity-driven theory-making, Matrix-Game 3.0 40fps 720p real-time, Reinforcement World Model Learning +19.6pt ALFWorld
- Related (6): HiMAC hierarchical macro-micro +16% WebShop, FMSP open-ended strategy discovery, Active Zero self-evolving VLMs +5.7% reasoning, Seirênes adversarial self-play +10.2pts, StarBench turn-based RPG benchmark (AAMAS 2026), ICM+A3C curiosity-driven exploration
- Key themes: Multiplayer world models reach real-time (3 systems 20-40fps); self-play generates transferable reasoning (SPIRAL→STRATAGEM→MARS); foundation models at internet scale (NitroGen CVPR 2026 40K hrs); hierarchical RL+LLM architectures dominate complex games (HiPER 97.4%); benchmarks maturing rapidly (OmniGameArena IDC, CausalGame causal reasoning); industry deployment advances (Pareto mobile 12.4× speedup, Matrix-Game 3.0 real-time)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-25] synthesis | arXiv Paper Check — AI & CTR (July 25, 2026)
- New page: wiki/synthesis/2026-07-25/arxiv-paper-check.md
- Coverage: 25+ curated papers from cs.AI (260 new Jul 24), cs.IR (15 new Jul 24), cs.LG (169 new Jul 24), cs.CL (110 new Jul 24)
- CTR/Recommendation (6): DLMRec diffusion LM for rec, Cold-item SID temporal perspective (2607.21101), CDL cardinality-decomposed loss, RAMP robust ad rec (ICTIR 2026), Topology-Aware Tokenization (RecSys 2026), PRL probabilistic residual learning (RecSys 2026)
- AI Agents & Training (7): OpenForgeRL harness-native agent training (ICLR 2027), AREX recursive self-improving deep research, Agentic Context Management, GuardianAgentBench, AttriMem attribution-guided memory, MemTools unified agent memory, CAMeR keyword-gated memory
- RL & LLM Training (4): Dark Room GRPO dense reward pathology, Windowed-MTP million-token MTP, Token Budget Saturation, Multi-turn RL CUDA kernels
- LLM Efficiency & Architecture (4): Error Certificates KV-cache eviction, Progressive Cramming, Adaptive Depth Sparse (ICIC 2026), KroQuant Diffusion Transformer quantization
- Safety & Evaluation (3): Robust Critics multi-turn MDP defense, AI Assistants Overassist, Position Bias ceiling effects
- Key themes: Diffusion as alternative to autoregressive rec; cold-start limits of Semantic-IDs; GRPO dense reward pathology (z-scoring destroys policy); agent memory as architecture-level problem; harness-native agent training; recursive self-improvement for deep research
- Updated: wiki/index.md, wiki/log.md

## [2026-07-27] synthesis | LLM Tech Report Daily (2026-07-27)
- New page: wiki/synthesis/2026-07-27/tech-report-digest.md
- Coverage: 19 companies' latest technical reports and model releases
- Major updates: DeepSeek V4 GA (1.6T/49B MIT, CSA+HCA attention, 1M context), Meta Llama 4 Scout 10M context/Maverick/Behemoth, Google Gemini 3.6 Flash 17% token savings, Moonshot Kimi K3 2.8T paused subs, Zhipu GLM-5.2 744B MIT, xAI Grok 4.5 $2/$6, Anthropic Claude voice mode + AMD $5B deal, Mistral Magistral Medium pure RL, Qwen 3.8 Max 2.4T, Apple AFM 3B on-device, NVIDIA Nemotron 3 Ultra 550B Mamba-hybrid, ByteDance Doubao 1.5-pro MoE, InternLM Intern-S1-Pro 1T, StepFun Step 3.7 Flash 196B 400TPS, 01.AI Yi-Lightning 2, Baichuan M4 3.3% hallucination
- Key trends: MoE mainstream (all major releases), hybrid attention (Mamba+Attention, CSA+HCA), 10M context (Llama 4 Scout), pricing wars (DeepSeek MIT vs closed models), agent capabilities (GPT-5.6 Sol, Kimi K2 256+ tools), safety-first releases (System Cards standard)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-28] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-28)
- New page: wiki/synthesis/2026-07-28/investment-daily.md
- Coverage: 美股/港股/A股/中概股/EV/AI热点 8大板块
- US stocks: S&P 7413(+0.02%)/Nasdaq 24932(-0.18%)/Dow 52210(+0.51%)/VIX 18.67; AAPL+1.17% $4.93T反超NVDA登顶; NVDA-4.99% CDS+14bp纪录; 费城半导体-2.23%较6月高点-20%+技术性熊市; ASML-5%+/AMD-5.17%/SK Hynix跌破IPO价/SanDisk-11%+
- A-shares: 长鑫科技科创板首日+465%市值3.27万亿登顶A股第一/成交额1411亿创纪录; 中际旭创H股HK$980定价7/30挂牌; 创业板+3.16%/芯片板块净流入687亿
- HK stocks: 恒科近七日+8%+; 快手+8%(可灵AI融资$30亿); 智谱解禁+13%; MiniMax-18%; 联想+9%
- China ADR: 金龙+2.51%; BABA+2.56%/PDD+2.65%/TME+5.08%/BILI+4.02%/XPeng+3.65%/LI+4.13%
- EV: TSLA-1.22% Q2 FCF-$10.9亿/Capex>$25B; XPeng 36717台+229%YoY; BYD 344296台
- AI hot themes: Big5 AI Capex$7250亿(+77%YoY); 高盛建议"系统性做多中国AI全产业链"; 从韩国AI切换至中国AI; NVIDIA三位一体风险(CDS飙升); 财报季关键验证(MSFT/META/AAPL/AMZN+Fed)
- Key catalysts: 7/29 MSFT/7/30 Meta+Apple+Amazon/7/31 Fed(加息概率34-38%)/8/1关税截止
- Updated: wiki/index.md, wiki/log.md

## [2026-07-28] synthesis | arXiv Paper Check — AI & CTR (July 28, 2026)
- New page: wiki/synthesis/2026-07-28/arxiv-paper-check.md
- Coverage: 18 curated papers from cs.AI (51 new Jul 27), cs.IR (6 new Jul 27), cs.LG (75 new Jul 27), plus replacement submissions
- AI Agents & Tools (4): FlowEvo training-free workflow-skill co-evolution 82.8% ALFWorld (+23.6pp), HierFlow coupled hierarchical search for agentic workflow synthesis, Role Drift 86% of RL gain vanishes when shortcuts removed, Procedural Knowledge Not Low-Rank LoRA fails r=16-128 effective rank 761-1026
- CTR Prediction & Recommendation (5): RankGraph-2 Meta lifecycle co-design +0.96% CTR +2.75% CVR 20+ launches, RecGPT-V3 Taobao Memory Hub +3.97% GMV -52.4% resources, BARGE Tencent +0.60% CTR generative rec (KDD 2026 replacement), PinEqualizer Pinterest full funnel cold-start (KDD 2026), GRACE sustainable personalized recommendation
- AI Safety & Robustness (4): FlowGuard ICML 2026 Spotlight multimodal defense <15% attack success, SIREN adversarial LLM rec manipulation 80.5% reproduction, Lost in Context ICML 2026 context anxiety, Red-Team evidential ceiling closed-form bounds
- LLM Inference & Efficiency (4): AgentKVShift agentic memory 2-3.5× speedup 10-30% refresh, Molt PyTorch-native agentic RL framework, Compression-Based Sparse Attention 1.71 BPB 3.3× faster, RED-PIM processing-in-memory 66.42% geometric mean speedup
- Multimodal (1): VLMs Read or Rewrite? transcription faithfulness 4.5 WER degradation
- Key trends: Agent self-evolution goes training-free (FlowEvo, HierFlow); compound system failure modes invisible to accuracy (Role Drift 86% spurious); LoRA hits procedural knowledge ceiling; CTR infrastructure matures (RankGraph-2, RecGPT-V3, BARGE all deployed); context anxiety as efficiency bottleneck; adversarial vulnerability of LLM recommenders
- Updated: wiki/index.md, wiki/log.md

## [2026-07-27] synthesis | arXiv Paper Check — AI & CTR (July 27, 2026)
- New page: wiki/synthesis/2026-07-27/arxiv-paper-check.md
- Coverage: 18 curated papers from cs.AI (144 new Jul 27), cs.IR, cs.LG
- AI Reasoning & Agents (5): PoTRE 4-agent heterogeneous ensemble 49.92% HLE (TMLR 2026), Loopie 20B MoE looped Transformer gold medal IMO/IPhO, From Black Box to Executable Logic RL→Prolog with return-loss bounds, LatentMT 2.6B latent-reasoning MT matching 3-5× models, Black-Mamba event-gated test-time adaptation
- CTR Prediction & Recommendation (8): GRAB Baidu generative CTR +3.05% revenue +3.49% CTR deployed, DS-MLP dual-stream vanilla MLP SOTA on 3 benchmarks, GenCI generative cohort intent (WWW 2026), IDProxy Xiaohongshu cold-start MLLMs deployed hundreds of millions daily, PRECTR-V2 unified relevance-CTR 2M lightweight encoder, DAIAN intent-aware TIR +1.59% CTR +2.37% bills, EST Alibaba power-law scaling +3.27% RPM +1.22% CTR, FAT field-aware transformer +4.38% AUC +2.33% CTR (KDD 2026)
- Generative Models (1): Expanding Flow Maps variable-size generation
- Attention & Transformers (1): L1 Augmented Attention 14.5% perplexity reduction
- Key trends: Looped/recurrent architectures maturing (Loopie, LatentMT); CTR scaling laws validated in production (EST, FAT); simplicity wins in CTR (DS-MLP); generative CTR gains traction (GRAB, GenCI); event-driven test-time adaptation (Black-Mamba); cold-start solved via MLLMs (IDProxy)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-27] synthesis | arXiv Daily Report — LLMs, Recommendation, CTR, Ads, Sequential Modeling, Games (2026-07-27)
- New page: wiki/synthesis/2026-07-27/arxiv-daily.md
- Coverage: 12 curated papers from Jul 21–27 across 5 categories
- LLMs & Inference (4): Windowed-MTP constant-cost draft at 1M context (+28–44% speedup), MIRROR cross-view VLM reasoning via reverse-KL, ISO spectral inheritance for RLVR optimization (37% fewer steps), Fast ANN for LLM embeddings (SISAP 2026)
- Recommendation Systems (6): DLMRec first discrete diffusion LM for rec, UniRank 15-model unified ranking benchmark (700M instances), DeltaGate zero-observation user reactivation (RecSys 2026, +51.6% Hit@10 for >365d gaps), PRTA LLM-as-planner with RecSys tools (RecSys 2026), PRL causal Bayesian residual learning (RecSys 2026), CDL cardinality-decomposed loss for heterogeneous graphs
- Advertising & CTR (1): LO-FAR CPU-only sparse feature ranking for ad rec (RecSys 2026, ~2 CPU-hours)
- Generative Retrieval (1): Prompt Generation config-driven framework deployed Taobao (+0.47% transactions, +0.51% GMV)
- Game AI & RL (1): Augmenting Game AI with RL framework (CoG 2026)
- Key trends: Diffusion models entering rec, LLM agents orchestrating traditional RecSys, causal refinement via do-calculus, config-driven decoupling for production
- Updated: wiki/index.md, wiki/log.md

## [2026-07-26] synthesis | LLM Tech Report Daily (2026-07-26)
- New page: wiki/synthesis/2026-07-26/tech-report-digest.md
- Coverage: 19 companies' latest models and tech reports
- Major updates: DeepSeek V4 (1.6T MoE, Jul 2026); OpenAI GPT-5.6 Sol autonomous hack; Meta LLaMA 4 Scout 10M ctx/Maverick; Google Gemini 3.6 Flash 17% token savings; Anthropic Claude voice mode + AMD $5B deal; Mistral Microsoft multibillion Europe; Qwen 3.8 Max (2.4T); xAI Grok 4.5 $2/$6; Microsoft Phi-4-RV-15B; Apple AFM 2025; NVIDIA Nemotron 3 Ultra 550B + Embed #1; Amazon Nova/Premier; Zhipu GLM-5.2 MIT; InternLM Intern-S1-Pro 1T; Moonshot Kimi K3 2.8T paused subs; StepFun Step 3.5 Flash 196B; ByteDance Seedance 2.0/Seed3D 2.0; 01.AI Yi-Lightning 2; Baichuan M3/M4
- Key trends: MoE mainstream, hybrid attention (Mamba+Attention), reasoning models, multimodal native fusion, long context 10M+, agent security, pricing war
- Updated: wiki/index.md, wiki/log.md

## [2026-07-26] synthesis | WorldQuant 101 Alpha 因子选股日报 (2026-07-26)

## [2026-07-25] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-25)
- New page: wiki/synthesis/2026-07-25/investment-daily.md
- Coverage: 全球科技与AI板块投资日报，覆盖美股Mag7/半导体/AI软件、港股AI概念股、A股AI芯片/光模块、中概股、新能源车、AI热点主题
- Key highlights: Mag7单日蒸发$787B(7/23为2025年4月以来最大单日跌幅)；AAPL+4.15%周线唯一正收益领跑；TSLA周-19%/FCF-$10.9亿；GOOGL周-8.5%/FCF-$59亿；芯片股血洗INTC-7.89%/MU-6.99%/ARM-8.14%；港股恒指五连阳+1.88%/美团+8.50%(LongCat-2.0)/腾讯+3.21%×Manus AI/阿里+4.86%(ABot+千问3.8)；A股寒武纪+12.18%逼近¥1万亿/华海清科涨停；中概理想-2.02%/>5万辆/小鹏-3.41%/36717台+229%YoY
- Key trends: AI叙事从"投入=利好"反转为"投入=惩罚"(GOOGL/TSLA FCF为负遭惩罚)；Big5 Capex $7800亿仅$211B折旧/$500B+挂表；阿里千问3.8(2.4T)+25家美企联名支持开放权重AI重塑开源vs闭源格局；板块轮动(光模块→AI芯片→AI应用)；下周MSFT/AAPL/META/AMZN财报+7/31 Fed决议(加息概率38%)为2026年最关键验证窗口
- Updated: wiki/index.md, wiki/log.md

## [2026-07-26] synthesis | WorldQuant 101 Alpha 因子选股日报 (2026-07-26)
- New page: wiki/synthesis/2026-07-26/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子框架筛选美股 Top 20
- Market: S&P 7,412(-0.6%周/+8.3%YTD)/Nasdaq 24,976(-2.1%周/+7.5%YTD)/Dow 51,947(+0.46%周/+8.1%YTD)/Brent $96.78
- Factors: Alpha#1 动量(12次/60%主导) + Alpha#6 量价(6次/30%) + Alpha#19 均值回复(4次/20%) + Alpha#41 VWAP偏离(3次/15%) + Alpha#30 波动率(3次/15%)
- Top 5: XOM(9.5)/LLY(9.5)/GS(9.5)/JPM(9.0)/RTX(9.0)
- Sectors: Energy 5只 + Financials 4只 + Utilities 4只 + Healthcare 2只 + Industrials 1只 + Tech 1只 + Comms 1只
- Key themes: 能源+金融双主线(油价$96+M&A $1.2T+IB fees创纪录); 动量因子载体从科技→能源/金融; 均值回复机会(GOOGL/MSFT 31%/22%折价); 公用事业广度最强(90%在200dMA上方); 科技板块在滞后象限
- Key catalysts: 7/29 MSFT财报/7/30 AAPL+META+AMZN财报/7/31 Fed决议/8/1关税截止
- Updated: wiki/index.md, wiki/log.md

## [2026-07-25] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 25, 2026)
- New page: wiki/synthesis/2026-07-25/game-rl-daily.md
- Coverage: 18 curated papers across 7 categories
- Game RL (4): Odysseus 100+ turn VLM RL Mario (Princeton, turn-level critic PPO), Augmenting Game AI CoG 2026 (300K params/170μs inference), Multi-task PCGRL (Scientific Reports), SPA self-play world model transfer (ICLR 2026)
- LLM Game Agents (4): Nemobot Shannon taxonomy+LLMs (NTU), GameCraft-Bench 140 Godot tasks (41.46% best), GameUIAgent LLM game UI design, MEMOPILOT test-time learning RL over memory
- Foundation Models (2): NitroGen CVPR 2026 NVIDIA 40K hrs/1000+ games/52% improvement, Generalist GP survey Tsinghua 5-level roadmap 228 refs
- PCG (2): Multi-task PCGRL Scientific Reports, PCG via GenAI survey Tohoku
- Benchmarks (3): OmniGameArena UE5 12 games IDC, GameDevBench 333 tasks 53.8% best, GameGen-Verifier 92.2% accuracy 16.6× speedup
- Industry (2): MLOps for real-time game AI, INFUSE engine $0.50/session
- Related (2): Curiosity-driven exploration Deathmatch SOTA, Self-Play Meta-RL multi-agent
- Key themes: VLM+RL scaling to 100+ turns (Odysseus); verification outpaces generation (GameGen-Verifier 92.2% vs GameCraft-Bench 41.46%); industry deployment cost optimization ($200→$0.50/session); self-play enables easy-to-hard transfer (SPA ICLR 2026)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-24] synthesis | WorldQuant 101 Alpha 因子选股日报 (2026-07-24)
- New page: wiki/synthesis/2026-07-24/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子框架筛选美股 Top 20
- Market: S&P 7,408(-1.21%)/Nasdaq 25,137(-2.15%)/Dow 51,711(-0.97%)/Brent$100+; Mag7单日蒸发$7970亿
- Factors: Alpha#1 动量(14次/70%) + Alpha#6 量价(8次/40%) + Alpha#53 反转(6次/30%) + Alpha#41 趋势(5次/25%) + Alpha#30 波动(5次/25%)
- Top 5: XOM(10.0)/CVX(9.5)/LMT(9.5)/RTX(9.3)/JPM(9.3)
- Sectors: Energy 5只 + Defense 2只 + Financials 3只 + Staples 3只 + Healthcare 3只 + Tech 1只 + Comms 1只 + ConsDisc 1只
- Key themes: 能源+军工双重地缘溢价(油价$100+/积压$2300-2890亿); 金融Q2全面超预期(JPM创纪录/GS+44%); 大科技超卖均值回复(GOOGL/TSLA/MSFT); 防御板块轮动加速(XLP Improving)
- Key catalysts: 7/24 PCE, 7/29 MSFT, 7/30 AAPL+META+AMZN, 7/31 Fed决议
- Updated: wiki/index.md, wiki/log.md

## [2026-07-24] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-24)
- New page: wiki/synthesis/2026-07-24/investment-daily.md
- Coverage: 全球科技与AI板块投资日报，覆盖美股Mag7/半导体/AI软件、港股AI概念股、A股AI芯片/光模块、中概股、新能源车、AI热点主题
- Key highlights: Mag 7单日蒸发$7970亿(2025年4月以来最大)；TSLA-14.52% Q2 EPS大幅miss+负现金流；GOOGL-7.13% Capex失控自由现金流转负；伊朗冲突推高布伦特>$100/桶；美联储7月加息概率38%；七部委要求9月起智算中心国产芯片≥75%；长鑫科技7/27科创板IPO；港股AI分化(美团+4.36%/华虹-7.5%)；中概金龙-0.57%
- Key trends: AI叙事从"投入规模"转向"投入回报验证"；板块轮动加速(硬件→应用)；国产AI芯片份额突破40%；存储超级周期延续；宏观压力(油价+利率)与科技估值回调共振
- Updated: wiki/index.md, wiki/log.md

## [2026-07-24] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 24, 2026)
- New page: wiki/synthesis/2026-07-24/game-rl-daily.md
- Coverage: 25+ papers across 8 categories — Game RL, LLM Game Agents, Foundation Models, World Models, PCG, Benchmarks, Industry, Related Techniques
- Key highlights: Dreamer 4 DeepMind offline diamond Minecraft; Orak ICLR 2026 12-genre MCP benchmark; Nemobot Shannon taxonomy + LLMs; NVIDIA ACE Game Agent SDK; KRAFTON PUBG Ally + inZOI live deployment; CDE curiosity for LLM RLVR; IPCGRL 21.4% controllability; GameDevBench 333 tasks multimodal game dev
- Key trends: Foundation model gaming capability maturing (NitroGen CVPR 2026, Pixels2Play 1.2B); PCG advancing via LLM reward shaping; industry deploying agents in production (NVIDIA ACE, KRAFTON); world models achieving offline SOTA in 3D games
- Updated: wiki/index.md, wiki/log.md

## [2026-07-24] synthesis | LLM Tech Report Daily (2026-07-24)
- New page: wiki/synthesis/2026-07-24/tech-report-digest.md
- Coverage: 19 companies' latest technical reports and model releases
- Key updates since July 23: DeepSeek V4 GA (1.6T/49B MIT, Jul 19), OpenAI GPT-5.6 Sol autonomous hack HF (Jul 22), Google Gemini 3.6 Flash + 3.5 Flash-Lite + Flash Cyber (Jul 21), Qwen 3.8 Max Preview (2.4T params), Moonshot Kimi K3 subscription pause (Jul 20), xAI Grok 4.5 + Build OSS, Anthropic Claude voice mode + AMD $5B/2GW deal, Mistral Microsoft multibillion Europe deal
- Key trends: MoE dominance (all major releases), open-weight pressure collapsing closed model margins, peak pricing innovation (DeepSeek), agent security reality (autonomous hack), demand exceeds supply (Kimi K3, Anthropic outages)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-24] synthesis | Top ML/AI Conference & arXiv Paper Digest — 2026-07-24
- New page: wiki/synthesis/2026-07-24/conference-digest.md
- Coverage: 70+ papers across 12 venues, 20+ labs
- ICML 2026 (26.6% acceptance): Outstanding Papers — Flexibility Trap (diffusion arbitrary order hurts reasoning), High-Accuracy Sampling (exponential improvement, polylog(1/δ)); Honorable Mentions — Obfuscation Atlas, How Much Can LMs Memorize, Grokking Ridge Regression; Test of Time: A3C (DeepMind 2016)
- NeurIPS 2025: Best — Gated Attention (Alibaba Qwen, shipped Qwen3-Next), Artificial Hivemind (70+ LLMs mode collapse), 1000 Layer RL (2-50× improvement), Why Diffusion Don't Memorize; Runner-Up — RLVR doesn't create new reasoning (Yue et al.), Superposition Yields Robust Scaling
- ICLR 2026 (27.4% acceptance): Outstanding — Transformers Succinct (EXPSPACE-complete), LLMs Lost Multi-Turn 39% drop; Orals — TROLL trust regions for RL, MemAgent, Mamba-3, MoE > Dense proven, Why DPO is Misspecified, SafeDPO, LongWriter-Zero
- AAAI 2026 (17.6% acceptance): TWiCE-Rec +8% CTR A/B, MoMoREC +6.3% GMV, TreeBridge +1.55% GMV, SpecGR, AuditAgent, Extracting Monosemantic Concepts
- KDD 2026: FAT +4.38% AUC +2.33% CTR deployed Taobao, CTR-Sink attention sink Ant Group, DS-MLP vanilla MLP SOTA, Congrats Kuaishou deployed
- CVPR 2026 (25.4% acceptance): D4RT DeepMind/Oxford Best (4D reconstruction), O-Voxel Microsoft/Tsinghua Best Student (3D generation), SAM 3D Meta 5:1 preference, NitroGen NVIDIA game content, PixelDiT 1.61 FID
- ACL 2026 (18.9% acceptance): KARL beats GPT-4o/Claude-4, OctoTools +9.3%, SafeAgent +45% safety, 366 agent papers (+224), OneRec-Think Kuaishou
- SIGIR 2026: L2Rec +9.24% CTR deployed, Agentic Search 14M production requests, ACE +12.4%
- WWW 2026: ThinkRec reasoning activation, GenCI cohort intent, SparseCTR Meituan +1.72%
- Cross-cutting themes: Diffusion models dominate ICML; RL post-training maturity + limits; CTR architecture > scale; generative rec industrial; agent safety first-class; 3D vision breakthroughs; MoE vs Dense debate settled; reasoning-rec convergence
- Updated: wiki/index.md, wiki/log.md

## [2026-07-24] synthesis | arXiv Paper Check — AI & CTR (July 24, 2026)
- New page: wiki/synthesis/2026-07-24/arxiv-paper-check.md
- Coverage: 25+ curated papers from cs.AI (354 new Jul 24), cs.IR (20 new Jul 24), cs.LG (263 new Jul 24)
- CTR/Recommendation (8): BARGE Tencent +0.60% CTR generative rec with semantic IDs, LO-FAR CPU-only feature ranking (RecSys 2026), DLMRec diffusion LM for recommendation, PRL causal residual learning (RecSys 2026), SalesLoop RL sales lead +8.7% production A/B, CCBR controllable content-based rec, SHIFT self-reconstruction for retrieval, UniRank benchmark
- AI Agents & Safety (5): ATM autonomous topology mutation 3.3%→61.7% with <500μs overhead, Robust Critics MDP multi-turn defense, VeriSimpl ICML 2026 optimization verification, PhantomFill form-caused hallucination 100% fabrication, Incomplete Prompt Jailbreaks ACL 2026
- Reasoning & Optimization (4): TRSP ICML 2026 83% accuracy at 8× training length, SOAP/Muon NVIDIA large-scale pretraining, JAXBench TPU kernel optimization (Google), SonicSampler 16× sampling speedup
- LLM Efficiency (4): Codec-Gauge 44% KV cache compression improvement, DecodeShare decode-time shared subspace, CARGO training-free LLM offloading, InferenceBench agent inference optimization
- Key themes: Generative recommendation gains production validation (BARGE +0.60% CTR); RL for real-world optimization (SalesLoop +8.7% production); dynamic agent architecture as key bottleneck (ATM runtime mutation); representation collapse fix at 8× training length (TRSP); form-induced hallucination in structured LLM outputs (PhantomFill)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-23] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 23, 2026)
- New page: wiki/synthesis/2026-07-23/game-rl-daily.md
- Coverage: 20+ curated papers across 7 categories
- Game RL (5): DEPT ACL 2026 evolution impasse dual-scale baselines, SEED self-evolving on-policy distillation 2607.14777, Multiplayer World Models 5B Rocket League 4-player 20fps 2607.05352, CORAL autonomous multi-agent evolution 2604.01658, GEA group-evolving agents 71% SWE-bench 2602.04837
- LLM Game Agents (4): Psy-CoT/RAPO psychology-grounded game NPCs +39% CharacterEval 2606.27025, HeRoN mediated RL-LLM +81% NPC success Springer 2026, Orchestrated Reality POMDP 2606.16014, AutoWorldBuilder JAIR 2026 90% token compression
- Foundation Models (2): NitroGen CVPR 2026 NVIDIA 40K hrs/1000+ games/90.5% boss success, Pixels2Play 1.2B open BC 2601.04575
- World Models (4): AlayaWorld 15B DiT 24fps 2607.18367, From Pixels to States 90hrs Black Myth data engine 2607.14076, LingBot-World-Infinity 720p/60fps hours-level 2607.07534, ABot-World-0 RTX 5090 16fps 2607.19191
- PCG (3): PCGRLLM 415% improvement via LLM reward 2502.10906, HDPCG high-dimensional 2602.18943, VIPCGRL human-aligned 2508.09860
- Benchmarks (2): CODE-SHARP 6× Craftax performance 2602.10085, AgentOdyssey continual learning 2606.24893
- Related Techniques (3): HRL-IM/CBS StarCraft hierarchical 2606.30092, Seirênes adversarial self-play +10.2pts 2605.11636, RHI harness self-improvement -60% cost 2607.15524
- Key themes: Interactive world models at real-time (4 systems); self-play evolution matures (DEPT/CORAL/GEA); multiplayer world models emerge; foundation models scale (NitroGen 90.5% boss); hierarchical RL for complex games
- Updated: wiki/index.md, wiki/log.md

## [2026-07-23] synthesis | LLM Tech Report Digest — 2026-07-23
- New page: wiki/synthesis/2026-07-23/tech-report-digest.md
- Coverage: 12+ major AI companies — DeepSeek, OpenAI, Meta AI, Google DeepMind, Anthropic, Mistral AI, Qwen, xAI, Microsoft, Apple, Moonshot AI, InternLM, ByteDance, Zhipu AI
- Key themes: MoE mainstream (DeepSeek-V3, Kimi K2, Qwen3, LLaMA 4), hybrid reasoning (Claude Opus 4, Qwen3), multimodal fusion (Gemini 2.5, Phi-4-Vision), million-token context
- Flagship models: Kimi K2 (1T/32B), DeepSeek-V3 (671B/37B), Qwen3-235B-A22B, LLaMA 4 Behemoth (288B/400B)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-23] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-23)
- New page: wiki/synthesis/2026-07-23/investment-daily.md
- Coverage: 7 market segments — US Mag 7, US AI stocks, HK tech, A-share AI/chips, China ADR, China EV/new energy, AI hot themes
- US stocks: S&P 7,502(+0.04%)/Nasdaq-100 25,690(-0.57%)/Dow 52,218(-0.01%); GOOGL盘后-3%(Q2云端$247.68亿+81.8%但Capex上修$1950-2050亿); SMCI+20%利润率翻倍+$600亿积压订单; AMD+8.11%获Anthropic数十亿订单; 芯片反弹(NVDA+3.15%/AVGO+2.7%); 公募科技仓位~60%历史极端拥挤
- HK stocks: 港股微调(NASDAQ-100 ETF-0.64%); 智谱解禁+13%; 小米+3%(SUV YU9曝光)
- A shares: 上证4005+22点/创业板3386+49点; 高端PCB涨超300%; 长鑫科技IPO/安徽长鑫存储+30%市值超3000亿
- China ADR: 金龙+2.92%(BABA+4.79%/BILI+4.58%); XPeng 7月36717台+229%YoY; 美团+2.76%; 小鹏汽车+2.67%
- Key catalysts: GOOGL+TSLA盘后财报; 7/24 PCE; 7/29 MSFT财报; 8/1关税截止; Kimi K3(2.8万亿参数)发布两天算力熔断; DeepSeek V4灰度测试; 四大CSP 2026年AI Capex $4280亿(+55%)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-23] synthesis | Conference & arXiv Digest — 2026-07-23
- New page: wiki/synthesis/2026-07-23/conference-digest.md
- Coverage: 13 sections across 12+ venues (ICML 2026, ICLR 2026, AAAI 2026, CVPR 2026, NeurIPS 2025, KDD 2026, EMNLP 2025, SIGIR 2025/2026, ACL 2026, CIKM 2025, WWW 2026, RecSys 2025) + 2026 工业界推荐/CTR/Ads 重点论文 + Agent Benchmarks
- ICML 2026 highlights: AOrchestra agent orchestration, InfoPO user-centric RL, ESP multi-token prediction, Clover FP4 training
- ICLR 2026 highlights: iFusion diffusion-based CTR, BridgeDrive diffusion bridge policy
- CVPR 2026 Best: D4RT dynamic scene reconstruction, Native Compact Structured Latents for 3D
- NeurIPS 2025: TTRL test-time RL, DreamGym agent experience synthesis
- 2026 Industrial CTR/Rec: ByteDance (HyFormer, MixFormer, TokenMixer-Large, Zenith, IAT, MDL), Alibaba (EST, SORT, Agentic Recommender), Meta (Kunlun, LLaTTE, ULTRA-HSTU), Kuaishou (OneRec, DualGR), Tencent (FEDIN), Meituan (MBGR)
- Agent Benchmarks: AgencyBench (ACL 2026), General AgentBench, ALE (2.6% pass rate), MalSkillBench
- Updated: wiki/index.md, wiki/log.md

## [2026-07-23] synthesis | arXiv Paper Check — AI & CTR (July 23, 2026)
- New page: wiki/synthesis/2026-07-23/arxiv-paper-check.md
- Coverage: 15+ curated papers from cs.AI (52 new Jul 23), cs.IR (8 new Jul 23), cs.LG
- CTR/Recommendation (5): Long-History User Transformers (Yandex offline encoding +2.77% search ad), DS-MLP dual-stream MLP SOTA, DeRes dual-path CTR +0.32% AUC steeper scaling, GenCI generative cohort intent (WWW 2026), Epistemic Position-Based Click Model (SIGIR 2026)
- AI Agents & Safety (3): NEXUS runtime safety 0.205ms latency, OpenEvoShield co-evolutionary defense 100 rounds, Stochastic Primal-Dual multiobjective rec +1.8% aux
- Long-Context (2): LISA 50% speedup 16K context, FineServe workload characterization
- Reasoning (2): FormulaSPIN self-play 74.9% EM (ACL 2026 Oral), AdaRoPE per-head RoPE (ICML 2026)
- LLM Applications (3): Information Discernment 13 models 670K trials, Profile-Graph Memory 80.1% MemHop, UniRank benchmark
- Key themes: CTR offline-online decoupling validated in production; simplicity wins (DS-MLP); agent safety with minimal overhead; long-context efficiency for production; uncertainty in click models
- Updated: wiki/index.md, wiki/log.md

## [2026-07-23] synthesis | WorldQuant 101 Alpha 因子选股日报 (2026-07-23)
- New page: wiki/synthesis/2026-07-23/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子框架筛选美股 Top 20
- Factors: Alpha#1 动量(12次/60%) + Alpha#6 量价(7次/35%) + Alpha#53 反转(4次/20%) + Alpha#41 趋势(5次/25%) + Alpha#30 波动率(5次/25%) + Alpha#19 均值回复(3次/15%)
- Top 5: MU(9.5)/AVGO(9.3)/AMD(9.0)/XOM(8.8)/CVX(8.7)
- Sectors: Semis 5只 + Energy 4只 + Financials 2只 + Healthcare 3只 + Comms 2只 + ConsDef 2只 + ConsDisc 1只 + Software 1只
- Key themes: AI存储超级周期(MU+260%/AVGO定制芯片)/能源地缘溢价(XOM+26%/CVX+22%)/科技估值修复(GOOGL超跌/MSFT-18%)/金融蓝筹轮动(JPM纪录)/防御价值配置(WMT/KO)/医疗超卖反弹(UNH-40%)
- Key catalysts: 7/23 GOOGL+TSLA盘后财报, 7/24 PCE数据, 7/29 MSFT财报, 7/31 Fed决议, 8/1关税截止
- Updated: wiki/index.md, wiki/log.md

## [2026-07-22] synthesis | WorldQuant 101 Alpha 因子选股日报 (2026-07-22)
- New page: wiki/synthesis/2026-07-22/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子框架筛选美股 Top 20
- Factors: Alpha#1 动量(10次/50%) + Alpha#53 反转(7次/35%) + Alpha#41 趋势(5次/25%) + Alpha#30 波动率(5次) + Alpha#12 量价(5次) + Alpha#19 均值回复(5次)
- Top 5: GOOGL(9.5)/NVDA(9.3)/MSFT(9.0)/AMZN(8.8)/META(8.5)
- Sectors: Tech 9只 + Healthcare 4只 + Comms 2只 + Semis 3只 + Fin 1只 + ConsDisc 1只 + Indust 1只
- Key catalysts: 7/22 Powell讲话, 7/23 GOOGL+TSLA财报, 7/24 PCE数据, 8/1关税截止
- Updated: wiki/index.md, wiki/log.md

## [2026-07-22] synthesis | Investment Daily — 全球科技与AI板块 (2026-07-22)
- New page: wiki/synthesis/2026-07-22/investment-daily.md
- Coverage: 美股S&P 5,847(+0.84%)/Nasdaq-100 +1.23%; NVDA+3.2%/SMCI+15%/neocloud暴涨; GOOGL+TSLA 7/22盘后财报; A股科创50+10.73%; 港股小米+3%/网易+4.2%; 中概金龙+2.92%; Kimi K3 2.8万亿参数开源; 四大CSP AI Capex $7250亿; 苹果×阿里通义千问合作; 美伊冲突
- Topics: 美股科技/AI, 港股科技, A股科技, 中概股, 新能源车, AI模型发布, AI资本开支, 算力产业链
- Updated: wiki/index.md

## [2026-07-22] synthesis | Conference & arXiv Digest — ICML/AAAI/NeurIPS/ICLR/KDD/CVPR/ACL/SIGIR/WWW/CIKM 2026
- New page: wiki/synthesis/2026-07-22/conference-digest.md
- Coverage: 60+ papers across 12 venues and 6 cross-cutting themes
- Venues: ICML 2026 (6352 papers, 26.6%), AAAI 2026 (Singapore), NeurIPS 2025 (5823 papers), ICLR 2026 (5300+ papers), KDD 2026 (Jeju), CVPR 2026, ACL 2026, SIGIR 2026, WWW 2026, CIKM 2026
- Industry labs: Google DeepMind, OpenAI, Meta AI, ByteDance, Alibaba, Tencent, Kuaishou, NVIDIA, Netflix
- Key papers: InTRO +20% math, Grokking ridge regression, Diffusion RL policies, Slate GLM Bandits, SPIRAL +16pp planning, PRIME dual-process, GRACE 11.5% MTEB, SRPFN 7.53% synthetic prior, DeGRe +3.75% GMV deployed, TUNA unified multimodal, Franca beats DINOv2, KARL RL agents, Think in Sentences +12.5% DROP, Agentic Search 14M requests, CTRL-Rec, GPT-5.6 Sol/Terra/Luna, TokenMixer-Large 7B deployed, GFlowGR +1% revenue deployed
- Updated: wiki/index.md, wiki/log.md

## [2026-07-22] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 22, 2026)
- New page: wiki/synthesis/2026-07-22/game-rl-daily.md
- Coverage: 15+ curated papers across 7 categories
- Game RL (4): DreamerV3 general-purpose model-based RL (DeepMind), Population-Based Self-Play PBT for strategy diversity, Nemobot LLM-powered game agents (NTU, arXiv:2604.21896), Multi-Agent QMIX improvements
- LLM Game Agents (4): GamingAgent LLM code interpretation (ICLR 2026, lmgame-org), Think in Games chain-of-thought reasoning (arXiv:2508.21365), GameRT-RL RL for game testing (arXiv:2601.18070), LLM4PCG LLM for PCG (ICLR 2026, Fudan)
- Foundation Models (2): Generalist Game Players survey 5-level roadmap (Tsinghua, arXiv:2605.09965), GAIM general game agent model (arXiv:2507.04873)
- PCG (1): PCGRLLM LLM-driven reward design for PCGRL (arXiv:2502.10906)
- Benchmarks (2): Gym4ReaL realistic RL benchmark (Politecnico di Milano, arXiv:2507.00257), Efficient Benchmarking of AI Agents (arXiv:2603.23749)
- World Models (1): RLVR-World RL for world model training (arXiv:2505.13934)
- Related Techniques (3): Self-Play survey (arXiv:2408.01072), Curiosity-driven exploration, Hierarchical RL
- Key themes: LLM game agents maturing rapidly (GamingAgent ICLR 2026); Foundation model vision concrete (Tsinghua roadmap + GAIM); Hybrid RL+LLM approaches dominate; PCG transformed by LLMs (LLM4PCG ICLR 2026); World models remain critical infrastructure; Benchmark maturation
- Updated: wiki/index.md, wiki/log.md

## [2026-07-21] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-07-21)
- New page: wiki/synthesis/2026-07-21/wq101-alpha-daily.md
- Coverage: S&P 7,444/Nasdaq 25,510/VIX 18.47; 美伊冲突布伦特$90+; Q2财报季加速
- Top 5: NVDA(9.5)/JPM(9.5)/AMD(9.3)/AAPL(9.3)/CVX(9.0)
- 7 WQ101因子应用: Alpha#1动量(60%), Alpha#6量价(45%), Alpha#53反转(35%), Alpha#41趋势(30%), Alpha#19均值回复(25%), Alpha#30波动率(20%), Alpha#12量价背离(5%)
- 板块分布: Semis 6只+Financials 3只+Staples 3只+Energy 2只+Healthcare 2只+Comm 2只+ConsDisc 2只+Industrials 1只
- Key: 动量因子载体从芯片→能源/金融/医疗; TMT动量因子-40%史上最快最深回撤后轮动剧烈
- Updated: wiki/index.md, wiki/log.md

## [2026-07-21] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 21, 2026)
- New page: wiki/synthesis/2026-07-21/game-rl-daily.md
- Coverage: 21+ curated papers across 7 categories
- Game RL (3): SPIRAL self-play interactive RL + LLM-augmented agents, Multi-Agent Game Playing via RL survey (2026), Reinforced Self-Training (ReST) for multi-agent games
- LLM Game Agents (4): Bounded Autonomy benchmark for LLM agents in open-world games, PCSP benchmark for planning+control in physics games, GameAgent LLM-driven game agent with tool-integrated reasoning, LLM multi-agent stock market simulation (game-theoretic)
- Foundation Models (4): NitroGen versatile foundation model for game content gen (sprites/tiles/textures/levels), GFM general foundation models for games, GAgent general game agents with LLMs, Survey of Foundation Models for Games
- PCG (2): Combining PCGRL and WFC hybrid approach, LLMs for PCG survey
- Benchmarks (1): GameWorld scalable benchmark for game AI agents (multiple genres)
- Industry (4): Solaris scalable AI-driven game worlds, Dream Cubed 3D game asset generation with latent diffusion, Human-Alignment taxonomy+framework for game AI, Survey of Generative AI for game development
- Related Techniques (2): Curiosity-Critic improved exploration in RL, TROFI truncated inverse reinforcement learning
- Key themes: LLM agents rapidly entering game AI with benchmarks maturing; Foundation models for games crystallizing as new subfield; Hybrid RL+LLM approaches dominate; PCG revolutionized by PCGRL+WFC and LLM-based generation; Industry moving fast on generative AI for game worlds/assets; Exploration remains critical RL challenge
- Updated: wiki/index.md, wiki/log.md

## [2026-07-21] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-21)
- New page: wiki/synthesis/2026-07-21/investment-daily.md
- Coverage: 美股/港股/A股/中概股/EV/AI热点 6大板块，70+只个股
- US stocks: S&P+0.14%/Nasdaq+0.38% 创历史新高; GOOGL+2.7%(Q2财报周); NVDA H20对华复供/AMD MI308重启; JPMorgan警告AI拥挤度100th percentile; Block(XYZ)+8.3%纳入S&P 500
- HK stocks: 腾讯AI重构微信生态/Q2预期营收+12%YoY; 阿里+1.81%(估值修复~13x P/E); 小米黄仁勋确认与雷军合作AI+自动驾驶
- A-shares: 上证+0.72%/深成+0.86%/创业板+0.87%创年内新高; 雅下水电1.2万亿开工涨停潮(中国电建/西藏天路/华新水泥等); 新易盛3天+40%/中际旭创强势; 宇树科技IPO催化机器人板块
- 中概股: BABA+4.69%/JD+3.31%/PDD+2.18%; BEKE+5.87%; YMM+6.54%; BZ+4.71%; TME+4.45%
- EV: XPeng 7月36717台创纪录+229%YoY; 小米>30000台创新高; BYD 344296台(+0.6%YoY/-10.1%MoM); NIO 21017台(ONVO L90售罄); LI 30731台(-39.7%YoY)
- AI热点: Stargate+4.5GW/$30B年合同Oracle/总容量>5GW; CoreWeave $6B宾州数据中心; OpenAI o3/o4-mini推理模型/IMO金牌水平; 混元3D模型HuggingFace第一; 中国光模块全球市占率38%
- Key themes: AI Capex持续超预期; H20复供提振中国算力板块; 雅下水电超级工程; 机器人商业化加速; 中国EV交付分化
- Updated: wiki/index.md, wiki/log.md

## [2026-07-21] synthesis | Conference & arXiv Digest — 2026-07-21
- New page: wiki/synthesis/2026-07-21/conference-digest.md
- Coverage: 80+ papers across 12 venues: ICML 2026, ICLR 2026, AAAI 2026, NeurIPS 2025, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, RecSys 2025, arXiv
- ICLR 2026 (225 Oral): TROLL trust regions, AlphaAlign deep safety, WaltzRL multi-agent safety, ToolTree MCTS agent planning (+10%), Mamba-3, MoE vs Dense
- NeurIPS 2025 Best: Gated Attention (Alibaba/Qwen), 1000 Layer RL, Artificial Hivemind, Diffusion Memorization; Runner-up: RLVR doesn't produce new reasoning
- AAAI 2026: CDCR-SFT causal DAG 95.33% CLADDER surpassing human, InTRO +20% math reasoning, LENS unified RL segmentation
- CVPR 2026 Best: D4RT (Google DeepMind 4D), O-Voxel (Microsoft 3D gen), SAM 3D (Meta); TUNA unified VMM
- KDD 2026: CTR-Sink attention sinks (Ant Group), FAT field-aware transformer (+4.38% AUC, +2.33% CTR live), DS-MLP vanilla MLP SOTA, LLM-as-a-Judge rec eval
- ACL 2026: 12,148 submissions → 2,296 accepted (18.9%); agent/reasoning 366 papers (+224); Deliberative Searcher 96% false-certain reduction
- SIGIR 2026: MVIGER variational multi-view generative rec (T5-small > Llama 7B), SIGMA AliExpress
- WWW 2026: ThinkRec System 2 reasoning for rec, GenCI generative user intent for CTR
- RecSys 2025: Engagement-Aware MoE Amazon, Kuaishou video+comment joint rec, GRACE Walmart
- Agent systems: ToolTree, HTAA (84.5% effort cut), STAR RL recipe, ParaManager parallel orchestration
- Code execution: ProgramBench (best 3% tasks), CodeSpecBench (20.2% repo-level), MirrorCode (56% reimpl), ExecVerify (7B=32B)
- Key themes: Agentic AI dominant; RL for LLM mature but limited; CTR prediction LLM+field-aware fusion; execution simulation emerging; 3D vision breakthroughs
- Updated: wiki/index.md, wiki/log.md

## [2026-07-21] synthesis | arXiv Paper Check — AI & CTR (July 21, 2026)
- New page: wiki/synthesis/2026-07-21/arxiv-paper-check.md
- Coverage: 14 curated papers from cs.AI (105 new Jul 20), cs.IR (10 new Jul 20), cs.LG (~200 new Jul 20)
- CTR/Recommendation (4): RecGPT-V3 (Taobao, Memory Hub + latent reasoning, CTR +1%, GMV +3.97%, deployed), RECAP (Kuaishou, GRPO reward streaming profiles, RecSys 2026), PCTD (preference-guided counterfactual tool retrieval), Yi (in-place vector index 1.75× throughput)
- AI Agents (3): ToolVerse (400 MCPs, 4500 tools, agentic RL environments), DSWorld (data science world model, 14× speedup), SeerGuard (mobile GUI safety via world model prediction)
- Causal & Scientific (4): Causal-Audit (ACL 2026, auditable graph reasoning), S1-Omni (unified multimodal scientific foundation model), NeurOWL (neuro-symbolic ontology reasoning), ToolSciVer (multimodal scientific claim verification via visual tool RL)
- LLM Efficiency (3): LLA (21.3× KV compression on H200), CAPC (cache-aware prompt compression 49% cost savings), LLMs layer-wise cross-lingual relevance encoding
- Key themes: World models as general efficiency lever; production LLM rec maturing; MCP validated as agent infrastructure; auditable reasoning at ACL 2026; KV cache as new deployment frontier
- Updated: wiki/index.md, wiki/log.md

## [2026-07-21] synthesis | LLM Tech Report Daily (2026-07-21)
- New page: wiki/synthesis/2026-07-21/tech-report-digest.md
- Coverage: 19 companies latest models and tech reports
- Major updates since 07-20: DeepSeek V4-Pro (Apr 2026), OpenAI GPT-5.5 Ultra (Apr 2026), Google Gemini 3.1 Pro (Feb 2026), Anthropic Claude Opus 4.8 (May 2026), Mistral Magistral Medium (Jun 2026), xAI Grok 4 "Heavy" (Jul 2026), Baichuan Omni-1.5 (Jan 2026), InternLM Intern-S1-Pro (Feb 2026)
- Key trends: MoE 15+ companies, reasoning models (Mistral Magistral Medium first reasoning model), multimodal native fusion, long-context 10M (Llama 4 Scout), small models (Phi-4 14B, InternLM3 8B), agent capabilities (256+ tools Kimi K2), hybrid Mamba-Attention (Nemotron 3 Ultra)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-18] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 18, 2026)
- New page: wiki/synthesis/2026-07-18/game-rl-daily.md
- Coverage: 30+ curated papers across 7 categories
- Game RL (10): MARL-GPT unified transformer MARL, Stratagem transferable reasoning, AlphaZero Tablut asymmetric, QZero model-free Go mastery, SPIRAL +10.5% self-play reasoning, PolicyEvolve programmatic PBT, PopuLoRA LoRA evolution 7B, GEMS 6x faster PSRO, FAMOU AAMAS 2026 MCTF winner, Beyond Static Evaluation co-evolution
- Game AI Bot (10): AVACraft ACL 2026 StarCraft II VLM+MARL, ROE episode reflection TextStarCraft II, Orchestrated Reality POMDP world simulation, Bounded Autonomy live multiplayer LLM characters, COSPLAY co-evolving skill bank +25.1%, Nemobot Shannon taxonomy NUS, Sensi 50-94x sample efficiency ARC-AGI-3, HeRoN RL-LLM mediated NPC +81%, CASCADE 3-layer social coordination, Psy-CoT psychology-grounded role-playing
- Foundation Models (6): NitroGen CVPR 2026 NVIDIA 40K hrs/1000+ games, Pixels2Play 8300+ hrs open BC 1.2B params, Odysseus 100+ turn VLM RL Mario, Generalist GP survey 5-level roadmap Tsinghua, See Symbolize Act VLM spatial grounding, GameVerse video reflection benchmark
- PCG (6): WFC+PCGRL hybrid Lode Runner, Multiverse cross-game level blending, HDPCG high-dimensional direction-space/time, PRP cake representation Sokoban, Multi-task PCG DeBERTa Scientific Reports, Co-adaptive DRL Unity level design
- Benchmarks (5): AVACraft StarCraft II 21 scenarios, GameVerse 15 games reflect-retry, Generalist GP survey 100+ games, ARC-AGI-3 Sensi curriculum learning, MCTF 2026 maritime CTF
- Related Techniques (8): Population-based training (PolicyEvolve/PopuLoRA/GEMS), self-play reasoning transfer (SPIRAL/Stratagem/QZero), RL+LLM agents (ROE/COSPLAY/Sensi/HeRoN), PCG workflows (WFC+PCGRL/Multiverse/PRP/HDPCG)
- Key themes: Self-play generates transferable reasoning; Foundation models at internet scale (NitroGen CVPR 2026); VLM perception is bottleneck (See Symbolize Act); LLM agents entering live games; PCG+RL complementary; Population evolution scales PSRO→GEMS→PopuLoRA→FAMOU
- Updated: wiki/index.md, wiki/log.md

## [2026-07-20] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-07-20)
- New page: wiki/synthesis/2026-07-20/wq101-alpha-daily.md
- Market: S&P 7,457.69(-1.55%周), Nasdaq 25,520.24(-2.9%周), SOX进入技术性熊市(较6月高点-20%+)
- Events: 美伊冲突→布伦特$90+/WTI$84; TMT动量因子-40%史上最快最深回撤; AAPL历史新高$334$4.9T市值反超NVDA; GS Prime 8周累计净卖出美IT股创10年+最高; Energy本周唯一收涨板块+4.54%; 费城半导体-9%周/-18%月
- Factor structure: Alpha#1动量(12次/60%主导)载体从芯片→能源/金融/医疗; Alpha#6量价(7次/35%); Alpha#53反转(5次/25%); Alpha#41趋势(6次/30%); Alpha#30波动(5次/25%); Alpha#12背离(4次/20%); Alpha#19均值(4次/20%)
- Top 20: JPM(9.5)/AAPL(9.3)/UNH(9.0)/GS(9.0)/XOM(8.8)/MS(8.8)/CVX(8.5)/WFC(8.5)/ABT(8.3)/VLO(8.3)/META(8.0)/GOOGL(8.0)/EOG(7.8)/V(7.8)/KO(7.5)/WMT(7.5)/PG(7.3)/MSFT(7.3)/HD(7.0)/LMT(7.0)
- Sectors: Financials 5只+Energy 4只+Tech 4只+Healthcare 2只+Staples 3只+ConsDisc 1只+Defense 1只
- Key themes: 动量因子载体切换(芯片→能源/金融/医疗); AAPL"Lazy AI"策略避开关税+capex风险; UNH Q2超预期+30%验证医疗成本改善; MSFT超卖-18%YTD=均值回复候选; Energy地缘溢价(EIA库存低于5年均值6.3%); 低波动防御价值凸显(KO/PG/WMT)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-18] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-18)
- New page: wiki/synthesis/2026-07-18/investment-daily.md
- Coverage: 全球科技与AI板块10大热点深度分析
- Market: S&P 7,457(-1.01%), Nasdaq 25,520(-1.40%), SOX 11,673(-1.63%进入熊市), 恒指24,562(-1.78%), 恒生科技4,623(-4.37%), 上证~3,764(-3%)
- Core catalyst: Kimi K3(月之暗面2.8万亿参数开源模型)发布引发全球芯片股暴跌/"DeepSeek 2.0时刻"担忧
- US stocks (18): NVDA-2.21%(SOX较6月高点-20%), AAPL+0.14%(避风港), META-2.8%(洽谈Anthropic算力出租$100亿), TSLA-2.61%(周-6.6%), AMZN-1%, GOOGL-2%, MSFT-1%+, AVGO-0.97%, AMD-1.03%, AMAT-5.57%, TSM-3%, MU-0.50%, INTC-2%, NFLX-7.26%(指引不及预期), SPCX-5.43%(星舰试飞中止), SNPS-7.85%, CDNS-9.47%, ISRG-14.15%
- HK stocks (13): 腾讯-4.63%, 阿里-3.68%, 美团-4.07%, 小米-2.25%, 快手-7.8%, 百度-3.45%, 智谱-28.49%, MiniMax-15.63%, 明略科技-16.06%, 中芯国际-10%, 华虹-11.9%, 小鹏-8.7%, 哔哩哔哩+3.13%
- A-shares: 科创50跌7%, 寒武纪-5%+, 海光信息-4.84%(H1利润创新高但估值承压), 中际旭创-5.23%, 北方华创-3.67%, 新易盛-6%+, 绿盟科技涨停(华为昇腾), 网宿科技涨停
- 中概股: 纳斯达克中国金龙-1.81%, BIDU-5%+, 理想-3.65%, 小鹏-7%+, 蔚来-8.8%
- EV: TSLA周-6.6%, BYD 7月A股+20%, 理想Q2超预期, 蔚来降价3万, 宁德时代储能订单排至2028
- AI热点: Kimi K3 2.8万亿参数开源/Code Arena 1679分登顶/AI CapEx $7250亿引发回报质疑/NVIDIA B200租赁价回落30%/曙光8000十万卡国产超集群上线/华为Atlas 950超节点首秀/DeepSeek $351B估值融资/WAICO 29国AI治理组织成立
- Key themes: Kimi K3触发AI硬件→软件估值重构; 费半技术性熊市; 资金从AI硬件向平台型公司切换; 国产算力生态突破(曙光8000+华为Atlas); 港股AI概念股崩盘但大型科网相对抗跌; 下周Alphabet/Tesla/Intel财报成关键风向球
- Updated: wiki/index.md, wiki/log.md

## [2026-07-20] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 20, 2026)
- New page: wiki/synthesis/2026-07-20/game-rl-daily.md
- Coverage: 40+ curated papers across 7 categories
- Game RL (7): SPIRAL self-play reasoning transfer (ICLR 2026), Stratagem trajectory-modulated transferable reasoning, MARS multi-agent self-play +28.7%/10% AIME, MEMO memory-augmented 19× fewer games, π-Play privileged self-distillation, MAE Proposer-Solver-Judge co-evolution, FMSP quality-diversity strategy discovery
- Game AI Bot (8): Sensi curriculum test-time 50-94× sample efficiency (ARC-AGI-3), Orchestrated Reality LLM POMDP world simulation, Bounded Autonomy live multiplayer LLM characters, COSPLAY co-evolving skill bank +25.1%, LLM Reasoner+Planner NPC, Nemobot Shannon taxonomy+LLMs (NUS), HexMachina Catan 54% vs AlphaBeta, Psy-CoT psychology-grounded game NPCs
- Foundation Models (5): NitroGen CVPR 2026 NVIDIA 40K hrs/1000+ games, Game-TARS ByteDance 500B tokens outperforms GPT-5, Pixels2Play 8300+ hrs open BC, Open MIND scaling BC laws, Generalist GP survey 5-level roadmap
- PCG (8): CreativeGame mechanic-aware iterative generation, VIPCGRL human-aligned level gen, Multiverse cross-game level blending, AutoUE 3D Unreal Engine multi-agent, OpenGame GameCoder-27B, HDPCG high-dimensional, WFC+PCGRL hybrid, Database-driven 3D level gen with LLMs
- Benchmarks (8): SciCrafter Minecraft 26% ceiling, Agentick 37 tasks/5 modalities, OmniGameArena UE5 IDC, lmgame-Bench 13 models/6 games, TextAtari 100K frames, VideoGameBench 0.48% completion, GameWorld 34 browser games state-verifiable, TeamCraft 55K Minecraft multi-agent
- World Models (5): Mind-Studio executable pygame WMs 48.7% NSP Montezuma, GameCWM distillation SFT+RLVR, Code World Models DeepMind 9/10 games, UHM universal horizon offline MBRL, JOWA 150M jointly-optimized world-action
- Key themes: Self-play generates transferable reasoning (SPIRAL/MARS/Stratagem); Foundation models at internet scale (NitroGen CVPR 2026, Game-TARS 500B tokens); Executable world models via LLMs (Mind-Studio, Code World Models); LLM agents still far from human (26% SciCrafter ceiling, 0.48% VideoGameBench); PCG+LLM complementary workflows; 8+ new game benchmarks
- Updated: wiki/index.md, wiki/log.md

## [2026-07-20] synthesis | LLM Tech Report Daily (2026-07-20)
- New page: wiki/synthesis/2026-07-20/tech-report-digest.md
- Coverage: 19 companies' latest model tech reports — DeepSeek, OpenAI, Meta, Google, Anthropic, Mistral, Qwen, 01.AI, Baichuan, Microsoft, Apple, NVIDIA, xAI, Amazon, Zhipu, InternLM, Moonshot, StepFun, ByteDance
- Key models: DeepSeek-V3 (671B MoE), Llama 4 Scout (10M ctx), Gemini 2.5 Pro, Claude Opus 4, Mistral Large 3 (675B), Qwen3-235B-A22B, Kimi K2 (1T), Nemotron 3 Ultra (550B Mamba-hybrid), Phi-4-RV-15B, Apple AFM (3B device), GLM-5 (DSA), Step-DeepResearch (32B agent), Seed 2.0 Pro
- Key trends: MoE mainstream (15+ companies), RL + test-time compute reasoning, native multimodal, context from 128K→10M, small model resurgence, Agent-ification, training efficiency innovation
- Updated: wiki/index.md, wiki/log.md

## [2026-07-20] synthesis | LLM Tech Report Daily (2026-07-20) — enriched update
- Updated page: wiki/synthesis/2026-07-20/tech-report-digest.md
- Enriched all 19 company sections with:
  - arXiv links for OpenAI GPT-5 (2601.03267), Google Gemini 2.5 (2507.06261), Microsoft Phi-4-RV (2603.03975), Apple AFM (2507.13575), Amazon Nova (2506.12103), DeepSeek R1 (2501.12948)
  - Training data sizes (DeepSeek 14.8T, Kimi K2 15.5T, xAI Grok 3 13.4T, InternLM3 4T, Qwen3 119 languages)
  - Specific parameter counts (Grok 3 1.2T/128 experts, Nemotron 3 Ultra 512 experts, Kimi K2 1.04T)
  - Context lengths (Kimi K2 196K, GLM-5 200K, Amazon Nova 300K)
  - Benchmark numbers (Kimi K2 MMLU 77.4, MATH-500 96.2; Baichuan-M4 hallucination rate 3.3%)
  - StepFun expanded to cover Step-3 + Step 3.5 Flash + Step-DeepResearch
  - ByteDance expanded to include Game-TARS (500B tokens, surpasses GPT-5)
- Enhanced trend analysis: added MoE comparison table (7 models with params/activations/experts/context), new section on Safety & Alignment (Anthropic ASL-3, OpenAI GPT-5 System Card, Apple on-device privacy)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-20] synthesis | Investment Daily Report (2026-07-20)
- New page: wiki/synthesis/2026-07-20/investment-daily.md
- Coverage: 美股/港股/A股/中概股/EV/AI热点 6大板块，60+只个股
- Key highlights: Hyperscaler 2026 Capex $7000亿; 科创50涨8.41%; 中概股HXC涨2.92%; 小鹏7月交付创纪录; AI新模型密集发布(GPT-5.6/Grok 4.5/千问新版)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-20] synthesis | arXiv Paper Check — AI & CTR (July 20, 2026)
- New page: wiki/synthesis/2026-07-20/arxiv-paper-check.md
- Coverage: 14 curated papers from cs.AI (201 new), cs.IR (9 new), cs.LG (70 new)
- CTR/Recommendation (3): RecGPT-V3 (Taobao, CTR +1%, GMV +3.97%, deployed), RECAP (Kuaishou, GRPO reward, uAUC +0.0084, RecSys 2026), Yi (vector index 1.75x throughput)
- AI Agents (4): ToolVerse (400 MCPs, 4500 tools), DSWorld (world model 14x speedup), SeerGuard (GUI safety), Causal-Audit (ACL 2026)
- Scientific (2): S1-Omni (beats GPT-5.5), NeurOWL (neuro-symbolic ontology)
- LLM Efficiency (3): LLA (21.3x KV compression), CAPC (49% API cost savings), LLMs layer-wise relevance
- Key themes: Production LLM rec maturing; world models as efficiency lever; MCP as agent infrastructure; cache-aware efficiency
- Updated: wiki/index.md, wiki/log.md


## [2026-07-20] synthesis | Top ML/AI Conference & arXiv Paper Digest — 2026-07-20
- New page: wiki/synthesis/2026-07-20/conference-digest.md
- Coverage: **47+ papers** across 12 venues (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, SIGIR 2026, WWW 2026, RecSys 2025, CIKM 2025, arXiv)
- ICML 2026 (8): Flexibility Trap Outstanding (diffusion constraint failure), Shannon Scaling Law (LLMs as noisy channels), MemoPilot ELO#1, HiPER 97.4% ALFWorld, JitRL 30× cheaper, Self-Flow, UniAR Alibaba, Complete-muE
- NeurIPS 2025 (5): Gated Attention Alibaba Best (shipped Qwen3-Next), Artificial Hivemind 70+ LLMs, 1000 Layer RL, Diffusion Memorization, RL vs Reasoning Runner-Up
- ICLR 2026 (4): Transformers Succinct Outstanding (expressiveness limits), LLMs Lost Multi-Turn 39% drop, Mean Flow Policy, Polar Express, Muon HM
- AAAI 2026 (4): AURA safety alignment for rec, InTRO +20% math reasoning, MoMoREC Taobao +6.3% GMV, TreeBridge Shopee +1.55% GMV
- KDD 2026 (3): RankElastor effective-rank dynamics, RPORec Kuaishou RL+reasoning, EST Alibaba +3.27% RPM, GR4AD +4.2% revenue
- CVPR 2026 (3): D4RT DeepMind Best 4D reconstruction, SAM 3D Meta 5:1 preference, NitroGen NVIDIA 40K hrs gaming agents
- ACL 2026 (4): SOAR +16.9% research quality, KARL beats GPT-4o, HSCodeComp Best Resource, RecPO intensity+temporal
- SIGIR 2026 (4): Agentic Search 14M requests, AgentRank, LTRR, HyDE, ACE anisotropy +12.4%
- WWW 2026 (3): ThinkRec, GenCI, SparseCTR Meituan +1.72% CTR
- RecSys 2025 (3): LSVCR Kuaishou +4.13%, Semantic IDs, LONGER ByteDance
- CIKM 2025 (1): RankMixer ByteDance
- arXiv (8): SAO GLM-5.2 750B async RL, MaRCA +16.67% revenue, Sparse Delta Memory beats attention 8B, Mamba-3, SPIRAL +10.5%, TiG Honor of Kings, Genstrat strategic reasoning, PCSP 64 agents
- Cross-cutting themes: Scaling Laws go vertical (CTR/rec/agents), RL post-training becomes norm, generative rec goes industrial, agent safety urgent, negative signals matter
- Updated: wiki/index.md, wiki/log.md

## [2026-07-20] synthesis | arXiv Daily Report (2026-07-20) — AI, LLMs, Recommendation, CTR, Advertising, Sequential Modeling, Games
- New page: wiki/synthesis/2026-07-20/arxiv-daily.md
- Summary: 20+ curated papers across 6 categories
- Categories: Generative Recommendation (5), CTR Prediction (5), Sequential Modeling (6), LLM Embeddings (3), Game AI (4), Scaling/Efficiency (2)
- Key highlights: SRPFN zero-shot KDD 2026, CADET LinkedIn +11% CTR, Beyond Positive Signals mixed-polarity +9.6% AUC, Incumbent Advantage GEO brand bias, SAO for GLM-5.2 750B
- Updated: wiki/index.md, wiki/log.md

## [2026-07-17] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-07-17)
- New page: wiki/synthesis/2026-07-17/wq101-alpha-daily.md
- Market: S&P 7,533.77(-0.51%), Nasdaq 25,881.95(-1.47%), Dow 52,553.50(-0.20%), SOX 11,867.50(-4.29%)
- Events: 芯片股暴跌(SOX-4.3%/SNDK-12.6%/MU-5.6%/WDC-9.2%); 资金轮动至防御板块(XLP+2.6%/XLV+1.0%); Energy+3.5pp跑赢Tech; UnitedHealth+8%(Q2上调指引); Abbott+13.5%(Q2超预期); JPM创纪录$212亿净利; 美伊冲突推升油价
- Factor structure: Alpha#1动量(10次/50%)主导+Alpha#6量价(8次/40%)+Alpha#53反转(5次/25%)
- Top 20: JPM(9.5)/AMZN(9.3)/UNH(9.0)/V(9.0)/BLK(8.8)/WMT(8.7)/MSFT(8.5)/KO(8.5)/XOM(8.3)/CVX(8.0)/GOOGL(8.0)/ABT(8.0)/AAPL(7.8)/META(7.8)/NVDA(7.5)/GS(7.5)/JNJ(7.5)/BAC(7.3)/COST(7.3)/LULU(7.0)
- Sectors: Financials 5只+Healthcare 3只+Tech 3只+Staples 3只+Energy 2只+Comm 2只+Cons.Disc. 1只+Semis 1只
- Key themes: 芯片集中度风险(S&P 20%+)引发防御轮动; Financials Q2财报全面超预期(NII+资本市场); Healthcare MA费率上调5%+成本改善; Energy中东冲突溢价; MSFT/GOOGL估值修复; 消费必需品+低Beta防御配置
- Updated: wiki/index.md, wiki/log.md

## [2026-07-17] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 17, 2026)
- New page: wiki/synthesis/2026-07-17/game-rl-daily.md
- Coverage: 25 curated papers across 7 categories
- Game RL (2): COvolve adversarial co-evolution MSNE meta-policy, ResDreamer hierarchical residual world model 3D Minecraft combat
- Game AI Bot (8): Bounded Autonomy live multiplayer LLM characters, Psy-CoT/RAPO psychology-grounded game NPCs, CASCADE 3-layer low-cost social coordination, WISE causal event graph Minecraft 30%+ task success, ProPlay procedural world model preplay, Orchestrated Reality parameterized-action POMDP, OPINE-World 20/25 ARC-AGI-3 games, RWML self-supervised world model learning
- Foundation Models (5): Game-TARS 500B tokens outperforms GPT-5/Gemini on FPS, Odysseus 100+ turn VLM RL Mario, Generalist GP survey 5-level roadmap, Pixels2Play 8300+ hrs open BC, GameVerse video reflection benchmark
- PCG (5): WCRL WFC+PCGRL hybrid, MultiGen editable multiplayer diffusion engine, HDPCG high-dimensional level generation, PCGRL+ JAX 1B timesteps, PRP cake playtrace representation
- Benchmarks (5): OmniGameArena UE5 12 games IDC, GameWorld 34 games state-verifiable evaluation, MineExplorer multi-hop Minecraft exploration, TextAtari 100K-frame language agents, SciCrafter Minecraft redstone discovery-to-application
- Industry (4): KRAFTON ICML 2026 PUBG ALLIE on-device LLM agents, Sony AI GT Sophy coachable agent 10-15 demos, NC AI production pipeline lessons, PCSP persona-conditioned shared RL 64 agents UE5
- Related Techniques (4): HWM hierarchical planning latent world models 70% real robot, WorldCompass RL for video world models 20%→55% accuracy, AgentOWL hierarchical neural options Atari, AgentOdyssey open-ended continual learning
- Key themes: On-device LLM agents reaching commercial viability (KRAFTON, inZOI); World models as NPC infrastructure (CASCADE/Orchestrated Reality/ProPlay/PCSP); Foundation models scaling (Game-TARS 500B tokens outperforms GPT-5); Benchmarks explosion (6 new this cycle); LLM agents still plateau at 26% on discovery tasks
- Updated: wiki/index.md, wiki/log.md

## [2026-07-17] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-17)
- New page: wiki/synthesis/2026-07-17/investment-daily.md
- Coverage: 美股(AAPL+4%创新高/NVDA H20复供), 港股(恒指+1.33%五连阳/小米+6.3%/智谱-9.3%), A股(新易盛3天+40%/CPO爆发/PCB涨停潮), 中概股(金龙+2.92%/BABA+4.79%), 新能源(XPeng+229% YoY/BYD海外+169%), AI热点(ChatGPT Agent/混元Hy3登顶/字节GR-3)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-17] synthesis | LLM 技术报告速递 (2026-07-17)
- New page: wiki/synthesis/2026-07-17/tech-report-digest.md
- Coverage: 19家机构技术报告汇总 (DeepSeek, OpenAI, Meta, Google, Anthropic, Mistral, Qwen, xAI, Moonshot, NVIDIA, Zhipu, InternLM, Microsoft, Amazon, StepFun, ByteDance, 01.AI, Baichuan, Apple)
- Key models: DeepSeek-V4 (1.6T MoE), GPT-5.5, LLaMA 4, Gemini 2.5, Claude 4, Grok 3, Kimi K2, GLM-5, Step-3.7-Flash
- Updated: wiki/index.md, wiki/log.md

## [2026-07-17] synthesis | Top ML/AI Conference & arXiv Paper Digest — Updated 2026-07-17
- New page: wiki/synthesis/2026-07-17/conference-digest.md
- Coverage: **150+ papers** across 12+ venues (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, arXiv)
- Key updates from previous digest: enriched with 70+ additional papers, detailed experimental results with numbers, new sections on game AI (TiG, SPIRAL, FMSP, Odysseus), sequential modeling at scale (10K Douyin, ReaSeq Taobao, ULIM), generative recommendation architectures (GLASS, SIDReasoner, Gryphon, GenRec JD), advertising/auction theory (LLM-Auction 59.1% revenue improvement, Bid2X, CBD, EGA-V1), live papers from Jul 16-17 arXiv submissions, comprehensive stats table
- Key papers added: SMACS (15 open models beat closed), Scalpel vs. Hammer (GRPO amplifies, SFT replaces), Sparse Delta Memory (Meta FAIR, beats attention at 8B), Mamba-3, Oryx, SPIRAL self-play (+10.5% reasoning), TiG Honor of Kings (Qwen-3-14B beats DeepSeek-R1), Foundation Model Self-Play, AutoSynthesis, Proof-or-Stop, SearchOS-V1, GRAD Meituan (+10.68% ROI), GRAB Baidu (+3.49% CTR), ToolRec OPPO (150M+ MAU), Adaptive Ad Load, PolyQ edge quantization, Muse Muon geometry
- Updated: wiki/index.md, wiki/log.md

## [2026-07-17] synthesis | arXiv Paper Check — AI & CTR (July 17, 2026)
- New page: wiki/synthesis/2026-07-17/arxiv-paper-check.md
- Coverage: 16 curated papers from cs.AI (204 new Jul 17), cs.LG (143 new Jul 17), cs.IR/CTR (~925 total)
- CTR/Recommendation (5): Long-History User Transformers (Yandex, offline encoding + cached representations, +2.77% search ad, +2.1% YAN, +2.26% revenue), TMallGS (Alibaba, unified Transformer search ranking with hierarchical tokenization), Mitigating Early Training Collapse (sparsity control > LR tuning), Privacy Preserving RecSys (federated learning + DP at ε≈5), Mutable Low-Rank Sketches (retrain-free recommendation)
- AI Agents (4): SearchOS-V1 (open-domain multi-agent search), AutoSynthesis (automated meta-analysis), Proof-or-Stop (verifiable evidence-gated lifecycle control, 48 pages), Atrex (LLM GPU kernel benchmark, Alibaba)
- ML (4): PolyQ (edge CPU LLM quantization), xHC (Expanded Hyper-Connections), Muse (Muon optimizer geometry analysis), Long-Context Fine-Tuning with Limited VRAM
- Advertising (3): Adaptive Ad Load Design (economics + ML), ToolRec (on-device query recommendation, 150M MAU, OPPO), Position Auctions with Capacity Constraint (truthful mechanism)
- Key themes: Offline-online decoupling for CTR; Unified Transformer ranking; Simplicity wins in CTR (sparsity control); Autoresearch goes production; Agent verifiability; Muon optimizer deepened
- Updated: wiki/index.md, wiki/log.md

## [2026-07-16] synthesis | WorldQuant 101 Alpha 因子选股日报 — 2026-07-16
- New page: wiki/synthesis/2026-07-16/wq101-alpha-daily.md
- Market: S&P 7,577.51(+0.38%), Nasdaq 100 29,406(-0.28%), Dow 50,970(-0.21%), VIX 15.67
- Macro: PPI低于预期+CPI降温3.5%→加息概率骤降至~10%; Fed Funds 3.75%不变
- Factors: Alpha#1动量(12次/60%主导)+Alpha#6量价(7次/35%)+Alpha#53反转(5次/25%)
- Top 20 by score: AAPL(9.5)/JPM(9.0)/GOOGL(9.0)/XOM(8.5)/LLY(8.5)/CVX(8.5)/META(8.5)/AMZN(8.0)/UNH(8.0)/MSFT(8.0)/JNJ(7.5)/BLK(7.5)/MRK(7.5)/NVDA(7.5)/AVGO(7.0)/ABBV(7.0)/TSLA(7.0)/PFE(7.0)/COP(7.0)/AMGN(6.5)
- Sectors: 科技5只(8.5均分)+医疗7只(7.6)+能源3只(7.5)+金融2只(8.3)+通信消费3只(7.5)
- Key catalysts: AAPL Qwen入华+V形突破$327历史新高; JPM Q2超预期12.7%营收增长; GOOGL加入道指+102%1Y涨幅; PYPL $53B收购要约+16%; LLY GLP-1龙头7/23财报; 能源YTD+33.84%
- Updated: wiki/index.md, wiki/log.md

## [2026-07-16] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 16, 2026)
- New page: wiki/synthesis/2026-07-16/game-rl-daily.md
- Coverage: 37 curated papers across 7 categories
- Game RL (10): SPIRAL self-play reasoning transfer, Strat-Reasoner recursive opponent modeling, MARSHAL multi-agent self-play +28.7%, MEMO memory-augmented 19× fewer games, OMAR conversational self-play, STRATAGEM transferable reasoning, AlphaZero Tablut asymmetric, QZero model-free Go, π-Play privileged self-distillation, SELF-REDTEAM safety alignment via self-play
- Game AI Bot (8): Nemobot Shannon taxonomy+LLMs, COSPLAY co-evolving skill bank 25.1% improvement, Generative Code Opt Atari competitive with deep RL, Sensi curriculum test-time 50-94× efficiency, AutoHarness code synthesis 145 games, HexMachina Catan 54% vs AlphaBeta, FAMOU co-evolutionary AAMAS 2026 1st, PORTAL 1000+ FPS games
- Foundation Models (6): NitroGen CVPR 2026 NVIDIA 40K hrs/1000+ games, Pixels2Play 1.2B open BC, Game-TARS ByteDance 500B tokens, Generalist GP survey 5-level roadmap, GameVerse video reflection, OmniGameArena UE5 IDC
- PCG (6): IPCGRL language-instructed RL, WCRL WFC+PCGRL hybrid, AutoUE 3D Unreal Engine multi-agent, PCGRLLM LLM reward design, AutoBG board game design assistant, Orchestrated Reality LLM-driven POMDP
- Benchmarks (3): TextArena 100+ games TrueSkill leaderboard, OmniGameArena UE5 IDC improvement dynamics, PCG Benchmark open-source
- World Models (9): RLVR-World RL for world models, PriorZero LLM priors+MCTS, WorldCam camera-pose geometry 3D, RWML self-supervised sim-to-real, Multiplayer World Models 5B Rocket League 20fps, PaW policy+world co-training, SWIRL latent actions, Kairos regret-aware Physical AI, PAN general interactable long-horizon
- Related Techniques (7): HiPER hierarchical 97.4% ALFWorld, HiMAC macro-micro 83.4% WebShop, SPEAR progressive exploration, CDE curiosity-driven RL, CuES curiosity task generation, cMarlTest curiosity MARL 3D testing, curiosity-driven action games ICM+A3C
- Key themes: Self-play generates transferable reasoning (SPIRAL, MARSHAL, Strat-Reasoner); Foundation models at internet scale (NitroGen CVPR 2026, Game-TARS 500B tokens); Code-as-policy beats large LLMs (AutoHarness, FAMOU); World models maturing for games (9 papers, multiplayer 5B Rocket League); Hierarchical RL unlocks long-horizon (HiPER 97.4% ALFWorld); 7 new benchmarks
- Updated: wiki/index.md, wiki/log.md

## [2026-07-16] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-16)
- New page: wiki/synthesis/2026-07-16/investment-daily.md
- Market: S&P 7,572(+0.38%), Nasdaq 26,269(+0.62%), Dow 52,658(+0.29%), Phil Semi -2.08%, 恒生科技+1.3%, 纳斯达克中国金龙+2.92%, 科创50跌4%+
- US stocks (8): AAPL+4%创新高(Qwen接入Apple Intelligence)/MSFT+2.78%(7/29财报+AI ARR $370亿)/NVDA+0.33%(Vera Rubin量产确认)/META+3.07%(自研芯片Iris 9月量产)/AMD-3.46%(UBS目标价$700)/PLTR-25%YTD(Q1+84.7%)/MU-8%(业绩+345%后回调)/ORCL-AI集群成本$490亿/GW
- HK stocks (7): BABA+4.79%(Qwen接入Apple Intelligence)/MiniMax+13%(ARR $5亿+400%)/智谱+6.7%(GLM-5.2开源SOTA)/美团+5.3%(LongCat-2.0万亿参数)/腾讯+3.9%(回购+AI)/快手+2%(Kling AI $180亿估值)/小米+4%
- A-shares (3): 中际旭创辟谣企稳(1.6T订单覆盖2027)/寒武纪万亿市值(科创板首支)/科创50跌4%+(韩国暴涨6% vs A股半导体暴跌6%)
- 中概股 (10): BABA+4.79%/MNSO+9.37%/YMM+6.54%/BEKE+5.87%/BZ+4.71%/BILI+4.58%/GDS+4.12%/UMC+4.47%/PDD+2.18%/BIDU+1.59%
- EV (4): TSLA-0.43%(Q2交付48万+25%)/BYD天神之眼333万辆+海外+95%/NIO+0.6%(CXMT IPO战略投资)/XPEV+3.18%
- AI热点: PPI降温→加息骤降(~10%概率); Big Tech从芯片轮动软件; Apple Intelligence中国落地7款手机备案; AI CapEx $7500-7690亿(+61-79%); Morgan Stanley集群成本+20%(Vera Rubin $490亿/GW); Agentic AI驱动CPU需求; 国产AI算力自主可控(寒武纪万亿+美团LongCat国产算力训练)
- Key themes: 资金从芯片→Big Tech软件轮动; Apple Qwen入华为AI终端化里程碑; 存储超级周期短期获利回吐不改长期逻辑; 中概AI全球配比1.2%重估空间巨大; A股科创短期估值出清
- Updated: wiki/index.md, wiki/log.md

## [2026-07-16] synthesis | 2026年7月 AI 大模型技术报告速览 (7月16日更新)
- New page: wiki/synthesis/2026-07-16/tech-report-digest.md
- Coverage: 19家机构全面覆盖 — DeepSeek V4-Pro/Flash/V3.2/R2, OpenAI GPT-5/5.6/GPT-Live, Meta LLaMA 4 Scout/Maverick/Behemoth, Google Gemini 2.5 Pro/Flash, Anthropic Claude Fable 5/Mythos 5/Opus 4.6/Sonnet 4.5, Mistral Small 4/Large 2, Qwen3.5-397B-A17B, Microsoft Phi-4-RV-15B/Phi-4.5-Small, Apple AFM 3.0, NVIDIA Nemotron Nano 2, xAI Grok 4, Amazon Nova 2, Zhipu GLM-5/5.2, Intern-S1-Pro 1T/InternVL3.5, Moonshot Kimi K2/VL-A3B, StepFun Step-3/Step-Video-T2V, ByteDance Seed 1.6/1.7/Seedream 2.0/Seed-Coder, 01.AI Yi-Lightning, Baichuan M4
- Key trends: MoE全面普及(所有主要模型), 推理模型标准化(GRPO-PR/thinking/Deep Think), 长上下文竞赛升级(10M Meta/1M DeepSeek/Gemini/GLM-5.2), 多模态成标配(除DeepSeek/NVIDIA外全部), Agent工具使用成标配(Kimi Agent Swarm/GLM-5异步Agent RL/Claude Computer Use), 端侧部署受重视(Apple AFM 3.0/Phi-4.5-Small/Nemotron Nano 2), 训练成本优化(DeepSeek V3 $5.6M)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-16] synthesis | arXiv Paper Check — AI & CTR (July 16, 2026)
- New page: wiki/synthesis/2026-07-16/arxiv-paper-check.md
- Coverage: 16 curated papers from cs.AI (148 new Jul 16), cs.IR (10 new Jul 16), cs.LG (~200+)
- AI Agents (6): Do Agent Optimizers Compound? (RELAI-VCL 76.4% lifelong pass, regression control critical), Theory-Level Autoformalization (ICML 2026 Spotlight, complete theory libraries), Experience Memory Graph (one-shot error correction), Self-Evolving Health Agent, LAPO (process rewards for multi-turn search), Self-Improvements in Agentic Systems survey (97 pages)
- CTR/Recommendation (6): TMallGS (Alibaba Tmall unified Transformer search ranking, heterogeneous tokenization), DANet discount-aware CVR (SIGIR 2026, +3.63% pCVR deployed), IBA information-gain budget allocation for generative rec, Learning to Forget satiation-aware transducers (SIGIR 2026), Mitigating Early CTR Collapse (sparsity control > LR tuning), Not Only NTP extending training signal
- Retrieval/Search (3): Cluster with Auctions for Vector Search (NeurIPS 2026), MESH heterogeneous content retrieval, GEO survey (45 studies on generative engine optimization)
- Code Generation (1): Generative Compilation (on-the-fly Rust compiler feedback, sealors, Lean-verified)
- Key themes: Agent optimization must be regression-controlled to compound; industrial CTR moving from DLRM → unified Transformer; discount/pricing signals underexploited; Semantic IDs + latent reasoning maturing; compilers as active generation participants
- Updated: wiki/index.md, wiki/log.md

## [2026-07-15] synthesis | WorldQuant 101 Alpha 因子选股日报 — 美股 Top 20 (2026-07-15)
- New page: wiki/synthesis/2026-07-15/wq101-alpha-daily.md
- Market: S&P 7,543(+0.38%), Nasdaq 26,107(+0.90%), Dow 52,508(+0.02%), CPI 3.5%降温
- Events: Q2银行财报开门红(GS EPS+92%/JPM创纪录); CPI 6年来首次环比下降→加息概率<20%; 美伊冲突油价$79.82; AAPL创52周新高$323; IBM暴跌25%
- Factor structure: Alpha#1 momentum (10/50%) dominant + Alpha#6 volume-price (4/20%); 能源超卖反弹+金融业绩驱动+科技估值修复三线并行
- Top 20: 5 financial (GS/JPM/BAC/V/HD), 7 tech (NVDA/AAPL/META/TSM/AVGO/AMD/MSFT), 2 energy (CVX/XOM), 3 healthcare (UNH/ABBV/JNJ), 1 storage (MU), 2 consumer (NFLX/DEO)
- Top 3: GS(10/Alpha#1,6) — 业绩爆发EPS+92%+动量加速; NVDA(9.5/Alpha#1,41) — Fwd P/E 22x历史低位+PEG 0.50; AAPL(9.5/Alpha#1,30) — 三角形突破$323+Services $31B/季
- Key themes: 金融板块GS/JPM业绩验证资本周期回升; 科技估值回归合理区间(MSFT P/E 22x/NVDA P/E 22x); 能源超卖反弹(CVX RSI 20→45); 医疗保健RRG领先象限持续; CPI降温→利率预期下修利好成长股
- Updated: wiki/index.md, wiki/log.md

## [2026-07-15] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 15, 2026)

## [2026-07-15] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 15, 2026)
- New page: wiki/synthesis/2026-07-15/game-rl-daily.md
- Coverage: 25 curated papers across 7 categories
- Game RL (4): GAE limitation in imperfect-info self-play RL (CMU), Yahtzee stochastic combinatorial RL, HiComm hierarchical communication MARL, AlphaEvolve discovering MARL algorithms (DeepMind)
- Game AI Bot (4): LLM agents competition/cooperation dynamics, cross-platform LLM NPC Unity+Discord, Slay the Spire 2 LLM testbed, GAMEBoT ACL 2025 transparent LLM reasoning assessment
- Foundation Models (3): NitroGen CVPR 2026 (NVIDIA 40K hrs, 1000+ games), Generalist GP survey Tsinghua (5-level roadmap), LLM Game Agent survey Georgia Tech/ACM Surveys 2026
- PCG (3): MIPCGRL multi-objective instruction GIST, PCGRLLM LLM reward IEEE ToG, PCG+LLM survey AIIDE 2024 (207 papers)
- Benchmarks (4): GameEngineBench UE5 C++ 55.5% pass@1, GBQA ICLR 2026 WS 48% bug discovery, GameWorld NUS 34 browser games, TowerMind tower defence
- Industry (2): GameEngineBench production C++ gap, cross-platform NPC systems
- Related Techniques (5): World Models comprehensive survey, probing IRIS/DIAMOND latent representations ICLR 2026 WS, MetaWorld hierarchical skill transfer, Self-Play survey Tsinghua/Tencent, Reward Models survey Nanjing U
- Key themes: Foundation models at internet scale (NitroGen); self-play as reasoning paradigm (AlphaEvolve MARL discovery); LLM game agents still far from human; PCG+LLM complementary workflows; world models maturing; GAE limitations exposed for imperfect-info games
- Updated: wiki/index.md, wiki/log.md

## [2026-07-15] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-15)
- New page: wiki/synthesis/2026-07-15/investment-daily.md
- Market: S&P 7,543(+0.38%), Nasdaq 26,107(+0.90%), Dow 52,508(+0.02%), SMH +2.54%
- US stocks (7): NVDA+4%(H20恢复+RTX PRO)/IBM-25%(54年最大跌幅)/MU+4.9%/AMAT+5.3%/CRWD+11.5%/PANW+6.8%/TSLA+0.36%(EPS超预期)
- HK stocks (8): BABA+17%周/腾讯+6.7%(Hy3极致量化)/美团+9.9%(LongCat-2.0开源)/小米+9.5%/百度+6%/商汤+12%/快手+1%(Kling AI $180亿估值)/中芯国际+8.2%
- A-shares (6): 新易盛20%涨停(Q2利润+51%)/中际旭创+17%/天孚通信+12%/澜起科技15日翻倍/寒武纪/MICR/中芯国际
- 中概股 (10): BABA-0.03%/PDD-0.77%/JD-0.14%/BIDU-3.23%/XPEV+3.28%/LI+2.38%/NIO+1.73%/BILI-0.63%/NTES-2.31%/PDD-0.77%
- EV (4): TSLA+0.36%(EPS超预期)/BYD璿玑A3 4nm芯片/XPEV L4路测/NIO 70万辆世界模型OTA
- AI热点: NVIDIA恢复H20对华销售+RTX PRO合规GPU/CPI 3.5%加息预期骤降/IBM客户支出转向AI硬件/腾讯Hy3极致量化单卡跑295B/美团LongCat-2.0开源1.6T参数/字节探索物理AI/中国AI模型API连续10周超美国/全球AI CapEx $7500亿(+80% YoY)/长鑫科技IPO+长江存储辅导/光模块800G/1.6T渗透率提升
- Key themes: CPI降温→芯片股全线反弹/光模块成A股绝对主线/国产算力自主可控加速/AI模型→API→商业化闭环验证/存储超级周期(涨价+IPO)/物理AI元年
- Updated: wiki/index.md, wiki/log.md

## [2026-07-15] synthesis | 2026年7月 AI 大模型技术报告速览 (7月15日更新)
- New page: wiki/synthesis/2026-07-15/tech-report-digest.md
- Coverage: 19家机构全面覆盖 — DeepSeek V4-Pro/Flash/V3.2/R1, OpenAI GPT-5/5.6/GPT-Live, Meta LLaMA 4 Scout/Maverick/Behemoth, Google Gemini 2.5 Pro/Flash, Anthropic Claude Fable 5/Mythos 5/Opus 4.8/Sonnet 4, Mistral Small 4/Medium 3.5/Leanstral 1.5, Qwen3/Qwen3.5-Omni/Qwen-Image-2.0/Qwen-VLA, Microsoft Phi-4-reasoning-vision-15B, Apple AFM PT-MoE, NVIDIA Nemotron 3 Ultra/Super/Nano, xAI Grok 4/4.1/4.20, Amazon Nova 2/Premier, Zhipu GLM-5/5.2, Intern-S1-Pro 1T/InternVL3.5, Moonshot Kimi K2/K2.5, StepFun Step-DeepResearch/StepFun-Prover, ByteDance Seed1.8/Seed1.5-VL, 01.AI Yi-Lightning, Baichuan M4
- Key trends: MoE全面普及(所有主要模型), 混合架构(Mamba-Transformer/CSA+HCA), Agent能力成核心竞争力(Kimi Agent Swarm/GLM-5异步Agent RL), 百万Token上下文标配(DeepSeek V4/LLaMA 4 10M/Gemini 1M+), RL后训练多范式(GRAP/异步RL/AgentRL/CascadeRL/CISPO), 垂直模型崛起(Baichuan M4医疗登顶3大榜单幻觉率3.3%), 开源白热化(Mistral Small 4 Apache 2.0/Kimi K2/GLM-5/Nemotron 3), 推理时间Scaling成新轴(Gemini Deep Think/Seed1.8/Leanstral 1.5)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-15] synthesis | 顶会论文专题报告 — Conference & arXiv Digest (2026-07-15)
- New page: wiki/synthesis/2026-07-15/conference-digest.md
- Coverage: 200+ papers across 12+ conferences, 20+ labs
- ICML 2026: Outstanding (Flexibility Trap, High-Accuracy Sampling), Test of Time (A3C), Agents (HiPER 97.4% ALFWorld, JitRL 30× cheaper, Multi², BEACON 92.9% ALFWorld, GLARE, HPO, Reasoning Collapse)
- ICLR 2026: Outstanding (Transformers Succinct, LLMs Lost Multi-Turn 39% drop), Honorable (Polar Express/Muon), 5356 accepted, 223 oral
- CVPR 2026: Best (D4RT DeepMind/Oxford dynamic 4D, O-Voxel Microsoft/Tsinghua 3D), Honorable (SAM 3D Meta 5:1 preference), 4090/16092 accepted
- AAAI 2026: TreeBridge Shopee +1.55% GMV, MoMoREC Taobao +6.3% GMV, RecCocktail, Monosemantic Rec, SPINRec, RecToM
- NeurIPS 2025: MeanFlow FID 3.43 one-step, Energy Matching, PartCrafter, AlignedGen DiT style, GPSToken, ARGenSeg
- KDD 2026: CTR-Sink Ant Group (attention sink for LM-CTR), GR4AD Kuaishou +4.2% ad rev, GenRec JD +9.5% clicks, UniSID, MARS Kuaishou deployed
- ACL 2026: PaCoRe 94.5% HMMT surpassing GPT-5 (8B model), Deliberative Searcher 96% false-certainty reduction, Think in Sentences +7.7% GSM8k
- WWW 2026: GenCI generative CTR, SparseCTR Meituan +1.72% CTR, ThinkRec, GEMS unified S&R
- SIGIR 2026: GEMS gradient multi-subspace, SIGMA AliExpress
- Key Trends: Hierarchical agent decomposition, training-free methods (JitRL), attention sink for CTR, generative recommendation scaling, one-step diffusion FID 3.43, 3D generation at production scale
- Industry Deployments: Meta SAM 3D, Shopee TreeBridge, Taobao MoMoREC, Kuaishou MARS/GR4AD, LinkedIn LLM Retrieval, JD GenRec, Meituan SparseCTR
- Updated: wiki/index.md, wiki/log.md

## [2026-07-15] synthesis | arXiv Paper Check — AI & CTR (July 15, 2026)
- New page: wiki/synthesis/2026-07-15/arxiv-paper-check.md
- Coverage: 16 curated papers from cs.AI (157 new Jul 15), cs.LG (1776 July), cs.IR
- AI Agents (6): E3 complexity-aware execution (85% cost cut), OAT unsupervised failure attribution (200-5000× faster), Critic Experience Bank step-level confidence (54% ECE reduction), PM-Bench prospective memory (COLM 2026, GPT-5.4 only 65.1% F1), MemOps lifecycle memory operations, Function-Aware FIM mid-training (+3.2 SWE-Bench)
- Scientific AI (1): Mechanistic World Models (Posner/Schölkopf — paradigm for autonomous discovery)
- Safety (1): Isolation as first-class principle for LLM-agent safety (5-boundary taxonomy)
- Evaluation (2): Bayesian Accuracy length bias correction (ICML 2026), Elenchos abductive reasoning (detection-attribution dissociation)
- Systems (2): On-Device Deep Research at 4B (exposure vs retrieval levers), PEFT Block-Diffusion negative result (drafter must be cheaper than verifier)
- CTR/RecSys (4): CADET LinkedIn decoder-only ads CTR (+11.04% lift), EST Alibaba unified CTR scaling (+3.27% RPM), Beyond Positive Signals mixed-polarity (+9.6% AUC), DS-MLP vanilla MLP SOTA
- Key trends: Agent efficiency as new frontier; memory as lifecycle not storage; detection≠attribution; CTR scaling laws go unified; negative signals matter; simplicity wins in CTR
- Updated: wiki/index.md, wiki/log.md

## [2026-07-15] synthesis | arXiv Daily Report — AI, LLMs, Recommendation, CTR, Advertising, Sequential Modeling, Games
- New page: wiki/synthesis/2026-07-15/arxiv-daily.md
- Coverage: 15 curated papers across 4 categories
- Advertising/CTR (4): CADET (LinkedIn decoder-only ads CTR, +11.04% lift, deployed), IDProxy (Xiaohongshu MLLM cold-start, deployed), GenLI (generative long-term interest, O(1) retrieval), Beyond Positive Signals (mixed-polarity sequences, +1.9–9.6% AUC)
- Sequential Modeling/Rec (3): PANTHER (WeChat Pay generative pretraining, 25.6% HitRate@1, deployed), TGA (Alibaba multi-behavior transitions, WWW 2026, deployed), PerSRec (Meta personalization, ICDM 2025)
- LLM/Multi-Agent (5): MARLIN (HP Labs game-theoretic sustainable LLM inference, -33% carbon), GARL (Tsinghua game-theoretic RL, open-source LLMs competitive with closed-source), Beyond the Leaderboard (Oxford 27-paper failure taxonomy), MALLM (Göttingen decision protocols), MALMAS (USTC memory-augmented, ACL 2026)
- Games (3): Never-losing chess engine, human-AI coordination, contextual-bandit oversight
- Key trends: Decoder-only transformers dominate ads CTR; MLLMs as embedding generators for CTR; mixed-polarity behavior sequences challenge positive-only assumption; generative pretraining extends from language to user behavior; game-theoretic RL convergence
- Updated: wiki/index.md, wiki/log.md

## [2026-07-14] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-07-14)
- New page: wiki/synthesis/2026-07-14/wq101-alpha-daily.md
- Market: S&P 7,431(-0.79%), Nasdaq 25,822(-1.55%), Dow 52,872(-0.35%), VIX 17.16, Brent ~$106
- Events: Q2 bank earnings (JPM/GS/BAC/C/WFC); chip rout (MU -4.3%, NVDA -3.5%, AMD -4.2%); Iran conflict oil surge
- Factor structure: Alpha#1 momentum (8/40%) from tech→energy/finance/defense; Alpha#41 trend (7/35%); Alpha#6 volume-price (6/30%)
- Top 20: 5 energy (XOM/COP/OXY/CVX/LNG), 3 financial (GS/JPM/BAC), 3 industrial/defense (CAT/LMT/RTX), 5 tech (MSFT/AVGO/GOOGL/AAPL/META), 1 utility (NEE), 2 healthcare (JNJ/UNH), 1 staples (PG)
- Top 3: XOM(9.5)/GS(9.3)/CAT(9.2)
- Key themes: Sector rotation dominant; energy +22% YTD leads; MSFT -22% 52W oversold reversal; defense budget $1.5T; Q2 earnings season starts
- Updated: wiki/index.md, wiki/log.md

## [2026-07-14] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 14, 2026)
- New page: wiki/synthesis/2026-07-14/game-rl-daily.md
- Coverage: 48 curated papers across 7 categories
- Game RL (5): MARL-GPT (foundation model for MARL), Generals.io superhuman AI (self-play RL), Stratagem (transferable reasoning via game self-play), AlphaZero Tablut (asymmetric board games), Generative Gamer (LLM dynamic deduction, ACL 2026)
- Game AI Bot (5): Bounded Autonomy (LLM characters live multiplayer), Nemobot (NUS LLM game agents), PTCG-Bench (Pokémon TCG LLM agents), Orchestrated Reality (LLM POMDP game world), OpenGame (agentic coding)
- Foundation Models (6): NitroGen CVPR 2026 (NVIDIA 40K hrs, 1000+ games), Game-TARS ByteDance (500B+ tokens, keyboard-mouse), Pixels2Play (8300+ hrs open BC), Generalist GP survey Tsinghua (5-level roadmap), GameVerse (video reflection), Lumine (5-hr open-world completion)
- PCG (7): IPCGRL (language-instructed RL), PCGRLLM (LLM reward design), Multiverse (cross-game level blending), Agentic PCG (tool-using LLMs), GRPO fun-aligned levels, Narrative Arc conditioning, MultiGen (diffusion multiplayer)
- Benchmarks (9): OmniGameArena UE5 IDC, GameWorld 34 games, AgentOdyssey text games, Orak KRAFTON 12 games MCP, PTCG-Bench, CivBench Civilization V, StarBench Star Rail, MineExplorer Minecraft, CausalGame
- Industry (2): Augmenting Game AI industry, Experience Transfer CVPR 2026 Minecraft
- Related Techniques (14): SPIRAL, MARS, MEMO, CuES, SuS, Mind-Studio, GameCWM distillation, WISE, MineEvolve, Sensi, AlayaWorld, WorldCam, RWML, Scalable Multi-Task RL
- Key themes: Foundation models at internet scale (NitroGen, Game-TARS); self-play as LLM reasoning paradigm (SPIRAL, MARS, Stratagem); executable world models via LLMs (Mind-Studio, GameCWM); memory and self-evolution critical (WISE, MineEvolve, MEMO); 8 new game benchmarks
- Updated: wiki/index.md, wiki/log.md

## [2026-07-14] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-14)
- New page: wiki/synthesis/2026-07-14/investment-daily.md
- US stocks (6): AAPL $323创新高(起诉OpenAI)/NVDA $211(大摩$288目标价)/GOOGL融资$800亿AI基建/MSFT Build七款自研模型/META追加$400亿Hyperion/TSLA Model Y Performance中国申报
- HK stocks (5): 百度+7.5%(昆仑芯$500亿IPO)/智谱+40%破万亿/GLM-5.2全量开放/商汤开源视觉模型/腾讯云DeepSeek-V4降价97.5%
- A-shares (3): 中芯国际+18%创历史新高(市值1.25万亿)/澜起科技15日翻倍(市值3000亿)/存储芯片涨停潮
- 中概股 (2): BABA $90→$110反弹(AI ARR ¥358亿)/BIDU AI收入占比首过半52%
- EV (4): BYD海外+95%/NIO上调至买入$7/XPEV Q2最佳月份/LI 6月交付-15%
- AI热点: DeepSeek $450亿估值(大基金领投)/Anthropic洽谈微软Maia芯片/OpenAI Codex整合ChatGPT/美团LongCat-2.0五万卡国产算力训练
- Key themes: AI CapEx $7500亿(+80% YoY)/国产算力自主可控加速/AI商业化拐点验证/存储超级周期分化/NEV需求疲软
- Updated: wiki/index.md, wiki/log.md

## [2026-07-14] synthesis | 2026年7月 AI 大模型技术报告速览 (7月14日更新)
- New page: wiki/synthesis/2026-07-14/tech-report-digest.md
- Coverage: 19家机构全面覆盖 — DeepSeek V3/R1/V3.2/V4, OpenAI o1/o3/o4-mini/GPT-5/GPT-5.5, Meta LLaMA 4, Google Gemini 2.5 Pro/Flash, Anthropic Claude Opus 4/Sonnet 4/4.1 Opus, Mistral Large 2/Magistral/Devstral, Qwen2.5/Qwen3/Qwen3.5, 01.AI Yi-Lightning, Baichuan M3/M4, Microsoft Phi-4/Phi-4-RV-15B, Apple AFM, NVIDIA Nemotron 3 Ultra, xAI Grok 4, Amazon Nova, Zhipu GLM-4.5/GLM-4, InternLM3/Intern-S1, Moonshot Kimi K2/K2.5, StepFun Step 3/Step 3.7 Flash, ByteDance Seed 2.0/Seedream 2.0
- Key trends: MoE架构成为主流, Reasoning模型标配化, 长上下文竞赛升级(10M Meta/1M Gemini), 中国AI实验室MoE+Reasoning重投入, 多模态成标配, Agent工具使用成标配, 端侧部署受重视, 训练成本优化(DeepSeek-V3 $5.576M), 模型能力持续突破(Claude 4.1 Opus GPQA 57%, GPT-5.5 agentic能力, DeepSeek-V4 KV cache 10% of V3.2)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-12] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-12)
- New page: wiki/synthesis/2026-07-12/investment-daily.md
- Market context: S&P 7575.39 距历史新高仅 0.6%; 纳指周 +1.74% 科技重夺领导力; 恒生科技 +5.33% 本周爆发; 创业板指创历史新高
- US stocks (11 stocks): META(+14.81% 周线最佳)/NVDA(+8.28%)/TSLA(+3.64%)/AAPL(+2.17%)/AMZN(+1.10%)/GOOGL(-0.76%)/MSFT(-1.38%)/SKHY(IPO +13.1%)/AMD(-8%)/AVGO/PLTR
- HK stocks (10 stocks): 阿里巴巴(+17.11%)/美团(+9.92%)/腾讯(+6.73%)/小米(+9.5%)/百度(+6%)/快手(+1.03%)/商汤(+2.17%)/智谱(-8.53%)/MINIMAX(-22.50%)/中芯国际
- A-shares (10 stocks): 中际旭创/新易盛/中芯国际/寒武纪/海光信息/北方华创/中微公司(+33% 12日)/天孚通信/工业富联/长鑫科技(Q1营收+719% YoY)
- 中概股 (10 stocks): BABA(+11%)/JD(+6%/$1000亿市值)/BIDU/PDD/NTES/BILI/NIO/XPEV/LI/TME
- EV (8 stocks): TSLA(Q2交付48万)/BYD(全球纯电销冠55.7万辆)/小米SU7(月交付10万+)/NIO/XPEV/LI/宁德时代/阳光电源
- AI热点: GPT-5.6全面公开(Sol/Terra/Luna)/Meta Muse Spark 1.1+Model API/腾讯Hy3+Agent Bucket/阿里云+45%增速/中国10万卡AI超算集群(郑州)/数据中心建设+190% YoY/$7500亿CapEx/美国25+州数据中心立法/AI推理成本2年降90%
- Key themes: 科技板块全球同步走强; AI模型→API→商业化闭环验证; 存储超级周期(DRAM+497%/NAND+352%); 港股低估值+AI催化+南向资金三重支撑; Q2财报季7/14启动验证AI CapEx回报
- Updated: wiki/index.md, wiki/log.md

## [2026-07-13] update | Game RL & Game AI Bot — Daily Paper Digest (July 13, 2026)
- Summary: wiki/synthesis/2026-07-13/game-rl-daily.md

## [2026-07-14] synthesis | arXiv Daily Digest — AI, LLMs, Recommendation, CTR, Games & Sequence Modeling
- New page: wiki/synthesis/2026-07-14/arxiv-daily.md
- 32 papers from recent arXiv submissions (July 2026)
- Categories: LLM Training & RL (6), LLM-as-a-Verifier (1), Audio/Multimodal (2), Recommendation/Advertising/CTR (8), Games/RL Agents (7), State Space Models & Sequence Modeling (7), NeuroAI Theory (1)
- Key themes: RL post-training dominance, industrial generative recommendation, hybrid SSM-Transformer theory foundations, long-horizon game RL for VLMs, verification as scaling axis
- Updated: wiki/index.md
- Updated: 35 → 53 papers across 7 categories
- Added 18 new papers: GARL (game-theoretic RL), Augmenting Game AI (CoG 2026), MARL Review (IEEE ToG), HLSMAC (StarCraft stratagems), SMAC-Talk, SeRL self-play LLM, Echo Minecraft transfer, OmniGameArena UE5, DSGBench strategic games, GameDevBench, JOWA offline MBRL 150M, Agent World Model, DiNAT-RCM curiosity Atari, Advanced Game-Theoretic Frameworks, Multi-task PCG Scientific Reports
- Updated: wiki/index.md, wiki/log.md

## [2026-07-14] synthesis | Conference & arXiv Digest — ICML/AAAI/NeurIPS/ICLR/CVPR/KDD/ACL/SIGIR/WWW 2026
- New page: wiki/synthesis/2026-07-14/conference-digest.md
- 15 sections, 12+ venues, 50+ papers, 15+ labs
- ICML 2026 Outstanding: Flexibility Trap (Tsinghua), High-Accuracy Diffusion Sampling (MIT/Yale); Test of Time: A3C (DeepMind 2016)
- ICLR 2026 Outstanding: Transformers Succinct (MPI-SWS), LLMs Lost Multi-Turn
- CVPR 2026 Best: D4RT (Google DeepMind/Oxford/UCL)
- AAAI 2026: InTRO (+20% math reasoning), PRIME (dual-process), CDCR-SFT (surpass human CLADDER)
- KDD 2026: CTR-Sink (Ant Group), SRPFN (synthetic prior RecSys), FlowTime (Kuaishou watch time)
- ACL 2026: KARL (THUDM, beats GPT-4o), SOAR (+16.9% deep research), Miner (+4.58% over GRPO)
- SIGIR 2026: LTRR, SmartSearch, SA²CRQ (JD.com deployed), Agentic Search 14M+ logs
- CTR Production: OneRanker (Tencent GMV+1.34%), EST (Taobao RPM+3.27%), RankUp (Tencent GMV+4.81%)
- Agent Systems: MILES, BIGMAS, DOLORES (8B beats 32B), SMTL (OPPO, BrowseComp 48.6%)
- Code Execution: Latent Programming Horizons (25-step lookahead), Self-RLEF, LongHorizonTerminalBench (GPT-5.5 only 15.2%)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-12] ingest | arXiv Paper Check — AI & CTR (July 12, 2026)
- Summary: wiki/synthesis/2026-07-12/arxiv-paper-check.md
- Coverage: 20 curated papers from cs.AI (~188K), cs.LG (~276K), cs.IR (~925 CTR)
- Key papers: Illusion of Equivalency (quantization), Super Weights (COLM 2026), SLORR (low-rank reg), Memory Agent (+8.3pp), WebSwarm, OpenCoF (video reasoning), POEM (Kuaishou CTR), RankGraph-2 (Meta +0.96% CTR), Beyond Positive Signals (+9.6% AUC), EMA-FS (LightGBM 2.61×), ARDY (SIGGRAPH 2026)
- Updated: wiki/index.md, wiki/log.md
- New pages: wiki/synthesis/2026-07-12/arxiv-paper-check.md
- Contradictions: none

## [2026-07-12] synthesis | arXiv AI Search Report
- New page: wiki/synthesis/2026-07-12/arxiv-ai-search.md
- Coverage: 20+ curated papers across 6 categories (Recommendation, CTR/Advertising, Sequential Modeling, LLMs, Games, Cross-cutting)
- Key papers: SCOReD (CoT distillation for rec), Agentic Rec Systems survey, GenLI (generative long-term interest), IDProxy (Xiaohongshu cold-start CTR), GRAB (Baidu generative CTR), DS-MLP (dual-stream MLP CTR), Diffusion-GR2 (diffusion re-ranker), Beyond Positive Signals (mixed-polarity sequences), TGA (multi-behavior transitions), Generals.io superhuman AI, Nemobot (LLM game agents)
- Key trends: generative paradigms in CTR, LLM in production (Baidu/Xiaohongshu), mixed-polarity negative signals, efficient inference for reasoning, edge LLM deployment, agentic recommendation

## [2026-07-13] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-07-13)
- New page: wiki/synthesis/2026-07-13/wq101-alpha-daily.md
- Market: S&P 500 7,575.39(+1.2%周线), Nasdaq 26,281(+1.7%), Dow 52,367(-0.5%), SOX +3.83%
- Key events: SK海力士Nasdaq IPO(+13.1%/7x超额), Mag 7周线+4.9%反弹, Q2财报季7/14启动(JPM/GS/WFC), 美伊局势升温油价$76+
- Core factor: Alpha#1 动量回归主导(10次/50%) — Mag 7反弹+芯片超卖反弹; Alpha#41趋势确认(6次/30%)
- Top 20: META(9.5, Alpha#1/#12), NVDA(9.3, Alpha#1/#41), MU(9.0, Alpha#1/#30), AAPL(8.8, Alpha#1/#6), JNJ(8.5, Alpha#30/#19), MSFT(8.3, Alpha#19/#41), AMD(8.0, Alpha#53/#1), AVGO(7.8, Alpha#1/#41), TSM(7.7, Alpha#1/#6), KO(7.5, Alpha#30/#19), GOOGL(7.3, Alpha#53/#19), TSLA(7.2, Alpha#1/#53), JPM(7.0, Alpha#1/#41), WDC(7.0, Alpha#1/#30), VRT(6.8, Alpha#1/#6), BABA(6.7, Alpha#53/#12), MRK(6.5, Alpha#30/#19), IBM(6.5, Alpha#1/#6), C(6.3, Alpha#1/#41), LLY(6.2, Alpha#30/#19)
- Sector: 半导体6只, 科技5只, 医疗3只, 金融2只, 消费1只, 汽车1只, 工业1只, IT服务1只
- Key change vs 07-09: Alpha#1动量强势回归(从Alpha#19主导); 半导体从3→6只; 科技从8→5只; 能源从3→0只; Top 3从防御(LLY/XOM/CVX)→成长(META/NVDA/MU)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-13] synthesis | arXiv Daily Report — AI, LLMs, Recommendation, Advertising, CTR, Games (2026-07-13)
- New page: wiki/synthesis/2026-07-13/arxiv-daily.md
- Coverage: 35 curated papers across 5 categories
- AI/LLMs (4): LLM-as-a-Tutor (KAIST, prompt adaptation for non-verifiable RL), LLM-as-a-Verifier, Set Diffusion (autoregressive-diffusion interpolation), Legible-by-Construction
- Recommendation (12): UniRec (Shopee +5.37% PVCTR, Chain-of-Attribute), GEMs (lifelong GR 100K+ sequences), Gryphon (Yandex Music item-level scoring), R3-REC (retrieval-augmented reasoning), CMSL (Meta multi-sequence learning), AgentX (Kuaishou self-iterating rec, RMB 100M+ annualized), GenAIR (archetype-grounded representations), SIDReasoner (reasoning over SIDs), Beyond Interleaving (Meta causal attention), FAVE (one-step flow matching), PRISM, Self-Evolving Rec
- Advertising/CTR (9): EST (Taobao unified transformer +3.27% RPM), GR4AD (Kuaishou generative ads +4.2% revenue), OneRanker (Tencent Weixin +1.34% GMV), GRAB (Baidu +3.05% revenue), LLM-HYPER (LLM hypernetwork cold-start), IDProxy (Xiaohongshu multimodal cold-start), GenCI (generative cohort intent), SparseCTR (sparse attention scaling law), CaliCausalRank (calibrated multi-objective)
- Games/Multi-Agent RL (8): CausalGame (ICML 2026 Oral, 30 LLMs benchmarked), ACPO (exact policy gradient decomposition), UnityMAS-O (general RL for LLM MAS), NePPO (potential function for general-sum), Dr. MAS (GRPO stability), MEMO (memory-augmented self-play), Cognitive Training (Xent Games), AgentOdyssey (test-time continual learning)
- Multi-Agent Systems (2): LLM-as-Environment-Engineer, Orchestration Traces RL
- Key themes: Generative recommendation maturing (UniRec, GR4AD, GEMs deployed at scale); LLM agents in production ads (LLM-HYPER, IDProxy); causal reasoning gap persists (CausalGame); self-evolving systems (AgentX); scaling laws for CTR (EST, SparseCTR)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-13] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 13, 2026)
- New page: wiki/synthesis/2026-07-13/game-rl-daily.md
- Coverage: 35 curated papers across 7 categories
- Game RL (5): SPIRAL ICLR 2026 (self-play reasoning), Code World Models (DeepMind LLM→code→MCTS), DeepMind RL review, Self-play survey (Tsinghua/Tencent), LLM Game Agents survey (Georgia Tech)
- Game AI Bot (5): Nemobot (NUS, Shannon taxonomy + LLMs), PCSP (persona-conditioned shared RL policy, 64 agents UE5), CPDC 2025 1st place (GRPO for NPC dialogue), AI LOD (SIGGRAPH 2026, distance-aware quantization), RuleSmith (LLM-as-player for game balancing)
- Foundation Models (3): NitroGen CVPR 2026 (NVIDIA, 40K hrs, 1000+ games), Generalist GP survey (Tsinghua, 5-level roadmap), CoMaTrack (3B VLA beats 7B via competitive MARL)
- PCG (4): PCGRLLM (LLM reward design for PCGRL, IEEE ToG), PCG+LLM survey (AIIDE 2024, 207 papers), PCG Benchmark (12 problems, open-source), Co-adaptive DRL Level Design
- Benchmarks (5): BALROG ICLR 2025 (LLM agentic on 6 RL envs), SC2BA (algorithm-vs-algorithm StarCraft), TeamCraft (55K Minecraft multi-modal multi-agent), OpenGuanDan (Chinese card game), BuilderBench (DeepMind block-building)
- Industry (3): NVIDIA ACE/NVIGI SDK (production LLM NPCs), INFUSE Engine (Actor-Director pattern), GenAI NPC production survey
- Related Techniques (10): CDE curiosity for LLM RL, HWM hierarchical planning (Meta), RLVR-World (Tsinghua), π-Play self-distillation, Matrix-Game world model, TheoryCoder (Harvard), MFG survey (DeepMind), Visual Generative Models + RL survey
- Key themes: Foundation models at internet scale (NitroGen); self-play as LLM reasoning paradigm (SPIRAL); LLM-generated code world models (DeepMind); NPC intelligence entering production (NVIDIA ACE); PCG+LLM complementary workflows; game benchmarks maturing (5 new benchmarks)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-13] synthesis | Investment Daily — 全球科技与 AI 板块 (2026-07-13)
- New page: wiki/synthesis/2026-07-13/investment-daily.md
- Market context: NVDA $211(+4%/周+5%), S&P 7,575(+0.42%), 恒生科技4,783(+4.95%周线), A股半导体市值首超银行
- US stocks (7 stocks): NVDA/AVGO/META/MSFT/TSLA/MU/AMD
- HK stocks (4 stocks): 小米/网易/中芯国际/联想
- A-shares (4 stocks): 寒武纪/云天励飞/澜起科技/中际旭创
- 中概股 (5 stocks): BABA/BIDU/JD/PDD/NTES
- EV (5 stocks): BYD/NIO/XPEV/LI/TSLA
- AI热点: AI CapEx $941B(TrendForce上调九大CSP至$830B+79%YoY); 存储超级周期(SK海力士Nasdaq IPO+美光$2500亿+韩国$3T); BABA两日+12%四大催化(DOUJ/五角大楼/即时零售/H200); BYD Q2 557K辆夺回全球BEV冠军; A股寒武纪+17.7%国产AI芯片加速
- Key themes: AI CapEx超级周期全面确认; 存储超级周期延续; 港股恒生科技强势反弹+5%; A股半导体市值首超银行; 中概ADR估值洼地; Mag 7估值修复窗口; 新能源车BYD增长放缓+EU关税风险; AI芯片板块内部分化
- Updated: wiki/index.md, wiki/log.md

## [2026-07-13] synthesis | 2026年7月 AI 大模型技术报告速览
- New page: wiki/synthesis/2026-07-13/tech-report-digest.md
- Coverage: 19家机构全面覆盖 — DeepSeek V3/R1, OpenAI GPT-5/5.5, Meta LLaMA 4, Google Gemini 2.5 Pro/Flash, Anthropic Claude Opus 4/Sonnet 4, Mistral Large 2/Magistral/Devstral, Qwen3/Qwen2.5-VL, 01.AI Yi-Lightning, Baichuan M3/M4, Microsoft Phi-4/Phi-4-RV-15B, Apple AFM, NVIDIA Nemotron 3 Ultra, xAI Grok 4, Amazon Nova, Zhipu GLM-5/GLM-4.7/GLM-4, InternLM3/Intern-S1, Moonshot Kimi K2/K2.5, StepFun Step 3/Step 3.7 Flash, ByteDance Doubao 2.0/Seedream 2.0
- Key trends: MoE架构成为主流(DeepSeek/Meta/Qwen/GLM-5/Step3/Kimi2), Reasoning模型标配化(GPT-5 thinking/Claude Opus 4/Gemini 2.5 Deep Think/Magistral/Step3), 长上下文竞赛(10M Meta/1M Gemini/200K GLM-5), 中国AI实验室MoE+Reasoning重投入(GLM-5 744B/Step3 321B/Doubao 1T/Kimi2 1T), 多模态成标配, Agent工具使用成标配, 端侧部署受重视, 训练成本优化(DeepSeek-V3 $5.576M)
- Updated: wiki/index.md

## [2026-07-13] synthesis | 顶会论文专题报告 — Conference & arXiv Digest (2026-07-13)
- New page: wiki/synthesis/2026-07-13/conference-digest.md
- Coverage: 200+ curated papers across 12+ venues (ICML 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, AAAI 2026, ACL 2026, WWW 2026, SIGIR 2026, EMNLP 2025, CIKM 2025, RecSys 2025), 20+ labs
- ICML 2026 Outstanding: "The Flexibility Trap" (Tsinghua, diffusion LMs), "High-Accuracy Sampling" (diffusion models), Test of Time (A3C DeepMind)
- ICML 2026 Honorable Mentions: Obfuscation Atlas (RLVR), Motion Attribution, How much memorize, Random Matrix Diffusion, Grokking Ridge Regression
- ICML 2026 Agent RL: HiPER (hierarchical plan-execute, 97.4% ALFWorld), MemoPilot (memory RL, ELO #1), Agentic Monte Carlo, RL-Focal (+8.48% ensemble), JitRL, ML-Agent, DiScoFormer (oral)
- NeurIPS 2025 Best: Gated Attention (Alibaba Qwen, shipped in Qwen3-Next), Artificial Hivemind (70+ LLMs think alike), 1000 Layer RL (2-50x locomotion), Why Diffusion Don't Memorize
- ICLR 2026 Outstanding: Mean Flow Policy, Emergent Dexterity, AlphaAlign (deep safety), WaltzRL (Meta, 39%→4.6% unsafe), Safety Subspaces (EPFL), SPIRAL (self-play reasoning)
- CVPR 2026 Best: D4RT (4D reconstruction), Honorable Mention SAM 3D (Meta), CUPID (+3dB PSNR), MatMart (material diffusion)
- KDD 2026 CTR: GR4AD (Kuaishou, generative ad rec, +4.2% ad rev, 400M DAU), EST (Alibaba, power-law CTR scaling, +3.27% RPM), FAT (+4.38% AUC), RankUp (Tencent), OneMall (Kuaishou)
- AAAI 2026: DMGIN (Alibaba, multimodal LLM lifelong behaviors, +4.7% CTR), TreeBridge (Shopee, LLM embedding alignment, +1.55% GMV), MoMoREC (Taobao, multi-agent motivation, +6.3% GMV)
- ACL 2026: MemRec (collaborative memory agents), RecPO (preference intensity), BLaIR (LLM encoder benchmark, 570M reviews), REASONREC (reasoning multimodal, +30% HR@5), STAR (trajectory distillation)
- WWW 2026: ThinkRec (LLM reasoning for rec), SparseCTR (Meituan, +1.72%), GenCI (generative CTR)
- CIKM 2025: UserIP-Tuning (Huawei, +7.47% AUC deployed), RankMixer (ByteDance), LONGER (ByteDance)
- RecSys 2025: ECAT Best Paper, SUAN (Meituan CTR scaling)
- Key themes: Diffusion LM maturing (ICML Outstanding); Agent RL systematizing (HiPER/MemoPilot/AReaL2.0); CTR scaling laws full bloom (EST/FAT/GR4AD); Generative rec industrialized (GR4AD 400M DAU); LLM+Rec deep fusion (ThinkRec/MemRec/RecPO/Taiji); Safety alignment matured (WaltzRL/AlphaAlign); Gated Attention in production (Qwen3-Next)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-12] synthesis | arXiv Paper Check — AI & CTR (July 12, 2026)
- New page: wiki/synthesis/2026-07-12/arxiv-paper-check.md
- Coverage: 22 curated papers from cs.AI (116 new), cs.IR (5 new) — July 13, 2026 listings
- AI Agent highlights: Agora (auction-based task allocation), TrustX ARC (risk classification), ProofCouncil (mathematical proving), ARCANA (ARC-AGI-2 reflective multi-agent), SAGEAgent (multimodal survival prediction)
- Multimodal & Medical: Multimodal Reward Hacking (first systematic study), LongMedBench (long-horizon clinical decision-making), PHIN-EEG (topological dream-state analysis)
- Memory & Context: Shared Selective Persistent Memory, KV-PRM (KV-cache transfer for multi-agent test-time scaling)
- CTR highlights: CADET (LinkedIn decoder-only ads CTR, +11.04% lift deployed), DPIFrame (23× embedding latency reduction, 5.83× speedup), DS-MLP (simple MLP SOTA via knowledge distillation), Beyond Positive Signals (+1.9–9.6% AUC with mixed-polarity sequences)
- Safety highlights: Scoped Verification (long-horizon agentic context under distribution shift), Neuro-Agentic Control (LLM agents for cybersecurity)
- Scientific AI: Vlasov Equation formalization (AI-assisted Lean), PHIN-EEG (dynamic Betti curves for dream classification)
- Key themes: Agent safety maturing (risk classification, verification, reward hacking); memory architecture as critical bottleneck; CTR simplicity wins (DS-MLP MLP beats complex architectures); multi-agent coordination via auction theory; formal verification integration with AI
- Updated: wiki/index.md, wiki/log.md

## [2026-07-11] synthesis | AI Papers Compilation: June-July 2026
- New page: wiki/synthesis/2026-07-11/ai-papers-june-july-2026.md
- Coverage: 40+ papers/reports across 7 topic areas from June-July 2026
- Topics: LLMs (10), Agent Systems (5), Code Generation (4), Recommendation Systems (7), Generative Models (6), Sequential Modeling (4), Benchmarks (4)
- Key labs: Google DeepMind (Gemma 4, DiffusionGemma, ProEval), OpenAI (GPT-5.6), Meta AI (Muse Spark 1.1, ULTRA-HSTU, Kunlun, LLaTTE), Anthropic (Claude Sonnet 5, A3, Global Workspace), ByteDance (CUDA Agent, MDL, CTR cluster), Alibaba (Qwen ParScale, TGA), NVIDIA (Nemotron Labs), DeepSeek (V4), Singapore MU (EAGER)
- Notable model releases: GPT-5.6 (Jul 9), Muse Spark 1.1 (Jul 9), Claude Sonnet 5 (Jun 30), Gemma 4 (Jun 19), DiffusionGemma (Jun 10)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-11] synthesis | 2026年7月 AI 大模型技术报告速览 — 19家机构全面覆盖
- New page: wiki/synthesis/2026-07-11/tech-report-digest.md
- Coverage: 19 AI orgs — DeepSeek (V3/R1/V4 Pro), OpenAI (GPT-5.5), Meta (LLaMA 4), Google (Gemini 2.5 Pro), Anthropic (Claude Opus 4/4.5 Sonnet), Mistral (Large 2/Codestral 2), Alibaba Qwen (Qwen3/Qwen2.5-VL), 01.AI (Yi-Lightning), Baichuan (Omni-1.5/M3/M4), Microsoft (Phi-4), Apple (AFM on-device+server), NVIDIA (Nemotron 3 Ultra), xAI (Grok 4/4.20), Amazon (Nova family), Zhipu AI (GLM-4), Shanghai AI Lab (InternLM3), Moonshot AI (Kimi K2), StepFun (Step 3.7 Flash), ByteDance (Seedream 2.0)
- Key themes: MoE架构成为主流; Reasoning能力持续强化(RL post-training); 长上下文竞赛升级(10M tokens); 医疗垂直模型崛起(百川M4幻觉率3.3%); Agent和工具使用成为标配; 端侧部署受重视; 训练成本优化(DeepSeek V3仅$5.6M)
- Cross-cutting analysis: 横向对比表格(19模型), 7大关键趋势总结
- Updated: wiki/index.md, wiki/log.md

## [2026-07-11] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-07-11)
- New page: wiki/synthesis/2026-07-11/wq101-alpha-daily.md
- Market context: S&P 500 ~7,543, Nasdaq 100 ~29,698, SOX ~13,800 (+2.2%芯片反弹)
- Key events: SK海力士ADR首日+14%（全球最大外国企业美国上市）、美光Q2财报超预期（$2500亿投资计划）、美伊冲突升级（油价$73.71）、SpaceX纳入纳斯达克100
- Top 20 stocks: MU(9.5), INTC(9.2), AVGO(9.0), AAPL(8.8), LLY(8.7), NVDA(8.5), GOOGL(8.5), AMZN(8.3), AMD(8.3), TSM(8.2), META(8.0), MRVL(8.0), MSFT(7.8), VRT(7.7), CEG(7.5), JPM(7.5), MRNA(7.3), ABBV(7.2), DELL(7.2), PLTR(7.0)
- Factor analysis: Alpha#1 动量因子回归主导（70%，+5 vs 前日）、Alpha#19 均值回复（40%）、Alpha#30 低波动（40%）
- Sector breakdown: 半导体8只、科技5只、医疗3只、工业/能源/金融4只
- Updated: wiki/index.md, wiki/log.md

## [2026-07-11] synthesis | arXiv Paper Check — AI & CTR (July 11, 2026)
- New page: wiki/synthesis/2026-07-11/arxiv-paper-check.md
- Coverage: 18 curated papers from cs.AI (~157 new), cs.LG (~93 new), cs.IR (~3 new) — Friday July 10, 2026 listings
- LLM Reasoning highlights: Pyligent (backtrack/continue/finish framework, +72.7pp on hidden graphs), CompactionRL (#1 trending cs.LG, context compaction for long-horizon agents), Danus (fact-graph memory for math reasoning agents)
- KV Cache highlights: KVpop (learned eviction policy), SeKV (resolution-adaptive hierarchical semantic memory), Linear Attention Architectures (ETH Zurich, 350M study of 4 recurrent architectures + CLVR)
- Vision-Language highlights: SaMer (object-aware token merging for VL retrieval), CMDR (contextual multimodal document retrieval)
- CTR highlights: DiseCTR (OOD CTR disentangled interests, +0.02 AUC, ACM TOIS), CADET (LinkedIn decoder-only ads CTR)
- Safety highlights: Overthinking (ICML 2026, reasoning amplifies harm 10×), CoT persuasion attacks (+9.5% harm), Agreement≠Accuracy (ρ 0.20–0.59)
- Scientific AI highlights: Agentic verifiable rules for chemical reaction classification (EPFL/Schwaller), PraMem (experiential memory for long-horizon behavior)
- Key themes: Reasoning recovery as first-class training objective; KV cache research intensifying (3 papers same bottleneck); Safety implications of test-time compute scaling; Agent generalization fragility (ICML 2026)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-11] synthesis | Investment Daily — 全球科技与 AI 板块 (2026-07-11)
- New page: wiki/synthesis/2026-07-11/investment-daily.md
- Market context: SK海力士Nasdaq IPO(+14%/7x超额认购)为年度最大IPO；NVDA市值>$5T；纳指周线+1.7%；存储超级周期确认(韩国$3T投资计划/SK Hynix CEO称短缺延续至下个十年/江波龙H1净利62204%↑)
- US stocks (9 stocks): SKHY/NVDA/META/AAPL/MU/MSFT/GOOGL/AMZN/TSLA/PLTR/AMD/AVGO
- HK stocks (8 stocks): 腾讯/阿里巴巴/美团/小米/比亚迪/中芯国际/联想/快手/商汤
- A-shares (11 stocks): 江波龙/中芯国际/寒武纪/海光信息/中微公司/北方华创/中际旭创/新易盛/澜起科技/科大讯飞/盛科通信
- 中概股 (12 stocks): BABA/JD/TCOM/BEKE/LI/XPEV/NIO/BIDU/MNSO/KC/VIPS/TME/NTES/PDD/BILI/BZ/TSM/FUTU/PONY
- EV (8 stocks): TSLA/BYD/LI/XPEV/NIO/ZK/宁德时代/小米汽车
- AI热点: 存储超级周期(韩国$3T/MU $2500亿/江波龙业绩爆发); AI CapEx $700B+供需定价(Meta Compute Cloud); 机器人量产(Optimus 2026H2万台); 自动驾驶(FSD V13/Waymo $16B); A股科技调整定性(估值出清非逻辑终结/从β→α范式转变)
- Key themes: 存储超级周期全面确认; AI算力供不应求格局延续; A股科技7月调整为牛市中期估值出清; 港股四大AI主线(大厂生态→算力→应用→终端); Mag 7估值修复窗口; 中概股估值洼地(全球配比仅1.2%)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-10] synthesis | Investment Daily — 全球科技与 AI 板块投资热点 (2026-07-10)
- New page: wiki/synthesis/2026-07-10/investment-daily.md
- Market context: 美光$2500亿投资+SK海力士ADR超额7倍+长鑫科技IPO三重催化；Mag 7估值十年最低；港股AI分化（智谱+11%配售创纪录/MINIMAX解禁-18%）；A股科创50+8.41%年内最大涨幅/半导体净流入¥292亿
- US stocks (9 stocks): Micron/Meta/Tesla/AMD/NVDA/AMAT/AVGO/Broadcom/Oracle等
- HK stocks (7 stocks): 阿里巴巴/腾讯/中芯国际/智谱/MINIMAX/联想/商汤
- A-shares (8 stocks): 中芯国际/寒武纪/中微公司/兆易创新/沐曦/摩尔线程/中际旭创/新易盛
- 中概股 (10 stocks): BABA/PDD/JD/BIDU/NTES/NIO/XPEV/LI/BILI/TME
- EV (5 stocks): Tesla/BYD/宁德时代/阳光电源/小米汽车
- AI热点: 云厂商涨价潮/华为Atlas 950/阶跃星辰AI手机/Amazon Moonraker/Q2财报验证窗口
- Key themes: 半导体定价权向上游转移; Mag 7估值压缩→配置窗口; 中国AI资产全球重估(配比仅1.2%); AI算力进入供需定价阶段
- Updated: wiki/index.md, wiki/log.md

## [2026-07-10] synthesis | Conference & arXiv Digest — 2026-07-10
- New page: wiki/synthesis/2026-07-10/conference-digest.md
- Coverage: 18 sections across 12+ venues — ICML 2026 Best (Flexibility Trap), CVPR 2026 Best (D4RT), NeurIPS 2025 Best (Gated Attention, Artificial Hivemind), AAAI 2026, ICLR 2026, KDD 2026 (OneMall/FAT), WWW 2026 (ThinkRec), ACL 2026, SIGIR 2026, EMNLP 2025, CIKM 2025, RecSys 2025
- Key papers: Flexibility Trap (dLLMs), D4RT (4D reconstruction), Gated Attention (Qwen), OneMall (Kuaishou 400M DAU), DS-MLP (CTR), FAT (Taobao deployed), CSRO (DeepMind game agents), ProAct (game lookahead), NitroGen (NVIDIA 40K hrs), CARD (diffusion LM), Metacognitive Harness
- Labs: Google DeepMind, Alibaba Qwen, Kuaishou, ByteDance, Meituan, Tencent, NVIDIA, Meta, Microsoft, Tsinghua
- Key themes: Diffusion LM maturing, RL+LLM limits exposed, Agent→Code paradigm, CTR scaling laws, 4D scene understanding
- Updated: wiki/index.md, wiki/log.md

## [2026-07-10] synthesis | arXiv Paper Check — AI & CTR (July 10, 2026)
- New page: wiki/synthesis/2026-07-10/arxiv-paper-check.md
- Coverage: 18 curated papers from cs.AI (56 new), cs.LG (93 new) — Friday July 10, 2026 listings
- CTR highlights: PIT-SUN (Kuaishou, parameter-efficient multi-domain CTR adapters), BACH (Alibaba, Bayesian anchor cold-start), COBART (bid-aware CTR integrating auction info)
- AI Agent highlights: Tool-Making Self-Evolving Agents (Amazon, 42% latency + 53% error reduction), HeaPA (hierarchical planning + GRPO)
- Safety highlights: Overthinking (ICML 2026, reasoning amplification surfaces secrets 10× more), CoT persuasion attacks (monitor access increases harm by 9.5%), Agreement ≠ Accuracy (ρ 0.20–0.59, frontier models 48% wrong when agreeing), Alignment Plausibility (healthcare regulatory construct)
- RL highlights: DRRO-RLHF (distributionally robust reward optimization), ReCoLoRA (continual fine-tuning via recursive consolidation), FMR (offline agent alignment, 98% misalignment reduction)
- Efficiency highlights: Jet-Long (bifocal RoPE, 1.39× FA2 throughput), Block-sparse uncertainty router (+28pp recall), AgentNAS (11/17 SOTA via LLM+NAS)
- Key themes: CTR diversifying (multi-domain adapters, auction-aware, cold-start anchors); Safety research maturing (3 papers challenge core assumptions); Production agent patterns crystallizing; RLHF robustness as new frontier
- Updated: wiki/index.md, wiki/log.md

## [2026-07-10] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-10)
- New page: wiki/synthesis/2026-07-10/wq101-alpha-daily.md
- Market: S&P ~7,560 (+11% YTD), Nasdaq +1.3% 半导体反弹, WTI $67 (-40% from $112 peak); 板块轮动确认 (Tech 广度37%/HC 63%/Fin 69% uptrend)
- Key theme: Alpha#19 均值回复 (9次, 45%) + Alpha#30 低波动 (7次, 35%) 主导; Alpha#1 动量集中于科技/AI
- Top 3: GOOGL (9/10, Alpha#1/#41), AMZN (9/10, Alpha#1/#6), AVGO (9/10, Alpha#1/#30)
- 板块分布: 半导体6只, 软件/安全3只, 医疗3只, 工业2只, 金融1只, 能源1只, 消费2只, 通信1只
- 关键变化 vs 07-09: Top 3 从防御(LLY/XOM/CVX)→Mega-cap科技(GOOGL/AMZN/AVGO); 科技从8→10只回升; 能源从3→1只; 均值回复维持主导
- Updated: wiki/index.md, wiki/log.md

## [2026-07-10] synthesis | arXiv AI Research Paper Search Report
- New page: wiki/synthesis/2026-07-10/arxiv-ai-search.md
- Coverage: 15 curated papers across 3 categories — CTR/Recommendation (8), LLM Reasoning (4), Game Theory/Multi-Agent (3)
- Key papers: LLaTTE (Meta, scaling laws for rec), GRAB (Baidu, generative CTR), EST (Alibaba, unified CTR scaling), IDProxy (Xiaohongshu, MLLM cold-start), GPR (Tencent, one-model ad rec), GenLI (generative long-term interest), Beyond Positive Signals (Tencent, mixed-polarity sequences), CTR-Sink (Ant Group, attention sink for CTR), Periodic Table of LLM Reasoning survey, LLM Reasoning Failures (Stanford/TMLR), Agentic Reasoning survey, MIPI (training-inference gap in RL), Strat-Reasoner (ICML 2026, strategic reasoning in games), Competitive Information Design, Multi-Agent RL for game strategies
- Key trends: Scaling laws arrive in rec sys; Generative paradigm shift in ad rec; MLLMs meet CTR cold-start; Sequence data reimagined (mixed-polarity, attention sinks); Strategic reasoning as RL frontier
- Updated: wiki/log.md

## [2026-07-09] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-09)
- New page: wiki/synthesis/2026-07-09/wq101-alpha-daily.md
- Market: S&P 7,495 (+9% YTD), Dow 52,422, Nasdaq 29,362; 美伊冲突升级原油+5%至$78; Fed 6月纪要偏鹰; IMF下调全球增长至3%
- Key theme: Alpha#19 Mean Reversion (8次) + Alpha#30 Low Vol (8次) 主导; 板块轮动科技→医疗/能源/金融/防御
- Top 3: LLY (9/10, Alpha#19/#30), XOM (8/10, Alpha#53/#6), CVX (8/10, Alpha#53/#12)
- 板块分布: 医疗4只(LLY/UNH/ABBV/JNJ), 能源3只(XOM/CVX/COP), 科技8只(INTC/MU/AVGO/GOOGL/AMD/MRVL/SNDK/NVDA), 金融2只(JPM/GS), 消费3只(AMZN/WMT/COST)
- 关键变化 vs 07-08: 主导因子从Alpha#1动量→Alpha#19/#30防御; 医疗从1→4只; 能源从2→3只; 最大变化为板块轮动确认; NVDA从Top 3掉至#20(6/10)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-09] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 9, 2026)
- New page: wiki/synthesis/2026-07-09/game-rl-daily.md
- Coverage: 50+ curated papers across 7 categories — Game RL (QZero, Generative Code Opt, DAGS, Think in Games), Game AI Bot (AVA, Odysseus, COSPLAY, Sensi, PokéChamp, PORTAL, MEMO, Nemobot, OpenGame, MineDreamer), Foundation Models (NitroGen NVIDIA, Game-TARS ByteDance, Pixels2Play, MARL-GPT, Generalist GP survey), PCG (PCGRLLM, IPCGRL, VIPCGRL, MOPCGRL, Agentic PCG), Benchmarks (OmniGameArena, lmgame-Bench, GameWorld, Orak, AI Gamestore, CivBench, PokéAgent, RevengeBench), Industry (GT Sophy 5-year, NVIDIA ACE, Ubisoft Teammates, GenAI NPC survey), Related Techniques (SPIRAL, MARSHAL, MATWM, Multiplayer World Models 5B, MultiWorld, SPA, ProPlay, Dreamer 4, GRACE IRL, iLLM, SENSEI, GLANCE, Inverse Game Theory)
- Key themes: Model-free Go at scale (QZero), VLM+RL for 100+ turn games (Odysseus), GPUs-as-game-foundation-models maturing (NitroGen 1000+ games), Agentic PCG as new sub-area, Industry deployment milestones (GT Sophy production, Ubisoft Teammates), Self-play + world models as dual paradigm continues
- Updated: wiki/index.md (synthesis entry added), wiki/log.md

## [2026-07-09] synthesis | LLM Tech Report Digest 2026 — 12家AI公司技术报告汇总
- New page: wiki/synthesis/2026-07-09/tech-report-digest.md
- Coverage: 12 AI orgs — DeepSeek (V4), OpenAI (o3/o4-mini), Meta (Llama 4), Google (Gemini 2.5), Anthropic (Claude Opus 4.7/Fable 5/Mythos 5), Mistral (3), Alibaba (Qwen3), Microsoft (Phi-4), xAI (Grok 4), NVIDIA (Nemotron 3), Apple (AFM 2025), Google (Gemma 4)
- Key themes: cross-cutting architecture analysis (MoE, hybrid Mamba-Attention, MLA), training methods (RL post-training, GRPO/RLVR), scaling law trends, multimodal capabilities, long context (1M+ standard), reasoning model landscape
- Key sections: Architecture table (12 models), Context length comparison (4 tiers), Cross-cutting themes (8 dimensions), 12 company entries with model cards
- Updated: wiki/index.md (synthesis entry added), wiki/log.md

## [2026-07-09] synthesis | arXiv Conference Digest — Comprehensive Multi-Venue Report (2026-07-09)
- **Updated page:** wiki/synthesis/2026-07-09/arxiv-daily.md (expanded from 15 to 44 curated papers)
- **Venues now covered:** ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025
- **New sections added:** Cross-Cutting Themes table, Summary Statistics table
- **LLM Architecture (10 papers):** Review Residuals (emergent at scale), Legible-by-Construction, Hybrid Seq (6× fewer params), Linearization (32B), Fractal KV (36–54×), DepthWeave-KV (8.3×), FourierQK (79% loss reduction), RoPE theory, GD beyond NTK, Algorithmic Foundations
- **LLM RL & Agents (10 papers):** Agon (2× GRPO), AdaPrefix-GRPO (2.1× GRPO), Compositional RL, SAO (GLM-5.2 750B), EPPO, LLM-as-a-Verifier (78.2% SWE-Bench), CPE, SPIRAL (10% gain 8 benchmarks), Agentic Transformers (proven DFS), MEMO (19× fewer games)
- **CTR Prediction (12 papers):** OneRanker (Tencent +1.34% GMV), GR4AD (Kuaishou +4.2% revenue), GRAB (Baidu +3.49% CTR), DS-MLP (TKDD SOTA), CADET (LinkedIn), IDProxy (XHS), SparseCTR (WWW +1.72% CTR), GenCI (WWW), DAIAN, RankUp (KDD), UniSID, LOOPCTR
- **Recommendation Systems (8 papers):** MMEACR, Agentic RS Roadmap, HGenPush (Kuaishou +0.181% DAU), R^3 ad compliance (ACL 2026), IntuRec, Meta Lattice (KDD), AgentX (3.7×), GenCI
- **Games & MARL (4 papers):** Multiplayer World Models (4-player 20fps), MARL-GPT, RAID (NHL26), SPIRAL
- **Updated:** wiki/index.md (synthesis entry expanded), wiki/log.md

## [2026-07-08] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-08)
- New page: wiki/synthesis/2026-07-08/wq101-alpha-daily.md
- Market: S&P 500 7,503 (-0.45%), Nasdaq 25,818 (-1.16%), Dow 52,925 (-0.25%), SOX 芯片板块回调, 伊朗局势升温油价反弹
- Key theme: Alpha#1 动量 (6次) + Alpha#41 趋势强度 (5次) 主导; 金融板块 5 只入选为最强板块
- Top 3: JPM (9.0, Alpha#41/#6, 52周新高+50B回购), META (8.8, Alpha#1/#12, 量价齐升), CRWD (8.7, Alpha#1/#30, AI安全YTD+76%)
- 板块分布: 金融 5只, 科技/安全 9只, 通信 2只, 能源 2只, 医疗 1只, 消费 1只
- 关键变化 vs 07-07: 主导因子从 Alpha#53 反转→Alpha#1 动量+Alpha#41趋势; 金融从 3→5 只; 网络安全动量为主; 能源超卖反转机会 CVX/XOM
- Updated: wiki/index.md, wiki/log.md

## [2026-07-08] synthesis | arxiv-paper-check — AI & CTR (July 8, 2026)
- New page: wiki/synthesis/2026-07-08/arxiv-paper-check.md
- Coverage: Scanned cs.AI (49 new), cs.LG (58 new), cs.IR (11 new) from Wednesday July 8, 2026 listings
- AI highlights: SearchEyes (multi-hop multimodal search), Memory-in-the-Loop (100us in-process retrieval), NapMem (memory as structured action space), Akashic/MemAttention (low-overhead LLM inference with chunked memory), CSTutorBench (SLM tutoring evaluation), Narrative World Model (narratology-grounded memory), TurnOPD (efficient on-policy distillation), PolyWorkBench (multilingual agents), StateFuse (conflict-preserving multi-agent memory), FirstResearch (auditable scientific question formation), ArtisanCAD (industrial CAD with expert knowledge distillation), Controlling Tool Use (activation steering)
- ML highlights: FourTune (W4A4G4 diffusion post-training, 2.25× memory reduction), λ-VAE (variance equalization for posterior collapse), Exogenous Dropout (robust time series), STS/SBS (stochastic token steering)
- IR highlights: PORTS (preference-optimized retrievers for tool selection), SCOReD (student-aware CoT for recommendation distillation), Signed MaxSim (theoretical capacity of late-interaction)
- CTR: No new CTR papers today; included recent highlights (DeRes, DS-MLP, LoopCTR, EST, GRAB)
- Key themes: Memory architectures dominate (4 papers), agent evaluation maturing, 4-bit training for diffusion
- Updated: wiki/index.md, wiki/log.md

## [2026-07-07] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-07)
- New page: wiki/synthesis/2026-07-07/investment-daily.md
- Coverage: US Mag 7 (AAPL +2.9%/MSFT -4.17%/NVDA -0.69%/TSLA +1.89%), AI 链 (AMD +9.2%/PLTR +2.51%/AVGO +5.1%), 港股科技 (腾讯 +4.82%/快手 +8%/美团 +4.68%), A 股 AI (寒武纪/中际旭创 -13.47% 4 天/华大九天 +14%/沐曦 +10%), 中概 ADR (BIDU -3.93%/BABA -1.89%), 新能源 (TSLA Optimus 量产线), AI 热点 (腾讯 Hy3 发布/美团 LongCat-2.0 开源/快手可灵 $3B 融资/昆仑芯 $50B 估值/"韬定律"国产芯片/DRAM 涨价)
- Key themes: Dow 53,055 新高; Great Rotation 2.0 持续 (科技→医疗/金融); 半导体超卖反弹; 恒生科技反弹 300 点; AI 模型国产化加速; "韬定律"重新定义 A 股芯片叙事; AI CapEx $700B 回报验证在即
- Updated: wiki/index.md, wiki/log.md

## [2026-07-08] synthesis | arxiv-ai-search — arXiv AI Research Scan July 2026
- New page: wiki/synthesis/2026-07-08/arxiv-ai-search.md
- Coverage: 40+ papers across 6 categories — LLM Training (LLM-as-a-Verifier, MiniMax MSA, CPE, TTT-NTP, TEMPO, Overthinking, T² Scaling), Advertising CTR (OneRanker, GR4AD, DAIAN, DS-MLP, GRAB, GenCI, RankUp, CADET, IDProxy), Sequential Rec (HPGR, CMSL, MVCrec, DiffSBR, MLTFR, Persona-KG, LLM Distillation), Time Series (UniTok-FM, TimeSqueeze, Time-TK, UniMamba, TimeFormer, CAPS), Games (Odysseus, SPIRAL, MARL-GPT, Stratagem), RL Agents (RAPO, T-STAR, Trainee-to-Trainer, Agentic Transformers Search)
- Key themes: verification as new scaling axis, generative recommendation industrial deployment, context pollution in rec systems, overthinking in test-time compute, time series foundation models via NTP, self-play for transferable reasoning
- Updated: wiki/index.md, wiki/log.md

## [2026-07-08] synthesis | arxiv-daily — arXiv Daily Digest 2026-07-08
- New page: wiki/synthesis/2026-07-08/arxiv-daily.md

## [2026-07-08] synthesis | game-rl-daily — Game RL & Game AI Bot Paper Digest (July 8, 2026)
- New page: wiki/synthesis/2026-07-08/game-rl-daily.md
- Coverage: 65+ curated papers across 10 categories — Game RL (QZero, Generals.io AI, RGSC, AlphaZero Tablut, SPIRAL, Stratagem, Generative Code Opt, GAE, GFXP), MARL (MARL-GPT AAAI/AAMAS 2026, SHPPO, HLSMAC, MARSHAL), Game AI Bot (Odysseus, AVA ACL 2026, Nemobot, Sensi, AdaMARP, Psy-CoT, Bounded Autonomy, LLM Testing), Foundation Models (NitroGen NVIDIA, Game-TARS, Pixels2Play, Lumine, GameVerse, OpenGame, Survey), World Models (Dreamer 4, NE-Dreamer, R2-Dreamer ICLR 2026, WAM, Dreamer-CDP, ARROW, OWM, ResDreamer, RAW-Dream, Matrix-Game 3.0/2.0), PCG (IPCGRL, VIPCGRL, Multiverse, PCGRLLM, CreativeGame, WFC+PCGRL, Word2Minecraft, HDPCG, Word2World, SLM for PCG, DRL Level Design), Benchmarks (OmniGameArena UE5, GameWorld, Orak KRAFTON, lmgame-Bench, AI Gamestore, V-MAGE ACL 2026, HLSMAC), Self-Play & Related (PopuLoRA, FMSP, SeRL, Reasonably Reasoning Agents, DEDA-FP NeurIPS 2025, Karma DPGs), Industry (KRAFTON ICML 2026, Sony GT Sophy, Microsoft WHAM, NC AI, AI Native Games survey), Orchestrated Worlds (Orchestrated Reality, MultiGen)
- Updated: wiki/index.md, wiki/log.md
- Coverage: 22 curated papers — LLMs (DepthWeave-KV, FreqDepthKV, World Models Roadmap, ProtoType LMs), CTR (DS-MLP TKDD, IDProxy XHS, CADET LinkedIn, GenLI), Rec (HGenPush, Agentic RS Roadmap, LBR, Temporal Gap Tokenization), Time Series (RMISC), RL & Games (SPIRAL ICLR 2026, FootsiesGym, Augmenting Game AI CoG 2026, Strat-Reasoner), Multi-Agent (StateFuse, Doomed Probe Cascade), IR (UniSGR, Off-Policy REINFORCE, SCOReD)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-07] synthesis | 大模型技术报告摘要 — LLM Tech Report Digest (22家机构全面覆盖)
- New page: wiki/synthesis/2026-07-07/tech-report-digest.md
- Coverage: 22 AI orgs — DeepSeek (V4 2606.19348), OpenAI (GPT-5/5.5/o1), Meta (Llama 4), Google (Gemini 2.5 2507.06261), Anthropic (Claude Opus 4.8/Mythos/Sonnet 5), Mistral (Ministral 3 2601.08584), Alibaba Qwen (Qwen3 2505.09388/Qwen3.5-Omni/Qwen3-Coder-Next 2603.00729/Qwen-VLA 2605.30280), 01.AI (Yi-Lightning 2412.01253), Baichuan (M3 2602.06570/M4 2606.08982/Omni-1.5 2501.15368), Microsoft (Phi-4-reasoning 2504.21318/Phi-4-reasoning-vision 2603.03975), Apple (AFM 2025 2507.13575), NVIDIA (Nemotron 3 Super 2604.12374/Ultra), xAI (Grok 4/4.1/4.20), Amazon (Nova 2506.12103), Zhipu AI (GLM-5 2602.15763), Shanghai AI Lab (Intern-S1-Pro 2603.25040), Moonshot AI (Kimi K2 2507.20534/K2.5 2602.02276), StepFun (Step 3.5 Flash 2602.10604/STEP3-VL 2601.09668), ByteDance Seed (Seed 2.0 2607.00248/Seed 1.8 2603.20633)
- Key themes: MoE普及化; 混合架构（Mamba-Transformer, CSA+HCA）; 百万Token上下文标配; 推理/思考模式成为基本功能; Agent原生化; 多模态融合加速; 开源开放科学
- Updated: wiki/index.md, wiki/log.md

## [2026-07-07] synthesis | 顶会论文专题报告 — Conference & arXiv Digest (全面更新版)
- New page: wiki/synthesis/2026-07-07/conference-digest.md
- Coverage: 12+ venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025), 80+ curated papers, 15+ labs (Google DeepMind, OpenAI, Meta AI, Microsoft, Anthropic, NVIDIA, ByteDance, Kuaishou, Alibaba, Tencent, Yandex, Amazon, Apple, MPI, NTU)
- Key content: Gated Attention & Artificial Hivemind (NeurIPS 2025 Best Papers), HyPER (ICML 2026), PAPL (ICLR 2026 Oral), MAMMA & WorldLens (CVPR 2026 Orals), DS-MLP (TKDD 2026, CTR SOTA), SPiKE (KDD 2026), SDLM (Sequential Diffusion LM), LatentMAS (latent-space multi-agent), AgentForge (SWE-Bench 40%), DGenCTR/ContRec/OneRec (Generative Rec), ULTRA-HSTU (Meta), CLSR (symbolic agent communication)
- 7 sections: LLM Architecture & Reasoning, Agent Systems, CTR & RecSys, Generative Rec & Diffusion, Computer Vision, NLP & IR, RL & Games
- Updated: wiki/index.md, wiki/log.md

## [2026-07-07] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-07)
- New page: wiki/synthesis/2026-07-07/wq101-alpha-daily.md
- Market: Dow 53,055 历史新高; S&P 7,537 (+0.72%); Nasdaq 26,121 (+1.12%); SOX +2.2% 半导体反弹
- Key theme: Alpha#53 反转因子主导（10次）— 动量回撤24%后超卖机会凸显
- Top 3: MRNA (9/10, CAR-T概念+33.5%), LLY (9/10, GLP-1趋势), MSFT (8/10, P/E 19x均值回复)
- 板块分布: 医疗4只, 软件/安全4只, 金融3只, 半导体3只, 工业2只, 通信2只, 消费电子1只, 防御1只
- 关键变化 vs 07-06: 主导因子从 Alpha#30低波动→Alpha#53反转；医疗从3→4只(MRNA新高); 新增PLTR/MSFT/CRWD软件标的
- Updated: wiki/index.md, wiki/log.md

## [2026-07-07] synthesis | arXiv Paper Check — AI & CTR (July 7, 2026)
- New page: wiki/synthesis/2026-07-07/arxiv-paper-check.md
- Coverage: Scanned cs.AI (228 new), cs.LG (181 new), cs.IR (12 new) from Friday July 3, 2026 — the most recent arXiv batch
- AI Safety highlights: How to Avoid Debate (single-prover interactive proofs, ICML 2026), Online Safety Monitoring, Fast Multi-dimensional Refusal Subspaces, Steerability via Constraints
- Knowledge Distillation highlights: Teacher Supervision over Representation Equivalence Classes (logit-only drives capability), Co-Adaptive Multi-Task LoRA (CoDA, label-free transfer-aware)
- Weight Space / Neuro-Symbolic highlights: WeightCLIP (dataset-aligned weight representations, ICML 2026), NDVM (native differentiable VM, 24× faster co-search), MentalThink (SVG-based visual reasoning)
- Agent & Governance highlights: Safety Testing LLM Agents at Scale, CAGE-1 (Control/Assurance/Governance Evaluation), AGL-1 (Enterprise AI Governance Layer), PACE (Agentic Capability Proxy), AgenticSTS, DRIFTLENS, Atomic Task Graph
- Architecture highlights: Expander SAEs (parameter-efficient dictionaries), BayesLoRA (sparse Bayesian LoRA), A Hippocampus for Linear Attention, Spec-AUF, G-RRM
- Diffusion highlights: MoG-guided BBDM schedule design, ART Continuous-Time Control, Subliminal Clocks, Distribution-wise Rewards (ICML 2026)
- Time Series / Graphs highlights: Zeus (tuning-free TS foundation model, ICML 2026), Self-Gating Attention, NetinfoGC (training-free graph classification)
- IR/CTR highlights: Relevance-Based Embeddings (approximate any similarity), Agentic Search for EO, Chunking for RAG evaluation
- Key themes: Single-prover AI verification emerging; weight-space learning as new paradigm; enterprise AI governance formalizing; multi-task co-adaptation without labels; Adam convergence limitations; diffusion theory maturing
- Updated: wiki/index.md, wiki/log.md

## [2026-07-06] synthesis | 大模型技术报告综合摘要 — 全面更新版 (22家机构, 40+报告)
- New page: wiki/synthesis/2026-07-06/tech-report-digest.md
- Coverage: 22 AI orgs: DeepSeek (V4/V3.2), OpenAI (GPT-5.6/GPT-5/GPT-5.5), Meta (Llama 4), Google (Gemini 3 Pro/3.1 Pro), Anthropic (Claude Fable 5/Mythos 5/Opus 4.8/Sonnet 5), Mistral (Large 3/Ministral 3), Alibaba Qwen (Qwen3/Qwen3.5-Omni/Qwen3-Max), 01.AI (Yi-Lightning/Yi-34B/Yi-Coder), Baichuan (Omni-1.5/M3/M4), Microsoft (Phi-4/reasoning/reasoning-vision), Apple (AFM 2025), NVIDIA (Nemotron 3 Nano/Super/Ultra/Omni), xAI (Grok 4.1/4.20), Amazon (Nova 2), Zhipu AI (GLM-5/GLM-4.5V), Shanghai AI Lab (InternLM3/Intern-S1-Pro), Moonshot AI (Kimi K2/K2.5/K2.6), StepFun (Step 3/3.5 Flash), ByteDance Seed (Seed2.0/2.1)
- Key content: 6 cross-cutting analyses (MoE/hybrid architectures, training methods, scaling law, multimodal, long-context, reasoning models); 8 key trends summary
- Updated: wiki/index.md, wiki/log.md

## [2026-07-06] synthesis | 顶会论文专题报告 — Conference & arXiv Digest (全面版)
- New page: wiki/synthesis/2026-07-06/conference-digest.md
- Coverage: 12+ venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025), 80+ curated papers, 15+ labs (Google DeepMind, OpenAI, Meta AI, Microsoft, Anthropic, NVIDIA, Alibaba, ByteDance, Tencent, Kuaishou, Baidu, Zhipu AI, Mistral, Amazon, Apple)
- Key content: Gated Attention (NeurIPS 2025 Best Paper), HyPER & TEAM (ICML 2026), FastDriveVLA (AAAI 2026), D4RT (CVPR 2026 Best Paper), Total Recall QA (SIGIR 2026), DS-MLP & HyFormer (CTR), CADET (LinkedIn), RankUp (Tencent KDD 2026), Meta Lattice (Meta KDD 2026), SDLM (Sequential Diffusion LM), Nemotron 3, Mamba-3, agent systems (59 ICML/82 ACL/162 ICLR), CTR scaling laws, generative recommendation, game AI (NitroGen, SPIRAL), 10 key trends summary, company research focus map
- Updated: wiki/index.md, wiki/log.md

## [2026-07-06] synthesis | arXiv Paper Check — AI & CTR (July 6, 2026)
- New page: wiki/synthesis/2026-07-06/arxiv-paper-check.md

## [2026-07-06] synthesis | 投资日报 2026-07-06
- New page: wiki/synthesis/2026-07-06/investment-daily.md
- Coverage: 美股 Mag 7 / AI 链（NVDA, MSFT, GOOGL, AMZN, AVGO, AMD 等）、港股科技（腾讯/阿里/美团/小米/智谱/MiniMax）、A 股 AI 算力与应用（寒武纪/工业富联/中际旭创/新易盛/天孚通信）、中概 ADR（BABA/PDD/JD/BIDU/NIO/LI/XPEV）、新能源车（TSLA/比亚迪/蔚小理/宁德时代）、AI 热点主题（云 CapEx 军备竞赛 $670B、新模型发布潮、机器人/具身智能、SpaxeX-Google $30B 算力大单）
- Updated: wiki/index.md, wiki/log.md
## [2026-07-06] synthesis | WQ101 Alpha Daily — 美股 Top 20
- New page: wiki/synthesis/2026-07-06/wq101-alpha-daily.md
- Market: S&P 500 7,483.24 (+1.76%); Dow 52,900 历史新高; SOX -6.7% 半导体暴跌
- Key theme: Great Rotation 2.0 确认 — XLV新进Leading象限, XLK跌入Lagging
- Top 3: JNJ (9/10), MRK (9/10), LLY (9/10) — 医疗板块首次包揽前三
- 核心因子变化: Alpha#30低波动(13次)超越Alpha#1动量(11次)成为主导因子
- 7/14起Q2财报季前瞻: JPM/GS/WFC先发
- Updated: wiki/index.md, wiki/log.md

- Coverage: Scanned cs.AI (353 new submissions) + cs.IR (23 new) from Friday July 3, 2026 listings
- LLM highlights: PMD (procedural memory distillation, +3.8-13.6% over SDPO), DemoPSD (GRPO alternative), SOLiD scaling trends, Staleness-LR scaling laws for async RLHF, Scaling with Confidence (adaptive test-time scaling), ReContext (long-context reasoning), LACUNA (unlearning localization testbed)
- Agent highlights: RLVR for tool-use agents (Atlassian), Clinical RL in FHIR, Multi-agent debate social structure (3%→40% divergence), PAW (0.6B→32B matching), Distributed attacks in persistent AI control
- Rec/CTR highlights: CoPersona (collaborative persona graphs), IntentTune (e-commerce query resolution), Bi-NAS (NAS for RecSys explanations), Monosemanticity in RecSys, GR2 technical report, Planning over MF-MDPs for candidate gen
- Architecture highlights: Wiola (novel SLM architecture), Discrete Diffusion LMs for radiology, OrbitQuant (W2A4 DiT quantization)
- Key themes: Procedural memory as training paradigm; on-policy self-distillation maturing; agent safety in persistent codebases; fuzzy function compilation (PAW); reasoning effort > tool access
- Updated: wiki/index.md, wiki/log.md

## [2026-07-05] synthesis | arXiv Daily Report — AI, LLMs, CTR, Recommendation, RL, Games, Sequential Modeling
- New page: wiki/synthesis/2026-07-05/arxiv-daily.md
- Coverage: 21 curated papers across 6 domains (LLM Reasoning & Architecture (4), LLM Agents & Self-Evolution (4), Recommendation Systems (4), CTR Prediction & Advertising (4), Sequential Modeling (2), Reinforcement Learning & Games (3))
- LLM highlights: ReRec (RFT for recommendation reasoning, ACL 2026), Understanding LLMs survey, Physics Literacy diagnostic (Claude Opus 4.7/GPT-5.5/Gemini 3.1 Pro — 6/15 PASS), Research Ideas Gap (Yale, LLM ideas narrower than human)
- LLM Agents highlights: Next-Gen Agentic RL Systems (Ant Group/HKUST/Tsinghua, AReaL2.0), SPIRAL (ICLR 2026, self-play zero-sum games improve reasoning 10%), RWML (world model learning for LLM agents, matches expert-data), ReContext (recursive evidence replay)
- Rec/CTR highlights: CADET (LinkedIn, decoder-only ads CTR, +11.04%), FAT (Alibaba, Field-Aware Transformer, +4.38% AUC, KDD 2026), IDProxy (Xiaohongshu, MLLM cold-start), POEM (Kuaishou, partial-order sequential modeling), Self-Evolving Rec (YouTube/Gemini)
- RL/Games highlights: CART (adversarially robust Decision Transformer), SlimDT (RTG-free DT, 1/3 shorter sequences), Transformer-Enhanced RL survey, Game AI with DRL (CoG 2026)
- Key themes: LLM+Rec convergence accelerating; Transformers for CTR graduating to production (LinkedIn, Alibaba, Kuaishou); self-play/self-evolution for LLMs hot; scaling law thinking spreading to recommendation
- Updated: wiki/index.md

## [2026-07-04] synthesis | arXiv Daily Report — AI, LLMs, CTR, Recommendation, RL, Games, Sequential Modeling
- New page: wiki/synthesis/2026-07-04/arxiv-daily.md
- Coverage: 17 curated papers across LLM alignment/reasoning (6), generative recommendation/CTR (4), RL/games (5), sequential modeling/SSM (1), multi-agent/game theory (2)
- LLM highlights: DRIFTLENS (memory-induced reasoning drift), HOLA (hippocampal linear attention + exact cache), Reasoning Alignment audit (alignment regression in reasoning models), Reasoning Structure (graph-based efficiency metric), Constructive Alignment (dynamic preference control), Understanding LLMs survey
- Rec/CTR highlights: PauseRec (implicit reasoning for GenRec, SID-free), DS-MLP (dual-stream MLP knowledge distillation), LLaCTR (field-level LLM enhancement, 10-100x cheaper), IDProxy (cold-start CTR proxy)
- RL/Games highlights: IRumAI (first RL for Indian Rummy, 7000x faster), MTG-Causal-RL (causal RL benchmark), SlimDT (RTG-free Decision Transformer), MARLIN (sustainable LLM inference MARL), CART (adversarially robust DT)
- Key themes: Alignment drift from reasoning conversion, hippocampal memory for linear attention, implicit > explicit reasoning for GR, pure MLP distillation for CTR, RL expanding to underserved games, MARL for sustainability
- Updated: wiki/index.md

## [2026-07-05] synthesis | arXiv AI Research Search — July 5, 2026
- New page: wiki/synthesis/2026-07-05/arxiv-ai-search.md
- Coverage: 17 papers across 5 categories — LLMs, Recommendation, CTR & Advertising, Sequential Modeling, Game AI
- LLM highlights: Understanding LLMs survey, LLM Reasoning Failures (TMLR 2026 Survey), Agentic Reasoning survey, Single-Layer RL post-training (2607.01232), SPIRAL (ICLR 2026, self-play for reasoning)
- RecSys highlights: RecPilot (deep research paradigm), Self-Evolving RecSys at YouTube (Gemini agents), Trustworthy Recommendation in LLM Era survey, Meta Lattice (KDD 2026, model space redesign)
- CTR & Advertising highlights: CADET (LinkedIn, decoder-only transformer CTR, +11.04% lift), LoopCTR (loop scaling, Alibaba), DS-MLP (dual-stream MLP distillation, TKDD 2026)
- Sequential Modeling highlights: Mamba-3 (ICLR 2026, complex-valued state + MIMO), Continuity Laws for Sequential Models, Mechanistic Evaluation of Transformers & SSMs (Stanford)
- Game AI highlights: Augmenting Game AI with Deep RL (Conference on Games 2026)
- Key themes: Decoder-only entering CTR domain, scaling without parameter growth, LLM agents as autonomous ML engineers, mechanistic understanding beyond accuracy, simplicity+distillation beats complexity
- Updated: wiki/index.md

## [2026-07-04] synthesis | arXiv Paper Check — AI & CTR (July 4, 2026)
- New page: wiki/synthesis/2026-07-04/arxiv-paper-check.md
- Coverage: 20 curated papers from cs.AI (30 sampled, submissions from July 2, 2026) and cs.IR (30 sampled, submissions from July 1-2) — July 4, 2026 listing
- AI highlights: Distributed Attacks in Persistent-State AI Control (2607.02514, Iterative VibeCoding, 93%→47% evasion with ensemble), PAW (2607.02512, 0.6B fuzzy function compiler matches 32B prompting, 50× less memory), ReContext (2607.02509, recursive evidence replay for 128K-context reasoning), DemoPSD (2607.02502, disagreement-modulated self-distillation beats GRPO), TAP (2607.02466, ICML 2026, VLA task-agnostic pretraining, matches 1M+ demos), TestEvo-Bench (2607.02469, 746+509 test-code co-evolution tasks), Reasoning effort > tool access (2607.02436, 89% first-try with xHigh effort), OrbitQuant (2607.02461, W2A4 DiT quantization), Multi-agent OTR divergence (2607.02507, 3%→40% public-private gap), WorldSample (2607.02431, real-robot RL +28% success, -59% steps), EvoPolicyGym (2607.02440, GPT-5.5 best at autonomous policy evolution), LACUNA (2607.02513, parameter-level unlearning testbed)
- IR/CTR highlights: CoPersona (KDD '26, collaborative persona graphs for LLM personalization), IntentTune (e-commerce query disambiguation, user-specific > population signals), Bi-NAS (bi-level NAS + LLM zero-shot for RecSys explanations), Hard Negative Sampling via LLM Clustering (two-tower retrieval, breaks feedback loops), PaperPilot (DAG-based scientific literature search, Hit@5 58→77), PlanRAG (SIGMOD 2027, logical query trees for exploratory reasoning), Spotify Behavior-Grounded Judge (91% improvement on disagreement cases), MemSyco-Bench (memory-induced sycophancy benchmark)
- Key themes: Agent safety in persistent codebases, fuzzy function compilation for edge deployment, on-policy self-distillation advances, reasoning effort as dominant reliability factor, collaborative personalization for sparse user profiles, search evaluation grounded in behavioral data, agentic search workflows as DAGs
- Updated: wiki/index.md, wiki/log.md

## [2026-07-04] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-04)
- New page: wiki/synthesis/2026-07-04/wq101-alpha-daily.md
- Market context: Dow 52,900 历史新高 (+1.97% 周); S&P +1.75%; Nasdaq +0.72%; SOX -5.44% 连续 2 日暴跌; 非农弱→7月加息概率<20%; WTI $68.43 (-2%, 连续 4 周下跌)
- Core theme: **医疗板块 (XLV) 新进 Leading + 科技 (XLK) 滑入 Lagging** — Great Rotation 2.0 确认
- Top picks: AAPL (9/10, Alpha#1/#6, iPhone 涨价+$4.53T), ABBV (9/10, Alpha#1/#6, Q2 $15B), LLY (9/10, Alpha#41/#1, GLP-1), MU (9/10, Alpha#53/#19, 2日-17% 极端超卖)
- 板块分布: 医疗 4只, 金融 6只, 半导体 3只, 技术 2只, 必需消费 2只, 消费周期 2只, 工业 1只, 通信 1只
- 关键变化 vs 07-02: 最大变化为重大板块轮动确认 (科技→医疗+金融+防御); 半导体从 7→3 只; 能源出局; 新增 10 只 (ABBV/LLY/MRNA/GS/JPM/BRK.B/V/MA/WMT/PG)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-04] synthesis | Game RL & Game AI Bot — Daily Survey (2026-07-04)
- New page: wiki/synthesis/2026-07-04/game-rl-daily.md
- Coverage: ~40 papers across 7 categories (Game RL, Game AI Bot, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, Related Techniques)
- Key papers: QZero (NetEase, model-free Go via self-play), MARL in Video Games survey (Li et al.), DAGS (DeepMind, data-augmented self-play), NitroGen (CVPR 2026 NVIDIA, 1000+ game foundation model), Game-TARS (ByteDance, 500B+ token generalist agent), DreamerV3 (DeepMind, world model Minecraft diamond), Looped World Models (DeepMind), GameNGen (ICLR 2025, neural game engine), PCGRLLM (NYU/GIST, LLM reward for PCG), IPCGRL (CoG 2025, instruction PCG), DSGBench, TowerMind (AAAI 2026 Oral), Orak (KRAFTON, 12-game MCP benchmark), OmniGameArena (HKU/LIGHTSPEED, UE5 Solo/PvP/Coop), GameDevBench (CMU), CDE (ICLR 2026, curiosity for LLM RL), SPEAR (self-imitation for agentic RL), CuES (Alibaba, curiosity-driven task generation), NVIDIA ACE (production autonomous NPCs in PUBG/Total War/inZOI)
- Key themes: Generalist game foundation models (NVIDIA/ByteDance/DeepMind); self-play + world models as dual paradigm; LLM-NPCs entering production (NVIDIA ACE 2026); benchmark standardization (Oarak/OmniGameArena/TowerMind); curiosity-driven exploration for LLM reasoning (CDE/CuES); PCG with LLMs maturing (PCGRLLM/IPCGRL); MARL surveys consolidating field; neural game engines (GameNGen)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-04] synthesis | LLM Tech Report Digest — 2026-07-04 综合版（20 家机构全面覆盖）
- New page: wiki/synthesis/2026-07-04/tech-report-digest.md
- Coverage: 20 AI labs/companies — DeepSeek (V3/R1/V3.2), OpenAI (GPT-5/o3/o4-mini), Meta (Llama 4 Scout/Maverick), Google (Gemini 2.5 Pro/Flash), Anthropic (Claude Opus 4/Sonnet 4), Mistral (Large 3/Ministral 3), Alibaba (Qwen3 series), 01.AI (Yi-Lightning), Baichuan (Baichuan 4), Microsoft (Phi-4 series), Apple (AFM), NVIDIA (Nemotron 3 Nano/Super/Ultra), xAI (Grok 3), Amazon (Nova family), Zhipu AI (GLM-5), InternLM (InternLM3), Moonshot AI (Kimi K2/K2.5), ByteDance (Seed2.0/Seed1.5-VL), StepFun (Step-2)
- Key themes: MoE domination (flagship models), Hybrid Mamba-Attention (Nemotron 3), DSA sparse attention (DeepSeek V3.2 → GLM-5), MLA (DeepSeek → Kimi), RL post-training scaling (V3.2 10%+ compute), Hybrid reasoning (Qwen3/Gemini/Claude), 1M+ context (Llama 4 Scout 10M, Gemini/Nemotron/Amazon Nova 1M)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-03] synthesis | Game RL & Game AI Bot — Daily Survey (2026-07-03)
- New page: wiki/synthesis/2026-07-03/game-rl-daily.md
- Coverage: ~40 papers across 7 categories (Game RL, Game AI Bot, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, Related Techniques)
- Key papers: SPIRAL (ICLR 2026, self-play reasoning), NitroGen (CVPR 2026 NVIDIA, 1000+ game foundation model), Game-TARS (ByteDance, 500B+ token generalist agent), Towards Generalist Game Players (Tsinghua survey), Orak (KRAFTON ICLR 2026, 12-game MCP benchmark), AI GameStore (MIT/Harvard, LLM-synthesized game eval), GameWorld (NUS verifiable benchmark), PCGRLLM (NYU, LLM-driven reward for PCG), IPCGRL (instruction-conditioned PCG RL), GAMEBoT (ACL 2025, transparent LLM game reasoning), Game Theory Meets LLMs (IJCAI 2025 survey), Decrypto (Facebook Research, ToM benchmark), cMarlTest (ICSTW 2025, curiosity-driven multi-agent 3D game testing), SUR-RL Survey (ACM CS 2026), Game-RL (game video for VLM reasoning), MARSHAL (ICLR 2026 multi-agent self-play), JOWA (offline MBRL on Atari, 78.9% human-level), NVIDIA ACE
- Key themes: Self-play + RL as LLM reasoning paradigm; generalist game foundation models (NVIDIA/ByteDance/Tsinghua); game benchmarks standardizing (Orak/AI GameStore/GameWorld/Decrypto); PCG with LLMs maturing (PCGRLLM/IPCGRL); game theory + LLMs intersection (GAMEBoT/IJCAI survey); industry deployment accelerating (NVIDIA, ByteDance, KRAFTON); MARL surveys consolidating field; world models for games (JOWA)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-04] synthesis | Investment Daily — 2026-07-04（美股/港股/A股/中概/新能源与AI热点）
- New page: wiki/synthesis/2026-07-04/investment-daily.md
- Coverage: US (Meta Compute cloud +8.8%, semi selloff SOX -6.3%, AAPL +4.84%, Palantir +7.77% NVDA tie-up); HK (Tencent WeChat AI agent, Alibaba +6.5% AI trade, 智谱/MiniMax IPO, H-share downgrade by GS, HK$255B lockup expiry); A-share (AI concept rally/profit-taking rotation, 磷化铟 new material surge, InP concept <10 stocks, 寒武纪/海光/中科曙光, 科大讯飞 "标王" 蝉联, 澜起科技 1158机构调研); China ADR (BIDU +14.97% Kunlun Chip spinoff, PDD +6.97%, NTES +7%, HSAI +15%); EV (BYD global sales leader 2.26M units 2025, TSLA Q2 delivery ahead, XPEV +3.44%, Waymo $16B funding); AI hot topics (AI capex $1T data center 2026, DeepSeek V4/Kimi K2.6/GLM-4.7 advances, Chinese open-source AI 41-58% global downloads, Meta Compute cloud, OpenAI S-1 IPO filing, Neuralink mass production 2026, SpaceX Nasdaq-100 July 7)
- Key themes: Semi selloff oversold opportunity; Meta Compute marks AI capex monetization pivot; China AI model ecosystem global leadership; A-share AI rotation hardware→application; China ADR decoupling from US tech weakness
- Updated: wiki/index.md, wiki/log.md

## [2026-07-03] synthesis | Investment Daily — 2026-07-03（美股/港股/A股/中概/新能源与AI热点）
- New page: wiki/synthesis/2026-07-03/investment-daily.md
- Coverage: US Mag 7 (Meta +8.8% cloud spin-off rumor, AAPL +2.83%, chip sell-off SOX -6.3%), HK tech (HSI +1.6%, southbound net inflow 40B HKD), A-share (SSE -0.9%, STAR -3.99% chip profit-taking, gold stocks surging), China ADR (HSAI +15%, CSIQ +8.5%, XPEV +3.44%), EV (BYD HK leader, Waymo $16B funding, TSLA FSD V13), AI hot topics (马斯克每月新大模型, AWS GPU涨价, Stargate数据中心, Waymo/FSD自动驾驶, 机器人Optimus量产, 韩国半导体出口+200% YoY)
- Key themes: Semi selloff panic creates oversold opportunity; STARGate/Colossus 2 GW-scale DC buildout; AI capex debate intensifies ($830B 2026); A-share AI rotation from hardware to application
- Updated: wiki/index.md, wiki/log.md

## [2026-07-03] synthesis | Conference Digest — Comprehensive Roundup (ICML/AAAI/NeurIPS/ICLR/CVPR/KDD/ACL/EMNLP/SIGIR/WWW/CIKM/RecSys 2025–2026)
- New page: wiki/synthesis/2026-07-03/conference-digest.md
- Coverage: 12+ venues (AAAI 2026, ICLR 2026, CVPR 2026, ICML 2026, KDD 2026, ACL 2026, EMNLP 2025, NeurIPS 2025, SIGIR 2026, CIKM 2025, RecSys 2025, WWW 2026), 80+ curated papers, 15+ labs (Google DeepMind, OpenAI, Meta AI, Microsoft, Anthropic, NVIDIA, Alibaba, ByteDance, Tencent, Kuaishou, Baidu, Zhipu AI, Mistral, Amazon, Apple)
- Award papers detailed: NeurIPS 2025 Best (Gated Attention, Hivemind, 1000 Layer RL, Diffusion Memorization), ICLR 2026 Outstanding (Succinct Transformers, Multi-Turn Drop, ∇-Reasoner), CVPR 2026 Best (D4RT), EMNLP 2025 Best (Infini-gram mini), AAAI 2026 Outstanding (COREA, ProCo, GenMatLab)
- Key sections: Hybrid architectures (Nemotron 3/Mamba-3/Gated DeltaNet-2/Qwen3.6), Agent systems (Intelligent AI Delegation, Scaling Agent Systems, ACE), CTR scaling laws & generative recommendation, DeepMind & Anthropic research portfolios, Reasoning & test-time compute, LLM post-training & alignment (RLVR limitations)
- Trends: Hybrid Mamba-Attention; test-time gradient descent; deflationary findings winning awards; agent formalization; generative CTR paradigm
- Updated: wiki/index.md, wiki/log.md

## [2026-07-03] synthesis | arXiv Paper Check — AI & CTR (July 3, 2026)
- New page: wiki/synthesis/2026-07-03/arxiv-paper-check.md
- Coverage: 14 curated papers from cs.AI (353 total, 86 new), cs.IR (23 total, 8 new), cs.LG (273 total, 101 new) — July 3, 2026 listings
- AI highlights: Epistemic Goggles (2607.01690, gradient editing for epistemic framing, 91% fictional detection), PMD (2607.01480, procedural memory distillation, +3.8-13.6%), C3RL+CAS (2607.01612, confidence calibration RL, 12.33× inference savings), SOLiD at 405B (2607.01567, deception 34%→14%), InfoDelphi (2607.01661, information asymmetry for multi-agent, 12-18% Brier), Auto-FL-Research (2607.01366, NVIDIA agentic FL algo search), PACE (2607.01306, neuro-symbolic counterfactuals), Agentic Garden of Forking Paths (2607.01507, m-value for analysis credibility)
- CTR/IR highlights: MixFormer (KDD 2026, ByteDance Douyin co-scaling dense+sequence), GR2 (generative reasoning re-ranker, +18.7% R@1), CoPersona (KDD '26, collaborative persona graphs), Bi-NAS (bi-level NAS for RecSys explanations), IntentTune (e-commerce query disambiguation), Planning over MF-MDPs (KDD 2026 WS, one-step planning for retrieval)
- Key themes: LLM self-improvement via procedural memory; confidence calibration as RL objective; collaborative personalization for sparse profiles; generative re-ranking with RL entering production; information asymmetry as key enabler for multi-agent reasoning; gradient editing for epistemic control
- Updated: wiki/index.md, wiki/log.md

## [2026-07-02] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-02)
- New page: wiki/synthesis/2026-07-02/wq101-alpha-daily.md
- Market context: S&P 500 ~7,499 (-0.22%), Nasdaq -1.54% (芯片恐慌 MU -10.6%, SNDK -10.6%, AMD -6.9%, INTC -9%, AMAT -10%); META +10% 云业务拆分领涨; NKE +5%, CRM +4.6%, MSFT +3%
- Core theme: Alpha#53 反转因子主导 (7只) — 7/1 芯片恐慌创造超卖机会; META 云分拆成为最强动量信号 (Alpha#1/#6, 10/10); 资金从半导体轮入 Mega-cap 科技
- Top picks: META (10/10, Alpha#1/#6), MU (9/10, Alpha#53/#19), SNDK (9/10, Alpha#53/#12)
- 板块分布: 半导体/AI 7只, 技术/软件/云 4只, 工业 3只, 能源 1只
- 关键变化 vs 07-01: 主导因子从 Alpha#1 动量→Alpha#53 反转; 能源从 4→1 只 (Hormuz 和谈); Mega-cap 科技从 1→5 只 (META/MSFT/AAPL/GOOGL/CRM)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-02] synthesis | Investment Daily — 2026-07-02
- New page: wiki/synthesis/2026-07-02/investment-daily.md
- Coverage: US Mag 7 (AAPL/NVDA/MSFT/GOOGL/AMZN/META/TSLA), HK tech (Tencent/Alibaba/Meituan/Xiaomi), A-share AI (chip/optical module/server), China ADR (BABA/PDD/JD/BIDU), EV (Tesla/BYD/NIO/LI/XPEV/ZK), AI hot topics (DeepSeek V4, OpenAI, AI Capex, compute rental, autonomous driving, robotics)
- Updated: wiki/index.md, wiki/log.md
- New pages: wiki/synthesis/2026-07-02/investment-daily.md

## [2026-07-02] synthesis | Conference Digest 2025–2026
- New page: wiki/synthesis/2026-07-02/conference-digest.md
- Coverage: 10+ venues — ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026 (Best Paper), KDD 2026, SIGIR 2026, EMNLP 2025, ACL 2026, RecSys 2025
- Industry labs: OpenAI (GPT-5.6, Unit Distance Problem), Google DeepMind (D4RT, Gemini Deep Think, Co-Scientist), Meta AI (ULTRA-HSTU), Anthropic (Claude Sonnet 5)
- Special topics: CTR/Recommendation Scaling (12 papers across KDD/SIGIR/arXiv), Agent Systems & Reasoning
- Key themes: Scaling laws everywhere, test-time compute, agent safety, diffusion LMs, CTR+LLM convergence, multimodal unity
- Updated: wiki/index.md, wiki/log.md

## [2026-07-02] synthesis | arXiv Paper Check — AI & CTR
- New page: wiki/synthesis/2026-07-02/arxiv-paper-check.md
- Coverage: 10 curated papers from cs.AI / cs.IR / cs.LG new submissions (July 1, 2026)
- AI highlights: Single-layer RL training (2607.01232, middle layers carry all gains), AutoMem memory as trainable skill (2607.01224, 2-4x improvement), Theoria structured verification (2607.01223, 91.4% precision), State-Prediction Separation (2607.01218, 2-3pp gains), Adversarial RLVR (2607.01181, eliminates reward hacking), QuasiMoTTo QMC sampling (2607.01179, 25-47% fewer samples), Human vs LLM research ideas gap (2607.01233)
- CTR/IR highlights: Diffusion-GR2 block-diffusion re-ranker (2607.01170, 2.4-3.5x speedup), DeRes dual-path residual CTR (2606.07980, 2x compute savings), Trie-based experiment plans for IR pipelines (2607.01162, 26% faster)
- Key themes: RL post-training layer efficiency, memory as separable skill, structured verification, diffusion for ranking, CTR residual bottlenecks
- Updated: wiki/index.md, wiki/log.md

## [2026-07-02] synthesis | LLM Tech Report Digest — 增量更新
- New page: wiki/synthesis/2026-07-02/tech-report-digest.md
- Coverage: OpenAI GPT-5.6 Preview (Sol/Terra/Luna, Jun 2026), Anthropic Claude Fable 5 & Mythos 5 详细版 (Jun 2026), xAI Grok 4.x (4/4.1 Fast/4.3), Google Gemini Ultra 2 & 3.1 Pro Preview, Kimi K2.5 Visual Agentic Intelligence
- News: US export ban on Fable 5/Mythos 5 lifted Jul 1; White House restricts GPT-5.6 preview; OpenAI Jalapeño ASIC chip
- Key themes: dual-release safety strategy (public/restricted), government AI pre-approval, sub-agent orchestration (ultra mode, Agent Swarm), custom AI chips
- Updated: wiki/index.md, wiki/log.md

## [2026-07-02] synthesis | arXiv AI Research Roundup
- New page: wiki/synthesis/2026-07-02/arxiv-ai-search.md
- Coverage: 36 papers across 5 categories — LLM Training & Optimizers (Spectra, Muown, LITE, MUD, Spectral Scaling Laws, HyperP, HTMuon, BSS), LLM-Based Recommendation (Logs-to-Language, Reasoning-to-Rank, Scaling Laws for Synthetic Data, R³-REC, STAR, IAM, SMTPO), Generative Recommendation & Semantic IDs (GenRec JD, Gryphon, CapsID, UniSID, DeepInterestGR, SIGMA AliExpress, SIDReasoner, LASAR), CTR Prediction (LAIN, CADET, IDProxy Xiaohongshu, FEDIN, DS-MLP, AgentX Kuaishou), Multi-Agent Systems/Games/RL (Odysseus, SPIRAL, Stratagem, Strat-Reasoner, T-STAR, Trainee2Trainer, LangMARL, Coalition Formation, MAFP, TRACER, MARO, Competition&Cooperation, Agentic Transformers)
- Key themes: Muon optimizer variants dominating LLM training research; Generative recommendation with Semantic IDs maturing across industry (JD, Kuaishou, Xiaohongshu, AliExpress, Kuaishou AgentX); Multi-agent RL and game self-play converging as reasoning training paradigms
- Updated: wiki/index.md, wiki/log.md

## [2026-07-02] synthesis | Game RL & Game AI Bot — Daily Survey
- New page: wiki/synthesis/2026-07-02/game-rl-daily.md
- Coverage: ~40 papers across 7 categories (Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Industry Game AI, Related Techniques)
- Key papers: SPIRAL (ICLR 2026), MARSHAL (ICLR 2026), π-Play, FMSP, OMAR, ArenaRL (Alibaba), GIFT, PokéChamp, Odyssesus (Princeton VLM+RL 100+ turns), NitroGen (CVPR 2026 NVIDIA), Game-TARS (ByteDance), P2P (Elefant), WorldCam, GeoWorld, WoVR, RWML, PCGRLLM, IPCGRL, VIPCGRL, OpenGame, GameDevBench, OmniGameArena (UE5), GameWorld (NUS), lmgame-Bench, Orak (ICLR 2026 KRAFTON), OmniPlay, GameCraft-Bench, LEGO (HPCA 2026), NVIDIA ACE, HeRoN, HiPER, CuES, IR³, GRACE
- Key themes: Self-play + RL as dominant LLM reasoning paradigm; generalist game foundation models; VLM+RL for long-horizon; game benchmarks standardizing; PCG with LLMs; industry deployment maturing; world models unifying games/robotics/agents
- Updated: wiki/index.md, wiki/log.md

## [2026-07-01] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-01)
- New page: wiki/synthesis/2026-07-01/wq101-alpha-daily.md
- Market context: S&P 500 ~7,491, Q2 6年最佳季度(+14%), 7月开局回调, 能源 YTD +31%领跑, 科技 XLK -2.9%, VIX ~16.6, WTI ~$69, Fed维持利率3.75%, 通胀4.2%
- Core theme: AI Infrastructure Buildout (MU/MRVL/CRDO/BE/VRT), Memory Supercycle (SNDK/MU), Energy Rally (XOM/OXY/COP/CVX), Tech Rotation → Industrial/Energy
- Top picks: MU (9/10, Alpha#1/#41), MRVL (9/10, Alpha#1/#6), SNDK (9/10, Alpha#1/#12), CRDO (9/10, Alpha#30/#1)
- 板块分布: 半导体8只, 能源4只, 工业4只, 技术/硬件2只, 医疗1只, 清洁能源1只
- 关键变化 vs 06-30: 板块大幅转向半导体动量(从6→8只), 能源维持4只, 新增清洁能源(BE), 减少防御性医疗/消费
- Updated: wiki/index.md, wiki/log.md

## [2026-07-01] synthesis | Game RL & Game AI Bot — Daily Survey
- New page: wiki/synthesis/2026-07-01/game-rl-daily.md
- Coverage: ~80 papers across 7 categories (Game RL, Game AI Bot, Foundation Models, PCG, Benchmarks, Industry, Related Techniques)
- Key papers: Stratagem (self-play reasoning transfer), OPR (Atari SOTA 10M), SPIRAL (self-play reasoning), MARL-GPT (multi-task MARL foundation model), SOL (scalable hierarchical NetHack), NitroGen (CVPR 2026 NVIDIA), Game-TARS (ByteDance), Odysseus (VLM+RL 100+ turns), AVA (ACL 2026 StarCraft II), OpenGame (GameCoder-27B), GameWorld (state-verifiable benchmark), OmniGameArena (UE5 benchmark), GameDevBench, AstraGame (Tencent FSE 2026), PUBG Ally (KRAFTON), Matrix-Game 3.0 (40FPS 720p world model)
- Updated: wiki/index.md

## [2026-07-01] synthesis | AI Tech Report Digest — 全面更新 (22 家机构)
- New page: wiki/synthesis/2026-07-01/tech-report-digest.md
- Coverage: 22 orgs, 40+ reports. DeepSeek (V4/V3.2/R1/V3), OpenAI (GPT-5/o3), Meta (Llama4), Google (Gemini 2.5), Anthropic (Claude 4/5 series), Mistral (Magistral/Large3/Ministral3), Qwen3, Yi-Lightning, Baichuan4-Finance, Microsoft (Phi-4/reasoning/vision), Apple (AFM 2025), NVIDIA (Nemotron 3), xAI (Grok 3), Amazon (Nova/Premier/2), Zhipu (GLM-5), InternLM (InternLM3/Intern-S1), Moonshot (Kimi K2/K1.5/K2.5), ByteDance (Seed 2.0/Thinking-v1.5), StepFun (Step 3.5 Flash/Step3-VL-10B)
- Key themes: MoE 成为主流架构、混合 Mamba-Attention (NVIDIA)、纯 RL 推理 (DeepSeek-R1/Magistral)、混合推理模式 (Qwen3/GPT-5/Claude 4)、长上下文 10M (Llama 4 Scout)、RL Scaling Law、数据效率 Scaling
- Updated: wiki/index.md

## [2026-07-01] synthesis | AI/ML Conference Digest — July 2026
- New page: wiki/synthesis/2026-07-01/conference-digest.md
- Coverage: Comprehensive digest of 10+ conferences (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, WWW 2026, RecSys 2025), frontier models from OpenAI/Google/Anthropic/Meta/Apple, CTR/RecSys from ByteDance/Alibaba/Tencent/Kuaishou, AI agents, CV, NLP, RL, scaling laws, safety, benchmarks
- Key themes: Conference review systems under unprecedented strain (ICML 23,918 submissions, AAAI 23,680), agent ecosystem protocols maturing (A2A, MCP, ACP), CTR scaling as established research area, safety as production infrastructure, Chinese AI ecosystem (ByteDance/TikTok, Alibaba, Tencent, Kuaishou) at forefront of RecSys research
- Updated: wiki/index.md

## [2026-07-01] synthesis | arXiv Paper Check — AI & CTR (July 1, 2026)
- New page: wiki/synthesis/2026-07-01/arxiv-paper-check.md
- Coverage: 12 curated papers from latest cs.AI (277 total, 74 new), cs.IR (28 total, 11 new), cs.LG (249 total, 95 new) — latest available submissions through Jun 26, plus late-breaking Jun 30 paper (Agents-A1)
- AI highlights: Agents-A1 (35B MoE matching 1T models via agent-horizon scaling, 2606.30616), AgentX (Kuaishou agent-driven RecSys iteration, 3.7× business value, 2606.26859), KARLA (KB-augmented LLM generation, 2606.26807), OPSD diversity cost (2606.26091), Tmax (9B terminal agent SOTA, 2606.23321), Reasoning Quality Emerges Early (91% token efficient, 2606.26797), Red Queen Gödel Machine (co-evolving evaluators, 2606.26294), Abstract Representational Geometry (hippocampal-like LLM representations, 2606.23345)
- CTR/Rec highlights: DeRes (dual-path residual, 2× compute savings for CTR, 2606.07980), AgentX (also CTR pick)
- Key themes: Agent-horizon scaling, self-evolving agent systems, hidden diversity costs of self-distillation, LLM–neuroscience convergence, CTR residual bottleneck, CoT safety erosion
- Updated: wiki/index.md, wiki/log.md

## [2026-07-01] synthesis | arXiv AI Search — July 2026
- New page: wiki/synthesis/2026-07-01/arxiv-ai-search.md
- Coverage: 70+ papers across 6 categories (Recommender Systems & LLMs for Rec, CTR & Advertising, LLM Alignment & RL, AI Agents & Games, Efficient Architectures & Attention, Multimodal Learning)
- Key papers: AgentX (Kuaishou), LLaTTE (Meta), CADET (LinkedIn), GRAB (Baidu), EST (Taobao), f-GRPO, DAR, GAC, MemoPilot, Strat-Reasoner, Odysseus, Gecko, SFA/FlashSFA, MiniMax MSA, Nexusformer, Lance, UniAR, Hydra-X, GenLIP, Penguin-VL
- Key themes: Scaling laws for recommendation and CTR, generative LLM-based Rec, RL alignment innovation (f-GRPO, DAR, GAC), VLM game agents, feature-level and multi-step sparse attention, unified multimodal models, agentic training frameworks
- Updated: wiki/index.md, wiki/log.md

## [2026-07-01] synthesis | arXiv Daily — July 1, 2026
- New page: wiki/synthesis/2026-07-01/arxiv-daily.md
- Coverage: 20 papers across 5 categories (LLM Agents & RL, CTR Prediction, Advertising Recommendation, Emerging AI Methods)
- Highlights: Odysseus (VLM RL 100+ turns), AMC (SMC for black-box agents, ICML 2026), SPPO (seq-level PPO, ACL 2026), GR4AD (Kuaishou generative ad rec, +4.2% revenue), GRAB (Baidu LLM-style CTR, +3.49% CTR), DS-MLP (TKDD), GenCI (WWW 2026), IDProxy (Xiaohongshu cold-start), RankUp (Tencent +4.81% GMV), OneRanker (Tencent), GraphPO, T-STAR, SeeUPO, CELEUS, MEMPROBE
- Updated: wiki/index.md, wiki/log.md

## [2026-06-30] synthesis | arXiv AI Research Roundup — June 30, 2026
- New page: wiki/synthesis/2026-06-30/arxiv-ai-search.md
- Coverage: 29 papers across 6 categories (LLMs & Reasoning, RecSys, CTR & Advertising, Sequential Modeling, RL & World Models, Graph Learning)
- Key themes: TACO (GRPO for tool agents), Speculative decoding theory, MCP server patterns, IID-Nav & POEM at Kuaishou, CMSL at Meta, DeGRe at Taobao KDD 2026, test-time compute scaling for CTR (UTTSI), AdaGRPO, DreamForge-World world models, model monotonicity in autobidding auctions
- Updated: wiki/index.md, wiki/log.md

## [2026-06-30] synthesis | arXiv Paper Check — AI & CTR (June 30, 2026)
- New page: wiki/synthesis/2026-06-30/arxiv-paper-check.md
- Coverage: 16 papers from cs.LG (232 total, 75 new) + cs.IR (17 total, 8 new) + cs.AI (277 total, 74 new) — weekend submissions consolidated into Mon Jun 29 listing
- AI highlights: R2LM (bifocal diffusion LMs, 2.4×–12.9× throughput), L2A (resource-adaptive LLM inference, 34% sparsity at 0.6% loss), COOPA (OR agents), PEBS (per-rater RLHF calibration, 8.58% RMSE reduction), RAC (delayed-reward RLHF), Textual Belief States + fGRPO (world models), KARLA (KB-augmented generation), SelfCompact, Prism Transformer, CFRG (diffusion noise schedule)
- CTR/Rec highlights: IntuRec (intuition-guided latent reasoning), GLAN (Kuaishou +0.158% DAU), NOVA (verification-aware RecSys evolution, 13× speedup), PermR (revenue reranking, +2% revenue/56M queries), Journal Rec (LLM semantic alignment)
- Key themes: Resource-adaptive inference, RLHF tooling (PEBS, RAC), agent-driven RecSys iteration, diffusion LMs with KV caching, world models via fGRPO
- Updated: wiki/index.md, wiki/log.md

## [2026-06-30] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-06-30)
- New page: wiki/synthesis/2026-06-30/wq101-alpha-daily.md
- Market context: S&P 500 7,408 (-1.24%), Q2 收官, 能源 YTD +31% 领跑, Nasdaq -5.1% 周跌, Brent $109, VIX 18.4, Fed 鹰派, Mag 7 六月蒸发 ~$2T
- Key picks: XOM (9.5/10, Alpha#41/#6), CVX (9/10, Alpha#1/#41), COP (8.5/10, Alpha#1/#6), LNG (8.5/10, Alpha#41/#30)
- Top factors: Alpha#1 (momentum, 11 stocks), Alpha#53 (reversal, 10 stocks), Alpha#19 (mean-reversion, 9 stocks)
- 板块分布: 能源 4只, 半导体/AI 6只, 医疗 3只, 消费防御 2只, 工业 2只, 金融 1只, 大型科技 2只
- 关键变化 vs 06-29: 能源板块从 1→4 只（油价 $109 驱动）, 新增 Mag 7 均值回复（MSFT/GOOGL/NVDA）, 医疗从 5→3 只
- Updated: wiki/index.md, wiki/log.md

## [2026-06-30] synthesis | arXiv Daily Scan — June 30, 2026
- New page: wiki/synthesis/2026-06-30/arxiv-daily.md
- Coverage: 45 papers across 5 categories (LLMs & Foundation Models, Reasoning & Inference, Sequence Modeling & Attention, CTR & Advertising Recommendation, Games & Reinforcement Learning)
- Key themes: Head-level attention hybridization (HydraHead), Polar attention (ATMA), MiniMax MSA production deployment, CTR gen-adv unification at Tencent/Baidu/Kuaishou, GraphPO DAG-structured RL, compositional generalization theory for SFT+RL, self-compacting agents
- Updated: wiki/index.md, wiki/log.md

## [2026-06-27] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-27)
- New page: wiki/synthesis/2026-06-27/investment-daily.md
- Coverage: 美股(Mag 7, 半导体/AI), 中概ADR(周五反弹, NTES+7.74%领涨, PDD+4.43%), 港股科技(智谱/MiniMax -8~11%大幅回调), A股(创业板-4.07%, 存储芯片+7.10%周涨幅逆势走强), 新能源/机器人, AI热点主题(SK Hynix $29B ADR获批, RAMageddon存储涨价全面传导, OpenAI IPO推迟至2027)
- Key events: SK Hynix 纳斯达克上市获批(7/10, $29B募资), Apple/Mac/iPad全线涨价~20%, Microsoft/Xbox涨价$150, 功率半导体密集涨价(立昂微/扬杰科技7月涨10-15%), 宇树机器人R1降至2.99万元(-58%), 恒生科技盘中跌超3%
- Updated: wiki/index.md, wiki/log.md

## [2026-06-27] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-06-27)
- New page: wiki/synthesis/2026-06-27/wq101-alpha-daily.md
- Market context: S&P 500 7,354 (-0.05%), -3.5% off ATH, Nasdaq -5.7% from peak, sector rotation tech→industrial/energy/healthcare/financials, VIX ~19, Fed hawkish signals, Warsh 10月加息概率上升
- Key picks: MU (10/10, Alpha#1/#30), MRVL (9.5/10, Alpha#1/#6), AMAT (9.5/10, Alpha#30/#41), SNDK (9.5/10, Alpha#1/#30)
- Top factors: Alpha#19 (mean-reversion, 9 stocks), Alpha#1 (momentum, 8 stocks), Alpha#41 (trend strength, 8 stocks), Alpha#53 (reversal, 6 stocks)
- Key theme: Great Rotation 2.0 — 半导体AI强者恒强 vs 防御/价值板块均值回复; Mega-Cap超卖机会积累
- Updated: wiki/index.md, wiki/log.md

## [2026-06-27] synthesis | arXiv AI Research Scan — June 2026
- New page: wiki/synthesis/2026-06-27/arxiv-ai-search.md
- Coverage: 36 papers across 6 domains (LLMs & Foundation Models, LLM Inference Efficiency, Sequence Modeling & Architecture, CTR Prediction, Recommendation, Games & RL)
- Top papers: Ling & Ring 2.6 (Ant Group 1T hybrid attention), SparDA (Forecast-based sparse attention), DeRes (dual-path residual, 2× compute savings for CTR), Keyless Attention (50% KV cache reduction), Odysseus (100+ turn VLM game-play), MARL-GPT (multi-task MARL foundation model), LLMZero (auto RL strategy discovery)
- Key themes: Hybrid SSM+Attention mainstream, KV cache reduction via architectural innovation, CTR scaling laws maturing, VLM+RL convergence for games, generative CTR/rec at scale
- Updated: wiki/index.md, wiki/log.md

## [2026-06-29] synthesis | Conference Digest — 顶会论文专题报告 2026年6月全面版
- New page: wiki/synthesis/2026-06-29/conference-digest.md
- Coverage: 12 venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, WWW 2026, SIGIR 2026, CIKM 2025, RecSys 2025), 100+ papers, 15+ labs
- Architecture highlights: Mamba-3 (Princeton/CMU), Gated DeltaNet-2 (NVIDIA), GPT-5.6 Sol (OpenAI), TabICLv2 (INRIA/ICML), LimiX-2M (ICML)
- CVPR 2026 Best: D4RT (Google DeepMind 4D reconstruction), O-Voxel (Microsoft/Tsinghua 3D generation)
- ICLR 2026 Outstanding: Transformers Succinctness, Multi-Turn LLM Eval, Polar Express
- CTR/Advertising: FAT (KDD, Alibaba +4.38% AUC), GRAB (Baidu +3.05% revenue), GR4AD (Kuaishou, +4.2% revenue deployed to 400M+ users), GenRec (JD, +9.5% clicks), OneLive/SARM/UniFormer (Kuaishou), SIF/UG-Sep (ByteDance), RankUp (Tencent, +3.41% GMV), SparseCTR (Meituan WWW), CTR-Sink (Ant KDD)
- Agents: GrandCode (first AI to beat all humans in Codeforces), OpenGame (game coding), MonoScale, HarnessBridge, Lacuna, LLM-as-Code, DeepPlanner, ForeAgent
- LLM Reasoning: Google DeepMind Efficient Exploration (10× RLHF data efficiency), Aletheia (solves open Erdős problems), ICL from Feedback, Interpreting via Constitutions
- NeurIPS 2025: Gated Attention (Best), Infinity-Chat (Artificial Hivemind), LLMs as CO solvers (7B > Deepseek-R1)
- Key themes: RLVR/GRPO dominant, CTR scaling laws mature, generative recommendation at scale, hybrid SSM-attention, agent systems explosion, self-play for reasoning
- Updated: wiki/index.md, wiki/log.md

## [2026-06-29] synthesis | arXiv Paper Check — AI & CTR (June 29, 2026)
- New page: wiki/synthesis/2026-06-29/arxiv-paper-check.md
- Coverage: 15 selected papers from cs.AI / cs.IR / cs.LG (submitted June 25-26, 2026)
- Top picks: CARVE (new recurrent architecture beating GDN-2), AgentX (agent-driven RecSys iteration at Kuaishou), NOVA (verification-aware architecture evolution), UniFormer (unified model-centric scaling), L2A (resource-adaptive LLM inference), R2LM (bifocal diffusion LMs), Google PAT (automated paper review), IntuRec (intuition-guided latent reasoning for RecSys), TRUST (item-calibrated temporal signals), co-failure ceiling for multi-model ensembles
- Key themes: Agent-driven RecSys iteration production-ready, LLM reasoning+RecSys convergence, resource-adaptive inference, ensemble limits quantified, interpretability advances
- Updated: wiki/index.md, wiki/log.md

## [2026-06-29] synthesis | LLM Tech Report Digest — 各大 AI 公司最新技术报告摘要
- New page: wiki/synthesis/2026-06-29/tech-report-digest.md
- Coverage: 14 份经 arXiv 验证的技术报告 — DeepSeek (V3/R1), Meta (Llama 4), Microsoft (Phi-4/Phi-4-Mini/Phi-4-reasoning/Phi-4-reasoning-vision), Qwen (Qwen3/Qwen3-VL/Qwen3-Omni), Amazon (Nova Family), MiniMax (M1), LG (EXAONE Deep)
- Key themes: MoE 主流架构, 推理模型 (DeepSeek-R1, Phi-4-reasoning, MiniMax-M1), 混合注意力机制 (MiniMax-M1 Lightning Attention), 多模态统一 (Qwen3-Omni, Phi-4-Multimodal), 合成数据训练 (Phi-4), 数据质量优先
- 核心创新: DeepSeek-R1 纯 RL 推理激励; MiniMax-M1 CISPO RL 算法; Qwen3 thinking/non-thinking 统一框架; Phi-4-reasoning SFT+outcome-based RL
- Updated: wiki/index.md, wiki/log.md

## [2026-06-27] synthesis | LLM Tech Report Digest — 2026-06-27
- New page: wiki/synthesis/2026-06-27/tech-report-digest.md
- Coverage: 19 AI labs — DeepSeek (V4/V3/R1), OpenAI (GPT-5), Meta (Llama 4), Google (Gemini 3 Pro), Anthropic (Claude Opus 4/Sonnet 4), Mistral (Large 3/Small 4/Medium 3.5), Qwen (Qwen3), xAI (Grok 4.20), Microsoft (Phi-4-RV-15B), NVIDIA (Nemotron 3 Ultra), Apple (AFM), Amazon (Nova), ByteDance (Doubao-Seed-2.0), Zhipu (GLM-5), Moonshot (Kimi K2/K2.5), StepFun (Step 3), Baichuan (M1/M2/M3), InternLM, 01.AI (Yi)
- Key themes: MoE dominance, context scaling to 1M-10M, reasoning models becoming standard, sparse attention innovations, open-weight race, domain specialization (medical/coding), multi-token prediction, RL innovation (GRPO/RLVR/async)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-26] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-06-26)
- New page: wiki/synthesis/2026-06-26/wq101-alpha-daily.md
- Market context: S&P 500 7,357 (-0.01%), MU blowout Q3 ($41.46B, +346% YoY), Core PCE 4.1% (3Y high), CAT +76% YTD, sector rotation semi→industrial/energy/healthcare
- Key picks: MU (10/10, Alpha#1/#6), CAT (9/10, Alpha#41/#1), MRVL (9/10, Alpha#1/#30), SNDK (9/10, Alpha#1/#41)
- Top factors: Alpha#1 (momentum, 10 stocks), Alpha#19 (mean-reversion, 9 stocks), Alpha#30 (volatility, 7 stocks)
- Key theme: MU earnings confirms AI supercycle → momentum dominant again; Mag7 mean-reversion signals accumulate
- Updated: wiki/index.md, wiki/log.md

## [2026-06-26] synthesis | Game RL & Game AI Bot — Daily Paper Digest
- New page: wiki/synthesis/2026-06-26/game-rl-daily.md
- Coverage: ~30 papers across 8 categories — MARL in games, LLM-powered game agents, game foundation models (NitroGen CVPR 2026 Oral, Game-TARS, Lumine, GROW), procedural content generation (IPCGRL, PCGRLLM, MOPCGRL, CrawLLM), game benchmarks (WildClawBench, GameWorld, PokeGym), self-play RL (SPIRAL, SPA, SeRL, SPEAR), related techniques (curiosity-driven RL, hierarchical RL, imitation learning), industry game AI (NVIDIA, ByteDance, NYU)
- Key trends: VLM+RL convergence, unified keyboard-mouse action spaces, self-play for reasoning transfer, commercial 3D games as testbeds, LLMs for PCG reward/level/asset generation
- Updated: wiki/index.md, wiki/log.md

## [2026-06-26] synthesis | Investment Daily — 美股/港股/A股/中概/新能源科技与AI热点
- New page: wiki/synthesis/2026-06-26/investment-daily.md
- Coverage: 美股(Mag 7, 半导体/AI), 中概股, 港股科技, A股AI概念, 新能源/电动车, AI热点主题(大模型/Agent/自动驾驶/机器人/资本开支)
- Key events: 美光Q3炸裂财报(营收$41.46B, EPS $25.11), 核心PCE 3.4%施压科技估值, Apple -6%, 费城半导体+3.59%, GPT-5.6正式发布, Anthropic AI递归自进化报告
- Updated: wiki/index.md, wiki/log.md

## [2026-06-26] synthesis | Tech Report Digest — 各大 AI 公司技术报告汇总 (2026-06-26 第十二版)
- New page: wiki/synthesis/2026-06-26/tech-report-digest.md
- Coverage: 21 家机构, 40+ 份 Tech Report / System Card
- Companies: DeepSeek (V4/V3.2), OpenAI (GPT-5.5/5.4), Meta (Llama 4), Google (Gemini 3.1/2.5), Anthropic (Opus 4.8/Fable 5/Mythos 5/Sonnet 4.6), Mistral (Large 3/Ministral 3/Magistral), Qwen (Qwen3/3.5-Omni/Image-2.0), Microsoft (Phi-4-reasoning-vision/Phi-4-reasoning), Apple (AFM 2025), NVIDIA (Nemotron 3 Ultra/Super/Nano), xAI (Grok 4.1/4/3), Amazon (Nova family), Zhipu (GLM-5/GLM-4.5V), InternLM (Intern-S1-Pro/S1), Moonshot (Kimi K2.5/K2), StepFun (Step-3/3.5 Flash/Step3-VL-10B), ByteDance (Seed1.8/1.5-VL), 01.AI (Yi-Lightning/Yi), Baichuan (M3/Omni-1.5)
- Key trends: MoE 全面主流化, 1M+ context 旗舰标配, RLVR 推理训练普及, Hybrid Mamba-Transformer 新兴, Muon/MuonClip 优化器挑战 AdamW, 原生多模态 MoE 成为标准
- Updated: wiki/index.md, wiki/log.md

## [2026-06-27] synthesis | arXiv Paper Check — AI & CTR (2026-06-27)
- New page: wiki/synthesis/2026-06-27/arxiv-paper-check.md
- Coverage: 12 AI/LLM papers + 8 CTR/IR/RecSys papers from Friday June 26 submissions
- AI highlights: Refusal-Persona gating (2606.26161), Sycophancy detection (2606.26155), Verification Horizon (2606.26300), Instruction Bleed (2606.26356), Red Queen Gödel Machine (2606.26294), auto-psych (2606.26460)
- CTR highlights: UniFormer scaling (2606.27058, Kuaishou), NOVA agent harness (2606.27243), AgentX (2606.26859), TRUST temporal calibration (2606.27214), TikTok attribution (2606.26690)
- Key themes: Agent-driven RS iteration, mechanistic interpretability for safety, verification bottleneck, co-evolution, GPU-native retrieval acceleration
- Updated: wiki/index.md, wiki/log.md

## [2026-06-26] synthesis | Conference & arXiv Digest — Comprehensive Roundup
- New page: wiki/synthesis/2026-06-26/conference-digest.md
- Comprehensive roundup of 12+ ML/AI conferences: ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, WWW 2026, SIGIR 2025, CIKM 2025, RecSys 2025
- 100+ curated papers, 12+ industry labs: Google DeepMind, OpenAI, Meta AI, Microsoft, NVIDIA, Apple, ByteDance, Alibaba, Tencent, Kuaishou
- Key themes: RLVR/GRPO for LLM reasoning, diffusion language models (LLaDA, CALM), CTR scaling laws, generative recommendation, agent systems, generalist game agents (NitroGen), 4D scene reconstruction (D4RT), continuous reasoning (MUX, PaCoRe)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-26] synthesis | arXiv Paper Check — AI & CTR (2026-06-26)
- New page: wiki/synthesis/2026-06-26/arxiv-paper-check.md
- Scanned new listings for Thu, 25 Jun 2026 across cs.IR (9 new), cs.LG (186 new), cs.AI (182 new)
- 20 papers curated: TokenMinds (YouTube SID user tokens), Graph-GRPO (JD GRPO e-commerce), GenRec (JD generative rec), GenCI/GenLI (generative CTR), Gryphon (SID item scoring), ASRM/DSIRM e-commerce relevance, Autodata (agentic data scientist), Pigeonholing (prompt robustness), Abstract representational geometry in LLMs, Active Inference scaling law, Causal RL intro
- Key themes: GRPO/RL for recommendation, SIDs dominate generative retrieval, agentic AI safety, mechanistic interpretability × neuroscience, test-time compute scaling
- Updated: wiki/index.md, wiki/log.md

## [2026-06-25] synthesis | WQ101 Alpha Daily — 美股 Top 20
- New page: wiki/synthesis/2026-06-25/wq101-alpha-daily.md
- WorldQuant 101 Alpha factor-based screening of US stocks, Top 20 picks
- Key picks: MU, SNDK, MRVL, ALAB, CRDO, QCOM, NVDA, AVGO (semi/AI momentum plays)
- Market context: S&P 500 7,394 (-0.10%), Fed rate hike fears, sector rotation out of tech into energy/defensives
- Top factors used: Alpha#1 (momentum, 8 stocks), Alpha#19 (mean-reversion, 9 stocks), Alpha#41 (trend strength, 7 stocks)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-25] synthesis | Game RL & Game AI Bot — Daily Survey
- New page: wiki/synthesis/2026-06-25/game-rl-daily.md
- ~75 curated papers across 8 categories covering Game RL, LLM Game AI Bots, Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, Self-Play/MARL, World Models, Curiosity, HRL, IRL
- Key highlights: QZero (model-free Go), RGSC (ICLR 2026), NitroGen (CVPR 2026 NVIDIA), Game-TARS (ByteDance), SPIRAL (ICLR 2026), Dreamer (Nature 2025), Matrix-Game 3.0, Odysseus, PopuLoRA, MARSHAL, FMSP, ChatNPC (ACL 2026), GameWorld, OmniGameArena, Orak (KRAFTON), BALROG, PCGRLLM (NYU), Multiverse
- Key themes: RL+LLM convergence via self-play, generalist game foundation models, LLM-powered NPCs, diffusion game engines, population-based self-play, evaluation infra maturity
- Updated: wiki/index.md, wiki/log.md

## [2026-06-25] synthesis | arXiv Daily — AI, LLMs, Recommendation, Advertising, CTR, Games, RL, Sequential Modeling
- New page: wiki/synthesis/2026-06-25/arxiv-daily.md
- 33 papers across 8 categories (LLM Training & Alignment, LLM Reasoning & Agents, LLM Inference & Efficiency, Recommendation & Advertising, E-Commerce & IR, RL & Games, World Models & Multi-Agent, Sequential Modeling & Architectures)
- Key themes: LLM↔RecSys convergence, KV-cache compression explosion, agentic LLM training, scaling pitfalls, SSMs as Transformer alternatives
- Updated: wiki/index.md, wiki/log.md

## [2026-06-25] synthesis | Conference & arXiv Digest — June 2026
- New page: wiki/synthesis/2026-06-25/conference-digest.md
- 100+ papers across 12 venues (ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, WWW 2026, SIGIR 2026, RecSys 2025, CIKM 2025)

## [2026-06-26] synthesis | arXiv Daily
- New page: wiki/synthesis/2026-06-26/arxiv-daily.md
- 30 papers across 7 categories: LLM Reasoning & Alignment, Efficient Transformers & Attention, CTR Prediction & Advertising, Sequential Recommendation, RL for LLMs & Agents, Games & Long-Horizon Decision Making
- Key highlights: SelfCompact (adaptive context compaction), HydraHead (head-level FA/LA hybridization), G2PO (graph credit assignment for RL), Odysseus (100+ turn VLM game-playing), DeRes (dual-path residual for CTR), Taiji (Pareto-optimal semantics-IDs trade-off; Kuaishou deployed), Pigeonholing (bad-context mode collapse)
- Updated: wiki/index.md, wiki/log.md
- Covers: LLM training/alignment, reasoning, agents, CTR prediction, recommendation systems, generative models, multimodal, games, formal math, RL
- Key institutions: Google DeepMind, NVIDIA, Meta AI, Apple, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, JD.com, NetEase, Microsoft Research, Amazon
- Updated: wiki/index.md, wiki/log.md

## [2026-06-25] synthesis | 投资日报 — 2026-06-25（美股/港股/A股/中概/新能源科技与AI热点）
- New page: wiki/synthesis/2026-06-25/investment-daily.md
- Micron Q3 FY26 财报 "核弹级" 超预期：营收 $41.5B（+346% YoY），EPS $25.11（+930% YoY），Q4 指引 $50B（+74% QoQ），盘后 +15%+
- SK Hynix 宣布 $294 亿纳斯达克上市（7/10）；JPMorgan 上调标普 500 目标至 7,800
- 美股：S&P 500 -0.09%，Nasdaq -0.43%，Dow +0.36%（板块大轮动科技→工业/金融）
- 港股：恒指 +0.33%，科技指数 +1.81%（SMIC +8.9%、Tencent +3.4%、Zhipu +4.6%）
- A 股：AI 应用端接棒（神州数码涨停、信创 ETF +3.68%）；MiniMax M1 开源提振科创板
- EV：出口创纪录 $9.2B（+49% YoY），内需承压，BYD 首选
- AI 热点：Micron take-or-pay 合同 $100B+、Zhipu 配售、腾讯/阿里 Agent 落地、曹操 Robotaxi
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-25] synthesis | arXiv AI Research Search — June 2026
- New page: wiki/synthesis/2026-06-25/arxiv-ai-search.md
- 11 curated papers across LLM Alignment (implicit feedback, MLLM bias), CTR/Advertising (DS-MLP, IDProxy, UniVA, Token Factory), Games/RL (MindGames Arena, SlimDT, Game AI)
- Key institutions: UMass Amherst, UIUC, Yahoo Research, Renmin University, Xiaohongshu, Tencent, Google, Embark Studios
- Updated: wiki/index.md, wiki/log.md

## [2026-06-24] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-24)
- New page: wiki/synthesis/2026-06-24/wq101-alpha-daily.md
- 宏观背景：费城半导体 -7.6%（SK Hynix 放缓 HBM）+ FOMC 鹰派 + VIX 19 + 板块大轮动科技→能源/工业/防御
- 核心信号：Alpha#53（反转）> Alpha#41（趋势强度）> Alpha#1（动量）；防御反转逻辑取代纯动量
- Top 3: CAT (9.0), OXY (8.5), LLY (8.5)
- 板块分布：能源 5只, 半导体 5只, 医疗 3只, 工业 3只, 消费防御 2只, 材料 1只
- 变化 vs 06-23：全面转向能源+防御+工业；半导体从 8 只减至 5 只；新增 OXY/CAT/LLY/GEV/VRT/WMB/FCX 等
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-24] synthesis | 投资日报 — 2026-06-24（美股/港股/A股/中概/新能源科技与AI热点）
- New page: wiki/synthesis/2026-06-24/investment-daily.md
- 全球 AI 信仰压力测试：四大云厂商 Capex $7,250 亿（+77%），算力租赁价回落 30%，科技巨头集体缩紧预算
- 美股：S&P 500 -1.44%, Nasdaq -2.21%, 费城半导体 -7.9%（MU -13%, SNDK -12.5%, MRVL -9%）
- 港股：恒指一年新低（-1.8%），恒科指 -3.3%（Zhipu -10%, MiniMax -16%, 9988 跌破 HK$99）
- A 股：创业板 -3.84%，光模块/PCB 全线杀跌，寒武纪 -3%
- 中概：1260H 清单持续发酵，BABA $102.60 52 周新低
- EV：全线下挫，TSLA -5.79%，中国 EV 价格战利润侵蚀加速
- 焦点事件：MU Q3 FY26 财报明日盘后（预期营收 +268%, EPS +930%），白宫 1260H 清单诉讼
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-24] synthesis | Tech Report Digest — 各大AI公司技术报告汇总 (2026-06-24 第十一版)
- New page: wiki/synthesis/2026-06-24/tech-report-digest.md
- Coverage: 20+ 家机构, 50+ 份 Tech Report / System Card
- Companies: DeepSeek, OpenAI, Meta, Google, Anthropic, Mistral, Qwen, xAI, Microsoft Phi, Apple, NVIDIA, Amazon, Zhipu, InternLM, Moonshot Kimi, ByteDance Seed/Doubao, StepFun, 01.AI, Baichuan, MiniMax, Cohere, Stability AI, AI21 Labs
- Key trends: MoE 全面主流化, 1M+ context 成为旗舰标配, RLVR 推理训练普及, Hybrid Mamba-Transformer 新兴, Muon/MuonClip 优化器挑战 AdamW
- Pricing comparison table added for all major models
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-24] search | arxiv-daily
- Summary: wiki/synthesis/2026-06-24/arxiv-daily.md
- Coverage: 68 papers across 7 categories (LLM Reasoning & Agents, Efficient Inference & KV Cache, SSM & Sequence Modeling, CTR & Advertising, Recommendation, Multi-Agent RL & Games, Social World Models & Alignment)
- Key papers: SPIRAL (Stanford), SelfCompact, MiniMax Sparse Attention (109B MoE), Mamba-3, DeRes, DS-MLP, Odysseus (Princeton), LoopCTR, Keyless Attention, Tangram

## [2026-06-24] synthesis | game-rl-daily
- Summary: wiki/synthesis/2026-06-24/game-rl-daily.md
- Coverage: 40 papers across 7 categories (Game RL, Game AI Bots, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, Related Techniques)
- Key papers: Strat-Reasoner (ICML 2026), NitroGen (CVPR 2026), Game-TARS (ByteDance), Dreamer 4 (DeepMind), GameNGen (Google), Matrix-Game 3.0 (Skywork), BALROG (ICLR 2025), DSGBench, AI GameStore (MIT/Harvard), MCU (ICML 2026)
- New page: synthesis/2026-06-24/game-rl-daily.md
- Updated: wiki/index.md, wiki/log.md

## [2026-06-23] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-23)
- New page: wiki/synthesis/2026-06-23/wq101-alpha-daily.md
- 宏观背景：科技 Mega-Cap 抛售（GOOGL -5%/AMZN -4.8%/MSFT -3.2%）+ 美伊协议落地 + FOMC 鹰派 Hold
- 核心信号：Alpha#1（动量）主导半导体（MU/MRVL/ARM）+ Alpha#53（反转）覆盖超卖 Mega-Cap
- Top 3: MU (10), MRVL (9.5), SNDK (9.5)
- 板块分布：半导体/AI 8只, 通信服务 2只, 能源 2只, 工业 2只, 云计算 1只, 消费周期 1只, 医疗 1只, 金融 1只, 技术/消费电子 2只
- 变化 vs 06-22：Mega-Cap 均值回复策略上调（GOOGL/AMZN/MSFT/META），能源回调后超卖机会（XOM/CVX）
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-22] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-22)
- New page: wiki/synthesis/2026-06-22/wq101-alpha-daily.md
- 宏观背景：美伊和平协议签署 + FOMC 鹰派 Hold + Apple-Intel 芯片合作 → 半导体爆发
- 核心信号：Alpha#1（动量）+ Alpha#53（反转）主导；存储/AI 半导体突破新高
- Top 3: MU (10), INTC (10), WDC (9.5)
- 板块分布：半导体/AI 9只, 科技/互联网 3只, 消费 3只, 工业 2只, 金融 2只, 能源 2只
- 变化 vs 06-21：半导体从 8→9 只、消费防御 1→3 只、金融 3→2 只、医疗出局
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-22] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-22)
- Summary: wiki/synthesis/2026-06-22/investment-daily.md
- 宏观背景：6/22 周一港股下跌（恒指 -1.24%）；A 股科技分化（创业板/科创 50 创历史新高）；美股 6/19 Juneteenth 休市
- 美股热点：NVDA $210.69、Intel +10.6%（Apple 芯片合作传闻）、TSMC +6.9%、Mag 7 表现分化
- 港股热点：腾讯 WeChat AI Agent 预期差、恒指跌至 11 月低点、AI 公司 IPO 热潮（HQVT 今日上市）
- A 股热点：PCB/半导体/CPO 为绝对主线，寒武纪创新高，中际旭创市值超越茅台
- 中概/EV：EU 拟对 PHEV 加税、BYD Da Tang EV 发布、ADRs 整体走弱
- AI 主题：DeepSeek V4 开源 1.6T MoE、AI CapEx ~$830B（Top 9 CSP）、Agentic AI 时代、机器人、自动驾驶
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-23] search | arXiv Paper Check — AI & CTR (June 23, 2026)
- New page: wiki/synthesis/2026-06-23/arxiv-paper-check.md
- Coverage: cs.AI (220 new, 1181 total) + cs.IR (18 new, 90 total) + cs.LG (201 new, 1113 total) from Fri, 19 Jun 2026
- Top picks: VIMPO (critic-free RLVR via policy-implied value, beats GRPO on AIME/OlympiadBench), Beyond Entropy/ICT (token-level distributional RLVR, +4.58% pass@4), Connect the Dots (Alibaba long-lifecycle agent RL), MATM (multi-agent transactive memory for trajectory sharing), UltraQuant (AMD 4-bit KV cache, 3.47× TTFT reduction), Token Factory (Google soft tokens for LRMs), OneRank (KDD 2026 unified MTL ranking), DIF (Kuaishou cold-start denoising, KDD 2026), ELVA (ECCV 2026 RLVR for multimodal retrieval), TPOUR (ICML 2026 temporal preference optimization)
- Key themes: RLVR optimization beyond GRPO (VIMPO, ICT); long-lifecycle & multi-agent memory; KV compression for agents; generative RecSys maturation; RLVR extends to retrieval
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-23] synthesis | arXiv AI Search — CTR/Recommendation/Attention/LLM Reasoning/Games
- New page: wiki/synthesis/2026-06-23/arxiv-ai-search.md
- Coverage: 30 papers across 4 domains (CTR, Recommendation, Attention/Sequence Models, LLM Reasoning/Games)
- Top picks: GRAB (Baidu, +3.05% revenue), DeRes (dual-path residual, 2× compute savings), GenRec (JD, +9.5% clicks deployed), Kunlun (Meta, MFU 17%→37%), MiniMax Sparse Attention (28.4× compute reduction at 1M ctx), GraphPO (DAG-based RL for reasoning), Odysseus (Princeton, 100+ turn VLM game play), RA-RFT (analogical reasoning via retrieval augmented RL)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-22] search | arXiv Paper Check — AI & CTR (June 22, 2026)
- New page: wiki/synthesis/2026-06-22/arxiv-paper-check.md
- Coverage: cs.AI (73 new, 312 total) + cs.IR (11 new, 22 total) from Fri, 19 Jun 2026
- Top picks: ITNet (unified integral transform subsuming conv/attn/rnn), Token Factory (Google soft tokens for LRMs), G2Rec (generative rec graph tokenization), DIF (Kuaishou cold-start denoising, KDD 2026), ELVA (RLVR for multimodal retrieval, ECCV 2026), Beyond Entropy (token-level distributional LLM reasoning), Which Pairs to Compare (DPO comparison curation theory), Emergent Alignment (self-supervised DPO alignment), VCG (multimodal e-commerce cold-start), Diffusion LMs experimental analysis (8×8 architectures×benchmarks), Stellar (disk-backed multimodal retrieval), Beyond Static Leaderboards (agent eval predictive validity), PACMS (submodular context selection for agents)
- Key themes: Unified architectures (ITNet); generative recommendation productionization (Token Factory, G2Rec); RLVR extending to retrieval (ELVA); cold-start & denoising for industrial recsys (DIF, VCG); LLM reasoning & alignment (Beyond Entropy, Emergent Alignment, Which Pairs to Compare); agent evaluation (Beyond Static Leaderboards, PACMS)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-23] synthesis | arxiv-daily
- New page: wiki/synthesis/2026-06-23/arxiv-daily.md
- Coverage: ~70 papers across 7 categories — LLM Reasoning & RLVR (14), Efficient Attention & Architecture (7), Multimodal (2), CTR Prediction & Advertising (18), Recommendation (2), Games & RL (14), Sequential & Time Series Modeling (10)
- Top picks: CADET (LinkedIn, +11.04% CTR), GrandCode (first to beat all humans in Codeforces), MiniMax Sparse Attention (28.4× compute reduction), SPIRAL (self-play reasoning), NRT (verifier-free reasoning), GraphPO (DAG-based RL), CAPS (unified attention for TS), Hidden-Align (zero-overhead RL improvement)
- Key themes: RL for reasoning is dominant paradigm; CTR/advertising going generative across all major tech companies; sparse attention for long context; self-play/multi-agent RL for reasoning; foundation models for time series maturing; cross-layer communication emerging

## [2026-06-22] synthesis | arxiv-daily
- New page: wiki/synthesis/2026-06-22/arxiv-daily.md
- Coverage: ~50 papers across LLM reasoning, RLVR/GRPO, efficient inference, recommendation/CTR, games/RL, multimodal, safety/alignment, synthetic data, multi-agent systems
- Domains: AI, LLM, CTR, advertising, recommendation, games, RL, multimodal, safety

## [2026-06-21] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-21)
- New page: wiki/synthesis/2026-06-21/wq101-alpha-daily.md
- 宏观背景：FOMC 鹰派点阵图后深 V 修复 + 美伊和平协议签署 + 三巫日平稳到期 + 6/19 Juneteenth 休市
- 核心信号：Alpha#1 动量 + Alpha#53 反转因子共同主导，半导体/存储全面反攻
- Top 3: MU (9.5), MRVL (9.5), INTC (9.0)
- 板块分布：半导体/AI 8只, 金融 3只, 医疗 3只, 科技/互联网 3只, 消费必需 1只, 工业 1只, 能源 1只
- 周度变化 vs 06-18：风格从金融防御→半导体反攻；反转因子增强；新增 INTC/WDC/CVX/JNJ
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-21] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-21)
- Summary: wiki/synthesis/2026-06-21/investment-daily.md
- 宏观背景：6/21 周日无交易；FOMC 鹰派信号（10 月加息概率 72%）；板块大轮动科技→防御；美伊协议执行中
- 美股：S&P 500 +1.08%至 7,500，Nasdaq +1.91%至 26,518（周四 6/18 收盘）；Mag 7 六月合计蒸发 $2T+；NVDA +3%/$214；INTC +10.6%（Apple 芯片合作）；TSM +6.9%/$462；AMD +4.9%创历史新高
- 中概：BABA $107（-13.78%月）；PDD $81.5（PE 9.9x）；1260H 清单持续压制；DeepSeek $510 亿首轮融资
- 港股：恒生科技 4,604（-1.39%）；智谱 AI GLM-5.2 发布+32.8%市值 HK$7,000亿+；WeChat AI Agent 预期
- A 股：沪指 4,090（-0.43%）；科创50 +3.84%创新高；寒武纪 ¥1,507（+23.6%/周，高盛目标 ¥2,406）；中际旭创千元股创历史新高；上交所 AI 大模型科创板第五套上市标准发布
- 新能源：中国四大 EV 厂全部发布自研智驾芯片；BYD 出口+80%；NEV 渗透率 62.9%
- AI 热点：DeepSeek V4 1.6T MoE；Claude Fable 5/Mythos 5 出口管制；1M 上下文成为旗舰标配；MoE 绝对主流
- 三大主线：AI 算力基础设施 / 半导体国产替代 / 中概估值修复
- 三大风险：10 月加息 / AI CapEx ROI 验证 / 1260H 中概抛售
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-21] synthesis | 顶会论文专题报告 — 2026年6月全面版（2026-06-21）
- New page: wiki/synthesis/2026-06-21/conference-digest.md
- Coverage: 12+ 会议/venue (ICML 2026 / AAAI 2026 / NeurIPS 2025 / ICLR 2026 / CVPR 2026 / KDD 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025), 50+ 论文, 13+ 实验室
- 章节: 19 个分类（LLM 架构 / 推理 & RL / Agent 系统 / CTR & 推荐 / 生成模型 / 代码推理 / Benchmark / 游戏 / 序列建模 / Frontier 模型等）
- NeurIPS 2025 Best: Gated Attention (Attention Sink 消除), RL Reasoning Critique (value-action gap), Transductive Online Learning
- ICLR 2026 Outstanding: Transformers Succinctness, MEM1 (memory-reasoning), AgentFlow (7B > GPT-4o), Mamba-3 (inference-first SSM)
- ICML 2026: Shannon Scaling Law (数据质量 SNR), Self-Flow Matching, CTR-RL, ALIVE (Alibaba 游戏), BitsMoE (MoE 量化), Process-Verified RL
- CVPR 2026 Best: D4RT (Google DeepMind 4D 场景重建), NitroGen (NVIDIA 通用游戏 Agent), LLaDA-V (扩散 MLLM)
- KDD 2026: RankUp (Tencent), RankElastor, DIF (Kuaishou 冷启动去噪), JourneyFormer (Airbnb), GenCTR (Alibaba)
- RecSys 2025: Amazon Prime Video MoE-Transformer, TikTok Explicit Negatives, Meta Peak-End Retention
- 新增 Frontier Model 报告: DeepSeek V4, GPT-5.5, Gemini 3.1, Claude Opus 4.8/Fable 5/Mythos 5, Llama 4, Qwen3/3.5/3.7, Mistral Large 3, Kimi K2.7 Code
- Key trends: 推理模型/RLVR 全会议覆盖; Gated Attention 新范式; MoE 主流化; 生成式推荐产业化; 游戏 Agent 通用化; 扩散 LM 崛起
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-20] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-20)
- Summary: wiki/synthesis/2026-06-20/investment-daily.md
- 宏观焦点：美联储 10 月加息概率 72%；美股板块大轮动（科技→医疗/金融）；美伊协议；DeepSeek 510 亿融资（估值 4000 亿）
- 美股：Mag 7 全线下跌（META -5.31%/MSFT -3.80%/AMZN -3.46%）；MU +6.4%/INTC +8.9%/AMD +4.0% 半导体反弹；ACN -19% Q3 指引 miss
- 中概：金龙指数 -1.14%；BABA -3.18%/PDD -2.12%/BEKE -3.72%；TSM +1.48%；蔚来 +0.80%
- 港股：腾讯 WeChat AI Agent 推进；智谱/MiniMax A+H 双平台布局加速；美图 AI 应用出海 +26%
- A 股：沪指 4,090（-0.43%）；寒武纪/工业富联/源杰科技 Q1 业绩爆发；AI 算力板块 +3.56%
- 新能源：小鹏市值反超理想；BYD 出口 +80%；NEV 渗透率 62.9%；中国四大 EV 厂自研智驾芯片全部发布
- AI 主题：Anthropic $650 亿融资；NVIDIA Vera Rubin 量产；AI CapEx 大辩论；机器人融资超 ¥345 亿
- 三大风险：10 月加息 / AI CapEx ROI 验证 / 1260H 中概抛售
- 三大主线：AI 算力基础设施 / 半导体国产替代 / 中概估值修复
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-20] synthesis | Frontier Model Tech Reports Digest
- New page: wiki/synthesis/2026-06-20/tech-report-digest.md
- Coverage: 8 major tech reports — DeepSeek V4 (Apr 2026, 1.6T MoE, CSA/HCA), Llama 4 (Apr 2025, Scout/Maverick/Behemoth), Gemini 2.5 (Jul 2025, MoE, dynamic thinking, 3h video), Claude 4/5 (May 2025–Jun 2026, Opus 4/Sonnet 4/Fable 5/Mythos 5), Mistral Large 3 (Dec 2025, 675B MoE, Apache 2.0), Kimi K2→K2.6 (Jul 2025–Apr 2026, 1T MoE, MuonClip, agentic), GPT-5.5 (Apr 2026, 1M context, $5/$30), Qwen3 (May 2025, 119 languages, hybrid thinking)
- Key themes: All labs converge on MoE + thinking modes + million-token contexts + RLVR post-training; pricing ranges 40× from DeepSeek V4 ($0.87/M out) to GPT-5.5 Pro ($180/M out)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-20] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-20)
- New page: wiki/synthesis/2026-06-20/game-rl-daily.md
- Coverage: ~50 papers across 7 categories — Game RL (12), Game AI Bots (6), Game Foundation Models (4), Procedural Content Generation (5), Game Benchmarks (5), Industry Game AI (6), Related Techniques (12)
- Top picks: Game-RL (ICLR 2026, Fudan, Code2Logic synthesis for VLM RL), SPIRAL self-play (ICLR 2026), GROW (GRPO for Minecraft VLMs), Dreamer 4 (offline Minecraft diamonds), Dreamer-CDP (ICLR 2026 WS, reconstruction-free world models), Absolute Zero (zero-data self-play), Self-Challenging Agent (Meta/Berkeley), Language Self-Play (Meta), Realtime Async RL (formal realtime RL), NVIDIA ACE production in PUBG/inZOI, Ubisoft Teammates (GDC 2026), GameWorld (NUS, 34 games standardized), Multi-task PCGRL (Scientific Reports 2026), Reward Design Agent (VLM reward design)
- Key themes: Game data as scalable RL training signal for VLM reasoning; self-play convergence for LLM reasoning; reconstruction-free world models; realtime asynchronous RL; industry production at scale (NVIDIA ACE); standardized evaluation benchmarks
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-20] synthesis | Conference Digest — 顶会论文专题报告（2026-06-20 全面版）
- New page: wiki/synthesis/2026-06-20/conference-digest.md
- Coverage: 12+ conferences/venues, 50+ papers, 13+ industry labs (Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon)
- Sections: NeurIPS 2025 Best Papers (Gated Attention, RLVR Critique) → ICLR 2026 Outstanding (Transformers Succinctness, MEM1, AgentFlow) → ICML 2026 (Shannon Scaling Law, Self-Flow, CTR-RL, ALIVE) → AAAI 2026 Outstanding → CVPR 2026 Best (D4RT, NitroGen) → EMNLP 2025 (Speculative Streaming, Value-Action Gap) → KDD 2026 (RankUp, RankElastor, DIF, JourneyFormer) → RecSys 2025 → SIGIR 2026 (656 accepted across all tracks) → WWW 2026 Industry (OneTrans, NEZHA, JD generative rec) → Frontier Models (Kimi K2.7 Code, DiffusionGemma, Gemma 4 12B, GLM-5.2, Gemini Omni)
- Key themes: Reasoning models & test-time compute (cross-venue); Gated Attention & attention innovation; CTR Scaling Laws mature; Generative Recommendation industrial deployment; Agent explosion (465 ICML 2026 papers); 4D Vision & 3D Generation; Multi-Agent Society protocols; MoE + Hybrid + RLVR convergence
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-19] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-19)
- New page: wiki/synthesis/2026-06-19/game-rl-daily.md
- Coverage: ~80 papers across 7 categories — Game RL (16), Game AI Bots (16), Game Foundation Models (8), Procedural Content Generation (10), Game Benchmarks (8), Industry Game AI (6), Related Techniques (16)
- Top picks: SPIRAL (ICLR 2026, self-play for LLM reasoning transfer), NitroGen (CVPR 2026, NVIDIA generalist gaming foundation model), Game-TARS (500B token pre-training, beats GPT-5/Claude-4), Dreamer 4 (Minecraft diamonds from offline data), PCGRLLM (+415% reward generation), lmgame-Bench (ICLR 2026), CDE (curiosity-driven exploration for RLVR, ICLR 2026)
- Key themes: Self-play + RL convergence for LLM reasoning; generalist game foundation models; world models as unifying framework; standardization of game benchmarks; industry deployment maturing (NVIDIA ACE/IGI, AstraGame); PCG with LLMs for reward design
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-19] synthesis | Tech Report Digest — 各大AI公司技术报告汇总 (2026-06-19 全面更新版)
- New page: wiki/synthesis/2026-06-19/tech-report-digest.md
- Coverage: 20+ 家机构, 19+ 份 Tech Report / System Card
- 核心新增/补充: DeepSeek V4 (1.6T MoE, CSA+HCA, 1M ctx), GPT-5 System Card (router-based unified system), Llama 4 (Scout/Maverick, MoE+early fusion), Gemini 3.1 Pro (2M ctx MoE), Claude 4 系列 (Opus 4.8/Fable 5/Mythos 5 最新 System Card 索引), Mistral Ministral 3/Magistral (Cascade Distillation + 纯RL推理), Phi-4-reasoning-vision (多模态推理), Apple AFM 2025 (PT-MoE server), NVIDIA Nemotron 3 Ultra (Mamba-Attention hybrid + LatentMoE), Grok 4/4.1, Amazon Nova Premier (1M ctx), Qwen3.5-Omni/Qwen 4 Coder (OmniMoE, SWE-Verified 82%), GLM-5 (DSA + 异步RL slime), Kimi K2/K2.5 (MuonClip + Agentic), ByteDance Seed2.0/Seed1.8, Step 3.5 Flash (MFA+AFD, 196B-A11B), InternLM3 (4T 数据效率), Yi-Lightning (MoE+RAISE), Baichuan-M3 (SPAR 医疗RL)
- 架构趋势: MoE 绝对主流 → Hybrid Mamba-Attention 新兴 → Hybrid Attention (CSA/DSA) 长上下文效率 → Muon/MuonClip 优化器替代 AdamW
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-19] synthesis | Conference Digest — 顶会论文专题报告（2026-06-19 全面版）
- New page: wiki/synthesis/2026-06-19/conference-digest.md
- Coverage: 12+ conferences/venues, 50+ papers, 12+ industry labs (Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon)
- Sections: LLM Architecture (Mamba-3, Nemotron 3, Gated DeltaNet-2, ParaRNN) → Reasoning (Re², SFPO, CAPO, PoLR) → RL for LLMs (RLVR, AREAL, Long-RL, TAMPO) → Agent Systems (A-MEM, ACE, WebOperator, AgentAuditor) → CTR/Recommendation Scaling (EST, LoopCTR, UniMixer, TokenFormer, RankUp, TencentGR) → Generative Models (DiffusionGemma, MMAudio) → CVPR 2026 → ACL/EMNLP 2025–2026 → SIGIR/WWW/CIKM/RecSys → Frontier Models (Claude Opus 4.8, Nemotron 3 Ultra, Gemini 3.5, DiffusionGemma, Kimi K2.7 Code)
- Key themes: Hybrid SSM-Attention dominant architecture; CTR Scaling Laws established research area; RLVR critique paper (NeurIPS 2025); All-Modality Generative Recommendation emerging; Frontier models converging on MoE + Hybrid + RLVR
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-19] search | arXiv Paper Check — AI & CTR (June 19, 2026)
- New page: wiki/synthesis/2026-06-19/arxiv-paper-check.md
- Coverage: cs.AI (73 new, 312 total) + cs.IR (11 new, 22 total) from Fri, 19 Jun 2026
- Top picks: G2Rec (generative rec graph tokenization), Token Factory (Google soft tokens for LRMs), ITNet (unified integral transform subsuming conv/attn/rnn), ELVA (RLVR for retrieval, ECCV 2026), DIF (Kuaishou cold-start denoising, KDD 2026), VCG (multimodal video cold-start), Beyond Entropy (token-level distributional LLM reasoning)
- Key themes: Generative recommendation productionization; unified architectures (ITNet); RLVR extending to retrieval; cold-start & denoising for industrial recsys; cost-aware AI inference
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-20] search | arXiv Paper Check — AI & CTR (June 20, 2026)
- New page: wiki/synthesis/2026-06-20/arxiv-paper-check.md
- Coverage: cs.AI (73 new, 312 total) + cs.IR (11 new, 22 total) from Fri, 19 Jun 2026
- Top picks: ITNet (unified integral transform subsuming conv/attn/rnn), Token Factory (Google soft tokens for LRMs), G2Rec (generative rec graph tokenization), ELVA (RLVR for retrieval, ECCV 2026), DIF (Kuaishou cold-start denoising, KDD 2026), VCG (multimodal video cold-start), Beyond Entropy (token-level distributional LLM reasoning), Which Pairs to Compare (DPO comparison curation theory), MonaVec (training-free edge vector search), Diffusion LMs experimental analysis (8 architectures × 8 benchmarks)
- Key themes: Unified architectures (ITNet); generative recommendation productionization (Token Factory, G2Rec); RLVR extending to retrieval (ELVA); cold-start & denoising for industrial recsys (DIF, VCG); cost-aware AI inference (SLARouter, Semantic Caching); agent evaluation rethought (Predictive Validity, Agentic Review Systems)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-19] search | arXiv Daily — AI, LLMs, Recommendation, CTR, Games, RL, Sequential Modeling (June 19, 2026)
- New page: wiki/synthesis/2026-06-19/arxiv-daily.md
- Coverage: 23 papers across 6 categories — LLMs & Reasoning (4), Recommendation & CTR (9), Games & Multi-Agent RL (2), Sequential Modeling & Architecture (5), RAG & IR (3)
- Top picks: VIMPO (critic-free RLVR, Berkeley/MIT), G2Rec (Meta generative rec with graph tokenization), Token Factory (Google soft tokens for LRMs), Beyond Entropy (token-level distributional RLVR), Connect the Dots (Alibaba long-lifecycle agent RL), Hierarchical Control in Multi-Agent Games (Embracer LLM+RL NPCs), Lie-Algebra Attention (geometric deep learning meets attention)
- Key themes: RLVR optimization (VIMPO, ICT, Rubric-Conditioned Self-Distillation); generative recommendation deployments from Meta and Google; LLM+RL hybrid agents for games; diffusion model fundamentals revisited (timestep embedding redundancy); long-lifecycle agents as new training paradigm
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-18] synthesis | Tech Report Digest — 各大AI公司技术报告汇总 (2026-06-18 全面更新版)
- New page: wiki/synthesis/2026-06-18/tech-report-digest.md
- Coverage: 22+ 家机构, 40+ 份技术报告/System Card
- 新增/验证内容: Yi-Lightning MoE 报告, InternLM2/InternVL3, Baichuan-M3 (医疗, 2602.06570), Amazon Nova 家族 (arXiv:2506.12103), NVIDIA Nemotron 3 系列 (2512.20856) + Nano 2 (2508.14444), Phi-4-reasoning-vision (2603.03975), Apple AFM v2 (2407.21075 v2 2026-05-27)
- 更新数据来源覆盖: arXiv 验证所有核心链接, 补充中国 vs 西方差异分析表
- Detailed breakdown: 20 家机构逐个参数表 + 架构趋势/开源生态/区域差异三维度分析
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-21] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-21)
- New page: wiki/synthesis/2026-06-21/game-rl-daily.md
- Coverage: ~40 papers across 7 categories — Game RL (6), Game AI Bots (6), Game Foundation Models (5), Procedural Content Generation (4), Game Benchmarks (5), Industry Game AI (4), Related Techniques (7)
- Top picks: SPIRAL (ICLR 2026, self-play for reasoning transfer), NitroGen (CVPR 2026, NVIDIA generalist gaming agent), Game-TARS (ByteDance 500B token pre-training), GROW (GRPO for Minecraft VLMs), PCGRLLM (LLM reward design for PCG), GameWorld/Orak (standardized game benchmarks)
- Key themes: Self-play + RL convergence for LLM reasoning; generalist game foundation models; game world models as real-time engines; LLM + RL for game content generation; standardized evaluation benchmarks; industrial deployment maturing
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-18] search | arXiv Paper Check — AI & CTR (June 18, 2026)
- New page: wiki/synthesis/2026-06-18/arxiv-paper-check.md
- Coverage: 15 papers from June 17 submissions — LoopWM (looped world models), FPRM (fixed-point reasoning), FoMoE (federated MoE training), Diffusion-Proof (dLLM theorem proving), CAHP (attention head pruning), ESM (model merging), JourneyFormer (Airbnb KDD 2026), Querit-Reranker, Strategic Feature Selection
- Key themes: Looped/depth-adaptive architectures, post-hoc model efficiency, production RecSys at scale, safety alignment during pretraining, diffusion beyond generation
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-18] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-18)
- New page: wiki/synthesis/2026-06-18/game-rl-daily.md
- Coverage: 65+ papers across 7 categories — Game RL (7), Game AI Bots (11), Game Foundation Models (8), Procedural Content Generation (12), Game Benchmarks (10), Industry Game AI (2), Related Techniques (18)
- Top picks: NitroGen (NVIDIA generalist gaming agent), Game-TARS (500B token pre-training, beats GPT-5/Claude-4), SPIRAL/STRATAGEM (self-play for LLM reasoning), OmniGameArena (UE5 benchmark, IDC metric), Matrix-Game 3.0 (40 FPS 720p world model), AstraGame (Tencent/WeChat 24,000+ games), NVIDIA ACE Game Agent SDK, GameWorld/Orak/VideoGameBench (standardized game agent benchmarks)
- Key themes: Self-play + RL convergence for LLM reasoning; generalist game foundation models; real-time world models for PCG; industry deployment at scale (AstraGame, NVIDIA ACE); benchmark standardization (OmniGameArena, GameWorld, DSGBench); hierarchical RL for long-horizon agents
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-18] synthesis | Conference Digest — 顶会论文专题报告（2026-06-18 全面版）
- New page: wiki/synthesis/2026-06-18/conference-digest.md
- Coverage: 12+ conferences, 100+ papers, 13+ industry labs
- NeurIPS 2025 Best Papers: Gated Attention (Alibaba, attention-sink-free), RL Reasoning Critique (Tsinghua, value-action gap), Transductive Online Learning (30-year open problem)
- ICLR 2026 Outstanding: Transformers Succinctness, Mamba-3 (CMU/Princeton, inference-first SSM), MEM1 (memory-reasoning synergy), AgentFlow (7B beats GPT-4o)
- ICML 2026: Shannon Scaling Law, BLT Byte-Level Diffusion, CTR-RL, How CoT Decomposes Tasks, ALIVE (Alibaba game RL)
- CVPR 2026 Best Paper: D4RT (Google DeepMind, dynamic 4D scene reconstruction)
- EMNLP 2025: Speculative Streaming (Apple), Value-Action Gap, Song Generation (VersBand)
- KDD 2026: RankUp (Tencent), RankElastor, JourneyFormer (Airbnb)
- RecSys 2025: Amazon Prime Video MoE-Transformer, TikTok Explicit Negatives, Meta Peak-End Retention, Meituan SUAN Scaling
- 7 key trends: reasoning models & test-time compute, attention mechanism innovation (Gated Attention, Mamba-3), generative recommendation paradigm, AI agent production readiness, diffusion/flow matching, CTR scaling laws, CV→multimodal shift
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-18] search | arXiv Daily — AI, LLMs, CTR, Recommendation, Advertising, Agents, Games, Sequential Modeling (2026-06-18)
- New page: wiki/synthesis/2026-06-18/arxiv-daily.md
- Coverage: 20 papers across LLMs (Variable-Width Transformers, Looped World Models, VibeThinker-3B, Ternary Mamba, Agentic Reasoning Survey), CTR/Advertising (GenLI, CADET, GRAB, Field Matters), Recommendation (ChronoID, Implicit Reasoning GR, OneRetrieval, LLM Personas), Games/Agents (ALE Berkeley, NeuroGame Transformer, MARLIN, StraTA, Agent Traces Survey), Sequential Modeling (NextFlow)
- Key themes: Decoder-only CTR going mainstream; generative recommendation + temporal IDs; variable-width transformers challenging fixed-width assumption; professional agent benchmarks showing huge capability gap; game theory meets attention mechanisms
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-17] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-17)
- New page: wiki/synthesis/2026-06-17/wq101-alpha-daily.md
- 宏观背景：FOMC 维持利率 3.5%-3.75%（略偏鹰），Dow 创新高 / Nasdaq -1.15%，Mag 7 六月蒸发 $2T
- 核心信号：Great Rotation 加速 — 医疗/金融/消费必需 > 半导体/AI；Alpha#19/#53 反转+均值回复因子主导
- Top 5: LLY (9.0), UNH (9.0), JPM (8.5), GS (8.5), BRK.B (8.5)
- 板块分布：医疗 4 只, 金融 5 只, 半导体 4 只, 消费必需 3 只, 工业 2 只, 能源 1 只, 通信 1 只
- 核心变化 vs 06-16：风格从半导体 Risk-on 全面转向防御价值轮动
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-17] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-17)
- Summary: wiki/synthesis/2026-06-17/investment-daily.md
- 宏观焦点：FOMC 利率决议今日公布（市场预期不变）；美伊协议油价-5.8%；板块大轮动（科技→金融/工业/医疗）；Mag 7 六月已蒸发 $2 万亿
- 美股：SPY -0.55% / Dow +0.67% 创新高 / Nasdaq -1.15%（NVDA $200-250亿债券发行；AVGO/Q3指引miss持续发酵；ORCL RPO $6380亿但CapEx承压-11%）；SOX 6/5 暴跌 10% 后动量减弱
- AI 监管首例：美国商务部强制召回 Anthropic Fable 5/Mythos 5（$9650亿 IPO 推增加监管不确定性）
- 中概：BABA $112.69（1260H + 618监管双重压制，Jefferies 仍为 Top Pick）；BIDU 昆仑芯字节跳动采购叙事；PDD PE 8.5x 极端低估
- 港股：智谱 GLM-5.2 发布+32.8%（市值突破 HK$7000亿）；MiniMax 纳入恒生科技；恒生科技指数 AI 化转型加速
- A股：沪指-0.04%（缩量 1.21万亿）；AI 硬件分化（PCB/MLCC/光通信延续强势但降温）；6 只科技牛股集体辟谣"概念热炒脱离基本面"；电子+236亿/通信+121亿主力流入
- 新能源：中国四大 EV 厂全部发布自研智驾芯片（BYD 玄玑 A3/理想 Mach M100/蔚来神玑/小鹏图灵）；BYD 承担 NOA 事故全责；NIO 5月交付 37,705（+62.3%）
- AI 主题：SpaceX IPO $2.5万亿（Mag 7 资金外流）；Howard Marks "AI 投资更接近投机"；CapEx 大辩论白热化（Big4 $7000亿+）；DeepSeek 融资 $70亿
- 三大风险：FOMC 鹰派意外 / AI CapEx ROI 验证 / 1260H→CMIC 路径与被迫抛售
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-17] synthesis | Tech Report Digest — 大模型技术报告全面更新 (2026-06-17)
- New page: wiki/synthesis/2026-06-17/tech-report-digest.md
- Coverage: 22 家机构 40+ 份技术报告
- 新增重点：Claude Fable 5 / Mythos 5, AFM 3, GPT-5.5 Instant, Seed2.0 系列, Step 3.7 Flash, Mistral Medium 3.5, Qwen3.6-27B, Qwen3.5-Omni, Intern-S1-Pro, Step 3.5 Flash, Grok 4.1, DeepSeek-V4 完整规格
- 架构趋势归纳：MoE 全面主流化, Hybrid Mamba-Transformer 验证, RL for Reasoning 普及, 1M context 成为旗舰标配
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-17] synthesis | Conference Digest — Top ML/AI Conferences (2026-06-17)
- New page: wiki/synthesis/2026-06-17/conference-digest.md
- Coverage: 70+ papers across 12+ venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025)
- Frontier model reports: GPT-5.5 System Card, Claude Opus 4.7, DeepSeek-V4 Technical Report
- Key themes: RL for reasoning, generative recommendation at scale, agent systems explosion (465 ICML agent papers), diffusion LLMs, spatial VLMs
- Updated: wiki/index.md, wiki/log.md

## [2026-06-17] synthesis | arXiv Daily — AI, LLMs, CTR, Recommendation, Games, Sequential Modeling (2026-06-17)
- New page: wiki/synthesis/2026-06-17/arxiv-daily.md
- Coverage: 15 papers across LLMs (SPIRAL, NextFlow, FLARE, SDLM), CTR/Ads (IDProxy, CADET, FEDIN, Pinterest LLM, GenCTR), Games/RL (Game-RL, Strat-Reasoner, MARSHAL), Recommendation (OneRetrieval, UniVA), Sequential Modeling (Diffusion for TS)
- Key theme: Self-play and game-based RL as scalable reasoning pathway; generative paradigm converging with CTR/advertising

## [2026-06-16] synthesis | WorldQuant 101 Alpha — 美股 Top 20 (2026-06-16)
- New page: wiki/synthesis/2026-06-16/wq101-alpha-daily.md
- 宏观背景：美伊协议达成（油价 -4.8%）, FOMC 6/16-17 会议, NASDAQ +3.07% 领涨
- 核心信号：SOXX +5.45% 创新高, 半导体 Alpha#1/#6/#30 三重共振
- Top 5: ARM (9.5), MU (9.5), MRVL (9.0), WDC (9.0), AMD (8.5)
- 板块分布：半导体/AI 13 只, 存储 3 只, 其他 4 只
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-16] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-16)
- New page: wiki/synthesis/2026-06-16/game-rl-daily.md
- Coverage: 26 papers across Game RL (self-play, MARL, world models), Game AI Bots (LLM agents, NPCs), Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, Related Techniques
- Top picks: NitroGen (CVPR 2026, NVIDIA generalist gaming agent), SEMA (self-evolving multi-agent for StarCraft II), RetroAgent (dual intrinsic feedback RL), SkillRL (recursive skill library), GameNGen (ICLR 2025, diffusion game engine), GameArena (ICLR 2025, LLM reasoning via games), ProxyWar (ICSE 2026, game-based code evaluation)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-16] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-16)
- Summary: wiki/synthesis/2026-06-16/investment-daily.md
- 宏观焦点：FOMC 6/17-18 会议前夜；美伊协议达成（油价 -5.34%）；特朗普提议美国政府持有AI公司股权
- AI CapEx 辩论白热化：Big4 2026 CapEx $725B (+77% YoY)；Dell'Oro 预测 2026 数据中心 CapEx 超 $1 万亿；Janus Henderson 警告仅 53% 规划能建成
- 美股：NVDA $224.36 (GS $285 PT/+35%)；GOOGL $850 亿 equity raise（含 Berkshire $100 亿）；ORCL 财报后 -8%（FY27 $900B 指引但 CapEx 承压）
- 中概：BABA $113.49（6月 -9.18%，受 1260H 拖累）；BIDU ERNIE 5.1 #4 全球搜索榜；PDD PE 8.5x 极低估
- 港股：腾讯 WeChat AI 助手临近发布；智谱纳入恒生科技指数（6/15 生效）+14.95%；MiniMax +5.30%
- A股：6/12 核心指数年内最大调仓（AI/半导体/机器人获集中加码）；有色金属/商业航天/物理 AI 领涨
- AI 主题：Anthropic $965B IPO 推进（Claude Fable 5 发布）；OpenAI 筹备 IPO；SK hynix 8 月赴美上市；Anthropic/OpenAI/SpaceX 三大科技 IPO 同台
- 新能源：NIO CEO 预测中国汽车销量降 15-20%；BYD 董事长敦促耐心；宁德时代钠电池 2026 规模量产
- 人形机器人：宇树科技 73 天过会；NVIDIA Isaac GR00T；具身智能融资超 ¥345 亿
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-16] synthesis | Conference & arXiv Digest (NeurIPS 2025, ICML 2026, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, ACL 2026, EMNLP 2025)
- New page: wiki/synthesis/2026-06-16/conference-digest.md
- Coverage: 12+ conferences, 50+ highlighted papers across LLM/agents/CTR/recommendation/generative models/benchmarks
- Top highlights: D4RT (CVPR 2026 Best Paper), Gated Attention (NeurIPS 2025 Best Paper), ICLR 2026 Oral Papers (223), AAAI 2026 Outstanding Papers, Industry lab releases (Google DeepMind, OpenAI, Anthropic, Meta, NVIDIA, Alibaba)
- Key trends: Gated Attention standardization, Hybrid architectures (Mamba-Transformer), RL for LLM reasoning, Agent systems, Generative recommendation, On-device LLMs, 4D vision
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-15] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-15)
- New page: wiki/synthesis/2026-06-15/game-rl-daily.md
- Coverage: 29 papers across Game RL (self-play, MARL), Game AI Bots (LLM agents, NPCs), Foundation/World Models, PCG, Game Benchmarks, Industry Game AI, Related Techniques
- Top picks: SPIRAL (ICLR 2026, self-play for reasoning), MARSHAL (self-play multi-agent LLM reasoning), FAMOU (co-evolutionary LLM strategy evolution), lmgame-Bench, Orak (KRAFTON game benchmark), Agent World Model (ICML 2026, synthetic environments)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-15] synthesis | 投资日报 — 2026-06-15（美股/港股/A股/中概/新能源科技与AI热点）
- Summary: wiki/synthesis/2026-06-15/investment-daily.md
- 宏观焦点：FOMC 6/17-18 会议（CPI 4.2%→鹰派风险）；SpaceX 上市首日+19.3%；AI CapEx 大辩论白热化（Big4 $725B）
- 美股：NVDA -3.73%($200.42)；INTC +6.5%（Google/NVIDIA 18A 传闻）；ORCL -12%（RPO 创纪录但 $700 亿 CapEx 承压）；CBRS -5.5%（Cathie Wood 买跌）；SOX 6/5 单日 -10%；Microsoft 发 MAI 7 模型
- 港股：智谱/MiniMax 正式纳入恒生科技指数（6/15 起）；智谱市值从 HK$579 亿→HK$5,858 亿（+911%），启动科创板 150 亿 IPO；仙工智能 6/15-18 招股（"机器人大脑第一股"）
- 中概：BIDU -13%（1260H 名单重创）；BABA 6 连跌（1260H+618 监管）；AI 收入首超 Core 50%
- A股：具身智能融资超 ¥345 亿（宇树 73 天过会）；千寻智能 Spirit v1.6 登顶 RoboArena；内部人减持 ¥120 亿/周；智谱 150 亿科创板 IPO 推进
- 新能源：BYD 王传福喊话 5 年世界第一（出口+80%）；NIO 连续 2 季盈利；NEV 渗透率 62.9% 新高
- AI 主题：NVIDIA Alpamayo 2 Super、Nemotron 3 Ultra、Isaac GR00T 人形机器人；Alibaba RynnBrain 开源机器人模型；Anthropic Fable 5；DeepSeek 寻求 $70 亿融资
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-15] search | arXiv Paper Check — AI & CTR (June 15, 2026)
- New page: wiki/synthesis/2026-06-15/arxiv-paper-check.md
- Sources: cs.IR new (13 entries, Mon 15 Jun), cs.AI new + cs.LG new (Fri 12 Jun — latest weekday listings)
- Papers surveyed: 11 top picks (6 AI/LLM + 5 CTR/IR/Rec)
- Top picks: MiniMax Sparse Attention (28.4× compute reduction at 1M context), Agentic Monte Carlo (ICML 2026, SMC for black-box agent RL), PCAF (hash-bucket associative memory beats Transformer PPL), Reasoning as Pattern Matching (LLMs and humans both use pattern matching), LLM Reproducibility Assessment (96% agreement), Timeflies (observability + value joint forecasting), ADORE (retrieval-grounded query expansion), TASR (training-free adaptive retrieval stopping, KDD 2026), KGERMAR (KG-enhanced memory for long context), PAD (denoising × popularity bias interaction), ChronoID (temporal signals for generative rec)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-13] search | arXiv Daily — AI Research Survey (June 13, 2026)
- New page: wiki/synthesis/2026-06-13/arxiv-daily.md
- Coverage: 21 papers across LLM Efficiency (7), Attention & Sequence (2), E-Commerce Search (2), Recommendation & CTR (3), Games & Multi-Agent (3), IR & RAG (2), LLM Behavior (2)
- Top picks: MiniMax Sparse Attention (28.4x compute reduction at 1M context), Reversible Foundations (120B MoE on single 8-GPU node), OneRetrieval (Kuaishou editable generative retrieval, production), HiGR (Tencent hierarchical slate), Helmsman (RedNote ANNS 90% cost savings, OSDI'26), Boltzmann Attention (Ising attention mechanism), LENS (CTR interaction granularity)
- Sources: arXiv cs.AI, cs.CL, cs.LG, cs.IR, cs.GT (Jun 10-12 submissions)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-13] synthesis | 大模型技术报告摘要（2025-2026）
- New page: wiki/synthesis/2026-06-13/tech-report-digest.md
- Coverage: 19 家 AI 公司最新 Tech Report / System Card 综合摘要
- Companies: DeepSeek, OpenAI, Meta, Google, Anthropic, Mistral, Qwen, Yi, Microsoft, Apple, NVIDIA, xAI, Amazon, Zhipu, InternLM, Moonshot, StepFun, ByteDance, Baichuan
- Topics: 新架构 (MoE/Mamba/Hybrid), 训练方法, Scaling Law, 多模态, 长上下文, 推理模型
- Updated: wiki/index.md, wiki/log.md

## [2026-06-12] synthesis | 投资日报 — 2026-06-12（美股/港股/A股/中概/新能源科技与AI热点）
- Summary: wiki/synthesis/2026-06-12/investment-daily.md
- 美股：大盘强力反弹（Dow +930 pts/+1.86%，Nasdaq +2.54%，费半 +7.9%）；SpaceX IPO 今日上市（$135/股，$1.77T，2 周内从 Mag 7 抽血约 $2T）；Apple WWDC AI Siri 发布 + Google Cloud NVIDIA GPU 合作
- Mag 7/NVIDIA：NVDA 盘后 $206.01；从高点回落 -15% 后反弹；Q1 营收 $816B（+85%），$1,190 亿供货承诺；Apple 背书 NVIDIA GPU
- 港股：腾讯 WeChat AI Agent 推动 6 月 2 日 +10.46%（$532 亿市值增）；$46.6 亿双币债券超额认购 3.6 倍；阿里 618 监管冲击 -5.4% + 1260H 名单
- 中概/ADRs：BABA -5.3%/JD -3%/PDD -1.5%（618 监管执法），BIDU -2.1%（1260H 名单 + 广告 -29%）
- A 股：寒武纪 A 股股王（Q1 净利 +185%，高盛目标 2,406 元），国产芯片 41% 市占率，字节 800 亿/阿里 1,260 亿 AI 芯片采购
- 新能源：比亚迪全球出口 160,644（+80%），王传福喊话 5 年世界第一；蔚来 37,705（+62.3%）创新高；NEV 渗透率 66.7% 新高
- AI 主题：全球 DC CapEx >$1T；三大 IPO（SpaceX/OpenAI/Anthropic）；特朗普会见 AI 高管；CPI 4.2% → 加息风险；1260H 名单扩至 188 家
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-13] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-13)
- Summary: wiki/synthesis/2026-06-13/wq101-alpha-daily.md
- Market context: SpaceX IPO首日+19%（$161.11, $1.9T市值）；美伊和谈可能周日签署（瑞士）；S&P 500 +0.50%至7,431；VIX 17.68持续下降；Russell 2000 YTD +40.2%领跑
- 板块轮动：AI/半导体反弹（AMD +4.7%, MRVL纳入S&P 500）+ 能源受和平协议预期承压 + 消费必需品走强
- Top picks: MRVL (9/10), NVDA (9/10), AMD (9/10), AVGO (8/10), GLW (8/10)
- 核心因子有效性：Alpha#53（反转）> Alpha#1（动量）> Alpha#41（趋势强度）
- 关键变化vs 06-12：新增AMD/AAPL/COP/LMT/WMT；存储权重下调；AI半导体反转信号确认
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-12] synthesis | WorldQuant 101 Alpha 精选 — 美股 Top 20
- Summary: wiki/synthesis/2026-06-12/wq101-alpha-daily.md
- 市场背景：Dow +930pts (+1.86%)，Nasdaq +2.54%，S&P +1.75%；特朗普伊朗外交信号驱动风险偏好
- 板块轮动：AI/半导体 → Healthcare/Financials/Value 持续
- Top picks：MU (9/10), DELL (9/10), SNDK (8/10), GS (8/10), AVGO (8/10)
- 核心因子有效性：Alpha#41（趋势强度）> Alpha#1（动量）> Alpha#30（波动率）> Alpha#53（反转）
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-13] synthesis | 投资日报 — 2026-06-13（美股/港股/A股/中概/新能源科技与AI热点）

## [2026-06-13] synthesis | arXiv Daily — 2026-06-13
- Summary: wiki/synthesis/2026-06-13/arxiv-daily.md
- New: 16 papers covering LLM architectures (MSA, PCAF, MaxProof, Select & Improve, SWITCH), recommendation/CTR (OneRetrieval, GenAIR, AIR, Mult-DPO, DiffCold, LLM Personas, τ-Rec, Representation Curriculum), RL/multi-agent/games (DoorDash MARL, competitive search game theory), and tool use (ToolSense)
- Summary: wiki/synthesis/2026-06-13/investment-daily.md
- 美股：三大指数周线收涨；SpaceX 上市首日 +19.34%（$161，史上最大 IPO $750 亿）；Adobe -7%（AI Freemium 压制 ARR）；Mag 7 涨跌互现
- A 股：沪指 +1.12% 站上 4000 点，成交 3.21 万亿放量 6629 亿；有色金属 +6.32%（钨/钼涨价），商业航天（SpaceX 映射），大金融走强；半导体材料获利了结
- 港股：腾讯 Q1 AI 驱动收入 +9%，CapEx 环比 +84%；阿里云 +40% AI 收入占比 30%；国产算力链受益 CapEx 提升
- 中概：BIDU +1.69%/NTES +1.71% 领涨；NIO -3.12%/LI -2.89% 回调；板块分化加剧
- 新能源：5 月 NEV 渗透率 56.9%，出口 +68.7%；宁德时代主力净流入 19.74 亿
- AI 主题：SpaceX IPO 落地；全球数据中心 CapEx $750B+；半导体市场预计 $1.51T；AI IPO 超级周期（OpenAI/Anthropic 排队）；美伊缓和油价大跌
- Updated: wiki/index.md, wiki/log.md

## [2026-06-12] synthesis | Tech Report Digest — 2026-06-12 (第十一版)
- New page: wiki/synthesis/2026-06-12/tech-report-digest.md
- Coverage: 19 家机构, 40+ 技术报告/System Card
- DeepSeek: V4 Model Card, R1 (arXiv:2501.12948), V3 (arXiv:2412.19437)
- OpenAI: GPT-5.5 System Card (2026-04), GPT-5 System Card (arXiv:2601.03267), o3 System Card (2025-04)
- Meta: Llama 4 Scout/Maverick/Behemoth (2025-04, MoE, 10M context)
- Google DeepMind: Gemini 3.1 Pro Model Card, Gemini 2.5 Technical Report, Gemini Embedding 2
- Anthropic: Claude Opus 4 & Sonnet 4 System Card, 4.5/4.6/4.7/4.8/Fable 5/Mythos 5
- Mistral: Medium 3.5, Magistral (arXiv:2506.10910), Large 3
- Qwen: Qwen3 (arXiv:2505.09388), Qwen3.5-Omni, Qwen3.6-35B-A3B
- Microsoft: Phi-4 (arXiv:2412.08905), Phi-4-Reasoning (arXiv:2504.21318), Phi-4-reasoning-vision (arXiv:2603.03975)
- Apple: AFM Tech Report 2025 (arXiv:2507.13575) — On-device ~3B + Server PT-MoE
- NVIDIA: Nemotron 3 Ultra (MoE + Hybrid Mamba-Transformer), Nemotron 3 Super (arXiv:2604.12374), Llama-Nemotron (arXiv:2505.00949)
- xAI: Grok 4/4.1/4 Fast Model Cards
- Amazon: Nova 2 (2025-12), Nova Premier (2025-04)
- Zhipu AI: GLM-5 (arXiv:2602.15763, 744B-A40B)
- Moonshot AI: Kimi K2 (arXiv:2507.20534), K2.5 (arXiv:2602.02276), Kimi Linear (arXiv:2510.26692)
- ByteDance: Seed 2.0 Model Card, Seed1.5-VL (arXiv:2505.07062)
- Shanghai AI Lab: Intern-S1 (arXiv:2508.15763), Intern-S1-Pro (arXiv:2603.25040), InternLM3-8B
- StepFun: Step3 (arXiv:2507.19427), Step-DeepResearch (arXiv:2512.20491), StepAudio 2.5
- 01.AI: Yi-Lightning (arXiv:2412.01253), Yi (arXiv:2403.04652)
- Baichuan: Baichuan-Omni (arXiv:2410.08565), Baichuan-M1 (arXiv:2502.12671)
- Key trends: MoE 主导, Hybrid Mamba-Transformer 崛起, 推理模型成为标配, 多模态原生集成, Agentic 竞争白热化
- Updated: wiki/index.md, wiki/log.md

## [2026-06-12] synthesis | Game RL & Game AI Bot — Daily Synthesis (2026-06-12)
- New page: wiki/synthesis/2026-06-12/game-rl-daily.md
- Coverage: 61 papers across 8 categories — Game RL (10), Game AI Bots (12), Game Foundation Models (4), Procedural Content Generation (8), Game Benchmarks (8), Industry Game AI (4), World Models (9), Related Techniques (6)
- Top papers: STRATAGEM (game self-play for math reasoning), FAMOU (co-evolution for MCTF, AAMAS 2026 winner), AVACraft (VLM zero-shot StarCraft II 75-90%), WorldCam (camera-pose world models), NVIDIA IGI SDK (on-device game inference), SMAC-HARD/HLSMAC (next-gen StarCraft benchmarks), π-Play (privileged self-distillation)
- Key trends: self-play+RL convergence for LLM reasoning, MARL benchmarks evolving beyond SMAC, on-device game AI maturing (NVIDIA IGI, Arm Neural Dawn), co-evolution for open-ended learning, multiplayer world models (Solaris), PCG goes multi-modal
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-12] synthesis | Conference Digest — 2026-06-12
- New page: wiki/synthesis/2026-06-12/conference-digest.md
- Coverage: 17 sections across 12+ venues (ICLR 2026 Outstanding Papers, ICML 2026, AAAI 2026, CVPR 2026, NeurIPS 2025, KDD 2025/2026, EMNLP 2025, ACL 2026, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025)
- ICLR 2026 Outstanding: Transformers Succinctness, Multi-Turn LLM Degradation, Mamba-3, AgentFlow (7B beats GPT-4o)
- ICML 2026: MEMO multi-agent games, Curriculum tree-reasoning provable complexity, 6,352 accepted
- CVPR 2026: 16,092 submissions (+24%), NitroGen gaming agents, Apple 14 papers
- SIGIR 2026: 90 RecSys papers, LLM Rec dominates, cross-domain & generative rec surge
- WWW 2026: NEZHA (Taobao 100M DAU, ¥10B GMV), AgentDR, FeDecider
- CTR/Advertising: HyFormer (ByteDance), GR4AD (Kuaishou 400M users), TencentGR-1M/10M
- Agent Systems: AlphaEvolve (DeepMind), MCMA meta-cognitive memory, KAIROS, OpenAI o1 System Card
- Generative Models: DiT with Representation Autoencoders, PixelDiT, SeedVR2
- Key trends: inference-first architecture, generative recommendation replacing cascaded pipelines, test-time compute scaling, SSMs competitive with Transformers
- Updated: wiki/index.md, wiki/log.md

## [2026-06-12] search | arXiv Paper Check — AI & CTR (June 12, 2026)
- New page: wiki/synthesis/2026-06-12/arxiv-paper-check.md
- Sources: Fri 12 Jun 2026 — cs.AI (86 new), cs.IR (7 new, 4 cross, 12 replacements), cs.LG (121 new)
- Papers surveyed: ~20 top picks
- AI/LLM highlights: Pythagoras-Prover (4B beats DeepSeek-Prover-V2-671B at theorem proving), Arbor (tree search cognition for agents, 193% LLM inference gain), From AGI to ASI (DeepMind), Prefill Awareness (models detect tampered outputs), MLUBench (ICML 2026 MLLM unlearning), SciAgentArena (science agent benchmark), Boltzmann Attention (Ising attention mechanism), LoRA-α optimization theory, Zero-source hallucination detection (ICML 2026)
- CTR/Rec highlights: OneRetrieval (Kuaishou editable generative retrieval, production), Helmsman (RedNote ANNS 90% cost saving, OSDI'26), CQC-RAG (cross-query consistency for robust RAG), AdaGRPO (adaptive GRPO for generative rec), HiGR (Tencent hierarchical slate, production), LENS (CTR interaction granularity)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-11] synthesis | 投资日报 — 2026-06-11（美股/港股/A股/中概/新能源科技与AI热点）
- Summary: wiki/synthesis/2026-06-11/investment-daily.md
- 美股：AI/半导体技术性调整（S&P 500科技板块-11%正式进入回调区）；Oracle财报今夜揭晓（$5530亿RPO验证AI需求）；SpaceX IPO明日上市（$135/股，$1.75万亿，~4%流通量）；Super Micro $70亿融资-28%；CPI +4.2%符合预期
- Mag 7分化：GOOGL YTD +28%领跑（云+63%）；MSFT/META受CapEx压制；AAPL Siri AI褒贬不一
- 中概/港股：Pentagon 1260H清单冲击（Alibaba/Baidu/BYD/NIO/CATL等）；天数智芯港股上市+31.5%（国产GPU四小龙齐上市）；澜起科技H股+57%（DDR5互连芯片）；快手可灵AI全球用户破1亿
- A股：AI应用杀跌/CPO光通信逆市活跃；海光信息+7%（深算4号进展）；半导体设备高景气（北方华创订单至2027）
- 新能源：比亚迪王传福喊话"低估"（出口+85.5%）；蔚来月交付创新高+37,705(+62.3%)；EV股集体52周新低
- AI主题：三大超级IPO（SpaceX/OpenAI/Anthropic）、Anthropic Fable 5发布、微信AI生态开放、Google×Intel 300万TPU订单、TSMC产能紧张推动代工格局变化
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-11] synthesis | Game RL & Game AI Bot — Daily Synthesis (2026-06-11)
- New page: wiki/synthesis/2026-06-11/game-rl-daily.md
- Coverage: 69 papers across 7 categories — Game RL (16), Game AI Bots (16), Game Foundation Models (7), Procedural Content Generation (8), Game Benchmarks (8), Industry Game AI (1), Related Techniques (13)
- Top papers: NitroGen (CVPR 2026, NVIDIA), Game-TARS (500B token pre-training), MARL-GPT (multi-task MARL foundation model), STRATAGEM/SPIRAL (game self-play for LLM reasoning), GameWorld/OmniGameArena (standardized benchmarks)
- Key trends: convergence of RL and foundation models, generalist game agents at scale, world models as unifying framework, co-evolution for open-ended learning, PCG goes multi-modal, benchmark standardization, industry deployment matures (NVIDIA ACE + NVIGI)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-11] search | arXiv Daily — AI Research Survey (June 11, 2026)
- New page: wiki/synthesis/2026-06-11/arxiv-daily.md
- Coverage: 17 papers across LLM/Architecture (6), Agentic RL & Reasoning (2), CTR/Advertising (1), Recommendation (5), Ranking/Allocation (1), Games (2)
- Top picks: CADET (decoder-only CTR @ LinkedIn), AIR (LLM cross-domain rec @ Kuaishou), Gryphon (item-level scoring for generative retrieval), APPO (fine-grained agentic RL), Bebop (MTP acceleration for RL), nD-RoPE (generalized position embedding)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-11] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-11)
- New page: wiki/synthesis/2026-06-11/wq101-alpha-daily.md
- Market context: S&P 500 -0.98%, Nasdaq -1.54%, sector rotation AI→Healthcare/Energy/Industrials; CPI 4.2%; oil ~$97 (Iran conflict)
- Selected 20 stocks across 6 sectors: Healthcare (UNH/LLY/JNJ/GILD), Energy (XOM/CVX/OXY/COP), Industrials (CAT/GEV/FIX), Technology (NVDA/MRVL/AMD/INTC), Financials (GS/JPM), Consumer Staples (WMT/COST/PG)
- Top 3 picks: UNH (Alpha#12, 9/10), XOM (Alpha#1/#30, 9/10), CAT (Alpha#41, 8.5/10)
- Key factor: rotation momentum captured via Alpha#12 (volume-price divergence) and Alpha#1 (12-month momentum)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-10] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-10)
- New page: wiki/synthesis/2026-06-10/wq101-alpha-daily.md
- Applied Alpha#1/#6/#12/#19/#30/#41/#53 across 7 dimensions
- Market context: US-Iran conflict escalation, CPI data day (YoY +4.2% expected), AI trade selloff continues, VIX 19.87 (+5.02%), Oil ~$89 (+1.02%)
- Top picks: ORCL(9), XOM(9), LMT(9), JNJ(9), CVX(8), RTX(8), JPM(8), BAC(8), LLY(8), NVDA(8), GOOGL(8)
- Sectors: 3 Energy, 3 Defense, 4 Financials, 3 Healthcare, 3 Tech, 2 Consumer Defensive, 2 AI Infrastructure
- Key shift vs 06-09: Energy/Defense/Healthcare dominate (geopolitical risk-off), AI/Technology underweight (CPI fear + trade unwind)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-10] synthesis | 投资日报 — 2026-06-10（美股/港股/A股/中概/新能源科技与AI热点）
- Summary: wiki/synthesis/2026-06-10/investment-daily.md
- 美股：SpaceX IPO（$135/股，$1.77万亿，本周五上市）；OpenAI 秘密提交 S-1（$8,520亿估值）；Anthropic 秘密提交 S-1 + Claude Fable 5 发布（$9,650亿估值）；Apple WWDC Siri AI 发布；Super Micro $70亿融资（盘后-9%）；Marvell 加入 S&P 500 (+10%)；Citi 将 S&P 500 目标上调至 8,100
- 全球科技：Broadcom 财报引发上周五 AI 抛售后，本周全球科技股反弹（韩国 KOSPI +8%）；亚洲芯片股 SK Hynix +6.44%，Tokyo Electron +5.65%
- 中概/港股：中国 5 月 PPI +3.9%（近四年新高，AI 投资拉动），CPI +1.2%（miss）；出口 +19.4%；腾讯/阿里/美团 AI 驱动
- A股：光模块（中际旭创）、半导体设备（北方华创）、国产算力（寒武纪/海光信息）持续高景气
- 新能源：比亚迪出口高增长；宁德时代 AI 储能新需求；特斯拉 Robotaxi 持续推进
- AI 主题：AI IPO 三重奏（SpaceX/OpenAI/Anthropic）、推理芯片竞争（D-Matrix Corsair 投产）、AI 数据中光互联（Corning-Amazon 协议）、JPMorgan AI Agent 部署
- Updated: wiki/index.md (Synthesis section), wiki/log.md

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

## [2026-06-10] search | Game RL & Game AI Bot — Daily Survey (initial)
- New page: wiki/synthesis/2026-06-10/game-rl-daily.md
- Coverage: 20 papers across Game RL (5), Game AI Bot (4), Game Foundation Models (3), PCG (2), Game Benchmarks (3), World Models (2), Related Techniques (2)
- Top picks: NitroGen (CVPR 2026 Oral, NVIDIA), SPIRAL, MARSHAL, GROW, Orak, Matrix-Game, PCGRLLM
- Updated: wiki/index.md, wiki/log.md

## [2026-06-11] synthesis | Game RL & AI Bot — expand & reorganize (~41 papers)
- Updated: wiki/synthesis/2026-06-10/game-rl-daily.md (20 → ~41 papers)
- New papers added: Dreaming in Code (curriculum learning via world models), EAWM (event-aware world model), CDE (curiosity exploration), WOMBET (experience transfer), HiPER (hierarchical RL), STEP-HRL (HRL+language feedback), Voyager (Minecraft agent), AWM (infinite synthetic environments), Galileo (VLM agent), Competition & Cooperation of LLM Agents, Towards Generalist Game Players, IPCGRL (language-instructed PCG), PANGeA (narrative PCG), CrawLLM (asset generation), BALROG (ICLR 2025 Spotlight), GameWorld (NUS/Oxford), VideoGameBench (retro games VLM), OfflineMania (EA SEED), MuDreamer (reconstruction-free world model), Unity ML-Agents, Search Self-Play (ICLR 2026), Self-RedTeam
- New sections added: Industry perspective (Unity ML-Agents), Summary statistics & trends
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

## [2026-06-10] synthesis | Tech Report Digest (第九版) — 2026-06-10
- New page: wiki/synthesis/2026-06-10/tech-report-digest.md
- Coverage: 22+ organizations, 35+ reports
- Highlights: DeepSeek V4 CSA/HCA attention, GPT-5 thinking+router, Claude Opus 4.8 (SWE-bench Pro 69.2%), Gemini 3.1 Pro (ARC-AGI-2 77.1%), Qwen3/3.6 thinking/non-thinking unified, Mistral Large 3 (675B MoE, Apache 2.0), Nemotron 3 Ultra (550B hybrid Mamba-Attention), GLM-5.1 (8h autonomous agent), Kimi K2.6 (1.1T MoE, MuonClip), Seed 2.0, Grok 4.3, Amazon Nova Premier, Llama 4, Phi-4, Apple AFM v2, InternLM3, Yi, Baichuan, StepFun
- Six directions: architecture (MoE/Mamba/hybrid), training (Muon/async RL/distillation), scaling law, multimodal, long context (1M~10M), reasoning models (thinking modes)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-10] synthesis | Conference Digest — 2026年AI/ML顶级会议论文全景
- New page: wiki/synthesis/2026-06-10/conference-digest.md
- Coverage: 13 venues (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, ACL/EACL 2026, EMNLP 2025, KDD 2026, SIGIR 2026, WWW 2026, RecSys 2025) + arXiv industry papers
- Sections: 18 categories spanning LLM architecture, diffusion, agents, CTR prediction, games, SSMs, recommendation systems, RL, alignment, efficiency
- Best papers covered: Gated Attention (NeurIPS), 1000-Layer SSL RL (NeurIPS), Why Diffusion Don't Memorize (NeurIPS), D4RT (CVPR Best), O-Voxel (CVPR Best Student), Learning Unmasking Policies (ICML Oral), Transformers are Succinct (ICLR Outstanding), Polar Express (ICLR HM)
- Industry CTR papers: CADET (LinkedIn), EST (Alibaba), GRAB (Baidu), LoopCTR (Alibaba), GR4AD (Kuaishou), TokenMixer-Large (ByteDance), HeMix (AMAP), RankUp (Tencent), S-GRec (Tencent), SparseCTR, HyFormer (ByteDance), DAIAN
- AI labs: Google DeepMind, Meta FAIR, OpenAI, Anthropic, NVIDIA, Microsoft Research, Apple, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, LinkedIn, Pinterest, Walmart, Amazon, Spotify
- Updated: wiki/index.md, wiki/log.md

## [2026-06-10] synthesis | Game RL & Game AI Bot Daily — 2026-06-10
- New page: wiki/synthesis/2026-06-10/game-rl-daily.md
- Coverage: 81 papers across 8 categories — Game RL/MARL/self-play (16), Game AI Bots (9), Game Foundation Models (7), PCG (12), Benchmarks (7), Industry Game AI (6), World Models (10), Curiosity/HRL/Imitation/IRL (14)
- Key papers: NitroGen (CVPR 2026, NVIDIA), Game-TARS (Tencent, 500B tokens), Odysseus (VLM+PPO 100+ turns), SPIRAL (self-play reasoning transfer), MARSHAL (self-play MARL for LLMs), Matrix-Game (17B world model), Orak (KRAFTON benchmark), Continual Harness (Google DeepMind Pokémon), Pareto Distillation (Tencent HoK mobile)
- Key themes: self-play going open-ended, foundation models as generalist game agents, RL for VLM agents, MARL+LLMs cross-pollination, industry deployment maturing, PCG meets LLMs, world models becoming real-time
- Updated: wiki/index.md, wiki/log.md

## [2026-06-11] arxiv-daily | arXiv Daily — AI Research Survey (June 11, 2026)
- Summary: wiki/synthesis/2026-06-11/arxiv-daily.md
- Coverage: ~30 papers across 8 categories — LLMs & Architectures (4), RL & Games (4), Recommendation & CTR (5), Sequential Modeling (2), Agents & Multi-Agent (4), Information Retrieval & RAG (3), Science of AI & Safety (3), Notable Mentions (6)
- Key papers: RoVE (position-aware value pathway), SWARR (RL for sliding-window attention), DiffCold (diffusion for cold-start recommendation), LLM-Based User Personas (Google-scale), INFRAMIND (infrastructure-aware multi-agent), Behavior Forecasting (bypassing explanations)
- Key themes: RL for architecture adaptation, infrastructure-aware agent orchestration, generative recommendation maturing, quantization limits on retrieval, calibration drift under reasoning
- New page: wiki/synthesis/2026-06-11/arxiv-daily.md

## [2026-06-11] search | arXiv Paper Check — AI & CTR (June 11, 2026)
- New page: wiki/synthesis/2026-06-11/arxiv-paper-check.md
- Surveyed: cs.AI (199 new entries) + cs.IR (19 new entries) — Thu 11 Jun 2026
- AI highlights (11): Impossibility of Eliciting Latent Knowledge (alignment theory), MoE Manifold Power Iteration (routing), Architecture-Aware RL for Sliding-Window Attention, SVoT (spatial reasoning + RL), TreeSeeker (tree-structured deep search), Can AI Agents Synthesize Scientific Conclusions?, ATLAS (active theory learning), APPO (agentic procedural RL), Hippocampal Memory for AGI (ICML position), Search Discipline for Research Agents, Forecasting Future Behavior
- CTR/Rec highlights (7): DiffCold (diffusion for cold-start rec, ECML-PKDD), LLM-Based User Personas at Scale (Google), Tail-Aware Adaptive-k for RAG (ECML-PKDD), CORE-Bench (code retrieval benchmark), CompRank (token-compressed reranking), Quantization Limits on Dense Retrieval (theory), FAST-MEL multimodal entity linking (SIGIR)
- Key themes: RL for reasoning convergence, alignment theory maturing, LLM+recommendation convergence, efficient retrieval, rigorous agent evaluation
- Updated: wiki/index.md, wiki/log.md

## [2026-06-11] synthesis | Conference & arXiv Digest — June 2026
- New page: wiki/synthesis/2026-06-11/conference-digest.md
- Coverage: 14 sections across 12+ venues (ICLR 2026 Oral highlights, AAAI 2026, CVPR 2026, ICML 2026, NeurIPS 2025, KDD 2026, EMNLP 2025/ACL 2026, RecSys 2025/CIKM 2025)
- Architecture: Mamba-3 (ICLR 2026 Oral with 7× speedup), NVIDIA Nemotron 3 Ultra (550B MoE), Inception Mercury dLLMs
- LLM Reasoning: Curriculum-based RL (provable sample complexity), test-time compute scaling
- Agent Systems: AgentFlow (7B beats GPT-4o), AMC (black-box agent RL), KAIROS, Agent Security vulnerabilities
- Recommendation/CTR: CADET (LinkedIn - 11.6% online CTR), ByteDance TokenMixer-Large (15B params), Netflix GenRec scaling laws, Kuaishou OneRec/GRLM, TencentGR datasets
- Industry labs: Google DeepMind (Gemini 3.5/Omni/Gemma 4), OpenAI (o3/S-1), Anthropic (Claude Fable 5/S-1), Meta (Llama 4), NVIDIA (Nemotron 3), ByteDance (Douyin/TokenMixer), Alibaba (Large User Model), Tencent (TencentGR), Kuaishou (OneRec/GRLM), Netflix (GenRec), Apple (14 @ CVPR 2026)
- Key shifts: inference-first architecture design, generative recommendation replacing cascaded pipelines, SSMs competitive with Transformers, open-weight frontier models
- Updated: wiki/index.md, wiki/log.md

## [2026-06-11] synthesis | Tech Report Digest — 第十版 (2026-06-11)
- New page: wiki/synthesis/2026-06-11/tech-report-digest.md
- Coverage: 22+ organizations, 40+ technical reports/system cards
- Highlights: DeepSeek V4 (1.6T MoE, CSA/HCA, Muon Optimizer) + R1/V3, OpenAI GPT-5/o1 System Cards, Meta Llama 4 (Scout 10M context), Google Gemini 2.5/3.1/3.5 reports, Anthropic Claude Opus 4/4.6/4.7/4.8/Mythos System Cards, Mistral Large 3 (675B MoE), Qwen3.5/3.6/3.7 Max, Microsoft Phi-4 (+reasoning variants), Apple AFM 2025 (PT-MoE), NVIDIA Nemotron 3 (Hybrid Mamba-Transformer), xAI Grok 4/4.1/4.20/4.3, Amazon Nova/Nova 2, Zhipu GLM-5/5.1, Kimi K2/K2.5/K2.6 (MuonClip), ByteDance Seed 1.8/2.0, Step 3.5 Flash, InternLM2/3, Yi, Baichuan
- Key themes: MoE domination, Hybrid Mamba-Transformer (Nemotron 3), Hybrid Attention CSA/HCA (DeepSeek V4), 10M context windows (Llama 4 Scout), configurable thinking modes, Muon/JumpCLIP optimizer innovation, early fusion multimodal (Llama 4/Qwen3.5), full open weight/open data movement (Nemotron 3 OpenMDW, GLM-5 MIT)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-12] synthesis | arXiv Daily
- Page: wiki/synthesis/2026-06-12/arxiv-daily.md
- Coverage: 75 papers across LLMs, CTR/Advertising, Recommendation Systems, Sequential Modeling, Time Series, Games & RL, Agentic AI
- Updated: wiki/index.md

## [2026-06-13] synthesis | arxiv-paper-check | AI & CTR
- New page: wiki/synthesis/2026-06-13/arxiv-paper-check.md
- Saturday — no new arXiv submissions. Covers the Fri Jun 12 batch with additional LG highlights not in the previous report
- Highlights: RoVE (rotary value embeddings → attentive convolution), FlowBank (query-adaptive workflow optimization), BlendIn (inference-time alignment), OneRetrieval (Kuaishou editable generative retrieval), Helmsman (RedNote ANNS, 90% cost savings), HiGR (Tencent slate recommendation), Strategic Decision Support for AI Agents
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-13] synthesis | Conference Digest — 2026-06-13 全面版
- New page: wiki/synthesis/2026-06-13/conference-digest.md
- Coverage: 12 sections across 12+ venues (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) + arXiv GRPO training advances
- ICML 2026: CausalDPO (OOD generative rec +24.1%), ML-Agent (7B beats GPT-5 on ML), SciAgentGym, HyperAgents, 465 agent-related papers
- AAAI 2026: MoMoREC (Alibaba multi-agent motivation), TreeBridge (Shopee GMV +1.55%), Align³GR (Kuaishou +17.8%/20.2%), STARec (0.4% data SOTA)
- NeurIPS 2025: RecZero (GRPO for autonomous reasoning rec), R²ec (dual-head reasoning+rec), IGD (token IG for rec), TagCF (MLLM+LLM logic, +0.946% engagement), RecPIE, ORBIT benchmark
- ICLR 2026: T³ (belief deviation truncation, +30pp), ExpA (expanded action space EARL), MedAgentGym (+43~45% RL), MemAgent, Agent Proving
- KDD 2026: FAT (Field-Aware Transformer +4.38% AUC), FCN (exponential+linear cross), GR4AD (Kuaishou ads revenue +4.2%), OneRanker (Tencent GMV +1.34%), HAP (ByteDance pre-ranking), KLAN (Kuaishou DAU +0.205%), OneMall (GMV +4.9~14.7%)
- CVPR 2026: TWIG (thinking-while-generating), Thoughtful3D (CoT for 3D generation), Gen3R, PartDiffuser, Scone, SenseSearch
- EMNLP 2025: AgentPro (MCTS + PRM, +6.32% HotpotQA), ManuSearch, Preemptive Detection, IPIGuard, Search-o1, LMR-BENCH
- SIGIR 2026: SIGMA (AliExpress multi-task GR), GenRec (GRPO-SR), GFlowGR (4% revenue lift), ItemRAG, BEAR, SPRINT
- WWW 2026: ThinkRec (thinking-based rec), AgentDR (2× improvement), ISRF, SEDIRec, IAM, DualGR, HAP
- CIKM 2025: Climber (NetEase, +12.19% lift), STARec, Prompt Tuning for user profile
- RecSys 2025: Best Paper (Conformal Risk Control for unwanted rec), RESA, LONGER
- arXiv GRPO: Predictive Scaling Laws (80% epoch saturation), Prompt Augmentation, MT-GRPO (+16~28% worst-task), GRPO-VPS (+2.6pp), Latent-GRPO (3-4× shorter chains), iGRPO (AIME24 85.62%), GDRO-DRPO (+10.6%)
- Key trends: GRPO as core reasoning training paradigm, RecSys entering "reasoning era", Agent systems shifting to learning paradigm, game RL feeding back to LLM reasoning, multimodal generation with integrated reasoning, CTR shifting from deeper-to-structured expressivity
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-13] synthesis | Game RL & Game AI Bot — Daily Synthesis (2026-06-13)
- New page: wiki/synthesis/2026-06-13/game-rl-daily.md
- Coverage: 58 papers across 8 categories — Game RL (10), Game AI Bots (11), Game Foundation Models (5), Procedural Content Generation (8), Game Benchmarks (8), Industry Game AI (5), World Models (4), Related Techniques (7)
- Top papers: GARL (game-theoretic RL for multi-agent prioritization, Jun 2026), PopuLoRA (Vmax, co-evolving populations for self-play RLVR), NitroGen (CVPR 2026 Oral, NVIDIA, 40K hours/1K+ games), Dreamer 4 (Minecraft diamonds from offline data), AsyncWebRL (2.9× speedup for multi-step RL), World Models survey (2606.00133), FlowTracer (token-level credit assignment)
- Key trends: self-play+RL convergence for LLM reasoning as primary paradigm, generalist game agents (NitroGen), industry RL deployment accelerating (NVIDIA ACE, Sony GT Sophy, EA FC 26), world models as unifying framework, PCG becomes multi-objective/multi-modal, benchmark standardization (GameWorld/lmgame-Bench), agentic RL infrastructure matures, co-evolution for open-ended learning
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-15] conference-digest | 顶会论文专题报告 — 2026年6月全面版（NeurIPS 2025 Best / ICLR 2026 Outstanding / ICML 2026 / AAAI 2026 / CVPR 2026 Best / EMNLP 2025 / KDD 2026 / RecSys 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / ACL 2026）
- New page: wiki/synthesis/2026-06-15/conference-digest.md
- Coverage: 12+ venues, 100+ papers, 13 labs
- Highlights:
  - NeurIPS 2025 Best: Gated Attention (Alibaba Qwen, attention sink elimination), Artificial Hivemind (UW/CMU/AI2, LLM homogeneity), 1000-Layer RL (CMU/Google, 20-50x RL depth scaling)
  - ICLR 2026 Outstanding: LLMs Get Lost in Multi-Turn (Microsoft Research, 39% multi-turn drop), Mamba-3 (CMU/Princeton/Stanford, SSM Pareto frontier)
  - CVPR 2026 Best: D4RT (Google DeepMind, dynamic 4D scene reconstruction), O-Voxel (Microsoft/Tsinghua, 3D structured latents)
  - ICML 2026: CADET (LinkedIn, decoder-only ads CTR, 11.8% lift), 6,352 accepted papers
  - KDD 2026: OneMall (Kuaishou generative rec), PROMISE (process reward models), DOS (Meituan semantic IDs)
  - RecSys 2025: Generative recommendation paradigm, semantic ID revolution
  - AAAI 2026: ToxiAlert-Bench (audio toxicity), 29K submissions, AutoMalDesc
  - EMNLP 2025: Speculative Streaming (Apple), CodeArena (Alibaba), value-action gap
  - CIKM 2025: AGENTiGraph (95.12% KG interaction), HealthGenie
  - ACL 2026: Theme — "Explainability of NLP Models"
  - arXiv: Self-Harness (agents auto-improve, 52.6% gain), ExpGraph (Meta self-evolving graph memory), ALE (UC Berkeley, 2.6% agent pass rate), EvoArena, Agentic Monte Carlo
- Industry labs: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba/Qwen, Tencent, Kuaishou, NVIDIA, Anthropic, Apple, Amazon, Baidu
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-15] synthesis | 大模型技术报告摘要（2025-2026）— 2026-06-15 更新版
- New page: wiki/synthesis/2026-06-15/tech-report-digest.md
- Coverage: 20 家 AI 公司最新 Tech Report / System Card 综合摘要
- Companies: DeepSeek, OpenAI, Meta, Google, Anthropic, Mistral, Qwen, Microsoft, Apple, NVIDIA, xAI, Amazon, Zhipu, InternLM, Moonshot, StepFun, ByteDance, Yi, Baichuan
- Topics: MoE/Mamba/Hybrid 架构, 训练方法, Scaling Law, 多模态, 长上下文, 推理模型
- Updated: wiki/index.md, wiki/log.md

## [2026-06-15] arxiv-daily | arXiv Daily — AI Research Survey (June 15, 2026)
- New page: wiki/synthesis/2026-06-15/arxiv-daily.md
- Coverage: 14 papers across AI Alignment & Safety (2), CTR & Advertising (3), Recommendation Systems (3), IR & RAG (2), RL & Games (1), LLM Agents (2)
- Top picks: DS-MLP (Renmin Univ, SOTA CTR with vanilla MLP), UniVA (Tencent WeChat, 1.5% GMV lift via generative rec value alignment), Generalization Hacking (Anthropic, models resist RL behavioral modification), DiffCold (SJTU, diffusion-based cold-start, ECML-PKDD 2026), LLM-Based Personas (Google, billion-scale real-time user persona generation)
- Sources: arXiv cs.IR, cs.LG, cs.CL, cs.AI, cs.CR (May-Jun 2026 submissions)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-15] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-15)
- New page: wiki/synthesis/2026-06-15/wq101-alpha-daily.md
- Market context: S&P 500 at 7,520 (+0.50%, YTD +24.66%); 美伊协议6/19签署原油跌至两月低点; SpaceX IPO 首日+19% ($2T市值); FOMC 6/16-17会议
- 板块配置：能源(6) > 工业(4) > 半导体/AI(3) > 金融(2) > 消费必需品(2) > 医疗(1) > 航天(1) > 可选消费(1)
- Top picks: CAT(9.5), GEV(9.5), XOM(9), CVX(9), NVDA(9), JPM(9), WMT(9)
- 核心因子有效性：Alpha#1(动量) > Alpha#41(趋势强度) > Alpha#30(波动率) ≈ Alpha#53(反转) > Alpha#6 > Alpha#12 > Alpha#19
- 关键变化vs 06-13：工业取代能源成为最高评分板块；反转因子(Alpha#53)使用率上升（市场回调中涌现买入机会）；新增SPCX(SpaceX)/GM/VLO
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-16] search | arXiv AI Search — Comprehensive Survey (LLM, CTR, Rec, Ads, Games)
- New page: wiki/synthesis/2026-06-16/arxiv-ai-search.md
- Coverage: 35 papers across 8 domains — LLM Architecture & Efficiency (4), LLM Reasoning & Efficient Inference (4), LLM Agents & RL (5), Games & VLM/LLM (5), CTR Prediction (8), Advertising & Generative Recommendation (8), Sequential Recommendation (1), Cross-Lingual & Safety (1)
- Top picks: MiniMax Sparse Attention (28.4× compute reduction, 14.2× prefill speedup at 1M context), DeRes (1.66× steeper CTR scaling law), GR4AD/Kuaishou (4.2% ad revenue uplift fully deployed on 400M+ users), Odysseus (3× game progress via VLM RL at 100+ turns), AMC/Layer6 AI (SMC for black-box agent RL, outperforms GRPO), MemoPilot (Elo #1 on Texas Hold'em, beats DeepSeek-V3.2)
- Key trends: Sparse/long-context attention replacing quadratic (MSA, PCAF); generative CTR paradigm across Baidu/Tencent/Kuaishou/JD/Shopee; hierarchical RL for long-horizon agents; game-playing LLMs reaching production quality; CTR scaling laws converging on compute-AUC Pareto fronts
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-16] synthesis | arXiv Daily — AI Research Survey (June 16, 2026)
- Summary: wiki/synthesis/2026-06-16/arxiv-daily.md
- ~50 papers across 9 domains: LLM architectures & attention (12 papers), state-space models (5), sequence model theory (9), CTR prediction (11), advertising ranking (6), diffusion LMs (9), games & RL (9), agent memory & reasoning (4), industry deployment snapshot
- Key themes: sparse attention explosion, generative CTR paradigm shift, hybrid SSM-attention, diffusion LM viability, RL for LLM agents
- New page: wiki/synthesis/2026-06-16/arxiv-daily.md
- Updated: wiki/index.md, wiki/log.md

## [2026-06-16] search | arXiv Paper Check — AI & CTR (June 16, 2026)
- New page: wiki/synthesis/2026-06-16/arxiv-paper-check.md
- Sources: cs.AI (41 new + 110 cross-lists), cs.IR (13 new), cs.LG (165 new) — Mon 15 Jun 2026
- Papers surveyed: 16 top picks (10 AI/LLM + 6 CTR/IR/RecSys)
- Top picks: Hyperball (20-30% token speedup, Muon+Hyperball), CacheRL (92% tool-calling at 100× less compute), MiniMax Sparse Attention (28.4× at 1M context), RefGRPO (reflection calibration + free bonus), PAD (denoising × popularity bias), ChronoID (temporal signals for generative rec), ADORE (retrieval-grounded QE, +24.5% nDCG@10 BEIR), TASR (training-free adaptive stopping, KDD 2026), ScoreGate (adaptive RAG chunk selection, 35% fewer tokens)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-17] search | arXiv Paper Check — AI & CTR (June 17, 2026)
- New page: wiki/synthesis/2026-06-17/arxiv-paper-check.md
- Sources: cs.AI (214 new entries, Wed 17 Jun) + cs.IR (10 new Wed + 34 Tue 16 Jun)
- Papers surveyed: 13 top picks (7 AI/LLM + 6 CTR/IR/RecSys)
- Top picks: Fixed-Point Reasoners (looped Transformer with adaptive compute), Small Initialization Matters (γ-rule for LLM pretraining), How Inference Compute Shapes Frontier LLM Evaluation, PreAct (8.5-13× faster repeated computer-use), STAR (spatiotemporal RL for T2I), E³RL (self-healing autoregressive reasoning), HyGRAG (+9.7% multi-hop RAG), OneRank (Transformer-native MTL ranking, KDD 2026), TPOUR (temporal-aware unsupervised retrieval, ICML 2026), Information Cocoon in Generative Recommendation
- Key themes: Adaptive compute allocation across domains (Fixed-Point, PreAct, E³RL, STAR); Transformer-native ranking replacing encoder-predictor separation; Temporal awareness in retrieval (TPOUR); Generative recommendation behavioral analysis (cocoons, memorization)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-17] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-17)
- New page: wiki/synthesis/2026-06-17/game-rl-daily.md
- Coverage: ~60 papers across 8 categories — Game RL (11), Game AI Bots (8), Game Foundation Models (5), PCG (11), Game Benchmarks (9), Industry Game AI (6), World Models (10), Related Techniques (8)
- Top new papers vs 2026-06-16: Matrix-Game 3.0 (40FPS 720p real-time world model), DreamX-World 1.0 (general-purpose interactive world model), DreamerV3 (Nature 2025, Google DeepMind), CPQE (60Hz diffusion policies, EA SEED), NVIDIA ACE Game Agent SDK, Sony PlayStation AI framework, Forking Garden (narrative-conditioned PCG), GameDevBench (132 game dev tasks), OmniGameArena (12 UE5 games, PvP/Coop/Solo), GameGrammar (generative ontology for tabletop game design), HDPCG (high-dimensional PCG), FlyFailFix (iterative game repair via RL+LMM), PopuLoRA (co-evolving LLM populations), Seirênes (adversarial self-play distractions), SAGE (4-agent self-evolution loop), CreativeGame (7-agent iterative game generation), Mind Dreamer (active latent intervention, 1.67x DreamerV3), Distilling GameCWMs, ARROW (continual RL world models), PokeGym (30 tasks in Pokémon Z-A), Code World Models (executable Python world models from LLM), Multiverse (cross-game level blending), VIPCGRL (multi-modal PCG), AutoUE (end-to-end UE5 generation), Bounded Autonomy (LLM characters in live multiplayer)
- Key trends: Self-play+RL for LLM reasoning now mainstream; World models reach real-time deployment (Matrix-Game 3.0 at 40FPS); PCG goes fully multi-modal and end-to-end; Industry pipelines reaching 60Hz (CPQE, NVIDIA ACE on-device); Benchmarks standardize across multi-genre, multi-regime with state-verifiable metrics; Foundation models on 1000+ games approach human-level generalization
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-18] synthesis | Investment Daily — 投资日报（2026-06-18）
- New page: wiki/synthesis/2026-06-18/investment-daily.md
- Coverage: US/HK/A-share/China ADR/EV & AI markets
- Key events: FOMC hawkish dot plot (first Warsh meeting, 2026 hike signal); DeepSeek $7.4B funding at $50B+ valuation (Tencent/CATL); Pentagon 1260H blacklist adds 188 firms (BABA/BIDU/BYD/NIO); Sector rotation from tech to financials/healthcare continues; A-share AI hardware/半导体 rallies on DeepSeek news; Tesla SpaceX IPO tracking
- Key themes: FOMC pivot risk becomes real (dot plot shifted up), China AI arms race intensifies (DeepSeek V4/R2 funding), 1260H geopolitical risk premium on ADRs, Mag 7 June losses surpass $2T, Tripe Witching 6/20
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-18] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-18)
- New page: wiki/synthesis/2026-06-18/wq101-alpha-daily.md
- Coverage: 20 stocks across 7 sectors; FOMC hawkish dot plot (rate 3.8%) + US-Iran peace deal + semi rebound (AMAT +9%, LRCX +6%) + sector rotation Financials/Industrials leading, Technology weakening
- Top picks: JPM (9.0), BAC/GS/MS (8.5), CAT/GEV/RTX/HON/AMAT (8.0)
- Key factors: Alpha#41 (trend strength) dominant for Financials/Industrials; Alpha#53 (reversal) for semiconductors; Alpha#1 (momentum) across cyclical rotation
- Core theme: Rate hike beneficiary (Financials) + AI infrastructure buildout (Industrials) + Semi equipment reversal (AMAT/LRCX/INTC)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-19] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-06-19)
- New page: wiki/synthesis/2026-06-19/wq101-alpha-daily.md
- Coverage: 20 stocks across 7 sectors; Fed hawkish hold + INTC-Apple chip partnership + sector rotation Energy/Tech leading + semi correction bounce (AVGO -$285B aftermath) + Intel surge +9.3% premarket on Apple deal
- Top picks: SNDK (9.5), MRVL (9.5), AMD (9.0), MU/WDC/XOM (8.5), NVDA/STX/JPM (8.0)
- Key factors: Alpha#1 (momentum) dominant for Semis/Storage/Energy; Alpha#53 (reversal) for AVGO/MU/META post-correction; Alpha#41 (trend strength) for Financials/Industrials
- Core theme: Storage super-cycle (SNDK +985% 1Y) + Semi AI buildout (MRVL +217% 3M) + Energy sector momentum leadership + Financials value rotation
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-20] synthesis | arXiv Daily — AI, LLMs, CTR, Recommendation, Advertising, Sequential Modeling, Games, Agents
- New page: wiki/synthesis/2026-06-20/arxiv-daily.md
- Coverage: 20 papers across 7 categories — LLM Architecture (4), CTR/Advertising (4), Recommendation (2), Sequential Modeling / Decision Transformers (2), Games & RL (3), LLM Agents & Tool Use (3), Benchmarks (2)
- Top picks: Variable-Width Transformers (MIT, 22% FLOP reduction), CADET (LinkedIn, +11% CTR lift), SPIRAL (self-play for reasoning transfer), Strat-Reasoner (+22.1% strategic game performance), OPUS (30B tokens beats 200B training), SlimDT (1/3 shorter sequences)
- Key themes: Decoder-only CTR models, self-play reasoning, variable-width/hybrid architectures, LLMs as ancillary components, generative recommendation alignment
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-21] synthesis | arxiv-daily
- Summary: wiki/synthesis/2026-06-21/arxiv-daily.md
- Coverage: 21 papers across 7 categories — LLM Architecture & Training (3), CTR/Advertising (4), Recommendation (3), RL & Games (4), Sequential Modeling (2), Agents & Multi-Agent (3), AI Safety & Evaluation (2)
- Top picks: Variable-Width Transformers (MIT, -22% FLOP), CADET (LinkedIn, decoder-only CTR), SPIRAL (self-play reasoning), Game-RL (ICLR 2026), Connect the Dots (Alibaba, long-lifecycle agents), Token Factory (Meta, soft tokens for LRMs)
- Key themes: Decoder-only for CTR, games as RL training data, diffusion LLMs, long-lifecycle agent training, soft tokenization for recommendations, nonuniform transformer scaling
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-21] synthesis | tech-report-digest
- New page: wiki/synthesis/2026-06-21/tech-report-digest.md
- Coverage: 19 家 AI 公司/机构最新技术报告综合摘要
  - DeepSeek: DeepSeek-V4 (arXiv:2606.19348, MoE + CSA/HCA + mHC + Muon), DeepSeek-V3 (arXiv:2412.19437)
  - OpenAI: GPT-5.5 System Card (2026-04, 1M context), GPT-5 System Card (arXiv:2601.03267)
  - Meta: Muse Spark Safety Report (2026-05, 原生多模态推理), Llama 4 (2025-04, MoE, 10M context Scout)
  - Google DeepMind: Gemini 3.5 Flash (2026-06, agentic SOTA), Gemini 3.1 Pro (2026-02, Deep Think), Gemini 2.5, Gemini Embedding 2
  - Anthropic: Claude Opus 4.8 (2026-05), Fable 5 & Mythos 5 (2026-06), Opus 4.7 (2026-04), Opus 4.6 (ASL-3)
  - Mistral: Mistral Large 3 (2025-12, granular MoE), Magistral (纯 RL reasoning), Ministral 3 (Cascade Distillation), Leanstral
  - Qwen: Qwen3 (arXiv:2505.09388, thinking + non-thinking 统一), Qwen3.5-Omni (ARIA), Qwen3-Coder-Next (80B/3B active), Qwen3-TTS
  - Yi: Yi-Lightning (MoE + RAISE 安全框架), arXiv:2412.01253
  - Baichuan: Baichuan-Omni-1.5 (全模态 + 端到端音频)
  - Microsoft: Phi-4-reasoning-vision-15B (arXiv:2603.03975, MIT 开源)
  - Apple: AFM 3 (2026-06, 20B sparse on-device), AFM Tech Report 2025 (arXiv:2507.13575)
  - NVIDIA: Nemotron 3 Ultra (550B/55B active, LatentMoE + Mamba-Attention hybrid), Nemotron-Labs-Diffusion (AR+Diffusion+Self-Spec)
  - xAI: Grok 4.3 (2026-06, 1M context, configurable reasoning), Grok 4.1 (2025-11)
  - Amazon: Nova 2 (2025-12, Omni+Sonic+Pro), Nova Premier (1M context)
  - Zhipu AI: GLM-5 (arXiv:2602.15763, 744B/40B, DSA + 异步RL + 国产芯片生态)
  - InternLM: Intern-S1-Pro (万亿参数科学多模态), InternLM2 (COOL RLHF)
  - Moonshot AI: Kimi K2.6 (1T/32B, 多模态 Agentic, 300 sub-agents), Kimi K2 (MuonClip)
  - ByteDance: Seed 2.0 (2026-02, Agentic coding focus), Doubao 1.5-pro (稀疏 MoE Scaling Law)
  - StepFun: Step 3.5 Flash (196B/11B, MTP-3, SWA), Step3 (MFA+AFD)
- 6 大趋势总结: MoE 主流化 / RL 训练方法演进 / Scaling Law 新发现 / 原生多模态 / 百万+ token 长上下文 / 推理模型统一化
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-22] synthesis | Game RL & Game AI Bot — Daily Survey (2026-06-22)
- New page: wiki/synthesis/2026-06-22/game-rl-daily.md
- Coverage: ~77 papers across 7 categories — Game RL (12), Game AI Bot (8), Game Foundation Models (7), Procedural Content Generation (5), Game Benchmarks (9), Industry Game AI (4), Related Techniques (27+)
- Key highlights: Odysseus (VLM game RL, 100+ turn Mario), SPIRAL (self-play zero-sum games), NitroGen (CVPR 2026 open generalist gaming agent), Game-TARS (500B+ token generalist, beats GPT-5 at FPS), OmniGameArena (UE5 VLM benchmark with IDC), GameWorld (34 browser games, 170 tasks), Continual Harness (Gemini Plays Pokémon), Matrix-Game 3.0 (40 FPS 720p world model), KRAFTON Ally (PUBG AI teammate deployed), PopuLoRA (LoRA population self-play), MARSHAL (multi-agent reasoning via self-play), COvolve (adversarial co-evolution of envs/policies)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-23] synthesis | Conference Digest — 顶会论文专题报告（2026年6月全面版更新）
- New page: wiki/synthesis/2026-06-23/conference-digest.md
- Coverage: 12+ conferences/venues, 100+ 论文, 15+ 实验室
- ICML 2026: Stratified GRPO, Agentic Verifier, FPTQuant, CoT分解理论, CORAL推理时编辑, BudgetDraft推测解码, Emergent Alignment
- AAAI 2026: From AGI to ASI (DeepMind 57页路线图), AI Co-Mathematician, LLM有害操纵评估, AI辅助评审
- NeurIPS 2025: 门控LoRA连续学习, LLM非确定性来源, Default MoE, GPO推理优化, A-MEM Agent记忆
- ICLR 2026: PAPL扩散LM路径学习(Oral), MERCI探索奖励, ESPO序列级RL, ECF8无损压缩
- CVPR 2026: Perceval视觉过程奖励, LLaDA-V扩散MLLM, AVGGT加速, NitroGen游戏Agent
- KDD 2026: Google YouTube自进化推荐, DLRMv3 HSTU基准, 腾讯全模态GR, GenLI, IDProxy
- arXiv June: VIMPO, Beyond Entropy ICT, Connect the Dots, NF-CoT, Cola DLM, StreamKL
- 7大趋势: RLVR主线, 扩散LM崛起, Agent工程化, 生成式推荐渗透, 多模态融合加速, 评估体系重构, 中国科技CTR爆发
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-23] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-23)
- Summary: wiki/synthesis/2026-06-23/investment-daily.md
- 今日头条：OpenAI 发布 GPT-5.5-Cyber + "Patch the Planet" 开源漏洞修补计划；SpaceX 与 Reflection AI 签署 $6.3B 算力合同（$150M/月，GB300 在 Colossus 2），SPCX -10% 创最大单日跌幅；Anthropic Fable 5 出口管制积分制今日生效
- 美股热点：NVDA ~$214 受 SpaceX 合同间接拖累盘后 -2.1%；AVGO 盘后 -1.8%；SPCX -10% 最为瞩目
- 港股热点：恒指持续弱势接近 11 月低点 23,628；AI 公司 IPO 热潮（Pony AI 进展中）；腾讯 WeChat AI Agent 预期
- A 股热点：延续上周 PCB/半导体/CPO 主线；寒武纪创新高 9200 亿；中际旭创市值超越茅台
- 中概/EV：ADRs 整体偏弱；BYD Da Tang EV 出口布局；宁德时代储能强劲
- AI 主题：OpenAI 安全开源 vs Anthropic 出口管控战略对抗；SpaceX 算力合同收益模式存疑（客户融资稀释实质）；Agentic AI 继续推进（微信 AI Agent 即将发布）
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-23] synthesis | Game RL & Game AI Bot — Daily Paper Digest (2026-06-23)
- New page: wiki/synthesis/2026-06-23/game-rl-daily.md
- Coverage: ~30 curated papers across 7 categories from arXiv, ICLR 2026, ICML 2026, CVPR 2026
- Target categories: Game RL, LLM Game Agents, Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, Related Techniques
- Featured papers: SPIRAL (ICLR 2026 self-play reasoning), Game-RL (ICLR 2026 Fudan, game data → VLM reasoning), Strat-Reasoner (ICML 2026 multi-agent strategic reasoning), NitroGen (CVPR 2026 NVIDIA, 1k-game foundation model), Game-TARS (ByteDance generalist VLM agent), Orak (KRAFTON 12-game benchmark), Dreamer 4 (DeepMind imagination-based Minecraft), PCGRLLM (NYU LLM reward design for PCGRL), lmgame-Bench (ICLR 2026 gaming harness)
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-24] search | arXiv Paper Check — AI & CTR (June 24, 2026)
- New page: wiki/synthesis/2026-06-24/arxiv-paper-check.md
- Coverage: cs.LG (110 new) + cs.AI (198 new) + cs.IR (17 new) from Wed, 24 Jun 2026
- Top picks: OpenThoughts-Agent (agent data recipes, 50+ authors), Can Scale Save Us From Plasticity Loss in LLMs?, Scaling Laws for Task-Specific LLM Distillation, On the Smallness of the LLM Scaling Exponents, Grad Detect (gradient-based hallucination detection), AdversaBench (multi-judge red-teaming), ScaleToT (structured LLM reasoning for billion-scale user modeling), LLM-as-a-Judge for Top-K Recommendation (KDD 2026), The Pitfall of Scaling Up (popularity bias in transformer recommenders, KDD 2026), Improving Long-Context Retrieval with Multi-Prefix Embedding, Data Augmentation: A Fourier Analysis Perspective (COLT 2026), Holistic Data Scheduler for LLM Pre-training via Multi-Objective RL (KDD 2026), Catastrophic Compositional Generation (diffusion extrapolation failure), KLip-PPO (per-sample KL perspective on PPO-Clip), Reasoning as Attractor Dynamics (latent memory retrieval via Gibbs-weighted energy minimization), Unified Multi-Task Relevance Modeling for E-Commerce (SIGIR 2026), INSPIRE (intent-aware sponsored product retrieval, SIGIR 2026)
- Key themes: Agent data recipes and scaling, plasticity loss in LLMs, LLM distillation scaling laws, gradient-based hallucination detection, LLMs for user modeling/recommendation evaluation, popularity bias in scaling recommenders, Fourier theory for data augmentation, multi-objective data scheduling for pre-training, diffusion model compositional failures
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-25] search | arXiv Paper Check — AI & CTR (June 25, 2026)
- New page: wiki/synthesis/2026-06-25/arxiv-paper-check.md
- Coverage: cs.IR (30 entries, 9 new) + cs.AI (2 replacements) + cs.LG (240, from Wed Jun 24)
- Top picks: RaG (Kuaishou, 1.87% ad revenue lift, generative video rec), TokenMinds (YouTube, SID user tokens at billions-scale), IRENE (KDD 2024, 4.2% CTR lift in zero-shot ad retrieval), DynamicPO (DASFAA 2026 Best Paper, preference optimization collapse), DADF (distribution-aware debiasing, 0.65% time-spent lift), AutoRelAnnotator (SIGIR 2026, 150M+ relevance annotations), S2-CAR (energy-based intent segmentation), Weight-Space Geometry of Offline Reasoning (ICML 2026 Workshop, DPO near-orthogonal subspace), Hitchhiker's Guide to Agentic AI (comprehensive reference), Is GraphRAG Needed? (ACL 2026, 19-53% token reduction via context engineering), Catastrophic Compositional Generation (diffusion OOD limits), BITEMBED (ternary-weight text embeddings), Nexus Sampling (80% KV-cache eviction)
- Key themes: Generative recommendation meets video generation, SID-based user modeling at scale, zero-shot retrieval with classifier synthesis, preference optimization collapse in LLM-based rec, offline reasoning weight-space geometry, GraphRAG vs Agentic RAG tradeoffs, extreme quantization for embeddings, streaming KV-cache eviction
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-29] synthesis | Investment Daily — 2026-06-29
- New page: wiki/synthesis/2026-06-29/investment-daily.md
- Coverage: 美股(Mag 7 周跌$416B+, NVDA/AVGO/MU/AAPL/META), 港股(腾讯/阿里/小米/中芯), A股(AI算力/光模块/机器人), 中概ADR(PDD/BABA/JD), 新能源(TSLA/BYD/CATL/固态电池), AI主题(Scaling Law转缓/推理时代来临/Mag 7 capex焦虑)
- Key events: S&P 500 -1.95% wk, Nasdaq -4.6% wk, Micron Q3 EPS $19.72(+932% YoY), SK Hynix $29B ADR获批(7/10上市), 美光/三星/铠侠减产救市, US-Iran ceasefire talks
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-26] search | arXiv AI Research Scan
- New page: wiki/synthesis/2026-06-26/arxiv-ai-search.md
- Coverage: cs.LG (162 entries Jun 26), cs.CL (95 entries Jun 26), cs.IR (22 entries Jun 26 + 20 Jun 25 + 17 Jun 24), plus targeted web searches for games/RL and CTR
- 36 selected papers across 7 categories: LLMs (8), RecSys (5), Sequential/Session (3), Advertising/CTR/Attribution (6), CTR Prediction (5), Games/RL (4), Time-Series/IR (5)
- Top picks: RiVER (RL for LLMs w/o ground truth), GEOALIGN (geometric rollout curation for LLM RL, ICML 2026), Nemotron-TwoTower (NVIDIA diffusion LM, 2.42× throughput), NOVA (agent-driven rec arch evolution, Alibaba), AgentX (self-iterating multi-agent rec system, Kuaishou), TokenMinds (YouTube SID user tokens at billions-scale), Recommendation as Generation (Kuaishou, +1.87% ad revenue with generated video), CADET (LinkedIn, +11.04% CTR lift with decoder-only transformer), Superhuman AI for Generals.io (JAX-native self-play, #1 on leaderboard), Odysseus (VLM 100+ turn game decision-making via RL)
- Key trends: LLM agents for rec system iteration, diffusion/non-AR LMs, RL for LLM alignment without ground truth, linear attention improvements, generative video recommendation, LLM-powered CTR/ads, game AI with self-play RL
- Updated: wiki/index.md (Synthesis section), wiki/log.md

## [2026-06-29] synthesis | Game RL & Game AI Bot — Daily Paper Digest
- New page: wiki/synthesis/2026-06-29/game-rl-daily.md
- Coverage: 60 papers across 7 categories
  - Game RL (9): SPIRAL, OPR, QZero, Chess-R1, ROE, SEMA, CGRPA, LLM-GNCF, Stratagem
  - Game AI Bot (7): AVA, Sensi, PokerSkill, ToolPoker, SpinGPT, ISO, CrossAgent
  - Game Foundation Models (9): NitroGen (CVPR 2026), Game-TARS, P2P0.1, Odysseus, Scaling BC, Latent Bridge, MARL-GPT, Generalist Survey
  - Procedural Content Generation (9): IPCGRL, VIPCGRL, DRL Level Design, WorldGen, Narrative-to-Scene, AI Gamestore, MultiGen, DB-driven PCG, CreativeGame
  - Game Benchmarks (8): GameVerse, HLSMAC, MineExplorer, MineNPC-Task, PillagerBench, AgentOdyssey, ODYSSEY, OpenHA
  - Industry Game AI (4): PUBG Ally (KRAFTON/NVIDIA), Augmenting Game AI with DRL, OpenGame, SLM Game Content
  - Related Techniques (14): SPA, SeRL, ProPlay, SPEAR, π-Play, WorldLLM, SIPP, CuES, ZSG Offline RL, GEMS, MixExpert, LAMIR, Matrix-Game 3.0, Generative Code Opt
- Key themes: VLM+RL convergence, generalist game agents, on-device industry deployment, self-play for reasoning improvement,实时 world models, MARL foundation models, multi-modal PCG
- Updated: wiki/index.md, wiki/log.md

## [2026-06-29] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-06-29)
- New page: wiki/synthesis/2026-06-29/wq101-alpha-daily.md
- Market context: S&P 500 7,354 (-0.05%), Nasdaq -4.6% weekly (tech selloff), Dow +0.6% weekly, WTI crude <$70 (Iran ceasefire progress), PCE 4%+ (3yr high), VIX 18.41, sector rotation tech→healthcare/financials/industrials/utilities
- Top picks: MRNA (9.5/10, Alpha#1/#6, FDA adcomm unanimous flu vaccine), UNH (9/10, Alpha#1/#41, 52-week high), JNJ (8.5/10, Alpha#19/#53), LLY (8.5/10, Alpha#6/#41), ABBV (8.5/10, Alpha#19/#53)
- Top factors: Alpha#41 (trend strength, 12 stocks), Alpha#1 (momentum, 11 stocks), Alpha#30 (volatility, 9 stocks), Alpha#6 (volume-price, 8 stocks)
- Key theme: Rotation 2.0 — Healthcare as the new momentum leader, storage/semis pullback creating reversal entries, financials + industrials benefiting from value rotation
- Updated: wiki/index.md, wiki/log.md

## [2026-06-30] synthesis | LLM Tech Report Digest — 2026-06-30
- New page: wiki/synthesis/2026-06-30/tech-report-digest.md
- Coverage: 19家AI机构最新技术报告 (DeepSeek V4, GPT-5, Llama 4, Gemini 2.5, Claude Opus 4.8/Fable 5, Ministral 3/Mistral Medium 3.5, Qwen3/3.5-Omni, Yi-Lightning, Baichuan-M3, Phi-4 系列, Apple AFM, Nemotron 3 Ultra/Super/Nano, Grok 3/4, Amazon Nova/Premier/2, GLM-5, InternLM3, Kimi K2/K2.5, Step-2, Seed2.0)
- Key themes: MoE主流化, 推理模型融合, Mamba-Attention Hybrid, 长上下文标配(1M+), Agentic优化, 数据质量>数量, 多模态原生, RL训练创新(Muon/MuonClip, 异步RL)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-30] synthesis | Conference Digest — 2026-06-30
- New page: wiki/synthesis/2026-06-30/conference-digest.md
- Coverage: 48 curated papers across 10 sections — ICML 2026 (GoodDiffusion Oral, CPE, Q-learning, CRG), KDD 2026, ECCV 2026 (VisReflect, ViDiHand, Shell-LCC, Nemotron), Kuaishou (POEM, AgentX, RaG), Meta (CMSL), NVIDIA Nemotron, RL (Dual-Flow, ACPO, Chronos, DreamForge-World), Benchmarks (EvalSafetyGap, SpreadsheetBench 2, SWE-Together)
- Key themes: Diffusion models for CTR (GoodDiffusion), agent-driven RecSys evolution (AgentX, NOVA), video generation for recommendation (RaG), benchmark safety evaluation maturity (EvalSafetyGap, SWE-Together)
- Updated: wiki/index.md, wiki/log.md

## [2026-06-30] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-06-30)
- New page: wiki/synthesis/2026-06-30/investment-daily.md
- Coverage: 美股(Dow 52,182 +0.59%, S&P 7,440 +1.18%, Nasdaq 25,820 +2.07%, Alphabet纳入道指+4%+), 港股(恒指22,671 -1.76%, 恒科4,255 -3.41% 深度回调), A股(沪指4,027 -2.26%, 创业板-4.07%), 中概ADR(网易+7.74%领涨, BABA $99.80), 新能源/EV(BYD 1-5月140.5万辆, TSLA Robotaxi奥斯汀上线), AI热点主题(最高法院裁定联储独立性违宪, 美伊多哈和谈, GPT-5.6发布, DeepSeek大规模招聘¥3400亿估值, Claude Fable 5出口管制, 算力租赁转向按Token计费, 存储涨价, AI Agent时代宣言)
- Key events: Dow首次站上52,000; Nasdaq创6月最大单日涨幅+2.07%; Mag 7集体反弹但上周QQQ流出~$20B; 港股恒科YTD -22.82%逼近技术熊市; A股K-shape分化硬件抗跌/软件杀跌; 存储芯片周+7.1%逆势走强; HBM产能全年售罄; SK Hynix $29B ADR上市获批(7/10)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-01] synthesis | 投资日报 — 美股/港股/A股/中概/新能源与AI热点 (2026-07-01)
- New page: wiki/synthesis/2026-07-01/investment-daily.md
- Coverage: 美股(Mag 7 六月蒸发~$2T, NVDA Firmus $30B 订单, S&P 接近历史新高), 港股(恒科回调, 智谱/MiniMax纳入恒生科技), A股(寒武纪+8.2%, 中际旭创+10.2%, 存储芯片板块+20% Q2), 中概ADR(BABA $95.98, 整体缺乏催化剂), 新能源/EV(BYD 1-5月140.5万辆+28%, 小米SU7目标上修至15万台), AI热点主题(GPT-5 Q3发布预期, DeepSeek V4 MoE推理成本再降, COMPUTEX Rubin架构预览, Figure AI $1.5B融资, AI Agent落地)
- Key themes: Mag 7 六月同步杀估值(AI Capex回报率质疑), 国产算力替代逻辑强化, 电动汽车出海高速增长, AI Agent/智能体进入GA阶段
- Updated: wiki/index.md, wiki/log.md

## [2026-07-04] synthesis | Conference & arXiv Digest — Comprehensive Survey (2026-07-04)
- New page: wiki/synthesis/2026-07-04/conference-digest.md
- Coverage: 14 sections across 12+ venues (ICML 2026 / NeurIPS 2025 Best / ICLR 2026 / AAAI 2026 / KDD 2026 / CVPR 2026 Best / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025)
- ICML 2026: 59+ LLM Agent papers (AdaMEM, Agent-Omit, EvoClaw, Constitutional Monitoring, Graph Memory, MCP-Persona), Async Pipeline LLM Pretraining (Yandex, Muon + Error-Feedback for 10B MoE/200B tokens), CTR-Sink (KDD 2026, attention sink for LM-based CTR, AUC +0.2-0.5%)
- NeurIPS 2025 Best Papers: Gated Attention (used in Qwen3-Next), Artificial Hivemind (Infinity-Chat), 1000-Layer Self-Supervised RL, Diffusion Non-Memorization, Representation Superposition Scaling Laws. Agent papers: Agentic Plan Caching, SuffixDecoding, Hogwild! Inference, DRIFT (security), DyFlow.
- ICLR 2026: 5,355 accepted (27.4%), review crisis (45% identity leak, 21% AI reviews). 162 LLM Agent papers (A²FM -45% cost, DeepSynth benchmark, UIS-Digger beats O3/GPT-4.1 on unindexed search). SKT C-APO for recommendation. PAPL (diffusion LM planner-aware training).
- AAAI 2026: 23,000+ submissions, ~23% acceptance. 37 LLM Reasoning papers (Relation-R1, RPM-MCTS, SAPO, SCALE, SERL, MathSmith, Graph-of-Verification). LogicCat Text-to-SQL benchmark.
- CVPR 2026 Best Paper: D4RT (Google DeepMind, dynamic 4D scene reconstruction). Best Student Paper: Compact Structured Latents for 3D. NitroGen (NVIDIA, 1000+ game foundation model). VideoWorld 2 (ByteDance, transferable knowledge from video).
- ACL 2026: Meituan 6 papers (LLM evaluation, process reasoning, math reasoning, RL, generative recommendation).
- EMNLP 2025: 8,000+ submissions, 3,000+ accepted. S1 (simple test-time scaling), Automated Error Discovery (SEEED beats GPT-4o).
- SIGIR 2026: Modular Rep Compression (SJTU), Agentic ST Grounding (A*STAR), Total Recall QA (UMass CIIR), 7 papers from CIIR.
- WWW 2026: ScotRec (social CoT), FeDecider (federated cross-domain LLM), AgentDR (Amazon/MSU), NEZHA (Alibaba generative rec decoding), ByteDance pre-ranking, Kuaishou query rewriting.
- RecSys 2025: GRACE (Walmart, journey-aware gen rec), Spotify agentic query, CTR scaling laws, HSTU production scaling.
- Industry: ByteDance token-based ranking series (RankMixer → TokenMixer-Large 7B/15B, GMV +2.98%), IDProxy (Xiaohongshu MLLM cold-start CTR), CADET (LinkedIn decoder-only ads CTR).
- Key themes: Test-time compute scaling, agent safety/memory/orchestration, generative recommendation with scaling laws, LLM-as-ranker, reasoning-augmented recsys, hybrid architectures (Mamba-Attention, MoE), benchmark evolution crisis.
- Updated: wiki/index.md, wiki/log.md

## [2026-07-03] synthesis | Tech Report Digest — 大模型技术报告综合摘要 (2026-07-03)
- New page: wiki/synthesis/2026-07-03/tech-report-digest.md
- Coverage: 19 家机构 30+ 技术报告/System Card 全面搜索验证
- 新增/重点更新: DeepSeek-V4 (CSA+HCA hybrid attention, Muon optimizer, 1M context); OpenAI GPT-5.6 Preview (Sol/Terra/Luna); Claude Sonnet 5 & Opus 4.8 & Mythos Preview; Gemini 3.1 Pro; GLM-5 (DSA, async Agent RL); Kimi K2.5 (visual agentic, Agent Swarm); NVIDIA Nemotron 3 Ultra (Hybrid Mamba-Attention MoE) & Nemotron-Labs-Diffusion (AR+Diffusion+Self-Speculation); Step 3.5 Flash (11B active frontier); ByteDance Seed1.8 (generalized agency); Intern-S1-Pro (1T scientific multimodal); Baichuan-M3 (clinical medical); Qwen3.5-Omni (ARIA, 256K, omnimodal agent); Ministral 3 (Cascade Distillation)
- Trends: MoE 全面化; Hybrid Mamba-Attention; Diffusion LM; Thinking+Non-Thinking 统一; Configurable reasoning; Agentic RL; 1M context 标配; System Card 标准化
- Updated: wiki/index.md, wiki/log.md

## [2026-07-05] synthesis | WQ101 Alpha Daily — 美股 Top 20 (2026-07-05)
- New page: wiki/synthesis/2026-07-05/wq101-alpha-daily.md
- Market context: Dow 52,900 历史新高 (+1.14%); S&P 7,483 持平; Nasdaq 25,833 (-0.80%); SOX -5.44% 连续暴跌; 非农弱→7月加息概率<20%
- Core theme: **Great Rotation 2.0 确认** — 金融(XLF +2.2%) + 医疗(XLV)领涨, 科技(XLK -2.6%)滑入Lagging
- Top picks: AAPL (9/10, Alpha#1/#6, 动量+量价协同), JPM (9/10, Alpha#1/#41, 金融轮动龙头), LLY (9/10, Alpha#41/#1, GLP-1趋势), ABBV (9/10, Alpha#1/#6, 医疗防御+增长)
- 板块分布: 金融 6只, 医疗 5只, 必需消费 3只, 科技 2只, 能源 2只, 消费周期 1只
- 关键变化 vs 07-04: 板块重心从半导体修复转向低波价值防御; 金融+医疗占比 55%; 新增 BRK.B / JNJ; 半导体出局
- Updated: wiki/index.md, wiki/log.md

## [2026-07-05] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-05)
- New page: wiki/synthesis/2026-07-05/investment-daily.md
- Market overview: Dow 52,900 新高; Nasdaq -4.6% 连续5周下跌; Great Rotation 2.0 (科技→医疗+金融+防御)
- US highlights: META +8.8% (AI Cloud "Meta Compute"); Palantir +7.77% (NVIDIA AI tie-up); Reddit +13.7% (AI licensing); NVDA $194 (-1.78% weekly)
- China ADR: 板块-1.58%; BIDU -3.93% (ERNIE 5.1 中国#1/全球#4); BABA -1.89% (Qwen3.7 Max #5 global); PDD -0.16%
- HK tech: 恒指+1.57% 重回23000; 科指+3.23%; AI 国家标准落地; 百度昆仑芯上市传闻
- A-share: AI 算力芯片回调 (寒武纪/海光信息/沐曦); 存储受益韩国投资计划 (深科技涨停); 半导体设备创新高 (中微公司)
- AI themes: GPT-5.6 宣布(三重变体); Claude Sonnet 5 发布; 算力租赁价格回落30%; 大厂Token配给化; Tesla Optimus 7月量产
- Updated: wiki/index.md, wiki/log.md

## [2026-07-05] synthesis | LLM Tech Report Digest — 大模型技术报告综合摘要 (2026-07-05)
- New page: wiki/synthesis/2026-07-05/tech-report-digest.md
- Coverage: 20 家机构，基于 07-04 综合版增量更新
- 新增/重点更新: DeepSeek-V4 (1T MoE, CSA/HCA, On-Policy Distillation, 1M context, arXiv:2605.21510); Anthropic Claude Opus 4.6 System Card (ASL-3, sabotage risk eval, 2026-02); Qwen3-VL (多模态视觉语言, arXiv:2512.00593); Microsoft Phi-4-Reasoning-Vision 15B (arXiv:2603.03975); xAI Grok 4 (媒体报道, 无正式报告); Kimi K2 补充 MuonClip 优化器/RLVR 细节
- Updated: wiki/index.md, wiki/log.md

## [2026-07-05] synthesis | Conference Digest — Top ML/AI Venues 2025–2026 (ICML/AAAI/NeurIPS/ICLR/KDD/CVPR/ACL/EMNLP/SIGIR/WWW/CIKM/RecSys)
- New page: wiki/synthesis/2026-07-05/conference-digest.md
- Coverage: 14 sections across 12+ venues
- ICML 2026: MaxRL, Gated Attention, Learning Unmasking Policies (diffusion LLM), Equivariant Deep Learning, Latent Dynamics Geometry for RL. 10 key themes (foundation models, multimodal, efficient ML, XAI, ethical AI, RL, healthcare, federated, robustness, human-AI).
- AAAI 2026: 29K submissions → 4,167 accepted (largest ever). Key papers: LogicCat, JudgeBoard, RaCoT, ERank, TIV, DCTR, LiR3, DEPO, SpecQuant (ultra-low-bit), FedSEA-LLaMA, FedBRICK. Keynote on controllable/trustworthy LLM reasoning. AI alignment special track.
- NeurIPS 2025 Best Papers: Gated Attention (Alibaba Qwen, Attention-Sink-Free, 1.7B dense & 15B MoE, 3.5T tokens), Artificial Hivemind (INFINITY-CHAT homogenization dataset), 1000-Layer Self-Supervised RL, Diffusion Non-Memorization. Runners-up: RL for reasoning (skeptical), Online Learning bounds, Scaling Laws.
- ICLR 2026: 5,355 accepted (27.4%). Outstanding Papers: Transformers Inherently Succinct (ETH/Cambridge), Polar Express optimal matrix sign for Muon optimizer. Key papers: Aurelius (text-to-audio), AutoGPS (geometry), CARE (clinical reasoning), ADEPT (continual pretraining), AlphaSAGE (GFlowNets), Orak (KRAFTON game agents).
- KDD 2026: Congrats (Kuaishou graph-structured gen rec), MixRAGRec (MoE KG-RAG multi-agent), SPiKE (LLM semantic profiles + KG), Climber-Pilot (NetEase, non-myopic gen rec, +4.24% core metric), SRPFN (KAIST, synthetic pretraining zero-shot, +7.53% avg, ~1min inference), LLM-as-Judge for Rec, CREATE (transformer+GNN alignment), Causal Attention Reformulations, GR memorization analysis, GenRec (JD.com, +9.5% clicks +8.7% transactions).
- CVPR 2026 Best Paper: D4RT (Google DeepMind/UCL/Oxford, 4D dynamic scene reconstruction, unified transformer, 300× speedup). Best Paper HM: NitroGen (NVIDIA/Stanford, 40K hours 1000+ games, +52% success), SAM 3D (Meta, single-image 3D, 5:1 human preference). Highlighted: PixelDiT (pixel-space DiT, 1.61 FID), O-Voxel (Microsoft, 3D generation), tttLRM (test-time training for 3D), CoTyle (code-to-style). Embodied AI dominant theme.
- ACL 2026: Miner (intrinsic uncertainty as RL reward, +4.58 Pass@1 vs GRPO), PaCoRe (parallel coordinated reasoning, 8B beats GPT-5 at 94.5% HMMT), KARL (Tsinghua, knowledge-augmented RL agents beats GPT-4o/Claude-4), MetaJuLS (meta-RL constraint propagation, 1.5-2× speedup), Self-Evolving Multi-Agent (textual backpropagation), FOREAGENT (execution prediction world models). MTR-Bench (multi-turn reasoning benchmark).
- EMNLP 2025: Best Paper on Response Sampling Theory. Tool-Induced Myopia finding.
- SIGIR 2026: LTRR (learning to rank retrievers for RAG), L2Rec (dual-view LLM recommendation), GenRec (JD.com preference-oriented)
- WWW 2026: ThinkRec (thinking-based recommendation)
- CIKM 2025: MTGR (Meituan industrial generative rec)
- RecSys 2025: Various papers on generative recommendation
- Industry RecSys/CTR highlights: GR4AD (Kuaishou, gen rec for ads, +4.2% revenue, 400M users), OneMall (Kuaishou e-commerce, +13% GMV, 400M DAU), HyFormer (unified seq modeling + feature interaction), OneRec (pure generative matches full pipeline), UniFormer (Kuaishou, model-centric scaling), DualGR (Kuaishou, dual-branch long/short-term gen retrieval), AgentX (Kuaishou, 60+ authors, self-evolving rec sys, 3.7× human value, >RMB 100M revenue), AliBoost (Alibaba, cold-start boosting, 1B+ items, +60% GMV), DAIAN (Alibaba, trigger-induced CTR)
- General AI: DeepAgent (end-to-end reasoning agent with ToolPO RL), Eso-LMs (AR+MDM fusion, first exact MDM likelihood), RePlaid (continuous vs discrete diffusion scaling comparison).
- Agents: AlphaEvolve (Google DeepMind, evolutionary coding agent, improved Strassen's after 56 years), AutoHarness (synth code harness, 145 games, beats GPT-5.2), Confucius Code Agent (54.3% SWE-Bench-Pro), Lacuna (recursive program holes for safe agents), CSRO (Google DeepMind, code-space PSRO), Meta Runtime Behavior LLM.
- Models: PixelDiT, D-AR (diffusion via AR), NextFlow (multimodal sequential, 6T tokens, 5s 1024²), SSM+Video Diffusion.
- Benchmarks: CL-Bench (17.2% avg, context learning crisis), DRACO (Perplexity research benchmark), MathNet (MIT, 30K Olympiad problems), MTR-Bench, Orak, INFINITY-CHAT, LitBench (creative writing, 78% trained vs 73% OTS), LLMEval-Fair, KnowledgeBerg.
- Key themes: RecSys generative revolution led by Kuaishou; agent-driven development; embodied AI at CVPR; diffusion LLM maturity; test-time compute scaling; Chinese industry dominance in applied ML; homogenization as systemic risk.
- Updated: wiki/index.md, wiki/log.md

## [2026-07-05] synthesis | Game RL & Game AI Bot — Daily Survey (2026-07-05)
- New page: wiki/synthesis/2026-07-05/game-rl-daily.md
- Coverage: ~40 curated papers across 7 categories (Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Industry Game AI, Related Techniques)
- Game RL highlights: SPIRAL (self-play zero-sum games for LLM reasoning), Think in Games, Outbidding Liar's Poker (compute-efficient self-play), SpinGPT (first LLM for multi-player poker, ACG 2025), Playing Card Games with non-embedded RL, Pommerman curriculum self-play
- Game AI Bot: Nemobot Games (Shannon taxonomy LLM agents), LLM-Driven NPCs (cross-platform dialogue), AgentGym-RL, DPEPO
- Game Foundation Models: NitroGen (CVPR 2026 NVIDIA, 40K hours 1000+ games), Towards Generalist Game Players survey, Matrix-Game (17B param Minecraft world model), GameVerse
- PCG: PCGRLLM (LLM reward design for PCG-RL, Trans. Games), IPCGRL (language-instructed PCG), RL-enhanced WFC for AR, Game Generation via LLMs
- Benchmarks: Orak (KRAFTON, 12-game MCP-based LLM benchmark), DSGBench (6 strategic games, 5-dim evaluation)
- Industry: GameNGen (ICLR 2025, neural DOOM engine), MLOps for game AI, NVIDIA ACE & NVIGI SDK, Augmenting Game AI with DRL (CoG 2026)
- Related techniques: Self-play survey, DiNAT-RCM curiosity (hierarchical ViT, Neurocomputing), CERMIC (MARL curiosity), cMarlTest (curiosity game testing), CDE (LLM curiosity exploration), ARISE (hierarchical skill evolution RL), Causal HRL (ICML 2025), Transformer World Models (Craftax SOTA), Optimistic World Models, TWISTER (contrastive world model), Off-FSP (offline self-play), MTRO (multi-game DT auto target), ARMS (MARL reward shaping with equilibrium guarantees), RILe (reinforced imitation learning), Structured IL via Inverse Games
- Key themes: Self-play emerging as general reasoning training signal for LLMs; game foundation models scaling from pixels; LLM-driven PCG reward design; industry on-device inference maturing; MARL curiosity and hierarchical approaches advancing
- Updated: wiki/index.md

## [2026-07-06] synthesis | arxiv-ai-search
- New page: wiki/synthesis/2026-07-06/arxiv-ai-search.md
- Coverage: 40+ papers across 8 categories — LLM Training/Alignment (SPIRAL, T-STAR, SPPO, SeeUPO, Trainee-to-Trainer), Attention (Keyless, MSA, Affine-Scaled, Tucker, CAHP, Streaming Bounds, Hybrid), Compression (Joint Prune+Quant, Statistical Pruning, POP, GRINQH), RecSys/CTR (GenRec/JD, UniRec/Shopee, OneRanker/Tencent, RankUp/Tencent, GRAB/Baidu, IDProxy/Xiaohongshu, DS-MLP, GenCI, DAIAN), RL Agents/Games (MemoPilot, MEMO, Agentic Transformers, AgentOdyssey), Multimodal (UniAR, ARM, TVI-CoT, LaME, ROSE, CogniRoute, UniDrive), LLM Dev/Eval (CuratorKIT, KARLA, Causal Methods, Reasoning Trajectories), Sequential Decision Making
- Key themes: Self-play for reasoning training; attention becoming key-less/sparse/tensor-factorized; generative recommendation dominating industrial RecSys (JD, Shopee, Tencent, Baidu, Xiaohongshu); joint prune-quantize at ultra-low bits; multimodal unification via shared tokenizers; RL for agent memory optimization
- Updated: wiki/index.md

## [2026-07-05] synthesis | arXiv Paper Check — AI & CTR (July 5, 2026)
- New page: wiki/synthesis/2026-07-05/arxiv-paper-check.md
- Coverage: 17 curated papers from cs.AI (353 total, 86 new), cs.LG (273 total, 101 new), cs.IR (23 total, 8 new) — July 3, 2026 listings (no weekend submissions)
- AI/LLM highlights: Wiola SLM (2607.01394, novel architecture, 120M–1.5B), Discrete Diffusion Radiology (2607.01436, 3.5–4.4× faster, any-order infill), PMD (2607.01480, procedural memory distillation, +3.8–13.6%), SOLiD at 405B (2607.01567, deception 34%→14%), InfoDelphi (2607.01661, information asymmetry for forecasting, 12–18% Brier), C3RL+CAS (2607.01612, confidence calibration RL, 12.33× inference savings), NightVision (2607.01313, black-box LLM architecture inference), Ember optimizer (2607.01455, O(V+D) VRAM for embeddings), FADE (2607.01490, focal advantage with dynamic entropy, 20k steps earlier peak), MHM-LRU (2607.01523, multi-head recurrent memory, 73.96% retention at 896K), Minimax KV Cache Compression (2607.01520, theoretical guarantees)
- CTR/Rec highlights: MixFormer (KDD 2026, ByteDance Douyin co-scaling dense+sequence), GR2 (generative reasoning re-ranker, +18.7% R@1), Bi-NAS (bi-level NAS for RecSys explanations), CoPersona (KDD '26, collaborative persona graphs), IntentTune (e-commerce query disambiguation), Monosemanticity in RecSys (MSAE for interpretable collaborative filtering)
- Key themes: Novel SLM architectures challenging GPT/LLaMA hegemony; diffusion LLMs reaching parity with AR models; recurrent memory collapse fix via architectural shielding; KV cache compression getting theoretical foundations; generative re-ranking and co-scaling dominating industrial RecSys
- Updated: wiki/index.md, wiki/log.md

## [2026-07-06] synthesis | Game RL & Game AI Bot — arXiv & Proceedings Daily
- New page: wiki/synthesis/2026-07-06/game-rl-daily.md
- Coverage: 25+ papers across 7 topics
- Game Foundation Models: NitroGen (NVIDIA/CVPR 2026, 40K hrs/1K+ games), Scaling BC (open model, 1.2B, causal reasoning), Towards Generalist Game Players (Tsinghua, roadmap survey)
- Self-Play & Multi-Agent Reasoning: SPIRAL (ICLR 2026, self-play transfers to reasoning), MARSHAL (multi-agent RL for LLMs), DAGS (data-augmented game starts, OpenSpiel), PolicyEvolve (LLM programmatic policy evolution via PBT)
- World Models: Dreamer 4 (DeepMind, first offline diamond in Minecraft), Matrix-Game (17B params, SkyworkAI), MineWorld (Microsoft, open-source real-time), AWM (code-driven synthetic environments)
- MARL: GAWM (Transformer world model for SMAC), O2O MARL (AAMAS 2025, offline-to-online transfer)
- LLM Game Agents & NPCs: LLMGA survey (ACM CS 2026), CPDC Challenge 2025 winning solution (MSRA, GRPO for NPCs), cross-platform NPCs (Unity+Discord), DOOM 1.3M specialized model
- PCG: PCGRLLM (LLM-driven reward design, IEEE TG), IPCGRL (language-instructed PCG, CoG 2025), PCG+LLM survey (AIIDE 2024)
- Benchmarks: DSGBench (6 strategic games, 5-dim scoring), TowerMind (TD game for LLM agents)
- Industry: NVIDIA ACE (production in PUBG/inZOI/NARAKA), Inworld AI ($120M), Ubisoft NEO NPC
- Related Techniques: CDE (curiosity-driven exploration for LLM RL), Scalable IRL (DeepMind/NIPS 2024), offline MBRL adaptation, BC horizon theory
- Surveys: MARL in video games (IEEE TG), Self-play survey, LLM agents in games (ICCSIT 2025)
- Key trends: Open-source game foundation models, self-play for general reasoning, world models reaching practical deployment, LLM-driven PCG reward design, industry NPC AI going mainstream
- Updated: wiki/index.md, wiki/log.md

## [2026-07-07] synthesis | Game RL & Game AI Bot — arXiv & Proceedings Daily (2026-07-07)
- New page: wiki/synthesis/2026-07-07/game-rl-daily.md
- Coverage: 30+ papers across 7 categories — Game RL (SPIRAL ICLR 2026, SMAC-Talk, MARL survey IEEE ToG, OpenGuanDan), Game AI Bot (Nemobot, DRL NPCs CoG 2026, Echo Minecraft, Voyager TMLR 2024), Foundation Models (NitroGen CVPR 2026, Towards Generalist GP survey, SIMA 2), PCG (PCGRLLM IEEE ToG, IPCGRL CoG 2025, PCG+LLM survey AIIDE 2024), Benchmarks (GameDevBench, Orak KRAFTON, OmniGameArena UE5, GameWorld NUS, BALROG ICLR 2025, GameCraft-Bench), Industry (Matrix-Game 3.0, GameNGen ICLR 2025), Related Techniques (SPA, CDE, Valdi RLC 2026, Scaling WM-RL, RILe, IRL L4DC 2026, Self-play survey, Vid2World, Reward Shaping ICML 2026)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-07] arxiv-daily | arXiv Daily Report
- Report: wiki/synthesis/2026-07-07/arxiv-daily.md
- Contents: 23 curated papers across 8 categories — LLM Reasoning & RL (GRPO identity, DemoPSD, AReaL2.0), Architecture (HOLA linear attention, MosaicKV), Recommendation (Bi-NAS, CoPersona, DRIFTLENS), Games (AI Native Games survey, Sony Coachable Agents), IR & RAG (SchemaRAG, PRA-RAG, Diffusion-GR2), CTR (DS-MLP, CADET, ML-DCN), Time-Series (EVOTS, StateFlow), Emerging (Thermodynamic AI, Program-as-Weights, AutoMem)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-08] synthesis | conference-digest — Major ML/AI Proceedings Overview (2026-07-08)
- New page: wiki/synthesis/2026-07-08/conference-digest.md
- Coverage: 12 sections across 12+ venues (NeurIPS 2025, EMNLP 2025, AAAI 2026, ICLR 2026, WWW 2026, CVPR 2026, KDD 2026, ICML 2026, ACL 2026, SIGIR 2026, RecSys 2025)
- Key highlights: Gated Attention (NeurIPS 2025 Best), s1 test-time scaling (EMNLP 2025), Meta Lattice (KDD 2026), D4RT (CVPR 2026 Best), OneTrans (WWW 2026), ECF8 (ICLR 2026), CTR-Sink (KDD 2026)
- Themes: Test-time scaling, gated attention, industrial rec scaling, generative recommendation, LLM agents, 4D/3D vision, efficiency optimization
- Updated: wiki/index.md, wiki/log.md

## [2026-07-08] synthesis | investment-daily — 全球科技与 AI 板块 (2026-07-08)
- New page: wiki/synthesis/2026-07-08/investment-daily.md
- Coverage: 美股韩国 Margin Cascade (KOSPI -8% 熔断; NVDA +0.7%/MU -22%/TSM -4.4%/ASML -4.3%); Mag 7 分化持续 ($2.3T 6月蒸发; MSFT -16% YTD); 三星 Q2 利润暴增 18 倍 (DRAM +44%/NAND +53%); 港股 Momenta 上市 (414 倍超购/$751M); 智谱限售解禁 (HKD 400 亿/机构锁仓 70%); MiniMax 锁定期到期; 腾讯混元 Hy3 发布; A 股存储芯片全线走强 (澜起 H 股 15 天翻倍); BYD Seal 08 6.5 万单/30h/$29K; 昆仑芯冲刺 A+H 估值 $50B; OpenAI GPT-5.6 Sol 预览限美国政府审批; 国产算力替代; Robotaxi 监管松绑 (Momenta/Pony.ai/Hesai+NVIDIA)
- Key themes: KOSPI 连锁去杠杆; Great Rotation 2.0 (半导体→防御); 内存超级周期; AI CapEx 回报验证窗口临近; 港股 AI 解禁潮; 中国 EV 市场走弱+出口暴增; 国产芯片 IPO 密集期
- Updated: wiki/index.md, wiki/log.md

## [2026-07-09] synthesis | arXiv AI Research Scan (2026-07-09)
- New page: wiki/synthesis/2026-07-09/arxiv-ai-search.md
- Coverage: 26 curated papers across 6 categories from recent arXiv submissions (Jun–Jul 2026)
- LLM Architecture: Review Residuals (scale-emergent gating), Legible-by-Construction (interpretable transformers), Expressivity-Efficiency Tradeoffs (hybrid SSM+attention theory), GD Convergence (beyond NTK), Algorithmic Foundations (circuit-to-NN compilation)
- RL & Agents: LLM-as-a-Verifier (verification scaling axis, SOTA on 4 benchmarks), CPE (unsupervised weight-space elicitation of latent behaviors), SPIRAL (self-play reasoning via zero-sum games), AgentOdyssey (text game continual learning), AgenticSTS (bounded memory for long-horizon agents), MEMO (memory-augmented context optimization), Agentic RL Systems (self-evolving agents blueprint), Causal Methods for LLMs
- Games & MARL: Multiplayer World Models (Rocket League, 5B latent diffusion, 20fps on B200), MARL-GPT (foundation model for SMACv2/GRF/POGEMA)
- CTR/Rec/Advertising: OneRanker (Tencent, unified generation+ranking, +1.34% GMV-Normal), GR4AD (Kuaishou, +4.2% rev, <100ms latency), IDProxy (Xiaohongshu, MLLM cold-start CTR), DS-MLP (Renmin Univ, dual-stream MLP SOTA), GRAB (Baidu, +3.05% revenue), GenCI (WWW 2026, generative cohort intent), UniSID (end-to-end SID generation), SparseCTR (+1.72% CTR online), DAIAN (trigger-induced intent)
- Updated: wiki/index.md

## [2026-07-09] synthesis | arxiv-paper-check — AI & CTR (July 9, 2026)
- New page: wiki/synthesis/2026-07-09/arxiv-paper-check.md
- Coverage: 22 curated papers from cs.AI (95 new), cs.LG (110 new), cs.IR (4 new), cs.CL (34 new) — submissions from July 8, 2026
- AI & LLM highlights (14 papers): Co-LMLM (continuous-query LMLM), AdaPrefix-GRPO (2.1× GRPO efficiency), Compositional RL via RL post-training, RSI survey (1,250 papers, 7 paradigms), diffusion RLHF (6× efficiency), Future Confidence Distillation (soft+forecast), PALS (40/50% sparsity, -5% accuracy), Bielik (entity familiarity in models), STRACE (LLM agent optimization), SciReasoner (67/86 SOTA), role-factorized search (reasoning curriculum), DeLS-Spec (speculative decoding), Institutional red-teaming guide, CFG guidance repair for diffusion
- CTR & Rec highlights (4 papers): MMEACR (multimodal agent Rec), R³ (ad compliance, ACL 2026), InductWave (KG reasoning), interpretable uncertainty retrieval
- Key themes: RL training efficiency (AdaPrefix-GRPO, compositional RL), reasoning curriculum design (role-factorized, SciReasoner), LLM self-assessment (future confidence, entity familiarity), AI safety (red-teaming), CTR/recommendation with agentic multimodal and compliance awareness
- Updated: wiki/index.md, wiki/log.md

## [2026-07-09] synthesis | Investment Daily — 全球科技与 AI 板块投资热点 (2026-07-09)
- New page: wiki/synthesis/2026-07-09/investment-daily.md
- Market context: 美伊停火终止油价暴涨；Mag 7 vs 存储芯片轮动加剧；港股科技全线暴涨 5%；A 股 AI 算力产业链持续强势
- US stocks (13 stocks): Mag 7 全面分析 + Broadcom/AMD/Palantir/Oracle/SpaceX/Micron/SanDisk
- HK stocks (10 stocks): 阿里巴巴/腾讯/美团/小米/百度/快手/智谱/MINIMAX/商汤/中芯国际
- A-shares (6 stocks): 寒武纪/中际旭创/新易盛/源杰科技/北方华创/宁德时代
- 中概股 (7 stocks): PDD/JD/NTES/TCOM/BILI/LI/NIO
- EV (4 stocks): BYD/Tesla/Zeekr/阳光电源
- AI 热点主题: Grok 4.5, GPT-Live-1, LongCat-2.0, Protea (10M token), Robostral Navigate, LingBot-VLA 2.0, 混元 Hy3, 国产算力里程碑, 机器人/具身智能, 自动驾驶
- Updated: wiki/index.md (synthesis entry added), wiki/log.md

## [2026-07-10] synthesis | Game RL & Game AI Bot — Daily Digest (2026-07-10)
- New page: wiki/synthesis/2026-07-10/game-rl-daily.md
- Contents: 63 papers across 10 categories
  - Game RL Self-Play & Board Games (5): QZero (Go model-free), RGSC (AlphaZero ICLR 2026), SPIRAL (self-play reasoning), Generals.io AI, Tablut AlphaZero
  - MARL & Foundation Models (5): MARL-GPT, MARSHAL, π-Play, SAGE, OpenSIR
  - Atari & Video Game RL (3): Generative Code Optimization, Odysseus (100+ turn VLM), Latent Bridge
  - Game AI Bots & NPC (8): ROE StarCraft II LLM, HER role-play RL, Character-R1, Bounded Autonomy, Nemobot, AdaMARP, Sensi
  - Game Foundation Models (7): NitroGen CVPR 2026 NVIDIA (1000+ games), Game-TARS ByteDance, Pixels2Play (1.2B BC), Lumine, GameVerse, Towards Generalist GP
  - Procedural Content Generation (6): IPCGRL, PCGRLLM, CreativeGame, 3D Level LLM, PCGRL+ JAX, SBGames 2025
  - Game Benchmarks (6): OmniGameArena UE5, GameWorld NUS, VideoGameBench Princeton, Orak KRAFTON, AI Gamestore, AgentOdyssey
  - Industry Game AI (4): NVIDIA ACE Game Agent SDK/NVIGI SDK/Code Agents, AI Native Games survey
  - World Models (8): Matrix-Game 3.0, Solaris multiplayer Minecraft, MineWorld, Matrix-Game 17B, WorldCam, ActWorld, Multiplayer Rocket League 5B, OPINE-World
  - Related Techniques (11): Curiosity-Critic, exploration dynamics, TROFI offline IRL, STO-RL, HiPER HRL, PROF ICLR 2026, Cago, TRRO/PIRO, MAIL theory, structured IL
- Updated: wiki/index.md, wiki/log.md

## [2026-07-11] synthesis | 顶会论文专题报告 — Conference & arXiv Digest (2026-07-11 全面更新版)
- New page: wiki/synthesis/2026-07-11/conference-digest.md
- Coverage: 12+ venues (ICML 2026, ICLR 2026, AAAI 2026, NeurIPS 2025, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025), 200+ curated papers, 20+ labs
- Award papers: Gated Attention (NeurIPS 2025 Best, Alibaba Qwen), Transformers are Inherently Succinct (ICLR 2026 Outstanding), LLMs Get Lost In Multi-Turn (ICLR 2026 Outstanding, Microsoft), D4RT (CVPR 2026 Best, Google DeepMind), LLM2CLIP (AAAI 2026 Outstanding, Microsoft)
- ICML 2026 (23,918 submissions, ~6,500+ accepted): 6 Orals from Google (ATLAS, DPO Unchained, Rational Transductors, How Much Memorize, Equivalence, TokSuite), GRAM access control (Anthropic Spotlight), DreamDojo robot world models (NVIDIA), TCEC quantized diffusion (ByteDance Spotlight+Oral)
- ICLR 2026 (19,814 submissions, 5,340 accepted): 223 Orals; Mamba-3, MoE vs Dense, TileLang (5x Triton), NextStep-1 (ByteDance), Depth Anything 3 (TikTok), SANA-Video (NVIDIA)
- AAAI 2026 (23,680 submissions, 4,167 accepted): ReconVLA robot perception, AI peer review (22,977 papers, OpenAI GPT-5 sponsored), COREA (Amazon), SemanticVLA (Huawei)
- CVPR 2026 (16,092 submissions, 4,089 accepted): NitroGen game foundation (NVIDIA 40K hrs), SAM 3D (Meta), CLAY 3D generation (Microsoft/Tsinghua)
- KDD 2026: Kunlun Scaling Laws (Meta, MFU 17%→37%), CausalMoE (Tencent billion-scale)
- ACL 2026: WebAnchor Plan Anchor (Alibaba), DEEPPLANNER (ByteDance Seed), GeoRA RLVR (Meituan)
- SIGIR/WWW/RecSys: L2Rec (+9.24% CTR), SIDReasoner (Alibaba), GenCI (WWW), DiffuMIN (Kuaishou +1.52% CTR)
- CTR Industrial: EST/FAT/PRECTR-V2 (Alibaba), OneRanker (Tencent +1.34% GMV), GR4AD (Kuaishou +4.2% revenue), DeRes (ByteDance), IDProxy (Xiaohongshu), UniRec (Shopee +5.60% GMV), CADET (Amazon)
- 8 key trends: RL for LLM post-training, diffusion LM maturing, generative rec + CTR scaling laws, agent systems + autonomous research, multimodal unity, safety/alignment audit, efficient inference, memory/context management
- Updated: wiki/index.md (synthesis entry added), wiki/log.md

## [2026-07-12] synthesis | WorldQuant 101 Alpha 因子精选 — 美股 Top 20 (2026-07-12)
- New page: wiki/synthesis/2026-07-12/wq101-alpha-daily.md
- Market context: S&P 6,280(+0.3%), Dow 44,651(+0.4%), Nasdaq 20,631(+0.1%), VIX 15.78
- Key events: Trump 35%加拿大关税(8/1生效), NVDA市值突破$4万亿, BTC $118K, 黄金$39+, Fed维持4.25%-4.5%, DAL财报超预期
- Top 20 stocks: NVDA(9.5), MU(9.3), META(9.0), SNDK(8.8), TSLA(8.5), AAPL(8.3), AMZN(8.2), GOOGL(8.2), AMD(8.0), AVGO(7.8), LLY(7.7), MSFT(7.5), DELL(7.5), TSM(7.3), VRT(7.3), JPM(7.2), CEG(7.0), MRNA(7.0), PLTR(6.8), ABBV(6.8)
- Factor analysis: Alpha#1 动量主导(8次/40%), Alpha#6 量价相关(4次/20%), Alpha#30 低波动(5次/25%), Alpha#19 均值回复(4次/20%), Alpha#41 趋势(4次/20%), Alpha#53 反转(3次/15%), Alpha#12 量价背离(2次/10%)
- Sector breakdown: 半导体8只、科技5只、医疗3只、工业/能源/金融4只
- Updated: wiki/index.md, wiki/log.md

## [2026-07-14] ingest | arXiv Paper Check — AI & CTR (July 14, 2026)
- Summary: wiki/synthesis/2026-07-14/arxiv-paper-check.md
- Coverage: 10 curated papers from cs.AI (27 new), cs.IR (2 new) — Monday July 13, 2026 listings
- AI highlights: CogniConsole (inference-time control as formal abstraction), GATS (graph-augmented tree search with layered world models, 100% success vs 92% LATS), Long-Horizon-Terminal-Bench (46 long-horizon tasks, 15 frontier models), ProofCouncil (LLM agent for open mathematical problems, 6/10 correct), Multimodal Reward Hacking (first systematic study, 48.1% RHR), Shared Selective Persistent Memory (96% task completion vs 79% without memory), Agora (auction-based task allocation for LLM agents)
- CTR highlights: From Raw IDs to Semantic Planning (recommender systems evolution), Do Rec Algos Work for LLM Agents? (Moltbook, structural signals dominate), Rashomon Explanation Set (explanation fidelity improves prediction accuracy on click-through prediction)
- Safety highlights: Scoped Verification (GRACE, 0.091→0.673 reliability), Neuro-Agentic Control (LLM planner + TimesFM for cybersecurity), TrustX ARC (12-dimension risk classification)
- Key themes: Agent reliability via external control; memory as critical bottleneck; reward hacking in multimodal RL; recommender systems evolving from raw IDs to semantic planning; explanation-prediction coupling
- Updated: wiki/index.md, wiki/log.md

## [2026-07-16] synthesis | arXiv Daily Report — AI, LLMs, Recommendation, CTR, Advertising, Sequential Modeling, Games
- New page: wiki/synthesis/2026-07-16/arxiv-daily.md
- Coverage: 15 papers across 5 categories
- CTR Prediction (5): DS-MLP dual-stream MLP (Renmin/ByteDance/Meituan), CADET LinkedIn decoder-only CTR (+11.04%), EST Alibaba scaling laws (+3.27% RPM), GenLI generative long-term interest, LoopCTR loop scaling (Alibaba)
- Recommendation (4): Trustworthy LLM recommendation survey (200+ studies), SPiKE knowledge graph enrichment using LLMs (KDD 2026), SELLER sequence-aware explainable recommendation, Rec-R1 RL bridging generative LLMs with recommendation systems
- Sequential Modeling (3): PerSRec Meta personalization for long-term interest, TGA multi-behavior transitions (Alibaba), NextFlow unified multimodal sequential modeling (ByteDance)
- LLMs in Rec (2): Sequence-aware LLMs for explainable recommendation, Rec-R1 reinforcement learning framework
- Games (1): Augmenting Game AI with deep reinforcement learning (EA, Conference on Games 2026)
- Key themes: MLP-based efficient architectures for CTR, generative approaches enhancing discriminative models, LLM integration into recommendation systems, linear-complexity multi-behavior modeling, unified multimodal sequential modeling
- Updated: wiki/index.md, wiki/log.md

## [2026-07-16] synthesis | Top ML/AI Conference & arXiv Paper Digest (2026-07-16)
- New page: wiki/synthesis/2026-07-16/conference-digest.md
- Coverage: 80+ papers across 12+ venues (ICML 2026, NeurIPS 2025, AAAI 2026, CVPR 2026, KDD 2026, SIGIR 2026, ACL 2026, RecSys 2025, EMNLP 2025, ICLR 2026, CIKM 2025, WWW 2026) + arXiv recent preprints
- Top Conference Awards: NeurIPS 2025 Best (Gated Attention, Artificial Hivemind, 1000 Layer RL), ICLR 2026 Outstanding (Flexibility Trap dLLMs, High-Accuracy Sampling), AAAI 2026 (4167/23680 accepted), CVPR 2026 Best (SAM 3D Meta, D4RT DeepMind, B³-Seg 3DGS)
- Key Industry Labs: Google DeepMind (D4RT, CodeGen2.5), Alibaba (TMallGS, EST, TAROT), Tencent (OneRanker), Kuaishou (GR4AD, LSVCR), NVIDIA (NitroGen), Meta (SAM 3D), ByteDance (NextFlow)
- ICML 2026 Highlights: MemoPilot ELO#1, STAPO trajectory-aware RL (13-17% speedup), HiPER 97.4% ALFWorld, JitRL 30× cheaper, Multi² agent comms, BEACON planning-guided search
- CTR/Ads/Rec: DeRes dual-path attention +0.32% AUC, EST power-law +3.27% RPM, OneRanker +1.34% GMV, RankUp +3-4% GMV, Semantic IDs joint S&R (RecSys 2025)
- Code Generation: Self-Execution Simulation, DUET dual execution (28.9% code match), EAGER (37.3% latency cut, 5.5% quality), EvoCodeBench, CodeWorldModels
- Key themes: Diffusion language models (Flexibility Trap +8%), Agent RL (STAPPO, RE-TRAC, EAS), Agentic search (14M requests/day), Code execution as verification, Few-shot learning (TAROT, MoDoMoDo), LLM security (AURA, InTRO)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-17] synthesis | arXiv AI Research Report (2026-07-17)
- New page: wiki/synthesis/2026-07-17/arxiv-ai-search.md
- Coverage: 30+ papers across 6 categories
- LLMs (5): MILES modular instruction memory, LLM-as-a-Verifier verification framework, KARLA knowledge-base augmented retrieval, Belief-reality separation mechanisms, POPS recovering unlearned knowledge
- Recommendation (5): GLASS generative recommender, SIDReasoner reasoning over semantic IDs, GenRec JD.com deployed, AgentX Kuaishou self-iteration, Gryphon industrial music service
- Advertising (5): CADET LinkedIn +11.04% CTR, GRAB Baidu +3.49% CTR, GR4AD Kuaishou +4.2% revenue, AdNanny Bing Ads unified LLM, OneRanker Tencent +1.34% GMV
- Sequential Modeling (5): Mamba-3 SSM improvements, Oryx hybrid switching, MuonSSM orthogonalized updates, NextFlow multimodal 6T tokens, Sparse Delta Memory 3-order-of-magnitude state
- CTR Prediction (5): DS-MLP dual-stream MLP SOTA, SparseCTR sparse attention scaling laws, DeRes dual-path +0.32% AUC, LoopCTR loop scaling paradigm, GenCI generative interest cohorts
- Games (5): Odysseus VLM 100+ turn decisions, Multiplayer World Models 5B parameters, GIFT games for LLM training, Trainee-to-Trainer LLM environment design, T-STAR tree-structured policy optimization
- Key trends: Generative recommendation production deployment, LLM integration for verification/reasoning, scaling laws in CTR/rec, hybrid SSM-attention architectures, self-improving systems
- Updated: wiki/index.md, wiki/log.md

## [2026-07-19] synthesis | Top ML/AI Conference & arXiv Paper Digest — 2026-07-19
- New page: wiki/synthesis/2026-07-19/conference-digest.md
- Coverage: 68+ papers across 12 venues, 25+ labs
- ICML 2026 (15): Outstanding: Flexibility Trap (Tsinghua) + High-Accuracy Sampling (MIT/Yale); Position Paper: Censor's Toolkit (MCML); Honorable: Obfuscation Atlas, Motion Attribution, LLM Memorization, Random Matrix Diffusion, Grokking; Test of Time: Async DRL (Mnih/DeepMind 2016); Agents: MemoPilot ELO#1, HiPER 97.4% ALFWorld, JitRL 30× cheaper, SPIRAL +10.5%; Rec/CTR: Shannon Scaling Law, Self-Flow, UniAR (Alibaba), Complete-muE; Ads: Autobidding LLM Creatives (RUC/Tsinghua), Incentivized Exploration (UCLA/Meta)
- NeurIPS 2025 (5): Best: Gated Attention (Alibaba) → shipped Qwen3-Next; Artificial Hivemind 70+ LLMs; 1000 Layer RL; Diffusion Memorization; RL vs Reasoning Runner-Up
- ICLR 2026 (4): Outstanding: Transformers Succinct (MPI-SWS); LLMs Lost Multi-Turn 39% drop; Mean Flow Policy; Polar Express; Muon Honorable
- AAAI 2026 (4): AURA safety alignment for rec; InTRO +20% math reasoning; MoMoREC Taobao +6.3% GMV; TreeBridge Shopee +1.55% GMV
- KDD 2026 (3): RankElastor effective-rank dynamics; RPORec Kuaishou RL+reasoning; EST Alibaba +3.27% RPM; GR4AD Kuaishou +4.2% revenue
- CVPR 2026 (5): Best: D4RT DeepMind 4D reconstruction; Student: Native Compact Latents; Honorable: SAM 3D (Meta), NitroGen (NVIDIA), O-Voxel (Microsoft), B³-Seg; 16,092 submitted → 4,089 accepted
- ACL 2026 (8): Best Theme: Imperfective Paradox, Memory Efficiency, Local Attention Expressivity; Best Resource: HSCodeComp (Alibaba), ImplicitMemBench, Audio MultiChallenge, VeriTaS; Social Impact: DIA-HARM, Student LLM Use; 18 Outstanding: RLVR (Evolutionary Decoding, STEER, GeoRA, CURE), Agents (CAR-bench, MediEval), Safety; RecPO intensity+temporal
- SIGIR 2026 (5): Agentic Search 14M requests; AgentRank; LTRR +5.8% NDCG; Tool-Star web agents; ACE anisotropy +12.4% Recall; HyDE +18% long-tail; Purifying Multimodal RAG (Meituan/Zhejiang)
- WWW 2026 (3): ThinkRec +4.2% HR; GenCI +6.1% cold-start; SparseCTR Meituan +1.72% CTR
- RecSys 2025 (3): LSVCR Kuaishou +4.13%; Semantic IDs joint S&R; LONGER ByteDance 10K tokens
- CIKM 2025 (1): RankMixer ByteDance MoE ranking
- arXiv (12): SAO GLM-5.2 750B single-rollout RL; Push Your Agent goal persistence +34%; SkillOpt Microsoft +22%; MaRCA Alibaba +16.67% revenue; OD-LLM on-device rec; HORIZON benchmark CMU/MSR; GenLI generative interest; TiG Honor of Kings; Genstrat strategic reasoning; PCSP 64 personas; Scalpel vs Hammer GRPO/SFT; Sparse Delta Memory Meta 8B beats attention; Mamba-3 SSM
- Key themes: Diffusion wins ICML 2026 (both Outstanding); Alignment as dual-use (Censor's Toolkit position paper); RL post-training norm (GLM-5.2, Qwen3-Next, KARL, SPIRAL); Generative rec industrial (GR4AD, TreeBridge, MoMoREC, MaRCA); CVPR signals applied generative AI; ACL dominated by RLVR + safety
- Updated: wiki/index.md, wiki/log.md

## [2026-07-18] synthesis | Top ML/AI Conference & arXiv Paper Digest — 2026-07-18
- New page: wiki/synthesis/2026-07-18/conference-digest.md
- Coverage: 200+ papers across 12+ venues, 20+ labs
- ICML 2026: Outstanding (Flexibility Trap, Shannon Scaling Law), Agents (MemoPilot ELO#1, HiPER 97.4% ALFWorld, JitRL 30× cheaper), Rec/CTR (Self-Flow, UniAR, Complete-muE)
- NeurIPS 2025: Best (Gated Attention Alibaba → shipped Qwen3-Next), Artificial Hivemind 70+ LLMs, 1000 Layer RL, RL vs Reasoning Runner-Up
- ICLR 2026: Outstanding (Transformers Succinct), LLMs Lost Multi-Turn 39% drop, Mean Flow Policy, Polar Express, Muon HM
- AAAI 2026: AURA safety alignment, InTRO +20% math, MoMoREC Taobao +6.3% GMV, TreeBridge Shopee +1.55% GMV
- KDD 2026: RankElastor effective-rank dynamics, RPORec Kuaishou RL+reasoning, EST Alibaba +3.27% RPM, GR4AD +4.2% revenue
- CVPR 2026: Best (D4RT DeepMind 4D, SAM 3D Meta, NitroGen NVIDIA 40K hrs)
- ACL 2026: SOAR +16.9% research, KARL beats GPT-4o, HSCodeComp Best Resource, RecPO intensity
- SIGIR 2026: Agentic Search 14M requests, AgentRank, LTRR, HyDE, ACE anisotropy +12.4%
- WWW 2026: ThinkRec, GenCI, SparseCTR Meituan +1.72%
- RecSys 2025: LSVCR Kuaishou +4.13%, Semantic IDs, LONGER
- CIKM 2025: RankMixer ByteDance
- arXiv: SAO GLM-5.2 750B, MaRCA +16.67% revenue, Sparse Delta Memory beats attention 8B, Mamba-3, SPIRAL +10.5%, TiG Honor of Kings, Genstrat, PCSP 64 agents
- Key themes: Diffusion wins ICML 2026, RL post-training norm, generative rec industrial deployment, CVPR applied generative AI, ACL RLVR + safety
- Updated: wiki/index.md, wiki/log.md

## [2026-07-22] synthesis | arXiv Paper Check — AI & CTR (July 22, 2026)
- New page: wiki/synthesis/2026-07-22/arxiv-paper-check.md
- Coverage: 20 curated papers from cs.AI, cs.IR, cs.LG
- AI Agents & Reasoning (5): CodeRescue budget-calibrated coding agents, Agents in the Wild deployment research, ResearchArena AI safety benchmark, Supra Cognitive Modes agent memory, Shapley-based reward attribution for parallel reasoning
- Recommendation Systems (6): TSGR Taobao generative retrieval, dual-level denoising multi-modal recommendation, epistemic position-based click model, topology-aware tokenization for generative rec, RECAP streaming semantic user profiles, RecGPT-V3 technical report
- CTR Prediction & Advertising (9): RAMP privacy-preserving CTR, Long-History User Transformers for ad ranking, TMallGS Alibaba unified search, NONTP extending NTP for generative rec, Mitigating Early CTR Collapse, DeRes dual-path CTR, DS-MLP dual-stream MLP, Cross-Domain Semantic IDs for ads ranking, LENS staged interaction granularity
- Key themes: Agent safety and deployment readiness, generative retrieval architectures, privacy-preserving CTR prediction, offline/online split for latency-constrained ad ranking, quantization for cross-domain transfer, training stability in CTR models
- Updated: wiki/index.md, wiki/log.md

## [2026-07-24] ingest | arXiv Daily Report
- Summary: wiki/synthesis/2026-07-24/arxiv-daily.md
- Coverage: 14 curated papers across AI, LLM, Recommendation, Advertising, CTR, Game AI, Sequential Modeling
- Recommendation Systems (9): RECAP (Kuaishou), CoSimRec, ZoRRO, RecRec, NAILS, Raw IDs→Semantic Planning, Long-term Engagement (Pinterest), Diffusion-GR2, Agentic Rec Survey
- CTR & Advertising (3): DS-MLP, CADET (LinkedIn), GRAB (Baidu)
- Game AI (1): Augmenting Game AI with Deep RL (EA)
- LLM / Neuro-Symbolic (1): SoftReason
- Key themes: Generative CTR architectures at scale, streaming user profiles with LLM+RL, zero-weight recommendation, recursive sequential modeling, diffusion-based re-ranking, agentic recommendation roadmaps, post-hoc fairness alignment
- New pages: wiki/synthesis/2026-07-24/arxiv-daily.md

## [2026-07-25] synthesis | arXiv AI Search Report (2026-07-25)
- New page: wiki/synthesis/2026-07-25/arxiv-ai-search.md
- Coverage: 25+ papers across 9 categories
- CTR Prediction (4): CADET LinkedIn decoder-only +11.04% CTR, GRAB Baidu generative CTR +3.05% revenue +3.49% CTR, DS-MLP dual-stream MLP SOTA (TKDD), ML-DCN Pinterest +1.89% CTR
- Generative Recommendation (6): TokenMixer-Large 7B ByteDance +2.98% GMV, UniMixer unified scaling laws, ULTRA-HSTU Meta 5.3× training/21.4× inference speedup, OneRec Kuaishou end-to-end generative, RecGPT-V3 Taobao Memory Hub +3.97% GMV, PinFM Pinterest foundation model
- Sequential Modeling (4): LONGER ByteDance 10+ scenarios billion users, HLLM hierarchical LLM, R²ec reasoning recommender NeurIPS 2025, RecZero RL-based reasoning
- Advertising & Auto-Bidding (3): GRAD Meituan MoE+Value Estimator ROI+10.68%, GenCTR two-stage generative CTR, JD-BP joint-decision bidding
- LLM4Rec (4): Full-Stack LLM sequential, LLM agent users study, Autonomous Info Seeking survey, RecGPT series
- Semantic ID & Generative Retrieval (3): GPSD Alibaba KDD 2025, UniSID end-to-end, generative retrieval deployed
- AI for Games (6): Game-theory+RL border defense, SPIRAL self-play ICLR 2026, Think in Games LLM+RL, NitroGen NVIDIA generalist, Nemobot LLM game agents, Multi-agent KTO
- LLM Infrastructure (3): KV Cache optimization survey, Dynamic Agent Skills survey, Understanding LLMs
- Key trends: Generative CTR paradigm shift (discriminative→generative pre-training+fine-tuning), token-based ranking scaling to 7B+, foundation models for rec at billion scale, LLM4Rec maturing from feature encoding to reasoning chains, semantic IDs replacing traditional item IDs, auto-bidding reframed as generative sequence modeling
- Updated: wiki/index.md, wiki/log.md

## [2026-07-27] synthesis | Conference & arXiv Digest (2026-07-27)
- New page: wiki/synthesis/2026-07-27/conference-digest.md
- Coverage: 80+ papers across 12 venues + arXiv recent
- ICML 2026 (Outstanding): High-Accuracy Sampling Diffusion-NES, Alignment Community Censor, MoE Vision, Arabic LLM
- ICML 2026 DeepMind: Geo-Cultural Safety Alignment (GSA-Bench), LLM Overthinking (SimpleThenHard)
- NeurIPS 2025 (Best): Artificial Hivemind, Gated Attention, 1000 Layer Self-Supervised RL, LeCun Autonomous Intelligence; Runner-Up: RL Reasoning, Superposition Neural Scaling
- ICLR 2026 (Outstanding): Transformers Inherently Succinct, LLMs Lost Multi-Turn; Honorable: Polar Express/Muon Algorithm
- AAAI 2026: 17.6% acceptance (4167/23680); Outstanding: Causal Structure Learning, ReconVLA, LLM2CLIP; Best Alignment: Global Human Opinion
- KDD 2026: 21% acceptance (256/1215); Best: GReVLOC, Robustness of LLMs, GRAB Field-Aware Generative CTR
- CVPR 2026: 25.2% acceptance (4089/16092); Best: Draft-and-Refine Visual Experts, VQA Multimodal CoT, Fairness Face Models
- ACL 2026 (Outstanding): MauBERT, Evolutionary Decoding, Lying with Truths, CURE, GeoRA
- SIGIR 2026 (Best): Perfect Personalization, Unified ICL+IE, Feature Selection CTR
- WWW 2026 (Best): MedRGAG Medical QA, DualGR Dual-Perspective Retrieval
- EMNLP 2025 (Best): Infini-gram mini, LingGym, MiCRo, Causal Interventions
- RecSys 2026 (Best): Empathetic Conversational Recommender, Cold-Start LLM Profiling, Diverse Multi-Objective Re-Ranking
- CIKM 2025 (Best): GAE Link Prediction, Counterfactual LLM
- arXiv Recent: PromptPack ByteDance LLM annotation +8.2% CTR, Speculate with Memory agent acceleration, DAE Disentangled Sequential CTR, Long-Horizon-Terminal-Bench
- Key themes: Agentic AI as KDD 2026 core theme, LLM alignment & safety (ICML/NeurIPS/AAAI), multi-turn conversation failures (ICLR), generative recommendation at scale (GRAB/Draft-and-Refine), data poisoning robustness (ICML/NeurIPS), scaling laws for synthetic data (AAAI), multilingual LLMs (Arabic/African)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-27] ingest | Conference Digest: 2025-2026 Top ML/AI Venues (Updated)
- Summary: wiki/synthesis/2026-07-27/conference-digest.md
- Coverage: ICML 2026 (6634 papers), AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, SIGIR 2026, WWW 2026, EMNLP 2025, RecSys 2025
- Key papers: Align³GR (Kuaishou +17.8% Recall@10), Gated Attention (Qwen NeurIPS Best), Artificial Hivemind (NeurIPS Best), GR4AD (Kuaishou +4.2% ad revenue), Sparse by Design (Meta), VENOMREC, RSIR, HG-Rec, UniRec (+22.6% HR@50), 1000-layer RL
- 8 cross-conference trends identified: LLM4Rec industrialization, expanded alignment taxonomy, non-Euclidean geometry, auction+LLM, safety/robustness, MoE redesign, attention revolution, RL depth scaling
- Updated: wiki/index.md (added conference-digest entry)
- New pages: wiki/synthesis/2026-07-27/conference-digest.md
- Contradictions: none

## [2026-07-27] ingest | 投资日报 — 全球科技与 AI 板块 (2026-07-27)
- Summary: wiki/synthesis/2026-07-27/investment-daily.md
- Coverage: 美股大盘(Mag7分化)、AI芯片股血洗、港股科技、A股AI热点、中概股、新能源/EV、AI热点深度
- Key data: S&P 7411(+0.05%)/Nasdaq 24975(-0.64%)/周-2.1%; Mag7单日蒸发$787B(7/23); AAPL周+4.15%克制AI投入领跑/TSLA周-19%FCF-$10.9亿; 芯片股血洗INTC-7.89%/MU-6.99%/ARM-8.14%; 港股阿里+4.86%(千问3.8开源); A股寒武纪+12.18%逼近¥1万亿; 小鹏36717台+229%YoY; 比亚迪成全球纯电销冠
- Key themes: AI叙事从"Capex投入=利好"反转为"Capex投入=惩罚"; 7/29-7/30财报季为2026年最关键验证窗口; 华为Atlas 950超节点+七部委国产芯片政策突破; EV格局重塑(比亚迪全球销冠/小米跨界搅局)
- Updated: wiki/index.md (added investment-daily entry), wiki/log.md
- New pages: wiki/synthesis/2026-07-27/investment-daily.md
- Contradictions: none

## [2026-07-26] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 26, 2026)
- Summary: wiki/synthesis/2026-07-26/game-rl-daily.md
- Coverage: 33+ papers across 8 categories
- Key papers: SGS self-guided self-play (Stanford 2604.20209, 7B beats 671B Lean4), FootsiesGym (2607.06514, fighting game benchmark), Multiplayer World Models (2607.05352, 5B Rocket League 20fps), MCTS-Enhanced Policy Gradient (2607.17882), Reward-Free Evolving Agents (2607.14408, pairwise validator), Deflanderization (2510.13586, CPDC 2025), LLM+AP NPC (2501.10106), Psy-CoT/RAPO (2606.27025, +40% CoSER), EvolvingWorld (2607.17250, co-evolving agents), AlayaWorld (2607.06291, open-source real-time interactive), ABot-World-0 (2607.19191, RTX 5090 16fps 720P), From Pixels to States (2607.14076, Black Myth 90hrs data engine), OPINE-World (2607.01531, ARC-AGI-3 20/25 games), MAGIC (2607.11594, multi-scene 0.96F1), Garden of Forking Paths (2605.01245, narrative arc PCG), SLM dynamic game content (2601.23206, 93% success), WorldGen (CVPR 2026 NVIDIA traversable 3D), Multiverse (2603.26782, cross-game blending), CausalGame (ICML 2026 Oral, 2607.04293, 30 LLMs 68% vs 82% optimal), GameCraft-Bench (2606.17861, Godot 41% best), AI Gamestore (2602.17594, <10% human median), WebGameBench (2605.17637), GAME-Scope (2607.15224), CGSReg Atari Pong (2607.15142, DreamerV3 -21→-12), NVIDIA ACE, KRAFTON production, Sony AI CPDC
- Key themes: Self-play + world models dual paradigm; LLM game agents mature (Psy-CoT/RAPO +40%, EvolvingWorld co-evolving agents); open-source real-time interactive models (AlayaWorld/ABot-World-0); open-world game world models (Pixels to States Black Myth 90hrs); cross-game blending (Multiverse) and foundation models (WorldGen CVPR 2026); CausalGame ICML 2026 Oral shows 68% vs 82% optimality gap; CGSReg regularization improves world models
- Updated: wiki/index.md, wiki/log.md
- New pages: wiki/synthesis/2026-07-26/game-rl-daily.md
- Contradictions: none

## [2026-07-26] synthesis | 2026-07-26 Conference & arXiv Daily Digest
- Summary: wiki/synthesis/2026-07-26/conference-digest.md
- Updated: wiki/index.md, wiki/log.md
- New pages: wiki/synthesis/2026-07-26/conference-digest.md

## [2026-07-28] synthesis | Conference Digest — 2026-07-28 (ICML/AAAI/ICLR/NeurIPS/CVPR/KDD/SIGIR/WWW/EMNLP/ACL/CIKM/RecSys + Agent/CTR/Gen Rec/Code/GenModels)
- Summary: wiki/synthesis/2026-07-28/conference-digest.md
- Coverage: 12+ venues, 50+ papers, 13+ labs across 17 sections
- Updated: wiki/index.md (added conference-digest entry)
- New pages: wiki/synthesis/2026-07-28/conference-digest.md
- Contradictions: none

## [2026-07-28] synthesis | LLM Tech Report Digest — 2026-07-28 (19 companies)
- Summary: wiki/synthesis/2026-07-28/tech-report-digest.md
- Coverage: 19 companies, latest reports up to July 2026
  - DeepSeek: V4-Pro (1.6T/49B MoE) + V4-Flash (284B/13B), CSA+HCA compression, Muon optimizer, 33T tokens, 1M context
  - OpenAI: GPT-5 (SME 1400+ experts, dynamic reasoning, 256K tokenizer)
  - Meta: LLaMA 4 Scout (10M ctx, 109B), Maverick (400B), Behemoth (1.8T preview) — arXiv WITHDRAWN
  - Google: Gemini 1.5 (10M ctx Pro, 2M Flash), 99.2% needle recall, undisclosed params/training
  - Anthropic: Claude Opus 4.7 (1M ctx) + Sonnet 4.6 (200K), Constitutional AI+RLHF
  - Mistral: Magistral-Small/Medium (reasoning, 35+ languages, 128K ctx)
  - Qwen3: Dense+MoE 0.6B–235B, 36T+ tokens, Hybrid Thinking, Apache 2.0
  - 01.AI: Yi-Lightning (Enhanced MoE), RAISE safety, Arena #6
  - Baichuan: M4 medical agent (Jun 2026), M3 235B outperforms GPT-5.2 on HealthBench
  - Microsoft: Phi-4-reasoning-vision-15B (200B tokens), Mixture-of-LoRAs, o3-mini distillation
  - Apple: AFM 2025 (3B on-device + PT-MoE server), Parallel-Track Transformer, 2-bit QAT
  - NVIDIA: Nemotron 3 Ultra (550B Mamba-Attention Hybrid, 29B active), 128K ctx
  - xAI: Grok 4 (256K ctx, pretraining-scale RL, ARC-AGI V2 SOTA 15.9%), no arXiv
  - Amazon: Nova Premier (1M ctx, 200+ languages, distillation teacher)
  - Zhipu: GLM-5 (744B/40B, DSA sparse attention, 7 domestic GPU platforms, 28.5T tokens)
  - InternLM: Intern-S1-Pro (1T MoE+Mamba, science foundation model, 256K ctx)
  - Moonshot: Kimi K2.5 (1T/32B MoE, Agent Swarm, joint vision-text RL), K3 2.8T preview
  - StepFun: Step 3.5 Flash (196B/11B, MTP-3 100-300 tok/s), SWE-bench 74.4%
  - ByteDance: Seed2.0 Pro/Lite/Mini, 4-dim evaluation, ~1/10 cost vs GPT-5.2
- Key trends: MoE mainstream (15+ companies), 10M context (Scout/Gemini), Mamba/SSM revival, agent capabilities standard, native multimodal, domestic GPU adaptation
- Updated: wiki/index.md (added tech-report-digest entry)
- New pages: wiki/synthesis/2026-07-28/tech-report-digest.md
- Contradictions: Meta LLaMA 4 arXiv paper WITHDRAWN

## [2026-07-28] synthesis | WorldQuant 101 Alpha 因子选股日报 (2026-07-28)
- New page: wiki/synthesis/2026-07-28/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子框架筛选美股 Top 20
- Market: S&P 7,413(+0.02%)/Nasdaq 24,932(-0.18%)/Dow 52,210(+0.51%)/VIX 18.67
- Factors: Alpha#1 动量(12次/60%) + Alpha#6 量价(9次/45%) + Alpha#19 均值回复(6次/30%) + Alpha#41 趋势(5次/25%) + Alpha#53 反转(4次/20%)
- Top 5: AAPL(9.5)/JPM(9.3)/BAC(9.2)/ABBV(9.0)/RTX(9.0)
- Sectors: Healthcare 5只 + Financials 4只 + Industrials 3只 + Tech 2只 + Energy 2只 + Comms 1只 + Staples 1只 + RE 1只 + Utilities 1只
- Key themes: AAPL创历史新高$4.96T反超NVDA登顶/芯片SOX距6月高点-21%技术性熊市; 板块轮动→金融+医疗+消费必需品; Healthcare 5只入选为当日最大板块; 能源板块短期回调提供入场机会; 本周财报密集周(MSFT/META 7/29, AAPL/AMZN 7/30, Fed 7/31)
- Key catalysts: 7/29 MSFT+META财报/7/30 AAPL+AMZN+MA+V财报/7/31 Fed决议(加息概率38%)/8/1关税截止
- Updated: wiki/index.md, wiki/log.md

## [2026-07-29] synthesis | Tech Report Digest
- New page: wiki/synthesis/2026-07-29/tech-report-digest.md
- Coverage: 20 major AI companies — DeepSeek (V4/V3.2), OpenAI (GPT-5 System Card), Meta (LLaMA 4), Google (Gemini 2.5), Anthropic (Claude Opus 4), Mistral (Large 3), Alibaba (Qwen3), Microsoft (Phi-4), Apple (AFM 2025), NVIDIA (Nemotron 3 Ultra), xAI (Grok 4), Amazon (Nova), Zhipu AI (GLM-5), Shanghai AI Lab (Intern-S1-Pro), Moonshot AI (Kimi K2), StepFun (Step3), ByteDance (Seed 2.0), 01.AI (Yi-Lightning)
- Company count: 20 (18 active with reports, Baichuan no recent report found)
- Report count: 30+ technical reports / system cards
- Key themes: MoE dominance (90%+ of new architectures); Hybrid Mamba-Attention (Nemotron 3); 1M+ context becoming standard (6 companies); Reasoning models with budget control (GPT-5, Gemini 2.5, Qwen3); Agentic RL training pipeline (DeepSeek V3.2, GLM-5, Kimi K2); Low-precision pre-training validation (NVFP4, FP4 quantization); Multi-modality unified (Llama 4, Gemini 2.5, Step3)
- Updated: wiki/index.md, wiki/log.md

## [2026-07-29] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-29)
- New page: wiki/synthesis/2026-07-29/investment-daily.md
- Coverage: 7大板块, 50+ stocks — 美股AI芯片恐慌扩散（SOX-6%道指+537纳指-55，大轮动极致化）、港股汽车暴走（工信部智能EV"十五五"规划：理想+11%/比亚迪+4.6%）、A股算力光模块逆势暴涨（英伟达H20紧急订单30万片+上海6亿算力券）、中概ADR（BABA Qwen 3.8 Max + Apple合作）、新能源EV（BYD Q2纯电超越特斯拉、台积电H20订单）、AI热点（MSFT/META财报"审判日"、NVIDIA $7500亿循环融资CDS创新高、AMD Core Scientific $140亿、Broadcom Samsung $2000亿MOU、Kimi K3 2.8T开源、Grok 4.6预告、功率半导体涨价潮）
- Updated: wiki/index.md, wiki/log.md
