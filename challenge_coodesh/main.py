from fastapi import FastAPI, Depends, HTTPException
from challenge_coodesh.db import schemas
from challenge_coodesh import crud
from sqlalchemy.orm import Session
from challenge_coodesh.db.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index():
    return {
        "message": "Back-end Challenge 2021 :medal: - Space Flight News"
    }


@app.post("/articles/", response_model=schemas.Articles)
def create_article(
    articles: schemas.ArticlesCreate, db: Session = Depends(get_db)
):
    db_article = crud.get_article(db, id=articles.id)
    if db_article:
        raise HTTPException(
            status_code=400, detail="Article already registered"
        )
    return crud.create_article(db=db, articles=articles)
