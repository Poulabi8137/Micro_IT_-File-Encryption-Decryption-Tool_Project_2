import os
from cryptography.fernet import Fernet

key_file = 'key.bin'

def get_key():
    if not os.path.exists(key_file):
        with open(key_file, 'wb') as kf:
            kf.write(Fernet.generate_key())
    return open(key_file, 'rb').read()

def lock(path):
    if not os.path.isfile(path):
        print("Missing file.")
        return

    key = get_key()
    f = Fernet(key)

    with open(path, 'rb') as src:
        stuff = src.read()

    locked = f.encrypt(stuff)

    with open(path + '.lock', 'wb') as out:
        out.write(locked)

    print(f"Encrypted: {path}")

def unlock(path):
    if not path.endswith('.lock'):
        print("Needs .lock file.")
        return

    key = get_key()
    f = Fernet(key)

    with open(path, 'rb') as src:
        locked = src.read()

    try:
        unlocked = f.decrypt(locked)
    except:
        print("Bad key or file.")
        return

    out_path = path.replace('.lock', '')
    with open(out_path, 'wb') as out:
        out.write(unlocked)

    print(f"Decrypted: {out_path}")

def main():
    print("Encrypt / Decrypt Tool\n")

    while True:
        cmd = input("1) Encrypt  2) Decrypt  3) Quit > ").strip()
        if cmd == '1':
            file = input("File to encrypt: ").strip()
            lock(file)
        elif cmd == '2':
            file = input("Encrypted file (.lock): ").strip()
            unlock(file)
        elif cmd == '3':
            break
        else:
            print("Invalid.\n")

if __name__ == '__main__':
    main()
