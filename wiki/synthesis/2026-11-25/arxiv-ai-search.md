---
title: arXiv Search Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources: [arxiv]
tags: [arxiv, ai, llm, recommendation, advertising, sequential-modeling, ctr, games]
---

# arXiv Search Report: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

**Search date:** 2026-11-25

**Queries (arXiv API, sorted by submitted date, newest first):**
- `(abs:LLM OR abs:"large language model" OR abs:"foundation model" OR abs:LFM)` (max 25)
- `(abs:recommendation OR abs:advertising OR abs:CTR OR abs:click-through-rate OR abs:sequential)` (max 30)
- `(abs:game OR abs:"video game" OR abs:"game AI")` (max 20)

**Notes:**
- The CTR-specific search terms returned no recent papers in the feed; the most CTR-adjacent work is in the recommendation and sequential-modeling sections.
- Institutional affiliations are taken from the arXiv feed; entries without a reported affiliation are marked "(not reported)".

---

## 1. AI & LLMs

### 1. AgentDRC: Multi-Agent Algorithms for Spatially-Aware Automated DRC Correction
- **arXiv:** https://arxiv.org/abs/2611.31876v1
- **Published:** 2026-11-24
- **Authors:** Pengju Liu; Nuo Xu; Winso Chen; Peijun Li; Yang; Zhao; Yu Cao; Caiwen Ding
- **Institution/Company:** Pengju Liu [Katie]; Nuo Xu [Katie]; Winso Chen [Katie]; Peijun Li [Katie]; Yang [Katie]; Zhao; Yu Cao; Caiwen Ding (as reported in the arXiv feed)
- **Abstract:** Design Rule Checking (DRC) error fixing remains a time-consuming bottleneck in physical design, often requiring manual intervention despite advanced EDA optimizations. Existing LLM-agent approaches fall short due to redundant contextual shapes, limited spatial reasoning over raw coordinates, and inefficient flat layout representations. We propose AgentDRC, which formulates iterative DRC correction as a multi-agent algorithm and introduces a spatial-aware verification and correction algorithm that reconstructs structured spatial relations among critical shapes and validates fixes through geometric and semantic constraint checking. The system coordinates four specialized agents to perceive multi-level, multi-modal geometric features, filter irrelevant shapes, and iteratively correct violations. Experiments show that AgentDRC achieves up to 30.4% pass@1 and 55.7% pass@5 on challenging violations, with 13.8% pass@5 improvement over the best baseline. We will open-source all code and benchmark tasks upon acceptance.
- **Key innovations:**
  - Formulates iterative DRC correction as a multi-agent algorithm with a spatial-aware verification/correction algorithm that reconstructs structured spatial relations among critical shapes.
  - Four specialized agents coordinate to perceive multi-level, multi-modal geometric features, filter irrelevant shapes, and iteratively correct violations.

### 2. No Fixed Configuration Is Best: Context- and Cost-Aware Tuning of LLM Pipelines, with an Application to Schema Matching and Mapping
- **arXiv:** https://arxiv.org/abs/2611.31864v1
- **Published:** 2026-11-24
- **Authors:** Gokhan Kirlik; Xiuwen Zheng; Anirudh Sriram
- **Institution/Company:** (not reported)
- **Abstract:** The numeric settings of a multi-stage LLM pipeline (a compound AI system) are the usual target of tuning. We tuned all of them for an LLM pipeline for schema matching and mapping, with accuracy and cost as joint objectives, and we show what this buys, what it cannot buy, and where the remaining accuracy is. First, tuning buys cost and a little accuracy. On 35 tasks, with whole groups of tasks held out from tuning, one tuned configuration gains 2.9 points of top-1 accuracy (HR@1) over the default at 18% more cost, and another keeps the accuracy of the default at 32% lower cost. Second, the accuracy depends on a choice that numeric tuning cannot reach. Restricting the search for each source column to one assigned target table changes HR@1 by +30 points on a MIMIC-III to OMOP task and by -52 points on a task built from database views, more than numeric tuning gains on nine of ten test tasks. Neither setting is right for all tasks: on the larger set of 41 tasks used for the remaining results, mean HR@1 is 75.7% with the restriction (the default) and 83.1% without it. Third, choosing the setting per task is not enough either: even an oracle that picks the better setting for each task reaches only 87.8% on the 41 tasks, because the better setting differs between the columns of one task. The pipeline therefore runs both settings, and an LLM judge chooses among their candidate answers on the 26% of columns on which they disagree. This reaches 91.5% HR@1 on the 41 tasks, at 5.9 times the cost of the default, about one cent per column.
- **Key innovations:**
  - Joint tuning of all numeric settings of a multi-stage LLM pipeline with accuracy and cost as objectives.
  - Table-assignment restriction is a per-column decision that changes HR@1 by up to +30 / -52 points; a per-column LLM judge arbitrates among disagreeing configs.
  - Cost-at-accuracy-parity configurations and a 5.9x configuration with 91.5% HR@1.

