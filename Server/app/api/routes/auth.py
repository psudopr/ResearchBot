from datetime import timedelta
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User
from app.models.auth import UserCreate, UserUpdate, PasswordUpdate
from app.services.security import get_password_hash, verify_password, create_access_token
from app.core.config import Config
from app.db.database import db
from app.api.dependencies import get_current_active_user

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_data = db.users.find_one({"email": form_data.username})
    if not user_data or not verify_password(form_data.password, user_data["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user_data["_id"])}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=User)
async def register_user(user: UserCreate):
    existing_user = db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed_password = get_password_hash(user.password)
    user_data = user.dict()
    user_data.pop("password")
    user_data["hashed_password"] = hashed_password
    
    new_user = db.users.insert_one(user_data)
    created_user = db.users.find_one({"_id": new_user.inserted_id})

    return created_user

@router.put("/users/me", response_model=User)
async def update_user_profile(user_update: UserUpdate, current_user: User = Depends(get_current_active_user)):
    db.users.update_one(
        {"_id": current_user.id},
        {"$set": {"full_name": user_update.full_name}}
    )
    updated_user = db.users.find_one({"_id": current_user.id})
    return updated_user

@router.put("/users/me/password")
async def update_user_password(password_update: PasswordUpdate, current_user: User = Depends(get_current_active_user)):
    user_in_db = db.users.find_one({"_id": current_user.id})
    if not verify_password(password_update.current_password, user_in_db["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect current password",
        )
    
    new_hashed_password = get_password_hash(password_update.new_password)
    db.users.update_one(
        {"_id": current_user.id},
        {"$set": {"hashed_password": new_hashed_password}}
    )
    return {"message": "Password updated successfully"}
