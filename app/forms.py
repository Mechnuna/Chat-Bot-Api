from pydantic import BaseModel


class UserSendMessage(BaseModel):
    id: str
    message: str
