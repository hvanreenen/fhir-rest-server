import time
from typing import List, Any

import psycopg2
from sqlalchemy import create_engine



class Database():
    def __init__(self, config = {}) -> None:
        conn_string = config['conn_string']
        self.engine = create_engine(conn_string)


    def execute(self, sql: str, log_message: str = ''):
        self.log('-- ' + log_message.upper())
        self.log(sql)

        start = time.time()
        connection = self.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        rowcount = cursor.rowcount
        self.log('-- duur: ' + str(time.time() - start) + '; aantal rijen:' + str(cursor.rowcount))
        self.log('-- =============================================================')
        cursor.close()
        return rowcount


    def execute_returning(self, sql: str, log_message: str = ''):
        self.log('-- ' + log_message.upper())
        self.log(sql)

        start = time.time()
        connection = self.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        result = cursor.fetchall()
        self.log('-- duur: ' + str(time.time() - start) + '; aantal rijen:' + str(cursor.rowcount))
        self.log('-- =============================================================')
        cursor.close()
        return result


    def execute_read(self, sql, log_message='') -> List[List[Any]]:
        self.log('-- ' + log_message.upper())
        self.log(sql)

        start = time.time()
        # plan = text(sql)
        # result = engine.execute(sql)

        connection = self.engine.raw_connection()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()

        self.log('-- duur: ' + str(time.time() - start) + '; aantal rijen:' + str(cursor.rowcount))
        self.log('-- =============================================================')
        cursor.close()
        return result

    def log(self, msg):
        print(msg)

    def get_resource(self, res_name, id=''):
        sql = """SELECT * FROM res WHERE type = '{}'""".format(res_name)
        if id:
            sql += """ AND id = {}""".format(id)
        rows = self.execute_read(sql)
        json = ''
        for row in rows:
            json = row[2]
        return json

    def insert_resource(self, res_name, json=''):
        json = str(json).replace("'", '"')
        sql = """INSERT INTO res ("type", json)
        VALUES ('{}', '{}')""".format(res_name, str(json).replace("'", '"'))
        self.execute(sql)

    def update_resource(self, id, json=''):
        json = str(json).replace("'", '"')
        sql = """UPDATE res SET json = '{}' WHERE id = {}""".format(json, id)
        self.execute(sql)

    def delete_resource(self, id):
        sql = """DELETE from res WHERE id = {}""".format(id)
        self.execute(sql)

    def read_patient(self, id):

        sql = """
            SELECT achternaam
            FROM persoon_hstage
            WHERE _id = {}
        """.format(id)
        rows = self.execute_read(sql)
        row = {}
        row['achternaam'] = rows[0][0]


        return row

