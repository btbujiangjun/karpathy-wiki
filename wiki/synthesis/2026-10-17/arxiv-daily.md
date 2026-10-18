---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-17)
type: synthesis
created: 2026-10-17
updated: 2026-10-17
sources: [arxiv-listing, arxiv-html]
tags:
  - arxiv
  - ai
  - llm
  - recommendation
  - advertising
  - sequential-modeling
  - ctr
  - games
  - daily-digest
---

# arXiv Daily Report (2026-10-17)

Search scope: arXiv listing pages across 26 categories for the past week (Fri 2026-10-16 and Thu 2026-10-15); new-to-wiki candidates selected from 2026-10-16 block and summarized.

## Core AI / LLM / Agents (8)

### 2610.21055: Athanor: An Agent-Native System for Autonomous Post-Training Research
- **Authors**: Yufa Zhou; Yichen Wang; Jiakun Fan; Ziqi Shu; Zhichao Liu; Anru R. Zhang; Neiwen Ling; Zijun Wei
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG); Multiagent Systems (cs.MA)
- **Abstract**: Recursive self-improvement, in which AI systems build stronger AI systems, is one promising route to superintelligence. We study a weaker form that can be measured today: frontier agents post-training a small raw base model with public data, as a test of their research potential. We build Athanor, an open agent-native system for autonomous post-training research (AutoPostTrain) on real GPUs. We give the agents full research autonomy, low-friction engineering tools, and efficient starter code. The agents carry out the research themselves: they read datasets and evaluation results, build their training data, write and modify training algorithms, tune hyperparameters, and analyze the results to decide what to try next. They work in a sandbox and cannot use external teacher models. Athanor&#39...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21055

### 2610.22234: OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents
- **Authors**: Bowen Yang; Kaiming Jin; Zichen Ding; Zhenyu Wu; Zehao Li; Zhoumianze Liu; Kanzhi Cheng; Fangzhi Xu; Yanan Sun; Qiushi Sun; Yu Qiao
- **Institution/Company**: University of Science and Technology, Shanghai Jiao Tong University, Shanghai AI Laboratory, Jiaotong University, National University, Nanjing University, Fudan University
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)
- **Abstract**: Real desktop automation is neither purely visual nor purely programmatic. Agents must understand user-facing interfaces while efficiently manipulating files, scripts, and system state. However, native GUI/code coordination cannot be obtained by prompt-level tool composition. In our preliminary experiments, naively adding a code tool degrades a GUI agent, revealing that GUI/code routing must be internalized through training on high-quality hybrid data. We present OS-Helix, an end-to-end trained multimodal computer-using agent that unifies GUI actions and code execution in one action space. To construct the required supervision, we introduce application-artifact composition, pairing desktop applications with authentic file artifacts to instantiate executable Ubuntu states, and a decoupled in...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22234

### 2610.22344: MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering
- **Authors**: Shangheng Du; Jinxin Shi; Shuaiyu Zhang; Yiming Wu; Junpeng Zhao; Shiyang Feng; Xin Li; Liang He; Xiangchao Yan; Bo Zhang
- **Institution/Company**: Shanghai Artificial Intelligence Laboratory, East China Normal University
- **Subjects**: Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)
- **Abstract**: Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent MLE systems adopt model-directed interaction, allowing models to autonomously organize experiments and adapt optimization strategies based on execution feedback. However, feedback from each experiment reflects several preceding decisions, and a long MLE run contains many such costly experiments. Training must therefore select useful supervision from long interaction trajectories...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22344

### 2610.21887: MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents
- **Authors**: Vishal Bhutani; Prasang Gupta; Sumanth Chundru; Kevin Paul
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Multiagent Systems (cs.MA)
- **Abstract**: Humans often learn fastest not by repeating success, but by remembering which failures not to repeat. Open-ended self-improving agents can share experience across lineages, as in GEA, or edit their own improvement mechanisms, as in DGM-Hyperagents, yet failed improvement attempts are rarely retained as reusable cross-branch knowledge, and search can collapse onto redundant strategies. We introduce MetaShare, a failure-aware framework that records successful and unsuccessful agent modifications together with signed performance deltas. Before each generation, MetaShare retrieves diverse high-performing strategies alongside high-confidence failures from other lineages, letting agents reuse effective mechanisms while avoiding known dead ends. A task-blind auditor periodically injects absent or...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21887

### 2610.20926: SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills
- **Authors**: Enze Ma; Chunyu Miao; Yankai Chen; Jie Yang; Liancheng Fang; Kening Zheng; Hanrong Zhang; Muyao Xu; Xinle Yu; Chengze Li; Wei-Chieh Huang; Ziwei Ren; Yunhao Du; Zhixiang Shen; Xue Liu; Philip S. Yu; Zhen Wang
- **Institution/Company**: Zayed University of Artificial Intelligence University, Los Angeles Independent Researcher University, Zhen Wang University, San Diego University
- **Subjects**: Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract**: Agent skills turn procedural knowledge into reusable artifacts, allowing LLM agents to accumulate and refine expertise through experience. Building on this, skill evolution iteratively improves skills using execution feedback. However, improvement may require several interdependent edits, so low-reward versions can still be worth developing. Requiring immediate reward gains can discard useful partial repairs before their benefits emerge. Non-elitist evolution allows new versions to receive further edits despite scoring below earlier ones. For agent skills, this calls for evidence of what to preserve and repair next. We introduce SkillNEO (Non-Elitist Evolutionary Optimization for Agent Skills), which separately selects a version to use and versions to keep improving. Comparing how related ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20926

### 2610.21375: Memorilla: Latent Semantic Memory for LLMs
- **Authors**: Adibvafa Fallahpour; Parsa Idehpour; Vignesh Kothapalli; Nikita Mounier; Shirley Wu; Shayan Pardis; Jure Leskovec
- **Institution/Company**: Stanford University, Vector Institute, Arc Institute
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Abstract**: Memory enables large language models (LLMs) to use information beyond their parameters, such as past user conversations, long documents, or an agent&#39;s earlier actions. For a frozen LLM, access to this accumulated knowledge is limited to what a memory system places in its context window. However, gathering and combining relevant information needed for each query while keeping the model&#39;s context short remains challenging for existing systems. Here we introduce Memorilla, a memory system that gathers information from an entire document collection into a fixed number of query-dependent &#39;memory tokens&#39; for a frozen LLM. Memorilla encodes documents (such as user chats, book chapters) once into reusable embeddings, then learns to retrieve and place query-specific information in t...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21375