### 3. Ada-BFM: Adapting Behavior Foundation Models for Humanoid Scene Interaction
- **arXiv:** https://arxiv.org/abs/2611.31863v1
- **Published:** 2026-11-24
- **Authors:** Furui Xu; Weishuai Zeng; Zirui Wang; Kangning Yin; Jiacheng Bao; Huayi Wang; Yingying Qin; Yufei Xue; Yang Tang; Zenghao Tang; Kailin Li; Jingbo Wang; Weinan Zhang
- **Institution/Company:** (not reported)
- **Abstract:** Behavior Foundation Models (BFMs) have emerged as a promising paradigm for general-purpose humanoid control through pretraining on large-scale behavioral data. However, their proficiency in whole-body coordination does not readily extend to scene interaction, which requires adapting motion to scene-dependent geometric constraints and contact dynamics. To bridge this gap, we introduce Ada-BFM, a post-training framework that adapts pretrained BFMs for humanoid scene interaction. Ada-BFM augments the original architecture with a lightweight adapter, enabling interaction-specific adjustments while leveraging pretrained control capabilities. Rather than producing a separate controller for each task, the framework yields a shared model for each interaction domain, supporting diverse tasks involving terrain or object interaction. Extensive experiments in simulation and the real world demonstrate that Ada-BFM enables diverse scene interaction behaviors, accelerates learning compared with training from scratch, and largely preserves pretrained behavioral competence. These findings establish Ada-BFM as an effective and efficient approach to extending the capabilities of BFMs beyond their pretraining settings while retaining their strengths in general whole-body control.
- **Key innovations:**
  - Post-training framework adapting pretrained Behavior Foundation Models with a lightweight adapter, yielding a shared model per interaction domain.
  - Accelerates learning vs. training from scratch and preserves pretrained whole-body competence while enabling diverse scene interactions.

### 4. Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models
- **arXiv:** https://arxiv.org/abs/2611.31821v1
- **Published:** 2026-11-24
- **Authors:** Keyu He; Michael Li; Jiarui Liu; Mingqian Zheng; Koichi Onoue; Tongshuang Wu; Maarten Sap
- **Institution/Company:** (not reported)
- **Abstract:** The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with teammates and infer hidden roles, while their rules provide an objective outcome which can serve as a verifiable reward for training. Using three social games, we explore how much social intelligence Qwen3 models can acquire through supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). Results show that against a much stronger Gemma-3-27B model, SFT and RLVR raise the win rate of Qwen3-4B from 33% to 81% on the three trained games, and from 39% to 54% on three additional held-out games. In contrast, in-context strategies such as prompting improve the win rate of Qwen3-4B by only about 6 pp across the same games we train and evaluate on. Furthermore, we show that the gains from SFT and RLVR hold across the model sizes 1.7B, 4B, and 32B. Qualitative analyses of agent behavior show signs of stronger social intelligence; for example, trained agents tend to share information more openly, check each other's claims against public evidence, and coordinate their votes. More broadly, our results demonstrate that training LLMs on verifiable outcomes in social games can cultivate generalizable social behaviors, which offers a scalable path for building socially intelligent agents.
- **Key innovations:**
  - Uses multi-player social games as RLVR training grounds with objective game outcomes as rewards.
  - Qwen3-4B win rate 33% -> 81% vs Gemma-3-27B (trained) and 39% -> 54% (held-out); in-context prompting only improves ~6pp.
  - Trained agents show generalizable behaviors: information sharing, cross-checking claims against public evidence, coordinated voting.

