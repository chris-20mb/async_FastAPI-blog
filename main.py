from fastapi import FastAPI, status
from datetime import UTC, datetime
from pydantic import BaseModel

app = FastAPI()


fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com FastAPI", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Starllet", "date": datetime.now(UTC), 'published': False},
]


class Post(BaseModel):
    title: str 
    date: datetime = datetime.now(UTC)
    published: bool = False


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    #dump para converter a representação dos dados no formato dicionario
    fake_db.append(post.model_dump())
    return post   


@app.get("/posts/")
def read_posts(published: bool, limit: int, skip: int = 0):
    #def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):
    #return [post for post in fake_db[skip : skip + limit] if post['published'] is published]
    #TO DO - alterar aqui para exibir a quantidade correta de posts
    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post["published"] is published:
            posts.append(post)

    return posts        


@app.get('/posts/{framework}')
def read_framework_posts(framework: str):
    return {
        'posts': [
            {'title': f'Criando uma aplicação com {framework}', 'date': datetime.now(UTC)}, 
            {'title': f'Internacionalizando uma app {framework}', 'date': datetime.now(UTC)},
        ]
    }   