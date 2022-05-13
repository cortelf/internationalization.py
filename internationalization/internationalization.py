from typing import List, Any

from .loaders import BaseLoader
from .language import Language
from .singleton import Singleton
from .exceptions import DataNotInitializedError, LanguageNotPresentError, WordNotPresentError
from .types import LanguagePhrase


class Internationalization(metaclass=Singleton):
    _initialized: bool = False
    __data: dict[str, Language] = None

    @property
    def data(self) -> dict[str, Language]:
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
    def languages(self) -> list[Language]:
        return list(self.data.values())

    def get_language(self, name: str):
        if name not in self.data.keys():
            raise LanguageNotPresentError()

        return self.data[name]

    def find_phrase(self, phrase: str) -> List[LanguagePhrase]:
        """
        Returns all variations of the given phrase in other languages, if it is present in at least one of them
        :param phrase: Search phrase
        :return: Variations of the given phrase
        """
        existing_matches: List[LanguagePhrase] = []
        for lang in self.data.values():
            try:
                phrases = lang.find_phrase(phrase)
                existing_matches += list(map(lambda x: LanguagePhrase(
                    language_name=lang.name,
                    phrase_key=x.name,
                    value=x.value
                ), phrases))
            except WordNotPresentError:
                pass

        return_matches: List[LanguagePhrase] = []
        for match in existing_matches:
            for lang in self.data.values():
                try:
                    return_matches.append(LanguagePhrase(
                        language_name=lang.name,
                        phrase_key=match.phrase_key,
                        value=lang.get(match.phrase_key)
                    ))
                except WordNotPresentError:
                    pass

        return return_matches
