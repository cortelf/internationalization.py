from typing import List

from types import Phrase
from . import FilesPackLoader
import yaml


class YAMLLoader(FilesPackLoader):
    @property
    def allowed_extensions(self) -> List[str]:
        return ["yaml", "yml"]

    def load_file_content(self, file_content: str) -> List[Phrase]:
        data = yaml.safe_load(file_content)
        res = []

        for k, v in data.items():
            res.append(Phrase(name=k, value=v))

        return res
