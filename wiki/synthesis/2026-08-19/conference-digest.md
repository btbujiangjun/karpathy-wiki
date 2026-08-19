---
title: "Conference & arXiv Daily Digest — 2026-08-19"
type: synthesis
created: 2026-08-19
updated: 2026-08-19
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, acl-2026, cvpr-2026, emnlp-2025, sigir-2026, recsys-2026, recommendation, llm, advertising, ctr, agent-systems, code-execution, generative-models, sequential-modeling, benchmarks]
---

# Conference & arXiv Daily Digest — 2026-08-19

> Comprehensive survey of recent papers from top ML/AI conferences (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, SIGIR 2026, RecSys 2026, WWW 2026, EMNLP 2025, CIKM 2025) and general recent arXiv preprints on AI/LLMs, recommendation systems, advertising, CTR prediction, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks.

---

## 📊 ICML 2026 (Seoul, Jul 6–11, 2026)

> 6,634 papers accepted (26.6% acceptance rate). 168 Oral, 406 Spotlight.

### Recommendation & CTR Prediction

#### 1. UniAR: Unified Multimodal Autoregressive Modeling with Shared Context
- **Authors:** Wujian Peng, et al.
- **Affiliation:** Alibaba / ICML 2026
- **Venue:** ICML 2026
- **Problem:** Existing multimodal approaches rely on separate representations for understanding and generation, creating alignment gaps.
- **Innovation:** Visual tokenizer serves as shared representation for both understanding and generation, enabling truly unified autoregressive modeling.
- **Key Result:** Direct interpretation of generated visual tokens through shared context.
- **arXiv:** [Link in proceedings]

### Code Execution & Reasoning

#### 2. StepCodeReasoner: Aligning Code Reasoning with Stepwise Execution Traces via RL
- **Authors:** Hao Wang, Rui Li, Lei Sha, Jie M. Zhang
- **Affiliation:** - (arXiv: 2605.11922)
- **Venue:** ICML 2026 Poster
- **Problem:** Existing code reasoning methods supervise only final outputs, ignoring intermediate states → reward hacking.
- **Innovation:** Introduces Bi-Level GRPO RL algorithm for structured credit assignment at inter-trajectory and intra-trajectory levels. Automatic insertion of structured print-based execution-trace anchors.
- **Key Result:** 7B model achieves 91.1% on CRUXEval and 86.5% on LiveCodeBench, outperforming CodeReasoner-7B (86.0%, 77.7%) and GPT-4o (85.6%, 75.1%). On REval benchmark: 82.9% vs CodeReasoner-7B 72.3% and GPT-4o 77.3%.
- **Comparison:** Beat CodeReasoner-7B baseline and GPT-4o across all benchmarks.

#### 3. One Tool Is Enough: RL of LLM Agents for Repository-Level Code Navigation
- **Authors:** Zhaoxi Zhang, et al.
- **Affiliation:** - (arXiv: -)
- **Venue:** ICML 2026 Poster
- **Problem:** LLM-based methods treat code navigation as retrieval task, rely on multiple auxiliary tools, overlook execution logic.
- **Innovation:** RepoNavigator — single execution-aware tool (jump to definition of invoked symbol). Trained end-to-end via RL from base pretrained model, no closed-source distillation.
- **Key Result:** 7B outperforms 14B baselines, 14B surpasses 32B, 32B exceeds GPT-5 on most metrics.
- **Comparison:** SOTA on repository-level issue localization.

#### 4. Scaling Agentic Verifier for Competitive Coding
- **Authors:** -
- **Affiliation:** - (ICML 2026)
- **Venue:** ICML 2026 Poster
- **Problem:** LLMs struggle to solve competitive programming correctly in a single attempt. Execution-based re-ranking limited by difficult test case generation.
- **Innovation:** Agentic Verifier — active agent reasoning about program behaviors, searching for discriminative test inputs via multi-turn interaction with code execution environments. Trained via data synthesis + rejection fine-tuning + agentic RL.
- **Key Result:** Up to +10–15% absolute gains in Best@k accuracy across 5 competitive programming benchmarks.

### Agent Systems

