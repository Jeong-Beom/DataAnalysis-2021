from typing import Sequence
from pydantic import BaseModel, HttpUrl

class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl

class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]

class RecipeCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int
    