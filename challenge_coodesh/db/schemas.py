from pydantic import BaseModel


class LaunchesBase(BaseModel):
    id: str
    provider: str


class Launches(LaunchesBase):
    class Config:
        orm_mode = True


class LaunchesCreate(LaunchesBase):
    id_provider: int


class EventsBase(BaseModel):
    id: str
    provider: str
    # id_article: int


class Events(EventsBase):
    class Config:
        orm_mode = True


class EventsCreate(EventsBase):
    id_provider: int


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
