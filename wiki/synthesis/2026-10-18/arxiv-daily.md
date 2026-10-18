---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-18)
type: synthesis
created: 2026-10-18
updated: 2026-10-18
sources: [arxiv-listing, arxiv-html]
tags:
  - arxiv
  - ai
  - llm
  - recommendation
  - advertising
  - sequential-modeling
  - ctr
  - daily-digest
---

# arXiv Daily Report (2026-10-18)

Search scope: arXiv Friday 2026-10-16 announcement block across cs.AI/cs.CL/cs.LG/cs.IR/cs.GT/cs.MA; no weekend announcements (as of 2026-10-18). CTR lane remains empty (newest CTR hits older than Fri block). Papers are new-to-wiki unless noted.

## Core AI/LLM/Reasoning (8)

### 2610.21182: Does Latent Chain-of-Thought Actually Reason? A Single, Unifying Taxonomy for Latent Reasoning
- **Authors**: Qiu, Jingjie, Yu, Sheldon, Jiang, Xunyi, Liu, Jiajin, Huang, Zihan, Chu, Zhendong, Yu, Tong, McAuley, Julian, Wu, Junda
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: Latent chain-of-thought replaces written reasoning steps with continuous hidden states, giving models additional steps to compute before answering. It remains unclear what computation these steps actually perform. High task accuracy and decodable intermediate answers do not establish that a model uses its latent chain to reach an answer. We study this question across twenty-one model-task configurations covering three training recipes, three reasoning tasks, and two backbones. We combine chain deletion and content...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21182

### 2610.21286: The Density of Thought: Predicting and Steering Reasoning in Large Language Models
- **Authors**: Kalhan, Tanush, Chattopadhyay, Anupam, Ranga, Sriram, Mukherjee, Amritendu
- **Institution/Company**: Plaksha University
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: We investigate whether variation in information density across chain-of-thought (CoT) reasoning steps predicts answer correctness and can serve as a controllable inference-time target. We prompt frozen pretrained models to solve problems via CoT and measure the density of each reasoning step with two independent metrics: LP variance (how unevenly information is distributed across steps, computed as the variance in mean per-token negative log-likelihood) and the Caveman compression ratio. We then test whether densit...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21286

### 2610.22067: Beyond Context Length: Characterising the Difficulty of Long-Context Reasoning
- **Authors**: Qin, Shiwen, Barker, Cameron, Gouk, Henry, Crowley, Elliot J., Cohen, Shay B., Lapata, Mirella, Li, Miao
- **Institution/Company**: Shay B. Cohen
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: Long-context language models support ever longer context windows, and evaluations typically treat context length as the main indicator of difficulty. However, context length alone cannot explain why models fail on long-context tasks that require reasoning over complex information. Contexts of equal length can pose very different challenges: a task may be solvable from a single local passage, or it may require integrating evidence distributed across the full context. We quantitatively characterise this difficulty th...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22067

### 2610.21060: Bellman-Consistent Trajectory RL for LLM Arithmetic Reasoning
- **Authors**: Li, Lianfa
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Machine Learning (cs.LG) ; Artificial Intelligence (cs.AI)
- **Abstract**: To address sparse terminal rewards in LLM arithmetic reasoning, we propose a Bellman-consistent trajectory RL method. Our framework introduces Trajectory Bellman Residual Minimization (TBRM) to transform sparse rewards into dense token-level signals. We integrate a Reinforce Leave-One-Out (RLOO) group strategy to reduce gradient variance of Bellman residuals and use hindsight goal relabeling to accelerate intermediate learning. Evaluated on the Countdown task, our method alleviates optimization bottlenecks and stab...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21060

### 2610.20914: Recursive Offline Distillation via Entropy Gain Sampling and Answer Mixing
- **Authors**: Goncharov, Andrey, Vyazhev, Daniil, Epanov, Simon, Zaytsev, Alexey
- **Institution/Company**: Applied AI Institute Correspondence:
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Distillation of reasoning chains from Large Language Models (LLMs) into their smaller siblings is a standard training approach. Frequently, researchers do not have full access to a teacher model and its internal representations, which limits the resulting performance. We propose a recursive offline distillation method combining two components: entropy-based sampling for selective distillation and answer mixing. Specifically, for three open models (3-4B), at each epoch, we sample reasoning chains weighted by entropy...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20914

