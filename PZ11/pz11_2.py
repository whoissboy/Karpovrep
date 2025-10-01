
# 2. Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить строку
# наименьшей длины.

import string

# Функция для подсчета знаков препинания
def count_punctuation(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    punctuation_count = sum(1 for char in content if char in string.punctuation)
    return content, punctuation_count

# Функция для записи строки наименьшей длины в новый файл
def write_shortest_line_to_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Находим строку наименьшей длины
    shortest_line = min(lines, key=len).strip()
    
    with open(output_file, 'w') as f:
        f.write(shortest_line)

# Чтение файла и подсчет знаков препинания
text_file = 'text18-11.txt'  # Предполагается, что этот файл уже существует
content, punctuation_count = count_punctuation(text_file)

# Выводим содержимое файла и количество знаков препинания
print("Содержимое файла:")
print(content)
print("Количество знаков препинания:", punctuation_count)

# Записываем строку наименьшей длины в новый файл
shortest_line_file = 'shortest_line.txt'
write_shortest_line_to_file(text_file, shortest_line_file)

print(f"Строка наименьшей длины записана в файл '{shortest_line_file}'.")
