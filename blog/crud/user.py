from sqlalchemy.orm import Session
import datetime
from fastapi import HTTPException, status

from ..util import hash

from blog import schemas, models

def create(request: schemas.User, db: Session):
    hashed_password = hash.Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, username=request.username, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def read(db : Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND, detail=f"User not found. ID: {id}")

    return user