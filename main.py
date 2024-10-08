def generate_password(number):
    password = ""
    pairs = []
    # Генерируем пары чисел от 1 до 10
    for i in range(1, 11):
        for j in range(i + 1, 11):  # чтобы избежать дубликатов (1,2) и (2,1)
            pair_sum = i + j
            # Проверяем кратность
            if pair_sum != 0 and number % pair_sum == 0:
                pairs.append((i, j))
    # Формируем пароль
    for pair in pairs:
        password += str(pair[0]) + str(pair[1])
    return password
number = 9  # Например, число из первой вставки
password = generate_password(number)
print(password)