### 5. Verified Proof Refactoring with Codex and Qwen
- **arXiv:** https://arxiv.org/abs/2611.31762v1
- **Published:** 2026-11-24
- **Authors:** Lazar Milikic; Gordan Đurić; Viktor Kunčak
- **Institution/Company:** (not reported)
- **Abstract:** We refactor existing Lean 4 proofs to reduce source length and checking cost while preserving theorem statements and compatibility across Lean versions. A locally served Qwen model uses the open-source Codex CLI to inspect source, retrieve declarations, and test proof replacements. The host keeps a replacement only if it improves the objective and Lean accepts it on every required version. A deterministic CPU pass then refines the verified proofs. On the 60 problems in Lean Refactor Arena, model search achieves a local mean combined score of 82.07, and cleanup raises it to 82.18. The final proofs pass all 127 required proof--version checks. Our system placed first in the open-source LLM track of Lean Refactor Arena at VeriCodeGen.
- **Key innovations:**
  - LLM (locally served Qwen via Codex CLI) proof refactoring with version-gated acceptance ("only kept if Lean accepts on every required version").
  - Deterministic CPU cleanup pass after model search; won the open-source LLM track of VeriCodeGen.

### 6. Can Latent Reasoning Drive LLM Outputs Without a Trace?
- **arXiv:** https://arxiv.org/abs/2611.31015v1
- **Published:** 2026-11-23
- **Authors:** Tomer Ashuach; Zorik Gekhman; Avi Caciularu; Ori Ram; Jonathan Herzig
- **Institution/Company:** (not reported)
- **Abstract:** LLMs typically solve complex tasks with chain-of-thought (CoT) reasoning, which is also the main tool for monitoring them for misaligned behavior. However, standard transformers can also solve tasks with complete latent reasoning (CLR), carrying out the whole task internally and outputting only the final answer. Theory bounds the depth of CLR, the number of sequential steps it can carry out, and recent work measured it to be shallow. In this work, we ask whether CLR is deep enough for a model to pursue a hidden objective that requires reasoning. Such a model would generate a CoT that appears to solve the given task, while a latent multi-step computation decides its answer based on the hidden objective. First, we show that a simple auxiliary loss allows models to solve a multi-step task latently at least 5x deeper than previously reported. Then, in two common tasks, decision-making and code generation, we train a model to pursue such a hidden objective, which decides a loan or plants a vulnerability. The model's CoT justifies the output with no trace of the hidden objective, and a strong LLM monitor does not flag it. Finally, using activation patching, we find that the latent computation is completed before the model generates its CoT, which takes no part in it. Altogether, we show that a hidden objective that requires reasoning can go unseen by a monitor that reads only the output.
- **Key innovations:**
  - Simple auxiliary loss lets models do complete latent reasoning (CLR) at least 5x deeper than previously reported.
  - Trains models to pursue hidden objectives (loan decision / planted vulnerability) whose CoT is trace-free by design.
  - Activation patching shows the latent computation completes before the CoT is generated; a strong LLM monitor does not flag the output.

## 2. Recommendation & Advertising

### 7. From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization
- **arXiv:** https://arxiv.org/abs/2611.31052v1
- **Published:** 2026-11-23
- **Authors:** Adeep Hande; Shaghayegh Agah; Neeraj Sharma; Karina Halevy; Sardar Hamidian
- **Institution/Company:** (not reported)
- **Abstract:** Recommender systems exhibit popularity bias, often under-serving long-tail and cold-start items with sparse interaction data. We propose a group-specific data augmentation approach that leverages LLMs to generate synthetic interactions, formulated as a constrained optimization problem, maximizing group-specific NDCG@20 and coverage while bounding overall NDCG@20 degradation within an acceptable threshold. Items are partitioned by interaction frequency to find the optimal augmentation strategy for each group. We further study combining the augmentation across groups simultaneously and find that while individual optimal strategies navigate the multi-group augmentation design, they are not simply additive. We further ablate on the LLM-based augmentation itself, comparing LLM scales, augmentation configuration under token constraints, finding that augmentation quality scales with contextual richness, albeit at a proportionally higher cost. Experiments with SASRec demonstrate the effectiveness of the proposed approach, achieving over 100% and 60% improvement in group-specific NDCG@20 for extreme and regular long-tail items, respectively, on our industrial dataset, and 40%, 25% for MovieLens-32M, while increasing their coverage without significant overall degradation.
- **Key innovations:**
  - LLM-generated synthetic interactions targeted at long-tail/cold-start items, as a constrained optimization (maximize group NDCG@20 + coverage, bound overall NDCG@20).
  - Group-specific augmentation strategies via frequency-based item partitioning.
  - ablation over LLM scale; >100% and 60% NDCG@20 gains for extreme and regular long-tail items.

