# LLaMA 3.2 Agentic AI Notebook

This repository contains a Jupyter Notebook that demonstrates building and testing a range of agent patterns with a locally hosted **Ollama** model (`llama3.2`).

## 1. Requirements

### Hardware
- A machine with **sufficient RAM and VRAM** for the chosen model.
  - 7B models can run on consumer GPUs or CPU with enough RAM.
  - Larger models (13B, 70B) require high-end GPUs or lots of system RAM.
- Windows, macOS, or Linux.

### Software
- **Python 3.10+** (Anaconda, Miniconda, or system install)
- **Jupyter Notebook** or **VS Code with Jupyter extension**
- **Ollama** installed and running locally

---

## 2. Install Ollama

1. Go to [https://ollama.com/download](https://ollama.com/download)
2. Download and install Ollama for your OS.
3. Start the Ollama server:
   - On Windows/macOS, Ollama runs automatically in the background after installation.
   - On Linux, run:
     ```bash
     ollama serve
     ```

---

## 3. Add Ollama to PATH (Windows only)

If `ollama` is not recognized in Command Prompt or your Jupyter environment:

1. Press **Windows Key**, type `environment variables`, and open **Edit the system environment variables**.
2. Click **Environment Variables**.
3. Under **User variables** or **System variables**, find `Path` and click **Edit**.
4. Add:
   ```
   C:\Users\<YourName>\AppData\Local\Programs\Ollama
   ```
   Replace `<YourName>` with your Windows username.
5. Click **OK** to save and restart any terminals or VS Code/Jupyter sessions.

You can verify by running:
```powershell
where ollama
```
It should print the full path to `ollama.exe`.

---

## 4. Pull the latest model

From a terminal:
```bash
ollama pull llama3.2
```

To confirm:
```bash
ollama list
```
You should see something like:
```
NAME              ID        SIZE
llama3.2:latest   <id>      4.7 GB
```

---

## 5. Python environment setup

### Create and activate a virtual environment (recommended)
```bash
conda create -n ollama-agents python=3.10 -y
conda activate ollama-agents
```
Or with `venv`:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Install dependencies
```bash
pip install --upgrade pip
pip install ollama openai langchain langchain-community langgraph langchain-ollama duckduckgo-search wikipedia scikit-learn tiktoken
```

---

## 6. Running the notebook

1. Start the Ollama server (if not already running):
   ```bash
   ollama serve
   ```
2. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
3. Open `llama_3_agent_chatgpt_build.ipynb` (or the latest version).
4. Set `MODEL` in the first code cell to match your pulled model tag (e.g., `"llama3.2:latest"`).
5. Run the cells in order.

---

## 7. Notes & Tips

- Keep `temperature` low (0.0–0.3) for tool-using agents to reduce output format drift.
- The notebook assumes Ollama is already running; it does not attempt to start it automatically.
- If behind a corporate proxy, set:
  ```bash
  set NO_PROXY=127.0.0.1,localhost
  ```
  so local API calls are not blocked.
- For larger document retrieval, consider replacing the built-in TF-IDF RAG example with FAISS or Chroma for better scaling.
- Tools like `web_search` and `wikipedia` require internet access.

---

## 8. Quick sanity test

To verify your setup before running the full notebook:

```bash
python - <<'PY'
import ollama
MODEL = "llama3.2:latest"
resp = ollama.chat(
    model=MODEL,
    messages=[
        {"role":"system","content":"Respond with EXACTLY: READY"},
        {"role":"user","content":"Ping"}
    ],
    options={"temperature":0.0,"num_predict":4}
)
print(resp["message"]["content"].strip())
PY
```
You should see:
```
READY
```

---

## 9. Common issues & fixes

### `RuntimeError: Ollama CLI not found on PATH`
- Cause: The environment running Jupyter does not have Ollama’s installation folder in `PATH`.
- Fix: See **Section 3** to add Ollama to PATH. Restart Jupyter after adding.

### `Cannot talk to Ollama. Make sure the service is running.`
- Cause: Ollama service isn’t running or is blocked by a firewall/proxy.
- Fix:
  - Start manually with `ollama serve`.
  - On Windows, ensure `Ollama` service is set to automatic in Services.
  - If on a proxy, set `NO_PROXY=127.0.0.1,localhost`.

### Model not found after pull
- Cause: Using a different tag in `MODEL` than what `ollama list` shows.
- Fix: Set `MODEL` exactly to the name in the `NAME` column from `ollama list`.

### JSON parsing errors in planner
- Cause: LLM output isn’t valid JSON.
- Fix: Ensure your prompt escapes braces or has a JSON-only system message. The notebook includes a fallback to “fix” malformed JSON.

---

## 10. References

- Ollama Docs: [https://github.com/jmorganca/ollama](https://github.com/jmorganca/ollama)
- LangChain Docs: [https://python.langchain.com](https://python.langchain.com)
- LangGraph Docs: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
