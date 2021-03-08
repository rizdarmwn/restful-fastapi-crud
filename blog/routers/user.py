from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, models
from blog import schemas
from ..crud import user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

get_db = database.get_db

@router.get("/{id}", response_model=schemas.UserResponse, )
def get(id: int, db: Session = Depends(get_db)):
    return user.read(db, id)

@router.post("/", response_model=schemas.UserResponse)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db=db, request=request)
