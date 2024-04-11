import sqlite3 as sql


class Database:
    USERS_TABLE = 'users'
    KEYCHAIN_TABLE = 'keychain'

    def __init__(self, db_name='data') -> None:
        self.conn = sql.connect(f"{db_name}.sqlite")
        self.cursor = self.conn.cursor()

        self._create_table(
            self.USERS_TABLE, 
            'id INTEGER PRIMARY KEY, username TEXT, email UNIQUE, password TEXT'
        )

        self._create_table(
            self.KEYCHAIN_TABLE, 
            f'id INTEGER PRIMARY KEY, name TEXT, password TEXT, user INTEGER, FOREIGN KEY(user) REFERENCES {self.USERS_TABLE}(id)'
        )

    def _create_table(self, table_name, columns) -> None:
        STATEMENT = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

        self.cursor.execute(STATEMENT)
        self.conn.commit()

    def add_user(self, user, email, password) -> None:
        pass

    def get_user(self, email) -> tuple:
        pass
    
    def add_password(self, name, password, email) -> None:
        pass

    def __del__(self) -> None:
        self.conn.close()