# Дана строка S. Вывести строку, содержащую символы строки S, между которыми вставлено по одному пробелу.
def insert_spaces(s):
    # Проверяем, что строка не пустая
    if not s:
        return ""
    
    # Используем метод join для вставки пробелов между символами
    spaced_string = ' '.join(s)
    return spaced_string

# Пример использования функции
input_string = "Привет"
result = insert_spaces(input_string)
print("Строка с пробелами:", result)
