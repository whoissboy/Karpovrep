# Задание 2: Выделение названия первого каталога из полного имени файла
def get_first_directory(file_path):
    # Разделяем путь на части по символу '\'
    parts = file_path.split('\\')
    
    # Проверяем, есть ли хотя бы один каталог
    if len(parts) > 1:
        # Возвращаем первый каталог
        return parts[1]
    else:
        # Если файл в корневом каталоге, возвращаем символ '\'
        return '\\'

# Пример использования функции
file_path = "C:\\Users\\Username\\Documents\\file.txt"
first_directory = get_first_directory(file_path)
print("Первый каталог:", first_directory)
