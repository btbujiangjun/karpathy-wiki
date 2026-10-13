# arXiv AI Search Report (2026-10-13)

Search query covers recent submissions (last ~30 days) across AI/ML/NLP/CV/IR/RecSys/Ads/Sequential/CTR/Games/DM/GT.

## AI (cs.AI)
Found 10 recent papers (top 10 shown).

### [Can Language Models Play the Wikipedia Game?](http://arxiv.org/abs/2610.13948v1)
- Authors: Alexander Hickey, Joanna Knight, James Bishop
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13948v1
- Categories: cs.AI, cs.IR
- Abstract: Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. In the game, players must reach a target article using only article links. We compared sentence embedding models and LLMs across five Wikipedia languages and five academic-literature datasets. We construct very large local graphs of Wikipedia pages and of paper citations using OpenAlex and provide code to build and navigate them. This allows the study of language models' navigation capabilities without relying on third-party APIs. We compared the models with human and TF-IDF benchmarks. The Wikip...

### [Hide and Seek: HIDE Concepts to SEEK explanations for black box models](http://arxiv.org/abs/2610.13935v1)
- Authors: Bhanu Tokas, Rahul Nair, Rockwell Jackson, Hannah Kerner
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13935v1
- Categories: cs.CV, cs.AI, cs.LG
- Abstract: Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that does not require access to model weights or labeled concept datasets. HnS can interpret a wide range of vision models. Given a concept and image set, HnS retrieves concept-aligned images using a vision-language model, localizes the concept within each image, masks the localized region, and measures...

### [Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early Stopping](http://arxiv.org/abs/2610.13909v1)
- Authors: Danil Rudenko, Georgii Bulgakov, Nikolay Kartashev, Ivan Rubachev, Daniil Krasylnikov, Artem Babenko
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13909v1
- Categories: cs.LG, cs.AI
- Abstract: While deep learning models for tabular data have recently received significant research attention, the choice of objective functions for regression tasks remains an understudied degree of freedom. Several lines of research offer alternatives to the standard Mean Squared Error (MSE), but differences in datasets, backbones, and evaluation protocols make their practical benefits difficult to compare. In this work, we address this gap by performing a systematic re-evaluation of regression objectives across a broad collection of established tabular datasets and multiple neural backbones. Our comparison reveals that many proposed objectives provide limited or inconsistent gains over a properly tuned MSE baseline, while quantile loss yields consistent aggregate improvements over MSE across the te...

### [Task Context Shapes Component Roles in Language Models](http://arxiv.org/abs/2610.13895v1)
- Authors: Sovesh Mohapatra, Dani S Bassett
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13895v1
- Categories: cs.CL, cs.AI
- Abstract: Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention heads and the activation state in later layers (influence), as well as the answer (importance). Task changes redistribute the influence in five open-weight models spanning four families and 1.5-14 billion parameters. In Gemma-2-9B and Qwen3-14B, an activation edit changes an early internal activatio...

### [RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](http://arxiv.org/abs/2610.13889v1)
- Authors: Weiliang Chen, Song Liao
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13889v1
- Categories: cs.AI, cs.IR
- Abstract: As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This design enables rapid adaptation to runtime tool failures without expensive model retraining. We introduce EcoAgent, a benchmark of 5,172 real-world tools and over 210,000 query-tool pairs for offline ...

### [X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](http://arxiv.org/abs/2610.13886v1)
- Authors: Yeonsung Jung, Zhiyuan Wang, Zifan Wang, Vítor Albiero, Benjamin Newman, Edoardo Debenedetti, Ivan Evtimov, Ninareh Mehrabi
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13886v1
- Categories: cs.AI
- Abstract: Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying these compositional failures requires systematically exploring diverse cross-service paths. Existing red-teaming methods often simply prompt LLMs to identify potentially harmful paths from task and environment descriptions or decompose harmful objectives specified by humans or LLMs into seemingly benign action combinations. However, generation is biased toward patterns learned during training, potentially favoring familiar tool combinations and leaving novel cross-service interactions underexplored. To address this, w...

### [Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga](http://arxiv.org/abs/2610.13840v1)
- Authors: Emilio Ferrara
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13840v1
- Categories: cs.AI, cs.CL, cs.CY
- Abstract: Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parses every scan into panels, text and a bibliographic record; annotates each page with a vision-language model that follows a written codebook, as a human coder would; grounds samples of these readings in human annotation; and explains change across an archive, with estimates controlled for publisher a...

### [SpatialASM: Internalizing Active Mentalization for Spatial Reasoning](http://arxiv.org/abs/2610.13832v1)
- Authors: Yuhong Liu, Shenxi Wu, Junyi Chi, Beichen Zhang, Xuanlang Dai, Jiaqi Wang, Yuhang Zang, Dahua Lin
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13832v1
- Categories: cs.CV, cs.AI
- Abstract: When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Large Vision-Language Models (LVLMs) proactively think in the same way? We term this ability Active Spatial Mentalization (ASM), an intrinsic component of visual intelligence that remains substantially underdeveloped in current LVLMs. To bridge this gap, we introduce SpatialASM, a scalable framework to internalize ASM into LVLMs through training-time spatial simulation. SpatialASM employs an allocentric novel-view generator to ground hypothetical viewpoints in visual evidence and produces two complementary forms of supervision: i) explicit ASM trajectories that teach LVLMs when and how to adaptiv...

### [MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents](http://arxiv.org/abs/2610.13829v1)
- Authors: Jingwei Song, Zhisheng Chen, Bingfan Zeng, Jing Tang, Yubo Hou, Jinhao Jing, Zhengwei Xie, Linfeng Zhang
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13829v1
- Categories: cs.RO, cs.AI
- Abstract: A central challenge in embodied recursive self-improvement is enabling agents to convert interaction history into capabilities that persist beyond one world and transfer to later tasks. A saved memory or successful final action does not by itself establish that a reusable capability was acquired; evaluation must separate capability change from carried-over resources, unequal source exposure, and early execution failures. We construct MC-EvoBench as a controlled Minecraft benchmark with a fixed catalog of 19 registered evolution chains, including 12 primary evaluation chains and seven calibration or probe chains, together with three graph-aligned paired probe families for transfer. The benchmark represents each task as a task-state graph, defines stage-level environment verifiers, assigns m...

### [Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing](http://arxiv.org/abs/2610.13823v1)
- Authors: Oktie Hassanzadeh, Dharmashankar Subramanian
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13823v1
- Categories: cs.DB, cs.AI
- Abstract: Semantic query engines ask a large language model (LLM) to judge individual rows, and benchmarks compare these engines on the quality of a few executions at temperature 0. We measure how much another execution changes. We re-execute the text and tabular workloads of SemBench, LRO-Bench, and UDA-Bench through their own harnesses, log every one of 1.2 million model calls, and reanalyze SemBench's published executions. At temperature 0, between 0.07% and 10.2% of rows change their operator output over five executions, depending on the model, and up to 24.0% on one task. Plans amplify these changes exponentially in the number of rows an answer exposes, as a possible-worlds model predicts: on UDA-Bench, a few percent of extracted values change, but about two thirds of the answers do. In SemBenc...

---

## ML (cs.LG)
Found 10 recent papers (top 10 shown).

