from sqlalchemy.orm.session import Session
from db.models import User, Message, Group, GroupMember
import schemas.user


# create new user
def create_user(db: Session, user: schemas.user.UserCreate):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# send message
def create_message(db: Session, message: schemas.user.MessageCreate):
    db_message = Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# great group
def create_group(db: Session, group: schemas.user.GroupBase):
    db_group = Group(
        name=group.name,
        description=group.description,
        admin_id=group.admin_id
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

# add groupMember

def add_member_to_group(db: Session, group_id: int, user_id: int, is_admin: bool = True):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group:
        db_member = GroupMember(group_id=group_id, user_id=user_id, is_admin=is_admin)
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member
    return None