### 2610.22174: Mosaic: Multi-Session Agentic Reinforcement Learning
- **Authors**: Yilong Xu; Minrui Xu; Xinyu Zhou; Xiang Long; Haochen Tan; Zhijiang Guo
- **Institution/Company**: Foundation Model Lab, City University
- **Subjects**: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Abstract**: Most existing agentic reinforcement learning methods assume single-session trajectories, where interaction proceeds within one continuously accumulated context. However, agentic techniques such as context compaction and subagent forking may produce trajectories spanning multiple sessions, creating a mismatch between the single-session training assumption and inference-time execution. Therefore, we introduce Multi-Session Agentic Reinforcement Learning, a more general setting that supports an arbitrary number of sessions within a trajectory. Under this setting, a widely adopted method is to broadcast trajectory-level advantages to all sessions, but this does not distinguish contributions from various sessions or guide session allocation within trajectories. To address this issue, we propose...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22174

### 2610.22322: Learning Self-Orchestration in Decentralized Agent Swarms
- **Authors**: Guowei Xu; Zhenting Qi; Amani Kiruga; Himabindu Lakkaraju; Yilun Du
- **Institution/Company**: Harvard University
- **Subjects**: Multiagent Systems (cs.MA); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract**: The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in decentralized agent swarms. Agents express their willingness to participate through bids, which determine who acts and how collective outcomes provide local training credit. Learning both action and bidding behavior allows individual capabilities and patterns of participation to adapt together without a central coordinating agent. We evaluate MPT on embodied crafting, robot navigation, and...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22322

## Reasoning / RL / Post-Training / Test-Time (13)

### 2610.20814: Gibbs-Gap Policy Optimization for Off-Policy RL with Verifiable Rewards
- **Authors**: Xuanchang Zhang; Tong Zhang
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)
- **Abstract**: Reinforcement learning with verifiable rewards often trains language models on responses generated by a different, possibly stale behavior policy. Correcting this mismatch with learner-to-behavior importance weights can introduce high variance for long responses. We introduce Gibbs-Gap Policy Optimization (GGPO), which minimizes a log-mean-exp contrast of KL-adjusted rewards among responses to the same prompt, without learner-to-behavior importance weights. We derive GGPO from KL-regularized policy optimization: on policy, its population loss is exactly the KL-regularized optimality gap, and under suitable coverage the learner&#39;s single-response expected reward is at least the behavior policy&#39;s best-of-$K$ reward, minus terms for the raw finite-group loss, regularization, and finite...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20814

### 2610.20898: Wrong Votes, Right Gradients: Why Majority-Vote Rewards Track Verifiable RL
- **Authors**: Dylan P. Wilson; Chengsong Huang; Jiaxin Huang
- **Institution/Company**: Washington University, Dartmouth College
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract**: Reinforcement learning with self-generated labels, such as majority vote over a model&#39;s own samples, often recovers most of the gain of training with verifiable rewards. This is puzzling from the usual prompt-level view, in which majority vote only returns a model&#39;s modal answer and cannot add information about correctness. We argue that the relevant unit is the batch-level update. Because parameters are shared, a prompt&#39;s own gradient accounts for less than 1\% of the change in that prompt&#39;s output at practical batch sizes, so a wrong label matters only to the extent that label errors share a direction across prompts. We decompose the majority-vote update into shrinkage and misdirection relative to the gold update, and show that misdirection vanishes with batch size whenev...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20898

### 2610.21337: Does On-Policy Distillation Need to Complete Every Rollout?
- **Authors**: Zhengxin Zhang; Maosen Tang; Ning Wang; Changhao Li; Jingren Zhou; Bo Dai; Sainyam Galhotra; Alex Townsend; Claire Cardie
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Abstract**: On-policy distillation (OPD) effectively transfers capabilities from a teacher to a student through feedback on student-generated rollouts. However, generating complete student rollouts and computing teacher feedback for every token make OPD computationally expensive. We introduce Stochastic Truncated On-Policy Distillation (STOPD), which accelerates OPD by randomly truncating student rollouts and correcting the resulting sampling bias with blockwise inverse-probability weighting (IPW). At each training step, we sample a stopping position for each rollout before generation and let the student generate until that position or natural termination. We obtain teacher feedback on every generated token and use blockwise IPW to compensate for the lower probability of retaining later tokens while c...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21337

### 2610.21195: Condition-Contrastive Extrapolation for On-Policy Distillation of Language Models
- **Authors**: Wenxuan Luo; Chenxi Li; Haoyue Liu; Yongxin Guo; Xiaoying Tang
- **Institution/Company**: Shenzhen Future Network of Intelligence Institute, Guangdong Provincial Key Laboratory, The Chinese University
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: On-policy distillation (OPD) improves a student language model by training on its own generated trajectories with supervision from a stronger teacher. However, when conditioned on student-generated prefixes, the teacher can favor invalid continuations that violate the question&#39;s premises, causing OPD to encourage erroneous reasoning steps. As a remedy, we introduce Condition-Contrastive Extrapolated On-Policy Distillation (CCE-OPD), which makes teacher supervision sensitive to question conditions. CCE-OPD incorporates (1) a fixed-prefix comparison in which the same frozen teacher evaluates the complete question and a counterpart with a selected condition masked, and (2) a bounded log-probability contrast that reweights the teacher distribution into an auxiliary distillation target. On ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21195

### 2610.21601: Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation
- **Authors**: Bingxi Hou; Guochao Jiang; Guofeng Quan; Weiqing Li; Wenfeng Feng; Guohua Liu; Yuewei Zhang
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)
- **Abstract**: Policy-shift distillation reuses the difference between a teacher&#39;s log probabilities before and after reinforcement learning (RL) as supervision on student-generated trajectories. However, this endpoint policy shift cannot reveal whether local action preferences evolved consistently during teacher training. The same endpoint shift can result from early and late shifts that reinforce or partially cancel each other. We investigate whether agreement between early and late teacher policy shifts can guide selective transfer. We introduce Waypoint-guided On-Policy Distillation (Waypoint-OPD), which uses an intermediate teacher checkpoint from the same RL run to compare early and late shifts in relative action preferences at student-visited prefixes. We gate the endpoint shift according to t...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21601

### 2610.22236: Training-Free On-Policy Distillation
- **Authors**: Bangji Yang; Jiajun Fan; Zhaoyu Zhu; Hongbo Ma; Ge Liu
- **Institution/Company**: Tsinghua University
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract**: On-policy distillation consolidates specialist models into one student at the price of rollouts, teacher passes and gradient steps for every teacher. We show that the consolidation does not need training: with forward passes only, the capabilities of separately tuned specialists can be aggregated into one model that is, on average, more accurate than either specialist alone. When specialists share a base model, distillation has an exact layer-wise solution: each linear layer of the fused model must reproduce every specialist&#39;s output on the inputs that specialist receives while reading its own answers, a least-squares problem whose solution needs only the second moments of those inputs. One forward pass over a few hundred rollouts provides them. We call this training-free on-policy dis...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22236

