import insert
import click


@click.command()
@click.option(
    "--limit",
    default=1000,
    help="limit parameter used in /articles (get all articles)",
)
@click.option(
    "--execute_count",
    is_flag=True,
    help="With this argument, the limit will assume the number of /articles/count. Warning: the default database has a number max of rows equal to 10000, just use it if you are using a local database.",
)
@click.option(
    "--host",
    default="ec2-44-193-188-118.compute-1.amazonaws.com",
    help="Parameter to database, default Heroku",
)
@click.option(
    "--database",
    default="d9nqc80d3a42ha",
    help="Parameter to database, default Heroku",
)
@click.option(
    "--user",
    default="pgxdmopnfgypeb",
    help="Parameter to database, default Heroku",
)
@click.option(
    "--password",
    default="47a47dfd40d363698ecd938e80eecbce5c83101ff607e7cdc29ad5f3529a5aea",
    help="Parameter to database, default Heroku",
)
@click.option(
    "--port", default=5432, help="Parameter to database, default Heroku"
)
def populate_database(
    limit, execute_count, host, database, user, password, port
):
    ins = insert.Insert(
        limit, execute_count, host, database, user, password, port
    )
    result = ins.get_results()
    sqls = ins.make_sql(result)
    ins.insert_all(sqls)


if __name__ == "__main__":
    populate_database()