### [Hide and Seek: HIDE Concepts to SEEK explanations for black box models](http://arxiv.org/abs/2610.13935v1)
- Authors: Bhanu Tokas, Rahul Nair, Rockwell Jackson, Hannah Kerner
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13935v1
- Categories: cs.CV, cs.AI, cs.LG
- Abstract: Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that does not require access to model weights or labeled concept datasets. HnS can interpret a wide range of vision models. Given a concept and image set, HnS retrieves concept-aligned images using a vision-language model, localizes the concept within each image, masks the localized region, and measures...

### [Constructive Bounds for the Topological Expressivity of Neural Networks](http://arxiv.org/abs/2610.13931v1)
- Authors: Kosio Beshkov
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13931v1
- Categories: math.AT, cs.LG
- Abstract: The expressivity of a neural network $Φ$ describes the class of functions that a network can express. The term topological expressivity refers to a family of measures particularly suited to understand binary classification and is often formulated in terms of the Betti numbers of a decision boundary $β(Φ^{-1}(0))$. Despite its popularity, this measure is not as useful for regression and other problems that do not involve a decision boundary. Instead, we propose to study topological expressivity in terms of the Betti numbers of the output of a neural network $β(Φ(X))$. We formally prove that a ReLU network with architecture $(d,\sum\limits_{k=1}^{d } β_k(3k+2),\sum\limits_{k=1}^{d}β_k(k+1))$ can express spaces homotopy equivalent to wedge sums of spheres with arbitrary Betti numbers. This gi...

### [AI Models Can Provably Hide Arbitrary Capabilities](http://arxiv.org/abs/2610.13928v1)
- Authors: Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13928v1
- Categories: cs.LG, cs.CR
- Abstract: Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and l...

### [KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling](http://arxiv.org/abs/2610.13924v1)
- Authors: Tianyi Wu
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13924v1
- Categories: cs.LG, cs.IT
- Abstract: A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$ with the output-law divergence $D_{\mathrm{KL}}(p\|\mathbb{E}_U q_U)$, in nats. Rounds commit independent draws from exact conditional marginals frozen at the round's start, each output's schedule is drawn before sampling from a finite mixture of schedules, and every scheduled round is charged. For the uniform distribution on binary strings of even length $n$ with $n/2$ ones, the least expected number of rounds at a fixed tolerance $\varepsilon>0$ is $Θ_\varepsilon((\log n)^2)$ under the first criterion but $(e^{-\varepsilon}+o(1))\log_2\ln ...

### [Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning](http://arxiv.org/abs/2610.13923v1)
- Authors: Sajjad Baghaeea, Aimin Lib, Shanmugarajan Balasubramanian, Elif Uysal
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13923v1
- Categories: cs.NI, cs.LG, eess.SY
- Abstract: Deep-space communications operate under intermittent connectivity, long propagation delays, and relay storage constraints. In such networks, the Bundle Protocol enables store-carry-forward communication, requiring relay nodes to manage limited storage and scarce contact opportunities. Relay-side scheduling and dropping decisions are inherently goal-oriented: transmission resources should be allocated to bundles most valuable to downstream mission objectives. Conventional schedulers, such as FIFO, do not explicitly optimize task utility and may provide unfair service across heterogeneous planetary sources. This paper presents a closed-loop modeling and learning framework for relay-side bundle and flow management in a contact-driven deep-space network, where lunar and Martian updates are for...

### [DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness](http://arxiv.org/abs/2610.13918v1)
- Authors: Daniel Szelogowski
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13918v1
- Categories: cs.NE, cs.ET, cs.LG, q-bio.NC
- Abstract: Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothalamic leaky integrate-and-fire spiking neural network. We formalize five clinical cohorts across an identical 72-hour photoperiod: healthy control, circadian rhythm sleep-wake disorder (delayed-phase), chronic insomnia, paradoxical insomnia, and narcolepsy type 1. The synthetic local field potential c...

### [Designing Protein Structures from Natural Language](http://arxiv.org/abs/2610.13917v1)
- Authors: Joseph Lee, Yanjing Li, Bo Qiang, Gregory Lau, Allyson Ettinger, Noah A. Smith, Rory Donovan-Maiye, David Baker, Hanna Hajishirzi, Pang Wei Koh
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13917v1
- Categories: cs.LG, q-bio.BM
- Abstract: A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support. We develop Prompteina, the first all-atom structure generation model that supports new and broader design objectives specified in natural language, analogous to text-to-image generation. To train Prompteina, we construct Prompteina-Data, a paired text--protein structure dataset of 1.8M structures and 50M+ captions describing global and residue-specific structural and functional properties. We adapt Proteina-Complexa, a pretrained structure generation model, through text-conditioned pretraining and finetuning that aligns residues with th...

### [Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early Stopping](http://arxiv.org/abs/2610.13909v1)
- Authors: Danil Rudenko, Georgii Bulgakov, Nikolay Kartashev, Ivan Rubachev, Daniil Krasylnikov, Artem Babenko
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13909v1
- Categories: cs.LG, cs.AI
- Abstract: While deep learning models for tabular data have recently received significant research attention, the choice of objective functions for regression tasks remains an understudied degree of freedom. Several lines of research offer alternatives to the standard Mean Squared Error (MSE), but differences in datasets, backbones, and evaluation protocols make their practical benefits difficult to compare. In this work, we address this gap by performing a systematic re-evaluation of regression objectives across a broad collection of established tabular datasets and multiple neural backbones. Our comparison reveals that many proposed objectives provide limited or inconsistent gains over a properly tuned MSE baseline, while quantile loss yields consistent aggregate improvements over MSE across the te...

### [Hitting-Time Bounds for Asynchronous Q-Learning](http://arxiv.org/abs/2610.13901v1)
- Authors: Yang Peng
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13901v1
- Categories: stat.ML, cs.LG
- Abstract: We study the last iterate of standard asynchronous Q-learning from a single trajectory of a finite Markov decision process. The trajectory follows a fixed behavior policy whose state--action chain is irreducible and may be periodic. For discount factor $γ$, write $H=(1-γ)^{-1}$, and let $μ_{\min}$ be the minimum stationary state--action probability and $\mathfrak h_\star$ the largest expected hitting time of the reverse state--action chain. We prove that zero-initialized Q-learning with a constant step size achieves sup-norm error at most $\varepsilon$ with high probability using $\widetilde{O}(H^4/(μ_{\min}\varepsilon^2)+\mathfrak h_\star)$ transitions, for $0<\varepsilon\le1$. The statistical term retains the quartic effective-horizon dependence of standard Q-learning, while initializati...

### [Prediction Is Not a Sufficient Memory State](http://arxiv.org/abs/2610.13881v1)
- Authors: Robert Jenkinson Alvarez
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13881v1
- Categories: cs.LG
- Abstract: A memory that reproduces every current prediction may still have forgotten how to learn from the next observation. We characterize this distinction for exact cumulative learning and attention. For smooth convex residual losses with unrestricted real features and labels, a continuous recurrent state of fixed dimension exists exactly when the loss is polynomial. With ordinary, unweighted observations, degree $D$ requires precisely $r=\binom{d+D}{D}-1$ coordinates; even among histories with one fixed current predictor, exactly $r-d$ coordinates can remain necessary for continuation. Nonpolynomial losses have unbounded requirements on such equal-prediction histories. Bounded scalar logistic examples retain this obstruction after fixing any finite derivative jet. For ridge regression, the hidde...

