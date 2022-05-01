from pathlib import Path
from typing import List

from pydantic import BaseModel


class InternationalizationFile(BaseModel):
    name: str
    path: Path
    domain: str
    languages: List[str]