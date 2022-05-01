from abc import ABC, abstractmethod
from os import PathLike
from pathlib import Path
from typing import Union, Optional, List

from ..types import FullLanguage, PathFile, Phrase
from .base_loader import BaseLoader


class FilesPackLoader(BaseLoader, ABC):
    domain: Optional[str]
    directory: Path

    @property
    @abstractmethod
    def allowed_extensions(self) -> List[str]:
        ...

    def __init__(self, directory:  Union[str, PathLike[str]], domain: Optional[str] = None):
        path_directory = Path(directory)

        if not path_directory.exists() or not path_directory.is_dir():
            raise ValueError(f"{directory} must be valid and exists folder")

        if domain is not None and not isinstance(domain, str):
            raise TypeError(f"{domain} must be str or None")

        self.domain = domain
        self.directory = path_directory

        super().__init__()

    @abstractmethod
    def load_file_content(self, file_content: str) -> List[Phrase]:
        ...

    def load(self) -> List[FullLanguage]:
        result = []

        for path in self.directory.iterdir():
            if path.is_file() and self.check_file_name(path.name):
                content = path.read_text("utf-8")
                path_file = self.parse_file_name(path.name)
                transformed_data = self.load_file_content(content)
                result.append(FullLanguage(name=path_file.language, content=transformed_data))
        return result

    @staticmethod
    def parse_file_name(name: str) -> PathFile:
        parts = name.split(".")
        if len(parts) < 2:
            raise ValueError("Parser is not support no-extension files")
        domain = None
        ext = parts[-1]
        lang = parts[-2]

        if len(parts) > 2:
            domain = parts[-3]

        return PathFile(domain=domain, language=lang, extension=ext)

    def check_file_name(self, name: str) -> bool:
        try:
            path_file = self.parse_file_name(name)
            return path_file.domain == self.domain and path_file.extension in self.allowed_extensions
        except ValueError:
            return False