---

## NLP/CL (cs.CL)
Found 10 recent papers (top 10 shown).

### [RSI-Anything: Unlocking Recursive Self-Improvement with World Models](http://arxiv.org/abs/2610.13912v1)
- Authors: Taoyong Cui, Pinxian Zeng, Wanghan Xu, Hao Xiao, Shuhan Xue, Qiang Gao, Wanli Ouyang, Pheng Ann Heng, Zhenfei Yin, Yingcheng Wu, Ling Yang
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13912v1
- Categories: cs.CL
- Abstract: Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predictive world models to guide action and learning-data selection. Observed feedback drives policy or workflow improvement and conditional world-model adaptation, while component and compatibility checks govern the retention of updated policy-model pairs. Across diverse computational and scientific domains, RSI-Anything demonstrates substantial gains. In code repair, with the coder fixed, success increases from 26.3% with a static verifier to 29.2% through predictive selection and 31.2% after world-m...

### [When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors](http://arxiv.org/abs/2610.13910v1)
- Authors: Shubh Garg, Chen Shani
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13910v1
- Categories: cs.CL
- Abstract: Vision-Language Models (VLMs) increasingly analyze and reason about images, yet it remains unclear whether their internal representations faithfully encode the structured relations required for such reasoning. We introduce EICS (Evaluation-Invariant Concept Stability), a metric for testing whether representations consistently encode concepts under controlled one-concept interventions, and CASP-VL (Causally controlled Spatial Perturbations for Vision-Language models), a benchmark of causally controlled spatial perturbations derived from Visual Genome scene graphs. Across multiple VLM architectures, we find that spatial relations are represented substantially less faithfully than lexical information, even when the same models score well above chance on compositional benchmarks. Further analy...

### [Structural Automata for Neural Semantic Parsing](http://arxiv.org/abs/2610.13896v1)
- Authors: Xiao Zhang
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13896v1
- Categories: cs.CL
- Abstract: Neural semantic parsers generate meaning representations token by token, yet well-formedness depends on references, scope, and graph relations that unfold during generation. Constrained decoding prevents locally invalid tokens but does not guarantee that a valid prefix can be completed within a fixed output-length limit. We investigate structural automata at three stages of DRS parsing (decoding, post hoc processing, and training) and additionally evaluate decoding on AMR. For decoding, we introduce accepting-path decoding (APD), which maintains a verified completion within the remaining length limit and follows the model's preferred token whenever that token can also be completed. APD guarantees an accepted output without retracting tokens. Under tight length limits, it improves Smatch++ ...

### [Task Context Shapes Component Roles in Language Models](http://arxiv.org/abs/2610.13895v1)
- Authors: Sovesh Mohapatra, Dani S Bassett
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13895v1
- Categories: cs.CL, cs.AI
- Abstract: Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention heads and the activation state in later layers (influence), as well as the answer (importance). Task changes redistribute the influence in five open-weight models spanning four families and 1.5-14 billion parameters. In Gemma-2-9B and Qwen3-14B, an activation edit changes an early internal activatio...

### [Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga](http://arxiv.org/abs/2610.13840v1)
- Authors: Emilio Ferrara
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13840v1
- Categories: cs.AI, cs.CL, cs.CY
- Abstract: Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parses every scan into panels, text and a bibliographic record; annotates each page with a vision-language model that follows a written codebook, as a human coder would; grounds samples of these readings in human annotation; and explains change across an archive, with estimates controlled for publisher a...

### [OpenPA: Forced-alignment-free Multi-granular Pronunciation Assessment with Mixed-transcript Adaptation](http://arxiv.org/abs/2610.13826v1)
- Authors: Fu-An Chao, Bi-Cheng Yan, Berlin Chen
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13826v1
- Categories: eess.AS, cs.CL, cs.SD, eess.SP
- Abstract: Recent advances in automatic pronunciation assessment (APA) have driven a shift from scripted to free-form assessment. However, existing methods often rely on multi-stage pipelines with forced alignment and separate feature extractors, limiting their practicality across response settings. In light of this, we propose OpenPA, a novel APA framework that leverages Whisper's cross-attention mechanism to jointly predict word- and utterance-level pronunciation scores without forced alignment. Through mixed-transcript adaptation and adaptive substitution weighting, OpenPA accommodates heterogeneous transcripts across closed- and open-response settings within a single model. Trained solely on speechocean762, OpenPA achieves the strongest overall performance among evaluated systems under in-domain ...

### [Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection](http://arxiv.org/abs/2610.13821v1)
- Authors: Juan Terven, Diana-Margarita Córdova-Esparza, Ruben Gomez, Carlos Miranda Rocha, Julio-Alejandro Romero-González, Edgar Chavez-Urbiola
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13821v1
- Categories: cs.CL
- Abstract: A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention. Across three training seeds and two held-out confidence thresholds, a learned answer selector improves threshold-averaged utility over the original model's calibrated confidence filter. On TriviaQA, mean coverage increases from 20.2% to 30.9%, while the pooled error rate among scored answers decreases from 23.0% to 14.5% under exact-match grading. The tested reinforcement-learning changes do not establish consistent gains. On NQ-Open, the selector i...

### [QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code](http://arxiv.org/abs/2610.13811v1)
- Authors: Meriem Terki, Nouhaila Innan, Minghao Shao, Muhammad Kashif, Alberto Marchisio, Muhammad Shafique
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13811v1
- Categories: cs.LG, cs.CL, quant-ph
- Abstract: Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a correct solution, but not whether its tests can distinguish correct implementations from faulty ones. We introduce QTestBench, a framework that evaluates LLM-generated quantum test suites against independent benchmark checkers, never treating the tests themselves as ground truth. For each task, QTestBench prompts models...

### [Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering and Breadth-Aware Selection for LLM Query Expansion](http://arxiv.org/abs/2610.13810v1)
- Authors: Amit Kumar Jaiswal, Sagar Uprety, Prayag Tiwari
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13810v1
- Categories: cs.IR, cs.CL
- Abstract: Large language models (LLMs) are now a standard source of query expansion terms but they hallucinate. They inject non existent entities and off-topic terms that add ranking noise and can hurt strong retrievers. Existing remedies such as corpus grounding, mutual verification and preference alignment treat hallucinated terms as an undifferentiated nuisance to be filtered by agreement heuristics, without a mechanistic account of why a given term appears or a principled criterion for how many terms to keep. We propose Subsequence-Association Filtered, breadth-aware query expansion (SAFE-QE), a training-free, retriever agnostic method that draws on the subsequence-association account of hallucination. We score each candidate expansion term by its corpus conditioned cross-context reproducibility...

