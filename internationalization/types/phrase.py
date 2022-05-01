from pydantic import BaseModel


class Phrase(BaseModel):
    name: str
    value: str
