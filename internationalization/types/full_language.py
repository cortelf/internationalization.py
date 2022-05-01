from . import Phrase
from typing import List
from pydantic import BaseModel


class FullLanguage(BaseModel):
    name: str
    content: List[Phrase]
