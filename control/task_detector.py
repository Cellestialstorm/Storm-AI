from context.state import context_state

def detect_task():
    app = (context_state.get("active_app")  or "").lower()
    title = (context_state.get("window_title") or "").lower()

    if app in {"code", "pycharm"}:
        return "coding"
    
    if app in {"word", "notepad"}:
        return "writing"
    
    if "pdf" in title or "lecture" in title:
        return "studying"
    
    if app == "chrome":
        if any(x in title for x in ["youtube", "netflix"]):
            return "distraction"
        return "studying"
    
    return "generic"