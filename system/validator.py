import re

VALID_INTENTS = {"SYSTEM", "MEMORY", "RAG", "LLM"}
VALID_ACTIONS = {
    "open_app",
    "close_app",
    "open_url",
    "type_text",
    "screenshot",
    "read_clipboard",
    "set_reminder",
    "remember",
    "recall",
    "update",
    "forget",
    "none",
}

def validate_command(cmd: dict) -> bool:
    if not isinstance(cmd, dict):
        return False
    if cmd.get("intent") not in VALID_INTENTS:
        return False
    if cmd.get("action") not in VALID_ACTIONS:
        return False
    return True

def is_gibberish(text: str) -> bool:
    text = text.strip().lower()

    if len(text) < 3:
        return True
    
    if not re.search(r"[aeiou]", text):
        return True
    
    if re.fullmatch(r"[\d\w_]+", text):
        return True
    
    return False
