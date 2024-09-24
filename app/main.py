from random import randrange
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ROUTES
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
def root():
    return {"message": "FastAPI World"}


# @app.get("/sql")
# def test(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all
#     return {"data": posts}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(
        title=post.title, content=post.content, published=post.published
    )

    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):

    return {"post_detail": get_post}


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int):
    return {"data": "updated_post"}
