import pytest

from httpx import AsyncClient


''''''
class RecipeStep:
    num: int

async def test_add_recipe(ac: AsyncClient):
    data = {
        "title": "Test Recipe",
        "description": "Test Description",
    }
    response = await ac.post("/add_recipe", json=data)
    RecipeStep.num = response.json().get('id')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
''''''

async def test_add_steps(ac: AsyncClient):
    data = {
        "step": 1,
        "description": "Some text",
        "time": 30, 
        "url": " ",
        "recipe_id": RecipeStep.num
    }
    response = await ac.post("/add_cook_step", json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_get_cook_steps(ac: AsyncClient):
    response = await ac.get("/cook_steps")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

async def test_update_step(ac: AsyncClient):
    data = {
        "step": 1,
        "description": "Some text",
        "time": 30, 
        "url": " ",
        "recipe_id": RecipeStep.num
    }
    response = await ac.patch("/cook_step/1", json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_delete_step(ac: AsyncClient):
    response = await ac.delete("/cook_step/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_get_time(ac: AsyncClient):
    response = await ac.get("/time_cook/10/40")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
