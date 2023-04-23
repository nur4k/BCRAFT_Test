import pytest

from httpx import AsyncClient


''''''
class RecipeIngredient:
    num: int


async def test_add_recipe(ac: AsyncClient):
    data = {
        "title": "Test Recipe",
        "description": "Test Description",
    }
    response = await ac.post("/add_recipe", json=data)
    RecipeIngredient.num = response.json().get('id')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
''''''

async def test_get_ingredient(ac: AsyncClient):
    response = await ac.get("/ingredients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

async def test_create_ingredient(ac: AsyncClient):
    data = {
        "name": "Created test ingredient",
        "recipe_id": RecipeIngredient.num
    }
    response = await ac.post("/add_ingredient", json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_update_ingredient(ac: AsyncClient):
    data = {
        "name": "Updated test ingredient",
        "recipe_id": RecipeIngredient.num
    }
    response = await ac.patch("/ingredient/1", json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_delete_ingredient(ac: AsyncClient):
    response = await ac.delete("/ingredient/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_ingredient_filter(ac: AsyncClient):
    response = await ac.get("/ingredients/filter/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