### 2610.21427: Learning from Interaction Experience via Localized Context Distillation
- **Authors**: Hao, Zhezheng, Yang, Yongkang, Xia, Xilin, Yu, Jiarui, Liu, Yi, Wei, Fanjunduo, Dong, Peijie, Wang, Tianfu, Lin, Qiang, Wang, Can
- **Institution/Company**: Workbuddy Team, Tencent
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: Learning from interaction experience is essential for enabling large language models to continually improve during deployment. Context distillation offers a promising path: privileged information extracted from experience is provided to a teacher, whose behavior is then distilled into a student model that has no access to it. However, both existing forms of context distillation have limitations. Off-policy context distillation trains the student on teacher-generated trajectories and thus suffers from exposure bias;...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21427

### 2610.22080: Learning from Unverified Peers via Shared Residual Distillation
- **Authors**: Chen, Feiyang, Ma, Runze, Wang, Zichen, Lou, Jiong, Wang, Zihan, Zheng, Shuangjia, Li, Jie
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: A language model can generate several solutions to the same problem, some leading to correct answers and others to incorrect ones. Many post-training methods turn these trajectories into learning signals using supervision from reference answers, verifiable feedback, or external teachers. Without such supervision, learning from the model's own generations becomes less straightforward, as their correctness cannot be reliably assessed. An incorrect solution may nevertheless contain useful intermediate reasoning, so it...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22080

### 2610.20642: CoTS: Competitive Token Selection for Latent Reasoning in Large Language Models
- **Authors**: Yu, Jie, Sun, Yuxi, Li, Zhaoxu, Liu, Chunxiao, Jiang, Xudong
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Computation and Language (cs.CL) ; Artificial Intelligence (cs.AI)
- **Abstract**: Recent latent reasoning methods move beyond discrete Chain-of-Thought (CoT) by replacing sampled tokens with continuous soft embeddings or hidden states, enabling richer intermediate representations and preserving alternative reasoning paths. However, the need for latent reasoning varies across decoding steps: confident predictions favor discrete commitment, whereas ambiguous steps benefit from preserving multiple plausible alternatives. Existing approaches typically handle this variation through either global soft...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20642

## Agents/Workflows/Tools (6)

### 2610.21900: TEM: Temporal State Tracking Memory for Large Language Model Agents
- **Authors**: Song, Pengfeng, Zhuang, Yunkai, Shi, Liye
- **Institution/Company**: School of Information and Intelligent Engineering,Zhejiang Wanli University,Ningbo,315100,China
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: An agent's memory must remain useful as information changes across conversations. A new fact may replace an earlier value without making that value irrelevant to a later question. We present Temporal State Tracking Memory (TEM), a training-free framework for tracking these changes. TEM stores facts as versioned records linked to their sources. It retrieves relevant versions, places them in source order and labels historical records before passing the evidence to the answer model. Event memory and original dialogue...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21900

### 2610.20845: Evolving Together, Failing Apart: The Skill-Policy Co-evolution Trap in Self-Improving Agents
- **Authors**: Feng, Yujie, Wang, Xiaobin, Yang, Jinluan, Shi, Xiaonan, Xie, Pengjun, Yu, Philip S., Wu, Xiaoming, Ye, Jieping
- **Institution/Company**: Alibaba Token Hub, Alibaba Group
- **Subjects**: Artificial Intelligence (cs.AI) ; Computation and Language (cs.CL)
- **Abstract**: Skill-policy co-evolution, in which an agent's policy model and its skill bank improve each other during training, is a promising paradigm for self-improving agents. Current evaluations score the co-evolved policy on the final bank it trained with (the delivered bank). After deployment, however, skills may be rewritten, added or removed more frequently than the policy model is retrained, leaving the policy to operate on a drifted skill bank that neither the training objective nor existing evaluation protocols addre...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20845

### 2610.13991: Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents
- **Authors**: Xie, Zixuan, Xu, Chang, Jiang, Yuhua, Zhao, Li
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Machine Learning (cs.LG) ; Artificial Intelligence (cs.AI)
- **Abstract**: Self-evolving agents improve through repeated cycles of modification and evaluation. However, existing methods receive feedback on modifications only after costly evaluations, and aggregate scores may obscure distinctions between failures that require different repairs. We introduce predictive self-evolution through an editable Improvement Dynamics Model (IDM). Before evaluation, the IDM predicts task-level outcomes of a proposed modification and guides an optional revision. After evaluation, past modifications and...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.13991

