RULES = [
    {
        "name": "distraction_too_long",
        "category": "distraction",
        "min_duration": 15 * 60,
        "cooldown": 20 * 60,
        "message": "You were planning to focus. Want me to help you stay on track?"
    },
    {
        "name": "idle_too_long",
        "category": "unknown",
        "min_duration": 10 * 60,
        "cooldown": 30 * 60,
        "message": "You've been idle for a while> Everything okay?"
    }
]