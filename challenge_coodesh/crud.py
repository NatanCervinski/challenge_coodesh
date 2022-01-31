from sqlalchemy.orm import Session
from challenge_coodesh.db import models, schemas


def insert_element(id, elements):
    element_dict = elements.dict()
    element_dict["id_article"] = id
    return element_dict


def get_article(db: Session, id: int):
    article = (
        db.query(models.Articles)
        .filter(models.Articles.id == id)
        .first()
    )
    return article


def get_articles(db: Session):
    articles = db.query(models.Articles).all()
    return articles


def create_article(db: Session, articles: schemas.ArticlesCreate):
    launches = articles.launches
    events = articles.events
    articles_dict = articles.dict()
    del articles_dict["launches"]
    del articles_dict["events"]
    db_articles = models.Articles(**articles_dict)
    db.add(db_articles)
    for i in launches:
        db_launches = models.Launches(
            **insert_element(articles_dict["id"], i)
        )
        db.add(db_launches)
    for i in events:
        db_events = models.Events(
            **insert_element(articles_dict["id"], i)
        )
        db.add(db_events)
    db.commit()
    db.refresh(db_articles)
    return db_articles


def delete_article(db: Session, id: int):
    delete = (
        db.query(models.Articles)
        .filter(models.Articles.id == id)
        .delete()
    )
    db.commit()
    return delete


def update_article(db: Session, id: int, articles: schemas.Articles):
    update = (
        db.query(models.Articles)
        .filter(models.Articles.id == id)
        .update(
            {
                column: getattr(articles, column)
                for column in models.Articles.__table__.columns.keys()
            },
            synchronize_session=False,
        )
    )

    db.commit()
    return (
        db.query(models.Articles)
        .filter(models.Articles.id == id)
        .first()
    )