### 2610.21439: Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment for Multi-Reward RL
- **Authors**: Skylar Zhai; Haonan Wang; Zhining Liu; Linxin Song; Xuwei Ding; Jingcheng Liang; Jian Kang
- **Institution/Company**: National University
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Language models are increasingly trained against several verifiable rewards at once, such as the correctness and the format of a tool call, or the individual constraints of a complex instruction. Reward-decoupled normalization (GDPO) normalizes each reward separately so that different reward combinations keep distinct advantages, but it still spreads every reward&#39;s advantage evenly over the whole response, although each verifier checks only a few positions. We propose MRTPO, which assigns the advantage of each reward to the tokens relevant to it, using the information its verifier checks, without auxiliary models or token-level annotations. For each reward, the policy replays its own response with and without that reward&#39;s verifier information, and the per-token Jensen-Shannon dist...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21439

### 2610.21671: Enhancing Multimodal RLVR with Pairwise Token Contrast and Adaptive Trajectory Confidence
- **Authors**: Yiran Zhang; Hanbo Huang; Jielan Li; Zhen Zhao; Shiyu Liang; Hongxia Hao
- **Institution/Company**: Shanghai Artificial Intelligence Laboratory, Shanghai Jiao Tong University
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: Reinforcement learning with verifiable rewards (RLVR) improves multimodal reasoning, but group-relative policy optimization broadcasts a single sequence-level advantage to every token of a response, although errors usually localize to a few decisive steps. Recent self-distilled variants refine credit with a teacher--student likelihood gap. However, this signal cannot tell whether it relies on the image or on a language shortcut, and is applied uniformly even when the teacher is uninformative. To address this, we propose Pairwise token contrast and Adaptive trajectory ConfidencE (PACE). Pairwise token contrast scores each response under four teacher views, crossing a correct or incorrect answer hint with the image present or removed, and compares the two hints for every token, which cancels...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21671

### 2610.22290: EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity Search
- **Authors**: Hanane Nour Moussa; Doeun Lee; Sachin Kumar
- **Institution/Company**: The Ohio State University
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: Reinforcement learning has become a common post-training technique to improve the accuracy of LLMs on verifiable tasks. However, such training can narrow the set of solutions the model can produce. Several approaches have attempted to address this behavior-sharpening effect, but they often optimize metrics that do not reflect the diversity of correct solutions. Ideally, we want a model that can produce multiple good solutions, not only a single reliable one. We propose EliteReplay, a post-training recipe that pairs GRPO with an &#34;elite&#34; archive built by quality-diversity search. Before training, we use the frozen base model to collect solutions that span distinct approaches; during training, GRPO is combined with a replay loss on this archive. The result is a post-trained model that...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22290

### 2610.22331: KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents
- **Authors**: Siqi Chen; Zhengxi Lu; Yuchen Yan; Xingyu Wu; Qipeng Chen; Xin Zhang; Aiting Liu; Chao Deng; Jie Liu; Jin Ma; Weiming Lu; Jun Xiao; Yongliang Shen
- **Institution/Company**: Zhejiang University, Knowledge-Group
- **Subjects**: Artificial Intelligence (cs.AI)
- **Abstract**: Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinforcement learning provides only a single terminal reward shared across an entire trajectory. Recent process-supervision methods aim to assign credit at finer granularity, but they typically anchor credit to either surface-level trajectory states or model-internal signals, both of which become unreliable in deep search where observations are heterogeneous and retrieved contexts are long and noisy. We propose KnowGPO, a reinforcement learning framework that aligns trajectories by the task-relevant knowledge they have acquired rather than by their surface observations. For each query, KnowGPO deco...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22331

### 2610.21018: Failure Is the Mother of Success: Recovering Supervision with Grounding Hindsight
- **Authors**: Sheldon Yu; Tong Yu; Nikki Lijing Kuang; Zhendong Chu; Zhenwei Tang; Sungchul Kim; Lina Yao; Julian McAuley; Junda Wu
- **Institution/Company**: San Diego Adobe Research University, University of Toronto University
- **Subjects**: Artificial Intelligence (cs.AI); Machine Learning (stat.ML)
- **Abstract**: When every rollout for a problem fails, GRPO receives neither a successful exemplar nor a nonzero group-relative advantage, so it learns nothing from exactly the problems it most needs to learn. The failed reasoning can nevertheless suggest what to try next. We present Replay-Selected Hindsight Distillation (RSHD), which turns failed attempts into an additional, tested source of supervision during GRPO training. The policy writes a corrective note about each failed attempt without seeing a reference answer or solution, then re-solves the problem with the note in context. A note is admitted only if its replays succeed more often than the original group did, after screening for notes that state the answer, and an admitted replay is distilled into the plain-prompt policy. Because admission is...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21018

### 2610.20639: Same Answer, New Box: How Much of RLVR&#39;s Out-of-Domain Gain Is Answer Format?
- **Authors**: Zongye Lyu
- **Institution/Company**: Faculty of Information Technology, Monash University
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)
- **Abstract**: Reinforcement learning with verifiable rewards (RLVR) is credited with gains beyond the domain its rewards check, such as higher MMLU accuracy after training on mathematics. Such accuracies are usually read out of the model&#39;s text by an answer extractor. A model that learns to write its answer where the extractor looks can therefore score higher without answering better. We measure how much of the gain reported by extractors copied from public code arises this way. We generate outputs from a base model and its RL model and score them twice: with those extractors, and with one extractor of our own that reads a stated answer whether it is in the answer box \boxed{} or in the text. On four released 7B SimpleRL base-RL pairs, 82% of the out-of-domain multiple-choice gain that these extract...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20639

### 2610.21682: Router Drift Control: Mitigating Off-Policy Degradation in Mixture-of-Experts Reinforcement Learning
- **Authors**: Liangyao Jin; Zhixin Wang; Liming Liu; Mingjun Zhang; Zhengzhou Zhu; Fangcheng Fu; Jinlong Hou; Yuan Cheng; Xiaohe Hu; Ping Zhang; Siyuan Feng
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Abstract**: Reinforcement learning (RL) can become off-policy due to training-inference mismatch, mini-batch updates, and asynchronous this http URL resulting mismatch is especially harmful in Mixture-of-Experts (MoE) models, where rollout--training discrepancies can change routing decisions and lead to router drift. Rollout Routing Replay (R3) mitigates this mismatch by reusing expert selections from the rollout stage during training. Our analysis shows that routing replay introduces gradient bias by losing contributions from experts selected by the training router but not the rollout router. To address this, we propose Router Drift Control (RDC), which uses routing disagreement between rollout and training as a signal of off-policy staleness and selectively rejects high-drift responses. The sequence...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21682