#### 5. VeRO: An Evaluation Harness for Agents to Optimize Agents
- **Authors:** Scale API team (ICML 2026 Poster)
- **Affiliation:** Scale AI (arXiv: 2602.22480)
- **Venue:** ICML 2026
- **Problem:** No standardized benchmark for coding agents optimizing other agents via edit–execute–evaluate cycles.
- **Innovation:** VeRO provides versioned snapshots, budget-controlled evaluation, structured execution traces. VeRO-Bench: benchmark suite of target agents + tasks.
- **Key Result:** Claude Sonnet 4.5 as optimizer yields 7–15% gains on tool-heavy agents. Without VeRO guardrails, optimizers cheat. Full VeRO harness yields 8% average improvement over Claude Code Pure.
- **Comparison:** VeRO-enabled Claude Opus 4.6 ranks #1 on TerminalBench-2.

#### 6. Meta-Harness: Post-Training Reliable Agent Systems via Harness Search
- **Authors:** Yoonho Lee, Roshen S Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
- **Affiliation:** Stanford / -
- **Venue:** ICML 2026 Workshop (Agents in the Wild)
- **Problem:** Agent trustworthiness depends not only on model weights but on surrounding harness code.
- **Innovation:** Searches over agent-systems layer using execution traces from prior candidates, not compressed summaries.
- **Key Result:** On TerminalBench-2, discovered harness surpasses Terminus-KIRA on Claude Opus 4.6, ranks #1 among Claude Haiku 4.5 agents. On retrieval-augmented math: +4.7 points on 200 IMO-level problems.

#### 7. Automata from Agent Traces: Failure and Next-Step Prediction
- **Authors:** Seonglae Cho, et al.
- **Affiliation:** -
- **Venue:** ICML 2026 Workshop (Agents in the Wild)
- **Problem:** LLM agent behavior traces are opaque, resist safety auditing and runtime monitoring.
- **Innovation:** Collapses trace corpus into a provably minimal finite-state machine (FSM). Compact 7–43 states, replay at ≥0.997 fitness.
- **Key Result:** FSM-state context outperforms Agent Workflow Memory on next-step prediction. Per-state behavioral features reach held-out AUROC up to 0.94 for failure prediction.

### LLM Training & Optimization

#### 8. You Can Learn Tokenization End-to-End with Reinforcement Learning
- **Authors:** Sam Dauncey, Roger Wattenhofer
- **Venue:** ICML 2026
- **Problem:** Prior methods use heuristics or straight-through estimates for token boundaries.
- **Innovation:** Score function estimates for learning token boundaries — tighter theoretical guarantees by directly optimizing discrete token boundaries.
- **arXiv:** [Link in proceedings]

---

## 🏆 NeurIPS 2025 (San Diego, Dec 2025)

> 4 Best Papers: Artificial Hivemind, Gated Attention, 1000-Layer RL, Why Diffusion Don't Memorize.

### Recommendation Systems

#### 9. R²ec: Towards Large Recommender Models with Reasoning
- **Authors:** Yongqi Li et al.
- **Affiliation:** - (arXiv: proceedings.neurips.cc 2025)
- **Venue:** NeurIPS 2025
- **Problem:** Large recommender models extend LLMs but lack intrinsic reasoning. Existing approaches use separate reasoning modules, causing resource cost and optimization disconnect.
- **Innovation:** Dual-head architecture: (1) language-modeling head for reasoning, (2) recommendation head for item prediction via shared semantic embedding space. RecPO RL framework with fused reward mechanism.
- **Key Result:** Significantly outperforms traditional, LLM-based, and reasoning-augmented baselines on 3 datasets. Cross-domain robustness across Electronics, MovieLens, GoodReads. Scaling to Gemma-9B yields 21.7% higher NDCG@5.
- **Code:** https://github.com/YRYangang/RRec

#### 10. IGD: Token Decisiveness Modeling via Information Gain in LLMs for Recommendation
- **Authors:** - (NeurIPS 2025)
- **Venue:** NeurIPS 2025
- **Problem:** LLM4Rec treats all item tokens equally; >50% of tokens have zero Information Gain but high logits, biasing optimization.
- **Innovation:** Frames item generation as decision process; defines token decisiveness via Information Gain. IGD downweights zero-IG tokens during tuning, rebalances decoding toward high-IG tokens.
- **Key Result:** Average gains of 18.89% HR@10 and 20.15% NDCG@10 over strong baselines across 4 datasets with 2 LLM backbones (BIGRec and D3).

