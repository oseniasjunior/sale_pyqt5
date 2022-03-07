import psycopg2
from psycopg2 import DatabaseError


class Database:
    def __init__(self):
        self.dbname = 'sale'
        self.host = '127.0.0.1'
        self.user = 'postgres'
        self.password = '123456'
        self.connection = None

    def search(self, tablename: str, parameters: dict = None, many=True):
        try:
            with psycopg2.connect(host=self.host, database=self.dbname, user=self.user, password=self.password) as conn:
                with conn.cursor() as cursor:
                    if parameters is None:
                        default_sql = f'SELECT * FROM {tablename} ORDER BY id DESC'
                    else:
                        conditions = ''
                        for k, v in parameters.items():
                            conditions += f'{conditions}{k} = {v} AND '
                        conditions.rstrip('AND ')

                        default_sql = f'SELECT * FROM {tablename} WHERE {conditions} ORDER BY id DESC'

                    cursor.execute(default_sql)
                    result = cursor.fetchall()
                    columns = [column[0] for column in cursor.description]
                    rows = [dict(zip(columns, row)) for row in result]
                    return rows if many else rows[0] if len(rows) > 0 else None

        except DatabaseError as ex:
            print(f'Ocorreu um erro ao comunicar com o banco de dados. {ex}')
