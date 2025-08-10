
import streamlit as st
from agent.self_check_agent import run_self_check
from config.settings import APP_TITLE, DEMO_PROMPTS, DEFAULT_MODEL

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon="🤖", layout="wide")
    st.title(APP_TITLE)
    st.caption("Iterative refinement with local Llama 3.2 via Ollama")

    with st.sidebar:
        st.header("Settings")
        model = st.text_input("Model", value=DEFAULT_MODEL)
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.5, value=0.6, step=0.05)
        st.markdown("---")
        demo_choice = st.selectbox("Pick a demo prompt", ["Custom"] + list(DEMO_PROMPTS.keys()))
        if demo_choice != "Custom":
            prompt = DEMO_PROMPTS[demo_choice]
        else:
            prompt = st.text_area("Your prompt", value="How do I make a vegan chocolate cake?", height=120)

        run_btn = st.button("Run Self-Check Agent", type="primary", use_container_width=True)

    if run_btn:
        if demo_choice != "Custom":
            user_prompt = DEMO_PROMPTS[demo_choice]
        else:
            user_prompt = prompt.strip()
        if not user_prompt:
            st.warning("Enter a prompt first.")
            st.stop()
        try:
            run_self_check(model, user_prompt, temperature)
        except Exception as e:
            st.error(f"Inference failed: {e}")

if __name__ == "__main__":
    main()
