---
title: "arXiv Paper Check — AI & CTR (July 26, 2026)"
type: synthesis
created: 2026-07-26
updated: 2026-07-26
sources: []
tags: [arxiv, daily-digest, ai, ctr, recommendation, agents, reasoning, efficiency]
---

# arXiv Paper Check — AI & CTR (July 26, 2026)

> Curated from cs.AI (260 new Jul 24), cs.LG (169 new Jul 24), cs.IR new submissions.

---

## CTR & Recommendation (4 papers)

### 1. Can Generative Recommendation Reach Cold Items? A Temporal Perspective on Semantic-ID Generation
- **Authors:** Jie Peng, Yanping Zheng, Zhewei Zhe, Bin Tong, Guan Wang, Bo Zheng
- **Affiliation:** Not specified (arXiv:2607.21101)
- **Key Contribution:** Investigates whether generative recommendation models using semantic IDs can effectively handle cold-start items. Proposes a temporal perspective on how semantic IDs are generated, addressing the fundamental limitation that existing generative rec models struggle with items lacking interaction history. Provides theoretical and empirical analysis of the cold-start bottleneck in the generative paradigm.
- **Why Interesting:** Generative recommendation (HSTU, TIGER, etc.) is a fast-growing industrial paradigm, but cold-start remains its Achilles' heel. This paper directly confronts that gap.

### 2. OpenForgeRL: Train Harness-native Agents in Any Environment
- **Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao
- **Affiliation:** Microsoft Research (arXiv:2607.21557)
- **Key Contribution:** Introduces OpenForgeRL, a framework for training agents using RL within any environment through a harness-native approach. Decouples agent training from specific environment implementations, enabling RL training in diverse settings without environment-specific modifications.
- **Why Interesting:** Environment-agnostic RL training is a key enabler for scaling agent capabilities across domains, directly relevant to Karpathy's emphasis on verifiable environments for RL.

### 3. Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory
- **Authors:** Hyuk Lim, Seunghyun Yoon
- **Affiliation:** (arXiv:2607.21000)
- **Key Contribution:** Proposes a native discrete state-space model (SSM) that separates retention and writing mechanisms, enabling efficient long-sequence memory without the quadratic attention bottleneck. Achieves competitive performance on long-context tasks while maintaining linear scaling.
- **Why Interesting:** Addresses the fundamental memory bottleneck in sequence models — directly relevant to the scaling laws for long user behavior sequences in CTR/rec systems.

### 4. Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems
- **Authors:** Gaurav Dadhich
- **Affiliation:** (arXiv:2607.21503, 23 pages)
- **Key Contribution:** Proposes treating agent memory and cost as lifecycle/architecture problems rather than ad-hoc engineering. Introduces a systematic framework for managing agent context windows, memory retrieval, and cost optimization. Includes evaluation harness and empirical study.
- **Why Interesting:** Context engineering is a core challenge for production LLM agents — Karpathy has emphasized this repeatedly. This paper provides a structured approach.

---

## AI Agents & Safety (6 papers)

### 5. Beyond Sycophancy: Structured Resistance and Compliance in LLM Moral Reasoning
- **Authors:** Baihui Wang, Bernard Koch
- **Affiliation:** (arXiv:2607.21558)
- **Key Contribution:** Studies how LLMs handle moral dilemmas when asked to resist or comply with user requests. Proposes structured frameworks for measuring and improving LLM moral reasoning beyond simple sycophancy. Evaluates resistance patterns across multiple LLM families.
- **Why Interesting:** Alignment and moral reasoning are critical for safe agent deployment — directly relevant to the ongoing debate about LLM "people spirits" and alignment tax.

### 6. AREX: Towards a Recursively Self-Improving Agent for Deep Research
- **Authors:** Shuqi Lu, Chaofan Li, Kun Luo et al. (18 authors)
- **Affiliation:** (arXiv:2607.21461)
- **Key Contribution:** Introduces AREX, a recursive self-improvement framework for deep research agents. The agent iteratively refines its own research methodology, evaluation criteria, and information retrieval strategies. Demonstrates compounding quality improvements across research iterations.
- **Why Interesting:** Recursive self-improvement is the holy grail for agentic systems. This paper provides a concrete, evaluable framework — connects to Karpathy's "autoresearch" vision.

