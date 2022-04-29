from .exceptions import WordNotPresentError


class Language:
    @property
    def name(self):
        return self.__name

    def __init__(self, name: str, data: dict):
        self.__name = name
        self.__data = data or {}

    def __getattr__(self, item: str):
        if item in self.__data:
            return self.__data[item]

        raise WordNotPresentError(f"Word {item} not present in lang {self.__name}")