### [Error Rate is Not Enough: Costs of Augmentation in Low-Resource ASR](http://arxiv.org/abs/2610.13807v1)
- Authors: Katsumi Ibaraki, David Chiang
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13807v1
- Categories: cs.CL
- Abstract: Data augmentation is standard practice for low-resource automatic speech recognition (ASR), but its benefits are almost always reported as aggregate error rates, leaving open why and when a method helps. On four low-resource languages and English at five data sizes, we cross two augmentations that modify existing audio (speed perturbation and SpecAugment) with two that modify text transcriptions and synthesize audio from it. We analyze errors at the phoneme level and find that they help for complementary reasons. SpecAugment has the most reliable aggregate improvements, but increases tone and palatalization errors, whereas text-based methods introduce consonant insertions; in combination, each reduces the errors the other introduces. This complementarity is predictable. Tone and palataliza...

---

## IR/RecSys/Ads (cs.IR)
Found 10 recent papers (top 10 shown).

### [Can Language Models Play the Wikipedia Game?](http://arxiv.org/abs/2610.13948v1)
- Authors: Alexander Hickey, Joanna Knight, James Bishop
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13948v1
- Categories: cs.AI, cs.IR
- Abstract: Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. In the game, players must reach a target article using only article links. We compared sentence embedding models and LLMs across five Wikipedia languages and five academic-literature datasets. We construct very large local graphs of Wikipedia pages and of paper citations using OpenAlex and provide code to build and navigate them. This allows the study of language models' navigation capabilities without relying on third-party APIs. We compared the models with human and TF-IDF benchmarks. The Wikip...

### [RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](http://arxiv.org/abs/2610.13889v1)
- Authors: Weiliang Chen, Song Liao
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13889v1
- Categories: cs.AI, cs.IR
- Abstract: As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This design enables rapid adaptation to runtime tool failures without expensive model retraining. We introduce EcoAgent, a benchmark of 5,172 real-world tools and over 210,000 query-tool pairs for offline ...

### [Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering and Breadth-Aware Selection for LLM Query Expansion](http://arxiv.org/abs/2610.13810v1)
- Authors: Amit Kumar Jaiswal, Sagar Uprety, Prayag Tiwari
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13810v1
- Categories: cs.IR, cs.CL
- Abstract: Large language models (LLMs) are now a standard source of query expansion terms but they hallucinate. They inject non existent entities and off-topic terms that add ranking noise and can hurt strong retrievers. Existing remedies such as corpus grounding, mutual verification and preference alignment treat hallucinated terms as an undifferentiated nuisance to be filtered by agreement heuristics, without a mechanistic account of why a given term appears or a principled criterion for how many terms to keep. We propose Subsequence-Association Filtered, breadth-aware query expansion (SAFE-QE), a training-free, retriever agnostic method that draws on the subsequence-association account of hallucination. We score each candidate expansion term by its corpus conditioned cross-context reproducibility...

### [SPARQL-LLM in the TEXT2SPARQL 2026 Challenge](http://arxiv.org/abs/2610.13648v1)
- Authors: Panayiotis Smeros, Vincent Emonet, Ruijie Wang, Ana-Claudia Sima, Tarcisio Mendes de Farias
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13648v1
- Categories: cs.IR
- Abstract: Querying distributed data represented as Knowledge Graphs (KGs) via SPARQL remains a difficult task, requiring fluency in query syntax, endpoint specifications, and schema details. Knowledge Graph Question Answering (KGQA) systems address this by automatically translating natural language into SPARQL, and recent advances in Large Language Models (LLMs) have made this translation increasingly feasible. In this paper, we describe SPARQL-LLM, our open-source KGQA system, in the context of the TEXT2SPARQL 2026 challenge. In this challenge, SPARQL-LLM ranks first overall among eight competing approaches across all datasets, achieving up to 59% higher accuracy than the second-best approach and supporting multilingual question answering in English, German, and Spanish. SPARQL-LLM is publicly rele...

### [Beyond Temporal Proximity: Explanatory World Models for Credit Assignment in Reinforcement Learning](http://arxiv.org/abs/2610.13504v1)
- Authors: Oriol Corcoll, Qiyao Wei, Ciarán Mark Gilligan-Lee
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13504v1
- Categories: cs.LG, cs.AI, cs.IR
- Abstract: Generative Recommenders increasingly use Reinforcement Learning (RL) to optimize outcomes that may appear hundreds or thousands of interactions after a decision. Standard RL propagates reward according to temporal proximity rather than explicit relevance, attenuating the signal assigned to distant but important actions and creating a source of sample inefficiency. We introduce Explanatory World Models (EWM), an attribution framework that uses explanations to identify the earlier events that plausibly contributed to a realized outcome. We instantiate EWM with a frontier language model and use its explanations as learning signals using a conservative hierarchical operator that recursively redistributes reward while preserving the undiscounted episode return. To investigate what constitutes a...

### [Web$hell: A Unified Interface for Agentic Web Access](http://arxiv.org/abs/2610.13416v1)
- Authors: Sunghwan Kim, Deogyong Kim, Sangam Lee, Donguk Kwon, Dongha Lee
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13416v1
- Categories: cs.AI, cs.IR
- Abstract: Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access through different access models, including search-augmented agents, browser-based agents, and, more recently, filesystem-based agents. Nevertheless, as users expect agents to complete long-horizon, end-to-end tasks, they increasingly need to conduct broad information gathering, perform browser actions, and revisit acquired evidence within a single trajectory. Yet our preliminary analyses reveal that existing access models struggle to meet these demands. They primarily support either information gathering or browser...

### [NEAR: Neighborhood-Aware Residuals for Memory Retrieval](http://arxiv.org/abs/2610.13314v1)
- Authors: Han Luo, Zhan Zhuang, Xu He, Jujia Zhao, Yu Li, Suqin Yuan, Dong Li, Lei Feng
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13314v1
- Categories: cs.IR
- Abstract: Memory retrieval aims to identify evidence from stored records to answer a query. Stored records with different factual details may share topics, entities, or events. Such shared contents would make records without the required evidence more likely to receive high similarity scores and outrank the correct evidence. In this paper, we use the information shared by these records to construct local references for query-memory matching. We propose NEighborhood-Aware Residuals (NEAR), a training-free framework that uses these references to construct residual representations that complement the original embeddings. Specifically, each memory derives a reference direction from its neighbors, and each query obtains its reference from a precomputed table. Using these references, NEAR constructs proje...

### [PRIME: Pre-Retrieval Index Modeling Enhancement for Structured Document Retrieval-Real](http://arxiv.org/abs/2610.13296v1)
- Authors: Cheuk Hei Chung, Li Liu
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13296v1
- Categories: cs.IR, cs.AI
- Abstract: High-precision retrieval over external knowledge bases is essential for LLM agents to operate effectively. However, existing Information Retrieval (IR) research primarily optimizes query-side retrievers (e.g., ColBERT, BGE) and generators (e.g., Self-RAG, GraphRAG), while reducing corpus-side representation to chunking. This leaves index-side quality an underexplored lever. We propose Pre-Retrieval Index Modeling & Enhancement (PRIME), an index-side optimization framework built on two complementary tracks: an LLM-driven Semantic Restructuring (SR) track that transforms long documents into structured, information-dense sections, and a deterministic Metadata Synthesis (MS) and Hierarchical Retrieval (HR) track that extracts semantic anchors and heading structure for coarse-to-fine section re...

