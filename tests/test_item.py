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


def test_name_not_str():
    """
    Проверяет
    """
    with pytest.raises(ValueError):
        Item(1111, 10000, 5)


def test_name_is_not_alpha():
    """
    Проверяет
    """
    with pytest.raises(ValueError):
        Item('Apple123', 10000, 5)


def test_getter_name(item_smartphone):
    """
    Проверяет вывод приватного атрибута name
    """
    item_smartphone.name = 'Смартфон'


def test_setter_name(item_smartphone):
    """
    Проверяет работу сеттера атрибута name
    """
    item_smartphone.name = 'Телефон'
    assert item_smartphone.name == 'Телефон'

    item_smartphone.name = 'СуперСмартфон'
    assert item_smartphone.name == 'СуперСмарт'


def test_instantiate_from_csv():
    """
    Проверяет работу по созданию экзепляров класса Item из csv-файла
    """
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
