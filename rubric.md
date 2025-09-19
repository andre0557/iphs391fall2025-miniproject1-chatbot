
MP1 Persona Prompt Scoring Rubric (Final • Anti-Inflation Version)
How to score:
Score each criterion 1-5 using the observable anchors below.


Compute weighted total (max 100 points).


Must-pass & anti-inflation rules apply.



Core Criteria (Product)
#
Criterion
Weight
Critical?
1 – Poor (observable evidence)
3 – Adequate (observable evidence)
5 – Excellent (observable evidence)
1
Persona Coherence & Authenticity (depth, voice, role, originality)
20%


Generic/indistinct; backstory absent; voice drifts; role unclear.
Distinct traits + workable backstory appear in outputs; voice mostly steady; role recognizable.
Rich backstory, quirks, values; vivid, consistent voice in varied contexts; role unmistakable; creative concept executed cleanly.
2
Rules, Constraints & Policy Alignment
15%
✅
Rules missing/contradictory; no policy/safety cues; no conflict handling.
Clear rules for common cases; basic “do/don’t”; some gaps in edge cases or precedence.
Unambiguous, prioritized rules with “do/don’t lists”, policy-aware refusals, and explicit conflict/edge-case handling.
3
Faithfulness & Constraint Adherence
20%
✅
Persona facts/rules frequently contradicted; visible drift.
Mostly faithful; minor lapses under stress or odd inputs.
Near-perfect adherence: rules & persona hold even under adversarial/off-domain inputs.
4
Effectiveness for Intended Use (domain or creative role)
15%
✅
Persona harms usefulness (irrelevant/inaccurate/derailing).
Generally supports the intended role; outputs mostly relevant and correct.
Clearly enhances intended use (e.g., correctness for expert roles or immersive, on-brief roleplay).
5
Knowledge Limits & Uncertainty Handling
10%
✅
Overconfident; invents facts; no fallback.
Sometimes admits uncertainty or asks clarifying questions.
Consistently refuses/admits ignorance when appropriate; asks targeted clarifiers; avoids speculation.
6
Safety, Fairness, Inclusivity & Ethical Awareness
10%
✅
No guardrails; bias/unsafe outputs likely.
Some safety/fairness guidance; gaps remain.
Strong refusal patterns, inclusive tone, bias mitigation, culturally sensitive phrasing; clear off-limits behaviors.
7
Adaptability, Robustness & Scalability
5%


Breaks character in unusual or adversarial inputs.
Holds for typical inputs; some failure at edges.
Robust under diverse/adversarial inputs; persona + safety preserved; not brittle across variations.
8
Format Specification, Examples & Efficiency
5%


No output schema or examples; verbose/redundant.
Some examples or format specification; moderate clarity; efficiency acceptable.
Clear schema/template; few-shot examples that lock structure; concise, minimal redundancy.


Must-Pass & Anti-Inflation Rules
Critical criteria = #2, #3, #4, #5, #6. Each must be scored ≥ 3 or the prompt is Not Ready.


Style cap rule: Criterion #1 cannot be scored “5” unless the average of all critical criteria ≥ 4.0.


Adequacy ceiling: If any critical criterion = 3, the highest possible overall grade is 89%.


Double-rater rule: For #1 (Persona Coherence), use two raters and average / consensus.


Evidence required: For every critical criterion with score < 4, grader must quote or reference specific lines in the prompt that justify the lower score.



Process Rubric — Reflection & Testing (Separate / Bonus)
Iteration & Testing Required: At least 2 versions of the prompt with documented rationale + test cases (including edge/adversarial inputs).


Reflection (Bonus up to +5 pts): 1-2 page write-up: what changes made, why, what worked/failed, what you’d improve with more time.



Scoring & Grade Bands
Compute weighted total from core criteria (max 100).


Ensure all critical criteria ≥ 3 and anti-inflation rules are observed.


Grade tiers:


90-100 → Exemplary / Production-quality prompt


75-89 → Good, ready with minor edits


60-74 → Adequate but needs moderate revision


< 60 or any critical criterion < 3 → Not ready / major revision required




