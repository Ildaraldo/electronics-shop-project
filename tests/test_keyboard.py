from src.keyboard import KeyBoard


def test_keyboard():
    """Функция для тестирования класса 'KeyBoard'"""
    pass
    keyboard_1 = KeyBoard('Dark Project KD87A', 9600, 5)
    assert keyboard_1.language == 'EN'
