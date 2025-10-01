# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить ее в новый текстовый файл.
# Функция для извлечения информации за 1857 год из файла
def extract_info_for_year(input_file, output_file, year):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.readlines()  # Читаем все строки из файла

    # Ищем блок информации за указанный год
    year_info = []
    is_year_section = False

    for line in content:
        if str(year) in line:  # Проверяем, есть ли год в строке
            is_year_section = True  # Начинаем собирать информацию за этот год
        elif is_year_section and line.strip() == "":  # Если встретили пустую строку, заканчиваем сбор
            break
        
        if is_year_section:
            year_info.append(line)

    # Записываем извлеченную информацию в новый файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(year_info)

# Задаем имена файлов
input_filename = 'Dostoevsky.txt'
output_filename = 'Dostoevsky_1857.txt'

# Извлекаем информацию за 1857 год
extract_info_for_year(input_filename, output_filename, 1857)

print(f"Информация за 1857 год была успешно извлечена в файл '{output_filename}'.")
