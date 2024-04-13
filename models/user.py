from utils import decrypt
from utils import encrypt
from hashlib import md5

class User:
    def __init__(self, database) -> None:
        self.id = None
        self.username = None
        self.email = None

        self.db = database

    def login(self, email: str, password: str) -> bool:
        """
        Login a user with the given email and password.

        :param email: The email of the user.
        :param password: The password of the user.

        :return: True if the user is logged in, False otherwise.
        """
        hashed_password = md5(password.encode()).hexdigest()
        user = self.db.login_user(email, hashed_password)
        
        if user:
            self.id, self.username, self.email, _ = user
            self.keychain = KeyChain(self)
            return True

        return False
    
    def register(self, username: str, email: str, password: str) -> bool:
        """
        Register a user with the given username, email and password.

        :param username: The username of the user.
        :param email: The email of the user.
        :param password: The password of the user.

        :return: True if the user is registered, False otherwise.
        """
        hashed_password = md5(password.encode()).hexdigest()
        created = self.db.create_user(username, email, hashed_password)

        if not created:
            return False
        
        self.login(email, password)
        return True
    
class KeyChain:
    def __init__(self, user: User) -> None:
        self.user = user
        self.db = user.db

        self.passwords = dict()

        passwords = self.db.get_passwords(self.user.id)

        for password in passwords:
            _, name, token = password
            self.passwords[name] = token

    def add_password(self, name, password) -> bool:
        """
        Add a password to the keychain.

        :param name: The name of the password.
        :param password: The password to add.
        """
        id = self.user.id
        token = encrypt(password)

        created, encrpyted_password = self.db.add_password(id, name, token)
        
        if not created:
            return False

        self.passwords[name] = encrpyted_password
        return True

    def get_password(self, name) -> str:
        """
        Get a password from the keychain.

        :param name: The name of the password.

        :return: The password if it exists, None otherwise.
        """
        token = self.passwords.get(name, None)
        return decrypt(token) if token else None
    
    def change_password(self, name, password) -> None:
        """
        Change a password in the keychain.

        :param name: The name of the password.
        :param password: The new password.       
        """
        token = encrypt(password)

        if name not in self.passwords:
            return

        self.db.change_password(name, token)
        self.passwords[name] = token

    def delete_password(self, name) -> None:
        """
        Delete a password from the keychain.

        :param name: The name of the password.
        """
        if name not in self.passwords:
            return

        self.db.delete_password(name)
        del self.passwords[name]