from typing import Optional
from pydantic import BaseModel


class CookStep(BaseModel):
    id: int
    step: str
    description: Optional[str]
    time: int
    url: str
    recipe_id: int


class Cook_stepAdd(BaseModel):
    step: int
    time: int
    description: str
    url: str
    recipe_id: int