### 8. AdProducer: Towards Agentic Advertising Video Generation
- **arXiv:** https://arxiv.org/abs/2611.31466v1
- **Published:** 2026-11-23
- **Authors:** Kunyang Li; Chaoyang Wang; Mubarak Shah; Yuzhang Shang
- **Institution/Company:** (not reported)
- **Abstract:** Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelling, which requires more than visual synthesis: it calls for deeper product understanding and strategic decisions about how to present product value. Crucially, product research and creative design are closely intertwined, as the information gathered about a product determines which features can be faithfully demonstrated and how they should be presented. In this paper, we introduce AdProducer, the first end-to-end agentic framework for advertising video creation, transforming concise creative briefs into finished advertisements. Our multimodal agent autonomously researches products through web and image search and translates its findings into selling-point-driven storyboards that guide a frozen video generator. To achieve this, we develop a dedicated data construction pipeline that yields two training datasets, AdProducer-SFT and AdProducer-RL, and train the agent through supervised fine-tuning followed by reinforcement learning with joint optimization of storyboard- and video-level rewards. We further introduce AdCreation-Bench, comprising 305 advertising briefs across eight domains, with two complementary metrics: PG-Score for product correctness and creative execution, and Ad-Score for overall advertising effectiveness assessed by an independent judge. Experiments demonstrate that AdProducer improves the PG-Score of MiniMax H3 from 17.3 to 51.3 and generalizes to Veo 3.1 without additional training, improving its score from 28.0 to 35.9, with consistent gains in Ad-Score, VideoScore2, and human evaluations. Code, models, and data are released.
- **Key innovations:**
  - First end-to-end agentic framework: brief -> product research -> selling-point storyboard -> frozen video generator.
  - SFT + RL training with joint storyboard/video rewards; releases AdProducer-SFT/RL and AdCreation-Bench (305 briefs, 8 domains).
  - Strong gains: MiniMax H3 PG-Score 17.3 -> 51.3; Veo 3.1 28.0 -> 35.9.

### 9. Needwise: Generation-Free Conversational Recommendation from Need-Level Typed Decisions
- **arXiv:** https://arxiv.org/abs/2611.31175v1
- **Published:** 2026-11-23
- **Authors:** Sungchul Kim; Weixiao Huang; Mekala Raja Sekhar Reddy; Amrutha Srinivasan
- **Institution/Company:** (not reported)
- **Abstract:** Conversational recommenders must rank items against needs that catalogs record only in part, while users add, withdraw and reverse needs and switch between requests. LLM rankers re-read the dialogue at every turn: they are slow, and their ordering does not show which needs an item meets. We show that a conversational recommender can be built from typed decisions instead: named questions over fixed options, answered with option probabilities rather than generated text. On each turn, one typed request maps the message onto the catalog's fields, keeps what no field expresses in the user's words, and decides how the turn changes each earlier need. Needwise then ranks candidates must-first: the needs on the kind of item, its place and its price form a tier, and within it one holistic decision and need-level verdicts (supported, contradicted or unknown) are combined with equal weight (Needwise-HF). With the graded attributes withheld from the records, so that needs must be inferred from names, descriptions and reviews, Needwise-HF ranks Google Local requests significantly better than GPT-6 Sol (0.383 against 0.343 nDCG@10) and is not significantly different from the strongest LLM ranker on Google Local and Yelp; these comparisons keep their sign under every treatment of unrecorded attributes we test. It costs a fraction of GPT-6 Sol's API price and answers in 2.5 s at the median on Google Local, against 5.6 s for GPT-6 Sol. In conversations, the typed state keeps the ranking across switches and returns, but it recognizes only 19-27% of withdrawn needs.
- **Key innovations:**
  - Generation-free: typed decisions (named questions over fixed options) replace per-turn LLM re-ranking; keeps a persistent typed state across switches/returns.
  - Needwise-HF combines holistic decision + need-level verdicts (supported/contradicted/unknown) with equal weight.
  - Better than GPT-6 Sol on Google Local (0.383 vs 0.343 nDCG@10) with ~2.2s lower median latency.

