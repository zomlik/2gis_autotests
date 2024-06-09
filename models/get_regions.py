from pydantic import BaseModel
from typing import List


class Country(BaseModel):
    name: str
    code: str


class Items(BaseModel):
    id: int
    name: str
    code: str
    country: Country


class GetRegions(BaseModel):
    total: int
    items: List[Items] = []
