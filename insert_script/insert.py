import requests

# from mysql.connector import connect, Error
import psycopg2


class Insert:
    def __init__(
        self,
        limit: int,
        execute_count: bool,
        host: str,
        database: str,
        user: str,
        password: str,
        port: int,
    ):
        self.execute_count = execute_count
        self.limit = limit
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def get_results(self):
        if self.execute_count:
            url_count = (
                "https://api.spaceflightnewsapi.net/v3/articles/count"
            )
            r = requests.get(url_count)
            self.limit = r.json()
        else:
            pass

        url = f"https://api.spaceflightnewsapi.net/v3/articles?_limit={self.limit}"
        headers = {"accept": "application/json"}

        r = requests.get(url, headers=headers)
        result = r.json()
        return result

    def make_sql(self, result):
        list_launches = []
        list_events = []
        for i in result:
            sql = "INSERT INTO articles (id, title, url, imageUrl, newsSite, summary, publishedAt, updatedAt, featured) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            params = (
                i["id"],
                i["title"],
                i["url"],
                i["imageUrl"],
                i["newsSite"],
                i["summary"],
                i["publishedAt"],
                i["updatedAt"],
                i["featured"],
            )

            if len(i["launches"]) > 0:
                for j in i["launches"]:
                    sql_launches = (
                        "INSERT INTO launches values(%s, %s, %s)"
                    )
                    param_launches = j["id"], j["provider"], i["id"]
                    list_launches = [sql_launches, param_launches]
            if len(i["events"]) > 0:
                for j in i["events"]:
                    sql_events = "INSERT INTO events values(%s, %s, %s)"
                    param_events = j["id"], j["provider"], i["id"]
                    list_events = [sql_events, param_events]
            yield [[sql, params], list_launches, list_events]

    def insert_all(self, sqls):

        try:
            with psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("DROP TABLE IF EXISTS launches")
                    cursor.execute("DROP TABLE IF EXISTS events")
                    cursor.execute("DROP TABLE IF EXISTS articles")
                    cursor.execute(
                        """
                    CREATE TABLE IF NOT EXISTS articles (
                    id integer PRIMARY KEY,
                    featured boolean,
                    url text,
                    imageUrl text,
                    newsSite text,
                    summary text,
                    publishedAt text,
                    title text,
                    updatedAt text
                    );
                    """
                    )
                    cursor.execute(
                        """
                    CREATE TABLE IF NOT EXISTS launches(
                    id text,
                    provider text,
                    id_article integer,
                    key_id serial,
                    PRIMARY KEY(key_id, id, id_article),
                    FOREIGN KEY (id_article) REFERENCES articles(id) on delete cascade
                    )
                    """
                    )
                    cursor.execute(
                        """
                    CREATE TABLE IF NOT EXISTS events(
                    id text,
                    provider text,
                    id_article integer,
                    key_id serial,
                    PRIMARY KEY(key_id, id, id_article),
                    FOREIGN KEY (id_article) REFERENCES articles(id) on delete cascade
                    )
                    """
                    )
                    cursor.execute("DELETE FROM launches")
                    cursor.execute("DELETE FROM events")
                    cursor.execute("DELETE FROM articles")
                    for i in sqls:
                        # articles
                        cursor.execute(i[0][0], i[0][1])
                        # launches
                        if i[1]:
                            cursor.execute(i[1][0], i[1][1])
                        # events
                        if i[2]:
                            cursor.execute(i[2][0], i[2][1])
                    connection.commit()
        except Exception as e:
            print(e)
