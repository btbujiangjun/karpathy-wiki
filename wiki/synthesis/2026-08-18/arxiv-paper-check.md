---
title: arXiv Paper Check — AI & CTR (August 18, 2026)
type: synthesis
created: 2026-08-18
updated: 2026-08-18
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, agents, moe, efficiency, world-models, evaluation, bias, daily-digest]
---

# arXiv Paper Check — AI & CTR (August 18, 2026)

**Batch window**: Mon Aug 17, 2026 announced (submissions Sun Aug 16; IDs ~2608.138xx–2608.145xx)
**Categories scanned**: cs.AI (185 new), cs.LG (138 new), cs.IR (13 new) = 336 entries
**Paper selection**: 15 curated from cs.AI/cs.IR/cs.LG, all IDs grep-verified absent (0 hits) from the entire wiki; zero overlap with same-day arxiv-daily (which covers a different batch) and arxiv-ai-search

---

## CTR / Recommendation / Ads / IR (6 papers)

### 1. PriCoRec: Privacy-Aware Cloud-Device Collaborative Framework for Ad Recommendation under Feature Constraints

- **arXiv**: [2608.14429](https://arxiv.org/abs/2608.14429)
- **Authors**: Dairui Liu, Zhongyi Lu, Jitao Lu, Aghiles Salah, Mete Sertkan, Roger Zhe Li, Changhong Jin, Barry Smyth, Xingsheng Guo, Ruihai Dong
- **Venue**: Accepted to RecSys'26
- **Key contributions**: Proposes a privacy-aware collaborative framework for ad recommendation that operates under feature constraints between cloud and device. Addresses the tension between personalized ad ranking and user privacy by enabling cloud-device collaboration without raw feature exchange. Relevant to production systems where GDPR/privacy regulations limit feature availability.
- **Relevance**: Privacy-preserving CTR — increasingly critical as regulation tightens.

### 2. MACS: A Hybrid Multi-Agent Framework for Reliable Conversational E-Commerce Recommendation

- **arXiv**: [2608.14068](https://arxiv.org/abs/2608.14068)
- **Authors**: Juli Huang, Hannah Clay, Sajjad Beygi, Thomas Sarda, Negin Golrezaei, Amin Saberi
- **Venue**: Stanford Trust & Safety Conference + Stanford Market AI Conference
- **Key contributions**: Introduces a multi-agent framework combining retrieval, reasoning, and safety agents for conversational e-commerce recommendation. Uses hybrid agent orchestration to balance recommendation quality with reliability/safety constraints. Demonstrates production-grade design with 8 tables of ablation evidence.
- **Relevance**: Conversational CTR/rec systems with safety guarantees — aligns with industry shift toward agent-based recommendation.

### 3. EchoRec: Multi-Item Prediction-Empowered Generative Recommendation via Cycle-Consistent Preference Alignment

- **arXiv**: [2608.14011](https://arxiv.org/abs/2608.14011)
- **Authors**: Haokai Ma, Aoqi Hu, Yueao Xing, Ruobing Xie, Yonghui Yang, Teng Tu, Lei Meng, Tat-Seng Chua
- **Key contributions**: Proposes cycle-consistent preference alignment for generative recommendation models. Multi-item prediction empowers the generator to produce diverse, high-quality recommendations. Cycle consistency ensures preference alignment between user history and generated recommendations without requiring negative sampling.
- **Relevance**: Generative CTR paradigm (cf. GE4Rec, GPSD, GenCI in wiki) — new alignment mechanism.

### 4. AdsWorldEngine: A Self-Evolving Conversational Advertising Agent through Orchestrator and Tool Coevolution

- **arXiv**: [2608.13833](https://arxiv.org/abs/2608.13833)
- **Authors**: Simiao Zuo, Chenhui Xu, Yimeng Jia, Qiang Lou, Jian Jiao, Denis Charles
- **Key contributions**: Self-evolving agent architecture where the orchestrator and toolset co-evolve. Designed for conversational advertising where the agent must adapt its strategy and capabilities over time. Novel coevolution mechanism ensures the system improves both planning (orchestrator) and execution (tools) jointly.
- **Relevance**: Agentic advertising — extends the "build for agents" paradigm into ad serving.

### 5. Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders

- **arXiv**: [2608.14021](https://arxiv.org/abs/2608.14021)
- **Authors**: Keito Kozaki, Keigo Sakurai, Ren Togo, Takahiro Ogawa, Miki Haseyama
- **Venue**: Accepted at RecSys'26
- **Key contributions**: Provides a theoretical structural explanation for why causal self-attention recommenders tend to over-rely on the last item (recency bias). Identifies "residual dominance" — the residual connection's output dominates the attention output, causing the last item to disproportionately influence predictions. Offers a principled fix.
- **Relevance**: Architectural analysis directly relevant to Transformer-based CTR models (cf. Hiformer, InterFormer, HyFormer in wiki).

### 6. Content Depth Matters in Short-Video Recommendation: Rethinking the Attention Economy

- **arXiv**: [2608.13990](https://arxiv.org/abs/2608.13990)
- **Authors**: Liwei Deng, Jing Jiang, Zhiwei Li, Yang Wang, Guodong Long
- **Key contributions**: Argues that short-video recommendation systems over-optimize for engagement metrics (clicks, watch time) at the expense of content quality/depth. Proposes depth-aware ranking signals that improve long-term user satisfaction while maintaining short-term engagement. Challenges the "attention economy" framing of rec system objectives.
- **Relevance**: Rec system objective design — connects to Karpathy's "RL is terrible" concerns about reward hacking.

---

## AI Agents & Multi-Agent Systems (5 papers)

### 7. AgentRewind: Recoverable Execution for Long-Horizon LLM Agents

- **arXiv**: [2608.14380](https://arxiv.org/abs/2608.14380)
- **Authors**: Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang
- **Key contributions**: Introduces recoverable execution for long-horizon LLM agents — the ability to checkpoint, rollback, and retry agent execution branches. Addresses the brittleness of current agent systems where a single failure in a long chain requires full restart. Enables more efficient exploration of solution spaces.
- **Relevance**: Agent reliability engineering — directly addresses the "verification gap" Karpathy discusses.

### 8. Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents

- **arXiv**: [2608.14339](https://arxiv.org/abs/2608.14339)
- **Authors**: Zhizhao Guan, Chen Huang, Ziming Liu, Hongru Liang, Wenqiang Lei, See-Kiong Ng, Tat-Seng Chua, Anthony G Cohn
- **Key contributions**: Studies proactive exploration in LLM agents — the ability to proactively seek information rather than passively waiting for it. Proposes training and refinement methods to install proactive exploration capabilities. Addresses the "reactive agent" limitation where agents fail because they don't ask clarifying questions.
- **Relevance**: Agent capability engineering — proactive vs reactive behavior is a key differentiator for production agents.

### 9. Demystifying Agent Skills: Why They Work-Until They Don't

- **arXiv**: [2608.14036](https://arxiv.org/abs/2608.14036)
- **Authors**: Zhiyuan Jiang, Fangrui Huang, Hanwen Xing, Xander Wu, Yipeng Gao, Rui Cao, Mengdi Wang, Shilong Liu, Yijiang Li
- **Key contributions**: Empirical analysis of why agent skills (tool-use patterns, workflows) succeed initially but degrade over time. Identifies failure modes including context drift, skill-situation mismatch, and cascading errors. Provides diagnostic framework for understanding skill reliability boundaries.
- **Relevance**: Agent skill reliability — critical for understanding when "bacterial code" patterns break.

### 10. BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs

- **arXiv**: [2608.14161](https://arxiv.org/abs/2608.14161)
- **Authors**: Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos, Karin Sevegnani, Emine Yilmaz
- **Key contributions**: Traces how specific reasoning behaviors in LLMs lead to biased outputs. Provides a diagnostic tool that links chain-of-thought reasoning steps to downstream bias, enabling targeted mitigation. Moves beyond outcome-level bias measurement to process-level understanding.
- **Relevance**: LLM evaluation and safety — connects to Karpathy's "model smell" and eval concerns.

### 11. Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning

- **arXiv**: [2608.14290](https://arxiv.org/abs/2608.14290)
- **Authors**: Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, et al. (large team)
- **Key contributions**: Proposes decoupling knowledge storage from reasoning capabilities in foundation models. The "Mobius" architecture separates parametric knowledge from inference mechanisms, enabling independent scaling and updating of each component. Addresses the entanglement problem where knowledge updates disrupt reasoning patterns.
- **Relevance**: Foundation model architecture — knowledge-reasoning separation has implications for CTR models that combine user knowledge with prediction logic.

---

## Machine Learning & Efficiency (4 papers)

### 12. FreeBalance: Pre-Routing Online MoE Load Balancing via Residual Workload Prediction

- **arXiv**: [2608.14205](https://arxiv.org/abs/2608.14205)
- **Authors**: Pengfei Chen, Yize Wu, Shouxu Kuang, Ke Gao, Ling Li
- **Key contributions**: Solves the MoE load balancing problem with a pre-routing approach that predicts residual workload before expert assignment. Avoids the load imbalance that degrades training efficiency in large MoE models. Particularly important for sparse CTR models using MoE (cf. DeaMoE in same batch, MTmixAtt in wiki).
- **Relevance**: MoE efficiency — directly applicable to scaling CTR models with MoE architectures.

### 13. Traj-LeWM: Path-Aware World-Model Planning via Latent Trajectory Cost

- **arXiv**: [2608.14125](https://arxiv.org/abs/2608.14125)
- **Authors**: Xiaodi Huang, Ziyi Ding, Jingtian Wan, Yuchen Liu, Yuan Zhang, Xiao-Ping Zhang, Jiayu Chen, Zhang Zhang, Tao Huang
- **Key contributions**: Introduces latent trajectory cost estimation for world-model-based planning. Rather than evaluating entire trajectories, estimates cost in latent space to enable efficient long-horizon planning. Achieves planning quality comparable to full-trajectory evaluation at a fraction of the computational cost.
- **Relevance**: World models + planning efficiency — relevant to agent-based recommendation systems and game AI.

### 14. Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View

- **arXiv**: [2608.14430](https://arxiv.org/abs/2608.14430)
- **Authors**: Yixian Xu, Yuanrui Zhang, Shengjie Luo, Liwei Wang, Di He
- **Key contributions**: Provides a unified theoretical framework for applying RL to diffusion models via path-space formulation. Bridges the gap between RL policy optimization and diffusion model sampling. Establishes when and how RL fine-tuning of diffusion models is beneficial vs harmful.
- **Relevance**: RL + diffusion — foundational for understanding RL post-training of generative models (cf. NeurIPS "Why Diffusion Don't Memorize").

### 15. Forecast Collapse in Time-Series Foundation Models

- **arXiv**: [2608.14106](https://arxiv.org/abs/2608.14106)
- **Authors**: Shu Wan, Miles Ma, Hank Zhu, Guangqi Liu, Stephen Wang, Qingsong Wen, Huan Liu
- **Key contributions**: Documents and analyzes "forecast collapse" — a failure mode where time-series foundation models converge to degenerate predictions (e.g., always predicting the mean). Identifies causes including training objective mismatch and distribution shift. Provides diagnostic tools and mitigation strategies.
- **Relevance**: Foundation model failure modes — cautionary for applying FMs to CTR/time-series prediction tasks.

---

## Cross-Cutting Observations

1. **Privacy-preserving CTR is maturing**: PriCoRec (cloud-device) and the broader trend of on-device inference suggest production CTR systems will increasingly need to operate under feature constraints — a structural shift from the centralized feature store paradigm.

2. **Generative recommendation alignment**: EchoRec's cycle-consistent alignment offers a new mechanism beyond the preference optimization approaches (DPO, SDPO) used in GPSD/GenCI. The generative CTR paradigm continues to diversify its training methodologies.

3. **Agent reliability as a first-class concern**: AgentRewind (recoverable execution), Clearing the Fog (proactive exploration), and Demystifying Agent Skills (failure diagnosis) collectively address the reliability gap that Karpathy highlights as a core challenge in agentic engineering.

4. **MoE efficiency for CTR**: FreeBalance addresses a practical bottleneck for scaling CTR models with MoE — load balancing at serving time. Combined with DeaMoE (same batch, fast small-batch decoding), the MoE CTR stack is becoming more deployable.

5. **Residual dominance as architectural diagnosis**: The RecSys'26 paper on last-item reliance provides a structural explanation for a known failure mode in Transformer-based recommenders — directly applicable to the wiki's extensive catalog of Transformer CTR architectures.

---

*Report generated 2026-08-18. All 15 arXiv IDs verified absent from wiki before inclusion.*
