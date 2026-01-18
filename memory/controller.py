from llm.model import ask_llm
from memory.store import facts_memory

def save_notes():
    prompt = """
You are maintaining long-term memory for yourself.

You already have access to:
1. Existing long-term user memory
2. Short-term context from the current conversation
3. Today's Convertations history

Your job is to PROPOSE an updated long-term memory state.

IMPORTANT RULES (DO NOT BREAK):
- Do NOT invent new facts
- Do NOT guess or assume
- Do NOT include temporary emotions or one-time statements
- Do NOT repeat information that already exists unless it needs correction
- Keep memory concise and stable
- Long-term memory should describe who the user is, not what they said today
- If nothing meaningful should be updated, return the existing memory unchanged

========================
TASK
========================
Based on the recent conversation:
- Add new long-term facts only if they are stable and important
- Update existing facts only if the user explicitly corrected them
- Remove facts only if the user explicitly asked to forget them
- Avoid redundancy and rewording unless it improves clarity

========================
OUTPUT FORMAT (STRICT)
========================
Output ONLY valid JSON.
No explanations.
No comments.
No extra text.

The JSON MUST match this schema exactly:

{
  "notes": [
    "fact 1",
    "fact 2",
    "fact 3"
  ]
}

If no changes are needed, output the existing memory JSON unchanged.
one of the things that rohan mentioned today was he has an Importatt meeting tommorow at 12 PM

"""

    response = ask_llm(prompt)

    facts_memory(response)
    