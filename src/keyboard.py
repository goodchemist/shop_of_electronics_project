from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float | int, quantity: int):
        """
        Создание экземпляра класса Keyboard.
        param 'language' по умолчанию - английский (EN).

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.

        """
        super().__init__(name, price, quantity)

        self.__language = 'EN'

    @property
    def language(self):
        return self.__language
