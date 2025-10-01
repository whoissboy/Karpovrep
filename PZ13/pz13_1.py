# В двумерном списке найти сумму и произведение элементов строки N (N задать с клавиатуры).
# Функция для создания двумерного списка (матрицы)
def create_matrix(rows, cols):
    return [[j + i * cols for j in range(cols)] for i in range(rows)]

# Функция для вычисления суммы и произведения элементов строки N
def sum_and_product_of_row(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        return None, None  # Если индекс строки вне диапазона

    row = matrix[row_index]
    row_sum = sum(row)
    row_product = 1
    for num in row:
        row_product *= num

    return row_sum, row_product

# Задаем размеры матрицы
rows = 4  # Количество строк
cols = 5  # Количество столбцов

# Создаем матрицу
matrix = create_matrix(rows, cols)

# Выводим матрицу
print("Матрица:")
for row in matrix:
    print(row)

# Запрашиваем у пользователя номер строки
N = int(input("Введите номер строки (0 - {}): ".format(rows - 1)))

# Вычисляем сумму и произведение элементов строки N
row_sum, row_product = sum_and_product_of_row(matrix, N)

# Выводим результаты
if row_sum is not None:
    print(f"Сумма элементов строки {N}: {row_sum}")
    print(f"Произведение элементов строки {N}: {row_product}")
else:
    print("Неверный номер строки.")
