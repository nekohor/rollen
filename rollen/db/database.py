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

        if isinstance(key, str):
            self.key = key
        else:
            raise Exception("key in where() is not str")

        self.operator, self.value = self.get_oper_val(operator, value)
        return self

    def get_oper_val(self, operator, value):

        if not operator and not value:
            return None, None
        elif operator and not value:
            oper, val = self.isequal(operator)
        elif not operator and value:
            oper, val = self.isequal(value)
        elif operator and value:
            oper, val = self.compare(operator, value)
        else:
            raise Exception("other circums in operator_for_where()")

        return oper, val

    def compare(self, operator, value):

        if operator == "=" or operator == "==":
            oper, val = self.isequal(value)
        elif operator == "!=" or operator == "<>":
            oper, val = self.notequal(value)
        elif operator == ">" or operator == "<":
            oper, val = operator, value
        elif operator == ">=" or operator == "<=":
            oper, val = operator, value
        elif operator == "in":
            oper, val = self.isin(value)
        elif operator == "regexp":
            oper, val = self.regexp(value)
        return oper, val

    def isequal(self, value):
        if isinstance(value, list):
            return self.isin()
        else:
            return "=", value

    def notequal(self, value):
        if isinstance(value, list):
            return self.notin()
        else:
            return "<>", value

    def isin(self, elems):
        oper = "IN"

        if isinstance(elems, list):
            pass
        else:
            raise Exception("wrong type of elems in isin()")

        val = "(" + ",".join([str(e) for e in elems]) + ")"

        return oper, val

    def notin(self, elems):
        oper = "NOT IN"

        if isinstance(elems, list):
            pass
        else:
            raise Exception("wrong type of elems in notin()")

        val = "(" + ",".join([str(e) for e in elems]) + ")"

        return oper, val

    def regexp(self, pattern):
        oper = "REGEXP"

        if isinstance(pattern, str):
            pass
        else:
            raise Exception("wrong type of pattern in regexp()")

        val = pattern

        return oper, val

    def get(self):

        if self.fields:
            pass
        else:
            self.fields = "*"

        self.query = (
            "SELECT {} FROM `{}` WHERE `{}` {} {}").format(
            self.fields,
            self.table_name,
            self.key,
            self.operator,
            self.value
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
