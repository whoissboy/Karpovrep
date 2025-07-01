# Словарь с товарами в магазинах
stores = {
    "Магнит": {"молоко", "соль", "сахар", "печенье", "сыр"},
    "Пятерочка": {"мясо", "молоко", "сыр"},
    "Перекресток": {"молоко", "творог", "сыр", "сахар", "печенье"},
    "Лента": {"печенье", "молоко", "сыр"}
}

# 1. Определяем магазины, в которых нельзя приобрести соль
stores_without_salt = [store for store, products in stores.items() if "соль" not in products]

# 2. Определяем магазины, где можно приобрести одновременно молоко, печенье и сыр
stores_with_milk_cookie_cheese = [store for store, products in stores.items() if {"молоко", "печенье", "сыр"}.issubset(products)]

# 3. Определяем магазины, где можно приобрести мясо и молоко
stores_with_meat_and_milk = [store for store, products in stores.items() if {"мясо", "молоко"}.issubset(products)]

# Вывод результатов
print("Магазины, в которых нельзя приобрести соль:", stores_without_salt)
print("Магазины, где можно приобрести одновременно молоко, печенье и сыр:", stores_with_milk_cookie_cheese)
print("Магазины, где можно приобрести мясо и молоко:", stores_with_meat_and_milk)
