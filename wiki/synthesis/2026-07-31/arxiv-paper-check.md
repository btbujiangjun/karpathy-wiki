---
title: "arXiv Paper Check — AI & CTR (July 31, 2026)"
type: synthesis
created: 2026-07-31
updated: 2026-07-31
tags: [arxiv, ai, ctr, recommendation, agents, reasoning, rl, llm]
sources: []
---

# arXiv Paper Check — AI & CTR (July 31, 2026)

> Curated from arXiv submissions announced Jul 30–31, 2026 (cs.AI, cs.LG, cs.IR, via arXiv RSS/API). This report focuses on papers **not** featured in the [arXiv Daily Digest](../2026-07-31/arxiv-daily.md) and is weighted toward AI methodology and CTR / recommendation / search.

---

## Reinforcement Learning & LLM Post-Training

### 1. Weak-to-Strong On-Policy Distillation (W2S-OPD)
- **Authors**: Fangxu Yu, Zinan Lin, Xiaodong Liu, Weijia Xu, Michael Xu, Tianyi Zhou, Jianfeng Gao
- **Key Contribution**: Standard on-policy distillation (OPD) assumes a teacher at least as capable as the student — impossible at the frontier, where no larger teacher exists. W2S-OPD inverts this: it improves a **strong** student by distilling from multiple **weak** models. A proxy teacher is constructed in logit space from a contrast pair (positive − negative model), both smaller and cheaper than the student. Turns cheap weak models into a directional training signal.
- **Link**: https://arxiv.org/abs/2607.26246

### 2. Meta-Learned Reward Shaping for RLHF (MeRLa)
- **Authors**: Yunpeng Chu
- **Key Contribution**: Argues static, task-agnostic reward models are the bottleneck in RLHF. MeRLa meta-learns a task-aware shaping function Φ(x,y;φ) across auxiliary tasks before RLHF training, producing a composite reward that preserves policy optimality while densifying the learning signal. Includes theoretical guarantees for policy invariance and formal analysis of incentive compatibility and representation-drift sensitivity.
- **Link**: https://arxiv.org/abs/2607.26094

### 3. Probing the Origins of Reasoning Performance: Representational Quality for Math in RL vs. SFT
- **Authors**: Antyabha Rahman, Akshaj Gurugubelli, Omar Ankit, Kevin Zhu, Aishwarya Balwani
- **Key Contribution**: Mechanistic analysis of *why* RL fine-tuning beats SFT on math reasoning. Two converging lines of evidence: (1) linear probes on layer-wise hidden states predict answer correctness more accurately for RL models, indicating more linearly separable, structured representations; (2) mean-ablation studies show RL models develop a hierarchical architecture where deeper layers become progressively more critical, whereas SFT distributes importance uniformly across layers.
- **Link**: https://arxiv.org/abs/2607.26119

### 4. Collaborative Weighting with Pessimistic Critic (CWAC)
- **Authors**: Gong Gao, Xiao Lai, Ziqi Xie, Guojie Chen, Xianhui Liu, Weidong Zhao
- **Key Contribution**: Off-policy RL for continuous control suffers from overestimation bias propagated through TD bootstrapping. Existing fixes overemphasize high-uncertainty transitions, amplifying bias. CWAC is a unified actor-critic framework with collaborative weighting (down-weighting high-uncertainty/bootstrapping-heavy transitions) plus a pessimistic critic, addressing both the data-coverage and error-propagation failure modes.
- **Link**: https://arxiv.org/abs/2607.26509

### 5. Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models
- **Authors**: Anton de la Fuente, Arthur Conmy
- **Key Contribution**: Treats SFT lessons as transferable across three usually-separate research areas. Two concrete ports: (1) "Teaching Claude Why" — training on the *reason* for a behavior generalizes better than training on examples of the behavior alone (ported from alignment into toy models); (2) capability preservation via SFT on another model's outputs (ported from model organisms into the Model-Spec Midtraining setting).
- **Link**: https://arxiv.org/abs/2607.26173

