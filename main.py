calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if string == item.lower():
            return True
    return False
print(string_info('Capybara')) # Пример вызова string_info
print(string_info('Armageddon')) # Пример вызова string_info
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Пример вызова is_contains
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
