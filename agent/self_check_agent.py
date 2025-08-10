
import streamlit as st
from utils.ollama_client import chat_call, stream_response
from config.settings import SYSTEM_BASE, DRAFT_INSTR, CRITIQUE_INSTR, FINAL_INSTR

def run_self_check(model, user_prompt, temperature=0.6):
    draft_container = st.container()
    draft_container.subheader("DRAFT")
    messages = [
        {"role": "system", "content": SYSTEM_BASE},
        {"role": "user", "content": f"{user_prompt}\n\n{DRAFT_INSTR}"}
    ]
    draft_events = chat_call(model, messages, stream=True, options={"temperature": temperature})
    draft_text_area = draft_container.empty()
    draft_text = stream_response(draft_events, draft_text_area)

    critique_container = st.container()
    critique_container.subheader("CRITIQUE")
    messages = [
        {"role": "system", "content": SYSTEM_BASE},
        {"role": "user", "content": f"User request: {user_prompt}\n\nHere is the DRAFT:\n{draft_text}\n\n{CRITIQUE_INSTR}"}
    ]
    critique_events = chat_call(model, messages, stream=True, options={"temperature": temperature})
    critique_text_area = critique_container.empty()
    critique_text = stream_response(critique_events, critique_text_area)

    final_container = st.container()
    final_container.subheader("FINAL")
    messages = [
        {"role": "system", "content": SYSTEM_BASE},
        {"role": "user", "content": f"User request: {user_prompt}\n\nDRAFT:\n{draft_text}\n\nCRITIQUE:\n{critique_text}\n\n{FINAL_INSTR}"}
    ]
    final_events = chat_call(model, messages, stream=True, options={"temperature": temperature})
    final_text_area = final_container.empty()
    final_text = stream_response(final_events, final_text_area)

    return draft_text, critique_text, final_text