#### 11. Can LLMs Outshine Conventional Recommenders? (RecBench)
- **Authors:** Qijiong Liu, Jieming Zhu, Lu Fan, Kun Wang, Hengchang Hu, Wei Guo, Yong Liu, Xiao-Ming Wu
- **Venue:** NeurIPS 2025 Datasets & Benchmarks Track
- **Problem:** Need comprehensive benchmark comparing LLM-as-RS with conventional recommenders.
- **Innovation:** Evaluates 17 LLMs across 5 datasets (fashion, news, video, books, music) with 4 item representation forms, CTR + sequential recommendation tasks.
- **Key Result:** LLM-based recommenders achieve up to 5% AUC improvement in CTR and 170% NDCG@10 improvement in SeqRec. Best conventional recommender retains 95% of performance while operating thousands of times faster.

#### 12. Counterfactual Implicit Feedback Modeling (Counter-IF)
- **Authors:** -
- **Venue:** NeurIPS 2025
- **Problem:** Implicit feedback has PU (positive-unlabeled) and MNAR (missing not at random) challenges.
- **Innovation:** First to formalize relevance prediction as counterfactual estimation with missing treatment variables. Stratifies user-item pairs into 4 groups (DP, HE, HU, UN). Causal representation learning combining pointwise + pairwise loss.
- **Key Result:** Significantly outperforms SOTA methods on Yahoo and Coat datasets.

#### 13. Think before Recommendation: RecZero (Autonomous Reasoning-enhanced Recommender)
- **Authors:** -
- **Venue:** NeurIPS 2025
- **Problem:** Distillation-based reasoning methods suffer from teacher model limitations, costly supervision, superficial transfer.
- **Innovation:** RecZero trains a single LLM through pure RL (GRPO) to autonomously develop reasoning for rating prediction. "Think-before-Recommendation" prompt + rule-based reward.
- **Key Result:** Significantly outperforms baselines on multiple benchmark datasets.

#### 14. ORBIT: Open Recommendation Benchmark with Hidden Tests
- **Authors:** -
- **Venue:** NeurIPS 2025 Datasets & Benchmarks Track
- **Problem:** Existing datasets fail to capture realistic user behaviors, inconsistent evaluation settings.
- **Innovation:** ClueWeb-Reco: 87 million public webpages, real browsing sequences (privacy-preserving). LLM-QueryGen baseline uses LLM-generated queries for retrieval.
- **Key Result:** Traditional models struggle on large candidate pool; LLM-QueryGen with DeepSeek achieves highest Recall@10.

#### 15. AgentRecBench: Benchmarking LLM Agent-based Recommender Systems
- **Authors:** Tsinghua University team
- **Venue:** NeurIPS 2025 Datasets & Benchmarks Track
- **Problem:** No standardized evaluation for agentic recommender systems.
- **Innovation:** Interactive textual recommendation simulator with 3 scenarios (classic, evolving interest, cold-start). Unified modular framework. First benchmark comparing 10+ classical and agentic methods.
- **Key Result:** AgentSociety Challenge attracted 295 teams, 1400+ submissions; 20.3% improvement in Recommendation Track.

#### 16. Who You Are Matters: TagCF (LLM-Enhanced Logical Recommendation)
- **Authors:** -
- **Venue:** NeurIPS 2025
- **Problem:** Mainstream approaches neglect user characteristics and social roles as logical confounders.
- **Innovation:** Uses MLLM (M3) to extract user role tags + item topic tags; LLM (Qwen2.5-7B) to infer U2I/I2U logic graphs. Online experiments in industrial environment.
- **Key Result:** User role modeling outperforms item topic modeling; logic graphs are transferable across recommendation tasks.

#### 17. Listwise Preference Diffusion Optimization (LPDO) for User Behavior Trajectories
- **Authors:** -
- **Venue:** NeurIPS 2025
- **Problem:** Existing methods cannot capture global listwise dependencies for multi-step behavior prediction.
- **Innovation:** LPDO integrates Plackett–Luce ranking signal into diffusion ELBO. SeqMatch metric for trajectory-level evaluation.
- **Key Result:** Consistent improvement on 4 benchmark datasets, substantially outperforming DiffuRec and DCRec baselines.

### Code & Benchmarking

#### 18. Gated Attention (NeurIPS 2025 Best Paper)
- **Authors:** Qwen / Alibaba team
- **Venue:** NeurIPS 2025 Best Paper
- **Innovation:** Novel gated attention mechanism with significant theoretical and empirical contributions.
- **arXiv:** [Key paper in attention mechanisms]

---

