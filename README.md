# This is a challenge by Coodesh

An API RESTful project based on [Spaceflight News API].

## To do this were used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/14/orm/)
- [PostgreSQL](https://www.postgresql.org/)
- [pydantic](https://pydantic-docs.helpmanual.io/)
- [Click](https://click.palletsprojects.com/en/8.0.x/)

## Requeriments
- [pip][pip-installation]

## Installation
```bash
$ pip install poetry
$ poetry install
```
## Running
```bash
$ poetry run poetry run uvicorn challenge_coodesh.main:app --reload --host 0.0.0.0
```
## Documentation
A live documentation of api is generated by FastAPI on [http://127.0.0.1:8000/docs], there you can check all the endpoint and their parameters.

## Populating the database
On insert_scipt you can run:
```bash
$ poetry run python run.py
```
## Warning about database
As a free database hosted on [Heroku] there is a limit of 10000 rows, so the default amount of Articles to populate the database is 1000, you can change this with the parameter "--limit" when running "run.py" (For more information, please run "poetry run python run.py --help")

## Installing using Docker
```bash
$ docker image build -t coodesh:1.0
$ docker container run -d -p 8000:8000 coodesh:1.0
```

## Testing
To run the tests you can just execute:
```bash
$ poetry run pytest
```
The tests use another database.




[Spaceflight News API]: https://api.spaceflightnewsapi.net/v3/documentation
[FastAPI]:https://fastapi.tiangolo.com/
[SQLAlchemy ORM]: https://docs.sqlalchemy.org/en/14/orm/
[PostgreSQL]: https://www.postgresql.org/
[pip-installation]: https://pip.pypa.io/en/stable/cli/pip_install/
[http://127.0.0.1:8000/docs]: http://127.0.0.1:8000/docs
[Heroku]: https://www.heroku.com/
[http://172.17.0.4:8000]: http://172.17.0.4:8000