### 2610.20927: Prune the Summary, Not the History: Source-Judged Compaction for Long-Horizon Agents
- **Authors**: Min, Guanghui, Chen, Chen
- **Institution/Company**: Department of Computer Science
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: Long-horizon LLM agents rely on context compaction: when the interaction history outgrows the context window, a compressor replaces it with a natural-language summary. We show that these summaries contain more than a record of what happened. Compaction prompts ask for decisions and next steps, so each summary mixes facts established by the environment with reasoning written by the compressor, and the agent cannot tell the two apart afterwards. In an analysis of a widely used structured compressor, 83% of failed run...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20927

### 2610.22273: Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries
- **Authors**: Singh, Anikait, Zhang, Teresa, Lee, Yoonho, Nair, Roshen Sanjay, Kumar, Aviral, Finn, Chelsea
- **Institution/Company**: Stanford University
- **Subjects**: Machine Learning (cs.LG) ; Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract**: Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22273

### 2610.21165: From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models
- **Authors**: Gou, Chaogui
- **Institution/Company**: USTB
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time. Existing work on prompt compression, KV-cache management, efficient serving, retrieval augmentation, and agent memory is usually discussed in isolation, leaving the flow of information between storage and computation insufficiently understood. This survey reframe...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21165

## Recommendation/Retrieval/Search (5)

### 2610.18786: Where Do LLM Ensemble Gains Come From? Decomposing Candidate Value, Diversity, and Aggregation
- **Authors**: Kim, Donghwan
- **Institution/Company**: Independent Researcher
- **Subjects**: Computation and Language (cs.CL) ; Artificial Intelligence (cs.AI)
- **Abstract**: LLM ensemble gains are often measured against a single baseline, but the value attributed to additional candidates can change with the comparison used. We study an LLM aggregator under four matched conditions: Direct (no candidates), Single-slot (one candidate in a multi-slot interface), Duplicate (one candidate repeated), and Multi-candidate (separately generated candidates). Under either non-diverse control, overall candidate gain (CIV) splits algebraically into an additional-candidate contrast (DSV) and a candid...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.18786

### 2610.20247: Scaling Multilingual Mixture-of-Experts: How Language Coverage Changes Capacity and Compute Allocation
- **Authors**: Dag, Joel, Srivastava, Nikit, Zahera, Hamada M., Ngomo, Axel-Cyrille Ngonga
- **Institution/Company**: Data Science Group, Heinz Nixdorf Institute, Paderborn University, Germany
- **Subjects**: Computation and Language (cs.CL) ; Machine Learning (cs.LG)
- **Abstract**: Multilingual models share capacity across languages, so adding languages can hurt performance on existing ones. Mixture-of-experts models expand this capacity with little additional per-token computation. Given this extra capacity, does adding experts reduce what each additional language costs? To answer this question, we propose a repetition-aware joint scaling law relating number of active parameters, training tokens per language, number of experts, and language coverage. Fitted on 26,300 per-language loss observ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20247

### 2610.20773: Selection-Safe Conformal Early Exit: Distribution-Free Coverage under Adaptive Depth
- **Authors**: Habib, Adria Binte, Shihab, Ibne Farabi
- **Institution/Company**: Department of Computer Science, BRAC University
- **Subjects**: Machine Learning (cs.LG) ; Machine Learning (stat.ML)
- **Abstract**: Calibrating a conformal prediction set at each early exit does not preserve coverage once a data-dependent exit is selected. We construct one terminal path score from prefix maxima, calibrate a single split-conformal quantile, and return nested prefix sets that all contain the valid terminal set. The guarantee is selection-safe without an alpha/L correction and holds simultaneously for every post-calibration label-free stopping policy that preserves terminal-set containment. We also bound the efficiency cost of the...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20773

### 2610.22256: BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks
- **Authors**: Zhu, Max, Sun, Bohang, Lio, Pietro, Yu, Jialin
- **Institution/Company**: University of Cambridge University of Oxford
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations. The reemergence of sparse $\relu$ and $\relu^2$ activations creates a third opportunity: losslessly compressing the activation cache itself. We present BitSparse, a GPU-resident lossless compression format for sparse activations. Compression and reconstruction run in custom Triton kernels fused into an autograd function, s...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22256

