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
        self.name = name

        if not isinstance(price, float):
            if not isinstance(price, int):
                raise ValueError('price have to be float or int')
        if price <= 0:
            raise ValueError('price have to be more than 0')
        self.price = price

        if not isinstance(quantity, int):
            raise ValueError('quantity have to be int')
        elif quantity <= 0:
            raise ValueError('quantity have to be more than 0')
        self.quantity = quantity

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
        pass
