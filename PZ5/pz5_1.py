'''Вариант 11
Составить функцию, которая напечатает сорок любых символов.'''
def print_40_chars(char):
    for i in range(1, 40+1):
        print(char[0], i)
print_40_chars(input('Введите символ для печати: '))