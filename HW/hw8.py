import sqlite3


def connect_or_create_db():
    return sqlite3.connect('user_with_grades.db')

def get_user_with_inner_join():
    connect = connect_or_create_db()
    cursor = connect.cursor()

    cursor.execute('''
        SELECT users.fio, users.age, grades.subject, grades.grade
        FROM users
        INNER JOIN grades ON users.userid = grades.userid
    ''')

    rows = cursor.fetchall()

    print("Результаты INNER JOIN:")
    for row in rows:
        print(row)

    connect.close()

get_user_with_inner_join()