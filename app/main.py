from typing import Optional
from fastapi import FastAPI,Response,status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()

# request Get method URL: "/"

my_posts = [{"title": "title of post1", "content": "This is my post 1", "id": 1}, {
    "title": "title of post2", "content": "This is my post 1", "id": 2}]


class Post(BaseModel):
    title: str
    content: str
    published: bool
    rating: Optional[int] = None
    
# def find_post(id, posts_dict):
#     return posts_dict.get(id, None)

def find_post(id):
    for p in my_posts:
        
        print(f"{p['title']} p titles {type(p)} {p}")
        if p['id']==id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i
        


@app.get("/")
def read_root():

    return {"Hello": "World bro"}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  delete_post_index= find_index_post(id)
  my_posts.pop(delete_post_index)
  if not delete_post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No ID Found {id}")
  
  return Response(status_code=status.HTTP_204_NO_CONTENT)
       
    
    

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/latest")
def get_latest_posts():
    lastest_post= my_posts[len(my_posts)-1]
    return{"new post":lastest_post}

@app.get("/posts/{id}")
def get_posts(id:int, response:Response):
#    id=int(id) 
   # posts_dict = {p['id']: p for p in my_posts}
    #print(posts_dict)
    #post=find_post(id,posts_dict)
    
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Post Found with id: {id}")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return{"data":"No Post Found"}
    
    print(type(id))
    return {"post_details":post}





@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()  # model dump is dict basically
    post_dict['id'] = randrange(1, 9999999)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.put("/posts/{id}")
def update_post(id: int,post: Post):
    print(post)
    post_index= find_index_post(id)
    if not post_index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No ID Found {id}")
    
    post_dict=post.model_dump()
    post_dict['id']=id
    my_posts[post_index]=post_dict
    return {"Data":post_dict}
    
    
    
    
    
 