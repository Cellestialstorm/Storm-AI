from voice.wake_word import listen_for_wake_word
from voice.live_stt import listen_once
from voice.live_tts import speak
from system.command_router import handle_commands
from llm.model import ask_llm
from rag.query import ask_rag
from system.validator import validate_command, is_gibberish
import time
from memory.store import remember_short
from memory.reminders import check_due_reminders 
from datetime import datetime 
from llm.parser_llm import convert_to_command
from memory.controller import save_notes
from context.state import context_state
from control.actions import enable_focus, disable_focus
from desktop_ui.state import set_ui_state

def deliver_reminders():
    due = check_due_reminders()
    for r in due:
        message = f"Reminder. {r['text']}"
        speak(message)

def run_assistant():
    speak("Storm Online.")
    last_date = datetime.now().date()
    while True:
        print(context_state)
        deliver_reminders()

        listen_for_wake_word()

        set_ui_state(
            mode="speaking",
            listening=False,
            speaking=True
        )

        speak("How may I help you?")

        query = listen_once()
        if not query:
            set_ui_state(
                mode="idle",
                listening=False,
                speaking=False
            )
            continue

        print("🧠 Heard:", query)

        parsed = convert_to_command(query)
        commands = parsed.get("commands", [])

        if len(commands) > 4:
            speak("That's too many steps at once.")
            continue

        if not commands:
            speak("I didn't understand that.")
            continue
        
        for command in commands:
            if not validate_command(command) or is_gibberish(query):
                response = "Sorry, I couldn't complete that request."
                speak(response)
                continue

            if command["intent"] in {"SYSTEM", "MEMORY"}:
                response = handle_commands(command)
                if isinstance(response, dict) and response.get("type") == "MEMORY_CONTEXT":
                    response = ask_llm(query)

                elif response is None:
                    response = ask_llm(query)
            elif command["intent"] == "RAG":
                response = ask_rag(command)
            else:
                response = ask_llm(query)
            
            print("🤖 Response:", response)

            if response:
                set_ui_state(mode="speaking", listening=False, speaking=True)
                #Remember conversation
                remember_short("user", query)
                remember_short("storm", response)
                speak(response)
                
            current_date = datetime.now().date()

            if current_date != last_date:
                save_notes()
                last_date = current_date
            
            set_ui_state(mode="idle", speaking=False, listening=False)
            time.sleep(5)

        

        
