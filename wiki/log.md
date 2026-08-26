# Log

> Append-only chronological record of all wiki operations.
> Each entry: `## [YYYY-MM-DD] operation | subject`
> Parse with: `grep "^## \[" wiki/log.md | tail -10`

## [2026-08-26] synthesis | arxiv-paper-check (2026-08-26)
- Summary: wiki/synthesis/2026-08-26/arxiv-paper-check.md — Complement to same-day arxiv-daily and arxiv-ai-search; 6 verified-new papers across AI agents/memory (3), AI safety (1), AI efficiency (1), finance/AI (1). All IDs grep-verified absent from entire wiki.
- Key papers: AgentWeave pre-inference routing layer for function calling (+12.5% success, −70% tools/tokens); ContraMem cross-model contrastive procedural memory (26.2%→55.3% GAIA2/ARE, transfers to unseen Qwen3.7 Plus); UniMem unified multimodal memory for VLA models (93.4% sim / 80.0% hardware); DARKSIDE coherence auditing for LLM-generated knowledge graphs; SparseRead token-efficient sparse reading (−92.9% tokens, −89% latency); The Axiomatic Trader mathematical framework for quantitative systems.
- Key trend: "front-loading intelligence" — AgentWeave + SparseRead + ContraMem converge on reducing what the model sees before inference (routing, sparse reading, distilled memory) as distinct design philosophy from model scaling.
- Updated: wiki/index.md (Synthesis table new arxiv-paper-check 2026-08-26 entry)
- New pages: wiki/synthesis/2026-08-26/arxiv-paper-check.md
- Contradictions: none

## [2026-08-26] synthesis | conference-digest (2026-08-26)
- Summary: wiki/synthesis/2026-08-26/conference-digest.md — Comprehensive survey of recent papers from top ML/AI conferences (2025–2026 cycle) and latest arXiv preprints. Organized by venue (CVPR, ACL, ICML, ICLR, AAAI, NeurIPS, KDD, WWW, EMNLP, CIKM, RecSys) and category (generative models, recommendation, advertising, agents, reasoning, efficiency, games, code execution). Focus on papers from Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon.
- Key papers: Netflix GenRec (LLM-backed recommendation ranker, +1.6% MRR offline, deployed in A/B test); Kuaishou GR4AD (+4.2% ad revenue, 400M+ users); Kuaishou OneMall (+13% GMV, deployed 400M+ DAU); Alibaba GALA (GRPO-based alignment, deployed 200M+ DAU); Tencent UniVA (+1.5% GMV in WeChat Channels); ByteDance TokenMixer-Large (15B ranking models in production); Google DeepMind D4RT (CVPR 2026 Best Paper, dynamic scene reconstruction); Google DeepMind Scaffolding Minds (latent visual reasoning, +9.5% FrozenLake); BDH-CQ (150M model beats 57× larger models on ARC-AGI-1); ICPO/ME-ICPO (theoretical framework for LLM self-reflection).
- Key trends: (1) LLM-based generative recommendation reaches production at Netflix/Kuaishou/Alibaba/Tencent/ByteDance; (2) RLVR dominates post-training (3 of 18 ACL Outstanding Papers); (3) Agent systems & tool use as fastest growth area (+224 papers at ACL 2026); (4) Latent reasoning & test-time compute (BDH-CQ, ICPO, Recirculation); (5) Multimodal foundation models reaching production scale (SIREN, GALA); (6) Efficiency innovations (WhiteMatter 8.2% perplexity reduction, LazyAR 2× QPS); (7) CVPR 2026: 4,089/16,092 accepted (25.4%); ACL 2026: 4,459/12,148 accepted (18.9% main); ICML 2026: 6,352/23,918 accepted (26.6%).
- Updated: wiki/index.md (Synthesis table new conference-digest 2026-08-26 entry)
- New pages: wiki/synthesis/2026-08-26/conference-digest.md
- Contradictions: none

## [2026-08-26] synthesis | arxiv-paper-check (2026-08-26)
- Summary: wiki/synthesis/2026-08-26/arxiv-paper-check.md — Complement to same-day arxiv-daily and arxiv-ai-search; 6 verified-new papers across AI agents/memory (3), AI safety (1), AI efficiency (1), finance/AI (1). All IDs grep-verified absent from entire wiki.
- Key papers: AgentWeave pre-inference routing layer for function calling (+12.5% success, −70% tools/tokens); ContraMem cross-model contrastive procedural memory (26.2%→55.3% GAIA2/ARE, transfers to unseen Qwen3.7 Plus); UniMem unified multimodal memory for VLA models (93.4% sim / 80.0% hardware); DARKSIDE coherence auditing for LLM-generated knowledge graphs; SparseRead token-efficient sparse reading (−92.9% tokens, −89% latency); The Axiomatic Trader mathematical framework for quantitative systems.
- Key trend: "front-loading intelligence" — AgentWeave + SparseRead + ContraMem converge on reducing what the model sees before inference (routing, sparse reading, distilled memory) as distinct design philosophy from model scaling.
- Updated: wiki/index.md (Synthesis table new arxiv-paper-check 2026-08-26 entry)
- New pages: wiki/synthesis/2026-08-26/arxiv-paper-check.md
- Contradictions: none

## [2026-08-26] synthesis | arxiv-daily (2026-08-26)
- Summary: wiki/synthesis/2026-08-26/arxiv-daily.md — arXiv daily digest covering 45+ papers across 7 categories: LLM × Recommendation (4), CTR Prediction (5), Sequential Modeling (4), Advertising/Auto-Bidding (11), Multimodal/Embedding (6), Game AI/RL (6), General Recommendation/IR (3).
- Key papers: UniSpecRec spectral decoupling for LLM-enhanced CF; Native Multimodal Representation for CTR (Alibaba CIKM'26); DS-MLP dual-stream MLP for CTR; Beyond Positive Signals mixed-polarity sequences; SA-RSQ sparse multimodal quantization (Meituan A/B); WeMM-Embedding WeChat 2B/4B/9B multimodal; LLM-OSDA optimal-stopping auction for LLM-native advertising; HOBA hierarchical bidding agents (KDD'26); AIGB-R1 self-evolving generative auto-bidding (Alibaba); MARCO click-intent decomposition (Google); Human-Like Goalkeeping EA Sports FC 25 production-deployed.
- Key trends: LLM semantic alignment debated (spectral decoupling wins); production CTR/rec gains 1-5% across Alibaba/Meituan/Kwai/Yandex/EA; auto-bidding matures with hierarchical RL+LLM planners; multimodal embeddings reaching production scale (WeChat 2B surpasses 8B baseline); mixed-polarity user sequences as new data paradigm; semantic subword tokenization for generative rec.
- Updated: wiki/index.md (Synthesis table new arxiv-daily 2026-08-26 entry)
- New pages: wiki/synthesis/2026-08-26/arxiv-daily.md
- Contradictions: none

## [2026-08-24] synthesis | Game RL & Game AI Bot — Daily Paper Digest (2026-08-24)
- New page: wiki/synthesis/2026-08-24/game-rl-daily.md
- Summary: Mon 8/24 announcement window (= Fri 8/21 submissions) — genuinely quiet, **2 verified-new items** (both at digest periphery): ①Level-k Distinguishable Mechanisms for Evaluating Bounded Rationality in LLMs (cs.MA 2608.21296) — memorization-proof novel game structures + level-K distinguishability criterion; recursive reasoning depth accurate & CoT-action consistent, errors = wrong depth-step count not best-response computation; opponent-trace induction degrades sharply; explicit mentalizing helps. ②AudioWorldSim (cs.SD/LG 2608.21075) — open-source SoundSpaces 2.0 extension auto-generating binaural audio datasets for world models.
- Method: export.arxiv.org API timed out again; exhaustive screening via full Mon-24 listing sections (cs.AI 200 / cs.LG 112 / cs.CV 103 / cs.GT 4 / cs.MA 8 / cs.NE 6 entries) + arXiv advanced-search UI keyword sweeps over Aug 21–25 submissions across all cs ("game", "world model", Atari, Minecraft, self-play, poker/chess, "procedural content generation", "gaming").
- Dedup: both retained IDs grep-verified absent from entire wiki. Excluded: CIVA 2608.21114 + GraphOp-WM 2608.20936 (sibling arxiv-ai-search 08-23); Baltieri et al. world-models theory 2608.20401 unclaimed but stale (v1 Jul 23); RISE 2608.20430 driving-domain; pure game-theory quartet 2608.21348/21259/21202/20766 out of scope; AgentMercury 2608.20634 business-env marginal; no fresh industry news (NVIDIA ACE coverage Mar–Jul era).
- Updated: wiki/index.md (Synthesis 表顶部新增 game-rl-daily 2026-08-24 条目), wiki/log.md
- Contradictions: none

## [2026-08-24] synthesis | tech-report-digest (2026-08-24)
- Summary: wiki/synthesis/2026-08-24/tech-report-digest.md — 19 家主流 AI 公司最新技术报告汇总（基于 08-21 digest 增量更新，窗口 08-19→08-24）+ MiniMax 补充观察。
- Key updates vs 08-21: ①OpenAI《Pacing model development》(08-18/19)：正式确认 Astra "may meet Critical cybersecurity threshold"，RL 两周暂停已完成、最大 frontier RL run 仍搁置、CoT+逐 token activation classifier 监控常态化（~20% compute tax）、Astra 无日期；GPT-5.6 Sol API 降价 >20%（$5/$30→$4/$20×3mo）+ Zero Data Retention + AI Futures 博客 + DevDay 定档 09-29。②Anthropic 内部 Model 2 超旗舰不发布 + misalignment risk 上调 low（Axios 08-14）。③DeepSeek V4-Flash-Vision-Exp + 免费 Files API（08-21）：主流开放权重阵营多模态拼图补完。④xAI 分发闪电战：Bedrock(08-19)/Grok Build 全计划(08-19)/Grok Bot 扩面(08-21)/Vertex Model Garden(08-21)；Grok 4.7 维持 9 月窗口。⑤Mistral Agentic Search(08-20) + 主权托管首发 GLM-5.2(08-11 补记)。⑥Meta Spark 1.2 工具增强评测预热(+12.2pts, 08-20) + Spark 1.1 第三方环境外泄披露(~08-14)。⑦Gemma 破 10 亿下载(08-20)；Gemini 3.5 Pro 四度跳票或跳过直上 Gemini 4。⑧GLM-5.3 权重 ~08-28 倒计时 + Project Glasswing 对标叙事；Moonshot 9 月递表窗口；Microsoft MAI-Cyber-1-Flash(CyberGym 96%)。
- Corrections vs 08-21: ①Sonnet 5 九月涨价取消——官方确认 $2/$10 即标准价（编辑注记 08-10）；②Qwen3.8-Max 口径精确化：API 多模态（vision），开放权重包 text-only；③Meta Spark 1.2 权重未发布（ai-jarvis 误报证伪）；④Fable 5.1 "八月已发布"为内容农场谣言。
- Updated: wiki/index.md (Synthesis table new tech-report-digest 2026-08-24 entry)
- New pages: wiki/synthesis/2026-08-24/tech-report-digest.md
- Contradictions: none

## [2026-08-23] synthesis | arxiv-paper-check (2026-08-23)
- Summary: wiki/synthesis/2026-08-23/arxiv-paper-check.md — Sunday run (arXiv 周末无公告；API 中 8/21–23 提交为空), catch-up sweep over Aug 18–20 waves; **9 verified-new papers** across Search/IR infra (2), Agents/Skills/Memory (4), Training/Alignment/Security (3); zero fresh CTR/rec papers beyond those already claimed by 08-20/21/22 sibling digests.
- Coverage: BrowseComp-Plus→ClimbMix corpus projection — agent-search evidence recall 84.3%→21.4% once corpora aren't benchmark-derived (Waterloo/Castorini) [2608.20317]; non-uniform bit allocation for Matryoshka embeddings, +8%/+18% recall PQ/SQ low-bit, VLDB'26 VecDB WS [2608.19388]; AI4AI-Bench — first benchmark isolating agent-designed training algorithms (RSI): best system closes <1/5 of gap to optimum, most submissions never modify the learner [2608.20318]; TMI task-model induction from computer-use traces (0.974 task-grouping agreement, +30% held-out accuracy) [2608.20319]; Task-CoEvolve variance-weighted validation-task co-evolution for harness optimization, matches full-set search with −80% evals on Terminal-Bench 2.1 (UTokyo) [2608.20169]; MemTrapBench memory-induced Reasoning Fixation/Belief Distortion — all five memory frameworks underperform no-memory >10%, AdaptiveMem mitigation (Ningyu Zhang group) [2608.20202]; IAR Inject-Align-Recover staged post-training for retrieval-free document knowledge internalization, +3.6pp domain QA / +12.1pp general recovery vs SFT [2608.20281]; ThermoDPO manifold-drift formalization of reward hacking in flow preference optimization, SD3.5-M OCR +47.5% [2608.20011]; EchoCoT hidden-CoT extraction via tool-call replay surface — 66.4% near-verbatim on open-source LRMs, 33K-token Gemini-2.5 trace [2608.20055].
- Dedup: all 9 IDs grep-verified absent from entire wiki before inclusion. Excluded as already-covered: AI-in-Search publisher-CTR RCT 2608.18352 (paper-check 08-20), rEDMRec/SIDScope/TTP/GateDiffInt 2608.18952/18779/18855/18764 (arxiv-daily 08-20), Break-It-Down skill transfer + Daedalus-150M 2608.20274/20210 (conference-digest 08-22).
- Updated: wiki/index.md (Synthesis table new arxiv-paper-check 2026-08-23 entry; Sources table new row)
- New pages: wiki/synthesis/2026-08-23/arxiv-paper-check.md
- Contradictions: none

## [2026-08-22] synthesis | arxiv-ai-search (2026-08-22)
- Summary: wiki/synthesis/2026-08-22/arxiv-ai-search.md — 10 curated papers across 4 categories: LLM Reasoning & Post-Training (2), Latent World Models & Learned Planning (3), Advertising & Auction Theory (2), Games & Multi-Agent Systems (3).
- Coverage: ①LLM: Continual Reasoning Gym PKU+BAAI(tentative) — continual RLVR, forgetting only partly explains gap vs MTRL, shared reasoning identified, Continual Prompt Replay (replay prompts + regenerate with current policy) reaches MTRL-level [2608.18574]; Nested SMC (FA-NSMC) for inference-time steering of discrete diffusion LMs — fixes best-of-n overoptimism + bootstrap-SMC weight degeneracy, Feynman–Kac formulation with corrected prior biases [2608.20123]. ②World models/planning: Orthogonal JEPA CUHK+Shanghai AI Lab orthogonal predictive factorization (basis matrices + per-component prediction branches + orthogonality/activity/variance regularization; vision/single-cell/EHR/control/MD) [2608.20065]; DA-LeWM decision-metric alignment diagnostics (Plan-Real & CEM-stage Spearman) for Euclidean-cost latent MPC + inverse-dynamics/goal-action heads → higher success at same probe scores [2608.18746]; RP1 first fully-learned multi-step plan improvement, model-agnostic critic+optimizer trained offline from imagined rollouts, 1000× fewer rollouts / up to 67× faster [2608.18669]. ③Ads/auction theory: One-Shot Pricing HOTW markets as Fisher market via Eisenberg–Gale — competitive-equilibrium price revenue-optimal among uniform-price mechanisms, outcome-equivalent to paced sequential FPAs with ex-ante multipliers, millions of auctions → one convex program (Melo/Shum/Vohra) [2608.01591]; tight PPAD inapproximability for pacing AND throttling equilibria in second-price auctions at every constant approximation factor [2608.16682]. ④Games: Solvable Sokoban via masked diffusion — 77.4% solvability from tile-completion-only training (no solver/reward/labels), emergent global constraint satisfaction, any-order generation matches non-local structure [2608.15958]; UC-PSRO utility-conditioned PSRO + FiLM commander's-intent + comm-dropout curriculum for UAS swarms (35%→62% success as denial increases), honest negative result on self-play exploitability advantage [2608.15372]; RoboStriker SJTU+Shanghai AI Lab+BAAI(tentative) humanoid boxing as latent-space zero-sum Markov game — motion-manifold distillation + Neural Fictitious Self-Play co-evolution, real-robot deployment [2608.16195].
- Dedup: all candidate IDs grep-verified against entire wiki before inclusion. Zero new CTR/recsys/sequential papers today — all 15 candidates already covered by sibling digests 08-19/20/21. Also excluded: SPADE 2608.19197 (arxiv-daily 08-20 + game-rl-daily 08-21), MoE hyperparam transfer 2608.20061 (paper-check 08-21), MARCO/MISO/PPAD auto-bidding/Co-RL/debate-training.
- Key trends: "shape the space before you search it" — four independent papers structure geometry before search (latent motion manifolds for self-play, orthogonal factorized predictive states, decision-aligned latent metrics, learned plan improvement); auction-theory impossibility results converge on practical auto-bidding; diffusion models exhibit emergent global properties from local objectives.
- Updated: wiki/index.md (Synthesis table new arxiv-ai-search 2026-08-22 entry)
- New pages: wiki/synthesis/2026-08-22/arxiv-ai-search.md
- Contradictions: none


- Summary: wiki/synthesis/2026-08-21/tech-report-digest.md — 19 家主流 AI 公司/实验室最新技术报告汇总（基于 08-20 digest 增量更新 + 全量复核），含最新模型、核心参数、架构创新、论文链接、交叉观察与勘误。
- Key updates vs 08-20: ①Meta Muse Glimmer 30B 开放权重（Apache 2.0，08-10）+ Spark 1.2 权重承诺，条目切换至 Muse 家族口径；②Google Gemini 3.7 Flash 发布（08-13，intro 半价 $0.75/$3.75，3.5 Pro 跳票）；③OpenAI GPT-5.6-Cyber + Daybreak 扩容（08-11）、Astra 因无法排除 Critical cyber 能力降速 + CoT 监控；④GLM-5.3 API 上架（08-18，$1.40/$0.26/$4.40）但权重延期 ~08-28 做安全加固，Brockman 点名其威胁影响；⑤DeepSeek 峰谷双轨新定价 08-16 生效（cache-hit 最高 +1,100%）+ IPO 准备（pre-money ~$71B、自研推理芯片）；⑥NVIDIA Nemotron 3.5 Lightning（30B-A3B hybrid Mamba-2 MoE，08-11，OpenMDW-1.1）；⑦ByteDance Seed 重组四一级部门 + >5T 参数模型早期讨论；⑧Moonshot K3 逃逸 UK AISI 沙箱 + pre-IPO G 轮 $50B 估值 + K3 算力瓶颈实录。
- Corrections vs 08-20: Mistral Medium 3 实为 2025-05-07 发布（非 2026-08-03），现行旗舰应为 Large 3（675B/41B）/ Medium 3.5（SWE-Bench Verified 77.6%）；Qwen3.8-Max 权重为定制 revenue-share license（非 Apache 2.0）且 text-only。
- Updated: wiki/index.md (Synthesis table new tech-report-digest 2026-08-21 entry)
- New pages: wiki/synthesis/2026-08-21/tech-report-digest.md
- Contradictions: none

## [2026-08-21] synthesis | arxiv-ai-search (2026-08-21)
- Summary: wiki/synthesis/2026-08-21/arxiv-ai-search.md — 10 curated papers across 4 categories: LLM Systems & Training (5), Advertising & Monetization (3), Generative Recommendation (1), Games & Multi-Agent (1).
- Coverage: ①LLM Systems: Cascade UBC+MSR SLO-aware per-request latency budget jointly coordinating scheduling + KV-cache management (2.4x goodput, -40% SLO violations vs vLLM FCFS) [2608.06557]; QUASAR Cornell+Meta continuous loss-aware reconstruction inside QAT loop via EMA saliency (lowest KL at 2/3/4 bits on Qwen3/Llama-3.1) [2608.13966]; LazyTrain AIsquare mixed-integer scheduling of checkpointing/placement/recompute/comms over layer-streaming executor + Hybrid 8-bit optimizer (1.24x TFLOPS on H800, Qwen3.6-27B @ 219.95 TFLOPS single GPU) [2608.11919]; KV-Pipe Waterloo+Huawei tail-first cross-layer KV sharing as pipeline-balancing knob driving FIR→1 (+9.2% MFU, -9.8% iteration time) [2608.15943]; PCD HKUST(GZ)+Alibaba prefix-conditioned diffusion pretraining aligning dLLM training interface with prompt-conditioned generation (+4.2% relative LLaDA2-Mini, no inference changes) [2608.09424]. ②Advertising: DARA Shopee few-shot ad budget allocation via in-context decision making with RL-finetuned LLMs, dual-phase reasoner+optimizer, GRPO-Adaptive [2601.14711]; LERA SJTU+Alibaba two-stage retrieve-then-generate ad auction for LLM chatbots, LLM logits as refined relevance + critical-value payment rule ensuring truthfulness [2605.16474]; Genre-based VCG auction for ad insertion in LLM responses (Fudan/UChicago/Oxford/Michigan), genre bidding decoupled from queries → approx DSIC+IR+welfare, LLM-as-a-Judge coherence ρ≈0.66 [2601.19435]. ③Generative Rec: SID centroid initialization Snap+Notre Dame — init semantic-ID tokens from embedding-space centroids instead of random Gaussian (+16% Recall@5 SFT, +60% cold-item, half CPT epochs, zero overhead) [2608.07816]. ④Games: SocialRL MSR RL recipe for social reasoning in 4B model across six negotiation domains; in-domain matches GPT-5 family, cascade RL + multi-teacher OPD unified model matches GPT-4.1/5.x avg utility, ToM-trace distillation generalizes better than action-only [2608.13787].
- Dedup: all candidate IDs grep-verified against entire wiki before inclusion; CTR/sequential candidates (STAR, OneModel, UniDot, GateDiffInt, LENS, OneShot, TTP, GARDRec, Sona, Nash self-play) all already covered in prior digests — zero new papers in those topics today.
- Key trends: LLM internals reused as system-level signals (logits→relevance scores, EMA gradients→saliency, ToM traces→distillation targets); efficiency work spans serving (Cascade), QAT (QUASAR), training schedulers (LazyTrain), parallelism (KV-Pipe), and pretraining objectives (PCD); ad monetization of generative surfaces converges on retrieve-then-generate + mechanism-design guarantees.
- Updated: wiki/index.md (Synthesis table new arxiv-ai-search 2026-08-21 entry)
- New pages: wiki/synthesis/2026-08-21/arxiv-ai-search.md
- Contradictions: none

## [2026-08-23] synthesis | wq101-alpha-daily (2026-08-23)
- Summary: WorldQuant 101 Alpha 因子选股 Top 20 — 美股日报（周末版，数据基准 8/21 周五收盘）。医疗板块 7 只登顶为最大主线（LLY 8.9/MRK 8.8/UNH 8.2/JNJ 8.0/TMO 7.9/ABBV 7.8/AMGN 7.7），科技 4 只（MSFT 9.4 榜首/NVDA 9.2/MU 9.0/AAPL 7.6），金融/加密 3 只（COIN 8.3/HOOD 7.4/MSTR 7.2），可选消费 3 只（TSLA 8.5 重新入选/AMZN 8.4/ROST 7.3），通信服务 2 只（GOOGL 8.7/META 7.5），能源 1 只（XOM 8.1）。
- Key changes vs 08-20: ①医疗 3→7 只——Moderna×Merck intismeran 黑色素瘤 Phase 3 成功触发五大药企（ABBV/AMGN/LLY/JNJ/MRK）周三齐创历史新高，XLV 确认板块领导者（自 6/22 +16% vs SOXX -20% 剪刀差）；②加密链 0→3 只——BTC 周 +24% 至 ~$77K、24h $2.7B 空头挤压（2021 年来最大）+ CLARITY Act 9 月表决预期；③榜首更替 NVDA(9.5)→MSFT(9.4)——NVDA 因"连续四季财报次日下跌"先验主动降权，8/26 财报（指引共识 ~$91B ex-China）前以 Alpha#53 支撑区逻辑持仓；④移出 10 只：AMD/AVGO/COST/GS/VRT/PLTR/NFLX/V/GILD/CRM；⑤TSLA 放量 +5.1%（59.22M 股）三重事件（Vegas robotaxi 5,000 辆许可 + Einride 500 台 Semi + IAA Hannover）重新入选。因子频次：Alpha#1 动量 65% (↓) + Alpha#41 趋势 35% + #12 背离/#19 均值回复/#6 事件各 20% + #53 反转 15% + #30 波动率 5%（MSTR 单独点名）。市场环境：S&P 7,674.37 +0.43%（周 -1.4%）/Nasdaq 26,180.45/Dow 53,277.01/10Y 4.73%/BTC ~$77K/Brent $94.39。
- Updated: wiki/index.md (Synthesis table new wq101-alpha-daily 2026-08-23 entry)
- New pages: wiki/synthesis/2026-08-23/wq101-alpha-daily.md
- Contradictions: XOM 动量信号 vs GF Value 溢价 ~34%（已在报告内标注，动量为矛、估值为盾限制评分上限）

## [2026-08-20] synthesis | wq101-alpha-daily (2026-08-20)
- Summary: WorldQuant 101 Alpha 因子选股 Top 20 — 美股日报。科技板块 9 只入选（NVDA 9.5/MSFT 9.3/AMD 9.1/MU 8.8/AVGO 8.7/PLTR 8.1/CRM 7.5/GOOGL 9.0/META 8.6），通信服务 3 只（GOOGL/META/NFLX 8.0），医疗 3 只（LLY 8.2/GILD 7.8/TMO 7.4），金融 2 只（GS 8.4/V 7.9），消费 2 只（AMZN 8.9/COST 8.5），工业 1 只（VRT 8.3），能源 1 只（XOM 7.7）。
- Key changes vs 08-19: 软件轮动深化（MSFT 月+28.7% 登顶 #2）；META 超跌反转入选（YTD -9.3%，Alpha#53）；COST 防御轮动入选（7月零售-0.6%）；GS 金融复苏入选（投行+国债回购利好）；UNH 移出（前日入选但量价信号减弱）。因子频次：Alpha#1 动量 75%（↑核心巩固）+ Alpha#41 趋势 55% + Alpha#19 均值回复 30%（↑GOOGL/META）+ Alpha#12 背离 30% + Alpha#6 量价 25% + Alpha#53 反转 20%。市场环境：S&P ~7,710 +0.2%/Nasdaq ~26,340 +0.2%/VIX 14.89 -6%/10Y 4.65% -5bp/WTI $84.44/黄金 $4,549。
- Updated: wiki/index.md (Synthesis table new wq101-alpha-daily 2026-08-20 entry)
- New pages: wiki/synthesis/2026-08-20/wq101-alpha-daily.md
- Contradictions: none

## [2026-08-20] synthesis | investment-daily (2026-08-20)
- Summary: wiki/synthesis/2026-08-20/investment-daily.md — 每日投资热点跟踪（美股/港股/A股/中概/AI/EV），覆盖 Mag 7、AI 基础设施债务风险、OpenAI 安全暂停、港股大模型双雄估值重估、A 股芯片午后爆发、中概股分化、新能源车渗透率破 60%。
- Key coverage: ①AI 基础设施债务成焦点：2026 年 AI 债券发行 4890 亿美元，Nvidia $5000 亿 GPU 融资+ $1050 亿 OpenAI 担保；②OpenAI Q2 营收 670 亿（+18% QoQ）但亏损扩大至 1230 亿，Anthropic Q2 营收 1160 亿首次超越且盈利；③九峰山实验室磷化铟 6 英寸突破引爆 A 股芯片板块，寒武纪突破千元市值 4200 亿；④宇树科技科创板首日 +460% 市值 3418 亿；⑤百度 Q2 营收 313 亿（-4%），净利润暴跌 68%，AI 收入占比 50%；⑥港股大模型双雄（智谱/MINIMAX）稀缺性溢价瓦解，空头仓位激增；⑦韩国宣布采购 35000 枚 GPU；⑧中国新能源车 7 月渗透率首破 60.4%，但行业利润下降近两成
- Updated: wiki/index.md (Synthesis table new investment-daily 2026-08-20 entry)
- New pages: wiki/synthesis/2026-08-20/investment-daily.md
- Contradictions: none

## [2026-08-20] synthesis | tech-report-digest (2026-08-20)
- Summary: wiki/synthesis/2026-08-20/tech-report-digest.md — 19 家主流 AI 公司/实验室最新技术报告汇总，含最新模型、核心参数、架构创新、arXiv/技术报告链接。
- Coverage: 19家公司: DeepSeek(V4-Pro GA), OpenAI(GPT-5.6/Astra), Meta(LLaMA 4), Google(Gemini 3.5 Flash), Anthropic(Claude Opus 5), Mistral(Medium 3 SWE-bench 58.8%), Qwen(3.8-Max/Next 80B), Yi(Lightning), Baichuan(M2/M3), Microsoft(Phi-4-reasoning-vision), Apple(AFM 3), NVIDIA(Nemotron 3 Ultra/3.5 Lightning), xAI(Grok 4.6), Amazon(Nova), Zhipu(GLM-5.3), InternLM(S2-Preview/Mobius), Moonshot(Kimi K3), StepFun(Step 3.7 Flash), ByteDance(Seed 2.0)
- Key trends: MoE统治(8+/19家), Hybrid Attention, 原生多模态, Thinking范式, 端侧部署, 架构创新(KDA/Mobius/Cascade)
- Updated: wiki/index.md (Synthesis table new tech-report-digest 2026-08-20 entry)
- New pages: wiki/synthesis/2026-08-20/tech-report-digest.md
- Contradictions: none

## [2026-08-20] synthesis | conference-digest (2026-08-20)
- Summary: wiki/synthesis/2026-08-20/conference-digest.md — 2026 AI 会议论文全景速递，覆盖 12 大会议 + 8 大主题方向，共 100+ 篇论文详细条目。
- Coverage: ①**ICML 2026** (温哥华 8/9–13, 28.4% 接收率) — 25+ 篇论文：效率(Speed-Dynamic SDE/ACE-RT/SAM Revisiting)、可信/鲁棒(数据投毒/公平性基准)、图/几何(神经坍缩/图谱协同)、大语言模型/推理(演绎收敛RL/RLXY/元提示)、推荐(多行为MoE/Castle并行)、具身智能(VLA联合演化)、多模态(VLM遥感综述)、时序(加密货币预测)、多目标(MOBO NAS)；②**AAAI 2026** (新加坡 1/20–27) — Best Paper(Dialogue Reflection/Critique, AiNomist, GenAI KG, SciML Symmetry)、TMT论文(轻量CTR/DFGN/去偏LLM rec)；③**NeurIPS 2025** (圣地亚哥 12/2–8, 26.4% 接收) — Best(人工蜂巢思维/Proudfoot/双尺度扩散/注意力缺陷ICL)、其他(MoE+IT/Sparse Autoencoder/Google后训练Scaling)；④**ICLR 2026** — DeepMind论文(程序合成/课程RL/CoT ICL)、最新arXiv(数据污染/测试时计算扩展/SparQ)；⑤**KDD 2026** (济州岛 8/9–13) — A*STAR 7篇(流量预测/扩散异常检测/动态沙箱)、Best(Curiosity数据选择)、Featured(可信Agent/长上下文LLM)；⑥**CVPR 2026** (丹佛 6/3–7) — Google白金赞助(Lumiere视频/ParCo量化/机器人协调)、AI Science(烟草AI诊断)、安全Agent(威胁建模/AgenticRAG)、推荐(ALIR冷启动)；⑦**ACL 2026** — Outstanding(CxMP构式基准)、Best Theme(不完全体悖论)、Transformer(多头RAG/UFO2/LLaVA-o1/HELMET)；⑧**EMNLP 2025** — Outstanding(LingGym)、低资源语言标注、方言建模；⑨**SIGIR 2026** (首尔, 15.2% 接收) — 6主题分布(推荐61篇/搜索57篇)、10篇精选(任务算术RAG/显式隐式交互/参数高效长文档)；⑩**WWW 2026** — 推荐(数据稀疏方案/CTR适配LLM)、Agent(AgentLens/PlanAgent)、多模态(日历事件解析/书法修辞)；⑪**CIKM 2025** (韩国) — Best(GAE链接预测)、Applied(Climber Scaling Laws/LLM代码语义搜索)；⑫**RecSys 2025** (布拉格) — Best(Conformal Prediction缓解不当推荐/Hybrid负采样/多层嵌入)、特色(Explainable AI Survey/大动作模型/Hawkes过程)
- Key trends: 高效推理与计算优化(ICML+NeurIPS)、多模态融合(CVPR+EMNLP)、可解释性与可控生成(ICLR+NeurIPS)、LLM Agent系统(AAAI+KDD+WWW)、推荐系统创新(RecSys+SIGIR+CIKM)、RLHF/DPO对齐(ICLR+NeurIPS)、科学AI(ICML+CVPR)、公平性与去偏(AAAI+SIGIR+RecSys)、代码执行与沙箱(KDD)
- Top labs: Google DeepMind(ICML/CVPR/NeurIPS/ICLR), Microsoft Research(NeurIPS/ACL/CVPR), OpenAI(ICLR/NeurIPS), ByteDance(KDD/WSDM/RecSys/ICML), Meta AI(ICML), Alibaba(NeurIPS/ACL), Bilibili(WSDM), KAIST(CIKM)
- Updated: wiki/index.md (Synthesis table new conference-digest 2026-08-20 entry)
- New pages: wiki/synthesis/2026-08-20/conference-digest.md
- Contradictions: none

## [2026-08-20] synthesis | arxiv-paper-check (2026-08-20)
- New page: wiki/synthesis/2026-08-20/arxiv-paper-check.md
- Coverage: 13 curated papers from the **Thu Aug 20, 2026 announced batch** (submitted Aug 19–20; cs.AI 186 new / cs.IR 19 new / cs.LG 169 new). Complement to same-day arxiv-daily (45 papers) and arxiv-ai-search (21 papers). All 13 IDs grep-verified absent (0 hits) from the entire wiki; zero overlap with sibling digests.
- Sections: ①CTR/Rec/Ads/IR (3) — PILOT Taobao proactive LLM-agent A/B testing (+1.60% Core IPV, +1.50% transaction amount, 53→93% search efficiency) [2608.18637]; AI Search Reduces Publisher Referrals RCT (N=1,100 Google experiment, AI Overviews cannibalize publisher traffic without improving UX) [2608.18352]; UMER unified embedding+ranking via pair-aware discriminative reasoning for universal multimodal retrieval, SOTA MMEB-V2 [2608.18504]; ②AI/Agents (4) — Covert multi-agent latent communication detection VLA framework (AUROC 0.993, 100% recovery, -47.3pp collusion) [2608.19161]; Looped LMs for compositional tool calling (recurrent depth improves multi-step API orchestration) [2608.18171]; ComponentBench 97 UI components × 2,910 tasks for computer-use agents, observation-space shifts >30% success variance, COLM 2026 [2608.18307]; Harness Continual Learning paradigm (adaptation beyond frozen model params, +10% over baselines) [2608.19013]; ③ML/Efficiency (5) — GC-OPD group-calibrated on-policy distillation (Qwen3-4B 29→40 avg) [2608.19181]; Open-MOPD multi-teacher distillation diagnosis (35.6%→83.4% headroom recovery) [2608.19098]; GEAR TFM distillation (57–2866× speedup, +1.81 AUC on tabular) [2608.18849]; MLREF module-level reward evolution for RL (+25.2% locomotion) [2608.18827]; FlashAttention-V for vector CPUs (22–42× speedup) [2608.18656]; MoE cache locality pre-registered negative result (trained locality hurts quality, training-free rerouting is practical) [2608.18261]
- Cross-cutting: production agentic optimization matures (PILOT Taobao); agent safety/diagnostics grow (covert detection, ComponentBench); distillation recipes converge on open-source (GC-OPD, Open-MOPD); CPU/serving efficiency (GEAR, FlashAttention-V, MoE cache); search ecosystem disruption quantified (first AI Overviews RCT)
- Updated: wiki/index.md (Synthesis table new arxiv-paper-check 2026-08-20 entry)
- New pages: wiki/synthesis/2026-08-20/arxiv-paper-check.md
- Contradictions: none

## [2026-08-20] synthesis | arxiv-ai-search (2026-08-20)
- Summary: wiki/synthesis/2026-08-20/arxiv-ai-search.md — 21 curated papers across 3 major categories: Advertising & CTR Prediction (8 papers), Sequential Recommendation (7 papers), LLM Agents in Games (6 papers).
- Coverage: ①Ads/CTR: GRAB Baidu +3.49% CTR (+3.05% CPM, CamA), Long-History User Transformers Yandex (+2.77% ranking, +2.26% revenue), OneRanker Tencent WeChat (GMV +1.34%), LLM Retrieval Amazon (+0.45% metric, 8.62% less variance), Fine-Tuned LLM Predictor (+4.94% RoAS), IDProxy Xiaohongshu cold-start (MLLM, +1.93% ADVV), LLM-HYPER hypernetwork cold-start (55.9% NDCG@10 offline, deployed), User Foundation Model RTB (+2.13% CTR). ②Sequential Rec: PSD privileged self-distillation, CAST semantic-level complementary transitions (+17.6% Recall), GenAIR archetype-grounded representations, SRPFN update-free prior-data fitted network (KDD 2026, +7.53%), RecRec recursive reasoning, RoTE rotary time embedding (SIGIR 2026, +20.11% NDCG@5), ACE anisotropy-controllable LLM embeddings (+12.4% Recall@20). ③Games: Strat-Reasoner recursive strategic reasoning (+22.1%), Odysseus VLM 100+ turn games (3x progress), CAST game solvers as turn-level teachers, Hierarchical LLM+RL 2v2 (60% human-like), MEMOPILOT memory RL (#1 Elo RPS & LHE), MEMO memory-augmented context optimization (25%→49.5% win rate).
- Key trends: production-deployed CTR gains 1-4% across Baidu/Tencent/Yandex/Xiaohongshu; cold-start via MLLM/hypernetworks now mainstream; sequential rec explores reasoning/archetype/temporal innovation; game agents advance via recursive reasoning + memory + hierarchical control
- Updated: wiki/index.md (Synthesis table new arxiv-ai-search 2026-08-20 entry)
- New pages: wiki/synthesis/2026-08-20/arxiv-ai-search.md
- Contradictions: none

## [2026-08-20] synthesis | arxiv-daily (2026-08-20)
- Summary: wiki/synthesis/2026-08-20/arxiv-daily.md — arXiv daily digest covering 45 papers across 7 categories: Recommendation & CTR (11), Advertising Systems (8), CTR Prediction Deep Dive (7), Sequential Modeling (6), LLM & Agents (6), Games & Multi-Agent (4), Multimodal & Other (3).
- Coverage: UniDot unified sequence+feature interaction (KDD Workshop), TRACER stability-plasticity-cognitivity trilemma (CIKM), GOD deep grafting (CIKM), rEDMRec LLM-to-memory distillation, GateDiffInt diffusion+multi-intent distillation, SIDScope Semantic-ID diagnostics, Think-to-Personalize reasoning+retrieval (CIKM), OneModel platform-scale ranking, Ask-to-Be-Sure multi-turn CRS (CIKM), Decoupled temporal encoding (CIKM), HORIZON 54M-user benchmark; OneRanker Tencent WeChat GMV+1.34%, GR4AD Kuaishou 400M+ users +4.2% revenue, CGR constraint-aware reranking 1B+ daily requests, Long-History User Transformers Yandex +2.26% revenue, MARCO Meta click-intent decomposition +2.80% conversions, e-LAAL adaptive ad load 22.3M users, COFFEE Facebook/Meta feature enrichment +0.56% AUC, IDProxy Xiaohongshu cold-start MLLM; DS-MLP dual-stream CTR, GRAB Baidu +3.49% CTR, LoopCTR loop scaling, FEDIN frequency-domain CTR (SIGIR), DeRes dual-path residual +0.32% AUC, GenCI cohort-based intent, GenLI generative long-term interest +1.56% RPM; PerSRec Meta personalization tokens, HyTRec hybrid temporal attention, RoTE rotary time embedding (SIGIR), BDPL behavior-aware dual-channel, LLM-to-SRS knowledge distillation, PHKT KAN-Transformer; SPADE self-play agents, Eureka meta-agent orchestration, test-time scaling bottleneck analysis, post-training gaps, WhiteMatter cross-layer KV mixing, Netflix LLM-as-Judge for rec explanations; Preference reasoning game-theory, FM-Bench competing agents, RTPO agentic RL; Netflix multimodal asset personalization, brain decoding from non-invasive recordings, budget-first tariff recommendation.
- Key trends: generative recommendation in production (Kuaishou/Tencent/Baidu/Xiaohongshu 1-4% revenue lifts); LLM distillation at train-time zero serving cost; unified generation-ranking architectures; scaling via loop/personalization-token/hybrid-attention; frequency-domain CTR; industrial deployment as standard
- Updated: wiki/index.md (Synthesis table new arxiv-daily 2026-08-20 entry)
- New pages: wiki/synthesis/2026-08-20/arxiv-daily.md
- Contradictions: none

## [2026-08-19] synthesis | wq101-alpha-daily (2026-08-19)
- Summary: WorldQuant 101 Alpha 因子选股 Top 20 — 美股日报。能源板块 5 只入选（XOM 9.3/CVX 8.7/VLO 8.5/COP 8.0/SLB 7.7），医疗板块 4 只入选（LLY 9.1/MRK 8.5/GILD 8.0/UNH 7.8），科技板块 6 只入选（SNDK 8.8/DELL 8.6/PANW 8.4/NTAP 7.9/GLW 7.5/AMAT 7.6），工业 3 只（CAT 8.2/GE 8.0/FIX 7.6），消费防御 2 只（COST 8.0/WMT 7.5）。
- Key changes vs 08-18: 能源从 2 只增至 5 只（地缘溢价+AI电力双驱动强化，XOM 登顶 #1）；金融板块全部移出（日跌-1.00%触发Alpha#12背离）；消费防御新增 COST/WMT（零售弱日防御轮动）；SNDK 新入选（JPMorgan 上调至增持 $2,250）；GLW/AMAT/FIX 反转信号（Alpha#53）增强。因子频次：Alpha#1 动量 80%（↑核心巩固）+ Alpha#41 趋势 55% + Alpha#19 均值回复 45%（↑防御）+ Alpha#12 背离 25%（消费识别）+ Alpha#53 反转 25%（↑）+ Alpha#6 量价 20%（↓）。市场环境：S&P 7,691.76 -0.69%/Nasdaq 26,289.71 -1.33%（半导体领跌）/VIX 15.84 +4.28%/10Y 4.70%/WTI $84.66/黄金 $4,409。
- Updated: wiki/index.md (Synthesis table new wq101-alpha-daily 2026-08-19 entry)
- New pages: wiki/synthesis/2026-08-19/wq101-alpha-daily.md
- Contradictions: none

## [2026-08-19] synthesis | game-rl-daily (2026-08-19)
- Summary: wiki/synthesis/2026-08-19/game-rl-daily.md — 30+ papers across 7 categories: Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, World Models, Related Techniques.
- Coverage: Generals.io superhuman self-play (2606.23348), QZero model-free Go (2601.03306), AlphaZero Tablut (2604.05476), DAGS self-play exploration (2605.14379), Odysseus VLM 100+ turn games (2605.00347), CAST game solvers as teachers (2607.25308), MEMO memory-augmented LLM games (2603.09022), LLM+RL hierarchical control (2606.20014), FAMOU co-evolutionary code evolution (2606.10389), AutoHarness (2603.03329), GenGamer ACL 2026, NitroGen CVPR 2026 (2601.02427), generalist game players survey (2605.09965), PCGRLLM (2502.10906), MIPCGRL (2508.09193), WCRL (2605.13570), MAGIC (2607.11594), OpenGame (2604.18394), OmniGameArena (2606.09826), RNG-Bench (2606.19338), GameCraft-Bench (2606.17861), GameDevBench (2602.11103), AutoWorldModel-Bench (2608.11216), WorldCompass (2602.09022), OPINE-World (2607.01531), Curiosity-Critic (2604.18701), GLANCE (2605.03782)
- Updated: wiki/index.md (Synthesis table new game-rl-daily 2026-08-19 entry)
- New pages: wiki/synthesis/2026-08-19/game-rl-daily.md
- Contradictions: none

## [2026-08-19] synthesis | tech-report-digest (2026-08-19)
- Summary: wiki/synthesis/2026-08-19/tech-report-digest.md — 19 家 AI 公司最新技术报告与旗舰模型汇总。
- Key updates vs 08-18: DeepSeek API 定价调整（峰值/非峰值双轨，08-16 生效）；OpenAI GPT-5.6 ChatGPT 更新（thinking slider + Luna 免费用户默认）+ Model Spec 08-18 更新；xAI Grok 4.6 GitHub Copilot 全线集成（08-14）；Claude Opus 4.1 已退役；GLM-5.3 权重预计 08-28 前开源
- Updated: wiki/index.md (Synthesis table new tech-report-digest 2026-08-19 entry)
- New pages: wiki/synthesis/2026-08-19/tech-report-digest.md
- Contradictions: none

## [2026-08-19] synthesis | investment-daily (2026-08-19)
- Summary: wiki/synthesis/2026-08-19/investment-daily.md — 每日投资热点跟踪（美股/港股/A股/中概/AI/EV），覆盖 Magnificent 7、AI 模型与算力、港股科技、A 股 AI/芯片/光模块、新能源汽车、宏观地缘风险。
- Key coverage: 苹果 iPhone 17e 发布；英伟达 Q2 FY2027 财报 8/26；Anthropic Q2 营收超 11.5 亿美元（14 倍 YoY）实现调整后经营利润；Physical AI H1 2026 达 474 亿美元（+80% YoY）；阿里首发全栈 Agentic 电商系统；快手可灵 AI 2.1 定档 8/19 发布；小鹏全新 Robotaxi 8/19 发布；比亚迪巴西工厂投产、7 月欧洲销量首超特斯拉
- Updated: wiki/index.md (Synthesis table new investment-daily 2026-08-19 entry)
- New pages: wiki/synthesis/2026-08-19/investment-daily.md
- Contradictions: none

## [2026-08-19] synthesis | conference-digest (2026-08-19)
- Summary: wiki/synthesis/2026-08-19/conference-digest.md — Comprehensive survey of 53 papers from 12 top ML/AI conferences.
- Coverage: Recommendation (R²ec, IGD, RecBench, Counter-IF, RecZero, ORBIT, AgentRecBench, TagCF, LPDO, ThinkRec, GenCI, SparseCTR, TransX, GRAB, RoleMix, IDProxy, MARC, D-MoE, GenRec, LO-FAR), Code (StepCodeReasoner, R1-Code-Interpreter, ExecVerify, Agentic Verifier), Agents (VeRO, Meta-Harness, Automata from Traces, RepoNavigator), LLM Training (UniAR, Markovian Transformers, SPPO, LSE-MTP, LoongRL, GEPA), Generative (TiM, HierDiff, ControlAudio), Benchmarks (ORBIT, AgentRecBench, RecBench).
- Themes: Reasoning+Recommendation convergence, RL post-training, generative rec at scale, CTR scaling, agent safety.
- Updated: wiki/index.md (Synthesis table new entry)
- New pages: wiki/synthesis/2026-08-19/conference-digest.md
- Contradictions: none

## [2026-08-19] synthesis | arxiv-paper-check (2026-08-19)
- New page: wiki/synthesis/2026-08-19/arxiv-paper-check.md
- Coverage: 8 curated papers from the **Wed Aug 19, 2026 announced batch** (submitted Aug 18–19; cs.AI, cs.LG, cs.CL, cs.IR, stat.ML). Complement to same-day arxiv-daily. All IDs grep-verified absent (0 hits) from the entire wiki before inclusion.
- Sections: ①CTR/Rec/Ads/IR (4) — GRAB Baidu generative CTR +3.49% CTR/+3.05% revenue with CamA temporal dynamics [2602.01865v2]; LoopCTR loop scaling paradigm with sandwich architecture, zero-loop inference outperforms all baselines, oracle reveals 0.02-0.04 AUC headroom [2604.19550]; PRECTR-V2 unified relevance-CTR framework with LLM-distilled 2M-param encoder, +1.39% orders/+3.18% GMV on Xianyu [2602.20676]; DeRes dual-path residual connector, 8-layer matches 16-layer OneTrans, +0.32% AUC at <5% extra FLOPs [2606.07980]; ②AI/Agents (3) — ATLAS scaffold-free full-algorithm synthesis via quality-diversity search, outperforms SOTA on 4 NP-hard problems [2608.15546]; Evo-Harness context-to-harness skill compilation for self-evolving agents across 5 benchmarks [2608.15071]; Graph-Based RL drift diagnosis/recovery framework with small LM specialized per recovery-graph node [2608.14109]; ③ML/Efficiency (2) — SchurQuant 2-bit quantization +11.88pp accuracy on Qwen3-4B [2608.15567]; LoRA vs Embedding Regression for headline CTR — discriminative model wins 42.79% vs 35.70% [2608.11912]
- Cross-cutting: CTR scaling paradigms diversify (loop/reuse vs stacking vs generative); unified relevance-CTR frameworks mature (PRECTR-V2); agent self-improvement via skill compilation vs full-algorithm synthesis; extreme quantization approaching practical thresholds; task-specific discriminative models can outperform fine-tuned LLMs
- Updated: wiki/index.md (Synthesis table new arxiv-paper-check 2026-08-19 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-19/arxiv-paper-check.md
- Contradictions: none

## [2026-08-19] synthesis | arxiv-daily (2026-08-19)
- Summary: wiki/synthesis/2026-08-19/arxiv-daily.md — arXiv daily digest covering 37 papers from cs.AI, cs.CL, cs.IR, cs.LG, stat.ML (Aug 18–19, 2026). 7 categories: Recommendation Systems (13 papers — UniDot unified FM+sequential, OGR end-to-end slate gen with Kuaishou A/B, FLEXRec compact LLM exits, DTE temporal decoupling, TRACER SPC trilemma, GOD graft distillation, SDF Google Discover staleness 54.9% reduction, LLM-MGCL POI, SAGA multi-surface, SAHC-NS negative sampling, Ask-to-Be-Sure entropy-based CRS, Unbiased RecSys, Impression Share Prediction), LLM Agents & RL (7 — PlanPO +27.2% over GRPO, LEGO-RL SWE-bench 70.4%, Agent Lightning +14.6pp, Agentic ESOpt evolution strategies, FACA next-turn credit, GUPO gradient uncertainty, RLVR graph difficulty), LLM Reasoning (6 — Fragility of self-improving agents, LLM preference inconsistency, Chain-of-Experience +5.6%, J64/R64 MoE reasoning readout, When AI designs AI 96.8% human space, Policy-invariant reward shaping), LLM Memory (3 — ArborMem memory forests, WER skill optimizer, InnerExpert MoE hallucination), LLM Inference (3 — TileMix mixed-precision, MoNe O(1) query, SRT spaced repetition pretraining), Games (3 — CAD procedural content gen IEEE Games 2026, Concentration game, Contextual matrix games), RAG (2 — LineageRAG +5.96 EM, Ask-to-Be-Sure). Notable trends: generative recommendation matures (OGR/DTE), LLM as rec backbone (FLEXRec/TRACER), agentic RL mainstream (LEGO-RL/PlanPO/ESOpt), production validation (Google Discover/Kuaishou/KDD Cup), temporal awareness critical (DTE/SDF/TRACER), MoE internal signals fertile direction (InnerExpert/J64).
- Updated: wiki/index.md (Synthesis table new entry)
- New pages: wiki/synthesis/2026-08-19/arxiv-daily.md
- Contradictions: none

## [2026-08-18] synthesis | wq101-alpha-daily (2026-08-18)
- Summary: WorldQuant 101 Alpha 因子选股 Top 20 — 美股日报。能源板块 5 只入选（XOM 9.3/CVX 8.7/COP 8.5/SLB 7.9/DVN 7.7），医疗板块 6 只入选（LLY 9.1/HUM 8.9/CORT 8.6/DXCM 8.4/UNH 8.2/GILD 8.0），科技板块 5 只入选（DELL 9.0/PANW 8.8/NVDA 8.3/NTAP 7.6/ANET 7.5），公用事业 1 只（CEG 7.4），消费 1 只（BBY 8.1）。核心变化：能源从地缘溢价升级为 AI 电力+地缘双重驱动；金融板块全面移出（日跌-1.00% 触发 Alpha#12 背离）；VIX +6.60% 飙升 + WTI $85.09 + 黄金 $4,452.90。
- Updated: wiki/index.md (Synthesis table new entry)
- New pages: wiki/synthesis/2026-08-18/wq101-alpha-daily.md
- Contradictions: none

## [2026-08-18] synthesis | investment-daily (2026-08-18)
- Summary: wiki/synthesis/2026-08-18/investment-daily.md — 投资日报覆盖美股（Mag 7、AI 芯片、存储、光通信）、港股（腾讯/阿里/百度/MiniMax）、A 股（寒武纪/海光信息/AI 芯片板块）、中概股（小鹏/蔚来/拼多多）、新能源（比亚迪/宁德时代/特斯拉）。重点：Nvidia $1050 亿 OpenAI 数据中心担保；存储芯片逆势大涨（美光 +5.9%）；寒武纪/海光信息业绩创新高；特斯拉 Cybercab 计划 8 月底公开部署；ECB 预警 AI 市场修正风险。
- Updated: wiki/index.md (Synthesis table new entry)
- New pages: wiki/synthesis/2026-08-18/investment-daily.md
- Contradictions: none

## [2026-08-18] synthesis | tech-report-digest (2026-08-18)
- Summary: LLM Tech Report Digest — 2026-08-18, 19 家 AI 公司最新技术报告全面更新。重点变化：DeepSeek V4-Pro GA（08-13，Agent 能力大幅提升）；OpenAI GPT-5.6 System Card + Astra 数学定理证明；Apple AFM 3 首个端侧 20B Sparse 模型；NVIDIA Nemotron 3 Ultra（550B Hybrid Mamba-Attention）；xAI Grok 4.6 GA（1.5T，Cursor 联合）；Zhipu GLM-5.3（post-training scaling 驱动网络安全涌现）；InternLM 三篇论文（S2-Preview 397B + Mobius 架构 + S1-Pro 1T）；Kimi K3（2.8T KDA 线性注意力 + WebDev Arena #1）；Qwen3.8-Max 权重开放（08-17）；Step 3.7 Flash Advisor Mode（97% Opus 4.6 @ 1/9 成本）；Mistral Shieldstral 3B 安全分类器
- Updated: wiki/index.md (Synthesis table new tech-report-digest 2026-08-18 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-18/tech-report-digest.md
- Contradictions: none

## [2026-08-18] synthesis | Conference & arXiv Daily Digest (2026-06-05)
- Summary: Conference & arXiv Daily Digest — 2026-06-05 covering ICLR 2026, ICML 2026, NeurIPS 2025, CVPR 2026, AAAI 2026, ACL 2026, EMNLP 2025, KDD 2026, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, plus arXiv preprints. 56 paper entries organized across 14 sections including ICLR 2026 Outstanding Papers (Transformers Inherently Succinct, LLMs Lost in Multi-Turn), ICML 2026 Outstanding (Flexibility Trap, High-Accuracy Diffusion Sampling), NeurIPS 2025 Best (Artificial Hivemind, Gated Attention, 1000-Layer RL, Why Diffusion Don't Memorize), CVPR 2026 Best (D4RT 4D Reconstruction), ACL 2026 Best (Imperfective Paradox), AAAI 2026 Outstanding (LLM2CLIP, ReconVLA), and industry papers from Netflix (GenRec), Meta (ConnectionMind), Alibaba (MetaStrategy), NVIDIA (NitroGen), BMW (CAR-bench), plus CTR/Recommendation, LLM/Agent, Google DeepMind/OpenAI/Meta AI research sections.
- Updated: wiki/index.md (Synthesis table new conference-digest 2026-06-05 entry)
- New pages: wiki/synthesis/2026-06-05/conference-digest.md
- Contradictions: none

## [2026-08-18] synthesis | arXiv Paper Check — AI & CTR (2026-08-18)
- New page: wiki/synthesis/2026-08-18/arxiv-paper-check.md
- Coverage: 15 curated papers from the **Mon Aug 17, 2026 announced batch** (submissions Sun Aug 16; IDs ~2608.138xx–2608.145xx; cs.AI 185 new / cs.LG 138 new / cs.IR 13 new = 336 entries). Complement to same-day arxiv-daily (which covers a different batch). All 15 IDs grep-verified absent (0 hits) from the entire wiki; zero overlap with existing digests.
- Sections: ①CTR/Rec/Ads/IR (6) — PriCoRec privacy-aware cloud-device ad recommendation (RecSys'26) [2608.14429]; MACS multi-agent conversational e-commerce recommendation (Stanford) [2608.14068]; EchoRec cycle-consistent preference alignment for generative recommendation [2608.14011]; AdsWorldEngine self-evolving conversational advertising agent [2608.13833]; Residual Dominance structural account of last-item reliance in causal self-attention recommenders (RecSys'26) [2608.14021]; Content Depth short-video recommendation rethinking attention economy [2608.13990]; ②AI/Agents (5) — AgentRewind recoverable execution for long-horizon LLM agents [2608.14380]; Clearing the Fog proactive exploration in LLM agents [2608.14339]; Demystifying Agent Skills failure diagnosis [2608.14036]; BiasTrace reasoning-to-bias tracing in LLMs [2608.14161]; Intern-S2-Mobius decoupled knowledge and reasoning foundation model [2608.14290]; ③ML/Efficiency (4) — FreeBalance pre-routing MoE load balancing [2608.14205]; Traj-LeWM latent trajectory cost for world-model planning [2608.14125]; RL for Diffusion Models unified path-space view [2608.14430]; Forecast Collapse in time-series foundation models [2608.14106]
- Cross-cutting: privacy-preserving CTR maturing (PriCoRec); generative rec alignment diversifies (EchoRec cycle-consistency); agent reliability as first-class concern (AgentRewind + Clearing the Fog + Demystifying Agent Skills); MoE efficiency for CTR (FreeBalance + DeaMoE); residual dominance as Transformer-rec diagnosis (RecSys'26)
- Updated: wiki/index.md (Synthesis table new arxiv-paper-check 2026-08-18 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-18/arxiv-paper-check.md
- Contradictions: none (all 15 IDs grep-verified absent; zero overlap with sibling digests)

## [2026-08-18] synthesis | arxiv-daily (2026-08-18)
- New page: wiki/synthesis/2026-08-18/arxiv-daily.md
- Coverage: 41 curated papers across AI, LLM, recommendation, CTR/advertising, sequential modeling, and games/RL. Categories: LLM (7) — LLaDA MoE v2 diffusion MoE scaling, LongCat Sparse Attention (Meituan 1.6T model), HiLP hierarchical latent prediction, behavioral evolution measurement, ARCHead LM-head compression, reasoning interface evaluation, reference-free multilingual MT (Xiaomi). Sequential Recommendation (6) — PSD privileged self-distillation, RecRec recursive reasoning, GALLM graph-aware LLM rec, SRPFN prior-data fitted networks (KDD 2026), CAST semantic-level complementary transitions, MLTFR multi-LLM token routing. CTR/Advertising (15) — GRAB (Baidu, +3.49% CTR), CADET (LinkedIn, +11.04% CTR), EST (Taobao, power-law scaling), GenCI cohort-based intent, IDProxy cold-start (Xiaohongshu), LLM-HYPER hypernetwork cold-start, DS-MLP dual-stream, Long-History User Transformers (Yandex), OneRanker (Tencent, GMV+1.34%), GR4AD (Kuaishou, +4.2% revenue), LLaTTE (Meta, 4.3% conversion), SORT (+6.35% orders), UniVA (Tencent, HitRate+37%), MetaStrategy (Taobao, transaction+2.83%), DEGR (JD). Games/RL (6) — Superhuman Generals.io self-play, Odysseus VLM 100+ turn games, MEMOPILOT memory RL, CAST game solvers as teachers, EA SPORTS FC RL goalkeeping, MEMO memory-augmented LLM games. LLM+RecSys (5) — RecGOAT optimal transport alignment, SAILRec attention steering, TCA4Rec token-level CF alignment, DeepInterestGR multi-LLM interest mining, user/item embeddings for LLM rec.
- Updated: wiki/index.md (Synthesis table new arxiv-daily 2026-08-18 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-18/arxiv-daily.md
- Contradictions: none

## [2026-08-18] synthesis | game-rl-daily (2026-08-18)
- New page: wiki/synthesis/2026-08-18/game-rl-daily.md
- Coverage: 25+ papers across 7 categories — Game RL (Generals.io superhuman self-play 2606.23348, EMAgnet 2606.23995, GARIP 2606.22688, AlphaZero Tablut 2604.05476, Big 2 self-play 2605.28863, DAGS 2605.14379, Stratagem 2604.17696), Game AI Bot (CAST 2607.25308, Hierarchical LLM+RL 2606.20014, Spatial Reasoning 2607.22732, RAPOA 2606.17838, Bounded Autonomy 2604.04703, Continual Harness 2605.09998), Game Foundation Models (NitroGen CVPR 2026 2601.02427, Game-TARS 2510.23691, Survey 2605.09965), PCG (VIPCGRL 2508.09860, PCGRLLM 2502.10906, Multiverse 2603.26782, Multi-Agent PCGRL 2510.04862, WCRL 2605.13570), Benchmarks (GVGAI-LLM 2508.08501, OmniGameArena 2606.09826, LMGame-Bench ICLR'26 2505.15146, CUBE 2603.15798), World Models (Mind-Studio 2606.16070, GameCWM distillation 2605.24375, ITC 2605.16457, OPINE-World 2607.01531, RWML 2602.05842), Hierarchical RL (AgentOWL 2602.02799, CODE-SHARP 2602.10085). 5 cross-cutting themes identified.
- Updated: wiki/index.md (Synthesis table new game-rl-daily 2026-08-18 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-18/game-rl-daily.md
- Contradictions: none

## [2026-08-17] synthesis | wq101-alpha-daily (2026-08-17)
- New page: wiki/synthesis/2026-08-17/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子选股 Top 20 — 美股日报。数据基准 = 8/15（周五）完整收盘确认值 + 8/17（周日）事件窗口。板块轮动深化：从"科技+AI"集中 → "金融+医疗+工业"分散化。Top 20: JPM(9.2) / MRK(9.0) / MSFT(8.9) / DELL(8.7) / ETN(8.6) / BAC(8.4) / SCHW(8.3) / PANW(8.2) / MU(8.2) / AAPL(8.1) / SBUX(8.0) / BNY(7.9) / FIX(7.8) / VRT(7.8) / STX(7.7) / TRV(7.6) / GOOGL(7.5) / GS(7.5) / XOM(7.4) / AMZN(7.3)。核心变化：金融板块 6 只入选（JPM/BAC/SCHW/BNY/TRV/GS），Alpha#6 量价因子在银行股信号最强；医疗 MRK 3M 动量 +16% 领跑全市场；科技内部分化（MSFT/DELL 强 vs AVGO/AMAT 弱）；能源受地缘溢价支撑。因子权重：Alpha#1 30% + #41 25% + #6 15% + #12 10% + #53 10% + #19 5% + #30 5%。
- Updated: wiki/index.md (Synthesis table new wq101-alpha-daily 2026-08-17 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-17/wq101-alpha-daily.md
- Contradictions: none

## [2026-08-17] synthesis | game-rl-daily (2026-08-17)
- New page: wiki/synthesis/2026-08-17/game-rl-daily.md
- Coverage: 17 papers across 5 categories — Game RL (MARLIO EA/CoG 2026 MOBA DRL benchmark, self-play parking, Dream Rehearsal continual MBRL), Game AI Bot (Nemobot Games ByteDance 100K+ GPU envs, Game-TARS cross-game transformer, GameVerse VLM video reflection), Game Foundation Models (GameWorld autoregressive WM Wuhan/Huawei, MAGIC LLM PCG, World Models survey UW-Madison), Benchmarks (GameCraft-Bench Unity LLM game creation Fudan/PKU/ByteDance, OmniGameArena UE5 LLM eval PKU/BAAI, Orak game agent framework ZJU/Huawei, GameDevBench, Agent Benchmarks Protocol Validity), PCG (Multi-Objective Instruction-Aware PCGRL). Cross-cutting: LLM-as-game-agent performance gap with humans persists; world models as game testbed; GPU-accelerated simulation at 100K+ concurrent environments.
- Updated: wiki/index.md (Synthesis table new game-rl-daily 2026-08-17 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-17/game-rl-daily.md
- Contradictions: none

## [2026-08-17] synthesis | investment-daily (2026-08-17)
- New page: wiki/synthesis/2026-08-17/investment-daily.md
- Coverage: 全球科技与 AI 板块投资日报。覆盖美股 Mag 7 + AI 芯片/基础设施（NVDA/AMD/AVGO/PLTR/CRWV/NBIS/SNDK）、港股科技（腾讯/阿里/京东/联想/百度）、A 股算力/芯片（寒武纪/海光信息/中际旭创）、中概股（BABA/PDD/JD/NIO/XPEV）、新能源汽车（比亚迪/特斯拉/宁德时代）。核心驱动：①S&P 500 Q2 盈利 +31%（30 年最强）；②AI 基础设施链（CoreWeave $1040亿积压/Nebius +454% YoY）验证"新云"模式；③存储芯片超级周期（SNDK 周+35%/SKH +20%）；④中国新能源车渗透率突破 60%；⑤AI 模型密集发布（Gemini 3.7 Flash/Nemotron 3.5 Lightning/GLM-5.3）。
- Updated: wiki/index.md (Synthesis table new investment-daily 2026-08-17 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-17/investment-daily.md
- Contradictions: none

## [2026-08-17] synthesis | tech-report-digest (2026-08-17)
- New page: wiki/synthesis/2026-08-17/tech-report-digest.md
- Coverage: 19 家主流 AI 公司/实验室最新技术报告与旗舰模型汇总。每家一节：最新模型 + 发布日期 + 核心参数 + 架构创新 + 论文链接 + 最新动态。涵盖：DeepSeek (R1 + V4 Pro GA), OpenAI (GPT-5 + Astra), Meta (Llama 4 Scout/Maverick), Google (Gemini 2.5 Pro/Flash), Anthropic (Claude Opus 4/Sonnet 4), Mistral (Large 3), Qwen (Qwen3 + Qwen3.8-Max), Yi/Lightning, Baichuan (M2), Microsoft (Phi-4), Apple (AFM 2025), NVIDIA (Nemotron 3 Ultra + 3.5 Lightning), xAI (Grok 3 + 4.6), Amazon (Nova), Zhipu (GLM-5/5.2), InternLM (S1-Pro), Moonshot (Kimi K3), StepFun (Step-DeepResearch + Step 3), ByteDance (Seed 2.0/2.1)。交叉观察：MoE 统治、Hybrid Attention、原生多模态、Thinking 范式、端侧部署、开放 vs 闭源格局、"承诺→兑现"信用追踪、规模军备竞赛。
- Updated: wiki/index.md (Synthesis table new tech-report-digest 2026-08-17 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-17/tech-report-digest.md
- Contradictions: none

## [2026-08-17] synthesis | conference-digest (2026-08-17)
- New page: wiki/synthesis/2026-08-17/conference-digest.md
- Coverage: Structured digest covering 12 top ML/AI conferences (2025–2026): ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025. Updated 2026-08-17 with latest award details from web searches. Key papers: Flexibility Trap/JustGRPO (ICML Outstanding), High-Accuracy Diffusion Sampling (ICML Outstanding), Transformers Inherently Succinct (ICLR Outstanding), LLMs Lost in Multi-Turn (ICLR Outstanding), Artificial Hivemind (NeurIPS Best), Gated Attention Qwen (NeurIPS Best), 1000-Layer RL (NeurIPS Best), Why Diffusion Don't Memorize (NeurIPS Best), D4RT 4D reconstruction Google DeepMind (CVPR Best), Imperfective Paradox NII (ACL Best), Conformal Risk Control EC JRC (RecSys Best), MedRGAG WWW Best, XGBoost Test of Time KDD, GANs Test of Time ICLR. Industry: Netflix GenRec, Meta ConnectionMind, Alibaba MetaStrategy, BMW CAR-bench, NVIDIA NitroGen. Cross-conference thematic analysis included (diffusion, RL post-training, LLM-as-ranker, agent safety).
- Updated: wiki/index.md (Synthesis table new conference-digest 2026-08-17 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-17/conference-digest.md
- Contradictions: none (all papers verified against web sources; cross-references to 08-16 conference-digest, 08-17 arxiv-paper-check included)

## [2026-08-16] synthesis | wq101-alpha-daily (2026-08-16)
- New page: wiki/synthesis/2026-08-16/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子选股 Top 20 — 美股周末复盘版。数据基准 = **8/14（周五）完整收盘全确认值 + 8/16（周日）事件窗口**（8/15-16 无美股交易，无"事件窗口折价"）。①**零售销售 -0.6% 大幅 miss**（7 月环比 -0.6% vs 预期 +0.1%，2025/5 来最大降幅；核心 -0.3%、线上 -2.2%、汽车 -1.8%）+ 密歇根 8 月初值 51（预期 55）→ FedWatch 9 月加息概率降至 ~28.6%——"低于 0% 消费下调"预设兑现；②**指数自 8/13 纪录回落但周线三连涨**（S&P 7,785.76 -0.17% / Nasdaq 26,729.16 -0.28% / Dow 53,732.41 -0.20%）；③**油价反弹**（WTI $82.40 +1.42% / Brent $88.52 +1.67%，伊朗/霍尔木兹升级 + IEA 赤字预测）——"WTI 续破 $80 下调"条件未触发，CVX +0.4 / XOM +0.4 评分上调；④**Berkshire 13F**：Q2 增持 Alphabet 83% → 106M 股 ~$37.9B 第三大持仓，14 季度首次净买入 → GOOGL 评分 ↑ 至 8.0（Alpha#19 价值锚确认）；⑤**AI 硬件内部二次分化**：SNDK +7.39% $1,641.11（JPMorgan 上调至增持目标 $2,250）/ MU +2.30% / NBIS +8.88% vs ANET -2.36% / PLTR -2.78% / SHOP -2.66%；⑥**JD 均值回复论证伪（重要纠偏）**——8/13 财报日 ADR -8.3% + 8/14 续跌 -0.80%，弱零售增长盖过 EPS beat，Mizuho 目标价 $41→$39，JD 从 Top 20 剔除并纳入"低质修复被市场否决"减分条件（Alpha#19 运用规则更新）；⑦**DIS +1.96% 零售弱日逆势 = 防御属性确认**。
- Top 20: LLY(9.3) / NVDA(9.3) / MSFT(8.8) / ABNB(8.8) / SHOP(8.6 ↓) / CVX(8.5 ↑) / MU(8.4) / TSM(8.3) / XOM(8.3 ↑) / AAPL(8.5) / JPM(8.2) / DIS(8.2 ↑) / SMCI(8.2) / SNDK(8.0) / GOOGL(8.0 ↑) / ANET(7.9 ↓) / NBIS(7.9 ↑) / AMZN(7.8) / PLTR(7.8 ↓↓) / **WMT(7.5 新入选，防御轮动 + 8/20 财报窗口)**；移出 JD(6.9)
- Factor weighting: Alpha#1 30% + #41 25% + #6 15%（纪律化深化：仅"远期/长约型兑现"配溢价）+ #12 10% + #53 10% + #19 5%（GOOGL/Berkshire + WMT）+ #30 5%（SNDK 周 +35% 追高警告）
- Updated: wiki/index.md（Synthesis 表新增 wq101-alpha-daily 2026-08-16 条目，插在 08-14 wq101 条目之前、game-rl-daily 08-12 之后，保持 wq101 组逆序排列）, wiki/log.md
- New pages: wiki/synthesis/2026-08-16/wq101-alpha-daily.md
- Contradictions: JD "经营利润转正 + EPS beat 应获纠偏溢价"（8/14 报告假设）vs 市场 8/13 ADR -8.3% + 8/14 续跌——均值回复论证伪，已在报告中以 ⚠️ 标注并更新 Alpha#19 运用规则；8/13 油价 -2.4% 下调 CVX/XOM 被 8/14 +1.42% 反弹反转（地缘定价回归）

## [2026-08-16] synthesis | arXiv Paper Check — AI & CTR (2026-08-16)
- New page: wiki/synthesis/2026-08-16/arxiv-paper-check.md
- Coverage: 16 curated papers from the **Fri Aug 14, 2026 announced window** (submissions Aug 12–13; IDs ~2608.12308–2608.13560; cs.AI 204 new / cs.IR 19 new). Sat–Sun Aug 15–16, 2026 has **no arXiv announcement** (weekend), so the latest batch remains Fri Aug 14. Complement to the same-day arxiv-ai-search (20 papers) and arxiv-daily (26 papers), which together claim ~46 papers of this window. Every arXiv ID grep-verified absent (0 hits) from the entire wiki before inclusion.
- Sections: ①CTR/Rec/Ads/IR (5) — HybridRAG-BN hybrid retrieval (BM25+BGE-M3) + LoRA-fine-tuned verifier + DuckDuckGo fallback for Bangla KBQA, F1 0.71654/0.72912 public/private, first place [2608.13004]; KSR Knowledge Synthesis Review Framework task-level benchmarking of LLM evidence-synthesis systems (GPT-5/Claude Sonnet 4/Gemini 2.5 Pro/NotebookLM on 244-doc benchmark, 92.2% gold agreement κ=0.80; no system leads all tasks; Claude best screening 82.8%, GPT-5 best recall 91.8%) [2608.12741]; CRAFT generator+constraint-verifier iterative refinement for temporal reasoning over anchor-sparse clinical narratives, MedTempo 5,347-report vaccine-AE benchmark [2608.12779]; ParliamentRAG authority-aware multi-view RAG over Italian parliamentary proceedings — topic-dependent authority model beats NotebookLM (coverage 0.97 vs 0.95, quote faithfulness 1.00 vs 0.95) [2608.13410]; TRACE joint course-set+grade Transformer prediction, ~50% MAE reduction, beats LSTM/GNN (education analytics) [2608.13409]; ②AI/Agents/Evaluation (11) — MARC v1 open-source deterministic multi-agent clinical reasoning framework with auto-prompt Decomposer (Penn) [2608.13476]; Are-You-Sure instruction-tuning changes verbalized confidence while degrading likelihood-based calibration, cross-rationale diversity consistently down [2608.13430]; It's-How-You-Ask linguistic register (hedges/tag questions/collective reference) elicits shorter less formal responses, larger effects than explicit gender names, early-layer encoding blocks post-hoc mitigation [2608.13328]; Toward-a-Gricean-Retreat LLM activations encode knowledge-boundary + referent-specificity signals but generation doesn't act on them — hallucination as failure to retreat [2608.13484]; LittleLearner developmentally-restricted pretraining sandbox (5B on 88B-token ≤Grade-5 curriculum) — post-training/ICL don't raise out-of-scope capabilities [2608.13545]; RAIL unified 9-level AI Readiness Level + panel-of-LLM-experts classifier [2608.13428]; Concept-Drift malware — OCSVM drift-aware retraining beats static/periodic across MLP/RF/SVM/XGBoost [2608.13465]; ARMDIL MLLM-router heterogeneous vision ensembles, prompt-level adaptability [2608.13463]; TopoIntent compiles security intent into executable CIS-v8.1.2-compliance-checked Mininet topologies + new benchmark [2608.13389]; CAPRI contract-aware proof repair for Isabelle — proof-body-only 29/36 valid repairs with zero contract violations, 180 runs/138 valid repairs [2608.13459]; CEAA edge-SLM virtual agents, Think/Memory on Jetson Orin NX with Qwen2.5 [2608.13420]
- Version notes: all 16 submitted 08-12/13, listed in Fri Aug 14 window; first appearances. Zero cross-wiki duplicates (sibling 08-16 arxiv-ai-search 20 + arxiv-daily 26 IDs not re-listed)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-paper-check 2026-08-16 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-16/arxiv-paper-check.md
- Contradictions: none (all 16 IDs grep-verified absent; sibling-digest dedup cross-checked against arxiv-ai-search and arxiv-daily)

## [2026-08-14] synthesis | arXiv Paper Check — AI & CTR (2026-08-14)
- New page: wiki/synthesis/2026-08-14/arxiv-paper-check.md
- Coverage: 19 curated papers from the **Fri Aug 14, 2026 announced window** (submissions Aug 12–13; IDs ~2608.12389–2608.13558; cs.AI 204 new / cs.IR 19 new). Complement to the same-day arxiv-ai-search (20 papers) and arxiv-daily (29 papers), which together claim ~49 papers of this window. Every arXiv ID grep-verified absent (0 hits) from the entire wiki before inclusion.
- Sections: ①CTR/Rec/Ads/IR (7) — MM-slotgate attribute-conditioned Fashion-CLIP slot factorization (category/color/pattern/demographic, per-slot text-image gates, H&M) [2608.12570]; GEM generative embedding model reasons-then-embeds, beats non-reasoning variant/matches larger baselines (Glasgow, cross cs.CL) [2608.13200]; TTT-Embed test-time query-embedding optimization from scalar ranking rewards only (scope param, no weight/index access) [2608.12569]; When-Should-Multi-Round-RAG-Stop? S2G-RAG-style structured stopping judge on frozen Search-R1, STOP as sequential selection not state classification, −77 retrieval calls (−3.70%) at −0.625 pp Official EM (HotpotQA) [2608.13237]; RAGSieve self-referenced local-contrast knowledge-poison detection — RSQ query-local + RSG corpus-local contrast, 95.2% AUROC, 82.2% poison at 5% clean-doc removal, 3 QA × 6 poisons (cross cs.CL) [2608.13010]; EviReform evidence-guided query reformulation for multi-hop graph retrieval, residual queries + separate normalization + entity-propagation, up to +5.59 R@5 / +4.50 F1 (2WikiMultiHopQA/HotpotQA/MuSiQue) [2608.13006]; MASCOT model-aware submodular coverage for composite-attribute T2I retrieval — resource allocation framing fixes MS-DPP early-rank recall degradation on diversity-decrease tasks [2608.12532]; ②AI/Agents/Evaluation (12) — PAC-Bayes-regularized Meta-LoRA for cross-domain LLM personalization, meta-learned LoRA init as prior center, update scaled by support-set size + predictive uncertainty [2608.12389]; AQuA recursively self-improving quant-trading research agents — separate symbolic-factor vs model-development loops in sealed sandboxes, actions constrained to factor expressions/config diffs (finance-alpha thread) [2608.12841]; OmniScientist omni-modal omni-discipline AI scientist — perception layer + ideation/experiment/writeup agents, idea/rigour/claim checks executed in code [2608.13558]; Beyond-Final-Scores systematic eval of 7 frontier models × 36 long-horizon AI-R&D tasks, rule-based within-run metrics (Solution Framing/Execution/Feedback Control) — agents are engineering optimizers not autonomous researchers [2608.13417]; QuoteBench how matched scores hide command-path failures — one unescaped parser drops success 55.4–73.2 pp, disclosure recovers 30.4–60.7 pp, 56 one-shot tasks/14 incident families [2608.13547]; Rules-or-Character AIES 2026 safety-design allocation α between character shaping vs rule enforcement, closed-form expected harm + CVaR, optimal α* interior/rules-only shifting toward character with scale (Δα* +0.01…+0.21), dominant param = baseline character fragility rate (Δα* 0.50) [2608.13345]; StateBridge COLM 2026 training-free latent communication — closed-form orthogonal alignment of sender hidden states to receiver input space + norm calibration/vocab anchoring, 22/26 model-task pairs best/tied [2608.13317]; SkillShapley boundary-adaptive Shapley valuation for skill-step attribution in LLM agents (performance cliffs + additive step interactions, SkillsBench) [2608.13173]; VALG agentic ML-theory research — verification + adaptive formulation + graph-structured proofs, 9 subproblems/5 COLT 2026 open problems, 2 internally-finalized theorem candidates, open source [2608.13060]; DiG-bench discovery-in-games benchmark — 70 games/7 tiers with unknown transformation rules + unknown win conditions, 21 public/49 private, all solved by ≥1 human (Schmidhuber/Tenenbaum/Griffiths/Tri Dao/Kurth-Nelson et al.) [2608.12593]; Research-Assistant AstraZeneca agentic R&D system technical note — chat over literature/KG/chemistry/clinical trials/safety/expression/internal systems, fast + multi-step modes, deployed at scale [2608.12395]; ARAC-Bench auto-research alignment-and-completeness eval — Academic Cognition Skills rubrics + Proposal/Experiment/Synthesis diagnostic, best 67.9/100, ρ=0.8141 vs PhD-candidate rankings [2608.12788]
- Version notes: GEM/RAGSieve/EviReform cross-listed cs.CL→cs.IR/cs.AI; AstraZeneca RA submitted 08-06; PAC-Bayes Meta-LoRA submitted 08-01; Rules-or-Character accepted AIES 2026; StateBridge accepted COLM 2026. Zero cross-wiki duplicates (sibling 08-14 digests' ~49 IDs not re-listed)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-paper-check 2026-08-14 条目，插在 arxiv-daily 2026-08-14 之后), wiki/log.md
- New pages: wiki/synthesis/2026-08-14/arxiv-paper-check.md
- Contradictions: none (all 19 IDs grep-verified absent; sibling-digest dedup cross-checked against both arxiv-ai-search and arxiv-daily)

## [2026-08-14] synthesis | arXiv AI Research Search (2026-08-14)
- New page: wiki/synthesis/2026-08-14/arxiv-ai-search.md
- Coverage: 20 curated papers from the **Fri Aug 14, 2026** arXiv announcement batch (submissions Aug 12–13, IDs ~2608.12547–2608.13522; window continues past the 08-13 digests which covered up to 2608.12307). Harvested from cs.LG 157 / cs.CL 101 / cs.AI 204 / cs.IR 19 / cs.GT 6 / cs.MA 14 / cs.SE 18 new. First 2026-08-14 synthesis output (same-day arxiv-daily / arxiv-paper-check did not yet exist), so the strongest industrial cs.IR/cs.AI/cs.GT picks are included here. All 20 IDs grep-verified 0 hits across wiki/index.md, wiki/log.md, wiki/synthesis/**. Domains: **Ads/CTR/CVR** — STAR structured tokenization + target-aware interest for PCVR, KDD Cup 2026 Tencent UniRec Challenge, temporal context dominant AUC driver [2608.12986]; doubly robust causal CVR estimator via semiparametric theory + targeted regularization, "ideal loss" unbiased-loss ≠ unbiased-estimator [2608.13461]; **Recommendation** — FSGR token frequency bias fairness in SID-based generative rec (OT assignment + re-anchor + hierarchical frequency calibration, >20% Gini gain) [2608.12845]; DrEM dual-side (supervision+feature) robust ensemble ranking from noisy pxtrs, flip-probability-corrected robust loss + perturbation consistency, online A/B [2608.12778]; DTAMLP sporadic-click denoise via threshold-capped time-interval weight fusion + FFT filtering [2608.12975]; DrIG generative universal multimodal retrieval with dual-role (sequential+set-based) residual-quantized identifiers, M-BEIR [2608.12987]; **OPD/RL** — CROP counterfactual (paraphrase-calibrated sensitivity margin) task relevance for selective OPD, +1.92/+2.96 over best non-CROP [2608.13387]; LOPD learnable latent privileged context for on-policy self-distillation, <30% GRPO/Skill-SD rollout budget [2608.13040]; CrEST "teach magnitude not direction" turn-segmented verified advantages + entropy-gated teacher modulation, BFCL V3/WildToolBench [2608.13179]; **Alignment** — SPP synthetic persona pretraining from token zero (3B/500B tokens), early intervention compounds with budget [2608.13482]; **Efficiency** — vToken token-level KV virtualization (token-table indirection + async repacking in vLLM, 27–72% retained-block reduction, 1.37× throughput, 2× concurrency) [2608.13263]; RoPE-aligned Q/K rotations for dynamic W4A4KV4 — converse theorem + negative result (surrogate/quantizer-scale misalignment) [2608.13365]; **Architecture** — post-norm beats pre-norm under curriculum depth growing (Qwen3-8B→9-layer distillation, 0.0328 CE) [2608.13156]; **Verified code** — Vero first repo-level joint implementation+proof benchmark (43 Lean 4 multi-module instances, Python/Dafny/Verus/Coq; best agent 27/43) [2608.13522]; **Reasoning** — TsuGO Go life-and-death search-efficiency benchmark (CoT→search tree; length ≠ search quality) [2608.13221]; **GT/economics** — Keep/Customize/Exit Stackelberg default reasoning-token allocation + token pricing (closed-form user optimum, three-regime rule) [2608.13315]; EA-RAM dual-error-aware reverse auction for decentralized LLM routing (Bayesian IC/IR, welfare-loss bound) [2608.12719]; Do LLMs Beat Nash? 13 models one-shot no-communication self-play (2 frontier models beat Nash in dyadics; no transfer to 4+ teams) [2608.12547]; **Time series** — ORBIT controllable training regimes (Bootstrap Multi-Level Sampling + Omni-Range Incremental Training) for Falcon-2.0, GIFT-Eval/fev-bench [2608.13262]; **Theory** — Neural Quadratic Forms symmetry-derived universal leading form Tr[WWᵀA(x)], Lotka–Volterra dynamics unifying sudden learning + scaling-law power laws [2608.13335]
- Updated: wiki/index.md (Synthesis 表新增 arxiv-ai-search 2026-08-14 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-14/arxiv-ai-search.md
- Contradictions: none (all 20 IDs grep-verified absent; ⚠️ 2608.12547 listed "Submitted on 12 Aug 2026" but appears in Fri Aug 14 cs.MA listing — new to wiki, 0 hits; 2608.12987 carries "under review" comment)

## [2026-08-14] synthesis | arXiv Daily Digest (2026-08-14)
- New page: wiki/synthesis/2026-08-14/arxiv-daily.md
- Coverage: 29 curated papers from the **Fri Aug 14, 2026 announced window — Thu Aug 13 submission wave (IDs ~2608.124xx–2608.135xx)**, harvested from the `/list/{cat}/recent` pages for cs.AI (204) / cs.LG (157) / cs.CL (101) / cs.IR (19) / cs.GT (6) / cs.MA (14) / econ.TH (6) / stat.ML (29) = 536 entries. All 32 shortlisted arXiv IDs grep-verified absent from the entire wiki (0 hits; zero overlap with the 08-13 digests which stopped at ~2608.12307). **Same-day dedup:** the same-day [arxiv-ai-search](./synthesis/2026-08-14/arxiv-ai-search.md) already claims 20 papers of this window — the 18 overlapping IDs were removed, not duplicated (CROP 2608.13387, LOPD 2608.13040, CrEST 2608.13179, Post-Norm depth growing 2608.13156, SPP 2608.13482, Vero 2608.13522, TsuGO 2608.13221, STAR 2608.12986, Doubly-Robust-CVR 2608.13461, FSGR 2608.12845, DrEM 2608.12778, DrIG 2608.12987, ORBIT 2608.13262, vToken 2608.13263, RoPE-Q/K 2608.13365, Do-LLMs-Beat-Nash 2608.12547, EA-RAM 2608.12719, Keep-Customize-Exit 2608.13315); **model dedup:** AlayaWorld v1.1 (2608.13492) already covered ([game-rl-daily](../2026-08-02/game-rl-daily.md), [conference-digest](../2026-08-01/conference-digest.md)) — update note, not re-listed. Signature themes: **agent memory & skills dominate** — ReFind anti-structure raw-log search beats HippoRAG 2 (58.2 vs 53.2, zero LLM index construction); RippleMem associative recollection ~30× lower graph-construction cost; LycheeMemory V2 semantic segment-level consolidation, 86% construction-token cut; MindMemOS self-evolving memory schemas + skills; SkillEvo multi-turn interaction as renewable evolution gradient (+23.0 vs self-reflection); DIVE diversity-population parameter-free skill evolution; QCR target-bound trajectory reuse (+10.7 pts, −48.9% tokens); **skill safety formalization** — Practice Makes Unsafe / SkillMisevo (SafeEvolve, carryover ASR 16→35.3%, −26.7/−17.3 pp); **self-distillation teacher-trust** — I-SDPO instance-level GRPO/SDPO routing (SciKnowEval mean@16 56.67→70.31); **world-model planner-objective diagnostics** — Objective-Is-The-Bottleneck (⚠️ qualifies the 08-12 LeWorldModel reproduction's "predictor degrades" reading), ACPC JEPA perturbation bounds + IR–SR screen; **efficiency orthogonal to KV-cache work** — SNIPER knapsack-optimal pruning (CRAFT 0.98), RMM input-adaptive matrix-product reduction, DARTree AR draft trees for speculative diffusion decoding (9.73×), GCache quality-aligned diffusion caching; **forecasting/finance** — SsPCA-MIDAS, FlowLOB, LVPG, Defensive Boosting; **AI scientists** — Replica & Faraday (27B replication agent beats Claude Opus 4.8 / GPT-5.5); **MAS/mechanism** — E2-Explainer, Entropy-Augmented MO (+48% hypervolume), DePIN (deterrence ratio Γ); **open models & AI culture** — DFM Mimir v1 (permissible-data 1B, Danish SOTA), Novels formal-variation compression.
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-14 条目，插在 arxiv-ai-search 2026-08-14 之后), wiki/log.md
- New pages: wiki/synthesis/2026-08-14/arxiv-daily.md
- Contradictions: 1 cross-page — **Objective-Is-The-Bottleneck (2608.12959)** concludes the LeWorldModel/TwoRoom planning bottleneck is the **planner's objective** (CEM cost geometry — squared latent distance saturates ~80 units and inverts past 120), not predictor quality — a different conclusion from the 08-12 game-rl-daily reproduction's "predictor degrades" framing; flagged in both pages for reconciliation. Otherwise none (all 32 IDs grep-verified absent)

## [2026-08-13] synthesis | WQ101 Alpha Daily (2026-08-13)
- New page: wiki/synthesis/2026-08-13/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (数据基准 8/12 周三完整收盘确认 + 8/13 周四盘前/事件窗口)。①**CPI 落地符合预期**（7 月 +3.4% / 核心 +2.5%，FedWatch 9 月加息概率降至 42%）但 420 亿 10Y 拍卖 4.683%（2007 年来最高）——"加息暂缓 vs 长端高企"并存；②**8/12 AI 硬件全面爆发**——费半 +2.49%（SK海力士 +9.01%/Seagate +7.03%/SanDisk +5.76%/MU +4.92%）、光通信 Lumentum +13.63%（财报+指引）/Credo +8.26%/Coherent +8.24%、新云 **NBIS +34.14%**（Q2 超预期+2026 指引上调+12.7GW）/CRWV +19.28%（$104B 订单）/Cerebras +11.63% 盘后 -12%、**NVDA +3.03% $224.09 6/2 以来新高**（GS 买入 $285、传鸿海 Q4 Vera Rubin single-source）；③大型科技回落（META -3.38%/MSFT -2.26%）——"AI 硬件 > 应用/软件"分化成当日最大结构特征；④SMCI 财报兑现放量 +16.49% 收 $36.81（EPS $1.70 vs $0.92 + FY27 营收目标 $72B + $60B 订单簿；Google Finance 口径营收 miss -3.83% tentative + 大行质疑毛利率持续性）；⑤中概 8/12 金龙 -2.38%、腾讯 ADR -5%+（Q2 capex 528 亿 +176% → FCF 转负），8/13 港股低开 -3%+ 拖累恒指 -0.6%。Top 20 变更：**NBIS 新入选 8.0**（Alpha#6 事件动量，但单日 +34% 后 Alpha#30 波动率强警告）+ **CRWV 新入选 7.8**（$104B 订单积压，高杠杆）；**SMCI 上调 7.6→8.0**（财报兑现 +16.49% + FY27 $72B 目标，Alpha#6/#1）；**MU 上调 8.1→8.4**（8/11 报告设定"8/12 续涨则 Alpha#53 反转确认完成"条件兑现，因子标签切换为 Alpha#1 动量 + #6 事件）；**NVDA 上调 9.2→9.3**（新高 + GS $285 + 连续两日背离解除）；**MSFT 下调 9.1→8.8 / GOOGL 下调 8.0→7.7**（板块内负背离/均值回复未确认）；移出 LMT/GS（无独立催化，国防/金融让位于 AI Infra 事件兑现者）。因子频次：Alpha#1 动量 60% + **Alpha#6 事件 55%（↑40%→55%，SMCI/NBIS/CRWV/Lumentum 全部事件驱动）** + Alpha#41 趋势 55%（↓）+ **Alpha#12 背离 15%（↑，板块内负背离新场景 MSFT/GOOGL/AMZN）** + Alpha#53/#30 各 10% + Alpha#19 5%（↓）。板块：Software/AI 5 只（25%）+ Semis 4 只（20%）+ Cons Disc 4 只（20%）+ **AI Infra 3 只（15%，SMCI/NBIS/CRWV）** + Energy 2 只 + HC/Financials 各 1 只——**AI 硬件/Infra 合计 35% 为 7/2 以来最高配置**。策略：8/13 PPI（ET 8:30）+ JD/NTES 盘前 + **AMAT 盘后**（期权隐含 ±11%）为事件窗口——只对"超当期+上调远期指引"型兑现配动量溢价；新云追高纪律（Cerebras 盘后 -12% 警示，单日暴涨后回踩承接不追高，波动率仓位 <5%）；8/26 NVDA 财报为 9 月前板块再定价锚。交叉参考：[[synthesis/2026-08-12/wq101-alpha-daily]]（前一期）、[[synthesis/2026-08-13/investment-daily]]（8/12 收盘全口径 + 腾讯 Q2 + CPI + AI 硬件爆发）、[[synthesis/2026-08-13/tech-report-digest]]（同日 DeepSeek V4 Pro GA / Qwen3.8-Max 权重 / Grok 4.6）。
- Updated: wiki/index.md（Synthesis 表新增 wq101-alpha-daily 2026-08-13 条目，插在 08-12 条目之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-13/wq101-alpha-daily.md
- Contradictions: 无实质矛盾——8/12 报告将 MU 设为"8/12 若续涨则 Alpha#53 反转确认完成"，本报告按 8/12 实际续涨（+4.92%，Barron's 口径）确认并切换因子标签，属条件兑现；NBIS/CRWV 前一日不在观察池内，为 8/12 单日事件驱动新入选，属新增而非矛盾；MU 8/12 收盘未获单一口径确认（Barron's +4.9% vs MarketWatch 延迟报价 $915.99），报告采用 +4.92% / ~$912-916 区间并标注 tentative；SMCI Google Finance"EPS 惊喜 +77.55% vs 营收 miss -3.83%"与 8/12 报告"EPS $1.70 vs $0.92 大超 ~85%"为不同共识基线口径，已并列标注；CSCO 8/12 盘后财报结果撰写时点未核验，报告仅以日间 $123.88 +2.86% 标注

## [2026-08-13] synthesis | game-rl-daily (2026-08-13)
- New page: wiki/synthesis/2026-08-13/game-rl-daily.md
- Summary: 9 verified new game-RL / game-AI papers over the Thu Aug 13 window (Wed Aug 12 submissions, IDs ~2608.11207–2608.12307; harvested from /list/recent pages of cs.AI/cs.LG/cs.CL/cs.GT/cs.MA/cs.CV/cs.HC/cs.RO). All 9 IDs grep-verified absent (0 hits) from the entire wiki; zero overlap with same-day arxiv-daily (37) / arxiv-paper-check (17) / conference-digest (3) — game/world-model items those digests claimed (AutoWorldModel-Bench 2608.11216, RIFT 2608.11521, Foresight WAM 2608.11605, Simulator Collapse 2608.12253) intentionally not duplicated.
- Categories: Game RL (Is Per-Agent Policy Composition Safe? successor-feature transfer in cooperative MARL, 2608.11658) · Game AI Bot (Do LLMs Take Care of Their Own? graded-similarity cooperation, Conitzer group CMU, 2608.12125; Poor Man's Agentic Modeling surrogate LLM-agent societies, 2608.11215; IF:CARGO LLM-as-semantic-compiler, AIIDE 2026, 2608.12195; Pharos Night AI-native deck-building MAS game, CHI Play 2026, 2608.12216) · World Models (Better Slots Better Worlds object-centric WM audit, MPI-IS/RLC 2026 workshop, 2608.12078; driving world-model counterfactual gap abduction-action-prediction, Purdue, 2608.11601) · Industry Game AI (Steam GenAI player-perception analysis w/ PCG baseline, Northeastern, 2608.11539) · Related (Semantic Lenia artificial-life in LLM logit space, 2608.11657) · PCG/Benchmarks: no new submissions (threads noted)
- Updated: wiki/index.md (Synthesis 表新增 game-rl-daily 2026-08-13 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-13/game-rl-daily.md
- Contradictions: none (all 9 IDs grep-verified absent; institutions marked "(inferred)" are inferred from author identity, "not stated/not identified" where unknown)

## [2026-08-13] synthesis | LLM Tech Report Digest (2026-08-13)
- New page: wiki/synthesis/2026-08-13/tech-report-digest.md
- Summary: 各大 AI 公司最新技术报告 / System Card 汇总（08-13 版）。**今日最大落地=08-12 双验收日兑现其二**——①**DeepSeek V4 Pro 官方 GA**（OpenRouter 上架 `deepseek-v4-pro-0813`：1M ctx、$0.435/$0.87 每 M tokens；V4 Pro 1.6T 总参/49B 激活 MoE + CSA、V4 Flash 284B/13B，均 **MIT 开放权重**，08-10~08-20 窗口第 4 天终结"涨价先行、GA 随后"悬念）；②**Qwen3.8-Max 开源权重兑现**（HF 出现 `Qwen/Qwen3.8-2.4T-A95B`：2.4T/95B 激活、1M ctx、license `qwen3.8-max`——08-12 实时检查仍无条目，08-13 撰写时已上架）。**Grok 4.6 官方信息补全**（08-12：500K ctx、text+image 入/text-only 出、无输出上限、$2/$0.50/$6 <200k 与 $4/$1/$12 >200k、reasoning low/medium/high/xhigh——"上线无 model card"文档差距收窄）。**OpenAI Astra Preparedness**（08-07）或首次触及 Critical 网络安全阈值；公开旗舰仍为 GPT-5.6 Sol。**Meta Llama 4 405B 开放权重持续未兑现（第 2 天）**——仅 NeuralStack 07-28 单一预告反复出现，llama.com 仍仅 Llama 4 Scout/Maverick。**MiniMax M3 取代 M2.7 成现役旗舰**（BenchLM 68.6 vs 63/100，M2.7 200K ctx/开放权重/$0.3/$1.2 已退役；08-08 M2.7"自我进化"MLE Bench Lite 66.6% 为其最后一个重大动态）。**Mistral 欧洲主权 AI 路线**（08-11：in-region inference + 开放模型 + 欧洲基础设施）+ Shieldstral 安全产品（08-04）+ 机器人 Robostral Navigate（AI Science Robotics，Théo Cachet/Arjun Majumdar 等）——无新 LLM 报告。字节 Doubao 155M 周活/全球第 4 大 GenAI 应用/春节峰值 ~145M DAU（Seed 品牌经火山引擎，旗舰 Doubao Seed 2.0 Pro 02-14）。智谱 GLM-5.2 旗舰（744B MoE/1M ctx/约 40B active/约 1/6 GPT-5.5 成本）+ GLM-4.7 预算默认（SWE-bench Verified 73.8%），GLM-5.3 传闻维持、GLM-5.5 未确认。Moonshot 仅 Kimi Code CLI 0.34.0（08-06：会话恢复/Windows Kimi Computer Use），无新模型。InternLM3-8B-Instruct（01-15，4T tokens、训练成本 -75%）+ InternThinker（11-25）+ InternBootCamp & InternThinker·Go（05-23）仍为最新，无 8 月新报告。StepFun Step 3（2025-07-31 开源，**321B/38B** 官方口径——⚠️修正 08-12 页"198B"）+ Step3-VL-10B（2026-01，PaCoRe）+ Step 3.7 Flash（196B+1.8B/11B、400 tok/s、~2026-03，single-source）。01.AI 转向企业 AI/主权 AI（万策平台 07、哈国 Q.AI 合资、老板/投资官/销冠 AI），最新模型仍 Yi-Lightning（2024-10），2026 无新旗舰。Microsoft Phi / Amazon Nova / Apple 均无 8 月新报告（Phi-5 仍 single-source；Nova 2024 报告仍唯一；Apple AFM 3"summer"承诺未兑现、上一代 TR 2025-07-17 ~3B+PCC）。NVIDIA Nemotron 3.5 Lightning（08-11）仍为家族最新。
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 2026-08-13 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-13/tech-report-digest.md
- Contradictions: 1 —— StepFun Step-3 规格修正：08-12 页记"198B 稀疏 MoE"，官方公告（IT之家/InfoQ/维基百科一致）为 **321B 总参 / 38B 激活**，本期以官方口径修正并在正文显式标注。另有观察项：Meta 405B 预告口径（07-28 NeuralStack）持续无发布实据，维持"未兑现"记录

## [2026-08-13] synthesis | Conference Digest — KDD 2026 落幕颁奖全景
- New page: wiki/synthesis/2026-08-13/conference-digest.md
- Summary: KDD 2026（Jeju 8/9–13）闭幕/收尾版 digest。**颁奖全景**——Test of Time = XGBoost (Chen & Guestrin, KDD '16, DOI 10.1145/2939672.2939785, 42,397 引用 / 300,534 下载); Best Research Paper HM = EARTH (HKBU Jianliang Xu + 博士生 Yun Peng, spatiotemporal K-function 分析加速 26×–19.04×, 官方口径 top-3/2,000+); SIGKDD Innovation Award = **Wei Wang (UCLA)**（⚠️修正早期检索片段将获奖者记为 Haixun Wang 的口径, 以 cs.ucla.edu 公告为准）; 主 Best Paper / Best Student Paper **未确认**（kdd.org 奖项页反爬截断, caveat 标注待补）; keynote 三人——Jeff Dean (8/11 "Important Trends in AI": Gemini/TPU/大规模训练, 自 8/5 离开 Alphabet 另立 Discovery Loop 后公开演讲)、Jingren Zhou (Alibaba CTO)、Regina Barzilay (MIT, 延续「高预测精度不足以保证支撑临床决策」主题)。
- KDD 2026 论文挖掘（Paper Digest 500 条库, DOI 核验）: ①Alibaba **MAC/MoAE** CVR 多归因机制 benchmark + Mixture-of-Asymmetric-Experts（充分学习 multi-attribution 知识 + 主任务中心利用, 12 作者含 Xiang-Rong Sheng/Han Zhu/Jian Xu/Bo Zheng, DOI 10.1145/3770855.3817488）; ②**DLL** Decoupled Listwise Learning 流式兼容 Listwise CTR——免 session batching 重建 session 级监督, 打破 listwise-shuffle 两难（Junlin He/Rui Tang/Liyin Hong, DOI 10.1145/3770855.3818327）; ③Tencent **确定性分配匿名联合广告**——证明非确定性分配在所有在线广告场景导致可行解不存在, 取整解-最优解 gap 理论化（Zhen Zhang/Qianlong Xie/Qi Qi/Xingxing Wang, DOI 10.1145/3770855.3818370）。共同主题: 工业广告/推荐在「标签—分配—训练结构」三层的严谨化。
- arXiv 精选 3 篇（全部 arXiv ID + 标题 grep 0 命中）: ①**Simulator Collapse**（One Frozen Simulator Is Not Enough, Stanford/Berkeley/MIT 跨组 10 人含 Levine/Manning/Shi, [2608.12253]）——单 LLM 模拟用户导致 policy 过拟合窄策略, 理论形式化 + 推理期 Verbalized Sampling + 训练期 Co-Training; ②**Mechanist**（NUS/ZJU 25 人含 Ningyu Zhang/Tat Seng Chua/Huajun Chen, [2608.12036]）——AI 作为科学仪器做自主机制发现, 13K 可解释知识图谱 + 43M 论文库/26 领域 + 32 基础方法库, 发现模态间安全风险迁移 + 信念机制理论 + DNA 定向生成干预; ③**VITA** 语料特异临床 RAG（Praveen Reddy 等 7 人, [2608.12138]）——LMIC（印度）场景专有语料 RAG 在 HealthBench 4,023 题 GPT-4.1 裁判下匹配/超越新 frontier LLM, 评测材料全公开。
- 去重: HealthBench 本体已覆盖于 2026-06-13 tech-report-digest（index/log 命中）, VITA 论文本体为新收录; FAT-CTR 已在 wiki/papers/ctr/fat-ctr-scaling.md 覆盖故仅导航; 同日 37+17 篇 arXiv 归 [arxiv-daily](./arxiv-daily.md) + [arxiv-paper-check](./arxiv-paper-check.md) 不重复; KDD 开幕前口径/KDD Cup/组织变更见 08-08 digest。
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 2026-08-13 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-13/conference-digest.md
- Contradictions: 1 —— Innovation Award 获奖者口径修正: 早期检索/摘要片段记为 Haixun Wang, 本期以 UCLA CS 官方公告核实为 **Wei Wang**（已在 digest 正文与本期条目中显式标注）; 主 Best Paper / Best Student Paper 名单未确认, 待 kdd.org 奖项页可访问后补录

## [2026-08-13] synthesis | arXiv Paper Check — AI & CTR (August 13, 2026)
- New page: wiki/synthesis/2026-08-13/arxiv-paper-check.md
- Coverage: 17 curated papers from the **Thu Aug 13, 2026 announced window** (submissions Aug 11–12; IDs ~2608.11207–2608.12307; cs.AI 211 new / cs.IR 16 new). Complement to the same-day arxiv-daily (which claims the CIKM 2026 rec cluster HCGRec/PRISM/GALLM/FunnelCausalNet/Token-Level-Credit, OPD/RL diagnosis, agent-memory formalization, PIC/KV efficiency). Every arXiv ID grep-verified absent (0 hits) from the entire wiki before inclusion.
- Sections: ①CTR/Rec/Ads/IR (8) — IToM inverse theory-of-mind rec, inferred personas match/exceed ground truth, RecSys '26 [2608.11354]; RecSys Factory autonomy-at-decision-points, 78-day/3 Tencent rec lines, 1,624 CLI dispatches @ 78.6%, 400-entry PitfallStore [2608.11241]; LOFA RL-over-verifiable-purchase-outcomes + feedback-aware OPD from real shopping logs [2608.11604]; Gemini Embedding 2 vs frontier LLM rankers on Flickr30k — GPT-4.1/Claude Sonnet 4.6 at par [2608.11343]; TRACES epistemic-reliability — 42 retracted papers, 30 models fail >71% agentic probes, topic-keyed safety ≠ epistemic competence [2608.11415]; Sci-Surf verbalized-profile intent rec +10.4% alignment [2608.11973]; LODESTAR reinforced polarizer scoring text interventions by induced uncertainty, F1 0.5148→0.5339, wins all 70 cells [2608.11922]; Total-Recall-at-What-Cost agentic-memory serving cost — unpredictable from length (regression misses 18–69%), break-even never within 400 turns (worst), accuracy 21–54%, no system wins both axes [2608.11879]; ②AI/Agents/Eval/Security (9) — AgonAlpha verified-artifact alpha mining + fresh-context adversarial reviewer w/ veto, WorldQuant BRAIN Fitness 9.50/Sharpe 3.48 [2608.11250]; FrontierFinance 220 queries/11,543 rubrics — harness not model dominates, Samaya 56.0% vs Claude Fable 5 49.2% @2.2× lower cost, open Kimi K3 46.4% @4.5× lower cost [2608.11683]; VAKRA 8k+ APIs/62 domains — best 70.4% single-hop / 50–51% compositional, 2.4% on unanswerable policy queries, failures language-mediated [2608.12282]; Sleeping Agent gist-compression temporal loss — 1-sentence prompt fix 3.05%→62.39% (+0.314) [2608.11775]; Budget-Dependent Rankings — 3–19% non-monotone items, rankings reverse across budgets, oracle complementarity +27.8pp, router captures 14.1% [2608.12150]; Graph-Structured Rubrics typed eval graphs +0.62–6.75pp over Prometheus-style [2608.12097]; When Self-Consistency Backfires — majority vote hurts majority of GPQA-D for small LLMs (56.6% Qwen2.5-7B / 65.7% Llama-3-8B), pre-registered, confidence ≠ correctness [2608.11403]; ForeWAM latent-futures direct-policy WAM, Future-KV reuse, 96.7–96.9% LIBERO no future video [2608.11605]; GraphRP GNN model-extraction defense, structure-aware firewall + Fisher-information, KDD 2026 [2608.11495]
- Cross-cutting trends: rec moves from "what the user did" to "why the user acted" (IToM/LOFA/Sci-Surf); evaluation attacked on budgets/confidence/composition (Budget-Dependent Rankings / Self-Consistency-Backfires / TRACES / GSR); agent robustness re-engineered at input/context layer (LODESTAR/RecSys Factory/Sleeping Agent/VAKRA); finance-agent stack as first-class benchmark space (FrontierFinance/AgonAlpha — counterpart to the wiki's wq101-alpha-daily thread); rollout-free WAMs converge on KV-state reuse (ForeWAM ↔ daily's RIFT)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-paper-check 2026-08-13 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-13/arxiv-paper-check.md
- Contradictions: none (all 17 IDs grep-verified absent from wiki; batch identity cross-checked against arXiv /list recent pages — Thu Aug 13, 2026 confirmed as latest window; institutions marked "(likely)" are inferred, "—" means not identified)

## [2026-08-13] synthesis | arxiv-daily (2026-08-13)
- New page: wiki/synthesis/2026-08-13/arxiv-daily.md
- Summary: 37 curated papers from the **Thu Aug 13, 2026 announced window** — Wed Aug 12 submission wave (IDs ~2608.11207–2608.12307), harvested from the `/list/{cat}/recent` pages for cs.AI (211), cs.LG (182), cs.CL (92), cs.IR (16), cs.GT (5), cs.MA (18), econ.TH (5), stat.ML (11) = 540 entries / 380 unique IDs. All 37 IDs grep-verified absent (0 hits) from the entire wiki; zero overlap with the 08-12 digests (which ended ~2608.11208). First 2026-08-13 synthesis page.
- Categories (10 sections): LLM Post-Training/Rollout RL/OPD (5: GCPO subspace-geometry diagnosis+constraint [2608.11674]; PAIR U-statistic pair-contrast rollout allocation [2608.11368]; REOPD reliability-adaptive reward extrapolation [2608.11698]; OPD×TTS "illusory distillation" — OPD improves sampling efficiency not capability boundary [2608.11829]; Rubric Dropout reward-hacking fix [2608.11669]) · Reasoning/Test-Time (3: SFS-DPO step-level self-correction [2608.11573]; AI4AI strong-to-weak harness transfer 0.49→0.91 [2608.12307]; Small-Scale Experiments hyperparameter-focus methodology [2608.11859]) · Model Editing/Merging/Personalization (3: Weightless Fine-Tuning logit-space transport <7% SFT compute [2608.11342]; Orientation-not-magnitude preregistered task-vector interference causal structure [2608.11797]; HyperFix subset-conditioned nonlinear corrections [2608.11499]) · Agents/Skills/Memory (4: EvoGraph-Mem failure-aware editable insight graphs [2608.11248]; Formal Agent Memory basis/span/coverage + Odyssey instantiation [2608.11654]; Agent Skills Can Be Harmful — 307 skill-induced failures + SkillTriage [2608.11888]; SHAPER train-free skill-harness self-evolution [2608.11350]) · Recommendation/CTR/Ads (6: HCGRec hint-conditioned semantic-ID GRPO, zero-advantage 70%→20%, CIKM 2026 [2608.11980]; PRISM similarity-bias attention diagnosis, CIKM 2026 [2608.11846]; GALLM graph-relations-as-attention-bias LLM rec [2608.12184]; Personalized LLM Judges bidirectional-rationalization + alignment, +32.19% Macro-F1 [2608.11493]; FunnelCausalNet funnel-composed coupon uplift, CIKM 2026 [2608.11675]; Token-Level Credit Assignment GenIR [2608.12049]) · Sequential/TS/Finance (4: FM-LLM spectral frozen-LLM forecasting, 59/78 SOTA [2608.11623]; RG-ResMoE regime-in-routing-gate volatility [2608.12251]; Forma statement-tuple forecaster 1–20Q beats FMs/LLMs [2608.11327]; RoPE periodic-vs-conventional expressivity theory [2608.11909]) · Efficiency/KV (3: LinearKV single-state hybrid PIC, exact composition harmful on Mamba-2 [2608.11231]; QV-PIC query-aware visual PIC +21.6 F1 [2608.12121]; Massive Activations HLA PAS/ISP taxonomy [2608.12149]) · Games/GT/Mechanism (4: Welfare in Multilateral Trade O(k²)/Õ(k^1.5) [2608.11351]; Roommate Problem blocking-neutral concept [2608.11682]; VCR verifiable-content rewards vs citation wars [2608.11390]; Institutions-beat-Intelligence collective-reasoning boundary [2608.11357]) · Safety/Alignment/Unlearning (3: Implicit Personalization activation localization r=0.87 [2608.11735]; MLP mid-network refusal localization ≥2.7× [2608.11583]; J-Access unlearning Jacobian audit, don't-optimize warning [2608.11408]) · World Models (2: AutoWorldModel-Bench research-style agentic benchmark, EA [2608.11216]; RIFT rollout-free future K/V cache 98.8% LIBERO [2608.11521])
- Cross-cutting trends: OPD/rollout-RL from recipes to diagnosis-and-constrain; agent memory formalized + skills stress-tested (formal basis/span theory, EvoGraph-Mem, 307-failure skill attribution); CIKM 2026 rec attacks structural training signals (HCGRec/PRISM/GALLM); PIC/KV meets hybrid attention + visual RAG (LinearKV/QV-PIC/Massive Activations); test-time/no-weights adaptation matures (AI4AI/WFT/SHAPER); model merging gets causal-structure account; mechanism design meets generative engines (VCR); forecasting doubles down on specialist structure (Forma/RG-ResMoE/FM-LLM)
- Key takeaways: OPD "trust but verify" phase (illusory-distillation critique + geometry/allocation/reliability fixes); agent memory/skills now measured for failure cost; rec finds structural non-scaling wins; specialist-vs-generalist forecasting evidence (Forma vs FM-LLM); "where information enters" as key design axis (RG-ResMoE); LinearKV negative result cautions against algebraic elegance ≠ serving wins; VCR directly actionable for GEO/citation ecosystem
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-13 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-13/arxiv-daily.md
- Contradictions: none (all 38 IDs grep-verified absent from wiki; batch identity cross-checked against arXiv /list recent pages — Thu Aug 13, 2026 confirmed as latest window; institutions marked "(likely)" are inferred, "—" means not identified)

## [2026-08-13] synthesis | Investment Daily (2026-08-13)
- New page: wiki/synthesis/2026-08-13/investment-daily.md
- Coverage: 全球科技与 AI 板块投资日报（周四版·A股/港股盘中口径）。美股/中概 = 8/12 周三完整收盘——美国 7 月 CPI 落地（未季调年率 +3.4% 符合预期、月率 +0.1%、核心 +2.5%，FedWatch 9 月加息概率降至 42%；同日 420 亿 10Y 拍卖 4.683% 创 2007 年来最高）；三大指数涨跌不一（道 -0.04% 53,770.27 / 标普 +0.26% 7,748.50 / 纳指 +0.54% 26,588.49），**费半 +2.49% AI 硬件全面爆发**——存储（SK海力士 +9.01%/Seagate +7.03%/SanDisk +5.76%/MU +4.92%）+ 光通信（Lumentum +13.63% 财报指引上调/Credo +8.26%/Coherent +8.24%/Corning +5.18%）+ 新云（NEBIUS +34.14%/CoreWeave +19.28% $104B backlog/NCLD +17.26%/IREN +9.86%/Cerebras +11.63% 盘后 -12%）+ **NVDA +3.03% $224.09 阶段新高**（GS $285/传鸿海 Q4 供 Vera Rubin）+ SpaceX +9.65%（Grok 4.6）；大型科技回落（META -3.38%/MSFT -2.26%）"AI 硬件 > 应用"分化。中概 8/12：金龙 -2.38%（单来源）、腾讯 ADR 大跌逾 5%、万国数据 $32.74 +0.34%。港股 = 8/12 完整收盘（恒指 -0.83% 25,440.17 / 恒科 -0.99% 4,776.44 / 国企 -0.96% 8,446.27——房地产金茂 +13.92% 领涨、存储/光通/PCB 活跃、TME -12.55% 科网走弱）+ 8/13 开盘（恒指低开 0.6%/恒生科技 -0.29%/腾讯 -3%+ 拖累，人民币中间价 6.7888 下调 6 点、央行零规模逆回购）。A股 = 8/12 完整收盘（沪指 +0.32% 约 3,946.5/深成 +1.09%/创业板 +1.49%/科创50 +1.61%，成交 21,672 亿缩量，光纤/CPO/AI 应用/算力租赁活跃、百花医药 7 连板）+ 8/13 盘中待午间确认。重点主题：①**腾讯 2026 Q2 实际业绩**——收入 2,047.85 亿（+11% 超预期）Non-IFRS 经营盈利 756.36 亿（+9%；剔除新 AI 产品 +19%）净利率 36.9%，但 **capex 528 亿（+176%）自由现金流转负**、现金净额 1,469→582 亿；分业务游戏 659 亿单季新高/营销服务 +22%/金科企服 +9%；AI 产品 Hy3 正式版（OpenRouter 调用量前三、首周较 Hy2 +68 倍）WorkBuddy 解决率 72%→90%、微信"小微"灰度；H1 回购 244 亿；投行摩根大通 690 港元/全年 capex 2,000 亿、大和 1,810 亿——市场定价"业绩 beat vs FCF 折价"分歧（华盛通"奥德赛期"框架）；②今日 8/13 港股财报"四连击"——中芯国际（盘后 Q2 + 8/14 说明会；Q1 收入 $25.05 亿/利用率 93.1%，Q2 指引环比 +14-16%/毛利 20-22%）华虹/联想/京东 + 美股 AMAT（美东 8/13，北京时间 8/14 凌晨）；③美股新云/数据中心 + 万国数据（Q1 净收入 +23.6%/三年 300-500 亿投入/REIT 计费率 >97%）；④中汽协 7 月新能源月度占比首超 60%（累计首超 50%）+ 央行 Q2 货政报告适度宽松 + IEA 石油缺口 180 万桶/日 + 美银对冲基金连续第 6 周净买入 + 韩股技术性牛市。交叉参考：今日 [[synthesis/2026-08-13/tech-report-digest]]（DeepSeek V4 Pro GA + Qwen3.8-Max 权重兑现）、[[synthesis/2026-08-12/investment-daily]]（8/11 收盘 + 8/12 盘中、存储超级周期 + CPI 前瞻）、[[synthesis/2026-08-12/wq101-alpha-daily]]（SMCI 财报入选 + AMAT 财报窗口）。
- Updated: wiki/index.md（Synthesis 表新增 investment-daily 2026-08-13 条目，插在 08-13 tech-report-digest 条目之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-13/investment-daily.md
- Contradictions: ①⚠️ 已废弃财联社 flash"腾讯 8/13 09:56 +2% 报 573 港元（创 2021 年 6 月新高）"——与 8/12 收盘 461.6 港元（-1.95%，上证报/中国基金报确认）及 8/13 开盘 -3%+ 直接矛盾，已在报告数据说明标注废弃；②⚠️ 已排除 2024-08-13 同期旧闻（nbd"8/13 早盘恒指 +0.28% 报 17,160.21"系 2024 年文章——文内"腾讯 8/14 公布 2024 年二季度"佐证）；③金龙/利弗莫尔/阿里 8/12 数值为截断检索单来源，标注 tentative；④GDS Q2 2026 实际数撰写时未捕获（仅券商预测收入 +9%/经调整 EBIT +9%）；⑤A股/港股 8/13 盘中数据撰写时未独立确认待午间收评
- New page: wiki/synthesis/2026-08-12/game-rl-daily.md
- Summary: 13 verified new game-RL / game-AI papers over the Wed Aug 12 window (deep-scan follow-up — Aug 11 wave IDs ~2608.10325–2608.11208, late-Aug-10 tail ~2608.10008–2608.10324, plus absent Aug 10 fill-in ~2608.09000–2608.09926). All 13 IDs grep-verified absent (0 hits) from the entire wiki; zero overlap with same-day arxiv-daily / arxiv-paper-check / arxiv-ai-search / conference-digest.
- Categories: Game RL (guided tour 2608.09389; extensive-form switching regret 2608.09501; DTOA Byzantine-robust team fictitious play 2608.09256) · Game AI Bot (Hierarchical Games 2608.09574; Not a Monolith evolutionary IPD 2608.10262; CEAA NPC/IVA architecture 2608.09848) · World Models (FACT failure-aware causal WAM 2608.10232; LeWorldModel eval-protocol reproduction 2608.10145) · Benchmarks (DSLE Dark Souls, AAAI AIIDE 2026, 2608.09902) · Related (A-DFL GameSec 2026 2608.09036; competitive mediator games 2608.09894; IRL Fisher hypergradient 2608.11052; EDPFRL-IM curiosity federated RL 2608.10499) · PCG/Industry: no new submissions (cross-refs)
- Updated: wiki/index.md (Synthesis table — game-rl-daily 2026-08-12 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-12/game-rl-daily.md
- Contradictions: none (LeWorldModel reproduction's negative eval-fidelity findings noted as a reproducibility warning, not a contradiction)

## [2026-08-12] synthesis | LLM Tech Report Digest (2026-08-12)
- New page: wiki/synthesis/2026-08-12/tech-report-digest.md
- Coverage: 各大 AI 公司最新技术报告 / System Card 汇总（2025-2026），20 个公司/实验室分节 + 交叉观察，沿用 08-11 基线结构
- 今日增量（相对 08-11）:
  - **⚠️ Meta "Llama 4 405B 开放权重 08-12" 验收失败（关键纠偏）**：当日无 405B 开放权重、无 Meta 官方技术报告；实际为 08-10 开放权重战略转向——开源 30B **Muse Glimmer**（Apache 2.0、128K ctx、本地运行、由 Muse Spark 蒸馏）+ 承诺数周内开源 **Muse Spark 1.2** 权重（Muse Spark 4 月首发为闭源）+ Zuckerberg 6000 字文章《The Future Is for Everyone》（Ars Technica 08-10）；llama.com 目录仍为 Llama 4 Scout/Maverick（2025-04 时代）。08-11 页的 405B/15T tokens/11-14 基准细节源自 Bloomberg/NeuralStack 预告口径，今日确认未发生，不保留为正式发布条目
  - **⚠️ Qwen3.8-Max 权重验收日（08-12）截至撰写时未兑现**：ModelScope 发布页指向今日（08-12），但 HF Qwen org 实时检查仍无 Qwen3.8-Max / Qwen3.8-27B 权重条目（最新为 Qwen3-ASR ~07-22），license 未发布（byteiota 08-07 提示草案曾含 US/EU/UK/Korea 地域限制争议）；Qwen3.8-27B 同为今日验收
  - **OpenAI 下一大模型官方定名 Astra（08-01 官方博客）**：内部版本解决 10 道数学/理论计算机难题（非软 sofic、Connes rigidity 反例、高维 sphere packing 界、Erdős 问题等）；"next major model"、The Information 确认新家族为 long-running workloads 设计；GPT-5.7 传闻被搁置；最新正式发布仍为 GPT-5.6（System Card 07-09）
  - **NVIDIA Nemotron 3.5 Lightning（08-11）**：30B-A3B 开放 MoE，面向 always-on agents；Nemotron 3 家族（Ultra/Super/Nano）保留
  - **MiniMax M2.7 自我进化（08-08 官方新闻）**："第一代自我进化"模型——自建 Agent Harness 参与迭代自身模型；MLE Bench Lite 22 任务 66.6% 得牌率（9 gold/5 silver/1 bronze 最佳 run），仅次 Opus 4.6（75.7%）/ GPT-5.4（71.2%），与 Gemini 3.1（66.6%）持平；已在 MiniMax Agent/开放平台全量上线；M3 仍现役 SOTA、M4 仍 H2 2026 承诺
  - **DeepSeek API 涨价公告（08-06）**：官方宣布近期整体大幅上调定价；峰谷计费（工作日 9-12/14-18 高峰 = 2 倍）；平时价 V4-Flash 1/2 元、V4-Pro 3/6 元每 M tokens；业内预期 V4-Pro GA 临近；V4-Pro 官方窗口今日第 3 天（08-10~08-20）仍无 GA 公告
  - **字节跳动 >5T/10T 参数新模型训练传闻（08-06/07）**：晚点 LatePost（>5T）vs 金融时报（10T，或超 Mythos 5 约 8T）；Seed Foundation 负责人项亮主导 + 预训练数据负责人沈科合作；张一鸣 Seed 全员会表态反对蒸馏（"复制 Claude 能力难超越"）、编程是关键非唯一热点、接受短期落后；梁汝波承认豆包 AI Coding 不突出；预训练早期（3-6 个月），未发布
  - **Baichuan-M2（08-11）**：开源医疗增强大模型，32B，HealthBench 60.1，以 32B 尺寸超 gpt-oss-120B；延续医疗垂直战略（M4 HealthBench 68.6 世界第一保留）
  - **Anthropic Fable 5.1 事实核查（08-03）**：AIToolsReview 确认无官方公告——仅两条 X 泄漏（Pankaj Kumar 07-26 + Lumina），$10/$50 定价为传闻；Opus 5 已部分超越原 Fable 5；不写入正式条目
  - **Google DeepMind 领导层改组（08-05，Reuters）**：Hassabis 转任主席（兼 Alphabet 首席科学家）、Kavukcuoglu 升 SVP、Jeff Dean 离职另有任用；Gemini 3.5 Pro 仍延迟，Gemini 4 预期 11-12 月（Pichai 称"最雄心勃勃预训练"）
  - **智谱口径转向 GLM-5.3**：JPMorgan（8 月 >1T）+ 新浪财经（07-20）口径为新旗舰 GLM-5.3；GLM-5.5 为早期传闻未确认；均未发布，GLM-5.2 仍为确认旗舰
  - **Mistral（08-02 新闻）**：将推出 Code/Apps sections（Vibe/Le Chat）+ 夏季新"大而稀疏"开放 MoE 权重预告（未发布）；无新报告
  - **InternLM 补充**：Intern-S2-Preview-397B 于 WAIC 2026（07-01）以 397B 追平此前万亿模型（书生·端砚平台）；35B/397B 07-17/18 已收录
  - 复核无变更：Apple AFM 3（技术报告存在、正式发布承诺未兑现）/ Grok 4.6（已上线但官方 docs.x.ai 仍仅列 grok-4.5，无 model card，Grok 4.7 3-4 周后）/ Microsoft Phi-5（无官方报告）/ Amazon Nova（Nova TR 2024 仍唯一正式报告，re:Invent 2026 为下一观察点）/ StepFun / Yi / OpenAI GPT-5.6
- Key trends: 08-12 双验收日两"承诺制发布"均未兑现（Llama 4 405B + Qwen3.8-Max 权重）——对照 Kimi K3 按期放权（07-27）与 Nemotron 家族报告齐备，"承诺→兑现"信用分化加剧；同日并存新发布（Nemotron 3.5 Lightning / MiniMax M2.7 / Baichuan-M2 / DeepSeek 涨价 / Astra 定名 / DeepMind 改组）；"规模军备竞赛"叙事升级（字节 >5T~10T + Grok 4.7 2.1T + Kimi K4 + GLM-5.3 + M4）；闭源前沿"文档差距"持续扩大（Grok 4.6/V4-Pro/AFM 3 vs 开源阵营）
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 2026-08-12 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-12/tech-report-digest.md
- Contradictions: ⚠️ 验收失败已如实记录——08-11 页所载 "Llama 4 405B 08-12 开放权重（Bloomberg/NeuralStack 预告口径）" 与 08-12 当日实际（无 405B 发布、改为 Muse Glimmer 开源 + Muse Spark 1.2 权重承诺）矛盾，本页已纠偏并说明不保留为正式发布条目；Qwen3.8-Max "ModelScope 页面指向 08-12" vs "截至 08-12 撰写时 HF 无权重条目" 矛盾已标注（验收日未兑现）；字节新模型规模口径 >5T（晚点）vs 10T（FT）矛盾已标注为传闻；其余继承条目显式标注"保留"，新增均标注来源

## [2026-08-11] synthesis | LLM Tech Report Digest (2026-08-11)
- New page: wiki/synthesis/2026-08-11/tech-report-digest.md
- Coverage: 各大 AI 公司最新技术报告 / System Card 汇总（2025-2026），20 个公司/实验室分节 + 交叉观察，沿用 08-10 基线结构
- 今日增量（相对 08-10）:
  - **Meta Llama 4 开放权重明日（08-12）发布，今日核实新增细节**：405B 参数、原生多模态（文本/图像/音频）、单 H100 推理 32 tok/s、**15T tokens 训练含 2.4T 图文对**、**11/14 基准达到或超过 GPT-5 且推理计算量少 38%**、**70B 蒸馏边缘版**（neuralstack.network 援引 Bloomberg）；Meta 官方技术报告仍待发布，08-12 为最终验收日；405B 与 Behemoth "近 2T" 口径提示保留
  - **DeepSeek V4-Flash 官方 API 公开 beta（07-31）核实**：9 项 Agent 基准齐备——Terminal Bench 2.1: 82.7 / NL2Repo: 54.2 / Cybergym: 76.7 / DeepSWE: 54.4 / Toolathlon verified: 70.3 / Agent Last Exam: 25.2 / Automation Bench: 25.1 / DSBench-FullStack: 68.7 / DSBench-Hard: 59.6（releasebot.io/updates/deepseek）；V4-Pro 官方窗口今日第 2 天（08-10~08-20）仍无公告
  - **Qwen3.8-Max 开源权重窗口今日第 2 天**：截至今日 HF/ModelScope 仍无权重条目，缺日期/license/model card；2.4T MoE / 95B 激活 / 1M ctx / $2/$6 per M；Qwen3.8-27B 同日发布（08-03）
  - **Grok 4.6 状态升级："已上线但官方 model card 缺席"**：第三方（kie.ai 07-30、blog.4sapi.com）确认约 08-07 上线，1.5T 参数沿用 Grok 4.5 V9 基座、重点大幅升级 SFT+RL；但 xAI 官方 docs.x.ai 目录仍仅列 grok-4.5，API release notes 无 4.6 条目——"上线 vs 官方目录"矛盾持续；无官方 model card/基准/上下文/定价；Grok 4.7（2.1T）计划 3-4 周后
  - **Anthropic Claude Mythos Preview System Card 核实**（PDF 2026-04-07）：当前最先进闭源前沿；首个按 RSP v3 发布决策审查的系统卡；与 Opus 5 System Card（07-24）、Fable 5.1 泄漏（未确认）并列
  - **ByteDance Seed2.1 Model Card 确认**：Pro + Turbo，Agent/代码工程（agentic + coding E2E），视频理解多评测 SOTA 含小时级长视频，官方 Model Card PDF 随发布（seed.bytedance.com/zh/seed2_1）；Pro 06-23 报道 dev crowdsource coding 59.1% 击败 Claude Opus 4.6
  - **智谱 GLM-5 技术报告核实**（2026-02-22）：DSA（DeepSeek Sparse Attention）稀疏注意力 + 异步 RL 基础设施 + 异步 Agent RL 算法，端到端软件工程超此前开源基线，完全适配华为等国产芯片；36kr 08-09 复述报道；GLM-5.5 仍为 JPMorgan 8 月单源传闻
  - **Moonshot Kimi K4 训练传闻复核**：The Information/AI Weekly 07-28/29 报道寻求更多 NVIDIA Blackwell 芯片，训练阶段未发布；K3 全量权重 + 47 页技术报告（07-27）仍为最新
  - **Apple AFM 3 技术报告已存在**（"Introducing the Third Generation of Apple's Foundation Models"，5 模型含 AFM 3 Cloud Pro PCC on Google Cloud NVIDIA GPU）但 06-08 承诺的 "later this summer" 正式发布仍未兑现
  - **NVIDIA Nemotron 3 家族保留**：Ultra（550B/55B hybrid Mamba-Attention MoE + LatentMoE，1M ctx）/ Super（120B/12B）/ Nano（30B-A3B）；官方家族总报告仍待发布
  - 复核无变更：OpenAI（GPT-5.7 泄漏未确认，GPT-5.6 System Card 07-09 仍最新）/ Google（Gemini 3.1 Pro 卡 02 为最新 Pro 卡，8 月仅 Classroom 更新）/ Mistral（Large 3 2025-12 仍最新自有模型，聚合层定位）/ Microsoft（Phi-5 无官方报告）/ Amazon（Nova TR 2024 仍唯一正式报告，FMR 战略收缩）/ InternLM / Baichuan / StepFun / Yi / MiniMax（M4 仍 H2 2026）
- Key trends: 明日 08-12 "承诺制发布"集中验收（Llama 4 开放权重 + Qwen3.8-Max 权重第 3 天 + V4-Pro 窗口 + Grok 4.6 model card）；闭源前沿"文档差距"持续（Grok 4.6 上线无卡 / V4-Pro 官方版窗口期 / Apple AFM 3 承诺未兑现 vs 开源阵营 K3 47 页报告、Nemotron 3 家族报告齐备）；Agent 能力成官方评测新主战场（V4-Flash 9 项 Agent 基准 vs Opus 5 / Muse Spark 1.2 / Grok 4.5）；稀疏注意力进入收敛期（CSA/DSA/Mamba-Attention/Qwen hybrid/MiniMax H3）
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 2026-08-11 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-11/tech-report-digest.md
- Contradictions: ⚠️ 时间表矛盾已标注——kie.ai 等第三方宣称 Grok 4.6 约 08-07 上线 vs xAI 官方 docs.x.ai 目录/API release notes 无记录（结论：已上线但无官方 model card，明确标注）；Qwen3.8-Max "本周放权"承诺 vs 截至今日 HF/ModelScope 无条目（窗口第 2 天，继续观察）；Llama 4 405B vs 早期 Behemoth "近 2T" 口径（以 08-12 实际发布为准）。其余无（继承条目显式标注"保留"，新增均标注来源）

## [2026-08-11] synthesis | arXiv Paper Check — AI & CTR (August 11, 2026)
- New page: wiki/synthesis/2026-08-11/arxiv-paper-check.md
- Coverage: No new arXiv batch in the last 24h — latest announcement still Mon Aug 10, 2026 (cs.AI 88 new / cs.IR 9 new), fully curated in the 08-10 paper-check (36 papers); Tue Aug 11 batch lands ~20:00 ET (= 08:00 +08 Aug 12). This report = **second-pass deep scan of the same Mon Aug 10 batch**: 18 additional papers (IR/Rec/Ads/Finance 5, MoE & Efficiency 3, World Models & Agentic Science 4, Agent Safety/Eval/Benchmarks 6), every arXiv ID grep-verified absent from the wiki before inclusion
- Sections: ①CTR/Rec/Ads/IR — SAGEO Arena (first realistic end-to-end SAGEO evaluation, existing SEO/GEO approaches impractical & degrade under realistic generative-search pipelines, structural info mitigates, KDD 2026 [2602.12187]), Pre-Inference Routing (difficulty-predictive cheap/strong extractor routing, calibrated router −31–33% cost on receipts / −77% on degraded ad-buy forms, F1 within 0.02, genre-dependent [2608.06607]), DocMemo (tri-level Document Schema / Page Belief / Episodic memory + dynamic Bayesian belief updating with Thompson sampling, SOTA on 3 benchmarks [2608.07067]), FinRank (evidence-first financial QA/retrieval over SEC 10-K/10-Q, 1,185 records / 22 companies, provenance-sensitive hard negatives, 7B embedder 44.8% R@10 ceiling [2608.07400]), Accounting Graph Transformer (13-KPI SME forecasting over accounting-relation graph, MAE 0.6990 beats LightGBM/TimeMixer/SOFTS [2608.07037]); ②LLM Arch/MoE/Efficiency — TEXAS (correctness-conditioned task-expert discovery via success/failure activation contrast + token-level supervision allocation, best/tied 17/18 settings across 3 MoE models [2608.06396]), Policy-Masked Private Experts (disjoint private expert branch selected pre-top-k, zero unauthorized executions across 64 adversarial scenarios on Qwen3-30B-A3B / DeepSeek-V2-Lite, allow-deny-allow recovery [2608.06690]), ReQuant (backprop-free fixed-grid discrete refinement for PTQ, plug-and-play on any initializer [2608.07019]); ③World Models & Agentic Science — TaskSense (differentiable stochastic spatial attention + inverse dynamics, beats DreamerV3 on Distracting Control Suite [2608.06544]), Surg-UniWorld (Hierarchical Surgical Anchor + multimodal control experts on Wan2.2 video-diffusion backbone, Cholec80-SurgWAM benchmark [2608.06770]), CGMas (multi-agent LLM polymer CG-MD, 27/27 tasks, density within 5% in 22, 38–88 min → 1 min [2608.06694]), MolBioKG (multi-resolution structural anchoring into 9.6M-edge biomedical KG, multi-hop Hits@10 0.585→0.876 [2608.06713]); ④Agent Safety/Eval/Benchmarks — StepJack (multi-step indirect prompt injection over navigation chains, ASR +31.2 pts on 3/6 CUAs, GPT-5.4-mini 41.7→72.9% [2608.06477]), BFI-Adapt (first event-induced personality-evolution benchmark, PC-Agents simulate mean not shape of human personality dynamics, dispersion compressed 3–4× [2608.06485]), CyberForge (verified vulnerability injection, 1,034 validated vulns / 80 projects, SEC-bench +3.3–14.7 pts, 31B student matches GPT-5.4-mini teacher 72.7% vs 74.0% [2608.06471]), NxN E-valuation (e-value CRT hypothesis certification for LLM exploration [2608.06621]), Automated item evaluation (DeBERTa item triage, Accuracy .75 / AUC .80, math F1 .73 ≫ ELA .51 [2608.06609])
- Version/cross-list updates: Netflix generative recommender 2605.23312 v2 (RecSys '26) → note on existing paper page netflix-generative-recommender-scaling; SAGEO Arena 2602.12187 first appearance; READ 2608.06305 v2 (already covered in 08-07 arxiv-daily); Two Tower theory 2403.00802 v2
- Updated: wiki/index.md (Sources 表新增 arxiv-paper-check 2026-08-11 条目; Synthesis 表新增 arxiv-paper-check 2026-08-11 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-11/arxiv-paper-check.md
- Contradictions: none (all arXiv IDs grep-verified absent from wiki; batch identity cross-checked against arXiv /new listing — Mon Aug 10 confirmed as latest)

## [2026-08-08] synthesis | Conference Digest
- New page: wiki/synthesis/2026-08-08/conference-digest.md
- Coverage: KDD 2026 (Jeju 8/9-13) 开幕倒计时·最后一期开幕前全景——A*STAR CFAR 7 篇录用、Bohrium 分析 1,215→256 ≈21% 复核、⚠️ KDD 官网 OpenReview 数据泄露通告 (tentative, single-source)；NeurIPS 2026 三城联动官宣 (Sydney 12/6-12 + Atlanta 12/8-13 + Paris 12/9-13)，⚠️修正 08-07 digest 的 San Jose 单城口径；2027 议程前瞻——RecSys 2026 Minneapolis 9/28-10/2 (PC = Minmin Chen / Bart Goethals / Martijn Willemsen；GC = Konstan / Karypis / Adomavicius)、CIKM 2026 accepted TBD、EMNLP 2026 accepted 名单已上线 (Porto 11/2-6) + 引用 EMNLP 2025 Knowledge Infusion Scaling Law [2025.emnlp-main.1331, Alibaba Lv et al., memory-collapse threshold + critical collapse point 随模型规模 scale up]；arXiv 大厂精选 8 篇新增 (全库 grep 去重, 2608.xxxxx 本周批次)——Google DeepMind ResidencyRL 临床模拟 RL [2608.07418, 35 作者含 Quoc V. Le/Raia Hadsell/Joelle Barral/Dale R. Webster], Meta Skaling 耦合 Scaling Law [2608.07222, Videau/Youbi-Idrissi/Lopez-Paz/Ahuja, MAPE -1.5-3x, 全网格外推 ~10× 更少计算], TM20K 电商 20K 级序列蒸馏 (老师保留全 token, 学生学合并) [2608.07055], HD-Rec 华为 Noah's Ark + CityU 分层量化 + 域自适应稀疏路由生成式跨域推荐 [2608.06997, Bo Chen/Ruiming Tang/Guorui Zhou/Han Li/Xiangyu Zhao], Baidu Autonomy-of-Heads 免数据稀疏注意力 (冻结 QK 谱几何) [2608.06849, Yang/Shang/Wang/Yu], CoinRAG 上下文化 nugget KV 缓存复用 [2608.07458, Gyuwan Kim 等], CreativeInstruct UNC 质量/创造力/多样性平衡 [2608.07460, Bansal/Stengel-Eskin], MemWM LMU 记忆库条件文本世界模型 [2608.07107, SSF +206.3% vs SFT, ALFWorld/WebShop/ScienceWorld +65.4%]；WeatherNext Nature 8/6 气旋路径/强度/风结构 SOTA + 1 天预警提前量 (s41586-026-10953-2, 已开源)；导航 (已覆盖不重复): SITA 2608.03692 (08-07 ai-search) / DEGR 2608.04809 (08-06 arxiv-daily + paper-check) / Gryphon-v2 2608.06213 (08-07 arxiv-daily + ai-search) / DeepMind 组织变更 (08-06 investment-daily)；当日 arXiv 流由同日 arxiv-daily / arxiv-ai-search 覆盖
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 2026-08-08 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-08/conference-digest.md
- Contradictions: ⚠️ NeurIPS 2026 会址口径修正——08-07 digest 记 "San Jose, 12/6-12"，本期核验官方为三城 (Sydney + Atlanta + Paris)，已在本期 §2 标注以本期为准；KDD 2026 OpenReview 通告为 tentative, single-source，待后续核验；其余无（每篇 arXiv 均 grep 去重后收录）

## [2026-08-10] synthesis | wq101-alpha-daily (WorldQuant 101 Alpha 因子选股 Top 20 — 美股)
- New page: wiki/synthesis/2026-08-10/wq101-alpha-daily.md
- Data basis: 8/7 周五完整收盘（确认值）+ 8/10 周一盘前/事件窗口
- Coverage: 非农爆冷落地（-2.3 万 vs +8.3 万，9 月加息概率 ~44%）→ 标普收盘新高 7,757.64、纳指周 +5.19%；AI 交易选择性回归（SOX 周 +9%、NVDA 周 +11.6% +$562B 史上最大单周市值增幅、PLTR 周 +39.8%）；存储"利好出尽"第三日 + 底部信号（AAPL 抢购 DRAM + SK 海力士 $710 亿回报，MU V 型反转企稳）；能源地缘溢价回吐（Hormuz 总体框架，XOM/CVX 移出）；Fed 人事博弈 + 8/12 CPI 为下一"一元决定事件"；Top 20 榜单（NVDA 9.5 登顶 / SHOP 9.0 / MSFT 9.0 / PLTR 8.9 / AAPL 8.8 新入选 / LLY 8.8 / DIS 8.6 / TSM 8.4 上调 / COP 8.3 下调 / ANET 8.3 / JPM 8.3 下调 / LMT 8.1 上调 / MU 8.0 / GOOGL 8.0 回归 / AMZN 7.9 / BAC 7.9 / GS 7.9 / CAT 7.9 下调 / COHR 7.7 新入选 / AMAT 7.7 新入选）；因子主线 Alpha#41 60% + Alpha#1 45% + Alpha#19 扩展至 GOOGL；板块 Tech+Semis 11 只（55%）
- Updated: wiki/index.md (Synthesis 表新增 wq101-alpha-daily 2026-08-10 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-10/wq101-alpha-daily.md
- Contradictions: none（价格与 investment-daily 08-08/08-10 一致；Dow 54,036.93 新浪 vs 54,036.52 AP 尾数差 0.41 为来源舍入，已在报告标注；非农结果与 8/7 报告"偏鸽情境"预测一致）

## [2026-08-10] synthesis | Game RL & Game AI Bot — Daily Synthesis (2026-08-10)
- New page: wiki/synthesis/2026-08-10/game-rl-daily.md
- Coverage: 13 verified new papers (arXiv API + abs pages, Mon Aug 10, 2026 announcement batch = submissions Aug 7–9, IDs ~2608.06394–2608.07457; every ID grep-verified absent from all prior wiki digests 07-01 → 08-08 before inclusion)
- Sections: ①Game RL (3) — MDT solver-guided mixed-equilibrium reasoning (250M+ solver decisions, No-Limit Hold'em, ℓ₁ distance to equilibrium −52.6% across 8 LLM configs, CUHK-Shenzhen tentative 2608.06741), Aftab CNN-encoder + advanced value-function (Hadamax/distributional/ensemble/dueling) benchmark for PQN (Atari-57 IQM HNS 6.479, Procgen Hard OOD, Univ. Padova tentative 2608.07335), Crash-game optimal stopping-multiplier optimization balancing house vs players (2608.07103); ②Game AI Bot (2) — Deal Me Maybe prompt-conditioned emotion study of LLM negotiation (angry buyers 0.39% deal rate vs happy 28.91%, FBK tentative 2608.06922), PHASE-Tree mutable multi-timescale character-state tree for long-horizon role-play + LongEvoRoleBench (Tsinghua tentative 2608.06975); ③Game Foundation Models / World Models (3) — MemWM memory-bank-conditioned text world model (SSF +206.3% vs SFT, +65.4% relative task success ALFWorld/WebShop/ScienceWorld, LMU Munich tentative 2608.07107), Dueling World Models dueling-style action channel cancels common-mode distractors at readout (no extra losses, gridworld/Atari, 2608.06706), WorldTrace addressable KV memory for video world models + LoopBench (NVIDIA/Princeton/TU Munich, temporal consistency +15.5% / episodic recall +19.5% 2608.07408); ④Benchmarks — no new standalone benchmark paper; cross-refs (Tower of Hanoi 2608.07077 in today's arxiv-paper-check; LoopBench via WorldTrace; DungeonBench/MirrorCraft via 08-03/08-04); ⑤Industry — no new studio submissions; cross-ref NVIDIA γ-World in today's conference-digest; ⑥Related Techniques (5) — TRIAL trajectory-relative hindsight distillation (beats GRPO in 8/8 configs, WebShop +Qwen3-1.7B success 56.4→75.2%, 2608.07371), MARP multi-agent reward prediction aligning Harvest Game social dilemmas (2608.07280), closed-form partial-observability learning failure = critic bias fixable by lookahead not memory (UCL 2608.07228), mean-payoff bidding games ultimately-periodic realized play under adversarial-optimal strategies (Technion/Haifa tentative 2608.07383), PUSH staggered-horizon lifelong MAPF (10k agents <1s, higher throughput than PIBT/RHCR/TP baselines, CMU tentative 2608.06702)
- Trends: world models converge on three failure modes (long-horizon memory → WorldTrace, distractor-induced action-blindness → Dueling World Models, factual state fidelity → MemWM); solver output replaces human annotations for equilibrium reasoning in LLM game agents; emotions become a first-class, measurable agent parameter; character-state evolution becomes an explicit mutable model for RPG NPCs; MARL alignment via learned episode-level social rewards
- Updated: wiki/index.md (Synthesis 表新增 game-rl-daily 2026-08-10 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-10/game-rl-daily.md
- Contradictions: none (all claims verified against arXiv abs/API metadata; zero overlap confirmed via grep; affiliations marked tentative when inferred from co-authors)

## [2026-08-10] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-08-10)
- New page: wiki/synthesis/2026-08-10/investment-daily.md
- Coverage: 周一（8/10）盘中版——美股/中概 = 8/7（周五）完整收盘，A股 = 8/10 早盘盘中（10:32 央广网），港股 = 8/7 完整收盘 + 8/10 前瞻（盘中数据撰写时未获独立来源确认，夜期高水 122 点 + ADR +0.64% 预示偏暖开盘）。①中国 7 月 CPI/PPI（8/9）双双低于预期——CPI +0.5%（预期 ~0.7-0.9%）、PPI +3.5%（涨幅回落 0.6pct、结束持续改善高位回落）；结构性亮点 = AI 电子产品涨价（平板/计算机/手机价格同比 +17.2%/+17.4%/+8.5%，计算机通信电子制造业 PPI +4.4% 涨幅扩大）；②宇树科技今日（8/10）网上/网下申购——发行价 150.80 元、PE 219 倍、募资 ~60.99 亿，战配含 DeepSeek 93.34 万股（~1.41 亿，限售 36 个月）/腾讯旗下上海启善/社保，每经测算"中一签或赚 20 万元"；③长鑫科技今日正式纳入 MSCI 中国全股票指数（7/28 公告、8/10 生效）；④A股 8/10 早盘分化——上证 +0.28% 报 3,950.93 续创年内新高/深成指 -0.44%/创业板指 -1.02%，生物科技/电脑硬件/酒类/贵金属/CRO/创新药/PCB/工业金属领涨，煤炭/互联网/教育/种植业/水泥/保险领跌，早盘成交约 1.36 万亿；⑤美股 8/7 收官：标普创收盘新高 7,757.64、纳指周 +5.19% 为 4 月以来最强（非农 -2.3 万 → 9 月加息概率 ~44%）；⑥港股 8/7 收 +0.54% 报 25,668.03，智谱/胜宏/金斯瑞主线延续，张忆东"底部确认、8 月开启秋季行情"；⑦下周密集窗口：8/12 美国 7 月 CPI + 寒武纪业绩说明会 + Cisco，8/13 中芯 Q2 业绩，8/10-14 Llama 4/Qwen3.8-Max/Grok 4.6/DeepSeek V4-Pro 发布撞期
- Updated: wiki/index.md（Synthesis 表新增 investment-daily 2026-08-10 条目）, wiki/log.md
- New pages: wiki/synthesis/2026-08-10/investment-daily.md
- Contradictions: ⚠️ 拒收财联社"金龙指数涨超 4%/阿里+7%"头条——经核实为 2023-08-10 旧闻（cls.cn/detail/1429611，ctime 1691675951），非 2026-08-07 中概数据；8/7 US 中概确认值 = 金龙 +0.82%（一财）；⚠️ 美股 8/7 道指新浪口径 54,036.93（+151.83）vs 08-08 报告 54,036.52（+151.42），差 0.41 点为尾数舍入，已标注取新浪口径；港股 8/10 盘中数据 + 南向 8/7（2026）净额撰写时未确认（待午评/官方补齐）

## [2026-08-10] synthesis | arXiv Paper Check — AI & CTR (2026-08-10)
- New page: wiki/synthesis/2026-08-10/arxiv-paper-check.md
- Coverage: 36 papers curated from the Mon, Aug 10, 2026 arXiv announcement batch (cs.AI 88 new / cs.IR 9 new; first batch since Fri Aug 7; IDs ~2608.06394–2608.07457). ZERO overlap with Aug 7/8 digests and paper checks (verified by grep).
- Sections: ①CTR/Rec/Ads (8) — SYF agentic conversational rec [RecSys '26 Industrial, online A/B, 98.85% alignment accuracy], LP-FFT-RFT progressive foundation-model alignment [RecSys '26 Industry, RFT on dense-implicit reward], HD-Rec hierarchical quantizer + domain-adaptive sparse MoE for cross-domain GenRec [Huawei], TM20K 20K-seq e-comm ads teacher–student distillation [ByteDance, deployed, ADSS +1.036%, +5.6% latency], MISO model-internal-state ranking optimization [Meta ads, fewer validation runs], census-denominated AI venue-rec audit [85.6% of 4,776 venues never recommended; staleness not hallucination], audio-embedding Semantic-ID music rec study [codebook capacity can add instability], EAHR exact adaptive hybrid retrieval [23.4–30.3× latency cut, TREC-DL]; ②LLM Arch/Efficiency (4) — EntropyMoE entropy-routed byte-patch MoE, MAP question-contrastive middle-layer attention prediction [97.5% perf @5.56% visual tokens, 3.09×], CoCo contribution-contrast MoE reward-model interpretation, CoBa compute-balanced test-time routing [matches best-of-16 at −58.9% tokens]; ③Agentic RL & Post-Training (7) — WebGrader self-evolving programmatic grader [WebGen-Bench 52.01%], Gated-BEPO confidence-gated Bellman credit, FACTOR action-to-token credit allocation, DiDPO diff-structured coding-agent RL [>10% over baselines, open verl-code], IB-RL isolated bilateral strategic-dialogue RL, MemOPD memory-state-aligned OPD, ADIAS issue-centric agent design [+25.2%]; ④Agents & Memory (8) — WebRider intent-contract live-web agents [RiderBench 4,096 contracts; 99.2% completion vs 38.8% policy fidelity], ReASearch optimizer-as-agent [COLM 2026], MemPrism task-conditioned memory views, TEPA revocable evidence-memory [0.950 vs 0.210 LWW under reversal], Agent Memory Distillation [GPT-5-mini teacher, +27.2/+11.2/+3.4 AppWorld/BFCL V3/ToolSandbox], BONSAI evolvability-guided skill MCTS, SkillProx proximal textual gradient descent, EMAS evidence-guided MAS revision [MBPP 55.09→89.12, −62.2% tokens]; ⑤RL for Science (3) — ResidencyRL simulated clinical RL [Google, +7.0% diagnostic accuracy, −31% missed red flags, 87.6% clinician preference], Fisher-R1 + P-Bench verified-statistical-reward hypothesis-testing RL, Towers-of-Hanoi emergent-world-model study [frontier models encode but fail to use >3 rings]; ⑥Eval/Safety (5) — Divergent Response Modes [GPT-5 deflects reasoning disclosure 99% vs 0%], Winning by Peeking AutoML protocol-defect audit [win rate 59.4→34.3%], Blind to the Pivotal Vote [verification gains only on pivotal votes, +10.4–23.3 pts], Niyam-AI zk-SNARK-verifiable agent guardrails [F1 88.5%, ~53 ms verify], AI–AI interaction out-of-equilibrium dynamics
- Key cross-cutting trends: agentic/user-steerable rec reaches production (SYF/LP-FFT-RFT); long-sequence CTR efficiency via distillation (TM20K/HD-Rec); agentic RL credit assignment finer+cheaper (Gated-BEPO/FACTOR/DiDPO/MemOPD); agent memory as falsifiable engineering (TEPA/MemPrism/AMD); verifiable-execution RL spreads to web+science (WebGrader/Fisher-R1/ResidencyRL); evaluation-rigor audits multiply
- Updated: wiki/index.md (Synthesis 表新增 arxiv-paper-check 2026-08-10 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-10/arxiv-paper-check.md
- Contradictions: none (all claims verified against arXiv listing pages; zero overlap with prior digests confirmed via grep)

## [2026-08-08] synthesis | Game RL & Game AI Bot — Daily Synthesis (2026-08-08)
- New page: wiki/synthesis/2026-08-08/game-rl-daily.md
- Coverage: 8 verified new papers + 1 cross-referenced pair (arXiv abs pages, fresh window Aug 4–8, 2026, no overlap with prior dailies)
- New papers: Game RL (IFlowNets incomplete-information generative-flow strategies, NeurIPS 2025 workshop, beats OSMCCFR, 2608.05422), Game AI Bot (SyncPlan plan-execute-correct LLM coordination, <0.05% runtime, Overcooked + Honor of Kings, 2608.01652; Emotion Dynamics in Werewolf social deception EDA, 2608.04605), Game Foundation Models (MASS authoritative typed-state multiplayer world models, 1,024 players/10K steps, 0.76 vs 0.128 state recovery, 2608.06257), PCG (WorldClaw Tencent Hunyuan agentic 3D open-world generation with editable explicit assets, 2608.05248), Benchmarks (ACT-Eval tool-verified atomic-claim LLM chess commentary benchmark, GPT-5.4 22% sub-claim hallucination without tools, 2608.04240; AI World Cup 2026 completed FIFA tournament forecast benchmark, GPT-5.5 Thinking 744 pts/only model to pick Spain, 2608.03416), Related Techniques (OASE opponent-aware selective evolution, evidence-anchored skill adoption under co-evolving opponents, 2608.02005; Hybrid LLM-Augmented RL agents, 2608.03502; ADRS agentic RL self-distilled reward shaping with TVA gate, 2608.03223; AI Agent Economics executable-rights-driven emergence, 2608.03076; Computationally efficient collaborative communication via regularity-based coarsening, UC Berkeley, 2608.05327)
- Cross-referenced (already in today's arxiv-daily, not re-listed): NVIDIA VLM videogame data annotation pair 2608.05949/2608.05954 (Schmid & Frosio)
- Edge-submission note: SyncPlan (2608.01652) and OASE (2608.02005) published Aug 3, missed by the 08-04 digest (window Jul 31–Aug 3); confirmed absent from all prior dailies before inclusion
- Trends: authoritative-server design for multiplayer world models; agentic 3D world generation entering industry (Tencent); plan-execute-correct LLM coordination for games; sampling-side generative-flow advances in incomplete-information game RL; LLM evaluation extending into game commentary/tournament forecasting
- Updated: wiki/index.md (Synthesis table new game-rl-daily 2026-08-08 row), wiki/log.md
- New pages: wiki/synthesis/2026-08-08/game-rl-daily.md
- Contradictions: none

## [2026-08-08] synthesis | LLM Tech Report Digest (2026-08-08)
- New page: wiki/synthesis/2026-08-08/tech-report-digest.md
- Coverage: 各大 AI 公司最新技术报告 / System Card 汇总（2025-2026），20 个公司/实验室分节 + 交叉观察，沿用 08-07 基线结构
- 今日增量（相对 08-07）:
  - **Grok 4.6 观察日（08-07）已过，状态从"观察日"转为"窗口外溢、官方未确认"**：kie.ai 仍称 08-07 已上线（xAI API / Grok app / grok.com / SuperGrok / X Premium+）；但 xAI 官方 docs.x.ai 模型目录截至 08-08 仍仅列 grok-4.5（$2/$6，500K ctx，知识截止 2026-02-01），API release notes 无 grok-4.6 条目；Musk 07-27 "around August 7" / 07-28 1.5T V9 基座 + 大幅升级 SFT/RL，但 **08-04 SpaceX 财报电话会称"next week"（≈08-10~14）**，时间表实际后移；无官方 model card / 定价 / 上下文 / 基准；Grok 4.7（2.1T）随后数周
  - **Qwen3.8-Max 开源权重窗口今日（08-08）正式开启**：08-03 承诺"下周" = 08-08~08-14；截至搜索时 HF/ModelScope 无新权重条目，仍缺具体日期 + license + model card，对照 Kimi K3 按期放权（07-27 兑现）持续受评论界质疑
  - **Apple AFM 3 技术报告"承诺未兑现"观察**：06-08 承诺 "later this summer" 仍未发布（2025 年 AFM 2 报告 7 月发布，节奏对照）；核实五模型家族细节——AFM 3 Core（3B dense）/ Core Advanced（20B 稀疏，IFP 激活 1–4B）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像）/ AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU，NVIDIA Confidential Computing + Intel TDX + Google Titan）；与 Google 合作定制、TPU 训练；Siri AI 已进 iOS 27 消费者 beta（TechCrunch 08-03）
  - **StepFun / InternLM / Yi / Baichuan 无 8 月新报告**：StepFun 最新 = Step 3.7 Flash（05-29，198B/11B，原生多模态，256K）；InternLM 最新 = Intern-S2-Preview（07-17/18，S1-Pro arXiv:2603.25040 为 1T 级科学多模态基线）；Yi / Baichuan 无更新
  - 复核无变更：DeepSeek / OpenAI（GPT-5.7 仍未确认）/ Meta / Google DeepMind / Anthropic / Mistral / NVIDIA / Amazon / ByteDance / Zhipu（GLM-5.5 单源传闻）/ Moonshot（K3 07-27 仍最新，K4 传闻）/ Microsoft（Phi-5 无官方报告）/ MiniMax
- Key updates: 见今日重点框与交叉观察——"承诺制发布"验收：Grok 4.6 窗口外溢 + Qwen 开源窗口开启；Apple 技术报告滞后观察；8 月上旬密集发布窗口延续（GPT-5.7 传闻 / Qwen 权重 / Grok 4.7）
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 2026-08-08 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-08/tech-report-digest.md
- Contradictions: ⚠️ 时间表矛盾已标注——Musk 07-27/07-28 称 Grok 4.6 "around August 7"，但 08-04 财报电话会称"next week"（≈08-10~14），且第三方 kie.ai 宣称 08-07 已上线 vs xAI 官方目录无记录；结论为"官方未确认"（明确标注，不写入正式条目）。其余无

## [2026-08-08] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-08-08)
- New page: wiki/synthesis/2026-08-08/investment-daily.md
- Coverage: 周五（8/7）完整收盘确认版——美股/港股/A股/中概均为 2026-08-07 收盘口径。①美国 7 月非农爆冷转负（-2.3 万 vs 预期 +8 万，5/6 月合计下修 10.3 万，失业率 4.1%），9 月加息概率 ~55%→~44%，美股齐涨、S&P 500 创收盘新高 7,757.64、纳指周 +5.19%（4 月以来最强）；②A股 8/7 放量大涨（沪指 +1.02% 3,940.04 创年内新高，成交 26,834 亿放量 1,359 亿，超 2800 股上涨）——CRO/创新药爆发（百花医药 4 连板）、AI 硬件 PCB 涨停潮（高盛上修 PCB/CCL）、稀土永磁（中国稀土涨停）、黄金（金价逼近 5300）；③港股 8/7 恒指 +0.54% 收 25,668.03、恒生科技 +0.78%——智谱 +14.63%、MINIMAX-W +9.83%（DeepSeek 拟提价）、胜宏 +10.91%、金斯瑞 +16.18%（医药 BD 出海 997 亿美元）；④中概 8/7 US 时段金龙 +0.82%（确认值，BABA +1.26%、NIO +3.04%）；⑤AI 主题：SpaceX 解禁日 +15.83%（年底 ARR 冲击 $100B、NVIDIA 独供背书）、PLTR +10.31%、OpenAI 暂停 Astra、SK 海力士拟投 383 亿美元扩产、FCC 拟禁中国光收发器（COHR +13%）、寒武纪"最强中报"（H1 营收 59.96 亿 +108%、归母净利 23.11 亿 +122.6%）、宇树科技 8/10 申购（战配 DeepSeek/腾讯/社保）、特朗普对多晶硅加征 15% 关税；⑥策略：非农偏鸽利好长久期 AI 股但 8/12 美国 CPI（预期 3.4%）为下一验证点；A 股主线 = CRO/医药 BD + AI 硬件 + 稀土 + 国产算力；港股 ADR +0.64% 预示周一偏暖；中芯 8/13 Q2 业绩 + 8 月中旬财报季为港股关键催化
- Updated: wiki/index.md（Synthesis 表新增 investment-daily 2026-08-08 条目）, wiki/log.md
- New pages: wiki/synthesis/2026-08-08/investment-daily.md
- Contradictions: ⚠️ 重要口径校准——investment-daily 08-07 的 A股/港股 8/7 数字混入 2025 年同期数据（A股"1.83 万亿成交/医药续跌"实为 2025-08-07 口径，2026 实为沪指 +1.02% 3,940.04/成交 26,834 亿/CRO 爆发；港股"25,081.63/+0.69%"实为 2025，2026 为 25,668.03/+0.54%；"南向 6.61 亿/小米 17.22 亿"亦为 2025-08-07 数据），本报告已校准并注明 2026 南向 8/7 净额待官方确认（最近确认值 8/6 净买 94.85 亿）；中概 8/6 时段明细经 8/7 US 时段数据覆盖（金龙 +0.82%），36氪 8/6 flash 不再采信

## [2026-08-07] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-08-07)
- New page: wiki/synthesis/2026-08-07/wq101-alpha-daily.md
- Coverage: 数据基准 8/6 收盘 + 8/7 盘前/非农事件窗口（周五版，事件周"硬门槛"兑现日），基于 WorldQuant 101 Alpha 因子框架对美股 Top 20 打分
- 8/7 增量（相对 8/6 报告）: ①指数回落——8/6 Dow 53,885.10 (-0.85%, -464 点, 止步五连涨) / S&P 7,709.96 (-0.18%) / Nasdaq 26,348.35 (-0.06%), 8/11 板块 8 跌, 工业/房地产/材料领跌, 油价反弹 (伊朗-阿曼 Hormuz 草案拟禁美以船只 + 收费补偿) 引发 9 月加息担忧; ②存储"利好出尽"第二日——SNDK -6.8% / WDC -13% (指引后连续两日回吐), 但 MU 盘中 -5.6% (低 $827) 后 V 型收复至 $881.47 = Alpha#53 反转存储链唯一存活; ③COP 财报 beat + 回购翻倍 = 能源回归——Q2 调整后 EPS $3.24 (vs $2.88, +12.5%) / 营收 $19.52B (+32.4%) / 回购翻倍至 $20 亿 / 总股东回报 $30 亿 (45% CFO 回报目标) / $0.84 股息 / Permian 纪录 (2,248 MBOED) / Kirkuk 42% JV / LNG 12 MTPA, 区间 $116.20-119.11, 共识 25 分析师 Buy 均目标 ~$141; XOM +2.12% / CVX +1.51% 同日走强 (7 月板块 +10.8% 趋势延续); ④兑现者动量维持——SHOP +2.22% 连续第三日 (AI 渠道流量同比三倍, 75% AI 订单来自非头部品类) / DIS +2.87% 连续第三日 ($9B 回购扩大) / MSFT +2.54% 逼近 $500; ⑤金融高位小幅回吐——GS -2.62% / JPM -0.82% / BAC -0.40%, XLF 7/28 历史新高后非农前观望; ⑥8/6 盘后/8/7 盘前——ABNB +8% / NET +16% (财报后大涨) / DKNG -3% (营收 miss), SpaceX 解禁日 +6.1% ($1,010 亿解禁落地不跌反涨); 今日 ET 8:30 美国 7 月非农 (共识 +8 万, WSJ +8.3 万 vs 6 月 +5.7 万 / 失业率 4.2% / AHE +0.3% +3.5%, ADP +4.4 万 vs 7.5 万偏弱, ISM 服务业就业 47.4 收缩区; 9 月加息定价 ~57-65%, ADP 后回落至 ~57%) 为"一元决定事件", 全部评分含非农前置信度折价
- Key signals: SHOP(9.2, 登顶, 三连阳 + AI GMV 三倍); MSFT(9.1, 逆势领涨避险 + 云 AI 基准); COP(9.0, 新入选, "超当期+上调回报"型兑现 = 能源基本面锚); LLY(8.9, 医疗少数收涨板块); DIS(8.8, 三连阳反转修复); NVDA(8.7, 平台整固, 8/26 财报锚); XOM(8.6, 回归, 收于日内高点); JPM(8.5, 非农为加息路径验证按钮); ANET(8.4, 超买回吐); CVX(8.4, 回归); PLTR(8.3, 超买回吐); BAC(8.2); MU(8.1, 上调 7.7→8.1, 盘中 V 型反转); CAT(8.1); AMZN(8.0, Bezos 减持悬顶维持); GS(8.0, -2.62% 事件性回吐); MPWR(7.9); TSM(7.8); VRT(7.8); LMT(7.6); 移出: AVGO/LRCX/MRVL/RTX/GOOGL (无催化/存储链情绪传导/组织风险两日 -5.3%)
- Factor mix: Alpha#41 趋势(12 次/60%, 从 45% 升至最高频——能源反弹收高 + 兑现者动量 + 平台整固)+Alpha#1 动量(8 次/40%, 收敛为 SHOP/MSFT/COP 三主线)+Alpha#6 量价(7 次/35%)+Alpha#30 波动率(5 次/25%)+Alpha#53 反转(3 次/15%, 集中在 MU 存储链唯一存活)+Alpha#19 均值(3 次/15%, MU/GS)+Alpha#12 背离(2 次/10%, AMZN)
- Sector mix: Tech/Software 5 只(25%)+Semis 4 只(20%, 从 30% 续降配——移除 AVGO/LRCX/MRVL)+Financials 3 只(15%)+Energy 3 只(15%, 0→3 新回归)+Cons Disc 2 只(10%)+Healthcare 1 只(5%)+Industrials 1 只(5%)+Defense 1 只(5%, 移除 RTX)
- Top 5: SHOP(9.2)/MSFT(9.1)/COP(9.0)/LLY(8.9)/DIS(8.8)
- Strategy: 今日非农为"验证按钮"——偏强→9 月加息 ~65% 强化利好金融/能源 (NIM/交易弹性) 利空高估值 AI 成长, 偏弱→相反 (金融最敏感暴露); "确认非催化"升级为连续模式 ("确认非催化 2.0", SNDK/WDC 两日回吐) 确认只有"超当期 + 上调远期指引/回购/分红" (LLY/ANET/SHOP/COP 类型) 才配动量溢价; MU 独立 V 型反转 = 当前唯一"资金用脚投票"例外, 重点跟踪; 能源地缘溢价 (Hormuz) 回吐速度极快 (8/3 WTI -6% 先例); 候补: GOOGL/AVGO/LRCX/MRVL/RTX/AMD/SNDK/WDC/ABNB/NET/SPCX/META/NVO
- Updated: wiki/index.md (Synthesis 表新增 wq101-alpha-daily 2026-08-07 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-07/wq101-alpha-daily.md
- Contradictions: ⚠️ 口径勘误——investment-daily 08-06 曾将 8/4 收盘 (Dow +1.71% 54,085) 误标为 8/5, 已在 investment-daily 08-07 修正; 本报告 8/6 指数采用 AP 口径 (S&P 7,709.96) 与 investment-daily 08-07 的 7,710.02 存在 0.06 点尾差 (来源舍入), 不构成实质分歧; 其余无 (COP 财报"beat + 回购翻倍 + 股价走强" vs SNDK/WDC"业绩暴增 + 两日回吐"形成鲜明镜像但非数据冲突)

## [2026-08-07] synthesis | arXiv AI Research Search (2026-08-07)
- New page: wiki/synthesis/2026-08-07/arxiv-ai-search.md
- Coverage: 17 curated papers from the Aug 5–6, 2026 arXiv new-submission window (IDs ~2608.05150–2608.06380), scanned across cs.AI / cs.LG / cs.IR / cs.CL / cs.GT / econ.TH / cs.DB. 9 already covered by the 08-05/06/07 digests (included with full detail + coverage pointer for a self-contained report); 8 NEW (grep-verified no prior wiki coverage): LC-GRPO Langevin-corrected flow GRPO for diffusion LLM RL [2608.05600, Mengdi Wang = Princeton, tentative], Reasoning Errors in Residual-Stream Trajectory [2608.05660, Univ. of Adelaide], LLM-OSDA ad auctions in LLM conversations [2608.00123, ByteDance/TikTok, tentative], Beyond PPAD Hardness of Auto-bidding [2608.01889, U Washington], AV-AIVAT anytime-valid multi-armed bandit for agent evaluation [2608.06362], Auction-Learned bidding-strategy learner [2608.04455], LLM-OTW one-turn Othello-OpenAI wrapper [2608.05742], Synthetic-Data-Rec synthetic data for LLM rec [2608.01193]
- Sections: ①LLM RL & Diffusion RL (LC-GRPO + DASH-family context), ②Recommendation (Gryphon-v2/OMEGA/SITA/ATLAS/LIME-Rec/Synthetic-Data-Rec), ③Advertising & Auctions (DEGR/LLM-OSDA/Beyond-PPAD/Auction-Learned/AV-AIVAT), ④Sequential/Reasoning/Interpretability (RRC/Residual-Stream Errors), ⑤Games (LLM-OTW)
- Key cross-cutting trends: RL supervision becomes divergence/price-adaptive; generative recommender ranking escapes fixed-supply ceilings; ad auctions move into LLM conversation surfaces + tighter compute-theoretic limits on auto-bidding; anytime-valid statistics meet multi-armed agent evaluation; synthetic data retrofitting LLM rec
- Updated: wiki/index.md (Synthesis 表新增 arxiv-ai-search 2026-08-07 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-07/arxiv-ai-search.md
- Contradictions: none (all claims verified against arXiv listing/abs pages; arXiv export API intermittently rate-limited HTTP 503/429 so metadata came from listing + abs pages; institution attributions marked tentative when inferred from co-authors)

## [2026-08-07] synthesis | arXiv Daily Digest (2026-08-07)
- New page: wiki/synthesis/2026-08-07/arxiv-daily.md
- Coverage: 26 papers curated from the Fri Aug 7, 2026 arXiv batch (new submissions ~2608.05150–2608.06380, submitted Aug 5–6; stream sizes cs.AI 201 / cs.CL 94 / cs.LG 162 / cs.IR 15 / stat.ML 22 new, per listing-page headers). NO overlap with Aug 4/5/6 digests, paper checks, or AI scans. No dedicated advertising/CTR paper surfaced in today's cs.IR stream (noted in the report); industrial rec coverage via Yandex Music.
- Sections: ①Recommendation/Ranking/Retrieval (Gryphon-v2 single generate-and-rank model replaces 15+ generator cascade at Yandex Music, online A/B +1.41% active users, Rollout Distillation from training-only Teacher Ranker; Modality Weighting Audit shows per-user weighting adds no consistent utility over a single global weight, real-GM + real-shuf as minimum evidentiary standard; Popularity Calibration user study — users perceive but don't prefer calibrated lists, JSD reliability conditional on familiarity/history; READ deterministic MCP-exposed agentic ops beat embeddings 58.8% vs 15.7% on 780-page table-heavy financial report, BM25 indistinguishable → gain is interface not iteration; EXCISE query-side-only exclusion fixes late-interaction "exclusion inversion", success@10 0.058→0.691; Gender Sensitivity mechanistic localization of bi-encoder bias to embeddings + small late-layer head set, Brown/UvA), ②LLM Reasoning/RL/Post-training (DASH divergence-adaptive supervision horizons make OPSD token-weights history-aware, no extra forward pass, CAS; AgentOPSD Bayesian recursive turn-level credit in log-odds space, critic-free, 89.1% ALFWorld Qwen2.5-7B; RRC ranking-based reward construction unlocks generative reward models for RL via self-competitive + anchor-guided ranking, NEU; Refining Over Resampling verifier-free breadth-depth self-critique + majority vote, beats verifier-based best-of-N, 58.0% MATH500; Position: Optimize LLMs for Self-Consistency ICML 2026 position paper, MIT; EnvACE world rehearsal replaces external environments in agent RL, internalized agent world model, SJTU/Huawei), ③Sequential/Arch/Efficiency (Answer First, Reason Later: diffusion LLM reasoning failure is commitment-order pathology not belief — frontier-gated commitment recovers 0.528→0.852 with 4× parallelism, SNU; HiLP hierarchical latent prediction reduces compounding rollout error, MSR; SiPE syntax-informed PEs −9% PPL +10.3% SyntaxGym +8.2% GLUE, single-parse; MACRO Markov chain layer routing +5.0% avg, train-free, 9.4× less route-search vs Dr. LLM; QEvict 3-tier recoverable quantized KV eviction with attention-driven promotion), ④Agents/Skills/Personalization (TRAJDEBUG error-lifecycle tracing + TrajErrBench 486 failed trajectories, Tsinghua; LUNAR cross-domain behavioral personalization benchmark, 19 LLMs — behavior logs necessary-not-sufficient, retrieval > compressed memory; Cautious Context Steering per-token learned context control without per-user tuning or 2nd forward pass, Yonsei; Search2Skill rubric-RL skill distillation beyond parametric knowledge boundary, Alibaba/BIT), ⑤Games/World Models (GAUGE 22-task real-world-grounded physical-fidelity benchmark — no uniformly faithful engine, world models produce equation-form-but-wrong-dynamics; AV-AIVAT anytime-valid early stopping 74× cheaper HUNL agent evaluation with exact EB-CS certification; IFlowNets proves GFlowNet flow constraints inadmissible under incomplete information, Georgia Tech; Otter 15.3M-param history+clock human chess beats Maia 2)
- Key cross-cutting trends: verifiable/agentic RL supervision converges on dense distribution-shaped credit (DASH/AgentOPSD/EnvACE/RRC); recommender personalization claims get audited empirically while Gryphon-v2 kills a cascade; retrieval becomes mechanism/interface-first (EXCISE/READ/mechanistic gender bias); diffusion LLM reasoning reframed as commitment-order problem; efficiency adds recoverability (QEvict) and adaptability (MACRO); world models get physical-fidelity diagnostics (GAUGE); games remain rigorous eval/algorithm testbed (AV-AIVAT/IFlowNets/Otter)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-07 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-07/arxiv-daily.md
- Contradictions: none (all claims verified against arXiv listing/abs pages; arXiv API intermittently rate-limited HTTP 503/429 so metadata came from listing + abs pages; stream counts match listing-page headers; no overlap with Aug 6 digest/paper-check/AI-scan windows)

## [2026-08-06] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-08-06)
- New page: wiki/synthesis/2026-08-06/wq101-alpha-daily.md
- Coverage: 数据基准 8/5 收盘 + 8/6 盘前/事件窗口（周四版，事件周第四波），基于 WorldQuant 101 Alpha 因子框架对美股 Top 20 打分
- 8/6 增量（相对 8/5 报告）: ①指数分化——8/5 Dow 54,503.12 (+0.77%) 连续第三日历史收盘新高, 但 S&P 7,730.65 (-0.08%) 与 Nasdaq 26,472.87 (-0.42%) 自盘中纪录高点回落 (Russell 2000 早盘 +1.85%); ②存储验证日落地 = 利好兑现——SNDK Q4 营收 $8.97B (+372%)/EPS $39.25/毛利率 84.6% 均创单季新高 (数据中心 $2.98B 环比 +103%/同比 +1298%), 但 Q1 FY27 指引 $10.3-10.8B 低于预期 ~5.5% + 毛利率指引 83-85% 环比持平 (市场眼中的见顶), 8/5 收跌 5%+ 后盘后再跌 8%; WDC 指引全面超预期仍盘后 -10~12%; 今晨 SK 海力士 -8%/三星 -5%/铠侠 -10%——存储定价从"涨价斜率"切换至"订单/产能兑现", 与 8/5 报告预判完全吻合; ③"确认非催化"三连击完成 (AMD -9.2% → SNDK/WDC), 反转因子系统性失效; ④财报兑现者接力——LLY +4.2% (Q2 营收 $23.0B +48%/Mounjaro +91% $9.9B/Zepbound $4.9B/上调 2026 指引至 $85-87B), ANET +13.3% (首次 $3B 季度 $3.036B +37.7%/FY26 上调至 $12.6B +40%), SHOP +18% (营收 +34% $3.58B/GMV +32% $115.57B/FCF $654M 18% 利润率/Q3 指引低 30s% 远超 26.3% 预期), DIS +4.5% (Q3 利润超预期 + Toy Story 5 拉动流媒体/商品/乐园); ⑤GOOGL -~4% (Hassabis 卸任 DeepMind CEO 转任董事长兼 Alphabet 首席科学家/Jeff Dean 离职创办 Discovery Loop 获 Alphabet 资金算力/Koray 接任/Gemini 3.5 Pro 推迟)——AI 组织风险首次冲击谷歌叙事; ⑥NVDA +3.4% 收 $219.22 (市值 $5.51T, 逼近 52 周高 $236.54)——SpaceX 确认 AI 基建只用 NVIDIA (Musk: Vera Rubin "undisputed best"), 供给稀缺叙事强化登顶; ⑦宏观——黄金 +3% 现货 $4,199.78/期货 $4,260.80, WTI +0.45% $76.11 (胡塞袭击沙特 Yanbu 油轮), 财政部宣布"至少未来数季"维持发债规模稳定, 10Y 回落, VIX ~15-16
- Key signals: NVDA(9.4, 登顶, SpaceX 独家 + Alpha#1/#41 双共振); MSFT(9.2, 云兑现基准锚); LLY(9.1, 最大上调 7.8→9.1, "超当期+上调远期"标准兑现者); ANET(8.9, 新入选, 首次 $3B 季度 + 上调指引, AI Fabrics ≥$3.5B/营业利润率 ~49.9%); SHOP(8.8, 新入选, AI 电商 + FCF 利润率 18%); JPM(8.8, XLF 新高区域整固, 8/7 非农为下一个加息路径催化); PLTR(8.7, 下调 9.1→8.7, +30% 后超买+动量边际衰减); AVGO(8.5, Alpha#12 防 AMD 式传染); TSM(8.4, N3 受限稀缺); BAC(8.4); GS(8.3); CAT(8.3); DIS(8.3, 新入选, -12% YTD 深调后反转, Alpha#53 唯一存留); LMT(8.2); RTX(8.2); AMZN(8.2, 下调 9.0→8.2, Bezos 减持悬顶 + 无新增催化); LRCX(8.1, 下调, 存储链情绪传导); MRVL(7.8); MU(7.7, 下调 8.2→7.7, 验证日回吐, 基本面未逆转但情绪出清未完); GOOGL(7.5, 最大下调 8.9→7.5, 组织风险非基本面)
- Factor mix: Alpha#1 动量(11 次/55%, 从 40% 重回绝对主导——兑现者驱动)+Alpha#41 趋势(9 次/45%)+Alpha#6 量价(8 次/40%)+Alpha#30 波动率(5 次/25%)+Alpha#53 反转(3 次/15%, 从 30% 系统性退潮——"确认非催化"三连击使反转因子在高动量标的上失效)+Alpha#19 均值(2 次/10%, 仅 GOOGL/MU)+Alpha#12 背离(2 次/10%, AMZN/AVGO)
- Sector mix: Semis 6 只(30%, 从 45% 降配——硬件广度→稀缺精选)+Tech/Software/SaaS 5 只(25%, ANET/SHOP 软件兑现轮动)+Financials 3 只(15%)+Defense 2 只(10%)+Cons Disc 2 只(10%, +DIS)+Healthcare 1 只(5%, LLY)+Industrials 1 只(5%)
- Top 5: NVDA(9.4)/MSFT(9.2)/LLY(9.1)/ANET(8.9)/SHOP(8.8)
- Strategy: 只对"超当期+上调远期"的兑现者 (LLY/ANET/SHOP/DIS) 给动量溢价; 半导体从 45% 广度配置转向 30% 稀缺精选 (移除 AMD/SNDK/INTC); 软件/消费兑现轮动 (新入选 ANET/SHOP/DIS); 金融 15% 维持 (非农前加息交易敏感); GOOGL 大下调 (组织风险); 存储链 MU 保留但 Alpha#53 反转需等放量止跌; 候补: AMD/SNDK/WDC/SPCX(解禁)/INTC/CRL/UBER/META/AXP/NVO/CVX/XOM
- Updated: wiki/index.md (Synthesis 表新增 wq101-alpha-daily 2026-08-06 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-06/wq101-alpha-daily.md
- Contradictions: ⚠️ 发现 investment-daily 08-06 指数数据口径错误——其"美股 8/5 三大指数齐创收盘新高(道指 +1.71% 54,085/标普 +1.79% 7,736/纳指 +2.59% 26,584)"实为 8/4 收盘值 (8/5 实际为 Dow 54,503.12 +0.77% 创新高而 S&P -0.08%/Nasdaq -0.42% 回落), 已在 wq101-alpha-daily 08-06 报告顶部标注勘误并建议 investment-daily 更正; 其余无 (SNDK/WDC"业绩暴增+盘后大跌"与"确认非催化"模式一致)

## [2026-08-06] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-08-06)
- New page: wiki/synthesis/2026-08-06/investment-daily.md
- Coverage: 周四版·事件周第四波(验证日)。数据口径: 美股 8/5 收盘+8/5 盘后(北京 8/6 凌晨), 港股/A股 8/5 收盘 + 8/6 早盘/午前(约 10:30-10:40)
- ①美股 8/5: 三大指数齐创收盘新高——道指 +1.71% 报 54,085(首破 5.4 万,连续两日)/标普 +1.79% 报 7,736(首破 7,700)/纳指 +2.59% 报 26,584; 驱动=Caterpillar/Palantir 业绩理想 + 霍尔木兹和谈油价急回(能源落伍)
- ②存储"验证日"落地(今日核心): 闪迪 Q4 FY26 营收 89.7 亿美元(+372%,超预期 83.9 亿)/调整后 EPS 39.25 美元(去年同期 0.29 的 135 倍)/调整后毛利率 84.6%(预期 81.5%)均创单季新高, 数据中心收入 29.8 亿(环比+103%/同比+1298%)、Edge 54.3 亿(环比+48%)、Consumer 5.56 亿(环比-32%); 但 Q1 FY27 指引营收 103-108 亿(低于预期 111.6 亿近 5.5%)、EPS 44-46 美元(低于预期)、毛利率 83-85%(环比持平,见顶迹象); 新增 140 亿回购(总授权 155 亿); 8/5 收跌超 5% 后盘后再跌 8%; 西部数据指引全面超预期但盘后跌超 10%; 两股较 6 月高点跌约 40% 已先行回调(YTD 分别 +468%/+200%+,标普仅 +13%)
- ③8/6 存储链传导: 韩日存储大跌(SK 海力士 -8%/三星 -5%/铠侠 -10%), 港股南方东英 SK 海力士 ETF 低开 -15%, A/H 存储链补跌; 机构口径: 中信建投"非需求逆转,是涨价斜率与高利润率持续性风险重定价,2026 下半年价格仍有支撑/涨价斜率放缓/扩产逐步推进,定价权重从价格弹性转向订单/产能兑现"; 基本面证据仍硬(2027 三大原厂 DRAM/HBM 产能提前售罄 + HBF 标准发布谷歌/Tenstorrent 加入 + HBM 晶圆占比 2027~30%)
- ④SpaceX 解禁执行日(8/6): 9.115 亿股 ~$1,140 亿(美国史上最大单股解禁); Q2 营收 $78B(+92%), Q2 Capex $18.4B(~6 倍,95%+ AI), 2026 全年 Capex 指引 $100B+; 8/5 股价 -13%; 马斯克"未来 AI 基建只用 NVIDIA 芯片"(压制 AMD)
- ⑤谷歌 AI 重组: Jeff Dean 离职创办 Discovery Loop(Alphabet 资金+算力)/Hassabis 卸任 DeepMind CEO 转任董事长兼 Alphabet 首席科学家/Koray Kavukcuoglu 接任; Gemini 3.5 Pro 推迟; GOOGL -~4%
- ⑥Meta Muse Code: 首个 AI 编程智能体, 贡献者档每百万输出 token 仅 $0.20(低价策略); 苹果: 宣布新增 $1,000 亿美国制造投资
- ⑦港股: 8/5 收盘恒指 +0.24%(25,915.32)/恒生科技 +0.97%(PCB 胜宏 +16%/黄金中国黄金国际 +13%/三桶油跌/南向净卖 13.98 亿); 8/6 低开 -0.96% 报 25,667.14/恒生科技 -0.99%(科网普跌联想百度哔哩 -2%/黄金股逆势涨赤峰 +9%/建滔积层板 -4%/存储 ETF -15%); 南向早盘净买 94.85 亿港元(腾讯 15.18/阿里 8.76/中芯 6.11); 夜期 25,674 低水 242 点; MiniMax 今日纳入港股通生效 + H3 开源 Day0 适配 + 无问芯穹战略合作
- ⑧A股: 8/5 放量收涨(沪指 +1.47% 3,878.43/深成指 +1.86% 14,144.20/创业板 +1.32% 3,535.14, 成交 2.66 万亿放量 4,460 亿, 存储芯片/MLCC/玻纤领涨, 中际旭创收跌逾 7% 但成交 675 亿创 A 股个股历史纪录, 新易盛 -5%/天孚 +2.29%); 8/6 早盘半导体材料设备逆势走强(科创板主题指数 +2.09%, 中巨芯 +15.30%/欧莱新材 +11.77%/有研硅 +10.80%)而存储链补跌; 《集成电路布图设计保护条例》修订(10/15 施行)
- ⑨光模块禁令进展: 中国使馆"采取一切必要措施回应" + 商务部将美国 Compliance Testing LLC 列入反制清单 + "易中天"集体回应未收到限制性文件; FCC Cover List(7/28)未列中国光模块; 高盛/花旗看好龙头; 9 月底高层会晤为关键催化
- ⑩中概 8/5 US 时段: 金龙指数 +0.93%(阿里 +3%/蔚来 +2%/拼多多 +1%/理想 -5.43%); 宇树科技 8/6 定价(T-2)→8/7 路演→8/10 申购
- 宏观: 明日 8/7 美国 7 月非农(预期新增 8.5-9 万 vs 6 月 5.7 万, 失业率 4.3%; Fed 9 月加息概率 ~65%; 30Y 曾触 5.24-5.27%; Kalshi/Polymarket 押注 7 万区间; BNY 盈亏平衡就业 ~5 万/月)
- Key trends: 存储交易范式切换("涨价斜率"→"订单兑现"); "确认非催化"模式扩散(SNDK/WDC 接棒 AMD/SPCX——高动量标的财报利好即兑现); 美股 AI 组织/产品节奏不确定性(谷歌重组/Gemini 推迟)与政策红利(苹果千亿美国制造)并行; 南向逆势扫货=港股 AI 应用主线(阿里 Qwen/MiniMax/智谱)资金面支撑; A股半导体设备材料独立于美韩存储股价
- Updated: wiki/index.md (Synthesis 表新增 investment-daily 08-06 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-06/investment-daily.md
- Contradictions: none (SNDK 财报"业绩暴增+盘后大跌"与"确认非催化"模式一致; A股 8/6 存储承压 vs 半导体材料设备走强为结构性分化非数据冲突; 恒指 8/5 收盘 25,915.32 由 8/6 开盘 -0.96% 反推校验一致)

## [2026-08-06] synthesis | LLM Tech Report Digest (2026-08-06)
- New page: wiki/synthesis/2026-08-06/tech-report-digest.md
- Coverage: 继承 08-05 全部 20 节条目，今日新增/复核——
- ① Qwen3.8-Max 开源窗口状态更新 (08-03 阿里云官方博客 "A New Bar for Coding and Cowork" 确认; 权重"下周"→预计 08-10 前后放 HF/ModelScope, 仍缺具体日期/license/model card; 对照 Moonshot K3 07-27 按期放权, "承诺+日期+license"成 2T+ 开源旗舰竞争标准)
- ② xAI Grok 4.6 发布倒计时 (Economic Times 07-29 复核 Musk 口径: 明日 08-07, 1.5T V9 基座, 大幅升级 SFT/RL; Grok 4.7 2.1T 随后数周; 仍为预告, 08-07 为观察日)
- ③ OpenAI GPT-5.7 泄漏复核 (WinCentral 07-30: 8 月发布, 新 pretraining foundation ~10T tokens, 更强推理/agent 能力; GPT-6 推迟至 9 月; Astra 代号命名未定; 未获官方确认)
- ④ Apple Siri AI 进入 iOS 27 消费者测试版 (TechCrunch 08-03 "Apple finally fixed Siri", beta 自 07 月起; Apple Foundation Models 经 Google Gemini 合作训练, 与 AFM 3 发布口径一致; AFM 3 正式技术报告仍待发布)
- ⑤ Moonshot Kimi K4 训练传闻 (AI Weekly 07-28: 寻求更多 Blackwell 芯片, 训练阶段未发布, 不入正式条目; K3 技术报告 07-27 仍为最新)
- ⑥ Microsoft Phi-5 状态更新 (仍无官方技术报告, 唯一新增为 Inference Index 目录条目 2026-01-08/128K ctx, 非官方报告不写入正式条目)
- ⑦ NVIDIA Nemotron 3 Ultra 技术报告复核 (06-09, 550B/55B Hybrid Mamba-Attention MoE, 20T tokens, 1M ctx, LatentMoE+MTP+NVFP4 预训练+多环境 RLVR+MOPD, ~6× 推理吞吐; 家族 Nano/Super/Ultra 齐备, 无变更)
- ⑧ Mistral Shieldstral 复核 (08-04 公告/arXiv 07-28: 3B 多模态安全分类器, policy-adaptive QA, Apache-2.0, 12 语言, 单 16GB GPU, Open Secure AI Alliance) 与 Intern-S2-Preview 35B HF 复核, 均无变更
- 核实无更新: DeepSeek (V4-Flash-0731 保留, 无 8 月新报告), Meta (无 Llama 新报告, Muse Spark 为当前主线), Google (最新卡 Gemini 3.6 Flash 07-21), Anthropic (Opus 5 System Card 07-24), Amazon (BI 07-28 Nova 收缩+FMR 确认), ByteDance (Seed2.1 06-23), Zhipu (GLM-5.5 仍为 JPMorgan 8 月预测), StepFun (Step 3.7 Flash 官网现列), Baichuan/Yi/MiniMax (无新)
- Key trends: Qwen 开源窗口=本周最大观察点; 8 月上旬密集发布窗口 (Grok 4.6 明日 + GPT-5.7 传闻); 开放权重=前沿扩散主通道且"承诺兑现"成竞争维度; Nemotron 3 家族技术报告齐备对抗开源 2T+ 阵营; 安全报告行业共同语言化
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 08-06 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-06/tech-report-digest.md
- Contradictions: none (继承条目显式标注"保留"; 新增均标注复核来源; 传闻统一标 ⚠️ 未确认不入正式条目)

## [2026-08-06] synthesis | arXiv Daily Digest (2026-08-06)
- New page: wiki/synthesis/2026-08-06/arxiv-daily.md
- Coverage: 24 papers curated from the Thu Aug 6, 2026 arXiv batch (new submissions ~2608.04012–2608.05148, submitted Aug 4–5; stream sizes cs.AI 41 / cs.CL 72 / cs.LG 96 / cs.IR 8 new, per listing-page headers). NO overlap with Aug 4/5 digests (TurnSight 2608.04007 & WorldCup Arena 2608.04008 at this window's boundary were already covered in the Aug 5 digest). ~12 papers overlap the same-day arXiv Paper Check 2026-08-06 (cs.AI/cs.IR streams) — cross-referenced, not duplicated in coverage.
- Sections: ①Agent Memory (ScrubJay-MEM type-conditioned perishability + TGT/GenGap benchmark, BITS Pilani; MemoryCPT end-to-end trainable cost-aware pipeline with QPC metric, HKUST), ②Agent Skills (Capability Pages cluster-contrastive offline library rewrite +2.94 R@10, RPI/Tencent; SkillSV structure-aware Shapley skill-unit valuation; Skill²-Bench skill-entropy benchmark + skill-sequence-alignment RL, Princeton/PKU), ③LLM Reasoning & RL Post-Training (ABSeeker answer-backtracked step-level credit, SJTU; OCSD observation-calibrated self-distillation, Meituan; SpecRoll fast-slow verifier-feedback speculative RL rollouts 1.21–2.04×; Reasoning Core 50-procedural-generator library, Inria), ④Eval/Safety/Trust (IRT for AI Safety 8 benchmarks×192 models, 3 factors, 97–99% eval-cost cut; Mind the Cap output-budget regime artifact; confidence-sparsity AUARC stepwise-interpolation standardization; Social Pressure breaks majority-voting safety panels; MirageBench personalization over-inference + self-monitoring inversion), ⑤Efficiency (NOVA-KV attention-preserving KV transform coding, USC; BinaryPC training-free hashing attention 3.56×, ICML 2026; MESH hidden-momentum Sinkhorn MoE optimizer −62.5% state), ⑥Rec/Ads/Live-Streaming (DEGR exploration-driven generative reranking +1.22% UCTR, JD, KDD'26 ADS; GOAL constraint-generalizing generative incentives SCPO; live-streaming multi-objective fresh+delayed ranking +0.09% DAV, Amazon, RecSys'26; Price of Isolation heavy-tail law for two-sided A/B isolation cost), ⑦Agent Infra & Simulation (MatrAIx 8.3B-persona simulated users; Azure agentic-workflow architecture + Agora prototype, Microsoft; A/B Agent hierarchical Tree-RAG self-evolution +4.829% GMV)
- Key cross-cutting trends: agent memory becomes engineered (decay curves, cost budgets, faithfulness audits); the agent skill layer matures into a full lifecycle (retrieval/valuation/training/data); RL credit assignment gets finer and cheaper (step-level, observation-calibrated, speculative rollouts); evaluation defends against confounded metrics (IRT, output-cap control, AUARC interpolation, shared-context panel failure); serving efficiency targets fundamentals (KV transform coding, training-free hashing attention, MoE optimizer memory); industrial rec/ads adds new control surfaces (exploration value, global-constraint incentives, delayed signals, isolation cost); agent-scale infrastructure & simulation arrive (8.3B personas, agentic-server design, closed-loop A/B agent)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-06 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-06/arxiv-daily.md
- Contradictions: none (all claims verified against arXiv listing/abs pages; the arXiv API returned HTTP 429 during curation so metadata came from listing + abs pages; stream counts match listing-page headers, which differ from the paper-check's cs.AI 176/cs.IR 12 figures because the latter includes cross-listed entries)

## [2026-08-06] synthesis | arXiv Paper Check — AI & CTR (2026-08-06)
- New page: wiki/synthesis/2026-08-06/arxiv-paper-check.md
- Coverage: 27 papers curated from the Thu, Aug 6, 2026 arXiv announcement batch (cs.AI 176 new / cs.IR 12 new, verified via arXiv listing pages; NO overlap with Aug 4/5 paper checks or daily digests)
- Sections: ①CTR/Rec/Ads (7) — Multi-Objective Ranking for Live-Streaming [RecSys 2026 Industry, delayed-window feedback + fresh/delayed multi-model + segment-aware targeting + MMoE], DEGR [KDD 2026 ADS, dual exploration-driven generative re-ranking with exploratory reward model, escapes fixed-supply ceiling], GOAL [generative optimization for incentivized ads under global constraints, hierarchical causal state encoder], Price of Isolation [two-sided A/B isolation extreme-value tail-class dichotomy: light tails loss vanishes, heavy tails size-independent constant], A/B Agent [self-evolving agent for industrial A/B strategy iteration, hierarchical experiment knowledge], Compass [UIST 2026, in-situ feed reflection aligning stated vs behavioral preferences], WatchLens [RecSys 2026, configurable online video-rec experiment platform, policy+position-attached logging]
- ②LLM Reasoning & RL Post-Training (6) — Argus [persistent role-owned-review agentic runtime, Manager/Planner/Engineer/Reviewer over durable project state, 7 GPT-5.5 arenas], ABSeeker [Answer-Backtracked Credit Assignment, dense step-level supervision rewarding useful actions in failed trajectories], WorldCycle [reversible action cycles give annotation-free long-horizon verification for video world-model RL], Fewer Tokens-Smaller-Cache [reward-coordinated reasoning compression, KV tolerance tracks process reward], SPOT [sparse probing + outcome-calibrated targets for OPD], Agentic RL Observation-Calibrated Self-Distillation [deconfounds replay-scaffold score shifts in OPSD]
- ③Agents & Agent Evaluation (8) — HiGram [evolving hierarchical graph memory with path-level localization/rewrite], EviGraph [typed evidence graph as operational state for autonomous research agents], Canary Tools [6-type MCP tool-selection diagnostic taxonomy, 8,640 runs], SkillSV [structure-aware Shapley valuation of agent skill units], Breadcrumbing Search Agents [one-controlled-result-per-query steering via the search observation channel], ContextWeave [1,005-task real-world workflow memory benchmark], OneDayAgent [long-horizon harness managing goal drift/state loss/context overflow], MatrAIx [8.3B persona simulated-user evaluation, ~1M released coreset]
- ④Serving, Memory & Efficiency (3) — Spend Bits Where Queries Look [attention-preserving KV-cache VQ, transform derived from distortion criterion], AFD-Ledger [offline provisioning AFD vs collocated MoE serving under TPOT SLO], MESH [hidden-momentum Sinkhorn for MoE expert matrices, fixes stateless-normalization failure]
- ⑤Evaluation, Safety & Interpretability (4) — IRT for AI Safety [8 benchmarks × 192 models, 3 factors: refusal strictness/truthfulness/contextual harm, UK AI Security Institute], CoT Monitoring Unreliable in Implicit-Influence Settings, SciCode-Verified [263-defect audit, 192 reject correct solutions in 91% of problems], Inference Backend as Behavioral Confound [HF/vLLM/Ollama change scores even under greedy]
- Key cross-cutting trends: rec/ads experimentation infrastructure becomes a research topic (two-sided A/B cost, A/B agents, experiment platforms); generative ranking matures on constraints/serving (GOAL/DEGR/live-streaming); OPD credit-assignment cluster (SPOT + observation-calibrated self-distillation); long-horizon agent memory benchmarked by workflow outcomes (ContextWeave/HiGram/OneDayAgent); verification-first thinking spreads (WorldCycle/Argus/EviGraph/SciCode-Verified); safety evaluation gets psychometric + influence-aware (IRT, implicit CoT, breadcrumbing)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-paper-check 08-06 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-06/arxiv-paper-check.md
- Contradictions: none (all claims verified against arXiv listing/abstract metadata; explicit non-overlap with prior digests)

## [2026-08-05] synthesis | LLM Tech Report Digest (2026-08-05)
- New page: wiki/synthesis/2026-08-05/tech-report-digest.md
- Coverage: 今日新增核实 9 项 + 保留更新若干——
- ① NVIDIA Nemotron 3 Super Technical Report (技术报告 PDF 2026-04-03): 120B 总 / 12B 激活 Hybrid Mamba-Attention MoE; 首次 LatentMoE + NVFP4 量化感知预训练 + MTP 投机解码层; 25T tokens; 1M ctx; 吞吐 2.2× GPT-OSS-120B / 7.5× Qwen3.5-122B; 权重开源。Nemotron 3 家族 (Nano/Super/Ultra) 技术报告至此齐备
- ② OpenAI GPT-5.6 价格调整 (2026-07-30): Luna -80% ($0.20/$1.20, 综合 $1.40 低于 Gemini 3.5 Flash-Lite $2.80 与 Gemini 3.6 Flash $9), Terra -20% ($2/$12), Sol 不变 + premium Fast mode; 效率收益让渡 + 直入低成本推理层
- ③ Google Gemini Robotics 2 模型卡×3 (2026-07-30): Robotics 2 (VLA, 全身控制 feet-to-fingertips + 双臂); ER 2 (Embodied Reasoning VLM, 基于 Gemini 3.5 Flash, 多机器人协作 + 连续视频任务监控 + 原生工具调用, AI Studio + Enterprise Agent Platform 可用); On-Device 2 (本地 VLA 基于 Gemma, 数小时数据适配新形态, Trusted Testers 分发)
- ④ Amazon AI 战略收缩 (2026-07-28 Business Insider): Nova Premier (9 月 EOL) / Omni / Reel / Canvas 逐步弃用, AGI Lab 解散, Pieter Abbeel (Covariant) 领衔新前沿项目 Frontier Model Research (FMR), 目标 re:Invent 2026 新旗舰; Nova 2 Lite/Sonic 保留; 与 Nova 2 技术报告 (2025-12-02) 形成"架构仍有效、产品线洗牌"对比
- ⑤ MiniMax H3 开源权重 (2026-08-02/03): 33B dense Omni Transformer (约 13B 在 AdaLN 分支可预计算缓存、推理免加载), Qwen3-VL-32B 文本编码器, Visual VAE + 独立 Audio VAE; FL2VA/Ref2VA 双任务 checkpoint (CFG-distilled); SGLang/vLLM/diffusers; MiniMax H3 Community License 可用区域限 EU/UK/South Korea/US ("not yet, not not ever" 可申请) —— 更新 08-04 的 "open weights 计划中"
- ⑥ Intern-S2-Preview 系列确认 (08-04 "待核实" 落地): 35B (2026-07-17 HF, 从 Qwen3.5 续训, task scaling 在核心科学任务媲美万亿级 Intern-S1-Pro); Intern-S2-Preview-397B (2026-07-18, MoE 约 120B 激活/~30%, 三维扩展: 预训练/RL task coverage/interactive agent env); 均 Apache-2.0, BF16 + FP8, HF + ModelScope
- ⑦ Mistral Shieldstral (2026-08-04 公告 / arXiv 07-28): 3B 开源多模态安全分类器; policy-adaptive QA; Apache-2.0; 12 语言; 单张 16GB GPU; 匹配 7× 体积模型; Open Secure AI Alliance (与 NVIDIA) 成员
- ⑧ Meta Muse Spark Safety & Preparedness Report 补充: Advanced AI Scaling Framework 评估 (Chem/Bio 缓解前 high risk), 拒绝率 SOTA, 同行对比中 cyber-misuse compliance 最低; Meta AI 底层模型
- ⑨ Qwen3.8-Max 定价补充 (08-03): $2/$6/$0.25 per M tokens; 权重"下周"与 Qwen3.8-27B 同行开源; 激活参数数与 license 未披露 (noze.it 质疑); 发布日阿里港股 +7%; QwenWork 平台公测
- 传闻核实 (未确认, 不入正式条目): GPT-5.7 / Astra (WinCentral + The Information, 命名未定), GLM-5.5 (JPMorgan 8 月), Phi-5 (GogoAI 单源 16B/MMLU 86.7%), Grok 4.6 (8/7, 1.5T V9) / Grok 4.7 (2.1T) (Musk 口头时间表, 更新 Grok 5 口径)
- Key trends: 定价战进入 2T+ 开源旗舰层 (Luna $1.40 vs DeepSeek/Xiaomi); 机器人成 System Card 新品类 (Gemini Robotics + Robostral); 开源=前沿扩散主通道 (H3 区域 License / K3 / V4-Flash MIT / Intern-S2 Apache-2.0 / Nemotron 3); 安全评估行业共同语言化 (Muse Spark framework 与 Preparedness 口径趋同); Amazon 战略收缩与前沿加码并行
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 08-05 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-05/tech-report-digest.md
- Contradictions: none (新增条目均独立核实; 与 08-04 digest 重叠条目显式保留引用; 传闻均标注 ⚠️ 未确认)

## [2026-08-05] synthesis | conference-digest
- New page: wiki/synthesis/2026-08-05/conference-digest.md
- Coverage: 本期补全此前未覆盖论文，获奖全景导航至 08-01/08-03/08-04 digests（ICML 2026 Seoul 7/6-11 / NeurIPS 2025 / ICLR 2026 Rio / AAAI 2026 Singapore / CVPR 2026 Denver / ACL 2026 San Diego / EMNLP 2025 / WWW 2026 Dubai 奖项均已覆盖）。新增：KDD 2026 Vol.1（Jeju 8/9-13, 1,215→256 ~21%, 奖励 8/13 公布）工业推荐 5 篇——Meta Lattice model-space 重构 [2512.09200, 生产 +10% 营收指标/+11.5% 满意度/+6% CVR/20% 容量, 全指标胜 Wukong, 4/8 SOTA @17× 更少 FLOPs], Alibaba FAT field-aware Transformer [2511.12081, 首个 Rademacher complexity CTR scaling law, +4.38% AUC 离线/+2.33% CTR+0.66% RPM], ByteDance MixFormer 稠密-序列协同扩展 [2602.14110, Douyin+Lite 双系统 A/B], Meituan MTFM 免对齐异构 token [2602.11235, GQA+Hybrid Target Attn], Tencent 微信支付商户类目识别 [meta-path+多边际 OT, +8.8% 准确率/+18.9% 营收]; 上下文 Kunlun/LLaTTE/TokenMixer-Large/DeGRe/FARM + KDD Cup=Tencent UNI-REC
- SIGIR 2026（Melbourne 7/20-24, 234+131, 奖励 pending）4 篇：KARMA Taobao LLM 个性化知识-行为正则化 [2603.22779, 修复 action 微调语义崩塌, +0.97 gAUC/+22.57 HR@200, 全漏斗部署, A/B +0.5% Item Click 零推理开销, 负结果 diffusion=差 embedding 生成器], GFlowGR CityU+Alibaba GFlowNet 微调 GR [淘宝搜索广告 2025 中部署 +0.4% 年营收], A2Gen Kuaishou 动作序列 GR [2604.25834, +0.34% watch time/+8.1% interaction/+0.162% L7 留存≈百万 DAU], Relevance Posterior Glasgow [2607.23561, BM25+QualT5 nDCG@10 +0.046, RankZephyr Δ≈+0.054, SPLADE naive 融合退化]
- ACL 2026 补 4 篇：ViLL-E Adobe/UCF 视频 LLM embedding 检索 [Outstanding+SAC Highlight, 动态计算追平专用 embedding], Lying with Truths Liverpool 真实碎片 montage 信念操纵 [Outstanding, 14 LLM 家族 >70%, 更强模型更易受骗], TRACE 代码翻译执行效率基准 [2026.acl-long.140], AgencyBench RUC 1M token agentic 基准 [2026.acl-long.337]; WWW 2026 补 NEZHA 零牺牲超高速 GR 解码 [2511.18793, 十亿级广告营收] + DiffusionGS/COINS/OMGRec; RecSys 2025 补 ULIM Taobao 千级序列召回 [2507.10097, +5.54% 点击/+11.01% 订单/+4.03% GMV] + Best Short Beyond Top-1 CFE; CIKM 2025 补 Best Student Padua 成本高效 LLM 相关性判断评估; ICLR 2026 补 e3 in-context exploration [CMU/MIT/Berkeley]; NeurIPS 2025 补 HRPO GDM 混合潜在推理 [2505.18454, 无需 CoT, HRPO-3B 0.380 EM 超 7B RAG 4.5%]
- arXiv 分类精选 18 篇（与今日 arxiv-daily/arxiv-ai-search 及此前扫描无重叠）：LLMs (Scaling Laws×Architecture UW+Amazon ICLR26 2510.18245, Distilled RL 2607.17247, Unsupervised RLVR 2603.08660), Agents (Switchcraft MSR 路由 82.9% 准确率/成本 −84%/$3,600 每百万查询), Recsys (TwiSTAR 自适应推理 2605.11553, Task-Aware 画像 2605.13497), CTR (DeRes γ=0.118 vs 0.071, 8 层≈16 层 OneTrans 2606.07980), Games (One Policy Infinite NPCs ρ=0.73/快 22× 2605.23652, DRL 增强游戏 AI 2606.20210), Code Execution (Cambridge+Amazon 符号执行轨迹 Qwen3-8B 3000 trace 2605.06184), Generative (GenCeption GDM 视频扩散=通用视觉学习器 2607.09024, Helios 14B PKU 19.5 FPS 2603.04379, Paris 2.0 FVD 561→279 2605.26064), Sequential (Mamba-3 Cartesia 复值状态+MIMO 状态/解码成本减半 2603.15569, Swimba MoE-SSM 2603.06938), Benchmarks (Power Systems Agent 2606.20950)
- Key trends: 推荐 Scaling 进入架构纪律时代 (Meta 统一/ByteDance 协同/Alibaba field-aware/Meituan 免对齐); GR 工业落地闭环 (十亿级营收信号 GFlowGR/NEZHA); LLM 个性化检索语义崩塌证据链 (KARMA); 安全多线并进 (真实碎片操纵/污染量化/对齐双刃剑); 序列模型效率与表达力同升 (Mamba-3/Swimba); 视频扩散=通用视觉学习器 (GenCeption/Helios/Paris 2.0)
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 08-05 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-05/conference-digest.md
- Contradictions: none（与 08-01/08-03/08-04 digests 及今日 arxiv-daily/arxiv-ai-search 显式去重；标注 tentative 的条目待核实）

## [2026-08-05] synthesis | arXiv Daily Digest (2026-08-05)
- New page: wiki/synthesis/2026-08-05/arxiv-daily.md
- Coverage: 24 papers curated from the Tue Aug 4, 2026 arXiv batch (newest full listing at run time: cs.AI 292 new / cs.IR 45 / cs.CL 129; arXiv system maintenance Aug 4–5 delayed part of the cs.IR stream into the Wed Aug 5 window). NO overlap with the Aug 4 digests — the Aug 1–3-submitted flagship rec/ads serving papers (GRACE, HRPO, Exp-RSFT, Tevatron 3.0, GARDRec, X-KGRank, UpliftBench) were already covered in the Aug 4 paper check.
- Sections: ①Generative & Sequential Rec (SITA target-aware semantic interest-token compression Huawei/USTC; ATLAS Gromov-Wasserstein + adversarial + RVQ zero-shot cross-domain rec, +24% HitRate, TCS Research; SmartGR hierarchy- & beam-aware GR distillation +8.6%/2.39×; OMEGA collaborative memory bank for GR), ②Advertising/Push/RTB (competition-aware RTB request dispatch: −34.2% DSP traffic / +4.6% revenue, 20B+ req/day, 4 online experiments, AdKDD 2026; STEPS self-triggered agentic push, Douyin 1B users, +0.2843% active days / −1.9089% permission disablement / −79.42% compute), ③Rec Eval & Feedback Theory (Position Bias preference-system inconsistency in listwise LLM reranking, RecSys 2026; Between-User Collapse centered-covariance theorem + computable phase boundary; LIME-Rec lightweight recovery test auditing "semantic" sequential-rec gains), ④LLM Reasoning & Post-Training (SFT Conflicts-RL Coexists norm-limited vs variance-limited gradient interference, CASIA; ReflectRL golden negative trajectories reflection→direct; TurnSight turn-level execution-conditioned hindsight self-distillation; Soft Guidance: zero-shot > few-shot CoT for reasoning-native models, EPFL; Logic-PPT 100B-token formal-derivation pre-pretraining, Sheffield/IDSIA), ⑤LLM Eval/Arch/Theory (DeepMind game theory for FMs: embedded Bayesian agent + embedded equilibrium replacing Nash; WorldCup Arena prospective leakage-free eval, 4,494 forecasts; ALiBi linear-bias fp underflow blinds attention heads), ⑥Agents & MAS (GDPevo rule-hybridization enterprise self-evolution benchmark, +16.44pp; ContinualSkillBench adaptation-vs-consolidation, PKU; Field-Aware Agent Skill Retrieval, UC Riverside; cross-implementation cross-play for ZSC, Oxford/FAIR), ⑦Retrieval & Search Infra (RubricRanker search-rubric set-level reranking, Renmin U; SIEVE fielded-Boolean search-inspect-fetch, −20.7–50.6% tokens, UQ/CSIRO; Hierarchical BM25 billion-scale, ~4.4GB resident / 4.7–5.6× flat throughput)
- Key cross-cutting trends: GR hits the serving wall (efficiency-first cluster); post-training theory unifies across recommenders and LLMs (reward geometry & credit granularity); rec evaluation shifts to preference/feedback theory; embedded-agency game theory for FMs emerges; contamination-resistant agent self-improvement benchmarks; cautionary audits (CoT distraction, ALiBi underflow, ICL≈explicit skill maintenance); lexical/structured retrieval fights back in the agentic era
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-05/arxiv-daily.md
- Contradictions: none (explicit non-overlap with Aug 4 digests; header flags residual overlap risk with the day's later scans)

## [2026-08-02] synthesis | Game RL & Game AI Bot Daily (2026-08-02)
- New page: wiki/synthesis/2026-08-02/game-rl-daily.md
- Coverage: 53 papers verified against arXiv API (no overlap with 07-27/08-01 game-rl digests)
- Sections: ①Game RL (10): Generals.io superhuman self-play ranking #1 of 5,000+ humans, JAX sim (2606.23348); CAST solver-as-teacher turn-level credit, USTC/Meituan (2607.25308); WallZero WallGo citywide (2606.17847); AlphaZero sparse-reward limits + AZAL (2607.08984); Big 2 self-play (2605.28863); Real-Time Parallel CFR Tsinghua (2605.19928); AlphaExploitem poker exploitation TU Delft (2605.09150); StarWM SC2 world model CASIA (2602.14857); Endpoint Replay U Alberta (2607.25123)
- ②Game AI Bot (7): environment-grounded prompt optimization Leibniz Hannover (2606.17838); Latent Bridge slow-fast dual-VLM real-time play (2606.24470); SPIKE dual controller (2605.18636); Clue deductive reasoning 18 games/4 wins (2603.17169); CA2 code-aware game testing McGill/Ubisoft (2605.13918); MIMIC-Py personality playtesting Concordia (2604.07752); Fixed-Persona SLM NPC dialogue (2511.10277)
- ③Game Foundation Models (9): NitroGen NVIDIA 40k h/1k games (2601.02427); DeepMind multi-agent Rocket League world model (2607.05352); AlayaWorld Alibaba (2607.18367); ABot-World-0 single-GPU rollout (2607.19191); Lumine 3D open worlds Tsinghua (2511.08892); MARL-GPT AIRI/HSE (2604.05943); Mind-Studio executable world models Edinburgh (2606.16070); Nano World Models MIT (2605.23993)
- ④PCG (6): Garden of Forking Paths narrative-arc generation NYU (2605.01245); World-Gen to Quest-Line RPG pipeline (2604.25482); Multiverse cross-game level blending (2603.26782); High-Dimensional PCG McGill (2602.18943); Zero-shot 3D map LLM agents (2512.10501); AutoBG board-game design assistant (2606.01976)
- ⑤Benchmarks (7): MINDGAMES live social-reasoning arena (2605.29512); OmniGameArena UE5 12 games HKU (2606.09826); GameWorld NUS (2604.07429); SciCrafter Minecraft discovery-to-application UCLA (2604.24697); OpenGuanDan (2602.00676); FootsiesGym fighting-game (2607.06514); MTG-Causal-RL UWA (2605.06066)
- ⑥Industry (6): TerraZero driving self-play 1.3M steps/s (2607.13028); ActionParty Snap multi-subject generative games (2604.02330); LPM 1.0 Tencent character performance (2604.07823); Play Like Champions counterfactual RTS coaching (2607.00190); Scouting by Reward esports IRL JHU (2604.14474); GameVerse video reflection (2603.06656)
- ⑦Related techniques (9): info-theoretic open-endedness Stanford (2606.08369); compositional open-ended intelligence MSR/FAIR (2606.15386); PopuLoRA population self-play RLVR (2605.16727); structural self-play collapse threshold (2605.16315); adversarial action removal (2605.16312); ARMS MARL reward shaping (2605.23562); minimax-regret team games MIT (2607.09993); SuS strategy-aware curiosity HSE (2601.10349); PARED IRL Apple (2607.24900)
- Key cross-cutting trends: superhuman self-play agents moving to full commercial games (Generals.io/Big 2/poker); world models becoming the backbone for both agents and foundation-model pipelines; multi-agent world models (Rocket League) breaking single-agent ceilings; PCG shifting from tiles/levels to narrative/quest/board-game generation; benchmarks moving to live human arenas (MINDGAMES) and video-first (OmniGameArena); industry proving out at scale (NitroGen 40k h, LPM 1.0, TerraZero 1.3M steps/s); theory hardening open-endedness & self-play collapse
- Updated: wiki/index.md (Synthesis 表新增 game-rl-daily 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-02/game-rl-daily.md
- Contradictions: none (all claims verified against arXiv API metadata)

## [2026-08-04] synthesis | arXiv Daily Digest (2026-08-04)
- New page: wiki/synthesis/2026-08-04/arxiv-daily.md
- Coverage: Curated from the Mon Aug 3, 2026 arXiv batch (the latest listing available at run time: cs.AI 43 new, cs.IR 13, cs.LG 82, cs.CL 51), selecting 26 papers with NO overlap with the Aug 3 arXiv AI scan / Aug 3 paper check / Jul 31 digest. The batch's flagship rec/CTR/ads papers (TransX, SnapLGR, GALA, Think2Go, PaletteID, EvoReason, RecHarness, GenCDSR, MerchantBench) were already covered in the Aug 3 digests.
- Sections: ①LLM Evaluation & Alignment (Chain-of-Models cross-model judge auditing NUS; Formalism Trap D_E evaluator capture; CalibratedRubric IRT rubric banks; Know-It-Act-On-It Know/Act personalization gap; "LMs Agree With Each Other, Not With Readers" organic-reference homogenization study; TokenSwap modality-gap benchmark 42 MLLMs), ②LLM Reasoning & Efficiency (BLADE learned-layer dynamic exit −24.8% tokens; CoT entropy compression negative result vs random; LARA residual-stream adapters 7 behaviors/~33MB; Copula-Gumbel-Top-K frozen-MoE routing laws; PTP black-box previous-token LLM inversion), ③Recommendation/Search/User Modeling (MMShopBench real-log multimodal shopping agents; SERUM egocentric-video state-machine user models; MBDiff behavior-aware utility imputation +7.04%/+29.1%), ④Agents & Multi-Agent (MARS MCTS autonomous MAS repair +3.0–12.1% on StateMAS; WILC relay-style LLM crowds ≈GPT-5.2 at ~7× lower cost; CAGE certified authorization non-composition proof; SafeKeep tool-schema refusal erosion 23.8→70.6%; 257-paper agentic validation survey; AdaMM analytic memory +11.3%/+7.3%), ⑤RL & Bandits (Gated Q-learning Watkins/Peng interpolation; parameter-free heavy-tailed bandits COLT'25 open problem; continuous-time PG regret O(log T); LEMUR preference-based MORL), ⑥Sequential Modeling & Generative Efficiency (Transcript-Managed Transformers: 2 pop channels ⇒ RE universality; OnlineCache learned diffusion caching ~3× FLUX.1-dev)
- Key cross-cutting trends: judge formalization; negative results for cheap inference tricks (day 2); adaptation/routing out of the weights; agent memory splits storage-vs-use-vs-analysis; mechanistic agent safety; relay-style multi-LLM orchestration; heavy-tailed/off-policy RL theory
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-04/arxiv-daily.md
- Contradictions: none (report explicitly non-overlapping with Aug 3 scans; ⚠️ note flags that the strongest CTR/ads papers were covered Aug 3)

## [2026-08-03] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-08-03)
- New page: wiki/synthesis/2026-08-03/wq101-alpha-daily.md
- Coverage: 数据基准 7/31 收盘 + 8/3 盘前/期货口径（周一版），基于 WorldQuant 101 Alpha 因子框架对美股 Top 20 打分
- 8/3 盘前增量（相对 8/2 报告）: ①地缘大幅缓和——特朗普取消对伊打击, Brent <$84 (-5%)/WTI -4%+, OPEC+ 9 月增产 18.8 万桶/日 → 能源板块集体回吐 7 月地缘溢价; ②金融板块创新高——XLF 历史新高 $57.60, JPM/BAC 同创 52 周新高, 资金由科技向金融轮动; ③国防军工崛起——LMT +10.6%/RTX +7.7% (上调 2026 指引), Trump $1.5T 军费提案 + $1.15T 国防授权法案; ④美日 2011 年以来首次联合干预日元; ⑤金价 ~$4,060 高位; ⑥10Y 回落至 ~4.70%; ⑦9/16 FOMC 加息 25bp 定价维持 (CME FedWatch ~54-61%/MoneyDJ ~65%)
- Key signals: MSFT $464.72+3.02%(Azure 年化破 $100B+43%/下年 Capex 指引 $255-260B/兑现者第一名); AMZN $271.58+15.32%(AWS $42.2B+37%/积压 $364→$496B/Capex 上修 $220B/FCF-$76亿); GOOGL $356.13+6.73%(云+82%/积压 $514B/云利润率 35.6%/FCF 首负-$59亿); NVDA $200.75+2.93%(PE~24x 低位/供给承诺 $119B/8/26 财报前 AMD 周二为需求确认/SK hynix ADR 纳斯达克上市强化 HBM 链); JPM $351.79 创新高(Q2 净利 $21.2B 创纪录/ROTCE 23%/IB+30%/XLF $57.60 历史新高); BAC 新入选 52 周新高(Q2 净利 $9.1B/存款行 NIM 弹性); GS $1018.38(EPS $20.98 近翻倍/backlog 5 年最高); AVGO(Q3 AI 半导体指引 $16B+200%); AMD $476.15(周二 8/4 盘后财报/指引 $11.2B±$300M/EPYC+70% 预期/MI400 看点); LMT 新入选 +10.6%(积压 $230.4B+38.3%/上调指引/$1.15T NDAA); RTX 新入选 +7.7%(上调指引); TSM(3nm 交期超 50 周/类 EMIB); LRCX(下季指引 $8.1B vs 预期 $7.09B 设备链景气); CVX $196.83+2.35%(Q2 净利 $12.1B 创纪录/8/3 油价逆风); XOM(净利 $14.5B/回购 $5.1B); PLTR(周一盘后财报/营收预期 $1.81B+81%/EPS $0.35/Maven program-of-record/61x PS); LLY(周三盘前财报/2026 指引 $82-85B/GS 模型 $86.1B 上调空间); MU $823.03(7 月-28.7% 超卖/HBM4 量产/周四 SNDK/WDC 验证); GEV($176B 积压/FY26 FCF 指引上调至 $11.5-12.5B); CAT(周二盘前财报/EPS 预期 $6.26/积压 $63B)
- Factor mix: Alpha#6 量价(10 次/50%)+Alpha#41 趋势(10 次/50%, 从 8/2 的 35% 升至 50%——新高金融/国防主导)+Alpha#1 动量(9 次/45%, 从 55% 降至 45%)+Alpha#53 反转(4 次/20%)+Alpha#12 背离(3 次/15%)+Alpha#19 均值(2 次/10%)+Alpha#30 波动率(2 次/10%)
- Sector mix: Semis 6 只(30%)+Financials 3 只(15%)+Tech/Cloud/Comm 3 只(15%)+Defense 2 只(10%)+Energy 2 只(10%)+Software/AI 1 只(5%)+Healthcare 1 只(5%)+Utilities/Power 1 只(5%)+Industrials 1 只(5%)
- Top 5: MSFT(9.5)/AMZN(9.3)/GOOGL(9.2)/NVDA(9.0)/JPM(8.7)
- Strategy: 金融(15%↑)+国防(10%新增)接替能源成为轮动主线——地缘溢价从能源向军工转移, 9 月加息定价利好金融 NIM; 能源降至 10%(8/3 油价大跌, COP/LNG 移出仅留 CVX/XOM); Tech 降至 15%(META 移出, FCF-91% 许诺者折价未解); Semis 30% 持平(NVDA 低位+AMD 周二确认); 新入选 BAC/LMT/RTX; 候补: META/COP/LNG/SNDK/WDC/ETN/MRK; 事件周(PLTR 周一/AMD+CAT+SpaceX 周二/LLY 周三/SNDK-WDC 周四/非农周五)严控仓位, 8/3 盘中可能显著偏离盘前假设
- Updated: wiki/index.md (Synthesis 表新增 wq101-alpha-daily 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-03/wq101-alpha-daily.md
- Contradictions: none (9 月加息定价 8/2 修正后 54-61% 维持一致; 8/3 为盘前口径未涉及收盘数据冲突)

## [2026-08-03] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-08-03)
- New page: wiki/synthesis/2026-08-03/investment-daily.md
- Coverage: 周一版·超级周第二波 (数据说明: 美股最新完整收盘为 7/31, 港股/A股为 7/31 收盘 + 8/3 早盘口径)
- US stocks (7/31 close): S&P 7489.72(+0.70%)/Nasdaq 25373.85(+1.00%)/Dow 52485.03(+0.53%)/费半 11311.08(+0.07%) 7月-20.61% 创 2008/10 以来最差单月/VIX 15.99(-6.44%); 兑现者vs许诺者分化定格: AMZN +15.32% $271.58 (AWS $42.2B +37%/积压 $364→$496B/Capex 指引 $2200亿/FCF 转负 -$76亿, 创 2008 来最大单日涨幅), GOOGL +6.73% $356.13 (云 +82%/积压 $514B/云利润率 35.6%/FCF 上市来首负 -$59亿/Capex $195-205B), MSFT 7/30 财报后 +16% 7/31 收 $464.72 (+3.02%) (Azure 年化破 $100B +43%/Capex $41B), AAPL -7.35% $308.91 (Q3 营收 $109.42B +16% 但 Q4 指引 9-11% 弱/库克警告先进制程产能与内存供应吃紧/单日蒸发 $3578亿 美史上第三大), META 企稳但 FCF 同比 -91% 至 $7.84亿, NVDA +2.93% $200.75 (市值 ~$4.86T 重夺全球第一/PE ~22-24x/算力地租 OpenAI $2500亿担保+10GW)
- SpaceX (SPCX): 6/12 IPO $135 一度 $225 现 <$110; 8/4 盘后首份财报 + 8/6 首批 9.115 亿股解禁 (~$1092-1160亿, 美股史上最大单股解禁, 空头持仓 2.193 亿股≈流通盘 34%)
- Semis: AMD 8/5 盘后财报 (Q2 指引 $11.2B +46%/EPYC +70% 预期/MI400 看点); LRCX 下季指引 $8.1B vs 预期 $7.09B (设备链景气实证); 存储进入验证期: 铠侠 8/1 ADR -10.1%/MU -5.9%/SNDK -5.09% (8/6 SNDK/WDC 财报验证), 三星/SK 海力士创纪录财报+HBM 短缺至 2028; AI 造芯: Google 300 万颗 TPU 委托英特尔 + NVDA 评估 EMIB + OpenAI×Broadcom Jalapeño
- Macro: ⚠️口径修正与 8/2 一致——市场定价 9 月加息而非降息 (CME FedWatch ~65% MoneyDJ 口径/一周前 82%; wq101 8/2 修正为 54-61%), BofA 预期 2026 剩余三次会议均加息 25bp 至 4.25-4.50%, 7/29 FOMC 9-3 按兵不动 (3 位主张加息); 10Y 盘中破 4.7% 创 2025/1 来新高, 30Y ~5.25%; WTI $84.67 (+1.3%)/Brent $90.12 (+1.2%) (美伊反复); 中国 7 月 PMI 49.2%; 发改委"十五五"算力网新增直接投资 4 万亿+加快 AI 法立法
- HK stocks (8/3 早盘口径): 恒指开盘 +0.4%, 恒生科技 +0.68% 盘中涨超 1%; 阿里 +3%/百度 +近 3%/京东盘中 +4%; 智谱盘中一度 -5~-8% 市值跌破 8000 亿港元 (解禁抛压), MiniMax 千亿解禁创 3 个多月新低 (下一代模型 >2 万亿参数); 宁德时代 H (03750) 小摩 7/27 增持 40.9 万股 @ HK$627.77 持股升至 6.08%; 南向 7/31 净买超 120 亿; 中芯 Q2 业绩 8/13
- A-shares: 7/31 反攻收官 (上证 3832.26 +0.72%/深成指 +2.21%/创业板 +3.06%/科创 50 +2.99% 盘中 +8%, 成交 2.56 万亿, 4691 涨/101 涨停, 半导体净流入 94.97 亿居首); 7 月深成指 -16.21%/创业板 -23% 创逾十年最大, 市值蒸发逾 12 万亿; 8/3 低开 -0.51~-0.71% 半导体/PCB/光刻机走弱, 核聚变/人形机器人/AI 应用/PEEK 走强 (⚠️8/3 收盘数据来源矛盾, 仅以开盘/盘中口径呈现); 长鑫科技 688825 盘中 +13% 市值破 4 万亿 (H1 预告营收 1100-1200 亿 +612-677%/净利 500-570 亿, 8/1 起 20% 涨跌幅); 宇树科技 688836 8/5 初步询价/8/10 申购/8/12 缴款 (发行市值 ~420 亿, 募资 42.02 亿 85% 研发, 机构预期市值 600-1090 亿); 中科曙光+海光信息吸收合并推进; 寒武纪 8/8 中报; 宁德时代 H1 净利 432.8 亿 +42% +回购 200-400 亿注销; 电池消费税 9/1 起落地
- China ADR (7/31): 金龙指数 +0.67% (7 月累计 +19.89%); BABA +5.10% $122.25 (AI 云+Qwen 生态, ~8-10x P/E); PDD +1.28% $88.56; NIO +3%; BILI +2%; TME -1%; XPEV 7/30 -7.54% (阿里巴巴淘宝中国拟售 2500 万份 ADR ≈ $3.91 亿, 持股 10.2%→7.5%, 阿里回应仍为第二大股东) → 7/31 +0.15% $13.00; 花旗维持买入 H 目标 HK$87.7, 预期 Q2 Non-GAAP 净亏 ~10 亿、Q3 交付 ~13 万辆 (低于市场 15 万)
- EV (July 2026 汇总): 比亚迪 41.92 万 (+22%, 出口 17.98 万 +124.3% 海外占比破 40%)/零跑 10.13 万首破 10 万 (+102%)/鸿蒙智行 4.5 万/小鹏 38,027 (+4%)/蔚来 35,934 (+71%)/理想 30,468 (-0.86% 唯一同比环比双降)/小米超 3 万连 4 月 (全年 55 万目标需月均 6.7 万)/极氪 35,837 (+111%); TSLA Q2 营业利润 -57% $3.98亿/FCF -$10.92亿/Capex $57.89亿 +142%/2026 Capex >$250亿/拟融资 $300亿/Fremont Model S/X 产线改 Optimus 产线 (财报后 -14.52%)
- AI hot themes: ①大模型参数竞赛重启 (Kimi K3 2.78 万亿全球最大开源, 稀疏度 56x 激活 ~1042 亿, 48h 打满集群暂停订阅; 月之暗面超 $35 亿融资估值 $350 亿 Pre-IPO $500 亿; Qwen3.8 Max 2.4T/文心 5.0 2.4T/DeepSeek V4-Pro 1.6T (正式版尽快发布)/MiniMax 下一代 >2T; 野村: 3T 是下一里程碑; 海外 API 限制→倒逼国产大参数自研); ②Kimi K3 冲击余波 (美股单日蒸发 ~$4700 亿/17 家投行下调芯片目标价; 银河: K3 引爆推理算力需求利好国产超节点; 大摩 Buying the AI Infra Dip: 需求非仓位问题, Big5 Capex 2026 ~$8000亿→2028 $1.4T); ③杠杆出清 (Situational Awareness 7 月 -67% 被迫售予 Citadel 清杠杆 = 7/31 反弹部分归因; 去杠杆结束≠新杠杆繁荣); ④模型周报: DeepSeek-V4-Flash 正式版 8/1 (AA 指数 50 vs GPT-5.6 Luna 51, 成本低 60%), 字节 Seedance 2.5 视频, OpenAI Astra 10 项数学突破成本 ~$2000, Anthropic Claude 意外联网失控事件; ⑤定制 ASIC/先进封装 (台积电类 EMIB); ⑥AI 电力/散热瓶颈 (四大云厂 ~$2.4T 基建需 55-60GW≈55-60 座核反应堆; 三星 8/4-6 FMS HBM4E 路线图, Hinton/李飞飞/吴恩达首度同台)
- Key catalysts: 8/3 ISM+PLTR(盘后)/8/4 SpaceX 首份财报(盘后)+AMD(盘后)+FMS/Ai4/GIL 大会/8/5 宇树初步询价+SpaceX 电话会/8/6 SpaceX 解禁 ~$1092-1160亿+SNDK/WDC 财报/8/7 美国 7 月非农 (预期 +8.3万/失业率 4.3%)/8/8 寒武纪中报/8/9 中国 7 月 CPI/PPI/8/10 宇树申购/8/13 中芯 Q2
- Strategy: 短期持有"兑现者"(MSFT/AMZN/GOOGL/NVDA/AVGO) 回避存储高波动; 利率风险主导 (9 月加息 ~65% + 30Y 5.25% 压长久期); A 股机构称调整近尾声、未来两月修复窗口; 中期主线: 国产算力 (十五五 4 万亿算力网+大模型适配政策)/存储超级周期 (长鑫产业链)/人形机器人 (宇树 IPO+Optimus V3)/定制 ASIC/先进封装/AI 电力散热; 风险: SpaceX 财报+解禁双杀、SNDK/WDC 存储验证、9 月加息定价上行、非农超预期、油价/中东、A 股二次探底、智谱/MiniMax 解禁
- Updated: wiki/index.md (Synthesis 表新增 investment-daily 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-03/investment-daily.md
- Contradictions: 1 (8/3 A 股收盘数据多来源冲突 [淘股吧旧数据疑似 2021 年/另一来源报沪指 -1.15% 收 3831.66+成交换手暴增]，已标注为盘中口径; 9 月加息概率 8/2 已修正为 54-61% 一致)

## [2026-08-03] synthesis | LLM 技术报告摘要 (2026-08-03)
- New page: wiki/synthesis/2026-08-03/tech-report-digest.md
- Coverage: 19 家公司大模型技术报告/System Card 全景 (双语表格, 沿用 07-31/08-01 格式)
- 今日新增核实:
  - Amazon Nova 2 技术报告 (2026, Hybrid Reasoning: Lite/Pro 的 low/medium/high effort + 内置工具; Nova 2 Lite 相比 Nova Premier 7× 更低成本/5× 更快; τ²-bench Lite 76.0 / Pro 92.7) — ⚠️ 更正 08-01 "Amazon 无 2026 新报告" 结论
  - Anthropic Claude Sonnet 5 System Card (2026-06-30, RSP 评估 + agentic 增益; MASK 说谎率 3.1% 为对比集最低; hallucination/sycophancy 显著改善; cyber safeguards 默认开启; $2/$10 → 8/31 后 $3/$15)
  - Apple AFM 3 (2026-06-08, 五模型家族: 3B Core 端侧 + 20B Core Advanced 稀疏 IFP 激活 1-4B + Cloud PCC + ADM 3 Cloud 图像扩散 + Cloud Pro 首次跑在 Google Cloud NVIDIA GPU 上)
  - NVIDIA Nemotron 3 Ultra (550B/55B, 108 层/512 experts top-22, Mamba-2+Attention+LatentMoE 混合 + MTP, NVFP4 预训练 ~20T tokens, MOPD 后训练, 1M ctx, OpenMDW-1.1, AA Index ~48, 吞吐 5.9×)
  - xAI Grok 4.5 发布细节 (2026-07-08, SpaceXAI 品牌 + 与 Cursor 联合训练, 数万 GB300, 500K ctx, $2/$6, DeepSWE 62.0% / SWE-bench Pro 64.7% / Terminal-Bench 2.1 83.3%)
  - Qwen3.7-Flash (2026-07-25, 原生视觉语言 Flash) + Qwen-Audio-3.0-ASR-Flash (2026-07-30, 30 语言+七大方言)
  - Mistral Robostral Navigate (2026-07-08, 具身导航)
  - Baichuan-M4 细节 + 更正 (2026-06-22, 清华合作临床级医疗 agent, Baichuan-Harness 评测, hallucination 3.3%, arXiv:2606.08982) — ⚠️ 更正 08-01 误记的 arXiv ID (2606.12721)
  - Moonshot MoonEP 开源 (2026-07-29, 专家并行库)
- Confirmed no new report: OpenAI (GPT-5.6 已收录), Google (Gemini 3.6 Flash 已收录), Microsoft (Phi-4-rv 已收录), ByteDance (Seedance 2.5 已收录), Zhipu (GLM-5.2 已收录; GLM-5.3 仍为传言), InternLM (Intern-S1-Pro 已收录; 2026 无新技术报告), StepFun (Step 3.5 Flash 已收录), Yi/01.AI (2026 无新旗舰/新技术报告)
- 交叉观察: 美国开源权重旗舰之争 (Nemotron 3 Ultra vs DeepSeek-V4 / GLM-5.2 / Kimi K3); 混合推理 effort 控制趋同 (Nova 2 / OpenAI / Gemini / Grok); Mamba-Attention 混合 + 投机解码标配化; agentic 基准 (DeepSWE / SWE-bench Pro / Terminal-Bench 2.1) 成发布主战场; 端侧-云端边界重画 (Apple IFP + PCC on Google Cloud); 中国医疗垂直模型崛起 (Baichuan-M3/M4)
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-03/tech-report-digest.md
- Contradictions: 2 (Amazon "无 2026 报告" → Nova 2 技术报告存在; Baichuan-M4 arXiv ID 更正)

## [2026-08-02] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-08-02)
- New page: wiki/synthesis/2026-08-02/wq101-alpha-daily.md
- Coverage: 数据基准 7/31 收盘(周末版),基于 WorldQuant 101 Alpha 因子框架对美股 Top 20 打分
- Market (7/31 close): S&P 7489.72(+0.70%)/Nasdaq 25373.85(+1.00%)/Dow 52485.03(+0.53%)/VIX 15.99(-6.44%); 7月收官12年来首次7月收跌(S&P -0.13%/纳指-3.20%/道指+0.32%),费半-20.6%创2008来最差单月,等权标普7月跑赢纳指100达7.6pp,资金由Mag7高位AI交易向价值/防御轮动
- ⚠️ 修正 8/1 报告: "9月降息~68%"有误。经核实 7/29 FOMC 9-3 通过按兵不动(3名异议者主张立即加息),主席 Warsh 不给前瞻指引; 截至 7/31-8/2, Kalshi(54-59%)/CME FedWatch(55.9-61.4%)/Polymarket(52-60%)/利率互换(~60%)/BofA(2026剩余三次会议均加息25bp至4.25-4.50%)一致指向 **9/16 FOMC 加息 25bp 至 3.75-4.00%** 为基准情形 —— 本周宏观定价最重要变化
- Weekend (8/1-8/2): 中东升级(美State Dept敦促撤侨+空域封锁预警/黑海7月80+起商船遇袭/运输保险成本历史高位)但特朗普宣布取消最新一轮空袭; Brent~$87.9/WTI~$84.6(原油7月+21%)
- Earnings week: 8/3 PLTR财报(盘后)+ISM制造业; 8/4 AMD财报(盘后,官方确认)+CAT(盘前,EPS预期$6.26,Q1积压$63B)+SpaceX首份财报(盘后); 8/5 LLY财报(盘前)+MRK+SNDK; 8/6 SpaceX首批9.115亿股解禁(~$1092亿); 8/7美国7月非农(Reuters初值+8.3万/失业率4.3%)
- Key signals: AMZN $271.58+15.3%(AWS$42.2B+37%/Capex上修$220B/FCF-$76亿,单周市值+$400B); MSFT $464.72+3.02%(Azure年化破$100B+43%,单周+$600B); GOOGL $356.13+6.7%(云+82%/积压$514B/云利润率35.6%/FCF首转负-$59亿); NVDA $200.75+2.93%(Q1 FY27营收$81.6B+85%/数据中心$75.2B+92%/Q2指引$91B/PE~24x/供给承诺$119B,重夺全球市值第一$4.86T); CVX $196.83+2.35%(Q2净利$12.1B创纪录~+400%/美国产量~2M bpd创纪录/调整EPS $6.06超50c/炼化利润+500%); XOM(净利$14.5B/FCF$17.2B/回购$5.1B/调整EPS $3.52 miss 8c); AVGO+11%(Q3 AI硅片指引$16B+200% YoY/Apple $30B定制长约至2031/OpenAI Jalapeño); AMD $476.15-1.90%(8/4财报预期营收$11.2B+46%/数据中心Q1 $5.8B+57%/Meta 6GW+OpenAI/MI350 H2 2026); MU $823.03-5.9%(7月-28.7%/16份战略长约+14份take-or-pay锁定~$100B最低收入至2030/DRAM合约价Q2+89%/HBM4量产); TSM(3nm交期超50周/2027提价5-10%预期); JPM $351.79(Q2净利$21.2B创纪录/调整口径$16.9B ROTCE 23%/IB费+30% 2021来最高/市场交易+35%); GS $1018.38(EPS $20.98同比近翻倍/营收$20.34B+39%/backlog 5年最高); COP(7月+13.5%/油价弹性最大纯上游); LLY ~$1155(8/5盘前财报/2026指引$82-85B/GS模型$86.1B上调空间); LNG(霍尔木兹+LNG溢价); PLTR ~$122(周一盘后财报/61x PS/2026 FCF指引$4.2-4.4B); CAT(Q1积压$63B创纪录); GEV($176B积压/116GW燃气轮机锁定/Q2订单$24.2B+88%/FY26 FCF上调至$11.5-12.5B/与CVX合资4GW直供电/风电分部-275M+关税$100-200M); META(+3.28%企稳但Capex上修$135-145B/FCF同比-91%至$7.84亿)
- Factor mix: Alpha#1动量(11次/55%)+Alpha#6量价(10次/50%)+Alpha#41趋势(7次/35%)+Alpha#53反转(5次/25%)+Alpha#12背离(3次/15%)+Alpha#19均值(3次/15%)+Alpha#30波动率(1次/5%)
- Sector mix: Semis 6只(30%)+Energy 4只(20%)+Tech/Cloud/Comm 4只(20%)+Financials 2只(10%)+Healthcare 1只(5%)+Software/AI 1只(5%)+Industrials 1只(5%)+Utilities/Power 1只(5%)
- Top 5: AMZN(9.6)/MSFT(9.4)/GOOGL(9.2)/NVDA(8.9)/CVX(8.7)
- Strategy: 兑现者溢价延续(AMZN+MSFT+GOOGL单周合计+$1.5T市值)vs许诺者折价(META/AAPL); 事件周驱动(PLTR/AMD/LLY/非农); 新增Financials 2只(9月加息定价54-61%利好银行NIM,四大行Q2合计$43B创纪录); 存储降配仅留MU(铠侠8/1 ADR-10.1%指引弱=SNDK移出); Utilities/EV减配(30Y破5.2%+加息压制长久期,移除NEE/TSLA); 移除OXY/UNH; 候补观察: SNDK/BAC/MRK/ETN/DXCM/UNH
- Updated: wiki/index.md (Synthesis表新增wq101-alpha-daily条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-02/wq101-alpha-daily.md
- Contradictions: 1 (修正8/1 wq101报告"9月降息~68%"→9月加息54-61%; 与investment-daily(8/2)表述一致)

## [2026-08-02] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-08-02)
- New page: wiki/synthesis/2026-08-02/investment-daily.md
- Coverage: 周日版·超级周前瞻（美股 7/31 收盘/港股/A股/中概股/AI热点/7月新能源车交付）
- US stocks (7/31 close): S&P 7489.72(+0.70%)/Nasdaq 25373.85(+1.00%)/Dow 52485.03(+0.53%)/VIX 15.99(-6.44%); 7月收官: 标普-0.13%/纳指-3.20%/道指+0.32%, 费半-20.6%创2008来最差单月, 台积电ADR-15.4%; AMZN+15.3%创2008来最大单日(Q2净销售$200.6B+20%/AWS$42.2B+37%/Capex指引2200亿/FCF转负-$76亿); AAPL-7.4%创2014来最大单日跌幅、市值蒸发$3578亿(美国史上第三大)(Q3营收$109.42B+16%但Q4指引9-11%弱/大中华区$18.8B不及预期/内存涨价挤压毛利); MSFT+16%(Azure年化破$100B+43%/Q4营收$90B+18%); GOOGL+6.7%(云+82%/积压$514B/云利润率35.6%/FCF首转负-$59亿); META周四-7.98%周五+3.28%(Capex $135-145B/FCF同比萎缩90%至$7.84亿); NVDA+2.93%收$200.75市值$4.86T重夺全球第一(PE~22x/算力地租:OpenAI $2500亿担保+10GW数据中心/SPV+ABS)
- SpaceX (SPCX): 8/4首份财报(预期营收$68-69亿/EPS-$0.25~-0.29), 8/6首批9.115亿股解禁(约$1092亿=IPO募资额1.45倍), Starlink连接业务$32.57亿占69%, AI板块上季$8.18亿但Q1 AI Capex $77.2亿占76%=最大烧钱点, 星舰研发拖累FCF
- Semis: AVGO+11%(谷歌链)/AMBA+16.08%(AI边缘芯片)/TSM+0.2%(7月-15.4%)/MU-5.9%(Burry增空)/SNDK-5%(7/30+21%后回吐)/铠侠8/1财报不及预期ADR-10.1%(存储链降温信号); AMD 8/5财报(指引$11.2B+46%/EPYC+70%预期); AI造芯大战: Google Frozen v2+OpenAI×Broadcom Jalapeño定制ASIC
- Macro: Fed按兵不动3.50-3.75%9月降息~68%; 30Y美债5.2%+(2007来最高附近); 美国7月非农8/7(6月大幅不及预期后关键指引); 中国7月PMI 49.2%; 政治局会议"稳市"; 美伊冲突峰回路转(特朗普取消空袭/WTI$82.8); 四大云厂未来数年承诺~$2.4T基建/需55-60GW电力(≈55-60座核反应堆)
- HK stocks (7/31 close): 恒指25884.43(+0.10%)7月+13.1%(+3003点), 恒生科技4829.22(+0.53%)7月+7.98%; 阿里+4.65%领涨/智谱+14.56%/MiniMax+13.15%(发布MiniMax H3)/联想+9.75%/中际旭创H股+7%至HK$1028(较招股价高4.9%)/金山云+15.74%/小米-7.28%(澎程卖事实)/中芯+2.02%(业绩修正8/13); 南向净买超120亿(阿里12.34亿/小米17.16亿)
- A-shares (7/31 close): 上证3832.26(+0.72%)/深成指13578.93(+2.21%)/创业板3343.96(+3.06%)/科创50+2.99%盘中+8%; 成交2.56万亿放量逾2000亿/4691只上涨/科技四大板块吸金460亿; 半导体(杰华特/芯原/盛科+10%+)+AI应用(中文在线/昆仑万维涨停)+人形机器人(永茂泰涨停)+光通信回归(新易盛+6.71%/中际旭创+4.40%); 主力净流入前五: 东山精密33.44亿/太极实业25.08亿/蓝色光标24.19亿/兆易创新23.14亿/长鑫15.02亿
- 长鑫科技(688825.SH): 7/31盘中最高60.60元(+13%+)市值首破4万亿(≈2.4个茅台), 8/1起20%涨跌幅限制; Q1营收508亿(+719%)净利247.62亿扭亏, 2026H1营收预告1100-1200亿(+612-677%)
- 宇树科技(688836.SH): 8/5初步询价/8/10网上网下申购/8/12缴款, 发行4044.6434万股(占发行后10%), 募资42.02亿(85%研发/智能机器人模型研发20.22亿占48%), 发行价预估~104元/签缴款5.2万, 机构预测市值600-1090亿(建银PS 32x), 2026H1营收预计10.52-11.28亿(+35.6-45.4%), 王兴兴控制68.78%表决权(特别表决权机制); 7/31宇树概念指数+6.66%/人形机器人指数+4.98%
- EV (July 2026 confirmed): 比亚迪41.92万(+21.76%,海外17.98万+124.3%)/零跑10.13万首破10万(+102%)/鸿蒙智行4.5万(连续2月同比下滑)/小鹏3.8万(+4%)/蔚来3.59万(+71%)/理想3.05万(-0.86%唯一双降)/小米超3万连4月/极氪3.58万(+111%)/奇瑞27.68万(出口20.25万创中国单月出口纪录); 零跑/极氪/极狐同比翻番; 小米全年55万目标剩5个月月均需6.7万辆
- China ADR (7/31): 金龙指数+1.47%; BABA+5.09%($122.25)/JD+2.17%/金山云+近10%/有道+近5%/TME+3%
- AI hot themes: 兑现者溢价固化(AMZN/MSFT/GOOGL vs AAPL/META); 存储超级周期进入验证期(铠侠ADR-10.1% vs 长鑫破4万亿,中美定价分化); 人形机器人量产元年(宇树IPO+Optimus V3); 开源模型冲击(月之暗面Kimi K3发布引美股AI板块单日蒸发~$4700亿/17家投行下调芯片目标价/48小时打满集群暂停订阅); AI Infra新赛道(GPU利用率优化/vLLM·SGLang商业化/Baseten 20倍收入增长/Fireworks估值175亿); AI电力散热瓶颈(液冷渗透率2026破40%); Anthropic×SpaceX接管Colossus 1(300MW/22万张GPU)
- Key catalysts: 8/3央行逆回购/8/4 SpaceX首份财报/8/5 AMD财报+宇树初步询价/8/6 SpaceX首批解禁/8/7美国7月非农/8/10宇树申购/8/12宇树缴款/8/13中芯Q2业绩
- 修正: 中芯国际Q2业绩日由 8/6 修正为 8/13(董事会批准刊发,8/14业绩说明会)
- Updated: wiki/index.md (Synthesis表新增investment-daily条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-02/investment-daily.md
- Contradictions: 无(长鑫科技8/1起涨跌幅限制与前期"8/1无限制最后交易日"表述一致; 中芯业绩日修正为本期更正)

## [2026-08-02] synthesis | LLM 技术报告摘要 (2026-08-02)
- New page: wiki/synthesis/2026-08-02/tech-report-digest.md
- Coverage: 19 家公司大模型技术报告/System Card 全景（双语表格，沿用 07-31/08-01 格式）
- 今日新增核实:
  - NVIDIA Nemotron 3 Ultra 技术报告 (2026-06-09, 550B 总/55B 激活 Hybrid Mamba-Attention MoE + LatentMoE; NVFP4 预训练 20T tokens; MOPD 多环境 RLVR + 推理预算控制; 1M ctx; 吞吐约 6× 提升; 开源)
  - Apple AFM 3 五模型家族 (2026-06-08, 与 Google 合作: 3B Core + 20B Core Advanced 稀疏激活 1-4B + Cloud PCC + ADM 3 Cloud 图像 + Cloud Pro 推理/Agentic)
  - Amazon Nova 2 技术报告 (2026, Lite/Pro extended thinking 可配置推理; Omni 文本+图像+视频+音频输入/文本+图像输出; Sonic 语音到语音; 全系 1M ctx) — ⚠️ 更正 08-01 "Amazon 无 2026 新报告" 结论
  - Zhipu GLM-5 (arXiv:2602.15763, 2026-02-17, 与清华合作; DSA 降低训练/推理成本; 异步 RL 基础设施 + 异步 agent RL; 开源基准 SOTA; 端到端真实软件工程)
  - xAI Grok 4.5 Model Card 核实确认 (2026-07-14, SpaceXAI/Cursor 合作; 推理步骤数约为其他前沿模型一半; 安全域含 cyber/bio knowledge/bio agentic/反越狱/尽力输出安全含 CBRN 拒答/心理健康/行为)
  - Anthropic Claude Opus 5 System Card 核实确认 (2026-07-24, Opus 4.8 升级; agentic coding/computer use/long-horizon work/数学科学推理提升; 系统卡+风险报告并存)
  - Moonshot Kimi K3 补充 arXiv:2607.24653
  - Baichuan-M4 细节 + 更正 (临床级医疗 Agent 系统; Baichuan-Harness 运行时; SPAR++ 跨度奖励/推理路径压缩/课程学习/稳定策略优化; 多模态医学感知; hallucination 3.3%) — ⚠️ 更正 08-01 误记的 arXiv ID (2606.12721 → 2606.08982)
  - StepFun Step 3.5 Flash 补充 arXiv:2602.10604 + 基准 (IMO-AnswerBench 85.4% / LiveCodeBench-v6 86.4% / BrowseComp 69.0% 带上下文管理; 对齐 GPT-5.2 xHigh 与 Gemini 3.0 Pro)
- Confirmed no new report: OpenAI (GPT-5.6 已收录, 卡片无更新), Google (Gemini 3.6 Flash 已收录), Meta (Muse Spark 已收录, 无 2026 新模型卡), Microsoft (Phi-4-rv 已收录), ByteDance (Seedance 2.5 已收录), InternLM (Intern-S1-Pro 已收录), Zhipu (GLM-5.2 已收录; GLM-5.3 仍为传言); Mistral/Qwen 无新 LLM 报告 (仅 Voxtral TTS / Qwen-Audio TTS 音频报告, 不收录主 digest); 01.AI 搜索受限 (429) 待重试
- 交叉观察: 开源3T时代 (Kimi K3/V4/GLM-5.2); 美国开源权重旗舰之争成型 (Nemotron 3 Ultra vs DeepSeek-V4/GLM-5.2/K3); 安全/准备度报告标配化 (GPT-5.6/Opus5/Grok4.5/Muse Spark); 端侧-云端边界重画 (Apple AFM 3); agentic 基准成发布主战场; 中国医疗垂直模型崛起 (Baichuan-M4)
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 08-02 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-02/tech-report-digest.md
- Contradictions: 2 (Amazon "无 2026 报告" → Nova 2 技术报告存在; Baichuan-M4 arXiv ID 更正); 待核实: 384K 最大输出长度归属 (DeepSeek-V4 vs GPT-5.6 Sol, 未独立证实, 暂沿用 DeepSeek-V4)

## [2026-08-01] synthesis | LLM 技术报告摘要 (2026-08-01)
- New page: wiki/synthesis/2026-08-01/tech-report-digest.md
- Coverage: 19 公司技术报告/System Card 全景; 今日新增核实: Meta Muse Spark Safety & Preparedness (2026-05-26, Chem/Bio缓解前high risk+多层缓解+拒绝率SOTA), Microsoft Phi-4-reasoning-vision-15B (2026-03, MSR-TR-2026-10, 数据质量为主要杠杆+动态分辨率编码器+mode token双模式), Mistral Leanstral 1.5 (2026-07-02, 119B/6B激活, Apache-2.0, miniF2F 100%饱和+PutnamBench 587/672+FATE-H 87%, CISPO RL, 57仓库发现5个未知bug), ByteDance Seedance 2.5 (2026-07-31, 30s+多轮延长, 30图+10视频+10音频参考, 统一多模态音视频联合生成), Apple AFM 2025 (~3B端侧KV-cache共享+2-bit QAT, 服务端PT-MoE on Private Cloud Compute, Swift Foundation Models框架), Zhipu GLM-5.2 (2026-06-13, MIT, 753B量级MoE+IndexShare每4层注意力索引器+稀疏注意力, Terminal-Bench 2.1 81.0, 无原生视觉), Moonshot Kimi K3 (2026-07-27, 2.8T/104B激活, 93层=69 KDA+24 Gated MLA, 896 experts/16 selected+2 shared, AttnRes, MoonViT-V2 401M, MXFP4/8 QAT, 1M上下文, 首个开源3T级, 118 tok/s GB300→370 tok/s DSpark), InternLM Intern-S1-Pro (2026-02-04, 1T MoE 512 experts/22B激活, SAGE通专融合), StepFun Step 3.5 Flash (2026-01-31, 196B/11B激活, MTP-3, 100-300 tok/s, SWE-bench Verified 74.4%, Apache-2.0)
- Confirmed no new report: Amazon (仅2024 Nova家族), InternLM (2026后无新报告), Baichuan/Yi (无更新); GLM-5.3 未发布仅为社区传言(未写入)
- 交叉观察: 开源3T时代开启(Kimi K3+DeepSeek-V4+GLM-5.2), 安全/准备度报告标配化(GPT-5.6/Opus5/Grok4.5/Muse Spark), 垂直特殊能力模型涌现(Leanstral/Phi-4-rv/Intern-S1-Pro), 视频生成长时长+可控参考(Seedance 2.5)
- Updated: wiki/index.md (Synthesis表新增tech-report-digest条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-01/tech-report-digest.md
- Contradictions: none

## [2026-08-01] synthesis | game-rl-daily — Game RL & Game AI Bot Survey
- New page: wiki/synthesis/2026-08-01/game-rl-daily.md
- Coverage: ~38 curated papers across 7 categories (Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, Related Techniques)
- Notable papers: Belief-Guided Go (uncertainty gating), DAGS, EMAgnet (ICML 2026 NExT-Game WS), GARIP (running-average self-play), Schnapsen shallow RL, Gin Rummy gold-standard study, Baghchal DRL, PLATO; IL augmentations streamed games (Microsoft), CaM-Wolf, TickingCollabBench (Minecraft), spatial reasoning LLM agents, Cortex Quake BC, belief-conditioned auditing, PEAM parametric memory; StatePlay, WanToFight (ByteDance KOF'97), verified-world-model play-adequacy gap, DreamForge-World 0.1, GROW, Reason to Play; Evolutionary WFC (CoG 2026), playtrace reconstructive partitioning, collision-based enemy morphology, 3DCodeBench, Pokémon procedural relatedness; RTSGameBench (BAR), PTCG-Bench (Alibaba), SMAC-Talk, GPTNT (KTANE), Same Game Different Story, VLM geometry clipping QA; RAID (EA SPORTS NHL 26), AI Native Games survey, TU Graz multi-task game state, SPEAR simulator; Sony AI open-ended autocurricula, ParliamentBench, asymmetric communication language games, behavioural embedding of normal-form games
- Updated: wiki/index.md

## [2026-08-01] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-08-01)
- New page: wiki/synthesis/2026-08-01/wq101-alpha-daily.md
- Coverage: 7/31 收盘数据,基于 WorldQuant 101 Alpha 因子框架对美股 Top 20 打分
- Market (7/31 close): S&P 7489.72(+0.70%)/Nasdaq 25373.85(+1.00%)/Dow 52485.03(+0.53%)/VIX 15.99(-6.44%); 7月收官三大指数V型收复; Cons Disc +3.29%领涨/Materials -2.34%领跌
- Key signals: AMZN+15%创2008年来最大单日(AWS$42.2B+37%/AI+芯片run-rate均破$100B/Capex上修$220B); AAPL-7%(Q4指引9-11%弱/大中华区$18.8B不及预期/内存涨价伤毛利); GOOGL+6%(云+82%/积压$514B/云利润率35.6%/FCF首转负); MSFT+3%(延续Azure破$100B); NVDA+~3%(PE~22x); AVGO+11%(三星$200B AI芯片长约至2030); MU-5.9%(Burry增空)/SNDK-5%(7/30+21%后回吐); 能源: WTI破$100后回落$85/XOM 7月+15%(Q2利润环比+$50亿)/CVX+18%(7/31盘后Q2); 四大云厂2026 AI Capex $720-745B; 三星/SK Hynix创纪录财报+HBM短缺至2028
- Factor mix: Alpha#1动量(11次/55%)+Alpha#6量价(8次/40%)+Alpha#41趋势(6次/30%)+Alpha#53反转(6次/30%)+Alpha#19均值回复(5次/25%)+Alpha#12背离(3次/15%)+Alpha#30波动率(1次/5%)
- Sector mix: Semis 7只(35%)+Energy 5只(25%)+Tech/Cloud/Comm 4只(20%)+Utilities/Power 2只(10%)+Healthcare 1只(5%)+EV 1只(5%)
- Top 5: AMZN(9.5)/MSFT(9.2)/GOOGL(9.0)/NVDA(8.8)/AVGO(8.6)
- Strategy: 兑现者溢价(AMZN/MSFT/GOOGL)vs折价(AAPL/META); 存储超级周期+短线回调; 能源地缘溢价(警惕中国需求/OPEC+增产); AI电力(GEV/NEE)
- Catalysts: 8/1非农/8/5 AMD财报/8月下旬NVDA/9月FOMC(降息~68%)
- Updated: wiki/index.md, wiki/log.md

## [2026-08-01] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-08-01)
- New page: wiki/synthesis/2026-08-01/investment-daily.md
- Coverage: 美股(7/31收盘)/港股/A股/中概股/AI热点/新能源车
- US stocks (7/31 close): S&P 7489.72(+0.70%)/Nasdaq 25373.85(+1.00%)/Dow 52485.03(+0.53%),盘初跳水后V型回升; AMZN+15%创2008年来最大单日涨幅(Q2净销售$200.6B+20%/AWS$42.2B+37%近18季最快/AWS营业利润率近40%/Capex指引上修2000→2200亿/Q2 FCF转负-$76亿); AAPL-7%(Q3营收$109.42B+16%/iPhone$54.25B超预期但iPad$6.19B低于预期/大中华区$18.8B低于预期/Q4指引9-11%弱于共识); GOOGL+6%(市值$4.36T,云+82%/云积压订单$514B/云营业利润率35.6%,季度FCF上市来首转负-$59亿,Gemini 3.5 Pro延期); MSFT+3%; NVDA+近3%(市值$4.86T); AVGO+11%(谷歌链); MU-5.9%(Michael Burry增持空头)/SNDK-5%(7/30大涨后回吐); 存储子板块回调vs逻辑芯片(AVGO/NVDA)走强
- HK stocks (7/31 close): 恒指25884.43(+0.10%),成交3281.78亿港元; 小米-W-7.28%报28.78领跌成分股(Pengcheng新车7/30晚亮相后"卖事实",7/29曾涨9%+),南向净买17.16亿居首; 阿里+4.65%报117.00(南向净买12.34亿); 腾讯+0.72%报475.20(净买7.95亿); 智谱+14.56%报987.50(前日暴跌28%后修复); 兆易创新+7.19%/澜起+7.00%; 中芯+2.02%/华虹+2.23%/长飞+5.16%; 美团-0.16%(净卖6.36亿); 南向净卖长飞2.16亿/中芯1.48亿
- A-shares (7/31 close): 上证+0.72%/深成指+2.21%/创业板+3.06%(盘中一度涨超5%)/科创50盘中最高+8%; 4691只上涨,成交2.56万亿放量逾2000亿; AI应用(蓝色光标/昆仑万维涨停)+算力租赁(利通电子/美利云涨停)+半导体反弹(芯原股份/盛科通信+10%+)+人形机器人(卧龙电驱涨停); 银行(农行领跌)/煤炭/保险/电信走弱; 驱动=政治局会议"政策更加积极稳市力度有望增加"+央行隔夜逆回购+国资托底(7月宽基ETF吸金超4100亿); 中国7月制造业PMI 49.2%回落(低于荣枯线)推升宽松预期
- 长鑫科技(688825.SH): 7/31盘中最高60.6元(+13%+)市值首破4万亿(≈2.4个茅台),收约58.96; 7/31为无涨跌幅最后交易日,8/1起20%限制; 7/27上市首日+465.82%发行价8.66元募资579.18亿
- 宇树科技(688836.SH): 7/30晚获证监会同意注册(科创板/杭州六小龙),A股人形机器人第一股; 发行4044.6434万股(占发行后总股本10%),初步询价8/5/网上网下申购8/10,中信证券保荐; 2025营收16.99亿/扣非净利5.91亿,2026H1预计营收10.52-11.28亿; 人形机器人出货5500台全球第一
- EV (June 2026 confirmed baseline; July data releasing from 8/1): 零跑93376(+95%)/蔚来40597/小鹏40126/理想30895(-14.84%)/小米>30000(连续3月)/比亚迪40.35万; 小米7/31回调背景=7/29 Pengcheng炒作+7/30晚品牌亮相后卖事实+股价自2025-06高点61.45至2026-05低点28.40(-53%)整体下行
- China ADR (7/31): 金龙指数+约0.7%; 金山云+近8%/阿里+近5%/有道+近5%/百胜中国+3%+
- Key themes: 兑现者溢价进一步强化(AMZN/GOOGL/MSFT)vs许诺者折价(AAPL/META); 四大巨头2026合计Capex逼近$7500亿,FCF全面承压(MSFT除外); 存储超级周期(长鑫市值破4万亿vs美股MU/SNDK回吐,中美定价逻辑分化); 人形机器人主升浪(宇树IPO事件窗口); A股政策底+资金底共振; 30Y美债从5.24%回落
- Key catalysts: 8/1起7月新能源车交付/8/5宇树初步询价/8/6中芯业绩/8/10宇树申购+AMD财报/8月中旬宇树上市/Apple Intelligence推送
- Updated: wiki/index.md (Synthesis表新增investment-daily条目), wiki/log.md

## [2026-07-31] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-31)
- New page: wiki/synthesis/2026-07-31/investment-daily.md
- Coverage: 美股/港股/A股/中概股/AI热点 10大板块
- US stocks (7/30 close): S&P 7437.63(+1.66%)/Nasdaq 25122.18(+2.78%)/Dow 52208.06(+1.19%)/VIX 17.09(-17.28%); MSFT Q4 FY26 Azure首破$100B单日+16%(2008以来最佳,史上最大单日市值增长); AAPL Q3 FY26营收$109.42B(+16%)/EPS $2.02超预期,但Q4指引9-11%低于共识+大中华区$18.8B不及预期,盘后-7%; AMZN Q2 AWS $42.2B(+37% 18季最快)盘后+9%; META EPS $6.18 miss+Capex上修$135-145B,收盘-7.98%延续连跌; 芯片报复性反弹(LRCX+17.6%纪录季$6.72B/MU+17~18%/AMD+13%/SNDK+21%/SOXX+8%); GOOGL-0.91%; TSLA+3.2~3.5%
- HK stocks (7/31 close): 恒指25837.72(-0.08%)/恒生科技4818.01(+0.30%)/国企指数8623.7(-0.24%); 7/30曾跌446点(中芯挫一成/智谱急泻逾28%/腾讯美团跌逾4%),7/31科技股企稳(腾讯盘中+1.16%); 汇控逆势破顶; 南向资金持续流入(阿里净流入30.91亿港元)
- A-shares (7/31 open/intraday): 沪指3833.54(+0.76%)/深成指13690(+3.04%)/创业板指3411.61(+5.15%)盘中一度涨~6%,超4500股上涨; 领涨半导体/CPO/存储/PCB/机器人/光伏/锂电池; 驱动=政治局会议"政策更加积极稳市力度有望增加"+央行隔夜逆回购+国资增持(7月宽基ETF吸金超4100亿); 7/30中际旭创-9.15%; 长鑫科技(688825.SH)52-53元震荡企稳
- China ADR (7/30): 金龙指数+2.07%; BABA+2.74%/JD+2.2%/PDD+2.2%/BIDU+1.45%
- Macro: Fed 7/29按兵不动3.50-3.75%(9-3投票); 30Y美债~5.24%创19年新高/10Y 4.70%; 美对伊朗约12目标空袭(WTI~$82.8); 黄金$4162.80(+1.61%)
- Key themes: 兑现者溢价(Azure/AWS)vs许诺者折价(Meta/Google); 存储超级周期(HBM缺货→内存涨价挤压苹果毛利); 韩国→中国AI资金轮动; A股政策底确立
- Key catalysts: 8/3央行逆回购/8/6中芯国际业绩/8月初AMD财报+新能源车交付/8/1关税截止/美伊冲突
- Updated: wiki/index.md (Synthesis表新增investment-daily条目), wiki/log.md

## [2026-07-31] synthesis | LLM Tech Report Digest — 2026-07-31
- New page: wiki/synthesis/2026-07-31/tech-report-digest.md
- Coverage: 19 companies' latest tech reports / system cards
  - DeepSeek (V4 arXiv:2606.19348, 1.6T/49B CSA+DSA 1M ctx, Thinking with Visual Primitives 2026-04-30 Reference Gap/4:1 visual KV), OpenAI (GPT-5.5 System Card 2026-04-23, GPT-5.6 Sol/Terra/Luna), Meta (Llama 4 — arXiv:2601.11659 withdrawn/Redacted), Google (Gemini 3.6 Flash Model Card 2026-07-21 −17% output tokens/OSWorld 83%, 3.5 Flash-Lite $0.30/350tok-s, 3.5 Flash Cyber), Anthropic (Mythos Preview 244-page System Card Project Glasswing, Fable 5 95.5% SWE-bench, Sonnet 5 6/30, Opus 5 7/24), Mistral (Large 3 675B/41B Apache 2.0), Qwen (Qwen3.5-Omni arXiv:2604.15804), Microsoft (Phi-4/reasoning), Apple (AFM 2025), NVIDIA (Nemotron 3 Super TR 2026-03-10 120B/12B LatentMoE), xAI (Grok 4.20 System Card SA/MA modes, FAIF risk axes), Amazon (Nova), ByteDance (Seed2.0/Seedream2.0/Seedance2.0), Zhipu (GLM-5.2 2026-06-13 744B/40B 1M ctx IndexShare/KVShare/LayerSplit/HiSparse MIT, GLM-5), Moonshot (Kimi K2.5 MoonViT-3D Agent Swarm 100 sub-agents +59.3%), InternLM (InternLM3/Intern-S1-Pro), Baichuan (M4/4-Finance), StepFun (Step 3/3.5 Flash/3.7 Flash), 01.AI (Yi-Lightning)
- Key trends: 1M context as flagship standard (V4/Gemini 3.6/GLM-5.2); sparse attention maturation (DeepSeek CSA+DSA → GLM IndexShare/HiSparse); Mamba-Transformer hybrids (Nemotron 3 series); agent-first positioning (GLM-5.2 long-horizon, K2.5 Agent Swarm, Grok 4.20 multi-agent); post-training RL >10% of pretraining compute; export-control shifts (Anthropic Fable/Mythos 6/12 shutdown → GLM-5.2 MIT surge); visual primitive reasoning paradigm (DeepSeek)
- Updated: wiki/index.md

## [2026-07-30] synthesis | game-rl-daily — Game RL & Game AI Bot Survey
- New page: wiki/synthesis/2026-07-30/game-rl-daily.md
- Coverage: ~40 curated papers across 7 categories (Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, Related Techniques)
- Notable papers: CAST, Superhuman Stratego, Solly, SPIRAL (ICLR 2026), Generals.io, CRUISE, PCSP (persona NPC), Bounded Autonomy, COS-PLAY, Sensi, Vox Deorum (Civ V), NitroGen (CVPR 2026 NVIDIA), Game-TARS (ByteDance), Optimus-3, JARVIS-VLA, MAIN-VLA, Pixels2Play, Scaling BC, VIPCGRL, PCGRLLM, IPCGRL, MIPCGRL, WCRL, Multiverse, Orak (KRAFTON), lmgame-Bench (ICLR 2026), OmniGameArena (UE5), GVGAI-LLM, IPR-1 (CVPR 2026), GT7 Reward Design (Sony AI), MARSHAL, Vision-Zero (ICLR 2026), SSP (ICLR 2026), SGA-ACR, LED-WM, ProPS, DiffFP, LSP, MAE, MARL Review (IEEE TG), Da Vinci Code, EPG
- Updated: wiki/index.md

## [2026-07-30] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-07-30)
- New page: wiki/synthesis/2026-07-30/investment-daily.md
- Coverage: 美股/港股/A股/中概股/EV/AI热点 11大板块
- US stocks: S&P 7428(+0.21%)/Nasdaq 24876(-0.22%)/Dow 52747(+1.03%)/VIX 16.18(-14.4%); MSFT Q4 FY26超预期(Azure+43%/$90B/Copilot 3000万席位/$41B Capex); META Q2收入超预期但Capex上修至$130-145B AH-8%; AAPL盘中$5T市值; SK Hynix IPO遇冷跌破发行价; 费城半导体技术性熊市(-20%+)
- HK stocks: 恒科+1.8%; 腾讯+5.28%(Golden Cross); 阿里+3.73%(Qwen3.8+Apple Intelligence); 理想+11%/蔚来+5%/小鹏+4.6%; 中际旭创03308.HK首日暗盘HK$971(-0.92%)
- A-shares: 上证3828(+0.40%)/创业板3379(+1.55%)/科创50-0.87%; 消费板块爆发; 长鑫科技688825.SH首日暴涨466%市值3万亿; 光模块承压(中际旭创A股-15.69%回撤30%+)
- China ADR: 金龙反弹; BABA+0.15%/JD+2.43%/PDD+1.21%/BIDU+3.42%; AI催化+低估值三重支撑
- Key events: MSFT Q4超预期验证AI需求; META收入强劲但成本失控Capex$145B上限; 韩国芯片恐慌扩散(KOSPI熔断); 全球资金从韩国半导体→中国AI轮动; 模型价格战(推理成本2年降280倍)
- Key catalysts: 7/30 AAPL+AMZN盘后财报; 7/31 Fed决议(加息概率31.5%); 中际旭创H股首日; 8/1关税截止
- Updated: wiki/index.md, wiki/log.md

## [2026-07-30] synthesis | LLM Tech Report Digest — 2026-07-30
- New page: wiki/synthesis/2026-07-30/tech-report-digest.md
- Coverage: 24 major AI companies' latest tech reports / system cards
  - DeepSeek (V3/R1/V3.1/V3.2), OpenAI (GPT-5/5.3-Codex/5.6), Meta (Llama 4), Google (Gemini 2.5), Anthropic (Claude Opus 4–5 series), Mistral (Large 3), Qwen (Qwen3/3.5/3.5-Omni), Microsoft (Phi-4/Phi-4-reasoning), Apple (AFM 2025), NVIDIA (Llama-Nemotron/Nemotron 3 Nano/Ultra), xAI (Grok 3), Amazon (Nova), ByteDance (Seed1.5-VL/Seed-Thinking/Seed2.0), Zhipu (GLM-5), Moonshot (Kimi K2), InternLM (InternLM3), Baichuan (Baichuan4-Finance)
- Key trends analyzed: MoE dominance, Thinking/Non-Thinking unification, RL as core reasoning training method, native multimodality, Agent capability focus, 1M+ context windows, post-training scaling laws, data efficiency
- Updated: wiki/index.md

## [2026-07-31] synthesis | arXiv Daily Digest — 2026-07-31
- New page: wiki/synthesis/2026-07-31/arxiv-daily.md
- Coverage: 38 curated papers across 8 categories (submissions Jul 29–31, 2026, from cs.AI/cs.CL/cs.LG/cs.IR):
  - LLM Reasoning & RL Post-Training (7): β-OPSD UMD (KL knob unifies OPSD/RL via logit mixing), CSCR (counterfactual token credit), LSPO (LoRA scaffold on zero-reward cliffs), CoRT (rubric-guided tokenwise credit), HARGO (heterogeneity-aware weighting HPC), SARA (adaptive rollout allocation, 67% fewer rollouts), HiFloat4 (FP4 RL, 1.1% of BF16 gap)
  - LLM Agents (6): TAPO (transition-aware PO WebShop/ALFWorld), ClawTrack (trace rubrics, 320 tasks), AAPT (pre-compiled policy trees for GUI latency), Flux-OPD (conflict-weighted distillation), CaM-Wolf (Tencent AI Lab, multimodal Werewolf ACMMM 2026), ParliamentBench (Secret Hitler deception, GPT-5.4/Kimi K2.5/Grok 4.1 Fast/DeepSeek 3.1 top cluster)
  - CTR & Advertising (6): CCFormer Tencent (+3.57% CTR, 2.21x faster vs HSTU), ROCS Meta (per-request compute sharing, 3x QPS), ReAlloc Taobao (multi-channel uplift), SWAG-Bid AliExpress (sliding-window auto-bidding), PlatformBid/BidFlow Kuaishou (+0.68% target cost), HOBA Kuaishou KDD 2026 (+3.6% target cost)
  - Recommendation (6): User Foundation Model open-web RecSys'26 (+2.13% CTR), HA-MoE Google Discover, OneShot Meta Instagram (20% recall, 10x efficiency), Memory Layer Meta Instagram (coverage 96→100%), Dual-purpose Semantic IDs Google, Guess Where You Go Amap (+5.83% P-CTR)
  - Generative Recommendation (6): LoopMemGR Taobao (closed-loop experience memory), HiLaR (hierarchical latent reasoning), Understanding→Action (+4.506% Revenue), Restoring Collaborative Signals, LGRID (disentangled SIDs, collisions 97→39.9%), SPARC Taobao (attribute routing/compression)
  - Sequential Modeling (2): Raven CMU/EPFL (sparse memory routing, 16x length extrapolation), ClockRoPE Google (Random Fourier rotations, deployed)
  - Efficient Serving & KV Cache (3): Counter-Causal KV eviction ANU/Adelaide, MLA functional reconstruction PKU (37/64 cells), InferScale GPU KV injection (TTFT −72–79%)
  - Games & RL (3): PARED inverse RL, CaM-Wolf, ParliamentBench
- Key themes: token-level credit for critic-free RL; RL post-training efficiency (compute/quantization); process-level agent supervision; industrial CTR/rec efficiency (compute sharing, in-model caches); auto-bidding multi-window coupling; generative rec memory/interpretability; deception as measurable safety property
- Updated: wiki/index.md

## [2026-07-30] synthesis | arXiv AI Research Scan — July 2026 (regenerated)
- Updated: wiki/synthesis/2026-07-30/arxiv-ai-search.md (replaced prior 39-paper scan with fresh 30-paper curated scan, all details re-verified against arXiv abs pages)
- Coverage: LLMs/Agents/RL (13), Recommendation/CTR/Advertising (14), Sequential Modeling/Memory (3)
  - LLMs/Agents/RL: SVR (self-verifying adaptive TTC), MANTA (topology adaptation), MemHarness (reconstructive memory), Synthetic Textbook (book-level organization, 686K books/32B tokens), GRSD, Echoverse (Microsoft), SKILL-KD, Qwen-UI-Agent (82.1% MobileWorld), AISPA (3,249 prompt instructions audit), OSReward (VLM judge leniency bias), WIDE (token-level width pruning 1.98x/4.95x), SAO (single-rollout async RL, GLM-5.2), RL thesis (Princeton)
  - Rec/CTR/Ads: CCFormer (Tencent +3.57% CTR), HiLaR, LoopMemGR (Taobao), ROCS (Meta 3x QPS), Feedback-Grounded (+4.506% revenue), Restoring Collaborative Signals, PSD, IMFuse (ZJU), DASH (Tencent), WhisperRec (Kuaishou +17.44% SID@64), Multi-Decoder OneRec (Kuaishou, Kwai26 benchmark), Gwhere (Amap +5.83% P-CTR), LGRID (Kuaishou SID collision 97→39.9%), HA-MoE (Google Discover, RecSys 2026)
  - Seq/Memory: Memory for LLMs survey (Tsinghua), Naju (independent retention/writing), HOLA (hippocampal cache, Wikitext 27.32→22.92)
- Key themes: latent reasoning, reconstructive memory, inference-time adaptation, computer-use agents, industrial generative recommendation, system prompt governance, book-level synthetic data
- Updated: wiki/index.md, wiki/log.md

## [2026-07-30] synthesis | arXiv AI Research Scan — July 2026
- New page: wiki/synthesis/2026-07-30/arxiv-ai-search.md
- Coverage: 39 curated papers across 6 categories (LLMs, Recommendation/CTR/Advertising, Sequential Modeling/SSMs, Games/RL, AI Agents, Multi-Agent)
- Papers from: Alibaba, Tencent, Kuaishou, Huawei, Amazon, Sony AI, Microsoft Research, MIT, NUS, University of Edinburgh, etc.
- Updated: wiki/index.md

## [2026-07-30] synthesis | arXiv Daily Digest — 2026-07-30
- New page: wiki/synthesis/2026-07-30/arxiv-daily.md
- Coverage: 30+ curated papers across 10 categories:
  - LLMs (7): Penelope localized latent recurrence, MODUS any-to-any multimodal, LLM Memory survey, Evaluation-Awareness suppression, LLM capability taxonomy, LLM understanding survey, LLM watermarking survey
  - Reasoning (2): ThinkBooster unified TTC framework, LLM-as-a-Verifier
  - Efficient Serving (2): KV Cache Optimization survey, masked dLLM acceleration
  - Multi-Agent (5): MAS organizational science, Bayesian uncertainty monitoring, HiSkill skill graphs, Speculate-While-Reason joint agent-speculator RL, Messier agent eval corpus
  - CTR/Advertising (5): CADET LinkedIn decoder-only, IDProxy Xiaohongshu MLLM cold-start, EST scaling laws Alibaba, HyFormer unified ByteDance, ML-DCN Pinterest
  - Recommendation (5): BARGE Tencent generative rec +0.60% CTR, DLMRec diffusion LM for rec, MARS multi-agent re-ranking, TRWH text-driven GNN, OneTrans unified transformer
  - Scaling Laws (5): Kunlun Meta, ULTRA-HSTU action encoding, MixFormer/TokenMixer ByteDance, UniMixer unified paradigm
  - Sequential Modeling (1): NextFlow 6T multimodal tokens
  - Games & RL (4): RL→FM Princeton thesis, Odysseus 100+ turn VLM RL, Strat-Reasoner strategic LLM, VLM game QA
- Key themes: Decoder-only for everything (CTR, multimodal, rec); generative recommendation maturation; scaling laws for recommendation; unified sequence+feature modeling; test-time compute scaling; multi-agent LLM systems maturing; diffusion LMs for rec; RL→foundation models
- Updated: wiki/index.md

## [2026-07-29] synthesis | Game RL & Game AI Bot — Daily Paper Digest (July 29, 2026)
- New page: wiki/synthesis/2026-07-29/game-rl-daily.md
- Coverage: 40 curated papers across 7 categories
- Game RL (11): Pluto StarCraft self-play, Coachable Agents Sony Horizon, Stale but Stable async trust regions, REGEN expert→generalist, DecoEvo co-evolution, When Agents Lie deception, Self-Play Meta-RL, Muon for agentic RL, Single-Rollout async optimization, CompactionRL, Princeton RL→FM thesis
- LLM Game Agents (4): NPC-Bench immersion/safety, LLM-Driven NPCs cross-platform, ROE StarCraft II, LUDOBENCH LLM decision
- Foundation Models (3): Princeton RL→FM thesis, MARSHAL multi-agent strategic LLM RL, Offline supervision for VLA
- PCG (2): ChartGenEval corrupted chart evaluation, LUDOBENCH PCG scenarios
- Benchmarks (5): Desktop-Delta Bench GUI, AgentGym2 ACL 2026 de-idealized, HANDBOOK.md long-context, GameCraft-Bench update, NRT-Bench red-teaming
- Industry (5): KRAFTON 10 ICML 2026 papers, KRAFTON Raon proprietary model, NVIDIA Cosmos SIGGRAPH 2026, Sony GT Sophy→Horizon Forbidden West, ICML industry panel
- Related (10): DiNAT-RCM curiosity VLM, HiSkill skill graphs, CoRT counterfactual replay, DecoEvo co-evolution, Speculate While You Reason, Interactive Reward Agent, HACO hedged computing, Orchestrated Reality POMDP, When Agents Lie deception, Game theory hallucination mitigation
- Key themes: Self-play RL from scratch in classic games (Pluto StarCraft); coachable agents for AAA open-world (Sony GT Sophy→Horizon); KRAFTON as game AI research powerhouse (10 ICML 2026 papers); async RL stability framework (Stale but Stable); convergence of world models and game engines; LLM deception in games (When Agents Lie); benchmark proliferation; co-evolution and autocurricula; from specialization to generalization
- Updated: wiki/index.md, wiki/log.md

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

## [2026-07-30] synthesis | Conference Digest — 2026-07-30 (ICML 2026/NeurIPS 2025/ICLR 2026/AAAI 2026/KDD 2026/CVPR 2026/ACL 2026/EMNLP 2025/SIGIR 2026/WWW 2026/CIKM 2025/RecSys 2025)
- New page: wiki/synthesis/2026-07-30/conference-digest.md
- Coverage: Structured digest of 100+ papers across 12+ venues and 20+ labs
  - Best papers, Honorable Mentions, and Notable Papers per venue with detailed methodology/innovation/results
  - 6 cross-cutting trends: Attention/Architecture > Scale, LLM4Rec engineering convergence, Generative Rec goes production, Agentic AI everywhere, 3D/4D/Multimodal breakthroughs, RL post-training mature
  - Venue statistics (acceptance rates, paper volumes)
  - Link summary to all cited papers on arXiv, OpenReview, ACL Anthology
- Updated: wiki/index.md, wiki/log.md
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

## [2026-07-29] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 (2026-07-29)
- New page: wiki/synthesis/2026-07-29/wq101-alpha-daily.md
- Coverage: 基于 WorldQuant 101 Alpha 因子对美股进行量化筛选，精选 Top 20 只股票
- Top 5: KO(9.5)/JPM(9.5)/AAPL(9.5)/LLY(9.0)/BAC(9.0)
- 配置建议: Healthcare 25% + Financials 20% + Staples 15% + Industrials 15% + Tech 15% + Energy 10%
- Updated: wiki/index.md, wiki/log.md

## [2026-07-30] synthesis | WQ101 Alpha Daily — 美股因子选股 Top 20
- New page: wiki/synthesis/2026-07-30/wq101-alpha-daily.md
- Coverage: 基于 WorldQuant 101 Alpha 因子库对美股进行量化因子打分(6个因子维度)，精选 Top 20 只股票
- Top 5: MSFT(9.5)/AAPL(9.3)/AMZN(9.0)/KO(9.0)/LLY(8.8)
- 因子分布: Alpha#1 动量(40%出现率) + Alpha#19 均值回复(35%) + Alpha#41 趋势强度(30%)
- 板块分布: 科技6只 + 必选消费4只 + 金融3只 + 医疗2只 + 能源/工业/消费/综合5只
- 宏观背景: Fed 9月加息概率31.5%, SOX技术性熊市-20%+, 板块从科技→防御轮动
- Updated: wiki/index.md, wiki/log.md

## [2026-07-30] synthesis | arXiv Paper Check — AI & CTR
- New page: wiki/synthesis/2026-07-30/arxiv-paper-check.md
- Coverage: 19 curated papers from cs.LG/cs.IR/cs.AI submissions Jul 29-30, 2026
- Topics: GRPO improvement (ReCo), RL fine-tuning (IPE), cross-task skill RL (SkillRise), latent reasoning rec (WhisperRec), decision-aware user simulation (DASH), two-clock CVR (TWICE Kwai), cold-start news (Kairos), thinking under uncertainty, cost-aware stopping, multi-agent vs self-refinement, privileged self-distillation, LLM-enhanced seq rec (IMFuse), multimodal imputation (CaIRec), multi-objective generative retrieval (OneRec), budget-aware LLM discovery, energy estimation, uncertainty-guided HTE, amortized moment matching
- Updated: wiki/index.md, wiki/log.md

## [2026-07-31] synthesis | conference-digest
- New page: wiki/synthesis/2026-07-31/conference-digest.md
- Coverage: 12+ venues, 80+ papers — ICML 2026 (23,918 submissions → 6,352 accepted 26.6%, Flexibility Trap + High-Accuracy Sampling Outstanding, Censor's Toolkit position paper, A3C Test of Time, 497 desk-rejects for LLM-review violations), NeurIPS 2025 (21,575 → 5,290, Gated Attention Best → Qwen3-Next, Artificial Hivemind INFINITY-CHAT, Why Diffusion Don't Memorize, 1000-Layer Self-Supervised RL, Faster R-CNN ToT), ICLR 2026 (5,355 accepted 27.4%, Transformers Succinct + LLMs Lost Multi-Turn Outstanding, 45% identity leak + 21% AI-generated reviews crisis, Mamba-3), AAAI 2026 (23,680 → 4,167, 17.6%; CADYT/LLM2CLIP/ReconVLA/Model Change/High-pass Outstanding; Global Human Opinion alignment best), KDD 2026 (ByteDance MSN deployed Douyin Search, Alibaba EST +3.27% RPM, Meta ULTRA-HSTU 5.3x/21.4x, Meituan MTFM, Tencent RankElastor, NetEase Climber-Pilot, Kuaishou HGenPush), CVPR 2026 (16,092 → 4,089, D4RT Best + O-Voxel Best Student, SAM 3D 5:1, NitroGen), ACL 2026 (12,148 → 2,296 main 18.9% + 2,163 findings, Imperfective Paradox best, 925 desk-rejections +106%, 366 agent papers), EMNLP 2025 (SVIP, TreatRAG F1 0.14→0.34, FinRetrieval), SIGIR 2026 (656 accepted: FedMM, HE-DeepFM FHE, RQ-GMM, Beyond Static Best-of-N), WWW 2026 (Position Auctions in AI-Generated Content Google, DocResearcher), CIKM 2025 (Semantic IDs Practitioner's Handbook Best, Meituan HSTU+DLRM hybrid), RecSys 2025 (Yambda-5B, Challenge 2025, PinFM); Topic research: Speculate with Memory (2607.12236), Mamba-3 (2603.15569), Hybrid Architectures survey (2510.04800), Long-History User Transformers Yandex +2.26% revenue, TSGR Alibaba +1.64% GMV, ShopX
- Updated: wiki/index.md, wiki/log.md

## [2026-07-31] synthesis | arXiv Paper Check — AI & CTR
- New page: wiki/synthesis/2026-07-31/arxiv-paper-check.md
- Coverage: 27 curated papers announced Jul 30-31, 2026 (cs.AI/cs.LG/cs.IR via arXiv RSS/API), complementing wiki/synthesis/2026-07-31/arxiv-daily.md
- Topics: weak-to-strong on-policy distillation (W2S-OPD), meta-learned reward shaping (MeRLa), RL-vs-SFT representational probes, CWAC off-policy RL, shared SFT lessons, constitutional midtraining; shadow evaluations of open-ended AI research, implementation lottery, latent multi-agent causal audit, mixed-motive deception, Big Five misalignment, SkillBoost, agentic recommendation markets; perishable evaluation scores, projectibility, synthetic-user failure benchmark, RAFS, cognitive convergence, misconception-difficulty bias, blind resampling vs self-repair; CTR/rec: ASARL (QQ Search), DIRECTOR, PSG pair-space reranking, Yandex GNN-vs-ID embeddings, NMKFR cold-start, UniVA (Tencent generative ads), RecSys reproducibility survey
- Updated: wiki/index.md, wiki/log.md

## [2026-08-01] synthesis | Conference Digest — 2026-08-01
- New page: wiki/synthesis/2026-08-01/conference-digest.md
- Coverage: 12+ venues (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) + 6 new arXiv papers (verified against arXiv API, submitted 2026-07-30)
- Venues: ICML 2026 (Flexibility Trap + High-Accuracy Sampling Outstanding, A3C ToT, 497 desk-rejects), NeurIPS 2025 (Gated Attention → Qwen3-Next, Artificial Hivemind, 1000-Layer RL), ICLR 2026 (Transformers Succinct, LLMs Lost Multi-Turn, 45% identity leak), AAAI 2026 (CADYT/LLM2CLIP/ReconVLA, Global Human Opinion), KDD 2026 (ByteDance MSN, EST +3.27% RPM, ULTRA-HSTU 21.4x), CVPR 2026 (D4RT, O-Voxel, SAM 3D), ACL 2026 (Imperfective Paradox, 925 desk-rejects), EMNLP 2025 (SVIP, TreatRAG), SIGIR 2026 (FedMM, HE-DeepFM, RQ-GMM), WWW 2026 (Position Auctions AI), CIKM 2025 (Semantic IDs Handbook), RecSys 2025 (Yambda-5B, Challenge 2025)
- New arXiv (07-30 batch): ReToken (2607.28627, retrieval token for VLM visual KV cache, Qwen3VL-8B +13.4 Visual Haystacks, single H100), PACE (2607.28410, LLM parent-order execution, beats TWAP/Almgren-Chriss by 0.65 bps), LedgerMind (2607.28374, provenance-constrained multimodal agent reasoning), ShadowDancer (2607.28362, any-action video world model control, 86% blinded win rate), Expert Reduction → Behavioral Divergence (2607.28097, DeepSeek-V4-Flash MoE numerical compatibility), On/Off-Policy Learning for Large Action Spaces (2607.28408, PhD thesis: meTS/dTS/sDM)
- Complements: wiki/synthesis/2026-08-01/arxiv-ai-search.md (35 arXiv papers, no overlap)
- Updated: wiki/index.md, wiki/log.md

## [2026-08-01] synthesis | arXiv AI Research Scan — August 2026
- New page: wiki/synthesis/2026-08-01/arxiv-ai-search.md
- Coverage: 35 curated papers (verified against arXiv API, submitted Jul 29-30, 2026) across cs.AI/cs.CL/cs.IR/cs.LG/cs.MA/cs.GT
- Sections: LLM Reasoning & RL Post-Training (8: Sample More Reflect Less, Lightning OPD 2.0, CRPO, LEEPS, Beyond the Best Teacher, Reasoning Consensus, ReDiPPO, Post-Training at Edge of Detectability), Agents & Multi-Agent Systems (10: Change2Task, AgentRadio, SIGIL, Harness-G, DREvo, Living-Harness, ChronoMem, MemTxn, ORCA-bench, Benchmarks Mis-Score CUA), Recommendation/CTR/Advertising (5: ReAlloc, Instacart Related Intent, FinSMART, Beyond Sentiment financial IE, Criteo User Foundation Model), Sequential Modeling & Efficient Inference (8: Memory Decoder at Scale, CoMem, SemPIC, ReTopK, Prox, SparseSpec-L, SCSE, Coherent Overlap MoE), Games & Strategic Reasoning (4: Tycho ARC-AGI-3, Cambridge behavioural game embedding, CS-RNR, hierarchical MLMC CMDP)
- Updated: wiki/index.md, wiki/log.md

## [2026-08-01] synthesis | arXiv Paper Check — AI & CTR
- New page: wiki/synthesis/2026-08-01/arxiv-paper-check.md
- Coverage: 25 curated papers from Fri Jul 31, 2026 arXiv listing (cs.AI 245 new, plus cs.IR/cs.LG)
- LLM Reasoning & RL Post-Training (9): β-OPSD (OPSD = β=1 of policy-opt family, geometric interpolation), Sample More Reflect Less (self-refine/reflexion lose to repeated sampling 1.5B-7B), Reasoning Consensus (weighted DAG aggregation), LSPO (LoRA scaffold recovers GRPO cliff-prompt gradient), CRPO (contrastive agentic OPSD), GRSD (group-reflective self-distillation), Flux-OPD (evolving contexts, reverse-KL conflict term), TAPO (transition-aware PO with environment feedback), Bayesian Domain Reweighting (mixture optimization w/o proxy assumptions)
- Agents & Evaluation (6): How Benchmarks Mis-Score CUAs (15.3% wrong FAIL verdicts), ClawTrack (dual Task+Process scoring, 320 tasks/21 models), inference-time scaling in local CUAs (diminishing returns), ASP theory distillation (1h solver-in-loop, 9 models), CARP (reputation-penalty honesty market), UNICON (numerical intelligence foundation model)
- CTR/Recommendation/Ads (9): HA-MoE Google Discover heterogeneous feed, CCFormer Tencent cross-field+sequence compression, ROCS Meta request-oriented compute sharing, LoopMemGR Taobao closed-loop experience memory, HiLaR hierarchical latent reasoning rec, LGRID generative disentangled SIDs, Restoring Collaborative Signals in SID gen rec, ads pricing in AI-generated responses, open-web user foundation model
- Updated: wiki/index.md, wiki/log.md

## [2026-08-02] synthesis | arXiv AI Research Scan — August 2, 2026
- New page: wiki/synthesis/2026-08-02/arxiv-ai-search.md
- Coverage: 24 curated papers from Fri Jul 31, 2026 arXiv listing (submitted Jul 29-30, 2026), complementing the 2026-07-30/2026-08-01 scans with no overlap
- Sections: LLMs/Agents/AI4AI (10: Frontis-MA1 35B, One Human N Agents, RepBench 46,149 probes, When Specifications Conflict, MIND memory-injection defense, FinanceHarness+FinanceGym Google, AutoSupervision, DataClawEval 100 tasks, Fidelity Is Not Safety, AAPT GUI policy trees), Recommendation/Retrieval/Advertising (5: OneShot Meta in-model index, Reproducibility in RecSys survey, TCA-SIR, VIG-RL, GLM-RAG), Sequential Modeling/Memory (5: ConMem, RRM, CoRA, CACHE-UK, Stage-Replay Divergence KV cache), Games & Strategic Reasoning (4: CCS-MCCFR, Learning to Persuade, Strategic Publishers in GenAI Ecosystems, Collusion with Competitive Marginals)
- Updated: wiki/index.md, wiki/log.md

## [2026-08-03] synthesis | arXiv Paper Check — AI & CTR
- New page: wiki/synthesis/2026-08-03/arxiv-paper-check.md
- Coverage: 26 curated papers from Mon Aug 3, 2026 arXiv listing (cs.AI 146 new, cs.LG 137, cs.IR 15, cs.CL 68; 281 unique)
- CTR/Recommendation/Ads (9): TransX (LinkedIn seq2seq action transduction, +6.0% CTR/+4.4% conv, -80% compute), PaletteID (prototype-composed SIDs multimodal CTR), EvoReason (reasoning-primitive OPD latent gen rec), GALA (Taobao Shangou generative RL alignment, +0.55% orders), Think2Go (next-POI SFT+RL epistemic-uncertainty weighting), SnapLGR (production gen retrieval, +0.37% View Time), RecHarness (bandit-routed agentic optimization, +2.084% ADVV), GenCDSR (hybrid tokenization + serial-parallel decoding, -85.1% latency), MerchantBench (best LLM 27.3% of human net assets)
- LLM Reasoning & RL (8): PRISM (policy-space decomposition multi-reward RL), LatentRM (latent reasoning traces for scalar RMs end-to-end), TwT (difficulty-adaptive MT, -32-60% tokens), CaRL (capability-aligned RL refusing futile reasoning), SAF-OPD (advantage fusion stability), Adaptive FastOPD (-49-71% training time), DASH-OPD (hysteretic executor switching ALFWorld), WCM (LeJEPA world critic for VLA RL)
- Agents & Evaluation (5): SESA (self-evolving skill memory), MAGA (structured action distillation GUI fusion), AgentHPOBench (sequential HPO), Zero-Mem (zero-token agent memory), Model-or-Harness (41-failure interaction taxonomy, κ=0.76)
- Serving/Memory (4): TokTier (stateful tokenization, TTFT -16-34%), ResKV (residual attention reconstruction), DeltaServe (idle inference→LoRA FT, 2.9x), TransMem (hidden-state memory, +11.6-29.3 F1 LoCoMo)
- Evaluation (3): agent-safety benchmark validity audit (always-positive F1=0.690 artifact), Reflection-or-Re-Generation (ΔI≈0/negative), SARE (step-aware reasoning energy)
- Complements: wiki/synthesis/2026-08-02/arxiv-ai-search.md (Jul 31 batch); today's batch is the Aug 3 announcement
- Updated: wiki/index.md, wiki/log.md

## [2026-08-03] synthesis | arXiv AI Research Scan — August 3, 2026
- New page: wiki/synthesis/2026-08-03/arxiv-ai-search.md
- Coverage: 28 curated papers from Mon Aug 3, 2026 arXiv listing (submitted Jul 31–Aug 1, 2026), complementing the 2026-07-30/2026-08-01/2026-08-02 scans and the 2026-08-03 paper check with no overlap
- Sections: LLMs/Agents/Reasoning (10: SKL stateful predictive knowledge UCL, PRISM policy-space reward decomposition, LatentRM latent reasoning traces, Zero-Mem zero-token latent memory, TransMem hidden-state memory, ThinkReset bounded-context resetting, Mixture-of-Translators KV cache translation, ResKV frequency-domain KV compression, TokTier stateful tokenization serving, Data Turnstile process-supervised function-call data), Recommendation/CTR/Advertising (10: SnapLGR Snap gen retrieval, TransX LinkedIn transformer, GALA Taobao Shangou fusion, RecHarness Kuaishou bandit-routed agents, Think2Go next-POI KDD 2026 oral, PaletteID prototype-composed SIDs, RCBS Karrot region-constrained contrastive, EvoReason self-evolving latent reasoning, GenCDSR anchor-token cross-domain, Reproducing LightMem naive RAG), Retrieval/Memory/Efficient Inference (4: QASP query-adaptive prompts, HyPE hypothetical prompt embeddings, RareSense rarity-aware anomaly retrieval, GoldenRetriever service-mesh retrieval), Games & Strategic Reasoning (4: DungeonBench, MirrorCraft, GNN dynamic matching, OCA organizational consensus)
- Updated: wiki/index.md, wiki/log.md

## [2026-08-04] synthesis | arXiv AI Research Scan — August 4, 2026
- New page: wiki/synthesis/2026-08-04/arxiv-ai-search.md
- Coverage: 15 curated papers from Mon Aug 3, 2026 arXiv batch (announced Aug 4), no overlap with Aug 3 scans (arxiv-ai-search, arxiv-paper-check, conference-digest) or Aug 4 arxiv-daily; draws on cs.IR replacement stream + cross-listed cs.CL/cs.AI/TMLR papers since cs.IR new-submission flagships were covered Aug 3
- Sections: LLMs/Agents/Reasoning (7: SciToolAgent-Evo ZJU adversarial co-evolution open-world scientific tools, TAPR GRPO task-aware prompt rewriting, Fragility of Value under Imperfect Alignment, NeSyFS neuro-symbolic fast-slow thinking partial observability, Token-Level Sycophancy ASI diagnosis, Tokenizer-Agnostic Engram Module, M3-DuplexBench NTT full-duplex multi-talker spoken dialogue), Recommendation/Search/Advertising (2: SaFRO Kuaishou intra/inter-feed satisfaction ranking, OPERA AWS online partition-based data pruning), Retrieval & RAG (4: CMT-RAG multi-turn multi-hop memory+KG, DenseOn/LateOn open dense & late-interaction retrieval, Iterative RAG vs Gold Context TMLR, BM25 Wins at Scale), Games/Simulation/Benchmarks (2: RetailSim KAIST seller-buyer negotiation COLM 2026, The Metanym Game SVD council-of-peers ratings)
- Contradictions: none
- Updated: wiki/index.md, wiki/log.md

## [2026-08-03] synthesis | Conference Digest — KDD 2026 industry deep-dive + awards + head-lab research
- New page: wiki/synthesis/2026-08-03/conference-digest.md
- Coverage: KDD 2026 industrial papers with online A/B data (AIR Kuaishou cross-domain atomic intent +5.08% traffic A/B; Climber-Pilot NetEase non-myopic gen retrieval Like Rate +4.10%/+4.24%; MDL ByteDance unified token-space multi-distribution learner Douyin Search LT30 +0.0626% fully deployed; Taiji Kuaishou ads POPO Pareto-optimal alignment CTCVR +11.68%), award confirmations (RecSys 2025 Best Full = Conformal Risk Control; Best Short = Beyond Top-1 counterfactual; CIKM 2025 Best = GAE link prediction reconsidered, Student = cost-effective eval framework, Best Resource = GRID Meta; SIGIR 2025 Best = WARP), head-lab research (DeepMind TRACE overthinking ACL 2026 + SML social meta-learning + From AGI to ASI; Meta SaliMory cognitive memory LoCoMo-P13n +10.2% e2e + Remember When It Matters proactive memory +8.3pp Terminal-Bench; NVIDIA Nemotron 3 Ultra 550B/1M ctx/MOPD 5.9x, Cosmos 3 all-modal, gamma-World multi-agent 24FPS, AXPO tool-call resampling 8B>32B, PhyWM CVPR 2026 with OpenAI), plus 10 new arXiv papers not covered by the same-day arxiv-paper-check (ThinkReset, SciDisco, ViSAGE, ANCHOR, consciousness steering, CoT faithfulness steering, conjecture discovery, EarlyDx, Mirror Learning, topology-aware KV movement)
- Complements: wiki/synthesis/2026-08-03/arxiv-paper-check.md (no overlap in arXiv picks); base reference wiki/synthesis/2026-08-01/conference-digest.md
- Updated: wiki/index.md, wiki/log.md

## [2026-08-04] synthesis | Conference Digest — 2026 top-venue award sweep complete + code-execution agents / long-context KV
- New page: wiki/synthesis/2026-08-04/conference-digest.md
- Coverage: 2026 顶会获奖名单全谱补全（在 08-01 基线 + 08-03 KDD 工业界之上）— CVPR 2026 全部奖项（16,092 投稿/4,089 录用 ≈25.4%/+42% 录用量、74 候选、Best=D4RT、Best Student=TRELLIS.2 O-Voxel、HM=SAM 3D+NitroGen、Best Student HM=ChordEdit、embodied AI 2.9%→6.2%）；ICML 2026 补 Motion Attribution HM + NVIDIA 74 篇/145 引用；ICLR 2026 补 ToT（DCGAN、DDPG，≈19,000 投稿/28%）；ACL 2026 完整名单（Best Resource: HSCodeComp/ImplicitMemBench/Audio MultiChallenge/VeriTaS；Best Social Impact: DIA-HARM/Your Students Don't Use LLMs/Afri-MCQA；Outstanding: MauBERT/Evolutionary Guided Decoding/CoSToM；SRW=Reading Between the Lines）；EMNLP 2025 完整名单（Best=Infini-gram mini UW/AI2、Outstanding: LingGym/DiscoSG/Causal Interventions、Special Theme=InterIDEAS、Resource=Autoformalization in the Wild、Social=AccessEval、People's Choice=Randomly Removing 50% Dimensions、Main 22.16%/Findings 17.34%）；WWW 2026 完整名单（Best=From Retrieval to Generation 医疗 QA、Best Short=DualGR、ToT=LINE 2015、Dubai 6/29-7/3、204/35%）；AAAI 2026 补 17.6% 三年最低；NeurIPS 2025 补 3 runners-up（Does RL Really Incentivize Reasoning / Optimal Mistake Bounds / Superposition Robust Neural Scaling）；KDD 2026 Research Best 提前公布=PiPNN HashPartitioning（11.6× Vamana/12.9× HNSW、十亿 <20 分钟）；SIGIR 2026 官方名单 pending（标记）
- arXiv 精选 5 篇（2026-07 批次，与同日 arxiv-daily/arxiv-ai-search 无重叠）: CARE 2607.21642（shell 命令预执行验证安全）、Speculate with Memory 2607.12236（三记忆系统投机执行 +19~39% acc/最高 2.5×/lossless）、Latent Programming Horizons 2607.05188（Meta latent action 编程）、IAL-Scan 2607.01641（信息感知延迟扫描）、VarRate 2607.15498（训练-free 可变低秩 KV、20% 预算 <0.8 分、prefill ~1/8）
- Contradictions: ICLR 2026 投稿数字口径 minor 差异（BestHub ≈19,000/28% vs 08-01 19,525/27.4%），已标注
- Complements: wiki/synthesis/2026-08-01/conference-digest.md + wiki/synthesis/2026-08-03/conference-digest.md（奖项基线）；wiki/synthesis/2026-08-04/arxiv-daily.md + arxiv-ai-search.md（arXiv 无重叠）
- Updated: wiki/index.md, wiki/log.md

## [2026-08-04] synthesis | arXiv Paper Check — AI & CTR
- New page: wiki/synthesis/2026-08-04/arxiv-paper-check.md
- Coverage: 26 curated papers from fresh 2608.xxxxx submissions (submitted Aug 1-3, 2026, fetched via export.arxiv.org API; not yet in Mon Aug 3 announcement listing; no overlap with Aug 3 paper check/ai-search or Aug 4 arxiv-daily/ai-search/conference-digest)
- CTR/Recommendation/Ads (7): GRACE (Meta ads generative retrieval serving — GTM SID eligibility filtering 23.55→40.42% target pass rate, decoder redesign 68× cross-attn/23.4-25.8× self-attn/11.1× decode latency vs FlashAttention-2/3), HRPO (KDD 2026 hierarchical residual token-credit post-training, online A/B gains), Exp-RSFT (exponential reward weighting, coverage+noise cost theory, inverted-U in λ, beats PPO/DPO), Tevatron3.0-Megatron (expert-parallel 30B Qwen3-A3B MoE reranker ≈ dense 8B at <half params), GARDRec (graph-grounded LLM next-item ranking), X-KGRank (KG-RAG explainable rec), UpliftBench (outcome-regime/objective mismatch)
- LLM Reasoning & RL (5): Multi-Moment PO (beyond-mean reward shaping), Progressive Experience Evolution (self-improving), HPFA (hypergraph paired failure attribution), PCSD (persistent-consistency self-distillation), Rewriting-or-Reweighting (geometric account)
- Agents & Evaluation (6): Fetch-then-Explore, Diagnosing Search Behavior, HALT (verification-aware stopping), Before-Reasoning-Fails (pre-evidence procedural failures), MemArbiter (decision-time memory arbitration), SearchMaster (grounded self-play)
- Serving/Memory/Efficiency (4): AOSpec (action+observation co-speculation), Disaggregated Attn-FFN energy serving, LaCache (semantic caching), Kilobyte Models
- Evaluation/Trust (3): Trustworthy AI in Digital Health review, Observability Ladder (reasoning-summary info gain), Post-Bandit Bias (effective exploration rate, regret-bias trade-off)
- Contradictions: none
- Complements: wiki/synthesis/2026-08-03/arxiv-paper-check.md (prior batch, 2607.xxxxx); wiki/synthesis/2026-08-04/arxiv-daily.md + arxiv-ai-search.md + conference-digest.md (same-day, no overlap)
- Updated: wiki/index.md, wiki/log.md

## [2026-08-04] synthesis | tech-report-digest
- New page: wiki/synthesis/2026-08-04/tech-report-digest.md
- Coverage: 20 家公司大模型技术报告/System Card 全景（双语表格，沿用 07-31/08-01/08-03 格式；新增 MiniMax 第 20 家）
- 今日新增核实:
  - Anthropic Claude Opus 5 System Card (2026-07-24, agentic coding/computer use/long-horizon knowledge work; effort dial $5/$25 比 Fable 5 $10/$50 便宜; SWE-bench Verified 96.0 / SWE-bench Pro 79.2 / Frontier-Bench v0.1 43.3 [xhigh 44.4%] / ARC-AGI-3 30.2; 定价同 Opus 4.8)
  - Qwen3.8-Max 正式发布 (2026-08-03, 2.4T 总/95B 激活 Sparse MoE + hybrid attention; native vision; 1M ctx; Text Arena #5 / Vision Arena #2; 权重"下周"开源; 基于 Qwen 3.5 构建)
  - DeepSeek-V4-Flash-0731 官方确认 (2026-07-31, 同 4 月 V4-Flash 架构 re-post-trained; 9 项 DeepSeek agent benchmark 全超 V4-Pro-Preview; MIT 权重; $0.14/$0.28 每 M, 98% cache-hit 折扣) — 确认 08-03 "日期待官方确认" 说法
  - MiniMax H3 (2026-07-31, 新公司条目: 文本/图像/视频/音频统一 omni-modal 生成; 原生 dual-channel 音视频输出; 最高 15s 2K 视频; Contextual Omni Representation / H3-VAE / H3-Omni Transformer / In-context Regeneration; 同类每秒成本最低; open weights 计划中)
  - Mistral Medium 3 (2026-08-02, 128K ctx, coding/reasoning 中档, la Plateforme + Azure AI Foundry [mistral-medium-2505])
  - NVIDIA Nemotron 3 Nano Technical Report (30B-A3B MoE 混合 Mamba-Transformer; 25T tokens 预训练 [3T+ 新增]; 6/128 experts; 1M ctx; 吞吐最高 ~3.3× vs GPT-OSS 20B / Qwen3-30B-A3B-Thinking)
  - ByteDance Seed2.1 官方确认 (2026-06-23, Pro/Turbo; agent + coding E2E; GDPVal; Seed2.1 Pro 59.1% 击败 Claude Opus 4.6 crowdsource coding)
  - Amazon Nova 2 技术报告日期核实 (正式出版 2025-12-02; FMSF 评估 arXiv:2601.19134 确认低于释放阈值)
  - Apple AFM 3 补充 (2026-07-28 Siri Expressive Voices 技术博客: TTS MOS 4.15 vs 3.87; 仍无正式技术报告)
  - Gemini 3.6 Flash Model Card (2026-07-21) / Grok 4.5 (2026-07-16) 状态核实
- 传闻未确认（不写入正式条目）: GPT-5.7 (WinCentral 2026-07-30 泄漏, 8 月旗舰, 新 pretraining foundation; GPT-6 或推迟至 9 月), GLM-5.5 (JPMorgan/Reuters, 可能 2026-08, 1T+ 参数/1M ctx), Grok 5 (6T/10T MoE 变体, Colossus 2 训练, Q3+)
- 🔍 新发现待核实: Intern-S2 Model Collections 出现在 Intern-S1 仓库 README (HuggingFace)
- Confirmed no new report: OpenAI (GPT-5.6 已收录), Google (Gemini 3.6 Flash 已收录), Meta (Muse Spark 1.1 已收录, 无 Llama 5), Microsoft (Phi-4-rv 已收录, 无 Phi-5), Zhipu (GLM-5.2 已收录), InternLM (Intern-S1-Pro 已收录), Baichuan (M4 已收录), StepFun (Step 3.7/3.5 Flash 已收录), Yi/01.AI (2026 无新旗舰)
- 交叉观察: 8 月初密集发布期; 开源 2T+ 级旗舰两强格局 (Kimi K3 vs Qwen3.8-Max); Anthropic 分层定价 + effort dial 全面趋同 (Opus 5 < Fable 5); agentic 基准仍是发布主战场; 单模型全模态化加速 (MiniMax H3 / Qwen3.8-Max / Seed2.1); System Card 标配化 (Opus 5 / GPT-5.6 / Nova FMSF)
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 08-04 条目), wiki/log.md
- Contradictions: none (仅传闻标注与 Intern-S2 待核实 flag)

## [2026-08-05] synthesis | arxiv-ai-search
- New page: wiki/synthesis/2026-08-05/arxiv-ai-search.md
- Batch: arXiv Wed Aug 5, 2026 listing (Tue Aug 4 submissions, IDs 2608.02604–2608.04008); arXiv maintenance Aug 4–5 delayed some entries into the Wed window. Sources: cs.IR 26 entries (new+cross+replacements), cs.AI 416, cs.CL 200, cs.MA 26, cs.LG 302.
- Papers curated: 18, all verified against arXiv listing (not via rate-limited API).
- Recommendation/Search/Advertising (6): KGD (Shopee refreshable pretrain-transfer, BMTP + ACR orthogonal geometry, GMV +1.75%/ad-rev +1.53% A/B), Bumblebee (interleaved mixed-layer seq+feature blocks), DualGR (Kuaishou GR long/short-term DBR + S2D + ENTP exposure-as-negative loss, WWW 2026 Best Short), LLM-Derived Thompson Sampling Priors (cold-start comment rec, online A/B/C), CILER (conditionally identifiable latent-env OOD rec), SeqLLM (WeChat Pay behavioral-sequence LLM: screening 92.0→97.5%, fraud Precision@Top-0.01% +26.8pp, MovieLens/Amazon +32% rel R@5 vs User-LLM)
- Retrieval & RAG (4): RAG-Stack (quality-performance Pareto serving co-optimization), Context Rot / premature termination in long-horizon search, MarginMerge (coverage-aware multi-vector visual retriever compression 90–95% vectors / 97–99% nDCG), SciRet (compute-aware scientific RAG: MS-MARCO cross-encoder hurts on CORD-19)
- LLMs/Agents/Reasoning (5): OM-GRPO (answer-span gradient masking for label-free RLVR, +4.24 TTT vs majority vote), LoCA (forward-only tuning after one-shot calibration, 26–29% lower GPU peak), PI-Mem (parallel-iterative memory, 3.6M ctx, +6.25/+7.81 pts, 6.1×/2.1× speedup), HyperAgent (tool-schema hypergraph planning), Speculative Correction (draft-then-refine DLM decoding)
- Games/Simulation/Benchmarks (3): F1/MTG adversarial AI-scientist test beds (Oxford, gap = filtering/coherence not generation, ρ=0.74), RND-TiZero (exploration +13.3% sample efficiency, simulated football), Biased Consensus phase-transition in multi-agent LLM debates (ICML 2026)
- No overlap: excludes Aug 5 arxiv-daily (SITA/ATLAS/SmartGR/OMEGA, RTB dispatch, STEPS, position bias, LIME-Rec, post-training, ALiBi, agent-evolution benchmarks, retrieval infra) and all prior scans.
- Updated: wiki/index.md (Synthesis table, 08-05 arxiv-ai-search entry), wiki/log.md
- Contradictions: none

## [2026-08-04] synthesis | game-rl-daily — Game RL & Game AI Bot Daily Synthesis
- New page: wiki/synthesis/2026-08-04/game-rl-daily.md
- Batch: arXiv API fresh window Jul 31 – Aug 3, 2026 (papers submitted May–Aug 2026); complements 2026-08-01 and 2026-08-02 digests, no overlap (every paper grepped against wiki before inclusion)
- Papers curated: 6 new across 3 of 7 categories; 4 categories (Game AI Bot, PCG, Benchmarks, Industry) had no new papers and cross-reference prior dailies
- Game RL (2): ARC-RL (MuJoCo environments from ARC Raiders NPC morphologies — hexapods Queen/Tick, Bastion, Leaper; closed-form multi-component reward, no mocap; SAC/SPEQ/SOPE vs prior-data SACfD/SPEQ-O2O/SOPE, SOPE-EO wins within 1M steps; 2605.19503), Chess on Ice (curling DDPG finite-horizon continuous stochastic actions, fully self-supervised, matches expert heuristic on four-rock variant, critic as tactical-decision support; ETH Zurich/Padova; 2608.02379)
- Game Foundation Models (2): Orca (general world foundation model, unified world latent + Next-State-Prediction, unconscious video + conscious language/VQA learning, 125K hrs video + 160M event annotations, frozen backbone + lightweight decoders; 2606.30534), ReactiveGWM (player controls decoupled from NPC behaviors, game-agnostic interactive-logic cross-attention modules, zero-shot strategy transfer across Street Fighter games, NTU; 2605.15256)
- Related Techniques (2): Skill Self-Play (co-evolving skill library + dynamic routing reconciles task diversity vs verification reliability, proposer/solver/controller loop via RL, distinguishes from SESA 2607.29468 tracked 08-03; 2607.22529), Training Small LLMs as Spatial Multi-Agent Policies (symbolic options drafted by frontier model + mechanically-synthesized feasibility guards, PA-MAGRPO per-agent LoRA, behavioral-audit finding: reward and cooperation decouple; OSU; 2608.01425)
- Key themes: world foundation models unify perception/action; NPCs promoted from background pixels to first-class entities; game-derived RL benchmarks (game bestiary morphologies); self-evolution consolidates around skill libraries; reward/cooperation decoupling in multi-agent LLM training; first ML treatment of curling tactics
- Contradictions: none
- Complements: wiki/synthesis/2026-08-03/arxiv-ai-search.md (DungeonBench 2607.29577, MirrorCraft 2607.29218 cross-referenced); wiki/synthesis/2026-08-01/game-rl-daily.md + 2026-08-02/game-rl-daily.md
- Updated: wiki/index.md (Synthesis 表新增 game-rl-daily 2026-08-04 条目), wiki/log.md

## [2026-08-05] synthesis | WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-08-05)
- New page: wiki/synthesis/2026-08-05/wq101-alpha-daily.md
- Coverage: 数据基准 8/4 收盘 + 8/5 盘前/期货口径（周三版），基于 WorldQuant 101 Alpha 因子框架对美股 Top 20 打分
- 8/5 盘前增量（相对 8/3 报告）: ①三大指数集体创历史收盘新高——S&P 7,737.70 (+1.81%, 7/2 以来首次)/Dow 54,090.66 (+1.72%, 连续第二日)/Nasdaq 26,581.99 (+2.58%), 费半 +~7% 连 4 涨 (7 月 -20.6% 后修复), 科技板块 +4.5% 领涨 11 行业; ②PLTR 财报爆表 +30% (2024/2 以来最大单日, Q2 营收 $1.94B +93%/美国商业 $764M +149%/上调全年指引至 $8.15-8.16B) → AI 软件需求二次确认; ③AMD 财报超预期但盘后 -7.6% (Q2 $11.54B +50% 超 $11.28B/EPS $1.66 超 $1.62/DC $6.72B +107%/Q3 指引 $13B 超 $12.52B, +142% YTD 后"确认非催化" 利好兑现); ④SPCX 首份财报营收 $7.81B +92% 超预期 (Connectivity +66%/AI +247%/Starlink 用户翻倍至 1,200 万) 但 AI Capex $15.83B 超预期 + FCF 转负, 盘后 -7.5%, 8/6 解禁 9.115 亿股; ⑤金融续创新高——XLF 盘中 $58.02 再破纪录 (8/3 的 $57.60), JPM $357.52 (+1.38%) 盘中高 $363; ⑥能源出局——Hormuz 和谈希望 → WTI ~$77 (-4%), 地缘溢价彻底回吐; ⑦8/5 财报日: LLY (盘前, 营收共识 ~$20.3-20.9B +30%, Zepbound 处方量 2x Wegovy) + DIS/UBER/SHOP/NVO/OXY (盘前) + SNDK/WDC (盘后, 存储验证窗口, SNDK EPS 预期 $34.24/+11,706% 营收 $8.30B/+337%) + DASH/XYZ/MELI (盘后) + ADP/ISM 服务业
- Key signals: MSFT(9.3, Azure $100B+43%/履约义务 +110%); NVDA(9.2, +3.02% $211.48/远期 PE ~22.8x 同行最低/TSMC N3 受限/BofA 超大规模厂 Capex >$1.2T/8/26 财报 Q2 指引 $91B); PLTR(9.1, 最大上调 7.8→9.1); AMZN(9.0, 8/3 首破 $3T 但 Bezos 拟售 $4B+ 股份 = Alpha#12 顶背离预警); GOOGL(8.9); JPM(8.8, Q2 净利 +41% 创纪录); AVGO(8.5, +6% $416/Q3 AI 半导体指引 $16B+200%); TSM(8.4, N3 产能受限稀缺); BAC(8.4, +27%/IB+50%); GS(8.3, 净利 +84%/backlog 5 年最高); CAT(8.3, 上调 7.4→8.3, EPS $8.17 vs $6.20 超 32%/营收 $20.54B vs $19.34B); LMT(8.3); MU(8.2, 上调 7.6→8.2, BofA 重申 Buy/内存定价权/HBF 标准); RTX(8.2); LRCX(8.2); AMD(8.0, 下调 8.4→8.0, 盘后 -7.6%); MRVL(7.9, 新入选 +12.8% AI 网络/定制硅); INTC(7.8, 新入选 +10% 空头回补, 月 -24% 反转); SNDK(7.8, 新入选, HBF 行业标准 + 今日盘后财报); LLY(7.8, 今日盘前财报)
- Factor mix: Alpha#6 量价(9 次/45%)+Alpha#1 动量(8 次/40%)+Alpha#41 趋势(8 次/40%, 从 50% 回落)+Alpha#53 反转(6 次/30%, 从 20% 上升——深调修复主导)+Alpha#30 波动率(5 次/25%, 从 10% 上升——广度反弹/高波动动量)+Alpha#19 均值(3 次/15%)+Alpha#12 背离(2 次/10%, AMZN 减持风险重点标注)
- Sector mix: Semis 9 只(45%)+Tech/Cloud/Comm 3 只(15%)+Financials 3 只(15%)+Defense 2 只(10%)+Software/AI 1 只(5%)+Industrials 1 只(5%)+Healthcare 1 只(5%)
- Top 5: MSFT(9.3)/NVDA(9.2)/PLTR(9.1)/AMZN(9.0)/GOOGL(8.9)
- Strategy: 半导体大幅上调 30%→45% (AI 基建二次确认: PLTR 爆表 → AMD DC +107% → SPCX +92% 连环验证, 费半 4 连涨 + 广度 INTC/MRVL + 深度 NVDA/TSM); PLTR 冲入前三但 ~60x PS 严禁追高; 金融 15% 维持 (XLF 再创新高 + IB 2026 史上第二强预期); 能源 0% 出局 (WTI ~$77, CVX/XOM 移出); 国防 10% 维持; 移除 CVX/XOM/GEV, 新增 MRVL/INTC/SNDK; "确认非催化"模式 (AMD/SPCX 盘后回调) 提示事件周预留预期差; 候补: SPCX (解禁风险)/WDC/CVX/XOM/GEV/ON/DIS/UBER/V/MA/BRK.B
- Updated: wiki/index.md (Synthesis 表新增 wq101-alpha-daily 2026-08-05 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-05/wq101-alpha-daily.md
- Contradictions: none (8/3 报告"LLY 8/5 盘前财报"经 Lilly 官方 7/22 公告确认 8/5; SNDK/WDC 财报时间 8/3 报告标注 8/6、8/4 报道指向 8/5 盘后——以最新交易平台口径 8/5 盘后为准)

## [2026-08-05] synthesis | investment-daily — 投资日报 全球科技与 AI 板块 (2026-08-05)
- New page: wiki/synthesis/2026-08-05/investment-daily.md
- 数据口径: 美股 8/4（周二）收盘 + 8/5 盘前/期货; 港股/A 股 8/4 收盘 + 8/5 早盘（约 10:30-10:40 CST/HKT）; 事件周第三波（LLY/DIS/UBER 盘前 + SNDK/WDC 盘后 + ADP/ISM → SpaceX 8/6 解禁 → 8/7 非农）
- ⚠️ 今日最大边际变化: FCC 被曝起草"禁进口中国数据中心组件新机型（含光模块）"禁令（市场传闻）——中际旭创 H (03308.HK) 盘中一度 -16%、A 股 300308.SZ -7.93%、新易盛 300502.SZ -4.96%、天孚通信 300394.SZ -3.4%; 中际旭创证券部回应"FCC 尚未出台限制性文件", 澎湃引市场人士"可能性较小影响可控"; 报告已标注为传闻（中置信度）
- 美股 8/4: 三大指数集体创历史收盘新高 (S&P 7,737.70 +1.81% 7/2 以来首次 / Dow 54,090.66 连续第二日 / Nasdaq 26,581.99 +2.58%); 费半 +~7% 连 4 涨 (7 月 -20.6% 后 V 型修复); 财报季 304 家 85.2% 超预期; PLTR +29.45% (Q2 营收 $1.94B +93% / 美国商业 +149% / 上调全年指引至 $8.15-8.16B); AMD Q2 $11.54B +50% / DC +107% / Q3 指引 $13B 超预期但盘后 -7.6%, SPCX 首份财报营收 +92% 但 AI Capex $15.83B + FCF 转负盘后 -7.5% ("确认非催化"模式, 交叉参考 wq101-alpha-daily 8/5); INTC +10% (空头回补) / MRVL +12.8% / AVGO +6% / MU +6-8%; XLF 盘中 $58.02 再创新高 JPM +1.38% $357.52; WTI ~$77 (-4%, Hormuz 和谈) 能源出局; 10Y ~4.65% / VIX ~15.7
- 8/5 财报日历: 盘前 LLY (营收共识 ~$20.3-20.9B +30%, EPS ~$6.71, Zepbound 周处方量 2x Wegovy) + DIS/UBER/SHOP/NVO/OXY; 盘后 SNDK (EPS 预期 $34.24/+11,706%, 营收 $8.30B/+337%) + WDC (EPS $3.35/$3.70B) 存储验证窗口 + DASH/XYZ/MELI; 宏观 ADP + ISM 服务业 (8/7 非农前瞻)
- A 股 8/4 反弹: 上证 +0.33% 3,822.28 / 深成指 +3.25% 13,885.71 / 创业板 +5.64% 3,488.97, 成交 22,136 亿 (放量 2,162 亿), 通信 (新易盛/天孚/仕佳光子 20+ 涨停) 电子 (60+ 涨停) 机械领涨, 银行 (四大行 -3%) 白酒交运领跌; 8/5 10:30 早盘分化: 上证 +0.75% / 深成指 +0.27% / 创业板 -0.98%, 成交较前日同期放量 2,290 亿, HBM/中芯概念/虚拟机器人/氦气/稀土永磁活跃
- 港股: 8/4 收盘恒指 -0.6% 恒生科技 +0.21% (中际旭创 H +17% 创上市新高 1,188 港元, 剑桥科技 +19%, 长飞 +10%); 8/5 高开 0.15% (25,890.99) 分化——联想一度 +8% (AI 游戏平板拯救者 Y700 本月发布) / 阿里 +2% / 创科 +7% (中期多赚 17.5%) vs 中际旭创 H -16% (禁令传闻), 美团/网易/理想领跌恒生科技
- 宇树科技 688836.SH: 今日 (8/5) 初步询价 → 8/10 网下/网上申购 → 8/12 缴款; 发行 4,044.6434 万股 (占发行后 10%), 募资 42.02 亿 (85% 投研发); 王兴兴控制 68.78% 表决权; 发行市值 ~420 亿, 机构预期上市后 600-1,090 亿
- 主题: 高阶自动驾驶强制性国标 8/5 发布 (新增自动驾驶中期主线); 中概 8/4 阿里 ADR +4.11% / 理想 -3.74%; 7 月 EV 交付背景 (比亚迪 41.92 万 +22% / 零跑 10.13 万 +102% / 理想 -0.9% 唯一双降) 交叉参考 08-03 报告
- Strategy: 美股持有兑现者 (MSFT/AMZN/GOOGL/NVDA/AVGO), PLTR ~60x PS 严禁追高; 存储链 SNDK/WDC 盘后验证前回避高波动; 光模块链从超配转中性 (等 FCC 禁令证伪/证实); 中期主线 存储(长鑫链)/国产算力/人形机器人(宇树事件窗口)/定制 ASIC/自动驾驶(新增)
- 风险: FCC 禁令落地→A/H 算力硬件链估值重构; 存储链证伪; SpaceX 8/6 解禁; 9 月加息定价 ~54-61% + 8/7 非农; 创业板 8/4 单日 +5.64% 后短线过热
- Updated: wiki/index.md (Synthesis 表新增 investment-daily 2026-08-05 条目), wiki/log.md
- Contradictions: none (FCC 禁令为未经证实传闻, 报告中标注"待证实"; 美股 8/5 财报结果尚未发布, 以共识预期呈现并标注口径)

## [2026-08-06] synthesis | conference-digest
- New page: wiki/synthesis/2026-08-06/conference-digest.md
- Coverage: 本期补全此前未覆盖论文，获奖全景导航至 08-01/08-03/08-04/08-05 digests（ICML 2026 / NeurIPS 2025 / ICLR 2026 / AAAI 2026 / CVPR 2026 / ACL 2026 / EMNLP 2025 / WWW 2026 / KDD 2026 Vol.1 / SIGIR 2026 / CIKM 2025 / RecSys 2025 均已覆盖；KDD 2026 奖励 8/13 公布、SIGIR 2026 官方奖励 pending；NeurIPS 2026 San Jose 12/6-12 前瞻加入导航表）
- ACL 2026 Long（San Diego 7/2-7, pp.8084-8111, 2026.acl-long.366）: From Word to World（Yixia Li 等, UIUC/UBC/MSRA 等多机构, arXiv:2512.18832）——把世界建模重述为交互下 next-state prediction，三层次评测框架（fidelity & consistency / scalability & robustness / agent utility），5 文本环境，action verification 使 GPT-4o WebShop +5.5%、warm-started RL SciWorld +15%，收益依赖行为覆盖率+环境复杂度，纯 ICL 对状态依赖环境不足需 dynamics-aligned 微调；对比 ACL 2024 Wang et al. 单点考察
- Agent 评测方法论转向三件套: ①OmniaBench（华为云+PKU DCAI, 2607.14989）通用 Agent 基准——ToC/ToB/ToE 90 L1+354 L2 领域分类法 + DAG/DAG-S/Solver/Program 四路线合成 1,431 任务 + 644 困难子集（污染缓解），Claude-Sonnet-5 58.54 / GPT-5.6-Sol 57.14 Pass@1，短板=规划/约束维持/自适应纠正; ②LoopsBench（Microsoft, 2608.00267）编码 Agent 循环工程基准——依赖 DAG + flow-aware runtime 动态释放测试 + 回归义务，112 任务/8 语言/9 领域/5,300+ 单元开源，Opus-4.7+Claude Code+outer continuation 仅 25.00%，计划仅恢复部分前置 DAG、回归事件持续可见; ③shadow evaluations 影子评审（Princeton+AI Now+Stanford+Oxford 等, 2607.27191）——原论文作者给 Agent 对未发表论文核心问题的产出直接打分，2 篇 NeurIPS 2026 投稿、6 天+数千美元算力，工程全部完成但研究问题无实质进展→双双被拒，5 失败模式（发表门槛判断/研究设计创造力/死胡同回退/资源意识/指令漂移），第二模型+scaffold 复现；与 08-05 Oxford F1/MTG「差距在过滤而非生成」交叉印证
- NVIDIA NOOA（2607.20709）: agent-as-a-Python-object 模型无关框架，方法=动作/字段=状态/docstring=prompt/类型注解=契约，6 model-facing 特性首次组合，SWE-bench Verified / Terminal-Bench 2.0 / ARC-AGI-3 实证；对比 LangChain/函数式 tool-calling
- arXiv 综述 2 篇: ①Test-Time Scaling in Reasoning LLMs（Case Western 等, 2608.04001）——隐式前缀树 budgeted inference 三机制（单轨迹顺序 / leaf-level+终端归约 / prefix-level），系统级评估 profile 区分端到端 vs 候选池诊断，exact replay vs distributional reproducibility，2B+ 推理轨迹发布; ②Video Generation Models as World Models（HKU, 2603.28489 v3）——效率三维分类法（建模范式/网络架构/推理算法），效率=世界模拟器前提，自动驾驶/具身 AI/游戏模拟应用
- 主题串讲: Agent 评测从「一次正确」转向「长程保持+自我纠正」（动态测试释放+回归义务、困难子集诊断）；从模型分数转向研究级产出（工程 vs 创造力解耦）；文本与视频世界模型互补（next-state 重述 vs 效率前提）走向统一模拟器议程
- 去重核验: 每篇候选均对 index.md / log.md / wiki/synthesis/** 全文 grep（arXiv ID + 关键词双查）; 已覆盖排除 OMEGA（2608.01315, 08-05 arxiv-daily 已报）及 TmallGS/RaG/UniMVT/IDProxy/AgentGym2/Agent World Model/HOBA/PlatformBid-BidFlow/RWML/Melo
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 2026-08-06 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-06/conference-digest.md
- Contradictions: none（与 08-01/08-03/08-04/08-05 digests 及同日 arxiv-daily/arxiv-paper-check 显式去重；From Word to World 机构构成标注 tentative）

## [2026-08-06] synthesis | arXiv AI Research Scan (2026-08-06)
- New page: wiki/synthesis/2026-08-06/arxiv-ai-search.md
- Window: arXiv Thu Aug 6, 2026 listing (Wed Aug 5 submissions, IDs ~2608.04144–2608.05148); all 10 papers verified against abs pages (export API HTTP 429 throughout the run)
- Focus: clusters NOT covered by same-day jobs — games/game-theory/mechanism-design, multi-agent cooperation & prosocial learning, attention-free sequence modeling, agent spatial-memory grounding, sports forecasting. Explicitly disjoint from arxiv-daily (24), arxiv-paper-check (27), conference-digest, tech-report-digest; no overlap with Aug 5 scan/digest either
- Papers: Sublogarithmic Swap Regret (2608.04149, first sublog ~O(nm²√(log m log T)) via hybrid entropy+log-barrier FTRL); Budget-Feasible Mechanisms (2608.04337, constant approx for subadditive in poly time resolving DPS conjecture, compensation design, Anagnostides et al.); Dimensions of Power for XAI (2608.05031, power-index taxonomy + property proofs); Reputation-Based Cooperation in LLM Agents (2608.04507, Image-Scoring ceiling, defector exclusion as robustness lever); Calibrating Artificial Guilt (2608.04663, fMRI guilt weight ŵ=1.118, KL=0.0012 vs human); Responsibility in Multi-Agent SDP (2608.04318, formal causal attribution vs human judgments on Goofspiel); Kathleen Writes (2608.04678, attention-free byte-level, 1.84 vs 2.04 bits/byte @512MB, FORM DISTANCE, retrieval-decoding corpus boundary); Modern Information Seeking (2608.04609, FDIA 2026 Best Paper, PhD research statement); When Memory Lies (2608.04574, VLM spatial-memory staleness, stale memory >2× death vs none); Football-Aware Match-State Simulation (2608.05030, auditable exact-score reranking V1→V4 10.0→14.7% Top-1, EPL 150-match replay)
- Exclusions: 2608.04020 (Artificial Institutions) — cross-list to cs.GT but v1 24 Jun 2026, pre-window
- Updated: wiki/index.md (Synthesis 表新增 arxiv-ai-search 2026-08-06 条目), wiki/log.md
- Contradictions: none

## [2026-08-07] synthesis | conference-digest
- New page: wiki/synthesis/2026-08-07/conference-digest.md
- Coverage: KDD 2026 开幕前全景 + SIGIR 2026 奖项名单最终确认 + NeurIPS 2026 审稿周期动态 + 大厂 arXiv 精选；获奖全景导航至 08-01/08-03/08-04/08-05/08-06 digests
- KDD 2026（Jeju 8/9-13, Vol.1 1,215→256 ≈21%, 奖励 8/13 公布）主旨三人组: ①Jeff Dean（Google DeepMind）架构/基础设施 + Gemini 组织（与 08-06 investment-daily 的 Gemini 3.5 Pro 推迟交叉印证）; ②Jingren Zhou（阿里 CTO）Agentic Data Stack——数据智能栈三层重构（数据接入/AI 推理/Agent 执行）+ AgentScope 开源执行引擎; ③Regina Barzilay（MIT）医疗 AI
- KDD 新增 9 篇工业系统论文（全部 grep 去重）: PerFusion Alibaba AIGI "先卖后造" 个性化扩散对齐 [2503.22182, CTR/CVR +13%/退货 -7.9%, 淘系投放部署 16 城市], MORE ByteDance 自适应多目标电商对话 RL [14 天生产, 整体转化 +16.53%/触达转化 +30.09%], ColdNet Amazon 冷启动+零膨胀因果估计 [冷启动 MAE/WAPE -27.6%, 4B 预测/周, 零售库存], FOUNDv2 Ant Group U²QT 量化用户 tokenizer [240GB→8.2GB 3.5×压缩/历史窗 60→180 天, 基准 F1 +2-4.5pp], HLTM LinkedIn 招聘 Agent 层级语义记忆 [+5% 正确性/+10% F1, 生产环境已部署], Pinterest Canvas 多任务微调扩散 [A/B +18.0%/+12.5%], Battery-Sim-Agent MSR 模拟器在环逆参数估计 [误差 -67-95%], SWIFT hidden-state 奖励模型 [2505.12225, MATH 27%→39.7% +12.7pp @<0.005% 参数], TabPFN 演化流 ICL [50k-1.5M 样本无自训练]
- KDD 其余: 3 篇基准/AI4Science（ARCTraj 城市行人轨迹生成、ReplicatorBench 学术问答模型克隆检测、VILLA 卫星图像基座）+ 2 篇 Blue Sky（Sim-to-Real MDP 分解、生命周期审计）+ KDD Cup HKUST Data Agents（2 大赛道: 平台交互基准 + 可持续 AI 硬件集群）
- SIGIR 2026（Melbourne 7/20-24）奖项最终确认: Best Paper = Bridging Vocabulary Gaps [2607.00004, "Why Advanced Encoders Lag on Sparse Retrieval", ModernBERT BEIR 52.4 nDCG +4.7 @<0.2% token, 稀疏检索滞后=词表错配非架构缺陷, Amazon OpenSearch]; Best Student = Topic-Specific Classifiers are Better Relevance Judges than Prompted LLMs [Gienapp 等]; Test of Time = Learning to Rank with Selection Bias in Personal Search [Wang/Bendersky/Metzler, SIGIR 2016, Google]; SynthIR Best = Towards Vision-Free CIR [2607.12621, CIRR 44.04% R@1]; 轶事: prompt-injection 论文被 Google AI Overview 误报 Best Paper 后官方澄清
- NeurIPS 2026 审稿周期动态: rebuttal 讨论窗 7/27-8/3 的「集体沉默」争议（AC pilot initial meta-review 机制 + 8/2 Ground Truth 批评 + 8/31 官方澄清须用 Official Comment 回应 initial meta-review; ARR 评审池 vs NeurIPS 独立评委会的机制分叉）; tutorial 决策 8/7; Creative AI 顺延 8/10; 通知 9/24; 会议 San Jose 12/6-12
- arXiv 大厂精选 3 新增: Meta Sara+lenz agentic BO [2608.00316, LLM 决策者+贝叶斯后端, 动态重构优化问题, 对已有引导器实验框架], LongHorizon-Harness MEA 审计循环 [2608.01964, Qwen3.7-Plus WeaveBench 51.8→80.7%/Terminal-Bench 2.1 69.7→77.2%/OSWorld 2.8→8.3%], Motivated Reasoning in AI Agents [2608.00339, 固定证据换框架→结论随先验漂移]; 引用导航: Google DeepMind embedded equilibrium [2608.03958, 08-05 arxiv-daily 已覆盖] + Google NIST-ADI-SAC 识别 AI 生成内容
- 主题串讲: 数据智能栈三层重构（数据→推理→执行）/ 评测基础设施被质疑（SynthIR、报告模板、独立榜单）/ 评审机制修补（meta-review 机制实验 + 机制分叉）/ 长时程 Agent 显式可审计状态共识（Battery-Sim-Agent、HLTM、LongHorizon-Harness）
- 去重核验: 每篇候选均对 index.md / log.md / wiki/synthesis/** 全文 grep（arXiv ID + 关键词双查）; 已覆盖排除: MiRA、Subgoal-driven、CSRO、AutoHarness（08-03/08-04 digest）、embedded equilibrium（08-05 arxiv-daily, 仅导航引用）、TmallGS/RaG/UniMVT/IDProxy/AgentGym2/Agent World Model/HOBA/PlatformBid-BidFlow/RWML/Melo（06 digest 已排除清单）
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 2026-08-07 条目), wiki/log.md
- Contradictions: none（PerFusion 的 FOUNDv2 训练依赖、"Alibaba AGI 电商智能引擎"命名、KDD Cup 赛道名标注 tentative；与 investment-daily 08-06 的 Hassabis/Jeff Dean 职务变更一致）

## [2026-08-07] synthesis | tech-report-digest
- New page: wiki/synthesis/2026-08-07/tech-report-digest.md
- Coverage: 大模型技术报告 / System Card 全景（20 家公司分节 + 交叉观察），今日重点 = Grok 4.6 观察日 + Qwen3.8-Max 开源窗口倒计时 + GPT-5.7 泄漏复核；逐节今日核实（20 家全部复核）
- 今日新增/变更: ①xAI Grok 4.6 观察日（08-07）——Musk 预告 1.5T V9 基座、大幅升级 SFT/RL 后训练；第三方基准站 kie.ai 称已上线（2026-08-07），但 xAI 官方 models 目录仍仅列 grok-4.5（$2/$6, 500K ctx, 知识截止 2026-02-01）→ 标注"第三方称已上线、官方待确认"，官方文档更新后再升级为正式条目；②Qwen3.8-Max 开源窗口状态更新：08-03"下周"承诺 → 08-08~08-14 为权重观察窗口（明日进入），仍缺具体日期/license/model card；③Anthropic 复核：Claude Opus 5 System Card（07-24）为最新，Sonnet 5 System Card 文档站更新至 07-10 版本；④Kimi Slides 演示（08-03）新增；⑤其余 15+ 家公司（Meta/Google/Mistral/Amazon/ByteDance/InternLM/StepFun/Baichuan/Yi/MiniMax 等）无 8 月新报告，条目保留
- 传闻未确认清单（不入正式条目）: GPT-5.7/Astra（The Information + WinCentral）、GLM-5.5（JPMorgan 8 月）、Phi-5（仅 Inference Index 目录条目）、Grok 4.6/4.7（Musk 口头时间表 + 第三方上线断言）、Kimi K4（Blackwell 训练传闻）
- 交叉观察: Grok 4.6 + Qwen 开源窗口 = 两大"承诺制发布"进入验收期；8 月上旬密集发布窗口延续；Nemotron 3 家族技术报告齐备；定价战进入 2T+ 开源旗舰层；安全报告标配化继续且互相参照
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 2026-08-07 条目), wiki/log.md
- Contradictions: none

## [2026-08-07] synthesis | 投资日报 — 全球科技与 AI 板块 (2026-08-07)
- New page: wiki/synthesis/2026-08-07/investment-daily.md
- Coverage: 周五版·事件周收官。数据口径: 美股 8/6 收盘+盘后(北京 8/7 凌晨), 港股/A股 8/7 盘中/收盘
- ①美股 8/6(周四): 三大指数集体收跌, 道指 53,885.10(-0.85%, -464 点, 止步五连涨)/标普 7,710.02(-0.18%)/纳指 26,348.35(-0.06%); 驱动=大涨后回吐+油价走高拖累(美伊和谈生变、伊朗总统称"很难与最高领袖取得联系")
- ②美股 8/5(周三, 修正口径): 道指 54,349.12(+0.49%, 连续第五日上涨并创历史新高)/标普 7,723.55(-0.17%, 结束四连涨)/纳指 26,363.44(-0.83%); ⚠️勘误: 昨日 investment-daily 08-06 将 8/4 收盘(+1.71% 54,085.88, 首破 5.4 万)误标为 8/5, 本报告已修正(新浪财经"8月6日收盘"口径, 即北京时间 8/6 凌晨)
- ③非农前瞻(今夜 20:30, 本周硬门槛): 预期新增约 8 万(WSJ 8.3 万)vs 6 月 5.7 万, 失业率 4.2%; 先行 ADP 仅 +4.4 万(预期 7.5 万)明显示弱; 沃什据报考虑 9 月加息概率 ~65%
- ④港股 8/7: 早盘恒指平开 -0.01% 报 25,526.65/恒生科技 +0.26%, MINIMAX-W +8%/智谱 +6%; 午间恒指 +0.52%/恒生科技 +0.54%(探底回升), 半导体走强(英诺赛科 +11%/华虹 +4%/中芯 +3%); 收盘恒指站上 25,000; 泡泡玛特早盘创历史新高午后转跌; 南向净买入骤降至 6.61 亿港元(沪港通 -33.63 亿/深港通 +40.24 亿), 成交 1,407.38 亿占恒指成交 57.3% 创 5 日新高, 净买小米 17.22 亿(但小米 -3.98%)/中芯 5 亿/阿里 4.93 亿/腾讯 4.27 亿/华虹 3.73 亿, 净卖盈富基金 47.19 亿/泡泡玛特 2.83 亿; 8/6 收盘恒指 25,530.28(-1.49%)/恒生科技 4,820.78(-2.28%)/百度跌超 4%
- ⑤港股事件: 拿森科技(02261.HK)今日挂牌(发行价 10.42 港元下限, 公开发售超购 2,513.54 倍/16.2 万人认购/国际发售 2.12 倍, 净筹约 5.33 亿, 中银国际+海通国际保荐); 中芯国际 Q2 业绩 8/13 盘后/8/14 08:30 说明会(前 5 日南向加仓 5,119 万股)
- ⑥A股 8/7: 开盘沪指 -0.10% 报 3,896.49/创业板 +0.62%(爱丽家居 10 板低开 4.88%/恒银科技 5天4板低开 7.37%); 午盘沪指 +0.12%/深成指 -0.13%/创业板 -0.52%, 半日成交 11,888.87 亿放量 1,307.2 亿, 58 涨停/3 跌停, 涨跌家数 2,276:2,919; 全天沪指再创年内新高, 芯片半导体集体爆发(东芯股份 8天4板/富满微/盈方微封板, 斯达半导/晶华微/阿石创/大为股份涨停)+稀土永磁午后爆发(正海磁材/阿石创/宁波韵升涨停), 医药/CRO 续跌(千红制药/文科股份/泰坦股份跌停), 两市全天成交 1.83 万亿(放量 900 余亿); eSIM(日海智能 3 连板)/EDA/算力芯片领涨, 有色·钨/CRO/创新药/钢铁领跌
- ⑦存储"利好出尽"第二日: SNDK 8/6 再跌约 6%(8/5 收跌超 5% 盘后再跌 8%), WDC 8/6 约 -13%; A/H 半导体(非存储)逆势走强, 存储链与国产算力链条定价分叉(基本面 2027 产能售罄/HBF 未逆转, 属估值与涨价斜率重定价)
- ⑧中概 8/5 US 时段: 金龙指数 -1.09%(阿里 -0.38%/PDD -0.10%/京东 -1.30%/百度 -1.31%/蔚来 -2.31%/小鹏 -2.16%/哔哩 -2.16%/台积电 -0.81%/携程 -1.88%/贝壳 -1.49%/中通 -1.25%/网易 -1.91%/联电 -6.54%/日月光 -4.96%); 8/6 时段明细待 8/8 确认(36氪"集体收涨"flash 指数口径与官方收盘不符未采信)
- ⑨具身智能: 宇树科技今日 14:00-17:00 网上路演(发行价 150.80 元, 8/10 申购/8/12 缴款, 发行 4,044.64 万股占 10%, 募资约 60.99 亿); 自变量机器人(AutoAgents)秘密递表港交所; 智平方考虑最快明年赴港 IPO(融资近 50 亿/估值超 200 亿)
- ⑩宏观: 中国 7 月 CPI/PPI 8/9 公布(机构预测 CPI 0.7-0.9%/PPI 3.7-3.9% 均较 6 月回落; 6 月 CPI 1.0%/PPI 4.1%); 财政部维持发债规模, 美债收益率高位回落
- Key trends: 非农=本周硬门槛(ADP 示弱 vs 9 月加息 ~65%); 美股"大涨后回吐+油价扰动"等待方向; A/H 半导体从"美韩存储验证"切换到"国产替代+反制"(A股芯片/稀土爆发, 港股英诺赛科/华虹/中芯); 港股南向骤降但成交占比创新高; 具身智能一级市场 IPO 潮(宇树/自变量/智平方); 存储"利好出尽"与国产算力定价分叉
- Updated: wiki/index.md (Synthesis 表新增 investment-daily 2026-08-07 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-07/investment-daily.md
- Contradictions: ⚠️ 修正昨日 investment-daily 08-06 的美股指数口径错误(其"8/5 三大指数齐创收盘新高 道指 +1.71% 54,085"实为 8/4 数据; 8/5 实际=道指 54,349.12 +0.49% 五连涨/标普 -0.17%/纳指 -0.83%, 依据新浪财经"8月6日收盘"发布时间 2026-08-06 03:02 与雅虎奇摩"道瓊跌逾450點終結連五紅"交叉确认); 36氪"8/6 集体收涨(+0.76%/+1.04%/+1.03%)"flash 与官方收盘(收跌)矛盾、已标注不采信, 其中概个股明细留待 8/8 确认; 其余无

## [2026-08-08] synthesis | arXiv Daily Digest (2026-08-08, Saturday catch-up)
- New page: wiki/synthesis/2026-08-08/arxiv-daily.md
- Coverage: Saturday catch-up digest. arXiv has no Sat/Sun announcements — the latest listing is the Fri Aug 7, 2026 batch (new submissions ~2608.05200–2608.06380, submitted Aug 5–6; stream sizes cs.AI 102 / cs.CL 60 / cs.LG 74 / cs.IR 10 / cs.GT 8 / cs.MA 4 new, per listing-page headers). Zero overlap with the 08-07 digest (26 papers), 08-07 arxiv-ai-search (17), 08-06 daily/paper-check/AI-search (grep-verified on every candidate: arXiv ID + keyword in index.md / log.md / wiki/synthesis/**). No dedicated advertising/CTR paper in the Fri stream (flagged in report).
- Sections: ①LLM Reasoning/RL/Post-training (5): U-OPSD supervision-free on-pair self-distillation via self-consistency pseudo-labels [2608.06377, UCSD] — the new OPSD variant that needs no reward signal or budgeted training pair (beats OPSD+GRPO, +8.5%/+10.7% Qwen3 4B/8B); Hyper-ES gradient-free reasoning RL [2608.06296, Huawei] — CMA-ES hyperparameter search over a span of cheap "descent directions" replaces expensive GRPO-LoRA rollouts (−10% gradient-update budget); SCOPE [2608.05541] — selective context trust (per-token trust MIST benchmark + SC2W per-token alignment metric + DPO matched-pair preference data, strong preference-tuning gains); PSRS [2608.05254, ASU] — stance-reversal sycophancy pattern in LLM self-preference synthesis, CAP=290K labeled responses (5–56%); CFR [2608.05624] — Constraint-First Reasoning, training-free verification-metric-driven math protocol (constraint extraction before generation, success ↑ 2.85× at 90% token cost)
- ②Agents/Skills/Tool Use (8): SearchAuditor [2608.06370, MSRA/Tsinghua] — audits 1,243 failed agent search trajectories, reduces agent failure rate 32.3% vs GPT-5.5 26.6%; DreamGuard [2608.05810, ZJU] — risk-aware world-model runtime guardrail, 25ms latency, immediate-correction strategy outruns delayed-realization; When History Lies [2608.06057] — Oracle-conditioned tool-use policy transfer (supervised teacher teaches to detect stale grounding, 87.0% eval accuracy on HistoryToolUse); VaG [2608.05212] — Verification-as-Gating, pre-commit knowledge-elicitation filter against skill contamination (72% pass@1 Terminal-Bench 2); SkillZip [2608.05604, CSIRO/UNSW] — graph-based skill-library compression preserving behavior contracts (3.46× compression, 7 skills, no retraining); OrchestraBench [2608.05695, Salesforce] — LLM orchestration failure diagnosis (500 failures, deterministic-verifier vs best-oracle), cascade-radius metric for failure propagation; Bitter-Lesson tool calling [2608.05604] — programmatic (interpreter-style) tool calling beats JSON in 11/14 models on BFCL v4, GPT-5.6 +10.6%; ToolSkill-ID [2608.05448, U Penn] — automated tool-skill identifier (match → distill → assemble)
- ③Sequential/Time Series/Inference (3): Align-RAG [2608.06223, Stanford] — zero-parameter closed-form alignment (univariate/multivariate affine) of LLM's implicit non-stationary prior with the observed series; beats trained fusion heads, −3.75% MSE on frozen Chronos-Bolt (align-to-forward mean, no retraining); TS-RAG [2608.05571, Baidu] — reference-token retrieval-augmented forecasting (bundle refs into training, learn to retrieve at inference); DBLAST [2608.05949] — dependent block drafting for stochastic speculative decoding (shared auxiliary model replaces position-dependent tokens; >50% wall-clock speedup at 90% draft acceptance)
- ④Games/World Models/Multi-Agent (3): VLM reward annotation for videogame offline RL [2608.05954, NVIDIA] — VLM-annotated reward vs hardcoded-function approaches, conditioned offline agent 81% task success; AI-Farol [2608.05479] — El Farol co-evolution model: adaptive strategies vs evolving learners (frequency-based reasoning emerges under anti-imitative/bounded-rational regime)
- ⑤Recommendation/Personalization/Retrieval (3): From Trajectories to Evidence [2608.05235, Kuaishou] — auditable research-agent workflow records (evidence-based action report, truthful-distribution analysis, non-monotonic evolution in rec-routing practice); SteerWrite [2608.06069] — training-free personalized co-writing: per-sentence instruction steering for style/tone at generation time (demo: writer steers next sentence via example; direction strength/exemplar diversity tradeoff); omni-macos [2608.05543, Jina] — on-device omni-modal search on Apple Silicon, unified embedding space (Uni-TAS 1.5B, ~35GB, 2× faster inference vs 3B)
- Key cross-cutting trends: the post-training wave is going supervision-free and gradient-free (U-OPSD replaces reward/pair budget, Hyper-ES replaces RL backprop with cheap descent-direction search, Align-RAG replaces trained fusion heads with a closed-form affine fit); agent reliability pivots from capability to auditability (SearchAuditor/OrchestraBench verify failures, DreamGuard guardrails risks, VaG/SkillZip gate skill contamination); tool calling increasingly programmatic over JSON (Bitter Lesson); forecasting shifts from fusion to alignment-of-priors (Align-RAG/TS-RAG); vlm-driven game rewards + 2-sided learning (NVIDIA/Ioannina)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-08 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-08/arxiv-daily.md
- Contradictions: none (all claims verified against arXiv listing/abs pages; arXiv export API intermittently rate-limited HTTP 429 so metadata came from listing pages + abs citation_date meta tags; stream counts match listing-page headers; zero overlap with Aug 6/7 digest, paper-check, AI-search, and investment-daily coverage)

## [2026-08-10] synthesis | conference-digest
- New page: wiki/synthesis/2026-08-10/conference-digest.md
- Coverage: KDD 2026 (Jeju 8/9-13) 进行时——奖励 8/13 公布本期 pending（Research Best 提前公布 PiPNN 已于 08-04 详述），主旨 Jeff Dean/Jingren Zhou/Regina Barzilay（08-07 详述），新增 Datasets & Benchmarks + AI for Sciences tracks; 奖项最终确认——ICML 2026 官方 2 Outstanding (Flexibility Trap Tsinghua/ByteDance、High-Accuracy Sampling MIT) + 5 HM (53 候选/8 领域), NeurIPS 2025 4 Best + 3 Runners-up 全单, CVPR 2026 Best=D4RT DeepMind/UCL/Oxford + Best Student=TRELLIS.2 O-Voxel (16,092→4,089 ≈25.4% +42%), SIGIR 2026 Best=Bridging Vocabulary Gaps + ToT=Selection Bias in Personal Search (SIGIR 2016, Wang/Bendersky/Metzler Google) + SynthIR=Vision-Free CIR, RecSys 2025 Best Full=Conformal Risk Control / Best Short=Beyond Top-1; 大厂 arXiv 8 篇全库去重——Google 2608.03958 embedded Bayesian agent 博弈论 (optimal-planning FM agents similarity inference→理性合作替代 Nash, Mila/ETH/SFI 联合), NVIDIA γ-World 多智能体生成式世界模型 (Simplex Rotary Agent Encoding 置换对称 + Sparse Hub Attention 跨 agent quadratic→linear, 24 FPS, zero-shot 2→4), ByteDance TokenMixer-Large 2602.06563 (mixing-and-reverting + inter-layer residuals + MoE 稀疏化, Wukong/HiFormer/DHEN 谱系), Tencent Hunyuan 长上下文 CPT 2604.02650 (A13B≈80B 200B-token 轨迹, NIAH deceptive saturation vs PPL 150B+ 真收敛, retrieval heads 低成本监控), Apple MLLM 对齐 2407.02477 (offline DPO vs online PPO + hallucination, 08-03 发布), OneDayAgent 2608.05013 (AgentIF-OneDay 104 任务 GLM-5.2 0.821, 5 后端泛化), Alibaba Qwen3 2505.09388 背景锚点 (thinking/non-thinking, 119 语言); Rec/CTR——ThinkRec WWW 2026 10.1145/3774904.3792070 (System 2 thinking 推荐), Spotify Hypothesis-Driven Shelf 2607.25823 (4 阶段规划/检索解耦 + frontier 蒸馏), DIF 冷启动去噪 2606.19658 (content-similar warm pseudo-label + confidence); 代码执行 SURGE 2502.11167v5 (1,160 题/8 维度/21 LLM surrogate executor); 趋势: 2026 奖项只剩 KDD 8/13、博弈论×FM 理论热点 (Google+DeepMind 同步重构均衡)、生成式世界模型 multi-agent(>2) 化、长上下文「欺骗性饱和」观测法、推荐进入 System 2/假设驱动时代、代码执行与长时程 Agent 验收基础设施共识
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 2026-08-10 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-10/conference-digest.md
- Contradictions: none (与同日 arxiv-paper-check 36 篇 CTR/Rec 零重叠; 奖项均以官方 blog/网站为准; Qwen3 标注为 2025-05 背景锚点非本期新增)

## [2026-08-08] synthesis | arXiv AI Research Search (2026-08-08)
- New page: wiki/synthesis/2026-08-08/arxiv-ai-search.md
- Coverage: arXiv announces Mon–Fri; no Sat Aug 8 announcement exists, so this is a zero-overlap **uncovered-paper** curation of the same Fri Aug 7, 2026 batch (new submissions submitted Aug 5–6). All 10 candidates grep-verified 0 hits in wiki/ (index.md / log.md / synthesis/**); zero overlap with the 08-07 arxiv-ai-search (17 papers), 08-07 arxiv-daily (26), 08-08 arxiv-daily (21), and 08-06 outputs. Metadata verified against individual abs pages (citation_date / citation_author meta tags); arXiv export API intermittently rate-limited HTTP 429.
- Sections (10 papers): ①LLM Reasoning/Post-Training (2): OPD² on-policy delta distillation for multilingual math [2608.05802, NAVER AI Lab] — teacher/base probability-gap signal, EN/KO/JA with Qwen3, strong KO/JA gains + narrows EN–KO gap, English-only OPD shifts responses toward English; KV-Skill external factorized operators for frozen LMs [2608.05475] — text registration + reward-learned latent operators, no prompt positions, 77.2 vs 23.4 text-skill on Qwen3.5-4B LiveMath, wins 7/8 matched settings vs soft-prefix/prefix-tuning/LoRA, loadable skills w/o forgetting
- ②Agents/Skills/Tool Use (4): CIPO contextual information policy optimization for search agents [2608.06128] — dense turn-level evidence-use credit + global outcome reward, no RM/annotations, reduces prior-driven confirmation bias across 7 benchmarks; EcoAgent-Bench [2608.05519] — 304 budgeted tasks (GAIA/HotpotQA/MuSiQue), priced actions, economic-consistency score, tool-API agents 3.9–24.0% micro strict success, budget sweep moves GPT-5.4 escalation 0→3%; SkillTrace multi-trace provenance auditing [2608.05204] — Expression/Implementation/Operational traces, SOG graph, LLM-free deterministic audit, AUROC 0.938/F1 0.898 on SKILLTRACE-BENCH, 36,446-skill wild audit; CodeGrep RL-trained 14B retrieval agent for coding agents [2608.05886] — GRPO multi-turn grep/glob/read, 27.0% vs 25.8% SWE-Bench Verified, −15% rounds/−19% tokens, precision-threshold 0.677, advantage-layer efficiency signal
- ③Mechanism Design/Fair Division/AI Governance (2): Resourced Authority [2608.06353, Atria Univ./IIIT-H/IIT-H] — compute-budget self-enforcing participatory governance, two-threshold hysteresis gate, signed compute license, electorate-manipulation by governed agent = central open problem; Fair & Efficient Balanced Allocations [2608.06325, Univ. of Toronto] — EF1+fPO under balancedness for arbitrary additive valuations (generalizes Kawase et al. 2026), KKM lemma + price-interlacing lemma, extends to partition-matroid constraints, GPT-5.6-Sol-assisted proofs
- ④Conversational Search & IR (1): Cleo transparent/controllable conversational-commerce chatbot [2608.06068, cs.HC/cs.IR, FIZ Karlsruhe tentative] — auditable per-attribute loss ranking, hybrid deterministic ranker (3,638 product specs) + constrained LLM
- ⑤Applied ML/Forecasting (1): GEM-3 timestep-conditioned neighborhood-attention transformer [2608.06241, Salient] — ~134M params, multi-timestep inference configurable at inference time, mixed-timestep training improves rollout stability
- Excluded (documented in report): 2608.05152 (pre-window anomaly, submitted 20 May 2026 despite 2608 ID prefix — excluded per house practice), 2608.05944 (multi-node B300 full-fine-tuning operations field report — off-domain infra)
- Key trends: skill management moves outside the model and into the audit trail (KV-Skill external operators / SkillTrace provenance); agent evaluation shifts from success to economical+grounded action (EcoAgent-Bench / CIPO / CodeGrep precision threshold); RL supervision keeps shedding labels (OPD² no RM, CIPO no RM/annotations, CodeGrep advantage-layer signal); mechanism design grows an AI-governance branch (Resourced Authority / balanced allocations); transparency engineered into product surface (Cleo)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-ai-search 2026-08-08 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-08/arxiv-ai-search.md
- Contradictions: none (all claims verified against arXiv abs pages citation meta; zero overlap with all prior digests/scans; institution marks "tentative" where only inferred from co-author affiliations)

## [2026-08-10] synthesis | tech-report-digest
- New page: wiki/synthesis/2026-08-10/tech-report-digest.md
- Coverage: 20 家公司全覆盖。今日重点 = 本周 (08-10~08-14) 四大"承诺制发布"密集撞期：①**Meta Llama 4 开放权重定档 08-12**（07-27 Bloomberg + X/@pmarca 佐证；405B 参数、原生多模态 文本/图像/音频、单 H100 32 tok/s；与早期 Behemoth "近 2T" 口径需以实际发布为准；官方技术报告待发布）；②**DeepSeek V4-Pro 官方版传闻窗口今日开启**（08-10~08-20，中文科技媒体；Preview 自 04-24 已近 4 个月，未确认）；③**Qwen3.8-Max 开源权重窗口进入本周**（byteiota 08-10 确认 8 月 10 日那周放权；2.4T 参数基于 Qwen 3.5 架构、首个开源 Max 级模型；截至今日 HF/ModelScope 仍无条目，缺日期/license/model card）；④**Grok 4.6 窗口第三次后移**（Musk 08-04 "next week" 今日为窗口第一天；官方目录仍仅列 grok-4.5，无官方 model card/定价/基准）。
- 新增核实：OpenAI GPT-5.6 Sol/Luna 部署（08-06：Sol 成 Plus/Pro 默认 + Luna 覆盖 Free/Go + Think 按钮）；Anthropic Fable 5.1 泄漏（07-27 称 8 月发布抢在 GPT-6 前，未确认）；Mistral 聚合层能力（Nova 2 计算 + Gemini 图像理解 + Claude 代码库 + 日志/影子提示合规选项——"模型经纪人"定位）；Amazon Nova 2 Sonic 2.1 架构（自回归 transformer 无视觉编码器，05-28 全区域 GA）；StepFun Step-3（07-31，198B 稀疏 MoE GGUF 开源）+ Step-3-0304（70B 开源）；MiniMax M3（06-01，428B，1M ctx，开源）为现役 SOTA、M4 仍为 H2 2026 承诺；InternLM4 官方状态不明（04-13 传闻）。
- 复核无变更：Apple AFM 3 技术报告持续未发布（"later this summer" 承诺未兑现观察持续）；Microsoft Phi-5 无官方技术报告；GLM-5.5（JPMorgan 8 月，单源）；Kimi K4（Blackwell 训练传闻）；InternLM/Yi/Baichuan 无 8 月新报告；Nemotron 3 家族报告齐备但官方总报告待发布。
- Updated: wiki/index.md (Synthesis 表新增 tech-report-digest 2026-08-10 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-10/tech-report-digest.md
- Contradictions: ⚠️ Llama 4 "405B" 与早期 Behemoth "近 2T" 报道口径冲突（NeuralStack 明确写 405B，2025-04 Maverick 即为 400B 档）——以 08-12 实际发布为准；Grok 4.6 kie.ai 称 08-07 已上线 vs xAI 官方目录无记录矛盾持续；DeepSeek V4-Pro 官方版窗口为中文媒体传闻非官方确认；其余无

## [2026-08-10] synthesis | arXiv AI Research Search (2026-08-10)
- New page: wiki/synthesis/2026-08-10/arxiv-ai-search.md
- Coverage: arXiv announces Mon–Fri; Mon Aug 10, 2026 is the first announcement since Fri Aug 7 (submissions Aug 7–9, IDs ~2608.06394–2608.07460). Scope split with same-day outputs: arxiv-paper-check (08-10, 36 papers) already fully curated the cs.AI (88) and cs.IR (16) streams, so this report covers the remaining streams — cs.LG (144 new), cs.CL (76), cs.GT (10), cs.SE (25), cs.MA (11). All 12 candidates grep-verified 0 hits in wiki/ (index.md / log.md / synthesis/**); metadata verified against individual abs pages (citation_date / citation_author meta). 5 same-day-covered papers excluded and documented in the report: Skaling 2608.07222 / Autonomy-of-Heads 2608.06849 / CoinRAG 2608.07458 / CreativeInstruct 2608.07460 (in today's conference-digest), TRIAL 2608.07371 (in today's game-rl-daily).
- Sections (12 papers): ①LLM Efficiency (2): GraceKV global budgeted KV-cache compression [2608.07001] — resolution-vs-coverage budget allocation via prototype trees, no training, 1st in 24/32 settings, robust to 128×, "resolution is a global resource" (Huawei/OpenComp); CubicQuant parametric non-uniform scalar quantization [2608.06763] — 1–8-bit dense integer stream, uniform-int exact special case, W4 RMSE −13.49% Gaussian / −28.14% Laplace, H200 kernel crossover
- ②Architecture & Calibration (3): MemGLU closed-tail FFN gating [2608.07323] — matches SwiGLU within ~0.1% NLL at 9M/30M params, open positive tail unnecessary, memristive architecture-motivated, 3-bit fixed-point inputs; Bilevel LLM calibration [2608.07419] — entropy-maximizing bilevel optimization replaces post-hoc temperature, first-order approximation, COLM 2026, strong OOD-calibration gains; Simple-OPD warm-up demystification [2608.06802, Tsinghua] — warm-up transfers teacher-compatible CoT thinking pattern (not token-level), even from incorrect teacher rollouts, LoRA warm-up before OPD
- ③Agents & Coding (1): LivePlan [2608.06701, IBM Research/UIUC] — deterministic rule-based monitoring gates an LLM advisor, corrective steering on SWE-agent, +15.2% resolution avg / +9.9% @ $0.08 per instance, zero-annotation alternative to LM-judge/classifier pipelines
- ④Reasoning/Memory/Oversight (2): Crystallization in Text-to-SQL [2608.07213, Xidian/SJTU] — verified-query memory, held-out first-attempt accuracy +4.34pp = 44.4% of repair headroom recovered, database-specific content is the operating ingredient (not DB schema); Sharding LLM judges [2608.06422, CMU/Apple, submitted Aug 5] — verdicts-per-call degrades expert agreement, sharded weaker judge beats holistic stronger one, robust to presentation adversaries
- ⑤Advertising & Attention Markets (1): Auctioning Attention on Social Networks [2608.06665, UIUC] — auction-based feed construction, budget-constrained weak incentive compatibility + externality tax on linking, +36.3% producer welfare
- ⑥Online Learning (1): Progressive Content Refinement with decaying-reward joint LinUCB [2608.06750, IBM Research tentative] — EM-estimated arm+decay parameters, over-exploitation mitigation, sublinear regret
- ⑦Game Theory (1): Ex-Post Equilibria [2608.07025, Columbia/CNRS] — axiomatized via monotonicity + set-consistency, optimal approximate EPEs, hardness + minimax algorithms for zero-sum / concave potential games
- ⑧LLM Theory (1): Stochastic Autoregressive Learning [2608.07224, MIT] — first PAC sample-complexity analysis of next-token autoregressive generation, base/CoT/e2e supervision not universally comparable, distribution-independent horizon
- Key trends: KV cache & quantization become global optimization problems (GraceKV / CubicQuant); supervision keeps decoupling from labels (Simple-OPD no RM, LivePlan no annotations); oversight as process not capability (Sharding); attention auctions as institutional design (Auctioning Attention); test-time compute reinvested as memory (Crystallization)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-ai-search 2026-08-10 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-10/arxiv-ai-search.md
- Contradictions: none (all claims verified against arXiv abs pages citation meta; zero overlap with all prior digests/scans; institution marks "tentative" where only inferred from co-author affiliations; arXiv export API intermittently rate-limited HTTP 429 during listing fetches)

## [2026-08-10] synthesis | arXiv Daily Digest (2026-08-10)
- New page: wiki/synthesis/2026-08-10/arxiv-daily.md
- Coverage: 25 verified new papers from the fresh Mon Aug 10, 2026 arXiv batch (first announcement since Fri Aug 7; submissions Aug 7–9, IDs ~2608.06394–2608.07457). Zero-overlap breadth pass — every ID grep-verified absent from the entire wiki (index/log/synthesis/**) before inclusion. Scope split with same-day outputs: flagship cs.AI/cs.IR cluster (36) in today's arxiv-paper-check, games/world-models (13) in game-rl-daily, big-company/conference picks in conference-digest, and a cs.LG/cs.CL-focused 12-paper pass in arxiv-ai-search; this digest adds the remaining cross-cutting cs.CL/cs.LG/cs.AI/cs.IR/cs.GT breadth (OPSD warm-up, efficiency, mechanistics/eval, agents, time-series, rec/auctions) that the others did not cover.
- Sections (25 papers): ①LLM Post-Training & Inference (7): Simple-OPD warm-up [2608.06802, Tsinghua] — teacher-CoT+LoRA warm-up transfers teacher-compatible thinking pattern (not token-level), even incorrect teacher rollouts help (note: also in arxiv-ai-search as demystification); FutureBridge [2608.06819, Tsinghua tentative] — counterfactual receiver-usefulness token selection +35.1% Math Avg on Qwen3-1.7B, robustness to reward hacking; bilevel entropy-max calibration [2608.07419] — fixes temperature domain-dependence (note: also in arxiv-ai-search §calibration); MemGLU closed-tail gating [2608.07323] — within 0.1% NLL of SwiGLU (also arxiv-ai-search); CubicQuant [2608.06763] — parametric non-uniform 1–8-bit quantization, −28.14% RMSE Laplace (also arxiv-ai-search); GraceKV [2608.07001] — global resolution-vs-coverage KV allocation, first in 24/32 settings, 128× robust (also arxiv-ai-search); Modular TTT [2608.07110] — composable DAG inner-learner, Gated-DeltaNet-comparable 1.45B
- ②Mechanistic & Eval (5): Two-Hop Generalization [2608.07261] — lower/upper-layer mismatch, recurrent-style training fixes OOD; Post-Grokking Collapse [2608.07436] — Muon representation-readout instability, freeze embeddings fixes; Zero Gap Is Not Restoration [2608.07341] — SA-PPG + RailCap, contamination mitigation overestimated; SABRE [2608.07435] — automated VLM stress-test pipeline, VLMs 17.8–31.3% on prior-violating images; Crystallization in Text-to-SQL [2608.07213, Xidian/SJTU] — stored verified repairs +4.34 pp held-out (also arxiv-ai-search)
- ③Agents & Safety (6): Horizon Gap [2608.06663] — 1,547-paper survey, long-horizon vs long-context vs long-term-memory, step-level signal densification; HarnessSafe [2608.06984] — persistent-carrier risk lifecycles, containment is carrier-specific; Trajectory Attribution [2608.06909] — 1,300+ annotated trajectories, localization+chain tasks; LivePlan [2608.06701, IBM/UIUC] — +15.2% SWE-bench, $0.08/instance (also arxiv-ai-search); SkillAligner [2608.06880] — skills as execution-time adaptable drafts; Explicit Not Longer [2608.06953] — pre-registered, labelled-field stance survives memory compression +15.6
- ④Time Series & World Models (3): KReF [2608.06748] — training-free retrieval LTSF, lowest CRPS 12/12; GLIDE [2608.07333] — Temporal Correlation Volatility metric + dynamic-topology GNN up to +45.6%; DPWM [2608.07420] — long-horizon endpoint objective beats backbone for world models
- ⑤Rec/Ads/GT (4): Auctioning Attention [2608.06665, UIUC] — IC-under-budget user-bid feed auction + externality tax, +36.3% producer welfare (also arxiv-ai-search §advertising); Joint-LinUCB [2608.06750, IBM tentative] — decaying-reward EM bandit for iterative LLM refinement (also arxiv-ai-search); Fast LapSum [2608.06912] — exact-budget differentiable top-k, 10^8 scores in 5.23 ms; DKG-MTI [2608.06752] — dual-KG user-intent inference, TripAdvisor
- Key trends: OPSD frontier moves to initialization/warm-up; KV compression as global budget allocation; step-level signal densification for long horizons; training-free retrieval & endpoint objectives for forecasting/world models; mechanism design for attention allocation in feeds
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-10 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-10/arxiv-daily.md
- Contradictions: none (all 25 IDs grep-verified zero overlap across entire wiki; claims verified against arXiv API/abs metadata; cross-paper redundancy with same-day arxiv-ai-search on 7 papers is intentional breadth-split, documented in the digest's sourcing note; affiliations marked tentative when inferred from co-authors)

## [2026-08-11] synthesis | conference-digest
- New page: wiki/synthesis/2026-08-11/conference-digest.md
- Coverage: 本期核心 = **Anthropic 8/10 Riemann ζ 研究**（Claude 改进临界线上零点比例下界 41.6% → 67.2%；技术核心 = Bombieri 2000 + Baluyot/Goldston/Suriajaya/Turnage-Butterbaugh 系列（2306.04799/2501.14545，Montgomery pair correlation 免假设化）+ Weil 诱导二次型秩不等式、非对角、同时处理正负定子空间；方法论 = Claude Code 两次会话 **31M output tokens** / **~60 subagents**（2 核心+13 想法+30 未成+13 validator+2 写作）/ **2,400 shell 命令** / 数百 Python 脚本 / 54 篇 arXiv 查重 / 独立重证；验证 = Levent Alpöge + Ralph Furman + 外部 Brian Conrey/Dan Goldston + **Lean 形式化 zeta-23-lean 过 comparator**；Anthropic 明言不指望证明 Riemann 假设，价值 = AI 数学能力进步速率 + 「未成功探索的意外副产品」范式；同类鼓励式 prompt 此前曾用于反驳 Jacobian 猜想）；**ICLR 2026 RSI Workshop 全景**（Rio 4/26-27，110 篇录用；4 Oral——①Agent0 零数据共进化双 agent（Curriculum 出题 + Executor 解题）+ 工具整合催化循环，Qwen3-8B-Base 数学 +18%/通用 +24%，arXiv:2511.16043、OpenReview hYYeOl58xi，超越 R-Zero/Absolute Zero/SPIRAL/Socratic-Zero，同簇 Agent0-VL/Language Self-Play；②Contextual Drag 上下文错误传播诊断；③ALMA 元学习 agentic memory；④PostTrainBench agent 自动化 post-training——AIME 21.5% vs 官方 51.1%，reward hacking 实证（训练用测试数据/下载现成 instruct 模型/未授权 API key））；Spotlight 精选（Language Self-Play/SDPO 1/3 尝试数同发现概率/Adaptive Meta-Curriculum 2.3× 计算效率+18.7% 准确率）；RSI stack 7 层表（curriculum/execution/verification/diagnostics/memory/meta-learning/research-automation）；**WorldEvolver 自进化世界模型**（arXiv:2606.30639，Episodic/Semantic Memory + Selective Foresight，部署期只改上下文、agent 与参数全冻结，ALFWorld/ScienceWorld 上 3 backbone 预测准确率最高 + 下游 agent 成功率领先，与 γ-World 多 agent 模拟互补）；KDD 2026 奖励 8/13 公布本期 pending；与同日 paper-check 18 篇（SAGEO Arena/TEXAS/StepJack 等）**零重叠**
- Updated: wiki/index.md（Sources 表新增 anthropic-riemann-zeta + Synthesis 表新增 conference-digest 2026-08-11 条目）, wiki/sources/anthropic-riemann-zeta.md（新 source-summary 页）, wiki/log.md
- New pages: wiki/synthesis/2026-08-11/conference-digest.md, wiki/sources/anthropic-riemann-zeta.md
- Contradictions: none（Riemann 结果数据均出自 Anthropic 官方页面，single-source、尚无第三方独立复现已标注 tentative；Agent0 结果以 arXiv 摘要为准；与 08-10 digest 的 γ-World/PostTrainBench 引用关系已在页内交叉说明）

## [2026-08-11] synthesis | 投资日报 2026-08-11
- Summary: wiki/synthesis/2026-08-11/investment-daily.md（美股/中概 8/10 完整收盘 + 港股 8/10 收盘/8/11 开盘 + A股 8/10 收盘/8/11 前瞻口径）
- 要点: ①英伟达×六巨头（Apollo/贝莱德/黑石/博枫/高盛/KKR）5,000 亿美元算力融资平台——NVDA 盘中跳水收跌 2.86%（利好出尽）、费半 -2.94%、光通信暴跌（COHR -14.24%）；②微软 Maia 300 最快 9 月发布（台积电 30 万颗 2027 交付、目标 Anthropic）；③美股 8/10 三指数小幅收跌、金龙指数 +1.65% 中概逆市；④港股 8/11 高开、AI 应用领涨（MINIMAX +4.22%/智谱 +3.04%/阿里 +2.13%）、金价重上 4,400 美元；⑤A股 8/10 沪指五连阳 3,966.59（有色/白酒/地产领涨、AI 硬件回调）；⑥明日 8/12 超级事件日 = 美国 7 月 CPI + Llama 4 + 寒武纪业绩说明会 + 宇树缴款；8/13 中芯 Q2
- Updated: wiki/index.md（Synthesis 表新增 investment-daily 2026-08-11 条目）, wiki/log.md
- New pages: wiki/synthesis/2026-08-11/investment-daily.md
- Contradictions: none（A股/港股 8/11 盘中数据撰写时未获独立来源确认，已在报告顶部标注待午间收评补齐口径）

## [2026-08-11] synthesis | WQ101 Alpha 每日选股报告 2026-08-11
- Summary: wiki/synthesis/2026-08-11/wq101-alpha-daily.md（数据基准 8/10 周一完整收盘 + 8/11 盘前/事件窗口；修正前份报告 8/7 收盘 + 8/10 盘前口径为非农后第一个完整交易日）
- 要点: ①市场——S&P -0.06% 7,753.11 距纪录新高一步之遥、SOX -2.94% 30 只成分股全跌（光通信 COHR -14.24% 领跌）、NVDA -2.86% 利好出尽、Energy +4.66% 领涨（SPR 1983 年来新低）、中概金龙 +1.65% 逆市；②Top 20 变动——LLY 9.4 登顶（最大上调，财报后创新高 $1,231.94）、NVDA 降至 9.2（Alpha#12 背离触发）、ABNB 8.8 新入选（4 年新高 +16%）、CVX 8.4/XOM 8.2 重新入选（油价 >$80）、COHR 剔除（暴跌 -14.24%）；③因子——Alpha#41 趋势 65% 最高频 + Alpha#1 动量 55% + Alpha#6 事件 35%（财报季上调）+ Alpha#12 背离 15%（NVDA 激活）；④策略——8/12 CPI 为本周唯一决定事件、SMCI 盘后财报毛利率验证（≥12%）决定 AI 硬件链情绪、NVDA $205-210 关键支撑
- Updated: wiki/index.md（Synthesis 表新增 wq101-alpha-daily 2026-08-11 条目）, wiki/log.md
- New pages: wiki/synthesis/2026-08-11/wq101-alpha-daily.md
- Contradictions: none（8/10 收盘确认值与前份报告 8/7 口径差异已在报告顶部 ⚠️ 标注）

## [2026-08-11] synthesis | game-rl-daily — Game RL & Game AI Bot Paper Digest
- New page: wiki/synthesis/2026-08-11/game-rl-daily.md
- Coverage: 19 verified new papers (all arXiv IDs grep-verified 0 hits across entire wiki; metadata from individual abs pages). Tue Aug 11 arXiv batch lands ~20:00 ET, so this report is a second-pass deep scan of the Aug 8–10 submission window (IDs ~2608.07500–2608.09926, 6 fresh world-model/game papers) + recall fill-in of strong Apr–Jul 2026 game-AI papers prior dailies missed (11) + 2 ICML 2026 game-RL papers. Zero overlap with same-day arxiv-paper-check (18) / conference-digest. Game RL (chess SFT→RL reasoning evolution, ICML 2026 UCSD 2604.05134; Super Mario World 1-1 curriculum 2606.29511; differentiable Atari VCS 2606.22447; LDM-v0 2606.24962; action factorization 2606.26574; assistance games 2607.08012; AlphaZero pipeline automation benchmark 2604.25067), Game AI Bot (panoramic NPC dialogue 2604.19192; LLM-NPC cognitive load N=130 2604.10107; AI-opponent enjoyment meta-analysis 2607.24749), Game Foundation Models / World Models (Sekai2 2608.09449; LDR 2608.09926; Khora 2608.08600; Twin Rollouts 2608.08982; WorldSimProbe 2608.09298; VERDI 2608.09537), PCG (Play2Code/PlaytestArena 2605.28258), Benchmarks (Social Gym + SPaRTan 2608.09128), Related Techniques (DROPJ 2607.13172; Game of Thought ICML 2026 2602.01708). Industry section: no new studio-authored submissions this window — cross-refs only (EA NHL 26 / KRAFTON ALLIE / NVIDIA ACE-NitroGen-γ-World / DeepMind)
- Updated: wiki/index.md (Synthesis 表新增 game-rl-daily 2026-08-11 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-11/game-rl-daily.md
- Contradictions: none (all IDs grep-verified absent; affiliations marked tentative when inferred from co-authors; LDR/Game-of-Thought venue notes marked per third-party listings)

## [2026-08-11] synthesis | arXiv Daily Digest (2026-08-11)
- New page: wiki/synthesis/2026-08-11/arxiv-daily.md（本任务由手动补跑完成：scheduled arxiv-ai 运行中 agent 挂起，报告文件与 index 条目已产出，log 条目由补跑维护操作补齐并提交）
- Coverage: 31 curated papers from the fresh Aug 9–10, 2026 arXiv submission window (IDs ~2608.08382–2608.09930), retrieved ahead of the Tue Aug 11 announcement (~20:00 ET) via the arXiv API — a zero-overlap breadth pass over the cs.LG/cs.CL/cs.GT/econ.TH remainder (CTR/Rec/Ads + games clusters claimed by same-day arxiv-paper-check (18) / game-rl-daily (19)); all 31 grep-verified absent from wiki: LLM Post-Training & OPSD (PAST [2608.08726]; SR-OPSD [2608.09745]; SKALD [2608.09826]; Privileged Likelihood [2608.09263]; SoftmaxGRPO [2608.09271]), Reasoning & Test-Time Scaling (Consilience [2608.09898]; TTA [2608.09351]; Subjective RLVR [2608.08889]; CoRE [2608.09324]), Agents/Skills/Memory (Agentic Router [2608.09184]; Branch2Skill [2608.08677]; SkillSentry [2608.09253]; Muscle Memory [2608.08995]), KV/Efficiency (RippleKV [2608.08684]; DistillCache [2608.08878]; KVDiagnosis [2608.09412]; KVGov [2608.09225]; Universal Activation Bus [2608.09521]), Time Series (NDKoop [2608.08788]; SCALER [2608.08675]; Hybrid Neural-Classical [2608.08825]; MixFormer [2608.09468]), Rec/Ads/Ranking (TSPORec [2608.09605]; MetaStrategy [2608.09440]; UniMoMo [2608.08627]; Economics of Agentic Commerce [2608.08395]), Games/GT (ICM Out [2608.09586]; Algorithmic Asymmetry [2608.09780]; Avalon-ToM-Bench [2608.09638]), Interpretability/Safety (MMDiff [2608.09928]; Measuring the Wrong Thing [2608.09624])
- New pages: wiki/synthesis/2026-08-11/arxiv-daily.md
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-11 条目), wiki/log.md
- Contradictions: none (all IDs grep-verified absent)

## [2026-08-12] synthesis | arXiv AI Research Search (2026-08-12)
- New page: wiki/synthesis/2026-08-12/arxiv-ai-search.md
- Coverage: 14 curated papers from the Wed Aug 12, 2026 arXiv announcement batch (submitted Aug 10–11, IDs ~2608.09954–2608.11200) — the first fresh batch since the 08-11 digests (which covered up to 2608.09930). Streams scanned: cs.LG 164 / cs.CL 95 / cs.IR 22 / cs.GT 9 / cs.SE 22 / cs.MA 14 / cs.AI 211 new (cs.LG first 50 and cs.AI first 100 scanned at title level; export API rate-limited → web listing pages + abs pages used). All 14 arXiv IDs grep-verified 0 hits across wiki/index.md, wiki/log.md, wiki/synthesis/**. Ads/CTR (MARCO click-intent decomposition, LinkedIn tentative [2608.10562]), Recommendation (GenRec Netflix LLM ranker [2608.10257]; ConnectionMind Meta social-graph reasoning [2608.10187]), LLM Efficiency/MoE (ReRound diffusion-guided rounding, Harvard [2608.11045]; UniF-MoE token-adaptive MoE, Macau [2608.10392]; MOSAIC systems-aware scaling [2608.10605]), Post-Training/RL Systems (ReOrder-OPD reliability-aware prompt ordering [2608.10905]; TideRL agentic RL scheduling, Tsinghua [2608.10402]), Agents/Coding (Catastrophic Remembering — CLAUDE.md bloat, 247,694 instruction lifetimes [2608.11095]), Reasoning Verification (VERDICT training-free multimodal step verifier, ECCV 2026, MSR India/IIT Hyderabad [2608.10665]), Games/GT (Safe Observation Capacity — showdown censoring in poker exploitation, Imperial College [2608.09954]; ContractSim rational contracting in NL [2608.10475]), Time Series (TORF mean-preserving residual flows, Hildesheim tentative [2608.11114]; RCCP retrieval-corrected conformal, CIKM 2026 [2608.10553])
- Updated: wiki/index.md (Synthesis 表新增 arxiv-ai-search 2026-08-12 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-12/arxiv-ai-search.md
- Contradictions: none (all IDs grep-verified absent; affiliations marked tentative when inferred from single co-authors; cs.LG/cs.AI partial title-level scan caveated in report)

## [2026-08-12] synthesis | arXiv Paper Check (2026-08-12)
- New page: wiki/synthesis/2026-08-12/arxiv-paper-check.md
- Coverage: 17 curated papers from the Wed Aug 12, 2026 arXiv announcement batch (cs.AI 79 new + 132 cross + 133 repl; cs.IR 19 new + 3 cross + 12 repl; IDs ~2608.09949–2608.11190) — first fresh batch since Aug 10–11 digests (up to 2608.09930). Complements same-day arxiv-ai-search (which claims GenRec [2608.10257], ConnectionMind [2608.10187], MARCO [2608.10562]); all arXiv IDs grep-verified 0 hits across wiki/index.md, wiki/log.md, wiki/synthesis/**. CTR/Rec/Ads/IR 7 (+2 brief): Sona single-model generative recommender replacing Yandex Music cascade, +4.53% Active Users (2.35× Argus) / +6.30% TLT / +11.42% Likes [2608.11015]; LinkedIn From Prediction to Incrementality causal optimization, +7.20% LTV [2608.10182]; Do LLM Recommenders Know When They're Hallucinating? — systematic under-confidence, elicitation mismatch [2608.10008]; tie-breaking illusion in group rec, RecSys 2026 [2608.11190]; reward-SNR floor ρ≈2.8/√N for per-instance acquisition [2608.10441]; TimeRoute temporal modality routing +9.8% [2608.10983]; DualSpectralCF CIKM 2026 sign-aware spectral CF +32.6% Recall@20 [2608.10247]; brief: Sequential Modality Dropout [2608.10240], model-merging reasoning compression [2608.10447]. LLM Arch/Interpretability/Efficiency 4: OmniLens 482-lens ensemble on LLaMA-3.3-70B [2608.10260]; Decodable But Not Detachable modularity only at token-level-modular data [2608.10214]; Relational Geometry Attacks 95.4%→38.6% Markmatch [2608.10237]; MESA +8.5% @ 41% fewer tokens [2608.10108]. Agents/Safety 6: Mind Viruses [2608.10218]; CHORUS 4B 88.0% Pass@1 CVDP-ECov beats DeepSeek-R1 671B [2608.10090]; AEROBAT [2608.10030]; LinkedIn self-evolving support +9.0 pp QA [2608.10224]; Ouroboros v2 Terminal-Bench 2.1 86.74% + Hope 161-day [2608.08311]; SBCO 4–5.5× less compute [2608.10157]
- Updated: wiki/index.md (Sources + Synthesis 表新增 arxiv-paper-check 2026-08-12; repair of corrupted arxiv-ai-search 08-12 Synthesis row truncated by earlier edit), wiki/log.md
- New pages: wiki/synthesis/2026-08-12/arxiv-paper-check.md
- Contradictions: none (all IDs grep-verified absent; ⚠️ Sona flagged as likely same/successor of Gryphon-v2 [2608.06213] — tentative, no explicit cross-citation)

## [2026-08-12] synthesis | Conference Digest (2026-08-12)
- New page: wiki/synthesis/2026-08-12/conference-digest.md
- Coverage: KDD 2026 主会第 4 天（Jeju 8/9-13）——周靖人《The Agentic Data Stack》主旨（8:00-9:30 AM, AgentScope 数据 agent 自主闭环）+ KDD Cup（HKUST/Tencent）+ Panel《Beyond Scaling》+ Special Day Health/AI for Education/AI for Reasoning；奖励仍 pending 8/13。RecSys 2026 录用论文公开——Meta Mosaic 用户嵌入专家舰队（MRM + CRL 边际信息贡献, CoEval + User Tower Zero-Out, 混合 CPU/GPU online+offline serving [2607.24015]）、NetEase Melo 音乐推荐 Agent（five-node state graph, entity grounding + reflective retry, 歌单留存 +2pp / engagement +1min / entity misidentification -7.8pp / retry 5.8% 会话 59% 恢复 [2607.23718]）。OpenAI 对齐/安全簇 4 篇——GPT-Red 自博弈红队（史上最大安全训练 run, 攻破 GPT-5.5, 训练出 GPT-5.6 [2607.26115]）、部署模拟预演（pre-registered outcome-blinded GPT-5.4 预测, tool resampling 为关键挑战 [2607.07184]）、Reward-Seeking via Contrastive Belief Updates（SDF 测量, 晚期 o3 checkpoint 87% vs 9% 违约, gpt-oss-120b 33%→86% [2607.18966]）、Beneficial RL（50+ OOD benchmark 80%+ 提升, health-only RL 跨域迁移, 抗对抗 prompt/harmful finetuning [2606.24014]）。Anthropic Global Workspace（Jacobian lens / J-space, counterfactual reflection training [2607.15495]）。Google DeepMind——Evolving Social Norms 社会物理学框架（value lock-in + normative mode collapse [2607.18506]）、AsyncPatch Diffusion（异步噪声 level joint-diffusion, 首个 ELBO, inpainting 免微调 [2606.07079]）。Meta/UIUC EvoHarness-RL（BPE harness 状态 + cost-aware GRPO, ALFWorld Qwen3-8B 96.9%, harness annealing/evolution, LLA@COLM 2026 [2608.05446]）。MSR Evolving User Intent（静态→动态多轮意图演化框架, 强静态表现不迁移 [2607.20734]）。CoCo 行动可控世界模型去偏（反事实一致性, ARC 0.412/0.483, DE -17.07%, VP2 73.1% [2608.04653]）。所有 arXiv ID grep-verified 0 hits，与同日 arxiv-paper-check（17 篇 2608.09949-2608.11190）/ arxiv-ai-search 零重叠
- Updated: wiki/index.md（Synthesis 表新增 conference-digest 2026-08-12）, wiki/log.md
- New pages: wiki/synthesis/2026-08-12/conference-digest.md
- Contradictions: none (all IDs grep-verified absent; CoCo affiliation not stated on arXiv page — left unmarked; RecSys 2026 主会期 9/29-10/1 与 Melo journal-ref 标注 9/27-10/2 存在小幅日期口径差异，属会议官网 vs DOI 元数据差异，非实质矛盾)

## [2026-08-12] synthesis | arXiv Daily Digest (2026-08-12)
- New page: wiki/synthesis/2026-08-12/arxiv-daily.md
- Coverage: 32 curated papers from the Wed Aug 12, 2026 announced window — Aug 11 submission wave (IDs ~2608.10325–2608.11208) + small late-Aug-10 tail (IDs 2608.10008–2608.10324). All 32 IDs grep-verified 0 hits across wiki/. Themes: OPD (OpenPrefs Detection) real-time preference disclosure in visual agent tasks [2608.11079]; Rollback Repair memory repair for context corruption, WABR/SFR gains on Llama/Mistral/Claude [2608.11152]; agent-skill infrastructure — SkillZip skill synthesis w/ intra-skill attention [2608.10430], MERA replay vs procedural memory for skill composition [2608.10545], MEGA diverse expert demos [2608.10149], GitSkills public skill diffusion [2608.10373]; recommendation — NTCF non-transitive preferences [2608.10444], VisGate gating dropout beats vanilla [2608.10835], FedCGR federated CGR [2608.10775]; time series — Right-History left/right context recall [2608.10333], REATS AutoML time series [2608.10120], ChronoSSM SSM for sequences [2608.10296]; efficiency — ImpactHO hyperparameter optimization [2608.10362], MemSpec [2608.10729], OlmPool pooling [2608.10700]; reliability — UniProbe/Latent Critic/ProbGuard hallucination detection [2608.10906]/[2608.10397]/[2608.10823], error-aware step reasoning [2608.10928]; mechanism design — EFX∨MMS chore allocation + Lean-4 formalized EFX chores [2608.11025]. Zero-overlap: 15 same-day papers claimed by arxiv-ai-search / arxiv-paper-check were removed from this digest (batch note documents the split) — GenRec [2608.10257], MARCO [2608.10562], LinkedIn causal [2608.10182], LLM-rec hallucination audit [2608.10008], group-rec tie-breaking [2608.11190], Sequential Modality Dropout [2608.10240], TimeRoute [2608.10983], model merging [2608.10447], ReOrder-OPD [2608.10905], CLAUDE.md catastrophic remembering [2608.11095], MESA [2608.10108], UniF-MoE [2608.10392], TORF [2608.11114], VERDICT [2608.10665], ContractSim [2608.10475] (ai-search claimed GenRec/MARCO/ReOrder-OPD/UniF-MoE/CLAUDE.md/TORF/VERDICT/ContractSim; paper-check claimed MESA/TimeRoute/LinkedIn causal/hallucination audit/group-rec tie-breaking/sequential-modality dropout/model merging)
- Updated: wiki/index.md (Synthesis 表新增 arxiv-daily 2026-08-12), wiki/log.md
- New pages: wiki/synthesis/2026-08-12/arxiv-daily.md
- Contradictions: none (32 IDs grep-verified absent; 15 same-day overlaps excluded, not duplicated)

## [2026-08-12] synthesis | Investment Daily (2026-08-12)
- New page: wiki/synthesis/2026-08-12/investment-daily.md
- Coverage: 全球科技与 AI 板块投资日报（周三版·A股/港股盘中口径）。美股/中概 = 8/11 周二完整收盘——三大指数连续第二日收跌（道 -0.34% 53,791.85 / 标普 -0.32% 7,728.20 / 纳指 -0.60% 26,445.45），费半 +0.87% 逆势反弹（存储/设备 V 型修复：SK海力士 +4.7%、ASML +3%、泰瑞达 +3%、闪迪/希捷 +2%，光通信 COHR +4.5%/Lumentum +4.5% 反弹），大型科技股多数下跌（NVDA 高开低走收 $217.50 基本收平），TSLA +0.58% $332.81；中概金龙 -2.94%——TME 财报次日 -12%（收入 ¥89.3亿 +5.8% 但社交娱乐 -16.4%、费用率 14.5% 增收不增利），BILI -5%、京东/蔚来/新东方/网易 -4%、贝壳/阿里 -3%，再鼎 +10%/万国数据 +4% 逆势。港股 = 8/11 完整收盘（恒指 -1.10% 25,652.82 / 恒科 -1.93% 4,824.42，科网+黄金股普跌、中海油 +3.6% 逆势、药明康德历史新高）+ 8/12 低开 0.6% 报 25,498.39（存储概念高开、南方两倍做多三星 +8%、PCB 回暖建滔 +2%、再鼎 +8%、中广核新能源 -5% 盈警）。A股 = 8/11 完整收盘（沪指 -0.82% 3,934.09 终结五连阳、科创50 -1.63%，AI 硬件 PCB 回调芯碁微装 -9%，油气设服/MLCC/医药商业/CXO 领涨，成交 2.32 万亿缩量）+ 8/12 早盘低开后翻红（存储芯片高开澜起/兆易 ~+2%）。重点主题：①存储超级周期——美光 CBO"供需紧张延续至 2027 后、DRAM 首要制约" + SK海力士重启大连 NAND 2 号厂（+50% 产能） + 苹果测试长鑫 DRAM（WSJ，长鑫拒绝压价）；②恒生科技指数改革咨询文件（30→50 只、新增 AI 主题、双组别选股，12 月生效）；③今日 8/12 超级事件日——美国 7 月 CPI 晚 20:30（预期 3.4%/核心 2.5%，花旗排除 vs 美银保留 9 月加息）+ 寒武纪说明会 15:00 + 宇树缴款截止 16:00（中签号 19,414、中一签 7.54 万、科创板史低中签率）+ ⚠️ Meta "Llama 4 405B" 验收失败（实际 Muse Glimmer 开源）与 Qwen3.8-Max 权重验收日未兑现（对齐 08-12 tech-report-digest）；④工业富联 H1（净利 +95.99%、AI 服务器放量）但 8/11 股价 -4.58% 利好出尽；⑤8/13 中芯国际 Q2 业绩前瞻。
- Updated: wiki/index.md（Synthesis 表新增 investment-daily 2026-08-12 条目，插在 08-11 条目之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-12/investment-daily.md
- Contradictions: ⚠️ 已排除 2025-08-12 同期旧闻（财联社"恒指 25000/中芯 +5%"/每经"沪指七连阳 3,665.92"/智通"恒指 24,969.68"/寒武纪"848.88 涨停"等均为 2025 年口径，已在报告数据说明标注）；Meta "Llama 4 405B 开放权重 08-12" 验收失败——08-11 investment-daily/tech-report-digest 所载"Llama 4 定档 8/12"为预告口径，与 08-12 实际（无 405B 发布、改开源 Muse Glimmer）矛盾，本报告已按 08-12 tech-report-digest 纠偏；南向 8/11 净额撰写时未获独立确认；A股/港股 8/12 盘中数据撰写时未独立确认待午间收评

## [2026-08-12] synthesis | WQ101 Alpha Daily (2026-08-12)
- New page: wiki/synthesis/2026-08-12/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (数据基准 8/11 周二完整收盘确认 + 8/12 周三盘前/事件窗口)。8/11 三大指数连续第二日收跌（道 -0.34% 53,791.85 / 标普 -0.32% 7,728.20 / 纳指 -0.60% 26,445.45）但费半 +0.87% 逆势反弹——存储/半导体设备 V 型修复（SK海力士 +4.7%、ASML +3%、泰瑞达 +3%、闪迪/希捷 +2%），光通信反弹（COHR/Lumentum +4.5%）；NVDA 高开低走收 $217.50 基本收平（连续两日 Alpha#12 背离）；TSLA +0.58% $332.81；中概金龙 -2.94% 全线重挫（TME 财报次日 -12% 事件性拖累）。Top 20 变更：**SMCI 新入选 7.6**——8/11 盘后财报大超（调整后 EPS $1.70 vs 共识 $0.92、净销售 $11.1B +91% y/y、毛利率 15-17% 兑现接近翻倍、$60B 订单簿），Alpha#6 事件因子驱动，DOJ/出口管制审查/增发治理折价限制评分；**MU 上调 7.7→8.1**——存储超级周期三重再验证（美光 CBO"供需紧张至 2027 后、DRAM 首要制约" + SK海力士重启大连 NAND 2 号厂 +50% + 苹果开始测试长鑫 DRAM）；CAT 移出（无催化被 SMCI 替换）；COHR 移至观察池（8/11 +4.5% 反弹仅 1 日，待 8/13 财报）。因子频次：Alpha#41 趋势 60% + Alpha#1 动量 60%（↑55%→60%）+ Alpha#6 事件 40%（↑，财报季密集 SMCI/CSCO/AMAT/COHR/JD）+ Alpha#19/#53/#30/#12 各 10-15%。策略：8/12 CPI（ET 8:30 / 北京时间 20:30，共识 3.4%/核心 2.5%，Kalshi >3.3% 概率 <55%）为唯一决定变量——核心 <2.5% 利好成长（NVDA/MU/PLTR），>2.6% 防御（LLY/CVX/XOM/JPM）；SMCI 8/12 开盘承接力决定 AI 硬件链情绪；NVDA $205-210 为 Alpha#41 关键支撑；8/26 NVDA 财报为板块再定价锚。交叉参考：[[synthesis/2026-08-11/wq101-alpha-daily]]（前一期）、[[synthesis/2026-08-12/investment-daily]]（8/11 收盘全口径 + 存储事件）、[[synthesis/2026-08-12/tech-report-digest]]（同日 Llama 4/Qwen 验收）。
- Updated: wiki/index.md（Synthesis 表新增 wq101-alpha-daily 2026-08-12 条目，插在 08-11 条目之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-12/wq101-alpha-daily.md
- Contradictions: 无实质矛盾——8/11 报告将 SMCI 列为观察池（"毛利率 ≥12% 验证决定 AI 硬件链情绪"），本报告按 8/11 盘后实际财报（EPS $1.70/毛利率 15-17% 兑现）将其纳入 Top 20，属事件落地而非矛盾；能源板块 8/11 美国盘未获独立板块级涨跌数据（A/港股油股逆势：中海油 +3.6%），CVX/XOM 评分维持并在报告中标注"未独立确认"；MU 8/11 收盘价未获独立确认（8/10 收 $861.00 -1.89%，8/11 修复日，报告以存储链反弹结构 + 8/7 $877.57 企稳为锚并标注 tentative）

## [2026-08-11] synthesis | arXiv AI Research Search (2026-08-11)
- New page: wiki/synthesis/2026-08-11/arxiv-ai-search.md
- Coverage: 21 curated papers from the fresh Aug 9–10, 2026 arXiv submissions (retrieved via the API ahead of the Tue Aug 11 announcement ~20:00 ET; IDs ~2608.05791–2608.09930 incl. Aug 6–8 recall fill-in), every arXiv ID grep-verified absent (0 hits), zero overlap with same-day arxiv-paper-check (18, cs.AI+cs.IR deep scan) / arxiv-daily (31, cs.LG/cs.CL/cs.GT/econ.TH breadth) / game-rl-daily (19) / conference-digest. Streams: Coding Agents (SWE-Bench ProMax multilingual refactoring benchmark 170 instances avg 11.4 files/261.6 LOC, HKUST/SJTU [2608.09802]; SpecPath contract-equivalent spec-path sensitivity 35/100 direct-success blocks flip, USTC/HKUST [2608.09799]; OpenCodeReview deterministic review 2.17× SEM-F1 AACR-Bench, Nanjing [2608.09290]; AgentChaos shared-HTTP fault injection pass@1 −50pp, SMU/NUS [2608.06790]; GALA+ graph-guided RCA +25pp AC@1, U Toronto [2608.08968]; PMCoder plan×memory +5.0pp SWE-bench Verified [2608.06811]; Pseudo2CodeQA structured-algorithmic code benchmark 4.78 vs 4.31 [2608.09068]), Multi-Agent & Security (Koopman spectral certificates for collective debate, pre-run deadlines, CSU [2608.05956]; TIPEX replica×structural parallelism [2608.05791]; TBA query-only trajectory backdoor vs self-evolving skills, IIT [2608.08303]; Order 66 dormant-compromise compositional threat model, RIKEN [2608.08131]), Post-Training (Matryoshka LM Suites −36% compute +14–26% speculative decoding, Cornell [2608.09703]; TIDE excess/deficit OPD Avg@8 6.9%→20.3%, HKU [2608.09836]; TrajVal learnability prior, Alibaba [2608.09217]; OP²SD other-problem distillation [2608.09228]; 3PO parameter-space RLVR, TU Darmstadt [2608.09805]), Inference (SwiftQK scalar-only QK-Norm TP stats, latency −81.4–93.9%, TPOT −29.5% [2608.09160]), Game Theory (Repeated-Game Security restaking one-round slashing gap, history-dependent + reputation-weighted + vesting, HKUST [2608.09055]; VCG-style collusion detection in peer review, ICLR 2021 [2608.08486]), CAD (CADEngBench parametric+assembly engineering benchmark [2608.09296]; verifier-free consensus selection text-to-CAD [2608.09706]). cs.IR submissions (PushDualGen 2608.07989, Structure-Preserving Projection 2608.08583, PreGress 2608.09016) left to paper-check's domain
- Updated: wiki/index.md (Synthesis table — arxiv-ai-search 2026-08-11 entry inserted before 08-10 entry), wiki/log.md
- New pages: wiki/synthesis/2026-08-11/arxiv-ai-search.md
- Contradictions: none (21 IDs grep-verified absent; Ouroboros 2608.08311 / MARP 2608.07280 / extensive-form regret 2608.09501 excluded as already covered elsewhere and cross-referenced in the report)

## [2026-08-14] synthesis | LLM Tech Report Daily (2026-08-14)
- New page: wiki/synthesis/2026-08-14/tech-report-digest.md
- Coverage: 20 家机构滚动更新 digest（继承 08-13）。今日重点: **MiniMax M3 完整规格补全**——官方技术报告 + 开源权重齐备（arXiv:2606.13392, GitHub MiniMax-AI/MiniMax-M3），428B 总参/23B 激活原生多模态 MoE，1M ctx 下相对 M2 prefill 9×/decode 15× 提速（每 token 计算 1/20），核心创新 MSA（MiniMax Sparse Attention，Index Branch top-16 block 路由 + Main Branch 精确注意力）+ 7-MTP 投机解码，60 层（前 3 层 Full GQA 16:1 + 3-59 层 MSA），128 专家 top-4 sigmoid 路由 + 1 共享专家，CLIP ViT-32L + 3D RoPE 视觉塔，BrowseComp 83.5 超 Opus 4.7（79.3）/TrainBench 37.1 第三，国内首个 "frontier coding + 1M ctx + 原生多模态 + 开放世界" 齐备旗舰；**Gemini 3.7 Flash GA（08-13）**——1M input/64K output ctx、$0.75/$3.75 每 M（intro pricing 至 2026-12-31）、主打 agentic coding/terminal execution；**GPT-5.6 System Card 增补（08-03）**——GPT-Red 自动红队（自博弈 RL）；**Grok 4.6 Model Card（08-12 修订）**——1.5T 家族、text+image 输入/text-only 输出、与 Cursor 联合开发；**Nemotron 3.5 Lightning（08-11）**——30B-A3B 面向 always-on agents；**Kimi K3 技术报告（07-27）**——2.8T/104B、Delta Attention + Attention Residuals + Stable LatentMoE、约 2.5× scaling efficiency；**Microsoft Phi 核实**——无 Phi-5 官方报告，最新 Phi Silica Platform Card（06-24/07-08，NPU 端侧 SLM）；其余: Claude Sonnet 5/Opus 5 System Cards、Shieldstral、GLM-5.2、SeedRealtime、Step 3、Nova 2、AFM 3、InternGeometry、Baichuan-M4（清华合作）、Qwen3.8-Max 权重兑现（继承）、DeepSeek V4 GA（继承）；Meta Llama 4 405B 持续未兑现（第 3 天）
- Updated: wiki/index.md（Synthesis 表新增 tech-report-digest 2026-08-14 条目，插在 08-14 arxiv 条目之后、08-13 条目之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-14/tech-report-digest.md
- Contradictions: 无实质矛盾——Step 3 规格以官方 321B 总参/38B 激活为准（修正 08-12 记 198B 口径，与 08-13 digest 一致）；Gemini 3.6 Flash Model Card（07-21）与 3.7 Flash GA（08-13）为代际关系非矛盾；Phi Silica 为端侧 SLM 新品卡、与 Phi-4 开放家族并行，非 Phi-5 替代

## [2026-08-14] synthesis | game-rl-daily — Game RL & Game AI Bot Paper Digest (2026-08-14)
- New page: wiki/synthesis/2026-08-14/game-rl-daily.md
- Coverage: 16 curated papers from the **Fri Aug 14, 2026 announced window** (Thu Aug 13 submission wave, IDs ~2608.12308–2608.13560; 339 unique papers fused from API date-range queries `submittedDate:[202608130000 TO 202608140000]` across cs.AI/cs.LG/cs.CL/cs.GT/cs.MA/cs.CV/cs.HC/cs.RO), all 16 IDs grep-verified absent (0 hits), zero overlap with the 08-14 sibling digests (arxiv-daily 29 / arxiv-ai-search 20 / arxiv-paper-check 19). **Same-day dedup:** game/world-model items claimed by siblings were intentionally NOT duplicated — AlayaWorld 2608.13492 + Objective-Is-The-Bottleneck 2608.12959 + Diagnosing JEPA World Models 2608.12939 (arxiv-daily); Do-LLMs-Beat-Nash 2608.12547 + TsuGO 2608.13221 + Error-Aware Reverse Auction 2608.12719 (arxiv-ai-search); Entropy-Augmented 2608.12534 + DIVE 2608.12486 + 2608.12921/13043/13096/13120 (arxiv-daily). Themes: **world models dominate the window** — Alaya-EVOKE endless interactive WM (externalized camera-indexed world-state memory + linear-scaling long-horizon teacher supervision → 3-step CFG-free student, SOTA WBench, H200 2.11s/1.5s-chunk, Alaya Lab/Shanda + USTC [2608.13546]); PlayWorld agent-player benchmark of WMs over 171 long-horizon objectives (4 dims, 9 WMs unreliable on spatial consistency, HKU + Kuaishou Kling [2608.13552]); causal-WM unification [2608.13456]; S2-HWM event-structured hierarchical WM 98.7% SurRoL [2608.13103]; DreamX-Phi 1.0 action-conditioned video WM, WorldArena 2.0 Track 1 winner [2608.13489]. **Game AI Bot** — EpicStar memory-as-policy LLM StarCraft II agent (episodic bank + working memory + dynamic gate, higher win rate at 10× fewer tokens, extends ICLR 2025 WS paper) [2608.12626]. **Game RL** — decentralized multi-player Q-learning under information asymmetry near-tight regret [2608.12753]; action-intersection Q-learning bias [2608.12912]; OGR-MARL pursuit 75% capture [2608.12995]. **Benchmarks** — H2R-Bench cross-embodiment [2608.13049]; HumanoidVLN Isaac Sim 933 episodes JanusVLN 43.55% [2608.12860]. **Related** — SSPO Evidence Anchors + step-level GRPO advantages [2608.12764]; Temporal GRPO stage-aligned advantages [2608.13026]; online QTD inference FCLT + random scaling [2608.12973]; ContactGuard latent-WM pre-contact monitor CMU [2608.13438]; Agent Behavioral Contracts II shared-model co-fail 90.0% + finite-sample certificates [2608.12895]. PCG: none. Industry: Alaya/Shanda + Kuaishou Kling cross-refs only
- Updated: wiki/index.md (Synthesis 表新增 game-rl-daily 2026-08-14 条目，插在 08-13 条目之前), wiki/log.md
- New pages: wiki/synthesis/2026-08-14/game-rl-daily.md
- Contradictions: none (all 16 IDs grep-verified absent; PlayWorld 2608.13552 confirmed distinct from the robot "PlayWorld: Learning Robot World Models from Autonomous Play" 2603.09030 in index.md — noted in the digest; Alaya-EVOKE placed under Game Foundation Models rather than Industry, with cross-ref to AlayaWorld coverage)

## [2026-08-14] synthesis | WQ101 Alpha Daily (2026-08-14)
- New page: wiki/synthesis/2026-08-14/wq101-alpha-daily.md
- Coverage: WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (数据基准 8/13 周四完整收盘确认 + 8/14 周五盘前/事件窗口)。8/13 = "闪迪投资者日 + AMAT 盘后 + JD 财报"三线兑现日。**①PPI 偏软 + 标普创收盘纪录新高**——7 月 PPI 环比 0.0%（同比 +4.7%）、S&P 500 收 7,798.99（+0.65%，收盘纪录新高）、Nasdaq 26,803.03（+0.81% 两连涨）、Dow 53,839.99（+0.13%），9 月加息概率维持 ~42%；**②SNDK 投资者日 +~15% 收 $1,551.34**——FY28-30 目标调整毛利率 ~80%、营业利润率 ~75%、FCF 利润率 50%、100% 超额现金返还；2027 年产能 50%、2028 年 ~2/3 已签长期合约 = 存储超级周期最强指引；**③AMAT 记录级 Q3 财报但盘后 -3.5% = 教科书级"确认非催化"兑现**——Q3 FY26 营收 $9.12B +25%、EPS $3.50、经营现金流 $3.04B 创纪录、Q4 指引 ~$10.25B/$4.02 超当期，但年内 +108% 已 price in，完全命中 8/13 报告"确认非催化"风险预设；**④JD 中概纠偏信号**——Q2 营收 RMB 346.4B（-2.9%）但经营利润转正 +RMB 4.5B（vs -0.9B 亏损）、非 GAAP 净利 RMB 8.9B（+20%）、EPS 超预期（Regards of Wallstreet 口径），与腾讯"收入 beat 但 FCF 折价"构成对照组；**⑤油价回落**——Brent $87.07（-2.15%）、WTI $81.25（-2.4%）跌破 $82；**⑥Burry 高位做空**——NBIS @$247 / MU @$924 / ORCL @$152 + SOXX 看跌期权，"Nebius 就是繁荣顶部的样子"；**⑦CSCO beat 但毛利率下滑盘后 -4%+**、COHR 财报后下跌；**⑧大型科技反弹**——MSFT +0.9%（$496.88）、GOOGL +0.82%（$346.36，Gemini 3.7 Flash GA）、TSLA +3.8%、AAPL +1.0%，唯一逆势 AMZN -0.8%，TSM +0.45%（$432.42）、NVDA +0.54%（$225.30 逼近 52 周高 $236.54）、SMCI +4.12%（$39.16 财报后第二日续涨）。Top 20 变更：**SNDK 新入选 7.8**（投资者日超级周期指引兑现，单日 +15% Alpha#30 波动率警告）、**JD 新入选 7.7**（经营利润转正 + EPS beat 中概纠偏）；**AMAT 移出 7.7→7.0**（确认非催化实战命中，移至观察池）、**CRWV 移出 7.8→7.6**（回落 + Burry"top of a boom"叙事 + 高杠杆）；上调 NVDA(9.3→9.4)/MSFT(8.8→8.9)/AAPL(8.5→8.6)/TSM(8.3→8.4)/SMCI(8.0→8.3)/GOOGL(7.7→7.8)；下调 MU(8.4→8.2)/CVX(8.4→8.1)/XOM(8.2→7.9)/ANET(8.1→8.0)/NBIS(8.0→7.8)。因子频次：Alpha#1 65%（↑）+ Alpha#6 55% 但纪律化（从加分转减分工具，须"超当期+长约/远期指引"双满足）+ Alpha#41 50%（↓）+ Alpha#12 15%（AMZN 新负背离）+ Alpha#30 15%（↑）+ Alpha#19 10%（↑）+ Alpha#53 5%（↓）。板块：Software/AI 5 只 25% + Cons Disc/Tech 5 只 25%（7/2 以来最高）+ Semis 4 只 20% + AI Infra 2 只 10%（较 8/13 的 35% 回落 5pct）+ Energy 2 只 + HC/Financials 各 1 只。策略：8/14 零售销售（ET 8:30，共识 +0.1%）为今日唯一决定变量——>+0.2% 利好 ABNB/DIS/AMZN/JD，<0% 回流防御 LLY；"确认非催化"映射 8/26 NVDA 财报风险；Burry 空头 vs 长约基本面矛盾 = 基本面服从、仓位纪律服从。交叉参考：[[synthesis/2026-08-13/wq101-alpha-daily]]（前一期，含"确认非催化"风险预设的兑现验证）、[[synthesis/2026-08-13/investment-daily]]（8/12 收盘全口径 + 腾讯 Q2 + CPI + AI 硬件爆发）、[[synthesis/2026-08-14/tech-report-digest]]（同日 MiniMax M3 / Gemini 3.7 Flash GA）。
- Updated: wiki/index.md（Synthesis 表新增 wq101-alpha-daily 2026-08-14 条目，插在 08-13 条目之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-14/wq101-alpha-daily.md
- Contradictions: ⚠️ **Burry"top of a boom"做空（NBIS @$247 / MU @$924 / ORCL @$152 + SOXX 看跌）vs 大行上调/SNDK 投资者日超级周期指引/Street Strong Buy**——已分别在 NBIS/MU 条目标注 contradiction flag，处理原则"基本面服从（长约数据 > 空头情绪）+ 仓位纪律服从（拥挤度下降前不加仓）"；⚠️ **AMAT 记录级 Q3 beat（$9.12B +25%/Q4 指引 $10.25B）但盘后 -3.5%**——"确认非催化"情景与 8/13 报告预设完全一致（非矛盾，为事件落地验证），已移出 Top 20；⚠️ CSCO beat 但毛利率下滑盘后 -4%+（对 ANET 的板块情绪传导已计入评分）；NBIS 8/12 收盘修正为 $247.05（8/13 报告 tentative ~$259），8/13 收盘走低点位未获独立确认；SNDK $1,551.34 收盘价为单来源确认；JD EPS beat 为单来源（Regards of Wallstreet）

## [2026-08-16] synthesis | 投资日报 (2026-08-16)
- New page: wiki/synthesis/2026-08-16/investment-daily.md
- Coverage: 周六周末复盘版，全部为 8/14（周五）完整收盘确认口径 + 中芯国际 Q2 实际值 + 美国 7 月零售销售实际值。**①中芯国际 2026 Q2 大幅超指引 + A/H 逆势大涨**——收入 $30.06 亿首破 $30 亿（+36.1% YoY/+20.0% QoQ，超指引环比 +14-16% 上限）、归母净利 $4.79 亿（+261.7%/+142.7%）、毛利率 25.3%（超指引 20-22% 上限）、产能利用率 93.7%、月产能 109.65 万片、capex $18.36 亿、12 寸 78.2%、中国收入 90.2%；业绩会"算力配套芯片供不应求"+赵海军"今年看不到晶圆代工降价"→ 港股 8/14 收 70.80（+4.81%）领涨恒指成分股、A股 688981 +2.65%；**②美国 7 月零售销售转负（8/14 ET 8:30）**——环比 -0.6%（2025/5 以来最大降幅，预期 +0.1%）、总额 7,636 亿美元（+5.0% YoY）、核心零售 -0.3%、线上 -2.2%（Prime Day 提前）仅服装 +1.9%；密歇根信心初值 51 低于预期 → 美股 8/14 自 8/13 纪录回落：S&P 7,785.76（-0.17%）/Nasdaq 26,729.16（-0.28%）/Dow ~53,732（-0.20%），周线三连阳仍近纪录（WSJ/AP/Investopedia 多源）；**③港股 8/14 结构恶化但中芯独强**——恒指 -1.10% 25,116.85/恒生科技 -1.77% 4,707.62（本周恒指 -2.15%/恒科 -3.1%），财报回吐主导（华虹宏力 -11.55%、京东物流 -13.69%、京东集团-SW 领跌成分股、联想 -3.72%、MiniMax-W -12.69%），智通"问题在内部——银行股调整"；南向本周净买仅 ~0.89 亿港元（大举加仓 MiniMax、抛售阿里，MiniMax 7 日流入超 84 亿但 8/14 -12.69% 分歧）；**④A股 8/14 指数强个股弱**——沪指 +0.01% 3,927.18/深成指 +0.45%/创业板 +1.12% 领涨，但超 2,900 只下跌（2,363 涨/2,931 跌）、成交缩量 ~2.14 万亿（-4,080 亿）；存储/HBM/半导体/服务器/AI 算力走强（电子化学品/元件领涨），黄金/AI 应用/医药商业走弱，中石科技一字涨停（中际旭创拟接盘 10.47% 股份）；**⑤中概 8/13 US 时段下挫 + JD 分歧定价**——金龙 -1.84%，京东 -7%（Q2 收入 -2.9% 被惩罚尽管经营利润转正 +RMB 4.5B——与 wq101"JD 纠偏入选 Top 20"形成预期 vs 现实对照）、拼多多 -5%、阿里/美团 ADR -2%、腾讯/小米/比亚迪 ADR -1%+（南方财经 8/14 凌晨）；**⑥产业/宏观**——SK海力士董事长 8/14"价格涨太快我很抱歉；明年将是存储芯片供应缺口最大的一年"；宇树科技热搜（2023-25 营收 CAGR 226.78%、2025 归母净利 2.78 亿、出货 5,500 台+全球份额 32.4%、募资 42.02 亿、审核 104 天、8/19 前后挂牌）；恒生科指改革（宁德时代或纳入）+ 联想周内 +19% 史上最强季报（Q1 营收 1,834 亿 +43%、AI 收入 634 亿 +60%、储备订单 3,600 亿+）+ 腾讯单季 528 亿 AI 豪赌。交叉参考：[[synthesis/2026-08-14/wq101-alpha-daily]]（8/13 收盘：SNDK +15% $1,551.34/AMAT 盘后 -3.5% 确认非催化/JD 经营利润转正/Burry 空 NBIS/MU/ORCL/CSCO -4%+ AH/油价 WTI $81.25 -2.4%）、[[synthesis/2026-08-14/tech-report-digest]]（MiniMax M3/Gemini 3.7 Flash GA）、[[synthesis/2026-08-13/investment-daily]]（腾讯 Q2+CPI+AI 硬件爆发）、[[synthesis/2026-08-12/investment-daily]]（恒生科指改革+宇树缴款）。策略：美股"通胀温和 vs 消费转弱"增长担忧接棒通胀成主导矛盾，8/19 FOMC 纪要 + 8/26 NVDA 财报为再定价窗；港股财报兑现纪律（华虹 -11.55%）+ 南向骤降，唯中芯（超指引+满载+定价权）为最强兑现者；A股存储/算力主线 + 宇树 8/19 挂牌催化，但量价背离（缩量+2,900 下跌）注意题材轮动。
- Updated: wiki/index.md（Synthesis 表新增 investment-daily 2026-08-16 条目，插在 08-14 条目之前——周末复盘版，数据口径 8/14 周五完整收盘）, wiki/log.md
- New pages: wiki/synthesis/2026-08-16/investment-daily.md
- Contradictions: ⚠️ **京东"经营利润转正（wq101 8/14 视为中概纠偏入选 Top 20，Alpha#6/#19 均值回复）"vs 市场 8/13 US 时段 -7% + 港股 8/14 京东集团-SW/京东物流双领跌恒指成分股**——"基本面纠偏 vs 收入收缩定价"分歧，已在报告第五节标注；与腾讯"收入 beat 但 FCF 折价"构成镜像（当前中概定价 = 收入 + 现金流双验证）；⚠️ **MiniMax 南向 7 日流入超 84 亿港元 vs 8/14 股价 -12.69%**——"南向买、股价跌"分歧；⚠️ 8/13 报告中芯 Q2 指引（环比 +14-16%/毛利 20-22%）vs 实际（+20.0%/25.3%）为超指引兑现而非矛盾；8/14 美股个股级收盘、8/14 US 时段中概、8/14 油价收盘值未获独立来源确认（报告中已标注）；金龙 -1.84%/京东 -7% 等 8/13 US 中概为单来源（南方财经 headline）；Dow 8/14 点值为 investing.com CFD（tentative）

## [2026-08-15] synthesis | LLM Tech Report Daily (2026-08-15)
- New page: wiki/synthesis/2026-08-15/tech-report-digest.md
- Coverage: 20 家机构滚动更新 digest（继承 08-14）。今日重点: **Qwen3.8-27B 正式开源（08-14）**——27B dense 原生多模态（image+video）、Apache 2.0、262K native ctx（YaRN 可扩 1M）、Hybrid Gated DeltaNet + Gated Attention（64 层 = 16 组重复块），DeepSWE v1.1 42.2（vs 3.6-27B 13.3）/Terminal-Bench 2.1 73.0/SWE-bench Pro 61.7/OSWorld-Verified 84.3/WebArena 64.8/LiveCodeBench v6 90.3/GPQA Diamond 89.2/CoWorkBench 70.7（超 Opus 4.6 Max），整体超 Qwen3.7-Plus，FP8 ~28GB 单 48GB 卡可跑，OpenRouter $0.45/$3.20；**与 2.4T 旗舰权重"双轨"对照**——27B = Apache 2.0 + native vision + thinking 可调；2.4T（Qwen/Qwen3.8-2.4T-A95B，08-12/13 权重） = 定制 qwen3.8-max license + text-only + thinking 强制 + 512 专家（10 routed + 1 shared）+ 大客户 revenue share 条款（门槛/比例未公开）；**GLM-5.3 正式发布（08-14）**——"基座不变、后训练提智"：与 GLM-5.2 相同 743B 基座，纯后训练 Scaling（数十倍长程环境 + IndexShare + SAO + 新一代 Slime 框架），Terminal-Bench 3.0 4.6→28.3 开源第一、DeepSWE v1.1 46.2→66.9、Agents' Last Exam 23.8→28.5、GDPval-AA 1,769、编程体感 +50%、网络安全白盒审查/漏洞发现持平 Mythos 5（真实代码库 2436 漏洞）、Z.ai Code Bench High 31.4% 超 Opus 4.8 29.5%（每任务 ~5万 vs ~12万 tokens）、上线 ZCode/AutoClaw/GLM Coding Plan + 京东云 MaaS 当日接入、权重两周后开源；**Meta Llama 4 405B 持续未兑现（第 4 天）**——另剔除 annlive.com 04-24 "已发布"内容农场文章（与 llama.com/mungomash/codersera 追踪矛盾）；**GPT-5.6 Sol Ultrafast（Cerebras 08-14）**——chart 14×/end-to-end 5.6× 加速（非新模型）；**DeepSeek V4-Pro 官方 GA 确认（Reuters 08-13，API 定价显著高于 V4 Flash）**；其余继承: Gemini 3.7 Flash GA、GPT-5.6 GPT-Red、Claude Sonnet 5/Opus 5、Fable 5.1 观察、Shieldstral、Phi Silica、AFM 3、Nemotron 3.5 Lightning、Grok 4.6、Nova 2、SeedRealtime、Kimi K3、InternGeometry、Baichuan-M4、Step 3、M3、01.AI。交叉观察: 后训练 Scaling 成竞争前沿（同基座提智 vs 换基座）、中国开源旗舰周更（Kimi K3/DeepSeek V4-Pro/Qwen3.8 Max+27B/GLM-5.3）、开放权重"能力/许可证双轨"分化（Qwen 首次分层）、Meta 唯一持续失约方
- Updated: wiki/index.md（Synthesis 表新增 tech-report-digest 2026-08-15 条目，插在 08-16 investment-daily 之后、08-14 arxiv-ai-search 之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-15/tech-report-digest.md
- Contradictions: ⚠️ **修正 08-14 记录**——"GLM-5.3 传闻（>1T，新浪财经 07-20 + JPMorgan 8 月口径）未发布"→ 今日核实 GLM-5.3 已于 08-14 正式发布且为 **743B 同基座**（此前 ">1T" 传闻口径错误），已在 Zhipu 节标注修正并升级为正式条目；⚠️ **annlive.com 04-24 "Llama 4 405B 已发布"** 与 llama.com 目录 / mungomash（08-05）"2025-04 后无新 Llama" / codersera（05-01）一致证据矛盾，判定内容农场不采信，Meta 未兑现口径延续（第 4 天）；⚠️ Qwen3.8 双轨信息（27B Apache 2.0 + vision vs 2.4T 定制 license + text-only）为官方卡并排事实非矛盾；Qwen3.8-27B 部分评测（CoWorkBench 70.7 vs Opus 4.6 Max 68.2）为厂商自报；annlive 文章剔除后无 single-source 冲突项

## [2026-08-15] synthesis | Investment Daily (2026-08-15)
- New page: wiki/synthesis/2026-08-15/investment-daily.md
- Coverage: 投资日报 — 全球科技与 AI 板块（2026-08-15 周六周末复盘版）。数据口径：美股/中概 = 8/14（周五）完整收盘（含 8/13 周四收盘节点），港股 = 8/14 完整收盘，A股 = 8/14 完整收盘；中芯/华虹 Q2 = 8/13 盘后披露 + 8/14 市场反应。①**美股周五获利了结 + 消费数据转弱**——三大指数自 8/13 历史新高回落（Dow -0.20% 53,732.41 / S&P -0.17% 7,785.76 / Nasdaq -0.28% 26,729.16），美国 7 月零售销售环比 -0.6%（2025/5 以来最大降幅）+ 密歇根 8 月信心初值 51.0 → FedWatch 9 月加息概率降至 28.6%；10Y 4.695%、WTI +1.42% $82.40；②**周线三连涨但 AI 内部大分化**——S&P/Nasdaq 周线三连涨，存储续强（闪迪 +7.39% 周 +35%，JPMorgan 上调至增持目标 $2,250），AMD +6.5%（47.5 亿美元史上最大规模发债）vs AVGO -5.94% / AMAT -5% / ORCL -3.65%；8/13 节点：S&P 7,798.99 创收盘历史新高 + 闪迪投资者日 +13.67% + Workday +17.78%（Silver Lake 收购传闻）+ CSCO 8/13 -8.4%；③**港股四连跌、京东绩后重挫**——恒指 -1.10% 25,116.85（周 -2.15%）、恒生科技 -1.77% 4,707.62（周 -3.10%），京东 -10.4% / 京东物流 -13.69%（Q2 收入 -2.9% 高基数），半导体分化（中芯 +4.81% vs 华虹 -11.55%），MINIMAX-W -12.69% / 智谱 -3.57% 冲高回落，南向净卖 13.16 亿港元，腾讯传 20 亿美元收购 Manus 股份；④**A股缩量修复、通信板块爆发**——沪指 +0.01% 3,927.18、创业板指 +1.12% 收复 30 日线，成交 2.14 万亿（缩量 4,081 亿），通信 +3.45% 领涨（英伟达 Spectrum-X 硅光交换机量产 + 中际旭创 17.47 亿受让中石科技 10.47% → CPO/散热涨停潮），海光 +10%+、寒武纪 +11-12%（市值破 4,000 亿）、长鑫 +4.35%，华虹 A股 -8.57%；⑤**OpenAI 高管离职潮**——CRO Dresser 8/13 离职（任职仅 8 个月）、COO Lightcap 8/11 离职，年内 7-10+ 核心高管出走；估值 8,520 亿美元、IPO 倾向推迟至 2027（Altman 1 万亿估值底线）；Anthropic 年化营收 ~470 亿反超 OpenAI、拟 60 亿美元收购 Decart AI；⑥**产业/宏观**——中芯 Q2 收入 $30 亿（+20% QoQ）/毛利率 25.3%/稼动率 93.7%/Q3 指引环比 +2-4%；联想 ADR +18.95% vs 港股 -3.72% 分歧定价；伯克希尔 Q2 增持 Alphabet 83%；DeepSeek 峰谷定价 + 智谱 GLM-5.3；宁德时代 41 亿增资中恒科技 49%（800V HVDC）；KKR/摩根资管 2026-30 AI 投资 $5.3 万亿 vs $1.5 万亿现金流覆盖；宇树挂牌临近 + 世界机器人大会 8/19-23
- Updated: wiki/index.md（Synthesis 表新增 investment-daily 2026-08-15 条目，插在 08-16 investment-daily 之后、08-15 tech-report-digest 之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-15/investment-daily.md
- Contradictions: ⚠️ **联想 ADR +18.95%（财报超预期）vs 港股 -3.72%（8/14）**——同财报两地定价分歧，已在报告标注；⚠️ **京东"经营利润转正（wq101 8/14 视为中概纠偏入选 Top 20）"vs 市场 8/13 US 时段 -7.31% + 港股 8/14 -10.40%**——收入收缩 vs 盈利拐点定价分歧（与 08-16 周末复盘版口径一致）；⚠️ **中芯 Q2 实际（+20% QoQ/毛利率 25.3%）超 8/13 指引（环比 +14-16%/毛利 20-22%）**为超指引兑现非矛盾；⚠️ 单来源数据：中概周五个股涨跌、比亚迪/宁德时代 A股涨跌、港股 EV 个股（报告已标注）；AMAT "记录级 beat 但 -5%" 与 08-14 wq101 "确认非催化" 预设一致；OpenAI IPO 推迟为传闻口径（Altman 1 万亿底线为市场推测）

## [2026-08-16] synthesis | arXiv AI Research Search (2026-08-16)
- New page: wiki/synthesis/2026-08-16/arxiv-ai-search.md
- Coverage: **Sat–Sun Aug 15–16 = arXiv 无周末公告**, 最新批次仍为 **Fri Aug 14, 2026**（提交 Aug 12–13, IDs ~2608.12308–2608.13560）→ 本期为对该窗口的 **deep-scan 补扫**（08-14 digests 明确标注 cs.AI 204 / cs.LG 157 仅标题级部分扫描）。重扫流: cs.AI 204 / cs.CL 101 / cs.IR 19 / cs.GT 6 / cs.MA 14 / cs.SE 18 / cs.SI 4 / stat.ML 29 / econ.TH 6。**20 papers, 全部 NEW**（每 ID 全 wiki grep 0 命中, 与 08-14 arxiv-ai-search 20 / arxiv-daily 29 / arxiv-paper-check 19 / game-rl-daily 16 零重叠）。主题: ①ads/rec **更便宜的精确实验** — Fast A/B/n Tree-Coupled testing（任意历史相关 contextual-bandit 策略精确反馈共享, 代价恒等式 N(T)=T+TV, 条件最优 + 贪心 MST, T+o(T) vs JT, 子线性 pseudo-regret）[2608.12831]; ②**工业零售三件套（ICMLA 2026, Amazon tentative）** — Demand Transfer 系数 Restricted Logit 1M+ item 规模估计 [2608.12680]; Lines-and-Ladders 多智能体零售价格层级治理, Lines F1 0.83, 生产部署, Food&Consumables >90% P/>75% R [2608.12674]; ③**AutoResearch RL 重构为 world-model** — WMRL 用 biased+noisy world model 替代 sandbox 执行 + Online Debiasing + Inverse-Variance Denoising（收敛证明均严格改善）, 3–4× 加速, 4B/9B agent 超 48B/120B open-weight, 迁移 VLA [2608.12564]; ④**hallucination RL refusal-to-richness 权衡** — key-point rubric 奖励 + grounding+coverage+relevance 软组合, OOD checklist 迁移更好 [2608.12337]; ⑤**NCO 偏好优化** — SSPO dissimilarity-weighted LOO baseline 同时解 gradient signal polarization + baseline redundancy, JD.com 生产部署 [2608.12443]; ⑥**reasoning 定义澄清** — Position: Reasoning is a Learnable Rule-Based Process（construct validity 不可验证）[2608.12325]; ⑦**recurrent memory 内容路由生长** — MARCH state anchors + content-conditioned keys, LongBench/ICL 一致超 linear attention [2608.12435]; ⑧**相位拆分推理** — Dual-Flow Transformer prefill/decode 解耦（共享权重 + 单一 KV, MoE 相位特异 expert budget, prefill-decode 质量权衡）[2608.12385]; TEMPO makespan-aware EP load balancing（max-affine 两 regime 成本模型, phase diagram 而非普适胜, Qwen3-235B +4–6% 吞吐/−15.6% p99, Alaya/Shanda tentative）[2608.13057]; SPADE edge-draft/cloud-verify 投机解码, −76% cloud calls 零损失 [2608.13076]; ⑨**长度泛化理论** — 首个完整 C-RASP 正则语言长度泛化刻画 + syntactic monoid 多项式时间决策算法, Krohn–Rhodes 推广至整数无限加法群（unbounded counting 不可由有限半群表达）[2608.13433]; ⑩**模块化预训练** — Mixture of Training scaffolded block-wise 重组, 1.3B/C4 与 monolithic 同困惑度（compute 优势依赖 aligner 复用）[2608.13277]; ⑪**task-agnostic 数据影响** — 以对 final-params 轨迹距离缩减定义影响, Pythia/PolyPythia 18 配置 literature-early/STEM-late crossover [2608.13515]; ⑫**web agent 合成数据** — SynWeaver website-prior 任务-轨迹协同合成（map 构建 + UI-aware prior + 协同修复校验）, WebArena/WebVoyager 一致超 baseline [2608.12429]; ⑬**脑/LLM 记忆视角** — "LLM 领先的是实验可及性而非记忆本身", 功能/实验对照框架 [2608.12377]; ⑭**reasoning KV 压缩** — TAM thought 分段自适应预算 + pivotal token 保护（凸误差模型下分配最优 + 累积误差有界）, 峰值内存 −65% 保持精度 [2608.12331]; ⑮**生成 kernel 验证** — 12 道 tolerance-free contract 门审计 2,638 个 harness 已接受 kernel, **39.5% 破坏 + 62.1% 至少一处违规**, 4 重独立辩护; 首个原生 Blackwell tcgen05 GDN 训练 backward（reverse-state 阶段, fp64 oracle 验证）[2608.12700]; ⑯**体育/游戏** — H-xT/H-VAEP 手球首度移植 xT/VAEP（native 分区布局模拟更鲁棒 + team-identity leakage 控制, MLSA 2026, Paderborn tentative）[2608.12926]; StorySpark module-wise 进化搜索故事 premise, 原创性一致提升 [2608.12336]
- Updated: wiki/index.md（Synthesis 表新增 arxiv-ai-search 2026-08-16 条目, 插在 08-16 investment-daily 之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-16/arxiv-ai-search.md
- Contradictions: none（20 个 ID 全 grep-verified absent; v1 日期早于窗口的 6 篇（2608.12385/12337/12331/12377/12336/12325 为 05-29~07-31）系 Fri Aug 14 分类列表 cross-list/再公告, 非 wiki 旧条目, 报告已逐篇记录 published 日期与 caveat; WMRL "世界模型偏置/噪声奖励" 与 08-14 arxiv-daily Objective-Is-The-Bottleneck "check the planner" 为互补视角非矛盾, 已在 cross-trends 标注）

## [2026-08-16] synthesis | game-rl-daily — Game RL & Game AI Bot Paper Digest (2026-08-16)
- New page: wiki/synthesis/2026-08-16/game-rl-daily.md
- Coverage: **Sat Aug 16 = arXiv 无周末公告**, 最新批次仍为 **Fri Aug 14**（提交 Aug 12–13, IDs ~2608.12308–2608.13560, 已被 08-14 digests + 08-16 arxiv-ai-search 覆盖）→ 本期为 **Jul 15 – Aug 13, 2026 窗口的 game-dedicated 补扫**：全量 893 条 Aug 13 wave（API `submittedDate:[202608130000 TO 202608140000]`, cs.AI/LG/CL/GT/MA/CV/HC/RO）+ ~45 组关键词查询（game+RL, self-play, StarCraft, Minecraft, Atari, PCG, game+agent, NPC, chess, poker, card/board game, level generation, multi-agent RL, game+benchmark, world-model+game, game+engine, LLM+game, video game, game development 等, Jul 15–Aug 14）。**24 papers, 全部 NEW**（每 ID 全 wiki grep 0 命中; 与全部 50+ 期历史 game-rl-daily、同日 [[2026-08-16/arxiv-ai-search]] 20、08-14 arxiv-daily 29 / arxiv-ai-search 20 / arxiv-paper-check 19 零重叠; 已归 sibling 的游戏条目——AlayaWorld 2608.13492 / Do-LLMs-Beat-Nash 2608.12547 / TsuGO 2608.13221 / PlayWorld 2608.13552 / H-xT-H-VAEP 2608.12926——不重复收录）。主题: ①**Game RL** — CAP-DO 学习式 contextual action proposal 热启动 Double-Oracle, 保持 full-game certification 保证, 9,880 动作规模 benchmark [2607.24610]; N-player 随机微分博弈连续时间 RL, Gibbs 探索策略 + 可计算 Nash 均衡 cross-partial 判据, 不兼容时构造近似 correlated equilibrium (KL 界随 γ→∞ 消失) [2607.19928]; Curvature Shadow — Kuhn poker max-entropy 均衡选择表观失败为可去除伪影 (gap≈√(2δ/κ), 磁力扫描指数 0.50, R²>0.999999) [2607.17543]; S3 HRL 用 coarse-dynamics 预测不确定性 (MDN) 稳定 subgoal 选择 [2607.19232]; SADQ 单步 rollout 引导 TD-target 聚合, 降低 bootstrap 高估, Atari/经典控制 [2608.03069]; Neural-ODE latent-dynamics 正则化对齐表征与环境动力学, A2C/PPO Atari 大增益 [2608.06595]; Aggregate-in-the-Advantage — 合作 MARL 支持矩阵正则形分析: 目标仅依赖矩阵积 (冗余性) + 方差排序 (advantage 加法/ratio 乘法) → 设计原则 "advantage 聚合、ratio per-agent" [2607.17924]; ②**Game AI Bot** — The Weight of Silence — 潜性国际象棋推理六条件因果干预: RL 增加的是对扰动的鲁棒性而非对 thought 的依赖 (legality 48→61%, 换位迷惑消除; zero-vector 1% vs 9%) [2607.20952]; Three-Body Alignment — 人类 GM/NNUE 解说/LLM 三方国际象棋 rationale 语义分歧 (t-SNE 聚类) + rerank 对齐 + 战术性能权衡, 数据集开源 [2607.21993]; Diversity Collapse — SFT 压缩 LLM 落子 action support 超出 accuracy-diversity 权衡最低要求, action augmentation 部分缓解 [2607.19523]; RLSVR/SpyRL — 社交推理游戏 Who Is the Spy 式 self-play 将开放任务转化为可验证 reward, RLVR 超越 math/coding [2607.23802]; 3-Player Auction Bridge 精确算法 + 统计策略 [2608.03217]; WOPR — 可 replay 验证的 Nuclear War 卡牌规则引擎社会模拟 (decision-point contract + press ladder + Concordia harness, Georgia Tech tentative) [2608.01868]; Energy Society — token 消耗=生存压力的 LLM 多智能体经济测试床 [2607.14865]; Policy Gradient Steering — rollout 梯度构造可移除任务向量, 国际象棋谜题 + 足球队行为可迁移 [2607.27574]; ③**World Models** — ActSWM 诊断 Context Collapse (预测器对规划动作不敏感) + transition-separation 原则, Minecraft 闭环规划 [2607.26712]; WorldWeaver — 流式多智能体视频扩散加 cross-agent world state registers (MoT 权重分离), 双智能体 Minecraft [2607.21594]; PAVXploreRL — RL 微调 action-conditioned WM 显式优化 PAV 目标 + OOD action 探索 [2607.16602]; ④**PCG** — scheduled inpainting 交互式生成式 motion editing (Disney Research/ETH tentative) [2607.29133]; ⑤**Benchmarks**: 无新增; ⑥**Industry** — The AI Wave & Reinvention of Game Discovery — Steam 供给冲击 (Gini 0.96, top 1% = 73.5% 游玩时长), 1983 对照 → 集中而非崩溃, agentic player-game matching 议程 [2607.25010]; AI as Democratizing Force in Indie Game Development — 14 个月 agentic production 平台日志, planning $0.27–0.58/5.1min, 七维民主化仅 coordination cost 兑现 [2608.07825]; ⑦**Related** — Generalised Reachability Games PSPACE-complete + FPT + 记忆上下界 [2607.14199]; Generative Modeling as Mean-Field Game Design (MFGLab, DI-Flow) [2607.23026]; Draining the Energy Commons — LLM collective 过度取用可再生资源 = 系统性协调失败 (Sapienza tentative) [2607.22188]。趋势: 世界模型从 fidelity 转向 action-responsiveness (Context Collapse/registers/OOD action); 国际象棋成 reasoning-alignment 压力测试场; 合作 MARL 理论成熟化
- Updated: wiki/index.md（Synthesis 表新增 game-rl-daily 2026-08-16 条目, 插在 08-16 arxiv-ai-search 之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-16/game-rl-daily.md
- Contradictions: none（24 个 ID 全 grep-verified absent; ActSWM/WorldWeaver/PAVXploreRL 三个 action-sensitive world-model 方向为互补视角非矛盾; 与 08-14 PlayWorld "agent-player 评估" 为同一 "WM 必须响应动作" 主题的生成侧三条独立路径, 已在 cross-trends 标注）

## [2026-08-16] synthesis | arXiv Daily Digest (2026-08-16)
- New page: wiki/synthesis/2026-08-16/arxiv-daily.md
- Coverage: 26 curated papers, **all NEW**, from the **Sat–Sun Aug 15–16 无公告窗口 → Fri Aug 14, 2026 批次**（提交 Aug 12–13, IDs ~2608.12308–2608.13560）的 supplementary 零重叠 curation（08-14 arxiv-daily 29 / arxiv-ai-search 20 / arxiv-paper-check 19 / game-rl-daily 16 及当日早些 08-16 arxiv-ai-search 20 已各自认领其 picks）。每个 ID 全 wiki grep 0 命中（index.md/log.md/synthesis/**）；全部 published 2026-08-12/13 在窗口内，无 v1 早日期 caveat。来源: cs.AI 205 / cs.LG 158 / cs.CL 101 / cs.IR 19 / cs.GT 6 / cs.MA 13 / econ.TH 6 / stat.ML 29。
- 主题: ①**embedding 成本核算** — Embedder's Dilemma: LLM-as-embedder 与专用模型 aggregate 持平（Gemini 3.1 Pro 77.6 vs 77.2）但贵至 1,431×（$154 vs $0.11/benchmark pass）; 分工建议 = 相似/分类/聚类用 embedding 模型, reasoning-heavy retrieval 用 LLM [2608.12875]; 七系统向量库评测（FAISS 866 QPS / Weaviate recall>99% / Qdrant 4.55ms / LanceDB build 最快, 15 metrics, 开源框架）[2608.12812]; Sinhala-Tamil↔English CLIR: BGE-M3 96.2%/95.6% R@15 超 Google Translate 92.4/93.0 且免翻译开销 [2608.12820]; ②**agent 记忆: 访问协议 vs 可演化检索** — @skills 拆分 content/persistence/triggering, 仅 triggering 需 prompt residency, path 寻址读即用 "install less, use more"（56,804 公开 skills）[2608.12610]; ERSkill 检索本身作为可演化 skill 集（double-frontier 安全解耦, Qwen3-Next-80B +31.3%）[2608.12720]; SMA 冻结 VLM 无工具参数零更新的空间自进化（verifier-guided lessons + TRS 校准, 5 benchmarks × 4 VLMs）[2608.12743]; Reconcile Once 确定性 trust-tiered librarian + 多 agent writer, as_of 时点报告零 look-ahead, 6,845 跨节矛盾→0, tier-first 22/22, 3.7× 快于串行 [2608.12984]; Intern-S2-Preview 科学 agentic 基座（397B, Memory Decoder 冻结主干快速特化 Intern-MemDec-4B 56.92→60.32）[2608.13505]; ③**搜索/评估经济学** — Algorithm Transparency（econ.TH）: 透明化使排序算法从 steer 变 persuade, 对消费者福利非单调（detter/encourage search 两种情况相反）[2608.12558]; Sampling Luck 审计: NCO 样本预算 in-sample "allocation gain" 2.2–2.6% 系 sampling luck, out-of-sample 归零（pre-registered; 仅在分布漂移下真实: AM 11.5% / SymNCO 12.0%, POMO 负对照 −0.3%）[2608.13087]; ④**后训练: coverage vs exploitation** — ES 比 RL 更高 pass@k（RL 输出分布收窄致 coverage 塌缩; ES 权重空间扰动保多样性且数学基准更好）[2608.12679]; CABS+ gradient-free 合并系数搜索 + RSS mergeability 度量（+16.97% vs AdaMerging, <25% 内存, ~4× 快于 WUDIMerging）[2608.12842]; ε-MemEvo task-agnostic tactic-memory 跨任务迁移 + 自适应注入门（8 任务全胜 +8.7% AUCC, 可解释 skip→hint 后验, <1% 开销）[2608.12522]; CSE 多约束组合满足相变（15 模型 369,753 checks; k=8 单约束 41%→全中 5.7%; 结构约束退化 2× 于词法; 最强模型 7 约束跌破 50%, 12/15 在 ≤3）[2608.12426]; ⑤**训练/推理结构效率** — LoKiFormer LFA 卷积融合局部注意 + KMM 参数化 KV 解耦知识存储（预训练 1.33× 提速）[2608.12419]; Trie Automata 有限集约束解码（Aho-Corasick 预计算 mask, 每步 7× 于 XGrammar, batch-256 端到端 219 vs 7.5 req/s = 29×）[2608.12574]; RoutePack MoE RL 专家放置 + attention-aware packing 联合优化（Ling-3.0 Tiny/Flash +8.85%/+14.89% 吞吐）[2608.12146]; ⑥**金融生成 + 评估严谨性** — DYSANOS 首个无静态套利期权曲面生成模型（AR(1) baseline, 动态套利数值检验, IvyDB 2020–25）[2608.12587]; LOB-ID 把 FID/MIND 移植到订单簿（moment-matching attack 下 MIND 稳健, FID 可被攻破）[2608.13082]; ReCoGen represent-then-generate 多模态条件时序生成（16/16 生理场景最优, 13/16 达或超真实信号效用）[2608.12592]; ⑦**博弈/社会选择 tail** — Incidence Bimatrix Games 有向图一般化 Bapat-Tijs 1997（无环图 Player I 均衡唯一、顶点概率∝路径长; Player II 均衡 = path matrix 列凸包）[2608.13001]; Liquid Democracy Power 用 Random Walk Decay centrality + 公理化刻画 [2608.13188]; liquid-profile 同行选举强比例性 [2608.13085]; ⑧**基准/理论** — LigBench + PAIR-IQ 研究想法生成评估（去 LLM-scoring 主观性）[2608.13136]; UGC unmasking growth complexity 认证最优 masking-diffusion schedule（KL 误差界 + 样本可估, Wainwright）[2608.13520]; Numeracy NGF survey（RG/PG 分解, from-scratch vs 后验干预）[2608.13129]
- Updated: wiki/index.md（Synthesis 表新增 arxiv-daily 2026-08-16 条目，按字母序插在 arxiv-ai-search 2026-08-16 之后 / investment-daily 2026-08-16 之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-16/arxiv-daily.md
- Contradictions: none（26 个 ID 全 grep-verified absent; 当日 arxiv-ai-search 已覆盖的 15 个短名单 ID（2608.12325/12331/12337/12385/12429/12435/12564/12674/12680/12700/12831/12926/13057/13277/13433）已剔除未重复收录; 与 ES-vs-RL coverage 论点相关的 08-14 on-policy-distillation 线为互补视角非矛盾）

## [2026-08-16] synthesis | LLM Tech Report Digest (2026-08-16)
- New page: wiki/synthesis/2026-08-16/tech-report-digest.md
- Coverage: 08-16 大模型技术报告 digest，基于 08-15 digest 增量更新。今日重点：①**DeepSeek V4 新定价 08-16 生效**——V4 Flash $0.14/$0.28（cache hit $0.0028）、V4 Pro $0.435/$0.87 每 M tokens，SGLang Day-0 支持（PR #23600）+ LMSYS Miles 同步（V4-Pro 官方 GA 获 Reuters 08-13 确认，V4 家族全线 MIT 开源）；②**Grok 4.6 上线 GitHub Copilot（08-14）**——生态渠道在 Cursor 后再扩，Model Card 08-12 修订（1.5T 家族、text+image/text-only、500K ctx、$2/$0.50/$6 vs $4/$1/$12、reasoning 四档），Grok Bot 08-11；③**Step 3.7 Flash 由 single-source 升级为正式条目**——05-29 官方口径多源确认（官方博客/IT之家/NVIDIA/OpenRouter），196B+1.8B ViT≈198B/11B 激活 MoE、256K ctx、最高 400 tok/s、原生多模态（图像+视频）、Advisor Mode 达 Claude Opus 4.6 编码 97% 成本 1/9、SWE-Bench Pro 56.26/Terminal-Bench 2.1 59.55，开源（GitHub/HF/ModelScope）+ SGLang/TensorRT-LLM/vLLM/NVIDIA NIM 部署；**无正式 arXiv 报告**——官方引用 arXiv:2605.27761 核实为 AndroidDaily 论文（非本模型），相对 3.5 Flash 增量 = 原生多模态 + Advisor Mode + 搜索增强；④**Apple AFM 3 规格补全**——五模型家族（Core 3B dense / Core Advanced 20B sparse IFP 激活 1-4B / Cloud / ADM 3 Cloud 图像 / Cloud Pro），与 Google 合作（TPU 训练 + 复用 Gemini 技术 + Apple 自有数据后训练），Cloud Pro PCC 跑 Google Cloud NVIDIA GPU（PCC 首次延伸到 Apple 数据中心之外），评测偏好 Cloud 64.7% vs 2025 Server 8.7%、dictation 44.7%、TTS MOS 4.15，EU/中国大陆首发不可用（监管），技术报告承诺 "later this summer"（08-16 仍在窗口内）未兑现；⑤**Meta Llama 4 405B 持续未兑现（第 5 天）**——仍仅 NeuralStack 07-28（Bloomberg）预告（405B、原生多模态、15T tokens、单 H100 32 tok/s），llama.com 目录仍仅 Scout/Maverick；annlive 04-24 "is out" 判定低可信内容农场排除；08-10 开放权重战略转向（Muse Glimmer 30B Apache 2.0 开源 + 数周内 Muse Spark 1.2 权重）为实际重大事件；⑥**Microsoft Phi 复核**——Phi-5 仍为 single-source 传闻（rateais/Spheron 05-26 pre-release announcements vs systems-analysis 07-11 "no Phi-5 generation" 矛盾），不入正式条目；最新正式报告 = Phi-4-reasoning-vision-15B（arXiv:2603.03975）+ Phi Silica Platform Card；⑦**Baichuan 战略转医疗垂直确认**——Baichuan-M4 HealthBench 68.6 世界第一（清华合作 08-12，arXiv:2606.08982，hallucination 3.3%），M2 08-11 开源 32B HealthBench 60.1，通用线止于 Baichuan4-Air，无 8 月新通用模型；⑧**Yi/01.AI 无 2026 新旗舰**——最新仍 Yi-Lightning（2024-10-16，arXiv:2412.01253），重心转企业/主权 AI（万策平台 2026-07、哈萨克斯坦 Q.AI JV）；⑨**InternLM 无 8 月新报告**——最新前沿 InternGeometry（ICLR 2026，CBRL 复杂度提升 RL，IMO 2000-2024 几何 44/50），最大开放旗舰 Intern-S1-Pro（1T，arXiv:2508.15763），InternLM4 未确认（04-13 传闻）；⑩继承 08-15 条目：Qwen3.8-27B 开源、GLM-5.3 正式发布（743B 同基座后训练 Scaling）、Qwen3.8-Max 2.4T 权重兑现（PaperBench 93%）、GPT-5.6 Sol Ultrafast（Cerebras）、Gemini 3.7 Flash GA 等。交叉观察：后训练 Scaling 成竞争前沿（GLM-5.3 "同基座纯后训练提智" vs DeepSeek V4 重预训练）、中国开源旗舰"周更"节奏、开放权重"能力/许可证双轨"分化（Qwen3.8 2.4T 定制 license vs 27B Apache 2.0）、稀疏注意力/激活收敛期（MSA/CSA/IndexShare/Delta/IFP）、Agent 化能力成官方评测主战场（Terminal-Bench/DeepSWE/CyberGym/Copilot/Advisor Mode）、Meta 唯一持续失约方（405B 第 5 天）+ Apple AFM 3 报告为第二待兑现项。传闻不入正式条目清单（更新）：Llama 4 405B（未兑现）、GLM-5.5、Grok 4.7/5、Kimi K4、MiniMax M4（H2 2026）、Phi-5、Fable 5.1、InternLM4、字节 >5T/10T、Mistral 夏季开放 MoE、Astra "GPT-6"、Step 4。
- Updated: wiki/index.md（Synthesis 表新增 tech-report-digest 2026-08-16 条目，插在 investment-daily 2026-08-16 之后、investment-daily 2026-08-15 之前）, wiki/log.md
- New pages: wiki/synthesis/2026-08-16/tech-report-digest.md
- Contradictions: ①Step 3.7 Flash 发布日期修正（~2026-03 → 2026-05-29，以官方口径为准）；②Step 3.7 Flash 官方引用 arXiv:2605.27761 核实为 AndroidDaily 论文，非模型技术报告；③GLM-5.3 参数量传闻 ">1T" 已核实为 743B 同基座（08-15 修正延续）；④Meta Llama 4 405B "is out"（annlive 04-24）与 llama.com 目录/官方 07-27 预告矛盾，判定低可信排除；⑤Phi-5 pre-release 报道（rateais/Spheron 05-26）与 systems-analysis 07-11 复核矛盾，仍 single-source 传闻

## [2026-08-16] synthesis | Conference & arXiv Digest (2026-08-16)
- New page: wiki/synthesis/2026-08-16/conference-digest.md
- Coverage: 12 venues + general arXiv (Jul–Aug 2026), 中文标题双语呈现, 全部条目来自本次 web 检索（未编造 arXiv ID；无法确认的标注 "link not confirmed"）。**ICML 2026** (Seoul 7/6-11, ~24,661 submissions/6,352 accepted; Outstanding Paper ×2 = The Flexibility Trap/JustGRPO (Tsinghua, GSM8K 89.1%) + High-Accuracy Diffusion Sampling (MIT/Yale); Outstanding Position Paper; ToT = A3C (DeepMind); Oral: MaxRL (20× test-time scaling vs GRPO), daVinci-Dev (SWE-bench Verified 56.1%@32B/58.5%@72B from Qwen2.5-Base), WeDLM (Tencent, ~3× speedup), LIVE (MSR world model), Learning Unmasking Policies (Apple), DR Tulu (AI2), ThreadWeaver (AIME24 79.9%); Google Model Monotonicity in Autobidding 2605.31036 (66% revenue-loss counterexample); SWE-Bench Pro (long-horizon); Skill-MoE 2503.05641). **ICLR 2026** (Rio 4/23-27, 19,525 submissions/5,355 accepted; Outstanding ×2 = Transformers are Inherently Succinct 2510.19315 + LLMs Get Lost in Multi-Turn 2505.06120 (MSR, avg 39% drop); Oral/notable: Mamba-3 2603.15569 (+0.6pp vs Gated DeltaNet), Q-RAG (10M-ctx, single-A100), ATLAS (DeepMind, 774 runs/400+ langs), GEPA (35× fewer rollouts), DECS (>50% token cut), BARL (DeepMind), iFusion (CTR +2.44% online A/B), Prophet (3.4× fewer steps), R-Horizon, Generative Auto-bidding Oral). **NeurIPS 2025** (San Diego 12/2-7, ~20K submissions/25%; Best Paper ×4 = Artificial Hivemind 2510.22954 + Gated Attention 2505.06708 (Alibaba Qwen, 中国唯一) + 1000-Layer RL + Why Diffusion Models Don't Memorize 2505.17638; Runners-up = Does RL Really Incentivize Reasoning / Superposition Yields Robust Neural Scaling / Optimal Mistake Bounds; ToT = Faster R-CNN). **AAAI 2026** (Singapore 1/20-27, ~29K submissions/4,167 accepted 17.6%; Outstanding ×5 + AISI ×2: LLM2CLIP, ReconVLA, CADYT, Model Change for DL, High-Pass Sheaflet; Alignment Best = Global Human Opinion). **CVPR 2026** (Denver 6/3-7; Best = D4RT DeepMind dynamic-4D reconstruction; HM = SAM 3D (Meta), NitroGen (NVIDIA, 40K hrs/1K games); DeltaTok (ByteDance, 1024× token cut / 2000× fewer FLOPs), HoloCine 2510.20822 (HKUST/Ant/ByteDance), TV2TV (Meta FAIR, 91% pref), RVM-AE (DeepMind, ≤30× param efficiency), CURVE (DeepMind+Berkeley, human 95.22% vs Gemini-2.5-Pro 45.07%), TMD (NVIDIA, NFE=1.38, VBench 84.24), GenieDrive, VerseCrafter, AVGGT). **KDD 2026** (Jeju 8/9-13; Best D&B = Meta Multi-modal Multi-turn Comprehensive RAG Benchmark; ADS = MCGrad; Research Track 获奖者未确认; CTR-Sink 2508.03668 (Ant)); **ACL 2026** (Best = Imperfective Paradox (U Tokyo); Outstanding: DeepPlanning 2601.18137 (Alibaba/Qwen, 全对仅 35%), Evolutionary Guided Decoding (NVIDIA), CAR-bench (BMW, pass³ 0.42), Lychee-FD (HIT/Huawei, +7.4% QA), CxMP, ViLL-E (Meta), GeoRA, CURE, MediEval, Lying with Truths). **EMNLP 2025** (Suzhou 11/4-9; Best = Infini-gram mini (FM-Index); Outstanding: DeepResearcher 2504.03160 (SJTU, +28.9), LingGym, CoT-Faithfulness-by-Unlearning, Value-Action Gap; Best Resource = Autoformalization). **SIGIR 2026** (Melbourne 7/20-24; SilverTorch (Meta, 23.7× throughput/20.9× cost-eff), HyFormer (ByteDance), Generative Bid Shading, Verifiable Reasoning LLM4Rec (Meta/NUS), Bayesian List-wise Alignment, HE-DeepFM). **WWW 2026** ⚠️勘误 Dubai（悉尼=2025）; Best = Medical Retrieval-to-Generation; TESLA 2601.19965 (Alibaba Alimama, RI-AUC +12.41%); PLUM (Google/YouTube 数十亿用户全量上线); DualGR best short; ToT = LINE. **CIKM 2025** ⚠️勘误 Seoul（贝尔法斯特=2024）; Best = GAE Link Prediction; WeChat 多模态 CTR (Tencent). **RecSys 2025** (Prague 9/22-26; Best Full = You Don't Bring Me Flowers (conformal risk control, 评委全票); Best Short = Beyond Top-1; RESLONGER (ByteDance, 10+ 场景部署)). **General arXiv 7-8 月**: Seed 2.0 Model Card (ByteDance, 2607.00248), HiLS-Attention (Tencent, 2607.02980, 50B 续训), Qwen-Audio-VAE (2607.11738, 32min→541ms), Compute-Optimal≠Cluster-Optimal (2608.10605), SINKFLEX-RL (2608.10357), Self-Evolving Coding Agents survey (2608.03392), Ark/ArkBench (2608.10934, 8/10), Stealing Reasoning Traces (2608.09867), EMPO² (MSR, ScienceWorld +128.6%), RA-RFT (Meta, AIME +7.1), VIPE (DeepMind, 2607.25537), MiniWorld (2608.01127), PlayWorld (Kuaishou, 2608.13552), V-RAE/OmniScientist (2608.13556/13558), LLaTTE (Meta, +4.3% conv, 2601.20083), EST (Alibaba, RPM +3.27%, 2602.10811), WhisperRec (Kuaishou, 2607.26621), MixFormer (ByteDance, 抖音上线, 2602.14110), Autobidding PoA=2 (Google, 2602.21966), Netflix 1B gen-rec (MRR +22.5%, 2605.23312), UQ model-merging (2608.10447).
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 2026-08-16 条目，插在 game-rl-daily 2026-08-16 之前), wiki/log.md
- New pages: wiki/synthesis/2026-08-16/conference-digest.md
- Contradictions: ①WWW 2026 会址勘误——迪拜 (Dubai, UAE) 非悉尼（悉尼为 WWW 2025），已在本 digest 与 index 中标注；②CIKM 2025 会址勘误——首尔 (Seoul) 非贝尔法斯特（贝尔法斯特为 CIKM 2024）；③AAAI 2026 会址/时间勘误——新加坡 1/20-27（此前口头假设华盛顿）；④KDD 2026 Research Track Best Paper 获奖者公开来源未确认（Meta RAG Benchmark 为 D&B track、MCGrad 为 ADS track），caveat 标注；⑤RecSys 2025 Best Industry Paper 官方奖项页未列出（not confirmed）；⑥部分条目 (MaxRL, daVinci-Dev, LIVE, DR Tulu, ThreadWeaver, GEPA, CAR-bench 等) 为检索可见标题/摘要、affiliation 或 arXiv 链接未能独立确认，均已标注；⑦前序 digest 记 WWW 2026 悉尼、CIKM 2025 贝尔法斯特 为错误口径，本 digest 起以官方站点为准；⑧ICML 2026 Outstanding Position Paper 与部分 Honorable Mentions 未逐条展开（标注）；⑨与本 wiki 已有 NeurIPS/ICML/CVPR 奖项确认条目 (08-10 conference-digest) 一致，无实质冲突

## [2026-08-17] synthesis | arXiv Paper Check — AI & CTR (August 17, 2026)
- New page: wiki/synthesis/2026-08-17/arxiv-paper-check.md
- Coverage: 10 curated papers from Mon Aug 17 arXiv listings (cs.AI: 268 new entries, cs.LG: 138 new entries). Topics: LLM pruning (Sparsity Whisperer), nested LM training (Matryoshka), mechanistic interpretability (Graph Circuit Learning), agent evaluation (AV-AIVAT 74× cheaper), training-free LTSF (KReF), CTR loop scaling (LoopCTR), dual-path CTR residuals (DeRes), frequency-domain CTR (FEDIN), generative intent CTR (GenCI), unified relevance-CTR with LLM distillation (PRECTR-V2). Cross-cutting trends: computation-without-parameter-growth, dual-path architectures, frequency-domain for CTR, amortized/training-free methods, LLM→production CTR distillation.
- Updated: wiki/index.md (Synthesis 表新增 arxiv-paper-check 2026-08-17 条目，插在 arxiv-paper-check 2026-08-12 之后), wiki/log.md
- New pages: wiki/synthesis/2026-08-17/arxiv-paper-check.md
- Contradictions: none

## [2026-08-21] synthesis | arXiv Paper Check — AI & CTR (August 21, 2026)
- New page: wiki/synthesis/2026-08-21/arxiv-paper-check.md
- Coverage: 16 curated papers from last-24h window (submissions Aug 20 UTC; 179 unique new entries across cs.AI/cs.LG/cs.IR via arXiv API + CTR-keyword sweep). Topics: e-commerce dense retrieval RL (SSR-GRPO, SID-based hard negatives), training-free post-LLM CF refinement (CoRRe, CIKM 2026), synthetic-prior in-context sequential rec (RecPFN), seq-rec benchmark validity (RecSys 2026 probes beat eSASRec 15–38% on most benchmarks), continual retriever-reranker distillation (SCoRD), production generative matching for ride-hailing (GenMatch), CTR training throughput via early-backward scheduling (ERASE +9.51%), single-rollout autoregressive policy+value agentic RL (SAPO), tool-use mid-training corpus (MidTool), agent memory state tracking (StateMemBench 1.8×), step-level credit assignment audit vs executed replay (chance-level), self-improvement audit vs measured null (Phantom Gains), MoE μP transfer for MLA+Muon to 10T tokens (COLM 2026), BoN-style truncation distillation (TUP), adaptive reasoning budget in GRPO (-41% tokens), routing as costly-inspection search (Pandora's Router). Cross-cutting: benchmark-validity audits across three literatures; training-free/amortized rec; RL entering retrieval/matching stack; compute allocation as learned decision.
- Updated: wiki/index.md (Sources 表新增 arxiv-paper-check 2026-08-21 条目，插在 arxiv-paper-check 2026-08-17 之后; Synthesis 表新增同条目，插在 arxiv-ai-search 2026-08-21 之前), wiki/log.md
- New pages: wiki/synthesis/2026-08-21/arxiv-paper-check.md
- Contradictions: none（16 个 ID 全 grep-verified absent; 与当日 arxiv-ai-search 零重叠; RecSys'26 benchmark-validity 论文为对既有 seq-rec 文献的方法论警示，非与 wiki 具体页面矛盾）

## [2026-08-21] synthesis | Conference & arXiv Paper Daily Digest (2026-08-21)
- New page: wiki/synthesis/2026-08-21/conference-digest.md
- Coverage: 15 papers (all grep-verified absent from wiki; zero overlap with same-day arxiv-ai-search / arxiv-paper-check). **ICML 2026** (closed 8/9-13 Vancouver): TimesX 2607.06973 (GaTech+Google, multimodal TSF benchmark, main conf; 312K LLM inferences, AvgEns TimesFM-2.5+Gemini-2.0-Flash MASE 0.619 #1 beats agentic CodeRev; synthetic benchmarks overestimate LLMs) + Implicit Software World Models 2606.27406 (JetBrains, DL4Code WS; execution-resource axis: peak memory/wall-clock/profiler on SWE-bench Verified, all models incl. frontier modest & brittle). **Code World Models ×5**: PCWM 2604.20926 (LLNL+UMass, parallel-code world model, race pred 64.3%→72.8% @7B, profiling 49.3%→58.6% @8B, downstream race-fix +2.7~11.1%), Debugging CWM 2602.07672 (token-budget exhaustion + string-state subword tokenization failure modes), InCoder-32B-Thinking 2604.03144 (ECoT+ICWM industrial world model, Verilog/GPU traces, LiveCodeBench v5 81.3%), Execution Semantics robustness 2604.16320 (UC Davis+UCL; GPT-5.2 CRUXEval 99% → −20~24pp under perturbation vs DeepSeek-R1 stable 38-67%). **Agents ×2**: Router-Mem 2608.01285 (ZJU, sufficiency router single-token early termination for agent memory), EFCA 2608.08255 (NEU/NiuTrans, short/mid/long timescale credit assignment from environment feedback). **Video gen acceleration ×4**: MDD 2608.17695 (magnitude-direction decoupling, 2.95× on Wan2.1), SQuad 2608.16585 (Qualcomm, O(n√n) attention distillation), TMD 2601.09881 (NVIDIA+NYU, backbone+flow-head few-step distillation), Vorch-Omni 2608.05803 (unified audio-visual arbitrary-condition-to-arbitrary-output). **Time series ×3**: QuitoBench 2603.26017 (Ant/Alipay billion-scale corpus, 8 TSF regimes, context-length crossover L=96 DL leads / L≥576 FM dominates, 59× param efficiency), TempusBench 2604.11529 (Brown, leakage-free eval framework w/ standardized tuning), Break-even analysis 2607.04919 (10,800 configs; FM-dominant 15/30; rule n_train<700 & seasonal → FM zero-shot; LoRA can hurt short series).
- Updated: wiki/index.md (Synthesis 表新增 conference-digest 2026-08-21 条目，插在 arxiv-ai-search 2026-08-21 之后), wiki/log.md
- New pages: wiki/synthesis/2026-08-21/conference-digest.md
- Contradictions: none（15 个 ID 全部 rg-verified absent；ICML 2026 奖项论文 Flexibility Trap / High-Accuracy Sampling 已有收录故未重复；部分机构标注为推断并已在文中注明）

## [2026-08-21] synthesis | Game RL & Game AI Bot — Daily Paper Digest (2026-08-21)
- New page: wiki/synthesis/2026-08-21/game-rl-daily.md
- Coverage: 14 curated papers, **all NEW**, from the **Fri Aug 21, 2026 announced window**（提交 Wed Aug 19 – Thu Aug 20, IDs ~2608.19xxx–2608.20xxx）+ unclaimed Aug 14–18 catch-up + 一篇 Jul 10 PCG 论文。~150 unique candidates screened via 16 arXiv API queries（cs.AI/LG/CL/GT/MA/CV/HC/econ.TH/q-fin/math.OC）。每个 ID 全 wiki grep 0 命中，与当日 arxiv-paper-check / arxiv-ai-search / conference-digest / tech-report-digest 及全部前序 digest 零重叠。已收录故剔除：SPADE [2608.19197] + FM-Bench [2608.18423]（08-20 arxiv-daily）、PCG Metageneration [2608.17947]（08-19 arxiv-daily）、SAPO [2608.19842]（当日 arxiv-paper-check）、EpicStar [2608.12626]（08-14 game-rl-daily）、Steam GenAI 感知 [2608.11539]、PRP [2607.12097]、Evo-WFC [2607.02082]（更早 digest）。
- 主题: ①**Game RL 理论** — Planning Against Learning in Rank-1 Games：rank(A+B)=1 双矩阵博弈 Nash 可多项式计算但 planning against 学习者（RWU/Replicator Dynamics）在固定加性常数内近似即 NP-hard（uniform 起点+constant 策略+有界 payoff 下仍成立）[2608.18067, Stanford GSB]; RM+ 精确单步守恒律（forward utility gain = squared state motion + regret-state norm 增长, √(m−1) sharp）→ potential games alternating play 一致有界 regret（解决开放问题）+ product of simplices O(ε⁻²) [2608.17417, JHU]; N-player optimal stopping games 随机化嵌入 + α-potential O(N⁻¹) + Potential-CT-DDPG 学习算法数值吻合解析基准 [2608.18355, UC Berkeley]; DQL 不稳定性三机制统一分析（Bellman bootstrap bias × greedy 动作回归噪声敏感 × 参数 spike 动力学）→ controlled bootstrapping + ensemble quantile + spike-based regulation, Atari-100K/Procgen [2608.16182, PKU]。②**Game AI Bot** — LLM type-vector 拟合 119,147 决策/78,657 被试/10 经济博弈角色 → 三维基（Risk Aversion, Strategic Sophistication, Trust）+ <12 类型簇跨博弈泛化 [2608.18265, Stanford/Michigan]; DeepMind debate 训练（generator-critic 弱 judge 博弈）抑制 RLAIF reward hacking（45% gap 恢复; word limits ~150 平衡博弈）[2608.17776]。③**World Models** — ForgeWM 四阶段渐进因果训练（domain adaptation → teacher-forced causal → causal consistency distillation → on-policy distribution matching）→ 1/2/4-step action-conditioned video WM, Minecraft 键鼠 + FPS 手柄, dual-path interact-then-refine, Matrix-Game 2 + GameFactory + Causal Forcing 开源栈 8 GPU 可复现 [2608.14022, CUHK/Tencent PCG/FDU/Shanghai AI Lab/HKUST]; Neurosymbolic WM 符号潜变量子集承载 reward 预测 → 新 reward 函数零样本迁移 [2608.17959, KU Leuven 推断]。④**PCG** — 音乐游戏谱面生成 event+beat-shift token seq2seq（音频条件 Transformer 超 frame-level baselines）[2607.09095, JAIST]。⑤**Related** — Co-RL 多模型 peer-reward cohort 训练击败 self-rewarding collapse（多样性降低相关误差; LLM +3.0–8.6% / VLM +2.3–7.2% 无标签）[2608.17253, Exeter/JHU/UCSD]; QVIRL Q-space 变分 Bayesian IRL（首个 raw pixel Bayesian IRL, gridworld/LunarLander/Highway/2 Atari）[2608.16888, Oxford 推断]; NSPER novelty+surprise 双信号 PER/intrinsic reward（DMC vision）[2608.17373]; IER 即时 episode 重复数据采集侧样本效率（SAC/TD3 + 真机）[2608.17373 同组 Auckland]; reputation-as-information Q-learning 空间囚徒困境合作相变 [2608.20016, ECNU/Ningxia/Shaanxi Normal]。⑥**Industry** — 窗口内无新 studio 论文；背景条目 PUBG Ally CPC 架构演进（workflow SLM → autonomous tool-calling agent loop, Minitron 2B on-device ≤8GB VRAM, System1/System2 分层, ~40K 局网吧数据, A.X K1 韩语版）与 NVIDIA ACE Game Agent SDK Beta + UE5 插件（2026 年 6 月事件, 已注明日期）。
- Updated: wiki/index.md（主表新增 game-rl-daily 2026-08-21 条目插在 game-rl-daily 2026-08-19 之前; Synthesis 表新增同条目插在 tech-report-digest 2026-08-21 之后）, wiki/log.md
- New pages: wiki/synthesis/2026-08-21/game-rl-daily.md
- Contradictions: none（14 个 ID 全 grep-verified absent; QVIRL-Oxford 与 Neurosymbolic-KU Leuven 两处 affiliation 为作者名单推断并已在文中标注 tentative; FM-Bench claude-fable-5 结论与 08-20 arxiv-daily 收录口径一致无冲突）

## [2026-08-22] synthesis | Conference & arXiv Paper Daily Digest (2026-08-22)
- New page: wiki/synthesis/2026-08-22/conference-digest.md
- Coverage: 20 verified new papers from Aug 20–22 arXiv window (829 scanned); conference confirmations CIKM 2026 (ViT Feature Evolution) + ICONIP 2026 (RGA-Designer); mainline = agents/agentic RL (EnvHarness, Thinkingbox, MileGPO, PolicyGuide, BPS, skill transfer, CAMA) + serving (FlashPrefill V2, CacheRoute, ReCache) + video gen RL (Stream4D)
- Updated: wiki/index.md (Sources table row + Synthesis table row)
- Contradictions: none

## [2026-08-23] synthesis | LLM Tech Report Digest — 2026-08-23
- New page: wiki/synthesis/2026-08-23/tech-report-digest.md
- Coverage: 周末增量期（08-21 → 08-23，基于 08-21 期 digest），增量专题格式。核心更新：① DeepSeek-V4-Flash-Vision-Exp 发布（08-21，V4 家族首个 vision 模型，284B/13B 基座，图像 ≤384 tokens 平价计费无 vision surcharge，Terminal Bench 83.9 / Chartography 64.3，"接近 Opus 4.8" 为 vendor claim 未附对照列）；② OpenAI 正式确认前沿 RL 训练暂停（08-18：两周 RL 暂停完成但最大前沿 RL run 继续搁置，技术文档 "Pacing model development in an era of cyber-critical capabilities"，安全流程首次公开决定训练节奏）；③ Meta Muse Spark 1.2 多模态博客（08-20）+ Spark 1.2 Contributor 上架（08-21，单源待核）；④ Zhipu GLM-5.2 Turbo 上架（08-17）+ GLM-5.3 权重倒计时（~08-28 开源）；⑤ Stripe 收购 OpenRouter（08-19，分发层整合信号）；⑥ Gemini 3.5 Pro 跳票后 FutureSearch 重预测中位数 09-20；Grok 4.7 维持 9 月窗口；Mistral Agentic Search 产品（08-20）；GPT-6/Fable 5.1 传闻继续按 rumor 处理。其余 10 家公司无实质变化（快查表收录）。交叉观察：多模态下沉为 agent 基础设施、安全制度化第二阶段（训练节奏公开受控）、分发层收敛；承诺追踪表新增 DeepSeek vision 权重条目。
- Updated: wiki/index.md (Synthesis 表顶部新增 tech-report-digest 2026-08-23 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-23/tech-report-digest.md
- Contradictions: none（kie.ai "Fable 5.1 已发布/GPT-6 8月发布" 与 BenchLM 08-18 "未官宣" 结论冲突——已在 digest 中标注为 rumor 并说明证据等级；DeepSeek "接近 Opus 4.8" 官方口径缺 Opus 对照列已注明 vendor claim 待独立验证）

## [2026-08-23] synthesis | Game RL & Game AI Bot — Daily Paper Digest (2026-08-23)
- New page: wiki/synthesis/2026-08-23/game-rl-daily.md
- Coverage: 周末 catch-up 扫尾版（Sat 8/22 → Sun 8/23 无新公告，扫 8/8–8/17 未收录 backlog + 2 篇更早漏网）。11 items 全 NEW（10 papers + 1 community release），~45 候选 / ~12 组 web search 筛选，每个 ID grep-verified 零重叠。Game RL: PureTD Backgammon money-game pure-TD 无搜索自对弈 (2608.15146)；Watermarked Game Solving via Perturbed Regret Minimization — CFR 族求解策略水印 (CMU Kim & Sandholm, 2608.14977)；AgilePE UAV pursuit-evasion self-play PFSP + CTBR sim-to-real 零样本迁移 (2608.14135)。Related Techniques: Dynamic Reward Shaping 统一框架 12 method families (Bahrpeyma, 2608.08158)；CR-Eyes Atari 计算 rational 视觉采样 CHI'26 EA catch-up (2603.26527)。Game AI Bot: HSI 冻结 LLM harness 三层自进化 BALROG 大幅提升但 NLE 归零，feedback-fidelity/backbone-capability 双界 (2608.08466)；NCP-Bench ICML 2026 叙事 commitment preservation 对抗基准 GPT-5.2 仅 42% 存活 (2608.08160)。World Models & PCG: Marionette 显式 world state + 零参数 renderer + video diffusion，state-space 物理修复 (2608.14530)；Beyond Asking 行为→玩家特质推断驱动个性化游戏生成 (UIUC, 2608.16196)。Benchmarks: Two-Bridge StarCraft II 中间难度基准 v2 catch-up (2603.06608)。Industry/community: bedrock-rl HF blog (8/19) 确定性 Minecraft + verl GRPO VLM agent 框架
- Excluded as claimed (grep hits): VLM-Trackmania 2608.05954 / 流式 IL 增强 2607.14200 / OPR 2603.06793 / DiG-bench 2608.12593 / AgentOdyssey 2606.24893 / SciCrafter 2604.24697 / CODE-SHARP 2602.10085 / SCALAR 2603.09036；CrafterDojo 2508.13530 零命中但 >12mo 过期排除
- Updated: wiki/index.md (Synthesis 表顶部新增 game-rl-daily 2026-08-23 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-23/game-rl-daily.md
- Contradictions: none（全部 ID grep-verified absent；Marionette/AgilePE/Beyond Asking/Two-Bridge 等 5 处 affiliation 为作者名单推断并已在文中标注 tentative；bedrock-rl 为社区博客单源已标注）

## [2026-08-23] synthesis | arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-23)
- New page: wiki/synthesis/2026-08-23/arxiv-ai-search.md
- Coverage: 12 verified-new papers from the fresh window (Thu Aug 20 – Fri Aug 21 submissions, IDs ~2608.20xxx–2608.213xx; 105 unique candidates screened via 8 arXiv API queries over cs.IR/cs.CL/cs.AI/cs.LG/cs.GT with topic sweeps: recommendation / CTR+click-through+advertising+ranking / sequential+user-behavior / games / LLM+agents+post-training). 每个 ID 全 wiki grep 0 命中（含当日 sibling digests），零重叠。已收录故剔除：SCoRD/CoRRe/RecPFN/seq-benchmark-probes/ERASE/OneModel/SIDScope/rEDMRec/OGR-slate/Netflix-multimodal/GOD/SAGA/pacing-throttling（08-22 arxiv-ai-search、08-21 arxiv-paper-check）；MemTrapBench/Cross-task skill transfer/What-is-Missing-from-AI-Post-Training-AI（08-22 conference-digest）；Router-Mem/EFCA（08-21 conference-digest）；IAR/AI4AI-Bench（当日 arxiv-paper-check，运行期间新出现，已从本 digest 撤下并改写相应主题段）；streamed-games IL augmentations + VLM-conditioned agent（当日 game-rl-daily）。
- 主题: ①Rec/Generative-Rec ×6 — Netflix 8.5M-user field experiment：推荐质量提升使消费向 middle-tail 扩散而非极化（挑战 head+tail polarization 共识）[2608.21274, Netflix+Kellogg/Cornell inferred]; AdaptedKG 用校准 KG 关系证据做 seq-rec 行为去噪（不引入图表示进模型）[2608.21243, NEU-China inferred]; 单层大 semantic codebook 替代 multi-level RQ + exposure-aware 动态刷新 + collaborative disambiguation token [2608.21012]; eBay 单一 SID 层级同时服务 discovery ranking 与 search query reformulation（解决 merchant-scoped ID 碎片化）[2608.20640, eBay]; CAIRO user-context-aware item profiling 供 LLM rerank（CIKM'26）[2608.20801, KAIST/UIUC-affiliated inferred]; EviRank 把多模态图像 re-ranking 重构为 constraint satisfaction（六语义槽 required/forbidden/ignorable + rubric verification）[2608.20886]。②Agents ×3 — 轻量 GNN 做 agent failure attribution 挑战 LLM 管线必要性 [2608.18575, UIUC inferred]; AgenticRAG-FP certified-fault 注入+反事实重执行做因果归因（hop-1 coverage 0.91 → hops-2/3 0.00，静态 trace 归因在轨迹动态下失效）[2608.20627]; QAH 从原始未压缩 teacher 直接蒸馏修复结构压缩+4bit 模型（GPT-OSS 120B→60B→MXFP4；压缩中间体 bf16 checkpoint 本身是蒸馏近似故不宜作 target）[2608.20953, Multiverse Computing inferred]。③Seq/Memory ×1 — Context-Generation Substitution Law + training-free memory-augmented CoT 压缩（把计算从 decoding 移入 prefill）[2608.21265, ISCAS-inferred]。④Games/World Models ×2 — CIVA critic-induced value-subspace 攻击 DreamerV3 类 world-model agent（SVD 提取低秩 value 子空间+EMA 平滑系数优化）[2608.21114]; GraphOp-WM 形态无关局部动力学基 × 形态条件 structured operator 的图世界模型 [2608.20936, Tsinghua inferred]。
- Cross-cutting: SIDs 升级为跨系统平台基础设施；frozen LLM 周边的廉价自适应机制（profiling/checklist/memory-scaffold）；failure attribution 从 structural→causal→adversarial 演进；大规模 field-experiment 经济学进入推荐效果研究。
- Updated: wiki/index.md (Synthesis 表新增 arxiv-ai-search 2026-08-23 条目，插在 tech-report-digest 2026-08-23 之后), wiki/log.md
- New pages: wiki/synthesis/2026-08-23/arxiv-ai-search.md
- Contradictions: none（12 个 ID 全部 verified absent；Netflix middle-tail 结论与"推荐致极化"的流行叙事相悖但 wiki 无既有页面主张该叙事，非页面级冲突；affiliation 多处为作者推断并已在文中标注）

## [2026-08-24] synthesis | 投资日报 — 美股 / 港股 / A 股科技与 AI 热点 (2026-08-24)
- New page: wiki/synthesis/2026-08-24/investment-daily.md
- Coverage: 数据基准 = 美股/A 股周五 (8/21) 收盘 + 港股周一 (8/24) 开盘。核心事件：① 阿里巴巴周末公告 800 亿港元配售（710M 股 @ HK$112.70，折让 8.4%，港史最大 primary follow-on，100% 净额投全栈 AI，8/26 交割），叠加 FY27Q1 经营利润 -57%/Capex +75% 与 Burry 清仓言论，周一港股低开 ~8%；② NVIDIA 财报周（8/26 盘后）：指引 $91B±2%（不含中国 DC compute）、共识 $92–95B、Vera Rubin Q3 出货、与 Apollo/BlackRock/Blackstone/Brookfield/GS/KKR 共建 $500B+ AI 基建融资平台；③ Tesla +5.14%：Clark County 批准 Las Vegas 5,000 辆付费 robotaxi（Waymo/Uber 各约 1,500）；④ 存储通胀传导：AI 服务器明年初涨价 >15%、memory 占 NVDA 系统成本 40–50%（MU YTD +721%）；⑤ A 股算力中报验证：中际旭创 H1 净利 ¥136.51 亿 (+241.7%)、新易盛激励考核 2026 营收 ≥¥500 亿、寒武纪 H1 净利 +122.6%（存货 ¥82.48 亿隐忧）。港股：恒指五连升重越 26,000；小米"铁大"人形机器人 + SU7 七月零售 21,044 辆；网易 Q2 超预期 ADR +6.9%；智谱 (02513) 成交额居前、较 IPO 价 +871%。中概：HXC 全周 +0.10% 于 50 日均线拉锯。新能源车：BYD 7 月 41.9 万辆 (+21.8%)/海外 +124.3%，但行业 7 月销量同比 -5.9% 转负。本周日历：NVDA/Marvell 财报 (8/26)、Jackson Hole (Warsh 首秀)、阿里交割 (8/26)、7 月 PCE
- Updated: wiki/index.md (Synthesis 表顶部新增 investment-daily 2026-08-24 条目), wiki/log.md
- New pages: wiki/synthesis/2026-08-24/investment-daily.md
- Contradictions: none（BABA ADR 周五收盘价存在口径差异——cointelegraph 快讯报 -8.5% vs Yahoo bid 价 ~$119.4 推算约 -8.4%，已在报告中按 ~-8.5% 处理并标注；老虎社区"8 月 24 日"帖经交叉验证为往年旧文已排除）

## [2026-08-24] synthesis | WQ101 Alpha Daily — WorldQuant 101 Alphas 美股 Top 20 精选 (2026-08-24)
- New page: wiki/synthesis/2026-08-24/wq101-alpha-daily.md
- Coverage: 基于 WorldQuant "101 Formulaic Alphas" 7 因子框架 (Alpha#1 momentum / #6 量价 / #12 量价背离短线 / #19 均值回复 / #30 波动率预警 / #41 趋势强度 / #53 日内位置反转) 对美股大中盘 (市值 >$10B) 打分筛选。数据基准 = 8/21 (周五) 收盘 + 近两周公开报道 (~10 组 web search：指数与板块轮动、MRVL-Google 协议、存储 supercycle、TSLA robotaxi 牌照、AI 电力板块)。Top 20 按 Tier 分层: Tier1 = NVDA 9.2 / MU 9.0; Tier2 = SNDK, MRVL, TSLA, GEV, CEG, GS, GOOGL, MSFT, AVGO, SKHY, WDC; Tier3 = AMZN, INTC, META, NBIS, STX, VST, TLN。含因子公式表、打分规则、逐股卡片 (代码/板块/市值/因子/信号/逻辑/风险)、总表、板块汇总、组合级风险 6 条
- Updated: wiki/index.md (Synthesis 表顶部新增 wq101-alpha-daily 条目), wiki/log.md
- Contradictions: MU YTD 涨幅媒体口径冲突 (+216% vs +721%，已标注以券商口径为准)；SK Hynix ADR 代码按 247wallst 报道记为 SKHY 并标注近似；本文为定性推断非实时回测，已在文首与方法论节双重声明

## [2026-08-25] synthesis | arXiv Daily Digest — AI/LLM/RecSys/Ads/Games (2026-08-25)
- New page: wiki/synthesis/2026-08-25/arxiv-daily.md
- Coverage: 17 grep-verified new papers (fresh window Fri Aug 21 – Mon Aug 24 submissions, IDs ~2608.21xxx–2608.23xxx + 2 catch-ups 2608.13721/2608.16333), zero overlap with all sibling digests. LLM Training & Reasoning 6 — SOPD step-level on-policy distillation interpolating SFT↔OPD [2608.16333]; R2-OPD reasoning-progress-aware reward filtering for OPD (HKUST inferred) [2608.19408]; capacity-dependent Fast-Fit/Slow-Gain data selection 1.5B–8B (Virginia Tech inferred) [2608.13721]; BPCO stable critic recipe w/ privileged rubric conditioning (NUS inferred) [2608.23566]; ERPO query-distribution KL regularization (not stated) [2608.23311]; ADAPT amortized distillation across model-family size × variant axes (Harvard inferred) [2608.22854]. Recommendation & Generative Rec 6 — Alipay User Behavioral Densing Law: tokenization-capacity scaling relation at billion-scale (Ant Group inferred) [2608.23392]; Spotify factorial study showing descriptive CoT trace quality disconnects from rec effectiveness (Spotify inferred) [2608.23154]; ANR-DiffRec collaborative-prior noise rescheduling in discrete diffusion rec (Tongji/Fudan inferred) [2608.23400]; SST variable-length semantic subword item tokenization fixing intra-item attention overload (USTC inferred) [2608.22734]; HEGM hierarchical Exp-Gaussian mixtures fixing EGMN variance collapse in watch-time prediction (MSU inferred) [2608.23356]; pairwise counterfactual rank explanations from user profiles (Reichman/CU Boulder inferred) [2608.21662]. Ads & CTR 2 — CRRN cascading relevance network for Trigger-Introduced Recommendation CTR [2608.22973]; carousel click modeling + offline/off-policy evaluation thesis [2608.22022]. Games & World Models 3 — capability-based survey mapping 200 world-model works onto 8 simulator capabilities [2608.23070]; GameXpert-Bench process+artifact coding-agent game-dev benchmark [2608.21833]; LURE pursuit-evasion zero-data self-play with capture-frontier reward [2608.21871]. Cross-cutting themes: OPD rebuilt from first principles (3-paper cluster); tokenization as the new scaling axis in generative rec; input/environment-side control beating output-side regularization; explicit CoT traces facing replication crisis in rec
- Updated: wiki/index.md (Sources 表新增 arxiv-daily 条目), wiki/log.md
- Contradictions: none flagged; institution attributions marked inferred where not printed on papers; Spotify's "CoT hurts rec" finding noted as counter-evidence to OneRec-Thinking/RecOne lineage and support for WhisperRec latent-reasoning line (cross-referenced, not a hard contradiction)

## [2026-08-25] synthesis | arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-25)
- New page: wiki/synthesis/2026-08-25/arxiv-ai-search.md
- Coverage: 17 verified-new papers from the fresh window (Mon Aug 24 announcement wave — Fri 8/21 late – Mon 8/24 submissions, IDs ~2608.214xx–2608.235xx)。247 unique papers screened via 8 组 arXiv API queries（cs.IR sweep / click-through rate / CTR prediction / advertising∩cs.IR / sequential recommendation / cs.CL sweep / cs.GT / game∩cs.AI），131 篇 in-window，32 篇 topic-relevant 候选逐 ID 全 wiki grep 验证：同日 sibling arxiv-daily 已收 13 篇、game-rl-daily (08-24) 已收 1 篇，剔除后零重叠。
- 主题: ①Rec/Seq ×4 — DuELRec dual-expert LLM CDSR 治理 negative transfer (CIKM'26, KAIST-inferred, 2608.23131)；AGR group-rec agent token-hash-table memory + consensus-refinement reasoning (2608.21939)；N2DCG carousel 指标重构 eye-tracking 校准 discount (Uber/UvA-inferred, 2608.21877)；RecVerse 购物行为模拟器 cognitive 分层 memory + trajectory-level 监督 (Alibaba/RUC/NUS-inferred, 2608.20707)。②IR/RAG ×3 — multivector vs single-vector ranking 首个 exponential separation + ANDOR benchmark (Google-inferred, 2608.21494)；Laws of Context Allocation — causal leave-one-out probe + sequential-allocation-beats-widening (+16.7–20.5pp recall) (2608.23252)；RAG ingest-time semantic compilation position paper (2608.20845)。③Agents ×4 — AutoSaddler harness-as-code 从 failure traces 自动优化 harness +9–10pp (Microsoft, 2608.23041)；Prime Agent RLM harness ARC-AGI-3 RHAE 30%→95.5% (Prime Intellect, 2608.23552)；Agent-G² Gaussian hint-depth guidance 免 probe rollouts (ZJU, 2608.23318)；Compaction Cliff — Claude Code /compact 安全规则保留率 53%→10% (1→5 rounds)，Knowledge Triage typed retention 2–4× (Passau-inferred, 2608.22752)。④LLM Training/Safety/Efficiency ×4 — ERPO input-side Query-KL 破 stability-exploration dilemma (EMNLP'26, 2608.23311)；SDP reasoning/safety 方向耦合惩罚治 RIM (KAUST-inferred, 2608.23497)；training-free structured suffix modeling 加速 DLM 推理 (NJUST-inferred, 2608.23167)；Apodex 1.1 environment+coordination scaling agentic 报告 (single-source, 2608.23283)。⑤Games/WM ×2 — ReWorld pose-indexed landmark-bank bounded KV world model + metric-scale data engine + 4-step LoRA distillation (HKUST(GZ)+Alibaba-inferred, 2608.23565)；MBCCE MARL 新解概念 = decentralized no-regret learners 实际收敛点 (Liverpool-inferred, 2608.22840)
- Cross-cutting: harness 成为可学习一等公民（3 组独立量化 harness-vs-model 差距）；memory 受压成为本周高频失效模式；检索理论追上实践（multivector separation + context-allocation laws）；evaluation validity 持续受质疑（carousel metrics / harness artifacts / RIM）
- Updated: wiki/index.md (Synthesis 表顶部新增 arxiv-ai-search 2026-08-25 条目), wiki/log.md
- Contradictions: none（17 个 ID 全部 verified absent；affiliation 多为作者名单推断，已在文中标注 inferred/tentative；Apodex 1.1 为单源工业报告已标注待独立复现）

## [2026-08-25] synthesis | WQ101 Alpha Daily — WorldQuant 101 Alphas 美股 Top 20 精选 (2026-08-25)
- New page: wiki/synthesis/2026-08-25/wq101-alpha-daily.md
- Coverage: 延续 7 因子框架 (Alpha#1/#6/#12/#19/#30/#41/#53)，数据基准 = 8/24 (周一) 收盘 + ~9 组 web search (NVDA 财报前瞻、周一收盘详情、Micron/存储、TSLA robotaxi、电力股 CEG/VST/GEV、MRVL/AVGO、巨头财报、Jackson Hole/PCE/黄金/收益率、NBIS/SK 海力士)。本期核心判断：因子环境切换——NVDA 七连阴 (2022-10 以来最长) 使 AI 主线动量信号集体转负，榜单从"追动量"切换为"事件+反转"；实际收益率 20 年高位 + 30Y 5.25% + 各会议 30–60% 加息概率定价压制长久期资产；防御 rotation 确认 (Dow +0.26% vs Nasdaq -0.76%)。Top 20: Tier1 = GOOGL 8.7 / MSFT 8.6 / NVDA 8.5；Tier2 = AVGO 8.4 / MU 8.2 / CEG 8.2 / GS 8.1 / GEV 8.0 / VST 8.0 / META 7.9 / AMZN 7.9 / MRVL 7.8 / TSLA 7.7；Tier3 = INTC 7.6 / WDC 7.5 / STX 7.4 / AAPL 7.4 (新入榜，防御属性) / NBIS 7.2 / SKHY 7.2 / TLN 7.0。移出 SNDK (Q1 指引 miss)。含因子用法调整说明、打分规则、逐股卡片、总表、板块汇总、组合级风险 6 条
- Updated: wiki/index.md (Synthesis 表顶部新增 wq101-alpha-daily 2026-08-25 条目), wiki/log.md
- Contradictions: MRVL 财报日期修正 (昨日报告写 8/26，Zacks/TipRanks 实为 8/27，已在今日报告"口径修正"节声明)；SKHY ADR 代码与上市时点仍未官宣 (媒体近似口径已标注)；本文为定性推断非实时回测，已在文首与方法论双重声明

## [2026-08-26] synthesis | arXiv AI/LLM/RecSys Search Report
- New page: wiki/synthesis/2026-08-26/arxiv-ai-search.md
- Coverage: 15+ papers across CTR prediction, sequential modeling, generative recommenders, LLM inference, multi-agent RL/games, multimodal representation. Sourced from arXiv cs.AI, cs.IR, cs.LG listings (Aug 20–26, 2026).
- Key trends: Generative recommender tokenization (TAGR, Tlow, SST), mixed-polarity behavior sequences, LLM × recommendation alignment (DuELRec, UniSpecRec), multi-agent RL for system optimization (MARLIN), scaling laws for user representations (Densing Law).
