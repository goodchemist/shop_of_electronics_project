import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(keyboard):
    """
    Проверяет работу метода __init__.
    """
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'


def test_change_lang(keyboard):
    """
    Тестирует работу метода change_lang.
    """
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"
