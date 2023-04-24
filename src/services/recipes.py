from fastapi import HTTPException

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.database.models.models import Recipe, Rate
from src.schemas import recipe, rate


async def get_recipes(session: Session):
    return (await session.scalars(select(Recipe))).all()

async def get_recipe(session: Session, recipe_id: int):
    return await session.scalar(select(Recipe).where(Recipe.id == recipe_id))

async def create_recipe(session: Session, recipe: recipe.CreateRecipe):
    query = Recipe(**recipe.dict())
    session.add(query)
    await session.commit()
    return query

async def update_recipe(session: Session, id: int, recipe: recipe.CreateRecipe):
    recipes = await session.scalar(select(Recipe).where(Recipe.id == id))
    if not recipes:
        raise HTTPException("ERROR!")
    if recipe.title:
        await session.execute(update(Recipe).where(Recipe.id == id).values(title=recipe.title))
        await session.commit()
    elif recipe.description:
        await session.execute(update(Recipe).where(Recipe.id == id).values(description=recipe.description))
        await session.commit()
    elif recipe.url:
        await session.execute(update(Recipe).where(Recipe.id == id).values(rate=recipe.url))
        await session.commit()
    elif recipe:
        await session.execute(update(Recipe).where(Recipe.id == id).values(**recipe.dict()))
        await session.commit()
    return {"msg": "Succesfull updated recipe!"}

async def delete_recipe(session: Session, id: int):
    recipe = await session.scalar(select(Recipe).where(Recipe.id == id))
    if not recipe:
        raise HTTPException("Error!")
    await session.execute(delete(Recipe).where(Recipe.id == id))
    await session.commit()
    return {"msg": "Post deleted!"}

async def rate_add(session: Session, rate: rate.CreateRate):
    query = Rate(**rate.dict())
    session.add(query)
    await session.commit()
    return query

async def rate_recipe(rate: int, session: Session):
    raiting = (await session.scalars(select(Rate).where(Rate.number == rate))).all()
    if not raiting:
        return {"msg": "Rate is not found!"}
    return raiting
