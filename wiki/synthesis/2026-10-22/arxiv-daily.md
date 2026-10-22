---
title: arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-22)
type: synthesis
created: 2026-10-22
updated: 2026-10-22
sources: []
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, rag, agentic-rl, multi-agent, world-models, long-context]
---
# arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-22)

> Auto-generated from recent arXiv publications (submissions ~2026-10-20 to 2026-10-21). Deduplicated against existing wiki reports (many 10-20 papers already covered; this report focuses on newly surfaced papers from 10-21 and select 10-20 items not previously featured).

## Summary

Today's cluster centers around: (1) **Generative recommendation & retrieval** — CAPE restores long-tail memorization in generative recommenders (beam-search+likelihood both forget tails), LoopRec does item-level adaptive recursion for sequential recommendation, FineSID learns progressive content->relevance->personalization for CTR, SOAR adds social/opinion signals, and MAPS regulates RAG search momentum via macro-adaptive parallel reasoning. (2) **Agentic RL, memory & harnesses** — BIRD-RL scales agentic RL over stateful data-centric SQL environments with trajectory-scoped persistence (12.8× spatial efficiency), Uni-Mem jointly learns long-horizon agent memory construction+retrieval with stage-decoupled GRPO/ECA, Harness Scaling shows cross-harness generalization from diverse white-box harnesses, and Credit Where Credit Is Due (CATS) does contrastive attribution for MAS topology pruning. (3) **World models, embodied agents & games** — LiveAct does real-time multi-agent world models with heterogeneous action interfaces; Agentic World Action Models (AW-0) couple code/vision/action with reusable skill libraries; ALPS/PhysiCalWorld/CADRE rethink visual encoders/prediction for interactive world models; TARSphere is a robot-oriented full-stack framework for long-horizon embodied agents in evolving physical/social environments. (4) **Reasoning, distillation & alignment** — DPT encourages parallel thinking path diversity via prefix-similarity penalties; LongZero does self-generated long-context RL from zero external data; Flat-RLVR promotes flat reward optima to reduce distribution sharpening; TeachBack uses bidirectional preference optimization for on-policy self-distillation. (5) **Mechanism/design theory** — GSP autobidding equilibria computable in polynomial time for few advertisers/slots; nucleon for matching games; certifying Nash in general-sum games; cartel enforcement vs collusion in markets (LLM/RL agents).

