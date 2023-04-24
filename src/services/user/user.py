import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.config.settings import user_settings
from src.database.models.models import User
from src.schemas.user import UserIn, UserOut, UserUpdate
from src.services.user.token import create_access_token
from src.services.user.hash_password import get_password_hash, verify_password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, user_settings.secret_key, algorithms=[user_settings.algorithm])
        pk: int = payload.get("user_pk")
        if pk is None:
            raise credentials_exception
        username: str = payload.get("username")
        if pk is None:
            raise credentials_exception
        user = UserOut(id=pk, username=username)
    except ValueError:
        raise credentials_exception
    
    return user

async def get_user_me(user_me: Depends(get_current_user)):
    return user_me

async def get_users(session: Session):
    result = (await session.scalars(select(User))).all()
    return result

async def update_user(session: Session, id: int, request: UserUpdate):
    user_db = await session.scalar(select(User).where(User.id == id))
    if not user_db: 
        raise HTTPException('Not Auth!!!')
    elif request.username:
        update_user = await session.execute(update(User).where(User.id == id).values(username=request.username))
        await session.commit()
    elif request.password:
        update_user = await session.execute(update(User).where(User.id == id).values(password=await get_password_hash(request.password)))
        await session.commit()
    elif request.username and request.password:
        update_user = await session.execute(update(User).where(User.id == id).values(username=request.username, password=await get_password_hash(request.password)))
        await session.commit()
    return {"msg": "Succesfull updated user!"}

async def delete_user(session: Session, id: int):
    user_db = await session.scalar(select(User).where(User.id == id))
    if not user_db:
        raise HTTPException('Error!!!')
    delete_user = await session.execute(delete(User).where(User.id == id))
    await session.commit()
    return {"msg": "Succesfull deleted user"}

async def login(session: Session, request: OAuth2PasswordRequestForm = Depends()):
    user = await session.scalar(select(User).where(User.username == request.username))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not await verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    data={
        "user_pk": user.id,
        "username": user.username
        }
    access_token = await create_access_token(data)
    return {"access_token": access_token, "token_type": "bearer"}

async def registration(session: Session, user_in: UserIn):
    user_db = User(username=user_in.username, password=await get_password_hash(user_in.password))
    session.add(user_db)
    await session.commit()
    return user_db
