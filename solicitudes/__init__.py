import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import __main__
from cryptography.fernet import Fernet

password = b"password"
salt = b"slat_value"

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)

KEY = base64.urlsafe_b64encode(kdf.derive(password))
__main__.KEY = KEY
fernet = Fernet(KEY)
__main__.fernet = fernet

def encrypt_data(data):
    try:
        cipher = fernet.encrypt(data.encode())
    except:
        data = str(data)
        cipher = fernet.encrypt(data.encode())
    return cipher

def decrypt_data(data):
    data = data.encode()
    decrypted_data = None
    try:
        decrypted_data = fernet.decrypt(data).decode()
    except:
        decrypted_data = None
    return decrypted_data

__main__.encrypt_data = encrypt_data
__main__.decrypt_data = decrypt_data