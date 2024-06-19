import sqlite3

class DBManager:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')
        self.conn.commit()

    def register_user(self,username, password):
        if not username or not password:
            return False
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                       (username, password))
        existing_user = cursor.fetchone()
        if existing_user:
            False

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password))
        self.conn.commit()
        return True

    def check_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                       (username, password))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False