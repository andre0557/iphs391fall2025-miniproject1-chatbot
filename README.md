Absolutely — here’s the **entire `README.md`** in one block, ready for copy-paste:

````markdown
# 🎓 IPHS 391 — Miniproject 1: Persona-Driven Chatbot  

**Math & Logic Persona Example Output**  

---

## 🚀 Overview  
This project is a **persona-driven chatbot** developed for **Kenyon College IPHS 391 (Fall 2025)**.  
The goal was to create a **system prompt + chatbot pipeline** that demonstrates:

- **Prompt engineering** — Designing a clear, consistent persona  
- **Guardrails** — Building refusals and safety checks into the bot  
- **Structured reasoning** — Producing thoughtful, step-by-step responses  
- **Interactive demo** — Allowing graders and peers to engage with the bot locally  

The chatbot is lightweight, modular, and designed for **easy inspection** by instructors and graders.

---

## 🎯 Goals  

- **Persona Design:** Showcase a distinctive, well-crafted persona (see `persona_prompt.txt`)  
- **Reasoning Quality:** Produce clear, step-by-step logical output, avoiding hallucinations  
- **Safety & Guardrails:** Handle unsafe or irrelevant prompts gracefully  
- **Ease of Grading:** Simple, reproducible setup for instructors and peers  

---

## 🧠 How It Works  

The chatbot runs locally via `app.py` and uses a modular design:

- **`persona_prompt.txt`** contains the system prompt: identity, voice, rules, and style.  
- **`chatbot.py`** handles model calls and message formatting.  
- **`bot.py`** orchestrates I/O flow (routes user input to the core and returns responses).  
- **`app.py`** is the runnable entry point (console app or local server).  

Each response follows a **structured format** emphasizing:

- **Persona Voice:** Keeps tone and style consistent  
- **Step-by-Step Reasoning:** Explains outputs clearly for student comprehension  
- **Refusal Logic:** Rejects harmful, off-topic, or disallowed content  

---

## 🧪 Features  

✅ **Persona-Driven Prompting** — Coherent identity, tone, and style  
✅ **Guardrails** — Safe refusals and fallback behaviors  
✅ **Clear Reasoning** — Step-by-step explanations in plain language  
✅ **Simple Local Demo** — Run with `python app.py` or `flask run`  
✅ **Grading Rubric Included** — See `rubric.md` for evaluation criteria  

---

## 🛠️ Installation & Setup  

Clone the repository:  
```bash
git clone https://github.com/andre0557/iphs391fall2025-miniproject1-chatbot
cd iphs391fall2025-miniproject1-chatbot
````

Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Configure API credentials (if using OpenAI or other LLM provider):
Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
TEMPERATURE=0.2
MAX_TOKENS=800
```

Run the chatbot locally:

```bash
python app.py
```

> If `app.py` is a Flask app, you can alternatively use:
>
> ```bash
> flask run
> ```

---

## 📦 Project Structure

```
iphs391fall2025-miniproject1-chatbot/
│
├── app.py               # Entry point (console or web app)
├── bot.py               # Orchestration & I/O routing
├── chatbot.py           # Core chatbot logic and model interface
├── persona_prompt.txt   # Persona prompt with identity & rules
├── rubric.md            # Course grading rubric
├── requirements.txt     # Python dependencies
└── README.md            # Project overview (this file)
```

---

## 📊 Future Roadmap

* Web-based interface (Streamlit/Flask front-end)
* Multi-persona support (switchable system prompts)
* RAG integration for knowledge-grounded answers
* Lightweight test suite (`pytest`) for prompt regression checks
* Deployment on Render / Streamlit Cloud for live demos

---

## 🙏 Acknowledgments

Thanks to **Professors Katherine Elkins & Jon Chun** for guidance, and the IPHS 391 cohort for feedback and iteration suggestions.

---

## 📄 License

MIT License. See `LICENSE` for details.

```

Would you like me to add a small **Mermaid diagram** showing the message flow (User → bot.py → chatbot.py → LLM → Response) right in the README? It would look very polished and help graders understand your architecture at a glance.
```