## 🧠 ICLR 2026 (Rio de Janeiro, Apr 23–27, 2026)

> Outstanding Papers: "Transformers are Inherently Succinct", "LLMs Get Lost in Multi-Turn"

### Code Execution & Reasoning

#### 19. R1-Code-Interpreter: LLMs Reason with Code via SFT and Multi-stage RL
- **Authors:** Yongchao98 et al.
- **Venue:** ICLR 2026 Poster
- **Problem:** No guidance on training LLMs to use Code Interpreter across diverse tasks.
- **Innovation:** Multi-turn SFT + RL training on 144 diverse reasoning/planning tasks. Multi-stage curriculum learning partitions by improvement potential.
- **Key Result:** R1-CI-14B improves accuracy from 44.1% to 72.4% on 37 test tasks, outperforming GPT-4o (58.6%) and GPT-4o + Code Interpreter (70.9%). Emergent self-checking behavior through code generation.

#### 20. LoongRL: Reinforcement Learning for Advanced Reasoning over Long Contexts
- **Authors:** -
- **Venue:** ICLR 2026 Oral
- **Problem:** Long-context reasoning needs advanced thinking patterns; high-difficulty RL data scarce.
- **Innovation:** KeyChain synthesis transforms short multi-hop QA into long-context tasks by inserting UUID chains. Emergent plan–retrieve–reason–recheck pattern.
- **Key Result:** Trained at 16K effectively solves 128K tasks. On Qwen2.5-7B/14B: +23.5%/+21.1% absolute gains on multi-hop QA. LoongRL-14B reaches 74.2 score, rivaling o3-mini (74.5) and DeepSeek-R1 (74.9).

#### 21. Markovian Transformers for Informative Language Modeling
- **Authors:** -
- **Venue:** ICLR 2026 Poster
- **Problem:** CoT reasoning often fails to faithfully reflect underlying decision process.
- **Innovation:** Autoencoder-style reasoning bottleneck: all information must pass through bounded-length CoT. GRPO training with parallel sampling.
- **Key Result:** GSM8K: 19.6% → 57.1%; ARC-Challenge: 36.1% → 79.9%. Learned CoTs generalize across architectures.

### Agent Systems & Optimization

#### 22. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
- **Authors:** -
- **Venue:** ICLR 2026 Oral
- **Problem:** GRPO requires thousands of rollouts for new tasks.
- **Innovation:** Genetic-Pareto prompt optimizer with natural language reflection. Samples trajectories, reflects in language, proposes/test updates, combines Pareto frontier lessons.
- **Key Result:** Outperforms GRPO by 6pp avg (up to 19pp) using up to 35× fewer rollouts. Outperforms MIPROv2 by >10pp (e.g., +12pp on AIME-2025).

#### 23. Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs
- **Authors:** -
- **Venue:** ICLR 2026 Poster
- **Problem:** RL-trained models often lose diversity (mode-seeking reverse KL).
- **Innovation:** α-divergence family to approximate filtered target distribution, controlling precision–diversity trade-off.
- **Key Result:** State-of-the-art on Lean theorem-proving, outperforming all prior methods on the coverage axis.

### LLM Inference Efficiency

#### 24. Global Resolution: Optimal Multi-Draft Speculative Sampling
- **Authors:** -
- **Venue:** ICLR 2026 Oral
- **Problem:** Optimal transport in multi-draft speculative sampling is exponentially large.
- **Innovation:** Reverse engineering subset selection → max-flow problem → convex optimization with polymatroid theory. Reduces to V variables.
- **Key Result:** First multi-draft algorithm with 90% acceptance and <100ms overhead per token.

---

## 🌟 AAAI 2026 (Singapore, Jan 20–27, 2026)

> ~4,167 accepted papers from ~29,000 submissions.

### Recommendation & CTR

#### 25. LO-FAR: Cost-Aware Local Filter for Sparse Feature Ranking in Industrial Ad Recommendation
- **Authors:** - (RecSys 2026 / arXiv: 2607.20873)
- **Venue:** RecSys 2026 (published at AAAI venue context)
- **Problem:** Sparse ID-list features dominate storage/training/serving cost; need cost-aware feature selection.
- **Innovation:** CPU-only, model-agnostic workflow ranking features by stand-alone held-out predictive signal with lightweight local estimators. ~2 CPU-hours for full ranking.
- **Key Result:** NE gains competitive with shuffle-based importance and BSN on production dataset (>1M interactions, 475 features). 40–75% reduction in sparse embedding storage. Cost: <$100 vs >$4,000 for GPU methods.

