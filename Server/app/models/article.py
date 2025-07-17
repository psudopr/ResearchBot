from pydantic import BaseModel, Field
from typing import Optional

class Article(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    company_id: str # Foreign key to the Company collection
    url: str
    title: str
    summary_sentence: str
    summary_bullets: list[str]
    summary_narrative: str
    is_read: bool = False
