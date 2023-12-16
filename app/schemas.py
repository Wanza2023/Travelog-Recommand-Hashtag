from pydantic import BaseModel
from typing import List

class Content(BaseModel):
    content: str

class Hashtags(BaseModel):
    hashtag: List[str] = []