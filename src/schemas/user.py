from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: str | None
    password: str | None

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True