### 2610.21562: A Quantum Machine Learning Approach to Content-Based Media Recommendation
- **Authors**: Abbaszadeh, Mina, Moumou, Ouissal, Pearson, Anna, Coecke, Bob, Cooper, Rob, Piscopo, Alessandro, Sadrzadeh, Mehrnoosh
- **Institution/Company**: University College London
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: We use quantum machine learning techniques to develop a content-based media recommender system and evaluate its performance on TV programmes using textual descriptions from one week of BBC iPlayer data. Grounded in the Quantum Natural Language Processing framework (QNLP), programme synopses are mapped to variational quantum circuits using their semantic structure. The parameters of these circuits are trained via a supervised pairwise similarity learning task. We benchmark the quantum recommender against a classical...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21562

## Sequential/Time-Series/Forecasting (7)

### 2610.20637: Expanding Attention: A Taylor-Series Route to Linear-Time Transformers with a Fixed Number of Recurrent States
- **Authors**: Huang, Zicong
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: We expand the exponential kernel of attention into a truncated Taylor series of $n$ terms and factorize each term into a tensor-power inner product, which collapses the causal history into exactly $n$ recurrent states, each updated by one rank-one outer product per token and independent of context length $N$. The recursion is lossless with respect to the truncated kernel ($2.2 \times 10^{-16}$ in float64), and the states are additive across chunks ($5.7 \times 10^{-14}$), so prefill admits a parallel scan. Measured...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20637

### 2610.21060: Bellman-Consistent Trajectory RL for LLM Arithmetic Reasoning
- **Authors**: Li, Lianfa
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Machine Learning (cs.LG) ; Artificial Intelligence (cs.AI)
- **Abstract**: To address sparse terminal rewards in LLM arithmetic reasoning, we propose a Bellman-consistent trajectory RL method. Our framework introduces Trajectory Bellman Residual Minimization (TBRM) to transform sparse rewards into dense token-level signals. We integrate a Reinforce Leave-One-Out (RLOO) group strategy to reduce gradient variance of Bellman residuals and use hindsight goal relabeling to accelerate intermediate learning. Evaluated on the Countdown task, our method alleviates optimization bottlenecks and stab...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21060

### 2610.21419: What Does History Add? Calendar Controls and Information-Timing Audits for University Trajectory Forecasting
- **Authors**: Cao, Zepei
- **Institution/Company**: East China Normal University
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: We audit the predictive value of historical summaries in a rule-based university trajectory simulator. Seventeen ridge specifications and persistence separate current plans, past-state and past-plan summaries, and calendar-only history-length indicators. Across training, validation and two family-held-out evaluations, we reconstruct 16,750 routes and 804,000 monthly records. On the original 40-family set, six-month history lowers six-step normalized RMSE from 0.159234 to 0.151522, but its difference from a length-o...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21419

### 2610.20669: Value-Informed Schedule Trimming for Accelerated Sequential Monte Carlo Guidance in Discrete Diffusion
- **Authors**: Kim, Jaehyeon, Lee, Ziseok, Choi, Siyoung, Kim, Kyungsu
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Artificial Intelligence (cs.AI) ; Machine Learning (cs.LG)
- **Abstract**: Reward-guided discrete diffusion enables test-time alignment with downstream objectives, but applying Sequential Monte Carlo (SMC) guidance at every denoising step is computationally expensive. Active guidance steps require additional reward evaluations and, for gradient-based proposals, value-gradient computations. Sparse guidance reduces this cost by guiding only a subset of timesteps, but commonly used schedules are fixed heuristics whose effectiveness can vary substantially across tasks. We propose VISTA, a tra...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20669

### 2610.20894: Stochastic Gradient Descent: A Nonlinear Time Series Perspective
- **Authors**: Li, Jiaqi, Lou, Zhipeng, Richter, Stefan, Wu, Wei Biao
- **Institution/Company**: Department of Statistics, Rice University, USA
- **Subjects**: Machine Learning (stat.ML) ; Machine Learning (cs.LG); Statistics Theory (math.ST)
- **Abstract**: This paper investigates the statistical behavior of Stochastic Gradient Descent (SGD) with constant step size under the framework of iterated random functions. Compared to previous studies establishing the convergence of SGD in probability measure, e.g., Wasserstein distance, our approach directly provides the convergence in Euclidean distance by showing the Geometric Moment Contraction (GMC) of SGD. This new convergence can address the non-stationarity of SGD due to fixed initial points and can provide a more refi...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20894

