from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Articles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    featured = Column(Boolean, index=True)
    url = Column(String)
    imageurl = Column(String)
    newssite = Column(String)
    summary = Column(String)
    publishedat = Column(String)
    title = Column(String)
    updatedat = Column(String)
    launches = relationship(
        "Launches",
        # cascade="all,delete",
        backref="launches",
        passive_deletes=True,
    )
    events = relationship(
        "Events",
        # cascade="all,delete",
        backref="events",
        passive_deletes=True,
    )


class Launches(Base):
    __tablename__ = "launches"

    key_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String, primary_key=True, index=True)
    provider = Column(String)
    id_article = Column(
        Integer,
        ForeignKey(Articles.id, ondelete="CASCADE"),
        primary_key=True,
    )


class Events(Base):
    __tablename__ = "events"

    key_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String, primary_key=True, index=True)
    provider = Column(String)
    id_article = Column(
        Integer,
        ForeignKey(Articles.id, ondelete="CASCADE"),
        primary_key=True,
    )