### 6. Constitutional Midtraining: Content Presence Drives Alignment Gains
- **Authors**: Desiree Cho, Cameron Tice, Bernie Hogan, Hunar Batra, Puria Radmard, Jun Zhao, Nigel Shadbolt
- **Key Contribution**: Tests whether alignment can be made durable by inserting values-based content at **midtraining** (120B scale, 394M-token constitutional corpus from Anthropic's Constitution) cleanly isolated from post-training. 2×2 design (curriculum ordering × deliberative reasoning) yields four conditions + control, evaluated post-midtraining, post-SFT, and post-benign fine-tuning. Finds that *content presence* (not curriculum or reasoning variant) drives alignment gains — a strong negative-ish result on the value of delicate recipe design.
- **Link**: https://arxiv.org/abs/2607.26654

---

## Agents & Multi-Agent Systems

### 7. Can AI Agents Conduct Open-Ended AI Research? Shadow Evaluations
- **Authors**: Peter Kirgis, Sayash Kapoor, Andrew Schwartz, Stephan Rabanser, ... Arvind Narayanan (Princeton, 20+ authors)
- **Key Contribution**: Proposes **shadow evaluations** as a third way to measure AI R&D automation: give an agent the central open-ended research question of a high-quality unpublished paper, and let the paper's *original authors* grade the output. Ran on two unpublished NeurIPS 2026 submissions with frontier agents (6 days, thousands of dollars of compute). Agents completed all the engineering without human help — direct early evidence on whether agents can do open-ended research.
- **Link**: https://arxiv.org/abs/2607.27191

### 8. One Run Is Not an Idea: The Implementation Lottery in Automated Research
- **Authors**: Jingjie Ning, Shanshan Zhong, Xiaochuan Li, Ji Zeng, Chenyan Xiong
- **Key Contribution**: Automated research systems credit experimental scores to *ideas*, but one run scores one sampled *implementation* — the "implementation lottery." Introduces the **Idea Reliability Audit**: freeze candidate idea cards, sample fresh-session implementations, label fidelity outcome-blindly, and rerun saved artifacts. Reports idea-level ICC and leave-one-implementation-out (LOO) winner reversal to quantify how much an idea-level conclusion depends on which implementation was sampled.
- **Link**: https://arxiv.org/abs/2607.26587

### 9. Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLMs
- **Authors**: Huixiang Zhang, Mahzabeen Emu
- **Key Contribution**: Latent communication between LLM agents transmits continuous representations, but end-task performance can't show whether the receiver actually uses task-relevant information. Provides a **causal audit** with controlled message replacements at the sender→receiver boundary, yielding five measurements: encoded sender information, receiver sensitivity to message presence/identity, task value of example-specific content, and value supplied by a separate agent.
- **Link**: https://arxiv.org/abs/2607.26773

### 10. Even More Deception: Objective Misalignment in Mixed-Motive LLM Multi-Agent Systems
- **Authors**: Marylou Fauchard, Florian Carichon, Margarida Carvalho, Golnoosh Farnadi
- **Key Contribution**: Framework for evaluating objective misalignment in mixed-motive MAS using Werewolf: modifies the objective of a single agent while preserving its assigned role, across 4 model families/sizes, 4 player roles, 3 objective formulations. Dual analysis of internal reasoning vs. public cheap-talk (costless, non-binding communication), plus game-outcome analysis — measures how a single misaligned agent shifts collective outcomes.
- **Link**: https://arxiv.org/abs/2607.26120

### 11. Misalignment Has a Personality: A Big Five Account of Emergent Misalignment
- **Authors**: Hasibur Rahman, Smit Desai
- **Key Contribution**: Fine-tuning on a narrow flaw (insecure code, wrong math) causes broad misalignment; this work gives an interpretable account — misalignment behaves like a **shift in personality**. Extracts Big Five personality vectors via a graded, three-level intervention (validated on two open-weight models, Cohen's d up to 6.2). Vectors are linearly ordered, transfer zero-shot and trait-specifically to an independent corpus, with strongest effects in a middle-layer band.
- **Link**: https://arxiv.org/abs/2607.26389

### 12. SkillBoost: Constrained Exploration-Exploitation for Self-Evolving Skills
- **Authors**: Hongqiang Lin, Chao Liu, Xiaofan Bai, Xuan Jin, Yuhong Li, Nenggan Zheng, Xipeng Cao
- **Key Contribution**: Treats agent skills as trainable states but finds data-driven skill optimization overfits limited real-environment trajectories: over-exploitation overfits the current batch, unconstrained exploration regresses previously solved cases. SkillBoost is a three-stage framework (structured exploitation localizes failures to editable skill components; constrained search governs the exploration-exploitation trade-off) to mitigate both risks.
- **Link**: https://arxiv.org/abs/2607.26643

### 13. The User Asks, Platforms Compete: How Agentic Recommendation Markets Take Shape
- **Authors**: Deyao Hong, Kehan Zheng, Qian Li, Jun Zhang, Jie Jiang, Hongning Wang
- **Key Contribution**: New recommendation setting where a user agent specifies a need *before* choosing a platform, so platforms compete for attention — an **agentic recommendation market**. Controlled LLM experiments across three product domains show a tension between access and attention: user-centric recommendation greatly expands which relevant items enter comparison, but broader participation does not translate into effective exposure, and competition triggers platforms' strategic play.
- **Link**: https://arxiv.org/abs/2607.25253

---

## Evaluation, Benchmarks & LLM Behavior

### 14. Position: Evaluation Scores Are Perishable Knowledge Claims
- **Authors**: Sankalp Gilda, Shlok Gilda
- **Key Contribution**: Identifies **trust inflation in evaluation**: when automated metrics, LLM-as-judge ratings, human assessments, and benchmarks are averaged together, evaluation confidence can exceed the reliability of the weakest signal. Argues evaluation scores are epistemic claims with three properties — formality, scope, and **validity windows** (results expire as contamination accumulates and distributions shift). Draws on chain-of-thought analysis, possibilistic logic, and algebraic theory.
- **Link**: https://arxiv.org/abs/2607.26191

### 15. When Benchmark Inferences Do Not Compose: Projectibility in AI Evaluation
- **Authors**: Brett Reynolds
- **Key Contribution**: Beyond validity-centered "evidence per claim," shows warranted links don't automatically make a warranted chain: the target of one study may not be the source of the next, system/population/outcome/conditions may change at the interface, and shared data/model lineage makes apparently independent support dependent. Reintroduces Goodman's **projectibility** (whether a bounded extension from observed to unobserved cases is warranted) as the core concern.
- **Link**: https://arxiv.org/abs/2607.26159

### 16. When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses
- **Authors**: Zihan Chen, Di Zhu, Lei Nico Zheng
- **Key Contribution**: Packages when LLM-as-synthetic-user substitution fails into an evaluation framework, run across four models (8B→frontier, two families) on two real datasets (General Social Survey, World Values Survey). Two failures replicate across all domains/models/families, and models are benchmarked against non-LLM baselines fit on held-out human data — cautionary evidence for LLM-simulated user research.
- **Link**: https://arxiv.org/abs/2607.26348

### 17. RAFS: A Reference-Free Score for Detecting Silent Reasoning Failures
- **Authors**: Vivek Shukla, Varun Shukla, Atul, Divya Mishra, Mehul Kumar Das
- **Key Contribution**: Notes a **reasoning-answer consistency gap**: reference-based CoT evaluation conflates a correct conclusion with a valid derivation (invalid chains can accidentally reach the right answer; valid calculations can carry transcription errors). RAFS is a reference-free, instance-level diagnostic combining step validity, reasoning→answer entailment, counterfactual sensitivity, answer consensus, and conditional reasoning stability.
- **Link**: https://arxiv.org/abs/2607.26102

### 18. Cognitive Convergence: Deep Similarities Between LLMs and Human Cognition
- **Authors**: Chandra Sripada, Richard Lewis
- **Key Contribution**: Position paper pushing back on the "alien intelligences" framing: despite different substrate, learning history, and environments, LLMs converge with human cognition on five principles of cognitive organization — inferential organization, computational architecture, representational structure, prediction-driven learning, and RL-like learning. Argues similarities are structural, not anthropomorphic projection.
- **Link**: https://arxiv.org/abs/2607.26179

### 19. The Easy Trap: Why LLMs Underestimate Misconception-Driven Difficulty
- **Authors**: Amanda La Hadi, Muhammad Johan Alibasa, Guanliang Chen, A. Taufiq Asyhari
- **Key Contribution**: Four LLM systems rated 32 arithmetic items (N=640 ratings) vs. empirical difficulty from 770 Indonesian undergraduates (CTT + 2PL IRT). Moderate rank correlation (Spearman ρ = 0.52–0.70) but substantial systematic bias: LLMs underestimate misconception-driven difficulty — relevant for AI-generated educational assessment.
- **Link**: https://arxiv.org/abs/2607.26067

### 20. Try Again, Don't Look Back: Blind Resampling Outperforms Self-Repair in Small Code Models
- **Authors**: Yuvraj Verma
- **Key Contribution**: Argues self-repair evaluation confounds the value of feedback with the value of the extra attempt. Placebo-controlled MBPP+ study at 1.5B/3B/7B scales with four matched-budget retry conditions: blind resampling, a content-free failure notice, genuine execution feedback, and feedback + verbal self-reflection. Blind resampling is the strongest condition below 7B and statistically tied at 7B, consuming 2.5–5.5× fewer tokens — feedback is largely wasted on small code models.
- **Link**: https://arxiv.org/abs/2607.26117

---

## CTR Prediction & Recommendation

### 21. ASARL: Autonomous Social-Aware Relevance Learning for QQ Search
- **Authors**: Tao Su, Jinjing Hu, Xiao Wang, Xingzhong Cao, Hui Wang (Tencent)
- **Key Contribution**: Social search queries are informal and community-specific, limiting general LLM relevance models. ASARL is a fully automated pipeline: a collaborative agent system (ReasonAgent generates interpretable social-attribute-grounded relevance labels, CriticAgent validates logical consistency, GenAgent augments long-tail data) feeding staged model training — a multi-agent data-curation route to relevance learning, distinct from hand-labeled social search datasets.
- **Link**: https://arxiv.org/abs/2607.26593

### 22. DIRECTOR: Dynamic Index-based Recommendation with Transport-Optimized Retrieval
- **Authors**: Yuanhao Pu, Chenghao Zhang, Chao Feng, Xiang Li, Defu Lian
- **Key Contribution**: Reranking as combinatorial slate selection. Autoregressive generative rerankers capture inter-position dependencies but their prefix-based search prematurely prunes globally promising permutations and is sequential-latency-bound; non-autoregressive variants are efficient but position-parallel factorization under-coordinates positions. DIRECTOR proposes a dynamic index-based formulation with transport-optimized retrieval to bridge the search-space × latency trade-off.
- **Link**: https://arxiv.org/abs/2607.26418

### 23. PSG: Pair-Space Generation for Efficient Generative Reranking
- **Authors**: Chao Feng, Li Ma, Xiancheng Gao, Chenghao Zhang, Yuanhao Pu, Xiang Li
- **Key Contribution**: Targets Generator-Evaluator (G-E) list-wise reranking, where autoregressive generators suffer O(list length) complexity growth and teacher-forcing train-test mismatch (cumulative errors). **Pair-Space Generation (PSG)** elevates the generation atom from individual items to ordered item pairs over a pair vocabulary of size n(n−1), cutting the sequence dimension and improving exploration under latency budgets.
- **Link**: https://arxiv.org/abs/2607.26427

### 24. Embedding Items at Scale: GNN-Based vs. ID-Based Item Embeddings in the Yandex Ecosystem
- **Authors**: Sergei Makeev, Artem Matveev, Vladimir Baikalov, Kirill Khrylchenko
- **Key Contribution**: First large-scale industrial comparison of pretrained graph-neural-network item embeddings vs. end-to-end trainable (ID) embeddings for transformer sequential recommenders. Case study across two mature production systems (Yandex Market, Yandex Music) plus a public low-resource dataset (Yandex Lavka logs, data and code released) — evidence on the cost/quality trade-off of embedding strategy.
- **Link**: https://arxiv.org/abs/2607.26365

### 25. NMKFR: Neural Memory Kalman Fusion Recommender for Time-Aware Cold-Start
- **Authors**: Chengzhi Liu, Ning Zeng, Zehui Qu
- **Key Contribution**: Item cold-start when the recommendation environment changes over time. NMKFR combines a Titans-style memory-based semantic encoder with time-aware Kalman state tracking: the semantic branch extracts memory-enhanced item observations from text; the temporal branch estimates latent states under irregular interaction intervals; posterior covariance is used as an uncertainty signal to calibrate semantic-memory retrieval and static-temporal fusion. Evaluated on Amazon Video Games and MovieLens-32M.
- **Link**: https://arxiv.org/abs/2607.26429

### 26. UniVA: Unified Value Alignment for Generative Recommendation in Online Advertising at Tencent
- **Authors**: Xinxun Zhang, Yuling Xiong, Yangru Huang, Jiale Zhou, Zhengkai Guo, ... Jiawei Jiang, Jie Jiang (Tencent, v2)
- **Key Contribution**: Extends generative recommendation (next-token generation over Semantic IDs) to **advertising**, where high generation likelihood ≠ high ad utility. High-value ads are poorly distinguished in SID space, pruned during decoding, or missed when request-invalid branches consume beam capacity. UniVA is a unified value-alignment framework aligning generation likelihood with advertising value at decode time.
- **Link**: https://arxiv.org/abs/2605.05803

### 27. Reproducibility in Recommender Systems: A Survey
- **Authors**: Alan Said, Alejandro Bellogin
- **Key Contribution**: Structured analysis of the ACM RecSys Reproducibility Track (2020–2025), 51 accepted papers, classifying contributions by type and analyzing datasets, algorithms, frameworks, and evaluation practices. Finds the track expanded from reproduction/replication to benchmarking, resources, and — relevant to this wiki's CTR scaling theme — reproducible evaluation infrastructure.
- **Link**: https://arxiv.org/abs/2607.26074

---

## Key Themes

1. **Automated AI research is being empirically probed**: Shadow evaluations (author-graded open-ended research) and the implementation lottery (one run ≠ one idea) both challenge how we measure AI R&D automation.
2. **Evaluation validity is getting its own theory**: Perishable evaluation scores (validity windows), projectibility (warranted chains, not just warranted links), and synthetic-user failure modes all ask *when* benchmark evidence transfers.
3. **RL post-training gains weak teachers**: W2S-OPD distills strong models from cheap weak contrast pairs; MeRLa meta-learns reward shaping; RL-vs-SFT representational analysis shows deeper-layer hierarchy differences.
4. **Emergent misalignment is increasingly interpretable**: Big Five personality shifts and single-agent objective misalignment in mixed-motive games give measurable handles on a previously diffuse phenomenon.
5. **CTR/rec continues its generative & search-side push**: PSG (pair-space generation) and DIRECTOR attack the autoregressive-reranking latency/search-space trade-off; UniVA aligns generative recommendation with advertising value; Yandex provides an industrial verdict on GNN vs. ID item embeddings.
6. **Small models confound intuition**: Blind resampling beats self-repair on small code models, and LLM-simulated users fail consistently below frontier scale — scaling matters for both.

---

*Cross-references: [arXiv Daily Digest — 2026-07-31](../2026-07-31/arxiv-daily.md) (headline LLM/CTR/rec papers), [arXiv Paper Check — 2026-07-30](../2026-07-30/arxiv-paper-check.md), [arXiv AI Research Scan — 2026-07-30](../2026-07-30/arxiv-ai-search.md).*