## Efficiency / Inference / Serving (7)

### 2610.20641: AbridgeKV: Compressing Long Reasoning into the KV Cache of Learned Pause Tokens
- **Authors**: Jack Cai; Lijie Yang; Vasilis Kontonis; Dimitris Papailiopoulos; Shivam Garg
- **Institution/Company**: Princeton University, Microsoft Research
- **Subjects**: Computation and Language (cs.CL); Machine Learning (cs.LG)
- **Abstract**: Long chain-of-thought decoding is memory-bound: the KV cache of the generated tokens grows linearly with the test-time compute being spent. Evicting cache entries does not fix this, because a model never trained on a cache with entries removed generates longer, often up to the length limit. We instead train the model to compress its own output. AbridgeKV compresses each completed block of generated text into the KV entries of a few learned pause tokens. These are extra input tokens with trained embeddings that produce no output. Once the pause tokens have encoded the block, AbridgeKV frees the block&#39;s original cache; subsequent tokens attend to the pause tokens&#39; KV entries in its place. Three novel choices make this work: the pause tokens&#39; KV entries take positions inside the b...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20641

### 2610.20686: RoLaQ: Joint Rotation and Range Calibration for 2-Bit KV Caches in Multi-Head Latent Attention
- **Authors**: Shiyu Ji; Peng Ling; Chen Lin; Shupeng Li; Yixuan Wang; Qingfu Zhu; Wanxiang Che
- **Institution/Company**: Harbin Institute of Technology, Tsinghua University, Research Center, Baidu Inc
- **Subjects**: Machine Learning (cs.LG); Machine Learning (stat.ML)
- **Abstract**: Multi-head latent attention (MLA) compresses the content of a key-value cache into a shared latent per token, making low-bit storage attractive for long-context inference. At two bits, errors in this representation perturb both attention matching and value readout, with effects that depend on error direction and reconstruction scale. We introduce RoLaQ (Rotation-calibrated Latent Quantization), an offline method for joint rotation and range calibration. RoLaQ refines a shared rotation within subspaces defined by the frozen key and value projections, and jointly learns quantization ranges whose thresholds and reconstruction gains are coupled to control the shared signal&#39;s response. Prediction matching and attention-output supervision guide calibration with model weights frozen. Across t...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20686

### 2610.20865: Long-Context Drafting Does Not Require Long-Context Drafters
- **Authors**: Aref Jafari; Vansh Bhatia; Matt Qin; Subhajit Dutta Chowdhury; Ben Lee; Vikram Appia; Ali Ghodsi; Mehdi Rezagholizadeh
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Speculative decoding pairs a cheap drafter with parallel verification against the target. At ultra-long context it stops paying, because a drafter that attends over the full prefix inherits the target&#39;s context-dependent cost, so the speedup it was meant to provide first erodes and then reverses. The standard response is to build a long-context drafter, by training or fine-tuning one, or by using a multi-token-prediction head shipped inside the target checkpoint. We argue this is unnecessary, because the drafters in use are target-conditioned, reading hidden states the target computed over the entire prefix, so distant context already reaches them without their own attention, and verification corrects what they miss. We therefore freeze released short-context drafters and run them far ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20865

### 2610.21126: Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches
- **Authors**: Wanyang Hong; Zhaoning Zhang
- **Institution/Company**: College of Computer Science and Technology, National University of Defense Technology, National Key Laboratory
- **Subjects**: Computation and Language (cs.CL)
- **Abstract**: Sparse KV compression reduces long-context inference costs by retaining selected historical states, yet these states typically keep their coordinates from the full history. Under Rotary Position Embedding (RoPE), gaps left by evicted tokens continue to affect query-key matching, potentially limiting the use of retained evidence. We study post-selection positional geometry on a fixed selector-produced cache, examining how positional organization affects the use of retained information and which coordinate and continuation rules improve answer quality. To reorganize this geometry, we propose RoPERelay, which assigns compact, order-preserving RoPE coordinates, relocates cached key phases through inverse rotation and re-rotation, and synchronizes the current query and subsequent generation. It...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21126

### 2610.21257: Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference
- **Authors**: Sunghyun Wee; Geunjae Choi; Hyeonjin Kim; Suyoung Kim; Nojun Kwak
- **Institution/Company**: Seoul National University
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Abstract**: Large Language Models (LLMs) demand efficient inference, where the multiply-accumulate (MAC) operations in linear projections dominate compute and energy cost. Post-training quantization (PTQ) reduces this cost by mapping weights and activations to low-bit integers. Power-of-Two (PoT) weight quantization promises efficient multiplier-free LLM inference via shift-add logic, but suffers significant accuracy degradation at low bitwidths due to its coarse base-2 quantization grid. We introduce Fractional PoT (FPoT), a base-$\sqrt{2}$ (half-octave) fractional PoT grid that achieves practical 4-bit weight quantization while preserving a fully integer shift-add datapath. The method combines (i) the base-$\sqrt{2}$ weight grid with uniform integer activations, (ii) a calibration-time grid-alignmen...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21257

### 2610.21810: N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models
- **Authors**: Donghoon Han; Minseop Jung; Dong Woo Kwak; SeungJae Lee; Junhoo Lee
- **Institution/Company**: Dnotitia Inc
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)
- **Abstract**: Conditional memory expands language-model capacity through selective lookup, but the full embedding table must remain available for every possible input. We introduce Conditional Program (CP), a compressed representation that reconstructs only the rows an input requests. CP represents each row by a short code and a local scale, with a reconstruction program shared across the table. We instantiate this representation with a Gaussian trellis, norm restoration and independently decodable row records. CP&#39;s two-bit code lowers output KL by 41--63\% relative to 2-bit round-to-nearest. Analysis across three trained n-gram memory families shows that Gaussian-like coordinate statistics coexist with learned relationships among rows; at matched storage budgets, the shared trellis outperforms the ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21810

### 2610.20682: TurboMamba: Faster Inference, Faster Training, and Better Prediction with Lexical Memory
- **Authors**: Hanxin Zhang
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)
- **Abstract**: We introduce TurboMamba, a language-model architecture for faster inference, faster training, and better token prediction. A global Mamba-3 model runs once per completed token block. A small Transformer uses this global context and earlier tokens within the block to predict the next token. Three lightweight additions improve local predictions: direct access to the previous block&#39;s last token, a small correction to next-token scores, and a learned mixture with recent-token frequencies. We compare twelve small-scale implementations on public FineWeb-Edu, with comparable parameter counts and shared training-budget caps. The baselines include Transformer, Mamba-3, Jamba, and Zamba. The Jamba and Zamba versions use Mamba-3 in place of their original Mamba modules. TurboMamba achieves the lo...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20682

