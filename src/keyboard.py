from src.item import Item
from src.mixinLang import MixinLanguage


class KeyBoard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса KeyBoard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Раскладка клавиатуры
        """
        super().__init__(name, price, quantity)





