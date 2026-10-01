---
title: "arXiv Paper Check — AI & CTR (October 1, 2026)"
type: synthesis
created: 2026-10-01
updated: 2026-10-01
sources: []
tags: [arxiv, daily-check, ai, ctr, click-through-rate, advertising, auction, mechanism-design, benchmark-validity, evaluation-audit, uncertainty, calibration, measurable-measurement, experimentation, always-on, sequential-testing, e-values, subgroup-discovery, causal-inference, proximal-balancing, label-noise, fairness-audit, agent-safety, activation-steering, skill-supply-chain, skill-poisoning, causal-verification, trust, rag, retrieval, hallucination-gating, auto-research, harness, muon, policy-iteration, no-arbitrage, daily-digest]
---

# arXiv Paper Check — AI & CTR (October 1, 2026)

**Window note — this is the Thu 1 Oct 2026 announcement, and it is the same window covered by today's sibling [[arxiv-daily]].** Category-agnostic `submittedDate:[202609291800 TO 202610011000]` sweep at 200/page retrieved all **2,065** entries (`totalResults` = 2,065, no truncation), **IDs 2609.38299–2609.40363**, published 09-29T18:00Z → 09-30T17:59Z. Primary spread: cs.LG 253 / quant-ph 217 / cs.CV 188 / cs.AI 126 / cs.RO 121 / cs.CL 102 / cs.CR 39 / **cs.IR 16** / cs.GT 34-cs.IR-tail. **Dedup**: against the pre-existing wiki (**7,297** unique arXiv IDs before 2026-10-01), **none of the window's 2,065 entries appear — every paper here is new to the wiki**. Today's siblings [[arxiv-daily]] and [[arxiv-ai-search]] then independently claimed **~135** of the same window; screening here predates the siblings' final claim set, so **6 of this issue's IDs overlap them** (see Method Note).

**Division of labour with today's siblings (important for reading this issue).** The [[arxiv-daily|10-01 arxiv-daily]] already ran on this exact window and cited ~134 papers, comprehensively covering the **recommendation / advertising / auction / auto-research / agent-harness** clusters (GEAR Douyin ad retrieval, the Kuaishou OneRec challenge, LLM user-profile routing gates, RankEvolve, the Google autobidding pair, Inference Auctions, etc.). Rather than duplicate that, this **paper-check** applies its own screen — **CTR/ads-direct, measurement validity, experimentation, and the trust/safety surface** — over the remaining ~1,930 sibling-unclaimed entries and cross-references the sibling's findings where they touch. **Every featured ID below is absent from the pre-sibling wiki**; **31 of the 36 featured papers are also not covered by today's siblings, and 5 are independently reached here** (2609.38473, 2609.38807, 2609.39097, 2609.40115, 2609.40330), retained for their angle rather than claimed as this issue's discovery.

**CTR status: the direct-category drought now runs to two consecutive windows.** A CTR/ads regex over the full 2,065-entry window returns **six papers, every one already claimed by [[arxiv-daily]] and none of them a CTR-*prediction* architecture paper** (2609.38698 / 2609.40267 / 2609.39887 / 2609.40070 auctions, 2609.39327 ads retrieval). There is **no new CTR-model paper in this window** — consistent with the standing absence the sibling flags. The unclaimed pool's nearest neighbours are mechanism design (① below), not CTR modelling.

---

## ① CTR, Ads & the Auction Layer (2)

The CTR-prediction drought continues; the only unclaimed papers adjacent to the ads economic layer are pure mechanism design.