## Recommendation / Advertising / CTR / User Modeling (4)

### 2610.20635: Exploring the Design Space of Permutation Diffusion LLMs
- **Authors**: Zhe Xu; Mingfu Liang; Kavosh Asadi; Jean-Pascal Billaud; Tianyi Chen; Yanhui Guo; Christina Huang; Baekjin Kim; Jimmy Kim; Yufei Li; Daqi Sun; Jiachen Sun; Dian Yu; Zaiwei Zhang; Kaushik Rangadurai; Frank Shyu; Sandeep Pandey; Xi Liu; Luke Simon
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Abstract**: Permutation generation with language models requires both text-conditioned ranking and a global one-to-one assignment between candidates and output positions. We study this problem through three diffusion-LLM parameterizations: hard-assignment prediction over shuffled candidate-index sequences, soft-assignment prediction over doubly stochastic matrices, and direct ordering-score prediction followed by sorting. The three families place permutation constraints at different stages of prediction and decoding and therefore support different training objectives and sampling procedures. We evaluate these designs on recommendation reranking across three Amazon domains with candidate sets of size 10 and 20. At one function evaluation, the hard- and soft-assignment variants achieve Recall@1 comparab...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20635

### 2610.21713: Encoded but Exposed: Language Embeddings can Reveal More Than They Should in Recommender Systems
- **Authors**: Linda Beková; Rodrigo Alves
- **Institution/Company**: Czech Technical University
- **Subjects**: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)
- **Abstract**: Language embeddings are increasingly used in recommenders to represent item content, but their privacy risks remain poorly understood. We study whether item embeddings can reveal item identities when an adversary has access to auxiliary item text from external sources. We show that a simple cosine-similarity attack can recover item identities with high mean reciprocal rank across language models and candidate-set settings on two real-world datasets. Leakage is strongest when the adversary&#39;s partial information overlaps with the victim representation, but it also persists through semantic alignment between independently sourced descriptions. We further show that item leakage can propagate to user re-identification from sparse ratings. Finally, we evaluate obfuscated descriptions as a mi...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21713

### 2610.21938: Agentic-Priors: Using Large Language Models to Address the Cold Start Problem in Preference Elicitation
- **Authors**: Bruno Arcanjo; Zhaoxing Li; Sebastian Stein
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Multiagent Systems (cs.MA); Artificial Intelligence (cs.AI)
- **Abstract**: An agent that learns a user&#39;s preferences from their choices faces a cold start problem: before any choices are observed, it must rely solely on a prior. Informative priors are usually fitted to historical choice data, which new tasks and deployments lack. To address this, we present Agentic-Priors, which lets agentic systems use the implicit knowledge of large language models (LLMs) instead. Specifically, an LLM states a new user&#39;s trade-offs in interpretable terms, such as willingness to pay or value of time, which we map to a prior over multinomial logit coefficients. This prior is then refined by a Bayesian learner as choices are observed. Across seven choice datasets, Agentic-Priors improves cold start accuracy over an uninformed prior by 5-40 percentage points. It also outper...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21938

### 2610.21330: VoteGEO-Bench: Measuring the Impact of Generative Engine Optimization on Electoral Visibility
- **Authors**: Shiqi Zhang; Xiaokui Xiao
- **Institution/Company**: National University
- **Subjects**: Information Retrieval (cs.IR); Computation and Language (cs.CL); Computers and Society (cs.CY)
- **Abstract**: Large language models (LLMs) are increasingly used for election information, yet little is known about how external web content shapes the political information they present. Generative engine optimization (GEO) rewrites web content to improve its visibility in generated responses. To investigate its potential risks in voting scenarios (VoteGEO), we introduce VoteGEO-Bench, a benchmark covering the 2024 U.S. presidential election and the 2026 Japanese House of Representatives election, combining election-related queries, historical webpages, and voter personas. We first analyze sources cited by generative engines and find that many citations come from lower-cost owned and open-platform sources, while some webpages remain visible across days. We then evaluate 11 rewriting strategies in 4 ca...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21330

## IR / Retrieval / Ranking (4)

### 2610.20664: Information-Gain Calibrated On-Policy Distillation for Deep Search Agents
- **Authors**: Chenxi Li; Xueyang Feng; Songyang Liu; Chenxu Wang; Xiaoying Tang; Chaozhuo Li; Litian Zhang
- **Institution/Company**: The Chinese University, Beijing University, Renmin University, Beijing Academy
- **Subjects**: Information Retrieval (cs.IR)
- **Abstract**: On-policy distillation (OPD) has recently emerged as a promising approach for transferring the capabilities of large agents to compact students. In deep search, where agents iteratively retrieve external evidence, a teacher&#39;s preference among plausible queries before retrieval may not predict which queries will return useful evidence. Standard OPD nevertheless supervises each student query from the preceding context alone, inducing a failure mode we term \textbf{\textit{evidence-blind supervision (EBS)}}. To understand this, we regroup the OPD objective by interaction turns and reveal two implicit priors: a \textit{budget prior} that allocates supervision by token volume, and a \textit{direction prior} that favors tokens preferred by the teacher, neither of which accounts for the evide...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20664

### 2610.21877: Aligning LLMs with Sparse Retrieval via Adaptive Sparse Supervision
- **Authors**: Tongna Chen; Minghan Li; Guodong Zhou
- **Institution/Company**: School of Computer Science and Technology, Soochow University
- **Subjects**: Information Retrieval (cs.IR)
- **Abstract**: While large language models (LLMs) offer strong semantic representations, their application to first-stage retrieval incurs substantial latency and storage costs. Neural sparse retrievers such as SPLADE provide efficient retrieval but rely on relatively compact encoders with limited representational capacity. To bridge this gap, we propose an LLM-based sparse retrieval framework with input-adaptive sparse alignment. Specifically, we introduce a dynamic $\alpha$-truncation strategy that selects input-specific supervision supports based on the cumulative activation mass of SPLADE representations. This strategy guides the LLM to preserve salient lexical signals while suppressing less informative activations, without relying on a fixed support budget. Subsequent retrieval fine-tuning combines ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21877

### 2610.20857: Idea2Prior: Auditable Paper Retrieval and Ranking from Research Ideas
- **Authors**: Shitian Yang; Ruijie Tao; Jian Huang
- **Institution/Company**: Johns Hopkins University
- **Subjects**: Information Retrieval (cs.IR)
- **Abstract**: Finding a paper from an informal research idea requires more than matching topic words: relevant work may use different terminology, and its distinguishing mechanism may be absent from the abstract. We present \system{}, an auditable literature-search system built on PaperArena. It combines multi-source discovery, identity verification, facet-based abstract assessment, semantic citation expansion, and joint Expert ranking. A retrieval-only mode ranks up to five papers from a shortlist of at most 60, using complete available abstracts and locally selected PDF evidence from five fixed acquisition attempts, without generating a long-form report. In a historical comparison covering ten queries from each of EASY, MEDIUM, and HARD, aggregate reported Hit@5 is 53.3\% for \system{}, 43.3\% for Cha...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20857

