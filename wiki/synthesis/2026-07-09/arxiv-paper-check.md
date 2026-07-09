---
title: arXiv Paper Check — AI & CTR (July 9, 2026)
type: synthesis
created: 2026-07-09
updated: 2026-07-09
tags: [arxiv, paper-check, ai, ctr, llm, rl, recommendation]
---

# arXiv Paper Check — AI & CTR (July 9, 2026)

Scanned cs.AI (95 new), cs.LG (110 new), cs.IR (4 new), cs.CL (34 new) from Thursday July 8, 2026 listings. Highlights below.

---

## AI / LLM Highlights

### 1. Co-LMLM: Continuous-Query Limited Memory Language Models
- **Authors:** Yair Feldman, Linxi Zhao, Nathan Godey, Dongyoung Go, Yilun Hua, Kilian Q. Weinberger, Jennifer J. Sun, Yoav Artzi
- **Abstract:** Proposes continuous-query LMLM where KB pairs continuous keys with textual knowledge values, departing from relational KB reliance. Generates flexible vector queries while integrating attributable retrieved knowledge. At 360M scale, achieves lower perplexity than models pretrained on 40× more data, with SimpleQA performance in line with gpt-4o-mini and higher than Claude Sonnet 4.5.
- **Key Innovation:** Continuous-vector knowledge base queries for LMLMs, removing the Wikipedia restriction with free-form factual span annotation pipeline.
- **Link:** https://arxiv.org/abs/2607.07707

### 2. Max Out GRPO Signal: Adaptive Trace Prefix Control (AdaPrefix-GRPO)
- **Authors:** Vladislav Beliaev
- **Abstract:** GRPO stalls on hardest problems where no rollout succeeds — group advantages vanish and no gradient flows. AdaPrefix-GRPO prepends a correct prefix of a reference solution, then adaptively adjusts prefix length as a feedback controller to keep success rate near 50% (max gradient signal). At matched FLOPs, 2.1× GRPO accuracy on held-out hard math (0.6B), 1.6× on Qwen3-1.7B, 1.7× on AIME, with ~half trace length.
- **Key Innovation:** Adaptive curriculum on solution prefix length as a training-time difficulty controller that retires assistance at deployment.
- **Link:** https://arxiv.org/abs/2607.07674

### 3. RL Post-Training Builds Compositional Reasoning Strategies
- **Authors:** Azwar Abdulsalam, Nishil Patel, Andrew Saxe
- **Abstract:** Studies whether RL composes primitive skills into higher-level strategies in a controllable rewrite-grammar environment. RL solves held-out problems unsolvable by pretrained model even with larger sampling budgets. Trace analysis reveals phased compositional mechanism: strengthens primitive reductions → discovers sequential/parallel compositions → consolidates into stable repertoire. Key difference from RFT: not exploration volume but selectivity (RL concentrates on valid structure).
- **Key Innovation:** Controlled experiment proving RL post-training composes primitive competencies into novel higher-level reasoning strategies through selective exploration.
- **Link:** https://arxiv.org/abs/2607.07646

### 4. Recursive Self-Improvement in AI: Taxonomy and Limits
- **Authors:** Mingguang Chen, Licheng Wang, Bo Qu
- **Abstract:** Surveys 1,250 arXiv papers (2024–2026) along two axes: what the system improves (behavior→policy→evaluator→research process) and degree of loop closure. Separates bounded self-refinement (convergent, evaluable, industrial practice) from open-ended RSI (bounded by grounding, collapse dynamics, compute). Introduces verification hierarchy from formal verifiers (strongest) to intrinsic self-assessment (weakest); demonstrated improvement tracks this hierarchy.
- **Key Innovation:** Comprehensive taxonomy with verification hierarchy linking self-improvement strength to signal quality, identifying research direction-setting as the bottleneck keeping humans in the loop.
- **Link:** https://arxiv.org/abs/2607.07663

