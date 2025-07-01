import string

# Заданная строка
input_string = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'

# Функция для извлечения символов пунктуации
def extract_punctuation(s):
    return ''.join(char for char in s if char in string.punctuation)

# Извлекаем символы пунктуации
punctuation_chars = extract_punctuation(input_string)

# Вывод результатов
print("Символы пунктуации из строки:", punctuation_chars)
