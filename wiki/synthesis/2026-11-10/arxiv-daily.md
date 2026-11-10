---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-11-10)"
type: synthesis
created: 2026-11-10
updated: 2026-11-10
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, retrieval, quantization, recsys, game-theory]
---

# arXiv Daily Report (2026-11-10)

> **Query time**: 2026-11-10. This report surveys recently submitted/indexed arXiv papers (primarily the 2026-11-06 submission batch visible via the arXiv Export API at query time) across AI, LLMs, recommendation, advertising/CTR-related prediction, sequential modeling, and games/game-theoretic settings.
>
> **Method**: arXiv Export API queries over `cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA` and keyword searches for recommendation, advertising/click-through-rate, sequential recommendation, and games; sorted by `submittedDate` (descending) with title/abstract screening. Abstracts are condensed from arXiv metadata; all results and metrics are **author-reported**. Affiliations are listed when identifiable from arXiv metadata/comments; otherwise marked as not specified in metadata.
>
> **Caveats**: Abstract-level review only (no reproduction). Online/industrial claims are single-paper reports unless noted. Some papers span multiple categories; each is placed in its primary theme below.

## Summary

- **Agentic systems are pushing beyond specialist models.** Apple reports an agentic manipulation policy (AMP1) that outperforms VLA/WAM baselines zero-shot across robot embodiments; NVIDIA proposes executable reasoning caches (CPU-ARC) to reuse solved reasoning traces cheaply.
- **LLM efficiency and adaptation remain active.** Work spans low-precision quantization for reasoning models (CodeQuant2), reliability-aware test-time RL from majority-vote pseudo-labels (PC-Dr.DPO), and experience consolidation into weights via verified admission/release (ENGRAM).
- **Recommendation/retrieval focuses on sparse feedback, controllability, and explainability.** SAGE-PAIR targets 0.05–1.0% feedback regimes with source-pretrained routed residuals; SteerGR enables concept-level steering of generative game recommendation via sparse autoencoders; SPARSEUP improves learned sparse retrieval recipes.
- **Advertising/CTR-adjacent signals emphasize cold-start and simulation design.** A persona-simulation study for cold-start e-commerce ads finds signal form (demographic anchoring, qualitative cues, prompt phrasing) dominates LLM-based CTR estimation quality.
- **Sequential modeling appears in user-behavior and next-item prediction contexts.** Deliberate latent reasoning (DESRec) adapts reasoning depth per user history for sequential recommendation.
- **Games and strategic interaction span social-deduction agents and mechanism design.** Controlled Werewolf-agent experiments probe linguistic effects on trust/actions, while game-theoretic papers tighten regret/algorithms for contextual search and bilateral trade.

---

## A. AI, LLMs, and Agents

