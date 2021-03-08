from fastapi import FastAPI

from blog.database import engine
from blog.routers import blog, user, auth, file

from blog import models
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(file.router)
app.include_router(user.router)
