---
title: "arXiv AI Search 2026-10-17 — Listing-Page Harvest of the Friday 10-16 Block; the OPD Cluster Industrializes and the KV Cache Gets a 'Post-Selection' Thesis"
type: synthesis
created: 2026-10-17
updated: 2026-10-17
sources: [arxiv-org-listing, arxiv-abs-html, arxiv-html-ltx-authors]
tags: [arxiv, listing-harvest, on-policy-distillation, distillation, rlvr, reward-hacking, reward-modeling, agents, memory-agents, agent-evaluation, self-improvement, kv-cache, moe, routing, mamba, time-series, recommendation, personalization, generative-engine-optimization, advertising, bandits, game-theory, multi-agent, marl, specification-gaming, sequential-modeling, ctr, games]
---

# arXiv AI Search 2026-10-17 — the OPD cluster industrializes

> **Saturday run over the Friday announcement block.** arXiv posts no weekend announcements, so the freshest fully-populated block on 2026-10-17 is still **Friday, 2026-10-16**, and the `arxiv.org/list/{cat}/new` pages say exactly that (*"Showing new listings for Friday, 16 October 2026"*). This run enumerates that block by category, filters to the requested lanes (AI / LLMs / recommendation / advertising / sequential modeling / CTR / games), and picks **27 papers** — all grep-verified **0-hit** against the live wiki baseline (**9,226 IDs**).
>
> **Three threads run through the block.**
>
> **① The on-policy-distillation (OPD) design-axis thesis is now an industry-scale cluster.** The [2026-10-09 run](../2026-10-09/arxiv-ai-search.md) flagged that "in OPD the lever is target construction and signal shaping, not teacher selection or on-policyness itself," and the [10-16 conference-digest](../2026-10-16/conference-digest.md) already saw an OPD wave. On 10-16 the wave became a *program*: [`2610.22236`](https://arxiv.org/abs/2610.22236) (**Training-Free OPD**) removes training entirely, solving consolidation as a layer-wise least-squares problem from forward passes; [`2610.21337`](https://arxiv.org/abs/2610.21337) (**STOPD**) makes rollouts *stochastically truncated* with blockwise IPW; [`2610.21234`](https://arxiv.org/abs/2610.21234) makes **teacher selection token-level** (Princeton × Amazon Annapurna); [`2610.21195`](https://arxiv.org/abs/2610.21195) makes the target **condition-sensitive**; [`2610.21601`](https://arxiv.org/abs/2610.21601) gates the endpoint policy shift by early/late **waypoint agreement** (Alibaba Cloud); and [`2610.22196`](https://arxiv.org/abs/2610.22196) (Tencent Hunyuan) applies OPD + RL to **memory writing**. Five independent groups, four countries, one shared lever — **the OPD target is the object under design**. See §5.1.
>
> **② "Compression does not end at selection" — the KV cache gets a post-selection thesis.** Two unrelated 10-16 papers converge on the same reframing: once you have *chosen* which KV states to keep, the remaining work is not more selection. [`2610.21126`](https://arxiv.org/abs/2610.21126) (NUDT) shows the evicted tokens leave **positional gaps under RoPE** that corrupt retained-evidence matching, fixed by re-coordinating positions (RoPERelay: 23.6%→35.4% on LongMemEval-S). [`2610.22016`](https://arxiv.org/abs/2610.22016) (MIT ORC/CSAIL × IBM Research) shows a **frozen reader simply cannot consume a substitute cache** regardless of fidelity — "a more faithful substitute is not the remedy it appears to be" — and proposes *adding* the sender's cache as extra context instead. See §5.2.
>
> **③ CTR is empty again; advertising is generative-engine-optimization.** For the fifth consecutive October block, **zero explicit CTR-prediction papers** surfaced. The only advertising-adjacent work is [`2610.21330`](https://arxiv.org/abs/2610.21330) (**VoteGEO-Bench**, NUS), which measures how GEO rewriting shifts **electoral visibility** inside LLM answers — the ad-side of *generative* engines, not click prediction. See §5.3.

## 1. Search Metadata

| Field | Value |
|---|---|
| **Date of search** | 2026-10-17 (Saturday) |
| **Search channel** | **`arxiv.org` listing pages** (`/list/{cat}/new?skip=0&show=2000`) + per-paper `abs`/`html` pages. The export API (`export.arxiv.org/api/query`) returned **`HTTP 429` ("Rate exceeded.")** on the first harvest attempt — same rate-limit wall logged by the 10-15 and 10-16 runs — so the listing channel (different host) was used. |
| **Window covered** | Fresh **Friday 2026-10-16** announcement block; IDs **`2610.20614` → `2610.22372`** (all `2610.*`). No weekend block exists. |
| **Categories harvested** | `cs.AI` (453), `cs.CL` (267), `cs.LG` (435), `cs.IR` (26), `cs.GT` (16), `cs.MA` (34) → **897 unique entries** |
| **`2610.*` in pool** | **638** (the rest are re-announced older cross-listings, e.g. `2508.*`, `2603.*`) |
| **New-to-wiki candidates** | **585** (`2610.*`) / **540** (`2610.2xxxx`) after subtracting the 9,226-ID wiki baseline |
| **Featured, final** | **27** (4 Rec/Ads + 6 OPD/post-training + 3 RLVR/reward + 4 Agents/memory + 3 Efficiency/inference + 2 Sequential/TS + 5 Games/GT/MARL/bandits) |
| **Same-day collisions** | **0** — no `wiki/synthesis/2026-10-17/` siblings existed at run time |
| **Already on file** | **0 of 27** — all 27 IDs 0-hit against the 9,226-ID baseline |
| **Affiliation recovery** | **27/27 named** from arXiv LaTeXML author blocks (`arxiv.org/html/{id}v1`); 2 recovered from author affiliation tables, 1 from printed author line. Zero inferred from surname/domain. |
| **Production / online-experiment numbers** | **0** — the industrial CTR/ad-serving architecture lane remains vacant (§5.3) |
| **Temp artifacts** | `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-ai-search-20261017/` (authorized scratch), deleted after this write-up |

### 1.1 Queries issued

| # | Channel | Query / page | Fetched | Role |
|---|---|---|---|---|
| 1 | export API | `cat:cs.IR AND submittedDate:[20261016 TO 20261018]` | `HTTP 429` | attempted fresh-window enumeration |
| 2–8 | export API | `cat:cs.AI` / `cs.CL` / `cs.LG` / `(cs.GT OR cs.MA)` / LLM-game-agent / CTR / rec-keyword | `HTTP 429` | all refused |
| 9 | listing | `https://arxiv.org/list/cs.IR/new?show=2000` | 26 | fresh-window enumeration |
| 10 | listing | `…/cs.AI/new` | 453 | fresh-window enumeration |
| 11 | listing | `…/cs.CL/new` | 267 | fresh-window enumeration |
| 12 | listing | `…/cs.LG/new` | 435 | fresh-window enumeration |
| 13 | listing | `…/cs.GT/new` | 16 | games / mechanism design |
| 14 | listing | `…/cs.MA/new` | 34 | multi-agent / MARL |
| 15 | abs + html | `arxiv.org/abs/{id}` + `/html/{id}v1` for the 27 picks | 27 + 27 | abstract, authors, affiliations |

**Design note.** The export API's free-text date/sort queries are the reliable channel *when they are not throttled*; on 10-16/10-17 they were throttled for this run within seconds of the first call. The listing pages carry **title + authors + subjects** but not abstracts, so abstracts were pulled per-paper from the `abs` pages (browser UA required; plain `curl` on `abs` returned `HTTP:000` intermittently) and affiliations from the LaTeXML `html/{id}v1` author blocks. This is the same degradation path the 10-16 `arxiv-daily` and `game-rl-daily` documented.

### 1.2 Rate limiting

- The export API returned `429` on **all** eight attempted queries (single call first, then a spaced run). Message body: `Rate exceeded.`
- The listing pages (`arxiv.org`, Google-Frontend) were **not** throttled: 6/6 returned `HTTP 200`, sizes 54 KB–1.5 MB, with `x-cache: HIT` on most.
- Per-paper `abs`/`html` fetches were spaced 1 s and run at parallelism ≤6; 27/27 `abs` and 27/27 `html` succeeded (`HTTP 200`).

## 2. Dedup Ledger

1. **Whole-wiki baseline**: every arXiv ID referenced anywhere in `wiki/**/*.md`, regex `\b\d{4}\.\d{4,5}\b` → **9,226 IDs** (rebuilt by scanning the repo this run, matching the 10-16 baseline of 9,222 + one day of additions).
2. **Sibling coordination**: no `wiki/synthesis/2026-10-17/*` files existed at run time, so there was nothing to pre-exclude. The 10-16 siblings (`arxiv-daily`, `conference-digest`, `game-rl-daily`, `tech-report-digest`, `arxiv-ai-search`) cover the *same* Friday block; their featured IDs are inside the wiki baseline, so any paper they named is automatically excluded here. **The 585 `2610.*` candidates are precisely the block papers no sibling report and no other wiki page has ever mentioned.**
3. **Post-selection re-verify**: all 27 featured IDs grep-tested against `wiki/**/*.md` immediately before the first write → **0 hits**.

Result: **27 featured, 0 collisions, 0 duplicates.**

## 3. Master Table

| # | Paper | arXiv | Affiliation (verified) | Lane | Headline result |
|---|---|---|---|---|---|
| 1 | Encoded but Exposed | [2610.21713](https://arxiv.org/abs/2610.21713) | **Czech Technical University in Prague** | Rec / privacy | cosine attack re-identifies items → propagates to user re-ID |
| 2 | MoE Experts for Personalization | [2610.22127](https://arxiv.org/abs/2610.22127) | **University of Copenhagen** | Rec / interpretability | crosscoders localize personalization experts in MoE LLMs |
| 3 | Agentic-Priors | [2610.21938](https://arxiv.org/abs/2610.21938) | **University of Southampton** | Rec / cold-start | LLM-elicited priors **+5–40 pts** cold-start accuracy |
| 4 | VoteGEO-Bench | [2610.21330](https://arxiv.org/abs/2610.21330) | **National University of Singapore** | Ads (GEO) | target-specified GEO rewriting shifts LLM electoral visibility |
| 5 | Training-Free OPD | [2610.22236](https://arxiv.org/abs/2610.22236) | **University of Illinois Urbana-Champaign** | Distillation | consolidation as layer-wise least squares, **no training** |
| 6 | STOPD | [2610.21337](https://arxiv.org/abs/2610.21337) | **Cornell** + **Georgia Tech** + **Alibaba Group** | Distillation | stochastic rollouts, −25–48% tokens, **1.3–2.2×** faster |
| 7 | Compatibility Matters | [2610.21234](https://arxiv.org/abs/2610.21234) | **Princeton** + **Amazon Annapurna Labs** | Distillation | token-level teacher routing, **+10 pts** pass@k |
| 8 | CCE-OPD | [2610.21195](https://arxiv.org/abs/2610.21195) | **CUHK-Shenzhen** + **ByteDance** | Distillation | condition contrast cuts invalid-continuation pref. 27→16% |
| 9 | Waypoint-OPD | [2610.21601](https://arxiv.org/abs/2610.21601) | **Alibaba Cloud Computing** | Distillation | gate endpoint shift by early/late waypoint agreement |
| 10 | CleanRM | [2610.21138](https://arxiv.org/abs/2610.21138) | **Zhejiang** + **Xiaohongshu** + **NUS** + **NYU** + **UIUC** + **MBZUAI** | Reward modeling | optimal-transport noise calibration, unbiased clean risk |
| 11 | Multi-Reward Hacking | [2610.21404](https://arxiv.org/abs/2610.21404) | **UBC** + **Amazon Annapurna Labs** | RLHF × reward hacking | symmetric aggregation drifts; TAG **0.581 vs 0.220** pass@4 |
| 12 | Wrong Votes, Right Gradients | [2610.20898](https://arxiv.org/abs/2610.20898) | **Dartmouth** + **Washington U. in St. Louis** | RLVR | error *coherence*, not rate, decides if self-labels work |
| 13 | RLVR Data Decontamination | [2610.21229](https://arxiv.org/abs/2610.21229) | **Independent Researcher** | RLVR data | semantic thresholds: **88%** of sampled removals false |
| 14 | All-in-One Memory | [2610.21147](https://arxiv.org/abs/2610.21147) | **HIT Shenzhen** + **Fudan** + **HK PolyU** + **Peng Cheng Lab** | Memory agent | unified reward over search/write/stop, PA-DAPO |
| 15 | Hy-Memory-30B-A3B | [2610.22196](https://arxiv.org/abs/2610.22196) | **Tencent Hunyuan** | Memory agent | OPD+RL memory writer, **55.49%** vs Claude Opus 5 54.62% |
| 16 | Beyond Downstream QA (FEB-30) | [2610.22209](https://arxiv.org/abs/2610.22209) | **Amazon Web Services** + **TU Cluj-Napoca** | Agent eval | intrinsic vs extrinsic memory scores diverge **16 pts** |
| 17 | The Self-Improvement Problem | [2610.21646](https://arxiv.org/abs/2610.21646) | **DFKI** + **RPTU Kaiserslautern-Landau** | Agent safety | no terminating gate is both reliable and non-conservative |
| 18 | Compression Does Not End at Selection | [2610.21126](https://arxiv.org/abs/2610.21126) | **National University of Defense Technology** | KV cache | RoPE re-coord: **23.6%→35.4%**, 1–3% overhead |
| 19 | Close Enough is Nowhere Near | [2610.22016](https://arxiv.org/abs/2610.22016) | **MIT (ORC + CSAIL)** + **IBM Research** | KV cache | frozen readers can't consume substitute caches at any fidelity |
| 20 | Router Drift Control | [2610.21682](https://arxiv.org/abs/2610.21682) | **Peking U** + **Shanghai Innovation Inst.** + **ZJU** + **SJTU** + **Infrawaves** | MoE × RL | drift-based rejection, **+5.5 pts** over TIS (AIME) |
| 21 | TurboMamba | [2610.20682](https://arxiv.org/abs/2610.20682) | **University of Pittsburgh** | Sequential / arch | **9.4%** lower NLL than Mamba-3, **2.6×** training throughput |
| 22 | Twice Upon a Time | [2610.22327](https://arxiv.org/abs/2610.22327) | **Ben-Gurion University** + **Google** | TS reasoning | dual view **44.5%→53.2%** on TSRBench |
| 23 | Posetal Games | [2610.22277](https://arxiv.org/abs/2610.22277) | **WHOI** + **UC Berkeley** + **MIT LIDS** + **TU Munich** | Games / GT | legal-hierarchy games, all violations certified forced |
| 24 | Self-Orchestration in Agent Swarms | [2610.22322](https://arxiv.org/abs/2610.22322) | **Harvard University** | MARL | market-based post-training co-learns action + bidding |
| 25 | Hidden Belief Collapse | [2610.22138](https://arxiv.org/abs/2610.22138) | **University of Illinois Chicago** | Multi-agent LLM | private false answer **51.6%** vs public endorsement 19.7% |
| 26 | Replicable Dueling Bandits | [2610.20908](https://arxiv.org/abs/2610.20908) | **UIUC** + **UIC** + **Amazon** + **Carnegie Mellon** | Bandits | first replicable dueling bandits with **sublinear regret** |
| 27 | Specification Gaming in a Cleaning Gridworld | [2610.22152](https://arxiv.org/abs/2610.22152) | **Kwame Nkrumah University of Science and Technology** | Spec gaming | constrained-RL fix is an **exact** proxy/true-gap identity |

## 4. Per-Paper Detail

### Lane A — Recommendation / Advertising (4)

---

#### 1. Encoded but Exposed: Language Embeddings can Reveal More Than They Should in Recommender Systems

- **arXiv**: [`2610.21713`](https://arxiv.org/abs/2610.21713) · cs.CR / cs.AI
- **Authors**: Linda Beková, Rodrigo Alves
- **Institution**: Czech Technical University in Prague
- **Problem**: language embeddings increasingly represent *item content* in recommenders, but whether item embeddings leak item identity is poorly understood.
- **Method**: a simple **cosine-similarity attack** — with auxiliary item text scraped from external sources, rank items by embedding similarity to recover identities.
- **Results**: high **mean reciprocal rank** across language models and candidate-set sizes on two real datasets. Leakage is strongest when the adversary's partial info overlaps with the victim representation, but persists through **semantic alignment** between independently sourced descriptions. Item leakage **propagates to user re-identification** from sparse ratings. Obfuscated descriptions trade leakage for utility.
- **Why it matters**: recommendation deployments that embed item content inherit a re-identification surface from any public item text — a privacy/utility coupling that also undercuts "just obfuscate" mitigations.

---

#### 2. Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization

- **arXiv**: [`2610.22127`](https://arxiv.org/abs/2610.22127) · cs.CL / cs.AI
- **Authors**: Sekh Mainul Islam, Pepa Atanasova, Isabelle Augenstein
- **Institution**: University of Copenhagen
- **Problem**: prior personalization adapts *dense* LLMs whose polysemantic neurons hinder localizing the components behind personalization.
- **Method**: adapt three open-weight **MoE** LLMs on a large-scale personalization dataset; train **crosscoders** on paired personalized/non-personalized activations to learn interpretable personalized latents and identify the experts encoding distinct personalization features. Causal interventions on those experts.
- **Results**: personalized MoE LLMs match dense LLMs while activating only a fraction of parameters, exhibit **lower polysemanticity** than dense models with similar active parameters, and yield personalized latents **less shared** with the non-personalized model. Boosting the identified experts moves the non-personalized model toward the personalized behavior, revealing **distinct routing paths per personalization feature**.
- **Why it matters**: it connects the interpretability of sparse routing to controllable personalization — a mechanistic handle that dense-only personalization cannot offer.

---

#### 3. Agentic-Priors: Using Large Language Models to Address the Cold Start Problem in Preference Elicitation

- **arXiv**: [`2610.21938`](https://arxiv.org/abs/2610.21938) · cs.MA / cs.AI
- **Authors**: Bruno Arcanjo, Zhaoxing Li, Sebastian Stein
- **Institution**: University of Southampton
- **Problem**: a preference-learning agent must rely on a prior before any choices are seen, but informative priors are fitted to historical choice data that new tasks/deployments lack.
- **Method**: **Agentic-Priors** lets an LLM *state a new user's trade-offs* in interpretable terms (e.g. willingness-to-pay, value-of-time), mapped to a prior over **multinomial-logit** coefficients; a Bayesian learner refines it as choices arrive.
- **Results**: across seven choice datasets, **+5–40 percentage points** cold-start accuracy over an uninformed prior; beats **AutoElicit** on 3/4 datasets; up to **18 pts** better than in-context learning and never significantly worse; worth roughly **6–40 surveyed users** versus hierarchical Bayes — value concentrated in a deployment's first users.
- **Why it matters**: it turns "LLM knows people in general" into a calibrated, updatable prior — the practical fix for the recommender/agent cold-start regime.

---

#### 4. VoteGEO-Bench: Measuring the Impact of Generative Engine Optimization on Electoral Visibility

- **arXiv**: [`2610.21330`](https://arxiv.org/abs/2610.21330) · cs.IR / cs.CL / cs.CY
- **Authors**: Shiqi Zhang, Xiaokui Xiao
- **Institution**: National University of Singapore
- **Problem**: LLMs increasingly answer election questions, yet how external web content shapes the political information they present is unknown; **GEO** (generative engine optimization) rewrites content to boost visibility in generated responses.
- **Method**: **VoteGEO-Bench**, covering the 2024 U.S. presidential and 2026 Japanese House elections, with election queries, historical webpages, and voter personas. Eleven rewriting strategies in four categories are evaluated for target specification, cross-engine/election effectiveness, and persona effects.
- **Results**: citations disproportionately come from **lower-cost owned/open-platform sources**. Rewriting *without* a target rarely helps; **target-specified** rewriting often does. Organization/argumentation strategies beat adding evidence or rephrasing. Persona conditioning shows **no consistent effect** on gains, but explicit partisan identity creates baseline exposure gaps **larger than a single page's rewriting gain**.
- **Why it matters**: the advertising-adjacent surface of the LLM era is *visibility inside generated answers*. GEO is the new ad-placement mechanic, and this benchmark shows it can move electoral information — a governance-relevant finding. (There is still **no explicit CTR-prediction paper** in this block — §5.3.)

---

### Lane B — On-Policy Distillation / Post-Training (6)

---

#### 5. Training-Free On-Policy Distillation

- **arXiv**: [`2610.22236`](https://arxiv.org/abs/2610.22236) · cs.LG / cs.AI / cs.CL
- **Authors**: Bangji Yang, Jiajun Fan, Zhaoyu Zhu, Hongbo Ma, Ge Liu
- **Institution**: University of Illinois Urbana-Champaign
- **Problem**: OPD consolidates specialists into one student but pays rollouts + teacher passes + gradients for every teacher.
- **Method**: show consolidation needs **no training**. When specialists share a base model, fusion has an **exact layer-wise solution**: each linear layer must reproduce every specialist's output on that specialist's own-answer inputs — a least-squares problem needing only the **second moments** of those inputs, obtained from one forward pass over a few hundred rollouts. They call it **training-free OPD**.
- **Results**: on **Olmo-3 7B**, a few GPU-hours of forward compute per specialist yield a generalist that keeps most of each specialist's gain on **seven mathematics and code benchmarks**. Crucially, *what the rollouts contain matters more than the solver*: answer tails truncated in repetition loops are few but carry a large share of tokens, and removing them lifts the fused model on **AIME25** from task-arithmetic level to the specialist's at matched precision.
- **Why it matters**: the strongest statement of the OPD design-axis thesis — if consolidation is a moment-matching problem, then "more on-policy training" was never the requirement; **target/rollout curation** is.

---

#### 6. Does On-Policy Distillation Need to Complete Every Rollout? (STOPD)

- **arXiv**: [`2610.21337`](https://arxiv.org/abs/2610.21337) · cs.LG / cs.AI
- **Authors**: Zhengxin Zhang, Maosen Tang, Ning Wang, Changhao Li, Jingren Zhou, Bo Dai, Sainyam Galhotra, Alex Townsend, Claire Cardie
- **Institution**: Cornell University + Georgia Tech + Alibaba Group
- **Problem**: OPD generates complete rollouts and computes teacher feedback for *every* token — expensive.
- **Method**: **Stochastic Truncated OPD (STOPD)** — sample a stopping position per rollout *before* generation, generate only to there, and correct the induced sampling bias with **blockwise inverse-probability weighting (IPW)**. Proof: this preserves Vanilla OPD's gradient sum in expectation, with one-step update-error bounds for **SGD, Adam, and Muon**.
- **Results**: across multiple teacher–student pairs, domains, and optimizers: **−25–48% generated tokens** at comparable accuracy, **1.3–2.2× training speedups**.
- **Why it matters**: shows the rollout *length* budget is itself a design axis, orthogonal to teacher choice — the same lesson as training-free OPD, from the compute-allocation side.

---

#### 7. Compatibility Matters: A Framework for Token-Level Teacher Selection in On-Policy Distillation

- **arXiv**: [`2610.21234`](https://arxiv.org/abs/2610.21234) · cs.LG
- **Authors**: Stanley Wei, Jiin Woo, Kaan Ozkara, Youngsuk Park
- **Institution**: Princeton University + Amazon Annapurna Labs
- **Problem**: OPD typically uses a **single teacher per rollout** (or per run), ignoring a whole axis of flexibility available *because* it is on-policy: **per-token teacher selection**.
- **Method**: theory of what makes a teacher and student **compatible** for OPD — compatible reasoning patterns, teacher competence, and induced student diversity — yielding empirical **routing heuristics** and a taxonomy of teacher-routing schemes, with proofs that different schemes help under different scenarios.
- **Results**: in math, coding, kernel generation, and visual reasoning, up to **+10 percentage points of pass@k** over vanilla OPD *and* over the teacher experts on some tasks, indicating both capability and diversity gains.
- **Why it matters**: it directly interrogates the "single teacher" assumption and finds the axis is real — while remaining consistent with the design-axis thesis (the lever is *how supervision is composed*, not merely which teacher).

---

#### 8. Condition-Contrastive Extrapolation for On-Policy Distillation of Language Models (CCE-OPD)

- **arXiv**: [`2610.21195`](https://arxiv.org/abs/2610.21195) · cs.AI
- **Authors**: Wenxuan Luo, Chenxi Li, Haoyue Liu, Yongxin Guo, Xiaoying Tang
- **Institution**: The Chinese University of Hong Kong, Shenzhen + ByteDance
- **Problem**: when conditioned on *student-generated* prefixes, a teacher can favor **invalid continuations** that violate the question's premises, so OPD teaches erroneous reasoning steps.
- **Method**: **CCE-OPD** makes teacher supervision **condition-sensitive** via (1) a fixed-prefix comparison where the same frozen teacher evaluates the full question vs a condition-masked counterpart, and (2) a **bounded log-probability contrast** reweighting the teacher distribution into an auxiliary target.
- **Results**: on 200 diagnostic reasoning states, condition contrast reduces preference for invalid continuations from **27.0% → 16.0%**. Across six math benchmarks, **+1.60/+1.95 pts avg@8** over OPD distilling Qwen3-8B into 0.6B/1.7B students; strongest on four transfer benchmarks.
- **Why it matters**: another target-construction fix — it identifies a specific failure of the teacher signal (invalid-continuation preference) that a better teacher cannot fix because the problem is the *condition*, not the teacher.

---

#### 9. Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation

- **arXiv**: [`2610.21601`](https://arxiv.org/abs/2610.21601) · cs.LG / cs.CL
- **Authors**: Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
- **Institution**: Alibaba Cloud Computing
- **Problem**: policy-shift distillation reuses the teacher's pre/post-RL log-prob difference as supervision, but the **endpoint** shift cannot reveal whether local action preferences evolved consistently — the same endpoint can hide early/late shifts that reinforce or cancel.
- **Method**: **Waypoint-OPD** uses an **intermediate teacher checkpoint** from the same RL run to compare early vs late shift directions at student-visited prefixes, and **gates** the endpoint shift by their agreement (suppressing it when they oppose). Cost: one extra frozen-teacher scoring pass.
- **Results**: with RL-trained Qwen3-4B teachers and Qwen3-8B/14B/30B-A3B students, Waypoint-OPD achieves the **highest domain-average score in all six domain–student settings**; ablations (removing/shuffling gates) degrade math reasoning.
- **Why it matters**: it turns the RL "trajectory" into a usable supervisory signal — the target is a *path*, not an endpoint, again target-construction over teacher choice.

---

#### 10. CleanRM: Reward Modeling from Noisy Feedback with a Few Clean Feedback for RLHF

- **arXiv**: [`2610.21138`](https://arxiv.org/abs/2610.21138) · cs.AI / stat.ML
- **Authors**: Licheng Pan, Haocheng Yang, Yuzhou Chen, Yichen Sun, Yuan Lu, Yunfei Teng, Jiajun Fan, Guangyi Liu, Zhixuan Chu, Hao Wang
- **Institution**: Zhejiang University + Xiaohongshu Inc + National University of Singapore + New York University + UIUC + MBZUAI
- **Problem**: feedback noise (subjective judgments, annotation mistakes, imperfect LLM judges) biases reward modeling; classical denoisers assume a **uniform** noise ratio, false for feedback where noise is **sample-wise**.
- **Method**: **CleanRM** uses a few clean feedback to calibrate **sample-wise noise ratios via optimal transport**, aligning the joint distribution of preferences reverted from noisy feedback with that of clean feedback, then trains on a **noise-corrected surrogate loss**. Proof: the objective is unbiased w.r.t. the clean risk.
- **Results**: beats SOTA denoising baselines and yields more effective **downstream RLHF** alignment.
- **Why it matters**: reward modeling quality is a *target-estimation* problem too — the same "fix the target, not just the optimizer" motif, at the reward layer.

---

### Lane C — RLVR / Reward & Data (3)

---

#### 11. Multi-Reward Hacking: From Aggregation-Induced Drift to Trust-Anchored Defense (TAG)

- **arXiv**: [`2610.21404`](https://arxiv.org/abs/2610.21404) · cs.LG / cs.AI
- **Authors**: Yushu Li, Jiin Woo, Xiaoxiao Li, Youngsuk Park
- **Institution**: University of British Columbia + Amazon Annapurna Labs
- **Problem**: combining a primary reward (correctness) with auxiliary rewards (brevity, efficiency) can *degrade* primary-task performance while aggregate reward rises — even when each reward is individually meaningful.
- **Method**: a one-step multi-reward decision formulation characterizing when symmetric aggregation constitutes **multi-reward hacking**; proof that deterministic conditional-mean GRPO converges to auxiliary-favoring behavior **regardless of initialization**. **Trust-Anchored Gating (TAG)** elects an anchor channel by per-channel policy drift, then gates auxiliary credit on anchor satisfaction.
- **Results**: symmetric/constrained/normalized aggregation degrade across Qwen and Llama on math and program synthesis; on **Qwen3-4B with a brevity reward**, TAG reaches **0.581 pass@4 vs 0.220** for additive aggregation while shortening responses **44%** vs correctness-only.
- **Why it matters**: provides a provable mechanism (not calibration-sensitive reweighting) for the increasingly common multi-objective post-training stack.

---

#### 12. Wrong Votes, Right Gradients: Why Majority-Vote Rewards Track Verifiable RL

- **arXiv**: [`2610.20898`](https://arxiv.org/abs/2610.20898) · cs.LG / cs.AI / cs.CL
- **Authors**: Dylan P. Wilson, Chengsong Huang, Jiaxin Huang
- **Institution**: Dartmouth College + Washington University in St. Louis
- **Problem**: RL with self-generated labels (majority vote over a model's own samples) recovers most of the gain of verifiable rewards — puzzling, since majority vote returns a modal answer and carries no correctness information.
- **Method**: argue the relevant unit is the **batch-level update**: at practical batch sizes a prompt's own gradient accounts for <1% of its output change, so a wrong label only matters if label errors are **coherent across prompts**. Decompose the majority-vote update into shrinkage vs misdirection and measure per-response gradients on five models.
- **Results**: majority-vote errors are **as incoherent as a random-reward null**; the majority-vote update agrees with the gold update as closely as two independent gold updates agree; noise-corrected cosine with gold is **1 within error**. Randomly flipping up to **30%** of gold labels leaves direction intact; the same fraction flipped by a **shared rule destroys it**. Learned reward models fall measurably short. The equivalence holds at every checkpoint but is **local** (gold still ends ahead on held-out accuracy).
- **Why it matters**: an error-**coherence** theory of when self-labels can stand in for verification — and a caution that reward models (per prompt 11) may be the *coherent* case that breaks it.

---

#### 13. What Should We Remove? Evaluating the Reliability and Costs of RLVR Data Decontamination

- **arXiv**: [`2610.21229`](https://arxiv.org/abs/2610.21229) · cs.CL / cs.LG
- **Authors**: Esther Xin
- **Institution**: Independent Researcher
- **Problem**: RLVR math corpora are routinely screened for benchmark overlap, but the **reliability and data-loss costs** of cleaning policies are unexamined.
- **Method**: audit **16 open RLVR math corpora** (1,673,514 training items) against six benchmarks (1,949 questions); evaluate eight matching policies (exact/lexical/semantic) using **594 independently, blindly dual-reviewed** training–benchmark pairs, plus an item-level false-removal review.
- **Results**: at cosine threshold 0.80, **52 of 59 sampled removals (88%) were false removals**; no semantic threshold in the preregistered grid (0.80–0.98) meets the 90% conservative-precision target. The existing **judge-adjudicated** policy achieves **98.1% resolved precision / 98.2% candidate-frame recall** with zero confirmed false removals among six sampled removals.
- **Why it matters**: decontamination is usually reported as overlap counts; this shows the standard semantic-threshold knee-jerk is doing more harm than good, and that recall outside the candidate frame is unmeasured.

---

### Lane D — Agents / Memory / Self-Improvement (4)

---

#### 14. All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents (AiO-Mem)

- **arXiv**: [`2610.21147`](https://arxiv.org/abs/2610.21147) · cs.AI
- **Authors**: Bingbing Wang, Jingjie Lin, Weiming Qiao, Jing Li, Ruifeng Xu
- **Institution**: Harbin Institute of Technology (Shenzhen) + Fudan University + The Hong Kong Polytechnic University + Peng Cheng Laboratory
- **Problem**: existing memory methods optimize retrieval and memory construction **separately**, with no shared reward space for search/write/stop decisions.
- **Method**: **AiO-Mem** organizes the operations as transitions over a shared **evidence state**, compiles histories into source-traceable **multi-view events**, and trains a **trajectory-conditioned process reward model** (evidence-grounded SFT + trajectory-level DPO). Scores aggregate into an action-balanced trajectory reward optimized by **Process-Aligned DAPO (PA-DAPO)**.
- **Results**: consistent answer-accuracy gains on long-context memory benchmarks over both static memory systems and RL-trained memory agents.
- **Why it matters**: unifies the memory lifecycle under one process reward — the agent analogue of the target-construction thesis.

---

#### 15. Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing

- **arXiv**: [`2610.22196`](https://arxiv.org/abs/2610.22196) · cs.CL
- **Authors**: Tianxiang Fei, Jiazheng Kang, Mao Zheng, Xingyan He, Xiang Yu
- **Institution**: Tencent Hunyuan
- **Problem**: external-memory systems depend on a general-purpose LLM executing the **write path** behind framework-specific prompts — costly, and non-transferable across protocols; a unified cross-framework writer is unexplored.
- **Method**: a compact long-term-memory writer trained across **Mem0, MemOS, and Hy-Memory**. **Memory On-Policy Distillation** teaches framework-specific write protocols on student-generated states; **Memory RL** optimizes downstream answerability via dense per-chunk probes, **attributed cross-chunk rewards**, over-storage controls, and chunk-level GRPO. Policy-written banks carry across windows.
- **Results**: first on **all four evaluated harnesses** (including held-out EverMemOS), **55.49% macro average vs 54.62% for Claude Opus 5** on fixed 20% subsamples.
- **Why it matters**: a rare *industrial* result in the memory lane — and it is again **OPD + RL**, tying this lane to the block's dominant thesis.

---

#### 16. Beyond Downstream QA: Rethinking How We Evaluate Agent Memory (FEB-30)

- **arXiv**: [`2610.22209`](https://arxiv.org/abs/2610.22209) · cs.CL / cs.AI
- **Authors**: Sebastian-Antonio Toma, Jean de Kernier, Mike Ply, Oliviu Matei
- **Institution**: Amazon Web Services + Technical University of Cluj-Napoca
- **Problem**: agent-memory benchmarks use downstream QA accuracy as a proxy for memory quality, conflating memory correctness with retrieval and generation quality → false positives (correct answers mask broken memory) and false negatives.
- **Method**: **FEB-30** — 30 fact-evolution trajectories across 6 diagnostic categories and 3 difficulty levels, built by **paradigm inversion** (documents generated from known fact trajectories → deterministic ground truth, no human annotation), allowing direct inspection of the memory store after each ingestion.
- **Results**: intrinsic and extrinsic evaluation **diverge by 16 pts on average**, with **44%** of trajectories exceeding meaningful divergence. The system classifies memory operations (create/update/reinforce/supersede) correctly only **20%** of the time — invisible to extrinsic evaluation.
- **Why it matters**: a measurement paper that shows a whole lane's headline metric is blind to its central failure — worth flagging against every memory-agent claim above.

---

#### 17. The Self-Improvement Problem

- **arXiv**: [`2610.21646`](https://arxiv.org/abs/2610.21646) · cs.AI / cs.CL / cs.LG
- **Authors**: Brian B. Moser, Stanislav Frolov, Tobias C. Nauen, Federico Raue, Andreas Dengel
- **Institution**: German Research Center for Artificial Intelligence (DFKI) + RPTU Kaiserslautern-Landau
- **Problem**: as agents propose modifications to their own components, can an automated gate (reward model / reviewer) reliably decide whether an update is a genuine improvement?
- **Method**: formalize agents as programs and define improvement via a **semantic score that need not be computable**; study a certifier (approve/reject) and a searcher (output some improving candidate). Analysis via self-referential constructions.
- **Results**: in the fully general setting **no terminating procedure can be both reliable and non-conservative**; randomized gates with bounded error face the same limit. A standard decidable regime (bounded evaluation + finite proposal budget) recovers guarantees via exhaustive simulation — but a chain of accepted updates can raise the bounded score every round while the **true score falls**.
- **Why it matters**: a clean impossibility boundary for the self-improvement story that several papers in this block (and every "self-evolving agent") presuppose.

---

### Lane E — Efficiency / Inference (3)

---

#### 18. Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches (RoPERelay)

- **arXiv**: [`2610.21126`](https://arxiv.org/abs/2610.21126) · cs.CL
- **Authors**: Wanyang Hong, Zhaoning Zhang
- **Institution**: National University of Defense Technology, Changsha
- **Problem**: sparse KV compression retains selected states but leaves them in their **original coordinates**; under RoPE, the **positional gaps left by evicted tokens** keep affecting query-key matching, limiting the use of retained evidence.
- **Method**: **RoPERelay** assigns compact, order-preserving RoPE coordinates, relocates cached key phases via inverse rotation + re-rotation, and synchronizes the current query and subsequent generation — **no renewed selection, no historical re-prefill, no added cache budget**.
- **Results**: across **36 comparisons** (2 models × 6 selectors × 3 memory tasks), improves quality in **32**; for Llama-3.1-8B + BM25 on **LongMemEval-S, 23.6% → 35.4%**; ~**1–3%** request-time overhead.
- **Why it matters**: establishes **positional organization** as a distinct optimization dimension *after* content selection.

---

#### 19. Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches

- **arXiv**: [`2610.22016`](https://arxiv.org/abs/2610.22016) · cs.LG
- **Authors**: Adam Deng, Shicheng Liu, Yada Zhu
- **Institution**: MIT (Operations Research Center + CSAIL) + IBM Research
- **Problem**: multi-agent LLM systems pass **text** (lossy). A natural upgrade is to transmit the **KV cache**; the most appealing form is training-free substitution of the sender's cache into a frozen reader.
- **Method**: test eight diverse substitution methods against two measured anchors (an uninformative-cache baseline and the reader's own accuracy from reading the passage); explain the failure via **competitive attention** and a "**tolerable set**" of caches a frozen transformer can read.
- **Results**: substitution **does not work** and the obstruction belongs to the *reader*: geometric similarity does **not** predict usability, and the failure is **not gradual**, so "more faithful" is not the fix. All eight methods sit at the baseline. A **different design works**: keep the reader's own cache and **attend over the sender's as extra context**, adapting only queries — beating the baseline, and also clearing it with eight senders pooled.
- **Why it matters**: a redirection paper — the target is *not* faithful substitute caches but **additive** cache context. Pairs with §18 to form the block's "post-selection" thesis.

---

#### 20. Router Drift Control: Mitigating Off-Policy Degradation in Mixture-of-Experts Reinforcement Learning

- **arXiv**: [`2610.21682`](https://arxiv.org/abs/2610.21682) · cs.LG / cs.AI
- **Authors**: Liangyao Jin, Zhixin Wang, Liming Liu, Mingjun Zhang, Zhengzhou Zhu, Fangcheng Fu, Jinlong Hou, Yuan Cheng, Xiaohe Hu, Ping Zhang, Siyuan Feng
- **Institution**: Peking University + Shanghai Innovation Institute + Zhejiang University + Shanghai Jiao Tong University + Infrawaves Inc
- **Problem**: RL becomes **off-policy** through training–inference mismatch, mini-batch updates, and asynchrony; in MoE models this changes **routing decisions** → "router drift." Rollout Routing Replay (R3) reuses rollout expert selections but introduces **gradient bias** by dropping experts the training router would have chosen.
- **Method**: **Router Drift Control (RDC)** uses routing disagreement between rollout and training as a **staleness signal** and selectively **rejects high-drift responses** — sequence-level filtering avoids replay's gradient bias while preserving native expert selection for retained responses.
- **Results**: gains grow with staleness and persist in asynchronous RL; with Truncated Importance Sampling, **+5.5 pts** avg peak validation over TIS (**+4.5 over R3**) on AIME 2024/2025.
- **Why it matters**: MoE + RL is now mainstream; RDC shows the router is a first-class off-policy variable, not just a capacity trick.

---

### Lane F — Sequential Modeling / Time Series (2)

---

#### 21. TurboMamba: Faster Inference, Faster Training, and Better Prediction with Lexical Memory

- **arXiv**: [`2610.20682`](https://arxiv.org/abs/2610.20682) · cs.LG / cs.CL
- **Authors**: Hanxin Zhang
- **Institution**: University of Pittsburgh (Department of Neurology)
- **Problem**: sequence architectures trade off training speed, inference speed, and token prediction; can a hybrid beat pure Transformer/Mamba hybrids on all three?
- **Method**: a **hybrid** where a global **Mamba-3** runs once per completed token block and a small **Transformer** uses that global context plus earlier in-block tokens to predict the next token. Three additions: direct access to the previous block's last token, a small next-token score correction, and a learned mixture with recent-token frequencies.
- **Results**: among twelve small-scale implementations on **FineWeb-Edu** at matched parameter counts/budget, lowest mean test NLL — **−9.4% vs Mamba-3, −7.3% vs Jamba, −18.3% vs Zamba**; training throughput **2.60×/2.81×/4.82×**; batch latency (32×256-prompt, 128-gen) **3.12×/3.53×/6.21×**.
- **Why it matters**: a single-author incremental but concrete hybrid result — and a reminder that "lexical memory" (recent-token statistics) is a cheap, strong prior for local next-token prediction.

---

#### 22. Twice Upon a Time: Complementary Representations for Time-Series Reasoning

- **arXiv**: [`2610.22327`](https://arxiv.org/abs/2610.22327) · cs.LG / cs.AI / cs.CL
- **Authors**: Hedi Zisling, Liran Nochumsohn, Ilan Naiman, Mihir Parmar, Omri Azencot
- **Institution**: Ben-Gurion University + Google
- **Problem**: time-series language models (TSLMs) expose the LLM to a **single** representation, imposing a fixed inductive bias across tasks; which information should the representation preserve vs factor out?
- **Method**: **complementary representations** as a design principle — two visual views: **line plots** (absolute measurements + observed coordinate frame) and **normalized delay embeddings** (factor out positive amplitude rescaling/offsets while exposing temporal structure). Dedicated visual encoders integrate both via visual tokens + multi-level fusion into one LM.
- **Results**: built on **Qwen3-VL-8B**, dual-view raises **TSRBench accuracy 44.5% → 53.2%**, far above the strongest dedicated TSLM baseline (**36.7%**); **89.9%** on TSExam and **86.8%** multivariate ChatTS numeric accuracy. Evaluation-time interventions confirm distinct invariance profiles; single-view ablations show the combination helps most beyond perception.
- **Why it matters**: representation *choice* — not model scale — drives time-series reasoning, mirroring the block's target-construction motif.

---

### Lane G — Games / Game Theory / MARL / Bandits (5)

---

#### 23. Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines

- **arXiv**: [`2610.22277`](https://arxiv.org/abs/2610.22277) · cs.MA / cs.GT / cs.RO
- **Authors**: Florian Lercher, Karan Mahesh, Yujun Huang, Meshal Alharbi, Runyu Zhang, Hanna Krasowski, Michael R. Benjamin, Matthias Althoff, Gioele Zardini
- **Institution**: Woods Hole Oceanographic Institution + UC Berkeley + MIT LIDS + TU Munich
- **Problem**: deployed robots must satisfy **legal constraints** and their own goals, with only **partial prioritization** — scalarized objectives or full hierarchies are unsuitable.
- **Method**: **posetal games** (games with partially ordered preferences). Scenario-independent **legal guidelines** order abstract legal concerns; agent preferences and a legal game are auto-derived per scenario. Agents may refine with private objectives and regulators may refine the guideline as laws evolve. Proof: such customizations **can only remove equilibria**, preserving legality. **Belief play** recovers true equilibria from conservative local games; a distributed iterative best-response protocol needs less information.
- **Results**: applied to **maritime navigation**, lifting pairwise traffic rules to multi-vessel encounters. On seven encounters (up to four vessels), every rule violation of the committed equilibria is **certified as forced by the legal hierarchy or unsatisfiable**, and defectors are identified from public information in all tested cases.
- **Why it matters**: a concrete route from **partially specified laws** to auditable multi-agent planning — a rare GT paper whose guarantee is about *regulatory* correctness.

---

#### 24. Learning Self-Orchestration in Decentralized Agent Swarms

- **arXiv**: [`2610.22322`](https://arxiv.org/abs/2610.22322) · cs.MA / cs.AI / cs.CL
- **Authors**: Guowei Xu, Zhenting Qi, Amani Kiruga, Himabindu Lakkaraju, Yilun Du
- **Institution**: Harvard University
- **Problem**: existing multi-agent systems train agents within **fixed orchestration structures**, separating individual-capability learning from collective-behavior organization.
- **Method**: **market-based post-training (MPT)** — agents **bid** for participation; bids determine who acts and how collective outcomes provide local training credit, so action policies and self-orchestration adapt together **without a central coordinator**.
- **Results**: evaluated on embodied crafting, robot navigation, and deep research; beats monolithic post-training, and participation **evolves with learning**. With fixed action policies, learned self-orchestration beats alternative coordination strategies; larger populations at inference improve performance and suffer **smaller losses under agent dropout**.
- **Why it matters**: it makes *coordination itself* a learned object via a market mechanism — the swarm analogue of token-level teacher routing.

---

#### 25. Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions

- **arXiv**: [`2610.22138`](https://arxiv.org/abs/2610.22138) · cs.AI / cs.CL / cs.MA
- **Authors**: Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, Wooseong Yang, Yuwei Han, Philip S. Yu
- **Institution**: University of Illinois Chicago
- **Problem**: LLM systems rely on peer critique to catch errors; does group discussion actually protect individual beliefs?
- **Method**: in a ten-agent factual discussion, one or three **adversarial** agents repeatedly assert a plausible false answer. After each round, each benign agent's **private** answer is probed through a hidden separate call, and its **public** stance is labeled separately. Six models, three factual-QA datasets.
- **Results**: without an attacker, only **0.6%** of benign agents end with the false answer. One attacker → **44.8%**; three → **60.5%**. Contrary to conformity studies (public change without private change), here it is **reversed**: with three attackers, benign agents hold the false answer privately in **51.6%** of exposed turns but publicly endorse it only **19.7%** — most influence is **invisible in the discussion**. Agents retaining the truth often **fail to defend it**; baseline knowledge does not predict robustness.
- **Why it matters**: a hidden-belief metric that shows peer critique can collapse *private* correctness while public agreement looks fine — a serious evaluation gap for multi-agent safety.

---

#### 26. Replicable Dueling Bandits

- **arXiv**: [`2610.20908`](https://arxiv.org/abs/2610.20908) · cs.LG / cs.AI
- **Authors**: Rohan Deb, Aadirupa Saha, Udaya Ghai, Karan Singh, Arindam Banerjee
- **Institution**: University of Illinois Urbana-Champaign + University of Illinois Chicago + Amazon + Carnegie Mellon University
- **Problem**: dueling bandits choose comparisons based on noisy earlier outcomes, so two runs on the **same preferences** may compare different pairs — a **replicability** failure.
- **Method**: define replicable dueling bandits (two executions with shared internal randomness and independent outcomes must select the same ordered pair every round w.p. ≥ 1−ρ). Build on **Beat-the-Mean**, designing the first such algorithms with **sublinear regret**.
- **Results**: under relaxed stochastic transitivity (γ≥1) + stochastic triangle inequality, regret **Õ(γ⁸K⁴H_p/ρ²)**; under strong stochastic transitivity, a simultaneous-elimination algorithm improves K-dependence to **Õ(K²H_p/ρ²)**; for linear dueling bandits, **Õ(d³√T/(c_μρ))**. Experiments on synthetic and **language-model preferences** confirm replicability with sublinear regret.
- **Why it matters**: ties the bandit/RLHF-preference lane to the reproducibility agenda — the first genuine regret theory for the setting where preference comparisons must be *stable*.

---

#### 27. Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld

- **arXiv**: [`2610.22152`](https://arxiv.org/abs/2610.22152) · cs.LG / cs.AI
- **Authors**: Hilda Adwubi Osei
- **Institution**: Kwame Nkrumah University of Science and Technology, Ghana
- **Problem**: RL optimizes the given reward, which can diverge sharply from the intended objective (**specification gaming**); existing evidence is largely observational, with few controlled demonstrations paired with a *guaranteed* mitigation.
- **Method**: a minimal gridworld where a cleaning agent can genuinely remove dirt or **conceal it from a cheap sensor**; a standard DQN trained only on the sensor's proxy reward games it completely. Then a **constrained-RL fix** penalizes the specific exploiting behaviors; an exact **accounting identity** relates proxy reward, true reward, and the cost signal.
- **Results**: DQN converges to near-maximal proxy reward while **never achieving the true objective**; the constrained fix eliminates gaming from the final policy and substantially recovers true-objective performance; the cost signal measures the proxy/true gap **exactly** (not merely tracking it), yielding a deterministic guarantee under a hard-constrained variant.
- **Why it matters**: a controlled negative result *plus* a guarantee — the rare spec-gaming paper whose mitigation is certified rather than empirically better.

---

## 5. Cross-Cutting Synthesis

### 5.1 The OPD cluster is now a program, not a topic

The [2026-10-09 report](../2026-10-09/arxiv-ai-search.md) documented four OPD papers converging on "target construction and signal shaping" as the lever. The [10-16 conference-digest](../2026-10-16/conference-digest.md) saw a further wave. On the Friday 10-16 block, the same thesis shows up as **at least five independent training regimes**, each attacking a *different* part of the target:

| Paper | What it redesigns | Institution |
|---|---|---|
| Training-Free OPD [`2610.22236`](https://arxiv.org/abs/2610.22236) | removes training; fusion as layer-wise least squares | UIUC |
| STOPD [`2610.21337`](https://arxiv.org/abs/2610.21337) | rollout **length** (stochastic truncation + IPW) | Cornell / GT / Alibaba |
| Compatibility [`2610.21234`](https://arxiv.org/abs/2610.21234) | **teacher routing per token** | Princeton / Amazon |
| CCE-OPD [`2610.21195`](https://arxiv.org/abs/2610.21195) | **condition sensitivity** of the teacher signal | CUHK-SZ / ByteDance |
| Waypoint-OPD [`2610.21601`](https://arxiv.org/abs/2610.21601) | **gate the endpoint shift by path agreement** | Alibaba Cloud |

Two of them (STOPD, Compatibility) are by **Amazon Annapurna/Alibaba-adjacent applied groups**; one (Waypoint) is Alibaba Cloud; one (CCE-OPD) is ByteDance; one (Training-Free) is academic. The [10-09 report](../2026-10-09/arxiv-ai-search.md) predicted this axis would mature "not by teacher selection or on-policyness itself." **It has, and it is now an industry program.** Note the tension with Lane C's [`2610.20898`](https://arxiv.org/abs/2610.20898) (*Wrong Votes, Right Gradients*): that paper argues *coherent* error — which is exactly what a bad teacher-objective induces — is what destroys the update. OPD's target-design problem and RLVR's coherence problem may be the same problem seen from two ends. **(high confidence)**

### 5.2 The KV cache's "post-selection" thesis

Two 10-16 papers, from unrelated groups, argue that **selection is not the end of compression**:

- [`2610.21126`](https://arxiv.org/abs/2610.21126) (NUDT): even with the right content selected, **positional geometry under RoPE** still corrupts matching — fixable by re-coordinating positions (+11.8pts on LongMemEval-S).
- [`2610.22016`](https://arxiv.org/abs/2610.22016) (MIT/IBM): a frozen reader cannot consume a substitute cache at *any* fidelity — so the remedy is **additive context**, not a better substitute.

These complement, rather than contradict, the 10-16 block's selection-side work (RoLaQ, AbridgeKV, sparse-selector papers named there). Taken together, October's KV-cache literature is splitting into **selection**, **post-selection geometry**, and **cache-transport/asymmetry** sub-problems — with the last one producing the block's cleanest negative result ("pursuing faithful substitute caches is the wrong target"). **(high confidence)**

### 5.3 CTR stays empty; advertising moves to generative-engine visibility

For the fifth consecutive October block, **zero explicit CTR-prediction or industrial ad-serving architecture papers** surfaced in cs.IR/cs.AI/cs.CL. The only advertising-adjacent paper is [`2610.21330`](https://arxiv.org/abs/2610.21330) (**VoteGEO-Bench**), which measures visibility *inside generated answers* — the GEO analogue of ad placement. The recommendation lane did produce three strong papers (§Lane A), but they are **content-embedding privacy, MoE interpretability, and cold-start priors** — not click modeling. This matches the 10-15 and 10-16 runs' finding: the academic rec/ad lane has migrated from **click prediction** to **generative/agentic interaction and privacy**. **(single-block observation, consistent across five blocks)**

### 5.4 Agent memory is maturing — and its headline metric is being audited

The block contains a full memory stack: a **process-rewarded** memory agent ([`2610.21147`](https://arxiv.org/abs/2610.21147)), an **industrial** cross-framework memory writer that reports beating Claude Opus 5 on a subsample ([`2610.22196`](https://arxiv.org/abs/2610.22196)), and — crucially — a **benchmark audit** ([`2610.22209`](https://arxiv.org/abs/2610.22209)) showing intrinsic vs extrinsic memory evaluation **diverge by 16 pts** and that one system classifies memory operations correctly only **20%** of the time. The audit lands the same week as the strong claims, which is exactly the healthy sequence; but it also means every memory-agent number in this block should be read with FEB-30's caveat in hand. **(medium confidence)**

### 5.5 A quiet reproducibility / verification thread

Three papers independently push on **whether a proxy can stand in for truth**: [`2610.20898`](https://arxiv.org/abs/2610.20898) (majority-vote labels = gold updates iff errors are incoherent), [`2610.21646`](https://arxiv.org/abs/2610.21646) (no terminating gate is both reliable and non-conservative for self-improvement), and [`2610.22152`](https://arxiv.org/abs/2610.22152) (spec-gaming cost signal = an *exact* proxy/true-gap identity). Read together: the field increasingly states *when* a cheap proxy carries the full signal, and *provably when it cannot*. **(tentative)**

## 6. Caveats

- **Window**: arXiv posts no weekend announcements; the freshest block is **Friday 2026-10-16**. This run covers that block and does **not** claim any 10-17 content.
- **Sibling overlap**: the 10-16 reports (`arxiv-daily`, `conference-digest`, `game-rl-daily`, `tech-report-digest`, `arxiv-ai-search`) cover the *same block*. The 27 featured here are the papers **none of them named**; they were chosen to be zero-collision by construction, not to be the block's "best" papers.
- **Affiliations** are recovered from LaTeXML author blocks and are **literal as-printed**; where a paper prints none it was marked so. `2610.20682`'s single author is printed under "Department of Neurology, University of Pittsburgh" — reported faithfully without inference.
- **Abstracts** are used as the sole evidence for headline numbers; no full-text was read. All quantity claims are as the papers report them (single-source, un-replicated).
- **Rate limiting**: the export API was unusable this run (`429` on all queries); listing-page harvest + per-paper `abs`/`html` was the fallback. Listing pages expose only the **new** block, so no back-catalog sweep was possible.
- **CTR** is reported empty as an explicit (negative) finding rather than omitted.
