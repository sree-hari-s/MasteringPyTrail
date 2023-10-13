import base64, hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

choice = int(input("Encryption - 1, Decryption - 2 - "))


def gen_fernet_key(passcode: bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

if choice == 1:
    fileName = input("Enter filename with extension - ")
    file = open(fileName, "r")
    data = file.readlines()
    file.close()
    
    # doing encrypting stuff
    key = input("Enter Key = ")
    
    password= gen_fernet_key(key.encode("utf-8"))
    secretKey = Fernet(password)
    # print(secretKey)

    encrypted_data = {}
    i=1
    for lines in data:
        secret = secretKey.encrypt(lines.encode("utf-8"))
        encrypted_data[str(i)] = secret
        i += 1
    # print(encrypted_data)
    secretFile = input("Enter filename to store your encrypted data with extension (like encrypted.txt) - ")

    with open(secretFile, "wb") as f:
        for values in encrypted_data:
            f.write(encrypted_data[values])
            f.write(b"\n")

elif choice == 2:
    secretFile = input(
        "Enter filename in which the encrypted data is stored with extension - ")


    with open(secretFile, "rb") as f:
        secretData = f.readlines()
    
    key = input("Enter Key = ")
    password = gen_fernet_key(key.encode("utf-8"))
    secretKey = Fernet(password)

    decrypted_data =[]
    
    for lines in secretData:
        # print(type(lines))
        a =  secretKey.decrypt(lines.split(b"\n")[0]).decode()
        decrypted_data.append(a)

    fileName = input("Enter filename to store data with extension - ")
    with open(fileName, "w") as f:
        for lines in decrypted_data:
            f.write(lines)
