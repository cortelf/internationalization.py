from abc import ABC, abstractmethod
from typing import List
from ..types import FullLanguage


class BaseLoader(ABC):
    @abstractmethod
    def load(self) -> List[FullLanguage]:
        pass
