from fastapi import HTTPException
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.database.models.models import Ingredient
from src.schemas import ingredient


async def get_ingredients(session: Session):
    return (await session.scalars(select(Ingredient))).all()

async def filter_ingredient(session: Session, ingredient: str):
    filtering = await session.scalar(select(Ingredient).where(Ingredient.name == ingredient))
    if not filtering:
        return {"msg": "Ingredient is not found!"}
    return filtering

async def create_ingredient(session: Session, ingredient: ingredient.CreateIngredient):
    if not ingredient.recipe_id:
        raise Exception("This recipe not found!") 
    query = Ingredient(**ingredient.dict())
    session.add(query)
    await session.commit()
    return query

async def update_ingredient(session: Session, id: int, ingredient: ingredient.CreateIngredient):
    ingredient_db = await session.scalar(select(Ingredient).where(Ingredient.id == id))
    if not ingredient_db:
        raise HTTPException("Error!")
    if not ingredient.recipe_id:
        raise Exception("This recipe not found!")
    elif ingredient.name:
        await session.execute(update(Ingredient).where(Ingredient.id == id).values(name=ingredient.name))
        await session.commit()
    elif ingredient.recipe:
        await session.execute(update(Ingredient).where(Ingredient.id == id).values(recipe=ingredient.recipe))
        await session.commit()
    return {"msg": "Succesfull updated ingredient!"}

async def delete_ingredient(session: Session, id: int):
    ingredient = await session.scalar(select(Ingredient).where(Ingredient.id == id))
    if not ingredient:
        raise HTTPException("Error!")
    await session.execute(delete(Ingredient).where(Ingredient.id == id))
    await session.commit()
    return {"msg": "Post deleted!"}