### 2610.21267: TRACER: Trajectory-Aware Tool Retrieval for LLM Agents
- **Authors**: Tanish Kher; Sarvesh DK; Abedelkadir Asi; Sparsha Chennarayapatna Sundaresh; Dezhi Hong
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Information Retrieval (cs.IR)
- **Abstract**: Modern agents select tools from registries, but exposing entire registries incurs high token costs and can impair selection as they grow. We present TRACER, a retrieval front-end that indexes observed tool-call sequences in a trie and ranks continuations using a learned blend of empirical and contextual priors. On a mixed retail-and-telecom $\tau^2$ environment, TRACER improves GPT-5.4&#39;s tool-selection accuracy by 4.7 points while reducing input tokens per step by 80%, exposing just 5 of 128 tools. In autonomous full-turn execution, it matches GPT-5.4&#39;s full-registry task success with 61% fewer input tokens per step. Across six environments and four models, TRACER improves tool-selection accuracy over full-registry selection in 21 of 24 model-environment pairs, with average gains o...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21267

## Sequential / Time Series / Trajectory (8)

### 2610.22327: Twice Upon a Time: Complementary Representations for Time-Series Reasoning
- **Authors**: Hedi Zisling; Liran Nochumsohn; Ilan Naiman; Mihir Parmar; Omri Azencot
- **Institution/Company**: Complementary Representations for Time-Series Reasoning Hedi Zisling Ben-Gurion University, Mihir Parmar Google Omri Azencot Ben-Gurion University
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract**: Time Series Language Models (TSLMs) enable language-based understanding and reasoning over temporal data, yet a fundamental question remains: what information should their time-series representations preserve, and what variation should they factor out? Existing TSLMs typically expose the language model to a single representation, imposing a fixed inductive bias across downstream tasks. We instead introduce complementary representations as a design principle for time-series reasoning. Our model combines two visual views: line plots preserve absolute measurements and the observed coordinate frame, while normalized delay embeddings factor out positive amplitude rescaling and offsets while exposing temporal structure. Dedicated visual encoders integrate both views into a shared language model ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22327

### 2610.21123: DST-Net: Decomposed Spatio-Temporal Network for Time Series Forecasting
- **Authors**: Yaohua Zha; Hai Wu; Shu-Tao Xia
- **Institution/Company**: Tsinghua Shenzhen International Graduate School, Pengcheng Laboratory, Tsinghua University
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Abstract**: Series decomposition has emerged as a widely acknowledged paradigm in deep time series forecasting models. However, existing approaches predominantly employ a homogeneous modeling strategy for all subsequences, thereby overlooking the distinct inductive biases inherent in different components. We identify that the trend component exhibits dominant spatial coupling across channels but carries significant temporal redundancy, whereas the seasonal component is characterized by local temporal evolution but remains susceptible to attention distraction. To address this, we propose a novel disentangled architecture that tailors specific modeling strategies to align with the intrinsic properties of each component. For the trend branch, we design a Latent Graph Block, employing latent graph modelin...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21123

### 2610.20739: Quantile-Guided Diffusion for Probabilistic Time-Series Forecasting
- **Authors**: Shadi Omari; Bashar Khoury; Assaf Schuster
- **Institution/Company**: Israel Institute of Technology
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Quantile forecasts summarize uncertainty at each future time step, while diffusion forecasters represent it through sampled future trajectories. We study how predicted quantiles can serve as distributional controls for diffusion forecasting. Specifically, we investigate how the mechanism of quantile integration affects its effectiveness in guiding a pretrained diffusion forecaster. We find that residual control throughout the denoising network yields the most consistent improvements. We instantiate this approach as Control-TS, which learns a quantile-control pathway while keeping the pretrained backbone frozen. Across eight benchmarks, Control-TS consistently improves the backbone&#39;s CRPS, achieves competitive performance against state-of-the-art forecasting models, and retains its gain...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20739

### 2610.21308: PocketTSLM: Deploying an On-Device Soft-Prompt Time-Series Language Model for Privacy-Preserving Smartphone Reasoning
- **Authors**: Max Rosenblattl; Nikhil Krishnaswamy; Leon Nissen; Manuel Milling; Nicolas Zumarraga; Ning Wang; Thomas Kaar; Robert Jakob; Björn W. Schuller; Elgar Fleisch; Patrick Langer; Paul Schmiedmayer
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)
- **Abstract**: Consumer phones and wearables increasingly collect physiological time-series data, yet most mobile systems treat these streams as summaries or text rather than as temporal evidence. This representation is poorly matched to personal health systems that need to retrieve, route, or summarize sensor evidence while preserving temporal structure. Cloud-hosted time-series language models avoid smartphone limits, but they repeatedly move sensitive physiology off the device and add latency and per-query compute cost. Mobile model alternatives that aggregate time-series data into statistical features or serialize raw samples as text either compress temporal structure or exhaust the context and memory budgets of small on-device models. We present PocketTSLM, a mobile-native deployment of OpenTSLM Sof...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21308

### 2610.22242: SurvICL: a Foundation Model for in-context Survival Analysis
- **Authors**: Julie Alberge; Linus Bleistein; Judith Abécassis; Marine Le Morvan; Gaël Varoquaux; David Holzmüller
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (stat.ML); Machine Learning (cs.LG)
- **Abstract**: Tabular foundation models (TFMs) now outperform gradient-boosted trees in classification and regression. Yet in survival analysis, which predicts when an event occurs from censored data, often on small clinical cohorts, we find that no existing TFM beats the half-century-old Cox model. We address this issue by introducing SurvICL, a TFM that predicts survival curves in-context. SurvICL is pretrained on purely synthetic datasets generated from a novel flexible proportional-odds prior that outperforms other prior types in our ablation study. Unlike most other survival models, SurvICL is trained with a plain quantile regression loss, which is possible because its synthetic pre-training data generator can provide uncensored event times. Additionally, we introduce the largest survival benchmark...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22242

