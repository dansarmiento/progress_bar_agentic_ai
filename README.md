
# Self-Check Agents — Streamlit + Ollama (Llama 3.2)

Modular Streamlit app demonstrating a transparent **DRAFT → CRITIQUE → FINAL** workflow using a local LLM via **Ollama**.

## Features
- Three-stage self-check agent with token streaming
- Clean module layout for prompts, agent logic, and UI
- Built-in demos: Recipe Adjuster, Simple Code Debugger, Study Plan Creator
- Works with any Ollama model name, default `llama3.2`

## Quick start
1. Install and run Ollama, pull the model:
   ```bash
   ollama pull llama3.2
   ollama run llama3.2 "hello"
   ```

2. Create a virtual environment and install deps:
   ```bash
   python -m venv .venv
   . .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run Streamlit:
   ```bash
   streamlit run streamlit_app.py
   ```

4. Optional: point to a remote Ollama server
   ```bash
   export OLLAMA_HOST="http://localhost:11434"
   ```

## Structure
```
self_check_agents/
├─ README.md
├─ requirements.txt
├─ streamlit_app.py
└─ self_check_agents/
   ├─ __init__.py
   ├─ config.py
   ├─ prompts.py
   ├─ demos.py
   ├─ ollama_client.py
   ├─ agent.py
   ├─ ui/
   │  ├─ __init__.py
   │  └─ layout.py
   └─ utils/
      ├─ __init__.py
      └─ streaming.py
```

## Notes
- Switch models in the sidebar, for example `llama3.2:latest`.
- Extend `agent.py` to add tools, memory, or rubric-based scoring.
- The app uses three **separate** chats to enforce the self-check pattern.
