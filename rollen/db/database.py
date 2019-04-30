from sqlalchemy import create_engine
import pymysql
import pandas as pd
from .creator import Creator


def use(line):
    db = DataBase(line)
    return db


class DataBase():

    def __init__(self, line):
        self.line = line

        self.address = "localhost"
        self.port = 3306

        self.user = "root"
        self.password = ""

        self.db_name = "coil_{}"
        self.charset = "utf8mb4"

        # 将数据写入mysql的数据库，
        # 但需要先通过sqlalchemy.create_engine建立连接,
        # 且字符编码设置为utf8mb4，否则有些latin字符不能处理
        self.engine = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}?charset={}'
            .format(self.user, self.password,
                    self.address, self.port,
                    self.db_name.format(self.line), self.charset)
        )

        self.conn = pymysql.connect(
            self.address,
            self.user, self.password,
            self.db_name.format(self.line))

    def table(self, table_name):
        self.table_name = table_name
        return self

    def select(self, fields):
        if isinstance(fields, list):
            self.fields = ",".join([str(x) for x in fields])
        elif fields == "*":
            self.fields = "*"
        else:
            raise Exception("unknown fields in DataBase#select()")
        return self

    def where(self, col_name):
        self.col_name = col_name
        return self

    def isin(self, elem_list):
        self.elems = ",".join([str(e) for e in elem_list])
        self.query = (
            " SELECT {} FROM `{}` WHERE `{}` IN({})").format(
            self.fields,
            self.table_name,
            self.col_name,
            self.elems
        )
        return self

    def regexp(self, pattern):
        self.pattern = pattern
        self.query = (
            " SELECT {} FROM `{}` WHERE (`{}` REGEXP '{}')").format(
            self.fields,
            self.table_name,
            self.col_name,
            self.pattern
        )
        return self

    def get(self):
        df = pd.read_sql(self.query, self.engine)
        if df.shape[0] == 0:
            raise Exception("the data cannot find in datebase")
        df.index = df["coil_id"]
        return df

    def drop(self, table_name):
        cursor = self.conn.cursor()
        sql = "DROP TABLE IF EXISTS {}".format(self.table_name)
        cursor.execute(sql)

    def remove_dupilicates(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS tmp_table")
        cursor.execute("create table tmp_table as SELECT "
                       "DISTINCT * FROM {}".format(table_name))
        cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
        cursor.execute("RENAME TABLE tmp_table TO {}".format(table_name))

    def create(self, table_name):
        Creator().create(self.conn, table_name)

    def rebuild(self, table_name):
        self.drop(table_name)
        self.create(table_name)

    # def read_by_elems(self, table_name, col_name, elem_list):
    #     query = (
    #         " SELECT * FROM `{}` WHERE `{}` IN({})").format(
    #         table_name,
    #         col_name,
    #         ",".join([str(e) for e in elem_list])
    #     )
    #     return self.read_by_sql(query)

    # def read_by_regexp(self, table_name, col_name, regexp):
    #     query = (
    #         " SELECT * FROM `{}` WHERE (`{}` REGEXP '{}')").format(
    #         table_name,
    #         col_name,
    #         regexp
    #     )
    #     return self.read_by_sql(query)
