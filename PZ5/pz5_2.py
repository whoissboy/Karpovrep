'''Вариант 11
Описать функцию SortInc3(A, B, C), меняющую содержимое переменных A, B, C
таким образом, чтобы их значения оказались упорядоченными по возрастанию (A,
B, C — вещественные параметры, являющиеся одновременно входными и
выходными). С помощью этой функции упорядочить по возрастанию два данных
набора из трех чисел: (A1, B1, C1) и (A2, B2, C2).'''
def intcheck(x):
    while type(x) != int:
        try:
            return int(x)
        except ValueError:
            x = input(f'Неправильный ввод целого числа!\nПовторите ввод: ')

def SortInc3(A, B, C):
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A
    return A, B, C

for i in range(2):
    A = intcheck(input(f'Введите число A{i+1}: '))
    B = intcheck(input(f'Введите число B{i+1}: '))
    C = intcheck(input(f'Введите число C{i+1}: '))
    A, B, C = SortInc3(A, B, C)
    print(f'Отсортированный набор {i+1}: {A, B, C}')