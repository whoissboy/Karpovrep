# Приложение командировочных расходов для автоматизированного финансового контроля на предприятии. Должна содержать таблицу статей расходов, имеющую следующую структуру записей: № приказа, Дата, Место командировки, Опалата, Аванс, Вид расходов, Сумма расходов.
import sqlite3

# Функция для создания базы данных и таблицы
def create_database():
    conn = sqlite3.connect('expenses.db')  # Создаем или открываем базу данных
    cursor = conn.cursor()
    
    # Создаем таблицу, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number TEXT NOT NULL,
            surname TEXT NOT NULL,
            travel_place TEXT NOT NULL,
            payment REAL NOT NULL,
            advance REAL NOT NULL,
            expense_type TEXT NOT NULL,
            expense_amount REAL NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Функция для добавления записи о расходах
def add_expense(order_number, surname, travel_place, payment, advance, expense_type, expense_amount):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO expenses (order_number, surname, travel_place, payment, advance, expense_type, expense_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (order_number, surname, travel_place, payment, advance, expense_type, expense_amount))
    
    conn.commit()
    conn.close()

# Функция для отображения всех записей
def display_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    
    print("№ Приказа | Фамилия | Место командировки | Оплата | Аванс | Вид расходов | Сумма расходов")
    print("-------------------------------------------------------------------------------------")
    for row in rows:
        print(f"{row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]}")
    
    conn.close()

# Функция для поиска записей по фамилии
def search_expenses_by_surname(surname):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM expenses WHERE surname = ?', (surname,))
    rows = cursor.fetchall()
    
    print(f"Записи для фамилии '{surname}':")
    print("№ Приказа | Фамилия | Место командировки | Оплата | Аванс | Вид расходов | Сумма расходов")
    print("-------------------------------------------------------------------------------------")
    for row in rows:
        print(f"{row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]}")
    
    conn.close()

# Основная программа
if __name__ == "__main__":
    create_database()  # Создаем базу данных и таблицу

    # Пример добавления записей
    add_expense("001", "Иванов И.И.", "Москва", 1000.0, 200.0, "Транспорт", 800.0)
    add_expense("002", "Петров П.П.", "Санкт-Петербург", 1500.0, 300.0, "Проживание", 1200.0)

    # Отображаем все записи
    display_expenses()

    # Поиск записей по фамилии
    search_expenses_by_surname("Иванов И.И.")