### 7. GuardianAgentBench: Where Agents Fail and How to Guard Them
- **Authors:** Vishal Ishwar Naik, Chenyu Xu, Donna Dong, Hussein Hassan, Abhishek Pradhan, Ofer Mendelevitch, Tallat Shafat, Humayun Irshad
- **Affiliation:** (arXiv:2607.20982)
- **Key Contribution:** Proposes a comprehensive benchmark for evaluating agent failure modes and guardrail effectiveness. Identifies common failure patterns (goal drift, hallucinated actions, tool misuse) and evaluates existing mitigation strategies.
- **Why Interesting:** Agent safety benchmarks are becoming first-class concerns. This directly addresses the verification gap in agentic systems.

### 8. Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills
- **Authors:** Zibin Lin, Shengli Zhang, Taotao Wang, Yihan Xia, Deen Ma, Guofu Liao
- **Affiliation:** (arXiv:2607.20999)
- **Key Contribution:** Introduces a mechanism for learning reusable agent skills at the workflow level, with attribution-guided repair of broken skills. Enables transfer of learned behaviors across similar workflows without full retraining.
- **Why Interesting:** Skill transfer and repair are key for production agent systems — connects to Karpathy's "bacterial code" and skill graph concepts.

### 9. PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning
- **Authors:** Yipeng Shi, Zhipeng Ma, Yue Wang, Qitai Tan, Yang Li, Peng Chen, Zhengzhou Zhu
- **Affiliation:** (arXiv:2607.21419)
- **Key Contribution:** Proposes a policy-aware scaffolding approach for training agentic RL systems. The scaffolding adapts training difficulty and structure based on the current policy state, preventing reward hacking and improving sample efficiency.
- **Why Interesting:** Training agents via RL without reward hacking is a fundamental challenge — this provides a practical scaffolding solution.

### 10. Detecting LLM-Generated Tokens in Human--LLM Coauthored Text
- **Authors:** Yangjun Lu, Hongyi Zhou, Fabian Spill, Kai Ye, Chengchun Shi, Jin Zhu
- **Affiliation:** (arXiv:2607.21458)
- **Key Contribution:** Develops methods to detect which tokens in human-LLM coauthored text were generated by the LLM vs. written by humans. Uses statistical and model-based approaches to achieve high detection accuracy.
- **Why Interesting:** As human-AI coauthoring becomes the norm, attribution and provenance tracking become essential — relevant to data integrity and the "slopacolypse" concern.

---

## Reasoning & Optimization (4 papers)

