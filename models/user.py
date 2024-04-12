class User:
    def __init__(self, database) -> None:
        self.id = None
        self.username = None
        self.email = None

        self.db = database

    def login(self, email, password) -> bool:
        user = self.db.login_user(email, password)
        
        if user:
            self.id, self.username, self.email, _ = user
            self.keychain = KeyChain(self)
            return True

        return False
    
    def register(self, username, email, password) -> bool:
        try:
            self.db.create_user(username, email, password)
            self.login()
            return True
        except Exception as e:
            return False


    def __str__(self) -> str:
        return f"User: {self.username} - {self.email}"

    def __repr__(self) -> str:
        return f"User: {self.username} - {self.email}"
    
class KeyChain:
    def __init__(self, user: User) -> None:
        self.user = user
        self.db = user.db

        self.passwords = dict()

        passwords = self.db.get_passwords(self.user.id)

        for password in passwords:
            _, name, token = password
            self.passwords[name] = token

    def add_password(self, name, password) -> None:
        id = self.user.id

        self.db.add_password(id, name, password)
        self.passwords[name] = password

    def get_password(self, name) -> str:
        return self.passwords.get(name, None)
    
    def change_password(self, name, password) -> None:
        self.db.change_password(name, password)
        self.passwords[name] = password

    def delete_password(self, name) -> None:
        self.db.delete_password(name)
        del self.passwords[name]

    def __str__(self) -> str:
        return f"KeyChain: {self.id}"

    def __repr__(self) -> str:
        return f"KeyChain: {self.id}"