### AI Safety & Alignment

#### 26. AURA: Affordance-Understanding and Risk-aware Alignment Technique for LLMs
- **Venue:** AAAI 2026 Special Track on AI Alignment
- **Focus:** LLM safety alignment with affordance understanding.

### Benchmarking

#### 27. ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation
- **Venue:** AAAI 2026
- **Focus:** Hallucination detection in long-context financial/environmental reports.

---

## 🎨 CVPR 2026 (Denver, Jun 3–7, 2026)

> Best Paper: D4RT (Google DeepMind 4D reconstruction)

### Generative Models & Diffusion

#### 28. Transition Models (TiM): Rethinking the Generative Learning Objective
- **Authors:** - (CVPR 2026 Highlight)
- **Venue:** CVPR 2026 Highlighted Paper
- **Problem:** Diffusion models need many steps; few-step alternatives have quality ceiling.
- **Innovation:** Exact continuous-time dynamics equation for state transitions across any finite interval Δt. TiM adapts to arbitrary-step transitions.
- **Key Result:** 865M parameters surpasses SD3.5 (8B) and FLUX.1 (12B) across all step counts. Native-resolution: 4096×4096.

#### 29. HierDiff: Learning by Analogy for Compositional Generalization
- **Authors:** Lingjing Kong, et al.
- **Venue:** CVPR 2026
- **Problem:** Compositional generalization requires decomposing high-level concepts into recombable low-level ones.
- **Innovation:** Causal framework using hierarchical data-generating process with sparse interactions. Hierarchical concept injection with sparsity control.
- **Key Result:** Outperforms baselines on DPG-Bench across all 5 metrics.

---

## 📈 KDD 2026 (Jeju Island, Aug 9–13, 2026)

### Recommendation & CTR Prediction

#### 30. TransX: Scaling Transformer-based Recommendation via Behavioral and Serving Stream Crossings
- **Authors:** LinkedIn team
- **Venue:** KDD 2026
- **Problem:** Collapsing heterogeneous data sources into single monolithic token stream obscures distinct causal roles.
- **Innovation:** Encoder-decoder architecture reformulating recommendation as sequence-to-sequence action transduction. Decouples behavior-stream from serving-event modeling. Amortized serving with KV caching.
- **Key Result:** +6.0% CTR lift, +4.4% conversion gain on LinkedIn's largest social recommendation application. Online computation reduced ~80%.

#### 31. GRAB: Generative Ranking for Ads at Baidu (LLM-Inspired CTR)
- **Authors:** Baidu team
- **Venue:** KDD 2026
- **Problem:** Traditional DLRMs face performance/efficiency bottlenecks.
- **Innovation:** End-to-end generative framework for CTR with Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics. Monotonic scaling with longer sequences.
- **Key Result:** 3.05% increase in revenue and 3.49% increase in CTR in online A/B testing at Baidu home feed.

#### 32. RoleMix: Unified Interaction Architecture for Post-Click CTR Prediction
- **Authors:** Tencent team (KDD Cup 2026)
- **Venue:** KDD 2026 (KDD Cup 2026 Tencent UniRec Challenge)
- **Problem:** Structural mismatch between sparse unordered features and long behavior histories.
- **Innovation:** Role-preserving semantic token interface: non-sequential fields → 16 semantic tokens preserving roles; long behavior → hierarchical window attention. UniMixing-Lite backbone.
- **Key Result:** 83.648% online AUC on KDD Cup 2026 Tencent UniRec Challenge, outperforming baseline by 1.953%.

#### 33. IDProxy: Cold-Start CTR Prediction with Multimodal LLMs
- **Authors:** Xiaohongshu/RedNote team
- **Venue:** KDD 2026 (under review)
- **Problem:** CTR models rely on item ID embeddings, struggle with cold-start.
- **Innovation:** MLLM generates proxy embeddings from multimodal content signals. Explicitly aligned with existing ID embedding space, end-to-end optimized.
- **Key Result:** Deployed in both Content Feed (+0.22% time spent, +0.5% engagements) and Display Ads (+1.28% impression, +1.93% ADVV, +1.73% CTR) at Xiaohongshu (300M+ MAU).