### 11. Test-Time Scaling via Error Localization
- **Authors:** Rajiv Shailesh Chitale, Rahul Madhavan, Taneesh Gupta, Deepanway Ghosal, Aravindan Raghuveer
- **Affiliation:** (arXiv:2607.21453, 10 pages)
- **Key Contribution:** Proposes a test-time scaling method that localizes errors in LLM outputs and applies targeted correction. Instead of generating multiple full completions, identifies specific error regions and re-generates only those parts, achieving comparable quality with significantly less compute.
- **Why Interesting:** Test-time compute scaling is a major theme (Karpathy's "scaling laws go vertical"). Error-localized scaling is more efficient than brute-force sampling.

### 12. Relative Value Learning
- **Authors:** Marc Höftmann, Jan Robine, Stefan Harmeling
- **Affiliation:** Published at ICLR 2026 (arXiv:2607.21120)
- **Key Contribution:** Introduces a learning paradigm where models learn relative value comparisons rather than absolute scores. This enables better generalization across distributions and more robust preference learning.
- **Why Interesting:** Relative value learning connects to reward modeling and preference optimization (DPO/KTO) — fundamental to RL post-training.

### 13. Best-of-Evidence: Best-of-N Selection under Partial Verification
- **Authors:** Cenwei Zhang, Teng Fang, Yuxia Wang, Derek Li, Bryan Dai, Lei You
- **Affiliation:** (arXiv:2607.20950, 28 pages)
- **Key Contribution:** Studies best-of-N selection when only partial verification of solutions is available. Develops theory and algorithms for optimal selection strategies under incomplete verification, with applications to LLM reasoning and code generation.
- **Why Interesting:** Partial verification is the real-world scenario for most LLM applications — connects to Karpathy's emphasis on verifiability as a key challenge.

### 14. The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works
- **Authors:** Yu Wang
- **Affiliation:** (arXiv:2607.21273)
- **Key Contribution:** Identifies a failure mode where dense prediction rewards cause GRPO-trained agents to collapse into degenerate policies. Proposes alternative reward structures and training protocols that maintain agent capability while enabling RL improvement.
- **Why Interesting:** GRPO (Group Relative Policy Optimization) is widely used for LLM post-training. Understanding its failure modes is critical — directly relevant to Karpathy's RL insights.

---

## LLM Efficiency & Architecture (4 papers)

### 15. Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context
- **Authors:** Alagappan Valliappan
- **Affiliation:** (arXiv:2607.21535, 25 pages)
- **Key Contribution:** Proposes a windowed multi-token prediction (MTP) approach that eliminates the KV-cache overhead of full-context draft models at million-token context lengths. Enables efficient speculative decoding even with extremely long contexts.
- **Why Interesting:** Million-token context is becoming standard (Llama 4 Scout 10M, Kimi K2 196K). Efficient inference at scale is a production requirement.

### 16. Emergent Misalignment Recruits a Pre-existing Persona Subspace
- **Authors:** Mohammed Suhail B Nadaf
- **Affiliation:** (arXiv:2607.21356, 108 pages)
- **Key Contribution:** Provides comprehensive analysis showing that emergent misalignment in LLMs operates by activating pre-existing persona subspaces in the model's representation. Misalignment doesn't create new behaviors but amplifies existing latent tendencies.
- **Why Interesting:** Deep mechanistic understanding of alignment failures — connects to Karpathy's "ghosts not animals" insight that LLMs have latent behavioral modes.

### 17. AI Assistants Overassist
- **Authors:** Verona Teo, Raghav Jain, Tobias Gerstenberg, Max Kleiman-Weiner
- **Affiliation:** (arXiv:2607.21306)
- **Key Contribution:** Empirically demonstrates that AI assistants systematically over-assist users, reducing learning and skill development. Proposes calibration methods to balance helpfulness with preserving user agency and skill growth.
- **Why Interesting:** Directly addresses Karpathy's "atrophy" concern — that LLM assistance causes cognitive skill degradation.

### 18. HoPE: Hilbert Operator for Progressive Encoding
- **Authors:** Hossein Mobahi, Peter L. Bartlett
- **Affiliation:** (arXiv:2607.21366)
- **Key Contribution:** Proposes a mathematical framework (HOPE) for deconstructing learned representations in deep networks using Hilbert space operators. Provides theoretical guarantees for representation quality and progressive encoding.
- **Why Interesting:** Theoretical foundations for understanding what deep networks actually learn — connects to representation learning fundamentals.

---

## Summary & Key Themes

### Cross-cutting patterns from Jul 26 submissions:

1. **Agent memory as architecture problem**: Multiple papers (Naju, Agentic Context Management, AttriMem) treating agent memory not as ad-hoc engineering but as a first-class architectural concern.

2. **Recursive self-improvement goes concrete**: AREX provides an evaluable framework for autoresearch — moving from vision to measurable systems.

3. **Verifiability as the new bottleneck**: Best-of-Evidence, GuardianAgentBench, and PATS all address the verification gap in different ways — partial verification, failure mode benchmarking, and training scaffolding.

4. **Representation understanding deepens**: Emergent Misalignment (persona subspaces), HOPE (Hilbert operators), and Relative Value Learning all advance our understanding of what's inside neural networks.

5. **Efficiency at million-token scale**: Windowed-MTP and Error-Localization Scaling address the practical challenge of running LLMs at production scale with millions of tokens of context.

6. **Alignment beyond sycophancy**: Beyond Sycophancy and AI Assistants Overassist push the alignment conversation past simple "be helpful" toward calibrated, agency-preserving behavior.

---

## Raw Paper IDs

| Category | Papers |
|----------|--------|
| CTR/Rec | 2607.21101, 2607.21557, 2607.21000, 2607.21503 |
| Agents/Safety | 2607.21558, 2607.21461, 2607.20982, 2607.20999, 2607.21419, 2607.21458 |
| Reasoning | 2607.21453, 2607.21120, 2607.20950, 2607.21273 |
| Efficiency | 2607.21535, 2607.21356, 2607.21306, 2607.21366 |

**Total: 18 curated papers** from 430+ new submissions across cs.AI, cs.LG, and cs.IR.
