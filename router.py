from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import models
from db.database import get_db
from db.models import Group , GroupMember , User , Message
from schemas.user import UserCreate, UserResponse, MessageCreate, MessageResponse, GroupResponse, GroupBase
import crud


router = APIRouter()

users = {}
groups = {}

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.post("/messages/", response_model=MessageResponse)
def send_message(message: MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@router.post("/groups/", response_model=GroupResponse)
def create_group(group: GroupBase, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)

@router.post("/groups/{group_id}/members/{user_id}")
def add_member(group_id: int, user_id: int, db: Session = Depends(get_db)):
    #member = crud.add_member_to_group(db, group_id, user_id)
    if not group_id or not user_id:
        return {"msg": "Group ID and User ID are required"}
    member = crud.add_member_to_group(db, group_id, user_id)
    if member:
        return member
    return {"msg": "Group not found or user already added"}



@router.get("/groups/{group_id}/members/")
def list_members(group_id: int, db: Session = Depends(get_db)):
    db_group = db.query(Group).filter(group_id == Group.id).first()
    if not db_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")

    members = db.query(GroupMember).filter(group_id == GroupMember.group_id).all()

    members_details = []
    for member in members:
        member_user_id = member.user_id
        user = db.query(User).filter(member_user_id is User.id).first()
        if user:
            members_details.append({
                "user_id": User.id,
                "username": User.username,
                "email": User.email,
                "is_admin": member.is_admin
            })

    return {"group_id": group_id, "members": members_details}


@router.post("/groups/{group_id}/members/{user_id}")
def add_member(group_id: int, user_id: int, db: Session = Depends(get_db)):
    member = crud.add_member_to_group(db, group_id, user_id)
    if member:
        return {"msg": "Member added successfully"}
    raise HTTPException(status_code=404, detail="Group or User not found")
