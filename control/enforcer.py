import psutil
from control.focus_state import focus_state
import win32gui, win32process

def get_user_opened_apps():
    apps = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                proc = psutil.Process(pid)
                apps.append(proc.name())
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return True
    win32gui.EnumWindows(callback, None)
    return apps 

def enforce_focus():
    if not focus_state["enabled"]:
        return
    
    allowed = focus_state["allowed_apps"]
    apps_opened = get_user_opened_apps()

    for proc in apps_opened:
        try:
            name = proc.info["name"].replace(".exe", "").lower()
            if name not in allowed:
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue