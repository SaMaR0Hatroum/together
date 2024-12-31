from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# user
class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class GroupBase(BaseModel):
    name: str
    description : str
    admin_id : int

class GroupResponse(GroupBase):
        id: int
        admin: UserResponse
        is_admin: bool

        class Config:
            from_attributes = True


class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
   # id: int
    content: str
    group_id: int
    sender_id: int
    receiver_id: int




class MessageResponse(MessageBase):
    id: int
    timestamp: Optional[datetime] = datetime.now()

    class Config:
        from_attributes = True



