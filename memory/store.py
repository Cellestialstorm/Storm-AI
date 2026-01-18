import json
from collections import deque
import os

MEMORY_FILE = "memory/memory.json"

DEFAULT_MEMORY = {
    "user": {},
    "preferences": {}
}

SHORT_TERM_MEMORY = deque(maxlen=10)

def remember_short(role, text):
    SHORT_TERM_MEMORY.append({
        "role": role,
        "text": text
    })

def get_short_context():
    return "\n".join(
        f"{m['role']}: {m['text']}" for m in SHORT_TERM_MEMORY
    )

def load_memory():
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        save_memory(DEFAULT_MEMORY)
        return DEFAULT_MEMORY
    
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                raise ValueError("Empty memory file")
            return json.loads(content)
    except Exception as e:
        print("⚠️ Memory file corrupted. Resetting memory.", e)
        save_memory(DEFAULT_MEMORY)
        return DEFAULT_MEMORY
    
def update_memory(key, value, category="user"):
    memory = load_memory()
    memory.setdefault(category, {})
    memory[category][key] = value
    save_memory(memory)

def save_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

def remember(key, value, category="user"):
    memory = load_memory()
    memory.setdefault(category, {})
    memory[category][key] = value
    save_memory(memory)

def recall():
    return load_memory()

def facts_memory(notes: str):
    if not isinstance(notes, str) or not notes:
        return

    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    memory = {"notes": []}

    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                memory = json.load(f)
        except json.JSONDecodeError:
            pass

    data = json.loads(notes)
    load_notes = data.get("notes")
    clean_notes = []
    for note in load_notes:
        if isinstance(note, str) and 5 < len(note) < 200:
            clean_notes.append(note)

    if not clean_notes:
        return
    else:
        memory["notes"] = clean_notes

    with open(MEMORY_FILE, 'w', encoding="utf-8") as f:
        json.dump(memory, f, indent=2)
        print("Done!")


