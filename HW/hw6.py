def guess_number():
    print("Загадай число от 1 до 100, а я попробую угадать!")
    low, high = 1, 100
    while low <= high:
        mid = (low + high) // 2
        print(f"Это {mid}?")
        answer = input("Введи 'больше' если больше, 'меньше' если меньше, 'да' если угадал: ")
        if answer == "да":
            print(f"Ура! Я угадал: {mid}")
            break
        elif answer == "больше":
            low = mid + 1
        elif answer == "меньше":
            high = mid - 1
    print("Спасибо за игру!")
guess_number()