### [Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence](http://arxiv.org/abs/2610.13277v1)
- Authors: Han Luo, Zhan Zhuang, Xu He, Jujia Zhao, Yu Li, Suqin Yuan, Dong Li, Lei Feng
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13277v1
- Categories: cs.IR, cs.CL
- Abstract: Memory-augmented assistants retrieve evidence from stored conversations and documents to answer queries. Most embedding-based retrievers compare single-vector representations of queries and memories, even when relevance depends on a small part of the content. Such local evidence can be matched to queries using the contextual token representations already computed by the same embedding models. Our method uses sparse token matching to improve retrieval without additional training. Each query token retrieves a small set of matching tokens across candidate memories. The matching scores are aggregated for each memory and combined with whole-memory similarity to rank memories. An optional low-rank query adapter can be trained with supervision while keeping the encoder and stored memory represent...

### [Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA](http://arxiv.org/abs/2610.13128v1)
- Authors: Wenlin Lin, Fanzhe Wei
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13128v1
- Categories: cs.AI, cs.CL, cs.IR
- Abstract: Question answering over large heterogeneous document collections requires first finding the right passages and then reading them, yet current retrieval-augmented agents give one model both kinds of tools and let it schedule itself. We present KnowForge, a pipeline separated by job: a hybrid-retrieval knowledge-point index; a Locator agent that can only search; a code-scheduled bridge judge that forces the missing second hop; a typed, size-bounded evidence pool that merges every search's ranking; a Deep Reader agent that can only read text, images and tables; and a synthesizer with a format checker. With a self-hosted Qwen3.6-35B-A3B (3B active), KnowForge reaches F1 47.5 on the full open-domain M3DocVQA (2,441 questions, 3,368 PDFs), +11.0 over the published M3DocRAG system and +7.1 over o...

---

## CV (cs.CV)
Found 10 recent papers (top 10 shown).

### [Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark](http://arxiv.org/abs/2610.13947v1)
- Authors: Xudong Cai, Ruijie Zhu, Haoliang Shang, Ruining Li, Marc Pollefeys, Shangzhe Wu, Andrea Vedaldi, Chuanxia Zheng
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13947v1
- Categories: cs.CV
- Abstract: In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articraft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond geometry, appearance, and physically plausible articulation, such as collision-free motion, stability under gravity, and accurate mass and material properties. Furthermore, we construct a unified benchmark spanning four key aspects: spatial fidelity, physical plausibility, downstream task performance, and overall quality. The benchmark encompasses 100 reference assets from ArtVIP...

### [Splat2Act: From Captured Scenes to Personalized VLA Manipulation](http://arxiv.org/abs/2610.13945v1)
- Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13945v1
- Categories: cs.RO, cs.CV
- Abstract: A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive. We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy to a specific scene and object set using only a handheld phone scan and images of the user's objects. Unlike prior real-to-sim work that reconstructs individual tabletops, Splat2Act operates on building-scale indoor environments: it builds a photorealistic digital twin with 3D Gaussian Splatting and...

### [InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators](http://arxiv.org/abs/2610.13944v1)
- Authors: Xuanlang Dai, Jiazi Bu, Yujie Zhou, Yuhong Liu, Beichen Zhang, Penghui Yang, Ziyu Liu, Yuhang Zang
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13944v1
- Categories: cs.CV
- Abstract: Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representations. Despite their remarkable generation capabilities, the cross-model alignment of latent representations and the consistency of their underlying denoising dynamics remain underexplored. In this work, we uncover an intriguing cross-model compatibility: independently trained generators exhibit similar latent spatial organization, while directly handing off intermediate states between unaligned models can still preserve coarse visual content. Motivated by these observations, we propose InstantFusion, a lightweight shared latent interface that connects the denoising trajectories of heterogeneous i...

### [Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](http://arxiv.org/abs/2610.13941v1)
- Authors: Yucheng Yang, Xiaoxiao Sun, Shusheng Yang, Jiakang Chen, Serena Yeung-Levy
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13941v1
- Categories: cs.CV
- Abstract: Multimodal diffusion transformers (MMDiTs) allow the evolving image to update internal text representations through joint attention. These representations then guide subsequent image updates, raising a question: does this feedback help correct deviations from the prompt, or preserve them? We find that image-to-text (I2T) feedback can preserve the objects and attributes already represented in the evolving image, including errors. Transplanting I2T messages can rescue failures or disrupt successes. At matched intervention strengths, suppressing the influence of I2T feedback improves generation, whereas opposite controls degrade it. These findings motivate Semantic Feedback Guidance (SFG), which suppresses the influence of I2T feedback by guiding away from an auxiliary branch that strengthens...

### [Hide and Seek: HIDE Concepts to SEEK explanations for black box models](http://arxiv.org/abs/2610.13935v1)
- Authors: Bhanu Tokas, Rahul Nair, Rockwell Jackson, Hannah Kerner
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13935v1
- Categories: cs.CV, cs.AI, cs.LG
- Abstract: Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that does not require access to model weights or labeled concept datasets. HnS can interpret a wide range of vision models. Given a concept and image set, HnS retrieves concept-aligned images using a vision-language model, localizes the concept within each image, masks the localized region, and measures...

### [Chronos Policy: Learning Robot Policies on Physical Time](http://arxiv.org/abs/2610.13929v1)
- Authors: Changhao Wang, Jaden Clark, Shuran Song
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13929v1
- Categories: cs.RO, cs.CV
- Abstract: Robot policies often convert sensing and control into fixed-rate observation-action sequences, leaving physical time implicit in sequence position. This assumption breaks when observation rates or delays vary, or when inference latency changes. We introduce Chronos Policy, which makes physical time explicit by conditioning on observation capture times and desired action execution times. We study two ways to incorporate time into a diffusion transformer: adding timestamp embeddings to token features, or encoding physical time in positional encoding through time-aware rotary positional encodings (time-aware RoPE). We find that time-aware RoPE is more robust, allowing attention to depend directly on physical time while keeping token content unchanged. During training, we temporally randomize ...

### [Can machines reason non-verbally?](http://arxiv.org/abs/2610.13925v1)
- Authors: Shaheer U. Saeed, Zion Tse, Gregory Slabaugh, Daniel C. Alexander, Yipeng Hu
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13925v1
- Categories: cs.CV
- Abstract: Modern machines can solve equations, follow logic and reason through language, yet they still struggle with problems that require visual non-verbal reasoning. This is evident even in advanced systems such as DeepSeek, ChatGPT and Gemini, which remain limited on visual tasks such as completing abstract patterns or delineating ambiguous regions-of-interest. Unlike explicit intermediate steps in verbal reasoning which can be verified through logic or automated tests, visual reasoning involves implicit intermediate steps with no clear methods for verification. Non-verbal reasoning is therefore challenging to model and, as a result, remains a fundamental limitation of current machine intelligence. Here we introduce GenVerOpt, a general framework that unifies generation, verification and optimis...

