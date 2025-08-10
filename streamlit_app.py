
import streamlit as st

from self_check_agents.config import DEFAULT_MODEL
from self_check_agents.demos import DEMO_PROMPTS
from self_check_agents.agent import run_self_check

APP_TITLE = "Self-Check Agent Demo — Ollama + Llama 3.2"

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon="🤖", layout="wide")
    st.title(APP_TITLE)
    st.caption("Iterative refinement with local Llama via Ollama")

    with st.sidebar:
        st.header("Settings")
        model = st.text_input("Model", value=DEFAULT_MODEL, help="Example: llama3.2 or llama3.2:latest")
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.5, value=0.6, step=0.05)
        st.markdown("---")
        demo_choice = st.selectbox("Pick a demo prompt", ["Custom"] + list(DEMO_PROMPTS.keys()))
        if demo_choice != "Custom":
            prompt = DEMO_PROMPTS[demo_choice]
        else:
            prompt = st.text_area("Your prompt", value="How do I make a vegan chocolate cake?", height=120)

        run_btn = st.button("Run Self-Check Agent", type="primary", use_container_width=True)

        st.markdown("---")
        st.caption("Tip: set OLLAMA_HOST to point at a remote server, for example http://localhost:11434")

    if run_btn:
        user_prompt = DEMO_PROMPTS[demo_choice] if demo_choice != "Custom" else (prompt or "").strip()
        if not user_prompt:
            st.warning("Enter a prompt first.")
            st.stop()
        try:
            run_self_check(model=model, user_prompt=user_prompt, temperature=temperature)
        except Exception as e:
            st.error(f"Inference failed. Is Ollama running and the model pulled?\n\nDetails: {e}")
            st.info("Quick test in a terminal: `ollama run llama3.2 'hello'`")

    st.markdown("""
    ---
    **How it works:** The app makes three separate chats to the model. First it asks for a DRAFT, next it asks the model to CRITIQUE the draft, then it asks for a FINAL answer that fixes issues found in the critique.
    """)

if __name__ == "__main__":
    main()
