---
title: arXiv Paper Check — AI & CTR (June 27, 2026)
type: synthesis
created: 2026-06-27
updated: 2026-06-27
tags: [arxiv, ai, ctr, recommendation-systems, llm, agent]
sources: []
---

# arXiv Paper Check — AI & CTR (June 27, 2026)

> New submissions from Friday, 26 Jun 2026 — cs.AI (277 total), cs.LG (249 total), cs.IR (28 total).

## AI / LLM / Agent Highlights

### 1. Refusal Lives Downstream of Persona in Chat Models
- **arXiv**: 2606.26161
- **Authors**: Viola Zhong, Qirui Li
- **Venue**: ICML 2026 Mechanistic Interpretability workshop
- **Key insight**: Refusal is gated by a compliant persona direction in activation space. Steering persona suppresses refusal from 97% → 2% in Llama-3.1-8B. Projecting out persona restores refusal. Treating refusal as isolated misses its dependence on persona.

### 2. Detecting and Controlling Sycophancy with Cascading Linear Features
- **arXiv**: 2606.26155
- **Authors**: Maty Bohacek, Rishub Jain, Nicholas Dufour, Thomas Leung, Chris Bregler, Roma Patel
- **Key insight**: Cascading linear features enable better disentanglement of sycophancy behavior. Matches/outperforms LLM-as-judge baselines with lower compute and more interpretability guarantees.

### 3. The Verification Horizon: No Silver Bullet for Coding Agent Rewards
- **arXiv**: 2606.26300
- **Authors**: Binghai Wang et al.
- **Key insight**: For coding agents, verification is now harder than generation. Studies four reward constructions across tasks. Shows no fixed reward function remains effective as policy capability grows — verification must co-evolve with the generator.

