# В двумерном списке найти сумму элементов второй половины матрицы.
# Функция для вычисления суммы элементов второй половины матрицы
def sum_of_second_half(matrix):
    total_sum = 0
    total_elements = len(matrix) * len(matrix[0])
    half_index = total_elements // 2

    # Пробегаем по всем элементам матрицы и суммируем элементы второй половины
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i * len(matrix[i]) + j >= half_index:
                total_sum += matrix[i][j]

    return total_sum

# Вычисляем сумму элементов второй половины матрицы
second_half_sum = sum_of_second_half(matrix)

# Выводим результат
print("Сумма элементов второй половины матрицы:", second_half_sum)
