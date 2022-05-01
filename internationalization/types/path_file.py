from typing import Optional

from pydantic import BaseModel


class PathFile(BaseModel):
    domain: Optional[str]
    language: str
    extension: str
