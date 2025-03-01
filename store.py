# *Дополнительное задание:
#
# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача —
# создать класс `Store`, который можно будет использовать для создания различных магазинов.
#
class Store():
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        if items is None:
            self.items = {}
        elif isinstance(items, dict):
            self.items = items
        else:
            raise ValueError("Ассортимент должен быть словарем, где ключ - название товара, а значение - его цена")

    #  метод для добавления товара в ассортимент.
    def add_item(self, new_item):
        print(f'Товар(ы) {new_item} добавлен(ы) в ассортимент магазина {self.name}.')
        self.items.update(new_item)

    # метод для удаления товара из ассортимента.
    def remove_item(self, removed_item):
        print(f'Товар {removed_item} удален из ассортимента магазина {self.name}.')
        self.items.pop(removed_item)

    # метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`
    def prise(self, item):
        print(f'Стоимость товара {item} - {self.items.get(item)}.')

    # метод для обновления цены товара
    def new_prise(self, item_new_prise):
        self.items.update(item_new_prise)

    # информация об ассортименте магазина
    def store_info(self):
        print()
        print(f'Ассортимент магазина {self.name}: ', self.items)
        print()

# Создаю несколько объектов класса `Store`:
store1 = Store("Овощи", "Москва", {'огурцы': 5, "помидоры": 10, "картофель": 3})
store2 = Store("Фрукты", "Москва", {'яблоки': 5, "бананы": 6, "Груши": 7})
store3 = Store('Книги', "Подольск")
store4 = Store("Цветы", "Климовск", {'розы': 10, "тюльпаны": 7, "ромашки": 5, "васильки": 5})

# добавяю в каждый из них несколько товаров

store1.add_item({"морковь": 1, "баклажан": 4})
store1.store_info()

store2.add_item({"апельсины": 8, "черешня": 9})
store2.store_info()

store3.add_item({"Тихий Дон т.1": 100, "Тихий Дон т.2": 110, "Мастер и Маргарита": 120})
store3.store_info()

store4.add_item({"хризантемы": 4, "гладиолусы": 6})
store4.store_info()

# Выбираю один из созданных магазинов и тестирую все его методы:
test_store = store1

# добавляю товар,
test_store.add_item({"свекла": 2, "лук": 1})
test_store.store_info()

# обновляю цену,
test_store.new_prise({"свекла": 3, "лук": 2})
test_store.store_info()

# убираю товар
test_store.remove_item('помидоры')
test_store.store_info()

# и запрашиваю цену.
test_store.prise('лук')
test_store.prise('помидоры')