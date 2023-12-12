from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# request Get method URL: "/"


@app.get("/")
def read_root():

    return {"Hello": "World bro"}


@app.get("/posts")
def get_posts():
    return {"data": "your first post"}


@app.post("/createpost")
def create_post(payload: dict=Body(...)):
    print(payload)
    return {"message": "sucessfully created post"}

def get_post_by_id(payload: dict=Body(...)):
    print(payload)