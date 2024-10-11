def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции:
print_params()                             # без аргументов
print_params(5)                            # только a
print_params(5, 'другая строка')    # a и b
print_params(5, 'другая строка', False)  # все аргументы
print_params(b=25)                         # только b
print_params(c=[1, 2, 3])                  # только c

values_list = [3.14, 'тестовая строка', False]  # Список
values_dict = {'a': 42, 'b': 'значение', 'c': 0}  # Словарь

# Вызов функции с распаковкой
print_params(*values_list)              # распаковка списка
print_params(**values_dict)             # распаковка словаря

# Новый список
values_list_2 = [54.32, 'Строка']

# Вызов функции с распаковкой списка и дополнительным аргументом
print_params(*values_list_2, 42)



