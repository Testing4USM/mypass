from cryptography.fernet import Fernet
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def encrypt(password: str) -> str:
    """
    Encrypts a password using the TOKEN_KEY environment variable.

    :param password: The password to be encrypted.
    :type password: str

    :return: The encrypted password.
    :rtype: str
    """
    key = getenv("TOKEN_KEY")

    if not key:
        raise ValueError("TOKEN_KEY environment variable not set.")
    
    encoded_password = password.encode()

    return Fernet(key.encode()).encrypt(encoded_password).decode()

def decrypt(encoded_password: str) -> str:
    """
    Decrypts an encoded password using the TOKEN_KEY environment variable.

    :param encoded_password: The encoded password to be decrypted.
    :type encoded_password: str

    :return: The decrypted password.
    """
    key = getenv("TOKEN_KEY")

    if not key:
        raise ValueError("TOKEN_KEY environment variable not set.")

    encoded_password = encoded_password.encode()

    return Fernet(key.encode()).decrypt(encoded_password).decode()

def get_logfile():
    """
    Returns the logger object.

    :return: The logger object.
    """
    log_file = getenv("LOG_FILE")

    if not log_file:
        raise ValueError("LOG_FILE environment variable not set.")

    return log_file