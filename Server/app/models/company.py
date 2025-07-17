from pydantic import BaseModel, Field
from typing import Optional

class Company(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: str # Foreign key to the User collection
    name: str
    rss_feed_url: str
    analysis_frequency: int # in hours
    user_narrative: str
