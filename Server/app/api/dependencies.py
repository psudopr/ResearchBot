from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.models.user import User
from app.core.config import Config
from app.db.database import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        
        status_code=status.HTTP_401_UNAUTHORIZED,
        
        detail="Could not validate credentials",
        
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        
        user_id: str = payload.get("sub")
        
        if user_id is None:
            
            raise credentials_exception
    
    except JWTError:
        
        raise credentials_exception
    
    user = db.users.find_one({"_id": user_id})
    
    if user is None:
        
        raise credentials_exception
    
    return User(**user)


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user
