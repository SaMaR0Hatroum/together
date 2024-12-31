#from fastapi import FastAPI, Depends
#from sqlalchemy.orm import Session
#from db.database import  get_db
#from schemas.user import UserCreate, UserResponse, MessageCreate, MessageResponse, GroupResponse, GroupBase
from db import models
#import crud
from router import router
from db.database import  engine


from fastapi import FastAPI
from db.database import engine
from db import models
from router import router


models.Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(router)


users = {}
groups = {}



#@app.post("/users/", response_model=UserResponse)
#def create_user(user: UserCreate, db: Session = Depends(get_db)):
 #   return crud.create_user(db=db, user=user)

#@app.post("/messages/", response_model=MessageResponse)
# ///def send_message(message: MessageCreate, db: Session = Depends(get_db)):
#     return crud.create_message(db=db, message=message)

# @app.post("/groups/", response_model=GroupResponse)
# def create_group(group: GroupBase, db: Session = Depends(get_db)):
#     return crud.create_group(db=db, group=group)
#
# @app.post("/groups/{group_id}/members/{user_id}")
# def add_member(group_id: int, user_id: int, db: Session = Depends(get_db)):
#     member = crud.add_member_to_group(db, group_id, user_id)
    # if not group_id or not user_id:
    #     return {"msg": "Group ID and User ID are required"}
    # member = crud.add_member_to_group(db, group_id, user_id)
    # if member:
    #     return member
    # return {"msg": "Group not found or user already added"}

#@app.get("/groups/{group_id}/members/")
#def list_members(group_id: int, db: Session = Depends(get_db)):
    #  Query is the group exist or not
   # db_group = db.query(Group).filter(group_id == Group.id).first()
  #  if not db_group:
     #   raise HTTPException(status_code=404, detail="Group not found")

# Query members with user details
   # members = db.query(GroupMember).filter(GroupMember.group_id == group_id).all()

    #members details
   # members_details = []
   # for member in members:
     #   user = db.query(User).filter(User.id == member.user_id).first()
     #   if user:
       #     members_details.append({
        #        "user_id": user.id,
         #       "username": user.username,
        #        "email": user.email,
         #       "is_admin": member.is_admin
         #   })

   # return {"group_id": group_id, "members": members_details}
