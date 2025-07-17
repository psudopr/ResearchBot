from fastapi import APIRouter, Depends, Body
from app.models.user import User
from app.api.routes.auth import get_current_active_user
from app.db.database import db

router = APIRouter()

@router.get("/prompt", response_model=dict)
async def get_global_prompt(current_user: User = Depends(get_current_active_user)):
    user = db.users.find_one({"_id": current_user.id})
    return {"global_prompt": user.get("global_prompt", "")}

@router.put("/prompt")
async def update_global_prompt(prompt: str = Body(..., embed=True), current_user: User = Depends(get_current_active_user)):
    db.users.update_one(
        {"_id": current_user.id},
        {"$set": {"global_prompt": prompt}}
    )
    return {"message": "Global prompt updated successfully"}
