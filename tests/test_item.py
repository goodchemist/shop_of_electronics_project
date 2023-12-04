import pytest
from src.item import Item


@pytest.fixture
def item_smartphone():
    return Item('Смартфон', 10000, 20)


def test_calculate_total_price(item_smartphone):
    """
    Проверяет общую стоимость конкретного товара в магазине
    """
    assert item_smartphone.calculate_total_price() == 200000


def test_quantity_not_int():
    """
    Проверяет задано ли количество товаров целым числом
    """
    with pytest.raises(ValueError):
        Item('Смартфон', 10000, 'abc')


def test_quantity_negative():
    """
    Проверяет больше ли количество товара 0 ед.
    """
    with pytest.raises(ValueError):
        Item('Смартфон', 10000, -2)


def test_price_not_number():
    """
    Проверяет задана ли цена товара в цифровом значении
    """
    with pytest.raises(ValueError):
        Item('Смартфон', 'abc', 20)


def test_price_negative():
    """
    Проверяет не нулевая или отрицательная стоимость товара
    """
    with pytest.raises(ValueError):
        Item('Смартфон', -1, 20)


def test_apply_discount(item_smartphone):
    """
    Проверяет работу функции apply_discount
    """
    Item.pay_rate = 0.5
    item_smartphone.apply_discount()
    assert item_smartphone.price == 5000.0
