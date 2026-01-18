import time
from datetime import datetime
import win32gui, win32process, psutil

from context.state import context_state
from context.categories import categorize

POLL_INTERVAL = 1.0

def get_active_window():
    hwnd = win32gui.GetForegroundWindow()
    if not hwnd:
        return None, None
    
    title = win32gui.GetWindowText(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    try:
        process = psutil.Process(pid)
        name = process.name().replace(".exe", "")
        return name, title
    except psutil.NoSuchProcess:
        return None, None
    
def context_watcher():
    last_app = None
    last_start = None

    while True:
        app, title = get_active_window()
        now = datetime.now()

        if app != last_app:
            last_app = app
            last_start = now

            context_state["active_app"] = app
            context_state["window_title"] = title
            context_state["since"] = now.isoformat()
            context_state["duration_seconds"] = 0
            context_state["title"] = categorize(app or "", title)

        else:
            if last_start:
                context_state["duration_seconds"] = int(
                    (now - last_start).total_seconds()
                )

        time.sleep(POLL_INTERVAL)