### [Where to Look Matters: Rethinking Sub-Volume Sampling in 3D Medical Self-supervised Learning](http://arxiv.org/abs/2610.13915v1)
- Authors: Junkai Liu, Le Zhang
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13915v1
- Categories: cs.CV
- Abstract: Self-supervised learning on 3D medical images commonly relies on random sub-volume sampling during pretraining. However, random cropping implicitly treats all spatial regions as equally worth observing, despite anatomical priors and spatial redundancy that make regions inherently unequal in their value for representation learning. To this end, we first show through controlled crop-quality manipulations that better sub-volumes lead to better downstream transfer, revealing the observation policy as an overlooked bottleneck in 3D medical SSL. Motivated by this finding, we revisit sub-volume sampling as a \emph{where-to-look} problem. We propose \textbf{\method}, a plug-and-play framework that replaces random cropping with an offline coarse-to-fine probe bank guided by \textit{anatomy-awarenes...

### [Beyond the Snowflakes: Disentangling Weather Effects from Confounding Meta-Factors in LiDAR Object Detection](http://arxiv.org/abs/2610.13891v1)
- Authors: Yiming Yang, Jeremy P. Bos
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13891v1
- Categories: cs.CV, cs.RO
- Abstract: Light Detection and Ranging (LiDAR) is critical for autonomous perception, yet its performance is known to degrade in adverse weather. While existing literature models snow as atmospheric noise that degrades performance, our granular evaluation on the WADS-3D and CADC datasets reveals a counter-intuitive phenomenon: detection accuracy consistently improves as snow intensity increases. Through ablation study and meta-information analysis, we reconcile this by confirming that while falling snow acts as noise, its negative impact is outweighed by a dominant, concurrent factor: significantly increased object point count. We hypothesize that this object point count boost acts as a geometric enhancement, driven by snow accumulation increasing vehicle surface area and a shift from specular to dif...

### [Tracking the Invisible: Self-Supervised Wheel Track Detection with Thermal-RGB Fusion](http://arxiv.org/abs/2610.13872v1)
- Authors: Yiming Yang, Jeremy P. Bos
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13872v1
- Categories: cs.CV, cs.RO
- Abstract: Accurate detection of drivable area is essential for autonomous driving and advanced driver assistance systems. While state-of-the-art methods focus on general traversability estimation, they prove inadequate for snow-covered roads where following existing wheel tracks offers crucial advantages: improved traction, predictable vehicle dynamics, and verified path stability. To address this, we propose a low-cost, self-supervised approach detecting safety-critical wheel tracks using synchronized RGB-I (RGB + Long-Wave Infrared) imagery. Our method automatically generates training labels by projecting future wheel trajectories from recorded GNSS data. A neural network is designed to identify wheel tracks with the 4-channel RGB-I images from challenging, white-out road surfaces. Experimental re...

---

## DM/Algos (cs.DM)
Found 10 recent papers (top 10 shown).

### [Polynomial directed treewidth forces a large bramble with congestion two](http://arxiv.org/abs/2610.13270v1)
- Authors: Victor A. Campos, Raul Lopes, Rodrigo Nogueira, Ignasi Sau
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13270v1
- Categories: cs.DS, cs.DM, math.CO
- Abstract: Brambles of constant congestion in directed graphs have interesting structural and algorithmic applications, and it is desirable to find the smallest function $f_c(k)$ such that if a digraph has directed treewidth at least $f_c(k)$, then it contains a bramble of size at least $k$ and congestion at most $c$. By the Directed Grid Theorem of Kawarabayashi and Kreutzer [STOC 2015], such a function $f_c(k)$ exists for every value $c \geq 2$ of the congestion. However, even using the recent improvements due to Hatzel et al. [FOCS 2024], the resulting function is a power tower of height $22$. Recently, Masařík et al. [SIAM J. Discrete Math. 2022] proved that, for congestion $8$, the function $f_8(k)$ can be made polynomial; more precisely, they showed that $f_8(k) = \mathcal{O}(k^{48} \cdot \log^...

### [Equitable Subpartitionability Does Not Characterize Box-TDI Polyhedra](http://arxiv.org/abs/2610.13244v1)
- Authors: Emiliano Lancini, Francesco Pisanu
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13244v1
- Categories: cs.DM
- Abstract: Equitable subpartitionability (ESP) is a sufficient condition for an integral system to be box-totally dual integral. We show that the converse fails even when alternative descriptions of the same polyhedron are allowed. We provide a geometrical characterization of polyhedra that can be described by ESP systems in terms of normal cones. We construct a four-dimensional integer polytope described by a totally equimodular matrix that admits no integral ESP description. This answers negatively a previously posed question by the same authors.

### [Detection and Construction of Small Blocking Sets via Critical Independent Sets and Matching Decomposition](http://arxiv.org/abs/2610.13096v1)
- Authors: Quanlong Niu, Riheng Jia
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13096v1
- Categories: cs.DM
- Abstract: The small blocking set detection and construction problem asks whether a given connected simple graph contains a nonempty independent set whose cardinality equals the size of its neighborhood and is strictly less than half the number of vertices, and, if so, how to construct such a set. Previous work characterized restless explorability in vertex-permuted temporal graphs using small blocking sets, but left the computational complexity of detecting their existence as an open problem. We give a polynomial-time algorithm for detection and construction. Specifically, we first compute a maximum-cardinality critical independent set and use its difference and cardinality to handle the cases that admit an immediate solution. In the remaining boundary case, where the critical difference is zero and...

### [The Stable Marriage Polytope is Box-Totally Dual Integral](http://arxiv.org/abs/2610.12720v1)
- Authors: Michele Barbato, Emiliano Lancini
- Published: 2026-10-08
- arXiv link: http://arxiv.org/abs/2610.12720v1
- Categories: math.CO, cs.DM
- Abstract: A stable matching in a bipartite preference system is a matching that has no unmatched pair whose endpoints both prefer each other to their current assignments. Rothblum gave a linear description of the stable marriage polytope, the convex hull of the incidence vectors of stable matchings. We prove that this polytope is box-totally dual integral. The proof uses the affine representation of the stable marriage polytope as an order polytope together with the matricial characterization of box-TDI polyhedra. Since Kiraly and Pap proved that Rothblum's description is totally dual integral, our result further implies that Rothblum's system is box-totally dual integral.

### [Maximal Linear Arrangement is NP complete on Bipartite Graphs](http://arxiv.org/abs/2610.12613v1)
- Authors: Aparna Das, Jonathan Needleman
- Published: 2026-10-08
- arXiv link: http://arxiv.org/abs/2610.12613v1
- Categories: cs.DM, math.CO
- Abstract: The linear arrangement of a simple graph $G = (V,E)$ is a bijective labeling $π$ of the vertices of $G$ to the set $\{1, \ldots, n\}$. The maximum linear arrangement ($\texttt{maxLA}$) problem is to determine whether $G$ has a labeling such that the sum of labels across $G$'s edges, $\sum_{uv \in E} |π(u) - π(v)|$, is at least a given value $k$. Minimum linear arrangement ($\texttt{minLA}$) is defined analogously. Both $\texttt{maxLA}$ and $\texttt{minLA}$ are known to be NP complete for general graphs. $\texttt{minLA}$ has shown to be NP complete for bipartite graphs by Evans and Shiloah in 1975. It has been an open problem whether the same holds for $\texttt{maxLA}$. In this paper we prove that $\texttt{maxLA}$ is NP complete for bipartite graphs.

### [Improved Local Leakage Resilience of Shamir Secret Sharing and Worst-Case Optimal Polynomial Intersection](http://arxiv.org/abs/2610.12357v1)
- Authors: Yihang Sun, Mary Wootters
- Published: 2026-10-08
- arXiv link: http://arxiv.org/abs/2610.12357v1
- Categories: quant-ph, cs.CR, cs.DM, cs.IT
- Abstract: We study two problems: Local Leakage Resilience (LLR) for Shamir secret sharing, and worst-case Optimal Polynomial Intersection (OPI). Both problems concern polynomials $Q(X)$ of degree less than $k$, over a prime-order finite field $\mathbb{F}_p$. In LLR for Shamir secret sharing, one asks how much one can learn about $Q(0)$ given a few bits leaked from each of $Q(α_1), \ldots, Q(α_n)$, for distinct non-zero evaluation points $α_i \in \mathbb{F}_p$. In OPI, one is given input list $S_1, \ldots, S_n \subset \mathbb{F}_p$, and wants to find a polynomial $Q(X)$ of degree less than $k$ so that $Q(α_i) \in S_i$ for as many $i$ as possible. Leveraging recent connection between these two problems due to (Sun, Wootters 2026), we improve the state-of-the-art for both problems. For LLR, we show tha...

### [Lower bounds for Ramsey numbers: $\mathrm{R}(6,8)\ge 135$ and $\mathrm{R}(8,10)\ge 345$](http://arxiv.org/abs/2610.12122v1)
- Authors: Fritz Cremer
- Published: 2026-10-08
- arXiv link: http://arxiv.org/abs/2610.12122v1
- Categories: math.CO, cs.DM
- Abstract: We prove the lower bounds $\mathrm{R}(6,8)\ge 135$ and $\mathrm{R}(8,10)\ge 345$, improving the bounds 134 and 343 listed in the April 2026 revision of Radziszowski's dynamic survey. We give explicit red/blue colorings of $K_{134}$ with no red $K_6$ or blue $K_8$, and of $K_{344}$ with no red $K_8$ or blue $K_{10}$, and verify them with two independently written exhaustive clique checkers. Starting from published colorings, we find these witnesses by adding vertices and repairing the resulting monochromatic cliques through local search. The search uses exact conflict counts, preparation moves aimed at making remaining cliques cheaper to break, and mutations followed by repair. A loss based on the largest monochromatic clique containing each edge yielded a useful intermediate state for the ...

### [An ETH-based quasipolynomial lower bound for Dualization](http://arxiv.org/abs/2610.11473v2)
- Authors: Yasuaki Kobayashi, Kazuhiro Kurita, Kunihiro Wasa
- Published: 2026-10-08
- arXiv link: http://arxiv.org/abs/2610.11473v2
- Categories: cs.DS, cs.DM
- Abstract: Dualizing monotone Boolean functions (or equivalently, enumerating minimal transversals in hypergraphs) is a long-standing problem whose output-polynomial-time solvability remains open. While various special cases have been extensively studied, the state-of-the-art algorithm for the general case, due to Fredman and Khachiyan, runs in quasipolynomial time. This paper presents a subexponential-time reduction from \textsc{3SAT} to the complement of \textsc{Dual}: Given a 3CNF formula with $n$ variables, the reduction constructs hypergraphs $H$ and $L$ of total size $2^{O(n^{2/3}(\log n)^{1/3})}$ such that $L \subseteq Tr(H)$ and the formula is satisfiable if and only if $L\neq Tr(H)$, where $Tr(H)$ is the set of minimal transversals of $H$. As a consequence of this reduction, assuming the Exp...

### [Integer programming on polytopes of Chvátal rank one is as hard as lattice problems](http://arxiv.org/abs/2610.10911v1)
- Authors: Alberto Del Pia
- Published: 2026-10-07
- arXiv link: http://arxiv.org/abs/2610.10911v1
- Categories: math.OC, cs.CC, cs.DM
- Abstract: A rational polyhedron has Chvátal rank at most one if a single round of Chvátal-Gomory cuts yields its integer hull. For such polyhedra, integer feasibility is in NP $\cap$ coNP by a result of Boyd and Pulleyblank from the early 1980s, so it is unlikely to be NP-hard. Whether it is polynomial has remained open since then. We answer this question negatively, under either of two standard assumptions from lattice-based cryptography. First, a polynomial-time algorithm for this problem would solve bounded distance decoding with polynomial factors in deterministic polynomial time, contradicting a widely believed conjecture. Second, assuming the hardness of learning with errors, an average-case analogue of bounded distance decoding, the problem is also hard on average, for an efficiently samplabl...

### [Tweaking the constant in the Linear Hadwiger Theorem](http://arxiv.org/abs/2610.10831v1)
- Authors: David R. Wood
- Published: 2026-10-07
- arXiv link: http://arxiv.org/abs/2610.10831v1
- Categories: math.CO, cs.DM
- Abstract: Norin and Steiner recently proved the Linear Hadwiger Conjecture. That is, there is an absolute constant $C$ such that every graph $G$ satisfies $χ(G)\leqslant C\,\text{had}(G)$, where $χ(G)$ is the chromatic number and $\text{had}(G)$ is the Hadwiger number of $G$. Their proof gives a non-optimised constant $C$ of order $10^{100}$. This paper uses extensive AI-based optimisation to show that every graph $G$ satisfies $χ(G) \leqslant 19{,}885{,}160\,\text{had}(G)$.

---

## Games/GT (cs.GT)
Found 10 recent papers (top 10 shown).

### [A $1/2$-Approximation for Pandora's Problem with Deadlines](http://arxiv.org/abs/2610.13775v1)
- Authors: Shenyu Qin, Chihao Zhang, Yuhao Zhang, Zixuan Zhu
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13775v1
- Categories: cs.GT
- Abstract: Pandora's problem is a fundamental model of sequential search in which opening each box incurs a cost. We study the variant with deadlines, where each box has a publicly known deadline for both opening and selection. We prove that a simple threshold strategy achieves a $1/2$-approximation to the optimal expected utility, improving the previous guarantee of $(e-1)/(4e)\approx0.158$ due to Berger et al. (AAAI 2024).

### [Asymmetric Information in Dynamic Lending Games](http://arxiv.org/abs/2610.13759v1)
- Authors: Kristijan Atanasov, Frederik Mallmann-Trenn, Carmine Ventre
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13759v1
- Categories: cs.GT
- Abstract: We study a dynamic lending game with limited but reusable supply. Borrower arrivals and loan durations are stochastic. Demand is allocated cheapest-first, subject to available supply, so a lender's quote affects both its current payoff and its ability to serve future borrowers. Motivated by industry practice, we study this problem through the lens of information disclosure: Lenders observe either only their own available supply or also their rivals' aggregate available supply. We ask how providing this information to all, some or none of the lenders affects payoffs as demand varies relative to supply, and how these effects change when a fixed total supply is divided among different numbers of lenders. Interestingly, in the case of asymmetric information disclosure, total payoffs can increa...

### [The Distortion of Threshold Approval Multiwinner Voting](http://arxiv.org/abs/2610.13725v1)
- Authors: Mohamad Latifian, Marzieh Nilipour, Alexandros A. Voudouris
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13725v1
- Categories: cs.GT
- Abstract: We study multiwinner voting with $n$ voters and $m$ candidates, where the goal is to select a committee of size $k$. Voters have unit-sum cardinal utilities but report only coarse information induced by $t$ utility thresholds. In particular, each voter partitions the candidates into approval sets, with the utilities of all candidates in the same set lying between the same pair of consecutive thresholds. We model the utility of each voter for a committee as a normalized monotone symmetric norm, capturing, among others, additive welfare, best-representative utility, top-$r$ welfare, $\ell_p$ welfare, and normalized non-increasing ordered weighted averages. We design a deterministic rule with distortion at most $2(2m)^{1/t}$ and a randomized rule with distortion at most $2\min\{m^{1/(t+1)},m/...

### [Complexity of Autobidding Equilibria in GSP Sponsored Shopping](http://arxiv.org/abs/2610.13716v1)
- Authors: Kristoffer Arnsfelt Hansen, Yuhao Li, Xinhao Nie
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13716v1
- Categories: cs.GT, cs.CC
- Abstract: We revisit autobidding equilibria in GSP sponsored shopping auctions, recently proposed and studied in Dütting et al. On the existence side, we show that autobidding equilibria under both budget constraints (ABE-B) and return-on-investment constraints (ABE-R) always exist and, moreover, always admit equilibria with polynomial-size support over the allocation space. On the computational side, we show that computing an exact equilibrium is in FIXP, and that computing an approximate equilibrium is in PPAD. We also prove that computing an approximate equilibrium is PPAD-hard for both ABE-B and ABE-R. Together, these results provide a fairly comprehensive picture of the computational complexity of autobidding equilibria in GSP sponsored shopping auctions.

### [Limit-sure Winning in Team Games without Shared Randomness](http://arxiv.org/abs/2610.13569v1)
- Authors: Léonard Brice, Thomas A. Henzinger, Alipasha Montaseri, Ali Shafiee, K. S. Thejaswini
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.13569v1
- Categories: cs.GT, cs.FL, cs.MA
- Abstract: We study concurrent stochastic games in which a team of agents plays against an adversarial environment. If the agents could access a shared source of randomness, then these games reduce to two-player games. Despite being common in the literature on coalition games, this assumption does not accurately model real-world systems. In this paper, we consider the setting where the agents only have access to individual sources of randomness, and must satisfy a given reachability or safety objective. The limit-sure problem asks whether the team can ensure that the objective is satisfied with probability at least $1-λ$ for every $λ>0$. For reachability objectives, we show that this problem is $\mathsf{NP}$-complete. For safety objectives, we show that limit-sure winning coincides with almost-sure w...

### [Dynamic Matching with Abandonment: Optimal Guarantees via Static Priority Policies](http://arxiv.org/abs/2610.12991v1)
- Authors: Nick Arnosti, Rad Niazadeh, Pranav Nuti, Felipe Simon
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.12991v1
- Categories: cs.DS, cs.CC, cs.GT, econ.TH, math.OC
- Abstract: We study stochastic dynamic matching with abandonment, a fundamental model in which agents of different types arrive over time, may abandon the market while waiting, and can be matched in pairs for rewards that depend on their types. No online policy can guarantee more than $0.5$ of the omniscient benchmark, which knows all arrival and departure times. Whether this guarantee is achievable has been a central open problem, even in special cases. We resolve this problem by showing that, on every instance, a simple static priority policy, which is computable in polynomial time, earns at least $0.5$ of the omniscient benchmark. This establishes that the optimal competitive ratio is exactly $0.5$, improving the previous best guarantee of 0.192 for the general model [Li et al. 2026; Collina et al...

### [Network Topology Shapes AI Intervention Effectiveness on Deception: Truth-Telling vs. Investigative Agents](http://arxiv.org/abs/2610.12931v1)
- Authors: Zhao Song, Stefan Sarkadi, The Anh Han
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.12931v1
- Categories: cs.GT
- Abstract: Deploying AI agents to combat dishonest communication is an intuitive response to deception in hybrid human-AI societies. However, the efficacy of such interventions in realistic networked settings remains unclear. We study this problem using an evolutionary game-theoretic model of the Deceiver's Game by extending it to structured networks, where agents can adopt deception, truth-telling, and investigation strategies. We introduce committed AI agents (zealots) fixed to either truth-telling or investigative strategies and conduct agent-based simulations across three network topologies. Our key findings are: (1) passive committed truth-telling agents can amplify adaptive deception by creating exploitable honest partners, whereas investigative agents increase adaptive truth-telling in the osc...

### [The False Allure of "Security by Obscurity": A Game-Theoretic Approach](http://arxiv.org/abs/2610.12858v1)
- Authors: In-Uck Park, Sunoo Park
- Published: 2026-10-09
- arXiv link: http://arxiv.org/abs/2610.12858v1
- Categories: cs.GT, cs.CR, cs.CY, econ.TH
- Abstract: "Security by obscurity," or the idea that hiding how a system works helps protect it from adversaries, has long been poorly regarded in the security community. Yet its intuitive appeal persists, and it has resurfaced repeatedly in industry practices and public debates over the years. The logic, on the one hand, is that open scrutiny of systems is the best way to find and respond to problems; and on the other hand, that too much openness can increase risk by giving adversaries a roadmap for attack. This isn't purely a technical question, but a human one: it's about how attackers and good-faith security researchers respond to openness in the real world. As such, security experts base their stance on decades of community experience; however, the field lacks empirical or theoretical foundation...

### [Game Petri Nets: Compositional Modeling and Analysis of Large-Scale Strategic Systems](http://arxiv.org/abs/2610.12779v1)
- Authors: Quanyan Zhu
- Published: 2026-10-08
- arXiv link: http://arxiv.org/abs/2610.12779v1
- Categories: cs.GT, eess.SY
- Abstract: Large-scale strategic systems, such as maintenance workflows, cyber campaigns, and multi-agent AI pipelines, consist of many interactions whose outcomes determine which later interactions become possible, who takes part, and with what resources. We introduce game Petri nets, formalized as outcome-driven compositional game Petri nets (OCGPNs), to model and analyze such systems. Local games are attached to places of a colored Petri net, and a game-to-token interface converts each resolved game into typed tokens that enable, synchronize, or block subsequent games. For general, concurrent nets, we give an operational semantics and a structural theory based on invariants and Farkas certificates, which shows that guards can certify unreachability whereas incentive instruments can only change val...

### [Spatial Pattern Formation from Multi-Agent Learning in Public Goods Dilemmas](http://arxiv.org/abs/2610.12321v1)
- Authors: Yefei Zhang, Yuxuan Zhao
- Published: 2026-10-08
- arXiv link: http://arxiv.org/abs/2610.12321v1
- Categories: cs.MA, cs.GT, cs.LG
- Abstract: Spatial public goods models show that prescribed movement toward richer locations can generate spatial patterns. We ask how such patterns emerge when agents learn where to move and how learning rates shape their consequences for collective welfare. Fixed populations of cooperators and defectors independently learn movement policies using tabular Q-learning and local observations. Cooperator learning generates clusters around resource peaks, while co-adaptation changes their strength and motion. At a fixed training budget, the largest welfare losses occur when cooperators learn at high rates and defectors at low rates. In part of this regime, learned policies also generate traveling bands supported by a shared directional preference. The conditions supporting travel change with further trai...

---
