from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import database, models, schemas
from blog.util import oauth2
from blog.crud import blog
from typing import List

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

get_db = database.get_db

# TODO Depends get user oauth2

@router.get("/", response_model=List[schemas.BlogResponse])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.read(db, id=id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request, current_user)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(db, id, request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(db, id)
