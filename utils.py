from cryptography.fernet import Fernet
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def encrypt(password: str) -> str:
    key = getenv("TOKEN_KEY").encode()
    encoded_password = password.encode()

    return Fernet(key).encrypt(encoded_password).decode()

def decrypt(encoded_password: str) -> str:
    key = getenv("TOKEN_KEY").encode()
    encoded_password = encoded_password.encode()

    return Fernet(key).decrypt(encoded_password).decode()