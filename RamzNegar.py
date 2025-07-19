import json
import os
from cryptography.fernet import Fernet


FILE_NAME = r'D:\pythonProject\RamzNegar\ramznegarjson.json'
KEY_FILE = r'D:\pythonProject\RamzNegar\key.key'  


def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        return key

key = load_key()
fernet = Fernet(key)

def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'rb') as f:
            encrypted_data = f.read()
        if encrypted_data:
            decrypted_data = fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode())
        else:
            return {}
    else:
        return {}

def save_passwords(data):
    json_data = json.dumps(data).encode()
    encrypted_data = fernet.encrypt(json_data)
    with open(FILE_NAME, 'wb') as f:
        f.write(encrypted_data)

print('Welcome to RamzNegar')
mydict = load_passwords()

def main():
    print('1. Password List \n2. Add Password \n3. Remove password \n4. Exit')
    a = int(input())
    return a

def add_password(pasokh):
    if pasokh == 1:
        keys = list(mydict.keys())
        for i in range(len(keys)):
            print(f"{i + 1}: {keys[i]}")
        print()
        password_show = int(input('If you want to see password, please write its Number:\n'))
        if 1 <= password_show <= len(keys):
            key = keys[password_show - 1]
            print(f"{key} : {mydict[key]}")
        else:
            print("Invalid number!")
        exit = int(input('Send 0 to Exit\n'))
        return exit
    elif pasokh == 2:
        name = input('Please send name: ')
        password = input('Please send Password: ')
        mydict[name] = password
        save_passwords(mydict)
        print('Your password has been registered.')
        print()
        exit = int(input('Send 0 to Exit\n'))
        return exit
    elif pasokh == 3:
        print(mydict)
        print()
        remove = str(input('Send its key:\n'))
        if remove in mydict:
            del mydict[remove]
            save_passwords(mydict)
            print('Your key has been removed')
        else:
            print('Key not found!')
        print()
        exit = int(input('Send 0 to Exit\n'))
        return exit
    elif pasokh == 4:
        return 4
    else:
        print('Sorry, Please send again')
        return 0

while True:
    pasokh = main()
    exit_val = add_password(pasokh)
    if exit_val == 0:
        continue
    elif exit_val == 4:
        break
