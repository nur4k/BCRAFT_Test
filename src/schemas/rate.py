from pydantic import BaseModel, validator


class Rate(BaseModel):
    id: int
    number: int
    recipe_id: int


class CreateRate(BaseModel):
    number: int
    recipe_id: int

    @validator('number')
    def validate_number(cls, v):
        if v > 5 or v < 1:
            raise ValueError('must contain a space')
        return v
