import sqlite3

def setup_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    cursor.executemany("""
        INSERT INTO users (name, age) VALUES (?, ?)
    """, [("Олег", 35), ("Егор", 33), ("Игорь", 32)])

    conn.commit()
    conn.close()

if __name__ == "_main_":
    setup_database()

import sqlite3

def get_user(index):
    """
    Функция принимает индекс пользователя и выводит его имя и возраст.
    :param index: int - порядковый номер пользователя
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, age FROM users WHERE id = ?", (index,))
    user = cursor.fetchone()

    conn.close()

    if user:
        print(f"{user[0]} {user[1]}")
    else:
        print("Пользователь с таким номером не найден.")

if __name__ == "_main_":
    get_user(2)