### 2610.21742: Sparse Federated Echo State Networks for Time-Series Classification via Smooth-L1 Regularization
- **Authors**: Lyu, Gengcheng, Röder, Manuel, Schleif, Frank-Michael
- **Institution/Company**: Faculty of Computer Science and Business Information Systems
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Echo State Networks (ESNs), as lightweight implementations of reservoir computing, provide efficient solutions for temporal data processing in resource-constrained environments. While standard ESNs offer computational efficiency, their dense readout layers inflate the stored model and the per-sample inference cost. This paper introduces a Smooth-L1 regularized ESN (SL1ESN) that promotes sparsity in the readout layer while preserving differentiability for gradient-based optimization. The method employs a twice-diffe...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21742

### 2610.21958: ChronoSheaf: Joint Spatio-Temporal Spectral Filtering on Cellular Sheaves
- **Authors**: Mostafa, Abeer, Ahmadi, Zahra
- **Institution/Company**: Peter L. Reichertz Institute for Medical Informatics, Hannover Medical School, Germany
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Sheaf neural networks generalize graph neural networks by assigning each edge a learned linear restriction map that specifies how the local representations of adjacent nodes relate to one another, thereby mitigating oversmoothing. Existing sheaf architectures, however, define the sheaf Laplacian as an instantaneous spatial operator and therefore cannot explicitly model how signals evolve over time on a graph. We first introduce a spectral sheaf Laplacian, defined jointly over space and time, such that a single oper...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21958

## Efficiency/Quantization/Sparsity (5)

### 2610.21640: ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training
- **Authors**: Tian, Yukun, Su, Junwei, Xu, Haofeng, Diao, Lansong, Qian, Zhengping, Zhao, Weibo, Zhou, Wenchao, Zhou, Ruiting, Wu, Chuan
- **Institution/Company**: The University of Hong Kong
- **Subjects**: Machine Learning (cs.LG) ; Distributed, Parallel, and Cluster Computing (cs.DC)
- **Abstract**: Reinforcement learning (RL) has been a critical paradigm for improving large language model (LLM) reasoning and agentic capabilities, but its efficiency remains a major bottleneck. Existing RL systems commonly rely on asynchronous execution to overlap rollout generation with policy optimization for enhanced efficiency. However, this approach faces inherent limitations: mild policy staleness offers only limited training efficiency gains, whereas aggressive asynchrony can degrade model quality and yields diminishing...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21640

### 2610.22256: BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks
- **Authors**: Zhu, Max, Sun, Bohang, Lio, Pietro, Yu, Jialin
- **Institution/Company**: University of Cambridge University of Oxford
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations. The reemergence of sparse $\relu$ and $\relu^2$ activations creates a third opportunity: losslessly compressing the activation cache itself. We present BitSparse, a GPU-resident lossless compression format for sparse activations. Compression and reconstruction run in custom Triton kernels fused into an autograd function, s...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22256

### 2610.21742: Sparse Federated Echo State Networks for Time-Series Classification via Smooth-L1 Regularization
- **Authors**: Lyu, Gengcheng, Röder, Manuel, Schleif, Frank-Michael
- **Institution/Company**: Faculty of Computer Science and Business Information Systems
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Echo State Networks (ESNs), as lightweight implementations of reservoir computing, provide efficient solutions for temporal data processing in resource-constrained environments. While standard ESNs offer computational efficiency, their dense readout layers inflate the stored model and the per-sample inference cost. This paper introduces a Smooth-L1 regularized ESN (SL1ESN) that promotes sparsity in the readout layer while preserving differentiability for gradient-based optimization. The method employs a twice-diffe...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21742

### 2610.20637: Expanding Attention: A Taylor-Series Route to Linear-Time Transformers with a Fixed Number of Recurrent States
- **Authors**: Huang, Zicong
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: We expand the exponential kernel of attention into a truncated Taylor series of $n$ terms and factorize each term into a tensor-power inner product, which collapses the causal history into exactly $n$ recurrent states, each updated by one rank-one outer product per token and independent of context length $N$. The recursion is lossless with respect to the truncated kernel ($2.2 \times 10^{-16}$ in float64), and the states are additive across chunks ($5.7 \times 10^{-14}$), so prefill admits a parallel scan. Measured...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20637

