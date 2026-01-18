from datetime import datetime
from control.focus_state import focus_state
from control.rules import DEFAULT_ALLOWED_APPS
from control.task_detector import detect_task
from control.task_profiles import TASK_PROFILES

def enable_focus(reason=None, extra_allowed=None):
    focus_state["enabled"] = True
    focus_state["reason"] = reason or task
    focus_state["started_at"] = datetime.now().isoformat()

    focus_state["allowed_apps"] = set(DEFAULT_ALLOWED_APPS)
    task = detect_task()
    extra_allowed = TASK_PROFILES.get(task)
    if extra_allowed:
        focus_state["allowed_apps"].update(extra_allowed)

def disable_focus():
    focus_state["enabled"] = False
    focus_state["allowed_apps"].clear()
    focus_state["reason"] = None
    focus_state["started_at"] = None