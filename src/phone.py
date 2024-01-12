from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float | int, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название телефона.
        :param price: Цена за 1 шт.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество SIM-карт.
        """

        super().__init__(name, price, quantity)

        if not isinstance(number_of_sim, int):
            raise ValueError('Number of physical SIM-cards must be an integer.')
        elif number_of_sim <= 0:
            raise ValueError('Number of physical SIM-cards must be greater than 0.')

        self._number_of_sim = number_of_sim

    def __repr__(self):
        """
        Возвращает информацию об объекте класса в режиме отладки.

        :return: f-строка с информацией об объекте класса
        """
        return f'{self.__class__.__name__}{self.name, self.price, self.quantity, self.number_of_sim}'

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim: int) -> None:
        """
        Устанавливает новое количество сим-карт.

        :param new_number_of_sim: новое количество сим-карт
        """
        if not isinstance(new_number_of_sim, int) or new_number_of_sim <= 0:
            raise ValueError('Number of physical SIM-cards must be an integer and greater than 0.')
        self._number_of_sim = new_number_of_sim
