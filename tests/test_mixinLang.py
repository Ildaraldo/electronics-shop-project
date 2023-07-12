from src.mixinLang import MixinLanguage


def test_mixin_lang():
    """Функция для тестирования класса 'MixinLanguage' и его метода 'change_lang()'"""
    mixin_lang_1 = MixinLanguage()
    assert mixin_lang_1.language == 'EN'

    # смена языка
    mixin_lang_1.change_lang()
    assert mixin_lang_1.language == 'RU'

    # двойная смена языка
    mixin_lang_1.change_lang().change_lang()
    assert mixin_lang_1.language == 'RU'