### 5. Selective Timestep Weighting and Advantage-Based Replay for Diffusion RLHF
- **Authors:** Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
- **Abstract:** Two complementary strategies for sample-efficient diffusion RLHF. Per-timestep weighting reweights denoising steps during PPO (theoretically connected to optimal convergence). Advantage-based replay prioritizes informative trajectories, reusing past samples instead of querying new rewards. Achieves up to 6× sample efficiency improvement over diffusion RLHF baselines under identical hyperparameters.
- **Key Innovation:** Identifies that reward information is unevenly distributed across denoising timesteps and trajectories, then exploits this for 6× feedback efficiency gain.
- **Link:** https://arxiv.org/abs/2607.07693

### 6. Future Confidence Distillation in Large Language Models
- **Authors:** Sahil Kale
- **Abstract:** Investigates confidence from a temporal perspective — compares pre-solution Feeling-of-Knowing vs post-solution Judgement-of-Learning. Post-solution confidence is better calibrated. Linear probes on hidden representations recover richer confidence info than models verbalize. Introduces future confidence distillation: predictors on pre-solution hidden states trained with post-solution correctness probes. Recovers much of the improvement while needing only pre-solution representations.
- **Key Innovation:** Demonstrates confidence-related information can be anticipated before answer generation completes, enabling low-cost reliable confidence estimation via distillation.
- **Link:** https://arxiv.org/abs/2607.07626

### 7. PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning
- **Authors:** Yazdan Jamshidi, Alexey Shvets
- **Abstract:** Adjusts per-layer sparsity based on 99th percentile of activation magnitudes, bounded to ±5% around target ratio. On LLaMA-2-7B at 50% sparsity: 10.96 perplexity vs 12.92 for uniform Wanda (p < 0.001). Architecture-dependent: LLaMA-3-8B marginal, Mistral-7B none. Finds gradient-based allocation worse than random, suggesting gradient magnitude doesn't predict impact of discrete weight removal.
- **Key Innovation:** Simple activation-percentile-based sparsity allocation that beats uniform Wanda significantly on LLaMA-2, with negative result for gradient-based methods.
- **Link:** https://arxiv.org/abs/2607.07557

### 8. Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity Familiarity
- **Authors:** Grzegorz Brzezinka
- **Abstract:** Probes whether activations betray entity familiarity before any answer token. Two unsupervised dispersion measures (inverse participation ratio, spectral entropy) over post-SwiGLU MLP activations separate known from fabricated entities at AUROC 0.95–1.00 across four Polish Bielik models (1.5B–11B). Entity familiarity signal is at ceiling at 1.5B, but behavioral factual reliability scales sharply with model size. Models almost never abstain (2 refusals / 2520 answers).
- **Key Innovation:** Entity familiarity and factual reliability are distinct phenomena on different scaling curves — internal awareness does not translate to abstention or correctness.
- **Link:** https://arxiv.org/abs/2607.07670

### 9. STRACE: Structural Trajectory Analysis for Agent Optimization
- **Authors:** Ying Chang, Jiahang Xu, Xuan Feng, Chenyuan Yang, Peng Cheng, Yuqing Yang
- **Abstract:** Addresses signal-noise dilemma in long-horizon agent optimization. At batch level, mines failure patterns to filter redundant traces. Within each trace, performs causal localization over textual dependency graph to identify root-cause module. On VeruSAGE-Bench, delivers 1.4× success-rate improvement (42.5% → 58.5%) for human-expert designed agents.
- **Key Innovation:** Causal localization over textual dependency graphs for precise agent optimization contexts, eliminating both inter-trace redundancy and intra-trace noise.
- **Link:** https://arxiv.org/abs/2607.07702

