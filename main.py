from fastapi import FastAPI

from src.routers import user, recipe, ingredient, cook_step


app = FastAPI()
# User
app.include_router(user.router)
# Recipe
app.include_router(recipe.router)
# Ingredient
app.include_router(ingredient.router)
# Cook_step
app.include_router(cook_step.router)
