# arXiv Daily: AI/LLM/RecSys/Ads/Seq/CTR/Games (2026-10-02)

Generated from arXiv API (last updated first). Showing top 40 relevant papers.

## 1. DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication

**arXiv:** [https://arxiv.org/abs/2610.02161v1](https://arxiv.org/abs/2610.02161v1)
**Primary category:** 
**Authors:** Hanchu Zhou; Dechen Gao; Hang Wang; Brendan Lynch; Boqi Zhao; Qiyao Ma; Raman Goyal; Junshan Zhang
**Institution/Company:** _(not available from API)_

### Abstract

Vision-language models (VLMs) and vision-language-action models (VLAs) have recently driven rapid progress in general-purpose robots, yet most progress has focused on single-robot settings. Extending these capabilities to multi-robot systems remains challenging because robots must coordinate long-horizon behaviors while maintaining reliable, fine-grained execution. We introduce DuoMind, a distributed hierarchical framework for multi-robot coordination through semantic communication. Each robot uses a VLA-based action model for low-level execution and a VLM-based orchestrator for high-level reasoning and inter-agent coordination. At each planning step, the orchestrator at each robot reasons over the task instruction, local observations, and messages received from other robots. It then generates low-level instructions for the action model and semantic messages for peer robots. This architecture exploits the complementary strengths of pretrained models by combining the semantic reasoning capabilities of VLMs with the precise action-generation capabilities of VLAs. To address the scarcity of benchmarks for multi-robot coordination, we further develop RoboPoly, a benchmark comprising long-horizon manipulation tasks that require coordinated, closed-loop execution under distributed control. Experiments on RoboPoly and RoboTwin demonstrate that DuoMind improves multi-robot task performance, while ablation studies confirm the contributions of hierarchical orchestration and semantic communication. More details are available on our project page.

### Key Innovations

- Vision-language models (VLMs) and vision-language-action models (VLAs) have recently driven rapid progress in general-purpose robots, yet most progress has focused on single-robot settings.
- Extending these capabilities to multi-robot systems remains challenging because robots must coordinate long-horizon behaviors while maintaining reliable, fine-grained execution.
- We introduce DuoMind, a distributed hierarchical framework for multi-robot coordination through semantic communication.

---

## 2. VISTA: A Visual Harness for Reasoning in an Interactive World

**arXiv:** [https://arxiv.org/abs/2610.02200v1](https://arxiv.org/abs/2610.02200v1)
**Primary category:** 
**Authors:** Qiushi Han; Keya Hu; Linlu Qiu; Cathy Wu; Kaiming He
**Institution/Company:** _(not available from API)_

### Abstract

We show that multimodal models possess strong reasoning abilities and that an appropriate harness can unlock their potential to solve tasks across diverse interactive environments. We introduce VISTA, a visual harness that gives a general-purpose multimodal model long-horizon vision. VISTA allows the model to directly perceive the environment through visual observations and maintains a lossless visual memory that preserves past observations in their original form. The model can actively retrieve these observations and reorganize its visual input as it reasons. On ARC-AGI-3, VISTA improves Claude Opus 5.0's Relative Human Action Efficiency score from 40.68 to a perfect 100.00, with the model completing all 25 public games using 57.4% fewer actions than first-time human participants. VISTA's simple design also allows it to extend naturally to diverse visual environments with minimal adaptation. Across three additional benchmarks covering a diverse range of visual games and puzzles, it substantially outperforms baselines using the same underlying model with minimal harnesses. Our results highlight VISTA's potential as a general-purpose visual harness for advancing multimodal agents in complex visual environments.

### Key Innovations

- We show that multimodal models possess strong reasoning abilities and that an appropriate harness can unlock their potential to solve tasks across diverse interactive environments.
- We introduce VISTA, a visual harness that gives a general-purpose multimodal model long-horizon vision.
- VISTA allows the model to directly perceive the environment through visual observations and maintains a lossless visual memory that preserves past observations in their original form.

---

## 3. Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes

**arXiv:** [https://arxiv.org/abs/2610.02117v1](https://arxiv.org/abs/2610.02117v1)
**Primary category:** 
**Authors:** Sophia Sirko-Galouchenko; Monika Wysoczanska; Andrei Bursuc; Nicolas Thome; Spyros Gidaris
**Institution/Company:** _(not available from API)_

### Abstract

On-policy self-distillation has recently emerged as an effective approach for improving language-model reasoning by supervising students with a frozen or EMA version of themselves that receives privileged information. Its application to multimodal large language models (MLLMs), however, remains largely unexplored. Recent approaches use privileged visual information, such as image crops corresponding to a question, to improve fine-grained perception, but their gains are confined to tasks that benefit from such visual zooming and require either human-annotated grounding data or external teacher models. We introduce a different form of on-policy self-distillation for MLLMs that provides the teacher with textual, spatially grounded guidance identifying the visual elements relevant to a query. We use procedurally generated scenes with automatically available object identities and spatial coordinates, enabling scalable and annotation-free post-training. The teacher uses this spatial guidance to locate and integrate evidence from multiple relevant image regions, while the student learns to reproduce the resulting behavior from the image and question alone. Our approach consistently improves performance on counting, document and chart understanding benchmarks across multiple models. Importantly, although post-training uses only synthetic scenes, the resulting improvements transfer to real-world perception benchmarks, yielding a 3.23-point gain in average performance across CVBench, V*, ZoomBench, BLINK, HR-Bench, and MME-RealWorld. These results show that spatially grounded privileged information can induce broader perceptual capabilities through on-policy self-distillation, enabling substantial synthetic-to-real transfer beyond the task and data distribution used for post-training. Project page: https://github.com/sirkosophia/Where-OPD

### Key Innovations

- On-policy self-distillation has recently emerged as an effective approach for improving language-model reasoning by supervising students with a frozen or EMA version of themselves that receives privileged information.
- Its application to multimodal large language models (MLLMs), however, remains largely unexplored.
- Recent approaches use privileged visual information, such as image crops corresponding to a question, to improve fine-grained perception, but their gains are confined to tasks that benefit from such visual zooming and require either human-annotated grounding data or external teacher models.

---

## 4. SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale

**arXiv:** [https://arxiv.org/abs/2609.08228v2](https://arxiv.org/abs/2609.08228v2)
**Primary category:** 
**Authors:** Dawei Fu; Cheng Jiang; Sitian Qian; Huainan Wang; Zhongkai Hao
**Institution/Company:** _(not available from API)_

### Abstract

LLM agents use large libraries of reusable skills. At thousands of skill entries, retrieval becomes the bottleneck. Graph-of-Skills (GoS) retrieves dependency-aware bundles from a typed skill graph, and SkillDAG shows that such a graph can accumulate execution-backed structure online. Neither asks whether execution traces can be distilled into a better retrieval graph that generalizes to unseen tasks. We present \textbf{Self-Evolving Graph-of-Skills (SE-GoS)}, which treats the retrieval graph as an index rather than a learned representation: the graph is maintained from execution traces while the retrieval pipeline, the skill library, and the model stay fixed. SE-GoS applies three updates: (1) \textbf{topology}, which induces relations from execution evidence and retracts an avoid edge only after repeated successful co-use; (2) \textbf{edge-weight}, which softly attenuates unsupported semantic edges and reinforces incoming edges to used skills; and (3) \textbf{node-description}, which updates retrieval-facing descriptions stored on graph nodes ranked too low. On SkillsBench, one evolution round lifts average reward from 52.4\% to 59.4\%, above full-library loading, vector retrieval, static GoS, and SkillDAG, and this ordering repeats on all three backbones. Retrieval over the evolved graph spends about two-thirds of the input tokens that loading the full library costs. Repeating the round does not help. The same graph improves a held-out split it never saw from 52.9\% to 58.3\%, so what it accumulates transfers rather than memorizes traces. Skill graphs can therefore be improved from execution experience without model training, retrieval-algorithm changes, skill-content modifications, or a model judging which skills are related.

### Key Innovations

- LLM agents use large libraries of reusable skills.
- At thousands of skill entries, retrieval becomes the bottleneck.
- Graph-of-Skills (GoS) retrieves dependency-aware bundles from a typed skill graph, and SkillDAG shows that such a graph can accumulate execution-backed structure online.

---

## 5. Faynt: Scaling and Optimizing Policies for Competitive Melee

**arXiv:** [https://arxiv.org/abs/2610.02144v1](https://arxiv.org/abs/2610.02144v1)
**Primary category:** 
**Authors:** Ali Janati; Nikita Kuzmin; Rohit Swamy; Charles Niu
**Institution/Company:** _(not available from API)_

### Abstract

We introduce Faynt, a family of 10M- and 75M-parameter Transformer policies for Super Smash Bros. Melee, each controlling all 26 characters with a single checkpoint. After reinforcement learning (RL), the 10M wins 240 of 244 same-character games (98.4%) against fourteen specialist and multi-character releases on their supported rosters, with a winning record against every release. These opponents retain 21- or 24-frame action delays; Faynt uses no added delay, and we have not isolated the effect of this difference. In a separate evaluation against a privately supplied zero-delay Slippi-AI model, the 10M wins all 68 games across two conditioning settings. We study architecture, optimization, scaling, and hyperparameter transfer to guide pretraining on approximately 840,000 human replays. Post-training combines rank- and outcome-based curricula, 75M-to-10M distillation, and RL restricted to Fox mirror matches. On the initial 152-game benchmark, the supervised 10M wins 69.7% of games, compared with 45.4% for the pretrained 75M, despite higher overall held-out controller-prediction loss. The weighted validation loss used for supervised checkpoint selection agrees with the win-rate ordering of all four pretrained and supervised policies. After supervised post-training, both models take less damage per minute, build larger early leads, and win more often after losing the first life. Optimized inference on recorded game states averages 5.2 ms per decision for the 10M and 8.7 ms for the 75M on an NVIDIA T4, excluding emulator execution and communication. We open-source the weights, both benchmark suites, and a platform for automated model tournaments.

### Key Innovations

- We introduce Faynt, a family of 10M- and 75M-parameter Transformer policies for Super Smash Bros.
- Melee, each controlling all 26 characters with a single checkpoint.
- After reinforcement learning (RL), the 10M wins 240 of 244 same-character games (98.4%) against fourteen specialist and multi-character releases on their supported rosters, with a winning record against every release.

---

## 6. CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning

**arXiv:** [https://arxiv.org/abs/2610.02039v1](https://arxiv.org/abs/2610.02039v1)
**Primary category:** 
**Authors:** Yafei Zhang; Songshuo Lu; Sicong Liao; Zhi Chen; Yaohua Tang
**Institution/Company:** _(not available from API)_

### Abstract

Recent years have witnessed the rapid adoption of reinforcement learning (RL) in large language model (LLM) post-training, with substantial gains in mathematical reasoning and code generation. In practical systems, however, policy updates and differences between rollout and training engines can make sampled responses off-policy. Sequence-level masking addresses this mismatch by deciding whether an entire response should contribute to optimization. A common masking rule uses the length-normalized geometric mean of sampled token probability ratios. Its signed log-ratios can cancel across positions, concealing substantial bidirectional policy drift. We propose \emph{Cancellation-Aware Response Masking} (CARM), a sequence-level mask that takes the absolute value of each token log-ratio before averaging, preventing opposing probability changes from canceling. We prove that accepted responses satisfy a joint bound on the fraction of sampled-token ratios outside a prescribed band and their mean log-distance beyond its boundaries. Experiments on mathematical reasoning and code generation show that CARM improves mean@16 averaged over AIME 2024/2025/2026 and BeyondAIME by up to $3.13$ percentage points over geometric-mean masking, and increases average pass@1 across four code benchmarks by $2.88$ points over the strongest evaluated baseline. These findings support CARM as a theoretically grounded and effective method for response-level off-policy control in LLM reinforcement learning.

### Key Innovations

- Recent years have witnessed the rapid adoption of reinforcement learning (RL) in large language model (LLM) post-training, with substantial gains in mathematical reasoning and code generation.
- In practical systems, however, policy updates and differences between rollout and training engines can make sampled responses off-policy.
- Sequence-level masking addresses this mismatch by deciding whether an entire response should contribute to optimization.

---

## 7. SPHERE: Adaptive VR Indoor Scene Generation via LLM-Enhanced Spatial Preference Learning and Human-in-the-Loop RL

**arXiv:** [https://arxiv.org/abs/2610.02023v1](https://arxiv.org/abs/2610.02023v1)
**Primary category:** 
**Authors:** Hyeonmin Lee; Zheng Wei; Kyungmin Kwon; Jumin Seo; Jiwon Park; Hayoung Oh
**Institution/Company:** _(not available from API)_

### Abstract

While Large Language Models (LLMs) advance 3D indoor scene synthesis, current pipelines fail to retain user-specific preferences across sessions, making immersive authoring a repetitive and physically fatiguing process. We present SPHERE, an adaptive VR generation framework that transforms isolated synthesis into continuous human-AI co-creation. SPHERE extracts persistent spatial preferences from natural multimodal interactions (speech and controller edits). To ensure geometric resilience against spatial distortions, it abstracts these raw edits into hierarchical constraints modeling both local functional and global topological contexts. Furthermore, a human-in-the-loop reinforcement learning mechanism dynamically updates retrieval policies based on the user's final edited scenes. A mixed-design user study ($N=42$) and an offline ablation demonstrate that SPHERE significantly reduces corrective edits and physical demand, preventing bias toward shallow object-level traits to yield geometrically resilient, profile-aligned layouts. Ultimately, SPHERE demonstrates how capturing demonstrated spatial logic enables controlled spatial adaptation, establishing a reliable, governed human-AI collaboration framework for immersive authoring. Project page and source code will be available at: https://github.com/hyeonmin11/SPHERE

### Key Innovations

- While Large Language Models (LLMs) advance 3D indoor scene synthesis, current pipelines fail to retain user-specific preferences across sessions, making immersive authoring a repetitive and physically fatiguing process.
- We present SPHERE, an adaptive VR generation framework that transforms isolated synthesis into continuous human-AI co-creation.
- SPHERE extracts persistent spatial preferences from natural multimodal interactions (speech and controller edits).

---

## 8. External Observers May See More Clearly: Cross-Model Span-Level Hallucination Detection in Large Language Models via Hidden State Probing

**arXiv:** [https://arxiv.org/abs/2610.02066v1](https://arxiv.org/abs/2610.02066v1)
**Primary category:** 
**Authors:** Kingshuk Gupta; Davide Buscaldi
**Institution/Company:** _(not available from API)_

### Abstract

As Large Language Models (LLMs) increasingly serve as foundational reasoning engines, their tendency to hallucinate remains a critical vulnerability. While recent internal state probes offer a promising alternative to slow external retrieval systems, they largely reduce hallucination detection to a token-wise binary classification task, failing to capture the structured, sequential boundaries of semantic drift. Here, we introduce an internal hidden state framework for fine-grained, span-level hallucination detection. By inspecting layer-wise activation patterns, we attempt to detect the exact hallucination onset and continuation tokens in an LLM generation. Our experiments show that this approach successfully isolates hallucination onsets, achieving substantial improvements in Precision-Recall AUC over random baselines despite extreme class imbalance. Ultimately, we propose a novel cross-model detection framework in which one model observes the internal representations elicited by another model's generation. We find that an external observer can match or exceed a generator's self-detection of its own hallucination onsets, including when the observer is the smaller model, suggesting that self-detection is not the ceiling for onset localisation.

### Key Innovations

- As Large Language Models (LLMs) increasingly serve as foundational reasoning engines, their tendency to hallucinate remains a critical vulnerability.
- While recent internal state probes offer a promising alternative to slow external retrieval systems, they largely reduce hallucination detection to a token-wise binary classification task, failing to capture the structured, sequential boundaries of semantic drift.
- Here, we introduce an internal hidden state framework for fine-grained, span-level hallucination detection.

---

## 9. When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse

**arXiv:** [https://arxiv.org/abs/2609.28870v2](https://arxiv.org/abs/2609.28870v2)
**Primary category:** 
**Authors:** Yiyu Liu; Minlan Yu; Juncheng Yang
**Institution/Company:** _(not available from API)_

### Abstract

Long-running LLM applications repeatedly send growing context, making prefix caching critical for reducing prefill cost. Yet prefix-cache behavior under agentic workloads remains poorly understood. We study production traces from two companies and evaluate 14 eviction algorithms across HBM-constrained and large memory-pool settings. Despite a large gap to Belady, sophisticated policies designed for traditional caches provide little benefit over LRU. The reason is structural: prefix reuse is dominated by the regular pacing of active sessions, making recency unusually predictive. Prefix caching nevertheless introduces new challenges, including heavy-tailed session footprints and highly variable miss costs as attention computation grows with sequence length. We introduce the compute-savings ratio and two offline oracles to quantify these effects. Our results show that effective prefix-cache management should retain recency as its foundation while selectively adding quick demotion for one-hit prefixes, compute-aware partial eviction for expensive misses, and capacity-dependent eviction granularity. We will release the traces and simulator to support future research.

### Key Innovations

- Long-running LLM applications repeatedly send growing context, making prefix caching critical for reducing prefill cost.
- Yet prefix-cache behavior under agentic workloads remains poorly understood.
- We study production traces from two companies and evaluate 14 eviction algorithms across HBM-constrained and large memory-pool settings.

---

## 10. Bellman Meets Lyapunov: Unsupervised Reinforcement Learning via Mastering Chaos

**arXiv:** [https://arxiv.org/abs/2610.02012v1](https://arxiv.org/abs/2610.02012v1)
**Primary category:** 
**Authors:** Tristan Shah; Wooyoung Chung; Volodomyr Makarenko; Juan Wachs; Stas Tiomkin
**Institution/Company:** _(not available from API)_

### Abstract

Reinforcement learning (RL) is a powerful paradigm for training agents, yet its success rests on domain expertise of human engineers who design informative reward signals for every new task. Unsupervised RL aims to reduce this engineering with intrinsic motivation (IM): reward signals that emerge from the agent environment interaction itself. Existing IM objectives, however, involve the selection of information variables, which re-introduces domain expertise the field has sought to eliminate. We introduce Forward CIP (F-CIP), an RL-native formulation of the Controllable Information Production (CIP) objective, which is defined by the system's dynamics alone and requires no such selection. We prove that F-CIP is compatible with RL and demonstrate its effectiveness with existing algorithms. Training agents with F-CIP results in unsupervised discovery of primitive behaviors such as balancing and maintaining controllability, which are essential for more complex robot behaviors. Paired with a simple forward-velocity reward, our method produces coordinated gaits such as hopping and running which otherwise require reward engineering to learn.

### Key Innovations

- Reinforcement learning (RL) is a powerful paradigm for training agents, yet its success rests on domain expertise of human engineers who design informative reward signals for every new task.
- Unsupervised RL aims to reduce this engineering with intrinsic motivation (IM): reward signals that emerge from the agent environment interaction itself.
- Existing IM objectives, however, involve the selection of information variables, which re-introduces domain expertise the field has sought to eliminate.

---

## 11. Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints

**arXiv:** [https://arxiv.org/abs/2610.02074v1](https://arxiv.org/abs/2610.02074v1)
**Primary category:** 
**Authors:** Abid Mohamed Nadhir; Ahmad Al Hanbali; Beggas Mounir
**Institution/Company:** _(not available from API)_

### Abstract

Privacy-preserving machine learning presents significant deployment challenges on the cloud for intelligent systems with confidential data. Fully Homomorphic Encryption (FHE) offers a compelling solution for secure computation, preserving data confidentiality of cloud computations. However, applying FHE to reinforcement learning (RL) requires replacing non-linear operations with polynomial approximations, which diverge catastrophically due to a unique recursive error phenomenon known as the Bellman drift. This article introduces the Homomorphic Advantage Operator (HAO), a stabilization framework designed to prevent polynomial approximation divergence in FHE-based deep RL. HAO adapts the zero-mean centering projection from advantage-based value estimation directly to temporal-difference (TD) targets. This linear projection annihilates the uniform state-value baseline that drives the Bellman drift, maintaining per-state action rankings while requiring zero additional non-linear multiplicative depth and avoiding expensive ciphertext bootstrapping. The proposed HAO framework was evaluated using a three-tier experimental methodology, including a tabular Markov Decision Process (MDP), an encrypted CartPole environment using real CKKS cryptographic operations, and a 20-node logistics routing benchmark with dense continuous features. The results demonstrate that the proposed HAO strictly bounds network pre-activations within the safe polynomial approximation domain. The proposed HAO RL agents achieved 0% boundary breaches across all random seeds used, whereas regularization alone (L2 weight decay and gradient clipping) breached the bound on 3 of 5 seeds and the unstabilized baseline did so in 83.8% of episodes. Finally, HAO agents improve optimal policy accuracy by 18.0 percentage points in tabular domains and remain stable when DP-SGD-style Gaussian noise is added to the clipped gradients.

### Key Innovations

- Privacy-preserving machine learning presents significant deployment challenges on the cloud for intelligent systems with confidential data.
- Fully Homomorphic Encryption (FHE) offers a compelling solution for secure computation, preserving data confidentiality of cloud computations.
- However, applying FHE to reinforcement learning (RL) requires replacing non-linear operations with polynomial approximations, which diverge catastrophically due to a unique recursive error phenomenon known as the Bellman drift.

---

## 12. KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards

**arXiv:** [https://arxiv.org/abs/2610.02206v1](https://arxiv.org/abs/2610.02206v1)
**Primary category:** 
**Authors:** Pengfei Li; Naufal Suryanto; Sicheng Zhang; Muzammal Naseer
**Institution/Company:** _(not available from API)_

### Abstract

LLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations. However, existing evaluations focus on knowledge-based assessments or end-to-end agentic tasks, and do not directly measure LLMs' ability to generate executable commands for real-world cybersecurity tools. This gap is critical because cybersecurity operations rely on strict command-line interfaces (CLIs), where minor syntax errors, incorrect flag--value bindings, or argument misordering can invalidate execution. We introduce KaliBench, a fine-grained benchmark and dataset for natural-language--to--CLI translation on Kali Linux, comprising 8,504 query--command pairs spanning 1,642 tools across 23 capability dimensions and 5 security phases. KaliBench is constructed via a manuscript-grounded pipeline with deterministic canonicalization and alias-aware evaluation, enabling precise and reproducible assessment of tool selection and argument construction. To ensure both semantic correctness and practical executability, we develop a multi-stage verification pipeline that combines LLM-based validation, sandboxed terminal execution, and human-in-the-loop refinement. Building on these fine-grained, deterministic signals, KaliBench further enables runtime-free verifiable rewards for training. Across three evaluation modes and 24 configurations of general-purpose and security-focused open-weight models, no open-weight model exceeds 42% exact-command accuracy in the unrestricted setting, highlighting the difficulty of accurate CLI-based cybersecurity tool use without explicit tool hints. We further show that supervised fine-tuning and reinforcement learning with verifiable rewards derived from KaliBench significantly improve an 8B model and achieve performance comparable to a 685B MoE model.

### Key Innovations

- LLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations.
- However, existing evaluations focus on knowledge-based assessments or end-to-end agentic tasks, and do not directly measure LLMs' ability to generate executable commands for real-world cybersecurity tools.
- This gap is critical because cybersecurity operations rely on strict command-line interfaces (CLIs), where minor syntax errors, incorrect flag--value bindings, or argument misordering can invalidate execution.

---

## 13. Wasserstein Gradient Flows and Forward-Only Diffusion Are Not Enough for Multimodal Sampling

**arXiv:** [https://arxiv.org/abs/2610.02081v1](https://arxiv.org/abs/2610.02081v1)
**Primary category:** 
**Authors:** Daniel McBride; Pratik Khandagale; Cristina Garcia-Cardona; Yen Ting Lin
**Institution/Company:** _(not available from API)_

### Abstract

There has been a proliferation of sampling algorithms based on Wasserstein gradient flows (WGF) and forward-only diffusion processes (FODP), often accompanied by theoretical guarantees of exponentially fast convergence to the target distribution. These guarantees are frequently interpreted as evidence that such methods can efficiently sample complex multimodal distributions, often supported by empirical results. In this work, we argue that this interpretation is fundamentally misleading. By invoking the Jordan-Kinderlehrer-Otto (JKO) scheme and Otto calculus, we establish that the canonical WGF sampling dynamics and overdamped forward diffusion share the same density evolution and therefore inherit the same metastability and slow-mixing phenomena long understood in nonequilibrium statistical physics. We analyze this family of samplers using two complementary tools -- spectral analysis and mean first-passage time (MFPT) analysis -- and show that well-separated multimodality can induce exponentially long mixing times associated with small spectral gaps and rare inter-mode transitions. For the commonly adopted log-linear annealing schedule studied here, we find that introducing intermediate distributions does not remove the exponential scaling of the total transport time. The limitation is structural rather than implementation-specific: purely local, gradient-driven transport mechanisms can require exponentially long times to transport probability mass across well-separated modes. We argue that this represents a fundamental limitation of WGF- and FODP-based sampling in their standard forms, and motivates future development of fundamentally nonlocal mechanisms for efficient multimodal sampling.

### Key Innovations

- There has been a proliferation of sampling algorithms based on Wasserstein gradient flows (WGF) and forward-only diffusion processes (FODP), often accompanied by theoretical guarantees of exponentially fast convergence to the target distribution.
- These guarantees are frequently interpreted as evidence that such methods can efficiently sample complex multimodal distributions, often supported by empirical results.
- In this work, we argue that this interpretation is fundamentally misleading.

---

## 14. Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows

**arXiv:** [https://arxiv.org/abs/2610.02122v1](https://arxiv.org/abs/2610.02122v1)
**Primary category:** 
**Authors:** Gabriel Tomitsuka; Arman Raayatsanati; Emma Xing; Duke Gand; Joseph J Ma
**Institution/Company:** _(not available from API)_

### Abstract

Real-world enterprise data science and analytics workflows require reasoning across dozens of tables, performing statistical analyses, and acting on the results. Established text-to-SQL benchmarks evaluate query generation alone, and audits have found their answer keys frequently wrong. Because real enterprise warehouses are too sensitive to release, these benchmarks are built on public datasets where a business event fits in a single table. We introduce Argo-Bench, an evaluation framework comprising 210 data science and analytics tasks. Drawing on public data, peer-reviewed industry literature, and regulatory filings, we simulate a food delivery platform in New York City at true scale, with 81 million orders in 2024, grounded economics, fraud patterns, and marketplace incentives. We export this world to an ERP warehouse of 235 tables and 7.5 billion rows, modeled on the Oracle E-Business Suite schema. The simulator's ground-truth state is withheld from the warehouse the agent sees, so tasks require reconstructing facts by navigating the warehouse before acting on them. Argo-Bench goes beyond text-to-SQL: the agent files actions such as banning fraudulent accounts, allocating courier incentive budgets, or issuing back pay, and the grader scores each by its consequences in the simulator. Every task has an executable reference solution that demonstrates solvability using only the warehouse. The strongest of 14 frontier and open-weight models scores 95 or higher on only 34.8% of tasks and averages 59.5 points. We hope Argo-Bench drives progress toward agents that understand, navigate, and act within real data environments.

### Key Innovations

- Real-world enterprise data science and analytics workflows require reasoning across dozens of tables, performing statistical analyses, and acting on the results.
- Established text-to-SQL benchmarks evaluate query generation alone, and audits have found their answer keys frequently wrong.
- Because real enterprise warehouses are too sensitive to release, these benchmarks are built on public datasets where a business event fits in a single table.

---

## 15. Finetuning with Sampling: SFT Learns Better Than You Think

**arXiv:** [https://arxiv.org/abs/2610.02140v1](https://arxiv.org/abs/2610.02140v1)
**Primary category:** 
**Authors:** Aayush Karan; Sitan Chen; Yilun Du
**Institution/Company:** _(not available from API)_

### Abstract

Introducing new capabilities to frontier models has long been the goal of posttraining, which predominantly employs supervised finetuning (SFT) and reinforcement learning (RL) to this end. Conventional wisdom dictates that RL enables strong generalization on new tasks without losing existing capabilities, while SFT is prone to weak generalization and catastrophic forgetting. At the same time, SFT can learn from off-policy expert data, whereas RL must rely on a model's ability to find successful trajectories with repeated sampling. In our work, we seek to leverage the strength of on-policy learning while utilizing the privileged information contained in off-policy data. However, rather than modifying the learning objective to accommodate this data, we instead tailor the data distribution to better suit the learner. We introduce a Markov chain Monte Carlo (MCMC) sampling algorithm that progressively transforms off-policy traces to be more on-policy given a reference model for finetuning. Across tasks like scientific skill acquisition, mathematical reasoning, and open-ended expertise, our sampling algorithm enables SFT to rival prevailing posttraining techniques, often generalizing better and forgetting less than strong on-policy baselines. In addition, the resulting finetuned models exhibit strong distributional performance and are capable of learning beyond sharpening the base model distribution. At a higher level, our approach presents sampling as a model-native operator that shapes data for learnability, offering broader utility as a general-purpose primitive throughout the posttraining stack.

### Key Innovations

- Introducing new capabilities to frontier models has long been the goal of posttraining, which predominantly employs supervised finetuning (SFT) and reinforcement learning (RL) to this end.
- Conventional wisdom dictates that RL enables strong generalization on new tasks without losing existing capabilities, while SFT is prone to weak generalization and catastrophic forgetting.
- At the same time, SFT can learn from off-policy expert data, whereas RL must rely on a model's ability to find successful trajectories with repeated sampling.

---

## 16. From Knowledge Access to Source Learning: Developing Source-Specific Competence

**arXiv:** [https://arxiv.org/abs/2610.02150v1](https://arxiv.org/abs/2610.02150v1)
**Primary category:** 
**Authors:** Lucheng Fu; Kejing Xia; Yiyang Wang; Yiqiao Jin; Jinjin He; Xiyuan Yang; Haoxin Liu; Ye Yu; Haibo Jin; Yijia Xiao; Wenke Lee; B. Aditya Prakash; Haohan Wang
**Institution/Company:** _(not available from API)_

### Abstract

Large language model (LLM) agents increasingly rely on persistent external sources to solve sequences of knowledge-intensive tasks. Existing methods improve how source content is accessed and organized, while agent-memory systems preserve reusable knowledge from prior interactions, but repeated use of the same source is still largely treated as repeated access rather than an opportunity to progressively improve understanding of that source. We study source learning: developing reusable source-specific competence over a persistent authoritative source. We represent this competence with a persistent source model that captures reusable understanding of the source, including how its knowledge is structured, interpreted, and applied. To construct and progressively refine such models, we propose SourceLearn, which combines two complementary learning mechanisms. Self-Directed Source Learning identifies what remains incompletely understood and adaptively revisits the source, while Task-Guided Source Learning uses downstream experience to reveal local representational gaps and recurring needs in how source knowledge should be organized. In both cases, learning signals determine what should be reconsidered, while persistent updates are reconstructed from the authoritative source. Across five benchmarks and three LLM backends, SourceLearn achieves the best performance in 13 of 15 settings, with gains of up to 22.6 points over Hybrid RAG and substantial overall improvements over static source representations and experience-based memory baselines.

### Key Innovations

- Large language model (LLM) agents increasingly rely on persistent external sources to solve sequences of knowledge-intensive tasks.
- Existing methods improve how source content is accessed and organized, while agent-memory systems preserve reusable knowledge from prior interactions, but repeated use of the same source is still largely treated as repeated access rather than an opportunity to progressively improve understanding of that source.
- We study source learning: developing reusable source-specific competence over a persistent authoritative source.

---

## 17. Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation

**arXiv:** [https://arxiv.org/abs/2610.02022v1](https://arxiv.org/abs/2610.02022v1)
**Primary category:** 
**Authors:** Noy Sternlicht; Simra Shahid; Peter Jansen; Daniel S. Weld; Pao Siangliulue; Tom Hope
**Institution/Company:** _(not available from API)_

### Abstract

Automated ideation systems are often evaluated on the novelty of the ideas they produce, and that judgment is increasingly delegated to large language models. Such judges are typically built ad hoc and validated, if at all, on human-authored papers rather than on the generated ideas they are meant to score. So, how do novelty judges perform? Not well. We present a systematic controlled study of novelty evaluation design choices. We first build an evaluation set automatically, mining OpenReview for passages where reviewers explicitly affirm or dispute a paper's originality and keeping only submissions with unanimous agreement at the extremes of their research area; we pair these with ideas from a vanilla LLM generator. Across six judges, we find that small prompt design choices have large consequences; e.g., simply telling the judge that reviewers found one idea novel and the other not can change its verdict on more than half of the identical idea pairs it is shown, shifting pairwise accuracy by over 50 points and occasionally pushing it below chance. The same change helps one judge and hurts another. Retrieval and larger reasoning budgets help little, and two purpose-built novelty evaluators are outperformed by our cheapest prompted baseline. These results raise questions about reported novelty gains of automated ideation systems, and call for robust novelty evaluation methods.

### Key Innovations

- Automated ideation systems are often evaluated on the novelty of the ideas they produce, and that judgment is increasingly delegated to large language models.
- Such judges are typically built ad hoc and validated, if at all, on human-authored papers rather than on the generated ideas they are meant to score.
- So, how do novelty judges perform? Not well.

---

## 18. Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents

**arXiv:** [https://arxiv.org/abs/2610.02204v1](https://arxiv.org/abs/2610.02204v1)
**Primary category:** 
**Authors:** Yen-Jen Wang; Haozhe Jiang; Shuying Deng; Haoru Xue; Weirui Ye; Rocky Duan; Nika Haghtalab; S. Shankar Sastry; Pieter Abbeel; Haozhi Qi
**Institution/Company:** _(not available from API)_

### Abstract

Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control. We present Reconstruct, Practice, Go Real (RPG), a framework for autonomous improvement of robot execution systems without updating model weights. RPG identifies manipulation capabilities in an offline dataset and constructs related practice tasks in simulation. During practice, RPG uses execution feedback, privileged simulator state, and available dataset videos to diagnose failures. It develops new reusable symbolic skills, refines existing skills, and revises the system prompt based on these diagnoses. Cross-task evaluation tests individual candidate changes and merged revisions before they are retained for reuse. At test time, a multimodal LLM uses the resulting system prompt and skill library to coordinate perception and robot control. On held-out initializations of 22 manipulation tasks, RPG improves task success from 28.6% after the first practice round to 95.0% after 15 rounds, outperforming all evaluated baselines, including ASPIRE (75.5%) and CaP-Agent0 powered by GPT-6 Astra Pro (60.0%). After a common calibration and hardware-adaptation procedure, the frozen system succeeds in all 30 physical trials, with ten trials on each of three tasks. Project Website: https://rpg-robot.github.io/

### Key Innovations

- Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control.
- We present Reconstruct, Practice, Go Real (RPG), a framework for autonomous improvement of robot execution systems without updating model weights.
- RPG identifies manipulation capabilities in an offline dataset and constructs related practice tasks in simulation.

---

## 19. Diffusion Policy Improvement with Proposal-Conditioned Refinement Flows

**arXiv:** [https://arxiv.org/abs/2609.36812v2](https://arxiv.org/abs/2609.36812v2)
**Primary category:** 
**Authors:** Junhyun Ha; Juho Lee; Byoungwoo Park
**Institution/Company:** _(not available from API)_

### Abstract

Diffusion and flow policies can model complex behaviors in offline reinforcement learning (RL). However, penalizing their KL divergence from the behavior policy can discourage actions having high critic values with low behavior density. Directly refining behavior proposals may be an alternative, yet Gaussian or deterministic editors limit expressiveness to represent multiple separated modes for the same proposal. In this work, we introduce Proposal-Conditioned Refinement Flows (PReFlow), a policy extraction method combining critic-based proposal selection with a conditional refinement flow. To optimize proposal selection and refinement together, we formulate a KL-regularized objective whose optimum induces a Gibbs policy over final actions under a Gaussian-smoothed behavior prior. The refinement flow can represent multiple high value modes, while a proposal-centered Gaussian reference regulates large action changes. This Gaussian reference further enables us to make use of simulation-free, closed form adjoint matching targets from sampled endpoints and critic gradients, yielding a single velocity regression loss without a backward adjoint solve. On 50 OGBench tasks, PReFlow achieves competitive offline performance and the highest aggregate score among the compared methods after online fine-tuning, reaching 91\% after 500K environment steps.

### Key Innovations

- Diffusion and flow policies can model complex behaviors in offline reinforcement learning (RL).
- However, penalizing their KL divergence from the behavior policy can discourage actions having high critic values with low behavior density.
- Directly refining behavior proposals may be an alternative, yet Gaussian or deterministic editors limit expressiveness to represent multiple separated modes for the same proposal.

---

## 20. The Missing Primitive: Diagnosing and Repairing Mathematical Reasoning in Large Language Models

**arXiv:** [https://arxiv.org/abs/2610.02191v1](https://arxiv.org/abs/2610.02191v1)
**Primary category:** 
**Authors:** Shuo Xing; Zilin Dai; Chengyuan Qian; Fangzhou Lin; Wenjing Chen; Ping He; Pan Lu; Alvaro Velasquez; Mohit Bansal; Zhengzhong Tu
**Institution/Company:** _(not available from API)_

### Abstract

While Large Language Models (LLMs) have demonstrated striking capabilities on frontier mathematical problems, it remains unclear whether they possess the structural mathematical understanding underlying their solutions. In this paper, we take a first step toward systematically studying mathematical understanding in LLMs, from diagnosing its distinct capabilities to leveraging these findings to improve post-training. First, we introduce the notion of Mathematical Primitive to probe structural mathematical understanding and propose \hlei{}, a novel benchmark that evaluates mathematical reasoning along four distinct dimensions: Discovery, Generation, Digestion, and Execution. Second, our systematic diagnosis shows that solution accuracy masks distinct capability profiles, primitives unlock substantial latent execution capacity, and Discovery is the dominant bottleneck in mathematical reasoning. Our post-training analysis further shows that discovery-limited failures are particularly amenable to repair. Finally, building on these findings, we introduce \abs{}, a primitive-privileged self-distillation framework that selectively transfers primitive-guided reasoning into the student model. Extensive experiments demonstrate that \abs{} consistently improves mathematical reasoning over baselines across model scales and challenging benchmarks.

### Key Innovations

- While Large Language Models (LLMs) have demonstrated striking capabilities on frontier mathematical problems, it remains unclear whether they possess the structural mathematical understanding underlying their solutions.
- In this paper, we take a first step toward systematically studying mathematical understanding in LLMs, from diagnosing its distinct capabilities to leveraging these findings to improve post-training.
- First, we introduce the notion of Mathematical Primitive to probe structural mathematical understanding and propose \hlei{}, a novel benchmark that evaluates mathematical reasoning along four distinct dimensions: Discovery, Generation, Digestion, and Execution.

---

## 21. ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research

**arXiv:** [https://arxiv.org/abs/2610.02202v1](https://arxiv.org/abs/2610.02202v1)
**Primary category:** 
**Authors:** Sohyeon Kim; Yoonho Lee; Bo Liu; Dayoon Ko; Rulin Shao; Seungone Kim; Graham Neubig; Pang Wei Koh; Aakanksha Chowdhery; Akari Asai; Omar Khattab; Yejin Choi; Gunhee Kim; Chelsea Finn
**Institution/Company:** _(not available from API)_

### Abstract

What makes great scientists great? Even as AI systems start to make progress on open problems, scientists remain far ahead of them at sensing which prior idea, buried in an ever-growing archive of research, a new problem needs. To study this skill, we draw on researchers who know firsthand which earlier work advanced their completed projects, with papers serving as pointers to the ideas within. Using our automated pipeline that makes author annotation scalable, we build ScholarCatalyst by having 184 lead authors of 207 recent computer science papers label which candidates did or could have advanced their project, each with a detailed rationale. We introduce a retrieval task with author-provided judgments: given an initial research question, retrieve these papers from only the literature available when the project began. Agentic search does no better than embedding retrieval (0.42 vs. 0.48 Recall@20) despite calling that same retriever as a tool. Even an agent built on Claude Fable 5.1, which may have seen the completed papers during training, reaches only 0.51 R@20. These results highlight the need for new training recipes that equip models with expert intuition for searching broad corpora. We envision ScholarCatalyst as a step toward scientific agents that can take a half-formed idea and point to the prior research it needs.

### Key Innovations

- What makes great scientists great? Even as AI systems start to make progress on open problems, scientists remain far ahead of them at sensing which prior idea, buried in an ever-growing archive of research, a new problem needs.
- To study this skill, we draw on researchers who know firsthand which earlier work advanced their completed projects, with papers serving as pointers to the ideas within.
- Using our automated pipeline that makes author annotation scalable, we build ScholarCatalyst by having 184 lead authors of 207 recent computer science papers label which candidates did or could have advanced their project, each with a detailed rationale.

---

## 22. AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents

**arXiv:** [https://arxiv.org/abs/2610.02163v1](https://arxiv.org/abs/2610.02163v1)
**Primary category:** 
**Authors:** Xuan Zhang; Longtao Zheng; Cunxiao Du; Bo An; Xin Dong
**Institution/Company:** _(not available from API)_

### Abstract

Coding agents solve repository-level software engineering tasks through long trajectories of code inspection, search, editing, and testing. As a task progresses, earlier exploration becomes stale, so managing context is more than avoiding overflow: an agent must decide when to compact, what working state to preserve, and how to continue from it. We introduce AutoCompact, which trains a coding agent to make these decisions as part of its policy. To collect training data, we run the base agent on coding tasks and use a judge to review its compaction decisions, summaries, and actions after compaction. Flawed outputs are replaced with corrected ones before being executed in the environment, so each trajectory continues from the corrected decisions. We use these trajectories for supervised fine-tuning, then jointly optimize coding and compaction through reinforcement learning with task-success rewards. Experiments on SWE-bench Verified and SWE-PolyBench Verified show that AutoCompact improves pass rates over the base model by an absolute 9.2\% and 5.0\%, respectively. The improvements hold across all evaluated inference budgets, with a 256K context window that never overflows and with a 16K window whose overflow triggers fallback compaction.

### Key Innovations

- Coding agents solve repository-level software engineering tasks through long trajectories of code inspection, search, editing, and testing.
- As a task progresses, earlier exploration becomes stale, so managing context is more than avoiding overflow: an agent must decide when to compact, what working state to preserve, and how to continue from it.
- We introduce AutoCompact, which trains a coding agent to make these decisions as part of its policy.

---

## 23. On Language Drift during RLVR Post-Training

**arXiv:** [https://arxiv.org/abs/2610.02015v1](https://arxiv.org/abs/2610.02015v1)
**Primary category:** 
**Authors:** Michael Sullivan; Alexander Koller
**Institution/Company:** _(not available from API)_

### Abstract

Recent advances in LLM reasoning models---driven primarily by the paradigm of post-training via reinforcement learning with verifiable reward (RLVR)---have enabled them to accomplish impressively complex tasks. However, in parallel with their rising capabilities, LLMs have increasingly displayed signs of language drift in their chains of thought (CoTs): unusual, non-standard, and seemingly nonsensical language use. Although it is well-documented---and can potentially impair CoT monitorability---the causes of language drift are thus far poorly understood. In this paper, we identify the conditions under which language drift occurs: we prove theoretically that RLVR optimization pressure permits unbounded language drift, while supervised fine-tuning does not. We then show empirically that language drift specifically arises during RLVR on novel reasoning tasks---i.e. when the target behavior cannot be drawn out of the base model. Finally, we prove that it is not possible to constrain language drift without constraining expected reward, suggesting that CoT monitorability cannot be improved without harming performance during RLVR post-training at the frontier.

### Key Innovations

- Recent advances in LLM reasoning models---driven primarily by the paradigm of post-training via reinforcement learning with verifiable reward (RLVR)---have enabled them to accomplish impressively complex tasks.
- However, in parallel with their rising capabilities, LLMs have increasingly displayed signs of language drift in their chains of thought (CoTs): unusual, non-standard, and seemingly nonsensical language use.
- Although it is well-documented---and can potentially impair CoT monitorability---the causes of language drift are thus far poorly understood.

---

## 24. Constant-Time Planning for Chaining Collision-free Motion to Manipulation Behaviors

**arXiv:** [https://arxiv.org/abs/2512.00939v3](https://arxiv.org/abs/2512.00939v3)
**Primary category:** 
**Authors:** Nayesha Gandotra; Itamar Mishani; Lai Yuan; Oren Salzman; Maxim Likhachev
**Institution/Company:** _(not available from API)_

### Abstract

Recent progress in contact-rich robotic manipulation has been striking, yet most deployed systems remain confined to simple, scripted routines. One of the barriers is the lack of motion planning algorithms that can provide verifiable guarantees for safety, efficiency and reliability. Constant-Time Motion Planning (CTMP) is a recent step toward such guarantees for collision-free motion in a priori known environments:: a preprocessing phase enables queries to be answered within a fixed, user-specified time budget (e.g., 10 milliseconds). However, CTMP certifies only reachability---a binary predicate---and ignores the manipulation behavior that completes the task, which is increasingly stochastic (e.g., a learned skill) and whose success no single offline rollout can establish, let alone certify. We introduce the Behavioral Constant-Time Motion Planner (B-CTMP), which extends CTMP to two-step manipulation tasks in semi-structured environments: a collision-free motion to a behavior initiation state, followed by execution of a behavior such as grasping or insertion. B-CTMP departs from prior CTMP in two ways: neighborhoods are constructed in object-pose space rather than robot configuration space, and coverage is established by statistical certification rather than a reachability check. A plan is cached only if repeated rollouts lower-bound its success rate above a user-specified threshold, and we prove these bounds hold simultaneously across the entire cache at a prescribed confidence level. For deterministic behaviors a single rollout suffices, recovering the binary check of prior CTMP as a special case. We evaluate B-CTMP on three manipulation tasks---shelf picking, plug insertion, and wheel replacement---in simulation and on real robots. B-CTMP's certified plans succeed consistently where baselines fail during behavior execution, and it rejects infeasible object poses in constant time.

### Key Innovations

- Recent progress in contact-rich robotic manipulation has been striking, yet most deployed systems remain confined to simple, scripted routines.
- One of the barriers is the lack of motion planning algorithms that can provide verifiable guarantees for safety, efficiency and reliability.
- Constant-Time Motion Planning (CTMP) is a recent step toward such guarantees for collision-free motion in a priori known environments:: a preprocessing phase enables queries to be answered within a fixed, user-specified time budget (e.g., 10 milliseconds).

---

## 25. Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration

**arXiv:** [https://arxiv.org/abs/2610.02036v1](https://arxiv.org/abs/2610.02036v1)
**Primary category:** 
**Authors:** Xin Heng
**Institution/Company:** _(not available from API)_

### Abstract

AI agents can each make locally valid decisions yet jointly produce an invalid result. We call this the global coherence problem: a failure of shared state, not merely of model intelligence. Our Observation-Aliasing Impossibility Theorem gives the exact boundary. A policy can guarantee a valid action exactly when all worlds producing the same observation share an admissible action. If k indistinguishable worlds require pairwise-disjoint actions, the best randomized worst-case success is 1/k; more reasoning, roles, messages, or samples cannot recover the missing distinction. A stronger model can reason better within its context, but it cannot see beyond it. We then give local-to-global runtime semantics X = (H, C, G, F; D): topology H records overlapping scopes; category C governs state-changing actions; groupoid G retains reversible translations; sheaf F tests whether local views glue into one world; and minimal history D keeps only distinctions that alter legal futures. Models propose; the harness owns shared state and governs commit. Nine studies test both the failure and its boundary. On a controlled revision benchmark, the same frontier model scores 40/40 when the deciding event is visible; when it is hidden, tested arms score 12--17/40, consistent with chance (1/3); restoring one authoritative fact returns 40/40. On TeamBench, ordinary teams exceed a shared budget in 5/5 runs, a visible live count leaves 4/5 violations, and commit enforcement leaves 0/5. In tau2-bench Telecom, current-state checks score 0.07 after silent reverts, while the harness scores 1.00. Where a conventional solver already owns the complete relevant state, it ties the harness as predicted. The counterintuitive conclusion is that local intelligence cannot substitute for missing global state.

### Key Innovations

- AI agents can each make locally valid decisions yet jointly produce an invalid result.
- We call this the global coherence problem: a failure of shared state, not merely of model intelligence.
- Our Observation-Aliasing Impossibility Theorem gives the exact boundary.

---

## 26. Mimir: Physics-Grounded LLM Agents for Long-Horizon Irrigation Control

**arXiv:** [https://arxiv.org/abs/2610.02038v1](https://arxiv.org/abs/2610.02038v1)
**Primary category:** 
**Authors:** Yimeng Liu; Mi Zhang; Younsuk Dong; Zhichao Cao
**Institution/Company:** _(not available from API)_

### Abstract

Large language model (LLM) agents increasingly combine reasoning, tool use, and action, but most evidence comes from episodic tasks with relatively immediate feedback and reset failures. Long-running physical control operates in a different regime: actions alter future states, errors compound across decisions, and an agent must improve from experience without being allowed to rewrite the physical rules that make execution safe. We study this regime through irrigation, where daily decisions interact with soil-water dynamics over entire growing seasons. We present Mimir, a physics-grounded LLM agent organized around two repair timescales. At the fast timescale, a structured physical interface and deterministic simulator turn an LLM output into a proposal that we numerically check, revise, and subject to bounded deterministic action selection before execution. At the slow timescale, recurrent failure patterns are consolidated into persistent contextual principles that condition future proposals, while the physical model, evaluator, and execution constraints remain immutable. Under a common retrospective evaluator across multiple sites, crops, and years, Mimir attains the lowest reported aggregate control cost among the evaluated references and uses about 51% less irrigation than the historical schedule replay. The ablation study show higher control cost when forward simulation, verified revision, or persistent context is removed; model-scale and model-family studies show no monotonic gain from increasing LLM size. The resulting lesson show that persistent physical agents can combine semantic reasoning with bounded, evidence-driven self-improvement while reserving physical truth and actuator authority for explicit numerical mechanisms.

### Key Innovations

- Large language model (LLM) agents increasingly combine reasoning, tool use, and action, but most evidence comes from episodic tasks with relatively immediate feedback and reset failures.
- Long-running physical control operates in a different regime: actions alter future states, errors compound across decisions, and an agent must improve from experience without being allowed to rewrite the physical rules that make execution safe.
- We study this regime through irrigation, where daily decisions interact with soil-water dynamics over entire growing seasons.

---

## 27. Higher-Order Molecular Grammars for Generative and Foundation Models in Chemistry

**arXiv:** [https://arxiv.org/abs/2610.02186v1](https://arxiv.org/abs/2610.02186v1)
**Primary category:** 
**Authors:** Yiming Huang; Yujie Zeng; Vijay Prakash Dwivedi; Simone Foti; Jianmin Wang; Jure Leskovec; Tolga Birdal
**Institution/Company:** _(not available from API)_

### Abstract

Molecular learning models are strongly shaped by their underlying representations. Yet standard sequential and graph formalisms struggle to explicitly encode higher-order topology, such as ring systems and recurring motifs. Existing higher-order representations can capture these structures directly, but they are often computationally demanding and difficult to decode into valid molecules. Here, we introduce Higher-order Grammar Representation (HGR), a principled, topology-aware framework that lifts molecules to combinatorial complexes and parses each complex into a compact sequence of production rules under a context-free higher-order grammar. By serialising higher-order topology into rule sequences, HGR makes these structures directly compatible with standard sequence models, avoiding the computational overhead of explicit higher-order encodings while preserving topological expressiveness. To reduce benchmark bias towards simple ring systems, we construct RingDiv, a ring-enriched benchmark containing 1.18 million molecules, including the curated RingDiv300k subset, and introduce the ring diversity index (RDI) to quantify ring-system coverage. In molecular generation, HGR-based models uniquely combine 100% validity by construction with leading distributional alignment, ranking first in FCD on all five generation benchmarks. In representation learning, HGR-FM achieves the highest mean AUC across seven MoleculeNet benchmarks under both transfer protocols, improving on the strongest baseline by 8.3 and 3.3 AUC points under probing and full fine-tuning, respectively. Collectively, these results establish HGR as an efficient higher-order representation for molecular generation and transferable representation learning.

### Key Innovations

- Molecular learning models are strongly shaped by their underlying representations.
- Yet standard sequential and graph formalisms struggle to explicitly encode higher-order topology, such as ring systems and recurring motifs.
- Existing higher-order representations can capture these structures directly, but they are often computationally demanding and difficult to decode into valid molecules.

---

## 28. SILSA: Sliding-Window Slice Latents for Topology-Preserving High-Resolution 3D Generation

**arXiv:** [https://arxiv.org/abs/2610.02201v1](https://arxiv.org/abs/2610.02201v1)
**Primary category:** 
**Authors:** Tianjiao Yu; Xinzhuo Li; Yifan Shen; Ying Shen; Kiet A. Nguyen; Adheesh Sunil Juvekar; Ismini Lourentzou
**Institution/Company:** _(not available from API)_

### Abstract

High-resolution 3D generation increasingly relies on voxel latents and multi-stage pipelines that first predict active structure and then synthesize local geometry. While effective, this design fragments continuous surfaces into many local tokens, inflates generation cost, and often weakens topological consistency for thin or highly connected shapes. We introduce SILSA, a topology-aware 3D generation framework that represents shapes with compact sliding-window slice latents. Instead of generating expensive voxel tokens, SILSA uses a fixed set of overlapping slices along the three canonical axes, where each token summarizes a local depth window to preserve cross-sectional continuity and support single-stage rectified-flow generation. A Slice VAE encodes oriented surface samples into multi-axis slice latents and reconstructs them with a sparse volumetric decoder, while a Volumetric Anchor Lattice coordinates directional slice streams through a shared 3D workspace. To preserve structural correctness, we introduce slice-level topology supervision that matches persistence diagrams and aligns Betti transitions across neighboring slices. Experiments show that SILSA improves structural fidelity while substantially reducing generation cost. SILSA improves PSNR by $8.7\%$, coverage by $5.96$ absolute points, and Betti error by $9.2\%$ over the strongest baseline, while using $70.0\%$ fewer tokens than the next-most compact baseline and over $98\%$ fewer tokens than sparse or hierarchical tokenizers, effectively reducing training memory by $40.4\%$ and inference time by $58.5\%$. Qualitative results further show improved preservation of thin structures, repeated components, and long-range connectivity.

### Key Innovations

- High-resolution 3D generation increasingly relies on voxel latents and multi-stage pipelines that first predict active structure and then synthesize local geometry.
- While effective, this design fragments continuous surfaces into many local tokens, inflates generation cost, and often weakens topological consistency for thin or highly connected shapes.
- We introduce SILSA, a topology-aware 3D generation framework that represents shapes with compact sliding-window slice latents.

---

## 29. Generative modeling of intrinsically disordered protein regions by reinforcing sparse autoencoder features

**arXiv:** [https://arxiv.org/abs/2610.02189v1](https://arxiv.org/abs/2610.02189v1)
**Primary category:** 
**Authors:** Jason X. Liu; Sebastian Ibarraran; Frank Hu; Soojung Yang; Xinyu A. Feng; Abigail Park; Anagha Aneesh; Lacramioara Bintu; Alexander R. Dunn; Grant M. Rotskoff
**Institution/Company:** _(not available from API)_

### Abstract

Intrinsically disordered protein regions (IDRs) play central roles in cellular processes such as transcriptional regulation, signal transduction, and subcellular localization, yet their functional design remains challenging. Structure-based design methods do not readily apply to IDRs, and existing protein language models are trained on full-length protein sequences, thus learning a prior that is biased towards folded domains. Here, we present IDiom, an autoregressive protein language model trained on IDiom-DB, a dataset of 54 million predicted IDRs curated from the AlphaFold Database. IDiom generates diverse sequences that recapitulate the composition, patterning, motifs, and predicted disorder of natural IDRs. To control function-associated sequence patterns, we also introduce reinforcement learning with sparse autoencoder features (RL-SAE), a post-training method that rewards the generation of sequences that activate specified feature sets. Across eight IDR design tasks, RL-SAE sequences activate, on average, 90% of 30 targeted features, compared to 24% for activation steering. We demonstrate that RL-SAE improves the predicted subcellular localization and transcriptional activity of generated IDRs compared to steering and supervised fine-tuning, and enables features associated with distinct biological functions to be combined within individual sequences. Thus, IDiom and RL-SAE enable interpretable and composable IDR design through explicit control of function-associated sequence features. More broadly, RL-SAE could extend to other protein design settings where interpretable features provide useful design targets. Code is available at https://github.com/rotskoff-group/idiom.

### Key Innovations

- Intrinsically disordered protein regions (IDRs) play central roles in cellular processes such as transcriptional regulation, signal transduction, and subcellular localization, yet their functional design remains challenging.
- Structure-based design methods do not readily apply to IDRs, and existing protein language models are trained on full-length protein sequences, thus learning a prior that is biased towards folded domains.
- Here, we present IDiom, an autoregressive protein language model trained on IDiom-DB, a dataset of 54 million predicted IDRs curated from the AlphaFold Database.

---

## 30. TACO: Ternary Absolute-max Column-wise One-sparse Optimizer for LLM Fine-Tuning

**arXiv:** [https://arxiv.org/abs/2610.02199v1](https://arxiv.org/abs/2610.02199v1)
**Primary category:** 
**Authors:** Jichao Jiang; Cristian McGee; El Houcine Bergou; Hanqin Cai; Aritra Dutta
**Institution/Company:** _(not available from API)_

### Abstract

Full-parameter fine-tuning of large language models (LLMs) incurs substantial optimizer state memory overhead, limiting the model sizes that fit on modern GPUs. Existing approaches either compress optimizer state, abandon first-order gradients, or change the update geometry while retaining dense state. The recently introduced Muon optimizer reduces optimizer memory through matrix-valued updates. Still, its geometry differs from AdamW and can lead to performance degradation when fine-tuning AdamW-pretrained models. To reduce optimizer memory without sacrificing accuracy or computational efficiency in LLM fine-tuning, we propose Ternary Absolute-max Column-wise One-sparse optimizer, or TACO, which follows Muon's operator-norm steepest-descent view but takes the geometric route further. TACO computes the exact steepest-descent direction under a dimension-normalized $1\to1$ operator norm by selecting the sign of the largest magnitude entry in each column of two-dimensional weight matrices. This retains first-order gradients while making optimizer state memory nearly negligible. Our practical TACO optimizer maintains only a small set of low precision gradient components per column, reducing persistent optimizer state by $174\times$ relative to AdamW8bit (from 27.7 GB to 0.16 GB) and peak training memory by $2.9\times$ (from 80.6 GB to 27.5 GB) on OPT-13B, while achieving comparable accuracy and runtime. TACO further enables full-parameter fine-tuning of 30-32B-parameter models on a single 80 GB H100 GPU across multiple model families and tasks.

### Key Innovations

- Full-parameter fine-tuning of large language models (LLMs) incurs substantial optimizer state memory overhead, limiting the model sizes that fit on modern GPUs.
- Existing approaches either compress optimizer state, abandon first-order gradients, or change the update geometry while retaining dense state.
- The recently introduced Muon optimizer reduces optimizer memory through matrix-valued updates.

---

## 31. DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation

**arXiv:** [https://arxiv.org/abs/2610.02188v1](https://arxiv.org/abs/2610.02188v1)
**Primary category:** 
**Authors:** Zhengming Yu; Junkun Yuan; Haotian Yang; Gordon Guocheng Qian; Yizhi Wang; Angtian Wang; Yiding Yang; Bo Liu; Xin Li; Wenping Wang; Chongyang Ma
**Institution/Company:** _(not available from API)_

### Abstract

Distribution Matching Distillation (DMD) trains a few-step student from the difference between separately estimated target and student scores, so it must keep an auxiliary diffusion model fitted to the student's evolving distribution at extra memory and computation cost. We introduce DMAD, Distribution Matching as Adversarial Distillation, which recasts distribution matching as classification and learns the required log-density ratios directly. Two discriminator heads on a shared backbone distinguish real data and teacher samples from the student's, and linear losses on their logits train the student without auxiliary score fitting. We prove that at the discriminator optimum these losses recover the distribution-matching gradient underlying DMD, through the classical identity linking discriminator logits to log-density ratios. We further introduce gap-based reweighting, which adapts teacher supervision across noise levels from the real-data head's empirical logit gap between real and teacher samples. DMAD reaches a Fréchet Inception Distance (FID) of 1.04 with one-step generation on ImageNet-64x64, 14.47 with four-step SDXL on COCO-10K, and a VBench total score of 85.15 with four-step Wan2.1-T2V-14B, the best values among the compared few-step methods and the multi-step teachers. On MiniMax-H3-33B, our four-step student achieves overall human preference rates of 79.1% over DMD2 and 84.6% over rCM for joint audio-video generation, excluding ties. Our code, models and demos are available at https://yzmblog.github.io/projects/DMAD.

### Key Innovations

- Distribution Matching Distillation (DMD) trains a few-step student from the difference between separately estimated target and student scores, so it must keep an auxiliary diffusion model fitted to the student's evolving distribution at extra memory and computation cost.
- We introduce DMAD, Distribution Matching as Adversarial Distillation, which recasts distribution matching as classification and learns the required log-density ratios directly.
- Two discriminator heads on a shared backbone distinguish real data and teacher samples from the student's, and linear losses on their logits train the student without auxiliary score fitting.

---

## 32. Full-bandwidth transformer

**arXiv:** [https://arxiv.org/abs/2608.08888v2](https://arxiv.org/abs/2608.08888v2)
**Primary category:** 
**Authors:** Xi Wang; Ziyang Cai; Zheng Zhan; Harry Dong; Ying Fan; Gustavo de Rosa; Tim Pearce; John Langford
**Institution/Company:** _(not available from API)_

### Abstract

Autoregressive transformers compute along two axes: horizontally across generated tokens, and vertically through model depth. Dense attention gives each token broad horizontal access to the past, but the vertical feedback channel between decoding steps remains narrow: only the sampled token returns to the bottom of the stack, while the top-layer hidden state is discarded. We introduce the full-bandwidth transformer, which widens this channel with latent feedback: at each decoding step, the previous top-layer hidden state is fused with the sampled token embedding through a gated linear unit and fed back as the next input. Latent feedback lets non-verbalized computation re-enter the stack with a renewed depth budget, while preserving the standard transformer architecture, KV cache, and language-modeling objective. To train full-bandwidth transformers without losing parallel teacher forcing, we use a scheduled multi-pass objective that introduces latent feedback late in pretraining and mixes a small fraction of deeper feedback passes for stability. We train 1B-parameter full-bandwidth transformers on up to 400B tokens and find that latent feedback improves validation loss, 5-shot language-model evaluation, math and coding generation, and instruction-tuned performance. With negligible per-token decoding overhead, full-bandwidth transformers match or approach standard transformers trained with roughly 1.5x more tokens, and manage to produce shorter reasoning when no off-policy templates are provided.

### Key Innovations

- Autoregressive transformers compute along two axes: horizontally across generated tokens, and vertically through model depth.
- Dense attention gives each token broad horizontal access to the past, but the vertical feedback channel between decoding steps remains narrow: only the sampled token returns to the bottom of the stack, while the top-layer hidden state is discarded.
- We introduce the full-bandwidth transformer, which widens this channel with latent feedback: at each decoding step, the previous top-layer hidden state is fused with the sampled token embedding through a gated linear unit and fed back as the next input.

---

## 33. SWE-chat: Coding Agent Interactions From Real Users in the Wild

**arXiv:** [https://arxiv.org/abs/2604.20779v2](https://arxiv.org/abs/2604.20779v2)
**Primary category:** 
**Authors:** Joachim Baumann; Vishakh Padmakumar; Xiang Li; John Yang; Diyi Yang; Sanmi Koyejo
**Institution/Company:** _(not available from API)_

### Abstract

AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice. We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild. The dataset currently contains almost 18,000 sessions, comprising more than 229,000 user prompts and 2 million agent tool calls. SWE-chat is a living dataset; our collection pipeline automatically and continually discovers and processes sessions from public repositories. Leveraging SWE-chat, we provide an initial empirical characterization of real-world coding agent usage and failure modes. We find that coding patterns are bimodal: in 41% of sessions, agents author virtually all committed code ("vibe coding"), while in 25%, humans write all code themselves. Despite rapidly improving capabilities, coding agents remain inefficient in natural settings. Only 59% of all agent-produced code survives into user commits, and agent-written code introduces more security vulnerabilities than code authored by humans. Furthermore, users push back against agent outputs - through corrections, failure reports, and interruptions - in 50% of all turns. By capturing complete interaction traces with human vs. agent code authorship attribution, SWE-chat provides an empirical foundation for moving beyond curated benchmarks towards an evidence-based understanding of how AI agents perform in real developer workflows.

### Key Innovations

- AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice.
- We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild.
- The dataset currently contains almost 18,000 sessions, comprising more than 229,000 user prompts and 2 million agent tool calls.

---

## 34. Hierarchical Continuous Diffusion Language Models

**arXiv:** [https://arxiv.org/abs/2610.02193v1](https://arxiv.org/abs/2610.02193v1)
**Primary category:** 
**Authors:** Hui Ren; Zihan Li; Chang Liu; Huidong Liu; Alexander Schwing
**Institution/Company:** _(not available from API)_

### Abstract

Discrete diffusion language models offer a compelling alternative to autoregressive generation for tasks demanding bidirectional reasoning and global constraint satisfaction. Yet they share a structural bottleneck: when decoding in parallel, each token is sampled independently from its marginal, severing the statistical dependencies among the tokens decoded together. Continuous diffusion language models avoid this by denoising a shared continuous state, but their denoiser sees only that state, so nothing ties it to a valid token configuration until it is finally decoded. To address this, we propose Hierarchical Continuous Diffusion Language Models (HC-DLM), which couple discrete token generation with a continuous latent trajectory in a single, principled denoising process, whose training objective is derived from a variational bound on the token likelihood. In contrast to recent methods that attach continuous context to a self-contained discrete chain, HC-DLM makes the latent the only persistent generative state: tokens are read out from it at every step and feed back as a scaffold for the next latent update. On structured reasoning (Sudoku), mathematical planning (Countdown) and language modeling (LM1B), HC-DLM improves over discrete and continuous diffusion baselines at matched model size, in puzzle accuracy on Sudoku and Countdown and in generative perplexity on LM1B. Project page: https://hc-dlm.github.io/.

### Key Innovations

- Discrete diffusion language models offer a compelling alternative to autoregressive generation for tasks demanding bidirectional reasoning and global constraint satisfaction.
- Yet they share a structural bottleneck: when decoding in parallel, each token is sampled independently from its marginal, severing the statistical dependencies among the tokens decoded together.
- Continuous diffusion language models avoid this by denoising a shared continuous state, but their denoiser sees only that state, so nothing ties it to a valid token configuration until it is finally decoded.

---

## 35. Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy Optimization

**arXiv:** [https://arxiv.org/abs/2610.02019v1](https://arxiv.org/abs/2610.02019v1)
**Primary category:** 
**Authors:** Guangyu Yang; Jingbiao Mei; Mingsheng Sun; Jinghong Chen; Yingtong Bu; Pengda Qin; Da Chen; Bill Byrne
**Institution/Company:** _(not available from API)_

### Abstract

The rapid growth of video-based social media has increased users' exposure to harmful content, creating a need for reliable automated video safety detection. Although recent Vision-Language Models (VLMs) show strong video understanding capabilities, existing harmful video detection systems face two key limitations: they typically reduce safety detection to binary classification, overlooking the inherently multi-label nature of unsafe videos, and they rely on static training objectives that do not support controllable precision-recall trade-offs, though the desired operating point may vary across moderation pipelines and unsafe categories. To address these gaps, we propose Adaptive Tversky Policy Optimization (ATPO), a reinforcement learning framework for Multi-label Video Safety Detection (Multi-VSD). ATPO introduces the Adaptive Tversky Reward (ATR), which dynamically adjusts false-positive and false-negative penalties during training to enable controllable precision-recall trade-offs. Experiments on SafeWatch-Bench and XD-Violence show that ATPO substantially improves multi-label performance, increasing the Jaccard Index from 40.66 to 75.44 on SafeWatch-Bench-Real. Moreover, ATR enables reliable steering of the precision-recall operating point, supporting deployment scenarios with heterogeneous policy requirements. Code and checkpoints are provided at https://bruceyg.github.io/ATPO-project-page/ .

### Key Innovations

- The rapid growth of video-based social media has increased users' exposure to harmful content, creating a need for reliable automated video safety detection.
- Although recent Vision-Language Models (VLMs) show strong video understanding capabilities, existing harmful video detection systems face two key limitations: they typically reduce safety detection to binary classification, overlooking the inherently multi-label nature of unsafe videos, and they rely on static training objectives that do not support controllable precision-recall trade-offs, though the desired operating point may vary across moderation pipelines and unsafe categories.
- To address these gaps, we propose Adaptive Tversky Policy Optimization (ATPO), a reinforcement learning framework for Multi-label Video Safety Detection (Multi-VSD).

---

## 36. InterviewSim: A Scalable Framework for Interview-Grounded Personality Simulation

**arXiv:** [https://arxiv.org/abs/2602.20294v2](https://arxiv.org/abs/2602.20294v2)
**Primary category:** 
**Authors:** Yu Li; Pranav Narayanan Venkit; Yada Pruksachatkun; Chien-Sheng Wu
**Institution/Company:** _(not available from API)_

### Abstract

Simulating real personalities with large language models requires grounding generation in authentic personal data. Existing evaluation approaches rely on demographic surveys, personality questionnaires, or short AI-led interviews as proxies, but lack direct assessment against what individuals actually said. We address this gap with an interview-grounded evaluation framework for personality simulation at a large scale. We extract over 671,000 question-answer pairs from 23,000 verified interview transcripts across 1,000 public personalities, each with an average of 11.5 hours of interview content. We propose a multi-dimensional evaluation framework with four complementary metrics measuring content similarity, factual consistency, personality alignment, and factual knowledge retention. Through systematic comparison, we find that interview grounding yields consistent gains in content alignment and exact-match factual recall over biographical profiles and parametric prompting. We further find complementary strengths: retrieval-augmented methods tend to preserve personality alignment, while larger chronological contexts generally reduce contradictions and improve factual recall. Our evaluation framework enables principled method selection based on application requirements, and our empirical findings provide actionable insights for advancing personality simulation research.

### Key Innovations

- Simulating real personalities with large language models requires grounding generation in authentic personal data.
- Existing evaluation approaches rely on demographic surveys, personality questionnaires, or short AI-led interviews as proxies, but lack direct assessment against what individuals actually said.
- We address this gap with an interview-grounded evaluation framework for personality simulation at a large scale.

---

## 37. From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation

**arXiv:** [https://arxiv.org/abs/2610.02179v1](https://arxiv.org/abs/2610.02179v1)
**Primary category:** 
**Authors:** Siqi Zhu; Suozhi Huang; Kaixuan Zhang; Yuheng Yang; Zhanyang Jin; Yihang Sun; Jiaxuan You
**Institution/Company:** _(not available from API)_

### Abstract

Multi-teacher on-policy distillation (MOPD) aims to combine the strengths of RL-trained teachers in a single student, but how teacher signals affect parameter changes remains underexplored. We study Qwen3-1.7B with four domain teachers trained with RL from the same initialization as the student, comparing gradients, optimizer updates, and task learning curves, with additional SmolLM3-3B diagnostics. We find that several factors influence teacher signals. First, loss averaging implicitly weights responses: token averaging favors longer responses, and equalizing domain contributions retains this weighting within domains. Second, Adam's first moment reduces differences in parameter updates: the cosine similarity is 0.83 between teachers and 0.96 between averaging rules, despite differences in raw gradients. Third, BF16 rounding hides small changes: about 97\% of FP32 master weights differ from initialization, but only 7--11\% of BF16 weights do. Finally, the top-64 intersection KL gradient closely matches Qwen's full-vocabulary gradient, but the effect on task performance depends on averaging: mathematics accuracy is 2.6 points higher than with sampled-token policy-gradient (PG) under response averaging and 2.1 points lower under global token averaging.

### Key Innovations

- Multi-teacher on-policy distillation (MOPD) aims to combine the strengths of RL-trained teachers in a single student, but how teacher signals affect parameter changes remains underexplored.
- We study Qwen3-1.7B with four domain teachers trained with RL from the same initialization as the student, comparing gradients, optimizer updates, and task learning curves, with additional SmolLM3-3B diagnostics.
- We find that several factors influence teacher signals.

---

## 38. Optimizing Effective Training Time for Large-Scale Recommendation Systems

**arXiv:** [https://arxiv.org/abs/2610.02057v1](https://arxiv.org/abs/2610.02057v1)
**Primary category:** 
**Authors:** Mingming Ding; Ruilin Chen; Yuzhen Huang; Hang Qi; Menglu Yu; San Tan; Damian Reeves; Boris Sarana; Kevin Tang; Satendra Gera; Gagan Jain; Sahil Shah; Vishwa Karia; Fuzail Khan; Yashasvi Makin; Edward Z. Yang; Oguz Ulgen; Jia Chen Ren; Laith Sakka; Mayank Garg; Meet Vadakkanchery; Aici Lin; Wei Sun; Mengjiao Zhou; Shuai Yang; Junqing Zhou; Max Leung; Apoorv Purwar; Musharaf Sultan; John Bocharov; Zhenyu Tang; Vivek Trehan
**Institution/Company:** _(not available from API)_

### Abstract

Lifecycle overhead silently consumes accelerator capacity across large-scale recommendation training fleets. Our largest recommendation workloads process tens of billions train- ing examples per day on thousands of GPUs. Before this work, only 50-60% of their end-to-end wall time advanced training on new data. We present a fleet-scale study of this lifecycle overhead and a set of optimizations spanning the full training stack. We use Effective Training Time (ETT%) as an operational framework to instrument lost time, localize it to independently owned infrastructure components, and expose work repeated across job restarts. This analysis guides optimizations like communication elimination and pipeline overlap during trainer initialization; dynamic-shape handling, autotuning pruning, and reusable Py- Torch 2 compilation caches; asynchronous checkpointing; stan- dalone model publishing; and reductions in recovery cost. We evaluate the optimizations on representative models and measure their impacts in our training fleet. ETT% improves on every benchmark, by 15.5% on average, and reaches 85% on our largest workload. Fleet-wide ETT% rose from about 80% to above 90% after deployment.

### Key Innovations

- Lifecycle overhead silently consumes accelerator capacity across large-scale recommendation training fleets.
- Our largest recommendation workloads process tens of billions train- ing examples per day on thousands of GPUs.
- Before this work, only 50-60% of their end-to-end wall time advanced training on new data.

---

## 39. Cost-augmented Schrödinger bridges on graphs are exactly solvable: a Feynman-Kac tilt replaces learned control

**arXiv:** [https://arxiv.org/abs/2610.02195v1](https://arxiv.org/abs/2610.02195v1)
**Primary category:** 
**Authors:** Akshay Balsubramani
**Institution/Company:** _(not available from API)_

### Abstract

The generalized Schrödinger bridge on a graph moves mass between two distributions while charging a cost for the states visited. It has been approached by learning the rates of a controlled continuous-time Markov chain, with a temporal-difference penalty that restores the cost. A state cost folds into the reference process as a Feynman-Kac tilt. The cost-augmented bridge is then a plain bridge against the tilted reference, and the penalty is unnecessary. The bridge is computed exactly by alternating two endpoint rescalings, each one sparse matrix-exponential application; nothing is discretized in time or learned. The alternation converges at a rate set by the endpoint coupling alone. For a quadratic congestion cost on time-averaged occupancies, damped best response around the exact bridge is gradient descent on a strongly convex function, and its residual bounds its error. On a protein-folding model, a free-energy cost lowers the expected barrier of the folding paths. On the learned approach's road network, roll-outs of the exact bridge match the target within sampling error, and on networks with millions of intersections its memory grows linearly.

### Key Innovations

- The generalized Schrödinger bridge on a graph moves mass between two distributions while charging a cost for the states visited.
- It has been approached by learning the rates of a controlled continuous-time Markov chain, with a temporal-difference penalty that restores the cost.
- A state cost folds into the reference process as a Feynman-Kac tilt.

---

## 40. When Do Intrinsic Rewards Lead to Exploration?

**arXiv:** [https://arxiv.org/abs/2610.02159v1](https://arxiv.org/abs/2610.02159v1)
**Primary category:** 
**Authors:** Scott W. Viteri; Laura Gomezjurado Gonzalez; Clark Barrett
**Institution/Company:** _(not available from API)_

### Abstract

Intrinsic rewards are designed to guide exploration in reinforcement learning by assigning value to an agent's experience, for example through prediction error or learning progress. However, maximizing these rewards need not produce the most informative experience available. We propose a formal criterion for exploration that compares policies by the counterfactual information they acquire: how well their histories can substitute for experience under alternative policies. We construct a single, simple environment in which specified count-based, prediction-error, empowerment, and information-gain objectives have maximizing policies that are Pareto-suboptimal at acquiring counterfactual information. We explain these failures and establish conditions under which existing intrinsic rewards successfully encourage optimal exploration. We also construct an objective that assigns a higher value whenever exploration strictly improves under our criterion.

### Key Innovations

- Intrinsic rewards are designed to guide exploration in reinforcement learning by assigning value to an agent's experience, for example through prediction error or learning progress.
- However, maximizing these rewards need not produce the most informative experience available.
- We propose a formal criterion for exploration that compares policies by the counterfactual information they acquire: how well their histories can substitute for experience under alternative policies.

---
