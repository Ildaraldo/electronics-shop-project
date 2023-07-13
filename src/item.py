import csv


class InstantiateCSVError(Exception):
    """
    Класс для обработки исключений при повреждении файлов csv
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл csv повреждён'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Функция, возвращающая название товара
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Функция, задающая название товара
        """
        if len(name) <= 10:
            self.__name = name
        else:
            # raise Exception("Длина наименования товара превышает 10 символов.")
            print("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, filename):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        try:
            # чтение данных с файла .csv
            with open(filename, 'r', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)

                # при загрузке чистим список
                cls.all = []

                # создание экземпляров класса Item
                try:
                    for i, ex in enumerate(reader, start=1):
                        if not ex['name']:
                            raise InstantiateCSVError(f'В строке {i} отсутствует данные "name"')
                        elif not ex['price']:
                            raise InstantiateCSVError(f'В строке {i} отсутствует данные "price"')
                        elif not ex['quantity']:
                            raise InstantiateCSVError(f'В строке {i} отсутствует данные "quantity"')
                        else:
                            cls(ex['name'], ex['price'], ex['quantity'])

                except InstantiateCSVError as ex:
                    print(f'Файл {filename} поврежден\n{ex.__str__()}')

        except FileNotFoundError:
            print(f'Отсутствует файл {filename}')

    @staticmethod
    def string_to_number(string: str):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(string))


