---
title: "arXiv Daily — AI, LLMs, Recommendation, CTR, Games & Sequence Modeling (July 14, 2026)"
type: synthesis
created: 2026-07-14
updated: 2026-07-14
tags: [arxiv-daily, llm, rl, ctr, recommendation, advertising, sequence-modeling, games, ssm]
---

# arXiv Daily Digest — July 14, 2026

> Papers across AI, LLMs, recommendation systems, advertising, CTR prediction, sequential modeling, state space models, and games. Collected from recent arXiv submissions (July 2026).

---

## LLM Training & Reinforcement Learning

### 1. LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL
- **Link**: [2607.04412](https://arxiv.org/abs/2607.04412)
- **Authors**: Yujin Kim, Namgyu Ho, Sangmin Hwang, Joonkee Kim, Yongjin Yang, Sangmin Bae, Seungone Kim, Jaehun Jung, Se-Young Yun, Hwanjun Song
- **Affiliation**: KAIST
- **Key Innovation**: Extends the LLM's role from judge to tutor in RL training for non-verifiable instruction following. The tutor detects non-challenging prompts via pairwise comparison and appends atomic constraints, creating a self-calibrating curriculum that tracks policy capability. Consistently outperforms policy-unaware and prior policy-adaptive methods on FollowBench, AdvancedIF, and InfoBench.
- **Tags**: RL, LLM training, instruction following, reward models

### 2. Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning
- **Link**: [2607.05458](https://arxiv.org/abs/2607.05458)
- **Key Innovation**: Formalizes the LLM agent execution harness as a learnable control layer (Harness MDP). Uses advantage-weighted regression from offline rollouts to train a lightweight controller that selects structural execution actions. Shows consistent improvement in verification-before-submission behavior and selective final-quality gains across 6 controlled domains and 2 benchmarks.
- **Tags**: RL, LLM agents, harness, offline RL

### 3. MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
- **Link**: [2607.06974](https://arxiv.org/abs/2607.06974)
- **Affiliation**: (submitted Jul 8, 2026)
- **Key Innovation**: Dynamically expands step-wise memory with modular instruction units (asymmetric sub-goal embeddings + sub-instructions), each paired with a learnable selection head. Coarse-to-fine retrieval mechanism collects supervision from confident samples and applies learned selection heads for uncertain ones. Matches or outperforms prior memory-based methods with superior accuracy-efficiency tradeoffs.
- **Tags**: LLM reasoning, test-time computation, memory

### 4. Sparrow: Sparse Rollout for Stable and Efficient Long-context RL of Large Language Models
- **Link**: [2606.08446](https://arxiv.org/abs/2606.08446)
- **Key Innovation**: Studies sparse-to-dense actor-policy mismatch in RLVR training. Identifies that sparse rollout collapse is driven by the lower tail of per-token mismatch, not uniform degradation. Proposes dynamic sparsity scheduling that maintains tail statistics at a consistent threshold. Achieves 2.0–2.4× rollout speedup for Qwen3-1.7B/4B/8B, generalizes to 14B and coding domains. Also introduces DistillSparse for further gains via LoRA-based distillation on sparse rollout.
- **Tags**: RL, sparse attention, long-context, efficiency, Qwen3

### 5. LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents
- **Link**: [2606.18388](https://arxiv.org/abs/2606.18388)
- **Key Innovation**: LLM agents search over training trajectories via tree search, diagnosing pathologies at each checkpoint and proposing coordinated multi-parameter transitions. Discovers that capacity parameters accumulate monotonically while regularization parameters oscillate non-monotonically across stages. Improves over base model by 9–140% relative and over grid search by 6–15% across 4 GRPO tasks.
- **Tags**: RL, hyperparameter optimization, LLM agents, GRPO

### 6. Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents
- **Link**: [2607.01120](https://arxiv.org/abs/2607.01120)
- **Key Innovation**: Argues that self-evolving agent deployment is held back by agentic RL systems, not algorithms. Identifies 3 essential gaps: (1) no standardized trajectory data protocol for RL signals, (2) no enterprise-grade data proxy converting real workloads to learning substrates, (3) no unified evolution control plane. Instantiates AReaL2.0 as a reference architecture.
- **Tags**: RL systems, self-evolving agents, infrastructure

---

## LLM-as-a-Verifier / Verification Scaling

### 7. LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Link**: [2607.05391](https://arxiv.org/abs/2607.05391)
- **Key Innovation**: Identifies verification as a new scaling axis. Computes continuous scores via expectation over scoring token logits, enabling verification scaling across score granularity, repeated evaluation, and criteria decomposition. State-of-the-art on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), and MedAgentBench (73.3%). Also serves as dense reward signal for RL.
- **Tags**: verification, test-time scaling, reward model, agentic tasks

---

## Audio & Multimodal LLMs

### 8. Nemotron-Labs-Audex-30B-A3B (Audex): Unified Audio Intelligence Without Regressing on Text Intelligence
- **Link**: [2607.05196](https://arxiv.org/abs/2607.05196)
- **Authors**: Wei Ping et al. (NVIDIA / Nemotron Labs)
- **Key Innovation**: Unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B MoE. Single Transformer decoder handles audio inputs, text tokens, and quantized audio output tokens uniformly. Trained on 157.4B audio + 320.5B text tokens with multi-stage supervised training + Cascade RL. SOTA in audio understanding, ASR, translation, TTS, audio generation, speech-to-speech while preserving text-only reasoning and alignment capabilities.
- **Tags**: audio LLM, MoE, multimodal, speech, open-source

### 9. POPS: Recovering Unlearned Multi-Modality Knowledge in MLLMs with Prompt-Optimized Parameter Shaking
- **Link**: [2607.06649](https://arxiv.org/abs/2607.06649)
- **Key Innovation**: Adversarial attack on multi-modality machine unlearning (MMU). Uses prompt-suffix optimization to elicit private examples from victim MLLMs, then fine-tunes to reveal supposedly erased sensitive information. Achieves near-complete recovery, exposing fundamental vulnerabilities in MMU-based privacy protection.
- **Tags**: MLLM, machine unlearning, adversarial, privacy

---

## Recommendation Systems & Advertising

### 10. OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation
- **Link**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Affiliation**: Tencent (Weixin Channels)
- **Key Innovation**: Architectural-level fusion of generation and ranking in generative advertising recommendation. Value-aware multi-task decoupling via task tokens and causal masks. Coarse-to-fine target awareness with Fake Item Tokens. Key/Value pass-through and Distribution Consistency Constraint Loss for end-to-end optimization. Deployed at Tencent Weixin Channels — GMV-Normal +1.34% online.
- **Tags**: generative recommendation, advertising, ranking, Tencent

### 11. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Link**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Affiliation**: LinkedIn
- **Key Innovation**: End-to-end decoder-only transformer for ads CTR. Context-conditioned decoding with multi-tower prediction heads (solves CTR-position chicken-and-egg). Self-gated attention for training stability. Timestamp-based RoPE for multi-scale temporal relationships. Session masking for train-serve skew. Tensor packing, sequence chunking, custom Flash Attention kernels. 11.04% CTR lift over LiRank baseline at LinkedIn.
- **Tags**: CTR prediction, transformer, advertising, LinkedIn, RoPE

### 12. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Link**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Affiliation**: Xiaohongshu (小红书)
- **Key Innovation**: Uses MLLMs to generate proxy embeddings from rich content signals for cold-start items, explicitly aligned with the existing ID embedding space. End-to-end optimized under CTR objectives. Deployed in both Content Feed and Display Ads, serving hundreds of millions daily users.
- **Tags**: CTR, cold-start, MLLM, recommendation, Xiaohongshu

### 13. UniVA: Unified Value Alignment for Generative Recommendation in Industrial Advertising
- **Link**: [2605.05803](https://arxiv.org/abs/2605.05803)
- **Affiliation**: Tencent (WeChat Channels)
- **Key Innovation**: Commercial SID tokenizer injecting value attributes into item representations. Generation-as-Ranking SID Decoder with eCPM-aware RL. Value-guided personalized beam search with personalized trie tree constraint. 37.04% Hit Rate@100 improvement, 1.5% GMV lift online.
- **Tags**: generative recommendation, advertising, value alignment, Tencent

### 14. GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Link**: [2604.14878](https://arxiv.org/abs/2604.14878)
- **Affiliation**: JD.com (京东)
- **Key Innovation**: Page-wise NTP task (supervises over entire interaction page). Asymmetric linear Token Merger compresses multi-token Semantic IDs (2× input length reduction). GRPO-SR combining Group Relative Policy Optimization with NLL regularization and Hybrid Rewards. 9.5% click and 8.7% transaction improvement in month-long online A/B tests.
- **Tags**: generative retrieval, recommendation, GRPO, JD, e-commerce

### 15. GEM-Rec: One Model, Two Markets — Bid-Aware Generative Recommendation
- **Link**: [2603.22231](https://arxiv.org/abs/2603.22231)
- **Key Innovation**: Integrates monetization objectives into generative recommendation via control tokens (decouples ad vs. item decisions) and Bid-Aware Decoding (injects real-time pricing into inference). Proves allocation monotonicity — higher bids weakly increase ad likelihood without retraining.
- **Tags**: generative recommendation, advertising, bid optimization, auctions

### 16. DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction in Trigger-Induced Recommendation
- **Link**: [2602.13971](https://arxiv.org/abs/2602.13971)
- **Affiliation**: Industrial e-commerce
- **Key Innovation**: Addresses "intent myopia" in Trigger-Induced Recommendation. Extracts personalized intent representations from user click–trigger correlations. Hybrid enhancer combining ID and semantic information with adaptive selection. Validated on public and industrial datasets.
- **Tags**: CTR, intent-aware, trigger-induced recommendation, e-commerce

### 17. LLM Retrieval for Stable and Predictable Ad Recommendations
- **Link**: [2605.21969](https://arxiv.org/abs/2605.21969)
- **Key Innovation**: New evaluation framework for stability/predictability of ads recommender systems. Fine-tuned LLMs extract hierarchical semantic attributes from ad creatives, used for graph-based expansion ensuring consistent delivery for small creative variants.
- **Tags**: advertising, retrieval, stability, LLM

---

## Games & RL Agents

### 18. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Link**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Key Innovation**: Studies RL-based VLM training for long-horizon (100+ turn) game playing in Super Mario Land. Proposes adapted PPO with lightweight turn-level critic and positive-advantage filtering. Outperforms GRPO and Reinforce++. Pretrained VLMs provide strong action priors (more sample-efficient than classical deep RL). 3× average game progress over frontier models. Generalizes across game levels and maintains general-domain capabilities.
- **Tags**: VLM, RL, games, Super Mario, PPO, long-horizon

### 19. MemoPilot: From Player to Master — Enhancing Test-Time Learning of LLM Agents via RL over Memory
- **Link**: [2606.08656](https://arxiv.org/abs/2606.08656)
- **Key Innovation**: Treats memory updating as a trainable multi-turn decision problem optimized via multi-turn GRPO. Turn-wise reward signal and context-independent turn-level advantage estimation across rollouts. Frozen LLM player + trained memory copilot. Ranks first in Elo on both Limit Texas Hold'em (1762) and multi-round RPS (1590), outperforming DeepSeek-V3.2 and all baselines.
- **Tags**: memory, RL, games, test-time learning, GRPO, Texas Hold'em

### 20. Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Link**: [2604.17696](https://arxiv.org/abs/2604.17696)
- **Key Innovation**: Addresses domain specificity and contextual stasis in game-based reasoning. Selectively reinforces trajectories with abstract, domain-agnostic reasoning via Reasoning Transferability Coefficient. Reasoning Evolution Reward incentivizes adaptive reasoning. Gains on competition-level mathematics, general reasoning, and code generation.
- **Tags**: games, reasoning, self-play, transfer learning

### 21. MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Link**: [2604.05943](https://arxiv.org/abs/2604.05943)
- **Key Innovation**: Single GPT-based model trained via offline RL on expert trajectories across SMACv2 (400M), GRF (100M), and POGEMA (1B). Single transformer-based observation encoder with no task-specific tuning. Competitive with specialized baselines across all environments. Demonstrates viability of a generalist MARL foundation model.
- **Tags**: MARL, foundation model, transformer, StarCraft, football, multi-agent

### 22. AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents
- **Link**: [2606.24893](https://arxiv.org/abs/2606.24893)
- **Key Innovation**: Procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks. Multifaceted evaluation (world knowledge acquisition, episodic memory, exploration, action diversity, cost). Tests diverse agent paradigms — Long Context > RAG > SFT > Fixed Memory. Performance scales with model capability but top agents still far below human. Identifies short-term memory as effective component.
- **Tags**: continual learning, test-time learning, games, evaluation, text games

### 23. Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Link**: [2603.17683](https://arxiv.org/abs/2603.17683)
- **Key Innovation**: Two-player architecture (perception vs. action) + curriculum state machine + database-as-control-plane for ARC-AGI-3 game-playing. Achieves 50–94× sample efficiency (32 interactions vs. 1600–3000 for baselines). Failure mode precisely diagnosed as self-consistent hallucination cascade in perception layer — demonstrating bottleneck has shifted from learning efficiency to perceptual grounding.
- **Tags**: curriculum learning, test-time learning, games, ARC-AGI, LLM agents

### 24. Robust Adversarial Reinforcement Learning in Stochastic Games via Sequence Modeling — CART
- **Link**: [2510.11877](https://arxiv.org/abs/2510.11877)
- **Key Innovation**: First framework enhancing robustness of Decision Transformer in adversarial stochastic games. Formulates protagonist-adversary interaction as stage games with NashQ values. Conditions Transformer policies on NashQ derived from stage games for less exploitable and conservative policies. Superior minimax value estimation and worst-case returns.
- **Tags**: adversarial RL, games, Decision Transformer, robustness

---

## State Space Models & Sequence Modeling

### 25. MuonSSM: Orthogonalizing State Space Models for Sequence Modeling
- **Link**: [2606.30461](https://arxiv.org/abs/2606.30461)
- **Key Innovation**: Stabilizes SSM training by conditioning the geometry of memory updates (not recurrent transition matrix). Augments SSMs with momentum-based pathway + lightweight Newton-Schulz transformation on low-rank input injections. Bounded, spectrally conditioned updates while preserving parallel scan complexity. Consistent gains across language, vision, and time-series benchmarks.
- **Tags**: SSM, sequence modeling, optimization, memory

### 26. WaveSSM: Multiscale State-Space Models for Non-stationary Signal Attention
- **Link**: [2602.22266](https://arxiv.org/abs/2602.22266)
- **Key Innovation**: Constructs SSMs over wavelet frames instead of polynomial bases with global temporal support. Wavelet frames yield localized temporal support, better matched to transient/non-stationary signals. Outperforms orthogonal-basis SSMs (S4) on PTB-XL (physiological signals) and Speech Commands. Uses SaFARi framework to derive transition matrices from any wavelet frame.
- **Tags**: SSM, wavelets, non-stationary, biosignals, audio

### 27. AUSSM: Adaptive Unitary State Space Models — Bridging Expressivity and Scalability
- **Link**: [2507.05238](https://arxiv.org/abs/2507.05238)
- **Key Innovation**: Uses input-dependent skew-symmetric recurrence for unitary evolution + high expressivity. Proves AUSSM can perform modulo counting and simulate solvable group automata. Separable convolution formulation + custom CUDA kernel for linear-time training despite full adaptivity. Hybrid Mamba+AUSSM maximizes expressivity among diagonal SSMs.
- **Tags**: SSM, expressivity, unitary, formal languages, CUDA

### 28. Bayesian Optimality of In-Context Learning with Selective State Spaces
- **Link**: [2602.17744](https://arxiv.org/abs/2602.17744)
- **Key Innovation**: Formalizes ICL as meta-learning over latent sequence tasks (LG-SSMs). Proves meta-trained selective SSM converges to Bayes-optimal predictor (asymptotically optimal). Establishes statistical separation from gradient descent — constructs tasks where Bayesian predictor strictly outperforms ERM (which Transformers implement). SSMs converge faster to Bayes risk with temporally correlated noise.
- **Tags**: SSM, ICL, Bayesian, theory, Mamba

### 29. Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
- **Link**: [2603.08859](https://arxiv.org/abs/2603.08859)
- **Key Innovation**: Proves fundamental limitations of pure Transformer and pure SSM models on function-composition tasks. Constructs hybrid models that provably solve selective copying and associative recall with small size and sublinear memory. Empirically, learned hybrids outperform non-hybrids with up to 6× fewer parameters and show stronger length generalization and OOD robustness.
- **Tags**: hybrid models, expressivity, efficiency, theory, Transformer, SSM

### 30. Sessa: Selective State Space Attention
- **Link**: [2604.18580](https://arxiv.org/abs/2604.18580)
- **Key Innovation**: Places attention inside a recurrent feedback path, creating multiple attention-based paths for past tokens to influence future states. Proves power-law memory tails O(ℓ^{-β}) with slower decay than Transformer or Mamba baselines. Only model class that realizes flexible selective retrieval without influence decay over distance. Strongest performance on long-context benchmarks while competitive on short-context.
- **Tags**: SSM, attention, hybrid, long-context, theory

### 31. Parallel Hybrid Architecture (PHA): Long-Context Modeling via GSS-Transformer Hybrid
- **Link**: [2606.16093](https://arxiv.org/abs/2606.16093)
- **Key Innovation**: Runs Gated State Spaces (GSS), Grouped Query Attention (GQA), and FFNs as independent parallel branches fused by learned mixing. GSS captures global context, attention does selective retrieval. Achieves 16.51 PPL on WikiText-103 (125M params), 24% higher throughput and 40% lower memory at long contexts vs. pure attention.
- **Tags**: hybrid, long-context, transformer, SSM, efficiency

---

## NeuroAI / Theory

### 32. Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks
- **Link**: [2607.08561](https://arxiv.org/abs/2607.08561)
- **Authors**: Daniel Yamins et al.
- **Key Innovation**: Proves that for any two minimal DNN solutions to a sufficiently hard task, weak alignment via affine mappings guarantees strong alignment of privileged axes, and alignment zippers up the network hierarchy. Formalizes contravariance. Suggests that with sufficiently hard tasks, convergent evolution in neural representations is probably inevitable.
- **Tags**: neuroAI, alignment, theory, representations

---

## Key Themes

1. **RL post-training is the dominant paradigm** — GRPO variants, policy-aware prompt/criteria adaptation, sparse attention for efficient rollout, and automated hyperparameter discovery via LLM agents are all converging.
2. **Generative recommendation is industrializing** — OneRanker, UniVA, GenRec, GEM-Rec show that generative (next-token) approaches are replacing cascaded architectures in production at Tencent, JD, LinkedIn, and Xiaohongshu.
3. **Hybrid SSM-Transformer models gain theoretical foundations** — Multiple papers (Expressivity-Efficiency Tradeoffs, Sessa, PHA) provide theory for why hybrids outperform pure models, with proven expressivity separations.
4. **Long-horizon game RL for VLMs is maturing** — Odysseus (Mario), MemoPilot (poker), MARL-GPT (StarCraft/football), AgentOdyssey (text games) show VLMs + RL for 100+ turn decision-making is a thriving subfield.
5. **Verification as a scaling axis** — LLM-as-a-Verifier shows that continuous-score verification with repeated evaluation and criteria decomposition provides a new way to scale test-time compute.
