from typing import List

from .exceptions import WordNotPresentError
from .types import Phrase


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

    def get(self, key: str):
        """
        Returns a phrase given a key
        :param key: Key
        :return: Phrase
        """
        return self.__getattr__(key)

    def find_phrase(self, phrase: str) -> List[Phrase]:
        values = self.__data.values()
        if phrase not in values:
            raise WordNotPresentError(f"Phrase {phrase} not present in lang {self.__name}")

        response = []
        for k, v in self.__data.items():
            if v == phrase:
                response.append(Phrase(
                    name=k,
                    value=v
                ))

        return response
