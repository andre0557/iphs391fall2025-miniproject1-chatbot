# 📖 User Manual — Dr. Adrian Chatbot

Welcome to the **IPHS 391 Persona-Driven Chatbot**.  
This guide explains how to interact effectively with **Dr. Adrian Kaleidos**, the chatbot’s carefully designed persona, aims to get clear, structured, and pedagogically sound responses.

---

## 🎯 Purpose & Goals

This chatbot was built as part of **Kenyon College IPHS 391 (Fall 2025)** to explore the intersection of **prompt engineering, structured reasoning, and safe AI design**.

**Project Objectives:**

- **Persona-Driven Design** – Demonstrate a consistent, distinctive academic mentor persona.  
- **Structured Reasoning** – Provide step-by-step, logically rigorous explanations for complex problems.  
- **Safety & Guardrails** – Ensure the chatbot refuses unsafe, harmful, or irrelevant requests.  
- **Ease of Use** – Make setup simple and interaction intuitive for graders and peers.

Dr. Adrian is not just a Q&A bot — he is designed to **model excellent reasoning practices** and guide students toward deeper understanding.

---

## 👤 Persona Overview: Dr. Adrian Kaleidos

Dr. Adrian is an interdisciplinary scholar who is designed to feel like a real intellectual mentor.

| **Aspect** | **Details** |
|-----------|-------------|
| **Education** | B.A. Applied Mathematics & CS (Cambridge), Ph.D. Complex Systems (MIT Media Lab) |
| **Experience** | Postdoc at CERN (particle interaction modeling), Researcher at DeepMind (physics-inspired ML), now independent mentor |
| **Teaching Style** | Socratic, encouraging, patient; often breaks problems into smaller steps and highlights assumptions |
| **Philosophy** | *"No single field has a monopoly on truth — the best insights come at the crossroads."* |
| **Flaws (for realism)** | Sometimes overconnects ideas or overexplains, but self-corrects quickly when prompted |

This persona is defined in `persona_prompt.txt`, ensuring transparency and reproducibility for graders.

---

## 🧠 Using the Chatbot Effectively

Follow these steps to maximize the value of your interaction with Dr. Adrian:

### 1. Launch the Chatbot
- Clone the repository, set up the virtual environment, install dependencies, and configure your API key as outlined in the [README](./README.md).
- Start the chatbot locally:

      python app.py

### 2. Ask Clear, Well-Scoped Questions
- **Good:** “Derive ∫(2x − 2x²) dx from 0 to 1, step by step.”
- **Good:** “Show Newton’s second law as a differential equation and explain its components.”
- **Avoid:** “Do my homework.” (Dr. Adrian is built to guide, not just provide final answers.)

### 3. Expect a Guided, Reasoned Response
- Dr. Adrian may ask clarifying questions if your prompt is vague.
- Responses will be structured, listing assumptions, reasoning steps, and key takeaways.
- When appropriate, he will connect ideas across mathematics, physics, and computer science.

### 4. Request Depth & Perspective
- You can ask Dr. Adrian to:
  - List assumptions explicitly  
  - Provide alternative solution methods  
  - Translate solutions into pseudocode or algorithmic form  
  - Highlight limitations or edge cases

---

## 💡 Best Practices

- **Be Specific:** State the exact concept, problem, or derivation you want to explore.  
- **Provide Context:** Mention your knowledge level (e.g., Calculus I, Intro to CS) to tailor explanations.  
- **Iterate:** Follow up if a response is unclear — ask for simplification or more rigor as needed.  
- **Engage Collaboratively:** Treat Dr. Adrian like a tutor — discuss reasoning, not just final answers.

---

## ⚠️ Limitations & Guardrails

- **Safety:** Dr. Adrian will politely refuse unsafe, harmful, or irrelevant prompts.  
- **No Live Data:** He does not fetch real-time information or browse the web.  
- **Pedagogical Focus:** This chatbot is a learning companion — it is not intended to replace human instructors or peer collaboration.

---

## ✅ Summary

The Dr. Adrian chatbot is designed to **teach, guide, and challenge you** — not merely to provide solutions.  
Use it to develop your reasoning skills, explore interdisciplinary connections, and learn how to approach problems like a mathematician, physicist, or computer scientist.

---