### 2610.21274: TimeCap: A Scalable Open-Source Pipeline for Captioning Wearable Health Time-Series Data
- **Authors**: Max Rosenblattl; Milana Gurbanova; Karl Aurel Deck; Narayan Schuetz; Thomas Kaar; Manuel Milling; Nicolas Zumarraga; Ning Wang; Kelly W. Zhang; Anders Johnson; Robert Jakob; Björn W. Schuller; Elgar Fleisch; Daniel Seung Kim; Allan Lawrie; Patrick Langer; Maxwell A. Xu; Euan Ashley; Paul Schmiedmayer
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL)
- **Abstract**: Time-series data generated continuously across industrial, environmental, and especially health domains produce multimodal signals whose scale and heterogeneity make their processing and interpretation particularly challenging. Time-Series Language Models (TSLMs) promise scalable interpretation of these signals, yet remain bottlenecked by a fundamental lack of text-annotated time series pairs that are signal-grounded, reproducible, and extensible across modalities and schemas. Existing paired corpora are either closed or limited in scale and modality coverage. Annotation with large language models could scale them up, but its outputs cannot be regenerated exactly, which prevents others from re-deriving, extending, or auditing the resulting corpus. To address this, we release TimeCap, an op...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21274

### 2610.22215: FutureLift: Lifting Trajectory Proposals into Bidirectional Future Graphs for Motion Forecasting
- **Authors**: Daniel Grimm; J. Marius Zöllner
- **Institution/Company**: FZI Research Center for Information Technology
- **Subjects**: Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)
- **Abstract**: Accurate motion prediction is critical for safe autonomous driving, yet even strong forecasters leave residual errors in their multimodal proposals. Existing refiners compress complete proposals or update their segments sequentially, preventing the full proposed future from serving as explicit relational context for correction. We introduce FutureLift, a backbone-agnostic refiner that represents each multimodal proposal as a heterogeneous future graph, with spatially grounded temporal nodes connected to agent histories, map elements, alternative modes, and, for joint prediction, other agents future trajectories. Bidirectional temporal edges allow later evidence to revise earlier segments in a single pass, and the updated nodes predict residual coordinate and confidence corrections. Requiri...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22215

### 2610.22358: PathFM: Fast Generative Forecasting of Multivariate Trajectories
- **Authors**: Jiachen Yao; Xiyuan Zhang; Annan Yu; Boran Han; Abdul Fatir Ansari; Shuai Zhang; Michael Bohlke-Schneider; Bernie Wang
- **Institution/Company**: California Institute of Technology
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Time series foundation models are becoming increasingly popular for general-purpose forecasting. However, most leading models predict marginal quantiles, leaving the dependence structure of future trajectories unspecified. This distinction matters for trajectory-dependent quantities such as cumulative demand, peak load, and event timing, yet point and marginal scores do not reveal it. To model this dependence, we introduce PathFM, a trajectory-based forecasting model that uses flow matching to generate complete future paths. We further distill the model to one or two steps and share history attention cache across draws. Together, these enable PathFM to generate multiple paths for a single series in roughly the time needed for one query to a quantile model. The distilled sampler also makes ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22358

## Games / Multi-Agent / Bandits / Mechanism Design (8)

### 2610.20908: Replicable Dueling Bandits
- **Authors**: Rohan Deb; Aadirupa Saha; Udaya Ghai; Karan Singh; Arindam Banerjee
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Abstract**: Dueling bandits choose each comparison based on earlier noisy outcomes, so two runs on the same preferences can compare different pairs. We study replicable dueling bandits, where two executions with shared internal randomness and independent comparison outcomes must select the same ordered pair in every round with probability at least $1-\rho$. Building on Beat-the-Mean, whose scores change as arms are eliminated and need not rank the best arm highest, we design the first such algorithms with sublinear regret. Under relaxed stochastic transitivity with parameter $\gamma\ge 1$ and the stochastic triangle inequality, we design an algorithm that achieves expected regret $\widetilde{O}(\gamma^8 K^4 H_{\mathrm{p}}/\rho^2)$, where $H_{\mathrm{p}}=\sum_{i=2}^{K}(P_{1i}-1/2)^{-1}$. Under strong s...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20908

### 2610.22149: Smoothed analysis of policy iteration and value iteration for deterministic discounted and mean-payoff games played on any graph
- **Authors**: Bruno Loff; Mateusz Skomra
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Computer Science and Game Theory (cs.GT); Computational Complexity (cs.CC)
- **Abstract**: Our understanding of turn-based stochastic games is reminiscent of our understanding of linear programming in the 1970s. Instead of the simplex method, we have two families of algorithms - policy iteration and value iteration - which work well in practice but are known to run in exponential time on some input instances, and we still lack an algorithm that runs in polynomial time on all instances. A recent result by Loff and Skomra showed that, for deterministic discounted and mean-payoff games played on an ergodic graph, a variant of policy iteration runs in smoothed polynomial time. This offered an explanation of why policy iteration performs well in practice, analogous to Spielman and Teng&#39;s explanation for the simplex method. In this paper, we drop the ergodicity assumption: we show...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22149

### 2610.21487: Approximating the Value of Time-Bounded Weighted Timed Games
- **Authors**: Isa Vialard; Joël Ouaknine
- **Institution/Company**: Max Planck Institute
- **Subjects**: Computer Science and Game Theory (cs.GT)
- **Abstract**: The Value Problem for weighted timed games, an extension of timed automata with weights and adversity, consists in determining, given a weighted timed game with a reachability objective and a rational threshold, whether or not the value of the game exceeds the threshold. This problem is known to be undecidable for weighted timed games, i.e., there is no algorithm that can compute the value exactly. A natural alternative is to approximate the value; however, the Approximation problem is also undecidable in general. In this paper, we prove that the Approximation problem is decidable in 4-ExpTime for weighted timed games whose executions are time-bounded.
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21487

### 2610.21582: Transfer Learning in Bandits from Unknown Adaptive Policies: Problem-Dependent Lower and Upper Bounds
- **Authors**: Adrien Prevost; Timothee Mathieu; Waris Radji; Odalric-Ambrym Maillard
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: Transfer learning in stochastic multi-armed bandits is typically studied assuming that prior data forms a fixed offline dataset or is generated by a known source. In practice, historical observations come from a previous adaptive decision process whose policy is unknown. We study this setting for bounded rewards in $[0,1]$. Before the online game starts, the learner receives, for each arm $k$, $N&#39;_k$ observations drawn i.i.d.\ from an unknown distribution $\nu&#39;_k$, collected by an arbitrary and possibly data-dependent strategy, so the sample sizes $N&#39;_k$ may be random. Source and target means satisfy $|\mu_k-\mu&#39;_k|&lt;L_k$ for known constants $(L_k)_k$. We derive an asymptotic problem-dependent lower bound and propose KL-UCB-Transfer, which combines online and historical d...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21582