### 2610.21483: FlashAttention with Statistics: Low-Overhead Attention Features for Compact Hallucination Detectors
- **Authors**: Volodichev, Andrei, Savichev, Maksim, Sviridov, Nikita, Yuliy, Artem, Simakov, Dmitry, Zaytsev, Alexey
- **Institution/Company**: Applied AI Institute
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: Large language models can produce fluent answers that the supplied context does not support. A compact frozen proxy model can detect such answers by reading the context and another model's response, even from a proprietary generator. Attention-based detectors use summary statistics of the proxy's attention weights, but standard pipelines materialize the attention matrix, whose memory grows quadratically with sequence length. We compute these statistics without materializing attention, by accumulation in the FlashAt...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21483

## Other Notable (10)

### 2610.20668: CascadeLedger: Counterfactual Auditing of Information and Resource Integrity in LLM Cascades
- **Authors**: Hu, Miaobo, Hu, Shuhao, Guo, Xiaobo, Wang, Xin, Wang, Bokun, Zha, Daren, Xiao, Jun
- **Institution/Company**: School of Artificial Intelligence, University of Chinese Academy of Sciences, Beijing, China
- **Subjects**: Cryptography and Security (cs.CR) ; Computation and Language (cs.CL); Machine Learning (cs.LG)
- **Abstract**: We introduce CascadeLedger, a counterfactual execution-audit framework for budgeted language-model cascades. The protocol enforces call-before-read semantics, binds successful reads to service and cache identities, records availability and component-wise budget transitions, and freezes the event trace before any target or task scorer is joined. The central object is aggregate-equivalent trace validity: two executions can share a final answer, declared resource projection, and service histogram while differing in wh...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20668

### 2610.19705: RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing
- **Authors**: Wang, Xiaohan, Zhang, Haozhen, Liu, Qingyuan, Feng, Tao, Wang, Wenya
- **Institution/Company**: Nanyang Technological University
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: LLM routing dynamically selects and coordinates heterogeneous language models across diverse tasks. However, existing approaches are largely built around a predefined execution paradigm, such as single-round, multi-round, or agentic routing, which fixes how model calls are organized and limits adaptation to different query needs. We propose RouteWeaver, a unified routing framework that integrates these routing modes within a single LLM policy, jointly learning which mode to use and how to select models within that...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.19705

### 2610.22300: Knowledge That Is Linear Before Fine-Tuning Generalizes After It
- **Authors**: Mehri, Faridoun, Schütze, Hinrich
- **Institution/Company**: Center for Information and Language Processing, LMU Munich
- **Subjects**: Computation and Language (cs.CL) ; Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Abstract**: Not all facts a language model can recall support further learning equally well. We distinguish active facts, which support generalization beyond their own recall, from inert facts, which can be recalled but do not support such generalization in a given task. We study this distinction by constructing new relations from existing ones. Take the relation that maps a place to its continent (Paris -> Europe) and assign each of its answers an arbitrary new label (Europe -> crab, Asia -> zebra). The new relation then maps...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22300

### 2610.22324: Training Reasoning Models to Generate Diverse Scientific Ideas
- **Authors**: Wadhwa, Manya, Venkit, Pranav Narayanan, Hayashi, Hiroaki, Li, Yu, Chakrabarty, Tuhin, Wu, Chien-Sheng
- **Institution/Company**: New York University
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must propose a set of ideas that are each high-quality and clearly distinct from one another, while also being...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22324

### 2610.21808: RoleQ: Role-Aligned Scales for Converting Language Models to Ternary
- **Authors**: Knittel, Johannes, Helbling, Alec, Pfister, Hanspeter
- **Institution/Company**: Harvard University
- **Subjects**: Artificial Intelligence (cs.AI) ; Computation and Language (cs.CL)
- **Abstract**: Weight quantization below four bits shrinks memory and bandwidth at a perplexity that looks acceptable, but often at the cost of factual knowledge and task accuracy. Ternary weights have mostly been obtained by training from scratch or long fine-tuning. We introduce RoleQ, a quantization framework that places scales by the functional roles of Transformer units rather than by the layout of the weight matrix, as conventional formats do. Vectors that read from the residual stream take one scale per output unit; those...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21808

