from voice.live_stt import listen_once
from voice.live_tts import speak

YES_WORDS = ["yes", "confirm", "do it", "okay", "proceed"]
NO_WORDS = ["no", "cancel", "stop", "don't"]

def get_confirmation(action_description: str) -> bool:
    speak(f"This action is potentially dangerous. {action_description}. Do you want to continue?")

    response = listen_once().lower()
    print("🔐 Confirmation heard:", response)

    if any(word in response for word in NO_WORDS):
        speak("Confirmed.")
        return True
    
    if any(word in response for word in NO_WORDS):
        speak("Cancelled.")
        return False
    
    speak("I did not understand. Cancelling for safety.")
    return False