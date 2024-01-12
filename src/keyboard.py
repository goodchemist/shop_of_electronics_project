from src.item import Item


class Language:

    def __init__(self):
        """
        Инициализатор класса-миксина Language, который помогает создать экземпляр класса Keyboard,
        вызвав родительский класс Item.
        Параметр 'language' по умолчанию - английский (EN).
        """
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self) -> None:
        """
        Mетод для изменения языка (раскладки клавиатуры) - параметр 'language'.
        Всего поддерживается два языка: EN и RU.
        :return: None
        """
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, Language):

    def __init__(self, name: str, price: float | int, quantity: int):
        """
        Создание экземпляра класса Keyboard.
        Параметр 'language' по умолчанию - английский (EN).

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        Language.__init__(self)
