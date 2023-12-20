import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init(phone):
    assert phone.number_of_sim == 2


def test_repr(phone):
    """
    Проверяет работу метода repr.
    """
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