### 2610.21908: The Tilted Sampling Problem: Optimism, Posterior Sampling, and Logarithmic Regret
- **Authors**: Mohammad Pedramfar; Siamak Ravanbakhsh
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Optimization and Control (math.OC); Machine Learning (stat.ML)
- **Abstract**: Many modern learning systems are used not to select a single best action, but to sample diverse high-quality outputs. Examples include entropy-regularized reinforcement learning, RLHF, and reward-guided generative modeling. Motivated by these settings, we study tilted sampling: an online learning problem in which the goal is to sample from the Gibbs distribution induced by an unknown reward function. We define sampling regret as the temperature-normalized cumulative KL divergence between the learner&#39;s distribution and the Gibbs target, corresponding to the suboptimality gap in entropy-regularized reward maximization. Our framework generalizes recent sampling-based and KL-regularized formulations in bandits and reinforcement learning. Our main contribution is a general regret framework ...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21908

### 2610.22252: Explore Once, Evaluate Many: Multiple Policy Evaluation for Stochastic Linear Bandits
- **Authors**: Spyros Dragazis; Yilei Chen; Aldo Pacchiano
- **Institution/Company**: Boston University, Broad Institute
- **Subjects**: Machine Learning (cs.LG); Machine Learning (stat.ML)
- **Abstract**: We study how to evaluate $K$ target policies simultaneously in stochastic contextual bandits with linear reward structure. Given a known $d$-dimensional feature map and reward-free access to policy queries, we propose PRISMA (Policy evaluation through Regularized Information Sharing and Mixture Allocation), an algorithm that estimates every target policy&#39;s value to accuracy $\varepsilon$ with probability at least $1-\delta$. The algorithm uses $\widetilde{\mathcal{O}}\!\left( \frac{(L^2S^2+\beta^2)(1\vee\rho^\star)}{\varepsilon^2} \cdot \log(K) \right)$ context draws and reward observations, where $\rho^\star\le d$ is an instance-dependent measure of the difficulty of designing a shared sampling distribution. Here, $L$, $S$, and $\beta$ bound the feature norm, reward parameter norm, an...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22252

### 2610.21764: Q($γ_H$): Entropy-Guided Horizon Mixing in Multi-Discount Q-Learning
- **Authors**: Arwa Albelaihi; Abdulrahman Altahhan
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG)
- **Abstract**: A fixed discount factor in Q-learning imposes a single planning horizon throughout training, despite the differing demands of early exploration and long-term credit assignment. We propose Q($\gamma_H$), a multi-horizon Q-learning framework that maintains multiple discount-specific heads and adaptively combines them at control time using an entropy-derived confidence signal. The resulting state-dependent mixing weights shift control from shorter- to longer-horizon heads as policy confidence increases, enabling adaptive horizon mixing without modifying individual Bellman updates. Across classical control and deep reinforcement-learning benchmarks, Q($\gamma_H$) shows its strongest improvements on delayed-credit tasks relative to strong fixed-discount baselines. By decoupling horizon adaptati...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21764

### 2610.22277: Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines
- **Authors**: Florian Lercher; Karan Mahesh; Yujun Huang; Meshal Alharbi; Runyu Zhang; Hanna Krasowski; Michael R. Benjamin; Matthias Althoff; Gioele Zardini
- **Institution/Company**: National Science Foundation Graduate Research, Massachusetts Institute of Technology, Information and Technology, German Research Foundation, Technical University
- **Subjects**: Multiagent Systems (cs.MA); Computer Science and Game Theory (cs.GT); Robotics (cs.RO); Systems and Control (eess.SY)
- **Abstract**: When robots are deployed in the real-world, they must interact with other agents and accomplish their own goals while adhering to legal constraints. These potentially conflicting objectives are often only partially prioritized, making scalarized objectives or fully specified hierarchies unsuitable. We present a framework for multi-agent motion planning under legal requirements based on games with partially ordered preferences (posetal games). Scenario-independent legal guidelines order abstract legal concerns, from which we automatically derive agent preferences and a legal game for any concrete scenario. Agents may refine their legal preferences with private objectives, and regulators may refine the guideline as laws evolve. We prove that such customizations can only remove equilibria and...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22277

## Benchmarks / Evaluation / Interpretability (3)

### 2610.20748: Interpreting Language Model Parameters
- **Authors**: Lucius Bushnaq; Dan Braun; Oliver Clive-Griffin; Bart Bussmann; Nathan Hu; Michael Ivanitskiy; Linda Linsefors; Lee Sharkey
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
- **Abstract**: Mechanistic interpretability aims to uncover how neural networks use their parameters to implement their impressive neural algorithms. Although previous work has uncovered substantial structure in the intermediate representations that networks use, little progress has been made to understand how the parameters and nonlinearities of networks perform computations on those representations. In this work, we present a method that brings us closer to this understanding by decomposing a language model&#39;s parameters into subcomponents that each implement only a small part of the model&#39;s learned algorithm, while simultaneously requiring only a small fraction of those subcomponents to account for the network&#39;s behavior on any input. The method, adVersarial Parameter Decomposition (VPD), o...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.20748

### 2610.22169: Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics
- **Authors**: Jian Gu; Hongyu Zhang; Chunyang Chen; Aldeida Aleti
- **Institution/Company**: Chongqing University, Technical University, Monash University
- **Subjects**: Computation and Language (cs.CL); Machine Learning (cs.LG)
- **Abstract**: The vocabulary of a language model is its native semantics: the embedding and the unembedding fix the meaning of a state at the two ends of the residual stream. Between them, existing methods either reuse a fixed lens or treat the states as a point cloud, and neither reads a state the way the model does. We argue that every hidden state has a native reference frame, induced by the layers that read it next and adaptive to the context. Lexical reference frames approximate it by reading a state through the model&#39;s own remaining layers with a stated number of rounds of attention between positions and a typical attention output for the rest, without fitting to the model&#39;s output. No lens, with fixed directions per layer, can exceed the square root of the native frame&#39;s coherence, 0....
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.22169

### 2610.21240: Representation Redistribution in Sparse Autoencoders
- **Authors**: Ziye Mei; Haotian Ma
- **Institution/Company**: not stated (arXiv HTML omits affiliations or extraction limited)
- **Subjects**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Abstract**: Sparse autoencoders (SAEs) decompose language model activations into sparse features, but prompt transformations designed to preserve the underlying request can redistribute activity across them. A feature change observed on one transformed prompt need not recur, and even a recurring change need not affect a downstream computation. We introduce the redistribution sensitivity score (RSS), which identifies large feature responses that recur in a consistent direction, and evaluate the resulting supports on variants excluded from selection. Across 27 pretrained SAEs spanning eight language models, the tested prompt transformations produce a reproducible redistribution profile on these excluded variants. We then separate recurring representation change from signed readout contribution and decis...
- **Key innovations**: (see paper for details)
- **arXiv**: https://arxiv.org/abs/2610.21240
