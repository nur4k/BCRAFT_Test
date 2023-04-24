from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.schemas import ingredient
from src.services import ingredients
from src.database.dependencies import get_async_session


router = APIRouter(tags=["Ingredient"])

@router.get("/ingredients")
async def get_ingredient(session: Session = Depends(get_async_session) ):
    return await ingredients.get_ingredients(session)

@router.post("/add_ingredient")
async def add_ingredient(ingr: ingredient.CreateIngredient, session: Session = Depends(get_async_session) ):
    return await ingredients.create_ingredient(session=session, ingredient=ingr)

@router.patch("/ingredient/{id}")
async def update_ingredient(id: int, ingredient: ingredient.CreateIngredient, session: Session = Depends(get_async_session) ):
    return await ingredients.update_ingredient(id=id, ingredient=ingredient, session=session)

@router.delete("/ingredient/{id}")
async def delete_ingredient(id: int, session: Session = Depends(get_async_session) ):
    return await ingredients.delete_ingredient(session=session, id=id)

@router.get("/ingredients/filter/{ingredient}")
async def ingredients_filter(ingredient: str, session: Session = Depends(get_async_session) ):
    return await ingredients.filter_ingredient(session=session, ingredient=ingredient)
