 import random

# Генерация последовательности целых положительных и отрицательных чисел
def generate_numbers_file(filename, count):
    with open(filename, 'w') as f:
        numbers = [random.randint(-100, 100) for _ in range(count)]
        f.write(' '.join(map(str, numbers)))

# Обработка данных из файла
def process_numbers_file(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))

    # Подсчет необходимых данных
    total_count = len(numbers)
    min_element = min(numbers)
    positive_count_first_half = sum(1 for x in numbers[:total_count // 2] if x > 0)

    # Запись результатов в новый файл
    with open(output_filename, 'w') as f:
        f.write("Исходные данные:\n")
        f.write(' '.join(map(str, numbers)) + '\n')
        f.write(f"Количество элементов: {total_count}\n")
        f.write(f"Минимальный элемент: {min_element}\n")
        f.write(f"Количество положительных элементов в первой половине: {positive_count_first_half}\n")

# Генерируем файл с числами
input_filename = 'numbers.txt'
generate_numbers_file(input_filename, 20)

# Обрабатываем файл и создаем новый
output_filename = 'processed_numbers.txt'
process_numbers_file(input_filename, output_filename)

print(f"Файл '{output_filename}' успешно создан.")
