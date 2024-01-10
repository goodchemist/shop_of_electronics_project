import csv
import os


class InstantiateCSVError(Exception):
    pass


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
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError('name is not correct')

        if not isinstance(price, float | int):
            raise ValueError('price have to be float or int')

        if price <= 0:
            raise ValueError('price have to be more than 0')
        self.price = price

        if not isinstance(quantity, int):
            raise ValueError('quantity have to be int')
        elif quantity <= 0:
            raise ValueError('quantity have to be more than 0')
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        """
        Возвращает информацию об объекте класса в режиме отладки

        :return: f-строка с информацией об объекте класса
        """
        return f'{self.__class__.__name__}{self.name, self.price, self.quantity}'

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователя
        :return: f-строка с информацией об объекте класса
        """
        return f'{self.name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
            # Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_sum = self.price * self.quantity
        return total_sum

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path_to_file=None) -> None:
        """
        Kласс-метод, инициализирующий экземпляры класса Item данными из файла csv-формата

        :param path_to_file: путь до файла csv
        """
        if path_to_file is None:
            path_to_file = os.path.join(os.path.dirname(__file__), 'items.csv')

        cls.all = []

        items = []

        with open(path_to_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for item in reader:
                items.append(item)

        for item in items:
            if item.get('name') and item.get('price') and item.get('quantity'):
                cls(item['name'], float(item['price']), int(item['quantity']))
            else:
                raise InstantiateCSVError('Файл item.csv поврежден.')

    @staticmethod
    def string_to_number(number_in_string) -> int:
        """
        статический метод, возвращающий число из числа-строки
        :param number_in_string: числo-строкa
        :return: число
        """
        number_in_int = int(float(number_in_string))
        return number_in_int

    def __add__(self, other) -> int:
        """
        Складывает количество двух товаров.
        :param other: товар после знака +
        :return: общее количество двух товаров
        """
        if issubclass(other.__class__, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        raise Exception
