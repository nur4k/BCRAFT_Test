from pydantic import BaseModel
from typing import Optional



class Recipe(BaseModel):
    id: int
    title: str
    description: str
    url: Optional[str]


class CreateRecipe(BaseModel):
    title: str
    description: str
    url: Optional[str]
