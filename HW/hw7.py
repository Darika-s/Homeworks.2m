users = [
    (1, "Олег", 35),
    (2, "Егор", 33),
    (3, "Игорь", 32)
]

def get_user_by_id(user_id):
    for user in users:
        if user[0] == user_id:
            return f"{user[1]} {user[2]}"
    return "Пользователь с таким ID не найден"