### 1. On Agentic Manipulation Policies
- **arXiv**: [2611.09892](https://arxiv.org/abs/2611.09892)
- **Authors**: Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi, Fahad Islam, Xueting Li, Jean-Baptiste Regli, Kejia Ren, Petr Švec, David J. Yoon, Matthias Müller, Vladlen Koltun
- **Institution/Company**: Apple (per project/comment context: Apple AIML Research)
- **Categories**: cs.RO, cs.AI, cs.CV, cs.LG (submitted 2026-11-06)
- **Abstract**: Studies agentic manipulation policies (AMPs), where a generalist AI model directly commands a robot manipulator and adapts actions as tasks unfold, in contrast to specialist policies trained on demonstrations (e.g., VLAs/WAMs). Introduces AMP1, a reference harness that runs across single-arm, bimanual, and mobile manipulation without demonstrations or task-specific training. Reports state-of-the-art results on RoboLab-120 and CaP-Gym, strong zero-shot real-world performance across 12 tasks/3 robot instances, emergent strategies (search, tool use, camera calibration), and experience learning via a persistent memory store that reduces RoboDojo bimanual failure rates.
- **Key innovations**:
  - **AMP1 harness**: unified agentic control loop across diverse manipulation embodiments with no task-specific training.
  - **Zero-shot generalization**: outperforms leading VLA/WAM baselines on benchmarks and real-world trials (author-reported large failure-rate reductions).
  - **Emergent behavior**: agent develops task strategies without hand-coded grasp/place skills.
  - **Cross-episode memory**: persistent memory representation improves bimanual manipulation through experience.
- **arXiv link**: https://arxiv.org/abs/2611.09892

### 2. CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse
- **arXiv**: [2611.09891](https://arxiv.org/abs/2611.09891)
- **Authors**: Peter Belcak, Greg Heinrich, Saurav Muralidharan, Shizhe Diao, Pavlo Molchanov
- **Institution/Company**: NVIDIA (inferred from author affiliations commonly associated with NVIDIA research; not explicitly stated in arXiv metadata fields shown)
- **Categories**: cs.AI (submitted 2026-11-06)
- **Abstract**: Argues that LLMs often recompute solutions instead of reusing prior reasoning. Proposes agentic reasoning caching: construct robust CPU-executable agentic reasoning caches (ARCs) from LLM reasoning traces so that applying a learned solution to new problem instances requires little LLM involvement. Reports near-frontier performance on difficult mathematical/scientific tasks, explainability, continual trainability, robustness to perturbations, and 16–291× lower invocation cost than the source model.
- **Key innovations**:
  - **Agentic reasoning caches (ARCs)**: compile reasoning traces into reusable, CPU-executable procedures.
  - **Separation of solving vs. execution**: reuse prior task solutions on new instances with minimal model calls.
  - **Efficiency/robustness**: large cost reductions with robustness to input perturbations and support for continual updates.
- **arXiv link**: https://arxiv.org/abs/2611.09891

### 3. CodeQuant2: Enhanced Outlier Mitigation and Adaptive Clustering for Low-Precision LRMs
- **arXiv**: [2611.09868](https://arxiv.org/abs/2611.09868)
- **Authors**: Xingyu Liu, Xiangyang Yin, Tianhua Xia, Haiyu Wang, Sai Qian Zhang
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL (submitted 2026-11-06)
- **Abstract**: Targets low-precision quantization for large reasoning models (LRMs), where long reasoning traces increase inference cost but aggressive quantization can hurt reasoning quality. Observes larger activation fluctuations in early decoding steps and proposes CodeQuant2, a clustering-based LUT quantization framework with rotation/scaling outlier mitigation, non-uniform weight representation via clustering, adaptive per-layer codebook sizes, and reasoning-aware calibration sample selection. Reports accuracy improvements on reasoning benchmarks and up to 2.85× speedup over BF16 with a custom LUT CUDA kernel.
- **Key innovations**:
  - **Reasoning-aware calibration**: selects calibration samples reflecting early decoding activation behavior.
  - **Outlier mitigation + clustering LUTs**: rotation/scaling and clustered codebooks for non-uniform weight distributions.
  - **Adaptive codebook sizing**: allocates precision by layer difficulty.
  - **Systems co-design**: custom LUT CUDA kernel for practical speedups.
- **arXiv link**: https://arxiv.org/abs/2611.09868

### 4. On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning
- **arXiv**: [2611.09872](https://arxiv.org/abs/2611.09872)
- **Authors**: Haoyu Wang, Ru Wang, Yuanyuan Wang, Jiaxian Guo, Mingming Gong
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.AI (submitted 2026-11-06)
- **Abstract**: Analyzes test-time reinforcement learning (TTRL) with self-generated majority-vote pseudo-labels for online DPO adaptation. Decomposes pseudo-label error into population-majority bias and prompt-dependent finite-rollout variation; focuses on mitigating the latter. Proposes Prompt-Conditional Distributionally Robust DPO (PC-Dr.DPO), which conditions robust reweighting on observed vote reliability to downweight sampling-sensitive prompts, plus a cache-based mechanism to reduce self-supervised forgetting. Reports matching or outperforming the strongest TTRL baseline in 24/30 settings across six reasoning benchmarks and five backbones.
- **Key innovations**:
  - **Error decomposition** for majority-vote TTRL supervision (bias vs. finite-rollout variation).
  - **PC-Dr.DPO**: reliability-conditioned distributionally robust updates for noisy prompts.
  - **Cache-based anti-forgetting** during online self-supervised adaptation.
- **arXiv link**: https://arxiv.org/abs/2611.09872

### 5. ENGRAM: From Agent Experience to Weights through Verified Consolidation
- **arXiv**: [2611.09472](https://arxiv.org/abs/2611.09472)
- **Authors**: Ruiyi Yang, Zechen Li, Lihuan Li, Du Yin, Hao Xue, Flora D. Salim
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.AI, cs.IR (submitted 2026-11-06)
- **Abstract**: Addresses how to consolidate agent experience from external retrieval into model weights. Introduces ENGRAM, which separates training admission from memory release: a demonstration-aware gate admits skills based on student mastery or sufficient teacher demonstrations; learning uses action traces with context from an Engram Trace Graph (ETG); a verification gate compares the updated model without episodic retrieval against the base model with retrieval before release. Reports gains over frozen-weight ETG controls, reduced retrievable footprint with near-retain-all performance, and improved task performance with lower input-token usage/model calls.
- **Key innovations**:
  - **Admission/release separation**: distinct gates for what to train on and when external records can be removed.
  - **ETG-conditioned learning**: train from selected action traces with structured experience context.
  - **Verified release**: retain retrievable guidance for skills failing verification, enabling selective archival.
- **arXiv link**: https://arxiv.org/abs/2611.09472

---

## B. Recommendation, Retrieval, and Sequential Modeling

### 6. SAGE-PAIR: Source-Pretrained Routed Residual Adaptation for Sparse-Feedback Recommendation
- **arXiv**: [2611.09728](https://arxiv.org/abs/2611.09728)
- **Authors**: Weiqing Zeng, Zida Yang, Guquan You, Jiexin Zheng, Cong Wang
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-06)
- **Abstract**: Studies recommendation adaptation in new serving windows with extremely sparse feedback (0.05–1.0%). Instead of estimating target-specific updates directly, SAGE-PAIR transfers a source-supported residual correction space pretrained on an adjacent source period and adds a soft router over residual experts conditioned on source user profiles; target feedback calibrates this residual state. On KuaiSAR-v2, reports NDCG@10 improvements over source/pretrained baselines, with routed experts adding gains beyond global residual adaptation and millisecond-scale adaptation/inference costs.
- **Key innovations**:
  - **Source-pretrained residual correction space** for identifiable sparse-feedback adaptation.
  - **Soft-routed residual experts** conditioned on user profiles for differentiated corrections.
  - **Calibrate-not-relearn** paradigm: target labels tune residual state rather than full recommender updates.
- **arXiv link**: https://arxiv.org/abs/2611.09728

### 7. SPARSEUP: Towards Better Recipes for Training Modern Learned Sparse Retrievers
- **arXiv**: [2611.09680](https://arxiv.org/abs/2611.09680)
- **Authors**: Thibault Formal, Pierre Erbacher, Cosimo Rulli
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-06)
- **Abstract**: Presents a training recipe for SPLADE-like learned sparse encoders on modern backbones/data to improve efficiency-effectiveness trade-offs. Analyzes logit distribution effects on stability/sparsity, introduces per-position fan-out control (hard cap on vocabulary dimensions emitted per position), and applies vocabulary merging to remove redundant cased/BPE variants. Applying the recipe to the LateOn backbone yields SPARSEUP, reporting 56.4 average nDCG@10 on BEIR-13 among public vocabulary-based sparse encoders below 150M parameters (as claimed).
- **Key innovations**:
  - **Training-stability recipe** via logit-distribution analysis for sparse encoders.
  - **Per-position fan-out cap** to control sparsity/activation behavior.
  - **Vocabulary merging** to reduce redundant token variants in modern BPE vocabularies.
- **arXiv link**: https://arxiv.org/abs/2611.09680

### 8. SteerGR: Steering Generative Recommendation via Sparse Autoencoders for Controllable Game Discovery
- **arXiv**: [2611.08790](https://arxiv.org/abs/2611.08790)
- **Authors**: Sunkyung Lee, Xiaokai Wei, Da Long, Hyunsik Jeon, Jiajun Wu, Rithwik Seth, Jongwuk Lee, Michelle Gong, Gungor Polatkan
- **Institution/Company**: Not specified in arXiv metadata (includes industry-scale generative recommendation setting per abstract)
- **Categories**: cs.IR, cs.AI, cs.CL (submitted 2026-11-05)
- **Abstract**: Proposes SteerGR, a framework for concept-level controllability in generative recommendation (applied to game discovery). Uses sparse autoencoders (SAEs) to connect human-readable play concepts to internal features: (1) concept definition/grounding with an LLM, (2) feature discovery/selection by concept association and steering effect, and (3) sparse feature intervention to amplify/suppress features without retraining. Experiments on two industrial generative recommendation models over a real-world game dataset show steering toward/away from target concepts.
- **Key innovations**:
  - **SAE-based controllable generative recsys**: interpretable feature interventions without retraining.
  - **Concept-to-feature pipeline**: LLM-grounded concepts linked to effective internal SAE features.
  - **Industrial validation**: demonstrated on two production-scale generative recommenders for game discovery.
- **arXiv link**: https://arxiv.org/abs/2611.08790

### 9. Deliberate Latent Reasoning for Sequential Recommendation
- **arXiv**: [2611.06521](https://arxiv.org/abs/2611.06521)
- **Authors**: Haobo Zhang, Qiannan Zhu, Yutao Zhu, Zhicheng Dou
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-04)
- **Abstract**: Addresses fixed-depth latent reasoning in sequential recommenders, which can over-/under-think depending on user history complexity. Proposes DESRec, a deliberate latent reasoning framework with personalized reasoning-step selection during training and self-distillation to compress the most informative reasoning state into the final step for inference. Also introduces progressive preference extraction that segments histories into variable-length periods summarized as latent milestones, enabling personalized reasoning over evolving interests. Reports improvements over eight baselines across six datasets and four backbone recommenders.
- **Key innovations**:
  - **Personalized reasoning depth**: selects optimal latent reasoning steps per user sequence.
  - **Self-distilled reasoning state**: compresses best intermediate state into final representation.
  - **Progressive preference milestones**: variable-period summarization for evolving user interests.
- **arXiv link**: https://arxiv.org/abs/2611.06521

---

## C. Advertising and CTR-Related Modeling

### 10. What Matters for LLM Persona Simulation: Signal Form in Cold-Start E-Commerce Advertising
- **arXiv**: [2611.08840](https://arxiv.org/abs/2611.08840)
- **Authors**: Jiwoo Choi, In Ik Lee, Woo Sung Seo, Minho Lee, Yun Young Choi
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.LG, cs.AI (submitted 2026-11-06; accepted at GenAIECommerce'26 workshop co-located with RecSys 2026)
- **Abstract**: Investigates LLM-based persona simulation for estimating advertising performance in cold-start e-commerce campaigns without historical logs, using real Google Ads data across five demographic segments. Identifies three signal-form factors affecting simulation quality: (i) demographic anchor without noisy rich attributes, (ii) relative qualitative banner-blindness signals rather than quantitative anchors, and (iii) prompt phrasing. Reports MAE 24.9 / MAPE 26.1%, substantially better than tested non-LLM baselines and LLM configurations using explicit CTR anchors; ablations show minimal demographics and qualitative cues outperform richer/quantitative setups.
- **Key innovations**:
  - **Signal-form analysis** for LLM persona simulation in cold-start ad/CTR estimation.
  - **Empirical finding**: minimal demographic anchoring and qualitative cues beat richer personas and quantitative anchors.
  - **Practical guidance**: prompt phrasing materially impacts simulated response quality.
- **arXiv link**: https://arxiv.org/abs/2611.08840

---

## D. Games and Strategic Interaction

### 11. Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents
- **arXiv**: [2611.09768](https://arxiv.org/abs/2611.09768)
- **Authors**: Yuchen Li, Lisa Liu, Runqi Zou, Shuxuan Kuang, Qingquan Zhang, Julian Togelius
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.AI (submitted 2026-11-06)
- **Abstract**: Tests whether linguistic range and politeness strategies affect judgments/actions in LLM-agent social-deduction play using the LURK Werewolf framework. Rewrites only utterance realization while preserving speech-act/game content and replays game days from checkpoints against resampled controls. Across 30 games and 4,335 replays, finds no significant changes in trust and no vote/night-action effects surviving multiple-comparison correction; largest uncorrected effect is ~4 percentage-point vote shift when moving range away from neutral paraphrase. Also observes predominantly bald on-record face-threatening speech in natural play.
- **Key innovations**:
  - **Controlled causal replay design** separating speech-act content from linguistic realization in multi-agent games.
  - **Negative-result evidence**: linguistic style/politeness has limited measurable impact on trust and strategic actions in this setting.
  - **Large replay scale** (4,335 replays) for fine-grained social-deduction behavior analysis.
- **arXiv link**: https://arxiv.org/abs/2611.09768

### 12. Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games
- **arXiv**: [2611.09271](https://arxiv.org/abs/2611.09271)
- **Authors**: Eduardo C. Garrido-Merchán
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.AI (submitted 2026-11-06)
- **Abstract**: Explores zero-shot weight-space programming by LLMs: hand-setting all feed-forward network weights from specifications (no gradient descent/training data). Evaluates across a difficulty ladder of two-player games (Nim, tic-tac-toe, Connect Four variants, chess endgame) with independent replicate networks per rung. Reports six networks with complete non-statistical correctness proofs; chess-endgame networks are exact for cheap local properties (legality, some one-ply mates) but collapse in multi-move adversarial planning. Concludes remaining gaps reflect architectural/plan-composition limits rather than mere engineering effort in tested settings.
- **Key innovations**:
  - **Difficulty-graded game ladder** for evaluating weight-space programming capability.
  - **Proof-backed exactness where tractable**: verified correctness for several constructed networks/tasks.
  - **Characterization of failure mode**: strong local correctness but breakdown in long-horizon adversarial composition.
- **arXiv link**: https://arxiv.org/abs/2611.09271

### 13. Contextual Search and Bilateral Trade with a Trace-Square-Root Potential
- **arXiv**: [2611.09615](https://arxiv.org/abs/2611.09615)
- **Authors**: Romain Cosson, Federico Fusco, Anupam Gupta, Stefano Leonardi, Renato Paes Leme, Matteo Russo
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.GT, cs.LG (submitted 2026-11-06)
- **Abstract**: Presents a unified potential method for contextual search and bilateral trade with one-bit feedback. In a Bayesian setting, derives bounds using a trace-square-root potential (e.g., $O(\mathrm{Tr}\sqrt{\Sigma})$ for contextual search; analogous terms for bilateral trade). Adapts the method to adversarial worst-case settings over the unit Euclidean ball, obtaining tight $O(\sqrt{d})$-regret algorithms for both problems, improving prior guarantees and matching known lower bounds up to constants.
- **Key innovations**:
  - **Unified trace-square-root potential** framework spanning contextual search and bilateral trade.
  - **Order-tight adversarial algorithms**: $O(\sqrt{d})$ regret with one-bit feedback.
  - **Bayesian-to-worst-case transfer** of potential-based analysis ideas.
- **arXiv link**: https://arxiv.org/abs/2611.09615

### 14. Optimal Regret for Profit Maximization in Bilateral Trade
- **arXiv**: [2611.09558](https://arxiv.org/abs/2611.09558)
- **Authors**: Matteo Castiglioni, Anna Lunghi, Alberto Marchesi
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.GT, cs.LG (submitted 2026-11-06)
- **Abstract**: Studies repeated bilateral trade where an intermediary posts buy/sell prices to a seller and buyer with unknown joint valuation distribution and observes only whether trade occurs. Designs an algorithm achieving $\widetilde{\mathcal{O}}(T^{2/3})$ regret against the best fixed price pair, matching (up to logs) the classical one-dimensional dynamic pricing lower bound. Shows that learning both sides of the market is no harder in regret terms than learning one side in this setting.
- **Key innovations**:
  - **Near-optimal regret** for two-sided bilateral-trade pricing under bandit feedback.
  - **Dimensionality insight**: preserves one-dimensional $\widetilde{\mathcal{O}}(T^{2/3})$ rate despite learning both buyer and seller sides.
- **arXiv link**: https://arxiv.org/abs/2611.09558

---

## Notes

- **Institution coverage**: Some arXiv API records do not expose structured affiliations in the feed fields used here. Where not explicit, this report avoids guessing and marks them as not specified in metadata (except clear project/comment indications).
- **Category overlap**: Advertising, recommendation, sequential modeling, and CTR prediction intersect heavily; papers were grouped by primary emphasis while still reflecting cross-cutting relevance (e.g., sequential recommendation, game discovery steering, cold-start ad simulation).
- **Next pass (optional)**: For stricter affiliation completeness, fetch each paper's PDF/HTML author block and add confirmed institutions/companies.
