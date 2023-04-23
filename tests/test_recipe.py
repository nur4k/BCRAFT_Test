import pytest

from httpx import AsyncClient


class Recipe:
    num: int

async def test_get_recipes(ac: AsyncClient):
    response = await ac.get("/recipes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

async def test_add_recipe(ac: AsyncClient):
    data = {
        "title": "Test Recipe",
        "description": "Test Description",
    }
    response = await ac.post("/add_recipe", json=data)
    Recipe.num = response.json().get('id')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

""""""
class UserConf:
    token: str


async def test_registration(ac: AsyncClient):
    response = await ac.post("/registration", json={"username": "Hustle1", "password": "1234"})
    assert 200 == response.status_code

async def test_login(ac: AsyncClient):
    response = await ac.post("/login", data={"username": "Hustle1", "password": "1234"})
    UserConf.token = response.json().get("access_token")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
""""""
async def test_get_recipe(ac: AsyncClient):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {UserConf.token}"
    }
    response = await ac.get("/recipe/1", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_update_recipe(ac: AsyncClient):
    data = {
        "title": "Updated Test Recipe",
        "description": "Updated Test Description",
    }
    response = await ac.patch("/recipe/1", json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_create_rate(ac: AsyncClient):
    json = {
        "number": 1,
        "recipe_id": Recipe.num
    }
    response = await ac.post("/add_rate", json=json)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_filter_rate(ac: AsyncClient):
    response = await ac.get("/filter_rate/1")
    assert response.status_code == 200

# async def test_delete_recipe(ac: AsyncClient):
#     response = await ac.delete("/recipe/1")
#     assert response.status_code == 200
#     assert isinstance(response.json(), dict)

async def upload_image(ac: AsyncClient):
    data = {
        "image_name": "2ca52d01cbad7e1b76621c38dd9e3fa9.jpg"
    }
    response = await ac.post("/upload-image/", data=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
