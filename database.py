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
            SELECT VOORLETTERS
                  ,ROEPNAAM
                  ,TUSSENVOEGSEL
                  ,ACHTERNAAM
                  ,GEBOORTEDATUM
                  ,GESLACHT
                  ,TELEFOONNUMMER1
                  ,TELEFOONNUMMER2
                  ,EMAIL
                  ,GEBOORTEPLAATS
                  ,BURGELIJKESTAAT
                  ,PARTNERTUSSENVOEGSEL
                  ,PARTNERACHTERNAAM
                  ,NAAMGEBRUIK
                  ,INSCHRIJFDATUM
                  ,UITSCHRIJFDATUM
                  ,BSN
                  ,PATIENT_DIRECT_ID
            FROM persoon_hstage
            INNER JOIN patient_hstage on patient_hstage.id = persoon_hstage.patient_direct_id
            WHERE persoon_hstage._id = {}
        """.format(id)
        rows = self.execute_read(sql)

        row = {}

        row['voorletters'] = rows[0][0]
        row['roepnaam'] = rows[0][1]
        row['tussenvoegsel'] = rows[0][2]
        row['achternaam'] = rows[0][3]
        row['geboortedatum'] = rows[0][4]
        row['geslacht'] = rows[0][5]
        row['telefoonnummer1'] = rows[0][6]
        row['telefoonnummer2'] = rows[0][7]
        row['email'] = rows[0][8]
        row['geboorteplaats'] = rows[0][9]
        row['burgelijkestaat'] = rows[0][10]
        row['partnertussenvoegsel'] = rows[0][11]
        row['partnerachternaam'] = rows[0][12]
        row['naamgebruik'] = rows[0][13]
        row['inschrijfdatum'] = rows[0][14]
        row['uitschrijfdatum'] = rows[0][15]
        row['bsn'] = rows[0][16]
        row['patientid'] = rows[0][17]

        return row

