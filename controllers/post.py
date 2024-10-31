from fastapi import Response, Header, Cookie, FastAPI, status, APIRouter
from datetime import UTC, datetime
from pydantic import BaseModel
from typing import Annotated
from schemas.post import PostIn
from views.post import PostOut


router = APIRouter(prefix="/posts")

fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com FastAPI", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Starllet", "date": datetime.now(UTC), 'published': False},
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    #dump para converter a representação dos dados no formato dicionario
    fake_db.append(post.model_dump())
    return post   


@router.get("/", response_model=list[PostOut])
def read_posts(
    response: Response, 
    published: bool, 
    limit: int, 
    skip: int = 0, 
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None
):
    response.set_cookie(key="user", value="chris.c@gmail.com")
    print(f"Cookie: {ads_id}")
    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post["published"] is published:
            posts.append(post)

    return posts  



@router.get('/{framework}', response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        'posts': [
            {'title': f'Criando uma aplicação com {framework}', 'date': datetime.now(UTC)}, 
            {'title': f'Internacionalizando uma app {framework}', 'date': datetime.now(UTC)},
        ]
    }   