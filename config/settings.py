
APP_TITLE = "Self-Check Agent Demo — Ollama + Llama 3.2"

SYSTEM_BASE = (
    "You are a precise, direct AI that shows your process in three labeled stages: "
    "DRAFT, CRITIQUE, FINAL. Keep outputs concise and useful. "
    "Be honest about mistakes and improve them."
)

DRAFT_INSTR = "Produce a first attempt labeled as 'DRAFT:'. Do not include critique or final yet."
CRITIQUE_INSTR = "Critique the DRAFT only. Label the section 'CRITIQUE:'. Identify factual errors, clarity issues, missing constraints, unsafe or incorrect steps, and edge cases. Be specific and actionable."
FINAL_INSTR = "Refine the DRAFT using the CRITIQUE. Label as 'FINAL:'. Deliver a corrected and polished answer."

DEFAULT_MODEL = "llama3.2"

DEMO_PROMPTS = {
    "Recipe Adjuster 🧑‍🍳": "How do I make a vegan chocolate cake?",
    "Simple Code Debugger 🐛": "Here’s my Python code to find the average of a list, but it’s not working: def avg(nums): return sum(nums) / len(nums) - 1",
    "Study Plan Creator 📚": "Create a study plan for my history final exam which is in one week."
}
