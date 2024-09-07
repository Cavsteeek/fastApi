from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/create_post")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']}, content: {payload['body']}"}
