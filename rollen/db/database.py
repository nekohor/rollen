from sqlalchemy import create_engine
import pymysql
import pandas as pd
import logging
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
        self.wheres = []
        return self

    def select(self, fields):
        if isinstance(fields, list):
            self.fields = ",".join([str(x) for x in fields])
        elif isinstance(fields, str):
            self.fields = fields
        elif fields == "*":
            self.fields = "*"
        else:
            raise Exception("unknown fields in DataBase#select()")
        return self

    def where(self, key, operator=None, value=None):

        if not operator and not value:
            self.onlykey(key)
        elif operator and not value:
            self.isequal(key, operator)
        elif not operator and value:
            self.isequal(key, value)
        elif operator and value:
            self.wheres.append([key, operator, value])
        else:
            raise Exception("other circums in where()")

        return self

    def onlykey(self, key):
        """ no return """

        if isinstance(key, list):
            self.add_conditions_to_wheres(key)
        else:
            raise Exception("wrong type of one param key")

    def add_conditions_to_wheres(self, conditions):
        """ no return """

        for elems in conditions:
            if isinstance(elems, list):
                raise Exception("type of condition not list")

            if len(elems) != 3:
                raise Exception("count of condition list not equal to 3")

            for elem in elems:
                if isinstance(elem, str):
                    pass
                else:
                    raise Exception("type of elem in condition not str")

        for key, oper, val in conditions:
            self.wheres.append([key, oper, val])

    def isequal(self, key, value):
        """ no return """

        if isinstance(key, str):
            pass
        else:
            raise Exception("wrong type of key, str needed")

        if isinstance(value, list):
            self.wheres.append([key, "in", value])
        else:
            self.wheres.append([key, "=", value])

    def operator_strategy(self, key, oper, val):
        if oper == "=" or oper == "==":
            return "{} = {}".format(key, val)
        elif oper == "in" or oper == "isin":
            return "{} IN ({})".format(key, ",".join(val))
        elif oper == "!=" or oper == "<>":
            return "{} <> {}".format(key, val)
        elif oper == ">":
            return "{} > {}".format(key, val)
        elif oper == "<":
            return "{} < {}".format(key, val)
        elif oper == ">=":
            return "{} >= {}".format(key, val)
        elif oper == "<=":
            return "{} <= {}".format(key, val)
        elif oper == "regexp" or oper == "re":
            return "{} REGEXP ({})".format(key, ",".join(val))
        else:
            raise Exception("unknown operator")

    def get(self):

        if self.fields:
            pass
        else:
            self.fields = "*"

        conditions = []
        for key, oper, val in self.wheres:
            conditions.append(self.operator_strategy(key, oper, val))

        self.query = (
            "SELECT {} FROM `{}` WHERE `{}` {} {}").format(
            self.fields,
            self.table_name,
            "AND".join(conditions)
        )
        logging.info(self.query)

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
