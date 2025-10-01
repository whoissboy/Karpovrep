# 1. В последовательности из n целых чисел найти и вывести:
#     1. Минимальный среди положительных
#     2. Элементы кратные пяти
#     3. Их среднее арифметическое
import random

# Генерация последовательности целых чисел
def generate_numbers(n):
    return [random.randint(-100, 100) for _ in range(n)]

# Обработка последовательности
def process_numbers(numbers):
    # 1. Минимальный среди положительных
    positive_numbers = [num for num in numbers if num > 0]
    min_positive = min(positive_numbers) if positive_numbers else None

    # 2. Элементы, кратные пяти
    multiples_of_five = [num for num in numbers if num % 5 == 0]

    # 3. Среднее арифметическое элементов, кратных пяти
    average_of_multiples_of_five = sum(multiples_of_five) / len(multiples_of_five) if multiples_of_five else None

    return min_positive, multiples_of_five, average_of_multiples_of_five

# Генерируем последовательность из 20 целых чисел
n = 20
numbers = generate_numbers(n)

# Обрабатываем последовательность
min_positive, multiples_of_five, average_of_multiples_of_five = process_numbers(numbers)

# Вывод результатов
print("Сгенерированные числа:", numbers)
print("Минимальный положительный элемент:", min_positive)
print("Элементы, кратные пяти:", multiples_of_five)
print("Среднее арифметическое элементов, кратных пяти:", average_of_multiples_of_five)