## 3. Sequential Modeling & Speculative Decoding

### 10. Wavefront: Low-Rank Drafting with Parallel Causal Refinement for Speculative Decoding
- **arXiv:** https://arxiv.org/abs/2611.31638v1
- **Published:** 2026-11-23
- **Authors:** Huy Huu Nguyen; Xin Huang
- **Institution/Company:** (not reported)
- **Abstract:** Speculative decoding accelerates LLM inference by letting a cheap drafter propose tokens that the target model verifies in parallel. Parallel block drafters such as DFlash and P-EAGLE propose a whole block in one forward pass, but they lose the dependence between tokens in the block; DSpark restores part of it with a lightweight correction head that runs sequentially. Measuring DSpark, we find that this head overrides the base prediction on most slots, so the expensive base readout through the target's full lm_head mostly provides a seed. We therefore propose Wavefront, which follows a simple principle: shrink the base and strengthen the correction head. Wavefront replaces the full lm_head with a learned low-rank base, conditions the correction head on the whole drafted prefix within the same block, and resolves it with a few parallel Jacobi passes. A fixed pass budget makes the draft step free of data-dependent control flow, so we capture it as a single CUDA graph in vLLM with fused kernels. On Qwen3-8B, Wavefront improves throughput over xPress, DSpark and DFlash by 2.6%, 10.7% and 23.6% on average across math, code, chat and agentic benchmarks, and by 9.6%, 14.3% and 28.9% on SPEED-Bench long-context prompts. On Qwen3.8-27B it leads DFlash2, DSpark and xPress by 7.6%, 10.6% and 5.0%, and by 7.4%, 5.8% and 6.0% on the same long-context prompts. The gains persist as serving load grows to concurrency 32.
- **Key innovations:**
  - Principle: shrink the base, strengthen the correction head (replaces full lm_head with a learned low-rank base).
  - Correction head conditions on the whole drafted prefix; resolved with parallel Jacobi passes, captured as one CUDA graph in vLLM with fused kernels.
  - Up to 23.6% throughput gain over DFlash (Qwen3-8B, avg) and 28.9% on SPEED-Bench long-context.

### 11. XRL4T1D: A Post-hoc Explainability Framework for Reinforcement Learning in Type 1 Diabetes Management
- **arXiv:** https://arxiv.org/abs/2611.31498v1
- **Published:** 2026-11-23
- **Authors:** Malay Phadke; Chirath Hettiarachchi
- **Institution/Company:** (not reported)
- **Abstract:** Type 1 diabetes (T1D) requires lifelong insulin therapy, and reinforcement learning (RL) has shown promise for automated dosing in the UVA/Padova simulator. However, the decisions of RL controllers remain difficult to interpret. We present XRL4T1D, a post-hoc explainability framework for evaluating pretrained insulin-dosing policies without retraining. Each policy uses 60 minutes of continuous glucose monitor (CGM) and administered-insulin history, sampled every 5 minutes, to recommend insulin. We use SHapley Additive exPlanations (SHAP) to compare the importance of CGM and insulin-history inputs and summarize insulin-history attributions over three 20-minute windows motivated by insulin-on-board. We assess whether these attributions correspond to policy-output sensitivity through targeted input replacement and compare temporal rankings with TimeSHAP. In all 80 patient-policy-mask-size cases, replacing the highest-attribution inputs changes the normalized insulin recommendation more than replacing the lowest-attribution or random inputs. The highest-attribution insulin-history window is also the most output-sensitive in 115 of 120 patient-policy-scenario configurations, and KernelSHAP and TimeSHAP select the same top window in 111 of 120. Applying XRL4T1D to PPO and G2P2C across 20 virtual patients, we find that both controllers rely predominantly on CGM history, especially G2P2C. However, the distribution of insulin-history importance across recent, middle, and older windows varies by cohort, explainer, and analysis settings, without a consistent separation between controllers. Global feature-attribution rankings remain stable under the tested observation corruptions. These results show why attribution fidelity, temporal reproducibility, and controller-comparison robustness should be assessed separately.
- **Key innovations:**
  - Post-hoc SHAP-based explainability of pretrained insulin-dosing RL controllers without retraining.
  - Three 20-minute insulin-history windows (insulin-on-board motivated) with SHAP attributions, validated via targeted input replacement; cross-checked with TimeSHAP.
  - Both PPO and G2P2C controllers rely predominantly on CGM history; window importance varies by cohort/explainer.

