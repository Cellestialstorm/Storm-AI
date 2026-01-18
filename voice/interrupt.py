import keyboard

def wait_for_interrupt(stop_event):
    keyboard.wait("space")
    stop_event.set()