#### 34. Modular Representation Compression (MARC) for LLM-Enhanced Recommendation
- **Authors:** Yunjia Xi, et al. (Alibaba)
- **Venue:** KDD 2026
- **Problem:** Mid-layer representations outperform final layers (MRA phenomenon); existing compression methods suboptimal.
- **Innovation:** Modular Adjustment introduces compression + task adaptation modules. Modular Task Decoupling via information constraints.
- **Key Result:** 2.82% eCPM lift in online A/B test in large-scale commercial search advertising.

#### 35. Enhancing CTR Prediction with De-correlated Expert Networks (D-MoE)
- **Authors:** Tencent team
- **Venue:** arXiv preprint (2605.17925), targeted for conference submission
- **Problem:** MoE expert de-correlation strategies unclear in effectiveness.
- **Innovation:** Cross-Expert De-Correlation loss directly minimizing expert correlations. Progressive combination of de-correlation strategies.
- **Key Result:** 1.19% GMV lift on Tencent's advertising platforms in online A/B testing.

---

## 📚 ACL 2026 (San Diego, Jul 2026)

> Best Paper: Imperfective Paradox (NII/Tokyo)

### Code Execution & Reasoning

#### 36. ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning
- **Authors:** Lingxiao Tang, He Ye, et al.
- **Affiliation:** - (ACL 2026 Long Paper, pp. 13850–13875)
- **Venue:** ACL 2026
- **Problem:** Code LLMs struggle with code execution reasoning; SFT cannot verify intermediate steps.
- **Innovation:** Verifiable white-box rewards from execution traces (next-statement + variable value/type prediction). Constraint-based program synthesis for multi-difficulty datasets. Two-stage training: enhance execution reasoning → transfer to code generation.
- **Key Result:** 7B model achieves performance comparable to 32B models on code reasoning benchmarks; +5.9% pass@1 on code generation.

### Recommendation

#### 37. What Makes LLMs Effective Sequential Recommenders? (RecPO)
- **Authors:** Zhongyu Ouyang, et al.
- **Venue:** ACL 2026 Long Paper
- **Problem:** Binary pairwise comparisons overlook preference intensity and temporal context.
- **Innovation:** RecPO maps both explicit/implicit feedback to common preference signal; adaptive reward margins accounting for intensity + recency.
- **Key Result:** Consistently outperforms SOTA on 5 datasets; behavioral patterns aligned with human decision-making.

### Generative Models

#### 38. ControlAudio: Text-Guided, Timing-Indicated Audio Generation via Progressive Diffusion
- **Authors:** Yuxuan Jiang, et al. (Tsinghua)
- **Venue:** ACL 2026 Long Paper
- **Problem:** Data scarcity limits fine-grained controllability in text-to-audio.
- **Innovation:** Progressive diffusion modeling: pretrain DiT on text-audio pairs → incrementally add timing + phoneme features. Progressively guided generation aligns with coarse-to-fine sampling.
- **Key Result:** SOTA temporal accuracy and speech clarity.

### LLM Reasoning & Optimization

#### 39. SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks
- **Authors:** Tianyi Wang, et al.
- **Venue:** ACL 2026 Long Paper
- **Problem:** Token-level PPO unstable for long CoT horizons; GRPO requires multiple samples limiting throughput.
- **Innovation:** Reformulates as Sequence-Level Contextual Bandit. Decoupled scalar value function for low-variance advantage signals without multi-sampling.
- **Key Result:** Significantly surpasses standard PPO, matches computation-heavy group-based methods.

#### 40. Toward Consistent World Models with Multi-Token Prediction and Latent Semantic Enhancement
- **Authors:** Qimin Zhong, et al.
- **Venue:** ACL 2026 Long Paper
- **Problem:** Multi-Token Prediction promotes convergence toward belief states but often suffers from structural hallucinations.
- **Innovation:** LSE-MTP anchors predictions to ground-truth hidden state trajectories via latent semantic enhancement.
- **Key Result:** Reduces structural hallucinations, enhances representation alignment.

---

## 🔍 SIGIR 2026 (Melbourne, Jul 20–24, 2026)

### Recommendation Systems

#### 41. GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors:** JD.com team
- **Venue:** SIGIR 2026
- **Problem:** Scaling generative retrieval to industrial systems faces pagination ambiguity, long-sequence cost, preference alignment.
- **Innovation:** Page-wise NTP task supervises over entire interaction pages. Asymmetric linear Token Merger compresses multi-token SIDs. GRPO-SR: RL with NLL regularization + Hybrid Rewards (dense model + relevance gate).
- **Key Result:** Deployed at JD.com: 9.5% improvement in click count, 8.7% in transaction count in month-long online A/B tests. Long-tail items: +10% exposure, +16% clicks, +13% transactions.