## 4. Games

### 12. AlphaDefect: Expert-Level AI for Slay the Spire 2
- **arXiv:** https://arxiv.org/abs/2611.31076v1
- **Published:** 2026-11-23
- **Authors:** Qiyue Chen; Taian Yu; Junpei Komiyama; Haobo Huang
- **Institution/Company:** (not reported)
- **Abstract:** Slay the Spire 2 (STS2) is a single-player deck-building game that requires long-term planning under heavy randomness. We present AlphaDefect, an expert-level AI system for STS2: for each character, one network trained with proximal policy optimization (PPO) makes every decision of a run, in combat and outside it. At the highest difficulty, Ascension 10, on two versions of the game current in November 2026 and on test seeds not played in training, AlphaDefect wins 62-77% of runs across six characters with greedy play and 68-80% with test-time search, after 1.3 to 6.7 billion decisions of training per character; runs uploaded by human players of all levels are won 11-20% of the time at the same difficulty. The networks read the game as entity records that identify each card, relic and enemy through a learned embedding and attributes from the game data, together with consequences of public information computed by the engine. Ablations show how much the agent depends on this encoding: without these identities, the network did not win a single run, and without the computed consequences it won 8.3 points fewer. To our knowledge, AlphaDefect is the strongest publicly reported STS2 agent as of November 2026.
- **Key innovations:**
  - PPO-trained per-character expert for STS2 (wins 62-80% at Ascension 10 on unseen seeds).
  - Game encoded as learned entity embeddings (card/relic/enemy) + engine-computed consequences.

### 13. GameDoji: Benchmarking Real-Time Interactive Agents in Video Games
- **arXiv:** https://arxiv.org/abs/2611.30771v1
- **Published:** 2026-11-23
- **Authors:** Kuan Zhang; Zhihao Yang; Yukun Chen; Xingyilang Yin; Mingyu Ouyang; Yue Su; Xiangnan Wu; Jiaming Li; Longze Chen; Run Luo; Zirong Chen; Lu Wang; Yiming Li
- **Institution/Company:** (not reported)
- **Abstract:** Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss encounters across 20 games for evaluating model capabilities, learning algorithms, and agent harnesses. Coding agents reconstruct the environments and write gameplay scripts, producing GameDoji-Data with 600 hours of gameplay trajectories. Experiments reveal substantial challenges for frontier models, especially in real-time interaction. Training on GameDoji-Data brings GameDoji-4B to frontier performance, with the strongest real-time performance. We also find joint training improves individual tasks, and learned policies transfer across bosses. Together, these findings establish GameDoji as a challenging and valuable interactive gameplay benchmark for the community. Our project page is at https://gamedojo-benchmark.github.io/ , and our code is at https://github.com/THUSI-Lab/GameDojo .
- **Key innovations:**
  - Interactive gameplay benchmark: 120 boss encounters across 20 games; coding agents produce GameDoji-Data (600h of trajectories).
  - Frontier models lag especially in real-time interaction; training on GameDoji-Data brings smaller models to frontier performance.

