# Micro_IT_-File-Encryption-Decryption-Tool_Project_2
# 🔐  File Encryption/Decryption Tool

A simple Python tool to securely **encrypt** and **decrypt** files using symmetric encryption.  
This utility protects sensitive data by locking and unlocking files with a secure key.

---

## 💡 Features

- Encrypt any file using a key.
- Decrypt `.lock` files back to the original version.
- Auto-generates and securely stores the encryption key.
- Easy-to-use CLI interface.

---

## 🧰 Built With

- 🐍 Python 3.x
- 🔐 `cryptography` library (Fernet symmetric encryption)
- 📂 `os` module for file handling

---

## ▶️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/Poulabi8137/FileLocker.gitcd FileLocker
2. **Install required library**
   ```bash
   pip install cryptography
3. **Run the program**
   ```bash
   python filelocker.py
4. **🔧 Usage**
     ```bash
    Select 1 to encrypt a file. Provide the path to the file you want encrypted. It will generate an encrypted file with a .lock extension.

    Select 2 to decrypt a .lock file. Provide the encrypted filename, and it will decrypt it to the original file.

    Select 3 to exit the program.
5. **🖼️ Screenshots**
    ```bash
    Encrypt / Decrypt Tool
   1) Encrypt  2) Decrypt  3) Quit > 1
   File to encrypt: example.txt
   Encrypted: example.txt
   1) Encrypt  2) Decrypt  3) Quit > 2
   Encrypted file (.lock): example.txt.lock
   Decrypted: example.txt
   1) Encrypt  2) Decrypt  3) Quit > 3
6. **📁 File Structure**
     ```bash
     FileLocker/
    │
    ├── filelocker.py   # Main encryption/decryption script
    ├── key.bin         # Automatically generated encryption key
    ├── README.md       # Project documentation
