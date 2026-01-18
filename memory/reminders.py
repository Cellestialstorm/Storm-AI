import json, os, uuid
from datetime import datetime, timedelta
import re
import time
from voice.live_tts import speak

REMINDER_FILE = "memory/reminders.json"

def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return {"reminders": []}
    with open(REMINDER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_reminders(data):
    os.makedirs(os.path.dirname(REMINDER_FILE), exist_ok=True)
    with open(REMINDER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_reminder(text, time_iso):
    data = load_reminders()
    data["reminders"].append({
        "id": str(uuid.uuid4()),
        "text": text,
        "time": time_iso,
        "repeat": None,
        "active": True,
        "created_at": datetime.now().isoformat()
    })
    save_reminders(data)

def check_due_reminders():
    now = datetime.now()
    data = load_reminders()
    triggered = []

    for r in data["reminders"]:
        if r["active"] and resolve_time(r["time"]) <= now:
            triggered.append(r)
            r["active"] = False

    if triggered:
        save_reminders(data)

    return triggered

def resolve_time(time_str: str) -> datetime:
    if time_str.startswith("PT"):
        now = datetime.now()
        minutes = hours = seconds = 0

        m = re.search(r"(\d+)M", time_str)
        h = re.search(r"(\d+)H", time_str)
        s = re.search(r"(\d+)S", time_str)

        if m: minutes = int(m.group(1))
        if h: hours = int(h.group(1))
        if s: seconds = int(s.group(1))

        return now + timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )
    
    return datetime.fromisoformat(time_str)

STOP_REMINDER_THREAD = False

def reminder_watcher():
    global STOP_REMINDER_THREAD

    while not STOP_REMINDER_THREAD:
        due = check_due_reminders()

        for r in due:
            message = f"Reminder. {r['text']}"
            speak(message)

        time.sleep(10)