from fastapi import FastAPI, Depends, HTTPException
from challenge_coodesh.db import schemas
from challenge_coodesh import crud
from sqlalchemy.orm import Session
from challenge_coodesh.db.database import SessionLocal
from fastapi_pagination import Page, add_pagination, paginate

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


@app.get("/articles/{id}", response_model=schemas.Articles)
def read_article(id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, id=id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@app.get("/articles/", response_model=Page[schemas.Articles])
def all_articles(db: Session = Depends(get_db)):
    articles = crud.get_articles(db)
    if articles is None:
        raise HTTPException(status_code=400, detail="No articles")
    return paginate(articles)


add_pagination(app)


@app.post("/articles/", response_model=schemas.Articles)
def create_article(
    articles: schemas.Articles, db: Session = Depends(get_db)
):
    db_article = crud.get_article(db, id=articles.id)
    if db_article:
        raise HTTPException(
            status_code=400, detail="Article already registered"
        )
    return crud.create_article(db=db, articles=articles)


@app.delete("/articles/{id}")
def delete_article(id: int, db: Session = Depends(get_db)):
    delete = crud.delete_article(db, id=id)
    if delete:
        return {"message": "Article deleted"}
    else:
        raise HTTPException(
            status_code=400, detail="Failed to delete article"
        )


@app.put("/articles/{id}", response_model=schemas.Articles)
def update_article(
    articles: schemas.Articles,
    id: int,
    db: Session = Depends(get_db),
):

    db_article = crud.get_article(db, id=articles.id)

    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    update = crud.update_article(db=db, id=id, articles=articles)
    return update
