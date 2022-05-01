from typing import List, Any

from .loaders import BaseLoader
from .language import Language
from .singleton import Singleton
from .exceptions import DataNotInitializedError, LanguageNotPresentError


class Internationalization(metaclass=Singleton):
    _initialized: bool = False
    __data: dict[str, Language] = None

    @property
    def data(self) -> dict[str, Any]:
        if self.__data is None:
            raise DataNotInitializedError("Data from locales not initialized. Call initialize() before get data")

        return self.__data

    def initialize(self, loader: BaseLoader):
        languages = loader.load()
        self.__data = {}

        for lang in languages:
            dict_present = {o.name: o.value for o in lang.content}
            self.__data[lang.name] = Language(lang.name, dict_present)

    @property
    def languages(self) -> List[str]:
        return list(self.data.values())

    def get_language(self, name: str):
        if name not in self.data.keys():
            raise LanguageNotPresentError()

        return self.data[name]







