from item import Item


class Phone(Item):
    """
    Класс для представления товара (телефона) в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, count_sim: int):
        """
        Создание экземпляра класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param count_sim: Количество поддерживаемых сим-карт
        """

        super().__init__(name, price, quantity)
        self.count_sim = count_sim

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            return None
