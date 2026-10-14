---
title: "arXiv Paper Check — AI & CTR (October 14, 2026)"
type: synthesis
created: 2026-10-14
updated: 2026-10-14
sources: []
tags: [arxiv, arxiv-paper-check, daily-check, ai, ctr, advertising, recommendation, agents, agent-skills, agent-harnesses, memory, reasoning, retrieval, ir, safety, security, unlearning, efficiency, kv-cache, daily-digest]
---

# arXiv Paper Check — AI & CTR (October 14, 2026)

**Window framing, stated up front**: arXiv exposes no rolling "last 24 hours". The newest announced block at run time (2026-10-14 ~02:20 UTC) is the **2026-10-10 (Saturday) submission wave** — the previous `arxiv-paper-check` ([2026-10-12](../2026-10-12/arxiv-paper-check.md)) covered the Oct-09 block, and the [2026-10-13 arxiv-daily](../2026-10-13/arxiv-daily.md) re-mined that same Oct-09 block. This report therefore covers the **Oct-10 (+ early Oct-11) wave**, which is fresh to the series.

**Harvest**: arXiv export API over HTTPS, 19 category sweeps (`cat:cs.AI/LG/CL/IR/CV/MA/CR/NE/HC/SI/RO/DB/DC/SE/GT/SD`, `stat.ML`, `eess.AS/SP`) over `submittedDate:[202610100000 TO 202610111200]`, sorted descending. **594 unique candidate IDs**, all **grep-verified 0-hit** against the entire `wiki/` tree (8,842-ID baseline) before writing.

**CTR status**: **zero explicit Click-Through-Rate papers** this block (`"click-through rate"`, `"CTR prediction"`, `"click-through"` → 0 hits). The advertising/recommendation lane nevertheless returns a usable set — DPA relevance evaluation, generative-recommender poisoning, banner-ad auction mechanisms, LLM-native ad auctions, and four recommender papers — recorded in §①. As with the 10-12 report, the industrial CTR *architecture* (scaling laws, long-sequence modeling) lane is empty again.

⚠️ **Affiliation discipline**: arXiv API metadata carries no reliable affiliation field; affiliations were **not extracted and not inferred** this run. Venue tags are only those self-reported via the arXiv `comment` field.

---

## ① CTR, Advertising & Recommendation (8)

