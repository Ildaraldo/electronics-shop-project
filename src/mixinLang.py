class MixinLanguage:
    """
    Миксин-класс для смены раскладки клавиатуры
    """
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Функция, для смены раскладки клавиатуры"""
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

        return self

