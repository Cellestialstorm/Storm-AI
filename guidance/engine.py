import time
from datetime import datetime

from context.state import context_state
from guidance.rules import RULES
from voice.live_tts import speak

last_triggered = {}

def guidance_tick():
    now = time.time()

    for rule in RULES:
        name = rule["name"]
        
        if context_state["category"] != rule["category"]:
            continue

        duration = context_state.get("duration_seconds", 0)
        if duration < rule["min_duration"]:
            continue

        last_time = last_triggered.get(name, 0)
        if now - last_time < rule["cooldown"]:
            continue

        speak(rule["message"])
        last_triggered[name] = now