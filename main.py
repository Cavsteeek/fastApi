from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    body: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "FastAPI World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/posts")
def create_post(post: Post):
    # print(post.published)
    return {post.title, post.body, post.published, post.rating}
