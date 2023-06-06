"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src import item

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

