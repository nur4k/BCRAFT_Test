from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from src.services.user import user
from src.schemas.token import Token
from src.schemas.user import UserIn, UserOut, UserUpdate
from src.database.dependencies import get_async_session


router = APIRouter()

@router.get("/users")
async def get_users(session: Session = Depends(get_async_session)):
    return await user.get_users(session=session)

@router.get('/user/me', response_model=UserOut)
async def get_user(user_me: UserOut=Depends(user.get_current_user)):
    return await user.get_user_me(user_me=user_me)

@router.patch("/user/{id}")
async def update_user(id: int, request: UserUpdate, session: Session = Depends(get_async_session)):
    return await user.update_user(session=session, id=id, request=request)

@router.delete("/user/{id}")
async def delete_user(id: int, session: Session = Depends(get_async_session)):
    return await user.delete_user(session=session, id=id)

@router.post("/login", response_model=Token)
async def login(request: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_async_session)):
    return await user.login(session=session, request=request)

@router.post('/registration', response_model=UserOut)
async def registration_user(user_in: UserIn, session: Session = Depends(get_async_session)):
    return await user.registration(session=session, user_in=user_in)
