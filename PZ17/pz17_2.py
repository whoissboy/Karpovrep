# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из № 2 - 9.
import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Ошибка: деление на ноль"
            else:
                result = num1 / num2
        else:
            result = "Неизвестная операция"
            
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа")

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x250")

# Поле для первого числа
label_num1 = ttk.Label(root, text="Первое число:")
label_num1.pack(pady=(10, 0))
entry_num1 = ttk.Entry(root)
entry_num1.pack(pady=5)

# Выбор операции
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]

operation_frame = ttk.Frame(root)
operation_frame.pack(pady=5)

for op in operations:
    rb = ttk.Radiobutton(
        operation_frame, 
        text=op, 
        variable=operation_var, 
        value=op
    )
    rb.pack(side="left", padx=5)

# Поле для второго числа
label_num2 = ttk.Label(root, text="Второе число:")
label_num2.pack(pady=(10, 0))
entry_num2 = ttk.Entry(root)
entry_num2.pack(pady=5)

# Кнопка расчета
calc_button = ttk.Button(root, text="Вычислить", command=calculate)
calc_button.pack(pady=10)

# Поле результата
result_label = ttk.Label(root, text="Результат: ")
result_label.pack(pady=5)

root.mainloop()
