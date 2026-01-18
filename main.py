import threading
import time
import signal
import sys
from voice.assistant_loop import run_assistant
from memory.controller import save_notes
from memory.reminders import reminder_watcher, STOP_REMINDER_THREAD
from context.tracker import context_watcher
from guidance.engine import guidance_tick
from control.watchdog import focus_watchdog
from personality.engine import personality_tick
from desktop_ui.server import start_ui_server

def graceful_exit(signum, frame):
    print("🔻 Storm shutting down. Saving memory…")
    STOP_REMINDER_THREAD = True
    save_notes()
    sys.exit(0)

def guidance_watcher():
    while True:
        guidance_tick()
        time.sleep(30)

def personality_watcher():
    while True:
        personality_tick()
        time.sleep(60)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_exit)
    signal.signal(signal.SIGTERM, graceful_exit)

    reminder_thread = threading.Thread(target=reminder_watcher, daemon=True)
    reminder_thread.start()

    context_thread = threading.Thread(target=context_watcher, daemon=True)
    context_thread.start()

    guidance_thread = threading.Thread(target=guidance_watcher, daemon=True)
    guidance_thread.start()

    watchdog_thread = threading.Thread(target=focus_watchdog, daemon=True)
    watchdog_thread.start()

    personality_thread = threading.Thread(target=personality_watcher, daemon=True)
    personality_thread.start()

    ui_thread = threading.Thread(target=start_ui_server, daemon=True)
    ui_thread.start()

    time.sleep(0.5)

    run_assistant()