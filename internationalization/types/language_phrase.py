from pydantic import BaseModel


class LanguagePhrase(BaseModel):
    language_name: str
    phrase_key: str
    value: str
