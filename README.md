# 🎓 IPHS 391 — Miniproject 1: Persona-Driven Chatbot  

<p align="center">
  <img src="./FIG_Terminal_Chatbot.png" alt="Persona Chatbot Example Output" width="55%"
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

> ⚠️ Make sure you have **Python 3.10+** installed and (if needed) an API key for your LLM provider.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/andre0557/iphs391fall2025-miniproject1-chatbot
   cd iphs391fall2025-miniproject1-chatbot
````

2. **Set up a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure API credentials (if required):**

   Create a `.env` file in the project root with:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the chatbot:**

   ```bash
   python app.py
   ```
---

## 📦 Project Structure

```
iphs391fall2025-miniproject1-chatbot/
│
├── app.py               # Entry point for local run
├── bot.py               # Orchestration & I/O routing
├── chatbot.py           # Core chatbot logic and model interface
├── persona_prompt.txt   # Persona prompt with identity & rules
├── rubric.md            # Course grading rubric
├── requirements.txt     # Python dependencies
└── README.md            # Project overview (this file)
```

---


## 🙏 Acknowledgments

Thanks to Professors **Jon Chun** for guidance, and to the IPHS 391 cohort for feedback and iteration suggestions.

---

## 📄 License

MIT License. See `LICENSE` for details.

```




