def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    if len(str_number) > 1:# Если длина строки больше 1, продолжаем работу
        first = int(str_number[0])  # Берем первую цифру
        return first * get_multiplied_digits(int(str_number[1:]))# Рекурсивно вызываем функцию с оставшимися цифрами
    else:
        return int(str_number)# Если остается одна цифра, просто возвращаем её

result = get_multiplied_digits(40203)
print(result)
