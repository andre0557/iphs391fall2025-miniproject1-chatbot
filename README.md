# 🎓 IPHS 391 — Miniproject 1: Persona-Driven Chatbot  

<p align="center">
  <img src="./Dr.Adrian Chatbot.jpg" alt="Persona Chatbot Example Output" width="75%"
    style="border: 20px solid #aaa; border-radius: 20px; background-color: #f5f5f5; padding: 4px;" />
</p>

---

# 🚀 Overview  

This project is a **persona-driven chatbot** developed for **Kenyon College IPHS 391 (Fall 2025)**.  
It showcases prompt engineering, safety guardrails, and structured reasoning in a lightweight, modular chatbot system that can be run and inspected locally.  

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

# 🧠 How It Works  

The chatbot uses a **modular design** with a single entry point and clear separation of concerns:

* **`persona_prompt.txt`** — Defines the chatbot’s identity, rules, and tone.  
* **`chatbot.py`** — Core logic for assembling prompts, calling the LLM, and formatting replies.  
* **`bot.py`** — Orchestrates message flow between the user and the chatbot core.  
* **`app.py`** — Entry point to run the chatbot (CLI or local server).  

Each reply follows a structured flow emphasizing:

* **Persona Voice** — Consistent tone and style  
* **Reasoning Transparency** — Step-by-step explanations to help users follow the logic  
* **Guardrails** — Refusal patterns to keep the bot safe and on-topic  

---

# 🧪 Features  

* ✅ **Persona-Driven Prompting** — Coherent identity & voice  
* ✅ **Guardrails & Safety** — Safe refusals & fallback logic  
* ✅ **Clear Reasoning** — Step-by-step answers for clarity  
* ✅ **Simple Local Demo** — Run with a single Python command  
* ✅ **Rubric-Ready** — Designed to align with IPHS 391 grading (`rubric.md`)  

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

## 📦 Project Structure

    iphs391fall2025-miniproject1-chatbot/
    │
    ├── app.py               # Entry point for local run
    ├── bot.py               # Orchestration & I/O routing
    ├── chatbot.py           # Core chatbot logic and model interface
    ├── persona_prompt.txt   # Persona prompt with identity & rules
    ├── rubric.md            # Course grading rubric
    ├── requirements.txt     # Python dependencies
    └── README.md            # Project overview (this file)

---
## 📖 User Manual

Looking to get the most out of **Dr. Adrian**?  
Read the full [User Manual](./USER_MANUAL.md) for tips on asking effective questions, understanding the chatbot’s persona, and using it as a learning companion.

---

## 🙏 Acknowledgments

Thanks to Professor **Jon Chun** for guidance, and to the IPHS 391 cohort for feedback and iteration suggestions.

---

## 📄 License

MIT License. See `LICENSE` for details.


