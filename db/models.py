from sqlalchemy import Column, Integer, String, ForeignKey, Table , Boolean

from sqlalchemy.orm import relationship
from db.database import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    admin_id = Column(Integer, ForeignKey('users.id'))
    admin = relationship('User', backref='groups')

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey("users.id"))


class GroupMember(Base):
     __tablename__ = "group_members"
     id = Column(Integer, primary_key=True, index=True)
     group_id = Column(Integer, ForeignKey("groups.id"))
     user_id = Column(Integer, ForeignKey("users.id"))
     is_admin = Column(Boolean, default=False)
     user = relationship("User")
     group = relationship("Group")

#    group_members = Table(
#        "group_members", Base.metadata,
#        Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True),
#        Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
#    )