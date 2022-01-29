from pydantic import BaseModel


class LaunchesBase(BaseModel):
    id: str
    provider: str


class Launches(LaunchesBase):
    class Config:
        orm_mode = True


class LaunchesCreate(LaunchesBase):
    # id_article: int
    pass


class EventsBase(BaseModel):
    id: str
    provider: str


class Events(EventsBase):
    class Config:
        orm_mode = True


class EventsCreate(EventsBase):
    # id_article: int
    pass


class ArticlesBase(BaseModel):
    id: int
    featured: bool
    url: str
    imageurl: str
    newssite: str
    summary: str
    publishedat: str
    title: str
    updatedat: str
    launches: list[Launches] = []
    events: list[Events] = []


class Articles(ArticlesBase):
    class Config:
        orm_mode = True


class ArticlesCreate(ArticlesBase):
    pass