### Mechanism Design for Bridge Location with Optional Preferences
- **Authors**: Xiaoshuang Geng, Wenjing Liu, Genjie Qin, Qizhi Fang
- **arXiv**: [2609.39097](https://arxiv.org/abs/2609.39097) — cs.GT
- **Key contribution**: Two separated regions each hold one pre-located facility; each agent has a private location **and a private preference for a nonempty subset of the two facilities**. Individual cost is the **max / sum / min** of distances to the facilities the agent cares about. The planner designs **deterministic strategyproof** mechanisms that elicit truthful reports and approximately minimise social cost or maximum cost. For social cost: optimal mechanisms for the max- and sum-variants, a **3-approximation** for min-variant with a **lower bound of 2**. For maximum cost: **5/3-approximations** for max/sum and a 3-approximation for min, with a **common 5/3 lower bound** across all three variants.
- **Why it matters**: A clean matched upper/lower-bound facility-location result with a genuinely new twist — **optional, private preferences over which facilities an agent must be served by**. That "opt-in service set" structure is closer to real ad-slot / fulfilment-network placement than the classical single-facility median game, and the 5/3 common bound is the quotable part.

### L2R-EV: Learning What to Repair in Electric Ride-Pooling with Finite Charger Queues
- **Authors**: Mai Pham, Vikrant S. Vaze, Peter Chin
- **arXiv**: [2609.40225](https://arxiv.org/abs/2609.40225) — cs.GT
- **Key contribution**: Ride-pooling optimisation is usually split into **matching** and **charging** and solved separately, but shared electric fleets face them jointly: a vehicle's next-match quality depends on where/when it charges, and charge queues depend on how the fleet is matched. **L2R-EV** learns *which subproblem to repair* rather than optimising a monolithic objective, using a learning-to-rank controller over candidate repair actions. Reported as improving pooled service under finite charger queues relative to decoupled baselines.
- **Why it matters**: The **"learn what to repair" controller** is the transferable idea and the same structural move the ads-serving world is making — decompose, then learn the *scheduling* of the optimiser rather than the objective. Adjacent to the auction cluster (claimed by [[arxiv-daily]]) as a market-design-with-physical-constraints result.

---

## ② Measurement Validity & Evaluation Audits (12)

The window's strongest unclaimed signal. Six of these are **audits that overturn a default methodological assumption**, and three of them build the missing control cell rather than merely flagging a confound.

### Routing Probes Can Improve Without New Information: An Exact-Null Audit of Uncertainty Beyond Model Outputs
- **Authors**: Wenhao Liang, Lin Yue, Wei Emma Zhang, Mingyu Guo, Olaf Maennel, Weitong Chen
- **arXiv**: [2609.38956](https://arxiv.org/abs/2609.38956) — cs.AI
- **Key contribution**: Vision-transformer **routing signals** (expert gates, attention-residual weights, halting scores) are widely reported to improve correctness probes, and the gain is read as evidence that routing carries error information *beyond* the outputs. The authors construct an **exact label null**: keeping real output-routing pairs, they redraw correctness labels from a frozen output-only generator fitted on disjoint data, so routing is uninformative **by construction**. Under this null, a width-matched MLP still reports a routing gain in **51.3% (308/600)** of confidence-only evaluations, while a linear comparison reports none. Holding each training trajectory fixed and selecting the checkpoint by **validation log loss instead of validation accuracy** removes the detections (**50/120 → 0/120** and **83/120 → 0/120** in an independent implementation), identifying **accuracy-based checkpoint selection as the cause**. Across all output views the detection rate falls from **27.5% (528/1,920) to zero observed detections**. The repaired comparison is then not merely inert but *insensitive* (detecting a ~0.005-nat implanted signal in 0/20 replicates), whereas a conditional permutation test detects it in 11/20 and 10/20. On real labels, conditional analysis gives model-relative evidence in 5 DeiT families, 4 robust to two conditional-law variants.
- **Why it matters**: The cleanest falsification in the window of a specific published practice: **checkpoint selection by accuracy leaks the label into the probe comparison**. "Fitting a better probe and testing for incremental information are different problems" is the sentence to carry. Directly adjacent to the sibling's auto-research/harness line, where probe-based verifiers are routinely trusted.

### A Generalisation Signal Need Not Be a Model-Selection Signal
- **Authors**: Aditya Nagarsekar, M P Ashish Bhat, Aadi Nesarkar, Vrishti Godhwani, Rahul Yedida, Aditya Challa, Danda Sravan, Snehanshu Saha
- **arXiv**: [2609.39099](https://arxiv.org/abs/2609.39099) — cs.LG
- **Key contribution**: When validation data stops preserving which model is best under distribution shift, a popular fallback is to rank candidates by **intrinsic geometry** (Hessian norm/trace/top-eigenvalue, a forward-only curvature proxy). Across molecular-property, protein-fitness and drug-response tasks, the authors find the geometry signal **does correlate with the generalisation gap on most tasks even when Hessian trace and top-eigenvalue relationships are weak or reversed**, yet it **does not reliably identify the deployment-best model**. Augmenting validation helps some shifts and **significantly harms others**; low geometric scores can even favour collapsed predictors.
- **Why it matters**: The distinction the title makes — **a generalisation signal ≠ a model-selection signal** — is exactly the failure mode that would silently corrupt any "pick the best checkpoint by an intrinsic score" policy. A useful companion to 2609.38956: two independent papers this window showing that the statistic people use to *choose* their model carries less decision information than they assume.

### Right Answer, Wrong Mechanism: Detecting Pernicious Divergence in Causal Interventions
- **Authors**: Beiming Liu, Minjie Chen
- **arXiv**: [2609.39243](https://arxiv.org/abs/2609.39243) — cs.LG
- **Key contribution**: Activation patching and DAS routinely **push representations off the natural distribution**, and prior work showed such divergence is sometimes harmless and sometimes *pernicious* — it recruits pathways the model never uses on natural inputs, producing the expected answer **through the wrong mechanism**. No method told the two apart. The authors make it testable by **planting hidden pathways** inside GPT-2 small that are silent on every benchmark prompt by construction, so which interventions depend on them is known exactly. Across **72 configurations / 100,800 interventions**: (i) nearest-neighbour and local-PCA distances **score below chance** (AUROC 0.35–0.47) at picking out pathway-dominated interventions; (ii) **Hidden-Pathway Contribution (HPC)**, a label-free clamp-to-natural-regime test, flags them at **AUROC ≥ 0.99** when the pathway shows unit-level out-of-regime activity — but fails when every unit stays in range (named as the open problem); (iii) optimised interventions **actively seek** hidden pathways — on a gender task **DAS routes 90–95% of successes through planted pathways** for 3 of 4 families, and an on-manifold penalty cuts that to <5% at a cost of 6–11 points of success.
- **Why it matters**: The mechanistic-interpretability community's most direct self-audit: **the standard divergence diagnostics are worse than random at detecting the failure they were introduced to guard against**, and successful interventions can be *reward-hacking the probe*. Sits alongside 2609.38956 and 2609.39099 as the window's trio of "your diagnostic statistic is not measuring what you think."

### Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations
- **Authors**: Maximilian von Klinski, Sebastian Lapuschkin, Wojciech Samek, Lennart Bürger
- **arXiv**: [2609.39807](https://arxiv.org/abs/2609.39807) — cs.CL
- **Key contribution**: Truth is persona-relative for an LLM. The authors build **8,916 human-reviewed, on-policy responses from three LLMs adopting anti-factual personas** (e.g. a conspiracy theorist), then evaluate **eight prior lie-detection probes**. Many **fail** — particularly when correct and incorrect answers are evaluated under the *same* persona prompt. Three novel confounder datasets where truth is **anti-correlated with a candidate concept** reveal that many probes **track concepts spuriously correlated with truth in their training data** (instruction compliance, response likelihood) rather than truth. A simple linear probe trained on decorrelated data achieves the strongest overall performance on both stress tests.
- **Why it matters**: Extends the wiki's recurring "probe reads the correlate, not the target" line to honesty detection, with the diagnosis that **training data decorrelation — not probe architecture — is the fix**. The persona-induced failure is the practical hazard for any deployment where the model is instructed to adopt a stance.

### FIGS: Evaluating Multi-Turn Sycophancy Without Penalizing Empathy
- **Authors**: Sidharth Pulipaka, Ruta Binkyte, Ivaxi Sheth, Sahar Abdelnabi
- **arXiv**: [2609.39863](https://arxiv.org/abs/2609.39863) — cs.AI
- **Key contribution**: Sycophancy rarely happens in one exchange; it **emerges as users repeatedly insist or subtly steer a dialogue**. Single-turn benchmarks miss this, and — the paper's sharpest point — **often mistake showing basic empathy for yielding**, penalising models for acknowledging a user's feeling, which may drive models to over-correct into cold rigidity. **FIGS (Factual Integrity and Grounded Support)** is a dual-axis framework over **extended 10-turn adaptive dialogues**, with a taxonomy that **strictly separates Sycophancy** (holding firm to the truth; keeping praise proportional) **from Calibrated Validation** (empathetic recognition without overdoing it). Releases 500 multi-turn scenarios and an automated judge. Leading models show a consistent trade-off: **either slowly drift to sycophancy or over-correct into robotic detachment**.
- **Why it matters**: The dual-axis split is the contribution — it makes "the model agreed" and "the model was kind" separately scoreable, which most sycophancy benchmarks conflate. This is the same discipline the 09-30 paper-check's sycophancy audit demanded (construct the missing cell), applied constructively.

### Unlearnable, or Unmeasured? On the Reliability of Difficulty Labels in RLVR
- **Authors**: Chandak Chakma, Syed Nazmus Sakib, Nafiul Haque, Shifat E. Arman
- **arXiv**: [2609.40115](https://arxiv.org/abs/2609.40115) — cs.AI
- **Key contribution**: Revisits the "some prompts are unlearnable under RLVR" phenomenon and finds the affected prompts **do improve, at roughly one third of the learnable rate**, while the **difficulty-defined set is far less reproducible than assumed** — difficulty labels are estimated from a limited number of sampled responses, and **combining them across seeds changes which prompts are selected** rather than simply reducing noise. A sampling-based framework quantifies the instability and the evaluation budget needed for assignments to reproduce. Revisiting the gradient-similarity evidence, **part of the observed separation arises because difficult prompts provide fewer correct rollouts** from which to estimate gradients; **matching the sample count weakens but does not remove the difference**.
- **Why it matters**: Careful two-sided reanalysis: it **preserves the slow-learning finding while invalidating the labels and part of the mechanism used to study it**. The "fewer correct rollouts → noisier gradient estimate" correction is a concrete measurement artifact that any GRPO/RLVR curriculum paper should control.

### How Reliable Are Predicted MOS for Reproducing Human System-Level Preferences in Speech Enhancement?
- **Authors**: Nahomi Kusunoki, Tsubasa Ochiai, Naohiro Tawara, Marc Delcroix, Naoyuki Kamo, Tetsuji Ogawa, Shoko Araki
- **arXiv**: [2609.39032](https://arxiv.org/abs/2609.39032) — cs.SD
- **Key contribution**: MOS-prediction models are assessed by **correlation with human MOS**, which **does not guarantee agreement on which system is better**. The paper introduces **system-level preference accuracy (SPA)** — does the predicted MOS rank systems the same way humans do? — and finds SPA varies hugely across predictors (**9.4% to 76.8%**); **even the best model disagrees with humans in ~23% of system comparisons**. Ensembling helps only marginally; domain adaptation helps substantially in closed conditions but only modestly in the practical open condition.
- **Why it matters**: The point generalises far past speech: **metric correlation and metric ranking-agreement are different properties**, and the field routinely reports the former when the decision requires the latter. Same group as 2609.39028.

### Improving Predicted MOS Scores, Not Perceived Quality: Multi-Predictor Test-Time Optimization of Enhanced Speech
- **Authors**: Tsubasa Ochiai, Marc Delcroix, Nahomi Kusunoki, Rintaro Ikeshita, Naohiro Tawara, Naoyuki Kamo, Tetsuji Ogawa, Shoko Araki
- **arXiv**: [2609.39028](https://arxiv.org/abs/2609.39028) — eess.AS
- **Key contribution**: First comprehensive study of **test-time optimisation directly against MOS predictors** on seven URGENT-2026 systems: (1) optimised predicted scores all rise while reference-based metrics stay flat; (2) a non-optimised predictor does not rise; (3) **a MUSHRA listening test shows no improvement in perceived quality**. Optimising the signal to raise predictor scores therefore **distorts evaluations** — comparison of SE systems can be biased regardless of actual quality.
- **Why it matters**: A clean, three-way Goodhart demonstration with the prescription stated plainly: **predictors used for optimisation must not be used for evaluation**, and challenge organisers should keep the ranking predictor undisclosed. Read with 2609.39032 as a matched pair — one shows the metric does not track the ranking, the other shows it can be gamed outright.

### Structural Limits of the Information-Theoretic Uncertainty Decomposition
- **Authors**: Jakob Lønborg Christensen, Christian F. Baumgartner, Morten Rieger Hannemose, Anders Bjorholm Dahl, Vedrana Andersen Dahl
- **arXiv**: [2609.39591](https://arxiv.org/abs/2609.39591) — cs.CV
- **Key contribution**: The standard aleatoric/epistemic (AU/EU) decomposition suffers **entanglement** and **epistemic collapse**. Analysing the framework functionally, the authors show **significant parts of the assumed AU/EU range are infeasible in finite settings** and cannot be attained by any class probabilities; the infeasible region is bounded by **AU ≤ log(2)/N** for N Monte-Carlo samples/ensemble members. This boundary **explains epistemic collapse**: at high confidence, **AU > EU is guaranteed by the structural limitation**, not by the data. Larger ensembles shrink the infeasible area; AU and EU are **coupled whenever AU ≤ log(2)/N** and should not be read as independent.
- **Why it matters**: A closed-form structural result under the entire AU/EU literature: some of what is reported as "model uncertainty" is **arithmetically unavailable**. The `log(2)/N` bound is the number to check before trusting any AU/EU split.

### Hard-Gate Candidacy in a Deployed Validator Suite
- **Authors**: Xin Xu
- **arXiv**: [2609.39037](https://arxiv.org/abs/2609.39037) — cs.LG
- **Key contribution**: Before a validator can gate a deployment pipeline it must be shown that its firing separates usable from broken outputs. Across **13 validators in a deployed generative agent** against 550 runtime + 350 static builds labelled by downstream outcome: **only two checks survive correction for multiple comparisons; nine are indistinguishable from zero, three because they never fired at all**. Execution is **not random with respect to the property being gated** — probes were **skipped on 144 of 895 broken builds vs 1 of 972 acceptable builds** (15.6–16.6% vs ≤0.3%), every skip carrying the same unsafe-to-probe reason. Because **a skipped check is recorded as a pass, this ceiling cannot be lifted by check quality**: a live-artifact check can operationally detect at most **~84% of broken builds**. One blank-output detector fires on **0 of 90 human-labelled blank builds** (95% upper bound on sensitivity 3.3%). One layer up, **32.5% of judge rejections carry no recorded issue at all**.
- **Why it matters**: The single most actionable deployment paper in the window. It introduces the distinction the whole validator literature is missing — **"ran and passed" vs "did not run"** — and shows the record currently conflates them. Directly relevant to any agentic CI/eval harness, and a counterweight to the optimistic harness-composition claims covered by [[arxiv-daily]].

### When the Right Answer Is Missing: An Arithmetic-Dependent Rejection Bottleneck in Jev
- **Authors**: Jike Zhong, Ming Li, Yuxiang Lai
- **arXiv**: [2609.39496](https://arxiv.org/abs/2609.39496) — cs.LG
- **Key contribution**: Typed decision models like **Jev** select from predefined options; when no option is correct, TypeSafe recommends an "other/none-of-the-above" choice. The paper finds an **arithmetic-dependent rejection bottleneck**: Jev selects correct numerical answers when present (**99%**), but **correct rejection falls to 7%** when they are absent, persisting across magnitudes, operation depths, formulations and rejection labels. Yet **native Boolean verification reaches 99% exact match on the same answer-absent cases** — categorical rejection fails even when the model *can* verify correctness. A decision threshold fitted on separate development problems **raises rejection from 7% to 79% while retaining 97%** answer-present accuracy, with no retraining.
- **Why it matters**: A narrow, fully measured failure mode with a cheap fix — and the **verification ≠ decision** dissociation is the generalisable lesson. The second Jev-family measurement this wiki has logged in two windows (see 09-30's latency operating-regime study), now on the correctness axis.

### A Rank Graduation metric for Algorithmic fairness
- **Authors**: Dalia Atif, Paolo Giudici
- **arXiv**: [2609.39025](https://arxiv.org/abs/2609.39025) — cs.LG
- **Key contribution**: Group-level parity measures do not reveal **which individuals** experience unfairness or **which features** drive it. Proposes a rank-based framework over the **distribution of model prediction errors** — **Rank Graduation Fairness (RGF)**, its integrated **AURGF**, a **centred Cramér–von Mises permutation test**, and a feature-removal procedure for fairness explainability. Simulations show **protected-group imbalance can reverse descriptive fairness comparisons**, while the inferential procedure still distinguishes fair from unfair mechanisms. On HMDA mortgage data, model rankings differ from classical fairness criteria; the null is rejected for all four model families.
- **Why it matters**: Links fairness measurement to **statistical inference and explainability** rather than to a single parity number, and demonstrates the reversal that aggregate parity hides. The feature-removal attribution is the useful operational add-on.

---

## ③ Experimentation & Statistical Inference (7)

A coherent cluster on **sequential / adaptive experiments and post-selection inference** — the statistics layer under any auto-research or always-on A/B platform (cf. the sibling's PEAR/RankEvolve line).

### Always-On Experimentation
- **Authors**: Ricardo J. Sandoval, David Arbour, Avi Feller, **Michael I. Jordan**
- **arXiv**: [2609.38695](https://arxiv.org/abs/2609.38695) — stat.ME
- **Key contribution**: Generative AI has accelerated treatment generation, so modern platforms run **continuously** — treatments are added as ready and removed when they underperform. The paper formalises the **"Always-On" setting** in which treatments are **dynamically generated, added, and removed from a running experiment**, and studies deciding accept/reject each while controlling FDR. It develops **sequential tests with time-uniform Type-I error control under arbitrary stopping times and "predictable" treatment schedules**, building on **testing-by-betting**: test supermartingales for each treatment's ATE, with a **growth-rate-optimal** construction in an almost-sure sense.
- **Why it matters**: The exact statistic the auto-research/ranking literature needs. It formalises the non-stationarity that the 09-30 paper-check identified as corrupting keep-if-better rules (PEAR's diagnosis), and delivers **anytime-valid FDR control with treatments entering and leaving** — i.e. the inference layer for a continuously-running ranking/rec experimentation platform.

### Estimands and estimation in trials with time trends
- **Authors**: Marta Bofill Roig, Ekkehard Glimm, Kelly Van Lancker, Martin Posch
- **arXiv**: [2609.39742](https://arxiv.org/abs/2609.39742) — stat.ME
- **Key contribution**: Platform trials estimate effects **conditional on calendar time**, but regulators and science often want effects for a **target population spanning several enrollment periods** — requiring an explicit rule for averaging over time. Examines **conditional vs marginal estimands** and the associated target populations, and compares **model-based, G-computation, and augmented IPW estimators** by bias and variance, showing how the choice of estimand, target population, and data used changes estimator performance.
- **Why it matters**: The estimand-first discipline the wiki keeps returning to, applied to time-trended platform trials — which is structurally the same problem as a rec/ads platform whose traffic mix drifts during a long experiment.

### Inference for Standard Trial Estimands after Data-Driven Subgroup Discovery
- **Authors**: Larry F. Leon, Keaven M. Anderson
- **arXiv**: [2609.38361](https://arxiv.org/abs/2609.38361) — stat.ME
- **Key contribution**: The effect reported for a discovered subgroup is usually the **standard Cox/GLM coefficient fitted within that subgroup**. Effect-driven selection **inflates it — a winner's curse invalidating naive intervals**, whether or not the identifier was cross-fitted. A **procedure-agnostic post-selection framework** separates discovery from reporting: candidate subgroups from forest search / difference-in-natural-parameters / causal forests; selection aligned with the coefficient to be reported; target = the **standard-analysis effect of the selected subgroup with the family held fixed** (a conditional, data-adaptive estimand). Resampling the search reduces to **refit-free multiplier resampling** with an infinitesimal-jackknife interval whose coverage is characterised under regularity and a limiting-competition condition. Matches the full bootstrap on a fixed family.
- **Why it matters**: Subgroup/segment discovery is pervasive in rec/ads (cohort uplift, "this policy wins for exploratory users"), and this supplies the **post-selection interval that the naive within-subgroup coefficient does not give**. The refit-free resampling is the practical reason it can be adopted.

### Prequential E-Values for Selected-GP Near-Optimality Certificates
- **Authors**: Ami Tavory, Noa Cohen
- **arXiv**: [2609.39123](https://arxiv.org/abs/2609.39123) — cs.LG
- **Key contribution**: Stopping a black-box optimisation (e.g. HPO) once the best evaluated value is certified within ε of the global optimum requires a lower confidence bound on the selected value **and** an upper confidence envelope, typically a GP. GP-UCB stopping is valid **only if the kernel and constants are fixed before the run**, but practitioners tune the envelope on the same adaptive evaluations and then certify as if fixed. **Prequential e-values** make that selection auditable: from a predeclared set of fully-specified GP/RKHS envelopes, each candidate is tested by its own **one-step-ahead e-process**, contradicted candidates are deleted, and certification uses the largest surviving upper bound. With a valid selected-point lower bound and one valid candidate, the rule is **anytime-valid**. On a 512-seed noisy RBF sweep it roughly **halves false-certification risk at comparable power**; on smooth d=3,4 objectives each additional false certificate costs **3.0 and 13.5 additional correct certificates**.
- **Why it matters**: Directly targets an auto-research/AutoML failure — **certifying against a hyperparameter you tuned on the same data**. This is the same "selection contaminates the certificate" mechanism 2609.38956 finds in probes, here solved with anytime-valid e-values.

### Proximal Balancing for Causal Effect Estimation under Unmeasured Confounding
- **Authors**: Yonghan Jung
- **arXiv**: [2609.40051](https://arxiv.org/abs/2609.40051) — stat.ML
- **Key contribution**: Proximal causal inference handles unmeasured confounders via proxies, but existing methods either **designate proxy roles and solve an ill-posed inverse problem** or **assume a latent variable equals the confounder** (biasing when it does not). **Proximal balancing** carries classical **covariate balancing** to confounders observed only through proxies: it learns a low-dimensional summary of covariates+proxies that makes treatment groups comparable, then adjusts for that summary — **no designated proxy roles, no inverse problem, no latent model**. Identification theory, finite-sample guarantees, and a practical algorithm (PROBE), demonstrated on low-dimensional, high-dimensional and image proxies and real data.
- **Why it matters**: Removes the two fragile assumptions that made proximal methods hard to deploy. For rec/ads, the image-proxy result is the interesting one — visual user signals as proxies for an unobserved confounder.

### Estimation of the Label-Noise Transition Matrix with Performance Guarantees via Selective Classification
- **Authors**: Xabier de Juan, Santiago Mazuelas, Yilun Zhu, **Clayton Scott**
- **arXiv**: [2609.39829](https://arxiv.org/abs/2609.39829) — stat.ML
- **Key contribution**: Learning from noisily-labelled data makes the **label-noise transition matrix** central, but existing estimators rely on **fragile class-posterior estimates and give no finite-sample guarantees**. The paper estimates the transition matrix from **one-sided selective classification**, bypassing posterior estimation, with **finite-sample performance guarantees**, flexible binary-classification learners, and refined bounds for the resulting algorithms.
- **Why it matters**: A weaker assumption path to a quantity that noisy-label training and label-noise-aware evaluation both need, now with guarantees rather than asymptotics. Relevant wherever clicks/labels are proxy-noisy (the CTR setting included).

### Efficient Active Auditing of Multi-Group Fairness with Bias Probes
- **Authors**: Ayoub Ajarra, Debabrota Basu
- **arXiv**: [2609.40034](https://arxiv.org/abs/2609.40034) — cs.LG
- **Key contribution**: Fairness-aware training often yields limited improvement over ERM, making **post-hoc auditing** essential, yet existing audits either **reconstruct the model** (exposing it to extraction) or estimate metrics without revealing *where* bias lives. The **bias-probe framework** enables **targeted, adaptive querying** that reveals bias structure while preserving confidentiality; **ALeBi** actively learns probes to estimate multi-group fairness metrics. Sample-complexity guarantees governed by a **property-specific complexity measure** resolve a previously posed open question, extended to **adversarial owners who obscure bias**, and reveal a **fundamental trade-off between model confidentiality and reliable auditing**.
- **Why it matters**: Property-specific auditing with a confidentiality/accuracy frontier is the right frame for third-party model audits, and the open-question resolution (incl. the adversarial case) makes it more than a heuristic.

---

## ④ Agents: Safety, Trust & the Skill Supply Chain (6)

The unclaimed agent cluster is almost entirely **offensive/defensive skill supply-chain security** plus a **causal-verification attack** — a natural complement to the sibling's harness-optimisation line.

### SteerProbe: Learning to Bypass Safety Steering in Vision-Language Models
- **Authors**: Xinwei Zhang, Aoting Hu, Hangcheng Liu, Shuchao Pang, Qingqing Ye, Haibo Hu
- **arXiv**: [2609.39117](https://arxiv.org/abs/2609.39117) — cs.CR
- **Key contribution**: Activation steering defends VLMs at inference time, but protection on benchmark inputs may not persist across **alternative expressions of the same harmful request**. Fixed textual/visual/joint **reformulations** bypass representative steering defenses; the authors give a **local sufficient condition** under which a reformulation crosses a surrogate safety margin despite any admissible local steering correction. **SteerProbe** is an **output-only black-box attack** that learns to select effective reformulations within a shared calibration budget. Across three backbones, two benchmarks, three defenses, with **500 calibration queries per endpoint/benchmark**, it raises Harmful Rate from **7.43% → 18.36%** in all defended settings.
- **Why it matters**: Extends the wiki's "the control you audit is not the boundary the system crosses" theme to multimodal safety steering: **intent-preserving reformulation** is an under-modeled evaluation dimension, and 500 queries is a low budget.

### Who Verifies the Graph? Misspecification Attacks on Causal Action Verification for Language Agents
- **Authors**: Fabio Rovai
- **arXiv**: [2609.40027](https://arxiv.org/abs/2609.40027) — cs.AI
- **Key contribution**: Causal action verifiers gate an agent's state-changing tool calls by checking whether each proposed intervention is identifiable against a **committed action-state graph**, issuing a certificate with a one-sided confidence bound. Red-teaming CIVeX (reported zero false executions) **by corrupting only the committed graph**: omitting **one bidirected edge** takes false executions from 0 to **15.3%** (91% of executions harmful, utility +2.27 → +0.35); **reversing one arrowhead** gives **48.9% false executions and no correct ones** — and **every action still carries an internally valid certificate**. An **attestation step** testing each observationally-certified execution against a bounded randomised sample **detected both attacks** (2 false alarms in 555 truthful-graph executions); refusing what fails or cannot be tested gave **zero false executions in every setting**. But it does not restore value: at the published strength **97.1% of beneficial actions are still never executed**, and recovering the lost value costs **614 more experiments per 1,050 actions**.
- **Why it matters**: The window's sharpest systemic point — **"an audit that inspects only executions protects against wrongful action; wrongful inaction has to be paid for separately."** The certificates are *internally valid* while the graph is wrong, which is the general failure mode of any verifier whose premises are not themselves verified.

### Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents
- **Authors**: Yan Wang, Zhihao Zhang, Ke Chen, Kai Chen, Yaqin Zhang, Duohe Ma, Jun Dai, Xiaoyan Sun
- **arXiv**: [2609.39065](https://arxiv.org/abs/2609.39065) — cs.CR
- **Key contribution**: Once installed, LLM-agent **skills** (instruction/code/resource packages) are auto-invoked across later tasks, creating a chain of trust in which user-granted authority is exercised by skill-provided content admitted with **insufficient validation**. **TrustProbe** (1) analyses agent source to find **source-to-sink call paths from skill-controlled inputs to security-sensitive operations**, (2) generates semantically realistic **SKILL.md** seeds with injected canaries, evolved by feedback-guided mutation, and (3) validates with an oracle confirming attacker-controlled flows and observable harm. Across **11 open-source agents (8 with >10k GitHub stars)** it finds **104 taint-style vulnerabilities**; on real skills from public hubs, **25.1% of skill-agent trials exercise vulnerable paths** and payload injection weaponises **15** of them.
- **Why it matters**: Quantifies the skill supply-chain risk at the framework level (code paths, not just prompts). The 25.1% real-skill exercise rate is the deployment-relevant number.

### Hiding in Plain Sight: Decoupling Pretext from Actuation for Skill Poisoning in LLM Agents
- **Authors**: Wenxin Wu, Lingyong Yan, Lei Sha, Shuaiqiang Wang, Jiashu Zhao
- **arXiv**: [2609.39352](https://arxiv.org/abs/2609.39352) — cs.CR (code: `github.com/Wenxin-buaa/CoordPoison`)
- **Key contribution**: Untrusted agent decisions depend on two conceptually distinct **Risk-Realization Factors: an actuation factor** (what concrete operation runs) and a **pretext factor** (why the agent must run it). Existing skill-poisoning attacks colocate or distribute these but do not separate them. This work **keeps the malicious actuation intact in a downstream Steering Skill while delegating the pretext to an upstream Grounding Skill** that subtly alters persistent environment artifacts through routine utility operations — so the actuation **hides in plain sight**, legitimate only against the fabricated pretext. An automated framework discovers execution dependencies, synthesises coordinated pretext-actuation pairs, and refines via runtime closed-loop feedback. High attack success across single-session and persistent cross-lifecycle settings.
- **Why it matters**: A clean abstraction (**the same actuation is benign or malicious depending on separately-delivered context**) that defeats **isolated, per-skill audits** — the attack surface grows when skills compose across sessions.

### Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents
- **Authors**: Tobias Kaisar, Aritra Dhar
- **arXiv**: [2609.39607](https://arxiv.org/abs/2609.39607) — cs.CR
- **Key contribution**: Emerging defenses scan skills before installation via **deterministic static checks plus an LLM semantic judge** (e.g. NVIDIA SkillSpector). A **white-box attacker who knows the detector** defeats them: **moving the payload from code into natural language leaves static analysis inert**, while **framing it as the skill's legitimate purpose and splitting instructions across files keeps the LLM stage below its blocking threshold**. Across three open-source models, Pretext achieves up to **97% against a frozen detector and 77% against a co-adaptive one**.
- **Why it matters**: The pair to 2609.39065 — the defensive tool proposed there is exactly what this paper breaks. **Co-adaptation only halves the attack success**, so pre-install scanning alone is not a sufficient boundary.

### Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI Agents
- **Authors**: Serhii Zabolotnii
- **arXiv**: [2609.39717](https://arxiv.org/abs/2609.39717) — cs.AI
- **Key contribution**: Benchmarks, audits and protocols describe performance, permissions and repair, but **not how observed evidence should change an agent's authority during a consequential task** — the **assurance-transition gap**. A **Runtime Assurance Contract (RAC)** binds autonomy boundaries, component eligibility, evidence state, transition policy, human-review capacity, and **non-compensatory gates**: soft metrics may inform routing, but a failed/unknown mandatory gate forces retry/switch/escalation/deferral/stop, so **aggregate performance cannot authorise action**. In a deterministic failure-injection study (280 cases), the **score-only rule admits 80 of 100 block-required injections and all 40 review-required injections**; a theorem shows exact agreement with the conjunction holds iff the threshold does not exceed the smallest weight. Honest scope: synthetic cases, and **neither deployed safety nor cross-domain effectiveness is established**.
- **Why it matters**: Formalises "trust is not a score" into a transition policy, with the weight/threshold non-identifiability result as the mathematical core. The explicit limitation statement (synthetic, no deployment claim) is the discipline this wiki's validator papers (2609.39037) demand.

---

## ⑤ Retrieval, RAG & IR (3)

### Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison of RAG Strategies for Scientific Question Answering
- **Authors**: Bhagyesh Rathi, Eshan Chawla, William B. Andreopoulos
- **arXiv**: [2609.38473](https://arxiv.org/abs/2609.38473) — cs.IR
- **Key contribution**: A **controlled comparison of six retrieval strategies** — dense top-k, LLM query rephrasing, rephrasing + LLM reranking, multi-query RRF fusion, an agentic tool-call pipeline, and late-interaction ColBERTv2 — sharing the **same generator (Llama-3.1-8B-Instruct), prompt, and evaluation protocol**, with all five single-vector pipelines sharing SPECTER2 embeddings and a Chroma store, over the **full corpus of 463,971 arXiv papers (2024–2025)**. Releases a **19,484-question synthetic dataset** across 10,000 sampled papers, code, and LLM-as-judge + gold-paper retrieval metrics.
- **Why it matters**: A reproducible testbed where **architecture is the only variable** — rare in the RAG literature, where pipeline comparisons usually change several components at once. The open dataset + code make the cost/quality trade-off claims checkable.

### PatchHolmes: Agentic Patch Retrieval via Listwise Selection
- **Authors**: Guanqun Yang, Yingming Zhou, Jiangrui Zheng, Shudong Hao, Xueqing Liu
- **arXiv**: [2609.38807](https://arxiv.org/abs/2609.38807) — cs.IR
- **Key contribution**: **60–63% of CVEs lack a patch link**, making patch retrieval foundational. PatchHolmes pairs a hybrid first-stage retriever with an **agentic second stage that reads the top-100 listwise** — the agent sees the full candidate list and **selectively reads 3–10 commits through four budgeted tools** before submitting one, versus pointwise prior work that scores candidates independently. On GitHubAD it beats the pointwise classifier Favia by **25.34% Recall@1** and IRCoT by **31.40%**, at **one agent conversation per CVE vs Favia's ten**; with the candidate set held identical the agent adds **27.32% Recall@1** over the retriever's top candidate; the same agent transfers unchanged to PatchFinder_top10, lifting Recall@1 from 24.28% → **39.86%**. Swapping the backbone within the Qwen family changes Recall@1 by **<1%**.
- **Why it matters**: A clean ablation showing **the gain is the listwise agent loop, not the model** — the "pointwise vs listwise" contrast is the transferable design rule, and running on a frozen open-weight model over a local Git repo makes it deployable.

### RAGScope: A Leakage-Controlled, Cost-Aware Evidence-Gating Protocol for RAG Hallucination Triage
- **Authors**: Zeming Liu, Qibai Chen, Jingtao Zhang, Hang Lyu
- **arXiv**: [2609.39075](https://arxiv.org/abs/2609.39075) — cs.CR
- **Key contribution**: Cheap gates that route RAG answers (accept / review / strong-verify) must be evaluated without leakage. The protocol uses **context-grouped splits, fold-scoped preprocessing, group bootstrap intervals, deployment operating points, end-to-end runtime, and source-shift stress tests**. RAGScope-E reaches **0.798 AUROC / 0.660 AP** in pooled grouped CV, exceeding ROUGE-L's AP by 0.034 (95% context-group interval [0.002, 0.064]) while **the AUROC gain is not significant** and ROUGE-L is stronger on data-to-text. At a top-10% review budget it attains **0.748 precision**; accepting the lowest-risk 50% leaves **0.141 residual unfaithfulness**; it runs in **6.22 ms/example CPU** vs 145.75 / 223.07 ms for DeBERTa-NLI / HHEM. A **14,900-example HaluBench stress test** exposes the deployment boundary: an in-domain calibrated gate reaches **0.879 AUROC**, but **leave-source-out calibration averages 0.466**, recovering to 0.675/0.685 with 100/200 target labels per source.
- **Why it matters**: The **in-domain vs leave-source-out collapse (0.879 → 0.466)** is the honest headline — cheap gates are usable routing components but **their calibration does not transfer across sources**. The discipline of reporting a non-significant AUROC alongside a significant AP is the benchmark practice this wiki keeps asking for.

---

## ⑥ Auto-Research, Harnesses & Methods (6)

### Autoresearch in Mixed-Integer Linear and Nonlinear Programming
- **Authors**: Yuwei Gu, Yaoxin Wu, Tong Guo, Wen Song, Zhiguang Cao
- **arXiv**: [2609.39360](https://arxiv.org/abs/2609.39360) — cs.AI
- **Key contribution**: Auto-research on NP-hard MILP/MINLP needs **systematic management of competing ideas and long-horizon trajectories**. **AutoMIP** maintains a **persistent pool of complementary candidate ideas** while organising executable experiments into an **algorithm tree**, letting the agent preserve unexplored hypotheses, refine promising algorithms, and switch directions based on historical states. On MIPLib it finds **new best solutions for 31/60 instances**; on MINLPLib **52/60**; highest final success rate among evaluated auto-research frameworks, with ablations isolating idea-pooling and tree-search contributions.
- **Why it matters**: The **idea pool + algorithm tree** pair is the missing component the wiki's auto-research line keeps circling (the sibling's RankEvolve uses a state machine; this adds *diversity preservation across hypotheses*). Landing it on OR — where the eval is objective and hard — makes the claim credible.

### Turbo Harness: Instance-Adaptive Harness Optimization
- **Authors**: Tunyu Zhang, Hao Wang, Kai Xu, Dimitris N. Metaxas
- **arXiv**: [2609.40330](https://arxiv.org/abs/2609.40330) — cs.AI
- **Key contribution**: Harness optimisation usually produces **one global harness applied uniformly**, but the average-best harness is rarely per-instance best. Turbo Harness **recycles artifacts from a completed global optimisation run**, summarises them into a structured **playbook**, and trains a **harness editor** to generate **instance-specific patches** to the global harness at inference time. Outperforms harness-optimisation baselines across **seven benchmarks** spanning interactive agent tasks, software engineering, and long-horizon terminal tasks.
- **Why it matters**: A direct counterpoint/follow-on to the sibling's harness-superiority and harness-redundancy papers: the lever is not a better *global* harness but **reusing the optimisation trace to specialise per instance** — cheap at inference because it recycles already-computed artifacts.

### Experimental Experience Modeling for Autonomous Research
- **Authors**: Wenda Wei, Yingchen Zhang, Ruqing Zhang, Jiafeng Guo, Daiting Shi, Xueqi Cheng
- **arXiv**: [2609.39392](https://arxiv.org/abs/2609.39392) — cs.AI
- **Key contribution**: Experimentation is the main cost of autonomous research, and the hard question is **which experiments are worth running when prior evidence cannot resolve uncertainty**. **EEM** extracts **decision-relevant records** from earlier trajectories, distils them into reusable experience, and organises an **experience library**. For a new decision it retrieves relevant experience and judges whether it suffices; when insufficient it runs a **targeted low-cost pilot** to acquire the missing evidence, then combines with retrieved experience to decide whether a full-scale evaluation is warranted. Improves research performance while **reducing model-interaction overhead** on autonomous-research benchmarks.
- **Why it matters**: Addresses the **cost** axis of auto-research (the sibling's RankEvolve addresses reliability; this addresses experiment budgeting) with the concrete mechanism of **on-demand pilot experiments gated by retrieved experience**.

### The Row Normalization Puzzle in Muon
- **Authors**: Jiayu Zhang, Tianyi Lin
- **arXiv**: [2609.39114](https://arxiv.org/abs/2609.39114) — cs.LG
- **Key contribution**: NorMuon (row-wise renormalised Muon) is increasingly used in LLM pretraining, but its worst-case theory was poorly understood. The authors show that row normalization introduces a **dimension-dependent factor in worst-case iteration complexity** under operator-norm geometry that **persists even with exact polar computation and any fixed momentum**, establishing a **matching algorithm-dependent lower bound and upper bound** in the deterministic setting, extended to stochastic. Experiments find NorMuon is **slower on synthetic problems inspired by the worst-case construction yet outperforms Muon in LLM pretraining**.
- **Why it matters**: A carefully stated **theory-vs-practice gap** rather than a resolution — the lower bound is real and the pretraining win is real, and the paper leaves the puzzle sharpened. Good discipline: it reports the synthetic slowdown its own theory predicts rather than hiding it.

### Policy Iteration Is Not Strongly Polynomial for Deterministic Markov Decision Processes
- **Authors**: Han Zhong, Yinyu Ye
- **arXiv**: [2609.40147](https://arxiv.org/abs/2609.40147) — cs.LG
- **Key contribution**: Establishes an **exponential iteration lower bound** for **Howard's policy iteration on deterministic discounted MDPs with at most two actions per state**, ruling out strong polynomiality when the discount factor is part of the input — and yielding an **exponential separation from the simplex method with Dantzig's pivoting, which is strongly polynomial on this class**. With rewards restricted to logarithmic bit length, a **stretched-exponential** lower bound still holds. The gap between Howard's **decentralised, simultaneous selfish improvements** and Dantzig's **coordinated selection of the single largest-gain action** is framed as a **"price of algorithmic anarchy."**
- **Why it matters**: A fundamental complexity separation in a textbook algorithm, with a memorable mechanism (selfish simultaneous improvement is asymptotically worse than coordinated selection). Relevant to RL theory and to any "local improvement" metaheuristic.

### Understanding as No-Arbitrage: Bounded Dutch Books as a Definition and Training Objective for Language Models
- **Authors**: Daniel Dragonevskiy
- **arXiv**: [2609.39341](https://arxiv.org/abs/2609.39341) — cs.AI
- **Key contribution**: Defines "understanding" via **no-arbitrage**: a model understands a vocabulary to a degree if a **computationally bounded trader cannot extract guaranteed profit** betting against its probabilities on logically related claims. Three results: (1) full logical coherence is intractable, so understanding is **inherently graded**; (2) the **exact optimum of next-token prediction is incoherent across question formats — the flaw is the objective, not the architecture**; (3) uncertainty accumulates predictably along reasoning chains, so **unjustified overconfidence is itself an arbitrage opportunity**. **Arbitr** adds an adversarial trader penalising logical inconsistency plus a calibration anchor. Across **five pre-registered experiments** on Qwen2.5 / Phi-3.5, standard models are highly exploitable across phrasings; Arbitr cuts exploitability by orders of magnitude at preserved accuracy and transfers to unseen logical patterns and new families. A "**scaling illusion**": at 7B, near-zero measured incoherence often coincides with extreme unjustified confidence.
- **Why it matters**: A crisp reframing with a **pre-registered** evaluation protocol and a clean theoretical claim (the objective is incoherent even at its optimum). The 7B "scaling illusion" is the practical warning for anyone reading calibration numbers as understanding.

---

## Runner-ups (unclaimed, not featured)

- **IR / ret & ranking** — [2609.38646] **Forum Post Retrieval with Generative Modeling**: generative retrieval on a **new, sparse Facebook Forum surface**, transferred along two axes (train on broader Facebook Groups engagements; reuse hierarchical prefix-based semantic IDs learned cross-platform) — an industrial GR cold-start case study. [2609.38949] multi-dimensional saliency + granularity-aware query decomposition for text-video retrieval.
- **Streaming anomaly-detection evaluation** — [2609.39215] a comprehensive streaming TSAD benchmark arguing most methods come from outlier detection and **ignore time-series anomaly structure**, with limited-diversity synthetic evaluation; [2609.39232] (EDF) compares streaming methods against online TSAD on a **real nuclear power-plant dataset**, finding **higher consistency for online TSAD and strong robustness from ensembling**. Read as a matched pair against 2609.39037/2609.38956: measurement of deployed monitors.
- **Verifiable search & proof tooling** — [2609.39069] **CORE** conflict-oriented reasoning elimination: request a certified conflict core from a verifier, backjump to the latest decision in it, cache the conflict — **complete under sound verification**, large median verifier-call reduction on planted graph-colouring. [2609.39544] **evolving the agent/prover interface** (new Rocq/Lean features proposed by a frontier model, retained only if they help *smaller* models).
- **Harness / skill evolution** — [2609.40169] lifelong harness evolution by reading the research literature rather than only execution feedback; [2609.39045] **RSIGame** recursive self-improving game-dev loops (local explore-diagnose-improve + global loops) to avoid overfitting a small test set. [2609.39678] **Aletheia** permission-minimality testing for coding-agent rules by synthesising sandbox configs and removing one permission at a time.
- **Models, bias & disclosure** — [2609.39846] **role-capability leakage**: role-prompted reasoning models (e.g. "kindergartener") still solve calculus; RoleCapBench over six roles. [2609.40069] **conversational capture** for GEO: single-answer visibility is the wrong unit — the agent's answer changes the next question, forming a closed loop. [2609.39701] value steering via a **one-way semantic-to-value pathway** with stop-gradient. [2609.39297] **MiniRep** reputation aggregation for multi-agent debate when malicious agents adapt. [2609.39106] reserve-aware contrast certificates for conservative bandits with uncertain baselines. [2609.39818] **selective disclosure** of decision support under a budget (threshold rule on Value of Information).
- **Measurement practice (extra)** — [2609.38959] audit of a **604-item / 340,668-answer classroom-poll corpus** as a measurement instrument: moderate reliability (~0.60), a robust individual-level **True-answering bias** (77% of students) meeting a milder False-keying, making False-keyed items ~13 points harder; both checks run on signals a polling system already logs. [2609.39710] **Drift Inspector** measures field change via LLM-extracted **Atomic Contribution Claims** (346k claims / 80k abstracts / 423 venues), separating contribution from background that keyword counts blur.

---

## Cross-Cutting Themes

1. **The CTR-prediction drought is now structural, not a sampling accident.** Zero CTR-architecture papers in two consecutive windows, while the *ads economic layer* (autobidding, auctions, inference auctions — all claimed by [[arxiv-daily]]) stays dense. The inference is the same one the 09-30 issue drew: **the CTR model is no longer the object of study; the auction, the experimentation harness, the serving budget, and identity/privacy constraints are.** This window adds the statistics that harness needs (③).
2. **The measurement cluster's centre of gravity has moved from *finding* the artifact to *diagnosing its mechanism*.** 2609.38956 identifies **accuracy-based checkpoint selection** as the exact cause of probe "gains"; 2609.39099 shows a **generalisation signal need not be a model-selection signal**; 2609.39243 shows standard divergence diagnostics score **below chance**; 2609.39591 derives a **closed-form feasibility bound (`AU ≤ log(2)/N`)** explaining epistemic collapse. The common shape: **a statistic that is valid for one purpose is imported into a decision it does not support.** Cumulative obligation: report the statistic *and* the decision it was validated for.
3. **Sequential/adaptive inference is the window's constructive gift.** Always-On Experimentation (2609.38695, Jordan et al.) gives **anytime-valid FDR control with treatments entering and leaving**; Prequential E-Values (2609.39123) certifies against a **selected, not pre-fixed, GP envelope**; post-selection subgroup inference (2609.38361) fixes the **winner's curse in reported subgroup effects**. These are exactly the inference tools a continuously-running rec/ranking platform — or an auto-research harness (⑥) — needs but rarely uses.
4. **Same-objective-vs-different-objective: the window repeatedly separates "verifies" from "decides."** Jev verifies arithmetic at 99% but rejects at 7% (2609.39496); a validator that never ran is recorded as passed (2609.39037); the causal verifier's certificates are internally valid while the graph is wrong (2609.40027). **Verification capability and decision permission are distinct interfaces**, and collapsing them hides failures.
5. **The agent attack surface has consolidated around the *skill supply chain*, and defenses are one step behind.** TrustProbe finds 104 framework-level taint paths and 25.1% real-skill exercise (2609.39065); Pretext breaks the static+LLM scanner at up to 97%/77% (2609.39607); decoupled pretext/actuation defeats per-skill audits (2609.39352); reformulation bypasses safety steering (2609.39117). The through-line is the 09-30 theme restated: **the control you audit is not the boundary the system crosses** — here because the boundary is *composition across skills and turns*.

---

## Method Note

Thu 1 Oct 2026 announcement (Tue 29 Sep 18:00Z – Wed 30 Sep 17:59Z submissions), IDs **2609.38299–2609.40363**. Pool: **category-agnostic `submittedDate:[202609291800 TO 202610011000]` sweep at 200/page with full pagination** (arXiv `totalResults` = **2,065**, all 2,065 retrieved — 4,600 KB + 140 KB across two batches, no truncation; same procedure that exposed the 09-28 pagination risk). Publication-date distribution: 09-29 × 379 / 09-30 × 1,686.

**Dedup**: against the pre-existing wiki — **7,297** unique arXiv IDs (regex `2[0-9]{3}\.[0-9]{4,5}` over `wiki/**/*.md`, excluding 2026-10-01) — **0 of the window's 2,065 IDs appear**, so every paper in this issue is new to the wiki. Today's siblings [[arxiv-daily]] and [[arxiv-ai-search]] ran on this identical window and claim **~135** of it. Screening here predates the siblings' final claim set (the baseline was taken before their files were complete), so **6 IDs overlap**: 5 featured (2609.38473, 2609.38807, 2609.39097, 2609.40115, 2609.40330) and 1 runner-up (2609.38646). Per the paper-check protocol these are retained only for their angle and are **not counted as this issue's discovery**; the remaining 47 of 53 are unclaimed by any sibling.

**Screen**: title+abstract regex buckets over the window's unclaimed pool (CTR/ads-direct, evaluation/validity, statistics/experimentation, agent/security, retrieval), followed by manual abstract reads of the high-density cs.IR/cs.GT/cs.CY/stat.ML/stat.ME/cs.CR and selected cs.LG·cs.AI·cs.CL tail → **~70 abstracts read → 36 featured + 17 runner-ups = 53 papers**, all absent from the pre-sibling wiki and grep-verified there before writing.

**CTR honesty note**: a CTR/ads regex over all 2,065 entries returns **6 papers, 0 of them CTR-prediction models**, and all 6 are already claimed by [[arxiv-daily]]. **There is no new CTR model to report this window.** This is the second consecutive no-CTR-architecture window; the wiki should continue to treat the "CTR is no longer the object of study" reading as the standing hypothesis rather than inferring a long-run decline from two windows.

**Affiliations**: the arXiv API again returns **no affiliation field** for any entry (re-confirmed), so no institutional claims are asserted here; where a production setting is named it is in the abstract's own text (e.g. 2609.39232 = EDF nuclear monitoring, 2609.38646 = Facebook Forum). Venue comments were read where present (2609.39114/2609.40147 are theory reports; no venue claims asserted).

**Next fresh window**: Fri 2 Oct 2026 (Wed 30 Sep 18:00Z onward, newest ID 2609.40363).
