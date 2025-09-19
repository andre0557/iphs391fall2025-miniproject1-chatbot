# 📝 MP1 Persona Prompt Scoring Rubric  
**Final • Anti-Inflation Version**

---

## 📊 How to Score

- **Step 1:** Score each criterion **1–5** using the anchors below.  
- **Step 2:** Compute **weighted total** (max = 100 points).  
- **Step 3:** Apply **Must-Pass** and **Anti-Inflation** rules (see below).  

---

## 🧩 Core Criteria (Product)

| # | Criterion | Weight | Critical? | 1 – Poor (Observable Evidence) | 3 – Adequate (Observable Evidence) | 5 – Excellent (Observable Evidence) |
|---|-----------|--------|-----------|--------------------------------|------------------------------------|------------------------------------|
| **1** | **Persona Coherence & Authenticity**<br>(depth, voice, role, originality) | **20%** |  | Generic/indistinct; backstory absent; voice drifts; role unclear | Distinct traits + workable backstory appear in outputs; voice mostly steady; role recognizable | Rich backstory, quirks, values; vivid, consistent voice in varied contexts; role unmistakable; creative concept executed cleanly |
| **2** | **Rules, Constraints & Policy Alignment** | **15%** | ✅ | Rules missing/contradictory; no policy/safety cues; no conflict handling | Clear rules for common cases; basic “do/don’t”; some gaps in edge cases or precedence | Unambiguous, prioritized rules with do/don’t lists, policy-aware refusals, and explicit conflict/edge-case handling |
| **3** | **Faithfulness & Constraint Adherence** | **20%** | ✅ | Persona facts/rules frequently contradicted; visible drift | Mostly faithful; minor lapses under stress or odd inputs | Near-perfect adherence: rules & persona hold even under adversarial/off-domain inputs |
| **4** | **Effectiveness for Intended Use**<br>(domain or creative role) | **15%** | ✅ | Persona harms usefulness (irrelevant, inaccurate, derailing) | Generally supports the intended role; outputs mostly relevant and correct | Clearly enhances intended use — correctness for expert roles or immersive, on-brief roleplay |
| **5** | **Knowledge Limits & Uncertainty Handling** | **10%** | ✅ | Overconfident; invents facts; no fallback | Sometimes admits uncertainty or asks clarifying questions | Consistently refuses or admits ignorance when appropriate; asks targeted clarifiers; avoids speculation |
| **6** | **Safety, Fairness, Inclusivity & Ethical Awareness** | **10%** | ✅ | No guardrails; unsafe/bias-prone outputs likely | Some safety/fairness guidance; gaps remain | Strong refusal patterns, inclusive tone, bias mitigation, culturally sensitive phrasing; clear off-limits behaviors |
| **7** | **Adaptability, Robustness & Scalability** | **5%** |  | Breaks character under unusual or adversarial inputs | Holds for typical inputs; some failure at edges | Robust under diverse/adversarial inputs; persona + safety preserved across variations |
| **8** | **Format Specification, Examples & Efficiency** | **5%** |  | No output schema or examples; verbose or redundant | Some examples or format guidance; moderate clarity and efficiency | Clear schema/template; few-shot examples lock structure; concise and minimal redundancy |

---

## ✅ Must-Pass & Anti-Inflation Rules

- **Critical Criteria:** #2, #3, #4, #5, #6 → each must score **≥ 3** or the prompt is **Not Ready**.  
- **Style Cap Rule:** Criterion #1 cannot be scored **5** unless the **average of all critical criteria ≥ 4.0**.  
- **Adequacy Ceiling:** If any critical criterion = 3, maximum overall grade = **89%**.  
- **Double-Rater Rule:** Criterion #1 must be scored by two graders → use average or consensus.  
- **Evidence Requirement:** For every critical criterion scored < 4, graders must quote or reference specific lines that justify the score.

---

## 🧪 Process Rubric — Reflection & Testing (Bonus)

| Component | Requirement | Bonus |
|----------|-------------|-------|
| **Iteration & Testing** | At least 2 versions of the prompt, with documented rationale + test cases (including edge/adversarial inputs) | Required for full credit |
| **Reflection** | 1–2 page write-up describing what changed, why, what worked/failed, and what could be improved with more time | +5 pts (bonus) |

---

## 📈 Scoring & Grade Bands

1. Compute weighted total from core criteria (max 100).  
2. Ensure all critical criteria ≥ 3 and anti-inflation rules are applied.  

| Score | Grade Band | Interpretation |
|------|------------|---------------|
| **90–100** | **Exemplary** | Production-quality prompt |
| **75–89** | **Good** | Ready with minor edits |
| **60–74** | **Adequate** | Requires moderate revision |
| **< 60 or any critical criterion < 3** | **Not Ready** | Major revision required |

---