## 1. Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval and Ranking
- **arXiv**: [2610.29298](https://arxiv.org/abs/2610.29298)
- **Date**: 2026-10-21
- **Authors**: Xu Huang, Jiancan Wu, Hongzheng Qin, Jiawei Feng, Can Ye, Wencong Zeng, Fengze Li, Xiang Wang (Univ. of Science and Technology of China; Independent Researcher/Ant Group)
- **Institution/Company**: USTC / Ant Group-affiliated
- **Categories**: cs.IR

### Abstract
Generative recommenders replace retrieve-then-rank with a single model: beam search over semantic item identifiers performs retrieval, and the same likelihood performs ranking. We show this shared score makes them forget long-tail items twice. In retrieval, beam search keeps identifier prefixes by subtree probability mass so tail items are pruned early; wider beams admit few more. In ranking, likelihood places tail items below head items even when admitted, so expanding retrieval alone brings little gain. Both failures reflect missing item-level memorization (direct co-occurrence recall) that collaborative filtering provides but shared-prefix generation lacks. We propose CAPE (Co-occurrence-Aware Pool Expansion), a training-free plug-in that restores memorization at both stages: (i) a memorization channel retrieves co-occurrence-supported tail items outside the beam and scores them with the frozen generator, and (ii) memorization-calibrated ranking fuses generator likelihood with co-occurrence evidence while keeping the generator's first item. Experiments on product/music domains show CAPE significantly improves long-tail accuracy over backbones and re-ranking baselines sharing candidates, preserves/improves overall accuracy, adds small latency fraction.

### Key Innovations
- **Double forgetting diagnosis**: shared prefix/likelihood causes tail pruning in beam search and ranking demotion even if admitted.
- **CAPE (training-free)**: memorization channel (co-occurrence outside beam + frozen generator scoring) + memorization-calibrated ranking (fuse likelihood+co-occurrence, keep first item).
- **Pragmatic**: works on frozen generative recommenders, improves long-tail without sacrificing overall accuracy.

## 2. Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation
- **arXiv**: [2610.30128](https://arxiv.org/abs/2610.30128)
- **Date**: 2026-10-21
- **Authors**: Zhanshuo Cao, Jiakai Tang, Yuqi Zhou, Sunhao Dai, Jun Xu (Renmin University of China)
- **Institution/Company**: Renmin University of China
- **Categories**: cs.IR, cs.AI, cs.CL, cs.LG

### Abstract
Existing sequential recommenders allocate fixed computation to every item regardless of contribution. We find (1) non-uniform computational need: items vary in convergence depth (most shallow, critical few need full depth), (2) fixed allocation is suboptimal vs oracle non-uniform assignment. We propose LoopRec: recursively apply a single weight-shared block with a lightweight per-item exit-or-continue gate at each recursion boundary. Items mature early exit; others recurse deeper. This makes depth learned per-item without auxiliary labels and adapts to diverse backbones. Experiments on public benchmarks with four backbone families show consistent gains over matched fixed-depth; learned allocation favors lower-frequency and more recent items.

### Key Innovations
- **Item-level adaptive recursion** with weight-shared block + per-item gating (exit/continue).
- **Diagnostic evidence** that uniform depth wastes capacity and hurts quality.
- **Generalizable** across backbone families; interpretable allocation patterns.

## 3. Progressive Learning from Content to Relevance to Personalization for CTR Prediction
- **arXiv**: [2610.29138](https://arxiv.org/abs/2610.29138)
- **Date**: 2026-10-21
- **Authors**: Zhiguang Yang, Yulin Yang, Fuyu Lv, Dan Ou (Alibaba Group)
- **Institution/Company**: Alibaba Group
- **Categories**: cs.IR, cs.MM

### Abstract
Multimodal CTR needs to integrate item content, query-item relevance, and user preference. We propose FineSID, a progressive learning framework unifying content tokenization, query-item semantic pretraining, and personalized post-training via shared fine-grained discrete representations. (1) Pretrained multi-scale visual + text tokenizers convert heterogeneous content into fine-grained Semantic IDs aligned with ID features. (2) Full-parameter semantic pretraining under query-item relevance supervision builds matching prior across multimodal SIDs and conventional fields. (3) Direct fine-tuning with user clicks captures personalized preferences. Offline/online evals show gains in CTR and core business metrics; improves within-product creative discrimination beyond ID memorization.

### Key Innovations
- **Progressive pipeline**: content tokenization → relevance pretraining → personalization fine-tuning with shared fine-grained SIDs.
- **Fine-grained multimodal tokenization** aligned to ID space; joint optimization of multimodal SIDs + conventional fields.
- **Production-oriented**: shows business metric gains and better creative discrimination.

## 4. SOAR: Social and Opinion-Aware Recommendations
- **arXiv**: [2610.29556](https://arxiv.org/abs/2610.29556)
- **Date**: 2026-10-21
- **Authors**: Giannis Christoforidis, Apostolos N. Papadopoulos
- **Institution/Company**: not stated in abstract (academic)
- **Categories**: cs.LG, cs.IR

### Abstract
We propose SOAR (Social and Opinion Aware Recommendation) incorporating friendship network and textual reviews (with sentiment emphasis) for POI recommendation. Experiments on real-world datasets show adding reviews improves recommendation precision.

### Key Innovations
- **Joint social+opinion signals** for POI recommendation with sentiment-aware review utilization.

## 5. MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation
- **arXiv**: [2610.29792](https://arxiv.org/abs/2610.29792)
- **Date**: 2026-10-21
- **Authors**: Xinze Li, Dingwen Zhang, Zhenghao Liu, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun (Northeastern University; Tsinghua University)
- **Institution/Company**: Northeastern U, Tsinghua U
- **Categories**: cs.CL

### Abstract
Interleaved reasoning-retrieval RAG can suffer from redundant/ineffective sub-queries and insufficient exploration; evolving reasoning influences query intent. We introduce **search momentum** (accumulated retrieval tendency from historical sub-query changes). Analysis shows query generation tends to evolve along existing retrieval trajectories. MAPS (Macro-Adaptive Parallel Reasoning) retains retrieved knowledge and refined reasoning state to reduce historical trajectory influence, extends sequential reasoning to parallel reasoning at each iteration (identifies complementary directions, generates parallel sub-queries, consolidates evidence), improving performance across six QA benchmarks on different backbones. Code: [NEUIR/MAPS](https://github.com/NEUIR/MAPS).

### Key Innovations
- **Search momentum** metric quantifying drift along retrieval trajectories.
- **Macro-adaptive parallel reasoning**: state preservation + parallel complementary query generation + evidence consolidation.
- **Empirical**: reduces query-intent drift / improves exploration.

## 6. BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments
- **arXiv**: [2610.29426](https://arxiv.org/abs/2610.29426)
- **Date**: 2026-10-21
- **Authors**: Ge Qu, Jinyang Li, Xiaohan Xu, Xiaolong Li, Bowen Qin, Nan Huo, Ziwei Tang, Chenhao Ma, Reynold Cheng (Univ. of Hong Kong; National Univ. of Singapore; CUHK-Shenzhen)
- **Institution/Company**: HKU/NUS/CUHK-SZ
- **Categories**: cs.LG, cs.CL (Accepted NeurIPS 2026 Main Track)

### Abstract
Tool-centric agentic RL struggles with stateful data-centric tasks (e.g. SQL debugging) — separate DB containers per rollout are inefficient; naive DB reuse causes trajectory contamination/cross-trajectory interference. BIRD-RL introduces a four-stage curriculum alternating foundational reasoning and trajectory-adaptive on-policy exploration, plus a **Trajectory-scoped Persistent Execution Infrastructure** enabling safe DB replica reuse with trajectory isolation (12.8× spatial efficiency). 7B/14B achieve 44.40%/48.00% on BIRD-CRITIC-SQLite, competitive with Claude-Opus-4.6 Agent (48.20%); trains unified SLMs for SQL debugging+generation.

### Key Innovations
- **Trajectory-scoped persistence** for stateful DB environments (safe reuse + isolation).
- **Four-stage curriculum** for stable training in contaminated stateful settings.
- **Efficiency win** 12.8× spatial; strong performance vs proprietary agents.

## 7. Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization
- **arXiv**: [2610.29671](https://arxiv.org/abs/2610.29671)
- **Date**: 2026-10-21
- **Authors**: Zhiqian Xia, Jielong Tang, Ling-An Zeng, Shixiong Kai, Rong Yao, Hao Kong, Xiao Dong, Wei Wang, Mingxuan Yuan, Siyu Xia, Haifeng Xia
- **Institution/Company**: not fully stated in abstract (industrial/academic mix)
- **Categories**: cs.CL

### Abstract
Learnable memory managers must co-adapt construction and retrieval. Joint RL with GRPO suffers from confounded group comparisons and sparse feedback. We propose **Stage-Decoupled GRPO** (alternate construction/retrieval optimization while controlling variation from the other stage) and **Event-Wise Credit Assignment (ECA)** (localize feedback to responsible events, propagate to constituent operations). Uni-Mem outperforms strongest RL-based memory on LoCoMo and LongMemEval.

### Key Innovations
- **Unified online policy** for both memory construction and retrieval (end-to-end co-adaptation).
- **Stage-Decoupled GRPO** + **ECA** to handle confounding and sparse long-horizon credit.

## 8. Harness Scaling for Generalizable Agentic Reinforcement Learning
- **arXiv**: [2610.29458](https://arxiv.org/abs/2610.29458)
- **Date**: 2026-10-21
- **Authors**: Fei Bai, Huatong Song, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Ji-Rong Wen (IQuest Research; Beihang; RUC)
- **Institution/Company**: IQuest Research / Beihang / Renmin University
- **Categories**: cs.LG, cs.AI, cs.CL

### Abstract
Training through a single fixed harness causes specialization and poor cross-harness transfer. We introduce **Harness Scaling**: train across diverse execution configurations from a factorized harness space. Select compact subset with balanced factorial coverage, organize cross-harness training combining global coverage with controlled variation. Improves generalization to unseen white-box and transfers to unseen black-box harnesses better than training on a single complex black-box harness.

### Key Innovations
- **New scaling dimension**: harness diversity (factorized space + balanced subset + structured training).
- **Cross-harness generalization** to both white-box variants and external black-box harnesses.

## 9. Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems
- **arXiv**: [2610.29292](https://arxiv.org/abs/2610.29292)
- **Date**: 2026-10-21
- **Authors**: Fabian Tritthart, Tom Zehle
- **Institution/Company**: not stated in abstract
- **Categories**: cs.CL, cs.MA

### Abstract
MAS topology (which agents included, how they communicate) is critical; single task score doesn't reveal helpful/harmful agents. **Contrastive Attribution Topology Search (CATS)** searches compact teams in fixed supergraph of specialized agents: LLM attributer compares traces across candidate topologies to assign per-agent credit, updates supergraph edges and prunes weak edges/agents. On BigCodeBench, +5.3pp accuracy over score-only search using 54% fewer deployment tokens; matches strongest baselines on MBPP with fewer tokens. In prompt-poisoning stress test, CATS excludes all adversarial agents in all runs while random search retains some at comparable accuracy.

### Key Innovations
- **Contrastive trace-based attribution** for per-agent credit.
- **Topology search + pruning** for compact, robust teams (poisoning resistance).

## 10. LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces
- **arXiv**: [2610.29408](https://arxiv.org/abs/2610.29408)
- **Date**: 2026-10-21
- **Authors**: Xinyu Wang, Huafeng Shi, Yue Ma, Zijie Meng, Teng Xi, Yuzhuo Chen, Yucheng Wang, Ruicheng Zhang, Guoxin Zhang, Pengfei Wan, Xiu Li, Fangneng Zhan
- **Institution/Company**: Tsinghua University / Kuaishou
- **Categories**: cs.CV

### Abstract
Multi-agent video world modeling: generate joint visual future for multiple controlled agents interpreting heterogeneous controls (binary game buttons → continuous robot commands). Challenges: independent control per agent; heterogeneous control semantics across tasks. **LiveAct** uses **Heterogeneous Action Interface (HAI)**: (1) Agent-Aware Spatial Modulation (language-driven spatial gates + agent-specific attention) binds actions to intended agents, (2) Schema-Guided Action Adaptation describes each control variable in language and modulates with synchronized numerical value. Transferred to blockwise causal generator via teacher forcing + rollout-aware distribution matching for real-time streaming. Evaluated on games and multi-robot manipulation: 0.898/0.942 agent-attribution accuracy without agent locations/identity crops; causal generator 17.70 FPS at 512×448. Project: [liveact-ai.github.io](https://liveact-ai.github.io)

### Key Innovations
- **Multi-agent joint prediction** with heterogeneous controls.
- **HAI** decomposes binding (spatial/agent-aware) from semantics (schema-guided).
- **Real-time causal world model** with strong agent attribution.

## 11. Agentic World Action Models
- **arXiv**: [2610.30136](https://arxiv.org/abs/2610.30136)
- **Date**: 2026-10-21
- **Authors**: Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Renrui Zhang, Roei Herzig, Yutong Bai, Ken Goldberg, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi "Jim" Fan, Trevor Darrell
- **Institution/Company**: UC Berkeley / Stanford / Nvidia / Georgia Tech / etc.
- **Categories**: cs.RO

### Abstract
World action models provide visual foresight but lack compositional skill reuse; agentic robotics uses code-based planning with reusable skills but lacks predictive grounding. **AW-0** jointly models code, future video, robot actions as three coupled streams in unified mixture-of-transformers: code expert generates parameterized skill routines/control logic, video and action experts generate future states/motor commands. Code serves dual role (structure prediction+control, reusable programs). Automated curation labels trajectories with aligned programs and consolidates into reusable skill libraries. Improves over VLA/WAM on RoboTwin 2.0 and bimanual manipulation; better language following/semantic reasoning/robustness. Project: [agentic-wam.github.io](https://agentic-wam.github.io/)

### Key Innovations
- **Unified mixture-of-transformers** for code/video/action.
- **Code as both planner structure and reusable skill library**.
- **Automated program-aligned curation** for skill consolidation.

## 12. TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments
- **arXiv**: [2610.30043](https://arxiv.org/abs/2610.30043)
- **Date**: 2026-10-21
- **Authors**: Yicheng Xu, Zhikai Xu, Ziyuan Chen, Yuhang Dong, Tao Zhang, Zhucun Xue, Yong Liu, Jiangning Zhang
- **Institution/Company**: Zhejiang University
- **Categories**: cs.RO

### Abstract
Robots must act under physical/social constraints and adapt to environmental/human changes. **TARSphere** is full-stack: **TARSphere-Infra** runs policies in physics sim with embodied NPCs and constrained dialogue; event-driven FSM updates task states/evaluates outcomes. **TARSphere-Harness** lets frozen MLLM act via multi-level executable skills with observations/hierarchical memory/execution feedback. **TARSphere-Bench**: 360 episodes across 30 indoor scenes with paired conditions (perceptual robustness, disruption adaptation, task update, human coordination, intent understanding) for navigate-and-report/fetch-and-deliver. Evaluation of 8 MLLMs shows general-purpose can outperform embodied models; task updates/human interaction/collisions remain hard. Project: [xuyicheng-zju.github.io/TARSphere](https://xuyicheng-zju.github.io/TARSphere/), Code: [github.com/xuyicheng-zju/TARSphere](https://github.com/xuyicheng-zju/TARSphere)

### Key Innovations
- **Full-stack** (sim+NPCs+dialogue+FSM+harness+benchmark).
- **Evolving environment evaluation** (disruptions/updates/human coordination).
- **Multi-level executable skills + hierarchical memory** for frozen MLLM agents.

## 13. Rethinking Video Autoencoders for Interactive World Models
- **arXiv**: [2610.30129](https://arxiv.org/abs/2610.30129)
- **Date**: 2026-10-21
- **Authors**: Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour, Patrick Pérez, David Picard
- **Institution/Company**: Kyutai / Google / LIGM
- **Categories**: cs.CV

### Abstract
World models generate in video autoencoder latent space; cost/compression affect latency/wait times. We build **CADRE**, an open family of causal diffusion representation autoencoders across spatio-temporal compressions (small bottleneck on frozen features + diffusion decoder self-distilled to 1/few steps). Train same world model on each in manipulation/navigation (2 envs each). CADRE forms frontier (especially moving camera). Findings: (1) diffusion decoder sharper than perceptual regression at strong compression, (2) temporal compression more effective in autoencoder than world model for manipulation, (3) manipulation/nav need opposite compressions (temporal cheap if camera still, spatial when moving), (4) with still camera coarser spatial tokens hurt motion more than image quality. Code/models/demo: [kyutai.org/blog/2026-10-21-cadre](https://kyutai.org/blog/2026-10-21-cadre)

### Key Innovations
- **Systematic compression study** for interactive world models.
- **CADRE family** (causal diffusion representation autoencoders) with controlled ablations.
- **Pragmatic guidance** on spatial/temporal compression tradeoffs.

## 14. DPT: Diverse Parallel Thinking for Large Language Models via Path Diversity
- **arXiv**: [2610.29501](https://arxiv.org/abs/2610.29501)
- **Date**: 2026-10-21
- **Authors**: Jiaru Qian, Yihong Dong, Xue Jiang, Chun-Wah Hsu, Zhi Jin, Ge Li (Peking University; Shanghai Jiao Tong University; Wuhan University)
- **Institution/Company**: PKU/SJTU/Wuhan
- **Categories**: cs.AI

### Abstract
Parallel thinking via RL often suffers from mode collapse (paths degenerate similar), undermining exploration of multiple hypotheses. **Diverse Parallel Thinking (DPT)** penalizes prefix similarity of parallel trajectories to reward distinct reasoning strategies, encouraging broader exploration. Outperforms previous parallel thinking methods on reasoning benchmarks; validates path diversity is key. Code: [github.com/JiaruQian/DPT](https://github.com/JiaruQian/DPT).

### Key Innovations
- **Prefix-similarity penalty** for path diversity in parallel thinking RL.
- **Mode collapse mitigation** with empirical validation.

## 15. LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data
- **arXiv**: [2610.30132](https://arxiv.org/abs/2610.30132)
- **Date**: 2026-10-21
- **Authors**: Zhennan Wan, Jianfei Chen (Tsinghua University)
- **Institution/Company**: Tsinghua University
- **Categories**: cs.CL, cs.LG

### Abstract
RL for long-context reasoning needs long/diverse/challenging/verifiable data; hard to obtain. **LongZero** lets model improve without external data: synthesize question+answer with supporting evidence in compact structured form, then expand evidence into long multi-document context separately; train with GRPO on self-written multi-hop and multi-round retrieval tasks. Outperforms baselines using externally-synthesized data on two LLMs across five long-context reasoning benchmarks. Code/data: [github.com/zhennan1/LongZero](https://github.com/zhennan1/LongZero)

### Key Innovations
- **RL from zero data** for long-context reasoning (self-synthesis + expansion to long context).
- **Combines multi-hop and multi-round retrieval self-tasks**.

## 16. Flat-RLVR: Sharpness-Aware Reinforcement Learning with Verifiable Rewards for Reasoning Capacity
- **arXiv**: [2610.29281](https://arxiv.org/abs/2610.29281)
- **Date**: 2026-10-21
- **Authors**: Yeonbum Kim, Hyun Kyu Lee, Sung Whan Yoon (UNIST)
- **Institution/Company**: Ulsan National Institute of Science and Technology
- **Categories**: cs.LG, cs.AI

### Abstract
RLVR (GRPO) enhances reasoning but causes **distribution sharpening** (peaked distribution suppresses rare-correct trajectories, reducing diversity). **Flat-RLVR** promotes flat reward optima via sharpness-aware minimization during post-training with GRPO variants, reducing distribution sharpening while maintaining single-attempt accuracy and improving sample diversity.

### Key Innovations
- **Flat optima** in RLVR to counteract sharpening and improve diversity/efficiency tradeoff.

## Also Notable (New/Relevant)

- **TeachBack: Learning to Teach via Bidirectional Preference Optimization for On-Policy Self-Distillation** ([2610.29167](https://arxiv.org/abs/2610.29167), 2026-10-21) — bidirectional preference optimization for on-policy self-distillation (rec+eff lanes).
- **MemoryTax: The Bitter Lesson of Agent Memory** ([2610.29823](https://arxiv.org/abs/2610.29823), 2026-10-21) — agent memory systems often costly patch; strong coding agents can search their own history better/cost-effectively in tested setting.
- **Memory-Centric Continual Learning for AI Agents** ([2610.29357](https://arxiv.org/abs/2610.29357), 2026-10-21) — taxonomy/eval/protocol reframing memory from passive lookup to continual learning.
- **Reasoning-Search-Augmented LLMs: Taxonomy/Benchmark/Controlled Evidence** ([2610.29189](https://arxiv.org/abs/2610.29189), 2026-10-21) — operational taxonomy, benchmark analysis, controlled synthesis across RSA-loop architectures.
- **GSP Autobidding Equilibria with Few Advertisers or Slots** ([2610.29310](https://arxiv.org/abs/2610.29310), 2026-10-21) — exact autobidding equilibria (budget/ROI) polynomial-time when n advertisers or K slots small; relevant to ads/auction theory.
- **Computing the Nucleon of Matching Games** ([2610.29731](https://arxiv.org/abs/2610.29731), 2026-10-21) — polynomial for nonnegative rational weights matching games; NP-hard for unit-weight b-matching/capacity≥3 or partitioned matching width≥3.
- **When Are We Near Nash? Certifying Solutions in General-Sum Games** ([2610.29300](https://arxiv.org/abs/2610.29300), 2026-10-21) — zero-best-response certificate from regret accumulators for extensive-form games.
- **Is Anyone Enforcing the Cartel? RL Teaches LLM Agents in Markets** ([2610.28787](https://arxiv.org/abs/2610.28787), 2026-10-20, new-to-many) — audit shows enforcement (punishment of cheats) differs from collusive outcomes; outcome measures insufficient.
- **Environment Duels: A Microcosm of LLM Co-Evolution** ([2610.30116](https://arxiv.org/abs/2610.30116), 2026-10-21) — solve vs author duality; models shape each other (authoring/solving distinct skills).
- **Scaling in Games: Continued Pre-Training for Embodied Agents in Diverse Virtual Worlds** ([2610.28698](https://arxiv.org/abs/2610.28698), 2026-10-20) — CPT scaling across data/diversity/model size in virtual worlds; competitive with specialists/frontier in 3D.
- **Steering Black-Box LLM Agents with Pitfall Anticipation World Model (PAWM)** ([2610.29139](https://arxiv.org/abs/2610.29139), 2026-10-21) — selectively predicts impending failures to steer black-box agents (+24.3% ScienceWorld, +7.7% WebArena-Lite).
- **ALPS: Visual State Encoders for World Models** ([2610.30120](https://arxiv.org/abs/2610.30120), 2026-10-21) — unified encoder for physical state/language alignment/pixel reconstruction; strong on LIBERO/world-model planning.
- **PhysiCalWorld: In-Context Physics Calibration for World Models** ([2610.30125](https://arxiv.org/abs/2610.30125), 2026-10-21) — calibrate dynamics via exploratory interaction clip encoded as physics descriptor token (no finetune/analytic physics).
- **Multimodal Embodied Agents: Unified Capability-centric Perspective (PAPAV)** ([2610.30108](https://arxiv.org/abs/2610.30108), 2026-10-21) — maps computer-use→robot-use across Perceive/Anticipate/Plan/Act/Verify; notes evaluation gaps.

## Cross-Paper Observations

1. **Long-tail / memorization is a first-class issue for generative recommenders**: CAPE shows shared-prefix generation forgets tails at both retrieval and ranking; LoopRec adapts computation per item (recent/lower-frequency get more). Fine-grained SIDs + progressive training (FineSID) point to content-aware representations as mitigation. This complements the 10-21 report's SID lifecycle concerns (maintenance/topology) with *memorization* and *adaptive compute*.
2. **Agentic RL moves to stateful/data-centric environments**: BIRD-RL solves DB contamination with trajectory-scoped persistence; Uni-Mem does unified memory manager learning; Harness Scaling treats harness diversity as a scaling dimension. All emphasize environment/statefulness and co-adaptation (memory construction+retrieval, harness+policy) rather than pure tool use.
3. **World models become agentic/multi-agent and interactive**: LiveAct (multi-agent heterogeneous controls), AW-0 (code+video+action with reusable skills), TARSphere (full-stack evolving environments), CADRE/ALPS/PhysiCalWorld show systematic work on encoders/compression/physics calibration for real-time interactive use. Focus shifts from single-agent video prediction to compositional skills, social/physical adaptation, and deployment efficiency.
4. **Reasoning efficiency/diversity under RL pressure**: DPT fights mode collapse in parallel thinking; Flat-RLVR fights distribution sharpening in RLVR; LongZero shows zero-data self-improvement for long-context reasoning; MAPS regulates search momentum in RAG. Common theme: RL optimization has side effects (collapse/sharpening/drift) requiring diversity/flatness/structure-aware interventions.
5. **Attribution/topology and robustness in MAS**: CATS uses contrastive attribution to prune harmful/adversarial agents and compress teams; MemoryTax/Memory-Centric CL reframe memory evaluation; Environment Duels reveals solve/author distinctness and co-evolution. Together they push toward principled team design, adversarial robustness, and evaluation of agent capabilities beyond task success.

## Method & Coverage Notes
- **Harvest**: arXiv export API across cs.IR/cs.LG/cs.AI/cs.CL/cs.MA/cs.CV/cs.RO/cs.GT/cs.CY/stat.ML + keyword queries (CTR/advertising/recommendation/generative rec/sequential/LLM+RL/agents/games) → 1149 unique papers; filtered >=2026-10-20 with rec/ads/seq/llm/rl/agent/game focus. New-to-wiki prioritized; 10-20 duplicates (already in 10-21 report) excluded where appropriate.
- **Verification**: Abstracts/authors/affiliations/categories/comments collected from arXiv API/html; institutions marked as stated/inferred; all claims abstract-level.
- **Scope**: Covers recommendation/CTR/RAG, agentic RL/memory/harnesses, multi-agent world models/embodied agents/games, reasoning/distillation/alignment, and relevant theory (auctions/games/mechanism design).
