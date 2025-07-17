from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    email: EmailStr
    full_name: Optional[str] = None
    global_prompt: Optional[str] = ""

class UserInDB(User):
    hashed_password: str
