'''Вариант 11
Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).'''
while True:
    try:
        N = int(input("Введите число: "))
        if N < 0:
            print("Пожалуйста, введите положительное число.")
            continue
        break
    except ValueError:
        print("Неправильно ввели число!")
multiply = 1
for i in range(1, N + 1):
    multiply *= 1 + i / 10
print(f"Произведение равно {multiply}")