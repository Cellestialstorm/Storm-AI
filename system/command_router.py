from memory.store import remember, update_memory
from AppOpener import open, close
import time
from datetime import datetime
import webbrowser
from pyautogui import write, screenshot, hotkey
from memory.reminders import add_reminder, resolve_time

def handle_commands(cmd: dict):
    action = cmd.get("action")
    args = cmd.get("args", {})
    target = cmd.get("target")

    if action == "open_app":
        if not target:
            return "Which app should I open?"
        try:
            open(target)
            return f"Opening {target}"
        except Exception:
            return f"Sorry, I couldn't open {target}"
    
    if action == "close_app":
        if not target:
            return "Which app should I close?"
        try:
            close(target)
            return f"Closing {target}"
        except Exception:
            return f"Sorry, I couldn't close {target}"
        
    if action == "remeber":
        key = args.get("key")
        value = args.get("value")

        if not key or not value:
            return "What should I remember?"

        remember(key, value)
        return f"I'll remember that your {key} is {value}"
    
    if action == "recall":
        return {
            "type": "MEMORY_CONTEXT"
        }
    
    if action == "update":
        key = args.get("key")
        value = args.get("value")

        if not key or not value:
            return "What should I update?"
        
        update_memory(key, value)
        return f"I have successfully updated {key} to {value}"
    
    if action == "type_text":
        hotkey("ctrl", "l")
        write(args["text"], interval=0.03)
        return "Done."

    if action == "screenshot":
        screenshot(f"screenshot_{int(time.time())}.png")
    
    if action == "open_url":
        name = args.get("name", "the website")
        url = args.get("url")

        if not url:
            return "Which website should I open?"
        
        webbrowser.open(url)
        return f"Opening {name}"
    
    if action == "set_reminder":
        text = args.get("text")
        time_iso = args.get("time")

        dt = resolve_time(time_iso)
        now = datetime.now()

        date = dt.date()
        date_str = dt.strftime("%d %B %Y")
        time_str = dt.strftime("%I:%M %p")

        if dt <= now:
            return "That time has already passed. Can you tell me again?"
        
        add_reminder(text, time_iso)
            
        if date == now.date():
            return f"Alright. I’ll remind you at {time_str}."
        else:
            return f"Got it. I’ll remind you on {date_str} exactly at {time_str}."


    return None