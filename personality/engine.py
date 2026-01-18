import time
from personality.state import personality_state
from personality.traits import TRAITS
from context.state import context_state
from voice.live_tts import speak
from control.focus_state import focus_state

COOLDOWN = 5 * 60

def personality_tick():
    now = time.time()

    if not focus_state["enabled"]:
        return

    if now - personality_state["last_intervention"] < COOLDOWN:
        return
    
    category = context_state.get("category")
    duration = context_state.get("duration_seconds", 0)

    if category == "distraction" and duration > 15 * 60:
        personality_state["distraction_strikes"] += 1

        if personality_state["distraction_strikes"] == 1:
            speak("You're drifting a bit. Want help staying focused?")
        elif personality_state["distractuion_strikes"] == 2:
            speak("Be honest - is this healping you right now?")
        else:
            speak("Alright. You asked me to keep you on track.")

        personality_state["last_intervention"] = now
        return
    
    if category == "productive" and duration > 25 * 60:
        speak("Nice. You've been focused for a while.")
        personality_state["focus_successes"] += 1
        personality_state["last_intervention"] = now