### 14. Off-the-Shelf Autonomous Agents for Game Playtesting
- **arXiv:** https://arxiv.org/abs/2611.31570v1
- **Published:** 2026-11-23
- **Authors:** Ayush Maniar; Eryk Banatt
- **Institution/Company:** (not reported)
- **Abstract:** In playtesting games, a human operator is typically required to test most gameplay elements. In this work we present Buddy, an autonomous game solving agent which can solve long time horizon objectives in an unseen 3D role-playing game using off-the-shelf language model systems. Buddy will take actions, receive feedback on those actions, and pursue a goal across many turns. No written walkthrough or model training of any kind is required, and we show that this paradigm holds in a novel environment where the agent must discover solutions via exploration rather than recalling them from pretraining. We demonstrate three downstream capabilities: game solving with no provided walkthrough, logging bug tickets for encountered difficulties, and conversion of successful agent traces into scripted hierarchical task networks for regression testing. Unlike existing playtesting solutions, our framework is fully modular: language models and harnesses can be easily swapped out as capabilities improve over time.
- **Key innovations:**
  - Off-the-shelf LLM game-solving agent (Buddy) for long-horizon objectives in an unseen 3D RPG, no training or walkthrough.
  - Also logs bug tickets and converts agent traces into scripted HTNs for regression testing.

### 15. WorldLeague: Benchmarking Physical Agency
- **arXiv:** https://arxiv.org/abs/2611.30989v1
- **Published:** 2026-11-23
- **Authors:** Xinyang Zhou; Qi Li; Xinchao Wang
- **Institution/Company:** (not reported)
- **Abstract:** AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms. What range of physical goals can today's AI systems achieve autonomously? Answering this question requires testing systems on tasks that demand different combinations of perception, memory, planning, and action. We introduce WorldLeague, a benchmark that compares AI systems on a common set of 60 simulated robot tasks by measuring progress toward each task's physical goal from the robot's trajectory. Robots explore scenes to gather evidence in WorldSeek, rearrange objects in WorldShape, and adapt to changes in WorldShift. Tying these goals to a single control interface limits which AI systems can be compared. In WorldLeague, vision-language models (VLMs) choose targets and motions, while vision-language-action models (VLAs) and world-action models (WAMs) use their native controls. For each of six capability dimensions, we measure how much progress a system makes toward its goals (Interactive Score) and how often it achieves them (physical success rate). Together, these measures form the system's Physical Agency Profile. Among 13 representative AI systems, Claude Fable 5.2 achieves 13 of the 60 goals and earns the highest mean Interactive Score (28.58/100). Fable leads in four dimensions, while GPT-6.1-Sol and GPT-6-Astra tie for first on rule-following tasks. Even when VLMs answer every final question correctly, they receive an Interactive Score of zero in 71.8% of those episodes. WorldLeague gives Embodied AI, Physical AI, and Agentic AI a shared basis for comparing what AI systems achieve autonomously, from partial progress toward a physical goal to full goal completion. Project Webpage: https://xyangzhou.github.io/WorldLeague
- **Key innovations:**
  - Benchmark of 60 simulated robot tasks across WorldSeek/WorldShape/WorldShift with a Physical Agency Profile (Interactive Score + success rate).
  - Reports VLMs reaching Interactive Score 0 in 71.8% of episodes; Claude Fable 5.2 leads (13/60 goals, 28.58/100).

### 16. Heterogeneous Risk-Sensitive Evolutionary Learning in Coordination Games: Polarization, Welfare Loss, and Intervention for Efficiency
- **arXiv:** https://arxiv.org/abs/2611.31568v1
- **Published:** 2026-11-23
- **Authors:** Solaleh Mohammadi; Yiman Fong; Kaiqing Zhang
- **Institution/Company:** (not reported)
- **Abstract:** We study evolutionary learning in coordination games in a finite population of agents with heterogeneous risk attitudes, modeled using the entropic risk measure (ERM). The population consists of two subpopulations, each with a fixed risk attitude. Under risk-sensitive best response with mutations (BRM), we characterize the long-run outcomes of the learning process. In particular, we characterize when a polarized state, in which the two subpopulations choose different actions, is uniquely stochastically stable in terms of agents' risk attitudes and the subpopulation sizes. Notably, this polarized state is strictly Pareto dominated by the payoff-dominant equilibrium under both expected payoffs and agents' own ERM-adjusted payoffs. Moreover, its welfare, measured by average expected payoff, is always lower than that of the payoff-dominant equilibrium and can also be lower than that of the risk-dominant equilibrium. Thus, heterogeneity of risk attitudes in learning alone can lead to an inefficient long-run outcome. To mitigate such inefficiency, we propose intervention mechanisms to modify agents' risk attitudes in learning. We show that a sufficiently large intervention share (the fraction of agents modified) and sufficiently high intervention intensity (the increase in their risk parameter) ensure that the payoff-dominant equilibrium is uniquely stochastically stable. However, greater intervention intensity cannot compensate for an insufficient intervention share, and a larger intervention share cannot compensate for insufficient intervention intensity.
- **Key innovations:**
  - Characterizes risk-attitude heterogeneity's effect on long-run stability of polarized vs. coordination states.
  - Intervention mechanisms (share + intensity) to restore efficiency; intensity and share cannot substitute for each other.

