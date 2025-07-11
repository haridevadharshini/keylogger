from cryptography.fernet import Fernet

def generate_key():
    # Generate a secure Fernet key
    key = Fernet.generate_key()
    return key

def save_key_to_file(key, filename="protected_key.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)
    print(f"[✔] Encryption key saved to '{filename}'")

def main():
    key = generate_key()
    print("[*] Your new Fernet encryption key (keep it secret!):")
    print(key.decode())  # Display for backup if needed
    save_key_to_file(key)

if __name__ == "__main__":
    main()
