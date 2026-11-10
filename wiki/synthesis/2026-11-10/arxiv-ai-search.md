# arXiv AI Search Report (2026-11-10)

## Scope and method
- **Date:** 2026-11-10
- **Topics covered:** AI, LLMs, recommendation systems, advertising/CTR prediction, sequential modeling, and AI for games/reinforcement learning.
- **Sources:** Recent arXiv listings and search results from `cs.AI`, `cs.CL`, `cs.IR`, `cs.LG`, plus targeted arXiv searches for LLMs, recommendation/CTR/advertising, sequential recommendation, and game-playing agents.
- **Notes:** "Institution/Company" is included when explicitly stated on the arXiv page/result; otherwise marked as *Not listed on arXiv*. Abstracts are summarized or excerpted from arXiv metadata.

---

## 1) Represented but Not Used: Value-Policy Dissociation in LLM Agents
- **arXiv:** [2611.10457](https://arxiv.org/abs/2611.10457) (cs.AI, submitted 2026-11-07)
- **Authors:** Yuzhang Luo, Mohamed Aghzal, Liangming Pan, Ziyu Yao
- **Institution/Company:** *Not listed on arXiv*
- **Abstract:** Studies whether LLM agents represent action values (future consequences of candidate actions) even when their policy does not choose the best-valued action. Across Qwen2.5-7B-Instruct, Qwen2.5-32B-Instruct, and GPT-OSS-20B in a partially observed Grid environment and WebShop, the authors find relative action values are linearly decodable from intermediate hidden states, including states where the policy prefers worse actions—a phenomenon termed *value-policy dissociation*. They compare interventions along value readout directions with Natural Value Transport (NVT), learned from hidden-state changes induced by value differences.
- **Key innovations:**
  - Identifies and characterizes **value-policy dissociation** in LLM agents (value is represented but not reliably used by policy).
  - Introduces **Natural Value Transport (NVT)**, a transformation learned from natural hidden-state shifts associated with action-value differences, to influence action preferences.
  - Demonstrates a **closed-loop controller** using value readout as sensor and NVT as actuator, improving task outcomes in some settings.

## 2) Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference
- **arXiv:** [2611.10193](https://arxiv.org/abs/2611.10193) (cs.AI, submitted 2026-11-06)
- **Authors:** Saul Urso, Emanuele Carlini, Patrizio Dazzi, Matteo Mordacchini
- **Institution/Company:** *Not listed on arXiv*
- **Abstract:** Addresses cost-quality tradeoffs for LLM serving by proposing PISA (prompt-adaptive, cost-aware single-model router) and PISA-E (ensemble routing extension). PISA estimates per-model capabilities using soft cluster memberships and model-specific predictors. PISA-E jointly selects ensemble composition and cardinality under an adjustable cost-quality preference without retraining, using a tractable ensemble-success surrogate and efficient candidate selection.
- **Key innovations:**
  - **Prompt-adaptive capability estimation** combining soft clustering and model-specific predictors for routing decisions.
  - **PISA-E ensemble routing** that adapts both which models to include and how many, with inference-time cost-quality control (no retraining).
  - **Tractable ensemble-success surrogate** enabling practical ensemble selection; strong results on four routing benchmarks under in-distribution and out-of-distribution settings.

## 3) Test-Time Compute Scales Better with Parallel Agent Teams
- **arXiv:** [2611.09798](https://arxiv.org/abs/2611.09798) (cs.AI, submitted 2026-11-06)
- **Authors:** Junlin Wang, Haozhe Chen, Ang Li, Rahul Chalamala, Zhuang Liu
- **Institution/Company:** *Not listed on arXiv*
- **Abstract:** Studies how to allocate test-time compute for agents when a verifier can score attempts. Compares best-of-N independent sampling and single large collaborating teams, proposing **parallel agent teams**: sample many small teams in parallel and keep the best team's result. Evaluated on 12 long-horizon tasks (GPU kernels, formal proofs, exploit development, etc.) with a 27B model and budget of 100 agents.
- **Key innovations:**
  - **Parallel agent teams** strategy balancing high mean performance (collaboration) with variance gains (parallel sampling).
  - Empirical finding: teams of ten in parallel beat parallel independent agents on 10/12 tasks and beat one team of 100 on all tested large-team tasks; competitive with a frontier model at equal dollar cost on half the tasks.
  - Provides a **statistical model** explaining why independent sampling saturates (low mean) and one large team saturates (no variance gain).

## 4) CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **arXiv:** [2602.11410](https://arxiv.org/abs/2602.11410) (cs.LG, v1 2026-02-11, v2 2026-08-10; accepted at AdKDD 2026)
- **Authors:** David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang
- **Institution/Company:** LinkedIn (stated in abstract: "deployed at LinkedIn" / "LinkedIn's advertising platform")
- **Abstract:** Presents CADET, an end-to-end decoder-only transformer for ads CTR prediction addressing challenges unique to advertising: post-scoring contextual signals, offline-online consistency, and industrial scale. Deployed in LinkedIn's homefeed sponsored updates; online A/B testing shows an 11.04% CTR lift over the production LiRank baseline (hybrid DCNv2 + sequential encoders).
- **Key innovations:**
  - **Context-conditioned decoding** with multi-tower prediction heads to model post-scoring signals (e.g., ad position), resolving ranking/CTR coupling issues.
  - **Self-gated attention** to stabilize training by regulating information flow at representation and interaction levels.
  - **Timestamp-based RoPE variant** capturing temporal relationships from seconds to months.
  - **Session masking** to reduce train-serve skew from unavailable in-session events.
  - **Production engineering** (tensor packing, sequence chunking, custom Flash Attention kernels) enabling large-scale training/serving.

## 5) SAGE-PAIR: Source-Pretrained Routed Residual Adaptation for Sparse-Feedback Recommendation
- **arXiv:** [2611.09728](https://arxiv.org/abs/2611.09728) (cs.IR, recent submission on 2026-11-09 list)
- **Authors:** Weiqing Zeng, Zida Yang, Guquan You, Jiexin Zheng, Cong Wang
- **Institution/Company:** *Not listed on arXiv*
- **Abstract (from arXiv listing):** Proposes SAGE-PAIR for recommendation under sparse feedback, using source-pretrained representations and routed residual adaptation to improve transfer/adaptation in low-feedback regimes.
- **Key innovations:**
  - **Source-pretrained transfer** tailored to sparse-feedback recommendation settings.
  - **Routed residual adaptation** mechanism to selectively adapt pretrained knowledge for target recommendation tasks.

## 6) Rethinking Latent Reasoning for Generative Recommendation: Beyond Teacher-Generated CoT and Recurrent Hidden-State Feedback
- **arXiv:** [2611.09006](https://arxiv.org/abs/2611.09006) (cs.IR, recent submission on 2026-11-09 list)
- **Authors:** Yiwen Chen, Fuwei Zhang, Zehao Chen, Deqing Wang, Hehan Li, Peizhi Xu, Hanmeng Liu, Shuanglong Li, Xin Pei, Fuzhen Zhuang, Zhao Zhang
- **Institution/Company:** *Not listed on arXiv*
- **Abstract (from arXiv listing):** Re-examines latent reasoning approaches for generative recommendation, arguing limitations of teacher-generated chain-of-thought and recurrent hidden-state feedback, and proposing alternative latent reasoning design.
- **Key innovations:**
  - Critique and reformulation of **latent reasoning paradigms** for generative recommendation.
  - Moves beyond reliance on **teacher-generated CoT** and recurrent hidden-state feedback toward improved reasoning mechanisms for recommendation generation.

## 7) SteerGR: Steering Generative Recommendation via Sparse Autoencoders for Controllable Game Discovery
- **arXiv:** [2611.08790](https://arxiv.org/abs/2611.08790) (cs.IR/cs.AI/cs.CL, recent submission)
- **Authors:** Sunkyung Lee, Xiaokai Wei, Da Long, Hyunsik Jeon, Jiajun Wu, Rithwik Seth, Jongwuk Lee, Michelle Gong, Gungor Polatkan
- **Institution/Company:** *Not listed on arXiv*
- **Abstract (from arXiv listing):** Introduces SteerGR, a method to steer generative recommendation models using sparse autoencoders for controllable discovery, with application to game recommendation/discovery.
- **Key innovations:**
  - Uses **sparse autoencoders** to expose interpretable/controllable latent features for steering generative recommenders.
  - Enables **controllable recommendation/discovery** (e.g., for games) without retraining the full generative model.

## 8) Deliberate Latent Reasoning for Sequential Recommendation
- **arXiv:** [2611.06521](https://arxiv.org/abs/2611.06521) (cs.IR, submitted 2026-11-04)
- **Authors:** Haobo Zhang, Qiannan Zhu, Yutao Zhu, Zhicheng Dou
- **Institution/Company:** *Not listed on arXiv*
- **Abstract (from arXiv search):** Proposes DESRec, a deliberate latent reasoning framework for sequential recommendation that personalizes reasoning depth per user sequence. It selects informative reasoning steps during training, distills them into a final reasoning state for inference, and progressively extracts preference milestones from user histories to support personalized evolving-interest modeling.
- **Key innovations:**
  - **Personalized reasoning depth/step selection** instead of fixed-step latent reasoning for all users.
  - **Self-distillation** to compress the most informative reasoning state into the final representation used at inference.
  - **Progressive preference extraction** via variable-length milestones over user history to model evolving interests.

## 9) Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man
- **arXiv:** [2611.06704](https://arxiv.org/abs/2611.06704) (cs.LG, submitted 2026-11-04)
- **Authors:** Xinglu Wang, Edward Wang, Yong Zhang, Zhenan Fan
- **Institution/Company:** *Not listed on arXiv*
- **Abstract (from arXiv search):** Diagnoses failure modes of a Qwen3.5-9B-based vision-language agent in Pac-Man by separating perception checks from policy learning/decision studies. Finds that accurate static screenshot reading can coexist with interaction-time perception errors, and that training gains do not always translate to better action choices or robust game performance.
- **Key innovations:**
  - **Diagnostic decomposition** of agent failures into perception, memory/representation-in-use, and decision components in a game environment.
  - Demonstrates **perception-use gap** (static accuracy vs interaction errors) and need for post-training evaluation beyond a single score.
  - Provides empirical guidance for **evaluating and improving game-playing VLM/LLM agents**.

## 10) Discovering Update Rules for Opponent Shaping in General-Sum Games
- **arXiv:** [2611.08335](https://arxiv.org/abs/2611.08335) (cs.LG, v2 2026-11-06)
- **Authors:** Hong Jun Lee, Ziyan Wang, Jun Wang, Stefanos Leonardos, Yali Du
- **Institution/Company:** *Not listed on arXiv*
- **Abstract (from arXiv search):** Introduces Discovered Update Rule for Opponent Shaping (DUOS), a meta-learned update rule for general-sum games that shapes opponents without requiring access to opponent parameters, policies, rewards, or learning rules at deployment. The rule is meta-trained to maximize lifetime return and updates an inner network using only the agent's own experience.
- **Key innovations:**
  - **Meta-discovered opponent-shaping update rule (DUOS)** operating from own-experience signals only (deployment-time opponent observability not required).
  - Extends discovered-optimizer ideas to **multi-agent/general-sum opponent shaping**.
  - Shows emergent shaping behavior and strong tournament performance in evaluated settings.

## 11) Generative Search and Recommendation at Shopify
- **arXiv:** [2611.08804](https://arxiv.org/abs/2611.08804) (cs.IR, recent submission)
- **Authors:** Juhana Kangaspunta, Khalil Hajji, Darshan Fofadiya, Kyumin Park, Michael Garner, Anthony Maltsev, Ryan Synk, Jose Sepulveda, Joshua Crisologo, Shuying Sun, Akshay Soni
- **Institution/Company:** Shopify (implied by title; affiliation not explicitly listed on arXiv page snippet)
- **Abstract (from arXiv listing):** Describes generative approaches to search and recommendation in a large-scale commerce setting, focusing on practical deployment considerations and system design for unified generative retrieval/recommendation experiences.
- **Key innovations:**
  - **Generative unification** of search and recommendation workflows in production e-commerce context.
  - Industrial system design and deployment insights for **large-scale generative retrieval/recommendation**.

---

## Quick takeaways
- **LLM agents:** Active work on internal value representations vs action selection, and on better test-time compute allocation via parallelized team sampling.
- **Recommendation/ads/sequential modeling:** Strong momentum in generative/latent-reasoning recommenders, controllable steering, sparse-feedback adaptation, and production-grade transformer CTR systems (e.g., LinkedIn CADET).
- **Games/multi-agent:** Continued interest in diagnosing VLM/agent failures in games and in learning/meta-learning update rules for opponent shaping in general-sum settings.
