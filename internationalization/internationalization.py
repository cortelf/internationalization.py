from os import PathLike
from pathlib import Path
from typing import Union, Final, List, Any

from .language import Language
from .singleton import Singleton
from .exceptions import DataNotInitializedError, LanguageNotPresentError
from dataclasses import dataclass
import os
import yaml


@dataclass(frozen=True)
class InternationalizationFile:
    name: str
    path: Path
    domain: str
    languages: List[str]


class Internationalization(metaclass=Singleton):
    @property
    def data(self) -> dict[str, Any]:
        if self.__data is None:
            raise DataNotInitializedError("Data from locales not initialized. Call initialize() before get data")

        return self.__data

    @property
    def languages(self) -> List[str]:
        return list(self.data.keys())

    def __init__(self, domain: str,  locales_dir: Union[str, PathLike[str]]):
        if not os.path.isdir(locales_dir):
            raise FileNotFoundError()

        self.__locales_dir: Final[Path] = Path(locales_dir) if isinstance(locales_dir, str) else locales_dir
        self.__domain: Final[str] = domain

        self.__data = None

    def __read_files_from_directory(self) -> List[InternationalizationFile]:
        need_files: List[InternationalizationFile] = []

        for item in os.listdir(self.__locales_dir):
            dot_split = item.split(".")
            if len(dot_split) > 2 and dot_split[0] == self.__domain and dot_split[-1] in ["yaml", "yml"]:
                need_files.append(InternationalizationFile(
                    name=item,
                    domain=self.__domain,
                    path=self.__locales_dir / item,
                    languages=dot_split[1:-1]
                ))

        return need_files

    def __load_language_file(self, f: InternationalizationFile):
        with open(f.path, 'r', encoding="utf-8") as stream:
            md = yaml.safe_load(stream)

        for lang in f.languages:
            self.__data[lang] = md

    def initialize(self):
        files = self.__read_files_from_directory()
        self.__data = {}

        for file in files:
            self.__load_language_file(file)

    def get_language(self, name: str):
        if name not in self.languages:
            raise LanguageNotPresentError()

        return Language(name, self.__data[name])

    def find_phrase(self, name: str):
        res = {}
        for k, v in self.data.items():
            if name in v:
                res[k] = v[name]

        return res







