from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Возвращает информацию об объекте класса в режиме отладки.

        :return: f-строка с информацией об объекте класса.
        """
        return f'{self.__class__.__name__}{self.name, self.price, self.quantity, self.number_of_sim}'
