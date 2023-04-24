from fastapi import APIRouter, Depends, File, UploadFile

from sqlalchemy.orm import Session

from src.schemas import recipe, rate
from src.schemas.user import UserOut
from src.services.user import user
from src.services import recipes, utils
from src.database.dependencies import get_async_session


router = APIRouter(tags=["Recipe"])

@router.get("/recipes")
async def get_recipes(session: Session = Depends(get_async_session)):
    return await recipes.get_recipes(session)

@router.get("/recipe/{id}")
async def get_recipe(id: int, session: Session = Depends(get_async_session), user_me: UserOut=Depends(user.get_current_user)):
    return await recipes.get_recipe(session=session, recipe_id=id)

@router.post("/add_recipe")
async def add_recept(recipe: recipe.CreateRecipe, session: Session = Depends(get_async_session) ):
    return await recipes.create_recipe(session=session, recipe=recipe)

@router.patch("/recipe/{id}")
async def update_recipe(id: int, recipe: recipe.CreateRecipe, session: Session = Depends(get_async_session) ):
    return await recipes.update_recipe(id=id, session=session, recipe=recipe)

@router.delete("/recipe/{id}")
async def deletee(id: int, session: Session = Depends(get_async_session) ):
    return await recipes.delete_recipe(session=session, id=id)

@router.post("/add_rate")
async def create_rate(rate: rate.CreateRate, session: Session = Depends(get_async_session) ):
    return await recipes.rate_add(session=session, rate=rate)

@router.get("/filter_rate/{number}")
async def filter_rate(number: int, session: Session = Depends(get_async_session) ):
    return await recipes.rate_recipe(rate=number, session=session)

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...), session: Session = Depends(get_async_session) ):
    file.filename = await utils.generate_uniquie_name(filename=file.filename)
    await utils.create_image(file)
    return {"image_name": file.filename}
