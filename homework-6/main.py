from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('../src/items_1.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('../tests/items_test_3.csv')
    # InstantiateCSVError: Файл item.csv поврежден
