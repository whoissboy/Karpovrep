import tkinter as tk
from tkinter import ttk

def submit_form():
    # Здесь можно добавить логику обработки данных формы
    print("Форма отправлена!")

# Создание основного окна
root = tk.Tk()
root.title("Contact Us")
root.geometry("400x500")
root.resizable(False, False)

# Заголовок формы
title_label = ttk.Label(root, text="Contact Us", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Создание фрейма для полей формы
form_frame = ttk.Frame(root)
form_frame.pack(padx=20, pady=10, fill="x")

# Поле First Name
first_name_label = ttk.Label(form_frame, text="First Name")
first_name_label.pack(anchor="w", pady=(0, 5))
first_name_entry = ttk.Entry(form_frame)
first_name_entry.pack(fill="x", pady=(0, 10))

# Поле Last Name
last_name_label = ttk.Label(form_frame, text="Last Name")
last_name_label.pack(anchor="w", pady=(0, 5))
last_name_entry = ttk.Entry(form_frame)
last_name_entry.pack(fill="x", pady=(0, 10))

# Поле Email address
email_label = ttk.Label(form_frame, text="Email address")
email_label.pack(anchor="w", pady=(0, 5))
email_entry = ttk.Entry(form_frame)
email_entry.pack(fill="x", pady=(0, 10))

# Поле Website
website_label = ttk.Label(form_frame, text="Website")
website_label.pack(anchor="w", pady=(0, 5))
website_entry = ttk.Entry(form_frame)
website_entry.insert(0, "www.example.com")
website_entry.pack(fill="x", pady=(0, 10))

# Поле Password
password_label = ttk.Label(form_frame, text="Password")
password_label.pack(anchor="w", pady=(0, 5))
password_entry = ttk.Entry(form_frame, show="*")
password_entry.pack(fill="x", pady=(0, 5))

# Подсказка для пароля
password_hint = ttk.Label(form_frame, text="8-10 characters", font=("Arial", 8))
password_hint.pack(anchor="w", pady=(0, 10))

# Поле Password Confirmation
password_conf_label = ttk.Label(form_frame, text="Password Confirmation")
password_conf_label.pack(anchor="w", pady=(0, 5))
password_conf_entry = ttk.Entry(form_frame, show="*")
password_conf_entry.pack(fill="x", pady=(0, 10))

# Подсказка для подтверждения пароля
password_conf_hint = ttk.Label(form_frame, text="Type your password again", font=("Arial", 8))
password_conf_hint.pack(anchor="w", pady=(0, 20))

# Кнопка Sign Up
signup_button = ttk.Button(root, text="Sign Up", command=submit_form)
signup_button.pack(pady=10)

root.mainloop()