### LLM-based User-Product Relevance Evaluation for Dynamic Product Advertising
- **Authors**: Wen Zhang, Xiao Bai, Hsiang-wei Chao, Mengfan Zhu, Tong Zhao, Mingxuan Ju, Xiaodong Liu, Congfei Zhang, Yunzhi Zhou, Yajun Wang, Jinchao Li, Yu Zhang
- **arXiv**: [2610.14550](https://arxiv.org/abs/2610.14550) — cs.IR · **CIKM 2026**
- **Key contribution**: DPA retrieval evaluation is bottlenecked by sparse/biased offline engagement metrics and costly online tests. Proposes a **user–product relevance metric**: engagement history is compressed into a compact set of **intent representatives** via Semantic-ID-grouped, event-stratified segmentation; each recommended product is scored against each intent and aggregated into a user-level relevance score. Computed at scale with **LLMs as semantic judges** (agentic, human-aligned prompting → multi-category relevance guidelines, then teacher judgments distilled into a cheap student model). Strongly correlates with offline **and** online business metrics.
- **Why it matters**: A rare *evaluation-methodology* contribution for the ads-retrieval stack the wiki tracks (cf. [[est]], [[understanding-scaling-laws-rec]]) — intent-level relevance as a proxy that can be iterated before A/B.

### AlignPoison: Conditional Targeted Poisoning of Generative Recommenders via Decoding-Aligned Prefixes
- **Authors**: Zhuoxuan Zhang, Jinhao Duan, Xinyu Zhao, Jinduo Guo, Shuai Shao, Rui Li, Luke Simon, Zhun Deng, Tianlong Chen, Bo Sun
- **arXiv**: [2610.14487](https://arxiv.org/abs/2610.14487) — cs.AI · 23 pp.
- **Key contribution**: First study of **conditional targeted data poisoning** in autoregressive **generative recommenders** under a realistic black-box API setting. Injecting **<1%** synthetic interactions significantly raises the probability of promoting malicious targets under a trigger. Analysis isolates two drivers — **decoding alignment** and **prefix popularity**: short, context-aligned prefixes that are common under the model's induced transition dynamics and tied to a frequent trigger reliably amplify promotion. **AlignPoison** discovers/samples such prefixes from API outputs; improves ASR lift by up to **+16.3 pts**, in unimodal and multimodal settings.
- **Why it matters**: A new threat model for the wiki's generative-recommendation line ([[hstu-generative-recommendation]], [[ge4rec-generative-ctr]]): the discrete decoding interface is itself the attack surface.

### Diffusion-Based Auctions for Multi-Winner Banner Ads
- **Authors**: Lilian Sun, Henry Huang, Fucheng Warren Zhu, Giannis Daras, Constantinos Daskalakis
- **arXiv**: [2610.14473](https://arxiv.org/abs/2610.14473) — cs.GT, cs.AI, cs.LG · **EC 2026**
- **Key contribution**: Replaces the single-winner banner auction with a mechanism where **multiple bidders co-win** one impression and jointly steer the shown image. Bidders declare **value per unit of alignment** between the final image and their own textual description; bids are combined into a score driving the **reverse process of a diffusion model**, from which welfare-maximizing candidates are sampled. Experiments show efficiency gains over single-winner allocation, monotonicity, and approximate incentive compatibility (with Myerson/Clarke-style payments) that improve with Monte-Carlo samples while preserving image quality.
- **Why it matters**: Generative ad *creatives* become the allocation outcome — the diffusion mechanism-design analogue of generative-ads systems.

### Beyond Independent Values: Optimal Auctions with Correlated Valuations for LLM-Native Advertising (AffMyerson)
- **Authors**: Shiman Sheng, Mingyu Guo
- **arXiv**: [2610.14646](https://arxiv.org/abs/2610.14646) — cs.GT, cs.MA
- **Key contribution**: In conversational assistants, advertisers all read the **same conversation**, so their willingness-to-pay moves together — yet existing LLM-ad auctions assume independence. **AffMyerson** models conversation-conditioned values as a **multivariate normal** and turns positive dependence (**affiliation**) into a sign condition on the precision matrix, enforced by a neural parameterization. Proves the family yields **truthful, ex-post IR** auctions (estimation error costs revenue, never truthfulness); derives closed-form conditional virtual values; pricing is **O(n²)** with no matrix inversion. With LLM-agent bidders, earns **+6.2%** vs second-price-with-reserve, **+6.1%** vs Ronen lookahead, **+9.2%** vs Myerson-as-independent — still **+4.5%** on real keyword-search queries.
- **Why it matters**: Formalizes the "common demand" structure unique to LLM-mediated advertising — the auction-theory counterpart to [[byoai]] / [[build-for-agents]]'s AI-intermediary shift.

### Pathwise Alignment for Collaborative Filtering (PACF)
- **Authors**: Zhiwei Li, Guodong Long, Chengqi Zhang, Jing Jiang
- **arXiv**: [2610.15506](https://arxiv.org/abs/2610.15506) — cs.IR · 25 pp.
- **Key contribution**: BPR-trained matrix factorization updates each user only through that user's own observations, so sparse feedback gives few constraints. PACF trains MF with **one network shared across all training pairs**: a **flow-matching term** predicts the user-to-item step (reversed/scaled for negatives), and a **trajectory-consistency term** pulls each user's predicted path to end at the observed item; the network is **discarded at inference**, keeping MF efficiency. Proves a bounded-sensitivity network accurately fits users sharing an item only if their embeddings are close. Highest performance on **all 7 datasets** vs 11 baselines, with the largest relative gains where feedback is sparsest.
- **Why it matters**: A cheap way to import cross-user constraints into a classic CF model without changing inference cost.

### Context-Coupled Graph Learning for Multimodal Recommendation (CC-MGRec)
- **Authors**: Mingqiao Zhang, Qiyao Peng, Yumeng Wang, Wenzhe Dong, Hongtao Liu, Jian Yang
- **arXiv**: [2610.15523](https://arxiv.org/abs/2610.15523) — cs.IR
- **Key contribution**: Multimodal graph recommenders aggregate collaborative and semantic relations in a **context-separated** way, limiting cross-layer composition. CC-MGRec unifies **Semantic-Behavioral Evidence** in one context-coupled graph: user-item collaborative relations + item-item semantic relations with **joint normalization**; **recommendation-grounded semantic calibration** adjusts semantic neighbor weights using training behavior; **collaborative-semantic compositional propagation** forms implicit **Preference Evidence Chains** across layers. Improved quality and **faster inference** on 3 Amazon datasets, with theoretical analysis.
- **Why it matters**: The multimodal-rec thread's move from fusion-at-the-end to single-pass evidence composition.

### Federated Semantic Residuals for Multimodal Recommendation (SERA)
- **Authors**: Zhiwei Li, Guodong Long, Chengqi Zhang, Jing Jiang
- **arXiv**: [2610.15505](https://arxiv.org/abs/2610.15505) — cs.IR · 23 pp.
- **Key contribution**: Existing federated multimodal recommenders fuse content *into* the model, obscuring how content reorders the list. **SERA** keeps content out and adds **semantic residual scores** on top of a base FedRS's collaborative scores, so content lifts an item only when its residual exceeds the collaborative-score gap. A **residual bound** provably limits which items content can lift (an item enters the list only if its collaborative score is within twice the bound of the lowest in-list score). Validated bound improves **all 3 FedRSs on all 6 datasets** with no added personalized parameters, beating FedMRs in most comparisons.
- **Why it matters**: An interpretable, modular content-adapter for privacy-preserving ranking — auditable interaction between collaborative and semantic signals.

### Vela: User Behavior as Supervision Sparks LLM Intelligence
- **Authors**: Yang Xiao, Yusong Sun, Haoyi Wu, Wenyang Hui, Weiqiang Hang, Luqing Wang, Zejian Wang, Zirui Tu, Jingsheng Mao, Shaobo Hu, Yang Luo, Jiale Guo, et al.
- **arXiv**: [2610.14709](https://arxiv.org/abs/2610.14709) — cs.CL, cs.AI
- **Key contribution**: Current LLMs are trained on static text or synthetic data — neither captures how a user's behavior evolves over weeks-to-years, the "user dimension" that recommendation/advertising/personal-assistant deployments need. **Vela** converts **anonymized behavior records of 100,000 users** into **100,000 tasks across 91 real-world templates**; difficulty filtering + trajectory acceptance keep ~**75,000** tasks. Fine-tuning Qwen3.6-35B-A3B improves user-related tasks by up to **+11.5 pts** and general benchmarks by **+4 pts** on average; **RL after SFT** beats RL-from-base by up to **+7.7 pts**.
- **Why it matters**: Turns logged user behavior into a scalable supervision source — directly relevant to the [[byoai]] / personalized-agent thread and a bridge between recsys data and general LLM capability.

---

## ② Agent Skills, Harnesses & Memory (8)

### Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses
- **Authors**: Weichen Yu, Lesly Miculicich, Bhavana Dalvi Mishra, Jiefeng Chen, Shuo Li, Matt Fredrikson, Tomas Pfister, Long T. Le
- **arXiv**: [2610.15150](https://arxiv.org/abs/2610.15150) — cs.AI
- **Key contribution**: Self-evolving agents treat the **harness** (inputs/tools/memory/execution scaffold) as an optimization target, but existing work optimizes a **single objective** on a **monolithic** artifact. Harmony Harness formulates harness evolution as **multi-objective optimization**, using **decomposition-based evolutionary search** to maintain a Pareto frontier, plus **factorized evolution operators** that separately refine general-purpose mechanisms and benchmark-specific adaptations, composed at inference time. Beats strong harness baselines by **>10%** on SecRepoBench and BaxBench.
- **Why it matters**: The harness-evolution thread ([[agentic-engineering]]) gets objective trade-offs and structural separation — transferable design vs environment adaptation.

### HarnessNet: Feedback-driven Hierarchical Joint Harness Evolution for Multi-agent Systems
- **Authors**: Zhaoyuan Qiu, Sachith Seneviratne, Yu Xia, Saman Halgamuge
- **arXiv**: [2610.15221](https://arxiv.org/abs/2610.15221) — cs.AI
- **Key contribution**: Extends harness evolution from single agents to **multi-agent systems**. Basic unit **Agentron** = evolvable forward harness + frozen foundation model + **local optimizer** that can only see/modify its own harness. Agentrons form a **layered graph** with **backward-propagating feedback**; upstream optimizers receive node-specific feedback from the layer below, decomposing joint evolution into smaller coordinated sub-tasks with separate contexts. On AgentBench, matches a single global optimizer while respecting **local privacy** and using fewer tokens/time; evolved harnesses **transfer** across foundation models.
- **Why it matters**: Scales self-improvement to MAS with privacy/local-access constraints — a distributed counterpart to Harmony Harness.

### SkillForgeBench: Evaluating Agent Reliability Grounded in Agent Skill Specifications
- **Authors**: Zhengxi Li, Junyi Zhou, Qiyuan Zhang, Chuhan Wu, Fuyuan Lyu, Le Tian, Xiao Zhou, Chen Ma, Yufei Wang
- **arXiv**: [2610.14918](https://arxiv.org/abs/2610.14918) — cs.AI, cs.CL · 38 pp.
- **Key contribution**: Reconciles the depth-vs-diversity trade-off in agent benchmarks by using **agent skills as execution blueprints**: domain-balanced skills guide artifact retrieval; skills act as procedural anchors to synthesize tasks and sandbox scenarios; skill-embedded requirements become fine-grained **completion + process rubrics**. **842 sandboxed tasks** across 5 domains reveal a steep capability hierarchy (Opus 4.8 leads at **40.9% strict completion**; per-rubric pass 70.0–85.7% collapses to 12.6–40.9% when *all* constraints must hold). Skills give larger gains to stronger agents (**+19.2%** Opus 4.8 vs **+5.8%** Haiku 4.5); process rubrics are satisfied far less often than completion rubrics (<3% for Haiku 4.5).
- **Why it matters**: Quantifies that **completion-only checks overestimate reliability** — the benchmark-validity arc applied to agent skills.

### SkillHorizon: Constructing Long-Horizon Agent Tasks through Skill Composition
- **Authors**: Yuxuan Liu, Zhaochen Su, Hangyu Guo, Shijue Huang, Zhixiong Zhang, Kawai Chung, Zhongwei Xie, Tianshi Zheng, Wei Fan, Qing Zong, Haochen Shi, Baixuan Xu, et al.
- **arXiv**: [2610.14966](https://arxiv.org/abs/2610.14966) — cs.AI · 29 pp.
- **Key contribution**: Builds long-horizon tasks by **skill composition** across 7 business environments: generators turn reusable skill procedures into business activities linked by **input-output dependencies, shared resources, and state updates**, so workload and coordination demand grow together. **1,050 tasks** with reference interaction workloads from 64K to 1M tokens; programmatic evaluators score local completion and whole-task success. Mean local-goal completion falls **90.4% → 46.8%** as scale grows; at larger workloads agents submit unsuccessful finals with work unfinished and tool-call budget remaining.
- **Why it matters**: A configurable testbed for *sustained progress and dependency coordination*, exposing where long-horizon agents silently give up.

### SkillFusion: Towards Reliable Multi-Skill Composition for LLM Agents
- **Authors**: Enhao Huang, Xinye Zhao, Yiming Li, Bingrun Yang, Nanjun Zhou, Chunshu Xia, Hongwei Yao, Zhan Qin
- **arXiv**: [2610.15481](https://arxiv.org/abs/2610.15481) — cs.AI · 29 pp.
- **Key contribution**: Independently authored skills can impose **incompatible requirements, competing preferences, redundant instructions** when jointly loaded. SkillFusion is an **offline compiler** that reconciles interactions into one reusable merged skill via **typed, scoped constraints** linked to source directives: a type-scope gate + selective fallback for candidate interactions, an interaction-type classifier, an **adversarial verifier** for uncertain judgments, and resolvers (conditional routing / explicit priorities for hard conflicts; verified abstraction for soft conflicts; dedup). Highest mean success among non-oracle methods on 3 agent benchmarks + 2 transfer benchmarks across 3 executor models; **>2.5×** the success of unresolved multi-skill loading at the largest configurations.
- **Why it matters**: Skill *reconciliation* as a compilation problem — the missing layer between authoring skills and loading them.

### When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization (FSM)
- **Authors**: Haomiao Qiu, Yining Tang, Hongyi Wan, Changfeng Sun, Ziyue Qiao, Miao Zhang
- **arXiv**: [2610.15492](https://arxiv.org/abs/2610.15492) — cs.AI
- **Key contribution**: Studies **forgetting in continual skill internalization** and finds a hierarchy: early on a model may lose the ability to **invoke** an old skill from a raw request (**skill-addressing forgetting**) while supplying the canonical skill name restores behavior; with further training even that conditional execution degrades (**skill-execution forgetting**). **Factorized Skill Memory** separates memory into a plastic **Address Memory** and a stable **Execution Memory** (per-stage LoRA executors, frozen after acquisition). On a 5-stage benchmark from 100 TaskBench skills: **65.95%** mean exact match, **93.38%** addressing accuracy, **+14.3 pts** over the strongest replay-free isolation baseline and within **1.9 pts** of full Replay.
- **Why it matters**: Names the two forgetting modes of skill reuse and gives a replay-free memory factorization to stop them.

### VitaBench: Memory Lifecycles Beyond Retrieval
- **Authors**: Muquan Yu, Dihan Hu
- **arXiv**: [2610.14731](https://arxiv.org/abs/2610.14731) — cs.LG · **NeurIPS 2026 CL4FMAgents Workshop**
- **Key contribution**: Long-term memory benchmarks test **retrieval**, but a persistent system must first decide whether a memory should stay exact, be compressed, consolidated, or **deleted**. VitaBench formalizes **memory-lifecycle evaluation** via repeated reviews and full-horizon counterfactual evaluation: a controlled **Diagnostic** tier and a naturalistic customer-service tier. Three diagnostics — **lifecycle headroom** (1.364 / 1.405), **horizon reversal** (60.2% / 56.5% of states change preferred action between short/full horizon), **optimal-action diversity**. A learned delayed lifecycle policy reaches **101.5** vs **83.4** for the best fixed strategy.
- **Why it matters**: Separates "retrieve past info" from "decide how it persists" — the memory-safety/design thread ([[mem1-agent]], MemTrapBench, LongHarness) gets its missing evaluation axis.

### MetaCascade: End-to-End Attacks on Agent Skills via Metadata-Only Poisoning
- **Authors**: Junhao Wen, Ping Deng, Qizhi Chen, Junchen Li, Shuang Liang
- **arXiv**: [2610.14836](https://arxiv.org/abs/2610.14836) — cs.CR
- **Key contribution**: Agent Skills are retrieved by **documentation** then selected by **metadata**, creating a **process-wide attack surface** driven entirely by metadata. **MetaCascade** is an **end-to-end metadata-only poisoning** framework: multi-view semantic expansion generates malicious skill candidates, and task + black-box competition feedback iteratively optimizes malicious metadata. Across 4 datasets and 2 agents (Hermes, OpenClaw), beats the strongest baselines by **+35.53 pts** average ASR and **+34.65 pts** under four defense settings.
- **Why it matters**: The skill supply-chain ([[skillopt-agent-skills]], [[supply-chain-attacks]]) gets its first full end-to-end poisoning chain — attacks land at *selection*, before execution.

---

## ③ LLM Training, Reasoning & Architectures (6)

### UltraBERT: Beyond the Limit of BERT Pre-Training
- **Authors**: Jungwoo Park, Taewhoo Lee, Jaewoo Kang
- **arXiv**: [2610.15028](https://arxiv.org/abs/2610.15028) — cs.CL, cs.AI
- **Key contribution**: Revisits encoder pretraining design and reports three findings: (1) encoders **saturate** on downstream tasks beyond a few trillion tokens; (2) **lower masking ratios benefit classification, higher ratios benefit retrieval** — contradicting prior "larger ratio for larger models"; (3) distillation-with-pruning helps classification at low ratios but degrades retrieval at high ones. **UltraBERT** assigns **separate LM heads to low- and high-masking data within a batch** and restricts distillation to the low ratio — the first encoder to reach SOTA on **both** classification (**GLUE 91.0**) and retrieval (**BEIR 47.7**).
- **Why it matters**: A clean re-think of the bi-encoder recipe, with a concrete compute/masking-allocation rule.

### Apertus 1.5: From Open Text Models to Open Multimodal Reasoners
- **Authors**: Project Apertus, Yixuan Xu, Yassine Turki, Vinko Sabolčec, Valentina Pyatkin, Tommy Chu, Sven Najem-Meyer, Sean F. Carroll, Robert Smith, Raphael Kreft, Oscar Alessandro Tazza, et al.
- **arXiv**: [2610.15542](https://arxiv.org/abs/2610.15542) — cs.CL
- **Key contribution**: Fully-open public-infrastructure model family extended from text to **multimodal reasoning**: continued pretraining on **4T tokens (8B)** / **2T (70B)**, adding image + audio understanding and a **4× context extension to 262,144 tokens**; multimodality enters through the **tokenizer**, LM head stays text-only, architecture unchanged. SFT + long-context FT + **RLVR** + preference alignment; **thinking is a chat-template flag** (lifts math reasoning up to +20 pts on 8B). The 8B leads fully-open models of its class on knowledge/instruction-following/cultural benchmarks; competitive on document understanding and low-resource speech. Trained only on openly available data, respecting crawler opt-outs.
- **Why it matters**: The "open, sovereign, documented-data" alternative to closed frontier labs — openness as a values statement (charter-published alignment).

### Fitting Every Hint Is Not Enough: Premature Floods in Recurrent Algorithmic Reasoners
- **Authors**: Amin Najafgholizadeh, Mohsen Afsharchi
- **arXiv**: [2610.14982](https://arxiv.org/abs/2610.14982) — cs.LG, cs.AI · 33 pp.
- **Key contribution**: Recurrent algorithmic reasoners trained with per-step hints on small graphs and run many more steps on large ones can **reproduce every training hint and still fail on deep graphs** — declaring nodes reached before the search reaches them ("**premature flood**"). Two routes are traced (hidden-state degree-input tail effects; neighbor-sum vs average) across the GRU processor and the benchmark's own GIN/PGN. Remedies: clamp the degree input or add 200 dense training graphs removes the GRU failures; detaching state between steps avoids the flood in that processor (0/23 seeds vs 6 under full backprop) but not with sums/residual updates.
- **Why it matters**: A concrete **out-of-distribution-on-input-range** failure for looped/recurrent reasoning — recommends auditing input/aggregate ranges and testing on deep graphs.

### The Optimal Decoder is Tilted Temperature
- **Authors**: Nikolaos Papagiannis, Ananth Grama, Wojciech Szpankowski
- **arXiv**: [2610.15058](https://arxiv.org/abs/2610.15058) — cs.LG
- **Key contribution**: Poses decoding as **pass@k maximization** under an entropy floor (diversity) and a cross-entropy ceiling (plausibility), proving the optimum is a single closed-form rule — **tilted temperature** q* ∝ (p·e^{ηV})^{1/T} with a verifier potential V. Ordinary temperature, verifier-greedy, and reward-tilted policies are special cases; under a natural diversity-budget scaling, the optimal temperature **increases with k** (turning an empirical rule into a theorem). Online estimator (J-EOS); offline, when calibrated, the tilt collapses to plain temperature (**Calibrated Temperature Decoding**, one scalar, zero inference overhead). Improves on HumanEval/MBPP decoding baselines.
- **Why it matters**: A theory of *why* temperature scaling with sample budget works, plus a practical calibration variant — relevant to [[rlvr]] / test-time scaling.

### From Existing Methods to New Research Ideas: Two Perspectives on Recursive Self-Improvement
- **Authors**: Leijun Zhou, Yanke Yu, Zhihao Liu, Qu Xiang, Tiancheng Hu, Yiru Dong, Yihan Wu, Yangxi Xiang, Xuejun Wu, Xi Chen, Buyue Qian, Yaowei Zheng, et al.
- **arXiv**: [2610.14625](https://arxiv.org/abs/2610.14625) — cs.AI
- **Key contribution**: A unifying survey of **recursive self-improvement (RSI)** with a **nine-dimension taxonomy** in four groups (update targets; update organization; update schedule & scope; feedback & selection), mapping existing methods into a shared design space to generate new ideas. Second thread draws explicit analogies to traditional deep learning (optimization, regularization, data augmentation, continual learning, adversarial learning) and evolutionary computation; reviews benchmarks across online/offline/offline-to-online settings.
- **Why it matters**: A scaffold for the wiki's autoresearch / RSI thread ([[autoresearch]], AI4AI-Bench) — dimensions rather than ad-hoc methods.

### Large Decision Models: Repurposing LLMs as Single-Pass Decision Makers (LDM)
- **Authors**: Ziyi Chen, Yan Zhang, Jianhui Wei, Jianing Yin, Daoan Zhang
- **arXiv**: [2610.15501](https://arxiv.org/abs/2610.15501) — cs.AI
- **Key contribution**: LLM decision-making pays sequential-decoding cost and does not expose decision probabilities; task-specific classifiers need per-task training. **LDMs** return **explicit probabilities over run-time-specified labels via a single prefill forward pass**. Adapted with **Diverse Decision Supervision** (varied domains/rules/labels); **Self-Posed Reasoning Distillation** adds consistency-filtered teacher tasks with label distributions from repeated teacher reasoning. On DecisionVista: +1.8/+1.5 pts over a step-matched baseline and a **182× latency speedup** vs reasoning rollout (Gemma-4-31B); a confidence router recovers a median **92%** of reasoning's accuracy advantage at 27–58% of its tokens.
- **Why it matters**: A single-pass decision interface with calibrated probabilities — relevant to classification-style serving (relevance, moderation, routing).

---

## ④ Safety, Security & Unlearning (2)

### The Agent Clicks Approve: Injected Page Text Makes Browser Agents Authorize Access the Task Never Named
- **Authors**: Md Imran Hossen
- **arXiv**: [2610.15138](https://arxiv.org/abs/2610.15138) — cs.CR
- **Key contribution**: A browser agent in the user's signed-in session is a **confused deputy**: the session supplies authority, the page supplies the access request (OAuth grant or webhook URL) to approve, and nothing checks them against each other. On two authorization surfaces with two providers, the unauthorized action completed in **all 73 attack runs** without a defense; an instruction that only the user's task authorizes a grant still left **7/10** consent attacks completing. The **authority envelope gate** moves the check to the point of action: the service accepts a request only if it matches the task's pre-fixed envelope (client, account, or webhook URL). With the gate, the agent still sent the request in all 70 runs but the service rejected each; all named-task controls succeeded.
- **Why it matters**: Prompt-injection's "lethal trifecta" made concrete at the **authorization** layer — the fix belongs in the service, not the model ([[prompt-injection]], [[supply-chain-attacks]]).

### Decoupling Knowledge Forgetting and Refusal Learning in MLLM Unlearning (FASD)
- **Authors**: Haodong Chen, Shengtao Wen, Dong Liang, Lingbing Guo, Xiang Chen
- **arXiv**: [2610.14605](https://arxiv.org/abs/2610.14605) — cs.AI, cs.CL, cs.IR, cs.LG
- **Key contribution**: Surface-level "stops outputting target info" masks two failures: knowledge-suppression induces **confabulation** (hallucinating about the unlearned subject), and refusal training **changes behavior without erasing knowledge** (declines open queries but answers under multiple-choice probing). **Forget-Aware Self-Distillation (FASD)** targets **honest ignorance** via two channels: a **behavior channel** distills refusals from an ignorance-prompted copy of the model (masking target tokens from the teacher distribution to avoid re-teaching), and a **knowledge channel** directly suppresses ground-truth answer spans independent of generated responses.
- **Why it matters**: Separates *behavior* from *knowledge* in unlearning, with a probing test for genuine erasure — the safety-evaluation-honesty thread.

---

## ⑤ Efficiency & Systems (3)

### KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization
- **Authors**: Sihwan Park, Sung-Yub Kim, Doohyuk Jang, Eunho Yang
- **arXiv**: [2610.14448](https://arxiv.org/abs/2610.14448) — cs.LG, cs.AI · 32 pp.
- **Key contribution**: Characterizes **KV concentration** in asynchronous RLVR rollouts (sustained concurrency concentrates context processing into fewer decode steps, raising KV workload per step) and finds KV-cache quantization beats weight-only / weight-activation quantization. Naive INT4 KV degrades learning even with truncated importance sampling; **KV4-RL** combines calibration-free INT4 KV with **selective INT8 protection of attention sinks and recent context**. Over 400 GRPO iterations (Qwen3-8B-Base): **1.80×** cumulative rollout speedup, **1.27×** full-iteration speedup, **1.97×** over the final 50 iterations, with final accuracy within **0.5 pts** of BF16 for Qwen3-4B/8B.
- **Why it matters**: A deployment-grade speedup for the RLVR training loop the wiki tracks ([[rlvr]], [[reinforcement-learning]]) — protects exactly the positions that matter.

### Swarm Telepathy (SwaT): Prefill-Free KV-Cache Transfer Across Families
- **Authors**: Abdulrahman Alabdulkareem, Irene Tenison, Yang Zhang, Yada Zhu, Boris Katz, Dan Gutfreund
- **arXiv**: [2610.15095](https://arxiv.org/abs/2610.15095) — cs.LG
- **Key contribution**: Multi-agent systems communicate through text, constraining bandwidth and wasting compute; prior KV transfer needs same-family models or still requires the receiver to prefill. **SwaT** is the first **cross-family, prefill-free** KV-cache transfer method. Combined with KV compaction it beats text-to-text communication by a mean **+40% accuracy** and **4× faster** wall-clock; works across **17 benchmarks, 12 LLMs, 6 families**; transfers vision capability from a sender VLM to a text-only receiver despite text-only training. Both models stay frozen; needs **<50M tokens** and **<1 GPU-day** to train.
- **Why it matters**: Latent inter-agent communication with real bandwidth/compute savings — directly relevant to Karpathy's "teams of agents" vision and the [[llm-os]] stack.

### Fewer Bits, More Tries: Recovering Capability Under Memory Constraints
- **Authors**: Tomer Galanti, Josh Susskind, Eran Malach
- **arXiv**: [2610.15372](https://arxiv.org/abs/2610.15372) — cs.AI
- **Key contribution**: Asks whether a smaller/compressed model run **multiple times in parallel with test-based selection** can recover the capability gap. Across four code-gen benchmarks, **verified retry** recovers much of the accuracy lost to size or compression: a 7B Qwen with 8 parallel attempts essentially matches a 32B on MBPP+ and exceeds it on the other three, using ~**4× less memory**, up to **6× faster**, and less energy.
- **Why it matters**: Frames capacity-vs-verified-compute as a hardware-aware trade — the local-inference counterpart to [[verifiable-rewards]].

---

## ⑥ IR & Retrieval (2)

### Self-improving data synthesis can scale embedding models across domains and tasks (SYNTRA)
- **Authors**: Zucan Lyu, Rui Tang, Jianlyu Chen, Peisheng Jin, Zheng Liu, Defu Lian
- **arXiv**: [2610.14730](https://arxiv.org/abs/2610.14730) — cs.IR, cs.AI, cs.LG · 30 pp.
- **Key contribution**: Adapting embedding models to new tasks usually requires costly manual data design. **SYNTRA** iteratively refines **reusable synthesis instructions** using feedback on trial outputs, needing only an unlabelled corpus and a few query-document pairs. Across **24 retrieval datasets / 15 domains**, the synthesized data improves strong embedding models with and without existing labelled sets; self-improvement helps on **all 6 tasks**, beating human calibration on 4; MS MARCO performance keeps improving to **32×** the initial training size. Code + data released.
- **Why it matters**: A self-improving retrieval-data flywheel — the data-synthesis analogue of the RSI thread, applied to IR.

### What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)
- **Authors**: Mahe Chen, Nick Koudas
- **arXiv**: [2610.15033](https://arxiv.org/abs/2610.15033) — cs.IR, cs.CL, cs.LG, cs.SI
- **Key contribution**: Studies what earns citations in generative search across two 90-day collections (**158,099 answers / 468,037 citations**). Within a website, **question-matching titles/paragraphs** raise citation; FAQ blocks/structured data/page speed only help across websites. Replaying questions through APIs shows **retrieval dominates**: every page ChatGPT cites was retrieved by its own search (**32%** of variance vs **2.8%** for page properties), with sub-queries rewritten per answer and rarely matching Google/Bing. The model's **own knowledge** writes brands into searches and names brands with no supporting page; brand names reorder rankings of identical-fact products.
- **Why it matters**: Quantifies the "cited when searched, named when remembered" split — the mechanism behind the wiki's AI-citation / GEO interest and a caution for AEO tactics.

---

## Also worth recording (not detailed above)

- **`2610.14474`** — *RES-MR: Risk-Aware Reasoning for Explainable and Safe Medication Recommendation* (Cong Wang et al.). LLM medication recommendation with explainable clinical-reasoning distillation + risk-aware policy optimization using disentangled drug factors as patient-specific reference prototypes; improves accuracy/safety/explainability over SOTA.
- **`2610.14763`** — *CUSE: Fine-Grained Multimodal Unlearning with Counterfactual Guidance and On-Policy Self-Distillation*. Counterfactual-guided, on-policy self-distillation for multimodal unlearning.
- **`2610.15382`** — *Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations* (cs.IR). Companion empirical study to the GEO paper above.
- **`2610.15409`** — *CoverSynth: Coverage-Guided Generation of Retrieval Evaluation Sets*. Fuzzing-style coverage guidance to synthesize retrieval eval sets.
- **`2610.14816`** — *Data Curation and Model Souping: Unlocking Qwen3-0.6B for MS MARCO Passage Ranking*. Small-model recipe reaching competitive MS MARCO ranking.
- **`2610.14903`, `2610.15299`** — niche ML wins (5G-edge multi-agent orchestration; "WisdomNet" trustable error-free classification) noted for completeness.

---

## Cross-cutting observations

1. **The CTR architecture lane stays empty; the ads/rec *mechanism* lane is alive.** No CTR-prediction or scaling-law paper this block, but advertising returns through **mechanism design** (Diffusion-Based Banner Auctions, AffMyerson correlated-value auctions) and **evaluation** (DPA intent-level relevance). Generative recommenders are also newly *attacked* (AlignPoison). This is the fifth consecutive window without a CTR-scaling entrant ([[ctr-scaling-landscape]]).
2. **"Agent skills" crystallizes into a full lifecycle.** One block yields a benchmark (SkillForgeBench), a long-horizon generator (SkillHorizon), a multi-skill compiler (SkillFusion), a forgetting study + memory factorization (FSM), and an end-to-end poisoning chain (MetaCascade). Skills are now authored, composed, internalized, forgotten, and attacked — a supply chain in the making ([[supply-chain-attacks]], [[skillopt-agent-skills]]).
3. **Harness evolution goes multi-objective and multi-agent.** Harmony Harness (Pareto, factorized operators) and HarnessNet (hierarchical, privacy-local Agentrons) both argue the harness is an optimizable, *transferable* artifact whose value should be separated from environment specifics ([[agentic-engineering]]).
4. **Memory's real problem is persistence policy, not recall.** VitaBench formalizes compression/consolidation/delete decisions; FSM separates addressing from execution. Memory quality is now about *deciding what to keep*, echoing MemTrapBench/LongHarness.
5. **Safety moves to the authorization and unlearning boundary.** The confused-deputy browser-agent result puts the fix in the *service* (authority envelope), and FASD insists unlearning distinguish behavior from knowledge ("honest ignorance"). Both are evaluation-honesty moves: don't trust the surface signal.
6. **Efficiency turns to protecting what matters.** KV4-RL protects attention sinks + recent context in INT4; SwaT communicates agents in latent KV across model families; "Fewer Bits, More Tries" trades verified test-time compute for memory. Compression + verification as the recurring lever.

---

## Method note

**Queries**: arXiv export API (HTTPS), 19 category sweeps over `submittedDate:[202610100000 TO 202610111200]`, `sortBy=submittedDate desc`, paginated. 594 unique candidate IDs harvested; all featured IDs `rg -l -F`-verified **0-hit** against the full `wiki/` tree (8,842-ID baseline) immediately before writing. **Dedup**: no featured paper collides with the Oct-09 reports (`2026-10-12 arxiv-paper-check`, `2026-10-13 arxiv-daily`) or any sibling digest.

⚠️ **Window semantics**: "last 24 hours" is not exposed by arXiv. The newest block at run time is the **2026-10-10 single-day wave** (plus early Oct-11 submissions captured before the block boundary); the previous report covered Oct-09. This is a **fresh** block, not a re-mine.

⚠️ **CTR-lane caution**: **zero** explicit Click-Through-Rate papers in this block; the ads/rec yield is in mechanism design, evaluation methodology, and recommender modeling. Recorded explicitly so the zero-CTR result is not mistaken for an omission.

⚠️ **Affiliation discipline**: affiliations are not reliably present in arXiv API metadata and were **not extracted and not inferred** this run. Venue tags are only those self-reported via `comment` (e.g. CIKM 2026, EC 2026, NeurIPS 2026 workshop).

⚠️ **No independent replication**: none of the results were independently replicated or reproduced by a second group. All metric values are as self-reported in the abstracts.
