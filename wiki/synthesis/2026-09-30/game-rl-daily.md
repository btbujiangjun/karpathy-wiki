---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-30)"
type: synthesis
created: 2026-09-30
updated: 2026-09-30
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, game-foundation-models, pcg, benchmarks, self-play, world-models, marl, exploration, imperfect-information, causal-rl, godot, engine-tooling, player-experience, single-player, sota-gap, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-30)

> **First window with game content since the 09-29 pivot.** The Tue-29-Sep batch has now been indexed. Yesterday's digest reported a *verified* window-level game vacancy across all 1,059 unclaimed papers in IDs 2609.30361–2609.31620. This run covers the immediately following window, **IDs 2609.31757–2609.35771, 3,678 papers, `published` 2026-09-25T18:00Z → 2026-09-28T17:58Z**, and it does **not** repeat that result: **6 papers in the new window alone**, plus 15 from a topic sweep. Read §0 for why the two days are not in tension.

---

## §0 Method and Corpus

### 0.1 Window (Part I)
- **Oracle**: category-agnostic `submittedDate:[202609260000 TO 202610010000]`, paginated to exhaustion (19 requests × 200/page), `totalResults=3678` matched exactly at 3,678 entries retrieved.
- **Boundary check**: newest paper in the unfiltered descending index is `2609.35754` at `published=2026-09-28T17:58:21Z`. Yesterday's ceiling was `2609.31620` at `2026-09-25T17:59:59Z`. **The window moved by 4,134 IDs.**
- **Dedup**: whole-`wiki/` regex sweep over `2[0-9]{3}\.[0-9]{4,5}` → **7,037 unique arXiv IDs already claimed** across `wiki/**/*.md`. Result: **0 of 3,678 window papers already claimed** — this window is entirely disjoint from every prior digest. (Yesterday's 09-29 run claimed 0 in its window, so this is consistent, not anomalous.)
- **Screen**: 30-token strict game regex over title + abstract + comment → 157 hits; tightened to a hard gate (must name a real game, engine, or game-making artifact) → 45. Manual adjudication → 6 genuine game papers.
- **Primary-category mix**: cs.LG 587 / cs.AI 427 / cs.CV 385 / cs.CL 212 / cs.RO 173 / quant-ph 110 / cs.CR 75 / math.CO 70 / math.AP 69 / math.OC 63.

### 0.2 Topic sweep (Part II)
Per the standing rule proposed on 09-29, this run carries **both** a window pass and a rolling topic sweep. **109 queries** across game RL, LLM game agents, game foundation models, PCG, benchmarks, industry game AI, and related techniques → **6,442 raw entries → 4,411 unique IDs** → 3,868 unclaimed → **2,386 pass a hard game-domain gate** → filtered to `published >= 2026-08-01` for coverage **not already delivered by the 09-29 retrospective sweep**, which mined 2025-09 → 2026-09 comprehensively.

### 0.3 Why yesterday's "vacancy" and today's 6 papers are the same fact
The 09-29 report's §0.1 argued that game yield sits **below the noise floor of a 1,260-paper window**. Today's window is 3,678 papers and yields 6. That is a rate of 0.16%, consistent with a sparse-but-real field: a window can be empty on a given day and yield half a dozen the next. **The operational rule that falls out: read "0 game papers" as a statement about the sample, never about the field.** The topic sweep is the instrument that measures the field; the window is the instrument that measures latency.

---

## §1 Game RL — Reinforcement Learning in Games

### ★ SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing
- **Authors**: Zhiwei Chen, Tianchun Wang, Zhongtao Rao, Haiming Zhu, Ding Cao, Tianxiang Zhao
- **Affiliation**: HKUST (Guangzhou) / Johns Hopkins / **Microsoft** / Fudan / USTC *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.34342 (28 Sep 2026) — cs.AI, 31 pages
- **Abstract**: A strong LLM strategic agent must reason prospectively over uncertain futures, adapt to opponents' behavioral tendencies, and continuously recalibrate from interaction experience. Free-form reasoning produces unsupported strategic assumptions, inconsistent opponent estimates, and interference from irrelevant history. SAGE is a **training-free inference-time** framework structuring reasoning around three operations — **anchor** (bind reasoning to a computed equilibrium policy as a strategically valid prior), **adapt** (condition deviations from the anchor on a soft belief over opponent tendencies, enabling opponent-specific exploitation), and **recalibrate** (distill strategically related interactions into counterfactual hypotheses about previously-missing considerations). Evaluated on three repeated imperfect-information games — **Leduc Hold'em, Liar's Dice, Goofspiel** — against varied opponent types, versus Suspicion-Agent, ReTA, Agent-Pro, EMO, Hypothetical Minds.
- **Key innovations**: (1) equilibrium policy as a *reasoning anchor* rather than a search primitive — this is the load-bearing idea, and it is what makes the method training-free; (2) opponent modeling as a soft belief gating deviation from the anchor, i.e. exploitation is a *conditional* on the anchor rather than a replacement of it; (3) history compressed into counterfactual hypotheses, which is a claim that most retrieved interaction history is *noise* and should be filtered by strategic relevance before entering context.
- **Results**: up to **+127.6% payoff** in Liar's Dice over reasoning-intensive LLM agents, while cutting input tokens up to **80%** and output tokens up to **90%**. Non-negative mean payoff vs **5/10, 8/10, 8/10** opponents in Leduc Hold'em / Liar's Dice / Goofspiel respectively, at lower token cost.
- **Assessment**: the token-reduction result is the more interesting half. A method that wins *and* cuts output tokens by 90% is attacking the actual cost driver of LLM game agents, not just accuracy. ⚠️ All three games are small discrete games with closed-form equilibria; the anchor operation presupposes an equilibrium is computable, which will not hold for StarCraft/Dota-scale games. Code: `github.com/chenzhwsysu57/SAGE`
- **Link**: https://arxiv.org/abs/2609.34342

### ★ Modular Discovery of General Game-Playing Algorithms with Large Language Models
- **Authors**: Zun Li, John Schultz, Marc Lanctot, Daniel Hennes
- **Affiliation**: **Google DeepMind** *(verified — all four authors; Lanctot and Hennes marked "work done while at Google DeepMind")*
- **Venue**: arXiv:2609.33115 (27 Sep 2026) — cs.AI / cs.GT / cs.MA
- **Abstract**: General Game Playing from rules alone is hard because game classes need different algorithms and decision-time is strictly constrained. Rather than hand-designing search heuristics per domain, this work uses LLMs as a **proposal engine over algorithmic design space** — language models can propose and refactor structured code. A multi-agent LLM meta-learning system co-evolves **game-agnostic procedural search mechanisms in C++** alongside domain heuristics synthesized directly from game rules.
- **Key innovations**: (1) the discovered artifact is **C++ search code**, not a policy — an explicit bet that algorithmic structure transfers across games better than learned weights do; (2) multi-agent co-evolution, with game-agnostic mechanisms and game-specific heuristics evolving together; (3) evaluation controlled for compute budget, which is the honest way to claim discovered code is efficient rather than just searched harder.
- **Results**: benchmarked across **400+ environments** — OpenSpiel training and held-out games, procedural simulation engines, and games with deep neural policy-value representations trained via PPO. Evaluated via **AlphaRank stationary distributions and Soft Condorcet Optimization (SCO)** against **15 established MCTS baselines**; discovered mechanisms achieve top-tier ratings and pairwise ballot majorities over most baselines across independent evolutionary runs, generalize to unseen human-designed and procedurally synthesized games, and stay competitive on frozen neural network representations.
- **Assessment**: **this is the most institutionally significant paper in the digest** — it is a frontier lab doing open-ended algorithmic discovery in game playing, and the "generalist player" framing (one search mechanism spanning 400+ environments) directly continues the line the [[Game Foundation Models]] line was reaching for. The C++ choice signals that a neural policy alone is not seen as sufficient for general game playing.
- **Link**: https://arxiv.org/abs/2609.33115

### ★ GraphHCA: Closed-Form Hindsight Credit Assignment for Long-Horizon LLM Agents
- **Authors**: Haodong Zhu, Yangyang Ren, Changbai Li, Sheng Xu, Linlin Yang, Haiguang Liu, Baochang Zhang
- **Affiliation**: not listed in arXiv API or HTML header *(tentative: Huazhong University of Science and Technology / Huazhong Normal / UCL, inferred from author cohort — unverified)*
- **Venue**: arXiv:2609.35084 (28 Sep 2026) — cs.LG
- **Abstract**: Group-based RL extends to agentic tasks where sparse terminal rewards make step-level credit assignment essential. Existing methods assign credit from *what follows an action* in sampled rollouts, never capturing its *retrospective* relation to the realized outcome. Hindsight Credit Assignment (HCA) attributes credit via the ratio of hindsight to behavior-policy probabilities, but estimating the hindsight distribution needs an auxiliary model or an extra pass. GraphHCA is a **model-free realization of HCA that eliminates explicit hindsight-distribution estimation**: for terminal-goal tasks with deterministic transitions, Bayes' rule reduces the hindsight ratio to a ratio of behavior-policy success probabilities at consecutive states; taking logs yields a state-wise success potential whose increment across a transition gives step-level credit. Estimated from pooled rollouts by a discounted recursion on the induced transition graph, which admits a unique fixed point on any directed graph.
- **Key innovations**: (1) the elimination of the auxiliary hindsight model is the contribution — HCA was previously not practical for this reason alone; (2) the unique-fixed-point-on-any-directed-graph property is a clean theoretical guarantee; (3) **recovers GRPO exactly when the step-level weight is zero**, which is the right way to present an additive refinement.
- **Results**: state-of-the-art among compared baselines on ALFWorld and WebShop at both LLM scales, and on **Sokoban with a vision-language agent**. Up to **+24.6 points** over GRPO on ALFWorld, up to +4.7 points over the strongest step-level baseline.
- **Assessment**: the deterministic-transition requirement is the load-bearing assumption and it is *narrower* than it looks — Sokoban qualifies, but stochastic or partially-observed games do not. The 24.6-point gap over GRPO is large enough that the "GRPO leaves the signal on the table in long-horizon tasks" claim is plausible on its face. See also §7 CRBC, from an overlapping author group.
- **Link**: https://arxiv.org/abs/2609.35084

### RSD-Poker: Structure-Adaptive and Shift-Robust Risk-Utility Certification for Residual Policies
- **Authors**: Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Peng Zhang, Daren Zha, Jun Xiao
- **Affiliation**: not listed *(tentative: University of Macau / University of Arizona cohort — unverified)*
- **Venue**: arXiv:2609.33669 (27 Sep 2026) — cs.AI / cs.GT / cs.LG, 36 pages
- **Abstract**: Residual policy adaptation is a lightweight way to modify a strong reference policy, but a shared scale and a fixed subgroup partition can hide heterogeneous degradation and become fragile when the deployment mixture of information states changes. RSD-Poker freezes a bank of residual families and scales, learns a **policy-visible partition on an independent structure split**, and freezes that partition *before* calibration labels are joined. Each candidate-group pair gets a weighted simultaneous upper certificate for anchor-relative risk and a lower certificate for weak-response utility. A robust group-to-candidate map is selected over a predeclared uncertainty set of deployment group proportions.
- **Key innovations**: (1) the **learned-then-frozen partition ordering** — partition is fit on a structure split, then frozen before calibration labels are seen, which is what makes the certificates valid at all; (2) declaration of the deployment-mixture uncertainty set *in advance* rather than fitting to observed proportions; (3) supports both teacher-backed and **teacher-free observation-only** students.
- **Results**: under stated independence/invariance conditions, the selected map satisfies its declared mixture-robust risk budget and utility certificate with probability ≥ 1−ζ_risk−ζ_util. Deterministic 24-state audit: empirical-zero selects α=0.08, raising weak-response proxy 4.2082 → 4.2889 with 0/12 held-out threshold crossings. On stratified held-out states the learned-partition dual selector lifts weak utility 4.4074 → 4.4936 and cuts held-out violation 0.0215 → 0.0078; the mixture-robust variant reaches violation 0.0059. Across five observation-only checkpoints, risk-calibrated residuals reach weak utility 4.3659±0.0177, violation 0.0178±0.0057.
- **Assessment**: ⚠️ **This is a certification paper, not a performance paper, and the numbers are weak-response proxies on a 24-state audit, not poker win rates.** The "Poker" in the title is the motivating domain, not the contribution. The genuinely reusable idea is the frozen-partition protocol.
- **Link**: https://arxiv.org/abs/2609.33669

### Dynamic Resource Allocation for Ensemble Determinization MCTS
- **Authors**: Jakub Kowalski, Adam Ciężkowski, Artur Krzyżyński, Mark H. M. Winands
- **Affiliation**: University of Wrocław (Poland) / **Maastricht University** (Netherlands) *(verified from arXiv HTML)*
- **Venue**: arXiv:2607.13007 (14 Jul 2026) — cs.AI
- **Abstract**: Simulation-based algorithms suit high-uncertainty domains such as adversarial board games with substantial randomness and hidden information. Proposes two axes of dynamic resource allocation for Ensemble Determinization MCTS: **Dynamic Number of Determinizations** (raise/lower the count of live determinization trees based on so-far search behavior) and **Dynamic Simulation Allocation** (split the simulation budget non-uniformly across trees using simulation-to-simulation decisions targeting the tree with the best potential knowledge gain).
- **Results**: benchmarked on three tabletop games — **Jaipur, Lost Cities, Splendor**. Particular configurations yield statistically significant strength increases in both iteration- and time-based settings.
- **Assessment**: quiet, competent, orthodox work — the kind of paper that makes a search engine stronger without changing the paradigm. COST Action CA22137 (ROAR-NET) funded.
- **Link**: https://arxiv.org/abs/2607.13007

### Searching for Primes: A Neural AlphaZero Approach to a Factoring Game
- **Authors**: Marcel Crasmaru
- **Affiliation**: not listed *(single author preprint)*
- **Venue**: arXiv:2609.22968 (19 Sep 2026) — math.OC / cs.CR
- **Abstract**: A one-player token game on an N×N board where tokens slide along diagonals or duplicate onto neighbors to form a combinatorial R×S rectangle. A conserved integer weight W′ and a strict monovariant guarantee O(N²)-length solutions, placing the game in NP. Proves that reaching a final position **factors this 2N-bit W′ into two N-bit factors** encoding the rectangle's rows and columns — so solving for a balanced-semiprime target is **equivalent to integer factoring**. If the target rectangle is known, however, the solution reduces to two polynomial-time steps. The game's difficulty is isolated to the initial number-theoretic split. Supplying popcounts of the factors as a promise preserves asymptotic hardness but bounds the search space; the authors exploit this with a learned policy/value network and AlphaZero-style MCTS.
- **Assessment**: ⭐ **unusual and worth a read** — an engineered game whose solution is *provably* integer factorization, then attacked with AlphaZero. The honest framing is in the abstract itself: "empirically probing the limits of neural look-ahead on a factoring-equivalent environment." The hardness isolation is the real result; the MCTS is the illustration.
- **Link**: https://arxiv.org/abs/2609.22968

---

## §2 Game AI Bot — LLM Agents, Single-Player, and Self-Improvement

### ★★ GameBoyWorlds: A Testbed for Self-Improvement in Embodied Video Games
- **Authors**: Dhananjay Ashok, Adam Shen, Aslan Huo Feng, Chinmay Khanna, Jun Rui Huang, Raghav Sarmukaddam, Surendira Balaji Natarajan, Xiaotong Cui, Xincan Zhang, Thomson Yen, Hongseok Namkoong, Jonathan May, Jesse Thomason
- **Affiliation**: **USC Information Sciences Institute** (×5) / Columbia / UChicago / Purdue / **Georgia Tech** *(verified from arXiv HTML)*
- **Venue**: arXiv:2609.32093 (25 Sep 2026) — cs.AI
- **Abstract**: Expert guidance lets agents operate in interactive environments, but whether they can **learn autonomously from their own experience** is unclear. GameBoyWorlds-Execution evaluates task execution across 5 distinct game series. Agents get dedicated *training* games but **no demonstrations, no documentation, no rewards** — they must ground themselves through self-directed exploration and infer actionable knowledge from their own experience. At test time they complete short-horizon tasks in *unseen* games. GameBoyWorlds-Playthrough tests end-to-end completion in two fan-made **Pokémon** games.
- **Results**: out-of-the-box frontier models complete **fewer than 50% of the 500 tasks**, due to failures in multimodal grounding. The authors demonstrate contemporary self-improvement approaches are **lacking**: world modelling and autonomous skill discovery both **fail**, and a novel curiosity-based-exploration strategy that writes guides achieves only partial success. On Playthrough, despite frontier models having been pre-exposed to official releases like Pokémon Red, they lack essential information about the testbed games — and a sophisticated agentic pipeline with **multimodal memory and hierarchical subgoals fails to reach even the first major milestone in both games**.
- **Assessment**: ⭐ **the strongest negative result in the digest.** Three things make it unusually valuable. (a) It is a *targeted* attack on the claim that embodied game agents self-improve, and the answer is a clean no across three method families. (b) The **Pokémon pre-exposure control** is a genuinely good experimental design — it separates "knows the game" from "can act in *this* game," which almost all game-agent work conflates. (c) The headline "hierarchical subgoals + multimodal memory fails at the *first milestone*" is exactly the number that should discipline the current wave of game-agent demos. **This is a benchmark to watch, and the negative results are the point.**
- **Link**: https://arxiv.org/abs/2609.32093

### ★★ GlyphBench: A Playground for Language-Model Reinforcement Learning
- **Authors**: Roger Creus Castanyer, Marc-Alexandre Côté, Matthew James Sargent, Augustine N. Mavor-Parker, Glen Berseth, Pablo Samuel Castro
- **Affiliation**: **Mila – Quebec AI Institute / Université de Montréal / Vmax** *(verified from arXiv HTML + author CV)*
- **Venue**: arXiv:2609.34214 (28 Sep 2026) — cs.AI
- **Abstract**: An environment suite for RL post-training of language-model agents, with **360+ tasks spanning diverse games**. GlyphBench renders spatial observations as **two-dimensional Unicode grids** and connects training, evaluation, and trajectory replay through a unified interface. The suite spans **nine game families** — puzzles, arcade games, and established RL benchmarks (Atari, Agentick, classics incl. Connect Four, Sokoban, Craftax, BALROG) — through a common text interface. Used to study how observation interfaces, reasoning effort, and agent harnesses affect performance, and how RL configurations shape learning dynamics.
- **Key innovations**: (1) the **glyph observation interface** — 2D Unicode grids preserve relative object positions in a form LMs consume directly *and* researchers can inspect, sidestepping both pixels and free text; (2) a *unified* interface covering training + eval + trajectory replay, so benchmark, research instrument, and post-training suite are one artifact; (3) built on **Prime-RL (Prime Intellect)** for RL.
- **Results**: glyph observations **outperform native text and pixels** in the Craftax experiments, with further gains on several BALROG environments. RL on 100 GlyphBench tasks improves **Qwen3.5-4B** on held-out **Reasoning Gym** problems to **63.48%**, beating the base model (56.04%), a math-trained baseline (62.29%), and a code-trained baseline (58.98%). Paired 95% CI on the gain over Math RL: [0.38, 2.02].
- **Assessment**: ⭐ **the "gameplay RL transfers better than math or code RL" claim is the finding that matters, and the authors are appropriately careful about it** — +1.19pp over Math RL with a CI that barely clears zero. The mechanism claim (glyphs > text > pixels for spatial reasoning) is the more robust contribution and the more reusable one. The wiki has previously logged the same cohort's [[PopuLoRA]] and the Agentick benchmark, so this is a continuation, not a one-off. Released: `huggingface.co/roger-creus-vmax/glyphbench-assets`
- **Link**: https://arxiv.org/abs/2609.34214

### ★ Porimon: An LLM-Based Pokémon Battle Agent with Long/Short-Term Knowledge Augmented Generation
- **Authors**: Dongyin Zhuo, Fengjunjie Pan, Nenad Petrovic, Alois Knoll
- **Affiliation**: **Technical University of Munich**, Robotics, AI and Real-Time Systems / CIT School *(verified from arXiv HTML)*
- **Venue**: arXiv:2609.32544 (26 Sep 2026) — cs.AI, **accepted at FLLM 2026**
- **Abstract**: Uses Pokémon Battles to study how to improve LLM agents on tasks requiring **opponent-aware planning** without additional fine-tuning. Proposes **Long/Short-Term Knowledge Augmented Generation (LSTKAG)**, letting the agent leverage past states of the current task and retrieve experience summaries from similar previous task instances conditioned on current state. Adds an external API for precise damage calculation and finer game information.
- **Results**: tournament-style evaluation of **15,000 battles** for hyperparameter optimization, ablations, and performance. Optimized Porimon significantly outperforms **PokéLLMon** (a prior LLM agent structure) and a rule-based heuristic player. Ablation shows Porimon variants beat the version without extended game-information retrieval, confirming that extension's contribution.
- **Assessment**: ⚠️ **The authors report their own Long-Term KAG contribution as inconclusive** — that candor is worth more than the headline. The honest reading is that short-term state tracking + an external damage-calculation API carries the result, i.e. most of the gain may come from tooling rather than the memory mechanism. 15,000 battles is a solid evaluation scale for this domain.
- **Link**: https://arxiv.org/abs/2609.32544

### OptiArena: Can LLMs Improve Executable Algorithms under Fixed Resource Budgets?
- **Authors**: Wenjun Peng, Xinyu Wang
- **Affiliation**: not listed *(arXiv has no HTML render for this ID; author affiliations unverified)*
- **Venue**: arXiv:2609.32227 (26 Sep 2026) — cs.CL, **accepted at EMNLP 2026 (Findings)**
- **Abstract**: A budget-controlled testbed for whether LLMs can improve **executable game-playing algorithms** through five rounds of code edits, within a fixed minimal scaffold, bounded evaluator feedback, and fixed resource budgets. Two optimization regimes, surface-obfuscation controls, calibrated references, held-out/stress splits, and diagnostics for degradation and exceptional failures. LLM API cost reported separately from local evaluator wall-clock.
- **Results**: across **twelve frontier LLMs and five games**, models improve designated weak starters more consistently than they refine editable competent baselines, with substantial variation across games and models.
- **Assessment**: the weak-vs-competent asymmetry is the useful result, and it is a *negative* finding in effect — LLM code optimization is much better at climbing from bad than at improving something already good. The surface-obfuscation control is the methodological strong point: it tests whether gains are real or string-matching.
- **Link**: https://arxiv.org/abs/2609.32227

### In-game Toxic Detection: Bi-directional Representations with Attention Residuals
- **Authors**: Yuanzhe Jia
- **Affiliation**: not listed
- **Venue**: arXiv:2609.34584 (28 Sep 2026) — cs.CL, comment says "**Accepted by AAAI 2023**"
- **Abstract**: In-game toxic language is a critical concern for the gaming industry. Detecting toxicity in player chat is hard because utterances are extremely short and rely heavily on game slang, abbreviations, and domain-specific jargon that generic LMs poorly recognize. Presents a shared task for in-game toxic language detection on real-world in-game chat data, and proposes **Bi-directional Representations with Attention Residuals (BRAR)**, reported as the best-performing model for the toxic-language slot-filling formulation.
- **Assessment**: ⚠️ **Metadata red flag, stated rather than hidden.** The arXiv comment claims AAAI 2023 acceptance — 3 years before this listing, and no venue confirmation was found. Treat as an unverified claim. The single-author, 2023-vintage framing suggests this is a re-upload rather than new work. The *problem* is live and industrially relevant; this specific paper should not be cited as current state of the art.
- **Link**: https://arxiv.org/abs/2609.34584

---

## §3 Game Agents Benchmarking & Evaluation

### ★★ SWE-Game: Can Coding Agents Build the Games We Want?
- **Authors**: Xiaoyu Chen, Lai Wei, Jin Wang, Xiangyu Zou, Ruochen Fan, Enze Luo, Mingzhe Yao, Jiahui Zhu, Yuhua Wen, Linghe Kong, Weiran Huang
- **Affiliation**: **Shanghai Jiao Tong University** / Zhongguancun Academy / Shanghai Innovation Institute / Shenzhen University / BUPT / **Elbetech Technology** *(verified from arXiv HTML)*
- **Venue**: arXiv:2609.33678 (27 Sep 2026) — cs.AI
- **Abstract**: A benchmark of **247 tasks grounded in 41 executable reference Godot games** spanning 13 gameplay categories in 2D and 3D. **Five task types**: development from a brief, implementation from a game design document, skeleton completion, **repair of 83 injected-fault cases**, and **Godot-to-Unity porting**. A shared instrumentation interface lets evaluator-owned drivers and probes execute actions and observe independently implemented games. Evaluation combines engine-state checks, certified reference-input replay, and agent-authored feature demonstrations to assess mechanic correctness, demonstrated playability, and behavioral restoration/preservation after repair. Game-specific vision-language rubrics separately assess presentation.
- **Key innovations**: (1) **the instrumentation interface is the contribution** — evaluator-owned drivers can execute and observe *independently implemented* games, which is what makes cross-model comparison possible at all; (2) **injected-fault repair with behavioral preservation** is a task type game benchmarks have not had; (3) the **Godot→Unity porting** task tests whether agents understand engine semantics rather than one engine's API.
- **Results**: across six models, **Opus5 achieves the highest overall score in all five task types**. Best overall scores remain **below 60/100** across the three construction tasks, with Brief-to-Game at **50.38**. On 100 agent-built games with human-labeled behaviors, executable checks achieve **92.59% balanced accuracy vs 78.41% for a video-based VLM judge**. Rubric-based visual scores reach **Spearman ρ = 0.829** with human ratings of 200 gameplay clips.
- **Assessment**: ⭐ **the 92.59% vs 78.41% comparison is the single most useful number in the digest.** It is direct evidence that *executing* an agent-built game beats *watching* one, and by a 14-point margin on a task where both are the intended measurement. Every game-agent evaluation built on video/VLM judging is carrying a ~14-point handicap. The sub-60 ceiling is the other headline: **no current model can build a working game from a design document.** Note the wiki already logged a Unity toolkit paper (2609.27585) in a prior sweep; this is the Godot-side counterpart with far stronger verification.
- **Link**: https://arxiv.org/abs/2609.33678

### ★ AI-Generated Interactive Fiction for Educational Use
- **Authors**: Finn Rogosch, Andreas Schrader
- **Affiliation**: not listed *(tentative: University of Lübeck cohort — unverified)*
- **Venue**: arXiv:2608.10818 (11 Aug 2026) — cs.HC / cs.CY, **EDULEARN26 Proceedings, Article 1075**
- **Abstract**: Generative AI can produce educational content at scale, but technical generation alone is insufficient — confusing, narratively inconsistent, or unengaging scenarios will not be useful. Pilot user-centred evaluation of AI-generated interactive fiction for higher education using a domain-agnostic pipeline and shared STEM content base. N=22 STEM participants played one generated episode and rated narrative clarity, story-content coherence, engagement, and length acceptance.
- **Results**: narrative clarity and length acceptance rated positively; **engagement sat near the neutral midpoint**; **story-content coherence was the weakest dimension by a clear margin**. Qualitative feedback identifies **quiz integration as the bottleneck** — artificial in-fiction motivation for quiz prompts, abrupt setting changes, missing story-level consequences for wrong answers.
- **Assessment**: a small N=22 pilot, so treat as directional. But it is a rare honest *user-side* measurement of LLM game content, and the finding is specific and actionable: coherence across the generated narrative and the embedded quiz logic is where LLM-generated interactive content breaks, and it breaks in a way users notice even when they rate other dimensions fine. This is the [[Player-as-evaluator]] register noted in the 09-29 digest, now with a mechanism.
- **Link**: https://arxiv.org/abs/2608.10818

### Riftbound is Turing Complete
- **Authors**: Nathan Dalaklis, Beckett Fields
- **Affiliation**: not listed
- **Venue**: arXiv:2609.33839 (27 Sep 2026) — cs.CC, 17 pages
- **Abstract**: **Riftbound: League of Legends Trading Card Game** — a TCG about capturing and holding locations in a king-of-the-hill contest, released in China Aug 2025 and US Oct 2025. The authors demonstrate a facet of its complexity by providing sequences of valid game states that **construct Universal Turing machines within the game**, using tournament-legal decks at time of writing, with strategies directed by game state. Shows that given an appropriate board state, the machine may be constructed and the computation performed **in one game turn**.
- **Assessment**: ⭐ a genuinely charming and rigorous result. Same intellectual move as the factoring game in §1 — take a commercial game, prove it is computationally universal, and thereby establish that the game contains deep structure. The one-turn construction claim is the strong version. No affiliation listed; treat as independent work.
- **Link**: https://arxiv.org/abs/2609.33839

---

## §4 Causal & Structural Approaches to Game AI

### ★ Compiling VGDL into Causal Models
- **Authors**: Mohit Jiwatode, Bodo Rosenhahn, Alexander Dockhorn
- **Affiliation**: not listed in header *(tentative: University of Birmingham / CMU, inferred from Rosenhahn & Dockhorn cohort — unverified)*
- **Venue**: arXiv:2609.05459 (10 Aug 2026) — cs.AI, **to be published at IEEE Conference on Games 2026**
- **Abstract**: RL agents and LLMs both fail to capture the causal mechanics of game environments — standard RL agents rely on spurious correlations, LLMs hallucinate game rules. Despite causal RL improving interpretability, no formal methodology maps complex game mechanics into causal models. Proposes a **deterministic framework that compiles games specified in the Video Game Description Language (VGDL) into Dynamic Structural Causal Models**. Rather than inferring causal structure from gameplay traces or noisy LLM output, the methodology directly translates game components — sprite dynamics, interaction rules, termination conditions — into **explicit structural equations**. Each game tick is a causal transition from state variables at t to t+1.
- **Key innovations**: (1) the compile direction is **symbolic spec → causal model**, inverting the usual trace-inference direction, which is what buys the fidelity guarantee; (2) the fidelity claim is *absolute by construction* rather than learned — ground truth in, exact structure out; (3) the resulting model supports counterfactual reasoning, causal-RL agent training, and procedural content validation.
- **Assessment**: the strongest thing here is the inversion. Every other causal-game paper infers structure from data and inherits the data's errors; compiling from VGDL removes that error class entirely. The catch is equally clear: **it only works where a machine-readable game spec exists.** For the LLM-authored 3D games that are the field's current frontier, there is no VGDL — the method does not reach them. IEEE CoG acceptance is a real venue signal for game-AI methodology. Directly relevant to the [[Procedural Content Generation]] line the wiki has tracked since June.
- **Link**: https://arxiv.org/abs/2609.05459

---

## §5 Player Experience, Deployed Game AI, and Human Factors

### ★★ Runtime Action Interference for AI Control of AlphaStar in StarCraft II
- **Authors**: Jaymari Chua, Chen Wang, Liming Zhu, Lina Yao
- **Affiliation**: **University of New South Wales (Sydney) / CSIRO** *(verified from arXiv HTML institute block)*
- **Venue**: arXiv:2608.21398 (5 Aug 2026) — cs.LG / cs.AI / cs.CY
- **Abstract**: **A trained RL policy does not determine the behavior users actually encounter** — deployment code still schedules, admits, suppresses, or replaces its proposed actions. Introduces **Runtime Action Interference (RAI)**, a control mechanism that preserves policy parameters while regulating action pacing and filtering configured action patterns *after inference*. RAI releases a proposed action only when its cooldown is satisfied and its content detector does not flag it; otherwise it dispatches a no-op. The detector covers specified toxic behaviors including **worker-unit harassment**; the cooldown controls action rate. Implemented in a replication of AlphaStar's `actor.py`, with open-source reproducibility materials.
- **Results**: deployed RAI in a **StarCraft II human participant study** comparing two presentations of the same opponent — high capability with rate-limited actions, with the **capability claim withheld in one presentation and disclosed in the other**. On 1–5 response scales: claim-withheld → fairness 3.90, trust 3.50, toxicity 2.00; disclosed → fairness 2.62, trust 4.31, toxicity 2.85. Disclosure corresponded with **lower perceived fairness and higher perceived toxicity across every expertise group**, while **trust rose among novices and experts but fell among intermediate participants**.
- **Assessment**: ⭐⭐ **the most important paper in the digest for anyone shipping game AI, and the reason is the experimental design rather than the mechanism.** The control mechanism is unremarkable — cooldown plus content filter is a thin layer. What is remarkable is that they held the *configured control constant* and varied only whether the player was told the bot was good. Result: **the same bot with the same code was rated less fair and more toxic purely because players knew it was strong.** Lina Yao's group, and this is a serious result — it says human-evaluation of game AI is measuring the *disclosure*, not the *behavior*, unless the two are separated. Their own conclusion states it: human-computer evaluation "must separate control within the execution stack from capability disclosure and assess fairness, trust, and toxicity as distinct dimensions." **Every game-AI paper in this wiki that reports player-experience metrics should be re-read for whether it controlled for disclosure.** That is a real, transferable methodological demand, and it is corroborated from an independent direction by the 2608.14016 commentary system in §5 below.
- **Link**: https://arxiv.org/abs/2608.21398

### Content Based Video Narration of Gameplay with Vision Language Models
- **Authors**: Mathew Varghese
- **Affiliation**: not listed *(single author, independent)*
- **Venue**: arXiv:2608.14016 (14 Aug 2026) — cs.CV / cs.AI / cs.GR
- **Abstract**: Live game commentary is scarce — it exists for professional esports broadcasts and almost nowhere else. Presents a content-based video narration system producing spoken esports-style commentary for arbitrary gameplay recordings using a general-purpose VLM plus text-to-speech, with **no game-specific instrumentation, no engine telemetry, no task-specific training**. Three mechanisms: **temporal mosaic packing** (nine uniformly sampled frames into a single 3×3 image, letting an image-native VLM reason about motion while consuming one image payload per segment instead of nine); **context-conditioned prompting** (replays the K most recent narrations as assistant-role history, suppressing the repetition that dominates per-segment captioning of static scenes); **duration-conditioned generation and elastic alignment** (constrain narration length in the prompt, then time-scale or symmetrically pad synthesized audio so each utterance fills its segment slot exactly, giving frame-accurate muxing without a forced aligner).
- **Results**: supports cloud TTS or a **6-bit quantized 4B-parameter on-device TTS model on Apple silicon**, making the speech stage fully local. Qualitative case study on RTS footage; cost model showing mosaic reduces per-minute image payloads by **9×**. Candid failure-mode account: **hallucinated game state, resolution loss from mosaicking, prosody artifacts from time-scaling.** Released as a reproducible baseline with an evaluation protocol; quantitative study deferred to a full version.
- **Assessment**: the 9× payload reduction from mosaic packing is a clean, immediately reusable systems trick, and the "candid account of observed failure modes" is rare and valuable. **Hallucinated game state** is the failure that matters for anything downstream: a VLM commentator that invents game state is the same failure mode that [[SWE-Game]] measured at 78.41% for video-based VLM judging. Two independent papers, same weakness, same root cause — judging games from pixels without executing them.
- **Link**: https://arxiv.org/abs/2608.14016

### Capture the Narrative: Social Media Manipulation Wargaming for Cyberliteracy
- **Authors**: Alexandra Vassar, Rahat Masood, Hammond Pearce
- **Affiliation**: not listed *(tentative: Australian university consortium, per "18 Australian universities")*
- **Venue**: arXiv:2607.23993 (27 Jul 2026) — cs.CY, under review
- **Abstract**: Misinformation is deeply embedded in online discourse, with nearly **one in five posts during global events generated by bots**. GenAI has further lowered the barrier, yet most digital-literacy education still relies on static checklists and single-player inoculation games built for an earlier media landscape. Describes **Capture the Narrative**, a four-week multi-university competition where student teams build **LLM-powered bots to influence a simulated election**. Reports on a custom social-media platform, the competition environment, and the design of its **4,000 AI-driven NPC citizens**, and what running it at scale actually involved.
- **Results**: first iteration — **108 teams from 18 Australian universities produced 7,068,206 player-bot posts, ~60% of all platform content**. Surveyed 256 students before and 83 after. **Students did not become more confident at spotting bots, contrary to what inoculation theory predicts.** Because engagement was rewarded, most teams prioritised **high-volume posting over nuanced influence**, mirroring real-world platform dynamics.
- **Assessment**: a scale milestone (7M bot posts, 4,000 NPC citizens) and a genuine theory-refuting result on the education side. The mechanism of failure is the transferable part: **rewarding engagement made agents spam**, which is a real-time game-AI lesson — reward design shapes the *strategy space* of the agents you are training, and the emergent strategy will be the one your reward permits, not the one you want. Directly parallels the GT7 reward-design and MARL incentive-design lines the wiki has logged. Also one of the larger NPC-population deployments in the literature.
- **Link**: https://arxiv.org/abs/2607.23993

### Hypergamification Through Integrating Game Engines and Learning Management Systems
- **Authors**: Araz Yusubov, Michael Bechtel, Tangiz Alizada
- **Affiliation**: not listed
- **Venue**: arXiv:2607.29300 (31 Jul 2026) — cs.CY
- **Abstract**: Discusses games, their use in education, and prior work integrating game engines with learning management systems. Proposes a **bidirectional** integration where game environments are generated *from* LMS content, introducing **hypergamification** as the use of a comprehensive game environment rather than isolated game-design elements. Working pilot: an importable **Unity package for Blackboard integration**, plus a demo game.
- **Assessment**: modest pilot scale, but the bidirectional direction is the interesting part — prior work drives the game from the LMS; driving the *game structure* from the course content is a step toward automated game design, which is the PCG-adjacent content the task asked about. The Unity/Blackboard tooling is a concrete deliverable.
- **Link**: https://arxiv.org/abs/2607.29300

---

## §6 Procedural Content Generation — Documented Vacancy

**No new unclaimed PCG papers were found in this run, and this is reported as a vacancy rather than padded with adjacent work.**

Method: three dedicated PCG query rounds — `procedural content generation` × RL (37 hits), `abs:"level generation"` (200, page-capped), `procedural generation` × game (100), `PCG` × level (83), `game content generation` (12), `LLM` × level design × game (1), `VLM` × level generation (0), `wave function collapse` × learning (9), `dungeon generation` × neural (0), `level generator` × RL/diffusion (102). Pool → 75 unclaimed papers since 2026-06 → **all 75 are false positives** (software engineering "code generation", CV "scene generation", grid topology in power networks, image generative modeling, clinical text generation).

**Reason: this is a genuine backlog already harvested.** The 09-29 retrospective sweep ran a dedicated PCG sweep over a 12-month horizon (`level generation`, `procedural content generation`, `dungeon generation`, `wave function collapse`, `game generation` × `neural`, `cs.DS` × `game` × `generation`) and claimed 113 PCG-adjacent papers from 2025-09 onward. That harvest is the authoritative PCG coverage for the wiki, and nothing new has arrived above it since. The nearest genuinely new PCG-adjacent item this run is **2609.05459 (§4)**, whose "procedural content validation" application is PCG-adjacent but whose contribution is causal compilation.

> ⚠️ **Standing note for the next run:** the two page-capped queries (`abs:"level generation"` at 200 and `PCG` × level at 83, `level generator` at 102) mean the PCG pool is **not exhaustively searched** — the caps truncate by recency, not by relevance. A `max_results=1000` pass on `abs:"level generation"` would be needed before asserting PCG is genuinely empty.

---

## §7 Related Techniques

### Cross-Rollout Bellman Closure for Long-Horizon Agentic RL
- **Authors**: Yangyang Ren, Haodong Zhu, Linlin Yang, Sheng Xu, Peichao Lai, Baochang Zhang
- **Affiliation**: not listed
- **Venue**: arXiv:2609.35082 (28 Sep 2026) — cs.LG
- **Abstract**: Group-based RL such as GRPO trains LLM agents by comparing rollouts per task without a learned critic. In long-horizon settings rollouts **revisit shared anchor states**, offering cross-rollout evidence for step-level credit. Visit-local averaging pools realized suffix returns at shared anchors and respects observed frequencies, but does not recursively propagate evidence across rollouts; shortest-path estimators have global reach but let a rarely-observed route dominate an anchor's value. CRBC merges each rollout group into a finite empirical process with absorbing success/failure boundaries and evaluates its behavior-policy **Bellman fixed point with one linear solve**, propagating evidence through shared anchors while aggregating alternative continuations by empirical frequency. Backing up the resulting state values through observed transitions yields action values, whose gain over the corresponding state value provides step-level credit. A finite-depth family recovers visit-local return averaging at zero depth and converges to the exact closure as depth increases.
- **Results**: across **ALFWorld, WebShop, and Sokoban** at multiple model scales, CRBC consistently improves final performance and learning efficiency — e.g. **+5.59pp on ALFWorld with Qwen2.5-1.5B-Instruct** over the strongest evaluated baseline.
- **Assessment**: ⭐ **ship it together with GraphHCA (§1) — they share four authors and are the same diagnosis.** Both observe that group-based RL discards cross-rollout structure that group-based rollouts actually contain. CRBC's "one linear solve for a fixed point" and GraphHCA's "discounted recursion with a unique fixed point on any directed graph" are the same mathematical object reached from two directions. Read together, they are a credible two-paper argument that **step-level credit assignment in agentic RL is not yet solved and there is structure being left on the table.** Neither needs an extra rollout or a learned critic, which is what makes them deployable.
- **Link**: https://arxiv.org/abs/2609.35082

### HyperMCTS: Hypergraph-Augmented MCTS for Long-Horizon LLM Agents
- **Authors**: Tingsong Xiao, Nithish Balachandar Moudhgalya, Chandrayee Basu, Lichao Wang, Luyang Kong, Benjamin Z. Yao, Zhe Jiang, Jie Hao
- **Affiliation**: not listed *(tentative: UNC / Georgia Tech cohort — unverified)*
- **Venue**: arXiv:2609.33920 (27 Sep 2026) — cs.AI
- **Abstract**: MCTS offers test-time scaling by exploring alternative action trajectories, but model computation and environment interaction make search costly, so efficient search requires reuse of trajectory feedback. Standard MCTS keeps prefix-specific statistics and never accumulates outcomes for **decision groups that recur across different paths**. HyperMCTS is a training-free method that augments an ordered MCTS tree with a **cross-trajectory hypergraph**: hyperedges represent groups of canonical decisions and accumulate observed returns within the current task. The HyperUCT selection rule aggregates evidence from overlapping hyperedges into an action prior, letting outcomes collected under one prefix inform selection under another while preserving execution histories in the tree.
- **Results**: on **DeepPlanning**, +2.3–7.3pp average planning accuracy over the strongest baseline for each of three backbone models. Enables **Qwen3.6-27B to outperform Claude Opus 4.6 (max) on Shopping Planning**, at higher accuracy with fewer LLM calls and output tokens than the evaluated MCTS baselines.
- **Assessment**: **structurally the same idea as CRBC** — reuse cross-trajectory evidence instead of keeping statistics scoped to one prefix — but transplanted into tree search rather than RL credit assignment. The Qwen3.6-27B-beats-Claude-Opus-4.6 result is a claim worth watching and is exactly the kind of result that should be read as *search-compute-equivalent*, not as a model-capability ranking, unless the call budgets are matched. Three independent papers in one window converge on "the trajectory is under-exploited," which is the strongest cross-cutting signal in this digest.
- **Link**: https://arxiv.org/abs/2609.33920

### What Does a ProcGen Generalization Gap Measure? Action Rules, Convergence, and the Missing Random Floor
- **Authors**: Abhisek Keshari
- **Affiliation**: **Independent researcher** *(self-stated, verified in arXiv HTML)*
- **Venue**: arXiv:2609.32532 (26 Sep 2026) — cs.LG
- **Abstract**: A generalization gap in RL (return on training levels minus return on held-out levels) is usually reported **without a reference point**. Argues the missing reference is a measured **random floor**: the return of a uniform-random policy on the same levels under the same harness. On ProcGen the floor changes what several standard numbers mean. Across eight environments on identical checkpoints and levels, switching between sampled and greedy (argmax) test-time actions moves held-out return **in both directions**, and greedy evaluation takes three environments to or below the floor — in **miner**, the sampled policy scores **4.9× the floor** on held-out levels while its argmax scores **below it**. Raw policy entropy places seven of eight environments short of convergence, but **35–65% of that entropy is spread across actions with identical effects**; after merging them, one to three remain short, and against the floor only **heist** has learned nothing that transfers.
- **Results (methodological)**: an audit of **twelve prior ProcGen codebases** finds that **all eleven with held-out evaluation sample test-time actions for their policy-gradient agents — nine by default rather than by explicit choice — and six report running in-loop averages rather than evaluating a fixed checkpoint**. Applied to the authors' own case study, the same checks **grade down a statistically significant encoder effect** and rule out a within-encoder train-vs-test confound.
- **Assessment**: ⭐⭐ **the most useful methodological paper in the digest, and the only one that audits other people's published numbers.** Three specific, actionable claims: (a) **generalization gaps need a random floor or they are uninterpretable**; (b) **sampled-vs-greedy test-time action is a silent, uncontrolled variable that 9/11 codebases changed by default** — a practice difference masquerading as a result; (c) **35–65% of policy entropy is spent on actions with identical effects**, so raw entropy is a bad convergence diagnostic. The authors then apply their own checks to their own result and *retract its significance* — that is the behavior that makes the rest of the critique credible. This should be read as a protocol change for the whole ProcGen/Atari literature, not as a disagreement with one paper.
- **Link**: https://arxiv.org/abs/2609.32532

### TopoExplore: Homology as an Exploration Signal
- **Authors**: Jason Carlson
- **Affiliation**: not listed *(single author preprint)*
- **Venue**: arXiv:2607.09971 (10 Jul 2026) — cs.AI
- **Abstract**: Exploration signals in RL are computed from **what an agent has seen** — visitation counts, density estimates, or prediction error at individual states. None of these report **the holes in the visitation space**. TopoExplore computes the **persistent homology of the agent's own archive of visited states** and turns each detected class (an enclosed region the archive surrounds but has not entered) into a selection bonus concentrated on archived states from which entry is possible, gated by an attempt counter that retires candidate entrances and prunes sealed structures. The method is **Go-Explore plus one additive term**, so the comparison isolates that term.
- **Results**: on the 189 held-out worlds of the open-source **TopoGym** benchmark of topologically varied hard-exploration environments, TopoExplore finds the goal in **167 worlds vs 152 for Go-Explore**, and where both find it uses a **median 126k steps vs 186k**. On a stress environment with far-apart chambers creating archive holes, it enters **all six or eight chambers across 5 seeds vs 1 and 2 of 5 seeds** for Go-Explore. On **Montezuma's Revenge** (built over the room graph), the term helps whenever the archive surrounds an unentered room, placing **33–45% of selections on surrounding rooms** while active.
- **Assessment**: ⭐ the cleanest **hard-exploration** result available, and the "Go-Explore + one term" framing is exactly the right ablation discipline — it means every other number in Go-Explore's literature is directly comparable. The 167-vs-152 on TopoGym is a real but modest gain; the chamber experiment (6/8 vs 1/5) is where the method actually earns its name. Directly relevant to the open-ended-learning and curiosity lines the task asked about, and the persistent-homology framing is a genuine alternative to count-based bonuses.
- **Link**: https://arxiv.org/abs/2607.09971

### Adaptive Mixing of Policies from Searching and Policies from Learning
- **Authors**: Gavin B. Rens
- **Affiliation**: not listed *(single author preprint)*
- **Venue**: arXiv:2608.15700 (16 Aug 2026) — cs.AI, 23 pages
- **Abstract**: Distillation of training targets generated through search/planning has proven useful in RL, but search can take exceedingly long. Objective: rather than search to the same depth every time, reduce search depth **proportionally to the quality of the policy network's priors**. Describes **Flexer**, an architecture that for each step mixes the policy from a neural network with the policy from MCTS. The mixing factor favors the MCTS policy as **policy imitation error** of the network and the **environment model's variance** increase.
- **Results**: Flexer outperforms a version of AlphaZero (and DQN and ADP) for some experiments on **three toy symbolic problems**.
- **Assessment**: a small, honest paper with an under-explored idea — *adaptive* compute allocation between a prior and a search, gated on the prior's own error. This is the search-budget-allocation problem that nearly all self-play work treats as a fixed hyperparameter. ⚠️ Three toy symbolic problems is thin evidence; the framing is worth remembering when §1's [[Modular Discovery of General Game-Playing Algorithms]]-scale systems start tuning search budgets.
- **Link**: https://arxiv.org/abs/2608.15700

### Policy Representations in Two-Player Zero-Sum Imperfect-Information Games
- **Authors**: Kevin Wang, Kevin Yang, Arjun Prakash, Amy Greenwald
- **Affiliation**: **Brown University** *(verified from arXiv HTML)*
- **Venue**: arXiv:2607.01498 (1 Jul 2026) — cs.LG
- **Abstract**: Investigates learning useful policy representations (embeddings) in two-player zero-sum imperfect-information games. Three contributions: methods for creating policy datasets for a given game; methods for learning policy representations; downstream tasks to evaluate their effectiveness. Evaluated on **Kuhn and Leduc Poker**. The authors state their methods are "very basic" but demonstrate useful **behavioral representations are present in the learned embeddings**; claim to be among the first to systematically compare **self-supervised learning techniques for learning policy representations in games**.
- **Assessment**: a small but genuinely under-served direction — representation learning for policies as opposed to representations *of* states. "Self-play is the only source of game data" is implicit and worth stating explicitly, and the two games are the right size. The authors' own modesty claim is accurate and does not damage the contribution.
- **Link**: https://arxiv.org/abs/2607.01498

### Learning to Run Power Networks: AlphaZero-inspired Topological Control
- **Authors**: Lukas Zetto, Benjamin Schäfer, Qiong Huang
- **Affiliation**: not listed *(tentative: TU Dresden cohort — unverified)*
- **Venue**: arXiv:2608.14114 (14 Aug 2026) — cs.LG, **ACM SIGENERGY Energy Informatics Review 6(3), Sept 2026**
- **Abstract**: Rising renewable penetration strains grids; RL for autonomous **topological reconfiguration** is promising, but combinatorial action space and strict operational constraints hinder it. Evaluates model-based AlphaZero-inspired approaches using MCTS for proactive grid management, systematically varying reward functions, observation density, and search guidance.
- **Results**: optimized AlphaZero reaches **98.43% peak survivability**, significantly outperforming the PPO variant. Two findings worth carrying over: **MCTS without guidance from a prior learned policy or value function enhances training efficiency**, and a **straightforward binary survival reward outperforms complex multi-objective functions**.
- **Assessment**: not a game paper, but included because it is one of the few clean studies of *AlphaZero design choices* on a hard combinatorial control problem, and both findings transfer. The "no prior guidance is better" result is a direct challenge to the standard AlphaZero recipe and should be read alongside §1's LLM-discovered-search-mechanisms paper. The authors' own summary is the takeaway: pure RL is insufficient; an effective system needs minimalist integration of domain heuristics, binary rewards, and a restricted observation space.
- **Link**: https://arxiv.org/abs/2608.14114

### Game-Theoretic Inverse Reinforcement Learning for Competitive Human Driving
- **Authors**: Yu Song
- **Affiliation**: not listed *(single author preprint)*
- **Venue**: arXiv:2608.06445 (6 Aug 2026) — physics.soc-ph
- **Abstract**: Capturing strategic decision-making in competitive human driving matters for AV safety and traffic simulation. Compares data-driven **game-theoretic IRL** models against an established physics-based game-theoretic approach for predicting aggressive, safety-critical **cut-in** lane changes, using the highD dataset, with models of increasing feature complexity.
- **Results**: best IRL models exceed **75% overall prediction accuracy** with cut-in **precision up to 51% and recall up to 49%** — versus the physics-based benchmark's **4.4% precision** in these scenarios. Clear trade-off: granular instantaneous features maximize precision; temporal-consistency features maximize recall.
- **Assessment**: the 4.4% → 51% precision jump is dramatic, and the stated trade-off is more useful than the headline. Included under *related techniques* because competitive human driving is a genuine two-player game-theoretic environment and the physics-model-vs-learned-model comparison is a template for evaluating opponents in any partially-observed game. Precision 51% is far below deployment quality; the honest framing is comparative, not absolute.
- **Link**: https://arxiv.org/abs/2608.06445

---

## §8 Runner-ups (verified unclaimed, lighter entries)

| ID | Title | Date | Domain | Why it is here |
|---|---|---|---|---|
| 2609.33068 | Counting Reachable Positions in a Simplified Model of Connect Four | 27 Sep | math.GM | Eliminates Connect Four's win condition, extends the board to infinite height, derives polynomiality in move count, characterizes asymptotics, shows even-length positions form a monoid with symmetric finite generating set. **Published: J. Comb. Math. Comb. Comput. 131 (2026) 57-65.** Alistair Folster |
| 2607.06577 | Esports and Physiological Tremor: a StarCraft 2 Tournament Study | 2 Jul | q-bio.QM | Wrist accelerometer tremor in 16 StarCraft II players across two tournament days. Deviates from population norms in all bands (Cohen's d = 1.6–2.3), with tremor *declining* systematically over the tournament day — **the opposite of fatigue patterns in traditional motor tasks**. Neither outcome nor APM predicted post-game tremor. Suggests generalized psychophysiological adaptation, not a short-term performance predictor |
| 2608.29926 | Emergence of Strategic Equilibria from Transverse Field Ising Hamiltonian Dynamics | 30 Aug | quant-ph | Quantum game theory via transverse-field Ising; Hamiltonian dynamics generate entangling operators resolving game dilemmas, giving quantum advantage over classical outcomes. Unlike fixed-gate quantization, entanglement is **tunable by physical Hamiltonian parameters** — a hardware-relevant angle. Teena Thomas, S. Balakrishnan |
| 2608.25942 | Gaming Together on Discord: Teen Gamer's Cross-Platform Practices | 26 Aug | cs.HC | 16 semi-structured interviews; reflexive thematic analysis. Players use Discord to extend gameplay beyond the game, but fragmented governance between platforms creates a **"platform gap"** exposing players to risk. **Published: Proc. ACM Hum.-Comput. Interact. 10(7), Nov 2026, 32 pages.** Relevant as player-side infrastructure context |
| 2608.02635 | Wigner's Friend Paradox Revisited | 30 Jul | quant-ph | Quantum-games-adjacent foundations. Collected, not featured — no game application |
| 2609.34878 | Synthesizing Update Schedules with Game-Based Bounded Model Checking | 28 Sep | cs.GT | Two-player timed game between a system and its updater; bounded SMT encoding synthesizes fixed global-time update schedules guaranteeing safe deployment regardless of system behavior. Demonstrated on an autonomous-driving trajectory planner. **EPTCS 452, 2026, 19-34.** Timed-game methods, safety-critical application |

---

## §9 Cross-Cutting Observations

### 9.1 Three papers, one window, one discarded signal
GraphHCA (2609.35084), CRBC (2609.35082), and HyperMCTS (2609.33920) independently observe that **trajectory data is under-exploited**: GRPO compares rollouts but discards the cross-rollout state structure those rollouts contain; MCTS keeps prefix-local statistics and never accumulates outcomes for decision groups recurring across paths. GraphHCA and CRBC share **four authors** and are the same mathematical object (a fixed point on a transition graph) from two directions, while HyperMCTS reaches it independently inside tree search. The convergence of three groups on one diagnosis in one window is the strongest signal in this digest, and all three add step-level credit without extra rollouts or a learned critic.

### 9.2 Executing a game beats watching one — measured twice
[[SWE-Game]] (2609.33678) measures executable checks at **92.59% balanced accuracy vs 78.41%** for a video-based VLM judge. Independently, 2608.14016's VLM commentary system lists **"hallucinated game state"** as its primary failure mode. Same root cause, two unrelated groups: judging a game from pixels without executing it fails ~14 points. Every game-agent evaluation built on video or VLM judging carries this handicap, and most do not report it.

### 9.3 Player-experience measurement is confounded by disclosure, and one paper says so
[[RAI]] (2608.21398) held the *configured control constant* and varied only whether players were told the AlphaStar-derived opponent was high-capability. Same code, same rate limits — and yet fairness fell 3.90→2.62, toxicity rose 2.00→2.85, and trust moved in **opposite directions by expertise group**. The claim "human evaluations must separate control within the execution stack from capability disclosure" applies retroactively to every player-experience metric in this wiki. It is a demand for a control, not a claim about any specific result.

### 9.4 Reward design selects the strategy, and it is visible in agents you did not intend to reward
[[Capture the Narrative]] (2607.23993) rewarded engagement, and 108 student teams responded with **high-volume posting over nuanced influence** — 7.07M bot posts, ~60% of all platform content. The same mechanism operates in MARL incentive design and in the GT7 reward-design line the wiki has logged. Meanwhile the authors found students did **not** become better at spotting bots, contradicting inoculation theory. Both halves matter: the reward shaped the agents, and the educational premise did not survive.

### 9.5 A protocol change the whole ProcGen/Atari literature should adopt
[[2609.32532]] supplies a measured **random floor** for generalization gaps (uniform-random policy, same levels, same harness), documents that **sampled-vs-greedy test-time action is silently uncontrolled in 9 of 11 audited codebases**, and shows **35–65% of policy entropy is spent on actions with identical effects**, making raw entropy a poor convergence diagnostic. In miner, sampled action scores **4.9× the floor** while argmax scores *below* it. The author applies these checks to his own result and downgrades his own significance claim — which is what makes the critique credible rather than a complaint. Note the miner/miner discrepancy is a direct caution for the Atari numbers this wiki already holds.

### 9.6 A benchmark is not a model, and the gap is quantified
SWE-Game's best scores are **below 60/100** across all three construction tasks (Brief-to-Game: 50.38), with Opus5 leading all five task types. GameBoyWorlds' frontier models complete **fewer than 50% of 500 tasks** with no demos/docs/rewards, and a pipeline with multimodal memory plus hierarchical subgoals **fails to reach the first major milestone** in either Pokémon game. Against that, GlyphBench's Qwen3.5-4B reaches 63.48% on Reasoning Gym after gameplay RL, and DeepMind's LLM-discovered search mechanisms top-tier across **400+ environments**. **The gap is not "agents can't play games" — it is that agent capability is far more uneven across game *structure* than the headline numbers suggest**, with construct-the-artifact and self-improve-from-scratch both far behind the improve-a-working-scaffold case that OptiArena documents.

### 9.7 Two vacancies, both documented rather than padded
- **PCG (§6)**: nothing new above the 09-29 retrospective harvest. Reported as a vacancy with the query accounting, plus a standing note that two queries were page-capped and the pool is therefore not exhaustively searched.
- **Industry game AI (§ not present)**: 12 industry-targeted queries (`A/B test` × engagement, `game studio`, `commercial game`, `live service`, `publisher` × `game AI` × evaluation, `player retention` × ML, `Unreal Engine` × agent, `Unity` × RL × NPC, `game AI` × industry, `production` × `deployment`, `fun` × agent × evaluate, `human evaluation` × enjoyment) → 321 raw → **3 unclaimed candidates since 2026-07, all weak** (a sports-video CV paper, a WebXR/metaverse socio-technical analysis, a synthetic-video engine). **No game-studio-affiliated paper appears in this digest.** The only substantial industrial-deployment work found is [[RAI]] (2608.21398, UNSW/CSIRO) and it is a *research* deployment in a human-subject study, not a shipped game. The Wii-playing-robot AAAI-2026 Best Paper win recorded in the 09-29 conference digest remains the most notable industry-adjacent game-AI artifact in the wiki, and it was not re-claimed here.

---

## §10 Corpus Accounting and Caveats

- **Window (Part I)**: 3,678 papers, IDs 2609.31757–2609.35771, `published` 2026-09-25T18:00Z → 2026-09-28T17:58Z. 0 of 3,678 already claimed. 157 loose-token hits → 45 hard-gate hits → **6 genuine game papers** (§1–§3 items dated 25–28 Sep).
- **Topic sweep (Part II)**: 109 queries → 6,442 raw entries → 4,411 unique → 3,868 unclaimed → 2,386 hard-game-gate → `published >= 2026-08-01` for non-09-29-covered coverage → **21 featured** across §1–§7 and §8.
- **Totals**: **27 papers featured + 6 runner-ups = 33 papers claimed**, each verified at **0 arXiv-ID hits** in `wiki/` immediately before this file was written, and each re-checked for title-level duplication (`GlyphBench`, `SWE-Game`, `GameBoyWorlds`, `RSD-Poker`, `Porimon`, `OptiArena`, `HyperMCTS`, `TopoExplore`, `Riftbound`, `Ensemble Determinization` → 0 hits each; `AlphaStar` and `VGDL` return prior-mention hits only, all referring to earlier unrelated papers).
- **Dedup key**: arXiv ID, per the rule adopted on 09-29 after title word-order variants caused a 5-month miss. Wiki baseline for this run: **7,037 unique arXiv IDs** across `wiki/**/*.md` (regex `2[0-9]{3}\.[0-9]{4,5}`). ⚠️ The 09-29 run reported 6,966 under the same procedure; the difference is attributed to 27 IDs claimed by the 09-29 siblings plus the 09-29 retrospective sweep, and the glob scope is identical, so these two figures *are* comparable — unlike the 6,244/7,004 triple that the 09-29 digest declined to reconcile.
- **Affiliations**: verified from arXiv HTML author blocks for 2609.34342, 2609.33115, 2609.32093, 2609.32544, 2609.33678, 2608.21398, 2609.32532, 2607.13007, 2607.01498, 2609.34214 (also cross-checked against the first author's public CV). The arXiv **API returns no affiliations at all** — `arxiv:affiliation` is empty for all 3,678 window entries — so the API is unusable for this field and HTML scraping is required. 9 papers marked `tentative` are author-cohort inferences with **no page evidence**; treat as unverified. 2 papers have no affiliation listed anywhere (OptiArena has no HTML render; 2608.14016 and 2609.32532 are single-author independent preprints, the latter self-stated).
- **Single-source / no-replication**: all 33 are preprints or unrefereed items except where a venue is named (FLLM 2026, EMNLP 2026 Findings, IEEE CoG 2026, EDULEARN26, EPTCS 452, J. Comb. Math. Comb. Comput. 131, ACM SIGENERGY 6(3), PACM HCI 10(7)). **No result in this digest has been independently replicated.**
- **⚠️ Metadata flag**: 2609.34584 carries the comment "Accepted by AAAI 2023" on a 2026 listing with no verifiable venue record. Treated as an unverified claim, not as a AAAI publication.
- **Not re-claimed**: PCG coverage (§6) and industry game AI (§9.7) were searched with 10 and 12 dedicated queries respectively and returned nothing substantive above existing harvests. Both are recorded as vacancies rather than filled with adjacent robotics, generative-modeling, or software-engineering papers.
