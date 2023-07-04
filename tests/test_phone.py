"""Здесь надо написать тесты с использованием pytest для модуля phone"""
import pytest

from src.phone import Phone
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone14", 20000, 15, 1)


def test_add():
    print("awdawd")
    """Тестирование функции '__add__'"""
    assert phone1 + item1 == 35
    assert phone1 + 0 == None


def test_repr():
    """Тестирование функции '__repr__'"""
    assert repr(phone1) == "Phone('iPhone14', 20000, 15, 1)"


def test_number_of_sim():
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2

    # тестирование исключения
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0





