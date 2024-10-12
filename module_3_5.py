def get_multiplied_digits(number):
    str_number = str(number).lstrip('0')  # Удаляем нули из начала строки
    if str_number == '':  # Если строка пустая, возвращаем 1
        return 1
    first = int(str_number[0])  # Извлекаем первую цифру и преобразуем в int
    if len(str_number) > 1:         # Если длина строки больше 1, продолжаем рекурсию
        return first * get_multiplied_digits(
            int(str_number[1:]))  # Умножаем первую цифру на результат рекурсивного вызова
    else:
        return first  # Если длина 1, возвращаем первую цифру
result = get_multiplied_digits(420)# Пример использования функции
print(result)
