import pymysql
import pandas as pd
import numpy as np

import logging
from rollen.database import DataBaseManager


class QueryBuilder():

    def __init__(self, db_tag):

        self.engines = DataBaseManager.get_database(db_tag)

        self.line = None
        self.fields = "*"
        self.wheres = []
        self.query = None

    def millline(self, line):
        self.line = str(line)
        return self

    def table(self, table_name):
        self.table_name = table_name
        return self

    def to_str(self, x):
        return str(x).strip()

    def quote_field(self, x):
        return "`{}`".format(self.to_str(x))

    def quote_string(self, x):
        return "'{}'".format(self.to_str(x))

    def quote(self, x):
        if isinstance(x, str):
            return self.quote_string(x)
        else:
            return self.to_str(x)

    def select(self, fields):

        if isinstance(fields, list):
            self.fields = ",".join([self.quote_field(x) for x in fields])
        elif isinstance(fields, str):
            self.fields = self.quote_field(fields)
        elif fields == "*":
            self.fields = "*"
        else:
            raise Exception("unknown fields in QueryBuilder::select")
        return self

    def where(self, *params):

        if len(params) == 0:
            self.where_zero()
        if len(params) == 1:
            self.where_single(params[0])
        elif len(params) == 2:
            self.where_dual(params[0], params[1])
        elif len(params) == 3:
            self.wheres = []
            self.wheres.append([params[0], params[1], params[2]])
        else:
            raise Exception("wrong size of params for where()")

        return self

    def where_zero(self):
        self.wheres = []

    def where_single(self, key):
        """ no return """

        if isinstance(key, list):
            self.add_conds_to_wheres(key)
        else:
            raise Exception("wrong type of one param in QueryBuilder::where")

    def add_conds_to_wheres(self, conds):
        """ conds is a list of lists """
        self.wheres = []

        for cond in conds:

            if not isinstance(cond, list):
                raise Exception("type of cond is not list")

            if len(cond) == 0:
                self.wheres = []
            elif len(cond) == 1:
                raise Exception("[[x] [y] [z]] has no meaning")
            elif len(cond) == 2:
                self.wheres.append([cond[0], "=", cond[1]])
            elif len(cond) == 3:
                self.wheres.append([cond[0], cond[1], cond[2]])

    def where_dual(self, key, value):
        """ no return """
        self.wheres = []

        if isinstance(value, list):
            self.wheres.append([key, "in", value])
        else:
            self.wheres.append([key, "=", value])

    def render_where_clause(self, key, oper, val):
        if oper == "=" or oper == "==":
            return "{} = {}".format(key, self.quote(val))
        elif oper == "in" or oper == "isin":

            v = " , ".join([self.quote(x) for x in val])
            return "{} IN({})".format(key, v)

            # another implementation
            # s = " OR ".join(["{} = {}".format(key, str(v)) for v in val])
            # return s ; or use FIND_IN_SET()

        elif oper == "!=" or oper == "<>":
            return "{} <> {}".format(key, self.quote(val))
        elif oper == ">":
            return "{} > {}".format(key, self.quote(val))
        elif oper == "<":
            return "{} < {}".format(key, self.quote(val))
        elif oper == ">=":
            return "{} >= {}".format(key, self.quote(val))
        elif oper == "<=":
            return "{} <= {}".format(key, self.quote(val))
        elif oper == "regexp" or oper == "re":
            return "{} REGEXP {}".format(key, self.quote(val))
        else:
            raise Exception("unknown operator in render_where_clause")

    def get(self):

        conds = []
        for key, oper, val in self.wheres:
            conds.append(
                self.render_where_clause(self.quote_field(key), oper, val))

        wheres_len = len(self.wheres)
        if wheres_len > 0:
            self.query = (
                "SELECT {} FROM `{}` WHERE {};").format(
                self.fields,
                self.table_name,
                " AND ".join(conds)
            )
        else:
            self.query = (
                "SELECT {} FROM `{}`;").format(
                self.fields,
                self.table_name
            )

        logging.info(self.query)
        df = pd.read_sql(self.query, self.engines[self.line])

        if df.shape[0] == 0:
            # raise Exception("the data cannot find in datebase")
            return df

        df.index = df["coil_id"]
        df.sort_index(inplace=True)
        df.drop_duplicates("coil_id", "first", inplace=True)

        return df
