from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel  # Use this module to create an schema


app = FastAPI()  # call the module


class Post(BaseModel):  # create a class that automatically extracts the data from the posts
    Tittle: str
    Content: str
    Published: bool = True  # if we define a default value then the field becomes optional
    # this is another way to make a field optional and null, Need to import Optional module
    Rating: Optional[int] = None


@app.get("/")  # decorator aplies the fast api to the function with an http method
def root():  # Mainfunction
    return {"message": "Welcome to my API this is a reload test"}


@app.get("/post")
def get_posts():
    return {"data": "This is one post"}


@app.post("/post/create")
# Store the body of the post in an instance of the Post class
def create_post(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"new Post": f"Tittle: {new_post.Tittle}" + " " + f"Content: {new_post.Content}"}
