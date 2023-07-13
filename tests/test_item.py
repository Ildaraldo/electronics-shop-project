"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item
from src.item import InstantiateCSVError

item1 = item.Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    """
    Тестирование функции 'calculate_total_price' класса 'Item'"""
    assert item1.calculate_total_price() == 200_000


def test_apply_discount():
    """
    Тестирование функции 'apply_discount' класса 'Item'"""
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8_000


def test_string_to_number():
    assert item.Item.string_to_number('5') == 5


def test_name():
    # изменение наименования товара
    item1.name = 'Nokia'
    assert item1.name == 'Nokia'

    # длина наименования товара больше 10 символов
    item1.name = 'СуперСмартфон'
    assert item1.name == 'Nokia'

    item.Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(item.Item.all) == 5  # в файле 5 записей с данными по товарам


def test_repr():
    """Тестирование функции '__repr__'"""
    item2 = item.Item("Смартфон", 10000, 20)
    assert repr(item2) == "Item('Смартфон', 10000, 20)"


def test_str():
    item2 = item.Item("Смартфон", 10000, 20)
    assert str(item2) == 'Смартфон'


def test_add():
    item2 = item.Item("Смартфон", 10000, 20)

    assert item1 + item2 == 40
    assert item1 + 0 == None


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        item.Item.instantiate_from_csv('aaa.csv')

    with pytest.raises(InstantiateCSVError):
        item.Item.instantiate_from_csv('tests/items_test_1.csv')

    with pytest.raises(InstantiateCSVError):
        item.Item.instantiate_from_csv('tests/items_test_2.csv')

    with pytest.raises(InstantiateCSVError):
        item.Item.instantiate_from_csv('tests/items_test_3.csv')
