from pydantic import BaseModel
from typing import Optional


class UserSendMessage(BaseModel):
    id: str
    message: str


class GetAns(BaseModel):
    message: int
