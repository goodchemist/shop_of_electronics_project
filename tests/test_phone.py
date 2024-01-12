import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init(phone):
    """
    Проверяет работу метода __init__.
    """
    assert phone.number_of_sim == 2


def test_repr(phone):
    """
    Проверяет работу метода repr.
    """
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim_init_not_int():
    """
    Проверяет задано ли количество  SIM-карт целым числом.
    """
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, '2')


def test_number_of_sim_init_less_one():
    """
    Проверяет задано ли количество SIM-карт > 0.
    """
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, 0)


def test_number_of_sim_setter_less_one(phone):
    """
    Проверяет можно ли установить количество SIM-карт < 0 через setter.
    """
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_number_of_sim_setter_not_int(phone):
    """
    Проверяет можно ли установить количество SIM-карт не в формате integer через setter.
    """
    with pytest.raises(ValueError):
        phone.number_of_sim = 'abc'


def test_number_of_sim_setter(phone):
    """
    Проверяет установлено ли новое количество SIM-карт через setter.
    """
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
