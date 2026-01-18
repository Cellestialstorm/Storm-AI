import time
from control.enforcer import enforce_focus

def focus_watchdog():
    while True:
        enforce_focus()
        time.sleep(2)