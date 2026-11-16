# arXiv Daily — Recent Papers in AI, LLMs, Agents, and Related Areas

- **Date:** 2026-11-16
- **Scope:** Recent arXiv submissions/papers (queried 2026-11-16 via arXiv Export API, sorted by submitted date) across AI, LLMs, reasoning, agents/memory, multimodal models, and sequential decision-making. Requested areas included recommendation, advertising, sequential modeling, CTR, and games; targeted keyword API queries for those niches hit arXiv rate limits (HTTP 429) during this run, so this digest emphasizes the most relevant recent results retrieved from `cs.CL/cs.LG` and `cs.IR/cs.AI` feeds plus closely related agent/world-modeling work.
- **Data sources:** arXiv Atom API responses from `cat:cs.CL+OR+cat:cs.LG` and `cat:cs.IR+OR+cat:cs.AI` (max_results=12 each, submittedDate desc). Affiliations are taken from arXiv metadata when provided; otherwise marked as not specified.

---

## 1. Unbundling Multimodal Vision Encoding

- **arXiv:** [2611.17334v1](https://arxiv.org/abs/2611.17334v1) ([PDF](https://arxiv.org/pdf/2611.17334v1))
- **Submitted:** 2026-11-12
- **Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu
- **Institution / Company:** Not specified in arXiv metadata (project page: https://unbundling.github.io)
- **Categories:** cs.CV, cs.LG

**Abstract**
> How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e., before the multimodal backbone). Because published models also differ in data, architecture, and compute, comparing them cannot isolate the effect of each choice. We disentangle these choices via a controlled framework where we pretrain all models from scratch on common data and compare them on visual question answering and language benchmarks at matched lifetime compute. We find that the visual prior is not necessary; an encoder trained jointly from scratch is on par with a pretrained one, without a separate training stage. What matters instead is dedicated vision capacity: an encoder-free model trails on visual understanding even when its backbone is enlarged by the encoder's parameter count. Yet that capacity need not precede multimodal fusion, as vision-only modules added in-fusion to early backbone layers perform comparably to a pre-fusion encoder and can lower time to first token. These results also hold across backbone sizes, when encoder pretraining is treated as free, and when starting from a pretrained language model. Overall, our findings favor dedicated vision capacity trained jointly with the backbone and placed early within it.

**Key innovations**
- Controlled “unbundling” framework that isolates three vision-encoder design choices: visual prior (pretraining), dedicated vision capacity, and pre-fusion vs in-fusion placement, under matched data/compute.
- Shows pretrained visual priors are not necessary when encoders are trained jointly from scratch, challenging the default reliance on separate vision pretraining.
- Identifies dedicated vision capacity as the critical factor for visual understanding; encoder-free backbones underperform even when scaled up by encoder parameter count.
- Demonstrates that in-fusion vision-only modules in early backbone layers can match pre-fusion encoders and reduce time-to-first-token, suggesting flexible placement of vision capacity.

---

## 2. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research

- **arXiv:** [2611.17332v1](https://arxiv.org/abs/2611.17332v1) ([PDF](https://arxiv.org/pdf/2611.17332v1))
- **Submitted:** 2026-11-12
- **Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
- **Institution / Company:** Not specified in arXiv metadata
- **Categories:** cs.CL, cs.LG

**Abstract**
> Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult to establish whether improvements hold at larger scales or translate into broader impact. ArchSpace addresses both gaps as a public platform for Recording, Reviewing, and Referencing Architecture Researc}: each proposal is recorded with its experiments and reasoning, reviewed by the community, and referenced by later work. To evaluate ideas before costly large-scale training, ArchSpace leverages scaling laws to predict model loss at larger scales from smaller experiments, a practice widely adopted in industry. We provide initial references that make the platform usable: Qwen3.5 and OLMo3 baselines, fitted scaling laws, and a reusable training recipe. Ideas validated through this review can in turn become new baselines, and ArchSpace thereby aims to broaden the range of ideas that shape the next generation of models.

**Key innovations**
- Proposes ArchSpace, a public “record–review–reference” platform to document LLM architecture experiments, including negative results and rationale often missing from industry reports.
- Uses scaling-law extrapolation from small experiments to pre-screen architecture ideas before expensive large-scale training, bridging academic compute constraints and industrial practice.
- Seeds the platform with reusable references (Qwen3.5/OLMo3 baselines, fitted scaling laws, training recipes) to standardize comparisons and enable cumulative architecture research.

---

## 3. Learning When Diffusion Language Models Should Regenerate

- **arXiv:** [2611.17320v1](https://arxiv.org/abs/2611.17320v1) ([PDF](https://arxiv.org/pdf/2611.17320v1))
- **Submitted:** 2026-11-12
- **Authors:** Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, Minsik Seol, Jungwoo Lee
- **Institution / Company:** Not specified in arXiv metadata
- **Categories:** cs.CL

**Abstract**
> Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error usually reproduces it when the surrounding context remains fixed. These findings motivate DiVR , a verifier that predicts whether a partially generated sequence will reach a correct answer. Trained on the final correctness of the model's own trajectories, DiVR decides when to regenerate a block and which alternative to retain, while the generator itself stays unchanged. On five reasoning benchmarks with LLaDA-8B-Base, DiVR raises the average accuracy of the fine-tuned generator from 35.3% to 43.4% at $1.9$-$3.5\times$ the cost of greedy decoding, above search baselines that use $3.8$-$7.4\times$. It also complements post-training such as supervised fine-tuning and reinforcement learning, and generalizes to other generators, including Dream.

**Key innovations**
- Diagnoses diffusion LM remasking failures: token confidence can miss errors encoded in hidden states, and isolated remasking often reproduces mistakes when context is fixed.
- Introduces DiVR, a trajectory-correctness verifier trained on the generator’s own rollouts to decide *when* to regenerate a block and *which* alternative to keep without changing generator weights.
- Improves reasoning accuracy/cost trade-off on LLaDA-8B-Base (35.3%→43.4% avg at 1.9–3.5× greedy cost) and composes with SFT/RL while generalizing to other diffusion generators (e.g., Dream).

---

## 4. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation

- **arXiv:** [2611.17316v1](https://arxiv.org/abs/2611.17316v1) ([PDF](https://arxiv.org/pdf/2611.17316v1))
- **Submitted:** 2026-11-12
- **Authors:** Peiwen Li (Yale University), Harshit Verma (Yale University), Sophia Zhou (Yale University), Haiwen Wang (Yale University), Ngoc Bui (Yale University), Heng Chang (Tsinghua University), Fei Fei (Goodvision AI), David van Dijk (Yale University), Rex Ying (Yale University)
- **Institution / Company:** Yale University; Tsinghua University; Goodvision AI (per-author affiliations from arXiv metadata)
- **Categories:** cs.AI, cs.CL, cs.SE

**Abstract**
> Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memory saves effort as the task unfolds. We introduce Coding-Repository Memory (CoReMem), a cost-internalizing framework that guides memory design and actor adaptation through measured memory value on the next task. Prospective segment valuation compares runs of the next task with and without individual trajectory segments from the same inherited repository state, guiding a compact memory built around anchors: repository locations and executable checks. Actor adaptation estimates on-policy memory value within rollout groups with and without memory, using a reward that prioritizes resolution and penalizes step count in successful runs. Provenance-gated value credit assigns the additional value term to steps identified as using memory-supplied anchors, while every step retains outcome credit. On ChainSWE, CoReMem raises the 27B actor's resolve rate from 21.0% to 25.7%, with 17% fewer steps and 11% fewer total cache-aware tokens, including memory-module calls, relative to the untrained actor model without memory.

**Key innovations**
- Frames agent memory for *successive/sequential* repository tasks as a cost–value trade-off, explicitly internalizing write/read costs against future usefulness on unknown next tasks.
- Prospective segment valuation measures counterfactual memory value by comparing next-task runs with/without trajectory segments, producing compact “anchor” memories (repo locations + executable checks).
- Provenance-gated on-policy credit assigns extra reward to steps that actually use memory-supplied anchors, improving resolve rate while reducing steps and cache-aware token usage on ChainSWE.

---

## 5. AgentSSL: Can MLE Agents Leverage Unlabeled Data?

- **arXiv:** [2611.17323v1](https://arxiv.org/abs/2611.17323v1) ([PDF](https://arxiv.org/pdf/2611.17323v1))
- **Submitted:** 2026-11-12
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **Institution / Company:** Not specified in arXiv metadata
- **Categories:** cs.AI, cs.LG
- **Notes:** NeurIPS 2026 (per arXiv comment); project: https://codiscovery.ai/AgentSSL

**Abstract**
> Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested in realistic regimes where labeled data is scarce but unlabeled data is abundant. In this work, we introduce Agentic Semi-Supervised Learning (AgentSSL), framing SSL as a program search problem and studying how agents navigate this space under limited supervision. We find that even under weak feedback and matched compute, agents can synthesize code that combines and adapts established SSL techniques, exceeding the strongest human-engineered baselines in 8 of 12 settings by up to +21.8%. However, our results identify program selection as a critical bottleneck in AgentSSL, where performance drops by as much as 47% when selecting based on the agent's feedback metric. To systematically study this bottleneck, we introduce ProgramSelectBench, a large-scale benchmark with a combined total of 16,977 agent-generated and human-engineered SSL programs, and evaluate both unsupervised and active program selection methods. We further evaluate AgentSSL on real-world ecology detection tasks, highlighting the opportunities and challenges of transferring agent-discovered strategies beyond controlled benchmarks.

**Key innovations**
- Formulates agentic semi-supervised learning (AgentSSL) as program search, testing MLE agents in label-scarce/unlabeled-abundant regimes rather than fully supervised settings.
- Shows agents can compose and adapt SSL techniques to beat strong human baselines in 8/12 settings (up to +21.8%) under weak feedback, while exposing program selection as a major bottleneck (up to 47% drop).
- Introduces ProgramSelectBench (16,977 agent- and human-generated SSL programs) to study unsupervised/active selection and evaluates transfer to real-world ecology detection tasks.

---

## 6. Sketching Language Models for Context Attribution

- **arXiv:** [2611.17313v1](https://arxiv.org/abs/2611.17313v1) ([PDF](https://arxiv.org/pdf/2611.17313v1))
- **Submitted:** 2026-11-12
- **Authors:** Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Felix Zhou
- **Institution / Company:** Not specified in arXiv metadata
- **Categories:** cs.DS, cs.AI, cs.LG, stat.ML

**Abstract**
> Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using $O(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ evaluation calls. To complement our upper bound, we prove a matching $Ω(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ lower bound on the number of evaluation calls in an oracle model. Empirically, we verify coefficient decay consistent with stability and evaluate the performance of our sketching algorithm on a small language-model retrieval task.
> Technically, our result is based on a sketching algorithm for arithmetic circuits whose Taylor coefficients satisfy the stability condition recently introduced by Gunn [Gun26]. A direct adaptation of their forward differentiation sketches would require $\widetilde{O}(\log(n)/\varepsilon^2)$ evaluation calls. Our key observation is that we can apply forward differentiation to the backpropagation circuit, with only constant overhead over a forward sketch of the same Taylor degree. This reduces the variance of the sketches and is key to our improved evaluation bound. Our lower bound builds on the techniques of Amsel, Chen, Duman Keles, Halikias, Musco, and Musco [ACDH+26, SIAM Journal on Matrix Analysis and Applications] for lower bounding the number of matrix-vector queries to estimate the diagonal elements of random matrices.

**Key innovations**
- Provides near-optimal algorithms for LLM context/leave-one-out attribution: $O(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ model evaluations with a matching lower bound under a stability assumption.
- Technical advance applies forward differentiation to the *backpropagation* circuit (not just forward sketches), reducing variance and improving over direct $\widetilde{O}(\log(n)/\varepsilon^2)$ adaptations.
- Connects prompt-attribution efficiency to sketching/Taylor-coefficient stability theory, with empirical checks of coefficient decay and a retrieval-task evaluation.

---

## 7. Classical Energies Learn to Reason 1,000x Faster than Looped Models

- **arXiv:** [2611.17309v1](https://arxiv.org/abs/2611.17309v1) ([PDF](https://arxiv.org/pdf/2611.17309v1))
- **Submitted:** 2026-11-12
- **Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **Institution / Company:** Not specified in arXiv metadata
- **Categories:** cs.AI, cs.LG

**Abstract**
> Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigates these issues but also offers advantages: built-in early stopping, compute that adapts to problem difficulty, fast training without differentiating through a solver, and interpretable weights that learn the constraints of the puzzle. Here we demonstrate this with a learned version of Hopfield &amp; Tank's energy from the 80s, which we term CRAM, solves 99.996% of Sudoku-Extreme and 100% of Maze-Unique test puzzles after 42 ms and 132 ms of training on one GPU, at least 1,000x faster than looped models on these tasks. CRAM also matches baseline looped models at their highest accuracy on Sudoku-Extreme using at least 282x fewer inference FLOPs. Our work suggests two things. First, that energies are an extremely promising direction for training reasoning from data. Second, a caution against using trivially solvable benchmarks like Sudoku and Maze to test the scalability of looped reasoning techniques.

**Key innovations**
- Revisits classical Hopfield–Tank-style energy minimization (CRAM) as a learned reasoning method, contrasting with contemporary looped/iterative neural reasoning models.
- Achieves very fast training (ms-scale on one GPU) and strong puzzle accuracy with large efficiency gains (≥1,000× faster training, ≥282× fewer inference FLOPs in matched-accuracy settings) plus adaptive compute/early stopping.
- Argues for energy-based reasoning as a promising direction while cautioning that Sudoku/Maze-style benchmarks may be insufficient to validate scalability claims of looped reasoning.

---

## 8. LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds

- **arXiv:** [2611.17267v1](https://arxiv.org/abs/2611.17267v1) ([PDF](https://arxiv.org/pdf/2611.17267v1))
- **Submitted:** 2026-11-12
- **Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, Shengqiong Wu, Hao Fei, Mong-Li Lee, Wynne Hsu
- **Institution / Company:** Not specified in arXiv metadata
- **Categories:** cs.AI

**Abstract**
> We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed geographic states, GeoWorld is grounded in real-world geographic structure and allows external world states to evolve along their own temporal processes while preserving verifiable state histories. LiveGeo places geographic tasks within this evolving environment, requiring agents to actively acquire task-relevant information, verify whether the evidence supporting prior decisions remains valid, and revise their plans when necessary. Our results reveal that even frontier LLMs struggle with static tasks, with no model consistently excelling across tasks, while strong static performance does not ensure dynamic reliability. Further analysis identifies a key bottleneck: agents struggle to acquire and translate relevant evidence into valid decisions and maintain their correctness as the world evolves. By releasing LiveGeo together with its GeoWorld platform, we aim to provide the community with a flexible and extensible infrastructure for studying the next generation of agents capable of reliable action in evolving geographic worlds.

**Key innovations**
- Introduces GeoWorld, a controllable platform with real-world geographic grounding and temporally evolving states with verifiable histories, moving beyond static environment evaluations.
- Proposes LiveGeo benchmark requiring agents to acquire evidence, re-verify decision validity over time, and revise plans under world evolution—stressing sequential/temporal reliability.
- Finds static benchmark success does not guarantee dynamic reliability for frontier LLM agents, pinpointing evidence acquisition/translation and maintenance under change as core bottlenecks.

---

## 9. Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation

- **arXiv:** [2611.17329v1](https://arxiv.org/abs/2611.17329v1) ([PDF](https://arxiv.org/pdf/2611.17329v1))
- **Submitted:** 2026-11-12
- **Authors:** Zeynep Yıldız, Satchit Chatterji, Ercan Atam, Erman Acar
- **Institution / Company:** Not specified in arXiv metadata
- **Categories:** cs.LG
- **Notes:** Accepted at ICAIF '26 (per arXiv comment)

**Abstract**
> Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuitable for real-world deployment. Existing neurosymbolic methods such as Probabilistic Logic Policy Gradient (PLPG) offer constraint-satisfying reinforcement learning (RL) via differentiable symbolic supervision but assume a finite, discrete action space. We present a PLPG-inspired continuous allocation method that estimates the probability that the policy's own executed action satisfies the investment mandate, using reparameterized Monte Carlo sampling, and adds it to the training objective. No post-hoc enforcement mechanism intercepts actions at inference time and compliance is learned by the agent. Audited directly on deterministic mean actions with no correction, the policy reduces violations of a six-rule regime-conditional mandate from 96-98% for unconstrained RL and 33.4% for a reward-penalty baseline to 4.8%, showing that a continuous-action neurosymbolic policy can substantially internalize a symbolic mandate.

**Key innovations**
- Extends neurosymbolic constraint-satisfying RL (PLPG-style) to continuous portfolio allocation actions, addressing a key limitation of discrete-action symbolic supervision methods.
- Uses reparameterized Monte Carlo sampling to estimate mandate-satisfaction probability of executed actions and trains compliance into the policy objective (no post-hoc action correction at inference).
- Demonstrates large compliance gains on regime-conditional investment rules (96–98% violations → 4.8%) versus unconstrained RL and reward penalties, relevant to sequential decision-making under constraints.

---

## Notes and limitations

- This is an automated snapshot from arXiv API metadata/abstracts on 2026-11-16; it is not a full literature review. Metrics and claims are as reported by authors in abstracts.
- Author affiliations are included only when present in arXiv metadata fields; many entries do not expose structured affiliations.
- Coverage of recommendation systems, CTR prediction, computational advertising, and game-playing RL was constrained in this run because targeted arXiv keyword queries were rate-limited (HTTP 429). Future runs can retry those queries or supplement with category-specific feeds (e.g., `cs.IR`, `cs.GT`, `cs.MA`) when available.
- No files were written outside the repository; temporary files (if any) are limited to `/private/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and should be removed after use.
