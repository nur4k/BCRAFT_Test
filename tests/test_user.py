import pytest

from httpx import AsyncClient


class UserConf:
    token: str

async def test_registration(ac: AsyncClient):
    response = await ac.post("/registration", json={"username": "Hustle", "password": "1234"})
    assert 200 == response.status_code

async def test_login(ac: AsyncClient):
    response = await ac.post("/login", data={"username": "Hustle", "password": "1234"})
    UserConf.token = response.json().get("access_token")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_get_users(ac: AsyncClient):
    response = await ac.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

async def test_get_user(ac: AsyncClient):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {UserConf.token}"
    }
    response = await ac.get("/user/me", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_update_user(ac: AsyncClient):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {UserConf.token}"
    }
    response = await ac.patch("/user/1", json={"username": "Hustle3", "password": "1234"}, headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

async def test_delete_user(ac: AsyncClient):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {UserConf.token}"
    }
    response = await ac.delete("/user/1", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