### 10. SciReasoner: Deep Native Structural Reasoning Across Sciences
- **Authors:** Chen Tang et al. (multi-institution, ~30 authors)
- **Abstract:** Multimodal scientific foundation model for structural reasoning across proteins, small molecules, inorganic crystals. Discretizes coordinates/topologies/periodic connectivities into unified structure-aware vocabulary. SOTA on 67/86 benchmarks. Improves Gene Ontology Fmax 0.42→0.55, retrosynthesis accuracy 0.63→0.72. Human evaluation: preferred or comparable to frontier LLM in 98% of cases.
- **Key Innovation:** Unified structure-aware vocabulary treating structural tokens as addressable evidence units, enabling interpretable scientific reasoning across biology, chemistry, and materials science.
- **Link:** https://arxiv.org/abs/2607.07708

### 11. Think Big, Search Small: Role-Factorized Hierarchical Search Agents
- **Authors:** Qinnan Cai, Yibo Zhao, Xiang Li
- **Abstract:** Factorizes hierarchical search into delegation (task decomposition) and execution (retrieval/evidence) roles. Capacity sensitivity is asymmetric: scaling delegation improves EM by ~11 points, scaling execution only ~2.6 points. A 1.7B executor trained via trajectory distillation matches frontier sub-agent with 37% fewer tokens. Role factorization consistently outperforms single-agent baseline (+4.5–8.6 EM).
- **Key Innovation:** Identifies task decomposition as the capability bottleneck in multi-agent search, enabling Pareto-optimal capacity distribution.
- **Link:** https://arxiv.org/abs/2607.07548

### 12. DeLS-Spec: Decoupled Long-Short Contexts for Parallel Speculative Drafting
- **Authors:** Hong-Kai Zheng, Piji Li
- **Abstract:** Decouples long-context (DFlash backbone) and short-context (lightweight local head) for speculative decoding. Local head trains independently with standard NTP objective — no joint training needed. At inference, combines long + short context logits. Consistently improves speedup and average acceptance length over DFlash across math/code/dialogue benchmarks on Qwen3.
- **Key Innovation:** Modular speculative drafting where a lightweight locally-trained head can be plugged into any DFlash backbone without retraining the full model.
- **Link:** https://arxiv.org/abs/2607.07409

### 13. Institutional Red-Teaming: Deployment Rules Causally Shape Multi-Agent AI Safety
- **Authors:** Yujiao Chen
- **Abstract:** Introduces institutional red-teaming: hold agents/objectives fixed, vary only deployment rules. IABench-CA benchmark (228 contexts, 5 rules, 7 model populations, 33,924 games). Changing consequence rule moves mean fatality 22–58 percentage points. Identity-targeting is never decisively safest; anonymization only delays targeting as agents re-infer hidden rule.
- **Key Innovation:** Attribution methodology showing deployment rules causally alter safety outcomes independent of model capability — targeting hazard is universal.
- **Link:** https://arxiv.org/abs/2607.07695

### 14. Guidance Breaks the Fitted Operator: Terminal-Fitted Repair for CFG
- **Authors:** Shiheng Zhang
- **Abstract:** Analyzes CFG through asymptotic-preserving numerical analysis. Shows guidance re-stiffens discriminative subspace to exponent 1+w, making DDIM no longer fitted on coarse meshes. Proves guided clock barrier with three ordered step-size thresholds. Proposes one-coefficient, zero-extra-NFE repair replacing CFG's w(r-1) with r^(1+w)-r. Acts as high-guidance stabilizer on CIFAR-10 and Stable Diffusion 1.5 (9/9 point-FID wins).
- **Key Innovation:** Identifies CFG oversaturation as a numerical solver artifact (not continuous guided law) and provides a principled one-line repair.
- **Link:** https://arxiv.org/abs/2607.07665

---

## CTR / IR / Recommendation Highlights

