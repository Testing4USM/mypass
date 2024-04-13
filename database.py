import sqlite3 as sql

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

    def create_user(self, user, email, password) -> bool:
        statement = f"INSERT INTO {self.USERS_TABLE} (username, email, password) VALUES (?, ?, ?)"

        try:
            self.cursor.execute(statement, (user, email, password))
            self.conn.commit()

            return True
        except sql.IntegrityError:
            return False

    def login_user(self, email, password) -> tuple:
        statement = f"SELECT * FROM {self.USERS_TABLE} WHERE email = ? AND password = ?"

        self.cursor.execute(statement, (email, password))
        user = self.cursor.fetchone()

        return user
    
    def add_password(self, id, name, password: str) -> tuple:
        statement = f"INSERT INTO {self.KEYCHAIN_TABLE} (name, password, user) VALUES (?, ?, ?)"

        try:
            self.cursor.execute(statement, (name, password, id))
            self.conn.commit()
        except sql.IntegrityError:
            return (False, None)

        return (True, password)
    
    def get_passwords(self, id) -> list:
        statement = f"SELECT id, name, password FROM {self.KEYCHAIN_TABLE} WHERE user = ?"

        self.cursor.execute(statement, (id,))
        passwords = self.cursor.fetchall()

        return passwords
    
    def change_password(self, name, password) -> None:
        statement = f"UPDATE {self.KEYCHAIN_TABLE} SET password = ? WHERE name = ?"

        self.cursor.execute(statement, (password, name))
        self.conn.commit()

    def delete_password(self, name) -> None:
        statement = f"DELETE FROM {self.KEYCHAIN_TABLE} WHERE name = ?"

        self.cursor.execute(statement, (name,))
        self.conn.commit()

    def __del__(self) -> None:
        self.conn.close()