### 17. CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting
- **arXiv:** https://arxiv.org/abs/2611.31185v1
- **Published:** 2026-11-23
- **Authors:** Ramraj Chandradevan; Sayontan Ghosh; Vinoth Selvendran
- **Institution/Company:** (not reported)
- **Abstract:** Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a single trajectory under closed-loop execution with live retrieval. Each policy controls a mutually exclusive subset of four functional roles: intermediate reasoning, search-or-answer decision, search query generation, and final answer extraction. Evaluating all 2^4=16 role assignments without modifying weights or retraining defines a cooperative game whose Shapley values decompose the total RL gain across roles, while Möbius interaction terms distinguish standalone role improvements from multi-role coupling. Applying CO-GRAFT to Search-R1 agents across Qwen2.5 and Llama-3.2 models (spanning two sizes, base and instruction-tuned initializations, GRPO and PPO optimizers, and NQ and HotpotQA datasets), we show that query generation never exceeds 15% of the total gain; instead, gains are governed by pre-RL answer validity, search retention, model scale, and fixed task-level search budgets, shifting credit from reasoning toward answer extraction in larger or well-formatted answer response checkpoints while smaller base models rely on reasoning--decision coupling.
- **Key innovations:**
  - Reward-agnostic interventional attribution: RL agent + pre-RL init jointly generate trajectories; roles = 4 functional subsets.
  - Shapley values over the 2^4 role assignments; Möbius terms separate standalone vs coupled role gains.
  - Finding: query generation <= 15% of RL gain; gains driven by answer validity, search retention, model scale, task budgets.

### 18. The Computational Complexity of Concurrent Stochastic Games: Exact Value and Approximation
- **arXiv:** https://arxiv.org/abs/2611.30447v1
- **Published:** 2026-11-23
- **Authors:** Ali Asadi; Krishnendu Chatterjee
- **Institution/Company:** (not reported)
- **Abstract:** We consider two-player zero-sum concurrent stochastic games played over a finite state space for an infinite number of stages. In every stage, both players simultaneously and independently choose an action. Then, given the current state and chosen actions, the successor state is selected according to a stochastic transition function. We consider limit-average objectives, where Player 1 maximizes the long-run average of rewards assigned to every transition. The value from an initial state is the maximal expectation that Player 1 can ensure. We study the two basic computational problems: (a) the approximation problem of computing the values within an arbitrary additive error, and (b) the exact problem of deciding whether the value at a state is at least a given threshold. The previous results in the literature establish: (a) the approximation problem belongs to TFNP[NP], and (b) the exact problem belongs to PSPACE, via the theory of the reals, and is SQRT-SUM-hard. Our contributions are as follows. (a) Our main result shows that the approximation problem is in TFNP, and that the associated gap or promise problem is in NP ∩ coNP. (b) We also show that the exact problem is in ∃R ∩ co-∃R, i.e., it reduces to both the existential and the universal theory of the reals, and that it is PosSLP-hard.
- **Key innovations:**
  - Approximation problem in TFNP with promise problem in NP ∩ coNP (main complexity result).
  - Exact problem in ∃R ∩ co-∃R (reduces to existential and universal theories of the reals) and PosSLP-hard.

---

*Report generated from arXiv API query results fetched 2026-11-25 (sorted by submittedDate, newest first).*
