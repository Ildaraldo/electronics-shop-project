from src.item import Item


class Phone(Item):
    """
    Класс для представления товара (телефона) в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт
        """

        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if issubclass(self.__class__, other.__class__) or issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            return None

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Функция, возвращающая количество поддерживаемых сим-карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        """
        Функция, задающая количество поддерживаемых сим-карт
        """
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество поддерживаемых сим-карт должно быть больше нуля!")