### 4. Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems
- **arXiv**: 2606.26356
- **Authors**: Ching-Yu Lin, Yifan Liu
- **Venue**: ICML 2026 Workshop on Failure Modes in Agentic AI
- **Key insight**: Formalizes Compositional Behavioral Leakage (CBL) — editing one prompt module silently shifts behavior of others due to shared context window. Content channel produces detectable effect (Cohen's d = 0.63).

### 5. Humans Disengage, Reasoning Models Persist
- **arXiv**: 2606.26502
- **Authors**: Han-yu Wang
- **Key insight**: LRMs spend more tokens when wrong; humans spend less time when wrong. Both track difficulty identically across items, but diverge within-item. LRM trace length captures uncertainty, not the stopping policy.

### 6. Narration-of-Thought: Inference-Time Scaffolding for Defeasible Ethical Reasoning
- **arXiv**: 2606.26366
- **Authors**: Patrick Cooper, Alvaro Velasquez
- **Venue**: ACL 2026
- **Key insight**: Structured CoT (protagonist, stakeholders, consequences, uncertainty, commitment) cuts stakeholder collapse from 31% → 1% and uncertainty suppression from 72% → 1-24%. No fine-tuning needed.

### 7. Data-driven ML Cannot Reach Symbolic-level Logical Reasoning
- **arXiv**: 2606.26454
- **Authors**: Tiansi Dong, Mateja Jamnik, Pietro Liò
- **Key insight**: Formal proof that supervised deep learning cannot achieve rigorous syllogistic reasoning. Training data cannot distinguish all 24 valid types; end-to-end mapping introduces contradictory training targets. GPT-5 reaches 100% accuracy but still provides incorrect explanations.

### 8. Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight
- **arXiv**: 2606.00424
- **Authors**: Can Jin, Jiakang Li, Rui Wu, Eddy Zhang, Dimitris N. Metaxas
- **Key insight**: Uses weak critiques (cheaper, less capable models) to provide training signal for strong models. On-policy distillation enables scalable oversight beyond human capacity.

### 9. auto-psych: Automating the Science of Mind
- **arXiv**: 2606.26460
- **Authors**: Ben Prystawski et al.
- **Key insight**: Agent-driven theory discovery + automated crowdsourced experiments in cognitive psychology. Nested discovery loops recover ground-truth theories and find theories that fit human data better than literature baselines.

### 10. The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators
- **arXiv**: 2606.26294
- **Authors**: Alex Iacob et al.
- **Key insight**: Evolutionary framework where both agent and evaluator co-evolve. On coding tasks, improves pass rate while using 1.35-1.72x fewer tokens. On paper reviewing, corrects AI-over-acceptance bias (1.91x human rate → parity).

### 11. At the Edge of Understanding: SAEs Trace the Limits of Transformer Generalization
- **arXiv**: 2606.26396
- **Authors**: Praneet Suresh et al.
- **Key insight**: Sparse autoencoders reveal that OOD inputs (typos, jailbreaks) drive models to operate on more fallacious concepts. Enables mechanistically grounded fine-tuning for robustness.

### 12. MKG-RAG-Bench: Benchmarking Retrieval in Multimodal KG-Augmented Generation
- **arXiv**: 2606.26458
- **Authors**: Xiaochen Wang et al.
- **Venue**: KDD'26
- **Key insight**: First benchmark isolating retrieval in multimodal KG-RAG. Shows retrieval quality strongly determines generation outcomes. Cross-domain (general + medical).

## CTR / IR / Recommendation Systems Highlights

### 1. UniFormer: Efficient and Unified Model-Centric Scaling for Industrial Recommendation
- **arXiv**: 2606.27058
- **Authors**: Bo Chen, Jinlong Jiao, Tijian Hu et al. (Kuaishou)
- **Key insight**: Unified model-centric scaling framework decomposing feature and task spaces. Semantic-based tokenization for user-item decoupling. Online A/B: +0.101%/+0.260% Stay Time, +0.729%/+1.113% Watch Time on Kuaishou/Kuaishou Lite.

### 2. NOVA: Verification-Aware Agent Harness for Architecture Evolution in Industrial RecSys
- **arXiv**: 2606.27243
- **Authors**: Shaohua Liu, Liang Fang et al.
- **Key insight**: LLM agent harness with verification cascade (structure → local → offline → online). Architecture gradient for non-differentiable search. L2/L3 tasks achieve 54.5%/60.0% effective pass rate. L3 candidate improves GMV +1.25%/+1.70%/+2.02% on three pCVR objectives.

### 3. AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **arXiv**: 2606.26859
- **Authors**: Changxin Lao et al. (multi-author, alphabetical)
- **Key insight**: Production multi-agent system (Brainstorm → Develop → Evaluate → Harness Evolution SGPO). Closed-loop autonomous RS iteration. SGPO distills execution trajectories into semantic-gradient updates.

### 4. TRUST: Item-Calibrated Interval Evidence for Temporal Session-Based Recommendation
- **arXiv**: 2606.27214
- **Authors**: Linjiang Guo, Nitin Bisht, Shiqing Wu, Yifan Yin, Guandong Xu
- **Key insight**: Calibrates time intervals against each item's own distribution. Score function guides sampling, encoding, aggregation. Plug-in experiments show model-agnostic improvements.

### 5. From Clicks to Intent: Cross-Platform Session Embeddings with LLM-Distilled Taxonomy
- **arXiv**: 2606.26277
- **Authors**: Dianjing Fan, Yao Li et al.
- **Key insight**: Self-supervised Transformer + LLM taxonomy distillation for financial services. Session embedding improves macro Recall@1 by 1.88%, Log Loss by 13.38% on mobile homepage ranking.

### 6. Attributed, But Not Incremental: Cannibalization-Corrected Attribution
- **arXiv**: 2606.26690
- **Authors**: Donghui Li, Bowen Yuan et al. (TikTok)
- **Venue**: ADKDD 2026
- **Key insight**: Experiment-calibrated framework correcting attribution-cannibalization mismatch. Deployed globally across TikTok, achieved ~15pp reduction in cannibalization rate.

### 7. TileMaxSim: IO-Aware GPU MaxSim Scoring
- **arXiv**: 2606.26439
- **Authors**: Ashutosh Sharma
- **Key insight**: Triton kernels reaching 80.2% peak HBM bandwidth. 82M docs/sec, 220x over loop-based, 6.5x over fused PyTorch. Cuts ColBERTv2 latency at 100K candidates from 268ms → 1.2ms.

### 8. GPUSparse: GPU-Accelerated Learned Sparse Retrieval
- **arXiv**: 2606.26441
- **Authors**: Ashutosh Sharma
- **Key insight**: GPU-parallel inverted index for SPLADE. Exact scoring at 787 QPS on 8.8M documents, 235x speedup over Pyserini CPU. 62.6% of H100 peak HBM bandwidth.

## Key Themes

- **Agent systems for recommender evolution**: NOVA and AgentX both deploy multi-agent loops to autonomously improve production recommendation architectures, representing a shift from manual RS iteration to automated self-improvement.
- **Mechanistic interpretability for safety**: Both sycophancy detection (cascading features) and persona-refusal gating advance activation steering methods for understanding and controlling LLM behavior.
- **Verification as bottleneck**: The Verification Horizon paper crystallizes a growing theme — verification, not generation, is now the harder problem for coding agents.
- **Co-evolution**: RQGM and auto-psych both explore settings where the evaluator or environment co-evolves with the agent, moving beyond static benchmarks.
- **GPU-accelerated retrieval**: TileMaxSim and GPUSparse push retrieval to GPU-native execution, achieving 220x and 235x speedups respectively over CPU baselines.
