PRODUCTIVE_APPS = {
    "code", "pycharm", "notepad", "terminal", "cmd", "powershell"
}

DISTRACTION_APPS = {
    "chrome", "edge", "brave", "spotify", "discord"
}

def categorize(app_name: str, title: str | None):
    app = app_name.lower()

    if app in PRODUCTIVE_APPS:
        return "productive"
    
    if app in DISTRACTION_APPS:
        return "distraction"
    
    if app in DISTRACTION_APPS:
        if title and any(x in title.lower() for x in ["youtube", "netflix", "instagram"]):
            return "distraction"
        return "neutral"
    
    return "unknown"