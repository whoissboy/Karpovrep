# Создайте класс "Товар" с атрибутами "Название", "Цена" и "Количество". Реализуйте метод, который выводит информацию о товаре в формате "Название: название, Цена: цена, Количество: количество".
class Product:
    def __init__(self, name, price, quantity):
        """
        Инициализация атрибутов товара.
        
        :param name: Название товара
        :param price: Цена товара
        :param quantity: Количество товара
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """
        Метод для вывода информации о товаре.
        """
        info = f"Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}"
        print(info)

# Пример использования класса
if __name__ == "__main__":
    # Создаем экземпляр товара
    product1 = Product("Яблоко", 50, 10)
    product2 = Product("Молоко", 70, 5)

    # Выводим информацию о товарах
    product1.display_info()
    product2.display_info()
