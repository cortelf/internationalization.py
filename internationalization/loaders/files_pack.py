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

    def __init__(self, directory:  Union[str, PathLike[str]], domain: Optional[str] = None, recursive: bool = False):
        path_directory = Path(directory)

        if not path_directory.exists() or not path_directory.is_dir():
            raise ValueError(f"{directory} must be valid and exists folder")

        if domain is not None and not isinstance(domain, str):
            raise TypeError(f"{domain} must be str or None")

        self.domain = domain
        self.directory = path_directory
        self.recursive = recursive

        super().__init__()

    @abstractmethod
    def load_file_content(self, file_content: str) -> List[Phrase]:
        ...

    def scan_folders(self) -> List[Path]:
        folders: List[Path] = [self.directory]

        if self.recursive:
            for folder in folders:
                for path in folder.iterdir():
                    if path.is_dir():
                        folders.append(path)

        return folders

    def load(self) -> List[FullLanguage]:
        result = []

        for folder in self.scan_folders():
            for path in folder.iterdir():
                if path.is_file() and self.check_file_name(path.name):
                    content = path.read_text("utf-8")
                    path_file = self.parse_file_name(path.name)
                    transformed_data = self.load_file_content(content)
                    exist = list(filter(lambda x: x.name == path_file.language, result))
                    if len(exist) > 0:
                        exist[0].content += transformed_data
                    else:
                        result.append(FullLanguage(name=path_file.language, content=transformed_data))
        return result

    def parse_file_name(self, name: str) -> PathFile:
        parts = name.split(".")
        if len(parts) < 2:
            raise ValueError("Parser is not support no-extension files")
        domain = None
        ext = parts[-1]
        lang = parts[-2]

        if len(parts) > 2 and self.domain is not None:
            domain = parts[-3]
            name_parts = parts[:-3]
        else:
            name_parts = parts[:-2]

        return PathFile(domain=domain, language=lang, extension=ext, name_parts=name_parts)

    def check_file_name(self, name: str) -> bool:
        try:
            path_file = self.parse_file_name(name)
            return path_file.domain == self.domain and path_file.extension in self.allowed_extensions
        except ValueError:
            return False
