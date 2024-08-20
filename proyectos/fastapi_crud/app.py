from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

# Post model


class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    create_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


posts = []


@app.get("/")
def read_root():
    return {"Welcome": "Brandon"}


@app.get("/posts")
def get_posts():
    return posts


@app.post("/posts")
def save_posts(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return "Received"


@app.get("/posts/{post_id}")
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    return "Post not found"
# 32:00