---

## 🎯 RecSys 2026 (Minneapolis, Sep 27–Oct 2, 2026)

### Industrial Recommendation

#### 42. LO-FAR (see entry #25 above)
- Published at RecSys 2026.

---

## 🌐 WWW 2026

### Recommendation

#### 43. ThinkRec: Thinking-based LLM Recommendation
- **Venue:** WWW 2026
- **Key Innovation:** Thinking-based approach to LLM recommendation.

#### 44. GenCI: Generative CTR via Cohort Intent Learning
- **Venue:** WWW 2026
- **arXiv:** 2601.18251
- **Key Innovation:** Generative CTR paradigm using cohort-level intent signals.

#### 45. SparseCTR: Sparse Attention Long-Term CTR
- **Venue:** WWW 2026
- **arXiv:** 2601.17836
- **Key Innovation:** Sparse attention mechanism for efficient long-term behavior modeling.

---

## 🎮 General Recent Papers

### Agent Systems & Multi-Agent

#### 46. VeRO (entry #5 above) — Agent optimization harness
#### 47. Meta-Harness (entry #6 above) — Post-training agent systems
#### 48. Automata from Agent Traces (entry #7 above) — FSM for agent monitoring

### Games & Strategic Reasoning

#### 49._alive: Interactive Frontend Games via RL (Alibaba, ICML 2026)
- **Affiliation:** Alibaba
- **Venue:** ICML 2026
- **Innovation:** RL for interactive frontend game development.

### Sequential Modeling

#### 50. Markovian Transformers (entry #21 above) — Reasoning bottleneck framework

### Benchmarks

#### 51. ORBIT (entry #14 above) — Open Recommendation Benchmark
#### 52. AgentRecBench (entry #15 above) — LLM Agent-based Recommender Systems
#### 53. RecBench (entry #11 above) — LLM vs Conventional Recommenders

---

## 📊 Cross-Conference Themes

### 1. Reasoning + Recommendation
A major convergence across NeurIPS, ICML, and ACL: reasoning enhances recommendation quality. R²ec, RecZero, RecPO, and TagCF all demonstrate that LLM reasoning capabilities transfer to recommendation tasks.

### 2. RL Post-Training for Code & Agents
ICML 2026 and ICLR 2026 feature extensive RL work for code reasoning (StepCodeReasoner, R1-Code-Interpreter, ExecVerify) and agent systems (VeRO, Meta-Harness). GRPO variants dominate.

### 3. Generative Recommendation at Scale
KDD and SIGIR showcase industrial deployment of generative recommendation: GRAB (Baidu +3.49% CTR), GenRec (JD.com +9.5% clicks), TransX (LinkedIn +6.0% CTR). Semantic IDs + decoder-only architectures become standard.

### 4. CTR Prediction Scaling Laws
Industrial CTR papers continue exploring scaling: D-MoE (Tencent), GRAB (Baidu), RoleMix (Tencent), IDProxy (Xiaohongshu), MARC (Alibaba). Mix-of-experts and hierarchical attention dominate.

### 5. Agent Safety & Evaluation
Multiple papers address agent reliability: Automata from Traces (FSM monitoring), VeRO (agent optimization guardrails), Meta-Harness (post-training reliability).

### 6. Diffusion as First-Class
CVPR 2026 highlights Transition Models (TiM), while ICML features diffusion approaches. The gap between diffusion and autoregressive models continues to narrow.

---

## 🏢 Industry Impact Summary

| Company | Paper | Impact |
|---------|-------|--------|
| **LinkedIn** | TransX | +6.0% CTR, +4.4% conversion |
| **JD.com** | GenRec | +9.5% clicks, +8.7% transactions |
| **Baidu** | GRAB | +3.49% CTR, +3.05% revenue |
| **Tencent** | D-MoE | +1.19% GMV; RoleMix: 1.953% AUC lift |
| **Xiaohongshu** | IDProxy | +1.28% impressions, +1.73% CTR (ads) |
| **Alibaba** | MARC | +2.82% eCPM in search ads |

---

*Generated: 2026-08-19 | Sources: ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, SIGIR 2026, RecSys 2026, WWW 2026, arXiv*
