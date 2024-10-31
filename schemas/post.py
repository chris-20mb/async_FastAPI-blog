from datetime import datetime, UTC

from pydantic import BaseModel


class PostIn(BaseModel):
    title: str 
    date: datetime = datetime.now(UTC)
    published: bool = False