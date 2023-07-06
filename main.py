from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


# Pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    # if not available
    if id == 2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"FUCK")
    return {"post_detail": f"Here is the post {id}"}


@app.post("/createposts")
def create_posts(post: Post):
    return {"data": post.dict()}
