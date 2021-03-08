from sqlalchemy.orm import Session
import datetime
from fastapi import HTTPException, status

from ..models import Blog, User

from blog import schemas

def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def create(db: Session, request: schemas.Blog, current_user: schemas.User):
    author = db.query(User).filter(User.username == current_user.username).first()
    if not author:
        new_blog = Blog(title=request.title, content=request.content)
    else:
        new_blog = Blog(title=request.title, content=request.content, author_id=author.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(db: Session, id: int):
    blog = db.query(Blog).filter(Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found, ID: {id}")

    blog.delete(synchronize_session=False)
    db.commit()
    return {"data": "Successfully deleted."}

def update(db: Session, id: int, request: schemas.Blog):
    blog = db.query(Blog).filter(Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog not found, ID: {id}")

    blog.update(request)
    db.commit()
    return {"data" : f"Blog with {id} is successfully updated."}

def read(db: Session, id: int):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog not found, ID: {id}")
    
    return blog
