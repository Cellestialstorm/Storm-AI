from threading import Lock

_state = {
    "mode": "idle",
    "focus": False,
    "listening": False,
    "speaking": False
}

_lock = Lock()

def get_ui_state():
    with _lock:
        return dict(_state)
    
def set_ui_state(**kwargs):
    with _lock:
        _state.update(kwargs)