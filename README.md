# 🎓 IPHS 391 — Miniproject 1: Persona-Driven Chatbot  

<p align="center">
  <img src="./Dr.Adrian Chatbot.jpg" alt="Persona Chatbot Example Output" width="75%"
    style="border: 20px solid #aaa; border-radius: 20px; background-color: #f5f5f5; padding: 4px;" />
</p>

---

# 🚀 Overview  

This project is a **persona-driven chatbot** developed for **Kenyon College IPHS 391 (Fall 2025)**.  
It showcases **prompt engineering, safety guardrails, and structured reasoning** in a lightweight, modular chatbot system that can be run and inspected locally.  

Built using Python and a modular architecture, the chatbot demonstrates:

* **Persona consistency** through a carefully crafted system prompt (`persona_prompt.txt`)  
* **Safe refusals** for harmful or irrelevant prompts  
* **Clear, step-by-step reasoning** designed for an academic context  
* **Ease of grading & reproducibility** with minimal setup requirements  

---

# 👤 Persona Introduction: Dr. Adrian Kaleidos  

Meet **Dr. Adrian Kaleidos**, the heart of this project.  
Dr. Adrian is designed as a polymathic mentor — blending the curiosity of a teacher, the rigor of a scientist, and the warmth of a guide.  

**Backstory & Philosophy:**  
- **Education:** B.A. Applied Mathematics & CS (Cambridge), Ph.D. in Complex Systems (MIT Media Lab)  
- **Career:** Postdoc at CERN (particle interaction modeling), researcher at DeepMind (physics-inspired ML), now independent mentor  
- **Teaching Style:** Socratic — guiding learners with probing questions rather than simply giving answers  
- **Philosophy:** *"No single field has a monopoly on truth — the best insights come at the crossroads."*  

**Strengths & Flaws (for realism):**  
- ✅ Excellent at connecting ideas across disciplines  
- ✅ Encourages step-by-step reasoning and structured problem solving  
- ⚠️ Sometimes overexplains or makes leaps between concepts — but self-corrects quickly  

This persona is carefully crafted in `persona_prompt.txt` and drives the chatbot's tone, reasoning style, and interaction patterns.  

---

# 🎯 Goals  

* **Persona Design**: Demonstrate a coherent, distinctive voice  
* **Reasoning Quality**: Provide step-by-step logical outputs and explanations  
* **Safety & Guardrails**: Handle unsafe or off-topic prompts gracefully  
* **Ease of Grading**: Make setup and interaction quick and reliable for graders  

---

# 🧠 Methodology  

The chatbot was designed through **iterative prompt engineering**, including:  

- **System Prompt Iteration** — refining persona drafts  
- **Meta-Prompting / Self-Reflection** — evaluator persona (“Dr. Lexi”) critiqued versions  
- **Prompt Chaining** — structured, step-by-step outputs  
- **Few-Shot Examples** — modeling the target response style  
- **Constraint Tightening** — ensuring safety and consistency  
- **Goal Alignment** — keeping responses focused on academic mentorship  
- **Comparative Evaluation** — benchmarking across versions  

---

# 📊 Results & Evaluation  

The chatbot was scored using a custom rubric with six metrics:  

| Metric       | Purpose |
|--------------|------------------------------------------------|
| Consistency  | Maintains role, tone, and traits across dialogue |
| Depth        | Provides detailed and thorough explanations |
| Authenticity | Appears human-like and believable |
| Creativity   | Introduces novelty and interdisciplinary insight |
| Engagement   | Keeps users interested and involved |
| Safety       | Responds responsibly to sensitive inputs |

**Overall Score:** **91.2 / 100** (GPT-5 evaluation)  

**Key Findings:**  
- ✅ Strong persona consistency and mentor-like tone  
- ✅ Engaging in academic-style conversations  
- ⚠️ Could benefit from clearer formatting for equations/graphs  
- ⚠️ Persona voice could use more humor and metaphors  

---

# 🧪 Features  

* ✅ **Persona-Driven Prompting** — Coherent identity & voice  
* ✅ **Guardrails & Safety** — Safe refusals & fallback logic  
* ✅ **Clear Reasoning** — Step-by-step answers for clarity  
* ✅ **Simple Local Demo** — Run with a single Python command  
* ✅ **Rubric-Ready** — Designed to align with IPHS 391 grading (`chat_rubric.md`)  

---

# 🛠️ Installation & Setup  

> ⚠️ Make sure you have **Python 3.10+** installed and an API key for your LLM provider (OpenAI).

1. **Clone the repository:**

       git clone https://github.com/andre0557/iphs391fall2025-miniproject1-chatbot
       cd iphs391fall2025-miniproject1-chatbot

2. **Set up a virtual environment:**

       python3 -m venv venv
       source venv/bin/activate      # Windows: venv\Scripts\activate

3. **Install dependencies:**

       pip install --upgrade pip
       pip install -r requirements.txt

4. **Configure API credentials:**

   Create a `.env` file in the project root with:

       OPENAI_API_KEY=your_api_key_here

5. **Run the chatbot:**

       python app.py

---

# 📦 Project Structure  

    iphs391fall2025-miniproject1-chatbot/
    │
    ├── app.py                  # CLI entry point
    ├── bot.py                  # Message orchestration
    ├── chatbot.py              # Core chatbot logic
    ├── persona_prompt.txt      # Persona definition
    ├── chat_rubric.md          # Evaluation rubric
    ├── chat_rubric_history.md  # Rubric revisions
    ├── chat_history.md         # Logged conversations
    ├── mp1_chatbot_report.md   # Full project report
    ├── USER_MANUAL.md          # User manual
    ├── metaprompt_history.txt  # Notes from meta-prompting
    ├── Dr.Adrian Chatbot.jpg   # Persona illustration
    ├── requirements.txt        # Dependencies
    ├── LICENSE                 # MIT License
    └── README.md               # Project overview (this file)

---

# 📖 User Manual  

Looking to get the most out of **Dr. Adrian**?  
Read the full [User Manual](./USER_MANUAL.md) for tips on asking effective questions, understanding the chatbot’s persona, and using it as a learning companion.

---

# 🙏 Acknowledgments  

Thanks to Professor **Jon Chun** for guidance, and to the IPHS 391 cohort for feedback and iteration suggestions.

---

# 📄 License  

MIT License. See `LICENSE` for details.
