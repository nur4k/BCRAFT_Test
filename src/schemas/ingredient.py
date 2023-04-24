from pydantic import BaseModel


class Ingredient(BaseModel):
    id: int
    name: str


class CreateIngredient(BaseModel):
    name: str
    recipe_id: int
