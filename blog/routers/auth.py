from fastapi import APIRouter, status, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from blog import schemas, database, models
from blog.util import token
from sqlalchemy.orm import Session
from blog.util import hash

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

get_db = database.get_db

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.username == request.username).first()

    if not user or not hash.Hash.verify(user.password, request.password):
        raise HTTPException(status=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    access_token=token.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
