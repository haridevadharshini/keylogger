# 🔐 Ethical Keylogger PoC (Internship Project)

> ⚠️ **DISCLAIMER:**
> This project is strictly for **educational, ethical, and authorized use only**.
> Use it **only** on your own machine or with **explicit permission** in secure, controlled environments.

---

## 📋 Project Overview:

This is an **Ethical Proof-of-Concept Keylogger** designed for educational purposes, demonstrating:

* Secure keystroke logging.
* Encryption of captured keystrokes.
* Password-protected decryption of logs.
* Local simulation of data exfiltration (file copy, no networking).

---

## ✅ Features:

* Logs keystrokes from your system using `pynput`.
* Encrypts all logs securely with **Fernet encryption** (`cryptography` library).
* Supports decryption with password protection.
* Handles `[space]`, `[enter]`, `[tab]`, and `[backspace]` properly.
* Automatically splits logs into files by timestamp.
* Kill switch using the **ESC key** (stops the logger safely).
* Simulates "exfiltration" by copying logs to a local file (for ethical demonstration only).
* Designed for **educational cybersecurity internships, research, or ethical hacking labs**.

---

## 📂 Project Files:

```
keylogger.py         - Main keylogger script (captures & encrypts keystrokes)
decrypt_logs.py      - Decrypts encrypted logs (password-protected)
protect_key.py       - Generates new encryption key (run this first)
README.md            - Project documentation
.gitignore           - Prevents sensitive files from being uploaded to GitHub
```

---

## ⚙️ Setup Instructions:

### 1. Clone This Repository:

```bash
git clone https://github.com/your-username/ethical-keylogger.git
cd ethical-keylogger
```

### 2. Install Required Python Libraries:

```bash
pip install -r requirements.txt
```

#### `requirements.txt` content:

```
pynput
cryptography
```

### 3. Generate Your Own Encryption Key:

⚠️ This key will be used for encryption/decryption.

```bash
python protect_key.py
```

* This creates `protected_key.key` (keep it secret; it is ignored by `.gitignore`).
* Save the printed key somewhere secure for backup.

---

## 📝 Usage Guide:

### ▶️ Start the Keylogger (Ethically):

```bash
python keylogger.py
```

* It starts logging your keystrokes.
* Logs will be encrypted automatically in the `logs/` folder.
* Press `ESC` to safely stop the logger.

### ▶️ Decrypt Logs (Password Protected):

```bash
python decrypt_logs.py
```

* Enter the password (default: `root`; you can change it inside the script).
* It will decrypt logs from the `logs/` folder and display readable text.
* Keystrokes like `[space]`, `[enter]`, and `[backspace]` are handled correctly.

---

## 🚫 Security Precautions:

* NEVER upload or share `protected_key.key` or your actual encrypted logs.
* GitHub `.gitignore` prevents these sensitive files from being pushed accidentally.
* Always use this tool **responsibly** for learning, ethical testing, or approved research.

---

## 💡 Important Notes:

* You can regenerate a new key anytime by running `protect_key.py`.
* Anyone cloning this repo can generate their **own** keys & logs.
* Password can be changed in `decrypt_logs.py` under:

```python
correct_password = "root"
```

---

## ✅ Example Workflow (Internship Submission):

1. Clone the repo.
2. Install libraries from `requirements.txt`.
3. Generate encryption key.
4. Run the keylogger.
5. Decrypt logs using password.
6. Simulate "safe exfiltration" (optional).
7. Submit GitHub repo link.

---

## 📜 License & Legal:

This software is for **learning, ethical hacking training, and research purposes** only.
Do **NOT** use this tool on machines you don’t own or without explicit permission.

---

## 👩‍💼 Developed By:

**Hari Devadharshini**
Internship Project — 2025
