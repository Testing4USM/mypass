import sqlite3 as sql
from hashlib import md5
from utils import encrypt
from utils import decrypt

class Database:
    USERS_TABLE = 'users'
    KEYCHAIN_TABLE = 'keychain' 

    def __init__(self, db_name='data') -> None:
        self.conn = sql.connect(f"{db_name}.sqlite")
        self.cursor = self.conn.cursor()

        self._create_table(
            self.USERS_TABLE, 
            'id INTEGER PRIMARY KEY, username TEXT, email TEXT UNIQUE, password TEXT'
        )

        self._create_table(
            self.KEYCHAIN_TABLE, 
            f'id INTEGER PRIMARY KEY, name TEXT UNIQUE, password TEXT, user INTEGER, FOREIGN KEY(user) REFERENCES {self.USERS_TABLE}(id)'
        )

    def _create_table(self, table_name, columns) -> None:
        STATEMENT = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

        self.cursor.execute(STATEMENT)
        self.conn.commit()

    def create_user(self, user, email, password) -> None:
        hashed_password = md5(password.encode()).hexdigest()
        statement = f"INSERT INTO {self.USERS_TABLE} (username, email, password) VALUES (?, ?, ?)"

        try:
            self.cursor.execute(statement, (user, email, hashed_password))
            self.conn.commit()
        except sql.IntegrityError:
            print("User already exists")

    def login_user(self, email, password) -> tuple:
        hashed_password = md5(password.encode()).hexdigest()
        statement = f"SELECT * FROM {self.USERS_TABLE} WHERE email = ? AND password = ?"

        self.cursor.execute(statement, (email, hashed_password))
        user = self.cursor.fetchone()

        return user
    
    def add_password(self, id, name, password: str) -> None:
        token = encrypt(password)
        statement = f"INSERT INTO {self.KEYCHAIN_TABLE} (name, password, user) VALUES (?, ?, ?)"

        try:
            self.cursor.execute(statement, (name, token, id))
            self.conn.commit()
        except sql.IntegrityError:
            print("Password already exists")

        return token
    
    def get_passwords(self, id) -> list:
        statement = f"SELECT id, name, password FROM {self.KEYCHAIN_TABLE} WHERE user = ?"

        self.cursor.execute(statement, (id,))
        passwords = self.cursor.fetchall()

        return passwords
    
    def change_password(self, name, password) -> None:
        token = encrypt(password)
        statement = f"UPDATE {self.KEYCHAIN_TABLE} SET password = ? WHERE name = ?"

        self.cursor.execute(statement, (token, name))
        self.conn.commit()

    def delete_password(self, name) -> None:
        statement = f"DELETE FROM {self.KEYCHAIN_TABLE} WHERE name = ?"

        self.cursor.execute(statement, (name,))
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()