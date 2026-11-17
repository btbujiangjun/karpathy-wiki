# Game RL & Game AI Bot — Daily Paper Digest (2026-11-17)

- **Date**: 2026-11-17
- **Window**: ~2026-10-28 → 2026-11-14 (freshest arXiv submissions/revisions and arXiv-exposed venue metadata available at query time; feed timestamp 2026-11-17T03:00Z)
- **Scope**: Game RL and strategic/multi-agent learning in classic and commercial game environments; LLM/VLM-powered game agents, NPC/agent frameworks and real-time autonomous gameplay; game foundation/world models and industry game-AI systems; procedural content generation and game scene/level generation; game-based agent evaluation and game-state benchmarks; and related techniques (self-play, imitation learning, MARL, world models/model-based RL).
- **Method note**: Discovery used 23 keyword queries plus a six-category (cs.MA/AI/LG/CL/CV/RO) recency sweep against the arXiv Export API via HTTPS on 2026-11-17 (~1,675 unique keyword candidates + ~1,531 category-sweep records, ~3,200 screened); `websearch` was unavailable in this run, so recent non-arXiv proceedings coverage is limited to venue/status metadata exposed on arXiv and PDF first pages. Every included ID was grep-verified as absent from all prior `wiki/synthesis/*/game-rl-daily.md` digests (1,731 known IDs). Paper metadata, abstracts, venues, affiliations, and reported results are taken from arXiv abstract pages and PDF first pages (pypdf) and are **author-reported** unless noted. Affiliations were PDF-verified where a first-page byline was available; entries without a stated affiliation are marked accordingly.
- **Active preference file**: `EXTEND.md` (repo root).

## Executive Summary

This window's strongest signal is **industry-grade game foundation models and real-time agents**: Tencent's GameWM (2611.19247) proposes a full interaction-centric world-model stack for shipped games with a 5B–33B model family and a real-time causal variant, while SceneAgent (2611.17821, Tencent + Fudan) makes multi-agent game-scene generation portable across engines via reusable skills. On the **autonomous gameplay** side, ViCoR (2611.18723) pairs a deliberative VLM with sub-second visual "conditioned reflexes," and NYU's Mario study (2611.16175) shows that scaling PCG training levels plus DRAIL human-imitation yields general, human-like play on 1,000 held-out levels. **Evaluation** is getting more mechanism-aware: TReC (2611.17781) scores Go moves by move-induced state-change consistency, and a Chef's Hat robot (2611.15524, Univ. Hamburg) reaches F1 0.906 on sim-to-real game-state detection. **Related techniques** feature self-play robustness (hidden start-delay randomisation, 2611.18491), semantic unlearning of MARL conventions (CARVE, 2611.17917), a first systematic ANO×DiffQAS ablation for quantum RL on Atari (2611.19182), and a chess VLA fine-tuning study (2611.12676). PCG is represented by an AIIDE 2026 paper on perceptual-distance level segmentation (2610.38987).

---

## 1) Game Foundation Models, World Models, and Industry Game AI

### GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models
- **Title (EN)**: GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models
- **Authors**: Bing He; Runze Wang; Fei Zha; Zhongyuan Wu; Ke Xu; Tao Zhuang; Yuxuan Xie; Zhongyuan Liu
- **Affiliation**: Lightspeed Studios, Tencent (PDF first page)
- **Venue/conference**: arXiv preprint (35-page technical report)
- **Date**: 2026-11-14 (v1)
- **Abstract**: GameWM is a design for next-generation video games built on a clear division of labor between a conventional game engine and a generative video model (VM). Prior world-model-for-games systems treat the VM as a renderer that merely restyles engine-authored motion, leaving most of its generative capacity unused. The GameWM-engine keeps what must be exact — rules, state, camera, and world layout — which also spares the VM from having to remember it; the GameWM-VM generates what is expensive to author by hand: the look of the world and the detail of player interactions. One game mechanic can then be realized in many visually and physically distinct ways while its outcome stays exactly as the engine computed it. The full system comprises an interaction-centric data engine, an interface through which authored character sheets/scene art/skill descriptions enter the model, and a 5B–33B model family with a real-time causal variant for play.
- **Key innovations**:
  - **Engine/VM separation of labor**: engine retains exact rules/state/camera/layout; VM synthesizes appearance and interaction detail, so generated diversity cannot desync game outcomes.
  - **Interaction-centric data engine**: data collection organized around player interactions rather than generic exploration.
  - **Authoring interface**: character sheets, scene art, and skill descriptions are injected directly into the model.
  - **Scalable + real-time model family**: 5B–33B parameters plus a low-latency causal variant for playable deployment.
  - **Per-player personalization**: the same mechanics yield a distinct character/world/skill experience per player with engine-determined timing and outcomes (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.19247) | [PDF](https://arxiv.org/pdf/2611.19247)

### SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation
- **Title (EN)**: SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation
- **Authors**: Xingyi Li; Jiahao Yang; Yiqin Zhu; Jingwen Ye; Yang Sun; Weidong Zhang
- **Affiliation**: Tencent; Fudan University (PDF first page)
- **Venue/conference**: arXiv preprint (project page: https://xingyi-li.github.io/sceneagent/)
- **Date**: 2026-11-13 (v1)
- **Abstract**: Moving a scene generator to a new game engine requires more than exporting its final output — planning, construction tools, and stored experience may all depend on the original backend. SceneAgent is a multi-agent framework for reusing the construction process and its experience across backends. A canonical SceneContext maintains the evolving world while backend adapters isolate coordinate conventions, asset bindings, and export; structured handoffs let fresh Builder sessions query persistent state without inheriting the full construction transcript. Across generations, human-approved traces are distilled into asset-ID-free Layout skills and semantic Content skills that can be retrieved and recombined. The authors introduce GameSceneBench (69 indoor/outdoor prompts) and report human tie-adjusted preference scores of 78.2–89.4% against five baselines, with deployment preserved when switching to a second engine (author-reported).
- **Key innovations**:
  - **Portable construction process**: separates persistent scene state, task-local reasoning, and reusable skills so generators survive engine/backend changes.
  - **Backend adapters + structured handoffs**: isolate coordinates/assets/export and let new Builder sessions query a canonical SceneContext without full transcript inheritance.
  - **Distilled reusable skills**: asset-ID-free Layout skills and semantic Content skills mined from human-approved traces.
  - **GameSceneBench**: 69-prompt game-scene-generation benchmark; 78.2–89.4% tie-adjusted preference vs. five baselines (author-reported).
  - **Cross-engine deployment**: swapping backend integration components preserves the shared protocol and skill library (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.17821) | [PDF](https://arxiv.org/pdf/2611.17821)

---

## 2) Game AI Bot: LLM/VLM Agents, Frameworks, and Autonomous Gameplay

### Acting by Intent, Reacting by Sight: Visual Conditioned Reflexes for Real-Time VLM Agents (ViCoR)
- **Title (EN)**: Acting by Intent, Reacting by Sight: Visual Conditioned Reflexes for Real-Time VLM Agents
- **Authors**: Qiancheng Zhou; Wenhua Zhang
- **Affiliation**: Not stated in arXiv metadata or on PDF first page (verify from PDF/full text)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-09 (v1)
- **Abstract**: Real-time games demand both deliberate exploration and split-second reactions to hazards, which pure VLM control (seconds per action) and fixed scripts (blind to scene shifts) each fail to provide. ViCoR (Visual Conditioned Reflex) pairs a main deliberative VLM with a fast visual reflex branch that invokes the same VLM in "no-thinking" mode. The main VLM defines and updates lightweight situational guidance for recurring events; on recognizing a visual trigger, the reflex branch inspects a motion-annotated local view and makes the final sub-second decision. The main VLM monitors outcomes and refines triggers/guidance during interaction with fixed model weights. Across 17 2D/3D GameWorld tasks, ViCoR reports SOTA progress 80.4% vs 66.5% and success 64.7% vs 52.9%, with 2.6× lower per-action latency (14.0s→5.4s) and 36.9% fewer tokens (author-reported).
- **Key innovations**:
  - **Conditioned-reflex architecture**: fast reflex branch bound to visual triggers + concise guidance, with the main VLM as deliberative planner/teacher (fixed weights).
  - **Latency/token efficiency**: offloads ~68% of high-frequency reactions (≈0.68 s/check), 2.6× latency cut and −36.9% tokens (author-reported).
  - **In-life reflex refinement**: triggers and guidance are revised from outcome feedback without model updates.
  - **Broad real-time validation**: 17 GameWorld games incl. fast-paced titles (Doodle Jump, Wolfenstein 3D); 1.67× progress gains in real-time games (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.18723) | [PDF](https://arxiv.org/pdf/2611.18723)

### Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games
- **Title (EN)**: Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games
- **Authors**: Jens Lehmann
- **Affiliation**: Amazon; TU Dresden (PDF first page)
- **Venue/conference**: arXiv preprint (32 pages; code: github.com/JensLehmann/weight-space-programming-games)
- **Date**: 2026-11-12 (v1)
- **Abstract**: Weight-space programming (WSP) uses language models to construct neural-network weights directly, without training. This paper tests whether known game mechanics can be compiled into compact agents that generalize to held-out levels, renderings, and start states within a game family. Across 20 privately authored, unpublished ARC-AGI-3-style game families, a "writer" LM receives simulator source with held-out levels removed and must produce one network that plays them. With a fixed 57k-parameter recurrent architecture, the best writer reaches 56% held-out-level success with feedback, while the four main writers' Python players reach 97–100%; an exploratory free-architecture condition reaches 68–90%. Written networks are program-like (93% of parameters zero; 90% of the rest small integers or powers of two); standard PPO fine-tuning removes most of their success (author-reported).
- **Key innovations**:
  - **Rule-to-network compilation**: tests LM-written weights as compact, training-free game agents with held-out source/level/render splits.
  - **Source-vs-level information-access comparison**: writers read simulator source; learners see only support levels (learners transfer ≤11%, written weights robust to render change).
  - **Program-like weight structure**: sparse, quantized-integer weights make written networks interpretable as programs.
  - **Negative results**: written weights are fragile to PPO; prompts improve noise robustness ~10⁴× but PPO still erases most success — delineates limits of WSP + RL combination (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.16981) | [PDF](https://arxiv.org/pdf/2611.16981)

### Stack more levels: how to get general and human-like Mario playing
- **Title (EN)**: Stack more levels: how to get general and human-like Mario playing
- **Authors**: Shinichi Arimura; Yuchen Li; Julian Togelius
- **Affiliation**: New York University (PDF first page)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-12 (v1)
- **Abstract**: Super Mario Bros. is a standard game-AI and PCG testbed, yet it remains unclear whether a model-free agent can reliably win unseen levels. The authors train PPO agents on increasingly large sets of PCG-generated Mario levels and evaluate generalization on 1,000 held-out levels, then shape competent policies into three gameplay archetypes — runner, killer, collector. Finally they fine-tune with Diffusion-Reward Adversarial Imitation Learning (DRAIL) using human demonstrations. More distinct PCG training levels generally improve unseen-level performance, and DRAIL fine-tuning raises action-level human-likeness while largely preserving the PPO-induced persona (author-reported).
- **Key innovations**:
  - **Scale-driven generalization study**: quantifies how the number of distinct PCG-generated training levels affects winning on 1,000 held-out Mario levels with a model-free PPO agent.
  - **Playstyle archetypes**: runner/killer/collector personas shaped from competent PPO policies.
  - **DRAIL human-likeness**: diffusion-reward adversarial imitation increases action-level human-likeness without erasing persona.
  - **PCG ↔ game-AI bridge**: directly couples level-generation diversity to agent generalization.
- **Links**: [arXiv](https://arxiv.org/abs/2611.16175) | [PDF](https://arxiv.org/pdf/2611.16175)

---

## 3) Game Benchmarks, Evaluation, and Game-State Perception

### TReC: Evaluating Move-Induced State Changes in Instruction-Conditioned Go
- **Title (EN)**: TReC: Evaluating Move-Induced State Changes in Instruction-Conditioned Go
- **Authors**: Zhuangsheng Li; Yunhan Zhang; Dailin Li; Qingxian Yu; Yu Wu; Youqi Song; Bangyuan He
- **Affiliation**: UC San Diego; Univ. of Melbourne; Univ. of Virginia; Shanghai Jiao Tong Univ.; East China Normal Univ.; New York University (PDF first page)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-13 (v1)
- **Abstract**: When a Go model predicts a move different from the expert's, coordinate distance measures how far the prediction lands from the reference. Transition Representation Consistency (TReC) instead compares how the two moves change a board-state embedding: both moves are executed under the rules from the same position, and TReC is the cosine similarity between the two resulting representation changes. With a frozen KataGo network on 680 mid-to-late-game positions from five games, the per-position gap between highest and lowest candidate is median 0.01–0.08 for direct successor-state cosine but 0.88–1.33 for TReC; TReC follows coordinate distance only weakly (median rank correlation −0.19) (author-reported).
- **Key innovations**:
  - **Transition-based move evaluation**: scores moves by the representation change they induce rather than board-coordinate proximity to a single reference.
  - **Rule-grounded**: both candidate and reference moves are legally executed from the same position, so comparisons respect Go dynamics.
  - **Discriminative metric**: TReC separates candidates far more strongly than successor-state cosine and is nearly orthogonal to coordinate distance.
  - **Implication**: more faithful evaluation for instruction-conditioned Go / language-model game agents than exact-move accuracy or spatial distance alone.
- **Links**: [arXiv](https://arxiv.org/abs/2611.17781) | [PDF](https://arxiv.org/pdf/2611.17781)

### Reading the Table: Sim-to-Real Game State Detection for the Chef's Hat Card Game
- **Title (EN)**: Reading the Table: Sim-to-Real Game State Detection for the Chef's Hat Card Game
- **Authors**: Connor Gäde; Matthias Kerzel; Hauke Bünning; Jan-Gerrit Habekost; Mariana Barros; Stefan Wermter
- **Affiliation**: Knowledge Technology, Dept. of Informatics, University of Hamburg, Germany (PDF first page)
- **Venue/conference**: Dungeons, Neurons, and Dialogues workshop (DnD-SIDC 2026) at ICANN 2026 (as stated on arXiv)
- **Date**: 2026-11-11 (v1)
- **Abstract**: Tabletop games combine social interaction, game-state tracking, and physical manipulation in human–agent interaction. To assess game state, a robot must detect closely related objects such as different card designs, for which real-world annotation is costly. The authors build a fully automated synthetic-data pipeline using re-projection of known 3D coordinates for automatic labels plus domain randomization to bridge the reality gap, collecting 25,413 samples to fine-tune detection and segmentation models that assign cards to game zones and infer game state. On a real NICO humanoid robot the pipeline reaches F1 0.906 for card-to-zone assignment, providing perception for autonomous Chef's Hat play against humans (author-reported).
- **Key innovations**:
  - **Automated sim-to-real labeling**: 3D re-projection generates card/zone labels with no manual annotation; domain randomization closes the gap.
  - **Game-state inference from perception**: detection + segmentation → card-to-zone assignment → game state for a social card game.
  - **Real-robot validation**: F1 0.906 on a NICO humanoid, a concrete perceptual foundation for an autonomous game-playing agent.
  - **Cross-cutting relevance**: bridges game-AI state tracking, robot vision, and human–agent social gameplay.
- **Links**: [arXiv](https://arxiv.org/abs/2611.15524) | [PDF](https://arxiv.org/pdf/2611.15524)

---

## 4) Procedural Content Generation and Game Creation

### Syntactic Segmentation and Collage Generation for Videogame Levels with Perceptual Distance
- **Title (EN)**: Syntactic Segmentation and Collage Generation for Videogame Levels with Perceptual Distance
- **Authors**: Ross Mawhorter; Matthew Guzdial
- **Affiliation**: University of Alberta (PDF first page)
- **Venue/conference**: 22nd Artificial Intelligence and Interactive Digital Entertainment Conference (AIIDE 2026), as stated on arXiv
- **Date**: 2026-10-28 (v1)
- **Abstract**: Many procedural level-design techniques combine hand-authored level chunks, and some analysis techniques rely on a higher-level graph abstraction of the design. This paper computes both automatically from an existing design. It introduces *perceptual distance*, based on Space Syntax ideas from architecture, and uses it to segment level designs with hierarchical clustering. The authors compare with prior StarCraft analysis, show results on rooms from Super Metroid, and demonstrate a proof-of-concept level-generation algorithm based on the segmentation.
- **Key innovations**:
  - **Perceptual distance for levels**: imports Space Syntax analysis to automatically derive a design's structure from its geometry.
  - **Automatic chunk + graph extraction**: hierarchical clustering segments levels and recovers the abstraction graph without manual annotation.
  - **Cross-game validation**: comparisons against StarCraft analysis and results on Super Metroid rooms.
  - **PCG downstream use**: proof-of-concept collage generation turns segmentation into a level-generation algorithm.
- **Links**: [arXiv](https://arxiv.org/abs/2610.38987) | [PDF](https://arxiv.org/pdf/2610.38987)

---

## 5) Related Techniques: Self-Play, MARL, Imitation, Model-Based RL, and Chess

### When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners
- **Title (EN)**: When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners
- **Authors**: Mohammad Khoshnazar; Mike Degany; Deyuan Qu; Qing Yang; Matyas Szanto
- **Affiliation**: Universität Bremen; University of North Texas; Toyota Motor North America; Budapest University of Technology and Economics (PDF first page)
- **Venue/conference**: CoRL 2026 — Human-Centered Robot Learning and Interaction (HumanRLI) Workshop; code: github.com/mkhoshnam/Selfplay-PPO-handover
- **Date**: 2026-11-13 (v1)
- **Abstract**: Cooperative self-play can train a humanoid to receive an object with no human data, but the partner it meets after training is not the one it trained with. In a physics-based parcel handover between a Unitree G1 and a learned giver trained by alternating PPO self-play, the receiver completes 95%/90% of handovers with its own partner (two seeds) but only 31% with unseen scripted partners. The failure is traced to a single learned rendezvous timing under a shared reward. Hidden start-delay randomisation (HSD) — a one-line rule on the learned partner invisible to the receiver — lifts unseen-partner success from 31% to 80% after 300 updates (vs 35–41% for a budget-matched control), generalizes across held-out conditions, and cuts high-force contact 3–5× (author-reported).
- **Key innovations**:
  - **Diagnosis of self-play co-adaptation failure**: identifies overfit rendezvous timing as the cause of poor zero-shot cooperation with unfamiliar partners.
  - **Hidden start-delay randomisation (HSD)**: minimal, one-line partner-side augmentation requiring no partner retraining.
  - **Strong empirical recovery**: 31% → 80% unseen-partner success, robust across seeds/conditions; reduced contact forces.
  - **General lesson for game/self-play agents**: diversity on the *partner* side is essential for robustness to test-time collaborators.
- **Links**: [arXiv](https://arxiv.org/abs/2611.18491) | [PDF](https://arxiv.org/pdf/2611.18491)

### When Cooperation Must Change: Semantic Strategy Unlearning in Multi-Agent Reinforcement Learning
- **Title (EN)**: When Cooperation Must Change: Semantic Strategy Unlearning in Multi-Agent Reinforcement Learning
- **Authors**: Wenhan Wu; Linghan Chen; Yudong Gao; Fan Yang; Honglong Chen; Kai Yin; Jiawei Jiang; Chuang Hu
- **Affiliation**: Wuhan University; Univ. of Adelaide; HKUST; Huaqiao University; China University of Petroleum (East China); Central China Normal University (PDF first page)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-13 (v1)
- **Abstract**: Cooperative MARL relies on learned coordination conventions in distributed services, multi-robot control, and collaborative games. When deployment requirements change, a previously useful convention may become obsolete or unsafe, and teams must remove it while preserving useful cooperation — hard because the same relational pattern can be reproduced by different agents at different histories. The paper formalizes *semantic coordination-strategy unlearning* and proposes CARVE: causal coordination attribution identifies influential interactions, retain-aware subspace updates limit interference, counterfactual re-coordination teaches alternatives, and adversarial auditing checks whether the target convention can still be recovered; accepted updates are merged into decentralized actors. Across five cooperative MARL benchmarks CARVE reduces nominal convention-completion and worst-case elicitation by 91.4% and 83.3% at 5.9% median utility loss and unchanged inference latency (author-reported).
- **Key innovations**:
  - **New problem formulation**: role-invariant, semantic unlearning of learned coordination conventions in MARL.
  - **CARVE pipeline**: causal attribution + retain-aware subspace updates + counterfactual re-coordination + adversarial auditing.
  - **Deployable**: updates merged into decentralized actors with no added inference latency.
  - **Strong results**: >91% reduction in convention completion, >83% in worst-case elicitation with ~6% utility cost (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.17917) | [PDF](https://arxiv.org/pdf/2611.17917)

### Advancing Quantum Reinforcement Learning with Differentiable Quantum Architecture Search and Adaptive Non-local Observables
- **Title (EN)**: Advancing Quantum Reinforcement Learning with Differentiable Quantum Architecture Search and Adaptive Non-local Observables
- **Authors**: Junghoon Justin Park; Kyumin Lee; Anna Jung; Samuel Yen-Chi Chen; Huan-Hsin Tseng; Shinjae Yoo; Jiook Cha
- **Affiliation**: Seoul National University; Sungkyunkwan University; Wells Fargo; Brookhaven National Laboratory (PDF first page)
- **Venue/conference**: 2026 IEEE International Conference on Quantum Artificial Intelligence (QAI)
- **Date**: 2026-11-14 (v1)
- **Abstract**: Quantum RL with variational quantum circuits is constrained by fixed measurement protocols and hand-designed ansätze; Adaptive Non-local Observables (ANO) and Differentiable Quantum Architecture Search (DiffQAS) address these separately. This paper ablates both within a Quantum Time-series Transformer in a 2×2 design over six environments (two classic-control tasks, four Atari 2600 games). The quantum agent beats a matched classical transformer on five of six environments (e.g., MarioBros 360.0 vs 304.0; Breakout 17.2 vs 2.5) with ~12.5× fewer transformer parameters on Atari. ANO gives the largest continuous-control gain (CartPole 347.7 vs 223.2); DiffQAS the largest Atari gains (Breakout 17.2 vs 3.0; DonkeyKong 70.0 vs 37.0); combining them interacts asymmetrically (author-reported).
- **Key innovations**:
  - **First joint ANO × DiffQAS ablation in QRL** with a matched classical baseline and parameter-matched comparisons on Atari.
  - **Bottleneck-guided design rule**: choose ANO if measurement basis limits performance, DiffQAS if gate topology does; applying both indiscriminately can hurt.
  - **Parameter efficiency**: ~12.5× fewer transformer parameters on four Atari games at higher scores (author-reported).
  - **Game RL relevance**: concrete quantum-RL results on MarioBros/Breakout/DonkeyKong with ablations.
- **Links**: [arXiv](https://arxiv.org/abs/2611.19182) | [PDF](https://arxiv.org/pdf/2611.19182)

### VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess
- **Title (EN)**: VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess
- **Authors**: Matěj Kripner; Milan Straka
- **Affiliation**: Charles University, Faculty of Mathematics and Physics, Prague (PDF first page)
- **Venue/conference**: CoRL 2026 Workshop "Pretrain to Adapt: What Makes a Pretrained Policy Adaptable?"
- **Date**: 2026-11-09 (v1)
- **Abstract**: Vision-language-action models need task-specific fine-tuning; this study asks how much data/updates are needed, how to select checkpoints, and whether simulation can reduce real-data cost, using a chess task where an SO-101 arm moves a king between squares named in text (e.g., e4, a5). Fine-tuning π₀.₅ with teleoperated and simulated demonstrations shows success scaling with data and updates in simulation; a short learning-rate cool-down adds up to 31 points and is needed for fair checkpoint comparison, while validation loss/action error are unreliable selectors. On the real arm (≤256 teleop demos, 10 policies × 25 trials), simulated-data pretraining helps most when real data is scarce; self-rollout/filtered-BC/RECAP/coach-correction/residual-RL variants gave no measurable gain over plain BC (author-reported).
- **Key innovations**:
  - **Chess as a grounded VLA benchmark**: language-named board coordinates demand precise manipulation + spatial/symbolic understanding.
  - **Sim-to-real data recipe**: scripted-expert simulated demos substantially bootstrap real-world fine-tuning under low data.
  - **Checkpoint-selection finding**: LR cool-down ≥31 points; validation loss/action error mislead — important for imitation/VLA practice.
  - **Negative results**: several self-improvement/RL-style refinements fail to beat plain behavior cloning in this setting.
- **Links**: [arXiv](https://arxiv.org/abs/2611.12676) | [PDF](https://arxiv.org/pdf/2611.12676)

### f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models (DiSPaT)
- **Title (EN)**: f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models
- **Authors**: Hoang Tran Vuong; Linh Ngo Van; Dang Nguyen; Thin Nguyen; Phuoc Nguyen; Mehrtash Harandi; Trung Le
- **Affiliation**: Hanoi University of Science and Technology; Deakin University; Monash University (PDF first page)
- **Venue/conference**: ICML 2026 (PMLR 306, Seoul, South Korea)
- **Date**: 2026-11-13 (v1)
- **Abstract**: DiSPaT is an LLM self-play fine-tuning framework built on f-divergence minimization: at each iteration the policy generates synthetic samples as pseudo-anomalies while a critic discriminator separates them from real normal data, and the resulting signal drives policy updates that align the model distribution with true normality. A tight approximation links the training objective to reducing the distributional gap. Across diverse tabular benchmarks DiSPaT outperforms prior LLM-based, deep-learning, and classical unsupervised detectors (author-reported).
- **Key innovations**:
  - **Principled self-play objective**: f-divergence-minimization view of generator–discriminator self-play for tightening a model's "normality" description.
  - **Pseudo-anomaly generation**: the policy's own samples become adversarial training signal without external anomaly labels.
  - **Cross-domain relevance**: a notable ICML 2026 self-play RL method; relevant to self-play/reward-shaping technique transfer even though the task is tabular anomaly detection rather than a game.
- **Links**: [arXiv](https://arxiv.org/abs/2611.18370) | [PDF](https://arxiv.org/pdf/2611.18370)

---

## Cross-Cutting Observations

- **Industry game AI is now a first-class research track**: Tencent (GameWM, SceneAgent) and Amazon (WSP) ship system-level papers this window — full generative-game stacks, portable multi-agent scene generators, and training-free rule-to-network game agents — signaling a shift from isolated benchmarks to deployable game systems.
- **Real-time control is a co-design problem**: ViCoR and HSD both attack the gap between training-time fluency and deployment-time conditions (fast hazards; unfamiliar partners) via architectural/augmentation tricks rather than heavier training, echoing game agents' need for robustness to test-time dynamics.
- **Generalization is being driven by content scale and diversity**: more PCG levels improve unseen Mario play; partner-side randomization improves self-play handover; reusable skills improve scene generation across engines — diversity of the training/partner/distribution substrate recurs as the lever.
- **Evaluation is moving from outcome scores to mechanism**: TReC scores Go moves by induced state change, SceneAgent's GameSceneBench and OCTAVE-style capability decomposition diagnose *why* agents fail, and Chef's Hat supplies a perceptually grounded game-state benchmark.
- **Classical RL techniques remain active in game-like settings**: self-play (HSD, DiSPaT), imitation learning (DRAIL Mario, π₀.₅ chess), MARL convention unlearning (CARVE), and model-based/quantum RL on Atari all appear with concrete ablations and negative results that clarify when each helps.

## Coverage Notes and Gaps

- **Deduplication**: excluded all arXiv IDs already appearing in prior `game-rl-daily` digests (1,731 known IDs); every included ID was grep-verified as not previously *featured* in a game-rl digest. Two papers — Weight-Space Programming (2611.16981) and scaled-PCG Mario (2611.16175) — were mentioned in the 2026-11-15 game-rl digest's method note as intentionally excluded because they were covered by that day's `arxiv-ai-search`; they are included here because no prior game-rl digest actually covered them and they are directly on-topic. SceneAgent (2611.17821) also appears in today's `conference-digest.md` (different digest focus) and is included here for its game-generation relevance.
- **Topic coverage**: direct coverage for game foundation/world models and industry game AI (GameWM, SceneAgent), Game AI bots/LLM-VLM agents (ViCoR, WSP, Mario), game benchmarks/state perception (TReC, Chef's Hat), PCG (AIIDE level segmentation; Mario PCG levels; SceneAgent), and related techniques (self-play, MARL, imitation, model-based/quantum RL). Classic cards (StarCraft/Dota/Go/chess/poker/NetHack/Atari) appear via Go (TReC), chess (2611.12676), Atari (2611.19182) and Mario (2611.16175); dedicated new Atari/StarCraft/Dota/NetHack *training* papers were sparse in the deduplicated fresh window.
- **Affiliations/venues**: affiliations were PDF-verified for 12/13 papers; ViCoR's affiliation was not stated on the PDF first page. Venue labels are taken from arXiv comments/journal fields or PDF proceedings footers and may reflect acceptance status rather than final published versions.
- **Sources consulted (arXiv API, 2026-11-17)**: keyword queries — `all:"game agent"`, `all:"reinforcement learning" AND all:game`, `all:"LLM agent" AND all:game`, `all:"game" AND all:"self-play"`, `all:"world model" AND (all:game OR all:Minecraft OR all:Atari)`, `all:"Minecraft"/"Atari"/"StarCraft"/"Dota"/"poker"/"NetHack"` combinations, `all:"procedural content generation"`, `all:"game" AND all:"benchmark" AND all:agent`, `all:"game foundation model"`, `all:"NPC"`, `all:"game" AND all:"offline reinforcement"`, plus a recency sweep of `cat:cs.MA/cs.AI/cs.LG/cs.CL/cs.CV/cs.RO` sorted by submittedDate; PDF first pages parsed with pypdf for affiliations.