### 2610.21346: ARGUS: An Agenda-Driven Framework for Reliable User Simulation
- **Authors**: Zheng, Hang, Jiang, Nan, Zhu, Zichen, Yang, Zixu, Tang, Zhiyang, Fan, Shuai, Chen, Lu, Wu, Xiaobao, Yu, Kai
- **Institution/Company**: X-LANCE Lab, School of Computer Science, MoE Key Lab of Artificial IntelligenceSJTU AI Institute, Shanghai Jiao Tong University, Shanghai, China
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: High-fidelity user simulators are essential for evaluating and training agents in interactive environments. However, current LLM-based simulators struggle with reliability issues, such as goal omission and policy non-compliance. We propose ARGUS (Agenda-dRiven Goal-oriented User Simulator), a neuro-symbolic framework that maintains the user's goal state using a dynamic agenda stack manipulated via symbolic operations. By rigorously decoupling state tracking from natural language generation, ARGUS facilitates strict...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21346

### 2610.20823: Feasibility Ceilings Before Learning: Sizing and Timing Bounds for Drone-Mesh Interception
- **Authors**: Babarytskyi, Dmytro
- **Institution/Company**: Kharkiv National University of Radio Electronics
- **Subjects**: Robotics (cs.RO) ; Machine Learning (cs.LG); Multiagent Systems (cs.MA)
- **Abstract**: A mesh of interceptors defending a fixed site must spread over the predicted arrival point of an approaching object. This is a recurring task in multi-agent robotics: N agents, each covering a disc of radius r, spread over a probability density so that a point drawn from it falls within some agent's disc. We give closed forms for the quantities that bound performance before any policy is chosen, and validate each by Monte Carlo. The uncertainty of a point predicted by extrapolating a noisy linear track follows from...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20823

### 2610.20666: Accord: Schelling-Point Arbitration as a Composable Solana Primitive
- **Authors**: Schuh, Fabian
- **Institution/Company**: not stated (no Affiliation block in arXiv HTML)
- **Subjects**: Computer Science and Game Theory (cs.GT)
- **Abstract**: Accord is an arbitration oracle on Solana. Any Solana program can create an application specific court (i.e. subaccord) and file disputes. A random jury of a specialized, stake-weighted juror pool reviews encrypted evidence and votes under commit--reveal. Jurors that vote with the final ruling earn fees and slashed stake. Jurors that vote against it lose stake. Appeals grow the panel stepwise from 3 to 31 jurors, which raises both the cost of maintaining a captured verdict and, under certain conditions, the probabi...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20666

### 2610.21333: QuasiLeak-Bench: Evaluating LLM-Based Privacy Detectors on Policy-Conditioned Quasi-Evidence Group Recovery
- **Authors**: Zhu, Yufan, Jiang, Yangfan, Fei, Yang, Hou, Shizheng, Mohapatra, Shubhankar, Xiao, Xiaokui
- **Institution/Company**: School of Computing, National University of Singapore, Singapore
- **Subjects**: Computation and Language (cs.CL) ; Cryptography and Security (cs.CR)
- **Abstract**: Natural language messages often contain quasi-identifiers that are weak in isolation but can jointly reveal an individual's private attributes. We call such a jointly revealing set of cues a quasi-evidence group. Existing privacy benchmarks focus on explicit identifiers, attribute inference, or task-driven disclosures, leaving inference from quasi-evidence groups largely unmeasured. In practice, whether exposing such a quasi-evidence group violates privacy also depends on sender-specified disclosure policies. We in...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21333

### 2610.17818: Follow the Perturbed Leader for Linear Bandits: $\sqrt{T}$ Regret over General Convex Sets
- **Authors**: Wei, Chen-Yu
- **Institution/Company**: University of Virginia
- **Subjects**: Machine Learning (cs.LG) ; Machine Learning (stat.ML)
- **Abstract**: We give the first adversarial linear bandit algorithm based on Follow-the-Perturbed-Leader (FTPL) that achieves $\sqrt{T}$ regret over general convex action sets. Our algorithm attains $\widetilde{\mathcal{O}}(d^{5/4}\sqrt{T})$ regret using only linear optimization oracles, and the near-optimal $\widetilde{\mathcal{O}}(d\sqrt{T})$ regret when an optimal-design exploration distribution is further available. This improves on the $T^{2/3}$ regret of the FTPL algorithm of Dani and Hayes (2006) for general convex sets,...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.17818

