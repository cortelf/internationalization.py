from typing import Optional, List

from pydantic import BaseModel


class PathFile(BaseModel):
    domain: Optional[str]
    language: str
    extension: str
    name_parts: List[str]