### 15. MMEACR: Multimodal Memory-Enhanced Agent Collaboration for Recommendation
- **Authors:** Hao Cong, Huizu Lin, Zihan Wang, Chengkai Huang, Quan Z. Sheng, Lina Yao
- **Abstract:** Dual-track memory architecture separating interpretable agent reasoning from fine-grained multimodal matching. User/Item Memory Agents with attribute-guided reinforcement-and-reflection. Decoupled multimodal embedding memory from raw interaction narratives and item images.
- **Key Innovation:** Dual-track memory for agent-based recommendation: explicit reasoning + implicit multimodal matching with persistent memory updates.
- **Link:** https://arxiv.org/abs/2607.07108

### 16. R^3: Advertisement Compliance Rectification via Group-Relative Experience and Curriculum RL
- **Authors:** Yuan Chen, Zhenyu Hu, Mengge Xue, Te Cao, Liqun Liu, Peng Shu, Huan Yu, Jie Jiang
- **Venue:** ACL 2026 (Industry Track)
- **Abstract:** Targets rectification of textual violations in video ads (speech transcripts + on-screen text). Uses experience-driven data synthesis via group-relative compliance experience extractor, curriculum RL with hierarchical rewards. Seamlessly integrates text recognition, rewriting, and re-rendering for industrial video ad deployment.
- **Key Innovation:** First industrial framework that harmonizes video ad compliance with semantic intent preservation using curriculum RL and group-relative experience.
- **Link:** https://arxiv.org/abs/2607.07318

### 17. InductWave: Inductive Multi-Hop Logical Query Answering on Knowledge Graphs
- **Authors:** Mayank Kharbanda, Michael Cochez, Rajiv Ratn Shah, Raghava Mutharaju
- **Abstract:** Wavelet-based inductive embedding method for logical query answering on large KGs. Trains on fewer nodes than test graph, performs on par with baselines at half the message-passing layers, outperforms in most cases at 75% layers. Evaluated across varying train-test graph proportions on FB15k-237.
- **Key Innovation:** Inductive KG reasoning via wavelet embeddings requiring significantly fewer layers and supporting inductive generalization to unseen entities.
- **Link:** https://arxiv.org/abs/2607.07422

### 18. Interpretable Uncertainty for Adaptive Retrieval and Reasoning in QA
- **Authors:** Ritajit Dey, Iadh Ounis, Graham McDonald
- **Abstract:** Uncertainty-aware adaptive QA framework based on LLM internal representations. Distinguishes knowledge insufficiency vs ambiguity/conflict from hidden states in single forward pass. Triggers RAG when insufficient, applies reasoning when ambiguous. Provides transparent alternative to opaque retrieval policies.
- **Key Innovation:** Decomposed uncertainty signals from hidden states for transparent adaptive retrieval decisions without multi-step prompting.
- **Link:** https://arxiv.org/abs/2607.07380

---

## Summary Statistics

| Category | New Submissions | Curated |
|----------|----------------|---------|
| cs.AI | 95 | ~15 |
| cs.LG | 110 | ~12 |
| cs.CL | 34 | ~10 |
| cs.IR | 4 | 4 |

## Key Themes

| Theme | Papers |
|-------|--------|
| **LLM RL / Reasoning** | #1 AdaPrefix-GRPO, #2 Compositional RL, #3 SAO, #4 Agon |
| **Knowledge / Memory** | #5 Co-LMLM, #6 LMLM paradigm |
| **Scientific AI** | #7 SciReasoner |
| **LLM Confidence / Hallucination** | #8 Future Confidence, #9 Bielik entity familiarity |
| **LLM Efficiency** | #10 PALS pruning, #11 DeLS-Spec speculative decoding, #12 Role-factorized search |
| **AI Safety** | #13 Institutional Red-Teaming, #14 Recursive Self-Improvement survey |
| **Diffusion** | #15 CFG Guidance repair, #16 Diffusion RLHF |
| **Agent Optimization** | #17 STRACE, #18 EvoSOP |
| **Recommendation / CTR** | #19 MMEACR, #20 R^3 ad compliance |
| **IR / Knowledge Graphs** | #21 InductWave, #22 Interpretable Uncertainty |
