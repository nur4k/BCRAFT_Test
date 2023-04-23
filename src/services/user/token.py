import jwt

from datetime import datetime, timedelta

from src.config.settings import user_settings


SECRET_KEY = user_settings.secret_key
ALGORITHM = user_settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = user_settings.access_token_expire_minutes


async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
