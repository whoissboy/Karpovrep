'''Вариант 11
Дано целое число N (> 1). Найти наименьшее целое число K, при котором
выполняется неравенство 3К > N'''
while True:
    try:
        N = int(input("Введите число: "))
        if N <= 1:
            print("Число должно быть больше 1!")
        else:
            K = 1
            while 3 * K <= N:
                K += 1
            print("Наименьшее целое число K:", K)
            break
    except ValueError:
        print("Неправильно ввели число!")